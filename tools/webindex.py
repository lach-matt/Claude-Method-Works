#!/usr/bin/env python3
"""tools/webindex.py -- export the index for the interactive website.

Writes the static data the site under public/ reads:

    public/data/index.js            the drawn layout, the axes and their
                                    statuses, the closure figures, provenance,
                                    the equation with its coefficients, the
                                    instruments' own source, the fixtures the
                                    browser-side solvers must reproduce, and a
                                    manifest of every element file
    public/data/elements/<Z>.js     one element on every axis of every index,
                                    exactly as tools/populate.py returns it

THE DATA PROTOCOL. Each file is a JSON payload inside a one-line script
wrapper, because the page must open from a plain file:// URL on a phone,
where fetch() of a local file is blocked but a <script src> is not:

    window.__mi = window.__mi || {}; window.__mi.index = {...};
    window.__mi = window.__mi || {}; (window.__mi.el = window.__mi.el || {})[<Z>] = {...};

The payload inside the wrapper is the same object json.dumps would have
written to a .json file -- compact for an element, indented for the index --
so the manifest carries both the .js file's md5 and the payload's.

    python3 tools/webindex.py               # write public/data/
    python3 tools/webindex.py --selftest    # fixtures, nothing written
    python3 tools/webindex.py --verify      # public/data/ against the sources

NOTHING HERE IS COMPUTED TWICE. Every number the site shows is populate.py's,
which imports LW1-ground.py and tower-2.py by path and R from cypher.py, per
CLAUDE.md section 5. This file only serialises, and it carries populate.py's
own status vocabulary through untouched: READ, PINNED, DERIVED, RECOVERED and
RECONSTRUCTED. The site never prints a value without its status, because the
status travels with the axis in index.js.

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
import ast
import contextlib
import csv
import datetime as _dt
import hashlib
import inspect
import io
import json
import math
import os
import re
import subprocess
import sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TOOLS = os.path.join(REPO, "tools")
OUT = os.path.join(REPO, "public", "data")
MEMBER_INDEX = os.path.join(REPO, "method", "MEMBER-INDEX.tsv")
DRIVE_MANIFEST = os.path.join(REPO, "drive", "MANIFEST.tsv")

sys.path.insert(0, TOOLS)
import populate  # noqa: E402  -- the instrument; this file only serialises
import cypher    # noqa: E402  -- R, imported by populate; read here for its source

# The script wrappers of the data protocol. The page reads window.__mi.index
# and window.__mi.el[Z]; nothing else is global.
INDEX_PREFIX = "window.__mi = window.__mi || {}; window.__mi.index = "
ELEMENT_PREFIX = ("window.__mi = window.__mi || {}; "
                  "(window.__mi.el = window.__mi.el || {})[%d] = ")
WRAP_SUFFIX = ";\n"

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
# the instruments, verbatim, and their status
# ---------------------------------------------------------------------------

# Each entry: (name, function, file, status, where it comes from). The status
# is the one docs/POPULATE.md and docs/CYPHER.md give the quantity the function
# returns; the source sentence names the register or section. The browser-side
# solvers show this source beside their result and re-derive nothing from it.
INSTRUMENTS = [
    ("channel_delta", populate.channel_delta, "tools/populate.py", populate.PINNED,
     "the channel equation, final form (register 1205); its p = 0 branch "
     "carries the RECOVERED collapse ramp C(Z)"),
    ("collapse_C", populate.collapse_C, "tools/populate.py", populate.RECOVERED,
     "C(Z, l), the collapse coordinate, inverted out of COORDINATES-2.13's "
     "computed column (registers 1188 to 1190); no member states its form"),
    ("pauli_bound", populate.pauli_bound, "tools/populate.py", populate.PINNED,
     "B = min(p, n0 - l - 1), the Pauli bound (register 1141)"),
    ("core_p", populate.core_p, "tools/populate.py", populate.PINNED,
     "p, the core's orbital count at this l, from the observed ground "
     "configuration of the core (registers 1141, 1306)"),
    ("n0_of", populate.n0_of, "tools/populate.py", populate.RECON,
     "n0, the first entirely unoccupied n at this l; register 1141 names the "
     "term but not the reading, and He I ns settles it"),
    ("lambda_constraints", populate.lambda_constraints, "tools/populate.py",
     populate.PINNED, "section 7.1's seven constraints, four origins"),
    ("caps_needed", populate.caps_needed, "tools/populate.py", populate.PINNED,
     "the caps a Lambda_8 cell needs, read against section 7.4's "
     "(n, e, l, k, f) = (3, 3, 1, 3, 1); the cell it is applied to is the "
     "RECONSTRUCTED ionisation-ladder mapping and carries its own status"),
    ("within_caps", populate.within_caps, "tools/populate.py", populate.PINNED,
     "section 7.4's standing caps; a cell outside them is reported OUTSIDE, "
     "never truncated"),
    ("op_order", cypher.op_order, "tools/cypher.py", cypher.PINNED,
     "R, the order operator of section 32.4.1; matches the seated instrument "
     "rclose.py"),
]


def instruments():
    """Verbatim source of every instrument the browser-side solvers mirror,
    via inspect.getsource, so the page can show the Python beside its own
    result and a reader can diff the two."""
    out = {}
    for name, fn, rel, status, source in INSTRUMENTS:
        lines, start = inspect.getsourcelines(fn)
        out[name] = {"python": "".join(lines), "file": rel, "line": start,
                     "status": status, "source": source}
    return out


def _equation_form():
    """The two branches as text, exactly as populate.channel_delta's docstring
    states them -- read out of the docstring, not typed here."""
    doc = inspect.getdoc(populate.channel_delta) or ""
    return [ln.strip() for ln in doc.splitlines() if ln.strip().startswith("delta =")]


# ---------------------------------------------------------------------------
# fixtures -- what the browser-side solvers must reproduce
# ---------------------------------------------------------------------------

def equation_figures(spectra, grades=("measured",), table="observed"):
    """What populate.equation_report computes, returned rather than printed:
    the same rows, the same skips, the same rms, R2 and median |error| and the
    same per-l breakdown. The selftest holds this against the instrument's own
    printed line, so the two cannot drift apart silently."""
    rows = [r for r in spectra.rows if r["grade"] in grades]
    res, skipped = [], 0
    for r in rows:
        Z, c, l = int(r["Z"]), int(r["charge"]), int(r["l"])
        if (Z - c) >= 1 and (Z - c) not in populate.LW1.GROUND:
            skipped += 1
            continue
        eq = populate.channel_delta(Z, c, l, table)
        if eq is None:
            skipped += 1
            continue
        res.append((float(r["delta"]) - eq, float(r["delta"]), l))
    if not res:
        return None
    n = len(res)
    rms = math.sqrt(sum(d * d for d, _v, _l in res) / n)
    mean = sum(v for _d, v, _l in res) / n
    ss_tot = sum((v - mean) ** 2 for _d, v, _l in res)
    ss_res = sum(d * d for d, _v, _l in res)
    r2 = 1 - ss_res / ss_tot if ss_tot else None
    med = sorted(abs(d) for d, _v, _l in res)[n // 2]
    by_l = []
    for l in sorted({x[2] for x in res}):
        sub = [d for d, _v, ll in res if ll == l]
        by_l.append({"l": l, "n": len(sub),
                     "rms": math.sqrt(sum(d * d for d in sub) / len(sub))})
    return {"grades": list(grades), "table": table, "channels": n,
            "skipped": skipped, "rms": rms, "R2": r2,
            "median_abs_error": med, "by_l": by_l,
            "status": populate.PINNED,
            "note": "populate.equation_report over COORDINATES-2.13's measured "
                    "rows; register 1205 records rms 0.1610, R2 0.9741 on a "
                    "different sample of 284 channels, so the figures are not "
                    "expected to match it exactly"}


def _decoded_closure(name, coords, cells):
    """R over a set of cells, decoded back from cypher.Index's ordinal codes
    the way populate.layout_closure decodes the periodic layout."""
    ix = cypher.Index(name, coords, cells)
    admitted, _note = cypher.op_order(ix, {})

    def decode(c):
        return tuple(ix.decode[i][v] for i, v in enumerate(c))

    return {decode(c) for c in ix.cells}, {decode(c) for c in admitted}, ix.box


def janet_closure():
    """R over the distinct Janet cells of the elements that have one, built
    the way populate.layout_closure builds the periodic one."""
    cells = sorted({tuple(populate.janet_cell(Z)) for Z in populate.LW1.GROUND
                    if populate.janet_cell(Z) is not None})
    return _decoded_closure("Janet (n+l x l), the elements' cells",
                            ["n+l", "l"], cells)


def janet_closure_cypher_fixture():
    """cypher.py's own Janet fixture -- n = 1 to 7, l < min(n, 4) -- which its
    selftest records as cells=22 box=40 E(order)=0. It is not the elements'
    set of cells (that is 19 cells over a box of 32), and the two are kept
    apart rather than one quoted as the other."""
    ix = cypher._janet()
    return _decoded_closure(ix.name, ix.coords,
                            [tuple(ix.decode[i][v] for i, v in enumerate(c))
                             for c in ix.cells])


def fixtures(spectra):
    """Numbers the browser-side solver selftests must reproduce, every one
    computed here with populate.py's own functions and none typed in."""
    held, admitted = populate.layout_closure()
    jh, ja, jbox = janet_closure()
    ch, ca, cbox = janet_closure_cypher_fixture()
    collapse = []
    for l, z0 in sorted(populate.COLLAPSE_Z.items()):
        collapse.append({"l": l, "Z0": z0,
                         "rows": [{"Z": Z, "C": populate.collapse_C(Z, l)}
                                  for Z in range(z0 - 4, z0 + 5)]})
    measured = sorted((r for r in spectra.rows if r["grade"] == "measured"),
                      key=lambda r: (int(r["Z"]), int(r["charge"]),
                                     int(r["l"]), int(r["mult"])))
    sample = []
    for r in measured[:12]:
        Z, c, l = int(r["Z"]), int(r["charge"]), int(r["l"])
        Ne = Z - c + 1
        core = Ne - 1
        sample.append({
            "Z": Z, "charge": c, "l": l, "mult": int(r["mult"]),
            "delta": float(r["delta"]),
            "p": populate.core_p(core, l) if core >= 1 else 0,
            "Ne": Ne, "C": populate.collapse_C(Z, l),
            "delta_equation": populate.channel_delta(Z, c, l),
        })
    return {
        "note": "computed at build with tools/populate.py's own functions, "
                "never typed in; a browser-side solver that cannot reproduce "
                "these must say so rather than print a result",
        "equation_report": equation_figures(spectra),
        "closure": {
            "operator": "cypher.op_order, R (section 32.4.1)",
            "status": populate.PINNED,
            "periodic": {"held": len(held), "admitted": len(admitted),
                         "E": len(admitted) - len(held),
                         "index": "periodic table (period x group), section 6, "
                                  "the ninety main-table cells"},
            "janet": {"held": len(jh), "admitted": len(ja),
                      "E": len(ja) - len(jh), "box": jbox,
                      "cells": [list(c) for c in sorted(jh)],
                      "index": "Janet (n+l x l): the distinct cells of the 108 "
                               "elements LW1-ground.py carries"},
            "janet_cypher_fixture": {
                "held": len(ch), "admitted": len(ca), "E": len(ca) - len(ch),
                "box": cbox,
                "index": "cypher.py's own Janet fixture, n = 1 to 7 and "
                         "l < min(n, 4); its selftest records cells=22 box=40 "
                         "E(order)=0. Not the elements' cells."},
        },
        "collapse_table": {"status": populate.RECOVERED,
                           "form": "C(Z, l) = clamp(0.5 + (Z - Z0(l)) / 8, 0, 1)",
                           "by_l": collapse},
        "hydrogenic_zero": {"Z": 1, "charge": 1, "l": 0,
                            "delta_equation": populate.channel_delta(1, 1, 0),
                            "status": populate.PINNED,
                            "source": "register 5193: at Ne = 1 the (Ne-1)/Ne "
                                      "factor vanishes identically"},
        "pauli": {"status": populate.PINNED,
                  "source": "register 1141; populate.selftest's own pair",
                  "rows": [{"label": "He I ns", "Z": 2, "charge": 1, "l": 0,
                            "B": populate.pauli_bound(2, 1, 0)},
                           {"label": "Be I ns", "Z": 4, "charge": 1, "l": 0,
                            "B": populate.pauli_bound(4, 1, 0)}]},
        "coefficient_roundtrip_sample": {
            "statuses": {"delta": populate.READ, "p": populate.PINNED,
                         "Ne": populate.DERIVED, "C": populate.RECOVERED,
                         "delta_equation": populate.PINNED},
            "note": "the first 12 measured rows of COORDINATES-2.13 in "
                    "(Z, charge, l, mult) order",
            "rows": sample},
    }


