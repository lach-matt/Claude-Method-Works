#!/usr/bin/env python3
r"""
specthm.py -- STEP 1a: THE SPECIFICATION THEOREM, AS AN INSTRUMENT.

    python3 specthm.py             the reading: theorem, requirements, classes,
                                   escapes -- the printout M reviews
    python3 specthm.py --selftest  every ask, every derivation, and controls
                                   that turn it red

Runs under python3 (3.11).  Needs z3 and sympy (pypi; see PROOF-ASSISTANT.md),
but only inside functions: the import itself asks only stdlib and the seated
peers in this directory, which it imports by path and copies none of.

===============================================================================
0.  WHAT THIS IS, AND WHAT IT IS NOT
===============================================================================

M ruled the order: step 3 (testing) complete, then 1a the specification
theorem, 1b the balanced equation, 1c the device.  M chose INSTRUMENT FIRST:
the theorem's statement and its escape list are reviewed by M BEFORE any paper
is written.  So this file writes no paper.  It prints what M reviews.

    IT ESTABLISHES NO ROW.  Every status and every figure below is ASKED of the
    instrument that owns it, at run time, through `ledger.py`'s rows or the
    owner's own attribute or function.  A status or figure typed here would be
    failure mode 3.  What this file does itself is narrow and named:

      * it SORTS the object space into classes (a partition, checked by z3),
      * it DERIVES each class verdict by z3 from the owner facts that are in
        force -- each fact is admitted only while its owner still says THEOREM
        (or its computed equivalent), and the unsat core names which facts the
        verdict used,
      * it CHECKS that each class states every hypothesis its proof used, and
        no hypothesis it did not use,
      * it COMPOSES two owner functions into one figure: the persistence ratio
        restated on the corridor's own demand, Delta d (section 3), and
      * it DERIVES the headline from the verdicts, so a moved owner moves the
        headline.

    IT DOES NOT TYPE A VERDICT.  The selftest pins the verdicts it expects, as
    `ledger.py` pins its asks; the report never reads those pins.

M's rules, as this file applies them:
    "everything we claim must be accurate and true" -- every sentence that is
      a result carries its owner, and a result without one is marked (NO
      OWNER, READ, CITED, ASSUMED);
    "all things must be proven, no caveats" -- every limitation is a NAMED
      HYPOTHESIS inside the theorem or a NAMED OPEN ESCAPE, never a footnote;
    "no coefficients, exact calculations only";
    "over-representation must be avoided at all costs" -- one question is one
      requirement (R9 is folded into R4, R1 is the definition R2 is read
      from, O1 is S4 counted once), and every ledger row is PLACED exactly
      once, checked against the ledger's live row list;
    the status word DECLARED is never used, and the selftest checks it.

===============================================================================
1.  THE OBJECTS, AND WHY THEY MUST BE KEPT APART
===============================================================================

    C    the contracting corridor -- what the ledger's DEMAND column prices.
    T    phase1.py's TRANSITION, with D4 as M restated it (M-D64-1).
    S    M's scoped seat -- spec.py's "DROP THE LEAD. KEEP THE SEAT."
    W    the throat gate (non-simply-connected topology).
    Rec  the reconstruction route (ledger S5).

A requirement proved about C is not a requirement on S.  spec.py establishes S
as achievable with ordinary matter satisfying every energy condition, and this
file must not declare impossible anything that scoping establishes -- the
selftest checks, by z3, that no EMPTY class contains spec.py's witness and that
no requirement on C is applied to S.

===============================================================================
2.  THE CLASS VERDICTS, AND THE FOUR WORDS
===============================================================================

    EMPTY       no member of the class is an instance of its object: z3 finds
                the class, the object's definition and the owner facts in force
                jointly unsatisfiable, with NO assumed hypothesis.
    EMPTY IF    unsatisfiable only once a named ASSUMED hypothesis is added.
                The hypothesis is printed in the verdict and has an escape.
    OPEN        satisfiable with every owner fact in force: nothing in the tree
                decides it.  OPEN is not "possible".
    NONEMPTY    a witness exists, computed by its owner (only the seat, S-1).

"EMPTY" is about the OBJECT, never about spacetimes: Milne exists and lies in K0;
it is simply not a contracting corridor.

===============================================================================
3.  THE ONE COMPOSED FIGURE
===============================================================================

achievable.py's persistence ratio at its pinned (mu, alpha) = (5e-3, 0.02) prices
a core sized by concentric.py's SEAT + LEAD window edge (achievable.py line
"M_OVER_B = 5.0e-3  # concentric.py's window, weakest end") -- a lead M dropped
and a seat that is S's requirement, not C's.  Contraction is linear in m for
every m > 0 (phase1.py's transition equation), so that figure is not the price
of the minimal contracting corridor.  This file therefore also states the ratio
on C's OWN demand: with Delta d = (G/c^2) M Lambda (phase1.contraction_law) and
M = mu b c^2/G, S is linear in mu at fixed (b, alpha), and the refusal holds for
every contraction above Delta d_x(b) = Delta d_owner(b) / S_owner(b).  COMPOSED
HERE from two owners; it carries the transition equation's own hypotheses
(weak field, Lambda at R_s/b = 200, a/b = 0.02 -- MEASURED by phase1.py to 0.08 %).

===============================================================================
4.  WHAT THIS FILE REFUSES
===============================================================================

    IT DOES NOT RANK THE OPEN CLASSES.  Which is most promising is M's.
    IT DOES NOT TOTAL THE GAPS.  Orders on different quantities do not add.
    IT DOES NOT RULE.  Every place where the theorem needs a requirement M has
      not ruled is printed under PENDING FOR M, with what changes either way.
    IT DOES NOT DISCHARGE AN ASSUMED HYPOTHESIS.  H_flat stays ASSUMED until
      O2 closes, and if O2 closes this file prints RE-ASK rather than guess
      which way.
    IT REPAIRS NOTHING AND EDITS NO PEER.  The critiques' divergences from an
      owner are printed as divergences, not applied to the owner.
"""

import contextlib
import copy
import io
import math
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path:
    sys.path.insert(0, HERE)

import ledger          # noqa: E402  (imports most owners, by path)
import achievable      # noqa: E402
import axial           # noqa: E402
import bounds          # noqa: E402
import branelink       # noqa: E402
import candidates      # noqa: E402
import certify         # noqa: E402
import create          # noqa: E402
import driven          # noqa: E402
import drivensource    # noqa: E402
import excite          # noqa: E402
import fewsterteo      # noqa: E402
import foliation       # noqa: E402
import formation       # noqa: E402
import higgs           # noqa: E402
import hpscentre       # noqa: E402
import latticectc      # noqa: E402
import linstab         # noqa: E402
import noise           # noqa: E402
import nonstatic       # noqa: E402
import overturn        # noqa: E402
import phase1          # noqa: E402
import qeihps          # noqa: E402
import seatindex       # noqa: E402
import spec            # noqa: E402
import stockgate       # noqa: E402
import throatmass      # noqa: E402
import tolman          # noqa: E402
import transit         # noqa: E402
import warpfolder      # noqa: E402

# The status vocabulary is the ledger's, asked.  The four words that are not
# ledger statuses name how a clause is held, and none of them is a result.
THEOREM, NARROWED, MEASURED, SURVEY, OPEN, WITHDRAWN, REFUSED = (
    ledger.THEOREM, ledger.NARROWED, ledger.MEASURED, ledger.SURVEY,
    ledger.OPEN, ledger.WITHDRAWN, ledger.REFUSED)
CITED, ASSUMED, READ, DEFINITION, CHECKED, NO_OWNER = (
    "CITED", "ASSUMED", "READ", "DEFINITION", "CHECKED (a code path)",
    "NO OWNER")

EMPTY, EMPTY_IF, OPEN_V, NONEMPTY, RE_ASK = (
    "EMPTY", "EMPTY IF", "OPEN", "NONEMPTY", "RE-ASK")
VERDICTS = (EMPTY, EMPTY_IF, OPEN_V, NONEMPTY)

#: The one word this file must never use as a status or verdict.
FORBIDDEN_STATUS_WORD = "DECLARED"

#: M'S PENDING RULINGS THAT CHANGE A VERDICT.  None means "not ruled": the
#: requirement is NOT imposed.  The selftest sets each to True to show what the
#: ruling would change -- it never sets it in a reading.
PENDING_REQUIREMENTS = {
    "chronology": None,     # is a closed causal curve disqualifying?  (P3)
    "pathology": None,      # is a singularity / point at infinity?    (P3)
}


# ============================================================ 1. THE ASKS

def A(mod, attr):
    """An owner's pinned attribute, asked live.  Raises if the owner dropped it:
    a silently absent pin is how achievable.py's 65 orders survived."""
    m = sys.modules[mod]
    if not hasattr(m, attr):
        raise AttributeError("%s no longer pins %s -- specthm is stale"
                             % (mod, attr))
    return getattr(m, attr)


def ledger_ids():
    """Every row id on the board, in board order, asked live."""
    return ([r[0] for r in ledger.DEMAND] + [r[0] for r in ledger.SUPPLY]
            + [r[0] for r in ledger.OPEN_ROWS] + [r[0] for r in ledger.CLOSED_ROWS]
            + [r[0] for r in ledger.balance()] + [r[0] for r in ledger.RULED_BY_M])


def withdrawn_ids():
    return [r[0] for r in ledger.WITHDRAWN_ROWS]


def row(rid):
    """(status, claim, what-would-move-it) of a ledger row, asked live.

    A CLOSED row's status is the clause its own answer opens with, verbatim --
    "CLOSED, AND REFUSED" for O1 -- never re-worded here."""
    for r in ledger.DEMAND:
        if r[0] == rid:
            return r[2], r[1], r[4]
    for r in ledger.SUPPLY:
        if r[0] == rid:
            return r[2], r[1] + ": " + r[4], None
    for r in ledger.OPEN_ROWS:
        if r[0] == rid:
            return OPEN, r[1], r[2]
    for r in ledger.CLOSED_ROWS:
        if r[0] == rid:
            return r[2].split(".")[0], r[1], r[2]
    for r in ledger.balance():
        if r[0] == rid:
            return (REFUSED if r[4] is None else MEASURED,
                    "%s: demand %s; supply %s" % (r[1], r[2], r[3]), None)
    for r in ledger.RULED_BY_M:
        if r[0] == rid:
            return "RULED BY M", r[1], r[3]
    for r in ledger.WITHDRAWN_ROWS:
        if r[0] == rid:
            return WITHDRAWN, r[1], r[2]
    raise KeyError("no ledger row %s" % rid)


def st(rid):
    return row(rid)[0]


def _quiet(fn, *a, **kw):
    """Run an owner's function with its printing swallowed."""
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        out = fn(*a, **kw)
    return out, buf.getvalue()


def _scope_line(doc):
    """The owner's own SCOPE sentence from a docstring, verbatim."""
    m = re.search(r"SCOPE:\s*(.*?\.)", " ".join(doc.split()))
    if not m:
        raise ValueError("owner docstring no longer states a SCOPE")
    return m.group(1)


def duration_scope_split():
    """The duration bound's SCOPE, split into its MATTER-AND-STATE clauses
    (H_M0's) and its SPACETIME clause (H_flat's), so flatness is carried by one
    hypothesis and one escape only.  Raises if the owner's scope no longer has
    exactly one clause naming flat space."""
    items = [s.strip(" .") for s in
             _scope_line(achievable.duration_bound.__doc__).split(",")]
    flat = [s for s in items if "flat" in s]
    matter = [s for s in items if "flat" not in s]
    if len(flat) != 1 or not matter:
        raise ValueError("duration_bound's SCOPE changed shape -- specthm is stale")
    return matter, flat[0]


def _claim_status(doc, letter):
    """The status word an owner's docstring gives its lettered claim, e.g.
    '(a) REGULAR CENTRE, FORMAL SERIES -- THEOREM': asked, not retyped."""
    m = re.search(r"\(%s\) [^\n]*? -- (THEOREM|MEASURED|SURVEY|OPEN)" % letter, doc)
    if not m:
        raise ValueError("owner no longer states a status for claim (%s)" % letter)
    return m.group(1)


# ====================================================== 2. THE FIGURES

_SLOW = {}


def slow_figures():
    """The owner integrations that take seconds.  Computed once per process;
    nothing in a verdict depends on them, only in the report and selftest."""
    if not _SLOW:
        mu = A("achievable", "M_OVER_B")
        import composite
        # composite FIRST, and composite.phi restored after concentric: an
        # OWNER SIDE EFFECT, recorded not repaired -- concentric._install
        # assigns composite.phi and never restores it, so a composite survey
        # run after a concentric one integrates concentric's potential.
        phi0 = composite.phi
        plus = composite.survey(2.0e-3)     # composite.py's design point
        minus = composite.survey(-2.0e-3)
        try:
            below = concentric_survey(0.6 * mu)   # the table row concentric prints
            at = concentric_survey(mu)
        finally:
            composite.phi = phi0
        spec_rc, _ = _quiet(spec.selftest)
        _SLOW.update(concentric_below=below, concentric_at=at,
                     composite_plus=plus, composite_minus=minus,
                     composite_phi_restored=(composite.phi is phi0),
                     spec_selftest_ok=(spec_rc == 0),
                     theorem2=phase1.no_momentum())
    return _SLOW


def concentric_survey(m):
    import concentric
    r = concentric.survey(m)
    return {"seats": r["seats"], "leads": r["leads"],
            "inside_shell": r["inside_shell"]}


def S_ratio(b, mu=None, alpha=None):
    """demanded / allowed on the DURATION axis, by achievable.py's OWN functions
    at any (mu, alpha).  persistence_shortfall() fixes (mu, alpha) to the pins;
    this asks the same two functions it divides."""
    mu = A("achievable", "M_OVER_B") if mu is None else mu
    alpha = A("achievable", "A_OVER_B") if alpha is None else alpha
    return achievable.required_density(b, mu, alpha) / achievable.persistence_allow(b)


def S_closed(b, mu, alpha):
    """3 mu b^2 c^3 / (4 pi C alpha^3 hbar G), with achievable.py's constants.
    The closed form is checked against S_ratio, never used in its place."""
    c, G, hb, C = (achievable.C_SI, achievable.G_SI, achievable.HBAR,
                   achievable.FEWSTER_C)
    return 3.0 * mu * b * b * c ** 3 / (4.0 * math.pi * C * alpha ** 3 * hb * G)


def figures():
    """Every number the reading prints, asked or composed from asks."""
    mu, alpha = A("achievable", "M_OVER_B"), A("achievable", "A_OVER_B")
    b1 = 1.0
    S1 = S_ratio(b1)
    pts = ((1.0, mu, alpha), (1.0e3, 1.0e-2, 0.1), (1.0e-6, 2.0e-3, 0.5),
           (4.0e16, 1.0e-4, 0.02))
    closed_rel = max(abs(S_closed(*p) / S_ratio(*p) - 1.0) for p in pts)
    lam = phase1.lam()                                  # R_s/b = 200, a/b = 0.02
    c, G = achievable.C_SI, achievable.G_SI
    dd_owner = phase1.contraction_law(mu * b1 * c * c / G)   # Delta d of the family
    lin = S_ratio(b1, 2.0 * mu) / S_ratio(b1, mu)
    dd_x = dd_owner / S1
    sun = [x for x in spec.LENSES if x[0] == "Sun"][0]
    ast = [x for x in spec.LENSES if x[0] == "10 km asteroid"][0]
    f_sun = spec.focal_length(sun[1], sun[2])
    f_ast = spec.focal_length(ast[1], ast[2])
    scales = (1.0, 1.0e5, 1.0e8, 1.0e11)
    soc = [spec.seat_over_collapse(l) for l in scales]
    d3 = foliation.d3_table()[-1]
    fs = fewsterteo.refused_figures()
    tube_w_over_l = 1.0e-2
    l_t = 1.0
    u_t = seatindex.tkk_required(l_t)
    M_t = u_t * math.pi * (tube_w_over_l * l_t) ** 2 * l_t / spec.C_SI ** 2
    tube_rs_over_w = 2.0 * spec.G_SI * M_t / spec.C_SI ** 2 / (tube_w_over_l * l_t)
    return {
        "mu": mu, "alpha": alpha, "S1": S1, "log10S1": math.log10(S1),
        "closed_rel": closed_rel, "closed_points": len(pts),
        "demand_Pa": achievable.required_density(b1),
        "allow_Pa": achievable.persistence_allow(b1),
        "b_x": achievable.persistence_crossing(),
        "b_x_lP": achievable.persistence_crossing() / achievable.L_PLANCK,
        "fewster_C": achievable.FEWSTER_C, "fewster_mu1": achievable.FEWSTER_MU1,
        "flat_orders": A("fewsterteo", "FLAT_SHORTFALL_ORDERS"),
        "refused_curved": fs[1],
        "Lambda": lam, "Lambda_is_overturn": lam == A("overturn", "LAMBDA"),
        "dd_owner": dd_owner, "dd_owner_is_mu_b_Lambda":
            abs(dd_owner / (mu * b1 * lam) - 1.0),
        "S_linear_in_mu": lin, "dd_x": dd_x,
        "b_over_lG": math.sqrt(A("noise", "B_OVER_LG_SQUARED")),
        "f_sun_m": f_sun, "f_sun_AU": f_sun / spec.AU,
        "published_sun_AU": published_sun_au(),
        "lenses": [(n, spec.focal_length(M, b), spec.focal_length(M, b) / spec.AU)
                   for n, M, b in spec.LENSES],
        "f_ast_ly": f_ast / spec.LIGHT_YEAR,
        "soc": soc, "soc_scales": scales,
        "soc_const": max(abs(x / soc[0] - 1.0) for x in soc),
        "exchange": ledger.EXCHANGE_RATE,
        "proxima_ly": ledger.PROXIMA_LY,
        "S9_orders": math.log10(warpfolder.shortfall(warpfolder.PAYLOADS_KG[0])),
        "disp_W2": nonstatic.displacement_fraction(2.0),
        "milne": foliation.milne_row(100.0),
        "shapiro": foliation.shapiro(1.0, 10.0, 100.0)["excess"],
        "d3_frac": d3[3],
        "plummer_outside": 1.0 - (1.0 + (certify.A_CORE / certify.R_SHELL) ** 2) ** -1.5,
        "certify_negm": certify.conformastatic_forces_negative_mass(),
        "certify_iff": certify.theorem_holds(),
        "tube_w_over_l": tube_w_over_l, "tube_rs_over_w": tube_rs_over_w,
    }


