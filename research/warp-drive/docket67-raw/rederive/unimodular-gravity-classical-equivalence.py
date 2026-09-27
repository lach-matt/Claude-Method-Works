#!/usr/bin/env python3
"""DOCKET 67 -- re-derivation for key 'unimodular-gravity-classical-equivalence'.

What is checked (sympy, exact symbolic):
 C1  Divergence of the trace-free (unimodular) field equations.  Using only the
     contracted Bianchi identity, nabla^mu (R_mu nu - R g_mu nu /4) = nabla_nu R /4,
     so the trace-free equations imply
         nabla_nu (R + kappa T)/4 = kappa nabla^mu T_mu nu        (restatement eq.(1))
     Verified as an identity on a general time-dependent spherically symmetric metric.
 C2  WITH nabla.T = 0 imposed: Lambda := (R + kappa T)/4 is constant on a connected
     domain and the trace-free equations become G + Lambda g = kappa T exactly
     (checked: E_tf = 0 and G + Lambda g - kappa T differ by a pure-trace term that
     vanishes by definition of Lambda).
 C3  WITHOUT it: an explicit flat-FLRW witness -- dust with rho(t) chosen so the
     trace-free equation holds -- solves unimodular gravity with nabla.T != 0 and
     Lambda(t) non-constant; it solves GR+constant-Lambda for NO constant Lambda.
     So the conservation hypothesis is load-bearing for 'same equations'.
 C4  Static wormhole (restatement 2603.14718 Sec.III): the trace-free system has
     rank 2 in (rho, p_r, p_t), GR has rank 3; adding the radial conservation
     (TOV) equation restores GR-with-Lambda.
 C5  For matter from a diffeomorphism-invariant action (minimally coupled scalar),
     nabla^mu T_mu nu = (Box phi - V'(phi)) d_nu phi, i.e. conservation holds on the
     MATTER shell independently of the gravity equations -- evidence that the
     hypothesis dropped in the tree is satisfied by ordinary Lagrangian matter.
Exit 0 iff every check passes.
"""
import sys
import sympy as sp

t, r, th, ph = sp.symbols('t r theta phi', real=True)
X = [t, r, th, ph]
kap = sp.symbols('kappa', positive=True)
FAIL = []

def chk(name, cond):
    print(("PASS " if cond else "FAIL ") + name)
    if not cond:
        FAIL.append(name)

def geom(g):
    gi = sp.simplify(g.inv())
    n = 4
    Gam = [[[sp.simplify(sum(gi[a, d] * (sp.diff(g[d, b], X[c]) + sp.diff(g[d, c], X[b])
                                     - sp.diff(g[b, c], X[d])) for d in range(n)) / 2)
             for c in range(n)] for b in range(n)] for a in range(n)]
    Ric = sp.zeros(n)
    for b in range(n):
        for c in range(n):
            Ric[b, c] = sp.simplify(sum(sp.diff(Gam[a][b][c], X[a]) - sp.diff(Gam[a][b][a], X[c])
                                        + sum(Gam[a][a][d] * Gam[d][b][c] - Gam[a][c][d] * Gam[d][b][a]
                                              for d in range(n)) for a in range(n)))
    R = sp.simplify(sum(gi[a, b] * Ric[a, b] for a in range(n) for b in range(n)))
    return gi, Gam, Ric, R

def div_lower(gi, Gam, S):
    """nabla^mu S_{mu nu} for symmetric covariant S."""
    n = 4
    out = []
    for nu in range(n):
        val = 0
        for mu in range(n):
            for a in range(n):
                # nabla_a S_{mu nu}
                cov = sp.diff(S[mu, nu], X[a]) - sum(Gam[l][a][mu] * S[l, nu] + Gam[l][a][nu] * S[mu, l]
                                                     for l in range(n))
                val += gi[a, mu] * cov
        out.append(sp.simplify(val))
    return out

# ---------------------------------------------------------------- C1
A = sp.Function('A')(t, r); B = sp.Function('B')(t, r); C = sp.Function('C')(t, r)
g = sp.diag(-sp.exp(2 * A), sp.exp(2 * B), C**2, C**2 * sp.sin(th)**2)
gi, Gam, Ric, R = geom(g)
TF = Ric - R * g / 4
d = div_lower(gi, Gam, TF)
rhs = [sp.diff(R, x) / 4 for x in X]
chk("C1 nabla^mu(R_mu nu - R g/4) == d_nu R/4 on general time-dependent spherical metric (all 4 nu)",
    all(sp.simplify(d[i] - rhs[i]) == 0 for i in range(4)))
