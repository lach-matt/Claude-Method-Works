#!/usr/bin/env python3
"""provenance.py -- what every number in the design rests on.

The design's mathematics is exact. Every relation in this repository is
either a theorem or arithmetic: P = I.E, F = k/(nu(1-k)), G = N.V.eta/E_pi,
k_eff = k_inf/(1 + M2 B2). Worked to any precision you like, they stay exact.

WHAT IS NOT EXACT, AND WHAT THE MATHEMATICS DOES NOT CONTAIN, IS ITS OWN
CONSTANTS. nu = 2.9 is a measurement. The 25 to 30 neutrons per GeV deposited
is a measurement. eta_acc is a band across real machines. The driver's
standby load is not a measurement at all, and explore.py has just shown that
one un-measured constant carries more consequence than every free design
choice put together.

So this censuses them. It reads the design instruments, finds every
module-level constant, and reports what each one's own file says it rests on:

  SOURCED       a published measurement
  DERIVED       computed from others rather than stated
  ASSUMED       a value chosen because one was needed
  RECONSTRUCTED measured out of the corpus rather than out of the world
  DESIGN        a decision, with its reason recorded elsewhere
  UNANNOTATED   this census cannot tell

UNANNOTATED IS NOT A FINDING OF ABSENCE. Many are conversions and exact
definitions -- seconds in a year, atoms in a kilogram -- which have no
provenance to state because they are not measurements. The census says how
many it cannot classify and never calls one unmeasured. What it does report
as a finding is the ASSUMED inventory, and which of those explore.py has
already put an axis on, because the residue is where the next exposure is.

Stdlib only. python3 tools/provenance.py [--assumed] [--selftest]
"""

import argparse
import ast
import collections
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))

# THE DESIGN INSTRUMENTS. Not every .py here: the corpus tools (cypher,
# arith, pointers, buildtrace, populate, coverage, orderideal) census The
# Method's own volumes and hold no design constant, and the paper harness
# (verify_paper, render_paper, audit_paper, figures) reads a ledger rather
# than stating physics. Including them would inflate the denominator with
# files that have nothing to be measured about.
INSTRUMENTS = (
    "powersource.py", "materials.py", "collector.py", "machine.py",
    "criticality.py", "fuelchoice.py", "startcost.py", "restart.py",
    "buildpackage.py", "environment.py", "window.py", "mucf.py",
)

# Order matters: the first pattern that matches a constant's annotation wins,
# and a value that is both derived and assumed is ASSUMED, because the weaker
# claim governs. A STATUS IS NEVER FLATTENED UPWARDS.
CLASSES = (
    ("ASSUMED", re.compile(r"\bASSUMED\b")),
    ("RECONSTRUCTED", re.compile(r"\bRECONSTRUCTED\b|\bRECOVERED\b")),
    ("SOURCED", re.compile(r"\bSOURCED\b|\bMEASURED\b|\bPUBLISHED\b")),
    ("DERIVED", re.compile(r"\bDERIVED\b|\bIMPORTED\b")),
    ("DESIGN", re.compile(r"\bDESIGN\b|\bDECIDED\b|\bADOPTED\b")),
)
UNANNOTATED = "UNANNOTATED"
BLOCK_LINES = 4        # a dedicated note is short; see _annotation()

Const = collections.namedtuple("Const", "file name lineno status annotation")


def _annotation(lines, lineno, end_lineno=None):
    """(the constant's OWN comment, the block above it).

    Both styles are in use here -- a trailing '# SOURCED band' and a
    paragraph above the assignment -- and they are NOT the same evidence. The
    trailing comment and the comments inside a multi-line value belong to
    THIS constant; the paragraph above usually introduces a group and is full
    of ordinary prose. So they are returned apart and the classifier reads
    the constant's own words first. Reading them together let a paragraph
    that merely discussed the design overrule a value's stated source, which
    is how SPALL_TARGET_MW -- every row of it marked SOURCED -- came back
    graded DESIGN."""
    own = []
    line = lines[lineno - 1]
    if "#" in line:
        own.append(line.split("#", 1)[1])
    last = end_lineno or lineno
    for j in range(lineno, min(last, len(lines))):
        if "#" in lines[j]:
            own.append(lines[j].split("#", 1)[1])
    # THE BLOCK IS CAPPED, and the cap is the second thing this had to
    # learn. An unbounded walk upwards swallows whole explanatory paragraphs,
    # and a paragraph that merely DISCUSSES an assumption then grades the
    # next constant as one: LINAC_CLASS, a table every row of which is
    # sourced, came back ASSUMED because the paragraph introducing
    # LINAC_BEAM_MW sits above it. A dedicated note is short. An essay is
    # context for a section, not an annotation of one value.
    block = []
    i = lineno - 2
    while i >= 0 and lines[i].lstrip().startswith("#") \
            and len(block) < BLOCK_LINES:
        block.append(lines[i].lstrip()[1:])
        i -= 1
    if i >= 0 and lines[i].lstrip().startswith("#"):
        return " ".join(own).strip(), ""      # an essay: not this value's
    return " ".join(own).strip(), " ".join(reversed(block)).strip()


