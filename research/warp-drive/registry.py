#!/usr/bin/env python3
r"""
registry.py -- EVERY INDEX OF THE PERIODIC ELEMENTS, WITH THE CRITERION
ENFORCED RATHER THAN DESCRIBED.

M: "Remove any index in the project whose members do not have quantum numbers."

    python3 registry.py             the reading
    python3 registry.py --selftest  fixtures

===============================================================================
0. THE CRITERION IS A FUNCTION HERE, AND THAT IS THE WHOLE REPAIR
===============================================================================

THE SUBJECT IS THE PERIODIC ELEMENTS.  A member of an index of it is an
electron, a subshell, a transition, a channel or a series -- something carrying
quantum numbers.

    NOTHING ENFORCED THAT, AND THE FIGURE WAS CONTAMINATED.  Thirteen
    filing-system indexes were seated as vertices -- mirrored files, BUILD
    snapshots, conversations, archives, artefact names, handoff documents,
    numbering gaps, and this tree's own dockets -- beside indexes whose members
    are electrons.  E went from 9 to 133, and EVERY ONE of the twelve
    disruptive vertices was repository metadata.  Not one was an element.

    THE EXPLOSION WAS THE CONTAMINATION, NOT A FINDING, and it was reported as
    one.  Withdrawn here.  The element-only figure is NINE vertices at E = 15
    on the measurement that prompted this rewrite, and SEVEN once the two
    indexes whose members are axes rather than elements come out.

    SO `QUANTUM` IS A COLUMN AND `enforce()` IS A FIXTURE.  Every registered
    index names the quantum numbers its members carry; a row that names none is
    refused.  A criterion in a docstring is what let the filing cabinet in.

===============================================================================
0b. DOCKET 27 -- THE SUBJECT WIDENS, THE CRITERION DOES NOT
===============================================================================

M: "This is a valid exception to the registry criteria.  These are legitimate
particles and can and must be accepted."  And, setting the task: "we are
essentially filling in the rest of the space in the master index."

    THE CRITERION IS UNTOUCHED.  A member must still carry quantum numbers,
    `QUANTUM` is still a column, and `enforce()` still refuses a row that names
    none.  That guard caught a real contamination once and it is not relaxed.

    WHAT WIDENS IS THE SUBJECT.  It was the periodic elements, because that is
    what the project had.  It is now QUANTUM OBJECTS: a muon carries spin and
    charge and lepton number, and the only thing keeping it out was a noun in a
    docstring.  Every one of the rows seated before this ruling still passes --
    an electron, a subshell, a transition, a term and a nuclide-charge state
    are all quantum objects -- so the widening ADDS and retracts nothing.

    THE BOUNDARY THAT REMAINS.  Composite nuclei stay out of the particle
    capture, because they ARE the periodic elements and `gravity` already seats
    3,394 nuclide-charge states.  `nucshell` was already the exception that
    proved the old subject too narrow: its members are nuclear, not atomic, and
    it was seated with a note saying so.

===============================================================================
1. WHAT IS AN INDEX HERE, AND WHAT IS NOT
===============================================================================

    fibred        170 electrons          n, l, k
    madelung      the same 170           n+l, l, k
    ions          98 transitions         charge, electron count
    channels      209 channel shapes     l, Pauli bound, multiplicity
    laws          584 series             n range, l, quantum defect
    probability   25 subshells           n, l
    inversion     20 inversions          pairs of (n, l)
    gravity       3,394 nuclide-charge   Z, N, A, q, Ne, 2J, level status
                  states, read in 8
                  spacetime dimensions
    nucshell      22 NUCLEAR subshells   nr, l, j -- the only non-atomic
                                         member type seated here
    madrule       20 elements the        n+l acceptor, l donor, occupancy
                  Madelung rule misses
    terms         5,132 LS terms over    2S+1, L, parity, the banked J set
                  122 spectra

REMOVED, files deleted, all created in the session that made the mess:
`store.py` and its thirteen filing-system indexes; `obstruction.py` with its
currency and exotic-matter sub-indexes, whose members are obstructions to
building a warp drive; `filled.py`, a re-chart of the seated indexes;
`cross.py`, whose members are PAIRS OF AXES; and `density.py` and `occupy.py`,
both built on the contaminated figure.

PRESENT AS FUNCTIONS, NOT INDEXES OF THIS PROJECT: `mi.index`, `axes.index`,
`entropy.index`, `rindex.rindex`, `necindex.index`.  Their members are seated
indexes, measurement axes, refusals and energy conditions.  The files are NOT
deleted -- they carry charting machinery and findings this session did not
produce -- and `NOT_AN_INDEX` names each with its reason so nothing re-seats
them.

===============================================================================
2. WHAT THIS FILE REFUSES
===============================================================================

To claim completeness.  `COMPLETE = False`, and it stays false.

To accept a row that cannot name its quantum numbers.

To excuse a module silently.  A module exposing an `index()` that is neither
registered nor listed in `NOT_AN_INDEX` fails the selftest.
"""