# ---------------------------------------------------------------------------
# the export
# ---------------------------------------------------------------------------

def _compact(obj):
    return json.dumps(obj, ensure_ascii=False, separators=(",", ":"),
                      allow_nan=False)


def wrap_element(Z, body):
    """The element file: the protocol wrapper around the compact payload."""
    return (ELEMENT_PREFIX % Z).encode("utf-8") + body + WRAP_SUFFIX.encode("utf-8")


def wrap_index(text):
    return INDEX_PREFIX + text + WRAP_SUFFIX


def unwrap(text, Z=None):
    """The JSON payload out of a protocol file, or None if the wrapper is not
    the one this file writes."""
    prefix = INDEX_PREFIX if Z is None else ELEMENT_PREFIX % Z
    if not (text.startswith(prefix) and text.endswith(WRAP_SUFFIX)):
        return None
    return text[len(prefix):-len(WRAP_SUFFIX)]


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
        _remove_json_outputs(out_dir, log)
    for Z in zs:
        rec = element_record(Z, spectra)
        counts = _counts(rec)
        for k in ("rows", "measured", "exact", "computed", "witnessed"):
            totals[k] += counts[k]
        totals["populated" if rec["populated"] else "csv_only"] += 1
        body = _compact(rec).encode("utf-8")
        blob = wrap_element(Z, body)
        rel = "elements/%d.js" % Z
        if write:
            with open(os.path.join(out_dir, rel), "wb") as fh:
                fh.write(blob)
        manifest.append({"Z": Z, "file": rel, "bytes": len(blob),
                         "md5": hashlib.md5(blob).hexdigest(),
                         "payload_bytes": len(body),
                         "payload_md5": hashlib.md5(body).hexdigest()})
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
            Z, rec["symbol"], len(blob), counts["rows"], counts["measured"]))

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
                     "H": populate.H_COEFF,
                     "E0": populate.E0, "E1": populate.E1,
                     "form": _equation_form(),
                     "exponent": "e(Ne) = E0 - E1 ln Ne",
                     "status": populate.PINNED,
                     "source": "register 1205, final form"},
        "instruments": instruments(),
        "fixtures": fixtures(spectra),
        "caveats": CAVEATS,
        "totals": totals,
        "layout": layout,
        "manifest": manifest,
        "protocol": {
            "index": "data/index.js sets window.__mi.index",
            "element": "data/elements/<Z>.js sets window.__mi.el[Z]",
            "why": "the page opens from a file:// URL on a phone, where fetch() "
                   "of a local file is blocked and a <script src> is not",
            "encoding": "utf-8",
        },
    }
    if write:
        text = json.dumps(index, ensure_ascii=False, indent=1, allow_nan=False)
        with open(os.path.join(out_dir, "index.js"), "w", encoding="utf-8") as fh:
            fh.write(wrap_index(text))
    return index


