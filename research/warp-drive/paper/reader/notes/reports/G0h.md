# G0h: the fifth sharpening (P-GRD5) at levels 4 and 6, on D_A and D\*, both seeds

Report only. I edited no repository file and committed nothing. Every run was launched from `scratchpad/g0h/` with
absolute paths. I read nothing under method/, drive/, extracted/ or recovered/.

**What I evaluated.** P-GRD5 as confirmed: c3506861, md5 6ed9c262, merged as sec:tl5-hfv at 86f3d84e. The reader's two
corrections are in:
- **m1:** the pair (𝔣₂^o, 𝔣₂^i) is used only where c/z̲² + 1/z̲ ≤ 2, and (𝔣₂, 𝔣₂) elsewhere;
- **n2:** at a given η the cap is largest at ϑ₁ = ϑ₂, so the split can help only through the rates.

I read the draft (f49900d7) whole and the fix diff.

**Labels:**
- **computed**: floating point, mine; scripts under `scratchpad/g0h/` (§G0h.7);
- **deduced**: an argument or bookkeeping given here;
- **record**: G0g, G0f or P-GRD5, cited.

**Evaluated as in G0g and G0f.**
- **Unchanged:** intrinsic Sobolev constants with the rigorous C_(E,r)² bounds, α, β, ρ optimised per face (per t at level
  4), the same approximants, growth model and couplings.
- **Level 4:** P-GRD4's θ-family with the index-v replacements: 𝔨_rec, C_P^v, C_(P,ϱ)^v and C_(P,0)^v. C_P^v also
  enters the A-term of 𝔰_\*, since it is the m = 0 constant of the same bound (lem:tl5-hfv-rec). The ν-terms of 𝔰_\* keep
  P-GRD4's constants.
- **Level 6:** P-GRD3's options (a) and (b) with the index-v replacements.
- **Both levels:**
  - cap 𝔰_(θ,v);
  - 𝔣₂ by the m1 rule;
  - 𝔨_B = max(𝔷, 𝔤₁);
  - closing 4η^(−3/2)(δ_w + η^(−1/2)(ε^v + ε_M^v))(S_F^v + S_M^v) ≤ 0.1, with margin 10 and δ_w ≤ ε;
  - A_v = η^(−1/2)δ_w + η⁻¹ε in 𝔰_\*;
  - η = 1 − max(ϑ₁, ϑ₂) − 𝔯, with the 𝔯 budget r split equally between ϱ and η₀.

**New rates (computed).** For each (ϑ₁, ϑ₂) the rays of 𝔅_N itself were computed, and P-GRD5's LP was solved:
- minimise ∫ â_o du/(1 − ϑ₁) + ∫ â_i dv/(1 − ϑ₂), with (â_o, â_i) admissible for 𝔅_N;
- then a_o = â_o/(1 − ϑ₁) and a_i = â_i/(1 − ϑ₂);
- one LP per unequal pair and one per μ for all equal pairs;
- 8 LPs per μ, about 5 s each at level 4 and more at level 6.

**Grid:**
- ϑ₂ ∈ {0.003, 0.01, 0.03, 0.1, 0.2, 0.3, 0.5};
- ϑ₁ ∈ {ϑ₂, cap-matched}. Cap-matched is the least ϑ₁ that leaves the Σ₂ cap binding: ϑ₁ = ϑ₂ · 0.19 on D_A and
  ϑ₂ · 0.044 on D\*, floored at 10⁻³;
- r ∈ {0.01, 0.03, 0.1, 0.2};
- θ ∈ {0, ¼, ½, ¾, 1} at level 4; options (a), (b) at level 6;
- 𝔰_♭ ∈ {1/8, …, 10⁻¹²};
- μ ∈ {10⁻⁴, 3 × 10⁻⁵, 10⁻⁵, 3 × 10⁻⁶, 10⁻⁶}. Every optimum is interior.

Pages are not reported, as asked.

---

## G0h.0 Headline (computed; P-GRD5 as confirmed)

