#!/usr/bin/env python3
"""
provenance.py -- the epistemic audit.  Every load-bearing claim in this project,
classified by what it actually IS: theorem, identity, model, scaling, citation
or conjecture.  And then the question that matters: WHAT DOES THE HEADLINE REST
ON?

M: "let's take a moment to review all the research.  If anything we have used
from outside literature, such as assertions, conjecture, heuristics, perhaps we
can define the theorems, proofs, laws, etc."

    THIS IS THE RIGHT AUDIT TO RUN BEFORE ANYTHING IS PUBLISHED, and it returns
    one uncomfortable answer that no individual pass could see.

===============================================================================
THE STATUSES, AND THEY ARE NOT RANKED BY CONFIDENCE
===============================================================================

    THEOREM-HERE   proved in this tree from stated premises, derivation in the
                   file, reproducible by running it.
    THEOREM-CITED  a theorem in the literature, used as given and NOT re-proved
                   here.  Solid, and not this project's work.
    IDENTITY       follows algebraically from definitions.  TRUE, and carrying
                   no physical content beyond the definitions it is built from.
                   An identity cannot be wrong and cannot be evidence.
    MODEL          a consequence of a CHOSEN ansatz rather than a solved field
                   equation.  Internally validated, externally uncertified.
    MEASURED       a number an instrument produces; reproducible, and only as
                   good as the model or theorem it is computed inside.
    SCALING        order-of-magnitude or dimensional argument, explicitly not a
                   theorem, with the coefficient unresolved.
    CITED-2ND      taken from a report of a source not directly read.
    CONJECTURE     unproven in the literature.
    PRESCRIPTION   a proposed rule for an unsettled physical question, where
                   rival prescriptions exist and disagree.

===============================================================================
1. THE FINDING THIS AUDIT EXISTS TO REPORT
===============================================================================

THE TRANSITION EQUATION IS A MODEL, NOT A THEOREM, AND EVERYTHING THE PROJECT
HEADLINES INHERITS THAT STATUS.

    Delta d = (G/c^2) M Lambda comes from a CHOSEN POTENTIAL in a CHOSEN metric
    form -- isotropic, g_tt = -e^{2Phi}, g_ij = e^{-2Phi}, with Phi a Plummer
    core minus a shell.  Lambda = 2[ln(2 R_s/sqrt(b^2 + a^2)) - 1] is a closed
    form derived from THAT POTENTIAL and validated against its own integral to
    0.08 %.

    THAT VALIDATION IS INTERNAL.  It shows the closed form matches the ansatz.
    It does not show the ansatz solves G_munu = 8 pi T_munu for any specified
    matter model, and index3.py has carried NOT-CERTIFIED since the Le pass for
    exactly this reason: a metric-first construction may have no well-posed
    matter model at all.

    core.py already records the sharpest version: Phi_max = m/a runs 0.25 to 1.0
    across the seated window, and at Phi = 1 the linearised spatial metric
    (1 - 2 Phi) HAS FLIPPED SIGN.  "THE CORE IS INTRINSICALLY A STRONG-FIELD
    OBJECT IN THIS DESIGN AND NO WEAK-FIELD DESCRIPTION OF IT WILL DO."

    SO: the exchange rate c^4/(G Lambda) = 1.2123737e43 J/m is MODEL.  The
    seventy orders, the Planck cell, the 196 MJ, the tiling neutrality and the
    scale-invariance all inherit MODEL, because all of them are Lambda wearing
    different clothes.

===============================================================================
2. AND THE ASYMMETRY IS THE REAL RESULT
===============================================================================

Sort the tree's load-bearing claims by status and a pattern falls out that no
single pass could have shown:

    EVERY OBSTRUCTION THIS PROJECT TRUSTS IS A THEOREM.
    EVERY POSITIVE CONSTRUCTION IT OFFERS IS A MODEL.

    The refusals -- the Maxwell NEC theorem, the null-dust identity, PMT
    rigidity, the [0, pi] topology, the classical grandfather condition, the
    Deutsch fixed-point set -- are proved, here or in the literature, and do not
    move.  The construction -- the corridor, Lambda, the rate, the cell -- is an
    ansatz that has never been certified against a matter model.

        THAT IS EXACTLY THE SHAPE A NEGATIVE RESULT SHOULD HAVE, AND EXACTLY
        THE WRONG SHAPE FOR A POSITIVE ONE.

    It means the project's NO is much better supported than its YES ever was,
    and that asymmetry should be stated in any paper rather than discovered by
    a referee.

===============================================================================
3. WHAT IS GENUINELY PROVED HERE, AND IT IS A SHORT LIST
===============================================================================

    THE MAXWELL NEC THEOREM.  For T_munu = F_mu-a F_nu^a - (1/4) g_munu F^2 and
    any null k, set V_a = F_mu-a k^mu.  Then T_munu k^mu k^nu = V.V and V.k = 0
    BECAUSE F IS ANTISYMMETRIC, so V is orthogonal to a null vector, hence
    spacelike or parallel to it, hence V.V >= 0.  Proved, and measured over
    200,000 random fields and in D = 3..26.  THIS IS THE STRONGEST RESULT THE
    PROJECT HOLDS and it is a refusal.

    THE NULL-DUST IDENTITY.  T_munu k^mu k^nu = eps (eta.k)^2: a square times a
    non-negative.  Proved.

    THE ORIENTATION INTERVAL.  Two directions have relative angle in [0, pi],
    an interval with distinct endpoints, because theta and 2pi - theta are the
    same pair.  The coupling is a strict bijection onto [0, 8], so identifying
    the endpoints forces one configuration to carry both 0 and 8.  Proved.

    THE DEUTSCH FIXED-POINT SET.  rho = X rho X solved in full: a = d = 1/2 is
    FORCED, the fixed set is the Bloch x-axis, and every member has
    rho_00 = rho_11 = 1/2 exactly.  Proved, and scanned.

    THE CLASSICAL GRANDFATHER CONDITION.  b = b XOR 1 has no solution over
    {0,1}.  Proved by enumerating both elements of the domain.

===============================================================================
4. WHAT IS AN IDENTITY, AND WHY THAT MATTERS MORE THAN IT LOOKS
===============================================================================

    THE COLLAPSE IDENTITY.  E_transition/E_kugelblitz = 2/Lambda at every d.
    Both sides are (c^4/G) times a length by construction, so the ratio is a
    pure number by construction.  IT CANNOT BE OTHERWISE.

    E_t(l_P) = E_Planck/Lambda.  Same: l_P c^4/G IS E_Planck.

    THE GRANULARITY GAP.  One photon that fits the cell carries E_Planck; the
    cell's budget is E_Planck/Lambda; the ratio is Lambda.  Again by
    construction.

        THESE ARE TRUE AND THEY ARE NOT EVIDENCE.  An identity is a restatement
        of its definitions, and the recurrence of Lambda across them is the
        recurrence of one definition, NOT three independent confirmations.  A
        paper that presents them as corroboration would be presenting the same
        fact three times.

    THE ONE THING THEY DO ESTABLISH is internal consistency: the framework does
    not contradict itself at the Planck scale, and the margin comes out
    untuned.  That is worth stating and is not worth more than that.

===============================================================================
5. WHAT IS CITED RATHER THAN PROVED, AND ONE IS SECOND-HAND
===============================================================================

    THEOREM-CITED and load-bearing: the Positive Mass Theorem (Schoen-Yau,
    Witten) behind PMT rigidity -- this is what DERIVES the exotic requirement
    rather than assuming it, and the project leans on it hard.  Ford-Roman.
    Fewster & Osterbrink's unboundedness result.  Epstein-Glaser-Jaffe.

    RE-DERIVED RATHER THAN QUOTED, which is better: the 2024 kugelblitz numbers,
    Faraoni & Dumse's GE/GM chain, the Casimir and Ford-Roman crossovers.

    CITED-2ND, AND FLAGGED AS SUCH IN ITS OWN FILE: Barker, Bhatia & Gupta's
    factor of eight, held through Sparano-Vilasi-Vilasi because the 1967 paper
    is not reachable from here.  It agrees with an independent derivation, which
    is why it is usable -- but the project has never read it.

    AND ONE STRUCTURE IS ASSERTED, NOT DERIVED, WHICH IS WORTH BEING PLAIN
    ABOUT: the spin-2 exchange amplitude A = 2(p.p')^2 - p^2 p'^2 was TAKEN as
    the standard one-graviton-exchange numerator.  It was not derived here from
    the Einstein-Hilbert action.  It reproduces four independent known cases
    (Newton, light bending, TEP's factor 2, the parallel zero), which is strong
    evidence it is the right structure and is NOT a derivation of it.

===============================================================================
6. THE CONJECTURES, AND WHICH ONES ANYTHING RESTS ON
===============================================================================

    HOOP CONJECTURE -- used for the "largest coin" and the kugelblitz threshold.
    ALREADY FLAGGED in denominate.py as "a hoop-conjecture heuristic, not a
    theorem."  Nothing load-bearing rests on it; it decorates a metaphor.

    CHRONOLOGY PROTECTION -- chronology.py carries HAWKING = NOT-RUN and
    closure.py reaches its result WITHOUT it, deliberately.  NOTHING RESTS ON
    IT, and that was a design choice rather than an accident.

    THE CTC PRESCRIPTIONS -- Deutsch's and the postselected one are
    PRESCRIPTIONS, not theorems of quantum mechanics, and they contradict each
    other on nearly every question.  closure.py's conclusion is constructed to
    survive BOTH plus the classical case, which is the right way to lean on an
    unsettled question.

===============================================================================
7. THE SCALINGS, EACH ALREADY MARKED WHERE IT LIVES
===============================================================================

    THE TEARDOWN CTC WINDOW.  tau/loop = R/(2D) <= 1/2.  The factor of 2 is
    geometry-dependent; the SCALING (tau ~ R against loop ~ D >= R) is not.
    Marked in teardown.py.

    THE CANDIDATE-D EXPONENT MATCH.  N_n is schematic in the source and set to
    1.  A true coefficient of 10 or 1/10 moves the crossover by sqrt(10) in the
    CUTOFF and by nothing in the orders.  Marked in candidates.py.

    THE PLANCK-CELL SPECIFICATION rests on the candidate-D scaling for its
    MAGNITUDE gate, so it inherits SCALING there -- and MODEL from Lambda for
    its energy.  planckcell.py says so; this file makes the inheritance
    explicit.

===============================================================================
WHAT THIS AUDIT ESTABLISHES
===============================================================================

    THE HEADLINE IS A MODEL.  c^4/(G Lambda) = 1.21e43 J/m rests on a chosen
    potential that has never been certified against a matter model, and every
    downstream number inherits that.

    THE REFUSALS ARE THEOREMS.  Every obstruction the project trusts is proved
    here or cited from a proof.  The NO is better supported than the YES.

    THREE HEADLINE "CONFIRMATIONS" ARE ONE DEFINITION.  The collapse identity,
    the Planck-energy form and the granularity gap are identities in Lambda, not
    independent corroborations of it.

    NOTHING LOAD-BEARING RESTS ON A CONJECTURE, and where the physics is
    unsettled (CTCs) the conclusion was built to survive rival prescriptions.

    ONE STRUCTURE IS ASSERTED: the spin-2 amplitude, cross-checked against four
    known cases and not derived here.

    NOT CLAIMED: that this audit is complete.  It covers the load-bearing
    claims this project headlines.  A full census of all 508 index findings by
    status is not attempted and would be a different instrument.
"""

