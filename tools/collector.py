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


# ---- THE SPECIES: which pion, and therefore which target -------------------
# Only mu- catalyses. A mu+ binds an electron into muonium and is repelled by
# every nucleus, so it forms no mesomolecule at all; the catalytic cycle exists
# for one sign only. mu- comes only from pi- decay, so of everything a target
# produces only the pi- half is usable, and the yields above are pi- yields for
# that reason. What follows measures the half rather than assuming it.
#
# HARP Table 7 in full: p-Pb, pi+, 8 GeV/c, arXiv:0709.3458 Appendix A -- the
# same target, beam and binning as the pi- table above, so the two divide bin by
# bin. Units and layout are identical: barn/(GeV/c . rad).
HARP_PB_PIPLUS_8GEV = {
    (0.35, 0.55): _row([1.14, 1.86, 2.09, 1.99, 2.19, 2.21, 2.04],
                       [2.07, 1.73, 1.09], skip_first=True),
    (0.55, 0.75): _row([0.93, 1.81, 2.11, 2.26, 2.09, 2.09, 1.86, 1.63],
                       [1.30, 0.89, 0.56]),
    (0.75, 0.95): _row([1.21, 2.16, 2.27, 2.02, 1.85, 1.60, 1.39, 1.22],
                       [0.83, 0.46]),
    (0.95, 1.15): _row([1.47, 2.19, 1.97, 1.60, 1.31, 1.11, 0.88, 0.66], [0.46]),
    (1.15, 1.35): _row([1.82, 2.30, 1.86, 1.41, 0.94, 0.74, 0.55, 0.37], []),
    (1.35, 1.55): _row([1.84, 2.21, 1.57, 1.04, 0.74, 0.53, 0.38, 0.22], []),
    (1.55, 1.75): _row([1.54, 1.93, 1.34, 0.87, 0.53, 0.36, 0.25, 0.15], []),
    (1.75, 1.95): _row([1.31, 1.64, 1.02, 0.63, 0.34, 0.22, 0.14, 0.07], []),
    (1.95, 2.15): _row([1.14, 1.17, 0.75, 0.45, 0.20, 0.09, 0.06, 0.04], []),
}

# HARP FORWARD, p-Pb pi+, 8 GeV/c: arXiv:0907.3857 Table XXII (0.05-0.25 rad)
# plus the finest bin of Table XXXII (0.025-0.050 rad) -- the pi+ columns of the
# same two tables the pi- set above is read from. Same units, same Jacobian.
HARP_PB_PIPLUS_8GEV_FWD = {
    (0.025, 0.050): [((0.50, 0.75), 1.12), ((0.75, 1.00), 1.17), ((1.00, 1.25), 0.38),
                     ((1.25, 1.50), 0.62), ((1.50, 2.00), 1.13), ((2.00, 2.50), 0.54),
                     ((2.50, 3.00), 0.50), ((3.00, 3.50), 0.33), ((3.50, 4.00), 0.08),
                     ((4.00, 5.00), 0.05)],
    (0.050, 0.100): [((0.50, 1.00), 0.99), ((1.00, 1.50), 0.86), ((1.50, 2.00), 0.81),
                     ((2.00, 2.50), 0.66), ((2.50, 3.00), 0.41), ((3.00, 3.50), 0.16),
                     ((3.50, 4.00), 0.03), ((4.00, 5.00), 0.06), ((5.00, 6.50), 0.01)],
    (0.100, 0.150): [((0.50, 1.00), 1.18), ((1.00, 1.50), 0.77), ((1.50, 2.00), 0.80),
                     ((2.00, 2.50), 0.45), ((2.50, 3.00), 0.15), ((3.00, 3.50), 0.05),
                     ((3.50, 4.00), 0.031), ((4.00, 5.00), 0.011)],
    (0.150, 0.200): [((0.50, 1.00), 1.07), ((1.00, 1.50), 0.68), ((1.50, 2.00), 0.40),
                     ((2.00, 2.50), 0.24), ((2.50, 3.00), 0.08), ((3.00, 3.50), 0.040),
                     ((3.50, 4.00), 0.018), ((4.00, 5.00), 0.009), ((5.00, 6.50), 0.002)],
    (0.200, 0.250): [((0.50, 1.00), 0.54), ((1.00, 1.50), 0.41), ((1.50, 2.00), 0.22),
                     ((2.00, 2.50), 0.13), ((2.50, 3.00), 0.05), ((3.00, 3.50), 0.03),
                     ((3.50, 4.00), 0.020), ((4.00, 5.00), 0.01)],
}

# The low-A control. HARP Tables 5 and 6, p-Al, 8 GeV/c, large-angle only -- the
# same spectrometer and binning. Aluminium has N/Z = 1.077 against lead's 1.537,
# and the source states the effect this pair is here to measure: "In the lead
# data ... the number of pi+'s produced is smaller than the number of pi-'s in
# the lowest momentum bin ... Lower-A targets do not show this behaviour."
HARP_AL_PIPLUS_8GEV = {
    (0.35, 0.55): _row([0.321, 0.485, 0.517, 0.625, 0.645, 0.643, 0.675],
                       [0.626, 0.621, 0.492], skip_first=True),
    (0.55, 0.75): _row([0.229, 0.353, 0.553, 0.626, 0.601, 0.544, 0.491, 0.505],
                       [0.485, 0.336, 0.234]),
    (0.75, 0.95): _row([0.265, 0.464, 0.536, 0.521, 0.442, 0.411, 0.346, 0.307],
                       [0.256, 0.161]),
    (0.95, 1.15): _row([0.264, 0.489, 0.513, 0.396, 0.337, 0.293, 0.231, 0.184], [0.126]),
    (1.15, 1.35): _row([0.308, 0.422, 0.390, 0.337, 0.258, 0.186, 0.138, 0.097], []),
    (1.35, 1.55): _row([0.353, 0.416, 0.303, 0.215, 0.174, 0.119, 0.073, 0.045], []),
    (1.55, 1.75): _row([0.288, 0.331, 0.221, 0.159, 0.111, 0.070, 0.047, 0.027], []),
    (1.75, 1.95): _row([0.279, 0.329, 0.204, 0.125, 0.064, 0.035, 0.025, 0.013], []),
    (1.95, 2.15): _row([0.249, 0.255, 0.132, 0.066, 0.043, 0.022, 0.015, 0.006], []),
}
HARP_AL_PIMINUS_8GEV = {
    (0.35, 0.55): _row([0.356, 0.371, 0.455, 0.355, 0.383, 0.432, 0.422],
                       [0.367, 0.350, 0.333], skip_first=True),
    (0.55, 0.75): _row([0.232, 0.368, 0.424, 0.406, 0.355, 0.366, 0.341, 0.323],
                       [0.281, 0.250, 0.218]),
    (0.75, 0.95): _row([0.224, 0.356, 0.360, 0.348, 0.323, 0.293, 0.258, 0.233],
                       [0.203, 0.156]),
    (0.95, 1.15): _row([0.222, 0.326, 0.355, 0.288, 0.231, 0.189, 0.153, 0.139], [0.115]),
    (1.15, 1.35): _row([0.240, 0.338, 0.300, 0.253, 0.168, 0.128, 0.108, 0.091], []),
    (1.35, 1.55): _row([0.257, 0.279, 0.252, 0.187, 0.141, 0.111, 0.090, 0.066], []),
    (1.55, 1.75): _row([0.234, 0.257, 0.184, 0.150, 0.094, 0.052, 0.040, 0.033], []),
    (1.75, 1.95): _row([0.218, 0.234, 0.166, 0.113, 0.069, 0.048, 0.036, 0.026], []),
    (1.95, 2.15): _row([0.176, 0.178, 0.138, 0.061, 0.040, 0.039, 0.032, 0.017], []),
}
N_OVER_Z = {"Pb": 126.0 / 82.0, "Al": 14.0 / 13.0}
HARP_NORM_UNCERTAINTY_PB = 0.03    # the source's own, and not in its tables


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


# ---- the charge fraction, measured rather than assumed ---------------------
def _la_sigma(table, theta_min=HARP_THETA_MIN, window=None):
    """Integrated large-angle cross section over a table, barn."""
    tot = 0.0
    for (tlo, thi), bins in table.items():
        if tlo < theta_min:
            continue
        for (pl, ph), v in bins.items():
            if window and not (window[0] <= 0.5 * (pl + ph) <= window[1]):
                continue
            tot += v * (ph - pl) * (thi - tlo)
    return tot


def _fwd_sigma(table):
    """Integrated forward cross section over a table, barn, Jacobian applied."""
    tot = 0.0
    for (tlo, thi), bins in table.items():
        dom = 2 * math.pi * (math.cos(tlo) - math.cos(thi))
        tot += sum(v * (ph - pl) for (pl, ph), v in bins) * dom
    return tot


def charge_fraction_produced():
    """pi- as a fraction of all charged pions PRODUCED off lead at 8 GeV/c,
    integrated over everything HARP measured. Below one half: for a proton beam
    pi+ is the majority channel, because the beam carries two units of charge
    into the final state and the pion has to carry some of it back."""
    m = _la_sigma(HARP_PB_PIMINUS_8GEV) + _fwd_sigma(HARP_PB_PIMINUS_8GEV_FWD)
    p = _la_sigma(HARP_PB_PIPLUS_8GEV) + _fwd_sigma(HARP_PB_PIPLUS_8GEV_FWD)
    return m / (m + p)


def charge_ratio(minus, plus, theta_min=HARP_THETA_MIN, window=None):
    """pi-/pi+ over one large-angle pair of tables, optionally in one p window."""
    return (_la_sigma(minus, theta_min, window)
            / _la_sigma(plus, theta_min, window))


def charge_fraction_accepted(br=1.50, hemisphere="fwd", window=None):
    """pi- as a fraction of the charged pions a COLLECTOR accepts -- the same
    p_T cap, two-body decay and momentum requirement applied to each charge in
    turn. This, not the produced fraction, is what a captured-muon yield quoted
    for both charges has to be divided by."""
    sm = _la_sigma(HARP_PB_PIMINUS_8GEV) + _fwd_sigma(HARP_PB_PIMINUS_8GEV_FWD)
    sp = _la_sigma(HARP_PB_PIPLUS_8GEV) + _fwd_sigma(HARP_PB_PIPLUS_8GEV_FWD)
    m = delivered_fraction(br, hemisphere, window) * sm
    p = delivered_fraction(br, hemisphere, window,
                           la=HARP_PB_PIPLUS_8GEV, fwd=HARP_PB_PIPLUS_8GEV_FWD) * sp
    return m / (m + p)


# MEASURED, from the two tables above through the acceptance model of sec.5.24 at
# the built front end's own aperture and rf window. The captured-muon yield
# Y_P is quoted for both charges and has always been halved here; this is the
# number that halving assumes, and it comes out at 0.508 -- a 1.7 percent
# difference, inside HARP's own 3 percent normalisation uncertainty. The halving
# therefore stands, and stands MEASURED rather than assumed. It is not adopted as
# a correction: a 1.7 percent shift smaller than the uncertainty of the
# measurement that found it would be flattening a bound into a value.
CHARGE_FRACTION_ASSUMED = 0.5


def nf_captured_per_interacting_proton(ep_gev=8.0):
    """Captured mu- per interacting proton at a stated beam energy. The halving
    is the charge split, validated by charge_fraction_accepted() -- see there."""
    return YP_BOTH_CHARGES_PER_GEV * CHARGE_FRACTION_ASSUMED * ep_gev


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


# ---- pion -> muon: the decay step the p_T cap alone does not model ---------
# captured_fraction() above tests the PION against the solenoid's transverse cap.
# What a target receives is the MUON from that pion's decay, and pi -> mu nu is a
# two-body decay that redistributes momentum: the muon takes between (m_mu/m_pi)^2
# and 1 of the pion's energy and picks up a transverse kick of at most p*. Neither
# effect is in the p_T cap. This models both, deterministically -- the decay is
# isotropic in the pion rest frame (the pion is spin 0), so the rest-frame solid
# angle is integrated on a fixed grid rather than sampled.
M_PI_MEV = 139.570
M_MU_MEV = 105.658
P_STAR_MEV = (M_PI_MEV ** 2 - M_MU_MEV ** 2) / (2 * M_PI_MEV)   # 29.79 MeV/c
E_STAR_MEV = (M_PI_MEV ** 2 + M_MU_MEV ** 2) / (2 * M_PI_MEV)   # 109.78 MeV

# SOURCED, Strait et al. PRSTAB 13 111001 sec.II. The NF/MC front end captures the
# FORWARD hemisphere -- "to efficiently capture pions exiting the target in the
# forward hemisphere" -- and its acceptance is dominated NOT by the solenoid but by
# the rf-capture window it must deliver into: "The drop in acceptance at high
# momenta comes primarily from the requirement that T < 180 MeV (265 MeV/c), and
# secondarily from the transverse momentum p_T < 225 MeV/c". That window is a
# collider requirement. A stopping target has a different one.
NF_RF_WINDOW_MEV = (100.0, 265.0)    # 40 < T_mu < 180 MeV
NF_PT_CAP_MEV = 225.0                # 20 T on a 7.5 cm radius
NF_CHANNEL_M = 50.0


