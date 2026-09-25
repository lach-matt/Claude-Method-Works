#!/usr/bin/env python3
r"""
ledger.py -- WHAT IS ESTABLISHED, WHAT IS OWED, AND WHICH SIDE OWES IT.

    python3 ledger.py             the reading
    python3 ledger.py --selftest  every row asked of its owner; stdlib only
    python3 ledger.py --md        write LEDGER.md
    python3 ledger.py --check     LEDGER.md against a fresh ask; exit 1 on drift

Run under python3 (3.11).  STDLIB ONLY, plus the seated peers it asks.

===============================================================================
0.  WHY THIS EXISTS, AND WHAT IT IS NOT
===============================================================================

M ruled the order of work: CONSOLIDATE first, keep TESTING beside it, and only
then build the positive theory -- "we'll be working it like balancing an
equation with the theory and math on one side, and the device engineering and
materials on the other side".  This file is the first half of that instruction
and it is built in the shape of the second.

    IT ESTABLISHES NOTHING.  Not one row here is derived, measured or proved by
    this file.  Every row is ASKED of the instrument that owns it, at run time,
    and a row whose owner disagrees is a failure rather than a surprise.  That
    is `state.py`'s discipline applied to the warp work, which had no equivalent:
    `state.py` answers "what is the index right now", and nothing answered "what
    is the warp result right now".

    IT IS NOT A SUMMARY EITHER.  A summary can be read and believed.  This can
    be RUN, and `--check` fails when a peer moves underneath it.  The distinction
    is the whole point: this project has twice shipped a figure that was true
    when written and false when read -- `achievable.py`'s "sixty-five orders",
    `bounds.py`'s "Casimir saturates Ford-Roman" -- and both were prose quoting a
    number no instrument was asked for.

===============================================================================
1.  THE FIVE STATUSES, AND WHY THERE ARE FIVE RATHER THAN TWO
===============================================================================

M's standing rule is "Nothing less than computed or measured".  That rules out
ASSERTION as a status; it does not collapse the rest into one, because a
THEOREM and a SURVEY fail in different ways and a reader who cannot tell them
apart cannot tell what would change the answer.

  THEOREM    proved, with stated hypotheses, and the hypotheses are named.  It
             fails only if a hypothesis fails.
  MEASURED   a number produced by a computation someone can re-run.  It fails if
             the computation is wrong or its inputs move.
  SURVEY     true of everything looked at, and nothing proves the look was
             exhaustive.  It fails silently, when something unlooked-at turns up.
             DOCKET 55's verdict is this and says so.
  OPEN       named, not answered, and the thing that would answer it is named.
  WITHDRAWN  this project asserted it and then refuted it.  KEPT, never deleted:
             a withdrawn figure that leaves no trace is how a corpus forgets it
             was ever wrong.

THE DISTINCTION THAT MATTERS MOST HERE IS THEOREM AGAINST SURVEY, and it is
DOCKET 55's own finding about itself: four limbs, each proved inside its own
hypotheses, whose CONJUNCTION is a survey because nothing proves those
hypotheses exhaust the matter models.  Calling that conjunction a theorem would
be `achievable.py`'s error committed one level up.

===============================================================================
2.  THE TWO SIDES
===============================================================================

LEFT, THE DEMAND.  What the theory requires of any device that does this, with
the status of each requirement.  This side is settled by mathematics and moves
only when a proof moves.

RIGHT, THE SUPPLY.  What physics and materials actually deliver, with a ceiling
on each.  This side moves when a measurement improves or a mechanism is found.

THE BALANCE is the difference, in orders of magnitude, and the honest reading of
it is NOT always "how far short we are".  Two rows on this ledger are short by a
finite, quotable number.  One is short by a number that no engineering can move
because the ceiling is a-INDEPENDENT.  And one is not short at all -- DOCKET 56's
reconstruction route has a PRICE, and until DOCKET 65 it was the only row here
that did; DOCKET 65's remainders S11-S13 are priced too (section 6).

    A ROW WHERE THE DEMAND IS REFUSED RATHER THAN EXPENSIVE IS MARKED REFUSED
    AND CARRIES NO GAP.  A gap implies a ladder.  Where the sign inverts before
    the magnitude is reached, there is no ladder and quoting a gap would invent
    one.  DOCKET 54's Boyer inversion and DOCKET 53's plate mass are both of this
    kind and neither gets a number in the gap column.

===============================================================================
3.  WHAT THIS FILE REFUSES
===============================================================================

    IT DOES NOT RANK THE OPEN QUESTIONS.  How many are open is whatever
    statuses() counts -- this sentence first said "Three are open" and went
    stale the day O4-O7 arrived, which is the fault this file exists to catch,
    so no count is typed here.  Which is most promising is a judgement and
    judgements are M's.
    IT DOES NOT TOTAL THE GAPS.  Orders of magnitude on different quantities do
    not add, and a single headline number would be the most quotable false thing
    in the repository.
    IT DOES NOT CARRY THE INDEX WORK.  `state.py` owns that and this file does
    not duplicate a row of it.
    IT REPAIRS NOTHING AND EDITS NO PEER.

===============================================================================
4.  DOCKETS 62 AND 63, AS M RULED THEM
===============================================================================

DOCKET 62 CLOSED NOTHING.  O2, O3, O5, O6 and O7 stay OPEN and are NARROWED,
each now ASKED of the instrument that seated its narrowing (fewsterteo.py,
latticectc.py, throatmass.py, branelink.py), and each owner is asked whether it
closed -- an open row whose owner says CLOSED is a selftest failure.  The one
new row its narrowings produced is the flat-bulk lattice theorem, D21, a
THEOREM with its hypotheses named; its RECOMMENDED new rows are decided below,
one by one, under the principle for opening a row.  REFUSED by the ruling
and therefore NOT on this board: closing any of the five; the
curvature-tightened persistence figures; the void 9/64 adjustment; an R-1 row (it is O7 renamed); a separate NEC-everywhere row (it is
O3 with a clause); the Caldwell & Langlois withdrawal (it has no referent).
The selftest asserts each refusal.  The wording each narrowing replaced is
KEPT in SUPERSEDED_WORDING, because a row rewritten in place leaves no trace
otherwise.

DOCKET 63 adds D15-D20 (the Higgs at the endpoint), S6-S8 (all REFUSED, no
gap) and W9-W13, owners as the ruling named them.  W9 is excite.W9 and
W10-W13 are address.WITHDRAWN: the withdrawn rows are ASKED too, not retyped.

THE PRINCIPLE FOR OPENING A ROW, STATED ONCE AND APPLIED TO EVERY CANDIDATE:

    A QUESTION THE TREE ALREADY HAS AN INSTRUMENT FOR GETS A ROW NOW -- the
    board must not lag the tree.  A QUESTION WITH NO INSTRUMENT IS OPENED BY
    THE DOCKET THAT BUILDS ITS INSTRUMENT, because a row this file cannot ask
    is a row it cannot defend.

    AND A ROW IS FOR A QUESTION THAT CAN MOVE A REQUIREMENT OR A PRICE ON THE
    BOARD.  An unsettled question internal to an already-REFUSED row, which
    gates nothing, is recorded where that row's owner records it and gets no
    row of its own -- one row per question would over-represent it.  This is
    the criterion that keeps DOCKET 63 section E's thirteen items off the
    board (see the census re-pin below); it is part of the principle, not an
    exception to it.

Applied, candidate by candidate (the owner was READ before each decision):
  D22  stress-tensor fluctuations -- fluctuation.py.  OPENED.
  D23  the first trip / amortisation -- transit.py (TRAVERSAL_IS_REMOVED).
       OPENED; S5's note now carries the amortisation reading.
  D24  formation -- create.py (NUCLEATION_STATUS).  OPENED.
  D25  the destination stock gate -- stockgate.py (GATE), auditing stock.py.
       OPENED.
  S9   the Drive folder's device specification as a supply -- warpfolder.py
       (FLASH_IS_A_RECONSTRUCTION_MECHANISM).  SEATED, REFUSED.
  linearised stability -- OPENED by DOCKET 64 as D26 (linstab.py).  At
       DOCKETS 62/63 it was NOT OPENED because no instrument asked it:
       stability.py asked only the CLASSICAL radial stability of
       concentric.py's shell, and nothing evaluated Anderson-Molina-Paris-
       Mottola's criterion on anything.  That deferral is what the principle's
       second half is for, and DOCKET 64 built the instrument.
       WAITS_FOR_ITS_INSTRUMENT is now empty, and LEDGER.md prints "none"
       rather than dropping the section.
  the FINITE Higgs share of atomic mass -- massform.py.  NOT A ROW, ON M's
       RULING M-D65-2 ('Fold into S10 (Recommended)').  The question is
       internal to the REFUSED row S10, it gates nothing ("nothing in DOCKET
       65 moves on it") and nothing computes it, so by the principle's clause
       on questions internal to an already-REFUSED row that gate nothing it is
       recorded where its owner records it: as the OPEN item
       "S10 (open)" inside S10's note, a candidate question for a future
       docket.  DOCKET 65's seating first opened it as its own row, O8; M was
       asked which it should be and ruled the fold, and O8 is not seated.

===============================================================================
5.  DOCKET 64, AS M RULED IT
===============================================================================

M ruled that all DOCKET 64 calculations run and be seated.  Five instruments
were seated first -- noise.py, hpscentre.py, qeihps.py, linstab.py and
formation.py -- and every row below is ASKED of them.  This file reads their
CORRECTED attributes, which are in places weaker than the ruling's section C
wording, because the ruling never saw the full verifier verdicts for three of
the lines; where the two differ the weaker, better-supported statement is the
one printed here:

  D22  OPEN -> SURVEY, owner noise.CORRIDOR_APPLICATION.  C1 is a THEOREM in
       the flat model H1-H6 only; on the corridor H2 fails and the curved
       decision is O2's.  The Einstein-Langevin surrogate figure is printed
       from noise.EL_VACUUM_LOG10_NEG_LN_P, never typed.
  D24  stays OPEN, owner formation.NUCLEATION_PRICEABLE_FROM_SOURCE, whose
       value is NOT DETERMINED: the neck is a recipe with free functions and
       its price has not been computed.  "Cannot be priced from the source"
       was withdrawn by formation.py's verification and is not printed.
  D25  stays OPEN and UNCHANGED, owner stockgate.GATE.  formation.py evaluates
       no conjunct anew and re-prices none; stockgate's figures are not
       re-printed a second time.  The survey names a CONDENSED body (Proxima b);
       what is open is "primitive" and "accessible".
  D26  NEW, OPEN, owner linstab.SEMICLASSICAL_EVALUABLE_ON_DEMAND, text
       linstab.D26_CLAIM with the IFF narrowed to GMMPS's reported mode and
       "recorded or shown" in place of a proof.
  O5   stays OPEN, re-owned to hpscentre.O5_CLOSED; the throat-geodesic
       verdict is qeihps.VERDICT_THROAT_GEODESIC, "NOT A TEST".
  O2   stays OPEN; its answer now names D22's curved distribution question.

Not opened, each because it is the SAME question as an existing row (a
second row for one question is the over-representation the principle
forbids): the curved smeared variance (O2's); Kontou's QEI on HPS (O5's);
formation (D24's third part).  The phase1 D4 restatement was a requirement
question for M, not a row.  M RULED: restate it.  phase1.py now states D4 as
T^{0i} = 0 in each configuration and zero net momentum across a passage, and
RULED_BY_M records the ruling (M-D64-1).

DOCKET 64's lines withdrew claims their own reports had made before seating.
Each is kept on its owner (noise.WITHDRAWN, hpscentre.WITHDRAWN,
linstab.WITHDRAWN, qeihps.VERDICT_THROAT_GEODESIC_WITHDRAWN, formation.py's
[W1]-[W7]).  None was ever on this board, so none is a W row here; the board
wording DOCKET 64 replaced is kept in SUPERSEDED_WORDING.

===============================================================================
6.  DOCKET 65, AS M RULED IT
===============================================================================

DOCKET 65 tested M's mechanism (M-S1A-P1) in massform.py, and M ruled its rows
"Seat as proposed".  Every one is ASKED of massform.PROPOSED_ROWS at run time
-- text, status and owner -- and none is retyped here:

  D27, D28, D29  DEMAND, each a THEOREM on hypotheses its own row names
                 (M's consideration computed; the pair floor; the field has no
                 energy to give about v).
  S10            SUPPLY, M's mechanism as a supply of payload mass.  Its status
                 IS massform.MECHANISM_VERDICT[0], REFUSED reading by reading;
                 gap None, since no ladder is quoted for a refusal.
  S11, S12, S13  SUPPLY, OPEN: the anomaly route, the pair route and the
                 held-seat release route -- priced remainders, not refusals.
                 Their names are massform.SURVIVES's.
  S10 (open)     NOT A ROW: the FINITE Higgs share of atomic mass, an OPEN
                 item carried inside S10's note -- massform's item, asked, its
                 status massform.FINITE_HIGGS_SHARE_STATUS.  No DOCKET 65
                 verdict rests on it.  The seating first opened it as the row
                 O8; M ruled M-D65-2, 'Fold into S10 (Recommended)', and it is
                 folded back (section 4).
  S5             note appended: reconstruction from destination stock survives
                 M's mechanism (massform.RECONSTRUCTION_SURVIVES).

Not opened: massform.NOT_OPENED (asked), each internal to S10 or S13 or gating
nothing (the selftest asks each item: it names S10 or S13, says 'no verdict',
or is the H-FLAV-only sub-count, whose owner says it carries no verdict).

A SUPPLY row has one note, so S10-S13 carry the proposed claim followed by
what would move it, both asked; S10's note then carries the item S10 (open),
its text and what would move it, asked too.  massform.py asks THIS file for D23 (the
held-seat route needs a prior arrival) and for M's words, and it does so only
at CALL time, never while it is being imported: this file asks massform for
its rows during its own import, and two modules that each need the other at
import find each other empty.

M's QET ruling is on RULED_BY_M as M-D65-1: Quantum Energy Teleportation is not
a docket of its own; it is FOLDED INTO DOCKET 66.  Its literature is CITED, not
READ -- nothing in this tree has read those papers.  M's ruling on the finite
Higgs share is M-D65-2: folded into S10's note, not a row.  M's ruling on
DOCKET 67 is M-D65-3: the audit of the external results the board's refusals
rest on is OPENED, to run after DOCKET 65 is seated and before DOCKET 66 (NOT
YET RUN; specthm's DOCKETS_OPENED records it); no row here.  M's ruling on
the paper's caveat (b) is M-D65-4: qualified on P-UNIFORM, a named premise --
a paper edit on M's ruling under M's rule for the paper (M_PAPER_RULE_WORDS,
M's words verbatim from the session, witnessed by the lead; the tree holds no
copy to check them against); the paper's other marked edit on M's ruling is
DOCKET 63's, at the marker paper_d63_marker() READs back from paper/CLAIMS.md
(PAPER_D63_MARKER_LINE) -- the paper's edits are not counted here, the two
markers are named and the reader counts.  Nothing from
DOCKET 65 is pending M.
"""

import contextlib
import io
import math
import os
import re
import sys
import textwrap

import achievable
import address
import bounds
import branelink
import candidates
import certify
import create
import driven
import drivensource
import endpoint
import excite
import fewsterteo
import fluctuation
import foliation
import formation
import higgs
import hpscentre
import latticectc
import linstab
import massform          # DOCKET 65; it asks THIS file only at call time
import noise
import nonstatic
import overturn
import phase1
import qeihps
import stockgate
import throatmass
import tolman
import transit
import warpfolder

#: LEDGER.md sits beside this file, and is found there from ANY working
#: directory.  It was first resolved against the cwd, so --check run from the
#: repository root reported a tracked file missing.
HERE = os.path.dirname(os.path.abspath(__file__))
LEDGER_MD = os.path.join(HERE, "LEDGER.md")

THEOREM, MEASURED, SURVEY, OPEN, WITHDRAWN, REFUSED = (
    "THEOREM", "MEASURED", "SURVEY", "OPEN", "WITHDRAWN", "REFUSED")

#: A THEOREM whose SCOPE was stated wider than it was proved.  The theorem
#: stands; what was wrong was the class it was applied to.  DOCKET 61 needed
#: this and the five statuses had nowhere to put it: WITHDRAWN says the claim
#: fell, and it did not.
NARROWED = "THEOREM-NARROWED"

STATUSES = (THEOREM, NARROWED, MEASURED, SURVEY, OPEN, WITHDRAWN, REFUSED)

# CONSTANTS ASKED, NEVER RETYPED.  Each is read from the module that owns it so
# that a peer moving underneath this file is a --check failure rather than a
# stale sentence.
C_LIGHT = foliation.C_LIGHT                  # m/s,  exact by definition
G_NEWTON = foliation.G_NEWTON                # m^3 kg^-1 s^-2, CODATA 2018
M_SUN = foliation.M_SUN                      # kg,   IAU nominal
PROXIMA_LY = foliation.PROXIMA_LY            # ly,   Gaia DR3 parallax
LAMBDA = overturn.LAMBDA                     # the method equation's coefficient
LY_M = 9.4607304725808e15                    # m per light year, exact (IAU)

#: kg of negative enclosed Misner-Sharp mass per metre of contraction.
#: DERIVED here from two asked constants and nothing else; the figure the tree
#: quotes is 1.348948e26 and the selftest checks this against it.
EXCHANGE_RATE = C_LIGHT ** 2 / (G_NEWTON * LAMBDA)

PROXIMA_M = PROXIMA_LY * LY_M


def required_negative_mass(delta_d_m):
    """kg of negative enclosed mass to contract proper distance by delta_d_m.

    The method equation read the one way it is ever used here.  ASKED, not
    derived: LAMBDA is overturn.py's and the exchange rate is the two constants
    above.  Nothing in this function is this file's own physics.
    """
    return EXCHANGE_RATE * delta_d_m


# ---------------------------------------------------------------------------
# LEFT SIDE -- THE DEMAND.  (row id, claim, status, owner, what would move it)
#
# `owner` names a module and an attribute wherever the claim is pinned as one,
# so `ask()` can fetch it.  Where the owner is a paper rather than a module the
# attribute is None and the row is CITED in its note instead -- those rows are
# counted separately and the selftest says how many there are, because a row
# this file cannot ask is a row this file cannot defend.
# ---------------------------------------------------------------------------