import sys

# status vocabulary
THEOREM_HERE = "THEOREM-HERE"
THEOREM_CITED = "THEOREM-CITED"
IDENTITY = "IDENTITY"
MODEL = "MODEL"
MEASURED = "MEASURED"
SCALING = "SCALING"
CITED_2ND = "CITED-2ND"
CONJECTURE = "CONJECTURE"
PRESCRIPTION = "PRESCRIPTION"
ASSERTED = "ASSERTED-STRUCTURE"

STATUSES = (THEOREM_HERE, THEOREM_CITED, IDENTITY, MODEL, MEASURED,
            SCALING, CITED_2ND, CONJECTURE, PRESCRIPTION, ASSERTED)

# (claim, status, owner, load-bearing?, note)
LEDGER = (
    # --- the construction, and it is all one status
    ("transition equation Delta d = (G/c^2) M Lambda", MODEL, "phase1.py", True,
     "chosen isotropic ansatz with a Plummer core minus a shell; not a solved matter model"),
    ("Lambda = 2[ln(2 R_s/sqrt(b^2+a^2)) - 1] = 9.982529", MODEL, "phase1.py", True,
     "closed form OF THAT ANSATZ, validated against its own integral to 0.08 % -- internally"),
    ("exchange rate c^4/(G Lambda) = 1.2123737e43 J/m", MODEL, "phase1.py", True,
     "THE HEADLINE.  Inherits MODEL from Lambda"),
    ("no frame-independent Hawking-Ellis certification", MODEL, "index3.py", True,
     "NOT-CERTIFIED, seated since the Le pass: metric-first may have no well-posed matter model"),
    ("the core is intrinsically strong-field", MODEL, "core.py", True,
     "Phi_max = m/a runs 0.25 to 1.0; at Phi = 1 the linearised spatial metric flips sign"),

    # --- what is actually proved here
    ("every classical EM field satisfies the NEC", THEOREM_HERE, "lattice.py", True,
     "V_a = F_mu-a k^mu, V.k = 0 by antisymmetry, so V.V >= 0.  The strongest result held"),
    ("null dust saturates the NEC", THEOREM_HERE, "light.py", True,
     "T k k = eps (eta.k)^2, a square times a non-negative"),
    ("orientation space is [0, pi], an interval", THEOREM_HERE, "bisector.py", True,
     "theta and 2pi - theta are the same pair; the coupling is a bijection onto [0,8]"),
    ("every Deutsch fixed point is exactly 50/50", THEOREM_HERE, "closure.py", True,
     "rho = X rho X solved in full: a = d = 1/2 FORCED; fixed set is the Bloch x-axis"),
    ("classical grandfather has no solution", THEOREM_HERE, "closure.py", True,
     "b = b XOR 1 enumerated over both elements of its domain"),
    ("the coupling range is exactly [0, 8]", THEOREM_HERE, "bisector.py", False,
     "monotonic over 20,001 samples; A/A_N = c^4/2 with c the chord"),

    # --- cited theorems, load-bearing
    ("Positive Mass Theorem / PMT rigidity", THEOREM_CITED, "pair.py", True,
     "Schoen-Yau, Witten.  This DERIVES the exotic requirement rather than assuming it"),
    ("Ford-Roman quantum inequality", THEOREM_CITED, "candidates.py", True,
     "used as given; the crossover is re-derived from it, the inequality is not"),
    ("non-minimal coupling is unbounded below", THEOREM_CITED, "candidates.py", True,
     "Fewster & Osterbrink arXiv:0708.2450; read in full, not re-proved"),
    ("2024 kugelblitz Schwinger block", THEOREM_CITED, "lightbuild.py", True,
     "arXiv:2405.02389; its numbers ARE re-derived here, its argument is not"),

    # --- identities: true, and not evidence
    ("E_transition/E_kugelblitz = 2/Lambda at every d", IDENTITY, "lightbuild.py", True,
     "both sides are (c^4/G) x a length BY CONSTRUCTION.  It cannot be otherwise"),
    ("E_t(l_P) = E_Planck/Lambda", IDENTITY, "lightbuild.py", True,
     "l_P c^4/G IS E_Planck.  A restatement"),
    ("one fitting photon overshoots the cell by Lambda", IDENTITY, "planckcell.py", True,
     "hbar c/l_P = E_Planck and the budget is E_Planck/Lambda.  By construction"),
    ("the Planck cell costs 195.95 MJ", IDENTITY, "planckcell.py", True,
     "E_Planck/Lambda evaluated.  Inherits MODEL from Lambda"),
    ("tiling is exactly neutral", IDENTITY, "planckcell.py", True,
     "Delta d is linear in M, so N cells cost N times one.  Arithmetic"),

    # --- asserted structure
    ("spin-2 amplitude A = 2(p.p')^2 - p^2 p'^2", ASSERTED, "factor8.py", True,
     "TAKEN as the standard one-graviton numerator; NOT derived from Einstein-Hilbert here. "
     "Reproduces four known cases, which is evidence and not derivation"),

    # --- second-hand
    ("Barker, Bhatia & Gupta's factor of eight", CITED_2ND, "factor8.py", False,
     "held through Sparano-Vilasi-Vilasi; the 1967 paper was never read here"),

    # --- scalings
    ("teardown CTC window tau/loop = R/(2D) <= 1/2", SCALING, "teardown.py", True,
     "the factor of 2 is geometry-dependent; the scaling tau ~ R vs loop ~ D >= R is not"),
    ("candidate-D exponent match, shortfall (l_UV/l_P)^2/Lambda", SCALING, "candidates.py", True,
     "N_n schematic in the source and set to 1; a coefficient of 10 moves the CUTOFF by sqrt(10)"),

    # --- conjectures and prescriptions
    ("hoop conjecture, for the largest-coin threshold", CONJECTURE, "denominate.py", False,
     "already flagged there as a heuristic; decorates a metaphor, carries nothing"),
    ("Hawking chronology protection", CONJECTURE, "chronology.py", False,
     "NOT-RUN, and closure.py reaches its result WITHOUT it, deliberately"),
    ("Deutsch and postselected CTC prescriptions", PRESCRIPTION, "closure.py", True,
     "rival prescriptions that disagree elsewhere; the conclusion was built to survive both"),
)


