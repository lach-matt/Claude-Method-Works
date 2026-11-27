# R-P-40-sem: independent line-by-line reading of the repair P-40-sem

Tree read at HEAD 85bcfe80, with the diff 14817ece~1..HEAD on chapters/ and notes/reports/P-40-sem.md read in full.
Line numbers are those of HEAD. Nothing in the repository was edited.

## Verdict

**CONFIRMED** — Major 0, minor 3, nit 1.

The repaired proofs are correct. These are prop:iii-i8-4-1 (i) and (ii) at α″, the end of the proof of thm:iii-i11-4-1,
prop:iii-i15-2-5 (2) and (4), and prop:iii-i15-2-12 (2). The order of choices has no circle, every ‖·‖^+ exists at a
finite regularity, and every ε is chosen after what it depends on.

The three minors are as follows.

- One use of thm:iii-i11-4-1 in chapter 41 still quotes the old bound by the fixed seminorm. Read literally, it restates
  the cycle (m1).
- The statement of prop:iii-i8-4-1 (i) now quantifies over seminorms, but it leaves unsaid that d is chosen after the
  seminorm (m2).
- The fixer's first reported-only point (40:493–495) needs a clearer sentence (m3).

On the fixer's second reported-only point, chapter 46 needs no sentence (section 4).

## Was the gap real? Yes.

Each of the three requirements is in the text.

- **(R1) Step 0 of lem:iii-i8-3-2.** The proof (40:1002–1005, 40:1089–1092) bounds ‖(L − L_b)u‖_(𝒴(α)) ≤ C(‖h‖ + |p⃗|)‖u‖_(α′).
  - L − L_b is a b-differential operator of order 2 (eq:iii-i-4-2).
  - Its coefficients are generic, of size O(‖h‖ + |p⃗|), and come from g′ − g_b (lem:iii-i8-2-5).
  - So the seminorm at α′ must read u two orders above the regularity of ‖·‖_(𝒴(α)): n_i ≥ y_(i+1) + 2.
- **(R2) The solution map gains at most one derivative.**
  - Every bound in the text is a loss, not a gain:
    - thm:iii-i-5-3 / cor:iii-h2-5-1 bound u at order k by f at order k + d;
    - lem:iii-i7-2-5 (c) gives bounds "at each finite regularity" with such losses.
  - Independently of the paper's losses, a gain of more than one derivative is impossible:
    - Take a wave packet u supported in the interior of Ω_* and vanishing near {t^♭_* = 1}.
    - It lies in eq:iii-i8-4-2, so by uniqueness the map of (i) sends Lu to u with p⃗′ = 0.
    - Hence n_i ≤ y_i + 1.
- **(R3) The old (i) at α″.**
  - The old proof wrote ‖F‖ := ‖F‖_(𝒴(α″)) and took ‖u(0)‖_(α′) ≤ C‖F‖ from (i) at α′.
  - That needs ‖·‖_(𝒴(α′)) ≤ C‖·‖_(𝒴(α″)) on 𝒴(α″), so y_(i+1) ≥ y_i (and ε_(i+1) ≤ ε_i).
  - A seminorm of lower regularity does not bound one of higher regularity.

So y_(i+1) ≥ y_i ≥ n_i − 1 ≥ y_(i+1) + 1, which is impossible. The same cycle sat in three more places:

- the old (ii) at α″, which only had R_j → 0 in 𝒴(α″) but used ‖w_j − w‖_(α′) ≤ C‖R_j‖_(𝒴(α′));
- the old end of thm:iii-i11-4-1;
- the old prop:iii-i15-2-12 (2), where the forward solution u_1 of F_1 is read at reg ‖·‖_𝒴 + 2 and bounded by ‖F_1‖_𝒴,
  so k ≥ k + 1.

The gap was in the bookkeeping. Read as continuity of linear maps between Fréchet spaces, uniform in the background,
the statements were true.

## Findings

### m1 (minor) — chapters/41-s22-kerr-face.md:1428–1433 and 1459–1461: the old bound of thm:iii-i11-4-1 is still quoted

