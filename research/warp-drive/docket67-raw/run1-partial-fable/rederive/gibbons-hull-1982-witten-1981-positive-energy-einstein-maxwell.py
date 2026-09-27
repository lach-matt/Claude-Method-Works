#!/usr/bin/env python3
"""
DOCKET 67, result 22/286 -- the positive energy theorem for Einstein-Maxwell
(Gibbons & Hull 1982; Gibbons-Hawking-Horowitz-Perry 1983; Witten 1981 for the
spinor method), m >= |Q|, AS THE TREE USES IT in drivensource.py / charge.py.

What is checkable here is finite and closed-form, and it is checked in six parts:

  P1  sympy : Misner-Sharp mass of Reissner-Nordstrom is m(r) = M - Q^2/(2r),
              so m < 0 exactly on r < r_c = Q^2/(2M)          (drivensource 33-40)
  P2  sympy : r_c / r_-  =  (1 + sqrt(1 - q^2)) / 2  for q = Q/M   (drivensource 166-169, 366-368)
  P3  z3    : FORALL q in (0, 1] : r_c <= r_-   (the tree's "inside the INNER horizon"),
              and the ratio is 1/2 at q = 1, and -> 1 only as q -> 0
  P4  numeric: the owner's own table at q = 0.5, 0.9, 0.99, 1.0 (drivensource 553-559)
  P5  sympy : the theorem's charge-density hypothesis against a static charged
              thin shell (Israel junction, flat inside / RN outside):
              M = mu - (mu^2 - Q^2)/(2a).  Q > M is REACHED for every shell with
              a > (Q + mu)/2 ... i.e. the bound Q <= M is not a fact about charged
              bodies; it is a fact about bodies whose matter density dominates
              their charge density (the charged dominant energy condition).
  P6  numeric: the charged dominant energy condition |rho_e| <= mu_matter in
              geometric units, for the electron, the proton, and drivensource's
              own witness (4472 C on a 1 m shell of 1 kg bare mass) -- with the
              constants the authors had (CODATA 1973, recalled) and the constants
              the owner carries (CODATA 2018, drivensource.py:278-280, READ).

Exit 1 on any failure.  Stdlib + sympy; z3 if importable (pip install z3-solver).
"""
import math, sys
import sympy as sp

FAIL = []
def chk(label, ok):
    print(("  ok   " if ok else "  FAIL ") + label)
    if not ok:
        FAIL.append(label)

# ------------------------------------------------------------------ P1
print("P1  Misner-Sharp mass of Reissner-Nordstrom")
r, M, Q = sp.symbols("r M Q", positive=True)
f = 1 - 2*M/r + Q**2/r**2                    # g^{rr} = f, geometric units G=c=1
m_MS = sp.simplify(r*(1 - f)/2)              # 1 - 2m/r = g^{rr} g^{rr}? no: m = r(1 - g^{rr}... ) see below
# Misner-Sharp: 1 - 2m/r = g^{ab} d_a r d_b r = g^{rr} = f  for a static diagonal metric
chk("m_MS(r) == M - Q^2/(2r)", sp.simplify(m_MS - (M - Q**2/(2*r))) == 0)
r_c = sp.solve(sp.Eq(m_MS, 0), r)[0]
chk("m_MS = 0 at r_c = Q^2/(2M)", sp.simplify(r_c - Q**2/(2*M)) == 0)
chk("m_MS < 0 below r_c (sample r = r_c/2)", sp.simplify(m_MS.subs(r, r_c/2)) == -M)

# ------------------------------------------------------------------ P2
print("P2  r_c / r_-  in closed form")
q = sp.symbols("q", positive=True)
r_minus = M - sp.sqrt(M**2 - Q**2)           # inner horizon, needs Q <= M
ratio = sp.simplify((Q**2/(2*M)) / r_minus)
ratio_q = sp.simplify(ratio.subs(Q, q*M))
target = (1 + sp.sqrt(1 - q**2))/2
chk("r_c/r_- == (1 + sqrt(1 - q^2))/2 for q = Q/M", sp.simplify(ratio_q - target) == 0)
chk("ratio(q=1) == 1/2", sp.simplify(target.subs(q, 1)) == sp.Rational(1, 2))
chk("ratio -> 1 as q -> 0+", sp.limit(target, q, 0, "+") == 1)
# horizons exist iff Q <= M (this is what the tree's use of Q <= M buys)
chk("r_+- real iff Q <= M: discriminant M^2 - Q^2", sp.simplify(sp.expand((M + sp.sqrt(M**2 - Q**2))*(M - sp.sqrt(M**2 - Q**2))) - Q**2) == 0)

