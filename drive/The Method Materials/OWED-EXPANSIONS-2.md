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

## Batch from §12.11.8 "The electromagnetic index" (RELOCATED into the tower chapter per M ruling — was orphaned inside source Ch13) — Math Compendium
| 36 | Tower §12.11.8 — imposition criterion: a selection rule may be imposed on Λ₉ with closure surviving iff its set is convex in range; spin rule ΔS=0 = σ⁻¹({0}) convex → 526 cells E=0 (holds at 4 caps: 1,654/2,664/44,153/60,164); parity rule \|Δℓ\|=1 = δ⁻¹({−1,+1}) has a hole at 0 → 840 cells E=750; parity rule = 4th instance of the 2nd excluded form, first with a named repair (move the hole to an endpoint) | Math Compendium | OWED | convex-in-range ⟹ closure-preserving proof; the two set-images; §17.3 criterion derivation; four-cap stability |
| 37 | Tower §12.11.8 — quotient not extension: every EM quantity (Δℓ, ΔS, multipole) is a function of Λ's own coordinates, so adjoining them as new axes gives E=3,900 vs E(Λ₉)=0 (Theorem 17.1 direction); a derived coordinate cannot improve closure; EM predicate and composability predicate share 0.0004 of 0.633 bits — near-independent on the same cells | Math Compendium | OWED | Thm-17.1 application; the derived-coordinate-cannot-improve-closure lemma; the mutual-information near-independence computation |
| 38 | Tower §12.11.8 — four schemes price four routes: jK/LK reproduce stated Λ₁₃ counts from the recoupling chain alone (199,130 / 341,150); LS/jj bracket theirs under a looseness convention (LS ∈ [383,065, 597,325] ∋ 431,050; jj ∈ [160,380, 244,060] ∋ 206,520); the exact J-multiset is identical across all four in 15/15 configurations; the 2.17-fold cell-count spread prices four routes to one object; jK privileged because outer spin ½ degenerates the final triangle to \|2J−2K\|≤1 (Cowan & Andrew JOSA 55 502 (1965) precedent for the four-scheme set) | Math Compendium | OWED | chain reconstructions; the looseness-convention bracket; multiset-identity verification; the ½-spin degeneracy argument |

## token binding additions
- MC-36 → row 36 (imposition criterion / convex-in-range)
- MC-37 → row 37 (quotient not extension)
- MC-38 → row 38 (four schemes / four routes)

## PLACEMENT RULINGS (M, this session — source Ch13 pass)
- §12.11.8 "The electromagnetic index" RELOCATES into the approved tower chapter (REWRITE-chapter12B-tower.md, Drive 15MlD13IyVlhbfgY_4zN-aasp37YXCS2A) as its MISSING FINAL SECTION. It was orphaned inside source Ch13 but is tower material by number and content. The approved tower file currently ends at §12.11.6/MC-26; this section (with MC-36/37/38) appends after it. → produces a REVISED tower file for approval.
- §12.11.7 "What the tower leaves open" CUTS ENTIRELY to the working record (Q-item closures, self-duality self-audit, build-glyph mechanics, register-209, figure inventory). Nothing reader-facing survives that is not already stated. Recorded, not carried into any reader chapter.
- Consequence: reader Chapter 13 = title-history head + §13.1–§13.4 only (clean short Part II capstone). The EM material leaves it.

## Theorem 17.1 — flagged this session (invoked by the relocated EM-index section; stated in source §17.2, reader Ch15 not yet drafted)
| 39 | Theorem 17.1 (adjunction never repairs) — for any h : S → H with S′ = {(x, h(x))}: S′ closed ⇒ S closed; contrapositive, a non-closed set cannot be repaired by adjoining any function of its coordinates. Source states a compact proof (join/meet of (x,h(x)),(y,h(y)) = (x∨y, h(x)∨h(y)); tested on 7 functions incl. identity and constant, none repairs); tagged A.6 in the theorem index. The EM-index section (MC-37) invokes it as "a derived coordinate cannot improve closure." | Math Compendium | OWED | full expansion: the join/meet-projection argument in a product of chains; why every function of the coordinates falls under h; the seven-function exhaustive check; tie to the E=3,900 EM computation as the worked instance. **Bind BOTH the EM-index invocation AND source §17.2 (reader Ch15, when drafted) to this one expansion — one home, two citing sites.** |

## token binding addition
- MC-39 → row 39 (Theorem 17.1 adjunction never repairs — invoked in the EM-index section; also the home for §17.2 when Ch15 is drafted)

