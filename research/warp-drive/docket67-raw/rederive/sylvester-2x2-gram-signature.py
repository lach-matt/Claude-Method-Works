#!/usr/bin/env python3
"""DOCKET 67 re-derivation: sylvester-2x2-gram-signature (latticectc.py:40-47, 187-200, 381-393).

Claim as used: for g1, g2 in R^{1,d} (signature -,+,...,+) with A=|g1|^2>0, C=|g2|^2>0,
H=<g1,g2>, Q(m,n)=A m^2+2H mn+C n^2:
  (i)  span timelike  iff H^2 > AC; then Q<0 on the open interval between roots of A t^2+2Ht+C,
       which contains a rational m/n, so the lattice Z g1 + Z g2 holds a timelike vector;
  (ii) AC > H^2 -> Q positive definite -> no nonzero causal lattice vector.
Checks below are independent of the tree; section F calls the tree's own functions READ-ONLY.
Exit 0 iff every check agrees.
"""
import sys, random, itertools, importlib.util
from fractions import Fraction as Fr
import sympy as sp

OK = True
def chk(label, got, want):
    global OK
    good = (got == want)
    OK &= good
    print(("PASS " if good else "FAIL ") + label + "  -> " + repr(got))

# ---------------------------------------------------------------- A. binary form algebra (sympy)
A, C, H, m, n, t = sp.symbols('A C H m n t', real=True)
Q = A*m**2 + 2*H*m*n + C*n**2
# completing the square: A*Q = (A m + H n)^2 + (AC - H^2) n^2
chk("A1 A*Q == (A m + H n)^2 + (AC-H^2) n^2 (identity)",
    sp.expand(A*Q - ((A*m + H*n)**2 + (A*C - H**2)*n**2)), 0)
# roots of A t^2 + 2 H t + C
tp = (-H + sp.sqrt(H**2 - A*C))/A; tm = (-H - sp.sqrt(H**2 - A*C))/A
chk("A2 t+ and t- are roots", [sp.simplify(A*r**2 + 2*H*r + C) for r in (tp, tm)], [0, 0])
# midpoint value: q(-H/A) = C - H^2/A = -(H^2-AC)/A < 0 when A>0, H^2>AC
chk("A3 q(-H/A) == -(H^2-AC)/A", sp.simplify((A*t**2 + 2*H*t + C).subs(t, -H/A) + (H**2 - A*C)/A), 0)
# Q(m,n) = n^2 q(m/n)
chk("A4 Q(m,n) == n^2 q(m/n)", sp.simplify(Q - n**2*(A*t**2 + 2*H*t + C).subs(t, m/n)), 0)

# ---------------------------------------------------------------- B. signature identity in R^{1,d}
# AC - H^2 = sum_{i<j spatial}(x_i y_j - x_j y_i)^2 - sum_i (x_0 y_i - y_0 x_i)^2  (Cauchy-Binet, signed)
def ip(a, b): return -a[0]*b[0] + sum(a[i]*b[i] for i in range(1, len(a)))
for d in (1, 2, 3, 4):
    x = sp.symbols('x0:%d' % (d+1), real=True); y = sp.symbols('y0:%d' % (d+1), real=True)
    lhs = ip(x, x)*ip(y, y) - ip(x, y)**2
    rhs = sum((x[i]*y[j] - x[j]*y[i])**2 for i in range(1, d+1) for j in range(i+1, d+1)) \
        - sum((x[0]*y[i] - y[0]*x[i])**2 for i in range(1, d+1))
    chk("B1 signed Cauchy-Binet for Gram det, d=%d" % d, sp.expand(lhs - rhs), 0)

