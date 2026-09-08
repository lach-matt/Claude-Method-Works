#!/usr/bin/env python3
"""powersource.py -- the inverse problem: what a SELF-SUSTAINING POWER SOURCE
requires, solved rather than reported.

Every other instrument here takes a configuration and returns its balance. This
one runs the other way. It sets the balance to unity and solves for what each
term must be, because a verdict ("0.171, it fails") is not a specification and
the project asked for a specification.

    G  =  N . V . eta / E_pi   =  1

Four terms, and they are not alike. Two are bounded ABOVE by something no
engineering can move, and the instrument says so rather than quoting a number:

    N     the service life, bounded by 1/omega_s -- the sticking cap
    eta   the collection, bounded by 1 -- it is a fraction
    E_pi  the production cost, bounded BELOW by nothing proved here
    V     the value recovered per fusion, bounded above by nothing proved here

So a self-sustaining power source is a statement about V and E_pi, and the
instrument computes what each must be.

THE CLAUSE THIS EXISTS TO CORRECT. [3] sec.5.1 says breakeven "would need a
multiplication of 6.33 neutrons per source neutron -- beyond any (n,xn)
blanket, and reachable only by fission, which changes the product rather than
the yield." The first half is right. The second half is wrong: fission in a
SUBCRITICAL blanket returns heat, on site, inside the device, and heat is the
product. That is not a change of product; it is the product the whole exercise
was for.

WHAT IT REFUSES. It does not compare the configuration against spending the
same beam on a spallation-driven subcritical system, which is the deciding
comparison for a builder and which no number here settles. It reports the
requirement and the margin, not the choice.

Stdlib only.  python3 tools/powersource.py [--selftest]
"""
import math
import argparse
import functools
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

# ---- what the balance is made of, all of it measured or sourced ------------
E_ALPHA_MEV = 3.5           # [C59]  d+t alpha, standard nuclear data
E_NEUTRON_MEV = 14.1        # [C58]  d+t neutron, standard nuclear data
E_FISSION_MEV = 200.0       # [C196] downstream yield of one fissile nucleus
NU_FAST = 2.9               # neutrons per fast fission, Pu-239; SOURCED
STICKING = 0.00505          # [C113] the operative effective sticking
E_PI_MEASURED = 11.13       # [C100] GeV per pi-, integrated from HARP
E_PI_OPTIMISED = 4.69       # [C290] GeV per pi-, published optimisation
N_MEASURED = 150.0          # [C44]  cycles per binder, Los Alamos
V_HEAT_MEV = 26.06          # [C214] the sourced fission-SUPPRESSED blanket


@functools.lru_cache(maxsize=None)
def _mach():
    import machine
    return machine


def service_life_cap():
    """No service life exceeds this, at any density, by Proposition 1."""
    return 1.0 / STICKING


def configurations():
    m = _mach()
    return (
        ("as built", m.delivered_eta_window(1.50, 265.0), E_PI_MEASURED),
        ("both collector alterations", m.delivered_eta_window(2.60, 400.0),
         E_PI_MEASURED),
        ("with the optimised target", m.delivered_eta_window(1.50, 265.0),
         E_PI_OPTIMISED),
        ("with all three alterations", m.delivered_eta_window(2.60, 400.0),
         E_PI_OPTIMISED),
    )


# ---- the inverse problem ---------------------------------------------------
def required(term, n=N_MEASURED, v_mev=V_HEAT_MEV, eta=None, e_pi=None):
    """Solve G = 1 for one term with the others held where they are."""
    v = v_mev / 1000.0
    if term == "N":
        return e_pi / (v * eta)
    if term == "eta":
        return e_pi / (n * v)
    if term == "E_pi":
        return n * v * eta
    if term == "V":
        return 1000.0 * e_pi / (n * eta)
    raise KeyError(term)


# ---- the subcritical blanket, derived rather than quoted --------------------
def energy_per_source_neutron(k_eff, nu=NU_FAST, e_f=E_FISSION_MEV):
    """Fission energy released per source neutron in a subcritical assembly.

    Source multiplication gives M = 1/(1-k) neutrons in circulation per source
    neutron. One of those is the source neutron itself, so M-1 were born in
    fission, and each fission makes nu of them. Hence

        fissions per source neutron  F = (M - 1)/nu = k / (nu (1 - k))

    and the energy is F E_f. Two sourced inputs, one identity, no fit.
    """
    if not 0.0 <= k_eff < 1.0:
        raise ValueError("k_eff must lie in [0, 1)")
    return e_f * k_eff / (nu * (1.0 - k_eff))


def k_for_energy(target_mev, nu=NU_FAST, e_f=E_FISSION_MEV):
    """Invert the above: the k_eff that returns a required energy."""
    r = target_mev * nu / e_f
    return r / (1.0 + r)


def k_of_sourced_blanket(multiplication=1.6):
    """The k_eff the sourced fission-SUPPRESSED blanket sits at.

    Attributing its whole multiplication to fission overstates k -- some of it
    is Li-6 breeding exotherm -- so this is an UPPER bound on where that design
    sits, which is the direction that makes the comparison honest.
    """
    return k_for_energy(multiplication * E_NEUTRON_MEV)


def required_k(eta, e_pi, n=N_MEASURED):
    """The k_eff a self-sustaining POWER source needs, in one configuration."""
    v_req = required("V", n=n, eta=eta, e_pi=e_pi)
    return k_for_energy(max(0.0, v_req - E_ALPHA_MEV)), v_req


def fusion_share(v_req_mev):
    """How much of the recovered energy the FUSION supplies at that point."""
    return (E_ALPHA_MEV + E_NEUTRON_MEV) / v_req_mev


# ---- the comparison the paper had left unmade -------------------------------
# The muon channel does NOT replace spallation. The same protons hit the same
# target and make both: pions AND spallation neutrons. So the muon channel is
# additive in neutrons, and there is no "instead" to price. What there IS to
# price is that a target the pions can escape from is NARROW -- [1] sec.5.28's
# transparency argument fixes its radius -- and a narrow target is a poorer
# spallation source than the thick one a neutron facility would otherwise
# choose. That, and only that, is the trade.
BEAM_GEV = 8.0              # the HARP column the production integral uses
PI_PER_PROTON = 0.7188      # [C99] combined pi- per interacting proton


def fusion_neutrons_per_proton(eta, n_cycles=N_MEASURED):
    """Neutrons the muon channel ADDS, per interacting proton.

    One stopped binder catalyses n_cycles fusions and each fusion makes one
    neutron, so this is the pion yield times the collection times the life.
    """
    return PI_PER_PROTON * eta * n_cycles


def transparency_breakeven(spallation_per_proton, eta, worth=1.0,
                           n_cycles=N_MEASURED):
    """The fractional spallation yield a pion-transparent target may lose.

    Route A  a spallation-optimised target:      Y neutrons per proton
    Route B  a pion-transparent target:          Y(1-f) + w . Y_fus

    Setting them equal gives f = w . Y_fus / Y, and the muon channel is a net
    addition whenever the transparency penalty is below it. `worth` is what a
    14.1 MeV neutron is worth against a spallation neutron as a source; it is
    ABOVE one in any fast blanket, because 14.1 MeV drives fast fission and
    (n,2n) that a spallation spectrum reaches less of -- so worth = 1 is the
    conservative choice and is the default here.
    """
    return worth * fusion_neutrons_per_proton(eta, n_cycles) / spallation_per_proton


def report_spallation():
    """The comparison against spending the same beam on spallation alone."""
    m = _mach()
    print("  THE MUON CHANNEL AGAINST SPALLATION, ON THE SAME BEAM")
    print("    The question sec.11 records as unmade. It has a structure worth")
    print("    stating before any number: the muon channel does NOT replace")
    print("    spallation. The same protons hit the same target and make BOTH,")
    print("    so the muon channel is ADDITIVE in neutrons and there is no")
    print("    'instead' to price.")
    print()
    print("    What there is to price is that a target the pions can escape")
    print("    from is NARROW -- the transparency argument fixes its radius --")
    print("    and a narrow target is a poorer spallation source than the thick")
    print("    one a neutron facility would otherwise choose. That is the whole")
    print("    of the trade, and it is one number: how much spallation yield")
    print("    transparency costs.")
    print()
    for lab, eta, _e in configurations()[:2]:
        y = fusion_neutrons_per_proton(eta)
        print(f"    neutrons the muon channel adds, {lab:<28} {y:6.2f} per proton")
    print(f"      = {PI_PER_PROTON} pi-/proton x collection x {N_MEASURED:.0f} fusions")
    print()
    eta_best = m.delivered_eta_window(2.60, 400.0)
    print("    THE BREAK-EVEN, against what a spallation-optimised target makes:")
    print(f"      {'spallation n per proton':>26}{'penalty it may lose':>22}")
    for y in (50.0, 75.0, 100.0, 125.0, 150.0, 200.0, 250.0):
        f = transparency_breakeven(y, eta_best)
        print(f"      {y:26.0f}{100 * min(f, 1.0):21.1f} %")
    print()
    print("    READ IT AS A REQUIREMENT ON THE TARGET, WHICH IS WHAT IT IS.")
    print("    The muon channel is a net addition of neutrons unless making the")
    print("    target transparent to pions costs more than the figure above. At")
    print("    the highest spallation yield tabulated the requirement is still")
    f_hi = transparency_breakeven(250.0, eta_best)
    print(f"    that transparency cost stay under {100 * f_hi:.1f} percent.")
    print()
    print("    AND IT IS CONSERVATIVE IN TWO PLACES. A 14.1 MeV neutron is worth")
    print("    MORE than a spallation neutron as a source, because it drives")
    print("    fast fission and (n,2n) that a spallation spectrum reaches less")
    print("    of; this takes that worth as exactly one. And the muon route also")
    print("    returns the alpha directly as heat, which is not counted here.")
    print()
    print("    WHAT THIS STILL DOES NOT SETTLE. What a spallation-optimised")
    print(f"    target at {BEAM_GEV:.0f} GeV actually yields, and what transparency actually")
    print("    costs it. Neither is in this corpus, both are computable by a")
    print("    target designer, and sec.10 Stage D measures the pair on one")
    print("    apparatus -- the same beam and the same blanket, with the fuel")
    print("    cell in and out.")
    return 0


# ---- the two target figures the comparison had left open --------------------
# THE FIRST is what a spallation-optimised target returns at this beam energy.
# It is not a mystery: a thick heavy-metal target degrades essentially all of
# the beam into a cascade, and the cascade's neutron yield per unit of energy
# DEPOSITED is a flat, measured property of the material. So the yield is the
# beam energy times that figure, and the figure is what is sourced.
#
# THE SECOND is what pion-transparency costs it. That one turns out to be the
# wrong question in a blanket-coupled system, and the geometry says why.
N_PER_GEV_PB_LO = 25.0      # neutrons per GeV DEPOSITED, lead/mercury, low end
N_PER_GEV_PB_HI = 30.0      # the high end of the same engineering figure
U_OVER_PB = 1.5             # depleted uranium against lead, per GeV deposited
LAMBDA_HG_CM = 15.0         # inelastic interaction length; the repo's jet is 2 of them
JET_RADIUS_CM = 0.40        # [1] the published 8 mm jet
JET_LENGTH_CM = 30.0        # the same jet


@functools.lru_cache(maxsize=None)
def spallation_yield(e_gev=BEAM_GEV, n_per_gev=None):
    """Neutrons per proton from a target thick enough to contain the cascade."""
    lo = e_gev * N_PER_GEV_PB_LO
    hi = e_gev * N_PER_GEV_PB_HI
    return (lo, hi) if n_per_gev is None else (e_gev * n_per_gev,)


def primary_interacting(length_cm=JET_LENGTH_CM, lam=LAMBDA_HG_CM):
    """Fraction of the primary beam that interacts inside the target."""
    import math
    return 1.0 - math.exp(-length_cm / lam)


def cascade_retained(radius_cm=JET_RADIUS_CM, lam=LAMBDA_HG_CM):
    """Fraction of the CASCADE the transparent target keeps after the first
    interaction.

    A secondary born on the axis of a cylinder of radius r escapes sideways
    unless it interacts within that path, so the retention is 1 - exp(-r/lam).
    For the published jet r/lam is small and the retention is nearly nothing:
    the target is a production foil, not a spallation target.
    """
    import math
    return 1.0 - math.exp(-radius_cm / lam)


def transparency_penalty(u_over_pb=U_OVER_PB, radius_cm=JET_RADIUS_CM,
                         lam=LAMBDA_HG_CM):
    """What transparency costs the spallation yield, blanket-coupled.

    The cascade energy the narrow target does not keep is not lost: it crosses
    into the blanket and develops there. So the yield is

        Y  =  E [ phi . y_target  +  (1 - phi) . y_blanket ]

    with phi the fraction retained. The penalty against a fully-containing
    target of the SAME material is (1 - phi)(1 - y_blanket/y_target), which is
    NEGATIVE -- a gain -- whenever the blanket out-yields the target per unit
    of energy deposited. Depleted uranium out-yields lead, so it does.
    """
    phi = cascade_retained(radius_cm, lam)
    return (1.0 - phi) * (1.0 - u_over_pb)


def report_target():
    """The two target figures: the spallation yield, and transparency's cost."""
    print("  THE TWO TARGET FIGURES, CLOSED")
    print()
    print("  ONE -- WHAT A SPALLATION-OPTIMISED TARGET RETURNS")
    print("    A target thick enough to contain the cascade degrades essentially")
    print("    all of the beam into it, and the neutron yield per unit of energy")
    print("    DEPOSITED is a flat property of the material rather than of the")
    print(f"    machine: {N_PER_GEV_PB_LO:.0f} to {N_PER_GEV_PB_HI:.0f} neutrons per GeV for lead or mercury.")
    lo, hi = spallation_yield()
    print(f"    At {BEAM_GEV:.0f} GeV that is {lo:.0f} to {hi:.0f} neutrons per proton.")
    print()
    print("  TWO -- WHAT TRANSPARENCY COSTS IT, AND WHY THE QUESTION CHANGES")
    print(f"    The published jet is {2 * JET_RADIUS_CM:.1f} cm across and {JET_LENGTH_CM:.0f} cm long, against an")
    print(f"    interaction length of {LAMBDA_HG_CM:.0f} cm. Those are different by two orders:")
    print(f"      along the beam   {JET_LENGTH_CM / LAMBDA_HG_CM:>6.2f} interaction lengths"
          f"  -> {100 * primary_interacting():.1f} % of primaries interact")
    print(f"      across it        {JET_RADIUS_CM / LAMBDA_HG_CM:>6.3f} interaction lengths"
          f"  -> {100 * cascade_retained():.1f} % of the cascade is kept")
    print()
    print("    SO IT IS NOT A NARROW SPALLATION TARGET. It is a production foil.")
    print("    It stops the primary and it keeps almost none of the cascade the")
    print("    primary starts. In a bare neutron source that would be the whole")
    print("    loss. In a BLANKET-COUPLED system it is not a loss at all: the")
    print("    cascade crosses into the blanket and develops there.")
    print()
    print("    Writing y for neutrons per GeV deposited and phi for what the")
    print("    target keeps,")
    print()
    print("      Y = E [ phi . y_target + (1 - phi) . y_blanket ]")
    print()
    print(f"    and the penalty against a fully-containing target of the same")
    print(f"    material is (1 - phi)(1 - y_blanket/y_target). Depleted uranium")
    print(f"    out-yields lead by about {U_OVER_PB:.1f} per GeV deposited, because the")
    print(f"    cascade fast-fissions in it. So the penalty is")
    f = transparency_penalty()
    print()
    print(f"      transparency penalty  =  {100 * f:+.1f} %   -- a GAIN, not a cost")
    print()
    print("    THE BREAK-EVEN IS THEREFORE NOT MERELY MET. sec.9.4 asked how much")
    print("    transparency may cost before the muon channel stops paying, and")
    print("    the answer is that it costs nothing: the cascade is not thrown")
    print("    away, it is handed to the material that converts it best.")
    print()
    print("    WHAT WOULD OVERTURN THIS. A blanket that out-yields the target by")
    print("    LESS than one -- a low-Z or non-fissile blanket. The penalty is")
    print("    then positive and sec.9.4's table applies as written:")
    print(f"      {'y_blanket / y_target':>22}{'penalty':>12}")
    for r in (0.5, 0.75, 1.0, 1.25, U_OVER_PB, 2.0):
        print(f"      {r:22.2f}{100 * transparency_penalty(r):+11.1f} %")
    print("    Even at parity the penalty is zero. It is positive only for a")
    print("    blanket WORSE than the target per GeV, which a fissile one is not.")
    return 0


# ---- THE CRITERION THE PROJECT ACTUALLY ASKED FOR ---------------------------
# Everything above prices the reaction against the BEAM. That is the eighth
# condition's question and it is the right one to ask of a reaction. It is not
# the question to ask of a POWER SOURCE, because the beam does not stop. A
# machine that returns more than its beam is an amplifier; a machine that runs
# on nothing after it is lit is a power source, and the difference between them
# is two conversion efficiencies nothing in this work had counted.
#
#   heat out  ->  electricity      at eta_th
#   electricity -> beam            at eta_acc
#
# so the loop closes when  G > 1 / (eta_th . eta_acc), and that is a far
# heavier requirement than G > 1.
CARNOT_AT_BLANKET = 0.750    # [C174] Carnot at the advanced blanket temperature
CARNOT_REALISED = 0.60       # a real cycle against its Carnot ceiling; SOURCED
ETA_ACC_LO = 0.20            # wall plug to beam, high-power proton linac; SOURCED
ETA_ACC_HI = 0.50            # the design target for a superconducting one
Q_FUS_MEV = 17.59            # [C01]
E_ALPHA_MEV_ = E_ALPHA_MEV


def eta_thermal(realised=CARNOT_REALISED):
    """Heat to electricity. Bounded above by Carnot at the blanket temperature."""
    return CARNOT_AT_BLANKET * realised


def loop_requirement(eta_acc, realised=CARNOT_REALISED):
    """The balance a closed loop needs: G > 1 / (eta_th . eta_acc)."""
    return 1.0 / (eta_thermal(realised) * eta_acc)


def plant_energy_per_proton(k_eff, y_spall, y_fus, e_beam_mev=None):
    """Everything the beam returns, per interacting proton.

    The beam's own energy is deposited in the assembly and recovered as heat.
    On top of that: the fusion energy the muon channel makes, which is new, and
    the fission energy EVERY source neutron drives -- the spallation neutrons
    and the fusion neutrons alike, because the blanket does not know which is
    which.
    """
    e_beam = (BEAM_GEV * 1000.0) if e_beam_mev is None else e_beam_mev
    return (e_beam
            + y_fus * Q_FUS_MEV
            + (y_spall + y_fus) * energy_per_source_neutron(k_eff))


def plant_gain(k_eff, y_spall, y_fus):
    return plant_energy_per_proton(k_eff, y_spall, y_fus) / (BEAM_GEV * 1000.0)


def k_for_plant_gain(g, y_spall, y_fus):
    """The k a closed loop needs, counting every neutron the beam makes."""
    e_beam = BEAM_GEV * 1000.0
    need = (g * e_beam - e_beam - y_fus * Q_FUS_MEV) / (y_spall + y_fus)
    return k_for_energy(max(0.0, need))


def report_plant():
    """The closed loop: what runs on nothing after it is lit."""
    m = _mach()
    eta_w = m.delivered_eta_window(2.60, 400.0)
    y_fus = fusion_neutrons_per_proton(eta_w)
    y_sp = 0.5 * sum(spallation_yield())
    print("  THE CLOSED LOOP -- A POWER SOURCE, NOT AN AMPLIFIER")
    print("    Everything before this prices the reaction against the BEAM, which")
    print("    is the eighth condition's question and the right one to ask of a")
    print("    REACTION. It is the wrong one to ask of a POWER SOURCE, because")
    print("    the beam does not stop. A machine that returns more than its beam")
    print("    is an amplifier. A machine that runs on nothing once it is lit is")
    print("    a power source, and the difference is two conversions this work")
    print("    had never counted:")
    print()
    print(f"      heat -> electricity   at eta_th, ceiling Carnot = {CARNOT_AT_BLANKET}")
    print(f"                            realised at {CARNOT_REALISED:.2f} of it -> {eta_thermal():.3f}")
    print(f"      electricity -> beam   at eta_acc = {ETA_ACC_LO:.2f} to {ETA_ACC_HI:.2f}")
    print()
    print("    So the loop closes at  G > 1 / (eta_th . eta_acc):")
    print(f"      {'eta_acc':>10}{'G required':>14}")
    for ea in (ETA_ACC_HI, 0.40, 0.30, ETA_ACC_LO):
        print(f"      {ea:10.2f}{loop_requirement(ea):14.2f}")
    print()
    print("    AND THE ACCOUNTING CHANGES WITH THE QUESTION. Against the beam, only")
    print("    the fusion neutrons counted. For the PLANT, everything the beam")
    print("    makes counts -- the beam energy itself is deposited and recovered,")
    print("    the muon channel's fusions are new energy, and the blanket does not")
    print("    know which neutron is which:")
    print()
    print("      E = E_beam + Y_fus . Q_fus + (Y_sp + Y_fus) . E(k)")
    print()
    print(f"      Y_sp  = {y_sp:.0f} spallation neutrons per proton  (sec.9.4)")
    print(f"      Y_fus = {y_fus:.2f} fusion neutrons per proton     (the muon channel)")
    print()
    print("    THE SUBCRITICAL k A CLOSED LOOP NEEDS")
    print(f"      {'eta_acc':>8}{'G needed':>10}{'k with muons':>14}{'k without':>12}{'margin':>9}")
    for ea in (ETA_ACC_HI, 0.40, 0.30, ETA_ACC_LO):
        g = loop_requirement(ea)
        kw = k_for_plant_gain(g, y_sp, y_fus)
        ko = k_for_plant_gain(g, y_sp, 0.0)
        print(f"      {ea:8.2f}{g:10.2f}{kw:14.3f}{ko:12.3f}{ko - kw:+9.3f}")
    print()
    print("    EVERY ONE IS SUBCRITICAL, and every one is below the 0.95 an")
    print("    accelerator-driven system is designed around. THE LOOP CLOSES.")
    print()
    print("    AND A PLANT WANTS MORE THAN BREAK-EVEN. At the loop requirement")
    print("    all of the output recirculates and none is sold. For a net")
    print("    electrical fraction of 1 - G_req/G:")
    g_req = loop_requirement(0.30)
    print(f"      {'net electric':>14}{'G needed':>10}{'k needed':>10}")
    for net in (0.0, 0.50, 0.75, 0.90):
        g = g_req / max(1e-9, (1.0 - net)) if net < 1.0 else float("inf")
        print(f"      {100 * net:13.0f} %{g:10.2f}{k_for_plant_gain(g, y_sp, y_fus):10.3f}")
    print()
    print("    WHAT THE MUON CHANNEL ACTUALLY CONTRIBUTES, STATED PLAINLY.")
    print("    Not the loop. A subcritical assembly driven by spallation alone")
    print("    closes it too, and has been proposed for that purpose for decades.")
    ea = 0.30
    g = loop_requirement(ea)
    kw, ko = k_for_plant_gain(g, y_sp, y_fus), k_for_plant_gain(g, y_sp, 0.0)
    print(f"    What the muon channel adds is {100 * y_fus / y_sp:.0f} percent more source neutrons and so")
    print(f"    the SAME loop at a k lower by {ko - kw:.3f} -- {kw:.3f} against {ko:.3f}. That is")
    print("    subcriticality margin, which is a safety property before it is an")
    print("    energy one, and it is what the channel is worth here.")
    print()
    print("    WHAT IT CONSUMES AFTER IGNITION.")
    print("      electricity   none -- the loop is closed")
    print("      tritium       none -- the blanket breeds at 1.15 per fusion")
    print("      fissile fuel  fertile feed, bred in place; NOT free, and this")
    print("                    work does not price the fuel cycle")
    return 0


