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
import bisect
import collections
import contextlib
import csv
import datetime as _dt
import hashlib
import importlib.util
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
SITE_SUBTITLE = ("Every element on every axis of every index, each value carrying "
                 "the status the data gives it")

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

# ---------------------------------------------------------------------------
# the public build -- the site cites nothing from the unpublished books
# ---------------------------------------------------------------------------
# The books this index is drawn from are unpublished and not peer reviewed, and
# the author's ruling is that the public site references none of them: no
# register numbers, section numbers, member file names, line references or
# passages. The data, the statuses and the instruments stay; provenance outward
# is the public sources (NIST ASD, arXiv, DOI) and the papers the author has
# released to the site. PUBLIC_PAPERS names those; PRIVATE_PATTERNS is what may
# not appear in any string the site ships, and the selftest walks every string
# of index.js and every element file against it. Blocks drawn from papers not
# yet released (the muon material) build only behind --with-particles.
PUBLIC_PAPERS = {
    "THE-LOWDIN-SOLUTION-2.md": "the Löwdin paper",
    "The_Three_Body_Problem_for_Unknown_Masses_Lach-2.md": "the three-body paper",
}
PRIVATE_PATTERNS = [
    r"\b[Rr]egisters?\s+\d", r"\b[Ss]ections?\s+\d", r"§\s?\d", r"\bchapters?\s+\d",
    r"[A-Za-z0-9_\-]+\.md\b", r"\bL\d{2,5}\b(?![.\d])", r"The Method 1\.6", r"\bcorpus\b",
    r"\bCompendium\b", r"PROSE-ONLY", r"\bdockets?\b", r"\brulings?\b", r"\bseated members?\b",
    r"\bbundles?\b", r"method/members", r"\brecovered/", r"(?<![\w-])drive/", r"LW1-", r"r2-scf",
    r"tower-2\.py", r"\.tsv\b", r"rclose\.py", r"\bsessions?\s+\d", r"\bchats?\s+\d",
    r"\bhandoffs?\b", r"\bfaults?\s+\d",
]
_PRIVATE_RX = [re.compile(x) for x in PRIVATE_PATTERNS]
# names the site may print that a pattern would otherwise catch: the walk table
# is this repository's own reconstruction, not one of the books, and the two
# captures are public tables (PDG, spglib) written with their provenance
PUBLIC_NAMES = {"LOWDIN-WALK.tsv": "the walk table",
                "PDG-2026.tsv": "the PDG capture", "SPACEGROUPS-spglib.tsv": "the space-group capture",
                "THE-HIERARCHY-LAW.md": "the hierarchy law paper",
                "NUCBANDS-levels.tsv": "the band-level capture", "NUCBANDS-bands.tsv": "the band capture",
                "NUCBANDS-unplaced.tsv": "the unplaced-level capture", "DEFORMED-entries.tsv": "the deformed-band entry capture",
                "DEFORMED-levels.tsv": "the deformed-band level capture"}


def private_hits(text):
    """The private patterns a string matches, with the paper titles allowed."""
    if not isinstance(text, str):
        return []
    t = text
    for fn, title in list(PUBLIC_PAPERS.items()) + list(PUBLIC_NAMES.items()):
        t = t.replace(fn, title)
    return [rx.pattern for rx in _PRIVATE_RX if rx.search(t)]


def private_strings(obj, path="index", out=None, limit=40):
    """Every string in a JSON object that cites the private books, with its path."""
    out = [] if out is None else out
    if isinstance(obj, dict):
        for k, v in obj.items():
            k = str(k)
            if private_hits(k):
                out.append((path + "." + k, "(key) " + k))
            private_strings(v, path + "." + k, out, limit)
    elif isinstance(obj, list):
        for i, v in enumerate(obj):
            private_strings(v, path + "[%d]" % i, out, limit)
    elif isinstance(obj, str) and private_hits(obj):
        out.append((path, obj[:120]))
    return out


def public_text(s):
    """The narrow rewrites a data string needs to be public: the coordinates
    table's own source column names a register, and a walk note names a
    member. Everything else is written public at its source."""
    if not isinstance(s, str):
        return s
    s = re.sub(r"read from (\S+) levels, R 1627", r"read from the species' own level files", s)
    s = s.replace("NIST ASD fetched 2026-08-14 (session 1.8 queue)", "NIST ASD fetched 2026-08-14")
    s = s.replace("LW1-ground.py", "the observed configurations table")
    s = re.sub(r"\bregister 1706's eleven\b", "the Löwdin paper's eleven", s)
    s = re.sub(r"\bregister 1706\b", "the Löwdin paper", s)
    return s


def public_obj(obj):
    """public_text over every string of a JSON object, keys included."""
    if isinstance(obj, dict):
        return {public_text(k): public_obj(v) for k, v in obj.items()}
    if isinstance(obj, list):
        return [public_obj(v) for v in obj]
    return public_text(obj)


def redact_source(py):
    """An instrument's source for the public site: its code entire, its
    docstrings and comments kept only where they cite nothing private."""
    def fix_doc(m):
        body = m.group(2)
        if private_hits(body):
            return m.group(1) + "(docstring withheld on the public site: it cites the author's unpublished notes)" + m.group(1)
        return m.group(0)
    py = re.sub(r'(""")(.*?)(""")', lambda m: fix_doc(m), py, flags=re.S)
    out = []
    for ln in py.split("\n"):
        if "#" in ln:
            code, _, comment = ln.partition("#")
            if private_hits(comment):
                ln = code.rstrip() + ("  # (comment withheld)" if code.strip() else "# (comment withheld)")
        out.append(ln)
    return "\n".join(out)


STATUS_LEGEND = {
    "READ": "a measurement, taken as recorded from the source data",
    "PINNED": "a standing definition, stated at the precision a program needs",
    "DERIVED": "arithmetic on a READ or PINNED quantity, nothing added",
    "RECOVERED": "not stated anywhere in a program's form, but recovered by "
                 "measurement from the index's own computed column and consistent "
                 "with what is said of it qualitatively",
    "RECONSTRUCTED": "the object and its behaviour are stated but not the form a "
                     "program needs; reconstructed here, measured, and kept as "
                     "such so a later decision can move it",
}

# The site's own caveats, drawn from docs/POPULATE.md's "Known gaps" and
# "Two findings". They are shown on every page, not buried in a footnote.
CAVEATS = [
    {"id": "above-108",
     "text": "Elements above Z = 108 are not populated. The observed configurations "
             "stop at 108 because measurement does. COORDINATES-2.13 carries rows to "
             "Z = 120 and those are shown READ from the CSV with no configuration, "
             "equation or derived value behind them."},
    {"id": "b-aufbau",
     "text": "The spectra index's B column was built on a withdrawn configuration "
             "table (aufbau, patched by hand). The configurations were later corrected "
             "and COORDINATES-2.13 was never rebuilt on them. Where the observed table "
             "gives a different Pauli bound the site shows both and marks the "
             "disagreement."},
    {"id": "b-overloaded",
     "text": "25 measured rows carry a float in the B column: a dispersion of "
             "the median defect, not a bound. The site says 'B column is not a "
             "bound here' on those rows rather than comparing an integer "
             "against a spread."},
    {"id": "lambda8-mapping",
     "text": "A Λ₈ cell is a transition, so an element is not a cell. "
             "The mapping shown is the element's own ionisation ladder read off "
             "the observed configurations. Nothing fixes this mapping; it is "
             "RECONSTRUCTED and a later decision can move it."},
    {"id": "equation-domain",
     "text": "The channel equation is validated in its stated domain and "
             "extrapolated outside it. A residual on a channel outside that "
             "domain is not a finding against the equation."},
    {"id": "relativistic-not-held",
     "text": "The scalar-relativistic construction (Koelling\u2013Harmon "
             "Hartree\u2013Fock at c = 137) and its repetition at c \u2192 \u221e "
             "are not held: the code behind the L\u00f6wdin paper never arrived. "
             "The eleven displaced elements are READ from the paper's own statement "
             "and the site cannot recompute them."},
    {"id": "walk-reconstructed",
     "text": "The walk shown beside the paper is a RECONSTRUCTION "
             "(tools/lowdin_walk.py): the paper's construction rebuilt from its "
             "statement and run in two fields, a local-exchange one and the paper's "
             "own average-of-configuration Hartree\u2013Fock with non-local exchange, "
             "neither of them the paper's code, which never arrived. Where it "
             "agrees with the paper that is a measurement; where it disagrees "
             "that is a measurement too. It is never the paper's number."},
    {"id": "limit-kind",
     "text": "A limit kind is a classification of the csv's own bound note by "
             "the stated rule: the note is READ, the kind is DERIVED, and the "
             "rule is shown beside it. 'no analysis located' is, as the note "
             "itself says, not a bound on existence; a series limit is printed "
             "as the csv prints it, with no unit added."},
    {"id": "n0-reading",
     "text": "n₀'s reading is RECONSTRUCTED. The definition of B = min(p, n₀ − ℓ − 1) "
             "names its terms but not whether a partially filled subshell counts; "
             "'first entirely unoccupied n' matches the column at 97.7 % and He I "
             "settles it."},
]


# The eight kinds a bound note in COORDINATES-2.13 falls into. The note is READ;
# the kind is DERIVED by these rules, in this order, and the rules travel with
# the data so the page applies the same ones. Every one of the csv's distinct
# notes must match exactly one rule, and the selftest asserts it.
LIMIT_KINDS = [
    ("ionisation-limit", r"^limit [0-9.]+;",
     "a series limit the csv prints for the channel (one electron outside a "
     "closed shell); the value is shown as printed, no unit added"),
    ("unresolved", r"^series unresolved",
     "the series is unresolved above the stated n in any published analysis"),
    ("nuclear", r"^no (long-lived|primordial) isotope|^no nuclide synthesised",
     "a nuclear limit: no long-lived or primordial isotope, or no nuclide "
     "synthesised"),
    ("term", r"^not keyable",
     "no single 2S+1 keys the channel (hole plus electron, or multi-valence)"),
    ("coupling", r"^open-shell core",
     "an open-shell core with the stated number of parents"),
    ("no-analysis", r"^no analysis located|^none \u2014 separable",
     "no analysis located at this charge, or a separable series simply not "
     "yet measured; NOT a bound on existence, as the note says"),
    ("symmetry", r"^derived by symmetry",
     "delta = 0 by symmetry; no measurement required"),
    ("none", r"^-$",
     "the csv carries no note"),
]


def limit_kind(note):
    """The kind a bound note falls into, or None if no rule matches."""
    for kind, rx, _meaning in LIMIT_KINDS:
        if re.search(rx, note):
            return kind
    return None


def limits(spectra):
    """The bounds facet: every distinct bound note in COORDINATES-2.13 with its
    count and kind, and the kinds with their totals."""
    import collections
    notes = collections.Counter(r["bound"] for r in spectra.rows)
    kinds = collections.Counter()
    rows = []
    unclassified = []
    for note, n in notes.most_common():
        k = limit_kind(note)
        if k is None:
            unclassified.append(note)
        kinds[k] += n
        rows.append({"note": note, "kind": k, "count": n})
    return {
        "status": {"note": populate.READ, "kind": populate.DERIVED},
        "source": "COORDINATES-2.13, bound column",
        "rules": [{"kind": k, "regex": rx, "meaning": m} for k, rx, m in LIMIT_KINDS],
        "kinds": [{"kind": k, "count": kinds[k]} for k, _rx, _m in LIMIT_KINDS],
        "notes": rows,
        "distinct_notes": len(notes),
        "unclassified": unclassified,
    }


def _limit_counts(rec):
    out = {}
    for ch in rec["channels"]:
        for m in ch["measured"]:
            k = limit_kind(m["bound_note"]) or "unclassified"
            out[k] = out.get(k, 0) + 1
    return out


def _member_text(name):
    with open(os.path.join(populate.MEMBERS, name), encoding="utf-8") as fh:
        return fh.read()


def relativistic():
    """The relativistic limit, READ from the seated paper and the Register,
    with the instrument's held-status read from the delivery README and the
    SCF audit. Nothing here is computed: the construction is not held."""
    paper = "THE-LOWDIN-SOLUTION-2.md"
    lines = _member_text(paper).split("\n")
    def find(pattern):
        for i, l in enumerate(lines, 1):
            m = re.search(pattern, l)
            if m:
                s0 = l.rfind(". ", 0, m.start()) + 2 if ". " in l[:m.start()] else 0
                e0 = l.find(". ", m.end())
                return {"line": i, "text": l[s0:(e0 + 1 if e0 >= 0 else len(l))].strip()}
        return None
    eleven_s = find(r"They disagree at eleven elements: ")
    m = re.search(r"eleven elements: ([A-Z][a-z]?(?:, [A-Z][a-z]?)*), and ([A-Z][a-z]?)\.", eleven_s["text"])
    symbols = m.group(1).split(", ") + [m.group(2)]
    c137 = find(r"scalar-relativistic reduction of the Dirac equation as c = 137")
    thorium = find(r"inverts the underlying channel competition at thorium")
    irreducible = find(r"irreducibly relativistic: with the speed of light taken to infinity")
    # register 1706, first paragraph, verbatim
    reg = _member_text("The_Method_1_6___The_Register-2.md").split("\n")
    i = reg.index("### 1706")
    body = next(l for l in reg[i + 1:] if l.strip())
    # r2-scf.out: the eleven's configurations and entrants, and the budget
    scf = _member_text("r2-scf.out").split("\n")
    ent_line = next(l for l in scf if "the eleven in the observed table" in l)
    entrants = []
    for part in ent_line.split(": ", 1)[1].split(" | "):
        mm = re.match(r"([A-Z][a-z]?) (\d+) (.+?) ent (\S+)$", part.strip())
        entrants.append({"symbol": mm.group(1), "Z": int(mm.group(2)),
                         "configuration": mm.group(3), "entrant": mm.group(4)})
    count_line = next(l for l in scf if "eleven elements listed" in l)
    budget = next(l for l in scf if l.strip().startswith("UNREPRODUCIBLE with that budget"))
    readme = _member_text("LW1-README.md").split("\n")
    held_rows = [l for l in readme if "PENDING BANK" in l or "NOT HELD" in l]
    return {
        "status": populate.READ,
        "c": 137,
        "statement": irreducible["text"] if irreducible else None,
        "construction": c137["text"] if c137 else None,
        "eleven": [{"symbol": sym, "Z": populate.SYMBOL_TO_Z[sym],
                    **({e["symbol"]: e for e in entrants}.get(sym, {}) and
                       {"configuration": {e["symbol"]: e for e in entrants}[sym]["configuration"],
                        "entrant": {e["symbol"]: e for e in entrants}[sym]["entrant"]} or {})}
                   for sym in symbols],
        "thorium": thorium["text"] if thorium else None,
        "sources": {
            "paper": {"title": PUBLIC_PAPERS[paper], "eleven_line": eleven_s["line"],
                      "eleven_text": eleven_s["text"],
                      "construction_line": c137["line"] if c137 else None,
                      "thorium_line": thorium["line"] if thorium else None},
            "scf_audit": {"entrants": entrants},
        },
        "instrument": {
            "held": False,
            "note": "the scalar-relativistic construction and its c -> inf "
                    "repetition are not held; the figures are the paper's own",
        },
    }


FIGURE = "FIG6relativisticvsnonrelativistic.png"


def figure_source():
    """Figure 5 of the paper, as the extracted tree holds it, with the md5
    extracted/LEDGER.tsv records for it."""
    with open(os.path.join(REPO, "extracted", "LEDGER.tsv"), encoding="utf-8") as fh:
        for r in csv.DictReader(fh, delimiter="\t"):
            if r["member"].endswith(FIGURE) and r["disposition"] == "EXTRACTED":
                return {"path": os.path.join(REPO, r["target_path"]),
                        "md5_recorded": r["md5"], "bytes": int(r["size_bytes"]),
                        "archive": r["source"]}
    return None


WALK_TSV = os.path.join(REPO, "LOWDIN-WALK.tsv")
WALK_PY = os.path.join(TOOLS, "lowdin_walk.py")
_WALK_MOD = None


def walk_module():
    """tools/lowdin_walk.py, imported by path; the instrument, never copied."""
    global _WALK_MOD
    if _WALK_MOD is None:
        import importlib.util
        spec = importlib.util.spec_from_file_location("lowdin_walk", WALK_PY)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        _WALK_MOD = mod
    return _WALK_MOD


# The instrument's functions the page shows beside its own reading of the
# walk. Each carries RECONSTRUCTED: the record's field is Hartree-Fock and the
# instrument's is local-exchange, so nothing it returns is the record's number.
WALK_INSTRUMENTS = [
    ("walk_integrate", "integrate",
     "one shot of the Koelling-Harmon radial pair in x = ln r, RK4 outward "
     "from the r^gamma series and inward from the WKB tail, matched at the "
     "outer turning point; the Hartree matching correction"),
    ("walk_solve", "solve",
     "the bound state (n, l): node count brackets, the correction refines"),
    ("walk_potentials", "potentials",
     "Hartree + Kohn-Sham local exchange from the density; Latter's tail "
     "for the occupied orbitals, none for the added electron"),
    ("walk_scf", "scf",
     "the self-consistent field of the ion (Z, cfg), mixed to 1e-7"),
    ("walk_frontier", "frontier",
     "the unfilled (n, l) channels up to 8s and 8g"),
    ("walk_scan", "scan",
     "the candidate spectrum: one electron in each frontier channel of the "
     "frozen field, deepest first; the entrant is the first"),
    ("walk_hf_operator", "hf_operator",
     "the Hartree-Fock operator of one channel: the local part (direct and "
     "same-shell average-of-configuration exchange) and the non-local "
     "exchange source from every other occupied orbital"),
    ("walk_solve_inh", "solve_inh",
     "the orbital of the inhomogeneous equation, its energy fixed by the "
     "norm condition below the local pole, its multipliers by one Newton "
     "step to orthogonality"),
    ("walk_scf_hf", "scf_hf",
     "the Hartree-Fock field of the ion: per-equation multipliers and the "
     "pair rotation at which the energy is stationary"),
    ("walk_scan_hf", "scan_hf",
     "the candidate spectrum in the frozen Hartree-Fock field, each "
     "candidate's own exchange and multipliers iterated"),
]


def walk_instruments():
    lw = walk_module()
    out = {}
    for name, fn_name, source in WALK_INSTRUMENTS:
        fn = getattr(lw, fn_name)
        lines, start = inspect.getsourcelines(fn)
        out[name] = {"python": redact_source("".join(lines)), "file": "tools/lowdin_walk.py",
                     "line": start, "status": populate.RECON, "source": source}
    return out


def walk_rows_by_z(rows):
    """per Z, per field, the two settings' rows, values typed, the spectrum unpacked:
    {Z: {"Z", "symbol", "fields": {"lx": {"c137": row, "cinf": row, "displaced": bool},
    "hf": {...}}}}."""
    per_z = {}
    for r in rows:
        Z = int(r["Z"])
        d = per_z.setdefault(Z, {"Z": Z, "symbol": r["symbol"], "fields": {}})
        fld = d["fields"].setdefault(r.get("field", "lx"), {})
        key = "cinf" if r["c"] == "inf" else "c137"
        spec = []
        for tok in r["spectrum"].split(";"):
            ch, e = tok.split(":")
            spec.append({"channel": ch, "D": float(e)})
        fld[key] = {
            "c": r["c"], "cfg_prev": r["cfg_prev"], "entrant": r["entrant"],
            "D_ent": float(r["D_ent"]), "runner_up": r["runner_up"],
            "D_runner": (None if r["D_runner"] == "nan" else float(r["D_runner"])),
            "margin": (None if r["margin"] == "nan" else float(r["margin"])),
            "observed_gain": r["observed_gain"], "agree": r["agree"],
            "spectrum": spec, "scf_iterations": int(r["scf_iterations"]),
            "converged": r["converged"] == "yes", "status": r["status"],
        }
    for d in per_z.values():
        for fld in d["fields"].values():
            fld["displaced"] = ("c137" in fld and "cinf" in fld
                                and fld["c137"]["entrant"] != fld["cinf"]["entrant"])
    return per_z


def _public_walk_summary(summary):
    """The walk's summary as the site carries it: the paper's eleven under the
    key 'eleven', not under the number of the note that lists them."""
    def fix(o):
        if isinstance(o, dict):
            return {("eleven" if k == "eleven_1706" else k): fix(v) for k, v in o.items()}
        if isinstance(o, list):
            return [fix(v) for v in o]
        return o
    return fix(summary)


def walk_block():
    """The reconstruction of the walk -- tools/lowdin_walk.py over
    LOWDIN-WALK.tsv -- as the site carries it: the table's md5, the summary the
    instrument's own --report prints (openings, clauses, scores under each
    reading, the g-channel pins, the smallest margins, the displaced elements
    against register 1706's eleven, the thorium control), and one entrant per Z
    per setting. Every value is RECONSTRUCTED. The record's Lambda_chain and
    Lambda_cinf stay READ and unheld; this is placed beside them, not in their
    place. None if the table is absent."""
    if not os.path.exists(WALK_TSV):
        return None, {}
    lw = walk_module()
    rows = lw.read_rows(WALK_TSV)
    for r in rows:
        r.setdefault("field", "lx")
    per_z = walk_rows_by_z(rows)
    with open(WALK_TSV, "rb") as fh:
        blob = fh.read()
    grid = lw.Grid()
    summary = _public_walk_summary(lw.summarise(rows))
    field_names = {
        "lx": "Koelling-Harmon scalar-relativistic radial equation in a "
              "local-exchange (Kohn-Sham, V_x = -(3 rho/pi)^(1/3)) "
              "self-consistent field with Latter's tail: the Hartree-Fock-"
              "Slater construction, not the record's Hartree-Fock",
        "hf": "Koelling-Harmon scalar-relativistic radial equation in the "
              "average-of-configuration Hartree-Fock field with non-local "
              "exchange: the record's own field, rebuilt here",
    }
    not_reproduced = {
        "lx": "the record's non-local exchange; its collapse criterion; its "
              "correlation clause; its Z = 91 two-branch diagnostic",
        "hf": "the record's collapse criterion; its correlation clause; its "
              "Z = 91 two-branch diagnostic; and the record's own code, which "
              "never arrived -- this is a rebuild from its statement",
    }
    fields = {}
    for fld in ("lx", "hf"):
        if not any(fld in d["fields"] for d in per_z.values()):
            continue
        fields[fld] = {
            "field": fld,
            "name": field_names[fld],
            "not_reproduced": not_reproduced[fld],
            "entrants": [{"Z": Z, "symbol": d["symbol"],
                          "c137": d["fields"][fld].get("c137", {}).get("entrant"),
                          "cinf": d["fields"][fld].get("cinf", {}).get("entrant"),
                          "margin_c137": d["fields"][fld].get("c137", {}).get("margin"),
                          "margin_cinf": d["fields"][fld].get("cinf", {}).get("margin"),
                          "displaced": d["fields"][fld]["displaced"]}
                         for Z, d in sorted(per_z.items()) if fld in d["fields"]],
        }
    primary = summary.get("primary_field") or ("hf" if "hf" in fields else "lx")
    block = {
        "status": lw.STATUS,
        "instrument": "tools/lowdin_walk.py",
        "table": {"file": "LOWDIN-WALK.tsv", "bytes": len(blob),
                  "md5": hashlib.md5(blob).hexdigest(), "rows": len(rows)},
        "primary": primary,
        "field": field_names[primary],
        "not_reproduced": not_reproduced[primary],
        "fields": fields,
        "c": {"c137": lw.C_LIGHT, "cinf": None},
        "grid": {"r_min": grid.r[0], "r_max": grid.r[-1], "h": grid.h,
                 "points": grid.n},
        "summary": summary,
        # the primary field's entrants, for readers of the earlier shape
        "entrants": fields[primary]["entrants"],
    }
    return block, per_z


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


