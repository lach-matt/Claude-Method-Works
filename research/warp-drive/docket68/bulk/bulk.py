#!/usr/bin/env python3
"""
bulk.py -- H-HIGHER-CORRIDOR and H-NO-SPEED: two planes joined through a higher dimension, with no speed anywhere.

Not seated; not yet verified.  M (rulings item 57): "If two points, each on a different spacetime plane, are connected
by a corridor through a higher dimension, then speed cannot exist in the dimension below the corridor as you are at
position 1 then position 2, with no in between, which means no travel, no speed".  M (item 58): "3, then 2, then 1
please" -- the case fixed as two separate planes, then READ, then modelled.  Carried as M's hypotheses H-NO-SPEED and
H-HIGHER-CORRIDOR, never as results.  O9 stays OPEN.

    python3 bulk.py              report
    python3 bulk.py --selftest   checks, with CONTROLS
    python3 bulk.py --json       the numbers as JSON

THE CASE (item 58's step 3): TWO PLANES, NOT ONE
  Two separate 4D worlds (branes), each its own spacetime plane, joined only through a fifth dimension.  The READ model
  that is exactly this is Randall & Sundrum's two-brane set-up (hep-ph/9905221v1, READ via alphaXiv 2026-10-05):
  ds^2 = e^{-2 k r_c |phi|} eta dx dx + r_c^2 dphi^2 (eq. 12, printed p.4), two 3-branes at the orbifold fixed points
  phi = 0 ('hidden') and phi = pi ('visible'), the space between them 'a slice of an AdS5 geometry' (p.3), tensions
  V_hid = -V_vis = 24 M^3 k (eq. 11); a mass parameter m0 on the visible brane is seen as m = e^{-k r_c pi} m0 (eq. 21),
  and 'If e^{k r_c pi} is of order 10^15' this gives TeV scales (printed p.6).  Ordinary fields live on a brane; gravity
  lives in the bulk.  Its KK gravitons couple to visible-brane matter at 'Energy/TeV' (printed p.6), not Planck strength.
  DISCREPANCY: the same page, as extracted, prints 'kr_c [symbol lost] 50'; e^{k r_c pi} = 1e15 gives k r_c = 11.0.  The
  board uses the warp factor the paper states and computes k r_c from it (H-RS1-WARP).

WHAT THE SOURCES SAY ABOUT SHORTCUTS (READ via alphaXiv)
  * Chung & Freese (hep-ph/9906542v2 p.13): two regions that seem causally disconnected 'might in fact have talked to
    each other because of a geodesic between them that went off our brane, into the bulk, and then back onto our brane'.
  * Caldwell & Langlois (gr-qc/0103070v1): a bulk graviton between two brane points can 'appear quicker than a photon'
    (abstract); for a static brane (strict Randall-Sundrum) or de Sitter 'the photon horizon and the bulk gravitational
    horizon would be exactly identical' (p.5); 'there is no shortcut for compact, flat extra dimensions' (p.8); today
    r_g/r_gamma ~ 1 + (1/10)(l H0)^2 (1+z)^{5/2} with l H0 <~ 1e-29 (eq. 22, p.6).
  * The board's own one-plane case (D13, O7, branelink.py): bulk null geodesics join brane points the induced metric
    calls spacelike; the computed saving over the Proxima span is asked of branelink.o7_exact().

WHAT IS COMPUTED (no speed anywhere: only each end's own clock, H-LOCAL-CLOCK)
  (1) The jump between the planes.  In conformal coordinates z = e^{k y}/k the metric is (k z)^{-2}(eta dx dx + dz^2), so
      null curves are straight lines: a bulk-paired point (same x) on the hidden brane (z_h = 1/k) and on the visible
      brane (z_v = e^{k pi r_c}/k) are joined at coordinate interval dz = z_v - z_h.  Each end's clock reads its own
      proper time: tau_hidden = dz (its induced metric is eta), tau_visible = e^{-k pi r_c} dz.  Checked by integrating
      the null geodesic in the y-coordinate numerically, against the closed form.  There is no path in either plane
      between the two events: within each plane, speed is UNDEFINED, not small (H-NO-SPEED's precise sense).
  (2) A jump that also lands somewhere else: a lateral offset D (visible proper length) adds e^{k pi r_c} D to the
      coordinate offset; the visible clock then reads sqrt((1/k)^2 + D^2)/c -- at least the light time of D.
  (3) One plane, two places (the board's present case): from the visible brane into the bulk and back, the coordinate
      interval is sqrt((2 dz')^2 + dx^2) >= dx for every depth -- no shortcut in static RS (Caldwell-Langlois p.5);
      the expanding-brane advance today (Caldwell-Langlois eq. 22) and the moving-brane saving (branelink, O7).
  (4) Loops: the static two-brane metric has a global time function (the coordinate t), so no closed causal curve; the
      board's lattice theorem D21 covers the moving-brane quotient.  STRUCTURAL.
  (5) Entering and leaving (O6): in RS ordinary matter is confined to its brane; what crosses is gravitational (bulk
      gravitons, KK modes coupled at Energy/TeV on the visible brane).  On M's ruling (M-D68-1) what crosses is the
      defining information.  STRUCTURAL.

NAMED HYPOTHESES
  H-RS1 (the two planes are Randall-Sundrum's two branes, static, the bulk empty), H-RS1-WARP (e^{k pi r_c} = 1e15),
  H-K-PLANCK (k = the reduced Planck mass 2e18 GeV, RS p.1's M_Pl; RS give k 'of order the Planck scale', k < M),
  H-BULK-PAIRING (which point of one plane is 'the same place' as a point of the other is fixed by the bulk geometry's
  shared x, not by either plane), H-GRAVITATIONAL-CARRIER; with M's H-NO-SPEED, H-HIGHER-CORRIDOR and H-LOCAL-CLOCK.
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
sys.path.insert(0, WD)                                # branelink imports its peers by name
try:
    with contextlib.redirect_stdout(io.StringIO()):
        branelink = _by_path("wd_branelink", os.path.join(WD, "branelink.py"))
finally:
    sys.path[:] = _saved_path

C = branelink.C
HBARC_GEV_M = branelink.HBARC_GEV_M
L_PROXIMA = branelink.L_PROXIMA
YEAR_S = 365.25 * 86400.0
RS = {"warp": 1e15, "M_Pl_GeV": 2e18,
      "source": "Randall & Sundrum hep-ph/9905221v1: eq. 12 p.4, eq. 11, eq. 21, 'of order 10^15' p.6, M_Pl = 2e18 GeV "
                "p.1; READ via alphaXiv 2026-10-05"}
CL = {"lH0_max": 1e-29, "source": "Caldwell & Langlois gr-qc/0103070v1 eq. 22 p.6 ('l H0 <~ 1e-29'); READ via alphaXiv"}


def geometry(warp=RS["warp"], k_gev=RS["M_Pl_GeV"]):
    kpr = math.log(warp)                          # k pi r_c
    inv_k_m = HBARC_GEV_M / k_gev                 # 1/k as a length
    return {"k_pi_rc": kpr, "k_rc": kpr / math.pi, "inv_k_m": inv_k_m, "inv_k_s": inv_k_m / C,
            "z_h": 1.0, "z_v": math.exp(kpr), "dz": math.exp(kpr) - 1.0}   # z in units of 1/k


def null_geodesic_numeric(kpr, p_over_e=0.0, n=200000):
    """Integrate the null geodesic from y = 0 (hidden) to k y = kpr (visible) in the y-coordinate: with conserved E, P,
    dt/dy = E e^{ky}/sqrt(E^2-P^2) and dx/dy = P e^{ky}/sqrt(E^2-P^2) (units of 1/k).  Simpson's rule."""
    s = 1.0 / math.sqrt(1.0 - p_over_e ** 2)
    h = kpr / n
    acc = 0.0
    for i in range(n + 1):
        w = 1 if i in (0, n) else (4 if i % 2 else 2)
        acc += w * math.exp(i * h)
    integral = acc * h / 3
    return {"dt": s * integral, "dx": s * p_over_e * integral}


