#!/usr/bin/env python3
r"""deformed.py -- DOCKET 36.  A REFUSAL, AND A PROOF THAT IT IS THE RIGHT ONE.

    python3 deformed.py             the reading
    python3 deformed.py --selftest  fixtures

===============================================================================
0. WHAT WAS WANTED, AND WHY FOUR ATTEMPTS AT IT WERE ALL DOOMED
===============================================================================

`nucbands.py` (DOCKET 35) seated the magnetic and antimagnetic rotational
bands.  The OTHER paper the same join returned -- arXiv:2508.05447, Pinky,
Kumar, Singh & Jain, "Features of Two-Quasiparticle Rotational Bands in
Deformed Odd-Odd Nuclei, 156 <= A <= 168" -- is the closer match to the
candidate `subpop.py` named: a DEFORMED rotor's Goldstone tower, not the
shears mechanism of near-spherical nuclei.

FOUR PARSES WERE WRITTEN AND ALL FOUR CAME UP SHORT: 154, 176, 160 and 195
entries against the paper's stated 234.  Each fix was a better guess at the
line shapes, and each new guess moved the number without explaining the gap.
THAT IS THE SHAPE OF FITTING A PARSER TO A TARGET, which is the same fault
DOCKET 23 refused when it threw out three K4 charts found by searching for K4.

SO THIS FILE WORKS BACKWARDS INSTEAD -- from the output wanted, to the input
held -- and the answer falls out in one step.

===============================================================================
1. THE DOCUMENT DEFINES ITS OWN DELIMITER, AND IT IS NOT THE ONE I WAS USING
===============================================================================

The paper's EXPLANATION OF TABLE 3 says, in its own words:

    "A single blank row separates the entries for each band.  The number in
     the first column indicates the band number."

The delimiter is A BLANK ROW.  Every parse above instead reconstructed entry
boundaries from the band-number column, because that column is what a reader
sees -- and that column is bare one- and two-digit integers alone on a line,
typographically identical to page numbers, wrapped superscripts and the
comment column's own numbered markers.  It was a PROXY for the real delimiter,
and a bad one.

===============================================================================
2. AND THE REAL DELIMITER IS NOT IN THIS FILE.  MEASURED THREE WAYS.
===============================================================================

    REQUIRED.  234 entries spread over 24 nuclide sections need 210 separators
    between entries of the same nuclide.

    PRESENT.  The table region holds 71 blank lines in total.  22 of them sit
    at a page break -- a page number, a blank, then the repeated column
    header.  That leaves AT MOST 49 that could be entry separators, against
    210 required.  Even granting every one of them, the file is four times
    short.

    DIRECT.  At the 156-Ho entry 1 -> entry 2 boundary, where the
    specification requires a blank row, THERE IS NONE: the comment text of
    entry 1 runs straight into the line `2 `.

THE PDF-TO-TEXT EXTRACTION COLLAPSED THE BLANK ROWS.  The information that
segments this table was destroyed before the file reached this repository, and
no regex recovers a delimiter that is not there.  That is not a limitation of
the four parses; it is the reason all four failed, and it is why a fifth would
fail too.

===============================================================================
3. WHAT IS RECOVERABLE, WHICH IS NOT NOTHING
===============================================================================

    THE NUCLIDE SECTIONS ARE CLEAN.  24 of them, with Z and N for every one --
    Ho x8 (N 89..103), Tm x11 (N 87..107), Lu x5 (N 89..97).  Those resolve
    from the A / Z / N / symbol block and do not depend on the lost delimiter.

    THE LEVEL ROWS ARE CLEAN.  Level rows come out once the wrapped parity
    superscript is rejoined and RELATIVE energies are admitted -- this table
    writes bandheads as `A+134.27` and `1135.7+y`, which no absolute-energy
    token matches, and that alone was one of the four parses' losses.

WHAT CANNOT BE RECOVERED IS WHICH LEVELS BELONG TO WHICH BAND.  A level
without its band is still a quantum object carrying I and pi -- but the census
that would show the capture TOTAL is a census of BANDS, and without the
delimiter there is no way to show that the levels are all of them either.  A
capture that cannot be shown total is not seated.

===============================================================================
4. WHAT WOULD SETTLE IT
===============================================================================

AN EXTRACTION THAT PRESERVES LAYOUT.  The blank rows exist in the PDF; they
were lost in the conversion to text.  Any extraction that keeps blank rows, or
keeps the x-positions of the columns so the band-number column can be told
from a page number by POSITION rather than by shape, makes this table
parseable and this docket closeable.

That is not available here: arXiv is 403 through this egress proxy, exactly as
ENSDF is, and the connector that reached the content returns this same
extraction.  The docket is OPEN ON AN INPUT, not on an idea -- which is a
different thing from the four closed routes `subpop.py` records, and is why it
is written down rather than retried.
"""

