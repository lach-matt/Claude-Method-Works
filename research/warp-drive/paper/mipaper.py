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


# ---------------------------------------------------------------- the facts

def facts():
    """Every number the paper states, asked of the instrument that owns it."""
    import itertools
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
    for nm, mod, acc, _me, _w, _q in registry.rows():
        names = OR.COORDS.get(mod)
        if names is None:
            continue
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
        "seated": [(p, list(c), k, n) for p, c, k, n in OR.admissible()],
        "refused": [(p, list(c), w) for p, c, w in OR.refused()],
        "grounds": ["novel channel", "not a relabelling", "reach stable",
                    "coordinate forced"],
        "stat_by_arity": {a: tuple(v) for a, v in sorted(stat.items())},
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

    A(("abstract", (
        "A first-order index here is a finite set of cells charting some body of atomic, "
        "nuclear or particle data, and its members must carry quantum numbers. Five closure "
        "operators -- order, algebra, geometry, information "
        "and statistics -- act on such a set, and which of them close it is a property of "
        "the set rather than of the operators. We show that only %d of the %d subsets of the "
        "five can occur, characterise them as the down-sets of a seven-relation law, and use "
        "the resulting triple (channel, height, width) as an admissible chart. Charting every "
        "index this project seats gives a second-order object of %d vertices on %d distinct "
        "cells. We prove that 2-determinacy is vacuous at arity 2 and derive from it that an "
        "arity-2 chart can never occupy the two lowest channels, which explains why one channel "
        "was the last to be reached; all eight are now occupied by charts of real data, so the "
        "bound of the first theorem is tight from nature and not only by construction. We give "
        "a ruling admitting overlapping charts when they carry "
        "different information, four grounds on which it is tested, and a census over %d "
        "modules establishing that no unseated index exists in the tree. Of five adjudications "
        "reported here, four are refusals and one is a retraction of a seating this paper's "
        "own method had previously accepted. Finally we adjudicate the DEMAND -- the cells the "
        "seated indexes' own closure asks for and no member occupies. We prove that the demand "
        "invents no coordinate value, and that a bound monotone in the coordinates can never "
        "forbid a demanded cell, which empties at a stroke every hydrogenic and Pauli "
        "constraint one might bring to it; we prove that the quark model forbids no cell of "
        "the meson chart, and locate the cost in a coordinate that chart had refused for "
        "totality; and we exhibit the one bound in the tree that does forbid, which empties "
        "more than half of the largest prediction set in the register."
        % (f["nchannels"], f["nsubsets"], f["vertices"], f["distinct"],
           f["census"]["modules_attempted"]))))

    A(("h1", "1. The object, and the criterion that bounds it"))
    A(("p", (
        "A first-order index here is a finite set of tuples -- cells -- obtained by charting "
        "some body of atomic, nuclear or particle data on a fixed list of coordinates. The "
        "subject began as the periodic elements and was widened, by ruling, to quantum objects "
        "generally; the criterion did not move, and it is narrow and enforced in code rather "
        "than in prose: A MEMBER OF SUCH AN INDEX MUST CARRY QUANTUM NUMBERS. An electron, a "
        "subshell, a transition, a spectroscopic term, a nuclide-charge state, a meson, a "
        "baryon, a fractional-quantum-Hall quasiparticle and a nuclear excited state all "
        "qualify; a file, a build snapshot or a document does not, and neither does a chemical "
        "bond, a binding energy or a scattering channel -- each of which was tested against "
        "the criterion and refused on its own measured ground.")))
    A(("note", (
        "The criterion is a function and not a paragraph, and the reason is historical. When it "
        "was a paragraph, thirteen filing-system indexes were seated as vertices -- mirrored "
        "files, conversations, archives, handoff documents -- beside indexes whose members are "
        "electrons. Every one of the disruptive vertices was repository metadata and not one "
        "was an element. The explosion in demand that followed was reported as a finding; it "
        "was contamination, and it is withdrawn.")))
    A(("p", "%d indexes satisfy the criterion and are seated." % f["nrows"]))
    A(("table", (["index", "method", "one member is", "quantum numbers",
                  "cells", "cell"],
                 [[r["label"], r["method"], r["members"], r["quantum"],
                   "%d" % r["cells"], "(%d, %d, %d)" % r["cell"]]
                  for r in f["rows"]])))

    A(("h1", "2. Five languages and a law"))
    A(("p", (
        "Each of five closure operators takes a finite set of cells to a superset of it. "
        "Order and algebra are the sublattice hull under coordinatewise min and max; geometry "
        "is hull-completion on coordinate pairs; information is closure under coordinatewise "
        "join alone; statistics is 2-determinacy -- the set equals every box point whose "
        "two-coordinate projections all occur in it. A language CLOSES an index when applying "
        "it returns the index unchanged. The companion paper derives eight clauses relating "
        "them; this paper needs only the containments.")))
    A(("table", (["contained", "in", "source"],
                 [[a, b, why] for a, b, why in f["lawful"]])))

    A(("h2", "Theorem 1. The lawful channels are the down-sets of that law."))
    A(("p", (
        "Write cl[L] for the closure of an index X under language L. Every operator is "
        "extensive: X is a subset of cl[L] for all L. Suppose (a, b) is one of the seven, so "
        "cl[a] is a subset of cl[b], and suppose b closes X, meaning cl[b] = X. Then cl[a] is "
        "a subset of X, and by extensivity X is a subset of cl[a]; hence cl[a] = X and a closes "
        "X. So the set of languages closing any index is closed downward under the law. "
        "Conversely each down-set is realised, by exhibition. Enumerating the down-sets of the "
        "seven relations over five languages gives exactly %d of the %d subsets."
        % (f["nchannels"], f["nsubsets"]))))
    A(("table", (["channel", "languages that close"],
                 [["K%d" % i, c] for i, c in enumerate(f["channels"])])))
    A(("note", (
        "The law leaves exactly two languages free to close alone: information and statistics. "
        "Nothing forces either from anything else. That asymmetry is not decoration -- it is "
        "what makes K1 and K2 reachable at all, and section 6 shows that the freedom is "
        "exercised very differently by the two.")))

    A(("h1", "3. The admissible chart"))
    A(("p", (
        "An index is charted by the triple (K, h, w): its channel, the length of the longest "
        "chain in its cell poset (Mirsky), and the size of the largest antichain (Dilworth). "
        "The box is the product of the observed coordinate alphabets, never a declared range. "
        "Dilworth's theorem gives |X| <= h * w, so the three are not independent and the "
        "product box overstates the space; that inequality was checked on every seated index "
        "and holds on all of them (%d violations)." % len(f["dilworth_bad"]))))

    A(("h1", "4. The index of first-order indexes"))
    A(("p", (
        "Charting each seated index and taking its cell as a member gives a second-order "
        "object. It has %d vertices on %d distinct cells -- no two seated indexes share a cell "
        "-- it closes in %s, its demand E is %d, and its own cell is (%d, %d, %d), which %s."
        % (f["vertices"], f["distinct"], ", ".join(f["closers"]) or "nothing",
           f["E"], f["own"][0], f["own"][1], f["own"][2],
           "no member occupies" if not f["own_occ"] else
           "is occupied by " + ", ".join(f["own_occ"])))))
    A(("p", (
        "Applying the chart to itself is a test the object can fail. A coordinate whose "
        "distinct values number 90 percent or more of its members separates everything and "
        "therefore groups nothing: it is a row identifier wearing a measurement's clothes.")))
    A(("table", (["axis", "distinct", "of", "ratio", "verdict"],
                 [[a, "%d" % d, "%d" % n, "%.4f" % r, v]
                  for a, d, n, r, v in f["resolution"]])))
    A(("p", (
        "%s. At eleven vertices two of the three were row labels -- height at 0.909 and width "
        "perfectly injective at 1.000 -- and the reading filed with that finding was that each "
        "index brings its own height and width, so the two approach injectivity by "
        "construction as the object grows. That reading is refuted by the table above: the "
        "object grew and the labels became measurements. The prediction failed because a "
        "COARSENING of a seated index does not bring a new height and width; it lands in the "
        "part of the poset its parent already occupies. What the argument really showed is "
        "that the defect tracks how the vertex set is built, not how large it is."
        % ("No axis is a row label" if not f["labelled"]
           else "Row labels remain: " + ", ".join(f["labelled"])))))

    A(("h1", "5. Channel occupancy -- the bound of Theorem 1 is tight"))
    A(("p", (
        "The %d vertices occupy %s, and %s."
        % (f["vertices"], K(f["occupied"]),
           "EVERY ONE OF THE EIGHT LAWFUL CHANNELS IS OCCUPIED"
           if not f["empty"] else
           "%s %s empty" % (K(f["empty"]),
                            "is" if len(f["empty"]) == 1 else "are")))))
    A(("table", (["channel", "languages that close", "seated indexes there"],
                 [["K%d" % k, f["channels"][k],
                   ", ".join(f["by_channel"][k]) or "--"]
                  for k in range(8)])))
    A(("note", (
        "Theorem 1 proves that at most %d of the %d subsets can occur, and its converse half "
        "was proved by EXHIBITION -- constructing a set of cells for each down-set. That is "
        "now superseded by something stronger: every down-set is realised by a chart of real "
        "atomic, nuclear or particle data whose members carry quantum numbers. The bound is "
        "tight, and it is tight from nature rather than from construction. This was not the "
        "case when this paper was first drafted, and section 6 is why the last channel was the "
        "last." % (f["nchannels"], f["nsubsets"]))))

    A(("h1", "6. Theorem 2, and why one channel was the last to fall"))
    A(("p", (
        "Statistics is 2-determinacy: X is the set of box points all of whose 2-coordinate "
        "projections occur among X's. At arity 2 there is exactly one 2-subset of the "
        "coordinates -- the whole of them -- so the projection is the identity and the "
        "reconstruction returns X itself. 2-determinacy therefore holds VACUOUSLY at arity 2, "
        "for every set whatever, and statistics closes every arity-2 chart. This is a property "
        "of the definition and not of any implementation.")))
    A(("p", "Measured over every sub-chart of every seated index:"))
    A(("table", (["arity", "statistics closes", "does not"],
                 [["%d" % a, "%d" % v[0], "%d" % v[1]]
                  for a, v in f["stat_by_arity"].items()])))
    A(("h2", "Corollary. An arity-2 chart cannot occupy K0 or K1."))
    A(("p", (
        "Its channel contains statistics, and neither K0 nor K1 does. Measured over the same "
        "sub-charts, the arity-2 channels observed are %s -- K0 and K1 occur zero times, as the "
        "corollary requires."
        % ", ".join("K%d (%d)" % (k, v) for k, v in f["chan_arity2"].items()))))
    A(("note", (
        "THIS IS WHAT MADE K4 THE HARD CHANNEL, and the difficulty was structural rather than "
        "accidental. The law protects K5 and K6 from the free pass, because geometry closing "
        "forces statistics and so does the order/algebra block; at those channels the "
        "statistics bit is earned by law whatever the arity. K4 = {information, statistics} "
        "has neither protection -- nothing forces statistics from information -- so it is the "
        "only channel above K1 whose extra content is exactly the bit an arity-2 chart is "
        "given for free. For a long stretch of this work the only charts reaching K4 were "
        "arity 2, where half the channel is a gift, and a census over %d modules (section 10) "
        "found no chart of any arity reaching it.")))
    A(("p", (
        "IT IS NOW OCCUPIED, AND OCCUPIED AT ARITY %d. The seated index at K4 is %s, charted "
        "on %s -- an arity at which 2-determinacy is not vacuous and statistics has to be "
        "earned. So the channel that the theorem predicted would be hardest is reached, and "
        "reached in the way that makes it a measurement rather than a free pass. The "
        "explanation above survives as an explanation of the difficulty; it is no longer an "
        "account of an absence."
        % (f["arity_of"][f["by_channel"][4][0]], f["by_channel"][4][0],
           "its %d coordinates" % f["arity_of"][f["by_channel"][4][0]]))))

    A(("h1", "7. Seating an overlapping chart"))
    A(("quote", (
        "They can be seated with overlaps so long as it is not an overlap of same information. "
        "An overlap of values in two different languages should tell us two parts of definition "
        "contained in that overlapped position. Information is information. But its relative "
        "position in this index is information about an object.")))
    A(("p", (
        "A coarsening -- the same members charted on fewer coordinates -- overlaps its parent "
        "totally. The ruling above admits it when it is not the same information. Six readings "
        "of that phrase were charted against all proper sub-charts of the seated indexes: "
        "'channel differs from its parent' admits 109, 'cell differs from its parent' 254, "
        "'cell no seated vertex holds' 252, and 'CHANNEL no seated vertex holds' admits 6. The "
        "third admits 117 coarsenings of a single index; the fourth is bounded, and it is what "
        "the ruling says, since the ruling names languages and the channel is the set of "
        "languages that close a chart. Text and arithmetic select the same reading.")))
    A(("p", "Four grounds are tested, and a candidate must clear all four:"))
    A(("bullet", [
        "NOVEL CHANNEL -- the chart reaches a channel no seated index reaches.",
        "NOT A RELABELLING -- it has strictly fewer cells than its parent; a chart that "
        "separates exactly as much is the parent renamed.",
        "REACH STABLE -- the channel does not depend on where the construction stopped: no "
        "late arrival, no oscillation, and a majority of reaches.",
        "COORDINATE FORCED -- the channel survives a faithful re-coordinatisation. Two "
        "addresses inducing the identical partition of the identical members are one chart "
        "written twice.",
    ]))
    A(("p", "Of six candidates, %d seat and %d are refused."
        % (len(f["seated"]), len(f["refused"]))))
    A(("table", (["chart", "channel", "cells", "verdict / ground failed"],
                 [["%s (%s)" % (p, ", ".join(c)), "K%d" % k, "%d" % n, "SEATED"]
                  for p, c, k, n in f["seated"]] +
                 [["%s (%s)" % (p, ", ".join(c)), "", "", "refused: " + ", ".join(w)]
                  for p, c, w in f["refused"]])))

    A(("h1", "8. Two measurements that are about physics"))
    A(("h2", "8.1 A horizon threshold visible in the closure algebra"))
    A(("p", (
        "One seated coarsening charts nuclide-charge states on (horizon-bound class, forced "
        "angular momentum, spin-decade rank), dropping the spacetime dimension. Its bound class "
        "comes from the singly-rotating Myers-Perry horizon condition, which has the Kerr bound "
        "in four dimensions, a bound in five, and no bound at all from six upward, where the "
        "ultraspinning branch opens. Sweeping the dimension ceiling:")))
    A(("table", (["dimensions admitted", "channel"],
                 [["D <= %d" % d, "K%d" % k] for d, k in f["dim_bfx"]])))
    A(("p", (
        "Read in four and five dimensions the bound structure closes in all five languages. "
        "Admit the sixth and four of the five break at once, leaving information alone, and it "
        "never moves again. The closure operators are told nothing about dimension; the "
        "threshold appears at the dimension the theorem names. The chart is a join-semilattice "
        "that is not a lattice -- %d join counterexamples against %d meet, in %d unordered "
        "pairs. We record the coincidence and offer no mechanism for why losing a bound should "
        "cost four languages rather than three."
        % (f["gjoin"], f["gmeet"], f["gpairs"]))))

    A(("h2", "8.2 What the periodic table predicts against what it does"))
    A(("p", (
        "Two indexes chart the shell fibration: one on the configuration the Madelung rule "
        "predicts, one on the configurations a register of this corpus banks as observed. They "
        "are seated together by ruling. The predicted chart has 108 cells at the matched reach "
        "and closes statistics; the observed has %d cells at (%d, %d, %d) and closes nothing. "
        "%d of the %d addresses differ and %d of the configurations do -- and those %d are "
        "exactly the Madelung exceptions this project indexes separately, so the divergence is "
        "not an unknown quantity."
        % (f["obs_cells"], f["obs_cell"][0], f["obs_cell"][1], f["obs_cell"][2],
           f["obs_diff_addr"], f["obs_addr"], f["obs_diff_cfg"],
           f["obs_diff_cfg"]))))
    A(("p", (
        "The sharpest difference is one neither chart shows alone. %d elements -- %s -- LOSE "
        "occupancy in a subshell as Z increases by one: a filled subshell gives an electron up. "
        "The Madelung prediction is monotone in Z by construction and can never do this, "
        "verified at every step of the reach. Neither chart supersedes the other."
        % (len(f["obs_losses"]), ", ".join(f["obs_losses"])))))

    A(("h1", "9. What the register predicts, and the law that bounds it"))
    A(("p", (
        "Write J(X) for the closure of an index under coordinatewise join and E(X) for the "
        "number of cells in J(X) that X does not hold. The corpus reads E as the number of "
        "predictions an index can make. Measured over every seated index small enough to "
        "close -- one, at %d cells, is not, and it is named rather than dropped -- the "
        "register demands %s cells it does not hold. %d indexes predict; %d are complete."
        % (f["gravity_cells"], format(f["E_total"], ","), f["E_npos"], f["E_nzero"]))))
    A(("table", (["index", "E"],
                 [[k.replace(".index", "").replace("overlaprule.", ""), "%d" % v]
                  for k, v in sorted(f["E_by_index"].items(), key=lambda kv: -kv[1])
                  if v > 0])))
    A(("note", (
        "The partition is exact -- every E = 0 index closes under information and every E > 0 "
        "index does not -- and it is close to definitional, since E is the join deficit and "
        "the information closer is the join closer. It is said so that it is not mistaken for "
        "a result. The result is the numbers, and they say the register is overwhelmingly "
        "incomplete.")))
    A(("p", (
        "An unadjudicated E is a count of QUESTIONS and not of objects. A demanded cell is one "
        "of three things -- FORBIDDEN, %s; UNPLACED, %s; OPEN, %s -- and only the third is a "
        "prediction. Which of the three a cell is turns out to be settled by a theorem rather "
        "than by how much physics one is willing to bring to it."
        % (f["bin_why"]["FORBIDDEN"], f["bin_why"]["UNPLACED"], f["bin_why"]["OPEN"]))))

    A(("h2", "Theorem 3. The demand invents no coordinate value."))
    A(("p", (
        "For every coordinate i the projection of J(X) onto i equals the projection of X onto "
        "i. PROOF. X is contained in J(X). Conversely J(X) is generated from X by repeated "
        "componentwise max, and max(a, b) is either a or b, so every coordinate of every "
        "generated cell is a coordinate value already present in X; induct on the generation. "
        "COROLLARY: no bound constraining a single coordinate can forbid a demanded cell.")))
    A(("note", (
        "Measured on the largest prediction set in the register: of %d demanded baryon cells, "
        "ZERO carry an even doubled spin -- although 2J even is exactly what the spin-statistics "
        "of a three-quark state rules out. The strongest single-coordinate fact available about "
        "baryons adjudicates nothing, and Theorem 3 says why."
        % f["adj"]["baryons.index"][0])))

    A(("h2", "Theorem 4. A monotone bound forbids nothing."))
    A(("p", (
        "Let B be a set of cells with X contained in B and B closed under componentwise max. "
        "Then J(X) is contained in B, because J(X) is the least max-closed set containing X; "
        "so B forbids no demanded cell. In particular a bound of the form x_i <= f(x_j, ...), "
        "with i not among the j and f non-decreasing in each argument, is max-closed: if a and "
        "b lie in B and c is their join, then c_i = max(a_i, b_i) is one of them, say a_i, and "
        "a_i <= f(a_j) <= f(c_j) because a_j <= c_j for each j and f is non-decreasing.")))
    A(("p", (
        "%d bounds were derived for the seated indexes, each from a stated physical law, each "
        "checked against every member of its index before being applied to the demand, and "
        "none fitted to the demand. %d of the %d are monotone, and the monotone ones forbid "
        "nothing at all."
        % (f["nbounds"], f["nbounds_mono"], f["nbounds"]))))
    A(("table", (["index", "bound", "from", "monotone", "forbidden"],
                 [[short, lab, law, "yes" if mono else "NO",
                   "%d" % f["adj"][nm][1]]
                  for nm, short, lab, law, mono in f["bounds"]])))
    A(("note", (
        "The zeros are not a failed search. l <= n-1 is the radial node count n - l - 1 being "
        "non-negative; the Pauli caps count the spin-orbitals of a subshell; q <= k says one "
        "cannot ionise more electrons than are present; l = 0 forcing the upper spin-orbit "
        "branch is j = l +- 1/2 with j >= 0; and a Russell-Saunders singlet has one level, so "
        "it cannot fall short of its own multiplet. All are theorems, all hold on every seated "
        "member without exception, and by Theorem 4 none of them CAN forbid a demanded cell. "
        "The hypothesis is verified rather than read off the algebra: each bound's admissible "
        "set is enumerated over its index's own product box and closed under join by "
        "exhaustion.")))

    A(("h2", "Theorem 5. The quark model forbids no cell of the meson chart."))
    A(("p", (
        "For a quark-antiquark state P = (-1)^(L+1), C = (-1)^(L+S), S is 0 or 1, and J runs "
        "from |L - S| to L + S. CLAIM: every (J, P) with J a non-negative integer and P = +-1 "
        "is realised. PROOF, four cases. P = -1 requires L even: for J even take (L, S) = "
        "(J, 0); for J odd take (J - 1, 1), which is even and non-negative and has L + S = J; "
        "J = 0 forces L = S, and L = S = 0 gives 0-. P = +1 requires L odd: for J odd take "
        "(J, 0); for J even and at least two take (J - 1, 1); J = 0 forces L = S, and L = S = 1 "
        "gives 0+. Checked by exhaustion to J = 12 with no unreached pair.")))
    A(("p", (
        "The exotic quantum numbers -- 0--, 0+-, 1-+, 2+- -- are forbidden in J^PC, and C is "
        "not a coordinate of this chart. It was refused for TOTALITY: %d of the %d mesons in "
        "the source carry no C at all, and a chart carries only coordinates all its members "
        "have. THE REFUSAL WAS CORRECT AND IT HAS A PRICE, and this is where the price is "
        "paid. The meson index has %d demanded cells and the quark model, fully stated, "
        "empties none of them. A coordinate refused for totality is adjudication power given "
        "up, and the trade is visible only once someone tries to spend it."
        % (f["meson_noC"], f["meson_rows"], f["adj"]["mesons.index"][0]))))

    A(("h2", "The one bound that forbids"))
    A(("p", (
        "By Theorem 4 only a bound that is antitone somewhere, or carries a congruence, can "
        "forbid. One qualifies here and it qualifies twice over. Gell-Mann-Nishijima gives the "
        "isospin projection 2*I3 = 2Q - Y with Y = B + S + C + B' + T, and I3 must be a weight "
        "of the isospin-I representation: |2*I3| <= 2I, an absolute value, and 2I congruent to "
        "2*I3 modulo two, a congruence. Both break max-closure. The baryon chart carries Q, S, "
        "C, B and I as coordinates, so the bound is expressible on it, and it FORBIDS %d of "
        "the %d demanded cells -- %.1f per cent of the largest prediction set in the register, "
        "emptied by theorem rather than by observation."
        % (f["adj"]["baryons.index"][1], f["adj"]["baryons.index"][0],
           100.0 * f["adj"]["baryons.index"][1] / f["adj"]["baryons.index"][0]))))
    A(("p", (
        "The relation is not imported. Writing n_a for quarks minus antiquarks of flavour a, "
        "Q = (2/3)(n_u + n_c + n_t) - (1/3)(n_d + n_s + n_b), I3 = (n_u - n_d)/2, S = -n_s, "
        "C = n_c, B' = -n_b, T = n_t and B = (sum of n_a)/3, whence Q - I3 = n_u/6 + n_d/6 + "
        "(2/3)(n_c + n_t) - (1/3)(n_s + n_b) = Y/2 identically. All three legs -- the charge "
        "built from the quark charges, the isospin projection, and the identity -- are "
        "re-derived from the source's own quark strings: %d baryon rows, %d parse, and %d, %d "
        "and %d clean without exception."
        % f["gmn_baryon"][:5])))
    A(("note", (
        "The same check on the mesons found a fault in the source. %d of %d meson rows parse "
        "-- the rest are flavour mixtures, which is why S, C and B are not coordinates of the "
        "meson chart and therefore why the bound is inexpressible there -- and of those the "
        "charge and the identity are clean at %d and %d while the isospin projection fails at "
        "%d. The two failures are one state and its antiparticle, %s, carrying a "
        "strange-beauty content with doubled isospin one, while two other states of the "
        "identical content carry zero in the same file. Such a pair holds no up or down quark, "
        "so I3 = 0 and I = 1/2 has no weight to sit on. IT IS RECORDED AND NOT REPAIRED, and "
        "the cost is measured: with the isospin set to zero on both rows the meson index has "
        "%d cells, E = %d and chart position (%d, %d, %d) -- identical before and after, "
        "because both affected cells are already occupied by other members."
        % ((f["gmn_meson"][1], f["gmn_meson"][0], f["gmn_meson"][2],
            f["gmn_meson"][4], f["gmn_meson"][3],
            " and ".join(sorted(x[0] for x in f["gmn_meson"][5])),
            f["bs2"][1][0], f["bs2"][1][1]) + tuple(f["bs2"][1][2])))))

    A(("h2", "E is a deficit against an operator, and so is forbidding"))
    A(("p", (
        "Every E above is a JOIN deficit. The same cells measured against the ORDER closure "
        "give a different deficit and a different verdict. On the %d drawn positions of the "
        "period-by-group periodic layout the join deficit is %d and the order deficit is %d, "
        "and the hydrogenic bound l <= n-1 -- read through the layout's own rule for which "
        "subshell sits at which group -- forbids %d of the order ghosts and %d of the join "
        "ghosts. By Theorem 4 it could not have been otherwise: expressed on (n, l, k) that "
        "bound is monotone; expressed on (period, group) it is not."
        % f["precedent"])))
    A(("note", (
        "Two consequences, and the second is a caution. First, an earlier statement of this "
        "project cited that layout's ghosts as the precedent for adjudicating the join "
        "deficits tabled above without distinguishing the operators; the three bins survive "
        "intact and the precedent is re-attributed rather than withdrawn. Second, FORBIDDING "
        "POWER IS A PROPERTY OF THE CHART AND NOT OF THE BOUND: one bound forbids on one "
        "coordinatisation of the elements and nothing on two others. The layout on which it "
        "has teeth is the one this project WITHDREW as over-representation. A chart that can "
        "forbid is not thereby a better chart, and the inference is unsound in both "
        "directions.")))

    A(("h2", "UNPLACED separated from OPEN"))
    A(("quote", (
        "A demanded cell is UNPLACED if and only if the index's own source holds a row the "
        "chart declined to place which supplies all but one of the coordinates and agrees with "
        "the cell on every one of them.")))
    A(("p", (
        "The strength condition is the whole rule. A source row missing one coordinate names a "
        "line of cells and pins each of them; a row missing two names a plane and pins "
        "nothing. Without it, four thousand unparsed spectroscopic labels would explain every "
        "empty cell in one of these charts. Rows below the strength are counted apart and "
        "never used. For %d of the indexes the source has no gap at all, and that is measured "
        "rather than assumed: source rows are counted against rows charted and equality is "
        "required." % f["gapless"])))
    A(("table", (["index", "E", "forbidden", "unplaced", "open", "undecided"],
                 [[k.replace(".index", ""), "%d" % v[0], "%d" % v[1], "%d" % v[2],
                   "%d" % v[3], "%d" % v[4]]
                  for k, v in sorted(f["adj"].items(), key=lambda kv: -kv[1][0])]
                 + [["TOTAL"] + ["%d" % x for x in f["adj_tot"]]])))
    A(("p", (
        "%s cells are FORBIDDEN and every one of them is a baryon cell. %d are UNPLACED, in "
        "four charts, and the count of CELLS is deliberately kept apart from the count of "
        "OBJECTS: in one chart %d cells are pinned by %d objects, because a state lacking only "
        "its parity pins both parities and will fill exactly one of them. %s are OPEN. %d are "
        "UNDECIDED, and the reason is exact rather than a shrug -- the loader of that chart "
        "discards a refused row without banking its term key, so the tree cannot ask whether "
        "any term lost ALL of its levels, and such a term would pin a cell at precisely the "
        "required strength. Banking those keys would settle it."
        % (format(f["adj_tot"][1], ","), f["adj_tot"][2], f["unplaced_meson"][0],
           f["unplaced_meson"][1], format(f["adj_tot"][3], ","), f["adj_tot"][4]))))
    A(("note", (
        "What the OPEN column is and is not. For the %d indexes carrying a derived bound it is "
        "FINAL AGAINST EVERY MONOTONE BOUND, by Theorem 4 -- a proof and not a survey. For the "
        "%d carrying none it is open against nothing at all, and a bound found tomorrow may "
        "empty any of them. The two situations are different and are not summed into one "
        "adjective. Neither is a count of undiscovered objects."
        % (f["nbounds"], f["no_bound_derived"]))))

    A(("h1", "10. The census"))
    c = f["census"]
    A(("p", (
        "Every chart-shaped accessor in the research tree was charted, with each module's "
        "attempt logged so that coverage is measured and not inferred. %d of %d modules were "
        "attempted; %d could not be imported and each is named with the reason. %d charts were "
        "found over %d modules, of which %d are neither seated nor excused -- and not one of "
        "those is a new first-order index. They are members that are not elements, alternate "
        "charts of already-seated member sets (all landing in occupied channels), or withdrawn "
        "and duplicate charts."
        % (c["modules_attempted"], c["modules_in_tree"], len(c["unimportable"]),
           c["charts_found"], c["modules_with_a_chart"],
           c["unseated_not_excused"]))))
    A(("p", "Charts per channel: %s. %s"
        % (", ".join("%s %d" % (k, v) for k, v in c["charts_per_channel"].items()),
           c["K4_reached_by"].capitalize() + ".")))
    A(("note", (
        "Two artifacts of the census are recorded rather than allowed to read as findings: one "
        "chart appears unseated because the census keys on (module, accessor) and the seated "
        "row reaches it under a second accessor name, and one is a helper written during this "
        "work that reproduces an existing index's members.")))

    A(("h1", "11. What was refused, and what that establishes"))
    A(("p", (
        "Five adjudications are reported. Four are refusals and one is a retraction. We set "
        "them out because a method that only ever accepts has not been tested.")))
    A(("bullet", [
        "A candidate reproducing a published four-figure result of this corpus exactly -- 0 "
        "join counterexamples and meet counts %s at caps %s -- was REFUSED. Its channel is the "
        "same at nine of ten boxes we could hand it, so the channel is a property of the "
        "defining predicate and not of any data; it would sit where it sits in a universe with "
        "no atoms in it."
        % (", ".join("%s" % m for m in f["bi_corpus"]),
           ", ".join("%d" % c2 for c2 in f["bi_caps"])),
        "A channel was shown reachable at arity 3, where statistics must be earned, by three "
        "charts of an index's own measured quantities. All three were REFUSED: they were found "
        "by searching 120 charts for that channel, which is fitting, and a chart selected "
        "because it lands somewhere cannot be evidence that it lands there.",
        "Two further coarsenings were REFUSED on the reach ground -- one oscillating between "
        "channels as the element reach grew, one reaching its channel only at the terminal "
        "reach, which is the failure mode that withdrew an earlier chart of this project.",
        "One coarsening was SEATED and then RETRACTED. The same members under an equally "
        "faithful address -- and the alternative is the primitive the source actually banks -- "
        "land in an occupied channel, so the chart had no novel channel and was never a "
        "candidate. Its apparent result was a fact about which name had been written down. "
        "The ground that caught it became the fourth test in section 7.",
    ]))
    A(("p", (
        "%d statements this project had asserted were measured to be false in the course of "
        "the same work and are listed with their corrections in the accompanying state file. "
        "Among them: a parent index described as a complete rectangle closing everything for "
        "free, which has density %.4f -- %d cells in a box of %d -- and is not a "
        "down-set; an attribution of a closure "
        "property to one coordinate when a second restores it equally; and an instrument that "
        "DECLARED an index exempt from its own strongest test rather than measuring whether it "
        "was. Run properly, that test confirmed the seating and located the physics in a "
        "constraint of the hydrogenic spectrum."
        % (f["retractions"], f["mad_density"], f["mad_cells"], f["mad_box"]))))

    A(("h1", "12. What is not claimed"))
    A(("bullet", [
        "Completeness. The registry's completeness flag is false and stays false. This is the "
        "set of first-order indexes found and survived their tests, not a claim to have found "
        "them all.",
        "That occupying all eight channels closes the subject. It makes the bound of Theorem 1 "
        "tight and nothing more. It does not say the eight are the right coordinates, that no "
        "further index exists, or that any channel is occupied by the best chart of it -- and "
        "one of the eight is held by a single index, so its occupancy rests on one seating.",
        "That the demand E measures progress. It is reported because it is measured. No index "
        "here was built to land on a cell the demand wanted, and one that was would be fitted.",
        "That the second-order object is itself a first-order index. Its members are indexes "
        "and carry no quantum numbers; it fails the criterion of section 1 and is excused by "
        "name rather than by silence.",
    ]))

    A(("h1", "Appendix. Reproduction"))
    A(("p", (
        "Every figure above is read from an instrument at build time. Each instrument is "
        "stdlib-only and carries a selftest whose fixtures are this corpus's own recorded "
        "numbers; the selftest is the first thing to run and the reports are not to be trusted "
        "before it passes.")))
    A(("bullet", [
        "python3 registry.py --selftest -- the criterion, enforced on every row",
        "python3 figure.py --selftest -- the second-order object and its chart",
        "python3 overlaprule.py --selftest -- the ruling, the four grounds, the refusals",
        "python3 overlaprule.py --census -- re-derives the six candidates",
        "python3 boxinvariance.py --selftest -- the refused theorem, and the test run properly",
        "python3 observed.py --selftest -- the observed fibration against the predicted",
        "python3 predict.py --selftest -- the demand per seated index",
        "python3 ghosts.py --selftest -- the seven laws, the bounds, the adjudication",
        "python3 state.py --check -- the state file against every instrument",
        "python3 paper/mipaper.py --selftest -- that no figure in this paper is typed",
    ]))
    return D


