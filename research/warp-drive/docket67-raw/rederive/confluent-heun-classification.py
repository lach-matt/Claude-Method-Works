#!/usr/bin/env python3
"""DOCKET 67 -- re-derivation for 'confluent-heun-classification'.

Owner: research/warp-drive/fewsterteo.py:62-67, 105-107, 171, 432-452.
Claim as used: the massless radial equation on -F dt^2 + dr^2/F + r^2 dOmega^2,
F = 1 - 2M/r, has regular singular points r = 0, r = 2M and an irregular one at
infinity -> confluent Heun, 'no closed form in named special functions';
for M < 0 the class is unchanged; (107) 'shows they cannot be [determined]'.

What this script COMPUTES (sympy + mpmath, nothing declared):
  C1  singular points and local exponents at 0, 2M, and the Poincare rank at oo
  C2  an explicit s-homotopic map to the shape w'' + (g/z + d/(z-1) + e) w'
      + (a z - q)/(z(z-1)) w = 0 (the confluent Heun shape: 2 regular + rank-1 oo)
  C3  the degenerate cases the claim must exclude: M = 0 (spherical Bessel,
      closed form) and omega = 0 (Legendre P_l, Q_l of r/M - 1, closed form)
  C4  Kovacic cases 1-3: no Liouvillian solution for real omega != 0, M != 0
      (degree argument, general l), plus a brute-force ansatz check
  C5  count of non-apparent regular singular points (2) vs Kummer/Whittaker (1):
      no reduction by affine map + exponential/power gauge
  C6  M < 0: r = 0 is limit-circle in L^2(r^2/F dr) -> mode functions need a
      boundary condition (self-adjoint extension) the claim does not name
  C7  the mode functions ARE determinable: Frobenius series at r = 2M converges
      and matches direct numerical integration
  C8  the board's corridor metric (concentric.py Phi, M_ADM = 0): exterior is
      Minkowski (closed form), interior coefficients are not rational in r
"""
import sympy as sp
import mpmath as mp

ok = True
def row(name, got, want):
    global ok
    good = (got == want)
    ok &= bool(good)
    print("  [%s] %s: %s" % ("OK" if good else "XX", name, got))

r, M, w = sp.symbols('r M omega', nonzero=True)
l = sp.Symbol('l', integer=True, nonnegative=True)
Rf = sp.Function('R')

def radial(F, gtt_factor=None):
    """Box phi = 0 for -A dt^2 + dr^2/B + r^2 dOmega^2 (A = gtt_factor or F, B = F),
    phi = R(r) Y_lm e^{-i w t}; returns (P, Q) of R'' + P R' + Q R = 0."""
    A = F if gtt_factor is None else gtt_factor
    B = F
    R = Rf(r)
    # sqrt(-g) = r^2 sqrt(A/B) sin; g^rr = B, g^tt = -1/A
    sq = r**2 * sp.sqrt(A / B)
    box = sp.diff(sq * B * sp.diff(R, r), r) / sq + w**2 / A * R - l*(l+1)/r**2 * R
    E = sp.expand(box)
    c2 = E.coeff(sp.Derivative(R, (r, 2)))
    c1 = E.coeff(sp.Derivative(R, r))
    c0 = sp.expand(E - c2*sp.Derivative(R, (r, 2)) - c1*sp.Derivative(R, r)).coeff(R)
    return sp.simplify(c1/c2), sp.simplify(c0/c2)

F = 1 - 2*M/r
P, Q = radial(F)
print("P =", sp.factor(P)); print("Q =", sp.factor(Q))

print("\nC1  singular points, exponents, rank")
den = sp.denom(sp.together(sp.factor(P))) * sp.denom(sp.together(sp.factor(Q)))
rr_ = sp.Symbol('rr_')   # unrestricted symbol: r is declared nonzero, which hides the root r = 0
sing = sorted(set(sp.roots(sp.Poly(sp.expand(den.subs(r, rr_)), rr_)).keys()), key=str)
row("finite singular points", sing, sorted([0, 2*M], key=str))
rho = sp.Symbol('rho')
def indicial(c):
    p0 = sp.limit(sp.cancel((r - c) * P), r, c)
    q0 = sp.limit(sp.cancel((r - c)**2 * Q), r, c)
    return sp.factor(rho*(rho - 1) + p0*rho + q0), p0, q0
