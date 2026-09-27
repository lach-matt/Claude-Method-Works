#!/usr/bin/env python3
"""D67 audit -- minkowski-wightman-wick.

Independent re-derivation (does NOT import noise.py) of:
  (1) W = 1/(4 pi^2 sigma), sigma = |x-x'|^2 - (t-t')^2, and its point-split
      derivatives on an inertial worldline: D_00 = 3/(2 pi^2 u^4) (FFR 1204.3570
      Eq. (25)), D_0i = 0 (FFR Eq. (32)), D_ij = (1/3) delta_ij D_00 (FFR Eq. (33));
      W itself on the worldline = -1/(4 pi^2 u^2) (FFR Eq. (24)).
  (2) Wick's theorem for normal-ordered squares in a quasifree (Fock vacuum)
      state: <:A^2::B^2:> = 2 <A B>^2, checked in a truncated 2-mode Fock space
      with random complex mode coefficients (not just asserted).
      Consequence: <:rho::rho':> = (1/2) SUM_AB D_AB^2 = 3/(2 pi^4 u^8).
  (3) The Fourier identity with its PHASE: INT_0^oo w^(n-1) e^{-iw(u-i eps)} dw
      = (n-1)!/(i^n (u - i eps)^n), i.e.
      1/(u-i0)^n = (i^n/(n-1)!) INT_0^oo w^(n-1) e^{-iwu} dw.
      The unphased form (1/(n-1)!) INT ... holds iff i^n = 1, i.e. n = 0 mod 4;
      the tree uses n = 8 only (noise.py:397-399 says 'since i^n = 1 for n = 8').
      Checked symbolically and numerically at eps > 0 for n = 1..8.
  (4) kappa = (3/(2 pi^4))/7! = 1/(3360 pi^4) with fhat(w) = INT f e^{iwt} dt
      (FFR convention A2); Lorentzian K = 3/(512 pi^4), a_2(rho_S) = 3/2,
      a_2(phidot^2) = 9/2, a_2(phi^2) = 2 (FFR Table I); Gaussian K = 1/(70 pi^4);
      FFR Eq. (34) ratio C_2(rho_S)/C_2(phidot^2) = 1/4 + 3/36 = 1/3.
  (5) K_F for Fewster's clamped sampler f = g^2 on [0,1], recomputed here from
      scratch (exact fhat as a sum of exponentials, mpmath quadrature to W plus
      the analytic F4^2/W^2 tail), compared with noise.py's K_F_FIXTURE
      19.80242121506098 (read as a number only; noise.py is not imported).
Exit 0 iff every check passes.
"""
import sys
import sympy as sp
import mpmath as mp
import numpy as np

fails = []


def check(label, ok, detail=""):
    print("  [%s] %s %s" % ("PASS" if ok else "FAIL", label, detail))
    if not ok:
        fails.append(label)


print("(1) point-split derivatives of W = 1/(4 pi^2 sigma)")
t, tp, x, y, z, xp, yp, zp = sp.symbols('t tp x y z xp yp zp', real=True)
u = sp.symbols('u', positive=True)
sig = (x - xp)**2 + (y - yp)**2 + (z - zp)**2 - (t - tp)**2
W = 1 / (4 * sp.pi**2 * sig)
X, XP = (t, x, y, z), (tp, xp, yp, zp)
wl = {x: 0, y: 0, z: 0, xp: 0, yp: 0, zp: 0}
Wwl = sp.simplify(W.subs(wl).subs({t: u, tp: 0}))
check("W on worldline = -1/(4 pi^2 u^2)  [FFR Eq.(24)]",
      sp.simplify(Wwl + 1 / (4 * sp.pi**2 * u**2)) == 0)
D = [[sp.simplify(sp.diff(W, X[A], XP[B]).subs(wl).subs({t: u, tp: 0}))
      for B in range(4)] for A in range(4)]
