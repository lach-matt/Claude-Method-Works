#!/usr/bin/env python3
"""DOCKET 67 re-derivation: irrationality-sqrt2-degenerate-span (latticectc.py:54-58, 123, 404-408).
Signature (-,+,+) on (t,x,y), as latticectc.py's 3-tuple generators use.  Exact where possible."""
import math, sys
from fractions import Fraction as Fr
from math import isqrt
import sympy as sp
import z3

ok = True
def chk(name, got, want):
    global ok
    good = (got == want)
    ok &= good
    print(("PASS" if good else "FAIL"), name, "->", got)

eta = sp.diag(-1, 1, 1)
ip = lambda a, b: (sp.Matrix(a).T * eta * sp.Matrix(b))[0]
s, m, n = sp.symbols('s m n', real=True)
g1, g2 = [1, 1, s], [0, 0, 1]

print("A. the norm identity and the degenerate Gram (symbolic)")
v = [m*a + n*b for a, b in zip(g1, g2)]
chk("|m g1 + n g2|^2 - (m s + n)^2 == 0", sp.simplify(sp.expand(ip(v, v) - (m*s + n)**2)), 0)
A, C, H = ip(g1, g1), ip(g2, g2), ip(g1, g2)
chk("Gram: A = s^2, C = 1, H = s", (sp.simplify(A - s**2), C, sp.simplify(H - s)), (0, 1, 0))
chk("Gram determinant AC - H^2 == 0 for every s (degenerate span)", sp.simplify(A*C - H**2), 0)
nullv = [a - s*b for a, b in zip(g1, g2)]
chk("g1 - s g2 == (1,1,0)", [sp.simplify(x) for x in nullv], [1, 1, 0])
chk("(1,1,0) is null", sp.simplify(ip(nullv, nullv)), 0)
chk("g1, g2 linearly independent (rank 2 => L discrete)", sp.Matrix([g1, g2]).rank(), 2)

print("B. irrationality of sqrt 2 (the load-bearing hypothesis)")
# B1 exact box: m sqrt2 + n = 0 with (m,n) != 0 iff n^2 = 2 m^2 with m != 0
def hits(B):
    return [(a, b) for a in range(-B, B+1) for b in range(-B, B+1)
            if (a, b) != (0, 0) and b*b == 2*a*a]
chk("exact: no (m,n) != 0 with n^2 = 2m^2, |m|,|n| <= 60 (the tree's box)", hits(60), [])
cnt = sum(1 for a in range(1, 10**6+1) if isqrt(2*a*a)**2 == 2*a*a)
chk("exact: no m in 1..10^6 with 2m^2 a perfect square", cnt, 0)
# B2 descent step (Tennenbaum form, as restated in arXiv:2508.08267 sec 2.4), sympy + z3
a_, b_ = sp.symbols('a b', integer=True)
chk("identity (2b-a)^2 - 2(a-b)^2 == -(a^2 - 2b^2)", sp.expand((2*b_-a_)**2 - 2*(a_-b_)**2 + (a_**2 - 2*b_**2)), 0)
a, b = z3.Reals('a b')
sol = z3.Solver()
sol.add(a > 0, b > 0, a*a == 2*b*b, z3.Not(z3.And(b < a, a < 2*b)))
chk("z3: a,b>0, a^2 = 2b^2  =>  b < a < 2b, so 0 < a-b < b (strict descent)", str(sol.check()), "unsat")
# vacuity guard: premises satisfiable over the reals (a = sqrt2 b), so the unsat is not vacuous
sol2 = z3.Solver(); sol2.add(a > 0, b > 0, a*a == 2*b*b)
chk("vacuity guard: premises satisfiable over R", str(sol2.check()), "sat")
ai, bi = z3.Ints('ai bi')
sol3 = z3.Solver(); sol3.add(bi > 0, bi <= 200, ai >= 0, ai <= 300, ai*ai == 2*bi*bi)
chk("z3 integer (bounded box b<=200, a<=300): no a^2 = 2b^2", str(sol3.check()), "unsat")
chk("sympy: sqrt(2).is_rational", sp.sqrt(2).is_rational, False)