| | seed 1, D_A | seed 2, D_A | seed 1, D\* | seed 2, D\* |
|---|---|---|---|---|
| **Level 4: f** (G0g) | **10^−29.5** (−30.2) | **10^−27.7** (−28.5) | **10^−36.0** (−36.9) | **10^−32.6** (−33.4) |
| ϱ at the optimum (G0g) | 10^−32.0 (−32.4) | 10^−31.5 (−30.9) | 10^−39.5 (−39.6) | 10^−38.7 (−36.9) |
| η₀ | 10^−22.9 | 10^−21.2 | 10^−28.3 | 10^−24.7 |
| ϑ₁ / ϑ₂ / 𝔯 / θ / μ / 𝔰_♭ | 0.0019 / 0.01 / 0.01 / ½ / 10⁻⁵ / 10⁻⁴ | 0.001 / 0.003 / 0.01 / ¾ / 10⁻⁴ / 10⁻⁴ | 0.0013 / 0.03 / 0.01 / ¾ / 3 × 10⁻⁶ / 10⁻⁴ | 0.001 / 0.01 / 0.01 / 1 / 10⁻⁵ / 10⁻⁴ |
| η; 𝔰₁^v (what sets it) | 0.98; 2.0 × 10⁻⁵ (the cap) | 0.99; 5.9 × 10⁻⁶ (the cap) | 0.96; 1.4 × 10⁻⁵ (the cap) | 0.98; 4.5 × 10⁻⁶ (the cap) |
| what binds | closing (𝔰_\* has 0.4 to spare) | closing (0.5 to spare) | closing and 𝔰_\* together (0.0) | 𝔰_\* by 0.1 |
| **Level 6: f** (G0f E (b)) | **10^−36.8** (−37.2) | **10^−34.4** (−34.6) | **10^−45.9** (−46.6) | **10^−40.9** (−41.2) |
| ϱ at the optimum (G0f) | 10^−45.6 (−46.1) | 10^−42.4 (−42.7) | 10^−54.9 (−56.6) | 10^−49.1 (−49.4) |
| η₀ | 10^−24.7 | 10^−23.7 | 10^−27.0 | 10^−26.3 |
| ϑ₁ / ϑ₂ / 𝔯 / option / μ / 𝔰_♭ | 0.0057 / 0.03 / 0.01 / (b) / 10⁻⁵ / 10⁻⁴ | 0.0019 / 0.01 / 0.01 / (b) / 3 × 10⁻⁵ / 10⁻⁴ | 0.0013 / 0.03 / 0.01 / (b) / 3 × 10⁻⁶ / 10⁻⁴ | 0.001 / 0.01 / 0.01 / (b) / 10⁻⁵ / 10⁻⁴ |
| η; 𝔰₁^v (what sets it) | 0.96; 4.0 × 10⁻⁵ (1/(4k₃^♮(μ)), k₃ = 6.3 × 10³) | 0.98; 1.7 × 10⁻⁵ (k₃ = 1.4 × 10⁴) | 0.96; 1.4 × 10⁻⁵ (the cap; 1/(4k₃) = 1.8 × 10⁻⁵) | 0.98; 1.9 × 10⁻⁶ (k₃ = 1.3 × 10⁵) |
| what binds | 𝔰_\* < 𝔰₁ by 3.3 | by 2.8 | by 4.5 | by 4.3 |
| quad-double reach (f ≥ 10⁻³⁵) | L4 to u\* ≈ −1.14 (seed 1); L6 to ≈ −2.67 (seed 1) | L4 all of D\* (seed 2); L6 to ≈ −1.76 (seed 2) | (per seed, as left) | |
| double-double (f ≥ 10⁻²⁰) | none (best 10^−22.9 at u\* = −9) | none | | |

**What the fifth sharpening achieves (computed):**
- **Level 4:** 0.7–0.9 decades of f.
- **Level 6:** 0.2–0.7 decades of f.
- **Quad-double reach** grows a little: level 4 seed 1 from u\* ≈ −1.16 to −1.14; level 6 from −2.84 / −1.85 to −2.67 /
  −1.76. Seed 2 at level 4 already covered D\*.
- **Of the four changes, two do the work: the closing with η, and 𝔨_rec at level 4.** Two do nothing on these
  backgrounds (G0h.2).
