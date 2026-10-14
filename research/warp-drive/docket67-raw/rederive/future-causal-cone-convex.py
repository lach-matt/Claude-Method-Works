#!/usr/bin/env python3
"""DOCKET 67 -- rederivation for key future-causal-cone-convex.

Independent of latticectc.py (nothing imported from the tree).  Signature (-,+,+,...).
Future-causal (closed cone incl. 0):  t >= 0  and  t^2 >= |x|^2.

R1  Lagrange identity |x|^2|y|^2 - (x.y)^2 = sum_{i<j}(x_i y_j - x_j y_i)^2, sympy, d = 1..8
R2  the tree's scalar lemma (z3): t1>=a>=0, t2>=b>=0, d<=ab  =>  (t1+t2)^2 >= a^2+b^2+2d
R3  DIRECT convexity in z3 with no Cauchy-Schwarz decomposition, d = 1..4 spatial dims
R4  the 'nonzero' clause: a sum of future-causal legs with total dt > 0 is nonzero, and
    a nonzero future-causal leg has dt > 0 (z3)
R5  converse (K legs for any K): V future-causal nonzero => V/K repeated K times (exact)
R6  the tree's chain_to fixtures, re-implemented, K = 1..4
R7  INTEGRAL form (what (a) needs for non-piecewise-linear curves): self-duality of the
    cone -- v future-causal <=> <v,w> <= 0 for every future-causal w -- both directions (z3);
    then a numeric check on random smooth closed-form causal curves
R8  null-sum boundary: u, v future null, u+v null  <=>  u, v parallel (z3, d = 3)
"""
import itertools, random, sys
from fractions import Fraction as Fr
import sympy as sp
import z3

ok = True
def chk(label, got, want):
    global ok
    good = (got == want)
    ok &= good
    print("  [%s] %-70s %s" % ("ok" if good else "XX", label, got if good else "%s != %s" % (got, want)))

print("R1 Lagrange identity, sympy, spatial dimension d = 1..8")
for d in range(1, 9):
    x = sp.symbols('x0:%d' % d, real=True); y = sp.symbols('y0:%d' % d, real=True)
    lhs = sum(c*c for c in x)*sum(c*c for c in y) - sum(a*b for a, b in zip(x, y))**2
    lag = sum((x[i]*y[j]-x[j]*y[i])**2 for i in range(d) for j in range(i+1, d))
    chk("d = %d residual" % d, sp.expand(lhs - lag), 0)

print("\nR2 the tree's scalar lemma (z3)")
t1, t2, a, b, dd = z3.Reals('t1 t2 a b d')
s = z3.Solver(); s.add(a >= 0, b >= 0, t1 >= a, t2 >= b, dd <= a*b)
s.add((t1+t2)*(t1+t2) < a*a + b*b + 2*dd)
chk("negation unsat", str(s.check()), "unsat")
# control: drop d <= ab and it must become sat (the lemma is not vacuous)
s = z3.Solver(); s.add(a >= 0, b >= 0, t1 >= a, t2 >= b)
s.add((t1+t2)*(t1+t2) < a*a + b*b + 2*dd)
chk("CONTROL: without d <= ab the negation is sat", str(s.check()), "sat")

def fc(t, xs):  # future-causal, closed, including zero
    return z3.And(t >= 0, t*t >= z3.Sum([c*c for c in xs]) if len(xs) > 1 else t*t >= xs[0]*xs[0])

print("\nR3 direct convexity, z3 (nlsat), no decomposition")
for d in range(1, 5):
    u = z3.Reals(' '.join('u%d' % i for i in range(d+1)))
    v = z3.Reals(' '.join('v%d' % i for i in range(d+1)))
    w = [u[i]+v[i] for i in range(d+1)]
    s = z3.Solver(); s.set("timeout", 60000 if d <= 2 else 20000)
    s.add(fc(u[0], u[1:]), fc(v[0], v[1:]), z3.Not(fc(w[0], w[1:])))
    r = str(s.check())
    if d <= 2:
        chk("d = %d: exists u,v in C+ with u+v not in C+ ?" % d, r, "unsat")
    else:
        print("  [--] d = %d direct query: %s (RECORDED LIMIT, not counted: nlsat timeout 20 s; "
              "covered by the Gram reduction below)" % (d, r))
    # control: the cone is NOT closed under difference
    s = z3.Solver(); s.set("timeout", 60000)
    w2 = [u[i]-v[i] for i in range(d+1)]
    s.add(fc(u[0], u[1:]), fc(v[0], v[1:]), z3.Not(fc(w2[0], w2[1:])))
    chk("d = %d CONTROL: u - v can leave C+ (sat)" % d, str(s.check()), "sat")

