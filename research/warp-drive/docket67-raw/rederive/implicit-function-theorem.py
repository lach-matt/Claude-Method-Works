#!/usr/bin/env python3
"""DOCKET 67 -- audit of the implicit function theorem (IFT) as linstab.py uses it.

Source statement (de Oliveira, arXiv:1212.2066, Theorem 1, one equation):
  F : Omega -> R of class C^1 on an open Omega in R^n x R, F(a,b) = 0 and
  dF/dy(a,b) > 0  ==>  open X ni a, open Y ni b: for each x in X a UNIQUE
  y = f(x) in Y with F(x, f(x)) = 0; f(a) = b; f is C^1 with
  df/dx_j = -F_{x_j}/F_y.

Tree's use (linstab.py:164-166, 345-347, 367-369, 959-965): x = alpha~^S_1,
y = gamma, F = GMMPS (5.3)
  F_S(gamma) = gamma (a - gamma)^2 J(gamma) - (b_0 + b_1 gamma + b_2 gamma^2),
  a = 2m^2/(6xi-1), b_0 = -alpha 4m^4/(6(1/6-xi)^2), b_1 = -(2/kappa)/(6(1/6-xi)^2)
(GMMPS (5.2), read at source, 2604.01047 v1 pp. 59-60), J their (4.17).

Checks R1-R9 below.  Nothing in research/warp-drive is touched.
"""
import sys
import sympy as sp
import mpmath as mp
import z3

PASS, FAIL = [], []


def chk(name, got, want=True):
    ok = (got == want)
    (PASS if ok else FAIL).append(name)
    print(("PASS " if ok else "FAIL ") + name + ("" if ok else "   got %r want %r" % (got, want)))


# ---------------------------------------------------------------- symbols
m, kap = sp.symbols('m kappa', positive=True)
al, xi, g, b2 = sp.symbols('alpha xi gamma b_2', real=True)
M = sp.Symbol('M', positive=True)
c = 6 * (sp.Rational(1, 6) - xi) ** 2
a = 2 * m ** 2 / (6 * xi - 1)
b0 = -al * 4 * m ** 4 / c
b1 = -(2 / kap) / c
rho = sp.sqrt(1 - 4 * m ** 2 / M) / (16 * sp.pi ** 2 * M)          # GMMPS (4.5)
Jf = sp.Function('J')
F = g * (a - g) ** 2 * Jf(g) - (b0 + b1 * g + b2 * g ** 2)             # GMMPS (5.3)

# R1: J and its derivatives at 0 are finite (J real-analytic on (-inf, 4m^2) ni 0)
Jn = [sp.simplify(sp.factorial(n) * sp.integrate(rho / M ** (n + 1), (M, 4 * m ** 2, sp.oo)))
      for n in range(3)]
chk("R1 J(0) = INT rho/M = 1/(96 pi^2 m^2)", sp.simplify(Jn[0] - 1 / (96 * sp.pi ** 2 * m ** 2)), 0)
chk("R1 J'(0), J''(0) finite and positive (Taylor coefficients of an analytic J at 0)",
    all(v.is_finite and v.is_positive for v in Jn[1:]), True)
print("     J'(0) =", Jn[1], "  J''(0) =", Jn[2])

# R2: the IFT hypotheses at (alpha, gamma) = (0, 0)
F0 = F.subs(g, 0)
Fg = sp.diff(F, g).subs(g, 0).subs(Jf(0), Jn[0])
Fa = sp.diff(F, al).subs(g, 0)
chk("R2 F(alpha=0, gamma=0) = 0", sp.simplify(F0.subs(al, 0)), 0)
chk("R2 F_gamma(0,0) (1-6xi)^2 kappa = 12 + kappa m^2/(24 pi^2)",
    sp.simplify(Fg * (1 - 6 * xi) ** 2 * kap - (12 + kap * m ** 2 / (24 * sp.pi ** 2))), 0)
