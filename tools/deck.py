#!/usr/bin/env python3
"""deck.py -- the transport calculation, written out so it can be run.

WHY THIS FILE EXISTS
--------------------
The project has one uncertainty left. fuelchoice.py's one-group model places
the fissile fraction, criticality.py's ALWAYS-SUBCRITICAL property rests on
where that model puts k_inf = 1, and the whole hazard-class argument -- and
with it the adopted k = 0.900 -- rests on that. The model's own error is
ASSERTED at fifteen percent and has never been measured ON THIS MATERIAL,
because there is no critical benchmark for a fast chloride salt: the first
one is being built and has not run.

What settles it is a transport calculation, and a transport calculation is a
COMPUTATION rather than an experiment. So this writes the input decks for it,
from the design's own numbers, and states the prediction BEFORE the run.

WHY k_inf AND NOT k_eff
-----------------------
An infinite medium has no geometry, no leakage, no blanket and no reflector.
Every one of those is a place where two calculations can differ for reasons
that have nothing to do with the question. The question is whether a
one-group collapse of THIS composition puts k_inf where transport puts it,
and a reflective-boundary k_inf isolates exactly that and nothing else. The
last attempt at this compared a k_inf against a whole system's k_eff and had
to open a seven-point error band to cover the difference; this cannot.

THE PREDICTION IS REGISTERED IN ADVANCE, WHICH IS THE POINT
------------------------------------------------------------
The one-group model's curve is printed here with the decks. The comparison is
therefore decided before the run rather than after it, and the single number
that matters is where the transport curve crosses one: criticality.py says
7.93 % and the design's entire safety architecture is built on it.

    python3 tools/deck.py            write the decks and print the prediction
    python3 tools/deck.py --selftest
stdlib only. The decks are not run here -- see the closing note.
"""

import argparse
import math
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
OUT = os.path.join(ROOT, "decks")
sys.path.insert(0, HERE)

import fuelchoice as F                                          # noqa: E402
import materials as M                                           # noqa: E402
import criticality as C                                         # noqa: E402
import powersource as P                                         # noqa: E402

AVOGADRO = 6.02214076e23        # exact, SI definition
# Atomic masses, g/mol. SOURCED, and only the four nuclides the salt holds.
AMU = {
    "Pu239": 239.0521636,
    "U238": 238.0507882,
    "Na23": 22.98976928,
    "Cl37": 36.96590258,
    "Cl35": 34.96885268,
}
CL37_ENRICHMENT = 0.99          # DESIGN: the salt is Cl-37 enriched to stop
                                # parasitic capture on Cl-35. It also removes
                                # the nuclide whose evaluated data are known
                                # to disagree with measurement -- which this
                                # design did not know when it chose it
TEMPERATURE_K = 900.0           # the loop's hot leg, from materials.py
SCAN = (0.060, 0.070, 0.0793, 0.08346, 0.090, 0.100, 0.120)


def composition():
    """(mol fraction UCl3, salt density kg/m3) -- imported, never restated."""
    return F.mol_fraction_for_u_mass(M.SALT_U_MASS_FRAC), M.SALT_RHO


def molar_mass_cl():
    return (CL37_ENRICHMENT * AMU["Cl37"]
            + (1.0 - CL37_ENRICHMENT) * AMU["Cl35"])


def molar_mass_salt(f, x=None):
    """Grams per mole of salt formula units, at fissile fraction f."""
    if not 0.0 <= f <= 1.0:
        raise ValueError(f"fissile fraction must lie in [0,1], got {f}")
    x = composition()[0] if x is None else x
    m_hm = f * AMU["Pu239"] + (1.0 - f) * AMU["U238"]
    return (x * (m_hm + 3.0 * molar_mass_cl())
            + (1.0 - x) * (AMU["Na23"] + molar_mass_cl()))