check("D_00 = 3/(2 pi^2 u^4)  [FFR Eq.(25)]", sp.simplify(D[0][0] - 3 / (2 * sp.pi**2 * u**4)) == 0)
check("D_0i = D_i0 = 0  [FFR Eq.(32)]", all(sp.simplify(D[0][i]) == 0 and sp.simplify(D[i][0]) == 0 for i in (1, 2, 3)))
check("D_ij = (1/3) delta_ij D_00  [FFR Eq.(33)]",
      all(sp.simplify(D[i][j] - (sp.Rational(1, 3) * D[0][0] if i == j else 0)) == 0
          for i in (1, 2, 3) for j in (1, 2, 3)))
# Klein-Gordon: box W = 0 away from sigma = 0
box = sp.simplify(-sp.diff(W, t, 2) + sp.diff(W, x, 2) + sp.diff(W, y, 2) + sp.diff(W, z, 2))
check("box_x W = 0 off the light cone (massless, no curvature term needed in flat space)", box == 0)
# i0 prescription: with t -> t - i eps, W is analytic in the lower half t-t' plane ->
# positive frequency. Check numerically: W(u - i eps) = -1/(4pi^2 (u - i eps)^2) equals
# (1/4pi^2) INT_0^oo a e^{-i a (u - i eps)} da  (FFR Eq.(24), the positive-frequency rep).
uu, ee = mp.mpf('0.7'), mp.mpf('1.5')
OSC = [mp.mpf(k) / 2 for k in range(0, 161)] + [mp.inf]  # split the oscillatory range
lhs = -1 / (4 * mp.pi**2 * (uu - 1j * ee)**2)
rhs = mp.quad(lambda a: a * mp.exp(-1j * a * (uu - 1j * ee)), OSC) / (4 * mp.pi**2)
check("W(u - i eps) = (1/4pi^2) INT_0^oo a e^{-ia(u-i eps)} da  [FFR Eq.(24)]", abs(lhs - rhs) < 1e-12,
      "(|diff| = %.2e)" % float(abs(lhs - rhs)))

print("\n(2) Wick's theorem for normal-ordered squares, truncated 2-mode Fock space")
N = 7  # levels per mode; :A^2: on |0> reaches at most 2 quanta, so N = 7 is exact
a1 = np.diag(np.sqrt(np.arange(1, N)), 1)
I = np.eye(N)
A1 = np.kron(a1, I)
A2 = np.kron(I, a1)
vac = np.zeros(N * N, dtype=complex); vac[0] = 1
rng = np.random.default_rng(67)


def field(c):
    """A = c1 a1 + c2 a2 + h.c. -- a generic linear field (positive + negative freq part)."""
    ann = c[0] * A1 + c[1] * A2
    return ann, ann.conj().T


def wick_sq(c):
    ann, cre = field(c)
    return ann @ ann + cre @ cre + 2 * cre @ ann  # :A^2:


worst = 0.0
for trial in range(20):
    ca = rng.normal(size=2) + 1j * rng.normal(size=2)
    cb = rng.normal(size=2) + 1j * rng.normal(size=2)
    annA, creA = field(ca); annB, creB = field(cb)
    Aop, Bop = annA + creA, annB + creB
    two = vac.conj() @ Aop @ Bop @ vac
    four = vac.conj() @ wick_sq(ca) @ wick_sq(cb) @ vac
    worst = max(worst, abs(four - 2 * two**2))
check("<0|:A^2::B^2:|0> = 2 <0|A B|0>^2 over 20 random complex mode pairs", worst < 1e-10,
      "(max |diff| = %.1e)" % worst)
# the tree's step: rho = (1/2) SUM_A :(d_A phi)^2:  ->  <:rho::rho':> = (1/4) SUM_AB 2 D_AB^2
rho_uu = sp.simplify(sp.Rational(1, 2) * sum(D[A][B]**2 for A in range(4) for B in range(4)))
check("<:rho::rho':>_0 = (1/2) SUM_AB D_AB^2 = 3/(2 pi^4 u^8)",
      sp.simplify(rho_uu - 3 / (2 * sp.pi**4 * u**8)) == 0)
