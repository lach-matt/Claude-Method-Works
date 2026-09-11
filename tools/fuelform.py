#!/usr/bin/env python3
"""fuelform.py -- is there a material other than salt, and what does it cost?

WHY THIS FILE EXISTS
--------------------
materials.py says the blanket's chemistry is FORCED rather than chosen, in a
chain of three links:

    1. nu = 2.9 is Pu-239 FAST, so there is no thermal spectrum
    2. L = 0.20 must cover fission products for forty years, so the fuel
       must be LIQUID
    3. a liquid fast fuel is a SALT, and a fast salt is a CHLORIDE

deck.py --provenance then found that the chloride is the one material in the
design with no critical benchmark behind it: the first fast-chloride
criticality experiment is being built and has not run, the Cl-35 evaluated
data are known to disagree with measurement OUTSIDE their own covariance, and
this project's one-group model has never been checked on it.

So the question is whether the chain is as forced as it says. THIS FILE TESTS
EACH LINK, and two of the three turn out to be weaker than stated.

THE RESULT THAT MATTERS, AND IT WAS NOT EXPECTED
------------------------------------------------
The always-subcritical property -- criticality.py's central claim, the reason
k = 0.900 was adopted, the reason the hazard class "stops existing rather
than being managed" -- IS NOT BOUGHT BY THE SALT.

k_inf is a RATIO of macroscopic cross sections, and every one of them scales
with density, so DENSITY CANCELS. A dense fuel and a dilute one at the same
fissile fraction and the same absorber-per-heavy-atom have the same k_inf.
What sets the threshold is the fissile fraction and what the carrier absorbs,
and across every candidate fuel form the crossing sits in a band 1.35 wide.

    python3 tools/fuelform.py
    python3 tools/fuelform.py --selftest
stdlib only.
"""

import argparse
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

import fuelchoice as F                                          # noqa: E402
import materials as M                                           # noqa: E402

# ---- carrier cross sections, one-group fast, barns -------------------------
# The same discipline as fuelchoice.XS, which these join: each is a SOURCED
# band with the mid used, and the selftest asserts the ORDERING they imply
# rather than the values, because the ordering survives a better spectrum and
# the values do not.
CARRIERS = {
    "O": (0.0, 0.0002, 0.0),    # oxygen is nearly transparent in a fast
                                # spectrum, which is why oxide fuel needs the
                                # least fissile of any form here
    "N14": (0.0, 0.030, 0.0),   # the (n,p) is large -- which is exactly why
                                # nitride fuel programmes discuss N-15
                                # enrichment, and it is the same argument
                                # this design makes for Cl-37
    "Zr": (0.0, 0.020, 0.0),    # the IFR metal fuel's alloying addition
    "Pb": (0.0, 0.005, 0.0),
    "Bi": (0.0, 0.010, 0.0),    # and its (n,gamma) makes Po-210, which is
                                # LBE's own worst problem and not a
                                # neutronic one
    "Fe": (0.0, 0.010, 0.0),
}

# ---- WHAT LINK 2 IS ACTUALLY WORTH, WHICH NOTHING HERE HAD COMPUTED --------
# The report below says of link 2 that "an online loop holds a lower
# equilibrium fission-product inventory -- but 'the fuel must be liquid'
# overstates it, and this work has never priced the difference."
#
# --removal prices it, and the first thing it finds is a COMPARISON ERROR in
# the chain it is testing. materials.py's link 2 reads:
#
#     "A solid-fuel core accumulates fission-product capture MONOTONICALLY
#      and would eat that budget. The fuel must therefore be LIQUID."
#
# That is online removal against NEVER REMOVING ANYTHING, and against never
# the chain's arithmetic is right -- forty years of accumulation costs very
# nearly the whole L = 0.20 allowance. But nobody proposes never. The
# alternative to online removal is BATCH removal, which is what every solid
# fast fuel that has ever operated actually did, and the comparison that
# decides link 2 is online against batch.
FP_SIGMA_A = 0.20            # barn, lumped one-group fast capture of fission
                             # products                             SOURCED
