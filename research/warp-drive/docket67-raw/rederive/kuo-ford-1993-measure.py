#!/usr/bin/env python3
r"""
DOCKET 67 -- re-derivation for key kuo-ford-1993-measure.

Source READ: Kuo & Ford, gr-qc/9304008 v1 (text layer via alphaXiv), Eqs. (2.10)-(2.16),
(3.1)-(3.2), (3.39)-(3.45), Sec. V.  Journal PRD 47, 4510 NOT read.

Everything here is computed independently of research/warp-drive (nothing imported from it).

 A  KF's own algebra, massless minimally coupled scalar, diagonal G (sympy, exact)
    A1  <:phidot^2:> = (rho + p1 + p2 + p3)/2  -> its SQUARE carries 1/4, KF (3.41) prints 1/2
    A2  (3.43) with 1/8 == (1/2) SUM G_AA^2 / rho^2                 (so (3.43) is right)
    A3  RHS(3.43) == 1/2 + |xi|^2/2 identically  -> min 1/2 at xi = 0  (3.45)
    A4  Casimir xi = (-1,-1,3): Delta' = 6, Delta = 6/7 ; thermal xi = (1/3,1/3,1/3): 2/3, 2/5
    A5  (3.44) Delta = Delta'/(1+Delta') holds iff the (3.2) numerator is >= 0 (and X > 0)
 B  Fock space, single mode, built from KF (2.10)-(2.14) directly (numpy-free, exact sympy)
    B1  vacuum+2 state at eps = sqrt2, theta = pi/2: <:T00^2:> < <:T00:>^2  -- the
        normal-ordered 'variance' is NEGATIVE; (3.44) then fails (Delta = 1 by (3.2),
        Delta'/(1+Delta') = -1).  Non-Gaussian only; Gaussian states cannot do this.
    B2  thermal single mode (a MIXED Gaussian state): <a+^2 a^2> = 2 nbar^2 (Wick holds for
        a mixed quasifree state, which KF's stated Wick condition phi+|psi> = 0 does not cover)
        and the single-mode Delta' = 2.
 C  z3: the pointwise floor is 1/2 for 4 components (massless) and 2/5 for 5 (massive,
    m^2 phi^2 in T00); 1/2 is NOT a floor when m > 0.
 D  the tree's smeared use (mpmath): thermal normal-ordered phidot kernel g(u), beta = 1
    D0  G_xx / G_00 = 1/3 at r = 0 for each image term (wave eq + isotropy) -> the 2/3 factor
    D1  g(0) = pi^2/30 (closed form vs Fourier integral)
    D2  ||g^2||_1 = 180 (zeta6 - zeta7)/pi^3 (Parseval, exact series vs quadrature)
    D3  Delta'_f(tau = beta) with h Gaussian of s.d. tau; compare tree's 0.1186
    D4  crossing Delta'_f = 1/2; compare tree's TAU_STAR_OVER_BETA = 0.140196
    D5  Hoelder bound at tau = beta >= D3
"""
import sys
import sympy as sp
import mpmath as mp
mp.mp.dps = 40

OK = []


def chk(name, cond, detail=""):
    OK.append(bool(cond))
    print(("PASS " if cond else "FAIL ") + name + ("   " + detail if detail else ""))


# ------------------------------------------------------------------------- A
a, b1, b2, b3 = sp.symbols('a b1 b2 b3', real=True)       # <:phidot^2:>, <:phi_i^2:>
B = b1 + b2 + b3
rho = (a + B) / 2
p = [bi + (a - B) / 2 for bi in (b1, b2, b3)]              # T_ii = phi_i^2 + (phidot^2 - |grad|^2)/2
chk("A1 <:phidot^2:> = (rho+p1+p2+p3)/2", sp.simplify((rho + sum(p)) / 2 - a) == 0)
chk("A1 <:phi_x^2:> = (rho+p1-p2-p3)/2", sp.simplify((rho + p[0] - p[1] - p[2]) / 2 - b1) == 0)
chk("A1 KF (3.41) as printed [<:phidot^2:>^2 = (1/2)(rho+Sp)^2] is NOT an identity",
    sp.simplify(a**2 - sp.Rational(1, 2) * (rho + sum(p))**2) != 0,
    "exact coefficient is 1/4")