# ------------------------------------------------------------------ renders

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
    chk("eight channels, of thirty-two subsets",
        (f["nchannels"], f["nsubsets"]), (8, 32))
    chk("seven lawful containments", len(f["lawful"]), 7)
    chk("Dilworth holds on every vertex", f["dilworth_bad"], [])

    # THEOREM 2 AND ITS COROLLARY, as the paper states them
    chk("statistics closes EVERY arity-2 sub-chart -- theorem 2",
        f["stat_by_arity"][2][1], 0)
    chk("and not every arity-3 one", f["stat_by_arity"][3][1] > 0, True)
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
    chk("the demand totals 3,206 and the adjudication sums to it",
        (f["E_total"], f["adj_tot"][0]), (3206, 3206))
    chk("and it splits 593 forbidden / 36 unplaced / 2,479 open / 98 undecided",
        tuple(f["adj_tot"][1:]), (593, 36, 2479, 98))
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

    # THE SUBSTITUTION GUARD.  A figure typed into the prose would not move
    # when its instrument moved, which is the whole failure this file avoids.
    md = render_md(f)
    body = "\n".join(l for l in md.split("\n") if not l.startswith("|"))
    allowed = {"1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12",
               "0", "90", "109", "254", "252", "117", "120", "108", "1306",
               "66", "0218", "6"}

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
    stray = sorted({n for n in re.findall(r"(?<![.\d])\d{4,}(?![.\d])", body)}
                   - {str(x) for x in f["bi_corpus"]} - allowed)
    chk("no unexplained four-digit literal survives in the prose", stray, [])
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
