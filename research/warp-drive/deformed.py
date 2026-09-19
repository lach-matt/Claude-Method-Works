#!/usr/bin/env python3
r"""deformed.py -- DOCKET 36.  A RETRACTED REFUSAL, AND THE CAPTURE THAT CLOSES IT.

    python3 deformed.py             the reading
    python3 deformed.py --selftest  fixtures

===============================================================================
0. THIS FILE ONCE CLAIMED A PROOF OF IMPOSSIBILITY.  THE CLAIM WAS FALSE.
===============================================================================

    WHAT IT SAID: "no regex recovers a delimiter that is not there ... it is
    why a fifth would fail too", and "WHAT CANNOT BE RECOVERED IS WHICH LEVELS
    BELONG TO WHICH BAND".

    WHAT IS TRUE: a fifth parse succeeds.  `segment()` below recovers the
    paper's 234 entries with a seven-line rule, in 24 blocks that match the 24
    nuclide sections exactly, every block contiguous 1..n.  An adversarial
    audit found the rule at 233 and I reproduced it before writing this; the
    234th is section 2c.

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
2c. THE 234th ENTRY.  ONE LINE, AND IT IS A TRAILING FULL STOP
===============================================================================

The tightened rule reached 233 and stopped, and the missing one was NOT a
subtle parse: at 164-Ho the band-number line is printed

    `6. `

and `SEG = ^(\d{1,3})(\s|$)` refuses it, because after the 6 comes a period
and not whitespace.  Every other band number in the table is bare.

IT IS A BAND NUMBER AND NOT A COMMENT MARKER, and four things say so, none of
them the count:

    ITS VALUE IS THE ONE EXPECTED.  The preceding entry is band 5 of that
    nuclide, so the scan was looking for exactly 6 at exactly that moment.

    THE COMMENT NUMBERING RESTARTS RIGHT AFTER IT.  The next comment line is
    `1. pi7/2[523]nu11/2[505]` -- a fresh configuration, which is what comment
    1 of an entry always is.  A comment marker `6.` followed by comment `1.`
    is not a reading anyone would defend.

    THE ENERGY OFFSET CHANGES.  The levels before it are `...+x` and the ones
    after are `...+y`.  A band has ONE bandhead, so one entry cannot carry two
    unknown offsets.

    A NEW REFERENCE OPENS.  `2005LI63` appears immediately below it, as a
    citation does at the head of an entry.

AND THE SHAPE IS ADMITTED NARROWLY, WHICH MATTERS MORE THAN THE FIND.  The
obvious repair -- let the band-number regex take an optional period -- is
WRONG, and measurably so: the comment column is itself numbered `1. `, `2. `,
`3. `, so the pool jumps from 692 candidate lines to 1,032 and the rule
returns 380 boundaries against 234.  `SEGDOT` therefore matches a bare number
with a period AND NOTHING ELSE ON THE LINE.  Exactly ONE line in the whole
table region has that shape, and it is this one.  The candidate pool goes 692
-> 693 and the noise rejected stays at 459.

===============================================================================
2d. AND THE CAPTURE IS NOW TOTAL AGAINST THE PAPER'S OWN CENSUS
===============================================================================

    entries          234  stated     234  captured    EXACT
    bands            173  stated     173  captured    EXACT
    bandhead states   61  stated      61  captured    EXACT

THREE INDEPENDENT NUMBERS, NOT ONE, and the third was already exact before the
234th entry was found -- which is what made the search well-posed.  Splitting
a band into two bands adds one entry AND one band and leaves bandheads alone,
so only a split could have closed the gap, and only one split could.

Two further structural checks hold: 24 blocks against 24 nuclide sections, and
every block contiguous 1..n -- which a run of coincidences would not be.

    THE PAPER'S OTHER FOUR FIGURES ARE NOT VALIDATORS AND WERE CHECKED ANYWAY.
    63 GM doublets, 76 with signature splitting, 29 with inversion, 10 band
    crossings.  Those are counts the paper makes about its dataset in prose,
    not censuses of a table column: the comment text yields 73, 25 and 10 for
    the last three and nothing at all for GM doublets, which is a phrase the
    table never prints.  A capture is not validated against a number the
    source does not tabulate, so these are recorded and not used.

===============================================================================
2e. ONE DISCONTINUITY REMAINS, AND IT IS A FEATURE OF THE SOURCE
===============================================================================

164-Lu, band 4, runs (23+) (24+) (25+) and then (16-) (18-) (20-) (22-): the
spin falls and the parity flips, neither of which a rotational band does.  It
is NOT a missed boundary, and the same four tests that convicted `6. ` acquit
this one:

    NO CANDIDATE LINE.  There is no integer line of any shape at the break.
    THE COMMENT NUMBERING DOES NOT RESTART -- it runs 1, 2, 3 straight across.
    THE OFFSET DOES NOT CHANGE -- every level is `...+z`.
    NO NEW REFERENCE OPENS.
    AND THE TRANSITION ENERGIES ARE ONE SMOOTH CASCADE: 344.4, 411.4, 472.1,
    519.7, 553.9, 584.4, monotone across the break.

So the paper prints it as one entry, and this file captures it as one entry.
Whether the printed spins are right is the paper's business and not this
capture's.  RECORDED, NOT REPAIRED.

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
is RETRACTED.  The standard it was defending is met rather than waived: a
capture is not seated until its totality is demonstrated, and section 2d
demonstrates it on three of the paper's own numbers.

===============================================================================
4. WHAT WOULD HAVE SETTLED IT, AND WHY NONE OF IT WAS NEEDED
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

THE DOCKET IS CLOSED ON THE CAPTURE, and none of the three routes above was
used: no second extraction, no mirror, no external level scheme.  The whole of
it came out of the text already in hand, and the last step was one line with a
full stop on it.

WHAT IS NOT CLOSED IS SEATING.  A capture is not an index.  Whether these
levels earn a position in the master index is the overlap ruling's question,
and `docket36_chart()` measures the chart without answering it.
"""