DEMAND = [
    ("D1",
     "Contraction at r requires negative enclosed Misner-Sharp mass, "
     "ansatz-free, in any STATIC spherically symmetric spacetime",
     THEOREM, ("certify", "THEOREM_SCOPE"),
     "a failure of staticity or sphericity -- and D2 removes the first"),

    ("D2",
     "Gamma > 1 in EVERY foliation <=> m < 0.  The RANGE THEOREM: over all "
     "foliations Gamma takes exactly [sqrt(1-2m/R), infinity), so the LOCAL "
     "criterion is gauge and staticity is DELETED rather than weakened",
     THEOREM, ("foliation", "IDENTITY_DISPUTED"),
     "nothing in 4D spherical symmetry; 16 z3 obligations, all unsat"),

    ("D3",
     "The local criterion alone is NOT a scalar, so 'contraction' read off one "
     "slice is a statement about the foliation and not about the spacetime",
     THEOREM, ("driven", "CONTRACTION_IS_A_SCALAR"),
     "nothing; it is the content of D2 read from the other side"),

    ("D4",
     "certify.py's COROLLARY -- and therefore negative enclosed ENERGY -- needs "
     "a REGULAR CENTRE, m(0) = 0.  Reissner-Nordstrom is a counterexample "
     "inside the file's own stated scope, and the integration constant a "
     "regular centre kills IS the central mass",
     THEOREM, ("drivensource", "CERTIFY_COROLLARY"),
     "nothing; it is a hypothesis that was always in force and was unwritten"),

    ("D5",
     "Superluminal travel requires negative energies, with NO staticity, NO "
     "symmetry and NO sphericity, pointwise on the path travelled",
     THEOREM, None,
     "nothing read this pass; Olum PRL 81 3567, CITED"),

    ("D6",
     "There are NO purely spatially averaged quantum inequalities over bounded "
     "regions in 4D Minkowski.  The ball integral at an INSTANT is unbounded "
     "below, so THE MAGNITUDE AXIS CARRIES NO NO-GO",
     THEOREM, None,
     "nothing; Ford, Helfer & Roman PRD 66 124012, CITED, read in full"),

    ("D7",
     "A corridor must HOLD for at least one light-crossing or it transmits "
     "nothing, and the duration QEI rho >= -C/tau^4 refuses exactly that.  The "
     "bound is STATE-INDEPENDENT over Hadamard states, so no branch of any "
     "decomposition escapes it",
     THEOREM, ("bounds", "DURATION_ROUTE_Z"),
     "a matter model outside its hypotheses -- see O1, which is exactly that"),

    ("D8",
     "The pointwise T^r_r test RESTATES certify.py on a strictly SMALLER class "
     "and does not supersede it: it needs tracelessness and a test-field "
     "background where certify.py needs neither",
     THEOREM, ("tolman", "RESTATES_CERTIFY_ON_SMALLER_CLASS"),
     "nothing; the containment is proper and machine-checked"),

    ("D9",
     "A SOURCED background satisfying the pointwise test's hypotheses forces "
     "Minkowski, so the test has content only as a test-field statement",
     THEOREM, ("tolman", "SUPERSEDES_CERTIFY"),
     "nothing; THEOREM X, two independent machine checks"),

    ("D10",
     "Sustaining contraction does NOT force rho < 0.  Witnesses hold it for all "
     "time with rho = 0 exactly and with rho > 0 exactly, NEC satisfied and not "
     "saturated.  What kills the driven route is kinematics, not an energy "
     "condition",
     THEOREM, ("nonstatic", "SUSTAINING_FORCES_NEGATIVE_RHO"),
     "nothing; it is why D7 and not an energy condition is the obstruction"),

    ("D11",
     "The exchange rate: kg of negative enclosed mass per metre of contraction, "
     "from the method equation's own coefficient",
     MEASURED, ("overturn", "LAMBDA"),
     "a re-ruling of LAMBDA, which is a corpus question and not a physics one"),

    ("D12",
     "NO-IN-PRACTICE on the geometric route: four limbs, each proved inside its "
     "own hypotheses.  THE CONJUNCTION IS A SURVEY AND NOT A THEOREM, because "
     "limb one quantifies over ONE field and nothing proves the four hypotheses "
     "exhaust the matter models",
     SURVEY, None,
     "a matter model outside all four sets of hypotheses would break it "
     "without refuting any single limb"),

    ("D13",
     "Classical information travels at <= c IN THE METRIC ITS CARRIER "
     "PROPAGATES IN, and the no-communication theorem closes the entangled "
     "variant.  For a BRANE-CONFINED carrier that metric is the induced metric "
     "and the reconstruction route is EMIGRATION WITHOUT SPEED.  THE ROW IS "
     "NOT A STATEMENT ABOUT A BULK CARRIER: on a brane moving through a "
     "compact extra dimension, bulk null geodesics join brane points the "
     "induced metric calls spacelike, and GKLP's field commutator on M4 x S1 "
     "is non-zero across them",
     NARROWED, None,
     "nothing further -- limb 2 was always intact and limb 1 is now stated "
     "over the class it was proved for.  It is why S5 is a price rather than "
     "a shortcut FOR A BRANE-CONFINED CARRIER, which is the only case it "
     "covers"),

    ("D14",
     "A static spherically symmetric device has NO PARAMETER IN WHICH A "
     "DESTINATION CAN BE WRITTEN: the solution data is (Phi, m) as functions "
     "of r alone, no entry of either is a function of direction, and the "
     "contraction it certifies is identical in every direction.  Addressing "
     "is not un-answered on the priced object, it is UNDEFINED on it",
     THEOREM, ("certify", "THEOREM_SCOPE"),
     "nothing; dL/dtheta = dL/dphi = 0 is machine-checked.  What it costs is "
     "O4: the whole demand side prices an object that cannot have a "
     "destination.  SCOPE FLAGGED BY DOCKET 62: O4 closed on a CYLINDRICAL "
     "object, which has an axis, and an axis supplies a direction and two "
     "ends, not a 3-D destination -- so on the axial object undefinedness "
     "narrows from 'no parameter at all' to 'a one-bit parameter', and what a "
     "full 3-D address requires of a metric is written down nowhere.  The "
     "theorem stands on its own class; the board's use of it moved.  The "
     "Higgs does not supply the missing parameter (S6)"),

    # ----- DOCKET 63: the Higgs at the endpoint.  Owners exactly as ruled. ----
    ("D15",
     "A static displacement of any vacuum with V''(v) = m^2 > 0 returns to v "
     "at asymptotic rate EXACTLY m -- every Mexican hat, any dimension d, "
     "nonlinearly, for any source sign, size or shape, outside its support.  "
     "Proved by an elementary Riccati argument (ruling F1), not by the unread "
     "Levinson/Hartman theorem.  For the Higgs the rate is hbar/(m_h c) = "
     "%.6e m at the READ m_h" % excite.LAMBDA_H_READ_M,
     THEOREM, ("excite", "TAIL_RATE_IS_MASS"),
     "a failure of one of its hypotheses: %s"
     % "; ".join(excite.TAIL_RATE_HYPOTHESES)),

    ("D16",
     "The displacement is ULTRALOCAL: delta phi = -J/m_h^2 locally and "
     "INT G d^3r = 1/m^2, so a displaced vev exists only where its source is "
     "and no arrangement of sources beats the local density",
     THEOREM, ("excite", "DISPLACEMENT_IS_ULTRALOCAL"),
     "a failure of its hypotheses -- linear regime, static, source scale L "
     "large against lambda_h; the error is (lambda_h/L)^2"),

    ("D17",
     "Role 3 at the endpoint -- the Higgs as a source of negative energy -- is "
     "closed for ANY minimally coupled scalar, any potential, any mass: "
     "T_kk = (k.d phi)^2 >= 0.  The obstruction is not the Higgs mass; it "
     "would be just as closed at m_h = 0",
     THEOREM, ("higgs", "MINIMAL_SCALAR_SATISFIES_NEC"),
     "a non-minimal coupling -- which is S4 and O1, both refused"),

    ("D18",
     "m_e -> m_e(1 + eps), alpha fixed and nuclei clamped, is an EXACT "
     "dilation of the Schrodinger and Dirac-Coulomb problems, so a displaced "
     "endpoint does not bind wrong through a_0: the object is its own ruler",
     THEOREM, ("excite", "ELECTRON_MASS_IS_A_RULER"),
     "alpha not held fixed (H1) or finite nuclear size -- the residual "
     "channels, O(eps) through m_p/m_e, which S7 prices"),

    ("D19",
     "A displacement along T1, T2, T3 or Y leaves H+H, every mass and every "
     "derivative-free gauge-invariant local observable unchanged: the flat "
     "directions are INERT",
     THEOREM, ("excite", "FLAT_DIRECTIONS_ARE_INERT"),
     "nothing gauge-invariant, local and derivative-free; a radial "
     "displacement is the control that moves H+H"),

    ("D20",
     "Holding eps costs source 4 rho_EW eps(2-eps)(1-eps)^2 plus field "
     "rho_EW eps^2(2-eps)^2.  At the clock-comparison ORDER eps = %.0e that "
     "is %.6e kg/m^3 of Higgs-derived density, and %.2g (H1) to %.2g (H2) "
     "kg/m^3 of stable matter.  m_h is READ (125.13, captures/PDG-2026.tsv); "
     "G_F is NAMED-NOT-READ, and the figure inherits G_F's status"
     % (excite.EPS_AT_FIXTURE, excite.HOLD_HIGGS_DERIVED_KG_M3_AT_EPS_1E18,
        excite.HOLD_STABLE_KG_M3_AT_EPS_1E18["H1"],
        excite.HOLD_STABLE_KG_M3_AT_EPS_1E18["H2"]),
     MEASURED, ("excite", "HOLD_HIGGS_DERIVED_KG_M3_AT_EPS_1E18"),
     "a cheaper stable neutral source (DOCKET 63 E1, unsettled), the "
     "Yukawa-running correction to the 2/9 source fraction (E10, unsettled), "
     "a READ G_F or m_h, or the H1/H2 choice, which no Standard Model instrument can "
     "make and this file does not"),

    # ----- DOCKET 62: the O3 narrowing, seated as its own THEOREM. ----------
    ("D21",
     "THE FLAT-BULK LATTICE THEOREM: %s.  At rank 1 with a spatial circle the "
     "condition is vacuous, so GKLP's 'no' is FORCED rather than contingent; "
     "at rank >= 2 it holds exactly when the span is spacelike, and the "
     "separating witness e1, e2 has norms %s, %s and a %s sum (%s).  "
     "DOCKET 57's 'two independent routes' -- %s"
     % (latticectc.LATTICE_THEOREM,
        latticectc.WITNESS_NORMS[0], latticectc.WITNESS_NORMS[1],
        latticectc.WITNESS_SPAN, latticectc.WITNESS_NORMS[2],
        latticectc.DOCKET57_TWO_ROUTES),
     THEOREM, ("latticectc", "LATTICE_THEOREM"),
     "a failure of a hypothesis -- %s.  The codimension-one CTC does NOT move "
     "it: %s" % ("; ".join(latticectc.HYPOTHESES),
                 latticectc.CODIM1_CTC_REFUSAL)),

    # ----- the board catching up with the tree: fluctuation.py.  DOCKET 64:
    # noise.py prices the smeared fluctuation in flat space and the row moves
    # OPEN -> SURVEY; the wording it replaces is D22_DOCKET62 (kept). -------
    ("D22",
     "THE SMEARED FLUCTUATION DOES NOT RESTATE THE DEMAND, IN FLAT SPACE.  "
     "fluctuation.py's pointwise T1 stands (Delta' >= 1/2, Delta >= 1/3 for "
     "every zero-mean Gaussian state, z3), and it is sign-blind, so it cannot "
     "be the demand.  For the free minimal scalar in Minkowski (noise.py, "
     "flat model %s), Fewster's sampled energy density is bounded below AS "
     "AN OPERATOR by -C/tau^4 (C1_FLAT_THEOREM = %s).  The demanded density "
     "is therefore the mean of no state and, under H6 (the quantum spectral "
     "measure), the outcome of no measurement.  Vacuum SD_0 = %.6f C/tau^4 "
     "at every tau.  T1 fails under smearing (T1_SURVIVES_SMEARING = %s): "
     "thermal Delta'_f < 1/2 for tau > %.6f beta.  Under the Gaussian "
     "Einstein-Langevin surrogate -- a different reading of 'distribution', "
     "not H6 -- the probability is not zero: with the VACUUM's noise kernel "
     "at b = 1 m it is exp(-10^%.3f), below exp(-10^%d); a state with a "
     "larger noise kernel is not computed (EL_SURROGATE_NONVACUUM_COMPUTED "
     "= %s).  ON THE CORRIDOR THIS IS A %s: H2 fails, (b/l_G)^2 = %.0f, "
     "and the curved decision is %s's"
     % (", ".join(sorted(noise.HYPOTHESES)), noise.C1_FLAT_THEOREM,
        noise.SD0_OVER_C, noise.T1_SURVIVES_SMEARING,
        noise.TAU_STAR_OVER_BETA, noise.EL_VACUUM_LOG10_NEG_LN_P,
        int(math.floor(noise.EL_VACUUM_LOG10_NEG_LN_P)),
        noise.EL_SURROGATE_NONVACUUM_COMPUTED, noise.CORRIDOR_APPLICATION,
        noise.B_OVER_LG_SQUARED, noise.CURVED_PART_CARRIED_BY),
     SURVEY, ("noise", "CORRIDOR_APPLICATION"),
     "%s's absolute QEI evaluated on the corridor: by FFR 1004.0179 note "
     "[18] it decides the distribution question there, with no variance at "
     "all.  The smeared curved variance itself, were it wanted, needs no NEW "
     "renormalisation (Hu & Verdaguer 3.2, READ; "
     "CURVED_VARIANCE_NEEDS_QUARTIC_RENORMALISATION = %s), and its "
     "finiteness is %s.  Or a failure of H3 (%s: %s) -- a "
     "self-adjoint extension other than Friedrichs need not keep the bound"
     % (noise.CURVED_PART_CARRIED_BY,
        noise.CURVED_VARIANCE_NEEDS_QUARTIC_RENORMALISATION,
        noise.CURVED_VARIANCE_FINITENESS, noise.HYPOTHESES["H3"][0],
        noise.HYPOTHESES["H3"][1])),

    # ----- the principle applied (docstring section 4): each of these has an
    # instrument in the tree, so each gets its row now.  DOCKET 62's
    # recommended NEW rows. ------------------------------------------------
    ("D23",
     "THE FIRST TRIP.  transit.py: a channel spanning D required something to "
     "cross D at <= c beforehand -- THE CORRIDOR MUST BE TRAVERSED IN ORDER TO "
     "EXIST.  Its advantage over light is ZERO BY CONSTRUCTION, not by "
     "measurement: transit.py models the channel's arrival as the classical "
     "message at c, because reading the shared state carries nothing alone "
     "(READING_CARRIES_NOTHING_ALONE = %s -- the no-communication theorem), "
     "so advantage_over_light(D) = D/c - D/c at every distance it lists "
     "(%s: %s).  Applied to S5 with no entanglement in it: the "
     "fabricator, the stock survey and the receiver all had to reach the "
     "destination at <= c.  So S5 is an AMORTISATION SCHEME, not a transport "
     "route, with a minimum setup of the light time, %.4g years at Proxima "
     "(the span in light years, foliation.py).  "
     "Whether that setup amortises is OPEN"
     % (transit.READING_CARRIES_NOTHING_ALONE,
        ", ".join(n for n, _d in transit.DISTANCES),
        ", ".join(sorted(set("%.3f" % transit.advantage_over_light(d)
                             for _n, d in transit.DISTANCES))), PROXIMA_LY),
     OPEN, ("transit", "TRAVERSAL_IS_REMOVED"),
     "S5 priced per reconstruction -- DOCKET 56's owed instrument -- set "
     "against the first trip, giving the number of later reconstructions at "
     "which the route beats sending the payload itself at <= c.  Nothing "
     "removes the first trip: transit.py moves the traversal earlier, it does "
     "not delete it"),

    ("D24",
     "FORMATION.  D1-D14 each price a CONFIGURATION, and none prices getting "
     "to it.  create.py: bringing a throat into existence is TOPOLOGY CHANGE, "
     "and, FOR CAUSALLY COMPACT INTERPOLATING SPACETIMES, Geroch and Borde "
     "force causality violation for it kinematically -- '%s'; Borde: '%s' -- "
     "so exotic matter cannot help (EXOTIC_MATTER_HELPS_CREATION = %s).  "
     "Dropping causal compactness is one of Borde's three escapes, and none "
     "stays inside Lorentzian GR without a pathology "
     "(any_escape_stays_in_lorentzian_gr() = %s).  Enlarging an existing throat is a metric "
     "change those theorems say nothing about "
     "(create.theorems_apply_to_enlargement() = %s), but its premise is "
     "unpriced: %s"
     % (create.BORDE, create.BORDE_SINGULARITY,
        create.EXOTIC_MATTER_HELPS_CREATION,
        create.any_escape_stays_in_lorentzian_gr(),
        create.theorems_apply_to_enlargement(), create.ROUTE_COST)
     # DOCKET 64 appends; nothing above is replaced.
     + ".  THE PASSAGE IS PRICED (formation.py, DOCKET 64; F1 THEOREM under: "
     "%s).  Across a sphere the Kodama energy the passage carries is "
     "-m_1(R), the object's own enclosed negative mass, by any route at any "
     "speed; the extra outgoing radial null deficit is -(W_1 - 1)/(2 pi R) "
     "per passage, duration-independent (F2, THEOREM, adding: %s).  "
     "T^{0r} != 0 in the Eulerian (fixed-R) frame at some instant wherever m_1 != 0, with zero net momentum "
     "by symmetry (PHASE1_D4_POINTWISE_DURING_PASSAGE = %s) -- NOT PROPULSION "
     "under phase1.py's D4 as RESTATED ON M'S RULING (RULED_BY_M, M-D64-1).  "
     "Nucleation READ (%s): the neck is "
     "a recipe with free smooth functions (%s); its price has not been "
     "computed (NUCLEATION_PRICED = %s), and whether it is priceable from the "
     "source is %s"
     % ("; ".join(formation.F1_THEOREM),
        "; ".join(h for h in formation.F2_THEOREM
                  if h not in formation.F1_THEOREM),
        formation.PHASE1_D4_POINTWISE_DURING_PASSAGE,
        formation.NUCLEATION_SOURCE,
        ", ".join(formation.NUCLEATION_FREE_FUNCTIONS),
        formation.NUCLEATION_PRICED,
        formation.NUCLEATION_PRICEABLE_FROM_SOURCE),
     OPEN, ("formation", "NUCLEATION_PRICEABLE_FROM_SOURCE"),
     "the nucleation construction COMPUTED -- the neck recipe written out "
     "and integrated (%s, %s in create.py); or an observed throat, priced by "
     "F1 as m_final(R) - m_initial(R) (the find-and-enlarge route: %s); the "
     "surface layer at R_s priced, since every formation.py figure lies on "
     "one side of it; or a passage with U != 0, which is outside F1.  The "
     "wording this replaces is kept (SUPERSEDED_WORDING, DOCKET 64)"
     % (create.NUCLEATION_LITERATURE, create.NUCLEATION_STATUS,
        create.ROUTE_COST)),

    ("D25",
     "THE DESTINATION STOCK GATE.  stock.py derives it and stockgate.py "
     "audits it: %s  The assemblable set is a principal ideal, down-set and "
     "join-closed (stockgate's z3 discharges).  A reference adult (ICRP) "
     "against a CI chondrite binds on %s at %.4g kg of feedstock per kg; the "
     "same payload against a stellar photosphere binds on %s at %.4g kg per "
     "kg.  A "
     "manufactured payload binds on a refractory rarity instead.  S5 cannot "
     "close in either direction while this gate is unchecked at its "
     "destination"
     % ((stockgate.GATE,)
        + stockgate.binding_under("as-composed 59", "CI chondrite")
        + stockgate.binding_under("as-composed 59", "stellar photosphere"))
     # DOCKET 64 appends; the figures above are stockgate's and are NOT
     # re-printed below (formation.py's [W1]: over-representation).
     + ".  DOCKET 64 (formation.py): %s.  The aperture search covered "
     "'aperture' and its synonyms; %d files hit (%s among them) and none "
     "gives the arrival aperture a value (formation.APERTURE_SEARCH).  "
     "Survey: condensed body found = %s (%s); "
     "confirmed reservoir = %s; primitive measured = %s; accessible "
     "measured = %s; the data constrain bodies = %s"
     % (formation.D25_VERDICT,
        len(set(formation.APERTURE_HITS)
            | set(formation.APERTURE_SYNONYM_HITS)),
        " and ".join(sorted(
            f for f in ("ledger.py", "stockgate.py")
            if f in formation.APERTURE_HITS)) or "neither this file nor "
        "stockgate.py",
        formation.SURVEY_CONDENSED_BODY_FOUND,
        formation.SURVEY_CONDENSED_BODY,
        formation.SURVEY_CONFIRMED_RESERVOIR,
        formation.SURVEY_PRIMITIVE_MEASURED,
        formation.SURVEY_ACCESSIBLE_MEASURED,
        formation.SURVEY_CONSTRAINS_BODIES),
     OPEN, ("stockgate", "GATE"),
     "the destination's arrival aperture surveyed for a condensed, "
     "primitive body holding M(p,s) x m_payload of accessible mass -- a "
     "snow-line condition, so a condition on orbital radius at the "
     "destination, which the arrival coordinate does not yet carry.  "
     "Separation energy is not priced by stockgate.py and no figure here is "
     "an energy.  After DOCKET 64: an instrument that gives the arrival "
     "aperture a value, as an orbital-radius band at the destination; the "
     "formation-epoch disc T(a), P(a) there (NOT-FOUND, "
     "formation.SNOWLINE_SEARCH); and, for the condensed body the survey "
     "does name, its primitive (volatile) state and its accessibility "
     "measured"),

    # ----- DOCKET 64: linearised stability, opened by the docket that built
    # its instrument (docstring section 4).  Text ASKED of linstab.py. ------
    ("D26",
     "%s.  inf beta^2_crit over m > 0 = %s (classical radial sector: %s)"
     % (linstab.D26_CLAIM, linstab.BETA2_CRIT_INFIMUM,
        linstab.CLASSICAL_RADIAL_STATUS),
     OPEN, ("linstab", "SEMICLASSICAL_EVALUABLE_ON_DEMAND"),
     linstab.D26_ANSWERED_BY),
]

# ----- DOCKET 65 (massform.py), seated on M's ruling "Seat as proposed". -----

#: massform's rows as it states them, by id -- ASKED, never retyped.
PROPOSED = dict((r[0], r) for r in massform.PROPOSED_ROWS)


def _proposed_status(rid):
    """A proposed row's status, which must be one of this board's words: a
    status outside the vocabulary raises rather than seating a new word."""
    st = PROPOSED[rid][3]
    if st not in STATUSES:
        raise ValueError("massform proposes %s as %r, not a ledger status"
                         % (rid, st))
    return st


DEMAND += [(rid, PROPOSED[rid][2], _proposed_status(rid), PROPOSED[rid][4],
            PROPOSED[rid][5]) for rid in ("D27", "D28", "D29")]

#: THE WORDING DOCKET 64 REPLACED ON DEMAND ROWS, kept for SUPERSEDED_WORDING.
#: Typed here because it is HISTORY -- what the board said -- and not a result;
#: the one computed clause (create.py's) is still asked.
D22_DOCKET62 = (
    "THE SEMICLASSICAL DEBT.  Every demand row is a demand on <rho> inside "
    "G = 8 pi G <T>, and Kuo & Ford's measure of that equation's error, "
    "Delta, is re-derived exactly in flat space: the pointwise measure is "
    "recomputed two independent ways, and Delta >= 1/3 is PROVED (z3) for "
    "EVERY zero-mean Gaussian state, without Kuo & Ford's diagonal "
    "assumption.  The pointwise Delta is sign-blind -- it condemns thermal "
    "radiation too -- so it cannot be the demand.  THE SMEARED PRICE AT THE "
    "CORRIDOR'S OWN SCALES IS OPEN [status OPEN, owner "
    "fluctuation.PRICES_THE_CORRIDOR] || the SMEARED fluctuation priced at "
    "the corridor's scales -- the width b and Fewster's sampling time -- "
    "which needs the curved-space renormalisation of quartic operator "
    "products Kuo & Ford said did not exist.  If it is of order one there, "
    "the demand column must be written about a distribution rather than an "
    "expectation")
D24_ANSWER_DOCKET62 = (
    "[what would move it] the nucleation construction run rather than named "
    "(%s, %s here), or the 'find one and enlarge it' route priced; and for "
    "any configuration that changes no topology, the passage from flat "
    "space to it priced at all -- no instrument in the tree does that yet "
    "[owner create.NUCLEATION_STATUS]"
    % (create.NUCLEATION_LITERATURE, create.NUCLEATION_STATUS))

#: THE PRINCIPLE'S OTHER HALF (docstring section 4): a question with no
#: instrument is opened by the docket that builds one.  (question, why it has
#: no row yet, what opens it.)  Printed in LEDGER.md so a deferral is visible.
WAITS_FOR_ITS_INSTRUMENT = []

#: WHAT LEFT WAITS_FOR_ITS_INSTRUMENT, AND HOW.  (question, the docket that
#: built its instrument, the row it became, why it waited -- as first written.)
#: Kept so the deferral stays visible after it ended.
OPENED_FROM_WAITING = [
    ("linearised stability", "DOCKET 64", "D26",
     "no instrument asks it.  Anderson-Molina-Paris-Mottola state the validity "
     "criterion in print (no gauge-invariant perturbation unbounded in time), "
     "and the literature is split on Minkowski itself (AMM: infrared-stable; "
     "Galanda-Meda-Murro-Pinamonti-Schmid 2604.01047: linearly unstable, "
     "attributed to the renormalisation constants) -- as DOCKET 62's ruling "
     "reports them, not read here.  stability.py asks the "
     "CLASSICAL radial stability of a shell, not this"),
]

#: QUESTIONS THAT NEED M'S RULING, recorded and NOT applied.  This file edits no
#: peer and changes no requirement; it records the question so the board shows
#: it.  (id, question, why it is asked -- with the owner's computed values --,
#: the restatement proposed, and what waits on it.)
#: DOCKET 65's one pending question (M-D65-2, the finite Higgs share) has been
#: RULED by M and is on RULED_BY_M; nothing is pending.
PENDING_RULINGS = []

#: M'S OWN WORDS FOR DOCKET 65's RULINGS, each held ONCE and interpolated into
#: every cell that prints it, so no cell can carry a variant under the label
#: "verbatim" (the selftest extracts every printed copy and compares).
M_D65_1_WORDS = ("consider the idea that the introduction of information into a "
                 "space that never previously contained it would be considered "
                 "exotic matter")
M_D65_1_ANSWER = "Fold into D66"
#: The QET literature as it was named to M, CITED, not READ -- held once.
M_D65_1_LITERATURE = ("Hotta 2008; Funai & Martin-Martinez arXiv:1701.03805; "
                      "Ikeda arXiv:2301.02666; review arXiv:2505.04689; "
                      "arXiv:2506.19878")
#: M-D65-3 (DOCKET 67): the question exactly as it was put to M, M's words
#: verbatim -- they hold apostrophes, so every cell quotes them in double
#: quotes -- and M's answer verbatim.  PROVENANCE: M_D65_3_WORDS is verbatim
#: from the session, witnessed by the lead against the transcript; the tree
#: holds no copy of M's message, so nothing here can verify the constant
#: against M -- the selftest checks every printed copy against it, no more.
M_D65_3_QUESTION = ("Should I open a docket auditing the external results the "
                    "board's refusals rest on (theorem / measurement / "
                    "extrapolation; hypotheses, the data each used, re-derived "
                    "or machine-checked, graded STANDS / NARROWED / WRONG / "
                    "DATA-DEPENDENT)? If so, when?")
M_D65_3_WORDS = ("I didn't expect proving warp theory travel easy, but I'm "
                 "starting suspect that some of the previously established math "
                 "from outside art may be inaccurate or incomplete, or even "
                 "wrong. My justification is that some previous physicists may "
                 "have all lacked certain data")
M_D65_3_ANSWER = "After D65, before D66"
#: M-D65-3's ruling cell, a TEMPLATE over (M_D65_3_ANSWER, M_D65_3_WORDS): the
#: selftest checks the seated cell EQUALS the template filled from the
#: constants, so no verdict on DOCKET 67 can be typed beside them.
M_D65_3_RULING_T = ("RULED BY M: OPEN IT -- M's answer: '%s'.  M's words, "
                    'verbatim: "%s".  APPLIED: DOCKET 67 is opened on '
                    "specthm's DOCKETS_OPENED, NOT YET RUN; no row here")
#: M-D65-3's `why` cell, a TEMPLATE filled by m_d65_3_why() from the owners'
#: own records (fluctuation.py, massform.py): the characterisation is theirs,
#: the figures are asked, and the lead-in's COUNTS are asked too -- the
#: discrepancies fluctuation.py records are COUNTED from its KF flags
#: (fluctuation_discrepancies()), the divergences massform.py records are the
#: sentences under its own heading (massform_divergences()), the nouns are
#: regexed from the owners ('discrepancies', 'refuted', 'typographical',
#: 'divergences'), and the '2 of' figures are len() of the tuples naming the
#: items the cell details.  The framing is SCOPED to what the cell cites, not
#: a project-wide total (hpscentre.py counts three disagreements of its own).
#: Precedent: hpscentre.py withdrew a typed 'two misprints and two errors'
#: for its asked 'three disagreements'.
M_D65_3_WHY_ITEMS_FLUCT = ("KF_CLAIM_NEGATIVE_MEANS_DELTA_GT_1", "KF_341_HALF_IS_TYPOGRAPHICAL")
M_D65_3_WHY_ITEMS_MASS = ("RS96 eq. (2.8)", "Tye-Wong p.2 pairing")
M_D65_3_WHY_T = (
    'M\'s words, verbatim: "%s" (verbatim from the session, witnessed by the '
    "lead; the tree holds no copy to check them against).  Of what this project "
    "has recorded against outside results, the items whose owners expose flags "
    "asked here: %d of the %d %s fluctuation.py records against a preprint "
    "version (its own words: the inequality after (3.8) %s -- \"%s\" -- and "
    "(3.41)'s 1/2 \"%s\"; the rest, %d KF_*_IS_EXACT flags False), and %d of "
    "the %d %s massform.py records under its own heading.  "
    "fluctuation.py, against arXiv %s -- the journal version, %s, is %s "
    "(fluctuation.JOURNAL_VERSION_READ = %s), and its own clause holds: '%s': "
    "Kuo & Ford's printed 'rho < 0 => Delta > 1' is %s (fluctuation.KF_CLAIM_"
    "NEGATIVE_MEANS_DELTA_GT_1 = %s) and the 1/2 their eq. (3.41) prints where "
    "1/4 holds is %s (fluctuation.KF_341_HALF_IS_TYPOGRAPHICAL = %s).  "
    "massform.py, under its own heading '%s': Rubakov-Shaposhnikov's eq. (2.8) "
    "prints 10^%.0f at alpha_W = 1/%g where the arithmetic gives 10^%.2f "
    "(massform.RS96_PRINTED_LOG10, RS96_ALPHA_INV, log10_suppression); "
    "Tye-Wong's p.2 pairing prints 10^%.0f at alpha_W ~ 1/%g where the "
    "arithmetic gives 10^%.2f, %.2f decades off, and their p.7 pairing, "
    "1/%g, gives 10^%.2f, which %s the printed figure (massform.TW_PRINTED_"
    "LOG10, TW_ALPHA_INV, log10_suppression).  Kuo & Ford's qualitative "
    "conclusion %s (fluctuation.KF_QUALITATIVE_CONCLUSION_SURVIVES = %s) and "
    "%s (fluctuation.LEDGER_ROW_MOVES = %s)")
#: M-D65-4: the paper's caveat (b).  The question exactly as it was put to M
#: and M's answer verbatim -- both verbatim from the session, witnessed by
#: the lead; the tree holds no copy to check them against.  The clause the paper carries is
#: held once and READ back from paper/CLAIMS.md by paper_caveat_b_faults().
M_D65_4_QUESTION = ("The paper's caveat (b) states the Higgs vacuum's uniformity "
                    "as fact; the tree now carries it as a named premise "
                    "(P-UNIFORM). Does that count as a finding that changes the "
                    "paper?")
M_D65_4_ANSWER = "Yes, qualify it (Recommended)"
PAPER_CAVEAT_B_LINE = 7228
PAPER_CAVEAT_B_CLAUSE = ("on P-UNIFORM, a named premise (`massform.P_UNIFORM_STATUS`; "
                         "DOCKET 65)")
PAPER_CAVEAT_B_HEAD = "- **(b) It is uniform where nothing sources it**"
#: M's RULE FOR THE PAPER, M's words verbatim.  PROVENANCE: verbatim from the
#: session, witnessed by the lead; the tree holds no copy to check them
#: against.  M said it BEFORE DOCKET 63's paper edit (commit 524ccae,
#: 2026-09-24, applied on M's ruling under this same rule), which the paper
#: marks at PAPER_D63_MARKER_LINE -- the tree witnesses that marker by READING
#: it (paper_d63_marker()), so the DOCKET 65 edit is not the paper's only
#: edit on M's ruling: the paper carries two marked edits on M's ruling, and
#: this file names both and counts neither.
M_PAPER_RULE_WORDS = ("the paper is finalized and in the website now. No further "
                      "edit will be made to it unless a finding changes any of the "
                      "already existing paper")
#: paper/CLAIMS.md's DOCKET 63 marker starts on this line and runs to the
#: close of its parenthesis (two lines in the paper); both fragments
#: '(Corrected on M's ruling:' and 'DOCKET 63' must sit inside the one marker,
#: and the regex, never a typed copy, supplies the quoted text.
PAPER_D63_MARKER_LINE = 7233
PAPER_D63_MARKER_RE = re.compile(r"\(Corrected on M's ruling:.*?DOCKET 63\.\)", re.S)
#: M-D65-4's ruling cell, a TEMPLATE over (M's answer, the caveat line and
#: clause, M's rule for the paper, the DOCKET 63 marker's lines and text):
#: the paper's edits on M's ruling are NAMED by their markers, never counted.
M_D65_4_RULING_T = ("RULED BY M: YES, QUALIFY IT -- M's answer: '%s'.  APPLIED: "
                    'paper/CLAIMS.md:%d caveat (b) carries "%s" -- a paper edit on '
                    "M's ruling under M's rule for the paper (\"%s\", verbatim from "
                    "the session, witnessed by the lead); the paper's other marked "
                    "edit on M's ruling is DOCKET 63's (paper/CLAIMS.md:%s: \"%s\")")
M_D65_4_UNBLOCKS_T = ("nothing; M's rule for the paper stands (\"%s\", verbatim from "
                      "the session, witnessed by the lead)")
#: M-D65-4's `why` cell, a TEMPLATE over (the caveat line, massform's asked
#: status): the selftest checks the seated cell EQUALS it, so no verdict on
#: the paper can be typed beside the finding.
M_D65_4_WHY_T = ("The completeness lens's finding: paper/CLAIMS.md:%d caveat (b) "
                 "stated 'It is uniform where nothing sources it' as fact; massform "
                 "seats it as P-UNIFORM (massform.P_UNIFORM_STATUS = %s).  The "
                 "question and M's answer are verbatim from the session, witnessed "
                 "by the lead; the tree holds no copy to check them against")
#: M-D65-2's question exactly as it was put to M, and M's answer verbatim.
M_D65_2_QUESTION = ("The finite Higgs share (how much of atomic mass the Higgs "
                    "gives with the field switched off entirely): keep it as its "
                    "own open row O8, or record it inside S10's note as the "
                    "approved proposal had it?")
M_D65_2_ANSWER = "Fold into S10 (Recommended)"
#: Two fragments of the option M chose, as it was described to M (verbatim).
M_D65_2_OPTION = ("an open item inside S10's note, not a separate row",
                  "It stays a named candidate for a future docket")

def _owner_phrase(doc, pattern, owner):
    """A phrase READ out of an owner's own docstring by regex, never retyped;
    raises if the owner no longer says it."""
    m = re.search(pattern, " ".join(doc.split()))
    if not m:
        raise ValueError("%s no longer records '%s'" % (owner, pattern))
    return m.groups() if m.re.groups > 1 else m.group(1)


def fluctuation_discrepancies():
    """The discrepancies fluctuation.py records against the preprint version,
    COUNTED from its module namespace: every KF_*_IS_EXACT flag that is False,
    plus KF_CLAIM_NEGATIVE_MEANS_DELTA_GT_1 False, plus
    KF_341_HALF_IS_TYPOGRAPHICAL True.  Returns (total, not-exact count)."""
    not_exact = sum(1 for k, v in vars(fluctuation).items()
                    if k.startswith("KF_") and k.endswith("_IS_EXACT") and v is False)
    total = (not_exact + (fluctuation.KF_CLAIM_NEGATIVE_MEANS_DELTA_GT_1 is False)
             + (fluctuation.KF_341_HALF_IS_TYPOGRAPHICAL is True))
    return total, not_exact


