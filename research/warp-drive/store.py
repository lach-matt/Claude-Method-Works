#!/usr/bin/env python3
r"""
store.py -- THE FIRST-ORDER INDEXES THE ARTEFACT STORE CARRIES.  Six were
named; there are THIRTEEN, and the seven nobody had listed include the store of
record itself.

M: "We are trying to identify first-order indexes. Every time we think we have
identified all of them, more show up. The complete characterization index is not
settled until all first-order indexes are identified and built."

    python3 store.py                     the reading
    python3 store.py --selftest          fixtures, channel-cheap indexes only
    python3 store.py --selftest --slow   every channel, and it takes an hour

===============================================================================
0. SIX WERE NAMED.  THIRTEEN WERE THERE.
===============================================================================

M: "Every time we think we have identified all of them, more show up."  This
file was written to build the six `sources.py` named, and while building them the
tree was checked for generated tables that nobody had listed.  **Seven more.**

    method/MEMBER-INDEX.tsv     343 members -- THE STORE OF RECORD ITSELF
    extracted/LEDGER.tsv        2,504 source occurrences over 40 archives
    PROSE-ONLY.tsv              1,168 statements the chats hold and the repo does not
    RETRACTION-AUDIT.tsv        391 rows -- is a withdrawn figure still standing
    drive/chats/INDEX.tsv       352 conversations, with message counts
    HANDOFF-GAP.tsv             26 handoffs cited by number
    drive/PENDING.tsv           4 rows, outstanding by decision

THE MEMBER INDEX IS THE ONE THAT SHOULD HAVE BEEN OBVIOUS.  `method/` is the
store of record for The Method 1.6 -- 343 members, byte-exact, md5 per member --
and it is the first thing `CLAUDE.md` says to read.  `sources.py` named the BUILD
snapshots and the drive mirror and did not name the members themselves.

    SO THE COUNT IS NOT THE POINT AND THIS FILE SAYS SO IN ITS OWN CONSTANT.
    `UNNAMED_SOURCES_MAY_EXIST = True` was already here when six was the number;
    it is still here at thirteen, and the jump from six to thirteen is the
    evidence for it rather than an argument against.

===============================================================================
1. WHY THESE AND NOT A CHOICE
===============================================================================

`sources.py` named six first-order sources this tree had not built and ruled them
out of scope.  DOCKET 13 recorded that the ruling was taken under a scope that
has since moved.  These are those six, in the order that file names them, with
nothing added and nothing dropped:

    the BUILD series      the build snapshots, by number and stream
    the drive manifest    every mirrored file, by kind, size and depth
    the Register          every hole in the Register's numbering
    the recovered ledger  every conversation, by what was recovered from it
    the coverage census   every artefact name, by family and disposition
    the dockets           this tree's own open questions

and the seven that were not named:

    the member index      the 343 seated members of The Method 1.6
    the extracted ledger  the archives, by what came out of each
    the prose-only list   the conversations, by what they hold and the repo lacks
    the retraction audit  every withdrawn figure, by whether it still stands
    the chat export       the 352 conversations, by size
    the handoff gap       the handoffs cited by number and not held
    the pending list      what the mirror still owes

    FIRST-ORDER MEANS THE MEMBERS ARE THINGS THE CORPUS BANKS.  Not measurements
    of the seated indexes -- that is second-order, and `sources.py` measured that
    its supply is unbounded.  Each of the six below reads a generated table and
    charts its rows.

    THE CORPUS IS READ AND NEVER WRITTEN.  Every source here is a `.tsv` the
    corpus's own instruments generate, opened read-only.  `CLAUDE.md` governs
    those trees; this file adds nothing to them and regenerates nothing.

===============================================================================
2. EVERY COORDINATE IS A COUNT OR A MEASURED QUANTITY, NEVER A RANKING
===============================================================================

A categorical column -- a mime type, a gap class, a docket state -- has no order,
and inventing one puts a RECONSTRUCTED status into every figure downstream.  So
no category is ranked here.  Instead a category contributes **how many rows
carry it**, which is a measurement of the table and is ordered because integers
are.

    mime type  ->  how many of the 820 files are that type
    gap class  ->  how many of the 132 gaps are that class
    stream     ->  how many builds are in that stream

    THAT IS THE ONE DESIGN DECISION IN THIS FILE and it is what keeps
    `STATUS_ORDER_IS_RECONSTRUCTED` -- which `axes.py` and `obstruction.py` both
    have to carry -- out of it entirely.  It costs something: two categories of
    equal size become the same coordinate value, so the chart cannot tell a PDF
    from a ZIP if the mirror holds equally many.  `collisions()` reports where
    that happens rather than leaving it to be discovered.

===============================================================================
3. WHAT IS MEASURED AND WHAT IS NOT
===============================================================================

Each index gets its cell on the same admissible chart every other index in this
tree uses, and each is put through DOCKET 3's criterion in `criterion()`.  What
this file does NOT do is claim any of them fills a cell the figure demands.
`occupy.py` measured that eight of the ten demanded cells need 18 to 30 members
and can only be first-order; these are the first six first-order indexes built
since.  Section 5 reports where each lands, and the two indexes built before the
demand table was read both missed.

===============================================================================
4. WHAT THIS FILE REFUSES
===============================================================================

To read a table the corpus does not generate.  Every file is listed in
`SOURCES` and every one is produced by a named instrument.  Nothing is scraped and no tree is
walked; `CLAUDE.md` is explicit that the store is read from its manifests.

To treat thirteen as complete.  M's point is that the supply keeps growing, and
this file is the evidence: it set out to build six and found seven more by
looking.  A fourteenth found tomorrow is a fourteenth index.
`UNNAMED_SOURCES_MAY_EXIST = True`.

To smooth a table.  Where a column is empty or unparseable the row is counted as
`skipped` and reported, never guessed at.
"""

