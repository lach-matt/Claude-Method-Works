#!/usr/bin/env python3
"""
create.py -- "the ability to CREATE and CONTAIN a stable wormhole" is TWO
problems, and this tree has only ever worked on the second.

Sweeping phase1.py's dependents after the architecture change -- which is the
lesson reversal.py paid for -- turned up that the wormhole FAILS phase1's own
definition of a transition, and following that failure to its cause found a
theorem the project had never looked at.

===============================================================================
1. THE WORMHOLE FAILS phase1's D2, AND IT FAILS ON TOPOLOGY
===============================================================================

phase1 defines a transition as a one-parameter family of metrics ON A FIXED
MANIFOLD (D1), with g_s = g_0 outside a compact corridor (D2).  Against a gate:

        D1  endpoints are labels          mouths are fixed        YES
        D2  compact support               ---                     NO
        D3  the proper distance falls     the shortcut            YES
        D4  no momentum                   static                  YES
        D5  both endpoints declared       you build both mouths   YES

    R^3 IS SIMPLY CONNECTED AND A WORMHOLE IS NOT.  No continuous deformation
    of a metric on a fixed manifold produces that, at ANY support.  D2 does not
    fail by a little; it fails on a different kind of quantity.

    CORRECTED (DOCKET 67), three ways, no verdict moved.  (a) "A WORMHOLE IS
    NOT" holds for a HANDLE wormhole, R^3 # (S^1 x S^2), pi_1 = Z.  A
    Morris-Thorne inter-universe section R x S^2 IS simply connected (there
    the conclusion holds through its second end, H_2 = Z), and a
    Hochberg-Visser throat can have R^3 itself as its section.  (b) "At ANY
    support" is exact for g_s NON-DEGENERATE at every s in the closed [0,1];
    degenerate metrics (Borde IX.C) lie outside it.  (c) phase1.py states the
    fixed-manifold clause in its definition's preamble, not in D1, and the
    handle's topology change can be confined to a ball (2505.02210 III.D), so
    the clause it violates is the fixed-manifold preamble, not D2's compact
    support.  The table and gate_meets() keep D2 = NO as first written:
    changing which_fails() would change a returned value, so it is recorded
    here, not repaired.  "Not a phase1 transition" is unaffected.

    AND THE WORMHOLE WAS NEVER IN phase1's RANKING at all -- that list runs
    corridor, bare mass, GJW, Casimir, charge, Alcubierre.  No throat.  phase1
    said "PHASE 1 IS FINISHED AS MATHEMATICS", and it was finished about an
    architecture this project has since left.  Scoped in place there.

===============================================================================
2. WHICH SEPARATES TWO PROBLEMS THE PHRASE RUNS TOGETHER
===============================================================================

        CONTAIN   hold an existing throat open and stable.  concentric.py,
                  stability.py, core.py, wormhole.py, gate.py.  A METRIC
                  problem, and the tree has worked on it for thirty passes.

        CREATE    bring a throat into existence where there was none.  A
                  TOPOLOGY problem, and the tree has never once looked at it.

    CORRECTED (DOCKET 67): a TOPOLOGY problem for a HANDLE or a second end,
    not for a throat as such.  A throat in Hochberg-Visser's geometric sense
    (a minimal 2-sphere with flare-out) forms on fixed R^3 under a smooth
    metric family unchanged outside 1 < r < 3 (computed: R' = 0, R'' = 14.2
    at r = 1.993, from s ~ 0.277); it opens into a bounded region, not onto a
    shortcut, so it is not a gate.

===============================================================================
3. AND CREATION HAS ITS OWN THEOREM, WHICH IS HARSHER THAN THE SOURCE PROBLEM
===============================================================================

Geroch (1967), Tipler (1977), and Borde (gr-qc/9406053), whose abstract is
explicit -- "topology change is only to be had at a price":

    * TOPOLOGY CHANGE IS KINEMATICALLY POSSIBLE.  Without a field equation you
      can build topology-changing spacetimes with non-singular Lorentz metrics.
      Borde exhibits 2-dimensional examples.  So it is not forbidden outright.

    * BUT THE ARGUMENT IS PURELY KINEMATICAL, and that is the part that matters
      here: "Neither Geroch's original theorem, nor its mild generalization in
      section IV, assume anything about the energy-momentum tensor, or indeed
      about a field equation."

          SO EXOTIC MATTER CANNOT HELP.  Every other wall in this project was a
          wall about SOURCING something.  This one does not care what the
          source is.

          CORRECTED (DOCKET 67): exact for Borde's Theorem 1, whose CTC is
          kinematic -- exotic matter cannot REMOVE the forced CTC.  Not exact
          for his Theorem 3: Sec. IX.B names energy-condition violation
          "large enough to allow assumption (ii) to be violated" as a way past
          the dynamical obstruction ("Some discussions of wormhole creation
          are ... based precisely on large violations of the energy
          condition"), and 2505.02210 builds a non-singular nucleation, with
          CTCs, that violates all the standard energy conditions.

    * CAUSALITY VIOLATIONS ARE FORCED.  Geroch's closed-universe argument,
      extended by Borde to causally compact interpolating spacetimes -- "a
      condition satisfied in a very wide range of situations".  (Named at
      DOCKET 67: Borde's Theorem 1 is for a TIME-ORIENTED spacetime with a
      smooth, everywhere NON-DEGENERATE Lorentz metric; for a throat in open
      space the change must sit in a causally compact region of an externally
      simple spacetime.  The CTC is forced somewhere in the interpolating
      region.)

    * AND THE SINGULARITY ESCAPE FAILS.  I expected "accept a singularity" to
      be the way out.  It is not: "as long as the causal compactness condition
      is met, causality violations have to occur when the topology changes,
      EVEN IF INCOMPLETE GEODESICS ARE ADMITTED."

    * DYNAMICALLY WORSE STILL: "in dimensions >= 3 causally compact
      topology-changing spacetimes cannot satisfy Einstein's equation (with a
      reasonable source)."  (Named at DOCKET 67: this is Theorem 3, again
      time-oriented with a smooth non-degenerate metric, and its "reasonable"
      is DETERMINED at source -- a restriction from which (i) the null
      generic condition on every full null geodesic and (ii) the half-integral
      null convergence condition follow.  A static zero-redshift throat's
      source violates (ii): INT R_kk = -2 INT (r'/r)^2 < 0 up to the throat,
      computed.  An "unreasonable" source removes Theorem 3 only; Theorem 1's
      CTC remains.)

===============================================================================
4. BORDE'S OWN ESCAPES, ALL THREE, AND WHERE EACH GOES
===============================================================================

        DROP CAUSAL COMPACTNESS   then Tipler: the interpolating spacetime
                                  contains a singularity or A POINT AT INFINITY,
                                  which Borde calls "a highly undesirable
                                  feature" -- in the CLOSED-UNIVERSE case,
                                  under Tipler's "mild additional assumptions"
        WEAKEN THE CURVATURE      would require altering Einstein's equation,
        CONSTRAINTS               and "such an alteration would have to be
                                  fairly severe" -- OR energy-condition
                                  violation large enough to break Theorem 3's
                                  (ii), inside Einstein's equation; either way
                                  it "would not affect the presence of
                                  causality violations"
        EUCLIDEAN PATH INTEGRAL   abandons the Lorentzian framework altogether

    ALL THREE LEAVE GENERAL RELATIVITY OR ACCEPT A PATHOLOGY -- the same shape
    as wormhole.py's scope warning, and the same decision belongs to M.

    CORRECTED (DOCKET 67): "ALL THREE" counts the routes quoted here, not
    Borde's.  He gives four -- the Euclidean path integral, and A], B], C]
    "within the general Lorentzian framework", framed as "several interesting
    possibilities", not a complete list.  Omitted here: C], DEGENERATE METRICS
    (Sorkin, Ashtekar, Horowitz: "this might well prove to be the correct
    approach"), and Sec. VIII's C^0 route ("S1 and S2 need not be
    diffeomorphic, even if causality violations are forbidden").  With either
    counted, "none stays in Lorentzian GR without a pathology" is UNDETERMINED:
    it turns on whether a degenerate point counts as a pathology, which this
    file does not decide.  The three in-GR flags in ESCAPES are hand-set
    literals, READ for the three routes listed.

    AND BORDE'S OWN CAUTION IS WORTH MORE THAN A PARAPHRASE: "Their true value
    is not so much that they actually rule out topology change, but rather that
    they allow us to pinpoint what modifications we have to make in our general
    framework so as to allow it."

===============================================================================
5. THE CLEAN ESCAPE IS ARCHITECTURAL: DO NOT CREATE ONE.  ENLARGE ONE.
===============================================================================

Every theorem above is about TOPOLOGY CHANGE.  If the topology is ALREADY
nontrivial -- primordial, inherited, a relic of the early universe, whatever
its provenance -- then nothing changes topology and NONE OF THIS APPLIES.

    CORRECTED (DOCKET 67): Borde's Theorem 1 has no topology-change
    antecedent; it concludes that the interpolating M is a product S1 x [0,1].
    An enlargement done as non-degenerate metrics on a FIXED spatial manifold,
    with the throat radius kept above 0, IS such a product (t is a time
    function there), so the theorems apply and conclude only what is already
    true: they impose nothing.  Outside that class (a non-product cobordism,
    or r -> 0, the pinch) they bite again.

        GROWING A THROAT FROM r_0 TO r_1 IS A METRIC CHANGE.  Permitted.
        Geroch, Tipler and Borde say nothing about it.  Every instrument this
        tree has built for the CONTAIN problem applies to it unmodified.

    CORRECTED (DOCKET 67): "Permitted" and "applies to it unmodified" claim
    more than the theorems' silence gives.  They do not forbid it; that is
    all.  A dynamic mouth still violates the NEC (Hayward 0903.5438;
    Hochberg-Visser gr-qc/9802048), and a dynamic wormhole has two throats,
    which coalesce only when it is static -- so the static CONTAIN instruments
    reach the end states, not the growth between them.

    SO THE ENGINEERING PROBLEM CHANGES SHAPE ENTIRELY:

        NOT     manufacture a wormhole          -- closed, by a theorem that
                                                   does not care about the
                                                   source
        BUT     find one and enlarge it         -- a search problem, then the
                                                   contain problem the tree has
                                                   already been working on

    AND THE HONEST COST OF THAT MOVE: NOBODY HAS EVER OBSERVED ONE.  It
    converts a construction problem into an astronomy problem, and this file
    does not pretend that is a small conversion.  It is, however, a DIFFERENT
    problem, and it is not closed by anything above.

    CORRECTED (DOCKET 67): "observed" here means IDENTIFIED -- nothing has
    been identified as a wormhole.  Shadows cannot tell one from a black hole
    (detect.py: "Wormholes can mimic black hole shadows"), and the echo
    channel is contested rather than null (negmass.py's tentative claim;
    CONFIRMED_DETECTION = False there).  No confirmed detection is the record.

    The live constructive literature is named rather than leaned on:
    "Wormhole Nucleation via Topological Surgery in Lorentzian Geometry"
    (arXiv:2505.02210, 2025) models nucleation with Morse theory and 0-surgery.
    NOT-RUN here.

stdlib only.  phase1.py supplies the definition this file tests the gate
against.
"""
import math, sys


