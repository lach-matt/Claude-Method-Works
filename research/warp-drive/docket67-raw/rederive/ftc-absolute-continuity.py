#!/usr/bin/env python3
"""DOCKET 67 -- ftc-absolute-continuity.  Re-derivation of the integration step
tolman.py:932-936 cites:  d/dr(r^3 p_r) = r^2 u  ==>  m(R) = 4 pi R^3 p_r(R),
m(R) := 4 pi INT_0^R r^2 u dr.   sympy + exact Fractions; stdlib + sympy only.

  T1  FTC on [eps, R] + limit L at 0  ==>  m(R) = 4 pi (R^3 p_r(R) - L).   (sympy, general F)
  T2  'a limit at 0' is NOT sufficient; the limit must be ZERO.  The tree's own
      independence_witness (tolman.py:1380, V32): r^3 p_r = A, AC on (0,R],
      limit A exists, yet m = 0 != 4 pi A.
  T3  'regular centre' (r^3 p_r -> 0, AC) does NOT imply 'p_r finite at the centre':
      the tree's own W3 (tolman.py:584) p_r = -2 + 10 r^(-5/2).
  T4  'p_r finite at the centre' does NOT imply the identity: p_r = Cantor(r),
      bounded, r^3 p_r -> 0, ODE holds a.e. with u = 3 Cantor(r), but
      m(1)/(4 pi) = 11/16 != 1 = 1^3 p_r(1).  (exact via Cantor-measure moments,
      and numerically).  Absolute continuity is load-bearing -- IF the ODE is only
      required almost everywhere.
  T5  If the ODE holds at EVERY r in (0,R] (differentiable fields, the tree's V2/V3
      setting), F := m - 4 pi r^3 p_r has F' = 0 everywhere, hence constant by the
      mean-value theorem -- no absolute continuity needed; AC is then equivalent to
      r^2 u in L^1 (Rudin RCA Thm 7.21, NAMED-NOT-READ).
  T6  Locally-AC + limit at 0 gives the identity with m an IMPROPER integral, not
      necessarily a Lebesgue one: F = r^3 p_r = r^2 sin(r^-2): lim 0, differentiable
      on (0,R], INT_eps^R F' -> F(R), but INT_eps^R |F'| diverges (log).
"""
import sys
from fractions import Fraction as Fr
import sympy as sp

ok = True
def chk(label, cond):
    global ok
    print(("PASS  " if cond else "FAIL  ") + label)
    ok = ok and bool(cond)

r, R, eps, A = sp.symbols("r R epsilon A", positive=True)

# T1 -- general F = r^3 p_r, u := F'/r^2
F = sp.Function("F")
integrand = r**2 * (sp.diff(F(r), r) / r**2)
I = sp.integrate(sp.simplify(integrand), (r, eps, R))
chk("T1  INT_eps^R r^2 u dr == F(R) - F(eps)  (FTC on a compact subinterval)",
    sp.simplify(I - (F(R) - F(eps))) == 0)
L = sp.Symbol("L")
m_over_4pi = (F(R) - L)   # eps -> 0 with F(eps) -> L
chk("T1  => m(R)/(4 pi) = R^3 p_r(R) - L ; identity iff L == 0",
    sp.solve(sp.Eq(m_over_4pi, F(R)), L) == [0])

# T2 -- independence witness (tree's own V32)
pr2 = A / r**3
u2 = sp.simplify(sp.diff(r**3 * pr2, r) / r**2)
m2 = 4*sp.pi*sp.integrate(r**2 * u2, (r, 0, R))
lim2 = sp.limit(r**3 * pr2, r, 0, "+")
chk("T2  witness p_r = A/r^3: u == 0, limit of r^3 p_r exists (= A)", u2 == 0 and lim2 == A)
chk("T2  ... m(R) == 0 while 4 pi R^3 p_r = 4 pi A: the identity is off by -4 pi A",
    sp.simplify(m2) == 0 and sp.simplify(4*sp.pi*R**3*pr2.subs(r, R) - m2) == 4*sp.pi*A)
print("      => the hypothesis as WORDED at tolman.py:935 ('with a limit at 0') is "
      "INSUFFICIENT; the limit must be 0 (C = 0), as FULL at tolman.py:2055 encodes.")

# T3 -- W3: regular centre with p_r infinite at the centre
pr3 = -2 + 10 * r**sp.Rational(-5, 2)
chk("T3  W3: lim r^3 p_r = 0 (regular centre) yet p_r -> +oo at r -> 0",
    sp.limit(r**3*pr3, r, 0, "+") == 0 and sp.limit(pr3, r, 0, "+") == sp.oo)
u3 = sp.simplify(sp.diff(r**3*pr3, r)/r**2)
m3 = sp.integrate(r**2*u3, (r, 0, 1))
chk("T3  ... and the identity holds for W3: m(1)/(4 pi) == 1^3 p_r(1) == 8",
    sp.simplify(m3 - pr3.subs(r, 1)) == 0 and pr3.subs(r, 1) == 8)
print("      => 'regular centre is STRONGER than p_r finite at the centre' "
      "(tolman.py:936) holds only as 'finiteness does not suffice' (T4); as an "
      "implication it fails (T3).  The two are INCOMPARABLE.")