# hence trace-free eqs  TF = kappa (T - T g/4)  =>  d_nu R/4 = kappa (div T)_nu - kappa d_nu T/4
print("     => nabla_nu (R + kappa T)/4 = kappa nabla^mu T_mu nu   [restatement 2603.14718 eq.(1), rearranged]")

# ---------------------------------------------------------------- C2
# algebraic: if TF - kappa(T - Tg/4) = 0 and Lambda := (R+kappa T)/4 then
# G + Lambda g - kappa T = [TF - kappa(T - T g/4)] identically
Rs, Ts, Lam = sp.symbols('R T Lambda')
Ricm = sp.Matrix(4, 4, lambda i, j: sp.Symbol('Ric%d%d' % (min(i, j), max(i, j))))
Tm = sp.Matrix(4, 4, lambda i, j: sp.Symbol('T%d%d' % (min(i, j), max(i, j))))
gm = sp.Matrix(4, 4, lambda i, j: sp.Symbol('g%d%d' % (min(i, j), max(i, j))))
lhs = (Ricm - Rs * gm / 2) + ((Rs + kap * Ts) / 4) * gm - kap * Tm
tfe = (Ricm - Rs * gm / 4) - kap * (Tm - Ts * gm / 4)
chk("C2 G + Lambda g - kappa T == trace-free equation, with Lambda := (R + kappa T)/4 (identity)",
    sp.simplify(lhs - tfe) == sp.zeros(4))
print("     with nabla.T = 0, C1 gives d_nu Lambda = 0: Lambda is an INTEGRATION CONSTANT on each connected domain")

# ---------------------------------------------------------------- C3 FLRW witness
a = sp.Function('a')(t)
gF = sp.diag(-1, a**2, a**2 * r**2, a**2 * r**2 * sp.sin(th)**2)
giF, GamF, RicF, RF = geom(gF)
H = sp.diff(a, t) / a
rho = sp.Function('rho')(t)
# dust, u = d_t:  T_mu nu = rho u_mu u_nu, u_mu = (-1,0,0,0)
TF_ = sp.zeros(4); TF_[0, 0] = rho
Ttr = sp.simplify(sum(giF[i, j] * TF_[i, j] for i in range(4) for j in range(4)))   # = -rho
E = sp.simplify(RicF - RF * gF / 4 - kap * (TF_ - Ttr * gF / 4))
# only one independent component: solve E_tt = 0 for rho
sol = sp.solve(sp.Eq(E[0, 0], 0), rho)
chk("C3a trace-free FLRW dust system reduces to ONE equation (E_rr ∝ E_tt)",
    len(sol) == 1 and all(sp.simplify(E[i, i].subs(rho, sol[0])) == 0 for i in range(4)))
rho_s = sp.simplify(sol[0])
print("     rho solving UG =", rho_s, " (i.e. kappa rho = -2 dH/dt)")
# pick a concrete scale factor with no GR+const-Lambda dust counterpart
aw = sp.exp(t**2)      # H = 2t, dH/dt = 2 : rho = -4/kappa ... choose instead a = t^(1/2)
aw = sp.sqrt(t)        # H = 1/(2t), dH/dt = -1/(2t^2): kappa rho = 1/t^2 > 0
rho_w = sp.simplify(rho_s.subs(a, aw).doit())
chk("C3b witness a = t^(1/2): rho = 1/(kappa t^2) > 0 (ordinary positive-density dust)",
    sp.simplify(rho_w - 1 / (kap * t**2)) == 0)
divT = div_lower(giF, GamF, TF_)
div_w = sp.simplify(divT[0].subs(rho, rho_w).subs(a, aw).doit())
chk("C3c witness violates conservation: nabla^mu T_mu t != 0", sp.simplify(div_w) != 0)
print("     nabla^mu T_mu t =", div_w)
Lam_w = sp.simplify(((RF + kap * Ttr) / 4).subs(rho, rho_w).subs(a, aw).doit())
chk("C3d effective Lambda(t) = (R + kappa T)/4 is NOT constant", sp.simplify(sp.diff(Lam_w, t)) != 0)
print("     Lambda(t) =", Lam_w)
GF = RicF - RF * gF / 2
L0 = sp.symbols('Lambda0')
eq_tt = sp.simplify((GF + L0 * gF - kap * TF_)[0, 0].subs(rho, rho_w).subs(a, aw).doit())
solL = sp.solve(sp.Eq(eq_tt, 0), L0)
chk("C3e GR + constant Lambda fails: the tt equation demands Lambda0 depending on t",
    len(solL) == 1 and sp.diff(solL[0], t) != 0)
print("     Lambda0 demanded by G_tt + Lambda0 g_tt = kappa T_tt :", sp.simplify(solL[0]))