FP_SIGMA_RMS = 0.10          # the one-group capture cross sections of the
                             # important individual fission products agree to
                             # better than this RMS across evaluated
                             # datasets, and it is the only uncertainty this
                             # file claims for the lump              SOURCED
FP_PER_FISSION = 2.0         # two fragments per fission                EXACT
# The leakage-and-parasitic budget link 2 says the fission products must fit
# inside is powersource.LEAK_PARASITIC_HI. It is IMPORTED and never restated
# here -- see l_allowance() below.

# (label, atoms-per-heavy-atom multiplier on a year's production, note)
# An online loop at residence tau holds tau worth of production. A batch
# cycle of T years averages T/2 and peaks at T. Never-removed is the whole
# life, and it is in the table only because it is the case the chain
# compared against.
REMOVAL_CASES = (
    ("online, 30 day residence", 30.0 / 365.25, "the design's own loop"),
    ("online, 90 day residence", 90.0 / 365.25, "a slack online loop"),
    ("batch, 2 year cycle, average", 1.0, "EBR-II class"),
    ("batch, 3 year cycle, average", 1.5, "EBR-II class"),
    ("batch, 5 year cycle, average", 2.5, "a long batch cycle"),
    ("batch, 5 year cycle, END OF CYCLE", 5.0, "the peak, not the average"),
    ("never removed, 40 years", 40.0, "THE CASE THE CHAIN COMPARED AGAINST"),
)


def _exp():
    sys.path.insert(0, HERE)
    import explore
    return explore


def _psrc():
    sys.path.insert(0, HERE)
    import powersource
    return powersource


def l_allowance():
    """L, the leakage-and-parasitic allowance, from the file that owns it."""
    return _psrc().LEAK_PARASITIC_HI


def design_fissile_fraction():
    """The operating fissile fraction, imported and never restated.

    The low-leakage end, which is the design's own operating point and the
    conservative end for this calculation: less fissile is less absorption,
    so a fission product costs proportionally more."""
    P = _psrc()
    return F.fraction_for_k(P.K_DESIGN, "Pu239", "U238", P.LEAK_PARASITIC_LO)


def design_carriers():
    r = F.atom_ratios(F.mol_fraction_for_u_mass(M.SALT_U_MASS_FRAC))
    return {"Cl": r["Cl"], "Na": r["Na"]}


def absorption_per_heavy_atom(f=None):
    """Total absorption per heavy-metal atom, barns, at the design salt.

    This is k_infinity's own denominator. A fission product's penalty is its
    absorption divided by this, which is why the figure has to come from the
    same arithmetic the design's k does."""
    f = design_fissile_fraction() if f is None else f
    sf_a, sc_a, _ = F.XS["Pu239"]
    sf_b, sc_b, _ = F.XS["U238"]
    a = f * (sf_a + sc_a) + (1.0 - f) * (sf_b + sc_b)
    for nuc, n in design_carriers().items():
        a += n * F.XS[nuc][1]
    return a


def fp_atoms_per_heavy_atom_per_year():
    """Fission products made per heavy-metal atom per year.

    materials.burnup_fraction_per_year() is the share of the holding that
    fissions in a year; each fission makes two fragments."""
    return FP_PER_FISSION * M.burnup_fraction_per_year()


def k_penalty(n_fp, sigma=FP_SIGMA_A):
    """The relative fall in k from holding n_fp fission products per heavy
    atom. Fission products only absorb, so this is a pure denominator term
    and the sign is always negative for k."""
    return n_fp * sigma / absorption_per_heavy_atom()


def beam_penalty(dk_over_k):
    """What that fall in k costs in beam power, through explore.py's own
    elasticity at the design point. THIS is where the small number stops
    being small: the plant lives in the last 0.123 of multiplication."""
    return dk_over_k * abs(_exp().elasticity("k_eff"))


def cases():
    y = fp_atoms_per_heavy_atom_per_year()
    out = []
    for label, mult, note in REMOVAL_CASES:
        n = y * mult
        dk = k_penalty(n)
        out.append((label, n, dk, beam_penalty(dk), note))
    return tuple(out)


def fraction_for_k_inf(target):
    x = F.mol_fraction_for_u_mass(M.SALT_U_MASS_FRAC)
    lo, hi = 0.0, 0.5
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        if F.k_infinity(mid, "Pu239", "U238", x=x) < target:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


