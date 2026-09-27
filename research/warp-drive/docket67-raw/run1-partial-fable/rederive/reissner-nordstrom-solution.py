#!/usr/bin/env python3
"""DOCKET 67 -- re-derivation of the Reissner-Nordstrom facts the warp board uses.

Audits the result key 'reissner-nordstrom-solution' as the tree uses it
(certify.py:136-142, drivensource.py:94-131,420-424,525-559, specthm.py:872-898,
1801-1807, ledger.py:385-391, tolman.py:437-475,1288-1311, overturn.py:41-52,
phase1.py:405-407 / charge.py:32, throatmass.py:269-275,342-347).

What is checked, and how:

  A. The RN metric is DERIVED from the Einstein-Maxwell equations, not assumed:
     static spherically symmetric ansatz ds^2 = -f dt^2 + dr^2/h + r^2 dOmega^2,
     radial field F_tr = -q(r) (Gaussian, G = c = 1: T = (1/4 pi)(F F - g F^2/4)).
     Maxwell fixes q = C sqrt(f/h)/r^2; T^t_t = T^r_r with G^t_t - G^r_r forces
     f = h (up to the time rescaling); G^t_t = 8 pi T^t_t then integrates to
     h = 1 - 2M/r + Q^2/r^2; every remaining component is checked to vanish.
     Carroll gr-qc/9712019 eq. (7.107)-(7.113) is the source restated; the tree
     never derives the metric (drivensource.py:94-98 solves only MS-r/MS-t).
  B. The Misner-Sharp mass is COMPUTED from the metric by its definition
     E = (r/2)(1 - g^{-1}(dr,dr)) (Hayward gr-qc/9408002 eq. (4)/(27)), giving
     m = M - Q^2/2r; the energy density rho = -T^t_t = Q^2/8 pi r^4; the first
     law dm/dr = 4 pi r^2 rho (Hayward (28a)); sign region; central limit;
     Kretschmann scalar (true singularity at r = 0).
  C. The energy density is positive for EVERY unit timelike observer, not only
     the static one, so 'rho > 0 everywhere' holds also between the horizons
     where the static frame does not exist (the tree states it without proof).
  D. Horizons r_pm, the Cauchy-horizon inequality Q^2/2M < r_- for 0 < Q <= M,
     the series 1 - sqrt(1-y) - y/2 = y^2/8 + y^3/16 + O(y^4) (tolman.py:471-472),
     r_c/r_- = (1 + sqrt(1-q^2))/2 (drivensource.py:366-368), the M = 1,
     Q = 4/5 table (tolman.py:453-456), and the SI translation
     r_c = Q^2/(8 pi eps0 c^2 M) = 5.0e-8 m kg per C^2 (drivensource.py:534)
     under CODATA 2018 and 2022.
  E. z3: the tree's obligation E1 (m < 0 <=> 2 M R < Q^2) with a vacuity guard,
     the Cauchy-horizon containment as a real-arithmetic obligation, and the
     observer-independence of rho > 0.
  F. Hayward Proposition 2 cross-check: a central singularity with E < 0 is
     temporal (timelike) and untrapped -- Carroll's 'r = 0 is a timelike line'.

Exit 0 iff every check passes.  Nothing here is repaired; discrepancies are
recorded in the printed ledger and the audit JSON.
"""
import math
import sys
import time
from fractions import Fraction as Fr

import sympy as sp

FAIL = []
T0 = time.time()


def chk(label, ok):
    print(("  PASS  " if ok else "  FAIL  ") + label)
    if not ok:
        FAIL.append(label)


t, r, th, ph = sp.symbols("t r theta phi", real=True)
M, Q = sp.symbols("M Q", positive=True)
x = [t, r, th, ph]


def christoffel(g, ginv):
    n = 4
    G = [[[0] * n for _ in range(n)] for _ in range(n)]
    for a in range(n):
        for b in range(n):
            for c in range(n):
                G[a][b][c] = sp.cancel(sum(ginv[a, d] * (sp.diff(g[d, b], x[c]) + sp.diff(g[d, c], x[b]) - sp.diff(g[b, c], x[d])) for d in range(n)) / 2)
    return G