# ------------------------------------------------------------------ P3
print("P3  z3: FORALL q in (0,1]: r_c <= r_-  (negation must be unsat)")
try:
    import z3
    qz, s = z3.Reals("q s")
    S = z3.Solver()
    S.add(qz > 0, qz <= 1, s >= 0, s*s == 1 - qz*qz)          # s = sqrt(1 - q^2)
    S.add(z3.Not((1 + s)/2 <= 1))                              # negation of the claim
    res = S.check()
    chk("z3: no q in (0,1] with r_c/r_- > 1  (%s)" % res, res == z3.unsat)
    # strictness: r_c < r_- for every q in (0,1]  (ratio == 1 needs s == 1 i.e. q == 0)
    S2 = z3.Solver(); S2.add(qz > 0, qz <= 1, s >= 0, s*s == 1 - qz*qz, (1 + s)/2 >= 1)
    chk("z3: ratio == 1 unreachable on (0,1] (strict inside)  (%s)" % S2.check(), S2.check() == z3.unsat)
    # vacuity guard: the hypotheses themselves are satisfiable
    S3 = z3.Solver(); S3.add(qz > 0, qz <= 1, s >= 0, s*s == 1 - qz*qz)
    chk("z3 vacuity guard: hypotheses satisfiable (%s)" % S3.check(), S3.check() == z3.sat)
except ImportError:
    print("  (z3 not importable -- P3 skipped; sympy P2 already carries the algebra)")

# ------------------------------------------------------------------ P4
print("P4  the owner's own table (drivensource.py:553-559)")
def inner_horizon_ratio(qq): return 0.5*(1.0 + math.sqrt(1.0 - qq*qq))
print("     %-6s %10s %10s %10s" % ("q", "r_c/M", "r_-/M", "r_c/r_-"))
for qq in (0.5, 0.9, 0.99, 1.0):
    rc, rm = qq*qq/2, 1 - math.sqrt(1 - qq*qq)
    print("     %-6.2f %10.5f %10.5f %10.6f" % (qq, rc, rm, inner_horizon_ratio(qq)))
    chk("q=%.2f: rc/rm == closed form" % qq, abs(rc/rm - inner_horizon_ratio(qq)) < 1e-12)
    chk("q=%.2f: inside the inner horizon" % qq, inner_horizon_ratio(qq) <= 1.0)
chk("q=1: ratio == 0.5 to 1e-12", abs(inner_horizon_ratio(1.0) - 0.5) < 1e-12)

# ------------------------------------------------------------------ P5
print("P5  static charged thin shell (Israel junction): can Q exceed M?")
mu, a = sp.symbols("mu a", positive=True)
# flat interior, RN exterior, static shell of proper mass mu at areal radius a:
#   sqrt(1) - sqrt(1 - 2M/a + Q^2/a^2) = mu/a   =>  M = mu - (mu^2 - Q^2)/(2a)
Msol = sp.solve(sp.Eq(1 - sp.sqrt(1 - 2*M/a + Q**2/a**2), mu/a), M)
chk("one root", len(Msol) == 1)
M_shell = sp.simplify(Msol[0])
chk("M_shell == mu - (mu^2 - Q^2)/(2a)", sp.simplify(M_shell - (mu - (mu**2 - Q**2)/(2*a))) == 0)
# Q > M  <=>  Q - mu + (mu^2 - Q^2)/(2a) > 0  <=>  (Q - mu)(1 - (Q + mu)/(2a)) > 0
#         <=>  for Q > mu :  a > (Q + mu)/2      (checked as an identity)
diff = sp.simplify(Q - M_shell - (Q - mu)*(1 - (Q + mu)/(2*a)))
chk("Q - M == (Q - mu)(1 - (Q + mu)/(2a))", diff == 0)
# a witness in geometric units: mu = 0.01, Q = 1, a = 10  ->  M = 0.01 + (1 - 1e-4)/20 = 0.059995 < Q
w = M_shell.subs({mu: sp.Rational(1, 100), Q: 1, a: 10})
chk("witness mu=0.01, Q=1, a=10: M = %s < Q = 1" % w, w < 1)
# and the shell's exterior is superextremal RN: no horizon at all (M^2 - Q^2 < 0)
chk("witness exterior has M^2 - Q^2 < 0 (no horizon)", (w**2 - 1) < 0)
# the shell is also outside where any horizon could be: a > M
chk("witness shell radius a=10 > M", 10 > w)
# so the theorem's m >= |Q| does NOT hold for this data: which hypothesis fails?
# the surface charge density exceeds the surface mass density by Q/mu = 100 --
# the charged dominant energy condition (matter density >= |charge density|) fails.
chk("shell violates charged DEC: Q/mu = 100 > 1", sp.Rational(1, 1)/sp.Rational(1, 100) > 1)