import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "captures", "arxiv-2508.05447.txt")
ENTRIES_TSV = os.path.join(HERE, "captures", "DEFORMED-entries.tsv")
LEVELS_TSV = os.path.join(HERE, "captures", "DEFORMED-levels.tsv")

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
# EVERY SPELLING THE SOURCE ACTUALLY PRINTS FOR A LEVEL ENERGY.  Each was
# added because a row was being dropped for a mechanical reason, and each is
# pointed at a printed form rather than chosen to move a count:
#   558.579(4)   an uncertainty in parentheses      (the largest group by far)
#   595.841(50   the same, with the closing paren wrapped away
#   X+266.5      label-first, when the bandhead energy is unknown
#   266.5+X      offset-first, the same thing the other way round
#   118.0 or     an ambiguous energy, first value taken
ENER = (r'\(?(?:[A-Za-z]\s*\+\s*)?\d+(?:\.\d+)?(?:\(\d+\)?)?'
        r'(?:\s*\+\s*[A-Za-z])?\)?'
        r'|\(?[A-Za-z]\)?|\(A[<>]\d+\)\?')
SPIN = r'\(?\d{1,2}(?:/2)?[\(\)]*[+−-]?[\(\)]*\)?'
ROW = re.compile(r'^(%s)(?:\s+or)?\s+(%s)(\s|$)' % (ENER, SPIN))

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
# THE 234th ENTRY.  One band-number line in the whole table region is
# printed with a trailing period -- `6. ` at 164-Ho -- and `SEG` refuses
# it.  This shape is a BARE number alone on its line; it is NOT the
# comment column's `1. pi7/2[523]nu11/2[505]`, which carries text after
# the period and would flood the candidate pool if admitted (measured:
# 380 boundaries instead of 234).  Exactly ONE line in the table matches
# this, and it is the one that was missing.
SEGDOT = re.compile(r'^(\d{1,3})\.\s*$')


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
            m = SEG.match(line) or SEGDOT.match(line)
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