# ---- STABILITY, which is a separate requirement and has two halves ----------
# A power source that closes its loop and then runs away, or drifts off its
# operating point, is not a power source. Stability here is two questions that
# happen to have opposite answers, and conflating them is the error to avoid.
#
#   THE NEUTRONICS are stable by construction. The assembly is subcritical, so
#   the power is set by the source rather than by a chain that sustains itself.
#   There is no prompt-critical excursion available at any k < 1.
#
#   THE LOOP is NOT stable by construction. At the operating point its gain is
#   exactly one -- that is what "closed" means -- so a fixed-fraction feedback
#   is MARGINALLY stable and any perturbation persists. The beam has to be
#   regulated against a measured power, not simply fed a share of the output.
DOPPLER_K_LO = 0.005        # |T dk/dT|, fertile-loaded fast system; SOURCED
DOPPLER_K_HI = 0.010        # the other end of the same band
T_BLANKET_K = 800.0         # [C76] blanket operating temperature
CONTROL_WORTH_PCM = 5000.0  # total control worth of a fast reactor; SOURCED


def power_sensitivity(k_eff):
    """d(power)/power per unit dk. E(k) ~ k/(1-k), so this is 1/(k(1-k))."""
    return 1.0 / (k_eff * (1.0 - k_eff))


def subcritical_margin(k_eff):
    """Margin to criticality, in dk and in pcm."""
    return 1.0 - k_eff, 1e5 * (1.0 - k_eff)


def doppler_dk_per_k(kd=DOPPLER_K_LO, t_k=T_BLANKET_K):
    """Reactivity per kelvin from Doppler broadening. Negative: it restores."""
    return -kd / t_k


def restoring_delta_t(k_eff, margin=0.01, kd=DOPPLER_K_LO):
    """The temperature rise that pulls the loop gain `margin` below unity."""
    per_k = abs(doppler_dk_per_k(kd)) * power_sensitivity(k_eff)
    return margin / per_k


def report_stability():
    """Stability: the neutronics by construction, the loop by regulation."""
    m = _mach()
    eta_w = m.delivered_eta_window(2.60, 400.0)
    y_f = fusion_neutrons_per_proton(eta_w)
    y_s = 0.5 * sum(spallation_yield())
    k_loop = k_for_plant_gain(loop_requirement(0.30), y_s, y_f)
    k_plant = k_for_plant_gain(loop_requirement(0.30) / 0.25, y_s, y_f)
    print("  STABILITY, WHICH IS TWO QUESTIONS WITH OPPOSITE ANSWERS")
    print()
    print("  ONE -- THE NEUTRONICS ARE STABLE BY CONSTRUCTION")
    print("    The assembly is subcritical. Its power is set by the SOURCE and")
    print("    not by a chain that sustains itself, so there is no prompt-critical")
    print("    excursion available at any k < 1: cut the beam and it stops. The")
    print("    margin to criticality is what a reactivity insertion would have to")
    print("    cross, and it is large:")
    print()
    print(f"      {'operating point':<34}{'k':>8}{'margin':>10}{'pcm':>10}")
    for lab, k in (("the loop only closing", k_loop),
                   ("a plant selling three quarters", k_plant),
                   ("an accelerator-driven system", 0.95)):
        dk, pcm = subcritical_margin(k)
        print(f"      {lab:<34}{k:8.3f}{dk:10.3f}{pcm:10.0f}")
    dk_p, pcm_p = subcritical_margin(k_plant)
    print()
    print(f"    Against a total control worth of about {CONTROL_WORTH_PCM:.0f} pcm for a fast")
    print(f"    system, the plant's margin of {pcm_p:.0f} pcm is {pcm_p / CONTROL_WORTH_PCM:.1f} times the whole")
    print("    reactivity a comparable core can hold. No credible insertion")
    print("    reaches criticality. THAT IS THE SAFETY CASE, and it is why the")
    print("    subcritical route is worth its accelerator.")
    print()
    print("  TWO -- THE LOOP IS NOT STABLE BY CONSTRUCTION, AND THIS IS THE FINDING")
    print("    At the operating point the recirculating loop's gain is EXACTLY")
    print("    one. That is what 'closed' means. So a fixed-fraction feedback --")
    print("    take a share of the output, make beam with it -- is MARGINALLY")
    print("    stable: a perturbation neither grows nor decays, and the machine")
    print("    walks off its operating point on any drift.")
    print()
    print("    THE LOOP CANNOT BE CLOSED PASSIVELY. The beam must be regulated")
    print("    against a MEASURED power to a setpoint, so that the loop is closed")
    print("    by a controller rather than by the physics. That is an ordinary")
    print("    control problem with an ordinary solution, but it has to be said,")
    print("    because 'the loop closes' sounds passive and is not.")
    print()
    print("  AND THE PHYSICS DOES SUPPLY THE RESTORING TERM")
    print("    Power amplifies reactivity as 1/(k(1-k)), so the closer to")
    print("    criticality the sharper the response:")
    print()
    print(f"      {'k':>8}{'dP/P per dk':>14}{'dT to restore 1 %':>20}")
    for k in (k_loop, 0.85, k_plant, 0.95):
        print(f"      {k:8.3f}{power_sensitivity(k):14.1f}{restoring_delta_t(k):17.0f} K")
    print()
    print("    Doppler broadening in the fertile loading gives a NEGATIVE")
    print(f"    coefficient of about {DOPPLER_K_LO:.3f} to {DOPPLER_K_HI:.3f} in |T dk/dT|, so a rise in")
    print(f"    temperature lowers k, lowers the gain, and lowers the power. At the")
    print(f"    plant point that restores one percent of gain in {restoring_delta_t(k_plant):.0f} K, which")
    print("    is inside an ordinary operating swing. The feedback is adequate and")
    print("    it has the right sign.")
    print()
    print("  WHAT THE MUON CHANNEL DOES FOR STABILITY")
    k_no = k_for_plant_gain(loop_requirement(0.30), y_s, 0.0)
    print(f"    It lets the same loop close at k = {k_loop:.3f} instead of {k_no:.3f}, which is")
    print(f"    {1e5 * (k_no - k_loop):.0f} pcm of extra margin to criticality and a power")
    print(f"    sensitivity lower by {power_sensitivity(k_no) / power_sensitivity(k_loop):.2f}. Both are stability, and")
    print("    both are what the channel is worth here -- not the loop itself.")
    print()
    print("  WHAT THIS DOES NOT SETTLE.")
    print("    Beam trips. An accelerator-driven system's characteristic problem")
    print("    is not runaway but INTERRUPTION: every trip is a thermal cycle")
    print("    through the whole assembly, and trip rate rather than trip depth")
    print("    is what limits component life. No figure here bounds it, and it")
    print("    is a driver requirement rather than a physics one.")
    return 0


# ---- THE FUEL, WHICH MUST BE PRICED RATHER THAN NAMED --------------------
# "Fertile feed, not free, and not priced here" is a dodge. If the fuel costs
# more than the reaction returns, there is no power source, so the fuel has to
# be priced -- and the honest way to price it is to ask whether the device
# needs any after it is lit.
#
# It does not, IF it breeds what it burns. That is a neutron-balance statement
# and it closes in one line. Per source neutron a subcritical assembly makes
# 1/(1-k) neutrons in all and F = k/(nu(1-k)) of them cause fission, so the
# absorptions NOT spent on fission are 1/(1-k) - F. Breeding one fissile atom
# for every atom fissioned needs a fraction f_b of those to land in fertile
# material, and
#
#     f_b  >=  F / (1/(1-k) - F)  =  k / (nu - k)
#
# with everything else -- structure, coolant, fission products, leakage --
# sharing what is left.
def fissions_per_source(k_eff, nu=NU_FAST):
    return k_eff / (nu * (1.0 - k_eff))


def neutrons_per_source(k_eff):
    return 1.0 / (1.0 - k_eff)


def fertile_capture_required(k_eff, nu=NU_FAST):
    """The share of non-fission absorptions that must breed, for self-supply.

    Below this the assembly eats its own inventory and the fuel has a price.
    At or above it the device breeds what it burns and the fuel, after the
    first charge, costs nothing.
    """
    return k_eff / (nu - k_eff)


def breeding_ratio(k_eff, f_b, nu=NU_FAST):
    """Fissile atoms bred per atom fissioned, at a given fertile capture share."""
    f = fissions_per_source(k_eff, nu)
    return f_b * (neutrons_per_source(k_eff) - f) / f


def report_fuel():
    """The fuel, priced: what the device must breed to need none."""
    m = _mach()
    eta_w = m.delivered_eta_window(2.60, 400.0)
    y_f = fusion_neutrons_per_proton(eta_w)
    y_s = 0.5 * sum(spallation_yield())
    k_loop = k_for_plant_gain(loop_requirement(0.30), y_s, y_f)
    k_plant = k_for_plant_gain(loop_requirement(0.30) / 0.25, y_s, y_f)
    print("  THE FUEL, PRICED")
    print("    Naming the fertile feed and declining to price it is a dodge. If")
    print("    the fuel costs more than the reaction returns there is no power")
    print("    source. The honest way to price it is to ask whether the device")
    print("    needs any AFTER it is lit -- and that is a neutron balance.")
    print()
    print("    Per source neutron the assembly makes 1/(1-k) neutrons in all,")
    print(f"    and F = k/(nu(1-k)) of them cause fission at nu = {NU_FAST}. The")
    print("    absorptions NOT spent on fission are the difference. Breeding one")
    print("    fissile atom for each one fissioned therefore needs a fraction")
    print()
    print("      f_b  >=  F / (1/(1-k) - F)  =  k / (nu - k)")
    print()
    print("    of those absorptions to land in FERTILE material, with structure,")
    print("    coolant, fission products and leakage sharing the rest.")
    print()
    print(f"      {'k':>8}{'fissions':>11}{'neutrons':>11}{'spare abs':>12}{'f_b needed':>13}")
    for k in (k_loop, k_plant, 0.95):
        f = fissions_per_source(k)
        n = neutrons_per_source(k)
        print(f"      {k:8.3f}{f:11.4f}{n:11.3f}{n - f:12.4f}"
              f"{fertile_capture_required(k):13.3f}")
    print()
    print("    THE REQUIREMENT IS MET BY A BLANKET THAT IS MOSTLY FERTILE, which")
    print("    is what a fertile-loaded blanket is. Between a quarter and a half")
    print("    of the spare absorptions have to breed; the remainder is the")
    print("    parasitic budget, and it is a large one.")
    print()
    print("    IT IS ALSO EASIER THE FURTHER FROM CRITICALITY THE DEVICE SITS:")
    print(f"      at k = {k_loop:.3f} the requirement is {fertile_capture_required(k_loop):.3f}")
    print(f"      at k = {k_plant:.3f} it is {fertile_capture_required(k_plant):.3f}")
    print("    so the margin the muon channel buys is worth something here too.")
    print()
    print("    WHAT THE DEVICE THEREFORE CONSUMES AFTER IGNITION")
    print("      electricity   none -- the loop is closed")
    print("      tritium       none -- bred at 1.15 per fusion, above replacement")
    print(f"      fissile       none -- bred at 1.00 or above when f_b >= {fertile_capture_required(k_loop):.3f}")
    print("      fertile       yes -- and this is the one real feed. It is the")
    print("                    material the breeding consumes, and it is the")
    print("                    cheapest and most abundant input in the whole")
    print("                    device.")
    print()
    print("    SO THE IGNITION COST IS A ONE-TIME CHARGE, AND IT IS THREE THINGS:")
    print("      an initial FISSILE loading, enough to bring the assembly to its")
    print("      operating k; an initial TRITIUM charge, enough to start the")
    print("      fusion cycle; and the ELECTRICITY to run the driver until the")
    print("      loop closes. After that the device buys nothing but fertile")
    print("      feed, and returns more energy than it takes.")
    print()
    print("    WHAT THIS DOES NOT SETTLE. The size of that initial charge, which")
    print("    is a blanket-design figure and not a physics one; the fuel-cycle")
    print("    plant that separates bred fissile from fission products; and")
    print("    whether f_b is reached in a specific geometry, which is a")
    print("    transport calculation. The requirement is stated in the form a")
    print("    blanket designer checks, and no further.")
    return 0


# ---- SCALE: the smallest unit that closes, and why it is a plant -----------
# The reaction scales down linearly and without complaint. The DRIVER does not.
# eta_acc is an at-design-current figure: a superconducting proton linac draws a
# fixed cryogenic and rf standby load whatever the beam current, so
#
#     eta_eff(P) = eta_acc . P / (P + S)
#
# and below some beam power the wall-plug efficiency collapses, the loop
# requirement runs away, and the k it would need crosses the safety margin. The
# floor on the device's SIZE is therefore set by the driver's overhead and not
# by any part of the reaction -- which is why the answer is a plant a
# municipality adopts rather than an appliance a household buys.
HOUSEHOLD_KW = 1.14          # 10,000 kWh/yr average electric; ASSUMED design point
K_SAFE = 0.95                # the ACCELERATOR-DRIVEN-SYSTEM CONVENTION: the
                             # margin equals a fast core's whole control worth.
                             # It is the field's number, not this design's.

# THE ADOPTED OPERATING POINT, AND IT IS LOWER THAN THE CONVENTION ALLOWS.
# criticality.py finds that below 7.93 % fissile the fuel salt's k_inf drops
# under one, and an assembly whose k_inf is under one cannot be made critical
# by any amount in any shape. Holding the design there means NO ACCUMULATION OF
# FUEL SALT ANYWHERE ON SITE CAN EVER BE CRITICAL WHEN DRY -- the hazard class
# stops existing rather than being managed by procedure.
#
# That property caps k_eff at k_inf.(1 - leak) = 0.900 and there is no
# intermediate: either k_inf < 1 and the property holds, or it does not.
#
# THE PRICE IS 2.76x THE DRIVER for the same output, because at lower
# multiplication more of the plant's own electricity recirculates into its
# accelerators. It was quoted at 2.05x when the decision was taken, corrected
# to 2.76x before it was implemented, and re-confirmed at the true figure.
#
# The number is DERIVED and stated here only so that this file does not import
# criticality.py, which imports fuelchoice.py, which imports this one.
# criticality.py's selftest asserts the two agree, so a change there that this
# file did not follow is a test failure rather than a silent divergence.
K_DESIGN = 0.900             # DERIVED: criticality.always_subcritical_threshold
K_DESIGN_MARGIN_NOTE = ("adopted for intrinsic criticality safety; "
                        "costs 2.76x the driver")
STANDBY_LO_KW = 200.0        # driver fixed load, low; SOURCED band
STANDBY_HI_KW = 2000.0       # the same, high


def gain_at_k(k_eff, y_spall=None, y_fus=None):
    if y_spall is None or y_fus is None:
        m = _mach()
        y_fus = fusion_neutrons_per_proton(m.delivered_eta_window(2.60, 400.0))
        y_spall = 0.5 * sum(spallation_yield())
    return plant_gain(k_eff, y_spall, y_fus)


def eta_effective(p_beam_kw, standby_kw, eta_acc=0.30):
    """Wall plug to beam, with the driver's fixed load carried."""
    return eta_acc * p_beam_kw / (p_beam_kw + standby_kw)


def minimum_beam_kw(standby_kw, k_eff=K_SAFE, eta_acc=0.30):
    """Beam power below which the loop cannot close at a safe k.

    Setting G_req(P) = G(k) and solving: P (eta_th eta_acc G - 1) = S.
    """
    g = gain_at_k(k_eff)
    denom = eta_thermal() * eta_acc * g - 1.0
    return standby_kw / denom if denom > 0 else float("inf")


def net_electric_kw(p_beam_kw, standby_kw, k_eff=K_SAFE, eta_acc=0.30):
    """What the plant sells, after its own driver is fed."""
    g = gain_at_k(k_eff)
    g_req = 1.0 / (eta_thermal() * eta_effective(p_beam_kw, standby_kw, eta_acc))
    return p_beam_kw * g * eta_thermal() * (1.0 - g_req / g)


def homes(net_kw):
    return net_kw / HOUSEHOLD_KW


# ---- the fuel, in the units a municipality buys it in ----------------------
FISSION_MEV = 200.0
ATOMS_PER_KG = 2.53e24       # heavy-actinide atoms in a kilogramme
J_PER_MEV = 1.602e-13


def joules_per_kg_fertile():
    return ATOMS_PER_KG * FISSION_MEV * J_PER_MEV


def fertile_grams_per_home_year(kwh=10000.0):
    return 1000.0 * (kwh * 3.6e6 / eta_thermal()) / joules_per_kg_fertile()


def home_years_per_kg():
    return joules_per_kg_fertile() * eta_thermal() / (10000.0 * 3.6e6)


def report_scale():
    """The smallest unit that closes, and what a municipality gets."""
    print("  SCALE: WHY THE ANSWER IS A PLANT AND NOT AN APPLIANCE")
    print()
    print("    The reaction scales down linearly and without complaint. The")
    print("    DRIVER does not. eta_acc is an at-design-current figure: a")
    print("    superconducting proton linac draws a fixed cryogenic and rf")
    print("    standby load S whatever the beam current, so")
    print()
    print("      eta_eff(P) = eta_acc . P / (P + S)")
    print()
    print("    and below some beam power the wall-plug efficiency collapses, the")
    print("    loop requirement runs away, and the k it would need crosses the")
    print("    safety margin.")
    print()
    g = gain_at_k(K_SAFE)
    print(f"    Holding k at {K_SAFE} -- a margin of {1e5 * (1 - K_SAFE):.0f} pcm, which is a fast core's")
    print(f"    whole control worth -- the plant gain is G = {g:.1f}.")
    print()
    print(f"      {'standby':>9}{'min beam':>11}{'at 3x min: net':>17}{'homes':>10}")
    for sb in (STANDBY_LO_KW, 500.0, 1000.0, STANDBY_HI_KW):
        pmin = minimum_beam_kw(sb)
        net = net_electric_kw(3 * pmin, sb)
        print(f"      {sb / 1000:6.1f} MW{pmin:9.0f} kW{net:14,.0f} kW{homes(net):10,.0f}")
    print()
    print("    WHAT IT COSTS TO TRY TO GO SMALLER. At 30 kW of beam against a")
    sb = 1000.0
    eff = eta_effective(30.0, sb)
    greq = 1.0 / (eta_thermal() * eff)
    m = _mach()
    yf = fusion_neutrons_per_proton(m.delivered_eta_window(2.60, 400.0))
    ys = 0.5 * sum(spallation_yield())
    k_need = k_for_plant_gain(greq, ys, yf)
    print(f"    1 MW standby the effective efficiency is {eff:.4f}, the loop needs")
    print(f"    G = {greq:.0f}, and that needs k = {k_need:.4f} -- a margin of {1e5 * (1 - k_need):.0f} pcm")
    print(f"    against a control worth of {CONTROL_WORTH_PCM:.0f}. NOT SAFE.")
    print()
    print("    THE MARGIN THAT MAKES THIS REACTOR SAFE IS THE SAME MARGIN THAT")
    print("    FORBIDS SHRINKING IT. That is the finding, and it decides the")
    print("    product: a plant a municipality adopts, not an appliance a")
    print("    household buys.")
    print()
    print("  WHAT A MUNICIPALITY GETS, AND WHAT IT FEEDS IT")
    print(f"    one kilogramme of fertile, fully burned: {joules_per_kg_fertile() / 3.6e9:,.0f} MWh thermal,")
    print(f"    {joules_per_kg_fertile() * eta_thermal() / 3.6e9:,.0f} MWh electric at eta_th = {eta_thermal():.3f}")
    print(f"    a household at 10,000 kWh a year burns {fertile_grams_per_home_year():.2f} GRAMS of it")
    print(f"    one kilogramme therefore runs one household for {home_years_per_kg():,.0f} years")
    print()
    print("    The feedstock is depleted uranium -- an existing waste stockpile --")
    print("    or thorium, which is commoner in the crust than tin. The fuel is")
    print("    not free, because nothing is; it is negligible, which is the")
    print("    strongest thing that can honestly be said of a fuel.")
    return 0


# ---- TRITIUM, WHICH IS THE ONE CONSUMABLE THE GEOMETRY WILL NOT SHRINK -----
# Criterion 4 -- nothing supplied after ignition -- is settled for the fissile
# inventory by fertile_capture_required() above. It is NOT settled by that for
# tritium, and tritium is the harder of the two, for a reason that is geometric
# rather than nuclear: the fuel cell must be one muon range deep (collector.py
# report_stopping), so its tritium inventory is areal density times beam area
# and DOES NOT FALL WITH POWER. A bigger plant burns more tritium but holds the
# same amount, and what a fixed holding does is decay: 5.48 % of it a year, at
# a 12.32 y half-life, whether the machine runs or not.
#
# THE ACCOUNTING TRAP, AND IT IS THE ONE THIS SECTION EXISTS TO CLOSE. A fusion
# reactor breeds tritium from its own neutrons and prices the balance as a
# breeding ratio -- TBR times the fusion neutron yield. Applied here that is
# wrong by the whole spallation channel, and wrong by a factor near twenty:
# the blanket is driven by every neutron the target makes, not by the fusion
# neutrons alone, and at k = 0.95 each source neutron becomes 1/(1-k) = 20. The
# supply is therefore a share of the BLANKET's neutron economy, and the question
# is whether that economy has room for it once fission and fertile capture are
# paid.
#
# Per source neutron the assembly makes n_tot = 1/(1-k) neutrons; F of them
# cause fission; A = n_tot - F meet a non-fission fate; f_b.A = F must land in
# fertile material or the fissile inventory is a consumable again. What is left,
# less an allowance L.n_tot for leakage and parasitic capture in structure,
# coolant and fission products, is what may be spent on Li-6:
#
#     avail  =  A - F - L . n_tot          per source neutron
#
# and the requirement is one Li-6 capture per triton consumed. L is ASSUMED and
# banded; the result below is therefore a REQUIREMENT on the blanket's neutron
# budget, not a prediction of it -- Stage D measures it.
T_HALFLIFE_Y = 12.32          # SOURCED
T_AMU = 3.016
N_AVOGADRO = 6.02214076e23
SEC_PER_YEAR = 3.15576e7
# The cell's radius is NOT a free parameter and is not restated here: it is
# machine.py's, set by adiabatic recompression to CELL_B_T from the channel
# field, and imported. A wider guess understates the holding and so understates
# the plant. (7.5 cm -- a published channel geometry at a different field -- was
# used here in an earlier pass and is wrong for the CELL by 1.43x in mass.)
REF_BEAM_MW = 10.0            # the single-module reference, superseded as the
                              # project's object by station() below but kept:
                              # the tritium thresholds are stated against it
                              # thresholds rather than one: 5.58 MW to hold its
                              # own inventory, 8.1 MW to breed a successor's
                              # first charge inside a 40 year life, and this,
                              # which clears both with margin.
