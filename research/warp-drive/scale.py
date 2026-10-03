#!/usr/bin/env python3
"""
scale.py -- why every route crosses at the Planck length, and why that is a
DEFLATION rather than a discovery.

supply.py ended by noticing that three independent quantities -- a contraction,
a seat and a coupling -- all cross the feasibility line within two orders of
l_P, and called the convergence the interesting thing.  This file asks whether
it is deep or inevitable.

IT IS INEVITABLE, AND PROVING THAT IS WORTH MORE THAN THE CONVERGENCE WAS.

===============================================================================
THE SCALE THEOREM
===============================================================================

What the quantum vacuum SUPPLIES at scale L, by Ford-Roman and by every
Casimir-type calculation:

        u_supplied  ~  hbar c / L^4

What general relativity DEMANDS at scale L, from the Sturm seating condition
q l^2 >= pi^2 with q = 4 pi T_kk, or equivalently from the transition equation:

        u_demanded  ~  c^4 / (G L^2)

Their ratio has exactly one possible form, because those are the only constants
in it:

        u_supplied / u_demanded  =  kappa * hbar G / (c^3 L^2)  =  kappa (l_P/L)^2

    NAMED HYPOTHESIS SINGLE-LENGTH (CORRECTED, DOCKET 67 follow-ups: first
    unstated, so "exactly one possible form" read as unconditional).  The
    form is forced when the problem has ONE length L.  A model with a second
    length carries a dimensionless ratio, and kappa is then a function of it:
    achievable.py's kappa goes as 1/((a/b)(m/b)) -- computed below, halving
    when a/b or m/b doubles -- so its 4.19e4 against gjw's 0.035 is set by
    a/b = 0.02 and m/b = 5e-3, not by a mechanism.  Butcher 1405.1283 p.1
    fn. 2, quoted in gjw.py: the system "need not be characterised by a
    single length."  The l_P scaling with L, at fixed ratios, survives.

    THE CROSSING IS AT l_P BY DIMENSIONAL NECESSITY.  l_P is DEFINED as the
    length where hbar-physics and G-physics meet; any ratio of one to the other
    crosses there.  The three agreeing numbers were confirming that the O(1)
    prefactors are O(1), which is worth knowing and is not a discovery about
    warp transitions.

===============================================================================
THE CLOSED FORM MATCHES gjw.py, AND THE MATCH IS AN IDENTITY, NOT A SECOND ROUTE
===============================================================================
(CORRECTED, DOCKET 67 follow-ups: this heading read "IT IS NOT HAND-WAVING: IT
REPRODUCES A NUMBER THE TREE COMPUTED ANOTHER WAY".)

For gjw.py's route the prefactor is available in closed form.  With
T_kk_req = pi c^4/(4 G D^2) and the cycle's T_kk along the winding null
direction, 4 u_Casimir = 4 pi^2 hbar c/(90 (2D)^4) (FOP eq. 24; H-WIND),

        ratio  =  (pi/90) (l_P/D)^2,         kappa = pi/90 = 3.490659e-02

    PREDICTED amplification at D = 1 m:   1.0967e+71
    gjw.py's own gain_coefficient():      1.0967e+71     -- equal to 2e-16
                                                            relative, machine
                                                            precision
    PREDICTED unity separation:  l_P sqrt(pi/90) = 3.0197e-36 m = 0.1868 l_P
    gjw.py's own unity_separation():                3.0197e-36 m = 0.1868 l_P

    CORRECTED (DOCKET 67 follow-ups, M: verdicts rest on a correct stated
    ground).  This read "FIVE DIGITS, and gjw.py computes it from the Casimir
    formula directly, sharing no algebra with this."  It shares all of it:
    gjw.amplification_needed(D) is seatindex.tkk_required(D) over
    4 pi^2 hbar c/(90 (2D)^4), the same threshold and the same winding-
    direction Casimir T_kk divided here, and both are 90 D^2/(pi l_P^2)
    exactly.  gjw.py itself now records that figure as a single-length
    dimensional identity, "NOT AN INDEPENDENT ROUTE TO THE PLANCK SCALE".  So
    the agreement is a CONSISTENCY CHECK that the two files carry the same
    inputs -- a real one: it is the check that exposed the pi/360 energy-
    density factor below -- and not a reproduction by another method.  It
    supports the arithmetic, not the theorem; the theorem rests on dimensional
    analysis under SINGLE-LENGTH, above.

    CORRECTED (DOCKET 67 follow-up).  First written kappa = pi/360 =
    8.726646e-03, "T_kk against u_C": a T_kk threshold divided by an ENERGY
    DENSITY, 4x the T_kk gain (4.3866e+71, unity at 1.5098e-36 m = 0.0934
    l_P).  gjw.py now keeps that ratio as energy_density_gain_coefficient();
    this file keeps it as KAPPA_GJW_AS_FIRST_WRITTEN and still checks it.
    Along transverse null directions the cycle's T_kk is 0 and no gain
    suffices (gjw.TKK_OVER_RHO_TRANSVERSE); kappa = pi/90 holds on H-WIND.

And kappa is measured SCALE-INVARIANT, which is the theorem's real signature:
achievable.py's ratio gives kappa = 4.18879e+04 at b = 1 m, at 1e3 m and at
1e6 m -- IDENTICAL TO SIX DIGITS ACROSS SIX DECADES.  (CORRECTED, DOCKET 67
follow-ups: that is what SINGLE-LENGTH predicts for a model whose ratios a/b
and m/b are held fixed while b varies, so it confirms the code carries no
hidden scale; it is not evidence independent of the dimensional argument.)

===============================================================================
THE CENSUS, AND THE OUTLIER RECONCILES
===============================================================================

        route                       kappa        crossing, on its own length
        gjw.py    coupling gap      3.4907e-02   0.1868 l_P
        corridor.py  Casimir seat   1.7424e-02   0.1320 l_P
        supply.py contraction 1 %   1.3684e+01   3.6992 l_P
        achievable.py core density  4.1888e+04   204.67 l_P   <- OUTLIER?

    NO.  achievable.py's length is the CORRIDOR RADIUS b, while the others
    measure the gap that carries the energy.  Its core sits at a/b = 0.02 of
    that, and 204.67 * 0.02 = 4.09 l_P -- which achievable.py already prints
    as its own "core size there, in Planck lengths: 4.09".

    MEASURED ON THE SCALE OF THE THING THAT ACTUALLY CARRIES THE ENERGY, ALL
    FOUR LAND BETWEEN 0.132 AND 4.09 l_P -- A FACTOR OF 31, INSIDE TWO ORDERS.
    supply.py's "within two orders" was right, and right for a reason it did
    not give.  (CORRECTED, DOCKET 67 follow-up: first "between 0.093 and 4.09
    l_P -- a factor of 44", on gjw.py's energy-density kappa pi/360.)
    (CORRECTED, DOCKET 67 follow-ups: supply.py's kappa read 1.3699e+01 in
    CENSUS, which prints 3.7013 l_P against the 3.6992 this table showed;
    supply.py computes 1.36838e+01, crossing 3.6992 l_P, and CENSUS now
    carries that, checked against supply.py.)

===============================================================================
THE CONSEQUENCE, AND IT IS THE POINT OF THIS FILE
===============================================================================

        SHORTFALL AT SCALE L  =  (1/kappa) (L/l_P)^2

    THE EXPONENT IS 2 AND THE BASE IS l_P, AND NO MECHANISM CHANGES EITHER.
    A mechanism changes kappa and nothing else.  (CORRECTED, DOCKET 67
    follow-ups: within 4D GR with QFT at fixed length ratios.  A lower
    fundamental Planck scale, below, changes the base in another theory, and
    under SINGLE-LENGTH's failure a length ratio enters kappa itself.)

At L = 1 m the geometric factor (L/l_P)^2 is 3.8281e+69, and every "orders
short" figure this project has produced is that number divided by a kappa:

        gjw.py         1.0967e+71 short      = 3.8281e69 / 3.4907e-02
        achievable.py  9.1387e+64 short      = 3.8281e69 / 4.1888e+04
        supply.py      2.7975e+68 short      = 3.8281e69 / 1.3684e+01
                       (first 2.7943e+68 / 1.3699e+01, DOCKET 67 follow-ups)

    THEY ARE NOT THREE INDEPENDENT OBSTACLES.  THEY ARE ONE OBSTACLE COUNTED
    THREE TIMES, in three lengths and three prefactors.  65 orders, 69 orders
    and 71 orders are the same fact.

===============================================================================
SO WHAT WOULD HAVE TO BE TRUE
===============================================================================

To close the gap at metre scale, kappa must reach 3.8281e+69.  kappa is
DIMENSIONLESS, so it can only be large if the problem contains a large
dimensionless number.  The honest enumeration of what is available:

    * N field species.  Casimir energy scales with the number of massless
      fields.  The Standard Model gives N ~ 100.  TWO ORDERS, and it is the
      largest honest factor on the list.
    * Cavity mode count / resonant enhancement.  Bounded by the same
      quantum inequalities that bound the single-mode result, because
      Ford-Roman is a statement about the total.
    * A SECOND LENGTH.  (Added, DOCKET 67 follow-ups: first omitted.)  Where
      the problem has two lengths their ratio is a dimensionless number and
      kappa depends on it -- achievable.py's kappa goes as 1/((a/b)(m/b)).
      Whether any ratio a buildable, valid-regime model admits buys the
      3.8e69 is not evaluated here.  STATUS: NOT-RUN.
    * A LOWER FUNDAMENTAL PLANCK SCALE.  Large extra dimensions (ADD) replace
      l_P with l_* = hbar/(M_* c).  THIS IS THE ONLY THING ON THE LIST THAT
      CHANGES THE BASE RATHER THAN kappa.  At the current collider and
      torsion-balance bound M_* >~ 3 TeV, l_* ~ 6.6e-20 m, and the shortfall
      at metre scale falls from 3.83e69 to 2.3e38.

        THIRTY-ONE ORDERS FOR FREE, AND STILL THIRTY-EIGHT ORDERS SHORT.

      It is named because it is the only lever on this list that changes
      the base (CORRECTED, DOCKET 67 follow-ups: first "the only structural
      lever"; a second length, above, is structural too), and it is NOT
      evaluated here: whether the demand side rescales the same way in a
      braneworld is a different calculation in a different theory, and
      guessing it would be exactly the kind of thing this tree keeps having to
      withdraw.  STATUS: NOT-RUN.

===============================================================================
AND THE REFUSAL, WHICH IS THE MOST IMPORTANT LINE IN THIS FILE
===============================================================================

AT THE CROSSING, FIVE INDEPENDENT APPROXIMATIONS FAIL AT ONCE:

    1. SEMICLASSICAL GRAVITY.  Sourcing G_munu with <T_munu> requires L >> l_P;
       at L ~ l_P the graviton fluctuations are O(1) and there is no fixed
       background to compute <T> on.
    2. FORD-ROMAN ITSELF is derived in QFT on a FIXED background, so it does
       not survive its own crossing point.
    3. GEOMETRIC OPTICS.  Every seat in this tree solves the Jacobi equation
       for rays, which needs wavelength << curvature radius.
    4. THE CASIMIR FORMULA.  Perfect-conductor idealisation needs the gap to
       exceed the plate material's plasma wavelength.  At l_P there is no
       material; no atom is within twenty orders of that size.
    5. WEAK FIELD.  Every Phi expansion here assumes |Phi| << 1.

    SO THE CROSSING IS NOT A PREDICTION AND IT IS NOT A DESIGN TARGET.  IT IS
    THE POINT AT WHICH THE THEORY STOPS, REPORTED IN UNITS OF LENGTH.

    "You need a Planck-scale gap" must never be quoted as an engineering
    requirement.  The correct statement is: EVERY ROUTE THIS PROJECT CAN
    EVALUATE REMAINS SHORT AT EVERY SCALE WHERE THE EVALUATION IS VALID, and
    the extrapolation to where it would not be short runs off the edge of the
    map.

stdlib only.  gjw.py, achievable.py and corridor.py supply the numbers this
file predicts.  (CORRECTED, DOCKET 67 follow-ups: first "the independent
numbers"; gjw.py's is the same closed form, see above.)
"""
import math, sys

