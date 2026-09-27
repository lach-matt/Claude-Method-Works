#!/usr/bin/env python3
"""DOCKET 67, result 15 of 286: Olum, PRL 81, 3567 (1998), gr-qc/9805003,
"Superluminal travel requires negative energies".

What is finite or closed-form in the paper, re-derived here:
  (1) eq. (1)-(2): the "apparently superluminal" metric is flat (Riemann = 0),
      its right-going null ray from the origin is x = t/(1-t^2), and the
      arrival time at x = 1 -- the paper prints (1+sqrt5)/2 ~ 0.618, which is
      a misprint (the root is (sqrt5-1)/2 = 0.618...); a DISCREPANCY, not an error
      in the theorem.
  (2) eq. (9)-(10): Casimir stress tensor between plates gives
      R_ab K^a K^b = -2 pi^3 / (45 d^4) for a null K along z (G = c = 1, Einstein
      eq. R_ab = 8 pi (T_ab - T g_ab / 2), the trace term dropping on a null K).
      Lobo-Crawford gr-qc/0204038 eq. (33) restates it as -2 pi^2/(45 d^4): their
      misprint, not Olum's.
  (3) The Raychaudhuri step (eq. 3-4): theta(0) = 0, omega = 0, R_kk >= 0 (NEC,
      implied by WEC), shear not identically zero  ==>  theta(v_B) < 0.
      Checked as an inequality with sympy and numerically by ODE integration
      on sample shear profiles; the finite algebra of eqs (5)-(8)
      (K_{a;b} Z^a Z^b >= 0 from the sign of Z^3_{;b} Z^b) is checked with z3
      as a real-arithmetic implication.
  (4) The consequence for composite.py's use of the theorem: a null ray with
      T_kk = 0 along its whole length (composite.py:90-93) but non-zero Weyl
      shear has theta(B) < 0 by the same step, so Olum's Condition 1 cannot
      hold on it (unless a conjugate point intervenes, which composite.py says
      it does -- and past a conjugate point the ray is not achronal and the
      theorem's premise fails).  The theorem does NOT say "negative energy
      somewhere off the path supplies the requirement".
Not checkable here: the global causal-structure steps (P must be a null
geodesic normal to Sigma_A and Sigma_B; no point of P conjugate to Sigma_A;
the invertibility of the congruence map) -- standard Hawking-Ellis
propositions, accepted as READ, not machine-checked.
"""
import sys
import sympy as sp

FAIL = 0
def chk(label, ok):
    global FAIL
    print(("  ok   " if ok else "  FAIL ") + label)
    if not ok:
        FAIL += 1

# ---------------------------------------------------------------- (1) eq. (1)
print("(1) Olum eq. (1): the metric is flat space in odd coordinates")
t, x = sp.symbols('t x', real=True)
g = sp.Matrix([[-1 + 4*t**2*x**2, -2*t*x*(1 - t**2)],
               [-2*t*x*(1 - t**2), (1 - t**2)**2]])
coords = [t, x]
ginv = g.inv()
n = 2
Gam = [[[sp.simplify(sum(ginv[a, d]*(sp.diff(g[d, b], coords[c]) + sp.diff(g[d, c], coords[b])
                                      - sp.diff(g[b, c], coords[d])) for d in range(n))/2)
         for c in range(n)] for b in range(n)] for a in range(n)]
def riem(a, b, c, d):
    r = sp.diff(Gam[a][b][d], coords[c]) - sp.diff(Gam[a][b][c], coords[d])
    r += sum(Gam[a][c][e]*Gam[e][b][d] - Gam[a][d][e]*Gam[e][b][c] for e in range(n))
    return sp.simplify(r)
R = [riem(a, b, c, d) for a in range(n) for b in range(n) for c in range(n) for d in range(n)]
chk("Riemann tensor of eq. (1) vanishes identically", all(r == 0 for r in R))
# substitution x' = x (1 - t^2): pull-back of -dt^2 + dx'^2
xp = x*(1 - t**2)
J = sp.Matrix([[1, 0], [sp.diff(xp, t), sp.diff(xp, x)]])
eta = sp.diag(-1, 1)
chk("x' = x(1-t^2) pulls -dt^2 + dx'^2 back to eq. (1)", sp.simplify(J.T*eta*J - g) == sp.zeros(2))
# null rays eq. (2)
v = sp.symbols('v')
nullcond = sp.expand(g[0, 0] + 2*g[0, 1]*v + g[1, 1]*v**2)
roots = sp.solve(nullcond, v)
want = {sp.simplify((1 + 2*t*x)/(1 - t**2)), sp.simplify((-1 + 2*t*x)/(1 - t**2))}
chk("null rays dx/dt = (+-1 + 2 t x)/(1 - t^2)  [eq. (2)]",
    {sp.simplify(r) for r in roots} == want)
