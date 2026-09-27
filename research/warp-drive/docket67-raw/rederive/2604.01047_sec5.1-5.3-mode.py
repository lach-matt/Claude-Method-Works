#!/usr/bin/env python3
"""DOCKET 67 re-derivation: GMMPS (arXiv 2604.01047 v1) S-sector infrared growing mode,
secs. 5.1-5.3, as research/warp-drive/linstab.py uses it (linstab.py:142-168, 571-598,
942-965).  Nothing is imported from the tree.

Inputs (as restated -- the source could not be re-opened in this stage, see the audit JSON):
  (5.2)  c = 6 (1/6 - xi)^2,  b0 = -4 alpha m^4 / c,  b1 = -(2/kappa)/c,  a = 2 m^2/(6 xi - 1)
  (5.3)  F_S(gamma) = gamma (a - gamma)^2 J(gamma) - (b0 + b1 gamma + b2 gamma^2)
  (4.5)  rho(M) = sqrt(1 - 4m^2/M) / (16 pi^2 M),  J(z) = INT_{4m^2}^inf rho(M)/(M - z) dM
  Thm 3.6: alpha = alpha~^S_1 = 1/(64 pi^2);  5.1: alpha~^S_2 = 0 (kappa = 8 pi G unrenormalised)
  GMMPS 5.3 matching: (m/M_P)^4 = Lambda / (6 Omega alpha M_P^2), Lambda = 7.15e-121 M_P^2, Omega = 0.685

Checks
 K1  -b0/b1 = -2 kappa alpha m^4 = -16 pi G alpha m^4, xi-independent            (sympy)
 K2  J(0) = 1/(96 pi^2 m^2)                                                       (sympy)
 K3  first-order branch root, J KEPT: -2 kappa alpha m^4 / (1 + kappa m^2/(288 pi^2)),
     xi-independent; F_S'(0) (1-6xi)^2 kappa = 12 + kappa m^2/(24 pi^2) > 0 (IFT)   (sympy)
 K4  GLOBAL bracket (new, stronger than the tree's local IFT claim), z3:
     for alpha > 0, kappa > 0, xi != 1/6, J > 0, b2 >= 0:
       F_S(0) > 0  and  F_S(-b0/b1) <= 0  => a real zero in [-b0/b1, 0) = [-2 kappa alpha m^4, 0)
     and that interval lies inside Thm 4.16's (-4m^2, 0) iff kappa m^2 < 2/alpha = 128 pi^2
 K5  exact zero of the full F_S (J by quadrature, mpmath 160 digits) at GMMPS's matched m:
     against -b0/b1 and against the J-kept formula, for xi in {0, 1/3, -1}, b2 in {0, +-1e50, +-1e100}
 K6  where GMMPS's -b0/b1 stops being a good approximation: exact root vs -b0/b1 vs J-kept
     formula at kappa m^2 = 1e-6 ... 1e3 (m = 1 units), b2 = 0, xi = 0 (a first run asserted
     the J-kept form stays within 1 % at 1e3; it does not -- 26.9 % -- and the check now records that)
 K7  "slightly smaller than 0": gamma_0/m^2 and H = sqrt(-gamma_0) at the matched m (eV)
 K8  sign/convention: F_S(-w^2) = -Q(w^2) with Q as restated in linstab (4.30) -> zero at
     gamma_0 < 0 is w^2 = -gamma_0 > 0, growth e^{w t}, w = sqrt(-gamma_0)       (sympy)
 K9  CONTROL: alpha = 0 -> gamma = 0 is an exact root; alpha < 0 -> branch root > 0 (not growing)
Exit 0 iff every check passes.
"""
import sys
import sympy as sp
import mpmath as mp
import z3

ok = True


def chk(name, cond):
    global ok
    print(("PASS " if cond else "FAIL ") + name)
    ok = ok and bool(cond)


# ------------------------------------------------------------------ K1-K3 symbolic
m, kap, al, xi, g, b2 = sp.symbols('m kappa alpha xi gamma b_2', real=True)
mpos, Msym = sp.symbols('mpos M', positive=True)
c = 6 * (sp.Rational(1, 6) - xi) ** 2
b0 = -al * 4 * m ** 4 / c
b1 = -(2 / kap) / c
a = 2 * m ** 2 / (6 * xi - 1)
ratio = sp.simplify(-b0 / b1)
chk("K1 -b0/b1 = -2 kappa alpha m^4", sp.simplify(ratio + 2 * kap * al * m ** 4) == 0)
Gs = sp.Symbol('G', positive=True)
chk("K1 = -16 pi G alpha m^4 at kappa = 8 pi G",
    sp.simplify(ratio.subs(kap, 8 * sp.pi * Gs) + 16 * sp.pi * Gs * al * m ** 4) == 0)
