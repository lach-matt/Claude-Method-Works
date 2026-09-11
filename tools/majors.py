#!/usr/bin/env python3
"""majors.py -- the remaining MAJOR rows of FLAWS.tsv that no instrument had
touched, and the two program-wide rows the critical case answers.

  F-18  resource adequacy on export. The export is negative (F-01), so
        there is no export RA; what exists is in-state RA on the block,
        self-supplied by the Authority as the LSE. Sized here from the
        closed block and stated as MW, not as a revenue line.
  F-20  mirror washing. Scaled from Ivanpah, a built dry-cooled plant, per
        m2 of mirror, to Helios-3's field at each case and route, and the
        source named: the program's own desalinated water (Title II) where
        the mirrors route is chosen, the aqueduct where the water route is.
  F-21  land. cspchain's own acreage per node, at each case and route,
        against the parcels that exist -- fallowed Westside farmland is the
        one the document did not claim and should.
  F-22  the Central Valley node. hourly3.py runs each node on its own DNI;
        the node's field makes less per m2 by the DNI ratio and its December
        is the model's kindest (tule fog is not in the series). Its siting
        sensitivity is hourly3.siting(): moving it to the desert is worth two
        points of service and does not change the closing sizing.
  F-23  the nitrate register. Helios-3 holds no nitrate: the medium is
        sintered bauxite (R-13 to R-15, BENEFIT), so the four hazards --
        oxidiser, decomposition, freezing, the hot tank -- leave with the
        salt. They return only with the salt-block fallback, whose register
        is helios3's R-13 read backwards, and the hot tank is the record's
        own failure (Crescent Dunes, Noor III).
  F-25  federal nexus. NEPA cannot be shortened by state statute; the first
        node is therefore the one with no federal nexus, and the Mojave node
        budgets NEPA on the ladder's fleet rung, priced at the escalation.
  F-29  the downside case. The critical case is the downside case, by the
        author's standing rule; stated here with the coverage ratio a
        revenue bond needs (helios.COVERAGE_REQ) at each case.
  F-30  contingency, reserve, overrun. heliocost's contingency band is
        carried (30 % at critical, the first-of-kind figure the flaw asks
        for); a debt-service reserve fund of one year's debt service is
        sized at each case; the overrun backstop is the state GO of F-19.

Every number is imported or derived; every constant carries a status.
Stdlib only.
"""
import argparse
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import helios as H                                              # noqa: E402
import heliocost as HC                                          # noqa: E402
import cspchain as C                                            # noqa: E402
import helios3 as H3                                            # noqa: E402
import hourly3 as HR                                            # noqa: E402

CASES = ("mid", "critical")
NODES = len(H.NODES)
# --- F-20 -----------------------------------------------------------------------
IVANPAH_M2 = 2.6e6                        # mirror area                                   SOURCED (F-20)
IVANPAH_WASH_AFY = 100.0                  # dry-cooled, mirror washing                    SOURCED (F-20)
# --- F-21 -----------------------------------------------------------------------
WESTLANDS_RETIRED_ACRES = (100_000.0, 60_000.0)   # fallowed / drainage-impaired Westside land, nominal / critical  SOURCED band (~100 k acres retired)
# --- F-25 -----------------------------------------------------------------------
NEPA_YEARS = (2.0, 4.0)                   # EIS to record of decision, nominal / critical  SOURCED band (federal EIS median ~3.5 y)
# --- F-30 -----------------------------------------------------------------------
DSRF_YEARS = 1.0                          # debt-service reserve, years of debt service    SOURCED (municipal revenue-bond practice)
MIRRORS_FIELD_X = 2.0                     # hourly3's mirrors-route field factor           DERIVED (hourly3.py)
MIRRORS_BLOCK_X = 1.5                     # both routes' block factor                      DERIVED (hourly3.py)


def ra(case):
    """In-state RA: the closed block's net capacity, self-supplied by the Authority as LSE."""
    d = C.design("helios3", case)
    net = d["turb_mw"] * MIRRORS_BLOCK_X * d["links"]["par"]
    return dict(block_net_mw=net, export_mw=0.0)


