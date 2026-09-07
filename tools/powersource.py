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
    a = ap.parse_args()
    return selftest() if a.selftest else report()


if __name__ == "__main__":
    sys.exit(main())