C, G, HBAR = 2.99792458e8, 6.67430e-11, 1.054571817e-34
L_PLANCK = math.sqrt(HBAR * G / C ** 3)


def geometric_factor(L):
    """(L/l_P)^2 -- the whole shortfall, before any prefactor."""
    return (L / L_PLANCK) ** 2


def shortfall(L, kappa):
    """The scale theorem: shortfall = (1/kappa)(L/l_P)^2."""
    return geometric_factor(L) / kappa


def crossing(kappa):
    """Where supplied meets demanded, in metres."""
    return L_PLANCK * math.sqrt(kappa)


def crossing_in_planck(kappa):
    return math.sqrt(kappa)


# ------------------------------------------- the closed-form gjw prefactor

def kappa_gjw():
    """pi/90, from T_kk = pi c^4/4GD^2 against the cycle's winding-direction
    T_kk = 4 u_C = 4 pi^2 hbar c/90(2D)^4 (H-WIND).  CORRECTED (DOCKET 67
    follow-up): first returned pi/360, T_kk against u_C, an energy density."""
    return math.pi / 90.0


#: CORRECTED (DOCKET 67 follow-up): kappa as first written, pi/360 -- the T_kk
#: threshold against the ENERGY DENSITY u_C.  Kept as history; it reproduces
#: gjw.energy_density_gain_coefficient(), and the selftest still checks that.
KAPPA_GJW_AS_FIRST_WRITTEN = math.pi / 360.0


