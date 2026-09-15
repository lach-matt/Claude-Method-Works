#!/usr/bin/env python3
r"""
laws.py -- A NAMED PHYSICAL LAW RUN THROUGH THE INDEX, AND THE RESIDUAL IS THE
MEASUREMENT.  Rydberg-Ritz against 596 banked spectroscopic series.

M: "If you need help identifying indexes, start running field and theory
equations through the indexes and see if they produce information." And, ruling
the scope: "First-order indexes are not limited to the contents of the corpus.
The corpus is young and growing."

    python3 laws.py             the reading
    python3 laws.py --selftest  fixtures

===============================================================================
0. THE SCOPE THIS FILE RUNS UNDER, BECAUSE IT IS NEW
===============================================================================

Every index before this one charted a table the corpus generated.  This one
charts a RESIDUAL: what a law predicts, against what the corpus banked, for each
of 596 series.  The residual is in no table -- it is produced here -- and M's
ruling is what makes that first-order rather than out of scope.

    SO THE DISCIPLINE HAS TO BE TIGHTER, NOT LOOSER.  A residual can be
    manufactured by choosing a law that fits, and the check against that is
    written into section 2: the law is named, stated in closed form, taken from
    outside this project, and its prediction is computed BEFORE any row is
    looked at.  Nothing here is fitted.

===============================================================================
1. THE LAW, AND WHY THIS ONE
===============================================================================

    RYDBERG-RITZ.  A series of levels converging on a limit has energies

        E_n = limit - R / (n - delta)^2

    where `delta` is the QUANTUM DEFECT, nearly constant along a series.  The
    quantity `n - delta` is the EFFECTIVE PRINCIPAL QUANTUM NUMBER, written n*.

        n* = n - delta

    That is the whole law used here and it has no free parameter: the corpus
    banks `n`, `delta` and `nstar` in the same row of `SPECTRA-DATA.tsv`, so the
    identity is CHECKABLE ROW BY ROW with nothing supplied from outside.

    WHY THIS LAW AND NOT A HARDER ONE.  Because it is falsifiable against data
    already present, needs no constants, and the corpus states all three terms
    independently -- `n` as an observed range, `delta` as a fitted defect,
    `nstar` as an observed bracket.  Three independent statements of a relation
    with two degrees of freedom is exactly the shape that can be checked.

===============================================================================
2. WHAT A RESIDUAL MEANS HERE, AND WHAT IT DOES NOT
===============================================================================

`n` and `nstar` are RANGES in the table -- "4-55" and "4.0-55.0" -- so the law is
checked at both ends:

        low  residual = (n_lo - delta) - nstar_lo
        high residual = (n_hi - delta) - nstar_hi

A row where both are within rounding is CONSISTENT.  A row where they are not is
NOT AN ERROR IN THE DATA, and this file never says it is.  The likely reading is
that `delta` is a single fitted value for a series whose defect drifts, so the
bracket was computed per level and the tabulated defect is a summary.  That
makes the residual a measurement of HOW WELL A SINGLE DEFECT DESCRIBES THE
SERIES, which is a real physical quantity and the thing worth indexing.

    THE VERDICTS ARE NAMED AND NOT FLATTENED:

        CONSISTENT   both ends within one unit in the last place of nstar
        DRIFTS       the two ends disagree in the same direction -- a defect
                     that changes along the series
        INCONSISTENT neither end matches and they do not drift together
        REVERSED     the n range runs high to low.  NOT a physics verdict --
                     see section 3.
        UNPARSED     a column the table does not give in numeric form

===============================================================================
3. THE LAW RECOVERED A TRUNCATED DIGIT ON ITS FIRST RUN
===============================================================================

Exactly ONE row of 596 has an n range that runs backwards:

    Ga I   4s^2 np ^2P^o high   n "41-5"   nstar "38.8-52.7"   delta +2.2107
                                levels 15

It was found as an outlier two orders of magnitude clear of the rest -- drift
49.9 against a next-worst of 0.6 -- and it is not a drift at all.  Running the
law backwards recovers what the row should say:

    n_lo = nstar_lo + delta = 38.8 + 2.2107 = 41.01
    n_hi = nstar_hi + delta = 52.7 + 2.2107 = 54.91

so the range is **41-55**, and "41-5" has lost its final character.  A SECOND,
INDEPENDENT COLUMN CONFIRMS IT: the row banks `levels` = 15, and 55 - 41 + 1 is
exactly 15.  The law and the level count agree on a digit neither of them
contains.

    RECORDED, NOT REPAIRED.  The row lives in `extracted/`, a GENERATED tree
    derived from the mirror; `CLAUDE.md` says regenerate such a tree, never
    hand-edit it, and the fault is in the source archive rather than in the
    extraction.  `reversed_rows()` names it, `reconstruct()` states the
    inference and its two independent confirmations, and nothing is written.

    AND IT IS EXCLUDED FROM THE DRIFT READING, because a lost character is not
    a defect that moves along a series.  Leaving it in put a 49.9 at the top of
    a table whose real range is 0.0 to 0.6.

===============================================================================
4. THE INDEX
===============================================================================

Members are the 596 series.  Coordinates:

        span     how many n the series covers -- n_hi - n_lo
        levels   how many levels the corpus banks for it
        drift    |high residual - low residual|, banded to the table's own
                 precision by multiplying by 10 and truncating

    `drift` IS THE ONE DERIVED COORDINATE and it is the point: it is zero when a
    single defect describes the whole series and grows as the defect moves.

===============================================================================
5. WHAT THIS FILE REFUSES
===============================================================================

To call an inconsistent row an error.  Section 2 gives the likelier reading, and
this file has not read the source literature for any row.  `lit` is a column and
most of its values are `unverified`; that is the corpus's own caution and it is
inherited here.

To fit anything.  No constant is chosen, no threshold is tuned, and the only
tolerance is one unit in the last decimal place the table itself prints.

To extend to a law the corpus does not already state all the terms of.  The
Rydberg constant does not appear here, and neither does an energy: this file
checks an identity between three banked columns and stops.
"""

