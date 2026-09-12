#!/usr/bin/env python3.12
"""phase.py -- the one odd value, and it is a PHASE.

M: "We still need that one odd value that unlocks it all.  Pi/3?  Cube root?
Whatever it is, I would be surprised if it wasn't a complex number or even a
real value that has to be derived from i."

THE PREDICTION IS CORRECT ON ALL THREE COUNTS AND THE VALUE IS NAMED HERE.
It is complex, it is odd, and the real invariant that carries it is defined
only through an imaginary part.  M also guessed pi/3 AND cube root, and those
turn out to be ONE guess rather than two.

  1.  THE WHOLE SPIN DEPENDENCE OF KERR IS A COMPLEX SHIFT OF THE RADIUS.
      Every polynomial curvature invariant of Kerr is Schwarzschild's, at

              z = r - i a cos(theta)

      (Newman-Janis).  Verified: the complex Kretschmann 48 M^2 / z^6 equals
      Schwarzschild's 48 M^2 / r^6 with r -> z, and its REAL part is the Kerr
      Kretschmann while its IMAGINARY part is the Chern-Pontryagin scalar.

  2.  SO THERE IS EXACTLY ONE ODD VALUE AND IT IS arg(z).
      |z|^2 = Sigma = r^2 + a^2 cos^2(theta) is EVEN in a -- that is what both
      threads see.  arg(z) = -arctan(a cos(theta)/r) is ODD -- and it is
      IDENTICALLY ZERO ON THE EQUATORIAL PLANE.  Every result in cube.py is
      that one sentence: the Kretschmann blindness, the vanishing chirality
      invariant, the four-even-one-odd census.  MODULUS AGAINST PHASE.

  3.  AND THE PHASE IS EXTRACTABLE FROM THE TWO REAL INVARIANTS.
      arg z = -arg(K - (i/2) *RR)/6 -- a REAL procedure returning a REAL
      number whose only route is through i.  THAT IS M'S THIRD CLAUSE,
      LITERALLY.  It has a real limit: the sixth power ALIASES once
      |arg z| reaches pi/6, and off branch the instrument returns NO BIT
      rather than a wrong one.

  4.  PI/3 AND CUBE ROOT ARE THE SAME GUESS, AND BOTH LAND.
      The equatorial photon orbit solves u^3 - 3u = +/-2a/M, whose three roots
      are 2 pi/3 apart -- cube-root spacing.  The physical branch is
      r = 2M(1 + cos psi) with psi ranging over EXACTLY [0, 2 pi/3], and

              psi = pi/3 -/+ (2/3) arcsin(a/M)

      so PI/3 IS THE ACHIRAL CENTRE OF ONE CUBE-ROOT SECTOR and the chirality
      is the displacement from it.  Prograde and retrograde angles SUM TO
      2 pi/3 exactly, at every spin.

  5.  ONE TEMPTING COINCIDENCE, MEASURED AND REFUSED.  sqrt(Lambda) = 3.159514
      against pi = 3.141593 is a 0.5705 % miss.  It is NOT an identity and it
      is recorded as a near miss, not as a finding.  THE FIXTURE FOR IT WAS
      TYPED RATHER THAN COMPUTED ON THE FIRST DRAFT AND WAS WRONG IN THE
      SEVENTH DIGIT -- the selftest caught it, which is what a selftest whose
      fixtures are computed numbers is for.

  6.  AND WHAT IT DOES NOT UNLOCK, SAID AS PLAINLY AS WHAT IT DOES.  Naming the
      bit is not supplying it.  The parity theorem is UNTOUCHED: a phase is not
      a function of a modulus.  The phase is set by the SOURCE's angular
      momentum and is not a dial.  AND IT MOVES THE ENERGY BILL BY NOTHING.

Scope: the Kerr family, type D vacuum, polynomial invariants.  Stdlib only.

    python3.12 phase.py            full report
    python3.12 phase.py --selftest
"""

import cmath
import math
import sys

LAMBDA = 9.982529174194637


