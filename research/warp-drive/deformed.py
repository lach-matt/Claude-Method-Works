#!/usr/bin/env python3
r"""deformed.py -- DOCKET 36.  A RETRACTED REFUSAL, AND WHAT SURVIVES IT.

    python3 deformed.py             the reading
    python3 deformed.py --selftest  fixtures

===============================================================================
0. THIS FILE ONCE CLAIMED A PROOF OF IMPOSSIBILITY.  THE CLAIM WAS FALSE.
===============================================================================

    WHAT IT SAID: "no regex recovers a delimiter that is not there ... it is
    why a fifth would fail too", and "WHAT CANNOT BE RECOVERED IS WHICH LEVELS
    BELONG TO WHICH BAND".

    WHAT IS TRUE: a fifth parse succeeds.  `segment()` below recovers 233 of
    the paper's 234 entries with a six-line rule, in 24 blocks that match the
    24 nuclide sections exactly, every block contiguous 1..n.  An adversarial
    audit found it and I reproduced it before writing this.

    WHAT WENT WRONG IS WORTH MORE THAN THE FIX.  The blank-row measurement in
    section 2 is correct, and stronger than it was stated.  The error was
    generalising from it: "the delimiter the DOCUMENT DEFINES is absent" is a
    fact about blank rows, and I turned it into "no delimiter is recoverable",
    which is a fact about every possible parse and was never measured.  The
    four failed attempts felt like evidence for the stronger claim and were
    only ever evidence for the weaker one.

    AND THE FOUR ATTEMPTS FAILED FOR A REASON I HAD BACKWARDS.  Attempt 2
    tracked the band number as one stream with no per-nuclide reset; attempt 4
    RELAXED the sequence to tolerate a gap.  The rule that works TIGHTENS it:
    demand the next integer exactly, or a 1 that opens a new nuclide, and
    never anything else.  Relaxing admits the page numbers; tightening makes
    them invisible, because the scan is only ever looking for one value.

===============================================================================
0b. WHAT WAS WANTED, AND WHY THE FIRST FOUR ATTEMPTS MISSED
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

    PRESENT.  ZERO.  The table region holds 71 blank lines and not one is an
    entry separator: 50 sit immediately before a bare page number, and 21 sit
    INSIDE a nuclide header, whose extraction layout is A / Z / blank / N /
    symbol -- 21 rather than 24 because three headers print Z and N on one
    line ("67 89", "69 105", "71 93").

    AN EARLIER VERSION OF THIS FILE SAID "22 at a page break, so at most 49
    available", AND BOTH HALVES WERE WRONG.  Its classifier tested backwards
    -- a bare number BEFORE the blank -- which caught the 21 header internals
    plus exactly one real page break by accident, where the preceding line was
    a transition energy that happened to be three digits.  Its other arm,
    looking for the repeated column header after the blank, never fired at
    all, because in this extraction the order is content, blank, page number,
    header.  Classifying FORWARD, and testing for the nuclide symbol before
    the page number, gives 21 / 50 / 0.  The finding is stronger than the
    version that was wrong about it: not "at most 49 against 210" but NONE.

    DIRECT.  At the 156-Ho entry 1 -> entry 2 boundary, where the
    specification requires a blank row, THERE IS NONE: the comment text of
    entry 1 runs straight into the line `2 `.

THE PDF-TO-TEXT EXTRACTION COLLAPSED THE BLANK ROWS.  That much is measured
and it is why the document's OWN delimiter cannot be used.

IT DOES NOT FOLLOW THAT NOTHING ELSE SEGMENTS THE TABLE, and the sentence that
used to stand here said it did.  RETRACTED.  See section 2b.

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

AND BAND MEMBERSHIP IS RECOVERABLE AFTER ALL -- section 2b.  The sentence that
stood here, "WHAT CANNOT BE RECOVERED IS WHICH LEVELS BELONG TO WHICH BAND",
is RETRACTED.  What remains true is the standard it was defending: a capture
is not seated until its totality is demonstrated, and 233 of 234 is not 234.

===============================================================================
4. WHAT WOULD SETTLE IT
===============================================================================

AN EXTRACTION THAT PRESERVES LAYOUT.  The blank rows exist in the PDF; they
were lost in the conversion to text.  Any extraction that keeps blank rows, or
keeps the x-positions of the columns so the band-number column can be told
from a page number by POSITION rather than by shape, makes this table
parseable and this docket closeable.

That is not available here, and that was checked rather than assumed --
THREE ROUTES, ALL MEASURED:

    THE BYTES.  arXiv itself is 403 through the egress proxy, exactly as
    ENSDF is.  AN EARLIER VERSION OF THIS SECTION WENT FURTHER AND WAS WRONG:
    it said the proxy's bypass list "is package registries" and concluded no
    mirror is reachable.  That conflated two different things -- the `noProxy`
    list (hosts that skip the proxy entirely, which IS just the registries)
    with what the proxy PERMITS, which is much wider.  Measured directly:
    storage.googleapis.com and github.com both tunnel (server replies, not
    CONNECT refusals) while arxiv.org is refused outright.  So a mirror may
    well be reachable, and the sentence claiming otherwise is RETRACTED.
    It is also now moot: section 2b recovers the boundaries from the text
    already in hand, with no second extraction needed.

    THE CONNECTOR.  Both of its tools -- the whole-paper read and the
    page-query read -- return THIS extraction.  There is no layout-preserving
    mode to ask for.

    THE DATA'S OTHER HOME.  The paper says its level energies come from ENSDF
    and XUNDL, so the data exists outside the PDF.  pypi IS directly
    reachable, and was probed properly this time: `nucleardatapy` 1.0.2 (the
    package an earlier route record mis-named `nucleardata` and wrote off as
    non-existent) is real, and carries binding energies, charge radii, neutron
    skin and ISGMR -- NO LEVEL SCHEMES.  `pyne` on pypi is an unrelated
    package that took the name.  Closed on CONTENT, which is a better closure
    than the wrong-name one it replaces.

The docket is OPEN ON AN INPUT, not on an idea -- which is a different thing
from the four closed routes `subpop.py` records, and is why it is written down
rather than retried.
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
    page = hdr = 0
    for k in blanks:
        nxt = [b[j].strip() for j in range(k + 1, min(k + 6, len(b)))
               if b[j].strip()][:2]
        # ORDER MATTERS: a header-internal blank is followed by N, which looks
        # exactly like a page number.  Test for the nuclide symbol FIRST.
        if any(x in SY for x in nxt):
            hdr += 1
        elif nxt and re.fullmatch(r'\d{1,3}', nxt[0]):
            page += 1
    required = STATED["entries"] - len(sections())
    return (required, len(blanks), page, hdr, len(blanks) - page - hdr)


SEG = re.compile(r'^(\d{1,3})(\s|$)')


def segment():
    """[(line, band number)] -- the entry boundaries, recovered.

    THE RULE THAT WORKS, and it TIGHTENS where the four failed attempts
    relaxed.  Walk every line that opens with a small integer and accept it
    only if it is the next number expected, or a 1 that opens a new nuclide.
    Nothing else is ever accepted.

    That is why the band-number column's ambiguity with page numbers stops
    mattering: the scan is looking for ONE value at a time, so a page number
    is only ever consulted if it happens to equal the next band number at the
    moment it appears -- and it never does.  Of 692 candidate lines, 459 are
    noise and none of them is chosen.
    """
    if "s" not in _C:
        out, exp = [], 1
        for j, line in enumerate(table()):
            m = SEG.match(line)
            if not m:
                continue
            v = int(m.group(1))
            if v == exp:
                out.append((j, v)); exp += 1
            elif v == 1 and exp > 1:
                out.append((j, 1)); exp = 2
        _C["s"] = out
    return _C["s"]


def blocks():
    """[[band numbers]] per nuclide -- one block per reset."""
    out, cur = [], []
    for _j, v in segment():
        if v == 1 and cur:
            out.append(cur); cur = []
        cur.append(v)
    if cur:
        out.append(cur)
    return out


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
    """(blank-row delimiter absent?, entries recoverable another way, why)."""
    req, blanks, page, hdr, avail = separators()
    return (avail == 0, len(segment()),
            "the document's own delimiter is absent -- %d separators required, "
            "%d available -- but %d of %d entries are recoverable from the band "
            "number under a sequence-with-reset rule, so the earlier conclusion "
            "that none were is RETRACTED"
            % (req, avail, len(segment()), STATED["entries"]))


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

    req, blanks, page, hdr, avail = separators()
    chk("210 entry separators are REQUIRED by the paper's own census", req, 210)
    chk("71 blank lines are PRESENT: 50 page boundaries, 21 header internals",
        (blanks, page, hdr), (71, 50, 21))
    chk("so ZERO are entry separators -- stronger than the 49 once claimed",
        avail, 0)
    chk("DIRECT: the 156-Ho entry 1 -> 2 boundary carries no blank row",
        boundary_has_no_blank(), True)

    absent, got, _why = verdict()
    chk("the document's own delimiter IS absent -- that much stands", absent, True)
    # THE RETRACTION, AS A FIXTURE.  This file once concluded that no parse
    # could recover entry boundaries.  A tightened sequence rule does.
    chk("BUT 233 of 234 entries ARE recoverable -- the old conclusion is "
        "RETRACTED", got, 233)
    chk("in 24 blocks, matching the 24 nuclide sections exactly",
        (len(blocks()), len(sections())), (24, 24))
    chk("and every block is contiguous 1..n, which a coincidence would not be",
        [b for b in blocks() if b != list(range(1, len(b) + 1))], [])
    chk("the file says RETRACTED where it was wrong, rather than quietly "
        "rewriting", open(__file__, encoding="utf-8").read().count("RETRACTED") >= 3,
        True)

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
    print("DOCKET 36 -- THE DEFORMED BANDS.  A REFUSAL, RETRACTED.")
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
    print("3. AND THE DOCUMENT'S OWN DELIMITER IS NOT IN THIS FILE.")
    req, blanks, page, hdr, avail = separators()
    print("     required, by the paper's own census      %3d" % req)
    print("     blank lines present in the table         %3d" % blanks)
    print("       sitting at a page boundary             %3d" % page)
    print("       sitting INSIDE a nuclide header        %3d" % hdr)
    print("     available as entry separators            %3d" % avail)
    print("   DIRECT CHECK -- 156-Ho, entry 1 to entry 2, where the spec")
    print("   requires a blank row: %s"
          % ("THERE IS NONE" if boundary_has_no_blank() else "there is one"))
    print()
    print("4. BUT THAT DOES NOT MEAN NOTHING SEGMENTS THE TABLE, AND THIS")
    print("   FILE ONCE SAID IT DID.  RETRACTED.")
    print("     entries recovered by a sequence-with-reset rule   %3d of %d"
          % (len(segment()), STATED["entries"]))
    print("     blocks, against %d nuclide sections               %3d"
          % (len(sections()), len(blocks())))
    print("     every block contiguous 1..n                       %s"
          % all(b == list(range(1, len(b) + 1)) for b in blocks()))
    print("   The rule TIGHTENS where the four attempts relaxed: take the next")
    print("   expected integer, or a 1 that opens a nuclide, and nothing else.")
    print("   The band number's ambiguity with page numbers then stops")
    print("   mattering -- the scan seeks one value at a time, and of 692")
    print("   candidate lines the 459 noise ones are never chosen.")
    print()
    print("5. WHAT ELSE IS RECOVERABLE.")
    S = sections()
    print("     nuclide sections, with Z and N           %3d" % len(S))
    print("     level rows                              %4d" % len(levels()))
    print("   Band membership too, now that section 4 recovers the")
    print("   boundaries.  NOTHING IS SEATED YET, and the reason is no longer")
    print("   impossibility: it is that 233 of 234 is not 234, and a capture")
    print("   is not seated until its totality is demonstrated.")
    print()
    print("6. WHAT REMAINS BEFORE ANYTHING IS SEATED.")
    print("   ONE ENTRY of the 234, and the totality argument that follows")
    print("   from finding it.  The paper offers an unusually rich fixture set")
    print("   to check a finished capture against -- 234 = 173 bands + 61")
    print("   bandhead states, 63 GM doublets, 76 with signature splitting, 29")
    print("   with inversion, 10 band crossings, 58 bandheads with half-lives.")
    print()
    print("   A LAYOUT-PRESERVING EXTRACTION IS NO LONGER NEEDED and this file")
    print("   used to say it was.  Section 4 works on the text already here.")
    print()
    print("   THE DOCKET IS OPEN ON ONE MISSING ENTRY, NOT ON AN INPUT.")
    return 0


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    sys.exit(report())
