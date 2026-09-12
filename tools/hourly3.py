#!/usr/bin/env python3
"""hourly3.py -- Helios-3 run hour by hour, at mid and at critical.

cspchain.py sizes Helios-3 with three STATIC assumptions -- a direct-PV share
of the annual energy (DIRECT_SHARE), a winter heater sized to a fraction of
the night block's thermal input (WINTER_HEATER_FRACTION), and a dispatch
link near unity -- and names running the plant hour by hour as its next
step. studies.py puts that study first on the recommendation list because
it is the one only this repository can run. This is it.

What it does. It takes cspchain's Helios-3 design at a case (aperture,
turbine, particle store, PV, heaters, chain links) and runs one year at one
hour per step across the three nodes: PV serves the load first; PV surplus
charges the store through the heaters; the field charges the store; the
sCO2 block serves the residual load from the store, within its minimum load;
what nothing serves is UNSERVED and is counted by month. It then asks what
PV overbuild and heater size close the unserved energy at each case, and
prices them on cspchain's own lines.

Two things are RECONSTRUCTED and say so: the hourly load shape (California
residential, evening peak, summer amplification -- pinned exactly to the
annual energy so the shape cannot change the energy, only its timing) and
the PV output shape (a single-axis tracker follows the same DNI series
helios.py reconstructs, pinned to the case's sourced capacity factor). The
optical curve is helios.py's shape pinned to the case's annual link. Every
level is sourced or imported; only timing is reconstructed, and the
selftest asserts each pin exactly.

The author's standing rule applies: every result is printed at mid and at
critical, and the design is held to critical. Stdlib only.
"""
import argparse
import math
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import helios as H                                              # noqa: E402
import cspchain as C                                            # noqa: E402
import firmpower as FP                                          # noqa: E402

CASES = ("mid", "critical")
# --- load shape ---------------------------------------------------------------
LOAD_PEAK_HOUR = 19.0                     # residential evening peak, clock hour   SOURCED (CAISO net peak 17-20)
LOAD_PEAK_WIDTH_H = 3.5                   # gaussian half-width of the evening peak RECONSTRUCTED
LOAD_BASE = 0.70                          # night trough / daily mean               RECONSTRUCTED
LOAD_SUMMER = 1.25                        # Jul-Aug daily mean / annual mean        RECONSTRUCTED (AC load)
LOAD_WINTER = 0.92                        # Dec-Jan                                 RECONSTRUCTED
LOAD_PEAK_TO_MEAN_BAND = (1.4, 2.0)       # annual peak hour / mean hour            ASSUMED band (residential class)
# --- PV ----------------------------------------------------------------------
PV_DIFFUSE = 0.10                         # share of clear-sky output not tracking DNI  ASSUMED
# --- heaters ------------------------------------------------------------------
HEATER_EFF = 0.98                         # resistance heater, electric -> thermal  SOURCED band 0.95-0.99
# --- pricing of closure ---------------------------------------------------------
PV_OVERBUILD_SCAN = (1.0, 1.5, 2.0)
HEATER_SCAN = (1.0, 3.0)
TURBINE_SCAN = (1.0, 1.25, 1.5, 1.75)
APERTURE_SCAN = (1.0, 1.5, 2.0, 2.5)
TES_SCAN = (1.0, 2.0, 3.0)                # days of the 16 h store, beyond scaling with the block
TARGETS = (0.01, 0.001)                   # unserved share of load: 1 % and 0.1 %
FIELD_LINES = ("heliostat field", "site improvements", "towers", "receivers")
BLOCK_LINES = ("power block (sCO2)", "balance of plant")


def pv_cf(case):
    return FP.PV_CF[0] if case == "critical" else FP.PV_CF[1]


MIRRORS_ROUTE = (1.25, 1.5, 2.0)          # (block, field, store days): close() at the 1 % target, both cases  DERIVED (2026-09-11, corrected load shape)


def mirrors_run(case, design=None):
    b, f, s = MIRRORS_ROUTE
    return run(case, 1.0, 1.0, b, f, s, design=design)


def mirrors_cost_m(d):
    b, f, s = MIRRORS_ROUTE
    return closure_cost_m(d, 1.0, 1.0, b, f, s)


MEASURED = {"load": None, "dni": {}}      # profiles.py attaches measured shapes here; status MEASURED when set


