#!/usr/bin/env python3
"""
nonlocal.py -- Step 1c: the non-local branch of the coupling route, taken as M's hypothesis.

Not seated.  M (rulings item 39): "3, then 2. Then 1 last please" -- 3 first: revisit H-LOCALITY, i.e. take the
non-local branch as M's hypothesis: what an instantaneous coupling would have to be, what it contradicts on the board,
and what measurement would test it.  coupling.py found that locality bounds the transfer TIME: an instantaneous
coupling across spacelike L signals at every J > 0 and is excluded under H-LOCALITY.  This file drops H-LOCALITY and
carries the alternative as a hypothesis, never as a result and never dismissed.  Verified in both directions on
2026-10-05; the findings are applied and the first-written claims kept under HISTORY.

    python3 nonlocal.py              report
    python3 nonlocal.py --selftest   checks, with CONTROLS
    python3 nonlocal.py --json       the numbers as JSON

THE HYPOTHESIS
  H-NONLOCAL-COUPLING  an instantaneous (non-retarded) term H_AB = J (|A><B| + |B><A|) between qubits at A and B,
                       spacelike separated by L -- wave 3's H-DIRECT-COUPLING with H-LOCALITY dropped.  LINEAR quantum
                       mechanics with a non-local Hamiltonian; not H-SETTLE (docket68/settle.py: nonlinear, local), the
                       board's other signalling branch.
WHAT IT WOULD HAVE TO BE
  (1) A channel at any J: B's probability sin^2(J t) from |1_A 0_B> (coupling.instantaneous_signal).
  (2) Free of causal loops: under latticectc.py's hypotheses H1-H3, with each coupling carried as a translation
      identification of the two positions (H-CORRIDOR-MAP: a localized two-qubit link treated as a global
      identification acting freely; localized links close a loop only for suitable positions), two couplings with
      spacelike separation vectors close a causal loop IFF their span is timelike -- i.e. iff no single frame makes
      both simultaneous.  Asked of latticectc: its witnesses E1, E2 (timelike span) close one; the pair
      (0.1, 1, 0, 0), (0.1, 0, 1, 0) (spacelike span: a common simultaneity frame exists) does not.  So loop-freedom
      needs every coupling simultaneous in one common frame: M's H-FRAME (M-D68-C10, carried), as corridors.py found.
  (3) For the device: I couplings, one per qubit, each spanning L, at J = pi/(2T) per pair.
WHAT IT CONTRADICTS, AND WHAT IT DOES NOT
  It contradicts relativistic microcausality (H-LOCALITY).  It does not contradict non-relativistic linear quantum
  mechanics, which routinely carries instantaneous terms (the Coulomb term) -- but those are approximations of a
  retarded field theory, so the non-contradiction carries NO evidential weight for the hypothesis.  It does not
  contradict nosig.py, which concerns entanglement without a coupling term.
WHAT MEASUREMENT WOULD TEST IT
  Two protocols, two maps (each named):
    SPACELIKE (H-SPACELIKE-WINDOW): A and B stay spacelike, t <= r/c -- the test also excludes ordinary signals.
    TIMELIKE  (H-J-DISTANCE-FREE with crosstalk controlled): any duration -- at the day J a full transfer in one day at
              any separation.  It needs every retarded channel shut out, which is the protocol's own burden.
    SECOND-ORDER map: delta = sin^2(J t) (population transfer).  FIRST-ORDER map (reading C): delta ~ J t, when Alice's
              side carries coherence the coupling can turn into a marginal shift.
  Resolving a difference delta between two settings near 1/2 at 2 standard errors takes about 4/delta^2 trials (a
  two-proportion comparison; H-SHOT-NOISE).
WHAT PRESENT TESTS ALLOW (READ; every bound CONDITIONAL)
  The measured no-signalling checks of spacelike Bell tests bound J at their separation, J <= asin(sqrt(delta_max))/t
  (readings A, B) or delta_max/(2t) (reading C), with t = r/c minus the stated margin.  Conditions, each named:
  H-COUPLING-MAP (which map), H-SETTING-DEPENDENCE (the coupling's effect on Bob must depend on Alice's SETTING; if her
  photon is present under both settings the test bounds nothing), H-UNIVERSAL-COUPLING (the Bell-test systems carry
  the device's coupling at all), H-LAB-FRAME (the preferred frame moves slower than c^2 t / r relative to the lab, or
  Alice's setting does not precede Bob's measurement there), and H-J-DISTANCE-FREE (a bound at r applies at L).  If
  instead J falls as r^-alpha, the tightest bound carried to L excludes the device's coupling above an alpha printed
  here.  Whether the speed-free routes wave 3 named make J distance-free is OPEN: Eldredge et al.'s L-independence is a
  collective many-site effect, not a distance-free pairwise J.
SPEED-OF-INFLUENCE BOUNDS
  Salart 2008 (>= 5.4e4 c) and Yin 2013 (>= 1.38e4 c) bound the speed of an influence carrying correlations.  Bancal et
  al. (1110.3795, READ by the non-local verifier) show any finite-speed such model, c < v < infinity, predicts
  superluminal signalling (four parties, a privileged frame).  The decisive reason these bounds do not exclude
  H-NONLOCAL-COUPLING is that a LOWER bound on v cannot exclude v = infinity in a preferred frame; Bancal names the CMB
  frame as natural and finds no evidence ruling a privileged frame out -- which supports carrying H-FRAME.

NAMED HYPOTHESES
  H-NONLOCAL-COUPLING (M's branch), H-FRAME, H-CORRIDOR-MAP, H-SPACELIKE-WINDOW, H-J-DISTANCE-FREE, H-COUPLING-MAP,
  H-SETTING-DEPENDENCE, H-UNIVERSAL-COUPLING, H-LAB-FRAME, H-SHOT-NOISE, and coupling.py's and demand.py's.

HISTORY (non-local verifier, 2026-10-05; first-written claims kept):
  * 'Two couplings keyed to different frames close a causal loop' -- too broad: a spacelike-span pair keyed to
    different frames closes none; the true statement is loop iff timelike span (no common simultaneity frame), under
    latticectc's H1-H3 and the now-named H-CORRIDOR-MAP.
  * 'The coupling the device needs is testable only at separations comparable to L' -- holds only for the spacelike
    protocol under the second-order map; a timelike test under H-J-DISTANCE-FREE works at any separation, and the
    first-order map scales trials as r^-2, not r^-4.
  * Trials were 1/(4 delta^2) (one-sample, 1 SE); the bounds use a two-setting 2 SE comparison, 4/delta^2.
  * The bounds were stated without H-SETTING-DEPENDENCE, H-UNIVERSAL-COUPLING, H-LAB-FRAME or reading C; under reading
    C the tightest is 7.2e5 x the day demand, not 3.8e8 (the first check's 1e8 threshold would have failed there).
  * 'True of the speed-free routes wave 3 named' (H-J-DISTANCE-FREE) -- unsupported; now OPEN, with the falloff alpha
    that flips the conclusion printed.
  * NIST's margin: 63.5 ns is the 1-pulse aggregate's; the 5-pulse aggregate's is 38.3 ns, and which aggregate Table
    S-II is was not established (OPEN): both bounds printed (6.90e3, 6.60e3 rad/s).
  * The speed bounds were set aside as 'not signalling by the papers' own account'; Bancal et al. undercut that, and
    the reason is restated.
  * Counted as checks: two identities in the frame check; a CONTROL equivalent to the reach check; '4 STRUCTURAL' over
    three lines.  Moved to STRUCTURAL or corrected.
"""
import contextlib
import io
import json
import math
import os
import sys
from fractions import Fraction

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
SPAN_PAIR_NO_LOOP = ((Fraction(1, 10), Fraction(1), Fraction(0), Fraction(0)),
                     (Fraction(1, 10), Fraction(0), Fraction(1), Fraction(0)))
