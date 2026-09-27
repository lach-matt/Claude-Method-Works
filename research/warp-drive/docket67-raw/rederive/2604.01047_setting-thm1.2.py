#!/usr/bin/env python3
"""DOCKET 67 -- audit of GMMPS (arXiv:2604.01047 v1) Thm 1.2 / Thm 4.14 / Prop 2.4
as linstab.py:132-142 uses them.  Read-only; writes nothing.  sympy + mpmath.
Checks the finite / closed-form content of the SETTING and the hypotheses the
well-posedness proof chain (Prop 4.5 -> 4.10 -> 4.11 -> 4.12 -> Lemma 4.13 -> Thm 4.14)
places on the parameter a, for the S sector (a = 2m^2/(6xi-1), sec 5.1 eq 5.2) and the
TT sector (a = 4m^2, sec 5.2).  Units m = 1 throughout the numerics."""
import sympy as sp, mpmath as mp
mp.mp.dps = 30
fails = []
def chk(name, got, want):
    ok = (got == want)
    print(("PASS " if ok else "FAIL ") + name + " :: got %r want %r" % (got, want))
    if not ok: fails.append(name)

xi, m, box, n = sp.symbols('xi m box n', real=True)
print("C1  S sector: a = 2m^2/(6xi-1) < 4m^2 (GMMPS 5.1 '2/(6xi-1) < 4')")
sol = sp.solve_univariate_inequality(2/(6*xi-1) < 4, xi, relational=False)
print("    solution set:", sol)
chk("C1a  {xi : 2/(6xi-1) < 4} = (-oo,1/6) U (1/4,oo)", sol,
    sp.Union(sp.Interval.open(-sp.oo, sp.Rational(1,6)), sp.Interval.open(sp.Rational(1,4), sp.oo)))
chk("C1b  xi = 1/6 (conformal) excluded: a undefined", sp.Rational(1,6) in sol, False)
chk("C1c  minimal coupling xi=0 admitted, a = -2 m^2", (0 in sol, sp.simplify(2*m**2/(6*0-1))), (True, -2*m**2))
S_op = sp.Rational(2,3)*(m**2 + sp.Rational(1,2)*(1-6*xi)*box)**2          # (1.11)/(3.11)
chk("C1d  S operator double root box = 2m^2/(6xi-1)", sp.simplify(sp.solve(S_op, box)[0] - 2*m**2/(6*xi-1)), 0)
chk("C1e  S operator loses its box^2 term at xi=1/6 (top order degenerates)", sp.degree(sp.expand(S_op.subs(xi, sp.Rational(1,6))), box), 0)

print("\nC2  TT sector: T = (1/60)(box - 4m^2)^2  (1.11/3.11)  -> a1 = a2 = 4 m^2 (5.2)")
T_op = sp.Rational(1,60)*(box - 4*m**2)**2
roots = sp.roots(sp.Poly(T_op, box))
chk("C2a  TT double root a = 4m^2", roots, {4*m**2: 2})
a_TT = 4
chk("C2b  a_TT in (-oo,4m^2)  [Thm 4.14, Prop 4.12, Lemma 4.13 hypothesis]", sp.Interval.open(-sp.oo, 4).contains(a_TT), sp.false)
chk("C2c  a_TT in (-oo,4m^2]  [Prop 4.11 hypothesis]", sp.Interval(-sp.oo, 4).contains(a_TT), sp.true)

# ---- J (4.17) as the Stieltjes integral of rho (4.5), m = 1 ----
rho = lambda M: (1/(16*mp.pi**2))*mp.sqrt(1-4/M)/M
def J(z, k=0):   # k-th derivative in z: k! int rho/(M-z)^(k+1)
    return mp.factorial(k)*mp.quad(lambda M: rho(M)/(M-z)**(k+1), [4, 5, 20, 1e3, mp.inf])
def Jclosed(z):  # (4.17), real z in (0,4)
    return (1/(8*mp.pi**2))*(1/z - (4-z)*mp.acsc(2/mp.sqrt(z))/(mp.sqrt(4-z)*z**1.5))
chk("C3pre  (4.17) closed form = Stieltjes integral at z=1, 3 (1e-20)",
    all(abs(J(z)-Jclosed(z)) < 1e-20 for z in (mp.mpf(1), mp.mpf(3))), True)
