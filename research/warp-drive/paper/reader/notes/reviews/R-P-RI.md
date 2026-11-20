# R-P-RI: independent reading of proofs/P-RI.md

File read: `research/warp-drive/paper/reader/proofs/P-RI.md`, md5 aadbb3f1b0fd5ffdc68824940c96c1d2, 465 lines, in full;
the writer's report `notes/reports/P-RI.md`. Read as needed: chapter 33 (sec:iv4-0, sec:s14-model, sec:iv4-1,
sec:iv6 to sec:iv6-4), chapter 34 (sec:iii-f1-1, lem:iii-f1-2-4 with its proof, sec:iii-f1-3 with lem:iii-f1-3-1 and its
proof in full, prop:iii-f1-3-3), chapter 22 (sec:i-c-1, sec:i-c-2, sec:i-c-4, sec:i-c-5), chapter 20 (sec:i-a-1,
lem:i-a-7-1), Appendix A (thm:std-relative-index), proofs/P-G24b.md and proofs/P-G1.md. Nothing under method/, drive/,
extracted/ or recovered/ was read. No chapter, crosswalk or proof file was edited. All tool runs were on scratch copies
under `/tmp/claude-0/-home-user-Claude-Method-Works/36602a96-aefb-52fa-89f4-29a4ab038dc7/scratchpad/rri/`.

The base moved while I read. The writer's base is chapter 33 md5 9571426c…. The P-ADM merge (commit 54350a5d) made it
147ca162…, and the P-G1 merge, still in progress at the end of the reading, made it d2184d75… (HEAD b7553023). I checked
the placement against all three (section "What I checked", item 5).

**Verdict: NOT CONFIRMED.** I found 0 Major, 1 minor and 8 nits. The mathematics of the new index-0 argument is right:
- lem:iii-f1-3-1 applies at every λ.
- The family is norm-continuous between fixed spaces.
- G is well defined, independent of the weight and locally constant in λ.
- Both end evaluations are correct.
- No step needs the root locations at intermediate λ.
- The citation of chapter 34 is not circular.
- Both old texts still occur exactly once, also after the P-ADM merge and the P-G1 merge. The texts compose with P-G24b
  and P-G1 in every order tried.

The one minor finding is a false clause in the sentence that the rewrite reworded (m1). The nits are presentation and
merge-note points. A consolidated replacement for the whole P-RI-2 new text, with m1 and n1–n4 applied, is given after the
findings. It was checked with lint and assemble.

## Findings

### Major

None.

### minor

**m1. P-RI.md lines 333–335 (= lines 73–75 of section 2; P-RI-2 new text, lines 3–5): the R_in clause is false for
θ ∈ (0, π).**

Current text:

    θ ∈ {0, π}, or a constant 𝗋_mid < −½ for θ ∈ (0, π). It is > −½ at R_in and < −½ at R_out, so it is admissible for
    every h⁻¹ ≥ 0. For λ ∈ [0, 1] let P̂_λ be the spectral family of □^C_b with γ_C replaced by λh⁻¹. It satisfies
    (H1)–(H2) of [[sec:i-a-1-3]], by the proof of [[lem:iv4-1-6]], which does not use the value of γ_C. Its transition

What is wrong:
- For θ ∈ (0, π) the order is the constant 𝗋_mid < −½. So "It is > −½ at R_in" is false. The sentence just before it
  says 𝗋_mid < −½, so the two sentences contradict each other.
- The conclusion still holds. For non-real σ, def:iv6-0-2 asks the R_in condition only "when σ = ±1". P-G24b's T23 says
  the same: "For Im σ > 0 nothing is asked off R_out". thm:i-c-4-3 (2) needs only 𝗋 constant near R_out and below
  −½ + S̄ there.
- The clause comes from the old text ("…or r_mid for θ ∈ (0, π). It is invariant …, > −½ at R_in and < −½ at R_out"). The
  rewrite now states 𝗋_mid < −½ explicitly, so the contradiction is visible inside one sentence.

Replacement. These 4 lines replace the 3 above, and fold in n3:

    θ ∈ {0, π}, which is > −½ at R_in and < −½ at R_out, or a constant 𝗋_mid < −½ for θ ∈ (0, π), where only R_out
    enters ([[def:iv6-0-2]]); so it is admissible for every h⁻¹ ≥ 0. For λ ∈ [0, 1] let P̂_λ be the spectral family of
    □^C_b with γ_C replaced by λh⁻¹. It satisfies (H1)–(H2) of [[sec:i-a-1-3]], by the proof of [[lem:iv4-1-6]], whose
    (H1)–(H2) part does not use the value of γ_C. Its transition

The next line ("face normal operator N_tf(P̂_λ, ·) is …") is unchanged. The fourth line is short, which is harmless in
the source. If wanted, the crosswalk note can add "; the R_in clause restricted to θ ∈ {0, π}".

### nit

**n1. P-RI.md line 391 (= line 131): "G(0, γ)" after γ has just been reset to 2 − β.**

Current text:

    n_π(1, 2 − β) = k dim π = dim W_π for every π. Hence ind_1(2 − β) = G(1, 2 − β) = G(0, γ) = 0, and the index of

What is wrong:
- The paragraph first takes γ ∈ (0, 2) at λ = 0, then sets "γ = 2 − β" at λ = 1. So "G(0, γ)" literally means
  G(0, 2 − β).
