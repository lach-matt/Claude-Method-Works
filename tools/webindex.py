#!/usr/bin/env python3
"""tools/webindex.py -- export the index for the interactive website.

Writes the static data the site under public/ reads:

    public/data/index.json          the drawn layout, the axes and their
                                    statuses, the closure figures, provenance,
                                    and a manifest of every element file
    public/data/elements/<Z>.json   one element on every axis of every index,
                                    exactly as tools/populate.py returns it

    python3 tools/webindex.py               # write public/data/
    python3 tools/webindex.py --selftest    # fixtures, nothing written
    python3 tools/webindex.py --verify      # public/data/ against the sources

NOTHING HERE IS COMPUTED TWICE. Every number the site shows is populate.py's,
which imports LW1-ground.py and tower-2.py by path and R from cypher.py, per
CLAUDE.md section 5. This file only serialises, and it carries populate.py's
own status vocabulary through untouched: READ, PINNED, DERIVED, RECOVERED and
RECONSTRUCTED. The site never prints a value without its status, because the
status travels with the axis in index.json.

ELEMENTS ABOVE Z = 108. LW1-ground.py stops at 108 because measurement does.
COORDINATES-2.13 carries rows to Z = 120, and those rows are exported READ from
the CSV with no configuration, no equation and no derived value behind them --
the file says so in its own "populated" field, and the site draws them apart.

A finding is recorded, never repaired. Where populate.py reports that the
CSV's B column disagrees with the observed configurations, or that a row's B
is a dispersion rather than a bound, that reaches the site as it is.

Stdlib only, Python 3.9+.
"""

from __future__ import annotations

import argparse
import csv
import datetime as _dt
import hashlib
import importlib.util
import json
import os
import subprocess
import sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TOOLS = os.path.join(REPO, "tools")
OUT = os.path.join(REPO, "public", "data")
MEMBER_INDEX = os.path.join(REPO, "method", "MEMBER-INDEX.tsv")
DRIVE_MANIFEST = os.path.join(REPO, "drive", "MANIFEST.tsv")

sys.path.insert(0, TOOLS)
import populate  # noqa: E402  -- the instrument; this file only serialises

SITE_TITLE = "The Method Index"
SITE_SUBTITLE = "The Method 1.6 · every element on every axis of every index"

# IUPAC names, for search and labels only. They are not a corpus figure and the
# site labels them as such; the corpus carries symbols (register 1306).
NAMES = {
    1: "Hydrogen", 2: "Helium", 3: "Lithium", 4: "Beryllium", 5: "Boron",
    6: "Carbon", 7: "Nitrogen", 8: "Oxygen", 9: "Fluorine", 10: "Neon",
    11: "Sodium", 12: "Magnesium", 13: "Aluminium", 14: "Silicon",
    15: "Phosphorus", 16: "Sulfur", 17: "Chlorine", 18: "Argon",
    19: "Potassium", 20: "Calcium", 21: "Scandium", 22: "Titanium",
    23: "Vanadium", 24: "Chromium", 25: "Manganese", 26: "Iron", 27: "Cobalt",
    28: "Nickel", 29: "Copper", 30: "Zinc", 31: "Gallium", 32: "Germanium",
    33: "Arsenic", 34: "Selenium", 35: "Bromine", 36: "Krypton",
    37: "Rubidium", 38: "Strontium", 39: "Yttrium", 40: "Zirconium",
    41: "Niobium", 42: "Molybdenum", 43: "Technetium", 44: "Ruthenium",
    45: "Rhodium", 46: "Palladium", 47: "Silver", 48: "Cadmium", 49: "Indium",
    50: "Tin", 51: "Antimony", 52: "Tellurium", 53: "Iodine", 54: "Xenon",
    55: "Caesium", 56: "Barium", 57: "Lanthanum", 58: "Cerium",
    59: "Praseodymium", 60: "Neodymium", 61: "Promethium", 62: "Samarium",
    63: "Europium", 64: "Gadolinium", 65: "Terbium", 66: "Dysprosium",
    67: "Holmium", 68: "Erbium", 69: "Thulium", 70: "Ytterbium",
    71: "Lutetium", 72: "Hafnium", 73: "Tantalum", 74: "Tungsten",
    75: "Rhenium", 76: "Osmium", 77: "Iridium", 78: "Platinum", 79: "Gold",
    80: "Mercury", 81: "Thallium", 82: "Lead", 83: "Bismuth", 84: "Polonium",
    85: "Astatine", 86: "Radon", 87: "Francium", 88: "Radium", 89: "Actinium",
    90: "Thorium", 91: "Protactinium", 92: "Uranium", 93: "Neptunium",
    94: "Plutonium", 95: "Americium", 96: "Curium", 97: "Berkelium",
    98: "Californium", 99: "Einsteinium", 100: "Fermium", 101: "Mendelevium",
    102: "Nobelium", 103: "Lawrencium", 104: "Rutherfordium", 105: "Dubnium",
    106: "Seaborgium", 107: "Bohrium", 108: "Hassium", 109: "Meitnerium",
    110: "Darmstadtium", 111: "Roentgenium", 112: "Copernicium",
    113: "Nihonium", 114: "Flerovium", 115: "Moscovium", 116: "Livermorium",
    117: "Tennessine", 118: "Oganesson", 119: "Ununennium", 120: "Unbinilium",
}