def compensating_fraction(dk_over_k):
    """The loading fissile fraction that offsets an end-of-cycle penalty.

    This is what a batch plant actually does: load enough extra fissile at
    beginning of cycle that the plant still makes its power at end of cycle.
    It is also the step that walks the composition toward the threshold the
    whole safety architecture stands on."""
    f0 = design_fissile_fraction()
    x = F.mol_fraction_for_u_mass(M.SALT_U_MASS_FRAC)
    k0 = F.k_infinity(f0, "Pu239", "U238", x=x)
    return fraction_for_k_inf(k0 * (1.0 + dk_over_k))


def always_subcritical_threshold():
    """The design salt's own k_inf = 1 crossing -- the fissile fraction above
    which some geometry of this fuel can be made critical."""
    return crossing(design_carriers())


def longest_compensable_cycle_y():
    """The batch cycle beyond which compensating the swing at loading crosses
    the always-subcritical threshold.

    THIS IS THE COUPLING NOTHING HERE HAD STATED. The batch cycle is not
    bounded by chemistry or by the leakage budget. It is bounded by the one
    property criticality.py says the design's hazard class rests on."""
    f0 = design_fissile_fraction()
    x = F.mol_fraction_for_u_mass(M.SALT_U_MASS_FRAC)
    k0 = F.k_infinity(f0, "Pu239", "U238", x=x)
    kt = F.k_infinity(always_subcritical_threshold(), "Pu239", "U238", x=x)
    head = kt / k0 - 1.0
    n = head * absorption_per_heavy_atom() / FP_SIGMA_A
    return n / fp_atoms_per_heavy_atom_per_year()


# ---- the candidate fuel forms ----------------------------------------------
# (carriers per heavy-metal atom, state, fission-product removal, operating
#  history, criticality benchmarks)
Form = "name carriers state removal history benchmarks".split()


def forms():
    x = F.mol_fraction_for_u_mass(M.SALT_U_MASS_FRAC)
    r = F.atom_ratios(x)
    eu = F.atom_ratios(F.EUTECTIC_MOL_UCL3)
    return (
        ("NaCl-UCl3, the design's 18.9 mol %",
         {"Cl": r["Cl"], "Na": r["Na"]}, "liquid", "online, continuous",
         "NONE -- no fast chloride salt has ever gone critical",
         "NONE -- MCRE is being built to make the first"),
        ("NaCl-UCl3 at the eutectic, 34 mol %",
         {"Cl": eu["Cl"], "Na": eu["Na"]}, "liquid", "online, continuous",
         "NONE", "NONE -- this is MCRE's own salt"),
        ("LiF-ThF4-UF4 fluoride salt",
         {"F": 7.444, "Li7": 3.444}, "liquid", "online, continuous",
         "MSRE, thermal, 1965-69", "MSFR two-code benchmark, thermal-adjacent"),
        ("MOX oxide, bare fuel",
         {"O": 2.0}, "solid", "batch, aqueous or pyro",
         "Phenix, Superphenix, BN-600, BN-800, Joyo, FFTF -- decades",
         "abundant"),
        ("MOX in lead-bismuth, 50 vol % coolant",
         {"O": 2.0, "Pb": 2.6, "Bi": 1.4}, "solid", "batch",
         "the ADS field's own choice: MYRRHA and CiADS",
         "abundant, plus LBE-specific work"),
        ("U-Pu-Zr metal, the IFR fuel",
         {"Zr": 0.30}, "solid", "batch pyroprocessing, DEMONSTRATED",
         "EBR-II, thirty years, with its fuel cycle closed on site",
         "abundant"),
        ("mononitride fuel",
         {"N14": 1.0}, "solid", "batch",
         "test irradiations only", "some"),
        ("molten plutonium metal, Pu-Fe eutectic",
         {"Fe": 1.0}, "liquid", "liquid, but never demonstrated",
         "LAMPRE, Los Alamos, critical 1961, several thousand hours",
         "little"),
    )


def _xs():
    """fuelchoice's table, extended with the carriers this file adds.

    Extended rather than copied: an instrument imports a seated table, it
    never restates one."""
    x = dict(F.XS)
    x.update(CARRIERS)
    return x