REF_STANDBY_KW = 1000.0       # mid-band driver fixed load
LEAK_PARASITIC_LO = 0.10      # ASSUMED band: leakage + parasitic capture, as a
LEAK_PARASITIC_HI = 0.20      # share of the whole neutron population
F_LI_CEILING = 1.00           # every free neutron reaches Li-6; a ceiling, not a design
F_LI_DESIGN = 0.60            # ASSUMED: what a blanket that is also breeding fissile
                              # and also cooling actually routes into Li-6


@functools.lru_cache(maxsize=None)
def _coll():
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    import collector
    return collector


@functools.lru_cache(maxsize=None)
def tritium_inventory_kg(p_window_mev, b_cell=None):
    """The cell's holding. IMPORTED from machine.py's own cell geometry."""
    m = _mach()
    return m.cell_tritium_kg(m.CELL_B_T if b_cell is None else b_cell,
                             float(p_window_mev))


def tritium_decay_g_per_year(inventory_kg, half_life_y=T_HALFLIFE_Y):
    lam = math.log(2.0) / half_life_y
    return inventory_kg * 1000.0 * (1.0 - math.exp(-lam))


@functools.lru_cache(maxsize=None)
def protons_per_second(p_beam_mw, e_beam_gev=BEAM_GEV):
    return p_beam_mw * 1e6 / (e_beam_gev * 1e9 * 1.602176634e-19)


@functools.lru_cache(maxsize=None)
def fusions_per_proton(p_window_mev):
    """One fusion consumes one triton, so this is also tritons burnt per proton."""
    return PI_PER_PROTON * _mach().delivered_eta_window(1.50, float(p_window_mev)) \
        * N_MEASURED


def tritium_demand_per_second(p_window_mev, p_beam_mw, b_cell=None):
    """Decay of a fixed holding plus burn that scales with the beam."""
    inv = tritium_inventory_kg(p_window_mev, b_cell)
    decay_s = tritium_decay_g_per_year(inv) / SEC_PER_YEAR / T_AMU * N_AVOGADRO
    burn_s = fusions_per_proton(p_window_mev) * protons_per_second(p_beam_mw)
    return decay_s, burn_s


def free_neutrons_per_source(k_eff=K_SAFE, leak=LEAK_PARASITIC_HI, nu=NU_FAST):
    """What the blanket's economy has left for Li-6, per source neutron."""
    n_tot = neutrons_per_source(k_eff)
    f = fissions_per_source(k_eff, nu)
    return (n_tot - f) - f - leak * n_tot


def tritium_supply_per_second(p_window_mev, p_beam_mw, k_eff=K_SAFE,
                              leak=LEAK_PARASITIC_HI, y_spall=None,
                              f_li=F_LI_CEILING):
    """Tritons a second the neutron economy makes, at a stated Li-6 capture
    share f_li of the free neutrons. f_li = 1 is the ceiling; the design point
    is F_LI_DESIGN, because a blanket also breeding fissile and also cooled
    does not route everything spare into lithium."""
    if y_spall is None:
        y_spall = 0.5 * sum(spallation_yield())
    src_p = y_spall + fusions_per_proton(p_window_mev)
    return (f_li * free_neutrons_per_source(k_eff, leak)
            * src_p * protons_per_second(p_beam_mw))


def tritium_balance(p_window_mev, p_beam_mw, k_eff=K_SAFE,
                    leak=LEAK_PARASITIC_HI, b_cell=None,
                    f_li=F_LI_CEILING):
    """Supply over demand. Above one, criterion 4 holds on tritium."""
    d, b = tritium_demand_per_second(p_window_mev, p_beam_mw, b_cell)
    return tritium_supply_per_second(p_window_mev, p_beam_mw, k_eff, leak,
                                     f_li=f_li) / (d + b)


def beam_mw_for_tritium(p_window_mev, k_eff=K_SAFE, leak=LEAK_PARASITIC_HI,
                        b_cell=None, f_li=F_LI_CEILING):
    """The beam power at which the tritium balance closes.

    Demand is decay (fixed) plus burn (linear in P); supply is linear in P; so
    the balance is monotone in P and solves in closed form.
    """
    inv = tritium_inventory_kg(p_window_mev, b_cell)
    decay_s = tritium_decay_g_per_year(inv) / SEC_PER_YEAR / T_AMU * N_AVOGADRO
    per_mw = protons_per_second(1.0)
    burn_per_mw = fusions_per_proton(p_window_mev) * per_mw
    sup_per_mw = tritium_supply_per_second(p_window_mev, 1.0, k_eff, leak,
                                           f_li=f_li)
    if sup_per_mw <= burn_per_mw:
        return float("inf")
    return decay_s / (sup_per_mw - burn_per_mw)


def _beam_for_halflife(half_life_y, p_window_mev=265.0):
    """Only the decay term moves, so this isolates it: the requirement is a
    statement about the half-life and not about the reaction."""
    inv = tritium_inventory_kg(p_window_mev)
    decay_s = (tritium_decay_g_per_year(inv, half_life_y) / SEC_PER_YEAR
               / T_AMU * N_AVOGADRO)
    burn_per_mw = fusions_per_proton(p_window_mev) * protons_per_second(1.0)
    sup_per_mw = tritium_supply_per_second(p_window_mev, 1.0)
    return decay_s / (sup_per_mw - burn_per_mw)


def tritium_surplus_g_per_year(p_beam_mw, p_window_mev=265.0,
                               f_li=F_LI_DESIGN):
    """What is left after the plant's own decay and burn are paid."""
    d, b = tritium_demand_per_second(p_window_mev, p_beam_mw)
    sup = tritium_supply_per_second(p_window_mev, p_beam_mw, f_li=f_li)
    return (sup - d - b) * SEC_PER_YEAR * T_AMU / N_AVOGADRO


def tritium_doubling_years(p_beam_mw, p_window_mev=265.0, f_li=F_LI_DESIGN):
    """Years to breed a SECOND plant's first charge out of the surplus.

    This is the fleet question and it is not the same as the self-sufficiency
    question. A plant can hold its own inventory for ever and still never
    accumulate enough to light another, because the holding is fixed by
    geometry and the surplus is what the beam buys over it.
    """
    sur = tritium_surplus_g_per_year(p_beam_mw, p_window_mev, f_li)
    if sur <= 0.0:
        return float("inf")
    return tritium_inventory_kg(p_window_mev, None) * 1000.0 / sur


def beam_mw_for_doubling(years, p_window_mev=265.0, f_li=F_LI_DESIGN):
    """The beam power at which a plant breeds a successor's charge in the
    stated time. Closed form: supply and burn are linear in P and decay is
    not, so P (sup' - burn') = inv/years + decay."""
    inv = tritium_inventory_kg(p_window_mev, None)
    decay_s = tritium_decay_g_per_year(inv) / SEC_PER_YEAR / T_AMU * N_AVOGADRO
    burn_per_mw = fusions_per_proton(p_window_mev) * protons_per_second(1.0)
    sup_per_mw = tritium_supply_per_second(p_window_mev, 1.0, f_li=f_li)
    want_s = (inv * 1000.0 / years) / T_AMU * N_AVOGADRO / SEC_PER_YEAR
    denom = sup_per_mw - burn_per_mw
    return (want_s + decay_s) / denom if denom > 0 else float("inf")


# ---- THE STATION: ONE MILLION HOUSEHOLDS, AND WHAT THAT FORCES -------------
# A module is not a plant. The fuel cell's geometry does not scale -- it is one
# muon range deep over a beam the capture field sets -- and neither does the
# production target, which has a SOURCED power its own study designed it at. So
# a station for a million households is N modules and not one big machine, and
# the module count follows from the target rather than from anything else.
#
# THE SCALE-UP THEN FORCES THE STOPPING WINDOW, which until now was free. At
# the sourced 4 MW target the 265 MeV/c window returns a tritium balance of
# 0.733 -- it does not close -- because the holding is geometric and 4 MW is
# below the 5.58 MW that window needs. The 150 MeV/c window holds 1.605 kg
# instead of 5.126 and closes at 2.11. It costs 1.884x in the fusion channel's
# own yield and only 1.067x in the total source, because the fusion channel is
# a seventh of the source; the plant gain falls from 42.70 to 40.04.
#   A choice that was optional at one module is decided at twenty.
MODULE_BEAM_MW = 4.0          # SOURCED: the target study's own design point,
                              # and machine.py's 319 kW deposition is that study
STATION_WINDOW_MEV = 150.0    # forced by the module power -- see above
STATION_HOUSEHOLDS = 1.0e6
LINAC_BEAM_MW = 20.0          # ASSUMED: 4x ESS, and four of them, because one
                              # linac of the whole station's power is not a
                              # machine anyone has proposed
# DRY COOLING IS ADOPTED IN THE DESIGN, not offered as an option, because
# environment.py cannot drive the cooling-water row below MODERATE any other
# way: once-through cooling entrains and plumes, and a tower evaporates. Air
# cooling consumes NO water and costs a share of gross output, and the module
# count absorbs the cost. This is what a mitigation looks like when it is real:
# it changes the plant, not the prose.
DRY_COOLING_PENALTY = 0.05    # SOURCED band 0.02-0.05; the conservative end


def station_beam_mw(households=STATION_HOUSEHOLDS,
                    window=STATION_WINDOW_MEV, k_eff=K_SAFE,
                    eta_acc=0.30, n_linac=None):
    """Total beam a station of this size needs. Closed form.

    net = P (G eta_th - 1/eta_acc) - n_linac S/eta_acc, so P follows directly;
    bisecting it would recompute the gain at every step for nothing.
    """
    y_s = 0.5 * sum(spallation_yield())
    g = plant_gain(k_eff, y_s, fusions_per_proton(window))
    want_kw = households * HOUSEHOLD_KW
    if n_linac is None:
        n_linac = 1.0
    denom = (g * eta_thermal() * (1.0 - DRY_COOLING_PENALTY)
             - 1.0 / eta_acc)
    if denom <= 0:
        return float("inf")
    return ((want_kw + n_linac * REF_STANDBY_KW / eta_acc) / denom) / 1000.0


def net_electric_kw_at(beam_mw, n_linac, window=STATION_WINDOW_MEV,
                       k_eff=K_SAFE, eta_acc=0.30, y_fus=None,
                       standby_kw=None):
    """Net electricity from a beam and the drivers that carry it.

    THE one statement of the plant's net. station() reads it and so does the
    driver section, because a formula written twice is a formula that will
    disagree with itself once. y_fus = 0.0 is route C -- the same plant with
    the muon channel deleted -- and None takes it from the window."""
    y_s = 0.5 * sum(spallation_yield())
    y_f = fusions_per_proton(window) if y_fus is None else y_fus
    g = plant_gain(k_eff, y_s, y_f)
    gross_kw = beam_mw * 1000.0 * g * eta_thermal()
    sb = REF_STANDBY_KW if standby_kw is None else standby_kw
    return (beam_mw * 1000.0 * (g * eta_thermal() - 1.0 / eta_acc)
            - n_linac * sb / eta_acc
            - DRY_COOLING_PENALTY * gross_kw)


def built_station(n_mod, module_mw=MODULE_BEAM_MW, window=STATION_WINDOW_MEV,
                  k_eff=K_SAFE, eta_acc=0.30, y_fus=None, linac_mw=None,
                  standby_kw=None):
    """The plant that this many modules of this size actually is.

    Separated from station() so the driver section can ask what one more
    module would deliver without restating a line of the plant. y_fus = 0.0
    builds the same plant with the muon channel deleted -- route C."""
    if n_mod < 1:
        raise ValueError(f"a station has at least one module, got {n_mod}")
    y_s = 0.5 * sum(spallation_yield())
    y_f = fusions_per_proton(window) if y_fus is None else y_fus
    g = plant_gain(k_eff, y_s, y_f)
    lin = LINAC_BEAM_MW if linac_mw is None else linac_mw
    if lin <= 0:
        raise ValueError(f"a driver has positive power, got {lin}")
    beam = n_mod * module_mw
    n_lin = math.ceil(beam / lin)
    gross_kw = beam * 1000.0 * g * eta_thermal()
    net_kw = net_electric_kw_at(beam, n_lin, window, k_eff, eta_acc, y_fus,
                                standby_kw)
    return {
        "window": window, "module_mw": module_mw, "modules": n_mod,
        "beam_mw": beam, "linacs": n_lin, "gain": g, "y_fus": y_f,
        "y_spall": y_s, "k": k_eff,
        "thermal_mw": beam * g, "net_mw": net_kw / 1000.0,
        "gross_mw": gross_kw / 1000.0,
        "dry_cooling_mw": DRY_COOLING_PENALTY * gross_kw / 1000.0,
        "households": net_kw / HOUSEHOLD_KW,
        "tritium_per_module_kg": tritium_inventory_kg(window, None),
        "tritium_total_kg": n_mod * tritium_inventory_kg(window, None),
        "tritium_ratio": tritium_balance(window, module_mw, f_li=F_LI_DESIGN),
        "doubling_y": tritium_doubling_years(module_mw, window),
        "linac_mw": lin,
        "driver_installed_mw": n_lin * lin,
        "driver_stranded_mw": n_lin * lin - beam,
        "standby_kw": (REF_STANDBY_KW if standby_kw is None else standby_kw),
    }


def station_open_loop(households=STATION_HOUSEHOLDS,
                      window=STATION_WINDOW_MEV, module_mw=MODULE_BEAM_MW,
                      k_eff=K_SAFE, eta_acc=0.30):
    """The station sized the way it was sized before the driver section.

    KEPT, and not because anything should call it: station_beam_mw() must be
    told how many drivers the answer will need BEFORE it has the answer, and
    this passes the default, ONE. A station that ends up with twelve is sized
    against a load it does not have and lands BELOW the households it was
    sized for. That is what report_driver() prices, and a finding is easier to
    hold than to describe, so the wrong sizing is kept as a function rather
    than as a paragraph."""
    need = station_beam_mw(households, window, k_eff, eta_acc)
    return built_station(math.ceil(need / module_mw), module_mw, window,
                         k_eff, eta_acc)


def station(households=STATION_HOUSEHOLDS, window=STATION_WINDOW_MEV,
            module_mw=MODULE_BEAM_MW, k_eff=K_SAFE, eta_acc=0.30,
            max_modules=100000, y_fus=None, linac_mw=None,
            standby_kw=None):
    """The station as built: whole modules, and what they actually deliver.

    Sized by closing the loop -- charging the drivers the answer needs rather
    than the one the sizing formula had to assume. It walks up from the
    open-loop figure, which is a floor and never an over-estimate.

    At the ADS convention this returns exactly what the open-loop sizing did,
    which is why the fault went unseen until the beam was 2.76x larger."""
    n = max(1, station_open_loop(households, window, module_mw, k_eff,
                                 eta_acc)["modules"])
    while n <= max_modules:
        st = built_station(n, module_mw, window, k_eff, eta_acc, y_fus,
                           linac_mw, standby_kw)
        if st["households"] >= households:
            return st
        n += 1
    raise ValueError(f"no station under {max_modules} modules meets "
                     f"{households:,.0f} households")


# ---- RE-SCALING THE STATION FOR THE ADOPTED OPERATING POINT ----------------
# MODULE_BEAM_MW = 4.0 is "the target study's own design point", and that study
# is a PION PRODUCTION target. Route C has no pion target, so the constraint
# that set the module size does not exist in the plant being built. Asking what
# replaces it is the re-scale, and the four candidates are enumerated rather
# than guessed at:
#
#   1. PION PRODUCTION TARGET POWER   gone. No pion target in route C.
#   2. CAPTURE-COIL RADIATION LIFE    gone. No capture solenoid in route C, so
#                                     buildpackage's "modularising to 4 MW
#                                     lifted the coil clear at 99.8 years" is
#                                     answering a question route C does not ask.
#   3. FUEL-CELL TRITIUM GEOMETRY     gone. No fuel cell in route C.
#   4. SPALLATION TARGET POWER        SURVIVES, and it is now the only one.
#
# So route C's module is set by what one liquid-metal spallation target can
# take, and nothing else. That is a SOURCED and narrow band, because very few
# have been built.
SPALL_TARGET_MW = {                 # beam power one target accepts
    "MEGAPIE, operated 2006": 0.78,     # SOURCED: liquid Pb-Bi, PSI
    "SNS, operating": 1.40,             # SOURCED: liquid mercury
    "ESS, design": 5.00,                # SOURCED: rotating solid tungsten
    "high-power study": 10.00,          # SOURCED band: proposed, unbuilt
}
TARGET_DEMONSTRATED_MW = 1.40       # the highest OPERATED figure above


def rescaled_station(target_mw, k_eff=None, **kw):
    """The station with the module set by the spallation target, not the pion
    target. The blanket is NOT split -- modules are targets sharing one
    blanket -- so the module count is a target count and carries no leakage
    penalty. blanket_leakage_penalty is what refuses splitting, separately."""
    if target_mw <= 0:
        raise ValueError(f"target power must be positive, got {target_mw}")
    k = K_DESIGN if k_eff is None else k_eff
    return station(module_mw=target_mw, k_eff=k, **kw)


def report_rescale():
    print()
    print("  RE-SCALING THE STATION AT THE ADOPTED OPERATING POINT")
    print()
    print(f"    k = {K_DESIGN:.3f} is adopted for intrinsic criticality safety")
    print(f"    -- {K_DESIGN_MARGIN_NOTE}. The station must be rebuilt at it,")
    print("    and the module size must be rebuilt too, because what set it")
    print("    was a PION target and route C has no pion target.")
    print()
    print("    WHAT SET THE 4 MW MODULE, AND WHETHER IT SURVIVES ROUTE C")
    print("      pion production target power    GONE -- no pion target")
    print("      capture-coil radiation life     GONE -- no capture solenoid")
    print("      fuel-cell tritium geometry      GONE -- no fuel cell")
    print("      spallation target power         SURVIVES, and is now the only")
    print("                                      constraint on module size")
    print()
    print("    THE BLANKET IS NOT SPLIT. Modules are targets feeding one")
    print("    blanket, so the module count is a TARGET count and carries no")
    print("    leakage penalty; splitting the blanket is refused separately")
    print(f"    and would cost a factor of {blanket_leakage_penalty(20):.2f}"
          " at twenty ways.")
    print()
    print("    THE STATION AT EACH TARGET POWER")
    print()
    print("      target                     MW    modules   linacs"
          "   beam MW   households")
    for label, mw in sorted(SPALL_TARGET_MW.items(), key=lambda t: t[1]):
        st = rescaled_station(mw)
        mark = "" if mw <= TARGET_DEMONSTRATED_MW else "   unbuilt"
        print(f"      {label:<24} {mw:5.2f} {st['modules']:9d}"
              f" {st['linacs']:8d} {st['beam_mw']:9.1f}"
              f" {st['households']:12,.0f}{mark}")
    print()
    base = station(k_eff=K_SAFE)
    adopted = rescaled_station(SPALL_TARGET_MW["ESS, design"])
    print(f"    Against the design as it stood -- {base['modules']} modules of"
          f" {base['module_mw']:.0f} MW at k = {K_SAFE:.2f} --")
    print(f"    the adopted point at an ESS-class target is"
          f" {adopted['modules']} modules of {adopted['module_mw']:.0f} MW.")
    at4 = rescaled_station(4.0)
    big = rescaled_station(SPALL_TARGET_MW["high-power study"])
    print(f"    The module count falls from {at4['modules']} to"
          f" {adopted['modules']}, and to {big['modules']} at a 10 MW target.")
    print()
    print("    AND THE RE-SCALE DOES NOT ABSORB WHAT THE SAFETY DECISION COST.")
    print("    That was the hope it was undertaken on and it is not what the")
    print("    arithmetic gives. The beam is")
    print(f"    {adopted['beam_mw']:.0f} MW against {base['beam_mw']:.0f} MW"
          f" -- a factor of {adopted['beam_mw']/base['beam_mw']:.2f} -- at EVERY"
          " row of the table")
    print("    above, because the beam is set by the MULTIPLICATION and the")
    print("    module size only decides how it is divided. Re-scaling changes")
    print("    the number of targets and changes nothing else.")
    print()
    print(f"    So the safety decision costs {adopted['beam_mw']/base['beam_mw']:.2f}x"
          " the driver and keeps costing it.")
    print("    What re-scaling buys is a plausible number of targets rather")
    print(f"    than {at4['modules']} of them -- a buildability gain, not an"
          " energy one.")
    print()
    print("    AND THE HONEST CAUTION: only the first two rows have been")
    print(f"    built. {TARGET_DEMONSTRATED_MW:.1f} MW is the highest spallation"
          " target ever operated,")
    print("    and every row above it is a design study. A station at the ESS")
    print("    row is betting on a target class that does not yet exist, which")
    print("    is a smaller bet than the muon channel was and is still a bet.")
    print()


def blanket_leakage_penalty(n_split):
    """What splitting one blanket into n would cost the leakage allowance.

    INDICATIVE and marked so: leakage scales with surface over volume, which
    for n equal pieces of a fixed total volume goes as n^(1/3). It is not a
    transport calculation and it is not used as one -- it is used to REFUSE the
    split, which needs only the sign and the order."""
    return n_split ** (1.0 / 3.0)


# ---- THE DRIVER ALREADY BOUGHT --------------------------------------------
# The re-scale left the module count free and said nothing about the DRIVERS,
# which come in whole machines too. Asking what the drivers are doing turns up
# a fault in the sizing rather than an optimisation.
#
#   station_beam_mw() solves net = P(G eta_th - 1/eta_acc) - n S/eta_acc for P,
#   and it must be told n -- how many drivers the answer will need -- before it
#   has the answer. station() passes the default, ONE. At the base station that
#   is nearly harmless: five drivers, four unbilled standbys, and the whole-
#   module round-up covers it. At the adopted operating point the beam is 2.76x
#   larger, the station carries TWELVE drivers, and eleven unbilled standbys is
#   36.7 MW electric -- more than the round-up returns.
#
# So the station as re-scaled lands BELOW the million households it was sized
# for. That is a finding about the sizing, not about the plant, and the plant
# is where it is answered: the drivers are bought in units of LINAC_BEAM_MW and
# the beam does not fill them, so there is installed, paid-for driver capacity
# standing idle. Filling it closes the shortfall and needs no new driver.


def driver_capacity(st):
    """Installed driver power, beam used, and what is stranded between them."""
    return (st["driver_installed_mw"], st["beam_mw"], st["driver_stranded_mw"])


def station_open_loop_rescaled(target_mw, k_eff=None, **kw):
    """The re-scaled station as the open-loop sizing had it. See
    station_open_loop() -- kept to price the fault, not to be built."""
    k = K_DESIGN if k_eff is None else k_eff
    return station_open_loop(module_mw=target_mw, k_eff=k, **kw)


def marginal_net_mw(n_mod, module_mw=MODULE_BEAM_MW,
                    window=STATION_WINDOW_MEV, k_eff=K_SAFE, eta_acc=0.30):
    """What the n-th module is worth, in net MW per MW of beam it adds.

    Returns (net MW per beam MW, whether it forces a new driver). The two
    differ because a module inside installed driver capacity pays no new
    standby and a module that crosses a driver boundary pays a whole one."""
    if n_mod < 2:
        raise ValueError(f"a marginal module is the second or later, got {n_mod}")
    lo = built_station(n_mod - 1, module_mw, window, k_eff, eta_acc)
    hi = built_station(n_mod, module_mw, window, k_eff, eta_acc)
    return ((hi["net_mw"] - lo["net_mw"]) / module_mw,
            hi["linacs"] > lo["linacs"])


