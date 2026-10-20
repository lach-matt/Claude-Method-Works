#!/usr/bin/env python3
"""seriesdefect.py -- what the 25 non-integer values in COORDINATES-2.13's B column are.

Why it exists. The spectra index's B column holds the Pauli bound, an integer, in every row but
25. Those 25 are measured rows from one NIST fetch (2026-08-14), and they carry a float. The site
said only that the float was "a dispersion of the median defect, not a bound", and the series
limit printed in the same rows' bound note ("limit 41449.451; one electron outside a closed
shell") was shown "as the csv prints it, with no unit added". Neither was measured. This
instrument measures both.

What it finds, from NIST's own levels:

  * the printed limits are the neutral ionisation energies in cm^-1. Each of the nine equals
    the ground-state ionisation energy NIST ASD prints for that spectrum, to every printed
    digit (NIST_IE_CM1 below, read from NIST's ionisation-energy service on 2026-10-17);
  * delta is the MEDIAN quantum defect of the series and B is its RANGE, max - min. Take the
    series' members from NIST's levels (distinct energies of single-valence configurations whose
    last subshell carries the term's l, below the limit, n within the printed run). Each member's
    defect is n - sqrt(R_M / (limit - E)), and R_M is the Rydberg reduced by the element's
    standard atomic weight. That rule reproduces every printed member count, n range, delta and B,
    25 of 25 to the five decimals printed;
  * the reduced-mass Rydberg is what the source used: with R_inf no delta reproduces. Boron
    reproduces only with the standard atomic weight (10.81), not with 11B, which fixes the mass
    convention as the standard atomic weight. Francium has none, so 223Fr's mass from the held
    AME2020 table is used, and with a single isotope the two conventions coincide.

How the levels were reached. physics.nist.gov is refused by this environment's proxy, so the
listings were fetched through a web-fetch connector on 2026-10-17, from the energy-levels
service in CSV form (energy1.pl, units=0, i.e. cm^-1). Only the rows a series can be drawn from
were kept: every single-valence row below the first limit, and that limit. They are in
tables/nist-levels/ with their capture recorded in that directory's README, and nothing there is
hand-edited.

What it refuses. It does not say why the source chose the range over another spread, and it does
not treat the range as a bound: the site shows it under its own name and compares it with nothing.

READ and RECOVERED: the levels, limits and masses are READ, the identity is RECOVERED (measured out
of the corpus's own data against its stated source). stdlib only.

    python3 tools/seriesdefect.py              # the 25 rows, printed against the recomputation
    python3 tools/seriesdefect.py --json       # the same as JSON
    python3 tools/seriesdefect.py --selftest   # 25 of 25 with R_M, none of the deltas with R_inf
"""
import argparse
import csv
import importlib.util
import json
import math
import os
import re
import statistics
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SPECTRA = os.path.join(ROOT, "drive", "The Method Materials", "COORDINATES-2_13.csv")
LEVELS_DIR = os.path.join(ROOT, "tables", "nist-levels")
WEIGHTS = os.path.join(ROOT, "tables", "ciaaw", "STANDARD-ATOMIC-WEIGHTS.tsv")

R_INF = 109737.31568160      # cm^-1, CODATA 2018
M_E_U = 5.48579909065e-4     # the electron's mass in u, CODATA 2018

# The ground-state ionisation energies NIST ASD prints, in cm^-1, with their uncertainties, as
# its ionisation-energy service returned them on 2026-10-17 (ie.pl, units=0). READ.
NIST_IE_CM1 = {
    "B": ("66928.040", "0.022"), "Na": ("41449.451", "0.002"), "Al": ("48278.480", "0.025"),
    "Ga": ("48387.634", "0.010"), "In": ("46670.107", "0.004"), "Cs": ("31406.4677325", "0.0000014"),
    "Lu": ("43762.60", "0.10"), "Tl": ("49266.66", "0.01"), "Fr": ("32848.872", "0.009"),
}

LETTER = {"S": 0, "P": 1, "D": 2, "F": 3, "G": 4, "H": 5, "I": 6}
SUBSHELL = "spdfghik"


def float_rows(path=SPECTRA):
    """The rows whose B is not an integer, each with its series parsed out of the source text."""
    out = []
    with open(path, encoding="utf-8-sig", newline="") as fh:
        for r in csv.DictReader(fh):
            if r["B"].lstrip("-").isdigit():
                continue
            m = re.search(r"([A-Z][a-z]?)I (\d)([SPDFGHI])(\*?) n=(\d+)-(\d+), (\d+) members; median defect",
                          r["source"])
            lim = re.match(r"limit ([0-9.]+);", r["bound"])
            if not m or not lim:
                raise ValueError("a float B row this instrument cannot read: %r" % (r,))
            out.append({
                "Z": int(r["Z"]), "charge": int(r["charge"]), "l": int(r["l"]), "mult": int(r["mult"]),
                "grade": r["grade"],
                "symbol": m.group(1), "term": m.group(2) + m.group(3) + m.group(4),
                "n_min": int(m.group(5)), "n_max": int(m.group(6)), "members": int(m.group(7)),
                "delta": r["delta"], "B": r["B"], "limit": lim.group(1),
            })
    return out


