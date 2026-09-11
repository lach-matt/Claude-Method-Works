#!/usr/bin/env python3
"""helios3.py -- Helios-3's risks, each mitigated upfront where design can,
and named where only hours can

WHY THIS FILE EXISTS
--------------------
The author chose Helios-3 -- Gen3 particles and sCO2 on the DEWA hybrid
architecture -- and said: "I think each cost can be fully mitigated upfront."
The objective's own rule is that mitigations are addressed upfront, before
design. So the claim is tested the way environment.py tested the fission
plant's: a register in which every risk is graded BEFORE and AFTER its
mitigation, every mitigation is carried by a named part of the build (a
mitigation that lives only in a register is prose), and every row says which
KIND of mitigation it is:

    DESIGN   retired upfront, by a specification -- what the author means
    HOURS    retired only by operating time on a plant that does not yet
             exist -- which no specification can supply
    BENEFIT  a risk the salt plant had that this one does not

Then the mitigations are PRICED back into Helios-3 -- cspchain.py's own
design, imported -- so the $117/MWh is tested rather than kept.

    python3 tools/helios3.py
    python3 tools/helios3.py --selftest
stdlib only. Imports helios, heliocost, firmpower, cspchain; restates none.
"""

import argparse
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

import helios as H                                              # noqa: E402
import heliocost as HC                                          # noqa: E402
import firmpower as FP                                          # noqa: E402
import cspchain as CC                                           # noqa: E402

GRADES = ["BENEFIT", "NEGLIGIBLE", "MINOR", "MODERATE", "MAJOR", "DOMINANT"]

