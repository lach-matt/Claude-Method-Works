#!/usr/bin/env python3
r"""
formation.py -- DOCKET 64, LINE 5.  D24 (FORMATION) AND D25 (THE DESTINATION
STOCK GATE).  Each is asked only what can be asked of it here.

    python3 formation.py             the reading
    python3 formation.py --selftest  every identity, every control, every figure

Needs sympy, mpmath and z3 (pypi; see PROOF-ASSISTANT.md), but only inside
functions: the import itself is stdlib-only.  Runs under python3 (3.11).
Imports certify, nonstatic, stockgate, create, phase1, foliation and ladder
from this directory by path and copies none of them.

===============================================================================
0.  THE TWO QUESTIONS, WHAT THIS FILE RETURNS, AND WITH WHAT STATUS
===============================================================================

D24 asks for "the nucleation construction run rather than named, or the 'find
one and enlarge it' route priced; and for any configuration that changes no
topology, the passage from flat space to it priced at all".

    THE THIRD PART IS COMPUTED.  The priced object is certify.py's SEATED
    METRIC: conformastatic, Phi(r) = m/sqrt(r^2+a^2) - m/max(r,R_s), with
    m = a = 1/50 and R_s = 200 read from certify.M_SEATED, A_CORE and R_SHELL
    and turned into exact rationals.  It lives on R^3, so reaching it from
    flat space changes no topology.
        F1, F2, the transverse bound (this family) and the D4 statement:
        THEOREM.  The table on the seated object: MEASURED.
        The Eulerian half of F1 (E = R Delta W, independent of duration) is
        nonstatic.py section 4's result, credited there; see section 2.
    The first two parts stay OPEN (section 5).  Nucleation: READ, OPEN,
    because it has NOT BEEN COMPUTED, not because the source forbids it.
    Find-and-enlarge: OPEN.

D25 asks for "the destination's arrival aperture surveyed for a condensed,
primitive body holding M(p,s) x m_payload of accessible mass".

    OPEN AND UNCHANGED.  No conjunct is newly evaluated here.  The mass
    threshold is stockgate.py's own figure; it is cited, not re-priced.  The
    aperture: NOT EVALUABLE: NOT-FOUND (search named, APERTURE_SEARCH).  The
    formation-epoch snow line: NOT-FOUND, and a radius from today's luminosity
    is REFUSED.  Both of those the row and stockgate section 9 already carry.
    WHAT IS NEW is one READ survey result (section 6): MacGregor 2018 withdraws
    Anglada 2017's 1-4 au belt, and the only condensed body named in the two
    papers read is Proxima b, whose primitive and accessible status neither
    paper measures.

WITHDRAWN, KEPT AND MARKED (DOCKET 64 verification of this line):
  [W1] "D25: NARROWED ... the mass conjunct is priced with stockgate.py's own
       functions" (the old D25_VERDICT, kept as D25_VERDICT_WITHDRAWN).  The
       749.08 kg (P) and 1000 kg craft figures are stockgate.py's own printed
       reading, and the row already carries the 10.7 factor.  Re-printing them
       here over-represented D25.  This file no longer prices the conjunct.
  [W2] "The READ survey finds no confirmed condensed reservoir"
       (SURVEY_CONFIRMED_RESERVOIR = False, kept as
       SURVEY_CONFIRMED_RESERVOIR_WITHDRAWN).  This is inaccurate.  Proxima b
       (m sin i = 1.3 M_earth at 0.05 au) is named in the papers read and is a
       condensed body far above the threshold (computed in the selftest).  The
       open conjuncts are "primitive" and "accessible", not "condensed".
  [W3] "It never writes the neck metric, so the construction CANNOT be priced
       from the paper" (NUCLEATION_PRICEABLE_FROM_SOURCE = False, kept as
       ..._WITHDRAWN).  That is not a proved obstruction.  Sec. V specifies the
       neck by explicit homotopies H1-H4 with free smooth b, c and alpha, and
       the metric follows from the construction (2)/(24).  The price has NOT
       BEEN COMPUTED.  OPEN.
  [W4] "Its only energy-condition evidence is one type-IV point."  Sec. IV
       also classifies the Morse spacetime by the Hawking-Ellis criterion
       eq. (19) (type-IV regions, Fig. 9) and plots a WEC-violating region for
       CP^2 (Fig. 12).
  [W5] The "scope finding" that nonstatic.py's geodesic-slicing hypothesis
       "was idle".  nonstatic section 4 already stipulates "(R held fixed)",
       so its lapse term was already zero.  That is trivial, not a finding.
  [W6] "PROVED NOT EVALUABLE FROM THE TREE."  A grep is not a proof: the
       aperture could be named otherwise.  It is now "NOT EVALUABLE: aperture
       NOT-FOUND (search named)", and the search includes synonyms.
  [W7] "The field equation alone puts no lower bound on the duration."  That
       is vacuous, because T is defined as G/8pi.  Restated in section 3.

===============================================================================
1.  THE PASSAGE, AS AN EXPLICIT FAMILY OF SPACETIMES
===============================================================================

Write the seated object with areal radius R = h(r) = r e^{-phi(r)}.  Then
W_1 = e^{-Lambda} R' = 1 - r phi'(r).  The family, for any smooth f(t) with
f = 0 before the passage and f = 1 after it, is

    ds^2 = -e^{2 f phi} dt^2 + e^{2 Lambda} dr^2 + h(r)^2 dOmega^2,
    Lambda = (1 - f) ln h'(r) - f phi(r)

    f = 0   -dt^2 + dh^2 + h^2 dOmega^2           FLAT, in the areal radius h
    f = 1   -e^{2phi}dt^2 + e^{-2phi}(dr^2 + r^2 dOmega^2)   THE SEATED METRIC

Both ends are checked SYMBOLICALLY.  At f = 0 every component of G_ab is 0.  At
f = 1 the metric components equal certify's conformastatic components, and the
stress tensor equals the static one.  A BROKEN family (Lambda = -f phi, with
the (1-f) ln h' term dropped) is run through the same check and FAILS it.  That
is the control that the flat-end check can fail.  phi itself is tied to
certify.phi numerically on both sides of the shell.

THE AREAL RADIUS OF EVERY SPHERE IS HELD FIXED THROUGH THE WHOLE PASSAGE
(U = e^{-Phi} dR/dt = 0 exactly).  This is deliberate.  nonstatic.py's anchor
lemma says a place is a fixed areal radius, so this is the passage that builds
the object WITHOUT MOVING THE PLACES IT CONNECTS.

The stress tensor is the Einstein tensor of that metric, computed by
nonstatic.general_einstein().  That is the tree's own sympy derivation,
imported, not copied, with the family substituted.  Exactly (residual 0):

    W   = W_1^f
    m   = (R/2)(1 - W_1^{2f})                       Misner-Sharp
    j   = fdot omega W_1^f e^{-f phi} / (4 pi R),   omega = ln W_1
    rho, p_r  contain NO time derivative of f
    p_T = (static part) + (omega/8pi) e^{-2 f phi} (fddot - (phi+omega) fdot^2)
        = (static part) + (omega/8pi) (f_tautau - omega f_tau^2)

Here tau is the EULERIAN proper time, d tau = e^{f phi} dt, measured by the
observer at fixed areal radius (u = e^{-Phi} d/dt).  Every flux below is in that
frame.

===============================================================================
2.  THE PRICE AT EACH SPHERE -- PATH-INDEPENDENT, DURATION-INDEPENDENT
===============================================================================

THEOREM F1.  Hypotheses (F1_THEOREM, each discharged by a named selftest row):
spherical symmetry; G_ab = 8 pi T_ab; U = 0 at the sphere throughout; W > 0
(untrapped); the passage runs from f = 0 to f = 1.  Rest at the ends is NOT
needed for F1: a linear profile, not at rest at either end, gives the same
integral.  Rest is a hypothesis of the transverse bound only.  From
nonstatic.py's EV-W and MS-t at U = 0,

    D_t W = 4 pi R j            D_t m = -4 pi R^2 j W

and integrating in the Eulerian proper time across the whole passage gives

    E(R)  = INT 4 pi R^2 j d tau        = R (W_1 - 1)          Eulerian energy
    K(R)  = INT 4 pi R^2 j W d tau      = R (W_1^2 - 1)/2 = -m_1(R)   Kodama

    BY ANY ROUTE, AT ANY SPEED, IN ANY LAPSE.  Only the endpoint enters.

PRIOR, CREDITED.  E = R Delta W with R held fixed, "INDEPENDENT OF HOW LONG YOU
TAKE", is nonstatic.py section 4.  The K half is MS-t integrated.  What is NEW
here:
  - an explicit U = 0 family realising flat -> seated, with both ends checked;
  - K = -m_1 evaluated on the seated object, sphere by sphere;
  - F2;
  - the transverse bound for this family;
  - the D4 observation (section 3).

On the seated object (geometric units, lengths in certify's unit L):

    W_1 > 1 for 0 < r < R_s  and  0 < W_1 < 1 for r > R_s     (z3, both)

So across every interior sphere the passage must carry energy OUTWARD, with
K(R) -> m = 1/50 once r >> a.  Across every exterior sphere it carries a little
INWARD.  The Kodama mass it leaves is exactly the jump of m_1 at the shell.  The
ADM mass stays 0 (limit, sympy), agreeing with concentric.py's M_ADM = 0.

    THE FORMATION PRICE OF THE SEATED OBJECT, ACROSS A SPHERE, IS ITS OWN
    ENCLOSED NEGATIVE MASS, TO BE EXPORTED.  NOTHING IS ADDED BY THE PASSAGE
    AND NOTHING IS SAVED BY PASSING SLOWLY.

NOTE (was a "scope finding", [W5]): the family has a nonzero lapse gradient.
Because U = 0, EV-W's lapse term U D_r Phi vanishes regardless.  That is the
whole of it.

===============================================================================
3.  THE ENERGY-CONDITION COST OF THE PASSAGE
===============================================================================

RADIAL.  For the outgoing null k = u + n (normalised -u.k = 1, with u Eulerian),
T_kk = rho + p_r - 2 j.  This is checked as a residual on the family, and the
ingoing null gives + 2 j.  At U = 0, rho = D_r m /(4 pi R^2 W) and
p_r = (W D_r Phi - m/R^2)/(4 pi R) are INSTANTANEOUS in the slice data, so

    INT (T_kk - [rho + p_r]) d tau  =  -2 INT j d tau  =  -(W_1 - 1)/(2 pi R)

    THEOREM F2, hypotheses F2_THEOREM (those of F1, plus the null
    normalisation).  Every such passage pays exactly this extra
    outgoing-radial null deficit over its adiabatic sequence, whatever f(t)
    is.  Ingoing null pays the opposite sign.  Duration does not enter.

TRANSVERSE (THIS FAMILY ONLY, because p_T depends on the lapse and the Lambda
chosen).  Hypotheses TRANSVERSE_BOUND: those of F1, plus f in C^1 and at rest
at both ends (f_tau = 0).  The time part of p_T is
(omega/8pi)(f_tautau - omega f_tau^2), so integrating by parts gives

    INT (time part of rho + p_T) d tau = -(omega^2/8pi) INT f_tau^2 d tau
                                      <= -(omega^2/8pi) / tau_p

The inequality is Cauchy-Schwarz: INT f_tau^2 >= (INT f_tau)^2 / tau_p =
1/tau_p, where tau_p is the passage's Eulerian proper duration at that sphere.
The cost is STRICTLY NEGATIVE and grows as 1/tau_p.

TIME (restated, [W7]).  The family exists for every tau_p > 0.  With NO energy
condition imposed, nothing bounds tau_p.  That is vacuous, because T is defined
as G/8pi.  With the transverse NEC imposed, the family is excluded at EVERY
tau_p, since the cost above is strictly negative.  phase1.py's Theorem 4 (L/2c)
assumes agents acting in a compact region.  This family's stress tensor is
nonzero across the whole support from the first instant, so the family does
not meet that hypothesis.  The seated object is not compactly supported:
phi_out ~ -m a^2 / (2 r^3) for every r > R_s (limit, sympy), so it also fails
phase1's D2 (SEATED_COMPACT_SUPPORT = False).  Delivering the source causally
is Theorem 4's floor, not re-derived here.

PHASE1's D4 (T^{0i} = 0), in the Eulerian frame.  F1 gives
INT j d tau = (W_1 - 1)/(4 pi R), which is != 0 wherever W_1 != 1.  So every
U = 0 passage has T^{0r} != 0 at some instant
(PHASE1_D4_POINTWISE_DURING_PASSAGE = False).  The flux is radial, so the net
momentum is zero by symmetry: no thrust.  D4 was stated for the configurations
g_s.  It cannot hold pointwise for the passage between them.  THEOREM,
hypotheses of F1.

===============================================================================
4.  WHAT D24 NOW CARRIES
===============================================================================

    ANSWERED for the part asked.  The passage from flat space to the seated
    object without topology change IS priced, per sphere, exactly, by F1 and
    F2.  THE ROW STAYS OPEN on its other two parts.

===============================================================================
5.  THE PARTS OF D24 THAT REMAIN OPEN
===============================================================================

NUCLEATION, READ; OPEN BECAUSE NOT COMPUTED.  Pisana, Shoshany, Antoniou,
Kauffman & Lambropoulou, arXiv:2505.02210 v4, read at source (alphaXiv):
  - A 0-surgery gives a SINGULAR Lorentzian cobordism.  The singularity is
    removed by a connected sum with CP^2 (the Misner trick), which "replaces
    the naked singularity with a region containing closed timelike curves"
    (abstract).
  - Energy-condition evidence, qualitative only:
      - the Morse spacetime (13) classified by the Hawking-Ellis criterion,
        eq. (19), with type-IV regions (Fig. 9);
      - a region where T_ab w^a w^b < 0 for the timelike w^mu on CP^2
        (Fig. 12, WEC violated);
      - a type-IV point p = (1,0,0,0) on CP^2.
    The paper gives NO integrated energy-condition figure.
  - The neck is specified as a recipe: homotopies H1-H4 with free smooth
    b(eta), c(eta), alpha(eta).  The Lorentzian metric follows from the
    construction (2)/(24), whose zeta > 1 is also free.  "No further explicit
    expression is required for our purposes" (sec. V).
  So the price has NOT BEEN COMPUTED.  Whether it depends on the free
  functions is NOT DETERMINED.  No obstruction is claimed ([W3]).  The reading
  agrees with create.py's Borde reading: the singularity is traded for CTCs,
  not escaped.

FIND ONE AND ENLARGE IT.  F1 applies unchanged to an enlargement between two
throat configurations, at every sphere that exists in BOTH and stays untrapped.
The price at R is m_final(R) - m_initial(R).  It is NOT run, because the
route's premise is an observed throat and none is observed (create.ROUTE_COST).
OPEN.

===============================================================================
6.  D25 -- OPEN AND UNCHANGED; ONE NEW READ SURVEY RESULT
===============================================================================

stockgate.GATE:  B admissible <=> within the corridor's arrival aperture there
is a CONDENSED body, PRIMITIVE rather than devolatilised, holding at least
M(p,s) x m_payload of accessible mass.

(3) THE MASS.  stockgate.py owns it (python3 stockgate.py prints it).  This
    file only calls stockgate.feedstock_kg inside the gate predicate and inside
    one comparison against Proxima b ([W1]).

(1) THE APERTURE: NOT EVALUABLE: aperture NOT-FOUND (search named).  The
    search is APERTURE_SEARCH.  The selftest recomputes its file set, so a new
    hit turns it red until the hit is classified.  NO instrument assigns the
    corridor's arrival aperture a value.  A predicate with an unbound variable
    cannot be evaluated.  The row already says this.

(2) PRIMITIVE: NOT-FOUND.  stockgate classifies by Lodders' 50% condensation
    temperatures AT 1e-4 bar (stockgate.SOURCES "L03"), which are nebular.
    Turning "primitive" into an orbital radius needs the formation-epoch disc
    T(a), P(a) at the destination.  The search is SNOWLINE_SEARCH.
    Present-day luminosity would not do it either.  MacGregor et al. 2018,
    sec. 1, read at source: late M dwarfs "have long pre-main sequence phases
    during which the stellar luminosity can change significantly".  REFUSED to
    compute a radius: it would use a nebular T_c outside its pressure
    hypothesis and today's luminosity outside its epoch.

THE SURVEY, READ at the tree's destination (foliation.PROXIMA_LY).  This is
the new content:
  - Anglada et al. 2017 (arXiv:1711.00578) reported a 1-4 au belt, ~0.01 Earth
    masses TOTAL by extrapolating a -3.5 size law to 50 km bodies (sec. 3.2).
    Warm dust at ~0.4 au and a ~30 au belt are both marginal (abstract, 3.3).
  - MacGregor et al. 2018 (arXiv:1802.08257) attribute the ACA excess to "the
    short duration stellar flare": "no need to posit the cold belt at 1-4 AU"
    (sec. 4.2).  THE 1-4 au BELT, which would have held small primitive
    bodies, IS WITHDRAWN.  The 0.4 au warm dust is unnecessary if the 12-m
    excess is coronal.  The 30 au belt stays marginal, with 13+10-8 background
    sources > 150 uJy expected in the primary beam (sec. 4.2).
  - The ONLY CONDENSED BODY named in the sources read is PROXIMA b: m_p sin i =
    1.3 M_earth at 0.05 au, from Doppler data (Anglada 2017 sec. 1, citing
    Anglada-Escude et al. 2016; also MacGregor sec. 1).  Its minimum mass
    is far above stockgate's 70 kg threshold (the ratio is computed by
    proxima_b_over_threshold and printed by the reading).  Its volatile state is UNMEASURED, so the primitive conjunct is
    undetermined.  Its accessibility is also unmeasured.
  - 1.3 mm continuum "traces dust grains with um to cm sizes" (Anglada 3.2).
    Neither paper's own data constrain individual bodies.

    SURVEY (READ): condensed, yes (Proxima b).  Primitive and accessible:
    UNDETERMINED.  Whether a gate reservoir exists is UNDETERMINED
    (SURVEY_CONFIRMED_RESERVOIR), and that is not a negative.  This is what was
    looked at.  It is not proof of anything that was not looked at.

===============================================================================
7.  WHAT THIS FILE REFUSES
===============================================================================

    AN SI FIGURE FOR THE FORMATION PRICE.  certify's seated metric is in a
    length unit L that the tree never fixes.  The reading gives kg per metre of
    L (c^2/G from foliation.py) and no more.
    THE SHELL AT R_s.  phi is C^0 there and W_1 jumps: it is a surface layer
    whose own stress is not computed.  Every figure here is on one side of it.
    A SNOW-LINE RADIUS, AN APERTURE, ANY SEPARATION ENERGY, AND ANY RE-PRICING
    OF stockgate's MASS CONJUNCT.
    ANY ROW STATUS.  This file proposes; ledger.py rules.
    NOTHING IS REPAIRED AND NO PEER IS EDITED.

===============================================================================
8.  DOCKET 64 CORRECTIONS APPLIED (ruling section B5, and this line's verifier)
===============================================================================

  - The build_energy comparison is relabelled CONSISTENCY.  It is not a
    control: it compares R dW c^2/G with itself.  The CONTROL is now the raw
    passage integral, 4 pi R^2 INT j dtau against on_seated's E.  The same is
    done for K, and for F2's -2 INT j dtau.
  - The aperture is "NOT EVALUABLE: NOT-FOUND (search named)", with synonyms,
    and the selftest recomputes the search.
  - The path is HERE = dirname(abspath(__file__)).
  - F1_THEOREM, F2_THEOREM, TRANSVERSE_BOUND and
    PHASE1_D4_POINTWISE_DURING_PASSAGE are exposed.  Every named hypothesis
    must be discharged by a passing row (the last selftest control).
  - The z3 polynomials are generated by the same callables that the sympy
    encoding-drift guard checks against phi_in and phi_out.  A deliberately
    drifted polynomial must fail that guard.
  - The selftest counts its own rows by kind (residual, numeric, control,
    consistency, record pin).  No count is typed anywhere.
  - Where the ruling and the verifier disagreed, the weaker statement was
    applied: D25 UNCHANGED (not "narrowed"); the survey is condensed-yes and
    reservoir-UNDETERMINED (not "no confirmed condensed reservoir");
    nucleation is OPEN, not computed (not "cannot be priced"); and "at rest"
    is removed from F1's hypotheses, where the linear-profile row shows it is
    unused.
"""

