# What a faithful copy must carry (M-RULINGS items 86–89; READ, deduced and computed; verified once; SEATED, ledger section 8n, M-D68-89; 2026-10-06)

*Headed before seating* "(M-RULINGS items 86–88; READ, deduced and computed; verified once; not seated; 2026-10-06)".

*First headed* "(M-RULINGS items 86–88; READ, deduced and computed; not verified; not seated; 2026-10-06)".

## What M asked

- **Item 86, answer 7:** *"information... Consider it a to be like a software update patch presented as a README file
  telling position to what to construct with what it has."* Answer 8: *"if the original matter did not travel with it,
  it would not be the same but rather a copy/clone".*
- **Item 87:** the goal is *"A faithful copy"*.
- **Item 88:** *"3 then 4 then 2 then 1 please"*. This is link 3, what "faithful" needs (S1B-O1, H-WHICH-COUNT), and it
  comes first.

M's hypotheses are carried as hypotheses, never as results.

Every number is printed by `faithful.py`.
- **Selftest:** 11/11 checks, 2 genuine controls and 2 contrasts, with 4 STRUCTURAL lines printed and not counted.
  *First written* "9/9 checks, 2 genuine controls and 1 contrast". One "control" could not fail (History).
- **Snapshot counts:** imported from `measure.py`, never retyped.

## What follows the work

- **1. A faithful classical copy needs far less than any snapshot of the body.**
  - The board's four counts describe the body at an instant: 9.5e27 to 1.1e29 bits.
  - Part of what a snapshot fixes is the positions of freely diffusing molecules. Bulk water at body temperature
    scrambles a 1 Å placement in a time of order picoseconds (5.5e-13 s by d²/6D) and drifts about 0.135 mm in a
    second. A destination at 37 °C supplies its own; no README could fix those positions anyway.
  - **Not covered:** concentrations in compartments (ion gradients, membrane potentials). They are macrostate, and the
    recipe must fix them.
  - The board's thermal-entropy count (2.84e28 bits, CONDITIONAL) is the microstate a body-temperature destination
    supplies for itself. It neither bounds the README nor is subtracted from it.
  - *First written* "the bulk of its atoms" (not READ) and "what the copy may leave out".
- **2. What carries identity is classical, so a classical README loses none of it.**
  - Neuron firing decoheres in 10⁻²⁰ to 10⁻¹⁹ s, against dynamics of 10⁻³ to 10⁻¹ s (Tegmark, Table 1, p.8).
  - This holds under his identity-theory premise (p.11), carried as H-IDENTITY-IN-DYNAMICS, and the uncontested firing
    margin.
  - His microtubule figure is disputed: Hagan et al. recompute it at 10⁻⁵ to 10⁻¹ s (verifier-READ). But they agree a
    superposition of firing is unlikely.
  - Tegmark's p.8 argument covers the rest: if firing patterns are perceptions, consciousness "cannot be of a quantum
    nature even if there is a yet undiscovered physical process … with a very long decoherence time".
  - *First written* without the dispute.
- **3. The identity core, sized** (CONDITIONAL; an order-of-magnitude estimate, neither floor nor ceiling).

  | quantity | bits |
  |---|---|
  | one synapse, each neuron's inputs listed in order (36.3 for the partner + 4.70 for the strength) | 41.0 |
  | one synapse, inputs coded as an unordered set (k ≈ 7,000 synapses per neuron, computed from Shapson-Coe) | 29.7 |
  | one mm³ of cortex at 41 bits (133.7 million synapses) | 5.49e9 |
  | the electron-microscope read of that mm³ (1.4 PB) | 1.12e16 (2.0e6 × larger) |
  | a cortex of 5e5 mm³ (H-GREY-VOLUME, unread) | 2.7e15 |
  | the genome, diploid, 2 bits per base (CHM13 omits Y) | 1.2e10 |
  | the board's snapshot counts | 3.5e12 to 4.0e13 × the core |

  The named inputs pull in opposite directions:
  - the address coding is an upper side;
  - Bartol's 26 strengths are "a minimum", measured in rat hippocampus (H-STRENGTH-TRANSFERS), so a lower side;
  - the cerebral cortex holds only 19 % of the brain's neurons (Azevedo), and the cerebellum and subcortex are outside
    the figure;
  - omitted state (synapse position, morphology, glia, molecular and electrical state) is a lower side;
  - the density comes from one temporal-lobe sample (H-DENSITY-TYPICAL).

  *First written* "a floor of the identity layer".
- **4. The README is the part the destination cannot rebuild for itself.**
  - Computed: a megabyte made by a known rule is rebuilt exactly from its 32-byte seed, and zlib cannot shrink it at
    all.
  - Control: one flipped bit in the seed changes half the output bits, so the exactness comes from the seed.
  - **The README is as small as the builder's knowledge makes it** (H-REGENERABLE).
  - Construction information that need not carry identity (neuron morphology, axon routing) could be comparable to the
    core in size. It is OPEN unless the builder chooses the layout.
- **5. What crosses needs no quantum resources.**
  - No entanglement, no two-bits-per-qubit teleportation overhead, and no years-long quantum memory: S1C-O6 goes silent
    on this path.
  - A classical README can wait without decohering.
  - Every channel shortfall the board prices in bits falls by the same factor as the count, 3.5e12 or more.
- **6. For the identity layer the read need not resolve atoms.**
  - Synapses were read in sections of about 30 nm, a candidate narrowing of S1C-O1.
  - The only read demonstrated at that resolution destroys the tissue.
