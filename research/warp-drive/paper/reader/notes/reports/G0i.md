# G0i: the sixth sharpening (P-GRD6, the ϱ coefficient × 8𝔰₁^v) at the max-min points

Report only. I edited no repository file and committed nothing. Every run was launched from `scratchpad/g0i/` with
absolute paths. I read nothing under method/, drive/, extracted/ or recovered/.

**What I evaluated.** P-GRD6 as drafted at b8d033b5 (md5 6f10eb9c), sec:tl5-hfw. The reviewed copy, 30025949 (md5
4a08f9e3), leaves the formulas for ε^w and for the closing unchanged. I read the draft whole.
- **The one new factor:** ε^w = 𝒮[s_N[2R̂ic] + 2𝔰₁^v 𝔤_ϱ^v k₂ϱ]. This is the ϱ coefficient of ε^v times 8𝔰₁^v.
- **𝔤_ϱ^v:** at level 4, min(𝔤_(ϱ,q), μ^(−1/2)𝔤_(𝒥,s)); at level 6, 𝔤_(ϱ,s) under option (a) and μ^(−1/2)𝔤_(𝒥,s) under
  option (b).
- **Unchanged, as the reader notes:**
  - the ϱ of the level-4 mixed terms, in 𝔯_M and ε_M;
  - ϱ in η through 𝔯^v;
  - the ϱ-term of 𝔰_\*^w, i.e. its threshold term.

**Method: as in §G0h.rule** (`levelW.py` = `levelV` of G0h with ε^w):
- intrinsic Sobolev constants with the rigorous C_(E,r)² bounds;
- new rate LPs per (ϑ₁, ϑ₂);
- every parameter chosen to maximise min(f, ϱ): θ ∈ {0, ¼, 0.375, ½, 0.625, ¾, 0.875, 1} at level 4 (options (a), (b) at
  level 6), ϑ₂ ∈ {0.003, 0.01, 0.03, 0.1, 0.2} with ϑ₁ cap-matched or equal, 𝔯 ∈ {0.01, 0.03, 0.1}, μ ∈ {10⁻⁴, …, 10⁻⁶},
  𝔰_♭ ∈ {1/8, …, 10⁻¹²};
- the share of ε given to f over {0.99, 0.9, 0.7, 0.5, 0.3, 0.1, 0.03, 0.01, 0.001}, which P-GRD6's remark states is
  free.

ϱ is bounded by all three of its conditions, and the binding one is recorded:
1. the ε budget, which now holds the 8𝔰₁^v factor;
2. 𝔯^v ≤ r, through 𝔯_(w,s) + 𝔯_(M,q);
3. the ϱ-term of 𝔰_\*^w.

**Labels:**
- **computed**: floating point, mine; scripts under `scratchpad/g0i/` (§G0i.5);
- **deduced**: an argument or bookkeeping given here;
- **record**: G0h, G0g or P-GRD6, cited.

---

## G0i.0 Level 4: max min(f, ϱ) (computed)

| | **seed 1, D_A** | seed 2, D_A | **seed 1, D\*** | **seed 2, D\*** |
|---|---|---|---|---|
| **max min(f, ϱ), P-GRD6** | **10^−29.2** | **10^−27.5** | **10^−35.9** | **10^−32.7** |
| f / ϱ there | −29.2 / −29.2 | −27.5 / −27.0 | −35.9 / −35.7 | −32.7 / −32.3 |
| η₀ | −22.9 | −21.2 | −28.3 | −24.7 |
| θ | 0.375 | 0.625 | ¾ | ¾ |
| ϑ₁ / ϑ₂ | 0.0019 / 0.01 | 0.001 / 0.003 | 0.0013 / 0.03 | 0.001 / 0.01 |
| 𝔯 | 0.01 | 0.01 | 0.01 | 0.01 |
| μ | 10⁻⁵ | 10⁻⁴ | 3 × 10⁻⁶ | 10⁻⁵ |
| 𝔰_♭ | 10⁻⁴ | 10⁻⁴ | 10⁻⁴ | 10⁻⁴ |
| share of ε given to f | 0.99 | 0.9 | 0.7 | 0.9 |
| 𝔰₁^v; the factor 8𝔰₁^v on the ϱ coefficient | 8.3 × 10⁻⁶; 10^−4.2 | 4.9 × 10⁻⁶; 10^−4.4 | 1.4 × 10⁻⁵; 10^−3.9 | 1.8 × 10⁻⁶; 10^−4.8 |
| what binds | **f** (closing and 𝔰_\* together) | **f** (closing; 𝔰_\* 0.4 spare) | **f** (closing and 𝔰_\* together) | **f** (𝔰_\* by 0.4) |
| P-GRD5 max-min (§G0h.rule) | −31.3 | −29.9 | −38.6 | −35.9 |
| **gain** | **+2.2** | **+2.5** | **+2.7** | **+3.2** |
| rule cost against P-GRD5, (decades ratio)^4.5 | 0.72 | 0.68 | 0.72 | 0.66 |
| P-GRD5's best f (§G0h.0), for comparison | −29.5 | −27.7 | −36.0 | −32.6 |