SITE_URL = "https://lach-matt.github.io/Claude-Method-Works/"
SITE_AUTHOR = "Lach, M."
PAPERS_JS = "papers.js"
PAPERS_PREFIX = "window.__mi = window.__mi || {}; window.__mi.papers = "
# where each released paper's figures live, as extracted/LEDGER.tsv names the
# archive: the paper cites `figures/<name>` and more than one archive holds a
# file of that name, so the paper's own delivery is named here
PAPER_FIGURE_ARCHIVES = {
    "THE-LOWDIN-SOLUTION-2.md": "The_Method_1_6_figures.zip",
    "The_Three_Body_Problem_for_Unknown_Masses_Lach-2.md": "THREEBODY-DELIVERY-1/THREEBODY-DELIVERY-1.zip",
}
PAPER_SLUGS = {
    "THE-LOWDIN-SOLUTION-2.md": "lowdin",
    "The_Three_Body_Problem_for_Unknown_Masses_Lach-2.md": "three-body",
}
# papers the author has named as released to the site but whose file is not
# in the repository: a slot on the site, held: false, never a fabricated body
PAPER_SLOTS = []
# papers released to the site from the research tree rather than the store: the
# author's own text, in the repository under research/, with no ledger row to
# check against -- so the md5 is measured at build and the file's last commit
# recorded beside it, and a PDF beside the text is carried as a download
_OWN_SECTION_MARKS = {r"\b[Ss]ections?\s+\d", r"§\s?\d"}
RESEARCH_PAPERS = {
    "research/warp-drive/paper/THE-HIERARCHY-LAW.md": {
        "slug": "languages", "short": "the hierarchy law paper",
        "pdf": "research/warp-drive/paper/pdf/THE-HIERARCHY-LAW.pdf",
    },
}
# the edition history the site shows: the commits that changed public/ or the
# generator, each with a note written for the site (the commit subjects are
# git's record, not the site's, and are not shipped)
EDITION_NOTES = {
    "745414d": "first page",
    "a4cd621": "interactive index, first pass",
    "ef7b325": "touch-first site; data as script files; solver suite; coefficient calculator",
    "86276a0": "the relativistic limit as a seventh mode; the bounds facet",
    "d415284": "mode 7 asserts both directions, thorium the null-difference control",
    "0360a25": "the Löwdin delivery's reply cited from the store",
    "e9b77f6": "the Löwdin walk reconstructed beside the paper, at both settings",
    "5755759": "a Hartree-Fock field with non-local exchange, in progress",
    "ab7a374": "the walk in the paper's own Hartree-Fock field, 476 rows",
    "5e55930": "the thirty-six cells carry their definitions; helium's placement offered",
    "fc8bcdb": "the lattice in three dimensions: every element its slab, rotatable and zoomable",
    "81bd08e": "particles and binders; references linked by construction; the muon balance as a mode",
    "3f71e96": "set like a reference work: type, palette, frame",
    "337b922": "the index's cells drawn as a table, not a grid",
    "3c1abef": "the lattice drawn as a figure: fitted, grounded, labelled",
    "07f9ff7": "the lattice's cells as nodes",
    "2d0d5e3": "the public build: the site cites nothing from the unpublished books",
}


def _git_history():
    """The commits that changed the site, oldest first: date, short hash and
    the number of files each touched under public/ or the generator."""
    try:
        out = subprocess.run(["git", "log", "--date=short", "--format=%H%x09%h%x09%ad", "--",
                              "public/", "tools/webindex.py"],
                             cwd=REPO, capture_output=True, text=True, check=True)
    except Exception:  # noqa: BLE001 -- provenance is best effort
        return []
    rows = []
    for ln in out.stdout.strip().split("\n"):
        if not ln.strip():
            continue
        full, short, date = ln.split("\t")
        try:
            files = subprocess.run(["git", "show", "--format=", "--name-only", full, "--",
                                    "public/", "tools/webindex.py"],
                                   cwd=REPO, capture_output=True, text=True, check=True).stdout.split()
        except Exception:  # noqa: BLE001
            files = []
        rows.append({"date": date, "commit": short, "files": len(files),
                     "url": "https://github.com/lach-matt/Claude-Method-Works/commit/" + full,
                     "note": next((n for k, n in EDITION_NOTES.items() if short.startswith(k)), None)})
    rows.reverse()
    return rows


def cite_block(head):
    year = _dt.datetime.now(_dt.timezone.utc).year
    return {"author": SITE_AUTHOR, "title": SITE_TITLE, "year": year, "url": SITE_URL,
            "commit": head,
            "text": "%s (%d). %s, edition %s. %s" % (SITE_AUTHOR, year, SITE_TITLE, head or "?", SITE_URL),
            "bibtex": "@misc{lach%d_method_index,\n  author = {Lach, M.},\n  title = {%s},\n"
                      "  year = {%d},\n  howpublished = {\\url{%s}},\n  note = {edition %s}\n}"
                      % (year, SITE_TITLE, year, SITE_URL, head or "?")}


# --- a small Markdown renderer for the released papers -----------------------
_MD_INLINE = [
    (re.compile(r"!\[([^\]]*)\]\(([^)]+)\)"), lambda m, ctx: ctx["img"](m.group(1), m.group(2))),
    (re.compile(r"\[([^\]]+)\]\(([^)]+)\)"), lambda m, ctx: '<a href="%s" target="_blank" rel="noopener noreferrer">%s</a>' % (m.group(2), m.group(1))),
    (re.compile(r"`([^`]+)`"), lambda m, ctx: "<code>%s</code>" % m.group(1)),
    (re.compile(r"\*\*\*(.+?)\*\*\*"), lambda m, ctx: "<b><i>%s</i></b>" % m.group(1)),
    (re.compile(r"\*\*(.+?)\*\*"), lambda m, ctx: "<b>%s</b>" % m.group(1)),
    (re.compile(r"(?<![\w*])\*(?!\s)(.+?)(?<!\s)\*(?![\w*])"), lambda m, ctx: "<i>%s</i>" % m.group(1)),
]


def _md_inline(text, ctx):
    text = html_escape(text)
    # identifiers first, so a link's own URL is not re-linked inside a tag
    text = ARXIV_NEW.sub(lambda m: '<a href="https://arxiv.org/abs/%s" target="_blank" rel="noopener noreferrer">%s</a>' % (m.group(1), m.group(0)), text)
    text = ARXIV_OLD.sub(lambda m: '<a href="https://arxiv.org/abs/%s" target="_blank" rel="noopener noreferrer">%s</a>' % (m.group(1), m.group(0)), text)
    text = re.sub(r"(?<![/\w])(10\.\d{4,9}/[^\s\"'<>,;)\]]+)", lambda m: '<a href="https://doi.org/%s" target="_blank" rel="noopener noreferrer">%s</a>' % (m.group(1).rstrip("."), m.group(1)), text)
    for rx, fn in _MD_INLINE:
        text = rx.sub(lambda m, fn=fn: fn(m, ctx), text)
    return text


def html_escape(t):
    return t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def _slugify(t):
    t = re.sub(r"<[^>]+>", "", t)
    t = re.sub(r"[^A-Za-z0-9]+", "-", t).strip("-").lower()
    return t[:60] or "s"


def md_to_html(text, ctx):
    """Headings, paragraphs, lists, blockquotes, fenced code, pipe tables,
    rules and images, with the inline forms above. Not a Markdown engine; the
    two released papers use no more than this, and the selftest asserts the
    render carries every heading of the source."""
    out, headings = [], []
    lines = text.split("\n")
    i, n = 0, len(lines)
    para = []

    def flush():
        if para:
            out.append("<p>%s</p>" % _md_inline(" ".join(x.strip() for x in para), ctx))
            para.clear()
    while i < n:
        ln = lines[i]
        st = ln.strip()
        if st.startswith("```"):
            flush()
            j = i + 1
            code = []
            while j < n and not lines[j].strip().startswith("```"):
                code.append(lines[j]); j += 1
            out.append("<pre><code>%s</code></pre>" % html_escape("\n".join(code)))
            i = j + 1
            continue
        m = re.match(r"^(#{1,6})\s+(.*)$", st)
        if m:
            flush()
            lvl, txt = len(m.group(1)), _md_inline(m.group(2).strip(), ctx)
            hid = "h-%d-%s" % (len(headings) + 1, _slugify(m.group(2)))
            headings.append({"level": lvl, "text": re.sub(r"<[^>]+>", "", txt), "id": hid})
            out.append('<h%d id="%s">%s</h%d>' % (lvl, hid, txt, lvl))
            i += 1
            continue
        if re.match(r"^(-{3,}|\*{3,}|_{3,})$", st):
            flush(); out.append("<hr>"); i += 1; continue
        if st.startswith("|") and i + 1 < n and re.match(r"^\|?\s*:?-{2,}", lines[i + 1].strip()):
            flush()
            hdr = [c.strip() for c in st.strip("|").split("|")]
            j = i + 2
            body = []
            while j < n and lines[j].strip().startswith("|"):
                body.append([c.strip() for c in lines[j].strip().strip("|").split("|")]); j += 1
            out.append('<div class="tbl-wrap"><table class="t"><thead><tr>%s</tr></thead><tbody>%s</tbody></table></div>' % (
                "".join("<th>%s</th>" % _md_inline(c, ctx) for c in hdr),
                "".join("<tr>%s</tr>" % "".join("<td>%s</td>" % _md_inline(c, ctx) for c in r) for r in body)))
            i = j
            continue
        if st.startswith(">"):
            flush()
            q = []
            while i < n and lines[i].strip().startswith(">"):
                q.append(lines[i].strip()[1:].strip()); i += 1
            out.append("<blockquote>%s</blockquote>" % "".join("<p>%s</p>" % _md_inline(x, ctx) for x in " ".join(q).split("  ") if x.strip()))
            continue
        lm = re.match(r"^(\s*)([-*]|\d+[.)])\s+(.*)$", ln)
        if lm:
            flush()
            ordered = lm.group(2)[0].isdigit()
            items = []
            while i < n:
                lm2 = re.match(r"^(\s*)([-*]|\d+[.)])\s+(.*)$", lines[i])
                if lm2:
                    items.append(lm2.group(3)); i += 1
                elif lines[i].strip() and lines[i].startswith("  ") and items:
                    items[-1] += " " + lines[i].strip(); i += 1
                else:
                    break
            tag = "ol" if ordered else "ul"
            out.append("<%s>%s</%s>" % (tag, "".join("<li>%s</li>" % _md_inline(x, ctx) for x in items), tag))
            continue
        if not st:
            flush(); i += 1; continue
        para.append(ln)
        i += 1
    flush()
    return "\n".join(out), headings


def _ledger_figure(name, archive_hint):
    """The extracted figure a paper cites by `figures/<name>`, from the ledger
    row of the paper's own archive; None when the ledger holds no such row."""
    with open(os.path.join(REPO, "extracted", "LEDGER.tsv"), encoding="utf-8") as fh:
        rows = [r for r in csv.DictReader(fh, delimiter="\t")
                if os.path.basename(r["member"]) == name and r["disposition"] in ("EXTRACTED", "DUP-OF-EXTRACTED")]
    rows = [r for r in rows if archive_hint in r["source"]] or rows
    for r in rows:
        path = os.path.join(REPO, r["target_path"])
        if os.path.exists(path):
            return {"path": path, "md5_recorded": r["md5"], "bytes": int(r["size_bytes"])}
    return None


def papers_block(out_dir=OUT, write=True, log=print):
    """The released papers as the site reads them: each rendered to HTML at
    build from its seated text (the text is the author's own and is shipped as
    written), its headings as a table of contents, its figures copied from the
    extracted tree with their ledger md5, and every arXiv or DOI identifier it
    prints. Written to data/papers.js, loaded on demand."""
    papers = []
    for fn, short in PUBLIC_PAPERS.items():
        path = os.path.join(MEMBERS, fn)
        with open(path, "rb") as fh:
            raw = fh.read()
        text = raw.decode("utf-8")
        slug = PAPER_SLUGS[fn]
        figs = []
        figdir = os.path.join(out_dir, "papers", slug, "figures")

        def img(alt, src, _slug=slug, _figs=figs, _figdir=figdir, _fn=fn):
            name = os.path.basename(src)
            f = _ledger_figure(name, PAPER_FIGURE_ARCHIVES[_fn])
            rel = "papers/%s/figures/%s" % (_slug, name)
            if f is None:
                _figs.append({"ref": src, "file": None, "held": False})
                return '<span class="fig-missing">[figure %s: not held in the extracted tree]</span>' % html_escape(name)
            with open(f["path"], "rb") as fh:
                blob = fh.read()
            md5 = hashlib.md5(blob).hexdigest()
            if write:
                os.makedirs(_figdir, exist_ok=True)
                with open(os.path.join(_figdir, name), "wb") as fh:
                    fh.write(blob)
            _figs.append({"ref": src, "file": rel, "held": True, "bytes": len(blob), "md5": md5,
                          "md5_recorded": f["md5_recorded"], "ok": md5 == f["md5_recorded"]})
            alt = re.sub(r"[*_]", "", alt).strip()
            return '<img src="data/%s" alt="%s" loading="lazy">' % (rel, html_escape(alt))
        body, headings = md_to_html(text, {"img": img})
        h1 = next((h for h in headings if h["level"] == 1), None)
        h2 = next((h for h in headings if h["level"] == 2), None)
        arx = sorted({m.group(1) for m in ARXIV_NEW.finditer(text)} | {m.group(1) for m in ARXIV_OLD.finditer(text)})
        dois = sorted({m.group(1).rstrip(".)") for m in DOI_RX.finditer(text)})
        row = _member_row(fn)
        papers.append({
            "slug": slug, "short": short,
            "title": (h1 or {}).get("text") or short,
            "subtitle": (h2 or {}).get("text") if h2 and headings.index(h2) == 1 else None,
            "author": SITE_AUTHOR,
            "held": True,
            "bytes": len(raw), "md5": hashlib.md5(raw).hexdigest(),
            "md5_recorded": row["md5"] if row else None,
            "words": len(text.split()),
            "headings": headings,
            "figures": figs,
            "arxiv": arx, "doi": dois,
            "html": body,
            "note": "the paper as the author wrote it, rendered at build; nothing in it is edited "
                    "for the site, and its own citations are its own",
        })
    for rel, spec in RESEARCH_PAPERS.items():
        path = os.path.join(REPO, rel)
        if not os.path.isfile(path):
            papers.append({"slug": spec["slug"], "short": spec["short"], "title": spec["short"], "held": False, "author": SITE_AUTHOR,
                           "note": "named by the author as released; its file is not in this tree, so the site lists it and shows nothing in its place"})
            continue
        with open(path, "rb") as fh:
            raw = fh.read()
        text = raw.decode("utf-8")
        slug = spec["slug"]
        figs = []

        def img_r(alt, src, _figs=figs):
            _figs.append({"ref": src, "file": None, "held": False})
            return '<span class="fig-missing">[figure %s: not carried]</span>' % html_escape(os.path.basename(src))
        body, headings = md_to_html(text, {"img": img_r})
        h1 = next((h for h in headings if h["level"] == 1), None)
        arx = sorted({m.group(1) for m in ARXIV_NEW.finditer(text)} | {m.group(1) for m in ARXIV_OLD.finditer(text)})
        dois = sorted({m.group(1).rstrip(".)") for m in DOI_RX.finditer(text)})
        pdf = None
        if spec.get("pdf") and os.path.isfile(os.path.join(REPO, spec["pdf"])):
            with open(os.path.join(REPO, spec["pdf"]), "rb") as fh:
                pblob = fh.read()
            prel = "papers/%s/%s" % (slug, os.path.basename(spec["pdf"]))
            if write:
                os.makedirs(os.path.join(out_dir, "papers", slug), exist_ok=True)
                with open(os.path.join(out_dir, prel), "wb") as fh:
                    fh.write(pblob)
            pdf = {"file": prel, "bytes": len(pblob), "md5": hashlib.md5(pblob).hexdigest(), "commit": _git_last_commit(spec["pdf"])}
        papers.append({
            "slug": slug, "short": spec["short"],
            "title": (h1 or {}).get("text") or spec["short"],
            "subtitle": _paper_byline(text),
            "author": SITE_AUTHOR,
            "held": True,
            "bytes": len(raw), "md5": hashlib.md5(raw).hexdigest(),
            "md5_recorded": None,
            "tree": {"path": rel, "commit": _git_last_commit(rel)},
            "words": len(text.split()),
            "headings": headings,
            "figures": figs,
            "arxiv": arx, "doi": dois,
            "pdf": pdf,
            "html": body,
            # the guard as a measurement over the paper's text: the section-number patterns are
            # excluded because the paper numbers its own sections with § and "Section n", which
            # are its own marks and not citations of the books; every other pattern counts
            "book_citations": [h for h in private_hits(text) if h not in _OWN_SECTION_MARKS],
            "own_section_marks": [h for h in private_hits(text) if h in _OWN_SECTION_MARKS],
            "note": "the paper as the author wrote it, from the repository's research tree rather than the store: "
                    "no ledger row records its md5, so the md5 is measured at build and the file's last commit "
                    "is recorded beside it; nothing in it is edited for the site",
        })
    for slot in PAPER_SLOTS:
        papers.append(dict(slot, author=SITE_AUTHOR))
    blob = (PAPERS_PREFIX + json.dumps(papers, ensure_ascii=False, allow_nan=False) + WRAP_SUFFIX).encode("utf-8")
    if write:
        with open(os.path.join(out_dir, PAPERS_JS), "wb") as fh:
            fh.write(blob)
    summary = [{k: p.get(k) for k in ("slug", "title", "subtitle", "author", "held", "bytes", "md5",
                                        "md5_recorded", "words", "note", "tree", "pdf")}
               | {"headings": len(p.get("headings", [])), "figures": len(p.get("figures", [])),
                  "figures_ok": all(f.get("ok") for f in p.get("figures", []) if f.get("held")),
                  "arxiv": len(p.get("arxiv", [])), "doi": len(p.get("doi", []))}
               for p in papers]
    return {"file": "data/" + PAPERS_JS, "bytes": len(blob), "md5": hashlib.md5(blob).hexdigest(),
            "protocol": "data/papers.js sets window.__mi.papers, loaded on demand",
            "papers": summary}


def _git_last_commit(rel):
    """The short hash of the last commit that touched `rel`, or None."""
    try:
        return subprocess.run(["git", "log", "-1", "--format=%h", "--", rel], cwd=REPO,
                              capture_output=True, text=True, check=True).stdout.strip() or None
    except Exception:  # noqa: BLE001 -- not a git checkout
        return None


def _paper_byline(text):
    """The bold byline of a research paper (author · affiliation · date), or None."""
    for ln in text.split("\n")[1:12]:
        s = ln.strip()
        if s.startswith("**") and "·" in s:
            return re.sub(r"[*_]", "", s).strip()
    return None


def equation_points(spectra):
    """Every measured channel with its measured delta and the equation's, for
    the figure the page draws: [Z, charge, l, delta_measured, delta_equation].
    The same rows equation_figures scores, so the two cannot disagree."""
    pts = []
    for r in spectra.rows:
        if r["grade"] != "measured":
            continue
        Z, c, l = int(r["Z"]), int(r["charge"]), int(r["l"])
        if (Z - c) >= 1 and (Z - c) not in populate.LW1.GROUND:
            continue
        eq = populate.channel_delta(Z, c, l, "observed")
        if eq is None:
            continue
        pts.append([Z, c, l, float(r["delta"]), round(eq, 6)])
    return {"status": populate.PINNED, "rows": pts,
            "columns": ["Z", "charge", "l", "delta_measured", "delta_equation"],
            "source": "COORDINATES-2.13's measured rows (delta READ) against the channel "
                      "equation as populate.channel_delta computes it (PINNED)"}


# ---------------------------------------------------------------------------
# the particle indexes -- DOCKET 27 and 28 of research/warp-drive/
# ---------------------------------------------------------------------------
# The other session's tree seats three indexes of the particles that are not
# periodic atoms -- the 30 fundamental particles, the 250 mesons and the 292
# baryons of the PDG 2026 table, captured once with its provenance -- and a
# docket-28 finding on quasiparticles. The site imports those instruments by
# path and ships what they report: every member with its coordinates, each
# value carrying a status; the cells, the channel, the collisions; every
# refused coordinate with the measurement that refuses it. Nothing here is
# retyped: a figure the instruments do not return is not on the site.
WARP_ROOT = os.path.join(REPO, "research", "warp-drive")
PARTICLES_JS = "particles.js"
PARTICLES_PREFIX = "window.__mi = window.__mi || {}; window.__mi.particle_index = "
_WARP = {}


def warp_modules(root):
    """The particle instruments imported from the warp tree at `root`, once.
    They import each other by bare name and reach the repository's tools/ two
    levels up, so the tree's own directory goes on sys.path and nothing is
    copied."""
    root = os.path.abspath(root)
    if root in _WARP:
        return _WARP[root]
    if not os.path.isfile(os.path.join(root, "fundamental.py")):
        _WARP[root] = None
        return None
    import importlib
    # the root stays on sys.path: registry imports the other instruments lazily by name
    if root not in sys.path:
        sys.path.insert(0, root)
    mods = {n: importlib.import_module(n)
            for n in ("pdgcapture", "fundamental", "mesons", "baryons", "docket27", "registry")}
    try:
        mods["fqh"] = importlib.import_module("fqh")
    except Exception as e:  # noqa: BLE001 -- DOCKET 30 may not be in an older tree
        mods["fqh"] = None
        mods["fqh_error"] = repr(e)
    for extra in ("bosonqp", "readrezayi"):
        try:
            mods[extra] = importlib.import_module(extra)
        except Exception as e:  # noqa: BLE001 -- DOCKET 31/32 may not be in an older tree
            mods[extra] = None
            mods[extra + "_error"] = repr(e)
    try:
        mods["particlesweep"] = importlib.import_module("particlesweep")
    except Exception as e:  # noqa: BLE001 -- DOCKET 29 may not be in an older tree
        mods["particlesweep"] = None
        mods["particlesweep_error"] = repr(e)
    try:
        mods["quasiparticle"] = importlib.import_module("quasiparticle")
    except Exception as e:  # noqa: BLE001 -- the docket is in progress on the other session
        mods["quasiparticle"] = None
        mods["quasiparticle_error"] = repr(e)
    for extra in ("spin4", "subpop", "nucbands", "nbcapture", "deformed", "bonds", "predict", "ghosts", "demand"):
        try:
            mods[extra] = importlib.import_module(extra)
        except Exception as e:  # noqa: BLE001 -- DOCKET 33-39 may not be in an older tree
            mods[extra] = None
            mods[extra + "_error"] = repr(e)
    mods["root"] = root
    _WARP[root] = mods
    return mods


def _warp_commit(root):
    try:
        with open(os.path.join(root, "STATE.json"), encoding="utf-8") as fh:
            return json.load(fh).get("commit")
    except Exception:  # noqa: BLE001
        return None


PARTICLE_COORDS = {
    "fundamental": [
        {"name": "2J", "meaning": "spin, doubled so it is an integer", "status": "READ"},
        {"name": "Q3", "meaning": "electric charge in thirds, so a quark's is an integer", "status": "READ"},
        {"name": "COL", "meaning": "the dimension of the colour representation: 3 for a quark, 8 for the gluon, 1 otherwise; not in the capture, assigned from the Standard Model's definition and the assignment printed", "status": "PINNED"},
        {"name": "GEN", "meaning": "generation, 1 to 3 for a fermion and 0 for a boson, derived from the PDG id", "status": "DERIVED"},
    ],
    "mesons": [
        {"name": "2J", "meaning": "spin, doubled", "status": "READ"},
        {"name": "P", "meaning": "parity", "status": "READ"},
        {"name": "2I", "meaning": "isospin, doubled", "status": "READ"},
        {"name": "Q3", "meaning": "electric charge in thirds", "status": "READ"},
    ],
    "spin4": [
        {"name": "P", "meaning": "parity", "status": "READ"},
        {"name": "2I", "meaning": "isospin, doubled", "status": "READ"},
        {"name": "Q3", "meaning": "electric charge in thirds", "status": "READ"},
    ],
    "baryons": [
        {"name": "2J", "meaning": "spin, doubled", "status": "READ"},
        {"name": "P", "meaning": "parity", "status": "READ"},
        {"name": "2I", "meaning": "isospin, doubled", "status": "READ"},
        {"name": "Q3", "meaning": "electric charge in thirds", "status": "READ"},
        {"name": "S", "meaning": "strangeness, from the quark content by the pinned case convention", "status": "DERIVED"},
        {"name": "C", "meaning": "charm, likewise", "status": "DERIVED"},
        {"name": "B", "meaning": "beauty, likewise", "status": "DERIVED"},
    ],
}
PARTICLE_TITLES = {
    "fundamental": "The fundamental particles of the Standard Model",
    "mesons": "The mesons",
    "baryons": "The baryons",
    "spin4": "The spin-4 mesons",
}


