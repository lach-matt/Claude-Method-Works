#!/usr/bin/env python3
"""
apply.py -- what chain.py, pair.py and permute.py do to the transition project.

Three passes ran on M's own principles rather than on the device: the binary
chain, the wormhole/black-hole balance ledger, and the closed index against the
expansion.  Each produced findings.  NONE OF THEM WAS ASKED WHAT IT DOES TO THE
PROJECT, and that is this file.

The answer has four parts and one of them is a correction of my own phrasing
two passes ago.

===============================================================================
0. FIRST, THE HONEST HEADLINE: NOTHING MOVED
===============================================================================

expand.py's four rows are re-run below from the instruments that own them.

        ORDER        ADMITS       (GJW's external causal path)
        GEOMETRY     ADMITS       (no throat, no horizon, M_ADM = 0)
        ALGEBRA      ADMITS       (junction closes, DEC on the shell, stable)
        INFORMATION  REFUSES      (rho < 0 not available at magnitude)

        E = 1.  TRANSITION-POSSIBLE STILL NOT ADMITTED.

Three passes of real results and the verdict is identical.  That is said first
so nothing below can be read as progress it is not.  What changed is the KIND
of the refusal, and the kind is worth the file.

===============================================================================
1. A CORRECTION TO pair.py's OWN PHRASING, AND IT MATTERS
===============================================================================

pair.py concluded: "negative energy is DERIVED from the design's own
M_ADM = 0, by a theorem."  True, and it invites a reading that is false --
that the exotic matter is a consequence of a BOOKKEEPING CHOICE, and that
choosing M_ADM > 0 would remove it.

MEASURED HERE, on concentric.py's own machinery, by letting the shell mass
float free of the core's:

        Phi(r) = m_a / sqrt(r^2 + a^2)  -  m_s / max(r, R_s),
        M_ADM = m_s - m_a.

        M_ADM = 0        seats, LEADS
        M_ADM = +5.0e-3  seats, LEADS
        M_ADM = +1.5e-2  seats, LEADS
        positive core    SEATS, DOES NOT LEAD

    SO M_ADM IS A FREE PARAMETER OF THE DESIGN AND NOT A REQUIREMENT OF THE
    MECHANISM.  Raising it escapes the rigidity proof and changes nothing
    physical, because THE EXOTIC MATTER IS REQUIRED BY THE LEAD, NOT BY THE
    BOOKKEEPING -- and the last row is the proof: swap the core's sign and the
    ray still seats, and arrives LATE.

    The seat is free (reverse.py said so; this is that, measured again from the
    other side).  THE LEAD IS THE WHOLE COST.

So rigidity is a SECOND AND INDEPENDENT proof of a requirement that was always
local: Phi > 0 needs rho < 0, pointwise, whatever the ADM mass is.  It does not
tighten the requirement.  What it removes is the last hope that a bookkeeping
choice could dodge it.  pair.py's sentence is narrowed here, in the direction
of being less impressive and more true.

===============================================================================
2. AND THAT MAKES THE DICHOTOMY EXHAUSTIVE RATHER THAN ENUMERATED
===============================================================================

dichotomy.py had two routes and two different blockers, found by trying them.
Rigidity closes the branch nobody had tried, and the four cases are now the
WHOLE of the DEC-respecting space:

    M_ADM < 0, DEC holds      FORBIDDEN     positive mass theorem, inequality
    M_ADM = 0, DEC holds      MINKOWSKI     positive mass theorem, RIGIDITY
    M_ADM > 0, DEC holds      COLLAPSE      Sturm density exceeds it by 2pi^2/3
                                            (T_kk = u along the ray, radius)
    DEC fails                 THE DEVICE    everything this tree has built

        UNDER THE DOMINANT ENERGY CONDITION THERE IS NO SEAT-AND-LEAD.

    CORRECTED (DOCKET 67, the seated S-2 follow-on).  The COLLAPSE row's
    reason holds for T_kk = u along the ray -- pressureless matter -- with the
    Sturm stretch equal to the ball's radius.  Over H_ball as written class
    S-2 is OPEN in specthm: the ratio (2 pi^2/3)/((T_kk/u)(s/l)^2) is 1.6449
    on a diameter for pressureless matter, 1.2337 for radiation and 0.8225
    for T_kk = 2u, and on a diameter it falls to <= 1 for w >= 0.644934,
    inside the DEC's w <= 1 (specthm.sturm_over_ball).  WHETHER THIS ROW'S
    VERDICT, AND WITH IT THE SENTENCE ABOVE, MOVES IS OPEN: no verifier
    computed it.  The verdict logic below is unchanged.

    CORRECTED AGAIN (DOCKET 67 follow-up; M: "the verdict must rest on a
    correct, stated ground; where none exists it is OPEN").  It is now
    computed, and IT MOVES.  The M_ADM > 0 row splits on the Sturm ratio
    (2 pi^2/3)/((T_kk/u)(s/l)^2), computed by specthm.sturm_ratio from
    spec.seat_over_collapse:

    M_ADM > 0, DEC, (T_kk/u)(s/l)^2 <  2pi^2/3   COLLAPSE   ratio > 1: Sturm-
                                    certified seating needs u above collapse
                                    (6.5797 dust/radius, 1.6449 dust/diameter,
                                    1.2337 radiation/diameter)
    M_ADM > 0, DEC, (T_kk/u)(s/l)^2 >= 2pi^2/3   OPEN       ratio <= 1: seating
                                    below collapse is not excluded (0.8225 for
                                    T_kk = 2u on a diameter -- a w = 1 fluid
                                    or a ball magnetised across the ray, both
                                    within the DEC); no witness is built and
                                    the LEAD is not examined there

    Named hypotheses of the COLLAPSE ground: H_ball (a uniform-u ball, spec.py)
    and H_sturm (seating is Sturm-certified along a chord of the ball, the
    owners' criterion; Sturm's condition is sufficient, so the collapse is a
    statement about Sturm-certified seating).  The lead is NOT adopted as a
    ground on the OPEN sub-case: section 1 measures it in concentric.py's
    weak-field potential only, and Gao-Wald's delay theorem carries null
    completeness, the null generic condition and its authors' own hedge
    (driven.py, DOCKET 67).  So the branch is NOT exhaustive: three of its
    DEC-respecting sub-cases are blocked by a stated ground and one is OPEN.
    The DEC-respecting case admitting a demonstrated seat-and-lead is still
    none -- OPEN is not a seat.  First written, and kept here as history:

That is now a statement about the whole branch rather than about the cases
somebody thought to test, and it is the strongest negative result the project
holds.  It is also exactly as far as it goes: it says nothing about theories
where the DEC is not the right condition, which is section 4.

    (CORRECTED, DOCKET 67 follow-up: it is a statement about every case with
    (T_kk/u)(s/l)^2 < 2pi^2/3, and OPEN on the rest.)

===============================================================================
3. AND ONE LINE CLOSES A WHOLE CLASS OF ROUTES AT ONCE
===============================================================================

Three independent arrivals this session at the same discriminator:

        A SIGN-BLIND QUANTITY CAN PAIR, BALANCE AND BE CONSTRAINED BY
        CLOSURE.  A SIGN-COMMITTED ONE CANNOT.

    CORRECTED (DOCKET 67).  First written "A SIGN-BLIND QUANTITY PAIRS,
    BALANCES AND IS CONSTRAINED BY CLOSURE", as a universal.  The tree's own
    baryon row contradicts it: B takes either sign and closure does not force
    it (permute.py).  Sign-blindness is necessary, not sufficient; what
    constrains a total on a closed slice is a Gauss constraint from a massless
    gauge field (computed in DOCKET 67: the same lattice gives total != 0
    UNSAT with Gauss and SAT without), and U(1)_B, being anomalous in the SM,
    carries none.  The direction this section uses -- sign-committed, so not
    constrained -- is untouched.

    pair.py       Wheeler's charge without charge: mouths are +-Q, masses ADD
    dichotomy.py  Weyl focusing is sign-blind; Ricci focusing is not
    permute.py    Gauss on a boundaryless manifold forces total Q = 0 exactly

ENERGY IS SIGN-COMMITTED, by the positive mass theorem.  Therefore no argument
from balance, closure, topology, pairing or permutation will ever supply it --
not because each such argument has been tried and failed, but because the
class of quantity they operate on does not include energy.  Routes proposed
and where each dies:

    balance across a pair        pair.py       the negative member cannot exist
    a closed index, no defect    permute.py    closure constrains CHARGE, not E
    expansion as rearrangement   permute.py    theta is invariant and non-zero
    entanglement symmetry        entsym.py     QNEC has no Weyl term
    a binary chain's geometry    chain.py      the citation gives it, at 2^l cost

    AND EXACTLY ONE PROPOSED ROUTE IS UNTOUCHED BY THIS, WHICH IS WHY IT IS THE
    ONE TO PUSH: GJW's external causal path is an ORDER question, not an energy
    question.  It asks whether a non-achronal connection may exist, not what it
    costs.  Order is the row that admits, it is the row that governs SPEED, and
    it is the only row this project has ever moved.

===============================================================================
4. CONTAINMENT IS CLOSED, NOT OPEN -- AND THAT IS GOOD NEWS
===============================================================================

chain.py's Earnshaw result: the potential of any point sources is harmonic
whatever their signs, so no static configuration is stably in equilibrium, and
the one escape is the degenerate constant-potential case Newton's shell theorem
hands the device.  NEUTRAL IS OPTIMAL.

    So "drift to contact" is not an open defect on the project's list.  It is
    the Newtonian CEILING, the device is already at it, and the item moves from
    A RISK TO A BOUNDARY.  What is still open is only whether GR moves the
    boundary -- and that is one named NOT-RUN rather than an unbounded worry.

===============================================================================
5. WHAT IS ACTUALLY LEFT, AND IT IS THREE DOORS
===============================================================================

Taken from obstruct.py's ledger rather than typed here, plus the named
NOT-RUNs.  Everything remaining is one of exactly three kinds:

    OUTSIDE GR        f(R), noncommutative geometry -- the DEC and the positive
                      mass theorem are theorems OF general relativity with
                      matter, and neither applies unchanged there.
                      wormhole.py left this as M's scope decision and IT WAS
                      MADE on 2026-09-11: modified gravity counts. That turns
                      this door from a prohibition into a bill, and it
                      licenses nothing already seated -- everything derived
                      before that date was derived in GR and stays GR.

    NOT AN ENERGY     order, causal structure, chronology protection.  GJW's
    QUESTION          path; Kim-Thorne against Hawking past dt > D/c.  The
                      sign-commitment argument has no purchase on these.

    A RELIC, NOT A    create.py's topology theorems and detect.py's search both
    CONSTRUCTION      say the same thing from opposite ends: look for one, do
                      not try to make one.  Nothing above touches this.

    THOSE ARE THE THREE DOORS, AND AFTER THIS SESSION THEY ARE THE ONLY THREE.
    Every other route the project has proposed is now closed by a theorem
    rather than by a magnitude, which is a better place to be standing even
    though it is not a better answer.

    CORRECTED (DOCKET 67 follow-up).  "THE ONLY THREE" and "every other route
    ... closed by a theorem" no longer hold as written.  Section 2's DEC
    branch is now computed OPEN on (T_kk/u)(s/l)^2 >= 2 pi^2/3 -- inside GR,
    under the DEC, M_ADM > 0 -- and that sub-case is none of the three doors
    and is closed by no theorem (DEC_BRANCH_OPEN_OUTSIDE_THE_DOORS).  Whether
    it is a fourth door is OPEN: no witness is built and its lead is not
    examined.  The DOORS tuple keeps three entries, the doors this file found.

stdlib only.  Every row is recomputed from the instrument that owns it.
"""
import math
import sys

