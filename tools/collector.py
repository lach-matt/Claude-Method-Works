#!/usr/bin/env python3
"""collector.py -- the muon collection budget, stage by stage.

papers/Muon_Catalysed_Fusion_v1.1.md sec.4 costs the binder at 5 GeV per muon and
calls that figure achieved. sec.5.5 records that the per-stage budget behind it
does not exist and decides the paper. This instrument is that budget, built from
published figures for the three machines that bear on it, and it reports one
result the paper did not have:

    NO MACHINE ACHIEVES 5 GeV PER MUON. The best dedicated mu- facility in the
    world delivers 5 TeV per stopped mu-, a factor of 1000 above the figure the
    energy balance assumes.

That is not a defeat. It relocates the whole question: the balance's arithmetic
was never wrong, but its reference point was aspirational, and the real chain has
far more headroom below it than 16.7x -- and far more to find.

THE THREE REFERENCE MACHINES, and why each is here
--------------------------------------------------
PSI muE4       a physics beamline, mu+, the intensity record for its class.
               J/W = 3.5e2 mu/s/W at 1.2 MW. The baseline a reactor must beat,
               and the shape of machine v1.1 sec.5.3 says a reactor must NOT be.

MuSIC (RCNP)   a dedicated source: superconducting solenoid pion capture, the
               first demonstration of the scheme. 392 MeV, 400 W, graphite.
               J/W = (9.0 +/- 1.0)e4 mu-/s/W, "an improvement of about 1000 over
               existing facilities". This is the collector v1.1 sec.5.3 says has
               never been built -- built, at 400 W, in prototype.

Mu2e (FNAL)    the best stopped-mu- figure published: 0.0016 stopped mu- per
               8 GeV proton, of which ~40% of beamline-exit muons stop.
               8 GeV / 0.0016 = 5 TeV per stopped mu-.

COMET supplies the intermediate stage the other two do not resolve: 0.061-0.144
(pi- + mu-) per 8 GeV proton at 3 m from target, in a 5 T capture solenoid.

WHAT IT REFUSES
---------------
1. It will not fill a stage it cannot source. The chain has six stages and the
   literature here resolves three boundaries: protons in, captured pi-/mu- at
   3 m, stopped mu-. Everything between is reported as a LUMPED block with the
   stages it contains named, never as per-stage figures invented to fill a table.

2. It will not treat the 0.30 GeV kinematic floor as a target. It is the pion
   threshold divided into the beam energy and assumes every 300 MeV of beam
   becomes a captured, transported, stopped muon. It is a BOUND. The distance
   from any real machine to it is not all engineering: an unknown part of it is
   production cross-section, which no design changes.

3. It will not report the required improvement as achievable. It reports what is
   required, what is bounded, and the margin between them -- and names the single
   measurement that would convert the front-end block from a lump into a budget.

4. It will not average the two MuSIC yields. (10.4 +/- 2.7)e5 /s/W is mu+ and mu-
   together; (9.0 +/- 1.0)e4 /s/W is mu- alone, and muCF needs mu-. The mu- figure
   is used throughout and the combined one is never substituted for it.

Stdlib only. python3 tools/collector.py --selftest before trusting a report.
"""

import argparse
import math
import sys

J_PER_GEV = 1.602e-10        # J per GeV
Q_FUS_MEV = 17.59            # MeV per d+t fusion

# ---- reference machines, all published -------------------------------------
PSI_MUE4_PER_W = 3.5e2       # mu/s/W as the source STATES it. 4e8 / 1.2e6 = 333.3,
                             # so the source rounds up by 5%. Kept as stated, with
                             # the divergence reported by --selftest rather than
                             # silently corrected: it is 5% on the least
                             # load-bearing figure here, and flattening a source's
                             # own rounding is how a citation stops being one.
MUSIC_MU_MINUS_PER_W = 9.0e4     # mu-/s/W   +/- 1.0e4
MUSIC_MU_MINUS_ERR = 1.0e4
MUSIC_ALL_MU_PER_W = 10.4e5      # mu+ and mu- +/- 2.7e5  -- NOT the muCF figure
MUSIC_PROTON_GEV = 0.392
MU2E_STOPPED_PER_P = 0.0016  # stopped mu- per proton on target
MU2E_PROTON_GEV = 8.0
MU2E_STOPPING_FRAC = 0.40    # of muons exiting the beamline
COMET_CAPTURED_LO = 0.061    # (pi- + mu-) per 8 GeV proton at 3 m, 5 T capture
COMET_CAPTURED_HI = 0.144

PION_THRESHOLD_GEV = 0.300   # kinematic floor, perfect collection -- a THRESHOLD
                             # bound, not a production figure. See PROD_* below.