import hashlib
import importlib
import os
import sys

COMPLETE = False
HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))

METHODS = ("TABLE", "FIBRATION", "RESIDUAL")

# (module, accessor, method, what one member is, THE QUANTUM NUMBERS)
REGISTERED = (
    ("fibred", "index", "FIBRATION", "170 electrons, MADELUNG-PREDICTED",
     "n, l, k"),
    ("madelung", "janet", "FIBRATION",
     "the same 170 electrons, MADELUNG-PREDICTED", "n+l, l, k"),
    ("ions", "index", "TABLE", "98 Lambda-8 transitions",
     "charge, electron count"),
    ("channels", "index", "TABLE", "209 spectroscopic channel shapes",
     "l, Pauli bound, multiplicity"),
    ("laws", "index", "RESIDUAL", "584 series against Rydberg-Ritz",
     "n range, l, quantum defect"),
    ("probability", "index", "TABLE", "25 subshells", "n, l"),
    ("inversion", "index", "TABLE", "20 fill-order/shell-order inversions",
     "pairs of (n, l)"),
    ("gravity", "index", "TABLE",
     "3,394 nuclide-charge states x 8 dimensions",
     "Z, N, A, q, Ne, 2J, level status"),
    ("nucshell", "index", "TABLE", "22 nuclear single-particle subshells",
     "nr, l, j (nuclear)"),
    ("madrule", "index", "RESIDUAL", "20 Madelung exceptions, by their transfer",
     "n+l of the acceptor, l of the donor, occupancy"),
    ("terms", "index", "TABLE", "5,132 Russell-Saunders terms over 122 spectra",
     "2S+1, L, parity, the banked J set"),
    # ---- SEATED BY THE OVERLAP RULING.  M: "They can be seated with overlaps
    # so long as it is not an overlap of same information ... its relative
    # position in this index is information about an object."  Each of the
    # three is a coarsening of a row above, over the SAME members, reaching a
    # channel no row above reaches.  `overlaprule.py` states the ruling, the
    # three grounds it is tested on, the three candidates it REFUSES, and the
    # two parts of the definition each seating carries.  They are seated in
    # that file rather than in their parents so that the rows a ruling put here
    # are visible as such.
    # DOCKET 26.  M: "both".  `fibred` and `madelung` chart the configuration
    # MADELUNG PREDICTS; this charts the one register 1306 BANKS AS OBSERVED.
    # 25 of 108 addresses differ, 20 of 108 configurations do -- and those 20
    # are exactly `madrule`'s exceptions.  Neither supersedes the other; the
    # places they part are the finding neither holds alone.  See observed.py.
    ("observed", "index", "FIBRATION",
     "108 observed differentiating electrons, register 1306",
     "n, l, k (observed)"),
    ("overlaprule", "gravity_bound", "TABLE",
     "the same 3,394 nuclide-charge states, on the bound structure alone",
     "horizon-bound class, forced angular momentum, spin-decade rank"),
    # UNSEATED BY DOCKET 22.  ("overlaprule", "nucshell_lsigma", ...) sat here.
    # The same 22 members under (l, 2j) -- an IDENTICAL partition, and 2j is
    # what order_a() actually banks -- land at K7, which is occupied, so the
    # chart has no novel channel and was never a candidate.  The K5 was a fact
    # about writing the second coordinate as sigma.  overlaprule.py section 3e.
    ("overlaprule", "madelung_slot", "FIBRATION",
     "the same 170 electrons, subshell-blind",
     "n+l, k"),
    # ---- DOCKET 27.  M: "Can you now please produce indexes and plates for
    # all particles other than periodic atoms ... whatever particle there is
    # that isn't already indexed."  Section 0b rules the subject widened and
    # the criterion untouched.  Three NEW MEMBER SETS, not coarsenings of any
    # row above, so the overlap ruling's four grounds do not apply -- each is
    # a first index of objects this tree had never charted.  Antiparticles are
    # separate members in all three.  Composite nuclei stay out: they ARE the
    # periodic elements and `gravity` already seats them.
    ("fundamental", "index", "TABLE",
     "30 Standard Model particles -- 12 quarks, 12 leptons, 6 gauge/Higgs",
     "2J, Q3, colour dimension, generation"),
    ("mesons", "index", "TABLE",
     "242 mesons of the PDG table, 8 set aside for want of a printed parity",
     "2J, P, 2I, Q3"),
    ("baryons", "index", "TABLE",
     "278 baryons of the PDG table, 14 set aside for want of a printed parity",
     "2J, P, 2I, Q3, strangeness, charm, beauty"),
    # ---- DOCKET 29.  THE TREE'S ONLY K5.  DOCKET 25 closed with "a new
    # member set would reopen it", and DOCKET 27 seated three.  The reopened
    # census -- `particlesweep.py`, 142 sub-charts -- found one seating and two
    # refusals.  Seated in overlaprule.py because it is a coarsening of a row
    # above and the ruling's four grounds are what admitted it.
    ("overlaprule", "baryon_isomultiplet", "TABLE",
     "the same 278 baryons, isospin against charge with flavour dropped",
     "2I, Q3"),
    # ---- DOCKET 30.  M: "And they need to be seated.  Why were the indexes
    # not seated?"  DOCKET 28 refused an anyon chart on box invariance and the
    # refusal was sound FOR THE CHART IT RAN ON -- which charted SU(2)_k for
    # every k, a UNION OVER THEORIES rather than a reach over data.  fqh.py
    # charts a reach instead: the quasiparticles of the Laughlin states,
    # indexed by a MEASURED filling fraction.  The channel MOVES with the box
    # (K2 then K0), so boxinvariance.verdict_of() returns SEAT.  DOCKET 28's
    # chart stays refused; this is a different object, not an overrule.
    ("fqh", "index", "TABLE",
     "168 quasiparticles of twelve Laughlin states, three of them observed",
     "statistics class, order of the exchange phase, order of the charge, "
     "inverse filling fraction"),
    # ---- DOCKET 31.  M: "almost nothing -- but not nothing, which means
    # measurable ... it is a sub index/sublattice of bosons."  DOCKET 28 read
    # "almost nothing" as nothing; low resolution is not no resolution, and
    # overlap.py's LABEL threshold is the test these coordinates pass.  The
    # ruling also NAMES the object, which DOCKET 28 never found: not an index
    # of quasiparticles floating free but a SUBLATTICE of the bosons.  The
    # first draft LISTED eleven kinds with their spins and charges written out
    # from textbook knowledge.  M then ruled: "Do not add declared.  Nothing
    # less than computed or measured."  Rewritten -- a member is now defined by
    # WHAT IT IS MADE OF and every number is computed from the seated
    # electron by charge addition and angular-momentum addition.  The
    # collective modes left with it, because they are not composites.
    ("bosonqp", "index", "TABLE",
     "15 bosonic excitations -- composites, Goldstone modes and hybrids, "
     "every number derived",
     "2J, Q3"),
    # ---- DOCKET 32.  M: "the non-abelian Hall states are a further member
    # set and are not in this index -- we do this next."  The other kind of
    # Hall quasiparticle: exchange rotates the state inside a degenerate space
    # rather than multiplying it by a phase.  Moore-Read IS RR_2.  Same
    # coordinate frame as `fqh` on purpose, so the two can be compared -- and
    # neither turns out to nest in the other.
    ("readrezayi", "index", "TABLE",
     "363 parafermion primaries of eleven Read-Rezayi states, two observed",
     "statistics class, order of the twist, order of the charge, level"),
    # ---- DOCKET 34.  M: "still indexable.  Just contains no mass.  But a
    # legitimate index.  Build it and seat it."  DOCKET 33 found this chart and
    # refused it on a MASS reach -- but mass is not total over these members
    # and mesons.py already refuses it as a coordinate, so that was the wrong
    # reach.  On PDG STATUS, which every row carries, the channel MOVES (K5 to
    # K4) and boxinvariance seats it.  THE FIRST ARITY-3 K4 IN THE TREE: every
    # earlier one was arity 2, where statistics closes free.  This fills the
    # last empty channel.
    ("spin4", "index", "TABLE",
     "10 spin-4 mesons, two of them without a printed mass",
     "P, 2I, Q3"),
)

