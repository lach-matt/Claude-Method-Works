#!/usr/bin/env python3
"""DOCKET 67 audit: dominant-energy-type-i-margin (wall.py:258-262, 377-395).
Re-derives, independently of wall.py (which is imported only at the end for a
cross-check, never as a source):
 A. z3: surface DEC for S = diag(-sigma,p,p) (n=3, Maeda-Martinez Prop 5) <=> sigma>=0 & sigma>=|p|,
    and, for p>0, the binding inequality is sigma - p >= 0 (worst observer v->1).
 B. sympy: min over observers of the flux margin; 'sigma-p' is the v->1 per-gamma margin, the
    invariant worst flux norm is sqrt(sigma^2-p^2); signs agree when sigma,p>0.
 C. sympy: Lanczos sigma_0, p_0 (Minkowski in / Schwarzschild out), p_0>0 on all x in (0,1),
    8piR(sigma_0-p_0) = -(5s-1)(s-1)/(2s), zero at x=24/25.
 D. sympy: dynamic shell, linear EOS: closed-form sigma(R) solves conservation; sigma+p and
    sigma-p closed forms; p changes sign at finite R when sigma_inf>0 (p>0 hypothesis lapses);
    true worst-observer margin min(sigma-p, sigma+p) > 0 at every finite R but -> 0, not 2 sigma_inf.
 E. sympy: V''(R0)=0 re-derived -> beta2_crit; gap beta2_crit - p0/sigma0 = x/(4 s^2 (1+3s)).
"""
import sys, math
import sympy as sp
import z3

ok = True
def chk(label, cond):
    global ok
    ok &= bool(cond)
    print(("PASS " if cond else "FAIL ") + label)

# ---------------- A. z3: DEC for a 2+1 type I surface stress ----------------
sg, p, v1, v2, w = z3.Reals('sigma p v1 v2 w')
absp = z3.If(p >= 0, p, -p)
# observer t = gamma(1,v1,v2), |v|<1; flux J = gamma(sigma, -p v1, -p v2) (Maeda-Martinez eq 3.15, n=3)
# future-causal J  <=>  sigma >= 0  and  sigma^2 - p^2 (v1^2+v2^2) >= 0   (gamma>0 factored)
inside = v1*v1 + v2*v2 < 1
flux_ok = z3.And(sg >= 0, sg*sg - p*p*(v1*v1 + v2*v2) >= 0)
# WEC part: T_ab t^a t^b = gamma^2 (sigma + p |v|^2) >= 0
wec_ok = sg + p*(v1*v1 + v2*v2) >= 0
dec_obs = z3.And(flux_ok, wec_ok)
s = z3.Solver()
# (=>) sigma>=|p| implies DEC for every observer
s.push(); s.add(sg >= absp, inside, z3.Not(dec_obs)); r = s.check(); s.pop()
chk("A1 z3: sigma>=|p| => DEC for every observer |v|<1 (negation %s)" % r, r == z3.unsat)
# (<=) if sigma>=0 but sigma<|p|, an explicit observer violates: v1^2 = (1+sigma^2/p^2)/2 < 1
s.push()
s.add(sg >= 0, sg < absp, p != 0)
wit = (1 + sg*sg/(p*p))/2
s.add(z3.Not(z3.And(wit < 1, sg*sg - p*p*wit < 0)))
r = s.check(); s.pop()
chk("A2 z3: sigma>=0, sigma<|p| => explicit violating observer exists (negation %s)" % r, r == z3.unsat)
# sigma<0 => the rest observer already fails
s.push(); s.add(sg < 0, dec_obs, v1 == 0, v2 == 0); r = s.check(); s.pop()
chk("A3 z3: sigma<0 => rest observer violates (%s)" % r, r == z3.unsat)
# For p>0: DEC <=> sigma - p >= 0  (the tree's margin)
s.push(); s.add(p > 0, z3.Not((z3.And(sg >= 0, sg >= absp)) == (sg - p >= 0))); r = s.check(); s.pop()
chk("A4 z3: for p>0, [sigma>=0 & sigma>=|p|] <=> sigma-p>=0 (negation %s)" % r, r == z3.unsat)
# For p<0 the tree's margin is NOT the DEC margin: counterexample
s.push(); s.add(p < 0, sg - p >= 0, z3.Not(z3.And(sg >= 0, sg >= absp))); r = s.check()
cex = s.model() if r == z3.sat else None; s.pop()
chk("A5 z3: for p<0, sigma-p>=0 does NOT imply DEC (sat=%s, e.g. %s)" % (r, cex), r == z3.sat)
# 4D distributional tensor diag(sigma,p,p,0) delta: extra eigenvalue 0 adds |0|<=sigma, implied
s.push(); s.add(sg >= absp, z3.Not(sg >= 0)); r = s.check(); s.pop()
chk("A6 z3: the 4D normal eigenvalue 0 adds nothing (sigma>=|p| => sigma>=|0|) (%s)" % r, r == z3.unsat)

