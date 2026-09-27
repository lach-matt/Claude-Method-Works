#!/usr/bin/env python3
"""DOCKET 67 -- casimir-anec-violation-curved.

Tree (anecscope.py:25-28, :33-34, :166-168; obstruct.py:163-166):
  "ANEC IN CURVED SPACETIME. FALSE in general, and the standard counterexample is
   the Casimir vacuum, where a geodesic between the plates violates it."
  "Casimir escapes [achronal ANEC] because the geodesic between the plates is not achronal."

Checks (sympy + z3):
 A. EM field between ideal parallel plates, T_ab = (C/L^4)(eta_ab - 4 z_a z_b), C = pi^2/720
    (Kontou-Sanders 2003.01815 eq.101, Brown-Maclay): T_kk for every null k.
    -> k parallel to the plates: T_kk = 0 identically.  k with k_z != 0: T_kk = -4C k_z^2/L^4 < 0,
       but that geodesic reaches a plate at affine distance L/|k_z|: it is not complete in the gap.
 B. Scalar field between plates, ANY mass, ANY curvature coupling xi, Dirichlet OR Neumann:
    image-sum two-point function G = sum_n [f(sigma_n) -/+ f(sigma~_n)] with f an arbitrary
    function of the squared interval.  Every renormalised (n != 0 or reflected) image term of
    <(k.d phi)^2> vanishes at coincidence for k parallel to the plates, and the xi-term
    -xi (k.d)^2 <phi^2> vanishes by t,x translation invariance.  -> <T_kk> = 0 on EVERY
    parallel geodesic at EVERY z between the plates.
 C. Cylinder spacetime (Minkowski periodically identified in z, period L) -- FOP gr-qc/0609007
    eq.(24), T_ab = (pi^2/90L^4) diag(-1,1,1,-3): T_kk = -(4 pi^2/90L^4) sin^2(theta) for
    k = (1, cos th, 0, sin th): negative for every winding geodesic -> ANEC integral = -infinity;
    zero for non-winding.  Chronality: the winding geodesic re-reaches the same (y,z) after
    dt = L/|sin th|, dx = L cot th; the covering-space interval to the image point is -L^2 < 0,
    i.e. TIMELIKE: the geodesic is chronal (FOP p.10; Graham-Olum 0705.3193 p.3).
 D. Plates do not make a straight null line chronal: in (a convex region of) Minkowski space
    the sum of two future-directed causal vectors, at least one timelike, is timelike (z3), so
    any timelike curve joins timelike-separated points; two points of one null line have
    interval 0 -> no timelike curve joins them -> every null geodesic between plates is
    ACHRONAL (Kontou-Sanders p.35 as restated: 'all null geodesics in Minkowski space are
    automatically achronal').
 E. The CURVED-spacetime half: Urban-Olum 0910.5925 eq.(42) as printed, evaluated
    (re-derived from their eqs 37-38 in the sibling audit anec-klinkhammer-wald-yurtsever,
    part D; not re-derived again here): vacuum ANEC integral negative for b > 2a on a complete
    ACHRONAL geodesic of a conformally flat 4D spacetime.
Exit 0 iff every check reproduces the statement it is labelled with.
"""
import sys
import sympy as sp

ok = True
def check(label, cond):
    global ok
    print(("PASS " if cond else "FAIL ") + label)
    ok = ok and bool(cond)

# ---------------- A: EM plates
C, L = sp.symbols('C L', positive=True)
eta = sp.diag(-1, 1, 1, 1)
zhat = sp.Matrix([0, 0, 0, 1])
T_em = (C / L**4) * (eta - 4 * zhat * zhat.T)
k0, kx, ky, kz = sp.symbols('k0 kx ky kz', real=True)
k = sp.Matrix([k0, kx, ky, kz])
Tkk = sp.expand((k.T * T_em * k)[0])
null = sp.Eq(-k0**2 + kx**2 + ky**2 + kz**2, 0)
Tkk_null = sp.simplify(Tkk.subs(k0**2, kx**2 + ky**2 + kz**2))
check("A1 EM plates: T_kk on null k reduces to -4 C kz^2/L^4  [got %s]" % Tkk_null,
      sp.simplify(Tkk_null + 4 * C * kz**2 / L**4) == 0)
check("A2 EM plates: T_kk = 0 for every null k parallel to the plates (kz = 0)",
      sp.simplify(Tkk_null.subs(kz, 0)) == 0)
check("A3 energy density T_00 = -C/L^4 with C = pi^2/720 (KS p.34)",
      sp.simplify((T_em[0, 0]).subs(C, sp.pi**2 / 720) + sp.pi**2 / (720 * L**4)) == 0)
lam, z0 = sp.symbols('lambda z0', real=True)
# a null geodesic with kz != 0 starting at z0 in (0,L) hits z = L or z = 0 at finite affine lambda
hit = sp.solve(sp.Eq(z0 + kz * lam, L), lam)[0]
check("A4 non-parallel geodesic reaches the plate at finite affine parameter (L - z0)/kz  [got %s]" % hit,
      sp.simplify(hit - (L - z0) / kz) == 0)

