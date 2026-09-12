#!/usr/bin/env python3
"""pilot.py -- the pilot aperture as an acceptance protocol.

The one open item no instrument can close is the receiver's real efficiency:
receiver.py holds the design to a critical open-aperture figure of 0.690
(nominal 0.882) and hands the chain a field factor of 1.30, and no
falling-particle receiver above 2 MW_th has run. The ladder puts a ~30 MW_th
pilot aperture before the first module. This file states what that pilot
must measure and what number passes it up the ladder -- BEFORE it is built,
so the test cannot be graded on what it happens to return.

Everything is imported from receiver.py (the unit, the thresholds, the
losses), cspchain.py (the chain's rec link), hourly3.py (what a shortfall
costs in field and price) and titleone.py (what the pilot costs and when).
The protocol constants -- hours, uncertainty budget, wind envelope -- are
ASSUMED and marked so. Stdlib only.
"""
import argparse
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import receiver as RX                                           # noqa: E402
import cspchain as C                                            # noqa: E402
import hourly3 as HR                                            # noqa: E402
import titleone as T1                                           # noqa: E402

CASES = ("mid", "critical")
RXC = {"mid": "nominal", "critical": "critical"}
PILOT_MWTH = 30.0                          # the ladder's rung                             receiver.py ladder
# --- the protocol (ASSUMED, stated so the test is fixed before it runs) -------------
ON_SUN_HOURS = 1000.0                      # cumulative on-sun before acceptance is graded   ASSUMED (G3P3-USA >250 h is the record)
GRADED_HOURS = 500.0                       # the last N hours are the graded window          ASSUMED
U_MASSFLOW = 0.01                          # calorimetry: particle mass flow (weigh-cell)    ASSUMED band 0.5-2 %
U_DT = 0.01                                # calorimetry: inlet/outlet temperature           ASSUMED band 0.5-2 %
U_FLUX = 0.03                              # incident flux (calibrated heliostat + flux gauge) ASSUMED band 2-5 %
WIND_MS = (0.0, 12.0)                      # the envelope over which the figure must hold    ASSUMED (site 90th percentile ~12 m/s)
APERTURE_WIDTHS = (0.5, 1.0)               # fractions of the full pilot width run for the edge-loss test  ASSUMED


def unit(case):
    w, area, mdot = RX.aperture_unit(PILOT_MWTH, RXC[case])
    return dict(width_m=w, area_m2=area, drop_m=RX.pick(RX.DROP_M, RXC[case]), massflow_kg_s=mdot,
                flux=RX.pick(RX.FLUX_MW_M2, RXC[case]), t_amb=RX.pick(RX.T_AMB_C, RXC[case]))


def thresholds():
    d = C.design("helios3", "mid")
    return dict(chain=d["links"]["rec"], nominal_open=RX.efficiency("nominal", True),
                critical_open=RX.efficiency("critical", True), critical_dome=RX.efficiency("critical", False),
                nominal_dome=RX.efficiency("nominal", False))


def uncertainty():
    """Calorimetric efficiency = m cp dT / (flux * area): relative uncertainties add in quadrature.
    cp is taken from the sampled particles' own measured value and its band is folded into U_DT."""
    return (U_MASSFLOW ** 2 + U_DT ** 2 + U_FLUX ** 2) ** 0.5


def consequence(eta_measured):
    """What a measured critical-condition efficiency does upstream: the field factor
    against each case's own rec link (mid carries the chain's 0.90; critical already
    carries receiver.py's 0.690), and the price of that field. A factor below one is
    a saving the critical design was held pessimistic against."""
    out = dict(eta=eta_measured, field_factor=thresholds()["chain"] / eta_measured)
    for c in CASES:
        d = C.design("helios3", c)
        f = d["links"]["rec"] / eta_measured
        out[c + "_factor"] = f
        cost = HR.closure_cost_m(d, 1.0, 1.0, 1.0, f, 1.0)
        out[c] = HR.price_delta(d, cost, HR.closure_om_m(d, cost))
    return out