def _production_bins(la=None, fwd=None):
    """(p_pi GeV/c, theta rad, weight) over both HARP tables, with the forward
    set's solid-angle Jacobian applied exactly as captured_fraction() applies it.
    Defaults to the pi- tables, which are the ones every balance uses; the pi+
    tables are passed in only to measure the charge fraction against them."""
    for (tlo, thi), b in (HARP_PB_PIMINUS_8GEV if la is None else la).items():
        th, dth = 0.5 * (tlo + thi), thi - tlo
        for (pl, ph), v in b.items():
            yield 0.5 * (pl + ph), th, v * (ph - pl) * dth
    for (tlo, thi), b in (HARP_PB_PIMINUS_8GEV_FWD if fwd is None else fwd).items():
        th = 0.5 * (tlo + thi)
        dom = 2 * math.pi * (math.cos(tlo) - math.cos(thi))
        for (pl, ph), v in b:
            yield 0.5 * (pl + ph), th, v * (ph - pl) * dom


def muon_spectrum(br, hemisphere="both", ncos=160, nphi=96, la=None, fwd=None):
    """Momentum spectrum of the muons a solenoid of aperture `br` delivers, as
    (p_mu MeV/c, weight) pairs, with the total production weight for normalising.
    A pion outside the transverse cap is lost before it decays -- its decay length
    is metres and the absorber is centimetres away -- so only captured pions
    contribute, and each contributes the fraction of its decay sphere that leaves
    the muon inside the same cap."""
    ptm = pt_max(br) * 1000.0
    out, total = [], 0.0
    for p_gev, th, w in _production_bins(la, fwd):
        total += w
        if hemisphere == "fwd" and th > math.pi / 2:
            continue
        if hemisphere == "back" and th <= math.pi / 2:
            continue
        if p_gev * math.sin(th) >= ptm / 1000.0:
            continue
        p = p_gev * 1000.0
        beta = p / math.hypot(p, M_PI_MEV)
        gam = math.hypot(p, M_PI_MEV) / M_PI_MEV
        st, ct = math.sin(th), math.cos(th)
        for i in range(ncos):
            cs = -1.0 + (2.0 * i + 1.0) / ncos
            ss = math.sqrt(max(0.0, 1.0 - cs * cs))
            ppar = gam * (P_STAR_MEV * cs + beta * E_STAR_MEV)
            pperp = P_STAR_MEV * ss
            for j in range(nphi):
                phi = 2 * math.pi * (j + 0.5) / nphi
                cf = math.cos(phi)
                px = ppar * st + pperp * cf * ct
                py = pperp * math.sin(phi)
                pz = ppar * ct - pperp * cf * st
                if math.hypot(px, py) >= ptm:
                    continue
                out.append((math.sqrt(px * px + py * py + pz * pz), w / (ncos * nphi)))
    return out, total


def delivered_fraction(br, hemisphere="both", window=None, ncos=160, nphi=96,
                       la=None, fwd=None):
    """Captured mu- per pi- PRODUCED. `window` is a (p_lo, p_hi) MeV/c momentum
    requirement -- the rf bucket for a collider, the stopping range for a target.
    None applies no momentum requirement at all and is therefore an upper bound."""
    spec, total = muon_spectrum(br, hemisphere, ncos, nphi, la, fwd)
    if window is None:
        kept = sum(w for _, w in spec)
    else:
        lo, hi = window
        kept = sum(w for pm, w in spec if lo <= pm <= hi)
    return kept / total


def decay_survival(br, hemisphere="both"):
    """Captured muons per captured PION -- the decay step alone, with no momentum
    requirement. Near unity, which is the finding: the decay kick is small against
    the cap, so the pion acceptance is a good proxy for the muon acceptance."""
    pi_cap = captured_fraction(br, hemisphere != "back") if hemisphere != "fwd" else None
    if hemisphere == "fwd":
        ptm = pt_max(br)
        tot = cap = 0.0
        for p, th, w in _production_bins():
            tot += w
            if th <= math.pi / 2 and p * math.sin(th) < ptm:
                cap += w
        pi_cap = cap / tot
    elif hemisphere == "back":
        pi_cap = captured_fraction(br, False)
    return delivered_fraction(br, hemisphere) / pi_cap


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

# SOURCED, Kelly, Hart & Rose, J. Phys. Energy 3 035003 (2021): a G4Beamline
# optimisation of the production target itself. Their best configuration is a
# 3.61 GeV deuteron beam on a tungsten rod 652 mm long and 5.1 mm across,
# giving 0.77 pi- per BEAM PARTICLE -- not per interacting particle. That is
# the difference from this paper's own figure: HARP measured a 5 percent
# interaction-length target, where the beam's remaining energy leaves with it,
# and sec.5.1 labelled its yield a lower bound for exactly this reason. A long
# target lets the primary and its secondaries interact repeatedly.
# They assume every pi- becomes a usable mu-, so their cost is a
# perfect-collection figure, comparable like-for-like with cost_per_pion_produced().
KELLY_BEAM_GEV = 3.61
KELLY_PIMINUS_PER_BEAM = 0.77
KELLY_TARGET_LEN_MM = 652.0
KELLY_TARGET_DIA_MM = 5.1
KELLY_HEAT_GEV_150 = 3.9     # their heat per muon at 150 fusions
KELLY_Q_LO = 0.65
KELLY_Q_HI = 0.78


def kelly_cost_per_pion():
    """Beam kinetic energy per pi- produced in an optimised thick target."""
    return KELLY_BEAM_GEV / KELLY_PIMINUS_PER_BEAM


# SOURCED, Yin, Kou & Chen, arXiv:2605.26432 -- an independent review that
# arrives at the same fission-breeding escape this paper reaches in sec.5.18,
# and states the same service-life law at phi = 1. Their Table I parameters,
# kept here so their numbers can be recomputed rather than quoted.
YIN_E_MU_GEV = 5.0          # their assumed cost per mu-, said to include collection
YIN_LAMBDA_MU = 4.55e5      # their muon decay rate
YIN_Q_FUS_MEV = 17.6        # their fusion yield
YIN_TABLE = {               # column: (omega_s, lambda_c, X_mu stated, Q stated)
    "unpolarised":     (0.0045,  2.0e8, 148, 0.52),
    "pol-conservative": (0.00342, 2.6e8, 193, 0.68),
    "pol-optimistic":  (0.00315, 3.0e8, 292, 1.03),
    "ultimate":        (0.0006,  5.5e8, 873, 3.07),
}
YIN_LAMBDA_MU_ULTIMATE = 3.0e5   # the last column assumes lifetime control


def yin_cycles(col):
    """Their own equation, on their own printed parameters."""
    ws, lc, _, _ = YIN_TABLE[col]
    lm = YIN_LAMBDA_MU_ULTIMATE if col == "ultimate" else YIN_LAMBDA_MU
    return 1.0 / (lm / lc + ws)


def yin_q(col):
    return yin_cycles(col) * YIN_Q_FUS_MEV / (YIN_E_MU_GEV * 1000.0)


def yin_sticking_for_stated(col):
    """The sticking their stated X_mu implies at their stated cycle rate."""
    ws, lc, X, _ = YIN_TABLE[col]
    lm = YIN_LAMBDA_MU_ULTIMATE if col == "ultimate" else YIN_LAMBDA_MU
    return 1.0 / X - lm / lc


# SOURCED, MuFusE collaboration arXiv:2606.19304: a diamond-anvil-cell muCF
# target running on the PSI muon beam, DD and DT campaigns in 2024 and 2025.
# The best apparatus in the field for reaching density and temperature at once.
DAC_PRESSURE_MPA = 933.0     # achieved, stable sample volume
DAC_TEMP_K = 400.0           # achieved
DAC_TEMP_CEILING_K = 500.0   # design ceiling
DAC_SAMPLE_MM3 = 19.2


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
    return 1.0 / (YP_BOTH_CHARGES_PER_GEV * CHARGE_FRACTION_ASSUMED)


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


# ---- the stopping window: what a target can actually bring to rest ---------
# sec.5.24 shows the delivered fraction turns on the momentum window the target
# imposes. That window is not free: a muon must be brought to rest inside the
# fuel, so the target must be one CSDA range thick, and that areal density is
# tritium. Bethe stopping power, integrated. Validated two ways below.
BETHE_K = 0.307075        # MeV mol^-1 cm^2
M_E_MEV = 0.510999
H_Z_OVER_A = 0.99212      # hydrogen
H_I_EV = 21.8             # mean excitation energy, liquid hydrogen
T_HALFLIFE_S = 12.32 * 3.156e7
T_MASS_FRAC_DT = 3.0 / 5.0     # 50/50 D/T by number
A_DT_AMU = 2.5
AMU_G = 1.6605e-24


def bethe_dedx(T_mev, M_mev=M_MU_MEV, z_over_a=H_Z_OVER_A, i_ev=H_I_EV):
    """Mass stopping power in MeV cm^2/g. The density-effect correction is
    omitted, which overstates dE/dx above a few hundred MeV and therefore
    understates the range -- an optimistic direction for a stopping target, and
    stated as such rather than corrected."""
    E = T_mev + M_mev
    gam = E / M_mev
    beta = math.sqrt(max(1e-12, 1.0 - 1.0 / (gam * gam)))
    bg = beta * gam
    t_max = 2 * M_E_MEV * bg * bg / (1 + 2 * gam * M_E_MEV / M_mev + (M_E_MEV / M_mev) ** 2)
    i_mev = i_ev * 1e-6
    lterm = 0.5 * math.log(2 * M_E_MEV * bg * bg * t_max / (i_mev * i_mev)) - beta * beta
    return BETHE_K * z_over_a * lterm / (beta * beta)


def p_to_kinetic(p_mev, M_mev=M_MU_MEV):
    return math.hypot(p_mev, M_mev) - M_mev


def csda_range(p_mev, t_min=0.5, n=4000):
    """Muon CSDA range in hydrogen, g/cm^2, for a muon of momentum p_mev."""
    T = p_to_kinetic(p_mev)
    if T <= t_min:
        return 0.0
    h = (T - t_min) / n
    return sum(h / bethe_dedx(t_min + h * (i + 0.5)) for i in range(n))


def dt_density(phi):
    """g/cm^3 of a 50/50 D-T mixture at phi times liquid-hydrogen number density."""
    return LHD_ATOMS_PER_CM3 * phi * A_DT_AMU * AMU_G


def target_length_cm(p_mev, phi):
    return csda_range(p_mev) / dt_density(phi)


def tritium_curies(mass_g):
    lam = math.log(2) / T_HALFLIFE_S
    return lam * (mass_g / 3.016) * 6.022e23 / 3.7e10


def tritium_inventory_kg(p_mev, beam_radius_cm):
    """Tritium in a target one CSDA range deep over a beam of the stated radius.
    NOTE it does not depend on phi: the inventory is areal density times area,
    and the areal density is fixed by the range. Density buys length, not mass."""
    areal = csda_range(p_mev)                     # g/cm^2
    return areal * math.pi * beam_radius_cm ** 2 * T_MASS_FRAC_DT / 1000.0


# SOURCED, Strait et al. PRSTAB 13 111001 Table II. Y_P is captured muons, BOTH
# charges, per INTERACTING proton per GeV -- the same normalisation throughout, so
# the thin/thick ratio R_t isolates hadronic showering in the target and nothing
# else. (The published 2.2 GeV thick entry reads "0.50"; it is 0.050, which its own
# stated R_t of 0.874 confirms.)
#   T_beam GeV: (Y_P at 0.05 lambda_I, Y_P at 2 lambda_I, R_t)
STRAIT_TABLE_II = {
    2.2: (0.057, 0.050, 0.874),
    4.1: (0.056, 0.054, 0.963),
    7.1: (0.053, 0.057, 1.079),
    11.1: (0.042, 0.050, 1.186),
}


def strait_pions_per_interacting_proton(t_beam=4.1):
    """Invert a published captured-muon yield through the validated acceptance
    model to recover the PION production that must have fed it. Independent of
    this paper's own HARP integration -- it shares the cross sections but not the
    integration, the acceptance convolution, or the normalisation."""
    y_p = STRAIT_TABLE_II[t_beam][1]
    mu_minus_per_interacting = y_p * t_beam / 2.0
    return mu_minus_per_interacting / delivered_fraction(1.50, "fwd", NF_RF_WINDOW_MEV)


def strait_cost_per_pion(t_beam=4.1):
    return t_beam / strait_pions_per_interacting_proton(t_beam)


def thickness_amplification(t_beam=4.1):
    """What two interaction lengths buy over 0.05, per interacting proton."""
    return STRAIT_TABLE_II[t_beam][2]


# ---- what the two HARP tables do NOT cover ---------------------------------
HARP_GAP_RAD = (0.25, 0.35)      # between the forward and large-angle sets
HARP_BACKWARD_EDGE_RAD = 2.15    # the large-angle table stops here


def _solid_angle(a, b):
    return 2 * math.pi * (math.cos(a) - math.cos(b))


def _dsigma_domega_la(bin_key):
    lo, hi = bin_key
    sig = sum(v * (ph - pl) * (hi - lo)
              for (pl, ph), v in HARP_PB_PIMINUS_8GEV[bin_key].items())
    return sig / _solid_angle(lo, hi)