_NIST_PAIRS = ((1.06e-6, 3.13e-6), (3.96e-6, 5.31e-6), (4.91e-6, 3.09e-6), (-2.03e-6, 5.53e-6))

# The measured no-signalling checks of spacelike Bell tests, READ at source by this session's no-signalling reader
# (2026-10-05, alphaXiv answer_pdf_queries, the supplements from the arXiv ancillary files); Vienna's geometry (58 m,
# margins ~4 ns) re-read by the lead from the main text; NIST's 184.9 m and 63.5 ns (1-pulse) re-read by the verifier
# from the main text.  delta_max = the largest |marginal difference| + 2 standard errors over the reported setting
# pairs (the reader's two-proportion arithmetic from the published counts).
NOSIG_TESTS = {
    "Vienna 2015, reading A (Giustina 1511.03190v2)": {
        "r_m": 58.0, "margin_s": 4e-9, "delta_max": 4.23e-6, "reading": "A",
        "route": "supplement Sec. VIII eq. S18 (reader); geometry main text Figs. 1-2 (lead)",
        "phrase": "pA+(a1b1) = 2.45328 x 10^-4, pA+(a1b2) = 2.45308 x 10^-4", "kind": "measured"},
    "Vienna 2015, reading B (scaled by P+ = 2.45e-4)": {
        "r_m": 58.0, "margin_s": 4e-9, "delta_max": 4.23e-6 / 2.45328e-4, "reading": "B",
        "route": "as above", "phrase": "pA+(a1b1) = 2.45328 x 10^-4", "kind": "measured"},
    "NIST 2015, 1-pulse margin (Shalm 1511.03189v2)": {
        "r_m": 184.9, "margin_s": 63.5e-9, "delta_max": max(abs(dd) + 2 * se for dd, se in _NIST_PAIRS),
        "reading": "A", "route": "LHFSupplementary Table S-II, p.14 (reader); geometry main text (verifier)",
        "phrase": "The smallest observed p-value was 0.0017", "kind": "measured; which aggregate: OPEN"},
    "NIST 2015, 5-pulse margin": {
        "r_m": 184.9, "margin_s": 38.3e-9, "delta_max": max(abs(dd) + 2 * se for dd, se in _NIST_PAIRS),
        "reading": "A", "route": "as above; margin Table I p.8 (reader)", "phrase": "38.3 +- 3.7 ns",
        "kind": "measured; which aggregate: OPEN"},
    "Munich 2017, Apr 15 run (Rosenfeld 1611.04604v2)": {
        "r_m": 398.0, "margin_s": 267.4e-9, "delta_max": 0.0066 + 2 * 0.0100, "reading": "A (P ~ 1/2, heralded)",
        "route": "supplement Table S15 p.30 (reader)", "phrase": "no evidence to reject the no-signaling assumption",
        "kind": "measured; whether the per-run maximum: OPEN"},
    "Munich 2017, Apr 7 run (p = 0.014)": {
        "r_m": 398.0, "margin_s": 267.4e-9, "delta_max": 0.040 + 2 * 0.016, "reading": "A (P ~ 1/2, heralded)",
        "route": "supplement Table S15 p.30 (reader)", "phrase": "no evidence to reject the no-signaling assumption",
        "kind": "measured; a 2.5 sigma marginal difference the authors do not read as signalling -- recorded"},
}
NOSIG_NO_STATISTIC = {"Delft 2015 (Hensen 1508.05949v1)": "1280 m, 245 trials: the main text reports no no-signalling "
                      "statistic (the supplement was not read)"}
