#!/usr/bin/env python3
"""DOCKET 67 -- rederivation for key 'density-of-rationals'.
Reads research/warp-drive/latticectc.py (import by path, never edits it).
T1-T4 machine-check the external result (z3 / sympy); T5 checks the tree's
use (root interval, n != 0, vertex); T6 runs the owner's timelike_vector on a
census; T7 probes the implemented termination claim (float roots)."""
import importlib.util, math, random, signal, sys
from fractions import Fraction as Fr
import sympy as sp
import z3

OWNER = "/home/user/Claude-Method-Works/research/warp-drive/latticectc.py"
res = {}
def rec(k, v):
    res[k] = v; print("%-58s %s" % (k, v))

# T1: interval of length > 1 contains an integer: floor(x)+1 in (x, y)
x, y = z3.Reals("x y")
s = z3.Solver(); fl = z3.ToInt(x) + 1
s.add(y - x > 1, z3.Not(z3.And(x < fl, fl < y)))
rec("T1 y-x>1 => x < floor(x)+1 < y (z3; expect unsat)", s.check())

# T2: the owner's probe -- floor or ceil of the midpoint lies in (x,y) when y-x>1
# floor/ceil encoded as explicit integers (fl <= c < fl+1, ce-1 < c <= ce)
def t2(half_constraint):
    # interval (c-h, c+h).  floor(c) = c - d with 0 <= d < 1; ceil(c) = c if d == 0 else c + (1-d).
    # The claim is about distances only, so it is pure linear real arithmetic once d is named;
    # integrality of floor/ceil enters only through 0 <= d < 1 and ceil-floor in {0,1}.
    s = z3.Solver(); s.set("timeout", 60000)
    c, h, d = z3.Reals("c h d")
    f = c - d; ce = z3.If(d == 0, c, c + 1 - d)
    s.add(0 <= d, d < 1, half_constraint(h))
    s.add(z3.Not(z3.Or(z3.And(c - h < f, f < c + h), z3.And(c - h < ce, ce < c + h))))
    return s.check()
rec("T2 width>1 => floor(mid) or ceil(mid) in interval (z3; unsat)", t2(lambda h: h > z3.RealVal("1/2")))
rec("T2c control width=1/2 admits a miss (z3; expect sat)", t2(lambda h: h == z3.RealVal("1/4")))
rec("T2d control width=1 exactly admits a miss (z3; expect sat)", t2(lambda h: h == z3.RealVal("1/2")))

# T3: Archimedean step: w>0, q integer with q-1 <= 1/w < q (q=floor(1/w)+1) => q*w > 1;
# and then p = floor(q a)+1 gives a < p/q < b.  u stands for 1/w (u*w == 1).
w, a, b, u = z3.Reals("w a b u"); qI, pI = z3.Ints("qI pI")
qR, pR = z3.ToReal(qI), z3.ToReal(pI)
s = z3.Solver(); s.set("timeout", 60000)
s.add(w > 0, u * w == 1, qR - 1 <= u, u < qR, z3.Not(qR * w > 1))
rec("T3 w>0, q=floor(1/w)+1 => q*w > 1 (z3 nonlinear; unsat)", s.check())
s = z3.Solver(); s.set("timeout", 60000)
s.add(a < b, qR > 0, qR * (b - a) > 1, pR - 1 <= qR * a, qR * a < pR)
s.add(z3.Not(z3.And(qR * a < pR, pR < qR * b)))
rec("T3b q(b-a)>1, p=floor(qa)+1 => qa < p < qb (unsat)", s.check())

# T4: non-Archimedean control -- in R(eps) ordered at 0+, (0, eps) holds no positive rational
e, P, Qn = sp.symbols("epsilon P Q", positive=True)
lim = sp.limit(P / Qn - e, e, 0, "+")
rec("T4 R(eps): p/q - eps -> p/q > 0 as eps->0+ (no rational below eps)", lim)

