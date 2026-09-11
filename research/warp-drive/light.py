#!/usr/bin/env python3
"""
light.py -- light gravitates, it drags frames, and it is not a cheaper currency.

M: "we don't need mass or density energy, we can use light energy, supporting my
binary information currency idea.  Please read and research the Ronald Mallett
papers on ring lasers."

Read.  The papers are real and so is the physics they rest on: LIGHT IS A
GRAVITATIONAL SOURCE, and a circulating beam really does drag inertial frames.
Nothing in this tree ever denied that and this file does not either.

What fails is three separable things, and they fail for three different
reasons -- one of magnitude, one of KIND, and one specific to Mallett's
solution that is settled in the literature.

THE ONE THAT MATTERS IS THE MIDDLE ONE, because it is not a magnitude at all:
NULL DUST SATISFIES THE NULL ENERGY CONDITION IDENTICALLY.  Light is the most
NEC-respecting source there is, and rho < 0 is the one thing the transition
needs.

===============================================================================
1. THE REAL PHYSICS, AND IT IS REAL
===============================================================================

    Tolman, Ehrenfest & Podolsky (Phys. Rev. 37, 602, 1931)  "thin pencils of
        light" gravitate.
    Scully (Phys. Rev. D 19, 3582, 1979)                      gravitational
        coupling between laser beams.
    Mallett (Phys. Lett. A 269, 214, 2000)                    WEAK GRAVITATIONAL
        FIELD OF THE ELECTROMAGNETIC RADIATION IN A RING LASER -- frame dragging
        from circulating light, in linearised GR.  Ring-laser precession
        Omega = 8 sqrt(2) G lambda_L / (a c^3).
    Mallett (Found. Phys. 33, 1307, 2003)                     the exact
        cylindrically symmetric solution, with the CTC claim.
    Strohaber (arXiv:1112.3414)                               independent
        linearised calculation for OPTICAL VORTICES, confirming frame dragging
        and comparing directly with Mallett's ring laser.

    SO THE 2000 PAPER IS NOT THE CONTESTED ONE.  Frame dragging by circulating
    light is ordinary gravitomagnetism and it is right.  The 2003 CTC paper is
    the contested one, and section 4 is about that.

===============================================================================
2. BUT LIGHT IS NOT A CHEAPER SOURCE, BECAUSE THE COUPLING IS THE SAME
===============================================================================

The Einstein equation couples to T_munu with the constant 8 pi G / c^4, and
light's energy enters it exactly as any other energy does.  rates.py already
proved the general form: every denomination reaches mass-energy through a
monomial in G, c, hbar and k, and A CONSTANT OF NATURE IS NOT A DISCOUNT.
Light is another denomination.

Priced against this project's own exchange rate, 1.34895e26 kg per metre
contracted -- which is 1.21237e43 JOULES per metre:

    a 1 kW ring laser, to contract ONE METRE
        1.2124e40 s  =  3.8418e32 years  =  2.78e22 AGES OF THE UNIVERSE

    a 1 kW ring laser running for a full year
        buys 2.6030e-33 m  =  161 PLANCK LENGTHS

    to contract one metre in one second
        1.2124e43 W  =  3.17e16 SOLAR LUMINOSITIES

    THE FORM OF THE ENERGY WAS NEVER THE PROBLEM.  supply.py said it first:
    E = mc^2 is already inside G/c^4.  Switching from mass to light changes
    the engineering and not the bill.

===============================================================================
3. AND LIGHT CANNOT DO THE ONE THING THE TRANSITION NEEDS -- BY A THEOREM
===============================================================================

This is the part that is not about magnitude, and it is the decisive one.

For null dust -- the stress tensor of a light beam -- T_munu = eps eta_mu
eta_nu with eta null and eps >= 0.  Contract with ANY null vector k:

        T_munu k^mu k^nu  =  eps (eta . k)^2  >=  0,

a non-negative number times a SQUARE.  Measured below over 200,000 random
(eta, k, eps) triples: the minimum found is +1.75e-11, and it cannot be
otherwise.

        LIGHT SATISFIES THE NULL ENERGY CONDITION IDENTICALLY.  IT IS THE MOST
        NEC-RESPECTING SOURCE IN PHYSICS.

expand.py's INFORMATION row refuses for want of rho < 0 at magnitude.  Light is
not a weak answer to that; IT IS THE WRONG KIND OF ANSWER, in the exact sense
compress.py used for door two: the quantity the refusal names does not appear.
You cannot approach a negative energy density from a source whose energy
condition is saturated by construction.

===============================================================================
4. AND MALLETT'S CTC SOLUTION IS REFUTED, ON THREE INDEPENDENT GROUNDS
===============================================================================

Olum & Everett, "Can a circulating light beam produce a time machine?"
(gr-qc/0410078; Found. Phys. Lett. 18, 379, 2005), and Olum, "Geodesics in the
static Mallett spacetime" (arXiv:1003.3828).

  (a) THE MAGNITUDE, AND ITS SHAPE IS THE POINT.  CTCs need
      ln(rho/alpha) > 1/lambda with lambda = pi G P rho_0 / (c^5 r).  For a 1 kW
      laser, rho_0 = 0.5 m, r = 1 mm they get lambda ~ 1e-46; recomputed here,
      4.33e-47, order agreement.  So CTCs begin at

            rho > 10^(1.0e46) rho_0.

      THE DEPENDENCE IS LOGARITHMIC, SO 1/lambda SITS IN THE EXPONENT.  Power
      cannot buy past it -- their words, the numbers "could be changed by many
      orders of magnitude without altering the conclusions".

  (b) THE SPACETIME IS PATHOLOGICAL WITHOUT THE LIGHT.  R^t_rtr = 1/(8 rho^2)
      and the scalar R_abcd R^abcd = 3/(4 alpha rho^3) both diverge on the axis,
      and it is not a coordinate artifact.  Worse: THE DIVERGENCE HAS NO
      DEPENDENCE ON lambda, so it persists as the light intensity goes to ZERO.

            IT IS NOT THE SOLUTION YOU GET BY PUTTING A CYLINDER OF LIGHT INTO
            MINKOWSKI SPACE.  Unlike van Stockum/Tipler, which does.

  (c) THE APPARATUS IS NOT DOING THE WORK.  rho = const, dphi/dt = 1/alpha are
      NULL GEODESICS of the background: "the light does not require any external
      apparatus to keep it in circulation; the photonic crystals discussed in
      [Mallett] would not be necessary."  THE LIGHT IS ORBITING THE SINGULARITY.
      The ring laser is not the source of the effect.

  AND THE FOLLOW-UP IS WORSE.  In the static (eps = 0) spacetime, EVERY timelike
  geodesic originates and terminates at the singularity; a particle at rest at
  proper distance R is destroyed after proper time ~1.3 R; and "from any point
  the singularity fills the entire sky except for an infinitesimally thin
  strip".  Olum: any attempt to build this "would have a very unfortunate effect
  on nearby objects".

  AND THE ESCAPE FROM THE NO-GO THEOREMS DOES NOT SURVIVE FINITENESS.  Tipler
  and Hawking are evaded only because the Cauchy horizon of an INFINITE cylinder
  is not compactly generated.  Olum & Everett: "These theorems would, however,
  rule out the creation of CTC's in ANY FINITE-SIZE APPROXIMATION to this
  spacetime."  Every buildable version is closed by the theorems the infinite
  one dodges.

  IN FAIRNESS TO MALLETT, HE CONCEDED THE SINGULARITY.  Olum records that in
  Mallett's 2006 book he says he introduced it to confine the light rays and
  simplify the calculation.  The dispute is about what the solution shows, not
  about anyone's honesty.

===============================================================================
5. WHAT CIRCULATING LIGHT ACTUALLY BUYS, MEASURED BY SOMEONE ELSE
===============================================================================

Strohaber's optical-vortex calculation is the constructive counterpart and it
gives the honest engineering number.  For a spin precession of ONE HERTZ on a
test particle -- not a transition, just a frame drag you could measure:

        required            ~1e45 W/cm^2
        Hercules, the most intense laser system         ~2e22 W/cm^2
        SHORT BY 22.70 ORDERS

    And a ring laser is worse: its size is capped by the OPTICAL DAMAGE
    THRESHOLD of its own material, ~1e12 W/cm^2, which is 33.00 orders short.
    Optical vortices beat ring lasers only because they need no optics to
    circulate -- their radius is limited by the wavelength instead.

===============================================================================
6. ROUTED THROUGH THE INDEX, IT LANDS ON TWO ROWS AND FAILS ON BOTH
===============================================================================

    "USE LIGHT AS THE SOURCE"      an INFORMATION/magnitude claim.  Lands on the
                                   row that refuses the main question -- and the
                                   refusal names rho < 0, which null dust cannot
                                   supply BY AN IDENTITY.  Fails on KIND.

    "CIRCULATING LIGHT MAKES CTCs" an ORDER claim.  Lands on DOOR TWO -- refuted
                                   specifically by Olum & Everett, and door two
                                   is refused anyway by the bank-loan theorem.
                                   Fails twice over.

    TWO ROWS, TWO DIFFERENT REASONS, AND NEITHER IS THE ONE THE PROPOSAL
    ADDRESSES.  That is the index doing the same job it did in compress.py.

AND IT DOES NOT RESCUE THE INFORMATION CURRENCY EITHER.  compress.py and bits.py
settled that information is not a second currency because Bekenstein bounds it
BY the energy.  LIGHT ENERGY IS ENERGY.  Denominating the same bill in photons
changes neither the bound nor the rate.

stdlib only.  Literature rows are CITED with their references; the exchange-rate
arithmetic, the NEC identity and the intensity gaps are measured here.
"""
import math
import random
import sys