def _dsigma_domega_fwd(bin_key):
    return sum(v * (ph - pl) for (pl, ph), v in HARP_PB_PIMINUS_8GEV_FWD[bin_key])


def harp_gap_bracket():
    """The uncovered wedge between the two tables, bracketed by its neighbours.
    Returns (low, high) additional pi- per interacting proton. The two neighbours
    integrate different momentum ranges, so this is a bracket and not an estimate."""
    lo = _dsigma_domega_la((0.35, 0.55))
    hi = _dsigma_domega_fwd((0.2, 0.25))
    lo, hi = min(lo, hi), max(lo, hi)
    dom = _solid_angle(*HARP_GAP_RAD)
    return lo * dom / SIGMA_INEL_PB, hi * dom / SIGMA_INEL_PB


def harp_backward_ceiling():
    """An OVER-estimate of the uncovered backward cone: the last measured bin's
    differential yield held flat to 180 degrees, which it certainly is not."""
    d = _dsigma_domega_la((1.95, 2.15))
    return d * _solid_angle(HARP_BACKWARD_EDGE_RAD, math.pi) / SIGMA_INEL_PB


def coverage_corrected_cost(which="low"):
    """Cost per pi- with the gap bracket applied. RECONSTRUCTED, not measured."""
    lo, hi = harp_gap_bracket()
    return 8.0 / (harp_combined_yield() + (lo if which == "low" else hi))


def gyroradius_cm(pt_gev, b_tesla):
    return 100.0 * pt_gev / (0.3 * b_tesla)


def beam_envelope_cm(br, b_target=20.0, b_capture=20.0):
    """Radius the delivered beam fills at a target sitting in b_target, for a
    capture solenoid of aperture product `br` running at b_capture.

    A particle born on the axis with transverse momentum p_T spirals on a circle
    of radius r_g whose centre is r_g off-axis, so it reaches 2 r_g -- which is
    why a solenoid's clear radius equals twice the gyroradius at its own cap.
    Transport is adiabatic, conserving p_T^2 / B.

    This reproduces three stated geometries from the field and the cap alone:
    7.5 cm at 20 T and 1.50 T.m, 30 cm after the taper to 1.25 T, and the 13 cm
    of the sec.5.9 specification at 2.60 T.m."""
    pt = pt_max(br) * math.sqrt(b_target / b_capture)
    return 2.0 * gyroradius_cm(pt, b_target)


def tritium_inventory_derived_kg(p_mev, br, b_target=20.0):
    """The inventory with the beam radius derived rather than assumed."""
    return tritium_inventory_kg(p_mev, beam_envelope_cm(br, b_target))


def report_stopping():
    print("THE STOPPING WINDOW, and what it costs")
    print("  A delivered muon is useless unless it stops in the fuel, so the target")
    print("  must be one CSDA range thick. Bethe stopping power, integrated.")
    print()
    print("  VALIDATION 1 -- minimum-ionising dE/dx against PDG")
    for lab, za, i_ev, pdg in (("liquid H2", H_Z_OVER_A, H_I_EV, 4.034),
                               ("copper", 0.45636, 322.0, 1.403)):
        best = min(bethe_dedx(T, M_MU_MEV, za, i_ev) for T in [x * 0.5 for x in range(2, 4000)])
        print(f"    {lab:10s} {best:6.3f} vs PDG {pdg:5.3f} MeV cm2/g"
              f"   {'PASS' if abs(best / pdg - 1) < 0.05 else 'FAIL'}")
    print()
    print("  VALIDATION 2 -- tritium inventory against a running experiment")
    ci = tritium_curies(0.004 * T_MASS_FRAC_DT)
    print(f"    MuFusE state ~24 Ci for a 4 mg 50/50 fill; model gives {ci:.1f} Ci"
          f"   {'PASS' if abs(ci / 24.0 - 1) < 0.10 else 'FAIL'}")
    print()
    print("  THE COST OF A WINDOW  (target radius 5 cm)")
    print(f"    {'p_max':>6s} {'range':>12s} {'L at 1':>9s} {'L at 3':>9s} {'L at 8.5':>9s}"
          f" {'tritium':>10s}")
    for p in (150, 200, 265, 400):
        r = csda_range(p)
        print(f"    {p:5.0f} {r:8.1f} g/cm2 "
              f"{target_length_cm(p, 1.0):7.0f}cm {target_length_cm(p, 3.0):7.0f}cm "
              f"{target_length_cm(p, 8.5):7.0f}cm {tritium_inventory_kg(p, 5.0):8.2f} kg")
    print()
    print("  THE INVENTORY DOES NOT DEPEND ON DENSITY. It is areal density times")
    print("  beam area, and the areal density is set by the range. Compressing the")
    print("  fuel shortens the target and does not reduce its tritium by a gram.")
    print()
    print("  THE BEAM RADIUS IS NOT A FREE PARAMETER EITHER")
    print("  A particle born on axis with transverse momentum p_T reaches twice its")
    print("  gyroradius, so a solenoid's clear radius IS twice the gyroradius at its")
    print("  own cap. That reproduces three stated geometries:")
    for br, b, stated, what in ((1.50, 20.0, 7.5, "the capture solenoid's clear radius"),
                                (1.50, 1.25, 30.0, "the absorber after the taper"),
                                (2.60, 20.0, 13.0, "the sec.5.9 specification")):
        got = beam_envelope_cm(br, b)
        print(f"    {br:.2f} T.m at {b:5.2f} T -> {got:5.2f} cm   stated {stated:5.1f}"
              f"   {'PASS' if abs(got - stated) < 0.1 else 'FAIL'}   {what}")
    print()
    print("  SO THE BORE BUYS ACCEPTANCE AND PAYS IN TRITIUM, and the two are")
    print("  coupled through the same p_T cap:")
    print(f"    {'aperture':>9s} {'radius':>8s} {'trit@265':>10s} {'trit@400':>10s}")
    for br in (1.50, 2.60):
        r = beam_envelope_cm(br)
        print(f"    {br:6.2f} T.m {r:6.1f} cm {tritium_inventory_derived_kg(265, br):7.2f} kg"
              f" {tritium_inventory_derived_kg(400, br):8.2f} kg")
    print()
    print("  REFUSAL: this assumes the stopping target sits in the capture field and")
    print("  that transport is adiabatic and lossless. A real channel is neither, and")
    print("  a target in a weaker field is larger by sqrt(B_capture / B_target).")
    return 0


def report_acceptance():
    """What a solenoid actually delivers, decomposed. The p_T cap is only one of
    three cuts, and it is not the dominant one in the machine that has been built."""
    mars = 100.0 * nf_captured_per_interacting_proton() / harp_combined_yield()
    print("ACCEPTANCE, pi- produced -> mu- delivered")
    print("  the model: HARP production, solenoid p_T cap, two-body decay integrated")
    print("  over the pion rest frame, then a momentum requirement on the muon.")
    print()
    print("  VALIDATION against the full MARS15 front-end simulation")
    got = 100.0 * delivered_fraction(1.50, "fwd", NF_RF_WINDOW_MEV)
    print(f"    forward hemisphere, 1.50 T.m, rf window {NF_RF_WINDOW_MEV[0]:.0f}-"
          f"{NF_RF_WINDOW_MEV[1]:.0f} MeV/c")
    print(f"      model {got:5.2f}%   MARS15 {mars:5.2f}%   "
          f"ratio {got / mars:.3f}   {'PASS' if abs(got / mars - 1) < 0.05 else 'FAIL'}")
    print()
    print("  DECOMPOSITION at the existing 1.50 T.m aperture")
    fwd = 100.0 * delivered_fraction(1.50, "fwd")
    both = 100.0 * delivered_fraction(1.50, "both")
    print(f"    forward hemisphere, no momentum requirement   {fwd:6.2f}%")
    print(f"    both hemispheres,   no momentum requirement   {both:6.2f}%")
    print(f"    the rf window costs                           {fwd / got:6.2f}x")
    print(f"    the backward hemisphere adds                  {both / fwd:6.2f}x")
    print(f"    decay survival, captured mu- per captured pi- {decay_survival(1.50):6.4f}")
    print()
    print("  A STOPPING TARGET HAS ITS OWN WINDOW, and the model states the")
    print("  sensitivity rather than choosing one:")
    print(f"    {'aperture':>9s} {'hemi':>5s} " +
          " ".join(f"{'p<' + str(c):>8s}" for c in (200, 265, 400, 500)) + f"{'no cut':>9s}")
    for br, lab in ((1.50, "1.50 T.m"), (2.60, "2.60 T.m")):
        for hemi in ("fwd", "both"):
            row = [f"{100 * delivered_fraction(br, hemi, (0.0, c)):7.2f}%"
                   for c in (200, 265, 400, 500)]
            row.append(f"{100 * delivered_fraction(br, hemi):8.2f}%")
            print(f"    {lab:>9s} {hemi:>5s} " + " ".join(row))
    print()
    print("  REFUSAL: this is an acceptance and a decay, not a front end. Transport,")
    print("  cooling and stopping are not modelled, so every figure is an upper bound")
    print("  on what a machine delivers -- which is why the MARS15 row, the one that")
    print("  includes 50 m of transport, is the validation and not the prediction.")
    return 0


# ---- in-situ capture: the co-product configuration, priced as an experiment --
# The one configuration this corpus finds net-positive does not buy its binder:
# the pions are a byproduct of a spallation target that is already running, so
# the marginal beam energy per binder is zero. That argument was stated as an
# accounting and never as an apparatus. What follows is the apparatus, and it
# carries a correction to the accounting: a stopping target one muon range deep
# stops only the part of the accepted spectrum below its range, and the missing
# part is not recoverable by a better collector.
J_PER_GEV_EXACT = 1.602176634e-10
CELL_P_STOP_MEV = 111.5      # a 5 g/cm^2 cell -- see areal_for_p()
MUFUSE_TRITIUM_MG = 2.4      # the inventory MuFusE already holds and has licensed


def areal_for_p(p_mev):
    """Areal density a cell needs to stop a muon of this momentum, g/cm^2."""
    return csda_range(p_mev)


def p_for_areal(areal, lo=1.0, hi=2000.0):
    """The inverse: the highest momentum a cell of this areal density stops."""
    for _ in range(200):
        m = 0.5 * (lo + hi)
        if csda_range(m) < areal:
            lo = m
        else:
            hi = m
    return lo


def stopping_capture(p_stop_mev, br=1.50):
    """Captured mu- per pi- PRODUCED that also STOP in a target one range deep.
    This is the ceiling on the 'capture efficiency' any in-situ accounting may
    assume: a muon the solenoid accepts but the fuel does not stop is not a
    binder. It saturates at the solenoid's own acceptance and no target depth
    exceeds that."""
    return delivered_fraction(br, "fwd", (0.0, p_stop_mev))


def protons_per_s(power_mw, ep_gev):
    return power_mw * 1e6 / (ep_gev * J_PER_GEV_EXACT)


def insitu_stopped_per_s(power_mw=1.0, ep_gev=8.0, p_stop_mev=CELL_P_STOP_MEV,
                         cell_r_cm=0.016, beam_r_cm=7.5):
    """Binders per second stopping in a cell of the stated radius standing in a
    captured-muon beam of the stated radius. The cell intercepts (r/R)^2 of the
    beam -- which is the whole reason a bench-scale cell is affordable, and the
    whole reason it demonstrates a rate rather than a power."""
    n = protons_per_s(power_mw, ep_gev) * harp_combined_yield()
    return n * stopping_capture(p_stop_mev) * (cell_r_cm / beam_r_cm) ** 2


def cell_tritium_mg(p_stop_mev=CELL_P_STOP_MEV, cell_r_cm=0.016):
    return (areal_for_p(p_stop_mev) * math.pi * cell_r_cm ** 2
            * T_MASS_FRAC_DT * 1000.0)


def insitu_neutrons_per_s(cycles=150.0, **kw):
    return insitu_stopped_per_s(**kw) * cycles


def insitu_heat_fraction(capture, cycles=150.0, ep_gev=8.0):
    """Fusion heat as a fraction of beam energy, at a stated capture efficiency
    -- the accounting of the specification's own table."""
    return capture * harp_combined_yield() * cycles * MEV_PER_FUSION_HEAT / (ep_gev * 1000.0)


MEV_PER_FUSION_HEAT = 26.06   # alpha + blanket at the hot point, sec.5.8