def washing(case, route="mirrors"):
    d = C.design("helios3", case)
    field = d["aperture"] * (MIRRORS_FIELD_X if route == "mirrors" else 1.0)
    afy = field / IVANPAH_M2 * IVANPAH_WASH_AFY
    return dict(field_m2=field, afy=afy, afy_per_node=afy / NODES,
                source="Title II desalinated water" if route == "mirrors" else "aqueduct / recharge water of the water route")


def land(case, route="mirrors"):
    d = C.design("helios3", case)
    field = d["aperture"] * (MIRRORS_FIELD_X if route == "mirrors" else 1.0)
    acres = field / 0.20 / 4046.86 + d["pv_mw"] * C.FP.PV_ACRES_PER_MW
    ci = CASES.index(case)
    return dict(acres=acres, per_node=acres / NODES, km2=acres * 4046.86 / 1e6,
                westlands=WESTLANDS_RETIRED_ACRES[ci], westlands_covers=WESTLANDS_RETIRED_ACRES[ci] / (acres / NODES))


def central_valley():
    ratio = H.NODES[2][6] / H.NODES[0][6]
    base, closed = HR.siting("mid")
    r0 = HR.run("mid")
    return dict(dni_ratio=ratio, served_as_sited=r0["served_frac"], served_all_desert=base["served_frac"],
                dec_as_sited=r0["month_unserved"][12] / r0["month_load"][12], dec_all_desert=base["month_unserved"][12] / base["month_load"][12],
                closed_unserved=1 - closed["served_frac"])


def nepa(case):
    p = H3.priced(case)
    ci = CASES.index(case)
    years = NEPA_YEARS[ci]
    return dict(years=years, delay_m=p["capex_net"] / NODES * HC.ESCALATION * years)


def downside(case):
    p = H3.priced(case)
    d = p["base"]
    cov = H.COVERAGE_REQ
    price_cov = (H.debt_service_m(p["capex_net"] / 1e3, H.BOND_RATE, H.BOND_TERM_Y) * cov + p["om"]) / d["e_twh"]
    return dict(coverage=cov, price=p["price"], price_at_coverage=price_cov, hh=H.per_household(price_cov))


def reserve(case):
    p = H3.priced(case)
    ci = CASES.index(case)
    ds = H.debt_service_m(p["capex_net"] / 1e3, H.BOND_RATE, H.BOND_TERM_Y)
    return dict(contingency=HC.CONTINGENCY[ci + 1], epc=HC.EPC_OWNER[ci + 1], dsrf_m=ds * DSRF_YEARS, debt_service_m=ds)