import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "captures", "arxiv-2508.05447.txt")

PAPER = ("arXiv:2508.05447 -- Pinky, Kumar, Singh & Jain, Features of "
         "Two-Quasiparticle Rotational Bands in Deformed Odd-Odd Nuclei")

# The paper's own census, from its abstract and its conclusions.
STATED = {"entries": 234, "bands": 173, "bandheads": 61, "gm_doublets": 63,
          "signature_splitting": 76, "signature_inversion": 29,
          "band_crossings": 10}

# The sentence this whole docket turns on, quoted from EXPLANATION OF TABLE 3.
SPEC = "A single blank row separates the entries for each band"

# The four forward parses, recorded so a fifth is not written by accident.
ATTEMPTS = (
    ("segment on the symbol/'S.No.' header pair", 154,
     "found only 20 of the 24 nuclide sections"),
    ("track S.No. as one stream across page breaks", 176,
     "a stray integer desynchronises a whole nuclide"),
    ("add the parity rejoin and relative energies", 160,
     "recovers level rows, does not recover entry boundaries"),
    ("relax the S.No. sequence to tolerate one gap", 195,
     "admits spurious entries; split 120/75 against 173/61"),
)

SY = {"Ho", "Er", "Tm", "Yb", "Lu", "Dy", "Tb", "Gd"}
PARITY = re.compile(r'^[\(\)]*[+−-][\)\(]*$')
ENER = (r'\(?(?:[A-Za-z]\s*\+\s*)?\d+(?:\.\d+)?(?:\s*\+\s*[A-Za-z])?\)?'
        r'|\(?[A-Za-z]\)?|\(A[<>]\d+\)\?')
SPIN = r'\(?\d{1,2}(?:/2)?[\(\)]*[+−-]?[\(\)]*\)?'
ROW = re.compile(r'^(%s)\s+(%s)(\s|$)' % (ENER, SPIN))

_C = {}


def table():
    """The lines of TABLE 3, blank rows and all -- nothing is stripped."""
    if "t" not in _C:
        raw = open(SRC, encoding="utf-8").read().split("\n")
        i0 = max(i for i, s in enumerate(raw)
                 if s.startswith("TABLE 3: Two-quasiparticle"))
        _C["t"] = raw[i0:]
    return _C["t"]


def spec_is_stated():
    """The paper's own delimiter, quoted out of its Explanation of Table 3."""
    return SPEC in open(SRC, encoding="utf-8").read()


def sections():
    """[(line, symbol, Z, N)] -- the nuclide blocks, which DO resolve."""
    b = table()
    out = []
    for k, s in enumerate(b):
        if s.strip() not in SY:
            continue
        prev = [b[j].strip() for j in range(k - 1, max(k - 6, -1), -1)
                if b[j].strip()][:2]
        nums = []
        for p in prev:
            if re.fullmatch(r'[\d ]+', p):
                nums += [int(x) for x in re.findall(r'\d+', p)]
        Z = [n for n in nums if 60 <= n <= 75]
        N = [n for n in nums if 80 <= n <= 115]
        if Z and N:
            out.append((k, s.strip(), Z[0], N[0]))
    return out


