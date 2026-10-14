#!/usr/bin/env python3
r"""
DOCKET 67 -- re-derivation for key gklp-eq22.

    GKLP eq. (22) extremised, g -> 1, as the pass read it (branelink.py:81-83,
    :275-281, :307): B >= 0.999387630 buys one second over the Proxima span,
    B >= 0.99999993 buys half the light time, with the backward excess held at
    d = 7e-16 (GW170817).

SOURCE STATUS IN THIS STAGE: Greene, Kabat, Levin, Porrati arXiv:2208.09014 was
NOT readable here (alphaXiv quota exceeded on every call; arxiv.org, osti.gov,
semanticscholar, springer refused by the egress proxy).  What eq. (22) says at
cos = 1 is taken from this docket's sibling audit that DID read it
(audits/gklp-rank1-moving-brane-no-ctc.json: 'eq. 22 at cos theta = 1 equals
eq. 20 (their eqs. 23-24)'; eq. 20 v = gamma(1+Gamma^2B^2beta^2)/(1-Gamma^2 B
gamma beta^2), eq. 25 w = -gamma(1+Gamma^2B^2beta^2)/(1+Gamma^2 B gamma beta^2)).
Nothing here imports branelink.py.  Everything is derived from:

  H1  flat bulk M4 x S1, one flat unwrapped brane at z = beta t (0<beta<1), no
      back-reaction (GKLP's setting);
  H2  the signal is a free bulk wave: its front is the boundary of the bulk
      causal future of the emission event, restricted to the brane, at D >> 2 pi R;
  H3  emitter and receiver share ONE brane boost B (W8's common boost);
  H4  the GRB photon is brane-confined, speed 1 in every brane frame.

Checks
  A  brane rest frame: the late-time front speed is gamma, ISOTROPIC in the brane
     directions (identification vector has no brane component) -- sympy.
  B  boosted observer: exact arrival slope tau(c) = t/D in direction c = cos phi;
     tau(+1) = 1/v(eq.20), tau(-1) = -1/w(eq.25) -- sympy.
  C  first order in delta = gamma - 1: excess e(c) = delta Gamma^2 (1 + B c)^2, so
     forward/backward ratio ((1+B)/(1-B))^2 -- the tree's r.  sympy series.
  D  the tree's b_for_saving reproduced (0.999387630, 0.99999993).
  E  EXACT (no g -> 1, no linearisation), backward excess held at d exactly:
     B for a 1 s saving; B for half the light time; the supercritical boost B*
     at which the forward direction becomes instantaneous.
  F  REAL SKY: GW170817's propagation direction (from AT2017gfo) is NOT
     antiparallel to Earth -> Proxima; best boost direction optimised, B needed.
  G  datum sensitivity: d = 7e-16 (26 Mpc, zero intrinsic delay) vs the same
     1.74 s at 40 Mpc.
"""
import sys
import sympy as sp
import mpmath as mp

mp.mp.dps = 60
ok_all = True


def chk(name, cond, extra=""):
    global ok_all
    ok_all &= bool(cond)
    print(("  OK   " if cond else "  FAIL ") + name + (("   " + extra) if extra else ""))


# ------------------------------------------------------------------ A
print("A  brane rest frame: late-time front speed gamma, isotropic")
s, b = sp.symbols('s beta', positive=True)
g = 1 / sp.sqrt(1 - b ** 2)
# winding density s = n/D; identification (t', xvec', z') = (-g b L, 0, g L), L=1;
# arrival slope f(s) = s*(-g b) + sqrt(1 + (s g)^2)  (brane distance 1 in ANY direction)
f = -s * g * b + sp.sqrt(1 + (s * g) ** 2)
crit = sp.solve(sp.diff(f, s), s)
fmin = sp.simplify(f.subs(s, crit[0]))
_fm = [sp.N((fmin - 1 / g).subs(b, bv), 30) for bv in (sp.Rational(1, 10), sp.Rational(3, 5), sp.Rational(99, 100))]
chk("min_s f(s) = 1/gamma  (front speed gamma)",
    sp.simplify(sp.radsimp(fmin * g) - 1) == 0 or all(abs(x) < 1e-25 for x in _fm),
    "f_min = %s = gamma(1 - beta^2) = 1/gamma; residual at beta = 0.1, 0.6, 0.99: %s" % (fmin, [float(x) for x in _fm]))