**The problem.** Step 6 of the proof of thm:iii-i12-3-1, and the remark after that proof, quote the bounds at the end of
the proof of thm:iii-i11-4-1 as "at most C‖F‖_(𝒴⁰(α))". Step 6 reads "‖G(W⃗)‖_(𝒴⁰(α)) and ‖u_0‖_(w_(α′)) are at most
C‖F‖_(𝒴⁰(α)) by the bounds in that proof".

- After the repair, those bounds are by "a seminorm of 𝒴⁰(α) of large enough regularity". That seminorm must bound both
  ‖F‖_(𝒴⁰(α)) and ‖F‖^+_(𝒴(α′)), so it is of strictly larger regularity than ‖·‖_(𝒴⁰(α)).
- Read with one seminorm on both sides, ‖G(W⃗)‖_(𝒴⁰(α)) ≤ C‖F‖_(𝒴⁰(α)) is the old cycle again. The fixed seminorm of
  lem:iii-i11-3-2 cannot bound the solution at α′ in a seminorm two orders above it.
- The remark at 1459 says "for every choice of the seminorms of large enough regularity". That does not help, because
  the conclusion reuses the symbol of the left side.
- The fixer's report lists 1452–1459 as consistent but not 1428–1431. 41:1736 already says the right thing: "at most C
  times a seminorm of the forcing F".
- The statement of thm:iii-i12-3-1 ("bounds uniform") is unaffected, and so is every later use. The fix is wording only.

**Replacement for 41:1428–1433** (seven lines for six; the old 1434 follows unchanged):

```
*Step 6 (the rest).* Every map used is linear and bounded, uniformly for (h, p⃗) small ([[lem:iii-i11-3-2]],
[[thm:iii-i11-4-1]], [[lem:iii-i12-2-1]]–[[lem:iii-i12-2-4]]), and is applied to the forcing f′ of Step 0, whose size
is at most C‖F‖, ‖F‖ being the seminorm of 𝒴⁰(α) of large enough regularity at the end of the proof of
[[thm:iii-i11-4-1]]. Put w_(α′) := min(α′ − 2, λ_♯ − 1), with α′ ∈ (2, 3) the admissible level fixed in that proof:
‖G(W⃗)‖_(𝒴⁰(α)) and ‖u_0‖_(w_(α′)) are at most C‖F‖ by the bounds there, and ‖(L_(h,p⃗) − L_(b_0))u_0‖_(𝒴⁰(α)) ≤
C(‖h‖ + |p⃗|)‖u_0‖_(w_(α′)) by the count of Step 0 of the proof of [[lem:iii-i11-3-2]]. Reality: u is real and the
towers are real (the conjugate of T_ψ(Y) is T_ψ(Ȳ)), so replacing
```

**Replacement for 41:1459–1461:**

```
(0, w_0]. The bounds at the end of the proof of [[thm:iii-i11-4-1]], which hold for every choice of the seminorms of
large enough regularity, give |p⃗′_(h,p⃗)(F)|, ‖G(W⃗)‖_(𝒴⁰(α)) and ‖u_0(W⃗)‖_(w) at most C‖F‖, with ‖F‖ a seminorm of
𝒴⁰(α) of larger regularity, as there; so the three terms are at most C‖F‖, which is the bound of Step 6.
```

Lengths after label resolution: at most 112 and 117 characters.

### m2 (minor) — chapters/40-s21-parameters.md:1137–1140 and 748–752: the statement does not say that d follows the seminorm

**The problem.** The repaired (i) reads "for each fixed seminorm ‖·‖_(α) of the space of eq:iii-i8-4-2 there are a
seminorm ‖·‖^+_(𝒴(α)) … and C with …, with bounds uniform for (h, p⃗ − p⃗_b) small". "h small" means small in 𝒳^d, and
d is "fixed throughout" (sec:iii-i7-1). The proof for a target ‖·‖_(α″) needs d large for a whole chain of seminorms
built from that target:

- ‖·‖_(𝒴(α″)) and ‖·‖_(α′);
- ‖·‖^+_(𝒴(α′));
- in (ii), the seminorm two orders above ‖·‖^+_(𝒴(α′)) and its own ^+;
- and so on down to α_0.

