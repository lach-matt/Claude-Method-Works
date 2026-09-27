#!/usr/bin/env python3
"""DOCKET 67 re-derivation: Israel/Lanczos thin shell + Poisson-Visser linearisation,
as used in research/warp-drive/linstab.py (poisson_visser, device_closed_form).
Independent of linstab.py: rebuilt from the junction condition, then compared.
Sources READ: Poisson & Visser gr-qc/9506083 eqs (11)-(13),(18)-(19),(27),(29)-(36);
Ishak & Lake gr-qc/0108058 eq (5), eq (21), sec III.B (R/m+ ~ 2.37 and ~ 3 at P'/sigma' = 1).
"""
import sympy as sp, z3, sys
ok = []
def chk(name, cond):
    ok.append(bool(cond)); print(("PASS " if cond else "FAIL ") + name)

R, ms, Mi, Mo, b2, Rd2 = sp.symbols('R m_s M_in M_out beta2 Rdot2', real=True)
fi, fo = 1 - 2*Mi/R, 1 - 2*Mo/R
# ---- 1. V from the Israel junction sqrt(fi+Rd^2) - sqrt(fo+Rd^2) = m_s/R (outward normals, eps=+1 both)
A, B = sp.symbols('A B', positive=True)
sol = sp.solve([A - B - ms/R, A**2 - B**2 - (fi - fo)], [A, B], dict=True)[0]
Bexpr = sp.simplify(sol[B]); Aexpr = sp.simplify(sol[A])
V_derived = sp.simplify(fo - Bexpr**2)                  # Rdot^2 = B^2 - fo = -V
V_tree = 1 - 2*Mo/R - ((Mo - Mi)/ms - ms/(2*R))**2       # linstab.py:512-518
chk("1a tree V(R) == junction-derived V (squared Israel condition)", sp.simplify(V_derived - V_tree) == 0)
mbar, dm = (Mi + Mo)/2, Mo - Mi
V_IL = -(-1 + (dm/ms)**2 + 2*mbar/R + (ms/(2*R))**2)     # Ishak-Lake (5), eps=-1: Rdot^2 = -1 + ([m]/M)^2 + 2 mbar/R + (M/2R)^2
chk("1b tree V == Ishak-Lake eq (5) with eps = -1 (Lake 1979 identity)", sp.simplify(V_IL - V_tree) == 0)

# ---- 2. static solution, conservation law
ms0 = R*(sp.sqrt(fi) - sp.sqrt(fo))
sig0 = ms0/(4*sp.pi*R**2)
p0 = (1/(8*sp.pi*R))*((1 - Mo/R)/sp.sqrt(fo) - (1 - Mi/R)/sp.sqrt(fi))
# Lanczos p from K^tau_tau: p = (1/8pi)([K^tau_tau] + [K^theta_theta]), K^tau_tau = (Rdd + f'/2)/sqrt(f+Rd^2); static
Kt = lambda f: (sp.diff(f, R)/2)/sp.sqrt(f); Kth = lambda f: sp.sqrt(f)/R
p_lanczos = (1/(8*sp.pi))*((Kt(fo) + Kth(fo)) - (Kt(fi) + Kth(fi)))
sig_lanczos = -(1/(4*sp.pi))*(Kth(fo) - Kth(fi))
chk("2a tree sigma0 == Lanczos -[K^th_th]/4pi (PV eq 8 convention)", sp.simplify(sig0 - sig_lanczos) == 0)
chk("2b tree p0 == Lanczos ([K^t_t]+[K^th_th])/8pi (PV eq 8)", sp.simplify(p0 - p_lanczos) == 0)
chk("2c static family obeys m_s0'(R) = -8 pi R p0 identically (PV eq 13 on vacuum/vacuum)",
    sp.simplify(sp.diff(ms0, R) + 8*sp.pi*R*p0) == 0)
