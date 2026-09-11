#!/usr/bin/env python3
"""profiles.py -- the measured load and solar profiles, ingested and pinned.

hourly3.py runs Helios-3 on two RECONSTRUCTED shapes -- a California load
shape and per-node DNI series -- each pinned to a sourced annual level. The
measured files that would replace them (a CAISO hourly demand year, an NSRDB
hourly DNI file per node) are unreachable from this environment: every route
returns nothing at the egress proxy. This file is the ingestion path, so that
when the files exist the swap is a drop-in that has already been tested:

  1. read and VALIDATE a CAISO demand CSV (8,760 hourly MW; 8,784 in a leap
     year, 29 February dropped; no gaps, no non-positive values) and an NSRDB
     CSV per node (the two-row metadata header, then Year,Month,Day,Hour,
     Minute,...,DNI...; 8,760 rows; DNI in W/m2 within 0-1,200);
  2. ATTACH them to hourly3.py, which pins each to the same sourced annual
     level it pins the reconstruction to -- the annual energy and the annual
     DNI do not move; only the SHAPE does -- and stamps the run MEASURED;
  3. COMPARE: the shape statistics that decide whether the closing sizing
     moves -- peak/mean, the evening peak hour, the summer/winter ratio, the
     December DNI share -- reconstructed against measured, and the served
     fraction and closing sizing re-run on the measured shapes.

The selftest builds a synthetic fixture from the reconstruction plus noise,
round-trips it, and proves the hook is live (the served fraction moves) and
the pin holds (the annual energy does not). Stdlib only.
"""
import argparse
import csv
import io
import math
import os
import random
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import helios as H                                              # noqa: E402
import hourly3 as HR                                            # noqa: E402

HOURS = 8760
DNI_MAX_W_M2 = 1200.0                     # physical ceiling for an hourly DNI               SOURCED (clear-sky ~1,000-1,100)
FIXTURE_NOISE = 0.15                      # relative noise the synthetic fixture adds        selftest only
FETCH = {
    "load": "CAISO OASIS: report SLD_FCST / actual system demand, TAC_AREA_NAME=CA ISO-TAC, hourly, one calendar year; "
            "or Today's Outlook history CSVs concatenated. Columns: timestamp, MW.",
    "dni": "NREL NSRDB PSM3 (developer.nrel.gov/api/nsrdb/v2/solar/psm3-2-2-download.csv): "
           "wkt=POINT(lon lat) per node, names=tmy (or a named year), attributes=dni, interval=60, utc=false. "
           "Two metadata rows then a header; DNI in W/m2.",
}


# ---- read and validate ------------------------------------------------------------
def _drop_feb29(rows_by_date):
    return [v for (m, d), v in rows_by_date if not (m == 2 and d == 29)]


def read_load(path):
    """CAISO hourly demand -> 8,760 MW values. Refuses gaps, wrong length, non-positive."""
    vals, dates = [], []
    with open(path, newline="", encoding="utf-8") as f:
        rd = csv.reader(f)
        header = next(rd)
        for row in rd:
            if not row or not row[0].strip():
                continue
            ts, mw = row[0].strip(), float(row[-1])
            m, d = int(ts[5:7]), int(ts[8:10])
            dates.append((m, d))
            vals.append(mw)
    if len(vals) == HOURS + 24:
        vals = _drop_feb29(list(zip(dates, vals)))
    if len(vals) != HOURS:
        raise ValueError(f"load file has {len(vals)} hourly rows, need {HOURS} (or {HOURS + 24} with 29 Feb)")
    if min(vals) <= 0.0:
        raise ValueError("load file carries a non-positive hour: a gap, not a measurement")
    return vals


def read_nsrdb(path):
    """NSRDB PSM3 CSV -> 8,760 hourly DNI W/m2. Refuses wrong length or out-of-range values."""
    with open(path, encoding="utf-8") as f:
        lines = f.read().splitlines()
    body = "\n".join(lines[2:])                 # two metadata rows
    rd = csv.DictReader(io.StringIO(body))
    vals, dates = [], []
    for row in rd:
        if row.get("DNI") in (None, ""):
            continue
        vals.append(float(row["DNI"]))
        dates.append((int(row["Month"]), int(row["Day"])))
    if len(vals) == HOURS + 24:
        vals = _drop_feb29(list(zip(dates, vals)))
    if len(vals) != HOURS:
        raise ValueError(f"NSRDB file has {len(vals)} hourly rows, need {HOURS}")
    if min(vals) < 0.0 or max(vals) > DNI_MAX_W_M2:
        raise ValueError(f"NSRDB DNI outside 0-{DNI_MAX_W_M2:.0f} W/m2")
    return vals


# ---- attach ------------------------------------------------------------------------
def attach(load=None, dni=None):
    """load: 8,760 MW (any scale; hourly3 pins it). dni: {node name: 8,760 W/m2}."""
    HR.MEASURED["load"] = list(load) if load is not None else None
    HR.MEASURED["dni"] = {k: list(v) for k, v in (dni or {}).items()}
    HR._SERIES.clear()


def detach():
    attach(None, None)


