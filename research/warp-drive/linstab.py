#!/usr/bin/env python3
r"""
linstab.py -- LINEARISED STABILITY.  THE AMM CRITERION, ASKED OF WHAT THE DEMAND
COLUMN PRICES.

    python3 linstab.py             the reading (sympy, mpmath)
    python3 linstab.py --selftest  every figure re-derived; sympy, z3, mpmath

Run under python3 (3.11) from ANY directory that does not have the repository's
`recovered/` on sys.path (recovered/struct.py shadows the stdlib and breaks
`import sympy`; axial.py records the fault).  This file puts only its own
directory, research/warp-drive, on the path, and _need() refuses to run if the
`struct` it would get is not the stdlib's.

SEATED UNDER DOCKET 64's RULING (sections A4, B4) AND THE verify-stability
VERDICT (which the ruling did not see).  Where the two differ the weaker,
better-supported statement is the one kept.  Every withdrawn sentence is KEPT
below, marked WITHDRAWN, with the reason; WITHDRAWN (the tuple) carries them.

===============================================================================
0.  THE QUESTION, AND THE ANSWER
===============================================================================

ledger.py's WAITS_FOR_ITS_INSTRUMENT held "linearised stability" with no row,
because no instrument asked it.  The criterion is Anderson, Molina-Paris &
Mottola's (AMM, gr-qc/0209075 v1, abstract and section III p. 10): "solutions to
the semi-classical Einstein equations should be stable to linearized
perturbations, in the sense that no gauge invariant perturbation should become
unbounded in time."  THE QUESTION: can it be evaluated on any configuration the
demand column prices, and what does it return?

    IN THE CLASSICAL RADIAL SECTOR: YES, AND IT RETURNS STABLE -- A THEOREM.
    On the thin-shell object stability.py prices (Schwarzschild M_in = -m
    inside, Minkowski outside), with u = sqrt(1 + 2m/R), EXACTLY (sympy):

        V''(R_0) = [ 2 beta^2 (3u + 1) u^2 + (u - 1)(3u^2 + 2u + 1)/2 ] / (u^2 R^2)
        beta^2_crit(u) = -(u - 1)(3u^2 + 2u + 1) / (4 u^2 (3u + 1))

    beta^2_crit < 0 for EVERY m > 0 (z3), strictly decreasing, with infimum
    exactly -1/4 as m/R -> infinity.  So every beta^2 >= 0 is strictly stable
    -- beta^2 = 0 meaning NO PRESSURE RESPONSE (the static shell carries a
    tension p0 < 0, so it is not dust) -- and so is any beta^2 > -1/4 at large
    compactness.  This upgrades stability.py's four-point finite-difference
    SURVEY to a THEOREM over all m > 0, and its "NEARLY MIRROR IMAGES" to an
    EXACT identity: the device's V'' and beta^2_crit are the SAME FUNCTIONS as
    wall.py's ordinary shell, with s = sqrt(1 - 2M/R) < 1 replaced by
    u = sqrt(1 + 2m/R) > 1.  The factor (1 - s) carries the sign: the interior
    sign flip moves the argument across 1, and that is all it does.
      WITHDRAWN: "every beta^2 >= 0 -- dust included --".  beta^2 = 0 is no
      pressure response, not dust (verify-stability NOTE).

    IN THE SEMICLASSICAL SENSE AMM DEFINE: NOT EVALUABLE AT PRESENT.  AMM's
    linear-response equation (3.4) is the first variation of the semiclassical
    equations (2.9) ABOUT A SOLUTION of them: "the first variation vanishes by
    (2.9)" (p. 8), and the retarded correlator "is evaluated in the background
    geometry of the leading order solution of the semi-classical equations
    (2.9)" (p. 9).  Off a solution the linearised equation carries a
    zeroth-order source (the residual), and selftest section 3 proves by two
    exact witnesses (W1, W2) that a boundedness verdict computed there is not
    a property of the dynamics -- in either direction.  No configuration the
    demand column prices is RECORDED OR SHOWN to be a solution of (2.9): each
    prices a METRIC and reads its source off the Einstein tensor.  That is
    precondition H1 UNESTABLISHED, pending O5 -- NOT a proof that the
    configurations fail to be solutions; the existence question is O5's, and
    O5 is OPEN.
      The tree now holds self-consistent solutions WITH m < 0: hpscentre.py
    (DOCKET 64) finds them in HPS's model system (conserved reading), at a
    regular centre and on HPS's throat data -- outside the domain in which the
    AHS approximation has been established.  The obstruction survives them:
    they solve G = 8 pi <T> with <T> an APPROXIMATION (AHS), not AMM's (2.9)
    with the renormalised <T_ab> of a SPECIFIED state, and no Pi^(ret) exists
    for them.  THE MISSING QUANTITY, EXACTLY: a state omega on the
    configuration whose renormalised <T_ab>_omega equals the configuration's
    semiclassical left-hand side (AMM (2.9): Einstein tensor + Lambda g + the
    alpha, beta fourth-order terms) -- which is O5 -- and THEN the retarded
    polarization tensor Pi^(ret) (AMM (3.5), (3.9)) in that state on it.
      WITHDRAWN: "NO -- AND THE OBSTRUCTION IS PROVED", and "none of the demand
      configurations is one".  What is shown is that none is RECORDED OR
      SHOWN to be one: a scan of the tree, not a proof (ruling A4.3;
      verify-stability SHOULD-FIX).
      WITHDRAWN: "the only self-consistent solutions the tree holds
      (throatmass.py's six families) all have m >= 0".  Stale once
      hpscentre.py is seated (ruling A4.2); throatmass.py's families are what
      was REPORTED, and that part stays true.

    THE FLAT EXTERIOR DOES NOT INHERIT EITHER PAPER'S VERDICT.  The device's
    exterior is flat only for r > R_s.  AMM's flat-space analysis Fourier-
    transforms over all of Minkowski space (IV, (4.2)-(4.5)); GMMPS's theorem
    is posed on (R^4, eta) with the global Poincare vacuum and past-compact
    perturbations of all of R^4 (their 1.2, Thm 1.2).  A region of Minkowski
    bounded by a shell satisfies neither, so neither "stable" nor "unstable"
    transfers to it.  Failure mode 4 declined in the open.

===============================================================================
1.  WHAT EACH PAPER PROVES, AND UNDER WHAT HYPOTHESES  (READ)
===============================================================================

AMM, gr-qc/0209075 v1 (PRD 67, 024026 (2003)), text layer via alphaXiv.
  SETTING  large-N free scalar fields, arbitrary mass m > 0 and curvature
  coupling xi, in the Minkowski vacuum; CTP (in-in) effective action; eq. (2.9)
  the renormalised semiclassical equations with alpha (C^2) and beta (R^2).
  CRITERION (III, p. 10)  a NECESSARY condition for validity: (3.4) has no
  solution "with finite non-singular initial data for which any linearized gauge
  invariant scalar quantity grows without bound"; allowed gauge transformations
  are (3.11), excluding those under which the action (2.7) is not invariant.
  RENORMALISATION (4.4)  three subtractions at k^2 = 0 -- cosmological constant,
  1/G_N, and (alpha, beta) -- "the renormalized values of these parameters at
  k^2 = 0 are what appear then on the left hand side of (2.9)".  In the scalar
  sector (4.5b) the whole equation carries an overall k^2: NO k-independent
  term survives.
  RESULT, TENSOR SECTOR (4.5a)-(4.9)  the (4.6) POSITIVITY STEP uses alpha >= 0
  and rho^(T) >= 0: the bracket is then strictly positive for k^2 > 0 ((4.6):
  16 pi G alpha k^2 + 1 > 0), so no unstable transverse tensor mode; for
  k^2 < 0 no new mode unless G_N |k^2| ~ 1, because Re F^(T) grows only as
  ln|k^2| (4.9).  alpha >= 0 is a hypothesis OF THAT STEP ONLY, not of AMM's
  conclusion: p. 12, "If alpha < 0 then the preceding analyses for k^2 > 0
  and k^2 < 0 interchange roles, with the conclusion unchanged."
  IMPLICIT  the conclusion "cannot be satisfied except at k^2 approaching
  G_N^-1" (p. 12) takes the fourth-order coefficients to be O(1).  That is
  where GMMPS's large-b_2 roots enter (AMM_HYPOTHESES H6).
  RESULT, SCALAR SECTOR (4.5b), (4.11)  no solution with 4 pi G |k^2| << 1.
  NOT TREATED (p. 12)  "a finite number of non-propagating (global) modes in
  the scalar sector at k = 0 ... We do not treat this possibility."
  CONCLUSION  flat space "is stable to all perturbations on distance scales
  much larger than the Planck length" (abstract); growing modes appear only
  at G_N|k^2| = O(1), i.e. Planck scale for O(1) coefficients (V, p. 14).
    WITHDRAWN: "tensor sector needs alpha >= 0 and rho^(T) >= 0" as a
    hypothesis of AMM's RESULT (verify-stability SHOULD-FIX, AMM p. 12).

GALANDA, MEDA, MURRO, PINAMONTI, SCHMID, arXiv:2604.01047 v1 (GMMPS), text
layer via alphaXiv, body read in full.
  SETTING  ONE real Klein-Gordon field, mass m > 0, coupling xi with
  2/(6 xi - 1) < 4 (5.1, for Prop. 4.5); the Poincare vacuum; Hadamard;
  PAST-COMPACT metric and state perturbations posed as a forcing problem
  (1.8); de Donder gauge (Prop. 2.4: a complete gauge fixing for past-compact
  perturbations); renormalisation by Hollands-Wald (1.2) with the background
  fixed by Prop. 3.1, alpha_1 = (1/64 pi^2)(-3/2 + 2 gamma + log(m^2/2mu^2)).
  THE CONSTANT THAT MATTERS FOR THEIR REPORTED MODE  Thm 3.6: by general local
  covariance and perturbative agreement, alpha~^S_1 = 1/(64 pi^2) and
  alpha~^TT_1 = 0.  alpha~^S_2 = alpha~^TT_2 = 0 is ASSUMED (5.1, 5.2).
  alpha~^S_3 and alpha~^TT_4 (through b_2) are FREE.
  RESULT  Thm 1.2 / 4.14: unique past-compact solutions exist; Thm 4.16: a
  zero of the dispersion function on the growing side gives exponential
  growth (for Z strictly inside (-4m^2, 0)); 5.1: the S sector has a real
  zero gamma_0 "slightly smaller than 0", hence growth e^{sqrt|gamma_0| t};
  5.3: gamma_0 ~ -b_0/b_1 = -16 pi G alpha~^S_1 m^4, H = sqrt(-gamma_0), and
  matching Lambda gives m ~ 7.8e-3 eV.  5.2 (TT, alpha~^TT_1 = 0, b_0 = 0):
  "One of the zeros, say gamma_0, is, however, always negative ... the
  magnitude of gamma_0 can be made as small as we want by choosing larger and
  larger positive b_2" (p. 62).
  THEIR OWN ATTRIBUTION (5.2.1)  "This different behaviour is originated by the
  choice of the renormalisation parameters done in Theorem 3.6."

THE DISAGREEMENT, COMPUTED HERE (section 2 of the selftest) -- SCOPED TO WHAT
WAS COMPUTED.  Inside GMMPS's own S-sector dispersion function F_S (5.3), with
J their Stieltjes transform (4.17):

    F_S(0) = -b_0 = 4 alpha~^S_1 m^4 / (6 (1/6 - xi)^2)   -- zero IFF alpha~^S_1 = 0
    gamma_0 = -2 kappa alpha~^S_1 m^4 / (1 + kappa m^2/(288 pi^2)) + O(alpha~^2)

for THE ZERO ON THE BRANCH THROUGH gamma = 0, EXACTLY xi-INDEPENDENT at first
order, J INCLUDED (GMMPS drop J; the J term is the factor
1/(1 + kappa m^2/(288 pi^2)), with J(0) = 1/(96 pi^2 m^2) derived two
independent ways).  By the implicit function theorem, LOCALLY: THAT zero --
GMMPS's reported mode -- exists iff alpha~^S_1 != 0 and grows iff
alpha~^S_1 > 0.  AMM's k^2 = 0 subtraction is the choice that leaves no
k-independent term, i.e. the alpha~^S_1 = 0 case, where gamma = 0 is an exact
root.

OTHER GROWING ROOTS ARE NOT SET BY alpha~^S_1.  At alpha~^S_1 = 0 with b_2 < 0,
F_S still changes sign on the growing side near g* = -b_1/b_2; in the TT
sector (alpha~^TT_1 = 0, b_0 = 0) F_TT changes sign near g* = -b_1/b_2 for
b_2 > 0.  The selftest BRACKETS both at b_2 = -1e100 (S) and +1e100 (TT) --
the control that the "only if" is NOT claimed -- and shows the S bracket
does NOT fire at b_2 = +1e100 (so it can fail).  Their scale is set by the
FREE constants alpha~^S_3 and alpha~^TT_4 through b_2: Planckian for O(1)
values, and arbitrarily far below it otherwise.  Whether anything grows from
the gamma = 0 root at alpha~^S_1 = 0 is OPEN: it lies outside GMMPS Thm 4.16
(Z strictly inside (-4m^2, 0)) and Prop. 4.10 (b_0, b_1, b_2 != 0), and
outside AMM's treated modes (p. 12).  So the literature split is ONE
renormalisation constant FOR GMMPS's REPORTED MODE, NOT for growth in general,
and which value is right is a question about renormalisation conditions (AMM's
k^2 = 0 subtraction against GMMPS's Thm 3.6) that is not adjudicated here.
  WITHDRAWN: "the infrared growing mode EXISTS IFF alpha~^S_1 != 0" as a
  statement about growth in general; "where gamma = 0 is an exact root and
  NOTHING GROWS FROM IT"; "THE LITERATURE SPLIT IS ONE RENORMALISATION
  CONSTANT" (ruling A4.1; verify-stability BLOCKING: other_zeros.py).

Printed discrepancies in GMMPS v1, RECORDED, NOT REPAIRED:
  5.1 prints alpha~^S_1 = (64 pi)^-1 where Thm 3.6 has 1/(64 pi^2).  Their 5.3
      figure m ~ 7.8e-3 eV is reproduced ONLY with 1/(64 pi^2); (64 pi)^-1
      gives a figure the selftest shows is > 20 % off.  So 5.1's is
      typographical.
  Thm 1.2 prints the bound h~ <= e^{-Ht} eta; 1.5 describes it as e^{tH}.
  1.5 says the growth holds "regardless of renormalisation constants"; 5.2.1
      attributes it to Thm 3.6's choice.  The computation above shows the
      branch root vanishes at alpha~^S_1 = 0, and that other growing roots
      remain at a scale set by the free alpha~^S_3 and alpha~^TT_4, Planckian
      for O(1) values.
        WITHDRAWN: "the Planck-scale runaways AMM also record" for those
        roots.  GMMPS's own 5.2 sentence and the bracket say they need not be
        Planck-scale.

===============================================================================
2.  THE CLASSICAL RADIAL SECTOR -- HYPOTHESES, CHECKED AGAINST THE OBJECT
===============================================================================

  P1 Israel/Lanczos thin shell, spherically symmetric.            stability.py
  P2 static vacuum on both sides: Schwarzschild M_in = -m inside
     (f_in = 1 + 2m/R > 0, no horizon), Minkowski outside.         stability.device
  P3 radial (l = 0) perturbations only; the shell's areal radius
     R(tau) is the gauge-invariant scalar.
  P4 barotropic linearised EOS p' = beta^2 sigma', mass evolved by
     m_s' = -8 pi R p (the conservation law stability.py uses).
The theorem is about THAT object.  concentric.py's device has a Plummer core,
whose mass is not all inside R_s: the fraction outside is
1 - (1 + (a/R_s)^2)^(-3/2), computed from concentric.A_CORE and R_SHELL, so P2
holds there only up to that departure and the theorem is NOT claimed for
concentric.py's exact potential.  l >= 1 is stability.py's NOT-RUN list,
unchanged; the core's own stability is deferred with the identification
phase.  stability.py's bisected beta2_crit carries finite-difference error; the
selftest prints its maximum over the three m/R it tests (0.01, 0.1, 0.5) --
a maximum over those points, not over stability.py's range.

===============================================================================
3.  THE ROW THIS OPENS
===============================================================================

    D26  LINEARISED STABILITY (AMM).  OPEN.  Classical radial sector: THEOREM,
    stable for every m > 0 at every beta^2 > beta^2_crit(u) in (-1/4, 0).
    Semiclassical: NOT EVALUABLE AT PRESENT -- AMM's criterion is defined only
    about a solution of (2.9), and no demand configuration is recorded or
    shown to be one; that is O5, OPEN.  D26_STATUS is CHECKED against a status
    derived from the selftest's evidence.
    WOULD BE ANSWERED BY: O5's remaining question (a solution of the
    semiclassical equations with m < 0 in a specified state) and its retarded
    correlator Pi^(ret) there; classically, the l >= 1 modes of the shell.

NOTHING IS REPAIRED.  stability.py, wall.py, throatmass.py, hpscentre.py, AMM
and GMMPS are not edited; the discrepancies are recorded.
"""

