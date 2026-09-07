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
import argparse
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
    print("  the instrument can fail: a blanket that could not supply the")
    print("  requirement would have to need k >= 1, so that case is constructed")
    check("a requirement of 100 GeV per fusion would need k >= 1",
          k_for_energy(100000.0) > 0.99)
    print("    -- so the content of the result is that the requirement lands")
    print("       DEEPLY subcritical, which is a fact about the numbers")

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
    return report()


if __name__ == "__main__":
    sys.exit(main())
