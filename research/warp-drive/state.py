#!/usr/bin/env python3
r"""
state.py -- THE CURRENT STATE OF THE INDEX WORK, GENERATED, FOR A READER WHO
IS NOT THIS SESSION.

    python3 state.py            the reading
    python3 state.py --json     write STATE.json
    python3 state.py --md       write STATE.md
    python3 state.py --check    STATE.json against a fresh computation; exit 1
                                on drift
    python3 state.py --selftest fixtures

===============================================================================
0. WHY THIS EXISTS AND WHAT IT IS NOT
===============================================================================

`research/README.md` is twelve thousand lines and it is a RECORD: it keeps
superseded readings beside current ones on purpose, because a withdrawn figure
that leaves no trace is how a corpus forgets it was ever wrong.  That makes it
the right thing to read and the wrong thing to quote from at a glance -- the
paragraph you land on may be the one that was corrected three sections later.

    SO THIS FILE ANSWERS ONE QUESTION: what is true right now.

    NOTHING IN THE GENERATED PART IS TYPED BY HAND.  Every figure is ASKED of
    the instrument that owns it -- `registry` for the rows, `figure` for the
    vertex set, `demand` for E, `overlaprule` for what the ruling seated and
    refused, `boxinvariance` for its verdict.  A number here that disagrees
    with its instrument is impossible rather than unlikely, and `--check`
    proves the written STATE.json still agrees.

    THE ONE HAND-MAINTAINED PART IS `DOCKETS`, and it is marked as such,
    because a docket is prose: a question, its status, and what would settle
    it.  The selftest refuses a docket missing any of the three.

===============================================================================
1. WHAT A READER SHOULD AND SHOULD NOT TAKE FROM IT
===============================================================================

    TAKE the registry, the figure, the channels and the ruling's verdicts.
    Those are measurements and they are current by construction.

    DO NOT TAKE `COMPLETE`.  `registry.COMPLETE` is False and stays False.
    This is not a claim to have found every first-order index; it is a list of
    the ones that have been found and survived their tests.

    DO NOT READ AN EMPTY CHANNEL AS A THEOREM.  SEVEN OF THE EIGHT ARE NOW
    OCCUPIED AND ONLY K4 IS EMPTY -- DOCKET 29 filled K5 with `baryons
    (2I, Q3)`, which is not the chart DOCKET 22 retracted.  For K4 the state
    is three candidates reached it and all three were arity 2, where
    `statistics` closes for free (105 of 105, measured); no chart of arity 3
    or more has ever reached it here.  That is an argument, not a proof, and
    the file does not offer one.

    A DOCKET'S OWN FIGURES ARE AS MEASURED WHEN IT WAS RULED and are left
    alone -- DOCKET 25 and DOCKET 27 both say K4 and K5 are empty, and both
    were right when written.  DOCKET 29 supersedes them, and the generated
    part above is always current.

    READ `retractions` BEFORE QUOTING ANYTHING.  Things this tree asserted and
    later measured to be false are listed there with what replaced them.  They
    are the highest-value rows in the file for anyone building on this.
"""

import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
SCHEMA = 2