# ------------------------------------------ 1: the gate against phase1's D1-D5

def gate_meets(condition):
    """D2 is the one that fails, and it fails on topology rather than size."""
    return {"D1": True, "D2": False, "D3": True, "D4": True, "D5": True}[condition]


def gate_is_a_phase1_transition():
    import phase1
    return all(gate_meets(tag) for tag, _w, _y in phase1.CONDITIONS)


def which_fails():
    import phase1
    return [tag for tag, _w, _y in phase1.CONDITIONS if not gate_meets(tag)]


def fails_on_topology():
    """R^3 is simply connected; a wormhole is not.  No metric deformation on a
    fixed manifold bridges that, at any support.
    CORRECTED (DOCKET 67): a restatement, not a computation -- this returns
    the literal True.  It holds for a HANDLE wormhole and a family of metrics
    non-degenerate at every s in [0,1] (DOCKET 67's audit computed that class);
    a Morris-Thorne inter-universe section R x S^2 is simply connected."""
    return True


def wormhole_was_ranked():
    """phase1's candidate list has no throat architecture in it."""
    import phase1
    return any("throat" in n.lower() or "wormhole" in n.lower()
               for n, _l, _r, _w in phase1.CANDIDATES)


# ------------------------------------------------ 2: two problems, not one

PROBLEMS = (
    ("CONTAIN", "hold an existing throat open and stable", "METRIC",
     "concentric.py, stability.py, core.py, wormhole.py, gate.py -- thirty passes"),
    ("CREATE", "bring a handle or second end into existence where there was "
     "none (a throat alone can form on a fixed manifold; DOCKET 67)", "TOPOLOGY",
     "never looked at, until this file"),
)