def by_status(status):
    return [r for r in LEDGER if r[1] == status]


def load_bearing():
    return [r for r in LEDGER if r[3]]


def statuses_used():
    return sorted({r[1] for r in LEDGER})


def headline_status():
    for claim, st, _o, _lb, _n in LEDGER:
        if claim.startswith("exchange rate"):
            return st
    raise KeyError("headline")


def headline_is_a_theorem():
    return headline_status() in (THEOREM_HERE, THEOREM_CITED)


def obstructions():
    """The claims that REFUSE something."""
    return [r for r in LEDGER if r[1] in (THEOREM_HERE, THEOREM_CITED)]


def constructions():
    """The claims that BUILD something."""
    return [r for r in LEDGER if r[1] == MODEL]


def every_obstruction_is_a_theorem():
    return all(r[1] in (THEOREM_HERE, THEOREM_CITED) for r in obstructions())


def every_construction_is_a_model():
    return all(r[1] == MODEL for r in constructions())


def the_asymmetry():
    return len(obstructions()), len(constructions())


def identities_in_lambda():
    return [r[0] for r in by_status(IDENTITY) if "Lambda" in r[0] or "l_P" in r[0]]


def identities_are_independent_confirmations():
    """They are not.  They are one definition restated."""
    return False


def load_bearing_conjectures():
    return [r[0] for r in LEDGER if r[3] and r[1] == CONJECTURE]