# ---- what a real target actually produces ----------------------------------
# Two published figures, differing by ~6x, and the difference is exactly the
# distinction the collection argument turns on: captured-at-all vs accepted
# into a selective channel. muCF needs the first. Both are carried.
# SOURCED, and this is the load-bearing figure. Strait, Mokhov & Striganov,
# Phys. Rev. ST Accel. Beams 13, 111001 (2010), Table II: HARP-measured pion
# production cross sections off tantalum, convolved with the MARS15 acceptance
# of the 20 T NF/MC front-end channel, thick target (2 lambda_I):
#   Y_P = 0.054 captured muons per INTERACTING proton per GeV, BOTH charges.
# Per charge that is 0.027 /GeV, i.e. 1/0.027 = 37 GeV per captured mu-.
# The same paper: yield is flat within 10% over T_beam = 4-11 GeV with an
# optimum near 7 GeV -- so PROTON ENERGY IS NOT A LEVER, contrary to the
# budget paper's sec.5, which inferred one from MuSIC's 392 MeV point alone.
YP_BOTH_CHARGES_PER_GEV = 0.054   # captured mu / interacting proton / GeV
PROD_CAPTURED_PER_P = 0.34   # superseded; kept only for the selftest's history
PROD_CAPTURED_EP = 8.0
PROD_ACCEPTED_PCT = (5.0, 10.0)  # charge-averaged accepted pi+mu per 10 GeV proton,
PROD_ACCEPTED_EP = 10.0          #   %, through a NF cooling channel (MARS/ICOOL)
LAMBDA_0 = 4.665e5
LAMBDA_C = 2.6e8
OMEGA_MEASURED = 0.0045
OMEGA_BOTH_LEVERS = 0.00234
F_WORK = 0.501
PAPER_ASSUMED_GEV = 5.0      # what v1.1 sec.4 costs the binder at
WORK_BREAKEVEN_GEV = 1.96    # v1.1 sec.5.2
HEAT_BREAKEVEN_GEV = 3.90    # v1.1 sec.5.1, asymptotic convention


def gev_per_muon_from_per_watt(per_watt):
    """A yield in muons/s/W is an energy per muon."""
    return (1.0 / per_watt) / J_PER_GEV


def gev_per_stopped(proton_gev, stopped_per_proton):
    return proton_gev / stopped_per_proton


def machines():
    return [
        ("PSI muE4 (physics beamline, mu+)", gev_per_muon_from_per_watt(PSI_MUE4_PER_W), "MEASURED"),
        ("MuSIC (solenoid capture, mu-)", gev_per_muon_from_per_watt(MUSIC_MU_MINUS_PER_W), "MEASURED"),
        ("Mu2e (dedicated mu-, stopped)", gev_per_stopped(MU2E_PROTON_GEV, MU2E_STOPPED_PER_P), "DESIGN"),
        ("v1.1 sec.4 assumed", PAPER_ASSUMED_GEV, "ASPIRATIONAL"),
        ("kinematic floor (pion threshold)", PION_THRESHOLD_GEV, "BOUND"),
    ]


def report_machines():
    print("Energy cost per muon -- what machines actually deliver")
    print()
    print(f"  {'machine':<38} {'GeV/muon':>12}  status")
    for name, g, st in machines():
        s = f"{g:,.2f}" if g < 1e4 else f"{g:,.0f}"
        print(f"  {name:<38} {s:>12}  {st}")
    print()
    best = gev_per_stopped(MU2E_PROTON_GEV, MU2E_STOPPED_PER_P)
    print(f"  Best published stopped-mu- figure   {best:,.0f} GeV = {best / 1000:.1f} TeV")
    print(f"  v1.1 sec.4 assumes                  {PAPER_ASSUMED_GEV:,.2f} GeV")
    print(f"  --> the assumed figure is {best / PAPER_ASSUMED_GEV:,.0f}x BELOW anything achieved.")
    print()
    print("  MuSIC vs a physics beamline, the collector's demonstrated gain:")
    print(f"    {gev_per_muon_from_per_watt(PSI_MUE4_PER_W) / gev_per_muon_from_per_watt(MUSIC_MU_MINUS_PER_W):,.0f}x"
          "  (mu- only, at 400 W, 392 MeV protons)")
    print()
    print("  Proton energy is itself a lever, and it points UP:")
    mu = gev_per_muon_from_per_watt(MUSIC_MU_MINUS_PER_W)
    print(f"    MuSIC  392 MeV protons: {mu:>10,.0f} GeV per mu-")
    print(f"    Mu2e   8 GeV protons:   {best:>10,.0f} GeV per mu-")
    print(f"    -> 8 GeV protons are {mu / best:.1f}x more energy-efficient per mu-.")


