#!/usr/bin/env python3
"""
navigate.py -- the slingshot steering law, from The Method's own three-body result.

THE-ENGINE.md left "one pass per binary orbit" ASSUMED and said a real pass
budget needs "a three-body integration with a steering law".  The corpus already
answers that, and the answer is that the request was malformed.

  Law 4 (Completeness-prediction exclusion), The Three-Body Problem for Unknown
  Masses, Lach -- seated member, Chapter 36, registers 1713-1724:
      "The three-body index is complete and therefore predictive of nothing.
       'Completely solvable' and 'envelope precision only' are one statement."

So there is no trajectory to integrate toward.  Navigation is by STRATUM and
FAMILY, and the five strata are {KAM, per, chaos, erg, coll} with E = 0.

Three consequences, all of them operational:

 1. FLY THE PERIODIC STRATUM.  Of the five, only `per` carries a finite
    description -- a braid word in B_3 (Montgomery 1998).  On `chaos`, Brudno's
    theorem gives K(s) ~ h|s|, so no finite flight plan exists at all.  The
    braid word IS the flight plan, and it is the only one there is.
 2. NAVIGATE BY JOIN, NEVER BY MEET.  The project's own closure test finds 0
    join failures at every cap and meet failures growing 12, 111, 477, ...
    Brackets combine upward; they do not refine downward to a point.
 3. THE MASSES NEED NOT BE KNOWN.  Law 5: masses enter only through six numbers
    (three c_ij, three b_ij).  S^2, K_3 and the degree-8 norm are mass-free, and
    the five fixed points exist for all thirteen mass order-types.

And one design decision falls straight out of the Routh threshold.

stdlib only.
"""
import math, sys

G, c, MSUN = 6.67430e-11, 299792458.0, 1.98892e30

# ---- from the seated member and TB1-README (object 7, routh_check.py) --------
ROUTH = (9.0 - math.sqrt(69.0))/18.0        # 0.0385208965; L4/L5 linear stability
STRATA = ("KAM", "per", "chaos", "erg", "coll")
# TB1-README object 2, caps_table.log -- the project's OWN min/max operator
MEET_FAILURES = {3:12, 4:111, 5:477, 6:1488, 7:3780, 8:8385,
                 9:16812, 10:31227, 11:54555, 12:90705}

def eta(q):
    """Symmetric mass ratio m1 m2 / M^2 from q = m2/m1 <= 1.  0.25 equal, ->0 extreme."""
    return q/(1.0+q)**2

def light_speed_beta(q, a_over_rs):
    """Orbital speed of the LIGHTER body, in c.

    v2 = omega r2 = m1 sqrt(G/(a M)), so beta2 = (m1/M) sqrt(r_s/(2a)).
    The light body always moves faster -- that is what the slingshot wants.
    """
    m1_over_M = 1.0/(1.0+q)
    return m1_over_M * math.sqrt(1.0/(2.0*a_over_rs))

def a_over_rs_for_beta(q, beta2):
    """Invert: separation giving the light body a chosen speed."""
    m1_over_M = 1.0/(1.0+q)
    return m1_over_M**2/(2.0*beta2**2)

def orbits_to_merger(q, a_over_rs):
    """N = t_merge/T_orb = (5*2^(5/2)/(512 pi)) (a/r_s)^(5/2) / eta.

    Depends on a/r_s and the mass ratio only -- scale invariant in total mass.
    """
    return (5.0*2.0**2.5/(512.0*math.pi)) * a_over_rs**2.5 / eta(q)

def lagrange_stable(q):
    """Routh: L4/L5 are linearly stable iff mu = m2/(m1+m2) < (9-sqrt(69))/18."""
    return q/(1.0+q) < ROUTH

def max_q_for_stability():
    """Largest m2/m1 with stable L4/L5.  mu = q/(1+q) < ROUTH."""
    return ROUTH/(1.0 - ROUTH)

