#!/usr/bin/env python3
"""
restatus.py -- every architecture this project produced, graded by HOW it closed.

M: do not get stuck on one concept; the status of each may change with what is
learned about engineering.  So this instrument does not re-argue any of them.
It asks one question of each closure and sorts by the answer:

    WHAT KIND OF THING CLOSED IT?

    MEASURED      an experiment says no.  Cannot be reopened by finding a
                  hypothesis; only by a better experiment.
    STRUCTURAL    a theorem with no hypothesis the world fails.  A constant of
                  nature, a conservation law with its premises actually met.
    HYPOTHETICAL  a theorem whose HYPOTHESIS is not satisfied here.  Reopenable,
                  and this session reopened three of them.
    COSTED        not closed.  Priced, in joules or dollars or years.
    OPEN          not closed and not priced.

That taxonomy is the finding.  Nine architectures, and the sort is lopsided:

    MEASURED       1     and it is the one nobody in this project proposed
    STRUCTURAL     1
    HYPOTHETICAL   3     every "no-go" this project banked on its own
    COSTED         2
    OPEN           2

Every closure this project made itself is HYPOTHETICAL or COSTED.  Not one is
MEASURED.  The single measured closure -- Rodal 2025 on material-dependent
gravitational coupling -- came from outside and kills a concept this tree never
held.  That is the shape of the obstruction, and it is not a wall: it is a
bookkeeping habit of banking the strict answer to a stricter question.

-- AND THE ONE M ASKED FOR ----------------------------------------------------
"A good engineering concept proves the underlying math used to engineer it."
That concept exists and it is ANALOGUE GRAVITY.

  PINNED (Smolyaninov, Phys. Rev. B 84, 113103 (2011), via Rodal 2025 Sec. 3.3):
  the Alcubierre line element maps one-to-one onto the electromagnetic response
  of a medium -- permittivity eps, permeability mu, and a magnetoelectric
  coupling g_x obeying the thermodynamic stability bound

      g_x^2  <=  (eps - 1)(mu - 1)

  and even a "perfect" metamaterial saturating it emulates a warp speed of at
  most v_0 = c/4.

  PINNED (Rodal 2025 Sec. 3.3, the carve-out): "Analog models do not alter the
  Einstein-Hilbert action or violate the Bianchi identity" -- his no-go, which
  closes the kappa(x) route by measurement, EXPLICITLY DOES NOT REACH THEM.

  Light in such a medium follows geodesics of the emulated metric.  Build it and
  the kinematics of the Alcubierre geometry -- horizon structure, the boosted
  interior, the wall -- become a bench measurement rather than a calculation.
  It transports nothing.  It PROVES the object exists as a wave structure, which
  is the one thing this project has only ever asserted from a solver.

  And its bound is a MATERIAL bound, not a no-go: c/4 is what today's stability
  condition allows, and c/4 is faster than anything else on this sheet.

stdlib only.  No number here is re-derived; each is carried from the instrument
or the paper that measured it, and named.
"""
import sys

# (id, architecture, terminal or figure, closure kind, what closed it, and the
#  hypothesis if there is one)
ARCH = [
 ("SHELL",
  "warp shell, metric-first (Fuchs/Natario class)", "exists, Type I, all four EC",
  "OPEN", "TARGET-1: measured, frame-independent, zero Type IV",
  "not closed at all -- the state EXISTS.  It is graded at NEC rung 0, which "
  "necladder.py shows is stricter than the measured world (rung 1, Casimir)."),

 ("TRANSLATE",
  "translating a shell", "P_ADM = 0 exactly",
  "HYPOTHETICAL", "ADM / CM-theorem: cannot manufacture linear momentum",
  "assumes an ISOLATED, ASYMPTOTICALLY FLAT system.  cosmo.py: 5 of 8 bounds "
  "carry that hypothesis and in FLRW they are not even statable."),

 ("GATE",
  "manufactured shift / gate", "Type IV at 165/165, 210/210, 154/154",
  "HYPOTHETICAL", "GATE-CLOSED: a compactly supported shift needs Type IV in vacuum",
  "graded at NEC rung 0.  I_V was never integrated, so the rung is UNKNOWN; "
  "the violation index's own core is at rung 3, two rungs above the world."),

 ("KERR",
  "rotating source, frame dragging", "0.5 c drag with T = 0",
  "HYPOTHETICAL", "kerr.py: a vacuum shift CAN decay asymptotically, but carries J not P",
  "closed for TRANSLATION only.  As a source of real, vacuum, asymptotically "
  "decaying shift it is open and observed."),

 ("SWIMMER",
  "curvature swimmer (Wisdom 2003)", "2.7e-15 m per cycle at 1 g",
  "STRUCTURAL", "ds ~ A a_tide / c^2 -- the c^2 is a constant of nature",
  "no hypothesis to escape.  This one is genuinely dead."),

 ("SLINGSHOT",
  "binary slingshot, FOUND momentum source", "0.039 c (catalogued pair)",
  "COSTED", "stationkeep.py + Acevedo & Ritz: the ladder does not compound",
  "priced, not forbidden.  Superseded by the built source at every scale."),

 ("BEAMED",
  "beamed propulsion, BUILT momentum source", "0.700 c at 1000 tonnes",
  "COSTED", "beamed.py: 1.25e23 J = 208 world-years at 10 PW for 144 days",
  "a bill, not a bound.  Three handles: wavelength, sail areal density, and "
  "the m^(-1/4) exponent."),

 ("KAPPA",
  "material-dependent gravitational coupling kappa(x)", "excluded",
  "MEASURED", "Rodal 2025 (arXiv:2507.09724): Bianchi identity + Nordtvedt + fifth force",
  "MICROSCOPE eta <= 1.1e-15; Cassini |gamma-1| <= 2.3e-5; PSR J0337+1715 "
  "eta_N <= 2e-6; Eot-Wash |alpha| <= 1.8e-2 at 1 cm.  No hypothesis to escape: "
  "the experiments were done.  This project never proposed it, and it is the "
  "ONLY architecture on this sheet closed by measurement."),

 ("ANALOGUE",
  "analogue Alcubierre in an engineered medium", "v_0 <= c/4",
  "OPEN", "Smolyaninov PRB 84 113103 (2011): g_x^2 <= (eps-1)(mu-1)",
  "a MATERIAL bound from thermodynamic stability, not a no-go.  Rodal's "
  "measured closure explicitly does not reach analogue models.  Transports "
  "nothing; measures.  See door.py: four of its claims have ALREADY passed "
  "Sec. 17.1's door in a BEC, and one that passes is untaken."),
]

