#!/usr/bin/env python3
"""
DOCKET 67 -- re-derivation for 'energy-conditions-thin-shell'
(stability.py:29-37, 145-151, 238-239).

Checks, independent of the tree except section E (which imports stability.py
READ-ONLY with bytecode writing disabled, so nothing is written under research/):

 A. sympy: the Lanczos/Israel sigma, p for M_in = -m, M_out = 0 depend on x = m/R
    only through sigma*R, p*R; closed forms; signs for EVERY x > 0 (not just the
    four sampled): sigma > 0, p < 0, sigma + p > 0, hence sigma >= |p| (DEC).
    Limits: |p|/sigma -> 0 as x -> 0, -> 1/4 as x -> oo.
 B. z3: the same sign claims as a quantified proof over the reals
    (s = sqrt(1+2x) encoded as s > 0, s^2 = 1 + 2x).
 C. The tree's data column (stability.py:29-33) recomputed exactly.
 D. z3: what the SURFACE (2+1, tangential) conditions are equivalent to in the
    4D distributional stress tensor T = diag(sigma, 0, p, p) delta(l)
    (orthonormal frame t, n, theta, phi; zero normal pressure):
      D1 4D DEC  <=> surface DEC  (sigma >= 0 and sigma >= |p|)
      D2 4D WEC  <=> surface WEC  (sigma >= 0 and sigma + p >= 0)
      D3 4D NEC  <=> sigma >= 0 and sigma + p >= 0   (= surface WEC, NOT sigma+p>=0)
      D4 surface (tangential) NEC <=> sigma + p >= 0
      D5 counterexample: sigma = -1, p = 2 passes nec_holds, fails the 4D NEC.
 E. The tree's own functions at the tabulated compactnesses and on a dense grid.
"""
import math, sys, importlib.util
import sympy as sp
import z3

ok = True
def chk(label, cond):
    global ok
    ok &= bool(cond)
    print("  %-70s %s" % (label, "ok" if cond else "FAIL"))

# ---------------------------------------------------------------- A. sympy
print("A. closed forms (sympy)")
R, m, x = sp.symbols('R m x', positive=True)
f = lambda M: 1 - 2*M/R
Min, Mout = -m, 0
sig = -(1/(4*sp.pi*R))*(sp.sqrt(f(Mout)) - sp.sqrt(f(Min)))
p = (1/(8*sp.pi*R))*((1 - sp.Integer(Mout)/R)/sp.sqrt(f(Mout)) - (1 - Min/R)/sp.sqrt(f(Min)))
sigx = sp.simplify((sig*R).subs(m, x*R))
px = sp.simplify((p*R).subs(m, x*R))
print("   sigma*R =", sigx, "   p*R =", px)
chk("sigma*R, p*R are functions of x = m/R alone", not (sigx.has(R) or px.has(R)))
s = sp.sqrt(1 + 2*x)
chk("sigma*R == (sqrt(1+2x) - 1)/(4 pi)", sp.simplify(sigx - (s - 1)/(4*sp.pi)) == 0)
chk("p*R == (1 - (1+x)/sqrt(1+2x))/(8 pi)", sp.simplify(px - (1 - (1 + x)/s)/(8*sp.pi)) == 0)
# sign proofs by hand, each identity checked by sympy
# p < 0  <=>  (1+x)^2 > 1+2x  <=> x^2 > 0
chk("(1+x)^2 - (1+2x) == x^2  (so p < 0 for every x > 0)", sp.expand((1 + x)**2 - (1 + 2*x) - x**2) == 0)
# sigma + p = (1/8pi s) [ 2 s^2 - s - (1+x) ] = (1/8pi s)[1 + 3x - s]
sp_sum = sp.simplify((sigx + px)*8*sp.pi*s - (1 + 3*x - s))
chk("8 pi sqrt(1+2x) (sigma+p) R == 1 + 3x - sqrt(1+2x)", sp_sum == 0)
chk("(1+3x)^2 - (1+2x) == 4x + 9x^2 > 0  (so sigma + p > 0 for every x > 0)",
    sp.expand((1 + 3*x)**2 - (1 + 2*x) - (4*x + 9*x**2)) == 0)
