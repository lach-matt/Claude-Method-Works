#!/usr/bin/env python3
"""
supply.py -- Step 1c: present-day SUPPLY for READ-A, ASSEMBLE-B and CHANNEL, READ at source, set against demand.py.

Not seated.  M (rulings item 37): "All three (Recommended)" -- read present supply for the three subsystems, open
literature only, route recorded.  Every supply figure below is READ (the source, its place, the route, and a short
phrase containing the number); every derived rate is COMPUTED here from the READ inputs, never typed; every demand is
IMPORTED from demand.py.  Nothing is repaired and no owner is edited.

    python3 supply.py              report
    python3 supply.py --selftest   checks, with CONTROLS
    python3 supply.py --json       the numbers as JSON

ROUTES.  The figures were read by this session's three supply readers (2026-10-05) through alphaXiv
(answer_pdf_queries) and Firecrawl (scrape/search).  The two figures the largest gaps rest on were RE-READ by the lead
the same day: Sturm et al. 2608.12021v1 (alphaXiv: 1024 atoms, median 9.6 ms, t0 = 78.6 ms, pp.3, 6) and the IEEE
Photonics Society release (Firecrawl search excerpt of the page: 267 Mbps at 55 million km, 8.3 Mbps at 400 million km).
Paywalled or blocked, reported and not routed around: Gault et al. 2021 Nat. Rev. Methods Primers (paywall); PubMed
(reCAPTCHA); the full text of Biswas & Srinivasan, IEEE JSTQE 32(1) (sign-in; its open abstract was read).

WHAT IT COMPUTES
  The gap = demand / supply, per subsystem, at each schedule, for ONE instrument (H-ONE-INSTRUMENT).  The gap is also
  the number of such instruments that would have to run in parallel at the demonstrated rate (H-PARALLEL-INSTRUMENTS),
  which this file prints and does not claim is buildable.
  CHANNEL: the demonstrated rates are at 55e6 to 2.58e13 m; the demand is at 4.02e16 m.  The rate is carried to the
  Proxima span under H-INVERSE-SQUARE (R proportional to received power proportional to 1/d^2 at fixed hardware;
  Karmous et al. 2212.04933v4 eq. (2), READ, with its eq. (3) caveat: linear in received power only when
  quantum-limited -- noise-limited capacity falls faster, bandwidth-limited saturates).  The measured DSOC pair tests
  the law: from 55e6 km to 400e6 km the rate fell less than 1/d^2 predicts (the near point is not photon-starved), so the
  FARTHEST measured point is the anchor.
  ASSEMBLE-B errors: at a per-placement error p (READ) over the object's N atoms, the expected number of misplaced atoms
  is p N (H-INDEPENDENT-ERRORS) -- what an error-free assembly would have to correct.

NAMED HYPOTHESES
  H-ONE-INSTRUMENT, H-PARALLEL-INSTRUMENTS, H-INVERSE-SQUARE, H-FIXED-HARDWARE (the demonstrated link's power and
  apertures carried unchanged to 4.24 ly), H-FIXED-CARRIER (its 1550 nm carrier kept), H-FRIIS-IDEAL (far-field
  received power with no pointing, atmospheric or detector loss: a ceiling), H-NO-PREP (preparing a bulk object into
  atom-probe specimens is not priced), H-INDEPENDENT-ERRORS, and demand.py's (H-SCHEDULE, H-UNIFORM-RATE,
  H-PARALLEL) with their owners'.
THE CHANNEL'S 1/d^2 CARRY CUTS BOTH WAYS (Step 1c verifier, applied).  Optimistic for the hardware: at Proxima the
  DSOC link receives about 6e-3 signal photons per second, and with background and dark counts capacity falls
  faster than 1/d^2.  Pessimistic against physics: the board's own channel floor, inverted at the same received
  power, allows about 4e6 bps -- if quanta of any frequency could be beamed, which these apertures cannot.  And
  the measured 226e6-400e6 km pair obeys 1/d^2 to within 4%, while the 55e6-400e6 km pair departs by 1.64x.
  Linear closure (rate proportional to received power) is excluded at the demand: fewer than one transverse mode,
  and a rate above the carrier frequency (Karmous eq. (3)'s bandwidth saturation).
WHAT THE SUPPLY FIGURES ARE NOT
  The tweezer arrays place atoms in vacuum micrometres apart, not into a bonded solid; the STM figure moves vacancies
  in a Cl layer at 1.5 K, adding no atom; atom probe tomography destroys the specimen it reads (field evaporation).
  Each is the nearest demonstrated operation, not the operation the device needs.
"""
import contextlib
import io
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path:
    sys.path.insert(0, HERE)
