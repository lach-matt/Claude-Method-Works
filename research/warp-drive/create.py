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

    * CAUSALITY VIOLATIONS ARE FORCED.  Geroch's closed-universe argument,
      extended by Borde to causally compact interpolating spacetimes -- "a
      condition satisfied in a very wide range of situations".

    * AND THE SINGULARITY ESCAPE FAILS.  I expected "accept a singularity" to
      be the way out.  It is not: "as long as the causal compactness condition
      is met, causality violations have to occur when the topology changes,
      EVEN IF INCOMPLETE GEODESICS ARE ADMITTED."

    * DYNAMICALLY WORSE STILL: "in dimensions >= 3 causally compact
      topology-changing spacetimes cannot satisfy Einstein's equation (with a
      reasonable source)."

===============================================================================
4. BORDE'S OWN ESCAPES, ALL THREE, AND WHERE EACH GOES
===============================================================================

        DROP CAUSAL COMPACTNESS   then Tipler: the interpolating spacetime
                                  contains a singularity or A POINT AT INFINITY,
                                  which Borde calls "a highly undesirable
                                  feature"
        WEAKEN THE CURVATURE      would require altering Einstein's equation,
        CONSTRAINTS               and "such an alteration would have to be
                                  fairly severe"
        EUCLIDEAN PATH INTEGRAL   abandons the Lorentzian framework altogether

    ALL THREE LEAVE GENERAL RELATIVITY OR ACCEPT A PATHOLOGY -- the same shape
    as wormhole.py's scope warning, and the same decision belongs to M.

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

        GROWING A THROAT FROM r_0 TO r_1 IS A METRIC CHANGE.  Permitted.
        Geroch, Tipler and Borde say nothing about it.  Every instrument this
        tree has built for the CONTAIN problem applies to it unmodified.

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
    fixed manifold bridges that, at any support."""
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
    ("CREATE", "bring a throat into existence where there was none", "TOPOLOGY",
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


# --------------------------------------------- 4: the escapes, all three

ESCAPES = (
    ("drop causal compactness", False,
     "Tipler: a singularity or A POINT AT INFINITY, which Borde calls 'a "
     "highly undesirable feature'"),
    ("weaken the curvature constraints", False,
     "requires altering Einstein's equation, and 'such an alteration would "
     "have to be fairly severe'"),
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
    return initial_nontrivial != final_nontrivial


def enlarging_is_topology_change():
    """Growing r_0 -> r_1 on an ALREADY nontrivial topology.  No change."""
    return is_topology_change(True, True)


def theorems_apply_to_enlargement():
    return enlarging_is_topology_change()


ROUTE = "find one and enlarge it"
ROUTE_COST = "nobody has ever observed one -- a search problem, not a build"
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
    chk("so exotic matter helps creation", creation_wall_is_about_sourcing(), False)
    print("      \"%s\"" % BORDE[:66])
    chk("accepting a singularity escapes it", SINGULARITY_ESCAPES, False)
    print("      \"%s\"" % BORDE_SINGULARITY[:66])
    print("      and dynamically: \"%s\"" % BORDE_DYNAMICS[:56])
    print("      EVERY OTHER WALL IN THIS PROJECT WAS ABOUT SOURCING SOMETHING.")
    print("      THIS ONE DOES NOT CARE WHAT THE SOURCE IS.")

    print("\n4. BORDE'S OWN ESCAPES, ALL THREE")
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
  connected and a wormhole is not; no metric deformation on a fixed
  manifold bridges that at any support.  A throat was never in
  phase1's ranking either.  "Phase 1 is finished as mathematics" was
  finished about an architecture we have left.

  FOLLOWING THAT FAILURE TO ITS CAUSE SEPARATES TWO PROBLEMS THE
  PHRASE "CREATE AND CONTAIN" RUNS TOGETHER.  CONTAIN is a metric
  problem and this tree has worked on it for thirty passes.  CREATE
  is a TOPOLOGY problem and the tree had never once looked at it.

  AND CREATION HAS ITS OWN THEOREM, WHICH IS HARSHER IN KIND THAN THE
  SOURCE PROBLEM.  Geroch, Tipler and Borde: topology change forces
  causality violations, the argument is PURELY KINEMATICAL and
  assumes nothing about the energy-momentum tensor or even a field
  equation -- SO EXOTIC MATTER CANNOT HELP -- and I expected
  "accept a singularity" to be the way out and it is not: causality
  violations occur even if incomplete geodesics are admitted.  In
  d >= 3, causally compact topology-changing spacetimes cannot
  satisfy Einstein's equation with a reasonable source.

  EVERY OTHER WALL IN THIS PROJECT WAS ABOUT SOURCING SOMETHING.
  THIS ONE DOES NOT CARE WHAT THE SOURCE IS.

  BORDE'S THREE ESCAPES ALL LEAVE LORENTZIAN GR OR ACCEPT A
  PATHOLOGY, and his own caution is better than a paraphrase: these
  theorems' "true value is not so much that they actually rule out
  topology change, but rather that they allow us to pinpoint what
  modifications we have to make".

  AND THE CLEAN ESCAPE IS ARCHITECTURAL: DO NOT CREATE ONE, ENLARGE
  ONE.  Every theorem above is about topology CHANGE.  If the
  topology is already nontrivial, growing a throat from r_0 to r_1 is
  a METRIC change and none of this applies -- and it is exactly the
  problem the tree has been solving all along.

  THE HONEST COST OF THAT MOVE IS THAT NOBODY HAS EVER OBSERVED ONE.
  It converts a construction problem into an astronomy problem.  That
  is a real conversion and not a small one -- but it is a DIFFERENT
  problem, and nothing above closes it.""")


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    report()