import math
import os
import sys

#: This file's own directory -- research/warp-drive wherever the repository is
#: checked out; never an absolute path (DOCKET 64 ruling B1/B4).  It is the
#: ONLY directory this file adds to sys.path, so recovered/struct.py is never
#: reachable from here; _need() checks that the struct in use is the stdlib's.
HERE = os.path.dirname(os.path.abspath(__file__))
TREE = HERE
if TREE not in sys.path:
    sys.path.insert(0, TREE)

import achievable        # noqa: E402  constants
import concentric        # noqa: E402  A_CORE, R_SHELL
import stability         # noqa: E402  the priced shell, finite-difference V''
import throatmass        # noqa: E402  the self-consistent families (READ)
import wall              # noqa: E402  the ordinary shell's closed form
import hpscentre         # noqa: E402  O5, DOCKET 64: m < 0 in HPS's system

# ---------------------------------------------------------------- sources, READ
AMM = ("Anderson, Molina-Paris & Mottola, 'Linear response, validity of "
       "semi-classical gravity, and the stability of flat space', "
       "gr-qc/0209075 v1; PRD 67, 024026 (2003)")
AMM_READ = ("arXiv v1 text layer via alphaXiv: pages 1-16 read (body, "
            "Appendix A to (A23)); Appendix B (spectral-function details) and "
            "the bibliography NOT read")