C = 2.99792458e8
G = 6.67430e-11
L_PLANCK = 1.616255e-35
YEAR = 365.25 * 86400.0
AGE_UNIVERSE_YR = 1.38e10
SOLAR_LUMINOSITY = 3.828e26


# ------------------------------------------- 1: the real physics

LINEAGE = (
    ("Tolman, Ehrenfest & Podolsky 1931", "Phys. Rev. 37, 602",
     "thin pencils of light gravitate"),
    ("Scully 1979", "Phys. Rev. D 19, 3582",
     "gravitational coupling between laser beams"),
    ("Mallett 2000", "Phys. Lett. A 269, 214",
     "RING LASER frame dragging, linearised GR -- not the contested paper"),
    ("Mallett 2003", "Found. Phys. 33, 1307",
     "the exact solution and the CTC claim -- the contested one"),
    ("Strohaber 2011", "arXiv:1112.3414",
     "optical vortices, independent confirmation of the frame dragging"),
)


def light_gravitates():
    """Yes.  Energy is energy; T_munu does not ask what form it took."""
    return True


def frame_dragging_is_real():
    """Yes -- ordinary gravitomagnetism, and independently recomputed."""
    return True


CONTESTED_PAPER = "Mallett 2003"


# ------------------------------- 2: the same coupling, priced

