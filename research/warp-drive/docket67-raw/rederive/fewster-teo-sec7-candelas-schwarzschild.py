#!/usr/bin/env python3
r"""
DOCKET 67, audit 22/36: fewster-teo-sec7-candelas-schwarzschild.

What the tree uses (research/warp-drive/fewsterteo.py:56-60,170,622): F&T gr-qc/9812032
Sec. 7's Schwarzschild bound (7.10) rests on Candelas' outgoing/ingoing ("up"/"in") mode
sums, a basis defined by horizon boundary conditions, so (7.10) is NOT continued to M < 0.

The source text of Sec. 7 is NOT re-read in this stage (alphaXiv quota exhausted; arxiv.org
403 at the egress proxy).  What IS checkable here is the geometry/operator claim underneath
the refusal, for the massless minimally coupled scalar on -F dt^2 + dr^2/F + r^2 dOmega^2,
F = 1 - 2M/r, in the KG Hilbert space L^2(dr*) of psi = r R (the KG norm of a static mode is
INT F^{-1} r^2 |R|^2 dr = INT |psi|^2 dr*, checked below), radial operator
    -psi'' + V psi = w^2 psi,   V = F ( l(l+1)/r^2 + 2M/r^3 ),   ' = d/dr*.

CHECKS (each can fail; controls included):
 C1  M > 0: F vanishes at r = 2M (horizon); r* -> -oo there.  Domain r* in (-oo, oo):
     TWO asymptotic ends, V -> 0 at both (limit point at both, Weyl): the continuum at each
     w > 0 is 2-fold per (l,m) -- the "in"/"up" (ingoing/outgoing) families exist.
 C2  M < 0: F > 0 on r > 0 (no horizon); r* -> FINITE value at r = 0.  Domain r* in (x0, oo):
     ONE asymptotic end.  The continuum is at most 1-fold per (l,m): there is no second family.
 C3  M < 0, near r = 0: x^2 V -> -1/4 for EVERY l (x = r* - x0).  Indicial s(s-1) = -1/4,
     double root s = 1/2: solutions ~ sqrt(x), sqrt(x) ln x, BOTH in L^2 near x = 0, so the
     endpoint is LIMIT CIRCLE (limit point iff the coefficient >= 3/4): the radial operator is
     NOT essentially self-adjoint; a boundary condition at the singularity must be chosen
     (a one-parameter family).  That is a hypothesis Sec. 7 (M > 0) never needs.
     CONTROL: the same test on the M > 0 horizon end returns x^2 V -> 0 with V -> 0
     exponentially in r*, i.e. limit point, no choice.
 C4  F&T's internal (7.8)/(7.10) consistency the Docket 62 read relied on:
     (9/64)(16/9) = 1/4 exactly.
"""
import sympy as sp

r, m, x, w = sp.symbols('r m x omega', positive=True)
l = sp.symbols('l', integer=True, nonnegative=True)
ok = []
def chk(name, cond):
    ok.append(bool(cond)); print(("PASS " if cond else "FAIL ") + name)

# KG norm reduces to L^2(dr*)
M = sp.symbols('M', real=True, nonzero=True)
F = 1 - 2*M/r
R = sp.Function('R')(r)
psi = r*R
chk("KG static norm density F^-1 r^2 |R|^2 dr == |psi|^2 dr* (dr* = dr/F)",
    sp.simplify(r**2*R**2/F - psi**2*(1/F)) == 0)

# radial potential from the field equation, derived (not assumed)
t = sp.symbols('t'); rs = sp.symbols('rs')
# box phi for phi = e^{-iwt} R(r) Y_l: (1/r^2) d_r(r^2 F d_r R) + (w^2/F - l(l+1)/r^2) R = 0
Rf = sp.Function('R')
eqR = sp.diff(r**2*F*sp.diff(Rf(r), r), r)/r**2 + (w**2/F - l*(l+1)/r**2)*Rf(r)
# substitute R = psi/r, d/dr = (1/F) d/dr*: expect  F^{-1}[ psi_{**} + (w^2 - V) psi ] / r
Psi = sp.Function('Psi')
p = Psi(r)
expr = eqR.subs(Rf(r), p/r).doit()
# psi_** = F d/dr (F dpsi/dr)
psi_ss = F*sp.diff(F*sp.diff(p, r), r)
V = F*(l*(l+1)/r**2 + 2*M/r**3)
target = (psi_ss + (w**2 - V)*p)/(F*r)
chk("radial eq reduces to -psi'' + V psi = w^2 psi with V = F(l(l+1)/r^2 + 2M/r^3)",
    sp.simplify(sp.expand(expr - target)) == 0)