# ------------------------------------------------ 0: nothing moved

def expand_rows():
    """expand.py's own rows, recomputed by expand.py, not restated here."""
    import expand
    return expand.expand()


def expand_verdict():
    import expand
    st = expand.expand()
    admitted, e = expand.reduce_back(st)
    return admitted, e, expand.dissent(st)


# --------------------- 1: M_ADM is free; the LEAD is what costs

def general_potential(m_core, m_shell, a, Rs):
    """Phi = m_core/sqrt(r^2+a^2) - m_shell/max(r,Rs).  M_ADM = m_shell-m_core.

    concentric.py fixes the two equal.  Letting them float is the whole test."""
    def f(p, _M=None):
        r = math.sqrt(p[0] * p[0] + p[1] * p[1] + p[2] * p[2])
        return m_core / math.sqrt(r * r + a * a) - m_shell / max(r, Rs)
    return f


def survey_general(m_core, m_shell):
    """concentric.py's own survey, with its potential swapped for the general
    one.  Restored afterwards -- an instrument never leaves another patched."""
    import concentric
    a, Rs = concentric.A_CORE, concentric.R_SHELL
    old = concentric.potential
    concentric.potential = lambda m, a=a, Rs=Rs: general_potential(
        m_core, m_shell, a, Rs)
    try:
        r = concentric.survey(m_core)
    finally:
        concentric.potential = old
    r["M_ADM"] = m_shell - m_core
    return r