def published_sun_au():
    """The published solar focus as spec.py cites it ('~550 AU'), read from
    spec's own source -- spec's selftest prints it and compares nothing with it."""
    m = re.search(r"published solar gravitational lens focus(?: is)?:?\s*~(\d+)",
                  open(spec.__file__, encoding="utf-8").read())
    if not m:
        raise ValueError("spec.py no longer cites a published solar focus")
    return float(m.group(1))


def sr2_identity():
    """SR2's ratio is scale-free EXACT algebra: the owners' two coefficients are
    identified as pi c^4/(4G) (seatindex.T_COEFF) and 3 c^4/(8 pi G)
    (spec.collapse_bound * l^2), and their quotient is 2 pi^2/3 in sympy."""
    import sympy as sp
    c4G = spec.C_SI ** 4 / spec.G_SI
    k_seat = seatindex.T_COEFF / (seatindex.C_SI ** 4 / seatindex.G_SI)
    k_coll = spec.collapse_bound(1.0) / c4G
    seat_is = abs(k_seat / float(sp.pi / 4) - 1.0) < 1e-12
    coll_is = abs(k_coll / float(3 / (8 * sp.pi)) - 1.0) < 1e-12
    exact = sp.simplify((sp.pi / 4) / (sp.Rational(3, 8) / sp.pi))
    return seat_is, coll_is, exact


# ================================================ 3. HYPOTHESES, BY NAME

def hypotheses():
    """Every named hypothesis, (text, kind).  Where an owner states it, its own
    words are asked.  KIND: DEFINING restricts a class or object; ASSUMED is a
    claim about physics that nothing proves; OWNER is an owner theorem's."""
    return {
        "H_sph": (formation.H_SPH, "DEFINING"),
        "H_R1": ("'contracts' means %s (foliation.INVARIANT_CRITERION), the "
                 "definition R1, at EVERY point of K.  This is narrower than "
                 "phase1's integrated D3 (d_s(A,B) decreasing): a corridor "
                 "contracted on a proper sub-region K' only is not a member of C "
                 "over K, and K' itself -- in spherical symmetry a shell between "
                 "two areal radii, i.e. two places -- is priced as its own C"
                 % foliation.INVARIANT_CRITERION, "DEFINING"),
        "H_EFE": (formation.H_EFE + " -- its tt component dm/dr = 4 pi r^2 rho",
                  "OWNER"),
        "H_reg": ("regular centre, m(0) = 0 (drivensource.CERTIFY_COROLLARY: "
                  "'%s')" % drivensource.CERTIFY_COROLLARY, "DEFINING"),
        "H_M0": ("the negative energy is carried by the matter, in the state, of "
                 "the duration bound's own SCOPE: %s (achievable.duration_bound; "
                 "its remaining clause, '%s', is H_flat's and is not repeated here)"
                 % (", ".join(duration_scope_split()[0]), duration_scope_split()[1]),
                 "DEFINING"),
        "H_model": ("achievable.py's model: a UNIFORM negative-density core of "
                    "radius alpha*b carrying M = mu*b*c^2/G "
                    "(achievable.required_density)", "DEFINING"),
        "H_static": ("the density is held below its value at each point for the "
                     "whole hold b/c (achievable.hold_time); the corridor's "
                     "staticity supplies THIS and nothing else", "DEFINING"),
        "H_S": ("S(b; mu, alpha) > 1, the amount and scale at which D7 refuses",
                "DEFINING"),
        "H_flat": ("the flat-space, boundary-free duration QEI holds pointwise "
                   "on the curved corridor.  noise.py's H2 is '%s' and on the "
                   "corridor it %s" % (noise.HYPOTHESES["H2"][0],
                                       "FAILS" if not noise.H2_SATISFIED_BY_CORRIDOR
                                       else "holds"), "ASSUMED"),
        "H_axial": ("; ".join(axial.HYPOTHESES) + "; INFINITE along z and static "
                    "(axial.py section 4: it does not price a finite corridor, "
                    "PRICES_A_FINITE_CORRIDOR = %s)" % axial.PRICES_A_FINITE_CORRIDOR,
                    "DEFINING"),
        "H_ball": ("uniform energy density u over a BALL of radius l, M = u (4/3) "
                   "pi l^3/c^2 (spec.collapse_bound)", "DEFINING"),
        "H_collapse": ("a region is a black hole iff 2GM/c^2 >= l for that ball "
                       "(spec.collapse_bound's criterion)", "OWNER"),
        "H_cc": ("the interpolating spacetime is causally compact (Borde, READ "
                 "by create.py)", "DEFINING"),
        "H_seat": ("what S-1's membership rests on: the weak-field focal formula "
                   "(SR1, MEASURED); a NULL congruence -- a massive payload's "
                   "focus is velocity-dependent and computed by NO OWNER; impact "
                   "parameter b >= the lens radius; the causal step 'conjugate "
                   "point => not achronal' (CITED, escape causal-step); and the "
                   "endpoint gate (R5-S, CHECKED, a code path, not a theorem)",
                   "DEFINING"),
    }


# ==================================================== 4. THE OBJECTS

def objects(F):
    sf = slow_figures()
    return [
        {"id": "C", "name": "the contracting corridor (the demand column's object)",
         "definition":
            "A region K between two FIXED PLACES A and B -- a place is a fixed "
            "areal radius (nonstatic.py's anchor lemma) -- on which proper "
            "distance is contracted in the sense of R1 at every point, held for "
            "at least one light-crossing b/c (D7).  'At every point' is part of "
            "the definition (H_R1) and is narrower than phase1's integrated D3: "
            "a corridor contracted on a proper sub-region only is priced as a C "
            "over that sub-region.  The quantity acted on is "
            "proper distance, not light time (phase1.py Theorem 1).  m < 0 "
            "locally is compatible with M_ADM >= 0 "
            "(certify.REQUIRES_NEGATIVE_TOTAL_MASS = %s).  The board prices two "
            "realisations.  (i) certify.py's seated metric, Phi(r) = "
            "m/sqrt(r^2+a^2) - m/max(r,R_s), m = %g, a = %g, R_s = %g in "
            "certify's unit; m < 0 at every sampled radius "
            "(conformastatic_forces_negative_mass() = %s) with a regular "
            "centre, but its core is Plummer, NOT uniform: the Plummer density "
            "falls over the scale a (separately, a fraction %.3e of its mass "
            "lies outside R_s, linstab.py's formula), so it is in "
            "class %s under H_M0 and in K2 otherwise -- K1's figure does not "
            "price it until the mean-value step is seated.  (ii) "
            "achievable.py's scale model, (mu, alpha) = (%g, %g): class %s at "
            "b = 1 m under H_M0 (S = 10^%.3f), K6b for b <= b_x."
            % (certify.REQUIRES_NEGATIVE_TOTAL_MASS, certify.M_SEATED,
               certify.A_CORE, certify.R_SHELL, F["certify_negm"],
               F["plummer_outside"], "{realisation_i}", F["mu"], F["alpha"],
               "{realisation_ii}", F["log10S1"]),
         "source": "certify.py, foliation.py, nonstatic.py, achievable.py, "
                   "phase1.py; ledger D1-D4, D7, D11, D14"},
        {"id": "T", "name": "the transition and its passage",
         "definition":
            "phase1.py's TRANSITION: g_s, s in [0,1], on a FIXED manifold, "
            "meeting %s.  D4 as restated on M's ruling M-D64-1 "
            "(phase1.D4_RESTATED_ON_M_RULING = %s); the first wording is kept "
            "('%s').  phase1's D3 is a SLICE statement ('%s'), and a slice "
            "statement is gauge (ledger D3; foliation section 6: with both "
            "mouths anchored at U = 0 the slice length is driven to %.4f%% of "
            "the areal gap, NONSTATIC_ANCHOR_CLOSES_D3 = %s), so this file "
            "reads T's D3 per R1 -- pointwise invariant contraction on K -- and "
            "records that reading for M (P4).  IF D3 is read per R1 (P4) AND the "
            "endpoint g_1 is held for one light-crossing b/c (D7 -- phase1's "
            "D1-D5 contain no hold requirement), g_1 is an instance of C and "
            "every C verdict applies to it; without the hold it lies outside C, "
            "and D7 says it transmits nothing.  The PASSAGE "
            "the board prices is formation.py's family, f: 0 (flat) -> 1 "
            "(certify's metric), areal radii held fixed (U = 0), on R^3 -- no "
            "topology change."
            % ("; ".join("%s %s" % (c[0], c[1]) for c in phase1.CONDITIONS),
               phase1.D4_RESTATED_ON_M_RULING, phase1.D4_AS_FIRST_WRITTEN,
               [c[2] for c in phase1.CONDITIONS if c[0] == "D3"][0],
               100.0 * F["d3_frac"], foliation.NONSTATIC_ANCHOR_CLOSES_D3),
         "source": "phase1.py, formation.py, foliation.py; ledger M-D64-1"},
        {"id": "S", "name": "M's scoped seat",
         "definition":
            "M's ruling as spec.py records it: 'DROP THE LEAD.  KEEP THE SEAT.'  "
            "What is required is that the matter exist at both ends and "
            "traverse under the same physics.  As spec.DOES (the tuple, which "
            "this file uses) specifies it: %s.  DOES NOT: %s.  'Not required "
            "to contract' is a READING of M's quotation ('nothing else'), not "
            "spec.py's text -- the word 'contract' occurs in spec.py: %s -- and "
            "is listed for M (P1).  S IS NOT A TRANSITION: a positive lens "
            "mass lengthens proper distance (certify.theorem_holds() = %s: "
            "contraction iff m < 0), so S fails phase1's D3.  R5-S and SR1 "
            "constrain the NULL congruence; the focus of a massive payload's "
            "congruence is velocity-dependent and computed by no owner (OPEN, "
            "NO OWNER).  The payload's own motion -- free fall or propelled -- "
            "is part of S and is not the propulsion OPERATOR phase1 excludes "
            "(D1: 'Nothing is transported anywhere by the operator itself').  "
            "WITHDRAWN inside spec.py and not part of S: the Sturm-universal "
            "B*l specification, the magnetar figure, and the ANEC-protects-"
            "achronality line (struck, anecscope.py).  STALE TEXT IN THE OWNER, "
            "recorded not repaired: spec.py's prose DOES paragraph still says "
            "'UNIVERSAL in Sturm's sense' (%s) and spec.report() still prints "
            "the struck ANEC line and the withdrawn 65 orders (%s)."
            % ("; ".join(spec.DOES), "; ".join(spec.DOES_NOT),
               "contract" in open(spec.__file__, encoding="utf-8").read().lower(),
               F["certify_iff"],
               "UNIVERSAL in Sturm" in spec.__doc__,
               "65 orders" in _source(spec.report)),
         "source": "spec.py (DOES, DOES_NOT, focal_length, LENSES, "
                   "seat_over_collapse, HALTED), turnseat.py, composite.py, "
                   "seatindex.py"},
        {"id": "W", "name": "the throat gate",
         "definition":
            "A shortcut through non-simply-connected spatial topology.  It is "
            "not a transition: create.which_fails() = %s, on topology "
            "(fails_on_topology() = %s) -- R^3 is simply connected and a "
            "wormhole is not.  It is excluded from R2 on THAT ground only.  At "
            "the throat itself m = %s (throatmass.THROAT_MASS); in HPS's "
            "conserved system the flare carries m < 0 from %.4f l_P "
            "(hpscentre, %s reading, outside the established domain).  Two "
            "routes, split as create.py splits them: CREATE (topology change) "
            "and FIND-AND-ENLARGE (a metric change, "
            "theorems_apply_to_enlargement() = %s)."
            % (create.which_fails(), create.fails_on_topology(),
               throatmass.THROAT_MASS, hpscentre.FIRST_NEGATIVE_M_THROAT_LP,
               hpscentre.THROAT_M_NEGATIVE_READING,
               create.theorems_apply_to_enlargement()),
         "source": "create.py, throatmass.py, hpscentre.py, formation.py; ledger D24"},
        {"id": "Rec", "name": "the reconstruction route",
         "definition":
            "Ledger S5: specification, not mass.  No mass traverses, so D1-D4 "
            "and D7 are not instantiated.  A specification is carried to the "
            "destination and re-assembled from stock already there; by D23 the "
            "fabricator, the stock survey and the receiver all reached the "
            "destination at <= c first, so it is an AMORTISATION scheme with a "
            "minimum setup of the light time (%.4g years at Proxima).  D25's "
            "stock gate must hold at the destination." % F["proxima_ly"],
         "source": "ledger S5, D13, D21, D23, D25, O3, O6, O7; transit.py, "
                   "stockgate.py, branelink.py, warpfolder.py"},
    ]


def _source(fn):
    import inspect
    return inspect.getsource(fn)


B_ROWS = ("B1", "B2", "B3", "B4")


def b_rows_sentence():
    """R12's headline sentence, only when every balance row is REFUSED; any
    other state of the four rows is printed row by row and marked RE-ASK."""
    sts = [st(b) for b in B_ROWS]
    if all(x == REFUSED for x in sts):
        return ("OVER THE MECHANISMS EXAMINED no mechanism supplies negative "
                "enclosed mass at all (%s: each %s, no ladder)."
                % (", ".join(B_ROWS), REFUSED))
    return ("RE-ASK: the balance rows are no longer all %s (%s)."
            % (REFUSED, ", ".join("%s %s" % (b, x) for b, x in zip(B_ROWS, sts))))


# ============================================== 5. THE REQUIREMENTS

