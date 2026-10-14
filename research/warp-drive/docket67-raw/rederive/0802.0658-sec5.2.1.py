#!/usr/bin/env python3
"""DOCKET 67 re-derivation for key 0802.0658-sec5.2.1.

Hu & Verdaguer, arXiv:0802.0658v1 (2008 Living Reviews update), Sec. 5.2.1
"Finiteness of Noise Kernel" (p.29): "the noise kernel is finite for y != x ...
all possible divergences for y != x will cancel. When the coincidence limit is
taken divergences do occur."  The review ASSERTS the coincidence divergence; it
does not compute it (Sec. 5, p.25: "leave the discussion of point-wise limit to
a later date").  What is finite and closed-form is checked here, in the one case
where everything is explicit: free scalar, Minkowski vacuum, massless, flat.

C1  The Sec. 3.2 mechanism: T -> T + F*I (c-number counterterm) leaves
    t = T - <T> and hence N unchanged.  (Algebra; trivial but stated.)
C2  H&V's explicit functional, Eqs. (5.26),(5.29)-(5.32), evaluated in flat
    space (R=0), m=0, general xi, on G = G+ of the Minkowski vacuum, is compared
    component by component with an independent Wick-theorem evaluation of the
    connected <T_ab(x) T_cd(y)> built from the stress tensor (5.9).
    This fixes the normalisation: Sec. 5's N is (1/8)<{t,t}>, Eq. (5.17);
    Sec. 3's N is (1/2)<{t,t}>, Eq. (3.11) -- a factor 4 between two sections
    of the same review, which Sec. 5.2.1 introduces as "the noise kernel
    introduced in Eq. (3.11)".  Recorded as a notational discrepancy only.
C3  The coincidence behaviour: N_0000(x,y) ~ c / |x-y|^8 with c != 0, both at
    equal-time (spacelike) separation r and along a timelike worldline (dt).
    So the pointwise y -> x limit diverges (the Sec. 5.2.1 sentence), and the
    r^-8 singularity is not locally integrable in 4D (or along a line), so the
    kernel exists only as a distribution (the Sec. 3.2 sentence).
C4  The worldline-smeared variance is FINITE with the Wightman i*eps rule:
    int int f(t) f(t') (t - t' - i eps)^-8 = (1/7!) int_0^oo w^7 |f^(w)|^2 dw,
    checked numerically at eps > 0 and evaluated at eps -> 0 for a Gaussian;
    while the same integrand WITHOUT i*eps (the pointwise kernel) diverges as
    delta^-7 at the cut-off.  This is the flat-vacuum instance of the step the
    tree NAMES (Fewster 1208.5399 Sec. 3.3); it is not the curved argument.
Exit 0 iff every check passes.
"""
import itertools, math, sys
import sympy as sp
import mpmath as mp

ok = True
def chk(name, cond, detail=""):
    global ok
    ok &= bool(cond)
    print(("PASS " if cond else "FAIL ") + name + ("  " + detail if detail else ""))

# ---------------- C1 ----------------
T, F, meanT = sp.symbols("T F meanT")
t_before = T - meanT
t_after = (T + F) - (meanT + F)
chk("C1 counterterm F*I cancels in t = T - <T>", sp.simplify(t_before - t_after) == 0)

# ---------------- setup ----------------
xi = sp.symbols("xi")
X = sp.symbols("x0:4", real=True)
Y = sp.symbols("y0:4", real=True)
eta = sp.diag(-1, 1, 1, 1)            # H&V signature (-,+,+,+): T00 = (phi_t^2+|grad phi|^2)/2 at xi=0
sig2 = -(X[0]-Y[0])**2 + sum((X[i]-Y[i])**2 for i in (1, 2, 3))
G = 1/(4*sp.pi**2*sig2)                 # Minkowski-vacuum massless Wightman fn (real part off light cone)

def D(expr, xs=(), ys=()):
    for a in xs: expr = sp.diff(expr, X[a])
    for c in ys: expr = sp.diff(expr, Y[c])
    return expr