chk("R2 F_gamma(0,0) independent of b_2 and alpha", (sp.diff(Fg, b2), sp.diff(Fg, al)), (0, 0))
# z3: F_gamma(0,0) > 0 for every kappa > 0, m > 0, xi != 1/6 (the sign the tree needs)
K, Mm, X, P = z3.Reals('K Mm X P')
num = 12 + K * Mm * Mm / (24 * P * P)
den = K * (1 - 6 * X) * (1 - 6 * X)
s = z3.Solver()
s.add(K > 0, Mm > 0, X != z3.RealVal(1) / 6, P > 3, P < 4, z3.Not(num / den > 0))
chk("R2 z3: F_gamma(0,0) > 0 for all kappa>0, m>0, xi != 1/6 (unsat of negation)",
    s.check() == z3.unsat, True)
s2 = z3.Solver()
s2.add(K < 0, Mm > 0, X == 0, P > 3, P < 4, num / den < 0)
chk("R2 CONTROL z3: kappa < 0 can flip the sign (sat) -- G > 0 is a used hypothesis",
    s2.check() == z3.sat, True)
chk("R2 F at xi = 1/6 is undefined (a, b_0, b_1 singular) -- xi != 1/6 is a used hypothesis",
    sp.limit(sp.Abs(b1), xi, sp.Rational(1, 6)) == sp.oo, True)

# R3: the IFT slope and the tree's first-order formula
slope = sp.simplify(-Fa / Fg)
target = -2 * kap * m ** 4 / (1 + kap * m ** 2 / (288 * sp.pi ** 2))
chk("R3 f'(0) = -F_alpha/F_gamma = -2 kappa m^4/(1 + kappa m^2/(288 pi^2)) (tree's formula)",
    sp.simplify(slope - target), 0)
chk("R3 f'(0) is xi-independent", sp.simplify(sp.diff(slope, xi)), 0)
chk("R3 f'(0) < 0 for kappa, m > 0", sp.simplify(target).is_negative, True)
chk("R3 GMMPS 5.3: -b_0/b_1 = -2 kappa alpha m^4 = -16 pi G alpha m^4 (J dropped)",
    sp.simplify(-b0 / b1 + 2 * kap * al * m ** 4), 0)

# R4: F is AFFINE in alpha, so f(alpha) = 0 <=> F(alpha, 0) = 0 <=> alpha = 0 on ALL of X
chk("R4 d^2F/dalpha^2 = 0 (F affine in alpha)", sp.diff(F, al, 2), 0)
chk("R4 F(alpha, 0) = -b_0 vanishes only at alpha = 0", sp.solve(sp.Eq(F0, 0), al), [0])
# => by uniqueness in Y: the branch zero equals 0 iff alpha = 0; f continuous and nonzero on
#    X \ {0} (an interval) keeps one sign on each side, fixed by f'(0) < 0: growing side iff alpha > 0.

# R5: numeric -- the branch root at a generic point, full F with J from the (4.5) integral
mp.mp.dps = 40


def Jnum(gv, mv=1):
    f = lambda Mv: mp.sqrt(1 - 4 * mv ** 2 / Mv) / (16 * mp.pi ** 2 * Mv) / (Mv - gv)
    return mp.quad(f, [4 * mv ** 2, 8 * mv ** 2, mp.inf])


def FS(gv, alv, kv, xv, bv, mv=1):
    cv = 6 * (mp.mpf(1) / 6 - xv) ** 2
    av = 2 * mv ** 2 / (6 * xv - 1)
    return gv * (av - gv) ** 2 * Jnum(gv, mv) - (-alv * 4 * mv ** 4 / cv - (2 / kv) / cv * gv + bv * gv ** 2)


kv, xv, bv = mp.mpf('0.3'), mp.mpf(0), mp.mpf(-1)
lin = lambda alv: -2 * kv * alv / (1 + kv / (288 * mp.pi ** 2))
signs, err2 = [], []
for alv in (mp.mpf('1e-3'), mp.mpf('-1e-3'), mp.mpf('1e-4'), mp.mpf('-1e-4')):
    r = mp.findroot(lambda gv: FS(gv, alv, kv, xv, bv), lin(alv))
    signs.append((alv > 0, r < 0))
    err2.append(abs(r - lin(alv)) / alv ** 2)