## NOTE (coherence, this session)
Theorem 17.1 is NOT re-proved in the EM-index section. It is cited there. Its proof expansion is owed once (MC-39) and will be authored when the Math Compendium is written; source §17.2 (reader Ch15) will cite the SAME MC-39 rather than carrying a second copy. This keeps one theorem = one expansion = many citing sites, consistent with the standing sketch/expansion division.

# =====================================================================
# MULTI-COMPENDIUM POINTER CONVENTION (M approved, this session)
# =====================================================================
# The sketch/expansion division (Rule 2) applies to EVERY compendium, not only Math.
# Each compendium gets its own greppable token series; a main-volume claim points to
# whichever compendium carries its full expansion. A single claim may carry more than
# one pointer when its expansion is genuinely split (e.g. the closure math in Math and
# the physics in Physics).
#   [MC-NN] → Mathematical Compendium   (proofs, closure theory, lattice structure)
#   [PC-NN] → Physics Compendium        (spectroscopy, selection rules, coupling physics)
#   [IoI-NN] → Index of Indices         (an object's entry as one of the book's named indexes)
#   [SC-NN] → Spectra Compendium        (measured-spectra expansions)
# Resolve pass (all series): when a compendium is finished + numbered, grep the main
# volume for its token prefix and replace each with the real §-citation; mark rows DONE.
# grep -rnE '\[(MC|PC|IoI|SC)-[0-9]+\]' finds every unresolved pointer across all four.

## Physics Compendium batch — from §12.11.8 "The electromagnetic index" (tower chapter final section)
| P1 | Tower §12.11.8 — the multipole map: multipole fixed by Δℓ and parity alone (Δℓ=0→M1, 1→E1, 2→E2, 3→E3, lowest whose parity matches); |ΔJ| unavailable because Λ carries no source J; map validated against nine textbook classifications and shown able to refuse before use | Physics Compendium | OWED | the physical derivation of the multipole-from-(Δℓ,parity) rule; why |ΔJ| requires a source J the tower never builds; the nine-classification validation and the refusal test |
| P2 | Tower §12.11.8 — intercombination lines: 576 of Λ₉'s cells are E1 transitions with ΔS ≠ 0, which LS coupling forbids and the index admits; the physics of why LS forbids them and why a jK-built index does not | Physics Compendium | OWED | the LS spin-selection rule and its breakdown; why the index's coupling choice controls which lines appear; the intercombination-line physics |
| P3 | Tower §12.11.8 — the four coupling schemes as physical recoupling chains: jK (ℓ₁+s₁=j₁, j₁+ℓ₂=K, K+s₂=J), LK, LS, jj; NIST chain definitions; Cowan & Andrew (JOSA 55, 502, 1965) precedent for the four pure-coupling types for two-electron configurations; the ½-spin degeneracy giving jK its privileged status physically | Physics Compendium | OWED | the four recoupling chains written out; the looseness convention LS/jj depend on; the physical reason jK is realised at high n (weak coupling last) |

## token binding additions
- PC-01 → row P1 (multipole map)
- PC-02 → row P2 (intercombination lines)
- PC-03 → row P3 (coupling schemes / recoupling chains)

## Index of Indices batch — from §12.11.8
| I1 | The electromagnetic quotient as one of the book's named indexes: Λ's EM image is a quotient not an extension; carried in the Index of Indices as an entry with its E-values (image E=0 vacuous; adjoined E=3,900; imposed spin-rule E=0 at four caps; parity-rule E=750) | Index of Indices | OWED | the IoI entry for the electromagnetic quotient — its coordinates, its E-signature, its relation to Λ₉; ties to source Part VIII heading "the electromagnetic quotient — a selection rule is a quotient, not an extension" (Ruling 53 wording) |

## token binding addition
- IoI-01 → row I1 (electromagnetic quotient as a named index)

## Batch from reader Chapter 13 "What the title names" (source Ch13) — new expansion homes
| 40 | Ch13 head / Part IV §21.1 — the languages result: eight results already in the book are one statement — a language is a coordinate system, translation is re-coordinatisation, and E is what the translation costs; E(Λ)=0 verified at 976 cells in six languages | Math Compendium | OWED (NEW) | the proof that the eight named results collapse to one statement; the six-language verification of E(Λ)=0 at 976 cells; the coordinate-system/re-coordinatisation/E-as-cost formalisation. This is the SUBTITLE's justification — load-bearing. |

## token binding addition
- MC-40 → row 40 (the languages result / eight results are one statement)