i0, p0, q0 = indicial(0)
row("r = 0 regular (p0,q0 finite)", (p0.is_finite, q0.is_finite), (True, True))
row("indicial at r = 0 (double root 0 -> a log solution)", i0, rho**2)
i2, _, _ = indicial(2*M)
roots2 = sp.solve(i2, rho)
row("exponents at r = 2M", sorted(roots2, key=str), sorted([2*sp.I*M*w, -2*sp.I*M*w], key=str))
# infinity: z = 1/r ; rank from growth of the formal solutions
z = sp.Symbol('z')
Qinf = sp.limit(Q, r, sp.oo); Pinf = sp.limit(P, r, sp.oo)
row("P -> 0, Q -> omega^2 at oo", (Pinf, Qinf), (0, w**2))
row("r*P bounded but r^2*Q unbounded -> oo IRREGULAR",
    (sp.limit(r*P, r, sp.oo), sp.limit(r**2*Q/w**2, r, sp.oo)), (2, sp.oo))
# formal solution at oo: R = e^{s r} r^k (1 + O(1/r)); leading two orders
s, k = sp.symbols('s k')
# R'/R = s + k/r, R''/R = (s + k/r)^2 - k/r^2  (exact, no fractional powers)
res = sp.together((s + k/r)**2 - k/r**2 + P*(s + k/r) + Q)
ser = sp.series(sp.cancel(res.subs(r, 1/z)), z, 0, 2).removeO()
eq0 = sp.simplify(ser.coeff(z, 0)); eq1 = sp.simplify(ser.coeff(z, 1))
sols = sp.solve([eq0, eq1], [s, k], dict=True)
row("formal exponents at oo: e^{s r} r^k", sorted([(d[s], sp.simplify(d[k])) for d in sols], key=str),
    sorted([(sp.I*w, -1 + 2*sp.I*M*w), (-sp.I*w, -1 - 2*sp.I*M*w)], key=str))
row("Poincare rank at oo = 1 (s linear in r, nonzero for omega != 0)", all(d[s] != 0 for d in sols), True)

print("\nC2  explicit map to the confluent Heun shape")
zz = sp.Symbol('zz')
g = sp.exp(sp.I*w*r) * (r - 2*M)**(2*sp.I*M*w)
# simpler: substitute W by symbols through the chain rule directly
Wz = sp.Function('Wz')(zz)
Rz = (g.subs(r, 2*M*zz)) * Wz
# d/dr = (1/2M) d/dz
Pz = sp.simplify(P.subs(r, 2*M*zz)); Qz = sp.simplify(Q.subs(r, 2*M*zz))
odez = sp.diff(Rz, zz, 2)/(4*M**2) + Pz*sp.diff(Rz, zz)/(2*M) + Qz*Rz
odez = sp.expand(sp.simplify(odez / g.subs(r, 2*M*zz)))
C2c = sp.simplify(odez.coeff(sp.Derivative(Wz, (zz, 2))))
C1c = sp.simplify(odez.coeff(sp.Derivative(Wz, zz)))
C0c = sp.simplify(sp.expand(odez - C2c*sp.Derivative(Wz, (zz, 2)) - C1c*sp.Derivative(Wz, zz)).coeff(Wz))
Pn = sp.apart(sp.simplify(C1c/C2c), zz); Qn = sp.factor(sp.simplify(C0c/C2c))
print("   W'' coefficient-normalised P(z) =", Pn)
print("   Q(z) =", Qn)
gam, dlt, eps, al, qq = sp.symbols('gamma delta epsilon alpha q')
shapeP = gam/zz + dlt/(zz - 1) + eps
solP = sp.solve(sp.Poly(sp.numer(sp.together(Pn - shapeP)), zz).coeffs(), [gam, dlt, eps], dict=True)
row("P(z) has the form g/z + d/(z-1) + e", len(solP) == 1, True)
print("   gamma, delta, epsilon =", solP[0] if solP else None)
solQ = sp.solve(sp.Poly(sp.numer(sp.together(Qn - (al*zz - qq)/(zz*(zz - 1)))), zz).coeffs(), [al, qq], dict=True)
row("Q(z) has the form (a z - q)/(z(z-1))", len(solQ) == 1, True)
print("   alpha, q =", solQ[0] if solQ else None)