S2 = (a**2 + b1**2 + b2**2 + b3**2) / 2                     # (3.40) bracket: <:T00^2:> - rho^2
x1, x2, x3 = [pi / rho for pi in p]
rhs343 = sp.Rational(1, 8) * ((1 + x1 + x2 + x3)**2 + (1 + x1 - x2 - x3)**2
                              + (1 - x1 + x2 - x3)**2 + (1 - x1 - x2 + x3)**2)
chk("A2 (3.43) with 1/8 equals (1/2) SUM G_AA^2 / rho^2", sp.simplify(rhs343 - S2 / rho**2) == 0)
X1, X2, X3 = sp.symbols('xi1 xi2 xi3', real=True)
r343 = sp.Rational(1, 8) * ((1 + X1 + X2 + X3)**2 + (1 + X1 - X2 - X3)**2
                            + (1 - X1 + X2 - X3)**2 + (1 - X1 - X2 + X3)**2)
chk("A3 RHS(3.43) == 1/2 + (xi1^2+xi2^2+xi3^2)/2", sp.expand(r343 - (sp.Rational(1, 2) + (X1**2 + X2**2 + X3**2) / 2)) == 0)
cas = r343.subs({X1: -1, X2: -1, X3: 3})
thm = r343.subs({X1: sp.Rational(1, 3), X2: sp.Rational(1, 3), X3: sp.Rational(1, 3)})
chk("A4 Casimir (periodic) Delta' = 6, Delta = 6/7", cas == 6 and sp.nsimplify(cas / (1 + cas)) == sp.Rational(6, 7))
chk("A4 thermal (p = rho/3) Delta' = 2/3, Delta = 2/5", thm == sp.Rational(2, 3) and thm / (1 + thm) == sp.Rational(2, 5))
Xs, r = sp.symbols('X r', positive=True)                     # X = <:T00^2:>, r = rho^2
Dp = (Xs - r) / r
chk("A5 (3.44): Delta'/(1+Delta') == (X - rho^2)/X identically (sign NOT absolute)",
    sp.simplify(Dp / (1 + Dp) - (Xs - r) / Xs) == 0)

# ------------------------------------------------------------------------- B
N = 12                                                      # Fock truncation (states used need <= 4)
A_ = sp.zeros(N, N)
for n in range(1, N):
    A_[n - 1, n] = sp.sqrt(n)
Ad = A_.T
th = sp.symbols('theta', real=True)
# :T00: = K ( 2 a+a - e^{2i th} a^2 - e^{-2i th} a+^2 )   from KF (2.10),(2.12)-(2.14); K = 1
terms = [(2, 1, 1), (-sp.exp(2 * sp.I * th), 0, 2), (-sp.exp(-2 * sp.I * th), 2, 0)]   # (coef, #a+, #a)


def mono(j, k):
    M = sp.eye(N)
    for _ in range(j):
        M = M * Ad
    for _ in range(k):
        M = M * A_
    return M


T1op = sum((c * mono(j, k) for c, j, k in terms), sp.zeros(N, N))
T2op = sp.zeros(N, N)                                       # :T00^2: = sum c c' a+^(j+j') a^(k+k')
for c, j, k in terms:
    for c2, j2, k2 in terms:
        T2op += c * c2 * mono(j + j2, k + k2)
eps = sp.symbols('epsilon', positive=True)
psi = sp.zeros(N, 1)
psi[0] = 1 / sp.sqrt(1 + eps**2)
psi[2] = eps / sp.sqrt(1 + eps**2)
ev = lambda O: sp.simplify((psi.H * O * psi)[0])
rho_v = sp.simplify(sp.expand_complex(ev(T1op)))
X_v = sp.simplify(sp.expand_complex(ev(T2op)))
_d0 = rho_v - 2 * eps * (2 * eps - sp.sqrt(2) * sp.cos(2 * th)) / (1 + eps**2)
chk("B0 <:T00:> vac+2 = 2 eps (2 eps - sqrt2 cos 2th)/(1+eps^2)  [KF (2.16) middle line; final line prints half]",
    all(abs(complex(_d0.subs({eps: e_, th: t_}).evalf(30))) < 1e-25
        for e_, t_ in ((sp.Rational(1, 10), 0), (sp.Rational(7, 3), sp.Rational(2, 5)), (sp.sqrt(2), sp.pi / 2), (5, 3))),
    "checked at 4 points, 30 digits")