- That value need not be defined. For β = 2, 2 − β = 0 is a root of I_0 (the root −d at d = 0).
- What is meant is G(0, γ) for some γ ∈ (0, 2).

Replacement (same length):

    n_π(1, 2 − β) = k dim π = dim W_π for every π. Hence ind_1(2 − β) = G(1, 2 − β) = G(0, 1) = 0, and the index of

**n2. P-RI.md lines 357–358, 367–368, 379 (= 97–98, 107–108, 119): the letter X clashes with the manifold X.**

What is wrong:
- sec:iv6-0 fixes X := [ℝ̄⁴; {0}]. The spaces H^(s,(ℓ,q))_(sc,b) of this very paragraph live on it, and lem:iv6-0-1
  writes ρ²Diff²_b(X; 𝒯*_X).
- sec:iv6-4, which the new text cites, says "X is tf".
- "Let X := C_0 + 2" reuses the letter for a number in the same proof. The symbol γ_* occurs nowhere in chapters 22, 33
  and 34. With it the bound also reads as a bound on the weights γ.

Replacement. The X lines become the following; the lines between them are unchanged.

    Let γ_* := C_0 + 2. By [[lem:iii-f1-2-4]] with 𝒯 = [0, 1], there is d_0 > γ_* such that for every λ and every π
    with d(π) ≥ d_0 no root of I_λ on W_π has real part in [−γ_*, γ_*]. For λ ∈ [0, 1] and γ ∈ [−γ_*, γ_*] not the real
    part of a root of I_λ put

in place of lines 357–359;

    n_π(0, γ) = dim W_π for γ ∈ (0, 2), and for every γ ∈ [−γ_*, γ_*] if d(π) ≥ d_0. In the latter case the roots on
    W_π, which depend continuously on λ ([[lem:iii-f1-2-4]]), never have real part in [−γ_*, γ_*], so n_π(λ, γ) = dim W_π
    for every λ. So the terms with d(π) ≥ d_0 vanish, and only finitely many π have d(π) < d_0.

in place of lines 367–369. For line 379, see the replacement under n4, which covers lines 379–384.

**n3. P-RI.md line 335 (= 75): "by the proof of [[lem:iv4-1-6]], which does not use the value of γ_C".** The proof of
lem:iv4-1-6 does use γ_C: its (H3) part is lem:iv4-1-5, the horizon threshold, which needs h small. Only its (H1)–(H2)
part is free of it. The replacement is folded into m1 ("whose (H1)–(H2) part does not use the value of γ_C").

**n4. P-RI.md line 381 (= 121): "which lies in ρ²Diff¹_b" has no reference.**

What is wrong:
- The claim is that the stationary part of λh⁻¹𝓛_c is ρ² times a dilation-invariant first-order b-operator.
- This follows from lem:s14-tf-inputs (i): the coefficient of an order-k derivative is homogeneous of degree k − 2.
  The note in section 3.1 gives this argument, but the chapter text cites nothing.
- The mapping property claimed next uses it at both ends.

