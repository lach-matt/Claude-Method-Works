# P-GRD15: writer's report (sec:tl5-hff; levers 4 and 3a of the round-15 plan)

Writer's report as handed back (saved here by the coordinator). Two of the three levers are proved in full: lever 4 at
N ≥ 6 with option (b), and lever 3a at every level. The C₁ lever is left out: a weighted bound plausibly holds, but no
lemma of the chapter supports it yet, and in the worst case its leading part gains nothing.

**File:** research/warp-drive/paper/reader/proofs/P-GRD15.md, md5 4e071f06170039c3cd07f3bec8db4994, 365 lines.
Base: HEAD bea115c4, chapter 87 md5 532817d3 (7642 lines). Drafted under scratchpad/reader/pgrd15/ (tools copied from
pgrd14/tools/, orig/ taken from bea115c4).

Layout: chapter text 1–191 (11 labels), Placement 193–215, Comparison 217–349, Crosswalk 351–365.
Assembled: Section 57.30; Lemma 57.245 (lem:tl5-hff-rho), Lemma 57.246 (lem:tl5-hff-zero), Definition 57.247,
Theorem 57.248, Remark 57.249; displays (57.170)–(57.174). Index letter f.

## The levers

1. **Lever 4, the ϱ term into 𝔯: proved, for N ≥ 6 with option (b)** (lem:tl5-hff-rho).
   - **𝒮 check, done first:** ‖·‖_(1,t) and ‖·‖_(2,t) carry e^(−φ), so a factor e^(φ/2) in the forcing term cancels the
     weight. 𝒮[e^(φ/2)f] = 𝒮₀[f]. 𝒮 is subadditive, positively homogeneous and monotone, which is all the proof uses.
   - **Mechanism:** a monomial has a term with ϱ(p) only when Φ₂ = D̂²Ψ_C. Φ₁ is then H, h or a Ψ_B, a quantity of
     𝔰_P⁰, and ℓ_P + ℓ_E ≤ n − b + 3 gives the factor μ^(−3/2)μ^(b/2). So both terms of lem:tl5-hft-products hold with
     μ⁻¹𝔰_P⁰ in place of 𝔰.
   - Step 3 then gives 𝔰_P⁰ ≤ C_P⁰e^(φ/2)Y_s + C_(P,0)⁰η₀, which has no ϱ part. The result is a term 𝔯_ϱ^f Y_s² in 𝔯
     and a ϱη₀ part in ε, with no ϱ² term.
   - **Stated as an option:** route (𝔰) is the old one; route (𝔯) is offered only at N ≥ 6 with option (b). At N = 4
     and with option (a) it is not offered, because the counts there carry other arguments.
2. **Lever 3a, C_S through the shorter words: proved, at all levels** (lem:tl5-hff-zero).
   - Each |Ψ_(ZC)|² ≤ 𝔷²𝔨₂(e_o + κ′e_i)[Ψ_C], and the weight gives 𝔶_(|J|)μ^(|B|+2) ≤ μμ^(|C|).
   - The coefficient 1/(2Ω̂²z̲) becomes 6μ𝔷²𝔨₂: six preimages, the rotations as first letter of J. The shared words B′
     of a family carry at most 7μ𝔷²𝔨₂ (Z ∈ Γ), and 1 for a single word.
   - The part 8𝔲₀⁻¹|D̂∂_γ|² takes the same route, inside 𝔲₀^♯. At each point of the face the smaller of the two bounds
     is used, so C_S^f ≤ C_S^l for all weights.
   - Family and 𝔐_p versions are included.
   - **The word h:** the handoff note's first option, its own leaf weight 𝔶₀^h ≤ μ⁻². The reason is that h carries the
     entry 𝔤₁C_S^h of μ|H| in C_P⁰ = max(𝔤₁C_S^h, C_S^f). Under the second option that entry stays at 𝔤₁C_S^l. The
     second option is the case 𝔶₀^h = 𝔶₀ of the first, so nothing is lost.