def crossing(carriers, fissile="Pu239", fertile="U238"):
    """The fissile fraction at which k_inf = 1 for this form."""
    saved = dict(F.XS)
    F.XS.update(CARRIERS)
    try:
        lo, hi = 0.0, 0.95
        if F.k_infinity(hi, fissile, fertile, carriers=carriers) < 1.0:
            raise ValueError("no fissile fraction reaches k_inf = 1 here")
        for _ in range(200):
            mid = 0.5 * (lo + hi)
            if F.k_infinity(mid, fissile, fertile, carriers=carriers) < 1.0:
                lo = mid
            else:
                hi = mid
        return 0.5 * (lo + hi)
    finally:
        F.XS.clear()
        F.XS.update(saved)


def crossing_band():
    vals = [crossing(c) for _n, c, _s, _r, _h, _b in forms()]
    return min(vals), max(vals)


def salt_is_special():
    """Does the chloride salt buy a threshold the other forms cannot reach?

    Returns the design salt's crossing divided by the best other form's. If
    it is not comfortably below one, the salt is not what buys the property.
    """
    rows = forms()
    salt = crossing(rows[0][1])
    others = [crossing(c) for n, c, _s, _r, _h, _b in rows
              if "NaCl" not in n]
    return salt / min(others)


def report():
    lo, hi = crossing_band()
    print()
    print("  IS THERE A MATERIAL OTHER THAN SALT?")
    print()
    print("    materials.py says the chemistry is FORCED rather than chosen,")
    print("    in three links: the spectrum must be fast, so the fuel must be")
    print("    liquid to remove fission products for forty years, so it must")
    print("    be a salt, and a fast salt is a chloride. deck.py --provenance")
    print("    then found the chloride is the one material in the design with")
    print("    NO CRITICAL BENCHMARK BEHIND IT. So the chain is worth")
    print("    testing, and two of its three links are weaker than stated.")
    print()
    print("    LINK 3 FIRST, BECAUSE IT IS THE ONE THAT BREAKS.")
    print()
    print("    The always-subcritical property -- criticality.py's central")
    print("    claim and the reason k = 0.900 was adopted -- IS NOT BOUGHT BY")
    print("    THE SALT. k_inf is a RATIO of macroscopic cross sections and")
    print("    every one of them scales with density, SO DENSITY CANCELS. A")
    print("    dense fuel and a dilute one at the same fissile fraction and")
    print("    the same absorber per heavy atom have the same k_inf. What")
    print("    sets the threshold is the fissile fraction and what the")
    print("    carrier absorbs, and nothing else.")
    print()
    print("      fuel form                                k_inf = 1 at")
    for name, car, _st, _rem, _hist, _bench in sorted(
            forms(), key=lambda t: crossing(t[1])):
        mark = "   <- the design" if "18.9" in name else ""
        print(f"      {name:<42} {100 * crossing(car):5.2f} %{mark}")
    print()
    print(f"    THE WHOLE BAND IS {100 * lo:.2f} TO {100 * hi:.2f} PERCENT --"
          f" A SPREAD OF {hi / lo:.2f}.")
    print("    Every fast fuel form has an always-subcritical threshold, and")
    print("    they are all in the same place. The salt is not special, and")
    print(f"    the design's own salt is the SECOND WORST of them: it")
    print(f"    crosses at {100 * crossing(forms()[0][1]):.2f} % against"
          f" {100 * lo:.2f} % for bare oxide and"
          f" {100 * crossing(forms()[4][1]):.2f} % for")
    print(f"    MOX in lead-bismuth, so it needs {salt_is_special():.2f} times"
          " MORE fissile than")
    print("    the best form for the same property.")
    print()
    print("    LINK 2, WHICH IS WEAKER THAN IT LOOKS. 'The fuel must be")
    print("    liquid' is really 'fission products must come out', and a")
    print("    liquid is one way to do that. It is not the only demonstrated")
    print("    one:")
    print()
    print("      form                                       fission-product"
          " removal")
    for name, _c, _st, rem, _h, _b in forms():
        print(f"      {name:<42} {rem}")
    print()
    print("    EBR-II CLOSED ITS OWN FUEL CYCLE ON SITE FOR THIRTY YEARS with")
    print("    solid metal fuel and batch pyroprocessing. Batch is not online")
    print("    and the difference is real -- an online loop holds a lower")
    print("    equilibrium fission-product inventory -- but 'the fuel must be")
    print("    liquid' overstates it, and this work has never priced the")
    print("    difference.")
    print()
    print("    LINK 1 STANDS. Nothing here challenges the fast spectrum:")
    print("    nu = 2.9 is Pu-239 fast, materials.py derives it, and every")
    print("    form in the table above is a fast form.")
    print()
    print("    AND NOW THE COLUMN THAT DECIDES IT, WHICH IS THE ONE THIS")
    print("    PROJECT KEEPS LEARNING TO PUT FIRST.")
    print()
    print("      form                                       operating"
          " history")
    for name, _c, _st, _r, hist, _b in forms():
        print(f"      {name:<42} {hist}")
    print()
    print("      form                                       criticality"
          " benchmarks")
    for name, _c, _st, _r, _h, bench in forms():
        print(f"      {name:<42} {bench}")
    print()
    print("    THE DESIGN'S OWN MATERIAL IS THE ONLY ROW WITH 'NONE' IN BOTH")
    print("    COLUMNS, and the ADS field -- MYRRHA and CiADS, the two")
    print("    accelerator-driven systems actually being built -- chose MOX")
    print("    in lead-bismuth, which has decades of operating fast reactors")
    print("    and abundant benchmarks behind it AND a lower threshold.")
    print()
    print("    SO WHAT DOES THE SALT UNIQUELY BUY? ONE THING: ONLINE fission-")
    print("    product removal, which is link 2 and is real. What it uniquely")
    print("    costs is PROVENANCE -- no benchmark, no operating history, and")
    print("    a chlorine evaluation known to disagree with measurement")
    print("    outside its own covariance.")
    print()
    print("    AND deck.py --provenance SAYS THE SALT MAY NOT DELIVER THE")
    print("    SAFETY PROPERTY AT ITS OPERATING FRACTION ANYWAY. If that flag")
    print("    holds, the design is paying its entire provenance budget for a")
    print("    property it does not get, and the same property is available")
    print("    at a lower fissile fraction in a material with sixty years of")
    print("    operating history.")
    print()
    print("    THIS FILE DOES NOT TAKE THE DECISION. It is a change of")
    print("    material, it costs the online removal loop, and what that loop")
    print("    is worth in equilibrium fission-product inventory has never")
    print("    been computed here. WHAT IT DOES IS REMOVE THE WORD 'FORCED'")
    print("    FROM A CHOICE THAT WAS NEVER FORCED, and put the trade where")
    print("    the author can see both sides of it.")
    print()