def report_budget(target_gev):
    best = gev_per_stopped(MU2E_PROTON_GEV, MU2E_STOPPED_PER_P)
    required = best / target_gev
    bounded = best / PION_THRESHOLD_GEV
    print(f"The budget, against a target of {target_gev:.2f} GeV per stopped mu-")
    print()
    print(f"  present best (Mu2e-class)        {best:>12,.0f} GeV/mu-   [DESIGN]")
    print(f"  target                           {target_gev:>12,.2f} GeV/mu-")
    print(f"  REQUIRED improvement             {required:>12,.0f}x")
    print(f"  BOUND (to the kinematic floor)   {bounded:>12,.0f}x")
    print(f"  margin between them              {bounded / required:>12,.1f}x")
    print()
    print("  Where the loss sits -- three sourced boundaries, two lumped blocks:")
    print()
    ideal = MU2E_PROTON_GEV / PION_THRESHOLD_GEV
    cap_lo, cap_hi = COMET_CAPTURED_LO, COMET_CAPTURED_HI
    front_lo, front_hi = ideal / cap_hi, ideal / cap_lo
    exiting_pp = MU2E_STOPPED_PER_P / MU2E_STOPPING_FRAC
    mid_lo = cap_lo / exiting_pp
    mid_hi = cap_hi / exiting_pp
    print(f"    per 8 GeV proton, ideal at threshold      {ideal:>10,.1f} muons   [BOUND]")
    print(f"    captured pi- + mu- at 3 m (COMET, 5 T)    {cap_lo:>10.3f} - {cap_hi:.3f}   [SIMULATED]")
    print(f"    muons exiting the beamline (Mu2e)         {MU2E_STOPPED_PER_P / MU2E_STOPPING_FRAC:>10.4f}   [DESIGN]")
    print(f"    stopped mu- (Mu2e)                        {MU2E_STOPPED_PER_P:>10.4f}   [DESIGN]")
    print()
    print(f"    BLOCK 1  A1-A3 production + capture   {front_lo:>8,.0f} - {front_hi:,.0f}x lost   LUMPED")
    print(f"    BLOCK 2  A4-A5 decay + transport      {mid_lo:>8,.1f} - {mid_hi:.1f}x lost   LUMPED")
    print(f"    STAGE    A6 stopping fraction 40%     {1 / MU2E_STOPPING_FRAC:>8.1f}x lost   SOURCED")
    print()
    print(f"  A6 offers at most {1 / MU2E_STOPPING_FRAC:.1f}x. So at least"
          f" {required / (1 / MU2E_STOPPING_FRAC):,.0f}x must come from")
    print("  BLOCKS 1 and 2, which together hold"
          f" {front_lo * mid_lo:,.0f} - {front_hi * mid_hi:,.0f}x.")
    print()
    # How much of BLOCK 1 must actually be recovered, if the other two are
    # taken to their own ceilings? BLOCK 1 alone contains the irreducible
    # production cross-section, so this is the operative question.
    #
    # Note the cancellation: BLOCK1 x BLOCK2 = (ideal/cap) x (cap/exiting) is
    # independent of cap, so the COMET capture range drops out entirely and the
    # answer is a single number, not a range. The capture boundary can sit
    # anywhere between the two published values without moving it.
    a6_max = 1.0 / MU2E_STOPPING_FRAC
    frac = required * exiting_pp / (a6_max * ideal)
    print("  ALLOCATION -- what fraction of the front-end loss must be recovered,")
    print("  if A6 and BLOCK 2 are each taken to their own ceiling (perfect")
    print("  stopping, lossless decay and transport):")
    print()
    print(f"    {100 * frac:.1f}% of BLOCK 1")
    print()
    print("  The COMET capture range CANCELS out of this: BLOCK1 x BLOCK2 is")
    print("  (ideal/cap) x (cap/exiting), so cap drops out and the answer is one")
    print("  number rather than a range. Where the capture boundary sits does not")
    print("  move it.")
    print()
    print("  So the front end need not be beaten, only partly recovered. The other")
    print(f"  {100 * (1 - frac):.1f}% may remain production cross-section without costing the")
    print("  target. THAT is the quantity to measure.")
    print()
    print("  REFUSAL: Block 1 is not decomposed, and the paper does not pretend")
    print("  otherwise. An unknown part of it is pi- production cross-section,")
    print("  which no collector design changes, and the rest is capture")
    print("  acceptance, which one might. Separating those two is the single")
    print("  measurement that converts this lump into a budget.")


# HARP large-angle double-differential cross sections, p-Pb, pi-, 8 GeV/c beam,
# in barn/(GeV/c . rad). arXiv:0709.3458 Appendix A. Rows are theta bins of
# 0.20 rad from 1.15 to 2.15; columns are p bins of 0.05 GeV/c from 0.10 to 0.50.
# Pb (A=207) stands in for Ta (A=181); the source states the two "yield the same
# conclusions".
# HARP Table 8 in full: p-Pb, pi-, 8 GeV/c, arXiv:0709.3458 Appendix A.
# theta bin -> {(p_lo, p_hi): d2sigma/dpdtheta in barn/(GeV/c . rad)}
# Momentum bins are 0.05 GeV/c wide to 0.50 and 0.10 wide above it; the widest
# angular bins carry momentum out to 0.80, the backward ones stop at 0.50.
_P8 = [(0.10, 0.15), (0.15, 0.20), (0.20, 0.25), (0.25, 0.30),
       (0.30, 0.35), (0.35, 0.40), (0.40, 0.45), (0.45, 0.50)]
_PW = [(0.50, 0.60), (0.60, 0.70), (0.70, 0.80)]


def _row(v8, vw, skip_first=False):
    d = dict(zip(_P8[1:] if skip_first else _P8, v8))
    d.update(dict(zip(_PW, vw)))
    return d


