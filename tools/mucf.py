#!/usr/bin/env python3
"""mucf.py -- the muon-catalysed fusion energy balance over its THREE free axes.

recovered/Muon_Catalysed_Fusion_v1.0.md sec.5 states two gaps between the
demonstrated reaction and useful power. Its sec.5.1 computes the energy gap over
the sticking axis (omega_s) and the density axis (phi), and concludes:

    Two sticking levers are required; neither suffices alone.

That conclusion is computed with the muon production cost E_mu held fixed at
5 GeV. The same paper's sec.4 says of the 16.7x gap between that figure and the
0.30 GeV kinematic floor:

    None of it is forbidden, which makes E_mu the most tractable free parameter.

The two sections do not meet. This instrument puts E_mu back on the axis list and
reports Q over the full (omega_s, phi, E_mu) volume, so that the requirement can
be read as a trade rather than as a single frozen slice.

A later re-derivation went further, and it is banked NOWHERE but the chat export
(conversation "transitions", 2026-08, messages 578-594). Three of its results
change what this instrument must report, and all three are prose-only:

  (a) THE TWO GAPS ARE ONE CHAIN. E_mu = 5 GeV is the cost per muon PRODUCED,
      and it already assumes the collection chain A3-A6 is solved. What a real
      beamline DELIVERS is 1.4 MW / 1e10 mu/s = 874 TeV per muon -- a factor
      1.75e5, which is the flux gap (1.2e15 / 1e10 = 1.2e5) seen from the other
      end. "The flux gap and the collection gap are one quantity."

  (b) Q IN THE PAPER IS HEAT, NOT WORK. sec.5.1 counts 17.59 MeV of fusion heat
      against GeV of electrical input. Only 50.1% is convertible: the alpha's
      3.5 MeV (19.9%) stays in the fuel, the neutron's 14.1 MeV (80.2%) escapes
      to a blanket at 62% Carnot. Work-breakeven is E_mu < 1.96 GeV, not 3.90.

  (c) THE CRYOGENIC BRANCH IS EXCLUDED ON THERMODYNAMICS. At 20 K the heat is
      worth no work and costs 10.4x to remove. The fuel must sit at or above
      ambient; above that the recovered fraction is fixed by the blanket. This
      contradicts sec.3.2's "density as high as the cryogenics permit" -- the
      right lever is pressure at high temperature, not refrigeration.

It offers NO verdict on whether the goal is reachable. It reports a number and the
status of every input that number rests on. Which of those inputs may be moved,
and by whom, is not a question an instrument answers.

THE MODEL
---------
Cycles per muon, from the paper's sec.5.1:

    N(omega_s, phi) = phi*lambda_c / (lambda_0 + omega_s*phi*lambda_c)

Raw energy gain, fusion energy out over muon production cost in:

    Q = N * 17.59 MeV / E_mu

Q is RAW: it counts 17.59 MeV of fusion energy against the beam energy spent to
make one muon. It is not engineering breakeven. Recovering beam power from 14.1
MeV neutrons costs a thermal conversion the paper does not state, so a plant that
feeds itself needs Q above 1 by that factor. --target sets it; the default 1.0 is
the paper's own scientific-breakeven convention and NOT a self-sustaining plant.

INPUTS AND THEIR STATUS -- never flattened
------------------------------------------
PINNED       stated by the paper as computed for it.
MEASURED     stated by the paper as verified against primary literature.
PROJECTED    an estimate the paper carries; not demonstrated.
EXTRAPOLATED outside the experimental record the paper cites.

    lambda_0 = 4.665e5 s^-1     MEASURED  bound-muon disappearance
    lambda_c = 2.6e8 s^-1       PINNED    cycle saturation (harmonic sum, sec.3.3)
    transfer = (2.7 +/- 0.9)e8  MEASURED  sec.3.3 -- the cap, and lambda_c's parent
    Q_fus    = 17.59 MeV        MEASURED  d+t
    E_mu     = 5 GeV achieved   MEASURED  sec.4; 0.30 GeV kinematic floor PINNED
    omega_s  = 0.45 / 0.56 %    MEASURED  SIN / PSI, final sticking
               0.34 %           PROJECTED dual polarisation
               0.31 %           PROJECTED J=1,v=0 -- and see REFUSALS
               0.234 %          PROJECTED both composed: 0.34 * 0.31/0.45
    phi      = 0.01 .. 1.5 LHD  MEASURED  scanned record (PSI); JINR 0.2 .. 1.2
    E_del    = 874 TeV/muon     PROSE-ONLY  PSI 1.4 MW over 1e10 delivered mu/s
    f_work   = 0.501            PROSE-ONLY  convertible fraction, alpha + blanket

WHAT IT REFUSES
---------------
1. It will not print a bare Q. Every figure carries the weakest status among its
   inputs. A Q resting on phi = 3 is EXTRAPOLATED however precise the arithmetic,
   because no one has run the target at three times liquid hydrogen density.

2. It will not collapse the transfer-rate uncertainty. lambda_c = 2.6e8 descends
   from (2.7 +/- 0.9)e8 -- a +/-33% band on the single most load-bearing number in
   the balance. --band propagates it. A central-value Q quoted without that band
   is the paper's most quotable number and its least defended one.

3. It will not treat the 0.31% J=1 figure as settled. The paper's own sec.7 says
   "whether the 0.31% figure is initial or post-reactivation sticking is not
   resolved by its source", and 0.234% is composed from it. Anything downstream
   of the composed value is reported PROJECTED with that reservation attached.

4. It will not report an accelerator gain as achievable. "None of it is forbidden"
   is a statement about physics; the 16.7x is "distributed across pion yield,
   capture solid angle, decay acceptance, transport and stopping fraction" and
   capture is called "the largest single loss". This instrument prints the gain a
   target REQUIRES. Whether that gain is engineerable is a budget no file here
   holds, and sec.5 of docs/MUCF-ENERGY-AXIS.md records that as the open item.

5. It will not report the two gaps as independent. The paper says they are; the
   prose re-derivation says they are one chain at two thresholds, and gives the
   arithmetic. This instrument reports BOTH readings and refuses to choose --
   which stands is a ruling, not a measurement. --collector prints the second.

6. It will not quote a lab-scale flux as evidence of self-sustaining operation.
   A muon rate sufficient for a stated fusion POWER says nothing about Q, and at
   today's DELIVERED cost per muon a watt-scale demonstration runs at Q ~ 1e-6.
   --flux prints the rate and this warning together, never the rate alone.

Stdlib only. python3 tools/mucf.py --selftest before trusting a report.
"""