def riemann(G):
    """R^a_{bcd}"""
    n = 4
    Rm = [[[[0] * n for _ in range(n)] for _ in range(n)] for _ in range(n)]
    for a in range(n):
        for b in range(n):
            for c in range(n):
                for d in range(n):
                    if c >= d:
                        continue
                    v = sp.diff(G[a][b][d], x[c]) - sp.diff(G[a][b][c], x[d]) + sum(G[a][c][e] * G[e][b][d] - G[a][d][e] * G[e][b][c] for e in range(n))
                    v = sp.cancel(v)
                    Rm[a][b][c][d] = v
                    Rm[a][b][d][c] = -v
    return Rm


def ricci_from_riemann(Rm):
    n = 4
    R = sp.zeros(n, n)
    for b in range(n):
        for d in range(n):
            R[b, d] = sp.cancel(sum(Rm[a][b][a][d] for a in range(n)))
    return R


# ---------------------------------------------------------------- A. derive RN
print("A. Reissner-Nordstrom DERIVED from Einstein-Maxwell (Gaussian, G = c = 1)")
f = sp.Function("f")(r)
h = sp.Function("h")(r)
g = sp.diag(-f, 1 / h, r**2, r**2 * sp.sin(th) ** 2)
ginv = sp.diag(-1 / f, h, 1 / r**2, 1 / (r**2 * sp.sin(th) ** 2))
Gam = christoffel(g, ginv)
Rm = riemann(Gam)
Ric = ricci_from_riemann(Rm)
Rs = sp.cancel(sum(ginv[a, a] * Ric[a, a] for a in range(4)))
Ein_mixed = sp.Matrix(4, 4, lambda a, b: sp.cancel(ginv[a, a] * (Ric[a, b] - Rs * g[a, b] / 2)))  # G^a_b
print("     (Einstein tensor built: %.1f s)" % (time.time() - T0))

qf = sp.Function("q")(r)
F = sp.zeros(4, 4)
F[0, 1] = -qf
F[1, 0] = qf
Fup = ginv * F * ginv  # F^{ab}
sqrtg = sp.sqrt(f / h) * r**2 * sp.sin(th)
maxwell = sp.simplify(sp.diff(sqrtg * Fup[1, 0], r) / sp.sin(th))  # d_r(sqrt(-g) F^{rt}) = 0
qsol = sp.dsolve(sp.Eq(maxwell, 0), qf).rhs
print("     Maxwell d_r(sqrt(-g) F^{rt}) = 0  =>  q(r) =", qsol)
Cq = [s for s in qsol.free_symbols if s.name == "C1"][0]
chk("Maxwell: q(r) = C sqrt(f/h)/r^2 (Gauss's law in the curved static metric)",
    sp.simplify((qsol * r**2 / Cq) ** 2 - f / h) == 0)
F2 = sum(F[a, b] * Fup[a, b] for a in range(4) for b in range(4))
Tlow = (F * ginv * F.T - g * F2 / 4) / (4 * sp.pi)  # T_ab
Tmix = sp.Matrix(4, 4, lambda a, b: sp.simplify(ginv[a, a] * Tlow[a, b]))  # T^a_b
Tmix_q = Tmix.subs(qf, qsol)
chk("T^t_t = T^r_r = -q^2/(8 pi) for the radial field (so G^t_t = G^r_r is forced)",
    sp.simplify(Tmix_q[0, 0] - Tmix_q[1, 1]) == 0)
