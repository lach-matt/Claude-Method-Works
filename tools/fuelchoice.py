#!/usr/bin/env python3
"""fuelchoice.py -- what fissile fraction, what fertile fuel, and what it costs
the environment to choose either.

WHY THIS FILE EXISTS
--------------------
Three questions were asked together and they are one question, because the
answers are coupled: the fissile fraction sets k, k sets the breeding a fuel
must sustain, and which fertile fuel can sustain it decides what the plant
holds and therefore what it must mitigate.

Before this file, the repository asserted BOTH ENDS of the first question and
connected them by nothing:

    powersource.K_SAFE          = 0.95          the subcritical operating point
    powersource.FISSILE_FRACTION = (0.12, 0.20)  ASSUMED band

Those two are not independent. For a given geometry and chemistry the fissile
fraction DETERMINES k, and no file here computed the relation. Asking which
fraction is best is what exposed that, and this file supplies the missing link:
a one-group fast-spectrum neutronics model, inverted for the fraction that
reaches the operating point.

WHAT THE MODEL IS, AND WHAT IT IS NOT
-------------------------------------
One-group. Each nuclide carries a spectrum-averaged fast cross section, and
k_inf = nu.Sigma_f / Sigma_a with leakage applied afterwards. That is the
standard first estimate and it is honest about what it buys:

  IT IS RELIABLE FOR  ordering, trends, and the sign of a comparison -- which
                      fuel needs more fissile, which direction f moves k.
  IT IS NOT RELIABLE FOR  an absolute k to better than roughly fifteen
                      percent. A transport calculation with a real spectrum
                      would move every number here and would not move any
                      conclusion, which is why the conclusions are stated as
                      requirements and the numbers as estimates.

Self-shielding, resonance structure and spectrum hardening with fissile
fraction are all omitted, and each is named where it would bite.

    python3 tools/fuelchoice.py
    python3 tools/fuelchoice.py --selftest
stdlib only.
"""
import argparse
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "tools"))


def _ps():
    import powersource as P
    return P


def _mat():
    import materials as M
    return M


# ---- the salt, derived from stoichiometry rather than asserted --------------
# A chloride salt is NaCl-UCl3. Fixing the mol fraction of UCl3 fixes every
# mass in it, and that is how this file gets its atom densities -- a neutronics
# model cannot run on a composition that does not balance charge.
A = {"U": 238.0, "Pu": 239.0, "Th": 232.0, "Cl": 35.45, "Na": 23.0}
EUTECTIC_MOL_UCL3 = 0.34     # SOURCED band 0.28-0.36, NaCl-UCl3 eutectic


def salt_from_mol_fraction(x):
    """(U, Cl, Na) mass fractions of a NaCl-UCl3 salt at mol fraction x."""
    if not 0.0 < x < 1.0:
        raise ValueError(f"mol fraction must lie in (0,1), got {x}")
    mu = A["U"] * x
    mcl = A["Cl"] * (3.0 * x + (1.0 - x))
    mna = A["Na"] * (1.0 - x)
    tot = mu + mcl + mna
    return mu / tot, mcl / tot, mna / tot


def mol_fraction_for_u_mass(target):
    """Invert the above: what mol fraction gives this U mass fraction."""
    lo, hi = 1e-9, 1.0 - 1e-9
    for _ in range(300):
        mid = 0.5 * (lo + hi)
        if salt_from_mol_fraction(mid)[0] < target:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


def atom_ratios(x):
    """Atoms per heavy-metal atom, at mol fraction x. Cl and Na are the
    absorbers the fissile has to outcompete."""
    return {"HM": 1.0, "Cl": (3.0 * x + (1.0 - x)) / x, "Na": (1.0 - x) / x}


# ---- one-group fast cross sections -----------------------------------------
# Spectrum-averaged, barns. Every one is SOURCED as a band and the mid is used;
# the selftest asserts the ORDERING these imply rather than the values, because
# the ordering is what survives a better spectrum and the values do not.
XS = {                       # (sigma_fission, sigma_capture, nu)
    "Pu239": (1.80, 0.55, 2.90),   # the U/Pu cycle's fissile
    "U235":  (1.25, 0.55, 2.60),
    "U233":  (2.75, 0.28, 2.50),   # the Th cycle's fissile
    "U238":  (0.045, 0.29, 2.50),  # fertile: threshold fission only
    "Th232": (0.010, 0.36, 2.40),  # fertile: no threshold fission worth counting
    "Cl":    (0.0, 0.004, 0.0),    # Cl-37; Cl-35 is why it is enriched
    "Na":    (0.0, 0.0015, 0.0),
    # ADDED FOR THE BENCHMARK BELOW and for nothing else. The design's salt
    # holds neither, but the one published fast-molten-salt benchmark with a
    # two-code Monte Carlo k is a FLUORIDE, and a model that cannot be run on
    # the only benchmark available cannot be checked at all.
    "F":     (0.0, 0.010, 0.0),    # SOURCED band: F-19 fast capture is small
    "Li7":   (0.0, 0.001, 0.0),    # SOURCED band: Li-7, and MSFR enriches to
}                                  # avoid Li-6 for exactly this reason

CYCLES = {
    "U-Pu   uranium fertile, Pu-239 fissile": ("Pu239", "U238"),
    "Th-U   thorium fertile, U-233 fissile": ("U233", "Th232"),
}


