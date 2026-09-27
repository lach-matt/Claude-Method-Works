#!/usr/bin/env python3
"""DOCKET 67 -- re-derivation for key 'modified-gravity-effective-stress'.

The tree (overturn.py:234-241) uses: "In f(R), scalar-tensor, Einstein-Gauss-Bonnet or
any higher-curvature theory the field equations rearrange to
    G = 8 pi T^matter + T^effective
where T^effective is built from curvature. An effective term can be negative where the
matter term is not."

Checks (sympy, exact):
 A  Sotiriou-Faraoni (0805.1726) eq (6) -> eq (10)/(11)/(12): the f(R) rearrangement is an
    identity, on a general static spherical metric with arbitrary F(r), f(r).
 A2 In the TREE's form (coefficient 8 pi on T^matter) T^effective contains the matter term
    8 pi (1/F - 1) T: it is NOT built from curvature alone unless F == 1.
 A3 SF eq (55) (Brans-Dicke omega=0 form) equals eq (10) under phi=F, V=RF-f; T^eff there is
    built from the scalar phi, not curvature.
 B  Einstein-Gauss-Bonnet: the Gauss-Bonnet tensor H_mn vanishes IDENTICALLY in D=4 (so
    T^eff == 0 there) and not in D=5; trace H = -(D-4)/2 * GB.  Exact rational curvature
    jets at a point (generic: any algebraic jet), several random draws.
 C  Lobo-Oliveira (0909.5539), the published "matter satisfies WEC, effective term violates
    NEC" construction: (i) eqs (16)-(18) satisfy (10)-(12); (ii) (10)-(12) are invariant under
    rho -> rho - l, p -> p + l, so (16)-(18) are one member of a family fixed only by the trace
    equation (3) with f_R = F; (iii) sign of F in the published WEC examples; (iv) whether the
    reconstructed f(R) obeys df/dR = F.
 D  Static, Phi' = 0, metric f(R): rho = f/2 - box F exactly, so eq (16) rho = F b'/r^2 holds
    iff f = F R + 2 box F; with rho_eff := b'/r^2 (Lobo eq 10 LHS) one has, ON eq (16),
    sign(rho) = sign(F) * sign(rho_eff): negative effective density under non-negative matter
    density needs F < 0 (G_eff < 0, ghost graviton) in that class.
Exit 0 iff every assertion holds.
"""
import sys, random
from fractions import Fraction as Fr
import itertools
import sympy as sp

OK = True
def chk(name, cond):
    global OK
    print(("PASS " if cond else "FAIL ") + name)
    OK = OK and bool(cond)

# ---------------------------------------------------------------- curvature (sympy)
def curvature(g, X):
    n = len(X)
    gi = sp.simplify(g.inv())
    Gam = [[[sp.simplify(sum(gi[a, d]*(sp.diff(g[d, b], X[c]) + sp.diff(g[d, c], X[b])
             - sp.diff(g[b, c], X[d])) for d in range(n))/2) for c in range(n)]
             for b in range(n)] for a in range(n)]
    # R^a_{bcd} = d_c Gam^a_{db} - d_d Gam^a_{cb} + Gam^a_{ce}Gam^e_{db} - Gam^a_{de}Gam^e_{cb}
    Ric = sp.zeros(n)
    for b in range(n):
        for d in range(n):
            s = 0
            for a in range(n):
                c = a
                s += sp.diff(Gam[a][d][b], X[c]) - sp.diff(Gam[a][c][b], X[d])
                for e in range(n):
                    s += Gam[a][c][e]*Gam[e][d][b] - Gam[a][d][e]*Gam[e][c][b]
            Ric[b, d] = sp.simplify(s)
    Rs = sp.simplify(sum(gi[a, b]*Ric[a, b] for a in range(n) for b in range(n)))
    return gi, Gam, Ric, Rs

def hess_mixed(phi, g, gi, Gam, X):
    """(nabla^m nabla_n phi) as a mixed tensor, and box phi."""
    n = len(X)
    H = sp.zeros(n)
    for a in range(n):
        for b in range(n):
            H[a, b] = sp.diff(phi, X[a], X[b]) - sum(Gam[c][a][b]*sp.diff(phi, X[c]) for c in range(n))
    Hm = sp.simplify(gi*H)
    box = sp.simplify(Hm.trace())
    return Hm, box

