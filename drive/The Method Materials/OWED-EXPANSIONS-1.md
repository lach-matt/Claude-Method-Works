# Owed proof/claim expansions — main volume → compendia

Standing rule: every main-volume claim is a SKETCH bound to a FULL EXPANSION in a compendium.
When the expansion is missing/unfinished, it is flagged here as OWED — not authored inline.
When we reach a compendium, its owed rows are authored as a batch, each bound back to the citing claim.

| # | main-volume claim (chapter, sketch) | expansion home | status | notes |
|---|---|---|---|---|
| 1 | **Ch 5 (was 7) §5.3 — Λ is closed under join and meet** (sketch: check x∨y against each monotone condition, both branches, ∎) | Mathematical Compendium, `L.closed` entry | **OWED (unfinished)** | Entry EXISTS and states the theorem + prior art (Birkhoff 1940, sublattice of product of chains; forced by all constraints being xᵢ≤f(xⱼ) monotone) and the φ instrument (line 29776), but the WORKED CASE-BY-CASE PROOF is not written out. Author full expansion: x∨y and x∧y; slot-from-x and slot-from-y branches; each of the 7 constraints. Main volume currently the only place the argument appears (in sketch). |

## How to use
- Add a row whenever a main-volume claim's full expansion is missing or unfinished.
- "expansion home" = which compendium + which entry/section.
- At each compendium pass: filter this file for that compendium, author each owed expansion, bind it to the citing claim, then mark DONE.

## Batch from Ch 6 (was Ch 8) — all owed to Mathematical Compendium
| 2 | Ch 6 §6.1 — Λ distributive (product-of-chains embedding forces distributive law) | Math Compendium | OWED | verified 4,000 triples; full proof of the forcing not written out |
| 3 | Ch 6 §6.2 — rank modular (equality) = signature of distributivity; equiv on graded lattice | Math Compendium | OWED | verified 475,800 pairs; derivation of equality + equivalence owed |
| 4 | Ch 6 §6.3 — 17 join-irreducibles, 20 covers, exact down-set correspondence (Birkhoff) | Math Compendium | OWED | poset construction + proof all 976 down-sets = 976 cells; cap-independence of the 15 patterns |
| 5 | Ch 6 §6.4 — Sperner via log-concavity + Dilworth/matching; not rank-symmetric; not self-dual (8 fixed) | Math Compendium | OWED | log-concavity computation, Dilworth argument, particle-hole terms(ℓᵏ)=terms(ℓ^(4ℓ+2−k)) |
| 6 | Ch 6 §6.6 — order dimension 8 = width of J(Λ) (Dilworth) | Math Compendium | OWED | width computation owed; register 409 notes it is asserted-not-derived (that provenance is workshop, not for reader) |

## TOKEN BINDING (main volume ↔ this register)
Each row number N is cited in the main-volume prose as the placeholder token **[MC-NN]**, which reads as a finished citation to the Mathematical Compendium. The prose NEVER says "owed"/"not yet written" — that status lives only here.
- MC-01 → row 1 (Ch5 §5.3 closure)
- MC-02 → row 2 (Ch6 §6.1 distributive)
- MC-03 → row 3 (Ch6 §6.2 modular)
- MC-04 → row 4 (Ch6 §6.3 Birkhoff down-sets)
- MC-05 → row 5 (Ch6 §6.4 Sperner/log-concavity/Dilworth)
- MC-06 → row 6 (Ch6 §6.6 order dimension = width)

## RESOLVE PASS (when the Mathematical Compendium is finished)
1. Author each owed expansion into the compendium (batch, per this register).
2. Number the compendium sections.
3. grep the main volume for `\[MC-` and replace each [MC-NN] with the real compendium §-citation for that proof.
4. Mark each row DONE here.
Placeholders are greppable: `grep -rn '\[MC-' ` finds every unresolved pointer.

