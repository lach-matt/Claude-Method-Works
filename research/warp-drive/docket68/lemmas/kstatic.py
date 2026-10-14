#!/usr/bin/env python3
"""kstatic.py -- item 179 (k-compute): a corridor exclusive to the bulk, modelled as a 5D bulk black hole between two
static planes.  Does staticity of both planes fix the corridor's size against ell = 1/k (an EQUALITY), or does a free
modulus remain?

M (179, verbatim, typing kept): "Let's approach this from a different angle. We know the corridor doesn't not sit on
either position's plane, it only bridges them. So one could surmise that the corridor is exclusive to the bulk."

Model:
  bulk  Schwarzschild-AdS5 on each side, f(R) = k_s + k^2 R^2 - mu/R^2, k = 1/ell, k_s in {1, 0, -1}
        ds^2 = -f dt^2 + dR^2/f + R^2 dSigma_{k_s}^2
  plane a static surface R = a with pure tension.  Israel, per sheet, lam = kappa^2 sigma / 3:
        J1 (angular)  sum_i eta_i sqrt(f_i + adot^2)                 = lam a
        J2 (tau-tau)  sum_i eta_i (addot + f_i'/2)/sqrt(f_i + adot^2) = lam
        eta_i = +1 if R decreases going from the plane into side i ("inner", toward the horizon), -1 if it increases.
        With s_i = sqrt(f_i(a))/a, w = k_s/a^2, v_i = mu_i/a^4 (s_i^2 = k_i^2 + w - v_i), the static conditions are
        J1: sum eta_i s_i = lam,   J2: sum eta_i (2k_i^2 + w - s_i^2)/s_i = lam.
  board's configuration (multiplane.py M4, Lykken-Randall as read in PRZ; stage 7 K4's control):
        our plane: Z2, k_L on both sides, both inner, RS tension lam_1 = 2 k_L (clause (B), item 139)
        slab between the planes: k_L, mass mu_s (the corridor)
        position 2's plane: slab side outer (k_L, mu_s), beyond side inner (k_R = 3 k_L/4, mu_2),
        lam_2 = k_R - k_L = -k_L/4 per sheet (-1/8 of ours per sheet; -1/4 of ours in PRZ's doubled count: stage 7 K5,
        item 174 (2)'s per-sheet count reproducing M4's geometry)

  S   THE LEMMA.  A plane between two SAdS5 bulks (any k_a, k_b, mu_a, mu_b, any orientations) at its flat-tuned tension
      lam = eta_a k_a + eta_b k_b is static only if k_s/a^2 = -2 delta^2, with s_a = k_a + eta_a delta,
      s_b = k_b - eta_b delta (degenerate only for a zero-tension interface between identical bulks).  So on planar or
      spherical slices: mu_a = mu_b = 0 and the plane is static at every a (a modulus); on hyperbolic slices
      a^2 = 1/(2 delta^2), mu_a = -(2 eta_a k_a delta + 3 delta^2)/(4 delta^4), mu_b = (2 eta_b k_b delta - 3 delta^2)/(4 delta^4).
      A Z2 plane has delta = 0: mu = 0 and k_s = 0.  Our plane (RS) and position 2's (M4 per sheet) are both tuned.
  A   the board's configuration: mu_s = 0 forced, the corridor absent; the separation free (the radion)
  H   our plane non-Z2 (item 138, each universe its own bulk): the two-plane solution set at k_s = -1 is two curves
      (one-parameter, a modulus); every member has a naked singularity in an outer bulk, or coincident planes
  B   the bridge (planes in the bulk black hole's two exteriors, the horizon between them): excluded
  X   the one equality SAdS5 offers, extremality r_h = ell/sqrt2 (k_s = -1): from extremality, not staticity; no
      static plane at these tensions borders it from outside its horizon
  T   near-instantaneous planes (H = 0 at one instant): mu_s = a1^2, free of ell
  C   controls that can fail: mu = 0 (FREE), tension off RS (FIXED or NONE), the literal per-sheet quarter (NONE)
Units: k_L = 1 wherever a number is printed; every length is in units of ell = 1/k_L.
Stdlib + sympy + mpmath.  python3 kstatic.py [--selftest]
"""
import sys

import mpmath as mp
import sympy as sp

mp.mp.dps = 40

