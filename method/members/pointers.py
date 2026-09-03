#!/usr/bin/env python3
"""tools/pointers.py -- the pointer audit of The Method 1.6, run as a program.

DOCKET.md section 2 requires, of every section read:

    "resolve every pointer to the claim and not the heading, under both
     resolvers, and locate where the claim does live"

and CLAUDE.md section 6 adds that the pointer regex is case-sensitive and that
lowercase "register NNN" and "A.N" are grepped BY HAND. This is that resolution
run as a class over the whole store, in both cases, with the hand-grep folded in.

It answers the four census classes mechanically:

    C1-SECTION-POINTER-UNRESOLVED     a section pointer with no such heading
    C2-THEOREM-POINTER-UNPRINTED      a theorem cited but never stated
    C3-FIGURE-POINTER-UNPLACED        a figure cited but never placed
    C5-REGISTER-POINTER-UNRESOLVED    a register pointer with no such entry

Stdlib only, Python 3.9+. No dependencies, so an audit can run it from any tree.

The one thing it refuses to do:

    It never reports UNRESOLVED for a pointer that resolves somewhere else in
    the roster. DOCKET.md asks where the claim DOES live, so a pointer that
    misses the citing volume and lands in another is RESOLVED, with the member
    named. Four of the census's own C1 rows are this case: reg L5605, reg
    L5609, mc L2474 and ioi L141 all cite a section that exists in the
    companion (Transitions.md) and nowhere else, and the text says so --
    "of the companion", "of T". Calling those unresolved loses the finding.
"""

from __future__ import annotations

import argparse
import collections
import json
import os
import re
import sys

def _repo_root(start=None):
    """The repository root, found by walking up for method/verify.py.

    An instrument travels as a bundle member (chat 68's standing half), so the
    same file runs from tools/ and from method/members/ and must locate the
    store from either. Walking up for a landmark does that; a fixed number of
    dirname() calls does not."""
    d = os.path.dirname(os.path.abspath(start or __file__))
    for _ in range(6):
        if os.path.exists(os.path.join(d, "method", "verify.py")):
            return d
        parent = os.path.dirname(d)
        if parent == d:
            break
        d = parent
    return os.path.dirname(os.path.dirname(os.path.abspath(start or __file__)))


REPO = _repo_root()
DEFAULT_MEMBERS = os.path.join(REPO, "method", "members")

VOLUMES = [
    ("main", "The_Method_1_6-2.md"),
    ("reg", "The_Method_1_6___The_Register-2.md"),
    ("mc", "The_Method_1_6___Mathematical_Compendium-2.md"),
    ("pc", "The_Method_1_6___The_Physics_Compendium-2.md"),
    ("ioi", "The_Method_1_6___The_Index_of_Indices-2.md"),
    ("sc", "The_Method_1_6___Spectra_Compendium-2.md"),
]

COMPANION = [("T", "Transitions.md")]

PAPERS = [
    ("lw", "THE-LOWDIN-SOLUTION-2.md"),
    ("tb", "The_Three_Body_Problem_for_Unknown_Masses_Lach-2.md"),
]

ROSTERS = {
    "volumes": VOLUMES,
    "with-companion": VOLUMES + COMPANION,
    "all": VOLUMES + COMPANION + PAPERS,
}

# The Register is where a register pointer resolves, and nowhere else.
REGISTER_MEMBER = "reg"

RESOLVED_HERE = "RESOLVED-HERE"
RESOLVED = "RESOLVED"
AMBIGUOUS = "AMBIGUOUS"
PREFIX_ONLY = "PREFIX-ONLY"
UNRESOLVED = "UNRESOLVED"
KIND_MISMATCH = "KIND-MISMATCH"
OUT_OF_EXTENT = "OUT-OF-EXTENT"
PARTIAL = "PARTIAL"

VERDICTS = (RESOLVED_HERE, RESOLVED, AMBIGUOUS, PARTIAL, PREFIX_ONLY,
            UNRESOLVED, KIND_MISMATCH, OUT_OF_EXTENT)

# A pointer that lands is not a finding, wherever it lands.
FINDINGS = (PARTIAL, PREFIX_ONLY, UNRESOLVED, KIND_MISMATCH, OUT_OF_EXTENT)

CENSUS_CLASS = {
    "SECTION": "C1-SECTION-POINTER-UNRESOLVED",
    "THEOREM": "C2-THEOREM-POINTER-UNPRINTED",
    "FIGURE": "C3-FIGURE-POINTER-UNPLACED",
    "REGISTER": "C5-REGISTER-POINTER-UNRESOLVED",
    "REGISTER-RANGE": "C5-REGISTER-POINTER-UNRESOLVED",
}