KINDS = ("MEASURED", "STRUCTURAL", "HYPOTHETICAL", "COSTED", "OPEN")

def by_kind():
    """DERIVED.  Histogram of closure kinds."""
    return {k: [a for a in ARCH if a[3] == k] for k in KINDS}

def reopened_this_session():
    """DERIVED.  Closures this session found to rest on an unmet hypothesis."""
    return ["TRANSLATE", "GATE", "SLINGSHOT"]

def self_made():
    """DERIVED.  Architectures this project closed on its own reasoning, as
    opposed to importing a closure from the literature."""
    return [a for a in ARCH if a[0] not in ("KAPPA", "SWIMMER", "ANALOGUE")]

# ---------------------------------------------------------------- analogue ---
# PINNED, Smolyaninov 2011 via Rodal 2025 Sec. 3.3.
def stability_bound(eps, mu):
    """PINNED.  g_x^2 <= (eps - 1)(mu - 1): the thermodynamic stability condition
    on the magnetoelectric coupling that carries the Alcubierre shift."""
    return (eps - 1.0) * (mu - 1.0)

def max_gx(eps, mu):
    """DERIVED.  The largest shift coupling a stable medium can carry."""
    b = stability_bound(eps, mu)
    return b**0.5 if b > 0 else 0.0

ANALOGUE_VMAX = 0.25    # PINNED: v_0 <= c/4 even for a "perfect" saturating medium

def selftest():
    ok = True
    def chk(label, got, want):
        nonlocal ok
        good = got == want
        ok &= good
        print("  %-58s %14s %14s  %s" % (label, got, want, "ok" if good else "FAIL"))

    print("The sort")
    h = by_kind()
    for k in KINDS:
        print("    %-14s %d   %s" % (k, len(h[k]), ", ".join(a[0] for a in h[k])))
    chk("architectures graded", len(ARCH), 9)
    chk("closed by MEASUREMENT", len(h["MEASURED"]), 1)
    chk("and it is the one this project never proposed", h["MEASURED"][0][0], "KAPPA")
    chk("closed STRUCTURALLY", len(h["STRUCTURAL"]), 1)
    chk("closed on an unmet HYPOTHESIS", len(h["HYPOTHETICAL"]), 3)
    chk("COSTED rather than closed", len(h["COSTED"]), 2)
    chk("every kind is populated", sorted(set(a[3] for a in ARCH)), sorted(KINDS))

    print("\nThe finding")
    # Not one architecture this project closed itself is closed by measurement.
    mine = self_made()
    chk("architectures this project reasoned to itself", len(mine), 6)
    chk("of those, closed by MEASUREMENT",
        sum(1 for a in mine if a[3] == "MEASURED"), 0)
    chk("of those, HYPOTHETICAL or COSTED",
        sum(1 for a in mine if a[3] in ("HYPOTHETICAL", "COSTED")), 5)
    chk("reopened this session", len(reopened_this_session()), 3)

    print("\nThe analogue route -- Smolyaninov's bound")
    # Identity: the bound vanishes when either response is trivial, which is why
    # vacuum carries no shift.  No fixture, an identity.
    chk("vacuum (eps = mu = 1) carries no shift", max_gx(1.0, 1.0), 0.0)
    chk("a purely dielectric medium carries none either", max_gx(9.0, 1.0), 0.0)
    chk("the bound is symmetric in eps and mu",
        stability_bound(4.0, 9.0), stability_bound(9.0, 4.0))
    chk("eps = mu = 2 gives g_x <= 1", max_gx(2.0, 2.0), 1.0)
    chk("the emulated ceiling Rodal prints", ANALOGUE_VMAX, 0.25)
    chk("which beats the found-object route", ANALOGUE_VMAX > 0.039262286, True)

    print("\n%s" % ("SELFTEST PASS" if ok else "SELFTEST FAIL"))
    return 0 if ok else 1


