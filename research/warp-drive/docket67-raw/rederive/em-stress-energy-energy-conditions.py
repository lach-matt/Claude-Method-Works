#!/usr/bin/env python3
"""
DOCKET 67 -- audit re-derivation: em-stress-energy-energy-conditions.

External result as the tree uses it:
  charge.py:155-162  em_is_ordinary(): rho>0, p_r=-rho, p_t=+rho => NEC, WEC, DEC
  spec.py:99-101, 190, 305 ; specthm SR1 ("NEC, WEC and DEC satisfied everywhere")
Published form (Hawking & Ellis 1973, NAMED-NOT-READ; restated in Fewster,
arXiv:1208.5399, Lectures on QEIs, p.4 and p.? : "DEC also holds ... and the same
is true for the electromagnetic field").

Parts
  A  classical Maxwell field (sympy, exact): WEC, DEC, NEC for ALL F_ab; eigen-
     structure; null (type II) fields; homogeneity => rho=1 is WLOG.
  A6 energy-condition definitions for Hawking-Ellis type I (z3, linear quantifier).
  B  nonlinear electrodynamics L(F) (sympy): NEC <=> L_F <= 0; pure-B rho, p.
  C  one-loop Euler-Heisenberg, pure magnetic field (numeric). THE PROPER-TIME
     FORM USED IS NOT READ AT SOURCE HERE (alphaXiv quota exhausted, arxiv.org
     refused by the proxy): it is checked only for internal consistency (weak-
     field coefficient 2 alpha^2/45 m^4 (4F^2+7G^2) and the strong-field leading
     log), and every conclusion drawn from it is conditional on that form.
  D  data: B_crit from CODATA 2018 vs 2022; magnetic pressure at the tree's
     1e11 T; field-confinement scale.
"""
import math, random, sys
import sympy as sp

ok_all = True
def rep(label, good, detail=""):
    global ok_all
    ok_all &= bool(good)
    print("  %-66s %s %s" % (label, "ok" if good else "FAIL", detail))

eta = sp.diag(-1, 1, 1, 1)

def Fmat(E, B):
    Ex, Ey, Ez = E; Bx, By, Bz = B
    # F_{ab}, signature (-+++), F_{0i} = -E_i, F_{ij} = eps_{ijk} B_k
    return sp.Matrix([[0, -Ex, -Ey, -Ez],
                      [Ex, 0, Bz, -By],
                      [Ey, -Bz, 0, Bx],
                      [Ez, By, -Bx, 0]])

def T_maxwell(F):
    Fup = eta * F * eta                      # F^{ab}
    FF = sum(F[a, b] * Fup[a, b] for a in range(4) for b in range(4))
    Fmix = F * eta                           # F_a^c
    return sp.simplify(F * eta * F.T - sp.Rational(1, 4) * eta * FF), FF   # F_ac F_b^c - 1/4 g F^2

print("A  CLASSICAL MAXWELL FIELD (Heaviside-Lorentz, c=1; 1/4pi dropped)")
Ex, Ey, Ez, Bx, By, Bz = sp.symbols("E_x E_y E_z B_x B_y B_z", real=True)
E = (Ex, Ey, Ez); B = (Bx, By, Bz)
F = Fmat(E, B)
T, FF = T_maxwell(F)
E2 = Ex**2 + Ey**2 + Ez**2; B2 = Bx**2 + By**2 + Bz**2
EdB = Ex*Bx + Ey*By + Ez*Bz
S = sp.Matrix([Ey*Bz - Ez*By, Ez*Bx - Ex*Bz, Ex*By - Ey*Bx])
rep("A1 T_00 = (E^2+B^2)/2", sp.simplify(T[0, 0] - (E2 + B2) / 2) == 0)
rep("A1 |T_0i| = |E x B| (Poynting)", all(sp.simplify(T[0, i+1]**2 - S[i]**2) == 0 for i in range(3)))
trace = sp.simplify(sum((eta * T)[a, a] for a in range(4)))
rep("A1 trace g^ab T_ab = 0", trace == 0)
lag = sp.expand(T[0, 0]**2 - sum(T[0, i]**2 for i in (1, 2, 3)) - ((E2 - B2)**2 + 4 * EdB**2) / 4)
rep("A2 T00^2 - |T0i|^2 == ((E^2-B^2)^2 + 4(E.B)^2)/4  (identity)", sp.simplify(lag) == 0)
print("     => for EVERY observer (any frame's e0) energy density >= 0 and the flux")
print("        -T^a_b u^b is causal: WEC and DEC hold for every F_ab; NEC by limit.")

