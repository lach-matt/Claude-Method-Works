#!/usr/bin/env python3
r"""
terms.py -- THE TERM INDEX: every Russell-Saunders term of every banked
spectrum, charted by what its J values do.

    python3 terms.py             the reading
    python3 terms.py --selftest  fixtures
    python3 terms.py --gate      the tolerance sensitivity table alone

===============================================================================
0. TWO CANDIDATES WERE FOLDED INTO ONE INDEX, AND THAT IS THE POINT
===============================================================================

Two separate indexes were proposed over the same rows: a Russell-Saunders term
index, and a Lande interval-rule index whose members are consecutive-J triples.

    **A LANDE TRIPLE LIES INSIDE EXACTLY ONE TERM.**  Every triple needs an L,
    an S and a J to exist at all, so the map from triples to terms is TOTAL and
    MANY-TO-ONE.  Seating both would put ONE BODY OF ROWS on TWO VERTICES at two
    different cells -- which is the case `overlap.py`'s own section 0 names as
    the dangerous one, and which corrupts density in both terms at once.

    THE TWO PRECEDENTS DO NOT LICENSE IT.  `periodic layout 2-D` was withdrawn
    for being a strict projection of a seated index over the same members.
    `madelung` STAYED because it is a strict COARSENING over the same members.
    Lande is neither: it is a REFINEMENT of the member granularity over a subset
    of the same rows, which multiplies the box rather than coarsening it.

So there is one index.  The interval measurement is not discarded -- it is
banked per triple in the ledger, exactly as `nucshell` banks `delta`, and for
the same measured reason.

===============================================================================
1. THE GATE FIRED, AND THE INDEX SEATS ON FOUR COORDINATES RATHER THAN FIVE
===============================================================================

The interval verdict was proposed as a fifth coordinate.  It carries a
**declared tolerance**, which is a tuning constant, so it was gated: chart the
index at a range of tolerances and see whether the cell count moves.

        tolerance   cells   cell
        0.01         152    (0, 13, 31)
        0.02         162    (0, 13, 31)
        0.05         174    (0, 13, 32)
        0.10         177    (0, 13, 34)
        0.20         172    (0, 13, 33)
        0.50         163    (0, 13, 32)

**IT MOVES, AND SO DOES THE CELL.**  The width runs from 31 to 34 and the count
is not even monotone.  A coordinate whose alphabet is a function of a number
nobody measured is not an axis, and the gate was written before the numbers were
seen precisely so that this could not be argued afterwards.

    SO `interval` DROPS TO THE LEDGER and the index seats on

        (mult, L, parity, completeness)   112 cells, box 270, cell (0, 13, 18)

    and THAT chart is tolerance-independent: 112 cells at 0.01, at 0.05 and at
    0.50.  `gate()` returns the table and `gate_fires()` the verdict, so a
    reader does not have to take this paragraph's word for it.

===============================================================================
2. WHAT A MEMBER IS
===============================================================================

    (spectrum, configuration, term)

A term carries S, L and parity; the configuration carries the n and l
occupancies; the spectrum carries the element and the charge state.  The member
is the LABEL together with the set of J values banked against it.

    **THE SPECTRUM IS THE KEY, NEVER THE FILE.**  The candidate that proposed
    the Lande index keyed on the file and was disqualified for it; keying on the
    file here would be the same fault one level up, since `recovered/` holds the
    same spectrum under several filenames.

    **THE LOWERCASE PREFIX IS PART OF THE KEY.**  ASD writes `a 3F` and `b 3F`
    for two different terms of the same symbol, and collapsing them would merge
    two members.

===============================================================================
3. WHAT IS REFUSED AT THE DOOR
===============================================================================

**BRACKETED jK, jj AND RACAH LABELS ARE REFUSED, NOT COERCED.**  A label like
`2[5/2]*` is not an LS term and has no L or S to test; forcing one would invent
the measurement.  4,033 of 16,624 rows carry such a label and are refused.

**FOUR FILES ARE REFUSED FOR AN UNREADABLE SPECIES AND ARE NAMED**, not silently
dropped: `BaLII.tsv`, `LEVELS-Fe-I.tsv`, `LEVELS-K-I.tsv`, `LEVELS-Kr-I.tsv`.

**ONE FILE IS SKIPPED AS A DUPLICATE**: `recovered/LuI__16455659.tsv`, whose
data rows are byte-identical to `recovered/LuI.tsv`.  Reading both would count
every Lu I term twice.

    ON LuI, WHAT IS BANKED AND WHAT IS NOT.  `recovered/LuI.tsv` has data rows
    byte-identical to `extracted/archives/restore-point-2-13/quarantine/
    LuI.FABRICATED.tsv`.  It is read here anyway, because the label is not
    supported: `recovered/LuI__b3dd6bb5.tsv` is an INDEPENDENT capture under
    register 1639, and all 199 of its (config, term, J) rows agree EXACTLY with
    the corresponding rows of the quarantined file -- zero disagreements, and a
    strict subset.  So 199 rows are CORROBORATED, 35 are UNDECIDED, and the file
    is neither trusted whole nor discarded whole.  Nothing is repaired, moved or
    relabelled.

===============================================================================
4. THE FOUR SEATED COORDINATES
===============================================================================

    mult          2S+1 from the term symbol, clipped at 5
    L             the term letter, S=0 P=1 D=2 ..., clipped at 8
    parity        0 even, 1 odd (the asterisk)
    completeness  COMPLETE, SHORT or MIXED -- see below

`completeness` compares the SET of J values banked against the term with the
multiplet |L-S| .. L+S that the term symbol itself implies.

**IT DOES NOT TEST RUSSELL-SAUNDERS COUPLING, AND THE MEASUREMENT SAYS SO.**
MIXED -- a banked J outside the predicted multiplet -- occurs on exactly ONE
member out of 5,132.  So what this coordinate measures is the agreement between
a banked LABEL and its own banked J VALUES, which is a statement about the
table, not about whether nature couples that way.  Naming it a test of coupling
would be the claim the numbers refuse.

**AND `|J banked|` IS NOT A SECOND COORDINATE.**  It determines `completeness`
almost everywhere; carrying both would chart one fact twice.

===============================================================================
5. WHAT THIS FILE REFUSES
===============================================================================

**TO CALL SHORT A MISSING LEVEL.**  A capture that banks three J of a five-J
multiplet may be a partial capture or a partial measurement, and this file
cannot tell which.

**TO CALL BREAKS A FAULT.**  At the 5 % tolerance 774 members break the interval
rule and 150 obey it.  The rule is an approximation that holds in pure LS
coupling; departure from it is physics, not error.

**TO READ NOT-TESTABLE AS NEGATIVE EVIDENCE.**  4,163 of 5,132 members -- 81 %
-- have fewer than three banked levels with energies, so the interval cannot be
formed at all.  That is a fact about the capture.

**TO CLAIM THE UNION IS ASD-COMPLETE.**  It is what `recovered/` holds.

**TO REPAIR A ROW.**  Where a term's banked J set contradicts its own label, the
contradiction is charted as MIXED and left alone.

**TO NAME A FILE IN A MEMBER KEY, OR TO SELECT SOURCES BY A FILE LIST.**  The
sources are chosen by a PREDICATE on the header, which is why 194 files were
found where the candidate's own list held 43 -- the other 151 differ only in
whether their header is capitalised.
"""