A bound uniform over h that is small only in 𝒳^d cannot hold for targets of regularity far above d. The constants of a
forward solution at order k involve ‖h‖_(𝒳^(k+loss)). Read as "every seminorm, with one d fixed in advance", (i) is
false.

The intended order is: first the finitely many seminorms that a given target requires, then d. sec:iii-i8-1 implies
this ("d is taken so large that … in these seminorms"), and lem:iii-j2-2-3 collects the orders into d_*. Neither
sentence says it, and the new quantifier makes the omission visible. Two smaller points:

- sec:iii-i8-1 speaks of "a second seminorm ‖·‖^+_(𝒴(α))" in the singular, while it depends on the target seminorm.
- In sec:iii-i8-1, lem:iii-i8-2-6 (b) is not a "bound by ‖h‖". It is a bound by |S|, uniform for h small. Part (c) of
  the same lemma is used in (ii) at α″ (Φ_j → Φ) at the regularities of the ^+ seminorms.

This is the paper's existing convention: lem:iii-i7-2-5 (c) claims uniform bounds "at each finite regularity" in the
same way. So it is a precision, not a gap.

**Replacement for 40:1137–1140** (five lines for four; the statement ends at the new fifth line):

```
Moreover (i) p⃗′_(h,p⃗) and F ↦ u are linear, with bounds uniform for (h, p⃗ − p⃗_b) small and b ∈ ℬ̄_*: for each fixed
seminorm ‖·‖_(α) of the space of [[eq:iii-i8-4-2]] there are a seminorm ‖·‖^+_(𝒴(α)) of 𝒴(α), as in [[sec:iii-i8-1]],
and C with |p⃗′_(h,p⃗)(F)| + ‖u‖_(α) ≤ C‖F‖^+_(𝒴(α)), d being large for ‖·‖_(α) ([[sec:iii-i8-1]]); (ii) at fixed b,
if (h_j, p⃗_j) → (0, p⃗_b) and F_j → F in 𝒴(α), then p⃗′_(h_j,p⃗_j)(F_j) → p⃗′_(0,p⃗_b)(F). In compact spatial sets
u = O(t_*^(−α+2+ε)), almost O(t_*⁻¹) as α → 3.
```

**Replacement for 40:748–752** (seven lines for five; the heading of sec:iii-i8-2 follows after the blank line):

```
by ‖u‖_(α′). The bounds of [[prop:iii-i8-4-1]] (i) are taken in a second seminorm ‖·‖^+_(𝒴(α)), the same quotient
norm at a larger regularity and a smaller ε, which depends on the seminorm of the solution bounded and is fixed in the
proof: its step bounds the solution at a lower level α′ in ‖·‖_(α′) by (i) at α′, so its seminorm of the forcing must
bound the seminorm of (i) at α′ as well as ‖·‖_(𝒴(α)). For each seminorm that (i) bounds these choices are finitely
many and are made first; d is then taken so large that the bounds used below hold in them, uniformly for h small:
those of [[lem:iii-i8-2-6]] (b)–(c) and [[lem:s21-motions-at-b]], and the count of Step 0 of the proof of
[[lem:iii-i8-3-2]].
```

Lengths after label resolution: at most 119 and 118 characters.

### m3 (minor) — chapters/40-s21-parameters.md:493–495: the sentence on convergence of forcings (the fixer's lem:iii-i7-4-1 point)

**The problem.** The sentence is not clear enough. It reads "Forcings converge in the finite-regularity spaces on which
the bounds of lem:iii-i7-2-5 (c) hold, …; ‖·‖_𝒴 is the norm of one such space, fixed once and for all."

- The plural carries the right meaning, but the only norm the sentence names is the fixed ‖·‖_𝒴. A reader can take
  "F_j → F in 𝒴" in lem:iii-i7-4-1 to mean convergence in ‖·‖_𝒴 alone.
- Under that reading the proof of lem:iii-i7-4-1 fails, with the same cycle as prop:iii-i15-2-12 (2):
  - the proof needs u_j bounded two orders above the norm in which Ṡ and Q read R_j;
  - u_j is bounded by F_j only through a forward solution.