chk("R5 numeric branch root < 0 iff alpha > 0 (m=1, kappa=0.3, xi=0, b2=-1)",
    all(p == q for p, q in signs), True)
chk("R5 |root - first-order| / alpha^2 bounded (O(alpha^2) remainder)",
    max(err2) < 10 and abs(err2[0] - err2[2]) / err2[0] < 0.2, True)
r0 = mp.findroot(lambda gv: FS(gv, 0, kv, xv, bv), mp.mpf('1e-6'))
chk("R5 at alpha = 0 the branch root is gamma = 0 exactly (it EXISTS, and is zero)", abs(r0) < 1e-30, True)

# R6: holomorphic IFT / argument principle -- exactly ONE zero (so no complex pair) in a disk
#     |gamma| < 0.2 at alpha = 1e-3; J analytic there (cut starts at 4m^2 = 4)
mp.mp.dps = 20
alv = mp.mpf('1e-3')
Rd = mp.mpf('0.2')
N = 400
tot = mp.mpf(0)
prev = FS(Rd, alv, kv, xv, bv)
for k in range(1, N + 1):
    z = Rd * mp.expj(2 * mp.pi * k / N)
    cur = FS(z, alv, kv, xv, bv)
    tot += mp.im(mp.log(cur / prev))
    prev = cur
wind = int(mp.nint(tot / (2 * mp.pi)))
chk("R6 winding number of F_S on |gamma| = 0.2 is 1: one zero, real (no conjugate pair near 0)", wind, 1)

# R7: CONTROL -- the hypothesis F_gamma != 0 bites: F = gamma^2 - alpha has no real branch for alpha<0
chk("R7 CONTROL gamma^2 - alpha: F_gamma(0,0)=0 and no real root at alpha=-1e-3 (gamma real)",
    (sp.diff(g ** 2 - al, g).subs(g, 0), sp.solve(g ** 2 + sp.Rational(1, 1000), g)), (0, []))

# R8: how LOCAL is "locally"?  At GMMPS's own point (m = 1, kappa = eps = (m/M_P)^2,
#     alpha = 1/(64 pi^2)) the branch reaches the physical alpha only while the
#     quadratic F_0 + F_1 gamma - b_2' gamma^2 keeps a real root: for b_2 < 0 this is
#     |b_2| <= B* = F_1^2 / (4 F_0) (b_2' includes the J curvature, negligible here).
mp.mp.dps = 160


def eps_from(lam, om, alpha_s1):
    x4 = lam / (6 * om * alpha_s1)         # linstab.gmmps_mass_ev, GMMPS 5.3
    return mp.sqrt(x4)


alpha_phys = 1 / (64 * mp.pi ** 2)
J0v = 1 / (96 * mp.pi ** 2)
J1v = mp.mpf(1) / (16 * mp.pi ** 2) * mp.quad(lambda Mv: mp.sqrt(1 - 4 / Mv) / Mv ** 3, [4, 8, mp.inf])


def Bstar(epsv, xv):
    cv = 6 * (mp.mpf(1) / 6 - xv) ** 2
    av = 2 / (6 * xv - 1)
    F0v = alpha_phys * 4 / cv
    F1v = av ** 2 * J0v + (2 / epsv) / cv
    q = -(2 * av * J0v) + av ** 2 * J1v   # gamma^2 coefficient of gamma (a-gamma)^2 J(gamma)
    # F ~ F0 + F1 g + (q - b2) g^2 ; real root on the growing side iff F1^2 >= 4 F0 (q - b2)
    return F1v ** 2 / (4 * F0v) + q, F0v, F1v