with contextlib.redirect_stdout(io.StringIO()):
    import demand

# ============================================================================ READ: READ-A
READ_A = {
    "APT_LEAP4000XHR": {
        "source": "PNNL EMSL instrument page, emsl.pnnl.gov/science/instruments-resources/atom-probe-tomography",
        "route": "READ via Firecrawl scrape (supply reader)", "kind": "instrument specification",
        "ions_per_hour": 50e6, "phrase": "Collection Rate: > 50 M ions per hour",
        "detection_efficiency": 0.40, "phrase_eff": "Detection Efficiency: approx. 40%",
        "specimen_nm": (100, 100, 300),
        "note": "a specification, not a demonstration; a specimen is a needle of about 100 x 100 x 300 nm (the same "
                "page, read by the Step 1c verifier); preparing a bulk object into such needles is not included "
                "(H-NO-PREP); the 60% of removed atoms not detected are never read"},
    "APT_SrTiO3_run": {
        "source": "arXiv:2501.11089v1 (Rybak et al.)", "route": "READ via alphaXiv answer_pdf_queries, p.6 and "
        "Supp. Table S1 (supply reader)", "kind": "measured",
        "pulse_rate_hz": 100e3, "ions_per_pulse": (0.15e-2, 0.3e-2),
        "phrase": "detection rate window was set to 0.15 - 0.3 ions per 100 pulses"},
    "APT_destroys": {
        "source": "arXiv:2603.10276v1 (Marquis et al.)", "route": "READ via alphaXiv answer_pdf_queries, p.3 "
        "(supply reader)", "kind": "statement of method",
        "phrase": "extracted almost one by one from a specimen's surface"},
    "AET_atoms_per_reconstruction": {
        "source": "arXiv:2603.19942v1 (Zhang et al.), Supp. Table 1 p.27", "route": "READ via alphaXiv "
        "answer_pdf_queries (supply reader)", "kind": "measured (no acquisition time stated)",
        "atoms": 8800, "dose_e_per_A2": 5.7e5},
}

# ============================================================================ READ: ASSEMBLE-B
ASSEMBLE_B = {
    "tweezer_Sturm2026": {
        "source": "arXiv:2608.12021v1 (Sturm et al.)", "route": "READ via alphaXiv answer_pdf_queries, pp.3, 5-6 "
        "(supply reader; re-read by the lead)", "kind": "measured",
        "atoms": 1024, "transport_s": 9.6e-3, "t0_s": 78.6e-3, "sequences_max": 12,
        "transport_efficiency_min": 0.993, "filling": 0.993,
        "phrase": "a median of t_r,M = 9.6 ms"},
    "tweezer_Lin2024": {
        "source": "arXiv:2412.14647v1 (Lin et al.)", "route": "READ via alphaXiv answer_pdf_queries, abstract, "
        "p.8, Figs. 5a-b (supply reader; p.8 and Fig. 5a re-read by the Step 1c verifier)",
        "kind": "claim (Fig. 5b's time breakdown is labelled Simulated)",
        "atoms": 2024, "time_s_per_round": 60e-3, "rounds": 2, "single_round_max_atoms": 2016, "filling": 0.990,
        "phrase": "up to 2024 atoms with a constant time cost of 60 ms",
        "note": "60 ms is per rearrangement round; one round reaches at most 2016 atoms, 2024 took two rounds"},
    "tweezer_Barredo2016": {
        "source": "arXiv:1607.03042v1 (Barredo et al.)", "route": "READ via alphaXiv answer_pdf_queries, p.2, "
        "Supp. S.2 (supply reader)", "kind": "measured",
        "atoms": 50, "time_s": 50e-3, "move_success": 0.993, "phrase": "in about 50 ms for N ~ 50"},
    "STM_Kalff2016": {
        "source": "arXiv:1604.02265v1 (Kalff et al.)", "route": "READ via alphaXiv answer_pdf_queries, pp.2-3, 12 "
        "(supply reader)", "kind": "measured (approximate)",
        "vacancies_per_block": 64, "block_time_s": 600.0, "hops": 264, "wrong_hops": 1,
        "phrase": "Automated construction of a complete block takes in the order of 10 minutes",
        "note": "vacancies in a Cl layer on Cu(100) at 1.5 K; no atom added"},
}