# independent route to the same number through FFR's Eq.(34) structure
check("FFR Eq.(34): (1/2)[D00^2 + 3 (D00/3)^2] = (1/3) * 2 D00^2 * (1/2)... ratio to <:phidot^2 phidot^2:> = 1/3",
      sp.simplify(rho_uu / (2 * D[0][0]**2) - sp.Rational(1, 3)) == 0)

print("\n(3) the Fourier identity, with its phase")
w = sp.symbols('w', positive=True)
a = sp.symbols('a', positive=True)
for n in range(1, 9):
    val = sp.simplify(sp.integrate(w**(n - 1) * sp.exp(-a * w), (w, 0, sp.oo)) * a**n)
    assert val == sp.factorial(n - 1)
check("INT_0^oo w^(n-1) e^{-aw} dw = (n-1)!/a^n, n = 1..8 (sympy, a > 0)", True)
phase_ok = True
for n in range(1, 9):
    num = mp.quad(lambda ww: ww**(n - 1) * mp.exp(-1j * ww * (uu - 1j * ee)), OSC)
    pred_phased = mp.factorial(n - 1) / ((1j)**n * (uu - 1j * ee)**n)
    pred_unphased = mp.factorial(n - 1) / ((uu - 1j * ee)**n)
    ph = abs(num - pred_phased) / abs(num)
    un = abs(num - pred_unphased) / abs(num)
    unphased_holds = un < 1e-10
    phase_ok &= ph < 1e-10 and (unphased_holds == (n % 4 == 0))
    print("      n=%d  phased rel.err %.1e   unphased rel.err %.1e   i^n = %s" %
          (n, float(ph), float(un), sp.I**n))
check("1/(u-i0)^n = (i^n/(n-1)!) INT w^(n-1) e^{-iwu}; unphased form true iff n = 0 mod 4", phase_ok)
check("n = 8 (the tree's only use): i^8 = 1, so (1/7!) INT w^7 e^{-iwu} is exact", sp.I**8 == 1)

print("\n(4) kappa and the controls against FFR 1204.3570 Table I")
kappa = sp.Rational(3, 2) / sp.pi**4 / sp.factorial(7)
check("kappa = (3/(2 pi^4))/7! = 1/(3360 pi^4)", sp.simplify(kappa - 1 / (3360 * sp.pi**4)) == 0)
s, tau = sp.symbols('s tau', positive=True)
lor = sp.simplify(kappa * sp.integrate(s**7 * sp.exp(-2 * s * tau), (s, 0, sp.oo)))
check("Lorentzian (fhat = e^{-|w| tau}): K = 3/(512 pi^4)", sp.simplify(lor * tau**8 - 3 / (512 * sp.pi**4)) == 0)
check("a_2(rho_S) = (4 pi tau^2)^4 Var = 3/2  [FFR Table I]", sp.simplify((4 * sp.pi * tau**2)**4 * lor - sp.Rational(3, 2)) == 0)
# phidot^2: <:phidot^2 phidot'^2:> = 2 D00^2 = 9/(2 pi^4 u^8) -> coefficient/7!
kp = sp.Rational(9, 2) / sp.pi**4 / sp.factorial(7)
lorp = sp.simplify(kp * sp.integrate(s**7 * sp.exp(-2 * s * tau), (s, 0, sp.oo)))
check("a_2(phidot^2) = 9/2  [FFR Table I]", sp.simplify((4 * sp.pi * tau**2)**4 * lorp - sp.Rational(9, 2)) == 0)
# phi^2: <:phi^2 phi'^2:> = 2 W^2 = 2/(16 pi^4 u^4) = 1/(8 pi^4 u^4); 1/(u-i0)^4 = (1/3!) INT w^3 e^{-iwu}
k0 = sp.Rational(1, 8) / sp.pi**4 / sp.factorial(3)
lor0 = sp.simplify(k0 * sp.integrate(s**3 * sp.exp(-2 * s * tau), (s, 0, sp.oo)))
check("a_2(phi^2) = (4 pi tau)^4 Var = 2  [FFR Table I]", sp.simplify((4 * sp.pi * tau)**4 * lor0 - 2) == 0)
gau = sp.simplify(kappa * sp.integrate(s**7 * sp.exp(-s**2 * tau**2 / 2), (s, 0, sp.oo)))
check("Gaussian (fhat = e^{-w^2 tau^2/4}): K = 1/(70 pi^4)", sp.simplify(gau * tau**8 - 1 / (70 * sp.pi**4)) == 0)
# FFR's Table I connected-moment rule for n=2 (Appendix A): overall 32 tau^-(p+1) times
# INT w^p w'^p fhat(w+w')^2 ... cross-check a_2(phidot^2) with that rule directly
wp_ = sp.symbols('wp', positive=True)
a2_rule = sp.simplify(32 * sp.integrate(sp.integrate(w**3 * wp_**3 * sp.exp(-2 * (w + wp_)), (w, 0, sp.oo)), (wp_, 0, sp.oo)))
check("FFR App. A n=2 rule (32 INT INT w^3 w'^3 e^{-2(w+w')}) = 9/2 at tau = 1", a2_rule == sp.Rational(9, 2),
      "(got %s)" % a2_rule)
