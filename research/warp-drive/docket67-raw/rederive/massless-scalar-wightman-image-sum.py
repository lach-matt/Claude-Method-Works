#!/usr/bin/env python3
r"""
DOCKET 67 -- audit of 'massless-scalar-wightman-image-sum' (fluctuation.py:83-85, 264-281, 321-323).

Re-derives, WITHOUT importing anything from research/, every link the tree's
image_stress() relies on, each by a route independent of the image method where
one exists:

  W1  W = 1/(4 pi^2 sigma), sigma = -dt^2+dx^2+dy^2+dz^2, solves the wave equation off sigma=0
  W2  its normalisation equals the Fock mode integral  INT d^3k/((2pi)^3 2k) e^{-k tau + i k.x}
      (imaginary time t = -i tau, exact in sympy)
  W3  sign of the point-split derivative: <d_A phi(x) d'_B phi(x')> = -d_A d_B W(x-x')
      (checked on the mode integral: d/dt d/dt' of e^{-ik(t-t')} gives +k^2 = -d_dt^2)
  P1  periodic identification z ~ z+L: image sum SUM_{n!=0} W(nL) gives <:phi^2:> = 1/(12 L^2);
      an INDEPENDENT regulated mode sum (discrete k_z, exp(-eps omega) cutoff) gives the same
  P2  periodic <:T00:> from the regulated MODE SUM = -pi^2/(90 L^4)  (no images used)
  P3  periodic image-sum G matrix, rho, p_i, Delta' = 6, Delta = 6/7   (the tree's numbers)
  T1  thermal: Planck mode integral rho = pi^2/(30 beta^4) (no images used)
  T2  thermal Wightman difference: imaginary-time image sum SUM_{n!=0} W(t+i n beta, r)
      equals the Planck mode integral (1/(2 pi^2 r)) INT n(k) sin(kr) cos(kt) dk at non-coincident
      points (numeric, mpmath) -- this is the KMS/image identity the tree uses
  T3  thermal image-sum G: rho, p = rho/3, Delta' = 2/3, Delta = 2/5 (the tree's numbers)
  S1  doubling: SUM_{n>=1} x 2 == SUM_{n != 0} for every G_AB used (evenness in n)
  S2  Isserlis/Wick for normal-ordered moments of a zero-mean quasifree state:
      <:X_A^2 X_B^2:> = G_AA G_BB + 2 G_AB^2  =>  <:T00^2:> = rho^2 + (1/2) SUM G_AB^2
  X1  EXTENSION (not in the tree): Dirichlet parallel plates at separation a (images WITH
      reflections).  Machinery validated by conformal rho = -pi^2/(1440 a^4) at two z;
      minimal-coupling Delta' at the midpoint computed and compared with the T1 floor 1/2.
      Shows the tree's 'Casimir' 6, 6/7 is the PERIODIC geometry's value (KF's periodic case).
  C   controls that must FAIL: wrong sign on the point-split derivative; images at n beta
      (real-time shift) instead of i n beta.
"""
import sys
import sympy as sp
import mpmath as mp

RESULTS = []


def chk(name, ok):
    RESULTS.append((name, bool(ok)))
    print(("PASS  " if ok else "FAIL  ") + name)


dt, dx, dy, dz = sp.symbols('dt dx dy dz', real=True)
D = (dt, dx, dy, dz)
sig = -dt**2 + dx**2 + dy**2 + dz**2
W = 1 / (4 * sp.pi**2 * sig)

# ---------------------------------------------------------------- W1
box = -sp.diff(W, dt, 2) + sp.diff(W, dx, 2) + sp.diff(W, dy, 2) + sp.diff(W, dz, 2)
chk("W1 box W = 0 off the light cone", sp.simplify(box) == 0)

# ---------------------------------------------------------------- W2
k, r, tau = sp.symbols('k r tau', positive=True)
# INT d^3k/((2pi)^3 2k) e^{-k tau} e^{i k.x} = (1/(4 pi^2 r)) INT_0^oo e^{-k tau} sin(kr) dk
modeW = sp.integrate(sp.exp(-k * tau) * sp.sin(k * r), (k, 0, sp.oo)) / (4 * sp.pi**2 * r)
Wimag = W.subs({dt: -sp.I * tau, dx: r, dy: 0, dz: 0})
chk("W2 mode integral = 1/(4 pi^2 (tau^2 + r^2)) = W(t=-i tau)", sp.simplify(modeW - Wimag) == 0)