import collections
import csv
import os
import re
import sys

import hlaw
import mi

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
UNNAMED_SOURCES_MAY_EXIST = True

SOURCES = {
    "build series": "drive/MANIFEST.tsv",
    "drive manifest": "drive/MANIFEST.tsv",
    "register gaps": "REGISTER-GAPS.tsv",
    "recovered ledger": "recovered/LEDGER.tsv",
    "coverage census": "COVERAGE.tsv",
    "dockets": "research/warp-drive/DOCKET.md",
    "member index": "method/MEMBER-INDEX.tsv",
    "extracted ledger": "extracted/LEDGER.tsv",
    "prose-only list": "PROSE-ONLY.tsv",
    "retraction audit": "RETRACTION-AUDIT.tsv",
    "chat export": "drive/chats/INDEX.tsv",
    "handoff gap": "HANDOFF-GAP.tsv",
    "pending list": "drive/PENDING.tsv",
}
_SKIPPED = {}

# Above this many cells, measuring a channel costs minutes; the selftest skips
# those by default and SAYS SO.  See the note in selftest().
CHANNEL_BUDGET = 150


def _rows(rel):
    with open(os.path.join(ROOT, rel), newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f, delimiter="\t"))


def _int(v):
    try:
        return int(v)
    except (TypeError, ValueError):
        return None


def _tally(vals):
    """{value: how many rows carry it} -- a category's contribution."""
    return collections.Counter(vals)


# ---------------------------------------------------------------------------
# 1. the drive manifest -- every mirrored file
# ---------------------------------------------------------------------------

def manifest_index():
    """(how common its kind is, its size, its path depth) over 820 files."""
    rs = _rows(SOURCES["drive manifest"])
    kind = _tally(r["mime_type"] for r in rs)
    out, skip = set(), 0
    for r in rs:
        s = _int(r["drive_size_bytes"])
        if s is None:
            skip += 1
            continue
        out.add((kind[r["mime_type"]], s, r["repo_path"].count("/")))
    _SKIPPED["drive manifest"] = skip
    return frozenset(out)


# ---------------------------------------------------------------------------
# 2. the BUILD series
# ---------------------------------------------------------------------------

def _stream(title):
    if "main_and_register" in title:
        return "main"
    if "compendia" in title:
        return "compendia"
    return "figures"