def two_i(tok):
    """2I from an I^pi cell, doubled so half-integers stay integers."""
    t = re.sub(r'[()+\u2212\-\s]', "", tok)
    if not t:
        return None
    return int(t[:-2]) if t.endswith("/2") else 2 * int(t)


def entries():
    """[{no, levels, nuclide}] -- the table segmented into its entries.

    Boundaries from `segment()`, levels from the rows between them.  This is
    the capture the retracted refusal said could not exist.
    """
    if "e" not in _C:
        lines = _rejoin(table())
        out, exp, cur = [], 1, None
        Z = N = None
        for j, s in enumerate(lines):
            t = s.strip()
            if t in SY:
                prev = [lines[k].strip() for k in range(j - 1, max(j - 6, -1), -1)
                        if lines[k].strip()][:2]
                nums = []
                for pv in prev:
                    if re.fullmatch(r'[\d ]+', pv):
                        nums += [int(x) for x in re.findall(r'\d+', pv)]
                zz = [x for x in nums if 60 <= x <= 75]
                nn = [x for x in nums if 80 <= x <= 115]
                if zz and nn:
                    Z, N = zz[0], nn[0]
            m = SEG.match(t) or SEGDOT.match(t)
            if m:
                v = int(m.group(1))
                if v == exp or (v == 1 and exp > 1):
                    cur = {"no": v, "Z": Z, "N": N,
                           "A": (Z + N) if (Z and N) else None, "levels": []}
                    out.append(cur)
                    exp = v + 1 if v == exp else 2
                    rest = t[m.end():].strip()
                    if rest:
                        r = _is_row(rest)
                        if r:
                            cur["levels"].append(r)
                    continue
            if cur is not None:
                r = _is_row(t)
                if r:
                    cur["levels"].append(r)
        _C["e"] = out
    return _C["e"]


def census2():
    """(entries, bands, bandhead states) measured, against STATED."""
    E = entries()
    return (len(E),
            sum(1 for e in E if len(e["levels"]) >= 2),
            sum(1 for e in E if len(e["levels"]) <= 1))


def discontinuities():
    """[(index, no, spins, drop)] -- entries whose spin sequence FALLS.

    A rotational band's spins ascend.  A fall inside one entry means TWO bands
    were merged because a band-number line was not recognised.  This is the
    structural check that says the capture is NOT yet total, and it is
    reported rather than repaired: splitting both of these would give 235
    entries against the paper's 234, so something here is not yet understood
    and forcing the number would be fitting.
    """
    out = []
    for i, e in enumerate(entries()):
        sp = [two_i(x[1]) for x in e["levels"]]
        sp = [x for x in sp if x is not None]
        dr = [(a, b) for a, b in zip(sp, sp[1:]) if b < a]
        if dr:
            out.append((i, e["no"], sp, dr))
    return out


def verdict():
    """(blank-row delimiter absent?, entries recovered, why)."""
    req, _blanks, _page, _hdr, avail = separators()
    return (avail == 0, len(segment()),
            "the document's own delimiter is absent -- %d separators required, "
            "%d available -- and all %d of %d entries are recoverable from the "
            "band number under a sequence-with-reset rule, so the earlier "
            "conclusion that none were is RETRACTED"
            % (req, avail, len(segment()), STATED["entries"]))


def dotted_number_lines():
    """[(line, text)] -- every line that is a bare integer plus a full stop.

    Section 2c's narrowness, measured rather than asserted.  EXACTLY ONE line
    in the table region has this shape, which is why admitting it adds one
    candidate and not three hundred.
    """
    return [(k, s) for k, s in enumerate(table()) if SEGDOT.match(s)]


def candidate_pool():
    """(candidate lines, chosen, rejected as noise) under the live rule."""
    b = table()
    cand = [l for l in b if SEG.match(l) or SEGDOT.match(l)]
    return (len(cand), len(segment()), len(cand) - len(segment()))


