#!/usr/bin/env python3
"""
DOCKET 67 -- re-derivation for gr-qc/9506083 (Poisson & Visser, "Thin-shell
wormholes: Linearization stability", PRD 52, 7318 (1995)) AS THE TREE USES IT
(research/warp-drive/stability.py and wall.py).

Nothing here imports the tree.  The tree's printed numbers are copied in as
literals (with file:line) and compared against an independent sympy derivation.

Blocks
  A  junction algebra: the two-mass potential, and its three reductions
     (tree general form = Ishak-Lake eq (5) with mean mass; wall.py's
     Minkowski-inside form; PV eq (17) for the symmetric wormhole)
  B  PV eqs (11),(12) imply the conservation law (13)/(15); m_s' = -8 pi R p
  C  PV's own results: eq (27), (29)-(36): discriminant roots 3/2 +- sqrt3,
     region II boundary -1/2 as a0 -> infinity, min of region-I boundary
  D  general V''(R0) for any (M_in, M_out, beta^2); V = V' = 0 identically;
     wall.py closed forms (beta2_crit, (sqrt3-1)/2, sqrt5-3/2, x*, 0.07933);
     independent cross-check against Pitre-Schneider-Poisson 2026 eq (3.16)
  E  the device (M_in = -m, M_out = 0): stability.py's printed V'' and
     beta2_crit, exact; sign of beta2_crit for all m > 0 (z3)
  F  orientation signs lost on squaring: checked at the static solutions
"""
import sys
import sympy as sp

ok = True
def chk(label, cond):
    global ok
    ok = ok and bool(cond)
    print(("  PASS " if cond else "  FAIL ") + label)

R, a, Mi, Mo, ms, Rd, m, M = sp.symbols('R a M_in M_out m_s Rdot m M', real=True)
b2 = sp.symbols('beta2', real=True)

# ---------------------------------------------------------------- A
print("A. junction algebra")
# Israel for a static-exterior spherical shell with outward normal on both
# sides: A - B = m_s/R, A = sqrt(f_in + Rdot^2), B = sqrt(f_out + Rdot^2),
# f = 1 - 2M/R, m_s = 4 pi R^2 sigma.
# A^2 - B^2 = 2 dM / R  =>  A + B = 2 dM / m_s  =>  B = dM/m_s - m_s/(2R)
dM = Mo - Mi
B = dM/ms - ms/(2*R)
A_ = dM/ms + ms/(2*R)
chk("A - B = m_s/R", sp.simplify(A_ - B - ms/R) == 0)
chk("A^2 - B^2 = f_in - f_out", sp.simplify(A_**2 - B**2 - ((1-2*Mi/R) - (1-2*Mo/R))) == 0)
V_tree = 1 - 2*Mo/R - (dM/ms - ms/(2*R))**2          # stability.py:40, :158-160
Rdot2 = B**2 - (1 - 2*Mo/R)
chk("Rdot^2 = B^2 - f_out gives exactly the tree's V (stability.py:40)",
    sp.simplify(-Rdot2 - V_tree) == 0)
# Ishak-Lake gr-qc/0108058 eq (5), eps = -1: Rdot^2 = -1 + ([m]/M)^2 + 2 mbar/R + (M/2R)^2
mbar = (Mi + Mo)/2
V_IL = 1 - (dM/ms)**2 - 2*mbar/R - (ms/(2*R))**2
chk("tree V == Ishak-Lake eq (5) with mbar = (M_in+M_out)/2", sp.simplify(V_tree - V_IL) == 0)
V_IL_plus = 1 - (dM/ms)**2 - 2*Mo/R - (ms/(2*R))**2
chk("  (and NOT with m = M_out: differs by dM/R)",
    sp.simplify(V_tree - V_IL_plus - dM/R) == 0)
V_wall = 1 - (ms/(2*R) + M/ms)**2                     # wall.py:224-225, :327-330
chk("M_in = 0, M_out = M reduces to wall.py's V = 1 - [m_s/2R + M/m_s]^2",
    sp.simplify(V_tree.subs({Mi: 0, Mo: M}) - V_wall) == 0)