# mode-sum route (F) ingredients the tree also cites
cs = sp.symbols('cs', real=True)
check("angular average of (1 + cos theta)^2 = 4/3 over d(cos)/2, i.e. INT_{-1}^{1} = 8/3",
      sp.integrate((1 + cs)**2, (cs, -1, 1)) == sp.Rational(8, 3))
check("Beta integral INT_0^s w^3 (s-w)^3 dw = s^7/140",
      sp.simplify(sp.integrate(w**3 * (s - w)**3, (w, 0, s)) - s**7 / 140) == 0)

# "for any real sampler" (noise.py:63) needs INT w^7 |fhat|^2 < oo: a box sampler on [0,1]
# (|fhat|^2 = 4 sin^2(w/2)/w^2) makes the w-integral diverge like W^6 -- Var_0 = +oo there.
Wb = sp.symbols('Wb', positive=True)
box_growth = sp.limit(sp.integrate(w**7 * 2 / w**2, (w, 1, Wb)) / Wb**6, Wb, sp.oo)  # mean of 4 sin^2(w/2) is 2
check("box sampler: the (V) integral grows like W^6/3 (finite only when fhat = o(w^-4))", box_growth == sp.Rational(1, 3))

print("\n(5) K_F for Fewster's clamped sampler, recomputed from scratch")
mp.mp.dps = 30
mu = mp.findroot(lambda m: mp.cosh(m) * mp.cos(m) - 1, 4.73)
sg = (mp.cosh(mu) - mp.cos(mu)) / (mp.sinh(mu) - mp.sin(mu))
# g(x) = cosh(mu x) - cos(mu x) - sg (sinh(mu x) - sin(mu x)) as SUM c_k e^{l_k x}
terms = [(mp.mpf(1) / 2 - sg / 2, mu), (mp.mpf(1) / 2 + sg / 2, -mu),
         (-mp.mpf(1) / 2 + sg / (2j), 1j * mu), (-mp.mpf(1) / 2 - sg / (2j), -1j * mu)]
# check: -cos(mu x) + sg sin(mu x) = -(e^{i}+e^{-i})/2 + sg (e^{i}-e^{-i})/(2i)
sq = {}
for c1, l1 in terms:
    for c2, l2 in terms:
        key = l1 + l2
        sq[key] = sq.get(key, 0) + c1 * c2