import math
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path:
    sys.path.insert(0, HERE)

import certify      # noqa: E402  the seated metric and its FD pipeline
import create       # noqa: E402  ROUTE_COST, NUCLEATION_STATUS
import foliation    # noqa: E402  C_LIGHT, G_NEWTON, PROXIMA_LY
import ladder       # noqa: E402  M_EARTH
import nonstatic    # noqa: E402  general_einstein(), build_energy()
import phase1       # noqa: E402  CONDITIONS (D2, D4)
import stockgate    # noqa: E402  GATE, feedstock_kg, SOURCES

# --------------------------------------------------------------- status words
THEOREM, MEASURED, SURVEY, OPEN, READ, NOT_FOUND, REFUSED = (
    "THEOREM", "MEASURED", "SURVEY", "OPEN", "READ", "NOT-FOUND", "REFUSED")
UNDETERMINED = "UNDETERMINED"
NOT_DETERMINED = "NOT DETERMINED"

# ------------------------------------------------ the theorems' hypotheses
H_SPH = "spherical symmetry (-e^{2Phi}dt^2 + e^{2Lambda}dr^2 + R^2 dOmega^2)"
H_EFE = "G_ab = 8 pi T_ab (T defined from the metric; convention tied to certify)"
H_U0 = "U = 0: the sphere's areal radius held fixed throughout the passage"
H_W = "W > 0 at the sphere throughout (untrapped)"
H_ENDS = "the passage runs from f = 0 (flat) to f = 1 (seated)"
H_NULL = "outgoing radial null k = u + n, u Eulerian, normalised -u.k = 1"
H_FAMILY = "this family only: p_T depends on the lapse and Lambda chosen"
H_REST = "f is C^1 and at rest at both ends (f_tau = 0)"

