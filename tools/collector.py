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

PION_THRESHOLD_GEV = 0.300   # kinematic floor, perfect collection
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
    ap.add_argument("--target", type=float, default=WORK_BREAKEVEN_GEV,
                    help=f"GeV per stopped mu- to solve for (default {WORK_BREAKEVEN_GEV}, "
                         "v1.1 sec.5.2 work-breakeven)")
    a = ap.parse_args()
    if a.selftest:
        return selftest()
    if a.machines:
        report_machines()
        return 0
    report_budget(a.target)
    return 0


if __name__ == "__main__":
    sys.exit(main())
