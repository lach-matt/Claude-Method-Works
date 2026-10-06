#!/usr/bin/env python3
"""
stockdest.py -- the stock gate at a real destination (M-RULINGS item 88, link 4: D25 / W3-O3 at Proxima).  READ where
sources exist, deduced, computed.  Not seated; not verified.  M's words are carried as hypotheses, never as results.

The faithful copy (item 87) is built at position 2 "with what it has" (item 86, answer 7).  faithful.py sized what
crosses; this asks whether what it is built FROM is there.  The board's gate (stock.py, audited by stockgate.py --
both imported, never retyped): B is admissible iff within the arrival aperture there is a condensed, primitive body
holding M(p, s) x m_payload of accessible mass, M(p, s) = max_e p_e / s_e (one element binds).

WHAT FOLLOWS THE WORK
  * QUANTITY IS NEVER THE OBSTACLE.  A 70 kg copy needs 749 kg of CI-chondrite-like feedstock (phosphorus binds at
    10.7 kg per kg), 32 t of an Earth-like continental crust (nitrogen binds at 459 kg per kg; 1.2 t if the volatiles
    N, C, H come from elsewhere, when phosphorus binds at 17), or 134 t of stellar photosphere.  Proxima holds two
    confirmed condensed bodies, b (1.07 Earth masses, minimum) and d (0.26, minimum): each exceeds the largest of
    these needs by about nineteen orders.
  * UNDER M'S ANSWER 4 THE GATE BECOMES A SITING CONDITION.  If the second position is an input the device requires
    (H-ADDRESS-INPUT) and a builder must be at the destination (the board's B-RECV), the arrival aperture is where
    that builder stands: the gate asks only that it stand on a body with the feedstock.  The aperture the board left
    without a value (D25: "the arrival coordinate does not yet carry" an orbital radius) gets one: the device's site.
  * WHAT IS NOT KNOWN IS COMPOSITION.  Neither planet's composition is measured (no transit); the discovery paper
    itself names both outcomes -- migrated bodies "would be volatile rich", pebble migration "would produce much
    drier worlds".  That is exactly the gate's fork: volatile-rich, the copy binds on phosphorus near the crust's 17
    kg per kg; dry, nitrogen, carbon and hydrogen must come from somewhere else on the site.
  * Boundary (item 82): a primitive small-body reservoir at Proxima -- the best feedstock -- is not shown.  The dust
    belt reported at 1-4 au (total about 0.01 Earth masses) was attributed by a reanalysis to a stellar flare ("no need
    to invoke the presence of a dust belt at 1-4 AU"); an outer belt at about 30 au stays marginal.  Diffuse
    interstellar gas (CONTRAST) would need 8e25 m^3 swept per copy: the gate's condensed-body clause is real.

    python3 stockdest.py             report
    python3 stockdest.py --selftest  checks, CONTROLS and CONTRASTS marked, STRUCTURAL printed and not counted
    python3 stockdest.py --json      the numbers as JSON

SOURCES READ (2026-10-06; alphaXiv answer_pdf_queries, open arXiv copies, printed pages)
  Anglada-Escude et al. 1609.03449v1 (Nature 536, 437): Proxima b, P = 11.186 d, a = 0.0485 au, m sin i = 1.27
    [1.10, 1.46] M_earth (Table 1, p.10); no transit found (p.5); "While migrated planets and embryos originating
    beyond the ice-line would be volatile rich, pebble migration would produce much drier worlds" (pp.5-6).
  Faria et al. 2202.05188v1 (A&A): Proxima d, P = 5.122 d, a = 0.02885 au, m sin i = 0.26 +/- 0.05 M_earth (abstract,
    p.1; Table C.1, p.17); Proxima b re-measured at 1.07 +/- 0.06 M_earth (p.9, Table C.1); Proxima c (5.21 yr) "has so
    far eluded a clear detection with direct imaging or astrometry" (p.1).
  Anglada et al. 1711.00578v1 (ApJL): a belt "at distances ranging between 1 and 4 au", "estimated total mass,
    including dust and bodies up to 50 km in size, is of the order of 0.01 Earth masses" (abstract, p.1); an outer
    belt at about 30 au and a compact source, both marginal (p.1).
  MacGregor et al. 1802.08257v1 (ApJL): the ACA emission is a flare; "we conclude that there is no need to invoke the
    presence of a dust belt at 1-4 AU" (abstract, p.1; p.7); the warm dust's need "is also removed" if the 12-m excess
    is coronal (p.1); the 30 au belt: "caution should be used in over-interpreting this marginal result" (p.7).

NAMED HYPOTHESES AND PREMISES
  H-ADDRESS-INPUT (M's, item 86); B-RECV (the board's: a holder must be at the destination); H-SITE: the builder at
    position 2 can reach the accessible layer of the body it stands on.
  H-EARTHLIKE-CRUST: a rocky planet's accessible layer has Rudnick & Gao's continental-crust composition (stock.py's
    CRUST, atmosphere excluded) -- one reservoir of one planet, not a measurement of Proxima's.
  H-VOLATILES-ELSEWHERE: the dry branch, where N, C and H are supplied from outside the crust (an atmosphere, ices).
  M_EARTH = 5.9722e24 kg (the IAU 2015 nominal value; a standard constant, not READ this pass).
  The payload: stockgate.py's "as-composed 59" reference adult (imported).

OPEN
  1. The composition of Proxima b or d (a transit or emission spectrum; direct imaging).
  2. A primitive small-body reservoir at Proxima (the 30 au belt, marginal).
  3. The binder phosphorus in Proxima's photosphere (W3-O3).
  4. Separation energy: stockgate.py prices mass, not the energy to extract it.
"""
import contextlib
import importlib.util
import io
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
WD = os.path.dirname(os.path.dirname(HERE))