def grade(eta_measured, u=None):
    """PASS-DESIGN: clears the critical open figure by the uncertainty, the design basis holds.
    PASS-CHAIN: clears the chain's own link by the uncertainty, mid is witnessed too.
    UNDECIDED: inside the uncertainty band of the critical figure -- not a pass and not a fail.
    FAIL: below the critical figure by more than the uncertainty -- the field factor exceeds
    1.30 and the salt-block fallback is the recorded route."""
    th, u = thresholds(), uncertainty() if u is None else u
    if eta_measured >= th["chain"] * (1 + u):
        return "PASS-CHAIN"
    if eta_measured >= th["critical_open"] * (1 + u):
        return "PASS-DESIGN"
    if eta_measured >= th["critical_open"] * (1 - u):
        return "UNDECIDED"
    return "FAIL"


def pilot_tranche(case):
    for name, y0, y1, m in T1.tranches(case)[0]:
        if name.startswith("pilot"):
            return dict(years=(y0, y1), cost_m=m)
    return None


MEASUREMENTS = (
    ("M1 thermal efficiency", "particle mass flow (weigh-cell), inlet and outlet temperature, incident flux by calibrated heliostat field and flux gauge; eta = m cp dT / (q A)",
     "critical conditions: 0.5 MW/m2 aperture-average, 45 C ambient, 800 C outlet, hot back wall"),
    ("M2 edge losses", "M1 repeated at half and full curtain width on the same aperture",
     "loss per m2 must fall from half to full width as perimeter/area (receiver.py's scaling law)"),
    ("M3 dome against open", "one compound quartz dome (R-02) beside an open aperture on one tower, M1 on both",
     "whether the dome pays on the record or loses on the model; both are printed by receiver.py"),
    ("M4 particle ageing", "absorptance, attrition and oxide state sampled quarterly from the pilot's own inventory",
     "R-01 makeup rate and R-08's rate, the UNMOVED row"),
    ("M5 wind", "M1 across the site wind envelope, curtain stability by camera",
     "the graded figure must hold across the envelope, not at calm"),
)


def report():
    th, u = thresholds(), uncertainty()
    print()
    print("  THE PILOT APERTURE AS AN ACCEPTANCE PROTOCOL")
    print("  =============================================")
    print("    What it must measure and what passes it up the ladder, fixed before it is built.")
    print()
    print("    THE UNIT UNDER TEST: one 30 MW_th aperture")
    print(f"      {'':<40}{'nominal':>12}{'critical':>12}")
    U = {c: unit(c) for c in CASES}
    for label, k, fmt in (("curtain width, m", "width_m", "{:12.0f}"), ("drop, m", "drop_m", "{:12.1f}"),
                          ("aperture area, m2", "area_m2", "{:12.0f}"), ("particle flow, kg/s", "massflow_kg_s", "{:12.0f}"),
                          ("aperture-average flux, MW/m2", "flux", "{:12.2f}"), ("ambient, C", "t_amb", "{:12.0f}")):
        print(f"      {label:<40}" + "".join(fmt.format(U[c][k]) for c in CASES))
    print("      The critical unit is the design basis: wider, shallower, hotter, at half the flux.")
    print()
    print("    THE MEASUREMENTS")
    for name, how, what in MEASUREMENTS:
        print(f"      {name}")
        print(f"        how:   {how}")
        print(f"        what:  {what}")
    print()
    print("    THE PASS MARK (M1 at critical conditions, averaged over the graded window)")
    print(f"      chain's rec link (mid witnessed)            {th['chain']:.3f}")
    print(f"      nominal open aperture, receiver.py          {th['nominal_open']:.3f}")
    print(f"      CRITICAL open aperture -- the design basis   {th['critical_open']:.3f}")
    print(f"      critical with the dome                      {th['critical_dome']:.3f}")
    print(f"      measurement uncertainty (quadrature)        {u:.1%}   (flow {U_MASSFLOW:.0%}, dT {U_DT:.0%}, flux {U_FLUX:.0%})")
    print(f"      PASS-DESIGN at or above                     {th['critical_open'] * (1 + u):.3f}")
    print(f"      PASS-CHAIN at or above                      {th['chain'] * (1 + u):.3f}")
    print(f"      UNDECIDED between                           {th['critical_open'] * (1 - u):.3f} and {th['critical_open'] * (1 + u):.3f}")
    print(f"      hours: {ON_SUN_HOURS:.0f} on-sun, the last {GRADED_HOURS:.0f} graded, across {WIND_MS[0]:.0f}-{WIND_MS[1]:.0f} m/s")
    print("      A result inside the band is not a pass and not a fail: the pilot runs on.")
    print()
    print("    WHAT A RESULT COSTS UPSTREAM (field factor against each case's own rec link, and its price)")
    print(f"      {'measured eta':>14}{'grade':>14}{'mid field x':>12}{'+$/MWh':>8}{'crit field x':>14}{'+$/MWh':>8}")
    for eta in (0.90, 0.85, 0.80, 0.75, 0.70, 0.65, 0.60):
        r = consequence(eta)
        print(f"      {eta:>14.2f}{grade(eta):>14}{r['mid_factor']:>12.2f}{r['mid']:>8.0f}{r['critical_factor']:>14.2f}{r['critical']:>8.0f}")
    print("      The critical design already carries the 1.30; a pass at the design basis costs it nothing,")
    print("      and anything above is a saving it was held pessimistic against. Below the critical figure")
    print("      the salt-block fallback (Helios-2) is the recorded route; the first module is not ordered.")
    print()
    tr = {c: pilot_tranche(c) for c in CASES}
    print("    COST AND TIME (titleone.py's pilot tranche)")
    for c in CASES:
        print(f"      {c:<10} {tr[c]['years'][0]:.0f}-{tr[c]['years'][1]:.0f}, ${tr[c]['cost_m']:,.0f} M")
    print("      The pilot and the first node's field run in parallel; the first module waits on M1.")


