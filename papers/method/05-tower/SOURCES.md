# SOURCES.md — provenance map for 05-tower (not published)

Paper: `PAPER.md`, "The Tower over Λ: from Eight Coordinates to Thirteen". Drafted 2026-09-21; resumed and finished 2026-09-24 after the first run was cut off by a service limit; **repaired 2026-09-24 against `AUDIT.md`** (the repair record is at the end of that file, and the section "What the repair changed" below records every departure from the source it introduced).
Every number in the paper is produced by `check.py` or is CITED. `check.py` imports the seated
tower instrument `method/members/tower-2.py`, the constraint-graph instrument
`method/proofs/cgraph.py`, the triangle instrument `method/proofs/coupling.py` and the Z3 harness
`research/warp-drive/prover.py` **by path**; it copies none of them. The reference implementations
used by the two guards are written fresh inside `check.py`.

## Where each section draws from

All paths are under `/home/user/Claude-Method-Works/`.

| paper section | source passages |
|---|---|
| Thesis, §0, Abstract | `method/members/The_Method_1_6-2.md` §12.11 through §12.11.5 (lines 2309–3513), especially §12.11.0.10's one-table summary of the tower (cells, E, ambient box, fill, new coordinate, bounding rule, grading), §12.11.3's dichotomy, and §12.11.5's cylinder-and-boundary paragraph; `method/members/The_Method_1_6___The_Index_of_Indices-2.md` §II lines 38–61 (the stage table) and 1432–1440 (the tower entry: "the price of an axis … cycle rank, composability, exactness, and the point at which the tree becomes a graph") |
| §1 D1–D2, D6 (box, sublattice, ℛ, E) | main volume §6.1 lines 1537–1549 (Âᵢ, φ̂ᵢⱼ, ℛ(X), E(X) = \|ℛ(X)\| − \|X\|); §7.2–§7.3 lines 1769–1793 (every constraint is xᵢ ≤ φ(xⱼ) with φ non-decreasing; the closure proof); Appendix A.2 (cited at line 9983, proved in §14.1) |
| §1 D9–D11 (the thirteen coordinates, their bounds, the caps) | `method/members/tower-2.py` (the object under test: the coordinate order `n ℓ k q e f g 2S \| 2S′ v 2J_c 2K 2J`, `PHI = {1:3, 2:4, 3:5}`, `FMAX = 1`, and the six stage constructors); main volume §7.1 lines 1755–1768 (the seven constraints and their four origins); §7.4 lines 1794–1812 (the standing cap convention `(n_max, e_max, ℓ_max, k_max, f_max) = (3,3,1,3,1)`); §12.11.1's axis table and §12.11.3.1's provenance table (lines 3055–3070, 3190–3215) |
| §1 D12, §3 (terms, σ, μ, φ̂) | main volume §12.11.1's vocabulary block (`terms(ℓᵏ)` by microstate enumeration; `f_max` the cap; `φ̂` the monotone envelope and its collision with §6.1's φ̂ᵢⱼ); §12.11.2 (the three excluded forms: reflection, congruence, triangle); §12.11.0.6 (the earlier bound 2J_c ≤ k excludes physical states at every occupancy; φ̂ equals the realised maxima at every k); Mathematical Compendium §IV.T lines 1672–1840 (Racah 1943 seniority, the parent bound, the recoupling bound, the spin-half bound — each with its prior-art attribution) |
| §1 D13, §9 (envelope steps, seed) | main volume §14.5.8 lines 3830–3836 (the tower's seeds 7, 9, 9 "under greedy set cover" and the sentence "Λ₉ and Λ₁₀ seed identically" — the claim that does not reproduce, see below) and register 511 (the same figures "under set cover"); §14.5.9 lines 3922–3960 ("elements are the envelope steps, sets are the cells, a cell covers the steps it witnesses"; seed(Λ₈) = 7 exactly by branch and bound; the spread across heuristics); §14.5.10 lines 3962–4000 (the 102 elements = envelope steps plus alphabet values; no cell is forced); Mathematical Compendium K "Constraint tightness as a count" (Deville, Barette & Van Hentenryck 1999 — read, not used, since the paper's Lemma 3 is proved directly) |
| §1 D14, §6 (the cylinder) | main volume §12.6–§12.8.5 lines 2380–2470 (the two ends, the transfer, the section table 33×5 / 33×10 / 23×15 / 8×17, Σ_q \|A(q)\|·\|B(q)\| = 976, the Pareto frontier, log-concavity, ⟨q⟩); §12.11.5 (the sections at Λ₁₁ and Λ₁₃, the tight two-parent K and its 15,150 / 45,450 defect); §12.1 lines 2312–2326 (the bipartite sign structure and orientability) |
| §2 | main volume §12.11.0.10's table; §12.11.1's "Every stage closed exhaustively" table (the ℛ sweep over 6,912 … 47,775,744 ambient cells); §12.10.1 lines 3016–3035 (Λ₈/Λ₉ side by side: cells, box, E, rank levels, log-concavity) |
| §4 | Appendix A.15 lines 10160–10175 ("Two bands, and only one of them is a sublattice": B_k a sublattice for fixed k, C = {\|a−b\| ≤ c} join-closed and not; 12,654 failing meets at cap 8; "a bound by a constant is monotone in both directions, a bound by a free coordinate is not"; and the sentence the first draft's thesis turned on — "What the tower relies on at axis 13 is B₁, which is a sublattice and is the reason the last coupling step is carried exactly" — **which the paper no longer carries**: see "What the repair changed", item 1); Appendix A.18 lines 10177–10190 (the triangle region: the join proof in full and the two meet witnesses (0,1,1)∧(1,0,1) and (4,0,4)∧(2,2,0)); Appendix A.14, A.16, A.17 are cross-referenced at lines 9983–9989 to §12.11.2 and §12.11.3 and are read there; Appendix A.11 (a difference is not a lattice homomorphism, so ν is inadmissible as an axis) |
| §5 | `method/proofs/cgraph.py` (imported by path: `EDGES_BY_STAGE`, `graph`, `components`, `triangles`, `girth`, `treewidth`); `method/members/kparent.py` (the correction, see below); main volume §7.2's figure 7.1 caption (eight nodes, seven edges, a tree, treewidth 1); §12.7.1 (the two caterpillars glued at k–q); Mathematical Compendium's Freuder 1982 entry, line 376–384 |
| §6.1 | main volume §12.11.3.1 (dimension 12 is "law, weakened": the law is 2K ≤ 2J_c + 2f with the cell's own f, which has two parents; the construction substitutes f_max); §12.11.5 (the tight K breaks the factorisation by 15,150 at Λ₁₂ and 45,450 at Λ₁₃, 21.4% and 22.8%); Mathematical Compendium "The tower" and "The tree or the tightness" entries (the exact triangle at axis 12 gives 22,275 cells and E = 35,570) |
| §7 | main volume §8.3 lines 1852–1870 (seventeen join-irreducibles, twenty covering relations, all 976 down-sets); Appendix A.19 and A.19.0 lines 10192–10230 (the seventeen written out; "every generator is the least cell with one coordinate at one value", Σᵢ(\|Aᵢ\|−1) = 17; the twenty implications split nine within a coordinate and eleven between); §12.9 lines 2985–3005 (eighteen rank levels, widest 122 at rank 11, Λ exactly eight times its widest level, e(P) = 1,113,045,672) |
| §8 | Mathematical Compendium K, "The tower's two ends joined" lines ~2140–2150 (the gap-free interval with monotone endpoints at every consecutive stage; the directed system of brackets; the composition containing the direct bracket with slack ≤ 2 rank units; the projection covering ranks 3 through 20; branching 4, 4, 6, 8, 9) |
| §10 References | Mathematical Compendium §IV.T and §IV.K prior-art blocks, which name Racah 1942/1943, Condon & Shortley 1935, Wigner 1931, Pauli 1925, Birkhoff 1937, Freuder 1978/1982, Dechter & Pearl 1989, Mac Lane 1971, Green 1953 and Helly 1923. The paper cites only those it uses, plus Davey & Priestley, Grätzer, Stanley, Robertson & Seymour, Karp, Cowan and de Moura & Bjørner, which are the paper's own additions for the lattice-theoretic, graph-theoretic, set-cover and solver material. |

## The correction the paper applies

`method/members/kparent.py` records, and `check.py` reproduces, that the main volume defines
`f_max` inside §12.11.1's own vocabulary block as **the cap on f under §7.4, not the cell's own f**,
and states there that the bound `2K ≤ 2J_c + 2f_max` **has one parent**; and that two other sites
read the same bound with the cell's own `f` and so give K two parents. `cgraph.py`'s
`EDGES_BY_STAGE[12]` carries the two-parent edge list `[("2Jc","2K"), ("f","2K")]`, and its
`PRINTED_1790` accordingly records 13 nodes, **14** edges and cycle rank `(0,0,1,1,2,2)`.

**The correction is applied.** `check.py` substitutes the one-parent edge list into the imported
instrument — changing only that one entry and rebuilding, never rewriting the instrument — and
verifies the result against its own independent derivation of the edge list from `tower-2.py`'s
bounds. Under the corrected reading the thirteenth stage has **13 edges** and the cycle-rank
sequence is **(0, 0, 1, 1, 1, 1)**. Those are the values the paper states (§5, Table 3, Figure 2,
§0 item 3, Abstract). The two-parent reading is stated in the paper as Proposition 9, explicitly as
a counterfactual — what the arity-2 bound *would* cost the graph — with its 14 edges and
`(0,0,1,1,2,2)`, and §6.1 prices the same difference in cells. The triangle count, the treewidth,
the girth and the degrees of `k` and `g` are unchanged by the correction, and the paper says so.

Two further consequences of the same reading are carried through and are not stated in the source
in this form; they are the paper's own and are marked PROVED:

1. The distinction between the **arity of a bound** and the **number of parents of a coordinate**
   (D3). The source's phrase "has one parent" is about the bound. The tenth coordinate `v` has
   **two** parents (`2S′` and `g`) and **two bounds of arity 1**, and it closes — which is why
   Theorem 1 is stated with two possibly-different parent indices `j` and `j′`. Without that
   distinction the source's own dichotomy would predict that `v` breaks closure, and it does not.
2. Hence the tenth stage's cycle rank of 1 and the twelfth's exactness are two different
   phenomena: the first is a coordinate with two adjacent parents (costs the tree, costs no
   closure), the second is a single bound of arity 2 (costs closure). The paper states this as the
   closing remark of §5.

## What reproduces

Reproduced exactly, by `check.py`, from the imported instrument or from first principles:

- the six cell counts 976 / 1,654 / 2,535 / 13,585 / 70,905 / 199,130; the six ambient boxes
  6,912 / 27,648 / 110,592 / 663,552 / 5,308,416 / 47,775,744; the six fills 14.12 / 5.98 / 2.29 /
  2.05 / 1.34 / 0.42 per cent; `E = 0` at every stage by the ambient sweep, and the sublattice
  property by every pair at the first four stages;
- `φ̂ = {1:3, 2:4, 3:5}` equals the realised maxima; `max 2J(p^k) = 3,4,5,4,3,0`;
  `max 2S(p^k) = 1,2,3,2,1,0`; `min(g, 4f+2−g)` reproduces `max 2S(f^g)`; particle–hole symmetry;
- the density column of §12.11.1, **five of six entries**: 63.7% at axis 9, 44.7% at axis 10,
  17.0% at axis 11, 31.4% at axis 12, 64.4% at axis 13 (Table 2 of the paper), each as the ratio of
  the summed exact fibre to the summed admissible fibre over the stage below. §12.11.1.1's separate
  eleventh-axis figure — envelope 13,585 against exact 10,585, **77.9%** — also reproduces exactly,
  and the paper prints both readings;
- the sections 33×5 / 33×10 / 23×15 / 8×17 at Λ₈, 815 / 3,260 / 6,150 / 3,360 at Λ₁₁ and
  11,470 / 45,880 / 89,700 / 52,080 at Λ₁₃, with defect zero at every stage;
- the tight two-parent K's factorisation defect, 15,150 cells (21.4%) at Λ₁₂ and 45,450 (22.8%) at
  Λ₁₃ — the values §12.11.5 prints after its own recomputation;
- the exact triangle at axis 12: **22,275 cells and E = 35,570**, the Mathematical Compendium's
  figures under "The tree or the tightness";
- `coupling.py`'s recorded triangle figures at cap 6 — 2,862 failing meets and 0 failing joins —
  reproduced by an independently written brute force inside `check.py` and used as the encoding
  guard; and Appendix A.15's **12,654** failing meets for `{|a−b| ≤ c}` at cap 8;
- seventeen generators, twenty covering relations, 976 down-sets, **1,113,045,672** maximal chains,
  the rank sequence, widest level 122 at rank 11, `976 = 8 × 122`;
- the bracket system: gap-free intervals with monotone endpoints at all five stage projections,
  branching 4, 4, 6, 8, 9, composed bracket containing the direct one with slack ≤ 2 rank units,
  both routes covering ranks 3 to 20;
- `seed(Λ₈) = 7`, exact — the value §14.5.9 states by branch and bound, and the value the companion
  closure-law paper (`01-closure-law`) establishes; and §14.5.10's universe of **102** requirements =
  77 envelope steps + 25 alphabet values. The source's figures for Λ₉ and Λ₁₀ do **not** reproduce
  as seeds; see item 5 below.

## What does not reproduce, and what the paper prints instead

**1. ⟨q⟩ at the top of the tower.** §12.11.5 writes "The mean transfer rises, ⟨q⟩ = 1.4631 → 1.887",
and Figure 12.3's caption repeats "the tower shifts ⟨q⟩ from 1.463 to 1.887". Measured:

| stage | Λ₈ | Λ₉ | Λ₁₀ | Λ₁₁ | Λ₁₂ | Λ₁₃ |
|---|---|---|---|---|---|---|
| ⟨q⟩ | 1.4631 | 1.6850 | 1.8304 | **1.8874** | 1.9141 | **1.9159** |

1.887 is **Λ₁₁'s** value, not Λ₁₃'s; at the top of the tower the mean transfer is 1.9159. This is a
claim of the source that does not reproduce as written — a stage mismatch, not an arithmetic error
— and the paper prints the whole measured row (Proposition 11) and never the figure 1.887 attached
to Λ₁₃. Nothing else in the paper depends on it.

**2. The sixth density-column entry.** §12.11.1's row "9′" (67.5%) is for the *alternative* object
Λ₉′, built with the extra Pauli cut `2S′ ≤ 2f+1`, which is not a stage of the tower. It was not
attempted and the paper does not print it.

**3. §12.11.2's five presentations** (50,592 / 52,080 / 17,856 / 7,254 / 2,443 failures) are named
in prose and defined nowhere; `coupling.py` records that no instrument in the tree reproduces any of
the five. They were not attempted and nothing in the paper rests on them.

**4. A withdrawn price never enters.** The audited plate for the source's Figure 12.4 prints
"breaks the cylinder by 3.5%", a price §12.11.5 itself supersedes. The paper does not use that
plate: its constraint-graph figure is computed by `figures.py` from `check.py`'s own edge list, and
the price it prints is the recomputed 21.4% / 22.8%. Likewise the "2,475 cells" of Appendix A.15's
remark and §12.11.3.1 is superseded in §12.11.5 by 15,150 and 45,450, and the paper prints the
later values only.

**5. The seeds of Λ₉ and Λ₁₀.** §14.5.8's table (main volume lines 3830–3836) and register 511 print
the tower's seeds as **7, 9, 9** "under greedy set cover" / "under set cover", and conclude that
"Λ₉ and Λ₁₀ seed identically — so the seed does not even rise with every stage". Only the first of
the three is stated as exact (§14.5.9, by branch and bound). Measured:

| stage | Λ₈ | Λ₉ | Λ₁₀ |
|---|---|---|---|
| source (greedy) | 7 | 9 | 9 |
| plain greedy on steps + slots, recomputed | 7 | 9 | 9 |
| **exact, branch and bound over the maximal step signatures** | **7** | **8** | **9** |
| solver: no (seed − 1)-cover of the reduced instance | unsat | unsat | unsat |
| packing lower bound (exact search) | 6 | 7 | 8 |

The greedy figures reproduce exactly — the source's algorithm gives what the source says it gives —
but **`seed(Λ₉) = 8`, not 9**: the branch and bound finds an 8-cell step cover that also realises
every alphabet value (so it is a seed by Lemma 3), and Z3 refutes any 7-cover. This is a claim of the
source that does not reproduce, and it is not an arithmetic slip: greedy set cover is an
approximation and at Λ₉ it is one above the optimum. The consequence — "Λ₉ and Λ₁₀ seed
identically" — falls with it: the exact seeds are 7, 8, 9, one more at each stage. The paper prints
the exact values only (Theorem 7), prints the greedy figures beside them *as* greedy figures, and
claims no law from three points. `check.py`'s previous expectation `{9: 9, 10: 9}` was copied from
the source and was the second obligation the previous run reported as failing; it is replaced by the
measured values, which is what BRIEF-RESUME.md step 4 requires — a check is never changed to match a
text, and here the check's own branch and bound is what the paper prints.

Two facts the companion closure-law paper establishes are respected: `seed(Λ₈) = 7` is exact (agreed,
by the same method and independently certified here), and the linear box law `d + c − 2` is false
from five dimensions — the paper never states a linear law; the one place it mentions the rise 7, 8,
9 says outright that three points fix no law.

## Two obligations failed, and which of the two each was

**(a) `--selftest`'s first negative control was a bug in the control.** It asserted that the region
`{c ≤ a + b}` (the triangle with its lower bound dropped) is *closed*, so that its failure count
(0, 0) would separate it from the triangle's (2,862, 0). The region is not closed: `(2,0,2) ∧ (0,2,2)
= (0,0,2)` leaves it. Its true failure count at cap 6 is **(2,254, 0)**, which does separate it from
the triangle's, and that is what the control now asserts. No result of the paper depended on this;
it is the kind of error a selftest exists to surface, and the record of it is here.

**(b) The seed expectation at Λ₉**, above: a claim of the source, recorded, with the reproduced
value printed. (The Λ₁₀ figure, 9, coincides with the exact value and is printed as exact on the
strength of the branch and bound and the solver, not of the source.)

## An earlier obligation failed in the previous pass, and which of the two it was

`check.py` as it stood before this pass reported

```
[XX] EXHAUSTIVE  pair counts at Λ_12 and Λ_13 ...  2513724060 and 19826278885
```

against hard-coded expectations of `2513724560` and `19826278385`. This is **a bug in the check, not
a claim of the source that fails**: `70905·70904/2 = 2,513,724,060` and `199130·199129/2 =
19,826,278,885` exactly, so the computed values are right and the two constants were mistyped (a `5`
for a `0` in one, a `3` for an `8` in the other). Fixed by replacing the literals with the
expressions `70905 * 70904 // 2` and `199130 * 199129 // 2` **and** the correct literals, so the
obligation now asserts both the formula and the value. The paper's Table 1 prints the corrected
figures. No source passage states either number.

## Changes made to `check.py` in this pass, and why

1. The two mistyped pair-count literals, above.
2. `check_envelope_gap()` added: the exact fibre against the admissible one at each of the six axes
   (Table 2 of the paper), plus the monotone envelope of the non-monotone realised maximum.
3. The tight-K closure defect at Λ₁₂ was printed but not asserted (`ob(..., True, ...)`); it is now
   pinned at `E = 12,675` and carries REFUTATION rather than a free pass.
4. Three obligations added to `check_graph()`: no edge joins the parent block to the target block at
   any stage, and deleting `q` leaves exactly two components. The previous check confirmed only that
   the component containing `e` is the target block.
5. Four obligations added to `check_rank_and_chains()` and `check_seed()`: the coordinatewise
   extremes of Λ₈ are cells (so the bottom and top used by the chain recursion are the lattice's own),
   the rank sequence, the alphabet sizes, and the requirement counts 77+25 / 105+29 / 138+33.
6. **The seed-minimality obligation's domain was narrowed from all distinct covering signatures to
   the ones maximal under inclusion**, because the query over all 808 signatures is not decided in
   300 s by either an `AtMost` or a `PbLe` encoding, while the query over the 264 maximal ones
   returns `unsat` in about two minutes. This is a reduction, not a weakening: a cover using a
   signature contained in another may replace it by the larger without growing, so a minimum cover
   may always be taken among the maximal signatures. The reduction is **checked** by a new GUARD
   obligation that exhibits every one of the 808 signatures inside a maximal one, and it is stated
   and proved in the paper (§9, Theorem 7's proof). No number changed.
7. Section headers renumbered to match the paper's own section numbers.

Changes made in the resumption pass (2026-09-24):

8. `check_seed()` rebuilt around the exact values. The expectation `{8: 7, 9: 8, 10: 9}` is the
   branch and bound's own result; a second obligation asserts the exhibited minimum realises every
   slot (so the step relaxation is tight); the seed is regenerated under **two** independent
   staircases (fixed box and own box); the plain greedy cover is computed and pinned at the source's
   7, 9, 9 as an upper bound; the maximum packing is found by exact search and pinned at 6, 7, 8.
9. **The solver obligation now runs on a dominance-reduced instance**, because over the 442 unreduced
   maximal signatures of Λ₉ the query `AtMost 7` was not decided in ten minutes. Two exact
   reductions are applied — element dominance (a step witnessed by every cell that witnesses some
   kept step is dropped) and set dominance after the restriction — and **each is checked as a GUARD
   before the solver is asked**: every dropped step's witness family contains a kept step's, and
   every restricted signature sits inside a maximal one. Reduced, the three queries return `unsat`
   in 0–2 s. This is a reduction, not a relaxation: the reduced instance has the same optimum, and
   the guards are what say so. All three stages are now MACHINE-CHECKED where before only Λ₈ was.
10. The selftest's first negative control corrected as described above.
11. Five pins added for numbers the prose stated but nothing computed: the pair sum 97,323,996; the
    growth factors 204 and 6,912 and the sweep-to-pairs ratio 415; the 287,809 cells of the five
    upper stages and C(13, 3) = 286; the compressions 139, 207, 282.

Nothing else was altered, and no obligation was relaxed.

## What the repair changed (2026-09-24), and every departure from the source it introduced

**1. The thirteenth axis is an envelope, not exact.** Appendix A.15's closing sentence (main volume line ~10175) says B₁ "is the reason the last coupling step is carried exactly", and the first draft's Theorem 5(iii) asserted that substituting a constant for one side of the triangle gives the band. It does not: it gives {|xᵢ − k| ≤ y ≤ xᵢ + k}, which is not a sublattice ((0, k) ∧ (k, 0) = (0, 0)), and whose least envelope in Theorem 2's sense is the band Bₖ. `check.py` now builds the exact thirteenth stage under both readings — the doublet 2J = 2K ± 1 (128,225 cells, the 64.4% of §12.11.1's density column) and the constant-side triangle before the congruence (185,545) — exhibits the meet witness (…,0,1) ∧ (…,1,0) inside the construction, measures the staircase defects 70,905 and 13,585 (ℛ of either exact stage is Λ₁₃ itself), and verifies that D10's band is the least envelope of the doublet, reproducing 199,130 as a set equality. **The paper now agrees with §12.11.0.10's own grading of Λ₁₃ as "envelope"** and with §12.11.1.1's attribution of the ⅔ to parity plus the K = 0 singlet (main lines 3145–3150): the 70,905 cells the band admits and the doublet does not are 57,320 by the congruence and 13,585 at 2K = 0. Appendix A.15's sentence is recorded here as a claim of the source that does not reproduce as written; the theorem it rests on (Bₖ a sublattice) reproduces and is Theorem 4(i).

**2. Theorem 2 is fibre-wise.** The source's Appendix A.14 / §12.11.2 states the envelope for a bound of one coordinate; the exact fibres of Table 2 depend on two or three. The paper states Theorem 2 for F a function of the whole cell, with l⋆ over {x : xⱼ ≥ a} and h⋆ over {x : xⱼ′ ≤ b} (two parent indices, as in Theorem 1), and `check_envelope_family()` computes the least envelope at every axis with the construction's own parent indices. **New measurements, not in the source**: the construction's bound is the least envelope at axes 10, 13 and 11 (wider reading) and is *not* at axes 9 (1,638 against 1,654 — the 16 cells with g = 3, where 2S′ ≡ g mod 2 excludes 0), 12 (60,320 against 70,905) and 11 in the strict reading (12,425). Also new: at axis 10 the exact fibre is empty at 600 cells of Λ₉ and at axis 11 (strict) at 1,305 cells of Λ₁₀ — cells the envelope below admitted and no term realises; the paper says how Theorem 2 is applied there (minima and maxima over the non-empty fibres, with l⋆ ≤ h⋆ verified at every cell). §12.11.1's "each envelope is priced once" (main line ~3057) is the same phenomenon seen from the density column.

**3. The source's exact/envelope grading of Λ₉, Λ₁₀ and Λ₁₃** (§12.11.0.10: "exact", "exact", "envelope") **is not the paper's.** The source's "exact" there means E = 0 with the bound carried as written — what the paper states as Proposition 2 for every stage. The paper's Corollary 1 grades by whether the *exact physical set* is carried, and by Table 2's own realised shares (63.7%, 44.7%) no adjoined axis is; all five are envelopes in the paper's sense, and the thirteenth agrees with the source's grading. This is the paper's reading, recorded here as such (A-21).

**4. E = 0 is proved, not only swept.** Lemma 2 (new) proves ℛ(X) = X for any set cut out by constant bounds and monotone one-coordinate bounds; the source proves closure by §7.3's argument and confirms E = 0 by the sweep (register 249's table). The §5 remark that attributed ℛ's exactness to treewidth 1 and its loss to treewidth 2 — a reading of the Mathematical Compendium's Freuder entry — is withdrawn from the paper: Freuder 1982 is about arbitrary binary constraints on a tree, and the construction's exactness comes from the shape of its bounds. Jeavons & Cooper 1995 (max-closed constraints decided by arc consistency) is cited for the related fact.

**5. The coupling scheme is named and scoped.** The Mathematical Compendium's "The recoupling bound" and "The spin-half bound" entries (lines 1694–1712) and its coupling-scheme entry (line 1393: "the tower as built uses jK … jK is privileged by the outer electron's half-spin degenerating the final triangle to |2J − 2K| ≤ 1") are the source; the paper now states that 2K and 2J are the J₁l labels of Racah 1942a for one outer electron, applied at every g ≤ 3 as bookkeeping, that 2Jₚ is bounded by the terms of ℓᵏ before the transfer (not the residual core), and that the constant 1 is a convention of the labelling rather than a consequence of the cell's 2S′ ≤ 3 (R-8, R-9). The source does not state the scope; the paper does, and prices nothing under the residual-core reading.

**6. §6.2 (orientation) is cut**, with its obligation. Proposition 14 proved that a bipartite sign assignment is balanced — Harary 1953, which the Mathematical Compendium's own entry (line 1178) cites — over eight quantities (e, ν, V, T, r, δ, the spacing, w) that the paper never defined and that no other result used. The source's §12.1 claim ("zero reversing loops among all cycles of length 3 to 5") is therefore not carried by this paper; nothing else depends on it. The 8,018-cycle obligation was removed from `check.py` because it tested a signed complete graph on eight labels and no object of the paper.

**7. References added, each verified.** From the tree: Dilworth 1950 (main volume lines 11598, 11708: Ann. Math. 51, 161–166); Racah 1942b = Phys. Rev. 62, 438–462 (main line 11658). By web search on 2026-09-24 (publisher or index pages): Topkis 1978, *Operations Research* 26(2), 305–321; Topkis 1998, *Supermodularity and Complementarity*, Princeton; Milgrom & Shannon 1994, *Econometrica* 62(1), 157–180; Jeavons & Cooper 1995, *Artificial Intelligence* 79(2), 327–339; Jeavons, Cohen & Gyssens 1997, *J. ACM* 44(4), 527–548; Johnson 1974, *JCSS* 9(3), 256–278; Lovász 1975, *Discrete Math.* 13(4), 383–390; Chvátal 1979, *Math. Oper. Res.* 4(3), 233–235; Racah 1942a, "On a new type of vector coupling in complex spectra", *Phys. Rev.* 61, 537 — the APS page is behind the egress proxy, so only the first page is printed, as the volume's own reference style does. Harary 1953 was not added because §6.2 was cut. The Racah 1942 citation for the vector-coupling (triangle) rule is dropped — that rule is Wigner 1931 — and Racah 1942b is cited instead for the general classification of the terms of ℓᵏ, which is what the Compendium's "The parent bound" entry cites it for.

**8. The guards now guard.** The encoding-fidelity guard evaluates the Z3 predicates themselves at concrete integers (10,176 evaluations, 0 disagreements); the three seed obligations carry a non-vacuity guard and a fidelity guard of their own; Theorem 1's Z3 form carries two parent indices. See "Changes made in the repair pass" below.

**9. Figure 2's rim criterion** is now "first-stage coordinate" against "adjoined coordinate, carried as an envelope" — five orange rims, all five adjoined coordinates — consistent with Corollary 1. The first draft rimmed 2Jₚ, 2K and 2J only.

## Changes made in the repair pass (2026-09-24)

12. `counting_axis_formula()` carries two parent indices (x₁, x₂ for the lower bound's parent, u₁, u₂ for the upper), ten free variables; `py_counting_axis()` is its reference in ordinary arithmetic; the non-vacuity guard demands the two parents move oppositely and both bounds strictly monotone.
13. `z3_eval()` substitutes concrete integers into a Z3 formula and simplifies it to a constant. `guard_encoding()` now evaluates every Z3 predicate the solver is given (triangle, |a−b| ≤ c, Bₖ, the constant-side triangle, Theorem 1's hypothesis and conclusion) on cap boxes, random pairs, 600 random points and 450 cell pairs drawn from the 150 random sublattice instances, and counts disagreements with the lambdas (0). The brute-force references are kept, and the constant-side triangle is added to them.
14. `cst_formulas()` — Theorem 5(iii)'s region {|x − k| ≤ y ≤ x + k} with k free; MACHINE-CHECKED join-closed, REFUTATION for meet with the witness (0,k) ∧ (k,0) verified for k ≤ 6; a sixth negative control in the selftest.
15. `check_envelope_family()` — the least envelope at every axis (seven readings), l⋆ and h⋆ printed, monotonicity, l⋆ ≤ h⋆ at every cell, containment of the exact fibre and containment in D10's interval; the counts 1,638 / 2,535 / 12,425 / 13,585 / 60,320 / 199,130 and the empty-fibre counts pinned; the 16 cells with g = 3; the band as Λ₁₃ and as the least envelope of the doublet; the two exact thirteenth stages, the witness, the defects 70,905 / 13,585 and the split 57,320 + 13,585; Theorem 5(iii)'s envelope on {0..M} for k ≤ 6 (56 cases); exact < least at every axis; 2S′ ≡ g (mod 2) in every spin set.
16. `check_seed()` — a non-vacuity GUARD (the clauses satisfiable with `want` signatures, the model verified as a cover) and an encoding-fidelity GUARD (the clause set evaluated at concrete assignments against the direct cover test: the carried minimum, each one-member deletion, 40 random subsets) at each stage; the MACHINE-CHECKED row is gated on both.
17. The two obligations for the paper's Theorem 3 renamed (they were labelled "Theorem 5(i)/(ii)").
18. Pins added: the six ⟨q⟩ values; Prop. 13's 248,076,675 pairs, 52,767,450 failing meets and 28,742,850 failing joins; μ(0, 1) = 1 and μ(0, 2) = 0; φ̂ as the running maximum of D12.
19. `senior_set()` factors the axis-10 exact fibre out with the conjugate ceiling v ≤ 4f + 2 − g added; 1,132 is unchanged.
20. The `EDGES` comment says the list is a transcription; `check_graph()` compares it with the instrument's list as before.
21. The orientation obligation removed with §6.2 (item 6 above). It is the only removal; no obligation was relaxed.
22. `figures.py`: Figure 2's envelope set is the five adjoined coordinates, with the legend moved to the upper right; Figure 4's first-stage labels offset from markers and line; Figure 5's sixth-panel legend given headroom. `FIGURES.tsv` carries the three new md5s.

Totals moved from 122 obligations (99 EXHAUSTIVE, 8 MACHINE-CHECKED, 7 REFUTATION, 8 GUARD) to the figures the paper's §10 prints.

## Interpretations chosen

1. **Arity of a bound against parents of a coordinate** (D3). See "the correction" above. This is the
   paper's own distinction; the source's dichotomy is stated in terms of "parents" alone and is
   consistent with it only under this reading, because the tenth coordinate has two parents and closes.
2. **"Closed" means sublattice of its own box.** The source uses "closed" for this and also uses
   `ℛ(X) = X`. The paper keeps them apart: Lemma 1 proves `ℛ(X) = X ⟹ sublattice` and uses only
   that direction. The converse (Appendix A.2's biconditional) is **not** used anywhere, because
   Appendix A.3's own remark records that closure is a d-dimensional condition whose pairwise
   projections are necessary and not sufficient, and the two statements are in tension. Avoiding the
   biconditional costs the paper nothing: the sublattice property of every stage is also proved
   directly by induction from Theorem 1.
3. **The symbol for the bracket system.** The Mathematical Compendium writes it
   `χ(Λ₁₃) → … → χ(Λ₈)`, where χ denotes the set of rank values; the main volume uses χ at §7 for
   the indicator, a product of Heaviside steps. The paper avoids the collision entirely by writing
   `r` for the rank (D7) and naming the brackets `β_D`.
4. **The seed's covering universe, and which box `ℛ(G)` is computed in.** §14.5.10's 102 elements
   are 77 envelope steps plus 25 alphabet values, and the companion closure-law paper's Theorem 13
   defines the seed the same way (slots and steps, `ℛ(G)` in `Box(G)`). The paper's D13 now adopts
   that definition — the previous draft's D13 said "computed in `Box(X)`", under which the slots would
   not be required, and its Lemma 3 carried the alphabet condition as a hypothesis rather than a
   conclusion. Lemma 3 is restated as the biconditional (seed ⟺ every slot realised and every step
   witnessed) and proved in both directions. `check.py`'s minimum cover runs over the steps alone,
   which is a relaxation and hence a lower bound; the exhibited minimum turns out to realise every
   slot at all three stages, so the relaxation is tight and the seed equals its optimum. Theorem 7
   states the argument in that order.
5. **Which exact set is "the" exact set at axis 11.** Two readings both appear in the source and give
   different answers (17.0% and 77.9%). The paper prints both, names the definition behind each, and
   prefers neither.
6. **Orientation.** Not carried: §12.1's "zero reversing loops among all cycles of length 3 to 5" was
   the first draft's §6.2, cut in the repair ("What the repair changed", item 6).
7. **Exact against envelope, at the ninth and tenth axes.** The source grades Λ₉ and Λ₁₀ "exact"
   (§12.11.0.10); the paper carries every adjoined axis as an envelope of its exact physical set and
   says why ("What the repair changed", item 3).
8. **The coupling scheme.** 2Jₚ is bounded by the terms of ℓᵏ before the transfer, as `tower-2.py`
   and §12.11.1 define it, and 2K, 2J are the J₁l labels for one outer electron applied at every g;
   the paper states this as the reading it inherits and does not price the residual-core alternative.

## Out of scope, read but not used

§12.11.0 through §12.11.0.12 (composition, the clock, the arrow indexes, the fourteenth axis, an
index inside a larger index), §12.11.1.2 through §12.11.1.7 (the conservative share, composability
up the tower, the non-composable cells, the periodic table's own numbers, the selection rules),
§12.11.4 (precision is path-dependent) and §12.11.6 (an index whose one prediction is false) were
read in full and are outside the brief's scope. The Index of Indices' composable-fraction column
(0.0000, 0.7068, 0.8087, 0.6956, 0.6592, 0.6381) was read and is not reproduced here, because
composition is not part of this paper's subject; nothing in the paper depends on it.

## Typography pass (2026-09-24), and three symbol renames it forced

The contract's §9 rule — mathematics in running text is plain Unicode, never a code span; a bar
inside a table cell is ∣ (U+2223) — was applied to the whole paper: 900 code spans were converted
and only the solver's `unsat` remains in backticks. Three symbols had no Unicode subscript and were
renamed in the paper (and only there; `check.py` keeps the instrument's names, which are not published):

- the core's angular momentum `2J_c` is written **2Jₚ** (p for parent core); Figure 2 was regenerated
  by `figures.py` with that label and `FIGURES.tsv` carries the new md5;
- the generic stage index `D` (as in `Λ_D`, `β_D`) is written **s** (`Λₛ`, `βₛ`), since no subscript
  capital exists; the numbered stages `Λ₈ … Λ₁₃` are unchanged;
- the generator's coordinate index `c` in §7 is written **i** (`G(i, v)`, `xᵢ ≥ v`), and Theorem 5's
  two coordinates `a ≠ b` are written **i ≠ j**, since no subscript `b` or `c` exists; Theorem 1's
  second cell `(x′, y′)` is written `(u, w)` so that primes and subscripts do not collide;
- the envelope functions `l*`, `h*` are written `l⋆`, `h⋆` because a bare asterisk is emphasis markup.

None of these is a change of content.