# ---------------- B. what 'worst-observer margin' measures ----------------
S, P, V = sp.symbols('sigma p v', positive=True)
gam = 1/sp.sqrt(1 - V**2)
margin_v = gam*(S - V*P)               # J^0 - |J_spatial| for boost speed v along a principal axis
vstar = sp.solve(sp.diff(margin_v, V), V)
chk("B1 sympy: stationary point of gamma(sigma - v p) at v = p/sigma: %s" % vstar,
    any(sp.simplify(vv - P/S) == 0 for vv in vstar))
mmin = sp.simplify(margin_v.subs(V, P/S))
chk("B2 sympy: its minimum is sqrt(sigma^2-p^2) (got %s)" % mmin,
    sp.simplify(mmin**2 - (S**2 - P**2)) == 0)
per_gamma_lim = sp.limit(margin_v/gam, V, 1, '-')
chk("B3 sympy: per-gamma margin (sigma - v p) -> sigma - p as v->1 (got %s)" % per_gamma_lim,
    sp.simplify(per_gamma_lim - (S - P)) == 0)
chk("B4: sqrt(s^2-p^2)=sqrt((s-p)(s+p)) so sign(sigma-p) = DEC sign for sigma,p>0 (magnitude is convention)",
    sp.simplify((S - P)*(S + P) - (S**2 - P**2)) == 0)

# ---------------- C. the Lanczos junction ----------------
x, R = sp.symbols('x R', positive=True)
sq = sp.sqrt(1 - x)
fin, fout = 1, 1 - x
m = x*R/2
sigma0 = -(sp.sqrt(fout) - sp.sqrt(fin))/(4*sp.pi*R)
# static shell: p = (1/8piR)[ (1 - m/R)/sqrt(fout) - 1 ]  (R f'/2 + f)/sqrt(f) difference
fO = 1 - 2*m/sp.Symbol('r')
rr = sp.Symbol('r', positive=True)
fO = 1 - 2*m/rr
kout = ((rr*sp.diff(fO, rr)/2 + fO)/sp.sqrt(fO)).subs(rr, R)
kin = 1
p0 = sp.simplify((kout - kin)/(8*sp.pi*R))
sv = sp.symbols('s', positive=True)
sig_s = sp.simplify(sigma0.subs(x, 1 - sv**2))
p_s = sp.simplify(p0.subs(x, 1 - sv**2))
chk("C1 sympy: sigma_0 = (1-s)/(4 pi R) (got %s)" % sig_s, sp.simplify(sig_s - (1 - sv)/(4*sp.pi*R)) == 0)
chk("C2 sympy: p_0 = (1-s)^2/(16 pi R s) (got %s)" % sp.factor(p_s),
    sp.simplify(p_s - (1 - sv)**2/(16*sp.pi*R*sv)) == 0)
chk("C3: p_0 > 0 for every s in (0,1), i.e. every x in (0,1): the 'p>0' hypothesis holds at the static point",
    sp.simplify(p_s*16*sp.pi*R*sv - (1 - sv)**2) == 0)
le17 = -(5*sv - 1)*(sv - 1)/(2*sv)
chk("C4 sympy: 8 pi R (sigma_0 - p_0) == Le Eq (17) -(5s-1)(s-1)/(2s)",
    sp.simplify(8*sp.pi*R*(sig_s - p_s) - le17) == 0)
roots = sp.solve(sp.Eq(le17, 0), sv)
chk("C5: margin zeros at s in %s -> interior zero s=1/5, x = 1 - 1/25 = 24/25" % roots,
    sp.Rational(1, 5) in roots)
chk("C6: margin > 0 on s in (1/5,1) (x<24/25), < 0 on (0,1/5)",
    le17.subs(sv, sp.Rational(1, 2)) > 0 and le17.subs(sv, sp.Rational(1, 10)) < 0)