def build_index():
    """(build number, how many builds share its stream, its size)."""
    rs = [r for r in _rows(SOURCES["build series"])
          if re.search(r"BUILD\d+", r["drive_title"] or "")]
    st = _tally(_stream(r["drive_title"]) for r in rs)
    out, skip = set(), 0
    for r in rs:
        n = _int(re.search(r"BUILD(\d+)", r["drive_title"]).group(1))
        s = _int(r["drive_size_bytes"])
        if n is None or s is None:
            skip += 1
            continue
        out.add((n, st[_stream(r["drive_title"])], s))
    _SKIPPED["build series"] = skip
    return frozenset(out)


# ---------------------------------------------------------------------------
# 3. the Register's numbering gaps
# ---------------------------------------------------------------------------

def register_index():
    """(the missing number, how many gaps share its class, the span it sits in).

    The span is next_seated - prev_seated: how wide the hole is in the numbering
    around it, which is a fact about the Register and not about the gap's cause.
    """
    rs = _rows(SOURCES["register gaps"])
    cls = _tally(r["class"] for r in rs)
    out, skip = set(), 0
    for r in rs:
        n, p, q = _int(r["number"]), _int(r["prev_seated"]), _int(r["next_seated"])
        if n is None or p is None or q is None:
            skip += 1
            continue
        out.add((n, cls[r["class"]], q - p))
    _SKIPPED["register gaps"] = skip
    return frozenset(out)


# ---------------------------------------------------------------------------
# 4. the recovered ledger, by conversation
# ---------------------------------------------------------------------------

def recovered_index():
    """(files recovered, distinct statuses, total bytes) per conversation.

    THE MEMBERS ARE CONVERSATIONS, NOT FILES.  3,224 ledger rows over 259
    conversations; charting the rows would make the index a restatement of the
    ledger, where charting the conversations asks what each one yielded.
    """
    rs = _rows(SOURCES["recovered ledger"])
    by = collections.defaultdict(list)
    for r in rs:
        by[r["conversation"]].append(r)
    out, skip = set(), 0
    for v in by.values():
        sz = [_int(x["size_bytes"]) for x in v]
        if any(s is None for s in sz):
            skip += 1
            continue
        out.add((len(v), len({x["status"] for x in v}), sum(sz)))
    _SKIPPED["recovered ledger"] = skip
    return frozenset(out)


def conversations():
    rs = _rows(SOURCES["recovered ledger"])
    return len({r["conversation"] for r in rs})


# ---------------------------------------------------------------------------
# 5. the coverage census
# ---------------------------------------------------------------------------

def coverage_index():
    """(how big its family is, how big its disposition is, is it held)."""
    rs = _rows(SOURCES["coverage census"])
    fam = _tally(r["family"] for r in rs)
    st = _tally(r["status"] for r in rs)
    return frozenset((fam[r["family"]], st[r["status"]],
                      1 if (r["held_as"] or "").strip() else 0) for r in rs)


# ---------------------------------------------------------------------------
# 6. this tree's own dockets
# ---------------------------------------------------------------------------

DOCKET_HEAD = re.compile(r"^## DOCKET (\d+) — (.+)$", re.M)


def _dockets():
    """[(number, state, lines)] read from DOCKET.md's own headings."""
    path = os.path.join(ROOT, SOURCES["dockets"])
    text = open(path, encoding="utf-8").read()
    hits = list(DOCKET_HEAD.finditer(text))
    out = []
    for i, m in enumerate(hits):
        end = hits[i + 1].start() if i + 1 < len(hits) else len(text)
        head = m.group(2)
        state = ("PINNED" if "PINNED" in head else
                 "RULED" if "RULED" in head else
                 "REPAIRED" if "REPAIRED" in head else "OPEN")
        out.append((int(m.group(1)), state,
                    text[m.start():end].count("\n")))
    return out


def docket_index():
    """(docket number, how many dockets share its state, how long it is)."""
    d = _dockets()
    st = _tally(s for _n, s, _l in d)
    return frozenset((n, st[s], ln) for n, s, ln in d)


# ---------------------------------------------------------------------------
# 7. the member index -- the store of record itself
# ---------------------------------------------------------------------------