3. **The C₁ term of 𝔨_rec^p: scoped, not drafted.** No G0q numbers reached the writer.
   - A weighted family bound for the seven fields is plausible, but it needs the face energies split by the last letter
     of the words, which no lemma of the chapter gives. So it does not "clearly hold".
   - Even if it holds, the parts that split by last letter gain nothing in the worst case: max(|T|⁻², λ_M⁻¹) times
     their coefficient squared is K_rec² times the present one.
   - Only the parts that do not split gain: the (43n)^½𝔵^z nonlinear part and 𝔞_𝔄. Their factor lies between 0.93 and
     0.38, depending on |T|⁻¹ against λ_M^(−½) at the supremum, which is exactly what G0q is measuring.
   - The scoping is written out under "Not done" in the Comparison.

## New labels, theorem, closing display, Remark

- **Labels (11):** sec:tl5-hff, lem:tl5-hff-rho, eq:tl5-hff-rho, lem:tl5-hff-zero, eq:tl5-hff-cs,
  def:tl5-hff-constants, eq:tl5-hff-routes, eq:tl5-hff-constants, thm:tl5-hff, eq:tl5-hff-closing, rem:tl5-hff-what.
- **def:tl5-hff-constants:**
  - C_P⁰ := max(𝔤₁C_S^h, C_S^f) and C_(P,0)⁰ := max(𝔤₁C_(0,0)^h, C_(0,0)) replace 𝔤₁C_S^l and 𝔤₁C_(0,0) at the sites
    of lem:tl5-hfc-h and in 𝔎 and 𝔎₀.
  - C_S^h and C_(0,0)^h go into 𝔨_rec^p and 𝔨_rec^(0,p).
  - In 𝔐_p^(m), C_S^h is used at b = 0 and C_S^f at b ≥ 1.
  - Route (𝔯):
    - ε^f = 𝒮[s_N + μ⁻¹(1 − 𝔵^z)⁻¹𝔤^l_(ϱ,t)k₂^z C_(P,0)⁰η₀ϱ];
    - 𝔯_ϱ^f = ϱ𝒮[μ⁻¹(1 − 𝔵^z)⁻¹𝔤^l_(ϱ,t)k₂^z C_P⁰e^(φ/2)];
    - 𝔯^f = 𝔯^c + 𝔯_ϱ^f.
  - η_f, A_f, B_f as before; Y_f = 2A_f/(1 + (1 − 4A_fB_f)^½) and 𝔰_*^f = 𝔰_*^f[Y_f].
- **thm:tl5-hff:**
  - Hypotheses: thm:tl5-hfc's, with these constants and either route: η₀ < 𝔰₁^v, admissible rates, η_f > 0, the closing
    condition and 𝔰_*^f < 𝔰₁^v.
  - Conclusion: a solution with Y_σ ≤ Y_f, plus the other conclusions with 𝔰_*^f.
- **Closing display (eq:tl5-hff-closing):** 4A_fB_f = 4η_f^(−3/2)(δ_w + η_f^(−1/2)(ε^f + ε_M^f))(S_F^f + S_M^f) < 1.
- **rem:tl5-hff-what:** states each mechanism as proved: Φ₁ through 𝔰_P⁰, the cost μ⁻¹, e^(φ/2) taken up by 𝒮's
  weight, the routes as an option, the shorter-word coefficient 6μ𝔷²𝔨₂ (7 for families), and why h takes its own
  weight.

## Containment

For 𝔶₀^h = 𝔶₀ and route (𝔰), every constant with index f is at most its index-c version. This is the last claim of
thm:tl5-hff and the last paragraph of its proof:
- C_S^f ≤ C_S^l always, through the first entry of the minimum in eq:tl5-hff-cs.
- C_S^h ≤ C_S^l and C_(0,0)^h = C_(0,0) at 𝔶₀^h = 𝔶₀, so C_P⁰ ≤ 𝔤₁C_S^l and C_(P,0)⁰ = 𝔤₁C_(0,0).
- Route (𝔰) gives ε^f = ε^c and 𝔯_ϱ^f = 0.
- Y_f ≤ Y_c, because the smaller root is nondecreasing in A and in B; and 𝔰_*^f ≤ 𝔰_*^c.