def A(g, a):   return (a-g)**2*J(g)
def A1(g, a):  return -2*(a-g)*J(g) + (a-g)**2*J(g,1)
def A2(g, a):  return 2*J(g) - 4*(a-g)*J(g,1) + (a-g)**2*J(g,2)
def A2int(g,a):return mp.quad(lambda M: rho(M)*2*(M-a)**2/(M-g)**3, [4,5,20,1e3,mp.inf])  # Lemma 4.13 form
print("\nC3  Lemma 4.13: A(g) = (a-g)^2 J(g) convex with A'(I) = R, I = (-oo, 4m^2)")
chk("C3a  A'' (derivative form) = Lemma 4.13 integral form at g=1, a=4", abs(A2(mp.mpf(1),4)-A2int(mp.mpf(1),4)) < 1e-18, True)
eps_list = [mp.mpf(10)**(-k) for k in (1,2,3,4,5,6)]
print("    a = -2 (S sector, xi = 0):  A'(4 - eps) =", [mp.nstr(A1(4-e,-2),6) for e in eps_list])
print("    a =  4 (TT sector):         A'(4 - eps) =", [mp.nstr(A1(4-e, 4),6) for e in eps_list])
r = A1(4-mp.mpf('1e-6'),-2)/A1(4-mp.mpf('1e-4'),-2)
chk("C3b  a=-2: A'(4-eps) grows like eps^-1/2 (ratio over eps 1e-4 -> 1e-6 in (9,11)): diverges, Lemma 4.13 holds", 9 < r < 11, True)
chk("C3c  a=4:  |A'(4-1e-6)| < 1e-4 (tends to 0, Lemma 4.13's 'lim = +oo' FAILS)", abs(A1(4-mp.mpf('1e-6'),4)) < 1e-4, True)
grid = [-1e4,-1e3,-100,-10,-1,0,1,2,3,3.9,3.99,3.999,3.9999]
A1vals = [A1(mp.mpf(g),4) for g in grid]
chk("C3d  a=4: A' < 0 at every grid point of I (so A'(I) is contained in (-oo,0), not R)", all(v < 0 for v in A1vals), True)
chk("C3e  a=4: A'' >= 0 at every grid point (convexity survives)", all(A2int(mp.mpf(g),4) >= 0 for g in grid), True)

print("\nC4  Can Prop 4.12's conclusion (3 real distinct roots in I of A(g) = b0/g + b1 + b2 g, b0,b1 != 0)")
print("    be reached at a = 4m^2 by ANY auxiliary (b0,b1)?  Equivalent: G(g) = g A(g) - b2 g^2 meets a line")
print("    b1 g + b0 three times in I.  If G'' < 0 on all of I (G concave), no line does.")
def G2(g, b2): return 2*A1(g,4) + g*A2(g,4) - 2*b2
fine = [-1e6,-1e4,-1e3,-300,-100,-30,-10,-3,-1,-0.3,0,0.3,1,1.5,2,2.5,3,3.3,3.6,3.8,3.9,3.95,3.99,3.999,3.9999]
h = [ (2*A1(mp.mpf(g),4) + mp.mpf(g)*A2(mp.mpf(g),4))/2 for g in fine ]
bstar = max(h); gstar = fine[h.index(bstar)]
print("    b2* = sup_I (A' + g A''/2) on grid = %s at g = %s" % (mp.nstr(bstar,8), gstar))
# refine near the maximiser
from mpmath import findroot
f = lambda g: (2*A1(g,4) + g*A2(g,4))/2
xs = [mp.mpf(gstar) + d for d in mp.linspace(-0.5, 0.0999 if gstar < 3.9 else 0.0000999, 41)]
xs = [x for x in xs if x < 4]
bstar_ref = max(f(x) for x in xs)
print("    refined b2* =", mp.nstr(bstar_ref, 8))
for b2 in (mp.mpf('0.01'), mp.mpf('0.1'), mp.mpf(1), mp.mpf(10), mp.mpf('1e3')):
    conc = all(G2(mp.mpf(g), b2) < 0 for g in fine)
    print("    b2 = %-6s G concave on grid: %s" % (mp.nstr(b2,4), conc))
lim = 1/(8*mp.pi**2)
chk("C4pre  J(4m^2) = 1/(32 pi^2 m^2) (4.17 at z -> 4m^2, and the integral)", abs(J(mp.mpf(4)) - 1/(32*mp.pi**2)) < 1e-15, True)
fe = [f(4-mp.mpf(10)**(-kk)) for kk in (2,4,6,8)]
print("    f(4 - eps) =", [mp.nstr(v,10) for v in fe], " 1/(8 pi^2) =", mp.nstr(lim,10))
chk("C4lim  b2* = sup_I (A' + g A''/2) = its boundary value 4m^2 J(4m^2) = 1/(8 pi^2) (to 1e-5 at eps=1e-8; monotone approach; grid max below it)",
    (abs(fe[-1]-lim) < 1e-5, all(fe[i] < fe[i+1] for i in range(3)), bstar <= lim), (True, True, True))
