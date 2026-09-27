#!/usr/bin/env python3
"""DOCKET 67 -- integral-monotonicity.  Re-derivation / machine-check of
   'u < 0 throughout (0,R] implies m(R) = INT_0^R 4 pi r^2 u dr < 0'
as tolman.py G2/G3 cite it (tolman.py:590-591, 940-942, 2235-2264).
Layers:
  S  sympy: the power-law family u = -a r^k (a>0) closed form, and the k <= -3 boundary.
  N  sympy/numeric: non-algebraic negative u (exp, atan, oscillatory) -- integral < 0.
  Z  z3: the finite (simple-function / Riemann-sum) version for n = 1..10 cells,
     plus drift rows: strictness needs positive measure; one positive cell breaks it.
  C  the hypothesis 'm is the integral of its derivative' (absolute continuity) is
     load-bearing: m(r) = -r + 2*Cantor(r) has m' = -1 < 0 a.e., m(0)=0, m(1)=+1 > 0.
  P  the pointwise route: m differentiable EVERYWHERE on (0,R] with m' < 0 and m(0+)=0
     gives m(R) < 0 by the mean value theorem with NO integrability hypothesis (stated,
     checked on examples only).
Exit 0 iff every row returns what it should."""
import sys, math
import sympy as sp
import z3

ok_all = True
def row(label, got, want):
    global ok_all
    good = (got == want)
    ok_all &= good
    print(f"  {'ok ' if good else 'BAD'} {label}: got {got}, want {want}")

r, R, a = sp.symbols('r R a', positive=True)
k = sp.symbols('k', real=True)

print("S  power-law family u = -a r^k")
for kk in [sp.Rational(-5, 2), -2, -1, 0, 1, sp.Rational(7, 3), 5]:
    I = sp.integrate(4*sp.pi*r**2*(-a*r**kk), (r, 0, R))
    closed = -4*sp.pi*a*R**(kk+3)/(kk+3)
    row(f"k={kk}: INT = {sp.simplify(I)}, equals -4 pi a R^(k+3)/(k+3)", sp.simplify(I-closed) == 0, True)
    row(f"k={kk}: sign negative for a,R>0", sp.ask(sp.Q.negative(I), sp.Q.positive(a) & sp.Q.positive(R)), True)
# general k > -3 : antiderivative and the centre limit
F = sp.integrate(4*sp.pi*r**(k+2)*(-a), r, conds='none')
print("   general antiderivative:", sp.simplify(F))
kk = sp.symbols('kk', positive=True)  # kk = k+3 > 0
lim0 = sp.limit(-4*sp.pi*a*r**kk/kk, r, 0, '+')
row("k>-3 (k+3>0): centre term r^(k+3) -> 0, so m(R) = -4 pi a R^(k+3)/(k+3) < 0", lim0, 0)
for kk2 in [-3, -4]:
    Idiv = sp.integrate(4*sp.pi*r**2*(-r**kk2), (r, sp.Rational(1, 10**6), 1))
    row(f"k={kk2}: integral near centre diverges (value on [1e-6,1] = {sp.N(Idiv,6)} < -40): NOT integrable, regular centre fails",
        bool(Idiv < -40), True)

print("N  non-algebraic negative u (integral not a power law)")
cases = {
    "u=-exp(r), R=2": (-sp.exp(r), 2),
    "u=-1/(1+r^2), R=3": (-1/(1+r**2), 3),
    "u=-(2+sin(1/r)), R=1": (-(2+sp.sin(1/r)), 1),
    "u=-log(1+1/r), R=1 (unbounded at centre, integrable)": (-sp.log(1+1/r), 1),
    "u=-exp(-r^2) * (1.5+cos(40 r)), R=2": (-sp.exp(-r**2)*(sp.Rational(3, 2)+sp.cos(40*r)), 2),
}
for lab, (u, Rv) in cases.items():
    val = sp.Integral(4*sp.pi*r**2*u, (r, 0, Rv)).evalf(20)
    row(f"{lab}: INT = {sp.N(val, 10)} < 0", bool(val < 0), True)

print("Z  finite version: SUM w_i u_i with w_i > 0 (cell weights 4 pi r_i^2 dr_i)")
for n in range(1, 11):
    w = z3.Reals(' '.join(f"w{i}" for i in range(n)))
    u = z3.Reals(' '.join(f"u{i}" for i in range(n)))
    S = z3.Sum([w[i]*u[i] for i in range(n)])
    hyp = z3.And([w[i] > 0 for i in range(n)] + [u[i] < 0 for i in range(n)])
    s = z3.Solver(); s.add(hyp)
    vac = s.check()
    s.add(S >= 0)
    row(f"n={n}: hyp sat ({vac}) and (u<0 all cells) & SUM >= 0 is", str(s.check()), "unsat")
n = 6
w = z3.Reals(' '.join(f"w{i}" for i in range(n))); u = z3.Reals(' '.join(f"u{i}" for i in range(n)))
S = z3.Sum([w[i]*u[i] for i in range(n)])
s = z3.Solver(); s.add([w[i] > 0 for i in range(n)] + [u[i] <= 0 for i in range(n)] + [S == 0])
row("DRIFT Z1 u <= 0 only (u = 0 a.e.): SUM == 0 satisfiable -> strictness needs u<0 on positive measure", str(s.check()), "sat")
s = z3.Solver(); s.add([w[i] > 0 for i in range(n)] + [u[i] < 0 for i in range(1, n)] + [S > 0])
row("DRIFT Z2 one cell with u > 0 allowed: SUM > 0 satisfiable -> 'throughout' is load-bearing", str(s.check()), "sat")

print("C  absolute continuity is load-bearing (Cantor counterexample)")
def cantor(x, depth=60):
    # Cantor function via ternary expansion
    if x <= 0: return 0.0
    if x >= 1: return 1.0
    y, scale = 0.0, 0.5
    for _ in range(depth):
        x *= 3
        d = int(x); x -= d
        if d == 1:
            return y + scale
        y += scale*(d//2)
        scale /= 2
    return y
m = lambda x: -x + 2*cantor(x)
row("m(0) = 0", m(0.0), 0.0)
row("m(1) = -1 + 2 = +1 > 0", m(1.0), 1.0)
# derivative -1 on every removed middle-third interval (total length 1): check slope on a sample
h = 1e-9
slopes = [(m(x+h)-m(x-h))/(2*h) for x in (1/2, 1/6, 5/6, 1.5/27, 19.5/27, 7.5/27, 0.5/9**2*3)]
row("slope m' = -1 at sample points in removed intervals (u = m'/(4 pi r^2) < 0 a.e.)",
    all(abs(s_+1) < 1e-4 for s_ in slopes), True)
removed = sum(2**(j)/3**(j+1) for j in range(200))
row(f"removed-interval measure = {removed:.12f} (full measure, so m' = -1 a.e.)", abs(removed-1) < 1e-12, True)

print("P  pointwise route (MVT), stated not machine-checked: if m is differentiable at EVERY r in (0,R]")
print("   with m'(r) = 4 pi r^2 u(r) < 0 and m(0+) = 0, the mean value theorem gives m(R) < 0 with no")
print("   integrability hypothesis at all.  The N rows are instances (m defined as the integral).")
print("\nRESULT:", "ALL ROWS OK" if ok_all else "SOME ROW FAILED")
sys.exit(0 if ok_all else 1)
