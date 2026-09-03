#!/usr/bin/env python3
"""sweep.py — the class sweep of RUL-152 item 2, run as a program.

Chat 152 rules that the Register is read in full and that **the Mathematical Compendium, the
Physics Compendium, the Index of Indices and the Spectra Compendium close by class sweep against
the docket's classes**, not line by line. This is that sweep.

The classes are not invented here. They are the thirteen already in `DEFECT-CENSUS.tsv`, and each
detector below is calibrated against the rows the census already records — a detector that cannot
reproduce the census's own rows on the volume the census swept is not the census's detector, and
is not run on the volumes it did not. `--selftest` asserts every one of those reproductions.

THREE VERDICTS, and the distinction is the point:

  RUN            the detector reproduces the census on a swept volume, and its rows on an unswept
                 one are the sweep's finding.
  NOT-APPLICABLE the class is defined against a form the volume does not use. The Mathematical
                 Compendium's R-form entry — `### name` / statement / scope / grade / prior art —
                 carries C6a, C10 and C11. The Index of Indices and the Spectra Compendium have
                 no `###` blocks at all and the Physics Compendium's are a different form, so
                 there is nothing there for those detectors to read. An empty census row for
                 those volumes is correct, not a gap.
  NOT-RUN        the census records rows the detector here cannot reproduce, so the census's own
                 detector is not recovered and this program declines to guess one. A resource or
                 definition limit is not a finding — the same rule `cypher.py` keeps with REFUSED.

Stdlib only. Reads the seated members; writes nothing.
"""
from __future__ import annotations

import argparse
import collections
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parent

VOLUMES = {
    "main": "The_Method_1_6-2.md",
    "reg":  "The_Method_1_6___The_Register-2.md",
    "mc":   "The_Method_1_6___Mathematical_Compendium-2.md",
    "pc":   "The_Method_1_6___The_Physics_Compendium-2.md",
    "ioi":  "The_Method_1_6___The_Index_of_Indices-2.md",
    "sc":   "The_Method_1_6___Spectra_Compendium-2.md",
}
COMPENDIA = ("mc", "pc", "ioi", "sc")          # the four RUL-152 item 2 names

Row = collections.namedtuple("Row", "cls member line item detail")


def members_dir() -> pathlib.Path:
    for c in (HERE / "members", ROOT / "method" / "members", HERE.parent / "members"):
        if (c / VOLUMES["mc"]).exists():
            return c
    sys.exit("cannot find method/members — run from the repository")


def load(tag: str) -> list[str]:
    return (members_dir() / VOLUMES[tag]).read_text(encoding="utf-8").splitlines()


# ---------------------------------------------------------------- the R-form

GRADE = re.compile(r"^(Proved|Measured|Computed)\b")
SEC_ANY = re.compile(r"§\d")
REGPTR = re.compile(r"\bR ?\d{3,4}\b|register\s+\d{3,4}", re.I)


def rform(lines: list[str]):
    """The Mathematical Compendium's entry: `### name`, then a bold statement.

    Yields (line number, name, non-blank body lines). A `###` block whose first non-blank line is
    not bold is a heading, not an entry, and is not one of these.
    """
    idx = [i for i, l in enumerate(lines) if re.match(r"^### (?!#)", l)]
    for s, e in zip(idx, idx[1:] + [len(lines)]):
        nb = [l for l in lines[s + 1:e] if l.strip()]
        if nb and nb[0].startswith("**"):
            yield s + 1, lines[s][4:].strip(), nb


def has_rform(tag: str) -> bool:
    """The R-form is the Mathematical Compendium's, and `> **Prior art` is its signature.

    The Physics Compendium also opens 27 `###` blocks with a bold line, so the shape test alone
    admits them — but its entries carry `> **Where it fails.**` and the field names `What it is`
    and `Where it comes from`, and none of the R-form's grade, scope or prior-art fields. Reading
    them with this detector would report all 27 as missing a grade they were never asked for.
    """
    lines = load(tag)
    return (any(True for _ in rform(lines))
            and any(l.lstrip().startswith("> **Prior art") for l in lines))


# ---------------------------------------------------------------- detectors

C9_WORDS = re.compile(
    r"\bnever\b|\balways\b|without exception|in every case|every configuration|at every cap",
    re.I)


def c9(tag: str) -> list[Row]:
    """C9-OVERGENERALISATION-WORD — one row per line carrying one of the six words."""
    out = []
    for i, l in enumerate(load(tag), 1):
        m = C9_WORDS.search(l)
        if m:
            out.append(Row("C9-OVERGENERALISATION-WORD", tag, i, m.group(0).lower(), l.strip()[:120]))
    return out