- **The free ϑ₁, ϑ₂ help a little, and only where 𝔰_\* binds.** Optimal ϑ₂ is small, 0.003–0.03: the cap is raised just
  until it meets the closing (level 4) or 1/(4k₃^♮(μ)) (level 6). Larger ϑ₂ costs through the rates: ϑ₂ = 0.5 costs 2.5
  decades of f at level 4, seed 1 D_A.
- **The optimal 𝔯 is the smallest tried (0.01).** Raising it to 0.2 moves f by at most 0.2 and loosens η₀ by 1.3–1.4
  decades.

## G0h.1 ϑ, 𝔯 and θ (computed; level 4, seed 1 D_A unless stated)

| ϑ₂ (cap-matched ϑ₁) | 0.003 | 0.01 | 0.03 | 0.1 | 0.2 | 0.3 | 0.5 |
|---|---|---|---|---|---|---|---|
| L4 s1 D_A: f | −29.5 | **−29.5** | −29.5 | −29.8 | −30.2 | −30.6 | −32.0 |
| L4 s1 D_A: η | 0.99 | 0.98 | 0.96 | 0.89 | 0.79 | 0.69 | 0.49 |
| L4 s1 D_A: log₁₀ F₂ | 9.2 | 9.2 | 9.3 | 9.7 | 10.4 | 11.2 | 13.6 |
| L6 s1 D_A: f | −37.5 | −37.0 | **−36.8** | −37.0 | −37.4 | −38.0 | −39.4 |

**The split ϑ₁ < ϑ₂ against ϑ₁ = ϑ₂ at the same ϑ₂.** It is worth 0.00–0.03 decades on D_A and 0.15–0.19 on D\*, through
the rates only, as n2 says. The Σ₁ cap per unit ϑ is 5–23 times the Σ₂ cap, so ϑ₁ can be small.

**θ at level 4** behaves as in G0g:
- θ = 0 loses 2.3, 3.0, 4.7 and 5.6 decades;
- the f optimum is at θ ∈ [½, 1], with ϱ best at the least such θ;
- at θ = 1, ϱ is 6.6, 6.1, 6.6 and 6.1 decades below f.

**Level 6.** Option (a) loses 6.3, 7.8, 9.5 and 10.9 decades to option (b), as in G0f: its 𝔰₁^♮ is 10^−11…−17 whatever the cap.

## G0h.2 What each change does (computed; decades of f at the optimum)

| change | level 4 | level 6 | why |
|---|---|---|---|
| closing with η (8√2 and 16 towards 4) | ≈ 0.5 (closing factor 27.3 → 8.3 at η ≈ 0.98) | ≈ 0.2, through A_v in 𝔰_\* ((2 + √2) → 2.0–2.1) | the closing binds at level 4; 𝔰_\* binds at level 6 |
| free ϑ₁, ϑ₂ (cap 𝔰_(θ,v)) | 0.0–0.2 (D\*: ϑ₂ = 0.03 lifts 𝔰₁ to meet the closing) | ≈ 0.3 (𝔰₁ from the old cap 2 × 10⁻⁵ to 1/(4k₃^♮(μ))) | above that, k₃^♮(μ) or the closing binds and the rates cost |
| 𝔨_rec, C_P^v, C_(P,ϱ)^v, C_(P,0)^v (level 4) | ≈ 0.2–0.3 (M_w 24.8 → 24.5 at seed 1 D_A) | — | √7 against 4, and μ^(1/2), μ on the lower jets |
| 𝔣₂^o, 𝔣₂^i (with m1) | **0.0** | **0.0** | c/z̲² + 1/z̲ ≥ 36.5 on D_A and ≥ 2.3 on D\* (z̲ = 0.003–0.12 on D_A, 0.002–0.51 on D\*), so the split never applies |
| 𝔨_B = max(𝔷, 𝔤₁) | **0.0** | **0.0** | 𝔷 ≈ 4–6 > 2 ≥ 𝔤₁ wherever 𝔨_B enters |
| free 𝔯 (in η) | ≤ 0.2 | ≤ 0.1 | ϱ is set by the ε budget and η₀ by 𝔯; f hardly depends on r |

## G0h.3 κ, priced as a formula-level estimate (computed; seed 1, both domains, both levels)