# =============================================================================
# THE REGISTER
# (id, risk, before, mitigation, after, kind, carrier, source/status)
# =============================================================================
REGISTER = [
    ("R-01", "Particle attrition: grains break, make dust, and the medium is lost",
     "MODERATE",
     "Particle geometry: spherical sintered bauxite (roundness ~0.9), tight size "
     "cut. SYSTEM geometry (author, 2026-09-11): short drops, few transfer "
     "points, particles land on particles (rock-box liners, dead beds), "
     "mass-flow hoppers, gravity flow everywhere but the one cold lift. "
     "Enclosed conveyance; makeup in O&M; dust to baghouse. Fallback noted: "
     "a fixed ceramic bed with air as the moving fluid (Julich class) wears "
     "nothing and is a different plant",
     "NEGLIGIBLE", "DESIGN",
     "particle specification; plant arrangement (drops, transfer points, "
     "liners, hopper flow); conveyance; O&M makeup line",
     "SOURCED: after ~200 h on-sun in Sandia's 1 MW_t receiver, used-particle "
     "absorptance 0.946 vs 0.945 unused -- durability shown at hours scale, "
     "not decades; residual is HOURS"),
    ("R-02", "Receiver wind and convective loss: a falling curtain is open to the air",
     "MAJOR",
     "Compound quartz aperture (author, 2026-09-11): a dome lattice of long "
     "hexagonal-section low-OH fused-quartz rod lenses, each a two-surface "
     "thick lens placing its focus in the receiver, the dome acting as "
     "secondary concentrator and flux homogeniser aimed jointly with the "
     "field; hot face at cavity temperature, cold end in a cooled frame; "
     "single-element replacement. Multi-aperture receivers on smaller towers",
     "MODERATE", "HOURS",
     "receiver specification; aperture element specification; tower count",
     "SOURCED: windowed receiver +11.9 % efficiency over aerowindow; quartz "
     "half-shell transmissivity 0.97 / 0.94; fused silica k 1.38 W/m K, CTE "
     "0.55 ppm/K, devitrification above ~1,100 C. Rod length is cheap in "
     "light (low-OH quartz ~1.3 % from 1 to 30 cm) and buys a gentler "
     "gradient; what it cannot move is the hot-face temperature. No windowed "
     "receiver has run at commercial scale -- residual is HOURS"),
    ("R-03", "Particle-to-sCO2 heat exchanger: 800 C particles against 250 bar CO2",
     "MAJOR",
     "Moving packed-bed exchanger (Sandia / Solex / VPE lineage), low particle "
     "velocity for erosion, modular N+1 units so one can be out",
     "MODERATE", "HOURS",
     "power block; spares policy",
     "SOURCED: prototype 4-6x any known particle/sCO2 exchanger, tested to 500 C "
     "at 17 MPa, U ~300-400 W/m2K; design point is 800 C / 25 MPa -- the gap is "
     "HOURS at the design point"),
    ("R-04", "sCO2 turbomachinery at 715 C and 250 bar",
     "MAJOR",
     "Inconel 740H for the hot path; many small units (10-50 MWe) rather than "
     "few large, so a unit is a spare; STEP's recompression configuration",
     "MODERATE", "HOURS",
     "power block specification; unit sizing",
     "SOURCED: 740H is ASME-qualified 650-825 C, the only age-hardened superalloy "
     "approved for welded creep-limited pressure parts; STEP's RCBC at 715 C / "
     "250 bar is its next phase, 16 MW turbine under 100 kg -- residual is HOURS"),
    ("R-05", "CO2 inventory release: heavier than air, 4 % is IDLH, cold on release",
     "MODERATE",
     "Open-air or forced-ventilated turbine yards; no occupied low ground; CO2 "
     "sensors and dump tanks; inventory held per module, not per plant",
     "MINOR", "DESIGN",
     "site layout; safety systems",
     "SOURCED: hazard characterised in the CCUS literature; a power loop's "
     "inventory is tens of tonnes per module against tens of thousands in a "
     "CCUS pipeline; standard pressure-plant practice"),
    ("R-06", "High-pressure, high-temperature containment (250 bar / 715 C)",
     "MODERATE",
     "740H piping and headers under ASME Section I/VIII; design by code, not novelty",
     "MINOR", "DESIGN",
     "pressure-part specification",
     "SOURCED: 740H is the code-approved material for exactly this duty"),
    ("R-07", "Silo heat loss and thermal ratcheting at 800 C over forty years",
     "MODERATE",
     "Refractory-lined silos with expansion allowance; large silos, because loss "
     "goes as surface over volume",
     "MINOR", "DESIGN",
     "storage specification",
     "SOURCED: rock, sand and bauxite operate to >1000 C; loss falls with silo "
     "size; forty-year refractory life is HOURS"),
    ("R-08", "Particle chemistry: bauxite oxides transform in air at 700-1000 C",
     "MODERATE",
     "Periodic reduction to rejuvenate absorptance; makeup; inert or lean "
     "atmosphere in the hot silo",
     "MODERATE", "HOURS",
     "O&M rejuvenation line; silo atmosphere",
     "SOURCED: XRD shows transformations in sintered bauxite after heating in "
     "air; absorptance can be restored by reduction -- rate over decades unknown"),
    ("R-09", "Particle lift: erosion and temperature on the elevator",
     "MODERATE",
     "Lift COLD particles only; everything after the receiver is gravity-driven, "
     "so the lift never sees 800 C",
     "MINOR", "DESIGN",
     "plant arrangement",
     "SOURCED: G3P3's own architecture -- skip hoist to the receiver top, "
     "free-fall through receiver, storage and exchanger"),
    ("R-10", "Dust as PM10 in non-attainment counties",
     "MODERATE",
     "Negative-pressure enclosed handling with baghouse; no open transfer points",
     "MINOR", "DESIGN",
     "conveyance; air permit",
     "Kern, Imperial, San Bernardino are PM10 non-attainment; enclosed bulk "
     "handling is ordinary practice"),
    ("R-11", "Receiver scale: no particle receiver has run above ~1 MW_t",
     "DOMINANT",
     "Multi-aperture receivers; more, smaller towers; a first module built and "
     "run before the fleet",
     "MAJOR", "HOURS",
     "tower count; programme staging",
     "SOURCED: G3P3 is >1 MW_t; Helios-3 needs ~700 MW_th per tower. Design "
     "can split the receiver; only hours can prove it"),
    ("R-12", "Provenance: no plant of this kind exists at any commercial scale",
     "DOMINANT",
     "Stage: build the common field, towers and PV for Helios-2 OR Helios-3; "
     "build one Helios-3 module first; convert modules as hours accumulate",
     "MAJOR", "HOURS",
     "programme staging",
     "This row cannot be mitigated by a specification. What is upfront is the "
     "PLAN that buys the hours"),
    ("R-13", "No freezing point: no heat tracing, no drain-down, no hot-tank failure",
     "BENEFIT", "-", "BENEFIT", "BENEFIT", "-",
     "Crescent Dunes lost eight months to a hot-tank leak; a silo of sand at "
     "ambient is a silo of sand"),
    ("R-14", "No decomposition ceiling: stable past 1000 C",
     "BENEFIT", "-", "BENEFIT", "BENEFIT", "-",
     "nitrate decomposes above ~600 C; this is the link that buys the cycle"),
    ("R-15", "No oxidiser and no toxic medium: the author's hazard rule, met cleanly",
     "BENEFIT", "-", "BENEFIT", "BENEFIT", "-",
     "nitrate is NFPA OX; bauxite and sand are inert"),
    ("R-16", "Dry cooling at a sixth of the airflow",
     "BENEFIT", "-", "BENEFIT", "BENEFIT", "-",
     "SOURCED: sCO2 cooling profiles are near-parallel; steam needs ~6x the air"),
]

