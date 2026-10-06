# What a faithful copy must carry (M-RULINGS items 86–88; READ, deduced and computed; not verified; not seated; 2026-10-06)

## What M asked

- **Item 86, answer 7:** *"information... Consider it a to be like a software update patch presented as a README file
  telling position to what to construct with what it has."* Answer 8: *"if the original matter did not travel with it,
  it would not be the same but rather a copy/clone".*
- **Item 87:** the goal is *"A faithful copy"*.
- **Item 88:** *"3 then 4 then 2 then 1 please"*. This is link 3, what "faithful" needs, and it comes first.

M's hypotheses are carried as hypotheses, never as results.

Every number is printed by `faithful.py`.
- **Selftest:** 9/9 checks, 2 genuine controls and 1 contrast, with 4 STRUCTURAL lines printed and not counted.
- **Snapshot counts:** imported from `measure.py`, never retyped.

## What follows the work

- **1. A faithful classical copy needs far less than any snapshot of the body.**
  - The board's four counts describe the body at an instant: 9.5e27 to 1.1e29 bits (`measure.py`).
  - Most of that is thermal microstate. Water at body temperature forgets a 1 Å placement in 5.5e-13 s and drifts
    about 0.13 mm in a second. The destination regenerates its own by being at 37 °C, so the README need not carry it,
    and no README could fix it for longer than picoseconds.
  - The board's thermal-entropy count (2.8e28 bits, CONDITIONAL) measures what the copy may leave out, not what it
    must carry.
- **2. What carries identity is classical, so a classical README loses none of it.**
  - Tegmark computes brain decoherence times of 10⁻²⁰ to 10⁻¹³ s, against dynamical times of 10⁻³ to 10⁻¹ s.
    "Fall squarely in the classical category, by a margin exceeding ten orders of magnitude" (p.8).
  - This holds under his stated premise that consciousness is "synonymous with certain brain processes" (p.11),
    carried here as H-IDENTITY-IN-DYNAMICS.
- **3. The identity core, sized** (CONDITIONAL on the named premises). Each synapse costs about 41 bits:
  - 36.3 bits to name its partner among 86.1 billion neurons (Azevedo);
  - 4.70 bits for one of 26 distinguishable strengths (Bartol).

  | quantity | bits |
  |---|---|
  | one synapse | 41.0 |
  | one mm³ of cortex (133.7 million synapses, Shapson-Coe) | 5.49e9 |
  | the electron-microscope read of that mm³ (1.4 PB) | 1.12e16 (2.0e6 × larger) |
  | a cortex of 5e5 mm³ (H-GREY-VOLUME, unread) | 2.7e15 |
  | the genome, diploid, 2 bits per base | 1.2e10 |
  | the board's smallest snapshot count (species sequence) | 9.5e27 (3.5e12 × the core) |

  - The core is a floor of the identity layer, not a whole specification.
- **4. The README is the part the destination cannot rebuild for itself.**
  - Computed: a megabyte made by a known rule is rebuilt exactly from its 32-byte seed. zlib cannot shrink that same
    megabyte at all.
  - Control: data with no rule the builder knows does not shrink either.
  - **The README is as small as the builder's knowledge makes it** (H-REGENERABLE).
- **5. For the identity layer the read need not resolve atoms.**
  - Synapses were read in sections of about 30 nm.
  - That narrows S1C-O1 (an atom-resolving read) for this layer, under H-WIRING-SUFFICES.
  - The read that exists destroys the tissue.
- **6. No-cloning does not bind a classical copy.**
  - Computed: a CNOT copier copies |0⟩ and |1⟩ exactly and fails on |+⟩, where each output has fidelity ½.
  - Classical encodings "can be replicated perfectly" (Scarani p.2), so the copy does not require destroying the
    original.
  - **H-RETIRE-A's stated reason** (item 32: "to satisfy the no-cloning clause") **does not apply to a classical
    README.** Whether the original is retired becomes a choice for M, not a requirement of physics.

## What is ruled out, as the boundary

- A classical README cannot carry an unknown quantum state. No operation copies one, and a single copy cannot be
  measured (Scarani p.3).
- The README shrinks only by what the builder already knows. A builder that knows nothing receives the snapshot.

## For M

- **Your README picture holds up in a sharp form.** What crosses is the identity core plus a recipe. It is of order
  10¹⁵ bits, under named premises, against 10²⁸ for a snapshot.
- **The copy can be faithful in everything that carries identity.** At body temperature identity is classical, under
  the identity-theory premise.
- **One question your ruling opens:** with a classical copy, physics no longer requires the original to be retired.
  H-RETIRE-A's reason was no-cloning, so whether the original stays is now yours to decide.

## Named hypotheses

- **H-IDENTITY-IN-DYNAMICS** (Tegmark's premise); **H-WIRING-SUFFICES**; **H-ADDRESS-UNIFORM** (an upper side for the
  wiring).
- **H-GREY-VOLUME** (5e5 mm³, NAMED-NOT-READ; whole-brain figures are CONDITIONAL on it); **H-REGENERABLE**
  (load-bearing, not shown for a body); **H-DIPLOID**.
- **M's:** H-README, H-SAME-NEEDS-MATTER, H-RETIRE-A.

## Sources READ

| source | route | used |
|---|---|---|
| Tegmark, quant-ph/9907009v2 | alphaXiv | decoherence vs dynamical times (pp.1, 8); identity premise (p.11) |
| Scarani et al., quant-ph/0511088v1 | alphaXiv | no-cloning (p.3); classical encodings replicate (p.2); teleportation destroys the original (p.30) |
| Bartol et al., eLife 2015 | Firecrawl, open | 26 strengths, 4.7 bits per synapse |
| Shapson-Coe et al., bioRxiv 2021.05.29.446289v4 | Firecrawl, open | 1 mm³, ~30 nm sections, 133.7 M synapses, 1.4 PB |
| Azevedo et al., J. Comp. Neurol. 2009 | Firecrawl research index, abstract | 86.1 ± 8.1 billion neurons |
| Nurk et al., Science 2022 | Firecrawl research index, abstract | 3.055 Gbp |
| Holz et al., PCCP 2000, via Dietrich's compilation | Firecrawl, SECONDARY | water D at 35 and 40 °C |

## OPEN

1. Acquired body state outside the brain's wiring (immune memory, scars, the microbiome, bone shape).
2. A builder that rebuilds a body from a recipe (H-REGENERABLE; with S1C-O2, placement).
3. A non-destructive read at synapse resolution.
4. Whether H-WIRING-SUFFICES holds: what else of the brain's state identity needs.
5. A READ whole-brain synapse total, to replace H-GREY-VOLUME.