# C1: M = +m > 0
Fp = 1 - 2*m/r
chk("C1 M>0: F(2M) = 0 (horizon)", sp.simplify(Fp.subs(r, 2*m)) == 0)
rstar_p = r + 2*m*sp.log(r/(2*m) - 1)
chk("C1 M>0: d r*/dr = 1/F", sp.simplify(sp.diff(rstar_p, r) - 1/Fp) == 0)
chk("C1 M>0: r* -> -oo at r -> 2M+", sp.limit(rstar_p, r, 2*m, '+') == -sp.oo)
chk("C1 M>0: r* -> +oo at r -> oo", sp.limit(rstar_p, r, sp.oo) == sp.oo)
Vp = Fp*(l*(l+1)/r**2 + 2*m/r**3)
chk("C1 M>0: V -> 0 at horizon", sp.limit(Vp.subs(l, 3), r, 2*m, '+') == 0)
chk("C1 M>0: V -> 0 at infinity", sp.limit(Vp.subs(l, 3), r, sp.oo) == 0)
# V ~ F ~ e^{r*/2M} near horizon: F*exp(-r*/(2m)) -> finite nonzero
lim = sp.limit(sp.simplify(Fp*sp.exp(-rstar_p/(2*m))), r, 2*m, '+')
chk("C1 M>0: F ~ C e^{r*/2M} as r*->-oo (exponential decay => limit point, 2 ends)",
    lim.is_finite and lim != 0)
# control for C3's test: x^2 V at the horizon end with x = r* -> -oo
chk("C3-control M>0: (r*)^2 V -> 0 at the horizon end (no inverse-square core)",
    sp.limit((rstar_p**2*Vp).subs(l, 2), r, 2*m, '+') == 0)

# C2: M = -m < 0
Fn = 1 + 2*m/r
chk("C2 M<0: F > 0 for all r > 0 (no horizon)",
    sp.solve(sp.Eq(Fn, 0), r) == [] and sp.ask(sp.Q.positive(Fn), sp.Q.positive(r) & sp.Q.positive(m)))
rstar_n = r - 2*m*sp.log(1 + r/(2*m))
chk("C2 M<0: d r*/dr = 1/F", sp.simplify(sp.diff(rstar_n, r) - 1/Fn) == 0)
x0 = sp.limit(rstar_n, r, 0, '+')
chk("C2 M<0: r* -> finite x0 = %s at r -> 0+ (one asymptotic end only)" % x0, x0.is_finite)
# near r=0: x = r* - x0 ~ r^2/(4m)
ser = sp.series(rstar_n - x0, r, 0, 4).removeO()
chk("C2 M<0: x = r^2/(4m) - r^3/(12 m^2) + ...",
    sp.simplify(ser - (r**2/(4*m) - r**3/(12*m**2))) == 0)

# C3: x^2 V -> -1/4 for every l
Vn = Fn*(l*(l+1)/r**2 - 2*m/r**3)
c = sp.limit(sp.simplify(((rstar_n - x0)**2*Vn)), r, 0, '+')
chk("C3 M<0: x^2 V -> -1/4, independent of l (got %s)" % c, sp.simplify(c + sp.Rational(1, 4)) == 0)
s = sp.symbols('s')
roots = sp.roots(s*(s - 1) + sp.Rational(1, 4), s)
chk("C3 indicial s(s-1) = -1/4 has double root 1/2", roots == {sp.Rational(1, 2): 2})
# both local solutions of -psi'' - psi/(4x^2) = 0 and their L^2 behaviour
for sol in (sp.sqrt(x), sp.sqrt(x)*sp.log(x)):
    res = sp.simplify(-sp.diff(sol, x, 2) - sol/(4*x**2))
    nrm = sp.integrate(sol**2, (x, 0, sp.Rational(1, 2)))
    chk("C3 %s solves the core eq and is L^2 near 0 (INT_0^1/2 = %s)" % (sol, sp.nsimplify(nrm)),
        res == 0 and nrm.is_finite)
chk("C3 limit-circle criterion: coefficient -1/4 < 3/4 (Weyl limit point needs >= 3/4)",
    sp.Rational(-1, 4) < sp.Rational(3, 4))
# control: the criterion CAN return limit point -- at coefficient 3/4, s = 3/2, -1/2; x^{-1/2} not L^2
r2 = sp.roots(s*(s - 1) - sp.Rational(3, 4), s)
chk("C3-control: at coefficient 3/4 roots are %s and x^{-1/2} is NOT L^2 near 0" % r2,
    set(r2) == {sp.Rational(3, 2), sp.Rational(-1, 2)} and
    sp.integrate(x**-1, (x, 0, 1)) == sp.oo)

# C3 robustness: the remainder q - q0 (q0 = -1/(4x^2)) is O(x^{-3/2}) at worst, so
# INT_0 x |q - q0| dx < oo and both solutions keep their sqrt(x), sqrt(x) ln x asymptotics
# (standard perturbation of the Euler core) -- limit circle survives the full potential.
X = rstar_n - x0
for L in (0, 1, 2, 5):
    rem = sp.limit(sp.simplify(X**sp.Rational(3, 2)*(Vn.subs(l, L) + 1/(4*X**2))), r, 0, '+')
    chk("C3 robustness l=%d: x^(3/2) (V + 1/(4x^2)) -> finite (%s)" % (L, sp.simplify(rem)), rem.is_finite)

# C4
chk("C4 (9/64)(16/9) == 1/4", sp.Rational(9, 64)*sp.Rational(16, 9) == sp.Rational(1, 4))

print("\n%d/%d checks pass" % (sum(ok), len(ok)))
raise SystemExit(0 if all(ok) else 1)