- The reading the proof needs, and the one its only use (the base of prop:iii-i8-4-1 (ii)) supplies:
  - convergence in each finite-regularity space up to what d allows;
  - this is what lem:iii-i7-3-1 (c) gives for h → 0 in 𝒳^d.

**Replacement for 40:493–495** (six lines for three; the old 496, "𝒴^S_(α,α_+) := …", follows unchanged):

```
vanishes, and (ḃ, S) ↦ ġ_b(ḃ) + h_b(S) is injective ([[sec:iii-i7-1]]). F_j → F in 𝒴 means convergence in each of
the finite-regularity spaces on which the bounds of [[lem:iii-i7-2-5]] (c) hold, up to a regularity that d, being
large, allows; this is what [[lem:iii-i7-3-1]] (c) gives for h → 0 in 𝒳^d. It is not convergence in ‖·‖_𝒴 alone,
which is the norm of one such space, fixed once and for all: the proof of [[lem:iii-i7-4-1]] reads u_j two orders
above the norm in which it reads the parameters, and bounds u_j by F_j through a forward solution. For α and α_+ as
above let
```

Lengths after label resolution: at most 115 characters.

### n1 (nit) — chapters/40-s21-parameters.md:586–588: wording of the definition of ‖·‖^+_𝒴

**The problem.** "the norm of the same kind" should be "a norm": it is not unique. In "bound the forward solutions u_1
below at the regularity", the word "below" can be read as "bound from below".

**Replacement for 40:586–588** (four lines for three; the old 589, "And for F_1, F_2 ∈ 𝒴 …", follows unchanged):

```
(2) Let ‖·‖^+_𝒴 be a norm of the same kind as ‖·‖_𝒴 at a larger regularity and a smaller ε, in which the bounds of
[[lem:iii-i7-2-5]] (c) bound the forward solutions u_1 of the count below at the regularity of ‖·‖_𝒴 plus 2, d being
large enough for [[lem:iii-i7-3-1]] (c) in it as well. For F ∈ 𝒴, Ṡ_(h,p⃗)(F) − Ṡ_(0,p⃗_b)(F) has norm at most
C(‖h‖ + |p⃗ − p⃗_b|)‖F‖^+_𝒴.
```

Lengths after label resolution: at most 114 characters. No line starts with "|".

## The fixer's two reported-only points

### 1. lem:iii-i7-4-1 and 40:493–494

The proof is correct under the reading in which "F_j → F in 𝒴" means convergence in the finite-regularity spaces up to
what d allows (the Fréchet sense, as far as d permits). The sentence does not state this sharply enough; see m3 for the
exact replacement.

### 2. Chapter 46:1386: implied; no sentence needed

Two reasons, either of which suffices.

**(a) The requirement as the fixer frames it does not arise for e_S and e_(S⁰).** They are linear in S′ and S⁰′, the
base-level parameters, so at the base level they change the directions f^S and f^s1 of D_p⃗P_5. ch 46 says they perturb
Step 1 "by terms of the same kind". Those are the terms of 42:406–411, handled as in the paragraph "prop:iii-i8-4-1 for
P_4" (41:970–976).

- **The base step.** They change the boost map and the reduced map through Ṡ and Q. These read their forcing in the fixed
  norm ‖·‖_𝒴 of sec:iii-i7-4 (on 𝒴(α_0)), not in ‖·‖^+.
- **The level map T.** The level step α_0 → α_1 meets them only through D_p⃗P_3 applied to p⃗′_(α_0)(Σe^ν). That needs
  them bounded, not small: p⃗′_(α_0)(L m_ν) = 0 by uniqueness, so T_(0,0) = id still holds.
- **eq:s25-motions-small.** It applies p⃗′_(α_1) only to e_rows(W⃗), the row-direction remainders, and ch 46 changes none
  of them. The ‖·‖^+_(𝒴(α_1)) smallness there concerns r^ν, E^ν, R_q m_rows and Δ_q, which ch 44 (2) already covers
  ("d and the order of the seminorm of q being large").

**(b) Smallness at the order of ‖·‖^+_(𝒴(α_1)) holds anyway.**