import csv
import os
import sys

import hlaw
import mi

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
TABLE = "extracted/archives/method16-rp-b-data/SPECTRA-DATA.tsv"
TOL = 0.05                       # one unit in the last place nstar prints
_ROWS = None


def rows():
    global _ROWS
    if _ROWS is None:
        with open(os.path.join(ROOT, TABLE), newline="", encoding="utf-8") as f:
            _ROWS = list(csv.DictReader(f, delimiter="\t"))
    return _ROWS


def _range(s):
    """(low, high) from '4-55' or '4.0-55.0', with en-dashes honoured."""
    if not s:
        return None
    t = s.replace("–", "-").replace("—", "-").strip()
    neg = t.startswith("-")
    if neg:
        t = t[1:]
    parts = t.split("-")
    if len(parts) != 2:
        try:
            v = float(t)
            return (v, v)
        except ValueError:
            return None
    try:
        lo, hi = float(parts[0]), float(parts[1])
    except ValueError:
        return None
    return (-lo, hi) if neg else (lo, hi)


def _num(s):
    try:
        return float(str(s).replace("+", "").replace(",", "").strip())
    except (TypeError, ValueError):
        return None


def residuals(r):
    """(low residual, high residual) for one row, or None if unparseable."""
    n, ns, d = _range(r["n"]), _range(r["nstar"]), _num(r["delta"])
    if n is None or ns is None or d is None:
        return None
    return ((n[0] - d) - ns[0], (n[1] - d) - ns[1])


def is_reversed(r):
    """The n range runs high to low.  One row of 596; see section 3."""
    n = _range(r["n"])
    return n is not None and n[0] > n[1]


def reversed_rows():
    return [r for r in rows() if is_reversed(r)]


def reconstruct(r):
    """(what n should read, the two independent confirmations).

    Running the law backwards gives the endpoints; the banked `levels` count
    gives the span.  Neither contains the missing digit and they agree on it.
    """
    ns, d, lv = _range(r["nstar"]), _num(r["delta"]), _num(r["levels"])
    if ns is None or d is None:
        return None
    lo, hi = ns[0] + d, ns[1] + d
    span = None if lv is None else int(round(lo)) + int(lv) - 1
    return (int(round(lo)), int(round(hi)),
            {"from the law": (round(lo, 2), round(hi, 2)),
             "from the levels count": span,
             "they agree": span == int(round(hi))})


def verdict(r):
    """CONSISTENT / DRIFTS / INCONSISTENT / REVERSED / UNPARSED, per section 2."""
    res = residuals(r)
    if res is None:
        return "UNPARSED"
    if is_reversed(r):
        return "REVERSED"
    lo, hi = res
    if abs(lo) <= TOL and abs(hi) <= TOL:
        return "CONSISTENT"
    if abs(hi - lo) > TOL:
        return "DRIFTS"
    return "INCONSISTENT"


def census():
    """{verdict: count} over every banked series."""
    out = {}
    for r in rows():
        v = verdict(r)
        out[v] = out.get(v, 0) + 1
    return dict(sorted(out.items()))