# Symbols for the twelve elements LW1-ground.py does not carry. IUPAC for
# 109-118, systematic for 119 and 120. Labels only; see NAMES.
SYMBOLS_ABOVE_108 = {
    109: "Mt", 110: "Ds", 111: "Rg", 112: "Cn", 113: "Nh", 114: "Fl",
    115: "Mc", 116: "Lv", 117: "Ts", 118: "Og", 119: "Uue", 120: "Ubn",
}

STATUS_LEGEND = {
    "READ": "a measurement, taken from a member or the mirror",
    "PINNED": "the corpus defines it at the precision a program needs",
    "DERIVED": "arithmetic on a READ or PINNED quantity, nothing added",
    "RECOVERED": "not stated in any member, but recovered by measurement from "
                 "the index's own computed column and consistent with what the "
                 "registers say about it qualitatively",
    "RECONSTRUCTED": "the corpus states the object and its behaviour but not "
                     "the form a program needs; reconstructed here, measured, "
                     "and kept as such so a later ruling can move it",
}

# The site's own caveats, drawn from docs/POPULATE.md's "Known gaps" and
# "Two findings". They are shown on every page, not buried in a footnote.
CAVEATS = [
    {"id": "above-108",
     "text": "Elements above Z = 108 are not populated. LW1-ground.py stops at "
             "108 because measurement does. COORDINATES-2.13 carries rows to "
             "Z = 120 and those are shown READ from the CSV with no "
             "configuration, equation or derived value behind them."},
    {"id": "b-aufbau",
     "text": "The spectra index's B column was built on a withdrawn "
             "configuration table (aufbau, patched by hand). Register 1306 "
             "corrected the configurations and COORDINATES-2.13 was never "
             "rebuilt on them. Where the observed table gives a different Pauli "
             "bound the site shows both and marks the disagreement."},
    {"id": "b-overloaded",
     "text": "25 measured rows carry a float in the B column: a dispersion of "
             "the median defect, not a bound. The site says 'B column is not a "
             "bound here' on those rows rather than comparing an integer "
             "against a spread."},
    {"id": "lambda8-mapping",
     "text": "A Λ₈ cell is a transition, so an element is not a cell. "
             "The mapping shown is the element's own ionisation ladder read off "
             "the observed configurations. Nothing in the store fixes this "
             "mapping; it is RECONSTRUCTED and a later ruling can move it."},
    {"id": "equation-domain",
     "text": "The channel equation is validated in its stated domain and "
             "extrapolated outside it. A residual on a channel outside that "
             "domain is not a finding against the equation."},
    {"id": "n0-reading",
     "text": "n₀'s reading is RECONSTRUCTED. Register 1141 names the terms "
             "of B = min(p, n₀ − ℓ − 1) but not whether a "
             "partially filled subshell counts; 'first entirely unoccupied n' "
             "matches the column at 97.7 % and He I settles it."},
]


# ---------------------------------------------------------------------------
# provenance
# ---------------------------------------------------------------------------

def _md5(path):
    h = hashlib.md5()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def _member_row(name):
    with open(MEMBER_INDEX, encoding="utf-8") as fh:
        for r in csv.DictReader(fh, delimiter="\t"):
            if r["member"] == name:
                return r
    return None