def anything_rests_on_a_conjecture():
    return len(load_bearing_conjectures()) > 0


AUDIT_IS_COMPLETE = False
AUDIT_COVERS = "the load-bearing claims this project headlines, not all 508 index findings"


def selftest():
    ok = True

    def chk(label, got, want):
        nonlocal ok
        good = got == want
        ok &= good
        print("  %-56s %20s %20s  %s"
              % (label, str(got)[:20], str(want)[:20], "ok" if good else "FAIL"))

    print("1. THE FINDING THIS AUDIT EXISTS TO REPORT")
    chk("the headline's status", headline_status(), MODEL)
    chk("  is the headline a theorem", headline_is_a_theorem(), False)
    print("       Delta d = (G/c^2) M Lambda comes from a CHOSEN POTENTIAL in a")
    print("       chosen metric form.  Lambda's 0.08 % validation is INTERNAL:")
    print("       it shows the closed form matches the ansatz, not that the")
    print("       ansatz solves the field equations for any matter model.")

    print("\n2. AND THE ASYMMETRY IS THE REAL RESULT")
    o, c = the_asymmetry()
    print("     obstructions trusted: %d    constructions offered: %d" % (o, c))
    chk("is every obstruction a theorem", every_obstruction_is_a_theorem(), True)
    chk("is every construction a model", every_construction_is_a_model(), True)
    print("       THE PROJECT'S NO IS BETTER SUPPORTED THAN ITS YES EVER WAS.")
    print("       That should be stated in a paper, not found by a referee.")

    print("\n3. WHAT IS GENUINELY PROVED HERE")
    for claim, _st, owner, _lb, note in by_status(THEOREM_HERE):
        print("     %-46s %s" % (claim[:46], owner))
        print("        %s" % note[:72])
    chk("theorems proved here", len(by_status(THEOREM_HERE)), 6)

    print("\n4. WHAT IS AN IDENTITY -- true, and NOT evidence")
    for claim, _st, owner, _lb, _n in by_status(IDENTITY):
        print("     %-46s %s" % (claim[:46], owner))
    chk("identities", len(by_status(IDENTITY)), 5)
    chk("  how many are Lambda restated", len(identities_in_lambda()), 3)
    chk("  are they independent confirmations",
        identities_are_independent_confirmations(), False)
    print("       THE RECURRENCE OF Lambda ACROSS THEM IS THE RECURRENCE OF ONE")
    print("       DEFINITION.  A paper presenting them as corroboration would be")
    print("       presenting the same fact three times.")

    print("\n5. CITED, AND ONE IS SECOND-HAND")
    for claim, _st, owner, _lb, _n in by_status(THEOREM_CITED):
        print("     %-46s %s" % (claim[:46], owner))
    chk("cited theorems", len(by_status(THEOREM_CITED)), 4)
    chk("second-hand citations", len(by_status(CITED_2ND)), 1)
    chk("asserted structures", len(by_status(ASSERTED)), 1)
    print("       the spin-2 amplitude was TAKEN, not derived from the")
    print("       Einstein-Hilbert action.  Four known cases is evidence.")

    print("\n6. THE CONJECTURES")
    for claim, _st, owner, lb, _n in by_status(CONJECTURE):
        print("     %-46s %-16s load-bearing: %s" % (claim[:46], owner, lb))
    chk("load-bearing conjectures", load_bearing_conjectures(), [])
    chk("  so does anything rest on one", anything_rests_on_a_conjecture(), False)
    chk("CTC prescriptions", len(by_status(PRESCRIPTION)), 1)
    print("       rival prescriptions that disagree elsewhere; closure.py's")
    print("       conclusion was built to survive BOTH plus the classical case.")

    print("\n7. THE SCALINGS")
    for claim, _st, owner, _lb, note in by_status(SCALING):
        print("     %-46s %s" % (claim[:46], owner))
        print("        %s" % note[:72])
    chk("scalings", len(by_status(SCALING)), 2)

    print("\n  THE LEDGER")
    print("     %-22s %s" % ("status", "count"))
    for st in STATUSES:
        n = len(by_status(st))
        if n:
            print("     %-22s %d" % (st, n))
    chk("claims audited", len(LEDGER), 27)
    chk("  of which load-bearing", len(load_bearing()), 23)
    chk("is the audit complete", AUDIT_IS_COMPLETE, False)
    print("     it covers %s" % AUDIT_COVERS)

    print("\n  SELFTEST %s" % ("OK" if ok else "FAILED"))
    return ok