def massform_divergences():
    """[sentence] of the paragraph under massform.py's own heading
    'DIVERGENCES FROM THE SOURCES, RECORDED AND NOT REPAIRED', split by regex
    at a full stop followed by whitespace; the owner's count is len()."""
    m = re.search(r"DIVERGENCES FROM THE SOURCES, RECORDED AND NOT REPAIRED\.\s*"
                  r"(.*?)\n[ \t]*\n", massform.__doc__, re.S)
    if not m:
        raise ValueError("massform.py no longer carries its divergences paragraph")
    return [s for s in re.split(r"(?<=\.)\s+", " ".join(m.group(1).split())) if s]


def m_d65_3_why():
    """M-D65-3's `why` cell, built from the owners' own records: the counts
    and nouns of the lead-in (fluctuation_discrepancies(),
    massform_divergences(), the owners' own words by regex), the preprint
    version fluctuation.py checked and its clause on the journal version, its
    two KF flags; massform.py's own heading and the two divergences the cell
    details, with Tye-Wong's p.7 pairing printed beside the p.2 one; and
    fluctuation.py's balancing verdict, asked of its flags."""
    n_fluct, n_not_exact = fluctuation_discrepancies()
    n_mass = len(massform_divergences())
    with open(fluctuation.__file__, encoding="utf-8") as fh:
        fluct_src = fh.read()
    discrepancies = _owner_phrase(
        fluctuation.__doc__, r"the (discrepancies) above are against v1", "fluctuation.py")
    refuted = _owner_phrase(
        fluct_src, r"KF_CLAIM_NEGATIVE_MEANS_DELTA_GT_1 = False\s+# (refuted)",
        "fluctuation.py")
    typographical = _owner_phrase(
        " ".join(k for k in vars(fluctuation) if k.startswith("KF_")),
        r"KF_341_HALF_IS_(TYPOGRAPHICAL)", "fluctuation.py").lower()
    false_by_z3 = "%s by %s" % _owner_phrase(
        fluctuation.__doc__, r"that is (FALSE), and (z3) finds the counterexample",
        "fluctuation.py")
    divergences = _owner_phrase(
        massform.__doc__, r"(DIVERGENCES) FROM THE SOURCES, RECORDED AND NOT REPAIRED",
        "massform.py").lower()
    preprint = _owner_phrase(fluctuation.SOURCE, r"(gr-qc/\d+ v\d)", "fluctuation.SOURCE")
    journal, jstatus = _owner_phrase(
        fluctuation.__doc__,
        r"The published version, (Phys\. Rev\. D 47, 4510 \(1993\)), is ([A-Z-]+)",
        "fluctuation.py")
    if (jstatus == "NAMED-NOT-READ") == bool(fluctuation.JOURNAL_VERSION_READ):
        raise ValueError("fluctuation.py's docstring and JOURNAL_VERSION_READ disagree")
    clause = _owner_phrase(
        fluctuation.__doc__,
        r"(MUST NOT be quoted as errors in the journal version until it is read)",
        "fluctuation.py")
    heading = _owner_phrase(
        massform.__doc__, r"(DIVERGENCES FROM THE SOURCES, RECORDED AND NOT REPAIRED)",
        "massform.py")
    tw_p2 = massform.log10_suppression(1.0 / massform.TW_ALPHA_INV[1])
    tw_p7 = massform.log10_suppression(1.0 / massform.TW_ALPHA_INV[0])
    return M_D65_3_WHY_T % (
        M_D65_3_WORDS,
        len(M_D65_3_WHY_ITEMS_FLUCT), n_fluct, discrepancies, false_by_z3, refuted,
        typographical, n_not_exact, len(M_D65_3_WHY_ITEMS_MASS), n_mass, divergences,
        preprint, journal, jstatus, fluctuation.JOURNAL_VERSION_READ,
        clause,
        ("FALSE by z3" if not fluctuation.KF_CLAIM_NEGATIVE_MEANS_DELTA_GT_1
         else "NOT refuted, AGAINST fluctuation.py's record"),
        fluctuation.KF_CLAIM_NEGATIVE_MEANS_DELTA_GT_1,
        ("typographical" if fluctuation.KF_341_HALF_IS_TYPOGRAPHICAL
         else "NOT typographical, AGAINST fluctuation.py's record"),
        fluctuation.KF_341_HALF_IS_TYPOGRAPHICAL,
        heading,
        massform.RS96_PRINTED_LOG10, massform.RS96_ALPHA_INV,
        massform.log10_suppression(1.0 / massform.RS96_ALPHA_INV),
        massform.TW_PRINTED_LOG10, massform.TW_ALPHA_INV[1], tw_p2,
        abs(tw_p2 - massform.TW_PRINTED_LOG10),
        massform.TW_ALPHA_INV[0], tw_p7,
        ("rounds to" if round(tw_p7) == massform.TW_PRINTED_LOG10
         else "does NOT round to"),
        # Built from the owner's flags, so a flip moves the sentence.
        ("SURVIVES" if fluctuation.KF_QUALITATIVE_CONCLUSION_SURVIVES
         else "does NOT survive, AGAINST fluctuation.py's record"),
        fluctuation.KF_QUALITATIVE_CONCLUSION_SURVIVES,
        ("no ledger row moves" if not fluctuation.LEDGER_ROW_MOVES
         else "a ledger row MOVES, AGAINST fluctuation.py's record"),
        fluctuation.LEDGER_ROW_MOVES)


def _paper_lines(path=None):
    path = (os.path.join(os.path.dirname(os.path.abspath(__file__)), "paper", "CLAIMS.md")
            if path is None else path)
    with open(path, encoding="utf-8") as fh:
        return fh.read().split("\n")


def paper_d63_marker(lines=None):
    """(lines, text) of the paper's DOCKET 63 marker, READ from paper/CLAIMS.md
    by PAPER_D63_MARKER_RE starting at PAPER_D63_MARKER_LINE: 'lines' is
    '7233-7234' as the marker spans them, 'text' the marker itself with its
    whitespace joined.  Raises if the marker is not there: the tree witnesses
    it only by reading it."""
    lines = _paper_lines() if lines is None else lines
    tail = lines[PAPER_D63_MARKER_LINE - 1:PAPER_D63_MARKER_LINE + 3]
    m = PAPER_D63_MARKER_RE.search("\n".join(tail))
    if not m or "\n" in "\n".join(tail)[:m.start()]:
        raise ValueError("paper/CLAIMS.md:%d does not start the DOCKET 63 marker "
                         "'(Corrected on M's ruling: ... DOCKET 63.)'"
                         % PAPER_D63_MARKER_LINE)
    end = PAPER_D63_MARKER_LINE + "\n".join(tail)[:m.end()].count("\n")
    span = ("%d" % PAPER_D63_MARKER_LINE if end == PAPER_D63_MARKER_LINE
            else "%d-%d" % (PAPER_D63_MARKER_LINE, end))
    return span, " ".join(m.group(0).split())


def paper_d63_faults(lines=None):
    """[fault] where the paper no longer carries DOCKET 63's marker at
    PAPER_D63_MARKER_LINE with both fragments inside it."""
    try:
        _span, text = paper_d63_marker(lines)
    except ValueError as e:
        return [str(e)]
    return [f for f in ("marker lacks '(Corrected on M's ruling:'"
                        if "(Corrected on M's ruling:" not in text else "",
                        "marker lacks 'DOCKET 63'" if "DOCKET 63" not in text else "")
            if f]


def m_d65_4_ruling():
    """M-D65-4's ruling cell: M_D65_4_RULING_T filled from M's answer, the
    caveat's line and clause, M's rule for the paper and the DOCKET 63 marker
    READ back from the paper -- both of the paper's marked edits on M's ruling
    named, neither counted."""
    try:
        span, text = paper_d63_marker()
    except ValueError as e:
        # The board still imports; the selftest goes red on paper_d63_faults().
        span, text = "%d" % PAPER_D63_MARKER_LINE, "MARKER NOT FOUND -- %s" % e
    return M_D65_4_RULING_T % (M_D65_4_ANSWER, PAPER_CAVEAT_B_LINE, PAPER_CAVEAT_B_CLAUSE,
                               M_PAPER_RULE_WORDS, span, text)


def m_d65_4_why():
    """M-D65-4's `why` cell, M_D65_4_WHY_T filled from the caveat's line and
    massform's asked status."""
    return M_D65_4_WHY_T % (PAPER_CAVEAT_B_LINE, massform.P_UNIFORM_STATUS)


def paper_caveat_b_line(path=None):
    """paper/CLAIMS.md's line PAPER_CAVEAT_B_LINE, READ from the file."""
    path = (os.path.join(os.path.dirname(os.path.abspath(__file__)), "paper", "CLAIMS.md")
            if path is None else path)
    with open(path, encoding="utf-8") as fh:
        lines = fh.read().split("\n")
    return lines[PAPER_CAVEAT_B_LINE - 1]


def paper_caveat_b_faults(line=None):
    """[fault] where the paper's caveat (b) (paper/CLAIMS.md:PAPER_CAVEAT_B_LINE)
    does not carry the clause M-D65-4 applied, or still states the premise as
    fact (the wording as it stood: 'It is uniform where nothing sources it.**
    The same inside')."""
    line = paper_caveat_b_line() if line is None else line
    bad = []
    if not line.startswith(PAPER_CAVEAT_B_HEAD):
        bad.append("line %d is not caveat (b)" % PAPER_CAVEAT_B_LINE)
    if PAPER_CAVEAT_B_CLAUSE not in line:
        bad.append("caveat (b) does not carry '%s'" % PAPER_CAVEAT_B_CLAUSE)
    if "It is uniform where nothing sources it.**" in line:
        bad.append("caveat (b) states the premise as fact (the wording as it stood)")
    return bad


#: DOCKET 65's seated row ids, built from massform.PROPOSED_ROWS (the rows,
#: not the S10 (open) item or the S5 append), for M-S1A-P1's unblocks cell.
D65_SEATED_IDS = ", ".join(r[0] for r in massform.PROPOSED_ROWS
                           if re.fullmatch(r"[DS]\d+", r[0]))

#: QUESTIONS M HAS RULED ON, same shape, kept so the ruling has its question.
#: The last two fields now read: what M ruled, and what it unblocks.
RULED_BY_M = [
    ("M-D64-1",
     "phase1.py's D4 (not this board's D4): restate '%s' for the process?"
     % phase1.D4_AS_FIRST_WRITTEN,
     "phase1.py classes any momentum flux as PROPULSION (is_transition with a "
     "momentum flux and every other condition met returns %s).  formation.py "
     "shows every U = 0 passage from flat space has T^{0r} != 0 at some "
     "instant wherever m_1 != 0 (PHASE1_D4_POINTWISE_DURING_PASSAGE = %s; "
     "THEOREM under F1's hypotheses), with zero net momentum by symmetry.  "
     "Kept pointwise for the process, D4 makes every U = 0 formation "
     "propulsion by phase1's own classifier"
     % (phase1.is_transition(True, True, True, True, True),
        formation.PHASE1_D4_POINTWISE_DURING_PASSAGE),
     "RULED BY M: RESTATE IT, as DOCKET 64 ruling D.2 proposed -- (i) T^{0i} = 0 "
     "in each configuration g_s; (ii) zero NET momentum (no thrust) across the "
     "passage between them.  APPLIED in phase1.py (D4_RESTATED_ON_M_RULING = %s); "
     "a device that thrusts still fails D4 (ii) (is_transition = %s), and a "
     "transient flux with zero net momentum does not (is_transition = %s)"
     % (phase1.D4_RESTATED_ON_M_RULING,
        phase1.is_transition(False, True, True, True, True, net_momentum=True),
        phase1.is_transition(False, True, True, True, True, passage_flux=True)),
     "step 1a, the specification theorem, may now state D4"),

    # M's five rulings on specthm.py's PENDING FOR M (step 1a review).  M's
    # words are quoted; what is applied, and what is opened instead, is said.
    ("M-S1A-P1",
     "Is the seat (specthm's object S) required to contract?",
     "a positive lens mass lengthens proper distance: contraction iff m < 0 "
     "(certify.theorem_holds() = %s), so S-1's witness does not contract"
     % certify.theorem_holds(),
     "RULED BY M: NO, S IS NOT REQUIRED TO CONTRACT -- M's words: 'I would "
     "imagine the seat is an expansion.'  APPLIED: no contraction requirement "
     "binds S.  M's mechanism -- 'As soon as the "
     "information hits the seat, it triggers the higgs field, and atomic mass "
     "forms', with 'If the elements required for seating are present, then the "
     "conditions for a higgs field or something like it are also present' -- is "
     "NOT applied: M ruled it be TESTED AS A DOCKET (DOCKET 65), against D15, "
     "D16, S9 and a full energy and conservation-law account",
     "S-1 stands NONEMPTY with no contraction requirement; DOCKET 65 opens.  "
     "DOCKET 65 has run: %s (massform.py)" % D65_SEATED_IDS),

    ("M-S1A-P2",
     "Is aimability binding (DOCKET 62's R5)?",
     "D14 proves the destination UNDEFINED on a static spherically symmetric "
     "device (ledger D14 %s); no ruling had made aimability a requirement"
     % [r[2] for r in DEMAND if r[0] == "D14"][0],
     "RULED BY M: YES, NOT SOLE -- 'aiming is definitely part of it, but it "
     "doesn't have to be the only function.'  CLARIFIED BY M: the device's "
     "geometry must single out a POINT, not a sphere, and a subsystem may supply "
     "it -- 'consider the device shape a cylinder.  The idea is the user aims "
     "the device, the corridor is like another agent that verifies it.'  "
     "APPLIED: aimability is a REQUIRED function (necessary, not sufficient) of "
     "the device's whole geometry",
     "specthm imposes aimability on C; with D14 every static spherically "
     "symmetric member fails it"),

    ("M-S1A-P3",
     "Is a closed causal curve, or a Borde pathology, disqualifying?",
     "create.py reads Geroch and Borde: causally compact topology change forces "
     "causality violation with no matter assumption "
     "(GEROCH_NEEDS_MATTER_ASSUMPTION = %s), and no escape stays in Lorentzian "
     "GR without a pathology (any_escape_stays_in_lorentzian_gr() = %s)"
     % (create.GEROCH_NEEDS_MATTER_ASSUMPTION,
        create.any_escape_stays_in_lorentzian_gr()),
     "RULED BY M: BOTH readings of 'these are defects' -- (i) a closed causal "
     "curve or a Borde pathology DISQUALIFIES, and CLARIFIED BY M it does so AT "
     "THE SEAT ONLY: 'My ruling refers to the seat/destination.  Singular occurs "
     "in the throat where the geometry is compressed to binary information, and "
     "then push to the seat'.  APPLIED at the seat; a singular throat is not "
     "disqualified.  (ii) topological defects are candidate SEATING SITES "
     "('Seating occurs in a place where matter can occur but not in its "
     "original geometric form'): NOT applied, opened as DOCKET 66, with M's "
     "throat-compression mechanism",
     "the seat of every object must be free of a closed causal curve and a "
     "pathology; the throat-creation classes stay OPEN; DOCKET 66 opens"),

    ("M-S1A-P4",
     "Is phase1's D3 read per R1 (pointwise invariant contraction)?",
     "phase1's D3 is a slice statement and a slice statement is gauge; the "
     "anchor lemma does not close it (foliation.NONSTATIC_ANCHOR_CLOSES_D3 = %s)"
     % foliation.NONSTATIC_ANCHOR_CLOSES_D3,
     "RULED BY M: RUN BOTH AND COMPARE -- 'this can go either way according to "
     "the math, so we should run both scenarios and compare. Maybe its a "
     "combination of the two.'  APPLIED: specthm runs three readings -- R1 "
     "pointwise, phase1's slice D3 literally, and net contraction along the "
     "static slice between fixed places (the combination)",
     "specthm prints what T admits under each reading, side by side"),

    ("M-S1A-P5",
     "For the reconstruction route: what is specified, at what fidelity, "
     "classical or quantum?",
     "DOCKET 62's R11 note recorded three rulings unmade; transit.py already "
     "holds that teleportation is a move, not a copy "
     "(IT_IS_A_MOVE_NOT_A_COPY = %s), consumes its channel "
     "(CHANNEL_IS_CONSUMED_BY_USE = %s), carries no substance "
     "(CARRIES_SUBSTANCE = %s) and does not beat light (BEATS_LIGHT = %s)"
     % (transit.IT_IS_A_MOVE_NOT_A_COPY, transit.CHANNEL_IS_CONSUMED_BY_USE,
        transit.CARRIES_SUBSTANCE, transit.BEATS_LIGHT),
     "RULED BY M: BOTH, QUANTUM FIRST -- 'both. Quantum first, which should "
     "derive the classical.'  APPLIED: the specification is a quantum state; "
     "the classical specification is to be derived from it, and no derivation "
     "exists yet",
     "R11 is stated on a quantum specification; transit.py's four results bind "
     "it IF it is carried by teleportation as an unknown quantum state"),

    # M's ruling at DOCKET 65's seating.  M's words are quoted verbatim; the
    # literature is CITED as the question was put, and nothing here has READ it.
    # PROVENANCE: the question's parenthetical is exactly the question as the
    # lead put it to M -- verbatim from the session, witnessed by the lead
    # against the transcript; the tree holds no copy and cannot verify it.
    ("M-D65-1",
     "Should Quantum Energy Teleportation (information arriving at the "
     "destination creates a local negative-energy region there) be tested as "
     "its own docket?",
     "M's words, verbatim: '" + M_D65_1_WORDS + "'.  The question's "
     "parenthetical is the question's description as put to M, not READ.  The "
     "literature anchor, CITED, not READ: " + M_D65_1_LITERATURE,
     # The ruling cell is the one LEDGER.md and the report print, so M's words
     # and the literature's status are carried here too, not only in `why` --
     # from the SAME constants, so the two copies cannot differ.
     "RULED BY M: FOLD INTO DOCKET 66 -- M's answer: '" + M_D65_1_ANSWER + "'.  "
     "M's words, verbatim: '" + M_D65_1_WORDS + "'.  The QET literature ("
     + M_D65_1_LITERATURE + ") is CITED, not READ; the question's parenthetical "
     "is the question's description as put to M, not READ.  APPLIED: no "
     "separate docket and no row; QET is to be tested inside DOCKET 66 (NOT "
     "YET RUN)",
     "DOCKET 66 (NOT YET RUN) is to test QET beside seating at a topological "
     "defect"),

    # M's second ruling at DOCKET 65's seating.  The seating had opened the
    # finite share as its own row, O8; the question was put to M as below.
    ("M-D65-2",
     M_D65_2_QUESTION,
     "Section 4's principle gives no row to an unsettled question internal to "
     "an already-REFUSED row that gates nothing.  The finite share is internal "
     "to S10 (S10 is %s), it gates nothing (its own answer: '%s'), and nothing "
     "computes it (massform.FINITE_HIGGS_SHARE_STATUS = %s).  The option M "
     "chose was described to M as '%s'; '%s'"
     % ((massform.MECHANISM_VERDICT[0], PROPOSED["S10 (open)"][5].split("; ")[-1],
         massform.FINITE_HIGGS_SHARE_STATUS) + M_D65_2_OPTION),
     "RULED BY M: FOLD INTO S10's NOTE -- M's answer: '" + M_D65_2_ANSWER + "'.  "
     "APPLIED: no row; the finite share stays an OPEN item inside S10's note "
     "(massform's item 'S10 (open)', its status massform.FINITE_HIGGS_SHARE_"
     "STATUS, asked), a candidate question for a future docket.  O8 is not "
     "seated, and the OPEN census is statuses()'s without it",
     "S10's note carries the finite share as an OPEN item; massform.NOT_OPENED "
     "lists it again; specthm's SR5 places no O8"),

    # M's third ruling at DOCKET 65's seating: DOCKET 67, the audit of the
    # external results the board's refusals rest on.  M's words are quoted
    # verbatim; `why` is m_d65_3_why(), built from what fluctuation.py and
    # massform.py themselves record -- the discrepancies fluctuation.py
    # records against a preprint version, COUNTED from its KF flags, and the
    # divergences massform.py records under its own heading, COUNTED from its
    # sentences; the cell details two of each -- every figure and count ASKED,
    # never retyped, and fluctuation's balancing verdict (its conclusion
    # SURVIVES, no ledger row moves) asked beside them; the ruling cell is
    # M_D65_3_RULING_T filled from the constants.
    ("M-D65-3",
     M_D65_3_QUESTION,
     m_d65_3_why(),
     M_D65_3_RULING_T % (M_D65_3_ANSWER, M_D65_3_WORDS),
     "DOCKET 67, NOT YET RUN, runs after DOCKET 65 is seated and before "
     "DOCKET 66"),

    # M's fourth ruling at DOCKET 65's seating: the paper.  The completeness
    # lens found paper/CLAIMS.md's caveat (b) stating the Higgs vacuum's
    # uniformity as fact while massform seats it as the premise P-UNIFORM; the
    # question was put to M as M_D65_4_QUESTION and M answered M_D65_4_ANSWER.
    # The paper carries the clause (paper_caveat_b_faults() READS it back);
    # `why` is M_D65_4_WHY_T filled from the caveat line and massform's asked
    # status; the ruling cell is m_d65_4_ruling() -- M_D65_4_RULING_T filled
    # from the constants, M's rule for the paper (M_PAPER_RULE_WORDS) and the
    # DOCKET 63 marker READ back from the paper (paper_d63_marker()), so the
    # paper's two marked edits on M's ruling are named and neither is counted;
    # unblocks is M_D65_4_UNBLOCKS_T filled from M's rule for the paper.
    ("M-D65-4",
     M_D65_4_QUESTION,
     m_d65_4_why(),
     m_d65_4_ruling(),
     M_D65_4_UNBLOCKS_T % M_PAPER_RULE_WORDS),
]

# ---------------------------------------------------------------------------
# RIGHT SIDE -- THE SUPPLY.  What is actually available, and its ceiling.
#
# `gap_orders` is None where the row is REFUSED rather than expensive: the sign
# inverts, or the mechanism fails, BEFORE the magnitude is reached, and a gap
# would imply a ladder that is not there.
# ---------------------------------------------------------------------------

def _s5_docket65_append():
    """massform's "S5 (note)" row is an instruction -- 'APPEND to S5's note:
    <text>' -- so what is appended is the text after that prefix, asked.  The
    row must leave S5's status as it is (its status reads 'OPEN (unchanged)')."""
    prefix = "APPEND to S5's note: "
    row = PROPOSED["S5 (note)"]
    if not row[2].startswith(prefix) or row[3].split(" (")[0] != OPEN:
        raise ValueError("massform's S5 note is no longer an append to an OPEN "
                         "S5 -- ledger row S5 is stale")
    return row[2][len(prefix):]


#: The SUPPLY rows' names for DOCKET 65's priced remainders are massform's own
#: (massform.SURVIVES); S10's is a label for M's mechanism, not a result.
S10_NAME = "M's mechanism: atomic mass formed at the seat by the triggered Higgs field"


def s10_name_faults(name=None):
    """[fault] where S10's label is not a label for M's mechanism: it must
    begin "M's mechanism" and name 'by the triggered Higgs field', or it reads
    as a refusal of what S12 and S13 price."""
    name = S10_NAME if name is None else name
    bad = []
    if not name.startswith("M's mechanism"):
        bad.append("does not begin \"M's mechanism\"")
    if "by the triggered Higgs field" not in name:
        bad.append("does not name 'by the triggered Higgs field'")
    return bad


def _survives_name(word):
    """The one massform.SURVIVES name containing `word`, asked; raises if the
    owner no longer names exactly one such route."""
    hits = [n for n, _t in massform.SURVIVES if word in n]
    if len(hits) != 1:
        raise ValueError("massform.SURVIVES no longer names one %r route" % word)
    return hits[0]


def _s10_open_item():
    """massform's item "S10 (open)" -- the FINITE Higgs share -- as S10's note
    carries it on M's ruling M-D65-2 ('Fold into S10 (Recommended)'): an OPEN
    item inside S10's note, not a row.  Its text and movers are asked; it must
    still be an OPEN item on the SUPPLY side owned by FINITE_HIGGS_SHARE_STATUS,
    and that status must still read OPEN, or this raises rather than carrying
    a closed item as open."""
    r = PROPOSED["S10 (open)"]
    if (r[1], r[3], r[4]) != ("SUPPLY", OPEN, ("massform", "FINITE_HIGGS_SHARE_STATUS")) \
            or getattr(massform, r[4][1]) != OPEN:
        raise ValueError("massform's S10 (open) is no longer an OPEN item of S10 "
                         "-- ledger row S10's note is stale")
    return ("S10 (open), an OPEN item inside this note and not a row (M-D65-2): "
            + r[2] + ".  WHAT WOULD MOVE IT: " + r[5])


def _proposed_supply(rid, name):
    """A DOCKET 65 SUPPLY row: (id, name, status, owner, note).  A SUPPLY row has
    ONE note, so it carries the proposed claim and then what would move it, both
    asked of massform.PROPOSED_ROWS."""
    r = PROPOSED[rid]
    return (rid, name, _proposed_status(rid), r[4],
            r[2] + ".  WHAT WOULD MOVE IT: " + r[5])