def exchange_rate_kg_per_m():
    import phase1
    return phase1.exchange_rate()


def joules_per_metre():
    return exchange_rate_kg_per_m() * C ** 2


def seconds_at_power(power_w=1.0e3):
    return joules_per_metre() / power_w


def ages_of_the_universe(power_w=1.0e3):
    return seconds_at_power(power_w) / YEAR / AGE_UNIVERSE_YR


def metres_bought(power_w=1.0e3, seconds=YEAR):
    return (power_w * seconds / C ** 2) / exchange_rate_kg_per_m()


def planck_lengths_bought(power_w=1.0e3, seconds=YEAR):
    return metres_bought(power_w, seconds) / L_PLANCK


def solar_luminosities_for_a_metre_per_second():
    return joules_per_metre() / SOLAR_LUMINOSITY


# --------------------- 3: null dust satisfies the NEC identically

def minkowski_dot(a, b):
    """Signature (-,+,+,+)."""
    return -a[0] * b[0] + sum(a[i] * b[i] for i in (1, 2, 3))


def random_null(rng):
    x, y, z = (rng.gauss(0.0, 1.0) for _ in range(3))
    n = math.sqrt(x * x + y * y + z * z)
    return (1.0, x / n, y / n, z / n)


def null_dust_nec(eta, k, eps):
    """T_munu k^mu k^nu = eps (eta . k)^2.  A square times a non-negative."""
    return eps * minkowski_dot(eta, k) ** 2