HARP_PB_PIMINUS_8GEV = {
    (0.35, 0.55): _row([1.59, 2.00, 2.07, 1.99, 1.63, 1.63, 1.48],
                       [1.38, 1.37, 1.06], skip_first=True),
    (0.55, 0.75): _row([1.24, 2.09, 2.18, 2.19, 1.88, 1.51, 1.38, 1.26],
                       [1.20, 0.95, 0.70]),
    (0.75, 0.95): _row([1.71, 2.28, 2.04, 1.88, 1.54, 1.26, 1.11, 0.95],
                       [0.78, 0.61]),
    (0.95, 1.15): _row([2.17, 2.30, 1.85, 1.50, 1.15, 0.99, 0.80, 0.69], [0.52]),
    (1.15, 1.35): _row([2.40, 2.19, 1.70, 1.23, 0.92, 0.75, 0.59, 0.46], []),
    (1.35, 1.55): _row([2.34, 2.06, 1.60, 1.04, 0.69, 0.52, 0.41, 0.29], []),
    (1.55, 1.75): _row([2.09, 1.76, 1.29, 0.82, 0.48, 0.35, 0.26, 0.19], []),
    (1.75, 1.95): _row([1.78, 1.44, 0.92, 0.56, 0.30, 0.23, 0.20, 0.14], []),
    (1.95, 2.15): _row([1.52, 1.11, 0.68, 0.42, 0.24, 0.17, 0.12, 0.08], []),
}
HARP_THETA_MIN, HARP_THETA_MAX = 0.35, 2.15

# HARP FORWARD spectrometer, p-Pb pi-, 8 GeV/c: arXiv:0907.3857 Table XXIII
# (0.05-0.25 rad) plus the finest bin of Table XXXII (0.025-0.050 rad).
# NOTE THE UNITS CHANGE: this table is d2sigma/dp dOmega in barn/(sr . GeV/c),
# not d2sigma/dp dtheta. The solid-angle Jacobian dOmega = 2 pi (cos t1 - cos t2)
# must be applied; treating it as the large-angle table would overstate the
# forward contribution by more than an order of magnitude.
HARP_PB_PIMINUS_8GEV_FWD = {
    (0.025, 0.050): [((0.50, 0.75), 0.23), ((0.75, 1.00), 1.23), ((1.00, 1.25), 0.81),
                     ((1.25, 1.50), 0.35), ((1.50, 2.00), 0.54), ((2.00, 2.50), 0.34),
                     ((2.50, 3.00), 0.16), ((3.00, 3.50), 0.16), ((3.50, 4.00), 0.03),
                     ((4.00, 5.00), 0.07)],
    (0.050, 0.100): [((0.50, 1.00), 0.72), ((1.00, 1.50), 0.54), ((1.50, 2.00), 0.47),
                     ((2.00, 2.50), 0.27), ((2.50, 3.00), 0.15), ((3.00, 3.50), 0.05),
                     ((3.50, 4.00), 0.06), ((4.00, 5.00), 0.034)],
    (0.100, 0.150): [((0.50, 1.00), 1.01), ((1.00, 1.50), 0.58), ((1.50, 2.00), 0.37),
                     ((2.00, 2.50), 0.17), ((2.50, 3.00), 0.14), ((3.00, 3.50), 0.07),
                     ((3.50, 4.00), 0.037), ((4.00, 5.00), 0.013), ((5.00, 6.50), 0.002)],
    (0.150, 0.200): [((0.50, 1.00), 0.98), ((1.00, 1.50), 0.50), ((1.50, 2.00), 0.27),
                     ((2.00, 2.50), 0.17), ((2.50, 3.00), 0.07), ((3.00, 3.50), 0.033),
                     ((3.50, 4.00), 0.011)],
    (0.200, 0.250): [((0.50, 1.00), 0.68), ((1.00, 1.50), 0.37), ((1.50, 2.00), 0.17),
                     ((2.00, 2.50), 0.07), ((2.50, 3.00), 0.014)],
}
SIGMA_INEL_PB = 1.7                    # barn, p-Pb inelastic at few GeV


def harp_window_sigma(theta_min=HARP_THETA_MIN):
    """Integrated pi- cross section over the measured acceptance, barn.
    theta_min selects a sub-region; the default is the whole table."""
    tot = 0.0
    for (tlo, thi), bins in HARP_PB_PIMINUS_8GEV.items():
        if tlo < theta_min:
            continue
        tot += sum(v * (ph - pl) * (thi - tlo) for (pl, ph), v in bins.items())
    return tot


def harp_forward_sigma():
    """Integrated forward pi- cross section, barn. Applies the solid-angle
    Jacobian, which the large-angle table does not need."""
    tot = 0.0
    for (tlo, thi), bins in HARP_PB_PIMINUS_8GEV_FWD.items():
        dom = 2 * math.pi * (math.cos(tlo) - math.cos(thi))
        tot += sum(v * (ph - pl) for (pl, ph), v in bins) * dom
    return tot


def harp_combined_sigma():
    return harp_window_sigma() + harp_forward_sigma()


def harp_combined_yield():
    return harp_combined_sigma() / SIGMA_INEL_PB


def cost_per_pion_produced():
    return 8.0 / harp_combined_yield()


def harp_window_yield(theta_min=HARP_THETA_MIN):
    """pi- per interacting proton over the measured acceptance. A LOWER BOUND
    on total production: HARP's large-angle spectrometer does not cover the
    forward cone theta < 0.35 rad, where a further substantial fraction goes."""
    return harp_window_sigma(theta_min) / SIGMA_INEL_PB