def report_insitu():
    print("IN-SITU CAPTURE -- the co-product configuration as an apparatus")
    print()
    print("  The pions are already being made. The question this report answers is")
    print("  what a cell placed in the captured beam actually stops, and what it")
    print("  would count.")
    print()
    print("  THE CEILING THE ACCOUNTING DID NOT CARRY.")
    print("  A stopping target is one muon range deep, so it stops only the part of")
    print("  the accepted spectrum below that range. Capture efficiency is bounded")
    print("  by this and by nothing a collector can change:")
    print()
    print("    window        areal density   captured AND stopped   tritium over a")
    print("    MeV/c            g/cm2          per pi- produced      7.5 cm beam")
    for p in (150.0, 200.0, 265.0, 400.0, 700.0, 2000.0):
        a = areal_for_p(p)
        print(f"    0-{p:<8.0f}    {a:10.2f}        {stopping_capture(p):.4f}"
              f"            {tritium_inventory_kg(p, 7.5):8.2f} kg")
    print(f"    no window          --            {delivered_fraction(1.50, 'fwd'):.4f}"
          "                  --")
    print()
    print("    -> the ceiling is the solenoid's own acceptance, 0.507, approached")
    print("       only through tens of kilogrammes of tritium. At the 3.59 kg the")
    print("       specification already carries, the ceiling is 0.342. A capture")
    print("       efficiency of 0.90 is not reachable by any target depth.")
    print()
    print("    heat as a fraction of beam energy, at the reachable capture:")
    for c in (0.30, stopping_capture(265.0), 0.50, 0.90):
        tag = "  <-- the 3.59 kg ceiling" if abs(c - stopping_capture(265.0)) < 1e-9 else ""
        note = "  UNREACHABLE" if c > delivered_fraction(1.50, "fwd") else ""
        print(f"      capture {c:.3f}   heat {100 * insitu_heat_fraction(c):5.2f} %{tag}{note}")
    print()
    print("  THE DEMONSTRATION, AND WHAT IT COSTS IN TRITIUM.")
    print("  A cell intercepts (r_cell / r_beam)^2 of the beam, and its tritium goes")
    print("  as r^2 as well -- so rate and inventory fall together and the ratio of")
    print("  the two is fixed. That is what makes a bench cell affordable.")
    print()
    print(f"  1 MW at 8 GeV, thick target, a cell stopping to"
          f" {CELL_P_STOP_MEV:.1f} MeV/c"
          f" ({areal_for_p(CELL_P_STOP_MEV):.2f} g/cm2):")
    print()
    print("    cell radius   tritium            binders/s      14.1 MeV n/s     heat")
    for r in (0.016, 0.05, 0.10, 0.30):
        mg = cell_tritium_mg(cell_r_cm=r)
        st = insitu_stopped_per_s(cell_r_cm=r)
        n = insitu_neutrons_per_s(cell_r_cm=r)
        w = n * 17.59 * 1.602176634e-13
        print(f"    {10 * r:5.2f} mm     {mg:8.2f} mg ({tritium_curies(mg / 1000.0):7.1f} Ci)"
              f"  {st:.3e}    {n:.3e}    {w:.3e} W")
    print()
    print(f"    The first row is {MUFUSE_TRITIUM_MG} mg -- the inventory MuFusE already")
    print("    holds, licenses and has commissioned a delivery system for. At that")
    print(f"    inventory the committed prediction is {insitu_neutrons_per_s():.2e}")
    print("    neutrons per second at 14.1 MeV. It is a RATE demonstration and not a")
    print("    power one: the cell intercepts"
          f" {(0.016 / 7.5) ** 2:.2e} of the beam and returns"
          f" {insitu_neutrons_per_s() * 17.59 * 1.602176634e-13 * 1000:.0f} mW.")
    print()
    print("  WHAT IT DEPENDS ON, STATED RATHER THAN BURIED.")
    print("    The acceptance is sec.5.24's model, validated against MARS15 to 0.982")
    print("    and never measured end to end. Stage A of the programme measures it,")
    print("    and this prediction scales linearly with what Stage A returns.")
    print("    The cycle count is the witnessed 150 and the sticking cap allows 198.")
    return 0


# ---- HARP at four beam momenta: is beam energy the lever? ------------------
# The same lead target, the same spectrometers, the same binning, at 3, 5, 8 and
# 12 GeV/c. Table 8 (large angle) and Table XXIII (forward, 0.05-0.25 rad; its
# 0.025-0.050 row exists only at 8 and 12 and is therefore excluded here, so the
# four energies are compared over IDENTICAL coverage). Values are the pi- column
# at each beam momentum, in the units of the table they come from.
HARP_BEAM_MOMENTA = (3.0, 5.0, 8.0, 12.0)
HARP_PB_PIMINUS_BY_E = {
    (0.35, 0.55): {(0.15, 0.20): (0.17, 0.58, 1.59, 1.92), (0.20, 0.25): (0.33, 0.89, 2.00, 2.66),
                   (0.25, 0.30): (0.25, 0.98, 2.07, 2.54), (0.30, 0.35): (0.49, 0.96, 1.99, 2.30),
                   (0.35, 0.40): (0.37, 0.88, 1.63, 2.09), (0.40, 0.45): (0.30, 0.92, 1.63, 2.04),
                   (0.45, 0.50): (0.31, 0.79, 1.48, 1.89), (0.50, 0.60): (0.34, 0.78, 1.38, 1.50),
                   (0.60, 0.70): (0.21, 0.64, 1.37, 1.32), (0.70, 0.80): (0.11, 0.45, 1.06, 1.46)},
    (0.55, 0.75): {(0.10, 0.15): (0.34, 1.03, 1.24, 1.70), (0.15, 0.20): (0.40, 1.30, 2.09, 2.30),
                   (0.20, 0.25): (0.43, 1.21, 2.18, 2.45), (0.25, 0.30): (0.54, 1.29, 2.19, 2.20),
                   (0.30, 0.35): (0.53, 1.01, 1.88, 2.29), (0.35, 0.40): (0.40, 0.93, 1.51, 1.91),
                   (0.40, 0.45): (0.31, 0.89, 1.38, 1.79), (0.45, 0.50): (0.37, 0.70, 1.26, 1.59),
                   (0.50, 0.60): (0.27, 0.62, 1.20, 1.35), (0.60, 0.70): (0.16, 0.55, 0.95, 1.19),
                   (0.70, 0.80): (0.09, 0.41, 0.70, 0.95)},
    (0.75, 0.95): {(0.10, 0.15): (0.52, 1.12, 1.71, 1.95), (0.15, 0.20): (0.73, 1.47, 2.28, 2.74),
                   (0.20, 0.25): (0.61, 1.17, 2.04, 2.78), (0.25, 0.30): (0.60, 1.04, 1.88, 2.25),
                   (0.30, 0.35): (0.45, 0.94, 1.54, 2.29), (0.35, 0.40): (0.29, 0.76, 1.26, 1.67),
                   (0.40, 0.45): (0.19, 0.53, 1.11, 1.43), (0.45, 0.50): (0.18, 0.44, 0.95, 1.25),
                   (0.50, 0.60): (0.19, 0.45, 0.78, 0.99), (0.60, 0.70): (0.10, 0.36, 0.61, 0.67)},
    (0.95, 1.15): {(0.10, 0.15): (0.44, 1.28, 2.17, 2.58), (0.15, 0.20): (0.77, 1.53, 2.30, 2.93),
                   (0.20, 0.25): (0.47, 1.13, 1.85, 2.59), (0.25, 0.30): (0.40, 0.99, 1.50, 2.19),
                   (0.30, 0.35): (0.39, 0.85, 1.15, 1.77), (0.35, 0.40): (0.30, 0.61, 0.99, 1.44),
                   (0.40, 0.45): (0.28, 0.42, 0.80, 1.11), (0.45, 0.50): (0.18, 0.34, 0.69, 0.82),
                   (0.50, 0.60): (0.08, 0.26, 0.52, 0.65)},
    (1.15, 1.35): {(0.10, 0.15): (0.43, 1.45, 2.40, 3.22), (0.15, 0.20): (0.65, 1.56, 2.19, 3.14),
                   (0.20, 0.25): (0.37, 0.99, 1.70, 2.32), (0.25, 0.30): (0.25, 0.83, 1.23, 1.74),
                   (0.30, 0.35): (0.16, 0.63, 0.92, 1.16), (0.35, 0.40): (0.13, 0.42, 0.75, 0.90),
                   (0.40, 0.45): (0.11, 0.35, 0.59, 0.71), (0.45, 0.50): (0.09, 0.26, 0.46, 0.52)},
    (1.35, 1.55): {(0.10, 0.15): (0.60, 1.39, 2.34, 3.46), (0.15, 0.20): (0.70, 1.29, 2.06, 2.89),
                   (0.20, 0.25): (0.41, 0.84, 1.60, 1.78), (0.25, 0.30): (0.34, 0.55, 1.04, 1.28),
                   (0.30, 0.35): (0.24, 0.41, 0.69, 0.89), (0.35, 0.40): (0.16, 0.32, 0.52, 0.66),
                   (0.40, 0.45): (0.08, 0.27, 0.41, 0.47), (0.45, 0.50): (0.06, 0.20, 0.29, 0.31)},
    (1.55, 1.75): {(0.10, 0.15): (0.73, 1.17, 2.09, 3.05), (0.15, 0.20): (0.65, 1.20, 1.76, 2.45),
                   (0.20, 0.25): (0.39, 0.73, 1.29, 1.30), (0.25, 0.30): (0.22, 0.43, 0.82, 0.86),
                   (0.30, 0.35): (0.16, 0.34, 0.48, 0.69), (0.35, 0.40): (0.10, 0.26, 0.35, 0.49),
                   (0.40, 0.45): (0.07, 0.16, 0.26, 0.38), (0.45, 0.50): (0.04, 0.10, 0.19, 0.26)},
    (1.75, 1.95): {(0.10, 0.15): (0.72, 1.13, 1.78, 2.36), (0.15, 0.20): (0.52, 1.09, 1.44, 1.84),
                   (0.20, 0.25): (0.32, 0.65, 0.92, 1.10), (0.25, 0.30): (0.11, 0.36, 0.56, 0.58),
                   (0.30, 0.35): (0.11, 0.25, 0.30, 0.41), (0.35, 0.40): (0.09, 0.15, 0.23, 0.31),
                   (0.40, 0.45): (0.07, 0.11, 0.20, 0.30), (0.45, 0.50): (0.04, 0.09, 0.14, 0.21)},
    (1.95, 2.15): {(0.10, 0.15): (0.69, 1.08, 1.52, 1.84), (0.15, 0.20): (0.43, 0.84, 1.11, 1.35),
                   (0.20, 0.25): (0.23, 0.40, 0.68, 0.90), (0.25, 0.30): (0.08, 0.21, 0.42, 0.51),
                   (0.30, 0.35): (0.05, 0.11, 0.24, 0.34), (0.35, 0.40): (0.03, 0.07, 0.17, 0.19),
                   (0.40, 0.45): (0.02, 0.08, 0.12, 0.14), (0.45, 0.50): (0.02, 0.08, 0.08, 0.09)},
}
HARP_PB_PIMINUS_FWD_BY_E = {
    (0.050, 0.100): {(0.50, 1.00): (0.06, 0.37, 0.72, 1.35), (1.00, 1.50): (0.0, 0.30, 0.54, 1.37),
                     (1.50, 2.00): (0.01, 0.15, 0.47, 0.92), (2.00, 2.50): (0.0, 0.06, 0.27, 0.77),
                     (2.50, 3.00): (0.0, 0.04, 0.15, 0.43), (3.00, 3.50): (0.0, 0.0, 0.05, 0.47),
                     (3.50, 4.00): (0.0, 0.0, 0.06, 0.29), (4.00, 5.00): (0.0, 0.0, 0.034, 0.13),
                     (5.00, 6.50): (0.0, 0.0, 0.0, 0.03), (6.50, 8.00): (0.0, 0.0, 0.0, 0.008)},
    (0.100, 0.150): {(0.50, 1.00): (0.24, 0.43, 1.01, 2.23), (1.00, 1.50): (0.004, 0.19, 0.58, 1.39),
                     (1.50, 2.00): (0.003, 0.05, 0.37, 0.86), (2.00, 2.50): (0.0, 0.07, 0.17, 0.50),
                     (2.50, 3.00): (0.0, 0.03, 0.14, 0.31), (3.00, 3.50): (0.0, 0.007, 0.07, 0.21),
                     (3.50, 4.00): (0.0, 0.003, 0.037, 0.19), (4.00, 5.00): (0.0, 0.0, 0.013, 0.09),
                     (5.00, 6.50): (0.0, 0.0, 0.002, 0.024), (6.50, 8.00): (0.0, 0.0, 0.0, 0.002)},
    (0.150, 0.200): {(0.50, 1.00): (0.11, 0.39, 0.98, 1.98), (1.00, 1.50): (0.07, 0.14, 0.50, 0.90),
                     (1.50, 2.00): (0.0, 0.05, 0.27, 0.58), (2.00, 2.50): (0.0, 0.04, 0.17, 0.33),
                     (2.50, 3.00): (0.0, 0.01, 0.07, 0.24), (3.00, 3.50): (0.0, 0.007, 0.033, 0.19),
                     (3.50, 4.00): (0.0, 0.002, 0.011, 0.08), (4.00, 5.00): (0.0, 0.0, 0.0, 0.05),
                     (5.00, 6.50): (0.0, 0.0, 0.0, 0.019)},
    (0.200, 0.250): {(0.50, 1.00): (0.19, 0.41, 0.68, 1.41), (1.00, 1.50): (0.03, 0.16, 0.37, 0.85),
                     (1.50, 2.00): (0.01, 0.02, 0.17, 0.81), (2.00, 2.50): (0.0, 0.02, 0.07, 0.40),
                     (2.50, 3.00): (0.0, 0.021, 0.014, 0.16), (3.00, 3.50): (0.0, 0.0, 0.0, 0.15),
                     (3.50, 4.00): (0.0, 0.0, 0.0, 0.04), (4.00, 5.00): (0.0, 0.0, 0.0, 0.01)},
}