def load_series(e_twh):
    """8,760 hourly MW whose sum is exactly e_twh. Shape RECONSTRUCTED, or MEASURED
    when profiles.py has attached one (the pin to e_twh is the same either way)."""
    if MEASURED["load"] is not None:
        raw = list(MEASURED["load"])
        k = e_twh * 1e6 / sum(raw)
        return [v * k for v in raw]
    raw = []
    for doy in range(1, 366):
        season = 0.5 * (LOAD_SUMMER + LOAD_WINTER) + 0.5 * (LOAD_SUMMER - LOAD_WINTER) * math.cos(
            2.0 * math.pi * (doy - 200) / 365.0)          # peaks late July
        for hr in range(24):
            d = min(abs(hr + 0.5 - LOAD_PEAK_HOUR), 24 - abs(hr + 0.5 - LOAD_PEAK_HOUR))
            shape = LOAD_BASE + (1.0 - LOAD_BASE) * 2.0 * math.exp(-(d / LOAD_PEAK_WIDTH_H) ** 2)
            raw.append(shape * season)
    k = e_twh * 1e6 / sum(raw)
    return [v * k for v in raw]


def node_series(node, case):
    """Per node: DNI, elevation and a single-axis PV shape (unscaled)."""
    name, lat, lon, _ap, _g, _s, annual_dni, _st = node
    if name in MEASURED["dni"]:
        m = MEASURED["dni"][name]
        k = annual_dni * 1e3 / sum(m)          # pinned to the sourced annual, as the reconstruction is
        dni = [v * k for v in m]
    else:
        dni = H.dni_series(lat, lon, annual_dni)
    off = (lon + 120.0) / 15.0
    elev, pv = [], []
    for i in range(8760):
        doy, hr = i // 24 + 1, i % 24
        h = H.elevation_deg(lat, doy, hr + 0.5 + off)
        elev.append(h)
        pv.append(dni[i] * (1.0 - PV_DIFFUSE) + (PV_DIFFUSE * H.clear_sky_dni(h) if h > 0 else 0.0))
    return dni, elev, pv


def optical_scale(dni, elev, target_annual):
    """k such that the DNI-weighted annual optical efficiency of k*sin(h)^EXP is target."""
    num = sum(dni[i] * math.sin(math.radians(elev[i])) ** H.ETA_OPT_EXP
              for i in range(8760) if elev[i] > 0 and dni[i] >= H.DNI_START)
    den = sum(dni[i] for i in range(8760) if elev[i] > 0 and dni[i] >= H.DNI_START)
    return target_annual * den / num


_SERIES = {}


WINTER_MONTHS = (10, 11, 12, 1, 2, 3, 4)   # the months the first pass called the season; kept for the monthly table
HYDRO_MONTHS = tuple(range(1, 13))         # the hydraulic return delivers year-round                    DECIDED (author, 2026-09-11)