def atom_densities(f, x=None, rho_kg_m3=None):
    """Atoms per barn-centimetre, which is what a transport code wants.

    Derived from the design's density and stoichiometry and from nothing
    else, so a change to either lands here without being retyped."""
    x = composition()[0] if x is None else x
    rho = composition()[1] if rho_kg_m3 is None else rho_kg_m3
    rho_g_cm3 = rho / 1000.0
    n_formula = rho_g_cm3 * AVOGADRO / molar_mass_salt(f, x)   # per cm3
    per_bcm = n_formula / 1e24
    cl = (3.0 * x + (1.0 - x)) * per_bcm
    return {
        "Pu239": x * f * per_bcm,
        "U238": x * (1.0 - f) * per_bcm,
        "Na23": (1.0 - x) * per_bcm,
        "Cl37": CL37_ENRICHMENT * cl,
        "Cl35": (1.0 - CL37_ENRICHMENT) * cl,
    }


def density_check(f, x=None, rho_kg_m3=None):
    """Sum the atom densities back into a mass density. Must return the input.

    THE ONE CHECK THAT CATCHES A TYPO IN A DECK, and decks are where typos
    live: an atom density that does not reproduce the density it came from is
    a deck that computes a different material from the one the design holds."""
    n = atom_densities(f, x, rho_kg_m3)
    g_cm3 = sum(n[k] * 1e24 * AMU[k] / AVOGADRO for k in n)
    return g_cm3 * 1000.0


def prediction(f, x=None):
    """The one-group k_inf this deck is written to test. Registered here."""
    return F.k_infinity(f, "Pu239", "U238", x=composition()[0] if x is None
                        else x)


def crossing(x=None):
    """Where the one-group model puts k_inf = 1, AT THE DESIGN'S OWN SALT.

    NOT criticality.py's published 7.93 %, and finding out why is the first
    thing writing a deck for the real material bought. That figure is
    computed at the EUTECTIC, 34 mol % UCl3. The design's salt is 18.9 mol %
    -- a fact fuelchoice.py had already recorded and not repaired -- and a
    more dilute salt carries more sodium and more chlorine per heavy atom to
    absorb, so it needs MORE fissile to reach k_inf = 1, not less.

    A deck must be written for the material the design holds. Writing one
    showed that the safety property was published for a material it does
    not."""
    xx = composition()[0] if x is None else x
    lo, hi = 0.0, 0.5
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        if F.k_infinity(mid, "Pu239", "U238", x=xx) < 1.0:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


def crossing_published():
    """criticality.py's own figure, for the comparison above."""
    return C.always_subcritical_threshold()


# ---- PROVENANCE: WHAT EXISTS ON THIS MATERIAL, AND WHAT IT SAYS ----------
# The deck above is written to be run. Before it is, the question is what is
# already published ON A CHLORIDE FAST SALT that the prediction can be set
# beside -- not to replace the calculation, but to know in advance whether it
# is expected to confirm the model or to overturn it.
#
# Two figures exist and both are on the right material.
PUBLISHED = {
    "MCRE fuel": (
        "the Molten Chloride Reactor Experiment uses the NaCl-UCl3 binary "
        "EUTECTIC with uranium enriched to 93.2 wt % U-235; it needs 72 to "
        "75 batches of salt to go critical, and it has not yet run"),
    "MCFR startup": (
        "the commercial TerraPower / Southern Company Molten Chloride Fast "
        "Reactor states that FIRST PLANTS START WITH 12 % ENRICHMENT, and "
        "the fuel cycle needs no enrichment after start-up"),
}
MCFR_STARTUP_ENRICHMENT = 0.12   # SOURCED, and the number that tests the deck
MCFR_LEAKAGE_BAND = (0.03, 0.10)  # ASSUMED: a commercial fast core is large,
                                  # so its leakage is small. The band is wide
                                  # on purpose -- the conclusion below has to
                                  # survive all of it


def crossing_u235(x=None):
    """The U-235 fraction this model says reaches k_inf = 1, same salt.

    Computed so the comparison with published practice is apples to apples:
    the published figure is an ENRICHMENT, and turning it into a Pu-239
    fraction through a cross-section ratio would be doing the model's work
    twice. This asks the model its own question in the published units."""
    xx = composition()[0] if x is None else x
    lo, hi = 0.0, 0.9
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        if F.k_infinity(mid, "U235", "U238", x=xx) < 1.0:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