def status():
    return dict(load="MEASURED" if HR.MEASURED["load"] is not None else "RECONSTRUCTED",
                dni={n[0]: ("MEASURED" if n[0] in HR.MEASURED["dni"] else "RECONSTRUCTED") for n in H.NODES})


# ---- compare -----------------------------------------------------------------------
def load_stats(series):
    mean = sum(series) / HOURS
    by_hour = [0.0] * 24
    for i, v in enumerate(series):
        by_hour[i % 24] += v
    peak_hour = max(range(24), key=lambda h: by_hour[h])
    def month_mean(months):
        vals = [v for i, v in enumerate(series) if _month(i) in months]
        return sum(vals) / len(vals)
    return dict(peak_over_mean=max(series) / mean, peak_hour=peak_hour,
                summer_over_winter=month_mean((7, 8)) / month_mean((12, 1)))


def dni_stats(series):
    annual = sum(series) / 1e3
    dec = [v for i, v in enumerate(series) if _month(i) == 12]
    return dict(annual_kwh_m2=annual, dec_share=(sum(dec) / 31.0) / (annual * 1e3 / 365.0))


_MONTH_START = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334, 365]


def _month(i):
    doy = i // 24
    for m in range(12):
        if doy < _MONTH_START[m + 1]:
            return m + 1
    return 12


def compare(case="mid"):
    """Reconstructed against measured on the shape statistics and the plant's served share."""
    d = HR.C.design("helios3", case)
    attached = dict(load=HR.MEASURED["load"], dni=dict(HR.MEASURED["dni"]))
    detach()
    rec = dict(load=load_stats(HR.load_series(d["e_twh"])), run=HR.run(case, design=d),
               dni={n[0]: dni_stats(HR.node_series(n, case)[0]) for n in H.NODES})
    attach(attached["load"], attached["dni"])
    mea = dict(load=load_stats(HR.load_series(d["e_twh"])), run=HR.run(case, design=d),
               dni={n[0]: dni_stats(HR.node_series(n, case)[0]) for n in H.NODES})
    return rec, mea


def fixture(seed=0):
    """A synthetic measured set: the reconstruction with hourly noise, so the hook can be tested."""
    rng = random.Random(seed)
    d = HR.C.design("helios3", "mid")
    detach()
    load = [v * (1.0 + FIXTURE_NOISE * (rng.random() - 0.5)) for v in HR.load_series(d["e_twh"])]
    dni = {}
    for n in H.NODES:
        base = HR.node_series(n, "mid")[0]
        dni[n[0]] = [min(DNI_MAX_W_M2, max(0.0, v * (1.0 + FIXTURE_NOISE * (rng.random() - 0.5)))) for v in base]
    return load, dni


def write_fixture_files(dirpath, seed=0):
    """Write the fixture in the two file formats read_load / read_nsrdb expect."""
    load, dni = fixture(seed)
    os.makedirs(dirpath, exist_ok=True)
    lp = os.path.join(dirpath, "caiso_demand_fixture.csv")
    with open(lp, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["timestamp", "MW"])
        for i, v in enumerate(load):
            m = _month(i)
            day = i // 24 - _MONTH_START[m - 1] + 1
            w.writerow([f"2024-{m:02d}-{day:02d} {i % 24:02d}:00", f"{v:.3f}"])
    dps = {}
    for name, series in dni.items():
        fp = os.path.join(dirpath, f"nsrdb_{name.split()[0].lower()}_fixture.csv")
        with open(fp, "w", newline="", encoding="utf-8") as f:
            f.write("Source,Location ID,City,State,Country,Latitude,Longitude,Time Zone,Elevation\n")
            f.write("NSRDB,fixture,-,CA,USA,0,0,-8,0\n")
            w = csv.writer(f)
            w.writerow(["Year", "Month", "Day", "Hour", "Minute", "DNI"])
            for i, v in enumerate(series):
                m = _month(i)
                day = i // 24 - _MONTH_START[m - 1] + 1
                w.writerow([2024, m, day, i % 24, 0, f"{v:.1f}"])
        dps[name] = fp
    return lp, dps


def report(load_path=None, dni_paths=None):
    print()
    print("  THE MEASURED PROFILES: INGESTION PATH")
    print("  ======================================")
    print("    Sources (unreachable here; every route returns nothing at the proxy):")
    for k, v in FETCH.items():
        print(f"      {k:<5} {v}")
    if not load_path and not dni_paths:
        print()
        print("    No files given. Status: " + str(status()))
        print("    Run with --load <caiso.csv> --dni <node>=<nsrdb.csv> ... to attach and compare;")
        print("    --fixture writes a synthetic set in the right formats to a directory.")
        return
    load = read_load(load_path) if load_path else None
    dni = {n: read_nsrdb(p) for n, p in (dni_paths or {}).items()}
    attach(load, dni)
    print(f"\n    Attached. Status: {status()}")
    for case in ("mid", "critical"):
        rec, mea = compare(case)
        print(f"\n    {case.upper()} -- reconstructed vs measured")
        print(f"      {'load shape':<32}{'reconstructed':>15}{'measured':>12}")
        for k in ("peak_over_mean", "peak_hour", "summer_over_winter"):
            print(f"      {k:<32}{rec['load'][k]:>15.2f}{mea['load'][k]:>12.2f}")
        for n in H.NODES:
            print(f"      {'December DNI share, ' + n[0].split()[0]:<32}{rec['dni'][n[0]]['dec_share']:>15.2f}{mea['dni'][n[0]]['dec_share']:>12.2f}")
        print(f"      {'served share, as sized':<32}{rec['run']['served_frac']:>15.3f}{mea['run']['served_frac']:>12.3f}")
        print(f"      {'annual load, TWh (pinned)':<32}{rec['run']['load'] / 1e6:>15.2f}{mea['run']['load'] / 1e6:>12.2f}")
    print("\n    The annual levels are pinned and do not move; the shape does. If the served share")
    print("    moves, re-run both.py and the renderers: the closing sizing is the shape's.")


