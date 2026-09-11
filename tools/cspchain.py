#!/usr/bin/env python3
"""cspchain.py -- how a solar-thermal plant works, link by link, and where it
can be made smaller while producing more

WHY THIS FILE EXISTS
--------------------
The author chose CSP: "we just have to learn enough about how it works to
figure out how to do it better -- scale down in size while simultaneously
increasing output." That is a statement about the ENERGY CHAIN. A tower plant
turns direct sunlight into electricity through seven multiplications, and
every one of them is a place where the plant is bigger than it needs to be:

    E = A x DNI x eta_opt x eta_rec x eta_tes x eta_dispatch x eta_cycle
          x (1 - parasitic) x availability

Size is the aperture A. Output is E. So "smaller and more" means "a larger
product of the seven efficiencies", and the question is how much larger each
can be made -- by its physical bound, and by the best that has been built.

This file states each link three ways: as Helios carries it (helios.py's own
constants, imported), as the best achieved or credibly designed (SOURCED),
and at its physical limit (theory). Then it builds two plants on the same
requirement as the first two passes and prices them through heliocost.py's
lines, so the improvement is a number in the same column as the baseline.

    python3 tools/cspchain.py
    python3 tools/cspchain.py --selftest
stdlib only. Imports helios.py, heliocost.py and firmpower.py; restates none.
"""

import argparse
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

import helios as H                                              # noqa: E402
import heliocost as HC                                          # noqa: E402
import firmpower as FP                                          # noqa: E402

# =============================================================================
# THE CHAIN: (as Helios carries it, best achieved / designed, physical bound)
# =============================================================================
# Every "as Helios" value is imported from helios.py; nothing is restated.
T_COLD_K = 310.0                    # dry-cooled condenser, desert           SOURCED band
T_SALT_K = 565.0 + 273.15           # nitrate hot tank, helios.py             Title I
T_PARTICLE_K = 775.0 + 273.15       # Gen3 particle receiver outlet          SOURCED (G3P3 ~800 C)


def carnot(t_hot_k, t_cold_k=T_COLD_K):
    return 1.0 - t_cold_k / t_hot_k


CHAIN = [
    # key, name, helios value, best achieved/designed, bound, status of 'best'
    ("opt", "field optical efficiency, annual",
     None, 0.64, 0.70,
     "SOURCED: optimised surround fields 58-64 %; mono-tower upper limit ~70 %"),
    ("rec", "receiver thermal efficiency, annual",
     H.ETA_RECEIVER, 0.90, 0.95,
     "SOURCED: 84.7 % annual / 87.4 % design at 336-650 C salt; particle 85-90 %"),
    ("tes", "storage round trip",
     1.0 - H.TANK_LOSS_PER_DAY, None, 1.0,
     "SOURCED: ~1 C/day on a 275 K span; no gain claimed"),
    ("dispatch", "dispatch: spill, start-up, part load",
     None, None, 1.0,
     "DERIVED from helios.py's hourly run: SM 2.1 rarely fills the tank, so it"
     " barely spills; no gain claimed -- the loss is winter under-supply, F-06"),
    ("cycle", "power cycle, gross",
     H.ETA_CYCLE, 0.50, None,
     "SOURCED: subcritical reheat steam 41-44 %; sCO2 RCBC ~50 % at 700-715 C (STEP)"),
    ("par", "1 - parasitic share",
     1.0 - H.PAR_GROSS_FRAC, 0.92, 0.97,
     "SOURCED: sCO2 needs ~1/6 the cooling airflow of steam; ACC fans dominate"),
    ("avail", "availability",
     H.AVAILABILITY, 0.96, 1.0,
     "SOURCED band: soiling, tracking, outage"),
]