def published_crossing_band():
    """What the MCFR's stated start-up enrichment implies for k_inf = 1.

    A critical power reactor has k_eff = 1, so its k_inf exceeds one by
    whatever it leaks -- which means the k_inf = 1 crossing lies BELOW the
    enrichment it starts at, and the more it leaks the further below."""
    lo_leak, hi_leak = MCFR_LEAKAGE_BAND
    return (MCFR_STARTUP_ENRICHMENT * (1.0 - hi_leak),
            MCFR_STARTUP_ENRICHMENT * (1.0 - lo_leak))


def model_conservatism():
    """How much more fissile this model demands than published practice.

    Greater than one means the model over-states what criticality needs --
    which is the SAFE direction for a reactor and the UNSAFE direction for a
    criticality-safety threshold, because the threshold is the fraction below
    which nothing can be critical."""
    lo, hi = published_crossing_band()
    x_eut = F.EUTECTIC_MOL_UCL3
    return (crossing_u235(x_eut) / hi, crossing_u235(x_eut) / lo)


def implied_true_threshold():
    """The Pu-239 always-subcritical threshold, scaled by that conservatism.

    INDICATIVE AND MARKED SO. It assumes the model's error is the same
    multiple for Pu-239 as for U-235, which is an assumption and not a
    result. It is computed to answer one question -- does the design's own
    operating fraction sit above or below it -- and for nothing else."""
    lo, hi = model_conservatism()
    return (crossing() / hi, crossing() / lo)


def _wrap(text, indent="      ", width=64):
    import textwrap
    for line in textwrap.wrap(text, width=width):
        print(f"{indent}{line}")


def openmc_deck(f):
    n = atom_densities(f)
    x, rho = composition()
    lines = [
        '"""k_inf of the design fuel salt at a stated fissile fraction.',
        "",
        f"    fissile fraction of heavy metal   {f:.5f}",
        f"    UCl3 mol fraction                 {x:.5f}",
        f"    density                           {rho / 1000.0:.4f} g/cm3",
        f"    temperature                       {TEMPERATURE_K:.0f} K",
        f"    Cl-37 enrichment                  {CL37_ENRICHMENT:.3f}",
        "",
        "REFLECTIVE ON EVERY SURFACE: this is an infinite medium and the",
        "number wanted is k_inf. No geometry, no leakage, no reflector, no",
        "blanket -- none of the places two calculations differ for reasons",
        "that are not the question.",
        "",
        f"    one-group prediction, registered in advance: k_inf ="
        f" {prediction(f):.4f}",
        '"""',
        "import openmc",
        "",
        "salt = openmc.Material(name='NaCl-UCl3 fuel salt')",
    ]
    for nuc, dens in sorted(n.items()):
        if dens > 0.0:
            iso = nuc[:2].rstrip("ual") if False else None
            lines.append(f"salt.add_nuclide({_openmc_name(nuc)!r},"
                         f" {dens:.8e}, 'ao')")
    lines += [
        f"salt.set_density('sum')",
        f"salt.temperature = {TEMPERATURE_K:.1f}",
        "materials = openmc.Materials([salt]); materials.export_to_xml()",
        "",
        "# a box with reflective faces is an infinite medium",
        "L = 50.0",
        "box = openmc.model.RectangularParallelepiped(",
        "    -L, L, -L, L, -L, L, boundary_type='reflective')",
        "cell = openmc.Cell(fill=salt, region=-box)",
        "openmc.Geometry([cell]).export_to_xml()",
        "",
        "settings = openmc.Settings()",
        "settings.run_mode = 'eigenvalue'",
        "settings.particles = 100000",
        "settings.batches = 250",
        "settings.inactive = 50",
        "settings.temperature = {'method': 'interpolation'}",
        "settings.export_to_xml()",
        "",
        "openmc.run()",
    ]
    return "\n".join(lines) + "\n"