# numeric sample point (spacelike separated, generic)
pt = {X[0]: sp.Rational(3, 10), X[1]: sp.Rational(11, 10), X[2]: sp.Rational(-2, 5), X[3]: sp.Rational(7, 10),
      Y[0]: 0, Y[1]: 0, Y[2]: 0, Y[3]: 0}
assert sig2.subs(pt) > 0

cache = {}
def g(xs, ys):
    key = (tuple(xs), tuple(ys))
    if key not in cache:
        cache[key] = sp.nsimplify(D(G, xs, ys).subs(pt))
    return cache[key]

# ---------------- direct Wick: T_ab as bilinear list (coef, D1, D2), flat, m=0 ----------------
def Tterms(a, b):
    out = []
    out.append(((1-2*xi), (a,), (b,)))
    for p in range(4):
        for q in range(4):
            if eta[p, q] != 0:
                out.append(((2*xi-sp.Rational(1, 2))*eta[a, b]*eta[p, q], (p,), (q,)))
                out.append((2*xi*eta[a, b]*eta[p, q], (), (p, q)))
    out.append((-2*xi, (), (a, b)))
    return out

def C_direct(a, b, c, d):
    s = 0
    for (c1, d1, d2) in Tterms(a, b):
        for (c2, d3, d4) in Tterms(c, d):
            s += c1*c2*(g(d1, d3)*g(d2, d4) + g(d1, d4)*g(d2, d3))
    return sp.expand(s)

# ---------------- H&V functional (5.29)-(5.32), flat R=0, m=0 ----------------
# lower-index derivative arrays; indices raised with eta (flat: eta^-1 = eta)
def Gx(*a): return g(a, ())
def Gy(*c): return g((), c)
def Gxy(xs, ys): return g(xs, ys)
R4 = range(4)
def up(p): return eta[p, p]

def N8_tilde_abcd(a, b, c, d):
    e = (1-2*xi)**2*(Gxy((b,), (c,))*Gxy((a,), (d,)) + Gxy((a,), (c,))*Gxy((b,), (d,)))
    e += 4*xi**2*(Gy(c, d)*Gx(a, b) + g((), ())*Gxy((a, b), (c, d)))
    e += -2*xi*(1-2*xi)*(Gx(b)*Gxy((a,), (c, d)) + Gx(a)*Gxy((b,), (c, d))
                          + Gy(d)*Gxy((a, b), (c,)) + Gy(c)*Gxy((a, b), (d,)))
    return e  # curvature terms vanish (R=0)

def N8_tilde_prime_ab(a, b):   # Eq. (5.31), multiplies g_{c'd'}; m=0, R=0
    s1 = sum(up(p)*Gxy((b,), (p,))*Gxy((a,), (p,)) for p in R4)
    s2 = sum(up(p)*Gxy((a,), (p, p)) for p in R4)       # G_{;a p'}^{p'}
    s2b = sum(up(p)*Gxy((b,), (p, p)) for p in R4)
    s3 = sum(up(p)*Gy(p)*Gxy((a, b), (p,)) for p in R4)
    s4 = sum(up(p)*Gy(p, p) for p in R4)
    s5 = sum(up(p)*Gxy((a, b), (p, p)) for p in R4)
    e = 2*(1-2*xi)*((2*xi-sp.Rational(1, 2))*s1 + xi*(Gx(b)*s2 + Gx(a)*s2b))
    e += -4*xi*((2*xi-sp.Rational(1, 2))*s3 + xi*(s4*Gx(a, b) + g((), ())*s5))
    return e