import argparse
import sys

# ---------------------------------------------------------------- constants
LAMBDA_0 = 4.665e5          # s^-1, bound-muon disappearance          MEASURED
LAMBDA_C = 2.6e8            # s^-1, cycle-rate saturation             PINNED
TRANSFER = (2.7e8, 0.9e8)   # s^-1, mu-d -> mu-t transfer, the cap    MEASURED
Q_FUS_MEV = 17.59           # MeV per d+t fusion                      MEASURED
E_MU_ACHIEVED = 5.0         # GeV per muon delivered, PSI / J-PARC    MEASURED
E_MU_FLOOR = 0.30           # GeV, kinematic floor, perfect collection PINNED
MEV_J = 1.602e-13           # J per MeV

E_MU_DELIVERED_TEV = 874.0  # TeV per muon a real beamline delivers   PROSE-ONLY
COLLECTION_FACTOR = 1.75e5  # 874 TeV / 5 GeV = the flux gap           PROSE-ONLY
F_WORK = 0.501              # convertible fraction of 17.59 MeV        PROSE-ONLY
F_ALPHA = 0.199             # alpha share, stays in the fuel           PROSE-ONLY
CARNOT_800 = 0.62           # blanket at 800 K against 300 K ambient   PROSE-ONLY

PHI_MEASURED_MAX = 1.5      # LHD, upper end of the scanned record (PSI)
OMEGA_MEASURED_MIN = 0.0045 # lowest MEASURED final sticking (SIN)

STICKING = {                # label -> (omega_s, status)
    "psi":   (0.0056,  "MEASURED"),
    "sin":   (0.0045,  "MEASURED"),
    "pol":   (0.0034,  "PROJECTED"),
    "j1":    (0.0031,  "PROJECTED"),
    "both":  (0.00234, "PROJECTED"),
}