def selftest():
    fails = 0

    def check(label, ok):
        nonlocal fails
        print(f"  {label:<72} {'PASS' if ok else 'FAIL'}")
        fails += 0 if ok else 1

    th, u = thresholds(), uncertainty()
    check("the design-basis threshold is receiver.py's critical open figure", abs(th["critical_open"] - RX.efficiency("critical", True)) < 1e-12)
    check("the chain's link is above the critical figure (the pilot can pass one and not the other)", th["chain"] > th["critical_open"])
    check("the critical unit is wider and shallower than the nominal", unit("critical")["width_m"] > unit("mid")["width_m"] and unit("critical")["drop_m"] < unit("mid")["drop_m"])
    check("both units carry the same thermal power", abs(unit("mid")["flux"] * unit("mid")["area_m2"] - unit("critical")["flux"] * unit("critical")["area_m2"]) < 1e-6)
    check("the uncertainty is dominated by the flux term", U_FLUX ** 2 > U_MASSFLOW ** 2 + U_DT ** 2)
    check("a result at the critical figure exactly is UNDECIDED, not a pass", grade(th["critical_open"]) == "UNDECIDED")
    check("a result at the chain's link plus the uncertainty is PASS-CHAIN", grade(th["chain"] * (1 + u) + 1e-9) == "PASS-CHAIN")
    check("a result well below the critical figure is FAIL", grade(0.60) == "FAIL")
    check("the grades are monotone in the measured figure", [grade(x) for x in (0.60, 0.70, 0.75, 0.95)] == ["FAIL", "UNDECIDED", "PASS-DESIGN", "PASS-CHAIN"])
    check("a measured figure equal to the chain's link costs mid nothing", abs(consequence(th["chain"])["mid_factor"] - 1.0) < 1e-12 and abs(consequence(th["chain"])["mid"]) < 1e-9)
    check("a measured figure at the critical value costs critical nothing (it already carries it)", abs(consequence(th["critical_open"])["critical_factor"] - 1.0) < 1e-9)
    check("a measured figure at the critical value reproduces the 1.30 field factor on mid", abs(consequence(th["critical_open"])["field_factor"] - RX.upstream_field_factor(C.design("helios3", "mid"), "critical", True)) < 1e-12)
    check("the pilot tranche exists at both cases", all(pilot_tranche(c) for c in CASES))
    check("every measurement names how and what", all(len(m) == 3 and all(m) for m in MEASUREMENTS))
    print(f"\nselftest: {fails} failures -> {'PASS' if fails == 0 else 'FAIL'}")
    return fails == 0


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args()
    sys.exit(0 if selftest() else 1) if a.selftest else report()