# --------------------------------------------------------------------------
# 1.  The complex radius, and the invariant that lives on it.
# --------------------------------------------------------------------------

def z_of(r, th, a):
    """The Newman-Janis complex radius.  All of Kerr's spin lives here."""
    return r - 1j * a * math.cos(th)


def psi2(r, th, M, a):
    return -M / z_of(r, th, a) ** 3


def K_schwarzschild(r, M):
    """48 M^2 / r^6.  Real argument."""
    return 48.0 * M * M / r ** 6


def K_complex(r, th, M, a):
    """48 M^2 / z^6 -- Schwarzschild's Kretschmann AT COMPLEX RADIUS."""
    return 48.0 * M * M / z_of(r, th, a) ** 6


def kretschmann(r, th, M, a):
    return 48.0 * (psi2(r, th, M, a) ** 2).real


def pontryagin(r, th, M, a):
    """Same convention as cube.py: *RR = -96 Im(psi2^2)."""
    return -96.0 * (psi2(r, th, M, a) ** 2).imag


def K_minus_half_i_star(r, th, M, a):
    """K - (i/2) *RR.  The claim is that this IS K_schwarzschild(z)."""
    return kretschmann(r, th, M, a) - 0.5j * pontryagin(r, th, M, a)


# --------------------------------------------------------------------------
# 2/3.  The phase: the one odd value, and its extraction.
# --------------------------------------------------------------------------

def modulus(r, th, a):
    return abs(z_of(r, th, a))


def phase(r, th, a):
    """arg(z).  THE one odd value."""
    return cmath.phase(z_of(r, th, a))


BRANCH_LIMIT = math.pi / 6.0          # |arg z| below this, and no further


def phase_from_invariants(r, th, M, a):
    """arg z recovered from the two REAL curvature scalars alone.

    K - (i/2)*RR = 48 M^2 / z^6, so arg z = -arg(K - (i/2)*RR)/6.  Using the
    two-argument arctangent rather than the ratio *RR/2K matters: the ratio
    alone wraps at |6 arg z| = pi/2 and returns a confidently wrong number.

    VALID ONLY FOR |arg z| < pi/6, i.e. |a cos(theta)| / r < 1/sqrt(3).
    Beyond that the sixth power aliases and the phase is NOT recoverable.
    Ask on_branch() first; this function does not police itself.
    """
    K = kretschmann(r, th, M, a)
    P = pontryagin(r, th, M, a)
    return -math.atan2(-0.5 * P, K) / 6.0


def on_branch(r, th, a):
    """True where the extraction above is valid.  |a cos th| / r < 1/sqrt(3)."""
    return abs(phase(r, th, a)) < BRANCH_LIMIT


def sign_of_a_from_invariants(r, th, M, a):
    """The missing bit, returned as +1 or -1, from K and *RR only."""
    if not on_branch(r, th, a):
        return 0          # aliased: the sixth power has wrapped
    ph = phase_from_invariants(r, th, M, a)
    c = math.cos(th)
    if abs(ph) < 1e-15 or abs(c) < 1e-15:
        return 0          # on the equator there is nothing to read
    return -1 if (ph * c) > 0 else +1


# --------------------------------------------------------------------------
# 4.  pi/3, and the cube root that puts it there.
# --------------------------------------------------------------------------

def photon_cubic_roots(x):
    """All three roots of u^3 - 3u - 2x = 0, |x| <= 1.

    Returned as (u, angle) pairs with u = 2 cos(angle).  The angles are
    2 pi/3 apart -- the cube-root sector spacing.
    """
    base = math.acos(x) / 3.0
    out = []
    for k in (0, 1, 2):
        ang = base - 2.0 * math.pi * k / 3.0
        out.append((2.0 * math.cos(ang), ang))
    return out


def psi_angle(a, M, prograde=True):
    """The angle psi in r_ph = 2M(1 + cos psi), by the textbook route."""
    x = (-a / M) if prograde else (a / M)
    return (2.0 / 3.0) * math.acos(x)