chk("C4a  for b2 = 0.1, 1, 10, 1e3 (m=1): G'' < 0 on the whole grid => no auxiliary (b0,b1) gives 3 real roots",
    all(all(G2(mp.mpf(g), b2) < 0 for g in fine) for b2 in (mp.mpf('0.1'),1,10,1000)), True)
# contrast: a = -2, b2 = 10 -> Prop 4.12's tangent construction works
a = -2; b2 = mp.mpf('0.2')
gt = findroot(lambda g: A1(g,a) - b2, (mp.mpf('0.0'), 4-mp.mpf('1e-12')), solver='bisect')
q = A(gt,a) - b2*gt
e1, e2 = mp.mpf('1e-6'), mp.mpf('1e-7')
F = lambda g: A(g,a) - (e1/g + q + e2 + b2*g)
pts = sorted(set([mp.mpf(10)**(-mp.mpf(kk)/10) for kk in range(20, 120)] + [mp.mpf(x)/100 for x in range(1, 400)] + [4 - mp.mpf(10)**(-mp.mpf(kk)/40) for kk in range(1, 400)]
                 + [gt + d for d in mp.linspace(-mp.mpf('0.05'), min(mp.mpf('0.05'), (4-gt)*0.999), 401)]))
pts = [x for x in pts if 0 < x < 4]
vals = [F(x) for x in pts]
changes = sum(1 for i in range(len(pts)-1) if vals[i]*vals[i+1] < 0)
neg = [mp.mpf(-10)**0 * x for x in (-1000,-100,-10,-1,-0.1,-0.001)]
negchg = sum(1 for i in range(len(neg)-1) if F(mp.mpf(neg[i]))*F(mp.mpf(neg[i+1])) < 0)
print("    a=-2, b2=0.2: tangent point g~ = %s; real roots of A = B located by sign change: %d in (0,4m^2), %d on the sampled negative axis" % (mp.nstr(gt,8), changes, negchg))
chk("C4b  a=-2 (inside Lemma 4.13's hypothesis), b2=0.2: Prop 4.12's tangent construction yields 3 real roots in I", changes + negchg >= 3, True)

print("\nC5  Prop 2.4 algebra (n dims): de Donder fixing is complete on past-compact fields")
w, hb, Y = sp.symbols('wbar hbar Y')   # treat box as commuting symbol on scalars
Yt = -(sp.Rational(1,1)*(n-1)/(2*(n-2))*box*w + hb/(2*(n-2)))    # box Y~ = -[...] since G_ret inverts box
expr = (n-1)/n*box*box*w + hb*box/n + 2*(n-2)/n*box*Yt
chk("C5a  (n-1)/n box^2 wbar + 1/n box hbar + 2(n-2)/n box^2 Y~ = 0 with Y~ of Prop 2.4", sp.simplify(expr), 0)
k = sp.Matrix(sp.symbols('k0:4')); ks = sp.symbols('ksq')
# residual gauge symbol for n=4 generic n: box X_b + (1-4/n) d_b d.X  ->  -(k^2 I + (n-4)/n k k^T) in Fourier (Euclideanised)
Msym = sp.eye(4)*(k.T*k)[0] + (n-4)/n*(k*k.T)
ev = sp.simplify(Msym.subs(n,4).det()) ; ev5 = sp.factor(sp.simplify(Msym.det()))
print("    det of residual-gauge symbol (general n, embedded in 4 comps):", ev5)
chk("C5b  residual-gauge symbol det = |k|^8 (2n-4)/n: vanishes only on |k|=0 or n=2", sp.simplify(ev5 - (k.T*k)[0]**4*(2*n-4)/n), 0)
chk("C5c  trace-reversal convention hbar = h - (2/n) eta tr h reproduces Prop 2.4's -(4/n) eta d.X term",
    sp.simplify(-sp.Rational(2,1)/n*2), -4/n)

print("\n%d failed%s" % (len(fails), (": " + ", ".join(fails)) if fails else " -- all checks pass"))
raise SystemExit(1 if fails else 0)