- The display at 46:1378 bounds e_S and e_(S⁰) at every order k by C_k(Θ_k + Θ_0‖U‖_(𝒟^(k+5)_ex)), which is
  < 2C_kε_0 for k + 5 ≤ d.
- ch 46 takes d ≥ d′_0 ≥ d_* + 5 (46:1449–1455).
- d_* is the largest order at which the proofs of chapters s19–s25 read smallness. lem:iii-j2-2-3's proof reads Step 3
  of prop:iii-i15-2-5 "through the direct bound … in fixed seminorms", and that bound now goes through
  ‖·‖^+_(𝒴(α_1)) (eq:s25-motions-small). So reg ‖·‖^+_(𝒴(α_1)) ≤ d_* ≤ d − 5.
- The terms are therefore small in ‖·‖^+_(𝒴(α_1)) whether or not that regularity is ≤ m. What is needed is ≤ d − 5,
  not ≤ m.
- Numerically, P-U71-small (c) puts the base norms at regularities ≤ 2R_base + 2, far below m = ρ ≈ C_lev + I_lev.

## What I checked

**The gap.**

- lem:iii-i8-3-2: Step 0 at 40:1002–1005, the bound at 40:1086–1094, and the statement's bound at 40:994–998.
- lem:iii-i7-2-5 (c) (40:356–357 and its proof).
- thm:iii-i-5-3 (38-s19-forward-cone.md:594–606) and cor:iii-h2-5-1 (38-s19-forward-cone.md:1151–1155).
- The old (i) and (ii) at α″ and the old prop:iii-i15-2-12 (2), from the diff.

**sec:iii-i8-1 (40:739–752).**

- The quotient norms and the rule reg ‖·‖_(α′) ≥ reg ‖·‖_(𝒴(α)) + 2.
- ‖·‖^+ at larger regularity and smaller ε, and the requirements on d.

**prop:iii-i8-4-1, statement and proof (40:1127–1255), line by line.**

- **The base.** It rests on continuity on 𝒴(α_0) (cor:iii-i7-4-6 states it, uniformly) and on every continuous
  seminorm being dominated by a quotient norm.
- **"The seminorms".** The order is: target ‖·‖_(α″), then ‖·‖_(𝒴(α″)) (bounding the remainder into the target), then
  ‖·‖_(α′) (≥ +2), then ‖·‖^+_(𝒴(α′)) (from (i) at α′, the induction being over every target), then ‖·‖^+_(𝒴(α″)).
  - There is no circle, and the chain down to α_0 is finite.
  - The comparison holds: each defining space at α″ embeds in the one at α′ with norm inequality (K⁺-weight α″ > α′,
    smaller ε, higher regularity), and the quotient norm takes the infimum over fewer splittings.
- **The level map.** R(S⃗) uses lem:s21-motions-at-b in ‖·‖_(𝒴(α″)) and ‖·‖^+_(𝒴(α′)), with (i) at α′. ‖v(S⃗)‖_(α′) uses
  lem:iii-i8-2-6 (b) in ‖·‖^+_(𝒴(α′)). The Step 0 count is from ‖·‖_(α′) to ‖·‖_(𝒴(α″)). T is independent of the
  seminorms, so the smallness for its invertibility may be taken from any one choice.
- **(i) at α″.** Every inequality checked: G(0), u(0), C(0), S⃗, F(S⃗) in both seminorms, p⃗′_(α′)(F(S⃗)), G(S⃗), u(S⃗),
  and the remainder bound into the target.
- **(ii) at α″.**
  - The w_j are bounded in a target two orders above ‖·‖^+_(𝒴(α′)), with Φ_j convergent at the needed regularity.
  - (L_j − L_0)w_j → 0 in ‖·‖^+_(𝒴(α′)). The count needs only K⁺-weight α′ − 2 − ε + a_K > α′.
  - ‖w_j − w‖_(α′) ≤ C‖R_j‖^+_(𝒴(α′)) holds, and this is what lem:iii-i8-3-3 needs.

**thm:iii-i11-4-1's end (41:1031–1042).**

