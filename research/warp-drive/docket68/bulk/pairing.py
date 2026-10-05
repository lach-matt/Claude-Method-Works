#!/usr/bin/env python3
"""
pairing.py -- BULK-O1: what shape of the higher dimension would make a chosen destination close through it
(H-BULK-PAIRING), and what each shape needs.

Not seated; not yet verified.  M (rulings item 59): "4, then 3 please." -- bulk.py seated, then the pairing shape, then
entering and leaving (O6, with H-DETACH and H-CORRIDOR-STASIS folded in: item 61).  Carried as M's hypotheses
H-HIGHER-CORRIDOR and H-NO-SPEED, never as results.  O9 stays OPEN.

    python3 pairing.py              report
    python3 pairing.py --selftest   checks, with CONTROLS (sympy inside functions)
    python3 pairing.py --json       the numbers as JSON

THE QUESTION.  bulk.py found that whether the corridor lands far away depends on the bulk's shape.  Three published
routes make brane-distant points bulk-near; this file prices what each NEEDS.

  (1) A WARPED SECOND PLANE (Chung & Freese hep-ph/9910235v2 eq. 3, READ): ds^2 = dt^2 - [e^{-2ku} a^2 dh^2 + du^2].
      Its bulk stress-energy is COMPUTED here symbolically from the metric (G^M_N) and checked against CF's own eq. 37
      (p.8, static: T^0_0 = -6k^2, T^1_1 = -3k^2, T^4_4 = -3k^2).  The null energy condition (R_ab k^a k^b >= 0, a
      signature-independent sign) is evaluated along null directions.  CONTROL: Randall-Sundrum's AdS slice gives exactly
      0 (pure cosmological constant saturates it).  The design figure: to land a destination D away at our clock reading
      T, CF's static reading 2L/c + e^{-kL} D/c = T needs kL >= ln(D / (cT - 2L)).
  (2) A BENT PLANE (Ishihara gr-qc/0007070v2, READ): with an AdS bulk (the NEC holds) a brane carrying matter with
      T_ab k^a k^b > 0 is 'concave towards M in the null direction' and bulk shortcuts appear (eq. 11, p.5); 'The
      magnitude of the apparent causality violation becomes larger when the matter on the brane becomes more dense'
      (p.5).  Caldwell & Langlois p.8: shortcuts from a local distortion are negligible, lambda = c (r^3/GM)^{1/2} ~ 1e13
      cm for the Earth.  Printed for the Earth (asked of seat.py's constants) -- STRUCTURAL beyond that.
  (3) A FOLDED PLANE (the Manyfold, hep-ph/9911386v1, READ): the bulk is flat (the NEC holds) and folding is EXTRINSIC,
      so light along the brane sees nothing; but gravity crosses the bulk: a destination brought within a bulk gap r
      pulls with its mass at r.  Printed for Proxima at r = 1 mm against its pull at its brane distance (H-FOLD-NEWTON:
      4D Newton at r, as ADDK's own sub-mm folds assume gravity is 4D at the fold gap) -- an observed Proxima is not
      bulk-near (STRUCTURAL; a quantitative bound needs ephemeris limits READ, OPEN).  ADDK sec. 7: a folded brane is
      not a BPS state and tends to collapse; it needs stabilization.

  THE TIME-DELAY THEOREMS (READ): Gao & Wald gr-qc/0007021v2 -- under the NEC and the null generic condition, (Thm 1,
  null geodesically complete) fastest null geodesics between far points avoid a given compact set; (Thm 2, a timelike
  conformal boundary) the fastest null geodesic between boundary points lies in the boundary, so 'generic perturbations
  of anti-de Sitter spacetime always produce a time delay' (abstract).  A brane is not AdS's conformal boundary, so
  Thm 2 does not apply to braneworlds directly; route (1) evades both theorems' premise by violating the NEC, route (2)
  keeps it and gets its shortcut from the brane's matter, route (3) keeps it and moves the brane.  The board's D5 (Olum)
  already prices 4D superluminal travel in NEC violation; route (1) is its bulk analogue (H-D5-ANALOGUE).

NAMED HYPOTHESES
  H-M5 (the 5D Planck scale that prices route 1's violation in kg/m^3 -- unfixed), H-THREE-ROUTES (the three routes are the published ones; nothing shows they exhaust the shapes -- a SURVEY, not a
  theorem), H-CF-STATIC, H-L-ILLUSTRATIVE, H-FOLD-NEWTON, H-D5-ANALOGUE; with M's H-HIGHER-CORRIDOR, H-BULK-PAIRING (bulk.py).
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
GM_SUN = 1.3271244e20                 # IAU 2015 B3 (READ, held in localclock.py; restated here as the same READ value)
GM_EARTH = 3.986004e14                # IAU 2015 B3 nominal (GM)_E (verifier-READ, localclock.py)
R_EARTH = 6.3781e6
M_PROXIMA_SUN = 0.1221                # Faria 2022 (READ, seat.py)
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
    k = sp.symbols("k", positive=True)
    cf = lambda t, x, y, z, u: sp.diag(1, -sp.exp(-2 * k * u), -sp.exp(-2 * k * u), -sp.exp(-2 * k * u), -1)
    rs = lambda t, x, y, z, u: sp.diag(sp.exp(-2 * k * u), -sp.exp(-2 * k * u), -sp.exp(-2 * k * u),
                                       -sp.exp(-2 * k * u), -1)
    cf_g, cf_nec = nec_values(cf, {"t-u": lambda t, x, y, z, u: [1, 0, 0, 0, 1],
                                   "t-x": lambda t, x, y, z, u: [1, sp.exp(k * u), 0, 0, 0],
                                   "t-(x,u)": lambda t, x, y, z, u: [1, sp.exp(k * u) / sp.sqrt(2), 0, 0,
                                                                     1 / sp.sqrt(2)]})
    rs_g, rs_nec = nec_values(rs, {"t-u": lambda t, x, y, z, u: [sp.exp(k * u), 0, 0, 0, 1],
                                   "t-x": lambda t, x, y, z, u: [1, 1, 0, 0, 0]})
    per_k2 = lambda e: float(sp.simplify(e / k ** 2))
    return {"cf_G_mixed_over_k2": [per_k2(e) for e in cf_g], "cf_nec_over_k2": {n: per_k2(e) for n, e in cf_nec.items()},
            "rs_G_mixed_over_k2": [per_k2(e) for e in rs_g], "rs_nec_over_k2": {n: per_k2(e) for n, e in rs_nec.items()}}


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
            "ishihara_lambda_earth_cm": lam_earth_m * 100,
            "fold_pull_1mm_m_s2": gm_prox / 1e-3 ** 2, "fold_pull_brane_m_s2": gm_prox / L_PROXIMA ** 2}


def report():
    d = compute()
    r = d["routes"]
    print("BULK-O1: the shapes that make a destination close through the higher dimension (not verified; not seated)\n")
    print("(1) a warped second plane (Chung-Freese): G^M_N / k^2 = %s (CF eq. 37 static: -6, -3, -3); null energy "
          "R_ab k^a k^b / k^2 = %s -- VIOLATED in every null direction tested" % (
              [round(v, 6) for v in r["cf_G_mixed_over_k2"]], {n: round(v, 6) for n, v in r["cf_nec_over_k2"].items()}))
    print("    CONTROL Randall-Sundrum: G^M_N / k^2 = %s, null energy %s -- saturated, not violated" % (
        [round(v, 6) for v in r["rs_G_mixed_over_k2"]], {n: round(v, 6) for n, v in r["rs_nec_over_k2"].items()}))
    print("    to land the Proxima span at our clock reading T (L = 1 mm, %s): " % CF_PATCH_CAVEAT + ", ".join(
        "T %.0f s: kL %.2f (compression %.2e, k = %.2e /m)" % (x["T_s"], x["kL_needed"], x["compression"], x["k_per_m"])
        for x in d["designs"])
          + "; CF's published kL = %.2f" % d["cf_published_kL"])
    print("(2) a bent plane (Ishihara): the NEC holds in the bulk; the shortcut comes from brane matter and grows with "
          "density; for the Earth Caldwell-Langlois's scale c (r^3/GM)^1/2 = %.2e cm -- negligible" %
          d["ishihara_lambda_earth_cm"])
    print("(3) a folded plane (Manyfold): the NEC holds; light along the plane sees nothing, gravity crosses the bulk -- "
          "Proxima within 1 mm through the bulk would pull at %.2e m/s^2, against %.2e m/s^2 at its brane distance" % (
              d["fold_pull_1mm_m_s2"], d["fold_pull_brane_m_s2"]))


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
    chk("the null energy condition is violated in Chung-Freese's bulk along every null direction tested (%s)" %
        {n: round(v, 6) for n, v in r["cf_nec_over_k2"].items()}, all(v < 0 for v in r["cf_nec_over_k2"].values()))
    chk("Randall-Sundrum's AdS slice: G^M_N = -6 k^2 delta (a pure cosmological constant) and the null energy "
        "condition exactly saturated (%s)" % {n: round(v, 9) for n, v in r["rs_nec_over_k2"].items()},
        all(abs(v + 6) < 1e-9 for v in r["rs_G_mixed_over_k2"]) and all(abs(v) < 1e-9 for v in r["rs_nec_over_k2"].values()),
        ctl=True)
    chk("the design figure inverts the static reading: at the kL found for T = 1 day, 2L/c + e^{-kL} D/c = 1 day (rel. "
        "%.1e)" % abs(bulk.cf_reading(L_PROXIMA, bulk.CF["L_illustrative_m"], d["designs"][1]["kL_needed"]) / 86400 - 1),
        abs(bulk.cf_reading(L_PROXIMA, bulk.CF["L_illustrative_m"], d["designs"][1]["kL_needed"]) / 86400 - 1) < 1e-9)
    structural.append("route (1) evades the time-delay theorems' premise by violating the NEC in the bulk -- the bulk "
                      "analogue of D5 (H-D5-ANALOGUE); route (2) keeps the NEC and takes its shortcut from brane matter; "
                      "route (3) keeps it and moves the brane")
    structural.append("folding is extrinsic, so light along the plane cannot see it; gravity crosses the bulk, so a "
                      "bulk-near star would pull at its bulk distance; an observed Proxima is not bulk-near")
    structural.append("H-THREE-ROUTES: these are the published routes; nothing here shows they exhaust the shapes")
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
