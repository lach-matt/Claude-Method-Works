#!/usr/bin/env python3
"""DOCKET 67 re-derivation: Herrera arXiv:1801.08358v2 eq. (10)
    nu' = 2 (m + 4 pi P_r r^3) / (r (r - 2m))
computed from scratch (Christoffels -> Ricci -> Einstein) in the SOURCE's own
conventions (signature +,-,-,-; metric (1); G^mu_nu = 8 pi T^mu_nu, eq. (2);
T^0_0 = mu, T^1_1 = -P_r, T^2_2 = T^3_3 = -P_perp, eqs (3)-(5); G = c = 1),
then in the TREE's conventions (tolman.py: signature -,+,+,+, e^{2 Phi} = e^nu,
T^r_r = +p_r).  Hypothesis probes: Lambda != 0, r = 2m, matter model.
Numeric witness: Schwarzschild constant-density interior.  z3: I7/I8 re-encoded
independently, with and without the tree's added r - 2m > 0.
Exit 0 iff every check is as expected."""
import sys
import sympy as sp

bad = 0
def chk(label, expr, want=0):
    global bad
    got = sp.simplify(expr)
    ok = (got == want) if not isinstance(want, bool) else (bool(got) == want)
    bad += (not ok)
    print("  %-72s %s %s" % (label, got, "ok" if ok else "FAIL"))

t, r, th, ph = sp.symbols("t r theta phi")
X = [t, r, th, ph]
nu = sp.Function("nu")(r); lam = sp.Function("lambda")(r)
m = sp.Function("m")(r)
mu, Pr, Pp, Lc = sp.symbols("mu P_r P_perp Lambda_c")

def einstein_mixed(g, Lambda=0):
    gi = g.inv()
    G = [[[sp.simplify(sum(gi[a, d] * (sp.diff(g[d, b], X[c]) + sp.diff(g[d, c], X[b])
                                     - sp.diff(g[b, c], X[d])) for d in range(4)) / 2)
           for c in range(4)] for b in range(4)] for a in range(4)]
    Ric = sp.zeros(4)
    for b in range(4):
        for c in range(4):
            e = 0
            for a in range(4):
                e += sp.diff(G[a][b][c], X[a]) - sp.diff(G[a][b][a], X[c])
                for d in range(4):
                    e += G[a][a][d] * G[d][b][c] - G[a][c][d] * G[d][b][a]
            Ric[b, c] = sp.simplify(e)
    Rs = sp.simplify(sum(gi[i, j] * Ric[i, j] for i in range(4) for j in range(4)))
    Emix = sp.simplify(gi * (Ric - Rs * g / 2 + Lambda * g))
    return Emix, G

def riemann_up(G, a, b, c, d):   # R^a_{bcd}
    e = sp.diff(G[a][b][d], X[c]) - sp.diff(G[a][b][c], X[d])
    for k in range(4):
        e += G[a][c][k] * G[k][b][d] - G[a][d][k] * G[k][b][c]
    return sp.simplify(e)

print("A. SOURCE CONVENTIONS (Herrera metric (1), signature +,-,-,-)")
g = sp.diag(sp.exp(nu), -sp.exp(lam), -r**2, -r**2 * sp.sin(th)**2)
E, Gam = einstein_mixed(g)
# eq (12): R^3_{232} = 1 - e^{-lambda} = 2m/r   (text layer garbled; reading checked)
chk("eq(12) R^3_232 - (1 - e^{-lambda})", riemann_up(Gam, 3, 2, 3, 2) - (1 - sp.exp(-lam)))
# eqs (6),(7),(8) as printed, from G^mu_nu = 8 pi T^mu_nu
chk("eq(6)  8 pi mu = G^0_0 as printed",
    E[0, 0] - (-(-1/r**2 + sp.exp(-lam) * (1/r**2 - sp.diff(lam, r)/r))))
chk("eq(7)  -8 pi P_r = G^1_1 as printed",
    -E[1, 1] - (-(1/r**2 - sp.exp(-lam) * (1/r**2 + sp.diff(nu, r)/r))))
nup, lamp = sp.diff(nu, r), sp.diff(lam, r)
chk("eq(8)  -8 pi P_perp = G^2_2 as printed",
    -E[2, 2] - sp.exp(-lam)/4 * (2*sp.diff(nu, r, 2) + nup**2 - lamp*nup + 2*(nup - lamp)/r))
# eq (10): impose e^{-lambda} = 1 - 2m/r and G^1_1 = -8 pi P_r, solve for nu'
lam_m = -sp.log(1 - 2*m/r)
G11 = sp.simplify(E[1, 1].subs(lam, lam_m).doit())
nup_sol = sp.solve(sp.Eq(G11, -8*sp.pi*Pr), sp.Derivative(nu, r))[0]
eq10 = 2*(m + 4*sp.pi*Pr*r**3) / (r*(r - 2*m))
chk("eq(10) nu' from computed G^1_1  minus  2(m+4 pi P_r r^3)/(r(r-2m))", nup_sol - eq10)
# eq (10) needs NOTHING but G^1_1: mu, P_perp, and m' never enter
chk("eq(10) is free of mu, P_perp, m'  (free symbols of nu' solution)",
    sp.Symbol("x") if (nup_sol.has(mu) or nup_sol.has(Pp) or nup_sol.has(sp.Derivative(m, r)))
    else 0)