# ---------------------------------------------------------------- W3
# <phi-dot(x) phi-dot(x')> from modes: integrand gains (-ik)(+ik) = k^2 ; t-derivative of W(t-t') twice
# with respect to Delta gives -k^2 on e^{-ik Dt}, so the point-split value is -d^2 W / dDt^2.
kk, Dt = sp.symbols('kk Dt')
mode = sp.exp(-sp.I * kk * Dt)
ps = sp.diff(sp.exp(-sp.I * kk * (sp.Symbol('t') - sp.Symbol('tp'))), sp.Symbol('t'), sp.Symbol('tp'))
ps = ps.subs(sp.Symbol('t') - sp.Symbol('tp'), Dt)
ps = sp.simplify(ps.subs(sp.Symbol('t'), Dt + sp.Symbol('tp')))
chk("W3 d_t d_t' [mode] == -d^2/dDt^2 [mode]  (tree's sign)", sp.simplify(ps + sp.diff(mode, Dt, 2)) == 0)

# ---------------------------------------------------------------- image G builder (independent code)
n = sp.symbols('n', integer=True, positive=True)


def G_images(shift_t, shift_z, sign=-1, both=False):
    st, sz = shift_t, shift_z
    Wn = 1 / (4 * sp.pi**2 * (-(dt + st)**2 + dx**2 + dy**2 + (dz + sz)**2))
    G = sp.zeros(4, 4)
    for A in range(4):
        for B in range(4):
            term = sign * sp.diff(Wn, D[A], D[B])
            term = sp.simplify(term.subs({dt: 0, dx: 0, dy: 0, dz: 0}))
            G[A, B] = sp.simplify(2 * sp.summation(term, (n, 1, sp.oo)))
    rho = sp.simplify(sum(G[i, i] for i in range(4)) / 2)
    p = [sp.simplify(G[i, i] + (G[0, 0] - G[1, 1] - G[2, 2] - G[3, 3]) / 2) for i in (1, 2, 3)]
    Dp = sp.simplify(sum(G[A, B]**2 for A in range(4) for B in range(4)) / 2 / rho**2)
    return G, rho, p, Dp


L, beta, eps = sp.symbols('L beta epsilon', positive=True)

# ---------------------------------------------------------------- P1
phi2_img = sp.simplify(2 * sp.summation(1 / (4 * sp.pi**2 * (n * L)**2), (n, 1, sp.oo)))
chk("P1a image sum <:phi^2:>_L = 1/(12 L^2)", sp.simplify(phi2_img - 1 / (12 * L**2)) == 0)
# regulated mode sum: (1/L) SUM_kz e^{-eps|kz|}/(4 pi eps) - INT dkz/(2pi) e^{-eps|kz|}/(4 pi eps)
x = sp.pi * eps / L
disc = sp.coth(x) / (4 * sp.pi * eps * L)
cont = 1 / (4 * sp.pi**2 * eps**2)
lim = sp.series(disc - cont, eps, 0, 2).removeO()
chk("P1b regulated MODE SUM <:phi^2:>_L = 1/(12 L^2) (no images)", sp.simplify(lim - 1 / (12 * L**2)) == 0)

# ---------------------------------------------------------------- P2
# energy density = (1/L) SUM_kz INT d^2k/(2pi)^2 (omega/2) e^{-eps omega} - continuum
# INT d^2k omega e^{-eps omega} = 2 pi INT_{|kz|}^oo w^2 e^{-eps w} dw
a = sp.symbols('a', nonnegative=True)
w = sp.symbols('w', positive=True)
inner = sp.integrate(w**2 * sp.exp(-eps * w), (w, a, sp.oo))           # e^{-eps a}(a^2/eps + 2a/eps^2 + 2/eps^3)
per_kz = inner * 2 * sp.pi / (2 * sp.pi)**2 / 2                        # d^2k/(2pi)^2 * omega/2
c = 2 * sp.pi / L
q = sp.symbols('q', positive=True)
# SUM_{m in Z} f(|m| c) = f(0) + 2 SUM_{m>=1} f(m c); use closed geometric forms
m = sp.symbols('m', integer=True, positive=True)
# per_kz(a) = e^{-eps a}(a^2/eps + 2a/eps^2 + 2/eps^3)/(4 pi); with a = m c and y = e^{-eps c}, use the exact
# geometric identities SUM y^m = y/(1-y), SUM m y^m = y/(1-y)^2, SUM m^2 y^m = y(1+y)/(1-y)^3
y = sp.exp(-eps * c)
S1, S2, S3 = y / (1 - y), y / (1 - y)**2, y * (1 + y) / (1 - y)**3
chk("P2 pre: per-k_z integral is e^{-eps a}(a^2/eps + 2a/eps^2 + 2/eps^3)/(4 pi)",
    all(abs(sp.N((per_kz - sp.exp(-eps * a) * (a**2 / eps + 2 * a / eps**2 + 2 / eps**3) / (4 * sp.pi)).subs({a: av, eps: ev}), 30)) < 1e-25
        for av, ev in [(0, sp.Rational(1, 3)), (sp.Rational(7, 10), sp.Rational(3, 10)), (5, 2)]))