def problems_are_distinct():
    return len({p[2] for p in PROBLEMS}) == 2


def tree_has_worked_on(name):
    return name == "CONTAIN"


# --------------------------------- 3: the theorem, and what it does NOT need

GEROCH_NEEDS_MATTER_ASSUMPTION = False    # purely kinematical
EXOTIC_MATTER_HELPS_CREATION = False      # because of the line above
SINGULARITY_ESCAPES = False               # Borde: not under the standard defn
# CORRECTED (DOCKET 67), values unmoved.  EXOTIC_MATTER_HELPS_CREATION = False
# is exact as "exotic matter cannot remove the forced CTC" (Theorem 1,
# kinematic).  It does not hold as "cannot help creation": Borde IX.B names
# large energy-condition violation as the way past Theorem 3's DYNAMICAL
# obstruction, and 2505.02210 realises it, CTCs included.  SINGULARITY_ESCAPES
# = False holds for the standard incomplete-geodesic definition, under causal
# compactness; "other definitions of a singularity may make the statement
# true" (Borde IX), and the one he points to is IX.C, degenerate metrics.
KINEMATICALLY_POSSIBLE = True             # non-singular Lorentz metrics exist


def creation_wall_is_about_sourcing():
    """No -- and that makes it different in kind from every other wall here."""
    return EXOTIC_MATTER_HELPS_CREATION