AMM_CRITERION = ("no solution of (3.4) with finite non-singular initial data for "
                 "which any linearized gauge invariant scalar grows without "
                 "bound (III, p. 10) -- a NECESSARY condition for validity")
AMM_NEEDS_A_SOLUTION = ("(3.3): 'the first variation vanishes by (2.9)'; p. 9: "
                        "the retarded correlator 'is evaluated in the background "
                        "geometry of the leading order solution of the "
                        "semi-classical equations (2.9)'")
AMM_HYPOTHESES = (
    "H1 a background g that SOLVES the renormalised semiclassical eqs (2.9)",
    "H2 the in-state |in> of the (large-N, free) quantum fields in which (2.9) holds",
    "H3 the retarded polarization tensor Pi^(ret) (3.5), (3.9) in that state on g",
    "H4 renormalised Lambda, G_N, alpha, beta, fixed by a stated condition",
    "H5 the allowed gauge transformations (3.11), growing ones decided by (2.7)",
    "H6 (implicit, p. 12) the fourth-order coefficients are O(1): 'cannot be "
    "satisfied except at k^2 approaching G_N^-1' -- where GMMPS's large-b_2 "
    "roots enter",
)
AMM_FLAT_RESULT = ("Minkowski, scalar of any m > 0 and xi, vacuum: no unstable "
                   "or new mode with G|k^2| << 1 in either sector, for O(1) "
                   "fourth-order coefficients (H6).  alpha >= 0 and rho^(T) >= 0 "
                   "are hypotheses of the (4.6) positivity step ONLY: AMM p. 12, "
                   "'If alpha < 0 then the preceding analyses for k^2 > 0 and "
                   "k^2 < 0 interchange roles, with the conclusion unchanged.'  "
                   "Scalar k = 0 global modes NOT treated (p. 12)")
AMM_P12_ALPHA_NEGATIVE = ("If alpha < 0 then the preceding analyses for k^2 > 0 "
                          "and k^2 < 0 interchange roles, with the conclusion "
                          "unchanged.")

GMMPS = ("Galanda, Meda, Murro, Pinamonti & Schmid, 'The semiclassical "
         "Einstein-Klein-Gordon system: asymptotic analysis of Minkowski "
         "spacetime', arXiv:2604.01047 v1")
GMMPS_READ = ("arXiv v1 text layer via alphaXiv get_paper_content(fullText): "
              "body sections 1-5 and appendices A, B read in full; bibliography "
              "read to [67]")
GMMPS_HYPOTHESES = (
    "one real Klein-Gordon field, m > 0, xi with 2/(6 xi - 1) < 4 (5.1)",
    "background (R^4, eta) with the Poincare vacuum, Hadamard (1.2, Prop. 3.1)",
    "past-compact metric and state perturbations of ALL of R^4, forcing problem (1.8)",
    "de Donder gauge, a complete gauge fixing on past-compact sections (Prop. 2.4)",
    "alpha~^S_1 = 1/(64 pi^2), alpha~^TT_1 = 0 by Thm 3.6 (general local covariance "
    "+ perturbative agreement)",
    "alpha~^S_2 = alpha~^TT_2 = 0 assumed (5.1, 5.2)",
)
GMMPS_ALPHA_S1_THM36 = "1/(64 pi^2)"
GMMPS_ALPHA_S1_SEC51 = "(64 pi)^-1"            # printed; typographical (selftest 2)
GMMPS_ATTRIBUTION = ("5.2.1: 'This different behaviour is originated by the "
                     "choice of the renormalisation parameters done in Theorem 3.6'")
GMMPS_PRINTED_MASS_EV = 7.8e-3                   # READ, 5.3
GMMPS_PRINTED_LAMBDA_MP2 = 7.15e-121             # READ, 5.3, in M_P^2
GMMPS_PRINTED_OMEGA_LAMBDA = 0.685               # READ, 5.3

#: The elementary charge is EXACT by the 2019 SI definition; it converts J to eV
#: and is the only constant this file adds to achievable.py's.
E_CHARGE_EXACT = 1.602176634e-19

# ------------------------------------------------------------ what is decided
#: The selftest DERIVES a status from its section-1 proofs and checks this
#: against it; these are the ledger's attributes, not the evidence.
CLASSICAL_RADIAL_STATUS = "THEOREM"
CLASSICAL_RADIAL_STABLE_FOR_ALL_M = True
BETA2_CRIT_INFIMUM = "-1/4"
DEVICE_IS_WALL_FORMULA_AT_U = True   # same V'', same beta^2_crit, s -> u
#: Checked by the selftest against semiclassical_evaluable_on_demand(), which
#: derives it from the scan and the candidate table below.
SEMICLASSICAL_EVALUABLE_ON_DEMAND = False
SEMICLASSICAL_STATUS = ("NOT EVALUABLE AT PRESENT: precondition H1 (a solution "
                        "of AMM (2.9)) is unestablished for every demand "
                        "configuration, pending O5 -- not a proof that none is one")
SEMICLASSICAL_MISSING = ("a state omega on the configuration with <T_ab>_omega^ren "
                         "equal to its semiclassical left side (AMM (2.9)) -- O5 -- "
                         "and then Pi^(ret) in omega on it (AMM (3.5), (3.9))")
FLAT_EXTERIOR_INHERITS_AMM = False     # READ: AMM IV Fourier over all Minkowski
FLAT_EXTERIOR_INHERITS_GMMPS = False   # READ: GMMPS 1.2, Thm 1.2 on (R^4, eta)
#: Reworded under DOCKET 64 (ruling A4.1, B4; verify-stability BLOCKING).
LITERATURE_SPLIT_IS_ONE_CONSTANT = (
    "FOR GMMPS's REPORTED MODE ONLY: the S-sector zero on the branch through "
    "gamma = 0 exists iff alpha~^S_1 != 0 and grows iff alpha~^S_1 > 0 (locally, "
    "implicit function theorem).  NOT for growth in general: other growing roots "
    "sit near -b_1/b_2 at a scale set by the free alpha~^S_3 and alpha~^TT_4, "
    "Planckian only for O(1) values")
#: At alpha~^S_1 = 0, gamma = 0 is a root of F_S; whether anything grows from
#: it lies outside GMMPS Thm 4.16 and Prop. 4.10 and AMM's treated modes.
ALPHA_ZERO_ROOT_GROWTH = "OPEN"
SPLIT_ADJUDICATED_HERE = False
NOTHING_IS_REPAIRED = True

D26_STATUS = "OPEN"
D26_CLAIM = ("LINEARISED STABILITY (AMM).  Classical radial sector of stability.py's "
             "shell: THEOREM under P1-P4, stable for every m > 0 at every beta^2 > "
             "beta^2_crit(u) = -(u-1)(3u^2+2u+1)/(4u^2(3u+1)) in (-1/4, 0), "
             "u = sqrt(1+2m/R) -- wall.py's closed form for the ordinary shell "
             "with s = sqrt(1-2M/R) < 1 replaced by u > 1.  "
             "Semiclassical: NOT EVALUABLE AT PRESENT -- AMM's criterion is "
             "defined only about a solution of the semiclassical equations (2.9) "
             "(AMM pp. 8-9), and none of the demand configurations is recorded "
             "or shown to be one; that is O5, OPEN.  GMMPS's reported Minkowski "
             "mode (the S-sector zero on the branch through gamma = 0) exists, "
             "locally by the implicit function theorem, iff "
             "alpha~^S_1 != 0; other growing roots are set by the free "
             "fourth-order constants; the split is not adjudicated")
D26_ANSWERED_BY = ("O5's remaining question -- a solution of the semiclassical "
                   "equations with m < 0 in a specified state -- and its retarded "
                   "correlator Pi^(ret) there; classically, the l >= 1 modes of "
                   "the shell (stability.py's NOT-RUN list)")

#: The demand owners are NOT typed: demand_owners() reads them from
#: ledger.DEMAND's owner column at run time.  DEVICE_FILES own no ledger row
#: but are the device's own files, so they are scanned in addition, by name.
DEVICE_FILES = ("axial", "concentric", "stability")
#: Widened on the verifier's search (it found 'backreact' in tolman.py).
SELF_CONSISTENCY_TOKENS = ("semiclassical", "semi-classical", "self-consistent",
                           "self consistent", "selfconsistent", "backreact",
                           "back-react", "back reaction")
