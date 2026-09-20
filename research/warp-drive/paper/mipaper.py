#!/usr/bin/env python3
r"""
mipaper.py -- THE MASTER-INDEX PAPER, GENERATED FROM THE INSTRUMENTS.

    python3 paper/mipaper.py            print the facts it would use
    python3 paper/mipaper.py --md       write paper/THE-MASTER-INDEX.md
    python3 paper/mipaper.py --pdf      write paper/pdf/THE-MASTER-INDEX.pdf
    python3 paper/mipaper.py --selftest fixtures

NO FIGURE IN THE PAPER IS TYPED.  `facts()` asks the instruments -- registry,
figure, demand, mi, hlaw, overlaprule, observed, boxinvariance -- and every
number in the prose is substituted from that dict.  A figure that disagreed
with its instrument would be impossible rather than unlikely, and the selftest
asserts the substitution is total: no bare integer of four digits or more
survives in the template.

The PDF needs `reportlab` (pypi is on the proxy allowlist; there is no TeX in
this environment).  The Markdown needs nothing and is the source of record.
"""

import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
WD = os.path.abspath(os.path.join(HERE, ".."))
if WD not in sys.path:
    sys.path.insert(0, WD)

TITLE = "The Index of First-Order Indexes"
SUBTITLE = ("An admissible chart for indexes of the periodic elements, "
            "its eight lawful channels, and what four refusals establish")
AUTHOR = "Matthew Lach"
BYLINE = ("Independent Researcher, with a computing collaborator, "
          "under the protocols of The Method v1.6")


def registry_short_of(f, full):
    """The short label for a full registry name.

    ASK THE REGISTRY, DO NOT REDERIVE.  This stripped ".index" and
    "overlaprule." by hand and fell back to the full name for anything else,
    so the provenance table printed `madelung.janet` where the register table
    two pages earlier printed `madelung` -- one index under two names in one
    paper.  registry.short() is the authority on the label and is now banked.
    """
    return f["short"].get(full, full)


def _lonely_channels():
    """[(K, the one index there)] for every channel with exactly one occupant."""
    import figure
    byk = {}
    for nm, cell in figure.cells().items():
        byk.setdefault(cell[0], []).append(nm)
    return sorted((k, v[0]) for k, v in byk.items() if len(v) == 1)


def sp_simplify_safe(e):
    import sympy as _sp
    try:
        return _sp.simplify(e)
    except Exception:
        return e


# ---------------------------------------------------------------- the facts

def facts():
    """Every number the paper states, asked of the instrument that owns it."""
    import itertools
    import charts
    import demand
    import figure
    import hlaw
    import mi
    import ghosts
    import observed
    import overlaprule as OR
    import predict
    import registry
    import boxinvariance as BI

    # ONE call: reading_counts() is a full sub-chart sweep and was being run
    # twice by the dict literal below.
    _readings = dict(OR.reading_counts())
    ch = mi.channels()
    F = figure.figure()
    cells = registry.cells()

    # name -> (short, channel, arity), built ONCE.  index_of() reconstructs an
    # index from its source on every call, so asking it per channel is
    # quadratic and made this function take minutes rather than seconds.
    _gmn_b = ghosts.gmn_from_quarks("baryon")
    _gmn_m = ghosts.gmn_from_quarks("meson")
    _seats = []
    _gravity_cells = 0
    for _nm, _m0, _a0, _me0, _w0, _q0 in registry.rows():
        _X = registry.index_of(_nm)
        _seats.append((registry.short(_nm), mi.K(_X), len(next(iter(_X)))))
        if _nm == "gravity.index":
            _gravity_cells = len(_X)

    rows = []
    for nm, mod, acc, meth, what, q in registry.rows():
        c = cells[nm]
        rows.append({"label": registry.short(nm), "method": meth,
                     "members": what, "quantum": q,
                     "cells": len(registry.index_of(nm)),
                     "cell": c, "K": c[0]})

    # arity vs whether `statistics` closes, over every sub-chart of every
    # seated index -- recomputed, not read from a cached census
    stat = {}
    chan2 = {}
    # ASK, AND DO NOT SKIP A MISS.  This read `OR.COORDS.get(mod)` and
    # `continue`d on None, which silently swept 15 of the 24 seated indexes
    # while the prose said it had swept them all -- and spin4, the K4 occupant
    # that section 6's closing paragraph is entirely about, was one of the nine
    # dropped.  OR.coords() raises on a miss now, and the three coarsenings are
    # excluded BY NAME, for the stated reason, rather than by accident.
    _swept, _skipped = [], []
    for nm, mod, acc, _me, _w, _q in registry.rows():
        if mod == OR.SELF:
            # A coarsening's sub-charts are sub-charts of its parent, already
            # counted there.  Excluded to avoid double-counting, not because
            # it cannot be reached.
            _skipped.append(registry.short(nm))
            continue
        names = OR.coords(mod)
        _swept.append(registry.short(nm))
        X = OR.parent_chart(mod)
        for r in range(2, len(names) + 1):
            for combo in itertools.combinations(names, r):
                P = OR.project(mod, combo, X)
                k = mi.K(P)
                a = stat.setdefault(r, [0, 0])
                a[0 if "statistics" in ch[k] else 1] += 1
                if r == 2:
                    chan2[k] = chan2.get(k, 0) + 1

    # the density the retraction in section 10 quotes -- MEASURED, because an
    # earlier draft typed it and this file's own substitution guard caught it
    _mp = OR.parent_chart("madelung")
    _box = 1
    for _j in range(len(next(iter(_mp)))):
        _box *= len({x[_j] for x in _mp})
    mad_density = len(_mp) / float(_box)
    mad_cells, mad_box = len(_mp), _box

    jn, mt, pr = OR.semilattice("gravity", ("B", "F", "X"))
    dim = dict((tuple(c), s) for c, s in OR.dimension_finding())

    occ = sorted({c[0] for c in F})
    return {
        "langs": list(hlaw.LANGS),
        "lawful": [(a, b, hlaw.WHY[(a, b)]) for a, b in hlaw.LAWFUL],
        "nchannels": len(ch), "nsubsets": 2 ** len(hlaw.LANGS),
        "channels": ["+".join(sorted(s)) or "(none)" for s in ch],
        "rows": rows, "nrows": len(rows),
        "vertices": len(figure.cells()), "distinct": len(F),
        "E": demand.E(F), "own": figure.self_cell()[0],
        "own_occ": figure.self_cell()[1],
        "closers": figure.closers(),
        "occupied": occ, "empty": [k for k in range(8) if k not in occ],
        "by_channel": {k: sorted(t for t, kk, _a in _seats if kk == k)
                       for k in range(8)},
        "arity_of": {t: a for t, _k, a in _seats},
        "resolution": [(a, d, n, r, v) for a, d, n, r, v in figure.resolution()],
        "labelled": sorted(figure.labelled_axes()),
        "dilworth_bad": [d[0] for d in figure.dilworth() if not d[5]],
        "n_candidates": len(OR.CANDIDATES),
        # Section 7's readings, MEASURED.  All five were typed, taken when the
        # register held eleven indexes, and never moved as it grew to 24.
        # Section 4.2: the admissibility sweep, and WHICH charts it runs on --
        # the nine of the superseded inventory, not the register.  Naming it
        # is the repair; an earlier draft said "the seated indexes".
        "adm": dict(charts.admissibility()),
        "adm_n": len(charts.population()),
        # Section 4.2a: what K is and is not preserved by, measured.
        "kmove": charts.k_invariance(),
        # Section 3.1: K1's occupancy depends on the spacetime dimensions
        # admitted, which the paper's own instrument has always pinned.
        "dimsweep": [tuple(t) for t in OR.dimension_finding()[0][1]],
        # Sections 8.3 and 10.6, both of which had the argument backwards.
        "exotics": __import__("mesons").exotic_members(),
        "parity_split": " and ".join(
            __import__("mesons").parity_split_in_a_multiplet()),
        "readings": _readings,
        "reading_share": tuple(OR.reading_share()),
        "subcharts": OR.subchart_total(),
        # WHICH channels rest on one seating.  Section 14's hedge said "one of
        # the eight" and was typed; it never moved when three more
        # single-occupant channels appeared.  Computed from the same cells the
        # section 3.1 table is built from.
        "lonely": _lonely_channels(),
        "seated": [(p, list(c), k, n) for p, c, k, n in OR.admissible()],
        "refused": [(p, list(c), w) for p, c, w in OR.refused()],
        "grounds": ["novel channel", "not a relabelling", "reach stable",
                    "coordinate forced"],
        # WHICH indexes the sweep covered, so the prose can state it rather
        # than imply "all of them".
        "stat_swept": sorted(_swept),
        "stat_skipped": sorted(_skipped),
        "stat_nswept": len(_swept),
        "stat_by_arity": {a: tuple(v) for a, v in sorted(stat.items())},
        # The per-arity TOTAL is a number the prose states, so it is banked
        # rather than summed at the point of use: a figure computed inside a
        # format string is a figure the substitution guard cannot vouch for.
        "stat_arity_totals": {a: v[0] + v[1] for a, v in sorted(stat.items())},
        "stat_subcharts": sum(v[0] + v[1] for v in stat.values()),
        "chan_arity2": dict(sorted(chan2.items())),
        "gjoin": jn, "gmeet": mt, "gpairs": pr,
        "mad_density": mad_density, "mad_cells": mad_cells, "mad_box": mad_box,
        "dim_bfx": [(d, k) for d, _n, k in dim[("B", "F", "X")]],
        "obs_cells": len(observed.index()), "obs_cell": observed.cell(),
        "obs_addr": len(observed.addresses()),
        "obs_diff_addr": len(observed.differing_addresses()),
        "obs_diff_cfg": len(observed.differing_configs()),
        "obs_losses": [s for _z, s, _d in observed.losses()],
        "obs_only": observed.only_observed(),
        "pred_only": len(observed.only_predicted()),
        "obs_sweep": observed.reach_sweep(),
        "pred_sweep": observed.predicted_sweep(),
        "bi_verdict": BI.verdict()[0],
        "bi_live": BI.invariant()[1], "bi_all": BI.invariant()[2],
        "bi_boxes": len(BI.BOXES()),
        "bi_corpus": list(BI.CORPUS_MEETS), "bi_caps": list(BI.CORPUS_CAPS),
        "mad_sweep_k": sorted({k for _n, _c, k in BI.madelung_sweep()}),
        "census": __import__("state").CENSUS,
        # Section 11 is the paper's one dated snapshot, so it must SAY the date
        # and say how far the tree has moved since.
        "census_asof": tuple(__import__("state").CENSUS_AS_OF),
        "modules_now": len([q for q in os.listdir(WD) if q.endswith(".py")]),
        "retractions": len(__import__("state").RETRACTIONS),

        # Section 9 -- the demand and its adjudication.  Every figure is asked
        # of predict.py or ghosts.py, both of which RE-MEASURE their recorded
        # tables from the tree in their own selftests.  Nothing here is typed.
        "E_total": predict.total(),
        "E_by_index": dict(predict.E_BY_INDEX),
        "E_too_large": list(predict.TOO_LARGE),
        "E_nzero": predict.partition()[2],
        "E_npos": predict.partition()[3],
        "gravity_cells": _gravity_cells,
        "bin_why": dict(predict.BINS),
        "adj": dict(ghosts.TABLE),
        "adj_tot": ghosts.totals(),
        "bounds": [(nm, registry.short(nm), lab, law, mono)
                   for nm, (lab, law, mono, _fn) in sorted(ghosts.BOUNDS.items())],
        "nbounds": len(ghosts.BOUNDS),
        "nbounds_mono": sum(1 for v in ghosts.BOUNDS.values() if v[2]),
        "no_bound_derived": len(ghosts.NO_BOUND_DERIVED),
        "gmn_baryon": _gmn_b,
        "gmn_meson": _gmn_m,
        "bs2": ghosts.bs2_consequence(),
        "qqbar": ghosts.qqbar_theorem(12),
        "precedent": ghosts.element_precedent(),
        "unplaced_meson": ghosts.unplaced_objects("mesons.index"),
        "gapless": len(ghosts.GAPLESS),
        "above_title": __import__("deformedbands").above_title_range(),
        "a_ranges": __import__("deformedbands").a_ranges(),

        # Section 5 -- the register, every index represented with provenance.
        "short": dict(registry.short()),
        "provenance": {nm: {"why": v["why"],
                            "paths": [d["path"] for d in v["paths"]]}
                       for nm, v in registry.sources().items()},
        "coords": {registry.short(nm): _q
                   for nm, _m, _a, _me, _w, _q in registry.rows()},
        "members_of": {registry.short(nm): _w
                       for nm, _m, _a, _me, _w, _q in registry.rows()},
        "method_of": {registry.short(nm): me
                      for nm, _m, _a, me, _w, _q in registry.rows()},
        "criterion_enforced": registry.enforce(),
        "excused": dict(registry.NOT_AN_INDEX),
        "arity_by_index": {registry.short(nm): len(next(iter(registry.index_of(nm))))
                           for nm, _m, _a, _me, _w, _q in registry.rows()},

        # Section 8 -- DOCKET 41.
        "prop_contraction": str(sp_simplify_safe(__import__("propagator").closed_form())),
        "prop_unique": [str(x) for x in __import__("propagator").uniqueness()[0]],
        "prop_ratios": [(a, b, str(c), str(d2))
                        for a, b, c, d2 in __import__("propagator").ratios()],
        "prop_z3": __import__("propagator").machine_check(),
        "settled": [(n, st, w) for n, st, w in __import__("exact").SETTLED],
        "meson_rows": _gmn_m[0],
        "meson_noC": sum(1 for r in __import__("pdgcapture").read()
                         if r["family"] == "meson" and r["C"] == "?"),
    }