t, r, th, ph = sp.symbols('t r theta phi', real=True)
X = [t, r, th, ph]
Phi = sp.Function('Phi')(r); b = sp.Function('b')(r)
g = sp.diag(-sp.exp(2*Phi), 1/(1 - b/r), r**2, r**2*sp.sin(th)**2)
gi, Gam, Ric, Rs = curvature(g, X)
Ricm = sp.simplify(gi*Ric)
Gm = sp.simplify(Ricm - sp.eye(4)*Rs/2)          # G^m_n
F = sp.Function('F')(r); f = sp.Function('f')(r); kap = sp.Symbol('kappa', positive=True)
Hm, boxF = hess_mixed(F, g, gi, Gam, X)

# ---- A: SF eq (6) E^m_n := F R^m_n - f/2 d - [nabla^m nabla_n - d box] F  (= kappa T^m_n)
E = sp.simplify(F*Ricm - sp.eye(4)*f/2 - Hm + sp.eye(4)*boxF)
Tm = E/kap                                             # matter T^m_n defined by the field eq
Teff_SF = (sp.eye(4)*(f - Rs*F)/2 + Hm - sp.eye(4)*boxF)/kap   # SF eq (12), mixed
rhs10 = kap*Tm/F + kap*Teff_SF/F                       # SF eq (11)
chk("A  SF eq(6) <=> eq(10)/(11)/(12): G^m_n - kappa(T+T_eff)/F == 0 identically",
    all(sp.simplify(Gm[i, j] - rhs10[i, j]) == 0 for i in range(4) for j in range(4)))
# Bianchi-type consistency is not assumed here; the identity is purely algebraic.

# ---- A2: tree form G = 8 pi T + T_eff_tree  =>  T_eff_tree = G - kappa T
Teff_tree = sp.simplify(Gm - kap*Tm)
# express it as (coefficient)*kappa*T + (curvature/F-only part)
resid = sp.simplify(Teff_tree - (kap*Tm*(1/F - 1) + kap*Teff_SF/F))
chk("A2 T_eff(tree form) == kappa T (1/F - 1) + kappa T_eff^SF / F  (contains matter unless F==1)",
    all(sp.simplify(resid[i, j]) == 0 for i in range(4) for j in range(4)))
coef = sp.simplify((1/F - 1).subs(F, sp.Rational(1, 2)))
chk("A2 e.g. F=1/2 (f=R/2+...): coefficient of kappa T inside T_eff(tree) = 1 != 0", coef == 1)

# ---- A3: SF eq (55) with phi = F, V = R F - f  equals eq (10)
V = Rs*F - f
rhs55 = kap*Tm/F - sp.eye(4)*V/(2*F) + (Hm - sp.eye(4)*boxF)/F
chk("A3 SF eq(55) [phi=F, V=RF-f] == SF eq(10) identically (T_eff built from phi, V(phi))",
    all(sp.simplify(rhs55[i, j] - rhs10[i, j]) == 0 for i in range(4) for j in range(4)))

# ---------------------------------------------------------------- B: Gauss-Bonnet tensor
def rand_jet(D, seed):
    rng = random.Random(seed)
    # Lorentzian g0 = diag(-1,1,..) + small symmetric rational perturbation
    g0 = [[Fr(0)]*D for _ in range(D)]
    for i in range(D):
        g0[i][i] = Fr(-1 if i == 0 else 1)
    for i in range(D):
        for j in range(i, D):
            e = Fr(rng.randint(-3, 3), 17)
            g0[i][j] += e
            if i != j: g0[j][i] += e
    dg = [[[Fr(0)]*D for _ in range(D)] for _ in range(D)]      # dg[a][b][c] = d_c g_ab
    for a in range(D):
        for b2 in range(a, D):
            for c in range(D):
                v = Fr(rng.randint(-5, 5), rng.randint(1, 4))
                dg[a][b2][c] = v; dg[b2][a][c] = v
    ddg = {}                                                     # d_c d_d g_ab
    for a in range(D):
        for b2 in range(a, D):
            for c in range(D):
                for d in range(c, D):
                    v = Fr(rng.randint(-5, 5), rng.randint(1, 4))
                    for (x, y) in {(a, b2), (b2, a)}:
                        for (u, w) in {(c, d), (d, c)}:
                            ddg[(x, y, u, w)] = v
    return g0, dg, ddg