#: Files that DO hold self-consistent semiclassical solutions: the scan must
#: find tokens in them, or it is blind.
POSITIVE_CONTROLS = ("throatmass", "hpscentre")
#: A token is a weak proxy for "claims a solution of (2.9)", so every scanned
#: owner WITH hits was READ, and what the hits say is recorded here.  The
#: selftest requires the set of owners with hits to EQUAL this set's keys: an
#: owner that gains tokens without being read turns it red.
READ_HITS = {
    # D22 was re-owned from fluctuation.py to noise.py by DOCKET 64; demand_owners()
    # reads the ledger at run time, so the READ set follows the board, not a list.
    "noise": "D22's owner since DOCKET 64: line ~144 'lets the semiclassical "
             "equation carry blackbody radiation' -- a flat-space thermal remark "
             "on the smeared fluctuation; claims no solution of (2.9)",
    "tolman": "'backreaction bound' (a magnitude bound) and, line ~947, 'STABILITY, "
              "DYNAMICS OR BACKREACTION. The identity is kinematic.' -- disclaims it",
    "excite": "'a self-consistent fermion bag' listed among DOCKET 63's OPEN "
              "questions; claims none",
    "latticectc": "H3: branes are TEST hypersurfaces 'carrying no back-reaction' "
                  "-- disclaims it",
    # massform.py became a DEMAND owner (D27-D29) when DOCKET 65 was seated.
    # Its three hits were READ: every one is 'semiclassical' in the INSTANTON /
    # WKB sense of electroweak B + L violation, nothing about gravity.
    "massform": "D27-D29's owner since DOCKET 65: three 'semiclassical' hits, "
                "each the electroweak instanton/sphaleron sense -- the docstring's "
                "and S11's 'prevalent semiclassical results find it exponentially "
                "suppressed' (collider B + L rate, CONTESTED) and a quoted source "
                "text, 'suppressed by the semiclassical exponent exp(-4 pi / "
                "alpha_W)' (Rubakov & Shaposhnikov) -- a tunnelling estimate, not "
                "semiclassical gravity; claims no solution of (2.9)",
}
#: What this file READ about hpscentre.py's m < 0 solutions against AMM's
#: H1-H3.  Everything else candidates() ASKS of the peers at run time.
HPS_SOLVES_AMM_2_9_IN_A_SPECIFIED_STATE = False
HPS_HAS_PI_RET = False
HPS_READ_REASON = ("solves G = 8 pi <T> with <T> the AHS APPROXIMATION, not the "
                   "renormalised <T_ab> of a specified state (AMM (2.9)); no "
                   "Pi^(ret) exists for it; and it lies outside the domain the "
                   "approximation is established in (hpscentre.DOMAIN_WORD)")


def candidates():
    """The tree's self-consistent semiclassical solutions, as candidates for
    AMM's H1-H3 on a DEMAND configuration (which needs m < 0, D1).  Asked of
    the owners: throatmass.py's READ families (m < 0 reported: the family
    table's own column) and hpscentre.py's flags."""
    tm = throatmass.SELF_CONSISTENT_FAMILIES
    return (
        dict(name="throatmass: %d reported families" % len(tm),
             m_negative=any(bool(f[4]) for f in tm), inside_domain=None,
             solves_2_9_in_state=None, pi_ret=None,
             reason="m < 0 reported in none (throatmass.NEGATIVE_MASS_SELF_"
                    "CONSISTENT_FOUND = %s)" % throatmass.NEGATIVE_MASS_SELF_CONSISTENT_FOUND),
        dict(name="hpscentre: HPS's system, conserved reading",
             m_negative=hpscentre.M_NEGATIVE_FOUND_IN_HPS_SYSTEM,
             inside_domain=hpscentre.M_NEGATIVE_FOUND_INSIDE_DOMAIN,
             solves_2_9_in_state=HPS_SOLVES_AMM_2_9_IN_A_SPECIFIED_STATE,
             pi_ret=HPS_HAS_PI_RET, reason=HPS_READ_REASON),
    )


#: Kept, never deleted: every claim DOCKET 64 withdrew from this line, with why.
WITHDRAWN = (
    ("'the infrared growing mode EXISTS IFF alpha~^S_1 != 0' (growth in general)",
     "only the branch root through gamma = 0 is controlled by alpha~^S_1; roots "
     "near -b_1/b_2 grow at alpha~^S_1 = 0 (S, b_2 < 0) and in TT (b_2 > 0) -- "
     "bracketed in the selftest"),
    ("'where gamma = 0 is an exact root and NOTHING GROWS FROM IT'",
     "outside GMMPS Thm 4.16, Prop. 4.10 and AMM's treated modes: OPEN"),
    ("'THE LITERATURE SPLIT IS ONE RENORMALISATION CONSTANT'",
     "true for GMMPS's reported mode only"),
    ("'the Planck-scale runaways AMM also record'",
     "their scale is set by the free alpha~^S_3, alpha~^TT_4; Planckian for O(1) "
     "values only (GMMPS 5.2, p. 62)"),
    ("'NO -- AND THE OBSTRUCTION IS PROVED'; 'none of the demand configurations "
     "is one'", "a scan of the tree: none is RECORDED OR SHOWN to be one; H1 "
     "unestablished pending O5"),
    ("'the only self-consistent solutions the tree holds ... all have m >= 0'",
     "stale once hpscentre.py is seated: m < 0 in HPS's system, outside the "
     "established domain, not a solution of AMM (2.9) in a specified state"),
    ("AMM_FLAT_RESULT: 'tensor sector needs alpha >= 0'",
     "a hypothesis of the (4.6) step only (AMM p. 12)"),
    ("'every beta^2 >= 0 -- dust included --'",
     "beta^2 = 0 is no pressure response; the shell carries a tension"),
    ("DEMAND_OWNERS as a typed list of 'the nine demand owners'",
     "hand-picked, not the ledger's demand column; now read from ledger.DEMAND"),
)


def _need():
    try:
        import sympy as sp
        import z3
        import mpmath as mp
    except ImportError as exc:                       # pragma: no cover
        raise SystemExit("linstab.py needs sympy, z3 and mpmath: %s" % exc)
    import struct
    if "recovered" in (getattr(struct, "__file__", "") or "").split(os.sep):
        raise SystemExit("linstab.py: struct resolves to %s, not the stdlib -- "
                         "run from a directory that does not see recovered/"
                         % struct.__file__)
    return sp, z3, mp


def prove(z3, hyps, goal):
    s = z3.Solver()
    s.add(*hyps)
    s.add(z3.Not(goal))
    return s.check() == z3.unsat


def poly_z3(sp, expr, sym, Z):
    """A polynomial in sym, rebuilt term by term as a z3 expression in Z."""
    P = sp.Poly(sp.expand(expr), sym)
    if not all(c.is_Integer for c in P.coeffs()):
        raise ValueError("poly_z3 takes integer coefficients only")
    return sum(int(c) * Z ** int(k[0]) for k, c in P.terms())


def sat(z3, cons):
    s = z3.Solver()
    s.add(*cons)
    return s.check() == z3.sat


# ================================================= 1. classical radial sector
def poisson_visser(sp):
    """V(R) and its exact first two derivatives at the static shell, with the
    shell mass evolved by m_s' = -8 pi R p and p' = beta^2 sigma'."""
    R, ms, Mi, Mo, b2 = sp.symbols('R m_s M_in M_out beta2', real=True)
    V = 1 - 2 * Mo / R - ((Mo - Mi) / ms - ms / (2 * R)) ** 2
    fi, fo = 1 - 2 * Mi / R, 1 - 2 * Mo / R
    ms0 = R * (sp.sqrt(fi) - sp.sqrt(fo))
    sig0 = ms0 / (4 * sp.pi * R ** 2)
    p0 = (1 / (8 * sp.pi * R)) * ((1 - Mo / R) / sp.sqrt(fo) - (1 - Mi / R) / sp.sqrt(fi))
    m1 = -8 * sp.pi * R * p0
    m2 = -8 * sp.pi * p0 + 16 * sp.pi * b2 * (sig0 + p0)   # sigma' = -2(sigma+p)/R
    V1 = sp.diff(V, R) + sp.diff(V, ms) * m1
    V2 = (sp.diff(V, R, 2) + 2 * sp.diff(V, R, ms) * m1
          + sp.diff(V, ms, 2) * m1 ** 2 + sp.diff(V, ms) * m2)
    sub = {ms: ms0}
    return dict(R=R, Mi=Mi, Mo=Mo, b2=b2, V0=V.subs(sub), V1=V1.subs(sub),
                V2=V2.subs(sub), sig0=sig0, p0=p0)


def device_closed_form(sp):
    """(V'' at R = 1, beta^2_crit) for M_in = -m, M_out = 0, in u = sqrt(1+2m)."""
    pv = poisson_visser(sp)
    u = sp.Symbol('u', positive=True)
    v2 = sp.factor(sp.simplify(pv['V2'].subs({pv['Mi']: -(u ** 2 - 1) / 2,
                                               pv['Mo']: 0, pv['R']: 1})))
    bc = sp.solve(sp.Eq(v2, 0), pv['b2'])
    return u, pv['b2'], v2, sp.factor(sp.simplify(bc[0])), pv


def ordinary_closed_form(sp):
    """The same machinery on wall.py's ordinary shell, in s = sqrt(1 - 2M)."""
    pv = poisson_visser(sp)
    s = sp.Symbol('s', positive=True)
    v2 = sp.factor(sp.simplify(pv['V2'].subs({pv['Mi']: 0,
                                               pv['Mo']: (1 - s ** 2) / 2, pv['R']: 1})))
    bc = sp.solve(sp.Eq(v2, 0), pv['b2'])
    return s, v2, sp.factor(sp.simplify(bc[0]))