def _antimatter(D27, F):
    """Antimatter counted rather than implied, and the three particles the
    author asked for by name, resolved by name with their cells."""
    rows, tot = D27.antimatter()
    _m, charted, _u = D27.charted()
    names = {t[0]: t for t in F.rows()}
    named = []
    for what, where, cell in D27.named_by_hand():
        sym = {"photon": "gamma", "muon": "mu-", "antimuon": "mu+"}[what]
        named.append({"what": what, "name": sym, "index": where.split(".")[0], "cell": list(cell),
                      "coordinates": dict(zip(F.NAMES, cell))})
    return {
        "antimatter": {"by_index": [{"index": a, "antiparticles": b, "members": c} for a, b, c in rows],
                       "total": tot, "of_charted": charted, "share": round(tot / float(charted), 2),
                       "note": "an antiparticle is a member in its own right, never a footnote on the particle: the positron's charge is not the electron's, and a chart that merged them would be charting an equivalence class it had not declared",
                       "status": "DERIVED"},
        "named": {"rows": named, "status": "READ",
                  "note": "a total can be right while a named member is missing, so the three the author asked for are resolved by name; the photon shares its cell with the Z, because no quantum number separates them"},
    }


def _sweep(PS):
    """DOCKET 29 as the site carries it: every chart the three member sets
    admit, swept; the seating, the two refusals, and the measurements."""
    OR = PS.OR
    census = PS.census()
    honest = PS.honest_occupancy()
    current = PS.current_occupancy()
    ruling = OR.seated_channels()
    hits_r = PS.hits()
    hits_h = PS.hits(honest)
    parent, cols, chan = PS.SEATED
    X = OR.baryon_isomultiplet()
    K, h, w = PS.mi.cell(X)
    grounds = OR.grounds(parent, cols)
    ok, nhit, ntot, late, osc, maj, reach = OR.ground_reach_stable(parent, cols)
    missing, outside = PS.corners_outside_hull()
    refused_why = {
        ("baryons", ("P", "2I", "Q3")): "K1 is already held by a seated row of the overlap rule; that rule's own census leaves its rows out because novelty there means novel against the index the rule was handed, and that exclusion does not transfer to a new parent",
        ("fundamental", ("Q3", "GEN")): "arity 2: the statistics language closes every arity-2 chart in the tree for free (105 of 105), so what the chart shows is join-closure, which is K1, and K1 is occupied; it is the third arity-2 chart to reach K4 and the third refused",
    }
    return {
        "status_note": "every sub-chart of every particle member set, each subset of its declared columns of size two or more, enumerated and adjudicated against the index as it stands; a census, not a search. The sweep is the other session's; the site reads its record",
        "census": {p: len(v) for p, v in census.items()},
        "charts": sum(len(v) for v in census.values()),
        "by_channel": {p: sorted(((list(c), n, k) for c, n, k in v), key=lambda t: (t[2], -t[1])) for p, v in census.items()},
        "occupancy": {"before_this_sweep": sorted(honest), "now": sorted(current), "by_the_overlap_rules_own_census": sorted(ruling),
                      "gap": PS.occupancy_gap(),
                      "note": "the honest occupancy counts the overlap rule's seated rows and leaves out the row this sweep itself seated; the rule's own census leaves its rows out, which is right for its question and not for this one"},
        "hits": {"against_the_overlap_rules_census": [{"parent": a, "cols": list(b), "cells": c, "channel": d} for a, b, c, d in hits_r],
                 "against_the_honest_occupancy": [{"parent": a, "cols": list(b), "cells": c, "channel": d} for a, b, c, d in hits_h]},
        "seated": {"parent": parent, "cols": list(cols), "channel": chan, "cells": len(X),
                   "cell": {"channel": K, "height": h, "width": w},
                   "registered_as": "baryon_isomultiplet: the same 278 baryons, isospin against charge with flavour dropped",
                   "grounds": grounds, "grounds_note": "the overlap rule's four grounds, each measured",
                   "reach": {"passes": ok, "hits": nhit, "cuts": ntot, "late": late, "oscillates": osc, "majority": maj,
                             "sweep": [{"cut": a, "cells": b, "channel": c} for a, b, c in reach]},
                   "rows": [{"I2": i, "Q3": q} for i, q in PS.isomultiplet_rows()],
                   "corners_not_held": [list(m) for m in missing], "corners_outside_hull": outside,
                   "reading": "a multiplet's charge span widens with its isospin, steeply enough to cut the corners off; the chart is that widening and nothing else. Geometry is hull-completeness on coordinate pairs, and the four box points the chart does not hold fall outside the convex hull of the sixteen it does",
                   "why_arity_2_does_not_reach_it": "at K5 the statistics bit is forced by law from geometry, so the free pass changes nothing and the seating stands on geometry, which 31 of the 105 arity-2 charts fail",
                   "status": "DERIVED", "verdict_status": "READ"},
        "refused": [{"parent": a, "cols": list(b), "channel": c, "why": refused_why.get((a, b), d),
                     "cells": next((n for cc, n, k in census[a] if cc == b), None), "verdict": "REFUSED", "status": "READ"}
                    for a, b, c, d in PS.REFUSED],
        "arity2_freeness": {L: {"closes": a, "charts": b} for L, (a, b) in PS.arity2_freeness().items()},
        "claimed": "over the three particle member sets, every chart their declared columns admit has been enumerated and adjudicated: one seated, two refused with reasons, and the rest reach an occupied channel",
        "not_claimed": ["a chart on a coordinate none of the three modules declares (C-parity, G-parity, lepton number, mass) is not in this census; each was refused in its own module for a stated reason, and reaching for one after seeing which channels are short would be a fitted move",
                        "the registry does not claim completeness: this is a census over three member sets, not over member sets nobody has thought of"],
        "channels_note": "seven of the eight closure channels are now occupied; only K4 is empty, and every chart that ever reached it was arity 2",
    }


def _fqh(FQ):
    """DOCKET 30 as the site carries it: the quasiparticles of the Laughlin
    states, computed from the closed form, indexed by a measured filling."""
    rows = FQ.rows()
    K, h, w = FQ.cell()
    verdict, why = FQ.verdict()
    anyons, fermions, bosons = FQ.anyon_fraction()
    return {
        "id": "fqh", "title": "The quasiparticles of the fractional quantum Hall states",
        "member": "a quasiparticle of the Laughlin state at filling 1/m, m odd; the state has exactly m of them, j = 0 to m − 1, and j = 0 is the vacuum",
        "source": FQ.SOURCE[0], "source_status": "PINNED",
        "source_note": "computed from a closed form, not read from a table; every coordinate is an exact rational",
        "reach": FQ.REACH, "states": len(FQ.states()), "members": len(rows), "charted": len(rows),
        "observed": [{"m": m, "filling": f, "fundamental_charge": q} for m, f, q in FQ.observed_states()],
        "observed_note": "three of the twelve states have a reported plateau; the rest are the sequence's own continuation, declared as such because a rule's continuation is not a measurement",
        "coordinates": [
            {"name": "STAT", "meaning": "0 boson, 1 fermion, 2 anyon, from the exchange phase θ/π = j²/m mod 1", "status": "DERIVED"},
            {"name": "ORD", "meaning": "the order of the exchange phase: the denominator of θ/π", "status": "DERIVED"},
            {"name": "CHORD", "meaning": "the order of the charge: the denominator of Q = j/m", "status": "DERIVED"},
            {"name": "M", "meaning": "the inverse filling fraction; 1/m is the quantised Hall conductance in units of e²/h, the number the experiment reads off the plateau", "status": "READ"},
        ],
        "refused": [{"coordinate": "j, Q, θ", "verdict": "REFUSED", "status": "READ",
                     "why": "j is the quasiparticle's address within its state, and charting it would be a relabelling; Q and θ are near-injective rationals, which the overlap rule calls row labels; their orders are charted instead"}],
        "cells": len(FQ.index()), "cell": {"channel": K, "height": h, "width": w}, "closers": FQ.closers(FQ.index()),
        "rows": [{"m": m, "j": j, "Q": _frac(Q), "theta": _frac(t), "coords": [st, o, c, m], "observed": m in FQ.OBSERVED}
                 for m, j, Q, t, st, o, c in rows],
        "sweep": [{"box": a, "cells": b, "channel": c, "closers": d, "degenerate": g} for a, b, c, d, _e, _f, g in FQ.sweep()],
        "verdict": verdict, "why": why, "verdict_status": "READ",
        "verdict_note": "the box is a reach over one kind of system, more of the same thing further out, and the channel moves with it, K2 then K0; the earlier anyon chart varied which theories were included rather than how much data there was",
        "statistics": {"anyons": anyons, "fermions": fermions, "bosons": bosons, "status": "DERIVED",
                       "note": "not one of the members is a fermion, and it is forced: θ/π = j²/m is a half-integer only if m divides 2j², and m is odd, so the phase is a whole integer instead"},
        "fractional_charges": [{"m": m, "denominators": d} for m, d in FQ.fractional_charges()],
        "e_over_3": {"text": "the e/3 quasiparticle is not a prediction: its fractional charge was measured directly by shot noise in 1997, in a system built only from electrons", "status": "READ"},
        "not_here": "the non-abelian states (Moore–Read, Read–Rezayi) are a further member set and are not here",
        "in_progress": True,
    }


def _bosonqp(BQ):
    """DOCKET 31 as the site carries it: the composite bosonic excitations,
    every number computed by three stated rules from what the object is made
    of, as a sublattice beside the tree's own bosons."""
    K, h, w = BQ.cell()
    nb, nq, bsub, qsub, subset, outside, nunion, usub = BQ.relation()
    tot, full, n5, f5 = BQ.box_freeness()
    return {
        "id": "bosonqp", "title": "The composite bosonic excitations, as a sublattice of the bosons",
        "member": "a bosonic collective excitation of a solid: a composite of electrons and holes in one spin state, a collective mode named by the symmetry it breaks, or a hybrid of two modes",
        "source": BQ.SOURCE[0], "source_status": "DERIVED",
        "source_note": "nothing is written down as a value: charge adds and spin combines by angular-momentum addition for a composite, a broken generator's rank and commutation fix a collective mode's numbers, and a hybrid inherits what its constituents share; the electron and the photon are read from the fundamental index",
        "coordinates": [{"name": "2J", "meaning": "spin, doubled, computed", "status": "DERIVED"},
                        {"name": "Q3", "meaning": "electric charge in thirds, computed", "status": "DERIVED"}],
        "rules": [{"rule": "composition", "text": "charge adds; spin combines by angular-momentum addition, so a composite is one member per spin state; a hole is the electron with its charge negated"},
                  {"rule": "broken symmetry", "text": "2J is twice the broken generator's rank under rotation and Q3 is zero where the generator commutes with the charge operator; the phonon comes out a vector mode, which the three acoustic branches require"},
                  {"rule": "hybridisation", "text": "a hybrid mixes only modes that agree on every quantum number and inherits the shared value; a disagreement is an error, not a choice"}],
        "members": [{"kind": k, "name": n, "coords": [j, q]} for k, n, j, q in BQ.members()],
        "composites": [{"name": n, "parts": list(pts), "coords": [j, q]} for n, pts, j, q in BQ.rows()],
        "broken": [{"name": n, "breaks": b, "generator": g, "coords": [j, q]} for n, b, g, j, q in BQ.broken_rows()],
        "hybrids": [{"name": n, "parts": list(pts), "coords": [j, q]} for n, pts, j, q in BQ.hybrid_rows()],
        "excluded": [{"name": n, "parts": list(pts), "spins": list(sp), "why": why} for n, pts, sp, why in BQ.excluded()],
        "cells": len(BQ.index()), "cell": {"channel": K, "height": h, "width": w}, "closers": BQ.closers(),
        "relation": {"boson_cells": nb, "qp_cells": nq, "bosons_sublattice": bsub, "qp_sublattice": qsub, "qp_subset_of_bosons": subset,
                     "outside": [list(c) for c in outside], "union_cells": nunion, "union_sublattice": usub,
                     "outside_members": [{"cell": list(c), "members": m} for c, m in BQ.outside()],
                     "note": "the tree's own bosons on (2J, Q3) are already a sublattice; the excitations are a sublattice; they are not a subset; the cells outside are the extension, and the union is still a sublattice", "status": "DERIVED"},
        "channel_note": {"is_chain": BQ.is_chain(), "box": {"subsets": tot, "closing_all": full, "of_this_size": n5, "of_this_size_closing": f5},
                         "text": "the channel is measured over the chart's own box rather than asserted: how many subsets of the box close under every language, and how many of the chart's own size do"},
        "in_progress": True,
    }


def _readrezayi(RR):
    """DOCKET 32 as the site carries it: the non-abelian Hall quasiparticles,
    the Z_k parafermion primaries of the Read-Rezayi series, computed from the
    closed form and validated against the two values the literature fixes."""
    rows = RR.rows()
    K, h, w = RR.cell()
    verdict, why = RR.verdict()
    nA, nN, shared, a_in_n, n_in_a, a_sub, n_sub = RR.nesting()
    return {
        "id": "readrezayi", "title": "The non-abelian Hall quasiparticles: the Read–Rezayi series",
        "member": "a primary field of the Z_k parafermion theory of the Read–Rezayi state at filling ν = 2 + k/(k+2); Moore–Read is k = 2",
        "source": RR.SOURCE[0], "source_status": "PINNED",
        "source_note": "computed from the closed form h = l(l+2)/(4(k+2)) − m²/(4k) with (l, m) identified with (k − l, m − k); exact rationals",
        "reach": RR.REACH, "levels": len(RR.levels()), "members": len(rows), "cells": len(RR.index()),
        "cell": {"channel": K, "height": h, "width": w}, "closers": RR.closers(RR.index()),
        "observed": [{"k": k, "filling": f, "name": n, "nu": _frac(RR.filling(k)), "fundamental_charge": _frac(RR.fundamental_charge(k))} for k, (f, n) in sorted(RR.OBSERVED.items())],
        "coordinates": [{"name": "STAT", "meaning": "0 boson, 1 fermion, 2 anyon, from h mod 1", "status": "DERIVED"},
                        {"name": "ORD", "meaning": "the order of the topological twist: the denominator of h", "status": "DERIVED"},
                        {"name": "CHORD", "meaning": "the order of the quasihole charge", "status": "DERIVED"},
                        {"name": "K", "meaning": "the level, which names the filling fraction ν = 2 + k/(k+2)", "status": "READ"}],
        "rows": [{"k": k, "l": l, "m": m, "h": _frac(hh), "Q": _frac(Q), "coords": [st, o, c, k], "observed": k in RR.OBSERVED} for k, l, m, hh, Q, st, o, c in rows],
        "validation": [{"what": a, "computed": str(b), "expected": str(c), "agrees": d} for a, b, c, d in RR.validation()],
        "sweep": [{"box": a, "cells": b, "channel": c, "closers": d, "degenerate": g} for a, b, c, d, _e, _f, g in RR.sweep()],
        "verdict": verdict, "why": why, "verdict_status": "READ",
        "fermions": [{"k": k, "l": l, "m": m, "h": _frac(hh)} for k, l, m, hh in RR.fermions()],
        "fermions_note": "the abelian index proved that no Laughlin quasiparticle is a fermion; this series has them, the first the Ising ψ at h = 1/2, so that theorem was about the abelian ones",
        "nesting": {"abelian_cells": nA, "nonabelian_cells": nN, "shared": shared, "abelian_in_nonabelian": a_in_n, "nonabelian_in_abelian": n_in_a, "abelian_sublattice": a_sub, "nonabelian_sublattice": n_sub,
                    "note": "on the three coordinates the two Hall indexes share, neither nests in the other and neither is a sublattice: the negative counterpart of the bosonic result", "status": "DERIVED"},
        "in_progress": True,
    }


def _spin4(S4, extra):
    """DOCKET 34 as the site carries it: the ten spin-4 mesons as a seated
    index of their own -- a sub-population of the mesons (2J = 8) charted on
    the three coordinates that vary over it, seated on the table's own status
    as its reach, the tree's only K4. Both readings the instrument prints
    are carried: K5 on the established states alone, K4 once the status-2
    states are admitted."""
    K, h, w = S4.cell()
    moves, ks = S4.channel_moves()
    ec, ek = S4.established_reading()
    f = S4.arity_freeness()
    spins, const = S4.spin_is_constant()
    rows = [{"name": n, "pdgid": pid, "coords": [P, i, q], "extra": dict(extra(pid), pdg_status=s)}
            for n, pid, P, i, q, s in sorted(S4.rows())]
    return {
        "id": "spin4", "title": PARTICLE_TITLES["spin4"],
        "member": "a meson of spin 4 (2J = 8) of the PDG table, a sub-population of the meson index; antiparticles separate",
        "coordinates": PARTICLE_COORDS["spin4"],
        "members": len(rows), "charted": len(rows), "unplaced": [], "unplaced_why": "",
        "cells": len(S4.index()), "cell": {"channel": K, "height": h, "width": w}, "closers": S4.closers(),
        "rows": rows,
        "parent": "mesons", "held_constant": {"coordinate": "2J", "value": spins[0] if spins else None, "constant": const,
                                              "note": "2J is the same for every member, so it carries no information and is not a coordinate here; that is what makes the effective arity 3"},
        "massless": S4.massless(),
        "massless_note": "PDG prints no mass for these; they are charted anyway, because mass is not a coordinate of this index and the meson index already refuses it as one",
        "reach": {"on": "PDG status, the table's own flag for how established a state is, which every row carries",
                  "cuts": [{"status_max": c, "members": n, "cells": x, "channel": k} for c, n, x, k in S4.reach()],
                  "moves": moves, "channels_seen": ks,
                  "established": {"cells": ec, "channel": ek, "note": "on the established states alone (status 0 and 1) the index is K%d; it is K%d only once the status-2 states are admitted -- both readings are true, and the K%d is quoted with its condition" % (ek, K, K)},
                  "why_not_mass": "mass is not total over this member set, so a sweep by mass never reaches the full set and cannot test it; refusing an index because a variable it never claimed fails to order it is not a test of the index",
                  "status": "DERIVED"},
        "arity": {"effective": len(PARTICLE_COORDS["spin4"]), "statistics_at_arity_2": {"closes": f["statistics"][0], "charts": f["statistics"][1]},
                  "note": "at arity 2 statistics closes every chart in the tree, so a K4 there is join-closure and nothing more; at arity 3 it closes 59 of 125, so here the bit is earned -- the first chart of arity 3 or more to reach K4", "status": "DERIVED"},
        "tests": {"box_invariance": "the channel moves with the reach, so the box-invariance test seats it: K4 is a property of the data and not of the construction",
                  "reach_gate": "the overlap rule's reach gate would call a channel arriving at the last cut a late arrival; that gate governs coarsenings of an already-charted member set, and this is a new member set, as the three PDG indexes were",
                  "note": "the two tests disagree here and the disagreement is on the record rather than resolved by picking the convenient one", "status": "READ"},
        "channels": {"all_occupied": True, "note": "with this seating every one of the eight closure channels is carried by some index; that is a statement about eight cells, not about how many indexes there are, and the tree's completeness flag stays False"},
        "verdict": "SEAT", "verdict_status": "READ",
        "refused": [],
    }


def _subpop(SP):
    """DOCKET 33 as the site carries it: the member sub-population sweep --
    one coordinate held to one value over every index with declared
    coordinates -- with its census, its two hits at the last empty channel,
    the recursion determination that corrected itself, and the candidates run
    and not seated, in the instrument's own figures."""
    tested, closed, unocc = SP.census()
    tot, pairs, longest = SP.family_nesting()
    m, c, sub, box = SP.chiral_goldstone()
    n_ew, held = SP.electroweak()
    lat = SP.lattices()
    routes = {
        "IAEA ENSDF API": "closed: the network route this build runs behind refuses it",
        "pypi radioactivedecay": "closed: installs, but carries decay data only -- half-lives, modes, progeny -- and no level energies, no J^P per level, no bandhead K",
        "pypi nucleardata": "closed: no such distribution",
        "the corpus": "closed: nothing in this repository's own inventories names a nuclear level scheme",
        "the paper database": "open: two published data tables carrying level energy E and I^pi per band member, reached through a paper database rather than by direct fetch",
    }
    return {
        "title": "Every member sub-population, swept",
        "status_note": "every earlier sweep varied the columns of a chart; this one varies the members -- one coordinate held to one value, over every index that declares its coordinates -- and asks whether the sub-population is closed and what channel it reaches; nothing is seated by it, and its figures are the instrument's",
        "census": {"tested": tested, "closed_sets": closed, "reaching_an_unoccupied_channel": unocc, "status": "DERIVED",
                   "occupancy_note": "occupancy is measured as it stood before this sweep's own finding was acted on: the spin-4 index it found was then seated at K4, and measured against live occupancy the finding would erase itself"},
        "hits": [{"parent": nm.split(".")[0], "coordinate": col, "value": v, "cells": n, "channel": k, "effective_arity": eff,
                  "verdict": "statistics free at arity 2, refused" if eff <= 2 else "statistics earned at arity 3", "status": "DERIVED"}
                 for nm, col, v, n, k, eff in SP.unoccupied_hits()],
        "spin4_under_mass": {"cuts": [{"mass_max_MeV": a, "cells": b, "channel": k} for a, b, k in SP.spin4_reach()],
                             "massless": SP.spin4_massless(),
                             "note": "under the parent's own reach, mass, the population is K5 at every cut and never K4: the K4 rests on two rows the table gives no mass; it was then seated on a different reach, the table's status, which is total where mass is not -- both statements stand, and which reach a channel survives is part of the finding",
                             "status": "DERIVED"},
        "lattices": {"rows": [{"index": nm, "cells": n, "lattice": isl} for nm, n, isl in lat],
                     "count": sum(1 for _n, _c, l in lat if l), "not": sum(1 for _n, _c, l in lat if l is False), "undetermined": sum(1 for _n, _c, l in lat if l is None),
                     "note": "only these are closed under meet and join, so \"a sublattice of the index\" is well-posed only for them; for the rest the sweep tests closure in the ambient box, which is the right test and had the wrong word attached to it in an earlier reading", "status": "DERIVED"},
        "family": {"closed_sets": tot, "containments": pairs, "longest_chain": longest,
                   "note": "within the sweep's own family; a fact about the family and not about the lattices, as the exhaustive pass below shows", "status": "DERIVED"},
        "recursion": [{"lattice": nm, "cells": n, "chain": ch, "bad_intermediates": bad, "stalls_at": ends, "maximal": maxi,
                       "verdict": "exact -- peels to empty, the longest chain a lattice of this size admits" if maxi else "a verified lower bound; the greedy peel stalls at %d cells" % ends}
                      for nm, n, ch, bad, ends, maxi in SP.recursion()],
        "recursion_note": "each lattice peeled one element at a time with closure tested directly at every step and every intermediate re-checked; a first attempt used a removability shortcut that assumed the containing set was closed, produced a chain with ten intermediates that were not closed, and was discarded",
        "exhaustive": [{"index": nm, "cells": n, "closed_sets": ns, "longest_chain": ch} for nm, n, ns, ch in SP.exhaustive()],
        "exhaustive_note": "every subset of every index small enough to enumerate (at most %d cells): one sixteen-cell chart alone holds more closed sets than the whole family sweep found across the tree" % SP.EXHAUSTIVE_LIMIT,
        "too_large": [{"index": nm, "cells": n} for nm, n in SP.too_large()],
        "too_large_note": "where the true depth is not determined, named rather than implied",
        "candidates": {
            "chiral_goldstone": {"members": m, "cells": c, "sublattice": sub, "full_box": box,
                                 "text": "the pseudoscalar mesons are the pseudo-Goldstone bosons of chiral symmetry breaking, so a rule derives their J^P = 0- rather than reading it; they are a sublattice of the mesons, but a full product box is always closed, so the property is free -- recorded, not seated", "status": "DERIVED"},
            "electroweak": {"cells": n_ew, "held_by_fundamental": held,
                            "text": "the three Goldstones eaten by the W+, W- and Z land on cells the fundamental index already holds: a relabelling of three charted members, refused", "status": "DERIVED"},
            "nuclear_bands": {"routes": [{"route": "this repository's inventories" if r == "the corpus" else r, "state": routes.get(r, w)} for r, w in SP.NUCLEAR_ROUTES],
                              "sources": [{"arxiv": a, "what": w, "bands_or_states": nb, "nuclei": nn, "candidate": cand} for a, w, nb, nn, cand in SP.BAND_SOURCES],
                              "text": "a rotational band is the Goldstone tower of broken rotational symmetry in a deformed nucleus, and its members are nuclear excited states, which need a level scheme; four routes to one were closed, and the fifth opened by changing the operation -- a join over a paper database rather than a meet of two constraints -- and returned two different physical objects, only one of them the candidate; nothing is seated from either, because a total capture must be shown total",
                              "status": "READ"},
        },
        "in_progress": True,
    }