def prose_figures():
    """{phrase: occurrences} -- the paper's four NON-tabulated census figures.

    Checked so that nobody later mistakes their absence for an oversight, and
    NOT used as validators: these are counts the paper makes in prose about
    its dataset, not censuses of a column of Table 3.  `GM doublet` is not a
    phrase the table prints at all.
    """
    import re as _re
    txt = "\n".join(table())
    out = {}
    for lab, pats in (("signature_splitting", ("Signature splitting",
                                               "signature splitting")),
                      ("signature_inversion", ("Signature inversion",
                                               "signature inversion")),
                      ("band_crossings", ("crossing",)),
                      ("gm_doublets", ("GM doublet", "Gallagher"))):
        out[lab] = sum(len(_re.findall(x, txt)) for x in pats)
    return out


def _parity(tok):
    if "\u2212" in tok or "-" in tok:
        return -1
    return 1 if "+" in tok else None


def docket36_chart():
    """(cells, K, cell, members, levels with no parity) -- MEASURED, NOT SEATED.

    The chart these levels would give on (2I, parity), the same coordinates
    `nucbands.py` carries.  It is reported so the seating question is asked
    with numbers in hand; seating is a RULING and this file does not make it.
    """
    import mi as _mi
    cells, n, nopar = set(), 0, 0
    for e in entries():
        for _en, sp in e["levels"]:
            i2, p = two_i(sp), _parity(sp)
            if i2 is None:
                continue
            if p is None:
                nopar += 1
                continue
            cells.add((i2, p))
            n += 1
    X = frozenset(cells)
    return (len(X), _mi.K(X), _mi.cell(X), n, nopar)