# ============================================================================ READ: CHANNEL
CHANNEL = {
    "DSOC_near": {
        "source": "IEEE Photonics Society release on Velasco et al., DOI 10.1109/JSTQE.2025.3636824",
        "route": "READ via Firecrawl (supply reader scrape; lead re-read the page excerpt)", "kind": "measured",
        "bps": 267e6, "d_m": 55e9, "phrase": "267 Mbps at 55 million km"},
    "DSOC_far": {
        "source": "same release", "route": "as DSOC_near", "kind": "measured",
        "bps": 8.3e6, "d_m": 400e9, "phrase": "8.3 Mbps at 400 million km",
        "hardware": "22 cm flight aperture, 4 W average 1550 nm (Biswas & Srinivasan abstract, READ); 5 m Hale"},
    "DSOC_226": {
        "source": "nasa.gov, optical comms demo transmits data over 140 million miles", "route": "READ via Firecrawl "
        "scrape (supply reader)", "kind": "measured", "bps": 25e6, "d_m": 226e9,
        "phrase": "transmitted test data at a maximum rate of 25 Mbps"},
    "Voyager1": {
        "source": "science.nasa.gov/mission/voyager/spacecraft/ and .../where-are-voyager-1-and-voyager-2-now/",
        "route": "READ via Firecrawl scrape, 2026-10-05 (supply reader; distance live-updating)",
        "kind": "current specification; distance as scraped", "bps": 160.0, "d_m": 2.58e13,
        "phrase": "downlink telemetry at 160 bits/sec normally"},
}
KARMOUS_2022 = {"source": "arXiv:2212.04933v4 (Karmous et al.)", "route": "READ via alphaXiv (supply reader), "
                "Sec. II-B eqs. (1)-(3)", "phrase": "inversely proportional to the link distance squared"}

D_PROXIMA_M = demand.w3corridor.before_light()["L_m"]


# ============================================================================ computed supply rates
def read_a_rates():
    a = READ_A["APT_LEAP4000XHR"]
    det = a["ions_per_hour"] / 3600.0
    r = READ_A["APT_SrTiO3_run"]
    lo, hi = (r["pulse_rate_hz"] * x for x in r["ions_per_pulse"])
    return {"APT spec, atoms READ (detected)/s": det, "APT spec, atoms removed/s (40% of them read)":
            det / a["detection_efficiency"], "APT SrTiO3 measured, ions/s (low)": lo,
            "APT SrTiO3 measured, ions/s (high)": hi}


def assemble_b_rates():
    s = ASSEMBLE_B["tweezer_Sturm2026"]
    li, ba, k = ASSEMBLE_B["tweezer_Lin2024"], ASSEMBLE_B["tweezer_Barredo2016"], ASSEMBLE_B["STM_Kalff2016"]
    return {"tweezer, transport only (Sturm; upper bound)": s["atoms"] / s["transport_s"],
            "tweezer, one full sequence (Sturm)": s["atoms"] / (s["transport_s"] + s["t0_s"]),
            "tweezer, full cycle (Lin; claim, two rounds)": li["atoms"] / (li["rounds"] * li["time_s_per_round"]),
            "tweezer (Barredo 2016)": ba["atoms"] / ba["time_s"],
            "STM vacancies (Kalff)": k["vacancies_per_block"] / k["block_time_s"]}


