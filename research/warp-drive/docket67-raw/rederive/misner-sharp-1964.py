#!/usr/bin/env python3
"""DOCKET 67 -- re-derivation for key misner-sharp-1964.

The Misner-Sharp identity  Gamma^2 - U^2 = g^ab d_aR d_bR = 1 - 2m/R  is a DEFINITION of m
plus algebra, so everything below is closed-form.  Checks:

 C1  general diagonal metric -e^{2Phi}dt^2 + e^{2Lambda}dr^2 + R^2 dOmega^2:
     g^ab d_aR d_bR == e^{-2Lambda}R'^2 - e^{-2Phi}Rdot^2 == Gamma^2 - U^2   (tree's V1)
 C1b same with a SHIFT (non-diagonal 2-metric): the scalar is still (n.dR)^2 - (u.dR)^2
 C2  Hayward gr-qc/9408002 eq.(26)/(27): ds^2 = -dtau^2 + e^{lambda}dzeta^2 + r^2 dOmega^2
     gives 1 - 2E/r = e^{-lambda} r'^2 - rdot^2, i.e. the tree's form at Phi = 0, lambda = 2 Lambda
 C3  Hayward eq.(4) double-null form: E = r/2 + e^f r d+r d-r = r/2 + (1/4) e^f r^3 th+ th-
 C4  boost invariance of Gamma^2 - U^2 (foliation.py V4)
 C5  Schwarzschild in three charts (Schwarzschild, Lemaitre synchronous = Hayward's gauge,
     Painleve-Gullstrand with shift): E = M in all three
 C6  Minkowski hyperboloidal slicing: m = 0 while Gamma = cosh(chi) > 1 (static hypothesis
     load-bearing for 'contraction <=> m < 0')
 C7  Hayward eq.(28a),(28b) re-derived from the Einstein tensor in his gauge (G = 8 pi T)
 C8  z3: with the identity, R > 0, Gamma > 0:  Gamma > 1 <=> U^2 > 2m/R ; at U = 0, Gamma > 1 <=> m < 0
     and a witness that m < 0 is NOT necessary when U != 0
 C9  Escriva 2504.05813 eq.(2.24) M = (R/2)(1 + U^2 - Gamma^2) equals the tree's V2
 C10 exchange rate c^2/(G*LAMBDA) with CODATA 2018 vs 2022 G (identical values)
"""
import sympy as sp

res = []


def chk(name, expr):
    v = sp.simplify(expr)
    res.append((name, v == 0, v))


def inv_metric_grad2(g, x, f):
    gi = g.inv()
    n = len(x)
    return sum(gi[a, b] * sp.diff(f, x[a]) * sp.diff(f, x[b]) for a in range(n) for b in range(n))


t, r, th, ph = sp.symbols('t r theta phi', real=True)
X = [t, r, th, ph]
Phi, Lam, R = (sp.Function(n)(t, r) for n in ('Phi', 'Lambda', 'R'))

# C1
g = sp.diag(-sp.exp(2 * Phi), sp.exp(2 * Lam), R ** 2, R ** 2 * sp.sin(th) ** 2)
grad2 = inv_metric_grad2(g, X, R)
U = sp.exp(-Phi) * sp.diff(R, t)
Gam = sp.exp(-Lam) * sp.diff(R, r)
chk("C1  g^ab dR dR - (Gamma^2 - U^2), diagonal general metric", grad2 - (Gam ** 2 - U ** 2))

# C1b with shift beta: ds^2 = -N^2 dt^2 + A^2 (dr + beta dt)^2 + R^2 dOmega^2
N, A, be = (sp.Function(n)(t, r) for n in ('N', 'A', 'beta'))
gs = sp.zeros(4)
gs[0, 0] = -N ** 2 + A ** 2 * be ** 2
gs[0, 1] = gs[1, 0] = A ** 2 * be
gs[1, 1] = A ** 2
gs[2, 2] = R ** 2
gs[3, 3] = R ** 2 * sp.sin(th) ** 2
# unit normal u^a = (1/N, -beta/N), radial unit n^a = (0, 1/A)
u_dR = (sp.diff(R, t) - be * sp.diff(R, r)) / N
n_dR = sp.diff(R, r) / A
chk("C1b with shift: g^ab dR dR - ((n.dR)^2 - (u.dR)^2)", inv_metric_grad2(gs, X, R) - (n_dR ** 2 - u_dR ** 2))