# conservation d(sigma A)/dtau + p dA/dtau = 0, A = 4 pi R^2  =>  (sigma R^2)' = -2 R p  <=>  m_s' = -8 pi R p  <=> sigma' = -2(sigma+p)/R
s_, p_ = sp.symbols('sigma p'); sR = sp.Function('s')(R)
cons = sp.diff(sR*R**2, R) + 2*R*p_
chk("2d conservation => sigma' = -2(sigma+p)/R (PV eq 15)",
    sp.simplify(sp.solve(cons, sp.diff(sR, R))[0] - (-2*(sR + p_)/R)) == 0)

# ---- 3. V, V', V'' along m_s(R) with p' = beta^2 sigma'
m1 = -8*sp.pi*R*p0
m2 = -8*sp.pi*p0 - 8*sp.pi*R*b2*(-2*(sig0 + p0)/R)
V1 = sp.diff(V_tree, R) + sp.diff(V_tree, ms)*m1
V2 = (sp.diff(V_tree, R, 2) + 2*sp.diff(V_tree, R, ms)*m1 + sp.diff(V_tree, ms, 2)*m1**2 + sp.diff(V_tree, ms)*m2)
sub = {ms: ms0}
# numeric spot check of V=V'=0 over several (Mi, Mo, R) incl. Mi < 0
import random
random.seed(1)
good = True
for _ in range(40):
    mi = random.uniform(-3, 0.4); mo = random.uniform(0, 0.4); r = 1.0
    vals = {Mi: mi, Mo: mo, R: r}
    if 1 - 2*mo <= 0 or 1 - 2*mi <= 0: continue
    v0 = V_tree.subs(sub).subs(vals).evalf(); v1 = V1.subs(sub).subs(vals).evalf()
    good &= abs(v0) < 1e-12 and abs(v1) < 1e-12
chk("3a static shell: V(R0) = 0 and V'(R0) = 0 (40 random (M_in, M_out), M_in down to -3)", good)

# ---- 4. device: M_in = -m, M_out = 0, R = 1, u = sqrt(1+2m)
u = sp.Symbol('u', positive=True)
dsub = {Mi: -(u**2 - 1)/2, Mo: 0, R: 1}
v2dev = sp.simplify(V2.subs(sub).subs(dsub))
v2tree = (2*b2*(3*u + 1)*u**2 + (u - 1)*(3*u**2 + 2*u + 1)/2)/u**2          # linstab.py:33-34 at R = 1
chk("4a device V''(R0) == tree closed form", sp.simplify(v2dev - v2tree) == 0)
bc = sp.solve(sp.Eq(v2dev, 0), b2)[0]
bc_tree = -(u - 1)*(3*u**2 + 2*u + 1)/(4*u**2*(3*u + 1))
chk("4b beta2_crit == tree closed form", sp.simplify(bc - bc_tree) == 0)
chk("4c coefficient of beta2 in V'' is 2(3u+1) > 0 (so stable iff beta2 > beta2_crit)",
    sp.simplify(sp.diff(v2dev, b2) - 2*(3*u + 1)) == 0)