# PV wormhole: sigma = -(1/2 pi a) sqrt(1 - 2M/a + adot^2)   (PV eq 11)
sig = sp.symbols('sigma', real=True)
V_PV = 1 - 2*M/a - (2*sp.pi*sig*a)**2                 # PV eq (17)
adot2 = (2*sp.pi*sig*a)**2 - (1 - 2*M/a)             # squaring PV eq (11)
chk("PV eq (11) squared gives PV eq (17)", sp.simplify(-adot2 - V_PV) == 0)
print("  NOTE: the two-mass V (M_in != M_out) is NOT in PV; PV treat only the")
print("        symmetric wormhole, M equal on both sides (their eq 1, 17).")

# ---------------------------------------------------------------- B
print("B. conservation")
t = sp.symbols('tau')
af = sp.Function('a')(t)
f = 1 - 2*M/af
ad = sp.diff(af, t); add = sp.diff(af, t, 2)
sig11 = -1/(2*sp.pi*af)*sp.sqrt(f + ad**2)                           # PV (11)
p12 = 1/(4*sp.pi*af)*(1 - M/af + ad**2 + af*add)/sp.sqrt(f + ad**2)  # PV (12)
A4 = 4*sp.pi*af**2
cons = sp.diff(sig11*A4, t) + p12*sp.diff(A4, t)                      # PV (13)
chk("PV (11),(12) => (13) d(sigma A)/dtau + p dA/dtau = 0", sp.simplify(cons) == 0)
chk("PV (15) sigma_dot = -2(sigma+p) adot/a", sp.simplify(sp.diff(sig11, t) + 2*(sig11+p12)*ad/af) == 0)
# m_s = 4 pi R^2 sigma, sigma' = -(2/R)(sigma + p)  =>  m_s' = -8 pi R p
p_ = sp.symbols('p', real=True)
sigp = -(2/R)*(sig + p_)
msp = sp.diff(4*sp.pi*R**2*sig, R) + 4*sp.pi*R**2*sigp
chk("m_s' = -8 pi R p (stability.py:163, wall.py:223)", sp.simplify(msp + 8*sp.pi*R*p_) == 0)

# ---------------------------------------------------------------- C
print("C. PV's own results")
u = sp.symbols('u', positive=True)   # u = M/a0
s0 = -1/(2*sp.pi*a)*sp.sqrt(1 - 2*M/a)          # (18)
p0 = 1/(4*sp.pi*a)*(1 - M/a)/sp.sqrt(1 - 2*M/a)  # (19)
# (26): V'' = -4M/a^3 - 8 pi^2 [ (sigma+2p)^2 + 2 sigma (1+2 b2)(sigma+p) ]
V2_26 = -4*M/a**3 - 8*sp.pi**2*((s0 + 2*p0)**2 + 2*s0*(1 + 2*b2)*(s0 + p0))
V2_27 = -2/a**2*(2*M/a + (M**2/a**2)/(1 - 2*M/a) + (1 + 2*b2)*(1 - 3*M/a))
chk("PV (26) at (18),(19) equals PV (27)", sp.simplify(V2_26 - V2_27) == 0)
# independent: V(a) = 1 - 2M/a - (2 pi sigma(a) a)^2 with (sigma a)' = -(sigma+2p), p' = b2 sigma'
S0, S1, S2 = sp.symbols('S0 S1 S2')  # sigma(a0), sigma'(a0), sigma''(a0)
P0 = p0
sig_a = sp.Function('s')(a)
Vf = 1 - 2*M/a - (2*sp.pi*sig_a*a)**2
V2gen = sp.diff(Vf, a, 2)
S1v = -2*(s0 + P0)/a                        # (15) in a
S2v = sp.diff(-2*(sig + p_)/a, a).subs({sig: s0, p_: P0}) \
      + (-2/a)*(S1v + b2*S1v)               # d/da of -2(sigma+p)/a, p' = b2 sigma'
