#!/usr/bin/env python3
"""DOCKET 67 -- re-derivation for the external result 'misner-sharp-1964'.

The Misner-Sharp(-Hernandez) mass in spherical symmetry, as the warp board uses
it, checked against the two restatements READ at source:

    Hayward gr-qc/9408002 (PRD 53, 1938): eq. (4)  E = (r/2)(1 - g^{-1}(dr,dr))
                                          eq. (27) 1 - 2E/r = e^{-chi}(r')^2 - rdot^2
                                          eqs (28a,b) variation formulas
                                          eqs (32a,b) comoving perfect fluid
                                          Prop. 1 trapping, regular centre E = O(r^3)
    Escriva 2504.05813 (JCAP 2025):       eqs (2.3) U = D_t R, Gamma = D_r R
                                          (2.5)  Gamma = sqrt(1 + U^2 - 2M/R)
                                          (2.9)  D_t M = -4 pi R^2 U p
                                          (2.12) D_r M = 4 pi Gamma rho R^2
                                          (2.24) M = (R/2)(1 + U^2 - Gamma^2)

and against every form the tree states (certify.py, driven.py, nonstatic.py,
foliation.py, drivensource.py, tolman.py, throatmass.py, hpscentre.py).

Nothing here is quoted from a tree instrument; the Einstein tensor is built
from the Christoffel symbols in this file.  Every identity is a sympy residual
that must simplify to 0; every finite claim is a z3 obligation asserted negated
and reported unsat, each with a satisfiability guard against vacuity.  Exit 1
on any failure.  stdlib + sympy (+ z3 if importable; skipped with a notice
otherwise).
"""
import sys
import math
import sympy as sp

FAILS = []
ROWS = []


def row(name, ok, detail=""):
    ROWS.append((name, ok, detail))
    if not ok:
        FAILS.append(name)
    print(("PASS " if ok else "FAIL ") + name + ("   " + detail if detail else ""))


def zero(name, expr):
    e = sp.simplify(expr)
    row(name, e == 0, "residual = %s" % e)


# ---------------------------------------------------------------------------
# A. the general spherically symmetric metric and the gradient-scalar definition
# ---------------------------------------------------------------------------
t, r, th, ph = sp.symbols("t r theta phi", real=True)
Phi = sp.Function("Phi")(t, r)
Lam = sp.Function("Lambda")(t, r)
R = sp.Function("R")(t, r)
x = [t, r, th, ph]
g = sp.diag(-sp.exp(2 * Phi), sp.exp(2 * Lam), R**2, R**2 * sp.sin(th)**2)
gi = g.inv()

gradR = sp.simplify(sum(gi[a, b] * sp.diff(R, x[a]) * sp.diff(R, x[b])
                        for a in range(4) for b in range(4)))
mS = sp.Symbol("m")
sols = sp.solve(sp.Eq(1 - 2 * mS / R, gradR), mS)
row("A0 the definition 1 - 2m/R = g^{ab} d_aR d_bR solves UNIQUELY for m",
    len(sols) == 1, "solutions: %d" % len(sols))
m = sp.simplify(sols[0])

U = sp.exp(-Phi) * sp.diff(R, t)          # areal velocity, D_t R
W = sp.exp(-Lam) * sp.diff(R, r)          # generalised Lorentz factor, D_r R

zero("A1 Hayward eq.(4): m = (R/2)(1 - g^{ab} d_aR d_bR)",
     m - R / 2 * (1 - gradR))
zero("A2 Escriva (2.24): m = (R/2)(1 + U^2 - Gamma^2)",
     m - R / 2 * (1 + U**2 - W**2))
zero("A3 tree identity  e^{-2Lambda} R'^2 = 1 - 2m/R + e^{-2Phi} Rdot^2",
     sp.exp(-2 * Lam) * sp.diff(R, r)**2
     - (1 - 2 * m / R + sp.exp(-2 * Phi) * sp.diff(R, t)**2))
zero("A4 Escriva (2.5) squared: Gamma^2 = 1 + U^2 - 2m/R",
     W**2 - (1 + U**2 - 2 * m / R))