κ = κ′ is fixed by def:tl5-wg-domains in (0, ¼]. The admitted range here is κ < 3/8 (u\* = −2) and < 0.337 (u\* = −1.1),
so ¼ is admissible.

**What was varied.** κ in every constant and in the cap: 𝔨₁, 𝔨₂, ∂_γ, |D̂∂_γ|, w_t, the cap, c_\*κ_m/2 and the faces'
weights.

**What was not varied:**
- The rates were not recomputed. They are those of κ → 0, which stay admissible because admissibility is monotone in κ,
  κ′ (P-GRD5 item 1); this is valid but not optimal.
- The tilt of D^κ and of the faces was not modelled. D^κ loses 3κ′ in u at v = 7/2, i.e. 0.09–0.75.

So this is an estimate, not an evaluation.

| f (log₁₀) | κ = 0.01 | 0.03 | 0.1 | 0.25 |
|---|---|---|---|---|
| L4 s1 D_A | −29.5 | −29.3 | −29.2 | −29.3 |
| L4 s1 D\* | −36.0 | −35.8 | −35.8 | −36.1 |
| L6 s1 D_A | −36.8 | −36.5 | −36.5 | −36.5 |
| L6 s1 D\* | −45.9 | −45.6 | −45.6 | −45.8 |

**κ is worth at most 0.3 decades.** The reasons:
- **𝔨₂.** 𝔨₂ = (1/z̲ + max(1/c, 1/κ′))/(2Ω̂²) carries 1/z̲ ≈ 10²–4 × 10² at the points of the suprema (z̲ as low as
  0.003 on D_A and 0.002 on D\*), against 1/κ′ = 100.
- **𝔰₁.** The caps and c_\*κ_m/2 grow with κ, but 𝔰₁ then stops at 1/(4k₃^♮).
- **Costs.** 𝔨₁ and |∂_γ| grow.

Pricing it fully would need the tilted domain and faces, which the present grids do not represent.

## G0h.4 The remaining levers, ranked (computed where marked; decades)

**Level 6.** 𝔰_\* binds by 2.8–4.5. f from the closing alone would be 10^−33.5, −31.6, −41.4 and −36.6.
1. **𝔰₁ = 1/(4k₃^♮(μ))**, with k₃^♮(μ) = 6 × 10³ to 1.3 × 10⁵, from 𝔠^♮_(≤5)(μ) and the 𝔔 couplings.
   - Even k₃ → 0 is worth only 1.5–2.4, because c_\*κ_m/2 (1.9 × 10⁻³ on D_A, 4.3 × 10⁻⁴ on D\*) then caps 𝔰₁. The rest
     of the margin, 0.9–2.1, needs κ_m.
   - This is the only lever that moves f at level 6 now.
2. **Once 𝔰_\* is relieved, the closing items** (S_F, as in G0f; level 6 has no 𝔨_rec):
   - C₁^E against C_S^E: 3.1–3.2;
   - word count 7³: at most 2.5 (computed with the closing alone: −31.0 against −33.5 at seed 1 D_A; worth 0.0 in f while
     𝔰_\* binds);
   - the recovery 2k₁^(1,μ)√114: 2.1–2.3;
   - 𝔠^♮₆(μ) against 9·2⁶: 1.0–2.1;
   - 𝔣₂: 0.4–0.8 (the split does not apply; it would need z̲ larger);
   - 𝔨_B (𝔷): 0.6–0.75.

**Level 4.** The closing and 𝔰_\* are within 0–0.5 decades of each other. S_F leads S_M by 2.4–3.2.
1. **C₁^E against C_S^E: about 3 decades of S_F** (P-GRD5 item 2, not done). In f it is capped by the smallness slack
   (0.0–0.5) until 𝔰₁ rises, which ϑ₂ can now do at the cost of the rates (G0h.1).