def worst_nec_over(n=200000, seed=11):
    rng = random.Random(seed)
    worst = None
    for _ in range(n):
        v = null_dust_nec(random_null(rng), random_null(rng),
                          abs(rng.gauss(0.0, 1.0)))
        if worst is None or v < worst:
            worst = v
    return worst


def light_can_violate_the_nec():
    """No, and not by a margin -- by the form of the expression."""
    return worst_nec_over(20000) < 0.0


NEC_IS_SATURATED_BY = "light -- it is the most NEC-respecting source in physics"


# --------------------- 4: Mallett's CTC solution, and its refutation

def mallett_lambda(power_w=1.0e3, rho0_m=0.5, r_m=1.0e-3):
    """lambda = pi G P rho_0 / (c^5 r).  Olum & Everett's own expression."""
    return math.pi * G * power_w * rho0_m / (C ** 5 * r_m)


def ctc_log_radius(power_w=1.0e3, rho0_m=0.5, r_m=1.0e-3):
    """CTCs need ln(rho/alpha) > 1/lambda.  Returns log10(rho/rho_0)."""
    return (1.0 / mallett_lambda(power_w, rho0_m, r_m)) / math.log(10.0)


def power_can_buy_past_it(p_lo=1.0e3, p_hi=1.0e15):
    """The dependence is LOGARITHMIC in rho, so 1/lambda is in the exponent.
    Twelve orders of extra power moves the exponent, not the answer."""
    return ctc_log_radius(p_hi) < 100.0


REFUTATIONS = (
    ("magnitude", "lambda ~ 1e-46, so CTCs begin at rho > 10^(1e46) rho_0, and "
                  "the logarithm puts 1/lambda in the exponent"),
    ("the singularity", "R^t_rtr = 1/(8 rho^2) and R_abcd R^abcd = "
                        "3/(4 alpha rho^3) diverge, are not coordinate "
                        "artifacts, and are INDEPENDENT OF lambda -- they "
                        "persist at zero light intensity"),
    ("the apparatus", "rho = const, dphi/dt = 1/alpha are NULL GEODESICS: the "
                      "light orbits the singularity and needs no optics, so "
                      "the ring laser is not the source of the effect"),
)


def divergence_depends_on_intensity():
    """No.  Which is why the spacetime is pathological without the light."""
    return False


def is_minkowski_plus_light():
    return divergence_depends_on_intensity()


STATIC_SPACETIME = (
    "every timelike geodesic originates and terminates at the singularity",
    "a particle at rest at proper distance R is destroyed in proper time ~1.3 R",
    "the singularity fills the entire sky but an infinitesimally thin strip",
)


def finite_version_survives_tipler_hawking():
    """No.  The escape needs a non-compactly-generated Cauchy horizon, which
    needs an INFINITE cylinder.  Olum & Everett say the theorems rule out any
    finite-size approximation."""
    return False


MALLETT_CONCEDED_THE_SINGULARITY = True     # Olum, citing Mallett's 2006 book


# ------------------ 5: what circulating light actually buys