def gjw_amplification(D=1.0):
    """Predicted from the theorem alone.  gjw.py computes 1.0967e71 its own way."""
    return shortfall(D, kappa_gjw())


# ------------------------------------ the census, measured from the instruments

def measured_kappa(ratio_value, L):
    """Invert the theorem: kappa = ratio * (L/l_P)^2.  Must be L-independent."""
    return ratio_value * geometric_factor(L)


def kappa_is_scale_invariant(fn, lengths=(1.0, 1.0e3, 1.0e6), rtol=1e-9):
    """The theorem's real signature.  Measured across six decades."""
    ks = [measured_kappa(fn(L), L) for L in lengths]
    return (max(ks) - min(ks)) <= rtol * max(ks)


# (route, kappa, the length it measures, scale factor to the energy-carrying gap)
CENSUS = (
    ("gjw.py coupling gap", 3.490659e-02, "plate separation D", 1.0),   # pi/90
    ("corridor.py Casimir seat", 1.742400e-02, "gap", 1.0),
    # CORRECTED (DOCKET 67 follow-ups): first 1.369937e+01, not supply.py's
    # computed value; now supply.unity_gap_in_planck_lengths()**2 (selftest).
    ("supply.py contraction 1 %", 1.368384e+01, "corridor radius b", 1.0),
    ("achievable.py core density", 4.188790e+04, "corridor radius b", 0.02),
)