def separators():
    """(required, blank lines present, at a page break, available).

    THE WHOLE DOCKET IS THIS FUNCTION.  234 entries over 24 nuclides need 210
    separators between entries of one nuclide; the file holds 71 blank lines
    and most of what is left after the page breaks is nowhere near enough.
    """
    b = table()
    blanks = [k for k, s in enumerate(b) if not s.strip()]
    page = 0
    for k in blanks:
        nxt = next((b[j].strip() for j in range(k + 1, min(k + 4, len(b)))
                    if b[j].strip()), "")
        prv = next((b[j].strip() for j in range(k - 1, max(k - 4, -1), -1)
                    if b[j].strip()), "")
        if nxt.startswith("S.No.") or re.fullmatch(r'\d{1,3}', prv):
            page += 1
    required = STATED["entries"] - len(sections())
    return (required, len(blanks), page, len(blanks) - page)


def boundary_has_no_blank():
    """The 156-Ho entry 1 -> 2 boundary, where the spec requires a blank row."""
    b = table()
    j = next(k for k, s in enumerate(b) if s.strip() == "2" and 5 < k < 60)
    window = b[max(j - 6, 0):j]
    return not any(not s.strip() for s in window)


def _rejoin(lines):
    out, i = [], 0
    while i < len(lines):
        s = lines[i].strip()
        if out and PARITY.match(s):
            out[-1] += s
            nxt = lines[i + 1].strip() if i + 1 < len(lines) else ""
            if nxt.startswith(")"):
                out[-1] += nxt
                i += 2
                continue
            i += 1
            continue
        if out and s.startswith(")"):
            out[-1] += s
            i += 1
            continue
        out.append(s)
        i += 1
    return out


def _is_row(s):
    m = ROW.match(s)
    if not m:
        return None
    sp = m.group(2)
    if "." in sp or not re.search(r'\d', sp):
        return None
    return (m.group(1), sp)


def levels():
    """Every level row the table yields, WITHOUT band membership.

    Recoverable because a level row does not depend on the lost delimiter.
    Useless as an index, because the census that would show it total is a
    census of BANDS.
    """
    if "l" not in _C:
        b = table()
        secs = sections()
        bounds = [s[0] for s in secs] + [len(b)]
        out = []
        for i, (k, sym, Z, N) in enumerate(secs):
            for s in _rejoin(b[k:bounds[i + 1]]):
                r = _is_row(s.strip())
                if r:
                    out.append((Z + N, sym, Z, N, r[0], r[1]))
        _C["l"] = out
    return _C["l"]


def verdict():
    """(settled?, why) -- and it is settled as a REFUSAL, on the input."""
    req, blanks, page, avail = separators()
    return (avail < req,
            "the delimiter the document defines is absent from this "
            "extraction: %d separators required, at most %d available"
            % (req, avail))