def plummer_mass_outside(sp, a=None, Rs=None):
    """Fraction of a Plummer core's mass outside radius Rs: 1 - (1+(a/Rs)^2)^(-3/2)."""
    a = sp.nsimplify(concentric.A_CORE if a is None else a)
    Rs = sp.nsimplify(concentric.R_SHELL if Rs is None else Rs)
    return 1 - (1 + (a / Rs) ** 2) ** sp.Rational(-3, 2)


# ========================================================= 2. the literature
def amm_tensor_sector(z3):
    """AMM (4.5a)/(4.6): with alpha >= 0, G > 0, k^2 > 0 and the spectral
    integral I >= 0 (rho^(T) >= 0), the bracket 2 alpha k^2 + 1/(8 pi G) +
    k^4 I is > 0, so no k^2 > 0 (imaginary-frequency) root.  Control: with
    alpha < 0 the positivity STEP fails (a root exists).  alpha >= 0 is that
    step's hypothesis only: AMM p. 12 swap the k^2 > 0 and k^2 < 0 analyses
    for alpha < 0, "with the conclusion unchanged" (AMM_P12_ALPHA_NEGATIVE)."""
    al, G, k2, I, pi = z3.Reals('alpha G k2 I pi')
    br = 2 * al * k2 + 1 / (8 * pi * G) + k2 * k2 * I
    hyp = [pi > 3, pi < 4, G > 0, k2 > 0, I >= 0]
    stable = prove(z3, hyp + [al >= 0], br > 0)
    root_if_negative_alpha = sat(z3, hyp + [al < 0, I == 0, br == 0])
    return stable, root_if_negative_alpha


def gmmps_s_sector(sp):
    """GMMPS (5.2)-(5.3): b_0, b_1, a; F_S; the first-order root and its sign."""
    m, kap, al, xi, g, b2 = sp.symbols('m kappa alpha xi gamma b_2', real=True)
    c = 6 * (sp.Rational(1, 6) - xi) ** 2
    b0 = -al * 4 * m ** 4 / c
    b1 = -(2 / kap) / c
    a = 2 * m ** 2 / (6 * xi - 1)
    Msym = sp.Symbol('M', positive=True)
    mp_ = sp.Symbol('mpos', positive=True)
    rho = sp.sqrt(1 - 4 * mp_ ** 2 / Msym) / (16 * sp.pi ** 2 * Msym)      # (4.5)
    J0 = sp.simplify(sp.integrate(rho / Msym, (Msym, 4 * mp_ ** 2, sp.oo)))
    zz = sp.Symbol('zz')
    J417 = (1 / (8 * sp.pi ** 2)) * (1 / zz - (4 * mp_ ** 2 - zz) * mp_
                                     * sp.acsc(2 * mp_ / sp.sqrt(zz))
                                     / (mp_ * sp.sqrt(4 * mp_ ** 2 - zz) * zz ** sp.Rational(3, 2)))
    J0_417 = sp.simplify(sp.limit(J417, zz, 0, '+'))
    J0m = J0.subs(mp_, m)
    # F_S(gamma) linearised at 0: F_S(0) = -b0, F_S'(0) = a^2 J(0) - b1
    F0 = -b0
    F1 = a ** 2 * J0m - b1
    gam_first = sp.simplify(-F0 / F1)
    target = -2 * kap * al * m ** 4 / (1 + kap * m ** 2 / (288 * sp.pi ** 2))
    return dict(m=m, kap=kap, al=al, xi=xi, b0=b0, b1=b1, a=a, c=c,
                ratio=sp.simplify(-b0 / b1), J0=J0, J0_417=J0_417, J417=J417,
                mpos=mp_, rho=rho, F0=F0, F1=F1, gam_first=gam_first,
                first_minus_target=sp.simplify(gam_first - target),
                slope=sp.simplify(sp.diff(gam_first, al).subs(al, 0)),
                F1_positive_form=sp.simplify(F1 * (1 - 6 * xi) ** 2 * kap))


def dispersion_identity(sp):
    """GMMPS: F_S(gamma) (5.3) against Q(w^2) (4.30) with a1 = a2 = a:
    F_S(-w^2) + Q(w^2) must vanish identically, J an unspecified function."""
    w2, a, b0, b1, b2 = sp.symbols('w2 a b0 b1 b2')
    J = sp.Function('J')
    Q = w2 * (w2 + a) * (w2 + a) * J(-w2) + b0 - b1 * w2 + b2 * w2 ** 2
    gam = sp.Symbol('gamma')
    FS = gam * (a - gam) ** 2 * J(gam) - (b0 + b1 * gam + b2 * gam ** 2)
    return sp.simplify(FS.subs(gam, -w2) + Q)


def J_numeric(mp, g, m=1):
    """J(gamma) = INT_{4m^2}^inf rho(M)/(M - gamma) dM, rho from GMMPS (4.5)."""
    f = lambda M: mp.sqrt(1 - 4 * m ** 2 / M) / (16 * mp.pi ** 2 * M) / (M - g)
    return mp.quad(f, [4 * m ** 2, 8 * m ** 2, mp.inf])


def J_closed(mp, g, m=1):
    """GMMPS (4.17), as printed, evaluated in complex arithmetic."""
    g = mp.mpc(g)
    return (1 / (8 * mp.pi ** 2)) * (1 / g - mp.sqrt(4 * m ** 2 - g)
                                     * mp.acsc(2 * m / mp.sqrt(g)) / g ** mp.mpf(1.5))


def reduced_planck_ev():
    """sqrt(hbar c / 8 pi G) c^2 in eV, from achievable.py's constants."""
    kg = math.sqrt(achievable.HBAR * achievable.C_SI / (8 * math.pi * achievable.G_SI))
    return kg * achievable.C_SI ** 2 / E_CHARGE_EXACT


def gmmps_mass_ev(alpha_s1):
    """Invert GMMPS 5.3, Lambda = 6 Omega alpha (m/M_P)^4 M_P^2, for m in eV."""
    x4 = GMMPS_PRINTED_LAMBDA_MP2 / (6.0 * GMMPS_PRINTED_OMEGA_LAMBDA * alpha_s1)
    return x4 ** 0.25 * reduced_planck_ev(), x4 ** 0.5       # (m in eV, eps = (m/M_P)^2)


def s_root_bracket(mp, eps, xi, B, alpha=None):
    """At GMMPS's own point (m = 1 units, kappa = eps), bound F_S at gamma_lin/2
    and 2 gamma_lin over |b_2| <= B and over J in [4 J(0)/(4+|gamma|), J(0)]
    (J is monotone and M/(M+|g|) >= 4/(4+|g|) for M >= 4).  Returns
    (min F_S at gamma_lin/2, max F_S at 2 gamma_lin); a root lies between
    if the first is > 0 and the second < 0 (F_S is continuous there)."""
    mp.mp.dps = 150
    al = mp.mpf(1) / (64 * mp.pi ** 2) if alpha is None else mp.mpf(alpha)
    eps, xi, B = mp.mpf(eps), mp.mpf(xi), mp.mpf(B)
    c = 6 * (mp.mpf(1) / 6 - xi) ** 2
    b0, b1, a = -al * 4 / c, -(2 / eps) / c, 2 / (6 * xi - 1)
    J0 = 1 / (96 * mp.pi ** 2)
    glin = -2 * eps * al / (1 + eps / (288 * mp.pi ** 2))

    def extremes(gm):
        vals = []
        for J in (J0 * 4 / (4 + abs(gm)), J0):
            for bb in (-B, B):
                vals.append(gm * (a - gm) ** 2 * J - b0 - b1 * gm - bb * gm ** 2)
        return min(vals), max(vals)

    lo_half, _ = extremes(glin / 2)
    _, hi_two = extremes(2 * glin)
    return lo_half, hi_two, glin


# ============================================== 3. the obstruction, witnessed
def off_solution_witnesses(sp):
    """A boundedness verdict computed ABOUT A NON-SOLUTION is not a property of
    the dynamics, in either direction.  x' = f(x) at x0 with f(x0) != 0:
    linearised  d' = f'(x0) d + f(x0)  (the residual kept), or d' = f'(x0) d
    (dropped).  Returns the verdicts against the exact flows, and the controls
    at true equilibria, where the verdict must agree with the flow."""
    t = sp.Symbol('t', nonnegative=True)
    x = sp.Function('x')
    d = sp.Function('d')
    out = {}
    # W1: logistic, x0 = 1/2.  True flow bounded; residual-kept verdict unbounded.
    f1 = lambda y: y * (1 - y)
    X1 = 1 / (1 + sp.exp(-t))
    out['W1_true_solves'] = sp.simplify(sp.diff(X1, t) - f1(X1)) == 0 and X1.subs(t, 0) == sp.Rational(1, 2)
    out['W1_true_bounded'] = (sp.limit(X1, t, sp.oo) == 1)
    y = sp.Symbol('y')
    fp = sp.diff(f1(y), y).subs(y, sp.Rational(1, 2))
    r = f1(sp.Rational(1, 2))
    sol = sp.dsolve(sp.Eq(d(t).diff(t), fp * d(t) + r), d(t), ics={d(0): 0}).rhs
    out['W1_kept_verdict_unbounded'] = sp.limit(sol, t, sp.oo) == sp.oo
    out['W1_residual'] = r
    # W2: x' = 1/(1+x^2), x0 = 1.  True flow unbounded; both verdicts bounded.
    f2 = lambda y_: 1 / (1 + y_ ** 2)
    xs = sp.Symbol('xs', positive=True)
    implicit = xs + xs ** 3 / 3 - sp.Rational(4, 3)       # = t on the true flow
    out['W2_implicit_solves'] = sp.simplify(1 / sp.diff(implicit, xs) - f2(xs)) == 0
    out['W2_true_unbounded'] = sp.limit(implicit, xs, sp.oo) == sp.oo   # t -> oo as x -> oo, x monotone
    out['W2_flow_increasing'] = bool(f2(xs).is_positive)
    fp2 = sp.diff(f2(y), y).subs(y, 1)
    r2 = f2(sp.Integer(1))
    solk = sp.dsolve(sp.Eq(d(t).diff(t), fp2 * d(t) + r2), d(t), ics={d(0): 0}).rhs
    sold = sp.dsolve(sp.Eq(d(t).diff(t), fp2 * d(t)), d(t), ics={d(0): 1}).rhs
    out['W2_kept_verdict_bounded'] = sp.limit(solk, t, sp.oo) == 1
    out['W2_dropped_verdict_decays'] = sp.limit(sold, t, sp.oo) == 0
    out['W2_residual'] = r2
    # CONTROLS: at equilibria the linearised verdict must match the flow.
    out['C1_x1_stable'] = sp.diff(f1(y), y).subs(y, 1) < 0          # flow -> 1: W1
    out['C0_x0_unstable'] = sp.diff(f1(y), y).subs(y, 0) > 0        # flow leaves 0
    out['C_residual_zero_at_equilibria'] = (f1(sp.Integer(0)), f1(sp.Integer(1)))
    return out