- **7. No-cloning does not bind a classical copy.**
  - Computed: a CNOT copier copies |0⟩ and |1⟩ exactly and fails on |+⟩, where each output has fidelity ½. That this
    copier fails is computed; that every copier fails is no-cloning, READ.
  - Replication is perfect "if and only if a basis to which ψ belongs is known" (Scarani p.2), and a README fixes the
    basis.
  - **H-RETIRE-A's stated reason** (item 32: "to satisfy the no-cloning clause") **does not apply to a classical
    README.** The no-cloning theorem no longer requires the original to be retired, under H-IDENTITY-IN-DYNAMICS.
    Other grounds are not examined.
  - The gain is in principle, since the only read demonstrated at this resolution destroys the tissue.
  - *First written* "physics no longer requires the original to be retired".
- **8. It bears on two open items.**
  - **H-WHICH-COUNT (S1B-O1).** The README size is a fifth quantity, not one of the four counts. It singles none of
    them out, and your ruling at item 33 ("Keep all four") stands. You ruled (item 89): *"Add as fifth reading"*. The
    identity core is now H-WHICH-COUNT's fifth reading.
  - **BULK3-O1 and crossing.py's D3** asked whether the defining information is classical or quantum. Point 2 answers
    "classical" for the identity layer, conditionally.

## What is ruled out, as the boundary

- A classical README cannot carry an unknown quantum state. No operation copies one, and a single copy cannot be
  measured (Scarani p.3).
- The README shrinks only by what the builder already knows. A builder that knows nothing receives the snapshot.
- The copy is faithful at the instant of the read. Afterwards copy and original diverge: neural updates "may have to
  involve some classical randomness" (Tegmark p.11).

## For M

- **Your README picture holds up in a sharp form.** The cortical wiring core alone is of order 10¹⁵ bits, under named
  premises, against 10²⁸ for a snapshot. The recipe, the brain outside the cortex, and acquired body state are not
  priced.
  - *First written* "What crosses is the identity core plus a recipe. It is of order 10¹⁵ bits".
- **It fits your other answers.**
  - The core is relative wiring with no coordinates. The README says *what*; the device's input (answer 4) says
    *where*.
  - A classical README can wait, so on this path the hold need not be brief (answer 5).
- **The original.** With a classical copy, the no-cloning theorem no longer requires the original to be retired, and
  that was H-RETIRE-A's reason. You ruled (item 89): *"Leave it open"*. H-RETIRE-A stays carried with both readings.
- **H-WHICH-COUNT.** You ruled (item 89): *"Add as fifth reading"*.
- *First written* as two questions for you; both are now ruled.

## Named hypotheses

- **H-IDENTITY-IN-DYNAMICS** (Tegmark's premise); **H-WIRING-SUFFICES**; **H-ADDRESS-UNIFORM** (an upper side).
- **H-STRENGTH-TRANSFERS**, **H-DENSITY-TYPICAL** and **H-GREY-VOLUME** (5e5 mm³, NAMED-NOT-READ).
- **H-BULK-WATER**; **H-REGENERABLE** (load-bearing, not shown for a body); **H-DIPLOID**.
- **M's:** H-README, H-SAME-NEEDS-MATTER, H-RETIRE-A.

## Sources READ

| source | route | used |
|---|---|---|
| Tegmark, quant-ph/9907009v2 | alphaXiv | decoherence vs dynamics (pp.1, 8); the p.8 argument; identity premise and randomness (p.11) |
| Hagan, Hameroff, Tuszynski, quant-ph/0005025v1 | verifier-READ | microtubule margin disputed (p.1); firing superpositions unlikely (p.2) |
| Scarani et al., quant-ph/0511088v1 | alphaXiv | no-cloning (p.3); the basis condition, DNA, footnote 2 (p.2); teleportation destroys the original (p.30) |
| Bartol et al., eLife 2015 | Firecrawl, open | 26 strengths as "a minimum", 4.7 bits; rat CA1; title "upper bound on the variability" |
| Shapson-Coe et al., bioRxiv 2021.05.29.446289v4 | Firecrawl, open | 1 mm³, ~30 nm, 57,216 cells, 133.7 M synapses, 1.4 PB, glia 2:1, automated segmentation |
| Azevedo et al., J. Comp. Neurol. 2009 | research index; verifier-READ (Europe PMC) | 86.1 ± 8.1 billion neurons; 19 % in the cerebral cortex |
| Nurk et al., Science 2022 | verifier-READ abstract | 3.055 Gbp, T2T-CHM13, all chromosomes except Y |
| Holz et al., PCCP 2000, via Dietrich's compilation | Firecrawl, SECONDARY | water D at 35 and 40 °C |

## OPEN

1. The brain outside the cortex, and acquired body state (immune memory, scars, the microbiome, bone shape).
2. A builder that rebuilds a body from a recipe (H-REGENERABLE; with S1C-O2); construction information.
3. A non-destructive read at synapse resolution.
4. Whether H-WIRING-SUFFICES holds: what else of the brain's state identity needs.
5. A READ whole-brain synapse total, and human strength levels.

## History (verifier, 2026-10-06; first-written claims kept above, each where it stood)

- **"A floor of the identity layer"** became an estimate whose inputs pull both ways.
- **Bartol's rat-CA1 scope** and the **cortex-only scope** are now named.
- **The F4 random-data arm** was labelled CONTROL and cannot fail. It is now a contrast, and a seed-flip control was
  added.
- **"Physics no longer requires the original to be retired"** became "no-cloning no longer requires it".
- **Tegmark's microtubule margin** is now shown disputed (Hagan et al.).
- **H-WHICH-COUNT and BULK3-O1** are now tied in.
- **F3's regime, scope and the meaning of the thermal count** are corrected.
- **The Nurk quote** is replaced with the printed abstract. It was first quoted from a search index's summary.
- **"For M"** no longer prices the recipe as part of the 10¹⁵.