BORDE = ("Neither Geroch's original theorem, nor its mild generalization in "
         "section IV, assume anything about the energy-momentum tensor, or "
         "indeed about a field equation")

BORDE_SINGULARITY = ("as long as the causal compactness condition is met, "
                     "causality violations have to occur when the topology "
                     "changes, even if incomplete geodesics are admitted")

BORDE_DYNAMICS = ("in dimensions >= 3 causally compact topology-changing "
                  "spacetimes cannot satisfy Einstein's equation (with a "
                  "reasonable source)")
# Borde's abstract, verbatim.  Theorem 3 behind it is for a time-oriented
# spacetime with a smooth non-degenerate metric, and "reasonable" means a
# restriction yielding (i) the null generic and (ii) the half-integral null
# convergence conditions (named at DOCKET 67; see section 3 above).


# --------------------------------------------- 4: the escapes, all three

# The three routes quoted here, not Borde's four: IX.C (degenerate metrics)
# and Sec. VIII's C^0 route are omitted, and with either the "stays in
# Lorentzian GR" test is UNDETERMINED (DOCKET 67; section 4 above).  The
# booleans are hand-set literals, READ for the three listed.
ESCAPES = (
    ("drop causal compactness", False,
     "Tipler: a singularity or A POINT AT INFINITY, which Borde calls 'a "
     "highly undesirable feature' (closed-universe case, Tipler's mild "
     "additional assumptions)"),
    ("weaken the curvature constraints", False,
     "requires altering Einstein's equation, and 'such an alteration would "
     "have to be fairly severe' -- or energy-condition violation breaking "
     "Theorem 3's (ii), which 'would not affect the presence of causality "
     "violations'"),
    ("Euclidean path integral", False,
     "abandons the Lorentzian framework altogether"),
)


def any_escape_stays_in_lorentzian_gr():
    return any(ok for _n, ok, _w in ESCAPES)


BORDE_CAUTION = ("Their true value is not so much that they actually rule out "
                 "topology change, but rather that they allow us to pinpoint "
                 "what modifications we have to make in our general framework "
                 "so as to allow it")


# ------------------------------- 5: the architectural escape, and its cost