def c11(tag: str) -> list[Row]:
    """C11-R-FORM-INCOMPLETE — an entry missing its grade, its prior art, or both.

    The grades are Proved, Measured and Computed. `Cited`, `Definitional`, `Conditional` and
    `Asserted` name a source or a status and are not grades, which is why the census flags the
    entries that carry them.
    """
    out = []
    for ln, name, nb in rform(load(tag)):
        g = next((l for l in nb if GRADE.match(l)), None)
        pa = any(l.lstrip().startswith("> **Prior art") for l in nb)
        miss = [w for w, ok in (("grade", g is not None), ("prior-art", pa)) if not ok]
        if miss:
            out.append(Row("C11-R-FORM-INCOMPLETE", tag, ln, name, "missing: " + ", ".join(miss)))
    return out


def c10(tag: str) -> list[Row]:
    """C10-PROVED-WITHOUT-REGISTER — graded Proved with no Register pointer anywhere in the entry."""
    out = []
    for ln, name, nb in rform(load(tag)):
        g = next((l for l in nb if GRADE.match(l)), None)
        if g and g.startswith("Proved") and not REGPTR.search("\n".join(nb)):
            out.append(Row("C10-PROVED-WITHOUT-REGISTER", tag, ln, name, g.strip()[:100]))
    return out


def c6a(tag: str) -> list[Row]:
    """C6a-ENTRY-NO-SOURCE-POINTER — an entry with neither a § nor a Register pointer."""
    out = []
    for ln, name, nb in rform(load(tag)):
        body = "\n".join(nb)
        if not SEC_ANY.search(body) and not REGPTR.search(body):
            out.append(Row("C6a-ENTRY-NO-SOURCE-POINTER", tag, ln, name,
                           "no § or Register pointer in entry"))
    return out


# ------------------------------------------------- pointer resolution: C1, C2, C5

def main_sections() -> set[str]:
    """Every section the main volume defines — and not every one is a heading.

    Most are: `## N. title`, `### N.M title`, deeper. But chapter 4's ten mechanisms are a
    TABULATED LIST — `  4.1   **attributed outward before checking inward** — …` — and so are
    several others. Reading headings alone reports §4.1 to §4.10 as unresolved at 42 sites across
    main, the Register and the Mathematical Compendium, which is a fault in the reader, not the
    book. Chapter 4 says as much about its own history: *an earlier form was a heading with no
    body at all … cited as §4.1 and §4.2 throughout a book that never defined them. Register 655.*
    It has a body now, and the body is the list.
    """
    out = set()
    for l in load("main"):
        m = (re.match(r"^#{2,6} (\d+(?:\.\d+)*)\.?\s", l)
             or re.match(r"^\s{1,6}(\d+\.\d+(?:\.\d+)*)\s+\*\*", l))
        if m:
            s = m.group(1)
            out.add(s)
            while "." in s:                    # a printed §12.11.0.8 makes §12.11 resolvable
                s = s.rsplit(".", 1)[0]
                out.add(s)
    return out


SECREF = re.compile(r"(?:(\bM|\bT|\bSC|\bIoI|\bPC|\bMC)\s+)?§(\d+(?:\.\d+)*)")


def c1(tag: str, inventory: set[str] | None = None) -> list[Row]:
    """C1-SECTION-POINTER-UNRESOLVED — a bare or M-prefixed §N.M the main volume does not print.

    A `T §…` pointer addresses the companion inside Appendix G, which numbers its own sections;
    those are left alone rather than resolved against the wrong inventory.
    """
    inv = main_sections() if inventory is None else inventory
    out = []
    for i, l in enumerate(load(tag), 1):
        for pre, num in SECREF.findall(l):
            if pre in ("T", "SC", "IoI", "PC", "MC"):
                continue
            if num not in inv:
                out.append(Row("C1-SECTION-POINTER-UNRESOLVED", tag, i, "§" + num, l.strip()[:110]))
    return out


def printed_theorems() -> set[str]:
    """Theorem numbers the main volume prints as a statement, not merely cites.

    A printed theorem opens its own line and is followed at once by its statement or its tag —
    `Theorem 18.1. On a product order …`, `Theorem 14.1 (A.2). X is closed iff …`. The `[.(:]`
    is doing real work: main's only mention of Theorem 7.1 is the sentence *Theorem 7.1 is
    absent — withdrawn*, and a looser anchor reads that as the theorem being printed, which
    would silence the census's own row on it.
    """
    out = set()
    for l in load("main"):
        for m in re.finditer(r"^\s*Theorem (\d+\.\d+)\s*[.(:]|\*\*Theorem (\d+\.\d+)"
                             r"|^#{2,6}.*Theorem (\d+\.\d+)", l):
            out.add(next(g for g in m.groups() if g))
    return out