chk("identification vector has zero brane components -> isotropic", True)

# ------------------------------------------------------------------ B
print("B  boosted observer (boost B along x): exact arrival slope tau(c)")
tau, c, B, gg = sp.symbols('tau c B gamma', real=True)
G2 = 1 / (1 - B ** 2)
# event (t, D c, D sqrt(1-c^2)) in the observer frame; brane frame t' = Gamma(t + B x),
# x' = Gamma(x + B t); front t' = r'/gamma.  Squared form:
quad = sp.expand(gg ** 2 * G2 * (tau + B * c) ** 2 - G2 * (c + B * tau) ** 2 - (1 - c ** 2))
roots = sp.solve(quad, tau)
bp, Bp = sp.symbols('b Bb', positive=True)
gp = 1 / sp.sqrt(1 - bp ** 2)
Gp2 = 1 / (1 - Bp ** 2)
v20 = gp * (1 + Gp2 * Bp ** 2 * bp ** 2) / (1 - Gp2 * Bp * gp * bp ** 2)
w25 = -gp * (1 + Gp2 * Bp ** 2 * bp ** 2) / (1 + Gp2 * Bp * gp * bp ** 2)
tf = (1 - gg * B) / (gg - B)
tb = (1 + gg * B) / (gg + B)
chk("tau(+1) = (1 - gamma B)/(gamma - B) solves the front equation",
    sp.simplify(quad.subs({c: 1, tau: tf})) == 0)
chk("tau(-1) = (1 + gamma B)/(gamma + B) solves the front equation",
    sp.simplify(quad.subs({c: -1, tau: tb})) == 0)
chk("1/tau(+1) == GKLP eq. 20 v (= eq. 22 at cos = 1, per sibling reading)",
    sp.simplify((1 / tf).subs({gg: gp, B: Bp}) - v20) == 0)
chk("-1/tau(-1) == GKLP eq. 25 w",
    sp.simplify((-1 / tb).subs({gg: gp, B: Bp}) - w25) == 0)


def tau_exact(gam, Bv, cv):
    """earliest-arrival slope t/D on the brane, observer boost Bv, direction cos = cv."""
    gam, Bv, cv = mp.mpf(gam), mp.mpf(Bv), mp.mpf(cv)
    G2v = 1 / (1 - Bv ** 2)
    a2 = G2v * (gam ** 2 - Bv ** 2)
    a1 = G2v * 2 * Bv * cv * (gam ** 2 - 1)
    a0 = G2v * (gam ** 2 * Bv ** 2 * cv ** 2 - cv ** 2) - (1 - cv ** 2)
    disc = a1 ** 2 - 4 * a2 * a0
    rts = [(-a1 + sg * mp.sqrt(disc)) / (2 * a2) for sg in (1, -1)]
    good = [r for r in rts if r + Bv * cv > 0]     # t' > 0 branch of the cone
    return min(good)


# ------------------------------------------------------------------ C
print("C  first order in delta = gamma - 1")
dl = sp.symbols('delta', positive=True)
cc = sp.symbols('cc', real=True)
Bs = sp.symbols('Bs', positive=True)
# implicit: tau = 1 - delta*e1 + O(delta^2); excess e = 1/tau - 1 = delta*e1 + ...
e1 = sp.symbols('e1')
qd = quad.subs({gg: 1 + dl, B: Bs, c: cc, tau: 1 - dl * e1})
lin = sp.series(sp.expand(qd), dl, 0, 2).removeO().coeff(dl, 1)
e1sol = sp.solve(lin, e1)[0]
chk("e(c) = delta * Gamma^2 (1 + B c)^2 at first order",
    sp.simplify(e1sol - (1 + Bs * cc) ** 2 / (1 - Bs ** 2)) == 0, "e1 = %s" % sp.factor(e1sol))
ratio = sp.simplify(e1sol.subs(cc, 1) / e1sol.subs(cc, -1))
chk("forward/backward = ((1+B)/(1-B))^2 -- the tree's r", sp.simplify(ratio - ((1 + Bs) / (1 - Bs)) ** 2) == 0)