2. **The word count 7².** Upper bound, computed by dropping it: +0.9, +1.3, 0.0 and +0.4 decades of f.
3. **𝔠^♮₄(μ) against 9·2⁴: 1.0–1.4. Then the remaining recovery factor in 𝔨_rec** ((6/5)(√3 + 8/3)K_rec√7 against
   G0's), **𝔣₂ 0.4–0.8 and 𝔨_B (𝔷) 0.6–0.75.**
4. **𝔨₂ through z̲.** 𝔨₂ ≈ 10², about half of it 1/z̲, sits inside C₁ and S_M. A larger lower bound z̲ of the weight would
   lower 𝔨₂ and also let the 𝔣₂ split apply. That is a choice of the weights, not of the theorem, so I have not priced it.
5. **κ:** ≤ 0.3 (G0h.3). **The ϑ split:** ≤ 0.2. **𝔯:** ≤ 0.1.

**Distance to the G0b-type floor:**
- level 4: f is 8.9, 8.8, 9.8 and 9.7 decades above it (G0b-type 10^−20.6, −18.9, −26.2, −22.9);
- level 6: 14.0, 13.4, 16.7 and 15.7 decades (G0b-type 10^−22.8, −21.0, −29.2, −25.2).

## G0h.5 Reach (computed; D\*'s grid restricted to u ≤ u\*; best f)

| u\* | −9 | −7 | −5 | −3 | −2 | −1.5 | −1.3 | −1.2 | −1.1 |
|---|---|---|---|---|---|---|---|---|---|
| L4 seed 1 | −23.1 | −24.8 | −26.2 | −27.8 | −29.5 | −30.7 | −32.2 | −33.2 | −36.0 |
| L4 seed 2 | −22.9 | −24.2 | −25.1 | −26.4 | −27.7 | −28.8 | −29.9 | −30.7 | −32.6 |
| L6 seed 1 | −27.0 | −29.2 | −31.4 | −34.1 | −36.8 | −38.8 | −40.6 | −41.9 | −45.9 |
| L6 seed 2 | −26.7 | −28.3 | −29.7 | −31.9 | −34.4 | −35.7 | −37.2 | −38.3 | −40.9 |
| L6 closing alone, seed 1 / 2 | −26.3 / −26.0 | −28.3 / −27.4 | −29.7 / −28.5 | −31.5 / −30.1 | −33.2 / −31.5 | −34.6 / −32.6 | −36.1 / −33.6 | −37.3 / −34.3 | −40.5 / −36.2 |

- **Quad-double:** level 4 to u\* ≈ −1.14 (seed 1) and all of D\* (seed 2); level 6 to ≈ −2.67 and −1.76. If 𝔰_\* did not
  bind, level 6 would reach −1.45 and −1.16.
- **Double-double:** none at either level. The best is 10^−22.9 at u\* = −9.
- **The reach grid is reduced:** μ ∈ [3 × 10⁻⁶, 10⁻⁴], ϑ₂ ≤ 0.1, r ∈ {0.01, 0.03}, and θ ∈ {½, ¾, 1} at level 4. At
  u\* ≤ −3 larger μ may do slightly better, so the reach figures are lower bounds.

## G0h.6 Caveats

1. **G0c's approximants, growth model and couplings,** as before. 𝔰₁ is now set by k₃^♮(μ) at level 6, and that is the
   quantity most exposed to the growth model.
2. **The rates for unequal ϑ** are from the reweighted LP over the same rays and the same 21-ray sampling as before.
3. **𝔰_\* at level 4:** C_P^v is used in its A-term, and P-GRD4's ν-constants in its ϱ and η₀ terms (G0h, header).
4. **κ** is priced only at formula level (G0h.3).
5. **No hypothetical** (the word count, κ) is proved.

## G0h.7 Files (under `/tmp/claude-0/-home-user-Claude-Method-Works/36602a96-aefb-52fa-89f4-29a4ab038dc7/scratchpad/g0h/`)

| file | what |
|---|---|
| `levelV.py` (= `levelV_head.py` + `levelV_mid.py` + `levelV_tail.py`) | thm:tl5-hfv at levels 4 and 6: new rate LPs per (ϑ₁, ϑ₂); the cap 𝔰_(θ,v); 𝔣₂ by the m1 rule; 𝔨_B; 𝔨_rec and C_P^v at level 4; closing with η; the r budget; κ via `G0H_KAP` |
| `levelV_s{1,2}_46_-2.0.json`, `…_-1.1.json`, `run_*.log` | main grids |
| `levelV_s{1,2}_46_-9.0_…_-1.2.json`, `reach_*.log` | reach sweeps |
| `levelV_s1_46_{-2.0,-1.1}_k{0.03,0.1,0.25}.json` | κ estimate |
| `levelV_s{1,2}_46_-2.0_-1.1_nw.json`, `nw_*.log` | word-count hypothetical |
| `sumV.py`, `tablesV.py`, `reachV.py` | tables |
| `G0h.md` | copy of this report |

---

## G0h.rule Addendum: the parameters that maximise min(f, ϱ) at level 4 (computed)

**Why this addendum.** The approximant is now computed by a rule whose cost grows like the 4.5th power of the decades it
must reach. So the figure that matters is the stricter of f and ϱ. §G0h.0 maximises f; at that optimum ϱ is 2.5–6 decades
below f. Here every parameter is chosen to maximise min(f, ϱ).

**What is held fixed.** "P-GRD5" means sec:tl5-hfv as merged, with the same intrinsic Sobolev constants, approximants and
targets as above, at level 4.

**What is searched:**
- θ ∈ {0, ¼, 0.375, ½, 0.625, ¾, 0.875, 1};
- ϑ₂ ∈ {0.003, 0.01, 0.03, 0.1}, with ϑ₁ cap-matched or equal;
- 𝔯 ∈ {0.01, 0.03, 0.1};
- μ ∈ {10⁻⁴, …, 10⁻⁶};
- 𝔰_♭ ∈ {1/8, …, 10⁻¹²};
- one more free choice: **the split of ε between f and ϱ**. The closing bounds only their sum, ε^v = 𝒮[s₄]f + 𝒮[¼ min(𝔤_(ϱ,q),
  μ^(−1/2)𝔤_(𝒥,s))k₂]ϱ + ε_M, and §G0h.0 gave each half. Here the fraction s that goes to f ranges over {½, 0.3, 0.1,
  0.03, 0.01, 0.003, 0.001}.

**What sets ϱ.** In every optimum it is the ε budget, the term 𝒮[¼ min(𝔤_(ϱ,q), μ^(−1/2)𝔤_(𝒥,s))k₂]ϱ. It is not 𝔯, and
not the ν^(−2) term of 𝔰_\*.

| | **seed 1, D_A** | seed 2, D_A | **seed 1, D\*** | **seed 2, D\*** |
|---|---|---|---|---|
| **max min(f, ϱ), P-GRD5** | **10^−31.3** | **10^−29.9** | **10^−38.6** | **10^−35.9** |
| f / ϱ there | −31.2 / −31.3 | −29.6 / −29.9 | −38.5 / −38.6 | −35.4 / −35.9 |
| η₀ there | −22.9 | −21.5 | −28.3 | −25.0 |
| θ | 0.375 | ½ | 0.625 | 0.625 |
| ϑ₁ / ϑ₂ | 0.0019 / 0.01 | 0.001 / 0.003 | 0.0013 / 0.03 | 0.001 / 0.003 |
| 𝔯 | 0.01 | 0.01 | 0.01 | 0.01 |
| μ | 10⁻⁵ | 3 × 10⁻⁵ | 3 × 10⁻⁶ | 3 × 10⁻⁶ |
| 𝔰_♭ | 10⁻⁴ | 10⁻⁴ | 10⁻⁴ | 10⁻⁴ |
| share of ε given to f | 0.01 | 0.01 | 0.003 | 0.01 |
| what binds the closing | closing and 𝔰_\* (0.0) | 𝔰_\* by 0.1 | 𝔰_\* by 0.2 | 𝔰_\* by 1.1 |
| the same with ε split half and half | −31.6 (f −29.5, ϱ −31.6) | −30.2 (f −27.9, ϱ −30.2) | −38.9 (f −36.3, ϱ −38.9) | −36.2 (f −33.8, ϱ −36.2) |
| **G0g under the same criterion** (half split; G0g's ϱ is also set by the ε budget) | **−32.4** (θ 0.375; f −30.2, ϱ −32.4) | −30.8 (θ 0.4375) | **−39.4** (θ 0.5625; f −37.0, ϱ −39.4) | **−36.6** (θ 0.6875; f −33.8, ϱ −36.6) |
| gain of P-GRD5 over G0g in min(f, ϱ): half split; best split | 0.8; 1.1 | 0.6; 0.9 | 0.5; 0.8 | 0.4; 0.7 |
| rule cost relative to G0g, (decades ratio)^4.5 | 0.86 | 0.88 | 0.92 | 0.92 |
| G0h's best f (§G0h.0), for comparison | −29.5 | −27.7 | −36.0 | −32.6 |

**Reading the table:**
- **ϱ is the stricter quantity in every case.** At the max-min point the rule should target f ≈ ϱ ≈ 10^−31.3 (seed 1 D_A),
  10^−38.6 (seed 1 D\*) and 10^−35.9 (seed 2 D\*), not the f of §G0h.0.
- **Optimising the ε split is worth ≈ 0.3 decades in every case.** That is the ceiling log₁₀ 2, reached by giving almost
  all of ε to ϱ. It costs f 1.4–2.2 decades, which f can afford.
- **G0g with the best split** would gain at most the same 0.3, since its ϱ is set by the ε budget too: about −32.1,
  −30.5, −39.1 and −36.3. P-GRD5's gain over G0g is then 0.6–0.8 at equal treatment.
- **The max-min θ lies below the f-optimal θ** in every case (0.375–0.625 against ½–1), as in G0g.

**A hypothetical lever on the ϱ requirement** (computed; the ϱ coefficient of ε^v scaled by a factor):

| factor on the ϱ coefficient | seed 1, D_A | seed 2, D_A | seed 1, D\* | seed 2, D\* |
|---|---|---|---|---|
| 1 (proved) | −31.3 | −29.9 | −38.6 | −35.9 |
| 10⁻¹ | −30.4 | −29.0 | −37.6 | −35.0 |
| 10⁻² | −29.6 | −28.2 | −36.8 | −34.0 |
| 10⁻³ | −29.5 (f binds) | −27.7 (f binds) | −36.2 | −33.2 |
| **room: best f − max-min** | **1.9** | **2.2** | **2.6** | **3.3** |
| rule cost if all the room is taken | ×0.76 | ×0.71 | ×0.73 | ×0.64 |

- **Each decade off the ϱ coefficient raises min(f, ϱ) by about one decade**, until f takes over (×10⁻¹ gives 0.9–1.0).
  After that, f (the closing and 𝔰_\*) binds.
- **A ϱ lever is worth at most 1.9, 2.2, 2.6 and 3.3 decades,** with seed 2 D\* gaining most.
- **That ranks it first among the open levers at level 4 for the rule.** The levers of §G0h.4 that act on f buy nothing in
  min(f, ϱ) until ϱ catches up.
- **What a ϱ lever would have to shrink:**
  - the conversion 𝒮;
  - min(𝔤_(ϱ,q), μ^(−1/2)𝔤_(𝒥,s)), which carries 7^(j′/2), 𝔠^♮(ν) + 1 and the factor ν^(−1/2) or μ^(−1/2);
  - k₂ = (8/5) max_j 𝔮_j, the coupling sums.
  - None is sharpened in P-GRD5. A full ϱ lever is worth the room above.

Scripts: `levelR.py` (`levelV` with the ε split and a factor on the ϱ coefficient, `G0H_RULE=1`), output
`levelV_s{1,2}_4_{-2.0,-1.1}_rule.json`, table `ruleV.py`; G0g's figures from `scratchpad/g0g/levelQ_*.json`.

---

**Note (coordinator, 2026-11-28, from R-P-GRD11).** The lever "𝔠^♮₄(μ) → 9·2⁴" priced in this report is a comparison
count, not a proved target: the terms with no background letters already give 𝔠^♮₄(μ) + 1 ≥ 2⁴ + 16·5·2⁴ = 1296 =
9²·2⁴ for every μ (eq:tl5-hfs-cn), and going below that needs a bound of the bilinear form 2𝔮̂ (about 8 against
16λ̂₀² = 80) that the chapter does not state. The figures given for this lever are therefore upper bounds for a target
the text does not reach (at most log₁₀ 9 = 0.954 decades less is available).
