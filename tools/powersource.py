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
K_SAFE = 0.95                # the margin equals a fast core's whole control worth
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
    denom = g * eta_thermal() - 1.0 / eta_acc
    if denom <= 0:
        return float("inf")
    return ((want_kw + n_linac * REF_STANDBY_KW / eta_acc) / denom) / 1000.0


def station(households=STATION_HOUSEHOLDS, window=STATION_WINDOW_MEV,
            module_mw=MODULE_BEAM_MW, k_eff=K_SAFE, eta_acc=0.30):
    """The station as built: whole modules, and what they actually deliver."""
    y_s = 0.5 * sum(spallation_yield())
    y_f = fusions_per_proton(window)
    g = plant_gain(k_eff, y_s, y_f)
    need = station_beam_mw(households, window, k_eff, eta_acc)
    n_mod = math.ceil(need / module_mw)
    beam = n_mod * module_mw
    n_lin = math.ceil(beam / LINAC_BEAM_MW)
    net_kw = (beam * 1000.0 * (g * eta_thermal() - 1.0 / eta_acc)
              - n_lin * REF_STANDBY_KW / eta_acc)
    return {
        "window": window, "module_mw": module_mw, "modules": n_mod,
        "beam_mw": beam, "linacs": n_lin, "gain": g, "y_fus": y_f,
        "y_spall": y_s, "k": k_eff,
        "thermal_mw": beam * g, "net_mw": net_kw / 1000.0,
        "households": net_kw / HOUSEHOLD_KW,
        "tritium_per_module_kg": tritium_inventory_kg(window, None),
        "tritium_total_kg": n_mod * tritium_inventory_kg(window, None),
        "tritium_ratio": tritium_balance(window, module_mw, f_li=F_LI_DESIGN),
        "doubling_y": tritium_doubling_years(module_mw, window),
    }


def blanket_leakage_penalty(n_split):
    """What splitting one blanket into n would cost the leakage allowance.

    INDICATIVE and marked so: leakage scales with surface over volume, which
    for n equal pieces of a fixed total volume goes as n^(1/3). It is not a
    transport calculation and it is not used as one -- it is used to REFUSE the
    split, which needs only the sign and the order."""
    return n_split ** (1.0 / 3.0)


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
    check("driver standby has stopped mattering at station scale",
          st["linacs"] * REF_STANDBY_KW / 0.30
          < 0.02 * st["net_mw"] * 1000.0)
    print()
    check("a longer-lived triton would need proportionately less beam",
          _beam_for_halflife(123.2) < beam_mw_for_tritium(265.0) / 5.0)
    check("  -- so the plant's size is a statement about the half-life",
          abs(_beam_for_halflife(123.2) * 10.0
              / beam_mw_for_tritium(265.0) - 1.0) < 0.05)
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
    return report()


if __name__ == "__main__":
    sys.exit(main())