INTENSITY_FOR_1HZ = 1.0e45          # W/cm^2, Strohaber
HERCULES_INTENSITY = 2.0e22         # W/cm^2, the most intense laser system
DAMAGE_THRESHOLD = 1.0e12           # W/cm^2, optical material in a ring laser


def orders_short(have=HERCULES_INTENSITY, need=INTENSITY_FOR_1HZ):
    return math.log10(need / have)


# --------------------- 6: routed through the index

ROUTING = (
    ("use light as the source", "information",
     "the refusal names rho < 0, which null dust cannot supply BY AN IDENTITY",
     "fails on KIND"),
    ("circulating light makes CTCs", "order",
     "refuted specifically, and door two is refused anyway by the bank-loan "
     "theorem", "fails twice"),
)


def information_rate_is_a_constant():
    """rates.py owns the conversion table: the information row is a monomial in
    G, c, hbar and k, with no free parameter to exploit."""
    import rates
    return rates.rate_is_a_monomial("information")


def light_energy_is_energy():
    """It enters T_munu identically, so it uses that same row and same rate."""
    return True


def rescues_the_information_currency():
    """No.  The rate is a constant (rates.py) and light does not get its own
    row (it is energy), so denominating in photons changes neither."""
    return not (information_rate_is_a_constant() and light_energy_is_energy())