def _isotopes():
    spec = importlib.util.spec_from_file_location("isotopes", os.path.join(ROOT, "tools", "isotopes.py"))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def masses(symbols):
    """The mass the reduced Rydberg is taken at: the CIAAW standard atomic weight, or, for an
    element with none, the mass of its one isotope in the held AME2020 table (223Fr)."""
    out = {}
    with open(WEIGHTS, encoding="utf-8") as fh:
        for r in csv.DictReader(fh, delimiter="\t"):
            if r["symbol"] in symbols:
                out[r["symbol"]] = (float(r["value"]), "the standard atomic weight (CIAAW)")
    missing = [s for s in symbols if s not in out]
    if missing:
        iso = _isotopes()
        for m in iso.members():
            x = m["extra"]
            if m["name"] == "223Fr" and "Fr" in missing:
                out["Fr"] = (x["M_u"], "223Fr, the held AME2020 table (francium has no standard atomic weight)")
    for s in symbols:
        if s not in out:
            raise KeyError("no mass for %s" % s)
    return out


def levels(symbol):
    """[(configuration, term, energy)] from the captured listing, and the limit row's energy."""
    rows, limit = [], None
    with open(os.path.join(LEVELS_DIR, "%sI_levels.csv" % symbol), encoding="utf-8", newline="") as fh:
        for r in csv.reader(fh):
            if not r or r[0].startswith("#") or r[0] == "Configuration":
                continue
            if r[1] == "Limit":
                limit = r[4]
                continue
            rows.append((r[0], r[1], r[4]))
    return rows, limit


def members(rows, term, limit, n_min, n_max):
    """Distinct (n, E) of the series: single-valence configurations (no parenthesised parent, no
    '?'), the last subshell carrying the term's l, the term exactly, E below the limit."""
    l = SUBSHELL[LETTER[term.rstrip("*")[-1]]]
    out = set()
    for cfg, t, e in rows:
        if "(" in cfg or "?" in cfg or t != term or not e:
            continue
        m = re.search(r"(?:^|\.)(\d+)([spdfghik])$", cfg)
        if not m or m.group(2) != l:
            continue
        try:
            E = float(e.strip("[]()?+x "))
        except ValueError:
            continue
        n = int(m.group(1))
        if n_min <= n <= n_max and E < limit:
            out.add((n, E))
    return sorted(out)


def defects(mem, limit, R):
    return [n - math.sqrt(R / (limit - E)) for n, E in mem]


def recompute(rows=None):
    rows = float_rows() if rows is None else rows
    mass = masses(sorted({r["symbol"] for r in rows}))
    cache = {}
    out = []
    for r in rows:
        if r["symbol"] not in cache:
            cache[r["symbol"]] = levels(r["symbol"])
        lv, nist_limit = cache[r["symbol"]]
        lim = float(r["limit"])
        mem = members(lv, r["term"], lim, r["n_min"], r["n_max"])
        R_M = R_INF / (1.0 + M_E_U / mass[r["symbol"]][0])
        d = defects(mem, lim, R_M)
        d_inf = defects(mem, lim, R_INF)
        med, rng = statistics.median(d), max(d) - min(d)
        out.append(dict(r, **{
            "nist_limit": nist_limit, "mass_u": mass[r["symbol"]][0], "mass_source": mass[r["symbol"]][1],
            "got_members": len(mem), "got_n": [mem[0][0], mem[-1][0]] if mem else None,
            "median": med, "range": rng,
            "members_ok": len(mem) == r["members"] and bool(mem) and mem[0][0] == r["n_min"]
            and mem[-1][0] == r["n_max"],
            "delta_ok": "%.5f" % med == r["delta"], "B_is_range": "%.5f" % rng == r["B"],
            "delta_ok_with_R_inf": "%.5f" % statistics.median(d_inf) == r["delta"],
        }))
    return out