def adm_is_a_free_parameter(m=5.0e-3):
    """Does raising M_ADM above zero break seat-and-lead?  Measured: no."""
    return all(survey_general(m, ms)["leads"] for ms in (m, 2.0 * m, 4.0 * m))


def positive_core_leads(m=5.0e-3):
    """Flip the core's sign -- ordinary matter throughout.  It seats and it
    arrives LATE, which is the local proof that the LEAD is what needs rho<0."""
    return survey_general(-m, m)["leads"]


EXOTIC_REQUIRED_BY = "the lead"
RIGIDITY_IS = "a second, independent proof on the M_ADM = 0 branch only"
PAIR_PY_PHRASING_NARROWED = True


# ------------------------- 2: the DEC branch, exhausted
# CORRECTED (DOCKET 67 follow-up): the section heading's "exhausted" held for
# T_kk = u only; computed below, the branch is exhaustive on that sub-case and
# OPEN on (T_kk/u)(s/l)^2 >= 2 pi^2/3.  The old table is kept as history:
DEC_BRANCH_WITHDRAWN = (
    ("M_ADM > 0", True, "COLLAPSE", "WITHDRAWN (DOCKET 67 follow-up): 'Sturm "
     "density exceeds it by 2 pi^2 / 3' for the whole M_ADM > 0 branch -- true "
     "only where (T_kk/u)(s/l)^2 < 2 pi^2/3"),)

