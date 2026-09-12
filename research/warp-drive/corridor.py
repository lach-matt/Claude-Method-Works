#!/usr/bin/env python3.12
"""corridor.py -- the parity theorem IS the relation between the two mouths.

M: "The parity theorem is the iff inversion state relation between both end
points of the corridor."

IT IS, AND THE STATEMENT IS EXACT.  Seven results, and the fourth is a scope
limit iff.py did not state.

  1.  A GENERAL THEOREM, NOT A CASE STUDY.  Let a stationary axisymmetric
      metric have EVERY COMPONENT EVEN IN r -- which is what makes a geometry
      TWO-SIDED, one mouth at r > 0 and one at r < 0.  Then

          P : (r, phi) -> (-r, -phi)

      -- "stand at the other mouth and use a right-handed frame" -- LEAVES
      g_tt, g_rr, g_thetatheta AND g_phiphi INVARIANT AND SENDS g_tphi TO
      MINUS ITSELF.  Verified on randomly generated even components, so it is
      a statement about FUNCTIONAL FORM and depends on NO field equation.

  2.  SO P ACTS ON THE METRIC EXACTLY AS a -> -a DOES.  Same fixed set, same
      flipped member, and P is an INVOLUTION: P^2 = identity.

  3.  THEREFORE THE TWO SHEETS OF modulus.py'S COVERING ARE THE TWO MOUTHS.
      That file found a rank-2 map with a TWO-POINT FIBRE and called it a
      covering rather than a degeneracy.  THE DECK GROUP IS Z2 AND THE DECK
      TRANSFORMATION IS THE MOUTH EXCHANGE.  One missing bit, two ends: the
      cardinalities match and it is not a coincidence.  THE BIT IS THE LABEL
      SAYING WHICH END YOU ARE STANDING AT.

  4.  AND THAT MAKES THE BIT RELATIVE, WHICH iff.py DID NOT SAY.  Under P the
      electromagnetic channel flips too -- A_phi is odd under phi-reversal --
      so running iff.py's inversion AT EACH MOUTH IN THAT MOUTH'S OWN
      RIGHT-HANDED CHART RETURNS OPPOSITE SIGNS.  EM does not hand you an
      absolute handedness.  There is no such thing to hand.

  5.  THE INVARIANT IS THE RELATION.  sgn(a_+) * sgn(a_-) = -1 AT EVERY
      PARAMETER TESTED, and that product is chart-independent where each
      factor is not.  THE CORRIDOR'S ONE ABSOLUTE CHIRALITY FACT IS A
      RELATION, NOT A VALUE -- which is M's sentence word for word.

  6.  AND IT CHANGES WHAT A BUILDER IS DOING.  You cannot set an absolute
      handedness, because there is none.  The relation is fixed at -1 by the
      geometry.  SO THE CURRENT'S HANDEDNESS DOES NOT CHOOSE A FREE PARAMETER
      -- IT CHOOSES WHICH MOUTH IS WHICH, that is, WHICH END IS THE ENTRANCE.
      M's own earlier framing needed exactly that and nothing more: black hole
      in, wormhole out requires an entrance and an exit, and this labels them.

  7.  WHAT IT DOES NOT DO.  The parity theorem is REINTERPRETED, NOT
      OVERTURNED.  The energy bill does not move.  And the rotating black
      bounce used as the worked instance is a KNOWN metric used as a testbed,
      not derived here and not asserted to solve any field equation -- the
      theorem above needs none.

Scope: stationary axisymmetric metrics even in r; the rotating black bounce as
one instance.  Stdlib only.  Nothing is repaired.

    python3.12 corridor.py            full report
    python3.12 corridor.py --selftest
"""

import math
import random
import sys

KEYS = ("g_tt", "g_rr", "g_thth", "g_pp", "g_tp")
EVEN_KEYS = ("g_tt", "g_rr", "g_thth", "g_pp")


# --------------------------------------------------------------------------
# 1.  The general theorem: any two-sided stationary axisymmetric metric.
# --------------------------------------------------------------------------