# ---------------------------------------------------------------- C. z3: inertia facts for d = 1..3
import z3
def vec(nm, d): return [z3.Real('%s%d' % (nm, i)) for i in range(d+1)]
def zip_(a, b): return -a[0]*b[0] + z3.Sum([a[i]*b[i] for i in range(1, len(a))])
for d in (1, 2, 3):
    g1, g2 = vec('g', d), vec('h', d)
    a_, c_, h_ = zip_(g1, g1), zip_(g2, g2), zip_(g1, g2)
    # C1: no negative-definite 2-plane (law of inertia, one negative direction): A<0 & AC-H^2>0 unsat
    s = z3.Solver(); s.set('timeout', 60000)
    s.add(a_ < 0, a_*c_ - h_*h_ > 0)
    chk("C1 z3: no 2-plane with A<0 and AC-H^2>0 in R^{1,%d}" % d, str(s.check()), 'unsat')
    # C3: H^2>AC and Q(p,q)>=0 for the specific midpoint (p,q)=(-H, A) -> unsat when A>0
    s = z3.Solver(); s.set('timeout', 60000)
    s.add(a_ > 0, h_*h_ > a_*c_, a_*h_*h_ - 2*h_*h_*a_ + c_*a_*a_ >= 0)
    chk("C3 z3: A>0, H^2>AC => Q(-H,A)<0 (the span holds a timelike vector), R^{1,%d}" % d,
        str(s.check()), 'unsat')

    # C2: A>0, AC-H^2>0, some (p,q)!=(0,0) real with Q(p,q)<=0  -> unsat (positive definite)
    #     vector-level only for d<=2 (nlsat times out at d=3); C2s below is the scalar form, all d
    if d > 2:
        continue
    p, q = z3.Reals('p q')
    s = z3.Solver(); s.set('timeout', 60000)
    s.add(a_ > 0, a_*c_ - h_*h_ > 0, z3.Or(p != 0, q != 0), a_*p*p + 2*h_*p*q + c_*q*q <= 0)
    chk("C2 z3: A>0, AC>H^2 => Q>0 on all real (p,q)!=0, R^{1,%d}" % d, str(s.check()), 'unsat')
# C2s: scalar form, independent of d: reals A,C,H,p,q with A>0, AC>H^2, (p,q)!=0, Q<=0 -> unsat
Az, Cz, Hz, pz, qz = z3.Reals('Az Cz Hz pz qz')
s = z3.Solver(); s.set('timeout', 60000)
s.add(Az > 0, Az*Cz - Hz*Hz > 0, z3.Or(pz != 0, qz != 0), Az*pz*pz + 2*Hz*pz*qz + Cz*qz*qz <= 0)
chk("C2s z3 (scalar, every d): A>0, AC>H^2 => Q(p,q)>0 for all real (p,q)!=0", str(s.check()), 'unsat')
# C4s: H^2>AC (any sign of A) => exists real (p,q) with Q<0 : negation unsat
s = z3.Solver(); s.set('timeout', 60000)
s.add(Hz*Hz > Az*Cz, z3.ForAll([pz, qz], Az*pz*pz + 2*Hz*pz*qz + Cz*qz*qz >= 0))
chk("C4s z3 (scalar): H^2>AC => Q indefinite (takes a negative value)", str(s.check()), 'unsat')