def requirements(F):
    """One requirement per question.  `rows` are the ledger rows PLACED here
    (each row is placed exactly once across all requirements); `see` are rows
    referenced but placed elsewhere.  `status` is built from asks."""
    sf = slow_figures()
    d7 = st("D7")
    h_flat_status = (ASSUMED if not (noise.H2_SATISFIED_BY_CORRIDOR
                                     or fewsterteo.O2_CLOSED) else RE_ASK)
    r12_status = THEOREM if candidates.LIST_IS_EXHAUSTIVE else SURVEY
    sr2 = sr2_identity()
    sr2_status = (THEOREM if (all(sr2) and min(F["soc"]) > 1.0
                              and F["soc_const"] < 1e-12) else OPEN)
    unread = (phase1.is_transition(False, True, True, True, True, passage_flux=True)
              == phase1.is_transition(False, True, True, True, True, passage_flux=False))
    below, at = sf["concentric_below"], sf["concentric_at"]
    return [
        {"id": "R1", "applies_to": ["C", "T"], "kind": DEFINITION,
         "title": "WHAT 'CONTRACTS' MEANS -- the definition R2 is read from",
         "status": "%s (the definition); the equivalence it rests on: D2 %s, "
                   "D3 %s" % (DEFINITION, st("D2"), st("D3")),
         "rows": ["D3", "D10"], "see": ["D2"],
         "owners": [("foliation", "INVARIANT_CRITERION"), ("foliation", "GAMMA_RANGE"),
                    ("foliation", "ONLY_INVARIANT"), ("driven", "CONTRACTION_IS_A_SCALAR"),
                    ("foliation", "NONSTATIC_ANCHOR_CLOSES_D3"),
                    ("nonstatic", "SUSTAINING_FORCES_NEGATIVE_RHO"),
                    ("nonstatic", "QUASI_STATIONARY_CORRIDOR_EXISTS")],
         "hypotheses": ["H_sph", "untrapped (%s)" % foliation.GAMMA_RANGE,
                        "contraction measured against the areal increment dR",
                        "outside spherical symmetry the only invariant criterion "
                        "any owner writes is axial.CONTRACTION_FACTOR ('%s'); "
                        "for a general spacetime: NO OWNER" % axial.CONTRACTION_FACTOR],
         "statement":
            "'The corridor contracts' is a statement about the spacetime.  In 4D "
            "spherical symmetry the only foliation-invariant content of "
            "(U, Gamma) is %s, and Gamma ranges over %s (foliation.GAMMA_RANGE).  "
            "So contraction at a point is DEFINED as Gamma > 1 in every foliation, "
            "and foliation.INVARIANT_CRITERION reads '%s'.  This is R2 read from the "
            "other side and is not counted as a second constraint.  A one-slice "
            "criterion is gauge (driven.CONTRACTION_IS_A_SCALAR = %s): Milne, "
            "exactly flat, gives Gamma = %g with advance over flat %g; in "
            "Schwarzschild the slice between areal radii 10M and 100M, mouths "
            "anchored at U = 0, is driven to %.4f%% of the gap while the signal "
            "keeps its %.3f M Shapiro DELAY -- the anchor lemma does not close "
            "the integrated criterion (NONSTATIC_ANCHOR_CLOSES_D3 = %s).  WHY "
            "THE DEFINITION IS NOT A MERE CHOICE (D10, nonstatic.py): "
            "sustaining a slice contraction does not force rho < 0 "
            "(SUSTAINING_FORCES_NEGATIVE_RHO = %s), but with m >= 0 the far end "
            "must move, |U| >= sqrt(W^2 - 1), displacing the destination by at "
            "least sqrt(1 - 1/W^2) of the gap -- %.1f%% at W = 2 -- and "
            "QUASI_STATIONARY_CORRIDOR_EXISTS = %s."
            % (foliation.ONLY_INVARIANT, foliation.GAMMA_RANGE,
               foliation.INVARIANT_CRITERION, driven.CONTRACTION_IS_A_SCALAR,
               F["milne"]["gamma"], F["milne"]["advance_over_flat"],
               100.0 * F["d3_frac"], F["shapiro"],
               foliation.NONSTATIC_ANCHOR_CLOSES_D3,
               nonstatic.SUSTAINING_FORCES_NEGATIVE_RHO, 100.0 * F["disp_W2"],
               nonstatic.QUASI_STATIONARY_CORRIDOR_EXISTS)},

        {"id": "R2", "applies_to": ["C"],
         "title": "NEGATIVE ENCLOSED MISNER-SHARP MASS at every point of the corridor",
         "status": "D1 %s (static); D2 %s (any foliation); O4 '%s' (infinite "
                   "axial throat)" % (st("D1"), st("D2"), st("O4")),
         "rows": ["D1", "D2", "D8", "D9", "O4"], "see": [],
         "owners": [("certify", "THEOREM_SCOPE"), ("certify", "REQUIRES_NEGATIVE_TOTAL_MASS"),
                    ("foliation", "IDENTITY_DISPUTED"), ("tolman", "RESTATES_CERTIFY_ON_SMALLER_CLASS"),
                    ("tolman", "SUPERSEDES_CERTIFY"), ("axial", "THEOREM"),
                    ("axial", "AXIS_ESCAPES_THE_SIGN"), ("axial", "PRICES_A_FINITE_CORRIDOR")],
         "hypotheses": ["H_sph (static for D1: certify.THEOREM_SCOPE = '%s'; any "
                        "foliation for D2)" % certify.THEOREM_SCOPE,
                        "or H_axial, for the infinite throat only",
                        "untrapped: 1 - 2m/R > 0, automatic where m < 0"],
         "statement":
            "In any static spherically symmetric spacetime proper distance is "
            "contracted at r iff m(r) < 0, ansatz-free (D1).  With staticity "
            "deleted, Gamma > 1 in every foliation iff m < 0 (D2, "
            "foliation.IDENTITY_DISPUTED = %s).  tolman.py's pointwise test "
            "restates this on a strictly smaller class and adds no constraint "
            "(D8: RESTATES_CERTIFY_ON_SMALLER_CLASS = %s; D9: "
            "SUPERSEDES_CERTIFY = %s).  On an INFINITE static cylindrical throat "
            "(translation-invariant in z), %s, so any axial contraction forces "
            "u < 0 somewhere (AXIS_ESCAPES_THE_SIGN = %s); a conical excess "
            "restates the requirement.  axial.py does not price a finite "
            "corridor (PRICES_A_FINITE_CORRIDOR = %s): finite axial corridors "
            "are K5.  The requirement does NOT demand negative total mass "
            "(certify.REQUIRES_NEGATIVE_TOTAL_MASS = %s).  It is NOT a "
            "constraint on S (a positive lens does not contract) nor on W "
            "(excluded from T on topology)."
            % (foliation.IDENTITY_DISPUTED, tolman.RESTATES_CERTIFY_ON_SMALLER_CLASS,
               tolman.SUPERSEDES_CERTIFY, axial.THEOREM, axial.AXIS_ESCAPES_THE_SIGN,
               axial.PRICES_A_FINITE_CORRIDOR, certify.REQUIRES_NEGATIVE_TOTAL_MASS)},

        {"id": "R3", "applies_to": ["C"],
         "title": "A REGULAR CENTRE, if negative enclosed MASS is to mean negative enclosed ENERGY",
         "status": "D4 %s" % st("D4"),
         "rows": ["D4"], "see": [],
         "owners": [("drivensource", "CERTIFY_COROLLARY"), ("drivensource", "OVERTURN_L2"),
                    ("drivensource", "SCOPE"), ("drivensource", "EM_CLOSED_BY")],
         "hypotheses": ["H_sph", "H_EFE",
                        "electrovac sub-case: drivensource.SCOPE = '%s', and the "
                        "body's own (bare) contribution to M non-negative"
                        % drivensource.SCOPE,
                        "the interior step also needs rho >= 0 at every point of "
                        "the body and a regular centre (drivensource.py section 4)"],
         "statement":
            "With m(0) = 0, dm/dr = 4 pi r^2 rho integrates to m(r) = INT_0^r "
            "4 pi r'^2 rho, so m(R) < 0 forces rho < 0 somewhere inside R.  "
            "Without a regular centre the corollary fails: Reissner-Nordstrom "
            "has m < 0 near r = 0 with rho > 0 everywhere and m(0) = -infinity "
            "(drivensource.CERTIFY_COROLLARY = '%s').  Charged body of radius "
            "a > 0 with non-negative bare mass: r_c <= a, so the m < 0 region "
            "never reaches outside it; and a body with rho >= 0 at every point "
            "and a regular centre has m >= 0 everywhere, so it does not "
            "contract at all and lies in K0 (drivensource.py section 4; closed "
            "by '%s').  The point charge (a = 0) carries a -infinite bare mass, "
            "outside the non-negative-bare-mass hypothesis: it is in K3 "
            "(divergence V6)."
            % (drivensource.CERTIFY_COROLLARY, drivensource.EM_CLOSED_BY)},

        {"id": "R4", "applies_to": ["C"],
         "title": "PERSISTENCE for one light-crossing, and the refusal of it",
         "status": "flat bound: D7 %s (Fewster 1208.5399 eq. (4), %s via "
                   "achievable.py) | its application to C: %s (H_flat; O2 %s) "
                   "| the figure: %s | D22's reading: %s"
                   % (d7, CITED, h_flat_status, st("O2"), MEASURED, st("D22")),
         "rows": ["D6", "D7", "D22", "O2"], "see": [],
         "owners": [("bounds", "DURATION_ROUTE_Z"), ("achievable", "FEWSTER_C"),
                    ("achievable", "VERDICT_KIND"), ("achievable", "VERDICT_IS_A_THEOREM"),
                    ("fewsterteo", "FLAT_SHORTFALL_ORDERS"), ("fewsterteo", "CORRIDOR_SPECTRAL_GAP"),
                    ("fewsterteo", "NINE_64_APPLIES_TO_C_F"), ("fewsterteo", "O2_CLOSED"),
                    ("fewsterteo", "GAP_HYPOTHESIS"), ("fewsterteo", "CORRIDOR_MODE_FUNCTIONS"),
                    ("noise", "CORRIDOR_APPLICATION"), ("noise", "C1_FLAT_THEOREM"),
                    ("noise", "H2_SATISFIED_BY_CORRIDOR"), ("noise", "T1_SURVIVES_SMEARING"),
                    ("noise", "EL_VACUUM_LOG10_NEG_LN_P"), ("noise", "EL_SURROGATE_NONVACUUM_COMPUTED"),
                    ("noise", "DEMAND_RESTATED_ABOUT_DISTRIBUTION_CHANGES_REQUIREMENT"),
                    ("noise", "CURVED_PART_CARRIED_BY")],
         "hypotheses": ["H_M0", "H_flat (ASSUMED)", "H_static", "H_model", "H_reg",
                        "for D22's reading: noise.py's H3 '%s' -- %s"
                        % noise.HYPOTHESES["H3"]],
         "statement":
            "A corridor that does not hold for one light-crossing T = b/c "
            "transmits nothing (D7).  THE FLAT BOUND: if <T_00> stays below rho "
            "for a duration T at a point, rho >= -C hbar/(c^3 T^4), C = "
            "mu_1^4/(16 pi^2) with cos(mu_1) cosh(mu_1) = 1, mu_1 = %.15g, C = "
            "%.15g (bisection, achievable.fewster_constant).  It is a statement "
            "at each point about a DURATION, so Ford-Helfer-Roman (D6: 'NO "
            "purely spatially averaged quantum inequalities over bounded "
            "regions in 4D Minkowski') does not touch it.  ITS APPLICATION TO "
            "C IS "
            "ASSUMED (H_flat): the corridor fails noise.py's H2, b/l_G = %.3f; "
            "bounds.py calls it 'priced on the DURATION axis, by an instrument "
            "of the wrong shape under an extra hypothesis', "
            "achievable.VERDICT_KIND = %s and noise.CORRIDOR_APPLICATION = %s.  "
            "Staticity supplies H_static only.  THE FIGURE, MEASURED: in "
            "achievable.py's model, demanded/allowed is EXACTLY S(b; mu, alpha) "
            "= 3 mu b^2 c^3/(4 pi C alpha^3 hbar G) -- equal to "
            "required_density/persistence_allow to %.1e relative at %d "
            "parameter points.  At the owner's pins (mu, alpha) = (%g, %g), "
            "b = 1 m: %.4e Pa demanded against %.4e Pa allowed, 10^%.3f, i.e. "
            "%.3f + 2 log10(b / 1 m) orders; S = 1 only at b_x = %.4e m = %.4f "
            "l_P, 'l_P times an O(1) number by construction, NOT evidence'.  "
            "WHAT mu = %g IS: %s (concentric.survey at 0.6 mu: seats = %s, "
            "leads = %s; at mu: seats = %s, leads = %s, inside the shell = %s -- "
            "and the lead is interior-only, withdrawn there).  It is not a "
            "contraction threshold: contraction is linear in m for every m > 0.  "
            "ON C's OWN "
            "DEMAND (composed here, section 3): S is linear in mu (S(2mu)/S(mu) "
            "= %.12g), Delta d = (G/c^2) M Lambda with Lambda = %.10g at R_s/b "
            "= %g, a/b = %g (phase1.lam(), = overturn.LAMBDA: %s), so S = "
            "3 Delta d b c^3/(4 pi C alpha^3 hbar G Lambda) and, at b = 1 m "
            "and alpha = %g, under K1's hypotheses (H_flat ASSUMED among them) "
            "and the transition equation's (weak field, MEASURED by phase1.py), "
            "the refusal holds for EVERY contraction Delta d > %.4e m -- the "
            "owner family itself contracts by %.4g m.  The curvature-tightened %.3f is REFUSED: at spectral gap "
            "%g the Fewster-Teo form returns the flat bound, and the 9/64 is "
            "not applied (NINE_64_APPLIES_TO_C_F = %s).  D22, FOLDED IN HERE "
            "(DOCKET 64 D: the requirement is not restated about a "
            "distribution, DEMAND_RESTATED_ABOUT_DISTRIBUTION_CHANGES_REQUIREMENT "
            "= %s): in the flat model H1-H6 the sampled density is bounded "
            "below as an operator (C1_FLAT_THEOREM = %s), so in the flat model "
            "and under H6 the distribution reading refuses exactly the set R4 "
            "refuses; under the Einstein-Langevin surrogate with the VACUUM's "
            "noise kernel the probability is exp(-10^%.3f), nonzero, and a "
            "larger kernel is not computed (EL_SURROGATE_NONVACUUM_COMPUTED = "
            "%s).  On the corridor that reading is a %s; its curved part is "
            "%s's."
            % (F["fewster_mu1"], F["fewster_C"], F["b_over_lG"],
               achievable.VERDICT_KIND, noise.CORRIDOR_APPLICATION,
               F["closed_rel"], F["closed_points"], F["mu"], F["alpha"],
               F["demand_Pa"], F["allow_Pa"], F["log10S1"], F["log10S1"],
               F["b_x"], F["b_x_lP"], F["mu"],
               ("concentric.py's SEAT + LEAD window edge"
                if (below["seats"], at["seats"], at["leads"]) == (False, True, True)
                else "RE-ASK -- the survey no longer places mu at concentric's "
                     "SEAT + LEAD edge"),
               below["seats"], below["leads"],
               at["seats"], at["leads"], at["inside_shell"], F["S_linear_in_mu"],
               F["Lambda"], phase1.R_SHELL / phase1.B_RAY, phase1.A_CORE / phase1.B_RAY,
               F["Lambda_is_overturn"], F["alpha"], F["dd_x"], F["dd_owner"],
               F["refused_curved"], fewsterteo.CORRIDOR_SPECTRAL_GAP,
               fewsterteo.NINE_64_APPLIES_TO_C_F,
               noise.DEMAND_RESTATED_ABOUT_DISTRIBUTION_CHANGES_REQUIREMENT,
               noise.C1_FLAT_THEOREM, noise.EL_VACUUM_LOG10_NEG_LN_P,
               noise.EL_SURROGATE_NONVACUUM_COMPUTED, noise.CORRIDOR_APPLICATION,
               noise.CURVED_PART_CARRIED_BY)},

        {"id": "R5-C", "applies_to": ["C"],
         "title": "A DESTINATION PARAMETER, on the corridor -- NOT used as an exclusion",
         "status": "D14 %s; S6 %s; beyond static spherical and axial: %s"
                   % (st("D14"), st("S6"), NO_OWNER),
         "rows": ["D14", "D15", "D16", "S6"], "see": [],
         "owners": [("certify", "THEOREM_SCOPE"), ("excite", "ROLE1_DOMINATED_BY_OWN_SOURCE"),
                    ("excite", "TAIL_RATE_IS_MASS"), ("excite", "DISPLACEMENT_IS_ULTRALOCAL")],
         "hypotheses": ["static spherical symmetry, for the undefinedness theorem",
                        "the one-bit statement for the axial object is ledger "
                        "text (D14's DOCKET 62 scope flag), not an owner pin"],
         "statement":
            "A static spherically symmetric device has NO parameter in which a "
            "destination can be written; addressing is UNDEFINED on it, not "
            "unanswered (D14).  On the infinite axial object the destination "
            "narrows to a one-bit parameter (ledger D14 text).  What a full 3-D "
            "address requires of a metric is written down nowhere.  A displaced "
            "Higgs vev does not supply one (S6: the source is the better "
            "address, ROLE1_DOMINATED_BY_OWN_SOURCE = %s), because the "
            "displacement returns at rate exactly m_h (D15, TAIL_RATE_IS_MASS "
            "= %s) and is ultralocal (D16, DISPLACEMENT_IS_ULTRALOCAL = %s).  "
            "DOCKET 62 wrote R5 as 'a device that cannot be aimed is not a "
            "device'; D14 proves the destination UNDEFINED, not that the "
            "contraction fails to reach B, and no ruling makes aimability "
            "binding -- so no class is emptied by it (P2)."
            % (excite.ROLE1_DOMINATED_BY_OWN_SOURCE, excite.TAIL_RATE_IS_MASS,
               excite.DISPLACEMENT_IS_ULTRALOCAL)},

        {"id": "R6", "applies_to": ["C"],
         "title": "A MATTER MODEL OUTSIDE H_M0 -- the crack the tree cannot close",
         "status": "D12 %s (a paper; unaskable); S4 = O1 '%s' (one refusal, "
                   "counted once); D17 %s; S8 %s" % (st("D12"), st("O1"),
                                                    st("D17"), st("S8")),
         "rows": ["D12", "D17", "O1", "S4", "S8"], "see": ["S1", "S2", "O5"],
         "owners": [("achievable", "VERDICT_KIND"), ("candidates", "LIST_IS_EXHAUSTIVE"),
                    ("candidates", "NMC_STATE_INDEPENDENT_QEI"), ("candidates", "NMC_COEFFICIENT_STATUS"),
                    ("higgs", "MINIMAL_SCALAR_SATISFIES_NEC"), ("qeihps", "ABSOLUTE_QEI_FOR_NMC")],
         "hypotheses": ["D12's owner is a paper, so no instrument re-asks it "
                        "(ledger.unaskable() = %s)" % ", ".join(ledger.unaskable())],
         "statement":
            "What escapes R4 is matter outside H_M0.  DOCKET 55's four limbs "
            "are each proved inside their own hypotheses and their conjunction "
            "is a SURVEY (D12), because nothing proves the hypothesis sets "
            "exhaust matter.  O1, verbatim: '%s' -- 'it was S4 counted a "
            "second time', so the nonminimally coupled scalar is ONE refusal "
            "here, not two.  O1's two figures (E_pos/|E_neg| >= %s) are "
            "LEDGER TEXT, asked from the row: no instrument "
            "in this tree re-derives them (the selftest greps), so they are not "
            "quoted as MEASURED.  S4's cutoff coefficient is a %s.  An absolute "
            "QEI for NMC is %s.  Any minimally coupled scalar satisfies the NEC "
            "classically (D17, MINIMAL_SCALAR_SATISFIES_NEC = %s), which closes "
            "the Higgs as a source at the endpoint (S8).  Interacting fields: "
            "no state-independent QEI is expected (Fewster Sec. 5.1, as "
            "achievable.py quotes it).  Classical sources: no QEI constrains "
            "them.  O5's only m < 0 candidate, HPS's xi = 1/6 field, is "
            "non-minimally coupled and lies here (K2).  S1 and S2 are placed "
            "in R12."
            % (st("O1"), " and >= ".join("%s at xi = %s" % f for f in o1_figures()),
               candidates.NMC_COEFFICIENT_STATUS, qeihps.ABSOLUTE_QEI_FOR_NMC,
               higgs.MINIMAL_SCALAR_SATISFIES_NEC)},

        {"id": "R7", "applies_to": ["C"],
         "title": "SELF-CONSISTENCY: a SOLUTION of G_ab = 8 pi <T_ab>",
         "status": "O5 %s (hpscentre.O5_CLOSED = %s)" % (st("O5"), hpscentre.O5_CLOSED),
         "rows": ["O5"], "see": [],
         "owners": [("hpscentre", "M_NEGATIVE_FOUND_IN_HPS_SYSTEM"),
                    ("hpscentre", "M_NEGATIVE_FOUND_INSIDE_DOMAIN"),
                    ("hpscentre", "THROAT_M_NEGATIVE_READING"),
                    ("hpscentre", "FIRST_NEGATIVE_M_THROAT_LP"), ("hpscentre", "CENTRE_M_LEADING"),
                    ("hpscentre", "RECURSION_DIRECTION"), ("hpscentre", "LINEAR_CENTRE_THEOREM_SCOPE"),
                    ("hpscentre", "NONLINEAR_CENTRE_NONFLATNESS"),
                    ("hpscentre", "NONLINEAR_CENTRE_ASYMPTOTICS"),
                    ("hpscentre", "HPS_INTEGRATED_THE_PRINTED_SYSTEM"), ("hpscentre", "DOMAIN_WORD"),
                    ("qeihps", "KONTOU_REQUESTED_TEST_ON_HPS"), ("qeihps", "HPS_STATE_HADAMARD_ESTABLISHED"),
                    ("throatmass", "FAMILIES_WITH_NEGATIVE_MASS")],
         "hypotheses": ["G_ab = 8 pi <T_ab> with the Anderson-Hiscock-Samuel <T> "
                        "for HPS's xi = 1/6 field", "the conserved reading of HPS's system",
                        hpscentre.DOMAIN_WORD,
                        "HPS's state established Hadamard: %s"
                        % qeihps.HPS_STATE_HADAMARD_ESTABLISHED],
         "statement":
            "In HPS's CONSERVED system their own throat data have m < 0 in the "
            "flare from %.4f l_P (%s, hpscentre (d), %s reading only).  A "
            "regular centre has %s (%s, hpscentre (a), formal series; %s).  "
            "Every non-flat analytic regular-centre solution of %s changes the "
            "sign of m and is not asymptotically flat (%s, hpscentre (b), for "
            "that system only).  Nonlinear non-flatness is %s; "
            "their asymptotics are %s.  m < 0 FOUND IN HPS's SYSTEM = %s; FOUND "
            "INSIDE THE ESTABLISHED DOMAIN = %s.  Which system HPS integrated: "
            "%s.  Kontou's requested test: %s.  %d of %d families in print "
            "REPORT m < 0 -- true of what was reported."
            % (hpscentre.FIRST_NEGATIVE_M_THROAT_LP, _claim_status(hpscentre.__doc__, "d"),
               hpscentre.THROAT_M_NEGATIVE_READING,
               hpscentre.CENTRE_M_LEADING, _claim_status(hpscentre.__doc__, "a"),
               hpscentre.RECURSION_DIRECTION,
               hpscentre.LINEAR_CENTRE_THEOREM_SCOPE, _claim_status(hpscentre.__doc__, "b"),
               hpscentre.NONLINEAR_CENTRE_NONFLATNESS,
               hpscentre.NONLINEAR_CENTRE_ASYMPTOTICS, hpscentre.M_NEGATIVE_FOUND_IN_HPS_SYSTEM,
               hpscentre.M_NEGATIVE_FOUND_INSIDE_DOMAIN,
               hpscentre.HPS_INTEGRATED_THE_PRINTED_SYSTEM, qeihps.KONTOU_REQUESTED_TEST_ON_HPS,
               throatmass.FAMILIES_WITH_NEGATIVE_MASS, throatmass.SELF_CONSISTENT_FAMILIES_RETURNED)},

        {"id": "R8", "applies_to": ["C"],
         "title": "LINEARISED STABILITY (AMM)",
         "status": "D26 %s; classical radial sector %s; semiclassical: %s"
                   % (st("D26"), linstab.CLASSICAL_RADIAL_STATUS, linstab.SEMICLASSICAL_STATUS),
         "rows": ["D26"], "see": ["O5"],
         "owners": [("linstab", "SEMICLASSICAL_EVALUABLE_ON_DEMAND"),
                    ("linstab", "CLASSICAL_RADIAL_STATUS"), ("linstab", "BETA2_CRIT_INFIMUM"),
                    ("linstab", "DEVICE_IS_WALL_FORMULA_AT_U"), ("linstab", "D26_CLAIM"),
                    ("linstab", "LITERATURE_SPLIT_IS_ONE_CONSTANT")],
         "hypotheses": ["P1-P4 of linstab.py; P2's interior is Schwarzschild with "
                        "M_in = -m down to r = 0, i.e. m(0) != 0: the classical "
                        "THEOREM is about a K3 idealisation, not a regular-centre "
                        "corridor, and is not claimed for concentric.py's Plummer "
                        "potential",
                        "the core's own stability is deferred with the "
                        "identification phase (linstab.py section 2)"],
         "statement": "%s.  inf beta^2_crit = %s." % (linstab.D26_CLAIM,
                                                     linstab.BETA2_CRIT_INFIMUM)},

        {"id": "R10", "applies_to": ["C", "T", "W"],
         "title": "FORMATION: a route from ordinary initial data",
         "status": "D24 %s; part 3 %s; nucleation %s; find-and-enlarge %s"
                   % (st("D24"), formation.STATUS["D24 part 3: F1, F2, transverse bound (this family), D4"],
                      formation.STATUS["D24 nucleation"], formation.STATUS["D24 find-and-enlarge"]),
         "rows": ["D24"], "see": [],
         "owners": [("formation", "F1_THEOREM"), ("formation", "F2_THEOREM"),
                    ("formation", "TRANSVERSE_BOUND"), ("formation", "SEATED_COMPACT_SUPPORT"),
                    ("formation", "NUCLEATION_PRICEABLE_FROM_SOURCE"), ("formation", "NUCLEATION_PRICED"),
                    ("create", "EXOTIC_MATTER_HELPS_CREATION"), ("create", "GEROCH_NEEDS_MATTER_ASSUMPTION"),
                    ("create", "BORDE_DYNAMICS"), ("create", "KINEMATICALLY_POSSIBLE"),
                    ("create", "ROUTE_COST")],
         "hypotheses": ["F1: " + "; ".join(formation.F1_THEOREM),
                        "F2 adds: " + "; ".join(h for h in formation.F2_THEOREM
                                                if h not in formation.F1_THEOREM),
                        "(c) adds: " + "; ".join(h for h in formation.TRANSVERSE_BOUND
                                                 if h not in formation.F1_THEOREM),
                        "(e) rests on papers READ (Geroch, Borde gr-qc/9406053, "
                        "Tipler), not on a module"],
         "statement":
            "(a) F1: across any sphere, a passage from flat space to a "
            "configuration on R^3 holding every areal radius fixed carries the "
            "object's own enclosed negative mass -m_1(R) outward as Kodama "
            "energy, by ANY route, at ANY speed.  (b) F2: every such passage "
            "pays an extra outgoing radial null deficit -(W_1 - 1)/(2 pi R), "
            "independent of duration.  (c) IN formation.py's FAMILY ONLY: the "
            "TIME PART of rho + p_T integrates to <= -(omega^2/8 pi)/tau_p < 0 "
            "at every duration; whether the full transverse integral is "
            "negative is not shown by the owner.  (d) certify.py's seated metric "
            "is not compactly supported (SEATED_COMPACT_SUPPORT = %s), so it "
            "fails phase1's D2.  (e) Creating a throat is topology change: for "
            "causally compact interpolating spacetimes Geroch and Borde force "
            "causality violation kinematically, with no matter assumption "
            "(GEROCH_NEEDS_MATTER_ASSUMPTION = %s, EXOTIC_MATTER_HELPS_CREATION "
            "= %s); dynamically '%s' -- READ, and whether 'reasonable' excludes "
            "the source a throat needs is not determined here.  Topology change "
            "is kinematically possible (KINEMATICALLY_POSSIBLE = %s).  "
            "Nucleation (Pisana et al.) is READ, its price not computed "
            "(NUCLEATION_PRICED = %s), priceability %s.  Find-and-enlarge: %s.  "
            "NO SI FIGURE: certify's unit L is never fixed (formation.py "
            "section 7).  The surface layer at R_s is not priced; every "
            "formation figure lies on one side of it."
            % (formation.SEATED_COMPACT_SUPPORT, create.GEROCH_NEEDS_MATTER_ASSUMPTION,
               create.EXOTIC_MATTER_HELPS_CREATION, create.BORDE_DYNAMICS,
               create.KINEMATICALLY_POSSIBLE, formation.NUCLEATION_PRICED,
               formation.NUCLEATION_PRICEABLE_FROM_SOURCE, create.ROUTE_COST)},

        {"id": "R11", "applies_to": ["Rec"],
         "title": "FOR THE RECONSTRUCTION ROUTE: a destination stock, a receiver, a bit count",
         "status": "D23 %s; D25 %s; S5 %s; D13 %s; O3 %s, O6 %s, O7 %s; D21 %s; S9 %s"
                   % tuple(st(r) for r in ("D23", "D25", "S5", "D13", "O3", "O6",
                                           "O7", "D21", "S9")),
         "rows": ["D13", "D21", "D23", "D25", "S5", "S9", "O3", "O6", "O7"], "see": [],
         "owners": [("transit", "TRAVERSAL_IS_REMOVED"), ("transit", "READING_CARRIES_NOTHING_ALONE"),
                    ("stockgate", "GATE"), ("formation", "APERTURE_STATUS"),
                    ("branelink", "S5_FIGURES_MEASURED"), ("branelink", "S5_OWED"),
                    ("branelink", "O6_CLOSED"), ("branelink", "O7_CLOSED"),
                    ("latticectc", "O3_CLOSED"), ("latticectc", "LATTICE_THEOREM"),
                    ("warpfolder", "FLASH_IS_A_RECONSTRUCTION_MECHANISM"),
                    ("warpfolder", "HEATING_TO_EW_SCALE_RESTORES_SYMMETRY")],
         "hypotheses": ["what is specified, at what fidelity, and whether "
                        "classical or quantum: three rulings unmade (DOCKET 62, "
                        "R11 note)"],
         "statement":
            "The channel must be traversed at <= c to exist, so its advantage "
            "over light is zero by construction (D23; "
            "READING_CARRIES_NOTHING_ALONE = %s, TRAVERSAL_IS_REMOVED = %s): S5 "
            "is an amortisation scheme with a minimum setup of %.4g years at "
            "Proxima, and whether it amortises is OPEN.  D25: '%s' -- the "
            "aperture is %s.  S5: the bit count is owed (%s); the four figures "
            "once seated are not measured (S5_FIGURES_MEASURED = %s).  D13: a "
            "brane-confined carrier travels at <= c in its induced metric "
            "(D13 %s); a bulk carrier is O6/O7, and whether any "
            "braneworld shortcut yields a CTC is O3 (the flat-bulk quotient is "
            "settled by D21).  S9, the Drive folder's device, is a "
            "reconstruction-route specification REFUSED on two counts: short "
            "by %.1f orders ON ITS OWN NUMBERS (the specification against "
            "itself, not a gap against this board's demand), and its mechanism "
            "is inverted (HEATING_TO_EW_SCALE_RESTORES_SYMMETRY = %s)."
            % (transit.READING_CARRIES_NOTHING_ALONE, transit.TRAVERSAL_IS_REMOVED,
               F["proxima_ly"], stockgate.GATE, formation.APERTURE_STATUS,
               branelink.S5_OWED, branelink.S5_FIGURES_MEASURED, st("D13"),
               F["S9_orders"],
               warpfolder.HEATING_TO_EW_SCALE_RESTORES_SYMMETRY)},

        {"id": "R12", "applies_to": ["C"],
         "title": "THE ENGINEERING SIDE for the corridor: a supply that survives its arithmetic",
         "status": "%s (candidates.LIST_IS_EXHAUSTIVE = %s); %s; S1 %s, "
                   "S2 %s, S3 %s; D11 %s"
                   % (r12_status, candidates.LIST_IS_EXHAUSTIVE,
                      ", ".join("%s %s" % (b, st(b)) for b in B_ROWS), st("S1"),
                      st("S2"), st("S3"), st("D11")),
         "rows": ["D11", "B1", "B2", "B3", "B4", "S1", "S2", "S3"], "see": ["S4"],
         "owners": [("candidates", "LIST_IS_EXHAUSTIVE"), ("candidates", "REQUIREMENT_SCALES_AS"),
                    ("overturn", "LAMBDA")],
         "hypotheses": ["the exchange rate c^2/(G Lambda) is certify's geometry: "
                        "Lambda = 2[ln(2 R_s/sqrt(b^2+a^2)) - 1] at R_s/b = %g, "
                        "a/b = %g (phase1.lam), improvable only logarithmically; "
                        "D11 is a corpus question, not a physics one"
                        % (phase1.R_SHELL / phase1.B_RAY, phase1.A_CORE / phase1.B_RAY)],
         "statement":
            "%s  The corridor "
            "demands %.6g kg per metre of contraction (ledger.EXCHANGE_RATE) "
            "and %s over the Proxima span.  S1 is refused on KIND, S2 because "
            "the Casimir sign inverts for real mirrors, S4 on the EFT cutoff "
            "(placed in R6); S3 (squeezed vacuum) is %s: passes KIND and "
            "DEADLINE, fails MAGNITUDE.  The mechanism list is not exhaustive, "
            "so this is a %s.  DOCKET 62's 'the tree can PROVE the right side "
            "is empty' is not used (divergence V5)."
            % (b_rows_sentence(),
               F["exchange"], [r for r in ledger.balance() if r[0] == "B2"][0][2],
               st("S3"), r12_status)},

        {"id": "RT", "applies_to": ["T"],
         "title": "THE TRANSITION, with D4 as M restated it (M-D64-1)",
         "status": "%s; the passage statement %s (formation.py, F1's hypotheses)"
                   % (st("M-D64-1"), formation.STATUS["D24 part 3: F1, F2, transverse bound (this family), D4"]),
         "rows": ["M-D64-1"], "see": ["D24"],
         "owners": [("phase1", "D4_RESTATED_ON_M_RULING"), ("phase1", "D4_AS_FIRST_WRITTEN"),
                    ("phase1", "CONDITIONS"), ("formation", "PHASE1_D4_POINTWISE_DURING_PASSAGE"),
                    ("formation", "SEATED_COMPACT_SUPPORT")],
         "hypotheses": ["for the passage statement: F1's hypotheses",
                        "D4 (i) for static configurations is phase1 Theorem 2; its "
                        "selftest checks ONE POINT of ONE configuration "
                        "(no_momentum() = %s)" % sf["theorem2"],
                        "D2 is NOT met by certify's seated metric; whether any "
                        "m < 0 configuration is compactly supported is decided "
                        "by NO OWNER"],
         "statement":
            "D4: (i) T^{0i} = 0 in every configuration g_s; (ii) zero NET "
            "momentum across any passage.  Every U = 0 spherically symmetric "
            "passage from flat space has T^{0r} != 0 at some instant wherever "
            "m_1 != 0 (PHASE1_D4_POINTWISE_DURING_PASSAGE = %s), radially, with "
            "zero net momentum: it meets D4 (ii) and is not propulsion.  In "
            "phase1.is_transition the passage clause is accepted BY DEFINITION: "
            "the passage_flux parameter is unread (%s).  A device that thrusts "
            "fails D4 (ii) (is_transition(net_momentum=True) = %s); Alcubierre "
            "fails D4 (i) (alcubierre_is_propulsion() = %s).  phase1 Theorem 4 "
            "('never a lead') presupposes D2 and agents acting in a compact "
            "region; formation.py's family meets neither, so no owner decides "
            "whether that passage can lead -- and a lead is not required.  "
            "Theorem 5 (all value in amortisation) is likewise not required by "
            "M's scope."
            % (formation.PHASE1_D4_POINTWISE_DURING_PASSAGE, unread,
               phase1.is_transition(False, True, True, True, True, net_momentum=True),
               phase1.alcubierre_is_propulsion())},

        {"id": "R5-S", "applies_to": ["S"],
         "title": "SEAT, PARTS 1 AND 3 -- both endpoints at onset, the turn lands on the arrival",
         "status": CHECKED + "; spec selftest %s" % ("OK" if sf["spec_selftest_ok"] else "FAILED"),
         "rows": [], "see": [],
         "owners": [("spec", "DOES")],
         "hypotheses": ["the gate is a checked code path (turnseat.part2 returns "
                        "BLOCKED without a declared arrival; spec's selftest), "
                        "not a proved theorem"],
         "statement":
            "Both endpoints are given at onset: turnseat.py's part 2 does not "
            "initialise without an arrival, and spec.py's selftest checks that "
            "gate.  The range is the lens's focal length (SR1)."},

        {"id": "SR1", "applies_to": ["S"],
         "title": "SEAT, PART 2 -- a conjugate point at a chosen range, from ordinary matter",
         "status": MEASURED + " (spec.focal_length; spec selftest %s)"
                   % ("OK" if sf["spec_selftest_ok"] else "FAILED"),
         "rows": [], "see": [],
         "owners": [("spec", "DOES"), ("spec", "LENSES")],
         "hypotheses": ["weak field", "positive lens mass M",
                        "source outside the focal length (composite.py: a real image forms)",
                        "impact parameter b >= the lens radius, so the congruence "
                        "passes through vacuum",
                        "a NULL congruence; a massive payload's focus is "
                        "velocity-dependent and computed by NO OWNER"],
         "statement":
            "spec.DOES: '%s'.  Each null geodesic passing a positive lens mass "
            "M at impact parameter b >= the lens radius has a conjugate point at "
            "f(b) = b^2 c^2/(4 G M) (the source-at-infinity focus), through "
            "vacuum, NEC, WEC and DEC satisfied everywhere.  f grows with b "
            "(spherical aberration): at a given B only the rays of ONE impact "
            "parameter reconverge on the axis -- a focal line, not a point focus "
            "of the whole congruence -- and f(R_lens) is the lens's MINIMUM "
            "range, so a declared range must be >= f(R_lens).  The Sun at b = "
            "R_sun gives f = %.5e m = %.2f AU; spec's selftest pins f to its "
            "own figure at 1e-3, and spec cites the published value, ~550 AU "
            "(%.2f%% apart, computed here from spec's figure and pinned by no "
            "selftest).  %s.  Weyl focusing is sign-blind (composite.py); Ricci "
            "focusing needs T_kk > 0, which ordinary matter has."
            % ("; ".join(spec.DOES), F["f_sun_m"], F["f_sun_AU"],
               100.0 * abs(F["f_sun_AU"] / F["published_sun_AU"] - 1.0),
               "; ".join("%s %.5g AU" % (n, au) for n, _f, au in F["lenses"]
                         if n != "10 km asteroid")
               + "; 10 km asteroid %.1f ly" % F["f_ast_ly"])},

        {"id": "SR2", "applies_to": ["S"],
         "title": "SEAT -- a device, not a black hole",
         "status": sr2_status + " (uniform ball; exact algebra, sympy)",
         "rows": [], "see": [],
         "owners": [("seatindex", "T_COEFF")],
         "hypotheses": ["H_ball", "H_collapse"],
         "statement":
            "The seating region must not lie inside its own Schwarzschild "
            "radius.  For a uniform BALL of radius l, seating needs u >= "
            "pi c^4/(4 G l^2) (seatindex.T_COEFF) and avoiding collapse needs "
            "u < 3 c^4/(8 pi G l^2) (spec.collapse_bound), so u_seat/u_collapse "
            "= %s = %.10g at l = %s m (constant to %.1e).  Cumulative "
            "weak-field lensing meets it: the Sun is not inside its "
            "Schwarzschild radius.  A non-ball region (a tube) is not covered: "
            "see escape H_ball."
            % (sr2[2], F["soc"][0], ", ".join("%g" % l for l in F["soc_scales"]),
               F["soc_const"])},

        {"id": "SR3", "applies_to": ["S"],
         "title": "M's SCOPE CLAUSE -- no lead required, traversal under the same physics",
         "status": "D5 %s (its owner a paper, Olum PRL 81 3567: unaskable by any "
                   "instrument here); the causal-structure step %s; the delay figure "
                   "%s (composite.survey)" % (st("D5"), CITED, MEASURED),
         "rows": ["D5"], "see": [],
         "owners": [("spec", "DOES_NOT")],
         "hypotheses": ["'conjugate point => not achronal' is a standard "
                        "causal-structure result spec.DOES states and no owner "
                        "re-proves (CITED); it makes B timelike-reachable only for "
                        "B strictly past the focus",
                        "D5's owner is a paper (Olum PRL 81 3567); ledger.unaskable() "
                        "lists it: %s" % ("D5" in ledger.unaskable())],
         "statement":
            "No lead is required (M: 'DROP THE LEAD').  None is available from "
            "ordinary matter: a lead needs negative energy (D5, %s, owner a "
            "paper, no symmetry assumed), which is C's open question (K2, K3, "
            "S-3) -- "
            "D5 does not say negative energy is unavailable.  The traversal "
            "half of M's scope is met by any subluminal trajectory, lens or "
            "not; the seat's own content is SR1.  A positive-mass lens delays "
            "its signal (composite.survey(+2e-3): delay %+.4e, seats = %s); the "
            "same mass negative seats and arrives early (early = %s), which "
            "needs negative mass and so is C's question."
            % (st("D5"), sf["composite_plus"]["delay"], sf["composite_plus"]["seats"],
               sf["composite_minus"]["early"])},

        {"id": "SR4", "applies_to": ["S"],
         "title": "THE MATTER EXISTS AT BOTH ENDS under the same physics",
         "status": "D18 %s; D19 %s; S7 %s; D20 %s" % (st("D18"), st("D19"),
                                                     st("S7"), st("D20")),
         "rows": ["D18", "D19", "D20", "S7"], "see": [],
         "owners": [("excite", "ELECTRON_MASS_IS_A_RULER"), ("excite", "FLAT_DIRECTIONS_ARE_INERT"),
                    ("excite", "ROLE2_REBINDS")],
         "hypotheses": ["D18: '%s'" % excite.ELECTRON_MASS_IS_A_RULER,
                        "residual channels O(eps) through m_p/m_e (S7 prices them)"],
         "statement":
            "S-1's seat displaces no field: the lens is ordinary positive mass "
            "(spec.DOES), so the payload is ordinary matter at both ends.  For "
            "an endpoint displaced along the Higgs, the board already has the "
            "existence half: m_e -> m_e(1 + eps) with alpha fixed is an exact "
            "dilation, the object is its own ruler (D18: %s); flat directions "
            "are inert (D19: FLAT_DIRECTIONS_ARE_INERT = %s); rebinding never "
            "happens, only an O(eps) shift (S7: ROLE2_REBINDS = %s); holding "
            "eps costs what D20 measures."
            % (excite.ELECTRON_MASS_IS_A_RULER, excite.FLAT_DIRECTIONS_ARE_INERT,
               excite.ROLE2_REBINDS)},
    ]