def report_driver():
    """the drivers the station already owns, and what filling them is worth"""
    print()
    print("  THE DRIVER ALREADY BOUGHT")
    print()
    print("    Drivers come in whole machines of"
          f" {LINAC_BEAM_MW:.0f} MW, and the beam does not")
    print("    fill them. What is between the two is installed capacity doing")
    print("    nothing.")
    print()
    print("    THE RE-SCALED STATION AS THE OPEN-LOOP SIZING HAD IT")
    print()
    print("      target                   modules   beam MW   drivers"
          "   installed   stranded   households")
    for label, mw in sorted(SPALL_TARGET_MW.items(), key=lambda t: t[1]):
        st = station_open_loop_rescaled(mw)
        inst, beam, stray = driver_capacity(st)
        short = "" if st["households"] >= STATION_HOUSEHOLDS else "   SHORT"
        print(f"      {label:<24} {st['modules']:7d} {beam:9.1f}"
              f" {st['linacs']:9d} {inst:11.0f} {stray:10.1f}"
              f" {st['households']:12,.0f}{short}")
    print()
    print("    EVERY ROW WAS SHORT OF THE BASELINE IT WAS SIZED FOR, and the")
    print("    cause is in the sizing rather than in the plant. The beam is")
    print("    solved for before the driver count is known, so ONE driver's")
    print("    standby is charged where the answer needs twelve. Eleven")
    print(f"    unbilled standbys are"
          f" {11 * REF_STANDBY_KW / 0.30 / 1000.0:.1f} MW electric, which is more"
          " than the")
    print("    whole-module round-up returns.")
    print()
    print("    THE STATION THAT ACTUALLY MEETS THE BASELINE -- and station()")
    print("    is now sized this way, by closing the loop on the drivers it")
    print("    builds. At the ADS convention it returns exactly what the")
    print("    open-loop sizing did, which is why the fault went unseen until")
    print("    the beam was 2.76x larger.")
    print()
    print("      target                   modules   beam MW   drivers"
          "   households   new drivers")
    for label, mw in sorted(SPALL_TARGET_MW.items(), key=lambda t: t[1]):
        was = station_open_loop_rescaled(mw)
        st = rescaled_station(mw)
        extra = st["linacs"] - was["linacs"]
        print(f"      {label:<24} {st['modules']:7d} {st['beam_mw']:9.1f}"
              f" {st['linacs']:9d} {st['households']:12,.0f} {extra:13d}")
    print()
    print("    NO ROW NEEDS A NEW DRIVER. The beam that closes the shortfall")
    print("    is already installed and already paid for; what it needs is")
    print("    TARGETS, which are the cheap half of the module. At the")
    print("    ESS-class row the station that meets the baseline and the")
    print("    station that strands no capacity are the SAME station --")
    est = rescaled_station(SPALL_TARGET_MW["ESS, design"])
    was = station_open_loop_rescaled(SPALL_TARGET_MW["ESS, design"])
    print(f"    {est['modules']} modules, {est['beam_mw']:.0f} MW, twelve"
          f" drivers, {est['driver_stranded_mw']:.0f} MW stranded,")
    print(f"    {est['households']:,.0f} households against"
          f" {was['households']:,.0f}.")
    print()
    print("    WHY THE STRANDED BEAM IS THE CHEAPEST BEAM IN THE PLANT")
    print()
    inside, _ = marginal_net_mw(est["modules"], SPALL_TARGET_MW["ESS, design"],
                                k_eff=K_DESIGN)
    n_cross = est["modules"] + 1
    while not marginal_net_mw(n_cross, SPALL_TARGET_MW["ESS, design"],
                              k_eff=K_DESIGN)[1]:
        n_cross += 1
    across, _ = marginal_net_mw(n_cross, SPALL_TARGET_MW["ESS, design"],
                                k_eff=K_DESIGN)
    avg = est["net_mw"] / est["beam_mw"]
    print(f"      average over the whole station   {avg:6.3f} net MW per beam MW")
    print(f"      the module inside capacity       {inside:6.3f}")
    print(f"      the module that buys a driver    {across:6.3f}")
    print()
    print("    The marginal module beats the average because the standby is")
    print("    already paid, and the module inside installed capacity beats")
    print(f"    the one that buys a driver by {inside / across:.3f}x.")
    print()
    print("    That is the whole of the opportunity, and it is BOUNDED: it is")
    print(f"    worth exactly the {was['driver_stranded_mw']:.0f} MW that is"
          " stranded, and not one MW more.")
    print()
    print("    AND WHAT IT DOES NOT COST. Adding source neutrons does not")
    print("    change k -- k is composition, and the fuel salt is unchanged --")
    print(f"    so the subcritical margin stays"
          f" {subcritical_margin(K_DESIGN)[1]:,.0f} pcm and the always-")
    print("    subcritical property is untouched. This is the one lever in")
    print("    this work that buys output and spends no safety.")
    print()
    print("    THE CEILING IS NOT COMPUTED HERE, AND THAT IS THE FINDING.")
    print("    Net is EXACTLY linear in beam at a fixed driver count, so this")
    print("    model will hand back more output for more beam without limit.")
    print("    That is a property of the model and not of the plant. The")
    print("    blanket is NOT split -- one blanket, and splitting it is")
    print(f"    refused separately at {blanket_leakage_penalty(20):.2f}x the"
          " leakage. In thermal terms:")
    print()
    base = station(k_eff=K_SAFE)
    print(f"      the station the inventories are computed at "
          f"      {base['thermal_mw']:8,.0f} MW")
    print(f"      the station that meets the baseline at k = {K_DESIGN:.3f}"
          f" {est['thermal_mw']:8,.0f} MW"
          f"   ({est['thermal_mw'] / base['thermal_mw']:.2f}x)")
    print()
    print("    materials.py takes the station whole from station() and derives")
    print("    the salt flow, the salt inventory, the heavy-metal inventory")
    print("    and the drain tank FROM ITS THERMAL POWER -- and restart.py")
    print("    takes the decay heat from the same figure. Every one of those")
    print("    is therefore computed at the pre-decision station and is")
    print(f"    understated by {est['thermal_mw'] / base['thermal_mw']:.2f}x.")
    print()
    print("    A CORRECTION THIS SECTION OWES, AND --blanket IS WHERE IT WAS")
    print("    FOUND. This paragraph first read that factor as a factor on")
    print("    the POWER DENSITY, on the reasoning that one unsplit blanket")
    print("    taking more beam must run denser. IT DOES NOT. The blanket's")
    print("    volume is not fixed either: the inventory is flow times loop")
    print("    transit and the flow is set by the heat, so a bigger station")
    print("    holds proportionally more salt and the density does not move.")
    print("    What is understated by that factor is the INVENTORIES. See")
    print("    --blanket, which bounds the density question against published")
    print("    designs and lists what is still not computable here.")
    print()

# ---- THE DRIVER AS A MACHINE: CURRENT, LENGTH AND BEAM LOSS ---------------
# --driver asked what the drivers are DOING. This asks what they ARE, and it
# was owed before phase 4 because a station size is not achievable if its
# accelerator is not.
#
# The relation is exact and needs no model: P[MW] = I[mA] . E[GeV], since one
# milliamp through one gigavolt is one megawatt. So AT FIXED BEAM POWER THE
# CURRENT IS INVERSELY PROPORTIONAL TO THE ENERGY -- and --routes' finding
# that "the 8 GeV is bought by pion production and by nothing else" is
# therefore incomplete. The 8 GeV also buys a factor of eight OFF the current,
# and off the fractional beam loss, and that had not been counted.
PROTON_MACHINES = {                 # (energy GeV, beam power MW, status)
    "PSI HIPA cyclotron": (0.590, 1.40, "OPERATED"),   # SOURCED: highest
    "LANSCE": (0.800, 0.64, "OPERATED"),               # average proton
    "SNS, as built": (1.00, 1.40, "OPERATED"),         # current operated is
    "SNS after PPU": (1.30, 2.80, "OPERATED"),         # PSI's
    "J-PARC RCS": (3.00, 1.00, "OPERATED"),
    "MYRRHA": (0.600, 2.40, "DESIGN"),                 # SOURCED: the ADS one
    "ESS": (2.00, 5.00, "DESIGN"),
}
LOSS_W_PER_M = 1.0            # SOURCED: the hands-on-maintenance rule that
                              # sets every high-power proton linac's loss
                              # budget -- above it the machine is remote
                              # handling and a different plant
LINAC_M_PER_GEV = 300.0       # INDICATIVE: SNS is 335 m to 1.0 GeV and ESS
                              # about 600 m to 2.0 GeV. Used for the ORDER of
                              # the length and of the loss budget, never for
                              # a machine layout
ROUTE_C_GEV = 1.0             # what --routes states the route C driver at


def beam_current_ma(p_mw, e_gev):
    """P[MW] = I[mA] . E[GeV]. Exact, not a fit."""
    if e_gev <= 0:
        raise ValueError(f"beam energy must be positive, got {e_gev}")
    return p_mw / e_gev


def linac_length_m(e_gev):
    return LINAC_M_PER_GEV * e_gev


def allowed_loss_w(e_gev):
    """What the 1 W/m rule permits a machine of this energy to lose."""
    return LOSS_W_PER_M * linac_length_m(e_gev)


def fractional_loss_requirement(p_mw, e_gev):
    """The fraction of the beam that may be lost, at 1 W/m.

    LONGER IS EASIER: the allowance goes with length and the length goes with
    energy, while the power is fixed. So the high-energy machine is the
    forgiving one, which is the opposite of the intuition that made 8 GeV
    look like the expensive choice."""
    return allowed_loss_w(e_gev) / (p_mw * 1e6)


def record_current_ma(status="OPERATED"):
    """(machine, current) at the largest average proton current of that
    status. A band is not wanted here -- the question is what the record IS."""
    rows = [(n, beam_current_ma(p, e))
            for n, (e, p, st) in PROTON_MACHINES.items() if st == status]
    if not rows:
        raise ValueError(f"no machine with status {status!r}")
    return max(rows, key=lambda t: t[1])


def drivers_at_current_cap(beam_mw, e_gev, cap_ma):
    """How many drivers a station needs if no driver may exceed cap_ma."""
    if cap_ma <= 0:
        raise ValueError(f"a current cap must be positive, got {cap_ma}")
    return math.ceil(beam_mw / (cap_ma * e_gev))


def report_current():
    """the driver as a machine: current, length and the beam-loss budget"""
    print()
    print("  THE DRIVER AS A MACHINE")
    print()
    print("    P[MW] = I[mA] . E[GeV] exactly, so at fixed beam power the")
    print("    CURRENT IS INVERSELY PROPORTIONAL TO THE ENERGY. Nothing here")
    print("    had counted that, and it changes what --routes concluded.")
    print()
    print("    WHAT HAS BEEN BUILT AND WHAT HAS BEEN DESIGNED")
    print()
    print("      machine                    GeV      MW        mA   status")
    for n, (e, p, st) in sorted(PROTON_MACHINES.items(),
                               key=lambda t: -t[1][1] / t[1][0]):
        print(f"      {n:<24} {e:6.3f} {p:7.2f} {beam_current_ma(p, e):9.3f}"
              f"   {st}")
    rec_n, rec_i = record_current_ma("OPERATED")
    des_n, des_i = record_current_ma("DESIGN")
    print()
    print(f"      the record, operated  {rec_i:6.3f} mA   ({rec_n})")
    print(f"      the record, designed  {des_i:6.3f} mA   ({des_n})")
    print()
    a = station(module_mw=SPALL_TARGET_MW["ESS, design"], k_eff=K_DESIGN)
    c = station(module_mw=SPALL_TARGET_MW["ESS, design"], k_eff=K_DESIGN,
                y_fus=0.0)
    print("    THE TWO ROUTES AS ACCELERATORS")
    print()
    print("      route                        A d-t        C no muon channel")
    print(f"      driver energy               {BEAM_GEV:5.1f} GeV"
          f"          {ROUTE_C_GEV:5.1f} GeV")
    print(f"      station beam                {a['beam_mw']:5.0f} MW"
          f"           {c['beam_mw']:5.0f} MW")
    print(f"      drivers                     {a['linacs']:5d}"
          f"              {c['linacs']:5d}")
    print(f"      station current             {beam_current_ma(a['beam_mw'], BEAM_GEV):5.1f} mA"
          f"           {beam_current_ma(c['beam_mw'], ROUTE_C_GEV):5.1f} mA")
    i_a = beam_current_ma(LINAC_BEAM_MW, BEAM_GEV)
    i_c = beam_current_ma(LINAC_BEAM_MW, ROUTE_C_GEV)
    print(f"      CURRENT PER DRIVER          {i_a:5.2f} mA"
          f"           {i_c:5.2f} mA")
    print(f"        against the operated record {i_a / rec_i:6.2f}x"
          f"            {i_c / rec_i:6.2f}x")
    print(f"        against the designed one    {i_a / des_i:6.2f}x"
          f"            {i_c / des_i:6.2f}x")
    print(f"      linac length, each          {linac_length_m(BEAM_GEV):5.0f} m"
          f"            {linac_length_m(ROUTE_C_GEV):5.0f} m")
    tot_a = a["linacs"] * linac_length_m(BEAM_GEV) / 1000.0
    tot_c = c["linacs"] * linac_length_m(ROUTE_C_GEV) / 1000.0
    print(f"      linac length, all drivers   {tot_a:5.1f} km"
          f"           {tot_c:5.1f} km")
    f_a = fractional_loss_requirement(LINAC_BEAM_MW, BEAM_GEV)
    f_c = fractional_loss_requirement(LINAC_BEAM_MW, ROUTE_C_GEV)
    sns_e, sns_p, _ = PROTON_MACHINES["SNS, as built"]
    f_sns = fractional_loss_requirement(sns_p, sns_e)
    print(f"      fractional loss allowed   {f_a:8.2e}         {f_c:8.2e}")
    print(f"        against SNS's {f_sns:.2e}     {f_sns / f_a:6.2f}x tighter"
          f"      {f_sns / f_c:6.2f}x tighter")
    print("        (SNS is priced through the SAME length model, so the")
    print("         ratio is like for like and carries no claim about its")
    print("         real layout)")
    print()
    print("    SO --ROUTES IS CORRECTED, AND ON ITS OWN TERMS. It says the")
    print("    route C driver is 'SNS and MYRRHA class, machines that exist'.")
    print("    THAT IS TRUE OF THE ENERGY AND FALSE OF THE CURRENT. SNS runs")
    print(f"    {beam_current_ma(sns_p, sns_e):.2f} mA at"
          f" {sns_e:.1f} GeV; a {LINAC_BEAM_MW:.0f} MW driver at"
          f" {ROUTE_C_GEV:.0f} GeV is {i_c:.0f} mA --")
    print(f"    {i_c / rec_i:.1f}x the highest average proton current ever"
          " operated and")
    print(f"    {i_c / des_i:.1f}x the highest ever designed. The same driver at"
          f" {BEAM_GEV:.0f} GeV is")
    print(f"    {i_a:.2f} mA, which is {i_a / rec_i:.2f}x the operated record --"
          " AT it, not past it.")
    print()
    print("    AND THE BEAM-LOSS BUDGET RUNS THE SAME WAY. At 1 W/m the")
    print("    allowance goes with LENGTH and the length goes with ENERGY,")
    print("    while the power is fixed, so the high-energy machine is the")
    print(f"    forgiving one: {f_sns / f_a:.1f}x tighter than SNS at"
          f" {BEAM_GEV:.0f} GeV against"
          f" {f_sns / f_c:.0f}x at {ROUTE_C_GEV:.0f} GeV.")
    print()
    print("    WHAT ROUTE C ACTUALLY BUYS IS LENGTH, AND IT IS A LOT OF IT:")
    print(f"    {tot_c:.1f} km of linac against {tot_a:.1f} km, a factor of"
          f" {tot_a / tot_c:.1f}. That is the")
    print("    saving startcost.py already found by another route. What it")
    print("    costs is a machine nobody has built at a current nobody has")
    print("    designed for -- and the two do not cancel, because they are")
    print("    not the same kind of quantity.")
    print()
    print("    WHAT A CURRENT CAP WOULD DO TO THE DRIVER COUNT")
    print()
    print("      cap on one driver's current           route A     route C")
    for lab, cap in ((f"the operated record, {rec_i:.3f} mA", rec_i),
                     (f"the designed record, {des_i:.3f} mA", des_i)):
        na = drivers_at_current_cap(a["beam_mw"], BEAM_GEV, cap)
        nc = drivers_at_current_cap(c["beam_mw"], ROUTE_C_GEV, cap)
        print(f"      {lab:<36} {na:5d}       {nc:5d}")
    print(f"      {'none -- as designed here':<36} {a['linacs']:5d}"
          f"       {c['linacs']:5d}")
    print()
    print("    THE 20 MW DRIVER IS ONLY BUILDABLE BECAUSE OF THE 8 GeV. Held")
    print("    to a current that has been designed for, route A's driver count")
    print("    barely moves and route C's multiplies.")
    print()
    print("    AND WHAT THAT COSTS IS NOT PRICED HERE, DELIBERATELY.")
    print(f"    REF_STANDBY_KW is {REF_STANDBY_KW:,.0f} kW for a driver of"
          " UNSTATED size, inside a")
    print(f"    sourced band of {STANDBY_LO_KW:,.0f} to {STANDBY_HI_KW:,.0f}"
          " kW, and nothing here scales it with")
    print("    machine size. --driver has just shown that per-driver standby")
    print("    is a real cost -- eleven unbilled ones were 36.7 MW electric --")
    print("    so multiplying the driver count by five or by ten is a large")
    print("    term that this file cannot compute without inventing the")
    print("    scaling. RECORDED AS OWED, and owed before any route is priced")
    print("    on its accelerator count.")
    print()
    print("    THIS FILE DOES NOT DECIDE THE ROUTE ON IT. What it removes is")
    print("    the sentence that made route C's driver sound like an ordinary")
    print("    order.")
    print()

# ---- THE DRIVER RE-SCALED, THE WAY THE MODULE WAS ------------------------
# --rescale asked what sets the MODULE size and found the answer was a pion
# target route C does not have. LINAC_BEAM_MW has never been asked the same
# question: it is marked ASSUMED, "4x ESS, and four of them", and --current
# has just shown that the assumption is doing more work than that comment
# admits. So here is the same re-scale for the driver, against what proton
# linacs have actually been built, are being built, and have been studied.
#
# The sourced set is small, because very few exist:
LINAC_CLASS = {                # (energy GeV, beam power MW, status)
    "PSI HIPA, CW":            (0.590, 1.40, "OPERATED"),
    "SNS, design power":       (1.00, 1.40, "OPERATED"),
    "ESS":                     (2.00, 5.00, "BUILDING"),
    "Project X, 8 GeV upgrade": (8.00, 4.00, "STUDIED"),   # the muon-collider
    "BNL HFBR SC linac":       (1.00, 10.00, "STUDIED"),   # upgrade scenario
    "CW proton driver study":  (2.00, 15.00, "STUDIED"),   # 1.5-2.5 GeV band
}
# STANDBY IS THE TERM THIS SECTION CANNOT CLOSE, and it is worth more than
# everything else here put together. REF_STANDBY_KW is a driver's fixed
# cryogenic and rf load, sourced as a BAND for a machine of unstated size, and
# nothing anywhere states how it scales. The two ends are not close:
#   FIXED PER MACHINE      splitting the beam into more, smaller drivers
#                          multiplies the load
#   SCALING WITH THE MACHINE   the total is invariant in how it is divided
# Which it is decides whether a station of operated-class drivers works at all.


def standby_fixed(linac_mw):
    """One driver's standby if the load is a property of HAVING a machine."""
    return REF_STANDBY_KW


def standby_scaled(linac_mw):
    """One driver's standby if the load is a property of the machine's SIZE,
    referenced to the assumed 20 MW driver the band was quoted for."""
    return REF_STANDBY_KW * linac_mw / LINAC_BEAM_MW


def station_at_driver(linac_mw, scaling=standby_fixed, **kw):
    """The station rebuilt out of drivers of this power."""
    kw.setdefault("module_mw", SPALL_TARGET_MW["ESS, design"])
    kw.setdefault("k_eff", K_DESIGN)
    return station(linac_mw=linac_mw, standby_kw=scaling(linac_mw), **kw)


def standby_load_mw(st, eta_acc=0.30):
    """What the drivers draw before any beam: n . S / eta_acc, in MW."""
    return st["linacs"] * st["standby_kw"] / eta_acc / 1000.0


def report_linac():
    """the driver re-scaled against what has been built, and the term it opens"""
    print()
    print("  THE DRIVER RE-SCALED")
    print()
    print(f"    LINAC_BEAM_MW = {LINAC_BEAM_MW:.0f} MW is ASSUMED, and --current")
    print("    has shown the assumption is load-bearing. --rescale asked what")
    print("    sets the MODULE size; this asks the same of the DRIVER.")
    print()
    print("    WHAT PROTON LINACS ACTUALLY ARE")
    print()
    print("      machine                        GeV       MW        mA   status")
    for n, (e, p, st) in sorted(LINAC_CLASS.items(), key=lambda t: t[1][1]):
        print(f"      {n:<28} {e:6.3f} {p:8.2f} {beam_current_ma(p, e):9.3f}"
              f"   {st}")
    built = max(p for e, p, s in LINAC_CLASS.values() if s in ("OPERATED",))
    building = max(p for e, p, s in LINAC_CLASS.values() if s == "BUILDING")
    studied = max(p for e, p, s in LINAC_CLASS.values() if s == "STUDIED")
    at_a = max(p for e, p, s in LINAC_CLASS.values() if e >= BEAM_GEV)
    print()
    print(f"      the largest OPERATED        {built:6.2f} MW")
    print(f"      the largest BUILDING        {building:6.2f} MW")
    print(f"      the largest STUDIED         {studied:6.2f} MW")
    print(f"      the largest at {BEAM_GEV:.0f} GeV        {at_a:6.2f} MW"
          "   -- route A's own energy")
    print()
    print(f"    So the assumed {LINAC_BEAM_MW:.0f} MW driver is"
          f" {LINAC_BEAM_MW / building:.2f}x the largest under")
    print(f"    construction, {LINAC_BEAM_MW / studied:.2f}x the largest"
          " studied anywhere, and")
    print(f"    {LINAC_BEAM_MW / at_a:.2f}x the largest ever studied at the"
          " energy route A needs.")
    print()
    print("    THE STATION BUILT OUT OF EACH CLASS, AT BOTH ENDS OF THE")
    print("    STANDBY QUESTION -- and the two ends are the finding.")
    print()
    print("                 |-- standby FIXED per machine --|"
          "   |-- standby SCALED with size --|")
    print("      driver MW    drivers   beam MW   standby MWe"
          "     drivers   beam MW   standby MWe")
    rows = sorted({p for e, p, s in LINAC_CLASS.values()} | {LINAC_BEAM_MW})
    for mw in sorted(rows, reverse=True):
        f = station_at_driver(mw, standby_fixed)
        g = station_at_driver(mw, standby_scaled)
        mark = "  <- assumed" if mw == LINAC_BEAM_MW else ""
        print(f"      {mw:9.2f} {f['linacs']:10d} {f['beam_mw']:9.1f}"
              f" {standby_load_mw(f):13.1f} {g['linacs']:11d}"
              f" {g['beam_mw']:9.1f} {standby_load_mw(g):13.1f}{mark}")
    print()
    lo = station_at_driver(built, standby_scaled)
    hi = station_at_driver(built, standby_fixed)
    print("    READ THE TWO HALVES OF THAT TABLE AGAINST EACH OTHER. They are")
    print("    the same plant. The only difference is an assumption nobody has")
    print("    written down. At a driver of the largest power ever OPERATED,")
    print(f"    {built:.1f} MW, the standby load is"
          f" {standby_load_mw(lo):.0f} MW electric at one end and")
    print(f"    {standby_load_mw(hi):.0f} MW at the other -- against a station"
          f" that nets about")
    print(f"    {station_at_driver(LINAC_BEAM_MW)['net_mw']:,.0f} MW. THE"
          " DIFFERENCE IS COMPARABLE TO THE WHOLE OUTPUT.")
    print()
    print("    AND IT DECIDES WHETHER THAT STATION EXISTS. With the load fixed")
    print("    per machine, a station built out of drivers that have actually")
    print(f"    been operated needs {hi['beam_mw']:.0f} MW of beam against"
          f" {lo['beam_mw']:.0f} -- a factor of")
    print(f"    {hi['beam_mw'] / lo['beam_mw']:.2f} -- because every driver"
          " added to carry the beam brings a")
    print("    load the beam must then carry. With the load scaling, the")
    print("    division is free and the beam does not move at all.")
    print()
    print("    THIS IS NOW THE LARGEST UNPRICED TERM IN THE PLANT, and it was")
    print("    invisible while the driver size was assumed. --current recorded")
    print("    it as owed; this prices what being owed it costs. WHAT WOULD")
    print("    SETTLE IT IS ONE NUMBER FROM AN OPERATING MACHINE: the fixed")
    print("    cryogenic and rf load of a superconducting proton linac, stated")
    print("    beside that machine's beam power. It is an ordinary operating")
    print("    quantity at every facility in the table above, and this work")
    print("    has not found it published in any usable form.")
    print()
    print("    UNTIL IT IS, THE DRIVER SIZE IS NOT A FREE CHOICE AND MUST NOT")
    print("    BE TREATED AS ONE. The design keeps its assumed"
          f" {LINAC_BEAM_MW:.0f} MW driver")
    print("    because changing it would be choosing an answer to the question")
    print("    above rather than measuring it -- and the assumption is now")
    print("    recorded with its consequence rather than carried silently.")
    print()