SPEED_BOUNDS = {
    "Salart 2008 (0808.3316v1)": "V_QI >= 54000 c at 18 km: a lower bound on the speed of an influence carrying "
                                 "correlations",
    "Yin 2013 (1303.0614v2)": "V/c >= 1.38e4 at 15.3 km: the same kind",
    "Bancal 2012 (1110.3795)": "any finite-speed model (c < v < infinity) reproducing quantum correlations predicts "
                               "superluminal signalling (four parties, privileged frame); names the CMB frame; READ by "
                               "the non-local verifier"}


def frame_requirement():
    """latticectc, asked: the witnesses E1, E2 (timelike span) close a causal loop; the pair SPAN_PAIR_NO_LOOP
    (spacelike span) does not -- loop iff no common simultaneity frame (rank 2, latticectc H1-H3, H-CORRIDOR-MAP)."""
    E1, E2 = latticectc.WITNESS_E1, latticectc.WITNESS_E2
    a, b = SPAN_PAIR_NO_LOOP
    return {"witness_span": latticectc.span_kind(E1, E2), "witness_loop": bool(latticectc.box_has_causal(E1, E2)),
            "pair_span": latticectc.span_kind(a, b), "pair_loop": bool(latticectc.box_has_causal(a, b))}


def demand_J():
    rows = coupling.demand_rows()
    return {r["schedule"]: r["J_pair_rad_s"] for r in rows if r["count"].startswith("species")}


def trials_2se(delta):
    """Two settings compared near p = 1/2 at 2 standard errors: n per arm >= 2/delta^2, so 4/delta^2 in all."""
    return 4.0 / (delta * delta) if delta > 0 else float("inf")


def test_reach(J):
    """Spacelike protocol (t = r/c): delta under the second-order map sin^2(J t) and the first-order map J t."""
    out = {}
    for name, r in SEPARATIONS_M.items():
        r = L if r is None else r
        t = r / C
        d2, d1 = math.sin(J * t) ** 2, min(1.0, J * t)
        out[name] = {"r_m": r, "delta_2nd": d2, "trials_2nd": trials_2se(d2), "delta_1st": d1,
                     "trials_1st": trials_2se(d1)}
    return out