xr = t/(1 - t**2)
chk("x = t/(1-t^2) solves the right-going ray from the origin",
    sp.simplify(sp.diff(xr, t) - (1 + 2*t*xr)/(1 - t**2)) == 0 and xr.subs(t, 0) == 0)
arr = [r for r in sp.solve(sp.Eq(xr, 1), t) if r.is_real and 0 < r < 1]
chk("arrival at x = 1 is t = (sqrt5 - 1)/2 = %.6f" % float(arr[0]),
    len(arr) == 1 and sp.simplify(arr[0] - (sp.sqrt(5) - 1)/2) == 0)
chk("the paper's printed '(1+sqrt5)/2 ~ 0.618' is a MISPRINT: (1+sqrt5)/2 = %.6f, not 0.618"
    % float((1 + sp.sqrt(5))/2), abs(float((1 + sp.sqrt(5))/2) - 0.618) > 0.5)

# ---------------------------------------------------------------- (2) Casimir
print("(2) Olum eq. (9)-(10): Casimir R_ab K^a K^b")
d = sp.symbols('d', positive=True)
T = sp.pi**2/(720*d**4)*sp.diag(-1, 1, 1, -3)      # (t, x, y, z), signature -+++
eta4 = sp.diag(-1, 1, 1, 1)
K = sp.Matrix([1, 0, 0, 1])                        # null, along z
trT = sum(eta4[a, a]*T[a, a] for a in range(4))
Ric = 8*sp.pi*(T - sp.Rational(1, 2)*trT*eta4)
RKK = sp.simplify((K.T*Ric*K)[0])
chk("R_ab K^a K^b = -2 pi^3/(45 d^4)  [eq. (10), Olum]", sp.simplify(RKK + 2*sp.pi**3/(45*d**4)) == 0)
chk("the trace term drops on a null K (so only T_ab K^a K^b = T_tt + T_zz enters)",
    sp.simplify((K.T*eta4*K)[0]) == 0)
chk("Lobo-Crawford eq. (33) '-2 pi^2/(45 d^4)' differs from Olum by a factor pi: their misprint",
    sp.simplify(RKK/(-2*sp.pi**2/(45*d**4)) - sp.pi) == 0)
chk("R_ab K^a K^b < 0: the NEC is violated on the z-ray between the plates", RKK.subs(d, 1) < 0)

# ---------------------------------------------------------------- (3) Raychaudhuri sign
print("(3) eq. (3)-(4): theta(0)=0, omega=0, R_kk>=0, shear not identically 0  ==> theta(B) < 0")
# closed form: theta' = -R - 2 s^2 - theta^2/2  <=  -2 s^2  ==>  theta(v) <= -2 int_0^v s^2 < 0
# once s has been non-zero on a set of positive measure.  Numeric witness on profiles:
import math
def integrate(Rfun, sfun, vB=1.0, N=20000):
    th, v, h = 0.0, 0.0, vB/N
    for _ in range(N):
        # RK4
        f = lambda vv, tt: -Rfun(vv) + 0.0 - 2*sfun(vv)**2 - 0.5*tt*tt
        k1 = f(v, th); k2 = f(v + h/2, th + h*k1/2); k3 = f(v + h/2, th + h*k2/2); k4 = f(v + h, th + h*k3)
        th += h*(k1 + 2*k2 + 2*k3 + k4)/6; v += h
    return th
profiles = [
    ("R=0, shear bump at v~0.5",   lambda v: 0.0,               lambda v: math.exp(-50*(v-0.5)**2)),
    ("R=0.3 const, shear bump",    lambda v: 0.3,               lambda v: math.exp(-50*(v-0.5)**2)),
    ("R=0, shear only near v=0.9", lambda v: 0.0,               lambda v: 0.2*math.exp(-400*(v-0.9)**2)),
    ("R>=0 ramp, tiny shear",      lambda v: 0.1*v,             lambda v: 1e-3),
]
for name, Rf, sf in profiles:
    thB = integrate(Rf, sf)
    chk("%-30s theta(B) = %+.4e < 0" % (name, thB), thB < 0)
# and the two ways the conclusion can be dodged, shown as such:
chk("R=0, shear = 0 identically (generic condition FAILS): theta(B) = %+.1e, not < 0"
    % integrate(lambda v: 0.0, lambda v: 0.0), integrate(lambda v: 0.0, lambda v: 0.0) == 0.0)
