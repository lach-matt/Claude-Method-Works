#!/usr/bin/env python3
r"""
DOCKET 67 re-derivation for key 2405.05963-sec3.2 (Kontou 2024 Sec. 3.2, as
quoted at research/warp-drive/qeihps.py:46-50, 318-322).

The quoted sentence: "This is not true, for example, for the T_split operator of
nonminimally coupled fields, so these inequalities cannot be used in this case.
State-dependent bounds have been derived for the nonminimally coupled field
[17,29,30]."

What is checkable here, finite and closed-form:

 A. The minimally coupled point-split energy density IS a sum of squares
    (Fewster-Smith gr-qc/0702056 eq. (80), READ from the cached page text:
    T_split = 1/2 sum_alpha e_alpha^a nabla_a (x) e_alpha^b nabla_b + 1/2 mu^2 1(x)1),
    so its classical coincidence limit is >= 0 for every real field.   (sympy)
 B. For xi != 0 the classical energy density of the NMC field (FO 0708.2450
    eq. (7), READ) at a point, in Riemann normal coordinates about that point,
    is  rho = 1/2 phidot^2 + (1/2 - 2 xi)|grad phi|^2 - 2 xi phi Lap(phi) + K phi^2,
    with K collecting m^2/2 and every curvature term (all multiply phi^2).
    Derived from T_00 = phidot^2 + 1/2(m^2 phi^2 - (d phi)^2) + xi(g_00 Box - d0 d0 - G_00) phi^2
    in flat signature (+,-,-,-) by sympy.                                  (sympy)
 C. For every real K and every xi != 0 there is Cauchy data with rho < 0 at the
    point; for xi = 0 and K >= 0, rho >= 0 for all data.                   (z3)
    Contrapositive of A: a sum-of-squares T_split has rho >= 0 classically, so
    C shows the NMC T_split is NOT of the sum-of-squares (positive-type) form
    that the Fewster-type state-independent / absolute derivations need.
 D. A concrete smooth, compactly supported datum at xi = 1/6 (HPS's coupling)
    with rho(0) < 0, evaluated exactly.                                    (sympy)

NOT checkable here: FO Sec. 3's quantum no-go (Hadamard states with
<rho> < -rho_0 on any bounded region, xi > 0, massless, 4D Minkowski) -- an
infinite-dimensional state construction, READ at source but not re-run; and the
verbatim wording of Kontou Sec. 3.2 (source unreachable in this stage).
"""
import sympy as sp
import z3

ok = True
def chk(name, cond):
    global ok
    ok &= bool(cond)
    print(("PASS " if cond else "FAIL ") + name)

t, x, y, z, xi, m = sp.symbols('t x y z xi m', real=True)
X = (t, x, y, z)
eta = sp.diag(1, -1, -1, -1)
phi = sp.Function('phi')(*X)

def d(f, mu): return sp.diff(f, X[mu])
dphi2 = sum(eta[a, a] * d(phi, a)**2 for a in range(4))           # (d phi)^2 = g^ab d_a phi d_b phi
box = lambda f: sum(eta[a, a] * sp.diff(f, X[a], 2) for a in range(4))

# ---- A: minimal coupling, flat, orthonormal frame: T_00 = 1/2 sum_alpha (e_alpha phi)^2 + 1/2 m^2 phi^2
T00_min = d(phi, 0)**2 + sp.Rational(1, 2) * eta[0, 0] * (m**2 * phi**2 - dphi2)
sos = sp.Rational(1, 2) * sum(d(phi, a)**2 for a in range(4)) + sp.Rational(1, 2) * m**2 * phi**2
chk("A  xi=0: T_00 equals the FS sum of squares 1/2 sum (e_a phi)^2 + 1/2 m^2 phi^2",
    sp.simplify(sp.expand(T00_min - sos)) == 0)

# ---- B: NMC, flat (curvature terms go into K; they multiply phi^2 only)
T00 = T00_min + xi * (eta[0, 0] * box(phi**2) - sp.diff(phi**2, t, 2))
lap = sum(sp.diff(phi, X[i], 2) for i in (1, 2, 3))
grad2 = sum(d(phi, i)**2 for i in (1, 2, 3))
target = (sp.Rational(1, 2) * d(phi, 0)**2 + (sp.Rational(1, 2) - 2 * xi) * grad2
          - 2 * xi * phi * lap + sp.Rational(1, 2) * m**2 * phi**2)