def J_bound(delta_max, r, margin_s=0.0, reading="A"):
    """The largest instantaneous J a test allows: sin^2(J t) <= delta_max (readings A, B) or J t <= delta_max/2
    (reading C, first order), t = r/c - margin."""
    t = r / C - margin_s
    if reading == "C":
        return delta_max / (2.0 * t)
    return math.asin(math.sqrt(delta_max)) / t


def lab_frame_limit(r, margin_s):
    """H-LAB-FRAME: Alice's setting precedes Bob's measurement in a frame moving along the axis at v only for
    v/c < c t / r."""
    return C * (r / C - margin_s) / r


def falloff_alpha(J_bound_r, r, J_need):
    """If J falls as r^-alpha, the bound at r carried to L excludes J_need for alpha above this."""
    return math.log(J_need / J_bound_r) / math.log(r / L)


def bounds():
    out = {}
    for k, v in NOSIG_TESTS.items():
        out[k] = {"A_or_B": J_bound(v["delta_max"], v["r_m"], v["margin_s"]),
                  "C": J_bound(v["delta_max"], v["r_m"], v["margin_s"], "C"),
                  "lab_frame_v_over_c": lab_frame_limit(v["r_m"], v["margin_s"])}
    return out


def collect():
    dj = demand_J()
    b = bounds()
    tight_key = min(b, key=lambda k: b[k]["A_or_B"])
    tight = b[tight_key]["A_or_B"]
    tight_C = min(v["C"] for v in b.values())
    r_t = NOSIG_TESTS[tight_key]["r_m"]
    return {"frame": frame_requirement(), "demand_J": dj,
            "reach_century": test_reach(dj["1 century"]), "reach_1yr": test_reach(dj["1 yr"]),
            "nosig_bounds": b, "tightest": (tight_key, tight), "tightest_C": tight_C,
            "falloff_alpha": {"1 day": falloff_alpha(tight, r_t, dj["1 day"]),
                              "1 century": falloff_alpha(tight, r_t, dj["1 century"])},
            "no_statistic": NOSIG_NO_STATISTIC, "speed_bounds": SPEED_BOUNDS}


def report():
    d = collect()
    f = d["frame"]
    print("Step 1c -- the non-local branch, H-NONLOCAL-COUPLING (M's hypothesis; H-LOCALITY dropped)")
    print("  loops (latticectc, H1-H3, H-CORRIDOR-MAP): witnesses E1, E2 -- span %s, loop %s; pair (0.1,1,0,0), "
          "(0.1,0,1,0) -- span %s, loop %s.  Loop iff no common simultaneity frame -> H-FRAME"
          % (f["witness_span"], f["witness_loop"], f["pair_span"], f["pair_loop"]))
    print("  demand per pair: %s" % "; ".join("%s %.3g rad/s" % kv for kv in d["demand_J"].items()))
    for lbl, key in (("century", "reach_century"), ("1 yr", "reach_1yr")):
        print("  SPACELIKE reach at the %s J (trials = 4/delta^2, two settings at 2 SE):" % lbl)
        for name, v in d[key].items():
            print("    %-36s 2nd order delta %.3g (%.3g trials); 1st order delta %.3g (%.3g trials)"
                  % (name, v["delta_2nd"], v["trials_2nd"], v["delta_1st"], v["trials_1st"]))
    print("  TIMELIKE protocol under H-J-DISTANCE-FREE (crosstalk controlled): at the day J a full transfer in 1 day at "
          "any separation")
    print("  present spacelike no-signalling checks (READ), the J each allows (CONDITIONAL), and the lab-frame limit:")
    for k, v in d["nosig_bounds"].items():
        print("    %-50s A/B J <= %.3g; C J <= %.3g rad/s; preferred frame v/c < %.3f" % (k, v["A_or_B"], v["C"],
                                                                                    v["lab_frame_v_over_c"]))
    tk, tj = d["tightest"]
    print("  tightest (A/B): %.3g rad/s (%s) = %.2g x the day demand; under reading C %.3g = %.2g x -- not excluded "
          "under H-J-DISTANCE-FREE, H-SETTING-DEPENDENCE, H-UNIVERSAL-COUPLING" % (tj, tk, tj / d["demand_J"]["1 day"],
                                                                                 d["tightest_C"],
                                                                                 d["tightest_C"] / d["demand_J"]["1 day"]))
    fa = d["falloff_alpha"]
    print("  if J falls as r^-alpha the tightest bound carried to L EXCLUDES the device's coupling for alpha > %.3f "
          "(day) / %.3f (century)" % (fa["1 day"], fa["1 century"]))
    for k, v in d["no_statistic"].items():
        print("    no statistic: %s -- %s" % (k, v))
    for k, v in d["speed_bounds"].items():
        print("    speed bound: %s -- %s" % (k, v))
    print("  a lower bound on v cannot exclude v = infinity in a preferred frame: the speed bounds do not exclude the "
          "branch, and Bancal's privileged-frame reading supports carrying H-FRAME")