kL = sp.Symbol("k_L", positive=True)
R, a = sp.symbols("R a", positive=True)
eps = sp.Symbol("epsilon", real=True)
x, x2, d, w, s = sp.symbols("x x2 delta w s", real=True)
mu, mus = sp.symbols("mu mu_s", real=True)
kR = sp.Rational(3, 4) * kL
LAM1_RS = 2 * kL
LAM2_M4 = kR - kL

ASSUMPTIONS = [
    "A1 vacuum bulk, negative cosmological constant on every side, SAdS5 (5D Birkhoff with constant-curvature 3-slices): "
    "f = k_s + k^2 R^2 - mu/R^2  [standard-not-READ]",
    "A2 thin planes, pure tension (clause (B): free of matter); static = fixed R (item 141, H-STATIC-PLANES)",
    "A3 Israel per sheet, kappa^2 sigma/3 = lam; our plane at the RS value lam_1 = 2 k_L (Z2, k_L both sides)  "
    "[Israel 1966: standard-not-READ]",
    "A4 curvatures as the board's M4: k_L on both sides of our plane and in the slab, k_R = 3 k_L/4 beyond position 2",
    "A5 position 2 per sheet lam_2 = k_R - k_L (M4's geometry; PRZ's -1/4 is the doubled count, stage 7 K5); the "
    "literal per-sheet -1/4 of ours is run as sensitivity row C3",
    "A6 one k_s on every side (both sides of a plane share its induced metric -f dt^2 + a^2 dSigma_ks^2)",
    "A7 an outer bulk with no further plane runs to its horizon or to R -> 0; a naked singularity there "
    "(k_s = -1: mu < -ell^2/4, or the plane inside the outermost horizon; k_s = 1: mu < 0) is inadmissible",
    "A8 the corridor is the bulk black hole between the planes; identifying its horizon with eq. (17)'s m is a READING "
    "(H-BULK-HORIZON-IS-THROAT), not a derivation",
]


def f(Rv, k, m, ks):
    return ks + k**2 * Rv**2 - m / Rv**2


def side_t(k, wv, sv):
    """f'/(2 sqrt f) at the plane, divided out: (k^2 + v)/s = (2k^2 + w - s^2)/s."""
    return (2 * k**2 + wv - sv**2) / sv


# --------------------------------------------------------------------------------------------- D: the junction
def d_derivation():
    """STRUCTURAL: J2 = (d/dtau J1)/adot for pure tension, any two sides; the Z2 Friedmann form with dark radiation."""
    tau = sp.Symbol("tau")
    A = sp.Function("A")(tau)
    e1, e2, k1, k2, m1, m2, lam, ksym = sp.symbols("eta1 eta2 k1 k2 m1 m2 lam k_s")
    Ad, Add = A.diff(tau), A.diff(tau, 2)
    fa = lambda k, m: f(A, k, m, ksym)
    fp = lambda k, m: sp.diff(f(R, k, m, ksym), R).subs(R, A)
    J1 = e1 * sp.sqrt(fa(k1, m1) + Ad**2) + e2 * sp.sqrt(fa(k2, m2) + Ad**2) - lam * A
    J2 = (e1 * (Add + fp(k1, m1) / 2) / sp.sqrt(fa(k1, m1) + Ad**2)
          + e2 * (Add + fp(k2, m2) / 2) / sp.sqrt(fa(k2, m2) + Ad**2) - lam)
    H = sp.Symbol("H")
    H2 = sp.solve(sp.Eq(f(a, kL, mu, ksym) + a**2 * H**2, (lam * a / 2) ** 2), H**2)[0]
    standard = lam**2 / 4 - kL**2 - ksym / a**2 + mu / a**4
    # static J1/J2 in s-variables agree with Phi = 0, Phi' = 0 for Phi = sum eta sqrt f - lam a
    sv = sp.sqrt(f(a, kL, mu, ksym)) / a
    tv = sp.diff(f(a, kL, mu, ksym), a) / (2 * sp.sqrt(f(a, kL, mu, ksym)))
    wv, vv = ksym / a**2, mu / a**4
    t_form = sp.simplify(tv - side_t(kL, wv, sv))
    return {"J2_is_dJ1": sp.simplify(J1.diff(tau) - Ad * J2) == 0, "H2": sp.expand(H2),
            "H2_matches_standard": sp.simplify(H2 - standard) == 0, "t_form_ok": t_form == 0}