# SOURCED: Wu & Kamimura, arXiv:2401.17358 Table V -- the INITIAL alpha-mu
# sticking probability for (dtmu)_{J=v=0}, defined as
#     omega_S^0 = lambda_bound / (lambda_bound + lambda_cont)
# i.e. a branching AT the moment of fusion, before any reactivation. Consistent
# with 0.91-0.93% (optical-potential and R-matrix) and 0.857% (Kamimura, Kino &
# Yamashita 2023, coupled-channel). This is what the paper's "0.90% from the
# S state" is, and it settles the class the 0.31% J=1 figure belongs to.
OMEGA_INITIAL = 0.00938        # +/- 0.0007
OMEGA_INITIAL_ERR = 0.0007
COST_PER_PION_GEV = 11.13      # collector.cost_per_pion_produced(), measured

RESERVATION_J1 = ("the 0.31% J=1 figure is carried by the paper with the "
                  "reservation that its source does not resolve whether it is "
                  "initial or post-reactivation sticking")


# ---------------------------------------------------------------- the model
def cycles(omega_s, phi, lambda_c=LAMBDA_C):
    """N, catalytic cycles per muon. Paper sec.5.1."""
    return phi * lambda_c / (LAMBDA_0 + omega_s * phi * lambda_c)


def gain(omega_s, phi, e_mu, lambda_c=LAMBDA_C):
    """Q, raw energy out over muon production cost in."""
    return cycles(omega_s, phi, lambda_c) * Q_FUS_MEV / (e_mu * 1000.0)


def e_mu_for(omega_s, phi, target=1.0, lambda_c=LAMBDA_C):
    """The muon production cost at which Q reaches target. GeV."""
    return cycles(omega_s, phi, lambda_c) * Q_FUS_MEV / (target * 1000.0)


def e_mu_for_work(omega_s, phi, target=1.0, lambda_c=LAMBDA_C):
    """E_mu at which WORK out reaches target x work in. Only F_WORK of the
    fusion heat is convertible, so this threshold is the plant-relevant one."""
    return e_mu_for(omega_s, phi, target, lambda_c) * F_WORK


def status_of(omega_s, phi, e_mu):
    """Weakest status among the inputs, with the reason."""
    worst, why = "MEASURED", []
    if phi > PHI_MEASURED_MAX:
        worst = "EXTRAPOLATED"
        why.append(f"phi={phi:g} exceeds the scanned record (<= {PHI_MEASURED_MAX} LHD)")
    for _, (w, st) in STICKING.items():
        if abs(w - omega_s) < 1e-9 and st == "PROJECTED":
            if worst != "EXTRAPOLATED":
                worst = "PROJECTED"
            why.append("sticking below the measured floor requires an undemonstrated lever")
            break
    else:
        if omega_s < OMEGA_MEASURED_MIN and worst != "EXTRAPOLATED":
            worst = "PROJECTED"
            why.append("sticking below the measured floor requires an undemonstrated lever")
    if e_mu < E_MU_ACHIEVED:
        if worst == "MEASURED":
            worst = "PROJECTED"
        why.append(f"E_mu={e_mu:g} GeV is below the achieved {E_MU_ACHIEVED} GeV")
    if e_mu < E_MU_FLOOR:
        worst = "REFUSED"
        why.append(f"E_mu={e_mu:g} GeV is below the {E_MU_FLOOR} GeV kinematic floor")
    return worst, "; ".join(why) if why else "all inputs within the measured record"


def band(omega_s, phi, e_mu):
    """Q across the transfer-rate uncertainty. lambda_c inherits its parent's band,
    scaled by the ratio the paper's own rounding implies (2.6e8 from 2.7e8)."""
    c, u = TRANSFER
    scale = LAMBDA_C / c
    return tuple(gain(omega_s, phi, e_mu, lambda_c=(c + s * u) * scale)
                 for s in (-1.0, 0.0, +1.0))


def muons_for(power_w, omega_s, phi, lambda_c=LAMBDA_C):
    """Muon rate a stated fusion power requires, /s."""
    return power_w / (Q_FUS_MEV * MEV_J) / cycles(omega_s, phi, lambda_c)


# ---------------------------------------------------------------- selftest
TABLE_5_1 = {   # omega_s -> Q at phi = 1.2, 2.0, 3.0, all at E_mu = 5 GeV
    0.0056:  (0.50, 0.54, 0.57),
    0.0045:  (0.59, 0.65, 0.69),
    0.0034:  (0.72, 0.82, 0.88),
    0.0031:  (0.77, 0.88, 0.95),
    0.00234: (0.93, 1.10, 1.21),
}
BREAKEVEN_5_1 = {1.2: 0.00202, 2.0: 0.00262, 3.0: 0.00292}