def _remove_json_outputs(out_dir, log=print):
    """The earlier format wrote index.json and elements/<Z>.json. They are
    generated files and the page no longer reads them, so a build clears
    them rather than leaving two copies of the index side by side."""
    gone = 0
    old = [os.path.join(out_dir, "index.json")]
    eldir = os.path.join(out_dir, "elements")
    if os.path.isdir(eldir):
        old += [os.path.join(eldir, f) for f in os.listdir(eldir)
                if f.endswith(".json")]
    for p in old:
        if os.path.exists(p):
            os.remove(p)
            gone += 1
    if gone:
        log("  removed %d .json file(s) of the earlier format" % gone)


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
        print("  %-58s %-14s expected %-14s %s" % (name, got, want, "ok" if ok else "FAIL"))
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
    # one status per quantity: the axis table's C(Z) is the instrument's own
    # (RECOVERED), so the ion, channel and cell plates cannot badge it apart
    # from the solver, the provenance dialog and docs/POPULATE.md
    check("axes: C(Z) carries collapse_C's status (RECOVERED)",
          [a["status"] for a in index["axes"] if a["axis"] == "C(Z)"],
          [populate.RECOVERED])
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

    # --- the data protocol ---------------------------------------------------
    check("manifest names .js files only",
          all(m["file"].endswith(".js") for m in index["manifest"]), True)
    body = _compact(h).encode("utf-8")
    blob = wrap_element(1, body)
    check("element wrapper opens with the protocol prefix",
          blob.decode("utf-8").startswith(
              "window.__mi = window.__mi || {}; "
              "(window.__mi.el = window.__mi.el || {})[1] = {"), True)
    check("element wrapper unwraps to its payload",
          unwrap(blob.decode("utf-8"), 1) == body.decode("utf-8"), True)
    check("element payload md5 is the manifest's payload_md5",
          index["manifest"][0]["payload_md5"], hashlib.md5(body).hexdigest())
    check("element file md5 is the manifest's md5",
          index["manifest"][0]["md5"], hashlib.md5(blob).hexdigest())
    itext = json.dumps(index, ensure_ascii=False, indent=1, allow_nan=False)
    check("index wrapper unwraps to its payload",
          unwrap(wrap_index(itext)) == itext, True)

    # --- the equation block --------------------------------------------------
    eq = index["equation"]
    check("equation E0 is populate.E0", eq["E0"], populate.E0)
    check("equation E1 is populate.E1", eq["E1"], populate.E1)
    check("equation E0, E1 as docs/POPULATE.md prints them",
          (eq["E0"], eq["E1"]), (0.8297, 0.09))
    check("equation form: two branches out of the docstring", len(eq["form"]), 2)
    check("equation form: p > 0 then p = 0",
          ("where p > 0" in eq["form"][0], "where p = 0" in eq["form"][1]),
          (True, True))
    check("equation exponent", eq["exponent"], "e(Ne) = E0 - E1 ln Ne")

    # --- the instruments -----------------------------------------------------
    ins = index["instruments"]
    check("instruments: the nine, in order", list(ins),
          [n for n, *_ in INSTRUMENTS])
    parses = True
    for name, rec in ins.items():
        try:
            ast.parse(rec["python"])
        except SyntaxError:
            parses = False
    check("instruments: every source parses", parses, True)
    check("instruments: every status is in the legend",
          all(r["status"] in STATUS_LEGEND for r in ins.values()), True)
    check("instruments: op_order is cypher.py's",
          ins["op_order"]["file"], "tools/cypher.py")
    check("instruments: collapse_C is RECOVERED",
          ins["collapse_C"]["status"], populate.RECOVERED)
    check("instruments: n0_of is RECONSTRUCTED",
          ins["n0_of"]["status"], populate.RECON)

    # --- the fixtures ----------------------------------------------------------
    fx = index["fixtures"]
    er = fx["equation_report"]
    check("equation report: channels compared", er["channels"], 358)
    check("equation report: skipped", er["skipped"], 0)
    check("equation report: rms", round(er["rms"], 4), 0.1809)
    check("equation report: R2", round(er["R2"], 4), 0.9656)
    check("equation report: median |error|", round(er["median_abs_error"], 4), 0.0587)
    l4 = [b for b in er["by_l"] if b["l"] == 4]
    check("equation report: l = 4 n = 36 rms 0.0139",
          (l4[0]["n"], round(l4[0]["rms"], 4)) if l4 else None, (36, 0.0139))
    # the same figures as populate.equation_report prints them, so the
    # replicate and the instrument cannot drift apart silently
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        populate.equation_report(spectra)
    m = re.search(r"channels compared: (\d+).*?rms ([\d.]+)\s+R2 ([\d.]+)\s+"
                  r"median \|error\| ([\d.]+)", buf.getvalue(), re.S)
    printed = (int(m.group(1)), m.group(2), m.group(3), m.group(4)) if m else None
    check("equation report: populate.equation_report prints the same",
          printed, (er["channels"], "%.4f" % er["rms"], "%.4f" % er["R2"],
                    "%.4f" % er["median_abs_error"]))

    cl = fx["closure"]
    check("closure fixture: periodic 90 / 126 / E 36",
          (cl["periodic"]["held"], cl["periodic"]["admitted"], cl["periodic"]["E"]),
          (90, 126, 36))
    check("closure fixture: periodic equals the index's closure block",
          (cl["periodic"]["held"], cl["periodic"]["admitted"], cl["periodic"]["E"]),
          (c["held"], c["admitted"], c["E"]))
    check("closure fixture: Janet, the elements' cells, E = 0",
          cl["janet"]["E"], 0)
    check("closure fixture: Janet, the elements' cells, 19 held over box 32",
          (cl["janet"]["held"], cl["janet"]["admitted"], cl["janet"]["box"]),
          (19, 19, 32))
    check("closure fixture: Janet, cypher.py's own fixture, 22 / 40 / E 0",
          (cl["janet_cypher_fixture"]["held"], cl["janet_cypher_fixture"]["box"],
           cl["janet_cypher_fixture"]["E"]), (22, 40, 0))

    ct = fx["collapse_table"]["by_l"]
    check("collapse table: three l, nine Z each",
          [(b["l"], len(b["rows"])) for b in ct], [(1, 9), (2, 9), (3, 9)])
    check("collapse table: C = 0.5 at each Janet boundary",
          [b["rows"][4]["C"] for b in ct], [0.5, 0.5, 0.5])
    check("collapse table: 0 four below, 1 four above",
          [(b["rows"][0]["C"], b["rows"][8]["C"]) for b in ct],
          [(0.0, 1.0)] * 3)
    check("hydrogenic zero: channel_delta(1, 1, 0) == 0.0",
          fx["hydrogenic_zero"]["delta_equation"], 0.0)
    check("pauli: He I ns B = 1, Be I ns B = 2",
          [r["B"] for r in fx["pauli"]["rows"]], [1, 2])
    sm = fx["coefficient_roundtrip_sample"]["rows"]
    check("coefficient sample: 12 rows", len(sm), 12)
    check("coefficient sample: starts at He I ns, mult 1 (H has no measured row)",
          (sm[0]["Z"], sm[0]["charge"], sm[0]["l"], sm[0]["mult"]), (2, 1, 0, 1))
    check("coefficient sample: in (Z, charge, l, mult) order",
          [(r["Z"], r["charge"], r["l"], r["mult"]) for r in sm]
          == sorted((r["Z"], r["charge"], r["l"], r["mult"]) for r in sm), True)
    check("coefficient sample: delta_equation is channel_delta's",
          all(r["delta_equation"] == populate.channel_delta(r["Z"], r["charge"], r["l"])
              for r in sm), True)
    check("coefficient sample: every row grade measured",
          all(any(int(x["Z"]) == r["Z"] and int(x["charge"]) == r["charge"]
                  and int(x["l"]) == r["l"] and int(x["mult"]) == r["mult"]
                  and x["grade"] == "measured" for x in spectra.by_z[r["Z"]])
              for r in sm), True)

    print()
    print("fixtures checked: %d  failed: %d" % (len(ran), len(fails)))
    print()
    print("SELFTEST OK" if not fails else "SELFTEST FAILED: " + ", ".join(fails))
    return 0 if not fails else 1


