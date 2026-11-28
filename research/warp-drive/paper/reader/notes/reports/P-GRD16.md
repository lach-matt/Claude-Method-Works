# P-GRD16: writer's report (sec:tl5-hfk; the C₁ lever of 𝔨_rec^p)

Writer's report as handed back (saved here by the coordinator). The main lever is proved in part: the parts of the
C₁ bound that are one number for all seven fields, and the couplings, take a weighted constant; the leading family
terms keep the factor K_rec, and the exact obstruction for them is recorded.

**File:** research/warp-drive/paper/reader/proofs/P-GRD16.md, md5 31c985083f6805f0c092efaf5e76932d, 397 lines.
Base: HEAD 5d38849f, chapter md5 6b249255 (7837 lines by `wc -l`, ending with a newline). Drafted under
scratchpad/reader/pgrd16/ (tools copied from pgrd15/tools and adapted, orig/ from 5d38849f).
- Layout: chapter text 1–198 (11 labels), Placement 200–222, Comparison 224–381, Crosswalk 383–397.
- Assembled: Section 57.31; Lemma 57.250 (lem:tl5-hfk-rec), Lemma 57.251 (lem:tl5-hfk-fam), Definition 57.252,
  Theorem 57.253, Remark 57.254; displays (57.175)–(57.179).
- Index letter k. A_k, B_k, η_k, Y_k, ε^k, 𝔯^k, S_F^k, C₁^k, 𝔨_rec^k and 𝔷^k occur nowhere else in chapter 87. New
  symbols: 𝒳_p, |·|_Γ, 𝔨_Γ.
- Two clashes a reader may flag: k is also the frame metric of def:tl5-hf-frame (written k̂ in norms); 𝔫 was avoided
  because of 𝔫_Φ in the proof of lem:tl5-hfq-theta.

## 1. The main lever: proved in part

**Where K_rec comes from.**
- In the proof of lem:tl5-hf-recovery (87:4060–4064), X^½ is exactly |𝒳_p(D̂ℒ_ZΨ − 𝔷_(Z,·))_Z|, with 𝒳_p the map
  (v_Z) ↦ (|T|⁻¹v_T, (Σc^ab_j v_(K_ab))_j). Only after that is it bounded by K_rec times the family norm.
- lem:tl5-hfz-rec uses X only through that bound (87:6422–6423). lem:tl5-hfp-rec (87:6816–6820) bounds the family
  through eq:tl5-hfp-family with 𝔚 = Γ.

**The route.** |T(p)|⁻¹ and c^ab_j(p) are numbers, so eq:tl5-hfe-face applies to the four fields
Ã₀ = |T(p)|⁻¹D̂Ψ_T and Ã_j = Σc^ab_j(p)D̂Ψ_(K_ab). On the face, lem:tl5-hf-fields (a) gives
Σ_i|ℒ^JÃ_i|² ≤ |T(p)|⁻²|ℒ^JD̂Ψ_T|² + λ_M(p)⁻¹Σ|ℒ^JD̂Ψ_(K_ab)|². No new energy bound is needed.

Through lem:tl5-hfp-c1 (87:6772–6802) and lem:tl5-hfp-words (87:6744–6758), term by term, each part is of one of
three kinds:
- **First kind** (factor K_rec(p); no gain, no loss): bounds forming a family over the pairs (J, Z), bounded in the
  Euclidean norm. These are the leading terms D̂Ψ_(JZ), the remainders R′ and D̂R′, the face recovery's leading term
  through Z′JZ, and its terms with 𝔷 and 𝔯_♯.
- **Second kind** (gains): bounds that are one number for all seven fields, namely the nonlinear part
  𝔵^z(…)/(1 − 𝔵^z), the part with ϱ, and the terms on S_a. They take 𝔨_Γ := (|T|⁻² + 6λ_M⁻¹)^½ in place of √7K_rec.
- **Third kind** (gains): the couplings 𝔄. They take 𝔞_𝔄^k, the operator norm of their map with weighted rows, which is
  at most K_rec𝔞_𝔄(Γ).

**Correction to the previous scoping.** P-GRD15's "Not done" said a weighted bound needs the face energies split by
last letter. That is true only for a gain on the first kind, which is bounded by K_rec(p) times its present bound
without any split. So the gains on the second and third kinds are proved.

**The obstruction for the first kind** (exact; nothing drafted for it).
- What is needed is |T|⁻²E_T + λ_M⁻¹E_R, with E_T and E_R the face energies of the words ending in T and in a
  rotation.
