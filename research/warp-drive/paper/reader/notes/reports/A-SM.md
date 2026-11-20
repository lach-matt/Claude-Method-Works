# A-SM: does the proof of thm:settling use the smallness of the parameters only through the listed conclusions?

Read-only audit. Paper: `research/warp-drive/paper/reader/`, working tree of 2026-11-20. References `NN:line` are to
`chapters/NN-*.md`. Another agent was editing chapter 33 during this audit: its labels moved by up to about 200 lines
between my reads, so ch. 33 sites are cited by label, and "≈" marks a line as of my last read. Nothing in the
repository was changed, and `assemble.py` was not run. This is step 1 of the plan in S-INSIDE §4.

## Answer in brief

- **In substance, yes.** Every *existential* threshold on h, γ_(Υ,H), e_Υ, γ_Υ or z enters the proof of
  thm:settling only through the conclusions of these results:
  - thm:iii-e-1-1;
  - prop:iii-d1-4-1;
  - prop:iii-f1-3-3;
  - prop:iii-f1-2-3 (e), which is where z ∉ 𝖹_exc is used.

  I found no use of type (b) with an existential threshold. The two sites S-INSIDE names to check, 37:54 and 46:92,
  are (a).
- **Literally, no.** The list leaves out three explicit inequalities that the proof uses directly:
  - s_C > 100;
  - 0 < γ_Υ < ¼;
  - 0 < e_Υ < 1.

  These give γ_Υ < min(⅜, ½s_C) and z ∈ (0, ¼) at no cost. They must stay in the definition, and they hold at the
  computational point.
- **Several entries ask for more than the proof uses:**
  - z ∉ 𝖹_exc is used only through "every indicial root of L̂_b(0) is simple".
  - lem:iii-d-7-1 is used only inside the proof of prop:iii-d1-4-1.
  - thm:iii-e-1-1 (4) is used only inside the proof of prop:iii-f1-3-3 (Step 4).
  - (C4) is used only through ε_ind > 0.
  - (C2)–(C3) are used only through simplicity.
- **A lead, not fully verified.** Every use of simplicity I traced concerns roots with real part in (−3, 0]. There,
  simplicity holds for every z ∈ (0, ½], by bounds already in the proof of prop:iii-f1-2-3 (e). If no other use exists,
  u5, (C2) and (C3) can be dropped.
- **At the computational point** (10⁻⁶, 1/100, 1/100), h = 10⁻⁶ is no longer excluded by definition. Admissibility
  reduces to two certifications at γ_C = 10⁶ and (1/100, 1/100):
  - thm:iii-e-1-1 (1), the invertibility in (2), and (4);
  - the conclusion of prop:iii-d1-4-1, for some γ_(Υ,H).

  Everything else is explicit, already proved, or with the other agents. One caveat: an explicit γ_1 certifies
  prop:iii-f1-3-3 only together with thm:iii-e-1-1 (4) at γ_C = 10⁶, which its Step 4 uses.

---

## 1. Uses found

**Search.** I searched chapters 20–48 and 60–66 for:
- the patterns asked for;
- "small", "≪", "threshold" and "small enough";
- ε_0, ε_1, ϵ_0, ϵ_1, γ_1, γ_2 and ε_L;
- "γ_Υ = 0", "z → 0" and "homotop";
- 𝖹_exc, (C1)–(C5), s_C and 10⁻⁶;
- every line naming γ_Υ, e_Υ, γ_(Υ,H) or z_Υ.

I read each hit in context and traced it to the results it feeds. I then checked every downstream citation of
thm:iii-e-1-1 (by part), prop:iii-d1-4-1, lem:iii-d-7-1, prop:iii-f1-3-3, prop:iii-d-6-1, prop:iii-d-6-3,
lem:iii-d-5-1, prop:iii-f1-2-3 (e)–(f) and (C1)–(C5).

**Classes:**
- **(a):** used only through a listed conclusion.
- **(b):** smallness used directly, not covered by the list. All such uses found are explicit inequalities, marked
  (b-E).
- **(c):** harmless.

### 1.1 The damping parameter h (γ_C = h⁻¹)