def k_infinity(f, fissile, fertile, x=None, carriers=None):
    """k_inf for a heavy metal that is fraction f fissile, rest fertile.

    `carriers` is {nuclide: atoms per heavy-metal atom} and overrides the
    chloride salt's own Cl and Na. It exists so the model can be run on the
    published fluoride benchmark -- a model that cannot be run on the only
    benchmark available cannot be checked at all."""
    if not 0.0 <= f <= 1.0:
        raise ValueError(f"fissile fraction must lie in [0,1], got {f}")
    if carriers is None:
        x = EUTECTIC_MOL_UCL3 if x is None else x
        r = atom_ratios(x)
        carriers = {"Cl": r["Cl"], "Na": r["Na"]}
    sf_a, sc_a, nu_a = XS[fissile]
    sf_b, sc_b, nu_b = XS[fertile]
    prod = f * sf_a * nu_a + (1.0 - f) * sf_b * nu_b
    absorb = f * (sf_a + sc_a) + (1.0 - f) * (sf_b + sc_b)
    for nuc, n in carriers.items():
        if nuc not in XS:
            raise ValueError(f"no cross section for carrier {nuc!r}")
        absorb += n * XS[nuc][1]
    return prod / absorb


# ---- THE BENCHMARK, AND THE MEASUREMENT IT MAKES OF THIS FILE'S OWN MODEL --
# This file says of itself that one-group is "not reliable for an absolute k
# to better than roughly fifteen percent". THAT WAS AN ASSERTION. explore.py
# then made it load-bearing -- the design's whole k margin against
# non-existence turned out to equal that fifteen percent -- and
# powersource --efficiency closed the escape route beside it. So the number
# had to stop being an assertion.
#
# There is one published benchmark of a FAST MOLTEN SALT with a k computed by
# two independent Monte Carlo codes on evaluated data. It is a fluoride and a
# thorium cycle, which is not this design's salt or its fuel -- and it is what
# exists.
MSFR = {                          # SOURCED: SAMOFAR/EVOL reference
    "mol_LiF": 77.5, "mol_ThF4": 20.0, "mol_UF4": 2.5,
    "k_openmc": 1.04364, "k_openmc_sd": 0.00039,
    "k_serpent": 1.04338, "k_serpent_sd": 0.00075,
    "library": "ENDF/B-VIII.0",
    "note": "3000 MWth, 18 m3 fuel circuit, cylindrical core 2.25 m x 2.25 m, "
            "fertile LiF-ThF4 blanket, B4C, HT9 reflector, 973 K",
}


def msfr_composition():
    """(fissile fraction of heavy metal, carriers per heavy-metal atom)."""
    hm = MSFR["mol_ThF4"] + MSFR["mol_UF4"]
    f = MSFR["mol_UF4"] / hm
    fluorine = (MSFR["mol_LiF"] + 4.0 * MSFR["mol_ThF4"]
                + 4.0 * MSFR["mol_UF4"]) / hm
    lithium = MSFR["mol_LiF"] / hm
    return f, {"F": fluorine, "Li7": lithium}


def msfr_k_infinity():
    f, carriers = msfr_composition()
    return k_infinity(f, "U233", "Th232", carriers=carriers)


def msfr_benchmark_k():
    """The two codes agree; their mean is the figure to compare against."""
    return 0.5 * (MSFR["k_openmc"] + MSFR["k_serpent"])


def msfr_error_band():
    """(most favourable, least favourable) fractional error of this model.

    THE COMPARISON IS BETWEEN TWO DIFFERENT QUANTITIES and that is the whole
    difficulty. The model returns the fuel salt's k_inf; the benchmark returns
    the whole system's k_eff, which is lower by whatever the blanket captures
    and the boundary leaks. The paper does not break that budget out, so the
    error is BOUNDED rather than pinned: at zero loss the model is high by the
    difference, and at a loss as large as the benchmark's own fertile blanket
    plausibly takes it is low by more."""
    k_model = msfr_k_infinity()
    k_bench = msfr_benchmark_k()
    high = k_model / k_bench - 1.0                 # if the system loses nothing
    low = k_model / (k_bench / (1.0 - MSFR_LOSS_HI)) - 1.0
    return high, low


MSFR_LOSS_HI = 0.08     # ASSUMED: an upper estimate of what the benchmark's
                        # fertile blanket captures plus what its boundary
                        # leaks, as a share of the neutron budget. The paper
                        # does not state it, so the error band is opened by it
                        # rather than closed

# ---- AND THE FLUORIDE CHECK IS WITHDRAWN AS A VALIDATION ------------------
# The run above stands as arithmetic and is kept. WHAT IS WITHDRAWN IS ITS
# STANDING: it was used, for one pass, to replace this file's asserted
# fifteen percent with a measured seven, and the design basis was restated on
# it. That was wrong, on a rule the author stated plainly:
#
#     DO NOT TEST ON A MATERIAL YOU DO NOT INTEND TO USE.
#
# The benchmark is a FLUORIDE salt on a THORIUM cycle with U-233 fissile. The
# design is a CHLORIDE salt on a URANIUM cycle with Pu-239 fissile. It shares
# with the design neither halide, nor fertile, nor fissile nuclide -- only
# the shape of the problem. A model can agree on one material and disagree on
# another for reasons that have nothing to do with its method, and a design
# basis rested on that agreement is resting on a coincidence it cannot check.
#
# So the seven percent is withdrawn and the fifteen stands as ASSERTED, which
# is where it was before. What replaces the check is not another check: it is
# the STATE OF KNOWLEDGE ON THE ACTUAL MATERIAL, which is worse than the
# fluoride excursion made it look and is sourced.
BENCHMARK_WITHDRAWN = (
    "the SAMOFAR/EVOL benchmark is a fluoride salt on a thorium cycle and "
    "shares with this design neither halide, nor fertile, nor fissile "
    "nuclide; a validation on a material the design does not use is not a "
    "validation of the design")