Replacement (with n2's γ_*; with X instead the lines are only shorter), in place of lines 379–384:

    in [−γ_*, γ_*], and these roots depend continuously on λ; so there is γ ∈ (−γ_*, γ_*) that is not the real part of a
    root of I_λ for any λ near λ_0. The terms with the factor λh⁻¹, namely −2iσλh⁻¹ρS̄ in [[eq:iv6-0-2]] and the part of
    (□^C)^(0) that comes from λh⁻¹𝓛_c ([[lem:s14-box-c]]), which lies in ρ²Diff¹_b ([[lem:s14-tf-inputs]] (i)), map
    H^(s,(ℓ,q))_(sc,b) boundedly into H^(s−2,(ℓ+1,q−2))_(sc,b). So the domain of the map does not depend on λ, the map
    is continuous in λ in operator norm, and, being Fredholm, it has an index that is constant near λ_0; and every
    n_π(λ, γ) is constant near λ_0, as no root crosses the line Re ι = γ. So G is constant near λ_0, and as [0, 1] is
    connected, G(1, ·) = G(0, ·).

**n5. P-RI.md lines 413–428 (section 6) and line 402: the crosswalk change does not compose with P-G24b.**

What is wrong:
- Section 6 gives the change as "Old row" / "New row", that is, a whole-row replacement.
- P-G24b section 9 appends a note to the same row: "prop:iv6-1-1: … (T24–T29)", with "; P-G24b:" before it.
- If P-G24b goes first, which is the likely order (P-G1, then P-G24b), the old row is no longer a whole line. Pasting the
  new row would then delete P-G24b's note.
- So "If P-G24b is merged, nothing here needs adjusting" (line 402) is true of the chapter texts but not of the
  crosswalk.
- The new row is exactly the old row with an appended string, so the fix is to state the change as an append, as
  P-G24b and P-G1 do.

Replacement for section 6:

    No label is added, so no row is added. Append to the note (fourth field) of the row of prop:iv6-1-1 of
    crosswalk/33-s14-constraint-damping.tsv:

    ; P-RI: index 0 by the relative index formula lem:iii-f1-3-1 (localisation at ztf and the Smith-form count rank = order of the zero of the determinant) and lem:iii-f1-2-4, through the invariant G of the proof of prop:iii-f1-3-3 (iii), with gamma_C deformed to 0 in the spectral family of box^C_b; counts at gamma_C = 1/h from lem:iv4-1-3 (a) and prop:np-10-54 (i) with multiplicity, at 0 from the componentwise free operator; replaces the sector argument and the use of [Mel93, Theorem 6.5] outside its hypotheses; theta_in -> vartheta_in and r_mid -> sans-serif r_mid in the rewritten sentence

and add to line 402: "For the crosswalk, append the note after P-G24b's."

**n6. P-RI.md line 59, and the report ("Chapter 34 uses chapter 33 only in prop:iii-f1-3-3"): the statement about
chapter 34's uses of chapter 33 is too strong as written.**

What is wrong:
- Chapter 34 (md5 5dbbf887…) cites chapter 33 in many places:
  - line 35: prop:np-10-52;
  - lines 76–77 and 275–285: sec:iv4-0, and thm:iii-e-1-1 (3) as (C1)–(C4);
  - lines 458–459 and 500–501: prop:iii-f1-2-3, with lem:s14-delta50 and thm:t49-uniform;
  - lines 1148, 1500 and 1935–1937: thm:iii-e-1-1 (1)–(2);
  - lines 1296–1304 and 1456–1873: lem:iii-e1-2-2, prop:iii-e-3-1, prop:iii-e1-3-1 and others.
- The proof file's parenthetical "(thm:iii-e-1-1 (4))" saves line 59 if it is read as restrictive. The report drops the
  parenthetical.
- What non-circularity needs, and what holds, is narrower.

Replacement for line 59 (and the same sentence in the report):

    - Chapter 34 cites chapter 33 in several places, but none of them in lem:iii-f1-2-4, lem:iii-f1-3-1 or *Types and
      representations*. The results of chapter 33 that rest on prop:iv6-1-1 (thm:iv6-3-1, thm:iv6-4-1, hence
      thm:iii-e-1-1 (4)) enter chapter 34 only at Step 4 of prop:iii-f1-3-3 (ii).

**n7. P-RI.md lines 3–7, 267, 288, 397–407 and 461: the base and the counts are stale.**

What is wrong:
- The proof file pins chapter 33 md5 9571426c… with P-RI-1 at lines 2168–2169 and P-RI-2 at lines 2394–2426.
- It speaks of P-G24b's "43 old texts". P-G24b now has 45 (T44 and T45 were added), and its base is md5 147ca162….
- At the current HEAD (chapter 33 md5 d2184d75…, after the P-G1 merge), P-RI-1 is at lines 2791–2792, P-RI-2 at lines
  3017–3049, and the crosswalk row at line 127.
- Every old text still occurs exactly once, so only the pins are stale.

Replacement: update the md5, the line numbers and "43" to "45" in these places, or say that the line numbers refer to
md5 9571426c… and serve only to find the place.

**n8. P-RI.md line 212 (notes, section 3.2): "since other sectors have roots all along the real axis".**

What is wrong:
- At each h the real parts of all the roots form a discrete set, finitely many in each strip (prop:np-10-54 (iii)). So
  the reason given is not the reason.
- The real reason is the one section 1 gives under route (ii). Nothing in the paper says where the other sectors' roots
  lie at intermediate h⁻¹. So a fixed β₁ − 2 cannot be shown root-free for the whole family along the deformation.
- Also, at a fixed h the old step gives no reason why β₁ − 2 avoids the other sectors' roots.

Replacement:

    - β₁ is not of that kind in general: it is chosen from one sector's roots, and nothing in the paper places the other
      sectors' roots at intermediate h⁻¹, so the line Re ι = β₁ − 2 cannot be shown root-free for the whole family.

## Consolidated replacement for the P-RI-2 new text (m1, n1–n4 applied)

Applied in place of the new text of P-RI-2 (and of section 2) on a scratch copy of the current tree, after the P-G1
merge:
- lint --chapters: 62 files, 4665 labels, 0 hits.
- assemble --check: 0 problems.
- assemble, then lint --paper: 0 hits. Longest line of the assembled index-0 text: 117 characters.
- With every label replaced by "Proposition 33.123", no line exceeds 121.
- No line starts with a forbidden marker.
- 64 lines; md5 of the block 3ff2456e854726636c603698c5441504.

```text
*Index 0.* As the index does not depend on the admissible orders, we find it for s := 2, the given β and ℓ the order
of [[ch:s03]] for the free operator at this σ = e^(iθ): that of [[lem:i-a-7-1]] with ϑ_in = 0 and S̄ = 0 for
θ ∈ {0, π}, which is > −½ at R_in and < −½ at R_out, or a constant 𝗋_mid < −½ for θ ∈ (0, π), where only R_out
enters ([[def:iv6-0-2]]); so it is admissible for every h⁻¹ ≥ 0. For λ ∈ [0, 1] let P̂_λ be the spectral family of
□^C_b with γ_C replaced by λh⁻¹. It satisfies (H1)–(H2) of [[sec:i-a-1-3]], by the proof of [[lem:iv4-1-6]], whose
(H1)–(H2) part does not use the value of γ_C. Its transition
face normal operator N_tf(P̂_λ, ·) is (□^C)^(·) with h⁻¹ replaced by λh⁻¹, by the proof of [[lem:iv6-0-1]] (d); at
λ = 0 it is the spectral family of □_η = 2δ_ηG_ηδ*_η, which acts componentwise in the frame dt, dx^i
([[lem:s14-box-c]], Ric(η) = 0). The thresholds of P̂_λ at R_out and at R_in are −½ + λh⁻¹(1 − e)(1 − v) ≥ −½ and
−½ − λh⁻¹(1 − e)(1 + v) ≤ −½ ([[prop:np-10-21]], [[eq:s14-theta-in]]). So these orders are allowed in
[[thm:i-c-4-3]] (1)–(2) for every λ, and with them the map [[eq:iv6-1-1]], with N_tf(P̂_λ, e^(iθ)) in place of
(□^C)^(σ), is the map 𝒳_(tf,θ) → 𝒴_(tf,θ) of [[sec:i-c-4]] for P̂_λ at q = β ([[sec:iv6-4]]). For γ ∈ ℝ that is
not the real part of an indicial root of P̂_λ(0), let ind_λ(γ) be the index of this map at q = 2 − γ, which is
Fredholm by [[thm:i-c-4-3]] (3); this is the index of [[sec:iii-f1-3]] at the weight γ. The index to be found is
ind_1(2 − β), and 2 − β ∈ [−C_0, 2).

For λ ∈ [0, 1] let I_λ be the indicial family ([[eq:i-c-1-3]]) of P̂_λ(0). It is that of ρ⁻²(□^C)^(0) with h⁻¹
replaced by λh⁻¹ (the proof of [[lem:iv4-1-3]]), of the form of [[lem:i-c-2-4]], with coefficients affine in λ that
commute with the action of SO(4) rotating both 𝕊³ and the Cartesian components. For an irreducible representation π
of SO(4) let W_π, the π-isotypic subspace of C^∞(𝕊³; ℂ⁵), and d(π) be as in [[lem:iii-f1-2-4]]; sums over π below
run over the π with W_π ≠ 0. For γ ∈ ℝ let n_π(λ, γ) be the number of roots of I_λ on W_π with real part < γ, with
multiplicity. By *Types and representations* in [[sec:iii-f1-1]], W_π is ℂ^k ⊗ π for the type and degree of π, with
k = 2 at scalar type 0, k = 3 at scalar type l ≥ 1 and k = 1 at vector type, and I_λ(ι) acts on W_π as N(ι) ⊗ Id_π
for a k × k matrix N(ι). So det(I_λ(ι)|_(W_π)) = det(N(ι))^(dim π), and the roots on W_π are those of det N, each
with its multiplicity multiplied by dim π. At λ = 1, in the basis S dt, S dr, r dS (resp. rV) of [[prop:np-10-12]]
(ii), N is N_0, N_l or N_(v,l), so that det N is h⁻²P_0, h⁻³P_l or h⁻¹p_(v) ([[prop:np-10-12]] (iii)).

Let γ_* := C_0 + 2. By [[lem:iii-f1-2-4]] with 𝒯 = [0, 1], there is d_0 > γ_* such that for every λ and every π
with d(π) ≥ d_0 no root of I_λ on W_π has real part in [−γ_*, γ_*]. For λ ∈ [0, 1] and γ ∈ [−γ_*, γ_*] not the real
part of a root of I_λ put

    G(λ, γ) := ind_λ(γ) − Σ_π (n_π(λ, γ) − dim W_π).

The sum is finite. Each H_d ⊗ ℂ⁵, H_d the harmonics of degree d ((K4) of [[sec:i-c-2-1]]), is invariant under the
action of SO(4), so W_π is the sum of its intersections with these spaces, which vanish for d < d(π). At λ = 0, on
H_d ⊗ ℂ⁵, I_0(ι) = −ι² + 2ι + d(d + 2) = −(ι + d)(ι − d − 2), the free operator acting componentwise (the proof of
[[prop:i-c-5-3]]). So at λ = 0, W_π carries dim W_π roots ≤ −d(π) and dim W_π roots ≥ d(π) + 2; hence
n_π(0, γ) = dim W_π for γ ∈ (0, 2), and for every γ ∈ [−γ_*, γ_*] if d(π) ≥ d_0. In the latter case the roots on
W_π, which depend continuously on λ ([[lem:iii-f1-2-4]]), never have real part in [−γ_*, γ_*], so n_π(λ, γ) = dim W_π
for every λ. So the terms with d(π) ≥ d_0 vanish, and only finitely many π have d(π) < d_0.

G(λ, γ) does not depend on γ. Let γ₁ < γ₂ be two such weights, and choose γ₁ = w_0 < w_1 < … < w_M = γ₂ with
w_(i+1) − w_i < 1, none of them the real part of a root of I_λ; this is possible, as only finitely many roots have
real part in [γ₁, γ₂] ([[lem:i-c-2-4]] (b)). By [[lem:iii-f1-3-1]], applied to each pair (w_i, w_(i+1)) as its
weights (β_1, β_2), ind_λ(w_(i+1)) − ind_λ(w_i) is the number of roots of I_λ with real part in (w_i, w_(i+1)), with
multiplicity. Adding, ind_λ(γ₂) − ind_λ(γ₁) is the number of roots with real part in (γ₁, γ₂), which is the change of
the sum.

G(λ, γ) does not depend on λ. Let λ_0 ∈ [0, 1]. Only the finitely many W_π with d(π) < d_0 carry roots with real part
in [−γ_*, γ_*], and these roots depend continuously on λ; so there is γ ∈ (−γ_*, γ_*) that is not the real part of a
root of I_λ for any λ near λ_0. The terms with the factor λh⁻¹, namely −2iσλh⁻¹ρS̄ in [[eq:iv6-0-2]] and the part of
(□^C)^(0) that comes from λh⁻¹𝓛_c ([[lem:s14-box-c]]), which lies in ρ²Diff¹_b ([[lem:s14-tf-inputs]] (i)), map
H^(s,(ℓ,q))_(sc,b) boundedly into H^(s−2,(ℓ+1,q−2))_(sc,b). So the domain of the map does not depend on λ, the map
is continuous in λ in operator norm, and, being Fredholm, it has an index that is constant near λ_0; and every
n_π(λ, γ) is constant near λ_0, as no root crosses the line Re ι = γ. So G is constant near λ_0, and as [0, 1] is
connected, G(1, ·) = G(0, ·).

At λ = 0 and γ ∈ (0, 2), ind_0(γ) = 0: at ρ = 0, P̂_0 has the data of □_η acting componentwise, so it is
tf-admissible with every weight in (0, 2) ([[prop:i-c-5-3]]), and N_tf(P̂_0, e^(iθ)) is invertible at q = 2 − γ by
[[cor:i-c-5-2]] (a). As n_π(0, γ) = dim W_π for every π, G(0, γ) = 0. At λ = 1 and γ = 2 − β, no indicial root of
P̂_1(0) has real part in [−100, 2) ([[lem:iv4-1-3]] (a)), so n_π(1, 2 − β) is the number of roots on W_π with real
part < −100. With multiplicity, P_0 has two such roots, P_l (l ≥ 1) three and p_(v) one ([[prop:np-10-54]] (i)); so
n_π(1, 2 − β) = k dim π = dim W_π for every π. Hence ind_1(2 − β) = G(1, 2 − β) = G(0, 1) = 0, and the index of
[[eq:iv6-1-1]] is 0. ∎
```

## An observation outside P-RI (chapter 34; for the coordinator, not a finding on P-RI)

lem:iii-f1-3-1 asks only s ∈ ℤ. But Step 1 of its proof uses the half-plane Mellin transform of f ∈ H^(s−2)_(b,c_1)
"with the line bounds [[eq:i-c-2-1]]". sec:i-c-2-3 defines that transform, and eq:i-c-2-1 holds, only for weighted L²
functions, so the step needs s ≥ 2. Both uses meet this: s := 2 here, and "s ∈ ℤ large" in prop:iii-f1-3-3. The writer
notes the point in section 3.1. A one-word repair in chapter 34 would be "s ∈ ℤ, s ≥ 2".

## What I checked and found correct

1. **lem:iii-f1-3-1 applies at every λ ∈ [0, 1].**
   - P̂_λ satisfies (H1)–(H2). (H1) comes from the principal symbol of □_(g_b) ⊗ Id. E^C has order 0 and no ∂²_(t_*)
     term, so it changes neither σ₁(T) nor P₂. (H2) comes from lem:iv4-1-2, whose proof (prop:np-10-21 (i) on the model,
     differences counted in ρ-orders) holds for any damping value. Only the clause "all positive" of lem:iv4-1-2 uses
     γ_C > 0, and (H2) does not ask for it.
   - N_tf(P̂_λ, σ̂) = 2iσ̂ρ̂(ρ̂∂_ρ̂ − 3/2 − λh⁻¹S̄) + (□^C_λ)^(0), by eq:i-c-4-1 and the proof of lem:iv6-0-1 (d).
     □^C = 2δGδ* + h⁻¹𝓛_c is affine in the damping.
   - The spaces are those of thm:i-c-4-3 with α₊ = 0 and 𝗋 = ℓ, by sec:iv6-4. The thresholds of P̂_λ are λ times those
     of prop:np-10-21 / eq:s14-theta-in. They are evaluated in the λ-independent eigenbasis inner products of M and
     M + 2N, which (O3) allows to be chosen per radial set. So the free orders satisfy (O2)–(O3) with margins at least
     the free ones, at every σ₀ ∈ J_±.
   - The constant 𝗋_mid < −½ ≤ −½ + λh⁻¹(1 − e)(1 − v) is allowed in thm:i-c-4-3 (2) with I = {θ}.
   - s = 2 is an integer, as the lemma asks. The weights w_i, w_(i+1) are root-free with 0 < w_(i+1) − w_i < 1.
   - The lemma's proof, read in full:
     - Step 1: the expansion 𝒵 = 𝒳_1 ⊕ χF. f ∈ H⁰ for s = 2.
     - Step 2: 𝒴_2 = 𝒴_1 + N(𝒳_2).
     - Step 3: ind N_2 = ind N_1 + dim F. The index increases with β, which agrees with the sign used.
     - Multiplicity: the Smith form on each W_π, with finitely many W_π by lem:iii-f1-2-4.
     It uses only (H1)–(H2) data at ρ = 0 and SO(4) equivariance, and I_λ has both.

2. **The deformation.**
   - The λ-dependent part of N_tf(P̂_λ, e^(iθ)) is λh⁻¹(−2iσρS̄ + (𝓛_c)_stat). (𝓛_c)_stat is ρ² times a dilation-invariant
     first-order b-operator (lem:s14-tf-inputs (i)).
   - At the scattering end, ρ²Diff¹_b ⊂ ρDiff¹_sc maps H^(s,ℓ)_sc into H^(s−1,ℓ+1)_sc. Near r = 0, ρ and ρ² lower the
     b-weight q − 2 by 1 and 2, into H_(b,q−4), the weight of 𝒴. So the domain {w : N_λw ∈ 𝒴} is the same set for all λ,
     the graph norms are equivalent, and λ ↦ N_λ is affine and norm-continuous.
   - Fredholmness at each λ comes from thm:i-c-4-3 (3) at a weight root-free for all of I_λ. The weights do not have to
     stay root-free along the whole path, and the text does not claim that they do. G is defined at each λ with any
     root-free γ ∈ [−γ_*, γ_*], and is shown locally constant with a weight chosen near each λ_0. Such a weight exists,
     because only the finitely many W_π with d(π) < d_0 carry roots in the strip, and those move continuously
     (lem:iii-f1-2-4: on W_π the determinant has fixed degree 2 dim W_π and leading coefficient (−1)^(dim W_π)). So the
     root locations for λh⁻¹ in place of γ_C are never needed. This is the point of the invariant, and it is the
     correct reason route (ii) fails.

3. **G and its two evaluations.**
   - The sum is finite. W_π is the finite sum of W_π ∩ (H_d ⊗ ℂ⁵) for d(π) ≤ d ≤ d(π) + 4. For d(π) ≥ d_0 the term is 0
     for all λ.
   - Only finitely many π have W_π ≠ 0 and d(π) < d_0. ℂ⁵ = (0, 0) ⊕ (½, ½), so every π is scalar (l/2, l/2) or vector
     ((l ± 1)/2, (l ∓ 1)/2).
   - Independence of γ: Σ_π (n_π(γ₂) − n_π(γ₁)) counts the roots in [γ₁, γ₂) = (γ₁, γ₂). This equals Σ_i dim F by
     lem:iii-f1-3-1, with J(ι) = I(−ι), and dim F_μ = Σ_π ord.
   - λ = 0: in the frame dt, dx^i, I_0 = −ι² + 2ι + d(d + 2) on H_d ⊗ ℂ⁵, with roots −d and d + 2 and multiplicity
     dim(W_π ∩ H_d ⊗ ℂ⁵) each. So n_π(0, γ) = dim W_π on (0, 2). ind_0 = 0 by prop:i-c-5-3 and cor:i-c-5-2 (a), the gap
     being (0, 2) and q = 2 − γ ∈ (0, 2). The fibre inner product only enters the adjoint, so invertibility on 𝒳 → 𝒴
     does not depend on it, and H_0 = Id may be taken.
   - λ = 1: lem:iv4-1-3 (a) leaves no root with real part in [−100, 2). Since C_0 ≤ 100, 2 − β ∈ [−C_0, 2) ⊂ [−100, 2).
     The counts with multiplicity are those of prop:np-10-54 (i): P_0 has 2 and 2 (degree 4), P_l has 3 and 3
     (degree 6), and p_(v) has 1 and 1 (degree 2).
   - W_π = ℂ^k ⊗ π via (A, B, C) ⊗ S ↦ A S dt + B S dr + C r dS, which is equivariant and injective with image of
     dimension 3 dim π. The multiplicities checked by Clebsch–Gordan are 2 (l = 0), 3 (l ≥ 1) and 1 (vector type).
   - det N_0 = h⁻²P_0, det N_l = h⁻³P_l and N_(v,l) = h⁻¹p_(v), so n_π(1, 2 − β) = k dim π = dim W_π.
   - The relation to the old counts in section 3.2 of the notes (the missing factor dim π, the same on both sides) is
     right.

4. **The old step (ii).**
   - It claimed the Fredholm property at β₁, chosen below all roots of one sector for all h⁻¹, "by the estimates above".
     Those estimates (the Mellin step "with [β_0 − 2, β − 2] root-free", and thm:i-c-4-3 / lem:i-c-2-6) need the weight
     to avoid the real parts of all roots of the full indicial family.
   - Nothing in the chapter supplies a sector-restricted version, nor root-freeness of β₁ − 2 for the other sectors
     along the deformation. So the claim was a gap, as the writer says; only the note's wording is off (n8).
   - The new text uses only weights root-free for all of I_λ: γ ∈ (0, 2) at λ = 0, 2 − β at λ = 1, and locally chosen
     γ in between. It cites no "estimates above".

5. **Placement.**
   - Old texts. In the chapter at each of the three bases:
     - md5 9571426c…: P-RI-1 at line 2168, P-RI-2 at line 2394, crosswalk row at line 114;
     - md5 147ca162…: lines 2170 and 2396, row 114;
     - md5 d2184d75…, after the P-G1 merge: lines 2791 and 3017, row 127.
     Each old text occurs exactly once, as whole lines.
   - The section-2 text equals the P-RI-2 new text.
   - Composition (simulated by script on the 147ca162… chapter, starting from that chapter each time): P-G1's C33-1 to
     C33-20, then P-G24b's 45 texts with T41 in variant A; P-RI first, in the middle and last; and P-G24b alone before
     or after P-RI. Every old text was found exactly once at its turn, and the three P-G1/P-G24b/P-RI orders give
     identical chapters.
   - Starting from the post-P-G1 chapter, P-RI and P-G24b in both orders give identical chapters. P-RI's new texts
     survive intact.
   - The only order that fails is P-G24b before P-G1 (C33-11), which is P-G1/P-G24b's own documented constraint and
     not P-RI's.
   - No other proof file in proofs/ quotes a line of P-RI's old texts.
   - The crosswalk row has 4 tab-separated fields, and the new row is the old row with an appended string (n5).
   - After the change, thm:std-relative-index is cited once (P-RI-1, as attribution), as section 3.4 says. Before it
     was cited nowhere: the old text cites "[Mel93, Theorem 6.5]" without the label.
   - lem:s14-tf-inputs (v) is cited nowhere; "[Mel93" and "[Hin26a, p. 91]" no longer occur in chapter 33.

6. **Tool runs (scratch copies only; the plain assemble.py was never run in the repository).**
   - Base 147ca162… (tree/, treeA/):
     - before: lint --chapters 62 files, 4652 labels, 0 hits; assemble --check 0 problems;
     - after P-RI-1, P-RI-2 and the crosswalk row: the same; assemble then lint --paper: 0 hits.
   - Base d2184d75…, after the P-G1 merge (now/, nowA/):
     - before: 4665 labels, 0 hits, 0 problems;
     - after P-RI: 4665 labels, 0 hits, 0 problems; PAPER.md 0 hits.
   - P-G1, P-G24b and P-RI all applied (treeB/, nowB/): lint --chapters 62 files, 4681 labels, 0 hits; assemble --check
     0 problems; PAPER.md 0 hits; longest assembled line 121, elsewhere in the paper.
   - Line lengths and typography:
     - In the assembled paper the new index-0 text has lines of at most 117 characters, and P-RI-1 at most 113.
     - With every label replaced by "Proposition 33.123", no new line exceeds 121.
     - No line of either new text starts with "+ ", "- ", "* ", "> ", "#", "=", "|" or "<". There is no backslash, and
       no label is added.

7. **Non-circularity.**
   - lem:iii-f1-2-4 cites only lem:i-c-2-4. lem:iii-f1-3-1 cites lem:i-c-2-3, lem:i-c-2-4, lem:i-c-2-5, eq:i-c-2-1,
     eq:i-c-2-2, thm:i-c-4-3 (3), sec:i-c-4-1 (c) and lem:iii-f1-2-4. *Types and representations* cites only the type
     bases of chapter 30 (eq:iii-a1-2-9, eq:iii-a1-2-10) and recalls a representation fact "as in the proof of"
     prop:iii-d2-3-1 (chapter 32).
   - Chapters 20 and 22 cite ch:s14 and ch:s15 only as pointers to where operators are studied.
   - The results of chapter 33 resting on prop:iv6-1-1 (thm:iv6-3-1, thm:iv6-4-1, thm:iii-e-1-1 (4)) occur in chapter 34
     only at Step 4 of prop:iii-f1-3-3 (ii) (line 739). So there is no cycle through prop:iv6-1-1.
   - The new text's citation of sec:iv6-4 (in the proof of thm:iv6-4-1) is only for the identification of the spaces,
     which does not use prop:iv6-1-1, as in the old text.
   - Chapter 33 already cites chapter 34 (prop:iii-f1-2-3, sec:iii-f1-1, lem:iii-f-2-1, eq:iii-f1-2-2). INTEGRATION.md
     accepts logically acyclic forward references.

8. **Typos fixed by the rewrite.** "θ_in" becomes "ϑ_in", the threshold of lem:i-a-7-1. "r_mid" becomes "𝗋_mid", the
   constant order of cor:i-c-5-2 (b).

9. **P-RI-1.** The attribution "for b-elliptic operators on compact manifolds with boundary this is Melrose's
   [[thm:std-relative-index]]" matches Appendix A's statement ([Mel93, Theorem 6.5, p. 214], compact X, P b-elliptic).
   "With the indicial roots counted by type and degree on 𝕊³" describes the new count.

## Confirmation (fix round)

File re-read: proofs/P-RI.md, md5 a5756b0fec1a33885fcd3987fae1b51c, 586 lines, as committed at HEAD d96dc214. Also
read: the writer's fix report (scratchpad reader/reports/F-P-RI.md). The bases were chapter 33 md5 d2184d75…,
chapter 34 md5 5dbbf887…, crosswalk/33 md5 5b4e25fe… and crosswalk/34 md5 6995e64a…; the working tree equals HEAD for
all four. P-G24b was taken at HEAD, md5 a44f9f97…, 45 texts. No repository file was edited.

**Verdict: CONFIRMED.** Every finding is resolved, and I found nothing new of Major or minor weight.

### The findings, one by one

- **m1, n1–n4.** The P-RI-2 new text, and the identical block in section 2, is my consolidated replacement byte for
  byte: md5 without the final newline 3ff2456e…, 64 lines. P-RI-1's old and new texts and P-RI-2's old text are
  unchanged from the version I read first. The notes in sections 3.1 and 3.3 now explain the R_in clause, the (H3)
  point, γ_* and the weight 1. They are correct.
- **n5. Resolved.** Section 6 now gives both crosswalk changes as appends to the fourth field.
  - The prop:iv6-1-1 note is the old appended string plus ", and its R_in clause restricted to theta in {0, pi}".
  - In scratch copies B and C below, the row of prop:iv6-1-1 keeps 4 fields, with each of "; P-RI:" and "; P-G24b:"
    present once. Only the order of the two notes differs.
  - The new crosswalk/34 note for lem:iii-f1-3-1 goes into an empty fourth field: row 29, 4 fields, fourth empty at
    HEAD. Its text is accurate.
- **n6. Resolved, and the change is right.** My replacement said that the chapter-33 results resting on prop:iv6-1-1
  enter chapter 34 only at Step 4 of prop:iii-f1-3-3 (ii). As a statement about routes that was incomplete, and the
  writer is right to name the second route:
  - eq:iv4-0-1 (chapter 33, line 112) puts h_tf, the threshold of thm:iv6-3-1, into h_* := min(10⁻⁶, h_0, h_tf).
  - Chapter 34 fixes its damping data "in [[sec:iv4-0]]" (its lines 75–77).

  The bullet's conclusion holds on both counts:
  - The four pieces the new text uses (lem:iii-f1-2-4, lem:iii-f1-3-1, *Types and representations*, and the *Weights*
    paragraph) are stated for a general P̂ satisfying (H1)–(H2), or for a general equivariant indicial family. They cite
    no chapter-33 result and use none of chapter 34's fixed data.
  - prop:iv6-1-1 holds for every h ∈ (0, 10⁻⁶] (sec:iv6-0). Its proof, as now written, uses lem:iv4-1-3, lem:iv4-1-6
    and prop:np-10-54, all stated for every h ∈ (0, 10⁻⁶], so it never needs h < h_*.

  The listed citations of thm:iii-e-1-1 in chapter 34 match the file:
  - its setting: lines 77, 212, 275, 281 and 1935;
  - its clauses (1)–(3): lines 285, 1148, 1500 and 1937;
  - its clause (4): line 739.

  One precision, which needs no change: h_tf itself is defined (chapter 33, line 3173) as the h_0 of thm:iv6-2-1. So
  this route rests on prop:iv6-1-1 only through the statement of thm:iv6-3-1. Listing it is the conservative choice.
- **n7. Resolved.** I re-checked the pins and positions:
  - P-RI-1 is at chapter 33 lines 2791–2792, P-RI-2 at 3017–3049 and P-RI-3 at chapter 34 lines 595–596. Each occurs
    once, as whole lines. The crosswalk row is at line 127.
  - P-G24b's T21 is at 2752–2754, T23 at 2937–2939, T29 at 3005–3008 (ending inside line 3008, before " Near r = 0
    the normal operator") and T30 at 3080–3082 at HEAD.
  - T39 removes "sector" at line 3169. lem:s14-tf-inputs (v) is at 2823–2824 and is cited only at 3043.
  - The paragraph "So [[eq:iv6-1-1]] is Fredholm" is at 3011–3015.
  - P-G24b's §6.1 is at its lines 1475–1499, its table row at line 127 (chapter lines 2412–2413 of md5 147ca162…,
    3033–3034 at HEAD), and its summary item (c) at lines 16–17.
  - The proof file now says 45 texts throughout.