def selftest():
    ok = True

    def chk(lab, got, want):
        nonlocal ok
        good = got == want
        ok = ok and good
        print("  [%s] %-58s %s" % ("ok" if good else "XX", lab,
                                   got if good else "%s != %s" % (got, want)))

    chk("the paper states its own delimiter, and this is it",
        spec_is_stated(), True)
    chk("and its own census: 234 entries = 173 bands + 61 bandhead states",
        (STATED["entries"], STATED["bands"] + STATED["bandheads"]),
        (234, 234))

    S = sections()
    chk("the 24 nuclide sections DO resolve, with Z and N for every one",
        (len(S), sum(1 for _k, _s, Z, N in S if Z and N)), (24, 24))
    chk("and they are Ho x8, Tm x11, Lu x5",
        sorted((sym, sum(1 for _k, y, _z, _n in S if y == sym))
               for sym in {s[1] for s in S}),
        [("Ho", 8), ("Lu", 5), ("Tm", 11)])

    req, blanks, page, avail = separators()
    chk("210 entry separators are REQUIRED by the paper's own census", req, 210)
    chk("71 blank lines are PRESENT, 22 of them at a page break",
        (blanks, page), (71, 22))
    chk("so at most 49 could be separators, against 210 required",
        (avail, avail < req), (49, True))
    chk("and even granting every one, the file is four times short",
        req // max(avail, 1) >= 4, True)
    chk("DIRECT: the 156-Ho entry 1 -> 2 boundary carries no blank row",
        boundary_has_no_blank(), True)

    settled, _why = verdict()
    chk("SO THE REFUSAL IS PROVED, not asserted", settled, True)

    chk("what IS recoverable is measured too, not just the failure",
        len(levels()) > 1500, True)
    chk("the four forward attempts are recorded with their numbers",
        [n for _w, n, _y in ATTEMPTS], [154, 176, 160, 195])
    chk("and none of them reached the stated census",
        [n for _w, n, _y in ATTEMPTS if n == STATED["entries"]], [])

    print("deformed selftest: %s" % ("PASS" if ok else "FAIL"))
    return ok


def report():
    print("=" * 79)
    print("DOCKET 36 -- THE DEFORMED TWO-QUASIPARTICLE BANDS.  REFUSED, WITH A PROOF.")
    print("=" * 79)
    print()
    print("SOURCE  %s" % PAPER)
    print("        captures/arxiv-2508.05447.txt")
    print()
    print("1. FOUR FORWARD PARSES, ALL SHORT, AND EACH FIX A BETTER GUESS.")
    print("     %-46s %-6s %s" % ("attempt", "got", "why it failed"))
    for what, n, why in ATTEMPTS:
        print("     %-46s %-6d %s" % (what, n, why))
    print("     stated by the paper                            %d" % STATED["entries"])
    print("   Moving the number without explaining the gap is FITTING A PARSER")
    print("   TO A TARGET -- the fault DOCKET 23 refused.  So: work backwards.")
    print()
    print("2. THE DOCUMENT DEFINES ITS OWN DELIMITER.")
    print('     "%s."' % SPEC)
    print("   A BLANK ROW.  Every parse above used the band-number column as a")
    print("   proxy, and that column is bare integers indistinguishable from")
    print("   page numbers and the comment column's own markers.")
    print()
    print("3. AND THE DELIMITER IS NOT IN THIS FILE.")
    req, blanks, page, avail = separators()
    print("     required, by the paper's own census      %3d" % req)
    print("     blank lines present in the table         %3d" % blanks)
    print("     of those, sitting at a page break        %3d" % page)
    print("     AT MOST available as separators          %3d" % avail)
    print("   Even granting every one, the file is %dx short."
          % (req // max(avail, 1)))
    print("   DIRECT CHECK -- 156-Ho, entry 1 to entry 2, where the spec")
    print("   requires a blank row: %s"
          % ("THERE IS NONE" if boundary_has_no_blank() else "there is one"))
    print()
    print("   The extraction collapsed the blank rows.  No regex recovers a")
    print("   delimiter that is not there, which is why all four failed and")
    print("   why a fifth would too.")
    print()
    print("4. WHAT IS RECOVERABLE, WHICH IS NOT NOTHING.")
    S = sections()
    print("     nuclide sections, with Z and N           %3d" % len(S))
    print("     level rows                              %4d" % len(levels()))
    print("   But WHICH LEVELS BELONG TO WHICH BAND is exactly what the lost")
    print("   delimiter carried, and the census that would show a capture")
    print("   total is a census of BANDS.  So nothing is seated.")
    print()
    print("5. WHAT WOULD SETTLE IT.")
    print("   An extraction that preserves layout -- blank rows, or the column")
    print("   x-positions, so the band-number column is told from a page")
    print("   number by POSITION rather than by shape.  Not available here:")
    print("   arXiv is 403 through this proxy exactly as ENSDF is, and the")
    print("   connector returns this same extraction.")
    print()
    print("   THE DOCKET IS OPEN ON AN INPUT, NOT ON AN IDEA.")
    return 0


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    sys.exit(report())