SUPPLY = [
    ("S1", "negative effective mass (band curvature)", REFUSED, None,
     "STRUCK on KIND: m* is a dispersion curvature, not T_00.  It does not "
     "gravitate and will not source a metric"),

    ("S2", "Casimir between ideal plates", REFUSED, None,
     "STRUCK three ways by DOCKET 54 and once more by DOCKET 53.  The sign "
     "INVERTS for any real mirror at a_c = 0.480 x skin depth, "
     "materials-independent; 2G|m|/(ac^2) is a-INDEPENDENT so building it "
     "bigger buys nothing; and the plate outweighs its own Casimir energy for "
     "every material that exists"),

    ("S3", "squeezed vacuum", MEASURED, ("candidates", "REQUIREMENT_SCALES_AS"),
     "THE LEAST-DEAD ROUTE and the only survivor of the four.  Passes KIND and "
     "DEADLINE, fails MAGNITUDE.  Untouched by DOCKET 54, because the parity "
     "argument bites boundary conditions and squeezing is a state"),

    ("S4", "non-minimal coupling", REFUSED, None,
     "STRUCK on the EFT field cutoff -- and see O1, which is the same field "
     "from the other side and is STRUCK THERE TOO, at the same inequality.  "
     "The draft of this row ended 'and is OPEN rather than struck', four "
     "words that counted one refusal as an opening and inflated the open "
     "count by one"),

    ("S5", "the reconstruction route: specification, not mass", OPEN,
     ("branelink", "S5_FIGURES_MEASURED"),
     # "THE ONLY ROW" until DOCKET 65: S11-S13 are priced OPEN rows too.
     "THE FIRST ROW ON THIS LEDGER WITH A PRICE RATHER THAN A REFUSAL, AND THE "
     "ONLY ONE UNTIL DOCKET 65 SEATED S11-S13.  No mass "
     "traverses, so the demand rows D1-D4 and D7 are not instantiated and go "
     "silent.  Bounded by D13 FOR A BRANE-CONFINED CARRIER and therefore not a "
     "shortcut ON THE BRANE; a bulk carrier is not bounded by it, which is O6. "
     " STATUS DOWNGRADED FROM MEASURED, AND THE REASON IS THIS FILE'S OWN "
     "DISCIPLINE TURNED ON ITSELF: the figures this row was seated on -- "
     "8.041537e23 s.J, 6.000728e15 J, 4.870712e59 J, 43.909 orders -- OCCUR IN "
     "NO FILE IN THIS TREE.  Measured by grep this pass, all four absent.  "
     "They came from a docket's scratch computation, the scratch died with a "
     "container restart, and no instrument can re-derive or check them.  A "
     "number nobody can re-run is not MEASURED however carefully it was once "
     "computed, and seating it here was the exact fault section 0 of this file "
     "says it exists to prevent.  Re-seating it needs an instrument, not a "
     "citation.  DOCKET 62, UNCHANGED AND SHARPENED: re-grepped, the four "
     "occur in this note and in no other file.  The O6/O7 pass's apparent "
     "reproduction of them is %s.  Owed: %s.  READ WITH D23 (DOCKET 62): "
     "the fabricator, the stock survey and the receiver all had to reach "
     "the destination at <= c first, so this row is an AMORTISATION SCHEME "
     "with a minimum setup of %.4g years at Proxima, not a transport route; "
     "and D25's stock gate must hold at the destination"
     % (branelink.S5_FIGURES_STATUS, branelink.S5_OWED, PROXIMA_LY)
     # DOCKET 65 appends (massform "S5 (note)"); nothing above is replaced.
     + ".  " + _s5_docket65_append()),

    # ----- DOCKET 63: the Higgs as supply.  All REFUSED, all gap None. ------
    ("S6", "Higgs displacement as an ADDRESS", REFUSED,
     ("excite", "ROLE1_DOMINATED_BY_OWN_SOURCE"),
     "The source is a better address than the displacement it creates: its "
     "gravity reads the region farther (address.py section 9, the "
     "domination theorem), and its own interior redshift beats the vev "
     "signal beyond %.2g cm (m proportional to phi), %.2g cm (H1) or %.2g cm "
     "(H2).  Consistent with D14"
     % tuple(100.0 * excite.COURIER_CROSSOVER_M[k]
             for k in ("m propto phi", "H1", "H2"))),

    ("S7", "Higgs displacement as a BINDER", REFUSED,
     ("excite", "ROLE2_REBINDS"),
     "The m_e mechanism is exactly null (D18).  What remains is O(eps) "
     "through m_p/m_e, and it needs D20's filling source: a small, computable "
     "shift, inside matter denser than any object, and never a rebinding"),

    ("S8", "Higgs as a negative-energy source at the endpoint", REFUSED,
     ("higgs", "MINIMAL_SCALAR_SATISFIES_NEC"),
     "Minimal coupling is D17.  The xi != 0 case is S4 and O1, both refused; "
     "it needs phi at the GUT scale, xi_req = %.4g, a field %.0e (upper "
     "edge) to %.0e (lower edge) times Degrassi's instability scale "
     "10^(%g +- %g) GeV, %.0e at the centre, where the quartic is negative "
     "-- not an excitation of our vacuum.  DOCKET 63's printed '%s to %s' is "
     "the upper edge to the centre (excite.py: %s), %.0f%% of the band in "
     "log10; nothing turns on it"
     % (excite.XI_REQUIRED_AT_GUT,
        excite.XI_FIELD_OVER_INSTABILITY_UPPER_EDGE,
        excite.XI_FIELD_OVER_INSTABILITY_LOWER_EDGE,
        endpoint.DEGRASSI_LOG10_LI, endpoint.DEGRASSI_LOG10_LI_ERR,
        excite.XI_FIELD_OVER_INSTABILITY_CENTRE,
        excite.RULING_S8_PRINTED_RANGE[0], excite.RULING_S8_PRINTED_RANGE[1],
        " and ".join("/".join(m) for m in excite.RULING_S8_MATCHES),
        100.0 * excite.RULING_S8_COVERS_FRACTION_OF_BAND)),

    # ----- DOCKET 62: warpfolder.py's adjudication, the principle applied. --
    ("S9", "the Drive folder's device specification (warpfolder.py)", REFUSED,
     ("warpfolder", "FLASH_IS_A_RECONSTRUCTION_MECHANISM"),
     "The only complete device specification written for this project, "
     "REFUSED AS A SUPPLY on two independent counts.  Its own printed "
     "hardware stores %.0f J against the %.4g J its own premise needs at "
     "%.0f kg -- short by %.1f orders ON ITS OWN NUMBERS, the energy budget "
     "never connected to the chain (ENERGY_BUDGET_IS_CONNECTED_TO_THE_CHAIN "
     "= %s).  And its reconstruction mechanism "
     "is INVERTED: heating to the electroweak scale restores the symmetry "
     "(HEATING_TO_EW_SCALE_RESTORES_SYMMETRY = %s) and un-generates the masses it was to template.  That shortfall is "
     "the specification against itself, not a gap against this board's demand, "
     "so the row carries none.  NOT ADJUDICATED, and not to be quoted either "
     "way: %s -- the first is the only folder claim that touches this "
     "column"
     % (warpfolder.stored_joules(),
        warpfolder.rest_energy_j(warpfolder.PAYLOADS_KG[0]),
        warpfolder.PAYLOADS_KG[0],
        math.log10(warpfolder.shortfall(warpfolder.PAYLOADS_KG[0])),
        warpfolder.ENERGY_BUDGET_IS_CONNECTED_TO_THE_CHAIN,
        warpfolder.HEATING_TO_EW_SCALE_RESTORES_SYMMETRY,
        "; ".join(warpfolder.NOT_ADJUDICATED))),

    # ----- DOCKET 65: massform.py, seated on M's ruling.  S10 REFUSED (gap
    # None); S11-S13 the priced remainders, OPEN.  All asked. ---------------
    # S10's note carries the item S10 (open) on M's ruling M-D65-2.
    _proposed_supply("S10", S10_NAME)[:4]
    + (_proposed_supply("S10", S10_NAME)[4] + ".  " + _s10_open_item(),),
    _proposed_supply("S11", _survives_name("anomaly")),
    _proposed_supply("S12", _survives_name("pair")),
    _proposed_supply("S13", _survives_name("held-seat")),
]

# ---------------------------------------------------------------------------
# WHAT IS OPEN.  (row id, claim, what would answer it, owner)
#
# The count is statuses()'s, never typed.  `owner` names the instrument that
# seated the row's latest narrowing and an attribute that says whether the row
# CLOSED; the selftest asks it, and an owner answering True fails the ledger,
# because a row cannot be open here and closed there.  DOCKET 62 narrowed all
# five and closed none; the wording each narrowing replaced is kept below in
# SUPERSEDED_WORDING.
# ---------------------------------------------------------------------------

#: O5 AS DOCKET 62 WROTE IT (claim, answer), still computed from throatmass.py
#: so the kept wording is the wording the board printed.  DOCKET 64 replaced
#: it; SUPERSEDED_WORDING keeps it.
O5_DOCKET62 = (
     "Does a self-consistent static semiclassical solution with m(r) < 0 exist "
     "at all?  NARROWED BY DOCKET 62 (throatmass.py), status unchanged.  %d "
     "self-consistent families are in print, %d of them with m < 0: in the "
     "proper-distance gauge a throat has m = %s, and all the non-perturbative "
     "constructions are throats; the new content is the series result, %s.  "
     "The largest ever built is %.4g m, %.2f orders short of one metre.  No "
     "no-go forbids m < 0 -- %s, not NO, with a control that fires.  "
     "Flanagan-Wald and Sanders 5.1 are NOT applied, their hypotheses failing "
     "at the corridor; and if eps ~ 1 lies outside semiclassical gravity the "
     "corridor is EXPELLED rather than refuted, which is worse, because an "
     "expulsion names no hypothesis to attack.  The claim that no QEI can "
     "bound rho_ren is %s, so O5 is NOT separated from O2 permanently"
     % (throatmass.SELF_CONSISTENT_FAMILIES_RETURNED,
        throatmass.FAMILIES_WITH_NEGATIVE_MASS, throatmass.THROAT_MASS,
        throatmass.SERIES_RESULT, throatmass.LARGEST_THROAT_M,
        throatmass.ORDERS_SHORT_OF_ONE_METRE,
        throatmass.NEGATIVE_MASS_SELF_CONSISTENT_FOUND,
        throatmass.NARROWING_3_STATUS),
     throatmass.O5_ANSWERED_BY + ".  Read Anderson-Hiscock-Samuel PRD 51 4337 "
     "first")


#: THE FIVE O ROWS DOCKET 62 NARROWED (docstring section 4).  Named, so the
#: checks on narrowed rows ask for them by name and a later O row cannot be
#: mistaken for one of them.
DOCKET62_NARROWED = ("O2", "O3", "O5", "O6", "O7")


def _hps_ll_denominator(power):
    """HPS's ll-log denominator written as qeihps.py writes it, from
    hpscentre.py's integer power -- so the two instruments' repairs can be
    compared as strings rather than retyped."""
    return "/(f^2 r)" if power == 1 else "/(f^2 r^%d)" % power


OPEN_ROWS = [
    ("O5",
     "Does a self-consistent static semiclassical solution with m(r) < 0 exist "
     "INSIDE THE DOMAIN ITS <T> IS ESTABLISHED FOR?  NARROWED BY DOCKET 64 "
     "(hpscentre.py, qeihps.py), status unchanged.  HPS's system has %d "
     "disagreements with Popov; conservation decides them uniquely (tt-log "
     "coefficient %d, th %d, ll-log denominator %s), and qeihps.py's "
     "independent single-change scan finds the same two HPS repairs (%s: %d "
     "-> %d; %s: %s -> %s).  In that conserved system HPS's own throat data "
     "have m < 0 in the flare, first at %.4f l_P (MEASURED; the %s reading "
     "only).  A regular centre has %s (THEOREM, formal series; %s).  Every "
     "non-flat analytic regular-centre solution of %s changes the sign of m "
     "and is "
     "not asymptotically flat (THEOREM, 3L0 + 4 > 0, L0 != -1); for the "
     "nonlinear solutions non-flatness is %s, and their asymptotics are %s.  "
     "m < 0 FOUND IN HPS'S SYSTEM (%s reading) = %s; FOUND INSIDE THE ESTABLISHED DOMAIN "
     "= %s -- %s.  Which system HPS integrated: %s.  Kontou's requested "
     "test: %s.  Fewster-Smith on HPS: %s.  On the throat geodesic: %s.  "
     "%d of %d self-consistent families in print REPORT m < 0 "
     "(throatmass.py, READ) -- true of what was reported, and no longer the "
     "tree's finding"
     % (hpscentre.PRINTED_DISAGREEMENTS,
        hpscentre.CONSERVED["a_tt"], hpscentre.CONSERVED["a_th"],
        _hps_ll_denominator(hpscentre.CONSERVED["ll_pow"]),
        qeihps.REPAIR_CONSERVATION[0], qeihps.REPAIR_CONSERVATION[2],
        qeihps.REPAIR_CONSERVATION[3], qeihps.REPAIR_DIMENSION[0],
        qeihps.REPAIR_DIMENSION[2], qeihps.REPAIR_DIMENSION[3],
        hpscentre.FIRST_NEGATIVE_M_THROAT_LP,
        hpscentre.THROAT_M_NEGATIVE_READING, hpscentre.CENTRE_M_LEADING,
        hpscentre.RECURSION_DIRECTION,
        hpscentre.LINEAR_CENTRE_THEOREM_SCOPE,
        hpscentre.NONLINEAR_CENTRE_NONFLATNESS,
        hpscentre.NONLINEAR_CENTRE_ASYMPTOTICS,
        hpscentre.THROAT_M_NEGATIVE_READING.lower(),
        hpscentre.M_NEGATIVE_FOUND_IN_HPS_SYSTEM,
        hpscentre.M_NEGATIVE_FOUND_INSIDE_DOMAIN, hpscentre.DOMAIN_WORD,
        hpscentre.HPS_INTEGRATED_THE_PRINTED_SYSTEM,
        qeihps.KONTOU_REQUESTED_TEST_ON_HPS, qeihps.FEWSTER_SMITH_ON_HPS,
        qeihps.VERDICT_THROAT_GEODESIC,
        throatmass.FAMILIES_WITH_NEGATIVE_MASS,
        throatmass.SELF_CONSISTENT_FAMILIES_RETURNED),
     hpscentre.O5_ANSWERED_BY,
     ("hpscentre", "O5_CLOSED")),

    ("O6",
     "THE BRANE-BULK TRANSDUCER.  NARROWED BY DOCKET 62 (branelink.py), NOT "
     "CLOSED.  The row's stated cause of death -- no coupling in print -- is "
     "REFUTED: %s.  Eot-Wash bounds %s.  The throughput the closure called "
     "decisive, recomputed at omega_GW = %d Omega, is h = %.4e and %.4e "
     "bits/s/W; the pass used Omega and its figures were %.0fx and %.0fx too "
     "large, kept as withdrawn values in branelink.py.  It does not close: "
     "the closing premise, a %s, is %s; the closure runs through O7's "
     "UNTESTED B = 0, where the %.1f ns saving is evaluated; and the honest "
     "shape is a dichotomy -- %s -- so the row is settled %s"
     % (branelink.COUPLING_SOURCE, branelink.EOTWASH_BOUNDS,
        branelink.OMEGA_GW_OVER_OMEGA, branelink.STRAIN_H,
        branelink.THROUGHPUT_BITS_PER_S_PER_W,
        branelink.WITHDRAWN_STRAIN_H / branelink.STRAIN_H,
        branelink.WITHDRAWN_THROUGHPUT / branelink.THROUGHPUT_BITS_PER_S_PER_W,
        branelink.CLOSING_PREMISE, branelink.CLOSING_PREMISE_STATUS,
        branelink.SAVING_AT_B0_NS,
        "; ".join("if the %s: %s" % b for b in branelink.O6_DICHOTOMY),
        branelink.O6_SETTLED),
     "whether the graviton is a bulk degree of freedom -- on that branch the "
     "row settles, on the other it reverts -- together with the closing "
     "premise derived for a bulk carrier.  Still conceded: no moving-brane "
     "emission rate is in print, and the non-zero-winding amplitude has "
     "never been computed by anyone",
     ("branelink", "O6_CLOSED")),

    ("O7",
     "OUR OWN BOOST B RELATIVE TO THE PREFERRED BRANE FRAME.  The bulk saving "
     "is Delta_tau = (L/Gamma^2)[1/(1-B) - 1/(gamma-B)], THE FULL LIGHT TIME "
     "as B approaches 1/beta, and B cannot be purchased, because buying it "
     "means boosting the fabricator out of the destination's rest frame and "
     "forfeiting the destination-supplied atoms that are the premise.  "
     "NARROWED BY "
     "DOCKET 62 (branelink.py), NOT CLOSED: GW170817 bounds %s -- beta <= "
     "%.6e, CONDITIONAL on %s -- so at B = 0 the saving is %.4f ns, a fraction "
     "%.1e of the light time.  The provenance of that figure is %s; the "
     "dipole's Gamma - 1 = %.4e is a candidate for B and enters only through "
     "the anisotropy.  B IS UNMEASURED, and the escape is priced: B >= %.9f "
     "buys one second over the Proxima span.  The loop-induced SME route is a "
     "null %.0f orders short.  The proposed R-1 row is this row renamed and "
     "is not opened"
     % (branelink.GW170817_BOUNDS, branelink.BETA_MAX,
        branelink.BETA_BOUND_CONDITIONAL_ON, branelink.SAVING_AT_B0_NS,
        branelink.SAVING_FRACTION, branelink.PROVENANCE_94NS,
        branelink.CMB_GAMMA_MINUS_1, branelink.B_FOR_ONE_SECOND,
        branelink.SME_ORDERS_SHORT),
     branelink.O7_ANSWERED_BY,
     ("branelink", "O7_CLOSED")),

    ("O2",
     "Fewster & Teo's exact static-spacetime QEI on the corridor.  NARROWED BY "
     "DOCKET 62 (fewsterteo.py), NOT CLOSED.  Its prefactor is exactly %d, two "
     "routes in sympy.  Its %d/%d against Ford-Roman is exact and MUST NOT be "
     "applied to C_F, which already IS that family's constant at the optimal "
     "compactly supported sampler (the Parseval route is new; the agreement "
     "of two evaluations of one closed form is not a check).  Its Sec. 7 does "
     "not transplant to M < 0, the horizon being its mode-defining surface.  "
     "The corridor's own mode functions are %s.  The proposed curvature "
     "tightening came entirely from the witness's H^3 spectral gap, and the "
     "corridor has none (%s: gap %g), so the persistence refusal stays at "
     "%.3f orders, unmoved in either direction"
     % (fewsterteo.PREFACTOR_212, fewsterteo.NINE_64[0], fewsterteo.NINE_64[1],
        fewsterteo.CORRIDOR_MODE_FUNCTIONS, fewsterteo.GAP_HYPOTHESIS,
        fewsterteo.CORRIDOR_SPECTRAL_GAP, fewsterteo.FLAT_SHORTFALL_ORDERS),
     fewsterteo.O2_ANSWERED_BY + ".  The right instrument is " +
     fewsterteo.RIGHT_INSTRUMENT + " -- not Fewster & Teo's difference QEI"
     # DOCKET 64 appends (ruling C, O2), worded as noise.py states it: the
     # spectrum is bounded BELOW by the QEI bound, not equal to it.
     + ".  It also decides D22's distribution question on the corridor "
     "(noise.CURVED_PART_CARRIED_BY = %s): by FFR 1004.0179 note [18] every "
     "measurement distribution is supported in the spectrum of the sampled "
     "operator, which an absolute QEI bounds below"
     % noise.CURVED_PART_CARRIED_BY,
     ("fewsterteo", "O2_CLOSED")),

    ("O3",
     "Whether ANY braneworld shortcut yields a closed timelike curve -- with "
     "the NEC satisfied everywhere, the clause FOLDED IN rather than opened as "
     "a row.  NARROWED AND SPLIT BY DOCKET 62 (latticectc.py), NOT CLOSED.  "
     "The flat-bulk quotient is SETTLED by D21, where GKLP's 'no' is forced.  "
     "The proposed codimension-one 'yes' is REFUSED as an answer: %s"
     % latticectc.CODIM1_CTC_REFUSAL,
     latticectc.O3_ANSWERED_BY,
     ("latticectc", "O3_CLOSED")),

    # DOCKET 65 opens no O row: the finite Higgs share, first seated here as
    # O8, is an OPEN item inside S10's note on M's ruling M-D65-2.
]

#: THE WORDING DOCKETS 62 AND 64 REPLACED.  (row id, the docket that replaced
#: it, the wording as it stood -- claim, then what would answer it -- and why it
#: was replaced.)  KEYED BY (row, docket): O5 was narrowed twice, and both of
#: its earlier wordings are kept.  KEPT, NEVER DELETED: a row rewritten in
#: place is otherwise indistinguishable from one that always said the new
#: thing, and three of DOCKET 62's five said something now refuted.
SUPERSEDED_WORDING = [
    ("O5", "DOCKET 62",
     "Does a self-consistent static semiclassical solution with m(r) < 0 exist "
     "at all?  Fewster & Teo bound the NORMAL-ORDERED density relative to the "
     "static vacuum, so the bound is on rho_ren - rho_vac and not on rho_ren "
     "|| a self-consistent solve of G_ab = 8 pi <T_ab> on the negative-mass "
     "corridor, rather than a bound evaluated on an assumed background",
     "true of Fewster & Teo and NOT a limit on QEIs: " +
     throatmass.NARROWING_3_STATUS + "; the answering solve is now named "
     "exactly (HPS's system, regular-centre data)"),
    ("O6", "DOCKET 62",
     "THE BRANE-BULK TRANSDUCER.  DOCKET 61's intersection is structurally "
     "intact -- the two refusals genuinely cancel -- and dies on a coupling: "
     "neither GKLP paper states a coupling constant, a source model or an "
     "emission rate, and 2208.09014 has none in sixteen pages.  DOCKET 57's "
     "confinement ruling forces the available bulk fields to be gravitational "
     "|| a transducer that writes a specification into a bulk mode at one end "
     "and reads it at the other with brane-confined apparatus.  The "
     "energy-per-bit estimate spans 50 ORDERS AND STRADDLES ZERO, so its SIGN "
     "is unsettled and no figure may be seated from it",
     "the cause of death is REFUTED -- true of the two papers read, false of "
     "the literature: " + branelink.COUPLING_SOURCE),
    ("O7", "DOCKET 62",
     "OUR OWN BOOST RELATIVE TO THE PREFERRED BRANE FRAME.  The bulk saving is "
     "Delta_tau = (L/Gamma^2)[1/(1-B) - 1/(gamma-B)]: 94 ns at B ~ 0, and THE "
     "FULL LIGHT TIME as B approaches 1/beta.  B cannot be purchased, because "
     "buying it means boosting the fabricator out of the destination's rest "
     "frame and forfeiting the destination-supplied atoms that are the premise "
     "|| a measurement of Earth's velocity relative to the preferred brane "
     "frame, if one exists.  The only preferred-frame velocity ever measured "
     "is the CMB dipole at 370 km/s, Gamma - 1 = 7.6e-7, which is what gives "
     "94 ns",
     "WRONG PROVENANCE: the saving at B = 0 is " + branelink.PROVENANCE_94NS +
     "; the dipole is a candidate for B, not the source of the figure"),
    ("O2", "DOCKET 62",
     "Fewster & Teo give an EXACT static-spacetime QEI with no curvature cap, "
     "TIGHTER than Ford-Roman in the Minkowski limit, and the corridor is "
     "genuinely static so the class is right.  It has never been evaluated on "
     "the corridor || evaluate it once the corridor's scalar mode functions "
     "are determined -- the authors' own conclusion asks for exactly this for "
     "the static Morris-Thorne wormhole",
     "'TIGHTER' invited a void adjustment to C_F, which already IS the "
     "Fewster-Teo constant at the optimal sampler; the mode functions it "
     "waits on are NOT-FOUND; and the right instrument is Fewster & Smith's "
     "ABSOLUTE QEI"),
    ("O3", "DOCKET 62",
     "Whether ANY braneworld shortcut yields a closed timelike curve.  Every "
     "published 'no' is a one-extra-dimension or flat-bulk result; the single "
     "'yes' needs two extra dimensions and two inequivalent preferred frames "
     "|| a general result at codimension two, or an explicit CTC at "
     "codimension one.  The split in the literature tracks codimension and "
     "nobody has closed it",
     "an explicit codimension-one CTC is no longer enough -- a hand-written "
     "metric answers nothing -- and the flat-bulk 'no' is now a THEOREM (D21), "
     "forced rather than contingent"),
    # ----- DOCKET 64.  O5's DOCKET 62 wording, and the two demand rows whose
    # wording DOCKET 64 replaced rather than extended (D24's claim, D25 and O2
    # were only appended to, so nothing of theirs was replaced). -------------
    ("O5", "DOCKET 64",
     O5_DOCKET62[0] + " || " + O5_DOCKET62[1],
     "the question is narrowed to the ESTABLISHED domain: m < 0 is found in "
     "HPS's own conserved system (hpscentre.M_NEGATIVE_FOUND_IN_HPS_SYSTEM = "
     "%s), outside the domain the AHS approximation is established for.  "
     "throatmass.py's NOT-FOUND describes what HPS REPORTED and stays true "
     "of that, but is no longer printed as the tree's finding; the row is "
     "re-owned to hpscentre.O5_CLOSED"
     % hpscentre.M_NEGATIVE_FOUND_IN_HPS_SYSTEM),
    ("D22", "DOCKET 64", D22_DOCKET62,
     "the smeared price is computed in flat space (noise.py: C1 a THEOREM in "
     "H1-H6) and reaches the corridor only as a SURVEY, so the row moves OPEN "
     "-> SURVEY; 'needs the curved-space renormalisation of quartic operator "
     "products' is wrong as to NEW renormalisation (Hu & Verdaguer 3.2, "
     "READ), and the finiteness it does need is NAMED, not run (Fewster "
     "1208.5399 Sec. 3.3); fluctuation.PRICES_THE_CORRIDOR stays False and "
     "stays true of fluctuation.py"),
    ("D24", "DOCKET 64", D24_ANSWER_DOCKET62,
     "the third part -- the passage from flat space to a configuration that "
     "changes no topology -- is priced by formation.py (F1, F2), so 'no "
     "instrument in the tree does that yet' is no longer true; the row is "
     "re-owned to formation.NUCLEATION_PRICEABLE_FROM_SOURCE"),
    # ----- DOCKET 65.  S5's first sentence, replaced in place when S11-S13
    # were seated: S5 was the only priced row and is no longer. ------------
    ("S5", "DOCKET 65",
     "THE ONLY ROW ON THIS LEDGER WITH A PRICE RATHER THAN A REFUSAL",
     "S11-S13, DOCKET 65's priced remainders, are priced OPEN rows too"),
]


def superseded_dockets(table=None):
    """'62, 64 and 65': the dockets SUPERSEDED_WORDING names, built from the
    table, for the section header."""
    table = SUPERSEDED_WORDING if table is None else table
    ns = sorted(set(int(r[1].split()[1]) for r in table))
    return (", ".join(str(n) for n in ns[:-1]) + " and " + str(ns[-1])
            if len(ns) > 1 else str(ns[0]))

# ---------------------------------------------------------------------------
# WHAT WAS OPEN AND IS NOW ANSWERED.  KEPT, NEVER DELETED, for the reason the
# withdrawn rows are kept: an open question that closes and leaves no trace is
# indistinguishable from one nobody ever asked.
# ---------------------------------------------------------------------------

CLOSED_ROWS = [
    ("O4",
     "Does the contraction criterion survive the change from a CENTRE to an "
     "AXIS?  The priced object cannot have a destination (D14) and a corridor "
     "has an axis; the static cylindrical throat was unpriced in any geometry",
     "CLOSED, AND THE AXIS DOES NOT ESCAPE THE SIGN.  axial.py, six sympy "
     "residuals all 0.  In the Lambda = 0 gauge -- a FULL gauge fixing -- "
     "8 pi u W = -(W Psi')' - W Psi'^2 - W''.  On a regular axis (W(0) = 0, "
     "W'(0) = 1) and asymptotically flat (W -> r, W Psi' -> 0) both boundary "
     "terms vanish and INT 8 pi u W dr = -INT W Psi'^2 dr <= 0, with equality "
     "IFF Psi' == 0.  ANY axial contraction forces u < 0 somewhere.  NO ENERGY "
     "CONDITION IS USED -- geometry and two boundary conditions.  Phi is absent "
     "from u, so redshift buys nothing, which closes the S - 2u escape that "
     "looked real for one pass.  Same shape as certify.py's: a square carrying "
     "a minus sign, here -W Psi'^2 under an integral.  The one term with the "
     "other sign is a conical ANGLE EXCESS, W'(0) > 1, contributing exactly "
     "(W'(0) - 1) -- measured to nine places at four defects -- and an angle "
     "excess is the deficit of a NEGATIVE linear mass density, so it restates "
     "the requirement rather than avoiding it"),
    ("O1",
     "The nonminimally coupled scalar admits no state-independent QEI, so the "
     "sharpest limb of DOCKET 55 has a hole exactly where the project's "
     "most-favoured route sits",
     "CLOSED, AND REFUSED.  Both answers the row itself named are supplied, "
     "and it was S4 counted a second time -- this file's own note very nearly "
     "said so.  The compensating positive energy IS the enclosed-mass problem "
     "returning: E_pos/|E_neg| = 3 pi/(32 f xi c0^3) >= 1039.13 at xi = 1/4 "
     "and >= 1803.55 at xi = 1/6, from Fewster & Osterbrink's own "
     "construction.  LAMBDA CANCELS AND L CANCELS -- the overhead is a PURE "
     "NUMBER, which is WORSE than a power law: a growing penalty could in "
     "principle be outrun by building small, and a scale-free factor of 10^3 "
     "cannot be outrun at all"),
]