# ---------------------------------------------------------------- D. independent exact census
def nrm(v): return ip(v, v)
def gram(a, b): return nrm(a), nrm(b), ip(a, b)
def rational_in(Af, Hf, Cf):
    """exact: smallest-denominator search for p/q with Q(p,q)<0 using Fraction bisection bounds."""
    q = 1
    while True:
        # integer p nearest q*(-H/A) -- the vertex -- is tried; succeeds once q*width>2
        c = Fr(-Hf) * q / Af
        for p in (c.numerator // c.denominator, -((-c.numerator) // c.denominator)):
            if Af*p*p + 2*Hf*p*q + Cf*q*q < 0:
                return p, q
        q += 1
rnd = random.Random(1867)
tl = sl = 0; tl_ok = sl_ok = True; dim = 3
while tl < 400 or sl < 400:
    g1 = tuple(Fr(rnd.randint(-9, 9), rnd.randint(1, 7)) for _ in range(dim))
    g2 = tuple(Fr(rnd.randint(-9, 9), rnd.randint(1, 7)) for _ in range(dim))
    a, c, h = gram(g1, g2)
    if not (a > 0 and c > 0):
        continue
    if h*h > a*c and tl < 400:
        tl += 1
        p, q = rational_in(a, h, c)
        v = tuple(p*x + q*y for x, y in zip(g1, g2))
        tl_ok &= nrm(v) < 0
    elif a*c > h*h and sl < 400:
        sl += 1
        # brute control: no causal lattice vector in |m|,|n|<=15
        sl_ok &= not any(nrm(tuple(i*x + j*y for x, y in zip(g1, g2))) <= 0
                         for i in range(-15, 16) for j in range(-15, 16) if (i, j) != (0, 0))
chk("D1 independent census seed 1867: 400 timelike spans, exact timelike lattice vector in all", tl_ok, True)
chk("D2 independent census seed 1867: 400 spacelike spans, no causal vector |m|,|n|<=15", sl_ok, True)

# ---------------------------------------------------------------- E. scope findings (not refutations)
# E1: the tree's separating witness
e1 = (Fr(9, 10), Fr(1), Fr(0), Fr(0)); e2 = (Fr(9, 10), Fr(0), Fr(1), Fr(0))
chk("E1 witness Gram (A,C,H) and |e1+e2|^2", (gram(e1, e2), nrm(tuple(x+y for x, y in zip(e1, e2)))),
    ((Fr(19, 100), Fr(19, 100), Fr(-81, 100)), Fr(-31, 25)))
# E2: degenerate span with RATIONAL Gram entries (the entry's own hypothesis) always holds a
# null lattice vector: Q(-H, A) = A(AC - H^2) = 0.
chk("E2 sympy: Q(-H,A) == A*(AC-H^2)", sp.expand(Q.subs({m: -H, n: A}) - A*(A*C - H**2)), 0)
d1 = (Fr(0), Fr(1), Fr(0)); d2 = (Fr(1), Fr(1), Fr(1))
a, c, h = gram(d1, d2)
chk("E2 example g1=(0,1,0), g2=(1,1,1): A=C=H=1, degenerate", (a, c, h, a*c - h*h), (1, 1, 1, 0))
chk("E2 ... and the lattice vector g2-g1=(1,0,1) is NULL (closed causal, non-timelike, curve)",
    nrm(tuple(y - x for x, y in zip(d1, d2))), 0)
# E2': the tree's irrational boundary: g1=(1,1,s), g2=(0,0,1): Gram (s^2, 1, s), null direction -H/A=-1/s
s_ = sp.symbols('s', positive=True)
b1 = (1, 1, s_); b2 = (0, 0, 1)
chk("E2' boundary Gram det is 0 identically", sp.expand(ip(b1, b1)*ip(b2, b2) - ip(b1, b2)**2), 0)
# E3: rank 3: pairwise-spacelike 2-spans do NOT make the rank-3 span spacelike (so the 2x2 test
#     is a rank-2 statement; for n>=3 the full Gram matrix is needed -- Sylvester on n x n).
def pair_sl(a_, b_):
    A_, C_, H_ = gram(a_, b_); return A_ > 0 and A_*C_ > H_*H_
found = None
rnd = random.Random(3)
for _ in range(200000):
    gs = [tuple(Fr(rnd.randint(-6, 6), rnd.randint(1, 3)) for _ in range(4)) for _ in range(3)]
    if all(pair_sl(a_, b_) for a_, b_ in itertools.combinations(gs, 2)):
        for co in itertools.product(range(-3, 4), repeat=3):
            if any(co):
                v = tuple(sum(k*g[i] for k, g in zip(co, gs)) for i in range(4))
                if nrm(v) < 0:
                    found = (gs, co, nrm(v)); break
    if found:
        break
print("     rank-3 example:", found)
if found:
    G = sp.Matrix(3, 3, lambda i, j: sp.Rational(ip(found[0][i], found[0][j])))
    lead = [G[:k, :k].det() for k in (1, 2, 3)]
    print("     its 3x3 Gram leading minors:", lead)
    chk("E3 rank 3: all three 2-spans spacelike yet a timelike lattice vector exists", found is not None, True)
    chk("E3 ... and Sylvester on the FULL 3x3 Gram detects it (det < 0)", lead[2] < 0, True)

# ---------------------------------------------------------------- F. the tree's own functions, read-only
spec = importlib.util.spec_from_file_location(
    "latticectc", "/home/user/Claude-Method-Works/research/warp-drive/latticectc.py")
L = importlib.util.module_from_spec(spec)
try:
    spec.loader.exec_module(L)
    tl7 = L.census(7, "timelike", 400); sl23 = L.census(23, "spacelike", 400)
    chk("F1 tree census(7) timelike_vector exact-negative in all 400",
        all(L.nrm(L.add(g1, g2, *L.timelike_vector(g1, g2))) < 0 for g1, g2 in tl7), True)
    chk("F2 tree census(23): A>0, AC>H^2 in all 400",
        all(L.gram(a_, b_)[0] > 0 and L.gram(a_, b_)[0]*L.gram(a_, b_)[1] > L.gram(a_, b_)[2]**2
            for a_, b_ in sl23), True)
    chk("F3 tree span_kind on E2 rational degenerate example", L.span_kind(d1, d2), "degenerate")
except Exception as ex:  # pragma: no cover
    OK = False
    print("FAIL F: could not load tree module read-only:", ex)

print("\nALL AGREE" if OK else "\nDISAGREEMENT")
sys.exit(0 if OK else 1)