# careful: -2(sigma+p)/a differentiated: 2(sigma+p)/a^2 - (2/a)(sigma'+p')
S2v = 2*(s0 + P0)/a**2 - (2/a)*(1 + b2)*S1v
V2ind = V2gen.subs(sp.Derivative(sig_a, (a, 2)), S2v).subs(sp.Derivative(sig_a, a), S1v).subs(sig_a, s0)
chk("independent V''(a0) from V(a) and (15) equals PV (27)", sp.simplify(V2ind - V2_27) == 0)
V1ind = sp.diff(Vf, a).subs(sp.Derivative(sig_a, a), S1v).subs(sig_a, s0)
chk("V'(a0) = 0 at (18),(19)", sp.simplify(V1ind) == 0)
chk("V(a0) = 0 at (18),(19)", sp.simplify(Vf.subs(sig_a, s0)) == 0)
# (33),(34)
b = sp.symbols('b', real=True)
q33 = 3*(1 + 4*b)*u**2 - (3 + 10*b)*u + 1 + 2*b
V27u = sp.simplify((V2_27*a**2).subs(M, u*a))
num27 = sp.factor(sp.numer(sp.together(V27u))).subs(b2, b)
den27 = sp.factor(sp.denom(sp.together(V27u)))
print("    V''(a0) a0^2 = -(%s)/(%s)" % (num27, den27))
chk("V''=0 boundary is PV (33): numerator of V'' a0^2 == 2 x (33) (exact)",
    sp.simplify(num27 - 2*q33) == 0 or sp.simplify(num27 + 2*q33) == 0)
disc = sp.expand((3 + 10*b)**2 - 12*(1 + 4*b)*(1 + 2*b))
chk("discriminant of (33) = 4 b^2 - 12 b - 3 ... times 1 (PV 34)",
    sp.simplify(disc - (4*b**2 - 12*b - 3)) == 0)
rts = sp.solve(4*b**2 - 12*b - 3, b)
chk("roots 3/2 -+ sqrt3 (PV text after 34)",
    set(sp.nsimplify(r) for r in rts) == {sp.Rational(3, 2) - sp.sqrt(3), sp.Rational(3, 2) + sp.sqrt(3)})
bound = -(1 - 3*u + 3*u**2)/(2*(1 - 2*u)*(1 - 3*u))    # (31)/(32) RHS
chk("(31) RHS -> -1/2 as a0 -> infinity (u -> 0)", sp.limit(bound, u, 0) == sp.Rational(-1, 2))
db = sp.diff(bound, u)
crit = [c for c in sp.solve(sp.numer(sp.together(db)), u) if c.is_real and sp.Rational(1, 3) < c < sp.Rational(1, 2)]
chk("region-I boundary minimum on 1/3<u<1/2 is 3/2+sqrt3",
    len(crit) == 1 and sp.simplify(bound.subs(u, crit[0]) - (sp.Rational(3, 2) + sp.sqrt(3))) == 0)
# region II: for u in (0,1/3) is bound < -1/2 strictly?
chk("for 0<u<1/3 the (31) RHS is < -1/2 (bound decreasing), so region II is beta^2 < -1/2",
    all(bound.subs(u, sp.Rational(k, 300)) < sp.Rational(-1, 2) for k in range(1, 100)))
print("  NOTE: PV (36) prints 'beta0^2 <= -1/2'; at exactly -1/2 no finite a0 is stable")
print("        (the boundary -1/2 is reached only as a0 -> infinity).  Boundary nicety,")
print("        a discrepancy of '<=' vs '<', not a refutation.")
print("  NOTE: PV sec IV writes the Casimir slope as 'beta^2 = d sigma/d p = -1'; for")
print("        p = -sigma, dp/dsigma = dsigma/dp = -1, so the value is unaffected.")

# ---------------------------------------------------------------- D
print("D. general V''(R0) and wall.py's closed forms")
# static: A0 = sqrt(f_in), B0 = sqrt(f_out); m_s0 = R (A0 - B0)
R0 = sp.symbols('R0', positive=True)
fin = 1 - 2*Mi/R0; fout = 1 - 2*Mo/R0
ms0 = R0*(sp.sqrt(fin) - sp.sqrt(fout))
sig0 = ms0/(4*sp.pi*R0**2)
# p from Lanczos: p = (1/8pi)([K_tt] + [K_thth]), K_tt = f'/(2 sqrt f), K_thth = sqrt f / R, [X] = out - in
# with sigma = -(1/4pi)[K_thth] (PV eq 8 structure, orientation r increasing outward)
Kt = lambda F, Mx: (2*Mx/R0**2)/(2*sp.sqrt(F))
Kth = lambda F: sp.sqrt(F)/R0
sig_L = -(Kth(fout) - Kth(fin))/(4*sp.pi)
p_L = ((Kt(fout, Mo) - Kt(fin, Mi)) + (Kth(fout) - Kth(fin)))/(8*sp.pi)
chk("Lanczos sigma == m_s0/(4 pi R0^2)", sp.simplify(sig_L - sig0) == 0)
msR = sp.Function('mu')(R)
VR = 1 - 2*Mo/R - (dM/msR - msR/(2*R))**2
# derivatives of m_s at R0: m_s' = -8 pi R p ; p' = b2 sigma' ; sigma = m_s/(4 pi R^2)
m1 = -8*sp.pi*R0*p_L
sig1 = (m1*R0**2 - 2*R0*ms0)/(4*sp.pi*R0**4)
m2 = -8*sp.pi*p_L - 8*sp.pi*R0*b2*sig1
def at0(expr):
    e = expr.subs(sp.Derivative(msR, (R, 2)), m2).subs(sp.Derivative(msR, R), m1).subs(msR, ms0)
    return e.subs(R, R0)