def _nuclear(N, C, D):
    """DOCKET 35 as the site carries it: the nuclear excited states of the
    magnetic and antimagnetic rotational bands as an index on (2I, parity),
    with the capture's own totality argument, its three refusals counted
    apart, the free K2 said rather than banked, and the second paper's
    status (DOCKET 36) beside it."""
    K, h, w = N.cell()
    heads = {(b["table"], b["A"], b["el"], b["band"]): b for b in N.bandrows()}
    rows, seen = [], {}
    for r in N.members():
        A, el, tb, band, E = int(r["A"]), r["el"], r["table"], int(r["band"]), r["E_keV"]
        key = "%d%s-%s-%d-%s" % (A, el, tb, band, E)
        if key in seen:
            seen[key] += 1
            key += "~%d" % seen[key]
        else:
            seen[key] = 0
        hd = heads.get((tb, r["A"], el, r["band"]), {})
        rows.append({"name": "%d%s %s band %d · %s keV" % (A, el, tb, band, E), "key": key,
                     "coords": [int(r["2I"]), int(r["par"])],
                     "extra": {"table": tb, "A": A, "Z": int(r["Z"]), "N": A - int(r["Z"]), "el": el, "band": band, "E_keV": E,
                               "band_levels": int(hd["levels"]) if hd.get("levels") else None, "head_E": hd.get("head_E") or None}})
    nb_nospin, nb_nopar, nb_unplaced = N.refusals()
    reasons = collections.Counter(C.nospin_reason().values())
    steps = C.steps()
    mr = steps.get("MR", {}); amr = steps.get("AMR", {})
    bt = N.by_table()
    arity3 = [{"coordinates": list(c), "channel": k, "cells": n, "cell": {"channel": cl[0], "height": cl[1], "width": cl[2]}} for c, k, n, cl in N.ARITY3]
    cen = C.census()
    index = {
        "id": "nucbands", "title": "The nuclear excited states in rotational bands",
        "member": "a nuclear excited state in a magnetic or antimagnetic rotational band, carrying spin I and parity as a particle carries J and P; the bands themselves are measured as a sub-population and not seated",
        "coordinates": [{"name": "2I", "meaning": "spin, doubled so a half-integer spin stays an integer", "status": "READ"},
                        {"name": "P", "meaning": "parity, +1 or −1", "status": "READ"}],
        "members": len(rows), "charted": len(rows), "levels_captured": len(N.levels()), "unplaced": [], "unplaced_why": "",
        "rows": rows,
        "cells": len(N.index()), "cell": {"channel": K, "height": h, "width": w}, "closers": N.closers(N.index()) if hasattr(N, "closers") else ["statistics"],
        "free_channel": {"arity": N.statistics_is_free()[0], "free": N.statistics_is_free()[1], "status": "DERIVED",
                         "note": "at arity 2 the statistics closer is vacuous, so the K2 is the free one and the index really closes in nothing, which is where the mesons and baryons sit too; said rather than banked"},
        "supersets": {"rows": arity3, "status": "DERIVED", "note": "every superset of (2I, P) over the five coordinates the capture carries loses the channel: the extra coordinate buys cells and costs the free pass; all seven measured, the last on a ninety-minute run after a forty-minute one timed out and was named unmeasured rather than filled in"},
        "refusals": {"bands_no_spin": nb_nospin, "bands_no_spin_reasons": {"energy_unknown": reasons.get("ENERGY-UNKNOWN", 0), "spin_relative": reasons.get("SPIN-RELATIVE", 0)},
                     "levels_no_parity": nb_nopar, "levels_no_spin_in_a_band": nb_unplaced,
                     "unplaced": [{"table": u["table"], "A": int(u["A"]), "el": u["el"], "band": int(u["band"]), "E_keV": u["E_keV"], "Egamma": u["Egamma"], "closes": u["closes"] == "True"} for u in N.unplaced_rows()],
                     "status": "READ",
                     "note": "three refusals on the criterion, counted apart because they are different facts about the source: bands printed with no spin-parity column at all (energies relative to an unknown bandhead, or a relative spin ladder), levels with a spin and no parity, and level rows with no spin-parity inside a band that has them, each of the last closing its own gamma arithmetic against a level below it"},
        "bands": {"cells": len(N.band_chart()), "status": "DERIVED", "note": "the bandhead states as a chart: the same channel, a sub-population of this index, measured and not seated, because seating the tower and its rungs would be two indexes for one subject"},
        "by_table": {k: {"levels": v[0], "cells": v[1], "channel": v[2]} for k, v in bt.items()},
        "by_table_note": "MR is magnetic rotation, the shears mechanism at ΔI = 1; AMR is antimagnetic rotation at ΔI = 2; the two mechanisms charted apart land in the same channel",
        "resolution": [{"axis": a, "distinct": d, "cells": n, "ratio": round(r, 4)} for a, d, n, r in N.resolution()],
        "refused": [],
        "in_progress": True,
    }
    capture = {
        "paper": C.PAPER, "arxiv": "2303.13849", "source_md5": C.SRC_MD5, "source_md5_now": C.md5(C.SRC),
        "census": {"stated": {k: {"bands": v[0], "nuclei": v[1]} for k, v in C.STATED.items()}, "measured": {k: {"bands": v[0], "nuclei": v[1]} for k, v in cen.items()},
                   "exact": all(cen[k] == C.STATED[k] for k in C.STATED), "status": "DERIVED",
                   "note": "the paper's own census, from its abstract and summary, reproduced exactly and independently for its two tables; the parse is measured against it, never fitted to it"},
        "selection_rule": {"MR": {"delta_2I_2": mr.get(2, 0), "steps": sum(mr.values())}, "AMR": {"delta_2I_4": amr.get(4, 0), "steps": sum(amr.values())}, "status": "DERIVED",
                           "note": "a count cannot catch a parser that reads the right number of wrong things, so the second check is the physics each table is defined by: AMR steps at ΔI = 2, MR steps at ΔI = 1"},
        "source_faults": [{"A": a, "el": e, "band": b, "text": w} for a, e, b, w in C.SOURCE_FAULTS],
        "parser_faults": [{"A": a, "el": e, "band": b, "text": w} for a, e, b, w in C.PARSER_FAULTS],
        "not_a_fault": [{"A": a, "el": e, "band": b, "text": w} for a, e, b, w in C.NOT_A_FAULT],
        "faults_note": "faults in the source are captured as printed and not repaired; a fault in the parser, found by audit, is recorded beside them because a capture that only records the source's faults is flattering itself",
        "status": "READ",
    }
    deformed = None
    if D is not None:
        req, blanks, page, hdr, avail = D.separators()
        absent, recovered, why = D.verdict()
        ent, bands, heads_n = D.census2()
        total = (ent, bands, heads_n) == (D.STATED["entries"], D.STATED["bands"], D.STATED["bandheads"])
        closure = None
        if hasattr(D, "docket36_chart"):
            cells36, k36, cell36, n36, nopar36 = D.docket36_chart()
            cand = D.candidate_pool() if hasattr(D, "candidate_pool") else None
            closure = {"dotted_lines": [{"line": k, "text": s.strip()} for k, s in D.dotted_number_lines()] if hasattr(D, "dotted_number_lines") else [],
                       "candidate_pool": {"candidates": cand[0], "chosen": cand[1], "rejected": cand[2]} if cand else None,
                       "prose_figures": D.prose_figures() if hasattr(D, "prose_figures") else None,
                       "chart": {"cells": cells36, "channel": k36, "cell": {"channel": cell36[0], "height": cell36[1], "width": cell36[2]}, "members": n36, "levels_no_parity": nopar36},
                       "note": "the missing entry was a band-number line printed with a trailing full stop, which the sequence rule refused; it is admitted narrowly, a bare integer with a full stop and nothing else on the line, of which exactly one exists in the table, because admitting any dotted number would take the comment column's own numbering too; the capture is then total against three of the paper's own figures, and the third, the bandhead count, was exact before the entry was found, which is what made the search well-posed; the remaining falling spin sequence is one entry the paper prints as one, acquitted by the same four tests; on the same coordinates as the band index these levels give a chart no seated index holds, measured and not seated, because a capture is not an index and seating is a decision of the other session"}
        deformed = {
            "paper": D.PAPER, "arxiv": "2508.05447",
            "stated": dict(D.STATED), "spec": D.SPEC, "spec_is_stated": D.spec_is_stated(),
            "attempts": [{"method": m, "entries": n, "why": w} for m, n, w in D.ATTEMPTS],
            "separators": {"required": req, "blank_lines": blanks, "at_page_breaks": page, "inside_headers": hdr, "available": avail},
            "delimiter_absent": absent, "recovered": recovered, "sections": len(D.sections()),
            "census": {"entries": ent, "bands": bands, "bandheads": heads_n}, "total": total,
            "discontinuities": [{"entry": i, "band_number": no, "drop": [list(d) for d in dr]} for i, no, _sp, dr in D.discontinuities()],
            "verdict": "CAPTURED IN FULL, NOT SEATED" if total else "CAPTURED, NOT SEATED", "why": why, "verdict_status": "READ",
            "closure": closure,
            "note": "the deformed rotor's tower, the candidate the sub-population sweep actually named; the document's own delimiter, a blank row between entries, was collapsed by the text extraction, and an earlier refusal concluded from that that no parse could recover the entries; that conclusion is retracted, a sequence-with-reset rule on the band number recovering 233 of 234 in 24 blocks matching the 24 nuclide sections; two entries carry a falling spin sequence and splitting both would give 235, so the capture stays at 233 and nothing is seated",
        }
    return {"index": index, "capture": capture, "deformed": deformed,
            "status_note": "a candidate the sub-population sweep first declared unreachable, reached by navigating by join rather than by meet: the shears-rotation paper captured in full with its own census reproduced, and its levels seated as an index; the deformed-rotor paper captured and not seated"}


SITE_INDEX_IDS = {"fundamental.index": "fundamental", "mesons.index": "mesons", "baryons.index": "baryons", "spin4.index": "spin4",
                  "nucbands.index": "nucbands", "fqh.index": "fqh", "readrezayi.index": "readrezayi", "bosonqp.index": "bosonqp"}


def _predictions(PR, GH, DM, mods):
    """DOCKETS 38 and 39 as the site carries them: E per seated index, the
    cells each index's own join-closure demands and no member occupies, with
    every demanded cell of the site's own indexes adjudicated into FORBIDDEN,
    UNPLACED or OPEN by the instrument's bounds and source gaps, so the
    explorer can draw them as ghosts beside the members; E carried as the
    upper bound the instrument says it is."""
    import registry as R
    zero_ok, pos_ok, n_zero, n_pos = PR.partition()
    ep = GH.element_precedent()
    laws = [
        {"law": "L1 projection", "text": "the join-closure never invents a coordinate value, so no single-coordinate bound can forbid a demanded cell; measured, none of the demanded baryon cells carries an even 2J"},
        {"law": "L2 max-stability", "text": "a bound whose admissible set is closed under componentwise max forbids nothing"},
        {"law": "L3 monotone vacuity", "text": "a bound of the form x_i ≤ f(x_j) with f non-decreasing is max-closed, so it forbids nothing; every atomic and nuclear bound in the tree has that shape, holds on every member, and forbids nothing, not because nothing was found but because nothing can be"},
        {"law": "L4 what can forbid", "text": "only a bound that is antitone in some coordinate, carries a congruence, or is a non-monotone function of several coordinates; the one such bound here is Gell-Mann–Nishijima on the baryons"},
        {"law": "L5 coordinate expressibility", "text": "a bound on a variable the index does not carry forbids a cell only if no value of that variable satisfies it; the quark model forbids no cell of the meson index, because every (J, P) is realised by some (L, S), and the exotic combinations need C, a coordinate the meson index refused for totality"},
        {"law": "L6 relativity to the operator", "text": "E is a deficit against an operator: the element layout's 36 ghosts are an order deficit while these are join deficits, and on the same 90 cells the join deficit is zero"},
        {"law": "L7 forbidding power is the chart's", "text": "the same bound forbids 25 cells on (period, group) and none on (n, l, k); a chart that can forbid is not thereby a better chart"},
    ]
    bounds = []
    for nm, (label, law, mono, _fn) in GH.BOUNDS.items():
        e, f, u, o, und = GH.TABLE.get(nm, (None, None, None, None, None))
        bounds.append({"index": nm.split(".")[0], "bound": label, "from": law, "monotone": mono, "E": e, "forbidden": f})
    table = [{"index": nm.split(".")[0], "E": v[0], "forbidden": v[1], "unplaced": v[2], "open": v[3], "undecided": v[4],
              "bound": ("none, and the absence is a theorem" if nm in GH.NO_BOUND_BY_THEOREM else ("none derived" if nm in GH.NO_BOUND_DERIVED else GH.BOUNDS[nm][0]) if nm in GH.BOUNDS or nm in GH.NO_BOUND_BY_THEOREM or nm in GH.NO_BOUND_DERIVED else "undecided" if nm in GH.UNDECIDED else "—")}
             for nm, v in sorted(GH.TABLE.items(), key=lambda kv: -kv[1][0])]
    tot = GH.totals()
    gb = GH.gmn_from_quarks("baryon"); gm = GH.gmn_from_quarks("meson")
    before, after = GH.bs2_consequence()
    qq_ok, qq_missing = GH.qqbar_theorem()
    # every demanded cell of the site's own indexes, adjudicated cell by cell with the instrument's
    # own rule, so the explorer can draw them; a source row that pins an UNPLACED cell is named
    by_index = {}
    for nm, sid in SITE_INDEX_IDS.items():
        try:
            X = frozenset(R.index_of(nm))
        except Exception:  # noqa: BLE001 -- an index the registry does not seat in this tree
            continue
        d = sorted(DM.demand(X))
        fn = GH.BOUNDS[nm][3] if nm in GH.BOUNDS else None
        gap = GH.GAPS[nm]() if nm in GH.GAPS else []
        names = _gap_names(nm, mods)
        cells = []
        for c in d:
            if fn and not fn(c):
                b, pins = "FORBIDDEN", []
            else:
                pins = [names.get(tuple(g), None) for g in gap if GH._pins(g, c)]
                b = "UNPLACED" if pins else "OPEN"
            if nm in GH.UNDECIDED and b != "FORBIDDEN":
                b = "UNDECIDED"
            cells.append({"cell": list(c), "bin": b, "pinned_by": sorted({p for p in pins if p})})
        cnt = collections.Counter(x["bin"] for x in cells)
        by_index[sid] = {"E": len(d), "forbidden": cnt.get("FORBIDDEN", 0), "unplaced": cnt.get("UNPLACED", 0), "open": cnt.get("OPEN", 0), "undecided": cnt.get("UNDECIDED", 0),
                         "bound": GH.BOUNDS[nm][0] if nm in GH.BOUNDS else None, "bound_from": GH.BOUNDS[nm][1] if nm in GH.BOUNDS else None,
                         "bound_status": ("theorem: none forbids" if nm in GH.NO_BOUND_BY_THEOREM else "none derived" if nm in GH.NO_BOUND_DERIVED else "derived" if nm in GH.BOUNDS else "none"),
                         "recorded": list(GH.TABLE[nm]) if nm in GH.TABLE else None, "cells": cells, "status": "DERIVED"}
    return {
        "title": "What the indexes predict",
        "status_note": "E is the number of cells an index's own join-closure demands and no member occupies; it is reported as an upper bound on predictions, because a demanded cell is not a prediction until it is adjudicated, and the adjudication is done here with the instrument's own bounds and source gaps",
        "E_by_index": [{"index": nm.split(".")[0], "E": e} for nm, e in sorted(PR.E_BY_INDEX.items(), key=lambda kv: (-kv[1], kv[0]))],
        "too_large": [nm.split(".")[0] for nm in PR.TOO_LARGE],
        "partition": {"zero_close_information": zero_ok, "positive_do_not": pos_ok, "complete": n_zero, "predicting": n_pos, "status": "DERIVED",
                      "note": "every index with E = 0 closes under information and every index with E > 0 does not; near definitional, since E is the join deficit and the information closer is the join closer; the result is the numbers"},
        "total_E": PR.total(),
        "bins": [{"bin": b, "meaning": m} for b, m in PR.BINS],
        "worked_case": {"index": PR.UNPLACED_CASE[0].split(".")[0], "cell": list(PR.UNPLACED_CASE[1]), "text": PR.UNPLACED_CASE[2], "status": "READ"},
        "element_precedent": {"cells": ep[0], "E_join": ep[1], "E_order": ep[2], "order_ghosts_forbidden_by_l_le_n_minus_1": ep[3], "join_ghosts_forbidden": ep[4], "status": "DERIVED",
                              "note": "the element layout's thirty-six ghosts are an order deficit, adjudicated 25 forbidden and 11 deferred; the particle and nuclear E are join deficits, and on the same ninety cells the join deficit is zero, so the precedent transfers the bins and not the numbers"},
        "laws": laws,
        "bounds": bounds,
        "adjudication": {"rows": table, "totals": {"E": tot[0], "forbidden": tot[1], "unplaced": tot[2], "open": tot[3], "undecided": tot[4]}, "status": "DERIVED",
                         "rule": "a demanded cell is UNPLACED when the index's own source holds a row the instrument declined to chart which supplies all but one coordinate and agrees with the cell on every one it supplies; a row missing two coordinates pins nothing",
                         "undecided": {"index": "terms", "why": GH.UNDECIDED["terms.index"]},
                         "refuses": ["to call the OPEN total a count of undiscovered objects: for the indexes with a derived bound it is final against every monotone bound, by theorem; for those with none derived it is open against nothing at all", "to repair the capture fault below", "to read forbidding power as evidence of a better chart"]},
        "gmn": {"identity": "Q = I3 + Y/2 with Y = B + S + C + B' + T, re-derived from the capture's own quark strings",
                "baryons": {"rows": gb[0], "parsed": gb[1], "charge_ok": gb[2], "isospin_ok": gb[3], "identity_ok": gb[4], "faults": [{"name": n, "quarks": q, "I2": i, "T2": tt} for n, q, i, tt in gb[5]]},
                "mesons": {"rows": gm[0], "parsed": gm[1], "charge_ok": gm[2], "isospin_ok": gm[3], "identity_ok": gm[4], "faults": [{"name": n, "quarks": q, "I2": i, "T2": tt} for n, q, i, tt in gm[5]]},
                "fault_note": "the meson isospin leg fails on one state and its antiparticle, whose quark content carries no u or d and so no weight for I = 1/2 while the same content on two other rows carries I = 0 in the same file: a fault in the capture, recorded and not repaired",
                "fault_consequence": {"as_captured": {"cells": before[0], "E": before[1], "cell": list(before[2])}, "with_I_zero": {"cells": after[0], "E": after[1], "cell": list(after[2])}, "note": "measured rather than asserted: the meson index is the same before and after, because both cells are occupied by other members"},
                "quark_model_theorem": {"holds": qq_ok, "missing": [list(m) for m in qq_missing], "text": "every (J, P) with J a non-negative integer is realised by some quark–antiquark (L, S), so the quark model forbids no cell of the meson index; the exotic combinations are exotic in J^PC, and C is not a coordinate here"},
                "status": "DERIVED"},
        "by_index": by_index,
        "in_progress": True,
    }


def _gap_names(nm, mods):
    """{partial source tuple: a name} for the rows an index declined to chart, where the
    instrument's own rows carry one, so an UNPLACED cell can say what pins it."""
    out = {}
    try:
        if nm == "mesons.index":
            for r in mods["mesons"].all_rows():
                if r[3] is None:
                    out[(r[2], None, r[4], r[5])] = r[0]
        elif nm == "baryons.index":
            for r in mods["baryons"].all_rows():
                if r[3] is None:
                    out[(r[2], None) + tuple(r[4:])] = r[0]
        elif nm == "nucbands.index":
            for r in mods["nucbands"].levels():
                if r["2I"] and not r["par"]:
                    out.setdefault((int(r["2I"]), None), "%s%s %s band %s · %s keV" % (r["A"], r["el"], r["table"], r["band"], r["E_keV"]))
    except Exception:  # noqa: BLE001 -- a name is a courtesy, never a requirement
        pass
    return out


def _bonds(B):
    """DOCKET 37 as the site carries it: can a bond be indexed? Three
    readings, three refusals on three different grounds, the decidable
    parts re-derived by the instrument."""
    occ, empty = B.channels_exhausted()
    return {
        "title": "Can a bond be indexed?",
        "question": "an index or indexes of chemical, atomic and particle bonds",
        "status_note": "the question was worth measuring rather than waving off: the indexes chart atomic orbitals, nuclear orbitals, atomic terms, nuclei, particles and quasiparticles and nothing between the atom and the nucleus; the answer is no three times, and the three noes are not the same no",
        "refusals": [{"reading": n, "ground": g, "why": w, "status": "DERIVED"} for n, g, w in B.REFUSALS],
        "molecular": {
            "measured": dict(B.MEASURED), "measured_note": "measured with an electronic-structure package over fifteen diatomics in a scoping pass and recorded, not re-derived, since the instrument is stdlib-only; the figures the refusal turns on are re-derived below",
            "bond_vs_mo": [{"molecule": m, "bond_order": b, "occupied_mos": o, "equal": eq} for m, b, o, eq in B.bond_vs_mo()],
            "no_inversion": list(B.NO_INVERSION),
            "basis": {"molecule": "N2", "counts": [{"basis": b, "mos": c} for b, c in B.N2_MO_BY_BASIS], "distinct": B.basis_spread()[0], "min": B.basis_spread()[1], "max": B.basis_spread()[2]},
            "sigma_v_eigenvalues": B.sigma_v_on_sigma(), "pi2_microstates": sum(B.pi_squared().values()), "sigma_terms_from_pi2": {"triplet": B.sigma_terms_from_pi2()[0], "singlet": B.sigma_terms_from_pi2()[1]},
            "status": "DERIVED",
        },
        "particle": {"partial_waves_J3": B.partial_waves(3), "growth": [{"J_max": j, "channels": len(B.partial_waves(j))} for j in (1, 2, 3, 4)], "status": "DERIVED",
                     "note": "the nucleon-nucleon partial waves are derived from the triangle rule and the Pauli condition alone and are the channels the phase-shift literature prints; they fail twice, labelling the pair's state rather than the binding, and every finite count of them is a potential model's operator basis"},
        "channels": {"occupied": occ, "empty": empty, "status": "DERIVED",
                     "finding": "every one of the eight closure channels is now carried by some index, so the overlap rule's first ground, a channel no index reaches, can never be satisfied again; every future candidate must bring a genuinely new member set, as the nuclear band index did"},
        "in_progress": True,
    }


def _frac(x):
    return "%d/%d" % (x.numerator, x.denominator) if x.denominator != 1 else str(x.numerator)


WARP_COMMIT = None   # the commit the warp tree at --warp-root is at, when the caller knows it
_PBLOCK = {}         # the block once per (root, commit) in a process: the sweep costs a minute