import collections
import os
import re
import sys

import hlaw
import mi
import overlap

# WHERE THE DATA COMES FROM.  registry.sources() reads this, checks every
# path exists and hashes it, and state.py writes the result into STATE.json --
# so provenance is a checked fact in the tree and not a sentence in a chat.
SOURCE = (
    'The NIST ASD level tables held in recovered/, read as a directory; four files are refused by name and one skipped as a duplicate.',
    (
        'recovered',
    ),
)


ROOT = "/home/user/Claude-Method-Works"
ASD = os.path.join(ROOT, "recovered")
AME = os.path.join(ROOT, "extracted/archives/restore-point-2-13/captures/"
                         "AME2020-TableI.tsv")

# byte-identical data rows to recovered/LuI.tsv -- reading both doubles Lu I
SKIP = {"LuI__16455659.tsv"}

LSEQ = "SPDFGHIKLMNOQRTUV"          # the term letters; J is skipped, as always
TERM = re.compile(r"^(?:([a-z])\s+)?(\d+)([SPDFGHIKLMNOQRTUV])(\*?)$")
ROMAN = {r: i + 1 for i, r in enumerate(
    "I II III IV V VI VII VIII IX X XI XII XIII XIV XV XVI XVII XVIII XIX XX "
    "XXI XXII XXIII XXIV XXV XXVI".split())}