# C2 Hayward (26)/(27)
tau, zeta = sp.symbols('tau zeta', real=True)
lam = sp.Function('lambda')(tau, zeta)
rr = sp.Function('r')(tau, zeta)
gH = sp.diag(-1, sp.exp(lam), rr ** 2, rr ** 2 * sp.sin(th) ** 2)
XH = [tau, zeta, th, ph]
E_def = rr / 2 * (1 - inv_metric_grad2(gH, XH, rr))          # Hayward eq.(4)
chk("C2  Hayward (27): 1-2E/r - (e^-lambda r'^2 - rdot^2)",
    (1 - 2 * E_def / rr) - (sp.exp(-lam) * sp.diff(rr, zeta) ** 2 - sp.diff(rr, tau) ** 2))
# tree form at Phi=0, lambda = 2 Lambda
tree_form = (sp.exp(-2 * Lam) * sp.diff(R, r) ** 2 - sp.exp(-2 * Phi) * sp.diff(R, t) ** 2)
chk("C2b tree form at Phi=0, lambda=2Lambda == Hayward form",
    tree_form.subs(Phi, 0).doit() - (sp.exp(-lam) * sp.diff(rr, zeta) ** 2 - sp.diff(rr, tau) ** 2)
    .subs({lam: 2 * Lam.subs({t: tau, r: zeta}), rr: R.subs({t: tau, r: zeta})}).subs({tau: t, zeta: r}).doit())
# driven.py:58 prints e^{-chi}; there is no chi in eq.(26)-(27): transcription discrepancy only.

# C3 double null ds^2 = r^2 dOmega^2 - 2 e^{-f} dxi+ dxi-
xp, xm = sp.symbols('xi_p xi_m', real=True)
f = sp.Function('f')(xp, xm)
rn = sp.Function('r')(xp, xm)
gN = sp.zeros(4)
gN[0, 1] = gN[1, 0] = -sp.exp(-f)
gN[2, 2] = rn ** 2
gN[3, 3] = rn ** 2 * sp.sin(th) ** 2
XN = [xp, xm, th, ph]
EN = rn / 2 * (1 - inv_metric_grad2(gN, XN, rn))
thp, thm = 2 * sp.diff(rn, xp) / rn, 2 * sp.diff(rn, xm) / rn
chk("C3a Hayward (4): E - (r/2 + e^f r d+r d-r)", EN - (rn / 2 + sp.exp(f) * rn * sp.diff(rn, xp) * sp.diff(rn, xm)))
chk("C3b Hayward (4): E - (r/2 + e^f r^3 th+ th-/4)", EN - (rn / 2 + sp.exp(f) * rn ** 3 * thp * thm / 4))

# C4 boost invariance
w, Us, Gs = sp.symbols('w U Gamma', real=True)
Up = sp.cosh(w) * Us + sp.sinh(w) * Gs
Gp = sp.sinh(w) * Us + sp.cosh(w) * Gs
chk("C4  boost: Gamma'^2 - U'^2 - (Gamma^2 - U^2)", Gp ** 2 - Up ** 2 - (Gs ** 2 - Us ** 2))

