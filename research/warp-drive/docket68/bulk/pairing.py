#!/usr/bin/env python3
"""
pairing.py -- BULK-O1: what shape of the higher dimension would make a chosen destination close through it
(H-BULK-PAIRING), and what each shape needs.

SEATED in ledger.py section 8j (M-RULINGS item 64); verified once (2026-10-05), findings applied (HISTORY below).  M (rulings item 59): "4, then 3 please." -- bulk.py seated, then the pairing shape, then
entering and leaving (O6, with H-DETACH and H-CORRIDOR-STASIS folded in: item 61).  Carried as M's hypotheses
H-HIGHER-CORRIDOR and H-NO-SPEED, never as results.  O9 stays OPEN.

    python3 pairing.py              report
    python3 pairing.py --selftest   checks, with CONTROLS (sympy inside functions)
    python3 pairing.py --json       the numbers as JSON

THE QUESTION.  bulk.py found that whether the corridor lands far away depends on the bulk's shape.  Three published
shapes that make brane-distant points bulk-near are surveyed here (not exhaustive: H-THREE-ROUTES), with what each NEEDS.

  (1) A WARPED SECOND PLANE (Chung & Freese hep-ph/9910235v2 eq. 3, READ): ds^2 = dt^2 - [e^{-2ku} a^2 dh^2 + du^2].
      Its bulk stress-energy is COMPUTED here symbolically from the metric (G^M_N) and checked against CF's own eq. 37
      (p.8, static: T^0_0 = -6k^2, T^1_1 = -3k^2, T^4_4 = -3k^2).  The null energy condition (NEC, R_ab k^a k^b >= 0,
      Gao-Wald eq. 2; the sign does not change under g -> -g) is evaluated for a GENERAL null vector: -3k^2 in every
      direction (static CF is ultrastatic, R x H^4).  CONTROL: Randall-Sundrum's AdS slice gives exactly 0.  CONTROL: a
      static warp with dt^2 unwarped and e^{3B} = 1 - c u^2 compresses the hidden plane's distances and KEEPS the NEC
      (positive in both directions) -- so the price is CF's exponential warp's, not every warp's; it pays with a
      curvature singularity at u = 1/sqrt(c), and junction conditions may move the price onto the hidden brane (on the
      verifier's reading of CF eq. 36 with the normal reversed, H-ORIENTATION, CF's own hidden brane has rho + P < 0).
      With CF's time-dependent eq. 3 in the radiation era (a ~ t^{1/2}) the NEC holds only at kt <~ 0.1, before the
      path (t > 2L, kt > 23) can be completed: the early universe does not rescue route 1.
      The design figure: to land a destination D away at our clock reading T, CF's static reading 2L/c + e^{-kL} D/c = T
      needs kL >= ln(D / (cT - 2L)).
  (2) A BENT PLANE (Ishihara gr-qc/0007070v2, READ): with an AdS bulk (the NEC saturated, as in the RS control) a brane
      carrying matter with T_ab k^a k^b > 0 is 'concave towards M in the null direction' and bulk shortcuts appear (eq.
      11, p.5); 'The magnitude of the apparent causality violation becomes larger when the matter on the brane becomes
      more dense' (p.5); near the initial singularity there is 'no particle horizon' (pp.7-8).  Caldwell & Langlois
      (gr-qc/0103070v1, READ): at high energy the bulk-to-brane horizon ratio reaches ~10^3 (~10^4 on BBN alone; eq.
      25, p.7); for a local body, assuming l/lambda plays the role of lH, lambda = c (r^3/GM)^{1/2} ~ 10^13 cm for the
      Earth and the shortcut is negligible (p.8) -- 2.42e13 cm computed here from IAU constants.
  (3) A FOLDED PLANE (the Manyfold, ADDK hep-ph/9911386v1, READ): the bulk is flat (NEC trivially satisfied) and folding
      is EXTRINSIC: light along the plane sees no fold locally and reaches the other fold only round the tip (the long
      brane distance; 'old light', p.3).  Gravity crosses the bulk: ADDK's 'two different minimal distances:
      gravitational ... and electromagnetic' (p.2); 'Nearby matter on other folds can be detected gravitationally as
      dark matter' (abstract).  At planetary distances (>> the bulk size) gravity is 4D -- ADDK's own dark-matter premise
      -- so Proxima's mass bulk-near (within ~1 mm through the bulk) to any point of the solar system would pull like a
      0.12 M_sun body there: at 1 AU, 12 % of the Sun's pull (H-FOLD-NEWTON: 4D Newton, a FLOOR when the gap is <= the
      bulk size, since below it gravity is (4+N)-dimensional and stronger; the 1 mm point-mass figure is an
      idealisation).  So Proxima is not bulk-near to the solar system -- one fold arrangement for one star, not the fold
      route.  ADDK sec. 7: a folded brane 'becomes unstable, with a tendency to collapse' (p.21), but kink/anti-kink and
      domain-wall mechanisms follow and 'a Manyfold universe may be stable despite the tendencies towards
      self-annihilation' (p.23).

  THE TIME-DELAY THEOREMS (READ): Gao & Wald gr-qc/0007021v2 -- under the NEC and the null generic condition, (Thm 1,
  null geodesically complete) fastest null geodesics between far points avoid a given compact set; (Thm 2, a timelike
  conformal boundary) the fastest null geodesic between boundary points lies in the boundary, so 'generic perturbations
  of anti-de Sitter spacetime always produce a time delay' (abstract).  Neither covers these routes (STRUCTURAL).  The
  board's D5 (Olum) prices 4D superluminal travel in NEC violation for leads WITHOUT a reference geometry; CF's shortcut
  is a lead against the brane's own geometry, so calling route 1 D5's bulk analogue is a hypothesis (H-D5-ANALOGUE).

NAMED HYPOTHESES
  H-M5 (the 5D Planck scale that prices route 1's violation in kg/m^3 -- unfixed); H-THREE-ROUTES (a SURVEY, not a
  theorem); H-CF-STATIC (CF's static reading); H-L-ILLUSTRATIVE (L = 1 mm); H-FOLD-NEWTON (above); H-D5-ANALOGUE
  (above); H-ORIENTATION (the junction reading above); with M's H-HIGHER-CORRIDOR, H-NO-SPEED, H-BULK-PAIRING (bulk.py)
  and H-UNOBSERVED-UNBUILT (item 62: this file is part of the device line of work).

HISTORY (verifier, 2026-10-05; first-written claims kept)
  * 'violated in every null direction tested' -- three directions; now a general null vector.
  * 'negative-energy-type matter' / 'No negative energy needed' -- an AdS bulk has negative energy density too; what
    separates the routes is the NEC.
  * route 1's price was stated for any warp and as 'the bulk analogue of D5'; it is CF's exponential warp's price, a
    NEC-keeping warp exists, and the D5 analogy is a hypothesis.
  * 'route (1) evades both theorems' premise by violating the NEC' -- neither theorem's other premises hold either.
  * 'H-FOLD-NEWTON: 4D Newton at r, as ADDK's own sub-mm folds assume gravity is 4D at the fold gap' -- ADDK say the
    opposite (p.10, eq. 32); 4D Newton is a floor; the headline is now the 1 AU figure.
  * 'an observed Proxima is not bulk-near' -- scoped to the solar system and one star.
  * the design inversion was counted as a check; it is an identity round trip, now STRUCTURAL.
  * the Earth's lambda was keyed 'ishihara_lambda_earth_cm' and printed as Caldwell-Langlois's 2.4e13 cm; CL print
    ~10^13 cm under an assumption; 2.42e13 is computed.  Constants were said to be 'asked of seat.py'; they are
    restated, and the selftest checks them against their owners.
"""