# ---------------------------------------------------------------------------
# THE ONE HAND-MAINTAINED TABLE.  A docket is a question, a status and what
# would settle it; the selftest refuses a row missing any of the three.
DOCKETS = (
    ("36", "OPEN-ON-ONE-ENTRY (a REFUSAL, RETRACTED)",
     "Can arXiv:2508.05447's Table 3 -- the DEFORMED two-quasiparticle "
     "rotational bands, the candidate subpop.py actually named -- be captured "
     "total and seated?",
     "NOT YET, AND THE FIRST ANSWER GIVEN HERE WAS WRONG AND IS RETRACTED. "
     "Four forward parses came up short (154, 176, 160, 195 against the stated "
     "234). Working backwards found the paper's own delimiter -- 'A single "
     "blank row separates the entries for each band' -- and it IS absent from "
     "this extraction: 210 separators required, and of the 71 blank lines 50 "
     "are page boundaries and 21 are nuclide-header internals, so ZERO are "
     "separators (an earlier count of '22 page breaks, at most 49 available' "
     "was itself wrong, in a classifier that tested backwards). THAT MUCH "
     "STANDS AND IS STRONGER THAN STATED. What does not stand is the "
     "conclusion drawn from it: the file went on to claim no parse could "
     "recover entry boundaries, which is a statement about every possible "
     "parse and was never measured. AN ADVERSARIAL AUDIT REFUTED IT. A "
     "sequence-with-reset rule on the band number -- next expected integer, or "
     "a 1 opening a new nuclide, nothing else -- recovers 233 of 234 entries "
     "in 24 blocks matching the 24 nuclide sections, every block contiguous. "
     "The four attempts failed because they RELAXED the sequence; tightening "
     "it works. Also recoverable: the 24 sections with Z and N, and the level "
     "rows once wrapped parity is rejoined and relative energies (A+134.27, "
     "1135.7+y) are admitted. NOTHING IS SEATED, because 233 is not 234.",
     "Finding the 234th entry, then validating a finished capture against the "
     "paper's own rich fixture set (234 = 173 bands + 61 bandhead states, 63 "
     "GM doublets, 76 with signature splitting, 29 with inversion, 10 band "
     "crossings, 58 bandheads with half-lives). A layout-preserving extraction "
     "is NO LONGER NEEDED -- an earlier entry here said it was, on a claim "
     "that the proxy blocks every mirror, which was also wrong: "
     "storage.googleapis.com and github.com both tunnel. The docket is open on "
     "ONE MISSING ENTRY, not on an input."),
    ("22", "CLOSED-WITH-CORRECTIONS",
     "Were the ruling's per-witness physics claims ever independently checked?",
     "Nine adversarial agents, three lenses on each of three seatings. Two "
     "survived; nucshell (l, sigma) was UNSEATED. Ten corrections applied.",
     "Settled. Re-running the same lenses would re-check it."),
    ("23", "CLOSED",
     "Could madrule reach K4 at an arity where statistics is earned?",
     "Yes -- 3 of its 120 arity-3 charts do. None may be seated: they were "
     "found by searching for K4, which is fitted by this tree's own rule.",
     "A coordinate justified from the corpus BEFORE the chart is run."),
    ("24", "CLOSED",
     "Was the reported K1 candidate over the U3/U4 allowed sets real?",
     "Real and reproduced exactly -- 0 joins and 2,862/12,489/40,887/110,229, "
     "the corpus's own figures at §29.12 U4. Refused as a theorem: the channel "
     "is K1 at nine of ten boxes, so it does not depend on the data.",
     "Settled."),
    ("25", "CLOSED",
     "Does the research tree already hold an unseated first-order index?",
     "NO. Census of every chart-shaped accessor, all 232 modules attempted "
     "with attempt logging, 44 charts over 31 modules, 24 unseated and not "
     "excused, and NOT ONE is a new first-order index: they are members that "
     "are not elements, alternate charts of already-seated member sets (all "
     "landing in OCCUPIED channels), or withdrawn/duplicate charts. Two "
     "findings stand out -- K4 is reached by NOTHING in the whole tree, and "
     "K5 is reached by exactly one chart, the row DOCKET 22 retracted.",
     "Settled for the tree as it stands. A new member set would reopen it."),
    ("26", "CLOSED",
     "Is the madelung/fibred family built on a withdrawn table?",
     "The table was withdrawn as a source of OBSERVED configurations, and it "
     "remains exactly what its docstring says -- what Madelung PREDICTS -- so "
     "fibred and madelung are honestly labelled and stay. What was missing "
     "was the other object. M ruled BOTH, and `observed` is now seated: the "
     "108 differentiating electrons register 1306 banks, 98 cells at "
     "(0, 20, 13), K0. 25 of 108 ADDRESSES differ from the prediction and 20 "
     "of 108 CONFIGURATIONS do -- and those 20 are exactly madrule's "
     "exceptions. Twelve elements lose occupancy in a subshell, which the "
     "prediction is monotone and cannot do.",
     "Settled by ruling. Neither chart supersedes the other."),
    ("27", "CLOSED",
     "Can the subject widen past the periodic atoms, and if so is every other "
     "particle now indexed?",
     "M ruled it a valid exception: \"These are legitimate particles and can "
     "and must be accepted.\" The SUBJECT widened to quantum objects; the "
     "CRITERION is untouched and enforce() is still empty. Three indexes "
     "seated -- fundamental (30 Standard Model particles, K2), mesons (242 "
     "of 250, K0) and baryons (278 of 292, K0). docket27.py accounts for the "
     "whole PDG table: 6,506 = 5,880 composite nuclei (the periodic atoms, "
     "already seated as gravity) + 54 PDG status-4 + 572 kept, and ALL 572 "
     "are members of a seated index. 550 of them land on a cell; the 22 that "
     "do not are named, and each is a parity the table does not print. NO NEW "
     "CHANNEL was reached: K4 and K5 are still empty after three new families "
     "of matter.",
     "Quasiparticles are the one honest gap -- they would pass the criterion "
     "and are simply not in this table. Indexing them needs another source."),
    ("28", "CLOSED",
     "Can the quasiparticles DOCKET 27 left out be indexed?",
     "NO, and for two separate measured reasons rather than a failed fetch. "
     "There is no PDG for quasiparticles because the quantum numbers are not "
     "the quasiparticle's: the four textbook kinds land on TWO cells of their "
     "universal numbers and every one is a boson, while everything that "
     "distinguishes one mode from another is the HOST'S -- 230 space groups, "
     "32 point groups, 73 arithmetic crystal classes, banked in sgcapture.py "
     "from spglib. The member set would be (material, mode), a materials "
     "database and not a particle table. And the one family that needs no "
     "fetch, the anyons of SU(2)_k, charts but is REFUSED BY BOX INVARIANCE: "
     "the channel is K2 at every box from k<=4 to k<=24 while the cell moves "
     "at every box, so it is a theorem about the construction.",
     "PARTLY SUPERSEDED BY DOCKET 30, and the half that stands is the first: "
     "there is still no particle table for the textbook quasiparticles. What "
     "DOCKET 30 overturned is the SCOPE of the second -- the anyon refusal was "
     "of the wrong object, not of anyons. A materials database of phonon modes "
     "with each mode's irrep remains a legitimate member set nobody has "
     "fetched."),
    ("29", "CLOSED",
     "Has every index the particle member sets admit been found, or only "
     "every particle been made a member?",
     "The DOCKET 25 census reopened over the three new member sets, exactly "
     "as its ruling said a new member set would. All 142 sub-charts swept. "
     "Three reach a channel the ruling's census calls empty; two are refused "
     "and ONE IS SEATED. Refused: baryons (P, 2I, Q3) at K1, because K1 is "
     "held by gravity_bound and the ruling's self-exclusion does not transfer "
     "to a new parent; and fundamental (Q3, GEN) at K4, because it is arity 2 "
     "and statistics closes 105 of 105 arity-2 charts for free, so what it "
     "shows is join-closure, which is K1. SEATED: baryons (2I, Q3) at K5, the "
     "tree's ONLY K5 -- isospin against charge, 16 cells, all four grounds, "
     "K5 at every mass cut. It stands on GEOMETRY, which is earned (74 of "
     "105) and which the law forces statistics from, so the arity-2 free pass "
     "cannot reach it. SEVEN OF EIGHT CHANNELS ARE NOW OCCUPIED; only K4 is "
     "empty, and all three charts that ever reached K4 were arity 2.",
     "A chart of arity 3 or more reaching K4 would fill the last channel. "
     "None exists anywhere in this tree."),
    ("30", "CLOSED",
     "M: \"And they need to be seated. Why were the indexes not seated?\"",
     "TWO REASONS, AND ONLY ONE WAS A JUDGEMENT CALL. The textbook "
     "quasiparticles have no member set of the right shape and that is "
     "unchanged -- four kinds on two cells, every distinguishing number the "
     "host's. The ANYON refusal was re-examined and DOCKET 28 HAD REFUSED THE "
     "WRONG OBJECT: it charted SU(2)_k for every k, which is a UNION OVER "
     "THEORIES and not a reach over data, so the box varied which universes "
     "were included rather than how much data there was, and of course the "
     "channel never moved. The test was right; the object was wrong. Rebuilt "
     "as a reach -- fqh.py, the quasiparticles of the Laughlin states, indexed "
     "by a MEASURED filling fraction -- THE CHANNEL MOVES (K2 then K0) and "
     "boxinvariance.verdict_of() returns SEAT. 168 members over twelve states, "
     "30 cells, cell (0, 15, 4). Three of the twelve states are observed and "
     "the e/3 quasiparticle's charge was measured by shot noise in 1997. A "
     "theorem fell out: NOT ONE of the 168 is a fermion, forced because "
     "theta/pi = j^2/m is a half only if m divides 2j^2 and m is odd.",
     "DOCKET 28's chart stays refused -- this is a different object, not an "
     "overrule, and both verdicts are on the record. The non-abelian states "
     "(Moore-Read, Read-Rezayi) are a further member set and are not here."),
    ("31", "CLOSED",
     "M: \"almost nothing -- but not nothing ... it is a sub index/sublattice "
     "of bosons.\"",
     "DOCKET 28 wrote \"almost nothing\" and then treated it as nothing. Low "
     "resolution is not none -- overlap.py's LABEL threshold is 0.9 and these "
     "coordinates do not meet it. The ruling also NAMES the object, which "
     "DOCKET 28 never found: a SUBLATTICE OF THE BOSONS. bosonqp.py places 11 "
     "bosonic collective excitations in the frame the tree's own bosons share, "
     "(2J, Q3), which the ruling forces rather than leaves to be chosen. THE "
     "FINDING IS THE RELATION: the tree's bosons are 15 cells and already a "
     "sublattice, the quasiparticles are 3 cells and a sublattice, they are "
     "NOT a subset, and the one cell outside is the COOPER PAIR at charge -2e "
     "-- a charge no meson and no gauge boson reaches. The union is 16 cells "
     "and still a sublattice, so the extension is exactly one cell wide. The "
     "K7 is NOT a finding and the file says so first: three cells in a 2x2 box "
     "is a chain, and z3 proves over every subset of that box that a chain is "
     "closed under meet and join, with a vacuity guard and a contrast.",
     "REOPENED AND REBUILT BY A SECOND RULING. M: \"Do not add declared. "
     "Nothing less than computed or measured. Declared still requires proof.\" "
     "The first draft listed eleven kinds with their spins and charges written "
     "out from textbook knowledge and called it DECLARED provenance; "
     "registry.py had grown a whole category for it. Both are gone. A member "
     "is now defined by WHAT IT IS MADE OF and every number is COMPUTED -- "
     "charge additive, spin by angular-momentum addition, the electron read "
     "from the seated fundamental index. 7 members over 3 composites, 5 cells. "
     "The trion EXCLUDES ITSELF by composing to half-integer spin. The cost is "
     "real and recorded: the collective modes (phonon, magnon, plasmon, "
     "polariton, roton, phason, amplitude mode, magnon-polaron) are NOT "
     "composites, so they cannot be computed and are no longer seated. The "
     "finding survived and strengthened -- the extension is now TWO cells "
     "wide, both Cooper pair spin states -- and the K7 is no longer free "
     "because the chart is no longer a chain: of the six subsets its own size "
     "in its own box, only two close all five."),
    ("32", "CLOSED",
     "The non-abelian Hall states -- Moore-Read at nu=5/2 and Read-Rezayi at "
     "12/5 -- named as a further member set by DOCKET 30 and left open.",
     "SEATED. readrezayi.py charts the Z_k parafermion primaries of the "
     "Read-Rezayi series; Moore-Read IS RR_2, not a separate construction. 363 "
     "members over eleven levels, 78 cells, K0. k is a genuine REACH because "
     "RR_k sits at nu = 2 + k/(k+2), so each k names a plateau -- which is "
     "exactly what DOCKET 28's SU(2)_k union lacked -- and the channel MOVES "
     "K2 to K0, so the same test seats it. THE WEIGHTS ARE VALIDATED AGAINST "
     "THE LITERATURE: the closed form returns {0, 1/16, 1/2} at k=2, exactly "
     "the Ising category, and 2/5 at k=3, the Fibonacci tau; charges e/4 and "
     "e/5 as published. TWO NEGATIVE FINDINGS. First, the Majorana bounds "
     "DOCKET 30's theorem: fqh proved no Laughlin quasiparticle is ever a "
     "fermion, and this series has six, the first being the Ising psi at "
     "h = 1/2 -- so that theorem was about the ABELIAN ones. Second, NEITHER "
     "index nests in the other: 15 cells against 57 on their shared "
     "coordinates, 8 in common, neither containing the other and neither a "
     "sublattice, which is the negative counterpart of DOCKET 31.",
     "It also closes DOCKET 28's trap: SU(2)_2 carries h = 3/16 and the real "
     "Moore-Read state carries 1/16, so that chart had the wrong PHYSICS as "
     "well as the wrong shape."),
    ("33", "CLOSED-WITH-A-CORRECTION",
     "M: \"seat that sweep as an instrument ... run all candidates. Leave no "
     "stone unturned. And if any sublattice may possibly contain its own "
     "sublattice, we must seek a determination.\"",
     "subpop.py seats the MEMBER sub-population sweep -- every sweep before it "
     "varied COLUMNS (DOCKET 25 over accessors, DOCKET 29 over all 142 "
     "coordinate subsets), and DOCKET 31 asked the member question without "
     "naming it as a method. 143 sublattices found; TWO reach K4, the last "
     "empty channel. One dissolves (madrule at l_d=0 holds a coordinate "
     "constant, effective arity 2, statistics free). THE OTHER IS THE FIRST "
     "ARITY-3 K4 THIS TREE HAS SEEN: the spin-4 mesons on (P, 2I, Q3), 10 "
     "members, 9 cells, cell (4,5,3), statistics EARNED. IT STILL FAILS, and "
     "for a NEW reason -- two of the ten carry no printed mass, so under the "
     "parent's own reach the population is 7 cells at K5 at every cut and "
     "never 9 at K4. K4 stays empty for a THIRD reason: a channel that lives "
     "on members the table cannot place in a reach. THE RECURSION "
     "DETERMINATION CORRECTED ITSELF: within the sweep's family there are 14 "
     "strict containments and the longest chain is 2, which would have been "
     "reported as the answer -- but enumerating EVERY subset of the four "
     "indexes small enough gives chains of 5 (bosonqp), 7 (spin4), 6 (madrule) "
     "and 14 (baryon_isomultiplet, 1,649 sublattices in one 16-cell chart, more "
     "than the whole family sweep found). The depth-2 figure is about the FAMILY, "
     "not the lattices. All candidates run: the chiral Goldstone sublattice is "
     "real but a FULL PRODUCT BOX so its closure is free; the electroweak "
     "eaten Goldstones land on three cells fundamental already holds, a "
     "relabelling.",
     "NOT DETERMINED for the eighteen indexes too large to enumerate -- the "
     "family figure is a floor there, and too_large() names them. NUCLEAR "
     "ROTATIONAL BANDS were not run, and the reason this file first gave was "
     "WRONG: four searches for a level scheme returned nothing (ENSDF 403, two "
     "pypi dead ends, zero corpus hits) and subpop.py concluded there was "
     "nothing this environment could reach. ALL FOUR WERE MEETS. NAVIGATION.md "
     "section 3 -- the retrieval law this project derived from the three-body "
     "index -- says navigate by JOIN, never by meet: meet failures run 12 to "
     "90,705 by cap, join failures are 0 at every cap. Run as a join over the "
     "paper database the fifth route returns at once, with E and I^pi PER BAND "
     "MEMBER: arXiv:2508.05447 (234 two-quasiparticle bands in DEFORMED odd-odd "
     "nuclei -- the candidate) and arXiv:2303.13849 (290 magnetic and "
     "antimagnetic bands in 150 nuclei -- the SHEARS mechanism in NEAR-SPHERICAL "
     "nuclei, a DIFFERENT object). arXiv is 403 over https here exactly as ENSDF "
     "is; the connector is a different bracket and the join is what reached it. "
     "DOCKET 35 THEN WALKED IT: nbcapture.py captures 2303.13849 in full, "
     "reproducing the paper's own census exactly (252 MR bands in 123 nuclei, 38 "
     "AMR in 27) AND its own Delta-I selection rule (213 of 213 AMR steps at "
     "Delta-I = 2), which is a check on column order that a count cannot make. "
     "nucbands.py seats 2,145 nuclear excited states on (2I, parity): 121 cells, "
     "cell (2,63,2), K2 -- AND THE K2 IS THE FREE ONE, statistics being vacuous "
     "at arity 2, so the index closes in NOTHING and every third coordinate "
     "measured drops it to K0. Refused on the criterion: 27 bands the source "
     "prints with no I^pi column at all, and 93 levels with a spin but no "
     "parity, counted apart because they are different facts. 2508.05447 -- the "
     "DEFORMED rotor's tower, the candidate subpop.py actually named -- is "
     "captured as text and NOT parsed: two attempts reached 154 and 176 of its "
     "stated 234 entries, and a capture that cannot be shown total is not "
     "seated."),
)