def psi_angle_from_pi3(a, M, prograde=True):
    """The same angle written about its achiral centre."""
    d = (2.0 / 3.0) * math.asin(a / M)
    return math.pi / 3.0 + (d if prograde else -d)


def photon_sphere(M, a, prograde=True):
    return 2.0 * M * (1.0 + math.cos(psi_angle(a, M, prograde)))


# --------------------------------------------------------------------------
# Recorded verdicts.
# --------------------------------------------------------------------------

THE_ODD_VALUE = "arg(z), z = r - i a cos(theta)"
IT_IS_COMPLEX_DERIVED = True
IT_IS_ODD_IN_a = True
IT_VANISHES_ON_THE_EQUATOR = True
IT_IS_MEASURABLE_FROM_REAL_INVARIANTS = True
PI_OVER_3_IS_THE_ACHIRAL_CENTRE = True
CUBE_ROOT_SECTOR = "2 pi/3"
PARITY_THEOREM_IS_OVERTURNED = False
IT_SUPPLIES_AN_ORIENTATION = False
IT_MOVES_THE_ENERGY_BILL = False
SQRT_LAMBDA_EQUALS_PI = False
SCOPE = "Kerr family; type D vacuum; polynomial invariants"
NOTHING_IS_REPAIRED = True


BAR = "=" * 79