NOT_AN_INDEX = {
    "mi": "members are the seated indexes -- and NINE OF THEM ARE NOT "
          "REGISTERED ONES; figure.superseded_mi() measures it",
    "figure": "the index of first-order indexes: its members ARE the seated "
              "indexes, so they carry no quantum numbers",
    "axes": "members are measurement axes",
    "entropy": "members are the seated indexes",
    "rindex": "members are refusals",
    "necindex": "members are energy conditions",
    # DOCKET 28.  This one DOES chart quantum objects -- anyons carry
    # topological charge, spin and quantum dimension -- and it is still not
    # seated, for a reason that has nothing to do with the criterion:
    # boxinvariance.verdict_of() returns REFUSE-AS-THEOREM, because the
    # channel is K2 at every box from k <= 4 to k <= 24.  It is here so the
    # completeness guard accounts for it rather than being silenced.
    "quasiparticle": "members ARE quantum objects and the criterion passes -- "
                     "the chart is refused by BOX INVARIANCE instead, the "
                     "channel being K2 at every box, so it is a theorem about "
                     "the SU(2)_k construction and not an index of anyons",
}


def _mod(name):
    return importlib.import_module(name)


def enforce():
    """[(name, problem)] for any registered row that fails the criterion.

    MUST BE EMPTY.  This is the criterion as a function; it was a paragraph
    before, and a paragraph is what let thirteen filing-system indexes in.
    """
    bad = []
    for mod, acc, meth, _what, q in REGISTERED:
        nm = "%s.%s" % (mod, acc)
        if not q or not q.strip():
            bad.append((nm, "names no quantum numbers"))
        if meth not in METHODS:
            bad.append((nm, "unknown method %s" % meth))
    return bad