def _manifest_row(suffix):
    with open(DRIVE_MANIFEST, encoding="utf-8") as fh:
        for r in csv.DictReader(fh, delimiter="\t"):
            if r["repo_path"].endswith(suffix):
                return r
    return None


def _git_head():
    try:
        out = subprocess.run(["git", "rev-parse", "--short=12", "HEAD"],
                             cwd=REPO, capture_output=True, text=True,
                             check=True)
        return out.stdout.strip()
    except Exception:  # noqa: BLE001 -- provenance is best effort
        return None


def sources():
    """Every file a number on the site comes from, with the md5 the store
    records for it and the md5 measured now. A mismatch is reported, not
    repaired."""
    out = []
    for member in ("LW1-ground.py", "tower-2.py"):
        row = _member_row(member)
        path = os.path.join(populate.MEMBERS, member)
        out.append({
            "file": "method/members/" + member,
            "role": {"LW1-ground.py": "observed ground configurations, "
                                      "Z = 1 to 108 (register 1306, NIST ASD 5.12)",
                     "tower-2.py": "the tower above Λ₈"}[member],
            "md5_recorded": row["md5"] if row else None,
            "md5_measured": _md5(path) if os.path.exists(path) else None,
            "bundle": row["bundle"] if row else None,
        })
    row = _manifest_row("COORDINATES-2_13.csv")
    out.append({
        "file": "drive/The Method Materials/COORDINATES-2_13.csv",
        "role": "the spectra index: (Z, charge, ℓ, mult) → a channel",
        "md5_recorded": row["md5"] if row else None,
        "md5_measured": (_md5(populate.DEFAULT_SPECTRA)
                         if os.path.exists(populate.DEFAULT_SPECTRA) else None),
        "drive_modified": row["drive_modified"] if row else None,
    })
    for s in out:
        s["ok"] = (s["md5_recorded"] is not None
                   and s["md5_recorded"] == s["md5_measured"])
    return out


# ---------------------------------------------------------------------------
# the export
# ---------------------------------------------------------------------------

def _compact(obj):
    return json.dumps(obj, ensure_ascii=False, separators=(",", ":"),
                      allow_nan=False)


def _csv_only_element(Z, spectra):
    """Z = 109 to 120: rows READ from COORDINATES-2.13 and nothing else."""
    chans = {}
    for r in spectra.channels(Z):
        c, l, m = int(r["charge"]), int(r["l"]), int(r["mult"])
        ch = chans.setdefault((c, l), {
            "charge": c, "Ne": Z - c + 1, "l": l,
            "subshell_letter": populate.LSYM[l] if l < len(populate.LSYM) else str(l),
            "core_Ne": Z - c, "core_symbol": None, "p": None, "n0": None,
            "B_computed": None, "C_of_Z": None, "delta_equation": None,
            "measured": [],
        })
        cb = populate.csv_bound(r)
        ch["measured"].append({
            "mult": m, "delta": float(r["delta"]), "grade": r["grade"],
            "witness": r["witness"], "source": r["source"],
            "bound_note": r["bound"], "B_csv": cb, "B_agrees": None,
            "B_csv_is_not_a_bound": cb is None and r.get("B", "") != "",
            "floor_le_B": None, "residual": None,
        })
    return {
        "Z": Z, "symbol": SYMBOLS_ABOVE_108[Z], "shells_as_printed": None,
        "level": None, "electron_count": None, "electron_count_ok": None,
        "configuration": None,
        "period": populate.period_of(Z),
        "group": (populate.group_of(Z) if Z <= 118 else Z - 118),
        "block": None, "block_letter": None, "set_aside": False,
        "janet_cell": None, "outer": None, "closure": None,
        "config_table": None,
        "channels": [chans[k] for k in sorted(chans)],
        "lambda8": [],
        "populated": False,
        "note": "COORDINATES-2.13 rows only; LW1-ground.py stops at Z = 108",
    }


def element_record(Z, spectra):
    if Z in populate.LW1.GROUND:
        rec = populate.populate(Z, spectra)
        rec["populated"] = True
        return rec
    return _csv_only_element(Z, spectra)