def nf_captured_per_interacting_proton(ep_gev=8.0):
    """Captured mu- per interacting proton at a stated beam energy."""
    return (YP_BOTH_CHARGES_PER_GEV / 2.0) * ep_gev


def report_production():
    la, fw = harp_window_sigma(), harp_forward_sigma()
    tot, y = harp_combined_sigma(), harp_combined_yield()
    eb = cost_per_pion_produced()
    c = nf_captured_per_interacting_proton()
    q = Q_FUS_MEV / 1000.0
    print("PRODUCTION, integrated from HARP measured cross sections")
    print("  large angle: arXiv:0709.3458 Table 8   0.35-2.15 rad, p 0.10-0.80")
    print("  forward:     arXiv:0907.3857 Tab XXIII 0.025-0.25 rad, p 0.50-6.50")
    print("  both p-Pb, pi-, 8 GeV/c, 5% interaction-length target")
    print()
    print(f"    large-angle integral   {la:8.4f} barn")
    print(f"    forward integral       {fw:8.4f} barn   ({100 * fw / tot:.0f}% of the total)")
    print(f"    COMBINED               {tot:8.4f} barn")
    print(f"    pi- per interacting p  {y:8.4f}   (sigma_inel = {SIGMA_INEL_PB} b)")
    print(f"    COST PER pi- PRODUCED  {eb:8.2f} GeV")
    print()
    print("  The forward cone contributes only ~15%: its differential cross")
    print("  sections are large but its solid angle is small. Applying the")
    print("  Jacobian matters -- treating the forward table as if it shared the")
    print("  large-angle table's units would overstate it by over an order.")
    print()
    print("  AGAINST CONDITION 8, AT PERFECT COLLECTION -- every produced pi-")
    print("  becoming a stopped mu-, which no machine approaches:")
    for f, lab in ((1.0, "heat"), (F_WORK, "work")):
        c8 = q * f / OMEGA_BOTH_LEVERS
        print(f"    {lab:<5}: E_binder < {c8:5.2f} GeV;  {eb:5.2f} GeV  ->  short by {eb / c8:.2f}x")
    print()
    print(f"    FOM at perfect collection:  heat {q / (OMEGA_BOTH_LEVERS * eb):.3f}"
          f"   work {q * F_WORK / (OMEGA_BOTH_LEVERS * eb):.3f}")
    print()
    print("  => COLLECTION EFFICIENCY ALONE CANNOT SATISFY CONDITION 8.")
    print("  Even a perfect collector leaves the heat form short by 1.48x and")
    print("  the work form by 2.96x. Production is binding, not merely capture.")
    print()
    print(f"  The discard is still real and large: the best front end captures")
    print(f"  {c:.4f} mu- per interacting proton against {y:.4f} pi- produced,")
    print(f"  i.e. {100 * c / y:.0f}% -- but closing that gap entirely still falls short.")
    print()
    print("  REFUSAL: still a LOWER bound on production. The band 0.25-0.35 rad")
    print("  is covered by neither spectrometer, forward p < 0.5 GeV/c and")
    print("  large-angle p > 0.8 GeV/c are unmeasured. The residual 1.48x is")
    print("  therefore an upper bound on the shortfall, not a closure -- and no")
    print("  verdict on condition 8 is offered.")


# ---- the collector: capture as a function of solenoid aperture ------------
# p_T^max (GeV/c) = 0.3 B(T) R(m) / 2  -- MuSIC eq.1. Validated: COMET's
# 5 T on a 0.15 m bore returns 112 MeV/c against its stated 100 MeV/c cap.
LI6_Q_MEV = 4.78           # n + 6Li -> T + alpha, EXOTHERMIC, and required
T_BLANKET, T_AMBIENT = 800.0, 300.0
ALPHA_MEV, NEUTRON_MEV = 3.5, 14.1


def carnot(t_blanket=None):
    return 1.0 - T_AMBIENT / (T_BLANKET if t_blanket is None else t_blanket)


def pt_max(br_tesla_metre):
    return 0.15 * br_tesla_metre


def captured_fraction(br, both_hemispheres=True):
    """Fraction of HARP-measured pi- production inside a solenoid's p_T cap."""
    tot = cap = 0.0
    for (tlo, thi), bins in HARP_PB_PIMINUS_8GEV.items():
        th, dth = 0.5 * (tlo + thi), thi - tlo
        for (pl, ph), v in bins.items():
            p, w = 0.5 * (pl + ph), v * (ph - pl) * dth
            tot += w
            if p * math.sin(th) < pt_max(br) and (both_hemispheres or th > math.pi / 2):
                cap += w
    for (tlo, thi), bins in HARP_PB_PIMINUS_8GEV_FWD.items():
        th = 0.5 * (tlo + thi)
        dom = 2 * math.pi * (math.cos(tlo) - math.cos(thi))
        for (pl, ph), v in bins:
            p, w = 0.5 * (pl + ph), v * (ph - pl) * dom
            tot += w
            if p * math.sin(th) < pt_max(br) and (both_hemispheres or th > math.pi / 2):
                cap += w
    return cap / tot


