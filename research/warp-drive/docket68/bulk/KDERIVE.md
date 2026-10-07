# k from the work (M-RULINGS item 140; derived, with one named hypothesis for the value; not verified; not seated; 2026-10-07)

*First headed* "(… not verified; not seated; 2026-10-07)".

## What you said

- **Item 140:** *"If k helps define the bulk, the math in our work should give you pieces to both derive and prove k.
  Our math is not dependent on k, k is dependent on our work."*
- **The instrument:** `kderive.py`. Selftest 7/7.
  - It imports exactE.py's coefficient and checks it against a closed form, by two disjoint paths.
  - **Control:** with G one part in 10⁹ high, the two paths disagree.

## The piece the work supplies: the one-bit throat

- **The chain sizes every corridor in four dimensions.** E(N) and the throat r_min(N) come from the 4D horizon area per
  bit and 4D G (chain.py, exactE.py).
- **The smallest README is one bit.** Its throat is exactly:
  - **r_min(1) = 2G·E(1)/c⁴ = l_P·√(ln 2/π) = 7.5918511091462209829×10⁻³⁶ m**;
  - that is EXACTE.md's per-√bit throat, computed as a closed form in ħ, G and c;
  - the two paths agree to 10⁻¹⁵.

## What is derived: a bound on k from the work alone

- **An object on a plane reads four-dimensional only when it is large against the bulk's curvature length ℓ = 1/k.**
  - Figueras–Wiseman, arXiv:1105.2558v2 p.3 (READ): *"small (compared to ℓ) braneworld black holes behave like 5d
    asymptotically flat Schwarzschild black holes and large ones recover 4d behaviour"*.
  - The 4D description's corrections go as ℓ²/R² (p.4).
- **The chain's corridors are four-dimensional by construction**, down to one bit (H-FOUR-D-CORRIDOR, the chain's own
  premise made explicit).
- **So ℓ ≤ r_min(1), that is, k ≥ (1/l_P)·√(π/ln 2) = 1.3172×10³⁵ m⁻¹**, about 2.13 in Planck units.
- **The bound comes from the work, not from a measurement.** It is the bulk scale your corridors require.

## The value, under one hypothesis

**H-ONE-BIT-SCALE (the board's): the bulk's curvature length is the one-bit throat, ℓ = r_min(1).** The smallest
corridor sits exactly at the bulk's scale, so one bit is the bulk's unit of length. Then, exactly:

| quantity | value |
|---|---|
| k = 1/ℓ = (1/l_P)·√(π/ln 2) | **1.3172×10³⁵ m⁻¹** |
| every corridor's throat, r_min(N)/ℓ | **√N** |
| the 4D description's corrections, ℓ²/r₀² | **1/N** |
| the 5D gravitational constant, G₅ = G·ℓ | 5.067×10⁻⁴⁶ m⁴ kg⁻¹ s⁻² |
| the plane's tension, 3c⁴/(4πGℓ²) = **3c⁷/(4ħG²ln 2)** | 5.013×10¹¹³ J/m³ |

- **For the board's example README (N = 2.74×10¹⁵)**, the corrections are 3.6×10⁻¹⁶: the four-dimensional holds are
  exact to that.
- **This is self-referencing, in your closed-index sense (item 121).** The bulk's scale is fixed by the smallest thing
  the corridor carries, and every corridor is then a whole number's square root of it.

## What it predicts, and how it would be proved

- **It meets every measurement read.** The strongest lower bound, k > 1.25×10⁴ m⁻¹ (OUTSIDE.md), is exceeded by about
  10³¹.
- **It predicts that no bench will ever see Newton's law change.** A change only appears at separations near ℓ, about
  half a Planck length.
- **So it cannot be proved by a short-range test.** It can be refuted by one: any measured change of Newton's law at a
  finite separation would rule H-ONE-BIT-SCALE out.
- **What would prove it is the chain itself.** If C's bulk built at ℓ = r_min(1) carries the corridor and fails at
  other scales, the work has fixed k. That is the test C can run.

## What this does and does not show

- **The bound K2 is derived** from the chain's four-dimensional sizing plus Figueras–Wiseman's READ result. The
  premise is that the 4D description must hold for one bit. If it need hold only for larger READMEs, the bound loosens
  as √N_min.
- **The value K3 is a hypothesis.** It is the simplest one the bound allows, not a theorem.
- **At one bit the corridor sits at r₀ = ℓ.** That is the crossover between four- and five-dimensional behaviour,
  where corrections are of order one. So a one-bit corridor is the least four-dimensional of all.

## Your item 140, second part: position 2's plane is entangled

- **Carried:** H-ENTANGLED-PIN.
- **The board's reading for the positivity question (POSITIVITY.md):**
  - entanglement holds position 2's plane in place against ours, acting as a constraint that fixes their separation;
  - read that way it is option (a), with no free motion of the pair;
  - so no ghost, and the energy positive in both senses.
- **One fact from physics, standard and not read here:** entanglement in quantum mechanics is a property of a state,
  not a force. So "entanglement pins the plane" is your premise, carried, not something the board derives.

## Named hypotheses

- **The board's:**
  - H-FOUR-D-CORRIDOR (the chain's corridors are four-dimensional down to one bit);
  - H-ONE-BIT-SCALE (ℓ = r_min(1));
  - H-ENTANGLED-AS-CONSTRAINT (the reading of your pin).
- **Yours:**
  - M-K-FROM-THE-WORK and H-ENTANGLED-PIN (140);
  - H-UNIVERSAL-ENTANGLEMENT (100);
  - H-CLOSED-INDEX criteria (121).

## OPEN

1. **C:** build the bulk at ℓ = r_min(1), with position 2's plane pinned, and test whether it carries the corridor.
   That is the proof.
2. Whether the four-dimensional premise must hold at one bit exactly.