chk("B0 <:T00^2:> vac+2 = 12 eps^2/(1+eps^2)  [KF (3.7) prints (1+eps^2)^2]",
    sp.simplify(X_v - 12 * eps**2 / (1 + eps**2)) == 0)
at = {eps: sp.sqrt(2), th: sp.pi / 2}
rv, Xv = sp.nsimplify(rho_v.subs(at)), sp.nsimplify(X_v.subs(at))
num = sp.simplify(Xv - rv**2)
chk("B1 eps=sqrt2, theta=pi/2: <:T00^2:> - <:T00:>^2 < 0 (normal-ordered 'variance' negative)",
    num < 0, "X = %s, rho^2 = %s, numerator = %s" % (Xv, sp.simplify(rv**2), num))
D32 = sp.Abs(num / Xv)
Dpv = num / rv**2
chk("B1 there (3.2) gives Delta = 1 but Delta'/(1+Delta') = -1: (3.44) fails off the Gaussian class",
    sp.simplify(D32 - 1) == 0 and sp.simplify(Dpv / (1 + Dpv) + 1) == 0, "Delta' = %s" % sp.simplify(Dpv))
# B2 thermal single mode: p_n = (1-q) q^n ; nbar = q/(1-q)
q = sp.Rational(1, 3)
nb = q / (1 - q)
Ninf = 400
mpq = mp.mpf(1) / 3
m2 = mp.nsum(lambda n: (1 - mpq) * mpq**n * n * (n - 1), [0, mp.inf])
chk("B2 thermal mode <a+^2 a^2> = 2 nbar^2 (Wick for a MIXED Gaussian state)",
    abs(m2 - 2 * mp.mpf(nb)**2) < mp.mpf(10)**-25, "%s vs %s" % (mp.nstr(m2, 20), sp.nsimplify(2 * nb**2)))
# thermal single mode: <:T:> = 2 nbar ; <:T^2:> = coefficient of a+^2 a^2 in :T^2: times 2 nbar^2
coef22 = sum(c * c2 for c, j, k in terms for c2, j2, k2 in terms if j + j2 == 2 and k + k2 == 2)
coef22 = sp.simplify(coef22)
X_th = coef22 * 2 * nb**2
rho_th = 2 * nb
chk("B2 thermal single mode Delta' = 2 (= squeezed-vacuum single-mode value)", sp.simplify((X_th - rho_th**2) / rho_th**2) == 2,
    "coef(a+^2a^2) = %s" % coef22)

# ------------------------------------------------------------------------- C
try:
    import z3

    def floor_proved(k, fl):
        g = [z3.Real('g%d' % i) for i in range(k)]
        s = z3.Solver()
        tr = z3.Sum(g)
        s.add(z3.Not(2 * z3.Sum([x * x for x in g]) >= fl * tr * tr))
        return s.check() == z3.unsat

    chk("C1 massless, 4 components: 2 SUM G^2 >= (1/2) (tr G)^2 proved", floor_proved(4, z3.RealVal('1/2')))
    chk("C2 massive, 5 components (m^2 phi^2 in T00): 1/2 is NOT a floor (z3 sat)", not floor_proved(5, z3.RealVal('1/2')))
    chk("C3 massive, 5 components: floor 2/5 proved", floor_proved(5, z3.RealVal('2/5')))
except ImportError:
    print("SKIP C: z3 not installed")

# ------------------------------------------------------------------------- D
mp.mp.dps = 40
u, t, x, y, z, al = sp.symbols('u t x y z alpha', real=True)
F = 1 / (-(t + sp.I * al)**2 + x**2 + y**2 + z**2)
Gxx = sp.diff(F, x, 2).subs({x: 0, y: 0, z: 0})
Gtt = sp.diff(F, t, 2).subs({x: 0, y: 0, z: 0})
chk("D0 each image term: d_x^2 W / d_t^2 W = 1/3 at r = 0 (so G_ii = G_00/3, factor 2/3)",
    sp.simplify(Gxx / Gtt - sp.Rational(1, 3)) == 0)