def selftest():
    ok = True

    def chk(label, got, want):
        nonlocal ok
        good = got == want
        ok &= good
        print("  %-56s %20s %20s  %s"
              % (label, str(got)[:20], str(want)[:20], "ok" if good else "FAIL"))

    def near(label, got, want, tol=1e-3):
        nonlocal ok
        good = abs(got - want) <= tol * max(1.0, abs(want))
        ok &= good
        print("  %-56s %20.6g %20.6g  %s" % (label, got, want, "ok" if good else "FAIL"))

    print("1. THE REAL PHYSICS, AND IT IS REAL")
    for who, where, what in LINEAGE:
        print("     %-34s %-24s %s" % (who, where, what[:44]))
    chk("does light gravitate", light_gravitates(), True)
    chk("is frame dragging by circulating light real", frame_dragging_is_real(), True)
    chk("and the contested paper is", CONTESTED_PAPER, "Mallett 2003")
    print("       The 2000 ring-laser paper is ordinary gravitomagnetism and")
    print("       it is right.  Nothing here disputes it.")

    print("\n2. BUT THE COUPLING IS THE SAME, SO THE BILL IS THE SAME")
    near("exchange rate, kg per metre", exchange_rate_kg_per_m(), 1.34895e26)
    near("  in joules per metre", joules_per_metre(), 1.21237e43)
    print("     a 1 kW ring laser, to contract ONE METRE:")
    near("  years", seconds_at_power() / YEAR, 3.8418e32)
    near("  AGES OF THE UNIVERSE", ages_of_the_universe(), 2.7839e22)
    print("     a 1 kW ring laser running a full year:")
    near("  metres bought", metres_bought(), 2.6030e-33)
    near("  in PLANCK LENGTHS", planck_lengths_bought(), 161.05, 1e-2)
    print("     one metre per second:")
    near("  in SOLAR LUMINOSITIES", solar_luminosities_for_a_metre_per_second(),
         3.1671e16)
    print("       supply.py said it first: E = mc^2 is already inside G/c^4.")

    print("\n3. AND LIGHT CANNOT DO THE ONE THING NEEDED -- BY AN IDENTITY")
    w = worst_nec_over()
    print("     T_munu k^mu k^nu over 200,000 random (eta, k, eps):")
    print("       minimum found  %+.4e" % w)
    chk("is it ever negative", w < 0.0, False)
    chk("can light violate the NEC at all", light_can_violate_the_nec(), False)
    print("       T_munu k^mu k^nu = eps (eta . k)^2 -- A NON-NEGATIVE TIMES A")
    print("       SQUARE.  Not a margin; the form of the expression.")
    chk("so the NEC is saturated by", NEC_IS_SATURATED_BY,
        "light -- it is the most NEC-respecting source in physics")

    print("\n4. AND MALLETT'S CTC SOLUTION IS REFUTED ON THREE GROUNDS")
    near("lambda for 1 kW, rho_0 = 0.5 m, r = 1 mm", mallett_lambda(), 4.329e-47)
    print("       Olum & Everett quote 'of order 1e-46'.  Order agreement.")
    near("  so CTCs begin at log10(rho/rho_0)", ctc_log_radius(), 1.003e46)
    chk("can twelve more orders of power buy past it",
        power_can_buy_past_it(), False)
    print("       The dependence is LOGARITHMIC: 1/lambda is in the EXPONENT.")
    for what, why in REFUTATIONS:
        print("     %-16s %s" % (what, why[:58]))
    chk("does the curvature divergence depend on the intensity",
        divergence_depends_on_intensity(), False)
    chk("so is it Minkowski plus a light cylinder", is_minkowski_plus_light(), False)
    print("     and the static (eps = 0) spacetime:")
    for s in STATIC_SPACETIME:
        print("       %s" % s)
    chk("does a FINITE version survive Tipler and Hawking",
        finite_version_survives_tipler_hawking(), False)
    print("       The escape needs an INFINITE cylinder.  Every buildable")
    print("       version is closed by the theorems the infinite one dodges.")
    chk("did Mallett concede the singularity",
        MALLETT_CONCEDED_THE_SINGULARITY, True)
    print("       The dispute is about what the solution shows, not honesty.")

    print("\n5. WHAT CIRCULATING LIGHT ACTUALLY BUYS (Strohaber)")
    print("     1 Hz precession on a test particle needs  ~%.0e W/cm^2"
          % INTENSITY_FOR_1HZ)
    print("     Hercules, the most intense laser system   ~%.0e W/cm^2"
          % HERCULES_INTENSITY)
    near("  orders short", orders_short(), 22.699, 1e-3)
    near("  and against a ring laser's damage threshold",
         orders_short(DAMAGE_THRESHOLD), 33.0, 1e-3)
    print("       For a frame drag you could MEASURE -- not a transition.")

    print("\n6. ROUTED THROUGH THE INDEX")
    for claim, row, why, verdict in ROUTING:
        print("     %-30s %-12s %s" % (claim, row, verdict))
        print("       %s" % why[:70])
    chk("is the information rate a constant (rates.py)",
        information_rate_is_a_constant(), True)
    chk("does light get its own row, or is it just energy",
        light_energy_is_energy(), True)
    chk("so does it rescue the information currency",
        rescues_the_information_currency(), False)
    print("       Bekenstein bounds information BY energy, and LIGHT ENERGY IS")
    print("       ENERGY.  Denominating the same bill in photons changes")
    print("       neither the bound nor the rate.")

    print("\n  SELFTEST %s" % ("OK" if ok else "FAILED"))
    return ok