def N8_tilde_cd(c, d):         # mirror of (5.31) with x <-> y (NOT printed in the pages read; by symmetry)
    s1 = sum(up(p)*Gxy((p,), (d,))*Gxy((p,), (c,)) for p in R4)
    s2 = sum(up(p)*Gxy((p, p), (c,)) for p in R4)
    s2b = sum(up(p)*Gxy((p, p), (d,)) for p in R4)
    s3 = sum(up(p)*Gx(p)*Gxy((p,), (c, d)) for p in R4)
    s4 = sum(up(p)*Gx(p, p) for p in R4)
    s5 = sum(up(p)*Gxy((p, p), (c, d)) for p in R4)
    e = 2*(1-2*xi)*((2*xi-sp.Rational(1, 2))*s1 + xi*(Gy(d)*s2 + Gy(c)*s2b))
    e += -4*xi*((2*xi-sp.Rational(1, 2))*s3 + xi*(s4*Gy(c, d) + g((), ())*s5))
    return e

def N8_tilde_scalar():         # Eq. (5.32), m=0, R=0
    s1 = sum(up(p)*up(q)*Gxy((q,), (p,))**2 for p in R4 for q in R4)
    bx = sum(up(p)*Gx(p, p) for p in R4)
    by = sum(up(p)*Gy(p, p) for p in R4)
    bxy = sum(up(p)*up(q)*Gxy((p, p), (q, q)) for p in R4 for q in R4)
    s3 = sum(up(p)*up(q)*Gx(p)*Gxy((p,), (q, q)) for p in R4 for q in R4)
    s4 = sum(up(p)*up(q)*Gy(p)*Gxy((q, q), (p,)) for p in R4 for q in R4)
    e = 2*(2*xi-sp.Rational(1, 2))**2*s1 + 4*xi**2*(by*bx + g((), ())*bxy)
    e += 4*xi*(2*xi-sp.Rational(1, 2))*(s3 + s4)
    return e

def N8_HV_single(a, b, c, d):  # 8 N[G], Eq. (5.29) times 8
    return sp.expand(N8_tilde_abcd(a, b, c, d) + eta[a, b]*N8_tilde_cd(c, d)
                     + eta[c, d]*N8_tilde_prime_ab(a, b) + eta[a, b]*eta[c, d]*N8_tilde_scalar())

comps = [(0, 0, 0, 0), (0, 1, 0, 1), (1, 2, 1, 2), (0, 0, 1, 1), (1, 1, 2, 2), (0, 1, 2, 3), (3, 3, 3, 3), (0, 2, 1, 3)]
allmatch = True
for comp in comps:
    lhs = N8_HV_single(*comp)
    rhs = C_direct(*comp)
    diff = sp.simplify(lhs - rhs)
    m = (diff == 0)
    allmatch &= m
    print(f"   comp {comp}: 8N_HV[G] - C_direct = {diff}")
chk("C2 H&V (5.29)-(5.32) at R=0,m=0, all xi == independent Wick <T T>_c (8 components)", allmatch)
print("   => 8 N_Sec5(x,y) = C(x,y) + C(y,x) = <{t(x),t(y)}>, i.e. N_Sec5 = (1/8)<{t,t}> [Eq. (5.17)];"
      " Eq. (3.11) has N = (1/2)<{t,t}>: ratio N_Sec3/N_Sec5 = 4 (notational discrepancy, recorded)")

# ---------------- C3: r^-8 at coincidence ----------------
r, tau = sp.symbols("r tau", positive=True)
def C0000_expr(subsd):
    s = 0
    for (c1, d1, d2) in Tterms(0, 0):
        for (c2, d3, d4) in Tterms(0, 0):
            s += c1*c2*(D(G, d1, d3)*D(G, d2, d4) + D(G, d1, d4)*D(G, d2, d3))
    return sp.simplify(s.subs(subsd))