# A3 eigenstructure of T^a_b
lam = sp.symbols("lam")
Tmix = eta * T      # T^a_b
cp = sp.factor(sp.expand((Tmix - lam * sp.eye(4)).det()))
L2 = ((E2 - B2)**2 + 4 * EdB**2) / 4
rep("A3 char. poly of T^a_b = (lam^2 - L^2)^2, L^2=((E^2-B^2)^2+4(E.B)^2)/4",
    sp.simplify(sp.expand(cp - (lam**2 - L2)**2)) == 0)
print("     => eigenvalues {-L,-L,+L,+L}: canonical frame rho=L, p_1=-L, p_2=p_3=+L,")
print("        exactly charge.em_is_ordinary()'s (rho, p_r=-rho, p_t=+rho) with rho=L.")

# numeric DEC test T_ab u^a v^b >= 0, u, v future timelike, random fields
random.seed(67)
def num_T(e, b):
    Fn = Fmat(e, b)
    Tn, _ = T_maxwell(Fn)
    return [[float(Tn[i, j]) for j in range(4)] for i in range(4)]
def rand_future_timelike():
    v = [random.gauss(0, 3) for _ in range(3)]
    return [math.sqrt(sum(x*x for x in v)) + abs(random.gauss(0, 1)) + 1e-9] + v
worst = float("inf"); n = 0
for _ in range(300):
    e = [random.gauss(0, 1) for _ in range(3)]; b = [random.gauss(0, 1) for _ in range(3)]
    Tn = num_T(e, b)
    for _ in range(40):
        u = rand_future_timelike(); v = rand_future_timelike()
        val = sum(Tn[i][j] * u[i] * v[j] for i in range(4) for j in range(4))
        norm = (sum(x*x for x in e) + sum(x*x for x in b)) * sum(x*x for x in u) ** .5 * sum(x*x for x in v) ** .5
        worst = min(worst, val / norm); n += 1
rep("A2' numeric T_ab u^a v^b >= 0, %d random (F,u,v)" % n, worst >= -1e-12, "min normalised %.3e" % worst)

# A4 null field: E perp B, |E|=|B|
Tn = num_T([1.0, 0, 0], [0, 1.0, 0])
Fn = Fmat([1, 0, 0], [0, 1, 0]); Tnull, _ = T_maxwell(Fn)
Mn = eta * Tnull
nil = (Mn * Mn) == sp.zeros(4)
rep("A4 null field (E=x, B=y): T^a_b nilpotent (type II), T_00=1>0", nil and Tnull[0, 0] == 1,
    "T_ab=%s" % (Tnull.tolist(),))
worstk = float("inf")
for _ in range(2000):
    d = [random.gauss(0, 1) for _ in range(3)]; nd = math.sqrt(sum(x*x for x in d))
    k = [1.0] + [x / nd for x in d]
    worstk = min(worstk, sum(float(Tnull[i, j]) * k[i] * k[j] for i in range(4) for j in range(4)))
rep("A4 null field NEC: T_ab k^a k^b >= 0 for 2000 random null k", worstk >= -1e-12, "min %.3e" % worstk)
print("     charge.em_is_ordinary() tests only the non-null (type I) eigenstructure;")
print("     the null case is not in it and is shown here to satisfy NEC/WEC/DEC too.")

# A5 homogeneity
rho = sp.symbols("rho", positive=True); cc = sp.symbols("c", positive=True)
conds = lambda r, p1, p2: [r + p1 >= 0, r + p2 >= 0, r >= 0, r - sp.Abs(p1) >= 0, r - sp.Abs(p2) >= 0]
rep("A5 conditions at (rho,-rho,rho) are True for every rho>0 (rho=1 is WLOG)",
    all(bool(sp.simplify(c)) for c in conds(rho, -rho, rho)))