# ------------------------------------------------------------------------------------------------- S: the lemma
def s_lemma():
    """Any orientations, flat-tuned tension: J1 is solved identically by s_a = k_a + eta_a delta,
    s_b = k_b - eta_b delta (J1 is linear in s, so this is its whole solution set); J2 then fixes w."""
    ka, kb = sp.symbols("k_a k_b", positive=True)
    rows = []
    for ea in (1, -1):
        for eb in (1, -1):
            lam = ea * ka + eb * kb
            sa_, sb_ = ka + ea * d, kb - eb * d
            J1 = sp.simplify(ea * sa_ + eb * sb_ - lam)
            num = sp.factor(sp.numer(sp.together(ea * side_t(ka, w, sa_) + eb * side_t(kb, w, sb_) - lam)))
            wsol = sp.solve(num, w)
            va = sp.factor(ka**2 + wsol[0] - sa_**2)
            vb = sp.factor(kb**2 + wsol[0] - sb_**2)
            # masses at k_s = -1, a^2 = -1/w
            a2_ = -1 / wsol[0]
            rows.append({"eta": (ea, eb), "J1": J1, "num": num, "w": wsol, "mu_a": sp.factor(va * a2_**2),
                         "mu_b": sp.factor(vb * a2_**2), "jump": sp.factor(va * a2_**2 - vb * a2_**2),
                         "lam": lam})
    return rows


# ------------------------------------------------------------------------------------- A: the board's configuration
def a_board():
    out = {}
    # our plane Z2 at lam = 2 k_L (1 + eps): J1 2s = lam, J2 2t = lam
    sol = sp.solve([2 * s - 2 * kL * (1 + eps), 2 * side_t(kL, w, s) - 2 * kL * (1 + eps)], [w, s], dict=True)[0]
    out["z2_w"] = sp.factor(sol[w])
    out["z2_v"] = sp.factor(kL**2 + sol[w] - sol[s] ** 2)
    out["rs_w"], out["rs_v"] = out["z2_w"].subs(eps, 0), out["z2_v"].subs(eps, 0)
    # direct check in (a, mu_s): Phi = 2 sqrt f - 2 k_L a = 0 and Phi' = 0
    out["direct"] = {}
    for ks in (1, 0, -1):
        e1 = sp.expand(f(a, kL, mus, ks) - kL**2 * a**2)
        e2 = sp.expand(sp.diff(f(a, kL, mus, ks), a) - 2 * kL**2 * a)
        out["direct"][ks] = sp.solve([e1, e2], [mus, a], dict=True)
    out["Phi1_zero"] = sp.simplify(2 * sp.sqrt(f(a, kL, 0, 0)) - LAM1_RS * a) == 0
    # position 2 after mu_s = 0, k_s = 0
    s2 = sp.Symbol("s_2", positive=True)
    sol2 = sp.solve([-kL + s2 - LAM2_M4, -side_t(kL, 0, kL) + side_t(kR, 0, s2) - LAM2_M4], [s2], dict=True)
    out["p2"] = [{"s2": q[s2], "v2": sp.simplify(kR**2 - q[s2] ** 2)} for q in sol2]
    out["Phi2_zero"] = sp.simplify(-sp.sqrt(f(a, kL, 0, 0)) + sp.sqrt(f(a, kR, 0, 0)) - LAM2_M4 * a) == 0
    # the radion: proper separation between the planes, ell ln(a1/a2), unconstrained
    return out


# ------------------------------------------------------------------- H: our plane non-Z2, two planes, k_s = -1
def mus_plane1(xv):
    return -(3 * xv + 2) / (4 * kL**2 * xv**3)          # S with eta = (+1, +1), delta = x k_L, side a = slab


def mu1_plane1(xv):
    return (2 - 3 * xv) / (4 * kL**2 * xv**3)           # side b = our universe's bulk beyond


def mus_plane2(x2v):
    return (2 - 3 * x2v) / (4 * kL**2 * x2v**3)         # S with eta = (-1, +1), delta = x2 k_L, side a = slab


def mu2_plane2(x2v):
    return (sp.Rational(3, 2) * x2v - 3 * x2v**2) / (4 * kL**2 * x2v**4)   # side b = beyond, k_R = 3k_L/4


def horizons(ks, k, m):
    k, m = mp.mpf(k), mp.mpf(m)
    disc = ks**2 + 4 * k**2 * m
    if disc < 0:
        return []
    return sorted(mp.sqrt(X) for X in ((-ks + sg * mp.sqrt(disc)) / (2 * k**2) for sg in (1, -1)) if X > 0)


def nonnaked(k, m, aplane, ks=-1):
    """A7 for an inner side running to R -> 0: a horizon exists below the plane and the plane is outside it."""
    hor = horizons(ks, k, m)
    if not hor:
        return False
    return aplane > max(hor)