def member_index():
    """(how many members share its extension, its bytes, its bundle offset).

    THE 343 SEATED MEMBERS OF THE METHOD 1.6.  `method/` is the store of record
    and the first thing `CLAUDE.md` says to read; `sources.py` named the BUILD
    snapshots and the drive mirror and did not name the members themselves.
    The offset is where the member sits inside its bundle, which orders the
    members within a bundle exactly as the bundle does.
    """
    rs = _rows(SOURCES["member index"])
    ext = _tally(r["ext"] for r in rs)
    out, skip = set(), 0
    for r in rs:
        b, o = _int(r["bytes"]), _int(r["bundle_offset"])
        if b is None or o is None:
            skip += 1
            continue
        out.add((ext[r["ext"]], b, o))
    _SKIPPED["member index"] = skip
    return frozenset(out)


# ---------------------------------------------------------------------------
# 8. the extracted ledger, by archive
# ---------------------------------------------------------------------------

def extracted_index():
    """(occurrences, distinct dispositions, total bytes) per source archive.

    THE MEMBERS ARE ARCHIVES, NOT OCCURRENCES.  2,504 rows over the archives and
    project exports the mirror holds; charting the rows restates the ledger,
    charting the archives asks what came out of each.
    """
    rs = _rows(SOURCES["extracted ledger"])
    by = collections.defaultdict(list)
    for r in rs:
        by[r["source"]].append(r)
    out, skip = set(), 0
    for v in by.values():
        sz = [_int(x["size_bytes"]) for x in v]
        if any(x is None for x in sz):
            skip += 1
            continue
        out.add((len(v), len({x["disposition"] for x in v}), sum(sz)))
    _SKIPPED["extracted ledger"] = skip
    return frozenset(out)


def archives():
    return len({r["source"] for r in _rows(SOURCES["extracted ledger"])})


# ---------------------------------------------------------------------------
# 9. the prose-only list, by conversation
# ---------------------------------------------------------------------------

def prose_index():
    """(statements, distinct categories, distinct confidences) per conversation.

    What the chat history holds that the repository does not, charted by where
    it was said rather than by what was said -- the categories are a closed set
    of seven and would make a seven-cell index on their own.
    """
    rs = _rows(SOURCES["prose-only list"])
    by = collections.defaultdict(list)
    for r in rs:
        by[r["conversation"]].append(r)
    return frozenset((len(v), len({x["category"] for x in v}),
                      len({x["confidence"] for x in v})) for v in by.values())


# ---------------------------------------------------------------------------
# 10. the retraction audit
# ---------------------------------------------------------------------------

def retraction_index():
    """(how many rows share its verdict, its confidence tally, its pass tally).

    Is a withdrawn figure still standing.  Every coordinate is a tally, because
    all three columns are categorical and none of them has an order.
    """
    rs = _rows(SOURCES["retraction audit"])
    ver = _tally(r["verdict"] for r in rs)
    con = _tally(r["confidence"] for r in rs)
    pas = _tally(r["pass"] for r in rs)
    return frozenset((ver[r["verdict"]], con[r["confidence"]], pas[r["pass"]])
                     for r in rs)


# ---------------------------------------------------------------------------
# 11. the chat export
# ---------------------------------------------------------------------------

def chat_index():
    """(messages, bytes, how many conversations share its shard) per conversation."""
    rs = _rows(SOURCES["chat export"])
    shard = _tally(r["shard_path"] for r in rs)
    out, skip = set(), 0
    for r in rs:
        m, b = _int(r["message_count"]), _int(r["bytes"])
        if m is None or b is None:
            skip += 1
            continue
        out.add((m, b, shard[r["shard_path"]]))
    _SKIPPED["chat export"] = skip
    return frozenset(out)


# ---------------------------------------------------------------------------
# 12. the handoff gap
# ---------------------------------------------------------------------------

def handoff_index():
    """(how many share its class, its bytes, its lines) per cited handoff."""
    rs = _rows(SOURCES["handoff gap"])
    cls = _tally(r["class"] for r in rs)
    out, skip = set(), 0
    for r in rs:
        b, l = _int(r["bytes"]), _int(r["lines"])
        if b is None or l is None:
            skip += 1
            continue
        out.add((cls[r["class"]], b, l))
    _SKIPPED["handoff gap"] = skip
    return frozenset(out)


# ---------------------------------------------------------------------------
# 13. the pending list
# ---------------------------------------------------------------------------