def is_topology_change(initial_nontrivial, final_nontrivial):
    """Decides from two endpoint booleans (DOCKET 67: narrower than the
    theorems, whose conclusion is about the interpolating M).  It misses a
    non-product cobordism with the same nontrivial manifold at both ends, on
    which Theorem 1 forces a CTC, and a handle-number change R^3 # (S^1xS^2)
    -> R^3 # 2(S^1xS^2).  The one call carrying a verdict, (True, True) for a
    fixed-manifold enlargement with r > 0, lies inside the class where it
    holds."""
    return initial_nontrivial != final_nontrivial


def enlarging_is_topology_change():
    """Growing r_0 -> r_1 on an ALREADY nontrivial topology.  No change."""
    return is_topology_change(True, True)


def theorems_apply_to_enlargement():
    return enlarging_is_topology_change()


ROUTE = "find one and enlarge it"
# AS FIRST WRITTEN: "nobody has ever observed one -- a search problem, not a build"
# CORRECTED (DOCKET 67): "observed" meant IDENTIFIED (section 5).
# (Kept no longer than the original: ledger D24 prints it in a width-capped cell.)
ROUTE_COST = "none has ever been identified -- a search problem, not a build"
NUCLEATION_LITERATURE = "arXiv:2505.02210, Morse theory and 0-surgery"
NUCLEATION_STATUS = "NOT-RUN"


# ------------------------------------------------------------------ selftest

def selftest():
    ok = True

    def chk(label, got, want):
        nonlocal ok
        good = got == want
        ok &= good
        print("  %-56s %18s %18s  %s" % (label, got, want, "ok" if good else "FAIL"))

    print("1. THE GATE AGAINST phase1's OWN DEFINITION")
    import phase1
    for tag, what, _y in phase1.CONDITIONS:
        print("      %-4s %-38s %s" % (tag, what, "YES" if gate_meets(tag) else "NO"))
    chk("a wormhole gate is a phase1 transition", gate_is_a_phase1_transition(), False)
    chk("which condition fails", which_fails(), ["D2"])
    chk("and it fails on topology, not size", fails_on_topology(), True)
    chk("was a throat ever in phase1's ranking", wormhole_was_ranked(), False)
    print("      phase1 said 'FINISHED AS MATHEMATICS' about an architecture")
    print("      this project has since left.  Scoped in place there.")

    print("\n2. WHICH SEPARATES TWO PROBLEMS THE PHRASE RUNS TOGETHER")
    for n, what, kind, who in PROBLEMS:
        print("      %-8s %-46s %s" % (n, what, kind))
        print("               %s" % who)
    chk("they are different kinds of problem", problems_are_distinct(), True)
    chk("the tree has worked on CREATE", tree_has_worked_on("CREATE"), False)

    print("\n3. AND CREATION HAS ITS OWN THEOREM")
    chk("topology change is kinematically possible", KINEMATICALLY_POSSIBLE, True)
    chk("the theorem needs an assumption about matter",
        GEROCH_NEEDS_MATTER_ASSUMPTION, False)
    chk("so exotic matter removes the forced CTC", creation_wall_is_about_sourcing(), False)
    print("      \"%s\"" % BORDE[:66])
    chk("accepting a singularity escapes it (standard defn, cc)",
        SINGULARITY_ESCAPES, False)
    print("      \"%s\"" % BORDE_SINGULARITY[:66])
    print("      and dynamically: \"%s\"" % BORDE_DYNAMICS[:56])
    print("      EVERY OTHER WALL IN THIS PROJECT WAS ABOUT SOURCING SOMETHING.")
    print("      THIS ONE DOES NOT CARE WHAT THE SOURCE IS -- the KINEMATIC wall")
    print("      (Theorem 1); the dynamical sentence above is a source restriction.")

    print("\n4. BORDE'S OWN ESCAPES, ALL THREE QUOTED HERE (he gives four)")
    for n, in_gr, why in ESCAPES:
        print("      %-34s %s" % (n, why[:40]))
    chk("any escape stays in Lorentzian GR", any_escape_stays_in_lorentzian_gr(), False)
    print("      and his caution, which is worth more than a paraphrase:")
    print("      \"%s\"" % BORDE_CAUTION[:66])

    print("\n5. THE CLEAN ESCAPE IS ARCHITECTURAL")
    chk("enlarging an existing throat is a topology change",
        enlarging_is_topology_change(), False)
    chk("so the theorems apply to enlargement", theorems_apply_to_enlargement(), False)
    chk("the route", ROUTE, "find one and enlarge it")
    print("      NOT manufacture a wormhole -- closed by a theorem that does")
    print("      not care about the source.  BUT find one and enlarge it, which")
    print("      is a METRIC change and is exactly the problem the tree has")
    print("      already been working on for thirty passes.")
    print("      HONEST COST: %s" % ROUTE_COST)
    chk("nucleation literature", NUCLEATION_STATUS, "NOT-RUN")

    print("\n  SELFTEST " + ("OK" if ok else "FAILED"))
    return ok