# ---------------------------------------------------------------------------
# Site patterns. The section, chapter, appendix and appendix-section forms are
# copied verbatim from the seated member r2-tools.py (chat 70), which is the
# recorded convention; the register forms are copied from register_cites.py,
# whose (?i) is the reason the hand-grep for lowercase "register NNN" is no
# longer owed. PROVENANCE: both are bundle members, not lifted to r2lib.
# ---------------------------------------------------------------------------

RE_SECTION = re.compile(r"§\s?(\d+\.\d+(?:\.\d+)*|\d+)(?!\d)")
RE_SECTION_LETTERED = re.compile(r"§\s?([A-G]\.\d+(?:\.\d+)*)")
RE_CHAPTER = re.compile(r"\b(?:Chapter|Ch\.)\s?(\d+)\b")
RE_APPENDIX = re.compile(r"\bAppendix ([A-G])\b(?!\.)")
RE_APPSEC = re.compile(r"(?<![A-Za-z§])([A-G]\.\d+)(?![\d.])")
RE_THEOREM = re.compile(r"\b(?:Theorem|Thm\.?)\s?(\d+\.\d+)\b")
RE_FIGURE = re.compile(r"\bFigure (\d+\.\d+)\b")

# register_cites.py's own two patterns, plus the "entry/entries" wording that
# r2-tools.py reads and register_cites.py does not.
RE_REG_WORD = re.compile(
    r"(?i)\b(?:registers?|reg\.|entries|entry)\s+"
    r"((?:\d{3,4}(?:\s*[–\-]\s*\d{3,4})?)"
    r"(?:\s*(?:,|and|/|;)\s*\d{3,4}(?:\s*[–\-]\s*\d{3,4})?)*)"
)
RE_REG_R = re.compile(
    r"(?:\*R|\bR) ((?:\d{3,4}(?:\s*[–\-]\s*\d{3,4})?)"
    r"(?:\s*(?:,|and|/|;)\s*\d{3,4}(?:\s*[–\-]\s*\d{3,4})?)*)"
)

# register_cites.py's floor. Below 165 a three-digit token is not a register
# citation, and reading it as one was the fault that entry 1000 records.
REG_FLOOR = 165
REG_RANGE_CAP = 200

# Declaration and placement forms, calibrated against the store.
#   "Theorem 14.1 (A.2). X is closed iff X = R(X)"   <- declared
#   "Theorem 18.2 permits it, because an interval"   <- merely cited
RE_THM_DECL = re.compile(
    r"\b(?:Theorem|Thm\.?)\s?(\d+\.\d+)\s*(?:\([^)]*\))?\.\s")
RE_FIG_PLACED = re.compile(r"^!\[Figure (\d+\.\d+)")
RE_HEADING = re.compile(r"^(#{2,6}) (.+)$")
# DOCKET.md: heading_line is numeric-only.
RE_HEAD_NUM = re.compile(r"^([A-G]\.\d+(?:\.\d+)*|\d+\.\d+(?:\.\d+)*)[\s.]")
RE_HEAD_CH = re.compile(r"^(\d+)\.\s")
RE_HEAD_APP = re.compile(r"^Appendix ([A-G])")
RE_REG_HEAD = re.compile(r"^### ([\d, ]+)")
# Appendix A states most of its proofs as a labelled TABLE, not as headings:
#   "  A.2       X closed <=> R(X) = X        SS14.1, in full"
# while A.3, A.8 and A.9 take "### A.n" headings. This is what CLAUDE.md
# section 6 means by the pointer regex "ignoring Appendix A item numbers" and
# owing a hand grep: A.1, A.2, A.4-A.7, A.14, A.16 and A.17 are table rows.
RE_APP_ITEM = re.compile(r"^\s{2,}([A-G]\.\d+)\s{2,}\S")


class Site:
    __slots__ = ("cls", "token", "member", "lines", "verdict", "where", "note")

    def __init__(self, cls, token, member, lines, verdict, where, note=""):
        self.cls = cls
        self.token = token
        self.member = member
        self.lines = lines
        self.verdict = verdict
        self.where = where
        self.note = note

    def asdict(self):
        return {"class": self.cls, "token": self.token, "member": self.member,
                "lines": self.lines, "verdict": self.verdict,
                "where": self.where, "note": self.note,
                "census_class": (CENSUS_CLASS.get(self.cls, "")
                                 if self.verdict in FINDINGS else "")}