# ============================================ 6. THE CLASSES AND FACTS

FEATURE_TEXT = {
    # C space
    "sph": "4D spherical symmetry",
    "axial": "infinite static cylindrical symmetry (axial.HYPOTHESES)",
    "negm": "m < 0 at every point of K",
    "reg": "regular centre",
    "m0": "negative energy carried by H_M0 matter",
    "model": "uniform core held static (H_model, H_static)",
    "sgt1": "S(b; mu, alpha) > 1",
    # S space
    "wl": "cumulative weak-field lensing of positive mass through vacuum",
    "ball": "Sturm seating by uniform u over a ball of radius l",
    # W space
    "created": "brought into existence (topology change)",
    "cc": "causally compact",
}


def classes():
    """The partition.  `lits` define the class (and generate its printed
    definition); `hyps` is what the class STATES -- the selftest checks it
    against what the z3 proof used."""
    return [
        {"id": "K0", "object": "C", "space": "C", "lits": {"sph": True, "negm": False},
         "name": "not contracted at every point of K",
         "hyps": ["H_sph", "H_R1"],
         "note": "two kinds of member.  (i) m >= 0 throughout K: contraction "
                 "here is gauge only -- witnesses as spacetimes: Milne, open FRW "
                 "dust, Schwarzschild under Painleve-Gullstrand-E slicing or "
                 "bent between anchored mouths; and the charged body with "
                 "rho >= 0 and a regular centre (R3), which has m >= 0 "
                 "everywhere.  (ii) m < 0 on a proper sub-region K' of K only: "
                 "invariantly contracted on K' (D2), and by H_R1 K' is priced as "
                 "its own C, landing in K1-K6.  K0's EMPTY verdict is about C "
                 "over K, and says nothing against K'"},
        {"id": "K1", "object": "C", "space": "C",
         "lits": {"sph": True, "negm": True, "reg": True, "m0": True, "model": True,
                  "sgt1": True},
         "name": "the priced corridor",
         "hyps": ["H_sph", "H_reg", "H_EFE", "H_M0", "H_model", "H_static",
                  "H_S", "H_flat"],
         "note": "contains achievable.py's family at every b > b_x.  Its proof "
                 "does not use D2: the class is defined by m < 0, and D2 is "
                 "what makes m < 0 the definition of contracting (K0, and the "
                 "entailment)"},
        {"id": "K6a", "object": "C", "space": "C",
         "lits": {"sph": True, "negm": True, "reg": True, "m0": True, "model": False},
         "name": "inside H_M0, profile not a uniform static core",
         "hyps": ["H_sph", "H_reg", "H_M0"],
         "note": "contains certify.py's seated metric (Plummer core).  A "
                 "mean-value route to K1 exists (some point is at least as "
                 "negative as the mean) and is NOT SEATED in any owner"},
        {"id": "K6b", "object": "C", "space": "C",
         "lits": {"sph": True, "negm": True, "reg": True, "m0": True, "model": True,
                  "sgt1": False},
         "name": "inside H_M0, uniform static core, S <= 1",
         "hyps": ["H_sph", "H_reg", "H_M0", "H_model", "H_static"],
         "note": "D7 does not refuse S <= 1"},
        {"id": "K2", "object": "C", "space": "C",
         "lits": {"sph": True, "negm": True, "reg": True, "m0": False},
         "name": "matter or state outside H_M0",
         "hyps": ["H_sph", "H_reg"],
         "note": "NMC scalar (O1 = S4, one refusal), interacting fields, "
                 "massive fields, classical sources, non-Hadamard states; O5's "
                 "HPS field (xi = 1/6) is K2's open instance.  A BOUNDARY is not "
                 "a K2 feature: it breaks H_flat (the flat, boundary-free QEI), "
                 "whose escape reopens K1"},
        {"id": "K3", "object": "C", "space": "C",
         "lits": {"sph": True, "negm": True, "reg": False},
         "name": "non-regular centre",
         "hyps": ["H_sph"],
         "note": "a negative central (bare) mass, including the point charge "
                 "and R8's P2 shell (M_in = -m); m < 0 need not mean rho < 0, "
                 "so R4's density-based refusal does not apply"},
        {"id": "K4", "object": "C", "space": "C", "lits": {"sph": False, "axial": True},
         "name": "infinite axial throats",
         "hyps": ["H_axial"],
         "note": "u < 0 somewhere is forced (O4), but no persistence figure "
                 "exists on this object"},
        {"id": "K5", "object": "C", "space": "C", "lits": {"sph": False, "axial": False},
         "name": "no symmetry (incl. finite axial corridors)",
         "hyps": [],
         "note": "R1 is not supplied here: no owner writes an invariant "
                 "criterion for a general spacetime"},
        {"id": "S-1", "object": "S", "space": "S", "lits": {"wl": True},
         "name": "the seat by cumulative lensing of ordinary matter",
         "hyps": ["H_seat"],
         "note": "witness: the Sun.  The verdict's evidential status is MEASURED "
                 "(the focal formula) + CITED (the causal step) + CHECKED (the "
                 "endpoint gate), not THEOREM"},
        {"id": "S-2", "object": "S", "space": "S", "lits": {"wl": False, "ball": True},
         "name": "Sturm-universal seating over a uniform ball",
         "hyps": ["H_ball", "H_collapse"], "note": "spec.py's own withdrawal"},
        {"id": "S-3", "object": "S", "space": "S", "lits": {"wl": False, "ball": False},
         "name": "any other seat",
         "hyps": [],
         "note": "tubes and non-uniform sustained fields; strong-field "
                 "ordinary focusing; a seat WITH a lead (needs negative mass: "
                 "C's question), where the Kerr-Newman ergoregion is spec.HALTED's "
                 "one untested door"},
        {"id": "W-create-cc", "object": "W", "space": "W",
         "lits": {"created": True, "cc": True},
         "name": "throat created, causally compact interpolation",
         "hyps": ["H_cc"], "note": "create.py calls manufacture 'closed' (V7)"},
        {"id": "W-create-ncc", "object": "W", "space": "W",
         "lits": {"created": True, "cc": False},
         "name": "throat created, causal compactness dropped",
         "hyps": [], "note": "Borde's escapes: none stays in Lorentzian GR "
                             "without a pathology (READ)"},
        {"id": "W-enlarge", "object": "W", "space": "W", "lits": {"created": False},
         "name": "an existing throat found and enlarged",
         "hyps": [], "note": "a metric change; premise unpriced: nobody has "
                             "ever observed a throat"},
        {"id": "Rec", "object": "Rec", "space": "Rec", "lits": {},
         "name": "the reconstruction route", "hyps": [],
         "note": "R11 open in every part"},
    ]