| site | use | class |
|---|---|---|
| eq:iv4-0-1 (33:110–128); row c2 (46:1713); step (1) (46:1787) | h ∈ 𝖧 = (0, h_*) ∖ 𝖹, with h_* = min(10⁻⁶, h_0, h_tf) | (a). 𝖧 only makes thm:iii-e-1-1 hold. 33:125–127 says so: later results need the conclusions "for every γ_C > 1/h_* outside a countable set, which is what every later use requires, as each takes one admissible γ_C" |
| ch. 33: "for all sufficiently small h" and "absorbing for h small" (about 35 hits, in thm:iv5-7-3, prop:iv5-1-2 to prop:iv5-7-2, lem:iv5-8-1, thm:iv6-2-1, thm:iv6-3-1, lem:s14-small-h, lem:iv4-1-3) | inside the proofs of thm:iv4-2-1 (= thm:iii-e-1-1 (1)–(3)) and thm:iv6-4-1 (= (4)) | (a) |
| 𝖹₁ (lem:iv4-1-3 (b), 33:1121) | h off a countable set, so that (C2)–(C4) hold | (a): conclusions (C2)–(C4) |
| 𝖹₂, 𝖹₃ (prop:np-10-52 (ii)–(iii), 33:≈3025) | the entries of the lists ℛ_l are pairwise distinct, and ε_ind(h) > 0 | (a): these are the conclusions of prop:iii-f1-2-3 (e) and (f). See side finding 2 |
| the cap 10⁻⁶ | used only through prop:np-10-54 and lem:iv4-1-3, which give (C1)–(C4) on (0, 10⁻⁶], and through s_C > 100 and (C5) | (a) / (b-E). No other use |
| (C1) (sec:iii-f1-1, 34:285) | the list of roots in prop:iii-f1-2-3, and its (d); prop:iii-f1-3-3 Step 3 (34:661); thm:iii-g-5-1 (35:938); 35:53; 37:54 | (a): thm:iii-e-1-1 (3) |
| (C2)–(C3) (34:290–294) | used only in prop:iii-f1-2-3 (e) (34:479–483) and in the setting of sec:iii-g2-1 (35:1424), that is, only for simplicity | (a): thm:iii-e-1-1 (3) |
| (C4) (34:295) | used only in prop:iii-f1-2-3 (f) (34:496), to get ε_ind > 0 | (a): thm:iii-e-1-1 (3) |
| thm:iii-e-1-1 (1) | 34:1079 (prop:iii-f2-3-1, at b₀) | (a) |
| thm:iii-e-1-1 (2) | 34:1079, 34:1431, 34:1868; lem:iii-e-2-1 (33:≈2664), which feeds prop:iii-e-3-1 and prop:iii-e1-3-1 (the dual states, used in sec:iii-f4 and later) | (a) |
| thm:iii-e-1-1 (4) | only at 34:663 (prop:iii-f1-3-3, Step 4) | (a). Redundant once the conclusion of prop:iii-f1-3-3 is assumed |
| s_C := (1 − e_C)(1 − v_C)γ_C > 100. Sites: 34:76; 38:53; 38:1200–1202; 45:53; 45:802; 46:90–91 ("as h < 10⁻⁶, s_C > 100"); 46:1720–1721; row d2 (46:1772). The bound ℓ_I < 3/2 + s_C at 35:1188 and 36:647 | uses the smallness of h directly | **(b-E).** It needs "s_C > 100", that is h < (1 − e_C)/200 ≈ 5.0·10⁻³. This is not one of the listed conclusions, and (C5) (h ≤ 1) does not give it |
| (C5) γ_C v_C ≥ ½ (35:1433, 41:119) | gives ℓ_K^max = 3 | in the list (explicit) |
| lem:iii-f2-1-1 (34:737) | ϑ_L = max(0, 2 − 2a_vγ_C r_h), valid for every γ_C | (c) |
| lem:iv4-1-5, lem:iv4-1-6 (33:1187, 33:1200) | the horizon threshold and (H1)–(H4) for □^C, valid for every h ∈ (0, 10⁻⁶] | (a): part of thm:iii-e-1-1 (2) |

### 1.2 The gauge parameters γ_(Υ,H), e_Υ, γ_Υ and z