base = sp.pi / 2 * sp.coth(sp.pi * u) - 1 / (2 * u)
gexpr = -sp.diff(base, u, 3) / (2 * sp.pi**2)
gser = sp.series(gexpr, u, 0, 12).removeO()
g_cf = sp.lambdify(u, gexpr, 'mpmath')
g_sr = sp.lambdify(u, gser, 'mpmath')


def g(uu):
    uu = mp.mpf(uu)
    return g_sr(uu) if abs(uu) < mp.mpf('0.001') else g_cf(uu)


def g_fourier(uu):
    uu = mp.mpf(uu)
    return mp.quad(lambda k: k**3 * mp.cos(k * uu) / mp.expm1(k), [0, 10, 40, 120]) / (2 * mp.pi**2)


chk("D1 g(0) = pi^2/30", abs(g(0) - mp.pi**2 / 30) < mp.mpf(10)**-30, mp.nstr(g(0), 15))
chk("D1 closed form = Fourier form at u = 0.03, 0.4, 2.5",
    all(abs(g(v) - g_fourier(v)) < mp.mpf(10)**-20 for v in ('0.03', '0.4', '2.5')))
z6z7 = mp.zeta(6) - mp.zeta(7)
I6 = mp.quad(lambda k: k**6 / mp.expm1(k)**2, [0, 10, 40, 150])
chk("D2 INT k^6/(e^k-1)^2 = 720 (zeta6 - zeta7)", abs(I6 - 720 * z6z7) < mp.mpf(10)**-25)
L1 = 2 * mp.quad(lambda v: g(v)**2, [0, 0.001, 0.05, 0.5, 2, 8, 40, mp.inf])
chk("D2 ||g^2||_1 = 180 (zeta6 - zeta7)/pi^3", abs(L1 - 180 * z6z7 / mp.pi**3) < mp.mpf(10)**-18,
    "%s" % mp.nstr(L1, 18))
mp.mp.dps = 25


def dprime(tau):
    tau = mp.mpf(tau)
    h = lambda v: mp.exp(-v**2 / (2 * tau**2)) / (tau * mp.sqrt(2 * mp.pi))
    I = 2 * mp.quad(lambda v: h(v) * g(v)**2, [0, 0.001, 0.05, 0.5, 2, 8, 40, mp.inf])
    return mp.mpf(2) / 3 * I / g(0)**2


d1 = dprime(1)
chk("D3 Delta'_f(tau = beta) = 0.1186 (tree, 4 digits)", abs(d1 - mp.mpf('0.1186')) < mp.mpf('5e-5'), mp.nstr(d1, 10))
d_small = dprime('0.002')
chk("D3 Delta'_f -> 2/3 as tau -> 0 (pointwise thermal value)", abs(d_small - mp.mpf(2) / 3) < mp.mpf('1e-3'), mp.nstr(d_small, 10))
ts = mp.findroot(lambda s: dprime(s) - mp.mpf(1) / 2, mp.mpf('0.14'))
chk("D4 crossing tau*/beta = 0.140196 (tree, 6 digits)", abs(ts - mp.mpf('0.140196')) < mp.mpf('6e-7'), mp.nstr(ts, 12))
hoel = 108000 * z6z7 / (mp.sqrt(2 * mp.pi) * mp.pi**7)
hoel2 = mp.mpf(2) / 3 * (1 / (mp.sqrt(2 * mp.pi))) * (180 * z6z7 / mp.pi**3) / (mp.pi**2 / 30)**2
chk("D5 Hoelder coefficient 108000(z6-z7)/(sqrt(2pi) pi^7) == (2/3)||f||_2^2 ||g^2||_1/rho^2 at tau = beta",
    abs(hoel - hoel2) < mp.mpf(10)**-20, mp.nstr(hoel, 10))
chk("D5 bound >= measured at tau = beta, and < 1/2", d1 <= hoel < mp.mpf(1) / 2)

print("\n%d/%d PASS" % (sum(OK), len(OK)))
sys.exit(0 if all(OK) else 1)