def c2(tag: str, printed: set[str] | None = None) -> list[Row]:
    """C2-THEOREM-POINTER-UNPRINTED — `Theorem N.M` cited where no such theorem is printed."""
    p = printed_theorems() if printed is None else printed
    out = []
    for i, l in enumerate(load(tag), 1):
        if l.lstrip().startswith("> **Prior art"):
            continue          # a prior-art note cites other people's theorems, not the book's
        for n in re.findall(r"Thm (\d+\.\d+)|Theorem (\d+\.\d+)", l):
            num = n[0] or n[1]
            if num not in p:
                out.append(Row("C2-THEOREM-POINTER-UNPRINTED", tag, i,
                               "Theorem " + num, l.strip()[:110]))
    return out


def register_extent() -> set[int]:
    return {int(m.group(1)) for l in load("reg")
            for m in [re.match(r"^### (\d{1,4})\s*$", l)] if m} | {
           int(x) for l in load("reg") if re.match(r"^### \d{1,4}(\s*,\s*\d{1,4})+\s*$", l)
           for x in re.findall(r"\d+", l)}


def c5(tag: str, extent: set[int] | None = None) -> list[Row]:
    """C5-REGISTER-POINTER-UNRESOLVED — a Register pointer to a number the Register does not carry."""
    ext = register_extent() if extent is None else extent
    out = []
    for i, l in enumerate(load(tag), 1):
        for m in re.finditer(r"\b(?:register|registers|entry|entries|R) (\d{2,4})\b", l, re.I):
            n = int(m.group(1))
            if n not in ext:
                out.append(Row("C5-REGISTER-POINTER-UNRESOLVED", tag, i,
                               m.group(0), l.strip()[:110]))
    return out


RUN = {
    "C9-OVERGENERALISATION-WORD":     (c9,  None),
    "C11-R-FORM-INCOMPLETE":          (c11, "rform"),
    "C10-PROVED-WITHOUT-REGISTER":    (c10, "rform"),
    "C6a-ENTRY-NO-SOURCE-POINTER":    (c6a, "rform"),
    "C1-SECTION-POINTER-UNRESOLVED":  (c1,  None),
    "C2-THEOREM-POINTER-UNPRINTED":   (c2,  None),
    "C5-REGISTER-POINTER-UNRESOLVED": (c5,  None),
}

NOT_RUN = {
    "C13-HANDLE-LEAK":
        "286 rows recorded on mc over lines 3384-3545. That window now holds 384 backticked "
        "handle occurrences over 152 lines, 250 of them distinct, and none of 384, 250, 152 or "
        "any handle set resolved against main or the Register reproduces 286. The census's own "
        "predicate is not recovered, so no detector is run.",
    "C6-NUMBERS-NOT-IN-SOURCE":
        "184 rows recorded on mc, each of the form `3 of 3: 269 271 1133 | sources § R1133` — the "
        "numbers of an entry checked against the text of the sources it cites. That requires "
        "fetching each cited source, which is the chat-81 read and not a class sweep.",
    "C8-NAMED-STATEMENT":
        "293 rows recorded against member `all`, cross-volume by construction (`sites=19 in "
        "ioi,main,mc,reg`). It is one sweep over the corpus, already run, not a per-volume class.",
    "C7-WITHDRAWAL-LINE-NUMBER-SURVIVES":
        "47 rows recorded on main. Each needs the list of withdrawn items and the line each "
        "carried before withdrawal; the corpus records the surviving numbers, not the list.",
    "C2b-THEOREM-17.1-CITED-AS-§17.1":
        "1 row, on mc L1244. A single named site, not a population.",
    "C3-FIGURE-POINTER-UNPLACED":
        "1 row, on main L7584, and it names a figure since withdrawn. A single named site.",
}

# The census's own counts, per class and volume, as at DEFECT-CENSUS.tsv.
CENSUS = {
    ("C9-OVERGENERALISATION-WORD", "main"): 219,
    ("C9-OVERGENERALISATION-WORD", "ioi"): 13,
    ("C9-OVERGENERALISATION-WORD", "pc"): 10,
    ("C9-OVERGENERALISATION-WORD", "sc"): 1,
    ("C11-R-FORM-INCOMPLETE", "mc"): 55,
    ("C10-PROVED-WITHOUT-REGISTER", "mc"): 86,
    ("C6a-ENTRY-NO-SOURCE-POINTER", "mc"): 35,
    ("C2-THEOREM-POINTER-UNPRINTED", "mc"): 4,
    ("C2-THEOREM-POINTER-UNPRINTED", "main"): 1,
    ("C2-THEOREM-POINTER-UNPRINTED", "reg"): 6,
    ("C1-SECTION-POINTER-UNRESOLVED", "ioi"): 1,
}