def g(xx):
    return mp.cosh(mu * xx) - mp.cos(mu * xx) - sg * (mp.sinh(mu * xx) - mp.sin(mu * xx))


def int_exp(l):
    return mp.mpf(1) if abs(l) < mp.mpf(10)**-25 else (mp.exp(l) - 1) / l


norm = mp.re(sum(c * int_exp(l) for l, c in sq.items()))
check("g^2 as exponential sum integrates to the quadrature value", abs(norm - mp.quad(lambda xx: g(xx)**2, [0, 1])) < 1e-20)


def fhat(ww):
    return sum(c * int_exp(l + 1j * ww) for l, c in sq.items()) / norm


check("fhat(0) = 1 (f = g^2 / ||g||^2 is a probability density)", abs(fhat(0) - 1) < 1e-20)
# exact asymptotic tail: fhat(w) = SUM_{k>=4} f_k(0) (e^{iw} - (-1)^k)/(iw)^{k+1}, f_k = k-th derivative
# (f symmetric about 1/2, f_k(1) = (-1)^k f_k(0); f_0..f_3 vanish at the ends since g ~ x^2)
fk = [mp.re(sum(c * l**k for l, c in sq.items())) / norm for k in range(0, 14)]
check("f and its first three derivatives vanish at the clamped end (so fhat ~ w^-5)",
      all(abs(fk[k]) < 1e-15 * abs(fk[4]) for k in range(4)))
F4 = fk[4]
check("4th derivative at 0 = 6 g2(0)^2/||g||^2 = 24 mu^4/||g||^2", abs(F4 - 24 * mu**4 / norm) < 1e-18 * F4)


def tail(Wc, K=13):
    """INT_Wc^oo w^7 |asymptotic fhat|^2 dw in closed form (generalised exponential integrals)."""
    tot = mp.mpc(0)
    for j in range(4, K + 1):
        for k in range(4, K + 1):
            cjk = fk[j] * fk[k] / ((1j)**(j + 1) * (-1j)**(k + 1))
            m = j + k - 5            # integrand power w^-m
            sj, sk = (-1)**j, (-1)**k
            plain = Wc**(1 - m) / (m - 1)
            ep = Wc**(1 - m) * mp.expint(m, -1j * Wc)   # INT_W^oo w^-m e^{+iw}
            em = Wc**(1 - m) * mp.expint(m, 1j * Wc)    # INT_W^oo w^-m e^{-iw}
            tot += cjk * ((1 + sj * sk) * plain - sk * ep - sj * em)
    return mp.re(tot)


def K_at(Wc):
    pts = [mp.mpf(0)] + [mp.pi * k for k in range(1, int(Wc / mp.pi) + 1)] + [Wc]
    body = mp.quad(lambda ww: ww**7 * abs(fhat(ww))**2, pts)
    return (body + tail(Wc)) / (3360 * mp.pi**4)


Ktilde, Ktilde2 = K_at(mp.mpf(400)), K_at(mp.mpf(250))
K_FIX = mp.mpf('19.80242121506098')
print("      mu_1 = %s ; F4 = f''''(0) = %s" % (mp.nstr(mu, 16), mp.nstr(F4, 12)))
print("      K_F (W=400) = %s ; K_F (W=250) = %s ; fixture = %s" %
      (mp.nstr(Ktilde, 16), mp.nstr(Ktilde2, 16), mp.nstr(K_FIX, 16)))
rel = abs(Ktilde - K_FIX) / K_FIX
check("independent K_F agrees with noise.py K_F_FIXTURE to < 1e-11 relative", rel < 1e-11, "(rel %.2e)" % float(rel))
check("cutoff stability W=250 vs W=400 < 1e-12 relative", abs(Ktilde - Ktilde2) / Ktilde < 1e-12, "(rel %.2e)" % float(abs(Ktilde - Ktilde2) / Ktilde))

print()
if fails:
    print("FAILURES:", fails)
    sys.exit(1)
print("ALL PASS")