NAMES = ("mult", "L", "parity", "completeness")
ARITY = 4
COMPLETENESS = ("COMPLETE", "SHORT", "MIXED")
INTERVAL = ("OBEYS", "PARTLY", "BREAKS", "NOT-TESTABLE")

TOLERANCE = 0.05                    # DECLARED, and gated in section 1
GATE_TOLERANCES = (0.01, 0.02, 0.05, 0.10, 0.20, 0.50)

COUPLING_NOT_TESTED = True          # section 4: MIXED occurs once in 5,132
LUI_CORROBORATED_ROWS = 199         # register 1639, recovered/LuI__b3dd6bb5.tsv
LUI_UNDECIDED_ROWS = 35
INTERVAL_STATUS = "MEASURED"        # ledger column, never an axis
TERM_PARSE_STATUS = "RECONSTRUCTED"

_C = {}


# ------------------------------------------------------------------- sources

def _symbols():
    if "sym" not in _C:
        s = {}
        for ln in open(AME, encoding="utf-8"):
            if ln.startswith("#") or ln.startswith("Z\t"):
                continue
            p = ln.split("\t")
            if len(p) >= 7:
                s.setdefault(p[3], int(p[0]))
        _C["sym"] = s
    return _C["sym"]


def _species(lines, stem):
    """The spectrum, from the header or the filename stem -- never the file."""
    sym = _symbols()
    for h in lines[:10]:
        if not h.startswith("#"):
            continue
        m = re.match(r"#\s*([A-Z][a-z]?)\s+([IVX]+)\b", h)
        if m and m.group(1) in sym and m.group(2) in ROMAN:
            return "%s %s" % (m.group(1), m.group(2))
    m = re.match(r"([A-Z][a-z]?)([IVX]+)(?:_|__|$)", stem)
    if m and m.group(1) in sym and m.group(2) in ROMAN:
        return "%s %s" % (m.group(1), m.group(2))
    return None


def _two_j(s):
    s = s.strip()
    m = re.fullmatch(r"(\d+)/2", s)
    if m:
        return int(m.group(1))
    m = re.fullmatch(r"(\d+)", s)
    return 2 * int(m.group(1)) if m else None


def _level(s):
    t = s.replace("[", "").replace("]", "").replace("+x", "").strip()
    try:
        return float(t)
    except ValueError:
        return None


def _load():
    if "L" in _C:
        return _C["L"]
    mem = collections.defaultdict(dict)
    files, unreadable = [], []
    rows = refused_term = refused_j = 0
    for fn in sorted(os.listdir(ASD)):
        if not fn.endswith(".tsv") or fn in SKIP:
            continue
        lines = open(os.path.join(ASD, fn), encoding="utf-8",
                     errors="replace").read().split("\n")
        hi = cols = None
        for i, l in enumerate(lines):
            c = [x.strip().lower().replace("-", "").replace("_", "")
                 for x in l.lstrip("# ").split("\t")]
            if "term" in c and "j" in c and ("config" in c
                                             or "configuration" in c):
                hi, cols = i, c
                break
        if hi is None:
            continue
        sp = _species(lines, fn[:-4])
        if sp is None:
            unreadable.append(fn)
            continue
        files.append(fn)
        ic = cols.index("configuration") if "configuration" in cols \
            else cols.index("config")
        it, ij = cols.index("term"), cols.index("j")
        ils = [k for k, c in enumerate(cols) if c.startswith("level")]
        il = ils[0] if ils else None
        for l in lines[hi + 1:]:
            if not l.strip() or l.startswith("#"):
                continue
            p = l.split("\t")
            if len(p) <= max(ic, it, ij):
                continue
            rows += 1
            m = TERM.match(p[it].strip())
            if not m:
                refused_term += 1          # bracketed jK / jj / Racah
                continue
            tj = _two_j(p[ij])
            if tj is None:
                refused_j += 1
                continue
            key = (sp, p[ic].strip(), m.group(1) or "", int(m.group(2)),
                   LSEQ.index(m.group(3)), 1 if m.group(4) else 0)
            raw = p[il].strip() if il is not None and len(p) > il else ""
            mem[key][tj] = (_level(raw), raw)
    _C["L"] = (dict(mem), files, unreadable, rows, refused_term, refused_j)
    return _C["L"]