# eq (13) consistency: G^0_0 with lambda(m) gives m' = 4 pi r^2 mu
G00 = sp.simplify(E[0, 0].subs(lam, lam_m).doit())
mp_sol = sp.solve(sp.Eq(G00, 8*sp.pi*mu), sp.Derivative(m, r))[0]
chk("eq(13) m' = 4 pi r^2 mu from computed G^0_0", mp_sol - 4*sp.pi*r**2*mu)
# eq (9): conservation T^mu_{1;mu} = 0 for T = diag(mu,-P_r,-P_perp,-P_perp)
Prf = sp.Function("P_r")(r); muf = sp.Function("mu")(r); Ppf = sp.Function("P_perp")(r)
T = sp.diag(muf, -Prf, -Ppf, -Ppf)   # T^mu_nu
div1 = sum(sp.diff(T[a, 1], X[a]) for a in range(4)) \
    + sum(Gam[a][a][k]*T[k, 1] for a in range(4) for k in range(4)) \
    - sum(Gam[k][a][1]*T[a, k] for a in range(4) for k in range(4))
tov9 = sp.diff(Prf, r) + nup/2*(muf + Prf) - 2*(Ppf - Prf)/r
chk("eq(9)  -T^mu_{1;mu} minus [P_r' + nu'/2 (mu+P_r) - 2(P_perp-P_r)/r]",
    sp.simplify(-div1 - tov9))
# eq (11) = eq (9) with eq (10) substituted
chk("eq(11) = eq(9) with eq(10)",
    (-(eq10/2)*(mu+Pr) + 2*(Pp-Pr)/r) - (-(m+4*sp.pi*Pr*r**3)/(r*(r-2*m))*(mu+Pr) + 2*(Pp-Pr)/r))
# eqs (32),(33): e^{(nu-lam)/2} nu' r^2/2 = e^{(nu+lam)/2}(m + 4 pi r^3 P_r) given eq (10)
chk("eq(33)->(32) via eq(10)",
    sp.simplify((sp.exp(-lam_m/2)*eq10*r**2/2 - sp.exp(lam_m/2)*(m + 4*sp.pi*r**3*Pr))
                .subs(m, sp.Symbol("mm", positive=True)).subs(r, sp.Symbol("rr", positive=True))
                .subs(sp.Symbol("mm", positive=True), sp.Rational(1, 7)*sp.Symbol("rr", positive=True))))

print("B. TREE CONVENTIONS (tolman.py: -,+,+,+; e^{2Phi}=e^nu; T^r_r = +p_r)")
Phi = sp.Function("Phi")(r)
gt = sp.diag(-sp.exp(2*Phi), 1/(1 - 2*m/r), r**2, r**2*sp.sin(th)**2)
Et, _ = einstein_mixed(gt)
php = sp.solve(sp.Eq(Et[1, 1], 8*sp.pi*Pr), sp.Derivative(Phi, r))[0]
chk("tree Phi' (V9)  minus (m+4 pi r^3 p_r)/(r(r-2m))",
    php - (m + 4*sp.pi*r**3*Pr)/(r*(r - 2*m)))
chk("tree Phi' = nu'/2 of Herrera eq (10)", php - eq10/2)

print("C. HYPOTHESIS PROBES")
# Lambda.  Source eq (2) is G^mu_nu = 8 pi T^mu_nu with NO Lambda.  Probe in the
# tree's signature (-,+,+,+) with MTW's G_ab + Lambda g_ab = 8 pi T_ab (Lambda > 0
# = de Sitter), m GEOMETRIC (e^{-2Lam} = 1 - 2m/r, as in the tree and eq (12)).
ELt, _ = einstein_mixed(gt, Lambda=Lc)
phpL = sp.solve(sp.Eq(ELt[1, 1], 8*sp.pi*Pr), sp.Derivative(Phi, r))[0]
chk("with Lambda (m geometric): Phi' = (m + 4pi r^3 p_r - Lambda r^3/2)/(r(r-2m))",
    phpL - (m + 4*sp.pi*r**3*Pr - Lc*r**3/2)/(r*(r - 2*m)))
chk("  ... so eq (10) FAILS unless Lambda = 0 (shift is nonzero)",
    sp.simplify(phpL - php) != 0, True)
# matter mass m_M with m = m_M + Lambda r^3/6 recovers the textbook -Lambda r^3/3 form
mM = sp.Function("m_M")(r)
chk("  ... with matter mass m_M: (m_M + 4pi r^3 p_r - Lambda r^3/3)/(r(r-2m_M-Lambda r^3/3))",
    phpL.subs(m, mM + Lc*r**3/6).doit()
    - (mM + 4*sp.pi*r**3*Pr - Lc*r**3/3)/(r*(r - 2*mM - Lc*r**3/3)))