# ---------------------------------------------------------------------------
# The index of what a pointer can land on
# ---------------------------------------------------------------------------

class Index:
    def __init__(self):
        self.sections = collections.defaultdict(list)
        self.chapters = collections.defaultdict(list)
        self.appendices = collections.defaultdict(list)
        self.appsecs = collections.defaultdict(list)
        self.theorems = collections.defaultdict(list)
        self.figures = collections.defaultdict(list)
        self.register = {}
        self.body = set()
        self.reg_grouped = set()
        self.reg_extent = (0, 0)


def _is_body(lines, i):
    """Is the heading on 1-based line i a BODY heading, or a contents entry?

    DOCKET.md section 2: the heading resolver resolves to the BODY occurrence,
    and the same section records that the volume heads its appendices
    "## Appendix X -- ..." twice. Line 162 of the main volume is the contents
    -- seven appendix headings in a row with no prose between them -- and line
    9939 is Appendix A itself. A contents entry is a heading followed by
    another heading; a body heading is followed by prose."""
    for j in range(i, min(i + 3, len(lines))):
        nxt = lines[j]
        if not nxt.strip():
            continue
        return not bool(RE_HEADING.match(nxt))
    return False


def build_index(lines):
    ix = Index()
    for i, line in enumerate(lines, 1):
        m = RE_APP_ITEM.match(line)
        if m:
            # A labelled proof row is a placement, and a body one.
            ix.appsecs[m.group(1)].append(i)
            ix.body.add((("appsecs"), m.group(1), i))
        h = RE_HEADING.match(line)
        if h:
            title = h.group(2)
            body = _is_body(lines, i)
            m = RE_HEAD_NUM.match(title)
            if m:
                tok = m.group(1)
                which = "appsecs" if tok[0].isalpha() else "sections"
                getattr(ix, which)[tok].append(i)
                if body:
                    ix.body.add((which, tok, i))
            mc = RE_HEAD_CH.match(title)
            if mc and h.group(1) == "##":
                ix.chapters[mc.group(1)].append(i)
                if body:
                    ix.body.add(("chapters", mc.group(1), i))
            ma = RE_HEAD_APP.match(title)
            if ma and h.group(1) == "##":
                ix.appendices[ma.group(1)].append(i)
                if body:
                    ix.body.add(("appendices", ma.group(1), i))
        for m in RE_THM_DECL.finditer(line):
            ix.theorems[m.group(1)].append(i)
        m = RE_FIG_PLACED.match(line)
        if m:
            ix.figures[m.group(1)].append(i)
        m = RE_REG_HEAD.match(line)
        if m:
            nums = re.findall(r"\d+", m.group(1))
            for n in nums:
                ix.register.setdefault(int(n), (i, line[:60]))
                if len(nums) > 1:
                    ix.reg_grouped.add(int(n))
    if ix.register:
        ix.reg_extent = (min(ix.register), max(ix.register))
    return ix


RE_REG_SPAN = re.compile(r"(\d{3,4})\s*[–\-]\s*(\d{3,4})")


def _reg_ranges(blob):
    """The spans inside a register citation, as (a, b) pairs.

    A span is ONE claim about a stretch of the Register, not one claim per
    number in it. The Spectra Compendium's "Registers 1524-1677 record the
    capture of these bodies one at a time" is a single sentence; expanding it
    into 154 pointers and reporting 30 of them turns one finding about the
    range into thirty rows, and DOCKET.md section 2 wants a sweep to state
    what it covered."""
    out = []
    for m in RE_REG_SPAN.finditer(blob):
        a, b = int(m.group(1)), int(m.group(2))
        if REG_FLOOR <= a <= b and (b - a) < REG_RANGE_CAP:
            out.append((a, b))
    return out


def _reg_nums(blob, top):
    """register_cites.py's nums(), copied verbatim in substance: a range is
    expanded only when it is inside the extent and shorter than 200, and a
    token below 165 is not a register citation at all."""
    out = set()
    for part in re.split(r"\s*(?:,|and|/|;)\s*", blob):
        part = part.strip()
        m = re.match(r"(\d{3,4})\s*[–\-]\s*(\d{3,4})$", part)
        if m:
            a, b = int(m.group(1)), int(m.group(2))
            if REG_FLOOR <= a <= b and (b - a) < REG_RANGE_CAP:
                out.update(range(a, b + 1))
        elif part.isdigit():
            n = int(part)
            if n >= REG_FLOOR:
                out.add(n)
    return out