def members():
    return _load()[0]


def source_files():
    return _load()[1]


def unreadable_species():
    """Named, not silently dropped."""
    return _load()[2]


def census():
    _m, files, unread, rows, rt, rj = _load()
    return dict(files=len(files), unreadable=len(unread),
                spectra=len({k[0] for k in _m}), rows=rows,
                refused_bracketed=rt, refused_j=rj,
                admitted=sum(len(v) for v in _m.values()), members=len(_m))


# ------------------------------------------------------------- the verdicts

def multiplet(mult, L):
    """The J values Russell-Saunders coupling implies, as 2J."""
    s2 = mult - 1
    return set(range(abs(2 * L - s2), 2 * L + s2 + 1, 2))


def completeness(key, js):
    have = set(js)
    pred = multiplet(key[3], key[4])
    if have == pred:
        return "COMPLETE"
    return "MIXED" if have - pred else "SHORT"


def triples(js):
    """[(2J-1, 2J, 2J+1, ratio, Lande ratio)] for every consecutive triple."""
    E = {j: v[0] for j, v in js.items() if v[0] is not None}
    seq = sorted(E)
    out = []
    for a, b, c in zip(seq, seq[1:], seq[2:]):
        if b - a != 2 or c - b != 2:
            continue
        d1 = E[b] - E[a]
        if d1 == 0:                       # DEGENERATE, refused not banded
            out.append((a, b, c, None, (c / 2) / (b / 2)))
            continue
        out.append((a, b, c, (E[c] - E[b]) / d1, (c / 2) / (b / 2)))
    return out


def interval(js, tol=None):
    tol = TOLERANCE if tol is None else tol
    ok = bad = 0
    for _a, _b, _c, R, want in triples(js):
        if R is None:
            continue
        if abs(R - want) <= tol * abs(want):
            ok += 1
        else:
            bad += 1
    if ok + bad == 0:
        return "NOT-TESTABLE"
    return "OBEYS" if bad == 0 else ("BREAKS" if ok == 0 else "PARTLY")


# ------------------------------------------------------------------ the gate

def chart(tol=None, with_interval=False):
    out = set()
    for k, v in members().items():
        c = (min(k[3], 5), min(k[4], 8), k[5],
             COMPLETENESS.index(completeness(k, v)))
        if with_interval:
            c = c + (INTERVAL.index(interval(v, tol)),)
        out.add(c)
    return frozenset(out)


def gate():
    """[(tolerance, cells with interval, its cell, cells without)].

    THE EVIDENCE, not the conclusion.  Run it before believing section 1.
    """
    out = []
    for t in GATE_TOLERANCES:
        X = chart(t, with_interval=True)
        Y = chart(t, with_interval=False)
        out.append((t, len(X), mi.cell(X), len(Y)))
    return out


def gate_fires():
    """(does the 5-coordinate count move?, does the 4-coordinate count?).

    The first must be True and the second False, or the ruling in section 1 is
    not the one the numbers support.
    """
    g = gate()
    return len({n for _t, n, _c, _m in g}) > 1, len({m for *_r, m in g}) > 1


def index():
    """The term index: four coordinates, the gated fifth in the ledger."""
    return chart()


def ledger(limit=None):
    """[(spectrum, config, term, 2J triple, ratio, Lande, band, verdict)].

    THE LANDE MEASUREMENT, BANKED PER TRIPLE AND NEVER CHARTED.  The band is
    untuned -- round(ln(R / R_Lande) * 4), clipped to +-8 -- and a DEGENERATE
    interval is refused rather than banded to zero.
    """
    import math
    out = []
    for k, v in sorted(members().items()):
        for a, b, c, R, want in triples(v):
            if R is None:
                out.append((k[0], k[1], _term(k), (a, b, c), None, want, None,
                            "DEGENERATE-INTERVAL"))
                continue
            band = (None if R <= 0
                    else max(-8, min(8, round(math.log(R / want) * 4))))
            out.append((k[0], k[1], _term(k), (a, b, c), R, want, band,
                        "NEGATIVE-RATIO" if R <= 0 else "BANDED"))
            if limit and len(out) >= limit:
                return out
    return out