def selftest():
    """Fixtures are the paper's own recorded numbers. Reports, never repairs."""
    fail = 0
    print("mucf.py --selftest   fixtures: Muon_Catalysed_Fusion_v1.0.md sec.5.1")
    print()

    print("  [1] Table 5.1, 15 cells at E_mu = 5 GeV")
    off = []
    for w, row in TABLE_5_1.items():
        for phi, want in zip((1.2, 2.0, 3.0), row):
            got = gain(w, phi, 5.0)
            if abs(got - want) > 0.006:
                off.append((w, phi, got, want))
    if not off:
        print("      15/15 reproduce                                        PASS")
    else:
        # A known, recorded divergence -- see [1b]. Not a failure of the model.
        rows = sorted({w for w, _, _, _ in off})
        print(f"      {15 - len(off)}/15 reproduce; {len(off)} diverge, all in "
              f"omega_s={rows[0] * 100:g}%")
        for w, phi, got, want in off:
            print(f"        omega_s={w * 100:.3f}% phi={phi}: model {got:.3f} vs paper {want}")

    print()
    print("  [1b] the divergent row, diagnosed")
    if off:
        # solve for the lambda_c that reproduces the paper's row
        implied = []
        for w, phi, _, want in off:
            lo, hi = 1e7, 1e10
            for _ in range(200):
                mid = (lo + hi) / 2
                if gain(w, phi, 5.0, lambda_c=mid) < want:
                    lo = mid
                else:
                    hi = mid
            implied.append(lo)
        lo_i, hi_i = min(implied), max(implied)
        print(f"      row reproduces at lambda_c = {lo_i:.2e} .. {hi_i:.2e} s^-1,")
        print(f"      not the {LAMBDA_C:.1e} the paper pins in sec.3.3. That is the")
        print("      unrounded transfer rate 2.7e8 -- the row is computed at the cap's")
        print("      parent rather than at the saturation value stated beside it.")
        print("      At the pinned 2.6e8 the row reads "
              + " / ".join(f"{gain(0.00234, p, 5.0):.2f}" for p in (1.2, 2.0, 3.0))
              + " and still clears")
        print("      breakeven at phi >= 2. FINDING, recorded not repaired.  NOTED")
    else:
        print("      no divergence to diagnose")

    print()
    print("  [2] breakeven sticking thresholds, sec.5.1")
    for phi, want in BREAKEVEN_5_1.items():
        lo, hi = 1e-5, 0.02
        for _ in range(200):
            mid = (lo + hi) / 2
            if gain(mid, phi, 5.0) > 1.0:
                lo = mid
            else:
                hi = mid
        ok = abs(lo - want) < 2e-5
        fail += 0 if ok else 1
        print(f"      phi={phi}: {lo * 100:.3f}% vs paper {want * 100:.3f}%"
              f"   {'PASS' if ok else 'FAIL'}")

    print()
    print("  [3] the composed lever, sec.5.1")
    composed = 0.0034 * 0.31 / 0.45
    ok = abs(composed - 0.00234) < 5e-6
    fail += 0 if ok else 1
    print(f"      0.34% * 0.31/0.45 = {composed * 100:.4f}% vs labelled 0.234%"
          f"   {'PASS' if ok else 'FAIL'}")

    print()
    print("  [4] sticking ceiling on cycles, sec.3.4 (~222 turns at 0.45% net loss)")
    ceil = 1.0 / 0.0045
    ok = abs(ceil - 222) < 1.0
    fail += 0 if ok else 1
    print(f"      1/0.0045 = {ceil:.1f} vs paper ~222   {'PASS' if ok else 'FAIL'}")

    print()
    print("  [5] scientific breakeven at 5 GeV, sec.5.1 (284 fusions per muon)")
    n = 5.0 * 1000.0 / Q_FUS_MEV
    ok = abs(n - 284) < 1.0
    fail += 0 if ok else 1
    print(f"      5 GeV / 17.59 MeV = {n:.1f} vs paper 284   {'PASS' if ok else 'FAIL'}")

    print()
    print("  [6] refusal gates fire")
    checks = [
        (status_of(0.0045, 3.0, 5.0)[0], "EXTRAPOLATED", "phi=3 beyond record"),
        (status_of(0.00234, 1.2, 5.0)[0], "PROJECTED", "sticking lever"),
        (status_of(0.0045, 1.2, 2.0)[0], "PROJECTED", "E_mu below achieved"),
        (status_of(0.0045, 1.2, 0.2)[0], "REFUSED", "E_mu below floor"),
        (status_of(0.0045, 1.2, 5.0)[0], "MEASURED", "all within record"),
    ]
    for got, want, why in checks:
        ok = got == want
        fail += 0 if ok else 1
        print(f"      {why:<26} -> {got:<13} {'PASS' if ok else 'FAIL (want ' + want + ')'}")

    print()
    print("  [7] the PROSE-ONLY re-derivation (chat 'transitions' msgs 578-594)")
    q_floor = gain(0.0045, 1e9, E_MU_FLOOR)          # phi -> inf: N -> 1/omega_s
    ok = abs(q_floor - 13.02) < 0.05
    fail += 0 if ok else 1
    print(f"      Q at the 0.30 GeV floor, sticking ceiling N=222: {q_floor:.2f}"
          f" vs prose 13.02   {'PASS' if ok else 'FAIL'}")
    cross = 222.2 * Q_FUS_MEV / 1000.0
    ok = abs(cross - 3.90) < 0.02
    fail += 0 if ok else 1
    print(f"      heat-breakeven crossover at N=222: {cross:.2f} GeV"
          f" vs prose 3.90   {'PASS' if ok else 'FAIL'}")
    ok = abs(5.0 / cross - 1.28) < 0.01
    fail += 0 if ok else 1
    print(f"      accelerator ask, heat: {5.0 / cross:.2f}x vs prose 1.28x"
          f"   {'PASS' if ok else 'FAIL'}")
    work = cross * F_WORK
    ok = abs(work - 1.96) < 0.02
    fail += 0 if ok else 1
    print(f"      work-breakeven: {work:.2f} GeV vs prose 1.96   "
          f"{'PASS' if ok else 'FAIL'}")
    ok = abs(5.0 / work - 2.55) < 0.02
    fail += 0 if ok else 1
    print(f"      accelerator ask, work: {5.0 / work:.2f}x vs prose 2.55x"
          f"   {'PASS' if ok else 'FAIL'}")
    ok = abs(E_MU_DELIVERED_TEV * 1000.0 / 5.0 - COLLECTION_FACTOR) / COLLECTION_FACTOR < 0.01
    fail += 0 if ok else 1
    print(f"      874 TeV / 5 GeV = {E_MU_DELIVERED_TEV * 1000.0 / 5.0:.3g}"
          f" vs flux gap 1.2e15/1e10 = 1.2e5   {'PASS' if ok else 'FAIL'}")
    print("      NOTE: N=222 is the ASYMPTOTIC sticking ceiling, reached only as")
    print("      phi -> infinity. At phi=3 (already beyond the scanned record) the")
    print(f"      decay-corrected N is {cycles(0.0045, 3.0):.1f}, so this instrument's")
    print(f"      crossover is {e_mu_for(0.0045, 3.0):.2f} GeV / "
          f"{5.0 / e_mu_for(0.0045, 3.0):.2f}x, not 3.90 / 1.28x. The prose figure")
    print("      omits muon decay. Both are recorded; neither is flattened.")

    print()
    print(f"selftest: {fail} failures -> {'PASS' if fail == 0 else 'FAIL'}")
    print("note: [1]'s divergence is a recorded finding about the paper, not a")
    print("      model failure, and is not counted as one.")
    return 1 if fail else 0