# ---------------------------------------------------------------------------
# WHAT THIS PROJECT ASSERTED AND THEN REFUTED.  Kept, never deleted.
# ---------------------------------------------------------------------------

WITHDRAWN_ROWS = [
    ("W1", "achievable.py: the census is 'bounded by a THEOREM', and the core "
     "falls short by sixty-five orders",
     "Ford-Roman is a TIME average at ONE SPATIAL POINT, not a cap on |rho| "
     "over a spatial scale.  There is no pointwise cap to price against, and "
     "the figure was computed with the inequality's own coefficient dropped"),

    ("W2", "bounds.py: 'Casimir is the Ford-Roman bound saturated, not an "
     "exception to it, which is why no material choice crosses it'",
     "Fewster reports the Casimir density at 3-7 % of the bound and asks in "
     "print why it is so small a proportion.  Three per cent is not a wall "
     "with something standing against it"),

    ("W3", "tolman.py: 'p_r is a SCALAR under H'",
     "It is DETERMINED BY a scalar and is not one.  A boost witness turns the "
     "tension into a pressure at the same event while 1 - 2m/R does not move"),

    ("W4", "tolman.py: Phi' = 0 is an exactness route, and the class is smaller",
     "Under the computed G^r_r it forces 4 pi r^3 p_r = -m, which with the "
     "identity gives m == 0.  It does not restrict the class, it EMPTIES it"),

    ("W5", "tolman.py: the regular-centre hypothesis here and DOCKET 52's are "
     "'one fact seen twice'",
     "A separating witness holds certify.py's m(0) = 0 while C = 4 pi A != 0.  "
     "Two hypotheses, not one"),

    ("W6", "the corridor shortfall is 18.5 orders",
     "That figure is vacuumcorridor.py's ratio of two POSITIVE masses answering "
     "a domain-of-validity question.  It is not a supply against a demand, and "
     "quoting it understated the real shortfall by 52.1 orders"),
    ("W7", "DOCKET 61 pass A: the directional crack is closed by observation, "
     "because at Gamma = 1.89e6 the GKLP forward direction is supercritical",
     "ARITHMETICALLY WRONG BY A FACTOR OF 14.1.  Supercriticality needs "
     "Gamma >= 1/beta = 2.6726124e7, and 1.894565e6 is SUBcritical.  The crack "
     "is closed instead by a sky-fraction coincidence of prior 2.6e-7 plus an "
     "unmeasured cosmological boost -- a residual, recorded as one, not a "
     "proof"),

    ("W8", "DOCKET 61 pass D: the unbounded saving needs endpoints in common "
     "relativistic motion while the route needs the receiver at rest in the "
     "destination's atoms, so the two premises are jointly unsatisfiable",
     "B is the COMMON boost of both endpoints relative to the PREFERRED BRANE "
     "FRAME, not relative to Proxima.  Earth and Proxima are comoving to about "
     "one part in 1e4, so a receiver at rest in Proxima's atoms automatically "
     "shares Earth's B whatever B is.  No contradiction, and the closure does "
     "not stand"),

    # DOCKET 63.  ASKED, NOT RETYPED: W9 is excite.W9 and W10-W13 are
    # address.WITHDRAWN, each a (claim, why) whose figures are computed there.
    ("W9", "DOCKET 63: " + excite.W9[0],
     "; ".join(excite.W9[1])),
] + [(k, address.WITHDRAWN[k][0], address.WITHDRAWN[k][1])
     for k in ("W10", "W11", "W12", "W13")]


def _one_line(text, width):
    """First `width` characters of `text`, on one line, with an ellipsis if cut.

    NOT text.split(".")[0].  That was the first draft and it amputated every
    sentence containing a module name -- "certify.py's COROLLARY ..." printed as
    "certify".  A report that silently truncates at a full stop is unreadable
    exactly where this tree's prose is most specific.
    """
    t = " ".join(text.split())
    return t if len(t) <= width else t[:width - 3] + "..."


def ask(owner):
    """Fetch a row's pinned value from the module that owns it.

    THE WHOLE DISCIPLINE OF THIS FILE IS IN THIS FUNCTION.  A row with an owner
    is not believed, it is asked, every run.  A row whose owner has dropped the
    attribute raises rather than defaulting, because a silently absent pin is
    how `achievable.py`'s figure survived as long as it did.
    """
    if owner is None:
        return None
    mod, attr = owner
    m = sys.modules[mod]
    if not hasattr(m, attr):
        raise AttributeError("%s no longer pins %s -- ledger row is stale"
                             % (mod, attr))
    return getattr(m, attr)


def unaskable():
    """Rows this file cannot ask, because their owner is a paper.

    COUNTED AND NAMED RATHER THAN HIDDEN.  A row backed by a citation is not
    worse than one backed by a module, but it is defended differently, and a
    reader is owed the count.
    """
    return tuple(r[0] for r in DEMAND if r[3] is None)


def open_demand():
    """DEMAND rows whose status is OPEN.  Counted once, as demand, by
    statuses(); listed again beside the O rows so the open section shows
    every open question and not only the ones filed under an O."""
    return [r for r in DEMAND if r[2] == OPEN]


def statuses():
    """The status census over both sides plus the open and withdrawn rows."""
    c = dict((s, 0) for s in STATUSES)
    for r in DEMAND:
        c[r[2]] += 1
    for r in SUPPLY:
        c[r[2]] += 1
    c[OPEN] += len(OPEN_ROWS)
    c[WITHDRAWN] += len(WITHDRAWN_ROWS)
    # A CLOSED row counts as REFUSED, not as OPEN.  O1 closed by being refused,
    # and leaving it in the OPEN tally would report an opening this tree does
    # not have -- which is the exact inflation S4's four wrong words caused.
    c[REFUSED] += len(CLOSED_ROWS)
    return c


def pending_rulings():
    """PENDING_RULINGS as printed (none since M ruled M-D65-2)."""
    return list(PENDING_RULINGS)


def balance():
    """[(id, what, demand, supply, gap in orders or None)] -- the two sides.

    A gap of None means REFUSED: the mechanism fails before the magnitude is
    reached, so there is no ladder and a number would invent one.
    """
    rows = []
    rows.append(("B1", "negative enclosed mass, 1 m of contraction",
                 "%.6g kg" % required_negative_mass(1.0),
                 "no mechanism supplies negative enclosed mass at all",
                 None))
    rows.append(("B2", "negative enclosed mass, the Proxima span",
                 "%.6g kg  (%.6g solar masses)"
                 % (required_negative_mass(PROXIMA_M),
                    required_negative_mass(PROXIMA_M) / M_SUN),
                 "as B1", None))
    rows.append(("B3", "Casimir as a source of negative enclosed mass",
                 "m(r) < 0 near the wall",
                 "m(r) > 0 near the wall for every real mirror",
                 None))
    rows.append(("B4", "the mirror against the asset it buys",
                 "|E_Cas| >= M c^2 for the apparatus",
                 "|E_Cas|/(M c^2) <= 2.72e-8 for hydrogen, the lightest "
                 "conceivable sheet",
                 None))
    return rows


def report():
    print(__doc__.split("===============", 1)[0].strip())
    print()
    print("THE EXCHANGE RATE, ASKED AND RE-DERIVED")
    print("  Lambda (overturn.py)           %.15f" % LAMBDA)
    print("  c^2/(G Lambda)                 %.6e kg per metre" % EXCHANGE_RATE)
    print("  the Proxima span               %.6e m" % PROXIMA_M)
    print("  and its demand                 %.6e solar masses"
          % (required_negative_mass(PROXIMA_M) / M_SUN))

    print("\nLEFT -- THE DEMAND")
    for rid, claim, st, owner, moves in DEMAND:
        print("  %-4s %-9s %s" % (rid, st, _one_line(claim, 96)))
        if owner:
            # An owner that is a function (D28's massform.pair_floor_j) is
            # shown by its value at the owner's defaults, not by its address.
            v = ask(owner)
            print("       asked: %s.%s%s = %s"
                  % (owner[0], owner[1], "()" if callable(v) else "",
                     str(v() if callable(v) else v)[:58]))

    print("\nRIGHT -- THE SUPPLY")
    for rid, what, st, owner, note in SUPPLY:
        # The name in full (a cut name can change the meaning: S10's cut read
        # as a refusal of atomic mass formed at a seat, which S11-S13 price).
        print("  %-4s %-9s %s" % (rid, st, what))
        if owner == ("massform", "MECHANISM_VERDICT"):
            # M's mechanism: its one-line is massform.mechanism_label(), asked
            # and printed whole, so the refusal never prints without the
            # priced remainders beside it (M's rule).
            print(textwrap.fill("as stated: " + massform.mechanism_label(), 96,
                                initial_indent="       ",
                                subsequent_indent="         "))
        else:
            print("       %s" % _one_line(note, 100))

    print("\nTHE BALANCE")
    for rid, what, dem, sup, gap in balance():
        print("  %-4s %s" % (rid, what))
        print("       demand: %s" % dem)
        print("       supply: %s" % sup)
        print("       gap:    %s" % ("REFUSED -- no ladder, so no number"
                                     if gap is None else "%.3f orders" % gap))

    print("\nOPEN, AND WHAT WOULD ANSWER EACH")
    for rid, claim, answer, owner in OPEN_ROWS:
        print("  %-4s %s" % (rid, _one_line(claim, 100)))
        print("       would be answered by: %s" % _one_line(answer, 96))
        print("       asked: %s.%s = %s" % (owner[0], owner[1], ask(owner)))
    for rid, claim, _st, owner, moves in open_demand():
        print("  %-4s (a DEMAND row) %s" % (rid, _one_line(claim, 86)))
        print("       would be answered by: %s" % _one_line(moves, 96))
    for q, why, opener in WAITS_FOR_ITS_INSTRUMENT:
        print("  NOT OPENED, WAITING FOR ITS INSTRUMENT: %s" % q)
        print("       %s" % _one_line(why, 96))
        print("       opened by: %s" % _one_line(opener, 96))
    if not WAITS_FOR_ITS_INSTRUMENT:
        print("  NOT OPENED, WAITING FOR ITS INSTRUMENT: none")
    for q, docket, rid, _why in OPENED_FROM_WAITING:
        print("       (was waiting: %s -- opened by %s as %s)" % (q, docket, rid))

    print("\nRULED BY M -- APPLIED")
    for pid, q, why, ruling, unblocks in RULED_BY_M:
        # The question in full as well: M-D65-2's is printed exactly as it
        # was put to M.
        print(textwrap.fill(pid.ljust(8) + " " + " ".join(q.split()), 96,
                            initial_indent="  ", subsequent_indent="           "))
        # In full, never cut: a ruling carries M's own words (M-D65-1).
        print(textwrap.fill("ruled: " + " ".join(ruling.split()), 96,
                            initial_indent="       ",
                            subsequent_indent="         "))
        print(textwrap.fill("unblocks: " + " ".join(unblocks.split()), 96,
                            initial_indent="       ",
                            subsequent_indent="         "))
    print("\nPENDING M'S RULING -- RECORDED, NOT APPLIED%s"
          % ("" if PENDING_RULINGS else ": none"))
    for pid, q, why, proposal, waits in pending_rulings():
        print("  %-8s %s" % (pid, _one_line(q, 94)))
        print("       %s" % _one_line(why, 96))
        print("       proposed: %s" % _one_line(proposal, 86))
        print("       waiting on it: %s" % _one_line(waits, 81))

    print("\nROW WORDING REPLACED, KEPT: %s  (--md prints it)"
          % ", ".join("%s (%s)" % (r[0], r[1]) for r in SUPERSEDED_WORDING))

    print("\nCLOSED -- WAS OPEN, NOW ANSWERED")
    for rid, claim, answer in CLOSED_ROWS:
        print("  %-4s %s" % (rid, _one_line(claim, 100)))
        print("       %s" % _one_line(answer, 100))

    print("\nWITHDRAWN -- ASSERTED BY THIS PROJECT, THEN REFUTED BY IT")
    for rid, claim, why in WITHDRAWN_ROWS:
        print("  %-4s %s" % (rid, claim[:100]))
        print("       %s" % _one_line(why, 100))

    c = statuses()
    print("\nTHE STATUS CENSUS")
    for s in STATUSES:
        print("  %-11s %3d" % (s, c[s]))
    print("  %-11s %3d  (rows whose owner is a paper, not a module: %s)"
          % ("UNASKABLE", len(unaskable()), ", ".join(unaskable())))
    return 0


# ---------------------------------------------------------------------------
# THE GENERATED DOCUMENT.  `state.py`'s pattern: the markdown is WRITTEN by the
# instrument, never edited, and `--check` re-asks every row and fails on drift.
# A hand-edited LEDGER.md is the failure mode this whole file exists to prevent,
# so the header says so and --check would catch it.
# ---------------------------------------------------------------------------

MD_HEADER = """# The warp result: what is established, and what is owed

Generated by `python3 research/warp-drive/ledger.py --md`. **Do not edit.**
Every row below is asked of the instrument that owns it at generation time;
`--check` re-asks them and exits 1 on drift.

`COMPLETE` is not claimed and is not claimable. This is what has been
established and refuted so far, not a census of what is establishable.
"""


#: CELL WIDTHS FOR LEDGER.md.  The rows DOCKET 64 wrote are longer than any
#: before them, and a cell cut at a fixed width drops the end of a claim --
#: which is where this tree puts its qualifications.  The selftest checks that
#: no demand, supply, open, superseded or pending cell is cut (the closed and
#: withdrawn tables are summaries and keep their shorter widths).  DOCKET 65
#: added the supply note to that check: S10 carries its claim and its movers in
#: one note, and the old fixed 2000 would have cut them.
W_DEMAND_CLAIM = 2400
W_DEMAND_MOVES = 1200             # DOCKET 65: D27's movers run past 1000
W_SUPPLY_NOTE = 5000              # DOCKET 65: S10's claim and movers, one note,
                                  # and the item S10 (open) (M-D65-2)
W_OPEN_CLAIM = 2400
W_OPEN_ANSWER = 800
W_WAS = 1400
W_WHY = 600
W_RULING = 1000                   # DOCKET 65: M-D65-4's ruling cell names M's
                                  # rule for the paper and the DOCKET 63 marker
                                  # READ back from the paper; 600 would cut it


def _cell(text, width):
    """One table cell: one line, cut at `width`, and every '|' escaped so a
    claim like E_pos/|E_neg| cannot split the row into extra columns."""
    return _one_line(text, width).replace("|", "\\|")


def to_markdown():
    L = [MD_HEADER, "", "## The exchange rate", "",
         "| | |", "|---|---|",
         "| Lambda (overturn.py) | %.15f |" % LAMBDA,
         "| c^2/(G Lambda) | %.6e kg per metre |" % EXCHANGE_RATE,
         "| the Proxima span | %.6e m |" % PROXIMA_M,
         "| its demand | %.6e solar masses |"
         % (required_negative_mass(PROXIMA_M) / M_SUN),
         "", "## Left -- the demand", "",
         "| id | status | claim | asked of | what would move it |",
         "|---|---|---|---|---|"]
    for rid, claim, st, owner, moves in DEMAND:
        src = "%s.%s" % owner if owner else "*(a paper -- see the note)*"
        L.append("| %s | **%s** | %s | `%s` | %s |"
                 % (rid, st, _cell(claim, W_DEMAND_CLAIM), src,
                    _cell(moves, W_DEMAND_MOVES)))

    L += ["", "## Right -- the supply", "",
          "| id | status | mechanism | note |", "|---|---|---|---|"]
    for rid, what, st, _o, note in SUPPLY:
        L.append("| %s | **%s** | %s | %s |"
                 % (rid, st, _cell(what, 80), _cell(note, W_SUPPLY_NOTE)))

    L += ["", "## The balance", "",
          "| id | quantity | demand | supply | gap |", "|---|---|---|---|---|"]
    for rid, what, dem, sup, gap in balance():
        g = "**REFUSED** -- no ladder, so no number" if gap is None \
            else "%.3f orders" % gap
        L.append("| %s | %s | %s | %s | %s |"
                 % (rid, _cell(what, 200), _cell(dem, 200), _cell(sup, 200), g))

    L += ["", "## Open, and what would answer each", ""]
    for rid, claim, answer, owner in OPEN_ROWS:
        L += ["### %s" % rid, "", _one_line(claim, W_OPEN_CLAIM), "",
              "**Would be answered by:** %s"
              % _one_line(answer, W_OPEN_ANSWER), "",
              "*Asked:* `%s.%s = %s`" % (owner[0], owner[1], ask(owner)), ""]
    for rid, claim, _st, owner, moves in open_demand():
        L += ["### %s (a demand row)" % rid, "",
              _one_line(claim, W_OPEN_CLAIM), "",
              "**Would be answered by:** %s"
              % _one_line(moves, W_OPEN_ANSWER), "",
              "*Asked:* `%s.%s = %s`" % (owner[0], owner[1], ask(owner)), ""]
    L += ["### Not opened: waiting for its instrument", "",
          "A question with no instrument is opened by the docket that builds",
          "one (the principle in `ledger.py`'s docstring, section 4).", ""]
    if WAITS_FOR_ITS_INSTRUMENT:
        L += ["| question | why it has no row yet | what opens it |",
              "|---|---|---|"]
        for q, why, opener in WAITS_FOR_ITS_INSTRUMENT:
            L.append("| %s | %s | %s |"
                     % (_cell(q, 80), _cell(why, W_WHY), _cell(opener, 200)))
    else:
        L.append("**None.**")
    L += ["", "Opened since, by the docket that built the instrument:", "",
          "| question | opened by | as row | why it had waited |",
          "|---|---|---|---|"]
    for q, docket, rid, why in OPENED_FROM_WAITING:
        L.append("| %s | %s | %s | %s |"
                 % (_cell(q, 80), docket, rid, _cell(why, W_WHY)))
    L.append("")

    L += ["## Ruled by M -- applied", "",
          "| id | question | ruling | unblocks |", "|---|---|---|---|"]
    for pid, q, why, ruling, unblocks in RULED_BY_M:
        L.append("| %s | %s | %s | %s |"
                 % (pid, _cell(q, W_WHY), _cell(ruling, W_RULING), _cell(unblocks, W_WHY)))
    L.append("")
    L += ["## Pending M's ruling -- recorded, not applied", "",
          "This file edits no peer and changes no requirement. A question",
          "that needs M's ruling is recorded here so the board shows it.", "",
          "| id | question | why it is asked | proposed | waiting on it |",
          "|---|---|---|---|---|"]
    for pid, q, why, proposal, waits in pending_rulings():
        L.append("| %s | %s | %s | %s | %s |"
                 % (pid, _cell(q, W_WHY), _cell(why, W_WHY),
                    _cell(proposal, W_WHY), _cell(waits, W_WHY)))
    L.append("")

    L += ["## Row wording replaced by DOCKETS %s" % superseded_dockets(), "",
          "Kept, never deleted: a row rewritten in place is otherwise",
          "indistinguishable from one that always said the new thing.", "",
          "| id | replaced by | as it stood (claim \\|\\| answer) "
          "| why it was replaced |",
          "|---|---|---|---|"]
    for rid, docket, was, why in SUPERSEDED_WORDING:
        L.append("| %s | %s | %s | %s |"
                 % (rid, docket, _cell(was, W_WAS), _cell(why, W_WHY)))
    L.append("")

    L += ["## Closed -- was open, now answered", "",
          "| id | what was open | how it closed |", "|---|---|---|"]
    for rid, claim, answer in CLOSED_ROWS:
        L.append("| %s | %s | %s |"
                 % (rid, _cell(claim, 220), _cell(answer, 400)))

    L += ["", "## Withdrawn -- asserted by this project, then refuted by it", "",
          "Kept, never deleted. A withdrawn figure that leaves no trace is how",
          "a corpus forgets it was ever wrong.", "",
          "| id | what was claimed | why it fell |", "|---|---|---|"]
    for rid, claim, why in WITHDRAWN_ROWS:
        L.append("| %s | %s | %s |"
                 % (rid, _cell(claim, 220), _cell(why, 300)))

    c = statuses()
    L += ["", "## Status census", "", "| status | rows |", "|---|---|"]
    for st in STATUSES:
        L.append("| %s | %d |" % (st, c[st]))
    L += ["", "Rows whose owner is a paper rather than a module, and which this",
          "file therefore cannot ask: **%s**." % ", ".join(unaskable()), ""]
    return "\n".join(L) + "\n"


def write_md(path=LEDGER_MD):
    io_open = open
    with io_open(path, "w", encoding="utf-8") as fh:
        fh.write(to_markdown())
    print("wrote %s" % path)
    return 0


def check(path=LEDGER_MD):
    """Re-ask every row and compare against the written document."""
    try:
        with open(path, encoding="utf-8") as fh:
            on_disk = fh.read()
    except FileNotFoundError:
        print("XX   %s does not exist -- run --md" % path)
        return 1
    fresh = to_markdown()
    if on_disk == fresh:
        print("ok   %s agrees with a fresh ask of every row" % path)
        return 0
    da, db = on_disk.split("\n"), fresh.split("\n")
    print("XX   %s has DRIFTED from its instruments" % path)
    shown = 0
    for i in range(max(len(da), len(db))):
        a = da[i] if i < len(da) else "<absent>"
        b = db[i] if i < len(db) else "<absent>"
        if a != b and shown < 6:
            print("     line %d\n       on disk: %s\n       fresh:   %s"
                  % (i + 1, a[:100], b[:100]))
            shown += 1
    return 1


def _superseded_keys_unique(entries):
    """True iff no (row, docket) key occurs twice in `entries`."""
    keys = [(r[0], r[1]) for r in entries]
    return len(keys) == len(set(keys))


def _withdrawn_needles_64():
    """Wordings DOCKET 64 withdrew or corrected, each with its source.  Held
    as data for the needle check; none of them is a result."""
    return [
        "exp(-10^142)",                       # noise.CORRECTED (computed)
        "no confirmed condensed reservoir",   # formation [W2]
        "confirms no condensed reservoir",    # formation [W2], ruling C text
        "cannot be priced from the source",   # formation [W3]
        "OBSTRUCTION IS PROVED",              # linstab.WITHDRAWN
        "ONE RENORMALISATION CONSTANT",       # linstab.WITHDRAWN
        "Planck-scale runaways",              # linstab.WITHDRAWN
        "nothing grows from it",              # linstab.WITHDRAWN
        "0.0074335 ",                         # hpscentre.WITHDRAWN (typed K)
        "two misprints and two errors",       # hpscentre.WITHDRAWN
        "domain of validity for",             # hpscentre.WITHDRAWN (DOMAIN)
        "SATISFIED --",                       # qeihps withdrawn verdict form
        "PROVED NOT EVALUABLE",               # formation [W6]
        "HPS integrated the PRINTED",         # hpscentre.WITHDRAWN
    ]


def _truncated_cells(demand_claim=None, demand_moves=None, open_claim=None,
                     open_answer=None, was=None, why=None, supply_note=None):
    """(table, id) of every demand, supply, open, superseded or pending cell
    that _one_line would cut at the given widths (default: the module's)."""
    dc = W_DEMAND_CLAIM if demand_claim is None else demand_claim
    dm = W_DEMAND_MOVES if demand_moves is None else demand_moves
    oc = W_OPEN_CLAIM if open_claim is None else open_claim
    oa = W_OPEN_ANSWER if open_answer is None else open_answer
    wa = W_WAS if was is None else was
    wh = W_WHY if why is None else why
    sn = W_SUPPLY_NOTE if supply_note is None else supply_note

    def cut(text, width):
        return _one_line(text, width) != " ".join(text.split())
    out = []
    for r in DEMAND:
        if cut(r[1], dc) or cut(r[4], dm):
            out.append(("demand", r[0]))
        if r[2] == OPEN and (cut(r[1], oc) or cut(r[4], oa)):
            out.append(("open demand", r[0]))
    for r in SUPPLY:
        if cut(r[4], sn):
            out.append(("supply", r[0]))
    for r in OPEN_ROWS:
        if cut(r[1], oc) or cut(r[2], oa):
            out.append(("open", r[0]))
    for r in SUPERSEDED_WORDING:
        if cut(r[2], wa) or cut(r[3], wh):
            out.append(("superseded", r[0] + " " + r[1]))
    # Every cell of a pending ruling: its question states what M approved.
    for r in pending_rulings():
        if cut(r[1], wh) or cut(r[2], wh) or cut(r[3], wh) or cut(r[4], wh):
            out.append(("pending", r[0]))
    # A ruling carries M's own words (M-D65-1) and its question as put to M
    # (M-D65-2): neither is ever cut, nor what it unblocks.
    for r in RULED_BY_M:
        if cut(r[1], wh) or cut(r[3], W_RULING) or cut(r[4], wh):
            out.append(("ruled", r[0]))
    return out


#: DOCKET 65's QUALIFIERS, per seated row: (phrase, how many times the row
#: carries it).  The board's other guard on these rows is exact equality with
#: massform.PROPOSED_ROWS, and massform's own REQUIRED_WORDING does not pin
#: every one, so a qualifier deleted at the owner would reach LEDGER.md green.
#: Each is a named hypothesis, a scope or an admission the row rests on; a
#: count, not a presence, so deleting one of several occurrences is caught.
#: The bare hypothesis tokens are pinned by WHOLE-ROW count as well as in one
#: phrase each: a phrase pin covers one context, and every other occurrence of
#: the token (D27's 'on H-PRESENT it needs no P-UNIFORM', HELD_SEAT_TEXT's
#: H-TREE and H-UNSOURCED-SEAT, _C1_TEMPLATE's H-TREE) could otherwise be
#: deleted at the owner and reach LEDGER.md green.  The counts are what
#: _row_text returned when they were pinned.
SEATED_QUALIFIERS = {
    # D27's scope: 'can only LOWER |phi|' is a claim within D20's model, and
    # without the phrase it reads unconditional.
    "D27": (("Where H-UNSOURCED-SEAT fails", 1), ("measured masses (H-PRESENT)", 1),
            ("within excite's section-3 model", 1), ("Within D20's model", 1),
            ("H-PRESENT", 5), ("H-UNSOURCED-SEAT", 4), ("H-TREE", 3), ("P-UNIFORM", 6)),
    # D28's 'at least': the pair floor is PROVED as a floor; without it the
    # row states an exact cost, which is false.
    "D28": (("both NAMED-NOT-READ", 1), ("H-BL", 1), ("H-AME", 1),
            ("negligible at payload scale", 1), ("costs at least", 1)),
    "D29": (("H-REAL", 2), ("claimed and not computed", 1), ("not established", 1),
            ("INFERENCE", 1)),
    "S10": (("as NET formation only", 1), ("on P-UNIFORM)", 1), ("H-LINEAR", 1),
            ("none a bound", 1), ("OPEN, and no verdict rests on it", 1),
            ("elements (H-PRESENT)", 1),
            ("H-PRESENT", 5), ("H-UNSOURCED-SEAT", 3), ("H-TREE", 2), ("P-UNIFORM", 6),
            # The item S10 (open), carried in S10's note on M's ruling M-D65-2
            # (these pins were O8's while it was seated as a row): its
            # admissions, and 'undecided'/'H-LINEAR' counted over the note.
            ("(H-LINEAR)", 1), ("Not computed and not read here", 1),
            ("whether it exceeds half is undecided here", 2),
            ("H-LINEAR", 2), ("undecided", 2)),
    # S11's admission that v is NAMED-NOT-READ (via alpha_W).
    "S11": (("CONTESTED", 1), ("dissent", 1), ("decides nothing", 1), ("unproven", 1),
            ("alpha_W's NAMED-NOT-READ", 1)),
    # S12's 'at least': the carrier supplies the pair floor or more.
    "S12": (("(not computed here)", 1), ("supplies at least the pair floor", 1)),
    "S13": (("Within excite's section-3 model", 2), ("not a bound", 1),
            ("H-RELEASE", 3), ("H-UNSOURCED-SEAT", 2), ("H-TREE", 1),
            ("(not computed here)", 1)),
}