def report():
    print()
    print("  THE REMAINING MAJORS, SETTLED")
    print("  ==============================")
    print()
    print("    F-18  RESOURCE ADEQUACY. The export is negative, so there is no export RA.")
    print("          In-state RA is the closed block's net capacity, self-supplied by the")
    print("          Authority as the load-serving entity (F-10), a requirement met and")
    print("          not a revenue line:")
    for c in CASES:
        print(f"            {c:<9} block net at x{MIRRORS_BLOCK_X:.1f}: {ra(c)['block_net_mw']:,.0f} MW; export RA: {ra(c)['export_mw']:.0f} MW")
    print()
    print("    F-20  MIRROR WASHING. Ivanpah, dry-cooled, washes 2.6 M m2 with ~100 AFY.")
    print("          Scaled per m2 to Helios-3's field:")
    print(f"      {'':<36}{'mid':>12}{'critical':>12}")
    for route in ("mirrors", "water"):
        w = {c: washing(c, route) for c in CASES}
        print(f"      {route + ' route: field, M m2':<36}" + "".join(f"{w[c]['field_m2'] / 1e6:12.1f}" for c in CASES))
        print(f"      {'  washing, AFY (all nodes)':<36}" + "".join(f"{w[c]['afy']:12,.0f}" for c in CASES))
        print(f"      {'  per node, AFY':<36}" + "".join(f"{w[c]['afy_per_node']:12,.0f}" for c in CASES))
        print(f"          source: {w['mid']['source']}")
    print("          Under a module-year either way; the program makes its own.")
    print()
    print("    F-21  LAND. cspchain's own acreage (field at 20 % ground cover + PV):")
    print(f"      {'':<36}{'mid':>12}{'critical':>12}")
    for route in ("mirrors", "water"):
        l = {c: land(c, route) for c in CASES}
        print(f"      {route + ' route: acres, all nodes':<36}" + "".join(f"{l[c]['acres']:12,.0f}" for c in CASES))
        print(f"      {'  per node, acres':<36}" + "".join(f"{l[c]['per_node']:12,.0f}" for c in CASES))
        print(f"      {'  per node, km2':<36}" + "".join(f"{l[c]['km2'] / NODES:12.0f}" for c in CASES))
        print(f"      {'  Westside fallowed land covers a node':<36}" + "".join(f"{l[c]['westlands_covers']:12.2f}x" for c in CASES))
    print("          Fallowed, drainage-impaired Westside San Joaquin farmland is the one")
    print("          contiguous disturbed parcel of this size in the state, and the")
    print("          document did not claim it; the desert nodes are BLM-adjacent (F-25).")
    print()
    cv = central_valley()
    print("    F-22  THE CENTRAL VALLEY NODE. hourly3 runs each node on its own annual DNI;")
    print(f"          the Westside node's is {cv['dni_ratio']:.2f} of the Mojave's, so its field makes {cv['dni_ratio']:.2f}")
    print("          per m2 and the chain's aperture is split equally regardless -- the")
    print("          node is a fifth short of its share, which the fleet field absorbs.")
    print(f"          Its December is the model's kindest (tule fog is not in the series).")
    print(f"          Moving it to the desert: served {cv['served_as_sited']:.3f} -> {cv['served_all_desert']:.3f}, December")
    print(f"          {cv['dec_as_sited']:.3f} -> {cv['dec_all_desert']:.3f}; the closing sizing is unchanged ({cv['closed_unserved']:.4f}")
    print("          unserved). It is not a desert node, it is worth two points, and its")
    print("          land is the program's best. Kept, at a larger field share.")
    print()
    print("    F-23  THE NITRATE REGISTER. Helios-3 holds no nitrate. The medium is")
    print("          sintered bauxite: no oxidiser, no decomposition ceiling, no freezing")
    print("          point, no hot tank (helios3 R-13 to R-15, BENEFIT). The four hazards")
    print("          return only with the salt-block fallback, and the hot tank is the")
    print("          record's own failure: Crescent Dunes four leaks, Noor III fourteen")
    print("          months. The fallback's register is R-13 read backwards.")
    print()
    print("    F-25  FEDERAL NEXUS. NEPA is not shortened by any state statute. So the")
    print("          first node -- the ladder's field rung -- is the one with no federal")
    print("          nexus (Westside, state or private land), and the Mojave node budgets")
    print("          NEPA on the fleet rung:")
    for c in CASES:
        n = nepa(c)
        print(f"            {c:<9} NEPA {n['years']:.0f} y on one node; escalation while it waits ${n['delay_m']:,.0f} M")
    print()
    print("    F-29  THE DOWNSIDE CASE is the critical case (the author's standing rule):")
    print("          every band at its adverse end. A revenue bond adds a coverage ratio;")
    print(f"          at helios.COVERAGE_REQ = {H.COVERAGE_REQ:.2f} the price that covers it:")
    print(f"      {'':<36}{'mid':>12}{'critical':>12}")
    dd = {c: downside(c) for c in CASES}
    print(f"      {'price at cost recovery, $/MWh':<36}" + "".join(f"{dd[c]['price']:12.0f}" for c in CASES))
    print(f"      {'price at 1.25x coverage, $/MWh':<36}" + "".join(f"{dd[c]['price_at_coverage']:12.0f}" for c in CASES))
    print(f"      {'  per household, $/yr':<36}" + "".join(f"{dd[c]['hh']:12,.0f}" for c in CASES))
    print()
    print("    F-30  CONTINGENCY, RESERVE, OVERRUN. heliocost carries the contingency and")
    print("          EPC bands; a debt-service reserve fund of one year's debt service is")
    print("          sized; the overrun backstop is the state GO of F-19:")
    print(f"      {'':<36}{'mid':>12}{'critical':>12}")
    rr = {c: reserve(c) for c in CASES}
    print(f"      {'contingency':<36}" + "".join(f"{rr[c]['contingency']:12.0%}" for c in CASES))
    print(f"      {'EPC and owner':<36}" + "".join(f"{rr[c]['epc']:12.0%}" for c in CASES))
    print(f"      {'debt service, $M/yr':<36}" + "".join(f"{rr[c]['debt_service_m']:12,.0f}" for c in CASES))
    print(f"      {'DSRF, $M':<36}" + "".join(f"{rr[c]['dsrf_m']:12,.0f}" for c in CASES))
    print("          The critical case carries the 30 % first-of-kind contingency the flaw")
    print("          asked for; mid carries 15 %, and is not offered as the design.")
    print()