def inv(M):
    n = len(M); A = [row[:] + [Fr(int(i == j)) for j in range(n)] for i, row in enumerate(M)]
    for c in range(n):
        p = next(i for i in range(c, n) if A[i][c] != 0); A[c], A[p] = A[p], A[c]
        pv = A[c][c]; A[c] = [x/pv for x in A[c]]
        for i in range(n):
            if i != c and A[i][c] != 0:
                fct = A[i][c]; A[i] = [x - fct*y for x, y in zip(A[i], A[c])]
    return [row[n:] for row in A]

def riemann_at_point(D, g0, dg, ddg):
    gi = inv(g0); R = range(D)
    # Gamma_{d b c} (first kind) and its derivative
    G1 = [[[ (dg[d][b][c] + dg[d][c][b] - dg[b][c][d])/2 for c in R] for b in R] for d in R]
    dG1 = [[[[ (ddg[(d, b, c, e)] + ddg[(d, c, b, e)] - ddg[(b, c, d, e)])/2 for e in R]
              for c in R] for b in R] for d in R]
    Gam = [[[ sum(gi[a][d]*G1[d][b][c] for d in R) for c in R] for b in R] for a in R]
    # d_e g^{ad} = -g^{ap} d_e g_{pq} g^{qd}
    dgi = [[[ -sum(gi[a][p]*dg[p][q][e]*gi[q][d] for p in R for q in R) for e in R] for d in R] for a in R]
    dGam = [[[[ sum(dgi[a][d][e]*G1[d][b][c] + gi[a][d]*dG1[d][b][c][e] for d in R)
                for e in R] for c in R] for b in R] for a in R]   # d_e Gam^a_{bc}
    Rup = [[[[ dGam[a][d][b][c] - dGam[a][c][b][d]
              + sum(Gam[a][c][e]*Gam[e][d][b] - Gam[a][d][e]*Gam[e][c][b] for e in R)
              for d in R] for c in R] for b in R] for a in R]     # R^a_{bcd}
    Rdn = [[[[ sum(g0[a][p]*Rup[p][b][c][d] for p in R) for d in R] for c in R] for b in R] for a in R]
    return gi, Rdn

def gb_tensor(D, gi, Rd, g0):
    R = range(D)
    def up(T4):   # raise all four indices
        return [[[[ sum(gi[a][p]*gi[b][q]*gi[c][s]*gi[d][u]*T4[p][q][s][u]
                   for p in R for q in R for s in R for u in R) for d in R] for c in R] for b in R] for a in R]
    Ru = up(Rd)
    Ric = [[ sum(gi[a][c]*Rd[a][m][c][n] for a in R for c in R) for n in R] for m in R]   # R_mn = R^a_{man}
    Ricu = [[ sum(gi[m][p]*gi[n][q]*Ric[p][q] for p in R for q in R) for n in R] for m in R]
    Rs = sum(gi[m][n]*Ric[m][n] for m in R for n in R)
    riem2 = sum(Rd[a][b][c][d]*Ru[a][b][c][d] for a in R for b in R for c in R for d in R)
    ric2 = sum(Ric[m][n]*Ricu[m][n] for m in R for n in R)
    GB = riem2 - 4*ric2 + Rs*Rs
    H = [[None]*D for _ in R]
    for m in R:
        for n in R:
            t1 = Rs*Ric[m][n]
            t2 = sum(Rd[m][a][n][bb]*Ricu[a][bb] for a in R for bb in R)
            # R_{m a b s} R_n^{a b s} = R_{m a b s} R_{n p q u} g^{ap} g^{bq} g^{su}
            t3 = sum(Rd[m][a][bb][s]*Rd[n][p][q][u]*gi[a][p]*gi[bb][q]*gi[s][u]
                     for a in R for bb in R for s in R for p in R for q in R for u in R) if D <= 4 else None
            if t3 is None:
                # faster: contract with Ru
                t3 = sum(Rd[m][a][bb][s]*sum(g0[n][p]*Ru[p][a][bb][s] for p in R)
                         for a in R for bb in R for s in R)
            t4 = sum(Ric[m][a]*sum(gi[a][p]*Ric[p][n] for p in R) for a in R)
            H[m][n] = 2*(t1 - 2*t2 + t3 - 2*t4 - Fr(1, 4)*g0[m][n]*GB)
    trH = sum(gi[m][n]*H[m][n] for m in R for n in R)
    return H, GB, trH