chk("K1 xi-independent", sp.diff(ratio, xi) == 0)

rho = sp.sqrt(1 - 4 * mpos ** 2 / Msym) / (16 * sp.pi ** 2 * Msym)
J0 = sp.simplify(sp.integrate(rho / Msym, (Msym, 4 * mpos ** 2, sp.oo)))
chk("K2 J(0) = 1/(96 pi^2 m^2)", sp.simplify(J0 - 1 / (96 * sp.pi ** 2 * mpos ** 2)) == 0)
J0m = J0.subs(mpos, m)
F0 = -b0
F1 = a ** 2 * J0m - b1                      # d/dgamma [gamma (a-gamma)^2 J] at 0 = a^2 J(0)
groot = sp.simplify(-F0 / F1)
target = -2 * kap * al * m ** 4 / (1 + kap * m ** 2 / (288 * sp.pi ** 2))
chk("K3 first-order branch root (J kept) = -2 kappa alpha m^4/(1 + kappa m^2/(288 pi^2))",
    sp.simplify(groot - target) == 0)
chk("K3 xi-independent with J kept", sp.simplify(sp.diff(groot, xi)) == 0)
chk("K3 F_S'(0) (1-6xi)^2 kappa = 12 + kappa m^2/(24 pi^2)",
    sp.simplify(F1 * (1 - 6 * xi) ** 2 * kap - (12 + kap * m ** 2 / (24 * sp.pi ** 2))) == 0)
chk("K3 J-kept root -> -b0/b1 as kappa m^2 -> 0 (ratio of the two -> 1)",
    sp.limit(sp.simplify(target / ratio), kap, 0) == 1)

# ------------------------------------------------------------------ K4 z3 global bracket
A, K, M_, Jv, B2, X, C = z3.Reals('alpha kappa m J b2 a c')
gam = -2 * K * A * M_ ** 4
b0z = -4 * A * M_ ** 4 / C
b1z = -(2 / K) / C
Fz = lambda gg: gg * (X - gg) ** 2 * Jv - (b0z + b1z * gg + B2 * gg * gg)
hyp = [A > 0, K > 0, M_ > 0, C > 0, Jv > 0, B2 >= 0]


def proves(h, goal):
    s = z3.Solver()
    s.add(h + [z3.Not(goal)])
    return s.check() == z3.unsat


chk("K4 z3: F_S(0) > 0 for alpha > 0", proves(hyp, Fz(0) > 0))
chk("K4 z3: F_S(-b0/b1) <= 0 for b2 >= 0 (any a, any J > 0)", proves(hyp, Fz(gam) <= 0))
s = z3.Solver()
s.add(hyp[:-1] + [B2 < 0, Fz(gam) > 0])
chk("K4 CONTROL z3: with b2 < 0 the bound at -b0/b1 CAN fail (sat)", s.check() == z3.sat)
chk("K4 z3: -2 kappa alpha m^4 > -4 m^2 iff kappa m^2 < 2/alpha",
    proves([A > 0, K > 0, M_ > 0], (gam > -4 * M_ ** 2) == (K * M_ ** 2 < 2 / A)))
print("   2/alpha at alpha = 1/(64 pi^2): 128 pi^2 = %.2f  -> m < %.2f M_P (reduced)"
      % (float(128 * sp.pi ** 2), float(sp.sqrt(128 * sp.pi ** 2))))

# ------------------------------------------------------------------ numerics
mp.mp.dps = 160
ALPHA = mp.mpf(1) / (64 * mp.pi ** 2)
LAM, OMEGA = mp.mpf('7.15e-121'), mp.mpf('0.685')
EPS = mp.sqrt(LAM / (6 * OMEGA * ALPHA))       # (m/M_P)^2 = kappa m^2  (M_P^2 = 1/kappa)
HBAR, CSI, GSI, ECH = mp.mpf('1.054571817e-34'), mp.mpf(299792458), mp.mpf('6.67430e-11'), mp.mpf('1.602176634e-19')
MP_EV = mp.sqrt(HBAR * CSI / (8 * mp.pi * GSI)) * CSI ** 2 / ECH