V0 = at0(VR); V1 = at0(sp.diff(VR, R)); V2 = at0(sp.diff(VR, R, 2))
# numeric identity checks over a grid (sympy simplify of nested roots is slow)
import random
random.seed(1)
okV = True
for (mi, mo, bb) in [(0, 0.15, 0.3), (-0.2, 0, 0.0), (-0.05, 0.1, 1.7), (0.1, 0.3, -0.4), (-1, 0, 2)]:
    sub = {Mi: mi, Mo: mo, R0: 1, b2: bb}
    okV &= abs(float(V0.subs(sub))) < 1e-13 and abs(float(V1.subs(sub))) < 1e-12
chk("V(R0) = V'(R0) = 0 identically in beta^2 (five (M_in,M_out,beta^2) points)", okV)
# wall.py: M_in = 0, M_out = x R/2
x = sp.symbols('x', positive=True)
s = sp.sqrt(1 - x)
V2w = sp.simplify(V2.subs({Mi: 0, Mo: x/2, R0: 1}))
wall_Vpp = -2*((1 - s)/2 - b2*(1 + 3*s) + (1 - s)*(1 + s)**2/(4*s**2))   # wall.py:302-307
chk("independent V'' == wall.py Vpp closed form (x = 0.1..0.9, beta^2 in -1..2)",
    all(abs(sp.N((V2w - wall_Vpp).subs({x: sp.Rational(xx), b2: sp.Rational(bb)}), 50)) < 1e-40
        for xx in ('1/10', '3/10', '1/2', '7/10', '9/10') for bb in ('-1', '0', '1/2', '2')))
chk("  and symbolically: V''_indep - wall.Vpp simplifies to 0",
    sp.simplify(sp.radsimp(V2w - wall_Vpp)) == 0)
b2c = sp.solve(sp.Eq(wall_Vpp, 0), b2)[0]
wall_b2c = (1 - s)*(3*s**2 + 2*s + 1)/(4*s**2*(1 + 3*s))              # wall.py:28, :268-272
chk("beta2_crit(x) == wall.py closed form", sp.simplify(b2c - wall_b2c) == 0)
chk("beta2_crit(2/3) = (sqrt3-1)/2 exactly", sp.simplify(wall_b2c.subs(x, sp.Rational(2, 3)) - (sp.sqrt(3) - 1)/2) == 0)
chk("beta2_crit(4/5) = sqrt5 - 3/2 exactly", sp.simplify(wall_b2c.subs(x, sp.Rational(4, 5)) - (sp.sqrt(5) - sp.Rational(3, 2))) == 0)
v03 = float(wall_b2c.subs(x, sp.Rational(3, 10)))
print("    beta2_crit(0.3) = %.6f  (wall.py:30 prints 0.07933)" % v03)
chk("beta2_crit(0.3) rounds to 0.07933", round(v03, 5) == 0.07933)
sv = sp.symbols('sv', positive=True)
eq1 = sp.factor(sp.numer(sp.together((wall_b2c - 1).subs(x, 1 - sv**2))))
print("    beta2_crit = 1  <=>", eq1, "= 0")
chk("beta2_crit = 1 reduces to 15 s^3 + 3 s^2 - s - 1 = 0 (wall.py:38)",
    sp.simplify(sp.Poly(eq1, sv).monic() - sp.Poly(15*sv**3 + 3*sv**2 - sv - 1, sv).monic()) == 0)