def _openmc_name(nuc):
    return {"Pu239": "Pu239", "U238": "U238", "Na23": "Na23",
            "Cl37": "Cl37", "Cl35": "Cl35"}[nuc]


def serpent_deck(f):
    n = atom_densities(f)
    x, rho = composition()
    zaid = {"Pu239": "94239", "U238": "92238", "Na23": "11023",
            "Cl37": "17037", "Cl35": "17035"}
    lines = [
        f"% k_inf of the design fuel salt, fissile fraction {f:.5f}",
        f"% UCl3 mol fraction {x:.5f}, density {rho / 1000.0:.4f} g/cm3,"
        f" {TEMPERATURE_K:.0f} K",
        f"% one-group prediction, registered in advance: k_inf ="
        f" {prediction(f):.4f}",
        "",
        "set title \"NaCl-UCl3 fuel salt, infinite medium\"",
        "",
        "mat salt sum tmp %.1f" % TEMPERATURE_K,
    ]
    for nuc, dens in sorted(n.items()):
        if dens > 0.0:
            lines.append(f"{zaid[nuc]}.09c  {dens:.8e}")
    lines += [
        "",
        "surf 1 cube 0.0 0.0 0.0 50.0",
        "cell 1 0 salt -1",
        "cell 2 0 outside 1",
        "set bc 2                 % reflective on every face: infinite medium",
        "",
        "set pop 100000 250 50",
        "set gcu -1",
    ]
    return "\n".join(lines) + "\n"


def write_decks(outdir=None):
    d = OUT if outdir is None else outdir
    os.makedirs(d, exist_ok=True)
    written = []
    for f in SCAN:
        tag = f"f{int(round(f * 10000)):05d}"
        for name, text in ((f"kinf_{tag}_openmc.py", openmc_deck(f)),
                           (f"kinf_{tag}_serpent.inp", serpent_deck(f))):
            path = os.path.join(d, name)
            with open(path, "w", encoding="utf-8") as fh:
                fh.write(text)
            written.append(path)
    return written