for D, seeds in ((4, (1, 2, 3)), (5, (7,))):
    for sd in seeds:
        g0, dg, ddg = rand_jet(D, sd)
        gi_, Rd = riemann_at_point(D, g0, dg, ddg)
        H, GB, trH = gb_tensor(D, gi_, Rd, g0)
        allzero = all(H[m][n] == 0 for m in range(D) for n in range(D))
        if D == 4:
            chk(f"B  D=4 seed {sd}: Gauss-Bonnet tensor H_mn == 0 exactly (GB scalar = {float(GB):.4g} != 0)",
                allzero and GB != 0)
        else:
            chk(f"B  D=5 seed {sd}: H_mn != 0 (max |H| = {float(max(abs(H[m][n]) for m in range(D) for n in range(D))):.4g})",
                not allzero)
        chk(f"B  D={D} seed {sd}: trace H == -(D-4)/2 * GB exactly", trH == -Fr(D - 4, 2)*GB)

# ---------------------------------------------------------------- C/D: Lobo-Oliveira, Phi' = 0
g0s = g.subs(Phi, 0).doit()
gi0, Gam0, Ric0, Rs0 = curvature(g0s, X)
Ricm0 = sp.simplify(gi0*Ric0)
Hm0, boxF0 = hess_mixed(F, g0s, gi0, Gam0, X)
chk("C  R = 2 b'/r^2 for Phi'=0 (Lobo eq 14)", sp.simplify(Rs0 - 2*sp.diff(b, r)/r**2) == 0)
box_lobo = (1 - b/r)*(sp.diff(F, r, 2) - (sp.diff(b, r)*r - b)/(2*r**2*(1 - b/r))*sp.diff(F, r) + 2*sp.diff(F, r)/r)
chk("C  box F matches Lobo eq (15)", sp.simplify(boxF0 - box_lobo) == 0)
E0 = sp.simplify(F*Ricm0 - sp.eye(4)*f/2 - Hm0 + sp.eye(4)*boxF0)   # kappa = 1 (Lobo)
rho_true = sp.simplify(-E0[0, 0]); pr_true = sp.simplify(E0[1, 1]); pt_true = sp.simplify(E0[2, 2])
chk("D  static Phi'=0 metric f(R): rho = f/2 - box F exactly", sp.simplify(rho_true - (f/2 - boxF0)) == 0)

bp = sp.diff(b, r); Fp = sp.diff(F, r); Fpp = sp.diff(F, r, 2)
rho16 = F*bp/r**2
pr17 = -b*F/r**3 + Fp/(2*r**2)*(bp*r - b) - Fpp*(1 - b/r)
pt18 = -Fp/r*(1 - b/r) + F/(2*r**3)*(b - bp*r)
# Lobo eqs (10)-(12) as residuals, H = (F R + box F + T)/4
def lobo_resid(rho, pr, pt):
    T = -rho + pr + 2*pt
    Hh = (F*Rs0 + boxF0 + T)/4
    e10 = bp/r**2 - rho/F - Hh/F
    e11 = -b/r**3 - pr/F - ((1 - b/r)*(Fpp - Fp*(bp*r - b)/(2*r**2*(1 - b/r))) - Hh)/F
    e12 = -(bp*r - b)/(2*r**3) - pt/F - ((1 - b/r)*Fp/r - Hh)/F
    return [sp.simplify(e) for e in (e10, e11, e12)], sp.simplify(Hh)
res, H16 = lobo_resid(rho16, pr17, pt18)
chk("C(i)  Lobo (16)-(18) satisfy Lobo (10)-(12)", all(e == 0 for e in res))
chk("C(i)  ...and on (16)-(18) the function H = (FR + box F + T)/4 vanishes identically", H16 == 0)
lam = sp.Function('lam')(r)
res2, _ = lobo_resid(rho16 - lam, pr17 + lam, pt18 + lam)
chk("C(ii) (10)-(12) invariant under rho->rho-l, p->p+l for ARBITRARY l(r): (16)-(18) not unique",
    all(e == 0 for e in res2))