ratio = sp.simplify(-px/sigx)
lim0 = sp.limit(ratio, x, 0, '+'); limi = sp.limit(ratio, x, sp.oo)
print("   |p|/sigma -> %s (x->0),  -> %s (x->oo)" % (lim0, limi))
chk("|p|/sigma -> 0 as x -> 0 and -> 1/4 as x -> oo", lim0 == 0 and limi == sp.Rational(1, 4))
ser = sp.series(ratio, x, 0, 3).removeO()
print("   |p|/sigma = %s + O(x^3)" % sp.simplify(ser))
# monotone: ratio < 1/4 everywhere?
xs = [10**k for k in range(-6, 9)]
chk("|p|/sigma < 1/4 at x = 1e-6 .. 1e8 (margin to DEC >= 3/4 sigma)",
    all(float(ratio.subs(x, v)) < 0.25 for v in xs))

# ---------------------------------------------------------------- B. z3
print("\nB. quantified proof over the reals (z3)")
X, S = z3.Reals('X S')
hyp = z3.And(X > 0, S > 0, S*S == 1 + 2*X)
sigma_n = (S - 1)            # sign of sigma*R*4pi
p_n = S - (1 + X)            # sign of p (p*R*8pi*S = S - (1+X))
sum_n = 1 + 3*X - S          # sign of sigma + p
def valid(name, claim):
    sv = z3.Solver(); sv.add(hyp, z3.Not(claim))
    r = sv.check()
    chk("z3: for all x > 0: %s  [%s]" % (name, r), r == z3.unsat)
valid("sigma > 0", sigma_n > 0)
valid("p < 0", p_n < 0)
valid("sigma + p > 0", sum_n > 0)
# DEC: sigma >= |p| with the physical normalisations: 4pi sigma R = S-1, 8pi p R S = S-(1+X)
# sigma - |p| = sigma + p (p<0); (sigma+p)*8pi R S = 2 S(S-1) + S - (1+X) = 1+3X-S
valid("2S(S-1) + (S-(1+X)) == 1 + 3X - S (normalisation identity)",
      2*S*(S - 1) + (S - (1 + X)) == 1 + 3*X - S)

# ---------------------------------------------------------------- C. data
print("\nC. the tree's table, stability.py:29-33")
table = {0.01: (7.918e-4, -1.950e-6, 7.899e-4), 0.10: (7.595e-3, -1.654e-4, 7.430e-3),
         0.50: (3.296e-2, -2.414e-3, 3.055e-2), 2.00: (9.836e-2, -1.359e-2, 8.477e-2)}
for xv, (s_t, p_t, sp_t) in table.items():
    sv = float(sigx.subs(x, xv)); pv = float(px.subs(x, xv))
    good = (abs(sv - s_t) <= 0.5e-3*abs(s_t) + 1e-12 and abs(pv - p_t) <= 0.5e-3*abs(p_t)
            and abs((sv + pv) - sp_t) <= 0.5e-3*abs(sp_t) and abs((sv - abs(pv)) - sp_t) <= 0.5e-3*abs(sp_t))
    print("   x=%.2f sigma=%+.4e p=%+.4e sigma+p=%+.4e sigma-|p|=%+.4e" % (xv, sv, pv, sv + pv, sv - abs(pv)))
    chk("x=%.2f matches the printed row to 4 significant figures" % xv, good)

# ---------------------------------------------------------------- D. 4D vs surface
print("\nD. surface conditions vs the 4D distributional stress tensor (z3)")
sg, pp = z3.Reals('sigma p')
kt, kn, k2, k3 = z3.Reals('kt kn k2 k3')
def Tkk(a, b, c, d):   # T_{mu nu} v v in orthonormal frame, T = diag(sigma, 0, p, p)
    return sg*a*a + 0*b*b + pp*(c*c + d*d)
def equiv(name, lhs, rhs):
    sv = z3.Solver(); sv.add(lhs != rhs)
    r = sv.check()
    chk("z3: %s  [%s]" % (name, r), r == z3.unsat)
null4 = z3.And(kt > 0, kt*kt == kn*kn + k2*k2 + k3*k3)
NEC4 = z3.ForAll([kt, kn, k2, k3], z3.Implies(null4, Tkk(kt, kn, k2, k3) >= 0))
tl4 = z3.And(kt > 0, kt*kt > kn*kn + k2*k2 + k3*k3)
WEC4 = z3.ForAll([kt, kn, k2, k3], z3.Implies(tl4, Tkk(kt, kn, k2, k3) >= 0))
# DEC: WEC and -T^mu_nu v^nu causal: flux F = (sigma vt, 0, -p v2, -p v3) (signs irrelevant to norm)
DEC4 = z3.And(WEC4, z3.ForAll([kt, kn, k2, k3], z3.Implies(tl4,
        (sg*kt)*(sg*kt) >= (pp*k2)*(pp*k2) + (pp*k3)*(pp*k3))))
