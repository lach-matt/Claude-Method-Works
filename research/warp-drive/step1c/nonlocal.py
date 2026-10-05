#!/usr/bin/env python3
"""
nonlocal.py -- Step 1c: the non-local branch of the coupling route, taken as M's hypothesis.

Not seated.  M (rulings item 39): "3, then 2. Then 1 last please" -- 3 first: revisit H-LOCALITY, i.e. take the
non-local branch as M's hypothesis: what an instantaneous coupling would have to be, what it contradicts on the board,
and what measurement would test it.  coupling.py found that locality bounds the transfer TIME: an instantaneous
coupling across spacelike L signals at every J > 0 and is excluded under H-LOCALITY.  This file drops H-LOCALITY and
carries the alternative as a hypothesis, never as a result and never dismissed.

    python3 nonlocal.py              report
    python3 nonlocal.py --selftest   checks, with CONTROLS
    python3 nonlocal.py --json       the numbers as JSON

THE HYPOTHESIS
  H-NONLOCAL-COUPLING  an instantaneous (non-retarded) term H_AB = J (|A><B| + |B><A|) between qubits at A and B,
                       spacelike separated by L -- wave 3's H-DIRECT-COUPLING with H-LOCALITY dropped.  It is LINEAR
                       quantum mechanics with a non-local Hamiltonian; it is not H-SETTLE (docket68/settle.py:
                       nonlinear, local), which is the board's other signalling branch.
WHAT IT WOULD HAVE TO BE (each computed or asked of an owner)
  (1) A channel at any J: B's probability sin^2(J t) (coupling.instantaneous_signal).
  (2) Keyed to ONE frame, or it closes causal loops: two instantaneous couplings simultaneous in different frames
      contain a closed causal curve; any number keyed to one frame contain none (latticectc.py's theorem, asked with
      its own witnesses E1, E2 -- the computation behind corridors.py; carried on the board as M's H-FRAME, M-D68-C10).
  (3) For the device: I couplings, one per qubit, each spanning L (coupling.py's PARALLEL), at J = pi/(2T) -- at the
      century schedule 4.98e-10 rad/s per pair.
WHAT IT CONTRADICTS, AND WHAT IT DOES NOT
  It contradicts relativistic microcausality, which the board carries as H-LOCALITY.  It does NOT contradict
  non-relativistic linear quantum mechanics: Eldredge et al. (1612.02442v2, READ by wave 3) find transfer times
  independent of L for 1/r^alpha couplings with alpha < d, and Nachtergaele & Sims (1004.2086v1, READ by wave 3)
  call the non-relativistic locality structure approximate.  It does not contradict nosig.py, which concerns
  entanglement WITHOUT a coupling term.
WHAT MEASUREMENT WOULD TEST IT
  Bob's marginal moves by delta = sin^2(J t) while A and B stay spacelike, so t <= r/c at separation r.  Resolving a
  shift delta in a probability near 1/2 at one standard error takes N ~ 1/(4 delta^2) trials (H-SHOT-NOISE).  So the
  test's reach at separation r is delta(r) = sin^2(J r / c): it falls as r^2 for small J r/c, and the coupling the
  device needs is testable only at separations comparable to L itself.  Existing spacelike Bell tests' no-signalling
  checks are READ at source (below), and the bound each implies on J at its separation is computed:
  J <= asin(sqrt(delta_max)) c / r.

NAMED HYPOTHESES
  H-NONLOCAL-COUPLING (M's branch), H-FRAME (M-D68-C10, carried), H-SHOT-NOISE, H-SPACELIKE-WINDOW (the reach uses the
  full light time r/c; the READ tests use r/c minus their stated margin), H-J-DISTANCE-FREE (a bound measured at r
  applies at L: true of the speed-free routes wave 3 named, otherwise a test at r bounds J at r only), H-COUPLING-MAP
  (a Bell test's marginal shift is the coupling's sin^2(J t), unscaled -- reading A -- or scaled by the detection
  probability -- reading B; both printed, neither favoured), and coupling.py's and demand.py's.
"""
import contextlib
import io
import json
import math
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
WD = os.path.abspath(os.path.join(HERE, ".."))
if WD not in sys.path:
    sys.path.append(WD)


