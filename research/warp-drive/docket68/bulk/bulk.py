#!/usr/bin/env python3
"""
bulk.py -- H-HIGHER-CORRIDOR and H-NO-SPEED: two planes joined through a higher dimension, with no speed anywhere.

Not seated; verified once (2026-10-05), its findings applied; first-written claims kept under HISTORY.  M (rulings item
57): "If two points, each on a different spacetime plane, are connected by a corridor through a higher dimension, then
speed cannot exist in the dimension below the corridor as you are at position 1 then position 2, with no in between,
which means no travel, no speed".  M (item 58): "3, then 2, then 1 please" -- the case fixed as two separate planes,
then READ, then modelled.  Carried as M's hypotheses H-NO-SPEED and H-HIGHER-CORRIDOR, never as results.  O9 OPEN.

    python3 bulk.py              report
    python3 bulk.py --selftest   checks, with CONTROLS
    python3 bulk.py --json       the numbers as JSON

THE CASE (item 58's step 3): TWO PLANES, NOT ONE.  Two separate 4D worlds (branes) joined only through a fifth dimension.
Three published geometries with this topology are carried, none of them observed:

  (A) RANDALL & SUNDRUM's two branes (hep-ph/9905221v1, READ via alphaXiv; printed pages): ds^2 = e^{-2 k r_c |phi|} eta
      dx dx + r_c^2 dphi^2 (eq. 12, p.4); 'hidden' brane at phi = 0, 'visible' at phi = pi; between them 'a slice of an
      AdS5 geometry' (p.3); V_hid = -V_vis = 24 M^3 k (eq. 11, p.3).  A visible mass parameter m0 is m = e^{-k r_c pi}
      m0 'when measured with the metric g-bar' (eq. 21, p.5) -- so OUR atoms' observed masses are g-bar masses, and our
      clocks count g-bar time (H-OBSERVED-FRAME).  'If e^{k r_c pi} is of order 10^15' this gives TeV scales (p.6).
      Gravity lives in the bulk; its KK modes couple to visible matter at 'Energy/TeV' (p.6).  DISCREPANCY (a misprint
      or ambiguity in v1, not a refutation): p.6 prints 'kr_c [relation lost] 50' (the 50 is genuine text; p.1's 'only of
      order 50' is M r_c); e^{k r_c pi} = 1e15 gives k r_c = 11.0, and Goldberger & Wise hep-ph/9907447v2 p.3 read 'for
      kr_c around 12' (verifier-READ).
  (B) CHUNG & FREESE's two branes (hep-ph/9910235v2, READ): 'there are two separate 3-branes: one is our observable
      universe and the other is the hidden sector' (p.2); ds^2 = dt^2 - [e^{-2ku} a^2(t) dh^2 + du^2] (eq. 3), our brane
      at u = 0, the hidden at u = L, the dt^2 term 'does not share the conformal factor' (p.3).  A signal leaves our
      brane (A), runs along the hidden brane (B) and returns (C): h(1,2) = e^{kL} int_L^{t_f-L} dt/a against our brane's
      h(1,3) = int_0^{t_f} dt/a (eqs. 7-8, p.4); 'as long as kL ~ ln(10^5)' the horizon problem is solved (p.4).  Their
      caveats travel with it: the path is PATCHED -- the corners 'represent vertices of interactions of the bulk fields
      with the fields confined on the brane' (p.4); 'we have not found continuous paths which return to our brane at a
      point more distant than our naive horizon' (p.4); 'we have a fine tuned solution' (p.8).
  (C) THE MANYFOLD (Arkani-Hamed, Dimopoulos, Dvali & Kaloper, hep-ph/9911386v1, READ): our brane folded in the bulk;
      adjacent folds 'are nearby in the bulk, at sub-millimeter distances' (p.2); an object seen far away 'may in fact be
      just a millimeter away through the bulk!' (p.5); 'different folds can communicate at rates which appear superluminal
      to a brane-localized clock ... However these effects do not violate causality of the theory' (p.15).  It fixes
      which electromagnetically distant points are bulk-near -- H-BULK-PAIRING, answered by a geometry.

WHAT IS COMPUTED (no speed anywhere: only each end's own clock, H-LOCAL-CLOCK; one-way readings by the static slicing,
H-STATIC-SLICING; the round trip is convention-free)
  (1) RS: the jump between bulk-paired points.  Conformal z = e^{ky}/k makes null curves straight; the g-bar interval
      is (e^{k pi r_c} - 1)/k.  Our clock reads it in seconds at k = 2e18 GeV (H-K-PLANCK); a hidden clock built to the
      same Lagrangian (H-SAME-LAGRANGIAN) counts e^{k pi r_c} times as many ticks.  Checked by integrating the null
      geodesic in y numerically.  CONTROL: k -> 0 at fixed r_c gives both clocks pi r_c / c.
  (2) RS: landing elsewhere.  In conformal coordinates every causal curve has dt >= int sqrt(dx^2 + dz^2) >= |dx|, so
      landing a distance D away reads at least D's light time on our clock -- for EVERY causal curve, in static, flat-brane
      RS (H-RS1).  STRUCTURAL; printed for the Proxima span.
  (3) CF: landing elsewhere along A-B-C (static, a = 1: H-CF-STATIC): our clock reads 2L/c + e^{-kL} D/c, shorter than
      D/c once D > 2L/(1 - e^{-kL}).  At CF's kL = ln(1e5) the Proxima span's term is printed; L is free in CF (they need
      L >> 100/M5, p.8), so 2L/c is printed for an illustrative L = 1 mm (H-L-ILLUSTRATIVE).  POSITIVE CONTROL: below the
      threshold no shortcut, above it one.
  (4) MANYFOLD: a 1 mm bulk gap reads 1 mm / c on our clock; Proxima itself is seen at its light time, so it is on OUR
      fold, and the Manyfold pairs only electromagnetically distant points.  STRUCTURAL.
  (5) One plane (the board's present case): static RS, no shortcut (STRUCTURAL, by (2)); Caldwell & Langlois's expanding
      single brane with an infinite bulk (gr-qc/0103070v1 eq. 22, p.6; RS2-type, valid for a_B >> a_A), evaluated at l =
      1/k and as their bound l H0 <~ 1e-29; the board's moving brane (branelink O7), AT MOST 93.8 ns under its conditions.
  (6) Loops: static RS has a global time; CF hide their apparent causality violation today (p.8); the Manyfold 'do[es]
      not violate causality'.  Gao & Wald gr-qc/0007021 (a time-delay theorem under the NEC) -- NAMED-NOT-READ.
      STRUCTURAL.
  (7) Entering and leaving (O6): in RS ordinary matter is confined; what crosses is gravitational -- KK modes produced
      and detected through their decay products (RS p.6-7; collider rates in Davoudiasl, Hewett & Rizzo hep-ph/9909255,
      NAMED-NOT-READ); in CF, bulk-brane interactions at the corners, unsuppressed (p.5).  The board has not computed or
      READ a rate for a carrier of the defining information (M-D68-1).  STRUCTURAL.

NAMED HYPOTHESES
  H-RS1, H-RS1-WARP (e^{k pi r_c} = 1e15), H-K-PLANCK (k = 2e18 GeV; with RS's M_Pl^2 = M^3/k this sets M = k, the edge of
  RS's 'k < M' (p.4); every RS interval scales as 1/k), H-OBSERVED-FRAME, H-SAME-LAGRANGIAN, H-STATIC-SLICING,
  H-BULK-PAIRING, H-CF-STATIC, H-CF-PATCHED (the A-B-C path needs bulk-brane interactions at its corners),
  H-L-ILLUSTRATIVE, H-MM-FOLD, H-GRAVITATIONAL-CARRIER; with M's H-NO-SPEED, H-HIGHER-CORRIDOR and H-LOCAL-CLOCK.

HISTORY (verifier, 2026-10-05; first-written claims kept)
  * 'each end's clock reads: hidden 3.291e-28 s, visible 3.291e-43 s' and 'ours reads about the Planck time' -- the
    visible proper time was written in hidden-frame units; our atoms keep their observed masses in g-bar, so OUR clock
    reads the g-bar interval, 3.29e-28 s = hbar/(2 TeV); a hidden clock of the same Lagrangian counts 1e15 times more.
  * 'the catch: landing elsewhere costs at least the light time' was stated as general and 'no source says what fixes
    [the pairing]' -- the floor holds for static flat-brane RS only; Chung-Freese's two branes and the Manyfold are
    published counterexamples (with their caveats), now carried.
  * four of six checks could not fail and the control was the same identity; the detour 'costs between +1.2e-20 and
    +3.1e-37' were hand-picked depths, not bounds (the infimum is 0); Caldwell-Langlois eq. 22 was applied at z = 0, out
    of its validity, and to RS1 rather than their single infinite-bulk brane; O7's 93.8 ns is a MAXIMUM under
    conditions; 'exists as published physics' (RS is a model, unobserved) and 'no one has computed a rate' (KK-production
    rates exist) were too strong.
"""