# ---------------------------------------------------------------- C4 static wormhole
Phi = sp.Function('Phi')(r); b = sp.Function('b')(r)
gW = sp.diag(-sp.exp(2 * Phi), 1 / (1 - b / r), r**2, r**2 * sp.sin(th)**2)
giW, GamW, RicW, RW = geom(gW)
rh, pr, pt = sp.symbols('rho p_r p_t')
Tmix = sp.diag(-rh, pr, pt, pt)           # T^mu_nu
Tl = sp.simplify(gW * Tmix)               # T_mu nu = g_mu a T^a_nu
Tt = -rh + pr + 2 * pt
EW = sp.simplify(RicW - RW * gW / 4 - kap * (Tl - Tt * gW / 4))
EWm = sp.simplify(giW * EW)               # mixed E^mu_nu
eqs_tf = [EWm[0, 0], EWm[1, 1], EWm[2, 2]]
Jtf = sp.Matrix([[sp.diff(e, v) for v in (rh, pr, pt)] for e in eqs_tf])
GW = sp.simplify(giW * (RicW - RW * gW / 2))
eqs_gr = [GW[i, i] - kap * Tmix[i, i] for i in range(3)]
Jgr = sp.Matrix([[sp.diff(e, v) for v in (rh, pr, pt)] for e in eqs_gr])
chk("C4a trace-free static system: rank 2 in (rho,p_r,p_t) [restatement p.5: 'only two independent equations']",
    Jtf.rank(simplify=True) == 2)
chk("C4b Einstein static system: rank 3 [restatement p.5: 'three independent equations']",
    Jgr.rank(simplify=True) == 3)
# add conservation (radial): p_r' = -(rho+p_r) Phi' - 2 (p_r - p_t)/r, with rho,p_r,p_t functions of r
rhf, prf, ptf = [sp.Function(n)(r) for n in ('rhof', 'prf', 'ptf')]
TmixF = sp.diag(-rhf, prf, ptf, ptf)
TlF = sp.simplify(gW * TmixF)
dT = div_lower(giW, GamW, TlF)
tov = sp.simplify(dT[1])                  # nabla^mu T_mu r = nabla_mu T^mu_r (metric compatibility)
tov_expected = sp.diff(prf, r) + (rhf + prf) * sp.diff(Phi, r) + 2 * (prf - ptf) / r
chk("C4c radial conservation = TOV form p_r' + (rho+p_r)Phi' + 2(p_r-p_t)/r",
    sp.simplify(tov - tov_expected) == 0)
TtF = -rhf + prf + 2 * ptf
LamW = (RW + kap * TtF) / 4
# on the trace-free shell, d_r Lambda = kappa * (div T)_r  (C1 specialised): check symbolically
EWF = sp.simplify(giW * (RicW - RW * gW / 4 - kap * (TlF - TtF * gW / 4)))
# solve the trace-free shell for p_r, p_t in terms of rho (restatement eqs.19-20)
solW = sp.solve([EWF[1, 1], EWF[2, 2]], [prf, ptf], dict=True)
ok = False
if solW:
    s = solW[0]
    dLam = sp.simplify(sp.diff(LamW.subs(s), r).doit())
    # recompute conservation with substituted p_r, p_t as explicit functions
    tov_s = sp.simplify((tov_expected.subs(s)).doit())
    ok = sp.simplify(dLam - kap * tov_s) == 0
chk("C4d on the trace-free shell d_r Lambda == kappa x (TOV expression): conservation <=> Lambda constant",
    ok)

# ---------------------------------------------------------------- C5 scalar matter
f = sp.Function('f')(t, r); V = sp.Function('V')
gi5, Gam5 = gi, Gam
dphi = [sp.diff(f, x) for x in X]
kin = sum(gi5[i, j] * dphi[i] * dphi[j] for i in range(4) for j in range(4))
Tsc = sp.Matrix(4, 4, lambda i, j: dphi[i] * dphi[j] - g[i, j] * (kin / 2 + V(f)))
sqrtg = sp.sqrt(-g.det())
box = sp.simplify(sum(sp.diff(sqrtg * gi5[i, j] * dphi[j], X[i]) for i in range(4) for j in range(4)) / sqrtg)
dTs = div_lower(gi5, Gam5, Tsc)
chk("C5 scalar field: nabla^mu T_mu nu == (Box phi - V'(phi)) d_nu phi (conservation on the matter shell)",
    all(sp.simplify(sp.expand(dTs[i] - (box - sp.diff(V(f), f)) * dphi[i])) == 0 for i in range(4)))

print()
print("SUMMARY: %d FAIL" % len(FAIL))
sys.exit(1 if FAIL else 0)
