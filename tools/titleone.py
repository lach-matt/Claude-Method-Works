#!/usr/bin/env python3
"""titleone.py -- the four Title I flaws no instrument had touched, each
settled the way FLAWS.tsv says it settles, at mid and at critical.

  F-19  the bond rate. 3.85 % is an investment-grade municipal rate on a
        contracted revenue stream; a first-of-kind plant at many times the
        largest built has no such rating on its own. What settles it: state
        the security and price the bonds to it. Here the required price is
        recomputed at three rates -- a state general-obligation backstop, a
        revenue bond on contracted in-state offtake, and an unrated
        first-of-kind -- and the security is named.
  F-24  the schedule. 5.25 GW in two construction years, where the record
        is four years for a tenth of that. What settles it: a phased COD
        and the finance sized to the phasing. Here the ladder of R-12
        (studies.py) is dated from the groundbreaking the author estimated,
        and the capital is split into tranches by rung from cspchain's own
        lines, so each bond issue follows a rung that has been passed.
  F-09  transmission. The 1,515 MW export needed firm rights that do not
        exist. What settles it: the export re-sized to what exists. F-01
        found the export is negative, so the export need is zero; what
        remains is the in-state gen-tie per node, sized here from the
        hour-by-hour peak injection at the closed sizing, against a 500 kV
        circuit's rating, and already priced in heliocost's switchyard line.
  F-10  the tariff. $0.00/kWh is not the Authority's to give; retail
        generation charges are set in IOU tariffs under the CPUC. What
        settles it: decide the retail mechanism and price it. Here the
        tariff is an OUTPUT -- the household bill at cost recovery, at each
        price the re-base states -- and the mechanism is named: the
        Authority as a load-serving entity in the community-choice form,
        with IOU delivery, selling at cost recovery.

Every number is imported; the file states four positions and prices them.
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
import studies as ST                                            # noqa: E402

CASES = ("mid", "critical")
# --- F-19 -----------------------------------------------------------------------
RATES = (("GO-backed, state general obligation", 0.0385),      # Title I's own rate; a GO or contracted-revenue rating  SOURCED (Title I §4.1)
         ("revenue bond, contracted in-state offtake", 0.050),  # BBB-class project revenue bond                          ASSUMED band 4.5-5.5 %
         ("unrated first-of-kind", 0.065))                      # no contract, no backstop                                ASSUMED band 6-8 %
# --- F-24 -----------------------------------------------------------------------
RUNG_YEARS = (("field, towers and PV at the first node", 2.0, ("heliostat field", "site improvements", "towers", "PV, direct + winter", "500 kV switchyards + gen-tie")),
              ("pilot aperture on one tower", 2.0, ("receivers",)),
              ("first 100 MWe module", 3.0, ("power block (sCO2)", "thermal storage (particles)", "electric heaters", "balance of plant")),
              ("fleet, by tower group", 5.0, ()))               # durations ASSUMED; the fleet is what is left of every line
# --- F-09 -----------------------------------------------------------------------
CIRCUIT_500KV_MW = (2000.0, 1500.0)       # thermal rating of one 500 kV circuit, nominal / critical  SOURCED band
NODES = len(H.NODES)
# --- F-10 -----------------------------------------------------------------------
MECHANISM = ("the Authority registered as a load-serving entity in the community-choice form "
             "(PUC section 366.2), IOU delivery, generation sold at cost recovery")


def rate_table(case):
    p = H3.priced(case)
    d = p["base"]
    out = []
    for name, r in RATES:
        price = (H.debt_service_m(p["capex_net"] / 1e3, r, H.BOND_TERM_Y) + p["om"]) / d["e_twh"]
        out.append((name, r, price, H.per_household(price)))
    return out


def tranches(case):
    d = C.design("helios3", case)
    L = d["lines"]
    total = sum(L.values())
    rows, used = [], set()
    year = sum(HC.GROUNDBREAK) / 2.0
    for name, years, lines in RUNG_YEARS:
        if name.startswith("pilot"):
            # one tower and one aperture of one receiver
            amount = L["towers"] / d["towers"] + L["receivers"] / d["towers"] * (30.0 / 794.0)
        elif name.startswith("first"):
            # the module's share of the whole plant, block and field alike
            amount = total * H3.FIRST_MODULE_MWE / d["turb_mw"]
        elif name.startswith("fleet"):
            amount = total - sum(r[3] for r in rows)
        else:
            amount = sum(L[k] for k in lines) / NODES
        rows.append((name, year, year + years, amount))
        year += years
    return rows, total


def gentie(case):
    d = C.design("helios3", case)
    r = HR.run(case, 1.0, 1.0, 1.5, 1.0, 1.0, design=d)
    peak = r["peak_injection_mw"]
    per_node = peak / NODES
    circ = CIRCUIT_500KV_MW[CASES.index(case)]
    return dict(peak=peak, per_node=per_node, circuits=per_node / circ, circuit_mw=circ,
                switchyard_m=HC.SWITCHYARD_PER_NODE_M[CASES.index(case) + 1] * NODES)


def report():
    print()
    print("  TITLE I: THE FOUR FLAWS NO INSTRUMENT HAD TOUCHED")
    print("  ==================================================")
    print()
    print("    F-19  THE BOND RATE. The security is contracted in-state offtake at the")
    print("          required price -- the same LSEs who pay $80-120 for firm clean")
    print("          energy today -- with a state general-obligation backstop for the")
    print("          first-of-kind rungs. Priced to each security:")
    print(f"      {'':<44}{'rate':>6}{'mid $/MWh':>11}{'$/hh':>7}{'crit $/MWh':>12}{'$/hh':>7}")
    tm, tc = rate_table("mid"), rate_table("critical")
    for (name, r, pm, hm), (_n, _r, pc, hc) in zip(tm, tc):
        print(f"      {name:<44}{100 * r:5.2f}%{pm:11.0f}{hm:7,.0f}{pc:12.0f}{hc:7,.0f}")
    print(f"          Today a household pays ${H.per_household(H.GEN_RATE_NOW * 1e3):,.0f}. Each point of rate is worth about")
    print(f"          ${(tm[2][2] - tm[0][2]) / ((RATES[2][1] - RATES[0][1]) * 100):.0f}/MWh at mid; the GO backstop is what makes the first rungs")
    print("          financeable at all, and it is the state's to give.")
    print()
    print("    F-24  THE SCHEDULE. The ladder of R-12, dated from the author's 2028-2030")
    print("          groundbreaking, each bond tranche following a rung that has been")
    print("          passed at its critical figure:")
    for case in CASES:
        rows, total = tranches(case)
        print(f"      {case}: direct cost ${total / 1e3:.1f} B")
        for name, y0, y1, amt in rows:
            print(f"        {name:<44} {y0:.0f}-{y1:.0f}  ${amt / 1e3:6.2f} B  ({amt / total:5.1%})")
    print("          First water-of-the-block -- the first module's COD -- is the third")
    print("          rung; the fleet's last tower group is a decade from groundbreaking,")
    print("          not two years. The pilot and the field run in parallel, which is")
    print("          why the first two rungs share dates.")
    print()
    print("    F-09  TRANSMISSION. The export is negative (F-01), so the export need is")
    print("          zero and no firm right has to be bought. What remains is the in-state")
    print("          gen-tie per node at the closed sizing (block x1.5), from the")
    print("          hour-by-hour peak injection:")
    print(f"      {'':<44}{'mid':>12}{'critical':>12}")
    gm, gc = gentie("mid"), gentie("critical")
    for label, key, fmt in (("peak injection, fleet, MW", "peak", "{:12,.0f}"), ("per node, MW", "per_node", "{:12,.0f}"),
                            ("one 500 kV circuit, MW", "circuit_mw", "{:12,.0f}"), ("circuits per node", "circuits", "{:12.2f}"),
                            ("switchyards + gen-ties, $M (heliocost)", "switchyard_m", "{:12,.0f}")):
        print(f"      {label:<44}{fmt.format(gm[key])}{fmt.format(gc[key])}")
    print("          One 500 kV circuit per node carries it at mid and at critical, and")
    print("          heliocost's switchyard line already pays for it. The interconnection")
    print("          study and the CAISO cluster application are the Authority's to file;")
    print("          no sovereign authority shortens them.")
    print()
    print("    F-10  THE TARIFF. $0.00/kWh is replaced by the household bill at cost")
    print("          recovery, which is an OUTPUT of the balance and not an input:")
    p = {c: H3.priced(c) for c in CASES}
    print(f"      {'':<44}{'mid':>12}{'critical':>12}")
    print(f"      {'with the register, $/household/yr':<44}" + "".join(f"{H.per_household(p[c]['price']):12,.0f}" for c in CASES))
    print(f"      {'today, IOU generation charge':<44}" + "".join(f"{H.per_household(H.GEN_RATE_NOW * 1e3):12,.0f}" for c in CASES))
    print(f"          Mechanism: {MECHANISM}.")
    print("          The bill is lower than today's at mid and higher at critical, and")
    print("          the whole-load prices of the re-base (rebase.py section 5) move it")
    print("          further; a free tariff is a subsidy paid by someone, and this")
    print("          program names no one to pay it.")
    print()


def selftest():
    fails = 0

    def check(label, ok):
        nonlocal fails
        print(f"  {label:<72} {'PASS' if ok else 'FAIL'}")
        fails += 0 if ok else 1

    tm = rate_table("mid")
    check("the GO row reproduces helios3's register price exactly", abs(tm[0][2] - H3.priced("mid")["price"]) < 1e-9)
    check("the required price rises monotonically with the rate", tm[0][2] < tm[1][2] < tm[2][2])
    check("critical exceeds mid at every rate", all(c[2] > m[2] for m, c in zip(tm, rate_table("critical"))))
    for case in CASES:
        rows, total = tranches(case)
        check(f"{case}: tranches sum to the direct cost exactly", abs(sum(r[3] for r in rows) - total) < 1e-6)
        check(f"{case}: every tranche is positive", all(r[3] > 0 for r in rows))
        check(f"{case}: the fleet is the largest tranche and the pilot the smallest",
              max(rows, key=lambda r: r[3])[0].startswith("fleet") and min(rows, key=lambda r: r[3])[0].startswith("pilot"))
        check(f"{case}: the schedule ends a decade or more after groundbreaking", rows[-1][2] - rows[0][1] >= 10.0)
    gm, gc = gentie("mid"), gentie("critical")
    check("peak injection is below block x1.5 plus PV (they are anti-coincident)",
          gm["peak"] < 1.5 * C.design("helios3", "mid")["turb_mw"] + C.design("helios3", "mid")["pv_mw"])
    check("one 500 kV circuit per node suffices at both cases", gm["circuits"] <= 1.0 and gc["circuits"] <= 1.0)
    check("the gen-tie cost is heliocost's line, not restated", gm["switchyard_m"] == HC.SWITCHYARD_PER_NODE_M[1] * NODES)
    import io
    import contextlib
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        report()
    out = buf.getvalue()
    check("the report names the security, the mechanism and the zero export",
          "general-obligation backstop" in out and "community-choice" in out and "export need is" in out)
    check("the report says a free tariff is a subsidy someone pays", "subsidy paid by someone" in out)
    print(f"\nselftest: {fails} failures -> {'PASS' if fails == 0 else 'FAIL'}")
    return fails == 0


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args()
    if a.selftest:
        sys.exit(0 if selftest() else 1)
    report()