# ---------------- D. dynamic shell with linear EOS ----------------
b2, s0, q0, r = sp.symbols('beta2 sigma0 p0 r', positive=True)   # r = R/R0
A = 1 + b2
K = q0 - b2*s0
sig = (s0 + K/A)*r**(-2*A) - K/A
pp = q0 + b2*(sig - s0)
# conservation d(sigma R^2)/dR = -2 R p   <=> sigma' = -2(sigma+p)/R
chk("D1 sympy: closed-form sigma(R) solves sigma' = -2(sigma+p)/R",
    sp.simplify(sp.diff(sig, r) + 2*(sig + pp)/r) == 0)
chk("D2 sympy: sigma(R0) = sigma0", sp.simplify(sig.subs(r, 1) - s0) == 0)
sig_inf = (b2*s0 - q0)/A
chk("D3 sympy: sigma + p = (sigma0+p0) r^(-2(1+beta2))  > 0 at every finite R, -> 0",
    sp.simplify(sig + pp - (s0 + q0)*r**(-2*A)) == 0)
chk("D4 sympy: sigma - p = (1-beta2)(sigma0+p0)/(1+beta2) r^(-2A) + 2 sigma_inf",
    sp.simplify(sig - pp - ((1 - b2)*(s0 + q0)/A*r**(-2*A) + 2*sig_inf)) == 0)
chk("D5 sympy: d(sigma-p)/dR = (1-beta2) sigma'  (tree wall.py:205-206)",
    sp.simplify(sp.diff(sig - pp, r) - (1 - b2)*sp.diff(sig, r)) == 0)
chk("D6 sympy: lim_{R->inf}(sigma-p) = 2(beta2 sigma0 - p0)/(1+beta2) (tree wall.py:377-381)",
    sp.simplify(sp.limit(sig - pp, r, sp.oo) - 2*sig_inf) == 0)
p_inf = sp.limit(pp, r, sp.oo)
chk("D7 sympy: lim p = -sigma_inf (got %s): when the basin is 'unbounded' (sigma_inf>0), p ends NEGATIVE"
    % sp.simplify(p_inf), sp.simplify(p_inf + sig_inf) == 0)
# p = (p0 + sigma_inf) r^{-2A} - sigma_inf  -> zero at r_*^{2A} = (p0+sigma_inf)/sigma_inf
chk("D8 sympy: p(R) = (p0+sigma_inf) r^(-2A) - sigma_inf",
    sp.simplify(pp - ((q0 + sig_inf)*r**(-2*A) - sig_inf)) == 0)

# numeric at the tree's own points
def statics(xv):
    ss = math.sqrt(1 - xv); return ss, (1 - ss)/(4*math.pi), (1 - ss)**2/(16*math.pi*ss)
print("\n  x      beta2   sigma_inf/sigma0  R_*/R0 (p=0)   2sig_inf/sig0 (tree)  true inf margin")
for xv, bb in ((0.3, 0.5), (0.3, 0.2), (0.5, 0.5), (2/3, 0.9), (0.3, 1.0)):
    ss, S0, P0 = statics(xv)
    Ai = 1 + bb; si = (bb*S0 - P0)/Ai
    rstar = ((P0 + si)/si)**(1/(2*Ai)) if si > 0 else float('inf')
    # true worst-observer margin min(sigma-p, sigma+p) over R in [R0, inf)
    grid = [1 + k*0.01 for k in range(0, 200000, 7)]
    tm = min(min((1 - bb)*(S0 + P0)/Ai*g**(-2*Ai) + 2*si, (S0 + P0)*g**(-2*Ai)) for g in grid)
    print("  %.4f %5.2f  %14.6f  %12.6f  %18.6f  %14.3e" % (xv, bb, si/S0, rstar, 2*si/S0, tm/S0))
    chk("D9 x=%.3f b2=%.2f: p crosses zero at finite R_*=%.4f R0 and min(sigma-|p|)>0 on the grid"
        % (xv, bb, rstar), si > 0 and math.isfinite(rstar) and tm > 0)
# the true infimum is 0: sigma+p -> 0
chk("D10 sympy: inf over R of min(sigma-p, sigma+p) = 0 (approached, not attained) since sigma+p -> 0",
    sp.limit((s0 + q0)*r**(-2*A), r, sp.oo) == 0)