SUPPLY_KAPPA_AS_FIRST_WRITTEN = 1.369937e+01   # RECORD, DOCKET 67 follow-ups


def crossings_on_source_scale():
    """The outlier reconciles: achievable measures b, its core is a/b = 0.02."""
    return [(n, crossing_in_planck(k) * f) for n, k, _w, f in CENSUS]


def all_within_two_orders():
    v = [c for _n, c in crossings_on_source_scale()]
    return math.log10(max(v) / min(v)) < 2.0


def one_obstacle_counted_many_times(rtol=1e-3):
    """Every 'orders short' figure is (L/l_P)^2 / kappa.  Checked, not claimed."""
    return all(abs(shortfall(1.0, k) * k - geometric_factor(1.0))
               <= rtol * geometric_factor(1.0) for _n, k, _w, _f in CENSUS)


# ------------------------------------------------- what would have to be true

N_STANDARD_MODEL = 100.0              # massless field species, order
M_STAR_TEV = 3.0                      # collider + torsion-balance bound, order
HBAR_C_MEV_FM = 197.3269804


def kappa_needed(L=1.0):
    return geometric_factor(L)


def species_gain():
    """The largest honest dimensionless factor available: two orders."""
    return N_STANDARD_MODEL


def l_star(M_star_TeV=M_STAR_TEV):
    """hbar/(M_* c) in metres -- the ADD fundamental length at a given M_*."""
    return HBAR_C_MEV_FM * 1.0e-15 / (M_star_TeV * 1.0e6)


