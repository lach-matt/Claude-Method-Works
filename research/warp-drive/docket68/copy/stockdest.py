#!/usr/bin/env python3
"""
stockdest.py -- the stock gate at a real destination (M-RULINGS item 88, link 4: D25 / W3-O3 at Proxima).  READ where
sources exist, deduced, computed.  SEATED (ledger section 8n, M-D68-89; first written 'Not seated'); verified once,
findings applied (HISTORY at the end; first written 'not verified').  M's words are carried as hypotheses, never as results.

The faithful copy (item 87) is built at position 2 "with what it has" (item 86, answer 7); item 5 put the substance
"from the seat" (M: "Yes, from the seat").  faithful.py sized what crosses; this asks whether what it is built FROM is
there.  The board's gate (stockgate.GATE, imported, never retyped): "B admissible <=> within the corridor's arrival
aperture there is a CONDENSED body, PRIMITIVE rather than devolatilised, holding at least M(p,s) * m_payload of
accessible mass", with M(p, s) = max_e p_e / s_e (one element binds).

M'S RULING (item 89): "No costlier. Stock is stock. The cost is in how much information is transferred as a README
(how big the file is)."  Carried: H-STOCK-IS-STOCK -- any condensed body's accessible stock admits; the gate's
PRIMITIVE clause is set aside on the faithful-copy path (stockgate.py's text is not edited); and H-COST-IN-README --
the trip's cost is the README's size.  H-PRIMITIVE-AS-PRICE (offered) is not adopted; kept as history.  Under the
ruling, Proxima ADMITS ON QUANTITY at b (confirmed) and d (candidate), and the feedstock figures below are mass
throughput, not cost.  What a site's composition changes is what the README must instruct the builder to do with
it -- unpriced (OPEN 5).

WHAT FOLLOWS THE WORK
  * QUANTITY IS NOT THE OBSTACLE AT ANY ACCESSIBLE SCALE.  A 70 kg copy needs 749 kg of CI-chondrite-like feedstock
    (phosphorus binds at 10.7 kg per kg), or 32 t of an Earth-like crust if the rock must supply everything (nitrogen
    binds at 459), or 1.2 t of rock if the volatiles come from an atmosphere, ocean or ices (phosphorus binds at 17;
    rock fraction only -- the 25 kg of volatiles is not priced), or 134 t of a solar-composition photosphere.  The
    largest rock need is about 12 m^3 at 2,700 kg/m^3 (H-CRUST-DENSITY): the top metre of a 3.4 m square.  Whole-planet
    masses (b and d each at least 1e19 times the need) only confirm that it does not run out.  First written 'each
    exceeds the largest of these needs by about nineteen orders' as the point -- accessibility was not addressed.
  * UNDER M'S ANSWER 4 THE APERTURE BECOMES A SITING CHOICE.  M: "an input required as in input for the second
    position required by the device" (H-ADDRESS-INPUT).  With B-RECV (the board's: a holder at the destination) and
    H-COLOCATED-BUILD (the holder is also the builder, and the aperture is its site), the device must be placed on a
    body that passes the gate.  The aperture D25 left without a value becomes a design choice, not a value.  First
    written 'gets one: the device's site', and 'the gate asks only that it stand on a body with the feedstock'.
    The device itself must be carried to position 2 first: a one-time, non-local cost outside the gate.
  * EVEN THE DRY BRANCH PASSES ON QUANTITY.  Composition decides the cost per copy (17 or 459 kg per kg), not whether a
    copy is possible -- unless the gate's PRIMITIVE clause is held strictly (next).
  * Boundary (item 82):
    - BY THE GATE'S LETTER (stockgate.GATE, unedited), PROXIMA IS NOT SHOWN ADMISSIBLE; under M's ruling it admits.  The quantity clause passes by orders; the PRIMITIVE clause
      is unshown: no primitive body is shown there, and an Earth-like crust is the board's devolatilised case.  A reading
      that would admit planets is carried for M to rule on, not assumed: H-PRIMITIVE-AS-PRICE (the primitive clause is
      absorbed into M(p, s), so a devolatilised body costs 459 kg per kg instead of 10.7 but is not excluded) --
      stockgate itself calls "primitive" its own causal reading of a concentration.
    - Composition is not measured: one confirmed planet (b) and one candidate (d), both presumed rocky from minimum
      mass alone (H-ROCKY); no transit for b, and one "is unlikely" for d.  The discovery paper names b's fork: migrated
      bodies "would be volatile rich", pebble migration "would produce much drier worlds".
    - A primitive small-body reservoir is not shown: the 1-4 au belt (about 0.01 Earth masses) is unsupported after a
      reanalysis attributed its emission to a flare ("no need to invoke the presence of a dust belt at 1-4 AU"); the
      30 au belt stays marginal.  First written 'withdrawn' -- a reanalysis removes the need, it does not prove absence.
    - Diffuse interstellar gas (CONTRAST) would need 8e25 m^3 swept per copy (stock.py's own 14-element payload).

    python3 stockdest.py             report
    python3 stockdest.py --selftest  checks, CONTROLS and CONTRASTS marked, STRUCTURAL printed and not counted
    python3 stockdest.py --json      the numbers as JSON

SOURCES READ (2026-10-06; alphaXiv answer_pdf_queries, open arXiv copies, printed pages; verifier-READ again)
  Anglada-Escude et al. 1609.03449v1 (Nature 536, 437): Proxima b, P = 11.186 d, a = 0.0485 au, m sin i = 1.27
    [1.10, 1.46] M_earth (Table 1, p.10); no transit found (p.5); "While migrated planets and embryos originating
    beyond the ice-line would be volatile rich, pebble migration would produce much drier worlds" (pp.5-6; about b).
  Faria et al. 2202.05188v1 (A&A): "a candidate short-period sub-Earth" (title); Proxima d, P = 5.122 d, a = 0.02885 au,
    m sin i = 0.26 +/- 0.05 M_earth (abstract p.1; p.9; Table C.1 p.17); its radius 0.81 R_earth is a model estimate
    and "a transit is unlikely" (p.9); b at 1.07 +/- 0.06 M_earth (p.9; Table C.1); Proxima c "has so far eluded a clear
    detection with direct imaging or astrometry" (p.1).
  Anglada et al. 1711.00578v1 (ApJL): a belt "at distances ranging between 1 and 4 au", "of the order of 0.01 Earth
    masses" including bodies up to 50 km (abstract, p.1); an outer belt at about 30 au, marginal (p.1).
  MacGregor et al. 1802.08257v1 (ApJL): "we conclude that there is no need to invoke the presence of a dust belt at
    1-4 AU" (abstract, p.1; p.7 has "an inner dust belt"); the warm dust's need "is also removed" (p.1); on the 30 au
    belt, "caution should be used in over-interpreting this marginal result" (p.7).

NAMED HYPOTHESES AND PREMISES
  H-ADDRESS-INPUT (M's, item 86, answer 4, verbatim above); B-RECV (the board's: a holder at the destination);
  H-COLOCATED-BUILD (the holder is the builder; the aperture is its site); H-SITE (the builder reaches the accessible
    layer of its body).
  H-ROCKY: b and d are rocky, presumed from minimum mass alone.
  H-EARTHLIKE-CRUST: an accessible layer of Rudnick & Gao's continental-crust composition (stock.py's CRUST, atmosphere
    excluded) -- one reservoir of one planet; not evidence about Proxima, whose planets are tidally exposed to a flare
    star.
  H-VOLATILE-RICH: N, C and H available on the site from an atmosphere, ocean or ices; the rock then supplies the rest.
    First named H-VOLATILES-ELSEWHERE and labelled 'the dry branch' -- it is the volatile-rich one.
  H-CRUST-DENSITY: 2,700 kg/m^3 (NAMED-NOT-READ; for the accessibility scale only).
  H-PRIMITIVE-AS-PRICE: offered, not adopted (item 89).  M's: H-STOCK-IS-STOCK, H-COST-IN-README (item 89).
  M_EARTH = 5.9722e24 kg (a standard value, GM_earth / G; not READ this pass).  The payload: stockgate.py's
    "as-composed 59" reference adult (imported).  The photosphere row is the Sun's (A09), not Proxima's.

OPEN
  1. The composition of Proxima b or d (a transit or emission spectrum; direct imaging).
  2. A primitive small-body reservoir at Proxima (the 30 au belt, marginal).
  3. Phosphorus, the binder, in Proxima's own photosphere (W3-O3).
  4. Separation energy: stockgate.py prices mass, not the energy to extract it; the volatile reservoir's mass.
  5. Under H-COST-IN-README: how much a site's composition adds to the README (the instructions for processing a
     devolatilised or dry site).  First listed as 'H-PRIMITIVE-AS-PRICE: M's ruling', since ruled (item 89).

HISTORY (verifier, 2026-10-06; first-written claims kept above where they stood)
  The gate's PRIMITIVE clause had been dropped (verdict now stated); the volatile-rich and dry branches were swapped
  and the dry branch's 'N, C, H must come from elsewhere' was false (rock alone supplies N at 459); the 1.2 t figure
  is the rock fraction only; 'two confirmed condensed bodies' -> one planet and one candidate, rocky presumed; the
  'CONTROL' (phosphorus removed) could not fail -- it is STRUCTURAL, and the control is now the photospheric-only
  column, which fails because of what A09 did not measure; accessibility addressed; 'withdrawn' -> unsupported after
  reanalysis; the photosphere row named as solar; M's answer 4 quoted verbatim; the dry branch computed from the full
  factor table.
"""
import contextlib
import importlib.util
import io
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
WD = os.path.dirname(os.path.dirname(HERE))