null3 = z3.And(kt > 0, kt*kt == k2*k2 + k3*k3)
NEC3 = z3.ForAll([kt, k2, k3], z3.Implies(null3, sg*kt*kt + pp*(k2*k2 + k3*k3) >= 0))
surfDEC = z3.And(sg >= 0, sg >= pp, sg >= -pp)
surfWEC = z3.And(sg >= 0, sg + pp >= 0)
equiv("4D DEC <=> sigma >= 0 and sigma >= |p|", DEC4, surfDEC)
equiv("4D WEC <=> sigma >= 0 and sigma + p >= 0", WEC4, surfWEC)
equiv("4D NEC <=> sigma >= 0 and sigma + p >= 0 (the surface WEC)", NEC4, surfWEC)
equiv("surface (tangential, 2+1) NEC <=> sigma + p >= 0", NEC3, sg + pp >= 0)
sv = z3.Solver(); sv.add(sg == -1, pp == 2, sg + pp >= 0, z3.Not(NEC4)); r = sv.check()
chk("sigma=-1, p=2: passes sigma+p>=0 yet violates the 4D NEC [%s]" % r, r == z3.sat)
chk("  witness: radial null k=(1,1,0,0) gives T_kk = sigma = -1 < 0", -1*1 + 0 < 0)
# DEC (surface) implies the 4D NEC, so the tree's DEC verdict carries the 4D NEC with it
sv = z3.Solver(); sv.add(surfDEC, z3.Not(NEC4)); r = sv.check()
chk("surface DEC => 4D NEC  [%s]" % r, r == z3.unsat)

# ---------------------------------------------------------------- E. the tree's functions
print("\nE. stability.py's own dec_holds / nec_holds (imported read-only, no bytecode)")
sys.dont_write_bytecode = True
spec = importlib.util.spec_from_file_location(
    "stab_ro", "/home/user/Claude-Method-Works/research/warp-drive/stability.py")
st = importlib.util.module_from_spec(spec); spec.loader.exec_module(st)
for xv in (0.01, 0.1, 0.5, 2.0):
    Rr, Mi, Mo = st.device(xv)
    chk("x=%.2f  tree sigma, p agree with sympy to 1e-14; dec, nec True" % xv,
        abs(st.sigma(Rr, Mi, Mo) - float(sigx.subs(x, xv))) < 1e-14
        and abs(st.pressure(Rr, Mi, Mo) - float(px.subs(x, xv))) < 1e-14
        and st.dec_holds(Rr, Mi, Mo) and st.nec_holds(Rr, Mi, Mo))
grid = [10**(k/10.0) for k in range(-60, 61)]
chk("dec_holds True on 121 log-spaced x in [1e-6, 1e6]",
    all(st.dec_holds(*st.device(v)) for v in grid))
# non-vacuity: the ordinary textbook shell (flat in, mass out) -- does DEC hold? sigma>0, p>0
Rr, Mi, Mo = st.ordinary(0.1)
print("   ordinary shell M/R=0.1: sigma=%+.4e p=%+.4e dec=%s" % (
    st.sigma(Rr, Mi, Mo), st.pressure(Rr, Mi, Mo), st.dec_holds(Rr, Mi, Mo)))
# vacuity guard: dec_holds must be able to return False
Rr, Mi, Mo = st.ordinary(0.49)
chk("vacuity guard: dec_holds returns False somewhere (ordinary shell M/R=0.49: p>sigma)",
    st.dec_holds(Rr, Mi, Mo) is False)
Rr, Mi, Mo = (1.0, 0.3, 0.0)   # mass inside, flat outside: sigma < 0
print("   M_in=+0.3, M_out=0: sigma=%+.4e p=%+.4e nec=%s dec=%s" % (
    st.sigma(Rr, Mi, Mo), st.pressure(Rr, Mi, Mo), st.nec_holds(Rr, Mi, Mo), st.dec_holds(Rr, Mi, Mo)))
chk("vacuity guard: nec_holds returns False for M_in=+0.3, M_out=0 (sigma+p<0)",
    st.nec_holds(Rr, Mi, Mo) is False)

print("\nALL CHECKS PASS" if ok else "\nSOME CHECK FAILED")
sys.exit(0 if ok else 1)
