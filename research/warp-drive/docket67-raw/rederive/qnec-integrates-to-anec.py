#!/usr/bin/env python3
"""
D67 re-derivation: 'QNEC integrated along a complete null generator implies ANEC
(boundary term [S'] vanishes)'  -- anec.py:35-39, 154-159, 182.

What is finite / closed-form here and is checked:
  R1 (sympy)  the per-generator integrated QNEC (BFKW 1706.09432 eq 1.3 as restated)
              with cuts A -> -inf, B -> +inf is INT T >= (1/2pi)[S'(B) - S'(A)],
              and equals the FTC of the pointwise form: the tree's formula.
  R2 (z3)     on a discretised generator: pointwise QNEC + [S'] = 0  ==>  sum T >= 0
              (UNSAT of the negation); [S'] >= 0 suffices; [S'] < 0 admits sum T < 0
              (SAT, witness printed).  So the boundary hypothesis is load-bearing, and
              the tree's function qnec_implies_anec() (returns True unconditionally)
              encodes none of it.
  R3 (sympy)  the null-plane modular identity dK'(B) = -2pi INT_B^inf T (Wall;
              Casini-Teste-Torroba; CF 1812.04683, as restated) with S_rel = dK - dS:
                (a) QNEC  <=>  S_rel'' >= 0   (convexity, CF eq 3.19 as restated)
                (b) 2pi ANE = [S_rel'] + [dS']       -- exact identity
                (c) hence with [dS'] = 0, ANEC follows from MONOTONICITY alone
                    (S_rel' <= 0, S_rel'(+inf) = 0): QNEC adds nothing to the ANEC
                    conclusion beyond what relative-entropy monotonicity gives.
              Checked symbolically and on an explicit profile.
  R4 (numeric, ILLUSTRATIVE)  the size of boundary term that would be needed to
              absorb the tree's classical ANEC value: |[S'/A]| = 2pi|ANE|/(hbar c).
              With classical T = G_mn c^4/(8 pi G), the ratio to the Bekenstein-
              Hawking density 1/(4 l_P^2) per bubble radius is R-independent.
  R5 (read-only import of the tree)  qnec_implies_anec() takes no arguments and
              returns True: the flag cannot fail, whatever the hypotheses.

What is NOT checked: the QNEC itself (replica / modular-inclusion proofs are not
finite), and whether [S'] vanishes for any state on the warp background -- no state
exists in the tree to compute it for.
"""
import math, sys
import sympy as sp

OK = True
def chk(label, cond):
    global OK
    OK &= bool(cond)
    print("  %-72s %s" % (label, "ok" if cond else "FAIL"))

print("R1  per-generator integrated QNEC -> the tree's [S'] formula")
lam, A, B, hb = sp.symbols('lambda A B hbar', real=True)
S = sp.Function('S')
T = sp.Function('T')
# QNEC pointwise:  T - (hbar/2pi) S'' >= 0.  Integrate A..B:
lhs = sp.Integral(T(lam), (lam, A, B))
rhs = hb/(2*sp.pi) * (sp.diff(S(lam), lam).subs(lam, B) - sp.diff(S(lam), lam).subs(lam, A))
ftc = sp.integrate(sp.diff(S(lam), lam, 2), (lam, A, B))
chk("INT_A^B S'' dlambda == S'(B) - S'(A)   (FTC, sympy)",
    sp.simplify(ftc - (sp.diff(S(lam), lam).subs(lam, B) - sp.diff(S(lam), lam).subs(lam, A))) == 0)
# BFKW eq 1.3 form Q_-(A,B;y) = INT_A^B T - (1/2pi) S'(B) + (1/2pi) S'(A) >= 0 (hbar = 1)
Q = lhs - rhs.subs(hb, 1)
chk("Q_-(A,B) >= 0 is INT_A^B T >= (1/2pi)[S'(B)-S'(A)]  (same expression)",
    sp.simplify(Q - (lhs - (sp.diff(S(lam), lam).subs(lam, B) - sp.diff(S(lam), lam).subs(lam, A))/(2*sp.pi))) == 0)

print("\nR2  z3: the boundary hypothesis is load-bearing")
import z3
N = 12
h = z3.RealVal(1)
Tz = [z3.Real('T%d' % i) for i in range(N)]
Sz = [z3.Real('S%d' % i) for i in range(N + 2)]
twopi = z3.RealVal(2) * z3.RealVal(355) / z3.RealVal(113)   # positive constant; sign logic only
qnec = [Tz[i] * twopi >= (Sz[i + 2] - 2 * Sz[i + 1] + Sz[i]) for i in range(N)]
Sp_start = Sz[1] - Sz[0]
Sp_end = Sz[N + 1] - Sz[N]
def solve(extra):
    s = z3.Solver(); s.add(qnec); s.add(extra); s.add(z3.Sum(Tz) < 0)
    return s.check(), s
r, _ = solve([Sp_start == 0, Sp_end == 0])
chk("QNEC + S'(start)=S'(end)=0 + sum T < 0 : UNSAT", r == z3.unsat)
r, _ = solve([Sp_end - Sp_start >= 0])
chk("QNEC + [S'] >= 0 + sum T < 0 : UNSAT  ([S'] >= 0 already suffices)", r == z3.unsat)
r, s = solve([Sp_end - Sp_start == -1])
chk("QNEC + [S'] = -1 + sum T < 0 : SAT  (ANEC can fail)", r == z3.sat)
if r == z3.sat:
    m = s.model()
    tot = sum(float(m.eval(t).as_fraction()) for t in Tz)
    print("      witness: sum T = %.4f, [S'] = -1  (sum T >= [S']/2pi = %.4f)" % (tot, -1/(2*355/113)))