# ---- WHAT IS KNOWN ABOUT THE MATERIAL THIS DESIGN ACTUALLY USES -----------
# All SOURCED, and all about a fast CHLORIDE salt.
MCRE = {
    "what": "Molten Chloride Reactor Experiment -- the first critical "
            "fast-spectrum chloride-salt reactor, under construction by "
            "Southern Company, TerraPower and Idaho National Laboratory",
    "nd_uncertainty_pcm": 2161.0,      # SOURCED: nuclear-data-induced
    "nd_after_pcm": 886.0,             # SOURCED: after the proposed
                                       # criticality experiments
    "cl35": "recent measurements of the Cl-35 (n,p) cross section disagree "
            "with the evaluations OUTSIDE the bounds of their own covariance "
            "matrices; Los Alamos has been charged with re-measuring it and "
            "issuing a new evaluation",
}


def mcre_nd_uncertainty_k(after=False):
    """Nuclear-data-induced uncertainty in k for a fast chloride salt.

    A TRANSPORT-CODE figure with a full covariance treatment: it is what
    remains when the METHOD is exact and only the data are uncertain. This
    file's model is one-group, so this term sits UNDER its method error and
    never replaces it."""
    pcm = MCRE["nd_after_pcm"] if after else MCRE["nd_uncertainty_pcm"]
    return pcm / 1e5


def k_effective(f, fissile, fertile, leak=None, x=None):
    P = _ps()
    leak = P.LEAK_PARASITIC_LO if leak is None else leak
    return k_infinity(f, fissile, fertile, x) * (1.0 - leak)


def fraction_for_k(k_target, fissile, fertile, leak=None, x=None):
    """The fissile fraction that reaches k_target. None if unreachable."""
    lo, hi = 0.0, 1.0
    if k_effective(hi, fissile, fertile, leak, x) < k_target:
        return None
    for _ in range(300):
        mid = 0.5 * (lo + hi)
        if k_effective(mid, fissile, fertile, leak, x) < k_target:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


# ---- what a fraction costs and buys -----------------------------------------
def charge_and_gain(f, fissile, fertile, leak=None):
    """(k_eff, plant gain, fissile first charge in tonnes) at fraction f."""
    P, M = _ps(), _mat()
    k = min(k_effective(f, fissile, fertile, leak), 0.999)
    r = M.ref()
    g = P.plant_gain(k, r["y_spall"], r["y_fus"])
    charge_t = M.heavy_metal_inventory_kg() * f / 1000.0
    return k, g, charge_t


def loop_floor(fissile="Pu239", fertile="U238", leak=None, target=7.41):
    """The least fissile fraction at which the closed loop still closes."""
    P = _ps()
    leak = P.LEAK_PARASITIC_LO if leak is None else leak
    lo, hi = 1e-4, 1.0
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        if charge_and_gain(mid, fissile, fertile, leak)[1] < target:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


def breeding_required(k, nu):
    """f_b = k/(nu-k): the share of non-fission absorptions that must breed."""
    return k / (nu - k)


