#!/usr/bin/env python3
"""minors.py -- the seven MINOR rows of FLAWS.tsv, each settled the way the
register asks: a relabel, a citation, a recomputation or a named structure,
with a number where the register wants one, at mid and at critical.

  F-32  'supercritical Rankine' at 565 C salt. Helios-3 has no steam cycle
        (sCO2 recompression at 715 C); the salt-block fallback is subcritical
        reheat at helios.ETA_CYCLE. Relabelled.
  F-33  'CBC Seismic Zone 4; 0.75 g'. Zones left the code in 2001; design
        is site-specific under ASCE 7. The 0.75 g is kept as a design target
        above the mapped MCE at every node, and the citation corrected.
  F-34  '11.8 MMT CO2 avoided'. Recomputed from the hour-by-hour: the energy
        the plant serves, at CAISO marginal emissions, as sized and closed.
  F-37  'sovereign authority'. The Authority is defined as a statutory
        public entity created by the Act, on the pattern of the 2001 power
        authority the proposal should acknowledge, and Gov. Code 8571 is
        cited only for what it does.
  F-38  jobs. Permanent jobs per MW from two built plants, construction
        jobs from Ivanpah's peak, Title II's from Carlsbad; the multiplier
        is not carried.
  F-39  'turnkey EPC'. Named as a procurement structure: one EPC per node
        with an owner's engineer, the pilot and the first module as
        separate contracts.
  F-40  '40 dBA at the boundary'. The attenuation computed: source level,
        enclosure, distance; the enclosure priced as a share of module
        capital.

Every constant carries a status. Stdlib only.
"""
import argparse
import math
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import helios as H                                              # noqa: E402
import cspchain as C                                            # noqa: E402
import hourly3 as HR                                            # noqa: E402
import aquacost as AQ                                           # noqa: E402
import joinder as J                                             # noqa: E402

CASES = ("mid", "critical")
# --- F-33 ------------------------------------------------------------------------
MCE_PGA_G = {"Mojave (Kramer Junction)": (0.45, 0.50),        # mapped MCE_R PGA, nominal / critical   SOURCED (F-33: ~0.4-0.5 g)
             "Imperial (Desert Center)": (0.35, 0.45),        #                                         ASSUMED band
             "Central Valley (Westside)": (0.40, 0.55)}       # San Andreas proximity                   ASSUMED band
DESIGN_PGA_G = 0.75                       # Title I's own target, kept                     Title I §9
# --- F-34 ------------------------------------------------------------------------
CAISO_MARGINAL_T_MWH = (0.40, 0.35)       # marginal gas, t CO2/MWh; critical = less avoided  SOURCED band 0.35-0.45
CLAIMED_MMT = 11.8                        # v0.1 §6                                         Title I §6
# --- F-38 ------------------------------------------------------------------------
PERMANENT_PER_MW = (0.41, 0.23)           # Crescent Dunes ~45/110 MW; Ivanpah ~90/392 MW  SOURCED (F-38)
CONSTRUCTION_PEAK_PER_MW = 2_100.0 / 392.0   # Ivanpah peak construction ~2,100 on 392 MW   SOURCED
PV_OM_PER_MW = 0.10                       # utility PV O&M jobs per MW_AC                    ASSUMED band 0.05-0.15
CARLSBAD_PERMANENT = 40.0                 # Carlsbad plant staff                              SOURCED band 35-45
CLAIMED_JOBS = (22_500, 1_350)            # construction, permanent, v0.1 §7                  Title I §7
# --- F-40 ------------------------------------------------------------------------
RO_SOURCE_DBA = (90.0, 100.0)             # high-pressure pumps at 1 m, nominal / critical   SOURCED band (F-40: 85-100)
ENCLOSURE_DB = (28.0, 22.0)               # acoustic enclosure attenuation                     SOURCED band 20-30
BOUNDARY_DBA = 40.0                       # v0.1's own claim, kept as the requirement          Title II §3
ENCLOSURE_SHARE = (0.01, 0.02)            # of module capital                                  ASSUMED band


def cycle_label():
    return dict(helios3="sCO₂ recompression Brayton, 715 °C", helios3_eta=C.design("helios3", "mid")["links"]["cycle"],
                fallback="subcritical reheat steam at ~540 °C live steam from 565 °C salt", fallback_eta=H.ETA_CYCLE)


def seismic(case):
    ci = CASES.index(case)
    return {n: (v[ci], DESIGN_PGA_G / v[ci]) for n, v in MCE_PGA_G.items()}