def _sibling(name, fname):
    """A step1c owner, loaded by PATH under a private name: the board's root holds its own demand.py, supply.py and
    coupling.py, so a sibling is never imported by its bare name."""
    import importlib.util as _ilu
    key = "s1c_" + name
    if key in sys.modules:
        return sys.modules[key]
    spec = _ilu.spec_from_file_location(key, os.path.join(HERE, fname))
    mod = _ilu.module_from_spec(spec)
    sys.modules[key] = mod
    spec.loader.exec_module(mod)
    return mod


with contextlib.redirect_stdout(io.StringIO()):
    coupling = _sibling("coupling", "coupling.py")
    import latticectc

C = coupling.C
L = coupling.L
YEAR_S = coupling.YEAR_S
SEPARATIONS_M = {"1.3 km (a ground-station Bell test)": 1.3e3, "Earth-Moon (3.84e8 m)": 3.844e8,
                 "1 au": 1.495978707e11, "L (4.24 ly)": None}

# The measured no-signalling checks of spacelike Bell tests, READ at source by this session's no-signalling reader
# (2026-10-05, alphaXiv answer_pdf_queries, the supplements from the arXiv ancillary files); Vienna's geometry (58 m,
# margins ~4 ns) re-read by the lead from the main text.  delta_max is the largest |marginal difference| + 2 standard
# errors over the reported setting pairs (the reader's two-proportion arithmetic from the published counts).  t is the
# setting-to-distant-measurement interval, r/c minus the stated spacelike margin (H-SPACELIKE-WINDOW).
NOSIG_TESTS = {
    "Vienna 2015, absolute (Giustina 1511.03190v2)": {
        "r_m": 58.0, "margin_s": 4e-9, "delta_max": 4.23e-6, "reading": "A: shift unscaled by detection",
        "route": "supplement Sec. VIII eq. S18 (reader); geometry main text Figs. 1-2 (lead)",
        "phrase": "pA+(a1b1) = 2.45328 x 10^-4, pA+(a1b2) = 2.45308 x 10^-4", "kind": "measured"},
    "Vienna 2015, relative to P+ = 2.45e-4": {
        "r_m": 58.0, "margin_s": 4e-9, "delta_max": 4.23e-6 / 2.45328e-4, "reading": "B: shift scaled by detection",
        "route": "as above", "phrase": "pA+(a1b1) = 2.45328 x 10^-4", "kind": "measured"},
    "NIST 2015, absolute (Shalm 1511.03189v2)": {
        "r_m": 184.9, "margin_s": 63.5e-9, "delta_max": max(abs(dd) + 2 * se for dd, se in ((1.06e-6, 3.13e-6), (3.96e-6, 5.31e-6),
                                                          (4.91e-6, 3.09e-6), (-2.03e-6, 5.53e-6))),
        "reading": "A", "route": "LHFSupplementary Table S-II, p.14 (reader); 120 p-values, smallest 0.0017",
        "phrase": "The smallest observed p-value was 0.0017", "kind": "measured"},
    "Munich 2017, Apr 15 run (Rosenfeld 1611.04604v2)": {
        "r_m": 398.0, "margin_s": 267.4e-9, "delta_max": 0.0066 + 2 * 0.0100, "reading": "P ~ 1/2 (heralded)",
        "route": "supplement Table S15 p.30 (reader)", "phrase": "no evidence to reject the no-signaling assumption",
        "kind": "measured"},
    "Munich 2017, Apr 7 run (p = 0.014)": {
        "r_m": 398.0, "margin_s": 267.4e-9, "delta_max": 0.040 + 2 * 0.016, "reading": "P ~ 1/2 (heralded)",
        "route": "supplement Table S15 p.30 (reader)", "phrase": "no evidence to reject the no-signaling assumption",
        "kind": "measured; a 2.5 sigma marginal difference the authors do not read as signalling -- recorded"},
}
NOSIG_NO_STATISTIC = {"Delft 2015 (Hensen 1508.05949v1)": "1280 m, 245 trials: the main text reports no no-signalling "
                      "statistic (the supplement was not read)"}