# C5 Schwarzschild, three charts
M = sp.Symbol('M', positive=True)
rs_ = sp.Symbol('r', positive=True)
gS = sp.diag(-(1 - 2 * M / rs_), 1 / (1 - 2 * M / rs_), rs_ ** 2, rs_ ** 2 * sp.sin(th) ** 2)
ES = rs_ / 2 * (1 - inv_metric_grad2(gS, [t, rs_, th, ph], rs_))
chk("C5a Schwarzschild chart: E - M", ES - M)
# Lemaitre (synchronous, diagonal, lapse 1 = Hayward's (26) gauge):
rho_ = sp.Symbol('rho', real=True)
rL = (sp.Rational(3, 2) * (rho_ - tau)) ** sp.Rational(2, 3) * (2 * M) ** sp.Rational(1, 3)
gL = sp.diag(-1, 2 * M / rL, rL ** 2, rL ** 2 * sp.sin(th) ** 2)
EL = rL / 2 * (1 - inv_metric_grad2(gL, [tau, rho_, th, ph], rL))
chk("C5b Lemaitre (Hayward gauge, lambda = ln(2M/r)): E - M", sp.simplify(EL - M))
# Painleve-Gullstrand (shift): ds^2 = -dT^2 + (dr + sqrt(2M/r) dT)^2 + r^2 dOmega^2
T = sp.Symbol('T', real=True)
gP = sp.zeros(4)
v = sp.sqrt(2 * M / rs_)
gP[0, 0] = -1 + v ** 2
gP[0, 1] = gP[1, 0] = v
gP[1, 1] = 1
gP[2, 2] = rs_ ** 2
gP[3, 3] = rs_ ** 2 * sp.sin(th) ** 2
EP = rs_ / 2 * (1 - inv_metric_grad2(gP, [T, rs_, th, ph], rs_))
chk("C5c Painleve-Gullstrand (shift): E - M", EP - M)
# PG frame values: U = -sqrt(2M/r), Gamma = 1 -> Gamma^2 - U^2 = 1 - 2M/r: Gamma = 1, not > 1, m > 0
chk("C5d PG frame: Gamma=1, U=-sqrt(2M/r): Gamma^2-U^2-(1-2M/r)", 1 - v ** 2 - (1 - 2 * M / rs_))

# C6 Minkowski hyperboloidal
chi = sp.Symbol('chi', positive=True)
tp = sp.Symbol('tau', positive=True)
gM = sp.diag(-1, tp ** 2, (tp * sp.sinh(chi)) ** 2, (tp * sp.sinh(chi) * sp.sin(th)) ** 2)
RM = tp * sp.sinh(chi)
Em = RM / 2 * (1 - inv_metric_grad2(gM, [tp, chi, th, ph], RM))
GamM = sp.diff(RM, chi) / tp
UM = sp.diff(RM, tp)
chk("C6a Minkowski hyperboloidal: m = 0", Em)
chk("C6b Gamma = cosh(chi)", GamM - sp.cosh(chi))
chk("C6c Gamma^2 - U^2 = 1", GamM ** 2 - UM ** 2 - 1)


# C7 Hayward (28a),(28b) from G_ab in his gauge
def einstein(g, x):
    n = len(x)
    gi = g.inv()
    Gm = [[[sum(gi[a, d] * (sp.diff(g[d, b], x[c]) + sp.diff(g[d, c], x[b]) - sp.diff(g[b, c], x[d]))
                for d in range(n)) / 2 for c in range(n)] for b in range(n)] for a in range(n)]
    Ric = sp.zeros(n)
    for b in range(n):
        for c in range(n):
            e = 0
            for a in range(n):
                e += sp.diff(Gm[a][b][c], x[a]) - sp.diff(Gm[a][b][a], x[c])
                for d in range(n):
                    e += Gm[a][a][d] * Gm[d][b][c] - Gm[a][c][d] * Gm[d][b][a]
            Ric[b, c] = sp.simplify(e)
    Rs = sp.simplify(sum(gi[i, j] * Ric[i, j] for i in range(n) for j in range(n)))
    return (Ric - Rs * g / 2).applyfunc(sp.simplify)


