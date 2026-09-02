---
type: "path"
date: "2026-09-02T14:35:18.565643+00:00"
question: "What is the exact relationship between The Ground-State Derivation and The Janet Collapse?"
contributor: "graphify"
outcome: "corrected"
correction: "The graph labelled this edge conceptually_related_to / AMBIGUOUS. The source is stronger and explicit: math.pdf p.81 states Q.collapse 'depends on S.ground, Q.bound'. The correct relation is a declared dependency (S.ground -> Q.collapse), confidence EXTRACTED, because the p=0 collapse condition is only readable from the ground configuration."
source_nodes: ["The Ground-State Derivation", "The Janet Collapse", "Orbital Collapse", "The Three Exceptions - La, Ac, Th", "The Channel Equation", "Family Q The Channel Equation", "The Pauli Bound"]
---

# Q: What is the exact relationship between The Ground-State Derivation and The Janet Collapse?

## Answer

The ground-state derivation (S.ground, math.pdf p.27) and the Janet collapse (Q.collapse, math.pdf p.81) are joined by a DECLARED DEPENDENCY, not a loose conceptual link. Q.collapse's own header reads "depends on S.ground, Q.bound", depth 8.

Mechanism: orbital collapse is defined for a channel with p = 0 at l >= 2. The p = 0 condition (no penetrating core electrons) is readable only from the ground configuration, which is exactly what S.ground supplies ("the ground configuration determines every channel's existence and bounds its defect's integer part", grade MEASURED, 5 objects depend on it). So Q.collapse cannot be evaluated without S.ground as input.

Measurement: three exact coincidences between a Janet filling-order block boundary and a physical orbital collapse. n+l=5 block opens at Z=21 and 3d collapses at 21; n+l=7 opens at 57 and 4f at 57; n+l=8 opens at 89 and 5f at 89. Across 116 p=0 channels at l=2 or 3: collapsed median defect 0.637, uncollapsed 0.036, U-test p=9.8e-4. Adding the term takes Ti IV nd from -0.620 to -0.056 and overall rms from 0.1825 to 0.1411.

Cross-document reuse: the same collapse physics derives the three periodic-table exceptions La, Ac, Th in THE-LOWDIN-SOLUTION.pdf section VI.1 ("Orbital collapse and the three exceptions"), where at La, Ac and Th the f channel is still outer-well and the d channel is selected. Those elements sit at Z = 57, 89, 90 - on the same block boundaries. One mechanism does two jobs: it corrects the channel equation Q.final in the compendium, and it explains the periodic table's anomalies in the standalone paper.

Chain context: math.pdf p.89 prints the longest derivation path in the register, depth 14, and S.ground sits on it: A.alph <- A.env <- A.R <- K.redun <- K.axis <- K.produce <- S.ground <- S.ritz <- S.regime <- Q.alpha <- Q.pol <- Q.delta <- Q.region <- Q.anchor <- Q.final.

## Outcome

- Signal: corrected
- Correction: The graph labelled this edge conceptually_related_to / AMBIGUOUS. The source is stronger and explicit: math.pdf p.81 states Q.collapse 'depends on S.ground, Q.bound'. The correct relation is a declared dependency (S.ground -> Q.collapse), confidence EXTRACTED, because the p=0 collapse condition is only readable from the ground configuration.

## Source Nodes

- The Ground-State Derivation
- The Janet Collapse
- Orbital Collapse
- The Three Exceptions - La, Ac, Th
- The Channel Equation
- Family Q The Channel Equation
- The Pauli Bound