rr = [r for r in sp.Poly(15*sv**3 + 3*sv**2 - sv - 1, sv).nroots(n=30) if r.is_real and 0 < r < 1]
xstar = 1 - rr[0]**2
print("    x* = %.12f  (wall.py:40 prints 0.84374189, :548 0.8437418926)" % xstar)
chk("x* = 0.8437418926 to 1e-10", abs(float(xstar) - 0.8437418926) < 1e-10)
# PSP 2026 (arXiv:2604.05980v1) eq (3.16b): Gamma_1 = (1 + 2 sqrt F + 3F)/(4F), F = 1 - 2M/R = s^2,
# with dp = Gamma (p/sigma_rest) d sigma_rest and d mu = ((mu+p)/sigma_rest) d sigma_rest,
# so dp/dmu = Gamma p/(mu+p).  Turning point of M = onset of radial instability (their ref [34]).
mu0 = (1 - s)/(4*sp.pi)                    # PSP (3.11), R = 1
pp0 = (1/s - 1 + (x/2)/s)/(8*sp.pi)        # PSP (3.12): (F^1/2 - 1 + (M/R) F^-1/2)/(8 pi R)... sign form
pp0 = (s - 1 + (x/2)/s)/(8*sp.pi)
G1 = (1 + 2*s + 3*s**2)/(4*s**2)
chk("PSP (3.12) pressure == Lanczos p0 of the tree (wall.py statics)",
    sp.simplify(pp0 - (1 - s)**2/(16*sp.pi*s)) == 0)
chk("PSP 2026 Gamma_1 * p/(mu+p) == wall.py beta2_crit (independent 2026 source)",
    sp.simplify(G1*pp0/(mu0 + pp0) - wall_b2c) == 0)

# ---------------------------------------------------------------- E
print("E. the device: M_in = -m, M_out = 0 (stability.py)")
mm = sp.symbols('mm', positive=True)
V2d = V2.subs({Mi: -mm, Mo: 0, R0: 1})
V2o = V2.subs({Mi: 0, Mo: mm, R0: 1})
tree_dev = {0.01: 2.965e-2, 0.10: 2.700e-1, 0.50: 1.018e0}          # stability.py:54-57
tree_ord = {0.01: -3.036e-2, 0.10: -3.424e-1, 0.20: -8.169e-1}     # stability.py:47-50
for k, v in tree_dev.items():
    e = float(V2d.subs({mm: k, b2: 0}))
    print("    device   m/R = %.2f  V''(0) exact %+.6e   tree %+.3e" % (k, e, v))
    chk("    agrees to the printed 4 sig figs", abs(e - v) <= 0.0006*abs(v) + 1e-12)
for k, v in tree_ord.items():
    e = float(V2o.subs({mm: k, b2: 0}))
    print("    ordinary M/R = %.2f  V''(0) exact %+.6e   tree %+.3e" % (k, e, v))
    chk("    agrees to the printed 4 sig figs", abs(e - v) <= 0.0006*abs(v) + 1e-12)
b2d = sp.simplify(sp.solve(sp.Eq(V2d, 0), b2)[0])
print("    device beta2_crit(m) =", b2d)
for k, v in ((0.01, -0.0037), (1.0, -0.132)):
    e = float(b2d.subs(mm, k))
    print("    device beta2_crit(%.2f) exact %+.6f   tree %+.4f (stability.py:63)" % (k, e, v))
    chk("    agrees at printed precision", abs(e - v) < 0.00051 if k == 0.01 else abs(e - v) < 0.0006)
aa = float(V2o.subs({mm: 0.01, b2: 0})); bb_ = float(V2d.subs({mm: 0.01, b2: 0}))
rel = (aa + bb_)/abs(aa)
print("    (V''ord + V''dev)/|V''ord| at 0.01 = %+.5f (selftest tolerance 0.03)" % rel)
chk("    within 0.03 (stability.py:263-264); 'NEARLY mirror', not exact", abs(rel) < 0.03 and abs(rel) > 1e-3)
for k in (0.1, 0.5):
    print("    at %.2f: ordinary %+.4e, device %+.4e -> ratio %.3f (mirror loosens with compactness)"
          % (k, float(V2o.subs({mm: k, b2: 0})), float(V2d.subs({mm: k, b2: 0})),
             -float(V2d.subs({mm: k, b2: 0}))/float(V2o.subs({mm: k, b2: 0}))) if k < 0.5 else
          "    at 0.50 the ordinary shell has x = 1 (horizon); no mirror comparison possible")