M_EARTH = 5.9722e24                    # kg, IAU 2015 nominal (standard constant, not READ this pass)
PAYLOAD_KG = 70.0
PKIND = "as-composed 59"

# READ (see SOURCES)
PROXIMA_B_MSINI = 1.07                 # M_earth, Faria Table C.1 (TM RVs); Anglada-Escude 1.27
PROXIMA_D_MSINI = 0.26                 # M_earth, Faria abstract
DUST_BELT_CLAIM_ME = 0.01              # M_earth, Anglada 2017 -- WITHDRAWN as unneeded (MacGregor 2018)


def _owners():
    saved = list(sys.path)
    try:
        sys.path.insert(0, WD)
        with contextlib.redirect_stdout(io.StringIO()):
            mods = {}
            for name in ("stock", "stockgate"):
                spec = importlib.util.spec_from_file_location("wd_" + name + "_sd", os.path.join(WD, name + ".py"))
                m = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(m)
                mods[name] = m
    finally:
        sys.path[:] = saved
    return mods


def compute():
    o = _owners()
    sg, st = o["stockgate"], o["stock"]
    p = sg.payload("as-composed")
    res = {}
    for dkind in ("CI chondrite", "Earth cont. crust", "stellar photosphere"):
        binder, factor = sg.binding_under(PKIND, dkind)
        res[dkind] = {"binder": binder, "factor": factor, "feedstock_kg": sg.feedstock_kg(PAYLOAD_KG, PKIND, dkind)}
    crust_ranked = sg.ranked(p, sg.DESTS["Earth cont. crust"](), 6)
    dry = [(e, f) for e, f in crust_ranked if e not in ("N", "C", "H")][0]
    res["crust, volatiles elsewhere"] = {"binder": dry[0], "factor": dry[1], "feedstock_kg": dry[1] * PAYLOAD_KG}
    need_max = max(v["feedstock_kg"] for v in res.values())
    bodies = {"Proxima b (m sin i)": PROXIMA_B_MSINI * M_EARTH, "Proxima d (m sin i)": PROXIMA_D_MSINI * M_EARTH}
    ism_v, ism_r = st.ism_sweep_volume(PAYLOAD_KG)
    s_noP = dict(sg.DESTS["CI chondrite"]())
    s_noP.pop("P", None)
    noP = sg.processing_factor(p, s_noP)
    return {"reservoirs": res, "crust_ranked": crust_ranked, "no_P_control": noP, "need_max_kg": need_max, "bodies_kg": bodies,
            "orders_over_need": {k: v / need_max for k, v in bodies.items()},
            "dust_belt_claim_kg": DUST_BELT_CLAIM_ME * M_EARTH, "ism_sweep_m3": ism_v, "ism_sweep_radius_m": ism_r}