def co2(case):
    ci = CASES.index(case)
    d = C.design("helios3", case)
    as_sized = HR.run(case)["load"] * HR.run(case)["served_frac"] / 1e6
    closed = d["e_twh"]
    return dict(as_sized_twh=as_sized, closed_twh=closed, factor=CAISO_MARGINAL_T_MWH[ci],
                as_sized_mmt=as_sized * CAISO_MARGINAL_T_MWH[ci], closed_mmt=closed * CAISO_MARGINAL_T_MWH[ci])


def jobs(case):
    ci = CASES.index(case)
    d = C.design("helios3", case)
    block = d["turb_mw"] * 1.5
    perm = block * PERMANENT_PER_MW[ci] + d["pv_mw"] * PV_OM_PER_MW
    constr = block * CONSTRUCTION_PEAK_PER_MW
    modules = J.modules_to_close(case, 500.0, J.winter(case))["modules"]
    return dict(block_mw=block, permanent=perm, construction_peak=constr, title2_permanent=modules * CARLSBAD_PERMANENT)


def noise(case):
    ci = CASES.index(case)
    src, enc = RO_SOURCE_DBA[ci], ENCLOSURE_DB[ci]
    need = src - BOUNDARY_DBA
    d_open = 10 ** (need / 20.0)                     # spherical spreading from 1 m
    d_enclosed = 10 ** ((need - enc) / 20.0)
    cost_m = AQ.module(case)["financed_m"] * ENCLOSURE_SHARE[ci]
    return dict(source=src, enclosure=enc, d_open_m=d_open, d_enclosed_m=d_enclosed, cost_m=cost_m)


def report():
    print()
    print("  THE MINORS, SETTLED")
    print("  ====================")
    cl = cycle_label()
    print(f"    F-32  Helios-3's cycle is {cl['helios3']} at {cl['helios3_eta']:.2f}; the salt fallback is")
    print(f"          {cl['fallback']}, {cl['fallback_eta']:.2f}. 'Supercritical Rankine' is withdrawn.")
    print()
    print("    F-33  Seismic zones left the code in 2001; design is site-specific under ASCE 7")
    print("          (site class, mapped MCE_R). The 0.75 g target is kept, above the mapped value")
    print("          at every node:")
    for case in CASES:
        print(f"          {case}: " + "; ".join(f"{n.split(' (')[0]} {v[0]:.2f} g, target {v[1]:.2f}x" for n, v in seismic(case).items()))
    print()
    print("    F-34  CO2 avoided, recomputed from the hour-by-hour at CAISO marginal emissions:")
    print(f"      {'':<40}{'mid':>12}{'critical':>12}")
    cc = {c: co2(c) for c in CASES}
    print(f"      {'served as sized, TWh':<40}" + "".join(f"{cc[c]['as_sized_twh']:12.2f}" for c in CASES))
    print(f"      {'served closed, TWh':<40}" + "".join(f"{cc[c]['closed_twh']:12.2f}" for c in CASES))
    print(f"      {'marginal factor, t/MWh':<40}" + "".join(f"{cc[c]['factor']:12.2f}" for c in CASES))
    print(f"      {'avoided as sized, MMT/yr':<40}" + "".join(f"{cc[c]['as_sized_mmt']:12.2f}" for c in CASES))
    print(f"      {'avoided closed, MMT/yr':<40}" + "".join(f"{cc[c]['closed_mmt']:12.2f}" for c in CASES))
    print(f"          v0.1 claimed {CLAIMED_MMT} MMT; the honest figure is {cc['critical']['as_sized_mmt']:.1f}-{cc['mid']['closed_mmt']:.1f}.")
    print()
    print("    F-37  'Sovereign authority' names no mechanism. The Authority is a statutory")
    print("          public entity created by the Act -- on the pattern of the California")
    print("          Consumer Power and Conservation Financing Authority (SB 6X, 2001),")
    print("          which existed and was defunded by 2004, a history the Act acknowledges")
    print("          -- registered as a load-serving entity (F-10). Gov. Code 8571 is cited")
    print("          only for what it does: suspend regulatory statutes during a declared")
    print("          emergency; it does not issue a coastal permit or shorten NEPA (F-15, F-25).")
    print()
    print("    F-38  Jobs, from built plants per MW rather than asserted:")
    print(f"      {'':<40}{'mid':>12}{'critical':>12}")
    jj = {c: jobs(c) for c in CASES}
    print(f"      {'block at x1.5, MW':<40}" + "".join(f"{jj[c]['block_mw']:12,.0f}" for c in CASES))
    print(f"      {'permanent, Title I':<40}" + "".join(f"{jj[c]['permanent']:12,.0f}" for c in CASES))
    print(f"      {'construction peak, Title I':<40}" + "".join(f"{jj[c]['construction_peak']:12,.0f}" for c in CASES))
    print(f"      {'permanent, Title II (water route)':<40}" + "".join(f"{jj[c]['title2_permanent']:12,.0f}" for c in CASES))
    print(f"          v0.1 claimed {CLAIMED_JOBS[0]:,} construction and {CLAIMED_JOBS[1]:,} permanent; the $4.2 B")
    print("          multiplier is unsourced and is not carried.")
    print()
    print("    F-39  'Turnkey EPC' is a procurement structure: one EPC per node with an owner's")
    print("          engineer across the program; the pilot aperture and the first module as")
    print("          separate contracts, because no contractor has delivered more than one")
    print("          commercial tower at a time in the US.")
    print()
    print("    F-40  40 dBA at the boundary, computed:")
    print(f"      {'':<40}{'mid':>12}{'critical':>12}")
    nn = {c: noise(c) for c in CASES}
    print(f"      {'source at 1 m, dBA':<40}" + "".join(f"{nn[c]['source']:12.0f}" for c in CASES))
    print(f"      {'boundary distance, open, m':<40}" + "".join(f"{nn[c]['d_open_m']:12,.0f}" for c in CASES))
    print(f"      {'enclosure, dB':<40}" + "".join(f"{nn[c]['enclosure']:12.0f}" for c in CASES))
    print(f"      {'boundary distance, enclosed, m':<40}" + "".join(f"{nn[c]['d_enclosed_m']:12,.0f}" for c in CASES))
    print(f"      {'enclosure cost, $M per module':<40}" + "".join(f"{nn[c]['cost_m']:12,.0f}" for c in CASES))
    print("          Achievable with a full enclosure on a brownfield of the acreage F-27")
    print("          assumes; the cost is now carried.")
    print()