# sign of beta2_crit for all m > 0: substitute w = sqrt(1+2m), w > 1
w = sp.symbols('w', positive=True)
b2w = sp.simplify(b2d.subs(mm, (w**2 - 1)/2))
print("    in w = sqrt(1+2m/R): beta2_crit =", sp.factor(b2w))
try:
    import z3
    W = z3.Real('W')
    num, den = sp.fraction(sp.factor(b2w))
    zexpr = lambda e: eval(str(e).replace('w', 'W'))
    sol = z3.Solver()
    sol.add(W > 1, zexpr(num)/zexpr(den) >= 0)
    r1 = sol.check()
    sol2 = z3.Solver(); sol2.add(W > 1, zexpr(num)/zexpr(den) <= sp.Rational(-1, 4).__float__())
    r2 = sol2.check()
    # vacuity guard: the constraint set is satisfiable without the claim
    sol3 = z3.Solver(); sol3.add(W > 1); r3 = sol3.check()
    print("    z3: exists w>1 with beta2_crit >= 0 ?", r1, "; with beta2_crit <= -1/4 ?", r2, "; vacuity guard W>1 sat?", r3)
    chk("z3: -1/4 < beta2_crit(device) < 0 for EVERY m/R > 0", str(r1) == 'unsat' and str(r2) == 'unsat' and str(r3) == 'sat')
except ImportError:
    print("    z3 not available; sign checked on a grid only")
    chk("beta2_crit < 0 on grid", all(float(b2d.subs(mm, k)) < 0 for k in (1e-4, 0.01, 0.1, 1, 10, 1e3)))

# ---------------------------------------------------------------- F
print("F. orientation signs lost on squaring (not stated in PV's V)")
for (mi, mo, lab) in ((-0.01, 0, 'device m=0.01'), (-1, 0, 'device m=1'), (0, 0.1, 'ordinary M=0.1')):
    Aval = float((dM/ms + ms/(2*R)).subs({Mi: mi, Mo: mo, ms: ms0.subs({Mi: mi, Mo: mo, R0: 1}), R: 1}))
    Bval = float((dM/ms - ms/(2*R)).subs({Mi: mi, Mo: mo, ms: ms0.subs({Mi: mi, Mo: mo, R0: 1}), R: 1}))
    chk("%s: A = sqrt(f_in) = %.6f > 0 and B = sqrt(f_out) = %.6f > 0" % (lab, Aval, Bval), Aval > 0 and Bval > 0)


# ---------------------------------------------------------------- G (appended)
# PV's criterion is LINEAR ("at this order of approximation", PV eq 28; "perturbations
# can grow (at least until the nonlinear regime is reached)").  stability.py's verdict
# (stability.py:11-13, 255-258) says "RADIALLY STABLE" without "linearly".  Measure the
# finite-amplitude well for the device at beta^2 = 0: p = p0 fixed, so
# m_s(R) = m_s0 - 4 pi p0 (R^2 - R0^2) exactly, and V(R) is closed form.
import math
print("G. finite-amplitude well of the device at beta^2 = 0 (beyond PV's linear scope)")
def Vdev(Rr, mv):
    fin = math.sqrt(1 + 2*mv); ms0v = fin - 1.0                   # R0 = 1, M_out = 0
    p0v = ((0 - (-mv)/fin) + (1 - fin))/(8*math.pi)               # Lanczos, R0 = 1
    msv = ms0v - 4*math.pi*p0v*(Rr**2 - 1)
    dMv = 0 - (-mv)
    return 1 - (dMv/msv - msv/(2*Rr))**2
for mv in (0.01, 0.1, 0.5):
    # walk outward / inward until V stops increasing (barrier top) or m_s -> 0
    out = None; Rr = 1.0; vprev = 0.0
    for i in range(1, 200001):
        Rr = 1 + i*1e-4
        v = Vdev(Rr, mv)
        if v < vprev: out = (Rr, vprev); break
        vprev = v
    inn = None; vprev = 0.0
    for i in range(1, 9999):
        Rr = 1 - i*1e-4
        v = Vdev(Rr, mv)
        if v < vprev: inn = (Rr, vprev); break
        vprev = v
    print("    m/R=%.2f  outer barrier top %s ; inner barrier top %s" %
          (mv, ("R=%.4f V=%.3e" % out) if out else "none found to R=21",
               ("R=%.4f V=%.3e" % inn) if inn else "none found to R=0.0001 (V rises monotonically inward)"))
print("  (bounded-well sizes are recorded for scope; PV and the tree's V'' claim are linear)")

print("\nREDERIVATION %s" % ("OK" if ok else "FAILED"))
sys.exit(0 if ok else 1)