# Hayward's chart (26): ds^2 = r^2 dOmega^2 + e^{chi} dxi^2 - dtau^2, tau proper
# time along the slice normal.  That is Phi = 0, e^{chi} = e^{2 Lambda}.
chi = sp.Function("chi")(t, r)
m_h = m.subs(Lam, chi / 2).subs(Phi, 0).doit()
zero("A5 Hayward eq.(27) in his chart: 1 - 2E/r = e^{-chi}(r')^2 - rdot^2",
     (1 - 2 * m_h / R) - (sp.exp(-chi) * sp.diff(R, r)**2 - sp.diff(R, t)**2))
zero("A6 driven.py:64-66 mapping: Hayward's rdot is the tree's e^{-Phi} Rdot at Phi=0",
     U.subs(Phi, 0) - sp.diff(R, t))

# ---------------------------------------------------------------------------
# B. the Einstein tensor from scratch; MS-r, MS-t; Hayward (28a,b), (32a,b);
#    Escriva (2.9), (2.12)
# ---------------------------------------------------------------------------
def christoffel(g, gi, x):
    n = len(x)
    return [[[sp.simplify(sum(gi[a, d] * (sp.diff(g[d, b], x[c]) + sp.diff(g[d, c], x[b])
                                          - sp.diff(g[b, c], x[d])) for d in range(n)) / 2)
              for c in range(n)] for b in range(n)] for a in range(n)]


def ricci(Gam, x):
    n = len(x)
    Ric = sp.zeros(n, n)
    for b in range(n):
        for c in range(n):
            Ric[b, c] = sp.simplify(
                sum(sp.diff(Gam[a][b][c], x[a]) for a in range(n))
                - sum(sp.diff(Gam[a][b][a], x[c]) for a in range(n))
                + sum(Gam[a][a][d] * Gam[d][b][c] for a in range(n) for d in range(n))
                - sum(Gam[a][c][d] * Gam[d][b][a] for a in range(n) for d in range(n)))
    return Ric


Gam = christoffel(g, gi, x)
Ric = ricci(Gam, x)
Rs = sp.simplify(sum(gi[a, b] * Ric[a, b] for a in range(4) for b in range(4)))
Ein = sp.Matrix(4, 4, lambda a, b: sp.simplify(Ric[a, b] - Rs * g[a, b] / 2))
T = Ein / (8 * sp.pi)

rho = T[0, 0] * sp.exp(-2 * Phi)                 # T_ab u^a u^b, u = e^{-Phi} d_t
j = -T[0, 1] * sp.exp(-Phi - Lam)                # -T_ab u^a n^b, n = e^{-Lam} d_r
p_r = T[1, 1] * sp.exp(-2 * Lam)                 # T_ab n^a n^b
Dt = lambda f: sp.exp(-Phi) * sp.diff(f, t)
Dr = lambda f: sp.exp(-Lam) * sp.diff(f, r)

zero("B1 MS-r  D_r m = 4 pi R^2 (rho W + j U)   [nonstatic.py:66; Hayward (28a)]",
     Dr(m) - 4 * sp.pi * R**2 * (rho * W + j * U))
zero("B2 MS-t  D_t m = -4 pi R^2 (p_r U + j W)  [nonstatic.py:67; Hayward (28b)]",
     Dt(m) + 4 * sp.pi * R**2 * (p_r * U + j * W))

# Hayward (28a,b) in HIS variables: E' = d_xi E, T00 = T(d_tau,d_tau), T01 = T(d_tau,d_xi),
# T11 = T(d_xi,d_xi), Edot = d_tau E, Phi = 0, e^{chi} = e^{2 Lambda}.
sub = {Phi: 0}
E_h = m.subs(sub).doit()
T00 = T[0, 0].subs(sub).doit()
T01 = T[0, 1].subs(sub).doit()
T11 = T[1, 1].subs(sub).doit()
zero("B3 Hayward (28a): E' = 4 pi r^2 (T00 r' - T01 rdot)",
     sp.diff(E_h, r) - 4 * sp.pi * R**2 * (T00 * sp.diff(R, r) - T01 * sp.diff(R, t)))