def particle_index_block(root=WARP_ROOT, write=True, out_dir=OUT, commit=None):
    """The three particle indexes and the quasiparticle finding as the site
    carries them: a summary for index.js and the member tables for
    data/particles.js. None when the warp tree is not in the repository."""
    mods = warp_modules(root)
    if mods is None:
        return None, None
    key = (os.path.abspath(root), commit or WARP_COMMIT)
    if key in _PBLOCK:
        summary, full = _PBLOCK[key]
        if write:
            blob = (PARTICLES_PREFIX + json.dumps(public_obj(full), ensure_ascii=False, allow_nan=False) + WRAP_SUFFIX).encode("utf-8")
            with open(os.path.join(out_dir, PARTICLES_JS), "wb") as fh:
                fh.write(blob)
        return summary, full
    F, M, Bn, D27, R, PC = (mods[k] for k in ("fundamental", "mesons", "baryons", "docket27", "registry", "pdgcapture"))
    PS = mods.get("particlesweep")
    Q = mods.get("quasiparticle")
    FQ = mods.get("fqh")
    if commit is None and WARP_COMMIT is None and os.path.abspath(root) == os.path.abspath(WARP_ROOT):
        commit = _git_head()   # the tree is the repository's own, so its commit is the repository's
    cap = {int(r["pdgid"]): r for r in PC.read()}
    src = R.sources()
    header = PC.header()

    def extra(pid):
        r = cap[pid]
        return {"family": r["family"], "quarks": r["quarks"] or None,
                "anti": int(r["anti"]),
                "C": None if r["C"] == "?" else int(r["C"]),
                "G": None if r["G"] == "?" else int(r["G"]),
                "mass_MeV": None if r["mass_MeV"] == "?" else float(r["mass_MeV"]),
                "width_MeV": None if r["width_MeV"] == "?" else float(r["width_MeV"]),
                "status": r["status"], "rank": r["rank"]}

    def refusal(coord, why, measurement, status="DERIVED"):
        return {"coordinate": coord, "verdict": "REFUSED", "why": why,
                "measurement": measurement, "status": status}

    indexes = []
    # --- fundamental --------------------------------------------------------
    rows = [{"name": n, "pdgid": pid, "coords": [j, q, c, g], "extra": extra(pid)}
            for n, pid, j, q, c, g in F.rows()]
    d, n, ratio, verdict = F.mass_is_not_a_label()
    have, lack, lacking = F.mass_is_not_total()
    now, with_L, left = F.what_L_would_do()
    K, h, w = F.cell()
    indexes.append({
        "id": "fundamental", "title": PARTICLE_TITLES["fundamental"],
        "member": "a fundamental particle of the Standard Model; antiparticles are separate members because they carry different quantum numbers",
        "coordinates": PARTICLE_COORDS["fundamental"],
        "members": len(rows), "charted": len(rows), "unplaced": [],
        "cells": len(F.index()), "cell": {"channel": K, "height": h, "width": w},
        "closers": F.closers(),
        "rows": rows,
        "colour_rule": [{"what": a, "dimension": b} for a, b in F.colour_rule()],
        "by_generation": {str(k): v for k, v in F.by_generation().items()},
        "charge_multiplet": {str(k): v for k, v in F.charge_multiplet().items()},
        "collisions": [{"cell": list(k), "members": v} for k, v in F.collisions()],
        "collisions_note": "four cells hold two members: three neutrino/antineutrino pairs, which only lepton number separates, and the photon against the Z, which no additive quantum number separates",
        "refused": [
            refusal("mass", "not total: six of the thirty carry no mass in the table (the neutrinos, for which PDG publishes limits and not values), and a coordinate undefined on a fifth of the membership cannot chart it. The usual refusal, that a near-injective coordinate is a row label, is withdrawn here and the withdrawal measured: CPT doubles every mass",
                    {"distinct": d, "members": n, "ratio": round(ratio, 4), "label_verdict": verdict,
                     "with_mass": have, "without": lack, "without_names": lacking}),
            refusal("lepton number, baryon number", "derivable from the PDG id and not declared before the chart was run; adopting them because the chart collided would be fitted. The price is measured",
                    {"cells_now": now, "cells_with_L": with_L, "still_colliding": left}),
            refusal("weak isospin, hypercharge", "properties of a chiral field, and the table lists particles, not chiral components; charting one T3 against a particle would choose a chirality the data does not name", None, "READ"),
        ],
        "masses": [{"name": a, "mass_MeV": b} for a, b in F.masses()],
    })
    # --- mesons -------------------------------------------------------------
    allm = {p: (C, G, k) for n, p, j, P, i, q, C, G, k in M.all_rows()}
    rows = [{"name": n, "pdgid": pid, "coords": [j, P, i, q], "extra": extra(pid)}
            for n, pid, j, P, i, q in M.rows()]
    unplaced_rows = [{"name": n, "pdgid": pid, "coords": [j, None, i, q], "extra": extra(pid)}
                     for n, pid, j, P, i, q, _c, _g, _k in M.all_rows() if P is None]
    c_ok, c_bad = M.c_is_defined_iff()
    g_ok, g_bad = M.g_is_defined_iff()
    pairs, same, split, qs_same, qs_split = M.conjugation()
    ce_cells, ce_cell, ce_closers = M.ceigen_chart()
    K, h, w = M.cell()
    indexes.append({
        "id": "mesons", "title": PARTICLE_TITLES["mesons"],
        "member": "a meson of the PDG table; antiparticles separate",
        "coordinates": PARTICLE_COORDS["mesons"],
        "members": len(M.all_rows()), "charted": len(rows), "unplaced": M.unplaced(),
        "unplaced_why": "PDG prints no parity for them, so a chart carrying P cannot place them; a gap in the table, not in physics",
        "cells": len(M.index()), "cell": {"channel": K, "height": h, "width": w},
        "closers": M.closers(),
        "rows": rows + unplaced_rows,
        "conjugation": {"pairs": pairs, "collided": same, "split": split,
                        "charges_collided": qs_same, "charges_split": qs_split,
                        "note": "conjugation leaves 2J, P and 2I alone and flips only Q3, so the chart separates a pair if and only if the meson is charged"},
        "refused": [
            refusal("C-parity", "not total, and by a theorem: C is printed for exactly the mesons that are their own antiparticle, with two exceptions, K(L)0 and K(S)0, which are strangeness mixtures and so CP eigenstates rather than C eigenstates",
                    {"printed_iff_self_conjugate": c_ok, "exceptions": [{"name": a, "self_conjugate": b, "has_C": c} for a, b, c in c_bad],
                     "kaon_exceptions": [{"name": a, "quarks": b, "self_conjugate": c, "has_C": d} for a, b, c, d in M.kaon_exceptions()],
                     "without_C": sum(1 for v in allm.values() if v[0] is None), "members": len(allm)}),
            refusal("G-parity", "printed for exactly the flavour-neutral mesons, and most are not flavour-neutral",
                    {"printed_iff_flavour_neutral": g_ok, "exceptions": [{"name": a, "flavour": list(b), "has_G": c} for a, b, c in g_bad],
                     "without_G": sum(1 for v in allm.values() if v[1] is None)}),
            refusal("strangeness (and charm, beauty)", "a quark content that is a mixture carries no readable strangeness, and two members are not strangeness eigenstates at all",
                    {"unparsed": len(M.unparsed()), "unparsed_examples": [{"name": a, "quarks": b} for a, b in M.unparsed()[:12]]}),
            refusal("the I^G(J^PC) chart over the 82 with a C", "computed, not seated: it charts a subset the table itself selects",
                    {"cells": ce_cells, "cell": {"channel": ce_cell[0], "height": ce_cell[1], "width": ce_cell[2]}, "closers": ce_closers}),
        ],
        "case_convention": [{"name": a, "quarks": b, "flavour": list(c) if c else None, "expected": list(dd)} for a, b, c, dd in M.case_convention()],
        "case_note": "in this capture lowercase is the quark and uppercase the antiquark: the proton is uud; pinned against six named states",
    })
    # --- baryons ------------------------------------------------------------
    rows = [{"name": t[0], "pdgid": t[1], "coords": list(t[2:]), "extra": extra(t[1])} for t in Bn.rows()]
    unplaced_rows = [{"name": t[0], "pdgid": t[1], "coords": [t[2], None] + list(t[4:]), "extra": extra(t[1])}
                     for t in Bn.all_rows() if t[3] is None]
    nb, nc, ng = Bn.cg_absent()
    a_ok, a_bad = Bn.baryon_number_is_the_sign()
    pairs, same, split, mech = Bn.conjugation()
    K, h, w = Bn.cell()
    indexes.append({
        "id": "baryons", "title": PARTICLE_TITLES["baryons"],
        "member": "a baryon of the PDG table; antibaryons separate",
        "coordinates": PARTICLE_COORDS["baryons"],
        "members": len(Bn.all_rows()), "charted": len(rows), "unplaced": Bn.unplaced(),
        "unplaced_why": "PDG prints no parity for them; a gap in the table, not in physics",
        "cells": len(Bn.index()), "cell": {"channel": K, "height": h, "width": w},
        "closers": Bn.closers(),
        "rows": rows + unplaced_rows,
        "axis_contributions": [{"dropped": a, "cells": b} for a, b in Bn.axis_contributions()],
        "conjugation": {"pairs": pairs, "collided": same, "split": split,
                        "mechanism": [{"coordinate": a, "under_conjugation": b} for a, b in mech]},
        "refused": [
            refusal("C-parity, G-parity", "the table prints neither for any baryon: eigenvalues of operations under which no baryon is invariant",
                    {"baryons": nb, "with_C": nc, "with_G": ng}),
            refusal("baryon number", "it is the sign of the PDG id, so charting it would relabel; measured from the quark content independently of the id",
                    {"agrees": a_ok, "disagreements": [{"pdgid": a, "quarks": b, "A": c} for a, b, c in a_bad]}),
        ],
    })
    # --- the accounting (docket 27) -----------------------------------------
    total, nuclei, st4, kept = D27.census()
    members, charted, unplaced = D27.charted()
    accounting = {
        "table_total": total, "composite_nuclei": nuclei, "status_4": st4, "kept": kept,
        "members": members, "charted": charted, "unplaced": unplaced,
        "identity": "%d = %d + %d + %d" % (total, nuclei, st4, kept),
        "note": "every one of the kept entries is a member of one of the three indexes; the composite nuclei are the periodic elements and are the subject of the rest of this site; the status-4 entries are the fourth generation and the diquarks, excluded on PDG's own flag",
        "unplaced_list": [{"index": a, "name": b} for a, b in D27.unplaced()],
        **(_antimatter(D27, F) if hasattr(D27, "antimatter") else {}),
        "not_indexed": [
            {"what": "hypothetical particles", "why": "supersymmetric partners, axions, dark-matter candidates: none is in the table as an observed state, and a member must carry measured quantum numbers"},
            {"what": "quasiparticles", "why": "phonons, magnons, excitons, Cooper pairs carry quantum numbers and are not in this table; see the quasiparticle finding"},
            {"what": "the periodic atoms", "why": "the subject of the rest of this site"},
        ],
        "status": "DERIVED",
    }
    # --- quasiparticles (docket 28) -----------------------------------------
    if mods.get("spin4") is not None:
        indexes.append(_spin4(mods["spin4"], extra))
    nuclear = None
    if mods.get("nucbands") is not None and mods.get("nbcapture") is not None:
        nuclear = _nuclear(mods["nucbands"], mods["nbcapture"], mods.get("deformed"))
    elif mods.get("nucbands_error"):
        nuclear = {"absent": True, "note": "the nuclear band instrument did not import: " + mods["nucbands_error"][:200]}
    bonds = _bonds(mods["bonds"]) if mods.get("bonds") is not None else None
    predictions = None
    if mods.get("predict") is not None and mods.get("ghosts") is not None and mods.get("demand") is not None:
        predictions = _predictions(mods["predict"], mods["ghosts"], mods["demand"], mods)
    elif mods.get("ghosts_error") or mods.get("predict_error"):
        predictions = {"absent": True, "note": "the prediction instruments did not import: " + (mods.get("ghosts_error") or mods.get("predict_error"))[:200]}
    subpop = None
    if mods.get("subpop") is not None:
        subpop = _subpop(mods["subpop"])
    elif mods.get("subpop_error"):
        subpop = {"absent": True, "note": "the sub-population sweep did not import: " + mods["subpop_error"][:200]}
    quasi = None
    if Q is not None:
        verdict, why = Q.verdict()
        sg, pg, ac = Q.host_carries_it()
        kinds, distinct = Q.universal_is_almost_nothing()
        anyons = []
        for k in range(1, 5):
            for J in Q.anyons(k):
                hh = Q.spin(J, k)
                anyons.append({"k": k, "J": J, "h": _frac(hh), "h_float": float(hh),
                               "d": round(Q.dim(J, k), 9), "fusion_JxJ": Q.fuse(J, J, k),
                               "coords": list(Q.coords(J, k))})
        quasi = {
            "status_note": "the one gap the particle indexes left open, closed by the other session with two refusals, both measured; carried here as its instrument reports it and marked in progress",
            "in_progress": True,
            "no_table": {"claim": "there is no particle table for quasiparticles, and the reason is structural: what distinguishes one phonon mode from another is the host crystal's symmetry, so the member set would be (material, mode), a materials database",
                         "space_groups": sg, "point_groups": pg, "arithmetic_classes": ac, "status": "READ",
                         "universal": {"kinds": kinds, "distinct_cells": distinct,
                                       "list": [{"kind": a, "spin": b} for a, b in Q.UNIVERSAL]}},
            "anyons": {"claim": "one family is exactly specified with no fetch: the anyons of SU(2)_k, whose topological spin, quantum dimension and fusion follow from k and J in closed form",
                       "coordinates": [{"name": "STAT", "meaning": "0 boson, 1 fermion, 2 anyon, from h mod 1", "status": "DERIVED"},
                                       {"name": "ORD", "meaning": "the order of the topological twist, the denominator of h", "status": "DERIVED"},
                                       {"name": "NSELF", "meaning": "how many distinct outcomes J x J has", "status": "DERIVED"},
                                       {"name": "AB", "meaning": "abelian (d = 1) or not", "status": "DERIVED"}],
                       "rows": anyons, "rows_status": "PINNED",
                       "spot_checks": [{"what": a, "computed": _frac(b) if hasattr(b, "numerator") else b, "expected": _frac(c) if hasattr(c, "numerator") else c} for a, b, c in Q.spot_checks()],
                       "not_ising": Q.NOT_ISING,
                       "sweep": [{"box": a, "cells": b, "channel": c, "closers": d} for a, b, c, d, _e, _f, _g in Q.sweep()],
                       "verdict": verdict, "why": why, "verdict_status": "READ"},
            "reopens": "a materials database of phonon modes over a fixed set of crystals, each mode with its symmetry label and frequency, is a legitimate member set; it needs a real fetch and is named so the door is visibly open",
        }
        if mods.get("bosonqp") is not None:
            quasi["bosons"] = _bosonqp(mods["bosonqp"])
        if mods.get("readrezayi") is not None:
            quasi["nonabelian"] = _readrezayi(mods["readrezayi"])
        if FQ is not None:
            quasi["seated"] = _fqh(FQ)
            quasi["status_note"] = ("the gap the particle indexes left open, closed twice by the other session: first with two measured refusals, "
                                    "then, on re-examination, with a seating of a different object, the quasiparticles of the Laughlin states; "
                                    "both verdicts stay on the record, and the work is still in progress there")
        elif mods.get("fqh_error"):
            quasi["seated"] = {"absent": True, "note": "the Hall quasiparticle instrument did not import: " + mods["fqh_error"][:200]}
    elif mods.get("quasiparticle_error"):
        quasi = {"in_progress": True, "status_note": "the quasiparticle instrument is present but did not import: " + mods["quasiparticle_error"][:200]}
    # --- provenance ---------------------------------------------------------
    srow = src.get("fundamental.index") or {}
    census_line = next((l for l in header if "census" in l), None)
    prov = {
        "citation": "Review of Particle Physics, Particle Data Group, Takahashi et al., Int. J. Mod. Phys. A 41, 2630011 (2026)",
        "doi": "10.1142/S0217751X26300111",
        "via": "the scikit-hep particle package, version 1.0.1; the capture records the md5 of what it read",
        "capture": [{"path": d["path"], "bytes": d["bytes"], "md5": d["md5"], "exists": d["exists"]} for d in srow.get("paths", [])],
        "header": [l.lstrip("# ").strip() for l in header],
        "quantum_numbers_note": "the masses are the 2026 edition's; the quantum numbers the indexes chart reach the package from a 2008 file and a maintainers' extension, and nine spot-checks against canonical values are the instrument's fixtures",
        "tree": {"root": "research/warp-drive", "commit": commit or WARP_COMMIT,
                 "state_commit": _warp_commit(root),
                 "instruments": ["pdgcapture.py", "fundamental.py", "mesons.py", "baryons.py", "docket27.py"] + (["quasiparticle.py"] if Q else [])},
    }
    for extra_mod in ("spin4", "subpop", "nucbands", "nbcapture", "deformed", "bonds", "predict", "ghosts"):
        if mods.get(extra_mod) is not None:
            prov["tree"]["instruments"].append(extra_mod + ".py")
    if nuclear and not nuclear.get("absent"):
        for path in ("captures/NUCBANDS-levels.tsv", "captures/NUCBANDS-bands.tsv", "captures/NUCBANDS-unplaced.tsv", "captures/arxiv-2303.13849.txt"):
            fp = os.path.join(root, path)
            if os.path.isfile(fp):
                with open(fp, "rb") as fh:
                    prov["capture"].append({"path": "research/warp-drive/" + path, "bytes": os.path.getsize(fp), "md5": hashlib.md5(fh.read()).hexdigest(), "exists": True})
    sweep = None
    if PS is not None:
        sweep = _sweep(PS)
        prov["tree"]["instruments"].append("particlesweep.py")
    elif mods.get("particlesweep_error"):
        sweep = {"absent": True, "note": "the particle sweep instrument did not import: " + mods["particlesweep_error"][:200]}
    full = {
        "status_note": "%s indexes of the particles that are not periodic atoms, read from the other session's instruments at build; every member carries its coordinates with their statuses, and every refused coordinate carries the measurement that refuses it" % ("four" if len(indexes) == 4 else "three"),
        "source": prov, "accounting": accounting, "indexes": indexes, "sweep": sweep, "quasiparticles": quasi, "subpop": subpop,
        "nuclear": nuclear, "bonds": bonds, "predictions": predictions,
    }
    blob = (PARTICLES_PREFIX + json.dumps(public_obj(full), ensure_ascii=False, allow_nan=False) + WRAP_SUFFIX).encode("utf-8")
    if write:
        with open(os.path.join(out_dir, PARTICLES_JS), "wb") as fh:
            fh.write(blob)
    summary = {
        "file": "data/" + PARTICLES_JS, "bytes": len(blob), "md5": hashlib.md5(blob).hexdigest(),
        "protocol": "data/particles.js sets window.__mi.particle_index, loaded on demand",
        "status_note": full["status_note"],
        "source": {"citation": prov["citation"], "doi": prov["doi"], "capture": prov["capture"], "tree": prov["tree"]},
        "accounting": {k: accounting[k] for k in ("table_total", "composite_nuclei", "status_4", "kept", "members", "charted", "unplaced", "identity")},
        "indexes": [{k: ix[k] for k in ("id", "title", "members", "charted", "cells", "cell", "closers")}
                    | {"coordinates": [c["name"] for c in ix["coordinates"]], "unplaced": len(ix["unplaced"])}
                    for ix in indexes],
        "quasiparticles": ({"in_progress": True, "verdict": (quasi.get("anyons") or {}).get("verdict"),
                            "seated": ("fqh: %d quasiparticles of %d Laughlin states, %d cells, K%d" % (quasi["seated"]["members"], quasi["seated"]["states"], quasi["seated"]["cells"], quasi["seated"]["cell"]["channel"])
                                       if quasi.get("seated") and not quasi["seated"].get("absent") else None),
                            "bosons": ("bosonqp: %d bosonic excitations, %d cells, K%d" % (len(quasi["bosons"]["members"]), quasi["bosons"]["cells"], quasi["bosons"]["cell"]["channel"]) if quasi.get("bosons") else None),
                            "nonabelian": ("readrezayi: %d primaries of %d levels, %d cells, K%d" % (quasi["nonabelian"]["members"], quasi["nonabelian"]["levels"], quasi["nonabelian"]["cells"], quasi["nonabelian"]["cell"]["channel"]) if quasi.get("nonabelian") else None)} if quasi else None),
        "antimatter": ({"total": accounting["antimatter"]["total"], "of_charted": accounting["antimatter"]["of_charted"]} if "antimatter" in accounting else None),
        "spin4": (next(("spin4: %d spin-4 mesons, %d cells, K%d (K%d on the established states)" % (ix["members"], ix["cells"], ix["cell"]["channel"], ix["reach"]["established"]["channel"])
                        for ix in indexes if ix["id"] == "spin4"), None)),
        "nuclear": ({"members": nuclear["index"]["members"], "cells": nuclear["index"]["cells"], "channel": nuclear["index"]["cell"]["channel"],
                     "refusals": [nuclear["index"]["refusals"][k] for k in ("bands_no_spin", "levels_no_parity", "levels_no_spin_in_a_band")],
                     "census_exact": nuclear["capture"]["census"]["exact"],
                     "deformed": ("%d of %d entries, %s, not seated" % (nuclear["deformed"]["census"]["entries"], nuclear["deformed"]["stated"]["entries"], "total" if nuclear["deformed"].get("total") else "short") if nuclear.get("deformed") else None)}
                    if nuclear and not nuclear.get("absent") else None),
        "bonds": ({"refusals": len(bonds["refusals"]), "empty_channels": bonds["channels"]["empty"]} if bonds else None),
        "predictions": ({"total_E": predictions["total_E"], "predicting": predictions["partition"]["predicting"], "complete": predictions["partition"]["complete"],
                         "totals": predictions["adjudication"]["totals"], "site_ghosts": sum(v["E"] for v in predictions["by_index"].values())}
                        if predictions and not predictions.get("absent") else None),
        "subpop": ({"tested": subpop["census"]["tested"], "closed_sets": subpop["census"]["closed_sets"], "hits": subpop["census"]["reaching_an_unoccupied_channel"],
                    "exhaustive_chains": [e["longest_chain"] for e in subpop["exhaustive"]], "lattices": subpop["lattices"]["count"]} if subpop and not subpop.get("absent") else None),
        "sweep": ({"charts": sweep["charts"], "seated": "%s (%s) at K%d, %d cells" % (sweep["seated"]["parent"], ", ".join(sweep["seated"]["cols"]), sweep["seated"]["channel"], sweep["seated"]["cells"]),
                   "refused": len(sweep["refused"]), "occupied_now": sweep["occupancy"]["now"]} if sweep and not sweep.get("absent") else None),
    }
    _PBLOCK[key] = (summary, full)
    return summary, full


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
            "file": {"LW1-ground.py": "the observed configurations table",
                     "tower-2.py": "the tower"}[member],
            "role": {"LW1-ground.py": "observed ground configurations, "
                                      "Z = 1 to 108 (NIST ASD 5.12)",
                     "tower-2.py": "the tower above Λ₈"}[member],
            "md5_recorded": row["md5"] if row else None,
            "md5_measured": _md5(path) if os.path.exists(path) else None,
        })
    row = _manifest_row("COORDINATES-2_13.csv")
    out.append({
        "file": "COORDINATES-2.13 (csv)",
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
     "the channel equation, final form; its p = 0 branch "
     "carries the RECOVERED collapse ramp C(Z)"),
    ("collapse_C", populate.collapse_C, "tools/populate.py", populate.RECOVERED,
     "C(Z, l), the collapse coordinate, inverted out of COORDINATES-2.13's "
     "computed column; no source states its form"),
    ("pauli_bound", populate.pauli_bound, "tools/populate.py", populate.PINNED,
     "B = min(p, n0 - l - 1), the Pauli bound"),
    ("core_p", populate.core_p, "tools/populate.py", populate.PINNED,
     "p, the core's orbital count at this l, from the observed ground "
     "configuration of the core"),
    ("n0_of", populate.n0_of, "tools/populate.py", populate.RECON,
     "n0, the first entirely unoccupied n at this l; the source names the "
     "term but not the reading, and He I ns settles it"),
    ("lambda_constraints", populate.lambda_constraints, "tools/populate.py",
     populate.PINNED, "the seven constraints on Lambda_8, of four origins"),
    ("caps_needed", populate.caps_needed, "tools/populate.py", populate.PINNED,
     "the caps a Lambda_8 cell needs, read against the standing "
     "(n, e, l, k, f) = (3, 3, 1, 3, 1); the cell it is applied to is the "
     "RECONSTRUCTED ionisation-ladder mapping and carries its own status"),
    ("within_caps", populate.within_caps, "tools/populate.py", populate.PINNED,
     "the standing caps; a cell outside them is reported OUTSIDE, "
     "never truncated"),
    ("op_order", cypher.op_order, "tools/cypher.py", cypher.PINNED,
     "R, the order operator: a cell is admitted when every cell below it on "
     "every axis is held"),
]


PUBLIC_AXIS_SOURCES = {
    "symbol": "NIST ASD 5.12, through the observed configurations table",
    "capacity": "2(2l+1), Pauli exclusion",
    "n+l": "the Madelung/Janet coordinate",
    "period": "the drawn eighteen-column layout",
    "p": "the core's orbital count at this l, from the Pauli bound's definition",
    "B": "min(p, n0-l-1), the Pauli bound",
    "delta equation": "the channel equation, final form",
    "C(Z)": "the collapse coordinate, inverted out of COORDINATES-2.13's computed column; see collapse_C",
    "caps": "the standing caps (n,e,l,k,f) = (3,3,1,3,1)",
    "series limit": "the measured ionisation limit, read as printed or fitted from the series, never computed; none where not held",
}


def instruments():
    """Verbatim source of every instrument the browser-side solvers mirror,
    via inspect.getsource, so the page can show the Python beside its own
    result and a reader can diff the two."""
    out = {}
    for name, fn, rel, status, source in INSTRUMENTS:
        lines, start = inspect.getsourcelines(fn)
        out[name] = {"python": redact_source("".join(lines)), "file": rel, "line": start,
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
                    "rows; the equation's published fit (rms 0.1610, R2 0.9741) was "
                    "made on a different sample of 284 channels, so the figures are "
                    "not expected to match it exactly"}


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