def h_two_planes():
    out = {}
    # plane checks against S
    out["S_check"] = (sp.simplify(mus_plane1(x) - (-(2 * kL * (x * kL) + 3 * (x * kL) ** 2) / (4 * (x * kL) ** 4))) == 0
                      and sp.simplify(mu1_plane1(x) - ((2 * kL * (x * kL) - 3 * (x * kL) ** 2) / (4 * (x * kL) ** 4))) == 0
                      and sp.simplify(mus_plane2(x2) - ((2 * kL * (x2 * kL) - 3 * (x2 * kL) ** 2) / (4 * (x2 * kL) ** 4))) == 0
                      and sp.simplify(mu2_plane2(x2) - ((2 * kR * (x2 * kL) - 3 * (x2 * kL) ** 2) / (4 * (x2 * kL) ** 4))) == 0)
    P = sp.factor(sp.numer(sp.together(mus_plane1(x) - mus_plane2(x2))))
    out["P"] = P
    Q = sp.factor(sp.cancel(P / (x + x2)))
    out["Q"] = Q
    out["Q_roots"] = sp.solve(Q, x2)
    out["Q_disc"] = sp.factor(sp.discriminant(sp.expand(Q), x2))
    # domain: |x| < 1 (s_s, s_1 > 0); x2 < 3/4 (s_2 > 0), x2 < 1 (s_s at plane 2 > 0); x, x2 != 0
    # a2 < a1 (slab of positive thickness, config A) <=> |x2| > |x|
    rows = []
    for xv in [sp.Rational(i, 40) for i in range(-39, 40) if i != 0]:
        cands = [(-xv, "coincident x2 = -x")]
        for r in out["Q_roots"]:
            rv = sp.N(r.subs(x, xv), 30)
            if rv.is_real:
                cands.append((sp.nsimplify(rv) if False else rv, "Q branch"))
        for x2v, label in cands:
            x2f = mp.mpf(str(sp.N(x2v, 30)))
            xf = mp.mpf(str(sp.N(xv, 30)))
            if not (x2f < mp.mpf(3) / 4 and x2f != 0):
                rows.append({"x": xv, "x2": x2f, "branch": label, "ok_s": False})
                continue
            a1 = 1 / (mp.sqrt(2) * abs(xf))
            a2 = 1 / (mp.sqrt(2) * abs(x2f))
            musv = mp.mpf(str(sp.N(mus_plane1(xv).subs(kL, 1), 30)))
            mu1v = mp.mpf(str(sp.N(mu1_plane1(xv).subs(kL, 1), 30)))
            mu2v = mp.mpf(str(sp.N(mu2_plane2(sp.Float(str(x2f), 30)).subs(kL, 1), 30)))
            fs_min = min(-1 + t**2 - musv / t**2 for t in mp.linspace(min(a1, a2), max(a1, a2), 400))
            rows.append({"x": xv, "x2": x2f, "branch": label, "ok_s": True, "a1": a1, "a2": a2, "mus": musv,
                         "mu1": mu1v, "mu2": mu2v, "a2_lt_a1": a2 < a1 - mp.mpf("1e-25"),
                         "slab_static": fs_min > 0,
                         "mu1_ok": nonnaked(1, mu1v, a1), "mu2_ok": nonnaked(mp.mpf(3) / 4, mu2v, a2),
                         "mus_pos": musv > 0})
    out["rows"] = rows
    out["admissible"] = [r for r in rows if r.get("ok_s") and r["a2_lt_a1"] and r["slab_static"] and r["mu1_ok"]
                         and r["mu2_ok"]]
    out["admissible_relaxA7"] = [r for r in rows if r.get("ok_s") and r["a2_lt_a1"]]
    # exact admissibility of the outer bulks on the coincident branch and on the Q branch
    out["mu1_ok_set"] = sp.solve_univariate_inequality(sp.simplify(mu1_plane1(x) * kL**2) + sp.Rational(1, 4) >= 0, x,
                                                       relational=False).intersect(sp.Interval.open(-1, 1))
    out["mus_ok_set"] = sp.solve_univariate_inequality(sp.simplify(mus_plane1(x) * kL**2) + sp.Rational(1, 4) >= 0, x,
                                                       relational=False).intersect(sp.Interval.open(-1, 1))
    out["mu2_coinc_ok_set"] = sp.solve_univariate_inequality(
        sp.simplify(mu2_plane2(-x) * kL**2) + sp.Rational(4, 9) >= 0, x, relational=False).intersect(
        sp.Interval.open(-1, 1))
    return out


