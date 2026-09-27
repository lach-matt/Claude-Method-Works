#!/usr/bin/env python3
"""
DOCKET 67 audit -- le-2026-stiffer-wall-clause.

Le, arXiv:2606.22531v2 (30 Jun 2026) p.28, Sec 15, READ from cached alphaXiv page text:
  "A slightly stiffer, still-admissible wall is strictly stable at no cost in the
   surface dec margin, which is junction-fixed and independent of the equation-of-state
   slope, so strict stability and strict dominant energy decouple; this stiffened wall is
   a nearby model, not the realized one (App. J)."
App. J itself is NOT in the cache, so its exact hypotheses are unread.  This script
re-derives the clause FROM SCRATCH in the Poisson-Visser thin-shell linearisation
(PV eq (15) conservation, eq (23) beta^2 = dp/dsigma, V'' > 0 criterion; read in the
sibling audit gr-qc_9506083), Minkowski inside / Schwarzschild outside, and checks:

 C1  equation of motion Rdot^2 + V = 0, V = 1 - (m_s/2R + M/m_s)^2, satisfies the Lanczos
     junction sqrt(1+Rdot^2) - sqrt(f+Rdot^2) = m_s/R (with the sign condition).
 C2  statics from V(R0)=0, V'(R0)=0: sigma0 = (1-s)/(4 pi R), p0 = (1-s)^2/(16 pi R s);
     no beta^2 in either (symbolic, for ALL beta^2, not four sample values).
 C3  V(R0), V'(R0) have zero derivative w.r.t. beta^2 identically.
 C4  V''(R0) is AFFINE in beta^2 with strictly positive slope 2(1+3s)/R^2 on 0<s<1, so
     stiffening strictly raises V''; zero at beta^2_crit = (1-s)(3s^2+2s+1)/(4s^2(1+3s))
     (equals wall.py's form and the sibling audit's form).
 C5  z3: for all s in (0,1), eps > 0: V''(beta^2_crit + eps) > 0  ("slightly stiffer
     suffices") -- vacuity guard: the hypothesis set is satisfiable.
 C6  the dec margin 8 pi R(sigma0-p0) = -(5s-1)(s-1)/(2s) carries no beta^2.
 C7  "still-admissible" under the causal proxy beta^2 <= 1: exists beta^2 in
     (beta^2_crit, 1]  <=>  15 s^3 + 3 s^2 - s - 1 > 0  <=>  x < x* = 0.8437418926...
     z3: on x in (x*, 24/25) surface dec holds strictly but NO causal stiffer wall exists.
 C8  PSP 2604.05980 Gamma_1 = (1+2s+3s^2)/(4s^2) equals beta^2_crit (sigma0+p0)/p0.
 C9  decoupling is an EQUILIBRIUM statement: d(sigma-p)/dR at R0 = (1-beta^2) sigma'(R0),
     and d/d(beta^2) of it is nonzero.
 C10 finite-amplitude check (the tree's extension, wall.py:207-221): for 1 >= beta^2 >
     p0/sigma0 the surface DEC (sigma >= |p|) holds on the whole ray R in (0, inf); and
     beta^2_crit - p0/sigma0 = x/(4 s^2 (1+3s)) > 0.
 C11 numeric: wall.py (imported read-only, no bytecode) agrees with C4 to 1e-13 and
     V''(beta^2_crit(1+1e-6)) > 0 at x = 0.1, 0.3, 0.5, 0.8.
Exit 0 iff every check passes.
"""
import sys, math, importlib.util
import sympy as sp

sys.dont_write_bytecode = True
ok = True
def chk(label, cond):
    global ok
    ok &= bool(cond)
    print(("PASS " if cond else "FAIL ") + label)

R, M, Rd2 = sp.symbols('R M Rdot2', real=True)
s = sp.symbols('s', positive=True)
b2, eps = sp.symbols('beta2 epsilon', real=True)
sig0, p0 = sp.symbols('sigma0 p0', real=True)