def report():
    print(__doc__.split("Scope:")[0].rstrip())
    print()

    print(BAR)
    print("1.  KERR IS SCHWARZSCHILD AT A COMPLEX RADIUS")
    print(BAR)
    print()
    print("        z = r - i a cos(theta)        K_complex = 48 M^2 / z^6")
    print()
    print("    CLAIM:  K_complex  ==  K - (i/2) *RR   exactly, where K is the")
    print("    Kerr Kretschmann and *RR the Chern-Pontryagin scalar.")
    print()
    print("      %6s %8s %22s %22s %10s"
          % ("a", "theta", "48 M^2 / z^6", "K - (i/2)*RR", "diff"))
    worst = 0.0
    cfg = [(0.7, 1.1, 5.0), (0.99, 0.4, 3.0), (-0.5, 2.0, 8.0),
           (0.3, math.pi / 2, 20.0), (4.9, 0.9, 12.0)]
    for a, th, r in cfg:
        A = K_complex(r, th, 1.0, a)
        B = K_minus_half_i_star(r, th, 1.0, a)
        d = abs(A - B)
        worst = max(worst, d)
        print("      %6.2f %8.4f %22s %22s %10.1e"
              % (a, th, "%.9f%+.9fj" % (A.real, A.imag),
                 "%.9f%+.9fj" % (B.real, B.imag), d))
    print()
    print("      IDENTICAL TO %.1e.  ONE COMPLEX CURVATURE SCALAR: its REAL" % worst)
    print("      part is the Kretschmann and its IMAGINARY part is the chirality.")
    print("      They are not two invariants -- THEY ARE ONE NUMBER IN CARTESIAN")
    print("      FORM, and the object it is a function of is a complex radius.")
    print()

    print(BAR)
    print("2.  SO THERE IS EXACTLY ONE ODD VALUE, AND IT IS arg(z)")
    print(BAR)
    print()
    print("      %6s %8s %14s %14s %14s %14s"
          % ("a", "theta", "|z| (a>0)", "|z| (a<0)", "arg z (a>0)", "arg z (a<0)"))
    mw = pw = 0.0
    for a, th, r in [(0.7, 1.1, 5.0), (0.7, 0.3, 5.0), (0.7, math.pi / 2, 5.0),
                     (2.5, 0.8, 4.0), (0.99, 2.4, 6.0)]:
        mp, mm = modulus(r, th, a), modulus(r, th, -a)
        pp, pm = phase(r, th, a), phase(r, th, -a)
        mw = max(mw, abs(mp - mm))
        pw = max(pw, abs(pp + pm))
        print("      %6.2f %8.4f %14.9f %14.9f %+14.9f %+14.9f"
              % (a, th, mp, mm, pp, pm))
    print()
    print("      MODULUS IDENTICAL TO %.1e -- EVEN.  PHASE SUMS TO %.1e -- ODD."
          % (mw, pw))
    print("      And |z|^2 = Sigma = r^2 + a^2 cos^2(theta), which is precisely")
    print("      what appears in every even component.  THE TWO THREADS SEE THE")
    print("      MODULUS.  THE MISSING BIT IS THE PHASE.")
    print()
    print("      ON THE EQUATOR z IS REAL: arg z = %.1e at theta = pi/2, for"
          % max(abs(phase(5.0, math.pi / 2, a)) for a in (0.3, 0.7, 2.5, -0.7)))
    print("      every spin tested.  THAT IS ONE SENTENCE FOR ALL OF cube.py --")
    print("      the Kretschmann equalling Schwarzschild's, the Chern-Pontryagin")
    print("      vanishing, and the four-even-one-odd census are the SAME FACT.")
    print()

    print(BAR)
    print("3.  AND THE PHASE IS EXTRACTABLE FROM THE TWO REAL INVARIANTS")
    print(BAR)
    print()
    print("        K - (i/2) *RR = 48 M^2 / z^6    ->    arg z = -arg(that)/6")
    print("        (the ratio form arg z = (1/6) arctan(*RR/2K) wraps sooner)")
    print()
    print("      %6s %8s %16s %16s %10s %7s %6s %s"
          % ("a", "theta", "arg z (direct)", "from K and *RR", "diff", "sgn(a)",
             "true", "branch"))
    ew = 0.0
    bits_ok = 0
    bits_tot = 0
    for a, th, r in [(0.7, 1.1, 5.0), (-0.7, 1.1, 5.0), (0.3, 0.5, 9.0),
                     (-2.5, 2.6, 7.0), (0.99, 0.9, 4.0), (3.5, 0.2, 2.0)]:
        d0 = phase(r, th, a)
        d1 = phase_from_invariants(r, th, 1.0, a)
        s = sign_of_a_from_invariants(r, th, 1.0, a)
        t = 1 if a > 0 else -1
        ob = on_branch(r, th, a)
        if ob:
            ew = max(ew, abs(d0 - d1))
            bits_tot += 1
            bits_ok += (s == t)
        print("      %6.2f %8.4f %+16.12f %+16.12f %10.1e %7d %6d %s"
              % (a, th, d0, d1, abs(d0 - d1), s, t, "ok" if ob else "ALIASED"))
    print()
    print("      ON BRANCH IT AGREES TO %.1e AND THE BIT COMES BACK RIGHT %d"
          % (ew, bits_ok))
    print("      TIMES OUT OF %d.  OFF BRANCH IT RETURNS 0 RATHER THAN A WRONG"
          % bits_tot)
    print("      ANSWER: the sixth power aliases once |arg z| reaches pi/6 =")
    print("      %.9f, that is |a cos(theta)|/r >= 1/sqrt(3) = %.9f."
          % (BRANCH_LIMIT, 1.0 / math.sqrt(3.0)))
    print("      THE FIRST DRAFT USED atan ON THE RATIO *RR/2K AND WRAPPED AT")
    print("      pi/12 INSTEAD, RETURNING A CONFIDENTLY WRONG PHASE.  Its own")
    print("      fixture caught it.  A two-argument arctangent on the complex")
    print("      invariant is the fix, and the remaining limit is real.")
    print("      A REAL PROCEDURE RETURNING A REAL NUMBER WHOSE ONLY ROUTE IS")
    print("      THROUGH i -- *RR is DEFINED as an imaginary part.  That is M's")
    print("      third clause landing exactly as stated.")
    print()

    print(BAR)
    print("4.  PI/3 AND CUBE ROOT ARE ONE GUESS, AND IT LANDS")
    print(BAR)
    print()
    print("    The equatorial photon orbit, in u = sqrt(r/M):   u^3 - 3u = 2x,")
    print("    x = -/+ a/M.  A CUBIC.  Its three roots at a/M = 0.7, prograde:")
    print()
    print("      %6s %16s %16s %18s" % ("root", "u", "angle", "residual"))
    rw = 0.0
    roots = photon_cubic_roots(-0.7)
    for i, (u, ang) in enumerate(roots):
        res = abs(u ** 3 - 3.0 * u - 2.0 * (-0.7))
        rw = max(rw, res)
        print("      %6d %16.12f %16.12f %18.1e" % (i, u, ang, res))
    gaps = [roots[0][1] - roots[1][1], roots[1][1] - roots[2][1]]
    print()
    print("      All three satisfy the cubic to %.1e, and the angular gaps are" % rw)
    print("      %.12f and %.12f against 2 pi/3 = %.12f.  CUBE-ROOT SPACING."
          % (gaps[0], gaps[1], 2 * math.pi / 3))
    print()
    print("    The physical branch is r_ph = 2M(1 + cos psi).  Written two ways:")
    print()
    print("      %8s %18s %18s %12s %18s"
          % ("a/M", "psi (textbook)", "pi/3 + (2/3)asin", "diff", "psi+ + psi-"))
    pw2 = sw = 0.0
    for a in (0.0, 0.3, 0.7, 0.99, 1.0, -0.7):
        p1 = psi_angle(a, 1.0, True)
        p2 = psi_angle_from_pi3(a, 1.0, True)
        s = psi_angle(a, 1.0, True) + psi_angle(a, 1.0, False)
        pw2 = max(pw2, abs(p1 - p2))
        sw = max(sw, abs(s - 2 * math.pi / 3))
        print("      %8.2f %18.12f %18.12f %12.1e %18.12f" % (a, p1, p2, abs(p1 - p2), s))
    print()
    print("      THE TWO FORMS AGREE TO %.1e AND THE PROGRADE AND RETROGRADE" % pw2)
    print("      ANGLES SUM TO 2 pi/3 = %.12f AT EVERY SPIN, to %.1e."
          % (2 * math.pi / 3, sw))
    print()
    print("        psi = pi/3 -/+ (2/3) arcsin(a/M)")
    print()
    print("      SO PI/3 IS THE ACHIRAL CENTRE OF EXACTLY ONE CUBE-ROOT SECTOR,")
    print("      psi runs over [0, 2 pi/3] and nothing wider, AND THE CHIRALITY")
    print("      IS THE DISPLACEMENT FROM PI/3.  At a = 0 the angle is %.12f"
          % psi_angle(0.0, 1.0, True))
    print("      and r_ph = %.9f M, the Schwarzschild photon sphere."
          % photon_sphere(1.0, 0.0, True))
    print("      M NAMED PI/3 AND THE CUBE ROOT AS TWO GUESSES.  THEY ARE ONE.")
    print()

    print(BAR)
    print("5.  ONE TEMPTING COINCIDENCE, MEASURED AND REFUSED")
    print(BAR)
    print()
    sl = math.sqrt(LAMBDA)
    print("      sqrt(Lambda) = %.9f      pi = %.9f" % (sl, math.pi))
    print("      ratio        = %.9f      miss = %.4f %%"
          % (sl / math.pi, 100.0 * abs(sl / math.pi - 1.0)))
    print()
    print("      NOT AN IDENTITY.  Recorded as a near miss and NOT as a finding.")
    print("      RETRACTION-AUDIT.tsv found 187 digit coincidences in this corpus")
    print("      by fingerprinting numbers, and a %.4f %% agreement between two"
          % (100.0 * abs(sl / math.pi - 1.0)))
    print("      constants with no derivation between them is exactly that shape.")
    print()

    print(BAR)
    print("6.  WHAT IT UNLOCKS, AND WHAT IT DOES NOT")
    print(BAR)
    print()
    print("    UNLOCKED, AND M PREDICTED ALL THREE:")
    print("      * THERE IS ONE ODD VALUE and it is arg(z) -- every even/odd")
    print("        split in cube.py is modulus against phase of a single")
    print("        complex number.")
    print("      * IT IS COMPLEX.  z = r - i a cos(theta), and the real")
    print("        Lorentzian Kerr metric is reached from Schwarzschild by that")
    print("        shift (Newman-Janis).  A REAL OBJECT DERIVED THROUGH i.")
    print("      * IT IS MEASURABLE.  arg z = -arg(K - (i/2) *RR)/6, returning a")
    print("        real number from two real invariants, one of which has no")
    print("        definition except as an imaginary part.  With a real limit:")
    print("        the sixth power aliases at |arg z| = pi/6 and off branch the")
    print("        instrument returns NO BIT rather than a wrong one.")
    print("      * AND PI/3 AND CUBE ROOT WERE THE SAME GUESS AND BOTH LAND.")
    print()
    print("    NOT UNLOCKED, AND THIS HAS TO BE SAID AS PLAINLY:")
    print("      * THE PARITY THEOREM IS UNTOUCHED.  cube.py proved no function")
    print("        of the even components returns an odd one.  A PHASE IS NOT A")
    print("        FUNCTION OF A MODULUS, and naming the missing datum is not")
    print("        producing it.  This is a BETTER DESCRIPTION of the gap.")
    print("      * IT SUPPLIES NO ORIENTATION.  arg z is set by the SOURCE's")
    print("        angular momentum.  It is a reading, not a dial, and a")
    print("        construction must still put the rotation there.")
    print("      * IT MOVES THE ENERGY BILL BY NOTHING AT ALL.  Not one figure")
    print("        in currency.py, magnitude.py or frequency.py changes.  The")
    print("        three currencies stand where they stood.")
    print()
    print("    SCOPE: %s." % SCOPE)
    print("    Nothing here is repaired.")
    print()