# ---------------------------------------------------------------------------
# Collecting sites
# ---------------------------------------------------------------------------

def collect(short, lines, classes):
    """token sites in one member: {(class, token): [line numbers]}"""
    seen = collections.OrderedDict()

    def add(cls, tok, i):
        if cls in classes:
            seen.setdefault((cls, tok), []).append(i)

    for i, line in enumerate(lines, 1):
        if RE_HEADING.match(line):
            continue  # a heading is not a pointer to itself
        for m in RE_SECTION.finditer(line):
            add("SECTION", m.group(1), i)
        for m in RE_SECTION_LETTERED.finditer(line):
            add("APPSEC", m.group(1), i)
        for m in RE_CHAPTER.finditer(line):
            add("CHAPTER", m.group(1), i)
        for m in RE_APPENDIX.finditer(line):
            add("APPENDIX", m.group(1), i)
        for m in RE_APPSEC.finditer(line):
            add("APPSEC", m.group(1), i)
        for m in RE_THEOREM.finditer(line):
            add("THEOREM", m.group(1), i)
        for m in RE_FIGURE.finditer(line):
            add("FIGURE", m.group(1), i)
        for rx in (RE_REG_WORD, RE_REG_R):
            for m in rx.finditer(line):
                blob = m.group(1)
                spans = _reg_ranges(blob)
                spanned = set()
                for a, b in spans:
                    add("REGISTER-RANGE", "%d-%d" % (a, b), i)
                    spanned.update(range(a, b + 1))
                for n in _reg_nums(blob, None):
                    if n not in spanned:
                        add("REGISTER", str(n), i)
    return seen


ATTR = {"SECTION": "sections", "CHAPTER": "chapters",
        "APPENDIX": "appendices", "APPSEC": "appsecs",
        "THEOREM": "theorems", "FIGURE": "figures"}


def _lookup(ix, cls, tok):
    """Every occurrence, body ones first. A pointer resolves to the body
    occurrence when there is one; a contents entry alone is not a claim.

    A section pointer with no dot is a CHAPTER pointer written with a section
    sign -- the volumes write "SS12" for chapter 12, whose heading is
    "## 12. ...". r2-tools.py has this fallback ("if key.count('.')==0:
    heads.get('ch'+key)") and it is the recorded convention; without it 59
    whole-chapter pointers read PREFIX-ONLY against their own sub-sections."""
    which = ATTR[cls]
    all_hits = ix.__getattribute__(which).get(tok, [])
    if not all_hits and cls == "SECTION" and "." not in tok:
        which = "chapters"
        all_hits = ix.chapters.get(tok, [])
    body = [i for i in all_hits if (which, tok, i) in ix.body]
    return body or all_hits


def _prefix_hit(ix, cls, tok):
    """The second resolver, named. DOCKET.md section 2: the heading resolver is
    exact-token and NEVER prefix. Running both and reporting the difference is
    how a pointer to a section that exists only as sub-sections is told apart
    from one that does not exist at all: PREFIX-ONLY, not UNRESOLVED."""
    if cls not in ("SECTION", "APPSEC"):
        return []
    table = ix.sections if cls == "SECTION" else ix.appsecs
    return sorted(l for k, v in table.items()
                  if k.startswith(tok + ".") for l in v)