def l_by_group(g):
    """Transitions.md L368 (READ): l is fully determined by group -- s at 1-2,
    d at 3-12, p at 13-18 -- and non-monotone in g, which is why no envelope
    over (period, group) can refuse the thirty-six."""
    return 0 if g <= 2 else (2 if g <= 12 else 1)


def denied_cell_definitions(denied):
    """Section 6.1.1 names every one of the thirty-six (The_Method_1_6-2.md
    L1555-1570, ruled by Register 448): each is a subshell of the row it sits
    in, read off the group's l, and the hydrogenic bound l <= n-1 (section 7.1)
    splits them -- 1d (10), 1p (5) and 2d (10) forbidden, 25; 3d (10) real but
    deferred by the Madelung order, and period 1 group 2, the slot helium
    vacates, deferred rather than forbidden because l = 0 satisfies the bound
    there, 11. The class is DERIVED from the PINNED bound; the totals are READ
    and the selftest asserts the derivation reproduces them."""
    out = []
    for p, g in denied:
        n, l = p, l_by_group(g)
        letter = "spdf"[l]
        if l > n - 1:
            cls = "forbidden"
            sub = "%d%s" % (n, letter)
            reason = ("forbidden by l <= n-1, the hydrogenic radial solution: "
                      "a %d%s orbital cannot exist" % (n, letter))
        elif (p, g) == (1, 2):
            cls = "deferred"
            sub = "1s, the slot helium vacates"
            reason = ("deferred, not forbidden: l = 0 satisfies l <= n-1 here; "
                      "helium is drawn at group 18, and 1p contributes five "
                      "cells rather than six because of it")
        else:
            cls = "deferred"
            sub = "%d%s" % (n, letter)
            reason = ("real but deferred by the Madelung order: %d%s fills "
                      "after %ds and is drawn in period %d" % (n, letter, n + 1, n + 1))
        out.append({"p": p, "g": g, "n": n, "l": l, "subshell": sub,
                    "class": cls, "reason": reason})
    return out


def helium_placement():
    """Register 448 (READ): E is placement-sensitive -- 36 with helium at
    group 18, 20 with helium at group 2, because phi(group | period <= 1)
    drops from 18 to 2 and the whole first row of gaps disappears; E prices
    the choice at sixteen cells. Both closures are computed here with
    cypher's own R over the ninety cells, helium moved and nothing else."""
    held, admitted = populate.layout_closure()
    if (1, 18) not in held:
        raise RuntimeError("helium is not at (1, 18) in the drawn layout")
    alt = sorted((held - {(1, 18)}) | {(1, 2)})
    h2, a2, _box = _decoded_closure("periodic table, helium at group 2",
                                    ["period", "group"], alt)
    return {
        "status": populate.READ,
        "source": "the author's standing rule on helium's placement",
        "helium_at_18": {"held": len(held), "admitted": len(admitted),
                         "E": len(admitted) - len(held),
                         "denied": [list(c) for c in sorted(admitted - held)]},
        "helium_at_2": {"held": len(h2), "admitted": len(a2),
                        "E": len(a2) - len(h2),
                        "denied": [list(c) for c in sorted(a2 - h2)]},
        "priced": (len(admitted) - len(held)) - (len(a2) - len(h2)),
        "note": "IUPAC draws helium at 18, the left-step and quantum-chemical "
                "case at 2; E prices the choice at sixteen cells, a number that "
                "argument does not have",
    }


def lattice_block(spectra):
    """Lambda_spectra as the record draws it -- Index of Indices Figure 6: element
    across, l into the page, ionisation stage up -- carried compactly for the site's
    whole-index 3-D view. The slab of every element is charge 1..Z by l 0..7 (the
    selftest asserts 58,080 sites = 8 * sum Z), so only the known cells travel:
    every measured or exact row as [Z, charge, l, mult, grade], grade 1 measured
    and 2 exact. The axes are READ from the record's own caption; the drawing is
    DERIVED from the same rows the plane draws, and nothing is computed."""
    known = sorted(([int(r["Z"]), int(r["charge"]), int(r["l"]), int(r["mult"]),
                     1 if r["grade"] == "measured" else 2]
                    for r in spectra.rows if r["grade"] in ("measured", "exact")))
    sites = {(int(r["Z"]), int(r["charge"]), int(r["l"])) for r in spectra.rows}
    zs = sorted({int(r["Z"]) for r in spectra.rows})
    return {
        "index": "Lambda_spectra as a lattice: element across, l into the page, "
                 "ionisation stage up",
        "axes": {"x": "Z, the element", "y": "charge, the ionisation stage (1 is neutral)",
                 "z": "l, the channel (0 to 7: s p d f g h i k)"},
        "status": populate.READ,
        "source": "the author's own three-dimensional drawing of the index (element "
                  "across, l into the page, ionisation stage up; the Löwdin paper's "
                  "Figure 1(b) draws the same solid), whose renderer used cubes of "
                  "edge 0.86 for a known cell and 0.30 for an unmeasured one",
        "drawing": populate.DERIVED,
        "slab": "every element's slab is charge 1..Z by l 0..7; a site holds one cell "
                "per multiplicity, side by side",
        "sites": len(sites),
        "Z_max": zs[-1],
        "known": known,
        "counts": {"measured": sum(1 for k in known if k[4] == 1),
                   "exact": sum(1 for k in known if k[4] == 2),
                   "known_sites": len({(k[0], k[1], k[2]) for k in known})},
        "cube": {"known": 0.86, "faint": 0.30,
                 "note": "the archived renderer's own edge lengths; a known cell is a "
                         "full cube, an unmeasured one a faint small cube"},
    }


# ---------------------------------------------------------------------------
# particles -- what the corpus itself says of the binders and particles beyond the
# electron, every value parsed out of the passage that states it, never typed here
# ---------------------------------------------------------------------------

MEMBERS = os.path.join(REPO, "method", "members")
PAPERS = os.path.join(REPO, "papers")
MUCF_PY = os.path.join(TOOLS, "mucf.py")
COLLECTOR_PY = os.path.join(TOOLS, "collector.py")
PROSE_ONLY = os.path.join(REPO, "PROSE-ONLY.tsv")


def _lines(rel):
    with open(os.path.join(REPO, rel), encoding="utf-8") as fh:
        return fh.read().splitlines()


def _find(rel, pattern, flags=0):
    """The first passage of `rel` matching `pattern`: (line number, match, text).
    The file is searched flowed -- line breaks read as spaces, so a sentence the
    member wraps still matches -- and the line reported is the one the match
    starts on; the text is that line and the next where the match runs on. A
    passage the corpus no longer states is a build failure, not a silent
    default."""
    lines = _lines(rel)
    text = "\n".join(lines)
    m = re.compile(pattern, flags | re.MULTILINE).search(text)
    if m:
        line = text.count("\n", 0, m.start()) + 1
        end_line = text.count("\n", 0, m.end()) + 1
        return line, m, " ".join(ln.strip() for ln in lines[line - 1:end_line])
    # flowed: each line stripped of its indent and joined by one space, with the
    # offset at which each line starts so the match maps back to a line number
    starts, parts, pos = [], [], 0
    for ln in lines:
        t = ln.strip()
        starts.append(pos)
        parts.append(t)
        pos += len(t) + 1
    flowed = " ".join(parts)
    m = re.compile(pattern, flags).search(flowed)
    if not m:
        raise RuntimeError("%s: no passage matches %r" % (rel, pattern))
    line = bisect.bisect_right(starts, m.start())
    end_line = bisect.bisect_right(starts, max(m.start(), m.end() - 1))
    return line, m, " ".join(parts[line - 1:end_line])


def _plain(text):
    """A passage as prose: the members' markdown emphasis, blockquote marks and
    list numbers dropped, the words untouched."""
    t = re.sub(r"\*\*(.+?)\*\*", r"\1", text)
    t = re.sub(r"(?<![\w*])\*(?!\s)(.+?)(?<!\s)\*(?![\w*])", r"\1", t)
    t = re.sub(r"^(?:>\s*)+", "", t)
    t = re.sub(r"^\d+\.\s+", "", t)
    return t.replace("**", "").strip()


def _site(rel, line, quote=None):
    d = {"file": rel, "line": line}
    if quote is not None:
        q = _plain(quote)
        d["quote"] = q if len(q) <= 600 else q[:597] + "..."
    return d


def _tool_module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def _mucf_status_table():
    """mucf.py's own header table 'INPUTS AND THEIR STATUS -- never flattened',
    read out of the file: name, value, status, note."""
    out = []
    rx = re.compile(r"^\s{4}(\w+)?\s*=?\s*(.+?)\s{2,}(MEASURED|PINNED|PROJECTED|EXTRAPOLATED|PROSE-ONLY)\s+(.*)$")
    name = None
    for ln in _lines("tools/mucf.py"):
        m = rx.match(ln)
        if not m:
            continue
        if m.group(1):
            name = m.group(1)
        out.append({"name": name, "value": m.group(2).strip(), "status": m.group(3),
                    "note": m.group(4).strip()})
    if len(out) < 10:
        raise RuntimeError("mucf.py: the status table was not found (%d rows)" % len(out))
    return out


def _prose_only(ids):
    out = []
    with open(PROSE_ONLY, encoding="utf-8", newline="") as fh:
        for r in csv.DictReader(fh, delimiter="\t"):
            if r["id"] in ids:
                q = _plain(r["quote"].strip())
                out.append({"id": r["id"], "category": r["category"], "label": r["label"],
                            "quote": q if len(q) <= 700 else q[:697] + "...",
                            "confidence": r["confidence"], "status": "PROSE-ONLY"})
    found = {r["id"] for r in out}
    missing = [i for i in ids if i not in found]
    if missing:
        raise RuntimeError("PROSE-ONLY.tsv: rows missing: %s" % ", ".join(missing))
    order = {i: k for k, i in enumerate(ids)}
    return sorted(out, key=lambda r: order[r["id"]])


def _absent_terms(terms):
    """Which particle names occur nowhere in method/members or papers/ -- the
    corpus, not the repository's own documentation of this site, which names
    the absences -- counted at build (DERIVED), so 'absent' is measured and
    never assumed."""
    files = []
    for d in (MEMBERS, PAPERS):
        files += [os.path.join(d, f) for f in sorted(os.listdir(d)) if f.endswith(".md")]
    out = {}
    for t in terms:
        rx = re.compile(r"\b" + re.escape(t) + r"s?\b", re.IGNORECASE)
        n, first = 0, None
        for f in files:
            with open(f, encoding="utf-8") as fh:
                for i, ln in enumerate(fh, 1):
                    if rx.search(ln):
                        n += 1
                        if first is None:
                            first = _site(os.path.relpath(f, REPO), i, ln.strip()[:200])
        out[t] = {"occurrences": n, "first": first}
    return out


def particles_block():
    paper = "papers/Muon_Catalysed_Fusion_v1.1.md"
    main = "method/members/The_Method_1_6-2.md"
    reg = "method/members/The_Method_1_6___The_Register-2.md"
    mc = "method/members/The_Method_1_6___Mathematical_Compendium-2.md"
    pc = "method/members/The_Method_1_6___The_Physics_Compendium-2.md"
    partk = "recovered/structural-results.md"
    ch14f = "recovered/READ-ch14f.md"

    # -- the muon paper: the window, its occupants, the exclusions, the frame
    ln_w, m_w, q_w = _find(paper, r"The structural window is \[(\d+), (\d+)\] mₑ")
    window = [int(m_w.group(1)), int(m_w.group(2))]
    ln_o, m_o, q_o = _find(paper, r"the muon \((\d+) mₑ\) and the pion \((\d+) mₑ\)")
    ln_i, m_i, q_i = _find(paper, r"interior to the window by ([\d.]+)× and ([\d.]+)×")
    ln_mb, _, q_mb = _find(paper, r"occupies \*\*the same cell\*\* as its electronic twin")
    ln_fr, _, q_fr = _find(paper, r"The lattice supplies the frame; it does not supply")
    ln_b, _, q_b = _find(paper, r"\*\*A binder\*\* — negatively charged, leptonic")
    ln_st, _, q_st = _find(paper, r"It is not a member of either live bundle")
    ln_re, _, q_re = _find(paper, r"\*\*Reclassified in v1\.1:\*\* E_μ = 5 GeV per muon")
    ln_ex, _, _ = _find(paper, r"^## 6\. What the definition excludes")
    excl = []
    for i, ln in enumerate(_lines(paper)[ln_ex:], ln_ex + 1):
        m = re.match(r"^\| (.+?) \| (.+?) \|$", ln)
        if m and not m.group(1).startswith("excluded") and not m.group(1).startswith("---"):
            excl.append({"excluded": m.group(1).replace("**", ""), "grounds": m.group(2).replace("**", ""), "line": i})
        elif excl and not ln.startswith("|"):
            break
    if len(excl) < 8:
        raise RuntimeError("%s: the exclusion table was not parsed (%d rows)" % (paper, len(excl)))

    # -- the main volume: the bracket with one occupant, the antiprotonic-helium cell
    ln_n, m_n, q_n = _find(main, r"Recomputed here: N_states of ([\d.]+), ([\d.]+) and ([\d.]+) for electron, muon and tau")
    ln_br, _, q_br = _find(main, r"\*\*A bracket with one occupant is a derivation\.\*\*")
    ln_ah, m_ah, q_ah = _find(main, r"Antiprotonic helium, cell \((\d+),(\d+)\):")
    ln_r1, m_r1, _ = _find(main, r"\| measured directly \| ([\d,]+\.\d) ± ([\d.]+) MHz \|")
    ln_r2, m_r2, _ = _find(main, r"\| two-photon minus a different single-photon \| ([\d,]+\.\d) ± ([\d.]+) MHz \|")
    ln_ag, m_ag, q_ag = _find(main, r"\*\*Agreement at ([\d.]+)σ, with no shared measurement\.\*\*")

    # -- the register: the dimensional obstruction
    ln_do, _, q_do = _find(reg, r"THE DIMENSIONAL OBSTRUCTION: THE LATTICE PRODUCES PURE NUMBERS")
    q_do = q_do.split("Deuteron")[0].strip()

    # -- the photon: the one cell R restores, and the claim that is false
    ln_ph, _, ln_text = _find(mc, r"the photon's unit of angular momentum")
    q_ph = re.search(r"The defect is E = 1.*?the photon's odd parity\.", ln_text).group(0)
    ln_ph2, _, ln_text2 = _find(mc, r"the claim is false")
    q_ph2 = re.search(r"[^.]*the claim is false[^.]*\.", ln_text2).group(0).strip()

    # -- the constants register, Lambda_phys: every heading of the form '### name -- `value`'
    consts = []
    for i, ln in enumerate(_lines(pc), 1):
        m = re.match(r"^### (.+?) — `(.+?)`(.*)$", ln)
        if m:
            consts.append({"name": m.group(1).strip(), "value": m.group(2).strip(),
                           "note": m.group(3).strip(" ,"), "line": i,
                           "withdrawn": "WITHDRAWN" in m.group(3)})
    if len(consts) != 27:
        raise RuntimeError("%s: expected 27 constants, parsed %d" % (pc, len(consts)))

    # -- PART K, antimatter and exotic atoms (recovered, unbundled)
    ln_cpt, _, q_cpt = _find(partk, r"\*\*Λ is CPT-invariant\.\*\*")
    ln_alpha, m_alpha, _ = _find(partk, r"ALPHA measures antihydrogen 1S–2S agreeing with\s*$|agreeing with")
    q_alpha_ln = _find(partk, r"hydrogen at (2 × 10⁻¹²)")
    ln_rm, _, q_rm = _find(partk, r"\*\*The real second axis is reduced mass\*\*")
    exotic = []
    for i, ln in enumerate(_lines(partk), 1):
        m = re.match(r"^\| (positronium|hydrogen, antihydrogen|muonic hydrogen|antiprotonic helium) \| ([\d.,]+) \| ([\d.]+) \|$", ln)
        if m:
            exotic.append({"system": m.group(1), "mu_over_me": float(m.group(2).replace(",", "")),
                           "radius_A": float(m.group(3)), "line": i})
    if len(exotic) != 4:
        raise RuntimeError("%s: expected the four exotic systems, parsed %d" % (partk, len(exotic)))
    ln_ab, _, q_ab = _find(partk, r"\*\*Antiprotonic helium is the only antimatter system with")
    ln_nb, _, q_nb = _find(partk, r"\*\*The bracket cannot help antihydrogen\.\*\*")

    # -- the muon mass, pinned nowhere but in a numbered fault
    ln_pdg, m_pdg, q_pdg = _find(ch14f, r"muon (206\.7683) \(PDG\)")
    ln_f, _, q_f = _find(ch14f, r"internal-closure failure, not a wrong value")

    # -- the instruments
    mucf = _tool_module("mucf", MUCF_PY)
    coll = _tool_module("collector", COLLECTOR_PY)
    status_table = _mucf_status_table()
    sticking = {k: {"omega_s": v[0], "status": v[1]} for k, v in mucf.STICKING.items()}
    mucf_consts = {
        "lambda_0": mucf.LAMBDA_0, "lambda_c": mucf.LAMBDA_C, "transfer": list(mucf.TRANSFER),
        "Q_fus_MeV": mucf.Q_FUS_MEV, "E_mu_achieved_GeV": mucf.E_MU_ACHIEVED,
        "E_mu_floor_GeV": mucf.E_MU_FLOOR, "E_mu_delivered_TeV": mucf.E_MU_DELIVERED_TEV,
        "collection_factor": mucf.COLLECTION_FACTOR, "f_work": mucf.F_WORK,
        "f_alpha": mucf.F_ALPHA, "carnot_800": mucf.CARNOT_800,
        "phi_measured_max": mucf.PHI_MEASURED_MAX, "omega_measured_min": mucf.OMEGA_MEASURED_MIN,
        "sticking": sticking, "reservation_j1": mucf.RESERVATION_J1,
    }
    fixtures = {"table_5_1": [{"omega_s": w, "Q": list(row)} for w, row in mucf.TABLE_5_1.items()],
                "phis": [1.2, 2.0, 3.0], "E_mu": 5.0,
                "breakeven_5_1": [{"phi": p, "omega_s": w} for p, w in mucf.BREAKEVEN_5_1.items()],
                "note": "the paper's own Table 5.1 and section 5.1 thresholds, read from tools/mucf.py "
                        "whose selftest asserts them; the 0.234 % row is a recorded divergence (the "
                        "row is computed at the transfer rate 2.7e8 rather than the pinned saturation "
                        "2.6e8) and is NOTED, not repaired"}
    collector = {
        "status": "SOURCED",
        "source": "tools/collector.py; papers/Muon_Collection_Budget_v1.0.md",
        "MuSIC_mu_minus_per_W": [coll.MUSIC_MU_MINUS_PER_W, coll.MUSIC_MU_MINUS_ERR],
        "MuSIC_all_mu_per_W": coll.MUSIC_ALL_MU_PER_W,
        "MuSIC_proton_GeV": coll.MUSIC_PROTON_GEV,
        "Mu2e_stopped_per_p": coll.MU2E_STOPPED_PER_P,
        "COMET_captured_per_p": [coll.COMET_CAPTURED_LO, coll.COMET_CAPTURED_HI],
        "pion_threshold_GeV": coll.PION_THRESHOLD_GEV,
        "paper_assumed_GeV": coll.PAPER_ASSUMED_GEV,
        "work_breakeven_GeV": coll.WORK_BREAKEVEN_GEV,
        "heat_breakeven_GeV": coll.HEAT_BREAKEVEN_GEV,
        "arxiv": {"MuSIC": "1610.07850", "Mu2e": "1211.7019", "COMET": "1812.09018"},
    }
    for key, aid in collector["arxiv"].items():
        _find("papers/Muon_Collection_Budget_v1.0.md", r"arXiv:" + re.escape(aid))

    prose = _prose_only(["PO-0896", "PO-0893", "PO-0415", "PO-0341", "PO-0897", "PO-0898",
                         "PO-0411", "PO-0412", "PO-0279", "PO-0682"])
    absent = _absent_terms(["neutrino", "gluon", "Higgs", "muonium", "protonium", "kaon", "positronium"])

    return {
        "status_note": "every figure below is READ from the passage that states it, parsed at build; "
                       "an instrument's figures carry the instrument's own status vocabulary "
                       "(MEASURED / PINNED / PROJECTED / EXTRAPOLATED / PROSE-ONLY, and REFUSED below "
                       "the kinematic floor); a PROSE-ONLY row is held in the chat export and in no "
                       "file; ABSENT is counted, not assumed. Nothing here is a lattice figure: the "
                       "lattice carries configuration, not scale.",
        "scope": [
            {"name": "the lattice carries no scale", "status": populate.READ,
             "site": _site(paper, ln_mb, q_mb)},
            {"name": "the lattice supplies the frame, not the rates", "status": populate.READ,
             "site": _site(paper, ln_fr, q_fr)},
            {"name": "the dimensional obstruction", "status": populate.READ,
             "site": _site(reg, ln_do, q_do)},
            {"name": "the paper is not a member of either bundle (docket C-8 open)", "status": populate.READ,
             "site": _site(paper, ln_st, q_st)},
        ],
        "window": {"m_e": window, "status": populate.READ, "site": _site(paper, ln_w, q_w),
                   "occupants": {"muon": int(m_o.group(1)), "pion": int(m_o.group(2)), "site": _site(paper, ln_o, q_o)},
                   "interior": {"below": float(m_i.group(1)), "above": float(m_i.group(2)), "site": _site(paper, ln_i, q_i)},
                   "N_states": {"electron": float(m_n.group(1)), "muon": float(m_n.group(2)), "tau": float(m_n.group(3)),
                                "status": populate.READ, "site": _site(main, ln_n, q_n)},
                   "bracket": _site(main, ln_br, q_br)},
        "binder": _site(paper, ln_b, q_b),
        "exclusions": {"status": populate.READ, "file": paper, "rows": excl},
        "muon": {
            "mass_m_e": {"printed": int(m_o.group(1)), "PDG": float(m_pdg.group(1)), "status": populate.READ,
                         "site": _site(ch14f, ln_pdg, q_pdg), "fault": "14f-04",
                         "fault_note": _site(ch14f, ln_f, q_f)},
            "instrument": {"file": "tools/mucf.py", "status_table": status_table,
                           "constants": mucf_consts, "fixtures": fixtures,
                           "reclassified": _site(paper, ln_re, q_re)},
            "collection": collector,
        },
        "antimatter": {
            "status": populate.RECOVERED,
            "note": "PART K of recovered/structural-results.md -- recovered from the chat export, "
                    "not a member of either bundle, with no instrument",
            "cpt": _site(partk, ln_cpt, q_cpt),
            "alpha": {"value": q_alpha_ln[1].group(1), "site": _site(partk, q_alpha_ln[0], q_alpha_ln[2])},
            "reduced_mass": {"site": _site(partk, ln_rm, q_rm), "systems": exotic},
            "antihydrogen": _site(partk, ln_nb, q_nb),
            "antiprotonic_only": _site(partk, ln_ab, q_ab),
        },
        "antiprotonic_helium": {
            "status": populate.READ,
            "cell": [int(m_ah.group(1)), int(m_ah.group(2))], "site": _site(main, ln_ah, q_ah),
            "routes": [{"route": "measured directly", "MHz": m_r1.group(1), "pm": float(m_r1.group(2)), "line": ln_r1},
                       {"route": "two-photon minus a different single-photon", "MHz": m_r2.group(1), "pm": float(m_r2.group(2)), "line": ln_r2}],
            "agreement_sigma": float(m_ag.group(1)), "agreement_site": _site(main, ln_ag, q_ag),
            "scope": "PO-0279: enters as a scope statement, not as cells",
        },
        "photon": {"status": populate.READ, "E": 1,
                   "site": _site(mc, ln_ph, q_ph), "claim": _site(mc, ln_ph2, q_ph2)},
        "constants": {"status": populate.PINNED, "file": pc, "count": len(consts), "rows": consts,
                      "note": "Lambda_phys, the 27 declared parameters of the Physics Compendium, each "
                              "with kind, value, domain and provenance in the record; one is WITHDRAWN "
                              "and stays listed as such"},
        "prose_only": prose,
        "absent": {"status": populate.DERIVED, "terms": absent,
                   "note": "occurrences counted over method/members and papers/ at build; a "
                           "term with none is absent from the corpus, not a cell of it"},
    }