| site | use | class |
|---|---|---|
| **46:92** (sec:iii-k-0, *Parameters*) | "γ_(Υ,H), e_Υ, γ_Υ small enough for the mode stability of prop:iii-d1-4-1 and the tf-admissibility of prop:iii-f1-3-3" | **(a).** It does not name lem:iii-d-7-1, which is consistent with §2 |
| **37:54** (sec:iii-h-1) | "(Dyn), condition (C1) … and γ_Υ small" | **(a).** This is the only mention of a gauge parameter in ch. 37. The chapter uses (TF) from prop:iii-f1-3-3 (37:69, 37:749) and the gap β^L_+ > 1 from prop:iii-f1-2-3 (a), which is explicit for z ∈ (0, ½] |
| 35:54; thm:iii-g-5-1 (35:938), "the parameters of prop:iii-f1-3-3" | injectivity for Re ϰ < 2 uses only tf-admissibility (35:581) | (a) |
| 34:73–74 (sec:iii-f-1) | "0 < e_Υ ≪ 1 and 0 < γ_Υ ≪ 1 as prop:iii-d1-4-1 allows, so that … □^Υ_b is mode stable" | (a) |
| 34:278–281 (sec:iii-f1-1, *Parameters*) | used by prop:iii-f1-3-3; by prop:iii-f2-3-1 (34:1068: "those of prop:iii-d1-4-1"); and by sec:iii-f3-1 (34:1126) | (a) |
| 32:1165–1170 (setting of sec:iii-d2-1) | "Fix γ_(Υ,H) ∈ (0, ϵ_0] … as in prop:iii-d1-4-1". It uses the invertibility of (□^Υ_b)^(0) (prop:iii-d1-4-1, lem:iii-d1-5-1) and z ∈ (0, ½] | (a) |
| prop:iii-d-6-3 (32:730): \|e_Υ\|, \|γ_Υ\|, \|γ_(Υ,H)\| < ϵ | used only inside the proof of prop:iii-d1-4-1 (32:1106–1114), and in thm:vi-c-2-1 step (2), which notes that prop:iii-d1-4-1 implies it (46:1795–1797) | (a) |
| lem:iii-d-7-1 (32:780; "Small γ_Υ" at 32:788–801) | (TF) for □^Υ. Cited only at 32:827 (sec:iii-d1-1), for the proof of prop:iii-d1-4-1 (Step 1 at 32:1064, and Step 2 (i)), and in rows u3–u4. It is also cited at 65:448 and 66:911, but at γ_Υ = 0 and for other theorems | (a). Redundant given the conclusion of prop:iii-d1-4-1 on a neighbourhood of b₀ |
| prop:iii-d1-4-1 (32:1041); prop:iii-f1-3-3 (34:635, Step 6 at 34:669–676) | the listed results themselves; their internal uses of smallness lie inside their proofs | listed |
| ε_Υ (sec:iii-d2-1) | fixed by the roots of (□^Υ_b)^(0) for 0 < z ≤ ½ | explicit; no smallness |
| (R1)–(R5) (32:1839–1850), and the ranges in prop:np-10-29 and prop:np-10-30 (z < 4, 20/3, 40/7) | "all hold for 0 < z ≤ ½" | (b-E): z ∈ (0, ½], which follows from γ_Υ < ¼ and e_Υ < 1 |
| z ∉ 𝖹_exc: row u5 (46:1736), step (2) (46:1793–1795), 35:1424–1426, 36:1138 | always used through "every indicial root of L̂_b(0) is simple" (prop:iii-f1-2-3 (e)) | (a): the conclusion is simplicity. See the lead in §2 |
| 0 < γ_Υ < ¼ and 0 < e_Υ < 1. Sites: eq:iii-c-1-1 (36:61–67); 38:52–53; 39:56; 40:1284; 45:53; 36:1057; row d1 (46:1769, 46:1848); 62:559 | λ_♯ < 7/4; δ_♯ < ¼; σ_Υ ⊂ [0, ½); min Re ℰ_0 > 3/2 + 2γ_Υ; the conditions on ℰ_I^C | **(b-E):** the inequality itself |
| γ_Υ < min(½s_C, ⅜). Sites: lem:iii-g1-1-1 (35:1026); thm:iii-g1-3-1 (35:1180, "the smallness 0 < γ_Υ ≪ 1 of [Hin26]"); 35:1424; 36:643; 36:673 | S̄ is semisimple and its eigenvalues are separated | **(b-E).** Implied by γ_Υ < ¼ and s_C > 100 |
| the gauge in the weights: ε_K < δ_♯, ℓ_I ∉ 3/2 + σ_Υ, and η < (1 − e_Υ)γ_Υ (38:1273, 45:799) | rows w1 and d2 | explicit; unchanged |