M_EARTH = 5.9722e24                    # kg, standard value (GM_earth / G); not READ this pass
CRUST_DENSITY = 2700.0                 # kg/m^3, H-CRUST-DENSITY, NAMED-NOT-READ
PAYLOAD_KG = 70.0
PKIND = "as-composed 59"
VOLATILES = ("N", "C", "H")

# READ (see SOURCES)
PROXIMA_B_MSINI = 1.07                 # M_earth, Faria Table C.1 (TM RVs); Anglada-Escude 1.27
PROXIMA_D_MSINI = 0.26                 # M_earth, Faria abstract (a candidate)
DUST_BELT_CLAIM_ME = 0.01              # M_earth, Anglada 2017 -- unsupported after reanalysis (MacGregor 2018)


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
    crust = sg.DESTS["Earth cont. crust"]()
    res = {}
    for dkind, label in (("CI chondrite", "CI chondrite (primitive)"),
                         ("Earth cont. crust", "crust, rock only (dry)"),
                         ("stellar photosphere", "solar-composition photosphere")):
        binder, factor = sg.binding_under(PKIND, dkind)
        res[label] = {"binder": binder, "factor": factor, "feedstock_kg": sg.feedstock_kg(PAYLOAD_KG, PKIND, dkind)}
    f_all = sg.factors(p, crust)
    rich = max(((e, f) for e, f in f_all.items() if e not in VOLATILES), key=lambda ef: ef[1])
    res["crust, volatile-rich site (rock fraction)"] = {"binder": rich[0], "factor": rich[1],
                                                        "feedstock_kg": rich[1] * PAYLOAD_KG}
    volatile_kg = sum(p[e] for e in VOLATILES if e in p) * PAYLOAD_KG
    rock_need = res["crust, rock only (dry)"]["feedstock_kg"]
    need_max = max(v["feedstock_kg"] for v in res.values())
    bodies = {"Proxima b (m sin i)": PROXIMA_B_MSINI * M_EARTH, "Proxima d (m sin i, candidate)": PROXIMA_D_MSINI * M_EARTH}
    ism_v, ism_r = st.ism_sweep_volume(PAYLOAD_KG)
    s_noP = dict(sg.DESTS["CI chondrite"]())
    s_noP.pop("P", None)
    return {"gate": sg.GATE, "reservoirs": res, "crust_ranked": sg.ranked(p, crust, 6),
            "volatile_kg": volatile_kg, "rock_need_m3": rock_need / CRUST_DENSITY,
            "need_max_kg": need_max, "bodies_kg": bodies,
            "orders_over_need": {k: v / need_max for k, v in bodies.items()},
            "photospheric_only": sg.binding_under(PKIND, "photospheric-only"),
            "no_P": sg.processing_factor(p, s_noP),
            "dust_belt_claim_kg": DUST_BELT_CLAIM_ME * M_EARTH, "ism_sweep_m3": ism_v, "ism_sweep_radius_m": ism_r}