# ---- C1: equation of motion from the Lanczos junction ------------------------
ms = sp.symbols('m_s', positive=True)
V_expr = 1 - (ms / (2 * R) + M / ms) ** 2
f = 1 - 2 * M / R
Rd2_val = -V_expr
lhs_in = sp.sqrt(sp.expand(1 + Rd2_val))           # = m_s/2R + M/m_s
lhs_out2 = sp.expand(f + Rd2_val)                   # should be (M/m_s - m_s/2R)^2
c1a = sp.simplify(lhs_out2 - (M / ms - ms / (2 * R)) ** 2) == 0
c1b = sp.simplify((ms / (2 * R) + M / ms) - (M / ms - ms / (2 * R)) - ms / R) == 0
chk("C1 V = 1-(m_s/2R+M/m_s)^2 solves sqrt(1+Rd^2)-sqrt(f+Rd^2) = m_s/R "
    "(branch M/m_s >= m_s/2R)", c1a and c1b)

# ---- set up V(R) around R0 with conservation + linear EoS --------------------
# sigma' = -2(sigma+p)/R ; p = p0 + b2 (sigma - sigma0)
R0 = sp.symbols('R0', positive=True)
sigma = sp.Function('sigma')
def V_of(Rs, sg):
    m_s = 4 * sp.pi * Rs ** 2 * sg
    return 1 - (m_s / (2 * Rs) + M / m_s) ** 2
Vf = V_of(R, sigma(R))
d1 = sp.diff(Vf, R)
d2 = sp.diff(Vf, R, 2)
# derivatives of sigma at R0
sp1 = -2 * (sig0 + p0) / R0
# sigma'' = d/dR[-2(sigma+p)/R] = -2(1+b2) sigma'/R + 2(sigma+p)/R^2
sp2 = -2 * (1 + b2) * sp1 / R0 + 2 * (sig0 + p0) / R0 ** 2
subsd = {sp.Derivative(sigma(R), (R, 2)): sp2, sp.Derivative(sigma(R), R): sp1}
def at0(e):
    e = e.subs(subsd).subs(sigma(R), sig0).subs(R, R0)
    return sp.simplify(e)
V0, V1, V2 = at0(Vf), at0(d1), at0(d2)

# ---- C2 statics ---------------------------------------------------------------
Mval = (1 - s ** 2) * R0 / 2            # x = 1 - s^2 = 2M/R0
sig_star = (1 - s) / (4 * sp.pi * R0)
p_star = (1 - s) ** 2 / (16 * sp.pi * R0 * s)
c2a = sp.simplify(V0.subs(M, Mval).subs(sig0, sig_star)) == 0
c2b = sp.simplify(V1.subs(M, Mval).subs({sig0: sig_star, p0: p_star})) == 0
# uniqueness of p0 given sigma0: V1 linear in p0
p_sol = sp.solve(sp.Eq(V1.subs(M, Mval).subs(sig0, sig_star), 0), p0)
c2c = len(p_sol) == 1 and sp.simplify(p_sol[0] - p_star) == 0
chk("C2 V(R0)=0 at sigma0=(1-s)/(4 pi R0); V'(R0)=0 forces p0=(1-s)^2/(16 pi R0 s) uniquely",
    c2a and c2b and c2c)
chk("C2' neither V(R0) nor V'(R0) contains beta^2 (free symbols)",
    b2 not in V0.free_symbols and b2 not in V1.free_symbols)

# ---- C3 -----------------------------------------------------------------------
chk("C3 dV(R0)/dbeta^2 == 0 and dV'(R0)/dbeta^2 == 0 identically",
    sp.diff(V0, b2) == 0 and sp.simplify(sp.diff(V1, b2)) == 0)

# ---- C4 -----------------------------------------------------------------------
V2s = sp.simplify(V2.subs(M, Mval).subs({sig0: sig_star, p0: p_star}))
V2poly = sp.Poly(sp.together(V2s * R0 ** 2 * s ** 2).expand(), b2)
slope = sp.simplify(sp.diff(V2s, b2))
c4a = V2poly.degree() == 1
c4b = sp.simplify(slope - 2 * (1 + 3 * s) / R0 ** 2) == 0
b2c = sp.solve(sp.Eq(V2s, 0), b2)
b2crit_wall = (1 - s) * (3 * s ** 2 + 2 * s + 1) / (4 * s ** 2 * (1 + 3 * s))
c4c = len(b2c) == 1 and sp.simplify(b2c[0] - b2crit_wall) == 0
sib = (2 * b2 * (3 * s + 1) * s ** 2 + (s - 1) * (3 * s ** 2 + 2 * s + 1) / 2) / (s ** 2 * R0 ** 2)
c4d = sp.simplify(V2s - sib) == 0
chk("C4 V''(R0) affine in beta^2", c4a)
chk("C4 slope dV''/dbeta^2 = 2(1+3s)/R0^2 > 0", c4b)
chk("C4 unique zero beta^2_crit = (1-s)(3s^2+2s+1)/(4s^2(1+3s)) (= wall.py)", c4c)
chk("C4 V'' equals sibling audit's closed form", c4d)
print("     V''(R0) =", sp.factor(V2s))