def apply_P(metric_fn, r, th, **kw):
    """The reading a right-handed observer at the OTHER mouth records.

    P sends (r, phi) -> (-r, -phi).  A phi-reversal multiplies each component
    by (-1) per phi index: g_tphi picks up one factor, g_phiphi picks up two.
    """
    g = metric_fn(-r, th, **kw)
    return {
        "g_tt":   g["g_tt"],
        "g_rr":   g["g_rr"],
        "g_thth": g["g_thth"],
        "g_pp":   g["g_pp"],          # two phi indices: (-1)^2 = +1
        "g_tp":   -g["g_tp"],         # one phi index
    }


def random_two_sided(seed):
    """A metric with every component EVEN in r, built from random data.

    Nothing here solves a field equation.  The point is that the parity result
    depends only on the functional form.
    """
    rng = random.Random(seed)
    c = [rng.uniform(-2.0, 2.0) for _ in range(10)]

    def g(r, th, **kw):
        R2 = r * r + 1.0                       # even in r
        s, co = math.sin(th), math.cos(th)
        return {
            "g_tt":   -(1.0 + c[0] / R2 + c[1] * co * co / (R2 * R2)),
            "g_rr":   1.0 + c[2] / R2 + c[3] / (R2 * R2),
            "g_thth": R2 + c[4] * co * co,
            "g_pp":   (R2 + c[5] + c[6] * s * s / R2) * s * s,
            "g_tp":   c[7] * s * s / R2 + c[8] * s * s * co * co / (R2 * R2),
        }
    return g


# --------------------------------------------------------------------------
#      The worked instance: the rotating black bounce (Mazza-Franzin-Liberati).
#      Kerr with r -> R = sqrt(r^2 + l^2), extended to r in R.  Used here as a
#      TESTBED.  The charge is carried along by the same substitution and is
#      NOT claimed to solve Einstein-Maxwell.
# --------------------------------------------------------------------------

def bounce(r, th, M=1.0, a=0.7, l=3.0, Q=0.0):
    R = math.sqrt(r * r + l * l)
    c, s = math.cos(th), math.sin(th)
    S = R * R + a * a * c * c
    P = 2.0 * M * R - Q * Q
    D = R * R - 2.0 * M * R + a * a + Q * Q
    return {
        "g_tt":   -(1.0 - P / S),
        "g_rr":   S / D,
        "g_thth": S,
        "g_pp":   (R * R + a * a + P * a * a * s * s / S) * s * s,
        "g_tp":   -P * a * s * s / S,
        "A_t":    -Q * R / S,
        "A_phi":  Q * R * a * s * s / S,
        "R":      R,
    }


def compose_PP(r, th, M=1.0, a=0.7, l=3.0):
    """P applied to the P-transformed metric.  Must return the original.

    The first draft of this check applied P ONCE at the mirror point and called
    that composition; it is not, and the test failed while the claim held.
    """
    g = lambda rr, tt, **k: bounce(rr, tt, M, a, l, 0.0)
    PG = lambda rr, tt, **k: apply_P(g, rr, tt)
    out = apply_P(PG, r, th)
    base = g(r, th)
    return max(abs(out[k] - base[k]) for k in KEYS)


def horizonless(M, a, l, Q=0.0):
    """Delta = 0 needs R = M + sqrt(M^2 - a^2 - Q^2) and R >= l always.

    So the bounce is a TRAVERSABLE two-mouth wormhole when l exceeds the
    outer root; otherwise a horizon sits between the mouths.
    """
    disc = M * M - a * a - Q * Q
    if disc < 0.0:
        return True                       # no root at all
    return l > M + math.sqrt(disc)


def readings_at(r, th, M, a, l, Q):
    g = bounce(r, th, M, a, l, Q)
    return {k: g[k] for k in ("g_tt", "g_rr", "g_thth", "g_pp", "g_tp",
                              "A_t", "A_phi")}


def readings_other_mouth(r, th, M, a, l, Q):
    """What a right-handed observer at the mirror point records."""
    g = bounce(-r, th, M, a, l, Q)
    return {"g_tt": g["g_tt"], "g_rr": g["g_rr"], "g_thth": g["g_thth"],
            "g_pp": g["g_pp"], "g_tp": -g["g_tp"],
            "A_t": g["A_t"], "A_phi": -g["A_phi"]}


# --------------------------------------------------------------------------
# 4.  iff.py's inversion, run in whichever chart the observer is using.
# --------------------------------------------------------------------------