def pending_index():
    """(how many share its source, its bytes, how many share its reason).

    FOUR ROWS, AND IT IS STILL AN INDEX.  `CLAUDE.md` records that all four are
    pending by decision rather than by obstacle; the index says nothing about
    that and charts only what the table holds.
    """
    rs = _rows(SOURCES["pending list"])
    src = _tally(r["source"] for r in rs)
    rea = _tally(r["reason"] for r in rs)
    out, skip = set(), 0
    for r in rs:
        b = _int(r["drive_size_bytes"])
        if b is None:
            skip += 1
            continue
        out.add((src[r["source"]], b, rea[r["reason"]]))
    _SKIPPED["pending list"] = skip
    return frozenset(out)


# ---------------------------------------------------------------------------

INDEXES = {
    "build series": build_index,
    "drive manifest": manifest_index,
    "register gaps": register_index,
    "recovered ledger": recovered_index,
    "coverage census": coverage_index,
    "dockets": docket_index,
    "member index": member_index,
    "extracted ledger": extracted_index,
    "prose-only list": prose_index,
    "retraction audit": retraction_index,
    "chat export": chat_index,
    "handoff gap": handoff_index,
    "pending list": pending_index,
}
_CELL = {}


def cell(name):
    if name not in _CELL:
        _CELL[name] = mi.cell(INDEXES[name]())
    return _CELL[name]


def closers(name):
    X = INDEXES[name]()
    cl, _b = hlaw.closures(X)
    return sorted(L for L in hlaw.LANGS if len(cl[L]) == len(X))


def shapes():
    """[(name, cells, height, width)] -- cheap; no channel computed."""
    out = []
    for n, f in INDEXES.items():
        X = f()
        out.append((n, len(X), mi.height(X), mi.width(X)))
    return out


def collisions():
    """[(name, categories, distinct tallies)] -- where equal-sized kinds merge.

    The cost of using a category's SIZE in place of a ranking, named rather than
    left to be found.
    """
    out = []
    for nm, col, rel in (("drive manifest", "mime_type", SOURCES["drive manifest"]),
                         ("register gaps", "class", SOURCES["register gaps"])):
        t = _tally(r[col] for r in _rows(rel))
        out.append((nm, len(t), len(set(t.values()))))
    d = _dockets()
    t = _tally(s for _n, s, _l in d)
    out.append(("dockets", len(t), len(set(t.values()))))
    return out


def criterion(name):
    """{coordinate: moves under a monotone redundant append}.  DOCKET 3."""
    X = INDEXES[name]()
    lifted = frozenset(t + (t[0],) for t in X)
    return {"K": 0 if mi.K(X) == mi.K(lifted) else 1,
            "height": 0 if mi.height(X) == mi.height(lifted) else 1,
            "width": 0 if mi.width(X) == mi.width(lifted) else 1}


def against_demand():
    """[(name, cell, verdict)] -- where each of the six lands on the figure."""
    import demand
    import hexad
    F = hexad.figure()
    D = set(demand.demand(F))
    J, _r = demand.closure(F)
    out = []
    for n in INDEXES:
        c = cell(n)
        if c in D:
            v = "DEMANDED -- seating it drops E by one"
        elif c in J:
            v = "already a cell of the closure"
        elif demand.neutral(c, F):
            v = "neutral -- costs nothing, closes nothing"
        else:
            v = "disruptive -- raises E by %d" % (demand.E(F | {c}) - demand.E(F))
        out.append((n, c, v))
    return out


# ---------------------------------------------------------------------------

