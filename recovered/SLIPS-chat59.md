# SLIPS — chat 59 (await Register 1.1 numbering, with slips 05–12, B1/B2/B3-C*)

## MC-13 — `L.comb` (the language combinations)  [INSERTED, approved]
- Object: new Math-Compendium entry `L.comb`, placed between `L.closed` and `L.def` (alphabetical).
- Binds main §11.2 token [MC-13] → `L.comb`. OWED-EXPANSIONS-2 row 13 → DONE.
- grade COMPUTED · depth 11 · deps L.arith, L.closed, L.rankpoly, L.void, L.pal, L.chi, L.bits.
- Verified (lam8.py + exhaustive over 6,912-box / 475,800 pairs): all ten combinations hold —
  gcd/lcm=meet/join 0-fail; mean rank 11.0666; box−Λ=void 5,936; F not palindromic ⟺ not self-dual
  (5-vs-4 tail witness); ℛ(Λ)=Λ⇒E=0; A=7 rows×2 non-zeros; χ selects 976; F coeff-fn is χ, F(1)=976,
  F(−1)=2; log₂976=9.93; polytope integer points = Λ.
- Guard: measured-diff clean — 0 removed, 10 added, all in the L.comb block; 6 BUILD59 discriminators
  unchanged (==1); L.comb heading ==1.
- Compendia state after insert: md5 778d5dce4de1961cc744f60bafcc7c94, 32,461 lines
  (was 2ad6eae4b896b3198ca975b4286ac96b, 32,451).
- Open note for M: combination-5 source cell (§11.2 order+information) is line-wrapped in raw .md;
  rendering confirmed faithful to recoverable tokens (ℛ(Λ)=Λ⇒E=0); not logged as a defect pending PDF.