- Every bound in the chapter sees the face energies only through ℰ_g(p) (87:6794, 87:7720), and ℰ_g(p) ≤ e^φY_s²
  (87:7604–7605, 87:7802), with Y_s the single bootstrap quantity Σ_Iμ^|I|ℰ_I (87:6241–6243).
- Given only E_T + E_R ≤ ℰ_g, the supremum is K_rec²ℰ_g, attained with all the energy on words ending in T.
- **What would be needed:** a bound of E_T by a fraction of ℰ_g(p), or a bootstrap weighted by last letter. The second
  means restructuring Steps 2–3 and prop:tl5-hf-linear-n:
  - in lem:tl5-hf-system (87:4028–4031), the commutator terms with k < j keep the last letter, but those with k = j
    carry π^(Z_j) and change it;
  - the nonlinear terms mix all subwords;
  - δ_w and s_N would carry the weights. If the forcing sits on the words ending in T, A grows by the factor by which
    B falls (a deduced sketch).
- No report measures the split of the energies or of the forcing by last letter.

## 2. Labels, containment, checks, crosswalk

**Labels (11):** sec:tl5-hfk, lem:tl5-hfk-rec, eq:tl5-hfk-rec, lem:tl5-hfk-fam, eq:tl5-hfk-fam, def:tl5-hfk-constants,
eq:tl5-hfk-krec, eq:tl5-hfk-constants, thm:tl5-hfk, eq:tl5-hfk-closing, rem:tl5-hfk-what.

- **lem:tl5-hfk-rec:** (a) |𝒳_p x| ≤ |(|x_Z|)|_Γ ≤ K_rec|x|, with 𝔨_Γ ≤ √7K_rec and 𝔷₁^k, 𝔷₂^k ≤ K_rec𝔷₁′, K_rec𝔷₂′;
  (b) |D̂²Ψ| ≤ 𝔨_♯(𝔥)(|𝒳_p(D̂ℒ_ZΨ)_Z| + 𝔷₁^k|D̂Ψ| + 𝔷₂^k|Ψ|) + (1 − 𝔥)⁻¹(|𝔣| + 𝔯_♯|Ψ|).
- **lem:tl5-hfk-fam (N = 4):** |𝒳_p(D̂Ψ_Z(p))_Z| ≤ μ⁻²C₁^kℰ_g^½ + 𝔨_Γ(wC_(1,ϱ)^lϱ(p) + E₀), with C₁^k = K_rec(p)
  times C₁^(Γ,l) formed with 43^½𝔨_Γ/K_rec in place of 301^½ and 𝔞_𝔄^k/K_rec in place of 𝔞_𝔄(Γ); C₁^k ≤ K_rec C₁^(Γ,l).
- **def:tl5-hfk-constants:** 𝔨_rec^k = 𝔨_♯(C₁^k + 𝔷₁^kμ^½C₁^l + 𝔷₂^kμC_S^h) + (1 − 𝔰₁^v)⁻¹μ𝔯_♯C_S^h;
  𝔨_rec^(ϱ,k) = 𝔨_♯(𝔨_Γ + 𝔷₁^kμ^½)C_(1,ϱ)^l; 𝔨_rec^(0,k) likewise. These go into C_P^v, C_(P,ϱ)^v and C_(P,0)^v and every
  constant formed from them; ε^k = ε^f (route (𝔰)); η_k, A_k, B_k, Y_k, 𝔰_*^k as with index f.
- **thm:tl5-hfk (N = 4):** under the hypotheses of thm:tl5-hff with these constants and the closing condition
  4η_k^(−3/2)(δ_w + η_k^(−½)(ε^k + ε_M^k))(S_F^k + S_M^k) < 1, a solution with Y_σ ≤ Y_k.

**Containment.** The section adds no new choice. For all admissible choices every constant with index k is at most
its index-f counterpart, so η_k ≥ η_f, A_k ≤ A_f, B_k ≤ B_f, Y_k ≤ Y_f and 𝔰_*^k ≤ 𝔰_*^f, and the hypotheses of
thm:tl5-hff at N = 4 imply those of thm:tl5-hfk (the last claim of the theorem and the last paragraph of its proof).
Equality holds when |T|⁻¹ = λ_M^(−½). No earlier text is edited, so every earlier closing condition stays valid. The
new constants enter both 𝔰_* and the closing condition (through S_F, 𝔎 and 𝔎^D, and through 𝔯).