base = {Y[0]: 0, Y[1]: 0, Y[2]: 0, Y[3]: 0, X[2]: 0, X[3]: 0}
Cspace = C0000_expr({**base, X[0]: 0, X[1]: r})
Ctime = C0000_expr({**base, X[0]: tau, X[1]: 0})
cs = sp.simplify(Cspace*r**8); ct = sp.simplify(Ctime*tau**8)
print("   C_0000 at equal time, separation r :", sp.factor(Cspace))
print("   C_0000 along worldline, separation tau:", sp.factor(Ctime))
chk("C3a C_0000(r) = c_s(xi)/r^8 with c_s free of r", sp.diff(cs, r) == 0, f"c_s = {sp.factor(cs)}")
chk("C3b C_0000(tau) = c_t(xi)/tau^8 with c_t free of tau", sp.diff(ct, tau) == 0, f"c_t = {sp.factor(ct)}")
cs0 = cs.subs(xi, 0); ct0 = ct.subs(xi, 0); cs6 = cs.subs(xi, sp.Rational(1, 6)); ct6 = ct.subs(xi, sp.Rational(1, 6))
chk("C3c coefficient nonzero at xi=0 and xi=1/6 (so y->x DIVERGES pointwise)",
    all(v != 0 for v in (cs0, ct0, cs6, ct6)), f"xi=0: {cs0}, {ct0}; xi=1/6: {cs6}, {ct6}")
# minimal coupling known flat value check: 3/(2 pi^4 r^8)?  (computed, not assumed)
chk("C3e 30xi^2-10xi+1 has no real root (discriminant < 0): divergence for EVERY real xi",
    sp.discriminant(30*xi**2-10*xi+1, xi) < 0, f"disc = {sp.discriminant(30*xi**2-10*xi+1, xi)}")
print(f"   xi=0: C_0000 = {cs0}/r^8 (spacelike), {ct0}/tau^8 (timelike)")
# not locally integrable: int_delta^1 r^2 r^-8 dr ~ delta^-5 ; int_delta^1 tau^-8 dtau ~ delta^-7
d_ = sp.symbols("delta", positive=True)
chk("C3d r^-8 not locally integrable in 3D space nor along a line",
    sp.limit(sp.integrate(r**-6, (r, d_, 1)), d_, 0) == sp.oo and sp.limit(sp.integrate(tau**-8, (tau, d_, 1)), d_, 0) == sp.oo)

# ---------------- C4: smeared variance finite with i eps ----------------
mp.mp.dps = 30
tau0 = mp.mpf(1)
Fac = lambda u: mp.e**(-u**2/(2*tau0**2))/(mp.sqrt(2*mp.pi)*tau0)   # autocorrelation of Gaussian f = e^{-t^2/tau^2}/(sqrt(pi) tau)
for eps in (mp.mpf("0.7"), mp.mpf("0.3")):
    lhs = mp.quad(lambda u: Fac(u)*(u-1j*eps)**-8, [-mp.inf, -1, 0, 1, mp.inf])
    rhs = mp.quad(lambda w: w**7*mp.e**(-eps*w)*mp.e**(-w**2*tau0**2/2), [0, mp.inf])/mp.factorial(7)
    rel = abs(lhs-rhs)/abs(rhs)
    chk(f"C4a Fourier identity at eps={eps}: int F(u)(u-i eps)^-8 du = (1/7!) int w^7 e^-eps w |f^|^2", rel < 1e-15,
        f"lhs={mp.nstr(lhs,12)} rhs={mp.nstr(rhs,12)}")
lim = mp.quad(lambda w: w**7*mp.e**(-w**2*tau0**2/2), [0, mp.inf])/mp.factorial(7)
chk("C4b eps->0 limit finite and = 48/(7! tau^8) = 1/105", abs(lim - mp.mpf(48)/mp.factorial(7)) < 1e-25, f"{mp.nstr(lim,15)}")
# the same without i eps (pointwise kernel) diverges like delta^-7:
vals = []
for dl in (mp.mpf("1e-1"), mp.mpf("1e-2")):
    v = 2*mp.quad(lambda u: Fac(u)*u**-8, [dl, 1, mp.inf])
    vals.append(v)
ratio = vals[1]/vals[0]
chk("C4c without i*eps the cut-off integral scales ~ delta^-7 (divergent)", 0.9e7 < ratio < 1.1e7, f"ratio(1e-2 vs 1e-1) = {mp.nstr(ratio,6)}")

print("ALL PASS" if ok else "SOME FAIL")
sys.exit(0 if ok else 1)