F1_THEOREM = (H_SPH, H_EFE, H_U0, H_W, H_ENDS)
F2_THEOREM = F1_THEOREM + (H_NULL,)
TRANSVERSE_BOUND = F1_THEOREM + (H_FAMILY, H_REST)
ALL_HYPOTHESES = tuple(dict.fromkeys(F1_THEOREM + F2_THEOREM + TRANSVERSE_BOUND))

PHASE1_D4_POINTWISE_DURING_PASSAGE = False   # computed-checked in the selftest
SEATED_COMPACT_SUPPORT = False               # phase1 D2; limit checked in selftest

STATUS = {
    "D24 part 3: F1, F2, transverse bound (this family), D4": THEOREM,
    "D24 part 3: the table on the seated object": MEASURED,
    "D24 part 3: E = R Delta W (Eulerian half of F1)":
        "THEOREM, PRIOR (nonstatic.py section 4)",
    "D24 nucleation": "READ, OPEN (not computed)",
    "D24 find-and-enlarge": OPEN,
    "D25": "OPEN, UNCHANGED",
    "D25 survey": "SURVEY (READ)",
    "D25 aperture": "NOT EVALUABLE: aperture NOT-FOUND (search named)",
    "D25 formation snow line": "NOT-FOUND; a present-luminosity radius REFUSED",
}

D24_VERDICT = ("ANSWERED FOR THE THIRD PART: the passage from flat space to the "
               "seated object, no topology change, priced per sphere exactly "
               "(F1, F2: THEOREM; the seated table MEASURED; E = R Delta W is "
               "nonstatic.py section 4's, credited).  The row stays OPEN on "
               "nucleation (READ, not computed) and on find-and-enlarge")
D25_VERDICT = ("OPEN AND UNCHANGED: no conjunct is newly evaluated.  The mass "
               "threshold is stockgate.py's (cited, not re-priced); the aperture "
               "is NOT EVALUABLE: NOT-FOUND (search named); the formation-epoch "
               "snow line is NOT-FOUND and a present-luminosity radius REFUSED.  "
               "NEW, READ: MacGregor 2018 withdraws the 1-4 au belt; the only "
               "condensed body in the sources read is Proxima b, whose primitive "
               "and accessible status is unmeasured")
D25_VERDICT_WITHDRAWN = (
    "WITHDRAWN [W1]: 'NARROWED: the mass conjunct is priced; the aperture and the "
    "formation snow line are NOT-FOUND in the tree, so the gate is not evaluable "
    "here; the READ survey finds no confirmed reservoir' -- the mass figures are "
    "stockgate.py's own; the survey clause is [W2]")

# -------------------------------------------------------------- nucleation
NUCLEATION_SOURCE = ("Pisana, Shoshany, Antoniou, Kauffman & Lambropoulou, "
                     "arXiv:2505.02210 v4, read via alphaXiv")
NUCLEATION_NECK_EXPLICIT = False     # no closed-form neck metric is written
NUCLEATION_NECK_RECIPE = True        # sec. V: homotopies H1-H4
NUCLEATION_FREE_FUNCTIONS = ("b(eta)", "c(eta)", "alpha(eta)",
                             "zeta > 1 of the construction eq. (24)")
NUCLEATION_HAS_CTC = True            # abstract
NUCLEATION_EC_EVIDENCE = (
    "eq. (19) Hawking-Ellis criterion on the Morse spacetime (13): type-IV "
    "regions (Fig. 9)",
    "WEC violated, T_ab w^a w^b < 0, on a region of CP^2 (Fig. 12)",
    "a type-IV point p = (1,0,0,0) on CP^2 (sec. IV)")
NUCLEATION_EC_FIGURE = False         # no INTEGRATED energy-condition figure
NUCLEATION_PRICED = False            # not computed: the reason D24 stays OPEN
NUCLEATION_PRICEABLE_FROM_SOURCE = NOT_DETERMINED
NUCLEATION_PRICEABLE_FROM_SOURCE_WITHDRAWN = (
    False, "WITHDRAWN [W3]: not a proved obstruction; the neck is given by "
           "explicit homotopies with free smooth functions")
NUCLEATION_STATUS = "READ, OPEN (not computed)"