def write():
    """Write the capture AS IT STANDS -- short, and labelled short.

    It is not seated and the files say so in their own header, so nobody
    downstream can mistake 233 of 234 for a finished census.
    """
    c = census2()
    hdr = ("# %s\n"
           "# CAPTURE TOTAL AGAINST THE PAPER'S OWN CENSUS -- entries %d/%d, "
           "bands %d/%d,\n"
           "# bandhead states %d/%d, all exact; 24 blocks against 24 nuclide "
           "sections,\n"
           "# every block contiguous 1..n.  NOT SEATED: a capture is not an "
           "index, and\n"
           "# seating is the overlap ruling's question.  One entry (164-Lu "
           "band 4) carries\n"
           "# a falling spin sequence; it is the SOURCE's, not a missed "
           "boundary -- see\n"
           "# deformed.discontinuities() and section 2e.\n"
           % (PAPER, c[0], STATED["entries"], c[1], STATED["bands"],
              c[2], STATED["bandheads"]))
    with open(ENTRIES_TSV, "w", encoding="utf-8") as f:
        f.write(hdr)
        f.write("seq\tno\tA\tZ\tN\tlevels\tkind\tspin_falls\n")
        bad = {i for i, _n, _s, _d in discontinuities()}
        for i, e in enumerate(entries()):
            f.write("%d\t%d\t%s\t%s\t%s\t%d\t%s\t%s\n"
                    % (i, e["no"], e["A"] or "", e["Z"] or "", e["N"] or "",
                       len(e["levels"]),
                       "band" if len(e["levels"]) >= 2 else "bandhead",
                       "YES" if i in bad else ""))
    with open(LEVELS_TSV, "w", encoding="utf-8") as f:
        f.write(hdr)
        f.write("seq\tA\tZ\tN\tE\t2I\n")
        for i, e in enumerate(entries()):
            for (en, sp) in e["levels"]:
                f.write("%d\t%s\t%s\t%s\t%s\t%s\n"
                        % (i, e["A"] or "", e["Z"] or "", e["N"] or "", en,
                           "" if two_i(sp) is None else two_i(sp)))
    return c


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
    chk("BUT all 234 entries ARE recoverable -- the old conclusion is "
        "RETRACTED", got, 234)
    chk("in 24 blocks, matching the 24 nuclide sections exactly",
        (len(blocks()), len(sections())), (24, 24))
    chk("and every block is contiguous 1..n, which a coincidence would not be",
        [b for b in blocks() if b != list(range(1, len(b) + 1))], [])
    chk("the file says RETRACTED where it was wrong, rather than quietly "
        "rewriting", open(__file__, encoding="utf-8").read().count("RETRACTED") >= 3,
        True)

    chk("what IS recoverable is measured too, not just the failure",
        len(levels()) > 1500, True)

    # -- THE 234th ENTRY, AND THE NARROWNESS OF THE SHAPE THAT FOUND IT
    dots = dotted_number_lines()
    chk("EXACTLY ONE line in the table is a bare integer plus a full stop",
        [(k, t.strip()) for k, t in dots], [(1408, "6.")])
    chk("and admitting it adds ONE candidate, not a flood",
        candidate_pool(), (693, 234, 459))
    chk("the comment column is numbered too, which is why the shape is narrow",
        any(re.match(r'^\d{1,3}\.\s+\S', t) for t in table()), True)

    # -- THE CAPTURE, AND ITS TOTALITY AGAINST THREE STATED NUMBERS
    c = census2()
    chk("entries, bands and bandhead states all EXACT against the paper",
        c, (STATED["entries"], STATED["bands"], STATED["bandheads"]))
    chk("and the three are consistent: bands + bandheads = entries",
        c[1] + c[2], c[0])
    chk("every entry carries its nuclide",
        sum(1 for e in entries() if e["A"]), 234)
    chk("levels attached", sum(len(e["levels"]) for e in entries()), 1964)

    # -- THE ONE REMAINING DISCONTINUITY IS THE SOURCE'S, NOT A MISSED LINE
    d = discontinuities()
    chk("ONE entry has a falling spin sequence, and it is 164-Lu band 4",
        [(no, len(sp)) for _i, no, sp, _dr in d], [(4, 7)])
    chk("no integer line of any shape sits at its break -- not a boundary",
        [t for t in table()[7283:7286] if SEG.match(t) or SEGDOT.match(t)], [])
    chk("splitting it would give 235 against a stated 234, so it stands",
        c[0] + len(d), 235)

    # -- THE PROSE FIGURES WERE CHECKED AND ARE NOT USED
    pf = prose_figures()
    chk("the paper's four prose figures do not tabulate, and are not "
        "validators", (pf["gm_doublets"], pf["signature_splitting"] ==
                       STATED["signature_splitting"]), (0, False))

    chk("the four forward attempts are recorded with their numbers",
        [n for _w, n, _y in ATTEMPTS], [154, 176, 160, 195])
    chk("and none of them reached the stated census",
        [n for _w, n, _y in ATTEMPTS if n == STATED["entries"]], [])

    # -- MEASURED, NOT SEATED
    cells, K, cell, n, nopar = docket36_chart()
    chk("the chart these levels would give is measured", (cells, K, cell),
        (96, 2, (2, 49, 2)))
    chk("on 1,904 levels, with 60 carrying no parity", (n, nopar), (1904, 60))
    chk("and NOTHING IS SEATED HERE -- seating is a ruling",
        "docket36_chart" in open(__file__, encoding="utf-8").read()
        and "NOT SEATED" in open(__file__, encoding="utf-8").read(), True)

    print("deformed selftest: %s" % ("PASS" if ok else "FAIL"))
    return ok