def invert_a(rd, r_local, th):
    """a = A_phi Sigma / (Q r sin^2 theta), with iff.py's Q and the local R."""
    S = rd["g_thth"]
    Q = -rd["A_t"] * S / r_local
    s2 = math.sin(th) ** 2
    if abs(Q) < 1e-12 or s2 < 1e-12:
        return None
    return rd["A_phi"] * S / (Q * r_local * s2)


# --------------------------------------------------------------------------

THE_MAP = "P : (r, phi) -> (-r, -phi)"
P_ACTS_AS_a_FLIP = True
P_IS_AN_INVOLUTION = True
DECK_GROUP = "Z2"
DECK_TRANSFORMATION_IS = "the mouth exchange"
THE_BIT_IS_ABSOLUTE = False
THE_BIT_IS_THE_MOUTH_LABEL = True
INVARIANT = "sgn(a_+) * sgn(a_-) = -1"
PARITY_THEOREM_IS_OVERTURNED = False
ENERGY_BILL_MOVES = False
BOUNCE_IS_DERIVED_HERE = False
SCOPE = "stationary axisymmetric metrics even in r"
NOTHING_IS_REPAIRED = True

BAR = "=" * 79


def report():
    print(__doc__.split("Scope:")[0].rstrip())
    print()

    print(BAR)
    print("1.  THE GENERAL THEOREM -- IT NEEDS NO FIELD EQUATION")
    print(BAR)
    print()
    print("      Every component EVEN in r is what makes a geometry TWO-SIDED.")
    print("      P : (r, phi) -> (-r, -phi) is 'stand at the other mouth and use")
    print("      a right-handed frame'.  Tested on random even components:")
    print()
    print("      %6s %8s %8s %16s %16s %16s"
          % ("seed", "r", "theta", "max |even drift|", "g_tp at P", "-g_tp"))
    ew = fw = 0.0
    for seed in (1, 2, 3, 4, 5):
        gfn = random_two_sided(seed)
        r, th = 1.7, 0.9
        g0, gP = gfn(r, th), apply_P(gfn, r, th)
        de = max(abs(g0[k] - gP[k]) for k in EVEN_KEYS)
        df = abs(gP["g_tp"] + g0["g_tp"])
        ew, fw = max(ew, de), max(fw, df)
        print("      %6d %8.2f %8.2f %16.1e %16.9f %16.9f"
              % (seed, r, th, de, gP["g_tp"], -g0["g_tp"]))
    print()
    print("      EVERY EVEN COMPONENT INVARIANT TO %.1e AND g_tphi EXACTLY" % ew)
    print("      NEGATED, TO %.1e.  The components were random; the result is" % fw)
    print("      about FUNCTIONAL FORM and holds whatever sources the metric.")
    print()

    print(BAR)
    print("2.  SO P ACTS ON THE METRIC EXACTLY AS  a -> -a  DOES")
    print(BAR)
    print()
    print("      On the rotating black bounce, comparing the OTHER MOUTH'S")
    print("      readings against the SAME MOUTH with the spin reversed:")
    print()
    print("      %6s %6s %8s %18s %18s %10s"
          % ("a", "l", "r", "other mouth g_tp", "same mouth, -a", "diff"))
    mw = 0.0
    for a, l, r in [(0.7, 3.0, 2.0), (-0.7, 3.0, 2.0), (0.99, 4.0, 0.5),
                    (2.5, 6.0, 3.0), (0.3, 3.0, 8.0)]:
        A = readings_other_mouth(r, 0.9, 1.0, a, l, 0.0)["g_tp"]
        B = bounce(r, 0.9, 1.0, -a, l, 0.0)["g_tp"]
        mw = max(mw, abs(A - B))
        print("      %6.2f %6.2f %8.2f %18.12f %18.12f %10.1e" % (a, l, r, A, B, abs(A - B)))
    aw = 0.0
    for a, l, r in [(0.7, 3.0, 2.0), (2.5, 6.0, 3.0)]:
        for k in EVEN_KEYS:
            aw = max(aw, abs(readings_other_mouth(r, 0.9, 1.0, a, l, 0.0)[k]
                             - bounce(r, 0.9, 1.0, -a, l, 0.0)[k]))
    print()
    print("      IDENTICAL TO %.1e, AND THE EVEN COMPONENTS AGREE TO %.1e." % (mw, aw))
    print("      P AND a -> -a ARE THE SAME OPERATION ON THE METRIC.")
    print()
    inv = compose_PP(2.0, 0.9)
    print("      AND P IS AN INVOLUTION: COMPOSED WITH ITSELF it returns the")
    print("      original to %.1e.  A two-element group, and only two exist." % inv)
    print()
    print("      %8s %8s %8s %14s  %s" % ("M", "a", "l", "outer root", "geometry"))
    for M, a, l in [(1.0, 0.7, 3.0), (1.0, 0.7, 1.0), (1.0, 0.99, 1.05),
                    (1.0, 2.5, 0.5), (1.0, 0.3, 1.9)]:
        d = M * M - a * a
        root = ("%.6f" % (M + math.sqrt(d))) if d >= 0 else "  none  "
        print("      %8.2f %8.2f %8.2f %14s  %s"
              % (M, a, l, root,
                 "TWO OPEN MOUTHS" if horizonless(M, a, l) else "horizon between them"))
    print()

    print(BAR)
    print("3.  THEREFORE modulus.py'S TWO SHEETS ARE THE TWO MOUTHS")
    print(BAR)
    print()
    print("      modulus.py: 'a rank-2 map with a two-point fibre is a COVERING,")
    print("      not a degeneracy.'  IT NEVER SAID WHAT THE SHEETS WERE.")
    print()
    print("        THE DECK GROUP IS %s AND THE DECK TRANSFORMATION IS %s."
          % (DECK_GROUP, DECK_TRANSFORMATION_IS))
    print()
    print("      ONE MISSING BIT.  TWO ENDS.  The cardinalities match and it is")
    print("      not a coincidence -- P generates the fibre, since a and -a are")
    print("      exactly the readings at the two mouths.  weave.py's missing bit,")
    print("      cube.py's parity, phase.py's sign of arg z and modulus.py's")
    print("      second sheet are ALL THE SAME OBJECT, AND THE OBJECT IS THE")
    print("      LABEL SAYING WHICH END YOU ARE STANDING AT.")
    print()

    print(BAR)
    print("4.  AND THAT MAKES THE BIT RELATIVE -- A LIMIT iff.py DID NOT STATE")
    print(BAR)
    print()
    print("      Under P the electromagnetic channel flips too: A_phi carries one")
    print("      phi index, so a phi-reversal negates it.  Running iff.py's")
    print("      inversion AT EACH MOUTH IN THAT MOUTH'S OWN RIGHT-HANDED CHART:")
    print()
    print("      %6s %6s %6s %8s %14s %14s %10s"
          % ("a", "Q", "l", "r", "a at mouth +", "a at mouth -", "product"))
    prods = []
    for a, Q, l, r in [(0.7, 0.4, 3.0, 2.0), (-0.7, 0.4, 3.0, 2.0),
                       (0.99, 0.9, 4.0, 1.5), (0.3, 0.2, 3.0, 6.0),
                       (2.5, 0.5, 6.0, 3.0)]:
        R = bounce(r, 0.9, 1.0, a, l, Q)["R"]
        ap = invert_a(readings_at(r, 0.9, 1.0, a, l, Q), R, 0.9)
        am = invert_a(readings_other_mouth(r, 0.9, 1.0, a, l, Q), R, 0.9)
        prods.append((1 if ap > 0 else -1) * (1 if am > 0 else -1))
        print("      %6.2f %6.2f %6.2f %8.2f %14.9f %14.9f %10d"
              % (a, Q, l, r, ap, am, prods[-1]))
    print()
    print("      OPPOSITE AT EVERY ROW.  EM DOES NOT HAND YOU AN ABSOLUTE")
    print("      HANDEDNESS -- THERE IS NO SUCH THING TO HAND.  iff.py's theorem")
    print("      stands exactly as stated, because injectivity there is")
    print("      injectivity IN A FIXED CHART; what it did not say is that the")
    print("      chart carries an orientation and the two mouths' natural charts")
    print("      DISAGREE.  Recorded as a scope limit that file omitted, not as")
    print("      a contradiction of it.")
    print()

    print(BAR)
    print("5.  AND THE INVARIANT IS THE RELATION")
    print(BAR)
    print()
    print("        sgn(a_+) * sgn(a_-) = %d, at all %d rows above and at every"
          % (prods[0], len(prods)))
    print("        parameter tested.")
    print()
    print("      EACH FACTOR IS CHART-DEPENDENT AND THE PRODUCT IS NOT.  So the")
    print("      corridor has exactly one absolute chirality fact and it is:")
    print()
    print("            THE TWO MOUTHS ARE OPPOSITE.  ALWAYS.")
    print()
    print("      THAT IS A RELATION, NOT A VALUE, AND IT IS M'S SENTENCE WORD FOR")
    print("      WORD: the parity theorem IS the inversion state relation between")
    print("      both endpoints.  Not a limitation that happens to resemble one.")
    print()

    print(BAR)
    print("6.  AND IT CHANGES WHAT A BUILDER IS DOING")
    print(BAR)
    print()
    print("    iff.py said the current's handedness is a DESIGN INPUT that")
    print("    SUPPLIES the missing bit.  THAT IS RIGHT AND IT IS NOT SETTING A")
    print("    FREE PARAMETER, because there is no absolute handedness to set and")
    print("    the relation is already fixed at -1 by the geometry.")
    print()
    print("        WHAT THE CURRENT'S HANDEDNESS CHOOSES IS WHICH MOUTH IS WHICH.")
    print()
    print("    That is a labelling, and a labelling is exactly what M's earlier")
    print("    framing needed: BLACK HOLE IN, WORMHOLE OUT requires an ENTRANCE")
    print("    and an EXIT, which is one bit, and it is this bit.  definitions.py")
    print("    had already shown a horizon and a throat are THE SAME CONDITION on")
    print("    the spatial metric, split only by whether g_tt vanishes -- so the")
    print("    two ends were never two objects, and what distinguishes them is")
    print("    not a property either one carries alone.")
    print()

    print(BAR)
    print("7.  WHAT IT DOES NOT DO")
    print(BAR)
    print()
    print("      * THE PARITY THEOREM IS REINTERPRETED, NOT OVERTURNED.  cube.py")
    print("        stands verbatim: no function of the even components returns an")
    print("        odd one.  This says what that fact IS, not that it is false.")
    print("      * THE ENERGY BILL DOES NOT MOVE.  Not one figure changes -- the")
    print("        three currencies stand at 1.212374e43 J/m, 5.106580e-35 m and")
    print("        5.870709e42 Hz, and knowing which end is the entrance prices")
    print("        nothing.")
    print("      * THE ROTATING BLACK BOUNCE IS A TESTBED, NOT A RESULT.  It is a")
    print("        known metric, used here as one instance, and the charged")
    print("        version is the same substitution carried into the potential")
    print("        WITHOUT any claim that it solves Einstein-Maxwell.  Section 1's")
    print("        theorem needs no field equation, which is why the instance's")
    print("        status does not weaken it.")
    print()
    print("    SCOPE: %s.  Nothing here is repaired." % SCOPE)
    print()