chk("4d lim_{u->oo} beta2_crit = -1/4", sp.limit(bc_tree, u, sp.oo) == sp.Rational(-1, 4))
chk("4e lim_{u->1} beta2_crit = 0", sp.limit(bc_tree, u, 1) == 0)
Z = z3.Real('u'); zs = z3.Solver()
num = -(Z - 1)*(3*Z*Z + 2*Z + 1); den = 4*Z*Z*(3*Z + 1)
zs.add(Z > 1, z3.Not(z3.And(num < 0, num > -den)))       # beta2_crit in (-1/4, 0)  <=>  -den < num < 0
chk("4f z3: for every u > 1, -1/4 < beta2_crit < 0", zs.check() == z3.unsat)
dbc = sp.together(sp.diff(bc_tree, u)); nd, dd = sp.fraction(dbc)
print("   d beta2_crit/du numerator:", sp.factor(nd), " denominator:", sp.factor(dd))
zs2 = z3.Solver(); P = sp.Poly(sp.expand(nd), u)
zexpr = sum(int(c)*Z**int(k[0]) for k, c in P.terms())
zs2.add(Z > 1, zexpr >= 0)
Pd = sp.Poly(sp.expand(dd), u); zden = sum(int(c)*Z**int(k[0]) for k, c in Pd.terms())
zs3 = z3.Solver(); zs3.add(Z > 1, zden <= 0)
chk("4g z3: beta2_crit strictly decreasing on u > 1", zs2.check() == z3.unsat and zs3.check() == z3.unsat)
# orientation (sign) conditions lost on squaring: A = sqrt(f_in+Rd^2) > 0, B = sqrt(f_out+Rd^2) > 0 at the static shell
Bst = sp.simplify(Bexpr.subs(ms, ms0).subs(dsub)); Ast = sp.simplify(Aexpr.subs(ms, ms0).subs(dsub))
chk("4h device static shell satisfies the dropped sign conditions: B = 1 > 0, A = u > 0",
    sp.simplify(Bst - 1) == 0 and sp.simplify(Ast - u) == 0)
chk("4i device sigma0 > 0 for u > 1 (sigma0 = (u-1)/(4 pi) at R=1)", sp.simplify(sig0.subs(dsub) - (u - 1)/(4*sp.pi)) == 0)
# ordinary shell: M_in = 0, M_out = M, s = sqrt(1-2M)
s = sp.Symbol('s', positive=True)
osub = {Mi: 0, Mo: (1 - s**2)/2, R: 1}
v2o = sp.simplify(V2.subs(sub).subs(osub)); bco = sp.simplify(sp.solve(sp.Eq(v2o, 0), b2)[0])
chk("4j ordinary shell: V'' and beta2_crit are the device's with u -> s (DEVICE_IS_WALL_FORMULA_AT_U)",
    sp.simplify(v2o - v2tree.subs(u, s)) == 0 and sp.simplify(bco - bc_tree.subs(u, s)) == 0)