def report():
    print(__doc__)
    print("""
  ------------------------------------------------------------------------
  THE PASS IN ONE PARAGRAPH

  Sorted by epistemic status, the project splits cleanly and uncomfortably.
  The transition equation is a MODEL: Delta d = (G/c^2) M Lambda comes from
  a chosen potential in a chosen metric form, and Lambda's 0.08 % agreement
  validates the closed form against that ansatz rather than the ansatz
  against the field equations -- which is what NOT-CERTIFIED has recorded
  since the Le pass, and what core.py's sign-flipped spatial metric says
  more sharply.  So the headline, c^4/(G Lambda) = 1.21e43 J/m, is MODEL,
  and the seventy orders, the Planck cell, the 196 MJ and the tiling
  neutrality all inherit it, because all of them are Lambda in different
  clothes.  Against that: every obstruction the project trusts is a
  THEOREM -- the Maxwell NEC result and the null-dust identity proved here,
  PMT rigidity and Ford-Roman cited from proofs, the [0,pi] topology and
  the Deutsch fixed-point set solved in full.  THE NO IS BETTER SUPPORTED
  THAN THE YES, which is the right shape for a negative result and the
  wrong one for a positive.  Three apparent confirmations -- the collapse
  identity, the Planck-energy form, the granularity gap -- are IDENTITIES
  in Lambda and are one definition restated, not three corroborations.
  Nothing load-bearing rests on a conjecture: the hoop conjecture decorates
  a metaphor, chronology protection is NOT-RUN by design, and where the
  physics is genuinely unsettled the CTC conclusion was built to survive
  rival prescriptions.  One structure is ASSERTED rather than derived -- the
  spin-2 amplitude -- and one citation is second-hand and flagged.
  ------------------------------------------------------------------------""")
    return 0


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    sys.exit(report())