def facts(z3, V, F):
    """The owner facts, each GATED on its owner's live word.  A fact whose
    gate fails is not admitted, and the verdicts that used it fall to OPEN."""
    sr2 = sr2_identity()
    out = [
        {"name": "D2", "space": "C",
         "gate": st("D2") == THEOREM and foliation.IDENTITY_DISPUTED is False,
         "held": "ledger D2 %s; foliation.IDENTITY_DISPUTED = %s"
                 % (st("D2"), foliation.IDENTITY_DISPUTED),
         "hyps": ["H_sph", "H_R1"],
         "f": z3.Implies(V["sph"], V["contracts"] == V["negm"])},
        {"name": "D4", "space": "C",
         "gate": (st("D4") == THEOREM
                  and str(drivensource.CERTIFY_COROLLARY).startswith("NARROWED")),
         "held": "ledger D4 %s; drivensource.CERTIFY_COROLLARY = '%s'"
                 % (st("D4"), drivensource.CERTIFY_COROLLARY),
         "hyps": ["H_sph", "H_reg", "H_EFE"],
         "f": z3.Implies(z3.And(V["sph"], V["negm"], V["reg"]), V["rhoneg"])},
        {"name": "D7", "space": "C",
         "gate": st("D7") == THEOREM and bounds.DURATION_ROUTE_Z == 1,
         "held": "ledger D7 %s; bounds.DURATION_ROUTE_Z = %s"
                 % (st("D7"), bounds.DURATION_ROUTE_Z),
         "hyps": ["H_M0", "H_model", "H_static", "H_S", "H_flat"],
         "f": z3.Implies(z3.And(V["rhoneg"], V["m0"], V["model"], V["sgt1"],
                                V["H_flat"]), z3.Not(V["persist"]))},
        {"name": "O4", "space": "C",
         "gate": st("O4").startswith("CLOSED") and axial.AXIS_ESCAPES_THE_SIGN is False,
         "held": "ledger O4 '%s'; axial.AXIS_ESCAPES_THE_SIGN = %s"
                 % (st("O4"), axial.AXIS_ESCAPES_THE_SIGN),
         "hyps": ["H_axial"],
         "f": z3.Implies(z3.And(V["axial"], V["contracts"]), V["u_neg"])},
        {"name": "SR2", "space": "S",
         "gate": all(sr2) and min(F["soc"]) > 1.0 and F["soc_const"] < 1e-12,
         "held": "spec.seat_over_collapse = %.10g at four scales, sympy %s"
                 % (F["soc"][0], sr2[2]),
         "hyps": ["H_ball", "H_collapse"],
         "f": z3.Implies(V["ball"], V["bh"])},
        {"name": "GEROCH-BORDE", "space": "W",
         "gate": (create.GEROCH_NEEDS_MATTER_ASSUMPTION is False
                  and create.EXOTIC_MATTER_HELPS_CREATION is False),
         "held": "create.GEROCH_NEEDS_MATTER_ASSUMPTION = %s (READ)"
                 % create.GEROCH_NEEDS_MATTER_ASSUMPTION,
         "hyps": ["H_cc"],
         "f": z3.Implies(z3.And(V["created"], V["cc"]), V["ctc"])},
        {"name": "BORDE-ESCAPES", "space": "W",
         "gate": create.any_escape_stays_in_lorentzian_gr() is False,
         "held": "create.any_escape_stays_in_lorentzian_gr() = %s (READ)"
                 % create.any_escape_stays_in_lorentzian_gr(),
         "hyps": [],
         "f": z3.Implies(z3.And(V["created"], z3.Not(V["cc"])), V["pathology"])},
    ]
    return out


def _vars(z3):
    names = ("sph", "axial", "negm", "reg", "m0", "model", "sgt1", "contracts",
             "rhoneg", "persist", "u_neg", "H_flat", "wl", "ball", "bh",
             "created", "cc", "ctc", "pathology")
    return dict((n, z3.Bool(n)) for n in names)


def space_constraint(z3, V, space):
    if space == "C":
        return z3.Not(z3.And(V["sph"], V["axial"]))
    return z3.BoolVal(True)


def member(z3, V, space):
    """What it is to be an instance of the object.  C: contracts (R1) and holds
    for a light-crossing (D7).  S: a seat that is a device, not a black hole
    (SR2).  W: M's pending rulings, imposed only if M makes them."""
    if space == "C":
        return z3.And(V["contracts"], V["persist"])
    if space == "S":
        return z3.Not(V["bh"])
    if space == "W":
        cs = []
        if PENDING_REQUIREMENTS["chronology"]:
            cs.append(z3.Not(V["ctc"]))
        if PENDING_REQUIREMENTS["pathology"]:
            cs.append(z3.Not(V["pathology"]))
        return z3.And(*cs) if cs else z3.BoolVal(True)
    return z3.BoolVal(True)


def _lit(z3, V, lits):
    return z3.And(*[V[k] if v else z3.Not(V[k]) for k, v in lits.items()]) \
        if lits else z3.BoolVal(True)


ASSUMABLE = ("H_flat",)

PROP_TEXT = {"ctc": "a closed causal curve",
             "pathology": "a Borde pathology (a singularity or a point at infinity)"}


def derive(model):
    """Each class verdict by z3, with the unsat core naming the facts used."""
    import z3
    V = _vars(z3)
    fs = [f for f in facts(z3, V, model["F"]) if f["gate"]]
    model["facts_in_force"] = [f["name"] for f in fs]
    model["facts_refused"] = [f["name"] for f in facts(z3, V, model["F"]) if not f["gate"]]
    out = {}
    for K in model["classes"]:
        sp = K["space"]

        def solve(assume):
            s = z3.Solver()
            s.set(unsat_core=True)
            s.add(space_constraint(z3, V, sp), _lit(z3, V, K["lits"]), member(z3, V, sp))
            for f in fs:
                if f["space"] == sp:
                    s.assert_and_track(f["f"], z3.Bool("fact:" + f["name"]))
            for a in assume:
                s.assert_and_track(V[a], z3.Bool("assume:" + a))
            r = s.check()
            core = [str(c) for c in s.unsat_core()] if r == z3.unsat else []
            return r, core
        r0, core0 = solve(())
        if r0 == z3.unsat:
            verdict, core = EMPTY, core0
        else:
            r1, core1 = solve(ASSUMABLE)
            if r1 == z3.unsat:
                verdict, core = EMPTY_IF, core1
            else:
                verdict, core = OPEN_V, []
        if K["id"] == "S-1" and verdict == OPEN_V and model["witness_S1"]:
            verdict = NONEMPTY
        order = [f["name"] for f in fs]
        used = sorted((c.split(":", 1)[1] for c in core if c.startswith("fact:")),
                      key=order.index)
        assumed = [c.split(":", 1)[1] for c in core if c.startswith("assume:")]
        out[K["id"]] = {"verdict": verdict, "facts": used, "assumed": assumed}
    return out


def required_hyps(model, cid, verdicts):
    """What the class's proof used: the hypotheses of the facts in its core,
    and the assumptions in it.  For an OPEN class, nothing is used."""
    v = verdicts[cid]
    fmap = dict((f["name"], f) for f in _facts_plain(model))
    req = set()
    for fn in v["facts"]:
        req.update(fmap[fn]["hyps"])
    req.update(v["assumed"])
    return req


def _facts_plain(model):
    import z3
    return facts(z3, _vars(z3), model["F"])


LIT_HYPS = {"sph": ["H_sph"], "reg": ["H_reg"], "m0": ["H_M0"],
            "model": ["H_model", "H_static"], "sgt1": ["H_S"], "axial": ["H_axial"],
            "ball": ["H_ball"], "cc": ["H_cc"], "wl": ["H_seat"]}


def hyp_check(model, verdicts):
    """[(class, missing, padded)] for every class whose STATED hypotheses do not
    equal what its proof used plus what its positive literals define."""
    bad = []
    for K in model["classes"]:
        req = required_hyps(model, K["id"], verdicts)
        lit = set(h for k, v in K["lits"].items() if v for h in LIT_HYPS.get(k, []))
        stated = set(K["hyps"])
        missing = sorted(req - stated)
        padded = sorted(stated - req - lit)
        if missing or padded:
            bad.append((K["id"], missing, padded))
    return bad


def partition_check(model):
    """z3: in each space the classes are pairwise disjoint and cover it, and
    no class is vacuous (each is satisfiable in its space)."""
    import z3
    V = _vars(z3)
    res = {}
    for sp in sorted(set(K["space"] for K in model["classes"])):
        ks = [K for K in model["classes"] if K["space"] == sp]
        sc = space_constraint(z3, V, sp)
        overlap = []
        for i in range(len(ks)):
            for j in range(i + 1, len(ks)):
                s = z3.Solver()
                s.add(sc, _lit(z3, V, ks[i]["lits"]), _lit(z3, V, ks[j]["lits"]))
                if s.check() == z3.sat:
                    overlap.append((ks[i]["id"], ks[j]["id"]))
        s = z3.Solver()
        s.add(sc, z3.Not(z3.Or(*[_lit(z3, V, K["lits"]) for K in ks])))
        cover = s.check() == z3.unsat
        vac = []
        for K in ks:
            s = z3.Solver()
            s.add(sc, _lit(z3, V, K["lits"]))
            if s.check() != z3.sat:
                vac.append(K["id"])
        res[sp] = {"overlap": overlap, "cover": cover, "vacuous": vac}
    return res


def class_of(model, space, assignment):
    """The one class of `space` whose literals the assignment satisfies."""
    hits = [K["id"] for K in model["classes"] if K["space"] == space
            and all(assignment.get(k) == v for k, v in K["lits"].items())]
    return hits[0] if len(hits) == 1 else None