def report():
    print("=" * 74)
    print("THE SIX FIRST-ORDER INDEXES THE ARTEFACT STORE CARRIES")
    print("=" * 74)
    print()
    print("1. THE SOURCES, ALL READ-ONLY AND ALL CORPUS-GENERATED.")
    for n, rel in SOURCES.items():
        print("   %-18s %s" % (n, rel))
    print()
    print("2. THE SHAPES.")
    print("   %-18s %-8s %-8s %s" % ("index", "cells", "height", "width"))
    for n, c, h, w in shapes():
        print("   %-18s %-8d %-8d %d" % (n, c, h, w))
    if any(_SKIPPED.values()):
        print("   skipped rows: %s"
              % {k: v for k, v in _SKIPPED.items() if v})
    else:
        print("   no row was skipped: every column parsed.")
    print()
    print("3. THE COST OF USING A CATEGORY'S SIZE INSTEAD OF A RANKING.")
    for nm, cats, dist in collisions():
        print("   %-18s %d categories -> %d distinct values%s"
              % (nm, cats, dist, "" if cats == dist else "   SOME MERGE"))
    print("   No RECONSTRUCTED order is carried anywhere in this file.")
    print()
    print("4. THE CHART CRITERION (DOCKET 3) AND THE CHANNELS.")
    print("   (this section measures every channel and takes about an hour;")
    print("    the selftest skips the %d indexes over %d cells and says so)"
          % (len([n for n in INDEXES if len(INDEXES[n]()) > CHANNEL_BUDGET]),
             CHANNEL_BUDGET))
    bad = False
    for n in INDEXES:
        crit = criterion(n)
        bad |= any(crit.values())
        print("   %-18s %-12s closes %s"
              % (n, str(cell(n)), ", ".join(closers(n)) or "nothing"))
    if bad:
        print("   A COORDINATE MOVED. The reading below is void.")
        return 1
    print()
    print("5. WHERE THEY LAND.")
    for n, c, v in against_demand():
        print("   %-18s %-12s %s" % (n, str(c), v))
    print()
    print("6. REFUSED: to treat six as complete. M's point is that the supply")
    print("   keeps growing and this file cannot refute it -- it builds the six")
    print("   that were NAMED, and a seventh source found tomorrow is a seventh")
    print("   index. UNNAMED_SOURCES_MAY_EXIST = True. To read a table the")
    print("   corpus does not generate. To smooth one: a row that will not")
    print("   parse is skipped and counted.")
    return 0