**Checks** (fresh scratch tree with the section merged, run with the repository copy):
- `lint.py --chapters`: 62 files, 5342 labels, 0 hits;
- `assemble.py --check`: 0 problems;
- in-memory assembled lint: `[] 0`;
- numbering: 0 of 5331 existing numbers change, 11 added;
- merged crosswalk: 491 rows for 491 labels, in order, ASCII;
- chapter text at most 120 characters, also after labels resolve; the pointer line is 119 (116 resolved); no
  forbidden line starts; notes at most 121.

**Crosswalk rows** (paper/reader/proofs/P-GRD16.md@PENDING:<line>): sec:tl5-hfk 1, lem:tl5-hfk-rec 23,
eq:tl5-hfk-rec 37, lem:tl5-hfk-fam 57, eq:tl5-hfk-fam 66, def:tl5-hfk-constants 115, eq:tl5-hfk-krec 122,
eq:tl5-hfk-constants 137, thm:tl5-hfk 139, eq:tl5-hfk-closing 143, rem:tl5-hfk-what 177.

## 3. Deduced gains (upper figures; every supremum at one point; G0q figures are on P-GRD14)

Seed 1 D_A / seed 2 D_A / seed 1 D* / seed 2 D*.
- **The fall of the C₁ term:** at most G0q's "equal shares" figures, 0.31 / 0.29 / 0.20 / 0.20 decades, wherever the
  𝔞_𝔄 part is negligible, and in any case at most the "floor" figures, 0.46 / 0.44 / 0.26 / 0.26. The first kind keeps
  its size, so this is an upper figure only. On 𝔩_D(Γ) alone, with G0p's 𝔵^z, the fall is 0.14 / 0.11 / 0.13 / 0.13;
  where the |∂_γ|² part leads at the optimal 𝔲₁, C₁ falls by half the fall of 𝔩′.
- **Through the theorem, alone:** at most the C₁ term ÷ 2 price, +0.09 / +0.24 / +0.06 / +0.29. At seed 1 this is
  already capped by 𝔤₁C_S, which takes the supremum back after a fall of 0.098 / 0.185.
- **With C_P⁰ also falling by 0.30:** at most the "both together" price, +0.26 / +0.25 / +0.30 / +0.29.
- 𝔨_rec^(ϱ,k) and 𝔨_rec^(0,k) fall by the equal-shares figure on their 𝔨_Γ parts; their effect is not priced.

## 4. Optional levers

- **|H| ≤ |h|/(1 − |h|) in place of 𝔤₁:** not drafted; at most log₁₀(1 + 𝔰_♭), 0.0043 decades at 𝔰_♭ = 10⁻², about
  4 × 10⁻⁵ at 10⁻⁴.
- **The 𝔨₁ Cauchy–Schwarz sharpening:** not drafted; moves C_S by at most ¼log₁₀3 = 0.12 decades, and C_S does not hold
  the supremum at level 4.
- **Level 6 (k₁𝔐_p): scoped, not drafted; possibly the largest lever left.**
  - The level-6 step bounds every first-order term of the recovery of D̂²Ψ_B through L_g, the norm of all words of
    length ≤ m + 1 (87:5185–5193, 87:5585–5590, 87:6822–6834).
  - The leading term needs only the seven words ZB, which lem:tl5-hfk-fam's proof covers. So k₁𝔐_p could become
    𝔨_♯C₁^k({ZB}) plus the 𝔷 and 𝔯_♯ terms plus (1 − 𝔰₁^v)⁻¹α_𝔄𝔐_p, for both options of def:tl5-hft-constants. Not
    cheap to write.
  - k₁𝔐_p leads C_P^v at level 6 by 0.79–1.39 over 𝔤₁C_S; 𝔰_* sets ε there, 3.45–5.82 decades below the closing;
    𝔐_p^(2)/C₁ = 0.92–1.29 decades.
  - The deciding numbers are not reported: α_𝔄's share of k₁ at level 6, and C₁^l({ZB}) against 𝔐_p^(2).

## 5. Left open

- The first kind (§1): energies split by last letter, or a weighted bootstrap.
- The level-6 term-by-term recovery above.
- The rotation part of 𝔨_Γ² taken as min(6λ_M⁻¹, Σ|Σ_j c^ab_j c^cd_j|): at most 0.12 / 0.13 / 0.22 / 0.23 decades on
  the second kind.
- The 𝔷 terms of the face recovery; their gain carries a factor μ^½.
- For G0r or G0s to measure: the split of C₁^(Γ,l) by kind at the supremum, including 𝔞_𝔄's share; a re-chosen 𝔲₁ for
  C₁^k.