def harp_sigma_at(i):
    """Integrated pi- cross section at beam momentum index i, over the coverage
    common to all four energies, barn."""
    la = sum(v[i] * (ph - pl) * (thi - tlo)
             for (tlo, thi), b in HARP_PB_PIMINUS_BY_E.items()
             for (pl, ph), v in b.items())
    fw = 0.0
    for (tlo, thi), b in HARP_PB_PIMINUS_FWD_BY_E.items():
        dom = 2 * math.pi * (math.cos(tlo) - math.cos(thi))
        fw += sum(v[i] * (ph - pl) for (pl, ph), v in b.items()) * dom
    return la + fw


def harp_yield_at(i):
    return harp_sigma_at(i) / SIGMA_INEL_PB


def harp_cost_at(i):
    """GeV of beam per pi- PRODUCED at beam momentum index i, per interaction."""
    return HARP_BEAM_MOMENTA[i] / harp_yield_at(i)


# ---- the uncovered wedge, interpolated rather than bounded -----------------
HARP_GAP_SOLID_ANGLE = 2 * math.pi * (math.cos(0.25) - math.cos(0.35))


def wedge_added_sigma():
    """The 0.25-0.35 rad wedge neither HARP spectrometer covers, estimated by
    log-interpolating the two tables' per-steradian densities in the momentum
    band where they OVERLAP (0.5-0.8 GeV/c) and carrying the large-angle
    spectrum's shape across. RECONSTRUCTED, not measured: the two tables cover
    different momentum ranges, so no interpolation returns the wedge's own
    spectrum. It replaces a bound of 1.10 with a value."""
    la = HARP_PB_PIMINUS_8GEV[(0.35, 0.55)]
    fw = dict(HARP_PB_PIMINUS_8GEV_FWD[(0.200, 0.250)])
    t_la, t_fw, t_g = 0.45, 0.225, 0.30
    ov = [(0.50, 0.60), (0.60, 0.70), (0.70, 0.80)]
    la_ov = sum(la[b] * (b[1] - b[0]) for b in ov) / (2 * math.pi * math.sin(t_la))
    fw_ov = fw[(0.50, 1.00)] * 0.30
    f = (t_g - t_fw) / (t_la - t_fw)
    d_g = math.exp(math.log(fw_ov) + f * (math.log(la_ov) - math.log(fw_ov)))
    la_tot = sum(v * (b[1] - b[0]) for b, v in la.items()) / (2 * math.pi * math.sin(t_la))
    return la_tot * (d_g / la_ov) * HARP_GAP_SOLID_ANGLE


def wedge_factor():
    return 1.0 + wedge_added_sigma() / harp_combined_sigma()


def cost_per_pion_with_wedge():
    return 8.0 / ((harp_combined_sigma() + wedge_added_sigma()) / SIGMA_INEL_PB)


# ---- the 2.37, resolved as a normalisation rather than a physics gain ------
KELLY_PI_PER_BEAM_D = 0.77     # per BEAM deuteron
KELLY_BEAM_GEV = 3.61
KELLY_ROD_MM, W_LAMBDA_I_MM = 652.0, 103.0


def kelly_cost():
    return KELLY_BEAM_GEV / KELLY_PI_PER_BEAM_D


def kelly_nucleons_required(i):
    """Interacting nucleons per beam deuteron that Kelly's per-beam-particle
    yield requires, if each behaves as a HARP proton at beam momentum index i."""
    return KELLY_PI_PER_BEAM_D / harp_yield_at(i)


def cost_at_multiplicity(n, i=2):
    """This paper's own figure re-normalised from per-interaction to per-beam-
    particle, at n interacting nucleons per beam particle."""
    return HARP_BEAM_MOMENTA[i] / (harp_yield_at(i) * n)


def kelly_multiplicity_that_reconciles():
    """The multiplicity at which this paper's figure equals Kelly's."""
    return harp_cost_at(2) / kelly_cost()


def rod_interaction_lengths():
    return KELLY_ROD_MM / W_LAMBDA_I_MM


# ---- in-situ acceptance from a SECOND published capture simulation --------
def insitu_from_comet(power_mw=1.0, ep_gev=8.0, p_stop_mev=265.0, hi=False):
    """Binders per second from COMET's own 5 T capture figure with BLOCK 2 --
    decay and transport -- removed, because an in-situ cell sits AT the capture
    point and has no beamline. An independent route to the number sec.5.24
    models, sharing neither the simulation nor the field."""
    cap = COMET_CAPTURED_HI if hi else COMET_CAPTURED_LO
    frac_stopping = stopping_capture(p_stop_mev) / delivered_fraction(1.50, "fwd")
    return protons_per_s(power_mw, ep_gev) * cap * frac_stopping


# ---- the open questions, WORKED --------------------------------------------
# The first pass of this report sorted nine open questions into categories. A
# category is not an answer, and six of the nine were calculations this
# repository could already do. What follows is what each one returned. The
# status column is the corpus's own discipline: CLOSED where a computation
# settles it, NARROWED where it moves a bound, EXPLAINED where a mechanism
# reproduces the number but is not adopted into the balances.
#
# (id, question, status, what it returned)
OPEN = [
    ("Q1", "the acceptance has never been measured end to end", "NARROWED",
     "the span was withdrawn -- it compared two machines, not two estimates. A "
     "claimed second corroboration is ALSO withdrawn: it used the forward "
     "hemisphere against a machine that captures backward. The model now HAS the "
     "mirror term the failure exposed, worth 1.299 at a grade of 1.428 (--magnet), "
     "so it is no longer a lower bound against a graded field. It still has one "
     "validation, 0.982, and nothing has measured it end to end"),
    ("Q2", "which sticking branch is operative", "CLOSED",
     "inverting the witnessed 150 cycles gives 0.517-0.547 percent, inside the "
     "measured trio and below theory: a third route using neither published "
     "sticking measurement"),
    ("Q3", "the service-life model over-predicts its one checkable point by 2.24", "CLOSED",
     "at the corrected sticking it returns 150.5 cycles against 150 measured. "
     "The over-prediction was the sticking and nothing else"),
    ("Q4", "fuel purity is bounded by no experiment here", "CLOSED",
     "the fuel behind the 150 carried at most 0 to 10.93 ppm, below the "
     "31.10 ppm parity level at every density and sticking in the bracket"),
    ("Q5", "the temperature axis is confounded with purity and density", "CLOSED",
     "every balance already runs the cycle rate AT its ceiling, so deconfounding "
     "cannot raise any figure; and the co-product uses a measured cycle count, "
     "which carries whatever temperature produced it"),
    ("Q6", "the 2.37 between measured and optimised production is unexplained", "EXPLAINED",
     "it is a normalisation: per-interaction against per-beam-particle. 2.389 "
     "interacting nucleons reproduce the optimised figure to 0.8 percent, the "
     "value required is bracketed by HARP's own energy dependence, and a "
     "deuteron on 6.3 interaction lengths guarantees the lower end"),
    ("Q7", "HARP's two datasets leave a 0.186 sr wedge uncovered", "CLOSED",
     "log-interpolating the two tables where their momentum coverage overlaps "
     "puts the wedge at 1.072, against a bound of 1.10 -- production 10.39 GeV "
     "per pi- rather than 11.13"),
    ("Q8", "transport, cooling and stopping are unmodelled losses", "CLOSED",
     "retired by sec.6: in-situ capture has no transport line, and the stopping "
     "fraction is now computed rather than assumed"),
    ("Q9", "the composed sticking 0.234 inherits an unresolved figure", "CLOSED",
     "superseded by sec.5.26: no composed sticking enters any current balance"),
]


COMET_BORE_M = 0.15          # the radius the pT formula is already validated on:
                             # 5 T x 0.15 m returns 112.5 MeV/c against COMET's
                             # stated 100 MeV/c cap


def comet_model_at_aperture(r_m=COMET_BORE_M, b_t=5.0, hemisphere="back"):
    """The sec.5.24 acceptance model at COMET's own aperture, in COMET's own
    units: captured pi- per interacting proton, no stopping window.

    THE HEMISPHERE IS BACKWARD AND THAT IS NOT A DETAIL. COMET's transport
    solenoid takes "backward-emitted secondary pions and muons" (arXiv:2505.07464
    sec.1), the opposite of the NF front end sec.5.24 is validated against. An
    earlier pass of this file compared COMET against the FORWARD number, got
    0.0843 against a published 0.061-0.144, and reported the model as
    corroborated at a second field. It is not. See comet_scope_ratio()."""
    return delivered_fraction(b_t * r_m, hemisphere) * harp_combined_yield()


def comet_scope_ratio():
    """Model over the midpoint of COMET's published range, in the hemisphere
    COMET actually captures. It is 0.12, and it is a SCOPE LIMIT rather than a
    disagreement: a graded capture solenoid magnetically MIRRORS forward-going
    particles back into a backward channel, and this model has no mirror term at
    all -- only a transverse momentum cap. Against a graded field the model is
    therefore a LOWER bound and not an estimate, by a factor it cannot state."""
    return comet_model_at_aperture() / (0.5 * (COMET_CAPTURED_LO + COMET_CAPTURED_HI))


def mars_validation_ratio():
    """The one validation the model has, and it is at exactly the configuration
    sec.6 specifies: forward capture, 20 T on 7.5 cm, the front end's own rf
    window. Strait et al. sec.II states the forward hemisphere explicitly."""
    return (delivered_fraction(1.50, "fwd", NF_RF_WINDOW_MEV)
            / (nf_captured_per_interacting_proton() / harp_combined_yield()))


def acceptance_corroboration():
    """WITHDRAWN as a two-sided band. The model has ONE validation, at the
    configuration it is used for; the second comparison turned out to be a
    hemisphere error. Returns (ratio, 1.0) -- the agreement and unity."""
    r = mars_validation_ratio()
    return tuple(sorted((r, 1.0)))


def open_modelled_mu_per_s(power_mw=1.0, ep_gev=8.0, p_stop_mev=265.0):
    """Binders per second at the specified aperture -- the value, not a bound."""
    return (protons_per_s(power_mw, ep_gev) * harp_combined_yield()
            * stopping_capture(p_stop_mev))


def open_band_mu_per_s(power_mw=1.0):
    """That value scaled by the two corroboration ratios. NOT a floor-to-ceiling
    span between two rival estimates -- the model reproduces both simulations,
    and this is the width of the agreement."""
    lo, hi = acceptance_corroboration()
    v = open_modelled_mu_per_s(power_mw)
    return v * lo, v * hi


def open_floor_transported(power_mw=1.0):
    """The SUPERSEDED floor: MuSIC MEASURED, through a transport line. It is a
    floor on a different quantity -- what survives a beamline -- and using it as
    a floor on in-situ capture was an error, corrected in sec.5.30."""
    return MUSIC_MU_MINUS_PER_W * power_mw * 1e6


def open_floor_mu_per_s(power_mw=1.0):
    return open_band_mu_per_s(power_mw)[0]


def open_ceiling_mu_per_s(power_mw=1.0, ep_gev=8.0, p_stop_mev=265.0):
    return open_modelled_mu_per_s(power_mw, ep_gev, p_stop_mev)


def open_heat_pct(mu_per_s, cycles=150.0, power_mw=1.0):
    return 100.0 * mu_per_s * cycles * MEV_PER_FUSION_HEAT * 1.602176634e-13 / (power_mw * 1e6)