def report_benchmark():
    """the one-group model, checked against a two-code Monte Carlo benchmark"""
    P = _ps()
    print()
    print("  THE MODEL, CHECKED AGAINST A BENCHMARK")
    print()
    print("    This file says of itself that one-group is 'not reliable for")
    print("    an absolute k to better than roughly fifteen percent'. THAT")
    print("    WAS AN ASSERTION, and it became load-bearing: explore.py found")
    print("    the design's whole margin against non-existence EQUALS that")
    print("    fifteen percent, and powersource --efficiency then closed the")
    print("    escape route beside it. So the number had to stop being an")
    print("    assertion.")
    print()
    print("    THERE IS ONE BENCHMARK AND IT IS NOT THIS SALT.")
    print()
    print(f"      SAMOFAR / EVOL Molten Salt Fast Reactor")
    print(f"        fuel        LiF-ThF4-UF4 at"
          f" {MSFR['mol_LiF']:.1f} / {MSFR['mol_ThF4']:.1f} /"
          f" {MSFR['mol_UF4']:.1f} mol %")
    print(f"        k_eff       {MSFR['k_openmc']:.5f} +/-"
          f" {MSFR['k_openmc_sd']:.5f}   OpenMC")
    print(f"                    {MSFR['k_serpent']:.5f} +/-"
          f" {MSFR['k_serpent_sd']:.5f}   Serpent 2")
    print(f"        library     {MSFR['library']}")
    print(f"        geometry    {MSFR['note']}")
    print()
    print("      TWO INDEPENDENT MONTE CARLO CODES ON EVALUATED DATA, AGREEING")
    print(f"      TO {abs(MSFR['k_openmc'] - MSFR['k_serpent']) * 1e5:.0f} PCM."
          " That is what makes it a benchmark rather than a")
    print("      result. It is a FLUORIDE and a THORIUM cycle -- neither this")
    print("      design's salt nor its fuel -- and it is what exists.")
    print()
    f, carriers = msfr_composition()
    print("    RUNNING THIS FILE'S MODEL ON IT")
    print()
    print(f"      fissile fraction of heavy metal   {100 * f:.2f} %")
    print(f"      fluorine per heavy-metal atom     {carriers['F']:.3f}")
    print(f"      lithium per heavy-metal atom      {carriers['Li7']:.3f}")
    print(f"      one-group k_inf                   {msfr_k_infinity():.4f}")
    print(f"      benchmark k_eff                   {msfr_benchmark_k():.4f}")
    print()
    hi, lo = msfr_error_band()
    print("    AND THE COMPARISON IS BETWEEN TWO DIFFERENT QUANTITIES, WHICH")
    print("    IS THE WHOLE DIFFICULTY. The model returns the fuel salt's")
    print("    k_inf; the benchmark returns the whole system's k_eff, lower by")
    print("    whatever its fertile blanket captures and its boundary leaks.")
    print("    The paper does not break that budget out. So the error is")
    print("    BOUNDED rather than pinned:")
    print()
    print(f"      if the benchmark system lost nothing    model is"
          f" {100 * hi:+.2f} %")
    print(f"      if it loses {100 * MSFR_LOSS_HI:.0f} % to blanket and leakage"
          f"    model is {100 * lo:+.2f} %")
    print()
    print("    AND ALL OF THAT IS NOW WITHDRAWN AS A VALIDATION, ON A RULE")
    print("    THE AUTHOR STATED PLAINLY: DO NOT TEST ON A MATERIAL YOU DO")
    print("    NOT INTEND TO USE.")
    print()
    _wrap(BENCHMARK_WITHDRAWN)
    print()
    print("    The arithmetic above stands and is kept. WHAT IS WITHDRAWN IS")
    print("    ITS STANDING. For one pass it replaced this file's asserted")
    print("    fifteen percent with a measured seven and the design basis was")
    print("    restated on it. A model can agree on one material and disagree")
    print("    on another for reasons that have nothing to do with its")
    print("    method, and a design basis rested on that agreement is resting")
    print("    on a coincidence it cannot check. THE FIFTEEN PERCENT STANDS,")
    print("    ASSERTED, WHICH IS WHERE IT WAS.")
    print()
    print("    WHAT REPLACES THE CHECK IS NOT ANOTHER CHECK. It is the state")
    print("    of knowledge on the actual material, and it is worse than the")
    print("    fluoride excursion made it look.")
    print()
    print("      THERE IS NO CRITICAL BENCHMARK FOR A FAST CHLORIDE SALT.")
    _wrap(MCRE["what"])
    print("      IS BEING BUILT TO MAKE ONE. It has not run.")
    print()
    print(f"      nuclear-data uncertainty in k_eff   "
          f"{MCRE['nd_uncertainty_pcm']:.0f} pcm ="
          f" {mcre_nd_uncertainty_k():.5f} in k")
    print(f"      after the proposed experiments      "
          f"{MCRE['nd_after_pcm']:.0f} pcm ="
          f" {mcre_nd_uncertainty_k(after=True):.5f}")
    print()
    print("      AND THE DATA ARE KNOWN TO BE WRONG, NOT MERELY UNCERTAIN:")
    _wrap(MCRE["cl35"])
    print()
    print("    ONE THING IN THAT RUNS THE DESIGN'S WAY, AND IT WAS CHOSEN FOR")
    print("    ANOTHER REASON ENTIRELY. The nuclide whose data are discrepant")
    print("    is Cl-35, and this design's salt is Cl-37 ENRICHED -- specified")
    print("    that way to stop parasitic absorption, long before anyone here")
    print("    knew Cl-35 carried the largest nuclear-data uncertainty in the")
    print("    material. The enrichment removes most of the offending nuclide")
    print("    and therefore most of that term. THAT IS A MITIGATION THIS")
    print("    WORK GOT FOR FREE AND SHOULD NOT TAKE CREDIT FOR DESIGNING.")
    print()
    print("    SO THE DESIGN BASIS, RESTORED AND STATED ON THE RIGHT")
    print("    MATERIAL:")
    print()
    sys.path.insert(0, os.path.join(ROOT, "tools"))
    import explore as E
    unc = E.K_MODEL_UNCERTAINTY * P.K_DESIGN
    nd = mcre_nd_uncertainty_k() * P.K_DESIGN / P.K_DESIGN
    print(f"      one-group METHOD error, ASSERTED       {unc:.4f} in k")
    print(f"      nuclear data on a chloride, SOURCED    "
          f"{mcre_nd_uncertainty_k():.4f} in k")
    print("      the two are different terms and the second sits UNDER the")
    print("      first: it is what remains when the method is exact.")
    print()
    print("      eta_acc   margin at "
          f"{P.K_DESIGN:.3f}   vs method   vs nuclear data")
    for e, lab in ((0.20, "every machine measured"),
                   (0.30, "the design's assumption"),
                   (0.40, "a better machine")):
        m = P.K_DESIGN - E.k_floor(e)
        print(f"      {e:6.2f} {m:14.4f} {m / unc:11.2f}x"
              f" {m / mcre_nd_uncertainty_k():15.2f}x   {lab}")
    print()
    print("    THE NUCLEAR DATA ARE NOT THE PROBLEM -- the margin covers them")
    print(f"    {(P.K_DESIGN - E.k_floor(0.30)) / mcre_nd_uncertainty_k():.1f}"
          " times over at the design's own accelerator, and would still cover")
    print("    them at the efficiency every machine has actually returned.")
    print("    THE METHOD IS THE PROBLEM, and it is still asserted.")
    print()
    print("    SO THE GATE IS EXACTLY WHERE IT WAS BEFORE THIS EXCURSION, AND")
    print("    IT IS NOW PRECISELY NAMED. What is open is the one-group")
    print("    method error ON THIS COMPOSITION, and what closes it is a")
    print("    TRANSPORT CALCULATION ON THIS SALT -- a computation, not an")
    print("    experiment, and a day's work for anyone with Serpent or MCNP")
    print("    and an evaluated library. It is the last uncertainty in the")
    print("    project and it is a concrete, nameable, deliverable ask.")
    print()