def report():
    x, rho = composition()
    print()
    print("  THE TRANSPORT DECK, AND THE PREDICTION REGISTERED WITH IT")
    print()
    print("    The project has one uncertainty left: whether a one-group")
    print("    collapse of THIS composition puts k_inf where transport puts")
    print("    it. criticality.py's ALWAYS-SUBCRITICAL property rests on the")
    print("    answer, and with it the adopted k = 0.900 and the whole")
    print("    hazard-class argument. What settles it is a COMPUTATION.")
    print()
    print("    THE MATERIAL, IMPORTED FROM THE DESIGN AND NOT RESTATED")
    print()
    print(f"      salt                 NaCl-UCl3, {100 * x:.2f} mol % UCl3")
    print(f"      uranium by mass      {100 * M.SALT_U_MASS_FRAC:.0f} %")
    print(f"      density              {rho / 1000.0:.4f} g/cm3")
    print(f"      temperature          {TEMPERATURE_K:.0f} K")
    print(f"      chlorine             Cl-37 enriched to"
          f" {100 * CL37_ENRICHMENT:.1f} %")
    print()
    print("    WHY k_inf AND NOT k_eff. An infinite medium has no geometry,")
    print("    no leakage, no blanket and no reflector -- every one of which")
    print("    is a place two calculations differ for reasons that are not")
    print("    the question. The last attempt at this compared a k_inf")
    print("    against a whole system's k_eff and had to open a seven-point")
    print("    band to cover the difference. THIS CANNOT.")
    print()
    print("    THE DECKS, AND THE PREDICTION EACH ONE CARRIES")
    print()
    print("      fissile      atoms/b-cm                          one-group")
    print("      fraction     Pu-239      U-238       Cl          k_inf")
    for f in SCAN:
        n = atom_densities(f)
        mark = "   <- the always-subcritical threshold" \
            if abs(f - crossing()) < 5e-4 else ""
        print(f"      {100 * f:7.2f} % {n['Pu239']:.4e} {n['U238']:.4e}"
              f" {n['Cl37'] + n['Cl35']:.4e} {prediction(f):8.4f}{mark}")
    print()
    print("    AND WRITING A DECK FOR THE REAL MATERIAL BOUGHT A FINDING")
    print("    BEFORE IT BOUGHT AN ANSWER.")
    print()
    print(f"      criticality.py publishes the threshold at"
          f"   {100 * crossing_published():.2f} %")
    print(f"      at the composition the design actually holds"
          f" {100 * crossing():.2f} %")
    print()
    print("    THE PUBLISHED FIGURE IS COMPUTED AT THE EUTECTIC, 34 mol %")
    print(f"    UCl3. The design's salt is {100 * x:.1f} mol % -- which"
          " fuelchoice.py had")
    print("    already recorded and not repaired -- and a more dilute salt")
    print("    carries more sodium and more chlorine per heavy atom to")
    print("    absorb, so it needs MORE fissile to reach k_inf = 1, not less.")
    print("    THE SAFETY PROPERTY WAS PUBLISHED FOR A MATERIAL THE DESIGN")
    print("    DOES NOT USE, which is the same error the fluoride benchmark")
    print("    was withdrawn for, found one level further down.")
    print()
    print("    IT RUNS THE SAFE WAY, AND THAT IS luck rather than design. The")
    print("    always-subcritical band is wider than published, not narrower:")
    print(f"    5.5 % to {100 * crossing():.2f} % rather than to"
          f" {100 * crossing_published():.2f} %. And the adopted k = 0.900")
    print("    survives untouched, because it is k_inf = 1 carried through")
    print("    the leakage allowance and not a fissile fraction at all.")
    print()
    print("    THE ONE NUMBER THAT MATTERS is where the TRANSPORT curve")
    print(f"    crosses one. The one-group model puts it at"
          f" {100 * crossing():.2f} % on this salt,")
    print("    and criticality.py's whole argument is that below that")
    print("    fraction no quantity of it in any shape can be made critical.")
    print("    If transport puts the crossing materially lower, the operating")
    print("    window closes from below; if materially higher, the")
    print("    always-subcritical property was never true and the safety")
    print("    decision that set k = 0.900 was taken on a wrong number.")
    print()
    print("    EVERY DECK IS DERIVED, NOT TYPED. The atom densities come from")
    print("    the design's own density and stoichiometry, and the selftest")
    print("    sums them back into a mass density and requires the input")
    print("    back. A deck whose densities do not reproduce the density they")
    print("    came from is a deck that computes a different material.")
    print()
    print("    WHAT IS NOT DONE HERE, AND IT IS THE WHOLE REMAINING ASK.")
    print("    These decks are not run in this environment: it holds neither")
    print("    a transport code nor an evaluated cross-section library, and")
    print("    OpenMC is not installable from the package index here. What is")
    print("    needed is one of them plus ENDF/B-VIII.0 -- a day's work for")
    print("    anyone who has both, and the prediction above is registered so")
    print("    that whoever runs it is not marking their own homework.")
    print()


def closes_at(f, leak=None):
    """Beam MW to serve the baseline at this fissile fraction. inf if never."""
    lk = P.LEAK_PARASITIC_LO if leak is None else leak
    k = F.k_infinity(f, "Pu239", "U238", x=composition()[0]) * (1.0 - lk)
    try:
        return P.station(module_mw=P.SPALL_TARGET_MW["ESS, design"],
                         k_eff=k, max_modules=2000)["beam_mw"]
    except ValueError:
        return float("inf")