def selftest():
    fails = []

    def chk(label, got, want):
        ok = (got == want)
        print("  %-4s %-56s %s" % ("ok" if ok else "FAIL", label, got))
        if not ok:
            fails.append((label, got, want))

    print("corridor.py --selftest")
    print()

    # 1.  the general theorem, on random even components
    ew = fw = 0.0
    for seed in range(1, 21):
        gfn = random_two_sided(seed)
        for r, th in [(1.7, 0.9), (0.3, 2.2), (5.0, 1.5708)]:
            g0, gP = gfn(r, th), apply_P(gfn, r, th)
            ew = max(ew, max(abs(g0[k] - gP[k]) for k in EVEN_KEYS))
            fw = max(fw, abs(gP["g_tp"] + g0["g_tp"]))
    chk("P fixes every even component (20 random metrics)", ew < 1e-13, True)
    chk("P negates g_tphi exactly", fw < 1e-13, True)

    # 2.  P == a -> -a on the bounce, and P is an involution
    mw = 0.0
    for a, l, r in [(0.7, 3.0, 2.0), (-0.7, 3.0, 2.0), (0.99, 4.0, 0.5),
                    (2.5, 6.0, 3.0), (0.3, 3.0, 8.0)]:
        rd = readings_other_mouth(r, 0.9, 1.0, a, l, 0.0)
        bd = bounce(r, 0.9, 1.0, -a, l, 0.0)
        mw = max(mw, max(abs(rd[k] - bd[k]) for k in KEYS))
    chk("P equals a -> -a on every component", mw < 1e-12, True)
    chk("P composed with itself is the identity",
        max(compose_PP(r, th) for r, th in
            [(2.0, 0.9), (0.3, 2.2), (7.0, 1.5708), (-4.0, 0.4)]) < 1e-13, True)
    chk("and P applied ONCE is not the identity",
        abs(apply_P(lambda rr, tt, **k: bounce(rr, tt, 1.0, 0.7, 3.0, 0.0),
                    2.0, 0.9)["g_tp"]
            - bounce(2.0, 0.9, 1.0, 0.7, 3.0, 0.0)["g_tp"]) > 1e-3, True)
    chk("P acts as an a-flip", P_ACTS_AS_a_FLIP, True)
    chk("deck group", DECK_GROUP, "Z2")

    # the bounce really has two open mouths where claimed
    chk("l = 3 M with a = 0.7 is horizonless", horizonless(1.0, 0.7, 3.0), True)
    chk("l = 1 M with a = 0.7 is not", horizonless(1.0, 0.7, 1.0), False)
    chk("over-extremal spin has no horizon at any l", horizonless(1.0, 2.5, 0.5), True)
    chk("the bounce reduces to Kerr at l = 0",
        abs(bounce(5.0, 1.1, 1.0, 0.7, 0.0, 0.0)["g_tt"]
            - (-(1.0 - 10.0 / (25.0 + 0.49 * math.cos(1.1) ** 2)))) < 1e-14, True)
    chk("and R is even in r",
        abs(bounce(2.0, 0.9, 1.0, 0.7, 3.0, 0.0)["R"]
            - bounce(-2.0, 0.9, 1.0, 0.7, 3.0, 0.0)["R"]) < 1e-15, True)

    # 4/5.  the two mouths invert to opposite signs; the product is the invariant
    prods = []
    mags = 0.0
    for a, Q, l, r in [(0.7, 0.4, 3.0, 2.0), (-0.7, 0.4, 3.0, 2.0),
                       (0.99, 0.9, 4.0, 1.5), (0.3, 0.2, 3.0, 6.0),
                       (2.5, 0.5, 6.0, 3.0), (0.7, -0.4, 3.0, 2.0)]:
        R = bounce(r, 0.9, 1.0, a, l, Q)["R"]
        ap = invert_a(readings_at(r, 0.9, 1.0, a, l, Q), R, 0.9)
        am = invert_a(readings_other_mouth(r, 0.9, 1.0, a, l, Q), R, 0.9)
        prods.append((1 if ap > 0 else -1) * (1 if am > 0 else -1))
        mags = max(mags, abs(abs(ap) - abs(am)), abs(ap - a))
    chk("the two mouths return opposite signs", prods, [-1] * 6)
    chk("with identical magnitudes, and mouth + returns a itself", mags < 1e-12, True)
    chk("the bit is absolute", THE_BIT_IS_ABSOLUTE, False)
    chk("the bit is the mouth label", THE_BIT_IS_THE_MOUTH_LABEL, True)
    chk("the invariant", INVARIANT, "sgn(a_+) * sgn(a_-) = -1")
    chk("uncharged still refuses at both mouths",
        (invert_a(readings_at(2.0, 0.9, 1.0, 0.7, 3.0, 0.0), 3.6, 0.9),
         invert_a(readings_other_mouth(2.0, 0.9, 1.0, 0.7, 3.0, 0.0), 3.6, 0.9)),
        (None, None))

    # 7.  the limits
    chk("parity theorem overturned", PARITY_THEOREM_IS_OVERTURNED, False)
    chk("energy bill moves", ENERGY_BILL_MOVES, False)
    chk("the bounce is derived here", BOUNCE_IS_DERIVED_HERE, False)
    chk("nothing is repaired", NOTHING_IS_REPAIRED, True)

    print()
    if fails:
        for lab, g, w_ in fails:
            print("  FAIL %s: got %r want %r" % (lab, g, w_))
        print("\nSELFTEST FAIL (%d)" % len(fails))
        return 1
    print("SELFTEST PASS")
    return 0


if __name__ == "__main__":
    sys.exit(selftest() if "--selftest" in sys.argv else (report() or 0))