def placement_errors():
    """[(name, p, expected misplaced atoms over the object)] -- H-INDEPENDENT-ERRORS."""
    N = demand.atoms()
    k = ASSEMBLE_B["STM_Kalff2016"]
    # CORRECTED (Step 1c verifier): Kalff's 1/264 is per HOP and raw (the program re-planned after it); a vacancy
    # took 264/64 hops, so the raw error per PLACEMENT is 1 - (1 - 1/264)^(264/64).  First printed per hop beside
    # the tweezers' per-move figures as one basis.
    hops_per = k["hops"] / k["vacancies_per_block"]
    ps = [("STM, raw per placement (Kalff: 1 of 264 hops, %.3g hops each)" % hops_per,
           1.0 - (1.0 - k["wrong_hops"] / k["hops"]) ** hops_per),
          ("tweezer single move (Barredo, 1 - 0.993)", 1.0 - ASSEMBLE_B["tweezer_Barredo2016"]["move_success"]),
          ("tweezer transport (Sturm, 1 - 0.993 at least)", 1.0 - ASSEMBLE_B["tweezer_Sturm2026"]
           ["transport_efficiency_min"])]
    return [(n, p, p * N) for n, p in ps]


def inverse_square(bps, d_from, d_to):
    """H-INVERSE-SQUARE at fixed hardware."""
    return bps * (d_from / d_to) ** 2


def dsoc_law_test():
    """The measured DSOC pair against 1/d^2: the far rate predicted from the near one, and the measured / predicted."""
    n, f = CHANNEL["DSOC_near"], CHANNEL["DSOC_far"]
    pred = inverse_square(n["bps"], n["d_m"], f["d_m"])
    return {"predicted_far_bps": pred, "measured_far_bps": f["bps"], "measured_over_predicted": f["bps"] / pred}


DSOC_HW = {"P_t_W": 4.0, "D_t_m": 0.22, "D_r_m": 5.0, "lambda_m": 1550e-9,
           "source": "Biswas & Srinivasan, IEEE JSTQE 32(1), open abstract (22 cm, 4 W average, 1550 nm, 5 m Hale)",
           "route": "READ via Firecrawl of ieeexplore abstract (supply reader); full text behind sign-in"}


def link_at_proxima():
    """DSOC's hardware at the Proxima span under ideal far-field Friis (P_r = P_t A_t A_r / (lambda d)^2; no
    pointing, atmospheric or detector loss -- a CEILING on received power): received power, signal photons/s, the
    transverse-mode number A_t A_r/(lambda d)^2, the carrier frequency, and against the board's own channel floor
    (seat.channel_floor via demand.py, any carrier) the factor by which received power must rise, and the floor's
    inverse -- the rate the board's floor would allow at that power if quanta of any frequency could be beamed."""
    import math
    h, c, hbar = demand.seat.H, demand.seat.C, demand.aperture.HBAR
    At = math.pi * (DSOC_HW["D_t_m"] / 2) ** 2
    Ar = math.pi * (DSOC_HW["D_r_m"] / 2) ** 2
    lam, d = DSOC_HW["lambda_m"], D_PROXIMA_M
    modes = At * Ar / (lam * d) ** 2
    Pr = DSOC_HW["P_t_W"] * modes
    nu = c / lam
    sp = demand.counts()[0][0]
    rows = dict((r["schedule"], r["channel"][sp]["floor_W_one_pol"]) for r in demand.demand_table())
    return {"P_r_W": Pr, "photons_per_s": Pr / (h * nu), "modes": modes, "carrier_Hz": nu,
            "photon_eV": h * nu / 1.602176634e-19,
            "power_rise_needed": dict((k, v / Pr) for k, v in rows.items()),
            "floor_inverse_bps_at_P_r": math.sqrt(math.pi * Pr / (3.0 * hbar)) / math.log(2.0)}


def dsoc_long_range_test():
    """The 226e6 km point predicted from the 400e6 km point under 1/d^2: measured / predicted."""
    f, m = CHANNEL["DSOC_far"], CHANNEL["DSOC_226"]
    pred = inverse_square(f["bps"], f["d_m"], m["d_m"])
    return {"predicted_bps": pred, "measured_bps": m["bps"], "measured_over_predicted": m["bps"] / pred}


def channel_at_proxima():
    return dict((k, inverse_square(v["bps"], v["d_m"], D_PROXIMA_M)) for k, v in CHANNEL.items())