def _counts(rec):
    meas = [m for ch in rec["channels"] for m in ch["measured"]]
    return {
        "ions": len({ch["charge"] for ch in rec["channels"]}),
        "channels": len(rec["channels"]),
        "rows": len(meas),
        "measured": sum(1 for m in meas if m["grade"] == "measured"),
        "exact": sum(1 for m in meas if m["grade"] == "exact"),
        "computed": sum(1 for m in meas if m["grade"] == "computed"),
        "witnessed": sum(1 for m in meas if m["witness"] == "witnessed"),
        "lambda8_steps": len(rec["lambda8"]),
    }


def build(spectra, out_dir=OUT, write=True, log=print):
    held, admitted = populate.layout_closure()
    denied = sorted(admitted - held)
    layout = []
    manifest = []
    totals = {"rows": 0, "measured": 0, "exact": 0, "computed": 0,
              "witnessed": 0, "populated": 0, "csv_only": 0}
    zs = sorted(set(populate.LW1.GROUND) | set(spectra.by_z))
    if write:
        os.makedirs(os.path.join(out_dir, "elements"), exist_ok=True)
    for Z in zs:
        rec = element_record(Z, spectra)
        counts = _counts(rec)
        for k in ("rows", "measured", "exact", "computed", "witnessed"):
            totals[k] += counts[k]
        totals["populated" if rec["populated"] else "csv_only"] += 1
        body = _compact(rec).encode("utf-8")
        rel = "elements/%d.json" % Z
        if write:
            with open(os.path.join(out_dir, rel), "wb") as fh:
                fh.write(body)
        manifest.append({"Z": Z, "file": rel, "bytes": len(body),
                         "md5": hashlib.md5(body).hexdigest()})
        layout.append({
            "Z": Z, "symbol": rec["symbol"], "name": NAMES.get(Z),
            "period": rec["period"], "group": rec["group"],
            "block": rec["block_letter"], "set_aside": rec["set_aside"],
            "janet": rec["janet_cell"],
            "shells": rec["shells_as_printed"], "level": rec["level"],
            "held": (rec["closure"]["cell_held"] if rec["closure"] else None),
            "populated": rec["populated"],
            "counts": counts,
        })
        log("  Z=%3d %-3s %7d B  rows %5d  measured %3d" % (
            Z, rec["symbol"], len(body), counts["rows"], counts["measured"]))

    axes = [{"axis": a, "status": s, "source": d} for a, s, d in populate.AXES]
    index = {
        "meta": {
            "title": SITE_TITLE,
            "subtitle": SITE_SUBTITLE,
            "built": _dt.datetime.now(_dt.timezone.utc).isoformat(timespec="seconds"),
            "commit": _git_head(),
            "generator": "tools/webindex.py over tools/populate.py",
            "names_note": "Element names are IUPAC labels for search only; "
                          "they are not a corpus figure. The corpus carries "
                          "symbols (register 1306).",
        },
        "sources": sources(),
        "status_legend": STATUS_LEGEND,
        "axes": axes,
        "caps": populate.CAPS,
        "lambda_coords": populate.LAMBDA_COORDS,
        "lambda_meaning": populate.LAMBDA_MEANING,
        "closure": {
            "index": "periodic table (period × group), section 6",
            "operator": "ℛ, the PINNED order operator of section 32.4.1 "
                        "(tools/cypher.py)",
            "held": len(held), "admitted": len(admitted),
            "E": len(admitted) - len(held),
            "denied": [list(c) for c in denied],
            "set_aside": 28,
        },
        "collapse": {"Z0": populate.COLLAPSE_Z, "width": populate.COLLAPSE_WIDTH,
                     "status": populate.RECOVERED,
                     "form": "C(Z, ℓ) = clamp(0.5 + (Z − Z₀(ℓ)) / 8, 0, 1)"},
        "equation": {"A": populate.A_COEFF, "K": populate.K_COEFF,
                     "H": populate.H_COEFF, "status": populate.PINNED,
                     "source": "register 1205, final form"},
        "caveats": CAVEATS,
        "totals": totals,
        "layout": layout,
        "manifest": manifest,
    }
    if write:
        with open(os.path.join(out_dir, "index.json"), "w", encoding="utf-8") as fh:
            fh.write(json.dumps(index, ensure_ascii=False, indent=1,
                                allow_nan=False))
    return index