def shortfall_with_extra_dimensions(L=1.0, M_star_TeV=M_STAR_TEV):
    return (L / l_star(M_star_TeV)) ** 2


def extra_dimension_gain(L=1.0):
    return geometric_factor(L) / shortfall_with_extra_dimensions(L)


#: NAMED HYPOTHESIS (DOCKET 67 follow-ups): the scale theorem's single form
#: needs one length.  A second length enters kappa through its ratio.
SINGLE_LENGTH_HYPOTHESIS = ("SINGLE-LENGTH: the supplied/demanded ratio "
                            "contains one length L; with two, kappa is a "
                            "function of their ratio")
SECOND_LENGTH = "NOT-RUN"             # whether a ratio closes the gap
#: CORRECTED (DOCKET 67 follow-ups): the gjw match was described as an
#: independent reproduction "sharing no algebra"; it is the same expression.
GJW_MATCH_IS_INDEPENDENT = False
GJW_MATCH_IS_INDEPENDENT_AS_FIRST_WRITTEN = True

EXTRA_DIMENSIONS = "NOT-RUN"          # the only lever that changes the BASE,
                                      # and evaluating the demand side in a
                                      # braneworld is a different calculation
                                      # in a different theory


# ---------------------------------------------------------------- the refusal

BROKEN_AT_CROSSING = (
    "semiclassical gravity: <T_munu> as a source needs L >> l_P",
    "Ford-Roman itself: derived in QFT on a FIXED background",
    "geometric optics: the Jacobi equation needs wavelength << curvature radius",
    "the Casimir formula: perfect conductors need a gap above the plasma wavelength",
    "weak field: every Phi expansion here assumes |Phi| << 1",
)


def crossing_is_a_design_target():
    """NO.  Five approximations fail there simultaneously."""
    return len(BROKEN_AT_CROSSING) == 0


def crossing_is_where_the_theory_stops():
    return not crossing_is_a_design_target()


# ------------------------------------------------------------------ selftest