# the TRUE field equations fix the matter once f is given; eq (16) is the true rho iff f = F R + 2 box F
chk("D  eq(16) is the true rho  <=>  f = F R + 2 box F",
    sp.simplify((rho_true - rho16).subs(f, F*Rs0 + 2*boxF0)) == 0)
# on eq (16): sign(rho) = sign(F) sign(rho_eff) with rho_eff := b'/r^2 (Lobo eq 10 LHS, kappa=1)
chk("D  on eq(16): rho == F * rho_eff, rho_eff = b'/r^2  (rho>=0 & rho_eff<0 => F<0)",
    sp.simplify(rho16 - F*(bp/r**2)) == 0)

# ---- C(iii),(iv): the published WEC examples, b = r0^2/r
r0 = sp.Symbol('r0', positive=True); x = sp.Symbol('x', positive=True)
bb = r0**2/r
def ex_eval(Fexpr, label):
    subs = {b: bb, F: Fexpr}
    rho = sp.simplify(rho16.subs(F, Fexpr).subs(b, bb).doit())
    pr = sp.simplify(pr17.subs(F, Fexpr).subs(b, bb).doit())
    pt = sp.simplify(pt18.subs(F, Fexpr).subs(b, bb).doit())
    Rr = sp.simplify(Rs0.subs(b, bb).doit())
    bx = sp.simplify(boxF0.subs(F, Fexpr).subs(b, bb).doit())
    T = sp.simplify(-rho + pr + 2*pt)
    # f reconstructed from the trace eq (3): F R - 2 f + 3 box F = T
    frec = sp.simplify((Fexpr*Rr + 3*bx - T)/2)
    consist = sp.simplify(sp.diff(frec, r) - Fexpr*sp.diff(Rr, r))   # needs df/dr = F dR/dr
    return rho, pr, pt, Rr, T, frec, consist

# Example (31) with C1=-1, alpha=-1: F = C1 (1 - r0^2/r^2)^{1/2+alpha/2} = -1
Fa = sp.Integer(-1)
rho, pr, pt, Rr, T, frec, consist = ex_eval(Fa, "31")
pts = [sp.Rational(k, 4)*r0 for k in (5, 6, 8, 12, 20)]
chk("C(iii) ex.(31) C1=-1, alpha=-1: F == -1 < 0 everywhere (G_eff<0)", Fa < 0)
chk("C(iii) ex.(31): matter rho = r0^2/r^4 > 0, rho+p_r >= 0 (WEC as published)",
    sp.simplify(rho - r0**2/r**4) == 0 and all((rho + pr).subs(r, p) >= 0 for p in pts))
chk("C(iii) ex.(31): rho_eff + p_r^eff = (b'r-b)/r^3 = -2 r0^2/r^4 < 0 (NEC of T_eff violated)",
    sp.simplify((sp.diff(bb, r)*r - bb)/r**3 + 2*r0**2/r**4) == 0)
chk("C(iv) ex.(31): f from trace eq(3) obeys df/dR = F (consistent; f = -R, i.e. GR with G -> -G)",
    consist == 0 and sp.simplify(frec + Rr) == 0)
# printed eq (34) with C1=-1, alpha=-1 as extracted: f = C1 R (1-sqrt(R/R0))^{alpha/2-1/2} [sqrt(R/R0)(alpha^2+2alpha+2)+(alpha+2)]
Rsym, R0 = sp.symbols('R R0', negative=True)
al = -1; C1 = -1
f34 = C1*Rsym*(1 - sp.sqrt(Rsym/R0))**sp.Rational(al - 1, 2)*(sp.sqrt(Rsym/R0)*(al**2 + 2*al + 2) + (al + 2))
d34 = sp.simplify(sp.diff(f34, Rsym))
val = d34.subs({Rsym: -sp.Rational(1, 2), R0: -2})
print("     printed eq(34) as extracted, alpha=-1: df/dR at R/R0=1/4 =", sp.nsimplify(val), "(eq (31) says F = -1)")
DISCREP_34 = (sp.simplify(val + 1) != 0)
print("     -> eq(34) as extracted " + ("DISAGREES" if DISCREP_34 else "agrees") +
      " with eq(31)/(3) at alpha=-1: recorded as a DISCREPANCY (PDF extraction or misprint), not a refutation")