MUCF_INSTRUMENTS = [
    ("mucf_cycles", "cycles", "N, catalytic cycles per muon (paper section 5.1)"),
    ("mucf_gain", "gain", "Q, raw energy out over muon production cost in"),
    ("mucf_e_mu_for", "e_mu_for", "the muon production cost at which Q reaches a target, GeV"),
    ("mucf_e_mu_for_work", "e_mu_for_work", "E_mu at which WORK out reaches the target; only f_work of the fusion heat is convertible"),
    ("mucf_status_of", "status_of", "the weakest status among the inputs, with the reason; REFUSED below the kinematic floor"),
    ("mucf_band", "band", "Q across the transfer-rate uncertainty"),
    ("mucf_muons_for", "muons_for", "the muon rate a fusion power needs"),
]


def mucf_instruments():
    mod = _tool_module("mucf", MUCF_PY)
    out = {}
    for name, fn_name, source in MUCF_INSTRUMENTS:
        lines, start = inspect.getsourcelines(getattr(mod, fn_name))
        out[name] = {"python": redact_source("".join(lines)), "file": "tools/mucf.py", "line": start,
                     "status": populate.PINNED,
                     "source": source + " -- the paper's own model, computed for it (PINNED); "
                                        "each result carries the weakest status of its inputs in "
                                        "mucf.py's vocabulary: MEASURED, PINNED, PROJECTED, "
                                        "EXTRAPOLATED, PROSE-ONLY, and REFUSED below the floor"}
    return out


# ---------------------------------------------------------------------------
# references -- every outward identifier the corpus prints, with the line that cites it
# ---------------------------------------------------------------------------

ARXIV_NEW = re.compile(r"arXiv[: ]?(\d{4}\.\d{4,5})(?:v\d+)?", re.IGNORECASE)
ARXIV_OLD = re.compile(r"\b((?:hep-th|hep-ph|hep-ex|hep-lat|math-ph|alg-geom|physics|quant-ph|cond-mat|astro-ph|nucl-th|nucl-ex|gr-qc|math|cs)(?:\.[A-Za-z]{2})?/\d{7})\b")
DOI_RX = re.compile(r"\b(10\.\d{4,9}/[^\s\"'<>,;)\]]+)")
URL_RX = re.compile(r"https?://[^\s)\]>\"']+")


def references_block():
    files = []
    for d, tag in ((MEMBERS, "method/members"), (PAPERS, "papers")):
        files += [(os.path.join(d, f), tag + "/" + f) for f in sorted(os.listdir(d)) if f.endswith(".md")]
    arxiv, doi, urls = {}, {}, {}

    def add(store, key, rel, i, ln):
        # the identifier is public; the line that cites it is quoted only
        # from a paper the author has released to the site
        e = store.setdefault(key, {"id": key, "cites": []})
        e["n"] = e.get("n", 0) + 1
        paper = PUBLIC_PAPERS.get(os.path.basename(rel))
        if paper is None:
            return
        text = _plain(ln.strip())
        if len(text) > 320:
            text = text[:317] + "..."
        if len(e["cites"]) < 6:
            e["cites"].append({"paper": paper, "text": text})

    for path, rel in files:
        with open(path, encoding="utf-8") as fh:
            for i, ln in enumerate(fh, 1):
                for m in ARXIV_NEW.finditer(ln):
                    add(arxiv, m.group(1), rel, i, ln)
                for m in ARXIV_OLD.finditer(ln):
                    add(arxiv, m.group(1), rel, i, ln)
                for m in DOI_RX.finditer(ln):
                    add(doi, m.group(1).rstrip(".)"), rel, i, ln)
                for m in URL_RX.finditer(ln):
                    u = m.group(0).rstrip(".),;")
                    if "doi.org/" in u or "arxiv.org/" in u:
                        continue
                    add(urls, u, rel, i, ln)
    for e in arxiv.values():
        e["url"] = "https://arxiv.org/abs/" + e["id"]
    for e in doi.values():
        e["url"] = "https://doi.org/" + e["id"]
    for e in urls.values():
        e["url"] = e["id"]
    # the one data source the index links itself, and the spectra compilations by species
    _find("method/members/The_Method_1_6-2.md", r"https://physics\.nist\.gov/asd")
    _find("method/members/LW1-ground.py", r"NIST ASD ver\. 5\.12")
    return {
        "note": "identifiers the index's sources cite, found at build by pattern and linked by "
                "construction; a compilation named without an identifier is cited as a string "
                "and not linked, because the target would be invented. A citing line is quoted "
                "only from a paper released to the site.",
        "quoted_from": sorted(PUBLIC_PAPERS.values()),
        "arxiv": sorted(arxiv.values(), key=lambda e: e["id"]),
        "doi": sorted(doi.values(), key=lambda e: e["id"]),
        "urls": sorted(urls.values(), key=lambda e: e["id"]),
        "nist_asd": {"name": "NIST Atomic Spectra Database (ver. 5.12), Kramida, Ralchenko, Reader and NIST ASD Team (2024)",
                     "url": "https://physics.nist.gov/asd", "doi": "10.18434/T4W30F",
                     "doi_url": "https://doi.org/10.18434/T4W30F",
                     "cited_for": ["the observed ground configurations, Z = 1 to 108",
                                   "the measured levels of the spectra index"],
                     "query_not_held": "no query string or URL behind the level tables is stored "
                                       "anywhere; the query itself is NOT HELD -- the database is "
                                       "linkable, the query is not"},
        "spectra_sources": spectra_sources(),
    }