- **n8. Resolved.** Section 3.2 has the replacement as given.

### The new item P-RI-3 (lem:iii-f1-3-1: "and s ∈ ℤ." becomes "and s ∈ ℤ, s ≥ 2.")

- The text is correct. Steps 1 and 2 of the lemma's proof take Mellin transforms of elements of H^(s−2)_b with the
  bounds eq:i-c-2-1. sec:i-c-2-3 provides these only for weighted L² functions, so the proof needs s ≥ 2.
- Uses. A search of all chapter sources and all proof files finds one use at HEAD, chapter 34 line 760, in
  prop:iii-f1-3-3 (iii). It takes the s fixed at line 716, "Fix α_+, s ∈ ℤ large", which meets s ≥ 2. After P-RI there
  is one more use, P-RI-2, at s := 2. P-RI-1 only names the formula. No other proof file cites the lemma.
- Form. The old text is the two lines 595–596, found once. The new second line is 120 characters in the source, and in
  PAPER.md the two lines are 101 and 120. It adds no label, starts no line with a forbidden marker, and has no
  backslash.

### Scratch merges

The base was a git archive of HEAD (chapters/, crosswalk/, assemble.py, lint.py, OUTLINE.md), in scratchpad rri2/.
P-G24b was used at HEAD, with T41 in variant A and its §9 note on prop:iv6-1-1.