import contextlib
import importlib.util
import io
import json
import math
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))


def _by_path(key, path):
    if key in sys.modules:
        return sys.modules[key]
    spec = importlib.util.spec_from_file_location(key, path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[key] = mod
    spec.loader.exec_module(mod)
    return mod


with contextlib.redirect_stdout(io.StringIO()):
    bulk = _by_path("bulk_bulk", os.path.join(HERE, "bulk.py"))

C = bulk.C
L_PROXIMA = bulk.L_PROXIMA
YEAR_S = bulk.YEAR_S
# Restated, not imported: importing their owner (cmb/localclock.py, which loads cmbframe and seat) costs ~45 s.  The
# selftest asks the owners and fails if any restated value differs (check 5).
GM_SUN = 1.3271244e20                 # restated from cmb/localclock.py: IAU 2015 B3 nominal (READ there)
GM_EARTH = 3.986004e14                # restated from cmb/localclock.py: IAU 2015 B3 nominal (GM)_E (verifier-READ there)
R_EARTH = 6.3781e6                    # restated from cmb/localclock.py: IAU 2015 B3 nominal R_eE (verifier-READ there)
AU = 149597870700.0                   # restated from seat.py (seat.AU)
M_PROXIMA_SUN = 0.1221                # restated from seat.py FARIA_2022['M_star_sun'] (Faria 2022, READ there)
CF_PATCH_CAVEAT = "patched path; fine tuned (CF p.4, p.8)"


def einstein_mixed(metric):
    """G^M_N and R_MN for a diagonal 5D metric given as a sympy Matrix in coordinates (t, x, y, z, u)."""
    import sympy as sp
    t, x, y, z, u = sp.symbols("t x y z u", real=True)
    X = [t, x, y, z, u]
    g = metric(t, x, y, z, u)
    gi = g.inv()
    n = 5
    gam = [[[sum(gi[a, d] * (sp.diff(g[d, b], X[c]) + sp.diff(g[d, c], X[b]) - sp.diff(g[b, c], X[d]))
                 for d in range(n)) / 2 for c in range(n)] for b in range(n)] for a in range(n)]

    def riem(a, b, c, d):
        return (sp.diff(gam[a][b][d], X[c]) - sp.diff(gam[a][b][c], X[d])
                + sum(gam[a][c][e] * gam[e][b][d] - gam[a][d][e] * gam[e][b][c] for e in range(n)))
    ric = sp.Matrix(n, n, lambda b, d: sp.simplify(sum(riem(a, b, a, d) for a in range(n))))
    R = sp.simplify(sum(gi[a, b] * ric[a, b] for a in range(n) for b in range(n)))
    G = sp.simplify(ric - R * g / 2)
    return sp.simplify(gi * G), ric, X


def nec_values(metric, nulls):
    """R_ab k^a k^b along each given null vector (functions of the coordinates)."""
    import sympy as sp
    Gmix, ric, X = einstein_mixed(metric)
    out = {}
    for name, kfun in nulls.items():
        kv = sp.Matrix(kfun(*X))
        out[name] = sp.simplify((kv.T * ric * kv)[0])
    return [sp.simplify(Gmix[i, i]) for i in range(5)], out


def routes():
    import sympy as sp
    k, c = sp.symbols("k c", positive=True)
    a1, a2, a3 = sp.symbols("a1 a2 a3", real=True)
    cf = lambda t, x, y, z, u: sp.diag(1, -sp.exp(-2 * k * u), -sp.exp(-2 * k * u), -sp.exp(-2 * k * u), -1)
    rs = lambda t, x, y, z, u: sp.diag(sp.exp(-2 * k * u), -sp.exp(-2 * k * u), -sp.exp(-2 * k * u),
                                       -sp.exp(-2 * k * u), -1)
    # a general null vector of static CF: k = (1, e^{ku} n1, e^{ku} n2, e^{ku} n3, n4), |n| = 1 over three angles
    n = (sp.sin(a1) * sp.sin(a2) * sp.cos(a3), sp.sin(a1) * sp.sin(a2) * sp.sin(a3), sp.sin(a1) * sp.cos(a2), sp.cos(a1))
    cf_g, cf_nec = nec_values(cf, {"t-u": lambda t, x, y, z, u: [1, 0, 0, 0, 1],
                                   "t-x": lambda t, x, y, z, u: [1, sp.exp(k * u), 0, 0, 0],
                                   "general": lambda t, x, y, z, u: [1, sp.exp(k * u) * n[0], sp.exp(k * u) * n[1],
                                                                     sp.exp(k * u) * n[2], n[3]]})
    rs_g, rs_nec = nec_values(rs, {"t-u": lambda t, x, y, z, u: [sp.exp(k * u), 0, 0, 0, 1],
                                   "t-x": lambda t, x, y, z, u: [1, 1, 0, 0, 0]})
    # a static warp with dt^2 unwarped that compresses the hidden plane's distances and KEEPS the NEC (verifier's
    # counterexample, computed here): A = 0, e^{3B} = 1 - c u^2, hidden-plane compression (1 - c L^2)^{-1/3}; it needs
    # u < 1/sqrt(c), where a curvature singularity sits
    pw = lambda t, x, y, z, u: sp.diag(1, -(1 - c * u ** 2) ** sp.Rational(2, 3), -(1 - c * u ** 2) ** sp.Rational(2, 3),
                                       -(1 - c * u ** 2) ** sp.Rational(2, 3), -1)
    pw_g, pw_nec = nec_values(pw, {"t-u": lambda t, x, y, z, u: [1, 0, 0, 0, 1],
                                   "t-x": lambda t, x, y, z, u: [1, (1 - c * u ** 2) ** sp.Rational(-1, 3), 0, 0, 0]})
    u = sp.Symbol("u", real=True)
    pw_samples = {name: [float(e.subs({c: 1, u: uu})) for uu in (0.0, 0.3, 0.6, 0.9, 0.99)] for name, e in pw_nec.items()}
    per_k2 = lambda e: sp.simplify(e / k ** 2)
    gen = per_k2(cf_nec["general"])
    return {"cf_G_mixed_over_k2": [float(per_k2(e)) for e in cf_g],
            "cf_nec_over_k2": {nm: float(per_k2(e)) for nm, e in cf_nec.items() if nm != "general"},
            "cf_nec_general_over_k2": str(sp.simplify(sp.trigsimp(gen))),
            "cf_nec_general_is_minus3": sp.simplify(sp.trigsimp(gen) + 3) == 0,
            "rs_G_mixed_over_k2": [float(per_k2(e)) for e in rs_g], "rs_nec_over_k2": {nm: float(per_k2(e)) for nm, e in rs_nec.items()},
            "pw_nec": {nm: str(sp.simplify(e)) for nm, e in pw_nec.items()}, "pw_nec_samples_c1": pw_samples,
            "pw_compression_cL2_0p99": (1 - 0.99) ** (-1.0 / 3)}


def cf_radiation_nec(kts=(0.1, 0.3, 23.0), thetas=361):
    """CF's time-dependent metric (eq. 3 with a = (kt)^{1/2}, radiation era): the minimum of R_ab k^a k^b / k^2 over null
    directions in the (t, x, u) plane, at each kt.  Units k = 1; the value does not depend on u for this metric."""
    import sympy as sp
    kk = 1
    metric = lambda t, x, y, z, u: sp.diag(1, -sp.exp(-2 * kk * u) * t, -sp.exp(-2 * kk * u) * t,
                                           -sp.exp(-2 * kk * u) * t, -1)
    _g, ric, X = einstein_mixed(metric)
    t, x, y, z, u = X
    out = {}
    for kt in kts:
        R = ric.subs({t: kt, u: 0})
        best = None
        for i in range(thetas):
            th = math.pi * i / (thetas - 1) - math.pi / 2
            kv = [1.0, math.cos(th) / math.sqrt(kt), 0.0, 0.0, math.sin(th)]
            val = sum(float(R[a_, b_]) * kv[a_] * kv[b_] for a_ in range(5) for b_ in range(5))
            best = val if best is None or val < best else best
        out[kt] = best
    return out


def design(T_s, L_m=bulk.CF["L_illustrative_m"], D_m=L_PROXIMA):
    """Chung-Freese static: the kL needed to land D away at our clock reading T."""
    room = C * T_s - 2 * L_m
    kL = math.log(D_m / room) if room > 0 else float("inf")
    # the bulk's NEC violation is -3 k^2 / kappa5^2 in every null direction (route 1); k = kL / L sets its size, and
    # pricing it in kg/m^3 needs the 5D Planck scale M5, which no source fixes (H-M5, OPEN)
    return {"T_s": T_s, "kL_needed": kL, "compression": D_m / room if room > 0 else float("inf"),
            "k_per_m": kL / L_m}


def compute():
    r = routes()
    lam_earth_m = C * math.sqrt(R_EARTH ** 3 / GM_EARTH)
    gm_prox = M_PROXIMA_SUN * GM_SUN
    return {"routes": r,
            "designs": [design(T) for T in (YEAR_S, 86400.0, 3600.0, 1.0)],
            "cf_published_kL": bulk.CF["kL"],
            "cf_radiation_nec_min_over_k2": cf_radiation_nec(),
            "cl_lambda_earth_cm": lam_earth_m * 100,
            "fold_pull_proxima_at_1au_m_s2": gm_prox / AU ** 2, "sun_pull_at_1au_m_s2": GM_SUN / AU ** 2,
            "fold_pull_1mm_m_s2": gm_prox / 1e-3 ** 2, "fold_pull_brane_m_s2": gm_prox / L_PROXIMA ** 2}


def report():
    d = compute()
    r = d["routes"]
    print("BULK-O1: the shapes that make a destination close through the higher dimension (verified once; not seated)\n")
    print("(1) a warped second plane (Chung-Freese): G^M_N / k^2 = %s (CF eq. 37 static: -6, -3, -3); null energy "
          "R_ab k^a k^b / k^2 = %s -- VIOLATED; general null direction: %s" % (
              [round(v, 6) for v in r["cf_G_mixed_over_k2"]], {n: round(v, 6) for n, v in r["cf_nec_over_k2"].items()},
              r["cf_nec_general_over_k2"]))
    print("    CONTROL NEC-keeping warp (e^{3B} = 1 - c u^2): NEC t-u = %s, t-x = %s (> 0; singular at u = 1/sqrt c)" % (
        r["pw_nec"]["t-u"], r["pw_nec"]["t-x"]))
    print("    radiation era (a ~ t^1/2), min NEC / k^2 over (t,x,u) directions: %s -- holds only before the path closes" %
          {kt: round(v, 3) for kt, v in d["cf_radiation_nec_min_over_k2"].items()})
    print("    CONTROL Randall-Sundrum: G^M_N / k^2 = %s, null energy %s -- saturated, not violated" % (
        [round(v, 6) for v in r["rs_G_mixed_over_k2"]], {n: round(v, 6) for n, v in r["rs_nec_over_k2"].items()}))
    print("    to land the Proxima span at our clock reading T (L = 1 mm, %s): " % CF_PATCH_CAVEAT + ", ".join(
        "T %.0f s: kL %.2f (compression %.2e, k = %.2e /m)" % (x["T_s"], x["kL_needed"], x["compression"], x["k_per_m"])
        for x in d["designs"])
          + "; CF's published kL = %.2f" % d["cf_published_kL"])
    print("(2) a bent plane (Ishihara): the AdS bulk saturates the NEC; the shortcut comes from brane matter and grows "
          "with density (up to ~1e3 in distance above the brane tension, CL p.7); for the Earth c (r^3/GM)^1/2 = %.2e cm "
          "(CL print ~1e13) -- negligible today" % d["cl_lambda_earth_cm"])
    print("(3) a folded plane (Manyfold): flat bulk, NEC trivially kept; light sees no fold locally, gravity crosses the "
          "bulk -- Proxima bulk-near to the solar system would pull at %.2e m/s^2 at 1 AU, %.1f %% of the Sun's %.2e "
          "(H-FOLD-NEWTON, a floor); idealised point mass at 1 mm: %.2e m/s^2, against %.2e at its brane distance" % (
              d["fold_pull_proxima_at_1au_m_s2"], 100 * d["fold_pull_proxima_at_1au_m_s2"] / d["sun_pull_at_1au_m_s2"],
              d["sun_pull_at_1au_m_s2"], d["fold_pull_1mm_m_s2"], d["fold_pull_brane_m_s2"]))


def selftest():
    n_pass = n_fail = n_ctl = 0
    structural = []

    def chk(label, ok, ctl=False):
        nonlocal n_pass, n_fail, n_ctl
        n_ctl += ctl
        n_pass += bool(ok)
        n_fail += (not ok)
        print("  %s %s%s" % ("ok  " if ok else "FAIL", "CONTROL: " if ctl else "", label))

    d = compute()
    r = d["routes"]
    cfg = r["cf_G_mixed_over_k2"]
    chk("the Einstein tensor computed from Chung-Freese's metric reproduces their eq. 37, static (G^0_0 = -6k^2, "
        "G^i_i = G^u_u = -3k^2): %s" % [round(v, 9) for v in cfg],
        abs(cfg[0] + 6) < 1e-9 and all(abs(v + 3) < 1e-9 for v in cfg[1:]))
    chk("the null energy condition is violated in Chung-Freese's bulk along EVERY null direction: for a general null "
        "vector (three angles) R_ab k^a k^b / k^2 simplifies to %s" % r["cf_nec_general_over_k2"],
        r["cf_nec_general_is_minus3"] and all(v < 0 for v in r["cf_nec_over_k2"].values()))
    chk("Randall-Sundrum's AdS slice: G^M_N = -6 k^2 delta (a pure cosmological constant) and the null energy "
        "condition exactly saturated (%s)" % {n: round(v, 9) for n, v in r["rs_nec_over_k2"].items()},
        all(abs(v + 6) < 1e-9 for v in r["rs_G_mixed_over_k2"]) and all(abs(v) < 1e-9 for v in r["rs_nec_over_k2"].values()),
        ctl=True)
    pws = r["pw_nec_samples_c1"]
    chk("the same NEC code returns POSITIVE values for a static warp (dt^2 unwarped, e^{3B} = 1 - c u^2) that still "
        "compresses the hidden plane (x%.2f at c L^2 = 0.99): t-u %s, t-x %s" % (
            r["pw_compression_cL2_0p99"], [round(v, 3) for v in pws["t-u"]], [round(v, 3) for v in pws["t-x"]]),
        all(v > 0 for v in pws["t-u"] + pws["t-x"]) and r["pw_compression_cL2_0p99"] > 1, ctl=True)
    # the restated constants against their owners (slow: loads cmb/localclock.py and seat.py)
    with contextlib.redirect_stdout(io.StringIO()):
        lc = _by_path("cmb_localclock", os.path.join(os.path.dirname(HERE), "cmb", "localclock.py"))
    pairs = {"GM_SUN": (GM_SUN, lc.GM_SUN), "GM_EARTH": (GM_EARTH, lc.GM_EARTH), "R_EARTH": (R_EARTH, lc.R_EARTH),
             "AU": (AU, lc.AU), "M_PROXIMA_SUN": (M_PROXIMA_SUN, lc.FARIA["M_star_sun"][0])}
    chk("every restated constant equals its owner's value (localclock.py, seat.py): %s" % sorted(pairs),
        all(a == b for a, b in pairs.values()))
    structural.append("the design table inverts CF's static reading 2L/c + e^{-kL} D/c = T for kL (an identity round "
                      "trip, rel. %.1e at T = 1 day: arithmetic, not a test)" % abs(
                          bulk.cf_reading(L_PROXIMA, bulk.CF["L_illustrative_m"], d["designs"][1]["kL_needed"]) / 86400 - 1))
    structural.append("neither Gao-Wald theorem covers these routes: Thm 2 needs a timelike conformal boundary (a brane is "
                      "not one), Thm 1 needs null-geodesic completeness and the null generic condition (a brane-bounded "
                      "slab and a flat bulk are not shown to meet them); route (1) also violates their NEC premise")
    structural.append("H-THREE-ROUTES: three published shapes surveyed, not exhaustive -- Chung-Freese sec. II B-C give a "
                      "fourth (a curved brane in a flat bulk, continuous unpatched shortcuts) and Kalbermann-Halevi are "
                      "NAMED-NOT-READ")
    structural.append("whether every warp that brings a destination close needs NEC violation somewhere is OPEN: the "
                      "NEC-keeping warp above sits beside a curvature singularity at u = 1/sqrt(c), and junction "
                      "conditions may move the price onto the hidden brane (H-ORIENTATION)")
    for s in structural:
        print("  STRUCTURAL: " + s)
    print("pairing.py: %d/%d checks pass, %d of them controls; %d STRUCTURAL printed, not counted" % (
        n_pass, n_pass + n_fail, n_ctl, len(structural)))
    return n_fail == 0


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    elif "--json" in sys.argv:
        print(json.dumps(compute(), indent=1, default=str))
    else:
        report()