def report_removal():
    y = fp_atoms_per_heavy_atom_per_year()
    a = absorption_per_heavy_atom()
    rows = cases()
    never = rows[-1]
    b2, b3, b5, peak = rows[2], rows[3], rows[4], rows[5]
    on30 = rows[0]
    L = l_allowance()
    print()
    print("  WHAT ONLINE FISSION-PRODUCT REMOVAL IS WORTH")
    print()
    print("    The main report leaves link 2 of materials.py's chain open: it")
    print("    says 'the fuel must be liquid' overstates 'fission products")
    print("    must come out', and that this work has never priced the")
    print("    difference. This prices it. And the first thing it finds is")
    print("    not a number, it is A COMPARISON ERROR IN THE CHAIN.")
    print()
    print("    materials.py's link 2 reads: a solid-fuel core accumulates")
    print("    fission-product capture MONOTONICALLY and would eat the L =")
    print(f"    {L:.2f} budget, so the fuel must be liquid. That is online")
    print("    removal against NEVER REMOVING ANYTHING. Nobody proposes")
    print("    never. Every solid fast fuel that has ever operated removed")
    print("    fission products in BATCHES, and the comparison that decides")
    print("    link 2 is online against batch.")
    print()
    print("    THE ARITHMETIC. Fission products only absorb, so a holding of")
    print("    n per heavy-metal atom costs a relative fall in k of")
    print("    n x sigma / (absorption per heavy atom):")
    print()
    print(f"      fissile fraction, the design's own      "
          f"{100 * design_fissile_fraction():.3f} %")
    print(f"      absorption per heavy atom               {a:.4f} barn")
    print(f"      lumped fission-product capture          {FP_SIGMA_A:.2f}"
          f" barn, SOURCED, +/- {100 * FP_SIGMA_RMS:.0f} % RMS")
    print(f"      fissions per heavy atom per year        "
          f"{M.burnup_fraction_per_year():.6f}")
    print(f"      fission products per heavy atom per year {y:.6f}")
    print()
    print("      removal regime                        n_FP/HM    dk/k"
          "     beam")
    for label, n, dk, beam, _note in rows:
        print(f"      {label:<36} {n:8.5f}  {100 * dk:6.3f} %"
              f"  +{100 * beam:5.1f} %")
    print()
    print(f"    AGAINST NEVER, THE CHAIN IS RIGHT. {100 * never[2]:.1f} PERCENT"
          f" OF K, against an L")
    print(f"    allowance of {100 * L:.0f} percent -- forty years of"
          " accumulation does eat")
    print("    very nearly the whole budget, and a fuel that cannot remove")
    print("    fission products at all is excluded. That much of link 2")
    print("    stands and is not disturbed here.")
    print()
    print(f"    AGAINST BATCH, IT DOES NOT. A two-year cycle averages"
          f" {100 * b2[2]:.2f} %")
    print(f"    of k and a three-year cycle {100 * b3[2]:.2f} %"
          f" -- {b3[2] / L * 100:.1f} percent of the")
    print(f"    allowance the chain says it would eat, and"
          f" {never[2] / b3[2]:.0f} times smaller than the")
    print("    case the chain compared against. ON THE LEAKAGE BUDGET, WHICH")
    print("    IS THE ARGUMENT LINK 2 ACTUALLY MAKES, BATCH REMOVAL PASSES.")
    print()
    print("    SO LINK 2 DOES NOT FORCE A LIQUID. It forces removal, and")
    print("    batch removal is removal. What the liquid buys is the")
    print("    difference between the rows, and that difference is real:")
    print()
    print(f"      online at {on30[0].split(', ')[1]:<24}"
          f" {100 * on30[2]:6.3f} % of k")
    print(f"      batch, three-year cycle           {100 * b3[2]:6.3f} % of k")
    print(f"      the difference                    "
          f"{100 * (b3[2] - on30[2]):6.3f} % of k")
    print()
    print("    AND THAT IS WHERE THE SMALL NUMBER STOPS BEING SMALL. explore")
    print("    .py's elasticity at the design point is"
          f" {_exp().elasticity('k_eff'):.1f}: the plant lives in")
    print("    the last 0.123 of multiplication, so a one percent fall in k")
    print("    costs seventeen percent more beam. Through it, a three-year")
    print(f"    batch cycle costs {100 * b3[3]:.1f} PERCENT MORE BEAM than the"
          " design's own")
    print(f"    online loop, and a five-year cycle costs {100 * b5[3]:.1f}"
          " percent on average")
    print(f"    and {100 * peak[3]:.1f} percent at end of cycle. THE LIQUID"
          " IS WORTH ABOUT A")
    print("    TENTH OF THE BEAM AGAINST A THREE-YEAR BATCH CYCLE, and that")
    print("    is the price of the provenance the salt does not have.")
    print()
    print("    TWO THINGS RUN THE OTHER WAY AND BOTH ARE RECORDED.")
    print()
    print("    FIRST, THE SIGN IS SAFE. Fission products only absorb, so a")
    print("    batch plant's k FALLS through its cycle. In a subcritical")
    print("    source-driven assembly that is a power droop the beam follows,")
    print("    not a reactivity excursion: the composition moves AWAY from")
    print("    critical as it burns. Batch costs money and not margin.")
    print()
    print("    SECOND, AND IT IS THE FINDING THIS SECTION EXISTS FOR: THE")
    print("    OBVIOUS FIX FOR THE DROOP IS BOUNDED BY THE SAFETY PROPERTY.")
    print("    A batch plant offsets the swing by loading extra fissile at")
    print("    beginning of cycle. Do that here and the loading composition")
    print("    walks toward the always-subcritical threshold:")
    print()
    print(f"      the design's operating fraction         "
          f"{100 * design_fissile_fraction():.3f} %")
    for label, _n, dk, _b, _note in (b3, b5, peak):
        short = label.replace("batch, ", "").replace(" cycle", "")
        print(f"      loaded to offset {short:<22}"
              f"{100 * compensating_fraction(dk):>6.3f} %")
    print(f"      the always-subcritical threshold        "
          f"{100 * always_subcritical_threshold():.3f} %  <- criticality.py")
    print()
    print(f"    THE LONGEST BATCH CYCLE THAT CAN BE COMPENSATED AT LOADING")
    print(f"    WITHOUT CROSSING THAT THRESHOLD IS"
          f" {longest_compensable_cycle_y():.2f} YEARS. Beyond it the")
    print("    plant is loading a fuel some geometry of which can be made")
    print("    critical, which is the property criticality.py says the whole")
    print("    hazard class rests on. THE BATCH CYCLE IS NOT BOUNDED BY")
    print("    CHEMISTRY OR BY THE LEAKAGE BUDGET. IT IS BOUNDED BY THE")
    print("    ALWAYS-SUBCRITICAL PROPERTY, and nothing here had stated that")
    print("    coupling.")
    print()
    print("    WHAT IS NOT COUNTED, AND EACH WOULD MOVE IT. Fissile burnup")
    print("    and breeding are excluded -- the design holds its fissile")
    print("    fraction by breeding at f_b, so this is the residual swing")
    print("    and not the whole one. The lump is a lump: individual fission")
    print(f"    products agree to {100 * FP_SIGMA_RMS:.0f} percent RMS across"
          " evaluated data, which is")
    print("    the only uncertainty claimed for it, and a real spectrum would")
    print("    move it further. Out-of-pile inventory, decay heat, and the")
    print("    handling campaign a batch cycle needs are costs this file does")
    print("    not price at all.")
    print()
    print("    THE DECISION IS STILL NOT TAKEN HERE. What has changed is")
    print("    that link 2 now has a number instead of a word: the liquid is")
    print(f"    worth about {100 * b3[3]:.0f} percent of the beam, not the"
          " existence of the plant,")
    print("    and it is bought with a material that has no benchmark.")
    print()