def classify(own, block=""):
    """The constant's own words decide; the block above is the fallback."""
    for text in (own, block):
        for name, pat in CLASSES:
            if pat.search(text):
                return name
    return UNANNOTATED


def constants(filename):
    """Every module-level constant in one instrument, with its status."""
    path = os.path.join(HERE, filename)
    with open(path, encoding="utf-8") as fh:
        src = fh.read()
    lines = src.splitlines()
    tree = ast.parse(src, filename)
    out = []
    for node in tree.body:
        if not isinstance(node, ast.Assign):
            continue
        for tgt in node.targets:
            names = ([e.id for e in tgt.elts if isinstance(e, ast.Name)]
                     if isinstance(tgt, (ast.Tuple, ast.List))
                     else [tgt.id] if isinstance(tgt, ast.Name) else [])
            for nm in names:
                if not re.fullmatch(r"[A-Z][A-Z0-9_]*", nm):
                    continue
                own, block = _annotation(
                    lines, node.lineno, getattr(node, "end_lineno", None))
                out.append(Const(filename, nm, node.lineno,
                                 classify(own, block),
                                 (own + " || " + block).strip()))
    return out


def census():
    rows = []
    for f in INSTRUMENTS:
        rows.extend(constants(f))
    return rows


def by_status(rows=None):
    rows = census() if rows is None else rows
    c = collections.Counter(r.status for r in rows)
    return c


def assumed(rows=None):
    rows = census() if rows is None else rows
    return [r for r in rows if r.status == "ASSUMED"]


def _explore_axis_keys():
    sys.path.insert(0, HERE)
    import explore as E
    return E, {a.key for a in E.AXES}


# WHICH CONSTANT EACH OF explore.py's AXES ACTUALLY MOVES. Stated here rather
# than inferred, because an axis is a keyword argument and a constant is a
# module global, and nothing mechanical connects the two. A row with no
# constant is an axis that varies a function argument the design point
# supplies, and it is marked so rather than left blank.
AXIS_CONSTANT = {
    "k_eff": ("powersource.py", "K_DESIGN"),
    "eta_acc": ("powersource.py", "ETA_ACC_HI"),
    "linac_mw": ("powersource.py", "LINAC_BEAM_MW"),
    "standby_kw": ("powersource.py", "REF_STANDBY_KW"),
    "window": ("powersource.py", "STATION_WINDOW_MEV"),
    "module_mw": ("powersource.py", "MODULE_BEAM_MW"),
    "y_fus": (None, None),
}


def axis_provenance():
    """explore.py's axes, in its own ranked order, with what each rests on.

    THIS IS THE CROSS THE TWO FILES COULD NOT MAKE ALONE. explore.py ranks
    the axes by how much they move the answer and says nothing about what
    they rest on; this census says what each rests on and nothing about which
    matter. Neither is the finding. The finding is the join."""
    E, _keys = _explore_axis_keys()
    idx = {(r.file, r.name): r for r in census()}
    out = []
    for ax in sorted(E.AXES, key=lambda a: -E.swing(a)):
        f, n = AXIS_CONSTANT.get(ax.key, (None, None))
        row = idx.get((f, n)) if f else None
        out.append((ax, E.swing(ax), n, row.status if row else "n/a"))
    return out


def assumed_without_axis():
    """ASSUMED constants that explore.py has NOT put an axis on.

    This is the residue, and it is the point of running the census beside the
    search: explore.py measured the exposure of seven axes it was given, and
    the honest question is how many more there are."""
    _E, keys = _explore_axis_keys()
    covered = {AXIS_CONSTANT[k][1] for k in keys if AXIS_CONSTANT.get(k)}
    return [r for r in assumed() if r.name not in covered]