def entailment(model, verdicts):
    """z3: an instance of C lies in the OPEN classes (under H_flat), or in the
    OPEN and EMPTY IF classes (without it); each OPEN class is consistent with
    every fact in force."""
    import z3
    V = _vars(z3)
    fs = [f for f in facts(z3, V, model["F"]) if f["gate"] and f["space"] == "C"]
    ks = [K for K in model["classes"] if K["space"] == "C"]
    opens = [K for K in ks if verdicts[K["id"]]["verdict"] == OPEN_V]
    conds = [K for K in ks if verdicts[K["id"]]["verdict"] == EMPTY_IF]
    base = [space_constraint(z3, V, "C"), member(z3, V, "C")] + [f["f"] for f in fs]

    def unsat(extra):
        s = z3.Solver()
        s.add(*(base + extra))
        return s.check() == z3.unsat
    with_h = unsat([V["H_flat"], z3.Not(z3.Or(*[_lit(z3, V, K["lits"]) for K in opens]))]) \
        if opens else unsat([V["H_flat"]])
    without_h = unsat([z3.Not(z3.Or(*[_lit(z3, V, K["lits"]) for K in opens + conds]))]) \
        if (opens + conds) else unsat([])
    # every OPEN class, in EVERY space, is propositionally consistent with the
    # facts in force in its space; and what those facts FORCE on its members
    allf = [f for f in facts(z3, V, model["F"]) if f["gate"]]
    consistent, forced = [], {}
    for K in model["classes"]:
        if verdicts[K["id"]]["verdict"] != OPEN_V:
            continue
        sp = K["space"]
        fsp = [f["f"] for f in allf if f["space"] == sp]
        cb = [space_constraint(z3, V, sp), member(z3, V, sp), _lit(z3, V, K["lits"])] + fsp
        if sp == "C":
            cb.append(V["H_flat"])
        s = z3.Solver()
        s.add(*cb)
        consistent.append((K["id"], s.check() == z3.sat))
        for prop in ("ctc", "pathology"):
            s = z3.Solver()
            s.add(*(cb + [z3.Not(V[prop])]))
            if s.check() == z3.unsat:
                forced.setdefault(K["id"], []).append(prop)
    return {"with_H_flat": with_h, "without_H_flat": without_h,
            "opens_consistent": consistent, "forced": forced,
            "facts_encoded": [f["name"] for f in allf]}


# ================================================ 7. ESCAPES, PENDING, V

def landing(model, space, lits):
    """The classes of `space` a candidate with these literals may lie in: those
    whose own literals do not contradict it."""
    return [K["id"] for K in model["classes"] if K["space"] == space
            and all(lits.get(k, v) == v for k, v in K["lits"].items())]


def escapes(model, verdicts):
    """ONE ESCAPE PER HYPOTHESIS a verdict rests on, and one per OPEN ledger row
    no hypothesis escape already carries.  WHAT BREAKING IT REOPENS is COMPUTED
    where it can be: for an ASSUMED hypothesis, the classes whose verdict it
    carries; for a DEFINING hypothesis of an EMPTY / EMPTY IF class, the
    classes a candidate lands in when that literal is flipped, keeping only
    those not themselves EMPTY."""
    H, F = model["hyps"], model["F"]
    reopen = {}
    for K in model["classes"]:
        if verdicts[K["id"]]["verdict"] not in (EMPTY, EMPTY_IF):
            continue
        for a in verdicts[K["id"]]["assumed"]:
            reopen.setdefault(a, set()).add(K["id"])
        lit_h = set()
        for k, val in K["lits"].items():
            flipped = dict(K["lits"])
            flipped[k] = not val
            lands = [c for c in landing(model, K["space"], flipped)
                     if verdicts[c]["verdict"] != EMPTY]
            for h in LIT_HYPS.get(k, []):
                lit_h.add(h)
                reopen.setdefault(h, set()).update(lands)
        # a hypothesis of a fact the proof used, and not a literal of the
        # class: breaking it removes the fact, and the class itself reopens
        fmap = dict((f["name"], f) for f in _facts_plain(model))
        for fn in verdicts[K["id"]]["facts"]:
            for h in fmap[fn]["hyps"]:
                if h not in lit_h and h not in verdicts[K["id"]]["assumed"]:
                    reopen.setdefault(h, set()).add(K["id"])
    o1 = o1_figures()
    routes = [
        ("H_flat", ["O2", "D22 (curved part)"],
         "%s.  RIGHT INSTRUMENT: %s.  The Fewster-Teo spectral-gap tightening "
         "does not transfer (gap %g under GAP_HYPOTHESIS '%s'); Fewster-Teo on the "
         "corridor itself is not evaluated (mode functions %s), and its redshift "
         "factors are not priced."
         % (fewsterteo.O2_ANSWERED_BY, fewsterteo.RIGHT_INSTRUMENT,
            fewsterteo.CORRIDOR_SPECTRAL_GAP, fewsterteo.GAP_HYPOTHESIS,
            fewsterteo.CORRIDOR_MODE_FUNCTIONS)),
        ("H_M0", ["D12", "O1", "S4"],
         "the nonminimally coupled scalar admits no state-independent QEI "
         "(candidates.NMC_STATE_INDEPENDENT_QEI = %s) and is refused ONCE, as S4 = "
         "O1 ('%s'; the ledger's text prices it at >= %s, figures no instrument "
         "re-derives); state-dependent NMC bounds exist (Fewster-Osterbrink "
         "0708.2450, FFKP 2309.10848, as qeihps.py reads them) and an absolute "
         "one is %s.  Interacting fields: no state-independent QEI is expected.  "
         "Classical sources: no QEI applies."
         % (candidates.NMC_STATE_INDEPENDENT_QEI, st("O1"),
            " and >= ".join("%s at xi = %s" % f for f in o1),
            qeihps.ABSOLUTE_QEI_FOR_NMC)),
        ("H_reg", ["D4"],
         "a negative central (bare) mass.  No supply mechanism exists over the "
         "mechanisms examined (B1 %s: '%s' -- a survey, "
         "candidates.LIST_IS_EXHAUSTIVE = %s)."
         % (st("B1"), [r for r in ledger.balance() if r[0] == "B1"][0][3],
            candidates.LIST_IS_EXHAUSTIVE)),
        ("H_sph", ["D1", "D2", "O4"],
         "axial: price persistence on axial.py's object "
         "(PRICES_A_FINITE_CORRIDOR = %s, and the object is infinite in z); "
         "general: an invariant contraction criterion is written nowhere in the "
         "tree." % axial.PRICES_A_FINITE_CORRIDOR),
        ("H_model", ["D7"],
         "mean value over the core: for fixed enclosed negative mass over the "
         "core some point is at least as negative as the mean, so the pointwise "
         "duration bound would refuse a non-uniform profile on the SAME support "
         "volume a fortiori.  A profile whose negative density extends beyond "
         "the core (Plummer's does) has a less negative mean over its larger "
         "support, and the a fortiori step then needs a support bound that is "
         "not seated either.  "
         "Elementary, and NOT SEATED in any owner: until it is, certify.py's "
         "seated metric sits in %s." % model.get("realisation_i")),
        ("H_static", ["D7"],
         "a non-static hold: the pointwise bound needs the density held below "
         "at each point for the whole of b/c, which only staticity supplies here."),
        ("H_S", ["D7"],
         "none.  At the pins S = 1 only at b_x = %.4e m = %.4f l_P, 'l_P times an "
         "O(1) number by construction, NOT evidence'; at b = 1 m, alpha = %g, S <= 1 "
         "only for contractions of at most %.4e m.  Semiclassical validity there is itself "
         "unestablished (O5, D26)." % (F["b_x"], F["b_x_lP"], F["alpha"], F["dd_x"])),
        ("H_EFE", ["D4"],
         "a field equation other than G_ab = 8 pi T_ab: outside every owner "
         "here."),
        ("H_R1", ["D2", "D3", "D10"],
         "none inside spherical symmetry.  What is SHOWN for K0's m >= 0 "
         "members: a slice criterion admits exactly flat space as 'contracted' "
         "(Milne, advance over flat %g); Schwarzschild between anchored mouths "
         "keeps its Shapiro DELAY (%.3f M); and with m >= 0 a sustained slice "
         "contraction moves the far end (nonstatic.py's displacement bound, "
         "%.1f%% of the gap at W = 2).  K0's members with m < 0 on a proper "
         "sub-region are not reopened by breaking H_R1: their sub-region is "
         "already priced as its own C."
         % (F["milne"]["advance_over_flat"], F["shapiro"], 100.0 * F["disp_W2"])),
        ("H_ball", ["none (spec.py; not a ledger row)"],
         "none computed.  A tube of width w = %g l meeting Sturm's u carries "
         "r_s/w = %.4g by a spherical Schwarzschild criterion (computed here from "
         "seatindex.tkk_required -- an ILLUSTRATION only: that criterion is not a "
         "collapse criterion for a tube).  It shows that the ball hypothesis "
         "carries S-2's verdict; tubes and non-uniform sustained fields are S-3."
         % (F["tube_w_over_l"], F["tube_rs_over_w"])),
        ("H_collapse", ["none (spec.py)"],
         "a collapse criterion other than 2GM/c^2 >= l for the ball: none "
         "computed."),
    ]
    out = []
    for key, rows, route in routes:
        text, kind = H[key]
        out.append({"hyp": key, "text": text, "kind": kind,
                    "reopens": sorted(reopen.get(key, set())), "rows": rows,
                    "route": route})
    fixed = [
        ("H3", "noise.py's H3: %s (%s)" % noise.HYPOTHESES["H3"], ["D22"],
         "a self-adjoint extension other than Friedrichs need not keep the bound "
         "(ledger D22).  Breaking it reopens D22's reading.  K1 does not rest "
         "on it: D7's own row says the bound is '%s' (ledger D7), a statement "
         "about expectation values over Hadamard states that no self-adjoint "
         "extension enters." % D7_STATE_INDEPENDENCE),
        ("electrovac", "pure electrovac, spherical symmetry, non-negative bare "
         "mass, rho >= 0 in the body (drivensource.SCOPE and section 4)", ["D4"],
         "breaking it moves the charged body out of K0; not measured: %s"
         % drivensource.SCOPE),
        ("objects", "the object list C, T, S, W, Rec", [],
         "anything that is none of them -- the propulsion OPERATOR phase1 excludes "
         "(a device violating D4), per-use channels (phase1 Theorem 5: GJW) -- is "
         "outside the theorem, which says nothing about it.  The payload's own "
         "motion inside S is part of S."),
        ("static-sph-address", "static spherical symmetry, for D14", ["D14"],
         "beyond static spherical symmetry and the infinite axial object, what an "
         "address requires of a metric: NO OWNER."),
        ("causal-step", "conjugate point => not achronal (CITED)", ["D5"],
         "SR3's traversal clause rests on a standard causal-structure result no "
         "owner re-proves; B must lie strictly past the focus."),
        ("S-contract", "S is not required to contract (a reading of M's "
                       "quotation; PENDING P1)", [],
         "if M requires S to contract, S must be a C and R1-R4 bind it; a positive "
         "lens does not contract (certify.theorem_holds)."),
    ]
    for key, text, rows, route in fixed:
        out.append({"hyp": key, "text": text, "kind": "OWNER" if key not in
                    ("objects", "S-contract") else "SCOPE", "reopens": None,
                    "rows": rows, "route": route})
    # An OPEN row is folded into a hypothesis escape only where that escape IS
    # the row's open question (H_flat is O2's curved QEI).  Every other open
    # row keeps its own escape with the ledger's full route.
    carried = set(r for x in out if x["kind"] == ASSUMED for r in x["rows"])
    for rid in open_row_ids():
        if rid in carried:
            continue
        ans = row(rid)[2]
        if ans is None and rid == "S5":
            ans = branelink.S5_OWED
        out.append({"hyp": "OPEN " + rid, "text": ledger._one_line(row(rid)[1], 200),
                    "kind": "OPEN ROW", "reopens": None, "rows": [rid],
                    "route": " ".join(str(ans).split())})
    return out


#: D7's own words for why no branch escapes the bound, asked from the row.
D7_STATE_INDEPENDENCE = re.search(r"(STATE-INDEPENDENT over Hadamard states)",
                                  " ".join(row("D7")[1].split())).group(1)


def open_row_ids():
    return ([r[0] for r in ledger.DEMAND if r[2] == OPEN]
            + [r[0] for r in ledger.SUPPLY if r[2] == OPEN]
            + [r[0] for r in ledger.OPEN_ROWS])


def o1_figures():
    """O1's two figures, ASKED from the ledger's own text (no instrument
    computes them): [(value, xi)]."""
    txt = row("O1")[2]
    return re.findall(r">= (\d+\.\d+) at xi = (\d/\d)", txt)


#: EVERY FRAGMENT THIS FILE QUOTES FROM AN OWNER, checked against the owner's
#: source (whitespace, '*' and case normalised).  A misquote is a selftest
#: failure, which is the only defence a quotation has.
QUOTES = (
    ("bounds", "priced on the DURATION axis, by an instrument of the wrong shape "
               "under an extra hypothesis"),
    ("achievable", "l_P times an O(1) number by construction, NOT evidence"),
    ("achievable", "concentric.py's window, weakest end"),
    ("achievable", "Sec. 5.1"),
    ("phase1", "Nothing is transported anywhere by the operator itself"),
    ("spec", "DROP THE LEAD.  KEEP THE SEAT."),
    ("spec", "nothing else"),
    ("spec", "UNIVERSAL in Sturm's sense"),
    ("spec", "one untested door"),
    ("create", "manufacture a wormhole -- closed"),
    ("drivensource", "THE BREAK IS EMPTY"),
    ("formation", "length unit L that the tree never fixes"),
    ("formation", "INT (time part of rho + p_T) d tau"),
    ("formation", "assumes agents acting in a compact region"),
    ("linstab", "the core's own stability is deferred with the identification phase"),
    ("axial", "IT DOES NOT PRICE A CORRIDOR"),
    ("foliation", "THE ANCHOR LEMMA DOES NOT CLOSE THE INTEGRATED CRITERION"),
    ("nonstatic", "NO QUASI-STATIONARY CORRIDOR EXISTS"),
    ("concentric", "THE LEAD MEASURED HERE IS INTERIOR-ONLY"),
    ("composite", "forms no real image"),
    ("ledger:D14", "one-bit parameter"),
    ("ledger:O1", "it was S4 counted a second time"),
    ("ledger:S9", "the specification against itself, not a gap against this "
                  "board's demand"),
    ("ledger:D6", "NO purely spatially averaged quantum inequalities over bounded "
                  "regions in 4D Minkowski"),
    ("ledger:S3", "Passes KIND and DEADLINE, fails MAGNITUDE"),
    ("ledger:D7", "STATE-INDEPENDENT over Hadamard states"),
    ("drivensource", "INNER horizon"),
    ("drivensource", "Gibbons-Hull/Witten"),
)


def _norm(t):
    return " ".join(t.replace("*", "").split()).casefold()


def misquotes(quotes=QUOTES):
    """Every (owner, fragment) whose fragment is not in the owner's text."""
    import importlib
    bad = []
    for owner, frag in quotes:
        if owner.startswith("ledger:"):
            src = " ".join(str(x) for x in row(owner.split(":", 1)[1]) if x)
        else:
            with open(importlib.import_module(owner).__file__, encoding="utf-8") as fh:
                src = fh.read()
        if _norm(frag) not in _norm(src):
            bad.append((owner, frag))
    return bad


PENDING_FOR_M = [
    ("P1", "Is S required to contract?",
     "spec.py drops the LEAD and never says 'contract'; this file reads M's "
     "'nothing else' as not requiring it.",
     "If yes: S must be a C, R1-R4 bind it, and S-1's positive lens does not "
     "meet R2."),
    ("P2", "Is aimability binding (DOCKET 62's R5)?",
     "D14 proves the destination UNDEFINED on the static spherical object, not "
     "that the contraction fails to reach B.",
     "If yes: every static spherically symmetric MEMBER of K0-K3 and K6 is "
     "excluded (D14) -- no class is static spherical by definition, so no class "
     "empties whole; K4's one-bit parameter is undecided."),
    ("P3", "Is a closed causal curve, or a Borde pathology, disqualifying?",
     "create.py calls causally compact manufacture 'closed'; no requirement R1-R12 "
     "forbids causality violation as written.",
     "If yes: W-create-cc (chronology) and W-create-ncc (pathology) become EMPTY."),
    ("P4", "Is phase1's D3 read per R1?",
     "phase1's D3 is a slice statement and a slice statement is gauge; the anchor "
     "lemma does not close it (foliation.NONSTATIC_ANCHOR_CLOSES_D3 = False).",
     "If no: T admits K0 members (Milne satisfies a slice D3 in flat space)."),
    ("P5", "For Rec: what is specified, at what fidelity, classical or quantum?",
     "DOCKET 62's R11 note records these three rulings as unmade.  No verdict "
     "rests on them: Rec is OPEN.",
     "Any ruling fixes R11's bit count, which S5 owes (branelink.S5_OWED)."),
]

DIVERGENCES = [
    ("V1", "DOCKET 62 R2: 'over-determined three ways' including Olum",
     "Olum (D5) concerns superluminal travel -- the lead -- not m < 0 contraction; "
     "dropped from R2."),
    ("V2", "DOCKET 62 R4: 72.599", "REFUSED: gap 0 on an asymptotically flat corridor "
     "(fewsterteo.py); 71.256 stands."),
    ("V3", "DOCKET 62 R5: 'a device that cannot be aimed is not a device'",
     "not used as an exclusion (P2)."),
    ("V4", "DOCKET 62 R9 as a separate requirement",
     "folded into R4: DOCKET 64 D ruled the requirement is not restated about a "
     "distribution, so R9 refuses exactly R4's set in the flat model under H6."),
    ("V5", "DOCKET 62 R12: 'the tree can PROVE the right side is empty'",
     "candidates.LIST_IS_EXHAUSTIVE is False: a SURVEY."),
    ("V6", "drivensource.OVERTURN_L2: the point-charge break 'IS EMPTY'",
     "the emptiness is proved for bodies with non-negative bare mass; the point "
     "charge carries a -infinite bare mass, outside that hypothesis, so K3 carries "
     "it OPEN.  The owner has a second route: under Gibbons-Hull/Witten's Q <= M "
     "(charge.py, confirmed in drivensource section 4) the point charge's m < 0 "
     "region lies inside the INNER horizon r_- (drivensource.inner_horizon_ratio "
     "<= 1).  Whether that empties the K3 instance is not decided here: no "
     "requirement R1-R12 is written for a region inside a horizon."),
    ("V7", "create.py: manufacture 'closed'",
     "W-create-cc is OPEN here because no requirement forbids causality violation "
     "(P3); the owner's word is printed beside it."),
    ("V8", "DOCKET 62 R6 note: Fewster & Smith widen the covered set",
     "true of its class; it is not evaluated on the corridor, so H_flat is not "
     "discharged."),
    ("V9", "phase1 docstring: 'IT IS NEVER A LEAD' (Theorem 4)",
     "Theorem 4 presupposes D2 and agents in a compact region; formation.py's "
     "family meets neither, so it does not reach that passage."),
]