def Jq(gm, mm=1):
    """(4.5) Stieltjes transform, M = 4m^2/(1-u^2): J = INT_0^1 u^2 du /(8 pi^2 (4m^2 - gm (1-u^2)))."""
    return mp.quad(lambda u: u ** 2 / (8 * mp.pi ** 2 * (4 * mm ** 2 - gm * (1 - u ** 2))), [0, 1])


def J(gm, mm=1):
    """Closed form of the same u-integral, INT u^2/(A + B u^2), A = 4m^2 - gm, B = gm
    (elementary; checked against Jq below).  Used for the root solves (speed)."""
    gm = mp.mpf(gm)
    if gm == 0:
        return 1 / (96 * mp.pi ** 2 * mm ** 2)
    Aa, Bb = 4 * mm ** 2 - gm, gm
    if Bb < 0:
        I = mp.atanh(mp.sqrt(-Bb / Aa)) / mp.sqrt(-Aa * Bb)
    else:
        I = mp.atan(mp.sqrt(Bb / Aa)) / mp.sqrt(Aa * Bb)
    return (1 / Bb - (Aa / Bb) * I) / (8 * mp.pi ** 2)


chk("K2 numeric: quadrature J(0) = 1/(96 pi^2)", abs(Jq(0) * 96 * mp.pi ** 2 - 1) < mp.mpf(10) ** -100)
chk("K2 numeric: closed form == quadrature at gamma = -1e-60, -0.5, -7, +1, +3.9 (m = 1)",
    all(abs(J(mp.mpf(v)) / Jq(mp.mpf(v)) - 1) < mp.mpf(10) ** -60 for v in ('-1e-60', '-0.5', '-7', '1', '3.9')))
# independent check of the substitution against the defining M-integral at gamma = -3
mp.mp.dps = 40
Jm = mp.quad(lambda M: mp.sqrt(1 - 4 / M) / (16 * mp.pi ** 2 * M * (M + 3)), [4, 8, mp.inf])
chk("K5 CONTROL: substituted J(-3) equals the (4.5) M-integral", abs(Jq(-3) / Jm - 1) < mp.mpf(10) ** -30)
mp.mp.dps = 160


def FS(gm, eps, x, bb, alpha=ALPHA):
    cc = 6 * (mp.mpf(1) / 6 - x) ** 2
    B0, B1, aa = -alpha * 4 / cc, -(2 / eps) / cc, 2 / (6 * x - 1)
    return gm * (aa - gm) ** 2 * J(gm) - (B0 + B1 * gm + bb * gm ** 2)


def root(eps, x, bb, alpha=ALPHA):
    g0 = -2 * eps * alpha
    lo, hi = 2 * g0, g0 / 2
    flo, fhi = FS(lo, eps, x, bb, alpha), FS(hi, eps, x, bb, alpha)
    if not (flo < 0 < fhi):
        return None
    for _ in range(420):                     # bisection: sign-certain, no derivative
        mid = (lo + hi) / 2
        if FS(mid, eps, x, bb, alpha) < 0:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


print("   matched eps = (m/M_P)^2 = %s ; m = %s eV" % (mp.nstr(EPS, 6), mp.nstr(mp.sqrt(EPS) * MP_EV, 6)))
gl = -2 * EPS * ALPHA
gj = gl / (1 + EPS / (288 * mp.pi ** 2))
worst = mp.mpf(0)
for x in (mp.mpf(0), mp.mpf(1) / 3, mp.mpf(-1)):
    for bb in (0, 10 ** 50, -10 ** 50, 10 ** 100, -10 ** 100):
        r = root(EPS, x, mp.mpf(bb))
        good = r is not None
        if good:
            d_ratio = r / gl - 1
            d_j = r / gj - 1
            worst = max(worst, abs(d_ratio))
            print("   xi=%-6s b2=%+.0e : gamma_0 = %s m^2 ; root/(-b0/b1)-1 = %s ; root/Jkept-1 = %s"
                  % (mp.nstr(x, 3), float(bb), mp.nstr(r, 12), mp.nstr(d_ratio, 4), mp.nstr(d_j, 4)))
        chk("K5 exact zero bracketed in (2 g, g/2) at xi=%s, b2=%+.0e" % (mp.nstr(x, 3), float(bb)), good)
chk("K5 at the matched m, |root/(-b0/b1) - 1| < 1e-15 for every (xi, b2) tried", worst < mp.mpf(10) ** -15)