def worst(n=10):
    """The series a single defect describes least well."""
    out = []
    for r in rows():
        res = residuals(r)
        if res is None or is_reversed(r):
            continue                        # section 3: not a drift
        out.append((abs(res[1] - res[0]), r["species"], r["channel"],
                    r["n"], r["delta"], r["nstar"]))
    return sorted(out, reverse=True)[:n]


def exact():
    """Rows where BOTH ends land exactly, to the table's printed precision.

    The control: if the identity held nowhere the parser would be wrong, and if
    it held everywhere there would be nothing to index.
    """
    return [r for r in rows() if verdict(r) == "CONSISTENT"]


def index():
    """(span, levels, drift band) per series."""
    out = set()
    for r in rows():
        res = residuals(r)
        n = _range(r["n"])
        lv = _num(r["levels"])
        if res is None or n is None or lv is None or is_reversed(r):
            continue
        out.add((int(n[1] - n[0]), int(lv), int(abs(res[1] - res[0]) * 10)))
    return frozenset(out)


def unparsed():
    return [r for r in rows() if residuals(r) is None]


def criterion():
    X = index()
    lifted = frozenset(t + (t[0],) for t in X)
    return {"K": 0 if mi.K(X) == mi.K(lifted) else 1,
            "height": 0 if mi.height(X) == mi.height(lifted) else 1,
            "width": 0 if mi.width(X) == mi.width(lifted) else 1}


def closers():
    X = index()
    cl, _b = hlaw.closures(X)
    return sorted(L for L in hlaw.LANGS if len(cl[L]) == len(X))


def cell():
    return mi.cell(index())


# ---------------------------------------------------------------------------

def report():
    print("=" * 74)
    print("RYDBERG-RITZ RUN THROUGH THE INDEX, AND THE RESIDUAL IS THE")
    print("MEASUREMENT")
    print("=" * 74)
    print()
    print("1. THE LAW.  n* = n - delta.  No free parameter, and the corpus")
    print("   banks all three terms independently in the same row.")
    print("   series banked   %d" % len(rows()))
    print("   unparsed        %d" % len(unparsed()))
    print()
    print("2. THE CENSUS.")
    for v, c in census().items():
        print("   %-14s %4d" % (v, c))
    print("   CONSISTENT means both ends land within %.2f -- one unit in the" % TOL)
    print("   last place nstar prints. It is a control as much as a result: if")
    print("   the identity held nowhere the parser would be wrong, and if it")
    print("   held everywhere there would be nothing to index.")
    print()
    rv = reversed_rows()
    print("3. THE LAW RECOVERED A TRUNCATED DIGIT.")
    print("   rows whose n range runs backwards: %d of %d" % (len(rv), len(rows())))
    for r in rv:
        rec = reconstruct(r)
        print("   %s  %s" % (r["species"], r["channel"]))
        print("      banked      n %s   nstar %s   delta %s   levels %s"
              % (r["n"], r["nstar"], r["delta"], r["levels"]))
        print("      from the law            n %s-%s" % (rec[0], rec[1]))
        print("      from the levels count   n ends at %s"
              % rec[2]["from the levels count"])
        print("      the two agree: %s   -- so the range is %d-%d and the"
              % (rec[2]["they agree"], rec[0], rec[1]))
        print("      banked string has lost its final character.")
    print("   RECORDED, NOT REPAIRED. The row is in extracted/, a GENERATED")
    print("   tree; CLAUDE.md says regenerate, never hand-edit, and the fault")
    print("   is in the source archive rather than the extraction. It is also")
    print("   EXCLUDED from the drift table below: a lost character is not a")
    print("   defect that moves along a series.")
    print()
    print("4. WHERE A SINGLE DEFECT DESCRIBES THE SERIES LEAST WELL.")
    print("   %-9s %-22s %-9s %-9s %s"
          % ("drift", "species", "channel", "n", "delta"))
    for d, sp, ch, n, de, _ns in worst():
        print("   %-9.3f %-22s %-9s %-9s %s" % (d, sp, ch[:20], n, de))
    print("   NOT AN ERROR IN THE DATA. The likely reading is a defect that")
    print("   moves along the series while the table prints one fitted value,")
    print("   which makes the residual a measurement of how well a single")
    print("   defect describes it -- a real quantity, and the one worth")
    print("   indexing.")
    print()
    print("5. THE INDEX IT MAKES.")
    print("   members    %d series" % len([r for r in rows()
                                           if residuals(r) is not None]))
    print("   cells      %d" % len(index()))
    crit = criterion()
    print("   criterion  K %d  height %d  width %d"
          % (crit["K"], crit["height"], crit["width"]))
    if any(crit.values()):
        print("   A COORDINATE MOVED. The reading below is void.")
        return 1
    print("   closes     %s" % (", ".join(closers()) or "nothing"))
    print("   CELL       %s" % (cell(),))
    print()
    print("6. REFUSED: to call an inconsistent row an error -- the `lit` column")
    print("   says `unverified` for most rows and that caution is inherited.")
    print("   To fit anything: no constant chosen, no threshold tuned, and the")
    print("   only tolerance is the table's own printed precision. To extend to")
    print("   a law whose terms the corpus does not already state.")
    return 0