print("\nA6  ENERGY-CONDITION DEFINITIONS, HAWKING-ELLIS TYPE I (z3)")
try:
    import z3
    r, p1, p2, p3 = z3.Reals("r p1 p2 p3")
    a0, a1, a2, a3 = z3.Reals("a0 a1 a2 a3")   # a_i = u_i^2
    wec_def = z3.ForAll([a0, a1, a2, a3],
        z3.Implies(z3.And(a1 >= 0, a2 >= 0, a3 >= 0, a0 > a1 + a2 + a3),
                   r*a0 + p1*a1 + p2*a2 + p3*a3 >= 0))
    wec_alg = z3.And(r >= 0, r + p1 >= 0, r + p2 >= 0, r + p3 >= 0)
    nec_def = z3.ForAll([a1, a2, a3],
        z3.Implies(z3.And(a1 >= 0, a2 >= 0, a3 >= 0, a1 + a2 + a3 == 1),
                   r + p1*a1 + p2*a2 + p3*a3 >= 0))
    nec_alg = z3.And(r + p1 >= 0, r + p2 >= 0, r + p3 >= 0)
    for name, d, al in (("WEC", wec_def, wec_alg), ("NEC", nec_def, nec_alg)):
        s = z3.Solver(); s.add(z3.Not(d == al))
        res = s.check()
        rep("A6 %s: 'T_ab u^a u^b>=0 all %s u' <=> charge.py's algebraic form" %
            (name, "timelike" if name == "WEC" else "null"), res == z3.unsat, str(res))
    # vacuity guard: the algebraic forms are satisfiable and falsifiable
    s = z3.Solver(); s.add(wec_alg, r == 1, p1 == -1, p2 == 1, p3 == 1)
    g1 = s.check() == z3.sat
    s = z3.Solver(); s.add(z3.Not(wec_def), r == 1, p1 == -1.1, p2 == 1, p3 == 1)
    g2 = s.check() == z3.sat
    rep("A6 vacuity guard (EM point satisfies; p1=-1.1 rho refutes)", g1 and g2)
    # DEC type I: rho >= |p_i|  (flux -T^a_b u^b causal for all timelike u) -- numeric
    def dec_def(rv, ps, trials=4000):
        for _ in range(trials):
            u = rand_future_timelike()
            j0 = rv * u[0]; ji = [ps[i] * u[i+1] for i in range(3)]
            if j0 < 0 or j0*j0 < sum(x*x for x in ji) - 1e-12 * j0*j0: return False
        return True
    agree = True
    for _ in range(300):
        rv = random.uniform(-1, 1); ps = [random.uniform(-1.5, 1.5) for _ in range(3)]
        alg = rv >= max(abs(x) for x in ps)
        if dec_def(rv, ps, 600) != alg and abs(rv - max(abs(x) for x in ps)) > 0.05:
            agree = False
    rep("A6 DEC type I: flux-causal definition <=> rho >= |p_i| (300 random, margin 0.05)", agree)
except ImportError:
    rep("A6 z3 not installed", False)

print("\nB  NONLINEAR ELECTRODYNAMICS L(F), F = F_ab F^ab / 4  (sympy)")
LF, Lv = sp.symbols("L_F L", real=True)
# T_ab = -2 dL/dg^ab + g_ab L,  dF/dg^ab = 1/2 F_ac F_b^c
T_nl = -LF * (F * eta * F.T) + eta * Lv
kx, ky, kz = sp.symbols("k_x k_y k_z", real=True)
k = sp.Matrix([1, 0, 0, 1])     # null, along z (WLOG by rotation)
w = (F.T * k)                   # w_b = F_ab k^a
ww = sp.simplify((w.T * eta * w)[0]);  # w_b w^b, eta^-1 = eta
wk = sp.simplify((w.T * k)[0])   # w_b k^b (w covariant, k contravariant)
rep("B1 w_b = F_ab k^a obeys w.k = 0", wk == 0)
rep("B1 w.w = (E_x-B_y)^2 + (E_y+B_x)^2 >= 0 (spacelike or null)",
    sp.simplify(ww - ((Ex - By)**2 + (Ey + Bx)**2)) == 0, str(sp.factor(ww)))
Tkk = sp.simplify((k.T * T_nl * k)[0])
rep("B2 T_ab k^a k^b = -L_F (w.w)  =>  NEC <=> L_F <= 0 where w != 0",
    sp.simplify(Tkk + LF * ww) == 0)
Bs = sp.symbols("B", positive=True)
Fb = Fmat((0, 0, 0), (0, 0, Bs)); Tb = -LF * (Fb * eta * Fb.T) + eta * Lv
rep("B3 pure B_z: rho = -L, p_par = L, p_perp = L - B^2 L_F",
    sp.simplify(Tb[0, 0] + Lv) == 0 and sp.simplify(Tb[3, 3] - Lv) == 0 and
    sp.simplify(Tb[1, 1] - (Lv - Bs**2 * LF)) == 0)
print("     Maxwell L=-F=-B^2/2, L_F=-1 recovers (rho, -rho, +rho).")
print("     pure-B DEC <=> L_F <= 0 and -B^2 L_F <= 2 rho; with L = -B^2/2 + L1(B):")
print("       NEC <=> dL1/dB <= B;  DEC <=> additionally B dL1/dB >= 2 L1.")

print("\nC  ONE-LOOP EULER-HEISENBERG, PURE B (form NOT read at source; consistency only)")
import mpmath as mp
mp.mp.dps = 30
alpha = mp.mpf("7.2973525643e-3")        # CODATA 2022 (2409.03787, read by the codata audit)
e = mp.sqrt(4 * mp.pi * alpha)           # Heaviside-Lorentz, m = 1
def L1(b):
    """-(1/8pi^2) int ds/s^3 e^{-s} [x coth x - 1 - x^2/3], x = b s, b = eB/m^2."""
    def f(s):
        x = b * s
        if x < mp.mpf("1e-3"):
            br = -x**4 / 45 + 2 * x**6 / 945
        else:
            br = x * mp.coth(x) - 1 - x**2 / 3
        return mp.exp(-s) * br / s**3
    return -mp.quad(f, [0, 1 / b, 1, mp.inf]) / (8 * mp.pi**2)