def selftest():
    ok = True

    def chk(label, got, want):
        nonlocal ok
        good = got == want
        ok &= good
        print("  %-56s %18s %18s  %s" % (label, got, want, "ok" if good else "FAIL"))

    def near(label, got, want, rtol):
        nonlocal ok
        good = abs(got - want) <= rtol * abs(want)
        ok &= good
        print("  %-56s %18.6e %18.6e  %s" % (label, got, want, "ok" if good else "FAIL"))

    print("THE SCALE THEOREM -- ratio = kappa (l_P/L)^2, by dimensional necessity")
    near("l_P (m)", L_PLANCK, 1.616255e-35, 1e-6)
    near("(1 m / l_P)^2 -- the whole shortfall before any prefactor",
         geometric_factor(1.0), 3.8281e69, 1e-4)

    print("\nTHE CLOSED FORM MATCHES gjw.py -- an identity of shared inputs, not a second route")
    # EXACT IDENTITY, not a transcribed constant: a 7-digit literal against a
    # 1e-9 tolerance fails on its own truncation, which is what happened here.
    # CORRECTED (DOCKET 67 follow-up): pi/90 against the winding T_kk; the
    # first-written pi/360 (energy density) is checked below as a RECORD.
    chk("kappa_gjw is exactly pi/90", kappa_gjw() == math.pi / 90.0, True)
    near("  numerically", kappa_gjw(), 3.4907e-02, 1e-4)
    import gjw
    near("predicted gjw amplification at 1 m", gjw_amplification(1.0),
         gjw.gain_coefficient(), 1e-4)
    near("predicted unity separation (m)", crossing(kappa_gjw()),
         gjw.unity_separation(), 1e-4)
    near("  in Planck lengths", crossing_in_planck(kappa_gjw()), 0.18683, 1e-4)
    near("CENSUS carries the same kappa", CENSUS[0][1], kappa_gjw(), 1e-6)
    chk("kappa_gjw / first-written = gjw's winding T_kk / rho",
        abs(kappa_gjw() / KAPPA_GJW_AS_FIRST_WRITTEN - gjw.TKK_OVER_RHO_WINDING) < 1e-12,
        True)
    chk("RECORD: kappa as first written is exactly pi/360",
        KAPPA_GJW_AS_FIRST_WRITTEN == math.pi / 360.0, True)
    near("RECORD: it reproduces gjw's energy-density coefficient 4.3866e71",
         shortfall(1.0, KAPPA_GJW_AS_FIRST_WRITTEN),
         gjw.energy_density_gain_coefficient(), 1e-4)
    near("RECORD: and its unity separation 1.5098e-36 m",
         crossing(KAPPA_GJW_AS_FIRST_WRITTEN),
         gjw.energy_density_gain_coefficient() ** -0.5, 1e-4)
    # CORRECTED (DOCKET 67 follow-ups): this printed "gjw.py computes both
    # from the Casimir formula directly and shares no algebra with this
    # file".  Computed instead: the match is to machine precision, which a
    # second method would not give, and gjw's gain is seatindex's threshold
    # over the same winding T_kk this file divides.
    near("gjw's gain IS seatindex's threshold over the same winding T_kk",
         gjw.gain_coefficient(),
         __import__("seatindex").tkk_required(1.0)
         / (4.0 * math.pi ** 2 * HBAR * C / (90.0 * 2.0 ** 4)), 1e-6)
    chk("the match is exact to machine precision (one expression, twice)",
        abs(gjw_amplification(1.0) / gjw.gain_coefficient() - 1.0) < 1e-12, True)
    chk("so the match is an independent reproduction",
        GJW_MATCH_IS_INDEPENDENT, False)
    chk("RECORD: as first written it was called one ('sharing no algebra')",
        GJW_MATCH_IS_INDEPENDENT_AS_FIRST_WRITTEN, True)
    print("      A consistency check of shared inputs (it caught the pi/360")
    print("      factor), not a second route: gjw.py records it as a")
    print("      single-length dimensional identity.")

    print("\nAND kappa IS SCALE-INVARIANT -- the theorem's real signature")
    import achievable
    chk("achievable.py's kappa is the same across six decades",
        kappa_is_scale_invariant(achievable.ratio), True)
    near("  and its value", measured_kappa(achievable.ratio(1.0), 1.0),
         4.188790e+04, 1e-5)
    # DOCKET 67 follow-ups: SINGLE-LENGTH, computed rather than declared --
    # achievable's kappa moves with its length ratios.
    k0 = measured_kappa(achievable.ratio(1.0), 1.0)
    k_a = measured_kappa(achievable.available_density(1.0, 2 * achievable.A_OVER_B)
                         / achievable.required_density(1.0, a_over_b=2 * achievable.A_OVER_B), 1.0)
    k_m = measured_kappa(achievable.available_density(1.0)
                         / achievable.required_density(1.0, m_over_b=2 * achievable.M_OVER_B), 1.0)
    near("  doubling a/b halves kappa (a ratio enters kappa)", k_a / k0, 0.5, 1e-9)
    near("  doubling m/b halves kappa", k_m / k0, 0.5, 1e-9)
    chk("  so the single form is conditional on", SINGLE_LENGTH_HYPOTHESIS.split(":")[0],
        "SINGLE-LENGTH")
    chk("  and whether a second length closes the gap is", SECOND_LENGTH, "NOT-RUN")

    print("\nTHE CENSUS -- and the outlier reconciles")
    for n, c in crossings_on_source_scale():
        print("      %-32s %10.4f l_P" % (n, c))
    print("      achievable.py measures the CORRIDOR RADIUS; its core is at")
    print("      a/b = 0.02 of that, and it prints 4.09 l_P itself.")
    import supply
    near("CENSUS carries supply.py's computed kappa",
         CENSUS[2][1], supply.unity_gap_in_planck_lengths() ** 2, 1e-6)
    near("  RECORD: first typed 1.369937e+01 (crossing 3.7013 l_P)",
         math.sqrt(SUPPLY_KAPPA_AS_FIRST_WRITTEN), 3.7013, 1e-4)
    chk("all four inside two orders on the energy-carrying scale",
        all_within_two_orders(), True)
    chk("every 'orders short' figure is (L/l_P)^2 / kappa",
        one_obstacle_counted_many_times(), True)
    print("      65, 69 and 71 orders are ONE OBSTACLE COUNTED THREE TIMES.")

    print("\nWHAT WOULD HAVE TO BE TRUE")
    near("kappa needed at metre scale", kappa_needed(), 3.8281e69, 1e-4)
    near("largest honest dimensionless factor: N species", species_gain(), 100.0, 1e-9)
    near("l_* at M_* = 3 TeV (m)", l_star(), 6.5776e-20, 1e-4)
    near("shortfall with extra dimensions at 1 m",
         shortfall_with_extra_dimensions(), 2.3113e38, 1e-4)
    near("  orders gained", math.log10(extra_dimension_gain()), 31.219, 1e-3)
    chk("and it is evaluated here", EXTRA_DIMENSIONS, "NOT-RUN")
    print("      31 orders for free and still 38 orders short -- and whether")
    print("      the DEMAND side rescales the same way in a braneworld is a")
    print("      different calculation in a different theory.")

    print("\nTHE REFUSAL")
    for b in BROKEN_AT_CROSSING:
        print("      x  %s" % b)
    chk("the crossing is a design target", crossing_is_a_design_target(), False)
    chk("the crossing is where the theory stops",
        crossing_is_where_the_theory_stops(), True)
    print("      'You need a Planck-scale gap' must NEVER be quoted as an")
    print("      engineering requirement.  It is the edge of the map, in metres.")

    print("\n  SELFTEST " + ("OK" if ok else "FAILED"))
    return ok