# ------------------------------------------------------------------ survey
SURVEY_SOURCES = (
    ("Anglada et al. 2017", "arXiv:1711.00578",
     "1-4 au belt, ~0.01 M_earth total by -3.5 extrapolation to 50 km (sec 3.2); "
     "0.4 au and 30 au components marginal (abstract, sec 3.3); Proxima b "
     "m_p sin i = 1.3 M_earth at 0.05 au (sec 1, Anglada-Escude et al. 2016)"),
    ("MacGregor et al. 2018", "arXiv:1802.08257",
     "ACA excess is a ~1 min flare: 'no need to posit the cold belt at 1-4 AU' "
     "(sec 4.2); 12-m excess plausibly coronal; 30 au belt: 13+10-8 background "
     "sources > 150 uJy expected in the ACA primary beam (sec 4.2); PMS "
     "luminosity change (sec 1)"),
)
PROXIMA_B_MSINI_EARTH = 1.3          # READ, Anglada 2017 sec 1
PROXIMA_B_A_AU = 0.05                # READ, Anglada 2017 sec 1
SURVEY_CONDENSED_BODY = "Proxima b (m_p sin i = 1.3 M_earth, a = 0.05 au)"
SURVEY_CONDENSED_BODY_FOUND = True
SURVEY_PRIMITIVE_MEASURED = False
SURVEY_ACCESSIBLE_MEASURED = False
SURVEY_BELT_1_4AU_WITHDRAWN_BY_SOURCE = True    # MacGregor 2018 sec 4.2
SURVEY_CONFIRMED_RESERVOIR = UNDETERMINED
SURVEY_CONFIRMED_RESERVOIR_WITHDRAWN = (
    False, "WITHDRAWN [W2]: 'no confirmed condensed reservoir' -- Proxima b is "
           "condensed and far above threshold; primitive/accessible unmeasured")
SURVEY_CONSTRAINS_BODIES = False     # the papers' 1.3 mm data trace um-cm grains

# --------------------------------------------------------- the named searches
APERTURE_PATTERN = r"aperture"
APERTURE_HITS = {                     # READ, classified by hand, per file
    "stockgate.py": "the GATE text itself: names the arrival aperture, no value",
    "ledger.py": "D25's own row text",
    "beamed.py": "an optical transmitter aperture (a different object)",
    "branelink.py": "the Friis antenna aperture (a different object)",
    "device.py": "the device's transverse aperture, 5 lambda (a different object)",
    "index3.py": "the APERTURE index row for beamed.py (a different object)",
}
APERTURE_SYNONYM_PATTERN = (r"arrival (radius|band|window|zone|orbit|site)|"
                            r"capture (band|radius)|orbital radius")
APERTURE_SYNONYM_HITS = {
    "stockgate.py": "prose: the snow line, i.e. orbital radius, is the selector",
    "ledger.py": "D25's own row text",
    "warpdrive.py": "a muonic-atom orbital radius (a different object)",
}
SNOWLINE_PATTERN = r"snow.line|hayashi|nebula|disc temperature|disk temperature"
SNOWLINE_HITS = {
    "stockgate.py": "snow-line PROSE and RHO_DISC (a density); no T(a), P(a)",
    "ledger.py": "D25's own row text",
}


def _search_text(pattern, hits):
    return ("grep -il -E '%s' research/warp-drive/*.py (formation.py excluded): %s"
            % (pattern, "; ".join("%s -- %s" % kv for kv in sorted(hits.items()))))


APERTURE_SEARCH = (_search_text(APERTURE_PATTERN, APERTURE_HITS) + " || synonyms: "
                   + _search_text(APERTURE_SYNONYM_PATTERN, APERTURE_SYNONYM_HITS)
                   + " || no hit assigns the corridor's arrival aperture a value")
APERTURE_STATUS = "NOT EVALUABLE: aperture NOT-FOUND (search named)"
SNOWLINE_SEARCH = _search_text(SNOWLINE_PATTERN, SNOWLINE_HITS)
LODDERS_PRESSURE_BAR = 1.0e-4        # READ, as stockgate.SOURCES['L03'] states it


def tree_search(pattern, tree=None, exclude=("formation.py",)):
    """The file set a case-insensitive regex hits among tree/*.py -- the
    search the APERTURE/SNOWLINE records name, recomputed."""
    tree = tree or HERE
    rx = re.compile(pattern, re.I)
    out = set()
    for fn in sorted(os.listdir(tree)):
        if not fn.endswith(".py") or fn in exclude:
            continue
        try:
            with open(os.path.join(tree, fn), encoding="utf-8", errors="replace") as fh:
                if rx.search(fh.read()):
                    out.add(fn)
        except OSError:                      # pragma: no cover
            continue
    return out


def _need():
    try:
        import sympy as sp
        import mpmath as mp
        import z3
    except ImportError as exc:              # pragma: no cover
        raise SystemExit("formation.py needs sympy, mpmath, z3-solver: %s" % exc)
    return sp, mp, z3


# ============================================================ the seated object
def phi_forms(sqrt, m, a, Rs, r):
    """certify.phi's two branches, as ONE form shared by seated() and by the
    z3 encoding-drift guard: (inside the shell, outside it)."""
    s = sqrt(r**2 + a**2)
    return m / s - m / Rs, m / s - m / r


def seated(sp):
    """certify's constants as exact rationals, and phi on each side of R_s."""
    m = sp.nsimplify(repr(certify.M_SEATED))
    a = sp.nsimplify(repr(certify.A_CORE))
    Rs = sp.nsimplify(repr(certify.R_SHELL))
    r = sp.Symbol("r", positive=True)
    pin, pout = phi_forms(sp.sqrt, m, a, Rs, r)
    return dict(m=m, a=a, Rs=Rs, r=r, phi_in=pin, phi_out=pout)


def phi_vs_certify(S, sp, radii=((0.005, "in"), (1, "in"), (150, "in"),
                                 (250, "out"), (1000, "out"))):
    """Difference of this file's exact phi from certify.phi (float), per
    radius, relative to the size m/r0 of the two terms that cancel in phi_out
    (certify's float subtraction loses digits there; a drift in the FORM would
    not be at that scale)."""
    out = []
    for r0, side in radii:
        e = S["phi_in"] if side == "in" else S["phi_out"]
        mine = float(e.subs(S["r"], sp.nsimplify(r0)))
        theirs = certify.phi(float(r0))
        out.append((r0, side, abs(mine - theirs) / (certify.M_SEATED / float(r0))))
    return out


# ================================================================ the family
def family(broken=False):
    """The interpolating family, through nonstatic.general_einstein().

    broken=True drops the (1-f) ln h' term of Lambda: the NEGATIVE CONTROL,
    whose f = 0 end is not flat."""
    E = nonstatic.general_einstein()
    sp, t, r = E["sp"], E["t"], E["r"]
    f = sp.Function("f")(t)
    ph = sp.Function("varphi")(r)
    W1 = 1 - r * sp.diff(ph, r)
    h = r * sp.exp(-ph)
    # ln h' = ln(e^{-phi} W1) = ln W1 - phi, exact for W1 > 0 (z3 below)
    lnhp = sp.log(W1) - ph
    Lam = -f * ph if broken else (1 - f) * lnhp - f * ph
    subs = {E["Phi"]: f * ph, E["Lam"]: Lam, E["R"]: h}
    S = lambda e: e.subs(subs).doit()
    out = dict(E=E, sp=sp, t=t, r=r, f=f, ph=ph, W1=W1, R=h, om=sp.log(W1),
               Lam=Lam, fd=sp.diff(f, t), fdd=sp.diff(f, t, 2),
               g=E["g"].subs(subs).doit(), Ein=E["Ein"].subs(subs).doit())
    for k in ("rho", "j", "p_r", "p_T", "W", "U", "m"):
        out[k] = S(E[k])
    out["DrPhi"] = sp.exp(-Lam) * sp.diff(f * ph, r)
    out["Dt"] = lambda e: sp.exp(-f * ph) * sp.diff(e, t)
    return out


def _z(sp, e):
    return sp.simplify(sp.expand_log(sp.expand(e), force=True))


def _static(F, e):
    return e.subs(F["fdd"], 0).subs(F["fd"], 0)


def _at(F, e, v):
    return _static(F, e).subs(F["f"], v)