# ---- C5 z3 --------------------------------------------------------------------
try:
    import z3
except ImportError:
    z3 = None
if z3 is None:
    chk("C5 z3 available", False)
else:
    S, E, B = z3.Reals('s e b')
    # V'' * s^2 R0^2 = 2 b (3s+1) s^2 + (s-1)(3s^2+2s+1)/2 ; beta2_crit*(4 s^2 (1+3s)) = (1-s)(3s^2+2s+1)
    Vpp = lambda bb: 2 * bb * (3 * S + 1) * S * S + (S - 1) * (3 * S * S + 2 * S + 1) / 2
    bc_times = (1 - S) * (3 * S * S + 2 * S + 1)          # = b_crit * 4 s^2 (1+3s)
    den = 4 * S * S * (1 + 3 * S)
    hyp = z3.And(S > 0, S < 1, E > 0, B * den == bc_times + E * den)   # B = b_crit + e
    sol = z3.Solver(); sol.add(hyp, z3.Not(Vpp(B) > 0))
    r5 = sol.check()
    guard = z3.Solver(); guard.add(hyp); g5 = guard.check()
    chk("C5 z3: forall s in (0,1), eps>0: V''(beta^2_crit+eps) > 0  [negation %s, vacuity guard %s]"
        % (r5, g5), r5 == z3.unsat and g5 == z3.sat)

# ---- C6 -----------------------------------------------------------------------
margin = sp.simplify(8 * sp.pi * R0 * (sig_star - p_star))
chk("C6 8 pi R(sigma0-p0) = -(5s-1)(s-1)/(2s), no beta^2",
    sp.simplify(margin + (5 * s - 1) * (s - 1) / (2 * s)) == 0 and b2 not in margin.free_symbols)

# ---- C7 causal admissibility window ------------------------------------------
cond = sp.expand(4 * s ** 2 * (1 + 3 * s) - (1 - s) * (3 * s ** 2 + 2 * s + 1))
chk("C7 beta^2_crit < 1  <=>  15s^3+3s^2-s-1 > 0", sp.simplify(cond - (15 * s ** 3 + 3 * s ** 2 - s - 1)) == 0)
roots = [r for r in sp.Poly(15 * s ** 3 + 3 * s ** 2 - s - 1, s).nroots(n=30) if r.is_real and 0 < r < 1]
sstar = roots[0]; xstar = 1 - sstar ** 2
print("     s* = %s, x* = %s" % (sp.N(sstar, 15), sp.N(xstar, 15)))
chk("C7 x* = 0.8437418926 (wall.py:32)", abs(float(xstar) - 0.8437418926) < 1e-9)
chk("C7 exactly one root of the cubic in (0,1)", len(roots) == 1)
if z3 is not None:
    S = z3.Real('s')
    cub = 15 * S ** 3 + 3 * S ** 2 - S - 1
    # x in (x*, 24/25) <=> s in (1/5, s*) ; there cubic < 0, dec margin > 0
    sol = z3.Solver()
    sol.add(S > z3.RealVal(1) / 5, S < 1, cub <= 0,
            z3.Not(-(5 * S - 1) * (S - 1) > 0))       # dec fails?
    r7a = sol.check()
    wit = z3.Solver(); wit.add(S > z3.RealVal(1) / 5, S < 1, cub < 0); r7b = wit.check()
    w = wit.model()[S] if r7b == z3.sat else None
    chk("C7 z3: on s in (1/5,1) with cubic<=0 surface dec holds strictly [negation %s]; "
        "a witness with NO causal stiffer wall exists [%s, s=%s]" % (r7a, r7b, w),
        r7a == z3.unsat and r7b == z3.sat)
    sol2 = z3.Solver(); sol2.add(S > 0, S < 1, cub > 0, S * S > z3.RealVal(1) / 5)
    # x < 4/5 <=> s^2 > 1/5 ; show cubic > 0 on all of it
    sol3 = z3.Solver(); sol3.add(S > 0, S < 1, S * S > z3.RealVal(1) / 5, cub <= 0)
    r7c = sol3.check()
    chk("C7 z3: on the realized-wall window x < 4/5 a causal stiffer wall ALWAYS exists [negation %s]"
        % r7c, r7c == z3.unsat)