def _row_text(rid, rows=None):
    """Every text field of seated row `rid`, whitespace-normalised."""
    rows = dict((r[0], r) for r in DEMAND + SUPPLY + OPEN_ROWS) if rows is None else rows
    return " ".join(" ".join(x.split()) for x in rows[rid] if isinstance(x, str))


def missing_qualifiers(rows=None):
    """[(row id, phrase, times carried, times required)] for every DOCKET 65
    qualifier a seated row carries fewer times than SEATED_QUALIFIERS says."""
    out = []
    for rid, need in SEATED_QUALIFIERS.items():
        t = _row_text(rid, rows)
        for phrase, n in need:
            if t.count(phrase) < n:
                out.append((rid, phrase, t.count(phrase), n))
    return out


_VERBATIM = re.compile(r"verbatim: '([^']+)'")
#: M-D65-3's words hold apostrophes, so every cell quotes them in double quotes.
_VERBATIM_DQ = re.compile(r'verbatim: "([^"]+)"')
#: (the constant M's words are held in, the pattern that finds a printed copy)
#: per DOCKET 65 ruling that quotes M verbatim.
_M_WORDS = {"M-D65-1": (M_D65_1_WORDS, _VERBATIM),
            "M-D65-3": (M_D65_3_WORDS, _VERBATIM_DQ)}


def verbatim_faults(qrow=None, md=None, rid="M-D65-1"):
    """[fault] where a printed copy of M's words in a DOCKET 65 ruling (`rid`:
    M-D65-1 or M-D65-3) -- `why`, the ruling cell (which LEDGER.md and the
    report print), or LEDGER.md's line for it -- is not exactly the constant
    the words are held in, or where a copy is missing."""
    qrow = [r for r in RULED_BY_M if r[0] == rid][0] if qrow is None else qrow
    md = to_markdown() if md is None else md
    words, pat = _M_WORDS[rid]
    line = [l for l in md.splitlines() if l.startswith("| %s |" % rid)]
    bad = []
    for where, text, want in (("why", qrow[2], 1), ("ruling cell", qrow[3], 1),
                              ("LEDGER.md", " ".join(line), 1)):
        got = pat.findall(" ".join(text.split()))
        if len(got) != want:
            bad.append("%s: %d verbatim copies, want %d" % (where, len(got), want))
        bad += ["%s: '%s'" % (where, g) for g in got if g != words]
    return bad


def m_d65_1_faults(qrow=None):
    """[fault] where M-D65-1 misdescribes QET's standing: the literature named
    to M incomplete (arXiv:2506.19878 was named), QET said to be TESTED in
    DOCKET 66 while that docket has not run, or the question's parenthetical
    printed as READ rather than as the question's own description."""
    qrow = [r for r in RULED_BY_M if r[0] == "M-D65-1"][0] if qrow is None else qrow
    why, ruling = " ".join(qrow[2].split()), " ".join(qrow[3].split())
    bad = []
    for aid in ("1701.03805", "2301.02666", "2505.04689", "2506.19878"):
        if not ("arXiv:%s" % aid in why and "arXiv:%s" % aid in ruling):
            bad.append("arXiv:%s missing from why or the ruling cell" % aid)
    if "QET is to be tested inside DOCKET 66 (NOT YET RUN)" not in ruling:
        bad.append("the ruling cell does not say QET is TO BE tested (NOT YET RUN)")
    if re.search(r"QET is tested inside", ruling):
        bad.append("the ruling cell says QET IS tested, present tense")
    clause = "the question's description as put to M, not READ"
    if not (clause in why and clause in ruling):
        bad.append("the question's parenthetical is not attributed to the question")
    return bad


def p1_unblocks_faults(text=None):
    """[fault] where M-S1A-P1's unblocks cell does not say DOCKET 65 has run and
    which rows it seated, built from massform's ids."""
    text = ([r for r in RULED_BY_M if r[0] == "M-S1A-P1"][0][4]
            if text is None else text)
    want = "DOCKET 65 has run: %s (massform.py)" % D65_SEATED_IDS
    return [] if want in " ".join(text.split()) else ["missing: " + want]


@contextlib.contextmanager
def _scratch(attr, value):
    """Replace one module-level table for the duration, restored after."""
    g = globals()
    keep = g[attr]
    g[attr] = value
    try:
        yield
    finally:
        g[attr] = keep


#: DOCKET 65's POLARITY: (row, the phrase in which the seated text states a
#: DIRECTION, the owner predicate that direction reports, asked NOW).  massform
#: owns both the typed text and the flag, and either can drift alone, so each
#: seated row's text direction is tied here to the owner value it states.  Red
#: if the phrase is missing from the row or the owner disagrees.
POLARITY = (
    ("D27", "arrival switches nothing on",
     lambda: not massform.FIELD_SWITCHED_ON_BY_ARRIVAL),
    ("D28", "costs at least", lambda: massform.pair_floor_j() > 0),
    ("D28", "leaves B units of antibaryon number", lambda: massform.COUNTS["B"] > 0),
    ("D29", "has no energy to give about v",
     lambda: not massform.HIGGS_FIELD_SUPPLIES_THE_MASS_ENERGY),
    ("S10", "REFUSED, gap None", lambda: massform.MECHANISM_VERDICT[0] == REFUSED),
    # S11's text states its price per transition and its limits; it carries no
    # 'PRICED' word, so its priced direction is the stated exponent.
    ("S11", "exp(-4 pi/alpha_W) per transition", lambda: massform.ANOMALY_ROUTE_PRICED),
    ("S11", "extra leptons (D28)", lambda: massform.extra_leptons() > 0),
    ("S11", "Two-particle collisions: CONTESTED",
     lambda: massform.COLLIDER_RATE_STATUS == "CONTESTED"),
    ("S12", "Priced, not refused", lambda: massform.PAIR_ROUTE_PRICED),
    ("S13", "PRICED at eps", lambda: massform.HELD_SEAT_ROUTE_PRICED),
    ("S5", "survives M's mechanism: no mass forms at the seat",
     lambda: massform.RECONSTRUCTION_SURVIVES),
)


def polarity_faults(rows=None, table=None):
    """[(row, phrase, fault)] for every POLARITY entry whose phrase the seated
    row does not carry, or whose owner, asked now, disagrees with it."""
    table = POLARITY if table is None else table
    out = []
    for rid, phrase, owner_says in table:
        if phrase not in _row_text(rid, rows):
            out.append((rid, phrase, "phrase missing"))
        elif not owner_says():
            out.append((rid, phrase, "owner disagrees"))
    return out


def theorem_owner_disagreements():
    """[row id] of D27-D29 whose owner, asked NOW, no longer says what the
    THEOREM row says: D27 CONSIDERATION_HOLDS True; D28 the pair floor, above
    the rest energy by exactly B mu_min c^2; D29 HIGGS_FIELD_SUPPLIES_THE_
    MASS_ENERGY False.  This compares owner VALUES only.  The rows' text and
    the owner values are separate objects on massform and either can drift
    alone, so the text's DIRECTION is tied to the values by POLARITY
    (polarity_faults), checked beside this in selftest 4d."""
    row = dict((r[0], r) for r in DEMAND)
    bad = []
    if ask(row["D27"][3]) is not True:
        bad.append("D27")
    floor, rest = massform.pair_floor_j(), massform.rest_energy_j()
    pairs = massform.COUNTS["B"] * massform.MU_MIN[0] * massform.MEV_J
    if (row["D28"][3] != ("massform", "pair_floor_j") or not floor > rest
            or abs(floor - (rest + pairs)) > 1e-12 * floor):
        bad.append("D28")
    if ask(row["D29"][3]) is not False:
        bad.append("D29")
    return bad