# ---- THE BLANKET CEILING, BOUNDED --------------------------------------
# --driver recorded that nothing here computes a maximum blanket power
# density, so nothing could say where adding beam stops paying. That is no
# longer quite true: the quantity is not computable here, but it is BOUNDED,
# because liquid-fuel fast reactors have been designed and their power
# densities are published. A bound with its basis stated is worth more than
# an open item.
#
# THE BASIS MATTERS AND IS THE EASIEST THING TO GET WRONG. A power density
# quoted over the CORE is not the same number as one quoted over the whole
# fuel CIRCUIT, and they differ by the fraction of the salt that is in the
# core -- about half, in the one design that publishes both. This file's own
# figure is a CIRCUIT figure, because materials.py sizes the inventory from
# the loop transit and states no core volume. So the comparison is made
# against circuit figures only, and the core rows are printed for scale and
# explicitly not compared.
POWER_DENSITY_REF = {           # (thermal MW, salt volume m3, basis, status)
    "MSFR, whole fuel circuit": (3000.0, 18.0, "CIRCUIT", "DESIGN"),
    "MSFR, core only":          (3000.0, 9.0, "CORE", "DESIGN"),
    "MCFR, optimised":          (2500.0, 25.0, "CORE", "DESIGN"),
}
MSRE_DECAY_FRACTION = 0.0100    # SOURCED: 100 kW of decay power on a 10 MW
                                # reactor at 1.5 hours -- a published MSR
                                # figure, and the only one this work has found
                                # that its own decay model can be checked on
MSRE_DECAY_T_S = 5400.0
DRACS_MW = 2.36                 # SOURCED: the passive decay-heat system, at
                                # the largest capacity found stated for one


def power_density_mw_m3(thermal_mw, volume_m3):
    if volume_m3 <= 0:
        raise ValueError(f"a volume is positive, got {volume_m3}")
    return thermal_mw / volume_m3


def salt_litres_per_mw(thermal_mw, volume_m3):
    """The same quantity the other way up, which is how an inventory is felt."""
    return 1000.0 * volume_m3 / thermal_mw


def _mat_mod():
    sys.path.insert(0, HERE)
    import materials as X
    return X


def blanket_density(st=None):
    """(thermal MW, circuit volume m3, MW/m3) for a station of ours.

    The volume scales with the thermal power, because materials.py sizes the
    inventory as flow x loop transit and the flow is set by the heat. So the
    density is the SAME at every station size, and that is the first half of
    the answer: adding beam does not make this plant denser."""
    X = _mat_mod()
    ref = X.ref()
    th = ref["thermal_mw"] if st is None else st["thermal_mw"]
    vol = X.salt_volume_m3() * th / ref["thermal_mw"]
    return th, vol, power_density_mw_m3(th, vol)


def beam_headroom_to(reference="MSFR, whole fuel circuit"):
    """How much more beam before this plant is as dense as a published one."""
    mw, vol, basis, _st = POWER_DENSITY_REF[reference]
    if basis != "CIRCUIT":
        raise ValueError(f"{reference!r} is a {basis} figure and this plant's"
                         " is a CIRCUIT figure; the two are not comparable")
    return power_density_mw_m3(mw, vol) / blanket_density()[2]


def decay_removal_duty_mw(st, t_s=3600.0):
    sys.path.insert(0, HERE)
    import restart as R
    return R.decay_fraction(t_s) * st["thermal_mw"]


def report_blanket():
    """the ceiling --driver left open, bounded against published designs"""
    sys.path.insert(0, HERE)
    import restart as R
    print()
    print("  THE BLANKET CEILING, BOUNDED")
    print()
    print("    --driver recorded that nothing here computes a maximum blanket")
    print("    power density, so nothing could say where adding beam stops")
    print("    paying. The quantity is still not computable here. It is")
    print("    BOUNDED, though, because liquid-fuel fast reactors have been")
    print("    designed and their power densities are published.")
    print()
    print("    FIRST, THE BASIS, WHICH IS THE EASIEST THING TO GET WRONG.")
    print("    A density over the CORE is not a density over the whole fuel")
    print("    CIRCUIT; in the one design that publishes both they differ by")
    print("    two, which is the fraction of the salt in the core. This")
    print("    plant's figure is a CIRCUIT figure, because materials.py sizes")
    print("    the inventory from the loop transit and states NO CORE VOLUME.")
    print()
    print("      reference                     MWth      m3     MW/m3   basis")
    for n, (mw, v, basis, stt) in sorted(POWER_DENSITY_REF.items(),
                                         key=lambda t: t[1][0] / t[1][1]):
        note = "" if basis == "CIRCUIT" else "   not compared"
        print(f"      {n:<28} {mw:7.0f} {v:7.1f} {power_density_mw_m3(mw, v):9.1f}"
              f"   {basis}{note}")
    base = station(k_eff=K_SAFE)
    fill = station(module_mw=SPALL_TARGET_MW["ESS, design"], k_eff=K_DESIGN)
    for lab, st in (("this plant, pre-decision", base),
                    ("this plant, baseline-meeting", fill)):
        th, vol, d = blanket_density(st)
        print(f"      {lab:<28} {th:7.0f} {vol:7.1f} {d:9.1f}   CIRCUIT")
    print()
    print("    AND THE FIRST HALF OF THE ANSWER IS THAT THE DENSITY DOES NOT")
    print("    MOVE. The inventory is flow times loop transit and the flow is")
    print("    set by the heat, so a bigger station holds proportionally more")
    print("    salt. Adding beam does not make this plant denser -- it makes")
    print("    it bigger.")
    print()
    hr = beam_headroom_to()
    print(f"    Against the one CIRCUIT figure published, the headroom is"
          f" {hr:.2f}x")
    print("    in thermal power at equal salt. THAT IS NOT A LICENCE TO SPEND")
    print("    IT. The headroom exists because this plant holds")
    th, vol, d = blanket_density(fill)
    ms_mw, ms_v, _b, _s = POWER_DENSITY_REF["MSFR, whole fuel circuit"]
    print(f"    {salt_litres_per_mw(th, vol):.1f} litres of salt per MW against"
          f" {salt_litres_per_mw(ms_mw, ms_v):.1f}, and that is bought")
    print(f"    by an ASSUMED {_mat_mod().SALT_RESIDENCE_S:.0f} s loop transit."
          " Shorten the transit and the")
    print("    inventory falls and the density rises in exact proportion. So")
    print("    the headroom is a property of an assumption, not of a design,")
    print("    and it may not be quoted as margin.")
    print()
    print("    SECOND, THE DECAY HEAT, AND HERE THE MODEL CAN BE CHECKED.")
    print()
    print(f"      MSRE, published        {100 * MSRE_DECAY_FRACTION:6.3f} %"
          f" of full power at {MSRE_DECAY_T_S / 3600.0:.1f} h")
    got = R.decay_fraction(MSRE_DECAY_T_S)
    print(f"      this model returns     {100 * got:6.3f} %"
          f"   -- agreeing to {got / MSRE_DECAY_FRACTION:.3f}")
    print()
    print("    That is the Wigner-Way constants checked against a PUBLISHED")
    print("    molten-salt reactor figure by a route that shares nothing with")
    print("    it, and it is the only such check this work has found.")
    print()
    print("    THE TRANSIENT IS INVARIANT IN BEAM POWER, and that is the")
    print("    second half of the answer. The decay heat goes as the power and")
    print("    the salt mass goes as the power, so the adiabatic rise --")
    print(f"    restart.py's {R.adiabatic_rise_k(3600.0):.0f} K in the first"
          " hour -- is the SAME at every")
    print("    station size. A bigger station does not have a worse transient.")
    print("    It has a bigger duty:")
    print()
    for lab, st in (("pre-decision station", base),
                    ("baseline-meeting station", fill)):
        duty = decay_removal_duty_mw(st)
        print(f"      {lab:<26} {duty:7.1f} MW at 1 h"
              f"   = {duty / DRACS_MW:5.1f} passive systems")
    print()
    print(f"    A passive residual-heat system is sourced at"
          f" {DRACS_MW:.2f} MW. The duty here is")
    print(f"    {decay_removal_duty_mw(fill) / DRACS_MW:.0f} times one, so"
          " decay-heat removal is ACTIVE and large, which")
    print("    restart.py already says in its own words -- the plant cannot be")
    print("    walked away from. This states the size of what cannot be walked")
    print("    away from.")
    print()
    print("    WHAT IS STILL NOT COMPUTABLE HERE, AND IS NOW A SHORT LIST")
    print("    RATHER THAN AN OPEN QUESTION:")
    print("      the CORE volume, and so the core power density, which needs a")
    print("        geometry this work does not have")
    print("      the coolant velocity, pumping power and erosion limit, which")
    print("        need that geometry too")
    print("      the structural damage limit at the flux the blanket runs at")
    print("    None of the three is bounded by anything published, because")
    print("    each is a property of a design rather than of a class.")
    print()

WORLD_CIVIL_TRITIUM_KG = 25.0   # SOURCED band: the heavy-water reactor stock


def staged_charge(stock_kg=WORLD_CIVIL_TRITIUM_KG, **kw):
    """Commissioning a station whose first charge exceeds the world's stock.

    Modules do not all start together. Charge as many as the stock allows,
    run them, and let their surplus charge the rest -- which is not a
    workaround but the natural build order, since a module earns from its
    first day and the station is modular anyway.

    Returns (modules charged from stock, years to charge the remainder).
    """
    st = station(**kw)
    inv = st["tritium_per_module_kg"]
    sur = tritium_surplus_g_per_year(st["module_mw"], st["window"])
    n0 = int(stock_kg / inv)
    if n0 >= st["modules"]:
        return st["modules"], 0.0
    if sur <= 0.0:
        return n0, float("inf")
    bank_g = (stock_kg - n0 * inv) * 1000.0
    n, years = n0, 0.0
    while n < st["modules"]:
        need = inv * 1000.0 - bank_g
        years += need / (n * sur)
        bank_g = 0.0
        n += 1
    return n0, years


def station_doubling_years(stock=None, **kw):
    """Years for a finished station to breed a whole successor's charge."""
    st = station(**kw)
    sur = st["modules"] * tritium_surplus_g_per_year(st["module_mw"],
                                                     st["window"])
    if sur <= 0.0:
        return float("inf")
    return st["tritium_total_kg"] * 1000.0 / sur


def report_station():
    """One million households: what it is, and what the scale-up forces."""
    st = station()
    print("  THE STATION -- ONE MILLION HOUSEHOLDS")
    print()
    print("    A module is not a plant, and the difference is geometric. The")
    print("    fuel cell is one muon range deep over a beam the capture field")
    print("    sets, so its tritium holding does not scale with power; and the")
    print("    production target has a SOURCED power its own study designed it")
    print("    at. A station is therefore N modules, and N follows from the")
    print("    target rather than from any choice made here.")
    print()
    print("    THE SCALE-UP FORCES THE STOPPING WINDOW, which was free until now")
    print()
    print("      window   holding   threshold   ratio at   plant   beam for 1M")
    print("      MeV/c      kg       MW beam    a module    gain      MW")
    y_s = 0.5 * sum(spallation_yield())
    for w in (150.0, 200.0, 265.0):
        g = plant_gain(K_SAFE, y_s, fusions_per_proton(w))
        mark = "  <-- forced" if w == STATION_WINDOW_MEV else ""
        print(f"      {w:5.0f} {tritium_inventory_kg(w, None):9.3f}"
              f" {beam_mw_for_tritium(w, f_li=F_LI_DESIGN):10.2f}"
              f" {tritium_balance(w, MODULE_BEAM_MW, f_li=F_LI_DESIGN):11.3f}"
              f" {g:8.2f} {station_beam_mw(window=w):9.2f}{mark}")
    print()
    print(f"    At the sourced {MODULE_BEAM_MW:.0f} MW target the 265 MeV/c window"
          " does NOT close on")
    print("    tritium and the 150 MeV/c window closes with margin. The cost is")
    lo = _mach().delivered_eta_window(1.50, 150.0)
    hi = _mach().delivered_eta_window(1.50, 265.0)
    print(f"    {hi/lo:.3f}x in the fusion channel's own yield and only"
          f" {plant_gain(K_SAFE, y_s, fusions_per_proton(265.0))/st['gain']:.3f}x in")
    print("    the plant, because the fusion channel is a seventh of the source.")
    print("    A CHOICE THAT WAS OPTIONAL AT ONE MODULE IS DECIDED AT TWENTY.")
    print()
    print("    THE STATION")
    print(f"      modules                        {st['modules']:8.0f}"
          f"   of {st['module_mw']:.0f} MW each")
    print(f"      gross electric                 {st['gross_mw']:8.0f} MW")
    print(f"      dry-cooling penalty            {st['dry_cooling_mw']:8.0f} MW"
          f"   {100*DRY_COOLING_PENALTY:.0f} %, and it is ADOPTED:")
    print("                                                 zero water, and the"
          " module")
    print("                                                 count absorbs the"
          " cost")
    print(f"      total beam                     {st['beam_mw']:8.1f} MW")
    print(f"      driver linacs                  {st['linacs']:8.0f}"
          f"   at {LINAC_BEAM_MW:.0f} MW, ASSUMED")
    print(f"      blanket multiplication k       {st['k']:8.3f}")
    print(f"      plant gain G                   {st['gain']:8.2f}")
    print(f"      thermal                        {st['thermal_mw']:8.0f} MW")
    print(f"      net electric                   {st['net_mw']:8.0f} MW")
    print(f"      households                     {st['households']:8,.0f}")
    print(f"      tritium, per module            "
          f"{st['tritium_per_module_kg']:8.3f} kg")
    print(f"      tritium, whole station         "
          f"{st['tritium_total_kg']:8.2f} kg")
    print(f"      tritium balance, per module    {st['tritium_ratio']:8.3f}")
    print(f"      doubling time                  {st['doubling_y']:8.1f} yr")
    print()
    print("    THE BALANCE IS SCALE-INVARIANT UNDER REPLICATION, and that is")
    print("    why modularity is free here: a module's holding and a module's")
    print("    share of the neutron economy both scale with N, so the ratio")
    print("    does not move. Twenty modules is twenty times a solved problem")
    print("    rather than one twenty-times-harder problem.")
    print()
    print("    ONE BLANKET, NOT TWENTY. Leakage goes as surface over volume, so")
    print(f"    splitting the blanket {st['modules']:.0f} ways multiplies it by"
          f" {blanket_leakage_penalty(st['modules']):.2f} --")
    n_split = blanket_leakage_penalty(st["modules"]) * LEAK_PARASITIC_HI
    print(f"    an L of {n_split:.2f} where the budget allows"
          f" {LEAK_PARASITIC_HI:.2f}, at which the free")
    print(f"    neutrons per source are"
          f" {free_neutrons_per_source(K_SAFE, n_split):.3f} and the tritium")
    print("    balance has nothing to breed with. The estimate is INDICATIVE")
    print("    and is used only to refuse the split, which needs the sign and")
    print("    the order and not a transport calculation.")
    print()
    print("    THE FIRST CHARGE EXCEEDS THE WORLD'S TRITIUM, AND THE STATION")
    print("    IS BUILT ANYWAY -- BY STAGING IT.")
    n0, yrs = staged_charge()
    print(f"      station's cells need           {st['tritium_total_kg']:8.1f} kg")
    print(f"      world civil stock, order       {WORLD_CIVIL_TRITIUM_KG:8.1f} kg"
          "   SOURCED band")
    print(f"      modules the stock charges      {n0:8.0f}   of"
          f" {st['modules']:.0f}")
    print(f"      surplus per running module     "
          f"{tritium_surplus_g_per_year(st['module_mw'], st['window']):8.1f} g/yr")
    print(f"      years to charge the rest       {yrs:8.2f}")
    print()
    print("      A module earns from its first day and the station is modular")
    print("      already, so charging it in stages is the natural build order")
    print("      rather than a way round a shortage. The station reaches full")
    print(f"      power in year {yrs:.1f} and is self-supplying from then on.")
    print()
    print("      THE FLEET IS WHAT THIS BINDS, NOT THE STATION. A finished")
    print(f"      station breeds a successor's whole charge in"
          f" {station_doubling_years():.1f} years,")
    print("      so a fleet doubles on that timescale and no faster. That is a")
    print("      DEPLOYMENT rate, it is recorded rather than repaired, and it")
    print("      is the same number as one module's doubling because the")
    print("      balance is scale-invariant.")
    print()
    print("    WHAT THE DRIVER COSTS, AND IT IS THE HARD PART")
    print(f"      {st['beam_mw']:.0f} MW of {8.0:.0f} GeV protons is"
          f" {st['beam_mw']/5.0:.0f}x the largest machine of its")
    print("      class now building. THE REACTOR IS NOT WHAT MAKES A MILLION")
    print("      HOUSEHOLDS HARD; THE ACCELERATOR IS. Against that, the driver's")
    print("      standby load -- which set the FLOOR on plant size at one")
    print(f"      module -- is now {100*st['linacs']*REF_STANDBY_KW/0.30/(st['net_mw']*1000):.2f} %"
          " of the output and has stopped mattering.")
    print()
    print("    WHAT RELAXING k WOULD BUY, RECORDED AND NOT ADOPTED")
    print("      k       margin      G      beam for 1M households")
    for k in (0.95, 0.96, 0.97, 0.98, 0.99):
        g = plant_gain(k, y_s, fusions_per_proton(STATION_WINDOW_MEV))
        print(f"      {k:.2f} {subcritical_margin(k)[1]:9,.0f} pcm"
              f" {g:8.2f} {station_beam_mw(k_eff=k):14.2f} MW")
    print()
    print(f"    k = {K_SAFE:.2f} is held. The project's third criterion is")
    print("    STABILITY, the margin at 0.95 is a whole fast core's control")
    print("    worth, and buying a smaller accelerator with it would be buying")
    print("    the one property the device is for. The trade is stated so that")
    print("    a reader can see what is being declined, not so it can be taken.")


# ---- STARTING ONE: THREE PROBLEMS WITH THREE DIFFERENT ANSWERS ------------
# "Ignition" names nothing here. The device has no threshold to cross and no
# burning state to reach; it starts when the beam starts. What a station
# actually needs before it runs is three separate things, and they are usually
# run together under one word because in a tokamak they would be one thing.
#
#   1. ELECTRICITY to run the driver before the plant makes any. Ordinary,
#      hours long, and a neighbouring station supplies it easily.
#   2. TRITIUM for the cells. Bred, and a neighbour supplies it -- slowly.
#   3. FISSILE for the blanket. THIS IS THE ONE THAT BINDS, and it is the one
#      the design cannot solve from its own output, because f_b = k/(nu-k) is
#      a BREAK-EVEN condition: it was chosen to hold k, not to make surplus.
#
# The neutron budget does leave something over -- what is not spent on fission,
# on break-even breeding, on leakage and on Li-6 can go to EXTRA fertile
# capture, which is surplus fissile. But the resulting doubling time is decades
# to more than a century, against 15 years on tritium, so a fleet does not grow
# on its own fissile. It grows on a stockpile, and there is one.
WORLD_CIVIL_PU_T = 560.0     # SOURCED band: separated civil plutonium, IPFM order
SPENT_FUEL_PU_T = 4000.0     # SOURCED order: Pu in world spent fuel, unseparated
FISSILE_FRACTION = (0.12, 0.20)   # ASSUMED band: fissile share of heavy metal
                                  # for a fast chloride at k = 0.95. A transport
                                  # result this work does not compute, so the
                                  # charge and the doubling are stated as a BAND
ETA_ACC_START = 0.30         # wall plug to beam, the same figure the loop uses


def start_wall_power_mw(eta_acc=ETA_ACC_START, **kw):
    """What must come from outside to run the drivers before the plant runs."""
    return station(**kw)["beam_mw"] / eta_acc


def stations_startable(eta_acc=ETA_ACC_START, **kw):
    """How many neighbours one running station could start at once."""
    return station(**kw)["net_mw"] / start_wall_power_mw(eta_acc, **kw)


def tritium_per_source_neutron(**kw):
    """The station's tritium demand expressed in the blanket's own currency."""
    st = station(**kw)
    d, b = tritium_demand_per_second(st["window"], st["module_mw"])
    src = ((st["y_spall"] + st["y_fus"])
           * protons_per_second(st["module_mw"]))
    return (d + b) / src / F_LI_DESIGN


def breeding_ratio_available(leak=LEAK_PARASITIC_HI, k_eff=K_SAFE, **kw):
    """Fissile bred per fissile fissioned, once tritium is paid for.

    Break-even is 1.000 by construction -- f_b = k/(nu-k) was chosen to hold k.
    Anything above it is surplus, and it is what a fleet would have to grow on.
    """
    f = fissions_per_source(k_eff)
    extra = free_neutrons_per_source(k_eff, leak) - tritium_per_source_neutron(**kw)
    return (f + extra) / f


def fissile_surplus_kg_per_year(burnup_kg_yr, leak=LEAK_PARASITIC_HI, **kw):
    return (breeding_ratio_available(leak, **kw) - 1.0) * burnup_kg_yr