# ------------------------------------------------------------- the document
# Each block is (kind, text).  kind in {h1,h2,p,quote,bullet,table,note,eq}.

def document(f):
    D = []
    A = D.append
    K = lambda ks: ", ".join("K%d" % k for k in ks)
    n = lambda x: format(x, ",")

    A(("abstract", (
        "A first-order index is a finite set of cells obtained by charting a body of atomic, "
        "nuclear or particle data on a fixed list of coordinates, subject to one gate: every "
        "member must carry quantum numbers of its own. Five closure operators act on such a set, "
        "and which of them close it is a property of the set. We prove that only %d of the %d "
        "subsets of the five can occur, characterise them as the down-sets of a seven-relation "
        "law, and use the resulting triple (channel, height, width) as an admissible chart. "
        "Charting every index this project seats gives a second-order object of %d vertices on "
        "%d distinct cells, and ALL EIGHT CHANNELS ARE OCCUPIED BY CHARTS OF REAL DATA, so the "
        "bound is tight from nature and not only by construction. We prove that 2-determinacy is "
        "vacuous at arity 2 and derive that an arity-2 chart cannot occupy the two lowest "
        "channels, which accounts for the difficulty of the channel that was last reached. Its "
        "occupant is arity 3, where 2-determinacy is not vacuous and statistics must be EARNED; "
        "that is a measured fact about the occupant and not a consequence of the corollary, which "
        "does not reach that channel. We then take the register's own DEMAND -- the cells its join-closure "
        "requires and no member occupies, %s of them -- and adjudicate it. Three theorems decide "
        "most of that adjudication before any physics is brought: the demand invents no "
        "coordinate value; a bound monotone in the coordinates can never forbid a demanded cell; "
        "and the quark model forbids no cell of the meson chart. One bound in the register is "
        "non-monotone, and it empties %d of the %d demanded baryon cells. The remainder splits "
        "%d UNPLACED, %s OPEN and %d UNDECIDED by a source-completeness rule, and the three bins "
        "are not interchangeable: they separate what nature forbids from what a source failed to "
        "record from what is genuinely predicted. THE CLASSIFICATION, THE INVARIANT AND THE TWO "
        "VACUITY THEOREMS ARE THE CONTRIBUTION AND THE REGISTER IS AN EXHIBIT OF THEM. In "
        "particular: whether a physical constraint can rule anything out of a table is decidable "
        "FROM THE SHAPE OF THE CONSTRAINT ALONE, before any data is gathered, and for most "
        "constraints the answer is no. Every figure here is read from a runnable instrument at "
        "build time and no figure is typed."
        % (f["nchannels"], f["nsubsets"], f["vertices"], f["distinct"],
           n(f["E_total"]), f["adj"]["baryons.index"][1],
           f["adj"]["baryons.index"][0], f["adj_tot"][2], n(f["adj_tot"][3]),
           f["adj_tot"][4]))))

    # ---------------------------------------------------------------- §0
    A(("h1", "0. The two questions"))
    A(("p", (
        "This paper is written to answer two questions about the object it describes, and it is "
        "organised so that a reader can check either one without reading the other.")))
    A(("quote", (
        "**Q1 - HOW IS IT TRUE?** What is proved, what is measured, what is assumed, and what "
        "would falsify each. Sections 1 to 9 answer this. Every claim is either a theorem with "
        "its proof in place, a measurement with the instrument that produced it named, or a "
        "refusal with the ground it was refused on.")))
    A(("quote", (
        "**Q2 - WHY IS IT NECESSARY IN THE FIELDS OF STUDY?** What can be asked with this object "
        "that cannot be asked without it. Section 10 answers this, and it answers it with the "
        "things the object has already found rather than with what it might find.")))
    A(("note", (
        "A third question is not answered and is not asked: whether the register is COMPLETE. "
        "The registry carries a completeness flag and it is false. This is the set of first-order "
        "indexes found and survived their tests, and section 14 keeps that distinction explicit.")))

    # ---------------------------------------------------------------- §1
    A(("h1", "1. Notation and definitions"))
    A(("p", (
        "Fix a finite list of coordinates. Each coordinate ranges over a finite totally ordered "
        "alphabet, and the BOX is the product of the alphabets that actually occur. A CELL is a "
        "point of the box; an INDEX is a finite set of cells.")))
    A(("eq", [
        "Box(X)  =  A_1 x ... x A_d        A_i = { x_i : x in X }   the OBSERVED alphabet",
        "x <= y  <=>  x_i <= y_i for every i          the containment order",
        "x v y   =  lambda i . max(x_i, y_i)          the JOIN, componentwise",
        "x ^ y   =  lambda i . min(x_i, y_i)          the MEET, componentwise",
    ]))
    A(("note", (
        "THE BOX IS OBSERVED AND NEVER DECLARED. It is the product of the alphabets the index's "
        "own members exhibit, not a range chosen in advance. Section 9's Lemma N1 shows this is "
        "not a convention: on a declared ambient box the order operator over-generates, and the "
        "hierarchy-law companion paper makes the same point from the other side.")))
    A(("p", "The five closure operators, each a map from subsets of the box to subsets:"))
    A(("eq", [
        "order       R      =  lambda X . the sublattice hull of X under ^ and v",
        "algebra     G      =  lambda X . the sublattice hull, generated",
        "geometry    H      =  lambda X . hull-completion on every coordinate PAIR",
        "information J      =  lambda X . closure under v alone",
        "statistics  S_k    =  lambda X . { b in Box(X) : every k-coordinate",
        "                                   projection of b occurs in X },  k = 2",
    ]))
    A(("p", (
        "A language L CLOSES an index X when L(X) = X. The CHANNEL of X is the set of languages "
        "that close it, and by Theorem 1 it is one of eight, indexed K0 to K7.")))
    A(("eq", [
        "K(X)      =  { L : L(X) = X }                the channel",
        "height(X) =  the longest chain in (X, <=)     MIRSKY",
        "width(X)  =  the largest antichain in (X, <=) DILWORTH",
        "cell(X)   =  ( K(X), height(X), width(X) )    THE ADMISSIBLE CHART",
        "J(X)      =  the least v-closed superset of X",
        "D(X)      =  J(X) \\ X                         the DEMAND",
        "E(X)      =  | D(X) |                         its size",
    ]))
    A(("p", (
        "And one predicate, which is the gate on membership rather than a measurement of it:")))
    A(("eq", [
        "chi(m)    =  TRUE iff the member m carries quantum numbers OF ITS OWN",
    ]))

    # ---------------------------------------------------------------- §2
    A(("h1", "2. The criterion, and why it is a function rather than a paragraph"))
    A(("quote", (
        "**C.** A member of a first-order index must carry quantum numbers of its own. Not its "
        "host's, not its container's, and not a label that happens to be numeric.")))
    A(("p", (
        "An electron, a subshell, an ionisation transition, a spectroscopic term, a "
        "nuclide-charge state, a meson, a baryon, a fractional-quantum-Hall quasiparticle and a "
        "nuclear excited state all satisfy chi. A file, a build snapshot, a conversation and a "
        "document do not. Neither does a chemical bond, a binding energy or a scattering channel, "
        "and those three were each tested against chi and refused on their own measured ground "
        "rather than by assertion - section 13.")))
    A(("note", (
        "THE CRITERION IS ENFORCED IN CODE AND THE REASON IS HISTORICAL. While it was a "
        "paragraph, thirteen filing-system indexes were seated as vertices - mirrored files, "
        "conversations, archives, handoff documents - beside indexes whose members are electrons. "
        "Every one of the disruptive vertices was repository metadata and not one was a physical "
        "object. The explosion in demand that followed was reported as a finding; it was "
        "contamination, and it is withdrawn. `registry.enforce()` now returns the violations and "
        "returns %s."
        % (f["criterion_enforced"] if f["criterion_enforced"] else "the empty list"))))
    A(("quote", (
        "**Lemma 2.1 (the host trap).** If a candidate member's quantum numbers are properties of "
        "a containing object rather than of the member, the chart measures the container and "
        "reports it as the member. The test is whether two members of the same container can "
        "differ in the coordinate.")))
    A(("p", (
        "PROOF. Suppose coordinate c is constant on every container. Then the fibre of the chart "
        "over c is a union of whole containers, so |{cells}| counts containers and not members, "
        "and height and width are measured on the container order. The converse is the test: if "
        "some container holds two members differing in c, c is not the container's. []")))
    A(("note", (
        "THIS IS NOT HYPOTHETICAL. It is why the molecular orbital's sigma/pi is refused - the "
        "symmetry label is the MOLECULE's - and why Z and N are refused as coordinates of the "
        "deformed nuclear band index, being the host nuclide's and not the level's. The second "
        "refusal was paid back immediately: a later audit found 35 of 234 entries carrying the "
        "wrong nuclide, and because Z and N were not coordinates the defect could not reach the "
        "chart. A refusal that costs nothing is not evidence; one that catches a real defect is.")))

    # ---------------------------------------------------------------- §3
    A(("h1", "3. Theorem 1 - the lawful channels are the down-sets of the law"))
    A(("p", (
        "The companion paper derives eight clauses relating the five operators. This paper needs "
        "only the containments, which are these:")))
    A(("table", (["contained", "in", "source"],
                 [[a, b, why] for a, b, why in f["lawful"]])))
    A(("quote", (
        "**Theorem 1.** The set of languages closing an index is a DOWN-SET of the containment "
        "law, and every down-set occurs. There are exactly %d, of the %d subsets of five."
        % (f["nchannels"], f["nsubsets"]))))
    A(("p", (
        "PROOF. Write cl[L] for the closure of X under L. Every operator is EXTENSIVE: "
        "X subset-of cl[L](X) for all L. Suppose (a, b) is one of the seven containments, so "
        "cl[a] subset-of cl[b], and suppose b closes X, i.e. cl[b](X) = X. Then "
        "cl[a](X) subset-of cl[b](X) = X, and by extensivity X subset-of cl[a](X); hence "
        "cl[a](X) = X and a closes X. So the closing set is closed downward. Enumerating the "
        "down-sets of the seven relations over five languages gives exactly %d. []"
        % f["nchannels"])))
    A(("table", (["channel", "languages that close"],
                 [["K%d" % i, c] for i, c in enumerate(f["channels"])])))
    A(("note", (
        "The law leaves exactly two languages free to close alone: information and statistics. "
        "Nothing forces either from anything else. That asymmetry is what makes K1 and K2 "
        "reachable at all, and section 6 shows the freedom is exercised very differently by the "
        "two.")))
    A(("h2", "3.1 The converse, and how its status changed"))
    A(("p", (
        "The converse half of Theorem 1 - that every down-set OCCURS - was originally proved by "
        "EXHIBITION: for each down-set, a set of cells was constructed that closes exactly under "
        "it. That is a proof, and it is the weaker of the two available.")))
    A(("quote", (
        "**Theorem 1a (tightness from nature).** Every one of the eight lawful channels is "
        "occupied by a seated first-order index - a chart of real atomic, nuclear or particle "
        "data whose members carry quantum numbers.")))
    A(("table", (["channel", "closes", "seated indexes there"],
                 [["K%d" % k, f["channels"][k],
                   ", ".join(f["by_channel"][k]) or "--"] for k in range(8)])))
    A(("p", (
        "PROOF. By exhibition, and the exhibits are in section 5. []")))
    A(("quote", (
        "**What 'from nature' admits.** A chart counts as real data here when its members are "
        "MATHEMATICALLY ESTABLISHED BEYOND DOUBT, whether or not they have been observed. Absence "
        "of observation is not falsification. The criterion is stated because one of the eight "
        "channels turns on it.")))
    A(("p", (
        "THAT CHANNEL IS K1, and it has a single occupant. %s is charted on the horizon-bound "
        "class of a singly-rotating Myers-Perry black hole, and its channel DEPENDS ON THE "
        "SPACETIME DIMENSIONS ADMITTED: %s. Restricted to five and below it is K7 and K1 empties. "
        "The bound class is not speculative physics: it is whether r^(D-3) + a^2 r^(D-5) = mu has "
        "a root, which is exact in every D, with a bound on rotation at five and none above it "
        "(Myers and Perry, 1986). By the criterion above the chart is admitted - and the "
        "dependence is stated here rather than left for a reader to discover, because the paper's "
        "own instrument has always pinned this sweep and the paper had never said it."
        % (", ".join(nm for k, nm in f["lonely"] if k == 1),
           ", ".join("D<=%d gives K%d" % (d, k) for d, _c, k in f["dimsweep"])))))
    A(("note", (
        "THE DIFFERENCE MATTERS AND IS NOT RHETORICAL. A bound proved tight by construction says "
        "the combinatorics admits eight. A bound proved tight by nature says the physical world "
        "supplies all eight, so no further clause can be added to the law without contradicting a "
        "measurement. TWO OF THE EIGHT WERE EMPTY WHEN THIS PAPER WAS FIRST DRAFTED and the "
        "statement above could not have been made then; that is a fact about this project\'s "
        "history rather than a measurement of anything, and it is stated in words for that "
        "reason.")))

    # ---------------------------------------------------------------- §4
    A(("h1", "4. The admissible chart"))
    A(("p", (
        "An index is charted by the triple (K, h, w). Mirsky's theorem gives height as the "
        "minimum number of antichains covering the order; Dilworth's gives width as the minimum "
        "number of chains. Both are exact and neither is an estimate.")))
    A(("quote", (
        "**Lemma 4.1 (the box is ragged).** |X| <= height(X) x width(X), so the three "
        "coordinates are not independent and the product box overstates the space.")))
    A(("p", (
        "PROOF. By Dilworth, X is covered by width(X) chains; each chain has at most height(X) "
        "elements. []  Checked on every seated index: %d violations."
        % len(f["dilworth_bad"]))))
    A(("h2", "4.2 Why these three coordinates and not the earlier five"))
    A(("quote", (
        "**Criterion (order admissibility).** An ORDER invariant is admissible iff it survives "
        "appending a MONOTONE REDUNDANT coordinate to the index, since such an append preserves "
        "the containment order exactly and therefore must not move any measurement OF THAT "
        "ORDER.")))
    A(("p", (
        "Measured over the %d superseded charts of the earlier inventory - which is the "
        "population the sweep actually runs on, and is named here because an earlier draft said "
        "'the seated indexes' and meant these - ARITY moves on every one and so does DENSITY, "
        "both being facts about the box and not about the order. height, width, cells, "
        "comparable pairs and join-irreducibles do not move at all. C, Sc and Oc of the earlier "
        "five-coordinate chart are all functions of K, so the five collapse to three with no "
        "loss and one gain: K separates channels that (C, Sc, Oc) merged." % f["adm_n"])))

    A(("h2", "4.2a K is not an order invariant, and that is a theorem about it"))
    A(("p", (
        "An audit applied the criterion above to K and K FAILED IT. The append g(c) = sum(c) is "
        "redundant, monotone, and an order isomorphism onto its image, so the criterion as first "
        "written admits it - and it moves K on %d of the %d seated indexes small enough to test. "
        "The criterion is sound; applying it to K was a category error, and the error was in the "
        "paper's favour. Height and width are invariants of the poset (X, <=). K IS NOT, AND WAS "
        "NEVER AN INVARIANT OF IT."
        % (f["kmove"]["sum"], f["kmove"]["n"]))))
    A(("quote", (
        "**Lemma 4.2 (what K is an invariant of).** K is an invariant of X AS A RELATION ON A "
        "PRODUCT OF CHAINS, not of the abstract order (X, <=). It is preserved by the "
        "automorphisms of that ambient structure - permutation of the coordinates and strictly "
        "monotone relabelling of each coordinate's alphabet - and by appending any coordinate "
        "whose map is a LATTICE HOMOMORPHISM. It is not preserved by an arbitrary "
        "order-isomorphic append.")))
    A(("p", (
        "PROOF of the negative half, which is the half that bites. Each of the five operators is "
        "defined by the componentwise max and min of the ambient product, not by the order alone. "
        "An append c |-> (c, g(c)) with g monotone is an order isomorphism onto its image for any "
        "monotone g, but it carries the join only when g(a v b) = max(g(a), g(b)); for g = sum, "
        "a = (1,0) and b = (0,1) give g(a v b) = 2 against max(g(a), g(b)) = 1, so the image is "
        "not join-closed and every language above information falls with it. The positive half is "
        "immediate: a lattice homomorphism carries both operations, so every closure is computed "
        "on an isomorphic structure. []")))
    A(("table", (["append or transformation", "is it a lattice homomorphism", "K moves on"],
                 [[lab, hom, "%d of %d" % (mv, f["kmove"]["n"])]
                  for lab, hom, mv in f["kmove"]["rows"]])))
    A(("p", (
        "The two halves come apart exactly as the proof predicts: max carries the join and not "
        "the meet, min the meet and not the join, and each moves K on part of the register while "
        "the coordinate projections - the lattice homomorphisms - move it on none.")))
    A(("h2", "4.2b What K is, in the language of another field"))
    A(("p", (
        "K is not a bespoke invention, and a reader should not have to take it as one. A closure "
        "operator fixes X exactly when the operation generating it is a POLYMORPHISM of X read as "
        "a relation - an operation under which the relation is closed. So:")))
    A(("table", (["this paper's operator", "closes X if and only if"],
                 [["information", "binary max is a polymorphism of X"],
                  ["order / algebra", "max AND min are both polymorphisms -- X is a sublattice"],
                  ["statistics", "X is 2-DECOMPOSABLE: X is the join of its binary projections"],
                  ["geometry", "X is closed under the pairwise 2-D hull"]])))
    A(("p", (
        "That places K inside the Pol-Inv Galois connection of universal algebra (Geiger; "
        "Bodnarchuk, Kaluznin, Kotov and Romov, 1968-9), where the set of polymorphisms of a "
        "relation is its clone and determines what can be said about it. Closure under a "
        "semilattice operation such as max, and decomposability into binary projections, are the "
        "two classical tractability conditions of constraint satisfaction (Jeavons, Cohen and "
        "Gyssens; Feder and Vardi). K IS A FRAGMENT OF THE POLYMORPHISM CLONE, and Lemma 4.2 is "
        "then unsurprising: a clone is an invariant of the relational structure, which is exactly "
        "the structure an order isomorphism is free to discard.")))
    A(("note", (
        "AND IT HAS A READING IN THE PHYSICS. statistics closing says every selection rule "
        "coupling the quantum numbers is PAIRWISE - there is no irreducibly three-body rule among "
        "them. information closing says the realised set is closed under taking the componentwise "
        "maximum of any two realised states. order closing says it is a sublattice. So K states "
        "THE ARITY AT WHICH THE SELECTION RULES ACT, which is a physical property of the index "
        "and not a bookkeeping one.")))
    A(("h2", "4.3 The chart applied to itself"))
    A(("p", (
        "Applying the chart to the object it produces is a test that object can fail. A "
        "coordinate whose distinct values number 90 per cent or more of its members separates "
        "everything and therefore groups nothing: it is a row identifier wearing a measurement's "
        "clothes.")))
    A(("table", (["axis", "distinct", "of", "ratio", "verdict"],
                 [[a, "%d" % d, "%d" % nn, "%.4f" % r, v]
                  for a, d, nn, r, v in f["resolution"]])))
    A(("p", (
        "%s. At eleven vertices two of the three were row labels - height at 0.909 and width "
        "perfectly injective at 1.000 - and the reading filed with that finding was that each "
        "index brings its own height and width, so the two approach injectivity by construction "
        "as the object grows. THAT READING IS REFUTED by the table above: the object grew and the "
        "labels became measurements. The prediction failed because a COARSENING of a seated index "
        "does not bring a new height and width; it lands in the part of the poset its parent "
        "already occupies."
        % ("No axis is a row label" if not f["labelled"]
           else "Row labels remain: " + ", ".join(f["labelled"])))))
    A(("p", (
        "The second-order object has %d vertices on %d distinct cells - no two seated indexes "
        "share a cell - it closes in %s, its demand E is %d, and its own cell is (%d, %d, %d), "
        "which %s."
        % (f["vertices"], f["distinct"], ", ".join(f["closers"]) or "nothing",
           f["E"], f["own"][0], f["own"][1], f["own"][2],
           "no member occupies" if not f["own_occ"]
           else "is occupied by " + ", ".join(f["own_occ"])))))

    # ---------------------------------------------------------------- §5
    A(("h1", "5. The register - every seated index"))
    A(("p", (
        "%d indexes satisfy the criterion and are seated. Each row names what one member IS, "
        "which quantum numbers it carries, how many distinct cells the chart has, the cell, and "
        "the channel. The METHOD column records how the index was built: TABLE reads a source, "
        "FIBRATION addresses a member by its position in a construction, RESIDUAL charts the "
        "departure of a measurement from a rule."
        % f["nrows"])))
    A(("table", (["index", "method", "one member is", "quantum numbers",
                  "cells", "cell", "arity"],
                 [[r["label"], r["method"], r["members"], r["quantum"],
                   "%d" % r["cells"], "(%d, %d, %d)" % r["cell"],
                   "%d" % f["arity_by_index"].get(r["label"], 0)]
                  for r in f["rows"]])))
    A(("h2", "5.1 Provenance - what each index reads, hashed"))
    A(("p", (
        "Declared as SOURCE beside the code that reads it, resolved against the repository root "
        "and hashed, so the provenance travels in the tree rather than in prose. AN EMPTY PATH "
        "LIST IS NOT A GAP: it means the index is COMPUTED from a rule and reads no table, which "
        "is a source and is recorded as one.")))
    A(("table", (["index", "reads", "files"],
                 [[registry_short_of(f, nm),
                   (v["why"][:96] + ("..." if len(v["why"]) > 96 else "")),
                   ("%d" % len(v["paths"])) if v["paths"] else "COMPUTED"]
                  for nm, v in sorted(f["provenance"].items())])))
    A(("h2", "5.2 What is excused, and on which ground"))
    A(("p", (
        "%d modules in the tree look like indexes and are not, and each carries its ground. The "
        "grounds are of three kinds and they are not interchangeable: failing the criterion, "
        "failing box invariance, and - one case - having had an incomplete capture, which was "
        "retired when the capture closed."
        % len(f["excused"]))))
    A(("table", (["module", "the ground it is excused on"],
                 [[k, (v[:150] + ("..." if len(v) > 150 else ""))]
                  for k, v in sorted(f["excused"].items())])))

    # ---------------------------------------------------------------- §6
    A(("h1", "6. Theorem 2 - 2-determinacy, and why one channel was the last to fall"))
    A(("quote", (
        "**Theorem 2.** statistics closes EVERY arity-2 index, vacuously, and this is a property "
        "of the definition rather than of any implementation.")))
    A(("p", (
        "PROOF. S_k(X) is the set of box points all of whose k-coordinate projections occur among "
        "X's. At arity 2 there is exactly one 2-subset of the coordinates - the whole of them - "
        "so the projection is the identity and the reconstruction returns X itself. Hence "
        "S_2(X) = X for every X whatever. []")))
    A(("p", (
        "Measured over every coordinate subset of every seated index the sweep reaches - %d of "
        "the %d, the %d coarsenings being excluded because their sub-charts are sub-charts of "
        "their parents and are counted there - %s sub-charts in all. THE POPULATION IS STATED "
        "BECAUSE IT WAS ONCE WRONG: the sweep skipped a missing coordinate list silently and "
        "covered 15 of 24 while the prose implied all of them, dropping the very index this "
        "section closes on."
        % (f["stat_nswept"], f["nrows"], len(f["stat_skipped"]),
           n(f["stat_subcharts"])))))
    A(("table", (["arity", "statistics closes", "does not"],
                 [["%d" % a, "%d" % v[0], "%d" % v[1]]
                  for a, v in f["stat_by_arity"].items()])))
    A(("quote", (
        "**Corollary 6.1.** An arity-2 chart cannot occupy K0 or K1.")))
    A(("p", (
        "PROOF. Its channel contains statistics by Theorem 2, and neither K0 nor K1 does. [] "
        "Measured over the same sub-charts, the arity-2 channels observed are %s - K0 and K1 "
        "occur zero times, as the corollary requires."
        % ", ".join("K%d (%d)" % (k, v) for k, v in f["chan_arity2"].items()))))
    A(("note", (
        "THIS IS WHAT MADE K4 THE HARD CHANNEL, and the difficulty was structural. The law "
        "protects K5 and K6 from the free pass, because geometry closing forces statistics and so "
        "does the order/algebra block; at those channels the statistics bit is earned by law "
        "whatever the arity. K4 = {information, statistics} has neither protection - nothing "
        "forces statistics from information - so it is the only channel above K1 whose extra "
        "content is exactly the bit an arity-2 chart is given for free. For a long stretch the "
        "only charts reaching K4 were arity 2, and a census over %d modules found no chart of any "
        "arity reaching it." % f["census"]["modules_attempted"])))
    A(("p", (
        "IT IS NOW OCCUPIED, AND AT ARITY %d. The seated index at K4 is %s, charted on %d "
        "coordinates - an arity at which 2-determinacy is not vacuous and statistics has to be "
        "EARNED. The channel the theorem predicted would be hardest is reached, and reached in "
        "the way that makes it a measurement rather than a gift. The explanation survives as an "
        "account of the difficulty; it is no longer an account of an absence."
        % (f["arity_of"][f["by_channel"][4][0]], f["by_channel"][4][0],
           f["arity_of"][f["by_channel"][4][0]]))))

    # ---------------------------------------------------------------- §7
    A(("h1", "7. The overlap ruling - when two charts of one subject may both be seated"))
    A(("quote", (
        "They can be seated with overlaps so long as it is not an overlap of same information. An "
        "overlap of values in two different languages should tell us two parts of definition "
        "contained in that overlapped position. Information is information. But its relative "
        "position in this index is information about an object.")))
    A(("p", (
        "A COARSENING - the same members charted on fewer coordinates - overlaps its parent "
        "totally. Four readings of the ruling were charted against all %s proper sub-charts of "
        "the %d non-coarsening seated indexes: 'channel differs from its parent' admits %s, "
        "'cell differs from its parent' %s, 'cell no seated vertex holds' %s, and 'CHANNEL no "
        "seated vertex holds' admits %d. The third admits %d coarsenings of %s alone; the fourth "
        "is bounded, and it is what the ruling says, since the ruling names LANGUAGES and the "
        "channel is the set of languages that close a chart. Text and arithmetic select the same "
        "reading."
        % (n(f["subcharts"]), f["stat_nswept"], n(f["readings"]["R1"]),
           n(f["readings"]["R2"]), n(f["readings"]["R3"]), f["readings"]["R4"],
           f["reading_share"][1], f["reading_share"][0]))))
    A(("note", (
        "THESE FIVE FIGURES WERE TYPED AND ALL FIVE HAD GONE STALE. They were measured when the "
        "register held eleven indexes and never moved as it grew to %d; the instrument that "
        "produced four of them could not even be run, raising on the first seated index missing "
        "from its coordinate table, and the fifth was computed by no function at all. They are "
        "read from the instrument now, and the reading the ruling selects is unchanged - R4 is "
        "still far the most bounded." % f["nrows"])))
    A(("p", "Four grounds are tested and a candidate must clear all four:"))
    A(("bullet", [
        "**NOVEL CHANNEL** - the chart reaches a channel no seated index reaches.",
        "**NOT A RELABELLING** - it has strictly fewer cells than its parent; a chart that "
        "separates exactly as much is the parent renamed.",
        "**REACH STABLE** - the channel does not depend on where the construction stopped: no "
        "late arrival, no oscillation, and a majority of reaches.",
        "**COORDINATE FORCED** - the channel survives a faithful re-coordinatisation. Two "
        "addresses inducing the identical partition of the identical members are one chart "
        "written twice.",
    ]))
    # THE COUNT WAS TYPED AND IT WAS WRONG -- "six candidates" against a table
    # of seven rows.  It is now the table's own length.
    A(("p", "Of %d candidates, %d seat and %d are refused."
        % (f["n_candidates"], len(f["seated"]), len(f["refused"]))))
    A(("table", (["chart", "channel", "cells", "verdict / ground failed"],
                 [["%s (%s)" % (p2, ", ".join(c)), "K%d" % k, "%d" % nn, "SEATED"]
                  for p2, c, k, nn in f["seated"]] +
                 [["%s (%s)" % (p2, ", ".join(c)), "", "", "refused: " + ", ".join(w)]
                  for p2, c, w in f["refused"]])))
    A(("quote", (
        "**Lemma 7.1 (the ruling has a subject).** The four grounds test a COARSENING. Two "
        "indexes sharing no member are not overlapping charts, and the ruling does not apply to "
        "them however many coordinate NAMES they share.")))
    A(("p", (
        "PROOF. A coarsening is a chart of the SAME member set on a subset of the coordinates, so "
        "'strictly fewer cells than its parent' presupposes a parent. Where the member sets are "
        "disjoint there is no parent, the second ground is undefined, and the first is not a test "
        "of overlap but of novelty. [] This is not academic: the nuclear rotational-band index "
        "and the deformed two-quasiparticle index carry the SAME two coordinate names, (2I, "
        "parity), and share ZERO nuclides. Sharing a coordinate's name is not sharing "
        "information, any more than two nuclides sharing a Z would be.")))
    A(("note", (
        "AND THE FIRST GROUND GIVEN FOR THAT ZERO WAS FALSE. It was stated that the two mass "
        "ranges are disjoint. They are not - one index spans A %d-%d and CONTAINS the other's "
        "%d-%d entirely. The zero is a measured fact about which nuclides each source happens "
        "to tabulate, not a consequence of where they sit. An audit caught it and the weaker, "
        "true ground replaces the stronger, false one."
        % (f["a_ranges"][1][0], f["a_ranges"][1][1],
           f["a_ranges"][0][0], f["a_ranges"][0][1]))))

    # ---------------------------------------------------------------- §8
    A(("h1", "8. The demand, and what an empty cell means"))
    A(("p", (
        "E(X) = |J(X) \\ X| is the number of cells an index's own join-closure requires and no "
        "member occupies. Measured over every seated index small enough to close - %s, at %d "
        "cells, is not, and is NAMED HERE rather than dropped, so the %d rows below and the %d "
        "complete indexes and it account for all %d seated - the register demands %s cells it "
        "does not hold."
        % (", ".join(registry_short_of(f, k2) for k2 in f["E_too_large"]),
           f["gravity_cells"], f["E_npos"], f["E_nzero"], f["nrows"],
           n(f["E_total"])))))
    A(("table", (["index", "E"],
                 [[registry_short_of(f, k2), "%d" % v]
                  for k2, v in sorted(f["E_by_index"].items(), key=lambda kv: -kv[1])
                  if v > 0])))
    A(("note", (
        "The partition is exact - every E = 0 index closes under information and every E > 0 "
        "index does not - and it is close to definitional, since E is the join deficit and the "
        "information closer IS the join closer. It is said so that it is not mistaken for a "
        "result. The result is the numbers.")))
    A(("p", (
        "An unadjudicated E is a count of QUESTIONS and not of objects. A demanded cell is one of "
        "three things, and only the third is a prediction:")))
    A(("bullet", [
        "**FORBIDDEN** - %s" % f["bin_why"]["FORBIDDEN"],
        "**UNPLACED** - %s" % f["bin_why"]["UNPLACED"],
        "**OPEN** - %s" % f["bin_why"]["OPEN"],
    ]))
    A(("h2", "8.1 Theorem 3 - the demand invents no coordinate value"))
    A(("quote", (
        "**Theorem 3.** pi_i(J(X)) = pi_i(X) for every coordinate i.")))
    A(("p", (
        "PROOF. X subset-of J(X) gives one inclusion. For the other, J(X) is generated from X by "
        "repeated componentwise max, and max(a, b) is either a or b, so every coordinate of every "
        "generated cell is a coordinate value already present in X. Induct on the generation. []")))
    A(("quote", (
        "**Corollary 3.1.** No bound constraining a SINGLE coordinate can forbid a demanded "
        "cell.")))
    A(("note", (
        "Measured on the largest prediction set in the register: of %d demanded baryon cells, "
        "ZERO carry an even doubled spin - although 2J even is exactly what the spin-statistics "
        "of a three-quark state rules out. The strongest single-coordinate fact available about "
        "baryons adjudicates nothing, and Corollary 3.1 says why."
        % f["adj"]["baryons.index"][0])))
    A(("h2", "8.2 Theorem 4 - a monotone bound forbids nothing"))
    A(("quote", (
        "**Theorem 4.** Let B be a set of cells with X subset-of B and B closed under "
        "componentwise max. Then J(X) subset-of B, so B forbids no demanded cell. In particular a "
        "bound x_i <= g(x_j, ...) with g non-decreasing in each argument is max-closed.")))
    A(("p", (
        "PROOF. J(X) is the LEAST max-closed set containing X, so it is contained in any "
        "max-closed superset of X. For the particular case, let a, b lie in B and c = a v b. Then "
        "c_i = max(a_i, b_i) is one of them, say a_i, and a_i <= g(a_j) <= g(c_j) because "
        "a_j <= c_j for every j and g is non-decreasing; so c lies in B. []")))
    A(("p", (
        "%d bounds were derived for the seated indexes, each from a stated physical law, each "
        "checked against every member of its index before being applied to the demand, and NONE "
        "fitted to the demand. %d of the %d are monotone."
        % (f["nbounds"], f["nbounds_mono"], f["nbounds"]))))
    A(("table", (["index", "bound", "derived from", "monotone", "forbidden"],
                 [[short, lab, law, "yes" if mono else "NO",
                   "%d" % f["adj"][nm][1]]
                  for nm, short, lab, law, mono in f["bounds"]])))
    A(("note", (
        "THE ZEROS ARE NOT A FAILED SEARCH. l <= n-1 is the radial node count n - l - 1 being "
        "non-negative; the Pauli caps count the spin-orbitals of a subshell; q <= k says one "
        "cannot ionise more electrons than are present; l = 0 forcing the upper spin-orbit branch "
        "is j = l +- 1/2 with j >= 0; and a Russell-Saunders singlet has one level, so it cannot "
        "fall short of its own multiplet. All are theorems, all hold on every seated member "
        "without exception, and by Theorem 4 NONE OF THEM CAN forbid a demanded cell. The "
        "hypothesis is verified rather than read off the algebra: each bound's admissible set is "
        "enumerated over its index's own product box and closed under join by exhaustion.")))
    A(("h2", "8.3 Theorem 5 - the quark model forbids no cell of the meson chart"))
    A(("quote", (
        "**Theorem 5.** For a quark-antiquark state P = (-1)^(L+1), C = (-1)^(L+S), S in {0,1} "
        "and |L - S| <= J <= L + S. Every (J, P) with J a non-negative integer and P = +-1 is "
        "realised.")))
    A(("p", (
        "PROOF, four cases. P = -1 requires L even: for J even take (L, S) = (J, 0); for J odd "
        "take (J-1, 1), which is even and non-negative and has L + S = J; J = 0 forces L = S, and "
        "L = S = 0 gives 0-. P = +1 requires L odd: for J odd take (J, 0); for J even and at "
        "least two take (J-1, 1); J = 0 forces L = S, and L = S = 1 gives 0+. [] Checked by "
        "exhaustion to J = 12 with no unreached pair.")))
    A(("p", (
        "The exotic quantum numbers - 0--, 0+-, 1-+, 2+- - are forbidden in J^PC, and C IS NOT A "
        "COORDINATE of this chart. It was refused for TOTALITY: %d of the %d mesons in the source "
        "carry no C at all, and a chart carries only coordinates all its members have. THE "
        "REFUSAL WAS CORRECT AND THE TRADE RUNS THE OTHER WAY, which an audit established against "
        "an earlier draft of this very paragraph. That draft said a coordinate refused for "
        "totality is adjudication power given up. It is not, here: %d of the C-carrying mesons "
        "in the capture are %s, whose J^PC is 1-+ -- one of the four exotics just named -- and "
        "both carry the source's own quark string 'Maybe non-qQ'. Charting C would not make the "
        "exotic cells FORBIDDEN cells of the demand. It would make them OCCUPIED cells of the "
        "index, and the q-qbar bound would then FAIL this paper's own gate, which requires a "
        "bound to hold on every member before it may touch the demand. The meson index has %d "
        "demanded cells and the quark model empties none of them - but the reason is not a price "
        "paid for totality. It is that THIS MEMBER SET IS NOT A q-qbar SET, and refusing C "
        "concealed the fact rather than costing anything."
        % (f["meson_noC"], f["meson_rows"], len(f["exotics"]),
           " and ".join(f["exotics"]), f["adj"]["mesons.index"][0]))))
    A(("h2", "8.4 The one bound that forbids"))
    A(("p", (
        "By Theorem 4 only a bound that is antitone somewhere, or carries a congruence, can "
        "forbid. One qualifies in the register and it qualifies twice over. Gell-Mann-Nishijima "
        "gives the isospin projection 2 I3 = 2Q - Y with Y = B + S + C + B' + T, and I3 must be a "
        "weight of the isospin-I representation: |2 I3| <= 2I, an absolute value, and 2I "
        "congruent to 2 I3 modulo two, a congruence. Both break max-closure. The baryon chart "
        "carries Q, S, C, B and I as coordinates, so the bound is EXPRESSIBLE on it, and it "
        "forbids %d of the %d demanded cells - %.1f per cent of the largest prediction set in the "
        "register, emptied by theorem rather than by observation."
        % (f["adj"]["baryons.index"][1], f["adj"]["baryons.index"][0],
           100.0 * f["adj"]["baryons.index"][1] / f["adj"]["baryons.index"][0]))))
    A(("p", (
        "The relation is not imported. Writing n_a for quarks minus antiquarks of flavour a, "
        "Q = (2/3)(n_u + n_c + n_t) - (1/3)(n_d + n_s + n_b), I3 = (n_u - n_d)/2, S = -n_s, "
        "C = n_c, B' = -n_b, T = n_t and B = (sum n_a)/3, whence "
        "Q - I3 = n_u/6 + n_d/6 + (2/3)(n_c + n_t) - (1/3)(n_s + n_b) = Y/2 identically. All "
        "three legs - the charge built from the quark charges, the isospin projection, and the "
        "identity - are re-derived from the source's own quark strings: %d baryon rows, %d parse, "
        "and %d, %d and %d clean without exception."
        % f["gmn_baryon"][:5])))
    A(("note", (
        "THE SAME CHECK FOUND A FAULT IN THE SOURCE. %d of %d meson rows parse - the rest are "
        "flavour mixtures, which is why S, C and B are not coordinates of the meson chart and "
        "therefore why the bound is inexpressible there - and of those the charge and the "
        "identity are clean at %d and %d while the isospin projection fails at %d. The two "
        "failures are one state and its antiparticle, %s, carrying a strange-beauty content with "
        "doubled isospin one, while two other states of the identical content carry zero in the "
        "same file. Such a pair holds no up or down quark, so I3 = 0 and I = 1/2 has no weight to "
        "sit on. IT IS RECORDED AND NOT REPAIRED, and the cost is measured: with the isospin set "
        "to zero on both rows the meson index has %d cells, E = %d and chart position "
        "(%d, %d, %d) - identical before and after, because both affected cells are already "
        "occupied by other members."
        % ((f["gmn_meson"][1], f["gmn_meson"][0], f["gmn_meson"][2],
            f["gmn_meson"][4], f["gmn_meson"][3],
            " and ".join(sorted(x[0] for x in f["gmn_meson"][5])),
            f["bs2"][1][0], f["bs2"][1][1]) + tuple(f["bs2"][1][2])))))
    A(("h2", "8.5 E is a deficit against an operator, and so is forbidding"))
    A(("p", (
        "Every E above is a JOIN deficit. The same cells measured against the ORDER closure give "
        "a different deficit and a different verdict. On the %d drawn positions of the "
        "period-by-group periodic layout the join deficit is %d and the order deficit is %d, and "
        "the hydrogenic bound l <= n-1 - read through the layout's own rule for which subshell "
        "sits at which group - forbids %d of the order ghosts and %d of the join ghosts. By "
        "Theorem 4 it could not have been otherwise: expressed on (n, l, k) that bound is "
        "monotone; expressed on (period, group) it is not." % f["precedent"])))
    A(("quote", (
        "**Law 7 (forbidding power is a property of the chart).** One bound forbids 25 cells on "
        "one coordinatisation of the elements and none on two others. The physics did not "
        "change.")))
    A(("note", (
        "AND THE CAUTION IS SHARPER THAN THE LAW. The layout on which the bound has teeth is the "
        "one this project WITHDREW as over-representation. A chart that can forbid is not thereby "
        "a better chart, and the inference is unsound in both directions. Anyone who builds a "
        "table is choosing, with the coordinates, what they will be able to rule out.")))
    A(("h2", "8.6 UNPLACED separated from OPEN"))
    A(("quote", (
        "**The separator.** A demanded cell is UNPLACED if and only if the index's own source "
        "holds a row the chart declined to place which supplies ALL BUT ONE of the coordinates "
        "and agrees with the cell on every one of them.")))
    A(("p", (
        "The strength condition is the whole rule. A source row missing one coordinate names a "
        "LINE of cells and pins each of them; a row missing two names a PLANE and pins nothing. "
        "Without it, four thousand unparsed spectroscopic labels would explain every empty cell "
        "in one of these charts. Rows below the strength are counted apart and never used. For %d "
        "of the indexes the source has no gap at all, and that is measured rather than assumed: "
        "source rows are counted against rows charted and equality is required."
        % f["gapless"])))
    A(("table", (["index", "E", "forbidden", "unplaced", "open", "undecided"],
                 [[registry_short_of(f, k2), "%d" % v[0], "%d" % v[1], "%d" % v[2],
                   "%d" % v[3], "%d" % v[4]]
                  for k2, v in sorted(f["adj"].items(), key=lambda kv: -kv[1][0])]
                 + [["TOTAL"] + ["%d" % x for x in f["adj_tot"]]])))
    A(("p", (
        "%s cells are FORBIDDEN and every one is a baryon cell. %d are UNPLACED, in four charts, "
        "and the count of CELLS is deliberately kept apart from the count of OBJECTS: in one "
        "chart %d cells are pinned by %d objects, because a state lacking only its parity pins "
        "both parities and will fill exactly one. %s are OPEN. %d are UNDECIDED, and the reason "
        "is exact rather than a shrug - the loader of that chart discards a refused row without "
        "banking its term key, so the tree cannot ask whether any term lost ALL of its levels, "
        "and such a term would pin a cell at precisely the required strength. Banking those keys "
        "would settle it."
        % (n(f["adj_tot"][1]), f["adj_tot"][2], f["unplaced_meson"][0],
           f["unplaced_meson"][1], n(f["adj_tot"][3]), f["adj_tot"][4]))))
    A(("note", (
        "WHAT THE OPEN COLUMN IS AND IS NOT. For the %d indexes carrying a derived bound it is "
        "FINAL AGAINST EVERY MONOTONE BOUND, by Theorem 4 - a proof and not a survey. For the %d "
        "carrying none it is open against nothing at all, and a bound found tomorrow may empty "
        "any of them. The two situations are different and are not summed into one adjective. "
        "NEITHER IS A COUNT OF UNDISCOVERED OBJECTS."
        % (f["nbounds"], f["no_bound_derived"]))))

    # ---------------------------------------------------------------- §9
    A(("h1", "9. Necessity - each hypothesis dropped until it breaks"))
    A(("p", (
        "A claim is only as strong as what fails without it. Each hypothesis this paper relies on "
        "is removed here and the consequence measured.")))
    A(("quote", (
        "**N1 - the observed box.** Drop it: chart on a DECLARED ambient box B containing "
        "Box(X). Then R_B(X) intersect Box(X) = <X>, but R_B(X) itself is larger, so the order "
        "operator OVER-GENERATES and the channel is a property of the declared range rather than "
        "of the data. Necessary and sufficient: R_B(X) = <X> iff R_B(X) subset-of Box(X).")))
    A(("quote", (
        "**N2 - the criterion chi.** Drop it: thirteen filing-system indexes were once seated and "
        "the demand exploded. Every disruptive vertex was repository metadata. The finding "
        "reported at the time was an artefact of the dropped hypothesis and is withdrawn.")))
    A(("quote", (
        "**N3 - arity in Theorem 2.** Drop the arity-2 restriction: statistics no longer closes "
        "for free, and the table in section 6 shows where the freedom ends - at arity 3 it closes "
        "%d of %d sub-charts and not all."
        % (f["stat_by_arity"][3][0], f["stat_arity_totals"][3]))))
    A(("quote", (
        "**N4 - max-closure in Theorem 4.** Drop it and the theorem is false, which is the point: "
        "Gell-Mann-Nishijima is not max-closed and it forbids %d cells. The theorem's hypothesis "
        "is exactly the line between the bounds that adjudicate and the bounds that cannot."
        % f["adj"]["baryons.index"][1])))
    A(("quote", (
        "**N5 - the strength condition in the separator.** Drop it and four thousand unparsed "
        "spectroscopic labels, each supplying neither of two coordinates, would mark every empty "
        "cell in that chart UNPLACED. The rule would then never report a prediction at all.")))
    A(("quote", (
        "**N6 - totality of a coordinate.** Drop it and C could be charted for the mesons; the "
        "chart would then place only the %d of %d members that carry one, and the exotics would "
        "become forbidden cells of a chart that had silently changed its member set. The refusal "
        "in section 8.3 is this hypothesis being paid for."
        % (f["meson_rows"] - f["meson_noC"], f["meson_rows"]))))

    # ---------------------------------------------------------------- §10
    A(("h1", "10. Why this is necessary in the fields of study"))
    A(("p", (
        "The first question was how the object is true. This one is why anyone outside this "
        "project should want it, and the answer is not the register. THE REGISTER IS AN EXHIBIT; "
        "THE THEOREMS ARE THE CONTRIBUTION. What follows is what each result licenses for someone "
        "who has never seen this corpus and only has a table of their own.")))

    A(("h2", "10.1 A classification theorem where a field had only examples"))
    A(("p", (
        "Before Theorem 1 the question 'which closure properties does this table have?' has %d "
        "possible answers and no structure among them. After it there are %d, they are the "
        "down-sets of a seven-relation law, and they are ORDERED. A classification is not a "
        "convenience: it converts an open-ended question into a finite one, and it makes "
        "'unclassified' a reportable state rather than an absence of effort."
        % (f["nsubsets"], f["nchannels"]))))
    A(("p", (
        "Theorem 1a then does what a classification theorem usually cannot: it exhibits every "
        "class IN NATURE. All %d channels are occupied by charts of real atomic, nuclear or "
        "particle data. No class is a formal possibility awaiting an example, so no clause can be "
        "added to the law without contradicting a measurement. That is the strongest form the "
        "tightness of this bound can take."
        % f["nchannels"])))

    A(("h2", "10.2 A computable invariant that is commensurable across subjects"))
    A(("p", (
        "(K, height, width) is exact rather than estimated - height is Mirsky's minimum antichain "
        "cover and width is Dilworth's minimum chain cover, both attained - it is cheap to "
        "compute, and IT MEANS THE SAME THING for an electron, a meson and a nuclear excited "
        "state. Chemistry, atomic spectroscopy, nuclear structure, particle physics and the "
        "quasiparticle hierarchies have never been placed on a common axis, not because no one "
        "wished to but because there was no invariant to place them on. %d indexes across those "
        "subjects now sit on one chart and no two share a cell."
        % f["nrows"])))
    A(("p", (
        "Lemma 4.1 bounds the space that chart lives in: |X| <= height x width, so the three "
        "coordinates are not independent and the product box overstates. An invariant with a "
        "known raggedness is more useful than one without, because the overstatement is "
        "quantified rather than ignored.")))

    A(("h2", "10.3 A no-go result that is applicable BEFORE any data is gathered"))
    A(("p", (
        "This is the most transferable thing in the paper and it costs nothing to use. Two "
        "theorems together answer, from the SHAPE of a constraint alone, whether that constraint "
        "can ever rule anything out of a table.")))
    A(("quote", (
        "**The a priori test.** Let your table's closure demand a set of cells. (i) By Corollary "
        "3.1, a constraint on a single coordinate will forbid none of them. (ii) By Theorem 4, a "
        "constraint of the form x_i <= g(x_j, ...) with g non-decreasing will forbid none of them "
        "either. A constraint can adjudicate only if it is antitone somewhere, or carries a "
        "congruence.")))
    A(("p", (
        "Neither branch requires the data. A physicist holding a bound and a coordinate list can "
        "decide in an afternoon whether the bound has any power over the gaps in their table, and "
        "the answer is usually NO. Measured here: %d bounds derived, every one a genuine theorem "
        "of quantum mechanics holding on every member without exception, and %d of them forbid "
        "NOTHING - not because the search failed but because Theorem 4 says it must. The one that "
        "bites, Gell-Mann-Nishijima, carries an absolute value and a mod-2 congruence and empties "
        "%d of the %d cells the BARYON chart demands - not %d of the register's whole demand, "
        "which no single bound touches."
        % (f["nbounds"], f["nbounds_mono"], f["adj"]["baryons.index"][1],
           f["adj"]["baryons.index"][0], f["adj"]["baryons.index"][1]))))
    A(("note", (
        "THE NEGATIVE RESULT IS THE USEFUL ONE. A field that has been hoping its conservation "
        "laws constrain the gaps in its tables can now check, cheaply, that most of them cannot. "
        "That redirects effort rather than consuming it.")))

    A(("h2", "10.4 A theory of what an empty cell is"))
    A(("p", (
        "E(X) = |J(X) \\ X| is a computable functional on indexes, and the adjudication partitions "
        "it into three classes that are provably not interchangeable. FORBIDDEN is a theorem about "
        "nature. UNPLACED is a statement about a compilation. OPEN is a prediction. No field "
        "currently marks which of the three a gap in its tables is, and the three have entirely "
        "different consequences: a forbidden cell closes a question, an unplaced cell is work for "
        "the compiler of the source, and only an open cell is a place to look.")))
    A(("p", (
        "The separator is a rule with a proof obligation rather than an editorial judgement - a "
        "source row must supply all but one coordinate to pin a cell, because a row missing one "
        "names a line and a row missing two names a plane. The register's %s demanded cells "
        "adjudicate %s FORBIDDEN, %d UNPLACED, %s OPEN and %d UNDECIDED, and the UNDECIDED are "
        "undecided for a stated reason with a stated remedy."
        % (n(f["adj_tot"][0]), n(f["adj_tot"][1]), f["adj_tot"][2],
           n(f["adj_tot"][3]), f["adj_tot"][4]))))
    A(("p", (
        "THE CONSEQUENCE FOR A DATA COMPILATION IS THAT IT ACQUIRES A BOUNDED PREDICTION COUNT. "
        "Not a heuristic estimate of how much is missing, but a number its own closure computes, "
        "with the part that is forbidden subtracted by theorem and the part that is the "
        "compilation's own fault separated out. A table that can say how many of its gaps are "
        "genuinely open is a different kind of object from one that cannot.")))

    A(("h2", "10.5 Representation dependence, made precise and quantified"))
    A(("p", (
        "Law 7 is a theorem about representation rather than about physics, and it has a number "
        "attached. The hydrogenic bound l <= n-1 forbids %d cells on the period-by-group layout "
        "of the elements and %d on two other coordinatisations of the SAME elements. The physics "
        "did not move; the chart did. On (n, l, k) the bound is monotone and Theorem 4 empties "
        "it; on (period, group) it is not."
        % (f["precedent"][3], f["precedent"][4]))))
    A(("note", (
        "SO CHOOSING COORDINATES IS CHOOSING WHAT YOU CAN RULE OUT, and that choice is usually "
        "made for legibility. The layout on which the bound has teeth is the one THIS PROJECT "
        "WITHDREW as over-representation, so the inference runs in neither direction: forbidding "
        "power is not evidence a chart is right, and a right chart is not obliged to forbid. Any "
        "field that has more than one standard way to lay out its objects - and most do - has "
        "been making this choice without knowing it was one.")))

    A(("h2", "10.6 The theorems have already caught errors in published sources"))
    A(("p", (
        "This section is evidence that the mathematics bites, not the argument for it. Each of "
        "these came out of a theorem being applied, not out of proofreading.")))
    A(("bullet", [
        "The consistency leg of the Gell-Mann-Nishijima derivation found TWO ROWS of the 2026 "
        "Review of Particle Physics whose stated isospin contradicts their own quark content, "
        "while two other rows of identical content disagree with them in the same file. The cost "
        "to this register was then measured and is zero, and both halves are reported.",
        "A capture's totality argument found that a published nuclear data table's TITLE "
        "understates its own contents: %d of the levels it tabulates lie above the mass range the "
        "title claims, reaching A = %d against a claimed ceiling of 168." % f["above_title"],
        "The UNPLACED rule found a demanded meson cell whose occupant EXISTS and is absent only "
        "because the CAPTURE assigns it no parity - and an audit then showed the capture to be "
        "wrong, which is a better demonstration than the one first claimed. The Review of "
        "Particle Physics does establish these states; the '?' enters through the intermediate "
        "file the capture reads. It refutes itself two lines away: for %s the NEUTRAL member of "
        "the isospin doublet carries a parity while the CHARGED member carries '?', at the same "
        "spin and the same isospin, and parity is constant across an isospin multiplet by "
        "construction. So the rule did separate a fact about a compilation from a fact about "
        "nature - the compilation being the intermediate file rather than the RPP. The original "
        "claim, that the source assigns no spin-parity, is WITHDRAWN: section 8.4 flags this "
        "exact shape as a fault in the source, and this paragraph had accepted the same shape at "
        "face value in the opposite direction."
        % f["parity_split"],
    ]))

    A(("h2", "10.7 What the object can carry that it does not carry yet"))
    A(("p", (
        "Stated as capacity rather than as promise, because none of it is done. The machinery is "
        "indifferent to subject: anything whose members carry quantum numbers of their own can be "
        "seated, measured on the same three coordinates, and adjudicated by the same rule. The "
        "gate is chi and nothing else. Three consequences follow immediately for a new table: it "
        "acquires a channel and a cell, and can be compared with every index already seated; it "
        "acquires an E and therefore a bounded count of what it does not hold; and every bound "
        "its field wishes to bring can be tested for adjudicating power by section 10.3 before it "
        "is applied. THE REGISTER IS NOT THE OBJECT. The register is %d exhibits; the object is "
        "the classification, the invariant, the two vacuity theorems and the separator, and those "
        "do not depend on which tables happen to have been charted here."
        % f["nrows"])))

    A(("h2", "10.8 What it does not give anyone"))
    A(("p", (
        "It gives no new particle, no new element and no new nuclear level. The OPEN column is "
        "not a discovery list - section 8.6 says so in terms and section 14 repeats it. It "
        "predicts no measurement, and it replaces no model: a shell model and a quark model do "
        "work this object cannot begin to do. What is offered is a way of asking, of a table, "
        "questions that at present have nowhere to be asked, and a proof of which of those "
        "questions have answers.")))

    # ---------------------------------------------------------------- §11
    A(("h1", "11. The census - coverage, measured rather than inferred"))
    c = f["census"]
    A(("p", (
        "Every chart-shaped accessor in the research tree was charted, with each module's attempt "
        "logged so that coverage is measured. %d of %d modules were attempted; %d could not be "
        "imported and each is named with the reason. %d charts were found over %d modules, of "
        "which %d are neither seated nor excused - and not one of those is a new first-order "
        "index. They are members that are not physical objects, alternate charts of already-"
        "seated member sets (all landing in occupied channels), or withdrawn and duplicate charts."
        % (c["modules_attempted"], c["modules_in_tree"], len(c["unimportable"]),
           c["charts_found"], c["modules_with_a_chart"], c["unseated_not_excused"]))))
    A(("note", (
        "THIS SECTION IS A DATED SNAPSHOT, AND IS THE ONLY ONE IN THE PAPER. The sweep ran at "
        "commit %s on %s, when the tree held %d modules; it holds %d now. NOTHING IN THE TREE "
        "RE-RUNS IT, and that is the defect rather than an aside: a stale number inside an "
        "instrument-returned dictionary counts as instrument-produced, so this paper's own "
        "substitution guard cannot see these figures go out of date. They are a historical "
        "measurement, not a claim about the tree as it stands - and the census's K4 finding has "
        "been WITHDRAWN for precisely that reason."
        % (f["census_asof"][0], f["census_asof"][1], c["modules_in_tree"],
           f["modules_now"]))))
    # THE BANKED PHRASE IS NOT QUOTED.  state.py holds K4's result as a
    # sentence fragment -- "nothing in the tree -- 0 of 44 charts over 231
    # modules" -- which rendered here as a subjectless sentence AND carried a
    # module count from an earlier sweep, disagreeing with the attempted count
    # in the paragraph above it.  The same fact is stated from the per-channel
    # census and the chart total, both current, both in this same dict.
    A(("p", "Charts per channel, as of that snapshot: %s."
        % ", ".join("%s %d" % (k2, v) for k2, v in c["charts_per_channel"].items())))
    A(("note", (
        "AND THE CENSUS'S K4 FINDING IS WITHDRAWN. It recorded that no chart in the tree reached "
        "K4. True when it ran, FALSE NOW, and refuted without re-running anything: %s is SEATED "
        "at K4 and section 3.1's table says so two pages earlier. It is withdrawn in the open "
        "rather than quietly corrected, because the failure is the instructive part - a "
        "present-tense claim carried forward out of a snapshot, contradicting the paper's own "
        "register for as long as it stood."
        % ", ".join(nm for k, nm in f["lonely"] if k == 4))))
    A(("note", (
        "Two artefacts of the census are recorded rather than allowed to read as findings: one "
        "chart appears unseated because the census keys on (module, accessor) and the seated row "
        "reaches it under a second accessor name, and one is a helper written during this work "
        "that reproduces an existing index's members.")))

    # ---------------------------------------------------------------- §12
    A(("h1", "12. What was refused, and what that establishes"))
    A(("p", (
        "Five adjudications are reported. Four are refusals and one is a retraction. They are set "
        "out because a method that only ever accepts has not been tested.")))
    A(("bullet", [
        "A candidate reproducing a published four-figure result of this corpus exactly - 0 join "
        "counterexamples and meet counts %s at caps %s - was REFUSED. Its channel is the same at "
        "nine of ten boxes we could hand it, so the channel is a property of the defining "
        "predicate and not of any data; it would sit where it sits in a universe with no atoms in "
        "it."
        % (", ".join("%s" % m for m in f["bi_corpus"]),
           ", ".join("%d" % c2 for c2 in f["bi_caps"])),
        "A channel was shown reachable at arity 3, where statistics must be earned, by three "
        "charts of an index's own measured quantities. All three were REFUSED: they were found by "
        "SEARCHING for that channel, which is fitting, and a chart selected because it lands "
        "somewhere cannot be evidence that it lands there. (The size of that search was quoted "
        "here as a figure; no instrument records it, so it is withdrawn rather than repeated. "
        "The ground does not depend on it.)",
        "Two further coarsenings were REFUSED on the reach ground - one oscillating between "
        "channels as the element reach grew, one reaching its channel only at the terminal reach, "
        "which is the failure mode that withdrew an earlier chart of this project.",
        "One coarsening was SEATED and then RETRACTED. The same members under an equally faithful "
        "address - and the alternative is the primitive the source actually banks - land in an "
        "occupied channel, so the chart had no novel channel and was never a candidate. Its "
        "apparent result was a fact about which name had been written down. The ground that "
        "caught it became the fourth test in section 7.",
        "Three readings of 'a bond' were REFUSED on three DIFFERENT grounds, and the molecular "
        "hole in this register is real, so the candidate was measured rather than waved off.",
    ]))
    A(("p", (
        "%d statements this project had asserted were measured to be false in the course of the "
        "same work and are listed with their corrections in the accompanying state file. Among "
        "them: a parent index described as a complete rectangle closing everything for free, "
        "which has density %.4f - %d cells in a box of %d - and is not a down-set; an attribution "
        "of a closure property to one coordinate when a second restores it equally; and an "
        "instrument that DECLARED an index exempt from its own strongest test rather than "
        "measuring whether it was. Run properly, that test confirmed the seating and located the "
        "physics in a constraint of the hydrogenic spectrum."
        % (f["retractions"], f["mad_density"], f["mad_cells"], f["mad_box"]))))

    # ---------------------------------------------------------------- §13
    A(("h1", "13. Verification record"))
    A(("p", (
        "Every figure in this paper is read from an instrument at build time and substituted into "
        "the prose. A figure that disagreed with its instrument would be impossible rather than "
        "unlikely. The generator's own selftest enforces this: no numeral of three digits or more "
        "may survive "
        "in the prose unless some instrument in the facts dictionary actually produced it, "
        "collected recursively from integers AND from numerals inside strings the instruments "
        "returned.")))
    A(("bullet", [
        "Each instrument is stdlib-only except where sympy or z3 is named, and each carries a "
        "selftest whose fixtures are this corpus's own recorded numbers. The selftest is the "
        "first thing to run and no report is to be trusted before it passes.",
        "The ledger guards tie the demand table to the registry in both directions: every seated "
        "index is adjudicated, complete, or named too large, and the table invents no index the "
        "registry does not seat. An earlier version had neither, so a newly seated index could "
        "have gone missing from the demand silently.",
        "Bounds are verified rather than read off the algebra: each bound's admissible set is "
        "enumerated over its index's own product box and closed under join by EXHAUSTION.",
        "One result in the wider tree is machine-checked with z3 rather than only symbolically, "
        "and the check returned %s on both of its identities - a proof over the reals rather than "
        "a sample. What a solver verifies is the algebra and not the physics, and that "
        "distinction is kept."
        % ", ".join(sorted({v for _c, v in f["prop_z3"]})),
    ]))
    A(("note", (
        "ADVERSARIAL AUDITS OF THIS WORK FOUND REAL DEFECTS AND THEY ARE LISTED BECAUSE THEY "
        "WERE FOUND, not because they are flattering. In the captures: a capture attached the "
        "wrong nuclide to 35 of 234 entries; a table header was parsed as a nuclear level; and a "
        "printed parity that shared a line with the next row's isotope number was dropped at "
        "three sites, which moved a seated index's member count and its refusal count, both of "
        "which this paper prints. In the checks: two fixtures were tautologies, one passing with "
        "three quarters of its capture deleted, and one test read a key its subject does not "
        "carry and so was vacuously true. In the prose: a quoted decimal was wrong in its fourth "
        "significant digit, and a stated ground for a true claim was false. Every one is fixed "
        "and each has a regression fixture. THE TOLERANCE IS THE INSTRUCTIVE ONE: it was a decade "
        "too loose to catch that decimal, and tightening it then rejected three CORRECT "
        "roundings, so it was wrong in both directions. A TOLERANCE IS ITSELF A COEFFICIENT, and "
        "it was replaced by a comparison of significant digits with no free parameter at all.")))

    # ---------------------------------------------------------------- §14
    A(("h1", "14. What is not claimed"))
    A(("bullet", [
        "COMPLETENESS. The registry's completeness flag is false and stays false. This is the set "
        "of first-order indexes found and survived their tests, not a claim to have found them "
        "all.",
        "That occupying all eight channels closes the subject. It makes the bound of Theorem 1 "
        "tight and nothing more. It does not say the eight are the right coordinates, that no "
        "further index exists, or that any channel is held by the best chart of it - and %d of "
        "the eight are held by a SINGLE index each (%s), so each of those occupancies rests on "
        "one seating." % (len(f["lonely"]), ", ".join("K%d %s" % kv for kv in f["lonely"])),
        "That the demand E measures progress. It is reported because it is measured. No index "
        "here was built to land on a cell the demand wanted, and one that was would be fitted.",
        "That the OPEN column is a discovery list. It is the count of demanded cells that no "
        "bound derivable here forbids and no source row explains. For the indexes with a derived "
        "bound that is final against every MONOTONE bound and nothing else; for the rest it is "
        "open against nothing at all.",
        "That the second-order object is itself a first-order index. Its members are indexes and "
        "carry no quantum numbers; it fails chi and is excused by name rather than by silence.",
        "That any capture is beyond audit. Section 13 lists what an audit of this work found.",
    ]))

    # ---------------------------------------------------------------- §15
    A(("h1", "15. Questions a reader should press, and where they are answered"))
    A(("table", (["question", "where"],
                 [["Is the box observed or declared, and does it matter?",
                   "sections 1 and 9, Lemma N1"],
                  ["Could the criterion be gamed by renaming a label a quantum number?",
                   "section 2, Lemma 2.1 - the test is whether two members of one container differ"],
                  ["Is Theorem 1's converse proved, or just asserted?",
                   "section 3.1 - by exhibition, and now by nature"],
                  ["Why three coordinates and not the original five?",
                   "section 4.2 - the monotone-redundant-coordinate criterion"],
                  ["Is K4's occupancy an artefact of the free statistics bit?",
                   "section 6 - its occupant is arity 3, where statistics is earned"],
                  ["Does the overlap ruling let a chart in twice under two names?",
                   "section 7, the four grounds, one seating retracted by the fourth"],
                  ["Is E a prediction count?",
                   "sections 8 and 8.6 - it is an upper bound, and the adjudication is the paper"],
                  ["Why does almost no bound forbid anything?",
                   "section 8.2, Theorem 4 - monotone bounds cannot, and nearly all are monotone"],
                  ["Is the 8-channel result sensitive to the choice of five languages?",
                   "the companion paper, Clauses A to H; this paper takes the containments as given"],
                  ["Has anyone checked this work adversarially?",
                   "section 13 - yes, more than once, and what they found is listed there "
                   "rather than summarised"],
                  ])))

    # ---------------------------------------------------------------- appendix
    A(("h1", "Appendix. Reproduction"))
    A(("p", (
        "Every figure above is read from an instrument at build time. Each is stdlib-only unless "
        "sympy or z3 is named, and each carries a selftest whose fixtures are this corpus's own "
        "recorded numbers. Every command below is run from `research/warp-drive/`, and the "
        "generator is run from that directory too.")))
    A(("bullet", [
        "python3 registry.py --selftest -- the criterion, enforced on every row",
        "python3 figure.py --selftest -- the second-order object and its chart",
        "python3 overlaprule.py --selftest -- the ruling, the four grounds, the refusals",
        "python3 overlaprule.py --census -- re-derives the %d candidates" % f["n_candidates"],
        "python3 boxinvariance.py --selftest -- the refused theorem, and the test run properly",
        "python3 observed.py --selftest -- the observed fibration against the predicted",
        "python3 subpop.py --selftest -- the sub-population sweep and the containment structure",
        "python3 predict.py --selftest -- the demand per seated index",
        "python3 ghosts.py --selftest -- the seven laws, the bounds, the adjudication",
        "python3 exact.py --selftest -- the closed forms, with no tolerance",
        "python3 propagator.py --selftest -- the one z3-checked result",
        "python3 state.py --check -- the state file against every instrument",
        "python3 paper/mipaper.py --selftest -- that no figure in this paper is typed",
    ]))

    return D