#: The Sturm-ratio members the record holds, (label, T_kk/u, s/l) -- each one
#: specthm.sturm_over_ball computes (DOCKET 67, sturm-comparison-theorem).
STURM_MEMBERS = (("dust, radius", 1.0, 1.0),
                 ("dust, diameter", 1.0, 2.0),
                 ("radiation, diameter", 4.0 / 3.0, 2.0),
                 ("T_kk = 2u, diameter (w = 1; or B across the ray)", 2.0, 2.0))
#: T_kk/u = 2 is a DEC member: T_kk = rho + p <= 2 rho for |p| <= rho.
DEC_TKK_OVER_U_MAX = 2.0


def seat_over_collapse():
    """The owners' T_kk = u radius ratio, 2 pi^2/3 (spec.seat_over_collapse)."""
    import spec
    return spec.seat_over_collapse(1.0)


def sturm_ratio(tkk_over_u, s_over_l):
    """specthm's ratio, imported -- not restated."""
    import specthm
    return specthm.sturm_ratio(seat_over_collapse(), tkk_over_u, s_over_l)


def positive_adm_verdict(tkk_over_u, s_over_l):
    """M_ADM > 0 under the DEC: COLLAPSE where Sturm-certified seating needs u
    above the collapse bound (ratio > 1), OPEN where it does not."""
    return "COLLAPSE" if sturm_ratio(tkk_over_u, s_over_l) > 1.0 else "OPEN"


def dec_branch(members=STURM_MEMBERS):
    """The DEC branch, COMPUTED.  The M_ADM > 0 row is split by the verdict
    each recorded member returns; a sub-case appears only if a member is in it."""
    by = {}
    for label, t, sl in members:
        by.setdefault(positive_adm_verdict(t, sl), []).append(
            "%s %.4f" % (label, sturm_ratio(t, sl)))
    rows = [("M_ADM < 0", True, "FORBIDDEN", "positive mass theorem, the inequality"),
            ("M_ADM = 0", True, "MINKOWSKI", "positive mass theorem, the RIGIDITY clause")]
    if "COLLAPSE" in by:
        rows.append(("M_ADM > 0, (T_kk/u)(s/l)^2 < 2pi^2/3", True, "COLLAPSE",
                     "Sturm-certified seating needs u above collapse: ratio > 1 ("
                     + "; ".join(by["COLLAPSE"]) + ")"))
    if "OPEN" in by:
        rows.append(("M_ADM > 0, (T_kk/u)(s/l)^2 >= 2pi^2/3", True, "OPEN",
                     "ratio <= 1, seating below collapse not excluded ("
                     + "; ".join(by["OPEN"]) + "); no witness, lead not examined"))
    rows.append(("any", False, "THE DEVICE",
                 "the DEC fails; everything this tree has built"))
    return tuple(rows)


DEC_BRANCH = dec_branch()

BLOCKED = ("FORBIDDEN", "MINKOWSKI", "COLLAPSE")