def report():
    d = compute()
    print("stockdest.py -- the stock gate at Proxima (M item 88, link 4; not verified; not seated)\n")
    for k, v in d["reservoirs"].items():
        print("  %-28s binder %-2s %8.2f kg per kg   feedstock for 70 kg: %.4g kg" % (
            k, v["binder"], v["factor"], v["feedstock_kg"]))
    print("  crust ranking: %s" % ", ".join("%s %.1f" % ef for ef in d["crust_ranked"]))
    for k, v in d["bodies_kg"].items():
        print("  %s: %.3e kg = %.2e x the largest need" % (k, v, d["orders_over_need"][k]))
    print("  contrast: diffuse interstellar gas, %.2e m^3 per copy (radius %.2e m)" % (
        d["ism_sweep_m3"], d["ism_sweep_radius_m"]))


def selftest():
    n_pass = n_fail = n_ctl = n_con = 0
    structural = []

    def chk(label, ok, ctl=False, contrast=False):
        nonlocal n_pass, n_fail, n_ctl, n_con
        n_ctl += ctl
        n_con += contrast
        n_pass += bool(ok)
        n_fail += (not ok)
        print("  %s %s%s" % ("ok  " if ok else "FAIL", "CONTROL: " if ctl else ("CONTRAST: " if contrast else ""), label))

    d = compute()
    r = d["reservoirs"]
    chk("the owners' gate, imported: a CI chondrite binds on %s at %.2f kg per kg (749 kg for 70 kg), a stellar "
        "photosphere on %s at %.0f" % (r["CI chondrite"]["binder"], r["CI chondrite"]["factor"],
                                       r["stellar photosphere"]["binder"], r["stellar photosphere"]["factor"]),
        r["CI chondrite"]["binder"] == "P" and abs(r["CI chondrite"]["feedstock_kg"] - 749.08) < 0.5)
    chk("an Earth-like crust binds on the volatile N (%.0f kg per kg); with N, C, H supplied elsewhere it binds on %s "
        "at %.1f -- the fork the discovery paper names (volatile-rich or dry)" % (
            r["Earth cont. crust"]["factor"], r["crust, volatiles elsewhere"]["binder"],
            r["crust, volatiles elsewhere"]["factor"]),
        r["Earth cont. crust"]["binder"] == "N" and r["crust, volatiles elsewhere"]["binder"] == "P"
        and r["crust, volatiles elsewhere"]["factor"] < r["Earth cont. crust"]["factor"] / 10)
    om = d["orders_over_need"]
    chk("quantity is not the obstacle: Proxima b and d hold %.1e and %.1e times the largest need (%.3g kg)" % (
        om["Proxima b (m sin i)"], om["Proxima d (m sin i)"], d["need_max_kg"]), min(om.values()) > 1e15)
    chk("a chondrite with its phosphorus removed fails the gate outright (binder %s, factor %s): the gate can refuse "
        "a body, so its passes carry content" % d["no_P_control"], d["no_P_control"][1] == float("inf"), ctl=True)
    chk("diffuse interstellar gas needs %.2e m^3 swept per copy: a gate without its condensed-body clause would admit "
        "nowhere useful" % d["ism_sweep_m3"], d["ism_sweep_m3"] > 1e20, contrast=True)
    chk("the withdrawn dust belt, if it existed, would hold %.1e kg -- still %.1e times the need, so its withdrawal "
        "bears on composition (primitive feedstock), not on quantity" % (
            d["dust_belt_claim_kg"], d["dust_belt_claim_kg"] / d["need_max_kg"]),
        d["dust_belt_claim_kg"] / d["need_max_kg"] > 1e10)
    structural.append("the crust ranking (stockgate.ranked): %s" % ", ".join("%s %.1f" % ef for ef in d["crust_ranked"]))
    structural.append("b and d masses are minimum masses (m sin i); true masses are larger, so the quantity margins "
                      "are floors")
    for s_ in structural:
        print("  STRUCTURAL: " + s_)
    print("stockdest.py: %d/%d checks pass, %d of them controls and %d contrasts; %d STRUCTURAL printed, not counted" % (
        n_pass, n_pass + n_fail, n_ctl, n_con, len(structural)))
    return n_fail == 0


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    elif "--json" in sys.argv:
        print(json.dumps(compute(), indent=1, default=str))
    else:
        report()