# T5: the tree's use: Q(m,n) = n^2 (A t^2 + 2Ht + C), t=m/n; n=0 gives A m^2 >0
A, H, C, m, n, t = sp.symbols("A H C m n t", real=True)
Qf = A*m**2 + 2*H*m*n + C*n**2
rec("T5a Q(m,n) - n^2 q(m/n) == 0 (sympy)", sp.simplify(Qf - n**2*(A*(m/n)**2 + 2*H*(m/n) + C)))
r1, r2 = sp.solve(A*t**2 + 2*H*t + C, t)
rec("T5b root width^2 == 4(H^2-AC)/A^2 (sympy)", sp.simplify((r1 - r2)**2 - 4*(H**2 - A*C)/A**2))
rec("T5c q(vertex=-H/A) == (AC-H^2)/A (sympy)", sp.simplify((A*t**2 + 2*H*t + C).subs(t, -H/A) - (A*C - H**2)/A))
rec("T5d Q(m,0) == A m^2 (n=0 excluded when A>0)", sp.expand(Qf.subs(n, 0)))

# T6: the owner's routine on a census of exact-rational timelike spans
spec = importlib.util.spec_from_file_location("latticectc", OWNER)
L = importlib.util.module_from_spec(spec); spec.loader.exec_module(L)
tl = L.census(2026, "timelike", 400)
ok, worst = 0, 0.0
for g1, g2 in tl:
    mm, nn = L.timelike_vector(g1, g2)
    AA, CC, HH = L.gram(g1, g2)
    assert nn != 0 and L.nrm(L.add(g1, g2, mm, nn)) < 0
    width = 2 * math.sqrt(float(HH*HH - AA*CC)) / float(AA)
    bound = math.floor(1 / width) + 1          # first q with q*width > 1 (exact-real bound)
    worst = max(worst, abs(nn) / bound)        # <= 1 iff returned within the bound
    ok += 1
rec("T6 census: exact timelike (m,n), n!=0, of 400", ok)
rec("T6 max q_return / (floor(1/width)+1) over census (<=1 ok)", round(worst, 6))
e1, e2 = (Fr(9, 10), Fr(1), Fr(0), Fr(0)), (Fr(9, 10), Fr(0), Fr(1), Fr(0))
rec("T6 separating witness e1,e2 -> (m,n)", L.timelike_vector(e1, e2))

# T7: exact vertex is inside for rational Gram entries -- density not needed there
AA, CC, HH = L.gram(e1, e2)
v = -HH / AA
rec("T7a witness vertex -H/A (rational), q(vertex)<0", (v, AA*v*v + 2*HH*v + CC < 0))

# T8: termination of the float-rooted loop.  Valid input (A>0, H^2>AC, spacelike gens):
M = Fr(10**17 + 7)
g1 = (Fr(0), Fr(1), Fr(0)); g2 = (Fr(1, 2), -M, Fr(0))
AA, CC, HH = L.gram(g1, g2)
rec("T8 input: A, H^2-AC, nrm(g1)>0, nrm(g2)>0", (AA, HH*HH - AA*CC, L.nrm(g1) > 0, L.nrm(g2) > 0))
rec("T8 exact: integer m=M, n=1 gives Q<0 (density/vertex holds)", AA*M*M + 2*HH*M*1 + CC < 0)
def capped(g1, g2, qmax):   # the owner's loop verbatim, with a cap
    A_, C_, H_ = L.gram(g1, g2)
    D = math.sqrt(float(H_*H_ - A_*C_))
    lo, hi = (-float(H_) - D) / float(A_), (-float(H_) + D) / float(A_)
    for q in range(1, qmax + 1):
        for p in (math.floor(q*(lo+hi)/2), math.ceil(q*(lo+hi)/2)):
            if A_*p*p + 2*H_*p*q + C_*q*q < 0:
                return p, q
    return None
cp = capped(g1, g2, 200000)
rec("T8 capped copy of owner loop, q <= 200000 -> ", cp)
if cp:
    pp, qq_ = cp
    rec("T8 returned q vs docstring bound 'q > 2/width' (=q 3) and exact bound 2", (qq_, "exceeds" if qq_ > 3 else "within"))
    rec("T8 |p - q*M| vs half-width q/2 (exact)", (abs(Fr(pp) - qq_*M), Fr(qq_, 2)))
def alarm(*_): raise TimeoutError
signal.signal(signal.SIGALRM, alarm); signal.alarm(10)
try:
    out = L.timelike_vector(g1, g2); signal.alarm(0)
    rec("T8 owner timelike_vector (10 s)", out)
except TimeoutError:
    rec("T8 owner timelike_vector (10 s)", "NO RETURN in 10 s; docstring bound 2/width = 2")