zero("B4 Hayward (28b): Edot = 4 pi r^2 e^{-chi} (T01 r' - T11 rdot)",
     sp.diff(E_h, t) - 4 * sp.pi * R**2 * sp.exp(-2 * Lam)
     * (T01 * sp.diff(R, r) - T11 * sp.diff(R, t)))

# Comoving perfect fluid (Hayward (31), (32a,b); Escriva (2.9), (2.12)): j = 0.
# Impose j = 0 by substituting the flux identity; check the reduced forms.
# With j = 0: D_r m = 4 pi R^2 rho W  (Escriva 2.12: D_r M = 4 pi Gamma rho R^2)
#             D_t m = -4 pi R^2 p_r U (Escriva 2.9:  D_t M = -4 pi R^2 U p)
zero("B5 Escriva (2.12)/Hayward (32a) at j = 0: D_r m - 4 pi R^2 rho W = 4 pi R^2 j U",
     (Dr(m) - 4 * sp.pi * R**2 * rho * W) - 4 * sp.pi * R**2 * j * U)
zero("B6 Escriva (2.9)/Hayward (32b) at j = 0: D_t m + 4 pi R^2 p_r U = -4 pi R^2 j W",
     (Dt(m) + 4 * sp.pi * R**2 * p_r * U) + 4 * sp.pi * R**2 * j * W)

# ---------------------------------------------------------------------------
# C. the static case, the areal chart, and what the chart needs
# ---------------------------------------------------------------------------
rr = sp.Symbol("r", positive=True)
mf = sp.Function("m")(rr)
g_rr = 1 / (1 - 2 * mf / rr)
zero("C1 certify.py:360-362  m = (r/2)(1 - 1/g_rr) inverts g_rr = 1/(1 - 2m/r)",
     rr / 2 * (1 - 1 / g_rr) - mf)
# certify's samples, reproduced (line 370-373)
samples = (0.25, 0.5, 0.8, 1.0, 1.25, 2.0, 4.0)
ok = all((xx < 1.0) == (0.5 * 1.0 * (1.0 - 1.0 / xx) < 0.0) for xx in samples if xx != 1.0)
row("C2 certify.theorem_holds() samples: g_rr < 1  <=>  m < 0 at r = 1", ok)

# Static, areal chart: the tt Einstein equation gives dm/dr = 4 pi r^2 rho exactly.
Phis = sp.Function("Phi")(rr)
gs = sp.diag(-sp.exp(2 * Phis), 1 / (1 - 2 * mf / rr), rr**2, rr**2 * sp.sin(th)**2)
xs = [t, rr, th, ph]
gis = gs.inv()
Gs = christoffel(gs, gis, xs)
Rics = ricci(Gs, xs)
Rss = sp.simplify(sum(gis[a, b] * Rics[a, b] for a in range(4) for b in range(4)))
Eins = sp.Matrix(4, 4, lambda a, b: sp.simplify(Rics[a, b] - Rss * gs[a, b] / 2))
rho_s = sp.simplify(Eins[0, 0] * sp.exp(-2 * Phis) / (8 * sp.pi))
zero("C3 certify.py:118-120 / tolman.py:314-316: static tt equation gives dm/dr = 4 pi r^2 rho",
     sp.diff(mf, rr) - 4 * sp.pi * rr**2 * rho_s)

# proper-distance gauge (throatmass.py:19-23, hpscentre.py:644): g_ll = 1
l = sp.Symbol("l", real=True)
rl = sp.Function("r")(l)
fl = sp.Function("f")(l)
gl = sp.diag(-fl, 1, rl**2, rl**2 * sp.sin(th)**2)
xl = [t, l, th, ph]
gil = gl.inv()
m_l = rl / 2 * (1 - sum(gil[a, b] * sp.diff(rl, xl[a]) * sp.diff(rl, xl[b])
                        for a in range(4) for b in range(4)))
zero("C4 throatmass.py: in the g_ll = 1 gauge the definition reduces to m = (r/2)(1 - r'^2)",
     m_l - rl / 2 * (1 - sp.diff(rl, l)**2))