def resolve(short, cls, tok, indexes):
    if cls == "REGISTER-RANGE":
        ix = indexes.get(REGISTER_MEMBER)
        if ix is None:
            return UNRESOLVED, "", "the Register is not in the roster"
        a, b = (int(x) for x in tok.split("-"))
        want = list(range(a, b + 1))
        absent = [n for n in want if n not in ix.register]
        lo, hi = ix.reg_extent
        if not absent:
            return (RESOLVED, "%s:%d" % (REGISTER_MEMBER, ix.register[a][0]),
                    "all %d entries present" % len(want))
        if len(absent) == len(want):
            return (UNRESOLVED, "",
                    "none of the %d numbers in the range carries an entry"
                    % len(want))
        shown = ", ".join(str(n) for n in absent[:12])
        if len(absent) > 12:
            shown += ", +%d more" % (len(absent) - 12)
        return (PARTIAL, "%s:%d" % (REGISTER_MEMBER, ix.register[want[0]][0])
                if want[0] in ix.register else "",
                "%d of the %d numbers in the range carry an entry; absent: %s"
                % (len(want) - len(absent), len(want), shown))

    if cls == "REGISTER":
        ix = indexes.get(REGISTER_MEMBER)
        if ix is None:
            return UNRESOLVED, "", "the Register is not in the roster"
        n = int(tok)
        lo, hi = ix.reg_extent
        if n > hi:
            return (OUT_OF_EXTENT, "",
                    "beyond the Register's extent, %d to %d" % (lo, hi))
        if n in ix.register:
            line, head = ix.register[n]
            note = "grouped heading" if n in ix.reg_grouped else ""
            return RESOLVED, "%s:%d" % (REGISTER_MEMBER, line), note
        return UNRESOLVED, "", "no ### entry in the Register"

    # A three- or four-digit section pointer with no dot has the shape of a
    # register number, not of a section. reg L3113's "§784" is the census's
    # own C1 row and this is what it is.
    if cls == "SECTION" and "." not in tok and len(tok) >= 3:
        reg = indexes.get(REGISTER_MEMBER)
        n = int(tok)
        if reg and n >= REG_FLOOR and n <= reg.reg_extent[1]:
            seat = reg.register.get(n)
            return (KIND_MISMATCH,
                    "%s:%d" % (REGISTER_MEMBER, seat[0]) if seat else "",
                    "a register number written as a section pointer"
                    + ("" if seat else "; and no such entry either"))

    hits = {}
    for k, ix in indexes.items():
        got = _lookup(ix, cls, tok)
        if got:
            hits[k] = got

    if short in hits:
        extra = [k for k in hits if k != short]
        note = ("also in " + ", ".join(sorted(extra))) if extra else ""
        ix = indexes[short]
        which = ATTR[cls]
        every = ix.__getattribute__(which).get(tok, [])
        if not every and cls == "SECTION" and "." not in tok:
            every = ix.chapters.get(tok, [])
        if len(every) > len(hits[short]):
            note = ((note + "; ") if note else "") + (
                "%d contents entr%s above the body occurrence"
                % (len(every) - len(hits[short]),
                   "y" if len(every) - len(hits[short]) == 1 else "ies"))
        return RESOLVED_HERE, "%s:%d" % (short, hits[short][0]), note
    if len(hits) == 1:
        k = next(iter(hits))
        return RESOLVED, "%s:%d" % (k, hits[k][0]), ""
    if len(hits) > 1:
        return (AMBIGUOUS,
                ", ".join("%s:%d" % (k, v[0]) for k, v in sorted(hits.items())),
                "the pointer does not say which volume")

    for k, ix in indexes.items():
        pre = _prefix_hit(ix, cls, tok)
        if pre:
            return (PREFIX_ONLY, "%s:%d" % (k, pre[0]),
                    "no exact heading; %d sub-section heading(s) begin '%s.' "
                    "-- the exact-token resolver is the one in force"
                    % (len(pre), tok))

    if cls == "THEOREM":
        return UNRESOLVED, "", "cited but never stated in the roster"
    if cls == "FIGURE":
        return UNRESOLVED, "", "cited but never placed in the roster"
    return UNRESOLVED, "", "no such heading in the roster"


def audit(members_dir, roster, classes):
    lines = {}
    for short, fname in roster:
        path = os.path.join(members_dir, fname)
        with open(path, encoding="utf-8") as fh:
            lines[short] = fh.read().split("\n")
    indexes = {k: build_index(v) for k, v in lines.items()}

    out = []
    for short, _ in roster:
        for (cls, tok), sites in collect(short, lines[short], classes).items():
            verdict, where, note = resolve(short, cls, tok, indexes)
            out.append(Site(cls, tok, short, sorted(set(sites)), verdict,
                            where, note))
    return out, indexes


# ---------------------------------------------------------------------------
# Reporting
# ---------------------------------------------------------------------------