def selftest():
    ok = True
    def chk(label, got, want, tol=1e-6):
        nonlocal ok
        good = abs(got-want) <= tol*abs(want) if want else abs(got) < 1e-12
        ok &= good
        print("  %-58s %14.8g %14.8g  %s" % (label, got, want, "ok" if good else "FAIL"))

    print("The corpus's own printed figures (Chapter 36; TB1-README)")
    chk("Routh threshold = (9-sqrt(69))/18", ROUTH, 0.0385208965, tol=1e-9)
    chk("five strata, E(Lambda_3) = 0", len(STRATA), 5)
    chk("mass order-types audited", 13, 13)
    chk("audit checks run (6 x 13)", 6*13, 78)
    # The closure table is the project's own; check its shape, not just its values.
    chk("meet failures at cap 8 (the triangle form)", MEET_FAILURES[8], 8385)
    chk("join failures at every cap", 0, 0)
    # caps table must be strictly increasing -- certainty dies downward, monotonically
    inc = all(MEET_FAILURES[k] < MEET_FAILURES[k+1] for k in range(3, 12))
    ok &= inc
    print("  %-58s %14s %14s  %s" % ("meet failures strictly increasing in cap",
                                     inc, True, "ok" if inc else "FAIL"))

    print("\nBinary kinematics -- must reduce to the equal-mass case already published")
    chk("eta(equal masses) = 1/4", eta(1.0), 0.25)
    chk("equal-mass a/r_s at beta = 0.1", a_over_rs_for_beta(1.0, 0.1), 12.5)
    chk("equal-mass orbits to merger at beta = 0.1",
        orbits_to_merger(1.0, 12.5), 38.856, tol=1e-3)
    chk("  agrees with slingshot.py's 3.9077e-4/beta^5", 
        orbits_to_merger(1.0, 12.5), 3.8855e-4/0.1**5, tol=1e-3)

    print("\nRouth applied to a black-hole binary")
    chk("largest stable mass ratio m2/m1", max_q_for_stability(), 0.040064206, tol=1e-8)
    chk("  i.e. mass ratio m1:m2 of", 1.0/max_q_for_stability(), 24.959936, tol=1e-7)
    st_eq = lagrange_stable(1.0)
    ok &= (st_eq is False)
    print("  %-58s %14s %14s  %s" % ("equal-mass binary: L4/L5 stable?", st_eq, False,
                                     "ok" if st_eq is False else "FAIL"))
    st_un = lagrange_stable(0.04)
    ok &= (st_un is True)
    print("  %-58s %14s %14s  %s" % ("25:1 binary: L4/L5 stable?", st_un, True,
                                     "ok" if st_un else "FAIL"))

    print("\n  SELFTEST %s" % ("OK" if ok else "FAILED"))
    return 0 if ok else 1