### 1.3 Continuity statements on compact parameter sets: all (c)

- **lem:iii-d-5-1 (32:407).** ϑ_ℋ = 1 for every γ_(Υ,H), and ϑ_ℋ < 1 + δ near b₀ "and (e_Υ, γ_Υ, γ_(Υ,H)) in a compact
  set".
- **prop:iii-d-6-1 (32:575).** Invertibility at high energy for parameters "in a fixed compact set".
- **lem:iii-f2-1-1 (34:737) and cor:iii-f2-1-2 (34:806).** The thresholds and C_hf, with continuity on compact sets.
- **lem:iii-f1-2-4 (34:499) and lem:iii-f1-3-2 (34:623).** Uniform over compact parameter spaces; used only inside
  listed proofs.

At a fixed parameter point, each applies with the compact set {that point}. None imposes a threshold.

### 1.4 Hits that are not about parameter smallness

- **"h small" with a different h.** In ch. 21 and 27, h is the abstract semiclassical parameter. At 35:914 and 35:922
  it is |Im ϰ|⁻¹.
- **h as the metric perturbation.** In ch. 38–47 (38:234, 39:562, 40:166 ff., 45:529 ff., 46:58 ff.), "h small" refers
  to the metric perturbation h, that is, to data smallness (row n1).
- **The remaining "threshold" and "small enough" hits in ch. 37–47.** These are:
  - radial-point thresholds;
  - thresholds on ‖P − P_0‖ over ℬ_*, which are b-neighbourhoods (38:618–764, 38:1083–1136);
  - the Nash–Moser thresholds ε_NM and ε^G_NM;
  - the cut-off time T_K;
  - gluing data (47:574, 47:610).

None of these depends on the gauge or damping parameters, so the reformulation does not affect them.

### 1.5 Chapter 60, and chapters 61–66

- **Chapter 60.** It takes every parameter from thm:vi-c-2-1 and cor:s27-rate (60:55–68, 60:235–238, 60:287–296) and
  makes no direct use of gauge or damping smallness.
- **Chapters 61–66.** They prove other theorems, the ones listed in ch. 03 under *Further results*. Their uses of the
  gauge are explicit (γ_Υ < ¼ at 62:559 and 66:616) or taken at γ_Υ = 0, for the unmodified □ (65:447–448, 66:816,
  66:911).

---

## 2. Verdict

**Does the reformulation hold as stated? In substance yes; literally no.**

*Why yes, in substance.*
- The proof never uses that a gauge or damping parameter lies below h_0, h_tf, ε_0, ε_1, ε_L or γ_1, or outside 𝖹 or
  𝖹_exc, except to invoke the conclusions of the listed results at the one chosen point.
- The order of choices in thm:vi-c-2-1 exists only to make those conclusions hold. No later step reads the thresholds
  themselves, and none needs uniformity over an interval of parameters.
- I found no type-(b) use with an existential threshold.

*Why no, literally.* The list omits the explicit inequalities of §1.1–1.2: s_C > 100, 0 < γ_Υ < ¼ and 0 < e_Υ < 1.
(C5) is in the list, but it means h ≤ 1, while s_C > 100 means h < 5·10⁻³ approximately.

**The minimal list that makes it hold.** At a point (h, γ_(Υ,H), e_Υ, γ_Υ):

- **E (fixed data and explicit inequalities).**
  - (v_C, e_C, C_0) = (½, 1/102400, 100), and the 1-forms of row u1.
  - s_C > 100 and (C5).
  - 0 < e_Υ < 1 and 0 < γ_Υ < ¼. Together these imply z ∈ (0, ¼) ⊂ (0, ½] and γ_Υ < min(⅜, ½s_C).