S = per_kz.subs(a, 0) + 2 * (c**2 / eps * S3 + 2 * c / eps**2 * S2 + 2 / eps**3 * S1) / (4 * sp.pi)
disc_rho = S / L
cont_rho = sp.integrate(per_kz.subs(a, q), (q, 0, sp.oo)) * 2 / (2 * sp.pi)
diff_rho = sp.simplify(disc_rho - cont_rho)
rho_mode = sp.simplify(sp.series(diff_rho, eps, 0, 1).removeO())
print('      P2 regulated difference, eps-expansion: %s' % sp.series(diff_rho, eps, 0, 2))
chk("P2 regulated MODE SUM periodic <:T00:> = -pi^2/(90 L^4) (no images)",
    sp.simplify(rho_mode + sp.pi**2 / (90 * L**4)) == 0)

# ---------------------------------------------------------------- P3
Gc, rc, pc, Dpc = G_images(0, n * L)
chk("P3a image-sum rho_periodic = -pi^2/(90 L^4) (agrees with P2)", sp.simplify(rc + sp.pi**2 / (90 * L**4)) == 0)
chk("P3b p/rho = (-1,-1,3)", [sp.simplify(pp / rc) for pp in pc] == [-1, -1, 3])
chk("P3c trace -rho+p1+p2+p3 = 0 (conformal trace at m=0 for this state)", sp.simplify(-rc + sum(pc)) == 0)
chk("P3d Delta' = 6, Delta = 6/7 (tree's Casimir values)",
    Dpc == 6 and sp.simplify(Dpc / (1 + Dpc)) == sp.Rational(6, 7))

# ---------------------------------------------------------------- T1
# 1/(e^{bk}-1) = SUM_{j>=1} e^{-j b k}: each term integrates exactly
j = sp.symbols('j', integer=True, positive=True)
planck = sp.summation(sp.integrate(4 * sp.pi * k**3 * sp.exp(-j * beta * k), (k, 0, sp.oo)), (j, 1, sp.oo)) / (2 * sp.pi)**3
chk("T1 Planck mode integral rho = pi^2/(30 beta^4) (no images)", sp.simplify(planck - sp.pi**2 / (30 * beta**4)) == 0)

# ---------------------------------------------------------------- T2
mp.mp.dps = 40


def img_diff(t, rr, b, N=200000):
    # symmetric sum n = +-1..+-N of 1/(4 pi^2 (r^2 - (t + i n b)^2)); tail ~ 1/n^2 -> Richardson via nsum
    f = lambda nn: (1 / (4 * mp.pi**2 * (rr**2 - (t + 1j * nn * b)**2))
                    + 1 / (4 * mp.pi**2 * (rr**2 - (t - 1j * nn * b)**2)))
    return mp.nsum(f, [1, mp.inf])


def mode_diff(t, rr, b):
    return mp.quad(lambda kv: mp.sin(kv * rr) * mp.cos(kv * t) / (mp.exp(b * kv) - 1), [0, mp.inf]) / (2 * mp.pi**2 * rr)


worst = 0
for (t0, r0, b0) in [(0.3, 1.0, 1.0), (0.0, 0.5, 2.0), (1.7, 2.3, 0.8), (0.9, 0.4, 1.3)]:
    I1 = img_diff(mp.mpf(t0), mp.mpf(r0), mp.mpf(b0))
    M1 = mode_diff(mp.mpf(t0), mp.mpf(r0), mp.mpf(b0))
    worst = max(worst, abs(I1 - M1) / abs(M1), abs(mp.im(I1)))
print("      T2 worst relative gap image-sum vs Planck mode integral: %s" % mp.nstr(worst, 5))
chk("T2 imaginary-time image sum == thermal (Planck/KMS) Wightman difference, 4 points incl. timelike (t>r)",
    worst < 1e-12)