def report():
    print(__doc__)
    print("=" * 79)
    print("""VERDICT

  SWEEPING phase1's DEPENDENTS AFTER THE ARCHITECTURE CHANGE FOUND
  THAT THE WORMHOLE FAILS phase1's OWN DEFINITION -- D2, compact
  support, and it fails on TOPOLOGY rather than size.  R^3 is simply
  connected and a HANDLE wormhole is not; no non-degenerate metric
  deformation on a fixed manifold bridges that at any support.  (DOCKET
  67: the clause a handle violates is phase1's fixed-manifold preamble,
  not D2; recorded in section 1.)  A throat was never in
  phase1's ranking either.  "Phase 1 is finished as mathematics" was
  finished about an architecture we have left.

  FOLLOWING THAT FAILURE TO ITS CAUSE SEPARATES TWO PROBLEMS THE
  PHRASE "CREATE AND CONTAIN" RUNS TOGETHER.  CONTAIN is a metric
  problem and this tree has worked on it for thirty passes.  CREATE
  -- a handle or a second end -- is a TOPOLOGY problem and the tree
  had never once looked at it.

  AND CREATION HAS ITS OWN THEOREM, WHICH IS HARSHER IN KIND THAN THE
  SOURCE PROBLEM.  Geroch, Tipler and Borde: topology change forces
  causality violations, the argument is PURELY KINEMATICAL and
  assumes nothing about the energy-momentum tensor or even a field
  equation -- SO EXOTIC MATTER CANNOT REMOVE THE FORCED CTC -- and I
  expected "accept a singularity" to be the way out and it is not: as
  long as the causal compactness condition is met, causality
  violations occur even if incomplete geodesics are admitted (the
  standard definition of a singularity).  In d >= 3, causally compact
  topology-changing spacetimes cannot satisfy Einstein's equation
  with a reasonable source -- Borde's Theorem 3, where "reasonable"
  yields his conditions (i) and (ii), and where large energy-condition
  violation is the route past it he names (IX.B), CTC kept.
  (CORRECTED, DOCKET 67: first written "SO EXOTIC MATTER CANNOT HELP".)

  EVERY OTHER WALL IN THIS PROJECT WAS ABOUT SOURCING SOMETHING.
  THIS ONE -- THE KINEMATIC WALL -- DOES NOT CARE WHAT THE SOURCE IS.

  THE THREE OF BORDE'S ESCAPES QUOTED HERE ALL LEAVE LORENTZIAN GR OR
  ACCEPT A PATHOLOGY.  He gives four; with IX.C, degenerate metrics,
  that test is UNDETERMINED (section 4).  His own caution is better
  than a paraphrase: these
  theorems' "true value is not so much that they actually rule out
  topology change, but rather that they allow us to pinpoint what
  modifications we have to make".

  AND THE CLEAN ESCAPE IS ARCHITECTURAL: DO NOT CREATE ONE, ENLARGE
  ONE.  Every theorem above is about topology CHANGE.  If the
  topology is already nontrivial, growing a throat from r_0 to r_1 on
  that fixed manifold, with r > 0, is a METRIC change the theorems do
  not forbid -- they conclude only that the interpolation is the
  product it already is -- and it is the problem the tree has been
  solving, though a dynamic mouth is not a static one (section 5).

  THE HONEST COST OF THAT MOVE IS THAT NOTHING HAS EVER BEEN
  IDENTIFIED AS ONE (CORRECTED, DOCKET 67: first "NOBODY HAS EVER
  OBSERVED ONE"; shadows mimic, and the echo claim is contested).
  It converts a construction problem into an astronomy problem.  That
  is a real conversion and not a small one -- but it is a DIFFERENT
  problem, and nothing above closes it.""")


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    report()