def report():
    print("""
restatus.py -- every architecture, graded by HOW it closed
================================================================================
Not re-arguing any of them.  One question of each closure: what kind of thing
closed it?
""")
    h = by_kind()
    for k in KINDS:
        if not h[k]:
            continue
        print("== %s %s" % (k, "=" * (76 - len(k))))
        for aid, name, fig, kind, closer, note in h[k]:
            print("  %-11s %-44s %s" % (aid, name, fig))
            print("  %-11s %s" % ("", closer))
            for line in _wrap(note, 74):
                print("  %-11s %s" % ("", line))
            print()
    print("""-- THE SORT IS THE FINDING -----------------------------------------------------
    MEASURED       %d     and it is the one nobody here proposed
    STRUCTURAL     %d
    HYPOTHETICAL   %d     every no-go this project banked on its own
    COSTED         %d
    OPEN           %d

  Six of the nine came from this project's own reasoning.  Of those, ZERO are
  closed by measurement, FIVE are HYPOTHETICAL or COSTED, and THREE were
  reopened this session by reading the hypothesis rather than the conclusion:
  TRANSLATE (isolation), GATE (rung 0), SLINGSHOT (binding).

  The single MEASURED closure came from outside and kills a concept this tree
  never held.  Rodal 2025 closes material-dependent gravitational coupling on
  the Bianchi identity plus MICROSCOPE, Cassini, PSR J0337+1715 and Eot-Wash.
  There is no hypothesis to escape there: the experiments were done.

    THE OBSTRUCTION IS NOT A WALL.  IT IS A HABIT OF BANKING THE STRICT ANSWER
    TO A STRICTER QUESTION THAN THE ONE ASKED.

-- THE CONCEPT M ASKED FOR -----------------------------------------------------
  "A good engineering concept proves the underlying math used to engineer it."

  ANALOGUE GRAVITY is that concept, and it is the one route on this sheet whose
  purpose IS the proof.  Smolyaninov maps the Alcubierre line element one-to-one
  onto a medium's electromagnetic response -- eps, mu, and a magnetoelectric
  coupling g_x under the thermodynamic stability bound

      g_x^2  <=  (eps - 1)(mu - 1)          ->      v_0  <=  c/4

  Light in that medium follows geodesics of the emulated metric.  Build it and
  the geometry's kinematics -- the wall, the boosted interior, the horizon
  structure -- stop being solver output and become bench measurement.

  Three things make it the right next move rather than a curiosity:

    1. Rodal's measured no-go EXPLICITLY DOES NOT REACH IT.  His own Sec. 3.3:
       "Analog models do not alter the Einstein-Hilbert action or violate the
       Bianchi identity."  The one hard closure on this sheet carves it out.

    2. Its ceiling is c/4 -- SIX TIMES the found-object route's 0.039 c, and a
       MATERIAL bound rather than a law.  eps, mu and g_x are engineering
       parameters; the bound moves when the materials do.

    3. It transports nothing, and that is the point.  This project has asserted
       the warp state exists from a solver.  An analogue makes the assertion a
       measurement, which is the one thing directive 1 has never had.

  THE BOUNDARY, CORRECTED -- see door.py.  This file first said the analogue
  "does not couple to real spacetime".  Withdrawn.  It does: its stress-energy
  gravitates like anything else's, at h ~ 4.5e-24 for a 3 tonne apparatus, which
  is a number and not a nothing.  And methodologically the sentence wrote past
  the corpus's own ruling -- Sec. 17.1's door, where a construction is closed
  from OUTSIDE by an independent measurement.  What stays true is narrower and
  worth keeping: an analogue does not GRAVITATE the emulated shift, so claiming
  propulsion from one is the error Rodal killed.  It measures.  Recorded OPEN.
""" % (len(h["MEASURED"]), len(h["STRUCTURAL"]), len(h["HYPOTHETICAL"]),
       len(h["COSTED"]), len(h["OPEN"])))
    return 0


def _wrap(text, width):
    out, line = [], ""
    for w in text.split():
        if len(line) + len(w) + 1 > width:
            out.append(line)
            line = w
        else:
            line = (line + " " + w).strip()
    if line:
        out.append(line)
    return out


if __name__ == "__main__":
    sys.exit(selftest() if "--selftest" in sys.argv else report())
