# P-GRD17: writer's report (sec:tl5-hfn; the level-6 step at low levels, word by word)

Writer's report as handed back (saved here by the coordinator). Lever A is proved, for every m ≤ N − 4, both options and
both routes, and drafted. Its secondary part, round 16's weighted image applied to the seven-word family at N ≥ 6, is
proved as well and included. Lever B has no honest route; the obstruction is recorded below. Lever C is scoped only and
not drafted.

**File:** research/warp-drive/paper/reader/proofs/P-GRD17.md, md5 10d83c5cc91169a32fb89658a1aa7f3f, 396 lines, copied
once from the scratchpad.
- Base: HEAD f76dfef5, chapter md5 2a102936, 8038 lines.
- Drafted under scratchpad/reader/pgrd17/: the tools are copied from pgrd16 and adapted, and orig/ is extracted from
  f76dfef5. The sources src.md, rest.md and ptr.txt rebuild the file.
- Layout: chapter text 1–186 (10 labels), Placement 188–211, Comparison 213–381, crosswalk 383–396.
- Assembled numbering: Section 57.32; Lemma 57.255 (lem:tl5-hfn-fam), Lemma 57.256 (lem:tl5-hfn-low), Definition 57.257,
  Theorem 57.258, Remark 57.259; displays (57.180)–(57.183).
- Index letter **n**. A_n, B_n, η_n, Y_n, S_F^n, 𝔯^n, ε^n, 𝔰_*^n, 𝔐_n and 𝔨_rec^n occur nowhere else in chapter 87.
  - Rejected letters: m (Y_m is taken at 87:4950), j (A_j and B_j at 87:5699), o (E_o, a_o, 𝔣₂^o), and b, r, h, e.
  - The chapter text never uses n as a word count; it writes 301^(1/2) and "seven words".
  - A reader may still flag n against 𝔠_n and against "(43n)" in the cited lemmas.
- 𝔨_B was avoided because it is already taken in lem:tl5-hfs-products.

## 1. Lever A: proved

**Scoping, as mathematics** (lines at f76dfef5):
- **What 𝔰_g^(m) is.** It is a maximum over the words (def:tl5-hfg-graded, 87:5051–5052). So the step on second
  derivatives at low levels bounds a supremum: each D̂²Ψ_B(p), |B| ≤ m, through its own recovery at p. Nothing is summed
  over B.
- **What that recovery needs** (lem:tl5-hf-recovery 87:4040–4076, lem:tl5-hfz-rec 87:6408–6438, 𝔣 at 87:4332–4333):
  - D̂ℒ_ZΨ_B = D̂Ψ_(ZB): the seven words ZB, in the leading term;
  - D̂Ψ_B and Ψ_B, in 𝔷_Z and in 𝔯_♯|Ψ_B|;
  - the couplings 𝔄_BJ.
- **Only the couplings bring in other words.**
  - def:tl5-hf-coupling (87:4077–4098) replaces every D̂²Ψ_J (|J| < |B|) of the commutator terms of eq:tl5-hf-system by
    ℛ_p, recursively over the shorter words.
  - So 𝔄_BJ acts on jets of words with |J| ≤ |B|, and 𝔄_∅J = 0.
- **The old step.** It bounds all these jets by one number, L_g, the jets of all words of length ≤ m + 1 (87:5187–5188,
  87:5585–5588). lem:tl5-hfp-low (87:6827–6832) then bounds L_g by 𝔐_p^(m). That gives the entry k₁^(m,μ,p)𝔐_p^(m) of
  C_(∞,μ)^(m).

**What was proved.**
- **lem:tl5-hfn-fam** (N ≥ 6, |B| ≤ N − 4, ΓB := (ZB)_Z):
  - |𝒳_p(D̂Ψ_(ZB)(p))_Z| ≤ μ^(−(|B|+4)/2)C₁^k(ΓB)ℰ_g^½ + 𝔨_Γ(wC_(1,ϱ)^lϱ + E₀).
  - C₁^k(ΓB) is K_rec(p) times C₁^l(ΓB), formed with 43^½𝔨_Γ/K_rec in place of 301^½ and with 𝔞_𝔄^k(ΓB)/K_rec in place
    of 𝔞_𝔄(ΓB).
  - C₁^k(ΓB) ≤ K_rec C₁^l(ΓB).
  - The proof is that of lem:tl5-hfk-fam, applied to the words JZB, Z′JZB and σZB. The three kinds are checked one by
    one.