## Index of Indices batch — from reader Chapter 13
| I2 | Ch13 head — languages as coordinate systems: the eight results as one index-of-indexes statement; each "language" (jK, LS, LK, jj, and the four Part-names) as a coordinate system on the same object, E the translation cost between them | Index of Indices | OWED | the IoI treatment of languages-as-coordinate-systems; how the eight results register as one entry; tie to Part IV / source §21.1 and the Ruling-53 Part VIII heading "the languages — translation as re-coordinatisation, and E as its cost" |
| I3 | Ch13 §13.1 — the other closed indexes the method reaches: the nucleon index, the string partition function, the Kreuzer–Skarke frontier, and Appendix D's index of the book's own mathematics — each built, closed, and read for E(X), demonstrating the method travels beyond the cylinder | Index of Indices | OWED | the IoI entries for the nucleon index, string partition function, and Kreuzer–Skarke frontier as named closed indexes; each one's E-signature; the "build/close/read-E/record-every-failure" pattern shown to travel |

## token binding additions
- IoI-02 → row I2 (languages as coordinate systems)
- IoI-03 → row I3 (the other closed indexes the method reaches)

## NOTE (Chapter 13 pointer reuse — this session)
Ch13 restates several results whose expansions are already owed elsewhere; those cite the EXISTING tokens, no new rows:
- J-multiset identical across jK/LS/LK/jj + 2.17 spread (§12.11.4) → MC-38 (registered from the tower EM section)
- rank is modular → MC-03 (Ch6 §6.2)
- two-body separation |Λ|=Σ_q|A_q||B_q| → MC-18 (shape); maximal chains 1,113,045,672 → MC-21 (shape)

## Additional row from reader Chapter 13 §13.3
| 41 | Ch13 §13.3 — g ≤ q is the most active constraint in Λ: of the constraints defining the lattice, g ≤ q is the one that binds hardest (eliminates the most otherwise-admissible cells), and it is the coupling itself — the constraint that makes the object an index of transitions rather than of states | Math Compendium | OWED (NEW) | the ranking of constraints by cells eliminated; proof that g ≤ q is the binding one; why "most active" = "is the coupling." NOTE: distinct from MC-10 (which is the correlation factor); g≤q appears there as a shared coordinate but its activity-ranking is not MC-10's subject. |

## token binding addition
- MC-41 → row 41 (g ≤ q most active constraint)

## RULINGS (M, source Ch14 pass)
- Ch14 workshop is SUBJECT-MATTER proof-of-work → owed to the subject Register, tracked in OWED-REGISTER-EXPANSIONS.md (new file this session). Distinct from editorial/working-record cuts. Ruling-27 guard noted there.
- Ch14 SPLITS into two reader chapters along the recommended line: (A) "Closure, and the seed of Λ" (§14.1–§14.5.14); (B) "The family of closed indexes is open" (§14.6–§14.6.2). Split approved because it strengthens the arc (two distinct theorems).
- §14.5.8 counting/coupling seed-cost result STAYS as a qualified reader finding (it is subject matter). The challenge: untangle the surviving result from the withdrawn prune-greedy per-axis numbers. Surviving = the counting/coupling asymmetry read through the seed + Carathéodory linearity; withdrawn = the specific +1/+10/κ=S/4−1 parent-count numbers (→ R-02, register).