def report():
    P, M = _ps(), _mat()
    print()
    print("  WHAT FRACTION, WHAT FERTILE FUEL, AND WHAT IT COSTS TO MITIGATE")
    print()
    print("  0. A COMPOSITION THAT DID NOT BALANCE, FOUND ON THE WAY IN")
    print()
    implied = mol_fraction_for_u_mass(M.SALT_U_MASS_FRAC)
    uf, clf, naf = salt_from_mol_fraction(implied)
    salt_t = M.salt_inventory_kg() / 1000.0
    print(f"     materials.py sets the salt at {100*M.SALT_U_MASS_FRAC:.0f} %"
          " uranium by mass and calls it")
    print(f"     'near the eutectic'. Stoichiometry says that mass fraction is")
    print(f"     {100*implied:.1f} mol % UCl3, and the eutectic is near"
          f" {100*EUTECTIC_MOL_UCL3:.0f} mol %, which is")
    print(f"     {100*salt_from_mol_fraction(EUTECTIC_MOL_UCL3)[0]:.0f} %"
          " uranium by mass. THE DESIGN IS NOT AT THE EUTECTIC.")
    print()
    print(f"     It also carries {183.632:.1f} t of chlorine, computed as the"
          " chlorine in the")
    print("     NaCl portion alone. The chlorine bound to the uranium in UCl3")
    print(f"     is not in that figure. Stoichiometrically the salt holds"
          f" {salt_t*clf:.0f} t,")
    print(f"     which is {salt_t*clf/183.632:.2f} times what is carried --"
          " and every tonne of it")
    print("     must be Cl-37, because Cl-35 is what the enrichment is for.")
    print("     RECORDED, NOT REPAIRED: it is materials.py's row to fix, and it")
    print("     raises startcost.py's separation term with it.")
    print()
    print("     Both findings run the same way as restart.py's: off the")
    print("     eutectic the liquidus is HIGHER, so the cold leg that already")
    print("     froze freezes harder.")
    print()
    print("  1. THE FISSILE FRACTION IS NOT A FREE PARAMETER")
    print()
    print("     k = 0.95 is chosen for stability -- a fast core's whole control")
    print("     worth of margin. Given the chemistry and the leakage, that")
    print("     CHOOSES the fissile fraction; it is not separately available.")
    print()
    print("       cycle                                    f at k = 0.95")
    print("                                            leak 0.10   leak 0.20")
    for name, (fis, fer) in CYCLES.items():
        f_lo = fraction_for_k(P.K_SAFE, fis, fer, P.LEAK_PARASITIC_LO)
        f_hi = fraction_for_k(P.K_SAFE, fis, fer, P.LEAK_PARASITIC_HI)
        s_lo = "unreachable" if f_lo is None else f"{100*f_lo:8.1f} %"
        s_hi = "unreachable" if f_hi is None else f"{100*f_hi:8.1f} %"
        print(f"       {name:<38}{s_lo}  {s_hi}")
    print()
    band = P.FISSILE_FRACTION
    f_ref = fraction_for_k(P.K_SAFE, "Pu239", "U238", P.LEAK_PARASITIC_LO)
    f_hi = fraction_for_k(P.K_SAFE, "Pu239", "U238", P.LEAK_PARASITIC_HI)
    print(f"     The design carries {100*band[0]:.0f}-{100*band[1]:.0f} % as an"
          " ASSUMED band, and this is the")
    print("     first check it has ever had. IT DOES NOT PASS. On this model")
    print(f"     the U-Pu cycle reaches k=0.95 at {100*f_ref:.1f} %"
          f" to {100*f_hi:.1f} % across the")
    print(f"     leakage band -- BELOW the assumed floor of"
          f" {100*band[0]:.0f} %. At that floor the")
    print(f"     model gives k ="
          f" {k_effective(band[0], 'Pu239', 'U238', P.LEAK_PARASITIC_LO):.3f},"
          " which is past the margin the")
    print("     stability case is built on.")
    print()
    print("     STATED AS A REQUIREMENT AND NOT AS A REFUTATION. A one-group")
    print("     model is worth about fifteen percent on an absolute k and the")
    print("     gap here is larger than that, so the finding is real -- but")
    print("     what it establishes is that THE BAND WAS NEVER DERIVED, not")
    print("     that 8.9 % is the right answer. A transport calculation is")
    print("     what settles it, and until one runs, every figure that depends")
    print("     on the fissile charge carries this.")
    print()
    print("  2. WHAT MOVING THE FRACTION DOES, AND WHY HIGHER IS NOT BETTER")
    print()
    print("       f        k_eff      gain    first charge   verdict")
    for f in (0.03, 0.04, 0.05, 0.07, f_ref, 0.12, 0.20):
        k, g, ch = charge_and_gain(f, "Pu239", "U238", P.LEAK_PARASITIC_LO)
        raw = k_effective(f, "Pu239", "U238", P.LEAK_PARASITIC_LO)
        if raw >= 1.0:
            v, gs = "FORBIDDEN -- critical", "       --"
        elif raw > P.K_SAFE + 1e-9:
            v, gs = "forbidden -- margin lost", f"{g:9.1f}"
        elif abs(raw - P.K_SAFE) <= 1e-9:
            v, gs = "THE CEILING -- k = 0.95 exactly", f"{g:9.1f}"
        elif g < 7.41:
            v, gs = "loop does not close", f"{g:9.1f}"
        else:
            v, gs = "runs", f"{g:9.1f}"
        print(f"       {100*f:4.1f} %  {raw:7.3f} {gs} {ch:11.1f} t   {v}")
    lf = loop_floor()
    print()
    print(f"     THE WINDOW IS {100*lf:.1f} % TO {100*f_ref:.1f} %, and it is"
          " narrow. Below the floor")
    print("     the loop stops closing; above the ceiling the margin is gone.")
    print("     The gain column diverges as k approaches one, which is the")
    print("     subcritical multiplication doing what it does and not a")
    print("     result -- it is why the ceiling is a hard one.")
    print()
    print("     BEST IS THE LARGEST f THAT KEEPS THE MARGIN, AND NOTHING MORE.")
    print("     Above it the assembly goes critical and the whole safety case")
    print("     -- cut the beam and it stops -- is gone. Below it the gain")
    print("     falls and the loop stops closing. There is no optimum in the")
    print("     interior: the criterion picks the boundary.")
    print()
    print("  3. WHICH FERTILE FUEL, AMONG WHAT IS ABUNDANT")
    print()
    print("       fuel              station-lifetimes   nu     f_b required")
    rows = [
        ("enrichment tails", 31365, "U238", 2.90),
        ("spent LWR fuel", 7841, "U238", 2.90),
        ("natural uranium", 156825, "U238", 2.90),
        ("thorium", 125460, "Th232", 2.50),
        ("seawater uranium", 88000000, "U238", 2.90),
    ]
    for label, life, fer, nu in rows:
        fb = breeding_required(P.K_SAFE, nu)
        print(f"       {label:<20} {life:>12,}   {nu:.2f}   {fb:11.4f}")
    print()
    print("     The first three and the fifth are the SAME FUEL -- U-238 with")
    print("     different amounts of U-235 attached, and different provenance.")
    print("     Only thorium is a different cycle, and it costs twice: its")
    print(f"     nu is {2.50:.2f} against {2.90:.2f}, so fission takes more of the")
    print(f"     budget AND f_b rises from {breeding_required(P.K_SAFE, 2.90):.4f}"
          f" to {breeding_required(P.K_SAFE, 2.50):.4f}.")
    print()
    f_th = fraction_for_k(P.K_SAFE, "U233", "Th232", P.LEAK_PARASITIC_LO)
    f_up = fraction_for_k(P.K_SAFE, "Pu239", "U238", P.LEAK_PARASITIC_LO)
    print("     AND THE FRACTION RUNS THE SAME WAY, WHICH THIS FILE EXPECTED")
    print("     IT NOT TO. U-233 is the better nuclide -- it fissions"
          f" {XS['U233'][0]/XS['U233'][1]:.1f} times")
    print(f"     per capture against Pu-239's"
          f" {XS['Pu239'][0]/XS['Pu239'][1]:.1f} -- so the thorium cycle looked")
    print(f"     like it should need less fissile. It needs MORE:"
          f" {100*f_th:.1f} % against")
    print(f"     {100*f_up:.1f} %. Th-232 captures"
          f" {XS['Th232'][1]/XS['U238'][1]:.2f} times as much as U-238 and its"
          " nu is")
    print(f"     {XS['U233'][2]:.2f} against {XS['Pu239'][2]:.2f}, and the"
          " system beats the nuclide.")
    print()
    print("     So thorium is worse on the fraction AND worse on the budget,")
    print("     where materials.py --fertile already had it closing at L=0.10")
    print("     and failing at L=0.20. Two independent counts, same direction.")
    print()
    print("  4. WHICH CHOICE COSTS THE LEAST MITIGATION")
    print()
    print("     environment.py grades 23 impacts twice, before and after. The")
    print("     fuel choice moves a small number of them and this file names")
    print("     which, rather than re-grading anything:")
    print()
    print("       row                        U-Pu            Th-U")
    print("       proliferation              MODERATE        arguably better:")
    print("                                  (Pu-239)        U-232 daughter's")
    print("                                                  hard gamma is")
    print("                                                  self-protecting")
    print("       fissions civil Pu          BENEFIT         LOST -- a thorium")
    print("                                  permanently     plant cannot burn")
    print("                                                  the stockpile")
    print("       fertile supply             tails: already  mined for the")
    print("                                  mined, a        purpose, a NEW")
    print("                                  liability       extraction stream")
    print("       neutron budget             closes at both  fails at L=0.20")
    print("                                  leakage ends")
    print()
    print("     SO THE LEAST-MITIGATION CHOICE IS URANIUM, AND THE REASON IS")
    print("     NOT NEUTRONIC. Thorium's proliferation advantage is real and")
    print("     it is outweighed by two things a fuel table does not show: the")
    print("     uranium route CONSUMES an existing waste that is guarded at")
    print("     cost for ever, and it opens no new mine. Thorium closes one")
    print("     environmental row and opens two.")
    print()
    print("     That is the same answer materials.py --fertile reached from the")
    print("     neutron budget alone, by a different route. Two independent")
    print("     arguments, one conclusion, and the decision already recorded.")
    print()