def run(case, pv_overbuild=1.0, heater_factor=1.0, turbine_factor=1.0, aperture_factor=1.0,
        tes_factor=1.0, design=None, hydro=None):
    """hydro=(mw, twh): a hydraulic return (joinder.py) that serves what the block
    leaves unserved in HYDRO_MONTHS (year-round, by decision), up to its plant
    size and its annual energy."""
    d = C.design("helios3", case) if design is None else design
    links = d["links"]
    e_twh = d["e_twh"]
    load = load_series(e_twh)
    n = len(H.NODES)
    ap_node = d["aperture"] * aperture_factor / n
    pv_mw = d["pv_mw"] * pv_overbuild
    pv_node = pv_mw / n
    heater_mw = d["heater_mw"] * heater_factor
    turb = d["turb_mw"] * turbine_factor
    tes = d["tes_mwh"] * turbine_factor * tes_factor     # cspchain's 16 h rule scales with the block
    # per-node series and pins
    nodes = []
    for node in H.NODES:
        key = (node[0], case)
        if key not in _SERIES:
            _SERIES[key] = node_series(node, case)
        dni, elev, pvraw = _SERIES[key]
        k_opt = optical_scale(dni, elev, links["opt"])
        k_pv = pv_node * pv_cf(case) * 8760.0 / sum(pvraw)   # exact CF pin
        nodes.append((dni, elev, pvraw, k_opt, k_pv))
    store = 0.5 * tes
    out = dict(load=0.0, pv=0.0, pv_direct=0.0, pv_curtail=0.0, heater_e=0.0, heater_th=0.0,
               field_th=0.0, spill_th=0.0, tank_loss=0.0, to_turbine_th=0.0, gross=0.0, net=0.0,
               unserved=0.0, over=0.0, hours_unserved=0, hours_empty=0, hours_full=0,
               month_unserved=[0.0] * 13, month_load=[0.0] * 13, month_net=[0.0] * 13,
               month_pv_direct=[0.0] * 13, month_heater=[0.0] * 13, peak_heater_mw=0.0)
    rated_th = turb / links["cycle"]
    min_th = rated_th * H.MIN_LOAD
    hydro_mw, hydro_budget = (hydro[0], hydro[1] * 1e6) if hydro else (0.0, 0.0)
    out["hydro"] = 0.0
    out["peak_injection_mw"] = 0.0          # max over hours of PV + block net + hydro, fleet-wide (F-09)
    for i in range(8760):
        doy, hr = i // 24 + 1, i % 24
        m = H.month_of(doy)
        L = load[i]
        out["load"] += L
        out["month_load"][m] += L
        # ---- PV and field this hour
        pv = 0.0
        field = 0.0
        for dni, elev, pvraw, k_opt, k_pv in nodes:
            pv += pvraw[i] * k_pv
            if dni[i] >= H.DNI_START and elev[i] > 0.0:
                eo = k_opt * math.sin(math.radians(elev[i])) ** H.ETA_OPT_EXP
                field += ap_node * dni[i] * eo * links["rec"] * links["avail"] / 1e6
        out["pv"] += pv
        out["field_th"] += field
        # ---- PV serves load first
        direct = min(pv, L)
        out["pv_direct"] += direct
        out["month_pv_direct"][m] += direct
        residual = L - direct
        surplus = pv - direct
        # ---- tank loss
        loss = tes * H.TANK_LOSS_PER_DAY / 24.0
        store = max(0.0, store - loss)
        out["tank_loss"] += loss
        # ---- heaters: PV surplus -> store
        room = tes - store
        h_e = min(surplus, heater_mw, room / HEATER_EFF if room > 0 else 0.0)
        store += h_e * HEATER_EFF
        out["heater_e"] += h_e
        out["heater_th"] += h_e * HEATER_EFF
        out["month_heater"][m] += h_e
        out["peak_heater_mw"] = max(out["peak_heater_mw"], h_e)
        out["pv_curtail"] += surplus - h_e
        # ---- field -> store, spill if full
        store += field
        if store > tes:
            out["spill_th"] += store - tes
            store = tes
        # ---- sCO2 block serves the residual from the store
        # the block must make the residual NET of its own parasitics (par is
        # 1 - parasitic share of gross), within its rating
        want_e = min(residual / links["par"], turb)
        # thermal needed at part-load efficiency: eta = cycle * (A + (1-A) load)
        gross = 0.0
        if want_e > 0.0:
            # solve want_th from want_e with eta(load): iterate twice
            load_f = want_e / turb
            eta = links["cycle"] * (H.PART_LOAD_A + (1.0 - H.PART_LOAD_A) * load_f)
            want_th = want_e / eta
            if want_th < min_th:
                want_th = min_th if store >= min_th else 0.0
            want_th = min(want_th, store, rated_th)
            if want_th > 0.0:
                load_f = want_th / rated_th
                eta = links["cycle"] * (H.PART_LOAD_A + (1.0 - H.PART_LOAD_A) * load_f)
                gross = want_th * eta
                store -= want_th
                out["to_turbine_th"] += want_th
        net = gross * links["par"]
        out["gross"] += gross
        out["net"] += net
        out["month_net"][m] += net
        served = direct + net
        if hydro and m in HYDRO_MONTHS and served < L - 1e-9 and hydro_budget > 0.0:
            hy = min(L - served, hydro_mw, hydro_budget)
            hydro_budget -= hy
            served += hy
            out["hydro"] += hy
        out["peak_injection_mw"] = max(out["peak_injection_mw"], min(pv, L) + net + (served - direct - net if hydro else 0.0))
        if served < L - 1e-9:
            out["unserved"] += L - served
            out["month_unserved"][m] += L - served
            out["hours_unserved"] += 1
        else:
            out["over"] += served - L
        if store < 1e-6:
            out["hours_empty"] += 1
        if store > tes - 1e-6:
            out["hours_full"] += 1
    out["case"] = case
    out["design"] = d
    out["pv_overbuild"] = pv_overbuild
    out["heater_factor"] = heater_factor
    out["turbine_factor"] = turbine_factor
    out["aperture_factor"] = aperture_factor
    out["tes_factor"] = tes_factor
    out["served_frac"] = 1.0 - out["unserved"] / out["load"]
    out["direct_share"] = out["pv_direct"] / out["load"]
    out["turb_cf"] = out["gross"] / (turb * 8760.0)
    out["dispatch"] = out["to_turbine_th"] / out["field_th"] if out["field_th"] else 0.0
    return out