## Batch from reader Chapter 14A "Closure, and the seed of Λ" (source Ch14 §14.1–§14.5.14) — Math + Physics Compendia
| 42 | §14.1 — Theorem 14.1: X closed iff X = ℛ(X); ℛ reconstructs value sets and pairwise monotone bounds from X's extension | Math Compendium | OWED | full statement + proof; the staircase/φ_ij recovery |
| 43 | §14.2 — ℛ extensive/monotone/idempotent (closure operator); E(X)=|ℛ(X)|−|X| is a closure defect; periodic table 36, Λ 0 | Math Compendium | OWED | the three axioms verified; closure-defect framing; the two index E-values |
| 44 | §14.3 — scope: each coordinate presented as a chain (Birkhoff down-sets of join-irreducibles); bundling fails; presentation-respecting condition | Math Compendium | OWED | the chain-presentation requirement; why bundling hides structure; the 80/80 agreement |
| 45 | §14.5 — the closed subsets of a closed index form a Moore family (∩-closed, contains whole, not ∪-closed); Λ's own count open (2⁹⁷⁶), meet-irreducibles the route | Math Compendium | OWED | Moore-family proof; the three small-ambient counts (73/146/731); the ∩100%/∪32-68% asymmetry |
| 46 | §14.5.1 — Λ is the closure of SEVEN cells (compression 139:1), exact by branch and bound; no cell removable (ℛ(Λ∖{x})=Λ for all 976); seed = minimum set cover (elements=envelope steps, sets=cells) | Math Compendium | OWED | the set-cover reading; branch-and-bound exactness; seven tighter than Birkhoff's 17 because ℛ fills the envelope. **Register proof-of-work: R-01.** |
| 47 | §14.5.1 — the Carathéodory number: least c s.t. hull(U) reached from ≤c-subsets = largest irredundant set; for a semilattice with subsemilattices convex, Helly number = height, Carathéodory number = breadth | Math Compendium | OWED | the convexity-space identification; Helly=height / Carathéodory=breadth for Λ's case. **Register: R-03.** |
| 48 | §14.5.8 — seed linear in dimension (2d, 3d, d+3, d+4 on controlled families); seed = Carathéodory number + alphabet cost; breadth of product of d chains = d; compression Λ₈ 89×, Janet 3× | Math Compendium | OWED | the linear laws by branch and bound; the Carathéodory+alphabet decomposition; why the seed cannot be constant. **Register: R-03.** |
| 49 | §14.5.8 — the seed reads the dichotomy: linear law holds while adding counting axes, breaks at coupling axes (counting axis costs little, coupling more); the seed formula is a counting-axis formula; tree-or-tightness costs cells, E, and seed | Math Compendium | OWED | the counting/coupling asymmetry through the seed; SURVIVING result only — withdrawn per-axis numbers are **Register: R-02**, not carried to prose. |
| 50 | §14.5.10 — four corner cells in every sampled seed yet none forced (0 uniquely-covered envelope elements at every cap and Λ₉); stable attractor not forced core; cover 85%, rest to 3 cells; freedom concentrates on g (g ≤ min(q,4f+2), the Pauli term) | Math Compendium | OWED | the not-forced proof; attractor vs necessity; the g-concentration. **Register: R-05.** |
| 51 | §14.5.11 — 519 completions from 66 cells, none universal, min3/med12/max157 (13× spread), heavy-tailed not a tie; corners recoverable (nothing forced), no critical core | Math Compendium | OWED | the completion census; recoverability per position; erasure-code false start withdrawn (**Register: R-05**) |
| 52 | RETIRED — the 219-cover census and the six-condition channel table were a biased randomized sample, REFUTED by exact enumeration (24,585 covers). The surviving content (channel-not-cell; the six as the ℓ≤1 face of the envelope-step law) folds into MC-54 (T1/T3). Not carried to prose. | Math Compendium | RETIRED | superseded by MC-54; see OWED-REGISTER-EXPANSIONS.md correction batch (R 603) |
| 53 | RETIRED — the 'fifth cell / unit template' was a feature of the 219-sample; the unit template appears in only 10% of exact minimum covers (R 604 corrected). Refuted premise (corners 'extremal') — Λ₈ has NO extreme points. Not carried to prose. | Math Compendium | RETIRED | superseded by MC-54/P4; see OWED-REGISTER-EXPANSIONS.md (R 604) |
| 54 | §14.5.12–14.5.14 — the seed's forced structure, PROVEN (supersedes the described bit-pairing): T1 generation criterion (X₀ generates iff it matches every alphabet slot and every envelope step of Λ; the set-cover formulation is exact, 200/200 two-route validated); T2 the alphabet law (every seed witnesses every coordinate at both min and max — "every letter both ways" — cap-independent, proof uses no cap); C2.1 null (q=0) and full (q=k) transitions as corollaries; T3 the envelope-step law (the recorded six channel conditions are the ℓ≤1 face; s→d/d→s element-forced at d-shell; s→s never a step); P4 non-uniqueness located in the literature — Λ₈ has NO extreme points (ℛ(Λ∖{x})=Λ for all 976) yet seed 7, a maximal Krein–Milman failure, which is why 24,585 minimum covers coexist; complement pairings of old §14.5.14 REFUTED at Λ₈ (corner 4 in 14%, unit in 10%) | Math Compendium | DELIVERED (proofs in EXPANSION-MC54.md, Drive 1cRxi76vCe9J_eeF2e6_dmdOU3UZ2AWLn) | full expansion authored by original-works; carry T1/T2/T3/C2.1/P4 verbatim into the Math Compendium. **Register: correction batch in OWED-REGISTER-EXPANSIONS.md (R 602–605).** Prior art: PC-05. |