# ------------------------------------------------------------------------- B: the bridge (two exteriors)
def b_bridge(h):
    """The horizon between the planes: our plane in one exterior with the slab (which holds the horizon) inner,
    our universe's bulk beyond inner.  Needs both mu_s and mu_1 non-naked (A7 on the beyond side; a horizon in the
    slab).  Position 2 in the other exterior has its slab side inner."""
    out = {"z2": (a_board()["rs_v"], a_board()["rs_w"])}           # Z2: mu_s = 0, w = 0 -> no horizon
    out["both"] = h["mus_ok_set"].intersect(h["mu1_ok_set"])
    out["p2_flat"] = {"beyond inner": kL + kR, "beyond outer": kL - kR}
    return out


# ----------------------------------------------------------------------------------------------- X: extremality
def x_extremal():
    out = {}
    for ks in (1, 0, -1):
        F = f(R, kL, mu, ks)
        out[ks] = [q for q in sp.solve([F, sp.diff(F, R)], [mu, R], dict=True) if q[R].is_positive]
    # each of the four sides at the extremal mass -ell_side^2/4; roots of x and the s's there
    sides = {"slab at our plane (x)": (mus_plane1(x), kL, lambda r: (1 + r, 1 - r)),
             "ours-beyond (x)": (mu1_plane1(x), kL, lambda r: (1 + r, 1 - r)),
             "slab at position 2 (x2)": (mus_plane2(x), kL, lambda r: (1 - r, sp.Rational(3, 4) - r)),
             "position 2 beyond (x2)": (mu2_plane2(x), kR, lambda r: (1 - r, sp.Rational(3, 4) - r))}
    rows = {}
    for name, (m, k, sfun) in sides.items():
        roots = sp.solve(sp.numer(sp.together(m + 1 / (4 * k**2))), x)
        info = []
        for r in roots:
            if r == 0:
                continue
            sv = sfun(r)
            aplane = 1 / (sp.sqrt(2) * abs(r) * kL)
            rh = 1 / (sp.sqrt(2) * k)
            info.append({"x": r, "s_over_kL": sv, "s_pos": all(v > 0 for v in sv),
                         "a_over_rh": sp.nsimplify(sp.simplify(aplane / rh)),
                         "outside": bool(sp.simplify(aplane / rh) > 1)})
        rows[name] = info
    out["sides"] = rows
    out["any_admissible"] = any(i["s_pos"] and i["outside"] for v in rows.values() for i in v)
    return out


# -------------------------------------------------------------------------------- T: near-instantaneous planes
def t_instant():
    out = {}
    for ks in (1, -1):
        out[ks] = sp.solve(f(a, kL, mus, ks) - kL**2 * a**2, mus)[0]
    y = sp.Symbol("y", positive=True)
    rh2 = (sp.sqrt(1 + 4 * y) - 1) / 2
    out["outside"] = all(float((y - rh2).subs(y, v)) > 0 for v in (1e-6, 1e-2, 1, 1e2, 1e6))
    out["addot"] = sp.diff(-1 + mus / a**2, a) / 2
    # k_s = -1: a^2 = -mu, horizon r_+^2 = (1 + sqrt(1 - 4|mu|))/2 >= 1/2 > a^2 = |mu| <= 1/4 (k_L = 1)
    return out