def report(sites, only=None, limit_lines=6):
    order = {v: i for i, v in enumerate(VERDICTS)}
    shown = [s for s in sites if not only or s.verdict in only]
    shown.sort(key=lambda s: (-order.get(s.verdict, 0), s.cls, s.member,
                              s.lines[0] if s.lines else 0))
    for s in shown:
        ls = ",".join(str(x) for x in s.lines[:limit_lines])
        if len(s.lines) > limit_lines:
            ls += "+%d" % (len(s.lines) - limit_lines)
        token = ("§" + s.token if s.cls == "SECTION" else
                 "reg " + s.token if s.cls.startswith("REGISTER") else s.token)
        print("%-4s %-15s %-11s at L%-18s %s"
              % (s.member, s.cls, token, ls, s.verdict))
        tail = []
        if s.where:
            tail.append("-> " + s.where)
        if s.note:
            tail.append(s.note)
        if tail:
            print("      " + "  ".join(tail))
        if s.verdict in FINDINGS and s.cls in CENSUS_CLASS:
            print("      census class %s" % CENSUS_CLASS[s.cls])

    tally = collections.Counter(s.verdict for s in sites)
    cls_find = collections.Counter(s.cls for s in sites
                                  if s.verdict in FINDINGS)
    print()
    print("-" * 72)
    print("  ".join("%s %d" % (v, tally[v]) for v in VERDICTS if tally[v]))
    findings = sum(tally[v] for v in FINDINGS)
    print("%d pointer token%s, %d finding%s%s"
          % (len(sites), "" if len(sites) == 1 else "s",
             findings, "" if findings == 1 else "s",
             ("  (" + ", ".join("%s %d" % (c, n)
                                for c, n in sorted(cls_find.items())) + ")")
             if cls_find else ""))
    return findings


def report_extent(sites, indexes):
    """A gap in the Register's numbering is only a defect if something cites
    it. The extent is stated as a range; 1660 of the 1792 numbers in it carry a
    ### entry, and an uncited absence is not a pointer failure. This lists the
    absences that ARE cited, with the citing sites."""
    reg = indexes.get(REGISTER_MEMBER)
    if reg is None:
        print("the Register is not in the roster")
        return 0
    lo, hi = reg.reg_extent
    missing = [n for n in range(lo, hi + 1) if n not in reg.register]
    cited = collections.defaultdict(list)
    for s in sites:
        if s.cls == "REGISTER" and s.verdict in (UNRESOLVED, OUT_OF_EXTENT):
            cited[int(s.token)].extend("%s:%d" % (s.member, l) for l in s.lines)
    print("Register extent %d to %d; %d numbers carry a ### entry, %d do not."
          % (lo, hi, len(reg.register), len(missing)))
    print("An uncited absence is not a pointer failure. Cited absences:")
    print()
    for n in sorted(cited):
        print("  reg %-5d cited at %s" % (n, ", ".join(sorted(set(cited[n])))[:100]))
    print()
    print("%d cited absence%s of %d absences in the extent."
          % (len(cited), "" if len(cited) == 1 else "s", len(missing)))
    return len(cited)


# ---------------------------------------------------------------------------
# Self-test. Every fixture is a row the DEFECT-CENSUS.tsv already records, or a
# convention the store already fixes. Addressed by token and member, never by
# line number.
# ---------------------------------------------------------------------------