# ------------------------------------------------------------------ P6
print("P6  charged dominant energy condition against real matter, then vs now")
def q_over_m(e_C, m_kg, G, eps0, c):
    # geometric charge  Q_geom = e * sqrt(G/(4 pi eps0)) / c^2 ; geometric mass M_geom = G m / c^2
    return (e_C*math.sqrt(G/(4*math.pi*eps0))/c**2) / (G*m_kg/c**2)
# constants the owner carries (READ: drivensource.py:278-280, CODATA 2018)
G18, eps18, c = 6.67430e-11, 8.8541878128e-12, 299792458.0
e18, me18, mp18 = 1.602176634e-19, 9.1093837015e-31, 1.67262192369e-27   # CODATA 2018 (recalled)
# constants of the authors' era (CODATA 1973, recalled -- NOT read at source this pass)
G73, eps73 = 6.6720e-11, 8.854187818e-12
e73, me73, mp73 = 1.6021892e-19, 9.109534e-31, 1.6726485e-27
for lab, e_, me_, mp_, G_, eps_ in (("CODATA 2018", e18, me18, mp18, G18, eps18),
                                    ("CODATA 1973", e73, me73, mp73, G73, eps73)):
    qe, qp = q_over_m(e_, me_, G_, eps_, c), q_over_m(e_, mp_, G_, eps_, c)
    print("     %s: electron |Q|/M = %.4e   proton |Q|/M = %.4e" % (lab, qe, qp))
    chk("%s: electron violates |rho_e| <= mu by > 1e21" % lab, qe > 1e21)
    chk("%s: proton violates |rho_e| <= mu by > 1e18" % lab, qp > 1e18)
q73, q18 = q_over_m(e73, me73, G73, eps73, c), q_over_m(e18, me18, G18, eps18, c)
print("     electron ratio moved by %.2e relative between 1973 and 2018 constants" % abs(q73/q18 - 1))
chk("the datum's move is < 1e-3 relative: conclusion unmoved", abs(q73/q18 - 1) < 1e-3)
# drivensource's own witness: 4472 C on a 1 m shell, 1 kg bare mass
Qc, a_m, mu_kg = 4472.0, 1.0, 1.0
X = Qc*Qc/(8*math.pi*eps18*c*c)                 # kg m, drivensource.X_of_Q
M_kg = mu_kg + X/a_m                            # ADM mass ~ bare + exterior field energy
Q_geom = Qc*math.sqrt(G18/(4*math.pi*eps18))/c**2
M_geom = G18*M_kg/c**2
print("     drivensource witness: Q_geom = %.4e m, M_geom = %.4e m, Q/M = %.4e" % (Q_geom, M_geom, Q_geom/M_geom))
chk("owner's witness has Q/M > 1e13 -- outside q in (0,1]", Q_geom/M_geom > 1e13)
chk("owner's r_c/a = X/(mu a + X) = %.10f (drivensource: 0.4999847997)" % (X/(mu_kg*a_m + X)), abs(X/(mu_kg*a_m + X) - 0.4999847997) < 1e-9)
r_c_m = Q_geom**2/(2*M_geom)                    # metres, RN formula in geometric units
print("     witness r_c = Q^2/(2M) = %.6f m against a = %.1f m; M^2 - Q^2 = %.3e m^2" % (r_c_m, a_m, M_geom**2 - Q_geom**2))
chk("witness: M^2 - Q^2 < 0, so NO horizon exists and r_- (inner_horizon_ratio) is undefined there",
    M_geom**2 - Q_geom**2 < 0)
chk("witness: r_c = 0.5 m < a = 1 m -- it is N2's r_c <= a, not the inner horizon, that closes it",
    abs(r_c_m/a_m - 0.4999847997) < 1e-6 and r_c_m < a_m)

print()
if FAIL:
    print("FAILED:", *FAIL, sep="\n  "); sys.exit(1)
print("ALL CHECKS PASS -- the arithmetic the tree states agrees; the theorem's charge-density\n"
      "hypothesis is the one the tree's phrasing 'forces Q <= M' drops, and P5/P6 show it is not idle.")