def report_open():
    import mucf
    print("THE OPEN QUESTIONS, WORKED")
    print()
    print("  Nine were carried. Six were calculations this repository could")
    print("  already do. Categories are not answers; these are the answers.")
    print()
    for qid, text, status, got in OPEN:
        print(f"  {qid}  [{status}]  {text}")
        for line in _wrap(got, 68):
            print(f"        {line}")
        print()

    print("  Q1 -- TWO WITHDRAWALS, AND WHAT IS ACTUALLY KNOWN")
    print("    First withdrawal. Two earlier passes quoted a SPAN on the acceptance")
    print(f"    -- {open_ceiling_mu_per_s() / open_floor_transported():,.0f}x, then 5.97x -- by treating a 5 T machine's output as a")
    print("    lower ESTIMATE of a 20 T machine's. It is not one, and both are gone.")
    print()
    print("    Second withdrawal, and it is this report's own from one pass ago.")
    print("    Replacing that span with a 'second corroboration' compared the model's")
    print("    FORWARD hemisphere against a machine that captures BACKWARD. In the")
    print("    hemisphere COMET actually takes:")
    print()
    print(f"      model at 5 T x {COMET_BORE_M:.2f} m, backward:"
          f" {comet_model_at_aperture():.4f} pi- per interacting proton")
    print(f"      COMET published:                  "
          f" {COMET_CAPTURED_LO:.3f}-{COMET_CAPTURED_HI:.3f}")
    print(f"      ratio {comet_scope_ratio():.3f} -- the model is low by"
          f" {1 / comet_scope_ratio():.1f}x, not inside the range")
    print()
    print("    That is a SCOPE LIMIT, not a disagreement. A graded capture solenoid")
    print("    magnetically MIRRORS forward-going particles into a backward channel,")
    print("    and this model has no mirror term -- only a transverse cap. Against a")
    print("    graded field it is a LOWER bound by a factor it cannot state.")
    print()
    print(f"    WHAT IS KNOWN: one validation, {mars_validation_ratio():.3f}, against the front-end")
    print("    simulation at exactly the configuration sec.6 specifies -- forward")
    print("    capture, 20 T on 7.5 cm. One simulation, at one configuration.")
    v = open_modelled_mu_per_s()
    print(f"    The value is {v:.3e} binders/s and {open_heat_pct(v):.2f} % of the host beam,")
    print("    with an unquantified conservative bias from the missing mirror term.")
    print()
    print("    WHAT IS OPEN: nothing has been measured. Stage A measures it, and no")
    print("    calculation in this repository can stand in for that.")
    print()
    print("  Q2-Q4 -- THE STICKING, THE MODEL AND THE FUEL, FROM ONE MEASUREMENT")
    for phi in mucf.PHI_LOS_ALAMOS:
        print(f"    150 cycles at phi {phi:.1f} implies omega_eff ="
              f" {100 * mucf.omega_from_cycles(phi=phi):.4f} %")
    print(f"    measured trio: {', '.join('%.3f' % (100 * w) for w in mucf.OMEGA_EFF_MEASURED)} %"
          f"   theory: {100 * mucf.OMEGA_EFF_THEORY:.3f} %")
    print(f"    at 0.515 % the service-life model returns"
          f" {mucf.cycles(0.00515, 1.2):.1f} cycles, not 335.3")
    worst = max((mucf.contamination_bound(omega_s=w, phi=1.5) or 0.0)
                for w in mucf.OMEGA_EFF_MEASURED)
    print(f"    and that fuel carried at most {worst * 1e6:.2f} ppm, against a parity"
          f" level of {mucf.purity_for_parity(1.5) * 1e6:.2f}")
    print()
    print("  Q6 -- THE 2.37, AND IT IS NOT A DISCREPANCY")
    print("    beam energy first, since it was the last candidate standing:")
    print("      beam GeV/c    pi- per interaction    GeV per pi-")
    for i, e in enumerate(HARP_BEAM_MOMENTA):
        print(f"      {e:9.1f}    {harp_yield_at(i):18.4f}    {harp_cost_at(i):11.3f}")
    print("    -> a broad optimum near 8 GeV/c. Going DOWN to Kelly's energy makes")
    print(f"       production {harp_cost_at(0) / harp_cost_at(2):.2f}x dearer, not 2.37x cheaper."
          " Beam energy is refuted.")
    print()
    print("    what survives is the normalisation. Kelly quotes"
          f" {KELLY_PI_PER_BEAM_D} pi- per BEAM")
    print(f"    deuteron at {KELLY_BEAM_GEV} GeV = {kelly_cost():.2f} GeV per pi-."
          " HARP is per INTERACTION.")
    for i in (0, 1):
        print(f"      at {HARP_BEAM_MOMENTA[i]:.0f} GeV/c that needs"
              f" {kelly_nucleons_required(i):.2f} interacting nucleons per beam deuteron")
    print(f"      a deuteron carries 2, and the rod is"
          f" {rod_interaction_lengths():.1f} interaction lengths of tungsten,")
    print("      so the lower end is guaranteed before any secondary interacts.")
    print()
    print("    and this paper's own figure, re-normalised:")
    for n in (1.0, 2.0, kelly_multiplicity_that_reconciles(), 3.0):
        tag = "   <-- reproduces the optimised figure" \
            if abs(n - kelly_multiplicity_that_reconciles()) < 1e-9 else ""
        print(f"      {n:.3f} interacting nucleons per beam particle:"
              f" {cost_at_multiplicity(n):6.3f} GeV per pi-{tag}")
    print()
    print("    NOT ADOPTED. The mechanism reproduces the number, but it reproduces")
    print("    it for pions PRODUCED, and a thick target also reabsorbs them: the")
    print("    same source's thick/thin ratio for CAPTURED muons is 0.874-1.186 per")
    print("    interacting proton, which is evidence the gain may not survive to")
    print("    capture. sec.10.3 Stage C measures pions per BEAM particle against")
    print("    per interaction, on one target, and that is what it is now for.")
    print()
    print("  Q7 -- THE WEDGE, INTERPOLATED RATHER THAN BOUNDED")
    print(f"    the uncovered 0.25-0.35 rad wedge is {HARP_GAP_SOLID_ANGLE:.4f} sr and adds")
    print(f"    {wedge_added_sigma():.4f} barn to {harp_combined_sigma():.4f}:"
          f" a factor of {wedge_factor():.4f} against a bound of 1.10,")
    print(f"    so production is {cost_per_pion_with_wedge():.3f} GeV per pi- rather than"
          f" {cost_per_pion_produced():.3f}.")
    print("    RECONSTRUCTED: the two tables cover different momentum ranges, so no")
    print("    interpolation returns the wedge's own spectrum.")
    print()
    print("  WHAT IS LEFT.")
    n_open = len([q for q in OPEN if q[2] != "CLOSED"])
    print(f"    {len([q for q in OPEN if q[2] == 'CLOSED'])} closed,"
          f" {len([q for q in OPEN if q[2] == 'NARROWED'])} narrowed,"
          f" {len([q for q in OPEN if q[2] == 'EXPLAINED'])} explained and not adopted.")
    print(f"    {n_open} still move a number, and both are measurements rather than")
    print("    calculations: the acceptance (Stage A) and whether the thick-target")
    print("    normalisation survives to capture (Stage C).")
    print()
    print("  AND THE SIGN IS STILL OPEN AT NO VALUE OF ANY OF THEM.")
    print(f"    At the low end of the corroboration band and ONE fusion per binder:"
          f" {open_heat_pct(open_band_mu_per_s()[0], cycles=1.0):.5f} %")
    print("    of the host beam. Positive.")
    return 0


def _wrap(text, width):
    out, line = [], ""
    for w in text.split():
        if len(line) + len(w) + 1 > width:
            out.append(line)
            line = w
        else:
            line = (line + " " + w).strip()
    if line:
        out.append(line)
    return out


# ---- the magnetic mirror: the term the model did not have ------------------
# sec.5.30 records that this model captured the forward hemisphere and had no
# mirror term, and that against a graded field it is therefore a lower bound. A
# graded capture solenoid is graded FOR the mirror: the target sits at B_t in a
# field rising to B_max upstream, and a backward-going pion reflects rather than
# escaping. This is the term, and it is not a fitted one -- it is the adiabatic
# invariant p_T^2 / B with |p| conserved, which reflects a particle when its
# longitudinal momentum reaches zero:
#
#     reflected  <=>  sin(theta) >= sqrt(B_t / B_max)
#
# and the reflected pion emerges with the same p_T and its p_z reversed, so it
# enters the same transverse cap and the same decay integral as a forward one at
# pi - theta. Nothing else changes.
MIRROR_B_TARGET = 12.0       # T at the target, the design point of sec.11
MIRROR_B_MAX = 24.0          # T at the upstream plug


def mirror_loss_cone_rad(b_target=MIRROR_B_TARGET, b_max=MIRROR_B_MAX):
    """Half-angle of the upstream loss cone. Inside it a backward pion escapes."""
    return math.asin(min(1.0, math.sqrt(b_target / b_max)))


def mirrored_backward_fraction(b_target=MIRROR_B_TARGET, b_max=MIRROR_B_MAX):
    """Fraction of the backward hemisphere's SOLID ANGLE the mirror turns round.
    Geometry only -- it applies no transverse cap and is not a capture figure."""
    return math.cos(mirror_loss_cone_rad(b_target, b_max))


def _mirror_bins(b_target=MIRROR_B_TARGET, b_max=MIRROR_B_MAX):
    """Backward production the mirror returns, re-emitted forward: same p, same
    p_T, p_z reversed, hence theta -> pi - theta."""
    s_min = math.sqrt(b_target / b_max)
    for p, th, w in _production_bins():
        if th <= math.pi / 2:
            continue
        if math.sin(th) < s_min:          # inside the loss cone: escapes upstream
            continue
        yield p, math.pi - th, w


def delivered_fraction_mirrored(br, window=None, ncos=160, nphi=96,
                                b_target=MIRROR_B_TARGET, b_max=MIRROR_B_MAX):
    """Captured mu- per pi- PRODUCED, forward hemisphere PLUS the backward
    hemisphere the mirror returns. The transverse cap is applied to both in the
    same place and by the same test."""
    fwd = delivered_fraction(br, "fwd", window, ncos, nphi)
    ptm = pt_max(br) * 1000.0
    kept = total = 0.0
    for _, _, w in _production_bins():
        total += w
    for p_gev, th, w in _mirror_bins(b_target, b_max):
        if p_gev * math.sin(th) >= ptm / 1000.0:
            continue
        p = p_gev * 1000.0
        beta = p / math.hypot(p, M_PI_MEV)
        gam = math.hypot(p, M_PI_MEV) / M_PI_MEV
        st, ct = math.sin(th), math.cos(th)
        for i in range(ncos):
            cs = -1.0 + (2.0 * i + 1.0) / ncos
            ss = math.sqrt(max(0.0, 1.0 - cs * cs))
            ppar = gam * (P_STAR_MEV * cs + beta * E_STAR_MEV)
            pperp = P_STAR_MEV * ss
            for j in range(nphi):
                phi = 2 * math.pi * (j + 0.5) / nphi
                cf = math.cos(phi)
                px = ppar * st + pperp * cf * ct
                py = pperp * math.sin(phi)
                pz = ppar * ct - pperp * cf * st
                if math.hypot(px, py) >= ptm:
                    continue
                pm = math.sqrt(px * px + py * py + pz * pz)
                if window and not (window[0] <= pm <= window[1]):
                    continue
                kept += w / (ncos * nphi)
    return fwd + kept / total


def mirror_gain(br=1.50, window=None):
    return delivered_fraction_mirrored(br, window) / delivered_fraction(br, "fwd", window)


# ---- the capture solenoid, designed ----------------------------------------
# The mirror requirement is a specification and not a search: the loss cone stops
# biting once sqrt(B_t/B_max) falls below sin(2.15 rad), the edge of HARP's own
# table, and beyond that ratio nothing MEASURED is added. That fixes the grade at
# 1.428 and frees the absolute field to be chosen by what a magnet can hold.
#
# And B*R is what sets capture, not B. So the target field can be dropped and the
# bore grown to keep B*R, which is what puts the peak field inside reach.
MU_0 = 4.0e-7 * math.pi
MIRROR_RATIO_REQUIRED = 1.0 / math.sin(HARP_BACKWARD_EDGE_RAD) ** 2

# The design point.
DES_B_PEAK = 20.0            # T at the upstream plug -- large-bore HTS territory
DES_B_TARGET = DES_B_PEAK / MIRROR_RATIO_REQUIRED
DES_BR = 1.50                # T.m, the front end's own aperture, held
# SOURCED, and it supersedes a shield thickness this file chose for itself.
# Back, arXiv:1104.2742 (JINST), FLUKA and MARS over the Neutrino Factory target
# station -- a 4 MW, 8 GeV proton beam on a mercury jet in a 20 T solenoid, which
# is this machine. That study found a coil inner radius of 63 cm INADEQUATE and
# doubled it to 120 cm to bring the coil heat load below 1 kW. The shield is
# therefore not a free parameter here and the earlier 70 cm is withdrawn.
DES_COIL_INNER_SOURCED_M = 1.20
DES_W_LAMBDA_M = 0.103       # interaction length of tungsten
DES_SIGMA_ALLOW_MPA = 300.0  # conductor hoop stress with steel reinforcement
DES_LENGTH_M = 1.5           # magnetic length of the capture region


def des_bore_m(br=DES_BR, b_target=None):
    """Warm bore radius that holds the aperture at the chosen target field."""
    return br / (DES_B_TARGET if b_target is None else b_target)


def des_coil_inner_m(br=DES_BR):
    """SOURCED. Not bore plus a shield of this file's choosing: the published
    simulation of this machine sets it, having found a smaller radius unusable."""
    return DES_COIL_INNER_SOURCED_M


def des_shield_m(br=DES_BR):
    return des_coil_inner_m(br) - des_bore_m(br)


def des_taper_length_m(br=DES_BR, n_gyro=10.0):
    """Adiabaticity: the field must change slowly against a gyro-orbit. Requires
    L >> r_g / (dB/B). Taken at the transverse cap, the worst orbit there is."""
    r_g = gyroradius_cm(pt_max(br), DES_B_TARGET) / 100.0
    return n_gyro * r_g / (1.0 - 1.0 / MIRROR_RATIO_REQUIRED)


def des_stored_energy_j(br=DES_BR, length_m=DES_LENGTH_M):
    """B^2/2mu_0 over the bore out to the coil, at the peak field. A solenoid's
    true stored energy includes the winding pack and the return path; this is the
    field-volume term and is a LOWER bound on it."""
    r = des_coil_inner_m(br)
    return (DES_B_PEAK ** 2 / (2 * MU_0)) * math.pi * r * r * length_m


def des_current_density_a_mm2(br=DES_BR):
    """Engineering current density the hoop stress allows: sigma = B J r."""
    r = des_coil_inner_m(br)
    return (DES_SIGMA_ALLOW_MPA * 1e6) / (DES_B_PEAK * r) / 1e6


def des_amp_turns(length_m=DES_LENGTH_M):
    """NI = B L / mu_0 for a long solenoid."""
    return DES_B_PEAK * length_m / MU_0