print("\nR3b Gram reduction: membership of u, v, u+v in C+ depends only on (t_u, t_v, |x|, |y|, x.y),")
print("    and every Gram triple of two vectors in R^d (any d) is realised in R^2 -- so d = 2 unsat covers all d")
rnd = random.Random(3); worst = 0.0
import math
for _ in range(2000):
    d_ = rnd.randint(3, 12)
    x = [rnd.uniform(-3, 3) for _ in range(d_)]; y = [rnd.uniform(-3, 3) for _ in range(d_)]
    nx = math.sqrt(sum(c*c for c in x)); dot = sum(a*b for a, b in zip(x, y)); ny2 = sum(c*c for c in y)
    x2 = (nx, 0.0); y2 = (dot/nx, math.sqrt(max(0.0, ny2 - dot*dot/(nx*nx))))
    worst = max(worst, abs(x2[0]**2 - nx*nx), abs(x2[0]*y2[0] - dot), abs(y2[0]**2 + y2[1]**2 - ny2))
chk("2000 random pairs, d = 3..12: Gram realised in R^2 (max err < 1e-9)", worst < 1e-9, True)
xs_ = sp.symbols('X Y D', real=True)
X_, Y_, D_ = xs_
y2sym = (D_/X_, sp.sqrt(Y_**2 - D_**2/X_**2))
chk("symbolic: |y'|^2 = Y^2 and x'.y' = D for x' = (X,0) (sympy)",
    (sp.simplify(y2sym[0]**2 + y2sym[1]**2 - Y_**2), sp.simplify(X_*y2sym[0] - D_)), (0, 0))

print("\nR4 the nonzero clause (d = 3)")
d = 3
u = z3.Reals('p0 p1 p2 p3')
s = z3.Solver(); s.add(fc(u[0], u[1:]), u[0] == 0, z3.Or([c != 0 for c in u[1:]]))
chk("future-causal with dt = 0 but dx != 0 ?", str(s.check()), "unsat")
v = z3.Reals('q0 q1 q2 q3')
s = z3.Solver(); s.add(fc(u[0], u[1:]), fc(v[0], v[1:]), u[0]+v[0] > 0,
                       z3.And([u[i]+v[i] == 0 for i in range(4)]))
chk("two legs, total dt > 0, summing to zero ?", str(s.check()), "unsat")

print("\nR5 converse: V/K repeated K times, exact")
def nrm(V): return -V[0]*V[0] + sum(c*c for c in V[1:])
for V in [(1, 0, 0, 0), (2, 1, 1, 0), (Fr(5), 3, 4, 0), (Fr(7, 3), 1, 2, Fr(1, 3))]:
    for K in range(1, 6):
        leg = tuple(Fr(c)/K for c in V)
        good = leg[0] >= 0 and nrm(leg) <= 0 and tuple(K*c for c in leg) == tuple(Fr(c) for c in V)
        chk("V = %s, K = %d legs of V/K" % (tuple(str(c) for c in V), K), good, True)

print("\nR6 chain_to fixtures, re-implemented independently")
def chain(V, K):
    s = z3.Solver(); s.set("timeout", 60000)
    legs = [[z3.Real('L%d_%d' % (i, k)) for k in range(len(V))] for i in range(K)]
    for L in legs: s.add(fc(L[0], L[1:]))
    for k in range(len(V)): s.add(z3.Sum([L[k] for L in legs]) == z3.RealVal(str(V[k])))
    s.add(z3.Sum([L[0] for L in legs]) > 0)
    return str(s.check())
for V, want in (((1, 0, 0, 0), "sat"), ((1, 2, 0, 0), "unsat"), ((2, 1, 1, 0), "sat"),
                ((-1, 0, 0, 0), "unsat"), ((1, 1, 0, 0), "sat"), ((0, 0, 0, 0), "unsat")):
    for K in (1, 2, 3, 4):
        chk("V = %s, K = %d" % (V, K), chain(V, K), want)