def jump(g, lateral_m=0.0):
    """The hidden-to-visible jump with a lateral offset (visible proper length); each end's clock, in seconds."""
    dx = math.exp(g["k_pi_rc"]) * lateral_m / g["inv_k_m"]           # coordinate offset, units of 1/k
    dt = math.sqrt(g["dz"] ** 2 + dx ** 2)
    return {"tau_hidden_s": dt * g["inv_k_s"], "tau_visible_s": math.exp(-g["k_pi_rc"]) * dt * g["inv_k_s"],
            "light_time_of_offset_s": lateral_m / C}


def one_plane(g, offsets_m=(1.0, 1.0e3, L_PROXIMA)):
    """Visible brane, two places: into the bulk to depth dz' and back costs sqrt((2 dz')^2 + dx^2) >= dx."""
    rows = []
    for D in offsets_m:
        dx = math.exp(g["k_pi_rc"]) * D / g["inv_k_m"]
        # sqrt(a^2 + b^2) - b written as a^2/(sqrt(a^2 + b^2) + b), stable when b >> a (first written as the
        # difference, which cancels to 0.0 in double precision at the Proxima offset; depth 0, the brane path itself,
        # was also in the list, so the minimum was 0 by construction)
        worst = min((2 * dd) ** 2 / (math.sqrt((2 * dd) ** 2 + dx ** 2) + dx) for dd in (0.25 * g["dz"], g["dz"]))
        rows.append({"D_m": D, "bulk_minus_brane_coord": worst, "shortcut": worst < 0})
    return rows