def selftest():
    ok = True

    def chk(label, got, want):
        nonlocal ok
        good = got == want
        ok &= good
        print("  [%s] %-58s %s" % ("ok" if good else "XX", label,
                                   got if good else "%s != %s" % (got, want)))

    print("1. EVERY ROW WITH AN OWNER IS ASKED, AND THE ASK SUCCEEDS")
    asked = 0
    for rid, _claim, _st, owner, _m in DEMAND + [(a, b, c, d, e)
                                                 for a, b, c, d, e in SUPPLY]:
        if owner is not None:
            ask(owner)                       # raises if the peer dropped it
            asked += 1
    # RE-PINNED 10 -> 11: D14 (the addressing theorem, DOCKET 60) is asked of
    # certify.THEOREM_SCOPE, because the scope line IS the claim -- a device
    # specified by (Phi, m) of r alone has no parameter for a destination.
    chk("every owned row's attribute still exists on its peer", asked, 35)
    # RE-PINNED 28 -> 35 BY DOCKET 65, to what this loop counts after the
    # seating: +3 D27-D29 and +4 S10-S13, each asked of massform.py.  (The
    # finite share, seated first as O8 and folded into S10's note on M's
    # ruling M-D65-2, is no row and adds no owner here.)
    # RE-PINNED 27 -> 28 BY DOCKET 64, to what this loop counts after the
    # edit: +1 D26 (linstab.SEMICLASSICAL_EVALUABLE_ON_DEMAND).  D22 and D24
    # were already owned and are RE-OWNED (noise.CORRIDOR_APPLICATION,
    # formation.NUCLEATION_PRICEABLE_FROM_SOURCE), which moves no count.
    # RE-PINNED 11 -> 23 BY DOCKETS 62 AND 63, to what this loop counts after
    # the edit (the DOCKET 63 ruling projected 20; that was a prediction, not
    # a pin).  +6 D15-D20 and +3 S6-S8, owners as DOCKET 63 named them; +1
    # D21, the lattice theorem, asked of latticectc.py; +1 D22, fluctuation.py,
    # the board catching up with the tree; +1 S5, now asked of branelink.py
    # whether its four figures were measured -- they were not.
    # RE-PINNED 23 -> 27 by the fix pass on DOCKETS 62/63, to what this loop
    # counts: the row-opening principle (docstring section 4) applied to
    # every candidate with an instrument -- +1 D23 (transit.py), +1 D24
    # (create.py), +1 D25 (stockgate.py), +1 S9 (warpfolder.py).
    open_asked = 0
    for rid, _c, _a, owner in OPEN_ROWS:
        ask(owner)
        open_asked += 1
    chk("and every O row is asked of the instrument that narrowed it",
        open_asked, len(OPEN_ROWS))

    print("\n2. THE PEERS STILL SAY WHAT THE ROWS SAY THEY SAY")
    row = dict((r[0], r) for r in DEMAND + SUPPLY)
    chk("certify.py's scope is unmoved",
        ask(("certify", "THEOREM_SCOPE")), "static and spherically symmetric only")
    chk("foliation.py does not dispute the identity",
        ask(("foliation", "IDENTITY_DISPUTED")), False)
    chk("driven.py: the local criterion is not a scalar",
        ask(("driven", "CONTRACTION_IS_A_SCALAR")), False)
    chk("nonstatic.py: sustaining does not force rho < 0",
        ask(("nonstatic", "SUSTAINING_FORCES_NEGATIVE_RHO")), False)
    chk("drivensource.py: the corollary is NARROWED",
        ask(("drivensource", "CERTIFY_COROLLARY")).startswith("NARROWED"), True)
    chk("tolman.py does not supersede certify.py",
        ask(("tolman", "SUPERSEDES_CERTIFY")), False)
    chk("tolman.py restates it on a smaller class",
        ask(("tolman", "RESTATES_CERTIFY_ON_SMALLER_CLASS")), True)
    chk("bounds.py: the Ford-Roman saturation coding is wrong",
        ask(("bounds", "FORD_ROMAN_K_IS_WRONG")), True)
    # DOCKET 63's owners.
    for attr in ("TAIL_RATE_IS_MASS", "DISPLACEMENT_IS_ULTRALOCAL",
                 "FLAT_DIRECTIONS_ARE_INERT", "ROLE1_DOMINATED_BY_OWN_SOURCE"):
        chk("excite.py: %s" % attr, ask(("excite", attr)), True)
    chk("excite.py: the Higgs does not rebind (S7 REFUSED)",
        ask(("excite", "ROLE2_REBINDS")), False)
    chk("excite.py: the electron-mass ruler is a THEOREM on named hypotheses",
        ask(("excite", "ELECTRON_MASS_IS_A_RULER")).startswith("THEOREM given"),
        True)
    chk("higgs.py: a minimal scalar satisfies the NEC (D17, S8)",
        ask(("higgs", "MINIMAL_SCALAR_SATISFIES_NEC")), True)
    # D20 is ASKED; the ruling's 2.204772e11 is the FIXTURE it must reproduce,
    # and the ask must be the seated function's output, not a copy of it.
    # DOCKET 63 printed 2.204772e11 at the withdrawn pin 125.20; M's ruling switched
    # m_h to the READ 125.13, and the figure carries m_h^2.
    _mh = higgs.M_HIGGS / higgs.M_HIGGS_PIN_WITHDRAWN
    chk("D20 reproduces DOCKET 63's 2.204772e11 kg/m^3, rescaled by (m_read/m_pin)^2",
        abs(ask(("excite", "HOLD_HIGGS_DERIVED_KG_M3_AT_EPS_1E18"))
            / (2.204772e11 * _mh ** 2) - 1.0) < 1e-6, True)
    chk("  and it IS address.source_density at the fixture's eps",
        ask(("excite", "HOLD_HIGGS_DERIVED_KG_M3_AT_EPS_1E18")),
        address.source_density(excite.EPS_AT_FIXTURE, 1.0)[1])
    chk("W9-W13 are asked of their owners, not retyped",
        ([r[1:] for r in WITHDRAWN_ROWS[-4:]]
         == [address.WITHDRAWN[k] for k in ("W10", "W11", "W12", "W13")],
         WITHDRAWN_ROWS[-5][2] == "; ".join(excite.W9[1])), (True, True))
    chk("  and each W10-W13 claim is withdrawn on its owner too",
        (address.OPTICAL_OPTICAL_IS_EXACTLY_BLIND,
         address.K_ALPHA_H1_IS_NEGATIVE,
         address.SOURCE_TO_FIELD_IS_QUARTER_OVER_EPS,
         address.SAME_OBSTRUCTION_EVERY_ROLE), (False, False, False, False))
    # DOCKET 62's owners.
    chk("latticectc.py: the lattice theorem is a THEOREM (D21)",
        ask(("latticectc", "LATTICE_THEOREM_STATUS")), THEOREM)
    chk("  with its hypotheses named", len(latticectc.HYPOTHESES), 3)
    chk("  and GKLP's 'no' forced, the spacelike rank-2 span CTC-free",
        (latticectc.GKLP_NO_IS_FORCED, latticectc.RANK2_SPACELIKE_SPAN_HAS_CTC,
         latticectc.RANK2_TIMELIKE_SPAN_HAS_CTC), (True, False, True))
    chk("DOCKET 57's two routes are NOT independent at codimension one",
        latticectc.DOCKET57_ROUTES_INDEPENDENT_AT_CODIM1, False)
    # D22, DOCKET 64 (ruling C): the row is asked of noise.py now.  Its status
    # is THIS file's ruling, and the check ties it to the owner's own word, so
    # a noise.py that moved its corridor application off SURVEY turns it red.
    chk("noise.py: C1 is a THEOREM in the flat model, and D22's status IS "
        "noise.CORRIDOR_APPLICATION",
        (noise.C1_FLAT_THEOREM, ask(("noise", "CORRIDOR_APPLICATION")),
         row["D22"][2] == noise.CORRIDOR_APPLICATION), (True, SURVEY, True))
    chk("  the curved part is carried by an existing OPEN row (O2), not a new "
        "one",
        (noise.CURVED_PART_CARRIED_BY in [r[0] for r in OPEN_ROWS],
         noise.ROW_TO_OPEN), (True, None))
    chk("  and noise.py no longer claims to decide D22 (DECIDES_D22 withdrawn)",
        (noise.DECIDES_D22, "DECIDES_D22 = True" in noise.WITHDRAWN),
        (False, True))
    chk("  H2 fails on the corridor: (b/l_G)^2 = noise.B_OVER_LG_SQUARED > 1, "
        "and the owner agrees",
        (noise.B_OVER_LG_SQUARED > 1.0, noise.H2_SATISFIED_BY_CORRIDOR),
        (True, False))
    chk("  D22 prints the owner's figures at the precision the ruling named",
        all(t in row["D22"][1] for t in (
            "%.6f C/tau^4" % noise.SD0_OVER_C,
            "%.6f beta" % noise.TAU_STAR_OVER_BETA,
            "(b/l_G)^2 = %.0f" % noise.B_OVER_LG_SQUARED)), True)
    # The EL-surrogate bound: the ruling typed exp(-10^142) and computation
    # refutes it (noise.CORRECTED).  The exponent printed is floor() of the
    # owner's computed log10(-ln P), so it cannot drift from the owner.
    _el = int(math.floor(noise.EL_VACUUM_LOG10_NEG_LN_P))
    chk("  the EL-surrogate bound D22 prints is the owner's computed one",
        (("below exp(-10^%d)" % _el) in row["D22"][1],
         noise.EL_VACUUM_BELOW_EXP_MINUS_10_141 == (_el == 141),
         noise.EL_VACUUM_BELOW_EXP_MINUS_10_142), (True, True, False))
    chk("fluctuation.py does not price the corridor, and that stays true of "
        "fluctuation.py (D22 is no longer asked of it)",
        (ask(("fluctuation", "PRICES_THE_CORRIDOR")), row["D22"][3][0]),
        (False, "noise"))
    chk("  and its bound is sign-blind and needs no diagonal G",
        (fluctuation.POINTWISE_DELTA_DISCRIMINATES_SIGN,
         fluctuation.BOUND_NEEDS_DIAGONAL_G), (False, False))
    chk("branelink.py: S5's four figures are NOT measured (S5 stays OPEN)",
        ask(("branelink", "S5_FIGURES_MEASURED")), False)
    # The principle's rows (docstring section 4), each asked of its owner.
    chk("transit.py: the traversal is moved earlier, not removed (D23)",
        (ask(("transit", "TRAVERSAL_IS_REMOVED")), transit.BEATS_LIGHT),
        (False, False))
    chk("  and S5's note carries D23's amortisation reading",
        ("AMORTISATION SCHEME" in row["S5"][4],
         ("%.4g years" % PROXIMA_LY) in row["S5"][4]), (True, True))
    chk("create.py: nucleation is NOT-RUN (create.py's own word, unmoved)",
        create.NUCLEATION_STATUS, "NOT-RUN")
    # D24, DOCKET 64.  The ruling asked for NUCLEATION_PRICEABLE_FROM_SOURCE
    # = False; formation.py's verification withdrew that (not a proved
    # obstruction) and the owner now says NOT DETERMINED.  The weaker word is
    # the one asked, and the row stays OPEN because the price is not computed.
    chk("formation.py: nucleation READ, not computed, priceability NOT "
        "DETERMINED -- so D24 stays OPEN",
        (ask(("formation", "NUCLEATION_PRICEABLE_FROM_SOURCE")),
         formation.NUCLEATION_PRICED, formation.NUCLEATION_NECK_EXPLICIT,
         row["D24"][2]), (formation.NOT_DETERMINED, False, False, OPEN))
    chk("  and the withdrawn 'cannot be priced' is kept on the owner",
        formation.NUCLEATION_PRICEABLE_FROM_SOURCE_WITHDRAWN[0], False)
    chk("  D24 prints F1's and F2's hypotheses as the owner names them",
        ("; ".join(formation.F1_THEOREM) in row["D24"][1],
         formation.H_NULL in row["D24"][1],
         set(formation.F2_THEOREM) - set(formation.F1_THEOREM)
         == {formation.H_NULL}), (True, True, True))
    chk("  and the D4 observation is the owner's computed flag",
        ("PHASE1_D4_POINTWISE_DURING_PASSAGE = %s"
         % formation.PHASE1_D4_POINTWISE_DURING_PASSAGE) in row["D24"][1],
        True)
    chk("  exotic matter does not help creation; no escape stays in GR",
        (create.EXOTIC_MATTER_HELPS_CREATION,
         create.any_escape_stays_in_lorentzian_gr()), (False, False))
    chk("stockgate.py: D25's claim quotes the gate its owner states",
        ask(("stockgate", "GATE")) in row["D25"][1], True)
    chk("  and its binder is the one stockgate.py computes for a CI chondrite",
        ("binds on %s at %.4g"
         % stockgate.binding_under("as-composed 59", "CI chondrite"))
        in row["D25"][1], True)
    # D25, DOCKET 64: stays OPEN; formation.py narrows nothing and its
    # verification withdrew both "NARROWED" and "no confirmed condensed
    # reservoir".  stockgate's figures appear ONCE (over-representation).
    _bind = "%.4g" % stockgate.binding_under("as-composed 59",
                                             "CI chondrite")[1]
    chk("D25 stays OPEN, printing formation.D25_VERDICT, and stockgate's "
        "figure appears once",
        (row["D25"][2], formation.D25_VERDICT in row["D25"][1],
         formation.D25_VERDICT.startswith("OPEN AND UNCHANGED"),
         row["D25"][1].count(_bind)), (OPEN, True, True, 1))
    chk("  the survey names a CONDENSED body; primitive and accessible are "
        "unmeasured; no reservoir is claimed either way",
        (formation.SURVEY_CONDENSED_BODY_FOUND,
         formation.SURVEY_PRIMITIVE_MEASURED,
         formation.SURVEY_ACCESSIBLE_MEASURED,
         formation.SURVEY_CONFIRMED_RESERVOIR,
         formation.SURVEY_CONFIRMED_RESERVOIR_WITHDRAWN[0]),
        (True, False, False, formation.UNDETERMINED, False))
    chk("  and the aperture hit count D25 prints is the owner's",
        ("%d files hit" % len(set(formation.APERTURE_HITS)
                              | set(formation.APERTURE_SYNONYM_HITS)))
        in row["D25"][1], True)
    # D26, DOCKET 64: opened by the docket that built its instrument.
    # A GREEN BOARD OVER A RED OWNER is what the ownership contract forbids
    # (DOCKET 64 seating verifier): D26's typed flag alone cannot see linstab's
    # scan go red.  So the board re-runs the owner's own scan, over the owners
    # the board itself names, and requires the verdict False with nothing unread.
    _owners = linstab.demand_owners()[0]
    chk("linstab's scan, re-run by the board: verdict False and no unread hit",
        linstab.semiclassical_evaluable_on_demand(
            linstab.self_consistency_scan(_owners), _owners), (False, []))
    chk("linstab.py: D26 is OPEN because the semiclassical sector is not "
        "evaluable on any demand configuration",
        (ask(("linstab", "SEMICLASSICAL_EVALUABLE_ON_DEMAND")),
         row["D26"][2], linstab.D26_STATUS), (False, OPEN, OPEN))
    chk("  its text and answer are the owner's, not retyped",
        (row["D26"][1].startswith(linstab.D26_CLAIM),
         row["D26"][4] == linstab.D26_ANSWERED_BY), (True, True))
    chk("  classical radial THEOREM, infimum -1/4, the wall formula at u",
        (linstab.CLASSICAL_RADIAL_STATUS, linstab.BETA2_CRIT_INFIMUM,
         linstab.DEVICE_IS_WALL_FORMULA_AT_U), (THEOREM, "-1/4", True))
    chk("  the IFF is narrowed and 'recorded or shown' replaces a proof",
        ("recorded or shown" in linstab.D26_CLAIM,
         "GMMPS's reported" in linstab.D26_CLAIM,
         linstab.ALPHA_ZERO_ROOT_GROWTH), (True, True, OPEN))
    chk("  hpscentre is one of the scan's positive controls",
        "hpscentre" in linstab.POSITIVE_CONTROLS, True)
    chk("warpfolder.py: the flash is not a reconstruction mechanism (S9)",
        ask(("warpfolder", "FLASH_IS_A_RECONSTRUCTION_MECHANISM")), False)
    chk("  heating restores the symmetry; the budget is unconnected",
        (warpfolder.HEATING_TO_EW_SCALE_RESTORES_SYMMETRY,
         warpfolder.ENERGY_BUDGET_IS_CONNECTED_TO_THE_CHAIN), (True, False))
    chk("  S9's shortfall is warpfolder.shortfall() at its first payload",
        ("short by %.1f orders"
         % math.log10(warpfolder.shortfall(warpfolder.PAYLOADS_KG[0])))
        in row["S9"][4], True)
    chk("  and both NOT-ADJUDICATED claims are named in S9, not given rows",
        (all(n in row["S9"][4] for n in warpfolder.NOT_ADJUDICATED),
         len(warpfolder.NOT_ADJUDICATED)), (True, 2))
    chk("every OPEN demand row has an instrument (the principle's first half)",
        [r[0] for r in open_demand() if r[3] is None], [])
    chk("every question waiting for its instrument names what opens it",
        all(bool(w[2]) for w in WAITS_FOR_ITS_INSTRUMENT), True)
    chk("  and none of them is also a row",
        [w[0] for w in WAITS_FOR_ITS_INSTRUMENT
         if any(w[0] in r[1].lower() for r in DEMAND + SUPPLY)], [])
    # Those two rows are vacuous on an empty list, so the move itself is
    # checked: what left the list is a row now, and the row it names exists.
    chk("linearised stability left the waiting list and IS a row (D26)",
        ([w[0] for w in WAITS_FOR_ITS_INSTRUMENT],
         [(q, rid, rid in row and q in row[rid][1].lower())
          for q, _d, rid, _w in OPENED_FROM_WAITING]),
        ([], [("linearised stability", "D26", True)]))
    chk("  and LEDGER.md prints 'None.' rather than dropping the section",
        "### Not opened: waiting for its instrument\n\nA question with no "
        "instrument is opened by the docket that builds\none (the principle "
        "in `ledger.py`'s docstring, section 4).\n\n**None.**"
        in to_markdown(), True)
    # The phase1 D4 question (DOCKET 64 ruling D.2) is recorded for M, not
    # applied.  Its premise is computed on both owners, so it can fail.
    # M RULED on the phase1 D4 question: restate.  Each premise is computed on the
    # owners, so a revert of phase1.py or formation.py fails here.
    chk("the phase1 D4 question is RULED and APPLIED, on computed premises",
        ([p[0] for p in RULED_BY_M], [p[0] for p in PENDING_RULINGS],
         phase1.D4_RESTATED_ON_M_RULING,
         phase1.is_transition(True, True, True, True, True),
         phase1.is_transition(False, True, True, True, True, net_momentum=True),
         phase1.is_transition(False, True, True, True, True, passage_flux=True),
         formation.PHASE1_D4_POINTWISE_DURING_PASSAGE),
        (["M-D64-1", "M-S1A-P1", "M-S1A-P2", "M-S1A-P3", "M-S1A-P4",
          "M-S1A-P5", "M-D65-1", "M-D65-2", "M-D65-3", "M-D65-4"], [], True,
         False, False, True, False))

    print("\n3. THE EXCHANGE RATE, RE-DERIVED FROM ASKED CONSTANTS")
    chk("Lambda is overturn.py's", LAMBDA, overturn.LAMBDA)
    chk("c^2/(G Lambda) reproduces the tree's 1.348948e26 to 7 figures",
        round(EXCHANGE_RATE / 1e26, 6), 1.348948)
    chk("and the Proxima demand is 5.4194e42 kg to 5 figures",
        round(required_negative_mass(PROXIMA_M) / 1e42, 4), 5.4194)

    print("\n4. THE LEDGER'S OWN SHAPE")
    c = statuses()
    # RE-PINNED BY DOCKETS 60 AND 61, and every move is a row this file got
    # wrong or a row a docket answered -- not growth.
    #   THEOREM 11 -> 11: D14 arrives, D13 leaves for THEOREM-NARROWED.
    #   MEASURED 3 -> 2: S5 downgraded, because the four figures it was seated
    #     on occur in NO file in this tree.  Measured by grep, all four absent.
    #   OPEN 3 -> 7: O1 closes (refused), O4-O7 arrive, and S5 joins as open.
    #   WITHDRAWN 6 -> 8: W7 and W8, both of them DOCKET 61's own passes.
    #   REFUSED 3 -> 4: the closed row counts here, not as an opening.
    chk("the status census", c,
        {THEOREM: 20, NARROWED: 1, MEASURED: 3, SURVEY: 2, OPEN: 13,
         WITHDRAWN: 13, REFUSED: 10})
    # RE-PINNED BY DOCKET 65 to what statuses() returned after the seating
    # (M: "Seat as proposed"), every status asked of massform.PROPOSED_ROWS:
    #   THEOREM 17 -> 20: D27, D28, D29.
    #   OPEN 10 -> 13: S11, S12, S13 (priced remainders).  S5 stays OPEN;
    #     its note is appended to, not moved.  The seating first opened the
    #     finite Higgs share as O8 and statuses() gave 14; M ruled M-D65-2
    #     ('Fold into S10 (Recommended)'), O8 left OPEN_ROWS for S10's note,
    #     and this is RE-PINNED 14 -> 13 to what statuses() returned after it.
    #   REFUSED 9 -> 10: S10, M's mechanism as a supply (gap None).
    #   M-D65-1 and M-D65-2 are rulings, not statuses, and move no count.
    # RE-PINNED BY DOCKET 64 to what statuses() returned after the edit (not
    # typed from the ruling, which did not predict it).  The moves only:
    #   D22 OPEN -> SURVEY (noise.py: C1 a THEOREM in the flat model; the
    #     corridor application a SURVEY).       SURVEY 1 -> 2, OPEN -1.
    #   D26 new, OPEN (linstab.py).             OPEN +1, so OPEN 10 -> 10.
    #   Linearised stability left WAITS_FOR_ITS_INSTRUMENT (not a status).
    #   O5 re-owned to hpscentre.py; D24 re-owned to formation.py.
    #   No row closed, none withdrawn, none refused.
    # RE-PINNED BY THE FIX PASS ON DOCKETS 62/63, to what statuses() returns:
    #   OPEN 7 -> 10: D23 (the first trip, transit.py), D24 (formation,
    #     create.py), D25 (the destination stock gate, stockgate.py) -- the
    #     principle: a question the tree already has an instrument for gets a
    #     row now.  Linearised stability has no instrument and is NOT opened;
    #     it is in WAITS_FOR_ITS_INSTRUMENT, for the calculations docket.
    #   REFUSED 8 -> 9: S9, warpfolder.py's device specification as a supply.
    # AND WHY NONE OF DOCKET 63's SECTION E IS AN O ROW (its census said "OPEN
    # 6 plus the O rows added from E").  The thirteen are unsettled questions
    # INTERNAL to the refused rows S6-S8 and to D20's figure, and E12 says in
    # terms that the H1/H2 split gates nothing: every verdict in B holds under
    # both hypotheses.  Read one by one, none gates a requirement --
    #   E1 cheapest stable source and E10 the Yukawa-running correction MOVE
    #     D20's MEASURED figure, which D20 already names as what would move it;
    #     S6 and S7 are refused on kind, not on that price.
    #   E2 fermion bag, E3 f = -2.45, E4 in-medium massless point, E5
    #     evanescent reach, E7 release of a phi = 0 region, E8 hot restored
    #     region, E11 macroscopic gauged configuration: each is a way the
    #     displacement might be sourced, held or extended, and each still
    #     needs a source filling the region (D16), so S6-S8 stand either way.
    #   E6 curvature sourcing is the xi != 0 case, which is S4 and O1, both
    #     refused already; E13 a BSM dilaton is outside the docket's subject.
    #   E9 endpoint.py's E1/E3a/E3 checks verify an instrument, and no row on
    #     this board is asked of those theorems -- the board asks endpoint.py
    #     only for Degrassi's scale, in S8's note.
    # Opening them would count one refusal's internal questions as openings,
    # which is the inflation S4's four wrong words once caused.
    # RE-PINNED BY DOCKETS 62 AND 63 to what statuses() returns after the edit.
    # The DOCKET 63 ruling's projection (THEOREM 16, OPEN 6 plus E) and the
    # DOCKET 62 ruling's (UNCHANGED) were predictions, and each was made
    # without the other docket or the fluctuation row:
    #   THEOREM 11 -> 17: D15-D19 (DOCKET 63) and D21 (DOCKET 62's lattice
    #     theorem, seated as its own row).
    #   MEASURED 2 -> 3: D20.
    #   OPEN 6 -> 7: D22, fluctuation.py.  DOCKET 62 closed none of O2, O3,
    #     O5, O6, O7 and opened nothing; S5 stays open.
    #   WITHDRAWN 8 -> 13: W9-W13.
    #   REFUSED 5 -> 8: S6-S8.
    # O4 joins O1: OPEN 7 -> 6, REFUSED 4 -> 5.  axial.py answered it in the
    # negative -- the axis costs the same sign the sphere does.
    chk("rows that left OPEN by being ANSWERED, kept rather than deleted",
        sorted(r[0] for r in CLOSED_ROWS), ["O1", "O4"])
    chk("and no id appears in two lists at once",
        len(set([r[0] for r in OPEN_ROWS] + [r[0] for r in CLOSED_ROWS])),
        len(OPEN_ROWS) + len(CLOSED_ROWS))
    chk("every closed row says how it closed",
        all(bool(r[2]) for r in CLOSED_ROWS), True)
    chk("every status used is one of the five plus REFUSED",
        set(r[2] for r in DEMAND + SUPPLY) <= set(STATUSES), True)
    chk("every demand row names what would move it",
        all(bool(r[4]) for r in DEMAND), True)
    chk("every open row names what would answer it",
        all(bool(r[2]) for r in OPEN_ROWS), True)
    chk("every withdrawn row names why it fell",
        all(bool(r[2]) for r in WITHDRAWN_ROWS), True)
    chk("the unaskable rows are named, not hidden", unaskable(),
        ("D5", "D6", "D12", "D13"))

    print("\n4b. DOCKET 62 CLOSED NOTHING, AND WHAT IT REFUSED IS NOT HERE")
    chk("no O row's owner says it closed",
        [r[0] for r in OPEN_ROWS if ask(r[3])], [])
    chk("the five narrowed rows are all still open",
        [r for r in DOCKET62_NARROWED if r not in [x[0] for x in OPEN_ROWS]], [])
    # DOCKET 65 opens no O row: the finite Higgs share, first seated as O8, is
    # an OPEN item in S10's note on M's ruling M-D65-2.  The five are asked for
    # by name (DOCKET62_NARROWED), and no other O row stands beside them.
    chk("  and there is no O row beside them (O8 folded into S10's note, M-D65-2)",
        sorted(r[0] for r in OPEN_ROWS if r[0] not in DOCKET62_NARROWED), [])
    # RE-KEYED BY DOCKET 64 (ruling C, O5).  This compared sorted ids with the
    # OPEN ids, and O5's second entry (DOCKET 64 replacing DOCKET 62's
    # wording) would have turned it red for a correct reason.  Entries are
    # keyed by (row, docket) now, and the check is on SETS.
    chk("every narrowed row's replaced wording is kept (as sets)",
        set(DOCKET62_NARROWED) <= set(r[0] for r in SUPERSEDED_WORDING),
        True)
    chk("  DOCKET 62's entries are exactly the five O rows it narrowed",
        sorted(r[0] for r in SUPERSEDED_WORDING if r[1] == "DOCKET 62"),
        sorted(DOCKET62_NARROWED))
    chk("  DOCKET 64's are the rows whose wording it replaced, not extended",
        sorted(r[0] for r in SUPERSEDED_WORDING if r[1] == "DOCKET 64"),
        ["D22", "D24", "O5"])
    chk("  DOCKET 65's is S5's replaced first sentence (it was the only priced "
        "row), and the sentence is no longer on S5",
        ([r[2] for r in SUPERSEDED_WORDING if r[1] == "DOCKET 65"],
         [r[0] for r in SUPERSEDED_WORDING if r[1] == "DOCKET 65"],
         any("THE ONLY ROW ON THIS LEDGER WITH A PRICE RATHER THAN A REFUSAL" in r[4]
             for r in SUPPLY if r[0] == "S5")),
        (["THE ONLY ROW ON THIS LEDGER WITH A PRICE RATHER THAN A REFUSAL"], ["S5"],
         False))
    chk("  the section header names the dockets the table holds, built from it",
        (superseded_dockets(),
         "## Row wording replaced by DOCKETS 62, 64 and 65" in to_markdown()),
        ("62, 64 and 65", True))
    chk("  CONTROL: the table without its DOCKET 65 entry would print the old "
        "header, '62 and 64' (built, not typed)",
        superseded_dockets([r for r in SUPERSEDED_WORDING if r[1] != "DOCKET 65"]),
        "62 and 64")
    chk("  no (row, docket) key is used twice",
        _superseded_keys_unique(SUPERSEDED_WORDING), True)
    chk("  CONTROL: a duplicated (row, docket) key is caught",
        _superseded_keys_unique(SUPERSEDED_WORDING + SUPERSEDED_WORDING[:1]),
        False)
    chk("  every superseded id is a row on this board",
        [r[0] for r in SUPERSEDED_WORDING
         if r[0] not in [x[0] for x in DEMAND + SUPPLY + OPEN_ROWS]], [])
    chk("and each says why it was replaced",
        all(bool(r[3]) for r in SUPERSEDED_WORDING), True)
    chk("  O5's DOCKET 62 wording is kept verbatim as the board printed it",
        [r[2] for r in SUPERSEDED_WORDING
         if r[:2] == ("O5", "DOCKET 64")],
        [O5_DOCKET62[0] + " || " + O5_DOCKET62[1]])
    ids = [r[0] for r in DEMAND + SUPPLY + OPEN_ROWS + CLOSED_ROWS
           + WITHDRAWN_ROWS]
    chk("no R-1 row (it is O7 renamed) -- and its owner agrees",
        ("R-1" in ids, branelink.R1_ROW_OPENED), (False, False))
    chk("no separate NEC-everywhere row (it is O3 with a clause)",
        latticectc.NEC_EVERYWHERE_ROW_OPENED, False)
    chk("no Caldwell & Langlois withdrawal (it has no referent)",
        (latticectc.CALDWELL_LANGLOIS_WITHDRAWAL_SEATED,
         any("Caldwell" in r[1] for r in WITHDRAWN_ROWS)), (False, False))
    chk("no id is used twice anywhere on the board",
        len(ids), len(set(ids)))
    # The refused figures: the curvature-tightened persistence shortfall, its
    # redshift-loosened variant, and the void 9/64 adjustment.  Rendered
    # nowhere.  The needles are the owner's own computed values, so this fires
    # if any is ever printed at the precision the ruling refused.
    flat, curved, loosened = fewsterteo.refused_figures()
    md = to_markdown()
    needles = ["%.3f" % curved, "%.3f" % loosened,
               "%.6f" % fewsterteo.refused_void_adjustment(),
               "%.3f" % fewsterteo.WITNESS_ORDERS]
    chk("the refused figures appear nowhere in LEDGER.md",
        [n for n in needles if n in md], [])
    chk("  CONTROL: the needle search finds the figure that stands",
        "%.3f" % flat in md, True)
    chk("  CONTROL: and fires on a copy with a refused figure planted",
        [n for n in needles if n in md + needles[0]], needles[:1])
    chk("the 9/64 is not applied to C_F, on its owner",
        fewsterteo.NINE_64_APPLIES_TO_C_F, False)
    # O5, DOCKET 64: re-owned to hpscentre.py; every figure asked.
    o5 = [r for r in OPEN_ROWS if r[0] == "O5"][0]
    chk("O5 is asked of hpscentre.py, which says it did not close",
        (o5[3], ask(o5[3]), throatmass.O5_CLOSED),
        (("hpscentre", "O5_CLOSED"), False, False))
    chk("  m < 0 found in HPS's system, NOT inside the established domain",
        (hpscentre.M_NEGATIVE_FOUND_IN_HPS_SYSTEM,
         hpscentre.M_NEGATIVE_FOUND_INSIDE_DOMAIN,
         hpscentre.THROAT_M_NEGATIVE_READING, hpscentre.AHS_REACHED),
        (True, False, "CONSERVED", False))
    chk("  which system HPS integrated is NOT DETERMINED (the claim withdrawn)",
        (hpscentre.HPS_INTEGRATED_THE_PRINTED_SYSTEM,
         "NOT DETERMINED" in o5[1]), ("NOT DETERMINED", True))
    # The two instruments found the repairs independently; this compares
    # qeihps.py's scan with hpscentre.py's printed -> conserved change, so a
    # disagreement between the peers turns it red.
    chk("  qeihps.py's two repairs ARE hpscentre.py's printed -> conserved",
        (qeihps.REPAIR_CONSERVATION[2:],
         qeihps.REPAIR_DIMENSION[2:],
         hpscentre.PRINTED["a_th"] == hpscentre.CONSERVED["a_th"]),
        ((hpscentre.PRINTED["a_tt"], hpscentre.CONSERVED["a_tt"]),
         (_hps_ll_denominator(hpscentre.PRINTED["ll_pow"]),
          _hps_ll_denominator(hpscentre.CONSERVED["ll_pow"])), True))
    chk("  the first m < 0 is printed as the owner pins it, in l_P",
        ("first at %.4f l_P" % hpscentre.FIRST_NEGATIVE_M_THROAT_LP) in o5[1],
        True)
    chk("  the throat-geodesic verdict is qeihps.py's 'NOT A TEST'",
        (qeihps.VERDICT_THROAT_GEODESIC.startswith("NOT A TEST"),
         ("On the throat geodesic: " + qeihps.VERDICT_THROAT_GEODESIC)
         in o5[1]), (True, True))
    chk("  Kontou's test is the owner's (FO and FFKP both OPEN), F-S REFUSED",
        (qeihps.KONTOU_REQUEST_FOUND,
         qeihps.KONTOU_REQUESTED_TEST_ON_HPS in o5[1],
         qeihps.FEWSTER_SMITH_ON_HPS.startswith("REFUSED"),
         qeihps.DOCKET62_INSTRUMENT_STANDS), (True, True, True, False))
    _tm = "-- %s, not NO" % throatmass.NEGATIVE_MASS_SELF_CONSISTENT_FOUND
    chk("  throatmass's NOT-FOUND is no longer printed as the tree's finding",
        (_tm in o5[1], _tm in O5_DOCKET62[0]), (False, True))
    chk("  and O5 answers with hpscentre.O5_ANSWERED_BY, not throatmass's",
        o5[2], hpscentre.O5_ANSWERED_BY)
    chk("O5's narrowing #3 is demoted on its owner",
        (throatmass.NO_QEI_CAN_BOUND_RHO_REN,
         throatmass.SEPARATES_O5_FROM_O2_PERMANENTLY), (False, False))
    chk("O7's B is unmeasured on its owner", branelink.B_MEASURED, False)
    o6 = [r for r in OPEN_ROWS if r[0] == "O6"][0][1]
    chk("O6 says its saving is at the UNTESTED B = 0, figure from branelink",
        ("UNTESTED B = 0" in o6,
         ("%.1f ns" % branelink.SAVING_AT_B0_NS) in o6), (True, True))
    s8 = [r for r in SUPPLY if r[0] == "S8"][0][4]
    chk("S8 prints excite.py's full band and its centre, not the ruling's",
        all(("%.0e" % v) in s8 for v in excite.XI_FIELD_OVER_INSTABILITY),
        True)
    chk("O6's cause of death is refuted on its owner, and it did not close",
        (branelink.O6_CAUSE_OF_DEATH_REFUTED, branelink.O6_CLOSED),
        (True, False))
    chk("O5 declines Flanagan-Wald and Sanders 5.1 on its owner",
        (throatmass.FLANAGAN_WALD_APPLIED, throatmass.SANDERS_51_APPLIED),
        (False, False))
    chk("O2's Sec. 7 is not transplanted to M < 0 on its owner",
        fewsterteo.SEC7_TRANSPLANTABLE_TO_NEGATIVE_M, False)
    chk("fluctuation.py's own flag that it moves no row is unmoved",
        fluctuation.LEDGER_ROW_MOVES, False)
    o2 = [r for r in OPEN_ROWS if r[0] == "O2"][0]
    chk("O2's answer now names D22's curved question (ruling C addendum)",
        ("D22's distribution question" in o2[2],
         "note [18]" in o2[2]), (True, True))

    print("\n4c. DOCKET 64: WHAT WAS WITHDRAWN OR CORRECTED IS NOT PRINTED")
    # Each needle is a wording a DOCKET 64 verifier or computation withdrew.
    # LEDGER.md must carry none of them; the superseded and withdrawn tables
    # hold only the board's OWN earlier wording, which contains none.
    needles64 = _withdrawn_needles_64()
    md = to_markdown()
    chk("no withdrawn DOCKET 64 wording appears in LEDGER.md",
        [n for n in needles64 if n.lower() in md.lower()], [])
    chk("  CONTROL: the search fires on a copy with one planted",
        [n for n in needles64
         if n.lower() in (md + needles64[2]).lower()], [needles64[2]])
    chk("  each withdrawal is kept on its owner, not deleted",
        (len(noise.WITHDRAWN) > 0, len(hpscentre.WITHDRAWN) > 0,
         len(linstab.WITHDRAWN) > 0,
         qeihps.VERDICT_THROAT_GEODESIC_WITHDRAWN.startswith("WITHDRAWN"),
         formation.D25_VERDICT_WITHDRAWN.startswith("WITHDRAWN")),
        (True, True, True, True, True))
    # No cell DOCKET 64 made long is cut in LEDGER.md: a cut drops the end of
    # a claim, which is where its qualification sits.
    cut = _truncated_cells()
    chk("no demand, open, superseded or pending cell is cut in LEDGER.md",
        cut, [])
    chk("  CONTROL: at the widths before DOCKET 64 it would have cut some",
        len(_truncated_cells(demand_claim=900, open_claim=1400,
                             open_answer=600, was=900, why=400)) > 0, True)

    print("\n4d. DOCKET 65: EVERY SEATED ROW IS massform.py's, ASKED")
    row = dict((r[0], r) for r in DEMAND + SUPPLY)
    opn = dict((r[0], r) for r in OPEN_ROWS)
    chk("D27-D29 are massform's rows exactly (claim, status, owner, movers)",
        [rid for rid in ("D27", "D28", "D29")
         if row[rid][1:] != tuple(massform.PROPOSED_ROWS[
             [p[0] for p in massform.PROPOSED_ROWS].index(rid)][2:])], [])
    chk("  each a THEOREM, owned by massform",
        [(row[r][2], row[r][3][0]) for r in ("D27", "D28", "D29")],
        [(THEOREM, "massform")] * 3)
    chk("S10's status IS massform.MECHANISM_VERDICT[0], REFUSED, asked of it",
        (row["S10"][2], massform.MECHANISM_VERDICT[0], row["S10"][3]),
        (REFUSED, REFUSED, ("massform", "MECHANISM_VERDICT")))
    chk("S11-S13 are OPEN, owned by the flags that say each route is PRICED",
        [(row[r][2], row[r][3], ask(row[r][3])) for r in ("S11", "S12", "S13")],
        [(OPEN, ("massform", a), True) for a in (
            "ANOMALY_ROUTE_PRICED", "PAIR_ROUTE_PRICED", "HELD_SEAT_ROUTE_PRICED")])
    chk("  each note carries massform's claim and its movers, uncut",
        [r for r in ("S10", "S11", "S12", "S13")
         if not (PROPOSED[r][2] in row[r][4] and PROPOSED[r][5] in row[r][4])], [])
    chk("  and their names are massform.SURVIVES's, asked, one route each",
        (all(row[r][1] in [n for n, _t in massform.SURVIVES]
             for r in ("S11", "S12", "S13")),
         len(set(row[r][1] for r in ("S11", "S12", "S13")))), (True, 3))
    # M-D65-2 (RULED_BY_M): 'Fold into S10 (Recommended)'.  The finite share
    # is an OPEN item inside S10's note, asked of massform, and no row.
    chk("the finite share (massform's S10 (open)) is in S10's note, text and "
        "movers asked, OPEN on its owner, and is no row (M-D65-2)",
        (PROPOSED["S10 (open)"][2] in row["S10"][4],
         PROPOSED["S10 (open)"][5] in row["S10"][4],
         "not a row (M-D65-2)" in row["S10"][4],
         massform.FINITE_HIGGS_SHARE_STATUS,
         [r[0] for r in OPEN_ROWS if r[0] == "O8" or "FINITE Higgs share" in r[1]],
         "S10 (open)" in [r[0] for r in DEMAND + SUPPLY + OPEN_ROWS]),
        (True, True, True, OPEN, [], False))
    _keep = massform.FINITE_HIGGS_SHARE_STATUS
    massform.FINITE_HIGGS_SHARE_STATUS = "COMPUTED"
    try:
        _raised = False
        try:
            _s10_open_item()
        except ValueError:
            _raised = True
    finally:
        massform.FINITE_HIGGS_SHARE_STATUS = _keep
    chk("  CONTROL: a finite share no longer OPEN on its owner is not carried as "
        "an OPEN item (it raises)", _raised, True)
    chk("S5 stays OPEN and its note carries DOCKET 65's append, asked",
        (row["S5"][2], _s5_docket65_append() in row["S5"][4],
         massform.RECONSTRUCTION_SURVIVES), (OPEN, True, True))
    chk("S5 no longer claims to be the only priced row (S11-S13 are priced)",
        ("THE ONLY ROW ON THIS LEDGER WITH A PRICE" in row["S5"][4],
         "S11-S13" in row["S5"][4]), (False, True))
    chk("massform asks D23 of this board, and gets this board's row",
        massform.d23_row()[:4] == [r for r in DEMAND if r[0] == "D23"][0][:4],
        True)
    chk("  and its held-seat route needs that prior arrival",
        massform.preparation_needs_prior_arrival(), True)
    _qet = [r for r in RULED_BY_M if r[0] == "M-D65-1"]
    chk("M-D65-1: QET folded into DOCKET 66, M quoted, literature CITED not READ",
        (len(_qet), _qet[0][3].startswith("RULED BY M: FOLD INTO DOCKET 66"),
         "'%s'" % M_D65_1_ANSWER in _qet[0][3],
         M_D65_1_WORDS in _qet[0][2],
         "CITED, not READ" in _qet[0][2],
         all(a in _qet[0][2] for a in ("Hotta 2008", "1701.03805",
                                       "2301.02666", "2505.04689", "2506.19878"))),
        (1, True, True, True, True, True))
    _raw = to_markdown()
    _md = " ".join(_raw.split())
    chk("M's words in M-D65-1 are ONE sentence wherever printed: `why`, the "
        "ruling cell and LEDGER.md each quote exactly M_D65_1_WORDS",
        verbatim_faults(_qet[0], _raw), [])
    for _where, _mut in ((3, "ruling cell"), (2, "why"), (None, "LEDGER.md line")):
        _q = list(_qet[0])
        _m = _raw
        _bad = "consider that the introduction"
        if _where is None:
            _m = _raw.replace("consider the idea that the introduction", _bad)
        else:
            _q[_where] = _q[_where].replace("consider the idea that the introduction",
                                            _bad, 1)
        chk("  CONTROL: 'consider the idea that the' shortened in the %s only is "
            "caught" % _mut, len(verbatim_faults(tuple(_q), _m)) > 0, True)
    chk("  CONTROL: a copy of M's words dropped from the ruling cell is caught",
        len(verbatim_faults((_qet[0][0], _qet[0][1], _qet[0][2],
                             _qet[0][3].replace("verbatim: '", "roughly: '"),
                             _qet[0][4]), _raw)) > 0, True)
    _ms2 = [r for r in RULED_BY_M if r[0] == "M-D65-2"]
    chk("M-D65-2 is RULED: the question exactly as put to M, M's answer "
        "verbatim, the fold APPLIED, and nothing pending",
        (len(_ms2), _ms2[0][1] == M_D65_2_QUESTION,
         _ms2[0][3].startswith("RULED BY M: FOLD INTO S10's NOTE"),
         "M's answer: '%s'" % M_D65_2_ANSWER in _ms2[0][3],
         all("'%s'" % f in _ms2[0][2] for f in M_D65_2_OPTION),
         M_D65_2_QUESTION in _md, "'%s'" % M_D65_2_ANSWER in _md,
         PENDING_RULINGS, "O8" not in [r[0] for r in OPEN_ROWS]),
        (1, True, True, True, True, True, True, [], True))
    chk("  and M-D65-1 opens no row (QET is DOCKET 66's, not the board's)",
        [r[0] for r in DEMAND + SUPPLY + OPEN_ROWS if "QET" in r[1]
         or "Teleportation" in r[1]], [])
    chk("D27-D29's owners still SAY what the THEOREM rows say (values, asked)",
        theorem_owner_disagreements(), [])
    for _attr, _flip, _rid in (("CONSIDERATION_HOLDS", False, "D27"),
                               ("HIGGS_FIELD_SUPPLIES_THE_MASS_ENERGY", True, "D29")):
        _keep = getattr(massform, _attr)
        setattr(massform, _attr, _flip)
        try:
            _got = theorem_owner_disagreements()
        finally:
            setattr(massform, _attr, _keep)
        chk("  CONTROL: massform.%s -> %s is caught on %s" % (_attr, _flip, _rid),
            _got, [_rid])
    _keep = massform.pair_floor_j
    massform.pair_floor_j = lambda c=None: _keep(c) / 2.0
    try:
        _got = theorem_owner_disagreements()
    finally:
        massform.pair_floor_j = _keep
    chk("  CONTROL: massform.pair_floor_j halved is caught on D28", _got, ["D28"])
    chk("every DOCKET 65 qualifier is on its seated row, as often as pinned",
        missing_qualifiers(), [])
    _rows = dict((r[0], r) for r in DEMAND + SUPPLY + OPEN_ROWS)
    _ctl = [(rid, phrase) for rid, need in SEATED_QUALIFIERS.items()
            for phrase, _n in need
            if not any(q[:2] == (rid, phrase) for q in missing_qualifiers(
                dict(_rows, **{rid: tuple(x.replace(phrase, "", 1)
                                          if isinstance(x, str) and phrase in x
                                          else x for x in _rows[rid])})))]
    chk("  CONTROL: deleting any one qualifier from its row is caught (each)",
        _ctl, [])
    _d28 = dict(_rows, D28=tuple(x.replace("costs at least ", "costs ", 1)
                                 if isinstance(x, str) else x for x in _rows["D28"]))
    chk("  CONTROL: D28 with 'at least' deleted (a floor read as an exact cost) "
        "is caught", [q[:2] for q in missing_qualifiers(_d28) if q[0] == "D28"],
        [("D28", "costs at least")])
    chk("M-D65-1 as LEDGER.md PRINTS it: M's whole sentence, CITED not READ, "
        "the anchors; no ruling's question, ruling or unblocks cell is cut",
        (M_D65_1_WORDS in _md,
         "consider the idea that the introduction of information" in _md,
         "CITED, not READ" in _md,
         all(a in _md for a in ("Hotta 2008", "arXiv:1701.03805",
                                "arXiv:2301.02666", "arXiv:2505.04689",
                                "arXiv:2506.19878")),
         [c for c in _truncated_cells() if c[0] == "ruled"]),
        (True, True, True, True, []))
    chk("the finite share is NOT a row, on M's ruling, stated in the docstring "
        "(sections 4 and 6) and in the census comment's re-pin",
        ("NOT A ROW, ON M's\n       RULING M-D65-2" in __doc__,
         "S10 (open)     NOT A ROW" in __doc__,
         "Nothing from\nDOCKET 65 is pending M" in __doc__,
         "O8   the FINITE Higgs share" in __doc__), (True, True, True, False))
    _buf = io.StringIO()
    with contextlib.redirect_stdout(_buf):
        report()
    _rep = " ".join(_buf.getvalue().split())
    chk("the plain report prints S10's name whole and massform.mechanism_label() "
        "whole beside it (a cut there read as a bare refusal)",
        (S10_NAME in _rep, " ".join(massform.mechanism_label().split()) in _rep),
        (True, True))
    chk("nothing DOCKET 65 seated carries the status word DECLARED",
        [r[0] for r in massform.PROPOSED_ROWS if "DECLARED" in r[3]], [])
    # DOCKET 65's closing round.
    _seated65 = {"D27", "D28", "D29", "S10", "S11", "S12", "S13", "S10 (open)",
                 "S5 (note)"}
    chk("massform.PROPOSED_ROWS' ids are exactly what this board seats from "
        "DOCKET 65 (the rows, the S10 (open) item and the S5 append)",
        set(r[0] for r in massform.PROPOSED_ROWS), _seated65)
    chk("  CONTROL: a proposed row this board does not seat (D30) is caught here",
        set(r[0] for r in massform.PROPOSED_ROWS + (("D30",),)) == _seated65, False)
    chk("every seated row's text DIRECTION agrees with the owner value it states "
        "(POLARITY: phrase on the row, owner asked)", polarity_faults(), [])
    _inv = {"arrival switches nothing on": "arrival switches the field on",
            "costs at least": "costs",
            "leaves B units of antibaryon number": "leaves nothing",
            "has no energy to give about v": "has energy to give about v",
            "REFUSED, gap None": "PRICED, gap None",
            "exp(-4 pi/alpha_W) per transition": "no price per transition",
            "extra leptons (D28)": "no extra leptons",
            "Two-particle collisions: CONTESTED": "Two-particle collisions: SETTLED",
            "Priced, not refused": "Refused, not priced",
            "PRICED at eps": "REFUSED at eps",
            "survives M's mechanism: no mass forms at the seat":
                "is refused with M's mechanism: mass forms at the seat"}
    _ctl = []
    for _rid, _phrase, _p in POLARITY:
        _r2 = dict(_rows, **{_rid: tuple(x.replace(_phrase, _inv[_phrase], 1)
                                          if isinstance(x, str) else x
                                          for x in _rows[_rid])})
        if (_rid, _phrase, "phrase missing") not in polarity_faults(_r2):
            _ctl.append((_rid, _phrase))
    chk("  CONTROL: each phrase inverted on a private copy of its row is caught",
        _ctl, [])
    for _attr, _flip, _rid, _phrase in (
            ("FIELD_SWITCHED_ON_BY_ARRIVAL", True, "D27", "arrival switches nothing on"),
            ("PAIR_ROUTE_PRICED", False, "S12", "Priced, not refused"),
            ("RECONSTRUCTION_SURVIVES", False, "S5",
             "survives M's mechanism: no mass forms at the seat")):
        _keep = getattr(massform, _attr)
        setattr(massform, _attr, _flip)
        try:
            _got = polarity_faults()
        finally:
            setattr(massform, _attr, _keep)
        chk("  CONTROL: massform.%s -> %s is caught on %s (owner disagrees)"
            % (_attr, _flip, _rid), _got, [(_rid, _phrase, "owner disagrees")])
    chk("S10's label is a label for M's mechanism, not a refusal of what S12 "
        "and S13 price", s10_name_faults(), [])
    chk("  CONTROL: 'atomic mass formed at the seat' as the label is caught",
        len(s10_name_faults("atomic mass formed at the seat")), 2)
    chk("M-D65-1 names the literature as it was named to M (arXiv:2506.19878 "
        "included), QET TO BE tested in DOCKET 66 (NOT YET RUN), and the "
        "question's parenthetical as the question's description, not READ",
        m_d65_1_faults(), [])
    _q1 = list(_qet[0])
    _q1[3] = _q1[3].replace("QET is to be tested inside DOCKET 66 (NOT YET RUN)",
                            "QET is tested inside DOCKET 66")
    _q2 = list(_qet[0])
    _q2[2] = _q2[2].replace("; arXiv:2506.19878", "")
    _q3 = list(_qet[0])
    _q3[3] = _q3[3].replace("; the question's parenthetical is the question's "
                            "description as put to M, not READ", "")
    chk("  CONTROL: the old wording ('QET is tested inside DOCKET 66'), the "
        "literature without 2506.19878, and the parenthetical unattributed are "
        "each caught",
        [len(m_d65_1_faults(tuple(q))) > 0 for q in (_q1, _q2, _q3)], [True] * 3)
    chk("M-S1A-P1's unblocks cell says DOCKET 65 has run and names its rows, "
        "built from massform's ids", p1_unblocks_faults(), [])
    chk("  CONTROL: the cell as it stood ('DOCKET 65 opens' alone) is caught",
        len(p1_unblocks_faults("S-1 stands NONEMPTY with no contraction "
                               "requirement; DOCKET 65 opens")), 1)
    _d67 = [r for r in RULED_BY_M if r[0] == "M-D65-3"]
    chk("M-D65-3: DOCKET 67 OPENED by M -- the question exactly as put to M, "
        "M's answer verbatim, M's words verbatim in `why`, the ruling cell and "
        "LEDGER.md, NOT YET RUN and its order in what it unblocks",
        (len(_d67), _d67[0][1] == M_D65_3_QUESTION,
         _d67[0][3].startswith("RULED BY M: OPEN IT -- M's answer: '%s'"
                               % M_D65_3_ANSWER),
         verbatim_faults(_d67[0], _raw, rid="M-D65-3"),
         "NOT YET RUN" in _d67[0][4],
         "after DOCKET 65 is seated and before DOCKET 66" in _d67[0][4],
         M_D65_3_QUESTION in _md, "'%s'" % M_D65_3_ANSWER in _md),
        (1, True, True, [], True, True, True, True))
    # EQUALITY, not substring presence: the seated cells must EQUAL their
    # templates filled from the asked constants, so no verdict on a docket
    # that has not run can be typed beside the required phrases (a planted
    # 'DOCKET 67 has run: every audited result STANDS' passed substring
    # guards green).
    chk("  M-D65-3's ruling cell EQUALS M_D65_3_RULING_T filled from M's answer "
        "and M's words, and `why` EQUALS the owners' record (m_d65_3_why())",
        (_d67[0][3] == M_D65_3_RULING_T % (M_D65_3_ANSWER, M_D65_3_WORDS),
         _d67[0][2] == m_d65_3_why()), (True, True))
    chk("  CONTROL: 'DOCKET 67 has run: every audited result STANDS' planted in "
        "the ruling cell is caught",
        _d67[0][3] + "  DOCKET 67 has run: every audited result STANDS"
        == M_D65_3_RULING_T % (M_D65_3_ANSWER, M_D65_3_WORDS), False)
    _verdict = re.compile(r"\b(has run|HAS RUN|STANDS|WRONG|NARROWED|cannot|"
                          r"fails|expected to|is not exotic|no negative)\b")
    chk("  no template carries a verdict word in the board's own words "
        "(either direction) -- STANDS / NARROWED / WRONG enter only inside M's "
        "asked question; M-D65-4's ruling and `why` templates are scanned too",
        (_verdict.findall(M_D65_3_RULING_T), _verdict.findall(M_D65_3_WHY_T),
         _verdict.findall(M_D65_4_RULING_T), _verdict.findall(M_D65_4_WHY_T),
         _verdict.findall(M_D65_4_UNBLOCKS_T)), ([], [], [], [], []))
    _nf, _nne = fluctuation_discrepancies()
    _nm = len(massform_divergences())
    chk("  the characterisation in `why` is the owners': fluctuation's preprint "
        "version and its journal clause, massform's own heading, the p.7 "
        "pairing beside the p.2 one -- and 'published errors' is nowhere",
        ("against arXiv gr-qc/9304008 v1" in _d67[0][2],
         "MUST NOT be quoted as errors in the journal version until it is read"
         in _d67[0][2],
         "'DIVERGENCES FROM THE SOURCES, RECORDED AND NOT REPAIRED'" in _d67[0][2],
         "their p.7 pairing, 1/%g, gives 10^%.2f" % (
             massform.TW_ALPHA_INV[0],
             massform.log10_suppression(1.0 / massform.TW_ALPHA_INV[0])) in _d67[0][2],
         "published errors" in _d67[0][2], "published errors" in M_D65_3_WHY_T),
        (True, True, True, True, False, False))
    chk("  the lead-in's COUNTS are the owners': the printed '%d of the %d "
        "discrepancies' equals the count of fluctuation's KF flags recomputed "
        "here (KF_*_IS_EXACT False + the claim flag False + the typographical "
        "flag True), the printed '%d of the %d divergences' equals the sentences "
        "under massform's heading, the nouns are the owners' ('discrepancies', "
        "'refuted', 'typographical', 'divergences'), the framing is scoped to "
        "the cited items, and 'refutation' is nowhere"
        % (len(M_D65_3_WHY_ITEMS_FLUCT), _nf, len(M_D65_3_WHY_ITEMS_MASS), _nm),
        ("%d of the %d discrepancies fluctuation.py records against a preprint "
         "version" % (len(M_D65_3_WHY_ITEMS_FLUCT), _nf) in _d67[0][2],
         _nf == sum(1 for k in ("KF_216_FINAL_IS_EXACT", "KF_37_IS_EXACT",
                                "KF_38_IS_EXACT", "KF_319_IS_EXACT", "KF_323_IS_EXACT")
                    if getattr(fluctuation, k) is False)
         + (not fluctuation.KF_CLAIM_NEGATIVE_MEANS_DELTA_GT_1)
         + fluctuation.KF_341_HALF_IS_TYPOGRAPHICAL,
         "the rest, %d KF_*_IS_EXACT flags False" % _nne in _d67[0][2],
         "%d of the %d divergences massform.py records under its own heading"
         % (len(M_D65_3_WHY_ITEMS_MASS), _nm) in _d67[0][2],
         _nm == len(re.findall(r"\.(?:\s|$)", " ".join(re.search(
             r"RECORDED AND NOT REPAIRED\.(.*?)\n\n", massform.__doc__, re.S)
             .group(1).split()) + " ")),
         'FALSE by z3 -- "refuted" -- and (3.41)\'s 1/2 "typographical"' in _d67[0][2],
         "Of what this project has recorded against outside results, the items "
         "whose owners expose flags asked here" in _d67[0][2],
         "refutation" in _d67[0][2], "refutation" in M_D65_3_WHY_T,
         "What this project has already RECORDED" in _d67[0][2]),
        (True, True, True, True, True, True, True, False, False, False))
    chk("  fluctuation's balancing verdict is in `why`, asked of its flags: the "
        "conclusion SURVIVES and no ledger row moves",
        ("Kuo & Ford's qualitative conclusion SURVIVES (fluctuation.KF_QUALITATIVE_"
         "CONCLUSION_SURVIVES = True) and no ledger row moves (fluctuation."
         "LEDGER_ROW_MOVES = False)" in _d67[0][2],
         fluctuation.KF_QUALITATIVE_CONCLUSION_SURVIVES, fluctuation.LEDGER_ROW_MOVES),
        (True, True, False))
    chk("  CONTROL: the lead-in as it stood ('Three published errors this project "
        "has already caught') planted in `why` is caught",
        _d67[0][2].replace("Of what this project has recorded against outside "
                           "results", "Three published errors this project "
                           "has already caught") == m_d65_3_why(), False)
    chk("  CONTROL: the typed count as it stood ('two refutations of a preprint "
        "version and two divergences') planted in `why` is caught, and would "
        "carry 'refutation'",
        (_d67[0][2].replace(
            "%d of the %d discrepancies fluctuation.py records against a preprint "
            "version" % (len(M_D65_3_WHY_ITEMS_FLUCT), _nf),
            "two refutations of a preprint version and two divergences")
         == m_d65_3_why(),
         "refutation" in "two refutations of a preprint version and two divergences"),
        (False, True))
    # The template follows the owner: a KF flag flipped (here, in-process and
    # restored) moves the printed count, and the SURVIVES clause moves with
    # its flag.
    _kf, _sv = fluctuation.KF_319_IS_EXACT, fluctuation.KF_QUALITATIVE_CONCLUSION_SURVIVES
    try:
        fluctuation.KF_319_IS_EXACT = True
        fluctuation.KF_QUALITATIVE_CONCLUSION_SURVIVES = False
        _moved = m_d65_3_why()
    finally:
        fluctuation.KF_319_IS_EXACT, fluctuation.KF_QUALITATIVE_CONCLUSION_SURVIVES = _kf, _sv
    chk("  CONTROL: fluctuation.KF_319_IS_EXACT flipped True moves the printed "
        "count to %d, and its conclusion flag flipped moves the verdict clause "
        "(the template follows the owner)" % (_nf - 1),
        ("%d of the %d discrepancies" % (len(M_D65_3_WHY_ITEMS_FLUCT), _nf - 1) in _moved,
         "the rest, %d KF_*_IS_EXACT flags False" % (_nne - 1) in _moved,
         "conclusion does NOT survive, AGAINST fluctuation.py's record" in _moved,
         _moved == m_d65_3_why()), (True, True, True, False))
    chk("  the figures in `why` are the owners' (regenerated now: KF flags, TW "
        "p.2 and p.7, RS96)",
        ("KF_CLAIM_NEGATIVE_MEANS_DELTA_GT_1 = %s" % fluctuation.KF_CLAIM_NEGATIVE_MEANS_DELTA_GT_1
         in _d67[0][2],
         fluctuation.KF_CLAIM_NEGATIVE_MEANS_DELTA_GT_1, fluctuation.JOURNAL_VERSION_READ,
         "KF_341_HALF_IS_TYPOGRAPHICAL = %s" % fluctuation.KF_341_HALF_IS_TYPOGRAPHICAL
         in _d67[0][2],
         "prints 10^%.0f at alpha_W ~ 1/%g where the arithmetic gives 10^%.2f, %.2f "
         "decades off" % (massform.TW_PRINTED_LOG10, massform.TW_ALPHA_INV[1],
                          massform.log10_suppression(1.0 / massform.TW_ALPHA_INV[1]),
                          abs(massform.log10_suppression(1.0 / massform.TW_ALPHA_INV[1])
                              - massform.TW_PRINTED_LOG10)) in _d67[0][2],
         "prints 10^%.0f at alpha_W = 1/%g where the arithmetic gives 10^%.2f"
         % (massform.RS96_PRINTED_LOG10, massform.RS96_ALPHA_INV,
            massform.log10_suppression(1.0 / massform.RS96_ALPHA_INV)) in _d67[0][2]),
        (True, False, False, True, True, True))
    _d4 = [r for r in RULED_BY_M if r[0] == "M-D65-4"]
    _d63span, _d63text = paper_d63_marker()
    chk("M-D65-4: the paper's caveat (b) QUALIFIED on M's ruling -- the question "
        "as put to M, M's answer verbatim, the ruling cell EQUAL to its template "
        "filled from the asked pieces (M's rule for the paper, the DOCKET 63 "
        "marker READ back), `why` EQUAL to its template, unblocks EQUAL to its "
        "template (M's rule for the paper stands), printed in LEDGER.md",
        (len(_d4), _d4[0][1] == M_D65_4_QUESTION,
         _d4[0][3] == m_d65_4_ruling(),
         _d4[0][3] == M_D65_4_RULING_T % (M_D65_4_ANSWER, PAPER_CAVEAT_B_LINE,
                                          PAPER_CAVEAT_B_CLAUSE, M_PAPER_RULE_WORDS,
                                          _d63span, _d63text),
         _d4[0][2] == m_d65_4_why(),
         "'%s'" % M_D65_4_ANSWER in _d4[0][3],
         _d4[0][4] == M_D65_4_UNBLOCKS_T % M_PAPER_RULE_WORDS,
         M_D65_4_QUESTION in _md, "'%s'" % M_D65_4_ANSWER in _md,
         "M's ruling on\nthe paper's caveat (b) is M-D65-4" in __doc__),
        (1, True, True, True, True, True, True, True, True, True))
    chk("  M's rule for the paper (M_PAPER_RULE_WORDS) is printed wherever it is "
        "invoked -- the ruling cell, the unblocks cell, LEDGER.md -- with its "
        "provenance ('verbatim from the session, witnessed by the lead'), and "
        "the docstring names it",
        (M_PAPER_RULE_WORDS in _d4[0][3], M_PAPER_RULE_WORDS in _d4[0][4],
         _md.count(M_PAPER_RULE_WORDS),
         _d4[0][3].count("verbatim from the session, witnessed by the lead"),
         "M_PAPER_RULE_WORDS" in __doc__),
        (True, True, 2, 1, True))
    chk("  paper/CLAIMS.md:%s, READ now, carries DOCKET 63's marker with both "
        "fragments ('(Corrected on M's ruling:', 'DOCKET 63'), and the ruling "
        "cell names it by its READ lines and text -- the paper's edits on M's "
        "ruling are named, not counted ('the one', 'the second', 'two' absent)"
        % _d63span,
        (paper_d63_faults(), _d63span.startswith("%d" % PAPER_D63_MARKER_LINE),
         "(Corrected on M's ruling:" in _d63text, "DOCKET 63" in _d63text,
         "(paper/CLAIMS.md:%s: \"%s\")" % (_d63span, _d63text) in _d4[0][3],
         bool(re.search(r"\b(the one|the second|two) paper edits?\b",
                        _d4[0][3] + " " + _d4[0][4] + " " + __doc__))),
        ([], True, True, True, True, False))
    chk("  CONTROL: the marker altered in a private copy of the paper's lines "
        "(the fragment '(Corrected on M's ruling:' dropped; 'DOCKET 63' dropped; "
        "the marker moved off line %d) is caught each way" % PAPER_D63_MARKER_LINE,
        (paper_d63_faults([l.replace("(Corrected on M's ruling:", "(Corrected:")
                           for l in _paper_lines()]) != [],
         paper_d63_faults([l.replace("DOCKET 63", "DOCKET 6") for l in _paper_lines()]) != [],
         paper_d63_faults([""] + _paper_lines()) != []),
        (True, True, True))
    _srcs = {"ledger.py": open(__file__, encoding="utf-8").read(),
             "specthm.py": open(HERE + "/specthm.py", encoding="utf-8").read(),
             "LEDGER.md": _raw}
    # The withdrawn phrases are assembled from pieces here, so the source
    # scan finds them nowhere but where a planted copy would put them.
    _old_edit = "the one paper edit since M " + "finalis" + "ed it, on M's ruling"
    _old_rule = "M's " + "finalis" + "ation rule"
    chk("  the withdrawn phrases ('since M finalis.. it', 'finalis..ation rule') "
        "stand nowhere in ledger.py, specthm.py or LEDGER.md (source-read)",
        sorted(n for n, t in _srcs.items()
               if _old_edit[22:36] in t or _old_rule[4:] in t), [])
    chk("  CONTROL: the phrase as it stood ('the one paper edit since M finalis.. "
        "it, on M's ruling') planted in the ruling cell fails the equality, and "
        "planted in the template would be found by the source scan",
        (_d4[0][3].replace("a paper edit on M's ruling under M's rule for the paper",
                           _old_edit) == m_d65_4_ruling(),
         _old_edit[22:36] in M_D65_4_RULING_T.replace("a paper edit on M's ruling",
                                                      _old_edit)),
        (False, True))
    chk("  paper/CLAIMS.md:%d, READ now, is caveat (b) and carries the clause "
        "M-D65-4 applied; the premise is not stated as fact" % PAPER_CAVEAT_B_LINE,
        (paper_caveat_b_faults(),
         massform.P_UNIFORM_STATUS in ("PREMISE",),
         "massform.P_UNIFORM_STATUS = %s" % massform.P_UNIFORM_STATUS in _d4[0][2]),
        ([], True, True))
    chk("  CONTROL: the line as it stood ('It is uniform where nothing sources "
        "it.** The same inside') is caught",
        paper_caveat_b_faults("- **(b) It is uniform where nothing sources it.** "
                              "The same inside the throat as outside, and already "
                              "inside"),
        ["line %d is not caveat (b)" % PAPER_CAVEAT_B_LINE,
         "caveat (b) does not carry '%s'" % PAPER_CAVEAT_B_CLAUSE,
         "caveat (b) states the premise as fact (the wording as it stood)"])
    chk("  CONTROL: a verdict planted in M-D65-4's ruling cell, in its `why` "
        "cell or in its unblocks cell is caught by the equalities",
        (_d4[0][3] + "  The paper is otherwise confirmed." == m_d65_4_ruling(),
         _d4[0][2] + "  The paper is otherwise confirmed; every H92 claim STANDS."
         == m_d65_4_why(),
         _d4[0][4] + "; the paper is otherwise confirmed"
         == M_D65_4_UNBLOCKS_T % M_PAPER_RULE_WORDS), (False, False, False))
    # The superseded-wording header and M-S1A-P1's unblocks cell are BUILT
    # (superseded_dockets(), D65_SEATED_IDS), not typed: the source is read,
    # since a typed copy true today would go stale silently at DOCKET 68.
    _src = open(__file__, encoding="utf-8").read().split("\ndef selftest():")[0]
    chk("the superseded-wording header and M-S1A-P1's unblocks cell are built "
        "in the source ('%% superseded_dockets()', '%% D65_SEATED_IDS'), and no "
        "typed copy of either stands there",
        (bool(re.search(r'"## Row wording replaced by DOCKETS %s" % superseded_dockets\(\)',
                        _src)),
         bool(re.search(r'"DOCKET 65 has run: %s \(massform\.py\)" % D65_SEATED_IDS', _src)),
         bool(re.search(r'"## Row wording replaced by DOCKETS 62, 64 and 65"', _src)),
         bool(re.search(r'"DOCKET 65 has run: D27, D28', _src))),
        (True, True, False, False))
    chk("  CONTROL: the typed literals, planted, would be found",
        (bool(re.search(r'"## Row wording replaced by DOCKETS 62, 64 and 65"',
                        _src + '\n"## Row wording replaced by DOCKETS 62, 64 and 65"')),
         bool(re.search(r'"DOCKET 65 has run: D27, D28',
                        _src + '\n"DOCKET 65 has run: D27, D28, D29, S10"'))),
        (True, True))
    _q = list(_d67[0])
    _q[3] = _q[3].replace("I'm starting suspect", "I'm starting to suspect", 1)
    chk("  CONTROL: M's words in M-D65-3 corrected ('starting to suspect') in the "
        "ruling cell only is caught", len(verbatim_faults(tuple(_q), _raw,
                                                           rid="M-D65-3")) > 0, True)
    chk("massform.NOT_OPENED (asked): each item is internal to S10 or S13, or "
        "gates nothing -- names S10 or S13, says 'no verdict', or is the "
        "H-FLAV-only sub-count whose owner says it carries no verdict",
        ([i for i in massform.NOT_OPENED
          if not ("S10" in i or "S13" in i or "no verdict" in i
                  or ("H-FLAV only" in i and "no verdict"
                      in massform.electron_family_shortfall.__doc__.casefold()))],
         len(massform.NOT_OPENED) > 0), ([], True))
    chk("the docstring names section 4's clause (not 'the principle's second "
        "half') for the finite share, section 6's Not-opened sentence, and "
        "M-D65-3",
        ("so by the principle's clause\n       on questions internal to an "
         "already-REFUSED row that gate nothing it is\n       recorded" in __doc__,
         "principle's second\n       half it is recorded" in __doc__,
         "Not opened: massform.NOT_OPENED (asked), each internal to S10 or S13 "
         "or gating\nnothing" in __doc__,
         "M's ruling on\nDOCKET 67 is M-D65-3" in __doc__),
        (True, False, True, True))

    print("\n5. THE BALANCE REFUSES TO INVENT A LADDER")
    chk("every balance row whose mechanism fails carries NO gap number",
        all(g is None for _i, _w, _d, _s, g in balance()), True)
    chk("and there are four such rows", len(balance()), 4)

    print("\n6. THE GENERATED DOCUMENT ROUND-TRIPS, AND THE DRIFT CHECK BITES")
    # MUTATED ON A SCRATCH COPY, never on LEDGER.md itself.  A --check that has
    # never been shown to fail is decoration, and this tree has just finished
    # removing nine z3 probes that could not fire.
    import os
    import tempfile
    md = to_markdown()
    chk("the document is generated, not typed -- it re-renders identically",
        to_markdown() == md, True)
    d = tempfile.mkdtemp()
    good, bad = os.path.join(d, "G.md"), os.path.join(d, "B.md")
    with open(good, "w", encoding="utf-8") as fh:
        fh.write(md)
    with open(bad, "w", encoding="utf-8") as fh:
        fh.write(md.replace("1.348948e+26", "1.348949e+26"))
    chk("--check passes on a faithful copy", check(good), 0)
    chk("and FAILS on one digit of the exchange rate", check(bad), 1)
    chk("and fails on an absent file", check(os.path.join(d, "nope.md")), 1)
    # LEDGER.md IS FOUND FROM ANY CWD.  It was resolved against the cwd, and
    # --check from the repository root reported a tracked file missing.  Run
    # from a directory holding no LEDGER.md: the default path must find the
    # real one and pass, and the old cwd-relative path must not find it.
    here = os.getcwd()
    try:
        os.chdir(d)
        from_elsewhere = check()
        old_relative = check("LEDGER.md")
    finally:
        os.chdir(here)
    chk("--check from another cwd finds LEDGER.md beside ledger.py, passes",
        (from_elsewhere, LEDGER_MD == os.path.join(HERE, "LEDGER.md")),
        (0, True))
    chk("  CONTROL: the cwd-relative path, from there, does not find it",
        old_relative, 1)
    for f in (good, bad):
        os.unlink(f)
    os.rmdir(d)

    print("\n7. WHAT THIS FILE CLAIMS ABOUT ITSELF")
    chk("it derives nothing -- every row is asked or cited",
        DERIVES_NOTHING, True)
    chk("it does not total the gaps", TOTALS_THE_GAPS, False)
    chk("it does not rank the open questions", RANKS_THE_OPEN, False)
    chk("the conjunction of DOCKET 55's limbs is a SURVEY, never a theorem",
        [r[2] for r in DEMAND if r[0] == "D12"], [SURVEY])
    chk("nothing is repaired and no peer is edited",
        (NOTHING_IS_REPAIRED, NO_PEER_IS_EDITED), (True, True))

    print("\n  SELFTEST %s" % ("OK" if ok else "FAILED"))
    return 0 if ok else 1


DERIVES_NOTHING = True
TOTALS_THE_GAPS = False
RANKS_THE_OPEN = False
NOTHING_IS_REPAIRED = True
NO_PEER_IS_EDITED = True


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(selftest())
    if "--md" in sys.argv:
        sys.exit(write_md())
    if "--check" in sys.argv:
        sys.exit(check())
    sys.exit(report())