def FS_hp(gv, epsv, xv, bv):
    cv = 6 * (mp.mpf(1) / 6 - xv) ** 2
    av = 2 / (6 * xv - 1)
    Jv = J0v + J1v * gv          # |gamma| ~ 1e-60: higher terms below 1e-120 relative
    return gv * (av - gv) ** 2 * Jv - (-alpha_phys * 4 / cv - (2 / epsv) / cv * gv + bv * gv ** 2)


eps_g = eps_from(mp.mpf('7.15e-121'), mp.mpf('0.685'), alpha_phys)   # GMMPS 5.3 inputs
print("     eps = (m/M_P)^2 at GMMPS's point = %s" % mp.nstr(eps_g, 6))
for xv in (mp.mpf(0), mp.mpf(1) / 3):
    B, F0v, F1v = Bstar(eps_g, xv)
    print("     xi = %s : B* = %s" % (mp.nstr(xv, 3), mp.nstr(B, 6)))
    chk("R8 xi=%s: tree's bracket bound |b_2| <= 1e100 lies inside B*" % mp.nstr(xv, 3), B > mp.mpf(10) ** 100, True)
    # just inside B*: a real growing-side root (sign change between g_lin/2 and the fold)
    bin_ = -B * mp.mpf('0.9')
    gfold = -F1v / (2 * (-bin_))                  # vertex of F0 + F1 g - b2 g^2 with b2 < 0
    chk("R8 xi=%s: at b_2 = -0.9 B* F_S changes sign on (g_fold, 0): the branch root exists" % mp.nstr(xv, 3),
        (FS_hp(gfold, eps_g, xv, bin_) < 0, FS_hp(mp.mpf(0), eps_g, xv, bin_) > 0), (True, True))
    bout = -B * mp.mpf('1.1')
    gfold2 = -F1v / (2 * (-bout))
    grid = [gfold2 * mp.mpf(k) / 50 for k in range(0, 201)]
    chk("R8 xi=%s: at b_2 = -1.1 B* F_S > 0 on [4 g_fold, 0]: no real branch root reaches physical alpha"
        % mp.nstr(xv, 3), min(FS_hp(gv, eps_g, xv, bout) for gv in grid) > 0, True)

# R9: DATA -- move the cosmological inputs (Planck 2018 vs SH0ES H0) and recompute B*;
#     the IFT's qualitative conclusion (nonzero iff alpha != 0; sign) does not involve them.
hbar_eVs = mp.mpf('6.582119569e-16')
Mpl_red_eV = mp.mpf('2.435e27')
Mpc_km = mp.mpf('3.0856775814913673e19')


def lam_mp2(H0, OmL):
    Hs = H0 / Mpc_km
    return 3 * OmL * (hbar_eVs * Hs) ** 2 / Mpl_red_eV ** 2


lamP = lam_mp2(mp.mpf('67.4'), mp.mpf('0.6847'))
lamS = lam_mp2(mp.mpf('73.04'), mp.mpf('0.6847'))
print("     Lambda/M_P^2: Planck-2018 H0=67.4 -> %s (GMMPS print 7.15e-121);  SH0ES H0=73.04 -> %s"
      % (mp.nstr(lamP, 4), mp.nstr(lamS, 4)))
chk("R9 GMMPS's 7.15e-121 M_P^2 reproduces from Planck 2018 (H0 = 67.4, Omega_L = 0.6847) to 1%",
    abs(lamP / mp.mpf('7.15e-121') - 1) < 0.01, True)
BS = Bstar(eps_from(lamS, mp.mpf('0.6847'), alpha_phys), mp.mpf(0))[0]
BP = Bstar(eps_from(lamP, mp.mpf('0.6847'), alpha_phys), mp.mpf(0))[0]
print("     B*(xi=0): Planck %s ; SH0ES %s" % (mp.nstr(BP, 4), mp.nstr(BS, 4)))
chk("R9 B* stays >> 1e100 under the H0 move (the local neighbourhood covers the tree's bracket either way)",
    min(BP, BS) > mp.mpf(10) ** 100, True)

print("\n%d PASS, %d FAIL" % (len(PASS), len(FAIL)))
sys.exit(1 if FAIL else 0)