def report():
    print(__doc__)
    print("=" * 79)
    print("A 1 kW RING LASER, AGAINST THIS PROJECT'S OWN EXCHANGE RATE\n")
    print("  %-38s %.4e" % ("joules per metre contracted", joules_per_metre()))
    print("  %-38s %.4e yr" % ("time to contract one metre",
                               seconds_at_power() / YEAR))
    print("  %-38s %.4e" % ("  in ages of the universe", ages_of_the_universe()))
    print("  %-38s %.1f" % ("one year buys, in Planck lengths",
                            planck_lengths_bought()))
    print("  %-38s %.4e" % ("one metre per second, in L_sun",
                            solar_luminosities_for_a_metre_per_second()))
    print("\n  %-38s %.2f orders" % ("Strohaber: short of a 1 Hz frame drag",
                                     orders_short()))
    print("  %-38s %s" % ("can light violate the NEC", light_can_violate_the_nec()))
    print("\n" + "=" * 79)
    print("""VERDICT

  THE PHYSICS UNDERNEATH IS REAL AND THE 2000 PAPER IS NOT THE
  CONTESTED ONE.  Light gravitates -- Tolman, Ehrenfest and Podolsky
  showed it in 1931 -- and Mallett's ring-laser frame dragging (Phys.
  Lett. A 269, 214) is ordinary gravitomagnetism, independently
  recomputed for optical vortices by Strohaber.  Nothing in this tree
  denied that and nothing here does.

  BUT LIGHT IS NOT A CHEAPER SOURCE, BECAUSE THE COUPLING DOES NOT ASK
  WHAT FORM THE ENERGY TOOK.  Against this project's own exchange rate
  of 1.21237e43 joules per metre contracted, a 1 kW ring laser needs
  3.84e32 YEARS -- 2.78e22 AGES OF THE UNIVERSE -- to contract one
  metre.  Run for a full year it buys 161 PLANCK LENGTHS.  One metre
  per second is 3.17e16 SOLAR LUMINOSITIES.  supply.py said it first:
  E = mc^2 is already inside G/c^4, and rates.py generalised it -- a
  constant of nature is not a discount.

  AND THE DECISIVE OBJECTION IS NOT A MAGNITUDE AT ALL.  For null dust,
  T_munu k^mu k^nu = eps (eta . k)^2: A NON-NEGATIVE TIMES A SQUARE.
  Measured over 200,000 random configurations, never negative, and it
  cannot be -- it is the form of the expression, not a bound.

        LIGHT SATISFIES THE NULL ENERGY CONDITION IDENTICALLY.  IT IS
        THE MOST NEC-RESPECTING SOURCE IN PHYSICS.

  The transition's refusal names rho < 0.  Light is not a weak answer
  to that; it is the WRONG KIND of answer, exactly as a density
  argument was the wrong kind for door two.

  AND MALLETT'S CTC SOLUTION IS REFUTED IN THE LITERATURE, THREE WAYS.
  Olum & Everett (Found. Phys. Lett. 18, 379): CTCs begin at
  rho > 10^(1e46) rho_0 for a realistic laser, and BECAUSE THE
  DEPENDENCE IS LOGARITHMIC 1/lambda sits in the exponent, so power
  cannot buy past it.  The curvature diverges on the axis --
  R_abcd R^abcd = 3/(4 alpha rho^3) -- and THE DIVERGENCE DOES NOT
  DEPEND ON THE LIGHT INTENSITY, so it survives at eps = 0: this is not
  Minkowski plus a light cylinder.  And the circulating paths are NULL
  GEODESICS of that background, so the light is orbiting the
  singularity and the ring laser is not doing the work.  Olum's
  follow-up adds that every timelike geodesic ends on the singularity
  and a particle at rest dies in proper time ~1.3 R.  Finally the
  Tipler-Hawking escape needs an INFINITE cylinder: any finite,
  buildable version is closed by the very theorems the idealisation
  dodges.  In fairness, Mallett conceded the singularity himself.

  WHAT CIRCULATING LIGHT ACTUALLY BUYS, from the constructive side:
  Strohaber puts a 1 Hz spin precession -- a frame drag you could
  merely MEASURE -- at ~1e45 W/cm^2, against ~2e22 for the most intense
  laser system built.  22.70 ORDERS SHORT, and 33 orders against a ring
  laser's own optical damage threshold.

  ROUTED THROUGH THE INDEX IT LANDS ON TWO ROWS AND FAILS ON BOTH, for
  two different reasons: as a source it is an INFORMATION claim and
  fails on KIND; as a CTC mechanism it is an ORDER claim, lands on door
  two, and is refuted both specifically and by the bank-loan theorem.
  Neither row is the one the proposal addresses.

  AND IT DOES NOT RESCUE THE INFORMATION CURRENCY.  Bekenstein bounds
  information BY the energy, and LIGHT ENERGY IS ENERGY.  Denominating
  the same bill in photons changes neither the bound nor the rate.""")
    return 0


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    sys.exit(report())