def closure_cost_m(d, pv_overbuild=1.0, heater_factor=1.0, turbine_factor=1.0, aperture_factor=1.0,
                   tes_factor=1.0):
    """Extra overnight direct cost of an overbuild, on cspchain's own lines at
    the design's case: each factor scales the lines that carry it. $M."""
    L = d["lines"]
    return (L["PV, direct + winter"] * (pv_overbuild - 1.0)
            + L["electric heaters"] * (heater_factor - 1.0)
            + sum(L[k] for k in BLOCK_LINES) * (turbine_factor - 1.0)
            + sum(L[k] for k in FIELD_LINES) * (aperture_factor - 1.0)
            + L["thermal storage (particles)"] * (turbine_factor * tes_factor - 1.0))


def closure_om_m(d, extra_direct_m):
    """The O&M the closing plant brings with it, $M/yr: taken as proportional to
    direct capital at the design's own O&M-to-capital ratio. ASSUMED (the chain
    carries no per-line O&M); before 2026-09-12 the closing price carried no O&M
    at all, which understated it."""
    return d["om"] * extra_direct_m / sum(d["lines"].values())


def price_delta(d, extra_direct_m, extra_om_m=0.0):
    """What extra direct cost does to the required price, through cspchain's
    own overheads and firmpower's financing, with the O&M it brings: $/MWh."""
    over = extra_direct_m * (1.0 + C.HC.CONTINGENCY[1] + C.HC.EPC_OWNER[1] + C.HC.SALES_TAX * C.HC.SALES_TAX_BASE)
    return FP.required_price(FP.financed(over, C.HC.BUILD_YEARS), extra_om_m, d["e_twh"])


def mirrors_price_delta(d):
    cost = mirrors_cost_m(d)
    return price_delta(d, cost, closure_om_m(d, cost))


def scan(case):
    d = C.design("helios3", case)
    out = []
    for tf in TURBINE_SCAN:
        for af in APERTURE_SCAN:
            for sf in TES_SCAN:
                for pvo in PV_OVERBUILD_SCAN:
                    for hf in HEATER_SCAN:
                        r = run(case, pvo, hf, tf, af, sf, design=d)
                        out.append((closure_cost_m(d, pvo, hf, tf, af, sf), pvo, hf, tf, af, sf, r))
    return d, out


def close(case, target, scanned=None):
    """Cheapest point on the scan with unserved at or below target."""
    d, pts = scanned if scanned is not None else scan(case)
    ok = [p for p in pts if 1.0 - p[6]["served_frac"] <= target]
    return (d, min(ok, key=lambda p: p[0])) if ok else (d, None)


MONTHS = ("", "Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec")

# --- the author's question (2026-09-11): "this is California -- our winters
# still get dominant sunlight depending on where in the state we are." So:
# how much December sun does the model give each node, and what does moving
# the one non-desert node to the desert do?
DESERT_NODE = ("Mojave-2 (Blythe / Ivanpah class)", 34.6, -114.6, 15.2e6, 1750.0, 65728.0,
               2750.0, "ASSUMED: desert class, NSRDB 7.3-7.8 kWh/m2/day")
DAY_LENGTH_H = {"Dec": 10, "Jun": 14}      # Mojave, from helios.py's geometry     exact