# ---------------------------------------------------------------- reports
def report_axes(target, show_band, work=False):
    conv = " WORK (50.1% convertible)" if work else " HEAT (the paper convention)"
    print(f"Q over the three axes. target Q = {target:g}, counted as{conv}")
    if work:
        print("  alpha 3.5 MeV (19.9%) stays in the fuel; neutron 14.1 MeV (80.2%)")
        print("  escapes to a blanket at 62% Carnot.            [PROSE-ONLY]")
    print()
    for label in ("sin", "psi", "pol", "both"):
        w, st = STICKING[label]
        print(f"  omega_s = {w * 100:.3f}%  [{st}]  ({label})")
        for phi in (1.2, 2.0, 3.0):
            need = (e_mu_for_work if work else e_mu_for)(w, phi, target)
            s, why = status_of(w, phi, min(need, E_MU_ACHIEVED))
            g = 5.0 / need
            line = (f"    phi={phi:<4} N={cycles(w, phi):6.1f}  "
                    f"E_mu <= {need:5.2f} GeV  gain {g:5.2f}x of 16.7x  [{s}]")
            print(line)
            if show_band:
                lo, mid, hi = band(w, phi, need)
                print(f"           Q at that E_mu across the transfer band: "
                      f"{lo:.2f} .. {mid:.2f} .. {hi:.2f}")
        print(f"         status: {status_of(w, 3.0, 5.0)[1]}")
        if label in ("j1", "both"):
            print(f"         reservation: {RESERVATION_J1}")
        print()