def fissile_charge_t(hm_holding_t, fraction):
    return hm_holding_t * fraction


def fissile_doubling_years(hm_holding_t, burnup_kg_yr, fraction,
                           leak=LEAK_PARASITIC_HI, **kw):
    sur = fissile_surplus_kg_per_year(burnup_kg_yr, leak, **kw)
    if sur <= 0.0:
        return float("inf")
    return fissile_charge_t(hm_holding_t, fraction) * 1000.0 / sur


def stations_from_stock(hm_holding_t, fraction, stock_t=WORLD_CIVIL_PU_T):
    return stock_t / fissile_charge_t(hm_holding_t, fraction)


def min_k_for_loop(eta_acc=ETA_ACC_START, **kw):
    """The lowest multiplication at which the loop still closes.

    A station could be lit at a smaller charge and bred up -- this says how
    much smaller it could be before it stops being a power source at all.
    """
    st = station(**kw)
    req = loop_requirement(eta_acc)
    lo, hi = 0.05, K_SAFE
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        if plant_gain(mid, st["y_spall"], st["y_fus"]) < req:
            lo = mid
        else:
            hi = mid
    return hi


def report_ignition():
    """Starting one: electricity, tritium and fissile, and which one binds."""
    st = station()
    sys.path.insert(0, HERE)
    import materials as X
    hm_t = X.heavy_metal_inventory_kg() / 1000.0
    burn = X.burnup_kg_per_year()
    print("  STARTING A STATION")
    print()
    print("    'IGNITION' NAMES NOTHING HERE. The device has no threshold to")
    print("    cross and no burning state to reach; it starts when the beam")
    print("    starts and stops when the beam stops, which is the same fact")
    print("    that makes it stable. What a station needs before it runs is")
    print("    THREE separate things, and they have three different answers.")
    print("    They get run together under one word because in a tokamak they")
    print("    would be one thing. Here they are not.")
    print()
    print("    1. ELECTRICITY -- SOLVED, AND A NEIGHBOUR SUPPLIES IT")
    print(f"       drivers need           {start_wall_power_mw():8.0f} MW at the wall")
    print(f"       station sells          {st['net_mw']:8.0f} MW")
    print(f"       so one station starts  {stations_startable():8.2f} others at once")
    print()
    print("       This is ordinary. Every thermal station takes house power to")
    print("       start and this one takes more of it, for hours, until the")
    print("       blanket is at power. A grid connection does it; a neighbouring")
    print("       station does it with a fifth of its output; and after that the")
    print("       station takes no electricity at all, for ever.")
    print()
    print("    2. TRITIUM -- SOLVED, AND A NEIGHBOUR SUPPLIES IT SLOWLY")
    n0, yrs = staged_charge()
    print(f"       station's cells need   {st['tritium_total_kg']:8.1f} kg")
    print(f"       world civil stock      {WORLD_CIVIL_TRITIUM_KG:8.1f} kg"
          "    SOURCED band")
    print(f"       staged: {n0:.0f} modules from stock, the rest bred, full power")
    print(f"       in year {yrs:.1f}. A finished station breeds a successor's")
    print(f"       whole charge in {station_doubling_years():.1f} years.")
    print()
    print("    3. FISSILE -- NOT SOLVED FROM THE PLANT'S OWN OUTPUT, AND THIS")
    print("       IS THE ONE THAT BINDS.")
    print()
    print("       f_b = k/(nu-k) is a BREAK-EVEN condition. It was chosen to")
    print("       HOLD k, not to make surplus, so on the design point a station")
    print("       breeds exactly what it burns and no more. What the budget has")
    print("       left over after fission, break-even breeding, leakage and")
    print("       Li-6 CAN go to extra fertile capture -- but not much of it:")
    print()
    print("         leak    free for Li-6   tritium takes   left for surplus"
          "   BR")
    for L in (LEAK_PARASITIC_LO, LEAK_PARASITIC_HI):
        free = free_neutrons_per_source(K_SAFE, L)
        t = tritium_per_source_neutron()
        print(f"         {L:.2f} {free:14.3f} {t:15.3f} {free-t:18.3f}"
              f" {breeding_ratio_available(L):6.3f}")
    print()
    print(f"       At {burn/1000.0:.3f} t/yr fissioned that is a fissile surplus of")
    print(f"       {fissile_surplus_kg_per_year(burn, LEAK_PARASITIC_HI):.0f}"
          f" to {fissile_surplus_kg_per_year(burn, LEAK_PARASITIC_LO):.0f}"
          " kg a year, against a first charge of:")
    print()
    print("         fissile share   charge      doubling, high leak   low leak")
    for ff in (FISSILE_FRACTION[0], 0.16, FISSILE_FRACTION[1]):
        print(f"         {100*ff:11.0f} % {fissile_charge_t(hm_t, ff):9.1f} t"
              f" {fissile_doubling_years(hm_t, burn, ff, LEAK_PARASITIC_HI):19.1f} yr"
              f" {fissile_doubling_years(hm_t, burn, ff, LEAK_PARASITIC_LO):10.1f} yr")
    print()
    print("       (the fissile share is an ASSUMED band -- a transport result")
    print("        this work does not compute -- so the charge and the doubling")
    print("        are a band and not a number.)")
    print()
    print("       AGAINST 15.0 YEARS ON TRITIUM, THAT IS THE FLEET'S REAL LIMIT.")
    print("       A station cannot light its successor's fissile charge inside")
    print("       its own life on the high-leak budget, and only barely on the")
    print("       low one. So a fleet does not grow on its own fissile.")
    print()
    print("    IT GROWS ON A STOCKPILE, AND THERE IS ONE -- THE SAME SHAPE OF")
    print("    ANSWER AS THE FUEL. Separated civil plutonium is a material the")
    print("    world has already made, already paid for, and is paying to guard.")
    print()
    print(f"      separated civil Pu, world  {WORLD_CIVIL_PU_T:8.0f} t"
          "    SOURCED band")
    print(f"      stations it charges        "
          f"{stations_from_stock(hm_t, FISSILE_FRACTION[1]):8.0f} to"
          f" {stations_from_stock(hm_t, FISSILE_FRACTION[0]):.0f}")
    print(f"      Pu in world spent fuel     {SPENT_FUEL_PU_T:8.0f} t"
          "    SOURCED order, unseparated")
    print(f"      stations that would charge "
          f"{stations_from_stock(hm_t, FISSILE_FRACTION[1], SPENT_FUEL_PU_T):8.0f} to"
          f" {stations_from_stock(hm_t, FISSILE_FRACTION[0], SPENT_FUEL_PU_T):.0f}")
    print()
    print("      So the first charge is a SAFEGUARDED ACQUISITION and stays one.")
    print("      What changes is what it is FOR: separated civil plutonium has")
    print("      no use anyone is willing to pay for, is a proliferation")
    print("      liability by simply existing, and is consumed permanently by")
    print("      this station rather than stored. The fleet's growth rate is")
    print("      then set by reprocessing capacity and by policy, not by")
    print("      physics -- which is a different kind of limit and should not")
    print("      be reported as the same one.")
    print()
    print("    COULD A STATION START SMALLER AND BREED UP? A little, and it is")
    print("    recorded rather than used.")
    kmin = min_k_for_loop()
    print(f"      the loop still closes down to k = {kmin:.3f}")
    print(f"        (G there is {plant_gain(kmin, st['y_spall'], st['y_fus']):.2f}"
          f" against G_req {loop_requirement(ETA_ACC_START):.2f})")
    print(f"      at first order the charge goes with k, so that saves"
          f" {100*(1-kmin/K_SAFE):.0f} %")
    print(f"      and costs {plant_gain(K_SAFE, st['y_spall'], st['y_fus'])/plant_gain(kmin, st['y_spall'], st['y_fus']):.1f}x"
          " in output while it breeds up.")
    print("      A fifth off the charge for four fifths off the power is not a")
    print("      lever. The charge is what it is.")


# ---- THE ROUTE DECISION, AND ONE CORRECTION IT FORCES ---------------------
# Two decisions have been taken and are recorded here rather than argued:
#
#   FERTILE: uranium, with seawater uranium as the replacement when the tails
#            and the spent fuel are gone. Thorium is REFUSED -- see
#            materials.py --fertile for why it was a live option and what
#            refusing it costs, which is nothing.
#   FUSION:  no longer mandatory. The criterion is now "cleaner and more
#            efficient", and the muon channel must earn its place against it
#            like anything else.
#
# THE CORRECTION FIRST, BECAUSE IT REVERSES A COMPARISON THIS FILE'S OWN
# NEIGHBOUR MADE. environment.py --tradeoff priced the three routes on BEAM
# POWER and found the deuterium route and the no-channel route within 0.001 of
# each other -- 1.080x against 1.081x. That is true and it is not the whole
# cost, because THE MACHINE IS NOT THE BEAM POWER. Below is the term that was
# missing, and it changes which route is preferable.
#
# For a pure spallation plant the gain is EXACTLY INVARIANT IN BEAM ENERGY:
#
#     y_s = n_per_GeV . E        (yield per GeV DEPOSITED is a flat material
#                                 property -- see --target)
#     G   = (1000 E + y_s . E_k) / (1000 E)
#         = 1 + n_per_GeV . E_k / 1000                    -- E cancels
#
# so a 0.6 GeV driver and a 12 GeV driver give the same G. THE 8 GeV IS BOUGHT
# BY PION PRODUCTION AND BY NOTHING ELSE: HARP's own columns make 3 GeV/c
# 1.63x dearer per pion than 8. Delete the muon channel and the driver drops to
# about 1 GeV -- SNS and MYRRHA class ON ENERGY ONLY; --current corrects the
# "machines that exist" reading, because at that energy the same beam power is
# eight times the current -- and 21 capture
# solenoids, 42 km of REBCO and every fuel cell go with it.
ROUTES = ("A d-t", "B d-d self-tritiating", "C no muon channel")


def gain_invariant_in_energy(e_gev, n_per_gev=None, k_eff=K_SAFE):
    """Pure-spallation plant gain at a stated beam energy. Constant in e_gev,
    and the selftest asserts that rather than trusting the algebra."""
    npg = (0.5 * sum(spallation_yield()) / BEAM_GEV if n_per_gev is None
           else n_per_gev)
    y_s = npg * e_gev
    e_mev = 1000.0 * e_gev
    return (e_mev + y_s * energy_per_source_neutron(k_eff)) / e_mev


def route_table(**kw):
    """(name, y_fus, source share, G, gain over route C, station tritium kg)."""
    sys.path.insert(0, HERE)
    import materials as X
    import window as W
    st = station(**kw)
    m = _mach()
    _f1, _f2, _ct, _nc, _e, n_per_mu, m_t = W.selftritiation()
    y_dd = (PI_PER_PROTON * m.delivered_eta_window(1.50, st["window"])
            * n_per_mu)
    g_c = plant_gain(K_SAFE, st["y_spall"], 0.0)
    rows = []
    for name, y_f, trit in (
            (ROUTES[0], st["y_fus"], st["tritium_total_kg"]),
            (ROUTES[1], y_dd, st["tritium_total_kg"] * m_t / 0.600),
            (ROUTES[2], 0.0, 0.0)):
        g = plant_gain(K_SAFE, st["y_spall"], y_f)
        rows.append((name, y_f, y_f / (st["y_spall"] + y_f), g, g / g_c - 1.0,
                     trit))
    return rows


def breeding_without_tritium(leak=LEAK_PARASITIC_HI, **kw):
    """Route C frees the whole Li-6 share back to fertile capture."""
    f = fissions_per_source(K_SAFE)
    return (f + free_neutrons_per_source(K_SAFE, leak)) / f


def _capture_ps(fn):
    import contextlib as _c
    import io as _io
    b = _io.StringIO()
    with _c.redirect_stdout(b):
        fn()
    return b.getvalue()


def report_routes():
    """The route decision: what the muon channel costs and what it buys."""
    sys.path.insert(0, HERE)
    import materials as X
    st = station()
    hm_t = X.heavy_metal_inventory_kg() / 1000.0
    burn = X.burnup_kg_per_year()
    print("  THE ROUTE DECISION")
    print()
    print("    TWO DECISIONS ARE RECORDED HERE RATHER THAN ARGUED.")
    print("      FERTILE  uranium, with seawater uranium as the replacement")
    print("               when tails and spent fuel are gone. Thorium refused.")
    print("      FUSION   no longer mandatory. The criterion is cleaner and")
    print("               more efficient, and the muon channel must earn its")
    print("               place against it like anything else.")
    print()
    print("    A CORRECTION FIRST, AND IT REVERSES A COMPARISON MADE ONE PASS")
    print("    AGO. --tradeoff priced the routes on BEAM POWER and found the")
    print("    deuterium route and the no-channel route within 0.001 of each")
    print("    other. That is true and it is not the whole cost: THE MACHINE")
    print("    IS NOT THE BEAM POWER, and the missing term is the driver's")
    print("    ENERGY.")
    print()
    print("    FOR A PURE SPALLATION PLANT THE GAIN IS EXACTLY INVARIANT IN")
    print("    BEAM ENERGY. Yield per GeV DEPOSITED is a flat material")
    print("    property, so y_s = n_per_GeV . E and")
    print("      G = (1000E + y_s.E_k)/(1000E) = 1 + n_per_GeV.E_k/1000")
    print("    with E cancelling. The scan says the same thing:")
    print()
    print("        beam GeV    y_spall        G")
    for e in (0.6, 1.0, 2.0, 3.0, 8.0, 12.0):
        npg = 0.5 * sum(spallation_yield()) / BEAM_GEV
        print(f"        {e:8.1f} {npg*e:10.1f} {gain_invariant_in_energy(e):8.2f}")
    print()
    print("    SO THE 8 GeV IS BOUGHT BY PION PRODUCTION AND BY NOTHING ELSE.")
    print("    HARP's own columns make 3 GeV/c 1.63x dearer per pion than 8.")
    print("    Delete the muon channel and the driver drops to about 1 GeV --")
    print("    SNS and MYRRHA class ON ENERGY, and NOT on current: see")
    print("    --current, which prices what a 1 GeV driver of this power")
    print("    actually is. With the channel go")
    print(f"    {st['modules']:.0f} capture solenoids,"
          f" {st['modules']*1990.986/1000:.0f} km of REBCO and every fuel cell.")
    print()
    print("    THE THREE ROUTES, PRICED ON THE MACHINE AND NOT ON THE BEAM")
    print()
    print("      route                     y_fus   share      G    over C"
          "   station T")
    for name, y_f, share, g, over, trit in route_table():
        print(f"      {name:24s} {y_f:7.2f} {100*share:6.3f} % {g:7.2f}"
              f" {100*over:6.2f} % {trit:9.2f} kg")
    print()
    print("      driver, route A and B     8 GeV        capture solenoids: "
          f"{st['modules']:.0f}")
    print("      driver, route C          ~1 GeV        capture solenoids: 0")
    print()
    print("    AND THAT IS WHAT THE CORRECTION CHANGES. ROUTE B PAYS ROUTE A'S")
    print("    MACHINE FOR ROUTE C'S OUTPUT. Its fusion channel is"
          f" {100*route_table()[1][2]:.2f} % of")
    print("    the source and worth"
          f" {100*route_table()[1][4]:.2f} % of the plant, and it needs the 8 GeV")
    print("    driver and every solenoid to deliver that. It is a route that")
    print("    makes sense only if the object is to DEMONSTRATE the fusion,")
    print("    never if the object is for the fusion to CONTRIBUTE.")
    print()
    print("    ROUTE C GAINS TWICE MORE, AND NEITHER GAIN IS THE DRIVER.")
    print("    With no tritium to breed, the whole Li-6 share of the neutron")
    print("    budget returns to fertile capture:")
    print()
    print("        leak    breeding ratio   fissile surplus   doubling")
    for L in (LEAK_PARASITIC_LO, LEAK_PARASITIC_HI):
        for lab, t in (("with tritium", tritium_per_source_neutron()),
                       ("no tritium  ", 0.0)):
            f = fissions_per_source(K_SAFE)
            br = (f + free_neutrons_per_source(K_SAFE, L) - t) / f
            sur = (br - 1.0) * burn
            print(f"        {L:.2f}  {lab} {br:12.3f} {sur:15.0f} kg/yr"
                  f" {hm_t*FISSILE_FRACTION[0]*1000/sur:6.1f} -"
                  f"{hm_t*FISSILE_FRACTION[1]*1000/sur:6.1f} yr")
    print()
    print("      -- the fleet's binding constraint eases by nearly a factor of")
    print("      two, and it was the worst constraint in the design.")
    print()
    print("    AND THE 8 PERCENT IS NOT NEEDED. The loop requirement is"
          f" {loop_requirement(0.30):.2f}")
    print(f"    and every route clears it: A by"
          f" {route_table()[0][3]/loop_requirement(0.30):.2f}x, C by"
          f" {route_table()[2][3]/loop_requirement(0.30):.2f}x. Neither is near")
    print("    the edge, so route A's extra gain buys margin that was already")
    print("    there rather than margin the plant lacks.")
    print()
    print("    WHAT THIS FILE WILL AND WILL NOT SAY. On the criterion as")
    print("    stated -- cleaner and more efficient -- ROUTE C WINS AND IT IS")
    print("    NOT CLOSE: it deletes the tritium, the lithium, the breeder")
    print("    zone, the cells, the solenoids, the REBCO, and seven eighths of")
    print("    the driver's energy, for 7.5 percent of the gain. What argues")
    print("    for route A is not efficiency and never was -- it is that the")
    print("    fusion is the project's subject, and whether a demonstrated")
    print("    cold-fusion channel is worth an 8 GeV driver is a question")
    print("    about what is being built and not about which is better.")
    print("    THIS FILE DOES NOT DECIDE THAT.")


def report_tritium():
    """Tritium: the consumable geometry will not shrink, and whether it closes."""
    print("  TRITIUM, THE ONE CONSUMABLE THE GEOMETRY WILL NOT SHRINK")
    print()
    print("    The fissile inventory is settled by --fuel: breed what you burn")
    print("    and the fuel, after the first charge, costs nothing. Tritium is")
    print("    not settled by that argument and is the harder of the two.")
    print()
    print("    The cell is one muon range deep, so its holding is areal density")
    print("    times beam area and DOES NOT FALL WITH POWER. A fixed holding")
    print(f"    decays: {100*(1-math.exp(-math.log(2)/T_HALFLIFE_Y)):.2f} %"
          f" a year at a {T_HALFLIFE_Y} y half-life, running or idle.")
    print()
    print("    A CORRECTION FIRST, AND IT IS THIS SECTION'S REASON TO EXIST.")
    print("    Priced the way a fusion reactor prices it -- a breeding ratio")
    print("    times the FUSION neutron yield -- the balance fails, and that")
    print("    accounting is wrong here: the blanket is driven by every neutron")
    print("    the target makes, not by the fusion neutrons alone.")
    m = _mach()
    y_s = 0.5 * sum(spallation_yield())
    eta_265 = m.delivered_eta_window(1.50, 265.0)
    y_f = PI_PER_PROTON * eta_265 * N_MEASURED
    print(f"      spallation neutrons per proton      {y_s:8.1f}")
    print(f"      fusion neutrons per proton          {y_f:8.2f}"
          f"   (delivered eta {eta_265:.4f})")
    print(f"      the fusion channel is               {y_f/(y_s+y_f)*100:8.1f} %"
          "  of the source")
    print()
    n_tot = neutrons_per_source(K_SAFE)
    f = fissions_per_source(K_SAFE)
    print(f"    THE BLANKET'S NEUTRON BUDGET at k = {K_SAFE}, per source neutron:")
    print(f"      neutrons in all      1/(1-k)          {n_tot:8.3f}")
    print(f"      cause fission        F                {f:8.3f}")
    print(f"      non-fission fates    A = n_tot - F    {n_tot-f:8.3f}")
    print(f"      MUST breed fissile   f_b . A = F      {f:8.3f}"
          f"   (f_b = {fertile_capture_required(K_SAFE):.4f})")
    for lab, L in (("low ", LEAK_PARASITIC_LO), ("high", LEAK_PARASITIC_HI)):
        print(f"      leak + parasitic     L . n_tot  ({lab})  {L*n_tot:8.3f}"
              f"   ASSUMED L = {L:.2f}")
        print(f"      FREE for Li-6                         "
              f"{free_neutrons_per_source(K_SAFE, L):8.3f}")
    print()
    print("    THE WINDOW SETS THE HOLDING, AND SO SETS THE PLANT. Tritium goes")
    print("    as the muon range and fusions as the acceptance, so a narrower")
    print("    stopping window is a smaller holding and a smaller balance both.")
    print()
    print("      window   range   delivered   holding   decay    burn    supply"
          "   ratio   closes at, MW")
    print("      MeV/c    g/cm2      eta        kg      g/yr     g/yr     g/yr"
          "          ceiling design")
    C = _coll()
    for p in (150.0, 175.0, 200.0, 225.0, 265.0, 300.0, 400.0):
        inv = tritium_inventory_kg(p)
        d, b = tritium_demand_per_second(p, 1.0)
        sup = tritium_supply_per_second(p, 1.0)
        g = SEC_PER_YEAR * T_AMU / N_AVOGADRO
        print(f"      {p:5.0f}  {C.csda_range(p):7.2f}   {m.delivered_eta_window(1.50,p):8.5f}"
              f" {inv:8.3f} {d*g:8.1f} {b*g:8.1f} {sup*g:9.1f}"
              f" {sup/(d+b):7.3f}  {beam_mw_for_tritium(p):7.2f}"
              f" {beam_mw_for_tritium(p, f_li=F_LI_DESIGN):7.2f}")
    print()
    print(f"      (at 1 MW of beam, k = 0.95, L = 0.20, base collector 1.50 T.m,")
    print(f"       cell radius {m.cell_radius_cm():.2f} cm at {m.CELL_B_T:.0f} T recompression, IMPORTED;")
    print("       supply is a CEILING -- every free neutron")
    print("       captured in Li-6 -- so the ratio is an upper bound and the")
    print("       closing power a lower one.)")
    print()
    print("    THE FINDING, AND IT RESIZES THE PLANT. Supply above is a ceiling")
    print(f"    -- every free neutron into Li-6. At the design share f_li ="
          f" {F_LI_DESIGN:.2f}")
    print(f"    the base 265 MeV/c window closes at"
          f" {beam_mw_for_tritium(265.0, f_li=F_LI_DESIGN):.2f} MW of beam, not at the 1 MW")
    print("    the loop and the scale arguments alone would have allowed.")
    print("    TRITIUM, NOT THE LOOP AND NOT THE DRIVER OVERHEAD, IS WHAT SETS")
    print(f"    THE SIZE OF THIS PLANT -- and it sets it"
          f" {beam_mw_for_tritium(265.0, f_li=F_LI_DESIGN):.2f}x higher.")
    print()
    g = plant_gain(K_SAFE, y_s, y_f)
    print(f"      REFERENCE PLANT   8 GeV, {REF_BEAM_MW:.0f} MW beam, k = {K_SAFE},"
          f" base collector")
    print(f"        plant gain G                    {g:10.2f}")
    print(f"        thermal                         {REF_BEAM_MW*g:10.2f} MW")
    net = net_electric_kw(REF_BEAM_MW * 1000.0, REF_STANDBY_KW)
    print(f"        net electric, driver fed        {net/1000.0:10.2f} MW")
    print(f"        homes at {HOUSEHOLD_KW:.2f} kW               {homes(net):10.0f}")
    print(f"        tritium balance at f_li = {F_LI_DESIGN:.2f}  "
          f"{tritium_balance(265.0, REF_BEAM_MW, f_li=F_LI_DESIGN):10.3f}")
    print(f"        tritium holding                 "
          f"{tritium_inventory_kg(265.0):10.3f} kg")
    print()
    print("    AND A SECOND QUESTION THE FIRST DOES NOT ANSWER: CAN A PLANT")
    print("    LIGHT THE NEXT ONE? Self-sufficiency says the holding is held.")
    print("    A FLEET needs a SURPLUS, and the holding is fixed by geometry")
    print("    while the surplus is only what the beam buys over it.")
    print()
    print("        beam MW   surplus g/yr   doubling years")
    scan = sorted({round(beam_mw_for_tritium(265.0, f_li=F_LI_DESIGN), 2),
                   round(beam_mw_for_doubling(40.0), 2),
                   REF_BEAM_MW, 14.0, 20.0, 30.0})
    for mw in scan:
        dt = tritium_doubling_years(mw)
        shown = "never" if dt > 1e4 else f"{dt:.1f}"
        print(f"        {mw:7.2f}   {tritium_surplus_g_per_year(mw):12.1f}"
              f"   {shown:>14}")
    print()
    mw40 = beam_mw_for_doubling(40.0)
    print("    SELF-SUFFICIENT IS NOT SELF-REPLICATING, and the two were never")
    print("    the same claim. There are THREE thresholds on this axis, not one:")
    print(f"      {beam_mw_for_tritium(265.0, f_li=F_LI_DESIGN):5.2f} MW"
          "   the plant holds its own inventory")
    print(f"      {mw40:5.2f} MW   it breeds a successor's first charge inside"
          " a 40 year life")
    print(f"      {REF_BEAM_MW:5.2f} MW   the reference, clearing both with"
          " margin")
    print(f"    At {REF_BEAM_MW:.0f} MW the doubling time is"
          f" {tritium_doubling_years(REF_BEAM_MW):.1f} years. Below"
          f" {mw40:.1f} MW a plant")
    print("    is self-sufficient and STILL cannot start another, so a fleet")
    print("    would have to be lit from outside -- and the world's civil")
    print("    tritium is tens of kilogrammes, which lights a few plants and")
    print("    not a hundred. THE FLEET CONSTRAINT, NOT THE PLANT CONSTRAINT,")
    print("    IS WHAT PUTS THE REFERENCE ABOVE 8 MW.")
    print()
    print("    WHAT IT COSTS TO NARROW THE WINDOW. Acceptance falls with it, so")
    lo, hi = m.delivered_eta_window(1.50, 150.0), m.delivered_eta_window(1.50, 265.0)
    print(f"    the fusion channel's own yield falls {hi/lo:.3f}x -- from"
          f" {y_f:.1f} to {PI_PER_PROTON*lo*N_MEASURED:.1f}")
    print("    neutrons per proton. Against a spallation source of"
          f" {y_s:.0f} that is")
    y_f150 = PI_PER_PROTON * lo * N_MEASURED
    print(f"    a {(y_s+y_f)/(y_s+y_f150):.3f}x cut in the total source, and so in the plant's")
    print("    output at fixed beam. THE TRITIUM BALANCE IS BOUGHT WITH POWER,")
    print("    and the two ways of buying it -- narrow the window, or raise the")
    print("    beam -- are the same trade seen from two ends.")
    print()
    print("    NOT COUNTED, AND EACH RUNS IN OUR FAVOUR: Li-7(n,n'a)T is a")
    print("    threshold reaction that MULTIPLIES as it breeds, U-238 (n,2n)")
    print("    likewise, and a reflector returns part of L. Against that, the")
    print("    supply figure assumes every free neutron reaches Li-6, which no")
    print("    blanket achieves. The band is wide and it is stated as a")
    print("    REQUIREMENT on the neutron budget. Stage D measures it.")
    print()
    print("    LITHIUM IS THEN A CONSUMABLE TOO, one Li-6 per triton, but it is")
    print("    a different kind: it is stockpiled, not bred, and the quantity is")
    dR, bR = tritium_demand_per_second(265.0, REF_BEAM_MW)
    li_kg_yr = (dR + bR) * SEC_PER_YEAR * 6.015 / N_AVOGADRO / 1000.0
    print(f"    {li_kg_yr*1000:.0f} g of Li-6 a year at the reference plant -- a")
    print(f"    {li_kg_yr*40:.1f} kg lifetime charge over forty years, which is a")
    print("    first charge and not a supply line.")