def selftest():
    fails = 0

    def check(label, ok):
        nonlocal fails
        print(f"  {label:<72} {'PASS' if ok else 'FAIL'}")
        fails += 0 if ok else 1

    tmp = os.path.join(os.environ.get("TMPDIR", "/tmp"), "profiles_selftest")
    lp, dps = write_fixture_files(tmp)
    load = read_load(lp)
    dni = {n: read_nsrdb(p) for n, p in dps.items()}
    check("the fixture round-trips through the CAISO reader at 8,760 rows", len(load) == HOURS)
    check("the fixture round-trips through the NSRDB reader for every node", all(len(v) == HOURS for v in dni.values()) and set(dni) == {n[0] for n in H.NODES})
    detach()
    d = HR.C.design("helios3", "mid")
    base = HR.run("mid", design=d)
    check("detached, the status is RECONSTRUCTED everywhere", status()["load"] == "RECONSTRUCTED" and all(v == "RECONSTRUCTED" for v in status()["dni"].values()))
    attach(load, dni)
    check("attached, the status is MEASURED everywhere", status()["load"] == "MEASURED" and all(v == "MEASURED" for v in status()["dni"].values()))
    meas = HR.run("mid", design=d)
    check("the hook is live: the served share moves on a different shape", abs(meas["served_frac"] - base["served_frac"]) > 1e-4)
    check("the pin holds: the annual load does not move", abs(meas["load"] - base["load"]) < 1e-3)
    for n in H.NODES:
        s = HR.node_series(n, "mid")[0]
        check(f"the pin holds on DNI: {n[0].split()[0]} annual is the sourced figure", abs(sum(s) / 1e3 - n[6]) < 1e-6)
    detach()
    again = HR.run("mid", design=d)
    check("detached again, the base run is reproduced exactly", again["served_frac"] == base["served_frac"])
    # refusals
    bad = os.path.join(tmp, "short.csv")
    with open(bad, "w", encoding="utf-8") as f:
        f.write("timestamp,MW\n" + "\n".join(f"2024-01-01 {h:02d}:00,1000" for h in range(24)))
    try:
        read_load(bad); check("a short load file is refused", False)
    except ValueError:
        check("a short load file is refused", True)
    gap = os.path.join(tmp, "gap.csv")
    with open(gap, "w", encoding="utf-8") as f:
        f.write("timestamp,MW\n")
        for i in range(HOURS):
            m = _month(i); day = i // 24 - _MONTH_START[m - 1] + 1
            f.write(f"2024-{m:02d}-{day:02d} {i % 24:02d}:00,{0 if i == 4000 else 1000}\n")
    try:
        read_load(gap); check("a load file with a zero hour is refused as a gap", False)
    except ValueError:
        check("a load file with a zero hour is refused as a gap", True)
    leap = os.path.join(tmp, "leap.csv")
    with open(leap, "w", encoding="utf-8") as f:
        f.write("timestamp,MW\n")
        for i in range(HOURS + 24):
            f.write(f"2024-{'02' if 1416 <= i < 1440 else '01'}-{'29' if 1416 <= i < 1440 else '01'} {i % 24:02d}:00,1000\n")
    check("a leap-year file drops 29 February to 8,760", len(read_load(leap)) == HOURS)
    check("the fetch instructions name both sources", "CAISO" in FETCH["load"] and "NSRDB" in FETCH["dni"])
    print(f"\nselftest: {fails} failures -> {'PASS' if fails == 0 else 'FAIL'}")
    return fails == 0


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--selftest", action="store_true")
    ap.add_argument("--load", help="CAISO hourly demand CSV")
    ap.add_argument("--dni", action="append", default=[], help="<node name>=<NSRDB csv>; repeatable")
    ap.add_argument("--fixture", help="write a synthetic fixture set to this directory")
    a = ap.parse_args()
    if a.selftest:
        sys.exit(0 if selftest() else 1)
    if a.fixture:
        lp, dps = write_fixture_files(a.fixture)
        print(f"wrote {lp} and {len(dps)} NSRDB fixtures")
        sys.exit(0)
    dni = dict(x.split("=", 1) for x in a.dni)
    report(a.load, dni or None)