# Example (25) traceless, C1=0, C2=-1: F = -cosh(sqrt2 arctan(r0/sqrt(r^2-r0^2)))
Fb = -sp.cosh(sp.sqrt(2)*sp.atan(r0/sp.sqrt(r**2 - r0**2)))
rho, pr, pt, Rr, T, frec, consist = ex_eval(Fb, "25")
chk("C(iii) ex.(25) C1=0,C2=-1: F <= -1 < 0 on r>r0 (G_eff<0 throughout)",
    all(Fb.subs(r, p).evalf() < 0 for p in pts))
chk("C(iii) ex.(25): T = 0 (traceless EoS, eq 24 solved)", all(abs(T.subs(r, p).evalf()) < 1e-12 for p in pts))
cvals = [consist.subs({r: p}).subs(r0, 1).evalf() for p in (sp.Rational(5, 4), 2, 3)]
print("     ex.(25): df/dr - F dR/dr with f from trace eq(3), r0=1, r=1.25,2,3:", [float(c) for c in cvals])
EX25_CONSISTENT = all(abs(c) < 1e-10 for c in cvals)
print("     -> ex.(25) " + ("IS" if EX25_CONSISTENT else "is NOT") +
      " a solution of metric f(R) with f(R) reconstructed from the trace equation (needs f_R = F)")

# ---- C(v): the matter the field equations actually give for ex.(25) when f_R = F is enforced
# f = c + int_0^R F dR'  (R<0 here; R -> 0 at r -> infinity).  rho + p_r is invariant under the
# l-shift (C ii), so the published NEC-type sign stands; rho itself moves.
Rr25 = sp.simplify(Rs0.subs(b, bb).doit()).subs(r0, 1)
F25 = Fb.subs(r0, 1)
def f_true(rv, c=0.0):
    # integrate F dR along r from infinity (R=0) to rv: f(R(rv)) = c + int_inf^rv F(r) R'(r) dr
    import mpmath as mp
    Fr_ = sp.lambdify(r, F25, 'mpmath'); dR = sp.lambdify(r, sp.diff(Rr25, r), 'mpmath')
    return c + float(mp.quad(lambda u: Fr_(u)*dR(u), [mp.inf, rv]))
box25 = sp.lambdify(r, sp.simplify(boxF0.subs(F, Fb).subs(b, bb).doit()).subs(r0, 1), 'mpmath')
rho16_25 = sp.lambdify(r, sp.simplify(rho16.subs(F, Fb).subs(b, bb).doit()).subs(r0, 1), 'mpmath')
for rv in (1.25, 2.0, 3.0):
    rt = f_true(rv)/2 - float(box25(rv))
    print(f"     ex.(25) r={rv}: published rho(16) = {float(rho16_25(rv)):+.5f}; true rho with f=int F dR (c=0) = {rt:+.5f}")
print("     -> published rho(16) is not the matter density for f_R = F; rho+p_r (NEC-type) is unchanged;")
print("        rho can be made >= 0 by the integration constant c (a cosmological-constant shift).")

# ---- E: evidence the OTHER way: an effective term negative with F > 0 and no ghost
Lam = sp.Symbol('Lambda')
fL = Rs - 2*Lam      # f(R) = R - 2 Lambda, F = 1
EL = sp.simplify(Ricm - sp.eye(4)*fL/2)          # kappa T^m_n
TeffL = sp.simplify(Gm - EL)                      # tree form T_eff = G - kappa T
chk("E  f = R - 2 Lambda (F = 1 > 0): T_eff(tree)^m_n == -Lambda delta^m_n; effective density = Lambda",
    all(sp.simplify(TeffL[i, j] - (-Lam if i == j else 0)) == 0 for i in range(4) for j in range(4)))
print("     -> Lambda < 0 gives a NEGATIVE effective energy density with F = 1 > 0, no ghost, any matter:")
print("        the tree's weak claim 'can be negative' holds without a ghost -- but this example is GR + Lambda.")

print("\nSUMMARY: rearrangement = identity (A); tree's '8 pi' form puts matter inside T_eff unless F=1 (A2);")
print("scalar-tensor T_eff built from phi (A3); 4D EGB contributes T_eff == 0 identically (B);")
print("published WEC-respecting f(R) examples have F < 0 (C iii); in static Phi'=0 class on Lobo's")
print("eq (16), negative rho_eff with rho >= 0 requires F < 0 (D).")
print("ALL PASS" if OK else "SOME FAIL")
sys.exit(0 if OK else 1)