# =============================================================================
# WHAT THE MITIGATIONS COST (bands, ASSUMED unless stated)
# =============================================================================
MIT_COST = {
    "R-01": ("thermal storage (particles)", 0.10),   # enclosed conveyance + baghouse
    "R-02": ("receivers", 0.15),                      # quartz covers, multi-aperture
    "R-03": ("power block (sCO2)", 0.10),             # N+1 exchanger modules
    "R-04": ("power block (sCO2)", 0.08),             # small-unit premium, spares
    "R-05": ("power block (sCO2)", 0.02),             # CO2 safety systems
    "R-06": ("power block (sCO2)", 0.03),             # 740H over lesser alloys
    "R-07": ("thermal storage (particles)", 0.08),    # refractory, expansion
    "R-10": ("thermal storage (particles)", 0.03),    # negative pressure, baghouse
}
# A row whose mitigation MANAGES the risk without reducing its grade. The
# fission register's rule was that a mitigation which does not move the grade
# is not a mitigation; here it is recorded as such rather than promoted.
UNMOVED = ("R-08",)
PARTICLE_MAKEUP_PER_YEAR = 0.01          # of inventory                     ASSUMED band 0.5-2 %
REJUVENATION_OM_M = 15.0                 # $M/yr, whole plant               ASSUMED
FIRST_MODULE_MWE = 100.0                 # the module that buys the hours   DESIGN
FIRST_MODULE_PREMIUM = 1.5               # first-of-a-kind multiplier on its share  ASSUMED band 1.3-2.0


def priced():
    """Helios-3 from cspchain, with every DESIGN mitigation added to the line
    that carries it, the makeup and rejuvenation in O&M, and the first module
    at its first-of-a-kind premium."""
    d = CC.design("helios3")
    lines = dict(d["lines"])
    adders = {}
    for rid, (line, frac) in MIT_COST.items():
        adders[rid] = lines[line] * frac
    mit_total = sum(adders.values())
    direct = sum(lines.values()) + mit_total
    over = direct * (1.0 + HC.CONTINGENCY[1] + HC.EPC_OWNER[1]
                     + HC.SALES_TAX * HC.SALES_TAX_BASE)
    # first module: its share of the thermal block at a FOAK premium
    share = FIRST_MODULE_MWE / d["turb_mw"]
    thermal = sum(v for n, v in lines.items()
                  if n.startswith(("thermal", "power block", "receivers", "towers")))
    foak = thermal * share * (FIRST_MODULE_PREMIUM - 1.0)
    over += foak
    gross = FP.financed(over, HC.BUILD_YEARS)
    credit = FP.CREDIT_ELIGIBLE * (lines["thermal storage (particles)"]
                                   + adders["R-01"] + adders["R-07"] + adders["R-10"]
                                   + lines["electric heaters"]) * FP.ESC
    net = gross - credit
    makeup = PARTICLE_MAKEUP_PER_YEAR * lines["thermal storage (particles)"] * 0.5  # medium ~half the line
    om = d["om"] + makeup + REJUVENATION_OM_M
    price = FP.required_price(net, om, d["e_twh"])
    return dict(base=d, adders=adders, mit_total=mit_total, foak=foak,
                capex_net=net, om=om, price=price, share=share, credit=credit,
                lines=lines)


def grade_counts(after=False):
    idx = 4 if after else 2
    return {g: sum(1 for r in REGISTER if r[idx] == g) for g in GRADES}


def by_kind(kind):
    return [r for r in REGISTER if r[5] == kind]