def rows():
    """[(name, module, accessor, method, members, quantum numbers)]."""
    return [("%s.%s" % (m, a), m, a, me, w, q)
            for m, a, me, w, q in REGISTERED]


def short(name=None):
    """{full name: a unique short label}, or one label if `name` is given.

    THE MODULE NAME WAS THE LABEL AND THAT STOPPED BEING UNIQUE.  Every row
    here was one module until the overlap ruling seated three coarsenings in
    `overlaprule.py`; `figure.py` keyed its vertices on `name.split(".")[0]`
    and silently folded three vertices into one -- twelve where there are
    fourteen.  The selftest caught it because the figure's vertex count is a
    PROPERTY there and not a pinned number, which is the whole reason that
    conversion was made.

    So the label is the module where the module seats one row, and the
    ACCESSOR where it seats more.  `short_is_unique()` is a fixture, not a
    hope.
    """
    n = {}
    for _nm, m, _a, _me, _w, _q in rows():
        n[m] = n.get(m, 0) + 1
    out = {nm: (m if n[m] == 1 else a) for nm, m, a, _me, _w, _q in rows()}
    return out if name is None else out[name]


def short_is_unique():
    """[] unless two rows want the same label."""
    lab = short()
    seen, bad = {}, []
    for nm, l in sorted(lab.items()):
        if l in seen:
            bad.append((l, seen[l], nm))
        seen[l] = nm
    return bad