chk("T^a_b traceless (V12)", sp.simplify(sum(Tmix_q[a, a] for a in range(4))) == 0)
# G^t_t - G^r_r = 0  =>  f'/f = h'/h  =>  f = c h
diff_tr = sp.simplify(Ein_mixed[0, 0] - Ein_mixed[1, 1])
print("     G^t_t - G^r_r =", diff_tr)
fsol = sp.dsolve(sp.Eq(diff_tr, 0), f).rhs
Cf = [s for s in fsol.free_symbols if s.name == "C1"][0]
chk("G^t_t = G^r_r  =>  f = C h (time rescaling; C = 1 by asymptotic flatness)", sp.simplify(fsol - Cf * h) == 0)
# now f = h, q = C/r^2 =: Q/r^2; solve G^t_t = 8 pi T^t_t for h
eq_tt = sp.simplify(Ein_mixed[0, 0].subs(f, h).doit() - 8 * sp.pi * Tmix_q[0, 0].subs(f, h).doit().subs(Cq, Q))
print("     G^t_t - 8 pi T^t_t (f = h, q = Q/r^2) =", eq_tt)
hsol = sp.dsolve(sp.Eq(eq_tt, 0), h).rhs
Ch = [s for s in hsol.free_symbols if s.name == "C1"][0]
print("     =>  h(r) =", hsol)
h_rn = hsol.subs(Ch, -2 * M)  # the constant is fixed by the Schwarzschild (Q -> 0) limit / ADM mass
chk("h = 1 - 2M/r + Q^2/r^2 (ADM mass M fixes the constant)", sp.simplify(h_rn - (1 - 2 * M / r + Q**2 / r**2)) == 0)
sub = {f: h_rn, h: h_rn, qf: Q / r**2}
resid = sp.Matrix(4, 4, lambda a, b: sp.simplify((Ein_mixed[a, b] - 8 * sp.pi * Tmix[a, b]).subs(sub).doit()))
chk("ALL components of G^a_b - 8 pi T^a_b vanish on RN (theta-theta is the consistency check)", resid == sp.zeros(4, 4))
chk("Maxwell equation holds on RN with q = Q/r^2", sp.simplify(maxwell.subs(sub).doit()) == 0)
print("     (section A done: %.1f s)" % (time.time() - T0))

# ---------------------------------------------------- B. Misner-Sharp mass etc.
print("B. Misner-Sharp mass computed by definition, first law, sign region, limit")
g_rn = sp.diag(-h_rn, 1 / h_rn, r**2, r**2 * sp.sin(th) ** 2)
ginv_rn = sp.diag(-1 / h_rn, h_rn, 1 / r**2, 1 / (r**2 * sp.sin(th) ** 2))
grad_r2 = ginv_rn[1, 1]  # g^{ab} d_a r d_b r
m_ms = sp.simplify(r / 2 * (1 - grad_r2))  # Hayward eq. (4)
chk("E = (r/2)(1 - g^{-1}(dr,dr)) = M - Q^2/(2r)", sp.simplify(m_ms - (M - Q**2 / (2 * r))) == 0)
T_rn = Tmix.subs(sub).doit()
rho = sp.simplify(-T_rn[0, 0])
p_r = sp.simplify(T_rn[1, 1])
p_t = sp.simplify(T_rn[2, 2])
chk("rho = -T^t_t = Q^2/(8 pi r^4)", sp.simplify(rho - Q**2 / (8 * sp.pi * r**4)) == 0)
chk("p_r = -rho, p_t = +rho (tolman.py:439)", sp.simplify(p_r + rho) == 0 and sp.simplify(p_t - rho) == 0)
chk("first law dm/dr = 4 pi r^2 rho (Hayward (28a), static)", sp.simplify(sp.diff(m_ms, r) - 4 * sp.pi * r**2 * rho) == 0)
chk("conservation p_r' + (2/r)(p_r - p_t) = 0 (V12)", sp.simplify(sp.diff(p_r, r) + 2 / r * (p_r - p_t)) == 0)
chk("m = 0 exactly at r = Q^2/(2M)", sp.solve(sp.Eq(m_ms, 0), r) == [Q**2 / (2 * M)])
chk("m < 0 iff r < Q^2/(2M)  (sympy solve_univariate_inequality at M = 1, Q = 4/5: (0, 8/25))",
    sp.solve_univariate_inequality(m_ms.subs({M: 1, Q: sp.Rational(4, 5)}) < 0, r, relational=False) == sp.Interval.open(0, sp.Rational(8, 25)))