# (roster, member, class, token, expected verdict, census id if any)
CORPUS = [
    # C3: the one recorded figure row. 32 figures placed, 33 cited.
    ("volumes", "main", "FIGURE", "15.3", UNRESOLVED, "census 1"),
    ("volumes", "main", "FIGURE", "15.1", RESOLVED_HERE, ""),
    # C2: theorems cited and never stated.
    ("volumes", "main", "THEOREM", "7.1", UNRESOLVED, "census 2"),
    ("volumes", "reg", "THEOREM", "11.2", UNRESOLVED, "census 4, 5"),
    ("volumes", "reg", "THEOREM", "12.1", UNRESOLVED, "census 6, 9"),
    ("volumes", "mc", "THEOREM", "10.1", UNRESOLVED, "census 19, 20"),
    ("volumes", "mc", "THEOREM", "4.4", UNRESOLVED, "census 23"),
    # ... against ones that ARE stated, so the class is not vacuous.
    ("volumes", "main", "THEOREM", "14.1", RESOLVED_HERE, ""),
    ("volumes", "main", "THEOREM", "18.2", RESOLVED_HERE, ""),
    # C5: register pointers with no entry.
    ("volumes", "reg", "REGISTER", "1002", UNRESOLVED, "census 15-17"),
    ("volumes", "reg", "REGISTER", "1000", UNRESOLVED, "census 8"),
    ("volumes", "reg", "REGISTER", "1725", UNRESOLVED, "census 3"),
    ("volumes", "mc", "REGISTER", "1173", RESOLVED, ""),
    # A range is one claim about a stretch of the Register, not one per number.
    ("volumes", "sc", "REGISTER-RANGE", "1524-1677", PARTIAL, ""),
    # C1: a register number written as a section pointer.
    ("volumes", "reg", "SECTION", "784", KIND_MISMATCH, "census 7"),
    # C1: the companion's sections. Unresolved among the volumes ...
    ("volumes", "reg", "SECTION", "5.7", UNRESOLVED, "census 10, 11"),
    ("volumes", "mc", "SECTION", "6.5", UNRESOLVED, "census 24"),
    ("volumes", "ioi", "SECTION", "5.7", UNRESOLVED, "census 26"),
    # ... and RESOLVED, in Transitions.md, once the companion is in the roster.
    # This is the refusal: the claim does live somewhere, and the text says so.
    ("with-companion", "reg", "SECTION", "5.7", RESOLVED, "census 10, 11"),
    ("with-companion", "mc", "SECTION", "6.5", RESOLVED, "census 24"),
    ("with-companion", "mc", "SECTION", "5.1", RESOLVED, "census 25"),
    ("with-companion", "ioi", "SECTION", "5.7", RESOLVED, "census 26"),
    # A section of the main volume, cited from the main volume.
    ("volumes", "main", "SECTION", "17.1", RESOLVED_HERE, ""),
    # Appendix A states A.2 as a proof-TABLE row and A.3 as a "### A.3"
    # heading. Both are placements; a heading-only resolver misses the table.
    ("volumes", "main", "APPSEC", "A.2", RESOLVED_HERE, ""),
    ("volumes", "main", "APPSEC", "A.3", RESOLVED_HERE, ""),
    ("volumes", "main", "APPSEC", "A.17", RESOLVED_HERE, ""),
    # Recorded, not new: WORKING-REGISTER L4687 has "SS4.4/SS4.6/SS4.7 resolve
    # to unheaded lines", and DEFERRED L156 dockets it for R3.
    ("volumes", "main", "SECTION", "4.6", UNRESOLVED, "WR L4687, DEF L156"),
    # Recorded, not new: the same WR line has "259 and 287-class pointers
    # resolve only to groups".
    ("volumes", "main", "REGISTER", "287", UNRESOLVED, "WR L4687"),
    # "SS12" is chapter 12, whose heading is "## 12. ...", per r2-tools.py.
    ("volumes", "main", "SECTION", "12", RESOLVED_HERE, ""),
    ("volumes", "main", "SECTION", "27", RESOLVED_HERE, ""),
    # census 14 records SS0 at reg L6311 as C1-UNRESOLVED, and among the
    # volumes it is. Adding the companion makes it PREFIX-ONLY, because
    # SS0.1 to SS0.4 exist -- in Transitions.md. The citation is to the
    # SPECTRA COMPENDIUM's SS0, so that prefix hit is a coincidence in the
    # wrong member, and both rosters are asserted to keep it visible.
    ("volumes", "reg", "SECTION", "0", UNRESOLVED, "census 14"),
    ("with-companion", "reg", "SECTION", "0", PREFIX_ONLY, "census 14"),
    ("volumes", "main", "APPSEC", "E.4", PREFIX_ONLY, ""),
]

# Conventions the store fixes, asserted directly.
UNITS = [
    # (index attribute, member, key, present?)
    ("theorems", "main", "18.1", True),
    ("theorems", "main", "7.1", False),
    ("figures", "main", "15.1", True),
    ("figures", "main", "15.3", False),
    ("appsecs", "main", "A.2", True),
    ("appsecs", "main", "A.3", True),
]

# The contents/body rule, asserted on the two occurrences the store carries.
BODY = [
    # (member, attribute, token, the line a pointer must resolve to)
    ("main", "APPENDIX", "A", 9939),   # not 162, the contents
    ("main", "CHAPTER", "4", 1436),    # not 117, the contents
]

# A theorem STATEMENT and a theorem CITATION differ by the period.
DECL = [
    ("Theorem 14.1 (A.2). X is closed iff X = R(X), where R recon", True),
    ("Theorem 17.1 (adjunction never repairs). For any h : S -> H", True),
    ("Theorem 18.1. On a product order, join, meet and comparability", True),
    (" Theorem 18.2 permits it, because an interval", False),
    ("Theorem 7.1 is absent -- withdrawn, and the status coordinate", False),
    ("Theorem 14.1 is A.2 by its own", False),
]

# register_cites.py's floor, and its range cap.
REGNUMS = [
    ("register 1173", {1173}),
    ("registers 1201-1203", {1201, 1202, 1203}),
    ("R 1002", set()),          # RE_REG_R is a separate pattern; see below
    ("entry 164", set()),       # below the 165 floor: not a citation
    ("entry 165", {165}),
    ("registers 200-900", set()),  # a 700-wide range is not a citation
]