def spectra_sources():
    """Section B.1 of the Spectra Compendium: which compilation each measured
    species' levels were drawn from, parsed from the table as printed."""
    rel = "method/members/The_Method_1_6___Spectra_Compendium-2.md"
    lines = _lines(rel)
    start, _, _ = _find(rel, r"^## B\.1 Sources")
    rows = []
    for i in range(start, len(lines)):
        ln = lines[i]
        if i > start and (ln.startswith("##") or ln.strip().startswith("**Additional")):
            break
        if not ln.startswith("  ") or ln.strip() == "" or ln.strip().startswith("compilation"):
            continue
        name, species = ln[2:30].strip(), ln[30:].strip()
        if name and species:
            rows.append({"compilation": name, "species": species})
        elif name and rows:
            rows[-1]["compilation"] += " " + name
        elif species and rows:
            rows[-1]["species"] += " " + species
    by_species = {}
    for r in rows:
        for sp in [s.strip() for s in r["species"].split(",") if s.strip()]:
            by_species[sp] = {"compilation": r["compilation"],
                              "url": "https://physics.nist.gov/asd" if r["compilation"].startswith("NIST ASD") else None}
    if len(by_species) < 20:
        raise RuntimeError("%s: B.1 parsed %d species, expected about 26" % (rel, len(by_species)))
    return {"source": "the spectra index's own table of compilations by species",
            "rows": rows, "by_species": by_species}


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
            "operator": "cypher.op_order, R, the order operator",
            "status": populate.PINNED,
            "periodic": {"held": len(held), "admitted": len(admitted),
                         "E": len(admitted) - len(held),
                         "index": "periodic table (period x group), the ninety "
                                  "main-table cells"},
            "helium_at_2": dict(helium_placement()["helium_at_2"],
                                index="the ninety cells with helium moved to "
                                      "(1, 2); the author's rule records E = 20"),
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
                            "source": "the one-electron identity: at Ne = 1 the (Ne-1)/Ne "
                                      "factor vanishes identically"},
        "pauli": {"status": populate.PINNED,
                  "source": "the Pauli bound's definition; populate.selftest's own pair",
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
        "note": "COORDINATES-2.13 rows only; the observed configurations stop at Z = 108",
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


def build(spectra, out_dir=OUT, write=True, log=print, with_particles=False, warp_root=WARP_ROOT):
    held, admitted = populate.layout_closure()
    relb = relativistic()
    rel_z = {e["Z"] for e in relb["eleven"]}
    walk, walk_rows = walk_block()
    relb["walk"] = walk
    walk_z = {e["Z"] for e in (walk or {}).get("entrants", []) if e["displaced"]}
    walk_lx_z = {e["Z"] for e in ((walk or {}).get("fields", {}).get("lx", {}).get("entrants", [])) if e["displaced"]}
    lim_block = limits(spectra)
    fig = figure_source()
    figures = []
    if fig and os.path.exists(fig["path"]):
        with open(fig["path"], "rb") as fh:
            blob = fh.read()
        figures.append({"file": "figures/" + FIGURE, "bytes": len(blob),
                        "md5": hashlib.md5(blob).hexdigest(),
                        "md5_recorded": fig["md5_recorded"],
                        "ok": hashlib.md5(blob).hexdigest() == fig["md5_recorded"],
                        "caption": "Figure 5 of the Löwdin paper: the derived "
                                   "table at c = 137 against c -> inf",
                        "status": populate.READ})
        if write:
            os.makedirs(os.path.join(out_dir, "figures"), exist_ok=True)
            with open(os.path.join(out_dir, "figures", FIGURE), "wb") as fh:
                fh.write(blob)
    denied = sorted(admitted - held)
    denied_cells = denied_cell_definitions(denied)
    papers = papers_block(out_dir, write, log)
    pindex, _pfull = particle_index_block(warp_root, write, out_dir)
    walk_copy = None
    if walk and os.path.exists(WALK_TSV):
        with open(WALK_TSV, "rb") as fh:
            wblob = fh.read()
        if write:
            with open(os.path.join(out_dir, "LOWDIN-WALK.tsv"), "wb") as fh:
                fh.write(wblob)
        walk_copy = {"file": "data/LOWDIN-WALK.tsv", "bytes": len(wblob), "md5": hashlib.md5(wblob).hexdigest(),
                     "what": "the reconstructed walk, 476 rows, RECONSTRUCTED; the table the site reads"}
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
        rec["walk"] = walk_rows.get(Z)
        rec = public_obj(rec)
        counts = _counts(rec)
        lim = _limit_counts(rec)
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
            "relativistic": Z in rel_z,
            "walk_displaced": Z in walk_z,
            "walk_lx_displaced": Z in walk_lx_z,
            "limits": lim,
        })
        log("  Z=%3d %-3s %7d B  rows %5d  measured %3d" % (
            Z, rec["symbol"], len(blob), counts["rows"], counts["measured"]))

    axes = [{"axis": a, "status": s, "source": PUBLIC_AXIS_SOURCES.get(a, d)} for a, s, d in populate.AXES]
    index = {
        "meta": {
            "title": SITE_TITLE,
            "subtitle": SITE_SUBTITLE,
            "built": _dt.datetime.now(_dt.timezone.utc).isoformat(timespec="seconds"),
            "commit": _git_head(),
            "generator": "tools/webindex.py over tools/populate.py",
            "names_note": "Element names are IUPAC labels for search only; "
                          "they are not a figure of the index, which carries "
                          "symbols.",
            "url": SITE_URL,
            "cite": cite_block(_git_head()),
            "history": _git_history(),
        },
        "papers": papers,
        "downloads": [d for d in [
            {"file": "data/index.js", "what": "the index: layout, closure, lattice, references, instruments, fixtures, manifest"},
            {"file": "data/elements/<Z>.js", "what": "one element's record, every ion and channel, with statuses; md5 per file in the manifest"},
            {"file": papers["file"], "bytes": papers["bytes"], "md5": papers["md5"], "what": "the released papers, rendered"},
            *[{"file": "data/" + p["pdf"]["file"], "bytes": p["pdf"]["bytes"], "md5": p["pdf"]["md5"], "what": "%s, as a PDF; md5 measured at build, commit %s" % (p["title"], p["pdf"]["commit"] or "?")}
              for p in papers["papers"] if p.get("pdf")],
            {"file": pindex["file"], "bytes": pindex["bytes"], "md5": pindex["md5"], "what": "the particle indexes: 572 members of the PDG 2026 table with their coordinates and statuses"} if pindex else None,
            walk_copy,
            {"file": "figures/" + FIGURE, "what": "Figure 5 of the Löwdin paper, with its ledger md5"} if figures else None,
        ] if d],
        "sources": sources(),
        "status_legend": STATUS_LEGEND,
        "axes": axes,
        "caps": populate.CAPS,
        "lambda_coords": populate.LAMBDA_COORDS,
        "lambda_meaning": populate.LAMBDA_MEANING,
        "lattice": lattice_block(spectra),
        "particles": particles_block() if with_particles else None,
        "particle_index": pindex,
        "references": references_block(),
        "closure": {
            "index": "the eighteen-column periodic layout (period × group)",
            "operator": "ℛ, the PINNED order operator (tools/cypher.py)",
            "held": len(held), "admitted": len(admitted),
            "E": len(admitted) - len(held),
            "denied": [list(c) for c in denied],
            "denied_cells": denied_cells,
            "decomposition": {
                "status": populate.READ,
                "source": "the author's standing account of the thirty-six",
                "forbidden": sum(1 for d in denied_cells if d["class"] == "forbidden"),
                "deferred": sum(1 for d in denied_cells if d["class"] == "deferred"),
                "by_subshell": {k: sum(1 for d in denied_cells if d["subshell"] == k)
                                for k in sorted({d["subshell"] for d in denied_cells})},
                "rule": "l by group: s at 1-2, d at 3-12, p at 13-18 (READ); class by "
                        "l <= n-1 (PINNED); the split 25 + 11 is the author's own (READ) "
                        "and the derivation is asserted against it",
            },
            "placement": helium_placement(),
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
                     "source": "the channel equation's final form"},
        "instruments": dict(instruments(), **(walk_instruments() if walk else {}),
                            **(mucf_instruments() if with_particles else {}), lowdin_construction={
            "python": None,
            "file": PUBLIC_PAPERS["THE-LOWDIN-SOLUTION-2.md"],
            "status": populate.READ,
            "held": False,
            "source": "the scalar-relativistic construction is not held; the "
                      "paper's own statement is shown in its place",
            "text": "\n\n".join(t for t in [
                relb["statement"], relb["construction"], relb["thorium"]] if t)}),
        "relativistic": relb,
        "limits": lim_block,
        "figures": figures,
        "fixtures": fixtures(spectra),
        "figure_data": {"equation": equation_points(spectra)},
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
    index = public_obj(index)
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

def selftest(warp_root=WARP_ROOT):
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
    index = build(spectra, write=False, log=lambda *_a, **_k: None, warp_root=warp_root)
    # the public guard: no string of the public build cites the unpublished books
    hits = private_strings(index)
    for Z in sorted(set(populate.LW1.GROUND) | set(spectra.by_z)):
        rec = public_obj(element_record(Z, spectra))
        private_strings(rec, "elements/%d" % Z, hits)
    if index["particle_index"] is not None:
        private_strings(particle_index_block(warp_root, write=False)[1], "particles", hits)
    for path, text in hits[:12]:
        print("    private: %s: %s" % (path, text))
    check("public build: no string cites the unpublished books", len(hits), 0)
    check("public build: the particles block is off without --with-particles", index["particles"], None)
    check("public build: the muon balance's instruments are off without --with-particles",
          [n for n in index["instruments"] if n in {m[0] for m in MUCF_INSTRUMENTS}], [])
    full = build(spectra, write=False, log=lambda *_a, **_k: None, with_particles=True, warp_root=warp_root)
    check("with particles: the muon balance's seven instruments follow the walk's",
          [n for n in full["instruments"] if n in {m[0] for m in MUCF_INSTRUMENTS}],
          [n for n, *_ in MUCF_INSTRUMENTS])
    px = index["particle_index"]
    if px is None:
        print("  (the particle indexes are not built: %s holds no research/warp-drive tree; pass --warp-root)" % warp_root)
        check("particle indexes: absent from this build, and the index says so", px, None)
    else:
        _ps, pfull = particle_index_block(warp_root, write=False)
        private_strings(pfull, "particles", hits)
        four = len(px["indexes"]) == 4
        check("particle indexes: " + ("four, in order, the spin-4 mesons last" if four else "three, in order"), [x["id"] for x in px["indexes"]], ["fundamental", "mesons", "baryons"] + (["spin4"] if four else []))
        check("particle indexes: members 30, 250, 292" + (", 10" if four else ""), [x["members"] for x in px["indexes"]], [30, 250, 292] + ([10] if four else []))
        check("particle indexes: charted 30, 242, 278" + (", 10" if four else ""), [x["charted"] for x in px["indexes"]], [30, 242, 278] + ([10] if four else []))
        check("particle indexes: cells 26, 66, 184" + (", 9" if four else ""), [x["cells"] for x in px["indexes"]], [26, 66, 184] + ([9] if four else []))
        check("particle indexes: channels K2, K0, K0" + (", K4" if four else ""), [x["cell"]["channel"] for x in px["indexes"]], [2, 0, 0] + ([4] if four else []))
        check("particle indexes: the accounting identity 6506 = 5880 + 54 + 572", px["accounting"]["identity"], "6506 = 5880 + 54 + 572")
        check("particle indexes: 572 members, 550 charted, 22 unplaced", [px["accounting"][k] for k in ("members", "charted", "unplaced")], [572, 550, 22])
        check("particle indexes: every member row carries a status on every coordinate",
              all(all(c["status"] in STATUS_LEGEND for c in ix["coordinates"]) for ix in pfull["indexes"]), True)
        check("particle indexes: every row of every index is in the file",
              [len(ix["rows"]) for ix in pfull["indexes"]], [30, 250, 292] + ([10] if four else []))
        s4 = next((ix for ix in pfull["indexes"] if ix["id"] == "spin4"), None)
        if s4:
            check("spin-4 mesons: 10 members on 9 cells, cell (4, 5, 3), closed by information and statistics", (s4["members"], s4["cells"], s4["cell"], s4["closers"]), (10, 9, {"channel": 4, "height": 5, "width": 3}, ["information", "statistics"]))
            check("spin-4 mesons: 2J is constant at 8, so the effective arity is 3", (s4["held_constant"]["value"], s4["held_constant"]["constant"], s4["arity"]["effective"]), (8, True, 3))
            check("spin-4 mesons: the channel moves with the status reach, K5 then K4; K5 on the established states", (s4["reach"]["moves"], s4["reach"]["channels_seen"], s4["reach"]["established"]), (True, [4, 5], {"cells": 7, "channel": 5, "note": s4["reach"]["established"]["note"]}))
            check("spin-4 mesons: the two massless rows are charted, and every member is a meson row", (s4["massless"], all(r["extra"]["family"] == "meson" for r in s4["rows"])), (["K(4)(2500)+", "K(4)(2500)-"], True))
            check("spin-4 mesons: statistics is free at arity 2, every chart of at least 105", (s4["arity"]["statistics_at_arity_2"]["closes"] == s4["arity"]["statistics_at_arity_2"]["charts"], s4["arity"]["statistics_at_arity_2"]["charts"] >= 105), (True, True))
        nu = pfull.get("nuclear")
        if nu and not nu.get("absent"):
            ni = nu["index"]
            check("nuclear bands: 2,152 members of 2,245 levels on 121 cells, cell (2, 63, 2)", (ni["members"], ni["levels_captured"], ni["cells"], ni["cell"]), (2152, 2245, 121, {"channel": 2, "height": 63, "width": 2}))
            check("nuclear bands: the K2 is the free one, said", (ni["free_channel"]["arity"], ni["free_channel"]["free"]), (2, True))
            check("nuclear bands: three refusals counted apart, 27 + 93 + 6", [ni["refusals"][k] for k in ("bands_no_spin", "levels_no_parity", "levels_no_spin_in_a_band")], [27, 93, 6])
            check("nuclear bands: every superset of (2I, P) is K0", sorted({r["channel"] for r in ni["supersets"]["rows"][1:]}), [0])
            check("nuclear bands: the bands as a sub-population hold 67 cells", ni["bands"]["cells"], 67)
            check("nuclear bands: the capture reproduces the paper's census exactly, 252/123 and 38/27", (nu["capture"]["census"]["exact"], nu["capture"]["census"]["measured"]), (True, {"MR": {"bands": 252, "nuclei": 123}, "AMR": {"bands": 38, "nuclei": 27}}))
            check("nuclear bands: 213 of 213 AMR steps at ΔI = 2", (nu["capture"]["selection_rule"]["AMR"]["delta_2I_4"], nu["capture"]["selection_rule"]["AMR"]["steps"]), (213, 213))
            check("nuclear bands: the source md5 is the one the capture records", nu["capture"]["source_md5"], nu["capture"]["source_md5_now"])
            check("nuclear bands: every member row carries both coordinates and a nucleus", all(len(r["coords"]) == 2 and r["extra"]["A"] > r["extra"]["Z"] > 0 for r in ni["rows"]), True)
            if nu.get("deformed"):
                d36 = nu["deformed"]
                if d36.get("closure"):
                    check("deformed bands: all 234 entries recovered, 173 bands and 61 bandheads exact, total, not seated", (d36["census"], d36["recovered"], d36["total"], d36["verdict"]), ({"entries": 234, "bands": 173, "bandheads": 61}, 234, True, "CAPTURED IN FULL, NOT SEATED"))
                    check("deformed bands: exactly one dotted band-number line, and one discontinuity left, acquitted", (len(d36["closure"]["dotted_lines"]), len(d36["discontinuities"])), (1, 1))
                    check("deformed bands: the chart these levels would give, 96 cells at K2, cell (2, 49, 2), measured not seated", (d36["closure"]["chart"]["cells"], d36["closure"]["chart"]["channel"], d36["closure"]["chart"]["cell"]), (96, 2, {"channel": 2, "height": 49, "width": 2}))
                else:
                    check("deformed bands: 233 of 234 entries recovered, 61 bandheads exact, not seated", (d36["census"], d36["recovered"], d36["verdict"]), ({"entries": 233, "bands": 172, "bandheads": 61}, 233, "CAPTURED, NOT SEATED"))
                check("deformed bands: the document's delimiter is absent, 0 of 210, and the earlier refusal is retracted", (d36["separators"]["available"], d36["separators"]["required"], "RETRACTED" in d36["why"]), (0, 210, True))
        pr = pfull.get("predictions")
        if pr and not pr.get("absent"):
            check("predictions: 3,206 demanded cells over 22 indexes, 16 predicting and 6 complete", (pr["total_E"], len(pr["E_by_index"]), pr["partition"]["predicting"], pr["partition"]["complete"]), (3206, 22, 16, 6))
            check("predictions: the partition is exact, E = 0 iff the index closes under information", (pr["partition"]["zero_close_information"], pr["partition"]["positive_do_not"]), (True, True))
            check("predictions: adjudicated 593 forbidden, 36 unplaced, 2,479 open, 98 undecided", pr["adjudication"]["totals"], {"E": 3206, "forbidden": 593, "unplaced": 36, "open": 2479, "undecided": 98})
            check("predictions: the mesons' fifteen are 0 forbidden, 3 unplaced, 12 open, cell by cell", [pr["by_index"]["mesons"][k] for k in ("E", "forbidden", "unplaced", "open")], [15, 0, 3, 12])
            check("predictions: the baryons' 1,012 are 593 forbidden by Gell-Mann–Nishijima, 8 unplaced, 411 open, cell by cell", [pr["by_index"]["baryons"][k] for k in ("E", "forbidden", "unplaced", "open")], [1012, 593, 8, 411])
            check("predictions: every site index's cell-by-cell counts agree with the instrument's recorded table", all(v["recorded"] is None or [v["E"], v["forbidden"], v["unplaced"], v["open"], v["undecided"]] == v["recorded"] for v in pr["by_index"].values()), True)
            check("predictions: the worked case is the D_s slot, and it is pinned by a named row", (pr["worked_case"]["cell"], any(x["cell"] == pr["worked_case"]["cell"] and x["bin"] == "UNPLACED" and x["pinned_by"] for x in pr["by_index"]["mesons"]["cells"])), ([2, -1, 0, 3], True))
            check("predictions: Gell-Mann–Nishijima re-derived, 292 of 292 baryons clean and two meson faults recorded", (pr["gmn"]["baryons"]["identity_ok"], pr["gmn"]["baryons"]["rows"], len(pr["gmn"]["mesons"]["faults"])), (292, 292, 2))
            check("predictions: the fault's consequence is nil, measured", pr["gmn"]["fault_consequence"]["as_captured"] == pr["gmn"]["fault_consequence"]["with_I_zero"], True)
            check("predictions: the quark-model theorem holds and the element precedent is an order deficit with a zero join deficit", (pr["gmn"]["quark_model_theorem"]["holds"], pr["element_precedent"]["E_order"], pr["element_precedent"]["E_join"], pr["element_precedent"]["order_ghosts_forbidden_by_l_le_n_minus_1"]), (True, 36, 0, 25))
            # every demanded cell's coordinate values are values some member of that index carries (the projection law), so the explorer can place it
            ok_place = True
            for sid, v in pr["by_index"].items():
                src = next((ix for ix in pfull["indexes"] if ix["id"] == sid), None) or (pfull["nuclear"]["index"] if sid == "nucbands" and pfull.get("nuclear") else None) \
                      or ((pfull.get("quasiparticles") or {}).get({"fqh": "seated", "readrezayi": "nonabelian", "bosons": "bosons"}.get(sid, sid)) if sid in ("fqh", "readrezayi") else None)
                if not src:
                    continue
                rows = src["rows"]
                vals = [set(r["coords"][i] for r in rows if r["coords"][i] is not None) for i in range(len(rows[0]["coords"]))]
                ok_place &= all(all(x["cell"][i] in vals[i] for i in range(len(vals))) for x in v["cells"])
            check("predictions: every demanded cell of the site's indexes sits on coordinate values its members carry", ok_place, True)
        bo = pfull.get("bonds")
        if bo:
            check("bonds: three refusals on three grounds, and no channel empty", (len(bo["refusals"]), bo["channels"]["empty"]), (3, []))
            check("bonds: fourteen NN partial waves at J ≤ 3, growing 6, 10, 14, 18", (len(bo["particle"]["partial_waves_J3"]), [g["channels"] for g in bo["particle"]["growth"]]), (14, [6, 10, 14, 18]))
            check("bonds: an MO is not a bond, and g/u is the host's on 34 of 103", ([b["equal"] for b in bo["molecular"]["bond_vs_mo"]], bo["molecular"]["measured"]["without_gu"]), ([True, False, False, False], 34))
        sp = pfull.get("subpop")
        if sp and not sp.get("absent"):
            grown = bool(nu and not nu.get("absent"))
            check("sub-population sweep: %s closed sets, 2 reaching an unoccupied channel" % ("more than 143 once the band index is seated" if grown else "143"), (sp["census"]["closed_sets"] > 143 if grown else sp["census"]["closed_sets"], sp["census"]["reaching_an_unoccupied_channel"]), (True if grown else 143, 2))
            check("sub-population sweep: both hits at K4, one at effective arity 2 and one at 3", sorted((h["channel"], h["effective_arity"]) for h in sp["hits"]), [(4, 2), (4, 3)])
            check("sub-population sweep: under the mass reach the spin-4 population never reaches K4", 4 in {c["channel"] for c in sp["spin4_under_mass"]["cuts"]}, False)
            check("sub-population sweep: three lattices, and the family's chain is 2 over 14 containments", (sp["lattices"]["count"], sp["family"]["containments"], sp["family"]["longest_chain"]), (3, 14, 2))
            check("sub-population sweep: the not-lattices and the one too large to test are counted apart", (sp["lattices"]["not"] >= 18, sp["lattices"]["undetermined"] <= 1), (True, True))
            check("sub-population sweep: the exhaustive chains are 5, 7, 6, 14", [e["longest_chain"] for e in sp["exhaustive"]], [5, 7, 6, 14])
            check("sub-population sweep: two lattices peel to empty, exact", sorted(r["lattice"] for r in sp["recursion"] if r["maximal"]), ["bosonqp.index", "overlaprule.madelung_slot"])
            check("sub-population sweep: the chiral Goldstones are a full box, the electroweak ones a relabelling", (sp["candidates"]["chiral_goldstone"]["full_box"], sp["candidates"]["electroweak"]["held_by_fundamental"]), (True, True))
            check("sub-population sweep: five routes to nuclear bands, one open, one candidate source", (len(sp["candidates"]["nuclear_bands"]["routes"]), [s["arxiv"] for s in sp["candidates"]["nuclear_bands"]["sources"] if s["candidate"]]), (5, ["2508.05447"]))
        check("particle indexes: the fundamental collisions are four", len(pfull["indexes"][0]["collisions"]), 4)
        check("particle indexes: the capture's md5 is recorded", bool(px["source"]["capture"] and px["source"]["capture"][0]["md5"]), True)
        if "antimatter" in pfull["accounting"]:
            am = pfull["accounting"]["antimatter"]
            check("antimatter: 231 of the 550 charted members, 13 + 79 + 139", ([r["antiparticles"] for r in am["by_index"]], am["total"]), ([13, 79, 139], 231))
            check("named by hand: the photon, the muon and the antimuon resolve with their cells",
                  [(r["what"], r["cell"]) for r in pfull["accounting"]["named"]["rows"]],
                  [("photon", [2, 0, 1, 0]), ("muon", [1, -3, 1, 2]), ("antimuon", [1, 3, 1, 2])])
        sw = pfull.get("sweep")
        if sw and not sw.get("absent"):
            check("sweep: 142 charts, 11 + 11 + 120", (sw["charts"], sw["census"]), (142, {"fundamental": 11, "mesons": 11, "baryons": 120}))
            check("sweep: " + ("two hits against the overlap rule's census and one against the live occupancy once K4 is taken" if four else "three hits against the ruling's census, two against the honest occupancy"),
                  (len(sw["hits"]["against_the_overlap_rules_census"]), len(sw["hits"]["against_the_honest_occupancy"])), (2, 1) if four else (3, 2))
            check("sweep: the seating is baryons (2I, Q3) at K5, 16 cells, cell (5, 7, 4)",
                  (sw["seated"]["parent"], sw["seated"]["cols"], sw["seated"]["channel"], sw["seated"]["cells"], sw["seated"]["cell"]),
                  ("baryons", ["2I", "Q3"], 5, 16, {"channel": 5, "height": 7, "width": 4}))
            check("sweep: all four grounds hold for the seating", all(sw["seated"]["grounds"].values()), True)
            check("sweep: the four corners not held lie outside the hull", (sw["seated"]["corners_not_held"], sw["seated"]["corners_outside_hull"]),
                  ([[0, -6], [0, 6], [1, -6], [1, 6]], True))
            check("sweep: statistics is free at arity 2, every chart of at least 105; geometry is earned, 74", (sw["arity2_freeness"]["statistics"]["closes"] == sw["arity2_freeness"]["statistics"]["charts"], sw["arity2_freeness"]["statistics"]["charts"] >= 105, sw["arity2_freeness"]["geometry"]["closes"]), (True, True, 74))
            check("sweep: " + ("all eight channels occupied once the spin-4 index is seated" if four else "seven channels occupied, only K4 empty"), sw["occupancy"]["now"], [0, 1, 2, 3, 4, 5, 6, 7] if four else [0, 1, 2, 3, 5, 6, 7])
        fq = (pfull.get("quasiparticles") or {}).get("seated")
        if fq and not fq.get("absent"):
            check("quasiparticles seated: 168 members of 12 states, 30 cells, cell (0, 15, 4)", (fq["members"], fq["states"], fq["cells"], fq["cell"]), (168, 12, 30, {"channel": 0, "height": 15, "width": 4}))
            check("quasiparticles seated: the box-invariance verdict is SEAT", fq["verdict"], "SEAT")
            check("quasiparticles seated: 150 anyons, 0 fermions, 18 bosons", [fq["statistics"][k] for k in ("anyons", "fermions", "bosons")], [150, 0, 18])
            check("quasiparticles seated: the observed states are 1/3, 1/5, 1/7", [o["m"] for o in fq["observed"]], [3, 5, 7])
            check("quasiparticles seated: every row carries four coordinates and its charge as a fraction", all(len(r["coords"]) == 4 and "/" in r["Q"] or r["j"] == 0 for r in fq["rows"]), True)
        bq = (pfull.get("quasiparticles") or {}).get("bosons")
        if bq:
            check("bosonic excitations: members, cells and channel as the record states", (len(bq["members"]), bq["cells"], bq["cell"]["channel"]), (15, 5, 7))
            check("bosonic excitations: the trion excludes itself as a fermion", [x["name"] for x in bq["excluded"]], ["trion"])
            check("bosonic excitations: not a subset of the bosons, and the union still a sublattice", (bq["relation"]["qp_subset_of_bosons"], bq["relation"]["union_sublattice"]), (False, True))
        rr = (pfull.get("quasiparticles") or {}).get("nonabelian")
        if rr:
            check("non-abelian: 363 primaries of 11 levels, 78 cells, K0", (rr["members"], rr["levels"], rr["cells"], rr["cell"]["channel"]), (363, 11, 78, 0))
            check("non-abelian: the verdict is SEAT", rr["verdict"], "SEAT")
            check("non-abelian: every literature fixed point agrees", all(v["agrees"] for v in rr["validation"]), True)
            check("non-abelian: neither Hall index nests in the other", (rr["nesting"]["abelian_in_nonabelian"], rr["nesting"]["nonabelian_in_abelian"]), (False, False))
        if pfull["quasiparticles"] and pfull["quasiparticles"].get("anyons"):
            qa = pfull["quasiparticles"]["anyons"]
            check("quasiparticles: the anyon chart is refused as a theorem", qa["verdict"], "REFUSE-AS-THEOREM")
            check("quasiparticles: the semion's h is 1/4", next(r["h"] for r in qa["rows"] if r["k"] == 1 and r["J"] == 1), "1/4")
            check("quasiparticles: 230 space groups, 32 point groups, 73 arithmetic classes",
                  [pfull["quasiparticles"]["no_table"][k] for k in ("space_groups", "point_groups", "arithmetic_classes")], [230, 32, 73])
    pp = index["papers"]["papers"]
    check("papers: the three released papers, in order", [p["slug"] for p in pp], ["lowdin", "three-body", "languages"])
    check("papers: all three are held", [p["held"] for p in pp], [True, True, True])
    check("papers: every paper from the store carries the store's md5", all(p["md5"] == p["md5_recorded"] for p in pp if p["held"] and p["md5_recorded"]), True)
    check("papers: the hierarchy law paper comes from the research tree with its commit, and its PDF with an md5",
          (pp[2]["tree"]["path"], bool(pp[2]["tree"]["commit"]), bool(pp[2]["pdf"] and pp[2]["pdf"]["md5"])),
          ("research/warp-drive/paper/THE-HIERARCHY-LAW.md", True, True))
    check("papers: the hierarchy law paper is over ten thousand words and opens with the law", (pp[2]["words"] > 10000, pp[2]["title"]), (True, "The Hierarchy Law of Mathematical Languages"))
    full_papers = json.loads(open(os.path.join(OUT, PAPERS_JS), encoding="utf-8").read()[len(PAPERS_PREFIX):-len(WRAP_SUFFIX)]) if os.path.isfile(os.path.join(OUT, PAPERS_JS)) else []
    lang = next((p for p in full_papers if p["slug"] == "languages"), None)
    if lang:
        check("papers: the hierarchy law paper cites nothing from the books, measured by the guard with its own section marks excluded",
              (lang["book_citations"], sorted(lang["own_section_marks"])), ([], sorted(_OWN_SECTION_MARKS)))
        check("papers: its render carries every heading of the source", len(lang["headings"]), sum(1 for ln in open(os.path.join(REPO, "research/warp-drive/paper/THE-HIERARCHY-LAW.md"), encoding="utf-8") if ln.startswith("#")))
    check("papers: every figure a held paper cites is carried with its ledger md5", all(p["figures_ok"] for p in pp if p["held"]), True)
    check("papers: the three-body paper cites 3 figures, the Löwdin paper 3 or more",
          (pp[1]["figures"], pp[0]["figures"] >= 3), (3, True))
    html_l, heads_l = md_to_html(open(os.path.join(MEMBERS, "THE-LOWDIN-SOLUTION-2.md"), encoding="utf-8").read(), {"img": lambda a, b: ""})
    src_heads = [ln.lstrip("#").strip() for ln in open(os.path.join(MEMBERS, "THE-LOWDIN-SOLUTION-2.md"), encoding="utf-8") if ln.startswith("#")]
    check("papers: the render carries every heading of the Löwdin paper", len(heads_l), len(src_heads))
    check("papers: no raw markdown heading survives the render", "\n#" in html_l, False)
    fd = index["figure_data"]["equation"]
    check("figure data: one point per scored measured channel", len(fd["rows"]), index["fixtures"]["equation_report"]["channels"])
    check("meta: cite line names the author, the title and the edition", (SITE_AUTHOR in index["meta"]["cite"]["text"], SITE_TITLE in index["meta"]["cite"]["text"]), (True, True))
    check("meta: the edition history is carried, oldest first, every row with a date", all(r["date"] for r in index["meta"]["history"]) and len(index["meta"]["history"]) >= 1, True)
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
    pt = full["particles"]
    check("particles: the structural window is [119, 918] m_e (paper section 2)", pt["window"]["m_e"], [119, 918])
    check("particles: the window's occupants, muon and pion, in m_e", [pt["window"]["occupants"]["muon"], pt["window"]["occupants"]["pion"]], [207, 273])
    check("particles: the muon mass PDG 206.7683 from fault 14f-04", pt["muon"]["mass_m_e"]["PDG"], 206.7683)
    check("particles: 27 constants of Lambda_phys parsed", pt["constants"]["count"], 27)
    check("particles: mucf.py's status table read (rows)", len(pt["muon"]["instrument"]["status_table"]) >= 10, True)
    check("particles: the four exotic systems of PART K", [x["system"] for x in pt["antimatter"]["reduced_mass"]["systems"]],
          ["positronium", "hydrogen, antihydrogen", "muonic hydrogen", "antiprotonic helium"])
    check("particles: antiprotonic helium's cell (35, 33)", pt["antiprotonic_helium"]["cell"], [35, 33])
    check("particles: ten PROSE-ONLY rows carried", len(pt["prose_only"]), 10)
    check("particles: neutrino, gluon, Higgs are absent from the corpus",
          [pt["absent"]["terms"][t]["occurrences"] for t in ("neutrino", "gluon", "Higgs")], [0, 0, 0])
    rf = index["references"]
    check("references: the NIST ASD DOI is the corpus's own", rf["nist_asd"]["doi"], "10.18434/T4W30F")
    check("references: arXiv identifiers found (at least 40)", len(rf["arxiv"]) >= 40, True)
    check("references: DOIs found (at least 6)", len(rf["doi"]) >= 6, True)
    check("references: B.1 maps at least 24 species to a compilation", len(rf["spectra_sources"]["by_species"]) >= 24, True)
    lat = index["lattice"]
    check("lattice: sites = 8 * sum Z (charge 1..Z by l 0..7 for every element)",
          lat["sites"], 8 * sum(range(1, lat["Z_max"] + 1)))
    check("lattice: known cells = measured + exact rows", len(lat["known"]),
          sum(1 for r in spectra.rows if r["grade"] in ("measured", "exact")))
    check("lattice: measured cells", lat["counts"]["measured"],
          sum(1 for r in spectra.rows if r["grade"] == "measured"))
    c = index["closure"]
    check("closure held (section 6)", c["held"], 90)
    check("closure admitted", c["admitted"], 126)
    check("closure E", c["E"], 36)
    check("denied cells listed", len(c["denied"]), 36)
    d = c["decomposition"]
    check("the thirty-six decompose 25 forbidden (section 6.1.1)", d["forbidden"], 25)
    check("the thirty-six decompose 11 deferred (section 6.1.1)", d["deferred"], 11)
    check("by subshell: 1d 10, 1p 5, 2d 10, 3d 10, helium's slot 1",
          d["by_subshell"], {"1d": 10, "1p": 5, "2d": 10, "3d": 10,
                             "1s, the slot helium vacates": 1})
    check("every denied cell carries a definition",
          sorted((x["p"], x["g"]) for x in c["denied_cells"]),
          sorted(tuple(x) for x in c["denied"]))
    pl = c["placement"]
    check("E with helium at group 18 (Register 448)", pl["helium_at_18"]["E"], 36)
    check("E with helium at group 2 (Register 448)", pl["helium_at_2"]["E"], 20)
    check("E prices the placement at sixteen cells", pl["priced"], 16)
    check("helium at group 2: the twenty are the 2d and 3d rows",
          pl["helium_at_2"]["denied"],
          [[2, g] for g in range(3, 13)] + [[3, g] for g in range(3, 13)])
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

    # --- the relativistic limit and the bounds facet -------------------------
    rel = index["relativistic"]
    check("relativistic: eleven elements read from the paper", len(rel["eleven"]), 11)
    check("relativistic: the eleven resolve to Z in LW1-ground.py",
          all(e["Z"] in populate.LW1.GROUND for e in rel["eleven"]), True)
    check("relativistic: r2-scf entrant table agrees, in order",
          [e["symbol"] for e in rel["sources"]["scf_audit"]["entrants"]],
          [e["symbol"] for e in rel["eleven"]])
    check("relativistic: every one of the eleven carries an entrant channel",
          all("entrant" in e for e in rel["eleven"]), True)
    check("relativistic: the paper's eleven line names the same eleven",
          all(e["symbol"] in rel["sources"]["paper"]["eleven_text"] for e in rel["eleven"]), True)
    check("relativistic: thorium sentence read", bool(rel["thorium"]), True)
    check("relativistic: instrument recorded as not held", rel["instrument"]["held"], False)
    check("relativistic: layout flags exactly eleven",
          sum(1 for e in index["layout"] if e["relativistic"]), 11)
    check("relativistic: Th is not among the eleven", 90 in {e["Z"] for e in rel["eleven"]}, False)
    figs = index["figures"]
    check("figure 5 held and md5 matches extracted/LEDGER.tsv",
          bool(figs) and all(f["ok"] for f in figs), True)
    walk = rel["walk"]
    check("walk: LOWDIN-WALK.tsv read into the relativistic block", walk is not None, True)
    if walk:
        lw = walk_module()
        check("walk: status RECONSTRUCTED, never flattened", walk["status"], populate.RECON)
        flds = sorted(walk["fields"])
        check("walk: the fields held", flds, sorted(k for k in ("lx", "hf") if k in walk["fields"]))
        check("walk: primary field is hf when held, else lx",
              walk["primary"], "hf" if "hf" in walk["fields"] else "lx")
        settings = walk["summary"]["settings"]
        for fld in flds:
            keys = sorted(k for k in settings if k.startswith(fld + ":"))
            check(f"walk {fld}: two settings, 137.035999 and inf", keys, [f"{fld}:137.035999", f"{fld}:inf"])
            check(f"walk {fld}: 119 rows per setting, Z = 2 to 120",
                  [(settings[k]["rows"], settings[k]["Z_first"], settings[k]["Z_last"]) for k in keys],
                  [(119, 2, 120), (119, 2, 120)])
            # every local-exchange row converged; three Hartree–Fock rows at c = 137.035999 did
            # not (Ts, Og, Ubn: the open 7p and 8s shells' multipliers against the closed shells
            # of their ℓ under the energy-dependent Koelling–Harmon operator settle at a residual
            # of 10⁻⁶ rather than 10⁻⁷), and the table says so on the row -- the fixture is the
            # measured record, never a flattened one
            check(f"walk {fld}: rows not converged, as the table records them",
                  [settings[k]["not_converged"] for k in keys],
                  [[], []] if fld == "lx" else [["Ts", "Og", "Ubn"], []])
            ents = walk["fields"][fld]["entrants"]
            check(f"walk {fld}: one entrant row per Z", [e["Z"] for e in ents], list(range(2, 121)))
            disp = [e["symbol"] for e in ents if e["displaced"]]
            cp = walk["summary"]["fields"][fld]
            check(f"walk {fld}: displaced set is the summary's", disp, [d["symbol"] for d in cp["displaced"]])
            check(f"walk {fld}: the summary's eleven are the paper's", cp["eleven"], lw.ELEVEN_1706)
            check(f"walk {fld}: in/not-in/missing partition the record's eleven and the displaced",
                  (sorted(cp["in_eleven"] + cp["eleven_not_displaced"]),
                   sorted(cp["in_eleven"] + cp["not_in_eleven"])),
                  (sorted(lw.ELEVEN_1706), sorted(disp)))
            check(f"walk {fld}: the thorium control is reported", cp["thorium"] is not None, True)
        check("walk: table rows are the settings' rows", walk["table"]["rows"], 119 * 2 * len(flds))
        check("walk: table md5 is the file's", walk["table"]["md5"], _md5(WALK_TSV))
        prim = walk["fields"][walk["primary"]]["entrants"]
        check("walk: layout flags exactly the primary field's displaced",
              sorted(e["symbol"] for e in index["layout"] if e["walk_displaced"]),
              sorted(e["symbol"] for e in prim if e["displaced"]))
        check("walk: the c constant is register 1701's", walk["c"]["c137"], 137.035999)
        check("walk: instruments carried with python, RECONSTRUCTED",
              all(index["instruments"][n]["status"] == populate.RECON and index["instruments"][n]["python"]
                  for n, _f, _s in WALK_INSTRUMENTS), True)
        check("walk: the primary field's not_reproduced is stated",
              bool(walk["not_reproduced"]), True)
    lim = index["limits"]
    check("limits: distinct bound notes", lim["distinct_notes"], 22)
    check("limits: every note classified", lim["unclassified"], [])
    check("limits: kind counts sum to the rows",
          sum(k["count"] for k in lim["kinds"]), len(spectra.rows))
    check("limits: layout counts sum to the rows",
          sum(sum(e["limits"].values()) for e in index["layout"]), len(spectra.rows))
    check("limits: no unclassified in any layout entry",
          any("unclassified" in e["limits"] for e in index["layout"]), False)

    # --- the data protocol ---------------------------------------------------
    check("manifest names .js files only",
          all(m["file"].endswith(".js") for m in index["manifest"]), True)
    h["walk"] = walk_block()[1].get(1)      # the build attaches the walk rows before serialising
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
    check("instruments: the nine with python, then the walk's ten, in order",
          [n for n, r in ins.items() if r.get("python")],
          [n for n, *_ in INSTRUMENTS] + ([n for n, *_ in WALK_INSTRUMENTS] if walk else []))
    check("instruments: the tenth is the unheld construction, text only",
          (ins.get("lowdin_construction", {}).get("python"),
           ins.get("lowdin_construction", {}).get("held"),
           bool(ins.get("lowdin_construction", {}).get("text"))),
          (None, False, True))
    parses = True
    for name, rec in ins.items():
        if not rec.get("python"):
            continue
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
    walk = (index.get("relativistic") or {}).get("walk")
    if walk:
        got = _md5(WALK_TSV) if os.path.exists(WALK_TSV) else None
        if got != walk["table"]["md5"]:
            bad += 1
            print("  MISMATCH %s  index %s  on disk %s" % (walk["table"]["file"], walk["table"]["md5"], got))
        else:
            print("  %-52s ok (the walk table the index was built from)" % walk["table"]["file"])
    for d in index.get("downloads", []):
        if not d.get("md5"):
            continue
        p = os.path.join(out_dir, d["file"][len("data/"):] if d["file"].startswith("data/") else d["file"])
        got = _md5(p) if os.path.exists(p) else None
        if got != d["md5"]:
            bad += 1
            print("  MISMATCH %s  index %s  on disk %s" % (d["file"], d["md5"], got))
        else:
            print("  %-52s ok (download, md5 as the index records it)" % d["file"])
    for f in index.get("figures", []):
        p = os.path.join(out_dir, f["file"])
        got = _md5(p) if os.path.exists(p) else None
        if got != f["md5"] or got != f["md5_recorded"]:
            bad += 1
            print("  MISMATCH %s  manifest %s  ledger %s  on disk %s" % (f["file"], f["md5"], f["md5_recorded"], got))
        else:
            print("  %-52s ok (extracted/LEDGER.tsv md5)" % f["file"])
    print("VERIFY OK" if bad == 0 else "VERIFY FAILED")
    return 0 if bad == 0 else 1


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--out", default=OUT)
    ap.add_argument("--selftest", action="store_true")
    ap.add_argument("--verify", action="store_true")
    ap.add_argument("--warp-root", default=WARP_ROOT,
                    help="the research/warp-drive tree the particle indexes are read from "
                         "(default: the repository's own); absent, the site carries none")
    ap.add_argument("--warp-commit", default=None,
                    help="the commit the tree at --warp-root is at, recorded in the index "
                         "beside the commit its own STATE.json stamps")
    ap.add_argument("--with-particles", action="store_true",
                    help="build the Particles block and the muon balance's instruments; "
                         "off by default because the paper they read is not released")
    args = ap.parse_args(argv)
    global WARP_COMMIT
    WARP_COMMIT = args.warp_commit
    if args.selftest:
        return selftest(args.warp_root)
    if args.verify:
        return verify(args.out)
    spectra = populate.Spectra(populate.DEFAULT_SPECTRA)
    index = build(spectra, out_dir=args.out, with_particles=args.with_particles, warp_root=args.warp_root)
    t = index["totals"]
    print("wrote %s: %d elements (%d populated, %d CSV-only), %d rows, "
          "%d measured" % (args.out, len(index["layout"]), t["populated"],
                           t["csv_only"], t["rows"], t["measured"]))
    return 0


if __name__ == "__main__":
    sys.exit(main())