| copy | content | lint --chapters | assemble --check | assemble, then lint --paper |
|---|---|---|---|---|
| base | HEAD | 4665 labels, 0 hits | 0 problems | (not run) |
| A | P-RI alone (P-RI-1 to P-RI-3, both crosswalk notes) | 4665 labels, 0 hits | 0 problems | PAPER.md 0 hits |
| B | P-G24b, then P-RI | 4681 labels, 0 hits | 0 problems | PAPER.md 0 hits |
| C | P-RI, then P-G24b | 4681 labels, 0 hits | 0 problems | PAPER.md 0 hits |

- Every old text of both files was found exactly once at its turn. P-RI's texts were found as whole lines.
- B and C have byte-identical chapters 33 and 34 and an identical crosswalk/34. Their crosswalk/33 differs only in the
  order of the two notes on the prop:iv6-1-1 row.
- The longest line is 121 characters in chapter 33, chapter 34 and PAPER.md, in A, B and C.

### For the coordinator

These need no action on P-RI.md:
- The superseded first report, notes/reports/P-RI.md line 51, still says "Chapter 34 uses chapter 33 only in
  prop:iii-f1-3-3". The proof file now has the correct statement.
- The proof file's only lines over 121 characters are the two one-line crosswalk notes inside fences, lines 518 and 529.
- The short source line "(H1)–(H2) part does not use the value of γ_C. Its transition" was kept, as I proposed. It
  does not show in the rendering.