- **lem:tl5-hfn-low.**
  - 𝔨_rec^n(B) := 𝔨_♯(C₁^k(ΓB) + 𝔷₁^kμ^½C₁^l({B}) + 𝔷₂^kμC_S^f) + (1 − 𝔰₁^v)⁻¹μ𝔯_♯C_S^f, with C_S^h for B = ∅.
  - 𝔐_n^(m) := max_(|B|≤m) 𝔨_rec^n(B) + (1 − 𝔰₁^v)⁻¹α_𝔄^(m,μ)𝔐_p^(m).
  - The step holds with 𝔐_n^(m) in place of k₁^(m,μ,p)𝔐_p^(m) in its part with ℰ_g. Its parts with ϱ and η₀ are kept,
    because the new ones are proved to be at most the old: (2𝔐^(m))^½ ≥ 4, 𝔨_Γ ≤ √7K_rec, 𝔷₁^k + 𝔷₂^k ≤ √2K_rec𝔷′, and
    ν′ = μ, or ν′ = 1 in lem:tl5-hft-small (a).
  - 𝔐_n^(m) ≤ k₁^(m,μ,p)𝔐_p^(m). This uses C₁^l(𝔚′) ≤ C₁^l(𝔚) for subfamilies, proved there: restricting the map of 𝔞_𝔄
    has norm at most 1, and the integrands are monotone.
  - For B = ∅, 𝔨_rec^n(∅) has the form of 𝔨_rec^k.
- **def:tl5-hfn-constants and thm:tl5-hfn** (N ≥ 6, either route):
  - 𝔐_n^(m) replaces the entry in C_(∞,μ)^(m) for every m ≤ N − 4. So it reaches both 𝔐_p^(1), through C_P^♮ (hence 𝔎,
    𝔎^D, S_F and the closing condition), and 𝔐_p^(2), through the term of 𝔰_* with A.
  - ε^n := ε^f.
  - The closing condition is 4η_n^(−3/2)(δ_w + η_n^(−1/2)ε^n)S_F^n < 1.
- The coupling term keeps 𝔐_p^(m).

## 2. Lever B: not proved; the obstruction

- **Where the factor sits.** Kind 1 is 69–71 % of C₁^(Γ,l). It is bounded through 𝒟_g and 𝒥_g over the pairs (J, Z), and
  𝒳_p weights it by the last letter Z. It therefore needs |T|⁻²E_T + λ_M⁻¹E_R.
- **The energies.** The chapter sees face energies only through ℰ_g(p) ≤ e^φY_s² (87:6794, 7720, 7604–7605, 7802). With
  only that bound, the supremum is K_rec²ℰ_g.
  - Needed: E_T ≤ θℰ_g(p) at the supremum, with θ < 1.
- **The bootstrap quantity.** Needed: a bootstrap split by last letter, carried through prop:tl5-hf-linear-n
  (87:4099–4122).
  - The commutator terms with k = j change the last letter, and π^T ≠ 0 in general.
  - With constant weights, the recovery gains max(|T|⁻²/w_T, λ_M⁻¹/w_R), but every other use of ℰ_g pays 1/min(w). It is
    zero-sum unless the energy and forcing split is known, and no report measures it.
- **The transport split by letter.** The weights act on the last letter Z, so a split by the first letter does nothing.
  lem:tl5-hfk-rec at a face point would weight the first letter Z′ of Z′JZ, but the energies would then need splitting
  by both letters: the same obstruction.

## 3. Lever C: scoped, not drafted

- **Where k₃ sits.** In D_A, 𝔰₁^v = 1/(4 sup k₃), and k₃ carries the factor 8/5. The absorptions already use k₃^z =
  (5/8)(1 − 𝔰₁^v)⁻¹k₃ through 𝔵^z, but the thresholds keep k₃ (87:6467–6468).
- **A threshold with k₃^z.** This is not G0r's "smaller k₃": 𝔵^z rises with 𝔰₁^v, from about 5/32 to 1/4, and with it
  every nonlinear part, every (1 − 𝔵^z)⁻¹ and every (k₁ + 2𝔵^z)/(1 − 𝔵^z). It would also mean restating the lemmas of
  sec:tl5-hfs to sec:tl5-hfy.
- **A genuinely smaller absorption count** (smaller 𝔠^♮ or 𝔔 sums) does not exist in the chapter.
- **The cap, either way.** The rise of 𝔰₁^v is capped by ϑ's cap, 1.48× and 1.14× (G0r §G0r.1). At seed 1 it is also
  capped by 𝔰_♭ = 10⁻⁴, which is 1.25 × 𝔰₀ there, unless 𝔰_♭ is raised.
- **Deduced worth:** at most +0.10 (+0.17 with 𝔰_♭ raised) / +0.06 in D_A at the present ϑ₂, before the cost through
  𝔵^z, and 0 in D*.

## 4. Containment, checks, crosswalk

**Labels (10):** sec:tl5-hfn, lem:tl5-hfn-fam, eq:tl5-hfn-fam, lem:tl5-hfn-low, eq:tl5-hfn-low, def:tl5-hfn-constants,
eq:tl5-hfn-constants, thm:tl5-hfn, eq:tl5-hfn-closing, rem:tl5-hfn-what.

**Containment.**
- **No new choice.** For all weights, routes and options, 𝔐_n^(m) ≤ k₁^(m,μ,p)𝔐_p^(m) (the last paragraph of
  lem:tl5-hfn-low). Every index-f constant is nondecreasing in this entry.
- **The inequalities:** η_n ≥ η_f, A_n ≤ A_f, B_n ≤ B_f, Y_n ≤ Y_f and 𝔰_*^n ≤ 𝔰_*^f. So the hypotheses of thm:tl5-hff
  at N ≥ 6 imply those of thm:tl5-hfn.