chk("m(0+) = -oo (no regular centre: Hayward's E = O(r^3) fails)", sp.limit(m_ms, r, 0, "+") == -sp.oo)
enc = sp.integrate(4 * sp.pi * r**2 * rho, r)
chk("indefinite integral of 4 pi r^2 rho is -Q^2/(2r) (drivensource.py:530)", sp.simplify(enc + Q**2 / (2 * r)) == 0)
Rsym = sp.Symbol("R", positive=True)
chk("int_0^R 4 pi r^2 rho dr diverges (the regular-centre integral does not exist)",
    sp.integrate(4 * sp.pi * r**2 * rho, (r, 0, Rsym)) == sp.oo)
chk("m(R) - 4 pi R^3 p_r(R) = M at every R (tolman.py V13)", sp.simplify(m_ms - 4 * sp.pi * r**3 * p_r - M) == 0)
chk("1/g_rr - 1 = (Q^2 - 2 M r)/r^2 (drivensource.py:528)", sp.simplify(h_rn - 1 - (Q**2 - 2 * M * r) / r**2) == 0)
Gam_rn = christoffel(g_rn, ginv_rn)
Rm_rn = riemann(Gam_rn)
K = 0
for a in range(4):
    for b in range(4):
        for c in range(4):
            for d in range(4):
                if Rm_rn[a][b][c][d] != 0:
                    # R^a_bcd R_a^bcd with a diagonal metric
                    K += Rm_rn[a][b][c][d] ** 2 * g_rn[a, a] * ginv_rn[b, b] * ginv_rn[c, c] * ginv_rn[d, d]
K = sp.simplify(K)
chk("Kretschmann = 48 M^2/r^6 - 96 M Q^2/r^7 + 56 Q^4/r^8 -> oo at r = 0 (true singularity, Carroll p.202)",
    sp.simplify(K - (48 * M**2 / r**6 - 96 * M * Q**2 / r**7 + 56 * Q**4 / r**8)) == 0)
print("     (section B done: %.1f s)" % (time.time() - T0))

# ------------------------------------ C. positivity for EVERY timelike observer
print("C. rho > 0 for every unit timelike observer, at every r (between the horizons too)")
chk("T^a_b = rho diag(-1,-1,+1,+1) exactly", sp.simplify(T_rn - rho * sp.diag(-1, -1, 1, 1)) == sp.zeros(4, 4))
# T_ab u^a u^b = rho(-(u_t u^t + u_r u^r) + (u_th u^th + u_ph u^ph)); normalisation u_a u^a = -1
# => u_t u^t + u_r u^r = -1 - A with A = u_th u^th + u_ph u^ph = r^2 (u^th)^2 + r^2 sin^2 (u^ph)^2 >= 0
# => T(u,u) = rho (1 + 2A) >= rho > 0.  Holds in every region, since only the normalisation is used.
ut, ur, uth, uph = sp.symbols("u_t u_r u_th u_ph", real=True)
uu = [ut, ur, uth, uph]
Tuu = sum(g_rn[a, a] * T_rn[a, a] * uu[a] ** 2 for a in range(4))  # T_ab u^a u^b, diagonal metric
ang = g_rn[2, 2] * uth**2 + g_rn[3, 3] * uph**2  # >= 0 always
norm_sub = {ut**2: (-1 - g_rn[1, 1] * ur**2 - ang) / g_rn[0, 0]}  # g_ab u^a u^b = -1
chk("T(u,u) = rho (1 + 2 A) with A = r^2 (u^th)^2 + r^2 sin^2 (u^ph)^2 >= 0 -- uses ONLY the normalisation, so it holds in every region",
    sp.simplify(Tuu.subs(norm_sub) - rho * (1 + 2 * ang)) == 0)
chk("DEC: rho >= |p_r| and rho >= |p_t| (equality: the field is null-dust-like radially)", sp.simplify(rho - sp.Abs(p_r)) == 0 and sp.simplify(rho - sp.Abs(p_t)) == 0)