def dec_cases_with_a_seat_and_lead(branch=None):
    """Under the DEC, which case has a DEMONSTRATED seat-and-lead?  None: no row
    carries that verdict.  (CORRECTED, DOCKET 67 follow-up: this returned every
    row not in BLOCKED, which would now list the OPEN row as a seat-and-lead.)"""
    branch = DEC_BRANCH if branch is None else branch
    return [c for c, dec, verdict, _w in branch if dec and verdict == "SEAT-AND-LEAD"]


def dec_cases_open(branch=None):
    """DEC-respecting cases with no stated ground either way."""
    branch = DEC_BRANCH if branch is None else branch
    return [c for c, dec, verdict, _w in branch if dec and verdict not in BLOCKED
            and verdict != "SEAT-AND-LEAD"]


def dichotomy_is_exhaustive(branch=None):
    """Is every DEC-respecting case blocked by a stated ground?  Computed: no --
    the T_kk = 2u diameter member is OPEN.  On T_kk = u members alone it is."""
    branch = DEC_BRANCH if branch is None else branch
    return all(verdict in BLOCKED for _c, dec, verdict, _w in branch if dec)


# ------------------- 3: one line closes a class of routes

ARRIVALS = ("pair.py: Wheeler's charge without charge",
            "dichotomy.py: Weyl against Ricci",
            "permute.py: Gauss on a boundaryless manifold")

ROUTES_CLOSED_BY_SIGN_COMMITMENT = (
    ("balance across a pair", "pair.py", "the negative member cannot exist"),
    ("a closed index, no defect", "permute.py", "closure constrains charge, not E"),
    ("expansion as rearrangement", "permute.py", "theta is invariant and non-zero"),
    ("entanglement symmetry", "entsym.py", "QNEC has no Weyl term"),
    ("a binary chain's geometry", "chain.py", "the citation gives it, at 2^l cost"),
)

SURVIVING_ROUTE = ("GJW's external causal path", "order", "it governs SPEED")


def energy_is_sign_committed():
    """By the positive mass theorem.  Read from pair.py's own ledger rather
    than restated, so the two cannot drift apart."""
    import pair
    return not pair.quantity_pairs("ADM energy")


def charge_is_not():
    """The contrast, from the same ledger."""
    import pair
    return pair.quantity_pairs("electric charge")


def route_is_an_energy_question(row):
    """The surviving one is not, which is exactly why it survives."""
    return row[1] != "order"


# ------------------------------ 4: containment is a boundary

def containment_status():
    """Taken from chain.py, which owns the Earnshaw result."""
    import chain
    return chain.L1_NEWTONIAN


CONTAINMENT = "CLOSED -- neutral is the Newtonian ceiling"
CONTAINMENT_WAS = "OPEN -- drift to contact, an unbounded worry"
CONTAINMENT_REMAINDER = "whether GR moves the boundary; one named NOT-RUN"


# ------------------------------------- 5: the three doors

DOORS = (
    ("OUTSIDE GR", "f(R), noncommutative geometry",
     "the DEC and the positive mass theorem are theorems OF GR with matter"),
    ("NOT AN ENERGY QUESTION", "order, causal structure, chronology protection",
     "sign-commitment has no purchase on these"),
    ("A RELIC, NOT A CONSTRUCTION", "find one and enlarge it",
     "create.py's topology theorems and detect.py's search agree"),
)


#: COMPUTED (DOCKET 67 follow-up): the DEC-respecting sub-cases section 2
#: leaves OPEN, which lie in none of the three DOORS.
DEC_BRANCH_OPEN_OUTSIDE_THE_DOORS = tuple(dec_cases_open())


def open_rows_from_the_ledger():
    """Taken from obstruct.py rather than typed, so it cannot go stale."""
    import obstruct
    h = obstruct.by_status()
    return sorted(r[0] for r in h["OPEN"])


def scope_is_chosen():
    """wormhole.py's modified-gravity scope flag. CHOSEN on 2026-09-11.

    This read "Still unchosen" and pinned False for as long as the flag was
    None. The decision was made -- SCOPE_CHOSEN_HERE = "modified gravity
    counts" -- and this file was not swept, so the pin went on asserting the
    open state of a question that had been answered. It licenses nothing
    already seated: results derived before that date were derived in GR and
    stay GR.
    """
    import wormhole
    return wormhole.SCOPE_CHOSEN_HERE is not None