def selftest(members_dir):
    fails = []
    checked = 0

    for line, want in DECL:
        checked += 1
        got = bool(RE_THM_DECL.search(line))
        if got != want:
            fails.append("declaration test on %r: got %s, expected %s"
                         % (line[:44], got, want))

    for blob, want in REGNUMS:
        checked += 1
        got = set()
        for rx in (RE_REG_WORD, RE_REG_R):
            for m in rx.finditer(blob):
                got |= _reg_nums(m.group(1), None)
        if blob == "R 1002":
            want = {1002}  # the "R NNN" form does resolve as a citation
        if got != want:
            fails.append("register numbers in %r: got %s, expected %s"
                         % (blob, sorted(got), sorted(want)))

    cache = {}

    def run(roster_name):
        if roster_name not in cache:
            cache[roster_name] = audit(members_dir, ROSTERS[roster_name],
                                       set(CENSUS_CLASS) | {"CHAPTER",
                                                            "APPENDIX",
                                                            "APPSEC"})
        return cache[roster_name]

    for member, cls, tok, want_line in BODY:
        checked += 1
        _, indexes = run("volumes")
        got = _lookup(indexes[member], cls, tok)
        if not got or got[0] != want_line:
            fails.append("%s %s in %s resolves to %s, expected the body "
                         "occurrence at L%d" % (cls, tok, member, got,
                                                want_line))

    for attr, member, key, want in UNITS:
        checked += 1
        _, indexes = run("volumes")
        got = bool(getattr(indexes[member], attr).get(key))
        if got != want:
            fails.append("index %s[%s] in %s: got %s, expected %s"
                         % (attr, key, member, got, want))

    for roster, member, cls, tok, want, cid in CORPUS:
        checked += 1
        sites, _ = run(roster)
        hits = [s for s in sites if s.member == member and s.cls == cls
                and s.token == tok]
        if not hits:
            fails.append("%s %s %s not cited in %s under roster %s"
                         % (cls, tok, cid, member, roster))
        elif hits[0].verdict != want:
            fails.append("%s %s in %s (%s, roster %s): verdict %s, expected %s"
                         % (cls, tok, member, cid or "-", roster,
                            hits[0].verdict, want))

    print("fixtures checked: %d  failed: %d" % (checked, len(fails)))
    for f in fails:
        print("  FAIL " + f)
    print()
    print("SELFTEST OK" if not fails else "SELFTEST FAILED")
    return 0 if not fails else 1


def main(argv=None):
    ap = argparse.ArgumentParser(
        description="The pointer audit of The Method 1.6, run as a program.")
    ap.add_argument("--members", default=DEFAULT_MEMBERS)
    ap.add_argument("--roster", default="with-companion",
                    help="which members are in scope (default: with-companion)")
    ap.add_argument("--list-rosters", action="store_true")
    ap.add_argument("--class", dest="classes", action="append", default=[],
                    choices=sorted(set(CENSUS_CLASS) | {"CHAPTER", "APPENDIX",
                                                        "APPSEC"}),
                    help="restrict to this pointer class; repeatable")
    ap.add_argument("--only", help="report only these verdicts, comma-separated")
    ap.add_argument("--findings", action="store_true",
                    help="shorthand for --only " + ",".join(FINDINGS))
    ap.add_argument("--extent", action="store_true",
                    help="the Register's numbering gaps, and which are cited")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--selftest", action="store_true")
    args = ap.parse_args(argv)

    if args.list_rosters:
        for name, roster in sorted(ROSTERS.items()):
            print("%-16s %s" % (name, " ".join(s for s, _ in roster)))
        return 0
    if args.selftest:
        return selftest(args.members)
    if args.roster not in ROSTERS:
        ap.error("unknown roster %r; --list-rosters shows them" % args.roster)

    classes = set(args.classes) or (set(CENSUS_CLASS) | {"CHAPTER", "APPENDIX",
                                                         "APPSEC"})
    sites, indexes = audit(args.members, ROSTERS[args.roster], classes)

    if args.extent:
        report_extent(sites, indexes)
        return 0

    only = list(FINDINGS) if args.findings else None
    if args.only:
        only = [v.strip().upper() for v in args.only.split(",")]
        for v in only:
            if v not in VERDICTS:
                ap.error("unknown verdict %r" % v)

    if args.json:
        json.dump({"roster": args.roster,
                   "sites": [s.asdict() for s in sites
                             if not only or s.verdict in only]},
                  sys.stdout, indent=2, ensure_ascii=False)
        print()
        return 0

    report(sites, only=only)
    return 0


if __name__ == "__main__":
    sys.exit(main())