# r = 2m: multiplied form  nu' r (r - 2m) = 2(m + 4 pi P_r r^3) -> m + 4 pi r^3 P_r = 0 at r = 2m
mult = sp.simplify(sp.expand(nup_sol*r*(r - 2*m)))
chk("multiplied form nu' r(r-2m) = 2(m+4 pi P_r r^3) (no division)", mult - 2*(m + 4*sp.pi*Pr*r**3))

print("D. NUMERIC WITNESS: Schwarzschild constant-density interior")
import math
M, R = 1.0, 3.0            # 2M/R = 2/3 < 8/9 (Buchdahl) so P_c finite
rho = 3*M/(4*math.pi*R**3)
def mfun(x): return 4*math.pi*rho*x**3/3
def P(x):
    a, b = math.sqrt(1 - 2*M*x**2/R**3), math.sqrt(1 - 2*M/R)
    return rho*(a - b)/(3*b - a)
def nu_(x):
    return 2*math.log(1.5*math.sqrt(1 - 2*M/R) - 0.5*math.sqrt(1 - 2*M*x**2/R**3))
worst = 0.0
for x in [0.3, 0.9, 1.5, 2.1, 2.7, 2.95]:
    h = 1e-6
    d = (nu_(x+h) - nu_(x-h))/(2*h)
    rhs = 2*(mfun(x) + 4*math.pi*P(x)*x**3)/(x*(x - 2*mfun(x)))
    worst = max(worst, abs(d - rhs)/abs(rhs))
print("  max relative |nu'_numeric - eq(10)| over 6 radii = %.2e" % worst)
bad += (worst > 1e-7)
print("  boundary: P(R) = %.1e, e^{nu(R)} - (1-2M/R) = %.1e  (eqs 20, 22)"
      % (P(R), math.exp(nu_(R)) - (1 - 2*M/R)))

print("E. THE TREE'S USE: Phi' = 0 with the identity m = 4 pi r^3 p_r (I7/I8, V27)")
mm, pp, rr = sp.symbols("m p r", real=True)
sol = sp.solve([sp.Eq(mm + 4*sp.pi*rr**3*pp, 0), sp.Eq(mm, 4*sp.pi*rr**3*pp)], [mm, pp], dict=True)
chk("sympy: {Phi'=0 under eq(10), identity} -> {m:0, p:0}", 0 if sol == [{mm: 0, pp: 0}] else 1)
# Lambda = 0 is LOAD-BEARING for the tree's use: Phi' = 0 under the Lambda-form
# of G^r_r plus the identity m = 4 pi r^3 p_r no longer forces m = 0.
Ls = sp.Symbol("L", real=True)
solL = sp.solve([sp.Eq(mm + 4*sp.pi*rr**3*pp - Ls*rr**3/2, 0), sp.Eq(mm, 4*sp.pi*rr**3*pp)],
                [mm, pp], dict=True)
print("  with Lambda: {Phi'=0, identity} ->", solL)
chk("  ... m = Lambda r^3/4 (nonzero for Lambda != 0): I7/I8 need Lambda = 0",
    solL[0][mm] - Ls*rr**3/4)
try:
    import z3
except ImportError:
    print("  z3 not installed: pip install z3-solver"); bad += 1; z3 = None
if z3:
    R_, Mz, Pz, Ph, F = z3.Reals("r m p phi F")
    def run(label, extra, want):
        global bad
        s = z3.Solver()
        s.add(F > 0, R_ > 0, Ph * R_ * (R_ - 2*Mz) == Mz + F * R_**3 * Pz, Ph == 0,
              Mz == F * R_**3 * Pz, *extra)
        got = str(s.check()); ok = (got == want); bad += (not ok)
        print("  %-72s %s %s" % (label, got, "ok" if ok else "FAIL"))
    run("z3 I7 with r-2m>0 (tree's EINSTEINg), m != 0", [R_ - 2*Mz > 0, Mz != 0], "unsat")
    run("z3 I8 with r-2m>0, p != 0", [R_ - 2*Mz > 0, Pz != 0], "unsat")
    run("z3 I7 WITHOUT r-2m>0 (hypothesis not load-bearing), m != 0", [Mz != 0], "unsat")
    run("z3 vacuity guard: hypotheses alone (m = p = 0 allowed)", [], "sat")
    s = z3.Solver(); s.add(F > 0, R_ > 0, R_ - 2*Mz > 0, Ph*R_*(R_-2*Mz) == Mz + F*R_**3*Pz, Ph == 0, Mz != 0)
    got = str(s.check()); bad += (got != "sat")
    print("  %-72s %s %s" % ("z3 guard: Phi'=0 with m != 0 alone is sat (wormhole branch)", got,
                             "ok" if got == "sat" else "FAIL"))

print("\n%d check(s) not as expected" % bad)
sys.exit(1 if bad else 0)