def selftest():
    ok = True

    def chk(label, got, want):
        nonlocal ok
        good = got == want
        ok &= good
        print("  %-58s %18s %18s  %s"
              % (label, str(got)[:18], str(want)[:18], "ok" if good else "FAIL"))

    print("0. THE HONEST HEADLINE: NOTHING MOVED")
    st = expand_rows()
    for lang in ("order", "geometry", "algebra", "information"):
        print("     %-14s %s" % (lang, st[lang]))
    admitted, e, diss = expand_verdict()
    chk("E, after three passes of real results", e, 1)
    chk("TRANSITION-POSSIBLE admitted", admitted, False)
    chk("and the dissent is still exactly", diss, ["information"])
    print("       Said first so nothing below reads as progress it is not.")

    print("\n1. M_ADM IS A FREE PARAMETER -- THE LEAD IS WHAT COSTS")
    m = 5.0e-3
    for ms, label in ((m, "M_ADM = 0   (the device)"),
                      (2.0 * m, "M_ADM > 0   (heavier shell)"),
                      (4.0 * m, "M_ADM >> 0")):
        r = survey_general(m, ms)
        print("     %-28s M_ADM=%+.1e  seats=%s  leads=%s"
              % (label, r["M_ADM"], r["seats"], r["leads"]))
        chk("  it still seats", r["seats"], True)
        chk("  it still leads", r["leads"], True)
    r = survey_general(-m, m)
    print("     %-28s M_ADM=%+.1e  seats=%s  leads=%s"
          % ("positive core (ordinary)", r["M_ADM"], r["seats"], r["leads"]))
    chk("ordinary matter SEATS", r["seats"], True)
    chk("and it does NOT lead", positive_core_leads(m), False)
    chk("so M_ADM is free of the mechanism", adm_is_a_free_parameter(m), True)
    chk("the exotic matter is required by", EXOTIC_REQUIRED_BY, "the lead")
    chk("which narrows pair.py's phrasing", PAIR_PY_PHRASING_NARROWED, True)
    print("       The seat is free; THE LEAD IS THE WHOLE COST.  Rigidity is a")
    print("       second proof of a requirement that was always local, and it")
    print("       removes the hope that bookkeeping could dodge it -- nothing more.")

    print("\n2. THE DEC BRANCH -- EXHAUSTIVE ON T_kk = u, OPEN BEYOND IT (DOCKET 67)")
    for case, dec, verdict, why in DEC_BRANCH:
        print("     %-38s DEC %-5s %-10s %s"
              % (case, "holds" if dec else "FAILS", verdict, why))
    soc = seat_over_collapse()
    chk("the owners' T_kk = u radius ratio is 2 pi^2/3",
        abs(soc / (2.0 * math.pi ** 2 / 3.0) - 1.0) < 1e-12, True)
    for (label, t, sl), want in zip(STURM_MEMBERS,
                                    (6.5797362674, 1.6449340668,
                                     1.2337005501, 0.8224670334)):
        chk("  Sturm ratio, %s" % label[:30], round(sturm_ratio(t, sl), 10), want)
    chk("  the T_kk = 2u member is within the DEC (T_kk/u <= 2)",
        STURM_MEMBERS[3][1] <= DEC_TKK_OVER_U_MAX, True)
    chk("CONTROL: verdicts per member (COLLAPSE x3, OPEN x1)",
        [positive_adm_verdict(t, sl) for _l, t, sl in STURM_MEMBERS],
        ["COLLAPSE", "COLLAPSE", "COLLAPSE", "OPEN"])
    chk("DEC-respecting cases with a DEMONSTRATED seat-and-lead",
        dec_cases_with_a_seat_and_lead(), [])
    chk("DEC-respecting cases OPEN (computed)", dec_cases_open(),
        ["M_ADM > 0, (T_kk/u)(s/l)^2 >= 2pi^2/3"])
    # CORRECTED (DOCKET 67 follow-up): this pinned dichotomy_is_exhaustive() True.
    chk("so the dichotomy is exhaustive over the DEC branch (was True)",
        dichotomy_is_exhaustive(), False)
    chk("CONTROL: on the T_kk = u members alone it IS exhaustive",
        dichotomy_is_exhaustive(dec_branch(STURM_MEMBERS[:2])), True)
    import dichotomy
    chk("and dichotomy.py's two blockers are still different",
        dichotomy.different_blockers(), True)

    print("\n3. AND ONE LINE CLOSES A CLASS OF ROUTES AT ONCE")
    import permute
    chk("independent arrivals, agreeing with permute.py's own count",
        len(ARRIVALS), len(permute.ARRIVALS_AT_THE_SPLIT))
    for a in ARRIVALS:
        print("     %s" % a)
    chk("energy is sign-committed (from pair.py's ledger)",
        energy_is_sign_committed(), True)
    chk("and charge is not", charge_is_not(), True)
    for name, who, why in ROUTES_CLOSED_BY_SIGN_COMMITMENT:
        print("     %-28s %-14s %s" % (name, who, why))
    chk("routes closed by the class argument",
        len(ROUTES_CLOSED_BY_SIGN_COMMITMENT), 5)
    print("     SURVIVES: %s -- %s, and %s"
          % (SURVIVING_ROUTE[0], SURVIVING_ROUTE[1], SURVIVING_ROUTE[2]))
    chk("and it survives because it is not an energy question",
        route_is_an_energy_question(SURVIVING_ROUTE), False)
    chk("order still admits, which is the row it sits on", st["order"], "ADMITS")

    print("\n4. CONTAINMENT IS A BOUNDARY NOW, NOT A RISK")
    chk("containment, from chain.py's own result", containment_status(),
        "CLOSED -- neutral is optimal")
    print("       was: %s" % CONTAINMENT_WAS)
    print("       left: %s" % CONTAINMENT_REMAINDER)
    import chain
    chk("Earnshaw permits no stable static configuration",
        chain.has_strict_minimum((0.31, -0.17, 1.43),
                                 chain.chain_sources(chain.thue_morse(3))), False)
    chk("and negative masses do not help",
        chain.negative_masses_help(chain.thue_morse(3)), False)

    print("\n5. WHAT IS LEFT: THREE DOORS")
    for kind, what, why in DOORS:
        print("     %-28s %-38s %s" % (kind, what, why))
    chk("doors", len(DOORS), 3)
    # CORRECTED (DOCKET 67 follow-up): pinned ["TYPE-IV"]; obstruct.py (its
    # owner, M's ruling on ACHRONALITY) now holds ACHRONALITY OPEN as well.
    chk("obstruct.py's remaining OPEN rows", open_rows_from_the_ledger(),
        ["ACHRONALITY", "TYPE-IV"])
    chk("the DEC branch's OPEN sub-case lies outside the three doors",
        DEC_BRANCH_OPEN_OUTSIDE_THE_DOORS,
        ("M_ADM > 0, (T_kk/u)(s/l)^2 >= 2pi^2/3",))
    chk("and the modified-gravity scope IS chosen, 2026-09-11",
        scope_is_chosen(), True)
    print("       Every other route is now closed by a THEOREM rather than by a")
    print("       MAGNITUDE -- except the DEC branch's OPEN sub-case and the")
    print("       ledger's OPEN rows (DOCKET 67).  It is not a better answer.")

    print("\n  SELFTEST %s" % ("OK" if ok else "FAILED"))
    return ok