def selftest():
    fails = 0

    def check(label, ok):
        nonlocal fails
        print(f"  {label:<72} {'PASS' if ok else 'FAIL'}")
        fails += 0 if ok else 1

    cl = cycle_label()
    check("the fallback's label is subcritical and its efficiency is helios.ETA_CYCLE", "subcritical" in cl["fallback"] and cl["fallback_eta"] == H.ETA_CYCLE)
    check("the design PGA exceeds the mapped MCE at every node at both cases", all(v[1] > 1.0 for c in CASES for v in seismic(c).values()))
    cc = {c: co2(c) for c in CASES}
    check("the honest CO2 figure is below the 11.8 claimed at both cases", all(cc[c]["closed_mmt"] < CLAIMED_MMT for c in CASES))
    check("critical avoids less than mid", cc["critical"]["closed_mmt"] < cc["mid"]["closed_mmt"])
    jj = {c: jobs(c) for c in CASES}
    check("permanent jobs are computed from a built plant's per-MW figure", abs(jj["mid"]["permanent"] - (jj["mid"]["block_mw"] * PERMANENT_PER_MW[0] + C.design("helios3", "mid")["pv_mw"] * PV_OM_PER_MW)) < 1e-9)
    check("the construction peak is within a factor of two of the claim", 0.5 < jj["mid"]["construction_peak"] / CLAIMED_JOBS[0] < 2.0)
    nn = {c: noise(c) for c in CASES}
    check("the enclosure brings the boundary inside the brownfield at both cases (under 200 m)", all(nn[c]["d_enclosed_m"] < 200.0 for c in CASES))
    check("without an enclosure the boundary is hundreds of metres or more", all(nn[c]["d_open_m"] > 300.0 for c in CASES))
    check("critical needs more distance and costs more", nn["critical"]["d_enclosed_m"] > nn["mid"]["d_enclosed_m"] and nn["critical"]["cost_m"] > nn["mid"]["cost_m"])
    head = open(__file__).read().split("def cycle_label")[0].splitlines()
    consts = [l for l in head if l[:1].isupper() and "=" in l and not l.startswith(("HERE", "CASES")) and not l.startswith(" ")]
    check("every constant line carries a status", all(any(t in l for t in ("SOURCED", "ASSUMED", "Title I", "Title II")) for l in consts))
    import io
    import contextlib
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        report()
    out = buf.getvalue()
    check("the report withdraws 'supercritical' and does not carry the multiplier", "is withdrawn" in out and "is not carried" in out)
    check("the report acknowledges the 2001 authority's history", "defunded by 2004" in out)
    print(f"\nselftest: {fails} failures -> {'PASS' if fails == 0 else 'FAIL'}")
    return fails == 0


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args()
    if a.selftest:
        sys.exit(0 if selftest() else 1)
    report()
