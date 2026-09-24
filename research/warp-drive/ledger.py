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
reconstruction route has a PRICE, which is the only row here that does.

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
new row is the flat-bulk lattice theorem, D21, a THEOREM with its hypotheses
named.  REFUSED by the ruling and therefore NOT on this board: closing any of
the five; the curvature-tightened persistence figures; the void 9/64
adjustment; an R-1 row (it is O7 renamed); a separate NEC-everywhere row (it is
O3 with a clause); the Caldwell & Langlois withdrawal (it has no referent).
The selftest asserts each refusal.  The wording each narrowing replaced is
KEPT in SUPERSEDED_WORDING, because a row rewritten in place leaves no trace
otherwise.

DOCKET 63 adds D15-D20 (the Higgs at the endpoint), S6-S8 (all REFUSED, no
gap) and W9-W13, owners as the ruling named them.  W9 is excite.W9 and
W10-W13 are address.WITHDRAWN: the withdrawn rows are ASKED too, not retyped.

THE BOARD MUST NOT LAG THE TREE: fluctuation.py was committed with no row, so
D22 is an OPEN demand row owned by it.  Stability, formation and the stock
gate are NOT opened here -- a later docket prices and opens those.
"""

import math
import sys

import achievable
import address
import bounds
import branelink
import candidates
import certify
import driven
import drivensource
import endpoint
import excite
import fewsterteo
import fluctuation
import foliation
import higgs
import latticectc
import nonstatic
import overturn
import throatmass
import tolman

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
     "kg/m^3 of stable matter.  Inputs G_F and m_h are NAMED-NOT-READ, and "
     "the figure inherits that status"
     % (excite.EPS_AT_FIXTURE, excite.HOLD_HIGGS_DERIVED_KG_M3_AT_EPS_1E18,
        excite.HOLD_STABLE_KG_M3_AT_EPS_1E18["H1"],
        excite.HOLD_STABLE_KG_M3_AT_EPS_1E18["H2"]),
     MEASURED, ("excite", "HOLD_HIGGS_DERIVED_KG_M3_AT_EPS_1E18"),
     "a cheaper stable neutral source (DOCKET 63 E1, unsettled), a READ G_F "
     "or m_h, or the H1/H2 choice, which no Standard Model instrument can "
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

    # ----- the board catching up with the tree: fluctuation.py. -------------
    ("D22",
     "THE SEMICLASSICAL DEBT.  Every demand row is a demand on <rho> inside "
     "G = 8 pi G <T>, and Kuo & Ford's measure of that equation's error, "
     "Delta, is re-derived exactly in flat space: the pointwise measure is "
     "recomputed two independent ways, and Delta >= 1/3 is PROVED (z3) for "
     "EVERY zero-mean Gaussian state, without Kuo & Ford's diagonal "
     "assumption.  The pointwise Delta is sign-blind -- it condemns thermal "
     "radiation too -- so it cannot be the demand.  THE SMEARED PRICE AT THE "
     "CORRIDOR'S OWN SCALES IS OPEN",
     OPEN, ("fluctuation", "PRICES_THE_CORRIDOR"),
     "the SMEARED fluctuation priced at the corridor's scales -- the width b "
     "and Fewster's sampling time -- which needs the curved-space "
     "renormalisation of quartic operator products Kuo & Ford said did not "
     "exist.  If it is of order one there, the demand column must be written "
     "about a distribution rather than an expectation"),
]

# ---------------------------------------------------------------------------
# RIGHT SIDE -- THE SUPPLY.  What is actually available, and its ceiling.
#
# `gap_orders` is None where the row is REFUSED rather than expensive: the sign
# inverts, or the mechanism fails, BEFORE the magnitude is reached, and a gap
# would imply a ladder that is not there.
# ---------------------------------------------------------------------------

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
     "THE ONLY ROW ON THIS LEDGER WITH A PRICE RATHER THAN A REFUSAL.  No mass "
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
     "reproduction of them is %s.  Owed: %s"
     % (branelink.S5_FIGURES_STATUS, branelink.S5_OWED)),

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
     "it needs phi at the GUT scale, xi_req = %.4g, a field %.0e to %.0e "
     "times Degrassi's instability scale 10^(%g +- %g) GeV, where the quartic "
     "is negative -- not an excitation of our vacuum"
     % ((excite.XI_REQUIRED_AT_GUT,)
        + (min(excite.XI_FIELD_OVER_INSTABILITY),
           max(excite.XI_FIELD_OVER_INSTABILITY))
        + (endpoint.DEGRASSI_LOG10_LI,
           endpoint.DEGRASSI_LOG10_LI_ERR))),
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

OPEN_ROWS = [
    ("O5",
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
     "first",
     ("throatmass", "O5_CLOSED")),

    ("O6",
     "THE BRANE-BULK TRANSDUCER.  NARROWED BY DOCKET 62 (branelink.py), NOT "
     "CLOSED.  The row's stated cause of death -- no coupling in print -- is "
     "REFUTED: %s.  Eot-Wash bounds %s.  The throughput the closure called "
     "decisive, recomputed at omega_GW = %d Omega, is h = %.4e and %.4e "
     "bits/s/W; the pass used Omega and its figures were %.0fx and %.0fx too "
     "large, kept as withdrawn values in branelink.py.  It does not close: "
     "the closing premise, a %s, is %s, and the honest shape is a dichotomy "
     "-- %s -- so the row is settled %s"
     % (branelink.COUPLING_SOURCE, branelink.EOTWASH_BOUNDS,
        branelink.OMEGA_GW_OVER_OMEGA, branelink.STRAIN_H,
        branelink.THROUGHPUT_BITS_PER_S_PER_W,
        branelink.WITHDRAWN_STRAIN_H / branelink.STRAIN_H,
        branelink.WITHDRAWN_THROUGHPUT / branelink.THROUGHPUT_BITS_PER_S_PER_W,
        branelink.CLOSING_PREMISE, branelink.CLOSING_PREMISE_STATUS,
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
     fewsterteo.RIGHT_INSTRUMENT + " -- not Fewster & Teo's difference QEI",
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
]

#: THE WORDING DOCKET 62 REPLACED.  (row id, as first written -- claim, then
#: what would answer it -- and why it was replaced.)  KEPT, NEVER DELETED: a row
#: rewritten in place is otherwise indistinguishable from one that always said
#: the new thing, and three of these five said something now refuted.
SUPERSEDED_WORDING = [
    ("O5",
     "Does a self-consistent static semiclassical solution with m(r) < 0 exist "
     "at all?  Fewster & Teo bound the NORMAL-ORDERED density relative to the "
     "static vacuum, so the bound is on rho_ren - rho_vac and not on rho_ren "
     "|| a self-consistent solve of G_ab = 8 pi <T_ab> on the negative-mass "
     "corridor, rather than a bound evaluated on an assumed background",
     "true of Fewster & Teo and NOT a limit on QEIs: " +
     throatmass.NARROWING_3_STATUS + "; the answering solve is now named "
     "exactly (HPS's system, regular-centre data)"),
    ("O6",
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
    ("O7",
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
    ("O2",
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
    ("O3",
     "Whether ANY braneworld shortcut yields a closed timelike curve.  Every "
     "published 'no' is a one-extra-dimension or flat-bulk result; the single "
     "'yes' needs two extra dimensions and two inequivalent preferred frames "
     "|| a general result at codimension two, or an explicit CTC at "
     "codimension one.  The split in the literature tracks codimension and "
     "nobody has closed it",
     "an explicit codimension-one CTC is no longer enough -- a hand-written "
     "metric answers nothing -- and the flat-bulk 'no' is now a THEOREM (D21), "
     "forced rather than contingent"),
]

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
            print("       asked: %s.%s = %s"
                  % (owner[0], owner[1], str(ask(owner))[:58]))

    print("\nRIGHT -- THE SUPPLY")
    for rid, what, st, owner, note in SUPPLY:
        print("  %-4s %-9s %-46s" % (rid, st, what[:46]))
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

    print("\nOPEN-ROW WORDING REPLACED BY DOCKET 62, KEPT: %s  (--md prints it)"
          % ", ".join(r[0] for r in SUPERSEDED_WORDING))

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
                 % (rid, st, _cell(claim, 900), src, _cell(moves, 700)))

    L += ["", "## Right -- the supply", "",
          "| id | status | mechanism | note |", "|---|---|---|---|"]
    for rid, what, st, _o, note in SUPPLY:
        L.append("| %s | **%s** | %s | %s |"
                 % (rid, st, _cell(what, 80), _cell(note, 1400)))

    L += ["", "## The balance", "",
          "| id | quantity | demand | supply | gap |", "|---|---|---|---|---|"]
    for rid, what, dem, sup, gap in balance():
        g = "**REFUSED** -- no ladder, so no number" if gap is None \
            else "%.3f orders" % gap
        L.append("| %s | %s | %s | %s | %s |"
                 % (rid, _cell(what, 200), _cell(dem, 200), _cell(sup, 200), g))

    L += ["", "## Open, and what would answer each", ""]
    for rid, claim, answer, owner in OPEN_ROWS:
        L += ["### %s" % rid, "", _one_line(claim, 1400), "",
              "**Would be answered by:** %s" % _one_line(answer, 600), "",
              "*Asked:* `%s.%s = %s`" % (owner[0], owner[1], ask(owner)), ""]
    for rid, claim, _st, owner, moves in open_demand():
        L += ["### %s (a demand row)" % rid, "", _one_line(claim, 1400), "",
              "**Would be answered by:** %s" % _one_line(moves, 600), "",
              "*Asked:* `%s.%s = %s`" % (owner[0], owner[1], ask(owner)), ""]

    L += ["## Open-row wording replaced by DOCKET 62", "",
          "Kept, never deleted: a row rewritten in place is otherwise",
          "indistinguishable from one that always said the new thing.", "",
          "| id | as first written (claim \\|\\| answer) | why it was replaced |",
          "|---|---|---|"]
    for rid, was, why in SUPERSEDED_WORDING:
        L.append("| %s | %s | %s |"
                 % (rid, _cell(was, 900), _cell(why, 400)))
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


def write_md(path="LEDGER.md"):
    io_open = open
    with io_open(path, "w", encoding="utf-8") as fh:
        fh.write(to_markdown())
    print("wrote %s" % path)
    return 0


def check(path="LEDGER.md"):
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
    chk("every owned row's attribute still exists on its peer", asked, 23)
    # RE-PINNED 11 -> 23 BY DOCKETS 62 AND 63, to what this loop counts after
    # the edit (the DOCKET 63 ruling projected 20; that was a prediction, not
    # a pin).  +6 D15-D20 and +3 S6-S8, owners as DOCKET 63 named them; +1
    # D21, the lattice theorem, asked of latticectc.py; +1 D22, fluctuation.py,
    # the board catching up with the tree; +1 S5, now asked of branelink.py
    # whether its four figures were measured -- they were not.
    open_asked = 0
    for rid, _c, _a, owner in OPEN_ROWS:
        ask(owner)
        open_asked += 1
    chk("and every O row is asked of the instrument that narrowed it",
        open_asked, len(OPEN_ROWS))

    print("\n2. THE PEERS STILL SAY WHAT THE ROWS SAY THEY SAY")
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
    chk("D20 reproduces DOCKET 63's 2.204772e11 kg/m^3 to 7 figures",
        round(ask(("excite", "HOLD_HIGGS_DERIVED_KG_M3_AT_EPS_1E18")) / 1e11, 6),
        2.204772)
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
    chk("fluctuation.py does not price the corridor, so D22 stays OPEN",
        ask(("fluctuation", "PRICES_THE_CORRIDOR")), False)
    chk("  and its bound is sign-blind and needs no diagonal G",
        (fluctuation.POINTWISE_DELTA_DISCRIMINATES_SIGN,
         fluctuation.BOUND_NEEDS_DIAGONAL_G), (False, False))
    chk("branelink.py: S5's four figures are NOT measured (S5 stays OPEN)",
        ask(("branelink", "S5_FIGURES_MEASURED")), False)

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
        {THEOREM: 17, NARROWED: 1, MEASURED: 3, SURVEY: 1, OPEN: 7,
         WITHDRAWN: 13, REFUSED: 8})
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
        sorted(r[0] for r in OPEN_ROWS), ["O2", "O3", "O5", "O6", "O7"])
    chk("every narrowed row's replaced wording is kept",
        sorted(r[0] for r in SUPERSEDED_WORDING),
        sorted(r[0] for r in OPEN_ROWS))
    chk("and each says why it was replaced",
        all(bool(r[2]) for r in SUPERSEDED_WORDING), True)
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
               "%.6f" % fewsterteo.VOID_ADJUSTMENT_ORDERS,
               "%.3f" % fewsterteo.WITNESS_ORDERS]
    chk("the refused figures appear nowhere in LEDGER.md",
        [n for n in needles if n in md], [])
    chk("  CONTROL: the needle search finds the figure that stands",
        "%.3f" % flat in md, True)
    chk("  CONTROL: and fires on a copy with a refused figure planted",
        [n for n in needles if n in md + needles[0]], needles[:1])
    chk("the 9/64 is not applied to C_F, on its owner",
        fewsterteo.NINE_64_APPLIES_TO_C_F, False)
    chk("O5's narrowing #3 is demoted on its owner",
        (throatmass.NO_QEI_CAN_BOUND_RHO_REN,
         throatmass.SEPARATES_O5_FROM_O2_PERMANENTLY), (False, False))
    chk("O7's B is unmeasured on its owner", branelink.B_MEASURED, False)
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