# weak field check: L1 -> e^4 B^4/(360 pi^2) = b^4/(360 pi^2)
bw = mp.mpf("1e-2")
rep("C1 weak field: L1(b)/(b^4/360pi^2) -> 1 (= 2a^2/45 (4F^2), G=0)",
    abs(L1(bw) / (bw**4 / (360 * mp.pi**2)) - 1) < 1e-3, "%.6f" % float(L1(bw) / (bw**4 / (360 * mp.pi**2))))
# strong field: L1 ~ (b^2/24pi^2) ln b  (i.e. e^2B^2/24pi^2 ln(eB/m^2))
b1, b2 = mp.mpf(1e4), mp.mpf(1e6)
slope = (L1(b2) / b2**2 - L1(b1) / b1**2) / (mp.log(b2) - mp.log(b1))
rep("C2 strong field: d(L1/b^2)/d ln b -> 1/(24 pi^2)", abs(slope * 24 * mp.pi**2 - 1) < 1e-3,
    "%.6f" % float(slope * 24 * mp.pi**2))
print("     b = B/B_crit      L_F           rho/(B^2/2)     DEC margin (B L1' - 2 L1)/B^2")
rows = []
for bb in (1, 22.65, 226.5, 1e4, 1e8):
    b = mp.mpf(bb); Bf = b / e
    dL1 = mp.diff(lambda y: L1(y * e) , Bf)            # dL1/dB  (L1 as function of B)
    Lf = (-Bf + dL1) / Bf                               # L_F = (dL/dB)/B
    rh = (Bf**2 / 2 - L1(b)) / (Bf**2 / 2)
    decm = (Bf * dL1 - 2 * L1(b)) / Bf**2
    rows.append((bb, Lf, rh, decm))
    print("     %10.4g   %14.10f   %14.10f   %14.6e" % (bb, float(Lf), float(rh), float(decm)))
rep("C3 NEC (L_F<0), WEC (rho>0), DEC margin >= 0 at every tabulated b",
    all(r[1] < 0 and r[2] > 0 and r[3] >= 0 for r in rows))
bNEC = mp.exp(mp.mpf(3) * mp.pi / alpha - mp.mpf(1) / 2)
print("     leading-log NEC boundary L_F = 0: ln b ~ 3pi/alpha - 1/2 = %.1f (b ~ 10^%.0f):"
      % (float(mp.log(bNEC)), float(mp.log10(bNEC))))
print("     the Landau-pole scale, where one loop is not the theory.")

print("\nD  DATA")
from scipy.constants import physical_constants as pc
me22 = pc["electron mass"][0]; hbar = pc["reduced Planck constant"][0]
qe = pc["elementary charge"][0]; c = pc["speed of light in vacuum"][0]; mu0 = pc["vacuum mag. permeability"][0]
me18 = 9.1093837015e-31
Bc22 = me22**2 * c**2 / (qe * hbar); Bc18 = me18**2 * c**2 / (qe * hbar)
print("     B_crit = m_e^2 c^2/(e hbar): 2018 %.10e T, 2022 %.10e T (rel %.1e)" % (Bc18, Bc22, Bc22 / Bc18 - 1))
print("     tree's 1e11 T = %.3f B_crit ; 1e12 T = %.2f B_crit" % (1e11 / Bc22, 1e12 / Bc22))
rep("D1 1e11 T exceeds B_crit (classical-Maxwell hypothesis out of domain)", 1e11 / Bc22 > 1)
u11 = (1e11)**2 / (2 * mu0)
print("     magnetic pressure at 1e11 T: %.4e Pa (tree: 3.979e27); mass-equivalent %.3e kg/m^3"
      % (u11, u11 / c**2))
rep("D2 u(1e11 T) = 3.979e27 Pa as spec.py/charge.py print", abs(u11 / 3.979e27 - 1) < 1e-3)
# Sun as lens: order-of-magnitude p/(rho c^2) (inputs NOT read at source; indicative)
G = 6.67430e-11; M = 1.989e30; R = 6.957e8
Pc_scale = G * M**2 / R**4; rho_mean = M / (4 / 3 * math.pi * R**3)
print("     Sun (tree's M, R): G M^2/R^4 = %.2e Pa vs mean rho c^2 = %.2e J/m^3, ratio %.1e"
      % (Pc_scale, rho_mean * c**2, Pc_scale / (rho_mean * c**2)))
print("     (dimensional scale only, not a solar model; the lens-matter DEC is outside this result)")

print("\nRESULT:", "ALL CHECKS PASS" if ok_all else "SOME CHECK FAILED")
sys.exit(0 if ok_all else 1)