# ============================================================================ the gaps
def gaps():
    out = []
    ra, ab, ch = read_a_rates(), assemble_b_rates(), channel_at_proxima()
    # CORRECTED (Step 1c verifier): first the atoms REMOVED (3.47e4/s), which overstated the read by 2.5x --
    # 60% of removed atoms are never detected.  The read is the detected count (a specification).
    best_read = ra["APT spec, atoms READ (detected)/s"]
    best_place = ab["tweezer, transport only (Sturm; upper bound)"]
    best_link = max(ch["DSOC_far"], ch["Voyager1"])
    sp = demand.counts()[0][0]
    for row in demand.demand_table():
        out.append({"schedule": row["schedule"],
                    "READ-A": row["read_a"]["atoms_per_s"] / best_read,
                    "ASSEMBLE-B": row["assemble_b"]["atoms_per_s"] / best_place,
                    "CHANNEL": row["channel"][sp]["bits_per_s"] / best_link})
    return {"best": {"READ-A atoms/s": best_read, "ASSEMBLE-B atoms/s": best_place,
                     "CHANNEL bits/s at Proxima": best_link}, "rows": out}


def gap_channel_count(count_index, schedule):
    n = demand.counts()[count_index][0]
    row = [r for r in demand.demand_table() if r["schedule"] == schedule][0]
    return row["channel"][n]["bits_per_s"] / channel_at_proxima()["DSOC_far"]


def collect():
    return {"read_a": read_a_rates(), "assemble_b": assemble_b_rates(), "errors": placement_errors(),
            "dsoc_law_test": dsoc_law_test(), "dsoc_long_range_test": dsoc_long_range_test(),
            "channel_at_proxima": channel_at_proxima(), "link_at_proxima": link_at_proxima(), "gaps": gaps(),
            "channel_gap_finest_count_1yr": gap_channel_count(2, "1 yr"),
            "READ": {"READ_A": READ_A, "ASSEMBLE_B": ASSEMBLE_B, "CHANNEL": CHANNEL, "KARMOUS": KARMOUS_2022}}


def report():
    d = collect()
    print("Step 1c -- present supply, READ at source, against demand.py (one instrument each; H-ONE-INSTRUMENT)")
    print("\n  READ-A (atom probe tomography destroys what it reads):")
    for k, v in d["read_a"].items():
        print("    %-52s %.3g" % (k, v))
    print("\n  ASSEMBLE-B (atoms per second; none of these makes a bonded solid):")
    for k, v in d["assemble_b"].items():
        print("    %-52s %.3g" % (k, v))
    print("    expected misplaced atoms over the object's %.4g atoms (H-INDEPENDENT-ERRORS):" % demand.atoms())
    for n, p, m in d["errors"]:
        print("      %-50s p = %.3g -> %.3g" % (n, p, m))
    t = d["dsoc_law_test"]
    print("\n  CHANNEL: the DSOC pair against 1/d^2 -- far rate predicted %.3g bps, measured %.3g (%.2fx the law): the "
          "near point is not photon-starved, so the farthest point anchors" % (t["predicted_far_bps"],
                                                                               t["measured_far_bps"],
                                                                               t["measured_over_predicted"]))
    t2 = d["dsoc_long_range_test"]
    print("    and from 400e6 km to 226e6 km the law holds: predicted %.3g bps, measured %.3g (%.2fx)"
          % (t2["predicted_bps"], t2["measured_bps"], t2["measured_over_predicted"]))
    print("    carried to %.4g m under H-INVERSE-SQUARE and H-FIXED-HARDWARE, bits/s:" % D_PROXIMA_M)
    for k, v in d["channel_at_proxima"].items():
        print("      %-12s %.3g" % (k, v))
    lk = d["link_at_proxima"]
    print("    DSOC's hardware at that span (ideal Friis, a ceiling): received %.2g W = %.2g signal photons/s; "
          "transverse modes %.2g; carrier %.3g Hz (%.2f eV quanta)" % (lk["P_r_W"], lk["photons_per_s"], lk["modes"],
                                                                     lk["carrier_Hz"], lk["photon_eV"]))
    print("    against the board's channel floor (any carrier), received power must rise by %s"
          % "; ".join("%.2g (%s)" % (v, k) for k, v in lk["power_rise_needed"].items()))
    print("    the floor inverted at %.2g W allows %.2g bps -- if quanta of any frequency could be beamed, which these "
          "apertures cannot" % (lk["P_r_W"], lk["floor_inverse_bps_at_P_r"]))
    g = d["gaps"]
    print("\n  GAP = demand / best demonstrated supply, one instrument (also the number of such instruments in parallel):")
    print("    best: %s" % "; ".join("%s %.3g" % kv for kv in g["best"].items()))
    for r in g["rows"]:
        print("    %-10s READ-A %.2g   ASSEMBLE-B %.2g   CHANNEL %.2g" % (r["schedule"], r["READ-A"], r["ASSEMBLE-B"],
                                                                         r["CHANNEL"]))
    print("    (CHANNEL on the species count; on the 0.1 A count the 1 yr gap is %.2g)"
          % d["channel_gap_finest_count_1yr"])