def read_index(out_dir=OUT):
    """The index payload back out of data/index.js, or None."""
    path = os.path.join(out_dir, "index.js")
    if not os.path.exists(path):
        return None
    with open(path, encoding="utf-8") as fh:
        text = unwrap(fh.read())
    return None if text is None else json.loads(text)


def verify(out_dir=OUT):
    """public/data/ against the sources: every element .js file's md5 against
    the manifest, the payload inside each wrapper against its own md5, and the
    manifest's count against the layout."""
    index = read_index(out_dir)
    if index is None:
        print("no readable %s -- run without --verify first"
              % os.path.join(out_dir, "index.js"))
        return 1
    bad = 0
    for m in index["manifest"]:
        p = os.path.join(out_dir, m["file"])
        got = _md5(p) if os.path.exists(p) else None
        if got != m["md5"]:
            bad += 1
            print("  MISMATCH %s  manifest %s  on disk %s" % (m["file"], m["md5"], got))
            continue
        with open(p, encoding="utf-8") as fh:
            payload = unwrap(fh.read(), m["Z"])
        pm = (hashlib.md5(payload.encode("utf-8")).hexdigest()
              if payload is not None else None)
        if pm != m["payload_md5"]:
            bad += 1
            print("  BAD WRAPPER %s  payload md5 %s  manifest %s"
                  % (m["file"], pm, m["payload_md5"]))
    stray = [f for f in os.listdir(os.path.join(out_dir, "elements"))
             if not f.endswith(".js")]
    if os.path.exists(os.path.join(out_dir, "index.json")):
        stray.append("index.json")
    if stray:
        print("  %d file(s) of another format under data/: %s"
              % (len(stray), ", ".join(sorted(stray)[:6])))
    print("element files: %d  mismatched: %d  layout rows: %d"
          % (len(index["manifest"]), bad, len(index["layout"])))
    if len(index["manifest"]) != len(index["layout"]):
        bad += 1
        print("  manifest and layout disagree on the element count")
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