def report():
    rows = census()
    counts = by_status(rows)
    total = len(rows)
    print()
    print("  WHAT EVERY NUMBER IN THE DESIGN RESTS ON")
    print()
    print("    The mathematics is exact. Every relation in this work is a")
    print("    theorem or arithmetic, and worked to any precision it stays")
    print("    exact. WHAT THE MATHEMATICS DOES NOT CONTAIN IS ITS OWN")
    print("    CONSTANTS, and this is the inventory of those.")
    print()
    print(f"    {total} module-level constants across"
          f" {len(INSTRUMENTS)} design instruments.")
    print()
    print("      status            count    share")
    for name in ("SOURCED", "DERIVED", "DESIGN", "RECONSTRUCTED", "ASSUMED",
                 UNANNOTATED):
        n = counts.get(name, 0)
        print(f"      {name:<16} {n:6d} {100.0 * n / total:7.1f} %")
    print()
    print("    UNANNOTATED IS NOT A FINDING OF ABSENCE, and may not be read")
    print("    as one. Most are conversions and exact definitions -- seconds")
    print("    in a year, atoms in a kilogram, atomic masses -- which have no")
    print("    provenance to state because they are not measurements. This")
    print("    census says only that it cannot classify them.")
    print()
    print("    PER INSTRUMENT")
    print()
    print("      instrument            total  SOURCED  ASSUMED  unannotated")
    for f in INSTRUMENTS:
        rs = [r for r in rows if r.file == f]
        c = collections.Counter(r.status for r in rs)
        print(f"      {f:<20} {len(rs):6d} {c.get('SOURCED', 0):8d}"
              f" {c.get('ASSUMED', 0):8d} {c.get(UNANNOTATED, 0):12d}")
    print()
    print("    THE AXES THAT MOVE THE ANSWER, AND WHAT THEY REST ON")
    print()
    print("    explore.py ranks the axes and says nothing about what they")
    print("    rest on. This census says what they rest on and nothing about")
    print("    which matter. NEITHER IS THE FINDING. The join is:")
    print()
    print("      axis                    swing   constant"
          "                provenance")
    for ax, sw, nm, stt in axis_provenance():
        flag = "   <--" if stt == UNANNOTATED else ""
        print(f"      {ax.name:<22} {sw:7.2f}x  {str(nm):<22} {stt}{flag}")
    bad = [t for t in axis_provenance() if t[3] == UNANNOTATED]
    print()
    print(f"    {len(bad)} OF THE AXES THAT MOVE THIS PLANT REST ON A CONSTANT")
    print("    THAT CARRIES NO PROVENANCE AT ALL -- not SOURCED, not ASSUMED,")
    print("    nothing. They were invisible to the ASSUMED inventory below")
    print("    precisely because nobody wrote ASSUMED beside them, which is")
    print("    the failure mode an inventory of stated assumptions has and")
    print("    cannot fix from the inside.")
    print()
    print("    The sharpest of them is the driver standby. explore.py's")
    print("    largest interaction runs through it -- 19.25x against a")
    print("    product of 1.93 -- its band's low end says SOURCED, and the")
    print("    value the whole design actually uses says only 'mid-band")
    print("    driver fixed load'. A mid-point of a sourced band is not")
    print("    itself sourced, and the file had not said which it was.")
    print()
    print("    THE ASSUMED INVENTORY, WHICH IS THE SECOND FINDING")
    print()
    _E, keys = _explore_axis_keys()
    covered = {AXIS_CONSTANT[k][1] for k in keys if AXIS_CONSTANT.get(k)}
    for r in sorted(assumed(), key=lambda r: (r.file, r.name)):
        mark = "  <- explore.py has an axis on this" if r.name in covered \
            else ""
        print(f"      {r.file:<18} {r.name}{mark}")
    resid = assumed_without_axis()
    print()
    print(f"    {len(assumed())} constants are ASSUMED."
          f" explore.py has an axis on {len(assumed()) - len(resid)}.")
    print(f"    THE RESIDUE IS {len(resid)}, and that is the answer to the")
    print("    question explore.py could not ask of itself: it measured the")
    print("    exposure of the axes it was given, and there are more.")
    print()
    print("    THAT DOES NOT MAKE THE RESIDUE 19x EACH. Most of these do not")
    print("    reach the beam at all -- they set an inventory, a schedule or")
    print("    a margin rather than the balance. What it makes them is")
    print("    CANDIDATES, and each has to be put on an axis to be priced.")
    print("    None of them is priced here, because guessing which matter is")
    print("    the error this whole census exists to stop.")
    print()
    print("    AND THE READING THAT MATTERS FOR THE PROJECT: precision in the")
    print("    mathematics is worth 1.45x, which is explore.py's redesign")
    print("    ceiling. Provenance in the constants is worth the plant. They")
    print("    are not the same quantity and no amount of the first supplies")
    print("    the second -- absolute precision applied to a number nobody")
    print("    measured returns a precisely wrong answer, with more")
    print("    confidence attached to it than it had before.")
    print()


def report_assumed():
    """the ASSUMED inventory alone, with each constant's own words"""
    print()
    print("  EVERY ASSUMED CONSTANT, IN ITS OWN FILE'S WORDS")
    print()
    for r in sorted(assumed(), key=lambda r: (r.file, r.name)):
        ann = re.sub(r"\s+", " ", r.annotation).strip()
        if len(ann) > 180:
            ann = ann[:177] + "..."
        print(f"    {r.file}:{r.lineno}  {r.name}")
        print(f"      {ann}")
        print()