def compute():
    g = geometry()
    num = null_geodesic_numeric(g["k_pi_rc"])
    num_lat = null_geodesic_numeric(g["k_pi_rc"], p_over_e=0.6)
    with contextlib.redirect_stdout(io.StringIO()):
        o7 = branelink.o7_exact()
    # control: nearly unwarped (e^{k pi r_c} = 1 + 1e-9) through the same functions -- the two clocks agree
    gf = geometry(warp=1.0 + 1e-9)
    jf = jump(gf)
    flat = {"clock_ratio": jf["tau_hidden_s"] / jf["tau_visible_s"]}
    return {"geometry": g, "numeric_dt": num["dt"], "numeric_lateral": num_lat,
            "jump_same_place": jump(g), "jump_to_proxima_offset": jump(g, L_PROXIMA),
            "one_plane": one_plane(g),
            "cl_advance_today": 0.1 * CL["lH0_max"] ** 2, "cl_advance_z1090": 0.1 * CL["lH0_max"] ** 2 * 1091 ** 2.5,
            "o7_saving_ns": float(o7["Delta_tau ns"]), "o7_light_time_yr": float(o7["Proxima light time yr"]),
            "flat_control_clock_ratio": flat["clock_ratio"]}


def report():
    d = compute()
    g, js, jp = d["geometry"], d["jump_same_place"], d["jump_to_proxima_offset"]
    print("H-HIGHER-CORRIDOR: two planes joined through a fifth dimension (not verified; not seated)\n")
    print("(1) Randall-Sundrum's two branes: k pi r_c = %.3f (k r_c = %.2f) from e^{k pi r_c} = %.0e; 1/k = %.3e m = "
          "%.3e s at k = %.0e GeV" % (g["k_pi_rc"], g["k_rc"], RS["warp"], g["inv_k_m"], g["inv_k_s"], RS["M_Pl_GeV"]))
    print("    the jump between bulk-paired points: no path in either plane, so no speed in either; each end's clock "
          "reads: hidden %.3e s, visible %.3e s (numerical geodesic %.6e vs closed form %.6e, units 1/k)" % (
              js["tau_hidden_s"], js["tau_visible_s"], d["numeric_dt"], g["dz"]))
    print("(2) landing at a lateral offset of the Proxima span: the visible clock reads %.6f yr (the light time %.6f yr)"
          % (jp["tau_visible_s"] / YEAR_S, jp["light_time_of_offset_s"] / YEAR_S))
    print("(3) one plane, two places: into the bulk and back is never shorter in static RS: " + ", ".join(
        "D %.3g m: bulk - brane %+.3g (coordinate, units of 1/k)" % (r["D_m"], r["bulk_minus_brane_coord"]) for r in d["one_plane"]))
    print("    expanding brane (Caldwell-Langlois eq. 22): advance %.1e today, %.1e from z = 1090; moving brane "
          "(branelink O7): %.1f ns saved over %.4f yr" % (d["cl_advance_today"], d["cl_advance_z1090"],
                                                          d["o7_saving_ns"], d["o7_light_time_yr"]))
    print("(4) loops: the static two-brane metric has a global time -- STRUCTURAL; (5) what crosses is gravitational -- "
          "STRUCTURAL")


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
    g = d["geometry"]
    chk("the null geodesic integrated in y reaches the visible brane at the conformal closed form dz (rel. %.1e)" %
        abs(d["numeric_dt"] / g["dz"] - 1), abs(d["numeric_dt"] / g["dz"] - 1) < 1e-9)
    nl = d["numeric_lateral"]
    chk("with lateral momentum the integrated geodesic satisfies dt^2 - dx^2 = dz^2 (rel. %.1e)" %
        abs((nl["dt"] ** 2 - nl["dx"] ** 2) / g["dz"] ** 2 - 1), abs((nl["dt"] ** 2 - nl["dx"] ** 2) / g["dz"] ** 2 - 1)
        < 1e-9)
    chk("a nearly unwarped fifth dimension (warp 1 + 1e-9), through the same functions, gives the two clocks equal "
        "(ratio %.12f): the 1e15 split is the warping's" % d["flat_control_clock_ratio"],
        abs(d["flat_control_clock_ratio"] - 1) < 1e-8, ctl=True)
    chk("the two clocks differ by exactly the warp factor e^{k pi r_c} = 1e15 (%.6e)" % (
        d["jump_same_place"]["tau_hidden_s"] / d["jump_same_place"]["tau_visible_s"]),
        abs(d["jump_same_place"]["tau_hidden_s"] / d["jump_same_place"]["tau_visible_s"] / RS["warp"] - 1) < 1e-12)
    chk("landing at a lateral offset reads at least the offset's light time on the visible clock",
        d["jump_to_proxima_offset"]["tau_visible_s"] >= d["jump_to_proxima_offset"]["light_time_of_offset_s"])
    chk("one plane, static RS: no bulk detour is shorter than the brane path, at every offset tried (Caldwell-Langlois "
        "p.5)", not any(r["shortcut"] for r in d["one_plane"]))
    structural.append("within each plane there is no curve joining the two events, so a speed (length over time along "
                      "a path in the plane) is undefined -- H-NO-SPEED's precise sense; what remains is each end's own "
                      "clock reading (H-LOCAL-CLOCK)")
    structural.append("the static two-brane metric has the global time function t: no closed causal curve; the moving-"
                      "brane quotient is D21's")
    structural.append("in RS ordinary fields are confined to a brane; what crosses the bulk is gravitational (KK modes "
                      "at Energy/TeV on the visible brane): O6, OPEN")
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