def selftest():
    n_ok = n_bad = n_ctl = 0
    n_struct = 0

    def chk(label, got, want, ctl=False):
        nonlocal n_ok, n_bad, n_ctl
        ok = got == want
        n_ok += ok
        n_bad += not ok
        n_ctl += ctl
        print("  [%s]%s %-96s %r" % ("ok" if ok else "XX", " CTL" if ctl else "", label[:96], got))

    def structural(text):
        nonlocal n_struct
        n_struct += 1
        print("  [STRUCTURAL] " + text)

    print("nonlocal.py selftest")
    d = collect()
    f = d["frame"]
    chk("loops, asked of latticectc's search: the witnesses (timelike span) close one, the spacelike-span pair keyed to "
        "different frames does not -- loop iff no common simultaneity frame",
        (f["witness_span"], f["witness_loop"], f["pair_span"], f["pair_loop"]),
        ("timelike", True, "spacelike", False))
    rc = d["reach_century"]
    chk("SPACELIKE reach at the century J, second-order map: at L over 1e-3 (%.3g, %.3g trials), at Earth-Moon under "
        "1e-15 (%.3g)" % (rc["L (4.24 ly)"]["delta_2nd"], rc["L (4.24 ly)"]["trials_2nd"],
                          rc["Earth-Moon (3.84e8 m)"]["delta_2nd"]),
        (rc["L (4.24 ly)"]["delta_2nd"] > 1e-3, rc["Earth-Moon (3.84e8 m)"]["delta_2nd"] < 1e-15), (True, True))
    dj = d["demand_J"]
    tk, tj = d["tightest"]
    chk("not excluded under every map tried: the tightest bound exceeds the day demand per pair by over 1e8 under "
        "readings A/B (%.2g) and over 1e5 under reading C (%.2g)" % (tj / dj["1 day"], d["tightest_C"] / dj["1 day"]),
        (tj / dj["1 day"] > 1e8, d["tightest_C"] / dj["1 day"] > 1e5), (True, True))
    _r = NOSIG_TESTS["NIST 2015, 1-pulse margin (Shalm 1511.03189v2)"]
    chk("  CONTROL: the NIST geometry with a marginal shift of 1e-24 would EXCLUDE the day J (the comparison can "
        "turn)", J_bound(1e-24, _r["r_m"], _r["margin_s"]) < dj["1 day"], True, ctl=True)
    fa = d["falloff_alpha"]
    chk("with J falling as r^-alpha the conclusion flips above alpha %.3f (day) and %.3f (century): both between 0.5 "
        "and 1" % (fa["1 day"], fa["1 century"]), (0.5 < fa["1 day"] < 1, 0.5 < fa["1 century"] < 1), (True, True))
    chk("the NIST bound's lab-frame condition: the preferred frame must move below 0.95 c along the axis (%.3f)"
        % d["nosig_bounds"]["NIST 2015, 1-pulse margin (Shalm 1511.03189v2)"]["lab_frame_v_over_c"],
        d["nosig_bounds"]["NIST 2015, 1-pulse margin (Shalm 1511.03189v2)"]["lab_frame_v_over_c"] < 0.95, True)
    chk("every READ test names its route and phrase; phrases under 15 words",
        ([k for k, v in NOSIG_TESTS.items() if not (v.get("route") and v.get("phrase"))],
         [k for k, v in NOSIG_TESTS.items() if len(v["phrase"].split()) >= 15]), ([], []))
    structural("one coupling alone never closes a loop (multiples of a spacelike vector are spacelike), and couplings "
               "keyed to one frame (t = 0) never do (sums keep t = 0)")
    structural("J_bound inverts sin^2(J t) <= delta_max (and J t <= delta_max/2 for reading C)")
    structural("trials = 4/delta^2 is the two-proportion count at 2 SE near p = 1/2")
    structural("a test at r = L resolving 1e-3 excludes the century J iff sin^2(J L/c) > 1e-3 -- the reach check "
               "restated (first counted as a CONTROL)")
    structural("Vienna's readings A and B differ by 1/P+ in delta, so by about sqrt(1/P+) = 64x in J")
    print("\n%d/%d checks pass, %d of them controls; %d STRUCTURAL printed, not counted"
          % (n_ok, n_ok + n_bad, n_ctl, n_struct))
    return n_bad == 0


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    elif "--json" in sys.argv:
        print(json.dumps(collect(), indent=1, default=str))
    else:
        report()