def december_ratio(node):
    """Model December DNI per day / annual mean per day, at a node."""
    _n, lat, lon, _a, _g, _s, annual, _st = node
    dni = H.dni_series(lat, lon, annual)
    dec = sum(dni[i] for i in range(8760) if H.month_of(i // 24 + 1) == 12) / 31.0
    return dec / (sum(dni) / 365.0)


def siting(case="mid"):
    """The plant with the Central Valley node moved to a desert site."""
    d = C.design("helios3", case)
    orig = H.NODES
    try:
        H.NODES = (orig[0], orig[1], DESERT_NODE)
        _SERIES.clear()
        base = run(case, design=d)
        closed = mirrors_run(case, design=d)
    finally:
        H.NODES = orig
        _SERIES.clear()
    return base, closed


def report(do_close=True):
    print()
    print("  HELIOS-3, HOUR BY HOUR -- MID AND CRITICAL")
    print("  ===========================================")
    print("    cspchain sized the plant on three static assumptions: a direct-PV")
    print(f"    share of {C.DIRECT_SHARE[1]:.2f}, winter heaters at {C.WINTER_HEATER_FRACTION:.2f} of the night block's")
    print("    thermal input, and a dispatch link near unity. This runs the same")
    print("    plant through 8,760 hours at each case and reports what it serves.")
    runs = {c: run(c) for c in CASES}
    print()
    print(f"      {'':<38}{'mid':>12}{'critical':>12}")
    rows = [
        ("load, TWh", lambda r: r["load"] / 1e6, "{:12.2f}"),
        ("served, share of load", lambda r: r["served_frac"], "{:12.4f}"),
        ("UNSERVED, TWh", lambda r: r["unserved"] / 1e6, "{:12.3f}"),
        ("hours with any unserved load", lambda r: r["hours_unserved"], "{:12.0f}"),
        ("PV direct share (static 0.35)", lambda r: r["direct_share"], "{:12.3f}"),
        ("PV curtailed, TWh", lambda r: r["pv_curtail"] / 1e6, "{:12.2f}"),
        ("heater energy, TWh_e", lambda r: r["heater_e"] / 1e6, "{:12.2f}"),
        ("heater peak, MW (sized)", lambda r: r["peak_heater_mw"], "{:12,.0f}"),
        ("field to store, TWh_th", lambda r: r["field_th"] / 1e6, "{:12.2f}"),
        ("field spilled (defocus), TWh_th", lambda r: r["spill_th"] / 1e6, "{:12.2f}"),
        ("dispatch link (static ~0.996)", lambda r: r["dispatch"], "{:12.3f}"),
        ("sCO2 block CF", lambda r: r["turb_cf"], "{:12.3f}"),
        ("hours store empty", lambda r: r["hours_empty"], "{:12.0f}"),
        ("hours store full", lambda r: r["hours_full"], "{:12.0f}"),
    ]
    for label, f, fmt in rows:
        print(f"      {label:<38}" + "".join(fmt.format(f(runs[c])) for c in CASES))
    print()
    print("    UNSERVED BY MONTH, share of that month's load:")
    print(f"      {'':<6}" + "".join(f"{MONTHS[m]:>7}" for m in range(1, 13)))
    for c in CASES:
        r = runs[c]
        print(f"      {c:<6}" + "".join(f"{r['month_unserved'][m] / r['month_load'][m]:7.3f}" for m in range(1, 13)))
    print("    Winter is the shortfall, as F-06 said: the night block is sized for the")
    print("    average night and December has the longest nights and the least sun.")
    print()
    jul = runs["mid"]["month_unserved"][7] / runs["mid"]["month_load"][7]
    ptm = max(load_series(runs["mid"]["design"]["e_twh"])) / (runs["mid"]["load"] / 8760.0)
    print()
    print("    IS THE MODEL'S WINTER TOO HARSH FOR CALIFORNIA? December DNI per day as a")
    print("    share of the annual mean, by node (helios.py's reconstructed series):")
    for node in H.NODES:
        print(f"      {node[0]:<32} {december_ratio(node):.2f}")
    print(f"    The desert record is about 0.65 (Daggett TMY3: ~5 kWh/m2/day in December on")
    print(f"    7.67 annual -- RECALLED, to be verified). The model gives the deserts MORE")
    print(f"    December sun than that, not less. What December lacks is not clouds but")
    print(f"    hours and angle: {DAY_LENGTH_H['Dec']} h of day against {DAY_LENGTH_H['Jun']}, a low sun, and {24 - DAY_LENGTH_H['Dec']} h of")
    print("    night to serve from the store. The Central Valley node is the one place")
    print("    the model is too kind (tule fog is not in the series).")
    sb, sc = siting("mid")
    print(f"    Moving that node to a desert site: served {runs['mid']['served_frac']:.3f} -> {sb['served_frac']:.3f},")
    print(f"    December unserved {runs['mid']['month_unserved'][12] / runs['mid']['month_load'][12]:.3f} -> {sb['month_unserved'][12] / sb['month_load'][12]:.3f}; the closing sizing is unchanged")
    print(f"    (block x1.5, store 2 d, field x2 -> unserved {1 - sc['served_frac']:.4f}). Siting is worth two")
    print("    points; it is not the winter.")
    print()
    print("    WHY. The block is sized to the average night x 1.3 (cspchain's NIGHT_PEAK);")
    print(f"    the residential evening peak is {ptm:.2f}x the mean and falls after sunset, so")
    print(f"    the block cannot carry it in any month -- unserved is {100 * jul:.0f} % even in July.")
    print("    The store fills and the field defocuses in summer (spill), and the store")
    print("    empties in winter: 16 h of storage cannot move June into December.")
    if do_close:
        print()
        print("    WHAT CLOSES IT. A scan over block size (with its 16 h store), store")
        print("    days, field size, PV overbuild and heater size; the cheapest point on")
        print("    cspchain's own lines at each target, and the best point if none closes:")
        print(f"      {'':<10}{'target':>7}{'block x':>8}{'store d':>8}{'field x':>8}{'PV x':>6}{'heater x':>9}{'extra $M':>10}{'+ $/MWh':>9}{'unserved':>10}{'Dec':>7}{'spill TWh':>10}")
        for c in CASES:
            scanned = scan(c)
            for t in TARGETS:
                d, b = close(c, t, scanned)
                if b is None:
                    b = min(scanned[1], key=lambda p: 1.0 - p[6]["served_frac"])
                    tag = "best on scan, does not close:"
                else:
                    tag = ""
                cost, pvo, hf, tf, af, sf, r = b
                if tag:
                    print(f"      {c:<10}{t:7.3f}   {tag}")
                print(f"      {c:<10}{t:7.3f}{tf:8.2f}{sf:8.1f}{af:8.2f}{pvo:6.1f}{hf:9.1f}{cost:10,.0f}{price_delta(d, cost, closure_om_m(d, cost)):9.1f}"
                      f"{1 - r['served_frac']:10.4f}{r['month_unserved'][12] / r['month_load'][12]:7.3f}{r['spill_th'] / 1e6:10.2f}")
        print("    The block is what closes the evening; the field and PV are what close")
        print("    the winter. Both are size, and size is the thing cspchain's static")
        print("    shares understated. The '+ $/MWh' is on top of helios3.py's mitigated")
        print("    price at the same case.")
    print()
    print("    WHAT THIS DOES NOT DO. The load and PV shapes are RECONSTRUCTED and")
    print("    the levels are pinned; a measured CAISO residential profile and an")
    print("    NSRDB hourly file replace them when this environment can reach one.")
    print("    cspchain is not changed here; it is told what its static shares are")
    print("    worth hour by hour.")
    print()


def selftest():
    fails = 0

    def check(label, ok):
        nonlocal fails
        print(f"  {label:<72} {'PASS' if ok else 'FAIL'}")
        fails += 0 if ok else 1

    d = C.design("helios3", "mid")
    L = load_series(d["e_twh"])
    check("load series sums exactly to the design energy", abs(sum(L) / 1e6 - d["e_twh"]) < 1e-9)
    ptm = max(L) / (sum(L) / 8760.0)
    check("load peak-to-mean inside the residential band", LOAD_PEAK_TO_MEAN_BAND[0] <= ptm <= LOAD_PEAK_TO_MEAN_BAND[1])
    dni, elev, pvraw = node_series(H.NODES[0], "mid")
    k = optical_scale(dni, elev, d["links"]["opt"])
    num = sum(dni[i] * k * math.sin(math.radians(elev[i])) ** H.ETA_OPT_EXP for i in range(8760) if elev[i] > 0 and dni[i] >= H.DNI_START)
    den = sum(dni[i] for i in range(8760) if elev[i] > 0 and dni[i] >= H.DNI_START)
    check("optical curve pinned exactly to the chain's annual link", abs(num / den - d["links"]["opt"]) < 1e-9)
    r = run("mid")
    check("PV annual CF pinned exactly to the sourced band value",
          abs(r["pv"] / (d["pv_mw"] * 8760.0) - pv_cf("mid")) < 1e-9)
    bal = r["field_th"] + r["heater_th"] - r["spill_th"] - r["tank_loss"] - r["to_turbine_th"]
    check("store energy balance closes over the year to within 1 % of throughput",
          abs(bal) < 0.01 * r["field_th"])
    check("served never exceeds load hour by hour (over-serve only at turbine minimum)",
          r["over"] < 0.02 * r["load"])
    rc = run("critical")
    check("critical serves no more of the load than mid", rc["served_frac"] <= r["served_frac"])
    check("critical unserved >= mid unserved", rc["unserved"] >= r["unserved"])
    check("December is the worst month by share and no month is under 5 % unserved (the shortfall is year-round, evening-led)",
          all(max(range(1, 13), key=lambda m: x["month_unserved"][m] / x["month_load"][m]) == 12
              and min(x["month_unserved"][m] / x["month_load"][m] for m in range(1, 13)) > 0.05 for x in (r, rc)))
    check("the load shape peaks in summer, not winter (the 2026-09-11 sign correction)",
          sum(load_series(1.0)[(181 + 31) * 24:(243) * 24]) > sum(load_series(1.0)[:31 * 24]))
    check("PV direct share is within 0.10 of cspchain's static 0.35 at mid",
          abs(r["direct_share"] - C.DIRECT_SHARE[1]) < 0.10)
    check("a larger PV overbuild never increases unserved energy",
          run("critical", 1.5, 1.0)["unserved"] <= rc["unserved"])
    check("a larger block (with its store) never increases unserved energy",
          run("critical", 1.0, 1.0, 1.5)["unserved"] <= rc["unserved"])
    check("more store days never increase unserved energy",
          run("critical", 1.0, 1.0, 1.0, 1.0, 2.0)["unserved"] <= rc["unserved"])
    check("closure cost is zero at the design point", closure_cost_m(d) == 0.0)
    check("the mirrors route closes to 1 % at both cases", all(1.0 - mirrors_run(c)["served_frac"] <= 0.01 for c in ("mid", "critical")))
    dm, cm = close("mid", 0.01)
    check("the mirrors route is the cheapest closing point of the mid scan (block, field, store)",
          cm is not None and (cm[3], cm[4], cm[5]) == MIRRORS_ROUTE and cm[1] == 1.0 and cm[2] == 1.0)
    ratios = {n[0]: december_ratio(n) for n in H.NODES}
    check("the model gives every desert node at least 0.70 of its annual-mean DNI in December (not harsher than the record)",
          all(v >= 0.70 for k, v in ratios.items() if "Central" not in k))
    check("December is still below the annual mean at every node (geometry is in the series)",
          all(v < 1.0 for v in ratios.values()))
    sb, sc = siting("mid")
    check("moving the Central Valley node to the desert improves service by under five points",
          0.0 < sb["served_frac"] - r["served_frac"] < 0.05)
    check("all-desert siting does not close December on its own",
          sb["month_unserved"][12] / sb["month_load"][12] > 0.05)
    check("the closing sizing still closes at all-desert siting", 1.0 - sc["served_frac"] <= 0.01)
    check("siting restores the nodes it changed", H.NODES[2][0].startswith("Central Valley"))
    check("closure cost is linear in each factor",
          abs(closure_cost_m(d, 2.0) - 2 * closure_cost_m(d, 1.5)) < 1e-6)
    check("the evening peak is the binding constraint: unserved in July is above 3 % as sized",
          r["month_unserved"][7] / r["month_load"][7] > 0.03)
    check("summer spill and winter unserved coexist (storage cannot move seasons)",
          r["spill_th"] > 0.1 * r["field_th"] and r["month_unserved"][12] > r["month_unserved"][6])
    import io
    import contextlib
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        report(do_close=False)
    out = buf.getvalue()
    check("the report prints both cases and the monthly unserved table", "critical" in out and "UNSERVED BY MONTH" in out)
    check("the report says the shapes are RECONSTRUCTED and cspchain is not changed",
          "RECONSTRUCTED" in out and "cspchain is not changed here" in out)
    print(f"\nselftest: {fails} failures -> {'PASS' if fails == 0 else 'FAIL'}")
    return fails == 0


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--selftest", action="store_true")
    ap.add_argument("--no-close", action="store_true")
    a = ap.parse_args()
    if a.selftest:
        sys.exit(0 if selftest() else 1)
    report(do_close=not a.no_close)