def closed_forms(F):
    """Every closed form of section 1 as a residual that must be 0."""
    sp, f, ph, om, R = F["sp"], F["f"], F["ph"], F["om"], F["R"]
    fd, fdd = F["fd"], F["fdd"]
    pT_time = F["p_T"] - _static(F, F["p_T"])
    return [
        ("U = 0 (areal radius held)", F["U"], (H_U0,)),
        ("W = W_1^f", F["W"] - sp.exp(f * om), (H_W,)),
        ("m = (R/2)(1 - W_1^{2f})", F["m"] - R * (1 - sp.exp(2 * f * om)) / 2, ()),
        ("j = fdot omega W_1^f e^{-f phi}/(4 pi R)",
         F["j"] - fd * om * sp.exp(f * om) * sp.exp(-f * ph) / (4 * sp.pi * R), ()),
        ("p_T time part = (omega/8pi) e^{-2f phi}(fdd - (phi+omega) fd^2)",
         pT_time - om * sp.exp(-2 * f * ph) * (fdd - (ph + om) * fd**2) / (8 * sp.pi),
         (H_FAMILY,)),
        ("EV-W at U=0:  D_t W = 4 pi R j", F["Dt"](F["W"]) - 4 * sp.pi * R * F["j"],
         (H_U0,)),
        ("MS-t at U=0:  D_t m = -4 pi R^2 j W",
         F["Dt"](F["m"]) + 4 * sp.pi * R**2 * F["j"] * F["W"], (H_U0,)),
    ]


def spherical_form(F):
    """Residuals that the family's metric is diagonal with R^2 dOmega^2."""
    sp, g, th = F["sp"], F["g"], F["E"]["th"]
    off = [g[a, b] for a in range(4) for b in range(4) if a != b]
    return off + [_z(sp, g[2, 2] - F["R"]**2),
                  _z(sp, g[3, 3] - F["R"]**2 * sp.sin(th)**2)]


def null_identities(F):
    """T_kk for the outgoing (sign +1) and ingoing (-1) radial null vectors
    k = u +- n, built from the family's Einstein tensor, minus
    rho + p_r -+ 2 j.  Both must be 0."""
    sp, Ein = F["sp"], F["Ein"]
    Phi, Lam = F["f"] * F["ph"], F["Lam"]
    out = {}
    for sgn, name in ((1, "outgoing"), (-1, "ingoing")):
        k = [sp.exp(-Phi), sgn * sp.exp(-Lam), 0, 0]
        Tkk = sum(Ein[a, b] * k[a] * k[b] for a in range(2) for b in range(2)) / (8 * sp.pi)
        out[name] = _z(sp, Tkk - (F["rho"] + F["p_r"] - 2 * sgn * F["j"]))
    return out


def no_time_derivatives(F):
    """rho and p_r carry neither fdot nor fddot: INSTANTANEOUS in the slice."""
    return {k: (F[k].has(F["fd"]) or F[k].has(F["fdd"])) for k in ("rho", "p_r")}


def flat_end(F):
    """Every component of G_ab at f = 0, at rest.  All 0 <=> the end is flat."""
    sp = F["sp"]
    return [_z(sp, _at(F, F["Ein"][a, b], 0)) for a in range(4) for b in range(a, 4)]


def seated_end(F):
    """At f = 1: the metric components against certify's conformastatic form,
    and the stress tensor against the static conformastatic one (same
    machinery, Phi = phi, Lambda = -phi, R = r e^{-phi})."""
    sp, r, ph = F["sp"], F["r"], F["ph"]
    g1 = _at(F, F["g"], 1)
    th = F["E"]["th"]
    want = sp.diag(-sp.exp(2 * ph), sp.exp(-2 * ph), r**2 * sp.exp(-2 * ph),
                   r**2 * sp.exp(-2 * ph) * sp.sin(th)**2)
    metric = [_z(sp, g1[a, a] - want[a, a]) for a in range(4)]
    E = F["E"]
    subs = {E["Phi"]: ph, E["Lam"]: -ph, E["R"]: r * sp.exp(-ph)}
    stat = {k: E[k].subs(subs).doit() for k in ("rho", "p_r", "p_T")}
    stress = [_z(sp, _at(F, F[k], 1) - stat[k]) for k in ("rho", "p_r", "p_T")]
    return metric, stress


def fd_cross_check(F, S, r0=1):
    """INDEPENDENT ROUTE: certify's 4th-order finite-difference Einstein tensor,
    Cartesian, at x = (0, r0, 0, 0), against this file's symbolic f = 1 values.
    certify returns G_ab (c^4/8piG = 1), so its T_hat is 8 pi times ours."""
    sp = F["sp"]
    g = certify.conformastatic()
    x = [0.0, float(r0), 0.0, 0.0]
    Th = certify.orthonormal(certify.stress_energy(g, x, 1e-3), g(x))
    out = []
    for k, idx in (("rho", 0), ("p_r", 1), ("p_T", 2)):
        e = _at(F, F[k], 1).subs(F["ph"], S["phi_in"].subs(S["r"], F["r"])).doit()
        v = float(8 * sp.pi * e.subs(F["r"], r0))
        out.append((k, v, Th[idx][idx]))
    return out


# ============================================= section 2: the price per sphere
def price_integrals(F):
    """INT 4 pi R^2 j dtau and INT 4 pi R^2 j W dtau, done symbolically.  The
    integrand j e^{f phi} / fdot depends on t only through f, so the time
    integral IS an integral over f from 0 to 1, whatever f(t) is."""
    sp, f, ph, R = F["sp"], F["f"], F["ph"], F["R"]
    fs = sp.Symbol("f_s")
    per_df = sp.simplify(F["j"] * sp.exp(f * ph) / F["fd"])
    free_of_t = not per_df.has(F["fd"]) and not per_df.has(F["fdd"])
    E_int = sp.integrate((4 * sp.pi * R**2 * per_df).subs(f, fs), (fs, 0, 1))
    K_int = sp.integrate((4 * sp.pi * R**2 * per_df * F["W"]).subs(f, fs), (fs, 0, 1))
    W1 = F["W1"]
    return dict(free_of_t=free_of_t,
                E_residual=_z(sp, E_int - R * (W1 - 1)),
                K_residual=_z(sp, K_int - R * (W1**2 - 1) / 2),
                j_int=_z(sp, sp.integrate(per_df.subs(f, fs), (fs, 0, 1))))


def on_seated(S, sp, mp, r0, side="in", dps=40):
    """W_1, omega, R, E, K, radial deficit, transverse coefficient at r0."""
    r = S["r"]
    phi = S["phi_in"] if side == "in" else S["phi_out"]
    W1 = 1 - r * sp.diff(phi, r)
    R = r * sp.exp(-phi)
    mp.mp.dps = dps
    q = lambda e: mp.mpf(sp.N(e.subs(r, sp.nsimplify(r0)), dps))
    w1, RR = q(W1), q(R)
    om = mp.log(w1)
    return dict(r=r0, side=side, W1=w1, omega=om, R=RR,
                E=RR * (w1 - 1), K=RR * (w1**2 - 1) / 2,
                radial=-(w1 - 1) / (2 * mp.pi * RR),
                transverse_coeff=om**2 / (8 * mp.pi),
                phi=q(phi))


def raw_m1(F, S, sp, mp, r0, dps=40):
    """m at f = 1, at rest, from the family's RAW Misner-Sharp expression
    (general_einstein's m), evaluated on the seated interior phi at r0."""
    e = _at(F, F["m"], 1).subs(F["ph"], S["phi_in"].subs(S["r"], F["r"])).doit()
    mp.mp.dps = dps
    return mp.mpf(sp.N(e.subs(F["r"], sp.nsimplify(r0)), dps))


def adm_mass(S, sp):
    """lim_{r->inf} m_1 = lim (R/2)(1 - W_1^2) on the exterior branch."""
    r, phi = S["r"], S["phi_out"]
    W1 = 1 - r * sp.diff(phi, r)
    return sp.limit(r * sp.exp(-phi) * (1 - W1**2) / 2, r, sp.oo)


def exterior_tail(S, sp):
    """lim r^3 phi_out: nonzero means the seated object is not compactly
    supported (phase1 D2)."""
    return sp.limit(S["r"]**3 * S["phi_out"], S["r"], sp.oo)


def shell_jump(S, sp, mp, dps=40):
    """m_1(R_s+) - m_1(R_s-): the Kodama mass the passage deposits in the shell."""
    a = on_seated(S, sp, mp, S["Rs"], "in", dps)
    b = on_seated(S, sp, mp, S["Rs"], "out", dps)
    return (-b["K"]) - (-a["K"]), a, b


# -------------------------------------------- the z3 encoding, from ONE source
# r phi'(r) times a positive multiplier, as a polynomial in (m, r, s) with
# s = sqrt(r^2 + a^2).  The SAME callables build the z3 goals and are checked
# against sympy's phi_in / phi_out by z3_encoding_residuals (drift guard).
Z3_MULT = {"in": lambda r, s: s**3, "out": lambda r, s: r * s**3}
Z3_POLY = {"in": lambda m, r, s: -m * r * r,
           "out": lambda m, r, s: m * s**3 - m * r**3}