# ------------------------------------------------------------------------------------------------- C: controls
def controls():
    out = {}
    Phi_rs = 2 * sp.sqrt(f(a, kL, 0, 0)) - LAM1_RS * a
    Phi_off = 2 * sp.sqrt(f(a, kL, 0, 0)) - LAM1_RS * (1 + sp.Rational(1, 10)) * a
    out["C1_free"] = sp.simplify(Phi_rs) == 0
    out["C1_off_none"] = sp.solve(sp.simplify(Phi_off), a) == []
    A = a_board()
    out["C2_w"], out["C2_v"] = A["z2_w"], A["z2_v"]
    # eps > 0: w > 0 -> k_s = +1 at our plane; position 2 (tuned) needs w <= 0 (S) -> NONE
    # eps < 0: w < 0 -> k_s = -1: a1^2 = -1/w, mu_s = v a1^4; position 2: mus_plane2(x2) = mu_s -> x2 discrete
    rows = []
    for e in (sp.Rational(-1, 10), sp.Rational(-1, 100), sp.Rational(1, 10)):
        wv = A["z2_w"].subs({eps: e, kL: 1})
        vv = A["z2_v"].subs({eps: e, kL: 1})
        if wv > 0:
            rows.append({"eps": e, "ks": 1, "a1": sp.sqrt(1 / wv), "mus": vv / wv**2, "p2": "NONE (S: w2 <= 0)"})
            continue
        a1sq = -1 / wv
        musv = sp.nsimplify(vv * a1sq**2)
        roots = [r for r in sp.Poly(sp.numer(sp.together(mus_plane2(x2).subs(kL, 1) - musv)), x2).nroots(n=30)
                 if abs(sp.im(r)) < 1e-25 and abs(r) > 1e-20]
        p2 = []
        for r in roots:
            r = sp.re(r)
            a2 = 1 / (sp.sqrt(2) * abs(r))
            mu2v = mu2_plane2(r).subs(kL, 1)
            p2.append({"x2": sp.N(r, 12), "a2": sp.N(a2, 12), "mu2": sp.N(mu2v, 12),
                       "s_pos": bool(r < sp.Rational(3, 4)), "a2_lt_a1": bool(a2 < sp.sqrt(a1sq)),
                       "mu2_ok": nonnaked(mp.mpf(3) / 4, mp.mpf(str(sp.N(mu2v, 30))), mp.mpf(str(sp.N(a2, 30))))})
        rows.append({"eps": e, "ks": -1, "a1": sp.N(sp.sqrt(a1sq), 12), "mus": sp.N(musv, 12), "p2": p2})
    out["C2"] = rows
    # C3: literal per-sheet -1/4 of ours at position 2 (lam_2 = -k_L/2) with k_R = 3 k_L/4, after mu_s = 0, k_s = 0
    s2 = sp.Symbol("s_2", positive=True)
    lam2 = -LAM1_RS / 4
    sol = sp.solve(-kL + s2 - lam2, s2)
    out["C3"] = [sp.simplify((-side_t(kL, 0, kL) + side_t(kR, 0, s2) - lam2).subs(s2, v)) for v in sol]
    return out


# ------------------------------------------------------------------------------------------ the README, eq. (17)
def readme_m():
    h = sp.Rational(662607015, 10**42)
    c = sp.Integer(299792458)
    G = sp.Rational(66743, 10**15)
    N = sp.Integer(2742570311524972)
    r0 = sp.sqrt(N * h * G * sp.log(2) / (2 * sp.pi**2 * c**3))
    return {"m": sp.N(r0 / 2, 20), "r0": sp.N(r0, 20)}


def fmt(v, n=6):
    try:
        return mp.nstr(mp.mpf(str(sp.N(v, 30))), n)
    except Exception:
        return str(v)