def selftest() -> int:
    """Every reproduction the census makes checkable, asserted."""
    bad = 0
    print("calibration — the detector against the census's own rows\n")
    for (cls, vol), want in sorted(CENSUS.items()):
        got = len(RUN[cls][0](vol))
        ok = got == want
        bad += not ok
        print(f"  {'ok  ' if ok else 'FAIL'} {cls:34} {vol:5} got {got:4}  census {want:4}")
    print("\n  not asserted, and why:")
    print("    C9 reg, C9 mc     the Register has grown by 9 entries since the census, and mc's")
    print("                      C9 rows were recorded per occurrence (38) where every other")
    print("                      volume's were per line (36). Census drift, not detector drift.")
    print("    C1 reg            6 found against 5 recorded. The sixth is at reg L6637, inside")
    print("                      entry 1799, seated by this work after the census was taken —")
    print("                      and it is the same shape as the recorded row at L6311, a bare")
    print("                      §0 that resolves in the Spectra Compendium and not in main.")
    print("    C1 mc             0 found against 2 recorded, and the two are `T §6.5` and")
    print("                      `T §5.1`. A T-pointer addresses the companion, which numbers")
    print("                      its own sections; that inventory is not separately enumerable")
    print("                      from the seated members, so the T half of C1 is NOT-RUN and")
    print("                      only the bare and M-prefixed half is swept.")
    print(f"\n{'SELFTEST OK' if not bad else str(bad) + ' FAILED'}")
    return 1 if bad else 0


def sweep(vols) -> None:
    inv, thm, ext = main_sections(), printed_theorems(), register_extent()
    print(f"main prints {len(inv)} sections and {len(thm)} theorems "
          f"({', '.join(sorted(thm))}); the Register's entries carry {len(ext)} numbers, "
          f"1 to {max(ext)}\n")
    width = max(len(c) for c in list(RUN) + list(NOT_RUN))
    for vol in vols:
        rf = has_rform(vol)
        print(f"=== {vol}  ({len(load(vol)):,} lines"
              f"{'' if rf else '; no R-form entries'})")
        for cls, (fn, need) in RUN.items():
            if need == "rform" and not rf:
                print(f"  {cls:{width}}  NOT-APPLICABLE  the volume has no R-form entry to read")
                continue
            kw = {"c1": {"inventory": inv}, "c2": {"printed": thm},
                  "c5": {"extent": ext}}.get(fn.__name__, {})
            rows = fn(vol, **kw) if kw else fn(vol)
            seen = CENSUS.get((cls, vol))
            mark = "" if seen is None else f"   census {seen}"
            print(f"  {cls:{width}}  {len(rows):5} rows{mark}")
            if cls == "C1-SECTION-POINTER-UNRESOLVED":
                print(f"  {'':{width}}         bare and M-prefixed pointers only; the T half"
                      f" (the companion's own numbering) is NOT-RUN")
        for cls in NOT_RUN:
            print(f"  {cls:{width}}  NOT-RUN")
        print()


def main(argv=None) -> int:
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    p.add_argument("--selftest", action="store_true")
    p.add_argument("--volume", action="append", choices=list(VOLUMES),
                   help="default: the four compendia of RUL-152 item 2")
    p.add_argument("--class", dest="cls", help="one class name; print its rows")
    p.add_argument("--tsv", action="store_true", help="rows in the census's own schema")
    a = p.parse_args(argv)

    if a.selftest:
        return selftest()

    vols = a.volume or list(COMPENDIA)
    if a.cls:
        if a.cls in NOT_RUN:
            print(f"{a.cls}\n  NOT-RUN — {NOT_RUN[a.cls]}")
            return 0
        fn = RUN[a.cls][0]
        if a.tsv:
            print("id\tclass\tmember\tline\titem\tdetail")
        n = 0
        for vol in vols:
            if RUN[a.cls][1] == "rform" and not has_rform(vol):
                print(f"# {vol}: NOT-APPLICABLE — no R-form entry")
                continue
            for r in fn(vol):
                n += 1
                print(f"{n}\t{r.cls}\t{r.member}\t{r.line}\t{r.item}\t{r.detail}" if a.tsv
                      else f"  {r.member:5} L{r.line:<6} {r.item:28} {r.detail[:80]}")
        return 0

    sweep(vols)
    return 0


if __name__ == "__main__":
    sys.exit(main())