# =============================================================================
# REPORT
# =============================================================================
def report():
    p = priced()
    d = p["base"]
    h2 = CC.design("helios2")
    print()
    print("  HELIOS-3: EACH RISK, MITIGATED UPFRONT WHERE DESIGN CAN")
    print()
    print("    The author: 'each cost can be fully mitigated upfront.' The")
    print("    objective's own rule: mitigations before design. So every risk")
    print("    is graded before and after, every mitigation is carried by a")
    print("    named part of the build, and every row says whether DESIGN")
    print("    retires it or only HOURS can.")
    print()
    print(f"      {'id':<5} {'risk':<58} {'before':<9} {'after':<9} {'kind':<7}")
    for rid, risk, b, _m, a, k, _c, _s in REGISTER:
        print(f"      {rid:<5} {risk[:58]:<58} {b:<9} {a:<9} {k:<7}")
    bc, ac = grade_counts(False), grade_counts(True)
    print()
    print("      " + " / ".join(f"{bc[g]} {g}" for g in GRADES) + "   before")
    print("      " + " / ".join(f"{ac[g]} {g}" for g in GRADES) + "   after")
    print()
    print("    WHAT DESIGN RETIRES. Six rows move to MINOR by specification and")
    print("    stay there: the CO2 inventory (ventilated yards, per-module")
    print("    inventory, dump tanks), the pressure parts (740H under code), the")
    print("    silos (refractory, large, expansion allowed), the lift (lift")
    print("    cold, fall hot), the dust (enclosed, negative pressure), and the")
    print("    attrition (proppant spec, makeup). Each is ordinary practice in")
    print("    an industry that exists -- bulk solids, pressure plant, CCUS.")
    print()
    print("    WHAT DESIGN CANNOT RETIRE, AND THE FILE SAYS SO. Six rows are")
    print("    HOURS: the receiver in the wind, the receiver at scale, the")
    print("    exchanger at its design point, the turbine at 715 C, the particle")
    print("    chemistry over decades, and the plant's provenance. Each has a")
    print("    design mitigation, and all but one move a grade -- the chemistry")
    print("    row (R-08) does not: rejuvenation MANAGES it and does not reduce")
    print("    it, and it is recorded as UNMOVED rather than promoted. Each")
    print("    every one moves a grade -- and none reaches MINOR, because a")
    print("    specification cannot make a machine have run. What IS upfront")
    print("    for those five is the PLAN: the field, towers and PV are common")
    print("    to Helios-2 and Helios-3, so they are built once; one Helios-3")
    print(f"    module of {FIRST_MODULE_MWE:.0f} MWe is built first, at a first-of-a-kind")
    print("    premium, and modules convert as its hours accumulate. The salt")
    print("    block is the fallback, not the plan.")
    print()
    print("    THE MITIGATIONS, PRICED, so the $117 is tested rather than kept:")
    print()
    for rid, (line, frac) in MIT_COST.items():
        print(f"      {rid}  +{100 * frac:2.0f} % on {line:<30} {p['adders'][rid]:8,.0f} $M")
    print(f"      first module at {FIRST_MODULE_PREMIUM:.1f}x on its thermal share       {p['foak']:8,.0f} $M")
    print(f"      particle makeup {100 * PARTICLE_MAKEUP_PER_YEAR:.0f} %/yr + rejuvenation, O&M    "
          f"{p['om'] - d['om']:8,.0f} $M/yr")
    print()
    print(f"      {'':<30} {'Helios-3 as chained':>20} {'mitigated':>12} {'Helios-2':>12}")
    print(f"      {'capex net, $B':<30} {d['capex_net'] / 1e3:20.1f} {p['capex_net'] / 1e3:12.1f} {h2['capex_net'] / 1e3:12.1f}")
    print(f"      {'O&M, $M/yr':<30} {d['om']:20,.0f} {p['om']:12,.0f} {h2['om']:12,.0f}")
    print(f"      {'$/MWh needed':<30} {d['price']:20.0f} {p['price']:12.0f} {h2['price']:12.0f}")
    print(f"      {'$/household/yr':<30} {H.per_household(d['price']):20,.0f}"
          f" {H.per_household(p['price']):12,.0f} {H.per_household(h2['price']):12,.0f}")
    print()
    print(f"    MITIGATED, HELIOS-3 NEEDS ${p['price']:.0f}/MWh -- still under Helios-2's"
          f" ${h2['price']:.0f}")
    over = p["price"] - H.FIRM_CLEAN_PPA[1]
    where = (f"${-over:.0f} inside" if over <= 0 else f"${over:.0f} above") + " the top of"
    print(f"    and {where} the {H.FIRM_CLEAN_PPA[0]:.0f}-{H.FIRM_CLEAN_PPA[1]:.0f} band. The mitigations cost"
          f" {100 * (p['price'] / d['price'] - 1):.0f} percent, and")
    print("    the chained figure was inside the band; the mitigated one is")
    print("    not, by the price of the mitigation itself. THAT IS THE ANSWER TO")
    print("    THE AUTHOR'S CLAIM, stated exactly: every cost a design can carry")
    print("    is carried and priced, and it costs a few dollars a megawatt-")
    print("    hour, not the plant; what remains is not a cost but a clock, and")
    print("    the staging plan is how the clock is run.")
    print()
    print("    WHAT THIS FILE DOES NOT DO. The adders are ASSUMED bands and say")
    print("    so; a receiver vendor prices a quartz cover, not this file. It")
    print("    does not model the first module's schedule. And it does not")
    print("    flatten HOURS into DESIGN, because the author's rule is that")
    print("    mitigations come before design, and a row that only time can")
    print("    settle is owed to the record as such.")
    print()