# ---- C8 PSP Gamma_1 -----------------------------------------------------------
G1 = (1 + 2 * s + 3 * s ** 2) / (4 * s ** 2)
chk("C8 beta^2_crit (sigma0+p0)/p0 == PSP Gamma_1 = (1+2s+3s^2)/(4s^2)",
    sp.simplify(b2crit_wall * (sig_star + p_star) / p_star - G1) == 0)

# ---- C9 off-equilibrium -------------------------------------------------------
dmargin = sp.simplify((1 - b2) * sp1.subs({sig0: sig_star, p0: p_star}))
chk("C9 d(sigma-p)/dR|R0 = (1-beta^2) sigma'(R0) depends on beta^2 (equilibrium-only decoupling)",
    sp.simplify(sp.diff(dmargin, b2)) != 0)
print("     d(sigma-p)/dR|R0 =", sp.factor(dmargin))

# ---- C10 finite amplitude DEC along the ray -----------------------------------
c10a = sp.simplify(b2crit_wall - p_star / sig_star - (1 - s ** 2) / (4 * s ** 2 * (1 + 3 * s))) == 0
chk("C10 beta^2_crit - p0/sigma0 = x/(4s^2(1+3s)) > 0", c10a)
def sig_R(rr, x, bb):
    ss = math.sqrt(1 - x); sg = (1 - ss) / (4 * math.pi); pp = (1 - ss) ** 2 / (16 * math.pi * ss)
    A = 1 + bb; K = pp - bb * sg
    sgr = (sg + K / A) * rr ** (-2 * A) - K / A
    return sgr, pp + bb * (sgr - sg)
worst = float('inf')
for x in (0.05, 0.3, 0.6, 0.8):
    ss = math.sqrt(1 - x)
    bc = (1 - ss) * (3 * ss * ss + 2 * ss + 1) / (4 * ss * ss * (1 + 3 * ss))
    for bb in (bc * (1 + 1e-6), min(1.0, bc * 1.5), 1.0):
        if bb < bc: continue
        for k in range(-300, 601):
            rr = 10 ** (k / 100.0)
            sg, pp = sig_R(rr, x, bb)
            worst = min(worst, (sg - abs(pp)) / sg)
chk("C10 numeric: sigma >= |p| on R/R0 in [1e-3, 1e6] for stable, causal walls "
    "(min relative margin %.3e)" % worst, worst >= -1e-12)

# ---- C11 wall.py cross-check --------------------------------------------------
spec = importlib.util.spec_from_file_location("wall_ro", "/home/user/Claude-Method-Works/research/warp-drive/wall.py")
wall = importlib.util.module_from_spec(spec); spec.loader.exec_module(wall)
good = True
for x in (0.1, 0.3, 0.5, 0.8):
    sv = math.sqrt(1 - x)
    mine = float(b2crit_wall.subs(s, sv))
    good &= abs(mine - wall.beta2_crit(x)) < 1e-13
    for bb in (0.0, 0.2, 0.5, 1.0):
        good &= abs(float(V2s.subs({s: sv, R0: 1, b2: bb})) - wall.Vpp(x, bb)) < 1e-12
    good &= wall.Vpp(x, wall.beta2_crit(x) * (1 + 1e-6)) > 0
chk("C11 wall.py beta2_crit and Vpp agree with the symbolic derivation (1e-12); "
    "V'' > 0 at beta^2_crit(1+1e-6)", good)
# the tree's vacuous check (wall.py:527-528): the set has one element for any input
chk("C11' recorded: wall.py:527-528's len({round(dec_margin_scaled(0.3),12)}) == 1 varies no beta^2 "
    "(vacuous as a test; true claim)", len({round(wall.dec_margin_scaled(0.3), 12)}) == 1)

print("\nALL CHECKS PASS" if ok else "\nSOME CHECK FAILED")
sys.exit(0 if ok else 1)