- **On thm:tl5-hfk.** It is N = 4 only; at N ≥ 6 the latest theorem is thm:tl5-hff, and that is the one contained. At
  level four nothing changes.
- **Earlier text.** No earlier text is edited, so every earlier closing condition stays valid.
- **Both constraints.** The new constants enter 𝔰_* (C_(∞,μ)^(N−4)) and the closing condition (C_P^♮ → 𝔎, 𝔎^D, S_F).
  They do not enter 𝔯 or ε (deduced: 𝔯^n = 𝔯^f; the theorem states only the inequalities).

**Checks** (fresh scratch tree with the section merged):
- `lint.py --chapters`: 62 files, 5352 labels, 0 hits.
- `assemble.py --check`: 0 problems.
- In-memory assembled lint: `[] 0`.
- Numbering: 0 of 5342 existing numbers change; 10 are added.
- Merged crosswalk: rows are in order and ASCII.
- Chapter text is at most 120 characters, also after labels resolve. The pointer line is 112 characters (109 resolved).
- No forbidden line starts; no orphan ∎; notes are at most 121 characters.
- A random spot-check of the coefficient and containment inequalities (200,000 trials, nice 19) found 0 failures.

**Pointer line**, appended after 87:8038: "[[sec:tl5-hfn]] bounds the second derivatives at low levels word by word, at
the levels N ≥ 6 ([[thm:tl5-hfn]])."

**Crosswalk rows** (paper/reader/proofs/P-GRD17.md@PENDING:<line>): sec:tl5-hfn 1, lem:tl5-hfn-fam 20, eq:tl5-hfn-fam
30, lem:tl5-hfn-low 62, eq:tl5-hfn-low 68, def:tl5-hfn-constants 121, eq:tl5-hfn-constants 132, thm:tl5-hfn 134,
eq:tl5-hfn-closing 139, rem:tl5-hfn-what 168.

## 5. Deduced gains: upper figures, every supremum at one point

All figures are from G0r on P-GRD15, at level 6, through the term of 𝔰_* with A. Order: seed 1 D_A / seed 2 D_A / seed 1
D* / seed 2 D*.
- **The inputs.**
  - With r := C₁^l({ZB})/𝔐_p^(2) = 10^(−0.62/−0.61/−0.61/−0.59) at x = 𝔵_D and 10^(−0.70/−0.70/−0.66/−0.68) at the
    optimum's x (§G0r.4 item 2).
  - Every term of the new entry except the couplings is at most r times its old counterpart. The couplings are 0.3 / 0.3
    / 0.2 / 0.3 % of k₁.
- **Lower figure for the fall** (not an upper one), at fixed parameters at that point: at least about 0.61 / 0.60 / 0.60
  / 0.58 at x = 𝔵_D, and 0.69 / 0.69 / 0.65 / 0.67 at the optimum's x.
- **Upper figure for the fall:** −log₁₀ r + log₁₀ s + w, with s = k₁/(𝔨_♯K_rec) at that point and w the extra fall from
  the weighted image. Neither s nor w is reported at level 6; at level 4 on Γ, w is 0.07 / 0.06 / 0.05 / 0.04.
- **Cap from the unchanged entries.** The gain is also at most the distance to C₁^l, 1.1–1.3 decades (§G0r.4 item 2).
- **Does f keep binding?** Yes: ϱ is 4.0–7.9 decades above f and the closing is 2.9–5.2 away. G0r's ÷ 2 price (+0.286
  / +0.295 / +0.276 / +0.295) shows a nearly one-to-one response.
- **The expected level-6 gain is therefore about +0.65 to +0.70 per case:** at least 0.69 / 0.69 / 0.65 / 0.67 at fixed
  parameters, and at most 0.70 / 0.70 / 0.66 / 0.68 + log₁₀ s + w, below the 1.1–1.3 cap.
- **Elsewhere:**
  - Through the closing condition (𝔐_p^(1): about 0.32–0.37 decades) there is nothing at level 6.
  - Level 4: nothing.
  - Lever C: at most +0.10 (+0.17 with 𝔰_♭ raised) / +0.06 in D_A at the present ϑ₂, less its cost; 0 in D*.

## 6. Left open

- **Lever B (kind 1).** It needs face energies split by last letter, or a bootstrap weighted by last letter.
- **Lever C.** A threshold with k₃^z, or an induction that removes the absorption (a sketch, unchecked). Both are capped
  by ϑ's cap and by 𝔰_♭.
- **The couplings.** They could use 𝔐_p^(m−1) only. Their share is about 0.003 of the entry, so this was not drafted.
- **For G0s to measure:** 𝔐_n^(2) and 𝔐_n^(1) at the level-6 optima; s = k₁/(𝔨_♯K_rec); and C₁^k(ΓB) against K_rec
  C₁^l(ΓB) at level 6.

Files are in
/tmp/claude-0/-home-user-Claude-Method-Works/36602a96-aefb-52fa-89f4-29a4ab038dc7/scratchpad/reader/pgrd17/: the sources
src.md, rest.md and ptr.txt; tools/; PLAN.md; num/spot.py; tree/ (the merged scratch tree). No handoff note was needed.