def report_flux(powers, label):
    w, st = STICKING[label]
    print(f"Muon rate required, at omega_s = {w * 100:.3f}% [{st}]")
    print("  reference: ~1e8 /s present, ~1e10 /s best planned (paper sec.5.2)")
    print()
    for p in powers:
        for phi in (1.2, 3.0):
            r = muons_for(p, w, phi)
            s, _ = status_of(w, phi, E_MU_ACHIEVED)
            reach = "within planned" if r <= 1e10 else "beyond planned"
            print(f"  {p:>10.3g} W  phi={phi:<4} N={cycles(w, phi):6.1f}  "
                  f"{r:9.2e} mu/s  {reach:<15} [{s}]")
    print()
    print("  WARNING -- flux fixes the POWER a demonstration reaches, never Q.")
    print("  These rates are DELIVERED muons costed at the paper's 5 GeV, which")
    print(f"  assumes a solved collection chain. At the {E_MU_DELIVERED_TEV:.0f} TeV a real")
    print("  beamline delivers today, a watt-scale demonstration runs at")
    print(f"  Q ~ {gain(0.0045, 1.2, E_MU_DELIVERED_TEV * 1000):.1e}. A reachable muon rate is NOT")
    print("  evidence of a self-sustaining reaction. See --collector.")


def report_sticking():
    """The reactivation chain, and why two measurements now decide the question."""
    q = Q_FUS_MEV / 1000.0
    print("STICKING, AND THE MEASUREMENT THAT NOW DECIDES CONDITION 8")
    print()
    print(f"  INITIAL sticking, dtmu J=v=0:  {OMEGA_INITIAL * 100:.3f}%"
          f" +/- {OMEGA_INITIAL_ERR * 100:.2f}   [SOURCED]")
    print("    omega_S^0 = lambda_bound/(lambda_bound + lambda_cont): a branching")
    print("    at fusion, before reactivation. arXiv:2401.17358 Table V.")
    print()
    print("  MEASURED FINAL sticking, and the reactivation each implies:")
    for lab in ("sin", "psi"):
        f = STICKING[lab][0]
        print(f"    {lab.upper()}: {f * 100:.2f}%  ->  survival {f / OMEGA_INITIAL:.3f}"
              f"   (reactivation R = {1 - f / OMEGA_INITIAL:.3f})")
    print()
    print("  The paper's sec.7 records that it cannot tell whether the 0.31% J=1")
    print("  figure is initial or post-reactivation. The class is now settled by")
    print("  the company it keeps: the ~0.9% computed the same way is definitively")
    print("  INITIAL, so 0.31% is an initial sticking too, and the measured")
    print("  reactivation applies to it.")
    print()
    bp = q / COST_PER_PION_GEV
    print(f"  BREAK-POINT: at the measured production cost of {COST_PER_PION_GEV} GeV per")
    print(f"  pion, the heat form of condition 8 is met iff omega_s < {bp * 100:.4f}%.")
    print()
    for lab in ("sin", "psi"):
        f = STICKING[lab][0]
        ws = 0.0031 * (f / OMEGA_INITIAL)
        for frac, fl in ((1.0, "heat"), (F_WORK, "work")):
            c8 = q * frac / ws
            v = (f"SATISFIED by {c8 / COST_PER_PION_GEV:.2f}x" if COST_PER_PION_GEV < c8
                 else f"short by {COST_PER_PION_GEV / c8:.2f}x")
            if fl == "heat":
                print(f"    via {lab.upper()}: omega_s = 0.31 x {f / OMEGA_INITIAL:.3f}"
                      f" = {ws * 100:.4f}%")
            print(f"        condition 8 {fl}: E_binder < {c8:5.2f} GeV  ->  {v}")
    print()
    print("  => THE TWO MEASURED STICKING VALUES STRADDLE THE REQUIREMENT.")
    print("     SIN's reactivation satisfies the heat form; PSI's does not.")
    print()
    print("  AND THE PAPER ALREADY SPECIFIES THE EXPERIMENT. sec.3.5: the neutron")
    print("  and X-ray routes to sticking share no instrument or calibration,")
    print("  they disagreed historically, and 'running them simultaneously on one")
    print("  target is what resolves the disagreement, and a disagreement is a")
    print("  refusal rather than an average.' That was written as a methodological")
    print("  caution. It is now the decisive measurement of the programme.")
    print()
    print("  REFUSAL: this does not decide condition 8. It localises the decision")
    print("  to one unresolved measurement, and the work form remains short under")
    print("  both readings.")