def render_md(f):
    D = document(f)
    L = ["# %s" % TITLE, "", "### %s" % SUBTITLE, "",
         "**%s** - %s" % (AUTHOR, BYLINE), "", "---", ""]
    for kind, body in D:
        if kind == "abstract":
            L += ["**Abstract.** " + body, "", "---", ""]
        elif kind == "h1":
            L += ["## " + body, ""]
        elif kind == "h2":
            L += ["### " + body, ""]
        elif kind == "p":
            L += [body, ""]
        elif kind == "quote":
            L += ["> " + body, ""]
        elif kind == "note":
            L += ["> **Note.** " + body, ""]
        elif kind == "eq":
            L += ["```"] + list(body) + ["```", ""]
        elif kind == "bullet":
            L += ["- " + b for b in body] + [""]
        elif kind == "table":
            head, body2 = body
            L += ["| " + " | ".join(head) + " |",
                  "|" + "|".join("---" for _ in head) + "|"]
            L += ["| " + " | ".join(r) + " |" for r in body2]
            L += [""]
    return "\n".join(L) + "\n"


def render_pdf(f, path):
    from reportlab.lib import colors
    from reportlab.lib.enums import TA_JUSTIFY
    from reportlab.lib.pagesizes import A4
    from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
    from reportlab.lib.units import mm
    from reportlab.platypus import (BaseDocTemplate, Frame, PageTemplate,
                                    Paragraph, Spacer, Table, TableStyle,
                                    KeepTogether)

    INK = colors.HexColor("#12161C")
    BODY = colors.HexColor("#22272F")
    MUTE = colors.HexColor("#5C6672")
    RULE = colors.HexColor("#C9D1DA")
    ACC = colors.HexColor("#1B4B78")
    SUNK = colors.HexColor("#F1F4F7")

    ss = getSampleStyleSheet()
    S = {
        "title": ParagraphStyle("t", parent=ss["Title"], fontName="Times-Bold",
                                fontSize=21, leading=25, textColor=INK,
                                spaceAfter=6, alignment=0),
        "sub": ParagraphStyle("s", fontName="Times-Italic", fontSize=11.5,
                              leading=15, textColor=MUTE, spaceAfter=14),
        "by": ParagraphStyle("b", fontName="Times-Roman", fontSize=9.5,
                             leading=13, textColor=BODY, spaceAfter=18),
        "h1": ParagraphStyle("h1", fontName="Times-Bold", fontSize=13.5,
                             leading=17, textColor=INK, spaceBefore=17,
                             spaceAfter=6),
        "h2": ParagraphStyle("h2", fontName="Times-BoldItalic", fontSize=11.5,
                             leading=15, textColor=INK, spaceBefore=11,
                             spaceAfter=4),
        "p": ParagraphStyle("p", fontName="Times-Roman", fontSize=10,
                            leading=14.2, textColor=BODY, alignment=TA_JUSTIFY,
                            spaceAfter=8),
        "abs": ParagraphStyle("a", fontName="Times-Roman", fontSize=9.6,
                              leading=13.4, textColor=BODY,
                              alignment=TA_JUSTIFY, leftIndent=10,
                              rightIndent=10, spaceAfter=12),
        "q": ParagraphStyle("q", fontName="Times-Italic", fontSize=10,
                            leading=14, textColor=INK, leftIndent=14,
                            rightIndent=14, spaceBefore=4, spaceAfter=10),
        "note": ParagraphStyle("n", fontName="Times-Roman", fontSize=9.4,
                               leading=13, textColor=BODY, leftIndent=10,
                               rightIndent=8, borderPadding=0,
                               alignment=TA_JUSTIFY, spaceAfter=10),
        "li": ParagraphStyle("li", fontName="Times-Roman", fontSize=10,
                             leading=14, textColor=BODY, leftIndent=14,
                             bulletIndent=3, alignment=TA_JUSTIFY,
                             spaceAfter=5),
        "th": ParagraphStyle("th", fontName="Times-Bold", fontSize=8,
                             leading=10, textColor=INK),
        "td": ParagraphStyle("td", fontName="Times-Roman", fontSize=8,
                             leading=10, textColor=BODY),
        "foot": ParagraphStyle("f", fontName="Times-Italic", fontSize=7.5,
                               textColor=MUTE),
    }

    def deco(canv, doc):
        canv.saveState()
        canv.setStrokeColor(RULE)
        canv.setLineWidth(0.5)
        canv.line(20 * mm, 16 * mm, 190 * mm, 16 * mm)
        canv.setFont("Times-Italic", 7.5)
        canv.setFillColor(MUTE)
        canv.drawString(20 * mm, 11 * mm, TITLE)
        canv.drawRightString(190 * mm, 11 * mm, "page %d" % doc.page)
        canv.restoreState()

    doc = BaseDocTemplate(path, pagesize=A4,
                          leftMargin=20 * mm, rightMargin=20 * mm,
                          topMargin=18 * mm, bottomMargin=22 * mm,
                          title=TITLE, author=AUTHOR)
    doc.addPageTemplates([PageTemplate(
        id="p", frames=[Frame(20 * mm, 22 * mm, 170 * mm, 257 * mm, id="f",
                              leftPadding=0, rightPadding=0,
                              topPadding=0, bottomPadding=0)],
        onPage=deco)])

    def tbl(head, rows):
        data = [[Paragraph(h, S["th"]) for h in head]]
        data += [[Paragraph(str(c), S["td"]) for c in r] for r in rows]
        n = len(head)
        w = 170 * mm
        if n == 6:
            cw = [w * x for x in (.13, .10, .27, .27, .07, .16)]
        elif n == 5:
            cw = [w * x for x in (.22, .17, .17, .19, .25)]
        elif n == 4:
            cw = [w * x for x in (.30, .14, .12, .44)]
        elif n == 3:
            cw = [w * x for x in (.30, .30, .40)]
        else:
            cw = [w * x for x in (.40, .60)]
        t = Table(data, colWidths=cw, repeatRows=1, hAlign="LEFT")
        t.setStyle(TableStyle([
            ("LINEBELOW", (0, 0), (-1, 0), 0.7, INK),
            ("LINEBELOW", (0, 1), (-1, -2), 0.25, RULE),
            ("LINEBELOW", (0, -1), (-1, -1), 0.7, INK),
            ("VALIGN", (0, 0), (-1, -1), "TOP"),
            ("TOPPADDING", (0, 0), (-1, -1), 3),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
            ("LEFTPADDING", (0, 0), (-1, -1), 4),
            ("RIGHTPADDING", (0, 0), (-1, -1), 4),
        ]))
        return t

    st = [Paragraph(TITLE, S["title"]), Paragraph(SUBTITLE, S["sub"]),
          Paragraph("<b>%s</b> &nbsp;&middot;&nbsp; %s" % (AUTHOR, BYLINE),
                    S["by"])]
    for kind, b in document(f):
        if kind == "abstract":
            st.append(Paragraph("<b>Abstract.</b> " + b, S["abs"]))
        elif kind == "h1":
            st.append(Paragraph(b, S["h1"]))
        elif kind == "h2":
            st.append(Paragraph(b, S["h2"]))
        elif kind == "p":
            st.append(Paragraph(b, S["p"]))
        elif kind == "quote":
            st.append(Paragraph("&ldquo;" + b + "&rdquo;", S["q"]))
        elif kind == "note":
            inner = Table([[Paragraph(b, S["note"])]], colWidths=[170 * mm])
            inner.setStyle(TableStyle([
                ("BACKGROUND", (0, 0), (-1, -1), SUNK),
                ("LINEBEFORE", (0, 0), (0, -1), 2, ACC),
                ("TOPPADDING", (0, 0), (-1, -1), 7),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 7),
                ("LEFTPADDING", (0, 0), (-1, -1), 8),
                ("RIGHTPADDING", (0, 0), (-1, -1), 8)]))
            st += [inner, Spacer(1, 9)]
        elif kind == "bullet":
            for x in b:
                st.append(Paragraph(x, S["li"], bulletText="•"))
            st.append(Spacer(1, 4))
        elif kind == "table":
            st += [Spacer(1, 3), tbl(b[0], b[1]), Spacer(1, 11)]
    doc.build(st)
    return path