- **D1.** thm:iii-e-1-1 (1) and (2), for b near b₀.
- **D2.** From thm:iii-e-1-1 (3), the clause (C1) of sec:iii-f1-1. In place of (C4), its only use: ε_ind > 0, that is,
  no non-integer root of L̂_b(0) with |ι| ≤ 50 has integer real part (the conclusion of prop:iii-f1-2-3 (f)).
- **G1.** The conclusion of prop:iii-d1-4-1, for one γ_(Υ,H), on a neighbourhood ℬ(γ_(Υ,H)) of b₀.
- **G2.** The conclusion of prop:iii-f1-3-3.
- **S.** Every indicial root of L̂_b(0) is simple (the conclusion of prop:iii-f1-2-3 (e)). This replaces z ∉ 𝖹_exc.
  (C2)–(C3) are then not needed separately, because their only use is (e).

**Not needed by the proof**, though each is useful for certifying the items above:

- **lem:iii-d-7-1.** Used only inside the proof of G1. It is needed again if G1 is certified at b₀ alone and then
  extended to a neighbourhood by the low-energy step of prop:iii-d1-4-1, because thm:i-c-7-1 and thm:i-c-6-4 need (TF).
- **thm:iii-e-1-1 (4).** Used only inside the proof of G2 (Step 4, weights in (1, 2)).
- **z ∉ 𝖹_exc, 𝖹 and 𝖹₁–𝖹₃ as such.** Only their conclusions are used.
- **The cap h < 10⁻⁶ and the open interval (0, h_*).**

**A lead that would remove S (not fully verified).** Every use of simplicity I traced concerns roots μ with
−3 < Re μ ≤ 0:

- 35:1424–1426, and 35:1493 (lem:iii-g2-1-2, for μ ∈ 𝒲(ℓ_K) with ℓ_K < 3);
- 36:1162 (lem:iii-g4-1-1 (2));
  - used at 36:1360 in strips with −μ ∈ (β_ztf, w₀), w₀ < ℓ_K^max (36:1262);
  - and at 36:1423 and 36:1698, over 𝒲(w₀) and 𝒲(w);
- 41:1205 (roots in 𝒲).

*Why simplicity is automatic in that window.*
- No root in the window comes from □^C. The roots ι^C_≪ − 1 lie below −101 by (d). The root −2 − 2γ_C v_C is at most −3
  by (C5). See "Completeness of the list" at 35:1482–1485.
- The remaining entries lie in pairwise disjoint intervals for every z ∈ (0, ½], by the bounds at 34:475–479.
- The index set ℰ_K (35:1086–1105) allows logarithms and assumes nothing about roots below −101.

If a line-by-line check finds no use outside the window, then S, (C2) and (C3) drop out, and so do u5 and T9 of
S-INSIDE. I did not finish that check. At the computational point the window is covered anyway, by prop:is-mult
(71:2843), which proves simplicity on [−101, 5].

**Side findings (none affects the proof).**

1. 41:123–124 and 42:559 credit "s_C large" to "(C1) of ch:s15". It comes instead from the explicit condition of
   sec:iii-f-1 (34:76) and row c4. Under the reformulation it must be stated separately, as in E.
2. Row c2's 𝖹 includes 𝖹₂ and 𝖹₃, which are defined at z = 4·10⁻⁶. sec:s14-simple (33:≈3005) says "(e_Υ, γ_Υ) =
   (1/100, 1/100) are the constants of the gauge modification". But thm:vi-c-2-1 chooses h before the gauge, so for any
   other gauge these sets are a superfluous excision, countable and harmless. They disappear under the reformulation.
3. 46:92 names prop:iii-d1-4-1 and prop:iii-f1-3-3 but not lem:iii-d-7-1, which agrees with the finding above.

---

## 3. The reformulated definition

This is written to replace rows c2–c4 and u2–u5 of sec:vi-c-1, and steps (1)–(2) of thm:vi-c-2-1.