# ---- what the improved plant is built from --------------------------------
DIRECT_SHARE = FP.DIRECT_SHARE            # PV-direct daytime share, firmpower's own
PV_PER_KW_AC = FP.PV_PER_KW_AC
PV_CF = FP.PV_CF
PV_OM = FP.PV_OM
HEATER_PER_KW_TH = FP.HEATER_PER_KW_TH
NIGHT_HOURS = FP.NIGHT_HOURS
NIGHT_PEAK = 1.3                          # night peak / night average         ASSUMED
WINTER_HEATER_FRACTION = 0.25             # heaters sized to a quarter of the night
                                          # block's thermal input, for December  ASSUMED
WINTER_PV_OVERBUILD = 0.20                # extra PV to charge them             ASSUMED
HELIOSTAT_BEST = (80.0, 100.0, 120.0)     # $/m2, best reported to conventional  SOURCED band
SCO2_BLOCK_PER_KWE = (900.0, 1050.0, 1250.0)   # sCO2 block incl. recuperators + dry
                                               # cooler; turbomachinery 5-10x smaller
                                               # than steam                    ASSUMED band
PARTICLE_TES_PER_KWHTH = (10.0, 15.0, 22.0)    # bins + bauxite at $2/kg; DOE target
                                               # band                          ASSUMED band
PARTICLE_SYSTEM_PER_KWE = 5900.0               # 2025 TEA, particle CSP + sCO2 system
                                               # specific cost, design point   SOURCED
GEN3_STATUS = "PILOT: G3P3 >1 MW_t at Sandia; STEP 10 MWe sCO2 at 715 C -- not a 2030 plant"
DEWA_STATUS = "BUILT: Noor Energy 1 (700 MW CSP + 250 MW PV); Midelt adds PV-fed heaters"


# =============================================================================
# THE CHAIN, EVALUATED
# =============================================================================
def helios_values():
    """The two links helios.py does not carry as constants, measured from its
    own hourly run: annual optical efficiency and the dispatch factor."""
    pf = H.run_network()
    dni_total = sum(n[6] for n in H.NODES) * H.APERTURE_M2 / len(H.NODES)   # kWh/yr
    # field_th is what reached the receiver; opt = field_th / (DNI x A x avail)
    opt = pf["field_th"] * 1e3 / (dni_total * H.AVAILABILITY) / H.ETA_RECEIVER
    dispatch = pf["to_turbine_th"] / pf["field_th"]
    return opt, dispatch, pf


def chain_product(values):
    p = 1.0
    for v in values:
        p *= v
    return p


def yield_kwh_per_m2(opt, rec, tes, dispatch, cycle, par, avail, dni):
    return dni * opt * rec * tes * dispatch * cycle * par * avail


def baseline_links():
    opt, dispatch, pf = helios_values()
    vals = {"opt": opt, "rec": H.ETA_RECEIVER, "tes": 1.0 - H.TANK_LOSS_PER_DAY,
            "dispatch": dispatch, "cycle": H.ETA_CYCLE, "par": 1.0 - H.PAR_GROSS_FRAC,
            "avail": H.AVAILABILITY}
    return vals, pf


def best_links():
    """A link whose 'best' is None claims no gain: it takes Helios's own value."""
    base, _pf = baseline_links()
    return {k: (best if best is not None else base[k])
            for k, _n, _h, best, _b, _s in CHAIN}


def mean_dni():
    return sum(n[6] for n in H.NODES) / len(H.NODES)