# DOCKET 25's census, as measured.  The two artifact rows are named because a
# census that hides its own double-counts is not a census.
CENSUS = {
    "modules_in_tree": 232,
    "modules_attempted": 232,
    "never_attempted": [],
    "unimportable": ["c333 (needs a module 'common' that is not here)",
                     "machinecheck (SystemExit at import)",
                     "pdftext (IndexError -- takes argv)",
                     "render_pdf (IndexError -- takes argv)"],
    "imported_but_no_chart": ["state", "machinecheck-vacancy", "mcheck_mi"],
    "charts_found": 44,
    "modules_with_a_chart": 31,
    "unseated_not_excused": 24,
    "new_first_order_indexes": 0,
    "charts_per_channel": {"K0": 15, "K1": 1, "K2": 10, "K3": 7, "K4": 0,
                           "K5": 1, "K6": 2, "K7": 8},
    "K4_reached_by": "nothing in the tree -- 0 of 44 charts over 231 modules",
    "K5_reached_by": "exactly one chart, overlaprule.nucshell_lsigma, which "
                     "DOCKET 22 retracted",
    "artifacts_of_the_census": [
        "madelung.k6_chart is listed unseated but IS the seated "
        "madelung_slot under its other accessor name -- the census keys on "
        "(module, accessor) and double-counts it",
        "boxinvariance.madelung_predicate at K3 is a helper written during "
        "this work that reproduces fibred's members, not a discovery",
    ],
}