> **Definition {#def:vi-c-admissible}** (Admissible parameter points.) Fix (v_C, e_C, C_0) := (½, 1/102400, 100), the
> damping 1-form c_C of [[sec:iv4-0]] and the gauge 1-forms c_Υ = ζ(|x|)|x|⁻¹dt, c_(Υ,H) = −½χ(|x|)d|x| of row u1. For
> h > 0 put γ_C := h⁻¹ and s_C := (1 − e_C)(1 − v_C)γ_C, and for e_Υ, γ_Υ put z_Υ := 4e_Υγ_Υ². A point
> (h, γ_(Υ,H), e_Υ, γ_Υ) with γ_(Υ,H) > 0 is *admissible* if:
>
> (P0) s_C > 100, γ_C v_C ≥ ½ (the condition (C5)), 0 < e_Υ < 1 and 0 < γ_Υ < ¼; hence z_Υ ∈ (0, ¼) and
> γ_Υ < min(⅜, ½s_C);
>
> (P1) the conclusions (1) and (2) of [[thm:iii-e-1-1]] hold at γ_C for all b in a neighbourhood of b₀, and its
> conclusion (3) holds at least in the form (C1) of [[sec:iii-f1-1]];
>
> (P2) no non-integer indicial root ι of L̂_b(0) with |ι| ≤ 50 has integer real part, so that a number ε_ind ∈ (0, 1]
> with [[eq:iii-f1-2-2]] exists;
>
> (P3) there is a neighbourhood ℬ(γ_(Υ,H)) of b₀ such that for every b ∈ ℬ(γ_(Υ,H)), (□^Υ_b)^(σ) is invertible for
> every σ with Im σ ≥ 0, as a map 𝒳_σ → 𝒴_σ when σ ≠ 0, and as a map 𝒳_0 → 𝒴_0 for every s > 3/2 and every α with
> α + 2 ∈ (0, ι^Υ_(s1,2)) when σ = 0 (the conclusion of [[prop:iii-d1-4-1]]);
>
> (P4) for every b near b₀, L_b^(·) is tf-admissible ([[def:i-c-5-1]]) with every weight β ∈ (0, 1] (the conclusion
> of [[prop:iii-f1-3-3]]);
>
> (P5) every indicial root of L̂_b(0) is simple (the conclusion of [[prop:iii-f1-2-3]] (e)).
>
> The *proved set* is the set of admissible points. [[thm:settling]] holds at every admissible point, with the
> remaining choices (rows b1–b4, d1–d2, w1–w2 and n1) made as in steps (0) and (3)–(6) of [[thm:vi-c-2-1]].

**Notes for integration.**

- **The proved set grows and stays non-empty.** Every point that the old steps (1)–(2) produce is admissible:
  - P1 and P2 hold by thm:iv4-2-1, and by (C4) with (f);
  - P3–P5 hold by the cited results;
  - P0 holds because γ_C > 10⁶.

  So the new proved set contains the old one. thm:vi-c-2-1 needs only "choose an admissible point" in place of steps
  (1)–(2).
- **Later rows read the point only through derived numbers.** P1–P5 depend on the point alone. The thresholds of the
  later rows see it only through s_C, δ_♯, ε_ind, ε_Υ, σ_Υ, Λ and the neighbourhoods. Row b2's ℬ(γ_(Υ,H)) is the
  neighbourhood of P3.
- **If P3 is certified only at b₀,** add (P3′): the conclusion of [[lem:iii-d-7-1]]. The low-energy step of the proof
  of prop:iii-d1-4-1 (Step 2 (i)) then supplies the neighbourhood.
- **If P4 is certified through the proof of prop:iii-f1-3-3,** that proof also uses thm:iii-e-1-1 (4), at weights in
  (1, 2).
- **If the lead of §2 is confirmed,** delete P5, and P1 can then cite (C1) alone.
- **Wording that stays and wording that changes.**
  - The wording of thm:settling itself ("ε_ind the index distance", δ_♯, (G⁺), (G)) is unchanged.
  - rem:ec-point-outside and G-SWEEP C7 would change: under this definition h = 10⁻⁶ is not excluded by construction,
    and the point's admissibility is undecided in all four parameters.

---

## 4. What the computational point would still need

The point is (h, e_Υ, γ_Υ) = (10⁻⁶, 1/100, 1/100), so γ_C = 10⁶ and z = 4·10⁻⁶. γ_(Υ,H) is free.

| item | status at the point | route |
|---|---|---|
| P0 | **holds**: s_C = 499995.117…, γ_C v_C = 5·10⁵, e_Υ = γ_Υ = 1/100 | explicit |
| P1: (C1) | **proved**. prop:np-10-54 and lem:iv4-1-3 (a) hold on the closed interval (0, 10⁻⁶] | done |
| P1: (H1)–(H4) and ½ + ϑ_ℋ < −C_0, both part of (2) | **proved** for every h ∈ (0, 10⁻⁶] (lem:iv4-1-5, lem:iv4-1-6) | done |
| P1: (1), and the invertibility in (2) | **open.** thm:iv4-2-1 rests on thm:iv5-7-3, whose h_0 is existential | research level: the "T2 alternative" of S-INSIDE, harmonic by harmonic at γ_C = 10⁶, with large l handled by asymptotics and finitely many l by validated numerics. It is needed at b₀; the step to b near b₀ uses (4), which concerns the model only |
| P2 | **proved.** cor:s14-eps-ind-point gives ε_ind(10⁻⁶) = δ_50 > 0, and prop:s14-damping-distance covers every root with \|ι − 1\| ≤ 50. The full (C4) is not proved, and it is not used | done |
| P3 | **open.** The ε_0 and ε_1 of prop:iii-d1-4-1 come from contradiction and finite covers | research level: T6 direct, i.e. mode stability of □^Υ_(b₀) at (1/100, 1/100) for one γ_(Υ,H), enhanced at σ = 0. Then P3′ gives the neighbourhood |
| P3′ (lem:iii-d-7-1) | with the agent making ε_L explicit. Self-contained: the model at γ_Υ = 0 plus a perturbation, independent of h | done if ε_L > 1/100; otherwise prove tf-admissibility at γ_Υ = 1/100 directly (T7) |
| P4 | with the agent making γ_1 explicit. **But** the proof of prop:iii-f1-3-3 also needs thm:iii-e-1-1 (4) at γ_C = 10⁶ for weights β_C ∈ (1, 2) (Step 4, 34:663). That rests on thm:iv6-3-1, whose h_tf is existential and capped at 10⁻⁶ | an explicit γ_1 **and** T3: kernel triviality of the tf model of □^C at γ_C = 10⁶, one ODE per harmonic, about 800–2,000 lines by S-INSIDE's estimate |
| P5 | proved for real parts in [−101, 5] (prop:is-mult, 71:2843). Below −101 it is with the agents deciding 𝖹 and 𝖹_exc | at this point the two decisions are one computation: z ∉ 𝖹_exc(10⁻⁶) and h ∉ 𝖹₂(4·10⁻⁶) both say that no real root of □^C meets ι^Υ + 2 or 3 − ι^Υ, and with (C2)–(C3) (that is, 𝖹₁) they give P5. **If the lead of §2 holds, P5 is already met and none of this is needed** |
| rows d1–d2 and w1–w2 | **hold** at the choice of ch. 71 (lem:uc-admissible): min Re ℰ_0 = 2 > 1.52, δ_♯ = 0.0099, ε_ind = δ_50 | done |
| rows b1–b4 and n1 | neighbourhoods and data smallness; no number from them enters d | harmless |

**Summary.**

- **No definitional obstacle remains.** Under the reformulation, the open interval, the cap 10⁻⁶ and the existential
  h_0 and h_tf no longer exclude the point.
- **Four certifications remain**, at γ_C = 10⁶ and (1/100, 1/100):
  1. thm:iii-e-1-1 (1);
  2. the invertibility in thm:iii-e-1-1 (2);
  3. thm:iii-e-1-1 (4) (weights in (1, 2) suffice for P4);
  4. P3.
- **Cost.**
  - Items 1, 2 and 4 are research level, out of reach with present methods (T2, T5–T6 of S-INSIDE).
  - Item 3 is T3, of moderate cost.
- **What the other agents' work settles.** ε_L, γ_1, 𝖹 and 𝖹_exc settle P3′, the γ_Υ part of P4, and P5. The window
  argument may already settle P5.
- **Cheapest decisive next steps:**
  1. confirm or refute the lead of §2;
  2. then T3, which together with an explicit γ_1 certifies P4.