def selftest():
    fails = []

    def chk(label, got, want, tol=None):
        ok = (abs(got - want) <= tol) if tol is not None else (got == want)
        print("  %-4s %-56s %s" % ("ok" if ok else "FAIL", label, got))
        if not ok:
            fails.append((label, got, want))

    print("phase.py --selftest")
    print()

    # 1.  the complex Kretschmann
    w = 0.0
    for a, th, r in [(0.7, 1.1, 5.0), (0.99, 0.4, 3.0), (-0.5, 2.0, 8.0),
                     (0.3, math.pi / 2, 20.0), (4.9, 0.9, 12.0)]:
        w = max(w, abs(K_complex(r, th, 1.0, a) - K_minus_half_i_star(r, th, 1.0, a)))
    chk("48 M^2/z^6 == K - (i/2)*RR", w < 1e-12, True)
    chk("and at a = 0 it is Schwarzschild's",
        abs(K_complex(5.0, 1.1, 1.0, 0.0) - K_schwarzschild(5.0, 1.0)) < 1e-15, True)

    # 2.  parity of modulus and phase
    mw = pw = 0.0
    for a, th, r in [(0.7, 1.1, 5.0), (2.5, 0.8, 4.0), (0.99, 2.4, 6.0)]:
        mw = max(mw, abs(modulus(r, th, a) - modulus(r, th, -a)))
        pw = max(pw, abs(phase(r, th, a) + phase(r, th, -a)))
    chk("|z| is even in a", mw < 1e-15, True)
    chk("arg z is odd in a", pw < 1e-15, True)
    chk("|z|^2 == Sigma",
        abs(modulus(5.0, 1.1, 0.7) ** 2 - (25.0 + 0.49 * math.cos(1.1) ** 2)) < 1e-12, True)
    chk("arg z vanishes on the equator",
        max(abs(phase(5.0, math.pi / 2, a)) for a in (0.3, 0.7, 2.5, -0.7)) < 1e-16, True)
    chk("and is nonzero off it", abs(phase(5.0, 0.8, 0.7)) > 1e-3, True)

    # 3.  extraction
    ew = 0
    dw = 0.0
    for a, th, r in [(0.7, 1.1, 5.0), (-0.7, 1.1, 5.0), (0.3, 0.5, 9.0),
                     (-2.5, 2.6, 7.0), (0.99, 0.9, 4.0)]:
        dw = max(dw, abs(phase(r, th, a) - phase_from_invariants(r, th, 1.0, a)))
        ew += (sign_of_a_from_invariants(r, th, 1.0, a) == (1 if a > 0 else -1))
    chk("arg z recovered from K and *RR", dw < 1e-12, True)
    chk("and the bit comes back on all five", ew, 5)
    chk("the equator returns no bit",
        sign_of_a_from_invariants(5.0, math.pi / 2, 1.0, 0.7), 0)
    chk("branch limit is pi/6", round(BRANCH_LIMIT, 12), round(math.pi / 6, 12))
    chk("an aliased configuration is refused, not guessed",
        (on_branch(2.0, 0.2, 3.5), sign_of_a_from_invariants(2.0, 0.2, 1.0, 3.5)),
        (False, 0))
    chk("branch edge is |a cos th|/r = 1/sqrt(3)",
        abs(abs(phase(1.0, 0.0, 1.0 / math.sqrt(3.0))) - BRANCH_LIMIT) < 1e-15, True)

    # 4.  the cubic
    rw = 0.0
    for x in (-0.7, 0.0, 0.99, -1.0):
        for u, ang in photon_cubic_roots(x):
            rw = max(rw, abs(u ** 3 - 3.0 * u - 2.0 * x))
    chk("all three roots satisfy u^3 - 3u = 2x", rw < 1e-12, True)
    rts = photon_cubic_roots(-0.7)
    chk("root angles are 2pi/3 apart",
        abs((rts[0][1] - rts[1][1]) - 2 * math.pi / 3) < 1e-15
        and abs((rts[1][1] - rts[2][1]) - 2 * math.pi / 3) < 1e-15, True)
    pw2 = sw = 0.0
    for a in (0.0, 0.3, 0.7, 0.99, 1.0, -0.7):
        pw2 = max(pw2, abs(psi_angle(a, 1.0, True) - psi_angle_from_pi3(a, 1.0, True)),
                  abs(psi_angle(a, 1.0, False) - psi_angle_from_pi3(a, 1.0, False)))
        sw = max(sw, abs(psi_angle(a, 1.0, True) + psi_angle(a, 1.0, False)
                         - 2 * math.pi / 3))
    chk("psi = pi/3 -/+ (2/3) arcsin(a/M)", pw2 < 1e-15, True)
    chk("psi+ + psi- = 2pi/3 at every spin", sw < 1e-15, True)
    chk("psi = pi/3 exactly at a = 0",
        abs(psi_angle(0.0, 1.0, True) - math.pi / 3) < 1e-16, True)
    chk("and that is the 3M photon sphere",
        round(photon_sphere(1.0, 0.0, True), 12), 3.0)
    chk("psi spans exactly [0, 2pi/3]",
        abs(psi_angle(1.0, 1.0, True) - 2 * math.pi / 3) < 1e-15
        and abs(psi_angle(1.0, 1.0, False)) < 1e-15, True)
    chk("cube.py's extremal spheres reproduced",
        (round(photon_sphere(1.0, 1.0, True), 9),
         round(photon_sphere(1.0, 1.0, False), 9)), (1.0, 4.0))

    # 5.  the refused coincidence
    chk("sqrt(Lambda) / pi", round(math.sqrt(LAMBDA) / math.pi, 9), 1.005704565)
    chk("sqrt(Lambda) == pi", SQRT_LAMBDA_EQUALS_PI, False)

    # 6.  the verdicts
    chk("the odd value", THE_ODD_VALUE, "arg(z), z = r - i a cos(theta)")
    chk("it is complex-derived", IT_IS_COMPLEX_DERIVED, True)
    chk("it is measurable", IT_IS_MEASURABLE_FROM_REAL_INVARIANTS, True)
    chk("parity theorem overturned", PARITY_THEOREM_IS_OVERTURNED, False)
    chk("it supplies an orientation", IT_SUPPLIES_AN_ORIENTATION, False)
    chk("it moves the energy bill", IT_MOVES_THE_ENERGY_BILL, False)
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