print("   K6 validity of GMMPS's -b0/b1 (b2 = 0, xi = 0, m = 1 units):")
k6 = []
for e in ('1e-6', '1e-3', '1', '10', '100', '1000'):
    ee = mp.mpf(e)
    rr = root(ee, mp.mpf(0), mp.mpf(0))
    glk = -2 * ee * ALPHA
    gjk = glk / (1 + ee / (288 * mp.pi ** 2))
    if rr is None:
        print("     kappa m^2 = %-6s : no zero in (2g, g/2)" % e)
        k6.append((e, None, None))
        continue
    print("     kappa m^2 = %-6s : root = %s ; root/(-b0/b1) = %s ; root/Jkept = %s ; inside (-4,0): %s"
          % (e, mp.nstr(rr, 8), mp.nstr(rr / glk, 8), mp.nstr(rr / gjk, 8), rr > -4))
    k6.append((e, rr / glk, rr / gjk))
chk("K6 at kappa m^2 = 1e-6 both approximations agree with the exact root to < 1e-6",
    abs(k6[0][1] - 1) < 1e-6 and abs(k6[0][2] - 1) < 1e-6)
chk("K6 up to kappa m^2 = 10 (m ~ 3 M_P) both first-order forms are within 0.5 % of the exact root",
    all(abs(r[1] - 1) < 0.005 and abs(r[2] - 1) < 0.005 for r in k6[:4]))
chk("K6 REACH: at kappa m^2 = 1000 (m ~ 32 M_P) both first-order forms miss by > 5 % (O(alpha^2) and b2-free J nonlinearity)",
    abs(k6[-1][1] - 1) > 0.05 and abs(k6[-1][2] - 1) > 0.05)

# ------------------------------------------------------------------ K7
r0 = root(EPS, mp.mpf(0), mp.mpf(0))
m_ev = mp.sqrt(EPS) * MP_EV
H_ev = mp.sqrt(-r0) * m_ev
MPC_M = mp.mpf('3.0856775814913673e22')
H_kms = H_ev * ECH / HBAR * MPC_M / 1000
print("   K7 gamma_0/m^2 = %s ; H = sqrt(-gamma_0) = %s eV = %s km/s/Mpc"
      % (mp.nstr(r0, 6), mp.nstr(H_ev, 6), mp.nstr(H_kms, 6)))
chk("K7 'slightly smaller than 0': -1e-60 < gamma_0/m^2 < 0 at the matched m", -mp.mpf(10) ** -60 < r0 < 0)
chk("K7 H^2 = Lambda/(3 Omega) (the matching closes: H = %s km/s/Mpc)" % mp.nstr(H_kms, 5),
    abs(H_ev ** 2 / (LAM * MP_EV ** 2 / (3 * OMEGA)) - 1) < 1e-10)

# ------------------------------------------------------------------ K8
w2, aa_, B0s, B1s, B2s = sp.symbols('w2 a b0 b1 b2')
Jf = sp.Function('J')
Q = w2 * (w2 + aa_) ** 2 * Jf(-w2) + B0s - B1s * w2 + B2s * w2 ** 2       # (4.30) as restated in linstab
gs = sp.Symbol('gamma')
FSs = gs * (aa_ - gs) ** 2 * Jf(gs) - (B0s + B1s * gs + B2s * gs ** 2)
chk("K8 F_S(-w^2) + Q(w^2) == 0 identically (restated (4.30)) -> w = sqrt(-gamma_0)",
    sp.simplify(FSs.subs(gs, -w2) + Q) == 0)

# ------------------------------------------------------------------ K9 controls
chk("K9 CONTROL alpha = 0: F_S(0) = 0 exactly", FS(mp.mpf(0), EPS, mp.mpf(0), 0, alpha=mp.mpf(0)) == 0)
an = -ALPHA
gpos = -2 * EPS * an                      # > 0
fa, fb = FS(gpos / 2, EPS, mp.mpf(0), 0, an), FS(2 * gpos, EPS, mp.mpf(0), 0, an)
chk("K9 CONTROL alpha < 0: branch zero bracketed on gamma > 0 (oscillatory, not growing)", fa < 0 < fb)
chk("K9 CONTROL alpha < 0: the growing-side bracket does NOT fire", root(EPS, mp.mpf(0), 0, an) is None)

print("ALL PASS" if ok else "SOME FAIL")
sys.exit(0 if ok else 1)