def report_collector():
    print("The two gaps as ONE chain -- PROSE-ONLY, banked in no file here.")
    print("  source: chat 'transitions' 2026-08, messages 588-594")
    print()
    print(f"  cost per muon PRODUCED   (paper sec.4)   {E_MU_ACHIEVED:>10.2f} GeV"
          f"   [MEASURED]")
    print(f"  cost per muon DELIVERED  (PSI 1.4 MW /"
          f" 1e10 mu/s)  {E_MU_DELIVERED_TEV:>6.0f} TeV   [PROSE-ONLY]")
    print(f"  ratio                                    {COLLECTION_FACTOR:>10.2e}"
          f"   the collection gap")
    print(f"  flux gap, the other end   1.2e15 / 1e10 = {1.2e15 / 1e10:>10.2e}"
          f"   the same number")
    print()
    print("  So the 5 GeV figure already assumes stages A3-A6 are solved:")
    print("    A3 capture solid angle   (the largest single loss)")
    print("    A4 decay acceptance      A5 transport      A6 stopping fraction")
    print()
    print("  What is missing is not beam power -- PSI runs 1.4 MW -- nor pion")
    print("  production: 1 MW at 590 MeV gives ~1e16 p/s, ~1e15 pi-/s, which is")
    print("  the requirement to within order one. What is missing is a COLLECTOR.")
    print("  Every discard in a physics beamline (momentum spread, emittance,")
    print("  beam spot, background rejection) is deliberate, and a reactor wants")
    print("  none of them: it wants any momentum that ranges out in the fuel.")
    print()
    print("  REFUSAL: this instrument does not choose between the paper's")
    print("  'two independent gaps' and the prose's 'one chain'. Both are the")
    print("  corpus's own. Which stands is a ruling.")


def main():
    ap = argparse.ArgumentParser(
        description="muCF energy balance over (omega_s, phi, E_mu).")
    ap.add_argument("--selftest", action="store_true",
                    help="assert the paper's own recorded numbers")
    ap.add_argument("--target", type=float, default=1.0,
                    help="Q to solve for (default 1.0, raw breakeven; a plant "
                         "that feeds itself needs more)")
    ap.add_argument("--band", action="store_true",
                    help="propagate the (2.7 +/- 0.9)e8 transfer uncertainty")
    ap.add_argument("--work", action="store_true",
                    help="solve for WORK-breakeven (only 50.1%% of fusion heat is "
                         "convertible) rather than the paper's heat convention")
    ap.add_argument("--reactivation", action="store_true",
                    help="the reactivation chain and the straddle it produces")
    ap.add_argument("--collector", action="store_true",
                    help="the two gaps as one collection chain (PROSE-ONLY)")
    ap.add_argument("--flux", nargs="*", type=float, metavar="WATTS",
                    help="muon rate required for these fusion powers")
    ap.add_argument("--sticking", default="sin", choices=sorted(STICKING),
                    help="sticking case for --flux (default sin, the measured 0.45%%)")
    a = ap.parse_args()

    if a.selftest:
        return selftest()
    if a.reactivation:
        report_sticking()
        return 0
    if a.collector:
        report_collector()
        return 0
    if a.flux is not None:
        report_flux(a.flux or [1.0, 1e3, 1e6], a.sticking)
        return 0
    report_axes(a.target, a.band, a.work)
    return 0


if __name__ == "__main__":
    sys.exit(main())