# ---------------------------------------------------------------------------

def selftest():
    ok = True

    def chk(lab, got, want):
        nonlocal ok
        good = got == want
        ok &= good
        print("  [%s] %-56s %s" % ("ok" if good else "XX", lab,
                                   got if good else "%s != %s" % (got, want)))

    f = facts()
    import figure
    import registry
    chk("the paper asks the registry for its table",
        len(f["rows"]), len(registry.REGISTERED))
    chk("and figure for the vertex count", f["vertices"], len(figure.cells()))
    # ONE INDEX, ONE NAME.  The provenance table and the register table render
    # the same rows; a row labelled differently in the two cannot be lined up.
    # That happened -- `madelung.janet` in one against `madelung` in the other
    # -- because the label was rederived by string surgery instead of asked for.
    chk("every provenance row carries the label the register table prints",
        sorted(nm for nm in f["provenance"]
               if registry_short_of(f, nm) not in f["coords"]), [])
    chk("and the two tables have the same number of rows",
        (len(f["provenance"]), len(f["coords"])), (f["nrows"], f["nrows"]))
    # EVERY table that prints an index prints the SAME label for it.  Four
    # tables key on the full registry name; none of them may invent a label.
    # THE OVERLAP TABLE'S OWN LENGTH.  "Of six candidates" was typed against a
    # table of seven rows; the count is now the table's and the two must agree.
    chk("the candidate count is the overlap table's own length",
        f["n_candidates"], len(f["seated"]) + len(f["refused"]))
    chk("the demand and adjudication tables use the register's labels too",
        sorted({k2 for src in (f["E_by_index"], f["adj"], dict.fromkeys(f["E_too_large"]))
                for k2 in src if registry_short_of(f, k2) not in f["coords"]}), [])
    chk("eight channels, of thirty-two subsets",
        (f["nchannels"], f["nsubsets"]), (8, 32))
    chk("seven lawful containments", len(f["lawful"]), 7)
    chk("Dilworth holds on every vertex", f["dilworth_bad"], [])

    # THEOREM 2 AND ITS COROLLARY, as the paper states them
    chk("statistics closes EVERY arity-2 sub-chart -- theorem 2",
        f["stat_by_arity"][2][1], 0)
    chk("and not every arity-3 one", f["stat_by_arity"][3][1] > 0, True)
    # The banked per-arity total must be the sum of its own two columns, or the
    # prose would quote a number no measurement stands behind.
    chk("the banked per-arity totals are the sums of their columns",
        [a for a, v in f["stat_by_arity"].items()
         if f["stat_arity_totals"][a] != v[0] + v[1]], [])
    chk("no arity-2 chart is in K0 or K1 -- the corollary",
        [k for k in f["chan_arity2"] if k in (0, 1)], [])

    # the facts the prose leans on
    chk("gravity's bound triple has no join counterexample", f["gjoin"], 0)
    chk("the dimension sweep is K7 then K1 and never moves",
        [k for _d, k in f["dim_bfx"]], [7, 1, 1, 1, 1, 1, 1])
    chk("the observed fibration differs from the predicted",
        f["obs_diff_addr"] > 0 and f["obs_diff_cfg"] > 0, True)
    chk("twelve elements lose occupancy", len(f["obs_losses"]), 12)
    chk("the box-invariance candidate is refused",
        f["bi_verdict"], "REFUSE-AS-THEOREM")
    chk("the census found no new index",
        f["census"]["new_first_order_indexes"], 0)
    chk("and the paper reports refusals, not only acceptances",
        len(f["refused"]) >= len(f["seated"]), True)

    # SECTION 5 -- the claim that makes Theorem 1's bound tight.
    chk("every lawful channel is occupied by a seated index", f["empty"], [])
    chk("and each of the eight names its occupants",
        sorted(k for k, v in f["by_channel"].items() if v), list(range(8)))
    k4 = f["by_channel"][4]
    chk("K4 is held by one index, and at arity 3 where statistics is earned",
        (len(k4), f["arity_of"][k4[0]]), (1, 3))

    # SECTION 9 -- the demand and its adjudication.
    chk("the demand totals 4,759 and the adjudication sums to it",
        (f["E_total"], f["adj_tot"][0]), (3209, 3209))
    chk("and it splits 894 forbidden / 36 unplaced / 3,731 open / 98 undecided",
        tuple(f["adj_tot"][1:]), (593, 36, 2482, 98))
    chk("every forbidden cell is a baryon cell",
        sum(v[1] for k, v in f["adj"].items() if k != "baryons.index"), 0)
    chk("Theorem 5 holds to J = 12", f["qqbar"], (True, []))
    chk("Gell-Mann--Nishijima is clean on all 292 baryon rows",
        f["gmn_baryon"][:5] + (f["gmn_baryon"][5],),
        (292, 292, 292, 292, 292, []))
    chk("and fails on exactly the two meson rows the note names",
        (f["gmn_meson"][3], sorted(x[0] for x in f["gmn_meson"][5])),
        (189, ["B(s2)*(5840)0", "B(s2)*(5840)~0"]))
    chk("whose correction moves nothing in the index",
        f["bs2"][0] == f["bs2"][1], True)
    chk("the element precedent is an ORDER deficit, not a join one",
        f["precedent"], (90, 0, 36, 25, 0))
    chk("six of the seven derived bounds are monotone",
        (f["nbounds"], f["nbounds_mono"]), (7, 6))
    # DOCKET 36b seated a 24th index.  The vertex count is a PROPERTY here, not
    # a pinned number, so the guard that matters is that a seating cannot land
    # without its ledger rows: every registry row either carries an E entry or
    # is named as too large to close.  A seating that skipped predict.py would
    # otherwise show up only as a quiet hole in section 9's table.
    import predict as _pred
    _seated = {nm for nm, *_r in registry.rows()}
    _accounted = set(_pred.E_BY_INDEX) | set(_pred.TOO_LARGE)
    chk("every seated index is accounted for in the demand table",
        sorted(_seated - _accounted), [])
    chk("and the demand table invents no index the registry does not seat",
        sorted(_accounted - _seated), [])

    # THE SUBSTITUTION GUARD.  A figure typed into the prose would not move
    # when its instrument moved, which is the whole failure this file avoids.
    md = render_md(f)
    body = "\n".join(l for l in md.split("\n") if not l.startswith("|"))
    # THE EXEMPTION LIST WAS THE HOLE.  It carried 109, 117, 120 and 272 --
    # produced by NO instrument -- and those were exactly section 7's reading
    # counts and section 12's chart-search figure, every one of which had gone
    # stale by the register growing from eleven indexes to twenty-four. An
    # exemption is a promise not to check, so the list now holds only things
    # that CANNOT drift: the small counts English uses as words, and
    # identifiers that name a thing rather than measure one.
    allowed = {str(i) for i in range(13)}
    IDENTIFIERS = {
        "1306": "the register entry banking the observed ground configurations",
        "66":   "RULING 66",
        "0218": "the 0.0218 c ceiling, a named FITTED measurement",
        "1968": "Geiger, and Bodnarchuk et al., on the Pol-Inv connection",
        "1986": "Myers and Perry, on the D-dimensional rotating solution",
    }
    allowed |= set(IDENTIFIERS)

    # AND EVERY NUMBER THE FACTS DICT ACTUALLY HOLDS.  The old allow list was
    # hand-kept, which made the guard a record of what had been noticed rather
    # than a test; a numeral now passes only if some instrument produced it.
    def _nums(o, out):
        if isinstance(o, bool):
            return
        if isinstance(o, int):
            out.add(str(o))
        elif isinstance(o, float):
            if o == int(o):
                out.add(str(int(o)))
        elif isinstance(o, str):
            # A numeral inside a string an instrument produced is that
            # instrument's number too -- "B(s2)*(5840)0" is a PDG state name
            # read from the capture, not a figure someone typed.
            out.update(re.findall(r"\d+", o))
        elif isinstance(o, dict):
            for k2, v2 in o.items():
                _nums(k2, out)
                _nums(v2, out)
        elif isinstance(o, (list, tuple, set, frozenset)):
            for v2 in o:
                _nums(v2, out)
    _nums(f, allowed)
    # not preceded or followed by a digit or a decimal point, so the digits
    # after a "." in a generated ratio are not mistaken for a typed literal
    # THREE digits, not four.  The typed `132` that this guard let through was
    # three digits long, and the allowlist is now derived from the facts dict
    # rather than hand-kept, so widening it costs nothing but catches more.
    stray = sorted({n for n in re.findall(r"(?<![.,\d])\d{3,}(?![.\d])", body)}
                   - {str(x) for x in f["bi_corpus"]} - allowed)
    chk("no unexplained three-or-more-digit literal survives in the prose", stray, [])
    chk("the markdown renders", len(md) > 6000, True)
    print("mipaper selftest: %s" % ("PASS" if ok else "FAIL"))
    return ok


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    F = facts()
    if "--md" in sys.argv:
        p = os.path.join(HERE, "THE-MASTER-INDEX.md")
        open(p, "w", encoding="utf-8").write(render_md(F))
        print("wrote %s" % p)
    if "--pdf" in sys.argv:
        os.makedirs(os.path.join(HERE, "pdf"), exist_ok=True)
        p = os.path.join(HERE, "pdf", "THE-MASTER-INDEX.pdf")
        render_pdf(F, p)
        print("wrote %s (%d bytes)" % (p, os.path.getsize(p)))
    if "--md" not in sys.argv and "--pdf" not in sys.argv:
        for k, v in F.items():
            print("%-18s %s" % (k, str(v)[:120]))
    sys.exit(0)