## Batch from Ch 7 (was Ch 9) — Mathematical Compendium
| 7 | Ch 7 §7.1 — ω(N(x)) ≤ dim(Λ) tight; rank = Ω(N) | Math Compendium | OWED | one-prime-per-coordinate argument; full statement + tightness |
| 8 | Ch 7 §7.2 — occupancy measure d(x,y): five equivalent forms + metric properties (mult. triangle ineq, log d ℓ¹, hyperbolic balls) | Math Compendium | OWED | equivalence of 5 forms; metric proofs |
| 9 | Ch 7 §7.3 — Möbius closed form μ=(−1)^|y∖x| on antichains; arith transfer iff void-free unit hypercube | Math Compendium | OWED | closed form proof; transfer condition (60/56 split) |

## token binding additions
- MC-07 → row 7 (Ch7 §7.1 ω≤dim)
- MC-08 → row 8 (Ch7 §7.2 occupancy measure)
- MC-09 → row 9 (Ch7 §7.3 Möbius closed form + transfer)

## Batch from Ch 10 "The void" (was Ch 10 → new Ch 8) — Mathematical Compendium
| 10 | Ch 10 §10.2 — constraint correlation: 1.49× above independence from shared coordinates along the tree (67–94% individual, 20.19% product, 30.13% joint) | Math Compendium | OWED (NEW) | **Required by the four-origins vs correlation reconciliation.** Must derive the 1.49 factor from the tree's coordinate-overlap structure, and show WHY shared coordinates (q in q≤k & g≤q; k in k≤2(2ℓ+1) & q≤k) produce positive dependence. This is the "mathematical accompaniment" M flagged. |
| 11 | Ch 10 §10.4 — closed-form void count (tree factorisation, two closed-form leaves); treeness ⟺ sieve-free count | Math Compendium | OWED | full factorisation + proof that treewidth-1 is exactly the sieve-free condition |

## token binding additions
- MC-10 → row 10 (Ch10 §10.2 correlation analysis — NEW, from reconciliation)
- MC-11 → row 11 (Ch10 §10.4 closed-form void count)

## NOTE on reconciliation (Ch5 four origins vs Ch10 correlation)
Old §10.2 said correlation was because "all seven constraints descend from two origins" — this was IMPRECISE and collided with Ch5's "four origins". Corrected: the correlation is STRUCTURAL (constraints share coordinates along the tree → positive dependence), a fact about the constraint GRAPH, not the origin count. Four origins (physical laws) and coordinate-sharing (graph structure) are different things and don't compete. MC-10 owes the full derivation.

## Batch from Ch 11 "The single expression" (was Ch 11 → new Ch 9) — Mathematical Compendium
| 12 | Ch 11 §11.1.1 — binary/circuit: 20 implications cut 131,072→976 exactly; monotone boolean circuit depth 5; 7.07-bit surplus | Math Compendium | OWED | the exact cut, depth-5 circuit, surplus derivation |
| 13 | Ch 11 §11.2 — ten language-combinations each name a real object (P21) | Math Compendium | OWED | the 10 identities verified/derived |
| 14 | Ch 11 §11.6 — 2S detachable leaf: removing it leaves E=0; factor (1−z^{k+1})/(1−z); 976/319 both E=0 | Math Compendium | OWED | leaf-factorisation + E-invariance proof |
| 15 | Ch 11 §11.7 — closed expression exists ⟺ monotone + two-variable + acyclic; each removal breaks it (89,864 join failures for sum bound) | Math Compendium | OWED | the three-facts theorem + counterexamples |
| 16 | Ch 11 §11.8 — F(−1)=2 from the tree (even-valued coords ℓ,f vanish; couplings prevent free vanishing); palindromic ⟺ self-dual | Math Compendium | OWED | alternating-sum derivation; the three-routes-one-fact identity |

## token binding additions
- MC-12 → row 12 (Ch11 binary/circuit)
- MC-13 → row 13 (Ch11 ten combinations)
- MC-14 → row 14 (Ch11 detachable spin factor)
- MC-15 → row 15 (Ch11 why closed expression exists)
- MC-16 → row 16 (Ch11 F(−1)=2)

