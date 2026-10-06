# A carrier through the bulk (M-RULINGS item 88, link 2; deduced, computed and READ; verified once; not seated; 2026-10-06)

*First headed* "(M-RULINGS item 88, link 2; deduced, computed and READ; not verified; not seated; 2026-10-06)".

## What M asked

- **Item 88:** *"3 then 4 then 2 then 1 please"*. This is link 2: a carrier through the bulk (O6), measured against
  D13, which says information travels at or below c in the metric its carrier propagates in.
- **Item 89:** *"The cost is in how much information is transferred as a README (how big the file is)"*, carried as
  H-COST-IN-README.

The faithful copy's README (`faithful.py`: an identity core of order 10¹⁵ bits) has to cross from position 1 to
position 2. A carrier through the bulk moves in the bulk's metric, so D13 alone does not bound it on our plane.

Every number is printed by `carrier.py`.
- **Selftest:** 7/7 checks, 1 genuine control, with 7 STRUCTURAL lines printed and not counted. *First written* "7/7
  checks, 1 genuine control and 1 contrast, with 2 STRUCTURAL lines"; after the first verifier, "11/11 checks, 1
  genuine control and 1 contrast, with 4 STRUCTURAL lines". Each time, checks that could not fail were found and moved
  to STRUCTURAL (History).