def selftest():
    fail = 0

    def check(label, ok):
        nonlocal fail
        if not ok:
            fail += 1
        print(f"  {label:<64} {'PASS' if ok else 'FAIL'}")

    def raises(fn):
        try:
            fn()
        except ValueError:
            return True
        return False

    print()
    print("  the table is a table")
    rows = forms()
    check("every form carries all six columns",
          all(len(r) == 6 for r in rows))
    check("every carrier has a cross section",
          all(n in _xs() for _nm, c, _s, _r, _h, _b in rows for n in c))
    check("the design's salt is the first row",
          "18.9" in rows[0][0])
    check("fuelchoice's own table is left unmodified afterwards",
          "O" not in F.XS and "Pb" not in F.XS)

    print()
    print("  the result the file was written to get")
    lo, hi = crossing_band()
    check("every form has a k_inf = 1 crossing",
          all(0.0 < crossing(c) < 0.5 for _n, c, _s, _r, _h, _b in rows))
    check("  -- so the always-subcritical property is not the salt's alone",
          hi / lo < 2.0)
    check("  -- and the band is narrow, which is the finding",
          hi / lo < 1.5)
    check("the design's salt is NOT the best form on this axis",
          salt_is_special() > 1.0)
    check("  -- MOX in lead-bismuth crosses lower than the design's salt",
          crossing(rows[4][1]) < crossing(rows[0][1]))
    check("oxygen is the most transparent carrier, so oxide needs least",
          crossing(rows[3][1]) == min(crossing(c)
                                      for _n, c, _s, _r, _h, _b in rows))
    # DENSITY CANCELS, which is the physics the whole finding rests on, and
    # the cleanest way to assert it is STRUCTURAL: k_inf is a ratio of
    # macroscopic cross sections, every one of which carries the same number
    # density, so a density cannot enter the function at all. It does not.
    import inspect
    check("k_inf takes no density, because a ratio cannot depend on one",
          not any("rho" in p or "dens" in p
                  for p in inspect.signature(F.k_infinity).parameters))
    check("  -- and a form is specified by carriers PER HEAVY ATOM alone",
          all(isinstance(v, float) for _n, c, _s, _r, _h, _b in rows
              for v in c.values()))

    print()
    print("  the provenance column, which is what decides it")
    only_none = [n for n, _c, _s, _r, h, b in rows
                 if h.startswith("NONE") and b.startswith("NONE")]
    check("some form has NONE in both history and benchmarks",
          len(only_none) > 0)
    check("  -- and every one of them is the chloride",
          all("NaCl" in n for n in only_none))
    check("the ADS field's own choice is in the table",
          any("MYRRHA" in h for _n, _c, _s, _r, h, _b in rows))
    # A carrier heavy enough in absorption that NO fissile fraction reaches
    # k_inf = 1 is refused rather than returned as a number, because "the
    # threshold is 100 %" would read as an answer and is the absence of one.
    check("a form that cannot reach k_inf = 1 at all is refused",
          raises(lambda: crossing({"Cl": 2000.0})))

    print()
    print("  and what the file refuses")
    import contextlib
    import io
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        report()
    out = buf.getvalue()
    check("it does not take the decision",
          "DOES NOT TAKE THE DECISION" in out)
    check("  -- and says what the salt uniquely buys",
          "ONLINE fission-" in out)
    check("  -- and that the cost of losing it has never been computed here",
          "never" in out and "been computed here" in out)
    check("  -- and removes the word 'forced' rather than choosing for anyone",
          "REMOVE THE WORD 'FORCED'" in out)
    check("link 1 is left standing", "LINK 1 STANDS" in out)

    print()
    print("  --removal: what the liquid actually buys")
    rows = cases()
    on30, b3, peak, never = rows[0], rows[3], rows[5], rows[-1]
    check("the never-removed case eats essentially the whole L allowance",
          never[2] > 0.8 * l_allowance())
    check("  -- so link 2's arithmetic against NEVER is right",
          never[2] > 10.0 * b3[2])
    check("a three-year batch cycle costs about one percent of k",
          0.002 < b3[2] < 0.02)
    check("  -- which is a small share of the allowance it was said to eat",
          b3[2] / l_allowance() < 0.10)
    check("online is cheaper than batch, so the difference is real",
          on30[2] < b3[2])
    check("  -- and through the k cliff it is worth tens of percent in beam",
          0.05 < b3[3] < 0.30)
    check("the compensating load walks TOWARD the safety threshold",
          compensating_fraction(peak[2]) > design_fissile_fraction())
    check("  -- and crosses it at a finite cycle length, which is the finding",
          2.0 < longest_compensable_cycle_y() < 20.0)
    check("  -- the threshold is the design salt's own, not the eutectic's",
          abs(always_subcritical_threshold() - crossing(design_carriers()))
          < 1e-12)
    check("L is imported from the file that owns it, never restated",
          l_allowance() == _psrc().LEAK_PARASITIC_HI)

    buf2 = io.StringIO()
    with contextlib.redirect_stdout(buf2):
        report_removal()
    out2 = buf2.getvalue()
    check("the report names the comparison error rather than the number",
          "COMPARISON ERROR" in out2)
    check("  -- and says the chain is RIGHT against never",
          "THE CHAIN IS RIGHT" in out2)
    check("  -- and still does not take the decision",
          "DECISION IS STILL NOT TAKEN" in out2)
    check("  -- and lists what it does not count",
          "WHAT IS NOT COUNTED" in out2)

    print()
    print(f"selftest: {fail} failures -> {'PASS' if fail == 0 else 'FAIL'}")
    return 1 if fail else 0


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--selftest", action="store_true")
    ap.add_argument("--removal", action="store_true",
                    help="what online fission-product removal is worth")
    a = ap.parse_args()
    if a.selftest:
        return selftest()
    if a.removal:
        return report_removal()
    return report()


if __name__ == "__main__":
    sys.exit(main())