def selftest():
    fail = 0

    def check(label, got, want=True):
        nonlocal fail
        ok = got == want
        fail += 0 if ok else 1
        print(f"  {label:<62} {'PASS' if ok else 'FAIL'}")
        if not ok:
            print(f"      got {got!r} want {want!r}")

    P, M = _ps(), _mat()
    print()
    print("  the salt must balance before any neutronics runs on it")
    uf, clf, naf = salt_from_mol_fraction(0.34)
    check("the three mass fractions sum to one", abs(uf + clf + naf - 1.0) < 1e-12)
    check("more UCl3 means more uranium by mass",
          salt_from_mol_fraction(0.5)[0] > salt_from_mol_fraction(0.2)[0])
    check("the inversion round-trips",
          abs(salt_from_mol_fraction(mol_fraction_for_u_mass(0.40))[0] - 0.40) < 1e-9)
    check("a mol fraction outside (0,1) is refused",
          _raises(lambda: salt_from_mol_fraction(1.5)))
    # the finding: the design's own mass fraction is NOT the eutectic
    implied = mol_fraction_for_u_mass(M.SALT_U_MASS_FRAC)
    check("the design's 40 % U is well off the eutectic",
          abs(implied - EUTECTIC_MOL_UCL3) > 0.10)
    check("  -- and it is on the LEAN side, which raises the liquidus",
          implied < EUTECTIC_MOL_UCL3)
    check("stoichiometric chlorine exceeds the row materials.py carries",
          M.salt_inventory_kg() / 1000.0 * salt_from_mol_fraction(implied)[1]
          > 183.632)

    print()
    print("  the neutronics must behave like neutronics")
    check("k rises with fissile fraction",
          k_infinity(0.20, "Pu239", "U238") > k_infinity(0.10, "Pu239", "U238"))
    check("pure fertile cannot sustain a chain",
          k_infinity(0.0, "Pu239", "U238") < 1.0)
    check("pure fissile can", k_infinity(1.0, "Pu239", "U238") > 1.0)
    check("leakage lowers k_eff below k_inf",
          k_effective(0.15, "Pu239", "U238", 0.20)
          < k_infinity(0.15, "Pu239", "U238"))
    check("a fissile fraction outside [0,1] is refused",
          _raises(lambda: k_infinity(1.4, "Pu239", "U238")))
    # ORDERING, which is what a one-group model is actually good for. This
    # assertion was written the other way round and the model corrected it:
    # U-233 is the better NUCLIDE and the thorium CYCLE still needs more
    # fissile, because Th-232 captures more than U-238 and nu is lower. The
    # system beats the nuclide, and that is the finding.
    check("U-233 is the better nuclide, fission over capture",
          XS["U233"][0] / XS["U233"][1] > XS["Pu239"][0] / XS["Pu239"][1])
    check("  -- and the thorium CYCLE still needs MORE fissile, not less",
          fraction_for_k(0.95, "U233", "Th232", 0.10)
          > fraction_for_k(0.95, "Pu239", "U238", 0.10))
    check("  -- because the fertile captures more", XS["Th232"][1] > XS["U238"][1])
    check("  -- and nu is lower", XS["U233"][2] < XS["Pu239"][2])
    check("more leakage needs more fissile",
          fraction_for_k(0.95, "Pu239", "U238", 0.20)
          > fraction_for_k(0.95, "Pu239", "U238", 0.10))

    print()
    print("  the answer to the question, and it must be a boundary")
    f_ref = fraction_for_k(P.K_SAFE, "Pu239", "U238", P.LEAK_PARASITIC_LO)
    # AND THE MODEL DISAGREES WITH THE DESIGN'S ASSUMED BAND. This assertion
    # was written expecting agreement; the model puts the fraction BELOW the
    # band at both leakage ends, which means the band as assumed would carry
    # the assembly past its own margin. Recorded as a finding, not smoothed.
    check("the model's fraction is BELOW the design's ASSUMED band",
          f_ref < P.FISSILE_FRACTION[0])
    check("  -- at the loose leakage end too",
          fraction_for_k(P.K_SAFE, "Pu239", "U238", P.LEAK_PARASITIC_HI)
          < P.FISSILE_FRACTION[0])
    check("  -- so the band's own floor would exceed the margin",
          k_effective(P.FISSILE_FRACTION[0], "Pu239", "U238",
                      P.LEAK_PARASITIC_LO) > P.K_SAFE)
    check("far above it the assembly goes critical",
          k_effective(0.60, "Pu239", "U238", P.LEAK_PARASITIC_LO) > 1.0)
    check("well below it the loop stops closing",
          charge_and_gain(0.04, "Pu239", "U238", P.LEAK_PARASITIC_LO)[1] < 7.41)
    check("  -- so the workable window is a band, and a narrow one",
          0.0 < loop_floor() < f_ref)

    print()
    print("  breeding, and why thorium costs twice")
    check("f_b is higher for the lower nu",
          breeding_required(0.95, 2.50) > breeding_required(0.95, 2.90))
    check("  -- and both are real fractions of the budget",
          0.0 < breeding_required(0.95, 2.90) < 1.0)

    print()
    print("  the report states the findings rather than only computing them")
    out = _rendered()
    check("it says the design is not at the eutectic",
          "NOT AT THE EUTECTIC" in out)
    check("it records the chlorine row as unrepaired",
          "RECORDED, NOT REPAIRED" in out)
    check("it names uranium as the least-mitigation choice",
          "LEAST-MITIGATION CHOICE IS URANIUM" in out)
    check("it does not claim an interior optimum",
          "no optimum in the" in out)

    print()
    print("  the benchmark, and the measurement it makes of this model")
    _f, _car = msfr_composition()
    check("the benchmark composition is the published one",
          abs(_f - 2.5 / 22.5) < 1e-12)
    check("  -- and its carriers are stoichiometric",
          abs(_car["F"] - (77.5 + 4 * 22.5) / 22.5) < 1e-9)
    check("the two codes agree to within a hundred pcm",
          abs(MSFR["k_openmc"] - MSFR["k_serpent"]) < 1e-3)
    import io as _io
    import contextlib as _c
    import explore as _E
    _buf = _io.StringIO()
    with _c.redirect_stdout(_buf):
        report_benchmark()
    _b = _buf.getvalue()
    _hi, _lo = msfr_error_band()
    check("the model lands within ten percent of the benchmark either way",
          max(abs(_hi), abs(_lo)) < 0.10)
    check("a k_inf must exceed the k_eff of a leaking system",
          msfr_k_infinity() > msfr_benchmark_k())
    # AND THE WITHDRAWAL, which is the point of the section now. The rule is
    # the author's: do not test on a material you do not intend to use.
    check("the fluoride result is WITHDRAWN as a validation",
          "WITHDRAWN AS A VALIDATION" in _b)
    check("  -- on the stated rule, quoted",
          "DO NOT TEST ON A MATERIAL YOU DO" in _b)
    check("  -- and the asserted fifteen percent is restored, not replaced",
          "THE FIFTEEN PERCENT STANDS" in _b)
    check("  -- so nothing downstream uses the seven percent",
          "0.1350" in _b and "0.0688" not in _b)
    # THE ON-MATERIAL STATE OF KNOWLEDGE, which is what replaces it.
    check("the nuclear-data uncertainty on a chloride is sourced",
          0.01 < mcre_nd_uncertainty_k() < 0.05)
    check("  -- and falls after the experiment that has not run",
          mcre_nd_uncertainty_k(after=True) < mcre_nd_uncertainty_k())
    check("the margin covers the nuclear data at the design's accelerator",
          (_ps().K_DESIGN - _E.k_floor(0.30)) > 4.0 * mcre_nd_uncertainty_k())
    check("  -- and does NOT cover the asserted method error there",
          (_ps().K_DESIGN - _E.k_floor(0.30))
          < _E.K_MODEL_UNCERTAINTY * _ps().K_DESIGN)
    check("the report says there is no critical benchmark for this material",
          "NO CRITICAL BENCHMARK FOR A FAST CHLORIDE SALT" in _b)
    check("  -- and that the Cl-35 data are known WRONG, not just uncertain",
          "KNOWN TO BE WRONG" in _b)
    check("  -- and does not take credit for the Cl-37 mitigation",
          "SHOULD NOT TAKE CREDIT FOR DESIGNING" in _b)
    check("the remaining ask is named as a computation, not an experiment",
          "TRANSPORT CALCULATION ON THIS SALT" in _b
          and "a computation, not an" in _b)
    # AND WHAT IT DOES NOT COVER, asserted so it cannot be dropped.
    # THESE TWO USED TO CHECK THAT THE SECTION CAVEATED ITS VALIDATION --
    # that the U-Pu rows were untested and that the agreement was an argument
    # rather than a proof. The caveat is now moot: the whole result is
    # withdrawn, on a stronger rule than the caveat expressed, and what
    # replaces it is checked above.
    check("the withdrawal supersedes the caveats it used to carry",
          "an argument and not a proof" not in _b
          and "WITHDRAWN AS A VALIDATION" in _b)
    check("  -- and names the benchmark as neither this salt nor this fuel",
          "neither this" in _b and "design's salt nor its fuel" in _b)
    # THE CARRIER OVERRIDE, which is what let the model be run at all.
    check("the carrier override changes the answer",
          k_infinity(_f, "U233", "Th232", carriers=_car)
          != k_infinity(_f, "U233", "Th232"))
    check("  -- and the chloride path is unchanged by its existence",
          abs(k_infinity(0.10, "Pu239", "U238")
              - k_infinity(0.10, "Pu239", "U238",
                           carriers={"Cl": atom_ratios(EUTECTIC_MOL_UCL3)["Cl"],
                                     "Na": atom_ratios(EUTECTIC_MOL_UCL3)["Na"]}))
          < 1e-12)
    check("an unknown carrier nuclide is refused",
          _raises(lambda: k_infinity(0.1, "Pu239", "U238",
                                     carriers={"Xx": 1.0})))

    print()
    print(f"selftest: {fail} failures -> {'PASS' if not fail else 'FAIL'}")
    return 1 if fail else 0


def _wrap(text, indent="      ", width=66):
    import textwrap
    for line in textwrap.wrap(text, width=width):
        print(f"{indent}{line}")


def _raises(fn):
    try:
        fn()
        return False
    except ValueError:
        return True


def _rendered():
    import io
    import contextlib
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        report()
    return buf.getvalue()


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--selftest", action="store_true")
    ap.add_argument("--benchmark", action="store_true",
                    help=report_benchmark.__doc__)
    a = ap.parse_args()
    if a.selftest:
        return selftest()
    if a.benchmark:
        return report_benchmark()
    report()
    return 0


if __name__ == "__main__":
    sys.exit(main())