# ----------------------------------------- D. horizons, Cauchy-horizon inequality
print("D. horizons, the inner-horizon containment, the tables, the SI translation")
rp, rm = M + sp.sqrt(M**2 - Q**2), M - sp.sqrt(M**2 - Q**2)
chk("h(r_pm) = 0", sp.simplify(h_rn.subs(r, rp)) == 0 and sp.simplify(h_rn.subs(r, rm)) == 0)
y = sp.Symbol("y", positive=True)
gap = 1 - sp.sqrt(1 - y) - y / 2
ser = sp.series(gap, y, 0, 4).removeO()
chk("r_-/M - (Q^2/2M)/M = y^2/8 + y^3/16 + O(y^4), y = Q^2/M^2 (tolman.py:471-472)", sp.simplify(ser - (y**2 / 8 + y**3 / 16)) == 0)
chk("gap = (1 - sqrt(1-y))^2 / 2 exactly, hence > 0 on (0, 1]", sp.simplify(gap - (1 - sp.sqrt(1 - y)) ** 2 / 2) == 0)
qs = sp.Symbol("q", positive=True)
ratio = (qs**2 / 2) / (1 - sp.sqrt(1 - qs**2))
chk("r_c/r_- = (1 + sqrt(1-q^2))/2 (drivensource.py:366-368)", sp.simplify(ratio - (1 + sp.sqrt(1 - qs**2)) / 2) == 0)
chk("r_c/r_- = 1/2 at extremal q = 1", sp.simplify(ratio.subs(qs, 1)) == sp.Rational(1, 2))
chk("r_c/r_- -> 1 as q -> 0+ (the containment is NOT uniform: it is marginal at small charge)", sp.limit(ratio, qs, 0, "+") == 1)
Mf, Q2 = Fr(1), Fr(4, 5) ** 2
chk("m = 0 at R = Q^2/2M = 8/25 = 0.32 (tolman.py:453)", Q2 / (2 * Mf) == Fr(8, 25))
d = math.sqrt(1 - 0.8**2)
chk("horizons r_- = 0.4, r_+ = 1.6 at M = 1, Q = 0.8 (tolman.py:454)", abs((1 - d) - 0.4) < 1e-12 and abs((1 + d) - 1.6) < 1e-12)
chk("0.32 < r_- = 0.4: the m < 0 region is inside the Cauchy horizon", Fr(8, 25) < Fr(2, 5))
for qv in (0.5, 0.9, 0.99, 1.0):
    rc, rmin = qv * qv / 2, 1 - math.sqrt(1 - qv * qv)
    chk("drivensource.py:555-557 table q = %.2f: r_c/M = %.5f <= r_-/M = %.5f" % (qv, rc, rmin), rc <= rmin + 1e-15)
# charge.py:16-24 table: Phi = -M/r + Q^2/(2r^2) > 0 iff r < Q^2/(2M); horizon r_+
for qv, phi_below, rplus in ((0.5, 0.125, 1.86603), (0.9, 0.405, 1.43589), (0.99, 0.49005, 1.14107), (1.0, 0.5, 1.0)):
    chk("charge.py table q = %.2f: Q^2/2M = %.5f, r_+ = %.5f" % (qv, phi_below, rplus),
        abs(qv * qv / 2 - phi_below) < 1e-5 and abs(1 + math.sqrt(1 - qv * qv) - rplus) < 1e-5)
# SI translation: Q_geom = Q sqrt(G/(4 pi eps0))/c^2, M_geom = G M/c^2  =>  r_c = Q^2/(8 pi eps0 c^2 M), G cancels
c = 299792458.0
for label, eps0 in (("CODATA 2018", 8.8541878128e-12), ("CODATA 2022", 8.8541878188e-12)):
    X = 1.0 / (8 * math.pi * eps0 * c * c)
    chk("%s: r_c*M per C^2 = %.10e kg m  (drivensource.py:534 pins 5.0e-08 within 1e-9)" % (label, X), abs(X - 5.0e-8) < 1e-9)