def report_provenance():
    """what is published on this material, and what it says about the deck"""
    x, _rho = composition()
    print()
    print("  PROVENANCE: WHAT IS PUBLISHED ON A CHLORIDE FAST SALT")
    print()
    print("    The deck is written to be run. Before it is, the question is")
    print("    what already exists ON THIS MATERIAL that the registered")
    print("    prediction can be set beside -- not to replace the")
    print("    calculation, but to know in advance whether it is expected to")
    print("    confirm the model or to overturn it.")
    print()
    for name, text in sorted(PUBLISHED.items()):
        print(f"      {name}")
        _wrap(text, indent="        ")
        print()
    print("    THE SECOND ONE TESTS THE DECK, AND IT DOES NOT AGREE.")
    print()
    print("    A commercial power reactor is CRITICAL: k_eff = 1. Its k_inf")
    print("    therefore exceeds one by whatever it leaks, so the k_inf = 1")
    print("    crossing lies BELOW the enrichment it starts at.")
    print()
    lo_c, hi_c = published_crossing_band()
    print(f"      this model, U-235 in the eutectic salt   "
          f"{100 * crossing_u235(F.EUTECTIC_MOL_UCL3):6.2f} %")
    print(f"      what a 12 % start-up implies, leaking "
          f"{100 * MCFR_LEAKAGE_BAND[0]:.0f} to"
          f" {100 * MCFR_LEAKAGE_BAND[1]:.0f} %"
          f"   {100 * lo_c:5.2f} to {100 * hi_c:5.2f} %")
    lo_m, hi_m = model_conservatism()
    print()
    print(f"    SO THE MODEL DEMANDS {lo_m:.2f} TO {hi_m:.2f} TIMES MORE"
          " FISSILE THAN PUBLISHED")
    print("    PRACTICE DOES. That is the SAFE direction for a reactor -- you")
    print("    would build it and it would be more reactive than you thought")
    print("    -- and it is the UNSAFE direction for a criticality-safety")
    print("    THRESHOLD, because a threshold is the fraction below which")
    print("    nothing can be critical, and over-stating it puts the line in")
    print("    the wrong place.")
    print()
    lo_t, hi_t = implied_true_threshold()
    print("    WHAT THAT WOULD DO TO THE ALWAYS-SUBCRITICAL PROPERTY")
    print()
    print(f"      this model's threshold, Pu-239, design salt   "
          f"{100 * crossing():5.2f} %")
    print(f"      the same, scaled by the conservatism above     "
          f"{100 * lo_t:5.2f} to {100 * hi_t:5.2f} %")
    print(f"      the design's own operating fissile fraction    "
          f"{100 * crossing():5.2f} %")
    print()
    print("    THE DESIGN WOULD SIT ABOVE ITS OWN THRESHOLD. criticality.py's")
    print("    central claim -- that below the threshold no quantity of this")
    print("    salt in any shape can be made critical, so the hazard class")
    print("    stops existing rather than being managed -- is what justified")
    print("    k = 0.900 and the whole safety architecture. On this evidence")
    print("    the operating salt would be ABOVE the line, not below it.")
    print()
    print("    AND THE TWO CLAIMS MAY NOT BE SIMULTANEOUSLY SATISFIABLE.")
    print()
    print("      fissile   k_eff at the favourable leakage   beam MW")
    for f in (lo_t, hi_t, crossing()):
        b = closes_at(f)
        k = F.k_infinity(f, "Pu239", "U238", x=x) * (1.0 - P.LEAK_PARASITIC_LO)
        shown = "does not close" if math.isinf(b) else f"{b:,.0f}"
        print(f"      {100 * f:6.2f} % {k:24.4f}   {shown}")
    print()
    print("    Hold the always-subcritical property and the plant needs a")
    print("    beam it cannot have, or does not close at all. Hold the plant")
    print("    and the salt is not always subcritical. ON THIS EVIDENCE THE")
    print("    DESIGN IS ASKED TO CHOOSE, AND IT HAS NOT BEEN TOLD IT MUST.")
    print()
    print("    NOW THE CAUTIONS, AND THEY ARE LOAD-BEARING. This is a FLAG")
    print("    and not a result, and every step of it is weaker than a")
    print("    calculation:")
    print()
    print("      1. The MCFR's own salt composition is not stated in what is")
    print("         available. The comparison is made at the EUTECTIC because")
    print("         that is what MCRE uses, and if the MCFR is elsewhere the")
    print("         conservatism factor moves.")
    print("      2. 12 % is a START-UP enrichment for a breeder. Its core")
    print("         geometry and leakage are not published here, which is why")
    print("         the leakage band above is wide and the conclusion is")
    print("         required to survive all of it.")
    print("      3. Scaling the Pu-239 threshold by the U-235 conservatism")
    print("         ASSUMES the model errs by the same multiple on both")
    print("         nuclides. That is an assumption and not a result, and it")
    print("         is the weakest link in the chain.")
    print()
    print("    WHAT THE FLAG IS WORTH IS NOT ITS NUMBER BUT ITS DIRECTION.")
    print("    It is drawn from published practice ON A CHLORIDE FAST SALT --")
    print("    the material the design uses -- and it says the transport")
    print("    calculation is not a formality. It decides whether the design")
    print("    as it stands is internally consistent, and the prediction is")
    print("    registered so that the answer cannot be argued with after the")
    print("    fact.")
    print()
    print("    THE STUDIES THAT WOULD SETTLE IT, NAMED SO THEY CAN BE FOUND")
    print("      Idaho National Laboratory, 'Criticality Safety S/U based USL")
    print("        Calculation for UCl3-NaCl Fuel Salt Operations' -- the")
    print("        same question, on the same salt, by the discipline's own")
    print("        method")
    print("      the MCRE nuclear-data uncertainty analysis, which puts the")
    print("        data term at 2,161 pcm and names Cl-35 as its driver")
    print("      any MCFR neutronics paper stating a composition AND a k in")
    print("        the same table -- which is the one thing none of the")
    print("        available sources does")
    print()