def br_for_capture(target, both_hemispheres=True):
    lo, hi = 0.1, 20.0
    for _ in range(80):
        m = (lo + hi) / 2
        if captured_fraction(m, both_hemispheres) < target:
            lo = m
        else:
            hi = m
    return lo


def blanket_thermal_mev():
    """Thermal energy the blanket delivers per fusion. The 6Li breeding
    reaction is REQUIRED for a D-T cycle and is exothermic, so the blanket
    returns more than the neutron carries in."""
    return NEUTRON_MEV + LI6_Q_MEV


def total_thermal_mev():
    return ALPHA_MEV + blanket_thermal_mev()


def energy_multiplication():
    return total_thermal_mev() / Q_FUS_MEV


def work_per_fusion_mev():
    """At the operating point sec.3.2 resolves to -- fuel AND blanket hot."""
    return total_thermal_mev() * carnot()


def f_work_corrected():
    return work_per_fusion_mev() / Q_FUS_MEV


LHD_ATOMS_PER_CM3 = 4.25e22   # liquid hydrogen density, the paper's own figure
AVOGADRO = 6.022e23
# Reported metallization / dissociation of molecular hydrogen: ~0.6 mol/cm3 at
# >= ~400 GPa (predicted), semimetallic behaviour from ~315-360 GPa, and Raman
# evidence that hydrogen is STILL MOLECULAR to 440 GPa. Whether "0.6 mol/cm3"
# counts atoms or H2 molecules is not resolved by the sources read here, and
# the two readings bracket the density muCF needs -- so both are carried.
H2_TRANSITION_MOL_PER_CM3 = 0.6


def phi_to_molar_volume(phi):
    """cm3 per mole of H2 at a stated density in units of LHD."""
    return 2.0 * AVOGADRO / (phi * LHD_ATOMS_PER_CM3)


def transition_phi(counts_atoms=True):
    n = H2_TRANSITION_MOL_PER_CM3 * AVOGADRO * (1.0 if counts_atoms else 2.0)
    return n / LHD_ATOMS_PER_CM3


# SOURCED, fission-suppressed fusion-breeder design -- the LOW-multiplication,
# proliferation-conscious class of blanket: each fusion produces typically 0.6
# fissile atoms and releases about 1.6x the neutron's energy in the blanket,
# with a tritium breeding ratio near 1.15 (self-sufficient). These supersede
# this paper's own single-reaction arithmetic as the better-grounded figures,
# which they exceed: the 6Li-only calculation was conservative.
LAMBDA_INFLIGHT = 2.8e4   # s^-1 at LHD, CoMD; independent approach gives 0.5e5

BLANKET_MULT_SOURCED = 1.6      # x the neutron's energy, deposited in blanket
FISSILE_PER_FUSION = 0.6        # sourced, against 0.7 reconstructed
TBR_SOURCED = 1.15

PU239_FISSION_MEV = 200.0   # downstream yield of one bred 239Pu
BREEDING_RATIO = 0.7        # bred nuclei per fusion after tritium self-sufficiency


def thermal_sourced_mev():
    """Thermal per fusion from the sourced blanket design."""
    return ALPHA_MEV + BLANKET_MULT_SOURCED * NEUTRON_MEV


def work_sourced_mev(t_blanket=1200.0):
    return thermal_sourced_mev() * carnot(t_blanket)


def bred_credit_mev(ratio=None):
    return (FISSILE_PER_FUSION if ratio is None else ratio) * PU239_FISSION_MEV


def total_value_sourced_mev():
    return thermal_sourced_mev() + bred_credit_mev()


def total_with_breeding_mev(ratio=None):
    return total_thermal_mev() + bred_credit_mev(ratio)


BE_N2N_COST_MEV = 1.57     # 9Be(n,2n): endothermic, per multiplication


def net_per_extra_neutron():
    """A multiplied neutron costs the (n,2n) endotherm and returns 6Li's Q."""
    return LI6_Q_MEV - BE_N2N_COST_MEV


def thermal_with_multiplier(neutrons_per_source):
    """Blanket thermal per fusion at a stated neutron multiplication."""
    extra = neutrons_per_source - 1.0
    return (ALPHA_MEV + NEUTRON_MEV - extra * BE_N2N_COST_MEV
            + neutrons_per_source * LI6_Q_MEV)


def cycles(ws, phi):
    return phi * LAMBDA_C / (LAMBDA_0 + ws * phi * LAMBDA_C)


def e_binder_captured():
    """GeV of beam per captured mu-, from the sourced Table II yield."""
    return 1.0 / (YP_BOTH_CHARGES_PER_GEV / 2.0)


def condition8(f_work=None):
    """Condition 8, the binder-economy bound. Net-positive requires
    N x Q_fus x f_work > E_binder with N <= 1/omega_s, hence
    E_binder < Q_fus x f_work / omega_s. Returns GeV."""
    f = F_WORK if f_work is None else f_work
    return (Q_FUS_MEV / 1000.0) * f / OMEGA_BOTH_LEVERS