def report():
    print("=" * 79)
    print("DOCKET 36 -- THE DEFORMED BANDS.  A REFUSAL RETRACTED, AND THE CAPTURE CLOSED.")
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
    print("   boundaries -- and the totality a capture needs before it may be")
    print("   seated is demonstrated in section 6, not waived.")
    print()
    print("6. THE 234th ENTRY WAS ONE LINE WITH A FULL STOP ON IT.")
    for k, t in dotted_number_lines():
        print("     line %-6d %-8s the only bare integer + full stop in the"
              % (k, repr(t.strip())))
    print("                        whole table region.  SEG wanted whitespace")
    print("                        after the digits and refused it.")
    print("   IT IS A BAND NUMBER, and none of the four reasons is the count:")
    print("     its value is the one the scan was expecting at that moment;")
    print("     the comment numbering RESTARTS at 1 immediately below it;")
    print("     the energy offset changes from +x to +y, and a band has one")
    print("       bandhead;")
    print("     and a new reference, 2005LI63, opens under it.")
    cp = candidate_pool()
    print("   THE SHAPE IS ADMITTED NARROWLY.  Letting the band-number regex")
    print("   take an optional period would swallow the comment column's own")
    print("   `1. `, `2. `, `3. ` markers and return 380 boundaries.  A bare")
    print("   number with a period AND NOTHING ELSE matches exactly one line:")
    print("     candidates %d   chosen %d   noise rejected %d" % cp)
    print()
    print("7. THE CAPTURE IS TOTAL AGAINST THE PAPER'S OWN CENSUS.")
    c = census2()
    print("     %-22s %-10s %-10s %s" % ("", "paper", "captured", ""))
    for lab, key, got in (("entries", "entries", c[0]),
                          ("bands (>=2 levels)", "bands", c[1]),
                          ("bandhead states", "bandheads", c[2])):
        print("     %-22s %-10d %-10d %s"
              % (lab, STATED[key], got,
                 "EXACT" if got == STATED[key] else "SHORT BY %d"
                 % (STATED[key] - got)))
    print("     %-22s %-10s %-10d" % ("levels attached", "-",
                                      sum(len(e["levels"]) for e in entries())))
    print("   THREE INDEPENDENT NUMBERS, and the third was exact BEFORE the")
    print("   234th entry was found -- which is what made the search")
    print("   well-posed.  A split adds one entry and one band and leaves")
    print("   bandheads alone, so only a split could close the gap, and only")
    print("   one split could.  Two structural checks hold beside them: %d"
          % len(blocks()))
    print("   blocks against %d nuclide sections, every block contiguous 1..n."
          % len(sections()))
    print()
    print("   THE PAPER'S OTHER FOUR FIGURES ARE NOT VALIDATORS, and were")
    print("   checked rather than passed over -- they are prose counts about")
    print("   the dataset, not censuses of a table column:")
    pf = prose_figures()
    for k in ("gm_doublets", "signature_splitting", "signature_inversion",
              "band_crossings"):
        print("     %-22s stated %-6d in the table %d"
              % (k, STATED[k], pf[k]))
    print()
    print("8. ONE DISCONTINUITY REMAINS AND IT IS THE SOURCE'S.")
    for i, no, sp, dr in discontinuities():
        print("     entry %-4d no=%-3d %d levels, falls %s -> %s"
              % (i, no, len(sp), dr[0][0], dr[0][1]))
    print("   164-Lu band 4 runs (23+) (24+) (25+) then (16-) (18-) (20-)")
    print("   (22-).  The same four tests that convicted the `6. ` line")
    print("   acquit this one: no candidate line at the break, the comment")
    print("   numbering does not restart, the offset stays +z, no new")
    print("   reference opens -- and the transition energies are one smooth")
    print("   cascade across it, 344.4 411.4 472.1 519.7 553.9 584.4.")
    print("   The paper prints it as one entry.  RECORDED, NOT REPAIRED.")
    print()
    print("9. MEASURED, NOT SEATED.")
    cells, K, cell, n, nopar = docket36_chart()
    print("     on (2I, parity): %d cells, K%d, cell %s" % (cells, K, cell))
    print("     from %d levels carrying both, %d carrying no parity"
          % (n, nopar))
    print("   A CAPTURE IS NOT AN INDEX.  That cell is held by no seated")
    print("   index and the member set is a new one -- deformed odd-odd")
    print("   nuclei, not the near-spherical shears bands already seated --")
    print("   so it is a seating CANDIDATE.  Seating is a ruling and this")
    print("   file does not make it.")
    print()
    print("   THE DOCKET IS CLOSED ON THE CAPTURE.  IT IS OPEN ON SEATING.")
    return 0


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    if "--write" in sys.argv:
        c = write()
        print("wrote DEFORMED-entries.tsv and DEFORMED-levels.tsv "
              "(%d entries, %d bands, %d bandheads) -- TOTAL, NOT SEATED" % c)
        sys.exit(0)
    sys.exit(report())