# ---------------------------------------------------------------- T3
Gt, rt, pt, Dpt = G_images(sp.I * n * beta, 0)
chk("T3a image-sum thermal rho = pi^2/(30 beta^4) (agrees with T1)", sp.simplify(rt - sp.pi**2 / (30 * beta**4)) == 0)
chk("T3b p = rho/3", [sp.simplify(pp / rt) for pp in pt] == [sp.Rational(1, 3)] * 3)
chk("T3c G_ii = G_00/3", all(sp.simplify(Gt[i, i] - Gt[0, 0] / 3) == 0 for i in (1, 2, 3)))
chk("T3d Delta' = 2/3, Delta = 2/5 (tree's thermal values)",
    Dpt == sp.Rational(2, 3) and sp.simplify(Dpt / (1 + Dpt)) == sp.Rational(2, 5))
chk("T3e sign-blind: rho_thermal > 0 and rho_periodic < 0 both have Delta' >= 1/2",
    (rt.subs(beta, 1) > 0) and (rc.subs(L, 1) < 0) and Dpt >= sp.Rational(1, 2) and Dpc >= sp.Rational(1, 2))

# ---------------------------------------------------------------- S1
ok = True
nn = sp.symbols('nn', integer=True)
for (st, sz) in [(0, nn * L), (sp.I * nn * beta, 0)]:
    Wn = 1 / (4 * sp.pi**2 * (-(dt + st)**2 + dx**2 + dy**2 + (dz + sz)**2))
    for A in range(4):
        for B in range(4):
            e = sp.simplify((-sp.diff(Wn, D[A], D[B])).subs({dt: 0, dx: 0, dy: 0, dz: 0}))
            ok &= sp.simplify(e - e.subs(nn, -nn)) == 0
chk("S1 every image term is even in n, so 2 SUM_{n>=1} = SUM_{n!=0}", ok)

# ---------------------------------------------------------------- S2
s = sp.symbols('s0:4')
Gs = sp.Matrix(4, 4, lambda i, j: sp.Symbol('g%d%d' % (min(i, j), max(i, j))))
gen = sp.exp(sum(s[i] * Gs[i, j] * s[j] for i in range(4) for j in range(4)) / 2)
ok = True
for A in range(4):
    for B in range(4):
        if A == B:
            mom = sp.diff(gen, s[A], 4)
        else:
            mom = sp.diff(gen, s[A], 2, s[B], 2)
        mom = sp.simplify(mom.subs({si: 0 for si in s}))
        want = Gs[A, A] * Gs[B, B] + 2 * Gs[A, B]**2
        ok &= sp.expand(mom - want) == 0
chk("S2 Isserlis: <X_A^2 X_B^2> = G_AA G_BB + 2 G_AB^2 for every A,B (so <:T00^2:> = rho^2 + SUM G^2/2)", ok)

# ---------------------------------------------------------------- X1 plates (extension)
mp.mp.dps = 25
aa = mp.mpf(1)


def Wz(s_):
    return 1 / (4 * mp.pi**2 * s_**2)


def plate_state(z):
    # Dirichlet at z=0, a:  W_D = SUM_n [W(Dz + 2na) - W(z+z' + 2na)], renormalised: drop n=0 translation.
    # spatial-separation derivatives at Dt=Dx=Dy=0, argument s along z:
    #   -d_t^2 W = -1/(2 pi^2 s^4)... compute from W(sig) with sig = s^2: d_t^2 (1/sig) = +2/sig^2 ; d_x^2 (1/sig) = -2/sig^2
    #   d_z^2 (1/s^2) = 6/s^4
    tt = lambda s_: -(2 / s_**4) / (4 * mp.pi**2)       # -d_t^2 W -> G_tt contribution: -(+2/s^4)/(4pi^2)... sign fixed below
    # G_tt(trans) = -d_Dt^2 W  = -(1/(4pi^2)) * d_t^2 (1/(-t^2+s^2)) at t=0 = -(1/(4pi^2)) * 2/s^4
    # G_xx(trans) = -d_Dx^2 W  = -(1/(4pi^2)) * (-2/s^4) = +2/(4pi^2 s^4)
    # G_zz(trans) = -d_Dz^2 W  = -(1/(4pi^2)) * 6/s^4
    # reflected (W(z+z')): t,x,y as translation; z: d_z d_z' W(z+z') = +W'' -> +6/(4pi^2 s^4)
    def trans(s_):
        return (-2 / s_**4, 2 / s_**4, 2 / s_**4, -6 / s_**4)

    def refl(s_):
        return (-2 / s_**4, 2 / s_**4, 2 / s_**4, 6 / s_**4)

    G = [mp.mpf(0)] * 4
    for i in range(4):
        tsum = 2 * mp.nsum(lambda nn: trans(2 * nn * aa)[i], [1, mp.inf])
        rsum = mp.nsum(lambda nn: refl(2 * z + 2 * nn * aa)[i], [-mp.inf, mp.inf])
        G[i] = (tsum - rsum) / (4 * mp.pi**2)
    phi2 = (2 * mp.nsum(lambda nn: Wz(2 * nn * aa), [1, mp.inf])
            - mp.nsum(lambda nn: Wz(2 * z + 2 * nn * aa), [-mp.inf, mp.inf]))
    return G, phi2