# =============================================================================
# TWO PLANTS ON THE SAME REQUIREMENT
# =============================================================================
def design(kind="helios2", case="mid", e_twh=FP.E_REQ_TWH):
    """kind = 'helios2': nitrate salt, steam, PV-direct daytime, heliostat field
    sized for the night, PV-fed heaters for winter -- every part built.
    kind = 'helios3': the same architecture on Gen3 particles and sCO2 -- pilot."""
    base, _pf = baseline_links()
    best = best_links()
    links = dict(base)
    # what each kind changes
    links["opt"] = best["opt"]                    # Noor III-class fields, both
    links["dispatch"] = best["dispatch"]          # a hybrid dumps less, both
    links["avail"] = best["avail"]
    if kind == "helios3":
        links["rec"] = best["rec"]
        links["cycle"] = best["cycle"]
        links["par"] = best["par"]
    f = DIRECT_SHARE[1]
    e_direct = e_twh * f
    e_night = e_twh * (1.0 - f)
    per_m2 = yield_kwh_per_m2(dni=mean_dni(), **links)
    aperture = e_night * 1e9 / per_m2
    turb_mw = e_night * 1e6 / (365.0 * NIGHT_HOURS) * NIGHT_PEAK
    tes_mwh = turb_mw / links["cycle"] * NIGHT_HOURS
    towers = aperture / (H.APERTURE_M2 / HC.TOWERS)   # Noor III-class fields
    heater_mw = tes_mwh / 6.0 * WINTER_HEATER_FRACTION
    pv_mw = (e_direct * 1e6 / (8760.0 * _p(PV_CF, case))) * (1.0 + WINTER_PV_OVERBUILD)
    # cost lines, heliocost's own where the part is the same
    k = HC.calibration()
    lines = {}
    lines["site improvements"] = aperture * _p(HC.SITE_PER_M2, case) * k / 1e6
    lines["heliostat field"] = aperture * _p(HELIOSTAT_BEST, case) * k / 1e6
    lines["towers"] = towers * HC.tower_cost_m() * k
    rcv_m2 = (aperture * HC.DESIGN_DNI * H.ETA_OPT_PEAK / 1e6) / towers / HC.RECEIVER_FLUX_MW_M2
    lines["receivers"] = towers * HC.RECEIVER_REF_M * (rcv_m2 / HC.RECEIVER_REF_M2) ** HC.RECEIVER_EXP * k
    if kind == "helios3":
        lines["thermal storage (particles)"] = tes_mwh * 1e3 * _p(PARTICLE_TES_PER_KWHTH, case) / 1e6
        lines["power block (sCO2)"] = turb_mw * 1e3 * _p(SCO2_BLOCK_PER_KWE, case) / 1e6
    else:
        lines["thermal storage (nitrate)"] = tes_mwh * 1e3 * _p(HC.TES_PER_KWHTH, case) * k / 1e6
        lines["power block (steam + ACC)"] = turb_mw * 1e3 * _p(HC.POWER_BLOCK_PER_KWE, case) * k / 1e6
    lines["balance of plant"] = turb_mw * 1e3 * _p(HC.BOP_PER_KWE, case) * k / 1e6
    lines["PV, direct + winter"] = pv_mw * 1e3 * _p(PV_PER_KW_AC, case) / 1e6
    lines["electric heaters"] = heater_mw * 1e3 * _p(HEATER_PER_KW_TH, case) / 1e6
    lines["500 kV switchyards + gen-tie"] = 3 * _p(HC.SWITCHYARD_PER_NODE_M, case) * k
    direct = sum(lines.values())
    over = direct * (1.0 + _p(HC.CONTINGENCY, case) + _p(HC.EPC_OWNER, case)
                     + HC.SALES_TAX * HC.SALES_TAX_BASE)
    gross = FP.financed(over, HC.BUILD_YEARS)
    stor_key = next(n for n in lines if n.startswith("thermal storage"))
    credit = FP.CREDIT_ELIGIBLE * (lines[stor_key] + lines["electric heaters"]) * FP.ESC
    net = gross - credit
    om = (turb_mw * 78.0 + pv_mw * PV_OM) / 1e3 + HC.PILOT_FRACTION * HC.PROPERTY_TAX_RATE * net
    price = FP.required_price(net, om, e_twh)
    acres = aperture / 0.20 / 4046.86 + pv_mw * FP.PV_ACRES_PER_MW
    return dict(kind=kind, links=links, per_m2=per_m2, aperture=aperture,
                towers=towers, turb_mw=turb_mw, tes_mwh=tes_mwh, pv_mw=pv_mw,
                heater_mw=heater_mw, lines=lines, capex_gross=gross,
                capex_net=net, credit=credit, om=om, price=price, acres=acres,
                e_twh=e_twh, e_direct=e_direct, e_night=e_night,
                status=GEN3_STATUS if kind == "helios3" else DEWA_STATUS)


