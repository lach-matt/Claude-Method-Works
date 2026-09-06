# Batch 4 verification ledger (measured, chat 60)

All against Λ₈ rebuilt from lam8.py (976 cells), coords (n,ℓ,k,q,e,f,g,2S).

## MC-17 §12.1 (orientable/cylinder)
- Constraint graph is a tree (MC-21 confirms: no cycle, chain length 17, 17 join-irreducibles).
  Bipartite sign structure ⇒ no odd reversal is structural; both Möbius routes close by construction.
  [No standalone numeric; anchored on the tree fact and box=cylinder from MC-18.]  MEASURED downstream.

## MC-18 §12.6.1 (two-body separation)  — MEASURED
- bare product |A|·|B|·|q| = 33·17·4 = 2,244.
- conditioned: Σ_q |A(q)|·|B(q)| = 165+330+345+136 = 976 exact.
  A(q)=33,33,23,8 ; B(q)=5,10,15,17.

## MC-19 §12.7 (fibres closed form)  — MEASURED
- A_q(1) = 33,33,23,8 ; B_q(1) = 5,10,15,17  (closed forms reproduce enumeration at every q).

## MC-20 §12.8 (cross-sections)  — MEASURED
- peak fibre 345 at q=2 = 35.3% of 976 ; sequence 165,330,345,136 log-concave ⇒ unimodal.
- ⟨q⟩ = 1.4631, sd 0.930.
- 8→3 compression: 3-variable count S(1,1,1) = 976.
- every A_q and B_q closed (meet/join) with E=0 — all 8 slices, all q. Local E=0 is a new invariant.

## MC-21 §12.9 (interval-is-box; antichains; chains; absent shape)  — MEASURED
- interval-is-box EXACT = 31,604 / 115,162 comparable intervals = 27.4% (book "27%"); 72.6% carry active constraints.
- widest antichain = 122 at rank 11 ; Λ = 8 × 122 = 976 ; 18 rank levels.
- maximal chains e(P) = 1,113,045,672 (saturated bottom→top DP; exact match to record).
- chain length 17 = 17 join-irreducibles (the "two seventeens are one").
- constraint graph is a tree: no Möbius, no cycle, no non-planar minor.
- NOTE (reconstruction, not defect): the §12.9 per-constraint binding rates (g≤q 35.6%, q≤k 33.0%,
  g≤4f+2 4.9%) did not reproduce to the decimal on my "binds across [x,y]" definition over all
  comparable pairs (got 32.6 / 34.1 / 3.8%). Definitional basis differs (book measured over "random
  intervals"). Per standing ruling the finding is about the reconstruction; the ranking
  (coupling most active > q≤k > Pauli least) reproduces. MC-21 authored on the exact numbers;
  binding rates represented as the record states them, cited to §12.9.