- **Imported:** the rotor from `zeromode.py`, the identity core from `faithful.py`, and the Proxima span from
  `phase1.py` (seat's own, via settle). *First written* with 4.24 ly retyped.

## What follows the work

- **1. There is an exact test for a faster-than-light corridor, and it is Fermat's.**
  - For a static bulk, a path through the bulk beats light along the plane exactly when its optical length (the
    metric h_ij/N²) is shorter than the plane's.
  - **Evaluated on paths that leave the plane and come back:** in RS1's warp, and in a bulk with a non-trivial g_yy, no
    path is shorter (the shortest is 1.000002 of the plane's light time). With equal warps that is the theorem itself,
    since the integrand is at least 1 at every point, so it is printed as STRUCTURAL.
  - **Control:** with time and space warped differently, a returning path arrives at 0.61 of the plane's light time.
  - **The standard result, generalised from the board's own:** in a bulk with 4D Poincaré symmetry, g_ab positive
    definite and both planes at fixed y, no causal curve beats the plane's light time. `bulk.py` (2) states this for
    RS; Csáki–Erlich–Grojean state it as the equal-warp case of their eq. 1.1. *First written* as new.
  - **A shortcut needs at least one of these premises broken:**
    - the bulk's symmetry: unequal warping; a bulk that varies along the plane (which is what a *local* corridor is);
      planes in relative motion; a bulk that changes in time;
    - the plane's embedding: bent (Ishihara) or folded (the Manyfold), both already seated in `pairing.py`;
    - g_ab's signature (a second time dimension).
  - **So your corridor, if it beats light, is a place where the bulk's optical metric is shorter than the plane's along
    the route, or where the plane's embedding is not flat.**
  - *First written* "The condition for a faster-than-light corridor is now named exactly", with three escape classes,
    and "So your corridor, if it beats light, is a place where the bulk is warped unequally for time and space."
- **2. GW170817 does not bound a local corridor.**
  - Gravitons from GW170817 arrived with light: the speed difference is between −3×10⁻¹⁵ and +7×10⁻¹⁶ of c, over at
    least 26 Mpc (READ).
  - Two premises sit under that. LIGO assume the two signals were emitted together (H-SIMULTANEOUS-EMISSION). Under
    their "exotic" emission window (−100 s, 1000 s), each side widens by about two orders: +3.8×10⁻¹⁴ and −3.7×10⁻¹³.
  - What the bound constrains is the asymmetry weighted by the graviton's zero mode (CEG eq. 3.25), on the branch
    where the graviton crosses the bulk. It does not constrain the speed of a ray that dives deep, and a corridor
    confined near a device need not show.
  - CEG find faster gravitational signals to be the generic consequence of unequal warping.
  - On the Proxima line, a global asymmetry could save at most 9.4×10⁻⁸ s (H-BOUND-TRANSFERS). That is the same 7×10⁻¹⁶
    fraction as O7's 93.8 ns.
  - *First written* "A bulk warped unequally everywhere would have shown there", without the two qualifiers.
- **3. The port is where your cost lands, and it does not collapse.**

  | gravitational port (zeromode's rotor, same tip speed and density) | gravitons per mode | load time, one bit per graviton (zeromode's) | load time at the capacity ceiling g(N) |
  |---|---|---|---|
  | 1 m (500 kg each, waves at 200 Hz) | 0.026 | 5.4×10¹⁴ s | 7.9×10¹³ s (2.5 million years) |
  | 4.2 m (the fastest) | — | — | 6.7×10¹² s (213,000 years) |
  | 10 m | 2.6×10⁴ | 5.4×10⁹ s | 8.5×10¹² s |
  | 100 m | 2.6×10¹⁰ | 5.4×10⁴ s | 3.8×10¹³ s |
  | 1 km (5×10¹¹ kg each, waves at 0.2 Hz) | 2.6×10¹⁶ | 0.54 s | 2.5×10¹⁴ s (7.8 million years) |

  - The ceiling is the classical capacity of a bosonic mode, g(N) = (N+1)log₂(N+1) − N log₂N per use (Giovannetti et
    al., READ). It is taken with an ideal lossless receiver and a bandwidth of order the wave frequency
    (H-BANDWIDTH-F).
  - One bit per graviton holds only up to one graviton per mode, which is reached at an arm of 1.8 m. Below that the
    assumption undercounts (34.5 bits/s against 5.1 at 1 m). Above it, it overcounts: by 14.7 orders at 1 km, and more
    beyond.
  - **Above 4.2 m, larger rotors are slower.** At fixed tip speed the frequency falls as 1/a, while the gravitons pile
    into fewer modes. *First written* "Larger rotors are slower."
  - Under H-COST-IN-README, the README's size sets the port time. At any arm the time is proportional to the README
    (both columns), so the faithful copy's 3.5×10¹²-fold reduction is exactly the factor between loading the snapshot
    and loading the core. *First written* "the trip's cost is this port time" and "Where one bit per graviton holds".
  - *First written* with only the one-bit-per-graviton column, and "about half a second through a kilometre-scale one".

## What is ruled out, as the boundary

- **In RS1 as the board seats it, the README crosses at or below c.** RS1 keeps 4D Poincaré symmetry by construction:
  the tensions are "required in order to obtain a solution that respects four-dimensional Poincare invariance", as
  `crossing.py` READ it. Its planes also sit at fixed y. So D13 extends to bulk carriers there, and the trip takes the
  port time plus at least the light time.
- **The escape classes are the board's own open items, or shortcuts it has already seated.**
  - A bulk warped unequally needs an exotic bulk fluid to keep Newton's law on our plane (BULK3-O5), and may need NEC
    violation somewhere (BULK2-O2).
  - Gao and Wald prove that under the NEC and the null generic condition, perturbing AdS always gives a time *delay*:
    the fastest null geodesic between boundary points stays in the boundary. That suggests a shortcut needs NEC
    violation. It is not directly applicable, because an RS plane is not AdS's conformal boundary (H-GW-ANALOGY).
  - A compact bulk with moving planes needs our boost relative to the preferred frame, which is unmeasured (O7).
  - A time-dependent bulk is not modelled.
- **A gravitational port is slow at every arm computed (0.1 m to 10 km) in zeromode's rotor family.** The fastest loads
  the core in about 2×10⁵ years. *First written* "slow at any size".

## For M

- **This turns your corridor into a geometric condition that can be tested.** Its optical metric must be shorter than
  the plane's along the route (or the plane must bend or fold there), and it must be local. GW170817 constrains only a
  bulk-wide asymmetry. The board already holds three published shortcut geometries: Chung–Freese, Ishihara's bent
  plane and the Manyfold's fold. Your corridor is not without precedent.
- **The cost sits at the port, as you said, and the capacity ceiling makes that stronger.** It is set by the README's
  size and does not collapse at large rotors: about 2×10⁵ years at best through zeromode's family. A port that is not
  a rotor (the stabilisation scalar, or fields at the corridor's mouth) is the open route. Detecting single gravitons
  at the far end is unpriced.
  - *First written* "millions of years through a lab-scale gravitational emitter, about half a second through a
    kilometre-scale one".

## Named hypotheses

- **H-STATIC-WARP** (now: Poincaré-invariant slices, g_ab positive definite, planes at fixed y); **H-RS1** (carried);
  **H-BOUND-TRANSFERS**; **H-SIMULTANEOUS-EMISSION** (LIGO's).
- **H-BIT-PER-GRAVITON** (zeromode's; valid only up to one graviton per mode); **H-BANDWIDTH-F**; **H-GW-ANALOGY**.
- **M's:** H-COST-IN-README, H-ADDRESS-INPUT, H-INFORMATION-CROSSES.

## Sources READ (alphaXiv, open arXiv copies; read this pass, after the verifier read them too)

| source | used |
|---|---|
| LIGO–Virgo, Fermi-GBM, INTEGRAL, 1710.05834v2 | the speed bound (abstract p.1; eq. 1, p.6, D = 26 Mpc); "emitted simultaneously" and the exotic window (−100 s, 1000 s), "2 orders of magnitude broadening" (p.6); the 1.74 ± 0.05 s delay (p.1) |
| Csáki, Erlich, Grojean, hep-th/0012143v3 | eq. 1.1 (p.1); "globally violates 4D Lorentz invariance" (p.2); Fermat and "no discrepancy" when c(r) decreases (p.16); speed depends on E/\|p\| (p.19); eq. 3.25, ≥ 0 (p.21); μ and Q "could be severly constrained" (p.23) |
| Giovannetti, Guha, Lloyd, Maccone, Shapiro, Yuen, quant-ph/0308012v2 | g(x) and C (eq. 4, p.1); the single-mode capacity (eq. 14, p.3) |
| Gao, Wald, gr-qc/0007021v2 | Theorem 2 (pp.12–13); "always produce a time delay" (abstract) |
| Randall–Sundrum (via `crossing.py`'s READ) | the 4D Poincaré invariance the tensions are required for |

## OPEN

1. A corridor geometry that breaks C1's premises locally, with its energy conditions (with BULK2-O2, BULK3-O5; Gao–Wald
   as suggestive).
2. A time-dependent bulk.
3. A port faster than gravitational emission: the stabilisation scalar (BULK3-O3), or the planes' own fields at the
   corridor's mouth.
4. Reception: detecting single gravitons. A 0.2 Hz graviton carries 1.3×10⁻³⁴ J, against kT = 4.1×10⁻²¹ J at 300 K.
   *First listed* as "One bit per graviton, at sending and at receiving".
5. In a bulk that keeps C1's premises, the trip takes the port time plus at least the light time.

## History (verifier, 2026-10-06; first-written claims kept above, each where it stood)

- **C1's random-curve check could not fail.** Each step took dy and the fastest dx for it, so dx/dt = √(1−u²)
  whatever the warp. RS1 and the second metric both printed 0.876005, and the curves never returned to the plane. It
  is now STRUCTURAL ("the identity, evaluated"). The counted test is Fermat's, on returning paths. The sympy line is
  a string match and is now STRUCTURAL.
- **"A two-dimensional warp"** had one extra coordinate. It is now "a bulk with a non-trivial g_yy".
- **C1 was presented as new.** It is `bulk.py` (2) generalised, and a standard result (CEG).
- **The escape list was not exhaustive.** The bent and folded planes, a bulk varying along the plane, and a second time
  dimension were missing. "Named exactly" was an overclaim.
- **The port's 0.54 s at 1 km is not physical.** One bit per graviton fails at 2.6×10¹⁶ gravitons per mode. The g(N)
  ceiling is now computed.
- **C3** now names H-SIMULTANEOUS-EMISSION and the exotic window, carries the zero-mode and bulk-branch qualifiers, and
  pins LIGO's rounding (1.74 s over the light time is 6.5×10⁻¹⁶, printed as 7×10⁻¹⁶) instead of a 1 s tolerance.
- **The Proxima span** is imported, not retyped.
- **Gao–Wald** is cited at BULK2-O2 and OPEN 1.
- **Second pass (uses.py's verifier):** the two equal-warp Fermat checks could not fail for any equal-warp input; the C3
  Proxima line and the C4 linearity contrast recomputed their own formulas. All four are now STRUCTURAL. "Larger
  rotors are slower" now starts at 4.2 m; "up to 14 orders" is 14.7 at 1 km; "slow at any size" is scoped to the arms
  computed; the port time is said to be set by the README's size rather than to be M's cost.