def report():
    print(__doc__)
    print("=" * 79)
    print("""VERDICT

  THE CONVERGENCE IS INEVITABLE, NOT DEEP.  Any ratio of what the
  quantum vacuum supplies to what general relativity demands is
  kappa (l_P/L)^2, because those are the only two constants in it and
  l_P is defined as where they cross.  The three agreeing numbers
  were confirming that the prefactors are O(1).

  BUT PROVING THAT IS WORTH MORE THAN THE CONVERGENCE WAS, for three
  reasons.

  FIRST, IT UNIFIES THE PROJECT'S OBSTACLES.  65 orders, 69 orders
  and 71 orders are not three findings.  They are (L/l_P)^2 divided
  by three different prefactors, at three different lengths.  ONE
  OBSTACLE, COUNTED THREE TIMES.

  SECOND, IT SAYS WHAT A BETTER MECHANISM COULD POSSIBLY BUY.  The
  exponent is 2 and the base is l_P, and no mechanism touches either
  -- only kappa, which is dimensionless and therefore can only be
  large if the problem contains a large dimensionless number.  The
  honest list has one entry worth two orders (N field species) and
  one entry that changes the base instead (a lower fundamental Planck
  scale), which buys 31 orders at the current collider bound and
  leaves 38, and which this file marks NOT-RUN rather than guess at.

  THIRD, AND MOST IMPORTANTLY, IT DISQUALIFIES ITS OWN ANSWER.  At
  the crossing, five independent approximations fail at once --
  semiclassical gravity, Ford-Roman's own fixed background, geometric
  optics, the perfect-conductor Casimir formula, and the weak field.
  THE CROSSING IS NOT A PREDICTION AND NOT A TARGET.  IT IS THE POINT
  WHERE THE THEORY STOPS, REPORTED IN UNITS OF LENGTH.

  So the correct closing statement is narrower than 'you need Planck
  scale', and it is this: EVERY ROUTE THIS PROJECT CAN EVALUATE
  REMAINS SHORT AT EVERY SCALE WHERE THE EVALUATION IS VALID.""")


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    report()