def selftest():
    ok = True

    def chk(lab, got, want):
        nonlocal ok
        good = got == want
        ok &= good
        print("  [%s] %-54s %s" % ("ok" if good else "XX", lab,
                                   got if good else "%s != %s" % (got, want)))

    chk("thirteen sources named", len(SOURCES), 13)
    chk("thirteen indexes built", len(INDEXES), 13)
    chk("every named source has an index", sorted(SOURCES), sorted(INDEXES))
    chk("six of them are the ones sources.py listed",
        len([n for n in SOURCES if n in ("build series", "drive manifest",
                                         "register gaps", "recovered ledger",
                                         "coverage census", "dockets")]), 6)
    chk("and seven were found by looking", len(SOURCES) - 6, 7)
    chk("every source file exists",
        [n for n, r in SOURCES.items()
         if not os.path.exists(os.path.join(ROOT, r))], [])
    chk("the supply is not claimed complete", UNNAMED_SOURCES_MAY_EXIST, True)

    chk("the manifest mirrors 820 files",
        len(_rows(SOURCES["drive manifest"])), 820)
    chk("the coverage census is 1,005 names",
        len(_rows(SOURCES["coverage census"])), 1005)
    chk("the Register has 132 numbered gaps",
        len(_rows(SOURCES["register gaps"])), 132)
    chk("the recovered ledger is 3,224 rows",
        len(_rows(SOURCES["recovered ledger"])), 3224)
    chk("over 259 conversations", conversations(), 259)
    chk("the member index seats 343 members",
        len(_rows(SOURCES["member index"])), 343)
    chk("the extracted ledger is 2,504 occurrences",
        len(_rows(SOURCES["extracted ledger"])), 2504)
    chk("over %d archives" % archives(), archives() > 20, True)
    chk("the prose-only list is 1,168 statements",
        len(_rows(SOURCES["prose-only list"])), 1168)
    chk("the retraction audit is 391 rows",
        len(_rows(SOURCES["retraction audit"])), 391)
    chk("the chat export is 352 conversations",
        len(_rows(SOURCES["chat export"])), 352)
    chk("the handoff gap is 26 rows",
        len(_rows(SOURCES["handoff gap"])), 26)
    chk("the pending list is 4 rows",
        len(_rows(SOURCES["pending list"])), 4)
    d = _dockets()
    chk("the dockets are numbered from 1 with none missing",
        sorted(n for n, _s, _l in d), list(range(1, len(d) + 1)))
    chk("DOCKET 11 is pinned",
        next(s for n, s, _l in d if n == 11), "PINNED")
    chk("DOCKET 3 is ruled", next(s for n, s, _l in d if n == 3), "RULED")

    sh = {n: (c, h, w) for n, c, h, w in shapes()}
    chk("build series cells", sh["build series"][0], 131)
    chk("drive manifest cells", sh["drive manifest"][0], 661)
    chk("register gaps cells", sh["register gaps"][0], 132)
    chk("recovered ledger cells", sh["recovered ledger"][0], 259)
    chk("coverage census cells", sh["coverage census"][0], 18)
    chk("member index cells", sh["member index"][0], 343)
    chk("the member index is FAITHFUL -- one cell per seated member",
        sh["member index"][0], len(_rows(SOURCES["member index"])))
    chk("extracted ledger cells", sh["extracted ledger"][0], 29)
    chk("and it has one cell per archive at most",
        sh["extracted ledger"][0] <= archives(), True)
    chk("prose-only cells", sh["prose-only list"][0], 29)
    chk("retraction audit cells", sh["retraction audit"][0], 16)
    chk("chat export cells", sh["chat export"][0], 326)
    chk("handoff gap cells", sh["handoff gap"][0], 24)
    chk("pending list cells", sh["pending list"][0], 3)
    # THE DOCKET INDEX IS SELF-REFERENTIAL AND ITS COUNT IS NOT PINNED.
    # Opening a docket changes it -- including a docket about this index -- so
    # what is pinned is the PROPERTY (one cell per docket) and a floor on the
    # count, not a number that a later ruling would falsify.
    chk("the dockets index is faithful -- one cell per docket",
        sh["dockets"][0], len(_dockets()))
    chk("and there are at least fifteen dockets", len(_dockets()) >= 15, True)
    chk("no row was skipped", {k: v for k, v in _SKIPPED.items() if v}, {})
    for n, (c, h, w) in sh.items():
        chk("%s: height and width bound the size" % n,
            max(h, w) <= c <= h * w, True)

    # ---- THE CHANNEL-DEPENDENT FIXTURES, AND WHY THEY ARE BEHIND A FLAG.
    # Measuring a channel runs five closure operators over every pair of
    # coordinates, and DOCKET 3's criterion asks for it TWICE per index (the
    # index and its lifted copy).  On the drive manifest's 661 cells that is
    # minutes apiece, and the whole sweep timed out at fifty.  A selftest
    # nobody can finish is a selftest nobody runs.
    #
    # SO THEY ARE SKIPPED BY DEFAULT AND THE SKIP IS COUNTED AND PRINTED.
    # PROOF-ASSISTANT.md records the failure mode this avoids: guard_encoding
    # reported "no drift" while silently discarding 67 of 400 trials, and the
    # counterexamples lived in exactly what it discarded.  Nothing here is
    # skipped silently, and `--slow` runs every one.
    slow = "--slow" in sys.argv
    cheap = [n for n in INDEXES if len(INDEXES[n]()) <= CHANNEL_BUDGET]
    dear = [n for n in INDEXES if n not in cheap]
    for n in (sorted(INDEXES) if slow else sorted(cheap)):
        crit = criterion(n)
        chk("%s: K admissible" % n, crit["K"], 0)
        chk("%s: height admissible" % n, crit["height"], 0)
        chk("%s: width admissible" % n, crit["width"], 0)
        chk("%s: the cell is a 3-tuple" % n, len(cell(n)), 3)
    if not slow:
        print("  [--] SKIPPED the channel fixtures for %d of %d indexes, over"
              % (len(dear), len(INDEXES)))
        print("       %d cells each: %s" % (CHANNEL_BUDGET, ", ".join(sorted(dear))))
        print("       Run `python3 store.py --selftest --slow` for those.")
    chk("the skip is accounted for", len(cheap) + len(dear), len(INDEXES))
    chk("and it is not hiding most of the tree", len(cheap) > len(dear), True)

    chk("all thirteen verdicts reported", len(against_demand()), 13)
    print("store selftest: %s" % ("PASS" if ok else "FAIL"))
    return ok


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    sys.exit(report())