WHAT_IT_DOES_NOT_SAY = [
    "It does not say a contracting corridor is impossible: the OPEN classes are open.",
    "It does not say K1 is empty unconditionally: its verdict needs H_flat, ASSUMED.",
    "It does not declare impossible anything spec.py establishes: S-1 is NONEMPTY.",
    "It does not say the seat is new: '%s' (spec.DOES_NOT)." % spec.DOES_NOT[0],
    "It does not use aimability, chronology or pathology as exclusions (P2, P3).",
    "It does not decide whether a transition can lead; a lead is not required.",
    "It does not quote O1's two figures as MEASURED, nor any SI formation price.",
    "It does not rank the open classes or total any gaps.",
    "It says nothing about objects outside C, T, S, W, Rec.",
]


# ================================================= 8. BUILD AND HEADLINE

def build():
    F = figures()
    sf = slow_figures()
    model = {"F": F, "hyps": hypotheses(), "classes": classes(),
             "requirements": requirements(F),
             "witness_S1": bool(sf["spec_selftest_ok"] and F["f_sun_m"] > 0.0)}
    model["objects"] = objects(F)
    return model


RE_ASK_PINS = (("fewsterteo", "O2_CLOSED", False), ("hpscentre", "O5_CLOSED", False),
               ("branelink", "O6_CLOSED", False), ("branelink", "O7_CLOSED", False),
               ("latticectc", "O3_CLOSED", False),
               ("linstab", "SEMICLASSICAL_EVALUABLE_ON_DEMAND", False),
               ("noise", "H2_SATISFIED_BY_CORRIDOR", False))


def re_ask(model=None):
    """Owners whose movement this file cannot interpret -- an open row closing,
    in a direction the flag does not say.  Any of them moving makes the
    headline RE-ASK instead of a guess."""
    return ["%s.%s" % (m, a) for m, a, want in RE_ASK_PINS if A(m, a) != want]


def fill_objects(model, verdicts):
    F = model["F"]
    ri = class_of(model, "C", {"sph": True, "negm": F["certify_negm"],
                               "reg": True, "m0": True, "model": False})
    rii = class_of(model, "C", {"sph": True, "negm": True, "reg": True, "m0": True,
                                "model": True, "sgt1": F["S1"] > 1.0})
    for o in model["objects"]:
        o["definition"] = o["definition"].replace("{realisation_i}", str(ri)) \
                                         .replace("{realisation_ii}", str(rii))
    model["realisation_i"], model["realisation_ii"] = ri, rii


def headline(model, verdicts, ent):
    moved = re_ask(model)
    if moved:
        return ("RE-ASK: %s moved.  This file cannot tell which way an open row "
                "closed, so it states no theorem until it is re-read."
                % ", ".join(moved))
    by = lambda sp, v: [K["id"] for K in model["classes"]
                        if K["space"] == sp and verdicts[K["id"]]["verdict"] == v]
    L = []
    e, c, o = by("C", EMPTY), by("C", EMPTY_IF), by("C", OPEN_V)
    ass = sorted(set(a for k in c for a in verdicts[k]["assumed"]))
    L.append("OVER C (the contracting corridor): the classes partition C (z3).  "
             "EMPTY: %s.%s  OPEN: %s."
             % (", ".join(e) or "none",
                ("  EMPTY IF %s: %s." % (" and ".join(ass), ", ".join(c))) if c else "",
                ", ".join(o) or "none"))
    if ent["with_H_flat"] and c:
        L.append("So, under %s, every contracting corridor lies in %s; if %s "
                 "fails it may also lie in %s (z3: entailed).  Each OPEN class is "
                 "propositionally consistent with the facts encoded and in force "
                 "in its own space (of %s) (z3: %s) -- a check over those encoded "
                 "implications, not over the tree."
                 % (" and ".join(ass), ", ".join(o), " and ".join(ass), ", ".join(c),
                    ", ".join(ent["facts_encoded"]),
                    "all sat" if all(x[1] for x in ent["opens_consistent"])
                    else "NOT all sat"))
    for sp, name in (("S", "S (M's scoped seat)"), ("W", "W (the throat gate)"),
                     ("Rec", "Rec (the reconstruction route)")):
        parts = ["%s %s" % (v, ", ".join(by(sp, v))) for v in VERDICTS if by(sp, v)]
        L.append("OVER %s: %s." % (name, "; ".join(parts)))
    L.append("T (the transition): IF phase1's D3 is read per R1 (%s) AND the "
             "endpoint is held for one light-crossing (D7), its endpoint is an "
             "instance of C and inherits C's verdicts; without the hold it lies "
             "outside C and transmits nothing (D7).  Its passage is priced, not "
             "refused (R10, RT)." % ("PENDING P4" if any(p[0] == "P4" for p in PENDING_FOR_M)
                                    else "P4"))
    return "\n".join(L)


def run():
    model = build()
    verdicts = derive(model)
    fill_objects(model, verdicts)
    ent = entailment(model, verdicts)
    model["verdicts"], model["entailment"] = verdicts, ent
    model["escapes"] = escapes(model, verdicts)
    model["partition"] = partition_check(model)
    model["headline"] = headline(model, verdicts, ent)
    return model


# ============================================================ 9. THE REPORT

def _wrap(text, indent=6, width=96):
    import textwrap
    return textwrap.fill(" ".join(str(text).split()), width=width,
                         initial_indent=" " * indent, subsequent_indent=" " * indent)


def theorem_statement(model):
    v, H = model["verdicts"], model["hyps"]
    cls = dict((K["id"], K) for K in model["classes"])

    def defn(cid):
        K = cls[cid]
        return " and ".join(("" if val else "not ") + FEATURE_TEXT[k]
                            for k, val in K["lits"].items()) or "all of it"
    L = ["THE SPECIFICATION THEOREM (derived at run time from the class verdicts)", ""]
    n = 1
    for cid in [K["id"] for K in model["classes"]]:
        vv = v[cid]
        K = cls[cid]
        if vv["verdict"] == EMPTY:
            L.append(_wrap("(%d) [%s] %s -- the class '%s' (%s) is EMPTY of "
                           "instances of %s, by %s, under %s."
                           % (n, K["object"], cid, K["name"], defn(cid), K["object"],
                                          " + ".join(vv["facts"]),
                                          ", ".join(K["hyps"]) or "no hypothesis"), 2))
        elif vv["verdict"] == EMPTY_IF:
            L.append(_wrap("(%d) [%s] %s -- the class '%s' (%s) is EMPTY of "
                           "instances of %s IF %s (ASSUMED), by %s, under %s." %
                           (n, K["object"], cid, K["name"], defn(cid), K["object"],
                            " and ".join(vv["assumed"]), " + ".join(vv["facts"]),
                            ", ".join(K["hyps"])), 2))
        elif vv["verdict"] == NONEMPTY:
            L.append(_wrap("(%d) [%s] %s -- '%s' is NONEMPTY: witness the Sun, "
                           "f(R_sun) = %.2f AU (spec.focal_length), NEC, WEC and DEC "
                           "satisfied, under %s: %s.  Its evidential status is %s "
                           "+ %s + %s, not %s."
                           % (n, K["object"], cid, K["name"], model["F"]["f_sun_AU"],
                              ", ".join(K["hyps"]),
                              "; ".join(H[h][0] for h in K["hyps"]),
                              MEASURED, CITED, CHECKED, THEOREM), 2))
        else:
            continue
        n += 1
    opens = [K["id"] for K in model["classes"] if v[K["id"]]["verdict"] == OPEN_V]
    ent = model["entailment"]
    forced = ent["forced"]
    fsent = "".join("  %s's members are FORCED to carry %s by the facts in force "
                    "(z3; the facts are READ by create.py); %s empties only if M "
                    "rules P3." % (cid, " and ".join(PROP_TEXT[p] for p in props), cid)
                    for cid, props in sorted(forced.items()))
    L.append(_wrap("(%d) Every other class is OPEN: %s.  No requirement in force "
                   "empties any of them.%s  Each OPEN class is propositionally consistent "
                   "with the facts encoded and in force in its space -- %s -- "
                   "(z3: %s); that is a check over those encoded implications, not "
                   "consistency with the whole tree."
                   % (n, ", ".join(opens), fsent, ", ".join(ent["facts_encoded"]),
                      "all sat" if all(x[1] for x in ent["opens_consistent"])
                      else "NOT all sat"), 2))
    L.append(_wrap("(%d) The requirements hold as stated in the table, each on the "
                   "object named there; every limitation is a named hypothesis "
                   "there or an escape below." % (n + 1), 2))
    return "\n".join(L)


def report():
    model = run()
    print(__doc__.split("===============", 1)[0].strip())
    print("\n" + "=" * 79)
    print("HEADLINE")
    print("=" * 79)
    for line in model["headline"].split("\n"):
        print(_wrap(line, 2))
    print()
    print(theorem_statement(model))

    print("\n" + "=" * 79 + "\nTHE OBJECTS\n" + "=" * 79)
    for o in model["objects"]:
        print("  %s -- %s" % (o["id"], o["name"]))
        print(_wrap(o["definition"]))
        print(_wrap("source: " + o["source"]))

    print("\n" + "=" * 79 + "\nTHE REQUIREMENT TABLE\n" + "=" * 79)
    print("  %-5s %-8s %s" % ("id", "object", "status"))
    for r in model["requirements"]:
        print("  %-5s %-8s %s" % (r["id"], ",".join(r["applies_to"]),
                                  ledger._one_line(r["status"], 84)))
    for r in model["requirements"]:
        print("\n  %s  %s" % (r["id"], r["title"]))
        print(_wrap("OBJECT: %s.   STATUS: %s" % (", ".join(r["applies_to"]), r["status"])))
        print(_wrap(r["statement"]))
        print(_wrap("LEDGER ROWS PLACED HERE: %s%s" % (
            ", ".join(r["rows"]) or "none",
            ("; referenced: " + ", ".join(r["see"])) if r["see"] else "")))
        print(_wrap("OWNERS ASKED: " + "; ".join(
            "%s.%s = %s" % (m, a, ledger._one_line(repr(A(m, a)), 60))
            for m, a in r["owners"])))
        print(_wrap("HYPOTHESES: " + " | ".join(
            (model["hyps"][h][0] + " [%s]" % h) if h in model["hyps"] else h
            for h in r["hypotheses"])))

    print("\n" + "=" * 79 + "\nTHE CLASS TABLE\n" + "=" * 79)
    print("  %-13s %-4s %-9s %-24s %s" % ("class", "obj", "verdict", "facts used",
                                         "stated hypotheses"))
    for K in model["classes"]:
        vv = model["verdicts"][K["id"]]
        print("  %-13s %-4s %-9s %-24s %s"
              % (K["id"], K["object"], vv["verdict"],
                 (" + ".join(vv["facts"]) + (" | " + ",".join(vv["assumed"])
                                             if vv["assumed"] else "")) or "-",
                 ", ".join(K["hyps"]) or "-"))
    for K in model["classes"]:
        print("\n  %s  %s" % (K["id"], K["name"]))
        print(_wrap("DEFINITION: " + (" and ".join(
            ("" if val else "NOT ") + FEATURE_TEXT[k] for k, val in K["lits"].items())
            or "the whole route")))
        print(_wrap("NOTE: " + K["note"]))
    print("\n  facts in force: %s" % ", ".join(model["facts_in_force"]))
    print("  facts refused (owner moved): %s" % (", ".join(model["facts_refused"]) or "none"))
    for f in _facts_plain(model):
        print(_wrap("%-13s held by: %s.  hypotheses: %s"
                    % (f["name"], f["held"], ", ".join(f["hyps"]) or "-")))
    for sp, p in sorted(model["partition"].items()):
        print("  partition of %-4s disjoint: %-5s covers: %-5s vacuous classes: %s"
              % (sp, not p["overlap"], p["cover"], p["vacuous"] or "none"))
    e = model["entailment"]
    print("  entailed, under H_flat: C lies in the OPEN classes = %s; without H_flat, "
          "in OPEN + EMPTY IF = %s" % (e["with_H_flat"], e["without_H_flat"]))

    print("\n" + "=" * 79 + "\nTHE ESCAPE LIST\n" + "=" * 79)
    for i, x in enumerate(model["escapes"], 1):
        print("  E%-3d %s  [%s]" % (i, x["hyp"], x["kind"]))
        print(_wrap(x["text"]))
        if x["reopens"] is not None:
            print(_wrap("BREAKING IT REOPENS (computed): %s"
                        % (", ".join(x["reopens"]) or "nothing")))
        if x["rows"]:
            print(_wrap("LEDGER: %s" % ", ".join(x["rows"])))
        print(_wrap("KNOWN ROUTE: " + x["route"]))

    print("\n" + "=" * 79 + "\nPENDING FOR M -- what changes either way\n" + "=" * 79)
    for pid, q, why, change in PENDING_FOR_M:
        print("  %s  %s" % (pid, q))
        print(_wrap(why))
        print(_wrap(change))
    print("\n" + "=" * 79 + "\nDIVERGENCES FROM A SOURCE, STATED\n" + "=" * 79)
    for vid, src, why in DIVERGENCES:
        print("  %s  %s" % (vid, src))
        print(_wrap(why))
    print("\n" + "=" * 79 + "\nWHAT THE THEOREM DOES NOT SAY\n" + "=" * 79)
    for s in WHAT_IT_DOES_NOT_SAY:
        print(_wrap("- " + s, 2))
    wr = withdrawn_ids()
    print("\n  withdrawn rows relied on: none (%s are listed in ledger.py and none "
          "is an owner or a placed row here)" % ", ".join([wr[0], "...", wr[-1]]))
    return 0


def render(model=None):
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        report()
    return buf.getvalue()


# ======================================================== 10. THE CHECKS

def placement(model):
    """(missing, doubled, withdrawn_used, unknown) against the ledger's LIVE rows."""
    placed = [x for r in model["requirements"] for x in r["rows"]]
    ids = ledger_ids()
    missing = [i for i in ids if i not in placed]
    doubled = sorted(set(i for i in placed if placed.count(i) > 1))
    wd = set(withdrawn_ids())
    used = sorted(set(x for r in model["requirements"]
                      for x in r["rows"] + r["see"] if x in wd)
                  | set(m for r in model["requirements"] for m, _a in r["owners"]
                        if m in wd))
    unknown = [i for i in placed if i not in ids]
    return missing, doubled, used, unknown


def scope_check(model, verdicts):
    """spec.py's scoping respected: (1) no requirement on C (R1-R4 and the
    corridor rows) is applied to S; (2) no EMPTY / EMPTY IF class of S contains
    spec.py's achievable set (z3: class and wl jointly satisfiable)."""
    import z3
    V = _vars(z3)
    on_S = sorted(r["id"] for r in model["requirements"] if "S" in r["applies_to"])
    allowed = {"R5-S", "SR1", "SR2", "SR3", "SR4"}
    bad_req = sorted(set(on_S) - allowed)
    bad_cls = []
    for K in model["classes"]:
        if K["space"] != "S" or verdicts[K["id"]]["verdict"] not in (EMPTY, EMPTY_IF):
            continue
        s = z3.Solver()
        s.add(_lit(z3, V, K["lits"]), V["wl"])
        if s.check() == z3.sat:
            bad_cls.append(K["id"])
    return bad_req, bad_cls


def declared_check(model, verdicts, text):
    """The forbidden word appears in no status, no verdict and no printed line."""
    words = [r["status"] for r in model["requirements"]] + \
            [v["verdict"] for v in verdicts.values()]
    in_status = [w for w in words if FORBIDDEN_STATUS_WORD in w.upper()]
    in_text = re.findall(r"\b%s\b" % FORBIDDEN_STATUS_WORD, text)
    return in_status, in_text


WITHDRAWN_NEEDLES = ("65 orders", "sixty-five", "18.5 orders", "1.5456e19",
                     "PROTECTS ACHRONALITY")


def withdrawn_lines(text):
    """Printed lines carrying a withdrawn figure without saying so."""
    bad = []
    paras = text.split("\n\n")
    for p in paras:
        flat = " ".join(p.split())
        for n in WITHDRAWN_NEEDLES:
            if n in flat and not re.search(r"WITHDRAWN|withdrawn|struck|STRUCK|REFUSED",
                                           flat):
                bad.append((n, flat[:80]))
    return bad


def o1_figures_are_ledger_text():
    """The two O1 figures occur in ledger.py / LEDGER.md and no other file here."""
    hits = []
    for fn in sorted(os.listdir(HERE)):
        if not (fn.endswith(".py") or fn.endswith(".md")) or fn == os.path.basename(__file__):
            continue
        try:
            with open(os.path.join(HERE, fn), encoding="utf-8") as fh:
                t = fh.read()
        except (OSError, UnicodeDecodeError):
            continue
        if any(v in t for v, _xi in o1_figures()):
            hits.append(fn)
    return hits


def cls_hyps(model, cid):
    return [K for K in model["classes"] if K["id"] == cid][0]["hyps"]


@contextlib.contextmanager
def patched(obj, attr, value):
    old = getattr(obj, attr)
    setattr(obj, attr, value)
    try:
        yield
    finally:
        setattr(obj, attr, old)


@contextlib.contextmanager
def ledger_status(rid, status):
    """Replace one DEMAND row's status for the duration -- a scratch copy of the
    board, restored after."""
    new = [(r[0], r[1], status, r[3], r[4]) if r[0] == rid else r for r in ledger.DEMAND]
    with patched(ledger, "DEMAND", new):
        yield