**The writer's estimate, settled** (computed):
- **The coefficient falls 3.9–4.8 decades, not 14–17.** At the max-min points 𝔰₁^v = 1.8 × 10⁻⁶ to 1.4 × 10⁻⁵, so 8𝔰₁^v
  = 10^−4.8…−3.9. This agrees with the reader's 3.8–5.0. The writer's 10⁻¹⁵…10⁻¹⁸ are G0d's 𝔰₁ values (P-GRD, before
  the μ-weighted k₃).
- **Only 2.2–3.2 of those decades are needed** before f takes over. min(f, ϱ) then gains exactly that, 2.2–3.2 decades.
- **The new targets sit at, or slightly above, P-GRD5's best f.** By giving 70–99 % of ε to f, the rule targets f ≈ ϱ at
  10^−29.2 (seed 1 D_A), 10^−35.9 (seed 1 D\*) and 10^−32.7 (seed 2 D\*).

**Does ϱ still bind? No: f binds in all four cases.**
- The ϱ condition that is tight is still the ε budget, but only because most of ε is spent on f. ϱ has room: 𝔯 would
  allow 10^−21.8…−30.7 and the 𝔰_\* term 10^−16.1…−21.6.
- **A further ϱ lever is worth at most 0.0–0.4 decades** (computed: × 0.1 gives 0.00, 0.04, 0.11, 0.28; × 0.01 gives
  0.00, 0.04, 0.15, 0.39). That is only the last of the ε share.
- **The mixed terms' ϱ** (the ε_M part, unchanged) sits 3.3–4.8 decades below the ε^w coefficient. It does not bind.

## G0i.1 Level 4: the f-side levers re-ranked, for min(f, ϱ) (computed hypotheticals at the max-min points)

| lever (hypothetical, not proved) | seed 1, D_A | seed 2, D_A | seed 1, D\* | seed 2, D\* |
|---|---|---|---|---|
| **C₁^E ÷ 10** (C₁ against C_S, P-GRD5 item 2) | **+1.0** | **+1.0** | **+1.0** | **+1.0** |
| **C₁^E ÷ 10³** (about the C₁^E–C_S^E gap of 2.8–3.1) | **+2.8** | **+2.5** | **+2.6** | **+2.9** |
| word count 7² dropped from 𝔤_(𝒥,s) | +0.7 | +0.6 | 0.0 | +0.1 |
| 𝔠^♮_j(μ) → 9·2^j in 𝔤_(𝒥,s) | +0.7 | +0.6 | 0.0 | +0.1 |
| z̲ (estimate, not computed) | ≲ 0.3–0.5 | | | |
| a further factor on the ϱ coefficient (× 0.01) | 0.0 | 0.0 | +0.2 | +0.4 |

**Reading the table:**
- **C₁^E against C_S^E is now first by far.** It is the only lever that moves both conditions binding f:
  - S_F (through 𝔎 = C_P^v𝔨_B);
  - the A-term of 𝔰_\* (through C_P^v = 2 max(2C_S, C₁, 𝔨_rec), whose 𝔨_rec is itself ∝ C₁).
  - It gives one decade for its first decade and about 2.5–2.9 for three. After that the closing's other factors and
    the cap 𝔰_(θ,v) take over.
- **The word count and 𝔠^♮₄(μ) act on S_F only.** Each is worth what the 𝔰_\* slack allows: 0.6–0.7 on D_A, ≤ 0.1 on D\*,
  where 𝔰_\* already binds. With the cap raised (larger ϑ₂, at the cost of the rates) they would be worth up to their
  full S_F sizes, 1.7 and 1.0–1.4.
- **z̲ enters 𝔨₂.** 𝔨₂ = (1/z̲ + 1/κ′)/(2Ω̂²) sits under the root in C₁ and in S_M; 1/z̲ ≈ 10²–4 × 10² at the suprema. At
  most 1/z̲ out of 𝔨₂ is a factor ≤ 2–4 in 𝔨₂, i.e. 0.15–0.3 decades in C₁. It would also let 𝔣₂'s family split apply
  (§G0h.2).
  - Through the C₁ lever above, that is ≲ 0.3–0.5 decades of min(f, ϱ).
  - It is a choice of the weights, which also changes the rates, so I have not computed it.
- **The ϱ side is exhausted at level 4.**

## G0i.2 Level 6, briefly (computed; same method, options (a)/(b))