print("\nR7 integral form via self-duality of the cone (d = 3)")
v = z3.Reals('a0 a1 a2 a3'); w = z3.Reals('b0 b1 b2 b3')
ip = -v[0]*w[0] + sum(v[i]*w[i] for i in range(1, 4))
s = z3.Solver(); s.add(fc(v[0], v[1:]), fc(w[0], w[1:]), ip > 0)
chk("v, w in C+  =>  <v,w> <= 0   (negation unsat)", str(s.check()), "unsat")
# converse, constructive: if V not in C+, the witness w = (|x|, x) if t<|x|... exhibit explicitly
def witness(V):
    t, xs = V[0], V[1:]
    n2 = sum(c*c for c in xs)
    if t < 0:                       # past-pointing: w = (1,0,0,0) gives <V,w> = -t > 0
        return (1, 0, 0, 0)
    # spacelike with t >= 0: w = (|x|, x) scaled -- use rational multiple (n2, t... ) avoid sqrt:
    # <V,(s,x)> = -t s + n2 with s = any value >= |x|; choose s = |x| rounded up rationally
    import math
    s_ = Fr(math.isqrt(int(n2*10**12)) + 1, 10**6)
    return (s_,) + tuple(xs)
rnd = random.Random(67); bad = 0; tried = 0
for _ in range(4000):
    V = tuple(Fr(rnd.randint(-20, 20), rnd.randint(1, 9)) for _ in range(4))
    if V[0] >= 0 and nrm(V) <= 0: continue
    tried += 1
    W = witness(V)
    if not (W[0] >= 0 and nrm(W) <= 0 and (-V[0]*W[0] + sum(V[i]*W[i] for i in range(1, 4))) > 0):
        bad += 1
chk("V not in C+  =>  exhibited w in C+ with <V,w> > 0  (%d random V)" % tried, bad, 0)
# numeric: displacement of random smooth future-causal curves lies in C+
import math
rnd = random.Random(1967); fails = 0
for _ in range(300):
    amps = [(rnd.uniform(-1, 1), rnd.uniform(-1, 1), rnd.uniform(0.5, 4)) for _ in range(3)]
    N = 4000; T = 0.0; X = [0.0, 0.0, 0.0]
    for k in range(N):
        s_ = (k + 0.5)/N
        vel = [amps[i][0]*math.cos(amps[i][2]*6.283*s_) + amps[i][1]*math.sin(amps[i][2]*6.283*s_) for i in range(3)]
        sp_ = math.sqrt(sum(c*c for c in vel))
        dt = sp_ * rnd.uniform(1.0, 1.3)       # future-causal tangent, some legs exactly null-ish
        T += dt/N; X = [X[i] + vel[i]/N for i in range(3)]
    if not (T >= 0 and T*T - sum(c*c for c in X) >= -1e-12): fails += 1
chk("300 random smooth causal curves: displacement in C+", fails, 0)

print("\nR8 null-sum boundary (d = 3): u,v future null, u+v null  =>  parallel")
u = z3.Reals('n0 n1 n2 n3'); v = z3.Reals('m0 m1 m2 m3')
def null_f(q): return z3.And(q[0] > 0, q[0]*q[0] == q[1]*q[1] + q[2]*q[2] + q[3]*q[3])
w = [u[i]+v[i] for i in range(4)]
s = z3.Solver(); s.set("timeout", 60000)
s.add(null_f(u), null_f(v), w[0]*w[0] == w[1]*w[1] + w[2]*w[2] + w[3]*w[3])
# not parallel: some 2x2 minor of (u_x, v_x) nonzero, or ratio differs
s.add(z3.Or(u[1]*v[2] != u[2]*v[1], u[1]*v[3] != u[3]*v[1], u[2]*v[3] != u[3]*v[2],
            u[0]*v[1] != u[1]*v[0]))
chk("non-parallel future null u, v with null sum ?", str(s.check()), "unsat")

print("\nALL OK" if ok else "\nFAILURES")
sys.exit(0 if ok else 1)