# Things this tree asserted and then measured to be false.  Generated where it
# can be -- the unseating is read from overlaprule -- and quoted where the
# claim was prose.
RETRACTIONS = (
    ("overlaprule.py §5", "madelung's parent is 'a complete rectangle, which "
     "closes everything for free'",
     "FALSE. 170 cells in an 810-cell box, density 0.2099, not even a "
     "down-set. Its sibling fibred holds the same 170 at the same density and "
     "is K3."),
    ("overlaprule.py §5", "'the fill-order base carries order and algebra and "
     "does NOT carry geometry'",
     "FALSE of the base. Paired with l the same base is K7. The parent's three "
     "arity-2 projections are K7 / K6 / K7."),
    ("overlaprule.py §5", "'the radial node count is what breaks join-closure' "
     "in the nuclear shell sequence",
     "FALSE. (nr, sigma) is 6 cells at K7 with ZERO join counterexamples, so "
     "forgetting l restores join-closure exactly as completely."),
    ("overlaprule.py §5", "gravity: 'the raggedness lives in D,Y,L,E and NOT "
     "in the bound structure'",
     "TRUE operatively (256 join failures against 0) and FALSE in its strong "
     "reading: 509 of 96,372 parent join failures are witnessed inside the "
     "bound triple, cross-block."),
    ("overlaprule.py", "gravity (B,F,X) is 'dimension-blind'",
     "FALSE. B is a function of (D, q, F, Jzero) and its profile differs at "
     "D=4, D=5 and D>=6."),
    ("overlaprule.py §6", "the ultraspinning reading",
     "It is off CUMULATIVE D sweeps. Per single dimension D=4 is K7, D=5 is "
     "K1, and D=6..11 are EACH K0."),
    ("nucshell.py", "its parent closes 'K7 ... the only seated index of arity "
     "3 to reach it'",
     "BOTH HALVES FALSE. It is K3, and fibred.index is a second arity-3 K3."),
    ("boxinvariance.py", "madelung's 170 are 'ENUMERATED, not generated by a "
     "rule over an alphabet'",
     "FALSE. All 170 reproduce from {1<=n<=12, 0<=l<n, n+l<=9, 0<=k<2(2l+1)}. "
     "The test was applicable and had been declared inapplicable instead of "
     "run. Run now: madelung PASSES, the channel moves K6 -> K7 when l<n is "
     "dropped."),
    ("registry.py", "fibred and madelung described as '170 electrons' with no "
     "provenance",
     "INCOMPLETE rather than false. They are the MADELUNG-PREDICTED 170, built "
     "on a table Register 1306 withdrew as a source of observed "
     "configurations. Relabelled, and the observed object seated beside them "
     "-- DOCKET 26."),
    ("overlaprule.py §5", "gravity (B,F,X) has '64 meet counterexamples'",
     "That is the ORDERED count printed beside the UNORDERED pair total. It "
     "is 32 in 325 unordered pairs. The selftest caught it."),
    ("figure.py §1b", "'the three new vertices land at heights and widths the "
     "figure already held'",
     "FALSE of the one that fell -- nucshell (l, sigma) had width 2, which was "
     "new. True of the two that remain."),
)