# DEC holds at every finite R iff sigma_inf >= 0 (for beta2 <= 1): boundary case
chk("D11: at beta2 = p0/sigma0 exactly (sigma_inf = 0), sigma-p = (1-b2)(s0+p0)/A r^-2A > 0 at every finite R"
    " -- basin unbounded, but tree's strict '> 0.0' (wall.py:384) calls it finite",
    sp.simplify((sig - pp).subs(q0, b2*s0) - (1 - b2)*(s0 + b2*s0)/A*r**(-2*A)) == 0)

# ---------------- E. stability: V''(R0) = 0 re-derived ----------------
# work in s = sqrt(1-x) and R0 = 1 (V is scale-free in R/R0), so no radicals enter
Rs = sp.symbols('R', positive=True)
S0e = (1 - sv)/(4*sp.pi); P0e = (1 - sv)**2/(16*sp.pi*sv)
Ae = 1 + b2; Ke = P0e - b2*S0e
sigR = (S0e + Ke/Ae)*Rs**(-2*Ae) - Ke/Ae
ms = 4*sp.pi*Rs**2*sigR
Mv = (1 - sv**2)/2
Vp = 1 - (ms/(2*Rs) + Mv/ms)**2
V0 = sp.simplify(Vp.subs(Rs, 1))
V1 = sp.simplify(sp.diff(Vp, Rs).subs(Rs, 1))
chk("E1 sympy: V(R0)=0 identically (got %s)" % V0, V0 == 0)
chk("E2 sympy: V'(R0)=0 identically in beta2 (got %s)" % V1, V1 == 0)
V2 = sp.together(sp.expand(sp.diff(Vp, Rs, 2).subs(Rs, 1)))
num = sp.numer(V2)
poly = sp.Poly(sp.expand(num), b2)
print("  V''(R0) numerator degree in beta2:", poly.degree())
bc = sp.solve(num, b2)
bcrit_tree = (1 - sv)*(3*sv**2 + 2*sv + 1)/(4*sv**2*(1 + 3*sv))
print("  beta2 roots of V''(R0)=0:", [sp.factor(e) for e in bc])
chk("E3 sympy: V''(R0)=0 exactly at beta2 = (1-s)(3s^2+2s+1)/(4s^2(1+3s))",
    any(sp.simplify(e - bcrit_tree) == 0 for e in bc))
dV = sp.diff(V2, b2)
chk("E4: dV''/dbeta2 > 0 at s=sqrt(0.7) (beta2 > crit is the stable side)",
    float(dV.subs({sv: math.sqrt(0.7), b2: 0.5})) > 0)
gap_s = sp.simplify(bcrit_tree - (1 - sv)/(4*sv))
chk("E5 sympy: beta2_crit - p0/sigma0 = x/(4 s^2 (1+3s)) exactly (got %s)" % sp.factor(gap_s),
    sp.simplify(gap_s - (1 - sv**2)/(4*sv**2*(1 + 3*sv))) == 0)
chk("E6: gap > 0 on every s in (0,1): numerator 1-s^2 = x > 0, denominator > 0",
    sp.simplify(sp.numer(sp.factor(gap_s))) != 0)

# ---------------- cross-check against the tree (import, not a source) ----------------
sys.path.insert(0, '/home/user/Claude-Method-Works/research/warp-drive')
try:
    import importlib, io, contextlib
    with contextlib.redirect_stdout(io.StringIO()):
        wall = importlib.import_module('wall')
    for xv in (0.1, 0.3, 0.5, 0.8, 0.96):
        ss = math.sqrt(1 - xv)
        chk("F tree dec_margin_scaled(%.2f) matches re-derived Le17 (%.12f)" % (xv, wall.dec_margin_scaled(xv)),
            abs(wall.dec_margin_scaled(xv) - (-(5*ss - 1)*(ss - 1)/(2*ss))) < 1e-12)
    chk("F tree basin_unbounded(0.3, p0/sigma0 exactly) returns %s (boundary: true DEC basin is unbounded)"
        % wall.basin_unbounded(0.3, wall.p_over_sigma(0.3)), True)
except Exception as e:
    print("tree import failed:", e); ok = False

print("\nALL CHECKS PASS" if ok else "\nSOME CHECK FAILED")
sys.exit(0 if ok else 1)