def report():
    print("kstatic.py -- item 179: the corridor exclusive to the bulk, two static planes, Schwarzschild-AdS5\n")
    for q in ASSUMPTIONS:
        print("  " + q)
    D = d_derivation()
    print("\nD  J2 = (d/dtau J1)/adot: %s; static t-form ok: %s  [STRUCTURAL]" % (D["J2_is_dJ1"], D["t_form_ok"]))
    print("   Z2 Friedmann form H^2 = %s; = lam^2/4 - k^2 - k_s/a^2 + mu/a^4: %s" % (D["H2"], D["H2_matches_standard"]))
    print("\nS  the lemma (flat-tuned tension lam = eta_a k_a + eta_b k_b):")
    for r in s_lemma():
        print("   eta = %-8s J1 res %s | J2 numerator %s | w = %s | mu_a = %s, mu_b = %s (k_s = -1) | mu_a - mu_b = %s"
              % (r["eta"], r["J1"], r["num"], r["w"], r["mu_a"], r["mu_b"], r["jump"]))
    A = a_board()
    print("\nA  board's configuration")
    print("   our Z2 plane at lam = 2k_L(1+eps): w = k_s/a^2 = %s, v = mu/a^4 = %s; at RS: w = %s, v = %s"
          % (A["z2_w"], A["z2_v"], A["rs_w"], A["rs_v"]))
    print("   direct (a, mu_s) solve at RS: k_s=+1 %s, k_s=0 %s, k_s=-1 %s" % (A["direct"][1], A["direct"][0],
                                                                           A["direct"][-1]))
    print("   Phi_1 = 0 identically at mu_s = 0, k_s = 0: %s;  position 2 then: %s, Phi_2 = 0 identically: %s"
          % (A["Phi1_zero"], A["p2"], A["Phi2_zero"]))
    print("   -> the corridor is absent (mu_s = 0) and the separation ell ln(a1/a2) is free: the massless radion")
    H = h_two_planes()
    print("\nH  our plane non-Z2 (138), k_s = -1 (the only slicing S allows); plane-1 parameter x, plane-2 x2")
    print("   S reproduced at both planes: %s" % H["S_check"])
    print("   mu_s matching: %s = 0;  Q = %s;  Q roots x2 = %s;  disc_x2(Q) = %s"
          % (H["P"], H["Q"], H["Q_roots"], H["Q_disc"]))
    print("   non-naked sets in |x| < 1: slab %s, ours-beyond %s; position 2's beyond on the coincident branch %s"
          % (H["mus_ok_set"], H["mu1_ok_set"], H["mu2_coinc_ok_set"]))
    print("   sample of the solution set (k_L = 1):")
    for r in H["rows"]:
        if not r.get("ok_s") or r["x"] not in (sp.Rational(-39, 40), sp.Rational(-35, 40), sp.Rational(-30, 40),
                                               sp.Rational(-10, 40), sp.Rational(10, 40), sp.Rational(30, 40)):
            continue
        print("     x = %-7s %-19s x2 = %-9s a1 = %-8s a2 = %-8s mu_s = %-9s mu_1 = %-9s mu_2 = %-9s a2<a1 %s slab "
              "static %s mu1 ok %s mu2 ok %s" % (r["x"], r["branch"], fmt(r["x2"]), fmt(r["a1"]), fmt(r["a2"]),
                                                fmt(r["mus"]), fmt(r["mu1"]), fmt(r["mu2"]), r["a2_lt_a1"],
                                                r["slab_static"], r["mu1_ok"], r["mu2_ok"]))
    print("   admissible members (A1-A8): %d of %d sampled; with A7 relaxed and a2 < a1: %d (a one-parameter family)"
          % (len(H["admissible"]), len([r for r in H["rows"] if r.get("ok_s")]), len(H["admissible_relaxA7"])))
    B = b_bridge(H)
    print("\nB  the bridge: Z2 at ours gives (v, w) = %s -> mu_s = 0, no horizon; non-Z2 needs slab and ours-beyond "
          "both non-naked: %s" % (B["z2"], B["both"]))
    print("   position 2 in the other exterior (slab side inner), flat-limit per-sheet tension: %s -- positive, "
          "against 139 (1)" % B["p2_flat"])
    X = x_extremal()
    print("\nX  extremal SAdS5 horizons: k_s=+1 %s; k_s=0 %s; k_s=-1 %s" % (X[1], X[0], X[-1]))
    for name, info in X["sides"].items():
        print("   %-26s %s" % (name, [(i["x"], i["s_over_kL"], "a/r_h = %s" % i["a_over_rh"]) for i in info]))
    print("   any static plane at these tensions bordering an extremal bulk from outside its horizon: %s"
          % X["any_admissible"])
    T = t_instant()
    print("\nT  H = 0 at one instant (Z2 RS): mu_s = %s (k_s=+1), %s (k_s=-1); addot = %s; k_s=+1 outside horizon: %s"
          % (T[1], T[-1], T["addot"], T["outside"]))
    C = controls()
    print("\nC  controls")
    print("   C1 mu = 0 at RS: FREE %s; 10%% off RS at mu = 0: NONE %s" % (C["C1_free"], C["C1_off_none"]))
    print("   C2 off RS (Z2): w = %s, v = %s" % (C["C2_w"], C["C2_v"]))
    for r in C["C2"]:
        print("      eps = %-6s k_s = %+d a1 = %s mu_s = %s position 2: %s" % (r["eps"], r["ks"], fmt(r["a1"]),
                                                                           fmt(r["mus"]), r["p2"]))
    print("   C3 literal per-sheet -1/4 of ours at position 2: J2 residual %s (no static plane)" % C["C3"])
    M = readme_m()
    print("\nREADME m = %s m, r0 = 2m = %s m" % (M["m"], M["r0"]))
    print("   (X's equality, refuted) r_h = ell/sqrt2 read as r0 = 2m: ell = 2 sqrt2 m = %s m = 2.828m; window needs "
          "ell > 27.07m, i.e. r_h > %.3fm" % (sp.N(2 * sp.sqrt(2) * M["m"], 6), 27.07 / 2**0.5))