# ---- 5. cross-checks against PUBLISHED numbers (the machinery, not the device)
# 5a Ishak-Lake III.B: ordinary shell (m- -> 0) at P'/sigma' = 1 : R/m+ ~ 2.37
ssol = [r for r in sp.solve(sp.Eq(bc_tree.subs(u, s), 1), s) if r.is_real and 0 < r < 1]
Rm = [float(1/((1 - r**2)/2)) for r in ssol]
print("   ordinary shell, beta2 = 1 boundary: R/M_out =", Rm)
chk("5a Ishak-Lake 'R/m+ ~ 2.37 as m- -> 0' at P'/sigma' = 1 reproduced", any(abs(x - 2.37) < 0.01 for x in Rm))
# 5b Ishak-Lake III.B: m- -> m+ gives R/m+ ~ 3
q = 0.999999; import mpmath as mp
f = sp.lambdify(R, V2.subs(sub).subs({Mi: q, Mo: 1, b2: 1}), 'mpmath')
root = mp.findroot(f, 3.05)
print("   m-/m+ = %.6f, beta2 = 1 boundary: R/m+ = %s" % (q, mp.nstr(root, 8)))
chk("5b Ishak-Lake 'R/m+ ~ 3 as m- -> m+' reproduced", abs(root - 3) < 0.01)
# 5c Poisson-Visser wormhole: V = 1 - 2M/a - (2 pi sigma a)^2, sigma(a) via (15); V''(a0) against eq (27)
a, M, sg = sp.symbols('a M sigma', real=True)
Vw = 1 - 2*M/a - (2*sp.pi*sg*a)**2
sw0 = -sp.sqrt(1 - 2*M/a)/(2*sp.pi*a); pw0 = (1 - M/a)/sp.sqrt(1 - 2*M/a)/(4*sp.pi*a)
s1 = -2*(sw0 + pw0)/a
# sigma'' = 2(sigma+p)/a^2 - 2(sigma' + beta2 sigma')/a
s2 = 2*(sw0 + pw0)/a**2 - 2*(1 + b2)*s1/a
Vw1 = sp.diff(Vw, a) + sp.diff(Vw, sg)*s1
Vw2 = sp.diff(Vw, a, 2) + 2*sp.diff(Vw, a, sg)*s1 + sp.diff(Vw, sg, 2)*s1**2 + sp.diff(Vw, sg)*s2
Vw2 = Vw2.subs(sg, sw0)
pv27 = -2/a**2*(2*M/a + (M**2/a**2)/(1 - 2*M/a) + (1 + 2*b2)*(1 - 3*M/a))
chk("5c Poisson-Visser eq (27) V''(a0) re-derived", sp.simplify(Vw2 - pv27) == 0)
chk("5d Poisson-Visser V(a0)=0, V'(a0)=0", sp.simplify(Vw.subs(sg, sw0)) == 0 and sp.simplify(Vw1.subs(sg, sw0)) == 0)
x = sp.Symbol('x')  # x = M/a0
quad = sp.expand(sp.numer(sp.together(pv27.subs(M, x*a)*a**2/(-2)*(1 - 2*x))))
pv33 = 3*(1 + 4*b2)*x**2 - (3 + 10*b2)*x + 1 + 2*b2
chk("5e PV eq (33) quadratic re-derived (boundary V''=0)", sp.simplify(quad - pv33) == 0 or sp.simplify(quad + pv33) == 0)
disc = sp.discriminant(pv33, x)
chk("5f PV discriminant 4 b^4 - 12 b^2 - 3 (times const); roots 3/2 +- sqrt3", set(sp.solve(disc, b2)) == {sp.Rational(3, 2) + sp.sqrt(3), sp.Rational(3, 2) - sp.sqrt(3)})
# 5g ordinary shell against Pitre-Schneider-Poisson / LeMaitre-Poisson Gamma_1 = (4 - 6C + 2 sqrt(1-2C))/(4(1-2C)),
#    with Gamma = beta^2 (sigma + p)/p.  FORMULA AS QUOTED at research/warp-drive/wall.py:110-116 -- NOT read at
#    source in this audit (alphaXiv quota exhausted); a consistency check of the tree's machinery, not a READ.
C = sp.Symbol('C', positive=True)
so = {Mi: 0, Mo: C, R: 1}
sig_o = sig0.subs(so); p_o = p0.subs(so)
bco_C = bco.subs(s, sp.sqrt(1 - 2*C))
G1 = (4 - 6*C + 2*sp.sqrt(1 - 2*C))/(4*(1 - 2*C))
# exact: substitute C = (1 - t^2)/2 (t = s) and simplify; plus 40-digit evaluation (float64 loses it to cancellation)
tt = sp.Symbol('t', positive=True)
diffG = bco_C*(sig_o + p_o)/p_o - G1
exact0 = sp.simplify(sp.radsimp(diffG.subs(C, (1 - tt**2)/2))) == 0
worst = max(abs(sp.N(diffG.subs(C, sp.Rational(c)), 40)) for c in ['1/1000000', '1/1000', '1/100', '1/10', '1/5', '3/10', '2/5', '9/20'])
print("   beta2_crit (sigma+p)/p - Gamma_1: exact simplification zero = %s; max 40-digit residual %.1e" % (exact0, float(worst)))
chk("5g ordinary-shell beta2_crit converted to Gamma equals quoted Gamma_1 (LeMaitre-Poisson), exactly", exact0 and worst < 1e-30)
# 5h the tree's general V applied to the wormhole (normal sign flipped on one side): not the tree's case,
#    recorded only: the tree's V has eps=+1 on both sides; PV's wormhole is the other orientation.
print("\n%d/%d checks pass" % (sum(ok), len(ok)))
sys.exit(0 if all(ok) else 1)