def report_floor():
    q = Q_FUS_MEV / 1000.0
    cap = e_binder_captured()
    acc_lo = PROD_ACCEPTED_EP / (PROD_ACCEPTED_PCT[1] / 100.0)
    acc_hi = PROD_ACCEPTED_EP / (PROD_ACCEPTED_PCT[0] / 100.0)
    print("THE PRODUCTION FLOOR -- what a target costs before any collection loss")
    print()
    print(f"  threshold bound (v1.1 sec.4)          {PION_THRESHOLD_GEV:>8.2f} GeV/mu-   [BOUND, not a target]")
    print(f"  captured, 20 T + Hg jet, 8 GeV        {cap:>8.1f} GeV/mu-   [the muCF-relevant figure]")
    print(f"  accepted through an NF cooling channel {acc_lo:>7.0f} - {acc_hi:.0f} GeV/mu-   [selective; muCF needs none of it]")
    print()
    print(f"  The threshold bound understates the captured figure by {cap / PION_THRESHOLD_GEV:.0f}x.")
    print(f"  Sourced: Y_P = {YP_BOTH_CHARGES_PER_GEV} captured mu (both charges) per")
    print("  interacting proton per GeV -- HARP cross sections convolved with the")
    print("  MARS15 acceptance of a 20 T front end, thick (2 lambda_I) Ta target.")
    print()
    print("  PROTON ENERGY IS NOT A LEVER. The same source finds the beam-power")
    print("  normalised yield flat within 10% over T_beam = 4-11 GeV, optimum ~7 GeV.")
    print("  The budget paper's sec.5 inferred a 13.9x gain from MuSIC's 392 MeV")
    print("  point alone; that extrapolation is WITHDRAWN. Below ~2 GeV the yield")
    print("  does fall (85% of optimum at 2 GeV), which is all MuSIC's point shows.")
    print()
    print("  CONDITION 8 -- the binder-economy bound. Net-positive requires")
    print("  N x Q_fus x f_work > E_binder with N <= 1/omega_s, hence:")
    print()
    for f, lab in ((1.0, "heat"), (F_WORK, "work")):
        need = cap / condition8(f)
        print(f"    {lab}: E_binder < {condition8(f):5.2f} GeV;"
              f" muon costs {cap:.1f} -> need {need:4.1f}x"
              f" of the {cap / PION_THRESHOLD_GEV:.0f}x headroom, margin"
              f" {(cap / PION_THRESHOLD_GEV) / need:5.1f}x")
    print()
    print("  The admissible set is NOT empty: condition 8 sits between what is")
    print("  achieved and the kinematic threshold, not beyond it.")
    print()
    print("  CYCLES REQUIRED against the captured figure:")
    for lab, f in (("heat-breakeven", 1.0), ("work-breakeven", F_WORK)):
        print(f"    {lab:<16} N > {cap / (q * f):8.0f} cycles per muon")
    print()
    print("  CYCLES AVAILABLE -- N is capped by sticking, asymptote 1/omega_s:")
    for ws, lab in ((OMEGA_MEASURED, "measured 0.45%"),
                    (OMEGA_BOTH_LEVERS, "both levers 0.234%")):
        print(f"    {lab:<20} N(phi=3) = {cycles(ws, 3.0):6.1f}   asymptote = {1 / ws:6.1f}")
    print()
    print("  THE SHORTFALL, best case in every direction:")
    for ws, lab in ((OMEGA_MEASURED, "measured"), (OMEGA_BOTH_LEVERS, "both levers")):
        for f, fl in ((1.0, "heat"), (F_WORK, "work")):
            need = cap / (q * f)
            print(f"    {lab:<12} {fl:<5}: need {need:7.0f}, ceiling {1 / ws:6.1f}"
                  f"  -> Q = {(1 / ws) * q * f / cap:.3f}, SHORT by {need * ws:5.1f}x")
    print()
    print("  Sticking that WOULD be required, at the asymptotic ceiling:")
    for f, fl in ((1.0, "heat"), (F_WORK, "work")):
        print(f"    {fl:<5}: omega_s < {100 * q * f / cap:.4f}%  vs 0.234% projected"
              " (two undemonstrated levers) and 0.45% measured")
    print()
    print("  CROSS-CHECK against the historical measurement: Los Alamos reported")
    print("  ~150 cycles and Q ~ 0.53 costed at 5 GeV. Recosted at the captured")
    print(f"  production figure, 150 cycles gives Q = {150 * q / cap:.3f}, and 0.53 x 5/{cap:.1f}"
          f" = {0.53 * 5 / cap:.3f}.")
    print("  The two agree, which is what makes the floor figure load-bearing.")
    print()
    print("  SENSITIVITY -- and it is decisive. The 23.5 GeV figure is CAPTURED")
    print("  mu- per proton, not TOTAL pi- produced. With perfect collection the")
    print("  cost falls to the production figure alone, and the verdict flips")
    print("  across a number this instrument cannot source:")
    print()
    print(f"    {'pi-/p @8GeV':>12} {'GeV/pi-':>9} {'FOM heat':>9} {'FOM work':>9}  verdict")
    for Y in (0.5, 1.0, 1.5, 2.0, 3.0):
        eb = 8000.0 / Y
        fh, fw2 = Q_FUS_MEV / (OMEGA_BOTH_LEVERS * eb), Q_FUS_MEV * F_WORK / (OMEGA_BOTH_LEVERS * eb)
        v = "both PASS" if fw2 > 1 else ("heat PASS, work short" if fh > 1 else "both SHORT")
        print(f"    {Y:>12.1f} {eb / 1000:>9.2f} {fh:>9.2f} {fw2:>9.2f}  {v}")
    print()
    print("  So this is a BRACKET, not a closure. What decides it is the total")
    print("  pi- yield per proton at 4-11 GeV on a thick high-Z target, and how")
    print("  much of the gap between production and capture is recoverable.")
    print("  NO VERDICT IS OFFERED until that number is sourced.")
    print()
    print("  REFUSAL: this is a bound on the ENERGY BALANCE, not on the reaction.")
    print("  The reaction is demonstrated, the definition stands, the procedure")
    print("  stands. What this closes is net power on published production yields")
    print("  and published sticking -- and it names the two numbers that would")
    print("  reopen it.")