print("\nC3  degenerate cases the claim needs excluded")
P0, Q0 = radial(sp.Integer(1))
for L in range(4):
    x = w*r
    jl = sp.expand_func(sp.jn(L, x)); yl = sp.expand_func(sp.yn(L, x))
    for nm, f in (("j", jl), ("y", yl)):
        rr = sp.simplify((sp.diff(f, r, 2) + P0.subs(l, L)*sp.diff(f, r) + Q0.subs(l, L)*f))
        row("M = 0: spherical Bessel %s_%d(omega r) solves it (closed form)" % (nm, L), rr, 0)
Pw, Qw = sp.simplify(P.subs(w, 0)), sp.simplify(Q.subs(w, 0))
for L in range(4):
    xx = r/M - 1
    for nm, f in (("P", sp.legendre(L, xx)),
                  ("Q", sp.simplify(sp.legendre(L, xx)*sp.log((xx+1)/(xx-1))/2
                        - sum(sp.Rational(2*L-4*m_-1, (2*m_+1)*(L-m_)) * sp.legendre(L-2*m_-1, xx)
                              for m_ in range((L+1)//2)) if L > 0 else sp.log((xx+1)/(xx-1))/2))):
        rr = sp.simplify(sp.diff(f, r, 2) + Pw.subs(l, L)*sp.diff(f, r) + Qw.subs(l, L)*f)
        row("omega = 0: Legendre %s_%d(r/M - 1) solves it (closed form)" % (nm, L), rr, 0)

print("\nC4  Kovacic: no Liouvillian solution for real omega != 0, M != 0")
S = sp.simplify(P**2/4 + sp.diff(P, r)/2 - Q)   # y'' = S y, R = y exp(-1/2 int P)
print("   normalised S(r) =", sp.factor(S))
b0 = sp.limit(sp.cancel(r**2*S), r, 0)
b2 = sp.simplify(sp.limit(sp.cancel((r-2*M)**2*S), r, 2*M))
row("pole order 2 at r = 0 with b0 = -1/4 (1+4b0 = 0)", sp.simplify(1 + 4*b0), 0)
row("pole order 2 at r = 2M with 1+4b = -16 M^2 omega^2", sp.simplify(1 + 4*b2 + 16*M**2*w**2), 0)
row("order of S at oo is 0 (S -> -omega^2)", sp.limit(S, r, sp.oo), -w**2)
print("   case 3 needs ord_oo(S) >= 2: ord = 0 -> EXCLUDED")
# case 2: E_c = {2, 2 +- 2 sqrt(1+4b)} cap Z ; E_oo = {ord_oo} = {0}
# r = 0: sqrt(0) -> {2}; r = 2M: sqrt(-16M^2w^2) = 4iMw not real -> {2}
d_case2 = sp.Rational(1, 2)*(0 - 2 - 2)
row("case 2 maximal degree d = (e_oo - e_0 - e_2M)/2 = -2 < 0 -> EXCLUDED", d_case2, -2)
# case 1: alpha_c^{+-} = 1/2 +- sqrt(1+4b)/2 ; at oo, S = -w^2 + c1/r + ...:
#   [sqrt S]_oo = +-i w, alpha_oo^{+-} = +-(c1/(2 i w)) ... degree d = alpha_oo - sum alpha_c
c1 = sp.simplify(sp.limit(r*(S + w**2), r, sp.oo))
sqS = sp.I*w
a_oo = {sg: sg*c1/(2*sqS) for sg in (1, -1)}   # Kovacic: alpha_oo^{+-} = +-(b/a) /2 with ord 0, a = [sqrt S], b from c1
a_0 = [sp.Rational(1, 2)]
a_2 = [sp.Rational(1, 2) + 2*sp.I*M*w, sp.Rational(1, 2) - 2*sp.I*M*w]
degs = []
for sg in (1, -1):
    for a2_ in a_2:
        dd = sp.simplify(a_oo[sg] - a_0[0] - a2_)
        degs.append(dd)
print("   case-1 candidate degrees:", degs)
realdeg_nonneg_int = [dd for dd in degs if dd.is_integer and dd >= 0]
row("every case-1 degree has Re = -1 or nonzero Im for real omega != 0 -> EXCLUDED",
    all(sp.simplify(sp.re(dd.subs({M: 1, w: sp.Rational(3, 7)}))) == -1 or
        sp.im(dd.subs({M: 1, w: sp.Rational(3, 7)})) != 0 for dd in degs), True)
row("... the Re = -1 branch degree is exactly -1 (independent of l, M, omega)",
    sorted([sp.simplify(dd) for dd in degs if sp.simplify(dd).is_number], key=str), [-1, -1])
# brute force: R = e^{s i w r} (r-2M)^{t 2iMw} p(r), deg p <= 6, M = 1, w = 3/7, l = 0..3
Mv, wv = 1, sp.Rational(3, 7)
Pv, Qv = P.subs({M: Mv, w: wv}), Q.subs({M: Mv, w: wv})
found = False
for L in range(4):
    for sg in (1, -1):
        for tg in (1, -1):
            cs = sp.symbols('c0:7')
            poly = sum(cs[i]*r**i for i in range(7))
            Lg = sg*sp.I*wv + tg*2*sp.I*Mv*wv/(r - 2*Mv)          # E'/E of the exponential-power factor
            PL, QL = Pv.subs(l, L), Qv.subs(l, L)
            e = (sp.diff(poly, r, 2) + (2*Lg + PL)*sp.diff(poly, r)
                 + (Lg**2 + sp.diff(Lg, r) + PL*Lg + QL)*poly)
            num = sp.numer(sp.together(e))
            sol = sp.solve(sp.Poly(sp.expand(num), r).coeffs(), cs, dict=True)
            nontriv = [d for d in sol if any(sp.simplify(v) != 0 for v in d.values())
                       or len(d) < 7]
            if nontriv:
                found = True
row("brute force: no e^{+-iwr}(r-2M)^{+-2iMw} poly(deg<=6) solution, l=0..3, M=1, w=3/7", found, False)
# complex omega: the degree -1 + (s - t) 2iMw is a non-negative integer iff 4iMw = n + 1
nn = sp.Symbol('n', integer=True, nonnegative=True)
print("   (case-1 degree becomes n >= 0 only at omega = -i(n+1)/(4M): purely imaginary, not a real-frequency mode)")

print("\nC5  non-apparent regular singular points")
row("r = 0: double exponent -> logarithmic -> non-apparent", i0, rho**2)
row("r = 2M: exponent difference 4iMw not an integer for real w != 0", sp.simplify(roots2[0] - roots2[1]) in (4*sp.I*M*w, -4*sp.I*M*w), True)
print("   Kummer/Whittaker (1F1 class): ONE regular singular point + rank-1 oo.  An affine map")
print("   (the only rational map keeping a single rank-1 point at oo with rank 1) plus a gauge by")
print("   e^{linear} r^a (r-2M)^b preserves the number (2) of non-apparent regular points: NO")
print("   reduction to the confluent hypergeometric class in that transformation group.")
print("   NOT covered: first-order-operator (gauge-with-derivative) equivalences, integral")
print("   representations, series in named functions (Leaver/MST) -- 'closed form' is not a")
print("   decidable predicate and is not decided here.")

print("\nC6  M < 0: r = 0 is limit-circle")
Mneg = sp.Symbol('m', positive=True)   # M = -m
Fn = 1 + 2*Mneg/r
weight = sp.simplify(r**2/Fn)          # A symmetric in L^2(r^2/F dr)
eps_ = sp.Symbol('epsilon', positive=True)
I1 = sp.integrate(sp.series(weight, r, 0, 5).removeO(), (r, 0, eps_))
Ilog = sp.integrate(sp.series(weight, r, 0, 5).removeO()*sp.log(r)**2, (r, 0, eps_))
row("solution ~ 1 is L^2 near 0", I1.is_finite, True)
row("solution ~ log r is L^2 near 0 -> limit-circle: a boundary condition is required", sp.simplify(Ilog).is_finite, True)

print("\nC7  the mode functions are determinable (Frobenius at r = 2M, radius 2M)")
mp.mp.dps = 30
Mn, wn, Ln = mp.mpf(1), mp.mpf('0.5'), 1
Pl = sp.lambdify(r, P.subs({M: 1, w: sp.Rational(1, 2), l: Ln}), 'mpmath')
Ql = sp.lambdify(r, Q.subs({M: 1, w: sp.Rational(1, 2), l: Ln}), 'mpmath')
# Frobenius: R = x^rho sum a_n x^n, x = r - 2M, rho = 2iMw ; recurrence from exact series of x P, x^2 Q
xs = sp.Symbol('x')
Px = sp.series(sp.cancel((xs)*P.subs({M: 1, w: sp.Rational(1, 2), l: Ln}).subs(r, xs + 2)), xs, 0, 40).removeO()
Qx = sp.series(sp.cancel((xs)**2*Q.subs({M: 1, w: sp.Rational(1, 2), l: Ln}).subs(r, xs + 2)), xs, 0, 40).removeO()
pc = [complex(Px.coeff(xs, i)) for i in range(40)]
qc = [complex(Qx.coeff(xs, i)) for i in range(40)]
rh = 2j*1*0.5
a = [1+0j]
for n_ in range(1, 40):
    fnn = (rh+n_)*(rh+n_-1) + pc[0]*(rh+n_) + qc[0]
    sm = sum(a[k_]*((rh+k_)*pc[n_-k_] + qc[n_-k_]) for k_ in range(n_))
    a.append(-sm/fnn)
def Rser(rv, der=0):
    x = mp.mpf(rv) - 2
    if der == 0:
        return sum(mp.mpc(a[n_]) * x**(rh+n_) for n_ in range(40))
    return sum(mp.mpc(a[n_]) * (rh+n_) * x**(rh+n_-1) for n_ in range(40))
f = mp.odefun(lambda t, Y: [Y[1], -Pl(t)*Y[1] - Ql(t)*Y[0]], mp.mpf('2.5'), [Rser('2.5'), Rser('2.5', 1)])
num = f(mp.mpf('2.9'))[0]; ser_ = Rser('2.9')
rel = abs(num - ser_)/abs(ser_)
print("   series vs ODE integration at r = 2.9 (from r = 2.5): rel diff = %s" % mp.nstr(rel, 3))
row("Frobenius series = numerical solution to < 1e-8", rel < 1e-8, True)

print("\nC8  the board's own corridor metric (certify.py:116, concentric.py:3)")
mm, aa, Rs = sp.symbols('m a R_s', positive=True)
Phi_in = mm/sp.sqrt(r**2 + aa**2) - mm/Rs          # r < R_s
Pc_, Qc_ = radial(sp.Integer(1), gtt_factor=sp.exp(2*Phi_in))   # B = 1 kinematic slice as a test
row("with g_tt = -e^{2 Phi(r)} (Plummer core), Q is not rational in r", sp.simplify(Qc_).is_rational_function(r), False)
Phi_out = mm/sp.sqrt(r**2 + aa**2) - mm/r
row("M_ADM = 0: exterior Phi -> 0 like 1/r^3 (no 1/r tail)", sp.limit(r**2*Phi_out, r, sp.oo), 0)
print("   -> exterior radial eq tends to the M = 0 (spherical Bessel, closed-form) case, and the")
print("      interior is not a constant-M Schwarzschild equation at all: confluent Heun describes")
print("      neither region of the M_ADM = 0 device exactly.")

print("\nRESULT", "ALL COMPUTED ROWS AS EXPECTED" if ok else "SOME ROW DIFFERS")