| | seed 1, D_A | seed 2, D_A | seed 1, D\* | seed 2, D\* |
|---|---|---|---|---|
| P-GRD5 max min(f, ϱ) | −44.8 (option (a)) | −42.0 | −54.6 | −48.8 |
| **P-GRD6 max min(f, ϱ)** | **−41.7** | **−37.8** | **−50.5** | **−44.0** |
| gain | +3.1 | +4.2 | +4.2 | +4.9 |
| f / ϱ there | −41.3 / −41.7 | −37.3 / −37.8 | −49.9 / −50.5 | −43.2 / −44.0 |
| option; 𝔰_♭; 𝔰₁^v; share of ε to f | (b); 10⁻⁶; 5 × 10⁻⁷; 0.001 | (b); 10⁻⁶; 5 × 10⁻⁷; 0.01 | (b); 10⁻⁶; 5 × 10⁻⁷; 0.001 | (b); 10⁻⁶; 5 × 10⁻⁷; 0.01 |
| what binds | **ϱ** (ε budget); 𝔰_\* binds f by 5.2 | ϱ; 𝔰_\* by 3.5 | ϱ; 𝔰_\* by 6.0 | ϱ; 𝔰_\* by 4.9 |
| best f (§G0h.0) | −36.8 | −34.4 | −45.9 | −40.9 |

**At level 6, ϱ still binds.**
- The ϱ coefficient under (b) is μ^(−1/2)𝔤_(𝒥,s)k₂. Even after × 8𝔰₁^v it is 10^7–10^8.7, against 𝒮[s₆] ≈ 10^4.6–5.1.
- **The optimum lowers 𝔰_♭ to 10⁻⁶** to shrink 8𝔰₁^v (10^−5.4). It pays for this with 𝔰_\* binding f by 3.5–6 decades.
- **A further ϱ lever remains first at level 6.** Each decade off the coefficient gives one decade (computed: × 0.1 gives
  +1.0, × 0.01 gives +1.9…+2.0). The room up to the best f is 4.8, 3.4, 4.6 and 3.0 decades.
- **The rule cost at level 6** falls to 0.72, 0.62, 0.70 and 0.62 of P-GRD5's.

## G0i.3 Ranking for min(f, ϱ)

- **Level 4** (f binds):
  1. C₁^E against C_S^E: ≈ 2.5–2.9 decades;
  2. the word count 7²: ≤ 0.7, capped by 𝔰_\*;
  3. 𝔠^♮₄(μ): ≤ 0.7, capped by 𝔰_\*;
  4. z̲: ≲ 0.3–0.5;
  5. ϱ levers: ≤ 0.4;
  6. κ, the ϑ split, 𝔯: ≤ 0.3 each (§G0h).
- **Level 6** (ϱ binds):
  1. the ϱ coefficient: up to 3.0–4.8;
  2. then 𝔰₁ (k₃^♮(μ), c_\*κ_m/2) and the closing items of §G0h.4.

## G0i.4 Caveats

1. **G0c's approximants, growth model and couplings,** as before. 𝔰₁^v now multiplies the ϱ coefficient, so the growth
   model enters ϱ through 𝔰₁ as well (through k₃^♮(ν) and the cap).
2. **The ε share** is searched on a grid. The max-min values are within about 0.1 of the continuous optimum.
3. **The hypotheticals are not proved.** C₁^E ÷ 10^k scales C₁^♮ and C₁^g everywhere, so 𝔨_rec ∝ C₁ moves too. z̲ is an
   estimate only.

## G0i.5 Files (under `/tmp/claude-0/-home-user-Claude-Method-Works/36602a96-aefb-52fa-89f4-29a4ab038dc7/scratchpad/g0i/`)

| file | what |
|---|---|
| `levelW.py` (`levelW_head.py` + `levelW_mid.py` + `levelW_tail.py`) | thm:tl5-hfw: G0h's `levelV` with ε^w (`G0I_W=1`), the ε share, a factor on the ϱ coefficient, the max-min search |
| `levelW_h.py` | the same, with the hypotheticals: C₁^E scaled (`G0I_C1S`), the word count (nw) and 𝔠^♮_j(μ) → 9·2^j (c9) |
| `levelV_s{1,2}_{4,6}_{-2.0,-1.1}_w.json`, `w_*.log` | P-GRD6 max-min, levels 4 and 6 |
| `levelV_s{1,2}_6_{-2.0,-1.1}_v.json` | P-GRD5 max-min at level 6 (`G0I_W=0`) |
| `levelV_s{1,2}_4_*_{h,c1,c3}.json`, `h_*.log`, `x_*.log` | level-4 hypotheticals |
| `ruleW.py`, `hypW.py` | tables |
| `G0i.md` | copy of this report |