def rho_min(z):
    G, _ = plate_state(z)
    return (G[0] + G[1] + G[2] + G[3]) / 2, G


def phi2(z):
    return plate_state(z)[1]


target = -mp.pi**2 / (1440 * aa**4)
okc = True
for z0 in (mp.mpf('0.5'), mp.mpf('0.3')):
    rm, _ = rho_min(z0)
    d2 = mp.diff(phi2, z0, 2)
    rconf = rm - d2 / 6            # T00 gains -xi d_z^2 <phi^2> for a static state, signature (-+++)
    print("      X1 z=%s  rho_min=%s  rho_conf=%s  (target %s)" % (z0, mp.nstr(rm, 12), mp.nstr(rconf, 12), mp.nstr(target, 12)))
    okc &= abs(rconf - target) < 1e-15
chk("X1a plate machinery: conformal rho = -pi^2/(1440 a^4) at z = a/2 and z = 0.3a", okc)
rm, G = rho_min(mp.mpf('0.5'))
Dp_plate = (sum(g**2 for g in G) / 2) / rm**2
print("      X1 Dirichlet plates, minimal coupling, midpoint: G = %s, rho = %s, Delta' = %s, Delta = %s"
      % ([mp.nstr(g, 8) for g in G], mp.nstr(rm, 10), mp.nstr(Dp_plate, 10), mp.nstr(Dp_plate / (1 + Dp_plate), 10)))
chk("X1b plates midpoint Delta' >= 1/2 (T1 floor holds) and != 6 (periodic value is geometry-specific)",
    Dp_plate >= 0.5 and abs(Dp_plate - 6) > 1e-3)
chk("X1c plates midpoint minimal rho < 0 (sign-blindness conclusion unaffected)", rm < 0)

# ---------------------------------------------------------------- controls (must fail)
Gw, rw, _, _ = G_images(0, n * L, sign=+1)
chk("C1 CONTROL fires: wrong point-split sign gives rho_periodic = +pi^2/(90 L^4), not the mode-sum value",
    sp.simplify(rw - sp.pi**2 / (90 * L**4)) == 0 and sp.simplify(rw - rho_mode) != 0)
Gr, rr_, _, _ = G_images(n * beta, 0)
print("      C2 NOTE: real-time shift n*beta gives rho = %s at coincidence (beta -> i beta leaves 1/beta^4 unchanged)" % rr_)
chk("C2 NOTE (recorded, not a failure): at COINCIDENCE a real-time shift n beta reproduces Stefan-Boltzmann too,"
    " so the tree's SB control alone does not certify the i n beta prescription", sp.simplify(rr_ - sp.pi**2 / (30 * beta**4)) == 0)
def real_img(t, rr, b):
    f = lambda nn: (1 / (4 * mp.pi**2 * (rr**2 - (t + nn * b)**2)) + 1 / (4 * mp.pi**2 * (rr**2 - (t - nn * b)**2)))
    return mp.nsum(f, [1, mp.inf])
t0, r0, b0 = mp.mpf('0.3'), mp.mpf('1.0'), mp.mpf('1.0')
Rr = real_img(t0, r0, b0); Mm = mode_diff(t0, r0, b0)
print("      C3 real-time image sum %s vs Planck mode integral %s" % (mp.nstr(Rr, 10), mp.nstr(Mm, 10)))
chk("C3 CONTROL fires: off coincidence, the real-time shift does NOT reproduce the thermal Wightman difference (T2 does)",
    abs(Rr - Mm) > 1e-3 * abs(Mm))

npass = sum(ok for _, ok in RESULTS)
print("\n%d/%d PASS" % (npass, len(RESULTS)))
sys.exit(0 if npass == len(RESULTS) else 1)