def selftest():
    ok = True

    def chk(lab, got, want):
        nonlocal ok
        good = got == want
        ok &= good
        print("  [%s] %-54s %s" % ("ok" if good else "XX", lab,
                                   got if good else "%s != %s" % (got, want)))

    chk("the table is 596 series", len(rows()), 596)
    # the parser, on forms the table actually contains
    chk("an integer range parses", _range("4-55"), (4.0, 55.0))
    chk("a decimal range parses", _range("2.2-14.2"), (2.2, 14.2))
    chk("an en-dash range parses", _range("4–55"), (4.0, 55.0))
    chk("a bare number is a degenerate range", _range("7"), (7.0, 7.0))
    chk("a signed defect parses", _num("+1.7670"), 1.767)
    chk("a comma-grouped number parses", _num("48,278.480"), 48278.48)
    chk("nonsense does not parse", _num("published"), None)

    # THE WORKED CASE FROM THE TABLE'S OWN THIRD ROW, computed by hand:
    # n 4-16, delta +1.7670, nstar 2.2-14.2.  4 - 1.767 = 2.233, and
    # 16 - 1.767 = 14.233.  Both within a rounding of the printed bracket.
    r3 = next(r for r in rows()
              if r["species"] == "Al I" and r["n"] == "4–16")
    lo, hi = residuals(r3)
    chk("the worked row's low residual is a rounding", abs(lo) <= TOL, True)
    chk("and its high residual is too", abs(hi) <= TOL, True)
    chk("so it is CONSISTENT", verdict(r3), "CONSISTENT")

    # THE RECOVERED DIGIT
    rv = reversed_rows()
    chk("exactly one row runs backwards", len(rv), 1)
    chk("and it is the Ga I high series", rv[0]["species"], "Ga I")
    rec = reconstruct(rv[0])
    chk("the law puts its range at 41-55", (rec[0], rec[1]), (41, 55))
    chk("the levels count independently ends it at 55",
        rec[2]["from the levels count"], 55)
    chk("the two agree on a digit neither contains", rec[2]["they agree"], True)
    chk("the banked string has lost a character", rv[0]["n"],
        "41\u20135")
    chk("it is verdicted REVERSED, not DRIFTS", verdict(rv[0]), "REVERSED")
    chk("and it is excluded from the drift table",
        [x for x in worst(20) if x[1] == "Ga I" and "high" in x[2]], [])

    c = census()
    chk("every row got a verdict", sum(c.values()), len(rows()))
    chk("some rows are CONSISTENT", c.get("CONSISTENT", 0) > 0, True)
    chk("the law does NOT hold everywhere", c.get("CONSISTENT", 0) < len(rows()),
        True)
    chk("no verdict is outside the named five",
        sorted(set(c) - {"CONSISTENT", "DRIFTS", "INCONSISTENT", "REVERSED",
                         "UNPARSED"}), [])
    chk("drift is symmetric in the two ends",
        abs(residuals(r3)[1] - residuals(r3)[0])
        == abs(residuals(r3)[0] - residuals(r3)[1]), True)
    w = worst(5)
    chk("the worst list is ordered", [x[0] for x in w],
        sorted([x[0] for x in w], reverse=True))
    X = index()
    chk("the index is non-empty", len(X) > 0, True)
    crit = criterion()
    chk("K admissible", crit["K"], 0)
    chk("height admissible", crit["height"], 0)
    chk("width admissible", crit["width"], 0)
    cl = cell()
    chk("the cell is a 3-tuple", len(cl), 3)
    chk("height and width bound the size",
        max(cl[1], cl[2]) <= len(X) <= cl[1] * cl[2], True)
    print("laws selftest: %s" % ("PASS" if ok else "FAIL"))
    return ok


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    sys.exit(report())