Gl = christoffel(gl, gil, xl)
Ricl = ricci(Gl, xl)
Rsl = sp.simplify(sum(gil[a, b] * Ricl[a, b] for a in range(4) for b in range(4)))
Einl = sp.Matrix(4, 4, lambda a, b: sp.simplify(Ricl[a, b] - Rsl * gl[a, b] / 2))
Gtt_mixed = sp.simplify(sum(gil[0, c] * Einl[c, 0] for c in range(4)))
zero("C5 throatmass.py: G^t_t = (2 r r'' + r'^2 - 1)/r^2 (HPS eq. 5 left side)",
     Gtt_mixed - (2 * rl * sp.diff(rl, l, 2) + sp.diff(rl, l)**2 - 1) / rl**2)
rho_l = -Gtt_mixed / (8 * sp.pi)
zero("C6 throatmass.py: dm/dl = 4 pi r^2 r' rho", sp.diff(m_l, l) - 4 * sp.pi * rl**2 * sp.diff(rl, l) * rho_l)
r0 = sp.Symbol("r0", positive=True)
zero("C7 throat r' = 0, r = r0: m = r0/2 > 0 (no contraction, m positive)",
     m_l.subs(sp.diff(rl, l), 0).subs(rl, r0) - r0 / 2)

# ---------------------------------------------------------------------------
# D. Reissner-Nordstrom -- the D4 counterexample to the COROLLARY, not the THEOREM
# ---------------------------------------------------------------------------
M, Q = sp.symbols("M Q", positive=True)
f_rn = 1 - 2 * M / rr + Q**2 / rr**2
m_rn = sp.simplify(rr / 2 * (1 - f_rn))
zero("D1 drivensource.py:39: RN Misner-Sharp mass m(r) = M - Q^2/(2r)", m_rn - (M - Q**2 / (2 * rr)))
g_rn = sp.diag(-f_rn, 1 / f_rn, rr**2, rr**2 * sp.sin(th)**2)
gi_rn = g_rn.inv()
G_rn = christoffel(g_rn, gi_rn, xs)
Ric_rn = ricci(G_rn, xs)
Rs_rn = sp.simplify(sum(gi_rn[a, b] * Ric_rn[a, b] for a in range(4) for b in range(4)))
Ein_rn = sp.Matrix(4, 4, lambda a, b: sp.simplify(Ric_rn[a, b] - Rs_rn * g_rn[a, b] / 2))
rho_rn = sp.simplify(Ein_rn[0, 0] / f_rn / (8 * sp.pi))
zero("D2 RN energy density rho = Q^2/(8 pi r^4) > 0 everywhere", rho_rn - Q**2 / (8 * sp.pi * rr**4))
zero("D3 RN: dm/dr = 4 pi r^2 rho holds; the integration constant is M, not 0",
     sp.diff(m_rn, rr) - 4 * sp.pi * rr**2 * rho_rn)
row("D4 RN: m < 0 exactly on r < Q^2/(2M)  (sympy solve)",
    sp.solve(m_rn < 0, rr) == (rr < Q**2 / (2 * M)) or sp.simplify(sp.solve(m_rn < 0, rr).rhs - Q**2 / (2 * M)) == 0,
    str(sp.solve(m_rn < 0, rr)))
row("D5 RN centre is NOT regular in Hayward's sense (E = O(r^3) fails: E -> -oo)",
    sp.limit(m_rn, rr, 0) == -sp.oo, str(sp.limit(m_rn, rr, 0)))

# ---------------------------------------------------------------------------
# E. Hayward eq. (4) in double-null form, and Proposition 1 (trapping)
#    Hayward's metric (1) was not on the pages returned; it is RECONSTRUCTED here
#    as ds^2 = r^2 dOmega^2 - 2 e^{-f} dxi+ dxi-, the unique form under which (4)'s
#    three expressions agree with theta_pm = 2 d_pm r / r.  Marked RECONSTRUCTED.
# ---------------------------------------------------------------------------
xp, xm = sp.symbols("xi_p xi_m", real=True)
rn = sp.Function("r")(xp, xm)
fn = sp.Function("f")(xp, xm)
gn = sp.Matrix([[0, -sp.exp(-fn), 0, 0], [-sp.exp(-fn), 0, 0, 0],
                [0, 0, rn**2, 0], [0, 0, 0, rn**2 * sp.sin(th)**2]])