def report():
    d = compute()
    print("stockdest.py -- the stock gate at Proxima (M item 88, link 4; verified once; seated, ledger 8n)\n")
    print("  the gate (stockgate.GATE): " + d["gate"])
    for k, v in d["reservoirs"].items():
        print("  %-44s binder %-2s %8.2f kg per kg   feedstock for 70 kg: %.4g kg" % (
            k, v["binder"], v["factor"], v["feedstock_kg"]))
    print("  the volatile-rich branch leaves %.1f kg of N, C and H to an unpriced volatile reservoir" % d["volatile_kg"])
    print("  the largest rock need is %.1f m^3 at %.0f kg/m^3 (H-CRUST-DENSITY)" % (d["rock_need_m3"], CRUST_DENSITY))
    for k, v in d["bodies_kg"].items():
        print("  %s: %.3e kg = %.2e x the largest need" % (k, v, d["orders_over_need"][k]))
    print("  verdict by the gate's letter: quantity passes; PRIMITIVE unshown at Proxima.  Under M's ruling (item 89, "
          "H-STOCK-IS-STOCK): admits on quantity; composition bears on the README (H-COST-IN-README), unpriced")
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
    ci, dry, rich = (r["CI chondrite (primitive)"], r["crust, rock only (dry)"],
                     r["crust, volatile-rich site (rock fraction)"])
    chk("the owners' gate, imported: a CI chondrite binds on %s at %.2f kg per kg (%.0f kg for 70 kg)" % (
        ci["binder"], ci["factor"], ci["feedstock_kg"]), ci["binder"] == "P" and abs(ci["feedstock_kg"] - 749.08) < 0.5)
    chk("a dry site (rock only, Earth-like crust) binds on N at %.0f kg per kg (%.3g kg); a volatile-rich site's rock "
        "binds on %s at %.1f (%.3g kg, rock fraction only)" % (dry["factor"], dry["feedstock_kg"], rich["binder"],
                                                               rich["factor"], rich["feedstock_kg"]),
        dry["binder"] == "N" and rich["binder"] == "P" and rich["factor"] < dry["factor"] / 10)
    chk("quantity at an accessible scale: the largest rock need is %.1f m^3 -- the top metre of a %.1f m square" % (
        d["rock_need_m3"], d["rock_need_m3"] ** 0.5), d["rock_need_m3"] < 20)
    chk("the solar photospheric-only column (A09) cannot price the payload (binder %s, factor %s): the gate refuses a "
        "reservoir for what was actually not measured" % d["photospheric_only"],
        d["photospheric_only"][1] == float("inf"), ctl=True)
    chk("diffuse interstellar gas needs %.2e m^3 swept per copy: the condensed-body clause is real" % d["ism_sweep_m3"],
        d["ism_sweep_m3"] > 1e20, contrast=True)
    structural.append("the gate's text (imported) carries the PRIMITIVE clause: %s; no Proxima body is shown to meet "
                      "it, so the verdict by the letter is 'not shown admissible'" % (
                          "PRIMITIVE rather than devolatilised" in d["gate"]))
    om = d["orders_over_need"]
    structural.append("whole-planet masses: b and d hold %.1e and %.1e times the largest need (minimum masses, so "
                      "floors) -- they confirm the stock does not run out" % tuple(om.values()))
    structural.append("a chondrite with its phosphorus removed has factor %s (inf by definition of factors())" %
                      (d["no_P"][1],))
    structural.append("the unpriced volatile reservoir on the volatile-rich branch: %.1f kg of N, C and H" %
                      d["volatile_kg"])
    structural.append("the 1-4 au belt (unsupported after reanalysis), if it existed: %.1e kg, %.1e times the need" % (
        d["dust_belt_claim_kg"], d["dust_belt_claim_kg"] / d["need_max_kg"]))
    structural.append("the crust ranking (stockgate.ranked): %s" % ", ".join("%s %.1f" % ef for ef in d["crust_ranked"]))
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