chk("the 2018 -> 2022 eps0 move shifts r_c by 7e-10 relative: no conclusion moves", abs(8.8541878188e-12 / 8.8541878128e-12 - 1) < 1e-8)
e_, me = 1.602176634e-19, 9.1093837015e-31
r_c_e = e_ * e_ / (8 * math.pi * 8.8541878128e-12 * c * c * me)
chk("electron: r_c = %.4e m = r_e/2 (half the classical electron radius)" % r_c_e, abs(r_c_e - 2.8179403262e-15 / 2) < 1e-24)
chk("4472 C on 1 m with 1 kg bare mass: r_c/a = X/(X + mu a) = 0.4999848 (drivensource.py:546)",
    abs((4472.0**2 * 5.0e-8 / (1.0 / (8 * math.pi * 8.8541878128e-12 * c * c) * 8 * math.pi * 8.8541878128e-12 * c * c * 5.0e-8)) and
        (lambda X: X / (X + 1.0))(4472.0**2 / (8 * math.pi * 8.8541878128e-12 * c * c)) - 0.4999847997) < 1e-9)

# ----------------------------------------------------------------- E. z3
print("E. z3 obligations (with vacuity guards)")
try:
    import z3
    R_, M_, Q_, m_ = z3.Reals("R M Q m")
    rn = [R_ > 0, M_ > 0, Q_ > 0, m_ == M_ - Q_ * Q_ / (2 * R_)]
    s = z3.Solver(); s.add(rn + [m_ < 0]); chk("guard: RN with m < 0 is satisfiable", s.check() == z3.sat)
    s = z3.Solver(); s.add(rn + [m_ > 0]); chk("guard: RN with m > 0 is satisfiable", s.check() == z3.sat)
    s = z3.Solver(); s.add(rn); s.add(z3.Not((m_ < 0) == (2 * M_ * R_ < Q_ * Q_)))
    chk("E1: m < 0 <=> 2 M R < Q^2 (drivensource.py:420-424) -- no counterexample", s.check() == z3.unsat)
    sq = z3.Real("s")
    s = z3.Solver(); s.add(M_ > 0, Q_ > 0, Q_ <= M_, sq >= 0, sq * sq == M_ * M_ - Q_ * Q_)
    s.add(z3.Not(Q_ * Q_ / (2 * M_) <= M_ - sq))
    chk("Q^2/(2M) <= r_- for every 0 < Q <= M -- no counterexample (nonlinear real arithmetic)", s.check() == z3.unsat)
    s = z3.Solver(); s.add(M_ > 0, Q_ > 0, Q_ <= M_, sq >= 0, sq * sq == M_ * M_ - Q_ * Q_, Q_ * Q_ / (2 * M_) < M_ - sq)
    chk("guard: strict containment is satisfiable", s.check() == z3.sat)
    s = z3.Solver(); s.add(M_ > 0, Q_ > M_)  # over-extremal: no horizon, r_c = Q^2/2M > M/2 is NAKED
    s.add(Q_ * Q_ / (2 * M_) <= M_ / 2)
    chk("Q > M: Q^2/(2M) > M/2 always (the m < 0 region is naked when there is no horizon)", s.check() == z3.unsat)
    rho_, A_ = z3.Reals("rho A")
    s = z3.Solver(); s.add(rho_ > 0, A_ >= 0, z3.Not(rho_ * (1 + 2 * A_) > 0))
    chk("T(u,u) > 0 for every observer given rho > 0 -- no counterexample", s.check() == z3.unsat)
except ImportError:
    chk("z3 available", False)

# ----------------------------------------------------------------- F. Hayward
print("F. Hayward Proposition 2 cross-check")
chk("RN: E -> -oo as r -> 0 and h -> +oo there: E < r/2, untrapped centre (Hayward Prop. 2: temporal singularity)",
    sp.limit(h_rn, r, 0, "+") == sp.oo)
chk("trapped region E > r/2 is exactly r_- < r < r_+ (h < 0), at M = 1, Q = 4/5: (2/5, 8/5)",
    sp.solve_univariate_inequality(h_rn.subs({M: 1, Q: sp.Rational(4, 5)}) < 0, r, relational=False) == sp.Interval.open(sp.Rational(2, 5), sp.Rational(8, 5)))

print()
print("RESULT:", ("FAILURES: %s" % FAIL) if FAIL else "all checks pass", "(%.1f s)" % (time.time() - T0))
sys.exit(1 if FAIL else 0)