def selftest():
    fail = 0

    def check(label, ok):
        nonlocal fail
        if not ok:
            fail += 1
        print(f"  {label:<64} {'PASS' if ok else 'FAIL'}")

    rows = census()
    print()
    print("  the census reads what is there")
    check("every design instrument is read",
          {r.file for r in rows} == set(INSTRUMENTS))
    check("the census is large enough to be a census", len(rows) > 300)
    check("every row carries one of the known statuses",
          all(r.status in {n for n, _p in CLASSES} | {UNANNOTATED}
              for r in rows))

    print()
    print("  the classifier, on constants whose status is known by hand")
    known = {("materials.py", "SALT_RESIDENCE_S"): "ASSUMED",
             ("materials.py", "SALT_RHO"): "SOURCED",
             ("powersource.py", "LINAC_BEAM_MW"): "ASSUMED",
             ("powersource.py", "K_DESIGN"): "DERIVED",
             ("powersource.py", "SPALL_TARGET_MW"): "SOURCED"}
    idx = {(r.file, r.name): r.status for r in rows}
    for key, want in known.items():
        check(f"{key[1]} reads as {want}", idx.get(key) == want)
    # BOTH COMMENT STYLES, because reading only one would silently
    # under-report the other file's whole convention.
    check("a trailing-comment annotation is read",
          idx[("materials.py", "SALT_DT_K")] == "ASSUMED")
    check("a block-comment annotation above the line is read",
          idx[("powersource.py", "MODULE_BEAM_MW")] == "SOURCED")

    print()
    print("  a status is never flattened upwards")
    check("ASSUMED beats DERIVED where a comment carries both",
          classify("DERIVED from the above, but the input is ASSUMED")
          == "ASSUMED")
    check("SOURCED does not override ASSUMED", classify("SOURCED ASSUMED")
          == "ASSUMED")
    check("an empty annotation is UNANNOTATED and not SOURCED",
          classify("") == UNANNOTATED)
    # THE FAULT THIS SPLIT REPAIRS, constructed so it cannot come back.
    check("a constant's OWN word beats a paragraph above it",
          classify("SOURCED band", "a long DESIGN discussion above")
          == "SOURCED")
    check("  -- and the paragraph is still the fallback when it is silent",
          classify("kg/m3", "this whole group is ASSUMED") == "ASSUMED")

    print()
    print("  the residue against explore.py")
    _E, keys = _explore_axis_keys()
    check("every explore axis is mapped to a constant or explicitly to none",
          keys <= set(AXIS_CONSTANT))
    check("the mapped constants exist in the census",
          all(any(r.file == f and r.name == n for r in rows)
              for f, n in AXIS_CONSTANT.values() if f))
    resid = assumed_without_axis()
    check("there are ASSUMED constants explore.py has no axis on",
          len(resid) > 0)
    check("  -- and they are a strict subset of the ASSUMED inventory",
          0 < len(resid) <= len(assumed()))

    print()
    print("  the join with explore.py, which is the point of the file")
    rows_ax = axis_provenance()
    check("every axis is joined to a provenance or to n/a",
          len(rows_ax) == len(_E.AXES))
    check("the ranking order is explore's own",
          [t[1] for t in rows_ax] == sorted([t[1] for t in rows_ax],
                                            reverse=True))
    unann = [t for t in rows_ax if t[3] == UNANNOTATED]
    check("some axis that moves the plant rests on an UNANNOTATED constant",
          len(unann) > 0)
    check("  -- the driver standby among them, which carries the largest"
          " interaction",
          any(t[2] == "REF_STANDBY_KW" for t in unann))
    check("  -- and none of those appears in the ASSUMED inventory",
          not any(t[2] in {r.name for r in assumed()} for t in unann))

    print()
    print("  the refusals")
    import contextlib
    import io
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        report()
    out = buf.getvalue()
    check("UNANNOTATED is stated not to be a finding of absence",
          "NOT A FINDING OF ABSENCE" in out)
    check("the residue is not priced", "None of them is priced here" in out)
    check("  -- and the reason is given", "guessing which matter" in out)
    check("the report renders", len(out) > 2000)

    print()
    print(f"selftest: {fail} failures -> {'PASS' if fail == 0 else 'FAIL'}")
    return 1 if fail else 0


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--selftest", action="store_true")
    ap.add_argument("--assumed", action="store_true",
                    help=report_assumed.__doc__)
    a = ap.parse_args()
    if a.selftest:
        return selftest()
    if a.assumed:
        return report_assumed()
    return report()


if __name__ == "__main__":
    sys.exit(main())