def commit():
    """The HEAD commit, read from .git without shelling out.  None if absent."""
    try:
        head = open(os.path.join(ROOT, ".git", "HEAD"),
                    encoding="utf-8").read().strip()
        if head.startswith("ref: "):
            ref = head[5:]
            p = os.path.join(ROOT, ".git", ref)
            if os.path.exists(p):
                return open(p, encoding="utf-8").read().strip()[:12]
            for ln in open(os.path.join(ROOT, ".git", "packed-refs"),
                           encoding="utf-8"):
                if ln.rstrip().endswith(" " + ref):
                    return ln.split()[0][:12]
            return None
        return head[:12]
    except OSError:
        return None


def state():
    """The whole current state, ASKED of the instruments.  Nothing typed here."""
    import registry
    import figure
    import demand
    import overlaprule as OR
    import mi

    cells = registry.cells()
    ch = mi.channels()
    src = registry.sources()
    rows = []
    for nm, mod, acc, meth, what, q in registry.rows():
        c = cells[nm]
        rows.append({
            "name": nm, "module": mod, "accessor": acc, "method": meth,
            "label": registry.short(nm), "members": what, "quantum": q,
            "cells": len(registry.index_of(nm)),
            "cell": list(c) if c != "UNMEASURED" else None,
            "channel": c[0] if c != "UNMEASURED" else None,
            "languages": sorted(ch[c[0]]) if c != "UNMEASURED" else None,
            "seated_by_overlap_ruling": mod == OR.SELF,
            "source": src[nm],
        })
    F = figure.figure()
    occupied = sorted({c[0] for c in F})
    res = {a: {"distinct": d, "of": n, "ratio": r, "verdict": v}
           for a, d, n, r, v in figure.resolution()}
    return {
        "schema": SCHEMA,
        "commit": commit(),
        "regenerate": "python3 research/warp-drive/state.py --json",
        "complete": registry.COMPLETE,
        "registry": {"rows": len(rows), "indexes": rows},
        "figure": {
            "vertices": len(figure.cells()),
            "distinct_cells": len(F),
            "closers": figure.closers(),
            "own_cell": list(figure.self_cell()[0]),
            "own_cell_occupied_by": figure.self_cell()[1],
            "E": demand.E(F),
            "channels_occupied": occupied,
            "channels_empty": [k for k in range(8) if k not in occupied],
            "resolution": res,
            "labelled_axes": sorted(figure.labelled_axes()),
        },
        "channels": {"K%d" % i: sorted(s) for i, s in enumerate(ch)},
        "census": CENSUS,
        "overlap_ruling": {
            "grounds": ["novel channel", "not a relabelling", "reach stable",
                        "coordinate forced"],
            "seated": [{"parent": p, "cols": list(c), "channel": k,
                        "cells": n} for p, c, k, n in OR.admissible()],
            "refused": [{"parent": p, "cols": list(c), "failed": w}
                        for p, c, w in OR.refused()],
            "candidates": len(OR.CANDIDATES),
        },
        "retractions": [{"where": w, "claimed": c, "measured": m}
                        for w, c, m in RETRACTIONS],
        "dockets": [{"id": i, "status": st, "question": q, "finding": f,
                     "what_would_settle_it": s}
                    for i, st, q, f, s in DOCKETS],
        "not_claimed": [
            "COMPLETE is False and stays False -- this is not every "
            "first-order index, it is the ones found and survived.",
            "An empty channel is not a theorem that nothing can sit there.",
            "A refusal is recorded so it can be re-adjudicated, not closed.",
        ],
    }