SPEED_BOUNDS_NOT_BEARING = {
    "Salart 2008 (0808.3316v1)": "V_QI >= 54000 c at 18 km -- an influence carrying correlations, 'not a classical "
                                 "signaling' by the paper's own account: it does not bound a coupling that signals",
    "Yin 2013 (1303.0614v2)": "V/c >= 1.38e4 at 15.3 km -- the same kind; the paper notes two-party spooky action need "
                              "not lead to superluminal communication"}


def frame_requirement():
    """latticectc's own witnesses: two corridors simultaneous in different frames close a causal curve; one alone
    does not.  (Asked: rank1_has_causal, box_has_causal.)"""
    E1, E2 = latticectc.WITNESS_E1, latticectc.WITNESS_E2
    return {"one_corridor_closes_loop": bool(latticectc.rank1_has_causal(E1)),
            "two_frames_close_loop": bool(latticectc.box_has_causal(E1, E2)),
            "same_frame_pair_closes_loop": bool(latticectc.box_has_causal(
                tuple([0] + list(E1[1:])), tuple([0] + list(E2[1:]))))}


def demand_J():
    rows = coupling.demand_rows()
    return {r["schedule"]: r["J_pair_rad_s"] for r in rows if r["count"].startswith("species")}


def test_reach(J):
    """delta(r) = sin^2(J r/c) and N ~ 1/(4 delta^2) at each separation (H-SHOT-NOISE, H-SPACELIKE-WINDOW)."""
    out = {}
    for name, r in SEPARATIONS_M.items():
        r = L if r is None else r
        d = math.sin(J * r / C) ** 2
        out[name] = {"r_m": r, "delta": d, "trials_1sigma": (1.0 / (4.0 * d * d)) if d > 0 else float("inf")}
    return out


def J_bound(delta_max, r, margin_s=0.0):
    """The largest instantaneous J a test at separation r (interval t = r/c - margin) with marginal shift <= delta_max
    allows: sin^2(J t) <= delta_max.  Under H-J-DISTANCE-FREE it bounds J at L too; otherwise it bounds J at r only."""
    return math.asin(math.sqrt(delta_max)) / (r / C - margin_s)


def collect():
    dj = demand_J()
    return {"frame": frame_requirement(), "demand_J": dj,
            "reach_century": test_reach(dj["1 century"]), "reach_1yr": test_reach(dj["1 yr"]),
            "nosig_tests": NOSIG_TESTS,
            "nosig_bounds": dict((k, J_bound(v["delta_max"], v["r_m"], v["margin_s"])) for k, v in NOSIG_TESTS.items()),
            "no_statistic": NOSIG_NO_STATISTIC, "speed_bounds_not_bearing": SPEED_BOUNDS_NOT_BEARING}


def report():
    d = collect()
    f = d["frame"]
    print("Step 1c -- the non-local branch, H-NONLOCAL-COUPLING (M's hypothesis; H-LOCALITY dropped)")
    print("  frame (latticectc, asked): one corridor closes a loop %s; two keyed to different frames %s; two keyed to "
          "one frame %s -> H-FRAME is required" % (f["one_corridor_closes_loop"], f["two_frames_close_loop"],
                                                  f["same_frame_pair_closes_loop"]))
    print("  demand per pair: %s" % "; ".join("%s %.3g rad/s" % kv for kv in d["demand_J"].items()))
    for lbl, key in (("century", "reach_century"), ("1 yr", "reach_1yr")):
        print("  test reach at the %s J (delta = sin^2(J r/c); trials ~ 1/(4 delta^2)):" % lbl)
        for name, v in d[key].items():
            print("    %-38s delta %.3g, trials %.3g" % (name, v["delta"], v["trials_1sigma"]))
    if d["nosig_tests"]:
        print("  existing spacelike no-signalling checks (READ) and the J each allows:")
        for k, v in d["nosig_tests"].items():
            print("    %-48s r %.4g m, delta_max %.3g -> J <= %.3g rad/s" % (k, v["r_m"], v["delta_max"],
                                                                       d["nosig_bounds"][k]))
        lo = min(d["nosig_bounds"].values())
        print("  the tightest allows J <= %.3g rad/s: %.2g times the 1 day demand per pair and %.2g times the century's "
              "-- present tests do not exclude H-NONLOCAL-COUPLING at the strength the device needs (H-J-DISTANCE-FREE)"
              % (lo, lo / d["demand_J"]["1 day"], lo / d["demand_J"]["1 century"]))
        for k, v in d["no_statistic"].items():
            print("    no statistic: %s -- %s" % (k, v))
        for k, v in d["speed_bounds_not_bearing"].items():
            print("    not bearing: %s -- %s" % (k, v))