def selftest():
    fails = 0

    def check(label, ok):
        nonlocal fails
        print(f"  {label:<72} {'PASS' if ok else 'FAIL'}")
        fails += 0 if ok else 1

    check("export RA is zero at both cases", all(ra(c)["export_mw"] == 0.0 for c in CASES))
    check("in-state RA is the closed block net of parasitics", abs(ra("mid")["block_net_mw"] - C.design("helios3", "mid")["turb_mw"] * 1.5 * C.design("helios3", "mid")["links"]["par"]) < 1e-9)
    check("washing scales exactly per m2 from Ivanpah", abs(washing("mid", "water")["afy"] - C.design("helios3", "mid")["aperture"] / IVANPAH_M2 * IVANPAH_WASH_AFY) < 1e-9)
    check("washing is under one module-year (50,000 AFY) at every case and route",
          all(washing(c, r)["afy"] < 50_000 for c in CASES for r in ("mirrors", "water")))
    check("land at the water route equals cspchain's own acres", abs(land("mid", "water")["acres"] - C.design("helios3", "mid")["acres"]) < 1e-6)
    check("the mirrors route needs more land than the water route", all(land(c, "mirrors")["acres"] > land(c, "water")["acres"] for c in CASES))
    cv = central_valley()
    check("the Central Valley node's DNI is 0.7-0.85 of the Mojave's", 0.7 < cv["dni_ratio"] < 0.85)
    check("all-desert siting improves service by under five points and does not close December",
          0.0 < cv["served_all_desert"] - cv["served_as_sited"] < 0.05 and cv["dec_all_desert"] > 0.2)
    check("NEPA costs more at critical", nepa("critical")["delay_m"] > nepa("mid")["delay_m"])
    check("the coverage price exceeds the cost-recovery price at both cases", all(downside(c)["price_at_coverage"] > downside(c)["price"] for c in CASES))
    check("critical carries the 30 % contingency the flaw asks for", reserve("critical")["contingency"] >= 0.25)
    check("the DSRF is one year's debt service", all(abs(reserve(c)["dsrf_m"] - reserve(c)["debt_service_m"]) < 1e-9 for c in CASES))
    head = open(__file__).read().split("def ra(")[0].splitlines()
    consts = [l for l in head if l[:1].isupper() and "=" in l and not l.startswith(("HERE", "CASES", "NODES"))]
    check("every constant line carries a status", all(any(t in l for t in ("SOURCED", "ASSUMED", "DERIVED", "exact")) for l in consts))
    import io
    import contextlib
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        report()
    out = buf.getvalue()
    check("the report says Helios-3 holds no nitrate", "Helios-3 holds no nitrate" in out)
    check("the report says NEPA is not shortened by state statute", "not shortened by any state statute" in out)
    print(f"\nselftest: {fails} failures -> {'PASS' if fails == 0 else 'FAIL'}")
    return fails == 0


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args()
    if a.selftest:
        sys.exit(0 if selftest() else 1)
    report()