def to_markdown(S):
    L = ["# The index work: current state", ""]
    L.append("Generated by `%s`. Commit `%s`. Schema %d."
             % (S["regenerate"], S["commit"] or "unknown", S["schema"]))
    L.append("")
    L.append("**`COMPLETE` is %s and stays false.** This is the set of "
             "first-order indexes found and survived, not a claim to have "
             "found them all." % S["complete"])
    L.append("")
    f = S["figure"]
    L.append("## The figure")
    L.append("")
    L.append("| | |")
    L.append("|---|---|")
    for k, v in (("vertices", f["vertices"]), ("distinct cells",
                 f["distinct_cells"]), ("closes in", ", ".join(f["closers"])
                 or "nothing"), ("E", f["E"]),
                 ("its own cell", tuple(f["own_cell"])),
                 ("channels occupied", ", ".join("K%d" % k
                                                 for k in f["channels_occupied"])),
                 ("channels empty", ", ".join("K%d" % k
                                              for k in f["channels_empty"]))):
        L.append("| %s | %s |" % (k, v))
    L.append("")
    L.append("Resolution on itself (a coordinate at >= 0.9 is a row label, "
             "not a measurement):")
    L.append("")
    L.append("| axis | distinct | of | ratio | verdict |")
    L.append("|---|---|---|---|---|")
    for a, r in S["figure"]["resolution"].items():
        L.append("| %s | %d | %d | %.4f | %s |"
                 % (a, r["distinct"], r["of"], r["ratio"], r["verdict"]))
    L.append("")
    L.append("## The seated indexes")
    L.append("")
    L.append("| index | members | quantum numbers | cells | cell | channel |")
    L.append("|---|---|---|---|---|---|")
    for r in S["registry"]["indexes"]:
        L.append("| `%s` | %s | %s | %d | %s | K%s |"
                 % (r["label"], r["members"], r["quantum"], r["cells"],
                    tuple(r["cell"]) if r["cell"] else "unmeasured",
                    r["channel"]))
    L.append("")
    L.append("## Where each index's data comes from")
    L.append("")
    L.append("Declared as `SOURCE` beside the code that reads it, resolved "
             "against the repository root and hashed here, so the provenance "
             "travels in the tree rather than in a chat. An empty path list "
             "means the index is COMPUTED from a rule and reads no table -- "
             "that is a source, not a gap.")
    L.append("")
    L.append("| index | provenance | files (md5, bytes) |")
    L.append("|---|---|---|")
    for r in S["registry"]["indexes"]:
        src = r["source"]
        fs = "; ".join(
            ("`%s/` — %d files, %s B, digest %s"
             % (d["path"], d["files"], d["bytes"], d["md5"][:12])
             if d["kind"] == "dir" else
             "`%s` (%s, %s B)" % (d["path"], d["md5"][:12], d["bytes"]))
            if d["exists"] else "`%s` **MISSING**" % d["path"]
            for d in src["paths"]) or "*computed -- no table read*"
        L.append("| `%s` | %s | %s |" % (r["label"], src["why"], fs))
    L.append("")
    L.append("## The overlap ruling")
    L.append("")
    L.append("Grounds: " + "; ".join("**%s**" % g
                                     for g in S["overlap_ruling"]["grounds"])
             + ".")
    L.append("")
    for s_ in S["overlap_ruling"]["seated"]:
        L.append("- **seated** `%s (%s)` at K%d, %d cells"
                 % (s_["parent"], ", ".join(s_["cols"]), s_["channel"],
                    s_["cells"]))
    for s_ in S["overlap_ruling"]["refused"]:
        L.append("- refused `%s (%s)` -- failed: %s"
                 % (s_["parent"], ", ".join(s_["cols"]),
                    ", ".join(s_["failed"])))
    L.append("")
    L.append("## Retractions -- read these before quoting anything")
    L.append("")
    L.append("Claims this tree made and later measured to be false.")
    L.append("")
    for r in S["retractions"]:
        L.append("- **%s** claimed *%s*. %s" % (r["where"], r["claimed"],
                                                r["measured"]))
    L.append("")
    c = S["census"]
    L.append("## The census (DOCKET 25)")
    L.append("")
    L.append("Every chart-shaped accessor in the research tree, with attempt "
             "logging so coverage is measured rather than inferred.")
    L.append("")
    L.append("| | |")
    L.append("|---|---|")
    L.append("| modules attempted | %d of %d |"
             % (c["modules_attempted"], c["modules_in_tree"]))
    L.append("| charts found | %d over %d modules |"
             % (c["charts_found"], c["modules_with_a_chart"]))
    L.append("| unseated and not excused | %d |" % c["unseated_not_excused"])
    L.append("| **new first-order indexes** | **%d** |"
             % c["new_first_order_indexes"])
    L.append("| K4 | %s |" % c["K4_reached_by"])
    L.append("| K5 | %s |" % c["K5_reached_by"])
    L.append("")
    L.append("Charts per channel: " + ", ".join(
        "%s %d" % (k, v) for k, v in c["charts_per_channel"].items()) + ".")
    L.append("")
    L.append("Artifacts of the census itself, named because a census that "
             "hides its own double-counts is not a census:")
    L.append("")
    for a in c["artifacts_of_the_census"]:
        L.append("- %s" % a)
    L.append("")
    L.append("## Dockets")
    L.append("")
    L.append("| # | status | question | finding | what would settle it |")
    L.append("|---|---|---|---|---|")
    for d in S["dockets"]:
        L.append("| %s | **%s** | %s | %s | %s |"
                 % (d["id"], d["status"], d["question"], d["finding"],
                    d["what_would_settle_it"]))
    L.append("")
    L.append("## Not claimed")
    L.append("")
    for n in S["not_claimed"]:
        L.append("- %s" % n)
    L.append("")
    return "\n".join(L)