def des_winding_thickness_m(br=DES_BR, length_m=DES_LENGTH_M):
    """Radial build the allowed current density implies."""
    j = des_current_density_a_mm2(br) * 1e6
    return des_amp_turns(length_m) / (j * length_m)


def des_shield_attenuation(shield_m=None):
    return math.exp((des_shield_m() if shield_m is None else shield_m) / DES_W_LAMBDA_M)


# SOURCED, Back arXiv:1104.2742 table 3: 0.56 kW into all nineteen coils at 4 MW
# with the 120 cm shielding. This REPLACES a reconstructed figure of 335 W that
# this file computed from an assumed 30 percent of beam power into the shield.
DES_COIL_LOAD_KW_AT_4MW = 0.56


def des_heat_load_w(power_mw=1.0):
    """Beam power reaching the cold mass. No longer reconstructed: it is the
    published simulation's own figure for this machine, scaled by beam power."""
    return DES_COIL_LOAD_KW_AT_4MW * 1e3 * power_mw / 4.0


def des_refrigeration_w(power_mw=1.0):
    """Wall power to remove that at 4.5 K, at a Carnot fraction of 0.25."""
    return des_heat_load_w(power_mw) * (300.0 / 4.5) / 0.25


def report_magnet():
    """The capture solenoid, designed -- and the mirror term sec.5.30 said the
    acceptance model did not have."""
    print("THE CAPTURE SOLENOID, DESIGNED")
    print()
    print("  sec.5.30 records that this model captures the forward hemisphere and")
    print("  has no magnetic mirror term, so against a graded field it is a lower")
    print("  bound. A graded field is not an accident of other machines: it is what")
    print("  a capture solenoid IS. Designing one supplies the term.")
    print()
    print("  THE MIRROR, FROM THE ADIABATIC INVARIANT AND NOTHING ELSE.")
    print("    p_T^2 / B is conserved and |p| is conserved, so a backward pion")
    print("    reflects when its longitudinal momentum reaches zero:")
    print("        reflected  <=>  sin(theta) >= sqrt(B_t / B_max)")
    print("    and comes back with the same p_T and p_z reversed -- into the same")
    print("    transverse cap and the same decay integral, at pi - theta.")
    print()
    print("    B_max/B_t   loss cone      captured mu- per pi- produced")
    base = delivered_fraction(1.50, "fwd", (0.0, 265.0))
    for r in (1.05, 1.15, 1.25, 1.35, MIRROR_RATIO_REQUIRED, 2.00, 3.00):
        m = delivered_fraction_mirrored(1.50, (0.0, 265.0), b_target=10.0, b_max=10.0 * r)
        tag = "   <-- saturates here" if abs(r - MIRROR_RATIO_REQUIRED) < 1e-9 else ""
        print(f"      {r:5.3f}      {math.degrees(math.asin(min(1, math.sqrt(1 / r)))):5.1f} deg"
              f"        {m:.4f}   x{m / base:.3f}{tag}")
    print()
    print(f"    It saturates at {MIRROR_RATIO_REQUIRED:.3f} because HARP's large-angle table stops at")
    print(f"    {HARP_BACKWARD_EDGE_RAD} rad, where sin = {math.sin(HARP_BACKWARD_EDGE_RAD):.3f}. Past that ratio the loss cone")
    print("    no longer touches any MEASURED production, so a deeper grade buys")
    print("    nothing this repository can count. THE GRADE IS A SPECIFICATION,")
    print("    NOT A SEARCH -- which is the same shape as sec.5.7's finding on the")
    print("    binder mass and sec.5.28's on the target.")
    print()
    print("  AND B*R IS WHAT SETS CAPTURE, NOT B. That frees the design.")
    print(f"    Holding the front end's own aperture at {DES_BR} T.m, the target field")
    print("    can be dropped and the bore grown, which is what puts the PEAK field")
    print("    inside what a magnet holds:")
    print()
    print(f"      peak field, upstream plug          {DES_B_PEAK:8.1f} T")
    print(f"      target field                       {DES_B_TARGET:8.2f} T"
          f"   (grade {DES_B_PEAK / DES_B_TARGET:.3f})")
    print(f"      warm bore radius                   {100 * des_bore_m():8.1f} cm")
    print(f"      delivered beam envelope there      {beam_envelope_cm(DES_BR, DES_B_TARGET, DES_B_TARGET):8.2f} cm"
          "   -- fills the bore, by construction")
    print(f"      gyroradius at the transverse cap   {gyroradius_cm(pt_max(DES_BR), DES_B_TARGET):8.2f} cm")
    print(f"      adiabatic taper, 10 gyro-orbits    {des_taper_length_m():8.2f} m")
    print(f"      magnetic length of the capture     {DES_LENGTH_M:8.2f} m")
    print()
    print("  THE COLD MASS.")
    print(f"      tungsten shield                    {100 * des_shield_m():8.1f} cm"
          f"   ({des_shield_attenuation():,.0f}x on the cascade)")
    print(f"      coil inner radius                  {100 * des_coil_inner_m():8.1f} cm")
    print(f"      amp-turns                          {des_amp_turns() / 1e6:8.1f} MA-turns")
    print(f"      hoop stress allowed                {DES_SIGMA_ALLOW_MPA:8.0f} MPa")
    print(f"      engineering current density        {des_current_density_a_mm2():8.1f} A/mm2"
          "   sigma = B J r")
    print(f"      winding radial build               {100 * des_winding_thickness_m():8.1f} cm")
    print(f"      stored energy, field volume        {des_stored_energy_j() / 1e6:8.0f} MJ   LOWER bound")
    print()
    print("  THE PLANT.")
    print(f"      heat to the cold mass at 1 MW      {des_heat_load_w():8.0f} W")
    print(f"      refrigeration wall power           {des_refrigeration_w() / 1e3:8.1f} kW"
          "   at 4.5 K, Carnot 0.25")
    print()
    print("  WHAT THE MIRROR IS WORTH TO THE ANSWER.")
    m = delivered_fraction_mirrored(DES_BR, (0.0, 265.0))
    print(f"      captured and stopped, forward only  {base:.4f}")
    print(f"      with the mirror                     {m:.4f}   x{m / base:.3f}")
    print(f"      fusion heat, fraction of host beam  {100 * insitu_heat_fraction(base):.2f} %"
          f" -> {100 * insitu_heat_fraction(m):.2f} %")
    print()
    print("  WHAT THIS IS NOT. It is a physics design and a set of engineering")
    print("  requirements, not a build package. Three things are named and not")
    print("  done: the quench and energy-extraction design for a stored energy")
    print("  this size, the conductor choice and grading (above about 16 T only")
    print("  REBCO reaches it, so the insert is HTS and the outsert may be Nb3Sn),")
    print("  and the shielding, whose one RECONSTRUCTED number -- the fraction of")
    print("  beam power entering the shield rather than the target's own cooling")
    print("  -- a transport simulation owns and this repository does not.")
    print()
    print("  The hoop-stress figure assumes the CONDUCTOR carries the whole hoop")
    print("  load. A steel former carrying it instead raises the allowed current")
    print("  density several times and thins the winding in proportion; that is a")
    print("  design choice, and the conservative one is quoted.")
    return 0