GH = einstein(gH, XH)
Tl = GH / (8 * sp.pi)                         # covariant T_ab, coordinate basis
T00, T01, T11 = Tl[0, 0], Tl[0, 1], Tl[1, 1]
rp, rd = sp.diff(rr, zeta), sp.diff(rr, tau)
chk("C7a Hayward (28a): E' - 4 pi r^2 (T00 r' - T01 rdot)", sp.diff(E_def, zeta) - 4 * sp.pi * rr ** 2 * (T00 * rp - T01 * rd))
chk("C7b Hayward (28b): Edot - 4 pi r^2 e^-lambda (T01 r' - T11 rdot)",
    sp.diff(E_def, tau) - 4 * sp.pi * rr ** 2 * sp.exp(-lam) * (T01 * rp - T11 * rd))

# C9 Escriva (2.24) vs tree V2
mS = sp.Symbol('m')
chk("C9  Escriva (2.24) M=(R/2)(1+U^2-Gamma^2) solves Gamma^2 = 1+U^2-2M/R",
    (Gs ** 2 - (1 + Us ** 2 - 2 * (sp.Symbol('R') / 2 * (1 + Us ** 2 - Gs ** 2)) / sp.Symbol('R'))))

# C8 z3
try:
    import z3
    Gz, Uz, mz, Rz = z3.Reals('G U m R')
    ident = Gz * Gz == 1 + Uz * Uz - 2 * mz / Rz
    s = z3.Solver()
    s.add(ident, Rz > 0, Gz > 0, z3.Not((Gz > 1) == (Uz * Uz * Rz > 2 * mz)))
    c8a = s.check()
    s = z3.Solver()
    s.add(ident, Rz > 0, Gz > 0, Uz == 0, z3.Not((Gz > 1) == (mz < 0)))
    c8b = s.check()
    s = z3.Solver()
    s.add(ident, Rz > 0, Gz > 1, mz > 0)
    c8c = s.check()
    wit = s.model() if c8c == z3.sat else None
    res.append(("C8a z3: Gamma>1 <=> U^2 > 2m/R (unsat = proved)", str(c8a) == 'unsat', c8a))
    res.append(("C8b z3: U=0 => (Gamma>1 <=> m<0) (unsat = proved)", str(c8b) == 'unsat', c8b))
    res.append(("C8c z3: Gamma>1 with m>0 SATISFIABLE when U!=0 (sat expected)", str(c8c) == 'sat', wit))
except ImportError:
    res.append(("C8 z3 not installed", False, None))

# C11 vacuity guards: mutated statements must NOT reduce to 0
mut1 = sp.simplify(grad2 - (Gam ** 2 + U ** 2))
res.append(("C11a guard: Gamma^2 + U^2 (sign-flipped) is NOT the invariant", mut1 != 0, mut1))
mut2 = sp.simplify((1 - 2 * E_def / rr) - (sp.exp(-zeta) * sp.diff(rr, zeta) ** 2 - sp.diff(rr, tau) ** 2))
res.append(("C11b guard: driven.py:58's e^{-chi}, read with chi = the coordinate, is NOT eq.(27)", mut2 != 0, mut2))
mut3 = sp.simplify(EL - 2 * M)
res.append(("C11c guard: Lemaitre E != 2M", mut3 != 0, mut3))

# C10 exchange rate
c = 299792458.0
G18 = 6.67430e-11
G22 = 6.67430e-11   # CODATA 2022 (arXiv 2409.03787 Table XXXII): identical to 2018
LAMBDA = 9.982529174194637
x18, x22 = c ** 2 / (G18 * LAMBDA), c ** 2 / (G22 * LAMBDA)
res.append(("C10 c^2/(G LAMBDA) CODATA2018 = %.6e, CODATA2022 = %.6e, tree quotes 1.348948e26" % (x18, x22),
            abs(x18 - 1.348948e26) / 1.348948e26 < 1e-6 and x18 == x22, x18))

ok = True
for n_, passed, val in res:
    ok &= bool(passed)
    print(("PASS " if passed else "FAIL ") + n_ + ("" if passed else "   -> %s" % (val,)))
print("ALL PASS" if ok else "SOME FAIL")
raise SystemExit(0 if ok else 1)