## Batch from "The shape" (source §12.1–§12.10.2 → reader chapter, split A of Ch 12) — Math Compendium
| 17 | Shape §12.1 — Λ orientable/cylinder: bipartite sign structure ⟹ no odd orientation reversal; both Möbius routes closed | Math Compendium | OWED | bipartite argument; zero reversing loops len 3–5; the two-routes-closed proof |
| 18 | Shape §12.6.1 — two-body separation: conditioned on q, |Λ|=Σ|A(q)||B(q)|=976 exactly (bare product 2,244) | Math Compendium | OWED | the exact conditional separation |
| 19 | Shape §12.7 — fibres A_q(z), B_q(z) in closed form, verified 33/33/23/8 and 5/10/15/17 | Math Compendium | OWED | closed forms + verification |
| 20 | Shape §12.8 — every cross-section closed+modular+E=0 (local E form, new invariant); Pareto; ⟨q⟩=1.4631; 8→3 caterpillar compression | Math Compendium | OWED | per-fibre closure; local-E invariant proof (doesn't follow from global) |
| 21 | Shape §12.9 — interval-is-box condition; maximal chains e(P)=1,113,045,672 = linear extensions; the two seventeens are one | Math Compendium | OWED | box condition; linear-extension count; generator=chain-length identity |

## token binding additions
- MC-17 → row 17 (cylinder/orientable)
- MC-18 → row 18 (two-body separation)
- MC-19 → row 19 (fibres closed form)
- MC-20 → row 20 (cross-sections closed, local E invariant)
- MC-21 → row 21 (shapes contained; maximal chains)

## Batch from "The tower" (source §12.11 tower sections → reader chapter, split B of Ch 12) — Math Compendium
| 22 | Tower — Λ₉ composes (41,682 pairs, 0 fail, associative, category); three gradings; composability lost at axis 10 before exactness | Math Compendium | OWED | closure-under-composition proof; the strict composability grading |
| 23 | Tower — the six axes, densities, exhaustive closure each stage, exact projection; tree-or-tightness (1,561 vs 1,654) | Math Compendium | OWED | per-axis density derivations (the workshop re-derivations feed this); Λ₉′ cycle cost |
| 24 | Tower — three excluded forms (reflection/congruence/triangle); coupling exact bound needs two parents or a congruence; join-closed meet-broken half-triangle | Math Compendium | OWED | the three-machines decomposition; particle-hole terms identity |
| 25 | Tower — law-vs-extent: bound from law closes exact, from extent only to envelope; E(X)=price of extent-over-law; φ̂ observed | Math Compendium | OWED | the deep result; E(X) interpretation |
| 26 | Tower — false-prediction: E1 |Δ2J|≤2 index, J=0↛0 gives E=1, the restored cell = photon's angular momentum unit; E counts proposals not guarantees | Math Compendium | OWED | the four-meets computation; E-counts-proposals calibration |

## token binding additions
- MC-22 → row 22 (Λ₉ composes / gradings)
- MC-23 → row 23 (the six axes)
- MC-24 → row 24 (three excluded forms)
- MC-25 → row 25 (law vs extent / what E measures)
- MC-26 → row 26 (the false prediction)

## NOTE: the tower workshop (cut from reader volume) is proof-of-work that EARNED these results (M). It is preserved in the working/process record and FEEDS the MC-22..26 expansions — the density re-derivations, vocabulary definitions (terms(ℓᵏ), f_max, φ̂), Q-item closures, and four-cap variation checks are exactly the rigor the compendium proofs need.

## Batch from "Time, and the clock in the constraint" (source §12.11.0.1–.12 → reader chapter, split C of Ch 12) — Math Compendium
| 27 | Time — occupancy clock: never rises, 3 strata, tick=k−g; definability≠reachability (11.4/24.7/0.4%); nine = unique dim where time exists | Math Compendium | OWED | clock theorem; the three-way pair census; register-314 dimension result |
| 28 | Time — arrow is frame-relative: g placed-vs-present; (g,G) repair 13,775 cells; 31.6% raise occupancy; one arrow per coordinate | Math Compendium | OWED | the observation-frame result; four weight-arrows closure table |
| 29 | Time — DECAY THEOREM: MRF on tree → conditional independence → data-processing → Pinsker; agreement decays with tree distance; fails at cycle | Math Compendium | OWED | full theorem proof; mutual-information decay; cycle falsifier |
| 30 | Time — past/present/future a path not triangle; future ⊥ past | present; saturated bracket; tick 350/350 two sources | Math Compendium | OWED | the two-sided-cut = internal-degree-2-vertex proof; conditional independence |
| 31 | Time — two indices: rev(Λ₉) lawful ≠ Λ₉; intersection groupoid (389, g=q=k); union E=2,857 does not exist | Math Compendium | OWED | reversal closure; groupoid proof; union defect |
| 32 | Time — every-Λ table: all E=0 (47M cells at Λ₁₃); fill monotone down 14.12→0.42%; two gradings part at different heights | Math Compendium | OWED | the one-pass tower census |
| 33 | Time — fourteenth axis bounded-not-built: fill monotone↓ by construction, converges to [0,0.42%], limit-value undetermined; null definable, E=0 necessary-not-sufficient | Math Compendium | OWED | **THE BOUNDARY grounded from inside — reconciles with Preface spine.** convergence deduction; empty-index-complete |
| 34 | Time — entering a larger index: Λ₁₃→44 rank values, 12.14 bits/cell lost, 31% survives; composition→bracket from above; every branch terminates in a cell | Math Compendium | OWED | compression; bracket-from-above; "ignorance not evidence of another" |

## token binding additions
- MC-27 → row 27 (clock/definability≠reachability)
- MC-28 → row 28 (arrow frame-relative / observation)
- MC-29 → row 29 (DECAY THEOREM)
- MC-30 → row 30 (past/present/future path)
- MC-31 → row 31 (two indices / union E=2,857)
- MC-32 → row 32 (every-Λ table)
- MC-33 → row 33 (fourteenth axis — THE BOUNDARY)
- MC-34 → row 34 (entering a larger index)

## VOID↔TRANSITION WATCH — §12.11.0.12 checked, NOT a grounding hit
Entering a larger index = COARSENING (fine index → coarse rank coordinate one dim up), resolution loss, "every branch terminates in a cell of Λ₉ / ignorance about this index is not evidence of another." This CUTS AGAINST emptiness-becomes-higher-substance rather than grounding it. Watch continues.

## MILESTONE: source Chapter 12 COMPLETE — all three splits drafted (shape 12A / tower 12B / time 12C). The time chapter is the Part I capstone and reconciles with the Preface observation-boundary spine (§12.11.0.11 = the boundary from inside).

## Called-out proof (M flag) — the triangle proof gets its own row
| 35 | Time §past/present/future — **"Λ's exactness is a proof that the three parts are not a triangle"** — treewidth 1 closes exactly, treewidth 2 gives an envelope, so E(Λ)=0 ⟹ the past-present-future graph has no past–future edge (path, not triangle) | Math Compendium | OWED (M-flagged, load-bearing) | Must be FULLY represented, not folded into MC-30 as a remark. Full proof: (i) treewidth-1 ⟺ exact closure, treewidth-2 ⟺ envelope (the §18.4.1 result); (ii) a triangle on {past,present,future} would be treewidth 2; (iii) Λ closes exactly (E=0), therefore the graph is treewidth 1, therefore no past–future edge — a path. Tie to the three-body shape (register 316) as the treewidth-2 / triangle case. |

## token binding addition
- MC-35 → row 35 (the exactness ⟹ not-a-triangle proof — M-flagged as requiring full compendium representation)