print("C. positivity is strict but NOT uniform: the boundary mechanism")
r2 = sp.sqrt(2)
# lower bound |m r2 + n| >= 1/(|m| r2 + |n|) for m != 0 (since |2m^2 - n^2| >= 1)
# exact integer route: |m r2 + n| * |m r2 - n| = |2m^2 - n^2|, an integer, nonzero (part B) so >= 1,
# and |m r2 - n| <= |m| r2 + |n|; hence |m r2 + n| >= 1/(|m| r2 + |n|).  Check the integer factor.
viol = sum(1 for mm in range(1, 61) for nn in range(-100, 101) if abs(2*mm*mm - nn*nn) < 1)
chk("exact: |2m^2 - n^2| >= 1 on 1<=m<=60, |n|<=100, so |m sqrt2 + n| >= 1/(|m| sqrt2 + |n|)", viol, 0)
chk("sympy: (m sqrt2+n)(m sqrt2-n) == 2m^2 - n^2", sp.expand((m*r2+n)*(m*r2-n) - (2*m**2 - n**2)), 0)
# minimum of (m sqrt2 + n)^2 on the tree's box, exact convergent
best = min((((mm*r2 + nn)**2).evalf(40), mm, nn) for mm in range(1, 61) for nn in [-round(mm*math.sqrt(2))])
print("   box minimum of (m sqrt2 + n)^2 at (m,n) =", best[1:], "value =", sp.N(best[0], 20))
chk("box minimum is at the convergent 41/29", best[1:], (29, -41))
chk("box minimum >> 1e-12 (margin > 8 decades)", bool(sp.N(best[0], 30) > sp.Float('1e-4')), True)
# not stably causal: widen cones g_eps = g - eps dt^2 (invariant metric, descends to the quotient);
# lattice vector (m, m, m s + n) has g_eps-norm (m s + n)^2 - eps m^2.  Pell pairs make it < 0.
def pell(k):
    x, y = 1, 1   # x^2 - 2y^2 = -1, then alternate signs
    out = []
    for _ in range(k):
        out.append((x, y)); x, y = x + 2*y, x + y
    return out
res = []
for eps in [Fr(1, 100), Fr(1, 10**6), Fr(1, 10**12), Fr(1, 10**24)]:
    found = None
    for x, y in pell(200):
        # m = y, n = -x : (y sqrt2 - x)^2 = (2y^2 + x^2) - 2xy sqrt2 ; exact test via sympy
        val = (y*r2 - x)**2 - sp.Rational(eps.numerator, eps.denominator)*y**2
        if bool(sp.N(val, 200) < 0):
            found = (y, -x); break
    res.append(found is not None)
    print("   eps = %s : causal lattice vector for g_eps at (m,n) = %s" % (eps, found))
chk("every eps>0 tested admits a g_eps-causal lattice vector (not stably causal)", all(res), True)
# no global LINEAR time function descends: need a with <a,g1> = <a,g2> = 0 and a timelike
aa = sp.symbols('a0:3', real=True)
solset = sp.solve([ip(aa, g1), ip(aa, g2)], [aa[0], aa[2]], dict=True)[0]
anorm = sp.simplify(ip([solset.get(aa[0], aa[0]), aa[1], solset.get(aa[2], aa[2])],
                       [solset.get(aa[0], aa[0]), aa[1], solset.get(aa[2], aa[2])]))
chk("an L-invariant linear form's covector is null (norm 0), never timelike", anorm, 0)

print("D. the hypothesis is load-bearing: rational s gives a null lattice vector")
for p, q in [(1, 1), (3, 2), (7, 5), (41, 29)]:
    sv = sp.Rational(p, q)
    w = [q*x - p*y for x, y in zip([1, 1, sv], [0, 0, 1])]
    chk("s = %d/%d: q g1 - p g2 = %s is null (closed null curve)" % (p, q, w), sp.simplify(ip(w, w)), 0)

print("E. the tree's float stand-in is itself rational")
fs = Fr(math.sqrt(2.0))
chk("Fraction(math.sqrt(2.0)) has denominator 2^52", fs.denominator, 2**52)
M_, N_ = fs.denominator, -fs.numerator
chk("for s_float, (m,n) = (2^52, -%d) gives m s + n == 0 exactly" % fs.numerator, M_*fs + N_, 0)
# float check in the tree's own form, and exact check in the same box agree
flt = sum(1 for x in range(-60, 61) for y in range(-60, 61) if (x, y) != (0, 0) and (x*math.sqrt(2.0) + y)**2 <= 1e-12)
chk("tree's float check (|m|,|n|<=60, tol 1e-12) reproduces 0 hits", flt, 0)
# first m at which the float stand-in and sqrt2 part ways at tolerance 1e-12: |m s + n| <= 1e-6
# (Dirichlet: first convergent q with |q sqrt2 - p| <= 1e-6)
first = next((y, x) for x, y in pell(200) if abs(Fr(x) - y*fs) <= Fr(1, 10**6))
print("   smallest Pell m where the tolerance 1e-12 would fire:", first[0], "(box would need |m| >= that)")
chk("the tree's box (60) is far below the first tolerance hit", first[0] > 60, True)

print("F. measure zero: the degenerate set AC - H^2 = 0 is the zero set of a nonzero polynomial")
G = sp.symbols('u0:3'); K = sp.symbols('w0:3')
D = sp.expand(ip(G, G)*ip(K, K) - ip(G, K)**2)
chk("Gram determinant is a nonzero polynomial in the 6 generator entries", D != 0, True)

print("\nALL PASS" if ok else "\nSOME FAIL")
sys.exit(0 if ok else 1)