def z3_encoding_residuals(sp, poly=None):
    """ENCODING-DRIFT GUARD (PROOF-ASSISTANT.md): r phi' x multiplier from
    phi_forms, minus the polynomial handed to z3, for symbolic m, a, R_s > 0.
    Each must simplify to 0."""
    poly = poly or Z3_POLY
    m, a, r, Rs = sp.symbols("m a r R_s", positive=True)
    s = sp.sqrt(r**2 + a**2)
    pin, pout = phi_forms(sp.sqrt, m, a, Rs, r)
    return {side: sp.simplify(r * sp.diff(ph, r) * Z3_MULT[side](r, s)
                              - poly[side](m, r, s))
            for side, ph in (("in", pin), ("out", pout))}


def z3_signs(z3):
    """W_1 > 1 inside, 0 < W_1 < 1 outside, for EVERY m, a > 0 and r in range.
    s = sqrt(r^2 + a^2) is a variable constrained by s > 0, s^2 = r^2 + a^2.
    W_1 = 1 - r phi'; the obligations are on Z3_POLY (r phi' x a positive
    multiplier), so they are polynomial."""
    m, a, r, s, Rs = z3.Reals("m a r s Rs")
    base = [m > 0, a > 0, r > 0, s > 0, s * s == r * r + a * a]
    Pin, Pout = Z3_POLY["in"](m, r, s), Z3_POLY["out"](m, r, s)
    Mout = Z3_MULT["out"](r, s)

    def unsat(h, goal):
        so = z3.Solver()
        so.add(*h)
        so.add(z3.Not(goal))
        return so.check() == z3.unsat
    inside = unsat(base, Pin < 0)                     # r phi' < 0: W_1 > 1
    hout = base + [Rs > m, r > Rs]
    out_pos = unsat(hout, Pout > 0)                   # r phi' > 0: W_1 < 1
    out_lt1 = unsat(hout, Pout < Mout)                # r phi' < 1: W_1 > 0
    # VACUITY GUARD: the false claim "W_1 > 1 outside" must be SAT-refutable
    g = z3.Solver()
    g.add(*hout)
    g.add(z3.Not(Pout < 0))
    guard = g.check() == z3.sat
    return dict(inside=inside, out_pos=out_pos, out_lt1=out_lt1, guard=guard)


# ================================= section 3: integrals over a passage, numeric
PROFILES = {
    "smoothstep": lambda sp, s: 3 * s**2 - 2 * s**3,
    "sine": lambda sp, s: sp.sin(sp.pi * s / 2)**2,
    "overshoot": lambda sp, s: 3 * s**2 - 2 * s**3 + sp.Rational(4, 5) * sp.sin(sp.pi * s)**2,
}
# NOT at rest at either end: shows F1 does not use H_REST
CONTROL_PROFILES = {"linear": lambda sp, s: s}


def profile_ends(sp, fn):
    """(f(0), f(1), f'(0), f'(1)) of a profile, exactly."""
    s = sp.Symbol("s")
    p = fn(sp, s)
    dp = sp.diff(p, s)
    return tuple(sp.simplify(e) for e in (p.subs(s, 0), p.subs(s, 1),
                                          dp.subs(s, 0), dp.subs(s, 1)))


def passage_integrals(F, S, mp, profile, T, r0=1, dps=30):
    """Run the RAW family stress tensor (not the closed forms) through one
    passage of coordinate duration T at r0, and integrate in Eulerian proper
    time.  Returns (INT j dtau, INT transverse time part dtau,
    INT f_tau^2 dtau, proper duration, INT j W dtau)."""
    sp = F["sp"]
    t, f, ph, r = F["t"], F["f"], F["ph"], F["r"]
    phi = S["phi_in"].subs(S["r"], r)
    fn = PROFILES[profile] if profile in PROFILES else CONTROL_PROFILES[profile]
    prof = fn(sp, t / T)
    j = F["j"]
    pTt = F["p_T"] - _static(F, F["p_T"])
    rhoT_time = pTt                     # rho carries no time derivative
    lapse = sp.exp(f * ph)
    ftau2 = (sp.exp(-f * ph) * F["fd"])**2

    def num(e):
        e = e.subs(ph, phi).doit().subs(r, sp.nsimplify(r0))
        e = e.subs(f, prof).doit()
        return sp.lambdify(t, e, modules="mpmath")
    mp.mp.dps = dps
    fj, fp, ff, fl, fjw = (num(j * lapse), num(rhoT_time * lapse),
                           num(ftau2 * lapse), num(lapse), num(j * F["W"] * lapse))
    Tq = mp.mpf(sp.N(T, dps))
    q = lambda fn_: mp.quad(fn_, [0, Tq / 4, Tq / 2, 3 * Tq / 4, Tq])
    return q(fj), q(fp), q(ff), q(fl), q(fjw)


# ========================================= section 6: D25, the gate predicate
def gate(aperture=None, bodies=(), payload_kg=70.0, pkind="as-composed 59",
         dkind="CI chondrite"):
    """stockgate.GATE as a three-valued predicate.  This is a MODEL of GATE's
    wording, used only to show what binding the aperture would decide.
    aperture is (centre_au, half_width_au).  bodies are
    (orbit_au, condensed, primitive, accessible_kg), where a conjunct may be
    None = unmeasured.  With no aperture the predicate has an UNBOUND VARIABLE
    and returns NOT-EVALUABLE.  Otherwise it returns True if some body
    satisfies every conjunct, UNDETERMINED if none does but one might (an
    unmeasured conjunct), and False otherwise.  The mass threshold is
    stockgate.feedstock_kg's."""
    if aperture is None:
        return "NOT-EVALUABLE"
    need = stockgate.feedstock_kg(payload_kg, pkind, dkind)
    c, w = aperture
    verdicts = []
    for a, cond, prim, kg in bodies:
        if abs(a - c) > w:
            continue
        conj = (cond, prim, None if kg is None else kg >= need)
        if all(x is True for x in conj):
            return True
        if not any(x is False for x in conj):
            verdicts.append(UNDETERMINED)
    return UNDETERMINED if verdicts else False


def proxima_b_over_threshold():
    """Proxima b's minimum mass (READ) over stockgate's 70 kg feedstock
    threshold at a CI chondrite (imported, not re-priced)."""
    need = stockgate.feedstock_kg(70.0, "as-composed 59", "CI chondrite")
    return PROXIMA_B_MSINI_EARTH * ladder.M_EARTH / need


# ================================================================== the reading
def _fmt(x, n=6):
    return ("%%.%de" % (n - 1)) % float(x)


def report():
    sp, mp, z3 = _need()
    print(__doc__.split("=" * 79)[0].strip())
    S = seated(sp)
    print("\n" + "=" * 79)
    print("THE PRICE ON THE SEATED OBJECT  (m = a = %s, R_s = %s; geometric units,"
          % (S["m"], S["Rs"]))
    print("lengths in certify's unit L)")
    print("=" * 79)
    print("  %-8s %-4s %-12s %-12s %-12s %-12s %-12s %-12s"
          % ("r", "side", "W_1", "R", "E=R(W1-1)", "K=-m_1", "radial NEC", "om^2/8pi"))
    for r0, side in ((0.005, "in"), (0.02, "in"), (0.05, "in"), (0.2, "in"),
                     (1, "in"), (10, "in"), (100, "in"), (250, "out"), (1000, "out")):
        v = on_seated(S, sp, mp, r0, side)
        print("  %-8s %-4s %-12s %-12s %-12s %-12s %-12s %-12s"
              % (r0, side, _fmt(v["W1"]), _fmt(v["R"]), _fmt(v["E"]), _fmt(v["K"]),
                 _fmt(v["radial"]), _fmt(v["transverse_coeff"])))
    jump, a, b = shell_jump(S, sp, mp)
    print("\n  Kodama mass deposited at the shell, m_1(R_s+) - m_1(R_s-) = %s" % _fmt(jump))
    print("  ADM mass of the seated object (limit)                       = %s"
          % adm_mass(S, sp))
    print("  lim r^3 phi_out (not compactly supported: fails phase1 D2) = %s"
          % exterior_tail(S, sp))
    c2g = foliation.C_LIGHT**2 / foliation.G_NEWTON
    v1 = on_seated(S, sp, mp, 1, "in")
    print("  at r = 1: E = %s L,  i.e. %s kg per metre of L (c^2/G, foliation.py)"
          % (_fmt(v1["E"]), _fmt(v1["E"] * c2g)))
    print("\n  transverse, this family:  INT extra dtau <= -(omega^2/8pi)/tau_p")
    print("  radial, every U=0 passage: INT extra dtau  = -(W_1 - 1)/(2 pi R)")
    print("\n  F1 hypotheses: %s" % "; ".join(F1_THEOREM))
    print("  F2 adds:       %s" % H_NULL)
    print("  transverse adds: %s; %s" % (H_FAMILY, H_REST))
    print("\n" + "=" * 79)
    print("D25 -- OPEN AND UNCHANGED; the READ survey")
    print("=" * 79)
    print("  mass threshold: stockgate.py's own (python3 stockgate.py); not re-priced")
    print("  aperture:  %s" % APERTURE_STATUS)
    print("             %s" % APERTURE_SEARCH)
    print("  snow line: %s" % SNOWLINE_SEARCH)
    print("  gate(aperture=None) -> %s" % gate())
    for who, arx, what in SURVEY_SOURCES:
        print("  READ %-22s %-18s %s" % (who, arx, what))
    print("  condensed body in the sources read: %s; its minimum mass / stockgate's "
          "70 kg threshold = %s" % (SURVEY_CONDENSED_BODY, _fmt(proxima_b_over_threshold(), 3)))
    print("  primitive measured: %s; accessible measured: %s; reservoir: %s"
          % (SURVEY_PRIMITIVE_MEASURED, SURVEY_ACCESSIBLE_MEASURED,
             SURVEY_CONFIRMED_RESERVOIR))
    print("\n  D24: %s" % D24_VERDICT)
    print("  D25: %s" % D25_VERDICT)
    print("  nucleation: %s; EC evidence: %s" % (NUCLEATION_STATUS,
                                                 " | ".join(NUCLEATION_EC_EVIDENCE)))
    print("\n  STATUS")
    for k, v in STATUS.items():
        print("    %-58s %s" % (k, v))