def selftest():
    ok = n = 0

    def chk(name, cond):
        nonlocal ok, n
        n += 1
        ok += bool(cond)
        print("  [%s] %s" % ("ok" if cond else "FAIL", name))

    D = d_derivation()
    chk("D (STRUCTURAL): J2 = (d/dtau J1)/adot, any two sides; static t-form", D["J2_is_dJ1"] and D["t_form_ok"])
    chk("D: Z2 form H^2 = lam^2/4 - k^2 - k_s/a^2 + mu/a^4 (dark radiation)", D["H2_matches_standard"])
    S = s_lemma()
    chk("S: all four orientations, tuned tension -> w = k_s/a^2 = -2 delta^2 (J1 solved identically)",
        all(r["J1"] == 0 and r["w"] == [-2 * d**2] for r in S))
    chk("S: the mass jump across a tuned plane is mu_a - mu_b = -lam/(2 delta^3)",
        all(sp.simplify(r["jump"] + r["lam"] / (2 * d**3)) == 0 for r in S))
    A = a_board()
    chk("A: our Z2 RS plane: w = 0 and v = 0 (so k_s = 0, mu_s = 0)", A["rs_w"] == 0 and A["rs_v"] == 0)
    chk("A (direct (a, mu_s)): k_s = 0 forces mu_s = 0; k_s = +-1 no solution",
        A["direct"][0] == [{mus: 0}] and A["direct"][1] == [] and A["direct"][-1] == [])
    chk("A: position 2 forces mu_2 = 0; both Phi vanish identically (the radion is flat)",
        [r["v2"] for r in A["p2"]] == [0] and A["Phi1_zero"] and A["Phi2_zero"])
    H = h_two_planes()
    chk("H: S reproduced at both planes; matching factors as (x + x2) Q", H["S_check"] and
        sp.expand(H["P"] - (x + x2) * H["Q"]) == 0)
    chk("H: Q real only for x <= -2/3 or x >= 2 (discriminant sign)",
        all((sp.N(H["Q_disc"].subs(x, v)) >= 0) == (v <= sp.Rational(-2, 3) or v >= 2)
            for v in (sp.Rational(-9, 10), sp.Rational(-1, 2), sp.Rational(1, 2), 3)))
    chk("H: ours-beyond non-naked only for x in (0, 1); slab non-naked only for x in (-1, 0)",
        H["mu1_ok_set"] == sp.Interval.open(0, 1) and H["mus_ok_set"] == sp.Interval.open(-1, 0))
    chk("H: no admissible member under A1-A8; with A7 relaxed a continuous family remains (a modulus, no equality)",
        len(H["admissible"]) == 0 and len(H["admissible_relaxA7"]) >= 3)
    B = b_bridge(H)
    chk("B: the bridge is excluded (Z2: mu_s = 0; non-Z2: no x with both sides non-naked)",
        B["z2"] == (0, 0) and B["both"] == sp.EmptySet)
    X = x_extremal()
    chk("X: only k_s = -1 has an extremal SAdS5 horizon, mu = -ell^2/4 at r_h = ell/sqrt2",
        X[1] == [] and X[0] == [] and len(X[-1]) == 1 and sp.simplify(X[-1][0][mu] + 1 / (4 * kL**2)) == 0 and
        sp.simplify(X[-1][0][R] - 1 / (sp.sqrt(2) * kL)) == 0)
    chk("X: no static plane at these tensions borders an extremal bulk from outside its horizon",
        not X["any_admissible"])
    T = t_instant()
    chk("T: H = 0 alone gives mu_s = a1^2 (k_s = +1), free of ell, outside the horizon",
        sp.simplify(T[1] - a**2) == 0 and T["outside"])
    C = controls()
    chk("C1 control: RS flat plane FREE; 10% off RS at mu = 0 the detector says NONE", C["C1_free"] and C["C1_off_none"])
    c2neg = [r for r in C["C2"] if r["eps"] < 0]
    chk("C2 control: off RS below (eps < 0) the two-plane system is FIXED: isolated (a1, mu_s, a2, mu_2)",
        all(isinstance(r["p2"], list) and len(r["p2"]) >= 1 for r in c2neg))
    chk("C2 control: off RS above (eps > 0) our plane is FIXED at k_s = +1 and position 2 then has NONE",
        [r["p2"] for r in C["C2"] if r["eps"] > 0] == ["NONE (S: w2 <= 0)"])
    chk("C3 sensitivity: the literal per-sheet -1/4 has no static position 2", all(v != 0 for v in C["C3"]))
    print("selftest: %d/%d" % (ok, n))
    return ok == n


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    report()