r, _ = solve([Sp_start == 0])
chk("QNEC + only S'(start)=0 + sum T < 0 : SAT (both ends needed)", r == z3.sat)

print("\nR3  null-plane modular identity: what QNEC adds to ANEC")
b = sp.symbols('b', real=True)
# symbolic: dK(b) = 2pi INT_b^inf (l - b) T(l) dl  => dK'' = 2pi T(b)
l = sp.symbols('l', real=True)
dK = 2*sp.pi*sp.Integral((l - b)*T(l), (l, b, sp.oo))
dK1 = sp.diff(dK, b).doit()
dK2 = sp.diff(dK1, b).doit()
chk("dK'(b) = -2pi INT_b^inf T", sp.simplify(dK1 + 2*sp.pi*sp.Integral(T(l), (l, b, sp.oo))) == 0)
chk("dK''(b) = 2pi T(b)", sp.simplify(dK2 - 2*sp.pi*T(b)) == 0)
dS = sp.Function('dS')
Srel2 = dK2 - sp.diff(dS(b), b, 2)
chk("(a) S_rel'' = 2pi (T - dS''/2pi): QNEC <=> convexity of S_rel",
    sp.simplify(Srel2 - 2*sp.pi*(T(b) - sp.diff(dS(b), b, 2)/(2*sp.pi))) == 0)
# (b) boundary identity: [dK'] = dK'(+inf) - dK'(-inf) = 0 - (-2pi ANE) = 2pi ANE
#     S_rel' = dK' - dS'  =>  [S_rel'] = 2pi ANE - [dS']
ANE, Sr_m, Sr_p, dS_m, dS_p = sp.symbols('ANE Srel1_m Srel1_p dS1_m dS1_p', real=True)
ident = sp.Eq(Sr_p - Sr_m, 2*sp.pi*ANE - (dS_p - dS_m))
sol = sp.solve(ident, ANE)[0]
chk("(b) 2pi ANE = [S_rel'] + [dS']", sp.simplify(sol - ((Sr_p - Sr_m) + (dS_p - dS_m))/(2*sp.pi)) == 0)
# (c) monotonicity: S_rel' <= 0 everywhere and -> 0 at +inf  =>  [S_rel'] = -S_rel'(-inf) >= 0
ANE_c = sol.subs({Sr_p: 0, dS_p: 0, dS_m: 0})
chk("(c) with [dS']=0, S_rel'(+inf)=0: ANE = -S_rel'(-inf)/2pi >= 0 by monotonicity",
    sp.simplify(ANE_c + Sr_m/(2*sp.pi)) == 0)
# explicit profile: T = gaussian bump with a negative dip, ANE > 0; choose dS so that QNEC holds
x = sp.symbols('x', real=True)
Tx = sp.exp(-x**2) * (1 - sp.Rational(1, 2) * sp.exp(-4*x**2) * 3)   # dips negative near 0
ane_val = sp.integrate(Tx, (x, -sp.oo, sp.oo))
chk("explicit T(x): negative somewhere (T(0) = %s) yet ANE = %.5f > 0"
    % (Tx.subs(x, 0), float(ane_val)), Tx.subs(x, 0) < 0 and ane_val > 0)
# dS'' = 2pi T saturates QNEC; dS'(x) = 2pi INT_-inf^x T -> 0 at -inf, 2pi ANE at +inf
dS1 = 2*sp.pi*sp.integrate(Tx.subs(x, l), (l, -sp.oo, x))
bnd = sp.limit(dS1, x, sp.oo) - sp.limit(dS1, x, -sp.oo)
chk("QNEC-saturating dS has [dS'] = 2pi ANE (!= 0): boundary term need not vanish",
    sp.simplify(bnd - 2*sp.pi*ane_val) == 0)
print("      i.e. integrated QNEC then reads ANE >= ANE: consistent but vacuous; the")
print("      conclusion INT T >= 0 comes from [S'] = 0, a hypothesis on the state.")

print("\nR4  ILLUSTRATIVE: boundary term that would absorb the tree's classical ANE")
# INT T_kk dlambda (SI) = (c^4/G) * ANE_geom / R ; need |[S'/A]| = 2pi |ANE_SI| / (hbar c)
#   = 2pi |ANE_geom| / (l_P^2 R).  Bekenstein-Hawking density per area per length R: 1/(4 l_P^2 R)
for label, ane in (("tree value, non-affine (anec.py y=0)", -0.0807),
                   ("affine value (sibling audit)", -0.0524)):
    ratio = 2*math.pi*abs(ane) * 4
    print("      %-40s |[S'/A]| / (S_BH/A per R) = %.3f" % (label, ratio))
chk("ratio is O(1) and R-independent: a Planck-density entropy gradient", 0.5 < 2*math.pi*0.0807*4 < 5)
print("      => only a gravitational-scale entanglement gradient could offset a classical")
print("         violation; the fixed-background QNEC proofs do not reach that regime.")

print("\nR5  the tree's flag (read-only import)")
sys.dont_write_bytecode = True   # never write into research/warp-drive
sys.path.insert(0, '/home/user/Claude-Method-Works/research/warp-drive')
try:
    import inspect, anec
    sig = inspect.signature(anec.qnec_implies_anec)
    chk("qnec_implies_anec() takes no parameters", len(sig.parameters) == 0)
    chk("qnec_implies_anec() returns True", anec.qnec_implies_anec() is True)
    src = inspect.getsource(anec.qnec_implies_anec)
    chk("body contains no computation (only 'return True')", src.strip().endswith("return True"))
except Exception as e:
    chk("import anec.py: %r" % e, False)

print("\nOVERALL:", "PASS" if OK else "FAIL")
sys.exit(0 if OK else 1)