- Order of choice: ‖·‖_(𝒴⁰(α)) (lem:iii-i11-3-2), then ‖·‖_(w_0), then ‖·‖_(α′) (as in lem:iii-i11-3-3), then
  ‖·‖^+_(𝒴(α′)), then ‖F‖.
- Inclusion 𝒴⁰(α) ⊂ 𝒴(α′) is continuous. Every bound checked.

**prop:iii-i15-2-5 (44:264–477).**

- The induction bound at k = 0, (1)–(4) with (2) in ‖·‖^+_(𝒴(α_1)), the change of motion coordinates along 𝒫_k, and the
  bound on A_k.

**prop:iii-i15-2-12 (2) (40:586–637).**

- The definition of ‖·‖^+_𝒴, both counts, and the Q bound: C‖R‖_𝒴 ≤ C‖F_1 − F_2‖_𝒴 + C(…)‖F_1‖^+_𝒴.
- The boost map's second term, with f^S_(0,p⃗_b) smooth at h = 0.
- The reduced map:
  - ‖F_(h,p⃗)‖^+ ≤ C per unit, via |A_(h,p⃗)| ≤ 2C‖f^(=0)‖_𝒴 and lem:iii-i7-3-1 (c) with d large;
  - f^(=0)_(0,p⃗_b) in ‖·‖^+ serves the A comparison.
- lem:iii-i8-3-1's transfer to 𝒴(α_0) (40:974–983).
- The comparison with prop:iii-i15-2-8 (39:873–923), which already measures the smooth source in a larger norm.

**Uses, by grep over chapters 38a–46 and 71** for prop:iii-i8-4-1, prop:iii-i15-2-5, prop:iii-i15-2-12,
thm:iii-i11-4-1, sec:iii-i8-1, lem:iii-j2-2-3, "fixed seminorm" and the 𝒴(α) seminorms.

- **Chapter 40.**
  - Lines 19, 66, 77, 446, 573, 636 and 1697.
  - lem:iii-i8-3-2 and lem:iii-i8-3-3, which use only the fixed pair.
- **Chapter 41.**
  - Lines 67, 122, 227, 869, 918–936 (lem:iii-i11-3-3: u_j bounded in the Fréchet space, so R_j → 0 in ‖·‖^+), 963,
    970–979 (P_4 transfer), 1001, 1014–1027, 1033–1041.
  - Lines 1428–1431 and 1459–1461, which give m1.
  - Lines 1588, 1599, 1618–1620 (lem:iii-i13-2-3, as lem:iii-i11-3-3), 1627–1633, 1719–1720, 1733–1738.
- **Chapter 42.** Lines 143, 144, 401–416, 454.
- **Chapter 43.** Lines 213, 304–320, 378, 387–418.
- **Chapter 44.** Lines 57, 320–324, 328–393, 508–510, 602, 644, 681–685, 699–702.
- **Chapter 46.** Lines 1384–1393 and 1449–1455.
- **Chapter 71.** Lines 1757–1760, 1831, 1899, 2300, 2336, 3858–3882, 4195, 4239–4243 and 4250–4254. These are charges
  along chains, which the loss form of (i) matches.
- Chapters 38a, 39 and 45 have no uses.
- No statement changed in substance. Every use follows, except the wording in m1.

**proofs/P-U71-small.md.** I read lem:uc-small-orders, its proof and rem:uc-small-reading.

- (c) already reads (i) as a base map, from the forcing at the order of the seminorm plus 2 + R_base.
- So the new ^+ norms lie within 2R_base + 2, and no figure moves.

**Contract.**

- Every line changed by the two commits, in chapters 40, 41 and 44, is at most 121 characters both in source and after
  label resolution. This was computed with assemble.py's own numbering in memory, without writing.
- No changed line starts with "+ ", "- ", "* ", "> ", "#", "=" or "|".
- The changed lines have no backslash and no file, program, code or AI language.
- All replacement texts above were checked the same way.

**Checks run from the paper directory.**

    $ python3 lint.py --chapters
    chapters: 62 file(s), 4570 label(s) defined, 0 hit(s)

    $ python3 assemble.py --check
    labels 4570, computations cited 0, problems 0