def selftest():
    fails = []
    rows = []

    def chk(kind, label, got, want):
        good = got == want
        rows.append((kind, good))
        tag = {"ask": "ask", "fig": "fig", "z3": "z3 ", "ctl": "CTL", "pin": "pin",
               "chk": "chk"}[kind]
        print("  [%s] %s %-70s %s" % ("ok" if good else "XX", tag, label[:70],
                                      ledger._one_line(repr(got), 60)))
        if not good:
            fails.append((label, got, want))

    print("specthm.py --selftest")
    print("  kinds: ask = an owner asked, fig = a figure, z3 = a solver result,")
    print("  CTL = a control that must change the output, pin = a verdict pinned,")
    print("  chk = a structural check\n")

    print("1. EVERY OWNER CITED IS ASKED, AND EVERY ASK SUCCEEDS")
    model = run()
    n = 0
    for r in model["requirements"]:
        for m, a in r["owners"]:
            A(m, a)
            n += 1
    chk("ask", "owner attributes asked across the requirements (none missing)", n > 0, True)
    chk("ask", "every ledger row a requirement places or references exists",
        placement(model)[3], [])
    chk("ask", "the ledger's own selftest-facing census is unchanged in kind",
        sorted(ledger.statuses().keys()) == sorted(ledger.STATUSES), True)

    print("\n2. THE FIGURES, ASKED OR COMPOSED FROM ASKS")
    F = model["F"]
    chk("fig", "S closed form = owner ratio at every test point (rel < 1e-12)",
        F["closed_rel"] < 1e-12, True)
    chk("fig", "log10 S(1 m) at the pins = fewsterteo.FLAT_SHORTFALL_ORDERS",
        abs(F["log10S1"] - F["flat_orders"]) < 1e-9, True)
    chk("fig", "  and it IS achievable.persistence_shortfall(1 m)",
        abs(F["S1"] / achievable.persistence_shortfall(1.0) - 1.0) < 1e-12, True)
    chk("fig", "S = 1 at b_x (persistence_crossing), to 1e-9",
        abs(S_ratio(F["b_x"]) - 1.0) < 1e-9, True)
    chk("fig", "Lambda = phase1.lam() = overturn.LAMBDA", F["Lambda_is_overturn"], True)
    chk("fig", "phase1.contraction_law gives Delta d = mu b Lambda (rel < 1e-12)",
        F["dd_owner_is_mu_b_Lambda"] < 1e-12, True)
    chk("fig", "S is linear in mu at fixed (b, alpha)",
        abs(F["S_linear_in_mu"] - 2.0) < 1e-12, True)
    chk("fig", "at Delta d_x the composed S returns 1",
        abs(S_ratio(1.0, F["mu"] * F["dd_x"] / F["dd_owner"]) - 1.0) < 1e-9, True)
    sf = slow_figures()
    chk("fig", "mu is concentric's SEAT+LEAD edge: no seat at 0.6 mu, seat+lead at mu",
        (sf["concentric_below"]["seats"], sf["concentric_at"]["seats"],
         sf["concentric_at"]["leads"]), (False, True, True))
    chk("fig", "a positive lens seats LATE (composite +2e-3); the negative one early",
        (sf["composite_plus"]["seats"], sf["composite_plus"]["delay"] > 0.0,
         sf["composite_minus"]["early"]), (True, True, True))
    chk("fig", "spec.py's selftest passes (it pins f_sun to its own 547.6 AU)",
        sf["spec_selftest_ok"], True)
    chk("fig", "the published ~550 AU is read from spec.py, and it is NOT within "
        "spec's 1e-3 of f_sun", (F["published_sun_AU"],
                                 abs(F["f_sun_AU"] / F["published_sun_AU"] - 1.0) > 1e-3),
        (550.0, True))
    chk("fig", "SR2: the owners' coefficients are pi c^4/4G and 3c^4/(8 pi G)",
        sr2_identity()[:2], (True, True))
    import sympy
    chk("fig", "  and their quotient is 2 pi^2/3 exactly (sympy)",
        sympy.simplify(sr2_identity()[2] - 2 * sympy.pi ** 2 / 3), 0)
    chk("fig", "  equal to spec.seat_over_collapse at four scales",
        max(abs(x / float(2 * sympy.pi ** 2 / 3) - 1.0) for x in F["soc"]) < 1e-12, True)
    chk("fig", "D22 folded in: the demand is not restated about a distribution",
        noise.DEMAND_RESTATED_ABOUT_DISTRIBUTION_CHANGES_REQUIREMENT, False)

    print("\n3. THE PARTITION, BY z3")
    for sp, p in sorted(model["partition"].items()):
        chk("z3", "space %s: pairwise disjoint, covering, no class vacuous" % sp,
            (p["overlap"], p["cover"], p["vacuous"]), ([], True, []))

    print("\n4. THE VERDICTS AS DERIVED AT THIS HEAD (pins; the report never reads them)")
    v = model["verdicts"]
    want = {"K0": EMPTY, "K1": EMPTY_IF, "K6a": OPEN_V, "K6b": OPEN_V, "K2": OPEN_V,
            "K3": OPEN_V, "K4": OPEN_V, "K5": OPEN_V, "S-1": NONEMPTY, "S-2": EMPTY,
            "S-3": OPEN_V, "W-create-cc": OPEN_V, "W-create-ncc": OPEN_V,
            "W-enlarge": OPEN_V, "Rec": OPEN_V}
    chk("pin", "every class verdict", dict((k, v[k]["verdict"]) for k in want), want)
    chk("pin", "K1's proof uses D4 + D7 (not D2) and assumes exactly H_flat",
        (v["K1"]["facts"], v["K1"]["assumed"]), (["D4", "D7"], ["H_flat"]))
    chk("pin", "K0's proof uses D2 alone", v["K0"]["facts"], ["D2"])
    chk("pin", "S-2's proof uses SR2 alone", v["S-2"]["facts"], ["SR2"])
    chk("z3", "entailment: under H_flat C lies in the OPEN classes; without, + EMPTY IF",
        (model["entailment"]["with_H_flat"], model["entailment"]["without_H_flat"]),
        (True, True))
    chk("z3", "every OPEN class of C is consistent with every fact in force",
        all(x[1] for x in model["entailment"]["opens_consistent"]), True)
    chk("chk", "realisation (i), certify's seated metric, is in K6a (not K1)",
        model["realisation_i"], "K6a")
    chk("chk", "realisation (ii), achievable's family at b = 1 m, is in K1",
        model["realisation_ii"], "K1")

    print("\n5. EACH CLASS STATES EXACTLY WHAT ITS PROOF USED")
    chk("chk", "no class misses a hypothesis its z3 core used, none is padded",
        hyp_check(model, v), [])

    print("\n6. PLACEMENT AGAINST THE LIVE LEDGER, AND WHAT IS NOT RELIED ON")
    missing, doubled, used, unknown = placement(model)
    chk("chk", "every ledger row (D, S, O, closed O, B, ruled) is placed", missing, [])
    chk("chk", "and placed exactly once (no over-representation)", doubled, [])
    chk("chk", "no WITHDRAWN row is placed, referenced or used as an owner", used, [])
    text = render()
    chk("chk", "no withdrawn figure printed without saying it is withdrawn",
        withdrawn_lines(text), [])
    chk("chk", "O1's two figures occur only in ledger.py and LEDGER.md (ledger text)",
        o1_figures_are_ledger_text(), ["LEDGER.md", "ledger.py"])
    chk("chk", "O1's status is quoted verbatim from ledger.CLOSED_ROWS",
        st("O1"), ledger.CLOSED_ROWS[[r[0] for r in ledger.CLOSED_ROWS].index("O1")][2]
        .split(".")[0])

    chk("chk", "every fragment quoted from an owner is in the owner's text",
        misquotes(), [])
    chk("chk", "composite.phi restored after concentric's surveys (owner side effect)",
        sf["composite_phi_restored"], True)

    print("\n7. M's RULES, COMPUTED")
    chk("chk", "the word %s is no status, no verdict, and absent from the "
        "printout" % FORBIDDEN_STATUS_WORD, declared_check(model, v, text), ([], []))
    chk("chk", "spec.py's scope: no C requirement on S; no EMPTY seat class holds "
        "spec's witness", scope_check(model, v), ([], []))
    chk("chk", "R1-R4 apply to C (R1 also to T's D3) and never to S",
        [r["id"] for r in model["requirements"] if r["id"] in ("R1", "R2", "R3", "R4")
         and "S" in r["applies_to"]], [])
    chk("chk", "every ASSUMED hypothesis has an escape",
        sorted(h for h, (t, k) in model["hyps"].items() if k == "ASSUMED"
               and not any(x["hyp"] == h for x in model["escapes"])), [])
    open_rows = ([r[0] for r in ledger.DEMAND if r[2] == OPEN]
                 + [r[0] for r in ledger.SUPPLY if r[2] == OPEN]
                 + [r[0] for r in ledger.OPEN_ROWS])
    chk("chk", "every OPEN ledger row is carried by an escape (DOCKET 64 E's condition)",
        [r for r in open_rows if not any(r in x["rows"] for x in model["escapes"])], [])
    chk("chk", "  and their number is ledger.statuses()'s OPEN count",
        len(open_rows), ledger.statuses()[OPEN])
    stated = sorted(set(h for K in model["classes"]
                        if v[K["id"]]["verdict"] in (EMPTY, EMPTY_IF) for h in K["hyps"]))
    esc = dict((x["hyp"], x) for x in model["escapes"])
    chk("chk", "every hypothesis an EMPTY / EMPTY IF class states has an escape",
        [h for h in stated if h not in esc], [])
    chk("chk", "  and breaking each reopens a class (computed, never empty)",
        [h for h in stated if h in esc and not esc[h]["reopens"]], [])
    chk("chk", "  H_flat reopens exactly K1; H_reg lands in K3; H_M0 in K2",
        (esc["H_flat"]["reopens"], esc["H_reg"]["reopens"], esc["H_M0"]["reopens"]),
        (["K1"], ["K3"], ["K2"]))
    chk("chk", "no escape is listed twice, and no open row twice",
        (len(esc) == len(model["escapes"]),
         len([x for x in model["escapes"] if x["kind"] == "OPEN ROW"])
         == len(set(r for x in model["escapes"] if x["kind"] == "OPEN ROW"
                    for r in x["rows"]))), (True, True))
    chk("chk", "phase1.is_transition does not read passage_flux (accepted by definition)",
        phase1.is_transition(False, True, True, True, True, passage_flux=True)
        == phase1.is_transition(False, True, True, True, True, passage_flux=False), True)
    chk("chk", "no RE-ASK owner has moved", re_ask(model), [])

    print("\n8. CONTROLS -- EACH MUST CHANGE THE OUTPUT")
    base_head = model["headline"]

    def rerun():
        m = run()
        return m, m["verdicts"], m["headline"]

    with ledger_status("D4", SURVEY):
        m2, v2, h2 = rerun()
    chk("ctl", "ledger D4 -> SURVEY: K1 falls to OPEN, the headline moves",
        (v2["K1"]["verdict"], h2 != base_head), (OPEN_V, True))
    with ledger_status("D7", SURVEY):
        m2, v2, h2 = rerun()
    chk("ctl", "ledger D7 -> SURVEY: K1 falls to OPEN", v2["K1"]["verdict"], OPEN_V)
    with patched(foliation, "IDENTITY_DISPUTED", True):
        m2, v2, h2 = rerun()
    chk("ctl", "foliation.IDENTITY_DISPUTED -> True: K0 falls to OPEN, K1 (which "
        "never used D2) does not, the headline moves",
        (v2["K0"]["verdict"], v2["K1"]["verdict"], h2 != base_head),
        (OPEN_V, EMPTY_IF, True))
    with patched(drivensource, "CERTIFY_COROLLARY", "UNCHANGED"):
        m2, v2, h2 = rerun()
    chk("ctl", "drivensource corollary un-narrowed: K1 falls to OPEN (D4 refused)",
        (v2["K1"]["verdict"], "D4" in m2["facts_refused"]), (OPEN_V, True))
    with patched(spec, "seat_over_collapse", lambda l: 0.5):
        m2, v2, h2 = rerun()
    chk("ctl", "spec.seat_over_collapse -> 0.5: S-2 falls to OPEN, S-1 stays",
        (v2["S-2"]["verdict"], v2["S-1"]["verdict"]), (OPEN_V, NONEMPTY))
    with patched(fewsterteo, "O2_CLOSED", True):
        h2 = headline(model, model["verdicts"], model["entailment"])
    chk("ctl", "fewsterteo.O2_CLOSED -> True: the headline becomes RE-ASK",
        h2.startswith("RE-ASK"), True)
    with patched(candidates, "LIST_IS_EXHAUSTIVE", True):
        m2 = build()
    chk("ctl", "candidates.LIST_IS_EXHAUSTIVE -> True: R12's status moves off SURVEY",
        [r["status"].split(" ")[0] for r in m2["requirements"] if r["id"] == "R12"],
        [THEOREM])
    with patched(achievable, "M_OVER_B", 1.0e-80):
        m2 = run()
    chk("ctl", "achievable.M_OVER_B -> 1e-80: realisation (ii) leaves K1 for K6b",
        m2["realisation_ii"], "K6b")
    PENDING_REQUIREMENTS["chronology"] = True
    try:
        m2, v2, h2 = rerun()
    finally:
        PENDING_REQUIREMENTS["chronology"] = None
    chk("ctl", "if M ruled chronology a requirement, W-create-cc becomes EMPTY",
        (v2["W-create-cc"]["verdict"], v2["W-create-cc"]["facts"]),
        (EMPTY, ["GEROCH-BORDE"]))
    mm = copy.deepcopy(model)
    [K for K in mm["classes"] if K["id"] == "K1"][0]["hyps"].remove("H_reg")
    chk("ctl", "K1 with H_reg dropped from its stated hypotheses fails the check",
        [b[0] for b in hyp_check(mm, v)], ["K1"])
    mm = copy.deepcopy(model)
    [K for K in mm["classes"] if K["id"] == "K1"][0]["hyps"].remove("H_flat")
    chk("ctl", "K1 with H_flat dropped fails the check too",
        [b[:2] for b in hyp_check(mm, v)], [("K1", ["H_flat"])])
    mm = copy.deepcopy(model)
    [K for K in mm["classes"] if K["id"] == "K4"][0]["hyps"].append("H_flat")
    chk("ctl", "an OPEN class padded with an unused hypothesis fails the check",
        [b[0] for b in hyp_check(mm, v)], ["K4"])
    vv = copy.deepcopy(v)
    vv["K5"]["verdict"] = FORBIDDEN_STATUS_WORD
    chk("ctl", "a verdict of %s is caught" % FORBIDDEN_STATUS_WORD,
        declared_check(model, vv, "")[0], [FORBIDDEN_STATUS_WORD])
    chk("ctl", "the word %s in the printout is caught" % FORBIDDEN_STATUS_WORD,
        len(declared_check(model, v, "the rows " + FORBIDDEN_STATUS_WORD + " here")[1]), 1)
    mm = copy.deepcopy(model)
    [r for r in mm["requirements"] if r["id"] == "R2"][0]["applies_to"].append("S")
    chk("ctl", "R2 applied to S is caught by the scope check",
        scope_check(mm, v)[0], ["R2"])
    mm = copy.deepcopy(model)
    [K for K in mm["classes"] if K["id"] == "S-2"][0]["lits"] = {"ball": True}
    chk("ctl", "an EMPTY seat class that admits spec's witness is caught",
        scope_check(mm, v)[1], ["S-2"])
    mm = copy.deepcopy(model)
    [r for r in mm["requirements"] if r["id"] == "R1"][0]["rows"].remove("D10")
    chk("ctl", "a ledger row left unplaced (D10) is caught", placement(mm)[0], ["D10"])
    mm = copy.deepcopy(model)
    [r for r in mm["requirements"] if r["id"] == "R4"][0]["rows"].append("D2")
    chk("ctl", "a ledger row placed twice (D2) is caught", placement(mm)[1], ["D2"])
    mm = copy.deepcopy(model)
    [r for r in mm["requirements"] if r["id"] == "R4"][0]["see"].append("W1")
    chk("ctl", "a WITHDRAWN row relied on (W1) is caught", placement(mm)[2], ["W1"])
    extra = list(ledger.DEMAND) + [("D99", "a row this file never placed", OPEN,
                                    ("noise", "CORRIDOR_APPLICATION"), "-")]
    with patched(ledger, "DEMAND", extra):
        chk("ctl", "a NEW ledger row not yet placed turns the check red",
            placement(model)[0], ["D99"])
    chk("ctl", "a misquoted owner fragment is caught",
        misquotes((("bounds", "priced on the MAGNITUDE axis"),)),
        [("bounds", "priced on the MAGNITUDE axis")])
    with ledger_status("D5", SURVEY):
        m2 = build()
    chk("ctl", "ledger D5 -> SURVEY: SR3's status moves (D5 asked, not typed)",
        [r["status"] for r in m2["requirements"] if r["id"] == "SR3"]
        != [r["status"] for r in model["requirements"] if r["id"] == "SR3"], True)
    bal = ledger.balance
    with patched(ledger, "balance", lambda: [
            (r[0], r[1], r[2], r[3], "a supply figure") if r[0] == "B3" else r
            for r in bal()]):
        m2 = build()
    r12 = [r for r in m2["requirements"] if r["id"] == "R12"][0]
    chk("ctl", "ledger B3 given a supply figure: R12 prints B3 MEASURED and RE-ASK",
        ("B3 " + MEASURED in r12["status"], r12["statement"].startswith("RE-ASK")),
        (True, True))
    with patched(achievable, "M_OVER_B", 1.0e-3):
        _SLOW.clear()
        try:
            m2 = build()
        finally:
            _SLOW.clear()
    chk("ctl", "mu moved off concentric's edge: R4 prints RE-ASK for mu, not the edge",
        "RE-ASK -- the survey no longer places mu" in
        [r for r in m2["requirements"] if r["id"] == "R4"][0]["statement"], True)
    chk("chk", "H_M0 carries no flat-space clause; H_flat carries it (one escape)",
        ("flat space" in model["hyps"]["H_M0"][0].split("its remaining clause")[0],
         "flat" in model["hyps"]["H_flat"][0]), (False, True))
    chk("chk", "S-1 states its hypotheses (H_seat), and clause (3) prints them",
        (cls_hyps(model, "S-1"), "H_seat" in theorem_statement(model)), (["H_seat"], True))
    chk("z3", "W-create-cc forced to a CTC and W-create-ncc to a pathology (derived)",
        model["entailment"]["forced"], {"W-create-cc": ["ctc"],
                                        "W-create-ncc": ["pathology"]})
    chk("chk", "the T headline line is conditional on P4 and the hold",
        ("IF phase1's D3 is read per R1" in model["headline"]
         and "held for one light-crossing" in model["headline"]), True)
    chk("ctl", "a withdrawn figure printed bare is caught",
        len(withdrawn_lines("the lead is 65 orders short")), 1)
    mm = copy.deepcopy(model)
    [K for K in mm["classes"] if K["id"] == "K2"][0]["lits"]["m0"] = True
    pc = partition_check(mm)
    chk("ctl", "a class edited to overlap another breaks the z3 partition",
        bool(pc["C"]["overlap"]) and not pc["C"]["cover"], True)

    print()
    counts = dict((k, sum(1 for kk, _ in rows if kk == k))
                  for k in ("ask", "fig", "z3", "ctl", "pin", "chk"))
    summary = "%d checks: %s" % (len(rows), ", ".join("%d %s" % (c, k)
                                                       for k, c in counts.items()))
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
    sys.exit(report())