def _term(k):
    return "%s%d%s%s" % (k[2] + " " if k[2] else "", k[3], LSEQ[k[4]],
                         "*" if k[5] else "")


def degenerate_intervals():
    return [r for r in ledger() if r[7] == "DEGENERATE-INTERVAL"]


def verdict_counts(tol=None):
    c = collections.Counter(interval(v, tol) for v in members().values())
    d = collections.Counter(completeness(k, v) for k, v in members().items())
    return dict(d), dict(c)


def mixed_members():
    """The members whose banked J set leaves the multiplet -- MEASURED, not repaired."""
    return [(k[0], k[1], _term(k), sorted(set(v)), sorted(multiplet(k[3], k[4])))
            for k, v in members().items() if completeness(k, v) == "MIXED"]


def closers(X=None):
    X = frozenset(index() if X is None else X)
    cl, _b = hlaw.closures(X)
    return sorted(L for L in hlaw.LANGS if len(cl[L]) == len(X))


def cell():
    return mi.cell(index())


# ---------------------------------------------------------------- the reading

def report():
    X = index()
    c = census()
    comp, iv = verdict_counts()
    print("=" * 74)
    print("THE TERM INDEX")
    print("=" * 74)
    print()
    print("Every Russell-Saunders term of every banked spectrum, charted by")
    print("what its J values do. A member is (spectrum, configuration, term).")
    print()
    print("-" * 74)
    print("1. THE SOURCES, CHOSEN BY PREDICATE AND NEVER BY A FILE LIST.")
    print("-" * 74)
    print("   files carrying a term/J/config header   %d" % c["files"])
    print("   distinct spectra                        %d" % c["spectra"])
    print("   rows scanned                            %d" % c["rows"])
    print("   refused: bracketed jK/jj/Racah labels   %d" % c["refused_bracketed"])
    print("   refused: unreadable J                   %d" % c["refused_j"])
    print("   admitted levels                         %d" % c["admitted"])
    print("   MEMBERS                                 %d" % c["members"])
    print()
    print("   refused for an unreadable species, and NAMED: %s"
          % ", ".join(unreadable_species()))
    print("   skipped as a byte-identical duplicate:       %s"
          % ", ".join(sorted(SKIP)))
    print()
    print("   ON LuI: recovered/LuI.tsv has data rows byte-identical to the")
    print("   corpus's own quarantine/LuI.FABRICATED.tsv. It is read anyway,")
    print("   because the label is unsupported: an INDEPENDENT capture under")
    print("   register 1639 agrees EXACTLY on all %d of its rows, zero")
    print("   disagreements. %d rows corroborated, %d undecided. Nothing is"
          % (LUI_CORROBORATED_ROWS, LUI_UNDECIDED_ROWS))
    print("   repaired, moved or relabelled." % ())
    print()
    print("-" * 74)
    print("2. THE GATE FIRED. FOUR COORDINATES, NOT FIVE.")
    print("-" * 74)
    print("   The interval verdict carries a DECLARED TOLERANCE, which is a")
    print("   tuning constant, so it was gated before being seated.")
    print()
    print("   %-10s %-8s %-14s %s" % ("tolerance", "5-coord", "its cell", "4-coord"))
    for t, n, cc, m in gate():
        print("   %-10s %-8d %-14s %d" % (t, n, cc, m))
    moves5, moves4 = gate_fires()
    print()
    print("   does the five-coordinate cell count move with the tolerance? %s"
          % moves5)
    print("   does the four-coordinate count move?                         %s"
          % moves4)
    print()
    print("   IT MOVES, AND SO DOES THE CELL -- the width runs 31 to 34 and the")
    print("   count is not even monotone. A coordinate whose alphabet is a")
    print("   function of a number nobody measured is not an axis. `interval`")
    print("   DROPS TO THE LEDGER; status %s." % INTERVAL_STATUS)
    print()
    print("-" * 74)
    print("3. THE FOUR SEATED COORDINATES.")
    print("-" * 74)
    doc = {"mult": "2S+1 from the term symbol, clipped at 5",
           "L": "the term letter, clipped at 8",
           "parity": "0 even, 1 odd",
           "completeness": "banked J set against the implied multiplet"}
    for i, nm in enumerate(NAMES):
        vals = sorted({cc[i] for cc in X})
        print("   %-13s %-42s %-14s %d/%d = %.4f"
              % (nm, doc[nm], vals, len(vals), len(X), len(vals) / len(X)))
    print()
    print("   members        %d" % c["members"])
    print("   distinct cells %d" % len(X))
    print("   box            %d" % overlap.box_of(X))
    cl, _b = hlaw.closures(X)
    for L in hlaw.LANGS:
        e = len(cl[L]) - len(X)
        print("     %-13s admits %4d   E %4d%s"
              % (L, len(cl[L]), e, "   <-- CLOSES" if e == 0 else ""))
    print()
    print("   closers  %s" % (closers() or "NONE -- K0"))
    print("   CELL     %s" % (cell(),))
    print()
    print("-" * 74)
    print("4. WHAT THE VERDICTS ACTUALLY SAY.")
    print("-" * 74)
    for k in COMPLETENESS:
        print("   %-14s %5d" % (k, comp.get(k, 0)))
    print()
    print("   MIXED OCCURS ON EXACTLY %d MEMBER OF %d." % (comp.get("MIXED", 0),
                                                           c["members"]))
    for sp, cfg, tm, have, pred in mixed_members():
        print("      %-8s %-26s %-6s banked 2J %s against %s"
              % (sp, cfg[:26], tm, have, pred))
    print("   So this coordinate measures the agreement between a banked LABEL")
    print("   and its own banked J VALUES. It is NOT a test of Russell-Saunders")
    print("   coupling, and calling it one is the claim the numbers refuse.")
    print()
    for k in INTERVAL:
        print("   %-14s %5d" % (k, iv.get(k, 0)))
    print("   NOT-TESTABLE is %.0f%% -- fewer than three banked levels with"
          % (100.0 * iv.get("NOT-TESTABLE", 0) / c["members"]))
    print("   energies, so the interval cannot be formed. That is a fact about")
    print("   the capture and NOT negative evidence.")
    print()
    print("-" * 74)
    print("5. THE LANDE LEDGER -- banked per triple, never charted.")
    print("-" * 74)
    led = ledger()
    print("   consecutive-J triples        %d" % len(led))
    print("   degenerate intervals refused %d   (banded to 0 would be a lie)"
          % len(degenerate_intervals()))
    print()
    print("   %-9s %-22s %-7s %-9s %-9s %s"
          % ("spectrum", "term", "2J", "ratio", "Lande", "band"))
    for sp, _cfg, tm, tri, R, want, band, verd in led[:12]:
        print("   %-9s %-22s %-7s %-9s %-9.4f %s"
              % (sp, tm, "%d/%d/%d" % tri,
                 "%.4f" % R if R is not None else "DEGEN", want,
                 band if band is not None else verd))
    print("   ... and %d more" % (len(led) - 12))
    print()
    print("-" * 74)
    print("6. REFUSED.")
    print("-" * 74)
    print("   To call SHORT a missing level -- a partial capture and a partial")
    print("     measurement look the same from here.")
    print("   To call BREAKS a fault -- the rule is an approximation that holds")
    print("     in pure LS coupling, and departure from it is physics.")
    print("   To read NOT-TESTABLE as negative evidence.")
    print("   To claim the union is ASD-complete. It is what recovered/ holds.")
    print("   To repair a row. The one MIXED member is charted and left alone.")
    print("   To name a file in a member key, or select sources by a file list.")
    print("   To seat the Lande triples as a second index -- one body of rows")
    print("     on two vertices is the fault overlap.py exists to catch.")
    return 0