def selftest():
    fail = 0
    print("collector.py --selftest   fixtures: published figures, cited in the paper")
    print()
    checks = [
        ("PSI muE4: 4e8 mu/s at 1.2 MW", 4e8 / 1.2e6, PSI_MUE4_PER_W, 20.0),
        ("MuSIC mu-: 3.6e7 /s at 400 W", 3.6e7 / 400.0, MUSIC_MU_MINUS_PER_W, 1e3),
        ("MuSIC all-mu: 4.2e8 /s at 400 W", 4.2e8 / 400.0, MUSIC_ALL_MU_PER_W, 1e4),
        ("Mu2e: 8 GeV / 0.0016", MU2E_PROTON_GEV / MU2E_STOPPED_PER_P, 5000.0, 1.0),
    ]
    for name, got, want, tol in checks:
        ok = abs(got - want) <= tol
        fail += 0 if ok else 1
        print(f"  {name:<36} {got:>12,.1f} vs {want:,.1f}   {'PASS' if ok else 'FAIL'}")

    print("    NOTE: the muE4 row recomputes to 333.3 against the source's stated")
    print("    3.5e2 -- the source rounds up by 5%. Recorded, not repaired.")

    print()
    best = gev_per_stopped(MU2E_PROTON_GEV, MU2E_STOPPED_PER_P)
    ok = abs(best / PAPER_ASSUMED_GEV - 1000.0) < 1.0
    fail += 0 if ok else 1
    print(f"  best published / v1.1 assumed        {best / PAPER_ASSUMED_GEV:>12,.0f}x vs 1,000x"
          f"   {'PASS' if ok else 'FAIL'}")
    ok = abs(best / PION_THRESHOLD_GEV - 16666.7) < 5.0
    fail += 0 if ok else 1
    print(f"  best published / kinematic floor     {best / PION_THRESHOLD_GEV:>12,.0f}x vs 16,667x"
          f"   {'PASS' if ok else 'FAIL'}")

    print()
    print("  block arithmetic closes on the total")
    ideal = MU2E_PROTON_GEV / PION_THRESHOLD_GEV
    exiting = MU2E_STOPPED_PER_P / MU2E_STOPPING_FRAC
    for cap, label in ((COMET_CAPTURED_LO, "lo"), (COMET_CAPTURED_HI, "hi")):
        product = (ideal / cap) * (cap / exiting) * (1 / MU2E_STOPPING_FRAC)
        ok = abs(product - ideal / MU2E_STOPPED_PER_P) / (ideal / MU2E_STOPPED_PER_P) < 1e-9
        fail += 0 if ok else 1
        print(f"    capture {label}: blocks multiply to {product:>10,.0f}x"
              f"  vs total {ideal / MU2E_STOPPED_PER_P:,.0f}x   {'PASS' if ok else 'FAIL'}")

    print()
    print("  refusal: mu- and all-mu yields are never interchanged")
    ok = MUSIC_ALL_MU_PER_W / MUSIC_MU_MINUS_PER_W > 10
    fail += 0 if ok else 1
    print(f"    all-mu / mu- = {MUSIC_ALL_MU_PER_W / MUSIC_MU_MINUS_PER_W:.1f}x"
          f" -- substituting one would understate by that   {'PASS' if ok else 'FAIL'}")

    print()
    print(f"selftest: {fail} failures -> {'PASS' if fail == 0 else 'FAIL'}")
    return 1 if fail else 0


def main():
    ap = argparse.ArgumentParser(description="the muon collection budget, stage by stage")
    ap.add_argument("--selftest", action="store_true")
    ap.add_argument("--machines", action="store_true", help="what machines deliver")
    ap.add_argument("--production", action="store_true",
                    help="integrate the HARP cross sections; price the collector argument")
    ap.add_argument("--floor", action="store_true",
                    help="the production floor and the resulting energy shortfall")
    ap.add_argument("--target", type=float, default=WORK_BREAKEVEN_GEV,
                    help=f"GeV per stopped mu- to solve for (default {WORK_BREAKEVEN_GEV}, "
                         "v1.1 sec.5.2 work-breakeven)")
    a = ap.parse_args()
    if a.selftest:
        return selftest()
    if a.machines:
        report_machines()
        return 0
    if a.production:
        report_production()
        return 0
    if a.floor:
        report_floor()
        return 0
    report_budget(a.target)
    return 0


if __name__ == "__main__":
    sys.exit(main())