def report():
    m = _mach()
    print("WHAT A SELF-SUSTAINING POWER SOURCE REQUIRES")
    print("  G = N . V . eta / E_pi = 1, solved for each term in turn.")
    print()
    eta_best = m.delivered_eta_window(2.60, 400.0)
    print("  AT THE BEST CONFIGURATION THIS WORK SPECIFIES")
    print(f"    measured service life   N    = {N_MEASURED:.0f} cycles")
    print(f"    heat recovered per fusion V  = {V_HEAT_MEV} MeV  (sourced, fission-suppressed)")
    print(f"    delivered collection    eta  = {100 * eta_best:.2f} %")
    print(f"    production cost         E_pi = {E_PI_MEASURED} GeV")
    print(f"    balance                 G    = "
          f"{N_MEASURED * V_HEAT_MEV / 1000.0 * eta_best / E_PI_MEASURED:.3f}")
    print()
    print("  SOLVING FOR EACH TERM, THE OTHERS HELD THERE")
    n_req = required("N", eta=eta_best, e_pi=E_PI_MEASURED)
    e_req = required("eta", e_pi=E_PI_MEASURED)
    p_req = required("E_pi", eta=eta_best)
    v_req = required("V", eta=eta_best, e_pi=E_PI_MEASURED)
    cap = service_life_cap()
    print(f"    N    must be {n_req:8.1f} cycles   against a CAP of {cap:.0f}"
          f"  -- FORBIDDEN by {n_req / cap:.2f}")
    print(f"    eta  must be {100 * e_req:8.1f} %        against a CAP of 100"
          f"  -- FORBIDDEN by {e_req:.2f}")
    print(f"    E_pi must be {p_req:8.3f} GeV      against {E_PI_MEASURED} measured,"
          f" {E_PI_OPTIMISED} optimised  -- OPEN")
    print(f"    V    must be {v_req:8.1f} MeV      against {V_HEAT_MEV} sourced"
          f"  -- OPEN")
    print()
    print("    TWO OF THE FOUR ARE CLOSED BY SOMETHING NO ENGINEERING MOVES.")
    print("    The service life is capped by the sticking and the collection is")
    print("    a fraction. So a self-sustaining POWER source is a statement")
    print("    about V and E_pi, and V is where the room is.")
    print()
    print("  WHAT V REQUIRES, AND WHAT SUPPLIES IT")
    print("    A non-fissioning blanket returns the alpha, the neutron and the")
    print("    Li-6 exotherm, less the multiplier's endotherm: 24.31 to 27.20 MeV.")
    print("    [3] sec.5.1 is right that no (n,xn) blanket reaches the requirement,")
    print("    and wrong about what follows. Fission in a SUBCRITICAL blanket")
    print("    returns HEAT, ON SITE -- which is the product, not a change of it.")
    print()
    print(f"    Energy per source neutron in a subcritical assembly, from")
    print(f"    F = k/(nu(1-k)) fissions per source neutron at nu = {NU_FAST},"
          f" E_f = {E_FISSION_MEV:.0f} MeV:")
    print()
    print(f"      {'k_eff':>8}{'MeV per source n':>20}")
    for k in (0.25, 0.40, 0.50, 0.60, 0.70, 0.80, 0.90, 0.95):
        print(f"      {k:8.2f}{energy_per_source_neutron(k):20.1f}")
    print()
    ks = k_of_sourced_blanket()
    print(f"    The sourced fission-suppressed blanket, at a multiplication of")
    print(f"    1.6 on the neutron, sits at k_eff <= {ks:.3f} -- which is where a")
    print(f"    design that SUPPRESSES fission should sit, and is the check that")
    print(f"    this relation is in the right regime.")
    print()
    print("  THE SPECIFICATION, BY CONFIGURATION")
    print(f"      {'configuration':<30}{'V needed':>10}{'k_eff needed':>14}"
          f"{'fusion share':>14}")
    for lab, eta, e_pi in configurations():
        k, v = required_k(eta, e_pi)
        print(f"      {lab:<30}{v:10.1f}{k:14.3f}{100 * fusion_share(v):13.1f} %")
    print()
    print("    EVERY ONE OF THOSE IS DEEPLY SUBCRITICAL. For scale, an")
    print("    accelerator-driven subcritical system is designed around")
    print("    k_eff ~ 0.95 and a power reactor runs at 1.000. The requirement")
    print("    is met with a very large margin to criticality, which is a")
    print("    safety property and not only an engineering one.")
    print()
    print("  AND WHAT IT COSTS TO SAY IT")
    _, v = required_k(*[c[1:] for c in configurations()][3])
    print(f"    At the least demanding configuration the fusion itself supplies")
    print(f"    {100 * fusion_share(v):.1f} % of the recovered energy and all of the neutrons.")
    print("    The device is a fusion-driven subcritical fission reactor. It is")
    print("    self-sustaining as a POWER source on this work's own criterion --")
    print("    it returns more energy than the beam that drives it, as heat, with")
    print("    nothing leaving the device -- and it is not a fusion power plant.")
    print("    Both halves of that are stated because neither stands alone.")
    print()
    print("  WHAT THIS INSTRUMENT DOES NOT SETTLE.")
    print("    Whether the same beam spent on a SPALLATION-driven subcritical")
    print("    system does better. That is the deciding comparison for a builder,")
    print("    no number here settles it, and it is measurable on one apparatus.")
    return 0


def _raises_value(fn):
    try:
        fn()
        return False
    except ValueError:
        return True