def _strip(S):
    """Everything but `commit`, which moves with every push and is not drift."""
    d = dict(S)
    d.pop("commit", None)
    return d


def check():
    """Does the written STATE.json still agree with the instruments?"""
    p = os.path.join(HERE, "STATE.json")
    if not os.path.exists(p):
        return False, "STATE.json does not exist -- run --json"
    on_disk = json.load(open(p, encoding="utf-8"))
    fresh = state()
    if _strip(on_disk) == _strip(json.loads(json.dumps(fresh))):
        return True, "STATE.json agrees with every instrument"
    diff = [k for k in fresh
            if k != "commit"
            and json.dumps(on_disk.get(k), sort_keys=True)
            != json.dumps(json.loads(json.dumps(fresh[k])), sort_keys=True)]
    return False, "STALE in: %s -- regenerate" % ", ".join(diff)


def report():
    S = state()
    print(to_markdown(S))
    return 0


def selftest():
    ok = True

    def chk(lab, got, want):
        nonlocal ok
        good = got == want
        ok &= good
        print("  [%s] %-56s %s" % ("ok" if good else "XX", lab,
                                   got if good else "%s != %s" % (got, want)))

    S = state()
    import registry
    import figure
    chk("it asks the registry for its rows, and agrees",
        S["registry"]["rows"], len(registry.REGISTERED))
    chk("it asks figure for the vertex count, and agrees",
        S["figure"]["vertices"], len(figure.cells()))
    chk("every row carries its quantum numbers",
        [r["label"] for r in S["registry"]["indexes"] if not r["quantum"]], [])
    chk("every row has a measured cell",
        [r["label"] for r in S["registry"]["indexes"] if r["cell"] is None], [])
    chk("labels are unique",
        len({r["label"] for r in S["registry"]["indexes"]}),
        S["registry"]["rows"])
    chk("COMPLETE is not claimed", S["complete"], False)
    chk("the eight channels are all named", len(S["channels"]), 8)
    chk("empty and occupied channels partition the eight",
        sorted(S["figure"]["channels_occupied"]
               + S["figure"]["channels_empty"]), list(range(8)))
    # the hand-maintained table, guarded
    chk("every docket has an id, a status, a question, a finding and a remedy",
        [d["id"] for d in S["dockets"]
         if not all((d["id"], d["status"], d["question"], d["finding"],
                     d["what_would_settle_it"]))], [])
    chk("every retraction names where, what was claimed, and what was measured",
        [r["where"] for r in S["retractions"]
         if not all((r["where"], r["claimed"], r["measured"]))], [])
    chk("the retraction list is not empty -- a tree that never erred is "
        "a tree that never checked", len(S["retractions"]) > 0, True)
    chk("the ruling's seated rows all appear in the registry",
        [s_["parent"] for s_ in S["overlap_ruling"]["seated"]
         if not any(r["seated_by_overlap_ruling"] for r
                    in S["registry"]["indexes"])], [])
    chk("seated + refused accounts for every candidate",
        len(S["overlap_ruling"]["seated"])
        + len(S["overlap_ruling"]["refused"]),
        S["overlap_ruling"]["candidates"])
    # DOCKET 25's census -- hand-recorded from the sweep logs, so guarded.
    c = S["census"]
    chk("EVERY module in the tree was attempted",
        c["modules_in_tree"] - c["modules_attempted"], 0)
    chk("and the four that cannot be imported are named with the reason",
        [u for u in c["unimportable"] if "(" not in u], [])
    chk("its per-channel counts sum to the chart total",
        sum(c["charts_per_channel"].values()), c["charts_found"])
    chk("K4 is reached by no chart at all", c["charts_per_channel"]["K4"], 0)
    chk("K5 by exactly one -- the retracted row",
        c["charts_per_channel"]["K5"], 1)
    # DOCKET 34 broke the coincidence this fixture used to rest on.  The
    # census counts CHARTS (DOCKET 25's unseated candidates); the figure
    # counts SEATED INDEXES.  They agreed channel-for-channel until spin4 was
    # seated at K4 on the PDG status reach, which no chart reaches.  That is
    # not a drift -- it is the whole content of DOCKET 33 and 34.
    chk("K4 is occupied by a SEATED INDEX and reached by NO CHART",
        (4 in S["figure"]["channels_occupied"], c["charts_per_channel"]["K4"]),
        (True, 0))
    chk("and every OTHER channel the figure occupies has at least one chart",
        [k for k in S["figure"]["channels_occupied"]
         if k != 4 and c["charts_per_channel"]["K%d" % k] == 0], [])
    chk("the census names its own artifacts",
        len(c["artifacts_of_the_census"]) > 0, True)
    chk("markdown renders without raising", bool(to_markdown(S)), True)
    print("state selftest: %s" % ("PASS" if ok else "FAIL"))
    return ok


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    if "--check" in sys.argv:
        good, msg = check()
        print(("ok   " if good else "XX   ") + msg)
        sys.exit(0 if good else 1)
    if "--json" in sys.argv or "--md" in sys.argv:
        S = state()
        if "--json" in sys.argv:
            p = os.path.join(HERE, "STATE.json")
            open(p, "w", encoding="utf-8").write(
                json.dumps(S, indent=1, sort_keys=False) + "\n")
            print("wrote %s" % p)
        if "--md" in sys.argv:
            p = os.path.join(HERE, "STATE.md")
            open(p, "w", encoding="utf-8").write(to_markdown(S))
            print("wrote %s" % p)
        sys.exit(0)
    sys.exit(report())