def report_species():
    """Which pion the reactor is actually buying, and what that requires of the
    target. Only mu- catalyses; mu- comes only from pi-; so every yield here is
    a pi- yield and the charge split is a term in the budget, not a detail."""
    fp = charge_fraction_produced()
    print("SPECIES -- which pion, measured off the HARP tables for both charges")
    print()
    print("  Only mu- catalyses. A mu+ binds an electron into muonium and is")
    print("  repelled by every nucleus, so it forms no mesomolecule at all. The")
    print("  catalytic cycle exists for one sign, and mu- comes only from pi-.")
    print()
    print("  charge split of everything produced, p-Pb at 8 GeV/c")
    for label, mm, pp in (
            ("large angle, 0.35-2.15 rad",
             _la_sigma(HARP_PB_PIMINUS_8GEV), _la_sigma(HARP_PB_PIPLUS_8GEV)),
            ("forward, 0.025-0.25 rad",
             _fwd_sigma(HARP_PB_PIMINUS_8GEV_FWD), _fwd_sigma(HARP_PB_PIPLUS_8GEV_FWD))):
        print(f"    {label:<30} sigma- {mm:.3f} b   sigma+ {pp:.3f} b"
              f"   pi-/pi+ {mm / pp:.3f}")
    print(f"    {'all of it':<30} f(pi-) = {fp:.4f}"
          f"   -- BELOW one half: pi+ is the majority channel")
    print()
    print("  but the collector does not take all of it, and the part it takes")
    print("  is the part where the split runs the other way")
    for lo, hi in ((0.10, 0.15), (0.15, 0.20), (0.20, 0.25), (0.30, 0.35),
                   (0.45, 0.50), (0.70, 0.80)):
        r = charge_ratio(HARP_PB_PIMINUS_8GEV, HARP_PB_PIPLUS_8GEV, window=(lo, hi))
        print(f"    p {lo:.2f}-{hi:.2f} GeV/c   pi-/pi+ = {r:.3f}"
              f"{'   <-- pi- in the majority' if r > 1 else ''}")
    fa = charge_fraction_accepted(1.50, "fwd", NF_RF_WINDOW_MEV)
    print()
    print("  through the built front end's own acceptance -- 20 T on 7.5 cm, the")
    print("  two-body decay, and its rf window -- applied to each charge in turn:")
    print(f"    f(pi-) accepted = {fa:.4f}   against {fp:.4f} produced")
    print(f"    the halving this repository has always applied assumes"
          f" {CHARGE_FRACTION_ASSUMED:.4f}")
    print(f"    difference {100 * abs(fa / CHARGE_FRACTION_ASSUMED - 1):.1f} percent,"
          f" inside HARP's own {100 * HARP_NORM_UNCERTAINTY_PB:.0f} percent"
          f" normalisation uncertainty")
    print("    -> the halving stands, MEASURED. No balance moves. Not adopted as a")
    print("       correction: a shift smaller than the uncertainty of the")
    print("       measurement that found it is a bound, not a value.")
    print()
    print("  what it does settle is the target, and that is not a detail")
    rpb = charge_ratio(HARP_PB_PIMINUS_8GEV, HARP_PB_PIPLUS_8GEV)
    ral = charge_ratio(HARP_AL_PIMINUS_8GEV, HARP_AL_PIPLUS_8GEV)
    for el, r in (("Pb", rpb), ("Al", ral)):
        print(f"    {el}  N/Z = {N_OVER_Z[el]:.3f}   pi-/pi+ = {r:.3f}"
              f"   f(pi-) = {r / (1 + r):.4f}")
    fpb, fal = rpb / (1 + rpb), ral / (1 + ral)
    print(f"    lead over aluminium in the ratio: {rpb / ral:.3f};"
          f" in the usable fraction: {fpb / fal:.3f}")
    print("    At equal TOTAL charged-pion yield a low-Z target delivers"
          f" {fal / fpb:.3f} of")
    print("    lead's pi-, the rest going to the sign that cannot catalyse. So a")
    print("    high-Z target is required for the CHARGE and not only for the")
    print("    yield, and sec.10's tungsten rod already satisfies it. This is a")
    print("    requirement the balances met without stating why.")
    print()
    print("  and the charge split is not a lever")
    (blo, bhi), br_ = max(
        (((lo, hi), charge_ratio(HARP_PB_PIMINUS_8GEV, HARP_PB_PIPLUS_8GEV,
                                 window=(lo, hi)))
         for lo, hi in ((0.10, 0.15), (0.15, 0.20), (0.20, 0.25))),
        key=lambda kv: kv[1])
    keep = (_la_sigma(HARP_PB_PIMINUS_8GEV, window=(blo, bhi))
            / _la_sigma(HARP_PB_PIMINUS_8GEV))
    print(f"    the best single momentum bin is {blo:.2f}-{bhi:.2f} GeV/c at"
          f" f(pi-) = {br_ / (1 + br_):.4f},")
    print(f"    which is {br_ / (1 + br_) / fa:.3f} on the accepted fraction and costs"
          f" all but {100 * keep:.1f} percent")
    print(f"    of the pi- yield to reach. Selecting on charge cannot be bought.")
    return 0


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
    print("  acceptance model, validated against MARS15 (Strait et al. Table II)")
    mars = nf_captured_per_interacting_proton() / harp_combined_yield()
    got = delivered_fraction(1.50, "fwd", NF_RF_WINDOW_MEV)
    ok = abs(got / mars - 1.0) < 0.05
    fail += 0 if ok else 1
    print(f"    fwd hemisphere + rf window: model {100 * got:.2f}%"
          f" vs MARS15 {100 * mars:.2f}%   {'PASS' if ok else 'FAIL'}")
    ok = 0.99 < decay_survival(1.50) < 1.0
    fail += 0 if ok else 1
    print(f"    decay survival is just below unity: {decay_survival(1.50):.4f}"
          f"   {'PASS' if ok else 'FAIL'}")
    ok = delivered_fraction(1.50, "fwd") > delivered_fraction(1.50, "back")
    fail += 0 if ok else 1
    print(f"    the forward hemisphere is the large one, and the front end takes it:"
          f" {100 * delivered_fraction(1.50, 'fwd'):.1f}%"
          f" vs {100 * delivered_fraction(1.50, 'back'):.1f}%   {'PASS' if ok else 'FAIL'}")

    print()
    print("  stopping model, validated twice")
    mi = min(bethe_dedx(T) for T in [x * 0.5 for x in range(2, 4000)])
    ok = abs(mi / 4.034 - 1) < 0.05
    fail += 0 if ok else 1
    print(f"    min-ionising dE/dx in H2: {mi:.3f} vs PDG 4.034 MeV cm2/g"
          f"   {'PASS' if ok else 'FAIL'}")
    ci = tritium_curies(0.004 * T_MASS_FRAC_DT)
    ok = abs(ci / 24.0 - 1) < 0.10
    fail += 0 if ok else 1
    print(f"    MuFusE 4 mg fill: {ci:.1f} Ci vs the ~24 Ci they state"
          f"   {'PASS' if ok else 'FAIL'}")
    ok = abs(target_length_cm(265, 1.0) / target_length_cm(265, 8.5) - 8.5) < 1e-6
    fail += 0 if ok else 1
    print(f"    inventory is density-independent while length is not"
          f"   {'PASS' if ok else 'FAIL'}")
    for br, b, stated in ((1.50, 20.0, 7.5), (1.50, 1.25, 30.0), (2.60, 20.0, 13.0)):
        got = beam_envelope_cm(br, b)
        ok = abs(got - stated) < 0.1
        fail += 0 if ok else 1
        print(f"    envelope at {br:.2f} T.m, {b:5.2f} T: {got:5.2f} cm vs the stated"
              f" {stated:4.1f}   {'PASS' if ok else 'FAIL'}")

    print()
    print("  in-situ capture: the ceiling the accounting did not carry")
    ok = abs(p_for_areal(areal_for_p(265.0)) / 265.0 - 1) < 1e-6
    fail += 0 if ok else 1
    print(f"    p_for_areal inverts areal_for_p   {'PASS' if ok else 'FAIL'}")
    nowin = delivered_fraction(1.50, "fwd")
    ok = all(stopping_capture(p) < nowin for p in (150.0, 265.0, 700.0, 2000.0))
    fail += 0 if ok else 1
    print(f"    no target depth exceeds the solenoid's own acceptance"
          f" {nowin:.4f}   {'PASS' if ok else 'FAIL'}")
    ok = stopping_capture(2000.0) / nowin > 0.99
    fail += 0 if ok else 1
    print(f"    and it saturates against it: {stopping_capture(2000.0) / nowin:.4f}"
          f" at 2 GeV/c   {'PASS' if ok else 'FAIL'}")
    ok = abs(tritium_inventory_kg(265.0, 7.5) / 3.59 - 1) < 0.01
    fail += 0 if ok else 1
    print(f"    the specification's 3.59 kg reproduces:"
          f" {tritium_inventory_kg(265.0, 7.5):.2f} kg   {'PASS' if ok else 'FAIL'}")
    ok = abs(100 * insitu_heat_fraction(0.30) / 10.5 - 1) < 0.01
    fail += 0 if ok else 1
    print(f"    the specification's 10.5 percent row reproduces:"
          f" {100 * insitu_heat_fraction(0.30):.2f}   {'PASS' if ok else 'FAIL'}")
    ok = 0.90 > nowin
    fail += 0 if ok else 1
    print(f"    and its 90 percent row is above the ceiling -- UNREACHABLE, which is")
    print(f"    a correction to that table and not a rounding   {'PASS' if ok else 'FAIL'}")
    ok = abs(cell_tritium_mg(cell_r_cm=0.016) / MUFUSE_TRITIUM_MG - 1) < 0.05
    fail += 0 if ok else 1
    print(f"    the bench cell lands on MuFusE's own inventory:"
          f" {cell_tritium_mg(cell_r_cm=0.016):.2f} mg vs {MUFUSE_TRITIUM_MG}"
          f"   {'PASS' if ok else 'FAIL'}")

    print()
    print("  the capture solenoid, and the mirror term")
    base = delivered_fraction(1.50, "fwd", (0.0, 265.0))
    m = delivered_fraction_mirrored(1.50, (0.0, 265.0))
    ok = m > base
    fail += 0 if ok else 1
    print(f"    the mirror adds rather than subtracts: {base:.4f} -> {m:.4f}"
          f"   {'PASS' if ok else 'FAIL'}")
    sat = delivered_fraction_mirrored(1.50, (0.0, 265.0), b_target=10.0, b_max=100.0)
    ok = abs(sat - m) < 1e-9
    fail += 0 if ok else 1
    print(f"    and saturates: a grade of 10 returns what {MIRROR_RATIO_REQUIRED:.3f} does"
          f"   {'PASS' if ok else 'FAIL'}")
    ok = abs(MIRROR_RATIO_REQUIRED - 1.0 / math.sin(HARP_BACKWARD_EDGE_RAD) ** 2) < 1e-12
    fail += 0 if ok else 1
    print(f"    because the requirement is set by where HARP's table ends, not by")
    print(f"    the physics of the mirror   {'PASS' if ok else 'FAIL'}")
    env = beam_envelope_cm(DES_BR, DES_B_TARGET, DES_B_TARGET)
    ok = abs(env / (100 * des_bore_m()) - 1.0) < 0.01
    fail += 0 if ok else 1
    print(f"    the delivered envelope fills the designed bore: {env:.2f} cm vs"
          f" {100 * des_bore_m():.2f}   {'PASS' if ok else 'FAIL'}")
    ok = abs(DES_B_TARGET * des_bore_m() / DES_BR - 1.0) < 1e-9
    fail += 0 if ok else 1
    print(f"    and the aperture product is held while the field is dropped"
          f"   {'PASS' if ok else 'FAIL'}")
    ok = des_taper_length_m() > 10 * gyroradius_cm(pt_max(DES_BR), DES_B_TARGET) / 100.0
    fail += 0 if ok else 1
    print(f"    the taper is adiabatic against the worst orbit it must hold"
          f"   {'PASS' if ok else 'FAIL'}")

    print()
    print("  the open questions, worked")
    import mucf as _m
    lo, hi = open_band_mu_per_s()
    ceil = open_ceiling_mu_per_s()
    cm = comet_model_at_aperture()
    ok = cm < COMET_CAPTURED_LO
    fail += 0 if ok else 1
    print(f"    Q1 REFUSAL: in the hemisphere COMET captures, the model returns")
    print(f"       {cm:.4f} against its published {COMET_CAPTURED_LO:.3f}-{COMET_CAPTURED_HI:.3f}"
          f" -- BELOW it, so COMET is")
    print(f"       not a second validation and must never be quoted as one"
          f"   {'PASS' if ok else 'FAIL'}")
    ok = comet_model_at_aperture(hemisphere="fwd") > COMET_CAPTURED_LO
    fail += 0 if ok else 1
    print(f"       and the forward number does land inside it, which is how the")
    print(f"       error was made   {'PASS' if ok else 'FAIL'}")
    r1, r2 = acceptance_corroboration()
    ok = r2 == 1.0 and 0.95 < r1 < 1.0
    fail += 0 if ok else 1
    print(f"    Q1 the model has ONE validation: {mars_validation_ratio():.3f} at the")
    print(f"       configuration it is used for   {'PASS' if ok else 'FAIL'}")
    ok = all(min(_m.OMEGA_EFF_MEASURED) <= _m.omega_from_cycles(phi=p) <= _m.OMEGA_EFF_THEORY
             for p in _m.PHI_LOS_ALAMOS)
    fail += 0 if ok else 1
    print(f"    Q2 the witnessed cycle count implies a sticking inside the measured")
    print(f"       band and below theory   {'PASS' if ok else 'FAIL'}")
    ok = abs(_m.cycles(0.00515, 1.2) / 150.0 - 1) < 0.02
    fail += 0 if ok else 1
    print(f"    Q3 the 2.24 over-prediction closes at the corrected sticking"
          f"   {'PASS' if ok else 'FAIL'}")
    ok = max((_m.contamination_bound(omega_s=w, phi=1.5) or 0.0)
             for w in _m.OMEGA_EFF_MEASURED) < _m.purity_for_parity(1.5)
    fail += 0 if ok else 1
    print(f"    Q4 the 150-cycle fuel is bounded below the parity contamination"
          f"   {'PASS' if ok else 'FAIL'}")
    costs = [harp_cost_at(i) for i in range(4)]
    ok = costs[2] == min(costs) and costs[0] > costs[2]
    fail += 0 if ok else 1
    print(f"    Q6 beam energy has an optimum at 8 GeV/c and is DEARER at 3:")
    print(f"       {costs[0]:.2f} vs {costs[2]:.2f} GeV per pi-"
          f"   {'PASS' if ok else 'FAIL'}")
    ok = abs(cost_at_multiplicity(kelly_multiplicity_that_reconciles()) / kelly_cost() - 1) < 0.01
    fail += 0 if ok else 1
    print(f"    Q6 and the multiplicity that reconciles is"
          f" {kelly_multiplicity_that_reconciles():.3f}, bracketed by")
    print(f"       HARP's own {kelly_nucleons_required(1):.2f}-{kelly_nucleons_required(0):.2f}"
          f" and floored at 2 by the projectile   {'PASS' if ok else 'FAIL'}")
    ok = 1.0 < wedge_factor() < 1.10
    fail += 0 if ok else 1
    print(f"    Q7 the wedge interpolates to {wedge_factor():.4f}, inside its own bound"
          f"   {'PASS' if ok else 'FAIL'}")
    ok = open_heat_pct(lo, cycles=1.0) > 0.0
    fail += 0 if ok else 1
    print(f"    and the sign survives the floor at ONE fusion per binder:"
          f" {open_heat_pct(lo, cycles=1.0):.5f} %   {'PASS' if ok else 'FAIL'}")
    ok = len([q for q in OPEN if q[2] != "CLOSED"]) == 2
    fail += 0 if ok else 1
    print(f"    {len([q for q in OPEN if q[2] == 'CLOSED'])} of {len(OPEN)} closed;"
          f" the {len([q for q in OPEN if q[2] != 'CLOSED'])} that remain are measurements,")
    print(f"    not calculations   {'PASS' if ok else 'FAIL'}")

    print()
    print("  the species, measured off the pi+ tables")
    fp, fa = charge_fraction_produced(), charge_fraction_accepted(1.50, "fwd",
                                                                 NF_RF_WINDOW_MEV)
    ok = fp < 0.5 < fa
    fail += 0 if ok else 1
    print(f"    produced {fp:.4f} < one half < accepted {fa:.4f} -- the collector's")
    print(f"    window selects the region where pi- is the majority"
          f"   {'PASS' if ok else 'FAIL'}")
    ok = abs(fa / CHARGE_FRACTION_ASSUMED - 1) < HARP_NORM_UNCERTAINTY_PB
    fail += 0 if ok else 1
    print(f"    the halving is inside HARP's own normalisation uncertainty:"
          f" {100 * abs(fa / CHARGE_FRACTION_ASSUMED - 1):.1f}%"
          f" vs {100 * HARP_NORM_UNCERTAINTY_PB:.0f}%   {'PASS' if ok else 'FAIL'}")
    lo = charge_ratio(HARP_PB_PIMINUS_8GEV, HARP_PB_PIPLUS_8GEV, window=(0.10, 0.15))
    ok = lo > 1.0
    fail += 0 if ok else 1
    print(f"    HARP's stated lead effect reproduces: pi-/pi+ = {lo:.3f} in the")
    print(f"    100-150 MeV/c bin, above unity   {'PASS' if ok else 'FAIL'}")
    rpb = charge_ratio(HARP_PB_PIMINUS_8GEV, HARP_PB_PIPLUS_8GEV)
    ral = charge_ratio(HARP_AL_PIMINUS_8GEV, HARP_AL_PIPLUS_8GEV)
    ok = ral < rpb and charge_ratio(HARP_AL_PIMINUS_8GEV, HARP_AL_PIPLUS_8GEV,
                                    window=(0.10, 0.15)) < 1.0
    fail += 0 if ok else 1
    print(f"    and does NOT reproduce for aluminium: {ral:.3f} against lead's"
          f" {rpb:.3f}, no")
    print(f"    low-momentum excess -- the source says lower-A targets do not"
          f" show it   {'PASS' if ok else 'FAIL'}")

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
    ap.add_argument("--acceptance", action="store_true",
                    help="pi- produced -> mu- delivered, validated against MARS15")
    ap.add_argument("--magnet", action="store_true",
                    help="the capture solenoid designed, and the mirror term")
    ap.add_argument("--open", action="store_true",
                    help="every open question, and whether it can move the answer")
    ap.add_argument("--insitu", action="store_true",
                    help="the co-product configuration as an apparatus, and its ceiling")
    ap.add_argument("--species", action="store_true",
                    help="which pion the reactor buys, and what the target must be")
    ap.add_argument("--stopping", action="store_true",
                    help="the stopping window, its target size and its tritium cost")
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
    if a.acceptance:
        return report_acceptance()
    if a.magnet:
        return report_magnet()
    if getattr(a, "open"):
        return report_open()
    if a.insitu:
        return report_insitu()
    if a.species:
        return report_species()
    if a.stopping:
        return report_stopping()
    if a.floor:
        report_floor()
        return 0
    report_budget(a.target)
    return 0


if __name__ == "__main__":
    sys.exit(main())
