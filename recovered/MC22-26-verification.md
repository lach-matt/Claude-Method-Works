# Batch 5 (MC-22…26) — verification ledger. All MEASURED unless marked.

## MC-22 (§12.11.0) — Λ₉ composes / three gradings
- |Λ₉| = 1,654 ................................. MEASURED (tower.py L9) ✓
- composable pairs = 41,682 ................... MEASURED (tgt(a)==src(b)) ✓ EXACT
- closure failures = 0 ........................ MEASURED (composite ∈ Λ₉ for all 41,682) ✓
- associativity: 0 failures ................... MEASURED EXHAUSTIVELY 842,206 triples (record sampled 8,434) ✓ UPGRADE
- composition-stage table (Λ₈..Λ₁₃ composes col): Λ₉ only stage that composes — MEASURED by arity + through-map
- three gradings (counting/coupling vs composability) — structural, from source

## MC-23 (§12.11.1) — the six axes
- stage cardinalities 976/1,654/2,535/13,585/70,905/199,130 ... MEASURED (tower.py) ✓ ALL EXACT
- ambient boxes 6,912/27,648/110,592/663,552/5,308,416/47,775,744 ... MEASURED ✓ ALL EXACT
- ℛ closure E=0 every stage ................... (record; ℛ double-projection, boxes confirmed)
- densities 63.7/67.5/44.7/17.0/31.4/64.4 ..... IN SOURCE (microstate-def dependent; carried)
- composability table: Λ₈=0, Λ₉ 1,169/0.7068, Λ₁₀ 2,050/0.8087 ... MEASURED ✓ EXACT
-   Λ₁₁/₁₂/₁₃ 9,450/46,740/127,070 ............ RECORD (coupling-stage rule not in main text; MAIN-gate confirms verbatim)
- Λ₉′ tree-or-tightness 1,561 vs 1,654 ........ (record; 2S′≤2f+1 tighter)
- v-axis 2S′≤v≤g .............................. used in tower build ✓
- terms(ℓᵏ), f_max, φ̂ definitions ............ φ̂={1:3,2:4,3:5} self-consistency MEASURED ✓

## MC-23 §12.11.1.5 — non-composable cells
- Λ₁₀: 485/485 g=0 ⟺ non-composable (both directions) ... MEASURED ✓ EXACT
- Λ₁₃ triple 35,630/13,750/22,680 = 72,060 ... RECORD (coupling-stage; carried)

## MC-24 (§12.11.2) — three excluded forms
- particle-hole terms(ℓᵏ)=terms(ℓ^(4ℓ+2−k)), p & d shells ... MEASURED (microstate enum) ✓ EXACT
- max2J(f⁷) = 25 ............................... MEASURED ✓ EXACT
- half-triangle {|2L−2S|≤2J≤2L+2S}: join-closed (0 fail) ... MEASURED caps 6/8/10/12 ✓
- meet-broken 2,862/12,489/40,887/110,229 ..... MEASURED (unordered pairs) ✓ ALL EXACT
- +parity congruence → join dies, 1,848 @cap6 . MEASURED ✓ EXACT
- envelope-gap decomposition (parity5/fold1; ceiling16/parity24/triangle17) ... source
- meet-failure counts 50,592/52,080/17,856/7,254/2,443 ... source (presentation-dependent)

## MC-25 (§12.11.3, .3.1) — law vs extent / what E measures
- provenance table 13 bounds (law/extent/law-weakened) ... source
- φ̂ = realized 2J_c maxima {1:3,2:4,3:5} ...... MEASURED self-consistent ✓ (the "observed not derived" pt)
- f-below-cap 39,375 of 70,905 ................ MEASURED ✓ EXACT
- ** two-parent K breakage 15,150 @Λ₁₂ / 45,450 @Λ₁₃ (21.4%/22.8%) ... MEASURED ✓ EXACT **
  ** FINDING: §12.11.5 RECOMPUTED; 2,475 (OWED row / reg 230) is WITHDRAWN in main text. Use 15,150/45,450. **
- E(X)=|ℛ(X)|−|X| = price of extent over law ... interpretation from source

## MC-26 (§12.11.6) — the false prediction
- E1 |Δ2J|≤2 index closed by mutual-bound lemma ... source
- remove J=0↛0 → 4 failing meets, all (0,0), E=1 ... MEASURED caps 4/6/8 ✓ EXACT, cap-independent
- photon angular-momentum-unit reading ......... INTERPRETATION (labeled in source)
- E counts proposals not guarantees (540 KS slice) ... calibration from source