def sources():
    """{row name: {"why": ..., "paths": [{"path", "exists", "bytes", "md5"}]}}.

    THE PROVENANCE IS A CHECKED FACT, NOT A SENTENCE.  Each index module
    declares `SOURCE = (why, paths)` beside the code that reads the data, and
    this function resolves every path against the repository root, records
    whether it is there, and hashes it.  `state.py` writes the result into
    STATE.json, so anyone downstream gets the source and its digest from the
    tree rather than from a chat message -- which is the whole point: a
    provenance held only in prose has to be recovered later.

    A module whose data is COMPUTED rather than read declares an empty path
    tuple and says so in `why`.  That is a source too, and an empty tuple is
    not a missing declaration -- `undeclared()` reports those separately.
    """
    out = {}
    for nm, mod, _a, _me, _w, _q in rows():
        S = getattr(_mod(mod), "SOURCE", None)
        if S is None:
            out[nm] = {"why": None, "paths": []}
            continue
        why, paths = S
        ps = []
        for rel in paths:
            ps.append(_digest(rel))
        out[nm] = {"why": why, "paths": ps}
    return out


def _digest(rel):
    """{path, kind, exists, bytes, md5, files} for one declared source path.

    A DIRECTORY IS A SOURCE TOO and is hashed as one: `terms` and `gravity`
    read `recovered/` as a directory rather than naming each table, so the
    digest is taken over the sorted (name, md5) list of the files in it.  A
    file added or changed there moves the digest, which is the property that
    makes this worth writing down.
    """
    full = os.path.join(REPO, rel)
    if os.path.isfile(full):
        b = open(full, "rb").read()
        return {"path": rel, "kind": "file", "exists": True, "bytes": len(b),
                "files": 1, "md5": hashlib.md5(b).hexdigest()}
    if os.path.isdir(full):
        h = hashlib.md5()
        n = tot = 0
        for fn in sorted(os.listdir(full)):
            fp = os.path.join(full, fn)
            if not os.path.isfile(fp):
                continue
            b = open(fp, "rb").read()
            h.update(fn.encode("utf-8"))
            h.update(hashlib.md5(b).digest())
            n += 1
            tot += len(b)
        return {"path": rel, "kind": "dir", "exists": True, "bytes": tot,
                "files": n, "md5": h.hexdigest()}
    return {"path": rel, "kind": None, "exists": False}


def undeclared():
    """[row name] with no SOURCE at all.  MUST BE EMPTY."""
    return sorted(nm for nm, v in sources().items() if v["why"] is None)


def missing_source_files():
    """[(row, path)] a SOURCE names that is not on disk.  MUST BE EMPTY."""
    return sorted((nm, d["path"]) for nm, v in sources().items()
                  for d in v["paths"] if not d["exists"])


def index_of(name):
    for nm, mod, acc, _me, _w, _q in rows():
        if nm == name:
            return getattr(_mod(mod), acc)()
    raise KeyError(name)


def by_method():
    out = {}
    for nm, _mo, _a, me, _w, _q in rows():
        out.setdefault(me, []).append(nm)
    return {k: sorted(v) for k, v in sorted(out.items())}


def modules_with_index():
    """Every module here exposing an index()-like accessor, by module name."""
    out = []
    for f in sorted(os.listdir(HERE)):
        if not f.endswith(".py") or f == os.path.basename(__file__):
            continue
        src = open(os.path.join(HERE, f), encoding="utf-8").read()
        if "\ndef index(" in src or "\ndef rindex(" in src:
            out.append(f[:-3])
    return out


def missing():
    """Modules exposing an index that are neither registered nor excused."""
    named = {m for _n, m, _a, _me, _w, _q in rows()}
    return [m for m in modules_with_index()
            if m not in named and m not in NOT_AN_INDEX]


def sizes():
    out = {}
    for nm, _mo, _a, _me, _w, _q in rows():
        try:
            out[nm] = len(index_of(nm))
        except Exception as exc:                   # pragma: no cover
            out[nm] = "ERROR %s" % exc
    return out