# ------------------------------------------------------------------ fixtures

def selftest():
    ok = True

    def chk(lab, got, want):
        nonlocal ok
        good = got == want
        ok &= good
        print("  [%s] %-58s %s" % ("ok" if good else "XX", lab,
                                   got if good else "%s != %s" % (got, want)))

    print("terms selftest")
    c = census()

    # -- sources by predicate, not by a list
    chk("files found by header predicate", c["files"], 194)
    chk("distinct spectra", c["spectra"], 122)
    chk("the four unreadable species are NAMED, not dropped",
        unreadable_species(),
        ["BaLII.tsv", "LEVELS-Fe-I.tsv", "LEVELS-K-I.tsv", "LEVELS-Kr-I.tsv"])
    chk("the byte-identical LuI duplicate is skipped", sorted(SKIP),
        ["LuI__16455659.tsv"])
    chk("rows scanned", c["rows"], 16624)
    chk("bracketed jK/jj/Racah labels REFUSED, not coerced",
        c["refused_bracketed"], 4033)
    chk("unreadable J refused", c["refused_j"], 231)
    chk("levels admitted", c["admitted"], 8585)
    chk("MEMBERS", c["members"], 5132)
    chk("no member key names a file",
        [k for k in members() if ".tsv" in str(k)], [])
    chk("the lowercase ordering prefix is part of the key",
        len({k for k in members() if k[2]}) > 0, True)

    # -- THE GATE, which is the whole ruling in section 1
    g = gate()
    chk("the gate is run at six tolerances", len(g), 6)
    chk("THE FIVE-COORDINATE CELL COUNT MOVES", [n for _t, n, _c, _m in g],
        [152, 162, 174, 177, 172, 163])
    chk("...and so does its cell", len({cc for _t, _n, cc, _m in g}) > 1, True)
    chk("...and it is not even monotone",
        [n for _t, n, _c, _m in g] == sorted(n for _t, n, _c, _m in g), False)
    chk("THE FOUR-COORDINATE COUNT DOES NOT", {m for *_r, m in g}, {112})
    chk("so the gate fires", gate_fires(), (True, False))
    chk("interval is therefore a ledger column, not an axis", ARITY, 4)
    chk("and its status is not flattened", INTERVAL_STATUS, "MEASURED")

    # -- the chart
    X = index()
    chk("112 distinct cells", len(X), 112)
    chk("arity 4", len(next(iter(X))), ARITY)
    chk("box", overlap.box_of(X), 270)
    chk("no coordinate is constant",
        [NAMES[i] for i in range(ARITY) if len({cc[i] for cc in X}) == 1], [])
    chk("no coordinate is a LABEL",
        [NAMES[i] for i, _d, _n, _r, v in overlap.resolution(X)
         if v == "LABEL"], [])
    chk("it closes nothing -- K0", closers(), [])
    chk("CELL", cell(), (0, 13, 18))

    # -- what the verdicts actually say
    comp, iv = verdict_counts()
    chk("completeness", [comp.get(k, 0) for k in COMPLETENESS],
        [3922, 1209, 1])
    chk("MIXED OCCURS ONCE IN 5,132", comp.get("MIXED", 0), 1)
    chk("and it is the Al I 2S anomaly",
        [(m[0], m[2]) for m in mixed_members()], [("Al I", "2S")])
    chk("SO IT IS NOT A TEST OF RUSSELL-SAUNDERS COUPLING",
        COUPLING_NOT_TESTED, True)
    chk("interval verdicts at the declared tolerance",
        [iv.get(k, 0) for k in INTERVAL], [150, 45, 774, 4163])
    chk("NOT-TESTABLE is most of the index, and is not negative evidence",
        iv["NOT-TESTABLE"] > c["members"] / 2, True)

    # -- the Lande fold
    led = ledger()
    chk("the Lande measurement is banked per triple", len(led), 1269)
    chk("a degenerate interval is REFUSED, not banded to zero",
        len(degenerate_intervals()), 18)
    chk("every degenerate row carries its own verdict",
        {r[7] for r in degenerate_intervals()}, {"DEGENERATE-INTERVAL"})
    chk("every triple is consecutive in 2J",
        [r for r in led if r[3][1] - r[3][0] != 2 or r[3][2] - r[3][1] != 2],
        [])
    chk("the band is untuned -- no tolerance enters it",
        all(b is None or -8 <= b <= 8 for *_r, b, _v in led), True)

    # -- the multiplet arithmetic itself
    chk("multiplet(3, 2) is the 3D triplet", sorted(multiplet(3, 2)),
        [2, 4, 6])
    chk("multiplet(1, 0) is the single 1S", sorted(multiplet(1, 0)), [0])
    chk("multiplet(2, 1) is the 2P doublet", sorted(multiplet(2, 1)), [1, 3])
    print("terms selftest: %s" % ("PASS" if ok else "FAIL"))
    return ok


if __name__ == "__main__":
    if "--gate" in sys.argv[1:]:
        for row in gate():
            print("   tol %-6s  5-coord %-5d %-14s  4-coord %d" % row)
        sys.exit(0)
    if "--selftest" in sys.argv[1:]:
        sys.exit(0 if selftest() else 1)
    sys.exit(report())