def selftest():
    n_ok = n_bad = n_ctl = 0

    def chk(label, got, want, ctl=False):
        nonlocal n_ok, n_bad, n_ctl
        ok = got == want
        n_ok += ok
        n_bad += not ok
        n_ctl += ctl
        print("  [%s]%s %-96s %r" % ("ok" if ok else "XX", " CTL" if ctl else "", label[:96], got))

    print("nonlocal.py selftest")
    d = collect()
    f = d["frame"]
    chk("H-FRAME is required, asked of latticectc's theorem: two instantaneous couplings keyed to different frames "
        "close a causal loop; one alone, or two keyed to one frame, do not",
        (f["one_corridor_closes_loop"], f["two_frames_close_loop"], f["same_frame_pair_closes_loop"]),
        (False, True, False))
    rc = d["reach_century"]
    chk("test reach at the century J: at L the shift is over 1e-3 (%.3g; ~%.3g trials), at Earth-Moon under 1e-15 "
        "(%.3g; ~%.3g trials)" % (rc["L (4.24 ly)"]["delta"], rc["L (4.24 ly)"]["trials_1sigma"],
                                  rc["Earth-Moon (3.84e8 m)"]["delta"], rc["Earth-Moon (3.84e8 m)"]["trials_1sigma"]),
        (rc["L (4.24 ly)"]["delta"] > 1e-3, rc["Earth-Moon (3.84e8 m)"]["delta"] < 1e-15), (True, True))
    b = d["nosig_bounds"]
    lo = min(b.values())
    chk("every READ no-signalling test allows a J over 1e8 times the 1 day demand per pair (tightest %.3g rad/s, "
        "%.2g x): present tests do not exclude the device's coupling under H-J-DISTANCE-FREE"
        % (lo, lo / d["demand_J"]["1 day"]), lo / d["demand_J"]["1 day"] > 1e8, True)
    chk("  CONTROL: a test AT the device's span (r = L) resolving 1e-3 would exclude the century J (bound %.3g < %.3g)"
        % (J_bound(1e-3, L), d["demand_J"]["1 century"]), J_bound(1e-3, L) < d["demand_J"]["1 century"], True,
        ctl=True)
    chk("every READ test names its route and phrase; phrases under 15 words",
        ([k for k, v in NOSIG_TESTS.items() if not (v.get("route") and v.get("phrase"))],
         [k for k, v in NOSIG_TESTS.items() if len(v["phrase"].split()) >= 15]), ([], []))
    print("  [STRUCTURAL] the reach delta(r) = sin^2(J r/c) falls as r^2 for J r/c << 1, so trials ~ r^-4")
    print("  [STRUCTURAL] J_bound inverts sin^2(J t) <= delta_max; delta_max = 0 gives J = 0")
    print("  [STRUCTURAL] Vienna's readings A and B differ by 1/P+ in delta, so by about sqrt(1/P+) = 64x in J")
    print("\nHISTORY: the last two were first counted (one as a CONTROL); identities of the formula, moved here.")
    print("\n%d/%d checks pass, %d of them controls; 4 STRUCTURAL printed, not counted" % (n_ok, n_ok + n_bad, n_ctl))
    return n_bad == 0


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    elif "--json" in sys.argv:
        print(json.dumps(collect(), indent=1, default=str))
    else:
        report()