## Physics Compendium — from §14.1
| P4 | §14.1 — the attribution of Theorem 14.1 and its owners, stated in full as subject matter: Bergman double-projection (sublattice of a product fixed by two-fold projections), Baker–Pixley 1975 (majority term / lattice median), Montanari 1974 (path→global for monotone constraints) and Dechter 1992 (local→global at strong (w*+1)-consistency) as the two owners of the global-consistency result, and Freuder 1982 (backtrack-free search under strong (w+1)-consistency) as a DISTINCT theorem about search order — the two credited apart because they answer different questions; Deville–Barták–Van Hentenryck 1999 (staircase / connected row-convex closed under composition/intersection/transposition) | Physics Compendium | OWED | the full attribution chain written out; the precise statements of the Montanari/Dechter global-consistency theorems vs Freuder's backtrack-free-search theorem, so the apart-crediting is defensible on the mathematics. NOTE: the book's own PRIOR mis-citation (having cited Freuder for Dechter's result) is NOT reader content — it is Register proof-of-work, R-04. The reader sees only the correct full attribution. |

## token binding additions
- MC-42 → row 42 (Ch14A §14.1 Theorem 14.1 characterisation)
- MC-43 → row 43 (Ch14A §14.2 closure operator / closure defect)
- MC-44 → row 44 (Ch14A §14.3 scope / chain presentation)
- MC-45 → row 45 (Ch14A §14.5 Moore family)
- MC-46 → row 46 (Ch14A §14.5.1 seven-cell seed / set cover)
- MC-47 → row 47 (Ch14A §14.5.1 Carathéodory number)
- MC-48 → row 48 (Ch14A §14.5.8 seed linear in dimension)
- MC-49 → row 49 (Ch14A §14.5.8 seed reads the dichotomy)
- MC-50 → row 50 (Ch14A §14.5.10 stable core / nothing forced)
- MC-51 → row 51 (Ch14A §14.5.11 heavy-tailed completions)
- MC-52 → RETIRED (219-cover sample refuted; folds into MC-54)
- MC-53 → RETIRED (fifth-cell/unit template refuted; folds into MC-54/P4)
- MC-54 → row 54 (Ch14A §14.5.14 five cells as binary)
- PC-04 → row P4 (Theorem 14.1 prior-art provenance + mis-citation correction)

## Physics/prior-art token for the seed forced-structure law
| P5 | §14.5.12–14.5.14 prior art (the attribution block of EXPANSION-MC54.md): Moore 1910 (closure operators, retained root); Baker–Pixley 1975 (binary determination / 2,d-interpolation, T1's licence, already cited); Deville–Barták–Van Hentenryck 1999 (staircase class, already cited); Karp 1972 / Chvátal 1979 (set cover, forced-set half of P4, already cited); Shannon 1938 (binary word reading, retained for the bit-encoding); NEW Edelman 1980 + Edelman–Jamison 1985 (convex geometries / anti-exchange / combinatorial Krein–Milman — the NEGATIVE content of P4: empty extreme-point set with seed 7 = maximal failure, permits 24,585 covers); Dilworth 1940 (uniqueness-under-conditions precursor); Krein–Milman 1940 (classical antecedent) | Physics Compendium | DELIVERED (in EXPANSION-MC54.md) | the full attribution block; Edelman is the load-bearing new citation. No novelty claimed for machinery; the application is the contribution. |

## token binding additions
- PC-05 → row P5 (seed forced-structure prior art; Edelman the new citation)

## New expansion from the Request-3 resolution (1D↔14D bracket system) — Math Compendium
| 55 | §12.11.0.11 / §12.11.0.12 — the bracket-system theorem joining the tower's two ends: the rank-to-chain correspondence r ↦ {ranks below} is, at every consecutive stage Λ_{D+1}→Λ_D, a GAP-FREE INTERVAL with both endpoints monotone (exhaustive, all 199,130 cells; factor.py); the tower's chains form one directed system of monotone brackets χ(Λ₁₃)→…→χ(Λ₈); composing the five stage-brackets contains the direct Λ₁₃→Λ₈ bracket with slack ≤ 2 rank units (§22's outward rule inside the tower); the projection from Λ₁₃ covers ALL of χ(Λ₈) (ranks 3..20, no gap, two routes agree), so the 1D chain is the terminal object of the system and 14D its limit — the strict MAP form is refuted (branching 4,4,6,8,9 ascending) | Math Compendium | DELIVERED (proofs + scripts: 03-1D-lands-inside-14D.md, tower.py/tower2.py/tower3.py/factor.py) | carry the bracket-system theorem; the branching profile as the map-refutation; the composition slack bound; the surjectivity two-route proof. Native language is the bracket, NOT binary (M's single at-extreme bit breaks closure, E=1; lawful form is the two threshold bits, each E=0). Register: Request-3 resolution batch in OWED-REGISTER-EXPANSIONS.md. Prior art likely shares PC-04/PC-05 (staircase/closure) — check at authoring. |

## token binding addition
- MC-55 → row 55 (1D↔14D bracket-system theorem; the tower's two ends joined by a bracket)