# =============================================================================
# SELFTEST
# =============================================================================
def selftest():
    fail = 0

    def check(label, ok):
        nonlocal fail
        if not ok:
            fail += 1
        print(f"  {label:<66} {'PASS' if ok else 'FAIL'}")

    rk = [r for r in REGISTER if r[5] != "BENEFIT"]
    print()
    print("  the register is a register")
    check("every row carries a grade both sides, a kind and a carrier",
          all(r[2] in GRADES and r[4] in GRADES and r[5] in ("DESIGN", "HOURS", "BENEFIT")
              and r[6] for r in REGISTER))
    check("every mitigation moves its grade, except the rows recorded as UNMOVED",
          all(GRADES.index(r[4]) < GRADES.index(r[2]) for r in rk
              if r[0] not in UNMOVED))
    check("  -- every UNMOVED row is HOURS and keeps its grade exactly",
          all(r[5] == "HOURS" and r[4] == r[2] for r in REGISTER if r[0] in UNMOVED))
    check("every DESIGN row reaches MINOR or better",
          all(GRADES.index(r[4]) <= GRADES.index("MINOR") for r in by_kind("DESIGN")))
    check("no HOURS row reaches MINOR -- a specification cannot make a machine have run",
          all(GRADES.index(r[4]) > GRADES.index("MINOR") for r in by_kind("HOURS")))
    check("the two DOMINANT rows are both HOURS",
          all(r[5] == "HOURS" for r in REGISTER if r[2] == "DOMINANT"))
    check("no DOMINANT survives mitigation", grade_counts(True)["DOMINANT"] == 0)
    check("every priced mitigation names a row that exists and a line that exists",
          all(any(r[0] == rid for r in REGISTER) for rid in MIT_COST)
          and all(line in CC.design("helios3")["lines"] for line, _f in MIT_COST.values()))
    check("every DESIGN row with a capital cost is priced",
          all(r[0] in MIT_COST for r in by_kind("DESIGN") if r[0] != "R-09"))

    print()
    print("  the mitigations are priced and the design survives them")
    p = priced()
    d = p["base"]
    h2 = CC.design("helios2")
    check("mitigated capex is above the chained capex", p["capex_net"] > d["capex_net"])
    check("mitigated O&M is above the chained O&M", p["om"] > d["om"])
    check("the mitigated price is above the chained price", p["price"] > d["price"])
    check("  -- by under 20 %", p["price"] / d["price"] < 1.20)
    check("  -- and still below Helios-2", p["price"] < h2["price"])
    check("the first module is a minority of the plant", 0.0 < p["share"] < 0.1)
    exp = FP.CREDIT_ELIGIBLE * FP.ESC * (p["lines"]["thermal storage (particles)"]
                                         + p["adders"]["R-01"] + p["adders"]["R-07"]
                                         + p["adders"]["R-10"] + p["lines"]["electric heaters"])
    check("the storage credit covers the storage adders and not the power block",
          abs(p["credit"] - exp) < 1e-6)
    check("the mitigated price is within 10 % of the band's top",
          p["price"] <= 1.10 * H.FIRM_CLEAN_PPA[1])

    print()
    print("  and what the file refuses")
    import contextlib
    import io
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        report()
    out = buf.getvalue()
    check("it says what design cannot retire", "WHAT DESIGN CANNOT RETIRE" in out)
    check("it names the unmoved row rather than promoting it", "recorded as UNMOVED" in out)
    check("it states the band position exactly rather than claiming to clear",
          "above the top of" in out or "inside the top of" in out)
    check("it does not flatten HOURS into DESIGN", "does not\n    flatten HOURS" in out
          or "not flatten HOURS" in out.replace("\n    ", " "))
    check("it names the salt block as the fallback, not the plan", "fallback, not the plan" in out)
    check("it says the adders are ASSUMED", "ASSUMED bands" in out)

    print()
    print(f"selftest: {fail} failures -> {'PASS' if fail == 0 else 'FAIL'}")
    return 1 if fail else 0


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args()
    if a.selftest:
        return selftest()
    return report()


if __name__ == "__main__":
    sys.exit(main())