# T4 -- Cantor function: bounded p_r, identity fails
# Cantor measure mu: X = (2B + X')/3, B ~ Bernoulli(1/2).  Moments exactly:
def cantor_moments(n):
    M = [Fr(1)]
    for k in range(1, n+1):
        # E[X^k] = 3^-k * sum_j C(k,j) E[(2B)^j] E[X^(k-j)] ; E[(2B)^j] = 2^j/2 (j>=1), 1 (j=0)
        s = Fr(0)
        from math import comb
        for j in range(1, k+1):
            s += comb(k, j) * Fr(2**j, 2) * M[k-j]
        # E[X^k](1 - 3^-k) = 3^-k * s
        M.append(s / (3**k - 1))
    return M
M = cantor_moments(3)
chk("T4  Cantor-measure moments exact: E[X]=1/2, E[X^2]=3/8, E[X^3]=5/16",
    M[1:] == [Fr(1, 2), Fr(3, 8), Fr(5, 16)])
# INT_0^1 3 r^2 c(r) dr = [r^3 c]_0^1 - INT r^3 dc = 1 - E[X^3]
val = 1 - M[3]
chk("T4  m(1)/(4 pi) = INT_0^1 r^2 u = INT_0^1 3 r^2 c(r) dr = 11/16 != 1 = 1^3 p_r(1)",
    val == Fr(11, 16) and val != 1)
# correct digit map: base-3 digit 2 -> binary 1 at this scale
def cantor2(x, depth=45):
    y, s = 0.0, 0.5
    for _ in range(depth):
        x *= 3
        d = int(x)
        if d == 1: return y + s
        if d == 2: y += s
        x -= d
        s /= 2
    return y
N = 200000
num = sum(3*((k+0.5)/N)**2 * cantor2((k+0.5)/N) for k in range(N)) / N
chk("T4  numeric midpoint sum of INT_0^1 3 r^2 c(r) dr = %.6f  (11/16 = 0.6875)" % num,
    abs(num - 0.6875) < 1e-4)
print("      => 'p_r finite at the centre' does not suffice when the ODE holds only a.e.; "
      "absolute continuity of r^3 p_r is load-bearing there, as tolman.py:935 says.")

# T5 -- everywhere-differentiable: MVT route
Fm = sp.Function("m"); P = sp.Function("p")
Fexpr = Fm(r) - 4*sp.pi*r**3*P(r)
on_shell = {sp.Derivative(Fm(r), r): 4*sp.pi*r**2*(sp.diff(r**3*P(r), r)/r**2)}
dF = sp.simplify(sp.diff(Fexpr, r).subs(on_shell))
chk("T5  on shell (dm/dr = 4 pi r^2 u, u = (r^3 p_r)'/r^2 pointwise) dF/dr == 0 identically",
    dF == 0)

# T6 -- locally AC, limit 0, derivative not L^1 near 0
G = r**2 * sp.sin(r**-2)
dG = sp.diff(G, r)
chk("T6  G = r^2 sin(r^-2): lim_{r->0} G = 0", sp.limit(G, r, 0, "+") == 0)
t = sp.symbols("t", positive=True)
# |G'| >= (2/r)|cos(r^-2)| - 2r ; with t = r^-2, INT (2/r)|cos r^-2| dr = INT |cos t| / t dt
sub = sp.simplify((2/r).subs(r, t**sp.Rational(-1, 2)) * sp.Abs(sp.diff(t**sp.Rational(-1, 2), t)))
chk("T6  substitution t = r^-2 maps (2/r) dr to dt/t (so INT |G'| ~ INT |cos t|/t dt = oo)",
    sp.simplify(sub - 1/t) == 0)
import math
def absint(e, Rr=1.0, n=400000):
    # INT_e^R |G'(r)| dr by t-substitution: INT_{R^-2}^{e^-2} |G'(t^-1/2)| /(2 t^1.5) dt
    a, b = Rr**-2, e**-2
    h = (b - a)/n; s = 0.0
    for k in range(n):
        tt = a + (k+0.5)*h; rr = tt**-0.5
        g = 2*rr*math.sin(tt) - 2*math.cos(tt)/rr
        s += abs(g) / (2*tt**1.5)
    return s*h
vals = [absint(e) for e in (1e-1, 1e-2)]
signed = [float(G.subs(r, 1) - G.subs(r, e)) for e in (1e-1, 1e-2)]
print("      INT_eps^1 |G'| : eps=1e-1 -> %.3f, eps=1e-2 -> %.3f  (grows ~ (4/pi) ln(1/eps))" % tuple(vals))
print("      INT_eps^1  G'  = G(1)-G(eps): %.6f, %.6f -> G(1) = %.6f" % (signed[0], signed[1], float(G.subs(r, 1))))
pred = (2/math.pi)*math.log(1e4/1e2)   # mean |cos| = 2/pi times INT dt/t over t in [1e2, 1e4]
chk("T6  |G'| integral grows by %.4f over eps 1e-1 -> 1e-2, predicted (2/pi) ln 100 = %.4f (log divergence); signed integral converges to G(1)" % (vals[1]-vals[0], pred),
    abs((vals[1] - vals[0]) - pred) < 0.02 and abs(signed[1] - float(G.subs(r, 1))) < 1e-3)

print("\nALL PASS" if ok else "\nSOME FAIL")
sys.exit(0 if ok else 1)
