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

# =====================================================================
# BATCH 5 CLOSED — MC-22…26 seated in BUILD61 compendia
# =====================================================================
Compendia state: 32,569 lines (+50 from gate baseline 32,519), 2,410,501 B, md5 a2d0e0bc7e59bd7b117035e387ef4622.
Block: contiguous L14661–14710, source order, immediately before ### `L.chi`.

Entries (all M-approved, all R-FORM, all guarded PASS):
- MC-22 "Transitions compose" (§12.11.0, Proved) — 41,682 pairs/0, 842,206 triples/0 (exhaustive upgrade
  over record's 8,434); category (Eilenberg–Mac Lane 1945). 485/485 g=0 non-composable folded in per M.
- MC-23 "The six axes of the tower" (§12.11.1, Computed) — 6 cardinalities + 6 boxes exact; densities;
  Λ₉′ 1,561 vs 1,654; ℛ(X)=X closure sweep; Racah/Slater/Condon–Shortley/Birkhoff/Freuder.
- MC-24 "Three excluded forms" (§12.11.2, Proved) — particle-hole terms(ℓᵏ)=terms(ℓ^{4ℓ+2−k}) p&d exact;
  max2J(f⁷)=25; half-triangle join-closed/meet-broken 2,862/12,489/40,887/110,229; +parity→1,848@cap6.
- MC-25 "Law versus extent, and what E measures" (§12.11.3/.3.1/.5, Proved) — φ̂=realized 2J_c maxima;
  ** 15,150/45,450 (21.4%/22.8%) — CORRECTED, 2,475 withdrawn; f-below-cap 39,375/70,905. **
- MC-26 "An index whose one prediction is false" (§12.11.6, Proved) — E1 |Δ2J|≤2, remove (0,0)→4 meets
  all (0,0), E=1, cap-independent 4/6/8; Wigner/Dirac/Moore.

FINDINGS carried to handoff:
1. OWED-EXPANSIONS-2 row 22 note (register 230) says "2,475" — STALE. BUILD56 §12.11.5 recomputed to
   15,150/45,450. MC-25 carries the corrected figures. (Confirms handoff's "Drive copy stale for rows 13-21"
   extends in spirit to this register-230 value too, though row 22 itself was authoritative.)
2. MC-22 associativity: record sampled 8,434 triples; verified EXHAUSTIVELY 842,206 triples, 0 failures.

CARRIED (unchanged): MC-22…26 await Register 1.1 numbering (like slips 05–16, B1–B4). Coupling-stage
composability figures (9,450/46,740/127,070) carried from record — rule not in main text/tower.py;
MAIN-gate confirmed verbatim.
# Batch 6 (MC-27…35) — verification ledger. MEASURED unless marked.

## MC-27 (§12.11.0.1) — occupancy clock / definability≠reachability
- objects (source signatures) = 33 ................ MEASURED ✓
- object-pairs joined by a step = 739 ............. MEASURED ✓ EXACT
- steps raising k = 0 ............................. MEASURED ✓
- three SCCs pure in occupancy: 8@k=3, 15@k=2, 10@k=1 ... MEASURED (Tarjan) ✓ EXACT
- tick = k − g .................................... definitional
- census over 2,735,716 = 1654² ordered pairs:
  - lattice-comparable 311,180 = 11.4% ........... MEASURED ✓ EXACT
  - composition-path 675,606 = 24.7% ............. MEASURED (transitive closure) ✓ EXACT
  - in both 9,720 = 0.4% ......................... MEASURED ✓ EXACT
- nine = unique dim where time exists (reg 314/345) ... structural, from source

## MC-28 (§12.11.0.2) — arrow is frame-relative / observation
- (g,G) extended index = 13,775 cells ............ MEASURED ✓ EXACT
- composable pairs (extended) = 2,620,090 ........ MEASURED ✓ EXACT
- raise occupancy 826,950 = 31.6% ................ MEASURED (a.G > a.k over composable pairs) ✓ EXACT
- four arrows X_w (present-count G as target occ), all CLOSED E=0:
  - shell 9,407 ✓  subshell 9,845 ✓  occupancy 5,165 ✓  spin 7,160 ✓  ... MEASURED (double-proj) EXACT
- sum breaks closure (E=1,494>0) .................. MEASURED ✓ (max/min follow, standard)
- one arrow per coordinate, no others ............ from source (reg 352)

## MC-29 (§12.11.0.7) — the decay theorem
- overlap-against-independence, all six exact (MEASURED, arrow-indicator joints on extended index):
  1.466 / 1.222 / 1.107 (d=1); 1.080 / 1.070 (d=2); 1.025 (d=3) ✓ strictly ordered by distance
- mutual information value SET {0.353,0.227,0.199,0.094,0.070,0.020} reproduced EXACTLY on extended
  index (MEASURED, column MI). Row-to-pair labeling carried from record (overlap table fixes pairs).
- theorem (MRF on tree → data-processing → Pinsker |P(A∩B)−P(A)P(B)| ≤ √(I·ln2/2)) — PROVED, carried
- falsifier: Λ₉′ = 1,561 (MEASURED ✓); introduces f–g–2S′ cycle breaking tree-Markov (structural ✓);
  ** 6-of-16 PINNED (MEASURED): MRF test = f ⊥ 2S′ | g over (f,2S′) cells per g-stratum;
     16 tests (2+4+6+4), Λ₉′ gives 6 violations, base Λ₉ tree gives 0. Reconstructed from theorem defn. **

## MC-30 (§12.11.0.8) — past/present/future a path, not a triangle
- overcount 33·4·17 = 2,244 vs 976, defect 1,268, 130% ......... MEASURED ✓ EXACT
- four two-sided cuts ℓ,q,f,g all defect 0; internal degree-2 vertices ... MEASURED ✓ EXACT
  (degrees: n,e,2S leaves; k degree 3; ℓ,q,f,g degree 2 — the only two-sided cuts)
- 97 (past,present) pairs .................................... MEASURED ✓ EXACT
- Markov: one future-set per present; sizes 5/10/15/17; pasts 33/33/23/8; nest 5⊂10⊂15⊂17 ... MEASURED ✓
- tick k−g: 389/540/240 ...................................... MEASURED ✓ EXACT
- two sources 350 (k−q pure) / 350 (q−g pure) / 80 both; transpose (0,1)=270=(1,0),(0,2)=80=(2,0) ... MEASURED ✓
- Pauli minority: 60.2% counting / 29.5% tied / 10.3% shell (704/345/120) ... MEASURED ✓ EXACT

## MC-35 (§12.11.0.8 triangle proof) — M-FLAGGED, load-bearing, FULL representation
- Proof chain, all steps grounded:
  (i) treewidth-1 ⟺ exact closure under ℛ; treewidth-2 ⟹ envelope
      VERIFIED concretely: path P-Q-F E=0; triangle |P-Q|≤F≤P+Q E=168>0 ✓
      Mechanism = Freuder consistency ladder (pairwise vs strong 3-consistency, shortfall one level)
  (ii) a triangle on {past,present,future} would be treewidth 2 — graph fact
  (iii) E(Λ)=0 (gate-confirmed) ⟹ treewidth 1 ⟹ no past–future edge ⟹ PATH
- Tie to three-body shape: register 316 = the treewidth-2/K₃ case (working register, not reader-quoted)
- §18.4 grounds the treewidth result (line 5694: three-body shortfall exactly one level)

## MC-31 (§12.11.0.9) — two indices, and the one that does not exist
- Λ₉ forward 1,654 E=0; rev(Λ₉) 1,654 E=0 ............... MEASURED ✓
- reversal = exchange ends (n,l,k,2S)↔(e,f,g,2S′), q fixed: rev(c)=(e,f,g,q,n,l,k,2S′,2S)
- intersection Λ₉∩rev(Λ₉) = 389, all g=q=k, 23.5% of 1654, E=0 ... MEASURED ✓ EXACT
- intersection is a GROUPOID: 33 objects each with identity, every morphism reverse in set ... MEASURED ✓
- union Λ₉∪rev(Λ₉) = 2,919 ............................. MEASURED ✓
- union join-fail 360,000 / meet-fail 470,625 ......... MEASURED ✓ EXACT
- ** E(union) = 2,857 via ITERATIVE join/meet sublattice closure (converges 2 iters) ✓ EXACT **
  INSTRUMENT NOTE: double-projection (one pairwise pass) gives 2,757 for this union; the true
  ℛ sublattice-closure (iterate join&meet to fixpoint) gives 2,857. For non-tree sets the two can
  differ — ℛ is the iterative closure. Record's 2,857 = iterative closure. (Tree sets: they agree.)

## MC-32 (§12.11.0.10) — every Λ in one table
- the summary table consolidates results verified in MC-23/25/etc.:
  seven stages 976/1,654/1,561/2,535/13,585/70,905/199,130 ... MEASURED ✓ (tower.py + Λ₉′)
  seven boxes 6,912…47,775,744 ................................ MEASURED ✓ (all exact, gate+MC-23)
  E=0 at all seven (ℛ sweep, 47M cells at Λ₁₃) ............... verified via boxes; carried
- ** fill column 14.12/5.98/5.65/2.29/2.05/1.34/0.42% = cells/box ... MEASURED ✓ ALL EXACT **
  fill falls monotonically; surplus (7 bits/cell in Λ₈, §11.1.1) grows at every step
- two gradings part at different heights: composition lost Λ₁₀, exactness lost Λ₁₁;
  Λ₁₀ exact & non-composing; none composes without being exact ... structural (MC-22/23) ✓

## MC-33 (§12.11.0.11) — the fourteenth axis / THE BOUNDARY (M-flagged, load-bearing)
- bits table D=8..13: carried=log₂(box), needed=log₂(cells), surplus=diff
  carried 12.75/14.75/16.75/19.34/22.34/25.51 ✓; needed 9.93/10.69/11.31/13.73/16.11/17.60 ✓;
  surplus 2.82/4.06/5.45/5.61/6.23/7.91 ✓ ... MEASURED ✓ ALL EXACT
- fill ratios stage-to-stage 0.424/0.383/0.893/0.652/0.312 ... MEASURED ✓ EXACT
  ** NOT MONOTONE (crux): monotone-bounded ⇒ limit EXISTS (deduction); ratios not→0 so VALUE
     undetermined. Limit ∈ [0, 0.42%]. That limit=0 does NOT follow. §22.1.2 applies to own tail. **
- fill monotone-decreasing BY CONSTRUCTION (a constrained coord has mean multiplicity < its value
  count, else free; each axis multiplies box more than object) — a LAW not a pattern.
- empty index ∅: ℛ(∅)=∅ so E(∅)=0 closed; Q(∅)=∅ COMPLETE by P19; |J(∅)|=0, 0 bits.
  ** E=0 NECESSARY for completeness, NOT SUFFICIENT for content — every closure test passes on nothing. **
- |J(Λ₈)| = 17 join-irreducibles (excl. bottom (1,0,1,0,1,0,0,0)) ... MEASURED ✓ EXACT
  what distinguishes Λ from ∅ is |J(Λ)|=17 and its surplus, not closure.
- Preface-spine reconciliation: THE BOUNDARY (limit undetermined, null definable, E=0 nec-not-suff)
  grounded from inside the tower — matches the book's spine claim that the method bounds without
  overclaiming. The open limit "is the correct answer rather than a gap."

## MC-33 — FILL-LIMIT RESOLVED (method project, 2026-08-29, verdict C proved; independently re-verified this session)
Method project answered REQUEST-to-method-project-FILL-LIMIT.md. Verdict: outcome (C) PROVED,
(A) negative, (B) settled by counterexample. Independently verified here against tower.py:
- Λ₁₃ g-distribution c(g) = 35,630/72,480/76,140/14,880 ......... MEASURED ✓ EXACT
- fill(Λ₁₃) = 0.416801% (the supremum) ......................... MEASURED ✓ EXACT
- THREE admissible continuations of Λ₁₃ (all E=0, built from the tower's own axis-types):
  · Q (chain t₁≤g, tᵢ≤tᵢ₋₁): ratio→1/4, Σ(1−ratio) diverges → L=0 ......... VERIFIED (4.4e−22% at m=40) ✓
  · P (cap tᵢ≤g repeated): ratio→1, Σ converges → L=14,880/47,775,744=0.031146% ... VERIFIED (0.031147% at m=40) ✓
  · T (translated cap tᵢ≤g+M₀·2ⁱ⁻¹): L→fill(Λ₁₃) from below, never attained ... VERIFIED (→0.9984 as M₀↑) ✓
- admissibility = A.morph (bound is a lattice morphism of stage below, §18.4.1/Birkhoff 1940); E=0 by construction.
  Instrument validated: Λ₈+P¹=Λ₉=1,654, Λ₈+Q²=Λ₁₀=2,535 (reproduces tower stages) ✓; E=0 confirmed.
- P and Q SHARE stage 14 exactly (468,530 cells, ratio 0.5882, fill 0.2452%), PART at stage 15.
  ⇒ the 14th stage does not know which limit it heads for; six built stages could not either; NEITHER can any finite number.
RESULT for MC-33: bracket [0, 0.416801%) is TIGHT — 0 ATTAINED (Q), 0.416801% the UNATTAINED SUPREMUM (T),
right-open. L is UNDECIDABLE from the construction's own admissibility criterion. No multiplicity-vs-value-count
law follows from admissibility. "Existence of L is the law's; its value is the world's" (the physics that stopped at 13).
Files banked in Drive: FILL-LIMIT-FINDING.md, 01-fill-limit.md (slip), fill_limit.py, FILL-LIMIT-RESULTS.txt, tower-1.py.
Self-correction noted in finding: first run piped through head (killed at line 60); rerun to file, no figure changed.

## MC-33 — FILL-LIMIT FROM OUTSIDE (method project, 2026-08-29, companion; independently re-verified)
Second method-project finding (FILL-OUTSIDE-FINDING.md). M asked: can L be bounded from OUTSIDE?
Answer: YES. Outside FLIPS the lower end that inside could not decide.
- PREMISE (doctrine + physics): a fill-lowering axis must be a MEASUREMENT (new independent label),
  not a RELABEL — Thm 11.1, §32.1.4, the four operations (RELABEL adds none). Physics: a bound atomic
  transition under §7.4 caps has FINITELY many independent labels (2 multiplets, 1 nucleus I, 1
  projection each; Condon-Shortley 1935, Cowan 1981). 
- THEOREM (outside): finitely many axes have ratio<1 ⟹ Σ(1−ratio) is a FINITE sum ⟹ L = fill(D_last) > 0.
  ** L = 0 EXCLUDED from outside (was admissible from inside). The tower has no limit; it has a LAST STAGE. **
  Closure couldn't see this — closure never gives reference, can't tell measurement from repetition
  (every route to 0 = continuation Q = repeats).
- EXHIBIT (the named next rung, verified this session against tower.py):
  Λ₁₃ 2J-distribution 27,170/40,755/38,220/33,150/25,545/17,940/10,585/4,605/1,160 ... ✓ EXACT
  axis 14 = 2F: window max(0,2J−2I_max)≤2F≤2J+2I_max on single parent 2J (Casimir 1936 hyperfine F=J⊗I)
  axis 15 = m_F: cap 0≤m_F≤2F on single parent 2F
  Both single-parent monotone ⟹ morphisms ⟹ CLOSE (E=0; independently confirmed window closes E=0).
  Exact triangle |2J−2I|≤2F≤2J+2I is a sum+parity bound → FAILS (E>0), per E3 + §12.11.6.
  fill14/fill15 table VERIFIED EXACT for I=0,½,1,2,4,7:
    I=0:   fill15=0.018416% (2F=2J is a RELABEL, not an axis — ladder resumes at I≥½)
    I=½:   fill15=0.044752%  (upper end ≤0.0448%)
    I=7:   fill15=0.130061%  (upper end ≤0.1301%, I=7 = largest ground-state spin among primordial nuclides)
  ** Under any cap I≤7 the two rungs take the upper end from 0.4168% to at most 0.1301% (0.0448% at I=½). **
  As I_max→∞, F-rung ratio→1 (translated-cap T behaviour), fill15/fill13→½: bracket improves by factor >2
  under every cap, >3.2 under every physical one.
- 2I_max is a DECLARATION about the world (of Z=120's kind), M's to make.
- REFUSED (M's ruling, new subject-matter): the VALUE of L (needs ladder named+capped); the parent side
  of the cylinder (whether parent owed rungs, whether J_c carries parent's J); the two-parent §12.11.6 rung.
  Each rung ruled-in lowers fill(D_last) by a known factor; NONE can make it zero.
- VERDICT SPLIT: proved(outside) L>0=fill(D_last), Σ finite; computed(cap-conditional) L≤0.1301% for I≤7;
  refused a value/lower-bound until rungs ruled.
Files: FILL-OUTSIDE-FINDING.md, 02-fill-outside.md (slip), fill_outside.py, FILL-OUTSIDE-RESULTS.txt, tower-1.py.

## MC-33 — FILL-LIMIT VALUE (method project, 2026-08-29, third finding; independently re-verified)
Third finding (FILL-VALUE-FINDING.md). M asked: can we get a value ruling? Record consulted first.
- RECORD RULES OUTRIGHT: rungs are one-parent envelopes (§12.11.5/reg 358 declined two-parent K;
  §12.11.6 selection-rule bridge is two-parent → NOT a tower axis). Every rung one parent + declared cap.
- RECORD GIVES EVIDENCE: J_c already carries the source shell's J-range (φ̂(k) = envelope of parent
  shells' max 2J); the record's world is field-free (NIST levels; §12.11.6 rule written in J not M).
- RECORD SILENT: nuclide chart is (Z,N)+AME2020 masses — NO nuclear spins in the record.
- 12 combinations computed (cap 2I_max∈{14,18} × source∈{none,F_s-on-J_c,J_s+F_s} × proj∈{no,yes}),
  over joint (k,2Jc,2J) distribution of Λ₁₃ (91 classes, 199,130 cells) — ALL VERIFIED EXACT this session:
    min L = 0.047399% (cap14, J_s+F_s, proj, D_last=18)
    max L = 0.333117% (cap18, F_t alone, D_last=14)
  ** BRACKET TIGHTENS from [0, 0.4168%) to [0.047%, 0.333%] on premise: remaining physics among named
     rungs with I≤9. Field is largest factor (0.19-0.42); source side 0.76-0.81; cap 5-11% within a row. **
  Most record-consistent row (primordial cap, J_c=source J, field-free): L=0.283507% (I=7) / 0.302400% (I=9),
  D_last=15 — a READING of the record, becomes the value only on M's word.
- ** PROVENANCE FLAG (unresolved): the two spin caps I=7 (¹⁷⁶Lu) and I=9 (primordial isomer ¹⁸⁰ᵐTa) are
     cited from MEMORY, network disabled. MUST confirm vs NUBASE/NIST nuclear-moments before either cap
     declared. My network also disabled — cannot verify. VALUE of L depends on this; existence/bracket do not. **
- RULING (M's, subject-matter): cap 14 or 18 · source rungs none / F_s-on-J_c / J_s+F_s · projections no/yes.
Files: FILL-VALUE-FINDING.md, 03-fill-value.md (slip), fill_value.py, FILL-VALUE-RESULTS.txt, tower-1.py.

## MC-33 STATUS: seated version says "undecidable from inside." NOW SUPERSEDED by 3-part arc:
  inside (undecidable) → outside (L>0, last stage) → value (bracket [0.047%,0.333%], value = 1 ruling).
  MC-33 needs REVISION to carry the outside result at minimum. The VALUE awaits M's ruling + spin verification.

## MC-34 (§12.11.0.12) — how an index enters a larger index
- Λ₁₃ → 44 rank values (min-subtracted rank, 0..43) ............ MEASURED ✓ EXACT
- 17.60 bits (log₂ 199,130) → 5.46 bits (log₂ 44) ............. MEASURED ✓
- 12.14 bits/cell lost; compression 4,526:1 (199,130/44) ...... MEASURED ✓ EXACT
- 31% survives = 5.46/17.60 bits ratio ........................ MEASURED ✓
- Λ₉ → 21 rank values; fibres 1 to 185 ........................ MEASURED ✓ EXACT
- composition reduced to rank: 264 distinct (rank a, rank b) inputs ... MEASURED ✓ EXACT
- 17% (46/264) determine a single output rank ................. MEASURED ✓ EXACT
- worst spread 12 output ranks from one input pair ............ MEASURED ✓ EXACT
- ** composite rank range [3,23]: RAW COORDINATE-SUM scale (not min-subtracted; offset=Σmins=3).
     My min-subtracted scale gives [0,20]; raw-sum gives [3,23] exactly. Span 20 either way. PINNED. **
- structural claim (a transition from one coord up is an INTERVAL of width up to 12, not a point) ... VERIFIED
- 'every branch terminates in a cell of Λ₉' — branching is INSIDE the index; loses resolution not access.

# =====================================================================
# BATCH 6 CLOSED — MC-27…35 seated in BUILD61 compendia
# =====================================================================
Compendia: 32,659 lines (+90 from gate baseline 32,519; B5 +50, B6 +90 = 140 total this session),
md5 2603fc1bca3b47116a70a1432924139b.
Block: contiguous L14711–14799, working ROW order (reorder to main-volume physical order = FINAL step).

Nine entries (all M-approved, all R-FORM, all guarded PASS):
- MC-27 "The occupancy clock, and definability is not reachability" (§12.11.0.1, Computed)
- MC-28 "The arrow is a property of the assumption" (§12.11.0.2, Computed)
- MC-29 "The arrows decay with distance" (§12.11.0.7, Proved) — 6-of-16 falsifier PINNED
- MC-30 "Past, present and future" (§12.11.0.8, Proved)
- MC-35 "Exactness proves the three parts are not a triangle" (§12.11.0.8, Proved) — M-flagged, full proof
- MC-31 "Two indices, and the one that does not exist" (§12.11.0.9, Proved) — E(union) via iterative closure
- MC-32 "Every stage of the tower in one table" (§12.11.0.10, Computed)
- MC-33 "The fourteenth axis, and the tower's last stage" (§12.11.0.11/§17.1/§18.4.1, Proved) — M-flagged,
  FULL ARC: inside undecidable + door/closure separation + Last-Stage theorem + value L=0.283507%(I=7)/0.302400%(I=9)
- MC-34 "How Λ enters a larger index" (§12.11.0.12, Computed)

NEW THEOREMS extracted (logged to DEFERRED-REGISTER-ITEMS.md for the Register pass):
  1. THE LAST-STAGE THEOREM: tower has no limit, has a last stage, L=fill(D_last)>0 (given finite-labels premise).
  2. THE DOOR/CLOSURE SEPARATION: closure admits relabels but the door excludes them; fill-decrease can't
     distinguish measurement from relabel — why the limit is undecidable from inside.
  CORRECTION recorded: "ratio<1 marks a measurement" is FALSE (non-constant relabel has ratio 1/V<1).

FILL-LIMIT RESOLUTION (3 method-project findings, all independently re-verified against tower.py):
  inside (undecidable, [0,0.4168%) right-open) → outside (L>0, last stage) → value ([0.047%,0.333%], L≈0.284%).
  Provenance of nuclear-spin caps (I=7 176Lu, I=9 180mTa) ACCEPTED per M (verified by originating project).

CARRIED: B5+B6 tower block awaits (1) reorder to main-volume physical order + (2) [MC-NN] token resolution
— both at the FINAL renumbering step, one pass. Deferred Register items (3 total) append at Register pass.
# RULING (M, chat 61) — ORDERING & RENUMBERING

## Canonical compendium order: MAIN-VOLUME PHYSICAL ORDER (reader-friendly).
The finished compendium presents entries in the order their sections physically appear in the
main volume — NOT row/batch order. For the tower this means the time sections (§12.11.0.1–.0.12,
MC-27…35) sit BEFORE the axes/forms/dichotomy (§12.11.1/.2/.3, MC-23/24/25), which sit before
one-prediction-false (§12.11.6, MC-26).

## BUT: reordering + renumbering is a LAST STEP.
Physical reordering to main-volume order, and the [MC-NN] → §-citation token resolution, happen
ONCE at the end, after ALL subject matter is settled. We do NOT reorder as each batch lands —
that would repeat the task every batch.

## Consequence for the build-out phase (NOW):
- Entries are AUTHORED and INSERTED in row/batch order (MC-22, 23, … sequentially), appended as a
  growing contiguous tower block, exactly as done for B5 and B6-so-far. This is a WORKING order.
- The working order is provisional. It is NOT the final reading order.
- At the FINAL reordering step: the whole tower block is re-sequenced into main-volume physical order
  and tokens resolved, in one pass, verified by a single measured-diff guard.

## What this means for what is already seated:
- MC-22…26 (B5) and MC-27, 28, 29, 30, 35 (B6-so-far) are CORRECTLY seated for the working phase.
  Nothing needs to move now. They will be reordered at the final step.
- Continue B6 (MC-31, 32, 33, 34) in row order, appending to the block.

## Final-step reorder target (recorded now so it is ready, executed later):
Main-volume physical line order of the tower sections:
  §12.11.0    MC-22  Transitions compose
  §12.11.0.1  MC-27  occupancy clock
  §12.11.0.2  MC-28  arrow is a property of the assumption
  §12.11.0.7  MC-29  arrows decay with distance
  §12.11.0.8  MC-30  past, present and future
  §12.11.0.8  MC-35  exactness proves not-a-triangle
  §12.11.0.9  MC-31  two indices
  §12.11.0.10 MC-32  every-Λ table
  §12.11.0.11 MC-33  fourteenth axis
  §12.11.0.12 MC-34  entering a larger index
  §12.11.1    MC-23  the six axes
  §12.11.2    MC-24  three excluded forms
  §12.11.3    MC-25  the dichotomy
  §12.11.6    MC-26  one prediction false
(MC-36/37/38 EM-index, §12.11.8, follow after MC-26 — from B7.)
# DEFERRED REGISTER ITEMS — to be appended at the Register pass (not now)

## R-item: fill-limit undecidability (from MC-33 / method project 2026-08-29)
- Content: The tower's fill converges to L ∈ [0, 0.416801%]; L is UNDECIDABLE from the construction's
  own admissibility criterion (A.morph, lattice-morphism bounds, §18.4.1). Bracket tight & right-open:
  0 attained (chain-of-caps continuation Q), 0.416801% the unattained supremum (translated-cap T);
  repeated-cap P gives L=14,880/47,775,744=0.031146%. Three admissible continuations of Λ₁₃ (all E=0,
  built from the tower's own axis-types) reach three different limits. No multiplicity-vs-value-count
  law follows from admissibility: (A) negative, (B) counterexample, (C) certified-open PROVED.
  "Existence of L is the law's; its value is the world's" — decided by physics that stopped at 13.
- Cites: §12.11.0.11, register 333.
- Append-only. New entry (does NOT modify 333; cites it). Number assigned at Register pass.
- Provenance: method-project finding FILL-LIMIT-FINDING.md + slip 01-fill-limit.md (banked in Drive),
  independently re-verified in chat 61 (see MC27-35-verification.md).
- Reader-facing home: MC-33 (seated in compendia). This Register entry is the subject-matter proof-of-work record.

## R-item: THE LAST-STAGE THEOREM (new, from MC-33 full arc)
- Statement: The tower has no limit; it has a last stage D_last, and L = fill(D_last) > 0.
- Proof skeleton: (1) an axis must pass the door = be an independent degree of freedom (§17.1);
  (2) a relabel is dependent → fails the door → not an axis; (3) so every tower axis is a measurement;
  (4) PREMISE (prior-art physics): a bound atomic transition under §7.4 caps has finitely many
  independent labels (Condon-Shortley 1935, Cowan 1981); (5) ∴ finitely many axes → last stage,
  L = fill(D_last) > 0. Provable from OUTSIDE (needs 4), not inside (no reference).
- Cites §12.11.0.11, §17.1, register 333. Distinct from the inside undecidability result.
- Value (M's ruling, record-consistent): L = 0.283507% (I=7) / 0.302400% (I=9), D_last=15.
- Append-only. Number at Register pass.

## R-item: THE DOOR/CLOSURE SEPARATION (new structural principle, from MC-33 full arc)
- Statement: Admissibility (closure) admits relabels — they close, E=0 — but the door (§17.1) excludes
  them. A fill-lowering relabel is barred at the door, not at closure. Hence closure alone cannot
  distinguish a measurement from a relabel (both lower fill: a relabel inflates the box while leaving
  cells fixed), which is exactly why the fill-limit is undecidable from inside (from admissibility alone).
- Verified computationally: a relabel (t:=k) leaves cells fixed, inflates the box, closes (morphism,
  E=0), and lowers fill — yet fails the door. Cell-count is preserved by a relabel, increased by a measurement.
- NOTE (correction, recorded): "ratio < 1 marks a measurement" is FALSE — a non-constant relabel has
  ratio 1/V < 1 too. The measurement/relabel line is the DOOR (independence), NOT the fill ratio.
- Cites §17.1, §14.1, §32.1.4, §12.11.0.11. Append-only. Number at Register pass.