So the hypotheses of thm:tl5-hfc imply those of thm:tl5-hff. No earlier text is edited, so every earlier closing
condition stays valid beside the new one. Every change enters both 𝔰_*^f and the closing condition; the Comparison lists
the paths under "Both constraints".

## Checks

Run on a scratch tree from bea115c4 with the Placement applied, then again with the repository copy:
- **Placement:** the old lines occur once at 87:7641–7642; the pointer line is 117 characters.
- **`lint.py --chapters`:** 62 files, 5331 labels, 0 hits.
- **`assemble.py --check`:** labels 5331, 0 problems.
- **In-memory assembled lint:** `[] 0`.
- **Numbering:** 0 of 5320 existing numbers change; 11 are added.
- **Crosswalk:** 11 rows, ASCII only, each at the line of its label (1, 21, 29, 52, 60, 106, 116, 125, 127, 132, 171).
  Merged, there are 480 data rows for 480 labels, in the same order.
- **Format:** chapter text ≤ 120 characters per line with no forbidden line starts; notes ≤ 121.
- One lint hit along the way: "source" followed by a space is a forbidden working name. It is now "forcing term".

## Deduced gains (Comparison; upper figures, every supremum at one point; not evaluated)

The G0p figures used are from before P-GRD14.

**Lever 4, level 6, at G0p's optima (§G0p.4):**
- With the parameters fixed, f can take all of ε: min(f, ϱ) rises by at most +1.57 / +0.30 / +1.02 / +0.40. This
  assumes the ϱη₀ part of ε and 𝔯_ϱ^f are negligible; neither is evaluated.
- Re-optimised: route (𝔯) attains at least G0p's ×0.1 price, +0.90 / +0.61 / +0.81 / +0.40, less about 𝔯_ϱ^f/ln 10
  decades, wherever μ⁻¹C_(P,0)⁰η₀ ≤ 0.1𝔰₁^v at the supremum.

**Lever 3a:**
- The fall of C_S lies between ¼ and ½ of log₁₀(X/X′), where X′ = 6μ𝔷²𝔨₂. The inputs are X/𝔨₂ = 0.75 / 0.73 / 0.81 /
  0.81 (G0j §G0j.1) and 𝔷 = 10^0.75 / 10^0.68 / 10^0.67 / 10^0.59 (G0g §G0g.3), both measured at other suprema in earlier
  rounds.
  - At level-4 μ: 0.65–1.30 / 0.56–1.12 / 0.95–1.90 / 0.87–1.74 decades.
  - At level-6 μ: 0.65–1.30 / 0.43–0.86 / 0.83–1.66 / 0.74–1.48 decades.
- **Level 4: about 0 through 𝔰_*.** After P-GRD14's factor 𝔤₁, G0p's margins put 𝔨_rec^p above 𝔤₁C_S in all four
  cases, by +0.106 / +0.410 / +0.193 / +0.524. This confirms the handoff note's expectation. The route through S_F at
  seed 2 D_A is not evaluated.
- **Level 6:** at least G0p's C_S ÷ 2 price, +0.22 / +0.06 / +0.18 / +0.02, because the falls above all exceed 0.30.
  Beyond that it is capped where the C₁ part of 𝔐_p^(2) leads, and G0p does not report that split.
- The two levers act on different factors, so their gains add at most.

## Left open

- The C₁ lever (P-GRD16), once G0q gives |T|⁻¹ against λ_M^(−½) and K_rec's split at the supremum.
- Lever 4 at N = 4 and with option (a).
- The 𝔨₁ Cauchy–Schwarz sharpening and |H| ≤ |h|/(1 − |h|) in place of 𝔤₁.
- Not reported anywhere, and needed to price lever 4 at level 6: 𝔯_ϱ^f, and η₀/𝔰₁^v at level 6. For lever 3a: the cost
  C_(E,0)(𝔶^h)/C_(E,0)(𝔶) of h's own weight.