thC = integrate(lambda v: -2*math.pi**3/45, lambda v: 0.0)   # Casimir, d = 1, no shear
chk("Casimir R_kk = -2pi^3/45 (d=1), shear 0: theta(B) = %+.4f > 0 -- defocused, eq. (11)" % thC, thC > 0)

# sympy: the comparison inequality in closed form for a shear that is a constant s0 on [a,b]
vv, s0, a_, b_ = sp.symbols('v s0 a b', positive=True)
# with R = 0 and shear s0 on [a,b] only, theta' = -2 s0^2 - theta^2/2; theta(a)=0.
# Exact solution on [a,b]: theta = -2 s0 tan(s0 (v - a)); after b, theta' = -theta^2/2 keeps it negative.
th_exact = -2*s0*sp.tan(s0*(vv - a_))
chk("exact theta on the shear interval satisfies theta' = -2 s0^2 - theta^2/2 and theta(a) = 0",
    sp.simplify(sp.diff(th_exact, vv) + 2*s0**2 + th_exact**2/2) == 0 and th_exact.subs(vv, a_) == 0)
chk("and is strictly negative for v > a (tan > 0 on (0, pi/2))",
    th_exact.subs({s0: 1, a_: 0, vv: sp.Rational(1, 2)}) < 0)

# ---------------------------------------------------------------- z3: eqs (5)-(8)
print("(3b) z3: the finite algebra of eqs (5)-(8)")
try:
    import z3
    # unknowns at B in the E-basis: K components (K1=K2=0, K3>0, K4 free), Z components (Z3=0, Z4=0),
    # the derivative pairing D_ab := K_{a;b} Z^a Z^b, and the scalar q := Z^3_{;b} Z^b <= 0.
    K3, K4, q, D = z3.Reals('K3 K4 q D')
    s = z3.Solver()
    s.add(K3 > 0, q <= 0)
    # eq (5)-(6): 0 = D + K_a Z^a_{;b} Z^b with only a = 3 contributing (Z^4 = 0, K^1 = K^2 = 0),
    # and K_3 = +K^3 for the spacelike E_3 (metric +1):
    s.add(D + K3*q == 0)
    s.add(z3.Not(D >= 0))            # try to refute eq. (7)
    chk("eq. (7) K_{a;b} Z^a Z^b >= 0 follows from (5)-(6) with Z^3_{;b}Z^b <= 0, K^3 > 0  [z3: unsat]",
        s.check() == z3.unsat)
    # eq. (8): with Z = E1 and Z = E2 both giving >= 0, theta = K^1_{;1} + K^2_{;2} >= 0
    k11, k22 = z3.Reals('k11 k22')
    s2 = z3.Solver(); s2.add(k11 >= 0, k22 >= 0, z3.Not(k11 + k22 >= 0))
    chk("eq. (8) theta = K^m_{;m} >= 0 at B  [z3: unsat]", s2.check() == z3.unsat)
    # and the contradiction with eq. (4):
    th = z3.Real('th'); s3 = z3.Solver(); s3.add(th < 0, th >= 0)
    chk("eq. (4) theta < 0 (WEC + generic) and eq. (8) theta >= 0 (Condition 1) are jointly unsat",
        s3.check() == z3.unsat)
    # VACUITY GUARD: the hypotheses themselves are satisfiable
    s4 = z3.Solver(); s4.add(K3 > 0, q <= 0, D + K3*q == 0)
    chk("vacuity guard: hypotheses of (5)-(7) are satisfiable", s4.check() == z3.sat)
except ImportError:
    print("  z3 not installed: pip install z3-solver  (skipped)")

# ---------------------------------------------------------------- (4) composite.py
print("(4) composite.py:90-93, 116-117 -- a ray with T_kk = 0 along its whole length")
# On such a ray R_kk = 0 exactly; with any non-zero Weyl shear (a compact source's tidal
# field gives it) the same integration yields theta(B) < 0 -- Condition 1 fails, i.e. the
# ray is NOT the earliest among its neighbours -- unless a conjugate point precedes B,
# after which the ray is not achronal and Condition 1 fails for that reason instead.
thV = integrate(lambda v: 0.0, lambda v: 0.05*math.exp(-20*(v-0.4)**2))
chk("vacuum ray, Weyl shear only: theta(B) = %+.4e < 0 => Olum's Condition 1 cannot hold on it" % thV, thV < 0)
print("    => Olum's conclusion 'WEC violated at some point OF P' is not met by exotic matter the ray")
print("       never crosses.  composite.py:116-117 cites the theorem for a requirement it does not state.")

print()
print("RESULT: %d failures" % FAIL)
sys.exit(1 if FAIL else 0)