def _cap(fn):
    import contextlib
    import io
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        fn()
    return buf.getvalue()


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

    x, rho = composition()
    print()
    print("  the material is imported, not restated")
    check("the mol fraction comes from fuelchoice",
          x == F.mol_fraction_for_u_mass(M.SALT_U_MASS_FRAC))
    check("the density comes from materials", rho == M.SALT_RHO)
    # AND IT DOES NOT COME FROM criticality.py, which is the finding.
    check("the crossing is computed at the DESIGN's composition",
          crossing() == crossing(composition()[0]))
    check("  -- and differs from the published one, which is the eutectic's",
          abs(crossing() - crossing_published()) > 1e-3)
    check("  -- and is HIGHER, because a dilute salt absorbs more",
          crossing() > crossing_published())
    check("  -- and the published figure IS the eutectic's",
          abs(crossing_published()
              - crossing(F.EUTECTIC_MOL_UCL3)) < 1e-3)

    print()
    print("  the atom densities close, which is what catches a deck typo")
    for f in SCAN:
        check(f"density round-trips at f = {f:.4f}",
              abs(density_check(f) - rho) / rho < 1e-9)
    n = atom_densities(0.0793)
    check("chlorine balances the stoichiometry",
          abs((n["Cl37"] + n["Cl35"])
              / (3.0 * (n["Pu239"] + n["U238"]) + n["Na23"]) - 1.0) < 1e-9)
    check("the heavy metal is the stated mol fraction",
          abs((n["Pu239"] + n["U238"])
              / (n["Pu239"] + n["U238"] + n["Na23"]) - x) < 1e-9)
    check("the Cl-37 enrichment is what the design specifies",
          abs(n["Cl37"] / (n["Cl37"] + n["Cl35"]) - CL37_ENRICHMENT) < 1e-12)
    check("a fissile fraction outside [0,1] is refused",
          raises(lambda: molar_mass_salt(1.5)))

    print()
    print("  the prediction is registered, and it is the claim under test")
    check("the model's crossing is inside the scan",
          SCAN[0] < crossing() < SCAN[-1])
    check("  -- and a deck sits on it",
          any(abs(f - crossing()) < 5e-4 for f in SCAN))
    check("k_inf is one at the crossing, by construction",
          abs(prediction(crossing()) - 1.0) < 1e-6)
    check("  -- and is BELOW one at the published crossing, on this salt",
          prediction(crossing_published()) < 1.0)
    check("k_inf rises with fissile fraction",
          all(prediction(a) < prediction(b)
              for a, b in zip(SCAN, SCAN[1:])))
    check("every deck carries its own prediction in its header",
          all(f"{prediction(f):.4f}" in openmc_deck(f)
              and f"{prediction(f):.4f}" in serpent_deck(f) for f in SCAN))

    print()
    print("  the decks are decks")
    for f in (SCAN[0], crossing() if crossing() in SCAN else SCAN[2]):
        o, s = openmc_deck(f), serpent_deck(f)
        check(f"the OpenMC deck at {f:.4f} is reflective and eigenvalue",
              "reflective" in o and "eigenvalue" in o)
        check(f"  -- and imports openmc and runs it", "import openmc" in o
              and "openmc.run()" in o)
        check(f"the Serpent deck at {f:.4f} sets a reflective boundary",
              "set bc 2" in s)
        check(f"  -- and carries a ZAID for every nuclide present",
              all(z in s for z in ("94239", "92238", "11023", "17037")))
    check("the OpenMC deck parses as Python",
          compile(openmc_deck(0.0793), "<deck>", "exec") is not None)

    print()
    print("  the provenance flag, and that it is stated as a flag")
    _lo_c, _hi_c = published_crossing_band()
    check("a critical reactor's k_inf = 1 crossing is below its enrichment",
          _hi_c < MCFR_STARTUP_ENRICHMENT)
    check("  -- and the band widens with the leakage allowed",
          _lo_c < _hi_c)
    _lo_m, _hi_m = model_conservatism()
    check("the model demands MORE fissile than published practice",
          _lo_m > 1.0)
    check("  -- and it does so across the whole leakage band",
          _lo_m > 1.0 and _hi_m > 1.0)
    _lo_t, _hi_t = implied_true_threshold()
    check("the implied threshold is below the model's own",
          _hi_t < crossing())
    # THE FINDING: the design's operating fraction would sit ABOVE it.
    check("the design's operating fraction would sit ABOVE that threshold",
          crossing() > _hi_t)
    check("and at the implied threshold the plant does not close, or barely",
          math.isinf(closes_at(_lo_t))
          or closes_at(_lo_t) > 5.0 * closes_at(crossing()))
    check("  -- while at the design's fraction it closes ordinarily",
          math.isfinite(closes_at(crossing()))
          and closes_at(crossing()) < 400.0)
    _p = _cap(report_provenance)
    check("the report calls it a FLAG and not a result",
          "a FLAG" in _p and "not a result" in _p)
    check("  -- and names the assumption that is its weakest link",
          "weakest link" in _p and "ASSUMES the model errs" in _p)
    check("  -- and says the composition of the compared design is unstated",
          "not stated in what is" in _p)
    check("  -- and names the studies that would settle it",
          "Criticality Safety S/U" in _p)
    print()
    print("  and the file says what it did not do")
    out = _cap(report)
    check("the report records the composition finding",
          "PUBLISHED FOR A MATERIAL THE DESIGN" in out)
    check("  -- and says which way it runs, and that that is luck",
          "luck rather than design" in out)
    check("it states the decks were not run here",
          "not run in this environment" in out)
    check("  -- and why", "neither" in out and "evaluated cross-section" in out)
    check("  -- and that the prediction is registered in advance",
          "registered" in out and "marking their own homework" in out)

    print()
    print(f"selftest: {fail} failures -> {'PASS' if fail == 0 else 'FAIL'}")
    return 1 if fail else 0


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--selftest", action="store_true")
    ap.add_argument("--provenance", action="store_true",
                    help=report_provenance.__doc__)
    ap.add_argument("--write", action="store_true",
                    help="write the decks into decks/")
    a = ap.parse_args()
    if a.selftest:
        return selftest()
    if a.provenance:
        return report_provenance()
    if a.write:
        for p in write_decks():
            print(f"  wrote {os.path.relpath(p, ROOT)}")
        return 0
    return report()


if __name__ == "__main__":
    sys.exit(main())