def self_consistency_scan(names):
    """Case-insensitive count of SELF_CONSISTENCY_TOKENS in each owner's source."""
    out = {}
    for n in names:
        with open(os.path.join(TREE, n + ".py"), encoding="utf-8") as fh:
            src = fh.read().lower()
        out[n] = sum(src.count(tk) for tk in SELF_CONSISTENCY_TOKENS)
    return out


def demand_owners():
    """The ledger's demand column, READ at run time (never typed): every module
    named as a DEMAND row's owner, in row order, this file excluded; and the
    rows whose owner is a paper (attribute None), which no scan can reach.
    ledger.py imports this file, so it is imported here only inside a call."""
    import ledger
    mods, paper_rows = [], []
    for row in ledger.DEMAND:
        owner = row[3]
        if owner is None:
            paper_rows.append(row[0])
        elif owner[0] != "linstab" and owner[0] not in mods:
            mods.append(owner[0])
    return tuple(mods), tuple(paper_rows)


def demand_semiclassical_solutions():
    """Candidates that would make AMM's criterion evaluable on a DEMAND
    configuration: m < 0 (D1), a solution of (2.9) in a specified state, and
    Pi^(ret) there -- all three, asked of candidates()."""
    return [c for c in candidates()
            if c['m_negative'] and c['solves_2_9_in_state'] and c['pi_ret']]


def semiclassical_evaluable_on_demand(scan, owners):
    """DERIVED, never typed: evaluable iff some candidate satisfies H1-H3 with
    m < 0.  Returns (verdict, owners with UNREAD token hits) -- an unread hit
    means the scan has not been read, and the verdict is then not trusted."""
    unread = [n for n in owners if scan[n] > 0 and n not in READ_HITS]
    return bool(demand_semiclassical_solutions()), unread


def b2_root_bracket(mp, eps, sector, b2, xi=0):
    """GMMPS's dispersion functions at their own point (m = 1, kappa = eps), with
    the LEADING constant switched off -- alpha~^S_1 = 0 (S: b_0 = 0) or Thm
    3.6's alpha~^TT_1 = 0 (TT: b_0 = 0, a = 4, b_1 = 60/kappa, (5.4)) -- and
    b_2 given.  Bounds F at g*/2 and 2 g*, g* = -|b_1/b_2|, over J in
    [4 J(0)/(4 + |g|), J(0)] (J monotone, rho >= 0 on M >= 4).  Returns
    (lo, hi at g*/2), (lo, hi at 2 g*), g*: a GROWING root (g < 0) lies
    between when the two intervals exclude 0 with opposite signs."""
    mp.mp.dps = 150
    eps, xi, b2 = mp.mpf(eps), mp.mpf(xi), mp.mpf(b2)
    J0 = 1 / (96 * mp.pi ** 2)
    if sector == "S":
        c = 6 * (mp.mpf(1) / 6 - xi) ** 2
        a, b0, b1 = 2 / (6 * xi - 1), mp.mpf(0), -(2 / eps) / c
        F = lambda g, J: g * (a - g) ** 2 * J - b0 - b1 * g - b2 * g ** 2   # (5.3)
    else:
        a, b1 = mp.mpf(4), 60 / eps
        F = lambda g, J: g * (a - g) ** 2 * J - g * (b1 + b2 * g)           # (5.4)
    gs = -abs(b1 / b2)          # always on the GROWING side (g < 0), as -b_1/b_2 is
                                #   in both firing cases; for S at b_2 > 0 this puts
                                #   the probe where no root is (the control)

    def rng(g):
        v = [F(g, J) for J in (J0 * 4 / (4 + abs(g)), J0)]
        return min(v), max(v)
    return rng(gs / 2), rng(2 * gs), gs


def bracket_fires(half, two, gs):
    """A growing root is bracketed: g* < 0 and F keeps one strict sign on each
    interval end, opposite at the two ends."""
    return bool(gs < 0 and ((half[0] > 0 and two[1] < 0) or (half[1] < 0 and two[0] > 0)))


# ================================================================== report
def report():
    sp, z3, mp = _need()
    print(__doc__.split("=====", 1)[0].strip())
    u, b2, v2, bc, _pv = device_closed_form(sp)
    print("\nCLASSICAL RADIAL SECTOR (stability.py's shell, R = 1)")
    print("  V''(R_0)       = %s" % v2)
    print("  beta^2_crit(u) = %s" % bc)
    print("  %8s %14s %14s %14s" % ("m/R", "V''(beta2=0)", "beta2_crit", "stability.py FD"))
    for m in (0.01, 0.1, 0.5, 1.0, 2.0):
        uu = sp.sqrt(1 + 2 * sp.nsimplify(m))
        print("  %8.2f %+14.6e %+14.6f %+14.6e" % (
            m, float(v2.subs({b2: 0, u: uu})), float(bc.subs(u, uu)),
            stability.V_second(*stability.device(m), beta2=0.0)))
    print("  infimum of beta^2_crit over m > 0: %s" % sp.limit(bc, u, sp.oo))
    print("\nTHE LITERATURE SPLIT, IN GMMPS's OWN S SECTOR")
    g = gmmps_s_sector(sp)
    print("  -b0/b1          = %s   (GMMPS 5.3: -16 pi G alpha m^4 = -2 kappa alpha m^4)" % g['ratio'])
    print("  J(0)            = %s  (4.5 integral)  = %s (4.17 limit, m=1)" % (g['J0'], g['J0_417']))
    print("  gamma_0 (1st)   = %s   (the zero on the branch through gamma = 0 ONLY)" % g["gam_first"])
    m_ev, eps = gmmps_mass_ev(1 / (64 * math.pi ** 2))
    m_ev_typo, _ = gmmps_mass_ev(1 / (64 * math.pi))
    print("  m from 5.3 with alpha = 1/(64 pi^2): %.4e eV (printed 7.8e-3); "
          "with (64 pi)^-1: %.4e eV" % (m_ev, m_ev_typo))
    lo, hi, glin = s_root_bracket(mp, eps, 0, 10 ** 100)
    print("  at that m (xi = 0, |b_2| <= 1e100): F_S(g/2) >= %s > 0 > %s >= F_S(2g),"
          " g = %s m^2" % (mp.nstr(lo, 6), mp.nstr(hi, 6), mp.nstr(glin, 6)))
    print("  THE BRANCH ROOT ONLY.  Other growing roots at the leading constant = 0:")
    for sector, bb in (("S", -10 ** 100), ("TT", 10 ** 100), ("S", 10 ** 100)):
        half, two, gs = b2_root_bracket(mp, eps, sector, bb)
        print("    %-2s b_2 = %+.0e: F(g*/2) in [%s, %s], F(2g*) in [%s, %s], g* = %s m^2 -> %s"
              % (sector, bb, mp.nstr(half[0], 4), mp.nstr(half[1], 4), mp.nstr(two[0], 4),
                 mp.nstr(two[1], 4), mp.nstr(gs, 5),
                 "GROWING ROOT BRACKETED" if bracket_fires(half, two, gs) else "no bracket"))
    print("  LITERATURE_SPLIT_IS_ONE_CONSTANT: %s" % LITERATURE_SPLIT_IS_ONE_CONSTANT)
    print("\nTHE SEMICLASSICAL CRITERION ON THE DEMAND COLUMN")
    owners, paper_rows = demand_owners()
    names = owners + DEVICE_FILES + POSITIVE_CONTROLS
    scan = self_consistency_scan(names)
    for n in names:
        tag = ("   (positive control)" if n in POSITIVE_CONTROLS else
               "   (device file, no ledger row)" if n in DEVICE_FILES else "")
        print("  %-14s self-consistency tokens: %d%s%s" % (
            n, scan[n], tag, ("   READ: " + READ_HITS[n]) if n in READ_HITS else ""))
    print("  demand rows owned by a paper, not scannable: %s" % ", ".join(paper_rows))
    for c in candidates():
        print("  candidate %-44s m<0 %s; (2.9) in a state %s; Pi^ret %s -- %s"
              % (c['name'], c['m_negative'], c['solves_2_9_in_state'], c['pi_ret'], c['reason']))
    ev, unread = semiclassical_evaluable_on_demand(scan, owners + DEVICE_FILES)
    print("  EVALUABLE (derived): %s; unread hits: %s.  %s" % (ev, unread or "none", SEMICLASSICAL_STATUS))
    print("  MISSING: %s" % SEMICLASSICAL_MISSING)
    print("\nWITHDRAWN (kept, with why):")
    for claim, why in WITHDRAWN:
        print("  - %s\n      %s" % (claim, why))
    print("\nPROPOSED ROW  D26  %s\n  %s\n  WOULD BE ANSWERED BY: %s"
          % (D26_STATUS, D26_CLAIM, D26_ANSWERED_BY))
    return 0