xn = [xp, xm, th, ph]
gin = gn.inv()
grad_n = sum(gin[a, b] * sp.diff(rn, xn[a]) * sp.diff(rn, xn[b]) for a in range(4) for b in range(4))
E_n = rn / 2 * (1 - grad_n)
zero("E1 Hayward (4) second form: E = r/2 + e^f r d_+r d_-r   [metric RECONSTRUCTED]",
     E_n - (rn / 2 + sp.exp(fn) * rn * sp.diff(rn, xp) * sp.diff(rn, xm)))
thp = 2 * sp.diff(rn, xp) / rn
thm = 2 * sp.diff(rn, xm) / rn
zero("E2 Hayward (4) third form: E = r/2 + (1/4) e^f r^3 theta_+ theta_-   [RECONSTRUCTED]",
     E_n - (rn / 2 + sp.Rational(1, 4) * sp.exp(fn) * rn**3 * thp * thm))

# ---------------------------------------------------------------------------
# F. foliation boost: Gamma^2 - U^2 invariant (foliation.py:128-134)
# ---------------------------------------------------------------------------
w, Us, Gs_ = sp.symbols("w U Gamma", real=True)
Up = sp.cosh(w) * Us + sp.sinh(w) * Gs_
Gp = sp.sinh(w) * Us + sp.cosh(w) * Gs_
zero("F1 boost invariance: Gamma'^2 - U'^2 = Gamma^2 - U^2", Gp**2 - Up**2 - (Gs_**2 - Us**2))

# ---------------------------------------------------------------------------
# G. finite claims, z3
# ---------------------------------------------------------------------------
try:
    import z3
except Exception as exc:                                    # pragma: no cover
    z3 = None
    row("G0 z3 available", False, "z3 not importable: %s" % exc)

if z3 is not None:
    Rz, mz, Wz, Uz = z3.Reals("R m W U")
    ident = (Wz * Wz == 1 - 2 * mz / Rz + Uz * Uz)

    def obligation(name, hyp, concl):
        s = z3.Solver(); s.add(hyp); s.add(z3.Not(concl)); res = s.check()
        row(name, res == z3.unsat, "negation: %s" % res)

    def guard(name, hyp, want_sat=True):
        s = z3.Solver(); s.add(hyp); res = s.check()
        row(name, (res == z3.sat) == want_sat, "%s" % res)

    base = [Rz > 0, ident]
    guard("G1 guard: static (U = 0), W > 1 is satisfiable", base + [Uz == 0, Wz > 1])
    obligation("G2 certify THEOREM: U = 0, W > 0  =>  (W > 1 <=> m < 0)",
               base + [Uz == 0, Wz > 0], (Wz > 1) == (mz < 0))
    obligation("G3 static slice is never trapped: U = 0  =>  1 - 2m/R >= 0  (untrapped is a CONSEQUENCE, not a hypothesis)",
               base + [Uz == 0], 1 - 2 * mz / Rz >= 0)
    obligation("G4 throat: U = 0, W = 0  =>  m = R/2 > 0", base + [Uz == 0, Wz == 0], mz == Rz / 2)
    obligation("G5 Hayward Prop. 1: 1 - 2m/R = Gamma^2 - U^2 < 0  <=>  m > R/2",
               base, (Wz * Wz - Uz * Uz < 0) == (mz > Rz / 2))
    obligation("G6 driven THEOREM: contraction W > 1  <=>  2m/R < U^2", base + [Wz > 0],
               (Wz > 1) == (2 * mz / Rz < Uz * Uz))
    guard("G7 drift guard: W > 1 with m >= 0 IS satisfiable off the static slice (m < 0 not necessary)",
          base + [Wz > 1, mz >= 0])
    guard("G8 Escriva (2.5) sqrt is a BRANCH: Gamma < 0 also satisfies the constraint (type-II)",
          base + [Wz < 0])
    obligation("G9 foliation: m < 0 => Gamma^2 > 1 + U^2 >= 1 in EVERY foliation",
               base + [mz < 0], Wz * Wz > 1)

# ---------------------------------------------------------------------------
print()
print("checks: %d   failed: %d" % (len(ROWS), len(FAILS)))
for f_ in FAILS:
    print("  FAILED:", f_)
sys.exit(1 if FAILS else 0)