import contextlib
import importlib.util
import io
import json
import math
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
WD = os.path.dirname(os.path.dirname(HERE))


def _by_path(key, path):
    if key in sys.modules:
        return sys.modules[key]
    spec = importlib.util.spec_from_file_location(key, path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[key] = mod
    spec.loader.exec_module(mod)
    return mod


_saved_path = list(sys.path)
sys.path.insert(0, WD)                                # branelink and cosmo import their peers by name
try:
    with contextlib.redirect_stdout(io.StringIO()):
        branelink = _by_path("wd_branelink", os.path.join(WD, "branelink.py"))
        cosmo = _by_path("wd_cosmo", os.path.join(WD, "cosmo.py"))
finally:
    sys.path[:] = _saved_path

C = branelink.C
HBARC_GEV_M = branelink.HBARC_GEV_M
L_PROXIMA = branelink.L_PROXIMA
YEAR_S = 365.25 * 86400.0
RS = {"warp": 1e15, "k_GeV": 2e18}
CF = {"kL": math.log(1e5), "L_illustrative_m": 1e-3}
CL = {"lH0_bound": 1e-29}
MANYFOLD_GAP_M = 1e-3


def rs_geometry(warp=RS["warp"], k_gev=RS["k_GeV"]):
    kpr = math.log(warp)
    inv_k_m = HBARC_GEV_M / k_gev                                  # 1/k in g-bar units
    return {"k_pi_rc": kpr, "k_rc": kpr / math.pi, "inv_k_m": inv_k_m, "inv_k_s": inv_k_m / C,
            "dz": math.exp(kpr) - 1.0, "k_vis_GeV": k_gev * math.exp(-kpr), "pi_rc_m": kpr * inv_k_m}


def rs_null_numeric(kpr, p_over_e=0.0, n=200000):
    """The null geodesic from y = 0 to k y = kpr in the y-coordinate: dt/dy = E e^{ky}/sqrt(E^2 - P^2) (units 1/k)."""
    s = 1.0 / math.sqrt(1.0 - p_over_e ** 2)
    h = kpr / n
    acc = sum((1 if i in (0, n) else (4 if i % 2 else 2)) * math.exp(i * h) for i in range(n + 1))
    return s * acc * h / 3


def rs_jump(g):
    """One-way g-bar interval between bulk-paired points: OUR clock's reading (H-OBSERVED-FRAME); a hidden clock of the
    same Lagrangian counts e^{k pi r_c} times as many ticks (H-SAME-LAGRANGIAN); the round trip on our clock."""
    t = g["dz"] * g["inv_k_s"]
    return {"ours_s": t, "hidden_own_s": t * math.exp(g["k_pi_rc"]), "round_trip_ours_s": 2 * t,
            "ours_via_kk_scale_s": HBARC_GEV_M / g["k_vis_GeV"] / C}


def cf_reading(D_m, L_m, kL=CF["kL"]):
    """Chung-Freese A-B-C, static: our clock reads 2L/c + e^{-kL} D/c (H-CF-STATIC, H-CF-PATCHED)."""
    return (2 * L_m + math.exp(-kL) * D_m) / C


def cf_threshold_m(L_m, kL=CF["kL"]):
    return 2 * L_m / (1 - math.exp(-kL))


def compute():
    g = rs_geometry()
    j = rs_jump(g)
    gk = rs_geometry(warp=math.exp(g["k_pi_rc"] * 1e-6), k_gev=RS["k_GeV"] * 1e-6)   # k -> 0 at fixed r_c
    jk = rs_jump(gk)
    L = CF["L_illustrative_m"]
    thr = cf_threshold_m(L)
    h0 = cosmo.H0()
    lH0 = g["inv_k_m"] * h0 / C
    with contextlib.redirect_stdout(io.StringIO()):
        o7 = branelink.o7_exact()
    return {"rs": g, "rs_jump": j, "rs_numeric_dt": rs_null_numeric(g["k_pi_rc"]),
            "flat_control": {"ours_s": jk["ours_s"], "hidden_own_s": jk["hidden_own_s"] / math.exp(gk["k_pi_rc"]),
                             "pi_rc_over_c_s": gk["pi_rc_m"] / C},
            "rs_proxima_floor_yr": L_PROXIMA / C / YEAR_S,
            "cf": {"kL": CF["kL"], "proxima_term_s": math.exp(-CF["kL"]) * L_PROXIMA / C,
                   "two_L_over_c_s_at_1mm": 2 * L / C, "proxima_total_s_at_1mm": cf_reading(L_PROXIMA, L),
                   "threshold_m_at_1mm": thr, "below": cf_reading(0.5 * thr, L) < 0.5 * thr / C,
                   "above": cf_reading(2 * thr, L) < 2 * thr / C,
                   "static_ratio_tf_1e6L": math.exp(CF["kL"]) * (1e6 - 2) / 1e6},
            "manyfold_gap_s": MANYFOLD_GAP_M / C,
            "cl": {"lH0_at_1_over_k": lH0, "advance_z1090_at_1_over_k": 0.1 * lH0 ** 2 * 1091 ** 2.5,
                   "advance_z1090_bound": 0.1 * CL["lH0_bound"] ** 2 * 1091 ** 2.5},
            "o7_max_ns": float(o7["Delta_tau ns"]), "o7_light_time_yr": float(o7["Proxima light time yr"])}


def report():
    d = compute()
    g, j, cf, cl = d["rs"], d["rs_jump"], d["cf"], d["cl"]
    print("H-HIGHER-CORRIDOR: two planes joined through a fifth dimension (verified once; not seated)\n")
    print("(1) Randall-Sundrum: k r_c = %.2f from e^{k pi r_c} = %.0e; KK scale k e^{-k pi r_c} = %.0f GeV" % (
        g["k_rc"], RS["warp"], g["k_vis_GeV"]))
    print("    jump between bulk-paired points (no path in either plane): OUR clock %.3e s (= hbar/KK scale %.3e s); a "
          "hidden clock of the same Lagrangian %.3e s of its own; round trip on ours %.3e s; numerical geodesic %.6e vs "
          "closed form %.6e (units 1/k)" % (j["ours_s"], j["ours_via_kk_scale_s"], j["hidden_own_s"],
                                             j["round_trip_ours_s"], d["rs_numeric_dt"], g["dz"]))
    print("(2) Randall-Sundrum, landing elsewhere: every causal curve reads at least the light time -- for the Proxima "
          "span %.4f yr on our clock (STRUCTURAL)" % d["rs_proxima_floor_yr"])
    print("(3) Chung-Freese, landing elsewhere via the hidden plane (patched path, static): our clock 2L/c + e^{-kL} D/c; "
          "at kL = ln(1e5) the Proxima span's term is %.1f s (%.1f min); 2L/c = %.2e s at L = 1 mm; shortcut beyond D = "
          "%.3e m" % (cf["proxima_term_s"], cf["proxima_term_s"] / 60, cf["two_L_over_c_s_at_1mm"],
                      cf["threshold_m_at_1mm"]))
    print("(4) Manyfold: a 1 mm bulk gap reads %.2e s on our clock; Proxima is on our fold (seen at its light time) -- "
          "STRUCTURAL" % d["manyfold_gap_s"])
    print("(5) one plane: static RS, no shortcut; Caldwell-Langlois (single brane, infinite bulk, z = 1090): advance "
          "%.1e at l = 1/k (l H0 = %.1e), <= %.1e at their bound; branelink O7: at most %.1f ns over %.4f yr" % (
              cl["advance_z1090_at_1_over_k"], cl["lH0_at_1_over_k"], cl["advance_z1090_bound"], d["o7_max_ns"],
              d["o7_light_time_yr"]))
    print("(6) loops and (7) entering/leaving -- STRUCTURAL")


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
    g, fc, cf = d["rs"], d["flat_control"], d["cf"]
    chk("the RS null geodesic integrated in y reaches the visible brane at the conformal closed form (rel. %.1e)" %
        abs(d["rs_numeric_dt"] / g["dz"] - 1), abs(d["rs_numeric_dt"] / g["dz"] - 1) < 1e-9)
    chk("k -> 0 at fixed r_c: both clocks read pi r_c / c (ours %.4e, hidden %.4e, pi r_c/c %.4e s)" % (
        fc["ours_s"], fc["hidden_own_s"], fc["pi_rc_over_c_s"]),
        abs(fc["ours_s"] / fc["pi_rc_over_c_s"] - 1) < 1e-4 and abs(fc["hidden_own_s"] / fc["pi_rc_over_c_s"] - 1) < 1e-4,
        ctl=True)
    chk("Chung-Freese static reading reproduces their kL ~ ln(1e5) factor: h(1,2)/h(1,3) = %.6e at t_f = 1e6 L" %
        cf["static_ratio_tf_1e6L"], abs(cf["static_ratio_tf_1e6L"] / 1e5 - 1) < 1e-5)
    chk("(a positive control) in Chung-Freese's geometry no shortcut below D* = 2L/(1 - e^{-kL}), one above (%s, %s)" % (
        cf["below"], cf["above"]), (not cf["below"]) and cf["above"], ctl=True)
    structural.append("between bulk-paired points there is no curve in either plane, so a speed is undefined there -- "
                      "H-NO-SPEED holds strictly for bulk-paired points; for a destination on our own plane (Earth to "
                      "Proxima) an effective D/tau on our clock IS defined, and is <= c in static RS")
    structural.append("RS (static, flat branes, conformally flat bulk): every causal curve has dt >= |dx|, so landing "
                      "elsewhere reads at least the light time; Chung-Freese's warped hidden plane and the Manyfold's "
                      "folds are geometries where it does not")
    structural.append("loops: static RS has a global time; Chung-Freese hide their apparent causality violation today; "
                      "the Manyfold does not violate causality; Gao-Wald (NEC time delay) NAMED-NOT-READ")
    structural.append("entering and leaving: gravitational in RS (KK modes), bulk-brane vertices in Chung-Freese; no "
                      "rate for a carrier of the defining information is computed or READ here (O6)")
    for s in structural:
        print("  STRUCTURAL: " + s)
    print("bulk.py: %d/%d checks pass, %d of them controls; %d STRUCTURAL printed, not counted" % (
        n_pass, n_pass + n_fail, n_ctl, len(structural)))
    return n_fail == 0


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    elif "--json" in sys.argv:
        print(json.dumps(compute(), indent=1, default=str))
    else:
        report()