def selftest():
    n_ok = n_bad = n_ctl = 0

    def chk(label, got, want, ctl=False):
        nonlocal n_ok, n_bad, n_ctl
        ok = got == want
        n_ok += ok
        n_bad += not ok
        n_ctl += ctl
        print("  [%s]%s %-96s %r" % ("ok" if ok else "XX", " CTL" if ctl else "", label[:96], got))

    print("supply.py selftest")
    chk("every READ record names a source, a route and a kind", [k for D in (READ_A, ASSEMBLE_B, CHANNEL)
                                                             for k, v in D.items()
                                                             if not all(v.get(f) for f in ("source", "route",
                                                                                           "kind"))], [])
    chk("every quoted phrase is short (under 15 words: copyright rule)",
        [k for D in (READ_A, ASSEMBLE_B, CHANNEL) for k, v in D.items()
         for f in ("phrase", "phrase_eff") if f in v and len(v[f].split()) >= 15], [])
    # NARROWED (Step 1c verifier): first labelled 'each phrase carries the figure' over every record while it
    # compared six strings with strings; now, for the six figures the rates and gaps rest on, the NUMERIC field
    # used in the arithmetic is compared with the number its quoted phrase prints.
    _six = (("APT_LEAP4000XHR", "ions_per_hour", 1e6, r"> (\d+(?:\.\d+)?) M ions"),
            ("tweezer_Sturm2026", "transport_s", 1e-3, r"= (\d+(?:\.\d+)?) ms"),
            ("tweezer_Lin2024", "atoms", 1.0, r"up to (\d+) atoms"),
            ("DSOC_near", "bps", 1e6, r"(\d+(?:\.\d+)?) Mbps"),
            ("DSOC_far", "bps", 1e6, r"(\d+(?:\.\d+)?) Mbps"),
            ("Voyager1", "bps", 1.0, r"at (\d+(?:\.\d+)?) bits/sec"))

    def _field_faults(recs):
        import re as _re
        bad = []
        for k, f, scale, rx in _six:
            m = _re.search(rx, recs[k]["phrase"])
            if not m or abs(float(m.group(1)) * scale - recs[k][f]) > 1e-9 * abs(recs[k][f]):
                bad.append(k)
        return bad
    _all = {**READ_A, **ASSEMBLE_B, **CHANNEL}
    chk("for the six figures the rates and gaps rest on, the numeric field used equals the number in its phrase",
        _field_faults(_all), [])
    _bad = dict(_all)
    _bad["tweezer_Sturm2026"] = dict(_bad["tweezer_Sturm2026"], transport_s=9.0e-3)
    chk("  CONTROL: a field that disagrees with its phrase (Sturm's transport 9.0 ms against '9.6 ms') is caught",
        _field_faults(_bad), ["tweezer_Sturm2026"], ctl=True)
    t = dsoc_law_test()
    chk("the measured DSOC pair does NOT follow 1/d^2 from the near point: the far rate is %.2fx the law's (more "
        "than 1.5x)" % t["measured_over_predicted"], t["measured_over_predicted"] > 1.5, True)
    _keep = dict(CHANNEL["DSOC_far"])
    CHANNEL["DSOC_far"]["bps"] = _keep["bps"] / 4.0
    try:
        _faster = dsoc_law_test()["measured_over_predicted"]
    finally:
        CHANNEL["DSOC_far"] = _keep
    chk("  CONTROL: a far point falling faster than 1/d^2 (the measured rate quartered) reads below 1 (%.2f)"
        % _faster, _faster < 1.0, True, ctl=True)
    t2 = dsoc_long_range_test()
    chk("from 400e6 to 226e6 km the measured pair DOES follow 1/d^2 to within 5%% (measured / predicted %.3f)"
        % t2["measured_over_predicted"], abs(t2["measured_over_predicted"] - 1.0) < 0.05, True)
    ab = assemble_b_rates()
    chk("Sturm's transport-only rate, computed from the READ inputs: 1024 / 9.6 ms between 1.0e5 and 1.1e5 per s "
        "(%.4g)" % ab["tweezer, transport only (Sturm; upper bound)"],
        1.0e5 < ab["tweezer, transport only (Sturm; upper bound)"] < 1.1e5, True)
    chk("  and with the 78.6 ms detection phase the full sequence is about 9x slower (between 8 and 10x)",
        8 < ab["tweezer, transport only (Sturm; upper bound)"] / ab["tweezer, one full sequence (Sturm)"] < 10, True)
    g = gaps()
    yr = [r for r in g["rows"] if r["schedule"] == "1 yr"][0]
    chk("at 1 yr the gaps, computed: READ-A (detected atoms) between 1e16 and 2e16 (%.2g); ASSEMBLE-B between 1e15 "
        "and 1e16 (%.2g); CHANNEL over 1e23 (%.2g)" % (yr["READ-A"], yr["ASSEMBLE-B"], yr["CHANNEL"]),
        (1e16 < yr["READ-A"] < 2e16, 1e15 < yr["ASSEMBLE-B"] < 1e16, yr["CHANNEL"] > 1e23), (True, True, True))
    chk("the channel's best carried rate is DSOC's farthest point, not Voyager's, under the same law",
        g["best"]["CHANNEL bits/s at Proxima"] == channel_at_proxima()["DSOC_far"], True)
    lk = link_at_proxima()
    sp_rate_yr = [r for r in demand.demand_table() if r["schedule"] == "1 yr"][0]["channel"][
        demand.counts()[0][0]]["bits_per_s"]
    chk("linear closure is excluded at the 1 yr demand: fewer than one transverse mode (%.2g) and a rate (%.2g bps) "
        "above the 1550 nm carrier frequency (%.3g Hz)" % (lk["modes"], sp_rate_yr, lk["carrier_Hz"]),
        (lk["modes"] < 1, sp_rate_yr > lk["carrier_Hz"]), (True, True))
    chk("  and against the board's channel floor (any carrier) the received power must rise by over 1e27 at 1 yr "
        "(%.2g) -- more than the rate gap (%.2g)" % (lk["power_rise_needed"]["1 yr"], yr["CHANNEL"]),
        (lk["power_rise_needed"]["1 yr"] > 1e27, lk["power_rise_needed"]["1 yr"] > yr["CHANNEL"]), (True, True))
    chk("  the other direction, computed: the floor inverted at the received power allows %.2g bps, over 1e9 times "
        "the carried 1/d^2 rate -- if quanta of any frequency could be beamed (they cannot at these apertures)"
        % lk["floor_inverse_bps_at_P_r"],
        lk["floor_inverse_bps_at_P_r"] / channel_at_proxima()["DSOC_far"] > 1e9, True)
    print("  [STRUCTURAL] gap = demand / supply, so it equals the parallel-instrument count (H-PARALLEL-INSTRUMENTS)")
    print("  [STRUCTURAL] demand falls as 1/T and supply is fixed, so each gap scales as 1/T between schedules")
    print("  [STRUCTURAL] inverse_square is the 1/d^2 law itself (d -> 2d gives a quarter); a synthetic far point "
          "built with it reads 1.00x the law by construction")
    print("\nHISTORY: the first selftest counted the 1/T and 1/d^2 identities as checks (one labelled CONTROL); "
          "then a synthetic 1/d^2 point was counted as a CONTROL (Step 1c verifier: pred/pred = 1 by construction) "
          "-- all moved here.  The READ-A gap first used atoms REMOVED (6.1e15 at 1 yr); it now uses atoms read.")
    print("\n%d/%d checks pass, %d of them controls; 3 STRUCTURAL printed, not counted" % (n_ok, n_ok + n_bad, n_ctl))
    return n_bad == 0


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    elif "--json" in sys.argv:
        print(json.dumps(collect(), indent=1, default=str))
    else:
        report()