# ------------------------------------------------------------------ D
print("D  the tree's formula (branelink.b_for_saving), reproduced WITHOUT importing it")
C_LIGHT = mp.mpf(299792458)
YR = mp.mpf('365.25') * 86400
T = mp.mpf('4.2465') * YR                    # light time: span = 4.2465 ly = c * 4.2465 Julian yr
D_GW = mp.mpf('7e-16')


def tree_b(want):
    r = (want / T) / D_GW
    return (mp.sqrt(r) - 1) / (mp.sqrt(r) + 1)


b1_tree, bh_tree = tree_b(1), tree_b(T / 2)
chk("tree B(1 s) = 0.999387630 (9 digits)", mp.nstr(b1_tree, 9) == '0.99938763', mp.nstr(b1_tree, 15))
chk("tree B(T/2) prints 0.99999993 (%.8f)", "%.8f" % float(bh_tree) == "0.99999993", mp.nstr(bh_tree, 15))
print("     the tree's saving model: fraction = d ((1+B)/(1-B))^2 -- i.e. gamma -> 1 AND")
print("     saving fraction taken equal to the forward EXCESS (1 - 1/v ~ v - 1).")

# ------------------------------------------------------------------ E
print("E  EXACT, backward excess held at d, no linearisation")


def gamma_for_backward(Bv, cb, d=D_GW):
    """gamma such that the excess 1/tau - 1 in direction cb equals d exactly."""
    fn = lambda dd: 1 / tau_exact(1 + dd, Bv, cb) - 1 - d
    Bv, cb = mp.mpf(Bv), mp.mpf(cb)
    d0 = d * (1 - Bv ** 2) / (1 + Bv * cb) ** 2          # first-order guess (check C)
    try:
        r = mp.findroot(fn, (d0, d0 * (1 + mp.mpf('1e-3'))), solver='secant', tol=mp.mpf(10) ** (-2 * mp.mp.dps // 3))
        if r > 0 and abs(fn(r)) < d * mp.mpf('1e-20'):
            return 1 + r
    except Exception:
        pass
    # bracket in delta: excess is increasing in delta
    lo, hi = mp.mpf(0), mp.mpf('1e-30')
    while fn(hi) < 0:
        hi *= 10
    for _ in range(400):
        mid = (lo + hi) / 2
        if fn(mid) < 0:
            lo = mid
        else:
            hi = mid
    return 1 + (lo + hi) / 2


def saving_fraction(Bv, cf=1, cb=-1, d=D_GW):
    gam = gamma_for_backward(Bv, cb, d)
    if gam * Bv >= 1 and cf == 1:
        return None, gam                   # supercritical: forward instantaneous or past-directed
    return 1 - tau_exact(gam, Bv, cf), gam


def b_for(want_frac, cf=1, cb=-1, d=D_GW, lo=mp.mpf('0.5'), hi=None):
    hi = hi if hi is not None else 1 - mp.mpf('1e-12')
    for _ in range(200):
        mid = (lo + hi) / 2
        sf, _ = saving_fraction(mid, cf, cb, d)
        if sf is None or sf >= want_frac:
            hi = mid
        else:
            lo = mid
    return (lo + hi) / 2


# supercritical boost B* with backward held at d: gamma(B) * B = 1
lo, hi = mp.mpf('0.9999'), 1 - mp.mpf('1e-15')
for _ in range(300):
    mid = (lo + hi) / 2
    if gamma_for_backward(mid, -1) * mid >= 1:
        hi = mid
    else:
        lo = mid
Bstar = (lo + hi) / 2
eps_star = 1 - Bstar
chk("B* (forward instantaneous) = 1 - eps*, eps* ~ sqrt(2d)", abs(eps_star / mp.sqrt(2 * D_GW) - 1) < mp.mpf('1e-6'),
    "B* = %s, 1-B* = %s, sqrt(2d) = %s" % (mp.nstr(Bstar, 15), mp.nstr(eps_star, 8), mp.nstr(mp.sqrt(2 * D_GW), 8)))

b1_exact = b_for(1 / T)
bh_exact = b_for(mp.mpf('0.5'))
print("     B(1 s)  exact = %s   tree = %s   (1-B) ratio exact/tree = %s"
      % (mp.nstr(b1_exact, 15), mp.nstr(b1_tree, 15), mp.nstr((1 - b1_exact) / (1 - b1_tree), 12)))
chk("1 s: exact agrees with the tree to its 9 printed digits",
    mp.nstr(b1_exact, 9) == mp.nstr(b1_tree, 9))
print("     B(T/2)  exact = %s   tree = %s" % (mp.nstr(bh_exact, 15), mp.nstr(bh_tree, 15)))
sf_at_tree, gam_at_tree = saving_fraction(bh_tree)
print("     at the tree's B(T/2) = %s the exact saving fraction is %s (not 0.5); gamma-1 = %s"
      % (mp.nstr(bh_tree, 12), mp.nstr(sf_at_tree, 8), mp.nstr(gam_at_tree - 1, 6)))
chk("T/2: the tree's threshold does NOT buy half the light time (exact saving < 0.5)", sf_at_tree < mp.mpf('0.5'))
chk("T/2: exact threshold differs from the tree's in the 8th decimal",
    "%.8f" % float(bh_exact) != "%.8f" % float(bh_tree), "%.8f vs %.8f" % (float(bh_exact), float(bh_tree)))
chk("T/2: exact threshold lies below B* (still subcritical)", bh_exact < Bstar)
# the two approximations separately at T/2
gm_lin = mp.sqrt(mp.mpf('0.5') / D_GW)
b_excess1 = (mp.sqrt(1 / D_GW) - 1) / (mp.sqrt(1 / D_GW) + 1)   # g -> 1 but saving = 1 - 1/v, v-1 = 1
print("     decomposition at T/2: linear fraction=excess (tree) %s | g->1 with exact fraction %s | exact %s"
      % ("%.10f" % float(bh_tree), "%.10f" % float(b_excess1), "%.10f" % float(bh_exact)))

# ------------------------------------------------------------------ F
print("F  REAL SKY GEOMETRY (not extremised)")


def unit(ra_h, ra_m, ra_s, de_d, de_m, de_s):
    ra = mp.radians(15 * (ra_h + ra_m / mp.mpf(60) + ra_s / mp.mpf(3600)))
    sgn = -1 if de_d < 0 else 1
    de = mp.radians(sgn * (abs(de_d) + de_m / mp.mpf(60) + de_s / mp.mpf(3600)))
    return [mp.cos(de) * mp.cos(ra), mp.cos(de) * mp.sin(ra), mp.sin(de)]


n_prox = unit(14, 29, mp.mpf('42.946'), -62, 40, mp.mpf('46.16'))   # J2000, Gaia DR3 (via Wikipedia snippet)
n_kn = unit(13, 9, mp.mpf('48.085'), -23, 22, mp.mpf('53.343'))     # AT2017gfo, Coulter et al. 2017
dot = sum(a * b for a, b in zip(n_prox, n_kn))
psi = mp.degrees(mp.acos(dot))
chi = 180 - psi      # angle between propagation directions: Earth->Proxima and NGC4993->Earth
print("     angle(Proxima, AT2017gfo) on the sky = %s deg; between PROPAGATION directions = %s deg"
      % (mp.nstr(psi, 8), mp.nstr(chi, 8)))
chk("the two propagation directions are NOT antiparallel (extremisation is a bound, not the sky)",
    abs(chi - 180) > 1)
chir = mp.radians(chi)


def best_saving(Bv, want=None, n=121):
    """max over the boost direction in the plane of the two propagation directions
    of the forward saving fraction toward Proxima, with GW170817's direction held at d."""
    best = (mp.mpf(-1), None)
    # fast axis at angle a from Earth->Proxima; GW direction at angle chi from it
    grid = [mp.mpf(i) / (n - 1) for i in range(n)]
    def val(a):
        cf, cb = mp.cos(a), mp.cos(chir - a)
        gam = gamma_for_backward(Bv, cb)
        tf_ = tau_exact(gam, Bv, cf)
        return 1 - tf_
    # coarse over the whole plane a in [-pi, pi], golden refine
    span = 2 * mp.pi
    cands = [(val(-mp.pi + span * x), -mp.pi + span * x) for x in grid]
    v0, a0 = max(cands, key=lambda t: t[0])
    lo_, hi_ = a0 - span / (n - 1), a0 + span / (n - 1)
    for _ in range(80):
        m1, m2 = lo_ + (hi_ - lo_) / 3, hi_ - (hi_ - lo_) / 3
        if val(m1) < val(m2):
            lo_ = m1
        else:
            hi_ = m2
    a = (lo_ + hi_) / 2
    return val(a), a


def b_for_real(want_frac, lo=mp.mpf('0.99'), hi=1 - mp.mpf('1e-9')):
    for _ in range(40):
        mid = (lo + hi) / 2
        sv, _ = best_saving(mid)
        if sv >= want_frac:
            hi = mid
        else:
            lo = mid
    return (lo + hi) / 2


mp.mp.dps = 40
b1_real = b_for_real(1 / T)
sv, a_opt = best_saving(b1_real)
print("     real sky: B(1 s) = %s  (tree, extremised: %s); optimal fast axis %s deg from Proxima"
      % (mp.nstr(b1_real, 10), mp.nstr(b1_tree, 10), mp.nstr(mp.degrees(a_opt), 6)))
print("     (1-B) real/extremised = %s; anti-alignment prediction (1 + cos psi)/2 = %s"
      % (mp.nstr((1 - b1_real) / (1 - b1_tree), 8), mp.nstr((1 + mp.cos(mp.radians(psi))) / 2, 8)))
print("     angle of the optimal fast axis from the GW170817 propagation direction: %s deg"
      % mp.nstr(mp.degrees(abs(chir - a_opt)), 8))
bh_real = b_for_real(mp.mpf('0.5'), lo=mp.mpf('0.9999999'), hi=1 - mp.mpf('1e-10'))
print("     real sky: B(T/2) = %s (tree %s, exact-extremised %s)" % (mp.nstr(bh_real, 12), mp.nstr(bh_tree, 12), mp.nstr(bh_exact, 12)))
chk("real sky needs a LARGER B than the extremised figure (extremised = necessary floor)",
    b1_real > b1_tree)
# first-order closed form for comparison: max_a ((1 + B cos a)/(1 + B cos(chi - a)))^2 at B -> 1
lin_ratio = lambda Bv: max(((1 + Bv * mp.cos(a)) / (1 + Bv * mp.cos(chir - a))) ** 2
                           for a in [-mp.pi + 2 * mp.pi * mp.mpf(i) / 4000 for i in range(4001)])
print("     first-order check: ratio needed %s, ratio at real B %s"
      % (mp.nstr((1 / T) / D_GW, 8), mp.nstr(lin_ratio(b1_real), 8)))
# out-of-plane check: a coarse 2D sweep at b1_real never beats the in-plane optimum
# (a fast axis rotated out of the plane by angle th has cos to each direction scaled by cos th)
worse = True
for th in (mp.radians(5), mp.radians(20), mp.radians(45)):
    cf, cb = mp.cos(a_opt) * mp.cos(th), mp.cos(chir - a_opt) * mp.cos(th)
    gam = gamma_for_backward(b1_real, cb)
    worse &= (1 - tau_exact(gam, b1_real, cf)) <= sv
chk("out-of-plane tilts (5, 20, 45 deg) of the optimal axis do not do better", worse)

# ------------------------------------------------------------------ G
print("G  datum: d")
MPC = mp.mpf('3.0856775814913673e22')
d26 = mp.mpf('1.74') / (26 * MPC / C_LIGHT)
d40 = mp.mpf('1.74') / (40 * MPC / C_LIGHT)
print("     1.74 s over 26 Mpc = %s (published rounds to 7e-16); over 40 Mpc = %s"
      % (mp.nstr(d26, 6), mp.nstr(d40, 6)))
chk("7e-16 is 1.74 s / (26 Mpc / c) rounded up", abs(d26 - mp.mpf('6.5e-16')) < mp.mpf('0.2e-16'))
D_saved = D_GW
b1_40 = (mp.sqrt((1 / T) / d40) - 1) / (mp.sqrt((1 / T) / d40) + 1)
print("     tree formula at d(40 Mpc) = %s: B(1 s) = %s (vs %s)" % (mp.nstr(d40, 4), mp.nstr(b1_40, 9), mp.nstr(b1_tree, 9)))
chk("B(1 s) moves only in the 4th decimal with d (conclusion 'B ~ 0.9994-0.9995, unmeasured' unchanged)",
    abs(b1_40 - b1_tree) < mp.mpf('2e-4'))

print("\nALL CHECKS OK" if ok_all else "\nSOME CHECK FAILED")
sys.exit(0 if ok_all else 1)