# ---------------- B: scalar image sum, generic f(sigma)
t, x, y, z, tp, xp, yp, zp, n, a = sp.symbols("t x y z tp xp yp zp n a", real=True)
f = sp.Function('f')
sig_trans = -(t - tp)**2 + (x - xp)**2 + (y - yp)**2 + (z - zp - 2 * n * a)**2
sig_refl = -(t - tp)**2 + (x - xp)**2 + (y - yp)**2 + (z + zp - 2 * n * a)**2
def kk_coincidence(sig):
    F = f(sig)
    # k = (1,1,0,0):  (d_t + d_x)(d_t' + d_x') F, then coincidence t'=t, x'=x, y'=y, z'=z
    D = sp.diff(F, t, tp) + sp.diff(F, t, xp) + sp.diff(F, x, tp) + sp.diff(F, x, xp)
    return sp.simplify(D.subs({tp: t, xp: x, yp: y}).subs(zp, z).doit())
rt = kk_coincidence(sig_trans)
rr = kk_coincidence(sig_refl)
check("B1 translated-image term of <(k.dphi)^2> at coincidence, k parallel: %s" % rt, rt == 0)
check("B2 reflected-image term of <(k.dphi)^2> at coincidence, k parallel: %s" % rr, rr == 0)
# xi-term: -xi (k.d)^2 <phi^2>(z) -- <phi^2> depends on z only (t,x,y translation invariance)
xi = sp.symbols('xi', real=True)
phi2 = sp.Function('W')(z)
xi_term = -xi * (sp.diff(phi2, t, 2) + 2 * sp.diff(phi2, t, x) + sp.diff(phi2, x, 2))
check("B3 curvature-coupling term -xi (k.d)^2 <phi^2>(z) vanishes for k parallel", sp.simplify(xi_term) == 0)
# sanity: the same image machinery DOES give a nonzero result for k across the plates (not a vacuous test)
def zz_coincidence(sig):
    F = f(sig)
    D = sp.diff(F, t, tp) + sp.diff(F, z, zp)   # k = (1,0,0,1)
    return sp.simplify(D.subs({tp: t, xp: x, yp: y}).subs(zp, z).doit())
nz = zz_coincidence(sig_trans)
check("B4 vacuity guard: for k across the plates the translated-image term is NOT identically 0  [%s]" % nz,
      nz != 0)

# ---------------- C: cylinder spacetime
th = sp.symbols('theta', real=True)
T_cyl = (sp.pi**2 / (90 * L**4)) * sp.diag(-1, 1, 1, -3)
kc = sp.Matrix([1, sp.cos(th), 0, sp.sin(th)])
Tkk_c = sp.simplify((kc.T * T_cyl * kc)[0])
check("C1 cylinder: T_kk = -(4 pi^2/90 L^4) sin^2 th  [got %s]" % Tkk_c,
      sp.simplify(Tkk_c + 4 * sp.pi**2 * sp.sin(th)**2 / (90 * L**4)) == 0)
check("C2 cylinder: T_kk = 0 for non-winding (th = 0)", sp.simplify(Tkk_c.subs(th, 0)) == 0)
Lam = sp.symbols('Lambda', positive=True)
anec_c = sp.limit(sp.integrate(Tkk_c.subs(th, sp.pi / 4), (lam, -Lam, Lam)), Lam, sp.oo)
check("C3 cylinder: ANEC integral on a winding geodesic (th = pi/4) = %s" % anec_c, anec_c == -sp.oo)
s = sp.symbols('s', positive=True)  # s = sin(theta) in (0,1]
dt = L / s
dx = L * sp.sqrt(1 - s**2) / s
interval = sp.simplify(-dt**2 + dx**2 + (L - L)**2)  # image point: z advanced by exactly one period L
check("C4 winding geodesic re-reaches an image of its start at covering interval %s < 0 (TIMELIKE -> chronal)" % interval,
      sp.simplify(interval + L**2) == 0)

# ---------------- D: straight null lines of Minkowski-with-plates are achronal
try:
    import z3
    u = z3.Reals('u0 u1 u2 u3'); v = z3.Reals('v0 v1 v2 v3')
    q = lambda w: -w[0] * w[0] + w[1] * w[1] + w[2] * w[2] + w[3] * w[3]
    w = [u[i] + v[i] for i in range(4)]
    sol = z3.Solver()
    sol.add(u[0] > 0, v[0] > 0, q(u) < 0, q(v) <= 0, z3.Not(q(w) < 0))
    r = sol.check()
    check("D1 z3: future timelike + future causal is timelike (negation %s)" % r, r == z3.unsat)
    # vacuity guard: the hypotheses are satisfiable
    g = z3.Solver(); g.add(u[0] > 0, v[0] > 0, q(u) < 0, q(v) <= 0)
    check("D2 z3 vacuity guard: hypotheses satisfiable (%s)" % g.check(), g.check() == z3.sat)
except ImportError:
    check("D1 z3 unavailable -- achronality check NOT RUN", False)
# two points on one null line have interval 0, not < 0: no timelike curve joins them
kpar = sp.Matrix([1, 1, 0, 0])
check("D3 two points p, p + lam k on a parallel null line: interval = 0 (not timelike)",
      sp.simplify((kpar.T * eta * kpar)[0] * lam**2) == 0)

# ---------------- E: curved half, Urban-Olum eq.(42) as printed (evaluated, not re-derived here)
aa, bb, rr_ = sp.Rational(1, 100), sp.Rational(5, 100), 1
beta = -1 / (5760 * sp.pi**2)
anec_uo = (aa * bb - 2 * aa**2) * 16 * beta * sp.sqrt(2 * sp.pi) / rr_**3
check("E1 Urban-Olum eq.(42) at a=0.01, b=0.05, r=1: %.4g < 0" % float(anec_uo), float(anec_uo) < 0)

print("ALL AGREE" if ok else "DISAGREEMENT")
sys.exit(0 if ok else 1)