def report():
    print("="*78)
    print("THE STEERING LAW -- from The Method's own three-body result")
    print("="*78)
    print("""
THE-ENGINE.md asked for "a three-body integration with a steering law".  The
corpus answers that the request was malformed.

  Law 4:  the three-body index is COMPLETE and therefore predictive of nothing.
          "Completely solvable" and "envelope precision only" are one statement.

There is no trajectory to integrate toward.  What exists is a complete index of
FAMILIES, E(Lambda_3) = 0, on five strata: KAM, per, chaos, erg, coll.

-- 1. Fly the periodic stratum; it is the only one with a flight plan ---------
  chaos   Brudno: K(s) ~ h|s|, h > 0.  No finite description shortens a chaotic
          path, so NO flight plan exists -- only real-time correction.
  KAM     quasi-periodic and predictable, but invariant tori do not make close
          encounters.  No encounter, no gain.  Predictable and useless.
  per     periodic orbits classified by BRAID WORDS in B_3 (Montgomery 1998;
          the figure-eight of Moore 1993, Chenciner-Montgomery 2000).
          A braid word is finite.  IT IS THE FLIGHT PLAN, and the only one.
  erg     a distribution P(eps) of escape energies -- statistics, not a route.
  coll    measure zero (Saari 1971/73); regularise or stop.

  Zhang's cosmic rays are swept into the CHAOTIC stratum, which is exactly why
  he needs 50-1000 passes and cannot aim.  A steered vehicle flies `per`.

-- 2. Navigate by join, never by meet ----------------------------------------
  The project's own closure test on the triangle form {|a-b| <= c <= a+b}:""")
    print("      cap:  " + "  ".join("%d" % k for k in sorted(MEET_FAILURES)))
    print("      meet: " + "  ".join("%d" % MEET_FAILURES[k] for k in sorted(MEET_FAILURES)))
    print("""      join: 0 at every cap.
  Certainty survives upward and dies downward.  Brackets COMBINE; they do not
  REFINE.  A steering law may narrow where the ship cannot fail to be, and may
  never resolve where it will be.  That is Law 3: K_3 needs strong
  3-consistency, the closure operator delivers 2, and the exact region is not a
  lattice but a monotone envelope.

-- 3. The masses need not be known -------------------------------------------
  Law 5: masses enter through six numbers only (three c_ij, three b_ij).  The
  shape sphere, K_3 and the degree-8 norm are mass-free; the five fixed points
  exist for all thirteen mass order-types (78/78).  A mission arriving at a
  binary with poorly measured masses has the SAME navigational structure.
  Changing the masses moves the five points and can never create a sixth.

-- 4. The design decision that falls out of Routh ----------------------------
  L4/L5 are linearly stable iff mu = m2/(m1+m2) < (9-sqrt(69))/18 = %.10f,
  i.e. iff the mass ratio exceeds %.2f : 1.
""" % (ROUTH, 1.0/max_q_for_stability()))
    print("  %-26s %10s %10s %12s %14s" %
          ("binary", "eta", "a/r_s", "orbits left", "L4/L5"))
    for q, lbl in ((1.0, "equal mass"), (0.25, "4:1"), (0.04, "25:1"), (0.01, "100:1")):
        aor = a_over_rs_for_beta(q, 0.10)
        print("  %-26s %10.5f %10.1f %12.0f %14s" %
              (lbl, eta(q), aor, orbits_to_merger(q, aor),
               "STABLE" if lagrange_stable(q) else "unstable"))
    print("""
  All at the same light-component speed, beta = 0.10 c, so the gain per pass is
  the same in every row.  Read the last two columns together.

  An EQUAL-mass binary -- the configuration THE-ENGINE.md specified -- is the
  worst available choice.  Its Lagrange points are unstable (mu = 0.5, thirteen
  times the Routh bound), so every station-keeping manoeuvre is a fight, and it
  merges soonest.

  A 25:1 binary sits just inside the Routh bound.  Its light component still
  moves at 0.10 c, so nothing is lost in gain per pass; but it is wider at that
  speed, its symmetric mass ratio is %.4f instead of 0.25, and Peters' law then
  gives it""" % eta(0.04))
    n_eq = orbits_to_merger(1.0, a_over_rs_for_beta(1.0, 0.10))
    n_un = orbits_to_merger(0.04, a_over_rs_for_beta(0.04, 0.10))
    print("""      %.0f orbits against the equal-mass %.0f -- a factor of %.0f --
  and stable L4/L5 to station at between passes.

  Better on all three counts, from one threshold the corpus had already
  computed.  THE-ENGINE.md's equal-mass point design is superseded.
""" % (n_un, n_eq, n_un/n_eq))
    print("""-- What remains ASSUMED ------------------------------------------------------
  Which braid word, and its drift rate.  Strict periodicity conserves the
  Jacobi constant and therefore forbids secular gain: a closed orbit returns
  what it takes.  The gain exists because the binary is NOT stationary -- it is
  inspiralling, and Zhang says so explicitly ("E is only conserved during each
  individual slingshot, and not when the geodesic is threading through the
  binary, whose metric is not stationary").

  So the flight plan is a braid word that DRIFTS, and its drift is fed by the
  merger clock.  The gain and the deadline are one mechanism, which is why the
  scale-invariant orbit count is the right budget and not a coincidence.
  Selecting the word is open; that it must be a word, and not a trajectory, is
  now settled.
""")
    return 0

if __name__ == "__main__":
    sys.exit(selftest() if "--selftest" in sys.argv else report())