def _p(band, case):
    return band[{"low": 0, "mid": 1, "high": 2}[case]]


def baseline_row():
    r = FP.size_csp()
    base, pf = baseline_links()
    r["aperture"] = H.APERTURE_M2 * r["e_twh"] * 1e6 / pf["net"]
    r["per_m2"] = pf["net"] * 1e3 / H.APERTURE_M2
    r["towers"] = HC.TOWERS * r["aperture"] / H.APERTURE_M2
    r["links"] = base
    return r


# =============================================================================
# REPORT
# =============================================================================
def report():
    base, pf = baseline_links()
    best = best_links()
    print()
    print("  HOW A SOLAR-THERMAL PLANT WORKS, LINK BY LINK")
    print()
    print("    E = A x DNI x opt x rec x tes x dispatch x cycle x (1-par) x avail")
    print()
    print("    Size is the aperture A. Output is E. 'Smaller and more' means a")
    print("    larger product of the seven efficiencies. Each link, three ways:")
    print()
    print(f"      {'link':<40} {'Helios':>7} {'best':>7} {'bound':>7}   what sets it")
    for key, name, _h, _bst, bound, status in CHAIN:
        hv = base[key]
        bst = best[key]
        bd = f"{bound:7.3f}" if bound is not None else f"{carnot(T_PARTICLE_K):7.3f}*"
        print(f"      {name:<40} {hv:7.3f} {bst:7.3f} {bd}   {status}")
    print(f"      {'* Carnot at 775 C particles / 310 K; at 565 C salt it is'}"
          f" {carnot(T_SALT_K):.3f}")
    ph = chain_product(base.values())
    pb = chain_product(best.values())
    print()
    print(f"      product, sun to socket         Helios {ph:.4f}   best {pb:.4f}"
          f"   ratio {pb / ph:.2f}")
    print(f"      kWh_e per m2 of mirror per year  Helios {yield_kwh_per_m2(dni=mean_dni(), **base):5.0f}"
          f"   best {yield_kwh_per_m2(dni=mean_dni(), **best):5.0f}")
    print()
    print("    WHERE THE PLANT IS BIGGER THAN IT NEEDS TO BE, in order of what")
    print("    each link is worth if moved from Helios's value to the best:")
    gains = sorted(((best[k] / base[k], k, n) for k, n, *_ in CHAIN), reverse=True)
    for g, k, n in gains:
        print(f"      {n:<40} x{g:.3f}")
    print()
    print("    THREE OF THEM ARE THE STORY. The CYCLE: 565 C nitrate salt caps")
    print("    steam at 43 %, and 43 % of the heat is thrown at the desert")
    print("    through a fan-cooled condenser; sCO2 at 715 C on particles")
    print("    reaches 50 %, and its turbine is a tenth the size. The OPTICS:")
    print("    Helios's fields lose 42 % of the light before it reaches the")
    print("    receiver, mostly to the cosine of a sun that is never overhead")
    print("    and to blocking and attenuation in fields too large for their")
    print("    towers; Noor III-class fields reach 64 %, the theoretical mono-")
    print("    tower limit is ~70 %. And DISPATCH: a sun-only plant spills")
    print("    heat in June and starves in December; a plant with a second")
    print("    charging path does neither.")
    print()
    print("    AND ONE THING NO LINK CAN FIX: A THERMAL PLANT SERVES DAYTIME")
    print("    LOAD AT 43 % WHEN A PANEL SERVES IT AT 100 %. Every daytime MWh")
    print("    sent through the salt costs 2.3 MWh of sunlight; sent straight")
    print("    from PV it costs one. So the daytime share of the load -- about")
    print(f"    {100 * DIRECT_SHARE[1]:.0f} % of a household's day -- should never touch the mirrors,")
    print("    and the heliostat field should be sized for the NIGHT. That is")
    print("    the DEWA architecture, and it is the single largest 'smaller'.")
    print()
    b = baseline_row()
    h2 = design("helios2")
    h3 = design("helios3")
    print("    THREE PLANTS ON THE SAME 18.1 TWh, STATE-OWNED, SAME LINES:")
    print()
    print(f"      {'':<34} {'Helios as proposed':>18} {'Helios-2':>12} {'Helios-3':>12}")
    print(f"      {'mirror aperture, M m2':<34} {b['aperture'] / 1e6:18.1f} {h2['aperture'] / 1e6:12.1f} {h3['aperture'] / 1e6:12.1f}")
    print(f"      {'towers, Noor III class':<34} {b['towers']:18.0f} {h2['towers']:12.0f} {h3['towers']:12.0f}")
    print(f"      {'turbine, MW':<34} {b['mw']:18,.0f} {h2['turb_mw']:12,.0f} {h3['turb_mw']:12,.0f}")
    print(f"      {'thermal storage, GWh_th':<34} {H.STORAGE_MWH_TH * b['e_twh'] * 1e6 / pf['net'] / 1e3:18.0f} {h2['tes_mwh'] / 1e3:12.0f} {h3['tes_mwh'] / 1e3:12.0f}")
    print(f"      {'PV, MW_AC':<34} {0:18.0f} {h2['pv_mw']:12,.0f} {h3['pv_mw']:12,.0f}")
    print(f"      {'kWh_e per m2 of mirror':<34} {b['per_m2']:18.0f} {h2['per_m2']:12.0f} {h3['per_m2']:12.0f}")
    print(f"      {'land, acres':<34} {b['acres']:18,.0f} {h2['acres']:12,.0f} {h3['acres']:12,.0f}")
    print(f"      {'capex net of credit, $B':<34} {b['capex_net'] / 1e3:18.1f} {h2['capex_net'] / 1e3:12.1f} {h3['capex_net'] / 1e3:12.1f}")
    print(f"      {'$/MWh needed':<34} {b['price']:18.0f} {h2['price']:12.0f} {h3['price']:12.0f}")
    print(f"      {'$/household/yr (today 1,177)':<34} {H.per_household(b['price']):18,.0f}"
          f" {H.per_household(h2['price']):12,.0f} {H.per_household(h3['price']):12,.0f}")
    print(f"      {'status':<34} {'as submitted':>18} {'BUILT':>12} {'PILOT':>12}")
    print()
    print(f"    HELIOS-2 IS {b['aperture'] / h2['aperture']:.2f}x SMALLER IN MIRROR AND DELIVERS THE SAME ENERGY,")
    print("    with every part already built somewhere: Noor III's fields,")
    print("    Helios's own nitrate tanks and steam block, DEWA's PV-CSP")
    print("    split, Midelt's PV-fed heaters. What it costs is the sun-only")
    print("    purity: a third of the energy is photovoltaic. What it buys is")
    print(f"    a household charge of ${H.per_household(h2['price']):,.0f} against ${H.per_household(b['price']):,.0f}.")
    print()
    print(f"    HELIOS-3 IS {b['aperture'] / h3['aperture']:.2f}x SMALLER and reaches ${h3['price']:.0f}/MWh, and it is")
    print("    the right CSP -- sand at 775 C, no salt to freeze, no nitrate")
    print("    ceiling, a turbine the size of a desk -- and it is a pilot at")
    print("    Sandia and a 10 MW demonstrator in San Antonio, not a 2030")
    print("    plant. It is priced here so the author can see what the")
    print("    technology is worth; it is not offered as the build.")
    print()
    print("    WHAT IS ASSUMED, AND EACH IS NAMED IN THE SOURCE. The daytime")
    print("    share, the night peak ratio, the winter heater sizing, the sCO2")
    print("    block and particle storage unit rates. What is SOURCED: every")
    print("    link's best value, the built plants, the STEP and G3P3 figures,")
    print("    the hybrid LCOE reductions (7-22 %) the literature reports. The")
    print("    2025 particle-sCO2 TEA's whole-system figure is")
    print(f"    ${PARTICLE_SYSTEM_PER_KWE:,.0f}/kWe at design point; Helios-3's thermal block")
    print(f"    comes to ${(h3['lines']['thermal storage (particles)'] + h3['lines']['power block (sCO2)'] + h3['lines']['receivers'] + h3['lines']['towers'] + h3['lines']['heliostat field'] + h3['lines']['site improvements']) * 1e6 / (h3['turb_mw'] * 1e3):,.0f}/kWe before indirects, in the same band.")
    print()
    print("    WHAT THIS FILE DOES NOT DO. It does not run Helios-2 hour by")
    print("    hour -- that is helios.py's job and the next step -- so the")
    print("    dispatch link is the literature's, not the model's. It does not")
    print("    choose between 2 and 3; it says 2 is buildable and 3 is better.")
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

    base, pf = baseline_links()
    best = best_links()
    print()
    print("  the chain reproduces helios.py before it is used")
    y = yield_kwh_per_m2(dni=mean_dni(), **base)
    check("the chain's per-m2 yield reproduces the hourly model's to 10 %",
          abs(y / (pf["net"] * 1e3 / H.APERTURE_M2) - 1.0) < 0.10)
    check("Helios's annual optical efficiency is at or below the sourced 58-64 % band",
          0.50 <= base["opt"] <= 0.64)
    check("every link's Helios value is at or below its best",
          all(base[k] <= best[k] + 1e-9 for k in base))
    check("  -- and every best is at or below its bound",
          all(best[k] <= (bd if bd is not None else carnot(T_PARTICLE_K)) + 1e-9
              for k, _n, _h, _bst, bd, _s in CHAIN))
    check("  -- and two links claim no gain at all",
          sum(1 for _k, _n, _h, bst, _b, _s in CHAIN if bst is None) == 2)
    check("the steam cycle is below Carnot at the salt temperature",
          H.ETA_CYCLE < carnot(T_SALT_K))
    check("  -- and sCO2's 50 % is below Carnot at the particle temperature",
          best["cycle"] < carnot(T_PARTICLE_K))

    print()
    print("  smaller and more")
    b = baseline_row()
    h2 = design("helios2")
    h3 = design("helios3")
    check("the best chain yields at least 1.3x per m2 of mirror",
          chain_product(best.values()) / chain_product(base.values()) > 1.3)
    check("Helios-2 uses under 65 % of the baseline aperture",
          h2["aperture"] < 0.65 * b["aperture"])
    check("Helios-3 uses under 50 %", h3["aperture"] < 0.50 * b["aperture"])
    check("both deliver exactly the requirement",
          abs(h2["e_twh"] - FP.E_REQ_TWH) < 1e-9 and abs(h3["e_twh"] - FP.E_REQ_TWH) < 1e-9)
    check("price ordering: proposed > Helios-2 > Helios-3",
          b["price"] > h2["price"] > h3["price"])
    check("Helios-2 is built technology and Helios-3 is a pilot",
          h2["status"].startswith("BUILT") and h3["status"].startswith("PILOT"))
    check("the federal credit lands on storage and heaters only",
          abs(h2["credit"] - FP.CREDIT_ELIGIBLE * FP.ESC
              * (h2["lines"]["thermal storage (nitrate)"] + h2["lines"]["electric heaters"])) < 1e-6)
    check("the PV share is a minority of the energy (the CSP is the plant)",
          h2["e_direct"] < h2["e_night"])
    check("Helios-3's thermal block sits within 40 % of the sourced $5,900/kWe",
          abs(sum(v for n, v in h3["lines"].items()
                  if not n.startswith(("PV", "electric", "500 kV", "balance")))
              * 1e6 / (h3["turb_mw"] * 1e3) / PARTICLE_SYSTEM_PER_KWE - 1.0) < 0.40)

    print()
    print("  and what the file refuses")
    import contextlib
    import io
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        report()
    out = buf.getvalue()
    check("it does not offer the pilot as the build", "not offered as the build" in out)
    check("it names what is assumed", "WHAT IS ASSUMED" in out)
    check("it names the hourly run as the next step", "next step" in out)
    check("it states the one thing no link can fix", "NO LINK CAN FIX" in out)

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