def cells(slow=False, budget=None):
    """{name: cell or 'UNMEASURED'}.  An unmeasured cell is never guessed."""
    import mi
    out = {}
    for nm, _mo, _a, _me, _w, _q in rows():
        X = index_of(nm)
        if not slow and budget is not None and len(X) > budget:
            out[nm] = "UNMEASURED"
            continue
        out[nm] = mi.cell(X)
    return out


def figure(slow=False, budget=None):
    """The element figure: the cell of every registered index."""
    return frozenset(c for c in cells(slow, budget).values()
                     if c != "UNMEASURED")


# ---------------------------------------------------------------------------

def report():
    print("=" * 74)
    print("EVERY INDEX OF THE PERIODIC ELEMENTS")
    print("=" * 74)
    print()
    bad = enforce()
    print("1. THE CRITERION, ENFORCED.")
    print("   registered indexes      %d" % len(REGISTERED))
    print("   rows failing it         %d   %s" % (len(bad), bad if bad else ""))
    if bad:
        print("   THE CRITERION FAILS. Everything below is void.")
        return 1
    print()
    print("2. THE INDEXES, AND WHAT THEIR MEMBERS ARE QUANTISED ON.")
    sz = sizes()
    print("   %-16s %-8s %-30s %s" % ("index", "cells", "members", "quantum"))
    for nm, _mo, _a, _me, w, q in rows():
        print("   %-16s %-8s %-30s %s" % (short(nm), sz.get(nm), w[:30], q))
    print()
    print("3. NOT INDEXES OF THIS PROJECT.")
    for m, why in sorted(NOT_AN_INDEX.items()):
        print("   %-12s %s" % (m, why))
    print()
    miss = missing()
    print("4. UNACCOUNTED MODULES: %d   %s" % (len(miss), ", ".join(miss) or "none"))
    if miss:
        print("   A module exposing an index must be registered with its")
        print("   quantum numbers or named in NOT_AN_INDEX. This fails the")
        print("   selftest.")
    print()
    print("5. COMPLETE = %s." % COMPLETE)
    return 0