# ================================================================ selftest
def selftest():
    sp, z3, mp = _need()
    fails = []
    passed = []
    records = []

    def chk(label, got, want):
        good = got == want
        print("  [%s] %-66s %s" % ("ok" if good else "XX", label,
                                   got if good else "%s != %s" % (got, want)))
        (passed if good else fails).append(label)
        return good

    def near(label, got, want, tol):
        d = abs(got - want) / max(1e-300, abs(want))
        good = d <= tol
        print("  [%s] %-66s %.10g (rel %.1e)" % ("ok" if good else "XX", label, got, d))
        (passed if good else fails).append(label)
        return good

    def record(label, value):
        """A RECORD PIN: a READ or ruled value, printed and NOT counted as a
        check -- it compares nothing computed, so it cannot fail."""
        records.append(label)
        print("  [RECORD] %-62s %s" % (label, value))

    print("linstab.py --selftest\n")
    print("1. THE CLASSICAL RADIAL SECTOR, EXACT")
    theorem = []          # the checks the THEOREM status is derived from
    pv = poisson_visser(sp)
    for lab, sub in (("device m=1/10", {pv['Mi']: -sp.Rational(1, 10), pv['Mo']: 0}),
                     ("ordinary M=1/10", {pv['Mi']: 0, pv['Mo']: sp.Rational(1, 10)})):
        theorem.append(chk("V(R_0) = 0 identically, %s" % lab, sp.simplify(pv['V0'].subs(sub)), 0))
        theorem.append(chk("V'(R_0) = 0 identically in beta^2, %s" % lab,
                           sp.simplify(pv['V1'].subs(sub)), 0))
    u, b2, v2, bc, _ = device_closed_form(sp)
    s, v2o, bco = ordinary_closed_form(sp)
    wallform = (1 - s) * (3 * s ** 2 + 2 * s + 1) / (4 * s ** 2 * (1 + 3 * s))
    chk("CONTROL: same machinery reproduces wall.py's closed form exactly",
        sp.simplify(bco - wallform), 0)
    for x in (0.1, 0.3, 2 / 3):
        near("  ... and wall.beta2_crit(%.4f) numerically" % x,
             float(bco.subs(s, sp.sqrt(1 - sp.nsimplify(x)))), wall.beta2_crit(x), 1e-12)
    theorem.append(chk("device beta2_crit = -(u-1)(3u^2+2u+1)/(4u^2(3u+1))",
                       sp.simplify(bc + (u - 1) * (3 * u ** 2 + 2 * u + 1)
                                   / (4 * u ** 2 * (3 * u + 1))), 0))
    same = [chk("SAME FUNCTION: V''_device(u) == V''_ordinary(s -> u)",
                sp.simplify(v2 - v2o.subs(s, u)), 0),
            chk("SAME FUNCTION: beta2_crit_device(u) == beta2_crit_wall(s -> u)",
                sp.simplify(bc - wallform.subs(s, u)), 0)]
    chk("  DEVICE_IS_WALL_FORMULA_AT_U agrees with the two identities",
        DEVICE_IS_WALL_FORMULA_AT_U, all(same))
    fd_err = []
    for m in (0.01, 0.1, 0.5):
        uu = sp.sqrt(1 + 2 * sp.nsimplify(m))
        near("CONTROL: exact V''(0) at m/R=%.2f vs stability.py's FD" % m,
             float(v2.subs({b2: 0, u: uu})),
             stability.V_second(*stability.device(m), beta2=0.0), 1e-4)
        ex = float(bc.subs(u, uu))
        fd = stability.beta2_crit(*stability.device(m))
        fd_err.append(abs(fd - ex) / abs(ex))
        near("  and exact beta2_crit vs stability.py's FD bisection (FD error)", ex, fd, 1e-3)
    print("  [info] stability.py FD beta2_crit error: max %.2e relative over m/R in "
          "{0.01, 0.1, 0.5} -- a maximum over THOSE points only" % max(fd_err))
    near("CONTROL: exact ordinary V''(0) at M/R=0.01 vs stability.py's FD (-3.036e-2)",
         float(v2o.subs({pv['b2']: 0, s: sp.sqrt(sp.Rational(98, 100))})),
         stability.V_second(*stability.ordinary(0.01), beta2=0.0), 1e-4)
    U, B = z3.Reals('u b')
    num = (U - 1) * (3 * U * U + 2 * U + 1)
    den = 4 * U * U * (3 * U + 1)
    theorem.append(chk("z3: beta2_crit < 0 for EVERY u > 1 (every m > 0)",
                       prove(z3, [U > 1, B * den == -num], B < 0), True))
    theorem.append(chk("z3: beta2_crit > -1/4 for every u > 1",
                       prove(z3, [U > 1, B * den == -num], B > -sp.Rational(1, 4)), True))
    chk("z3 CONTROL: the SAME formula on 0 < s < 1 (wall) is > 0, not < 0",
        (prove(z3, [U > 0, U < 1, B * den == -num], B > 0),
         sat(z3, [U > 0, U < 1, B * den == -num, B < 0])), (True, False))
    theorem.append(chk("infimum is exactly -1/4 (u -> oo) = BETA2_CRIT_INFIMUM",
                       sp.limit(bc, u, sp.oo), sp.Rational(BETA2_CRIT_INFIMUM)))
    dnum, dden = sp.fraction(sp.together(sp.diff(bc, u)))
    theorem.append(chk("beta2_crit strictly decreasing: numerator and denominator of d/du (z3)",
                       (prove(z3, [U > 1], poly_z3(sp, dnum, u, U) < 0),
                        prove(z3, [U > 1], poly_z3(sp, dden, u, U) > 0)), (True, True)))
    theorem.append(chk("V''(beta^2 = 0) > 0 for every u > 1 (z3): beta^2 = 0 (no pressure "
                       "response) stable", prove(z3, [U > 1], (U - 1) * (3 * U * U + 2 * U + 1) > 0),
                       True))
    fr = plummer_mass_outside(sp)
    xx = (sp.nsimplify(concentric.A_CORE) / sp.nsimplify(concentric.R_SHELL)) ** 2
    near("HYPOTHESIS CHECK: Plummer mass outside R_s vs its series 3x/2-15x^2/8",
         float(fr), float(sp.Rational(3, 2) * xx - sp.Rational(15, 8) * xx ** 2), 1e-12)
    chk("  so P2 fails for concentric.py's exact potential; theorem not claimed there",
        float(fr) > 0, True)
    derived_classical = "THEOREM" if all(theorem) else "NOT PROVED"
    chk("CLASSICAL_RADIAL_STABLE_FOR_ALL_M agrees with the section-1 proofs",
        CLASSICAL_RADIAL_STABLE_FOR_ALL_M, all(theorem))

    print("\n2. THE LITERATURE, READ AND RE-DERIVED")
    st, neg = amm_tensor_sector(z3)
    chk("AMM (4.6) STEP: alpha >= 0, rho^(T) >= 0 => no k^2 > 0 root (z3)", st, True)
    chk("CONTROL: alpha < 0 breaks that STEP (a root exists; AMM p.12 swap the analyses)",
        neg, True)
    g = gmmps_s_sector(sp)
    chk("GMMPS 5.3: -b0/b1 = -2 kappa alpha m^4 (= -16 pi G alpha m^4)",
        sp.simplify(g['ratio'] + 2 * g['kap'] * g['al'] * g['m'] ** 4), 0)
    chk("  and it is xi-independent", sp.diff(g['ratio'], g['xi']), 0)
    chk("J(0) from the (4.5) integral = 1/(96 pi^2 m^2)",
        sp.simplify(g['J0'] - 1 / (96 * sp.pi ** 2 * g['mpos'] ** 2)), 0)
    chk("CONTROL: J(0) from the limit of printed (4.17) agrees",
        sp.simplify(g['J0_417'] - g['J0']), 0)
    mp.mp.dps = 40
    for gv in (1, 3, -1, -5):
        near("CONTROL: (4.17) against the (4.5) integral at gamma = %d" % gv,
             float(mp.re(J_closed(mp, gv))), float(J_numeric(mp, gv)), 1e-30)
    chk("GMMPS conventions: F_S(-w^2) = -Q(w^2) identically ((5.3) vs (4.30))",
        dispersion_identity(sp), 0)
    chk("BRANCH ROOT (through gamma = 0), J INCLUDED: -2 kappa alpha m^4/(1 + kappa m^2/288 pi^2)",
        g['first_minus_target'], 0)
    chk("  xi-independent with J included", sp.simplify(sp.diff(g['gam_first'], g['xi'])), 0)
    chk("F_S'(0) (1-6xi)^2 kappa = 12 + kappa m^2/(24 pi^2) > 0: IFT applies",
        sp.simplify(g['F1_positive_form'] - (12 + g['kap'] * g['m'] ** 2 / (24 * sp.pi ** 2))), 0)
    chk("F_S(0) = 0 IFF alpha~^S_1 = 0 (gamma = 0 an exact root there)",
        sp.solve(sp.Eq(g['F0'], 0), g['al']), [0])
    chk("d gamma_0/d alpha at 0 < 0: THE BRANCH ROOT grows iff alpha > 0 (locally)",
        sp.simplify(g['slope'] + 2 * g['kap'] * g['m'] ** 4
                    / (1 + g['kap'] * g['m'] ** 2 / (288 * sp.pi ** 2))), 0)
    m_ev, eps = gmmps_mass_ev(1 / (64 * math.pi ** 2))
    m_typo, _ = gmmps_mass_ev(1 / (64 * math.pi))
    near("CONTROL: GMMPS 5.3's m ~ 7.8e-3 eV reproduced with Thm 3.6's 1/(64pi^2)",
         m_ev, GMMPS_PRINTED_MASS_EV, 0.02)
    chk("  and NOT with 5.1's (64 pi)^-1 (so 5.1 is typographical)",
        abs(m_typo - GMMPS_PRINTED_MASS_EV) / GMMPS_PRINTED_MASS_EV > 0.2, True)
    for xi in (0, sp.Rational(1, 3)):
        lo, hi, _gl = s_root_bracket(mp, eps, xi, 10 ** 100)
        chk("BRACKET at GMMPS's m, xi=%s, |b_2|<=1e100: branch root in (2g, g/2), g<0" % xi,
            (lo > 0, hi < 0), (True, True))
    lo0, _hi0, gl0 = s_root_bracket(mp, eps, 0, 10 ** 100, alpha=0)
    chk("CONTROL: at alpha~ = 0 the BRANCH bracket collapses (g = 0, F_S(0) = 0)",
        (gl0 == 0, lo0 == 0), (True, True))
    print("  -- the 'only if' is NOT claimed: roots set by b_2 at the leading constant = 0")
    fires = {}
    for sector, bb, want in (("S", -10 ** 100, True), ("TT", 10 ** 100, True),
                             ("S", 10 ** 100, False)):
        half, two, gs = b2_root_bracket(mp, eps, sector, bb)
        fires[(sector, bb)] = bracket_fires(half, two, gs)
        chk("%s b_2 = %+.0e, alpha~_1 = 0: growing root in (2g*, g*/2), g* = %s%s"
            % (sector, bb, mp.nstr(gs, 3), "" if want else "  [CONTROL: must NOT fire]"),
            fires[(sector, bb)], want)
    split_general = fires[("S", -10 ** 100)] or fires[("TT", 10 ** 100)]
    chk("LITERATURE_SPLIT_IS_ONE_CONSTANT is scoped iff a b_2 root was bracketed",
        "NOT for growth in general" in LITERATURE_SPLIT_IS_ONE_CONSTANT, split_general)
    chk("  and D26_CLAIM does not call the split 'one renormalisation constant'",
        split_general and "one renormalisation constant" in D26_CLAIM.lower(), False)

    print("\n3. THE SEMICLASSICAL CRITERION ON THE DEMAND COLUMN")
    w = off_solution_witnesses(sp)
    chk("W1 logistic from x0 = 1/2: exact flow solves and is BOUNDED",
        (w['W1_true_solves'], w['W1_true_bounded']), (True, True))
    chk("  residual f(x0) = 1/4 != 0, and the kept-residual verdict is UNBOUNDED",
        (w['W1_residual'], w['W1_kept_verdict_unbounded']), (sp.Rational(1, 4), True))
    chk("W2 x' = 1/(1+x^2) from x0 = 1: exact flow is UNBOUNDED",
        (w['W2_implicit_solves'], w['W2_true_unbounded'], w['W2_flow_increasing']),
        (True, True, True))
    chk("  both linearised verdicts BOUNDED (kept -> 1, dropped -> 0)",
        (w['W2_kept_verdict_bounded'], w['W2_dropped_verdict_decays']), (True, True))
    chk("CONTROL: at equilibria (residual 0) the verdict matches the flow",
        (w['C_residual_zero_at_equilibria'], bool(w['C1_x1_stable']), bool(w['C0_x0_unstable'])),
        ((0, 0), True, True))
    owners, paper_rows = demand_owners()
    print("  [info] demand owners from ledger.DEMAND: %s" % ", ".join(owners))
    print("  [info] plus device files %s; paper-owned rows (not scannable): %s"
          % (", ".join(DEVICE_FILES), ", ".join(paper_rows)))
    scanned = owners + DEVICE_FILES
    scan = self_consistency_scan(scanned + POSITIVE_CONTROLS)
    chk("owners are READ from the ledger, not typed (>= 10, certify and stockgate in)",
        (len(owners) >= 10, "certify" in owners, "stockgate" in owners), (True, True, True))
    chk("CONTROL: the scan finds tokens where solutions ARE held (throatmass, hpscentre)",
        [n for n in POSITIVE_CONTROLS if scan[n] == 0], [])
    # DOCKET 64 ruling B4 asked for hpscentre here; dropping it must fire in THIS file,
    # not only downstream in ledger.py.  hpscentre is where m < 0 solutions are held.
    chk("  and hpscentre, which holds the m < 0 solutions, is one of them",
        "hpscentre" in POSITIVE_CONTROLS and hpscentre.M_NEGATIVE_FOUND_IN_HPS_SYSTEM, True)
    hits = sorted(n for n in scanned if scan[n] > 0)
    chk("every owner with token hits was READ, and only those (READ_HITS)",
        hits, sorted(READ_HITS))
    ev, unread = semiclassical_evaluable_on_demand(scan, scanned)
    chk("no unread hit, so the scan's verdict stands", unread, [])
    chk("SEMICLASSICAL_EVALUABLE_ON_DEMAND = the verdict derived from candidates()",
        SEMICLASSICAL_EVALUABLE_ON_DEMAND, ev)
    cands = candidates()
    chk("throatmass: m < 0 reported in none of its families (asked of its table)",
        (cands[0]['m_negative'], throatmass.NEGATIVE_MASS_SELF_CONSISTENT_FOUND), (False, "NOT-FOUND"))
    chk("hpscentre: m < 0 FOUND in HPS's system, NOT inside the established domain",
        (cands[1]['m_negative'], cands[1]['inside_domain']), (True, False))
    chk("  so 'all have m >= 0' is stale: no ledger-facing text asserts it",
        any("m >= 0" in t for t in (D26_CLAIM, D26_ANSWERED_BY, SEMICLASSICAL_STATUS,
                                    demand_semiclassical_solutions.__doc__)),
        not cands[1]['m_negative'])
    chk("  and O5 is open in both owners, so H1 is O5's question",
        (throatmass.O5_CLOSED, hpscentre.O5_CLOSED), (False, False))
    chk("D26_CLAIM says 'recorded or shown', not 'obstruction proved' (a scan, not a proof)",
        ("recorded or shown" in D26_CLAIM, "obstruction proved" in D26_CLAIM.lower()),
        (True, False))

    print("\n4. THE ROW -- statuses DERIVED from the evidence above")
    chk("CLASSICAL_RADIAL_STATUS = derived from section 1's proofs",
        CLASSICAL_RADIAL_STATUS, derived_classical)
    chk("D26_STATUS = OPEN iff the semiclassical half is not evaluable",
        D26_STATUS, "OPEN" if not ev else "EVALUABLE -- re-rule D26")
    record("FLAT_EXTERIOR_INHERITS_AMM (READ: AMM IV, Fourier over Minkowski)",
           FLAT_EXTERIOR_INHERITS_AMM)
    record("FLAT_EXTERIOR_INHERITS_GMMPS (READ: GMMPS 1.2, Thm 1.2 on R^4)",
           FLAT_EXTERIOR_INHERITS_GMMPS)
    record("SPLIT_ADJUDICATED_HERE", SPLIT_ADJUDICATED_HERE)
    record("ALPHA_ZERO_ROOT_GROWTH (outside Thm 4.16, Prop 4.10, AMM p.12)",
           ALPHA_ZERO_ROOT_GROWTH)
    record("AMM hypotheses named", len(AMM_HYPOTHESES))
    record("WITHDRAWN claims kept", len(WITHDRAWN))

    print("\n  %d checks that can fail, %d failed; %d record pins printed, not counted."
          % (len(passed) + len(fails), len(fails), len(records)))
    print("  SELFTEST %s" % ("OK" if not fails else "FAILED: %d" % len(fails)))
    return 0 if not fails else 1


if __name__ == "__main__":
    sys.exit(selftest() if "--selftest" in sys.argv else report())