def summary(res):
    return {
        "rows": len(res),
        "members_reproduced": sum(r["members_ok"] for r in res),
        "delta_is_median": sum(r["delta_ok"] for r in res),
        "B_is_range": sum(r["B_is_range"] for r in res),
        "delta_with_R_inf": sum(r["delta_ok_with_R_inf"] for r in res),
        "limits_equal_nist_ie": sum(1 for s in {r["symbol"] for r in res}
                                    if float(NIST_IE_CM1[s][0]) == float(next(x["limit"] for x in res
                                                                                if x["symbol"] == s))),
        "spectra": len({r["symbol"] for r in res}),
        "unit": "cm^-1",
    }


def selftest():
    fails = []

    def check(name, got, want):
        ok = got == want
        print("  %-4s %s%s" % ("ok" if ok else "FAIL", name, "" if ok else "  (got %r, want %r)" % (got, want)))
        if not ok:
            fails.append(name)

    rows = float_rows()
    check("25 rows of COORDINATES-2.13 carry a non-integer B", len(rows), 25)
    check("all 25 are stage 1 (neutral) and graded measured",
          ({r["charge"] for r in rows}, {r["grade"] for r in rows}), ({1}, {"measured"}))
    check("nine spectra", sorted({r["symbol"] for r in rows}),
          sorted(["B", "Na", "Al", "Ga", "In", "Cs", "Lu", "Tl", "Fr"]))
    res = recompute(rows)
    s = summary(res)
    check("the nine printed limits equal NIST's ionisation energies in cm^-1", s["limits_equal_nist_ie"], 9)
    check("each captured listing's limit row is the printed limit",
          all(float(r["nist_limit"]) == float(r["limit"]) for r in res), True)
    check("member count and n range reproduce, 25 of 25", s["members_reproduced"], 25)
    check("delta is the median defect, 25 of 25", s["delta_is_median"], 25)
    check("B is the range of the defects, 25 of 25", s["B_is_range"], 25)
    check("with R_inf in place of R_M, no delta reproduces", s["delta_with_R_inf"], 0)
    # negative control: 11B's mass in place of the standard atomic weight loses boron's 2P* row
    b = [r for r in rows if r["symbol"] == "B" and r["term"] == "2P*"][0]
    lv, _ = levels("B")
    mem = members(lv, "2P*", float(b["limit"]), b["n_min"], b["n_max"])
    d11 = defects(mem, float(b["limit"]), R_INF / (1.0 + M_E_U / 11.0093054))
    check("negative control: with 11B's mass the boron 2P* row does not reproduce",
          ("%.5f" % statistics.median(d11), "%.5f" % (max(d11) - min(d11))) == (b["delta"], b["B"]), False)
    # Na I 2S, by hand: the median of 18 defects, the range 0.02475
    na = [r for r in res if r["symbol"] == "Na" and r["term"] == "2S"][0]
    check("Na I 2S: 18 members n = 3-20, median 1.34857, range 0.02475",
          (na["got_members"], na["got_n"], "%.5f" % na["median"], "%.5f" % na["range"]),
          (18, [3, 20], "1.34857", "0.02475"))
    print("SELFTEST %s" % ("OK" if not fails else "FAILED: %d" % len(fails)))
    return 0 if not fails else 1


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--json", action="store_true", help="the rows and the summary as JSON")
    ap.add_argument("--selftest", action="store_true", help="25 of 25 with R_M, no delta with R_inf")
    a = ap.parse_args()
    if a.selftest:
        return selftest()
    res = recompute()
    if a.json:
        print(json.dumps({"summary": summary(res), "rows": res}, indent=1))
        return 0
    print("COORDINATES-2.13's 25 non-integer B rows, recomputed from NIST's levels (R_M, standard atomic weight)")
    print()
    print("  %-3s %-4s %-7s %-12s %-9s %-9s %-9s %-9s  %s" % ("el", "term", "n", "members", "delta", "median",
                                                             "B", "range", "verdict"))
    for r in res:
        ok = r["members_ok"] and r["delta_ok"] and r["B_is_range"]
        print("  %-3s %-4s %-7s %-12s %-9s %-9.5f %-9s %-9.5f  %s" % (
            r["symbol"], r["term"], "%d-%d" % (r["n_min"], r["n_max"]),
            "%d of %d" % (r["got_members"], r["members"]), r["delta"], r["median"], r["B"], r["range"],
            "reproduced" if ok else "NOT reproduced"))
    s = summary(res)
    print()
    print("  delta is the median defect in %d of %d rows; B is the range in %d of %d; with R_inf %d deltas."
          % (s["delta_is_median"], s["rows"], s["B_is_range"], s["rows"], s["delta_with_R_inf"]))
    print("  The nine limits are NIST's neutral ionisation energies in cm^-1 (%d of %d)."
          % (s["limits_equal_nist_ie"], s["spectra"]))
    return 0


if __name__ == "__main__":
    sys.exit(main())