def selftest():
    fail = 0

    def check(label, got, want=True):
        nonlocal fail
        ok = (got == want)
        fail += 0 if ok else 1
        print(f"  {label:<66} {'PASS' if ok else 'FAIL'}")

    m = _mach()
    eta_best = m.delivered_eta_window(2.60, 400.0)

    print("  the inverse solves the same identity the forward balance uses")
    g = N_MEASURED * (V_HEAT_MEV / 1000.0) * eta_best / E_PI_MEASURED
    v_req = required("V", eta=eta_best, e_pi=E_PI_MEASURED)
    check("solving for V and substituting it back returns exactly unity",
          abs(N_MEASURED * (v_req / 1000.0) * eta_best / E_PI_MEASURED - 1.0)
          < 1e-9)
    check("and the forward balance at the sourced blanket is below unity",
          g < 1.0)

    print()
    print("  the two closed axes are closed, and the instrument says which")
    n_req = required("N", eta=eta_best, e_pi=E_PI_MEASURED)
    check("the service life required exceeds the sticking cap",
          n_req > service_life_cap())
    check("the collection required exceeds one",
          required("eta", e_pi=E_PI_MEASURED) > 1.0)

    print()
    print("  the subcritical relation is checked against what is already known")
    check("a fission-suppressed blanket's 1.6 sits deeply subcritical",
          k_of_sourced_blanket() < 0.35)
    check("k -> 0 returns no fission energy",
          abs(energy_per_source_neutron(0.0)) < 1e-12)
    check("and the relation inverts exactly",
          abs(k_for_energy(energy_per_source_neutron(0.62)) - 0.62) < 1e-12)
    check("an ADS at k = 0.95 returns more than a GeV per source neutron",
          energy_per_source_neutron(0.95) > 1000.0)

    print()
    print("  the specification itself")
    worst = max(required_k(eta, e_pi)[0] for _, eta, e_pi in configurations())
    best = min(required_k(eta, e_pi)[0] for _, eta, e_pi in configurations())
    check("every configuration needs k_eff below 0.80", worst < 0.80)
    check("and the least demanding needs less than 0.50", best < 0.50)
    check("all of them are far from criticality", worst < 0.95)
    _, v = required_k(*[c[1:] for c in configurations()][3])
    check("at which point the fusion supplies under a third of the energy",
          fusion_share(v) < 0.34)
    check("so the claim is a POWER source and not a fusion power plant",
          fusion_share(v) < 0.50)

    print()
    print("  the spallation comparison, and the structure it turns on")
    y_fus = fusion_neutrons_per_proton(eta_best)
    check("the muon channel adds neutrons rather than replacing any",
          y_fus > 0.0)
    check("and the addition is the pion yield times collection times the life",
          abs(y_fus - PI_PER_PROTON * eta_best * N_MEASURED) < 1e-9)
    check("the break-even penalty falls as the spallation yield rises",
          transparency_breakeven(250.0, eta_best)
          < transparency_breakeven(100.0, eta_best))
    check("at a high spallation yield the requirement is still under a fifth",
          transparency_breakeven(250.0, eta_best) < 0.25)
    check("taking a 14.1 MeV neutron as worth exactly one is the conservative "
          "choice", transparency_breakeven(150.0, eta_best, worth=1.0)
          < transparency_breakeven(150.0, eta_best, worth=1.5))

    print()
    print("  the two target figures, and the geometry that decides the second")
    lo, hi = spallation_yield()
    check("a containing target at this beam energy yields hundreds per proton",
          150.0 < lo < hi < 300.0)
    check("the published jet stops most primaries",
          primary_interacting() > 0.80)
    check("and keeps almost none of the cascade they start",
          cascade_retained() < 0.05)
    check("so it is a production foil rather than a spallation target",
          cascade_retained() < primary_interacting() / 10.0)
    check("the transparency penalty is NEGATIVE for a fissile blanket",
          transparency_penalty() < 0.0)
    check("it is exactly zero at parity, which is where the sign turns",
          abs(transparency_penalty(1.0)) < 1e-12)
    check("and positive only for a blanket worse than the target per GeV",
          transparency_penalty(0.5) > 0.0)
    print("    -- the conclusion holds at PARITY, so it does not rest on the")
    print("       uranium-over-lead figure being right, only on the blanket not")
    print("       being WORSE than the target it replaces")

    print()
    print("  the closed loop, which is a heavier criterion than beating the beam")
    y_f = fusion_neutrons_per_proton(eta_best)
    y_s = 0.5 * sum(spallation_yield())
    check("the loop requirement is far above unity",
          loop_requirement(0.30) > 5.0)
    check("and it tightens as the accelerator gets worse",
          loop_requirement(0.20) > loop_requirement(0.50))
    check("the thermal efficiency stays under its Carnot ceiling",
          eta_thermal() < CARNOT_AT_BLANKET)
    for ea in (ETA_ACC_LO, 0.30, ETA_ACC_HI):
        g = loop_requirement(ea)
        check(f"the loop closes subcritically at eta_acc = {ea:.2f}",
              k_for_plant_gain(g, y_s, y_f) < 1.0)
    check("and below the accelerator-driven design point in every case",
          k_for_plant_gain(loop_requirement(ETA_ACC_LO), y_s, y_f) < 0.95)
    check("the muon channel LOWERS the k the loop needs",
          k_for_plant_gain(loop_requirement(0.30), y_s, y_f)
          < k_for_plant_gain(loop_requirement(0.30), y_s, 0.0))
    check("but spallation alone still closes it, so the channel is margin "
          "rather than enablement",
          k_for_plant_gain(loop_requirement(0.30), y_s, 0.0) < 1.0)
    check("substituting a solved k back reproduces the gain it was solved for",
          abs(plant_gain(k_for_plant_gain(6.0, y_s, y_f), y_s, y_f) - 6.0)
          < 1e-6)
    print("    -- the loop closing WITHOUT the muon channel is asserted here on")
    print("       purpose: the instrument must not be able to report the channel")
    print("       as necessary when the arithmetic says it is not")

    print()
    print("  stability, which is two questions with opposite answers")
    y_f2 = fusion_neutrons_per_proton(eta_best)
    y_s2 = 0.5 * sum(spallation_yield())
    k_loop = k_for_plant_gain(loop_requirement(0.30), y_s2, y_f2)
    k_plant = k_for_plant_gain(loop_requirement(0.30) / 0.25, y_s2, y_f2)
    check("every operating point keeps a positive margin to criticality",
          min(subcritical_margin(k_loop)[0], subcritical_margin(k_plant)[0]) > 0)
    check("the plant's margin exceeds a fast core's whole control worth",
          subcritical_margin(k_plant)[1] > CONTROL_WORTH_PCM)
    check("power amplifies reactivity more sharply nearer criticality",
          power_sensitivity(0.95) > power_sensitivity(k_plant)
          > power_sensitivity(k_loop))
    check("the Doppler coefficient is negative, so it restores",
          doppler_dk_per_k() < 0.0)
    check("and restores one percent of gain inside an ordinary swing",
          restoring_delta_t(k_plant) < 300.0)
    check("the muon channel widens the margin to criticality",
          k_for_plant_gain(loop_requirement(0.30), y_s2, 0.0) > k_loop)
    check("and lowers the power sensitivity with it",
          power_sensitivity(k_for_plant_gain(loop_requirement(0.30), y_s2, 0.0))
          > power_sensitivity(k_loop))
    g_op = loop_requirement(0.30)
    check("the recirculating loop's gain at the operating point is EXACTLY one",
          abs(eta_thermal() * 0.30 * g_op - 1.0) < 1e-12)
    print("    -- that last one is the finding, not a formality: a loop whose")
    print("       gain is exactly one is MARGINALLY stable, so it cannot be")
    print("       closed by feeding back a fixed share and must be regulated")

    print()
    print("  the fuel, priced rather than named")
    ys3, yf3 = 0.5 * sum(spallation_yield()), fusion_neutrons_per_proton(eta_best)
    kL = k_for_plant_gain(loop_requirement(0.30), ys3, yf3)
    kP = k_for_plant_gain(loop_requirement(0.30) / 0.25, ys3, yf3)
    check("the fertile capture required is a fraction, not a demand for all of it",
          0.0 < fertile_capture_required(kL) < 0.5)
    check("and it is easier the further from criticality the device sits",
          fertile_capture_required(kL) < fertile_capture_required(kP)
          < fertile_capture_required(0.95))
    check("breeding exactly at the requirement returns a ratio of one",
          abs(breeding_ratio(kL, fertile_capture_required(kL)) - 1.0) < 1e-9)
    check("breeding above it returns more than one",
          breeding_ratio(kL, 2 * fertile_capture_required(kL)) > 1.0)
    check("and below it, less -- so the device would eat its own inventory",
          breeding_ratio(kL, 0.5 * fertile_capture_required(kL)) < 1.0)
    print("    -- the requirement is what makes the fuel free AFTER ignition;")
    print("       below it the fuel has a price and the claim fails")

    print()
    print("  scale: why the answer is a plant and not an appliance")
    check("the minimum beam power rises with the driver's standby load",
          minimum_beam_kw(2000.0) > minimum_beam_kw(200.0))
    check("at three times the minimum the plant sells a useful surplus",
          net_electric_kw(3 * minimum_beam_kw(500.0), 500.0) > 1000.0)
    check("and that surplus is thousands of households, not one",
          homes(net_electric_kw(3 * minimum_beam_kw(500.0), 500.0)) > 1000.0)
    check("a household-scale beam cannot close the loop at a safe k",
          net_electric_kw(30.0, 1000.0) < 0.0)
    check("the effective efficiency collapses as the beam falls",
          eta_effective(30.0, 1000.0) < eta_effective(3000.0, 1000.0))
    check("a kilogramme of fertile runs a household for centuries",
          home_years_per_kg() > 500.0)
    check("and a household's year is grams rather than kilogrammes",
          fertile_grams_per_home_year() < 10.0)
    print("    -- the floor is the DRIVER's fixed overhead, not the reaction:")
    print("       the margin that makes the reactor safe is the same margin")
    print("       that forbids shrinking it")

    print()
    print("  the instrument can fail: a blanket that could not supply the")
    print("  requirement would have to need k >= 1, so that case is constructed")
    check("a requirement of 100 GeV per fusion would need k >= 1",
          k_for_energy(100000.0) > 0.99)
    print("    -- so the content of the result is that the requirement lands")
    print("       DEEPLY subcritical, which is a fact about the numbers")

    print()

    print()
    print("  tritium: the balance is a fact about the blanket, not about fusion")
    check("the holding is geometric -- same at 1 MW and at 100 MW",
          abs(tritium_inventory_kg(265.0) - tritium_inventory_kg(265.0)) == 0.0
          and tritium_demand_per_second(265.0, 1.0)[0]
              == tritium_demand_per_second(265.0, 100.0)[0])
    check("so demand per source neutron FALLS with power and the balance rises",
          tritium_balance(265.0, 10.0) > tritium_balance(265.0, 1.0))
    check("a narrower window lowers the holding faster than it lowers supply",
          tritium_balance(150.0, 1.0) > tritium_balance(400.0, 1.0))
    # the correction this section exists to record: the fusion-reactor
    # convention, TBR x fusion neutrons, against the blanket's own economy
    y_s = 0.5 * sum(spallation_yield())
    y_f = fusions_per_proton(265.0)
    fusion_only = 1.15 * y_f * protons_per_second(1.0)
    blanket = tritium_supply_per_second(265.0, 1.0)
    check("the fusion-reactor accounting understates supply by over 10x",
          blanket / fusion_only > 10.0)
    check("  -- by 18.8x at the reference window, stated rather than rounded",
          abs(blanket / fusion_only - 18.8) < 0.1)
    check("because the fusion channel is under a fifth of the source",
          y_f / (y_s + y_f) < 0.20)
    check("free neutrons are what is left AFTER fission and fertile capture",
          abs(free_neutrons_per_source(K_SAFE, 0.0)
              - (neutrons_per_source(K_SAFE) - 2 * fissions_per_source(K_SAFE)))
          < 1e-12)
    check("and a leakage allowance only ever reduces them",
          free_neutrons_per_source(K_SAFE, LEAK_PARASITIC_HI)
          < free_neutrons_per_source(K_SAFE, LEAK_PARASITIC_LO))
    check("the design Li-6 share is BELOW the ceiling, so the design is dearer",
          beam_mw_for_tritium(265.0, f_li=F_LI_DESIGN)
          > beam_mw_for_tritium(265.0, f_li=F_LI_CEILING))
    check("self-sufficiency and self-replication are different thresholds",
          beam_mw_for_doubling(40.0)
          > beam_mw_for_tritium(265.0, f_li=F_LI_DESIGN))
    check("  -- a plant exactly self-sufficient can never breed a successor",
          tritium_doubling_years(
              beam_mw_for_tritium(265.0, f_li=F_LI_DESIGN)) > 1e3)
    check("the reference clears the FLEET threshold, not just its own",
          tritium_doubling_years(REF_BEAM_MW) < 40.0)
    check("  -- and 7 MW, which clears self-sufficiency, does not",
          tritium_doubling_years(7.0) > 40.0)
    check("the reference plant closes on tritium at the design share",
          tritium_balance(265.0, REF_BEAM_MW, f_li=F_LI_DESIGN) > 1.0)
    check("  -- and 1 MW, which the loop alone would have allowed, does not",
          tritium_balance(265.0, 1.0, f_li=F_LI_DESIGN) < 1.0)
    # so the constraint is BINDING: it is not slack the other arguments left
    check("so tritium, not the loop, sets the plant's size",
          beam_mw_for_tritium(265.0, f_li=F_LI_DESIGN)
          > minimum_beam_kw(REF_STANDBY_KW) / 1000.0)
    # and it is not a tautology: a hypothetical stable triton needs no beam
    print()
    print("  the station: the scale-up decides what one module left open")
    st = station()
    check("the station meets the households it was sized for",
          st["households"] >= STATION_HOUSEHOLDS)
    check("  -- and does it in whole modules, so it overshoots rather than under",
          st["modules"] * st["module_mw"]
          >= station_beam_mw(window=STATION_WINDOW_MEV))
    check("the forced window closes on tritium at the sourced module power",
          tritium_balance(STATION_WINDOW_MEV, MODULE_BEAM_MW,
                          f_li=F_LI_DESIGN) > 1.0)
    check("  -- and the window this work used at one module does NOT",
          tritium_balance(265.0, MODULE_BEAM_MW, f_li=F_LI_DESIGN) < 1.0)
    check("  -- so the window is FORCED by the scale-up, not chosen",
          STATION_WINDOW_MEV < 265.0)
    check("the narrow window costs the fusion channel more than the plant",
          (_mach().delivered_eta_window(1.50, 265.0)
           / _mach().delivered_eta_window(1.50, STATION_WINDOW_MEV))
          > (plant_gain(K_SAFE, 0.5 * sum(spallation_yield()),
                        fusions_per_proton(265.0)) / st["gain"]))
    check("the balance is scale-invariant: N modules give one module's ratio",
          abs(tritium_balance(STATION_WINDOW_MEV, MODULE_BEAM_MW,
                              f_li=F_LI_DESIGN) - st["tritium_ratio"]) < 1e-12)
    check("splitting the blanket N ways breaks the neutron budget",
          free_neutrons_per_source(
              K_SAFE,
              blanket_leakage_penalty(st["modules"]) * LEAK_PARASITIC_HI)
          < 0.0)
    check("  -- and not splitting it leaves the budget positive",
          free_neutrons_per_source(K_SAFE, LEAK_PARASITIC_HI) > 0.0)
    check("relaxing k would shrink the driver, so the trade is real",
          station_beam_mw(k_eff=0.98) < station_beam_mw(k_eff=K_SAFE))
    check("  -- and it is declined: the margin at K_SAFE is a control worth",
          subcritical_margin(K_SAFE)[1] >= CONTROL_WORTH_PCM
          and subcritical_margin(0.98)[1] < CONTROL_WORTH_PCM)
    n0, yrs = staged_charge()
    check("the station's first charge exceeds the world's civil tritium",
          st["tritium_total_kg"] > WORLD_CIVIL_TRITIUM_KG)
    check("  -- and it is still buildable, because modules stage",
          0.0 < yrs < 10.0 and n0 < st["modules"])
    check("  -- a station whose stock covered it would need no staging",
          staged_charge(stock_kg=1e6)[1] == 0.0)
    check("the fleet doubles at the same rate one module does",
          abs(station_doubling_years()
              - tritium_doubling_years(st["module_mw"], st["window"])) < 1e-9)
    print()
    print("  starting one: three problems, and the selftest says which binds")
    sys.path.insert(0, HERE)
    import materials as _X
    hm_t = _X.heavy_metal_inventory_kg() / 1000.0
    burn = _X.burnup_kg_per_year()
    check("a running station can start several neighbours' drivers at once",
          stations_startable() > 1.0)
    check("break-even breeding is exactly break-even, by construction",
          abs(fissions_per_source(K_SAFE)
              / (fertile_capture_required(K_SAFE)
                 * (neutrons_per_source(K_SAFE)
                    - fissions_per_source(K_SAFE))) - 1.0) < 1e-12)
    check("  -- so any fissile surplus is what the budget has LEFT, not design",
          breeding_ratio_available(LEAK_PARASITIC_HI) > 1.0)
    check("  -- and a tighter leakage allowance leaves more of it",
          breeding_ratio_available(LEAK_PARASITIC_LO)
          > breeding_ratio_available(LEAK_PARASITIC_HI))
    check("fissile doubling is slower than tritium doubling, at every point",
          all(fissile_doubling_years(hm_t, burn, f, LEAK_PARASITIC_HI)
              > station_doubling_years()
              for f in (FISSILE_FRACTION[0], FISSILE_FRACTION[1])))
    check("  -- so FISSILE binds the fleet and tritium does not",
          min(fissile_doubling_years(hm_t, burn, f, L)
              for f in FISSILE_FRACTION
              for L in (LEAK_PARASITIC_LO, LEAK_PARASITIC_HI))
          > station_doubling_years())
    check("the stockpile route lights more than one station",
          stations_from_stock(hm_t, FISSILE_FRACTION[1]) > 1.0)
    check("the loop still closes below the design k, so 'start small' is real",
          min_k_for_loop() < K_SAFE)
    check("  -- and it is declined, because the output cost exceeds the saving",
          (plant_gain(K_SAFE, station()["y_spall"], station()["y_fus"])
           / plant_gain(min_k_for_loop(), station()["y_spall"],
                        station()["y_fus"]))
          > 1.0 / (min_k_for_loop() / K_SAFE))
    check("driver standby has stopped mattering at station scale",
          st["linacs"] * REF_STANDBY_KW / 0.30
          < 0.02 * st["net_mw"] * 1000.0)
    print()
    check("a longer-lived triton would need proportionately less beam",
          _beam_for_halflife(123.2) < beam_mw_for_tritium(265.0) / 5.0)
    check("  -- so the plant's size is a statement about the half-life",
          abs(_beam_for_halflife(123.2) * 10.0
              / beam_mw_for_tritium(265.0) - 1.0) < 0.05)
    print()
    print("  the route decision, and the correction it forced")
    # the invariance is ASSERTED numerically, not trusted from the algebra
    gains = [round(gain_invariant_in_energy(e), 9)
             for e in (0.6, 1.0, 2.0, 3.0, 8.0, 12.0, 30.0)]
    check("the pure-spallation gain is invariant in beam energy",
          len(set(gains)) == 1)
    check("  -- so the 8 GeV is bought by pion production and nothing else",
          abs(gains[0] - plant_gain(K_SAFE, 0.5 * sum(spallation_yield()),
                                    0.0)) < 1e-9)
    rt = route_table()
    check("three routes, and route C is the one with no channel",
          len(rt) == 3 and rt[2][1] == 0.0)
    check("route B's fusion channel is under one percent of the source",
          rt[1][2] < 0.01)
    check("  -- so B pays A's machine for C's output, which is the finding",
          rt[1][4] < 0.01 and rt[1][3] < rt[0][3])
    check("route A's channel IS worth several percent, unlike B's",
          rt[0][4] > 0.05)
    check("every route clears the loop requirement with margin",
          all(r[3] / loop_requirement(0.30) > 2.0 for r in rt))
    check("  -- so the channel's gain is not margin the plant lacks",
          rt[2][3] / loop_requirement(0.30) > 2.0)
    check("dropping tritium raises the breeding ratio",
          breeding_without_tritium() > breeding_ratio_available())
    check("  -- and so nearly halves the fissile doubling time",
          (breeding_without_tritium() - 1.0)
          / (breeding_ratio_available() - 1.0) > 1.5)
    check("the file states the decision is not its to make",
          "DOES NOT DECIDE THAT" in _capture_ps(report_routes))
    print()
    print("  every section renders -- which is how a stale call is caught")
    import contextlib as _c, io as _io
    for _name, _fn in (("report", report), ("spallation", report_spallation),
                       ("target", report_target), ("plant", report_plant),
                       ("stability", report_stability), ("fuel", report_fuel),
                       ("scale", report_scale), ("tritium", report_tritium),
                       ("station", report_station),
                       ("ignition", report_ignition),
                       ("routes", report_routes),
                       ("rescale", report_rescale),
                       ("driver", report_driver),
                       ("current", report_current),
                       ("linac", report_linac),
                       ("blanket", report_blanket)):
        try:
            _b = _io.StringIO()
            with _c.redirect_stdout(_b):
                _fn()
            _ok = len(_b.getvalue()) > 200
        except Exception as _e:                        # noqa: BLE001
            _ok = False
            print(f"      {_name}: {type(_e).__name__}: {_e}")
        check(f"section {_name!r} renders", _ok)
    print()
    print("  the adopted operating point, and what re-scaling does and does not do")
    check("the adopted k is below the ADS convention", K_DESIGN < K_SAFE)
    check("  -- so it carries more subcritical margin, not less",
          subcritical_margin(K_DESIGN)[1] > subcritical_margin(K_SAFE)[1])
    check("  -- and the loop still closes there",
          station(k_eff=K_DESIGN)["gain"] > loop_requirement(0.30))
    # THE FINDING THE RE-SCALE WAS UNDERTAKEN TO TEST, and it failed to give
    # the hoped-for answer: the beam is set by the multiplication, so changing
    # the module size cannot recover what the lower k costs.
    beams = [rescaled_station(mw)["beam_mw"] for mw in SPALL_TARGET_MW.values()]
    check("the beam is the same at every target power, to within one module",
          max(beams) - min(beams) < max(SPALL_TARGET_MW.values()) + 1e-9)
    check("  -- so re-scaling does NOT recover the cost of the lower k",
          min(beams) > 2.0 * station(k_eff=K_SAFE)["beam_mw"])
    check("what re-scaling does move is the module count",
          rescaled_station(10.0)["modules"] < rescaled_station(1.0)["modules"])
    check("a non-positive target power is refused",
          _raises_value(lambda: rescaled_station(0.0)))
    check("only the two operated rows are at or below what has been built",
          sum(1 for mw in SPALL_TARGET_MW.values()
              if mw <= TARGET_DEMONSTRATED_MW) == 2)

    print()
    print("  the driver already bought, and the ceiling that is NOT computed")
    _ess = SPALL_TARGET_MW["ESS, design"]
    # NET IS EXACTLY LINEAR IN BEAM at a fixed driver count. Pinned because the
    # whole marginal argument rests on it, and because it is what makes the
    # model hand back output without limit -- which is a fault of the model.
    _n = [net_electric_kw_at(b, 12, k_eff=K_DESIGN) for b in (200.0, 220.0,
                                                              240.0)]
    check("net is exactly linear in beam at a fixed driver count",
          abs((_n[2] - _n[1]) - (_n[1] - _n[0])) < 1e-6)
    _base = station(k_eff=K_SAFE)
    _built = station_open_loop_rescaled(_ess)
    _meets = rescaled_station(_ess)
    # THE FINDING: the sizing charges one driver's standby and the answer needs
    # twelve, so the station lands below the baseline it was sized for.
    check("EVERY open-loop-sized station was SHORT of its own baseline",
          all(station_open_loop_rescaled(mw)["households"]
              < STATION_HOUSEHOLDS for mw in SPALL_TARGET_MW.values()))
    check("  -- and the base station at the ADS convention was not, which is"
          " why it was not caught there",
          station_open_loop()["households"] >= STATION_HOUSEHOLDS)
    check("  -- indeed the closed loop returns that station unchanged",
          station()["modules"] == station_open_loop()["modules"])
    check("closing the loop meets the baseline",
          _meets["households"] >= STATION_HOUSEHOLDS)
    check("  -- and needs NO new driver, at every target power",
          all(rescaled_station(mw)["linacs"]
              <= station_open_loop_rescaled(mw)["linacs"]
              for mw in SPALL_TARGET_MW.values()))
    check("at the ESS row the baseline-meeting station strands nothing",
          _meets["driver_stranded_mw"] == 0.0)
    check("  -- so the beam that closes the shortfall was already installed",
          _meets["beam_mw"] <= _built["driver_installed_mw"])
    _inside, _cross_a = marginal_net_mw(_meets["modules"], _ess,
                                        k_eff=K_DESIGN)
    _nx = _meets["modules"] + 1
    while not marginal_net_mw(_nx, _ess, k_eff=K_DESIGN)[1]:
        _nx += 1
    _across, _cross_b = marginal_net_mw(_nx, _ess, k_eff=K_DESIGN)
    check("the boundary module is identified as the one that buys a driver",
          _cross_b and not _cross_a)
    check("the marginal module beats the average -- the standby is fixed",
          _inside > _meets["net_mw"] / _meets["beam_mw"])
    check("  -- and a module inside capacity beats one that buys a driver",
          _inside > _across)
    # AND WHAT IT DOES NOT SPEND. k is composition; source strength is not.
    check("adding modules does not move k",
          built_station(_meets["modules"] + 4, _ess, k_eff=K_DESIGN)["k"]
          == _meets["k"])
    check("  -- so the subcritical margin is unchanged by it",
          subcritical_margin(built_station(_meets["modules"] + 4, _ess,
                                           k_eff=K_DESIGN)["k"])
          == subcritical_margin(_meets["k"]))
    # THE CEILING IS OWED. The blanket is not split, so this is 1.39x the
    # power density in the SAME blanket, and every downstream inventory is
    # still computed at the station on the left of that comparison.
    check("the baseline-meeting station runs hotter than the station the"
          " inventories are computed at",
          _meets["thermal_mw"] > 1.3 * _base["thermal_mw"])
    check("  -- and the report says the ceiling is not computed here",
          "THE CEILING IS NOT COMPUTED HERE" in _capture_ps(report_driver))
    check("a station of no modules is refused",
          _raises_value(lambda: built_station(0)))
    check("a first module has no marginal figure",
          _raises_value(lambda: marginal_net_mw(1)))

    print()
    print("  the driver as a machine -- current, length and beam loss")
    # THE RELATION IS EXACT, not a fit: one milliamp through one gigavolt is
    # one megawatt. Pinned so the whole section cannot drift off arithmetic.
    check("P[MW] = I[mA] . E[GeV] exactly",
          abs(beam_current_ma(240.0, 8.0) - 30.0) < 1e-12)
    check("  -- so at fixed power the current is inverse in the energy",
          abs(beam_current_ma(20.0, 1.0)
              / beam_current_ma(20.0, 8.0) - 8.0) < 1e-12)
    _rec_n, _rec_i = record_current_ma("OPERATED")
    _des_n, _des_i = record_current_ma("DESIGN")
    check("the operated current record is PSI's",
          _rec_n == "PSI HIPA cyclotron")
    check("  -- and no OPERATED machine beats it",
          all(beam_current_ma(p, e) <= _rec_i + 1e-12
              for e, p, st in PROTON_MACHINES.values() if st == "OPERATED"))
    check("the designed record is above the operated one",
          _des_i > _rec_i)
    _ia = beam_current_ma(LINAC_BEAM_MW, BEAM_GEV)
    _ic = beam_current_ma(LINAC_BEAM_MW, ROUTE_C_GEV)
    # THE FINDING. --routes called route C's driver "machines that exist".
    # True of the energy, false of the current.
    check("route A's driver sits AT the operated current record",
          _ia < 1.2 * _rec_i)
    check("  -- and route C's is far past even the designed one",
          _ic > 4.0 * _des_i)
    check("  -- so 'machines that exist' is true of the energy, not the"
          " current",
          _ic / _ia > 7.9)
    check("and --routes now says so where it made the claim",
          "ON ENERGY, and NOT on current" in _capture_ps(report_routes))
    # THE LOSS BUDGET RUNS THE SAME WAY, and that is the counter-intuitive
    # half: longer is easier, because the allowance goes with length.
    check("the 1 W/m budget is looser at the higher energy",
          fractional_loss_requirement(LINAC_BEAM_MW, BEAM_GEV)
          > fractional_loss_requirement(LINAC_BEAM_MW, ROUTE_C_GEV))
    check("  -- by exactly the energy ratio, since power is fixed",
          abs(fractional_loss_requirement(LINAC_BEAM_MW, BEAM_GEV)
              / fractional_loss_requirement(LINAC_BEAM_MW, ROUTE_C_GEV)
              - BEAM_GEV / ROUTE_C_GEV) < 1e-9)
    # AND WHAT ROUTE C BUYS, so the section cannot be read as refuting it.
    _a = station(module_mw=SPALL_TARGET_MW["ESS, design"], k_eff=K_DESIGN)
    _c = station(module_mw=SPALL_TARGET_MW["ESS, design"], k_eff=K_DESIGN,
                 y_fus=0.0)
    check("route C is the shorter accelerator, and by a lot",
          _a["linacs"] * linac_length_m(BEAM_GEV)
          > 5.0 * _c["linacs"] * linac_length_m(ROUTE_C_GEV))
    check("  -- and it needs MORE beam, not less, having no fusion channel",
          _c["beam_mw"] > _a["beam_mw"])
    check("a current cap multiplies route C's driver count and not route A's",
          drivers_at_current_cap(_c["beam_mw"], ROUTE_C_GEV, _des_i)
          > 4 * _c["linacs"]
          and drivers_at_current_cap(_a["beam_mw"], BEAM_GEV, _des_i)
          <= _a["linacs"])
    check("the standby consequence of that is recorded as owed, not priced",
          "RECORDED AS OWED" in _capture_ps(report_current))
    check("  -- and the file refuses to decide the route on it",
          "DOES NOT DECIDE THE ROUTE" in _capture_ps(report_current))
    check("a zero or negative beam energy is refused",
          _raises_value(lambda: beam_current_ma(20.0, 0.0)))
    check("a non-positive current cap is refused",
          _raises_value(lambda: drivers_at_current_cap(240.0, 8.0, 0.0)))
    check("a status no machine carries is refused",
          _raises_value(lambda: record_current_ma("IMAGINED")))

    print()
    print("  the driver re-scaled, and the standby term that decides it")
    _built = max(p for e, p, st in LINAC_CLASS.values() if st == "OPERATED")
    _bldg = max(p for e, p, st in LINAC_CLASS.values() if st == "BUILDING")
    _std = max(p for e, p, st in LINAC_CLASS.values() if st == "STUDIED")
    _at8 = max(p for e, p, st in LINAC_CLASS.values() if e >= BEAM_GEV)
    check("the assumed driver is larger than anything under construction",
          LINAC_BEAM_MW > _bldg)
    check("  -- and larger than anything ever studied",
          LINAC_BEAM_MW > _std)
    check("  -- and several times the largest studied at route A's energy",
          LINAC_BEAM_MW / _at8 >= 4.0)
    # THE FINDING, and it is a spread rather than a number: the standby's
    # scaling law is not stated anywhere, and the two ends are a whole plant
    # apart. Pinned so it cannot be quietly resolved by picking one.
    _fix = station_at_driver(_built, standby_fixed)
    _sca = station_at_driver(_built, standby_scaled)
    check("at a driver of operated size the two standby readings diverge",
          standby_load_mw(_fix) > 10.0 * standby_load_mw(_sca))
    check("  -- by a load comparable to the whole station's net output",
          standby_load_mw(_fix) - standby_load_mw(_sca)
          > 0.5 * station_at_driver(LINAC_BEAM_MW)["net_mw"])
    check("  -- and the beam follows it, at one end and not the other",
          _fix["beam_mw"] > 1.5 * _sca["beam_mw"])
    check("scaled standby makes the division of the beam free",
          abs(standby_load_mw(station_at_driver(5.0, standby_scaled))
              - standby_load_mw(station_at_driver(LINAC_BEAM_MW,
                                                  standby_scaled))) < 1.0)
    check("the assumed driver is kept rather than re-chosen",
          "THE DESIGN KEEPS ITS ASSUMED" in
          _capture_ps(report_linac).upper())
    check("a driver of no power is refused",
          _raises_value(lambda: built_station(1, linac_mw=0.0)))

    print()
    print("  the blanket ceiling, bounded")
    _base = station(k_eff=K_SAFE)
    _fill = station(module_mw=SPALL_TARGET_MW["ESS, design"], k_eff=K_DESIGN)
    _d0 = blanket_density(_base)[2]
    _d1 = blanket_density(_fill)[2]
    # THE CORRECTION --driver OWED. The inventory scales with the heat, so a
    # bigger station is bigger and not denser.
    check("the circuit power density does not move with station size",
          abs(_d1 / _d0 - 1.0) < 1e-9)
    check("  -- and --driver now says so where it read it the other way",
          "IT DOES NOT" in _capture_ps(report_driver))
    check("the plant is less dense than the one published circuit figure",
          beam_headroom_to() > 1.0)
    check("  -- and a CORE figure is refused as a comparison",
          _raises_value(lambda: beam_headroom_to("MSFR, core only")))
    check("the headroom is stated as an assumption's doing, not as margin",
          "may not be quoted as margin" in _capture_ps(report_blanket))
    sys.path.insert(0, HERE)
    import restart as _R
    check("the decay model reproduces the published MSRE figure",
          0.9 < _R.decay_fraction(MSRE_DECAY_T_S) / MSRE_DECAY_FRACTION < 1.2)
    # THE TRANSIENT IS INVARIANT because both terms scale with the power.
    check("the adiabatic rise is invariant in station size",
          abs(decay_removal_duty_mw(_fill) / _fill["thermal_mw"]
              - decay_removal_duty_mw(_base) / _base["thermal_mw"]) < 1e-12)
    check("  -- while the removal DUTY is not, and is many passive systems",
          decay_removal_duty_mw(_fill) / DRACS_MW > 10.0)
    check("a zero volume has no power density",
          _raises_value(lambda: power_density_mw_m3(100.0, 0.0)))

    print()
    print(f"selftest: {fail} failures -> {'PASS' if fail == 0 else 'FAIL'}")
    return 1 if fail else 0


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--selftest", action="store_true")
    ap.add_argument("--spallation", action="store_true",
                    help=report_spallation.__doc__)
    ap.add_argument("--target", action="store_true", help=report_target.__doc__)
    ap.add_argument("--plant", action="store_true", help=report_plant.__doc__)
    ap.add_argument("--stability", action="store_true",
                    help=report_stability.__doc__)
    ap.add_argument("--fuel", action="store_true", help=report_fuel.__doc__)
    ap.add_argument("--scale", action="store_true", help=report_scale.__doc__)
    ap.add_argument("--tritium", action="store_true",
                    help=report_tritium.__doc__)
    ap.add_argument("--station", action="store_true",
                    help=report_station.__doc__)
    ap.add_argument("--ignition", action="store_true",
                    help=report_ignition.__doc__)
    ap.add_argument("--routes", action="store_true",
                    help=report_routes.__doc__)
    ap.add_argument("--rescale", action="store_true",
                    help="the station rebuilt at the adopted operating point")
    ap.add_argument("--driver", action="store_true", help=report_driver.__doc__)
    ap.add_argument("--current", action="store_true",
                    help=report_current.__doc__)
    ap.add_argument("--linac", action="store_true", help=report_linac.__doc__)
    ap.add_argument("--blanket", action="store_true",
                    help=report_blanket.__doc__)
    a = ap.parse_args()
    if a.selftest:
        return selftest()
    if a.spallation:
        return report_spallation()
    if a.target:
        return report_target()
    if a.plant:
        return report_plant()
    if a.stability:
        return report_stability()
    if a.fuel:
        return report_fuel()
    if a.scale:
        return report_scale()
    if a.tritium:
        return report_tritium()
    if a.station:
        return report_station()
    if a.ignition:
        return report_ignition()
    if a.routes:
        return report_routes()
    if a.rescale:
        return report_rescale()
    if a.driver:
        return report_driver()
    if a.current:
        return report_current()
    if a.linac:
        return report_linac()
    if a.blanket:
        return report_blanket()
    return report()


if __name__ == "__main__":
    sys.exit(main())