# ================================================================== the selftest
KINDS = ("residual", "numeric", "control", "consistency", "pin")


def selftest():
    sp, mp, z3 = _need()
    fails = []
    rows = []
    discharged = set()
    row_hyps = []     # (label, hyp) of every passing row -- read back by section 6

    def chk(kind, label, got, want, tol=None, hyp=()):
        assert kind in KINDS, kind
        if tol is None:
            ok = got == want
        else:
            ok = abs(float(got) - float(want)) <= tol * max(1.0, abs(float(want)))
        tag = {"residual": "res", "numeric": "num", "control": "CTL",
               "consistency": "cns", "pin": "pin"}[kind]
        print("  [%s] %s %-64s %s" % ("ok" if ok else "XX", tag, label, got))
        rows.append((kind, ok))
        if ok:
            discharged.update(hyp)
            row_hyps.append((label, tuple(hyp)))
        else:
            fails.append((label, got, want))

    print("formation.py --selftest")
    print("  kinds: res = symbolic residual, num = computed figure, CTL = a control")
    print("  that can fail, cns = consistency (not a control), pin = record pin\n")
    print("1. THE FAMILY -- both ends symbolic, and a broken family that must fail")
    F = family()
    for lab, res, hyp in closed_forms(F):
        chk("residual", lab, _z(sp, res), 0, hyp=hyp)
    chk("residual", "metric diagonal with R^2 dOmega^2 (spherical symmetry)",
        set(spherical_form(F)), {0}, hyp=(H_SPH,))
    nulls = null_identities(F)
    chk("residual", "T_kk = rho + p_r - 2j, outgoing null k = u + n", nulls["outgoing"], 0,
        hyp=(H_NULL,))
    chk("residual", "T_kk = rho + p_r + 2j, ingoing null k = u - n", nulls["ingoing"], 0)
    chk("residual", "rho, p_r carry no time derivative", no_time_derivatives(F),
        {"rho": False, "p_r": False})
    chk("residual", "f = 0: all ten G_ab components vanish (FLAT)", set(flat_end(F)), {0})
    met, st = seated_end(F)
    chk("residual", "f = 1: metric = certify's conformastatic, componentwise", set(met), {0})
    chk("residual", "f = 1: rho, p_r, p_T = the static conformastatic values", set(st), {0})
    Fb = family(broken=True)
    chk("control", "broken family (Lambda = -f phi) is NOT flat at f = 0",
        set(flat_end(Fb)) != {0}, True)
    S = seated(sp)
    chk("pin", "seated constants read from certify as rationals m, a, R_s",
        (S["m"], S["a"], S["Rs"]), (sp.Rational(1, 50), sp.Rational(1, 50), 200))
    for r0, side, rel in phi_vs_certify(S, sp):
        chk("control", "phi_%s = certify.phi at r = %s (relative to m/r)" % (side, r0),
            rel, 0, 1e-13)
    for k, mine, theirs in fd_cross_check(F, S, 1):
        chk("control", "INDEPENDENT: 8 pi %s (sympy) vs certify FD at r=1, rel" % k,
            abs(mine - theirs) / abs(theirs), 0, 1e-6, hyp=(H_EFE,))
    lapse_grad = _at(F, F["DrPhi"], sp.Rational(1, 2)).subs(
        F["ph"], S["phi_in"].subs(S["r"], F["r"])).doit().subs(F["r"], 1)
    chk("numeric", "the family's lapse gradient at f = 1/2, r = 1 (nonzero)",
        float(lapse_grad) != 0.0, True)

    print("\n2. THE PRICE PER SPHERE -- F1")
    P = price_integrals(F)
    chk("residual", "j e^{f phi}/fdot depends on t only through f", P["free_of_t"], True)
    chk("residual", "INT 4 pi R^2 j dtau = R (W_1 - 1), any f(t)", P["E_residual"], 0)
    chk("residual", "INT 4 pi R^2 j W dtau = R (W_1^2 - 1)/2 = -m_1, any f(t)",
        P["K_residual"], 0)
    enc = z3_encoding_residuals(sp)
    chk("residual", "ENCODING GUARD: z3 poly = s^3 r phi_in' (sympy)", enc["in"], 0)
    chk("residual", "ENCODING GUARD: z3 poly = r s^3 r phi_out' (sympy)", enc["out"], 0)
    drift = z3_encoding_residuals(sp, {"in": lambda m, r, s: -m * r**3,
                                       "out": Z3_POLY["out"]})
    chk("control", "the encoding guard rejects a drifted polynomial (-m r^3)",
        drift["in"] != 0, True)
    zs = z3_signs(z3)
    chk("residual", "z3: W_1 > 1 for 0 < r (inside the shell), all m, a > 0",
        zs["inside"], True, hyp=(H_W,))
    chk("residual", "z3: W_1 < 1 outside (r > R_s > m)", zs["out_pos"], True)
    chk("residual", "z3: W_1 > 0 outside", zs["out_lt1"], True, hyp=(H_W,))
    chk("control", "VACUITY GUARD: 'W_1 > 1 outside' is refutable", zs["guard"], True)
    chk("residual", "ADM mass of the seated object is 0 (concentric.py's M_ADM = 0)",
        adm_mass(S, sp), 0)
    tail = exterior_tail(S, sp)
    chk("residual", "lim r^3 phi_out = -m a^2/2 (not compact support: fails D2)",
        sp.simplify(tail + S["m"] * S["a"]**2 / 2), 0)
    chk("pin", "phase1 D2 is 'compact support', and SEATED_COMPACT_SUPPORT is False",
        ([c for c in phase1.CONDITIONS if c[0] == "D2"][0][1], SEATED_COMPACT_SUPPORT
         == (tail == 0)), ("compact support", True))
    jump, a, b = shell_jump(S, sp, mp)
    chk("numeric", "the shell receives positive Kodama mass", jump > 0, True)
    chk("numeric", "  and the exterior side carries almost none: |m_1(R_s+)| < 1e-6",
        abs(jump - a["K"]) < 1e-6, True)
    v1 = on_seated(S, sp, mp, 1, "in")
    chk("numeric", "K(r=1) = -m_1 from the family's RAW Misner-Sharp m at f = 1",
        abs(v1["K"] + raw_m1(F, S, sp, mp, 1)) < mp.mpf(10)**-30, True)
    # CONSISTENCY, NOT A CONTROL: nonstatic.build_energy computes R dW c^2/G,
    # the same arithmetic as the right-hand side here.  It pins units and
    # convention only.  E itself is controlled in section 3 by the raw passage
    # integral.
    L = 1.0
    kg_nonstatic = nonstatic.build_energy(float(v1["R"]) * L, float(v1["W1"] - 1))[1]
    kg_mine = float(v1["E"]) * L * nonstatic.C**2 / nonstatic.G
    chk("consistency", "E(r=1) in kg agrees with nonstatic.build_energy's units",
        kg_mine, kg_nonstatic, 1e-12)

    print("\n3. INTEGRALS OVER REAL PASSAGES -- raw stress tensor, three profiles")
    for p, fn in list(PROFILES.items()):
        f0, f1, d0, d1 = profile_ends(sp, fn)
        chk("residual", "profile %-10s runs f = 0 -> 1" % p, (f0, f1), (0, 1), hyp=(H_ENDS,))
        chk("residual", "profile %-10s at rest at both ends" % p, (d0, d1), (0, 0),
            hyp=(H_REST,))
    T = sp.Integer(3)
    runs = {p: passage_integrals(F, S, mp, p, T) for p in PROFILES}
    want_j = (v1["W1"] - 1) / (4 * mp.pi * v1["R"])
    fourpiR2 = 4 * mp.pi * v1["R"]**2
    for p, (ij, ipt, iff, tau, ijw) in runs.items():
        chk("numeric", "INT j dtau = (W_1-1)/(4 pi R), profile %-10s (25 digits)" % p,
            abs(ij - want_j) < mp.mpf(10)**-25, True)
        chk("control", "4 pi R^2 INT j dtau (raw) = on_seated E, %-10s" % p,
            abs(fourpiR2 * ij - v1["E"]) < mp.mpf(10)**-25, True)
        chk("control", "4 pi R^2 INT j W dtau (raw) = on_seated K, %-10s" % p,
            abs(fourpiR2 * ijw - v1["K"]) < mp.mpf(10)**-25, True)
        chk("control", "-2 INT j dtau (raw) = on_seated radial deficit (F2), %-10s" % p,
            abs(-2 * ij - v1["radial"]) < mp.mpf(10)**-25, True)
        chk("numeric", "INT transverse time part = -(omega^2/8pi) INT f_tau^2, %-10s" % p,
            abs(ipt + v1["omega"]**2 / (8 * mp.pi) * iff) < mp.mpf(10)**-25, True)
        chk("numeric", "  and it is <= -(omega^2/8pi)/tau_p  (Cauchy-Schwarz), %-10s" % p,
            ipt <= -v1["omega"]**2 / (8 * mp.pi) / tau, True)
    lf0, lf1, ld0, ld1 = profile_ends(sp, CONTROL_PROFILES["linear"])
    lin = passage_integrals(F, S, mp, "linear", T)
    chk("control", "F1 without rest: linear profile (f' = 1 at both ends) gives the "
        "same INT j", (ld0 != 0 and ld1 != 0, abs(lin[0] - want_j) < mp.mpf(10)**-25),
        (True, True))
    chk("control", "the transverse integrals DIFFER between profiles",
        len({mp.nstr(v[1], 12) for v in runs.values()}), len(PROFILES))
    ij2, ipt2 = passage_integrals(F, S, mp, "smoothstep", 2 * T)[:2]
    chk("control", "doubling the duration leaves the radial integral fixed",
        abs(ij2 - runs["smoothstep"][0]) < mp.mpf(10)**-25, True)
    chk("control", "  and halves the transverse one exactly (the lapse depends on f only)",
        abs(ipt2 / runs["smoothstep"][1] - mp.mpf(1) / 2) < mp.mpf(10)**-20, True)
    chk("pin", "phase1 D4 is stated as T^{0i} = 0 (READ from phase1.CONDITIONS)",
        [c for c in phase1.CONDITIONS if c[0] == "D4"][0][1].startswith("no momentum"),
        True)
    d4_holds = all(v[0] == 0 for v in runs.values())
    # M ruled (DOCKET 64 D.2): D4 is restated -- T^{0i} = 0 per configuration,
    # zero NET momentum per passage.  Under it this passage, whose flux is
    # transient and radial with zero net momentum, is a TRANSITION.
    chk("control", "under D4 as restated, this passage is a transition, not propulsion",
        phase1.is_transition(False, True, True, True, True,
                             net_momentum=False, passage_flux=not d4_holds), True)
    chk("numeric", "INT j dtau != 0 on every profile, so D4 fails pointwise; "
        "the attribute agrees", (d4_holds, PHASE1_D4_POINTWISE_DURING_PASSAGE),
        (False, d4_holds))

    print("\n4. D24's OTHER PARTS -- READ, and OPEN")
    chk("pin", "create.py still names nucleation NOT-RUN", create.NUCLEATION_STATUS, "NOT-RUN")
    chk("pin", "nucleation: no closed-form neck; a recipe with free functions",
        (NUCLEATION_NECK_EXPLICIT, NUCLEATION_NECK_RECIPE, len(NUCLEATION_FREE_FUNCTIONS) > 0),
        (False, True, True))
    chk("pin", "nucleation: not priced; priceability NOT DETERMINED (W3 kept)",
        (NUCLEATION_PRICED, NUCLEATION_PRICEABLE_FROM_SOURCE,
         NUCLEATION_PRICEABLE_FROM_SOURCE_WITHDRAWN[0]), (False, NOT_DETERMINED, False))
    chk("pin", "nucleation: CTCs; qualitative EC evidence, no integrated figure",
        (NUCLEATION_HAS_CTC, len(NUCLEATION_EC_EVIDENCE) > 0, NUCLEATION_EC_FIGURE),
        (True, True, False))

    print("\n5. D25 -- unchanged; the named searches recomputed; the gate predicate")
    for pat, hits, name in ((APERTURE_PATTERN, APERTURE_HITS, "aperture"),
                            (APERTURE_SYNONYM_PATTERN, APERTURE_SYNONYM_HITS,
                             "aperture synonyms"),
                            (SNOWLINE_PATTERN, SNOWLINE_HITS, "snow line")):
        found = tree_search(pat)
        chk("control", "the %s search's file set = the classified record" % name,
            sorted(found ^ set(hits)), [])
    chk("pin", "the aperture record says NOT EVALUABLE: NOT-FOUND (search named)",
        APERTURE_STATUS.startswith("NOT EVALUABLE: aperture NOT-FOUND"), True)
    chk("pin", "gate with no aperture returns NOT-EVALUABLE (a definition)",
        gate(), "NOT-EVALUABLE")
    need = stockgate.feedstock_kg(70.0, "as-composed 59", "CI chondrite")
    chk("control", "gate can return True (a body inside, primitive, enough mass)",
        gate((3.0, 1.0), [(3.5, True, True, 2 * need)]), True)
    chk("control", "and False (same body, devolatilised)",
        gate((3.0, 1.0), [(3.5, True, False, 2 * need)]), False)
    chk("control", "and False (primitive, but under the mass)",
        gate((3.0, 1.0), [(3.5, True, True, 0.5 * need)]), False)
    pb_kg = PROXIMA_B_MSINI_EARTH * ladder.M_EARTH
    chk("control", "and UNDETERMINED for Proxima b (condensed, primitive unmeasured), "
        "synthetic aperture", gate((PROXIMA_B_A_AU, 0.01),
                                   [(PROXIMA_B_A_AU, True, None, pb_kg)]), UNDETERMINED)
    chk("numeric", "Proxima b's minimum mass exceeds stockgate's 70 kg threshold (log10)",
        math.log10(proxima_b_over_threshold()) > 0, True)
    chk("pin", "survey: condensed body found; primitive, accessible unmeasured; "
        "reservoir UNDETERMINED",
        (SURVEY_CONDENSED_BODY_FOUND, SURVEY_PRIMITIVE_MEASURED,
         SURVEY_ACCESSIBLE_MEASURED, SURVEY_CONFIRMED_RESERVOIR,
         SURVEY_CONFIRMED_RESERVOIR_WITHDRAWN[0]),
        (True, False, False, UNDETERMINED, False))
    chk("pin", "survey: the papers' data constrain no individual bodies",
        SURVEY_CONSTRAINS_BODIES, False)
    chk("pin", "stockgate's T_c are nebular, at 1e-4 bar (READ from its SOURCES)",
        "1e%d bar" % round(math.log10(LODDERS_PRESSURE_BAR)) in stockgate.SOURCES["L03"],
        True)

    print("\n6. EVERY NAMED HYPOTHESIS IS DISCHARGED BY A PASSING ROW")
    missing = [h for h in ALL_HYPOTHESES if h not in discharged]
    chk("control", "F1, F2 and transverse hypotheses without a discharging row",
        missing, [])
    # The OTHER direction (DOCKET 64 seating verifier): a hypothesis a row USES to
    # prove F2 must be NAMED in F2_THEOREM.  Taken from the rows, not from H_NULL,
    # so setting F2_THEOREM = F1_THEOREM (dropping the null hypothesis) fires here.
    f2_row_hyps = set(h for lab, hyp in row_hyps if "outgoing null" in lab for h in hyp)
    chk("control", "every hypothesis the outgoing-null rows use is named in F2_THEOREM",
        sorted(f2_row_hyps - set(F2_THEOREM)), [])
    chk("control", "and F2 names every F1 hypothesis (F2 extends F1)",
        sorted(set(F1_THEOREM) - set(F2_THEOREM)), [])
    chk("control", "  and the outgoing-null rows do use a hypothesis F1 lacks",
        bool(f2_row_hyps - set(F1_THEOREM)), True)

    print()
    counts = {k: sum(1 for kk, _ in rows if kk == k) for k in KINDS}
    summary = ("%d checks: %s" % (len(rows), ", ".join("%d %s" % (counts[k], k)
                                                        for k in KINDS)))
    if fails:
        print("  SELFTEST FAILED: %d of %s" % (len(fails), summary))
        for fl in fails:
            print("    %s: got %r want %r" % fl)
        return 1
    print("  SELFTEST OK, %s" % summary)
    return 0


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(selftest())
    report()