chk("B  xi: T_00 = 1/2 phidot^2 + (1/2-2xi)|grad phi|^2 - 2 xi phi Lap phi + m^2 phi^2/2",
    sp.simplify(sp.expand(T00 - target)) == 0)

# ---- C: z3 over the jet at a point (phi, phidot, |grad phi|^2 = g2 >= 0, Lap phi = L free)
P, Pd, G2, L, XI, K = z3.Reals('P Pd G2 L XI K')
rho = Pd * Pd / 2 + (z3.RealVal(1) / 2 - 2 * XI) * G2 - 2 * XI * P * L + K * P * P
s = z3.Solver()
# claim C1: for all K and all xi != 0 there EXISTS data with rho < 0.  Refute its negation:
s.add(XI != 0)
s.add(z3.ForAll([P, Pd, G2, L], z3.Implies(G2 >= 0, rho >= 0)))
r1 = s.check()
chk("C1 z3: no (xi != 0, K) makes rho >= 0 for all jets  [unsat expected]", r1 == z3.unsat)
# explicit witness family (guards against vacuity): P=1, Pd=0, G2=0, L = (K+1)/(2 xi)  -> rho = -1
wit = z3.Solver()
wit.add(XI != 0, P == 1, Pd == 0, G2 == 0, L * 2 * XI == K + 1)
wit.add(z3.Not(rho == -1))
chk("C1' witness L=(K+1)/(2xi) gives rho = -1 exactly for every K, xi != 0  [unsat]", wit.check() == z3.unsat)
# claim C2: xi = 0, K >= 0 -> rho >= 0 for every jet (the positive side, anti-vacuity)
s2 = z3.Solver()
s2.add(XI == 0, K >= 0, G2 >= 0, rho < 0)
chk("C2 z3: xi = 0 and K >= 0 imply rho >= 0  [unsat expected]", s2.check() == z3.unsat)
# claim C3: the sign of the xi-dependent (phi, Lap phi) block is indefinite -- its matrix
M = sp.Matrix([[0, -xi], [-xi, 0]])
ev = M.eigenvals()
chk("C3 sympy: (phi, Lap phi) block has eigenvalues +-xi, indefinite for xi != 0",
    set(ev.keys()) == {xi, -xi})

# ---- D: explicit compactly supported datum at xi = 1/6, m = 0, phidot = 0 on t = 0
r = sp.symbols('r', nonnegative=True)
A, c = sp.symbols('A c', positive=True)
# phi = A (1 + c r^2) near 0 (times a bump equal to 1 on r < 1): at r = 0 only the jet matters
ph = A * (1 + c * r**2)
lap_r = sp.diff(r**2 * sp.diff(ph, r), r) / r**2
grad_r2 = sp.diff(ph, r)**2
xi0 = sp.Rational(1, 6)
rho0 = sp.limit((sp.Rational(1, 2) - 2 * xi0) * grad_r2 - 2 * xi0 * ph * lap_r, r, 0)
print("   rho(0) at xi = 1/6, phi = A(1 + c r^2):", sp.simplify(rho0))
chk("D  xi = 1/6: rho(0) = -2 c A^2 < 0 for c > 0", sp.simplify(rho0 + 2 * c * A**2) == 0)
# xi < 0: choose c < 0; show the sign flips accordingly (rho(0) = -12 xi c A^2)
xs, cs = sp.symbols('xs cs', real=True)
ph2 = A * (1 + cs * r**2)
lap2 = sp.diff(r**2 * sp.diff(ph2, r), r) / r**2
rho_gen = sp.limit((sp.Rational(1, 2) - 2 * xs) * sp.diff(ph2, r)**2 - 2 * xs * ph2 * lap2, r, 0)
chk("D' general xi: rho(0) = -12 xi c A^2 (negative whenever c has the sign of xi)",
    sp.simplify(rho_gen + 12 * xs * cs * A**2) == 0)

print("ALL PASS" if ok else "SOME FAIL")
raise SystemExit(0 if ok else 1)