# ---------------------------------------------------------------------------
# selftest and verify
# ---------------------------------------------------------------------------

def selftest():
    spectra = populate.Spectra(populate.DEFAULT_SPECTRA)
    fails = []
    ran = []

    def check(name, got, want):
        ok = got == want
        ran.append(name)
        print("  %-52s %-14s expected %-14s %s" % (name, got, want, "ok" if ok else "FAIL"))
        if not ok:
            fails.append(name)

    print("webindex selftest")
    index = build(spectra, write=False, log=lambda *_a, **_k: None)
    t = index["totals"]
    check("elements populated (LW1-ground.py)", t["populated"], 108)
    check("elements CSV-only (Z = 109 to 120)", t["csv_only"], 12)
    check("rows exported = COORDINATES-2.13 rows", t["rows"], len(spectra.rows))
    check("measured rows", t["measured"],
          sum(1 for r in spectra.rows if r["grade"] == "measured"))
    check("exact rows", t["exact"],
          sum(1 for r in spectra.rows if r["grade"] == "exact"))
    check("witnessed rows", t["witnessed"],
          sum(1 for r in spectra.rows if r["witness"] == "witnessed"))
    c = index["closure"]
    check("closure held (section 6)", c["held"], 90)
    check("closure admitted", c["admitted"], 126)
    check("closure E", c["E"], 36)
    check("denied cells listed", len(c["denied"]), 36)
    check("axes carry a status", all(a["status"] in STATUS_LEGEND
                                    for a in index["axes"]), True)
    check("every source md5 matches its record",
          all(s["ok"] for s in index["sources"]), True)
    k = element_record(19, spectra)
    check("K: closure cell held", k["closure"]["cell_held"], True)
    check("K: Janet cell", list(k["janet_cell"]), [4, 0])
    h = element_record(1, spectra)
    check("H I s: equation returns exactly 0 (register 5193)",
          [ch["delta_equation"] for ch in h["channels"] if ch["l"] == 0][0], 0.0)
    og = element_record(118, spectra)
    check("Og: CSV-only, not populated", og["populated"], False)
    check("Og: period 7 group 18", (og["period"], og["group"]), (7, 18))
    check("layout rows", len(index["layout"]), 120)
    check("manifest rows", len(index["manifest"]), 120)
    print()
    print("fixtures checked: %d  failed: %d" % (len(ran), len(fails)))
    print()
    print("SELFTEST OK" if not fails else "SELFTEST FAILED: " + ", ".join(fails))
    return 0 if not fails else 1


def verify(out_dir=OUT):
    """public/data/ against the sources: every element file's md5 against the
    manifest, and the manifest's count against the layout."""
    path = os.path.join(out_dir, "index.json")
    if not os.path.exists(path):
        print("no %s -- run without --verify first" % path)
        return 1
    with open(path, encoding="utf-8") as fh:
        index = json.load(fh)
    bad = 0
    for m in index["manifest"]:
        p = os.path.join(out_dir, m["file"])
        got = _md5(p) if os.path.exists(p) else None
        if got != m["md5"]:
            bad += 1
            print("  MISMATCH %s  manifest %s  on disk %s" % (m["file"], m["md5"], got))
    print("element files: %d  mismatched: %d" % (len(index["manifest"]), bad))
    for s in index["sources"]:
        print("  %-52s %s" % (s["file"], "ok" if s["ok"] else "MD5 DRIFT"))
    print("VERIFY OK" if bad == 0 else "VERIFY FAILED")
    return 0 if bad == 0 else 1


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--out", default=OUT)
    ap.add_argument("--selftest", action="store_true")
    ap.add_argument("--verify", action="store_true")
    args = ap.parse_args(argv)
    if args.selftest:
        return selftest()
    if args.verify:
        return verify(args.out)
    spectra = populate.Spectra(populate.DEFAULT_SPECTRA)
    index = build(spectra, out_dir=args.out)
    t = index["totals"]
    print("wrote %s: %d elements (%d populated, %d CSV-only), %d rows, "
          "%d measured" % (args.out, len(index["layout"]), t["populated"],
                           t["csv_only"], t["rows"], t["measured"]))
    return 0


if __name__ == "__main__":
    sys.exit(main())