def selftest():
    ok = True

    def chk(lab, got, want):
        nonlocal ok
        good = got == want
        ok &= good
        print("  [%s] %-54s %s" % ("ok" if good else "XX", lab,
                                   got if good else "%s != %s" % (got, want)))

    chk("THE CRITERION HOLDS ON EVERY REGISTERED ROW", enforce(), [])
    # PROVENANCE.  Asked for by the session building on this work: "it writes
    # the file with the statuses and sources in it, rather than in its chat.
    # Everything held only in prose has to be recovered later."
    chk("EVERY ROW DECLARES WHERE ITS DATA COMES FROM", undeclared(), [])
    chk("and every path a SOURCE names is on disk", missing_source_files(), [])
    chk("the three DOCKET 27 rows all cite the same PDG capture",
        sorted({tuple(d["path"] for d in sources()["%s.index" % m]["paths"])
                for m in ("fundamental", "mesons", "baryons")}),
        [("research/warp-drive/captures/PDG-2026.tsv",)])
    # M: "Do not add declared.  Nothing less than computed or measured.
    # Declared still requires proof."  A source with no file must be one of
    # these three, and DECLARED -- a human writing values out of knowledge --
    # is NOT among them.  It was briefly a fourth category to accommodate
    # bosonqp's first draft; that draft was rewritten to compute its numbers
    # instead, and the category is gone.
    NOFILE = ("COMPUTED", "INLINE", "Inherited", "recovered/")
    chk("an index with no file declares which kind of source it has instead",
        [nm for nm, v in sources().items()
         if not v["paths"] and not any(k in v["why"] for k in NOFILE)], [])
    chk("NO ROW IS DECLARED -- nothing less than computed or measured",
        sorted(nm for nm, v in sources().items() if "DECLARED" in v["why"]),
        [])
    chk("seventeen indexes registered -- eleven, two the overlap ruling seated "
        "after DOCKET 22 unseated a third, one DOCKET 26 added, and DOCKET "
        "27's three particle indexes, DOCKET 29's K5 and DOCKET 30's "
        "quasiparticles, DOCKET 31's boson sublattice and DOCKET 32's "
        "non-abelian states and DOCKET 34's K4", len(REGISTERED), 22)
    chk("DOCKET 27 seated three, and none of them is a coarsening of a row "
        "above -- each is a new member set",
        sorted(m for m, _a, _me, _w, _q in REGISTERED
               if m in ("fundamental", "mesons", "baryons")),
        ["baryons", "fundamental", "mesons"])
    chk("exactly three came from the ruling, and they agree with it",
        sorted((m, a) for m, a, _me, _w, _q in REGISTERED
               if m == "overlaprule"),
        [("overlaprule", "baryon_isomultiplet"),
         ("overlaprule", "gravity_bound"), ("overlaprule", "madelung_slot")])
    chk("every one names its quantum numbers",
        [n for n, *_r in rows() if not _r[4].strip()], [])
    chk("every method is known",
        sorted({m for _n, _mo, _a, m, _w, _q in rows()} - set(METHODS)), [])
    chk("names are unique", len({n for n, *_r in rows()}), len(rows()))
    chk("SHORT labels are unique too -- three rows share one module now",
        short_is_unique(), [])
    chk("and the three that do are labelled by their accessor",
        sorted(short(nm) for nm, m, *_r in rows() if m == "overlaprule"),
        ["baryon_isomultiplet", "gravity_bound", "madelung_slot"])
    chk("NO module exposing an index is unaccounted for", missing(), [])
    chk("seven modules are excused, with reasons", len(NOT_AN_INDEX), 7)
    chk("and SIX of the seven are excused by the criterion -- quasiparticle "
        "is the one excused by BOX INVARIANCE instead",
        sorted(k for k, v in NOT_AN_INDEX.items() if "criterion passes" in v),
        ["quasiparticle"])
    chk("every excuse is non-empty",
        [k for k, v in NOT_AN_INDEX.items() if not v.strip()], [])
    chk("mi is excused, not registered",
        "mi" in NOT_AN_INDEX and "mi" not in {m for _n, m, *_r in rows()}, True)
    chk("cross is gone", os.path.exists(os.path.join(HERE, "cross.py")), False)
    chk("store is gone", os.path.exists(os.path.join(HERE, "store.py")), False)
    chk("obstruction is gone",
        os.path.exists(os.path.join(HERE, "obstruction.py")), False)
    chk("filled is gone", os.path.exists(os.path.join(HERE, "filled.py")), False)
    chk("density is gone", os.path.exists(os.path.join(HERE, "density.py")), False)
    chk("occupy is gone", os.path.exists(os.path.join(HERE, "occupy.py")), False)
    sz = sizes()
    chk("no index errored", [n for n, v in sz.items() if isinstance(v, str)], [])
    chk("fibred seats 170 electrons", sz["fibred.index"], 170)
    chk("madelung seats the same 170", sz["madelung.janet"], 170)
    chk("ions seats 98 transitions", sz["ions.index"], 98)
    chk("channels seats 209 shapes", sz["channels.index"], 209)
    chk("probability seats 25 subshells", sz["probability.index"], 25)
    chk("inversion seats 17 distinct cells", sz["inversion.index"], 17)
    chk("gravity seats 914 distinct cells", sz["gravity.index"], 914)
    chk("nucshell seats 22 nuclear subshells", sz["nucshell.index"], 22)
    chk("madrule seats 13 distinct cells", sz["madrule.index"], 13)
    chk("terms seats 112 distinct cells", sz["terms.index"], 112)
    chk("DOCKET 26's observed fibration seats 98 distinct cells",
        sz["observed.index"], 98)
    chk("the ruling's gravity coarsening seats 26",
        sz["overlaprule.gravity_bound"], 26)
    chk("the ruling's madelung coarsening seats 82",
        sz["overlaprule.madelung_slot"], 82)
    chk("completeness is not claimed", COMPLETE, False)
    print("registry selftest: %s" % ("PASS" if ok else "FAIL"))
    return ok


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    sys.exit(report())