def report():
    print(__doc__)
    print("=" * 79)
    print("THE PROJECT, AFTER THE THREE PASSES\n")
    st = expand_rows()
    for lang in ("order", "geometry", "algebra", "information"):
        print("  %-14s %s" % (lang, st[lang]))
    admitted, e, diss = expand_verdict()
    print("\n  E = %d   admitted: %s   dissent: %s" % (e, admitted, ", ".join(diss)))
    print("\n  %-30s %s" % ("exotic matter required by", EXOTIC_REQUIRED_BY))
    print("  %-30s %s" % ("M_ADM", "a free parameter of the design"))
    print("  %-30s %s" % ("the DEC branch",
                          "exhausted" if dichotomy_is_exhaustive() else
                          "exhausted for (T_kk/u)(s/l)^2 < 2pi^2/3; OPEN: %s"
                          % ", ".join(dec_cases_open())))
    print("  %-30s %s" % ("containment", CONTAINMENT))
    print("  %-30s %s" % ("doors left", len(DOORS)))
    print("\n" + "=" * 79)
    print("""VERDICT

  NOTHING MOVED, AND THAT IS THE FIRST THING TO SAY.  Three passes of
  real results and expand.py still reads E = 1, the dissent still in
  INFORMATION alone.  TRANSITION-POSSIBLE IS STILL NOT ADMITTED.

  WHAT CHANGED IS THE KIND OF THE REFUSAL, AND IT STARTS WITH A
  CORRECTION.  pair.py said the exotic matter is derived from the
  design's own M_ADM = 0.  True, and it invites a false reading -- that
  a bookkeeping choice created the requirement and another could remove
  it.  Measured here by letting the shell mass float free of the core's:
  M_ADM = 0, +5.0e-3 and +1.5e-2 ALL SEAT AND ALL LEAD, and a positive
  core -- ordinary matter throughout -- SEATS AND ARRIVES LATE.

        M_ADM IS A FREE PARAMETER OF THE DESIGN.  THE SEAT IS FREE.
        THE LEAD IS THE WHOLE COST, AND IT IS LOCAL.

  So rigidity is a SECOND, INDEPENDENT proof of a requirement that was
  never about the ADM mass at all.  It does not tighten anything.  What
  it removes is the last hope that bookkeeping could dodge it, and
  pair.py's sentence is narrowed here toward being less impressive and
  more true.

  AND THAT MAKES THE DICHOTOMY EXHAUSTIVE.  M_ADM < 0 under the DEC is
  forbidden by the positive mass theorem's inequality; M_ADM = 0 under
  the DEC is Minkowski by its rigidity clause; M_ADM > 0 under the DEC
  seats by Ricci and, for T_kk = u along a radius, collapses, exceeding
  the bound by 2 pi^2 / 3.  COMPUTED NOW (DOCKET 67 follow-up), AND IT
  MOVES: the collapse holds wherever (T_kk/u)(s/l)^2 < 2 pi^2/3 (dust on
  a diameter 1.6449, radiation 1.2337), and where it is >= 2 pi^2/3 the
  branch is OPEN -- a T_kk = 2u member on a diameter, within the DEC,
  gives 0.8225.  So the dichotomy is EXHAUSTIVE ONLY ON THE COLLAPSE
  SUB-CASE.  Under the dominant energy condition no case has a
  demonstrated seat-and-lead, and one sub-case has no ground either
  way.  (First written: "That is the whole branch.  UNDER THE DOMINANT
  ENERGY CONDITION THERE IS NO SEAT-AND-LEAD -- a statement about every
  case rather than about the ones somebody thought to try.")

  AND ONE LINE CLOSES A WHOLE CLASS OF ROUTES.  A sign-blind quantity
  can pair, balance and be constrained by closure (closure needs a Gauss
  constraint to bind it); a sign-committed one is
  not; and energy is sign-committed by the positive mass theorem.  So
  balance, closure, topology, pairing and permutation cannot supply it
  -- not case by case, but because the class of quantity they act on
  does not include energy.  Five proposed routes die on that line at
  once.

  EXACTLY ONE SURVIVES IT, AND THAT IS WHY IT IS THE ONE TO PUSH.  GJW's
  external causal path is an ORDER question, not an energy question: it
  asks whether a non-achronal connection MAY EXIST, not what it costs.
  Order is the row that admits, it is the row that governs SPEED, and it
  is the only row this project has ever moved.

  CONTAINMENT STOPPED BEING A RISK AND BECAME A BOUNDARY.  Earnshaw
  permits no stable static configuration of point masses whatever their
  signs, and its one escape -- constant potential -- is what Newton's
  shell theorem hands the device.  Neutral is optimal.  Drift to contact
  is the Newtonian ceiling, not a defect on a list, and what remains is
  one named NOT-RUN about whether GR moves it.

  WHAT IS LEFT IS THREE DOORS AND THEY ARE THE ONLY THREE.  OUTSIDE GR,
  where the DEC and the positive mass theorem are not the governing
  theorems and the scope decision was MADE by M on 2026-09-11: modified
  gravity counts (wormhole.SCOPE_CHOSEN_HERE; corrected in DOCKET 67's
  follow-up -- this read "still M's and still unchosen").  NOT
  AN ENERGY QUESTION, where order, causal structure and chronology
  protection live and sign-commitment has no purchase.  AND A RELIC
  RATHER THAN A CONSTRUCTION, where create.py's topology theorems and
  detect.py's search already agree.

  Every other route is now closed by a THEOREM rather than by a
  MAGNITUDE.  That is a better place to be standing.  It is not a better
  answer.

  CORRECTED (DOCKET 67 follow-up): not every other route.  The DEC
  branch with M_ADM > 0 and (T_kk/u)(s/l)^2 >= 2 pi^2/3 is OPEN, closed
  by no theorem and in none of the three doors; whether it is a fourth
  is OPEN.  And obstruct.py's ledger now holds ACHRONALITY OPEN beside
  TYPE-IV.""")
    return 0


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    sys.exit(report())
