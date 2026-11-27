# P-UB3: the chain at h = 10⁻⁶ without its two side hypotheses, and its evaluation

Proof file for the coordinator. Nothing in chapters/, crosswalk/ or elsewhere in the repository was edited; this is the
only file written there, and nothing was committed. The old texts of section 6 are quoted from the chapters at HEAD
1680675a (chapter 71 md5 bb53f3e845095a3cd821bf51f8c12414, unchanged since 2b9cb2ea; 00-front 7304f875…, 01-introduction
648eb9ee…, 03-theorems aef99018…, 90-scope f771640b…) **with P-D0's sixteen texts applied**: proofs/P-D0.md md5
1265f3bd480c2df7bf0300e8a43d4c4f, the version after its review R-P-D0 (T1–T13 of the first version 5f41b63f, with the
new texts of T3 and T5 revised, and T14–T16 added). P-D0's old texts were checked against HEAD: each occurs exactly
once, as whole lines, and applied in the order of P-D0's section 6 each still occurs once, so they are disjoint and
apply at HEAD; chapter 71 with them has md5 1b1056faa127f742e1a2fc46b8cbf9e2. Of the texts below, U11–U15 replace
P-D0's new texts of T6–T9 and T12 (unchanged since 5f41b63f); every other old text occurs verbatim and once at HEAD as
well, and none overlaps a P-D0 text (U42 takes the last two lines of thm:tr-transfer (iii), which P-D0's T16 leaves).
All texts were applied together to a scratch copy (the working tree + P-D0 + these): lint --chapters 0 hits, assemble
--check 0 problems, assembled-paper check `[] 0` (section 7).

## 0. Outcome

- **Part 1 (a): the hypothesis 4k̄_max + 24 > I_base + 22,119 is removed, by proof.** It is T_11 < T_12, and it is used
  only to write T_12 for max(T_11, T_12) in the orders of the reads of Step 4′ (lem:uc-small-orders (d), (e),
  rem:uc-small-reading). prop:uc-dependence now holds without it, with D′_* := max(T_11, T_12) + 18 + … (text U20); the
  cost is max(0, T_11 − T_12) ≤ I_base + 22,119 added to D_NM. At P-D0's ε_K = 9.99·10⁻¹⁴, ε_+ = 9.995·10⁻¹⁴ this lets
  N̄_Λ be the proved count 3,683,190,611 and gives **d_NM ≤ D_NM < 2.08183·10⁴¹** (P-D0 estimated 2.08·10⁴¹).
- **Part 1 (b): the cap ε_+ < 10⁻¹³ is replaced, by proof, by ε_K < 0.998ε_Υ (and nothing on ε_+ beyond
  admissibility).** ε_+ < 10⁻¹³ is used only for one numerical bound (3.000005·10⁶ and the count 3,000,004 in I_lev),
  which every admissible ε_+ < ε_ind ≤ δ_50 < δ̄ < 10⁻⁷ meets; and ε_K < 10⁻¹³ was used tacitly for ε_K + ε < ε_g and
  ε_K < ε_g − 2ε, which ε_K < 0.998ε_Υ gives (ε ≤ 10⁻³ε_g). ε_Υ itself cannot be passed: def:iii-i10-1-3 asks ε_K < ε_Υ
  and the construction uses it (Step 4 of prop:iii-i11-3-1); the last factor 0.998 is worth less than 0.21 % of D_NM.
- **The choice evaluated (Part 2):** ε_K = 1.4589·10⁻¹⁰, ε_+ = 1.459·10⁻¹⁰, N̄_Λ = 3,683,190,611, with k̄_0 = 3,
  J_* = 15,000,015, l_* = 50, J′ = 765,000,816, ε_Υ = 1.4619·10⁻¹⁰ unchanged and the index sets ℰ^φ_ind, ℰ^(ι,φ)_ind of
  P-D0. At it T_11 < T_12 holds (X_12 = 11,270,575,291,594,154,340 > R_base + 22), so the texts of lem:uc-small-orders
  and rem:uc-small-reading keep T_12; (a) is used only in prop:uc-dependence in general and in sec:tr (N₁ removed).

| | HEAD (constructed sets) | P-D0 | (a) alone | (a) + (b), the texts |
|---|---|---|---|---|
| ε_K | 1.6747·10⁻¹⁷ | 9.99·10⁻¹⁴ | 9.99·10⁻¹⁴ | 1.4589·10⁻¹⁰ |
| N̄_Λ | 909,507,124,095,312 | 77,112,616,084 | 3,683,190,611 | 3,683,190,611 |
| D_acc < | 3.78623·10⁵⁵ | 4.56265·10⁴³ | 1.04092·10⁴¹ | 7.12778·10³⁷ |
| D_NM < | 7.57245·10⁵⁵ | 9.12529·10⁴³ | 2.08183·10⁴¹ | 1.42556·10³⁸ |
| 21D_NM + 6 < | 1.59022·10⁵⁷ | 1.91631·10⁴⁵ | 4.37183·10⁴² | 2.99367·10³⁹ |
| K ≤ 22D_NM + 345 < | 1.66594·10⁵⁷ | 2.00757·10⁴⁵ | 4.58002·10⁴² | 3.13622·10³⁹ |
| 3R at the choice > | 1.2251·10²⁷ | 2.0538·10²³ | 2.0538·10²³ | 1.40639·10²⁰ |

**The final numbers (all in the texts).** D_e = 1.41633·10²⁰ (first line of eq:ec-upper), L_< = 6,868,208,951,
L_> = R_b = 6,868,208,953, N_ι = 5,188,959,638,229,843,970,554,286,700, C_lev = 10,377,919,276,459,687,944,791,764,540,
C_* = 31,133,758,693,167,165,978,342,162,162,

- D_acc = 71,277,718,119,225,469,720,805,142,747,913,308,950 < 7.12778·10³⁷;
- D_NM = 142,555,436,217,695,100,271,475,851,685,218,689,090 < 1.42556·10³⁸;
- N_NM ≤ 21D_NM + 6 = 2,993,664,160,571,597,105,700,992,885,389,592,470,896 < 2.99367·10³⁹;
- K ≤ 22D_NM + 345 = 3,136,219,596,789,292,205,972,468,737,074,811,160,325 < 3.13622·10³⁹;
- for the fixed seminorms of lem:uc-small-orders (d): d_NM ≤ D_b = 71,277,718,129,603,389,008,535,406,246,925,875,580
  < 7.12778·10³⁷, N_NM < 1.4969·10³⁹, K < 1.5682·10³⁹;
- in the class ℰ_0^½: 1.27642·10⁴³ < K* < 3.93435·10⁷⁹ (was 9.684·10⁵⁶ < K* < 1.11014·10¹¹⁵).

**The lower bounds that move.** At the choice 3R > 1.40639·10²⁰ and D_e < 1.0071 · 3R (was 1.2251·10²⁷, 1.0072);
K > 22d > 3.094058·10²¹ (was 2.695·10²⁸); K* > 1.27642·10⁴³ (was 9.684·10⁵⁶); d_NM > 0.3168h⁻² exceeds the bound for
h ≤ 4.71·10⁻²⁰ (was 6.46·10⁻²⁹); prop:tr-fail: ε_ind(h) < 1.45·10⁻¹⁹, giving more than 1.4268·10³⁸, for
0 < |h − h_c| < 1.447·10⁻²⁵ (was 1.99·10⁻²⁸, 7.5755·10⁵⁵, 1.986·10⁻³⁴). Unchanged and still stated: d_acc > 1.403·10²⁰
at every admissible choice (thm:loss-d (ii)); 1.2250·10²⁷ and 2.5725·10²⁸ for the index sets as constructed
(cor:is-lower, eq:uc-lower, now qualified); 2.0517·10¹⁰/μ(h) at other h, for the index sets as constructed.

## 1. Part 1 (a): the hypothesis 4k̄_max + 24 > I_base + 22,119

**What it is.** With X_12 := 4k̄_max + 24, T_11 := 20,183 + 1,914 + I_base + 22 + C_lev + I_lev and
T_12 := C_lev + I_lev + X_12 of lem:cs-rest, and R_base = 22,097 + I_base, T_12 − T_11 = X_12 − (R_base + 22) =
4k̄_max + 24 − (I_base + 22,119). So the hypothesis is T_11 < T_12.

**Where it is used.** A search of all chapters for T_11, T_12, X_12, "22,119", "22,083", "4k̄_max" and N₁ finds:

1. lem:uc-small-orders (d): the statement "ρ < T_12 in Steps 4′ and 4", from the proof's sentence "In Step 4′, C^rot is
   read through thm:iii-i12-3-1 at (0, 0) and p⃗′_0 through thm:iii-i11-4-1, charged at most C_lev − 11 + I_lev + X_12
   and T_11 (lem:cs-rest), both less than T_12". The first charge is T_12 − 11 in every case; the second is below T_12
   exactly when the hypothesis holds.
2. lem:uc-small-orders (e), proof: "So ρ + R_base + 16 ≤ C_lev + I_lev + R_base + 5 < T_12 + 14, as X_12 = … exceeds
   R_base + 22, so that also T_11 < T_12 in (d)". This is the numerical check of the hypothesis at the choice; the
   inequality it serves, C_lev + I_lev + R_base + 5 < T_12 + 14, needs only R_base < X_12 + 9.
3. rem:uc-small-reading: "ρ_K ≤ T_12 + 2 + C_lev − 11 + I_lev, Step 4′ reading the solution at α at an order below
   T_12 + 2", where the order of the Step 4′ read is the ρ of item 1.
4. prop:uc-dependence: the hypothesis, and the sentence of its proof that names items 1–3.
5. Consequences only: P-D0's lem:uc-lambda (a) (N̄_Λ = 77,112,616,084 chosen to meet it) and thm:tr-transfer (iii) with
   its proof (N̄_Λ := max(N̄(h), N₁), N₁ the least integer with 3,060,003,264N₁ > I_base + 22,083, which is the same
   inequality, as 4k̄_max + 24 = 4 · 765,000,816N̄_Λ + 36 at k̄_0 = 3).

Nowhere else: lem:cs-rest uses T_11 and T_12 only as summands of the bound eq:cs-c0 for c_0, and prop:cs-cstar writes
that sum out; neither compares them.

**The improved statement (text U20).** prop:uc-dependence holds without the hypothesis, with

    D′_* := max(T_11, T_12) + 18 + 20,565,308,337L_< + (C_lev + I_lev − 9)L_> + 2R_base

and D_NM := D_acc + D′_* + d̄_Φ, and every other part of the statement as before; when T_11 < T_12, D′_* is the number
of rem:uc-small-reading.

**Proof.** *The fixed seminorms of lem:uc-small-orders (d).* The regularity ρ of the fixed seminorm of a step is the
order at which the maps that read the coefficients from its forcing are bounded, and a map built by the rules of
def:ec-accounted-loss is bounded from the order of its charge into the coordinates, the coefficient functionals being
bounded by the order 0 (lem:cs-elem (a)); this is how (d) bounds ρ at the levels. In Step 4′ the reads are C^rot through
thm:iii-i12-3-1 at (0, 0), charged at most C_lev − 11 + I_lev + X_12 = T_12 − 11, and p⃗′_0 through thm:iii-i11-4-1,
charged at most T_11 (lem:cs-rest); Step 4 applies thm:iii-i12-3-1 again. So ρ ≤ max(T_11, T_12) in Steps 4′ and 4,
whatever the sign of T_12 − T_11. The conditions there are read at b₀ (Step 4′ is a step of thm:iii-i14-3-1, at b₀, and
prop:iii-i15-2-5 has no Step 4′), so by (F3) and the comparisons of (d) each has order at most
ρ + 14 ≤ max(T_11, T_12) + 14. A condition read at a reference point (0, p⃗_b) with b ≠ b₀ occurs only at a level, where
ρ ≤ C_lev − 11 + I_lev, and has order at most ρ + R_base + 16 ≤ C_lev + I_lev + R_base + 5 = T_11 − 17. The orders of
(a)–(c) are at most 2R_base + 16. Hence every order named in the proof of lem:iii-j2-2-3 is at most
max(2R_base + 16, max(T_11, T_12) + 14), which is at most D′_* as just defined.
*The seminorms of rem:uc-small-reading.* There Step 4′ reads the solution at α at the order ρ + 2 ≤ max(T_11, T_12) + 2,
so ρ_K ≤ max(T_11, T_12) + 2 + C_lev − 11 + I_lev; the recursion ρ_k ≤ ρ_(k+1) + 2 + C_lev − 11 + I_lev above 3 and
ρ_k ≤ ρ_(k+1) + 20,565,308,337 below 3, with at most L_> levels above 3 (β_K among them) and L_< below, gives
ρ_k ≤ max(T_11, T_12) + 20,565,308,337L_< + (C_lev + I_lev − 9)L_>; the base norms are needed at most at
ρ_1 + 2R_base + 4, and every order is at most ρ_1 + 2R_base + 18 ≤ D′_*. Nothing else in rem:uc-small-reading uses
T_12.
*The conclusion.* prop:uc-d-small (a) gives d_NM = max(d_R, d_* + d_F + d_Φ) with d_F ≤ d_R ≤ D_acc (lem:cs-sharp, whose
proof does not involve T_11 or T_12 beyond c_0 ≤ C_*), d_* ≤ D′_* and d_Φ ≤ d̄_Φ; so d_NM ≤ D_acc + D′_* + d̄_Φ = D_NM,
and N_NM = 21d_NM + 6 ≤ 21D_NM + 6. The monotonicity statements hold because each of T_11 and T_12 is a polynomial with
non-negative coefficients in N̄_Λ, k̄_0, J′, L_<, L_>, R_b, and the larger of two non-decreasing functions is
non-decreasing. ∎

**Cost and effect.** D′_* exceeds the hypothesis-form value by max(0, T_11 − T_12) = max(0, I_base + 22,119 −
4k̄_max − 24) ≤ I_base + 22,119. At P-D0's ε_K, ε_+ and N̄_Λ = 3,683,190,611 this is 224,694,281,620,649,059,325, about
10⁻²¹ of D_NM. Evaluated there (D_e := 2.06834·10²³ ≥ F_1 = 2.068334379…·10²³, T_11 > T_12):
D_acc = 104,091,154,057,447,763,009,291,737,694,910,244,814,011 < 1.04092·10⁴¹,
D_NM = 208,182,308,114,874,770,522,794,546,328,109,871,464,022 < 2.08183·10⁴¹, 21D_NM + 6 < 4.37183·10⁴²,
22D_NM + 345 < 4.58002·10⁴². These are not drafted as texts, since (b) improves on them.

## 2. Part 1 (b): the hypothesis ε_+ < 10⁻¹³

**Where it is used.** Explicitly in two places, and tacitly, as a smallness of ε_K beyond ε_K < ε_Υ, in two more:

1. prop:uc-explicit: "As η_2 − η_1 < ε_+ < 10⁻¹³, (1 + η_2 − η_1)/𝔡₁ + 2 < (1 + 10⁻¹³) · 3.0000026·10⁶ + 2 <
   3.000005·10⁶". This bounds T_2 and gives, in lem:cs-iterations (a), "at most (1 + η_2 − η_1)/𝔡₁ + 1 < 3,000,004" at
   level 2, the term 3 · 3,000,004 of I_lev = 34,268,829,852, which lem:uc-small-orders (d) and rem:uc-small-reading
   also use.
2. prop:uc-dependence: the hypothesis, and its proof's list.
3. lem:uc-admissible, Step 4 of the proof of prop:iii-i11-3-1: a δ₄ > 0 with δ₄ + ℓ_3 + 2ε < ε_g, ℓ_3 = α − 4 − ε < ε_K;
   it needs ε_K + ε < ε_g.
4. lem:cs-rest, item (6) of Step 1 ("τ_0 = 2 + ε_g − 2ε exceeds α_1 − ε′, α_1 − 2 < ε_K < ε_g − 2ε"), and the bases of
   sec:cs-small ("Each of these levels is below τ_0 = 2 + ε_g − 2ε"): the level α_1 < 2 + ε_K must be below τ_0, so
   ε_K ≤ ε_g − 2ε is needed.

Every other occurrence of ε_K or ε_+ in sec:uc-eval, sec:cs and sec:cs-small was checked: it uses ε_K < ε_+, ε_K < ε_Υ,
ε_+ < ε_ind, (G), (G⁺) or a bound true for ε_K < ½ (lem:uc-n-iota "4 + ε_K < 5"; prop:uc-explicit
"ε_K/Δβ_0 = 1/0.998001 < 2"; lem:cs-fourier (b) "⌈3/2 + ε_K⌉ = 2", "−μ ≥ ε_ind > ε_K", "every other degree has real
part above ε_K" by (G); def:cs-choices (f) "a_K is at least 4 + ε_K"; lem:uc-admissible "α_1 < 2 + ε_K < 2 + ε_g" and
"ε′_0 < 0.001ε_K"; prop:ec-rounds and lem:ec-counts, which hold for every admissible choice). prop:tr-lambda's own
"0 < ε_+ < 10⁻¹³" belongs to sec:tr, for the index sets as constructed (where ε_+ < μ(h) < 1.65·10⁻¹⁴ anyway), and is
not this cap.

**The improved statement (text U20).** prop:uc-dependence holds for all ε_K, ε_+ with 0 < ε_K < ε_+ and ε_K < 0.998ε_Υ
for which the choice is admissible.

**Proof.** Item 1: admissibility gives ε_+ < ε_ind (eq:iii-i9-1-1), ε_ind ≤ δ_50 (prop:np-10-52 (iii)) and
δ_50 < δ̄ = 1.94137057·10⁻⁸ (def:ec-point); so η_2 − η_1 < ε_+ < 10⁻⁷, and with 1/𝔡₁ < 3.0000026·10⁶,
(1 + η_2 − η_1)/𝔡₁ + 2 < (1 + 10⁻⁷) · 3.0000026·10⁶ + 2 = 3,000,004.90000026 < 3.000005·10⁶. So the bound for T_2 and
the count 3,000,004 hold, and I_lev is unchanged; F_1 carries ε_+ exactly, through the factor 1 + ε_+. Items 3 and 4:
at the computational point ε_ind = δ_50 > ε_Υ, so ε_g = ε_Υ (lem:uc-admissible), and def:uc-choice takes ε ≤ 10⁻³ε_g.
If ε_K < 0.998ε_Υ, then ε_K + ε < 0.999ε_g < ε_g and ε_g − 2ε ≥ 0.998ε_g > ε_K. Nothing else changes. ∎

**Why ε_Υ cannot be passed.** cor:is-flat gives (G) for the index sets of def:uc-choice for every ε_K < μ♭_Z, and
μ♭_Z > ε_Υ; but def:iii-i10-1-3 itself asks ε_K < ε_Υ, so that ε_K < ε_g, and the construction uses this: Step 4 of the
proof of prop:iii-i11-3-1 asks δ₄ > 0 with δ₄ + ℓ_3 + 2ε < ε_g, where ℓ_3 + 2ε = α − 4 + ε > ε_K − ε′_0 + ε, and
ε_g ≤ ε_Υ (def:s21-eps-g). So ε_K < ε_Υ is a hypothesis of the theorem whose loss is being bounded, not of the chain,
and nothing in this paper allows it to be dropped. Within [0.998ε_Υ, ε_Υ) the chain would need ε < ½(ε_g − ε_K) in
def:uc-choice besides ε ≤ 10⁻³ε_g; this is allowed (def:uc-choice imposes ε ≤ 10⁻³ε_g "besides" the conditions placed
on ε) but not drafted, as D_NM is of the order L_>C_lev ∝ 1/ε_K and the gain is below a factor 0.998: the formulas give
1.42273·10³⁸ at ε_K = 1.4618·10⁻¹⁰, an estimate only.

**The choice.** ε_K := 1.4589·10⁻¹⁰ < 0.998ε_Υ = 1.4589762·10⁻¹⁰; ε_+ := 1.459·10⁻¹⁰, so that
ε′_0 = ½(ε_+ − ε_K) = 5·10⁻¹⁵ < 0.001ε_K (needed for 0.999ε_K ≤ α − 4 ≤ ε_K) and ε_+ < μ♭_Z, ε_+ < ε_ind, ε_+ < δ_♯;
η_1 < η_2 in (ε_K, ε_+) gives η_1 < ε_g. N̄_Λ := 3,683,190,611, the count of cor:is-flat for ε_+ ∈ (0, μ♭_Z).

## 3. The evaluation

**Reproduction first.** The formulas of prop:uc-dependence (with D′_* in the hypothesis form T_12) were coded in exact
rational arithmetic, reusing P-UB2's chain script. At the inputs of HEAD (ε_K = 1.6747·10⁻¹⁷, ε_+ = 1.67478·10⁻¹⁷,
N̄_Λ = 909,507,124,095,312, D_e = 1.23382·10²⁷) they give exactly the chapter's L_<, L_>, R_b, N_ι, k̄_max, d̄_Φ,
C_lev, I_base, R_base, X_12, T_12, D_*, C_*, D_♭ = D_acc, D′_*, D_b, D_NM, 21D_NM + 6, 22D_NM + 345, 22D_b + 345 and
k̂_0 (21 integers, each asserted equal); and at P-D0's inputs (D_e = 2.06834·10²³) P-D0's D_acc and D_NM.

**At the choice.** Every integer printed in the texts is computed exactly and every decimal is rounded outward: an
upper bound is the least decimal of the stated length strictly above the number, a lower bound the greatest strictly
below, and each comparison printed in a proof (for instance 1.4559836589 · 6.868209 > 10, (1 + Δβ_0/2)² < 1 + 1.5·10⁻¹⁰,
T_< < 2.3514208·10¹⁹ · (1 + 1.5·10⁻¹⁰) + 6.87·10⁹ < 2.35143·10¹⁹, 1.0071 · 1.40639·10²⁰ > 1.41633·10²⁰,
0.3168/(4.71·10⁻²⁰)² > 1.42556·10³⁸, 1002001 · 1.447·10⁻²⁵ < 1.45·10⁻¹⁹) was asserted. The first line of eq:ec-upper:
D_e = 1.41633·10²⁰ > 1.4114762·10²⁰ + 4.84721·10¹⁷ + 2.74·10¹⁰ > F_1 = 1.41631…·10²⁰. The floors:
14,559,836,589 · 6,868,208,951 < 10²⁰ < 14,559,836,589 · 6,868,208,952 < 10²⁰(1 + ε_K) < 14,559,836,589 · 6,868,208,953,
so L_> = L_< + 2 = R_b as before.

| quantity | value at the choice |
|---|---|
| Δβ_0 | 1.4559836589·10⁻¹⁰ (exact) |
| L_<, L_>, R_b | 6,868,208,951, 6,868,208,953, 6,868,208,953 |
| N_ι | 5,188,959,638,229,843,970,554,286,700 < 5.18896·10²⁷ |
| k̄_max, d̄_Φ, 62N̄_Λ + 10 | 2,817,643,822,898,538,579, 228,357,817,884, 228,357,817,892 |
| C_lev | 10,377,919,276,459,687,944,791,764,540 < 1.0378·10²⁸ |
| I_base, R_base, k̂_0 | 161,579,883,606,166,913, 161,579,883,606,189,010, 3,200,585,392,700 |
| X_12 | 11,270,575,291,594,154,340 |
| T_11 | 10,377,919,276,621,267,862,666,783,424 |
| T_12 | 10,377,919,287,730,263,270,654,748,732 |
| D_* = T_12 + 14 | 10,377,919,287,730,263,270,654,748,746 < 1.0378·10²⁸ |
| C_* | 31,133,758,693,167,165,978,342,162,162 < 3.11338·10²⁸ |
| D′_* | 71,277,718,098,469,630,550,670,708,708,947,562,256 < 7.12778·10³⁷ |
| D_acc, D_NM, 21D_NM + 6, 22D_NM + 345 | as in section 0 |

## 4. The sites changed

Chapter 71 (texts U1–U47 of section 6, with U3a, U6a, U22b, U41a, U43a, U44a):

- the opening (U1–U3): the bounds at the computational point, the choice "of the index sets", and the sentence on other
  h qualified "for the index sets as the proofs construct them";
- rem:ec-point-outside, last sentence (U3a): the transfer, for the index sets as constructed;
- thm:loss-d, the paragraph after (iii) (U4, U5);
- rem:ec-lb-unbounded (U6, U6a): the threshold h ≤ 4.71·10⁻²⁰, and the last sentence qualified;
- rem:ec-upper-point (U7), rem:ec-upper-open (U8), sec:uc-close (U9);
- lem:uc-fourier-count, last sentence (U10): which index sets J_* = 15,000,015 and lem:uc-n-iota refer to;
- def:uc-choice (U11), lem:uc-admissible (U12–U14), lem:uc-lambda (U15): P-D0's T6–T9, T12 at the new choice; U14 adds
  ε_K < 0.998ε_Υ ≤ ε_g − 2ε, which the bases use;
- lem:uc-n-iota (U16, U17), prop:uc-explicit (U18), thm:uc-integer (U19: "with the index sets of def:uc-choice",
  eq:uc-lower qualified as cor:is-lower, for the index sets as constructed, beside 1.403·10²⁰ at every choice and
  3R > 1.40639·10²⁰ at the choice), prop:uc-dependence (U20: Part 1, and either family of index sets, which sec:tr
  needs), rem:uc-missing (U21);
- cor:is-lower (U22, U22b): the clause and the sentence on ε_K = 1.6747·10⁻¹⁷, the former choice, removed (true but
  pointing at a choice the paper no longer makes; optional);
- sec:cs opening (U23), lem:cs-levels (U24), lem:cs-iterations (U25), lem:cs-rest (U26), prop:cs-cstar and
  rem:cs-sharpness (U27), sec:cs-small opening (U28, R_base), lem:cs-sharp (U29, U30), lem:uc-small-orders (U31–U35),
  rem:uc-small-reading (U36), prop:uc-d-small (U37–U39), prop:uc-data-order (d) (U40, U41); "with the index sets as
  constructed and the choices of def:uc-choice" becomes "with the choices of def:uc-choice" in prop:cs-cstar,
  lem:uc-small-orders, prop:uc-d-small and prop:uc-data-order (d);
- sec:tr: the opening (U41a: the section keeps the index sets as constructed; the smaller sets are shown to serve at
  the computational point only); thm:tr-transfer (iii) (U42: N̄_Λ := N̄(h), N₁ removed; "with the index sets as
  constructed" is P-D0's T16); rem:tr-scope (U43a, U43: (iii) concerns the index sets as constructed; the
  threshold 1.45·10⁻¹⁹; the lower bounds of (ii) and prop:tr-mu-small are for the index sets as constructed; the flat
  sets are proved to serve at the computational point only); sec:tr-proof (iii) (U44a, U44, U45: lem:uc-admissible with
  the index sets as constructed, ε_K < μ(h) ≤ μ_G < 0.998ε_Υ instead of N₁); prop:tr-fail (U46); the paragraph after
  prop:tr-mu-small (U47).

Other chapters: 00-front (U48), 01-introduction (U49), 03-theorems (U50 after thm:settling; U50a, the constants item:
"of the index sets" and the transfer for the index sets as constructed), 90-scope (U51–U53).

Not changed, and still true: cor:uc-two-offsets, thm:is-gap (its "ε_K = 1.6747·10⁻¹⁷ is admissible" is a statement
about the index sets as constructed), lem:is-gap-z, prop:is-count, rem:gap-sums, the "as constructed" sentences of
sec:sp, thm:uc-reduction as P-D0 leaves it (its closing sentence already says "for the index sets as constructed"),
lem:uc-gaps (P-D0's T10, T11), lem:uc-dr, def:cs-choices, lem:cs-elem, lem:cs-transforms, lem:cs-null, lem:cs-fourier,
lem:cs-base, prop:ec-rounds, prop:tr-lambda, def:tr-excess, prop:tr-mu-small.

## 5. sec:tr once the flat set serves (listed, not rewritten)

The texts above keep sec:tr for the index sets as constructed, where every statement stays true. A version for
ℰ^φ_ind, ℰ^(ι,φ)_ind at h ≠ 10⁻⁶ would first need thm:is-flat-serves proved at h (its index-set part concerns □^Υ_b,
which does not involve h, and the physical states, whose offsets are at least 1, so the extension is plausible but is
not proved). Then:

- **def:tr-excess.** μ(h) (through m(y) of lem:is-reduction, with the increments 𝔡₀ and 𝔡₁) and N̄(h) (through
  1/(2𝔡₀𝔡₁)) would be replaced by μ♭(h) := min({μ♭} ∪ {(⌊y_ι/𝔡₁⌋ + 1)𝔡₁ − y_ι : ι ∈ Z₃(h)}), with μ♭(h) ≥ μ(h) as
  Λ^φ ⊂ Λ, and a count linear in the y_ι, N̄♭(h) := 59,377,257 + Σ_(ι∈Z₃(h))(⌊(y_ι + ε_+)/𝔡₁⌋ + 1), the analogue of
  the count in cor:is-flat; its bound would grow like h^(−1/2) with another constant.
- **prop:tr-lambda.** (a) "the increments of real part below 1 are 𝔡₀ and 𝔡₁" becomes 𝔡₁ alone, and the description
  becomes {ι + q𝔡₁ : q𝔡₁ ≤ y_ι + ε_+}; (b) "(G) iff ε_K < μ(h)" stays true for the index sets as constructed and would
  read "(G) iff ε_K < μ♭(h)" for Λ^φ, with ε_K < ε_Υ asked besides; (c) the linear count.
- **thm:tr-transfer.** (ii) is a lower bound for the index sets as constructed only; for Λ^φ the bound of
  prop:ec-rounds at ε_K < min(ε_Υ, μ♭(h)) would replace it, and it exceeds the universal 1.403·10²⁰ only where
  μ♭(h) < ε_Υ. (iii) would take ℰ^φ_ind, ε_K < ε_+ < min(μ♭(h), 0.998ε_Υ) and N̄_Λ := N̄♭(h); its closing sentence
  (μ(10⁻⁶) = μ_Z, cor:is-lower) would refer to μ♭_Z and cor:is-flat.
- **prop:tr-mu-small** uses w_* = 356327𝔡₀ + 1116082𝔡₁, so 𝔡₀ as an increment, and does not apply to Λ^φ; its analogue
  would come from a root y_ι(h) crossing a multiple of 𝔡₁ and would need its own proof.
- **The sec:tr opening** (input (e), "the gap of (G) becomes the least excess μ(h)"), **sec:tr-proof (iii)** (the list
  of h-independent statements would need def:is-flat-set through thm:is-flat-serves, and cor:is-flat is h-dependent
  through Z₃), **rem:tr-scope** ("its bound is a number only once μ(h) is known", "N̄(10⁻⁶) ≤ 909,507,124,095,312"),
  and the sentences built on them (chapter 71 opening, rem:ec-point-outside, rem:ec-lb-unbounded, 03-theorems constants
  item, 90-scope) would follow.
- prop:tr-fail, prop:tr-measure, the roots of sec:tr-roots and prop:tr-eps, prop:tr-inputs do not depend on the index
  sets and would stay.

## 6. Texts

### Placement

This part and the crosswalk rows are instructions for merging; they are not chapter text. Each old text is quoted
exactly between the fences and occurs exactly once, as whole lines, in its chapter at HEAD 1680675a with P-D0's sixteen
texts applied; each new text replaces it as a whole, with the line breaks shown. Line numbers serve only to find the
place: "with P-D0" is the line in the chapter with P-D0 applied, "HEAD" the line at HEAD. U11–U15 replace P-D0's new
texts T6–T9 and T12 and so apply only after P-D0; all others apply at HEAD before or after P-D0. The texts are
pairwise disjoint; apply from the bottom up, or by matching the old texts. U46 changes only numbers and keeps the line
breaks.

#### U1. 71-explicit-constants.md, lines 22–28 with P-D0 (HEAD 22–28)

Place: the chapter opening, second paragraph: the bounds at the computational point.

Old (7 lines):

```old
and so d, larger
than 1.403 × 10²⁰ and N_NM larger than 2.946 × 10²¹ ([[thm:loss-d]]), and larger than 1.2250 × 10²⁷ and 2.5725 × 10²⁸ for
the index sets as the proofs construct them ([[cor:is-lower]]). At that point, at one admissible choice of the weights
and of the free orders and inner products ([[def:uc-choice]], [[def:cs-choices]]), d_acc is at most an integer below
3.78623 × 10⁵⁵, and d_NM, the d of [[thm:iii-k-3-2]], at least d_acc and the orders at which its lemmas ask U small
([[prop:uc-d-small]]), is at most an integer below 7.57245 × 10⁵⁵, and N_NM at most one below 1.59022 × 10⁵⁷
([[thm:uc-integer]]). That parameter point is not shown to lie in the set on which [[thm:settling]] is proved
```

New (7 lines):

```new
and so d, larger than 1.403 × 10²⁰ and N_NM larger than 2.946 × 10²¹ ([[thm:loss-d]]), and, for the index sets as the
proofs construct them, larger than 1.2250 × 10²⁷ and 2.5725 × 10²⁸ ([[cor:is-lower]]). At that point, at one admissible
choice of the index sets ([[thm:is-flat-serves]]), of the weights and of the free orders and inner products
([[def:uc-choice]], [[def:cs-choices]]), d_acc is at most an integer below 7.12778 × 10³⁷, and d_NM, the d of
[[thm:iii-k-3-2]], at least d_acc and the orders at which its lemmas ask U small ([[prop:uc-d-small]]), is at most an
integer below 1.42556 × 10³⁸, and N_NM at most one below 2.99367 × 10³⁹ ([[thm:uc-integer]]). That parameter point is not
shown to lie in the set on which [[thm:settling]] is proved
```

#### U2. 71-explicit-constants.md, lines 30–31 with P-D0 (HEAD 30–31)

Place: the chapter opening, second paragraph: the lower bound at other h, for the index sets as constructed.

Old (2 lines):

```old
it bound what this proof's choices produce, not the optimal loss. At the admissible parameter points with the same gauge
values and other values h ∈ (0, 10⁻⁶) of the damping parameter, d_acc and d_NM exceed 2.0517 × 10¹⁰/μ(h), μ(h) the least
```

New (3 lines):

```new
it bound what this proof's choices produce, not the optimal loss. At the admissible parameter points with the same gauge
values and other values h ∈ (0, 10⁻⁶) of the damping parameter, for the index sets as the proofs construct them, d_acc
and d_NM exceed 2.0517 × 10¹⁰/μ(h), μ(h) the least
```

#### U3. 71-explicit-constants.md, lines 40 with P-D0 (HEAD 40)

Place: the chapter opening, second paragraph: the order K.

Old (1 line):

```old
being an explicit number of derivatives; at the computational point K is at most an integer below 1.66594 × 10⁵⁷
```

New (1 line):

```new
being an explicit number of derivatives; at the computational point K is at most an integer below 3.13622 × 10³⁹
```

#### U3a. 71-explicit-constants.md, lines 93–97 with P-D0 (HEAD 93–97)

Place: rem:ec-point-outside, the last sentence: for the index sets as constructed.

Old (5 lines):

```old
4.76·10⁻¹¹ ≤ h < 10⁻⁶ outside a set of h of total length below 1.7·10⁻¹¹, the inputs of [[thm:uc-integer]] that depend on
h enter its proof as at the computational point, except the roots of real part below 3 of the damping polynomials,
through which the gap of (G) and the count N_Λ of [[lem:uc-lambda]] move with h; at the admissible points among these at
which the degrees l with hl(l + 2) > 70 have no root of real part in [2, 3 + ε_Υ), a condition decided only at h = 10⁻⁶,
the bounds of [[prop:uc-dependence]] hold with the gap and the count at h ([[thm:tr-transfer]]).
```

New (6 lines):

```new
4.76·10⁻¹¹ ≤ h < 10⁻⁶ outside a set of h of total length below 1.7·10⁻¹¹, and for the index sets as constructed, the
inputs that depend on h enter the proof of [[thm:uc-integer]], run with these index sets ([[prop:uc-dependence]]), as at
the computational point, except the roots of real part below 3 of the damping polynomials, through which the gap of (G)
and the count N_Λ move with h; at the admissible points among these at which the degrees l with hl(l + 2) > 70 have no
root of real part in [2, 3 + ε_Υ), a condition decided only at h = 10⁻⁶, the bounds of [[prop:uc-dependence]] hold with
the gap and the count at h ([[thm:tr-transfer]]).
```

#### U4. 71-explicit-constants.md, lines 1504–1506 with P-D0 (HEAD 1504–1506)

Place: thm:loss-d, the paragraph after (iii): the index sets.

Old (3 lines):

```old
The bounds (ii) are lower bounds for the loss that this proof's choices produce, not for the least loss with which the
tame estimates hold; for the index sets as the proofs construct them, (G) asks ε_K < μ_Z ([[thm:is-gap]]), and the lower
bound rises to 3R > 1.2250 × 10²⁷ ([[cor:is-lower]]). At every point of the set on which [[thm:settling]] is proved
```

New (4 lines):

```new
The bounds (ii) are lower bounds for the loss that this proof's choices produce, not for the least loss with which the
tame estimates hold; for the index sets as the proofs construct them, (G) asks ε_K < μ_Z ([[thm:is-gap]]), and the lower
bound rises to 3R > 1.2250 × 10²⁷ ([[cor:is-lower]]), while for the smaller index sets of [[def:uc-choice]] (G) asks only
ε_K < μ♭_Z, a number above ε_Υ ([[cor:is-flat]]). At every point of the set on which [[thm:settling]] is proved
```

#### U5. 71-explicit-constants.md, lines 1511–1514 with P-D0 (HEAD 1511–1514)

Place: thm:loss-d, the paragraph after (iii): the upper bounds.

Old (4 lines):

```old
the index sets. At the computational point [[thm:uc-integer]] evaluates every number of steps and every such count, and
[[lem:uc-small-orders]] and [[prop:uc-d-small]] the orders at which the proof of [[thm:iii-k-3-2]] asks U small: d_acc is
at most an integer below 3.78623 × 10⁵⁵, d_NM at most one below 7.57245 × 10⁵⁵, and N_NM at most one below
1.59022 × 10⁵⁷.
```

New (4 lines):

```new
the index sets. At the computational point [[thm:uc-integer]] evaluates every number of steps and every such count, and
[[lem:uc-small-orders]] and [[prop:uc-d-small]] the orders at which the proof of [[thm:iii-k-3-2]] asks U small: d_acc is
at most an integer below 7.12778 × 10³⁷, d_NM at most one below 1.42556 × 10³⁸, and N_NM at most one below
2.99367 × 10³⁹.
```

#### U6. 71-explicit-constants.md, lines 1825 with P-D0 (HEAD 1825)

Place: rem:ec-lb-unbounded.

Old (1 line):

```old
exceeds 7.57245·10⁵⁵, the bound of [[thm:uc-integer]], at every point of the proved set with h ≤ 6.46·10⁻²⁹. Likewise, at
```

New (1 line):

```new
exceeds 1.42556·10³⁸, the bound of [[thm:uc-integer]], at every point of the proved set with h ≤ 4.71·10⁻²⁰. Likewise, at
```

#### U6a. 71-explicit-constants.md, lines 1832–1834 with P-D0 (HEAD 1832–1834)

Place: rem:ec-lb-unbounded, the last sentence: for the index sets as constructed.

Old (3 lines):

```old
only. At the admissible points with (e_Υ, γ_Υ) = (1/100, 1/100) and other h ≤ 10⁻⁶ the second is replaced by
d_NM > 2.0517·10¹⁰/μ(h), with the least excess μ(h) of [[def:tr-excess]] ([[thm:tr-transfer]]); as h decreases to a point
h_μ ∈ (5·10⁻⁷, 10⁻⁶), μ(h) tends to 0 and this bound to infinity ([[prop:tr-mu-small]]).
```

New (3 lines):

```new
only. At the admissible points with (e_Υ, γ_Υ) = (1/100, 1/100) and other h ≤ 10⁻⁶ the second is replaced, for the same
index sets, by d_NM > 2.0517·10¹⁰/μ(h), with the least excess μ(h) of [[def:tr-excess]] ([[thm:tr-transfer]]); as h
decreases to a point h_μ ∈ (5·10⁻⁷, 10⁻⁶), μ(h) tends to 0 and this bound to infinity ([[prop:tr-mu-small]]).
```

#### U7. 71-explicit-constants.md, lines 2224–2234 with P-D0 (HEAD 2224–2234)

Place: rem:ec-upper-point, the whole remark.

Old (11 lines):

```old
**Remark {#rem:ec-upper-point}** (The upper bound at the computational point.) At the computational point ε_g ≤ ε_Υ <
1.46214·10⁻¹⁰ ([[lem:ec-gauge-gap]], [[rem:ec-gauge-gap]]), and for the index sets as the proofs construct them every ε_K
with which (G) holds lies below 1.6747859·10⁻¹⁷ ([[thm:is-gap]]). The levels are then less than 1.6747859·10⁻¹⁷ apart,
and the first line of [[eq:ec-upper]] is of the order 3/(ε_Kε_g), the order of the lower bound 3R of [[prop:ec-rounds]].
[[prop:uc-explicit]] evaluates it at the admissible choice of [[def:uc-choice]], with ε_K = 1.6747·10⁻¹⁷ and ε_g = ε_Υ =
1.4619·10⁻¹⁰: it is less than 1.23382·10²⁷, of which less than 4.22261·10²⁴ comes from the window loops at ι⁺ (bounded
there through ε^ι_ind = 𝔡₁, [[lem:uc-gaps]]), and less than 1.0072 times the lower bound 3R > 1.2251·10²⁷ at the same
choice ([[thm:uc-integer]]). The losses c(β_k), c_b and c′_b of single steps enter the second line with the
multiplicities K, N_b and N_b + 1, and c_0 once: at most 59,831,791,007,643,518 levels lie in (2, 3), where c(β_k) ≤ 497,
at most 59,831,791,007,643,520 in (3, α], where c(β_k) ≤ C_lev < 6.32812·10³⁸ ([[lem:cs-levels]]), and N_b <
59,831,791,007,643,520 ([[prop:uc-explicit]]); [[prop:cs-cstar]] bounds c_0 by C_* < 1.89844·10³⁹.
```

New (12 lines):

```new
**Remark {#rem:ec-upper-point}** (The upper bound at the computational point.) At the computational point ε_g ≤ ε_Υ <
1.46214·10⁻¹⁰ ([[lem:ec-gauge-gap]], [[rem:ec-gauge-gap]]). For the index sets as the proofs construct them every ε_K
with which (G) holds lies below 1.6747859·10⁻¹⁷ ([[thm:is-gap]]); for the smaller index sets of [[def:uc-choice]], which
omit the offset 𝔡₀, (G) holds for every ε_K < ε_Υ ([[cor:is-flat]]). The levels are less than ε_K apart, and the first
line of [[eq:ec-upper]] is of the order 3/(ε_Kε_g), the order of the lower bound 3R of [[prop:ec-rounds]].
[[prop:uc-explicit]] evaluates it at the admissible choice of [[def:uc-choice]], with ε_K = 1.4589·10⁻¹⁰ and ε_g = ε_Υ =
1.4619·10⁻¹⁰: it is less than 1.41633·10²⁰, of which less than 4.84721·10¹⁷ comes from the window loops at ι⁺ (bounded
there through ε^ι_ind = 𝔡₁, [[lem:uc-gaps]]), and less than 1.0071 times the lower bound 3R > 1.40639·10²⁰ at the same
choice ([[thm:uc-integer]]). The losses c(β_k), c_b and c′_b of single steps enter the second line with the
multiplicities K, N_b and N_b + 1, and c_0 once: at most 6,868,208,951 levels lie in (2, 3), where c(β_k) ≤ 497, at most
6,868,208,953 in (3, α], where c(β_k) ≤ C_lev < 1.0378·10²⁸ ([[lem:cs-levels]]), and N_b < 6,868,208,953
([[prop:uc-explicit]]); [[prop:cs-cstar]] bounds c_0 by C_* < 3.11338·10²⁸.
```

#### U8. 71-explicit-constants.md, lines 2236–2263 with P-D0 (HEAD 2236–2263)

Place: rem:ec-upper-open, the whole remark.

Old (28 lines):

```old
**Remark {#rem:ec-upper-open}** (The inputs of the upper bound.) Four inputs separate [[prop:ec-upper]] from an integer;
at the computational point all four are bounded: (1), (2) and (4) are evaluated, and (3) through the numbers C_lev and
C_*, which [[lem:cs-levels]] and [[prop:cs-cstar]] bound. (1) ε_K, N_Λ, k̄_0 and l_*: (G) asks that no element of the set
Λ of [[def:iii-i10-1-1]] have real part in (2, 2 + ε_K] or in (3, 3 + ε_K], and that no λ + d_c0 or λ + d_c1, λ ∈ Λ, have
real part in (2, 2 + ε_K]. [[prop:gap-sums]] and [[rem:gap-sums]] settle the three windows for ε_K < 5.019·10⁻⁸ on the
part of Λ built from 2, 3, λ_♯ and the offsets 𝔡₁, 1 + 𝔡₀, 1 + δ₂, 1 + δ′₁. With ℰ_ind as the proofs construct it, 𝔡₀ and
𝔡₁ are themselves increments, which asks ε_K < 1.6417·10⁻¹⁴ ([[cor:uc-two-offsets]]), and with the generators 1 + 𝒵 of Λ
(G) holds exactly for ε_K < μ_Z, where μ_Z < 1.6747859·10⁻¹⁷ ([[thm:is-gap]], [[eq:is-mu-z]]); [[prop:is-count]] and
[[cor:sp-lstar]] give N_Λ ≤ 909,507,124,095,312, k̄_0 = 3, J_* = 15,000,015 and the admissible l_* = 50, and
[[prop:uc-explicit]] the numbers of levels, rounds, applications and windows at an admissible choice. (2) ℓ⁺_tf = 1 at
the choices of [[lem:ec-tf-loss]] with s = 1 ([[prop:uc-ltf]]). (3) The single-step losses c(β), c_b, c′_b and c_0: each
is a finite composition of the elementary losses of [[lem:ec-closed-forms]] and [[rem:ec-other-losses]] and of the
forward loss, at most 20,180 ([[thm:fwd-loss]], [[cor:fwd-near-b0]]) and 20,183 at the backgrounds h + h_rem(q) +
h_tot(p⃗) ([[lem:cs-elem]] (e)), charged at each forward solution they apply; they contain the counts n(E, β) of the
index sets entering [[eq:ec-fourier-loss]], which [[lem:uc-n-iota]] bounds through N_Λ, k̄_0, l_* and J_*; c_0 contains,
besides, the iterations of Steps 4′ and 4 at the top level, each bounded as in [[lem:ec-counts]], and the loss of
[[thm:iii-j-2-4]], which its proof takes as the sum of the losses of its steps over the exponents of Λ ∩ {Re < 3 + ε_+}
([[lem:uc-phi-loss]]). The c(β) of the levels above 3 are at most C_lev < 6.32812·10³⁸ ([[lem:cs-levels]]), and these
levels, at most 59,831,791,007,643,520 of them, carry the bound of [[thm:uc-integer]]; c_0 enters once, and
[[prop:cs-cstar]] bounds it by C_* < 1.89844·10³⁹. (4) d_BG = 11 serves ([[prop:uc-dbg]]); it enters c(β), c_b, c′_b
and c_0 through the charge max(2, d_BG). For d_NM, and so for N_NM, the losses of [[lem:iii-k-2-2]] and
[[prop:iii-j2-4-3]] are at most 62N_Λ + 10 ≤ 56,389,441,693,909,354 ([[lem:uc-phi-loss]], [[lem:uc-lambda]]), that of
[[lem:iii-k-2-3]] satisfies [[eq:ec-upper]] in the form of [[lem:uc-dr]], and [[lem:uc-small-orders]] and
[[prop:uc-d-small]] bound the orders at which these results ask U small, and with them d_NM ([[thm:uc-integer]]). Given
ε_K, the explicit part of [[eq:ec-upper]] is of the order 1/(ε_Kε_g), the order of the lower bound of [[prop:ec-rounds]];
ℓ⁺_tf multiplies terms of that order, c(β) enters at most N_< + N_> times, about 2/ε_K, and c_b and c′_b at most about
1/ε_K times each. All these numbers depend on the point through z, which fixes ε_Υ ([[rem:ec-gauge-gap]]), and through
the index sets.
```

New (29 lines):

```new
**Remark {#rem:ec-upper-open}** (The inputs of the upper bound.) Four inputs separate [[prop:ec-upper]] from an integer;
at the computational point all four are bounded: (1), (2) and (4) are evaluated, and (3) through the numbers C_lev and
C_*, which [[lem:cs-levels]] and [[prop:cs-cstar]] bound. (1) ε_K, N_Λ, k̄_0 and l_*: (G) asks that no element of the set
Λ of [[def:iii-i10-1-1]] have real part in (2, 2 + ε_K] or in (3, 3 + ε_K], and that no λ + d_c0 or λ + d_c1, λ ∈ Λ, have
real part in (2, 2 + ε_K]. [[prop:gap-sums]] and [[rem:gap-sums]] settle the three windows for ε_K < 5.019·10⁻⁸ on the
part of Λ built from 2, 3, λ_♯ and the offsets 𝔡₁, 1 + 𝔡₀, 1 + δ₂, 1 + δ′₁. With ℰ_ind as the proofs construct it, 𝔡₀ and
𝔡₁ are themselves increments, which asks ε_K < 1.6417·10⁻¹⁴ ([[cor:uc-two-offsets]]), and with the generators 1 + 𝒵 of Λ
(G) holds exactly for ε_K < μ_Z, where μ_Z < 1.6747859·10⁻¹⁷ ([[thm:is-gap]], [[eq:is-mu-z]]). The index sets of
[[def:uc-choice]] ([[def:is-flat-set]]) omit 𝔡₀ and serve as well ([[thm:is-flat-serves]]); with them (G) holds exactly
for ε_K < μ♭_Z, where μ♭_Z > ε_Υ, [[cor:is-flat]] gives N_Λ ≤ 3,683,190,611, [[thm:is-flat-serves]] and [[cor:sp-lstar]]
give k̄_0 = 3, J_* = 15,000,015 and the admissible l_* = 50, and [[prop:uc-explicit]] gives the numbers of levels,
rounds, applications and windows at an admissible choice. (2) ℓ⁺_tf = 1 at the choices of [[lem:ec-tf-loss]] with s = 1
([[prop:uc-ltf]]). (3) The single-step losses c(β), c_b, c′_b and c_0: each is a finite composition of the elementary
losses of [[lem:ec-closed-forms]] and [[rem:ec-other-losses]] and of the forward loss, at most 20,180 ([[thm:fwd-loss]],
[[cor:fwd-near-b0]]) and 20,183 at the backgrounds h + h_rem(q) + h_tot(p⃗) ([[lem:cs-elem]] (e)), charged at each
forward solution they apply; they contain the counts n(E, β) of the index sets entering [[eq:ec-fourier-loss]], which
[[lem:uc-n-iota]] bounds through N_Λ, k̄_0, l_* and J_*; c_0 contains, besides, the iterations of Steps 4′ and 4 at the
top level, each bounded as in [[lem:ec-counts]], and the loss of [[thm:iii-j-2-4]], which its proof takes as the sum of
the losses of its steps over the exponents of Λ ∩ {Re < 3 + ε_+} ([[lem:uc-phi-loss]]). The c(β) of the levels above 3
are at most C_lev < 1.0378·10²⁸ ([[lem:cs-levels]]), and these levels, at most 6,868,208,953 of them, carry the bound of
[[thm:uc-integer]]; c_0 enters once, and [[prop:cs-cstar]] bounds it by C_* < 3.11338·10²⁸. (4) d_BG = 11 serves
([[prop:uc-dbg]]); it enters c(β), c_b, c′_b and c_0 through the charge max(2, d_BG). For d_NM, and so for N_NM, the
losses of [[lem:iii-k-2-2]] and [[prop:iii-j2-4-3]] are at most 62N_Λ + 10 ≤ 228,357,817,892 ([[lem:uc-phi-loss]],
[[lem:uc-lambda]]), that of [[lem:iii-k-2-3]] satisfies [[eq:ec-upper]] in the form of [[lem:uc-dr]], and
[[lem:uc-small-orders]] and [[prop:uc-d-small]] bound the orders at which these results ask U small, and with them d_NM
([[thm:uc-integer]]). Given ε_K, the explicit part of [[eq:ec-upper]] is of the order 1/(ε_Kε_g), the order of the lower
bound of [[prop:ec-rounds]]; ℓ⁺_tf multiplies terms of that order, c(β) enters at most N_< + N_> times, about 2/ε_K, and
c_b and c′_b at most about 1/ε_K times each. All these numbers depend on the point through z, which fixes ε_Υ
([[rem:ec-gauge-gap]]), and through the index sets.
```

#### U9. 71-explicit-constants.md, lines 2267–2286 with P-D0 (HEAD 2267–2286)

Place: sec:uc-close, the opening paragraph.

Old (20 lines):

```old
This section takes the inputs that [[prop:ec-upper]] leaves free, evaluates them at the computational point, and
assembles the bound. Two are fixed by general statements of this paper. The loss of the inverse of the transition face
model is 1 at the weights at which the construction may use it, so ℓ_tf = 1 ([[prop:uc-ltf]]); and the order of the
background terms may be taken to be d_BG = 11 ([[prop:uc-dbg]]). The others are fixed by the index sets that define
the set Λ of [[def:iii-i10-1-1]] and by the orders of the poles of N_ι⁺(L̄, ·)⁻¹: the admissible ε_K of the gap condition
(G), the counts n(E, β) of the index sets entering the Fourier steps of the levels ([[lem:uc-fourier-count]]), and the
loss of the map Φ of [[thm:iii-j-2-4]], which governs the other two losses ([[lem:uc-phi-loss]]). Memberships and least
real parts of the index sets alone fix no admissible ε_K ([[prop:uc-no-eps]]); if both offsets of the class roots are
increments of Λ, as they are for the index sets that the proofs construct, every admissible ε_K lies below 1.6417·10⁻¹⁴
([[cor:uc-two-offsets]]), and the generators 1 + 𝒵 of Λ put it below 1.6747859·10⁻¹⁷ ([[thm:is-gap]]). [[sec:is]] lists
the exponents of the index sets as constructed, and [[sec:sp]] the poles of N_ι⁺(L̄, ·)⁻¹ at real part at most 5, all
simple. With them (G) holds exactly for ε_K < μ_Z ([[thm:is-gap]]), and N_Λ, k̄_0, l_* and J_* are explicit
([[prop:is-count]], [[cor:sp-lstar]]). [[sec:uc-eval]] fixes an admissible choice of the weights, evaluates every
count of [[eq:ec-upper]] at it, and proves [[thm:uc-integer]]: d_acc and d_R are at most an integer D_acc < 3.78623·10⁵⁵,
and d_NM at most an integer D_NM < 7.57245·10⁵⁵, the single-step losses being at most C_lev < 6.32812·10³⁸ at the levels
above 3 ([[lem:cs-levels]]) and at most C_* < 1.89844·10³⁹ in all ([[prop:cs-cstar]]), and the orders of smallness being
bounded in [[sec:cs-small]], against the lower bound 1.2250·10²⁷ ([[cor:is-lower]]); [[prop:uc-dependence]] gives D_acc
and D_NM as functions of the inputs of the choice, and [[rem:uc-missing]] states what the bound rests on. Throughout we
work at the computational point of [[def:ec-point]], so z = 4·10⁻⁶ = 1/250000 and λ_♯ = 15099/10000, and 𝔡₀ = d_c0, 𝔡₁ =
d_c1 are the offsets of [[sec:ec-gap-sums]].
```

New (22 lines):

```new
This section takes the inputs that [[prop:ec-upper]] leaves free, evaluates them at the computational point, and
assembles the bound. Two are fixed by general statements of this paper. The loss of the inverse of the transition face
model is 1 at the weights at which the construction may use it, so ℓ_tf = 1 ([[prop:uc-ltf]]); and the order of the
background terms may be taken to be d_BG = 11 ([[prop:uc-dbg]]). The others are fixed by the index sets that define
the set Λ of [[def:iii-i10-1-1]] and by the orders of the poles of N_ι⁺(L̄, ·)⁻¹: the admissible ε_K of the gap condition
(G), the counts n(E, β) of the index sets entering the Fourier steps of the levels ([[lem:uc-fourier-count]]), and the
loss of the map Φ of [[thm:iii-j-2-4]], which governs the other two losses ([[lem:uc-phi-loss]]). Memberships and least
real parts of the index sets alone fix no admissible ε_K ([[prop:uc-no-eps]]); if both offsets of the class roots are
increments of Λ, as they are for the index sets that the proofs construct, every admissible ε_K lies below 1.6417·10⁻¹⁴
([[cor:uc-two-offsets]]), and the generators 1 + 𝒵 of Λ put it below 1.6747859·10⁻¹⁷ ([[thm:is-gap]]). [[sec:is]] lists
the exponents of the index sets as constructed, and [[sec:sp]] the poles of N_ι⁺(L̄, ·)⁻¹ at real part at most 5, all
simple. With them (G) holds exactly for ε_K < μ_Z ([[thm:is-gap]]), and N_Λ, k̄_0, l_* and J_* are explicit
([[prop:is-count]], [[cor:sp-lstar]]). Smaller index sets, which omit the offset 𝔡₀, serve as well
([[thm:is-flat-serves]]); with them (G) holds for every ε_K < ε_Υ, and N_Λ ≤ 3,683,190,611 ([[cor:is-flat]]).
[[sec:uc-eval]] fixes an admissible choice of these index sets and of the weights, evaluates every count of
[[eq:ec-upper]] at it, and proves [[thm:uc-integer]]: d_acc and d_R are at most an integer D_acc < 7.12778·10³⁷, and d_NM
at most an integer D_NM < 1.42556·10³⁸, the single-step losses being at most C_lev < 1.0378·10²⁸ at the levels above 3
([[lem:cs-levels]]) and at most C_* < 3.11338·10²⁸ in all ([[prop:cs-cstar]]), and the orders of smallness being bounded
in [[sec:cs-small]], against the lower bound 3R > 1.40639·10²⁰ at that choice ([[thm:uc-integer]]);
[[prop:uc-dependence]] gives D_acc and D_NM as functions of the inputs of the choice, and [[rem:uc-missing]] states what
the bound rests on. Throughout we work at the computational point of [[def:ec-point]], so z = 4·10⁻⁶ = 1/250000 and λ_♯ =
15099/10000, and 𝔡₀ = d_c0, 𝔡₁ = d_c1 are the offsets of [[sec:ec-gap-sums]].
```

#### U10. 71-explicit-constants.md, lines 2535–2536 with P-D0 (HEAD 2533–2534)

Place: lem:uc-fourier-count, the last sentence of the statement.

Old (2 lines):

```old
least 1 + n_ι. (For the index sets as constructed, η_0 = 𝔡₁ and J_* = 15,000,015 ([[prop:is-count]] (c)), and
[[lem:uc-n-iota]] gives a sharper bound for n_ι.)
```

New (2 lines):

```new
least 1 + n_ι. (For the index sets as constructed and for those of [[def:uc-choice]], η_0 = 𝔡₁ and J_* = 15,000,015
([[prop:is-count]] (c), [[thm:is-flat-serves]]), and at that choice [[lem:uc-n-iota]] gives a sharper bound for n_ι.)
```

#### U11. 71-explicit-constants.md, lines 2614 with P-D0 (P-D0's new text of T6)

Place: def:uc-choice, the display eq:uc-choice (P-D0's T6).

Old (1 line):

```old
    ε_Υ := 1.4619·10⁻¹⁰,     ε_K := 9.99·10⁻¹⁴,     ε_+ := 9.995·10⁻¹⁴,     l_* := 50,     k̄_0 := 3.
```

New (1 line):

```new
    ε_Υ := 1.4619·10⁻¹⁰,     ε_K := 1.4589·10⁻¹⁰,     ε_+ := 1.459·10⁻¹⁰,     l_* := 50,     k̄_0 := 3.
```

#### U12. 71-explicit-constants.md, lines 2631 with P-D0 (P-D0's new text of T7)

Place: lem:uc-admissible, the display eq:uc-deltas (P-D0's T7).

Old (1 line):

```old
    Δβ_0 := 0.999²ε_K = 9.97002999·10⁻¹⁴,     Δτ_0 := 0.999ε_Υ = 1.4604381·10⁻¹⁰.                      {#eq:uc-deltas}
```

New (1 line):

```new
    Δβ_0 := 0.999²ε_K = 1.4559836589·10⁻¹⁰,     Δτ_0 := 0.999ε_Υ = 1.4604381·10⁻¹⁰.       {#eq:uc-deltas}
```

#### U13. 71-explicit-constants.md, lines 2637–2642 with P-D0 (P-D0's new text of T8)

Place: lem:uc-admissible, proof: the constants, (G) and (G⁺) (P-D0's T8).

Old (6 lines):

```old
0 < ε_K < ε_+ < min(δ_♯, ε_ind), and 9.99·10⁻¹⁴ < 9.995·10⁻¹⁴ < 1.9413·10⁻⁸ < δ_50, while
δ_♯ = λ_♯ − 3/2 = 0.0099. *(G).* By [[cor:is-flat]], for the set Λ that [[def:iii-i10-1-1]] builds from the index sets
of [[def:uc-choice]], (G) holds if and only if ε_K < μ♭_Z, and μ♭_Z > 3.548125563·10⁻¹⁰ > 9.99·10⁻¹⁴ = ε_K. Also
ε_K < ε_Υ, as [[def:iii-i10-1-3]] asks. *(G⁺) and the exactness conditions.* By [[cor:is-flat]] and its proof, μ♭_Z is
the least excess above 3 of the real parts of the elements of Λ, and ε_+ = 9.995·10⁻¹⁴ < μ♭_Z; so no λ ∈ Λ has real
part in (3, 3 + ε_+], which is (G⁺) of
```

New (6 lines):

```new
0 < ε_K < ε_+ < min(δ_♯, ε_ind), and 1.4589·10⁻¹⁰ < 1.459·10⁻¹⁰ < 1.9413·10⁻⁸ < δ_50, while δ_♯ = λ_♯ − 3/2 = 0.0099.
*(G).* By [[cor:is-flat]], for the set Λ that [[def:iii-i10-1-1]] builds from the index sets of [[def:uc-choice]], (G)
holds if and only if ε_K < μ♭_Z, and μ♭_Z > 3.548125563·10⁻¹⁰ > 1.4589·10⁻¹⁰ = ε_K. Also ε_K < ε_Υ, as
[[def:iii-i10-1-3]] asks. *(G⁺) and the exactness conditions.* By [[cor:is-flat]] and its proof, μ♭_Z is the least excess
above 3 of the real parts of the elements of Λ, and ε_+ = 1.459·10⁻¹⁰ < μ♭_Z; so no λ ∈ Λ has real part in (3, 3 + ε_+],
which is (G⁺) of
```

#### U14. 71-explicit-constants.md, lines 2652–2654 with P-D0 (P-D0's new text of T9)

Place: lem:uc-admissible, proof: ε and α (P-D0's T9).

Old (3 lines):

```old
δ₄ + ℓ_3 + 2ε < ε_g, where ℓ_3 = α − 4 − ε < ε_K; it exists, as ε_K + ε ≤ 9.99·10⁻¹⁴ + 1.4619·10⁻¹³ < ε_g. *α.* An
admissible α ≥ 3 is a number in (4 + ε_K − ε′_0, 4 + ε_K], ε′_0 = ½ min(ε_K, ε_+ − ε_K) = ½(ε_+ − ε_K) =
2.5·10⁻¹⁷, off a finite set ([[def:iii-i10-1-3]]), and (A_J), (Ex3) and (Ex4) exclude finitely many more
```

New (4 lines):

```new
δ₄ + ℓ_3 + 2ε < ε_g, where ℓ_3 = α − 4 − ε < ε_K; it exists, as ε_K + ε ≤ 1.4589·10⁻¹⁰ + 1.4619·10⁻¹³ < ε_g. Also ε_K <
0.998ε_Υ ≤ ε_g − 2ε, as 0.998 · 1.4619·10⁻¹⁰ = 1.4589762·10⁻¹⁰; the bases of [[lem:cs-rest]] and [[sec:cs-small]] use
this. *α.* An admissible α ≥ 3 is a number in (4 + ε_K − ε′_0, 4 + ε_K], ε′_0 = ½ min(ε_K, ε_+ − ε_K) = ½(ε_+ − ε_K) =
5·10⁻¹⁵, off a finite set ([[def:iii-i10-1-3]]), and (A_J), (Ex3) and (Ex4) exclude finitely many more
```

#### U15. 71-explicit-constants.md, lines 2691–2708 with P-D0 (P-D0's new text of T12)

Place: lem:uc-lambda, the whole lemma (P-D0's T12).

Old (18 lines):

```old
**Lemma {#lem:uc-lambda}** (The numbers of [[def:iii-i10-1-1]].) At the choice of [[def:uc-choice]]:

(a) N_Λ = #(Λ ∩ {Re < 3 + ε_+}) is an integer with N_Λ ≤ 3,683,190,611 < N̄_Λ := 77,112,616,084;

(b) k̄_0 = 3, l_* = 50, η_0 = 𝔡₁ and J_* = 15,000,015, so that J′ := (J_* + 1)(l_* + 1) = 765,000,816;

(c) listed in an order of non-decreasing real part as λ_1, …, λ_(N_Λ), the elements of Λ ∩ {Re < 3 + ε_+} have n(λ_i) ≤
i − 1 and k̄(λ_i) ≤ k̄_0 + J′i ≤ k̄_max := k̄_0 + J′N̄_Λ = 58,991,214,228,154,724,547;

(d) d_Φ = 62N_Λ + 2 ≤ d̄_Φ := 62N̄_Λ + 2 = 4,780,982,197,210, and d_FM, d_Ψ ≤ 62N̄_Λ + 10 = 4,780,982,197,218.

*Proof.* (a) N_Λ ≤ 3,683,190,611 is [[cor:is-flat]], as ε_+ < μ♭_Z. N̄_Λ is taken larger, so that 4k̄_max + 24 exceeds
I_base + 22,119 ([[prop:uc-dependence]], [[eq:cs-iterations]]): with R_b = 10,030,060,100,152 ([[eq:uc-levels]]),
I_base + 22,119 = 235,964,856,912,243,213,665 < 235,964,856,912,618,898,212 = 4k̄_max + 24. (b) [[thm:is-flat-serves]]
gives that k̄_0 = 3, η_0 = 𝔡₁, J_* = 15,000,015 and l_* = 50 are admissible; and 15,000,016 · 51 = 765,000,816. (c) The
λ′ ∈ Λ with Re λ′ < Re λ_i lie in Λ ∩ {Re < 3 + ε_+} and come before λ_i in the list, so n(λ_i) ≤ i − 1; then
[[def:iii-i10-1-1]] gives k̄(λ_i) = k̄_0 + J′(n(λ_i) + 1) ≤ k̄_0 + J′i, and i ≤ N_Λ ≤ N̄_Λ. (d) is [[lem:uc-phi-loss]]
with (a), as 62 · 77,112,616,084 = 4,780,982,197,208. ∎
```

New (16 lines):

```new
**Lemma {#lem:uc-lambda}** (The numbers of [[def:iii-i10-1-1]].) At the choice of [[def:uc-choice]]:

(a) N_Λ = #(Λ ∩ {Re < 3 + ε_+}) is an integer with N_Λ ≤ N̄_Λ := 3,683,190,611;

(b) k̄_0 = 3, l_* = 50, η_0 = 𝔡₁ and J_* = 15,000,015, so that J′ := (J_* + 1)(l_* + 1) = 765,000,816;

(c) listed in an order of non-decreasing real part as λ_1, …, λ_(N_Λ), the elements of Λ ∩ {Re < 3 + ε_+} have n(λ_i) ≤
i − 1 and k̄(λ_i) ≤ k̄_0 + J′i ≤ k̄_max := k̄_0 + J′N̄_Λ = 2,817,643,822,898,538,579;

(d) d_Φ = 62N_Λ + 2 ≤ d̄_Φ := 62N̄_Λ + 2 = 228,357,817,884, and d_FM, d_Ψ ≤ 62N̄_Λ + 10 = 228,357,817,892.

*Proof.* (a) is [[cor:is-flat]], as ε_+ < μ♭_Z ([[lem:uc-admissible]]). (b) [[thm:is-flat-serves]] gives that k̄_0 = 3,
η_0 = 𝔡₁, J_* = 15,000,015 and l_* = 50 are admissible; and 15,000,016 · 51 = 765,000,816. (c) The λ′ ∈ Λ with Re λ′ < Re
λ_i lie in Λ ∩ {Re < 3 + ε_+} and come before λ_i in the list, so n(λ_i) ≤ i − 1; then [[def:iii-i10-1-1]] gives
k̄(λ_i) = k̄_0 + J′(n(λ_i) + 1) ≤ k̄_0 + J′i, and i ≤ N_Λ ≤ N̄_Λ. (d) is [[lem:uc-phi-loss]] with (a), as 62 ·
3,683,190,611 = 228,357,817,882. ∎
```

#### U16. 71-explicit-constants.md, lines 2716 with P-D0 (HEAD 2708)

Place: lem:uc-n-iota, the value of N_ι.

Old (1 line):

```old
and N_ι = 316,405,564,857,307,442,898,487,679,625,881,224,896 < 3.16406·10³⁸. In particular the count n_ι of
```

New (1 line):

```new
and N_ι = 5,188,959,638,229,843,970,554,286,700 < 5.18896·10²⁷. In particular the count n_ι of
```

#### U17. 71-explicit-constants.md, lines 2722–2725 with P-D0 (HEAD 2714–2717)

Place: lem:uc-n-iota, proof: the evaluation.

Old (4 lines):

```old
(k̄_0 + 1)N_Λ + J′N_Λ(N_Λ + 1)/2, which increases with N_Λ; at N_Λ = N̄_Λ = 909,507,124,095,312, where N̄_Λ/2 =
454,753,562,047,656, it equals

    4 · 909,507,124,095,312 + 765,000,816 · 454,753,562,047,656 · 909,507,124,095,313 = N_ι.
```

New (4 lines):

```new
(k̄_0 + 1)N_Λ + J′N_Λ(N_Λ + 1)/2, which increases with N_Λ; at N_Λ = N̄_Λ = 3,683,190,611, where (N̄_Λ + 1)/2 =
1,841,595,306, it equals

    4 · 3,683,190,611 + 765,000,816 · 3,683,190,611 · 1,841,595,306 = N_ι.
```

#### U18. 71-explicit-constants.md, lines 2734–2777 with P-D0 (HEAD 2726–2769)

Place: prop:uc-explicit, from the second paragraph of the statement to the end of the proof.

Old (44 lines):

```old
Then at most L_< of the levels β_1, …, β_K lie in (2, 3) and at most L_> in (3, α], so that K ≤ L_< + L_>; the number N_b
of [[lem:ec-counts]] (f) satisfies N_b < R_b; and L_< = 59,831,791,007,643,518, L_> = 59,831,791,007,643,520 and R_b =
59,831,791,007,643,520. In [[lem:ec-counts]], [[eq:ec-upper-counts]] and [[eq:uc-t2-w]],

    N_<, N_>, N_b < 5.98318·10¹⁶,   T_<, T_> < 2.04842·10²⁶,   T_2 < 1.79496·10²³,   W < 1,470,302.27,    {#eq:uc-counts}

and every window loop has at most 1,470,302 windows. The first line of [[eq:ec-upper]], with ℓ⁺_tf = 1, r_ι ≤ 16 and the
T_2 and W of [[eq:uc-t2-w]], is less than D_e := 1.23382·10²⁷; of it, the window loops at ι⁺ contribute less than
4.22261·10²⁴.

*Proof.* *The levels.* By [[eq:uc-deltas]], Δβ_0 = 0.999²ε_K = 1.6713522747·10⁻¹⁷ = 16,713,522,747·10⁻²⁷, and

    16,713,522,747 · 59,831,791,007,643,518 = 999,999,999,999,999,988,960,103,946,
    16,713,522,747 · 59,831,791,007,643,519 = 1,000,000,000,000,000,005,673,626,693,
    16,713,522,747 · 59,831,791,007,643,520 = 1,000,000,000,000,000,022,387,149,440,

while 10²⁷(1 + ε_K) = 1,000,000,000,000,000,016,747,000,000; so ⌊1/Δβ_0⌋ = 59,831,791,007,643,518 and ⌊(1 + ε_K)/Δβ_0⌋ =
59,831,791,007,643,519. By [[lem:ec-counts]] (a), at most N_< = (3 − α_1)/Δβ ≤ 1/Δβ_0 of the levels lie in (2, 3), as
α_1 > 2 and Δβ ≥ Δβ_0 ([[lem:uc-admissible]]), and at most N_> = (α − 3)/Δβ + 1 ≤ (1 + ε_K)/Δβ_0 + 1 in (3, α], as α ≤
4 + ε_K; these numbers of levels are integers, so they are at most L_< and L_>. Every level exceeds α_1 > 2 and none
equals 3, so K ≤ L_< + L_>. By [[eq:ec-upper-counts]], N_b ≤ 1/Δβ_0 + 1 < L_< + 2 = R_b.

*The counts.* By [[eq:uc-deltas]] and the lower bound for 𝔡₁ of [[lem:is-offsets]] (b),

    1/Δβ_0 < 5.9831792·10¹⁶,     1/Δτ_0 < 6.847261·10⁹,     1/(2Δβ_0Δτ_0) < 2.0484193·10²⁶,
    1/𝔡₁ < 3.0000026·10⁶,     0.4901/𝔡₁ < 1,470,301.27,

each by multiplying out (for instance 1.6713522747 · 5.9831792 > 10, and 3.333330462964850822194855 · 1.47030127 >
4.901). By [[eq:ec-upper-counts]], N_< ≤ 1/Δβ_0, and N_>, N_b ≤ (1 + ε_K)/Δβ_0 + 1 < 1/Δβ_0 + 3, as ε_K/Δβ_0 = 1/0.998001
< 2; so all three are less than 5.98318·10¹⁶. As (1 + Δβ_0/2)² < 1 + 2·10⁻¹⁷, (1 + ε_K + Δβ_0/2)² < 1 + 6·10⁻¹⁷, 1/Δβ_0 <
6·10¹⁶ and 2(1 + ε_K)/Δβ_0 + 2 < 1.3·10¹⁷,

    T_< < 2.0484193·10²⁶ · (1 + 2·10⁻¹⁷) + 6·10¹⁶ < 2.04842·10²⁶,
    T_> < 2.0484193·10²⁶ · (1 + 6·10⁻¹⁷) + 1.3·10¹⁷ < 2.04842·10²⁶.

As η_2 − η_1 < ε_+ < 10⁻¹³, (1 + η_2 − η_1)/𝔡₁ + 2 < (1 + 10⁻¹³) · 3.0000026·10⁶ + 2 < 3.000005·10⁶, and so T_2 <
5.98318·10¹⁶ · 3.000005·10⁶ < 1.79496·10²³. W = 0.4901/𝔡₁ + 1 < 1,470,302.27, and the number of windows of a loop, an
integer at most W ([[lem:uc-gaps]]), is at most 1,470,302. In the first line of [[eq:ec-upper]], 1/Δτ ≤ 1/Δτ_0, so
4(1/Δτ + 2) < 4(6.847261·10⁹ + 2) < 2.74·10¹⁰; N_< + N_> + N_b + 3 < 3 · 5.98318·10¹⁶ + 3 < 1.794955·10¹⁷, so r_ιW(N_< +
N_> + N_b + 3) < 16 · 1,470,302.27 · 1.794955·10¹⁷ < 4.22261·10²⁴, and so is the contribution of the window loops, each
of at most 1,470,302 windows. Hence the first line is less than

    3 · (2 · 2.04842·10²⁶ + 1.79496·10²³) + 2.74·10¹⁰ + 4.22261·10²⁴
        < 1.2295905·10²⁷ + 4.22261·10²⁴ + 2.74·10¹⁰ < 1.23382·10²⁷. ∎
```

New (44 lines):

```new
Then at most L_< of the levels β_1, …, β_K lie in (2, 3) and at most L_> in (3, α], so that K ≤ L_< + L_>; the number N_b
of [[lem:ec-counts]] (f) satisfies N_b < R_b; and L_< = 6,868,208,951, L_> = 6,868,208,953 and R_b = 6,868,208,953. In
[[lem:ec-counts]], [[eq:ec-upper-counts]] and [[eq:uc-t2-w]],

    N_<, N_>, N_b < 6.86821·10⁹,   T_<, T_> < 2.35143·10¹⁹,   T_2 < 2.06047·10¹⁶,   W < 1,470,302.27,    {#eq:uc-counts}

and every window loop has at most 1,470,302 windows. The first line of [[eq:ec-upper]], with ℓ⁺_tf = 1, r_ι ≤ 16 and the
T_2 and W of [[eq:uc-t2-w]], is less than D_e := 1.41633·10²⁰; of it, the window loops at ι⁺ contribute less than
4.84721·10¹⁷.

*Proof.* *The levels.* By [[eq:uc-deltas]], Δβ_0 = 0.999²ε_K = 1.4559836589·10⁻¹⁰ = 14,559,836,589·10⁻²⁰, and

    14,559,836,589 · 6,868,208,951 = 99,999,999,985,667,108,139,
    14,559,836,589 · 6,868,208,952 = 100,000,000,000,226,944,728,
    14,559,836,589 · 6,868,208,953 = 100,000,000,014,786,781,317,

while 10²⁰(1 + ε_K) = 100,000,000,014,589,000,000; so ⌊1/Δβ_0⌋ = 6,868,208,951 and ⌊(1 + ε_K)/Δβ_0⌋ = 6,868,208,952. By
[[lem:ec-counts]] (a), at most N_< = (3 − α_1)/Δβ ≤ 1/Δβ_0 of the levels lie in (2, 3), as α_1 > 2 and Δβ ≥ Δβ_0
([[lem:uc-admissible]]), and at most N_> = (α − 3)/Δβ + 1 ≤ (1 + ε_K)/Δβ_0 + 1 in (3, α], as α ≤ 4 + ε_K; these numbers
of levels are integers, so they are at most L_< and L_>. Every level exceeds α_1 > 2 and none equals 3, so K ≤ L_< + L_>.
By [[eq:ec-upper-counts]], N_b ≤ 1/Δβ_0 + 1 < L_< + 2 = R_b.

*The counts.* By [[eq:uc-deltas]] and the lower bound for 𝔡₁ of [[lem:is-offsets]] (b),

    1/Δβ_0 < 6.868209·10⁹,     1/Δτ_0 < 6.847261·10⁹,     1/(2Δβ_0Δτ_0) < 2.3514208·10¹⁹,
    1/𝔡₁ < 3.0000026·10⁶,     0.4901/𝔡₁ < 1,470,301.27,

each by multiplying out (for instance 1.4559836589 · 6.868209 > 10, and 3.333330462964850822194855 · 1.47030127 > 4.901).
By [[eq:ec-upper-counts]], N_< ≤ 1/Δβ_0, and N_>, N_b ≤ (1 + ε_K)/Δβ_0 + 1 < 1/Δβ_0 + 3, as ε_K/Δβ_0 = 1/0.998001 < 2; so
all three are less than 6.86821·10⁹. As (1 + Δβ_0/2)² < 1 + 1.5·10⁻¹⁰, (1 + ε_K + Δβ_0/2)² < 1 + 4.4·10⁻¹⁰, 1/Δβ_0 <
6.87·10⁹ and 2(1 + ε_K)/Δβ_0 + 2 < 1.374·10¹⁰,

    T_< < 2.3514208·10¹⁹ · (1 + 1.5·10⁻¹⁰) + 6.87·10⁹ < 2.35143·10¹⁹,
    T_> < 2.3514208·10¹⁹ · (1 + 4.4·10⁻¹⁰) + 1.374·10¹⁰ < 2.35143·10¹⁹.

As η_2 − η_1 < ε_+ < 10⁻⁹, (1 + η_2 − η_1)/𝔡₁ + 2 < (1 + 10⁻⁹) · 3.0000026·10⁶ + 2 < 3.000005·10⁶, and so T_2 <
6.86821·10⁹ · 3.000005·10⁶ < 2.06047·10¹⁶. W = 0.4901/𝔡₁ + 1 < 1,470,302.27, and the number of windows of a loop, an
integer at most W ([[lem:uc-gaps]]), is at most 1,470,302. In the first line of [[eq:ec-upper]], 1/Δτ ≤ 1/Δτ_0, so
4(1/Δτ + 2) < 4(6.847261·10⁹ + 2) < 2.74·10¹⁰; N_< + N_> + N_b + 3 < 3 · 6.86821·10⁹ + 3 < 2.060464·10¹⁰, so r_ιW(N_< +
N_> + N_b + 3) < 16 · 1,470,302.27 · 2.060464·10¹⁰ < 4.84721·10¹⁷, and so is the contribution of the window loops, each
of at most 1,470,302 windows. Hence the first line is less than

    3 · (2 · 2.35143·10¹⁹ + 2.06047·10¹⁶) + 2.74·10¹⁰ + 4.84721·10¹⁷
        < 1.4114762·10²⁰ + 4.84721·10¹⁷ + 2.74·10¹⁰ < 1.41633·10²⁰. ∎
```

#### U19. 71-explicit-constants.md, lines 2798–2831 with P-D0 (HEAD 2790–2823)

Place: thm:uc-integer, the whole theorem and its proof.

Old (34 lines):

```old
**Theorem {#thm:uc-integer}** (The loss d at the computational point.) At the computational point, with the index sets as
constructed, the admissible choice of the weights of [[def:uc-choice]] and the free orders and inner products of
[[def:cs-choices]], let c_* be the largest of the numbers c(β_k) (1 ≤ k ≤ K), c_b, c′_b and c_0 defined before
[[prop:ec-upper]] and c^Ψ(β_k), c^Ψ_b, c′^Ψ_b and c^Ψ_0 of [[lem:uc-dr]]: the largest loss that [[def:ec-accounted-loss]]
assigns to a single step outside the long iterations. Then c_* ≤ C_* < 1.89844·10³⁹ ([[prop:cs-cstar]]); at a level β ∈
(3, α], 1 + n_ι ≤ c(β) ≤ C_lev = 2N_ι + N̄_Λ + 529 < 6.32812·10³⁸, with N_ι of [[eq:uc-n-iota]] and N̄_Λ of
[[lem:uc-lambda]] ([[lem:cs-levels]]); and

    d_acc ≤ d_R ≤ D_acc,     d_NM ≤ D_NM,     N_NM = 21d_NM + 6 ≤ 21D_NM + 6,            {#eq:uc-integer}

where D_acc := D_♭ of [[eq:cs-sharp]] and D_NM := D_♭ + D′_* + d̄_Φ, with D′_* of [[rem:uc-small-reading]] and d̄_Φ of
[[lem:uc-lambda]] (d):

    D_acc = 37,862,223,260,395,633,917,123,246,147,912,828,863,693,156,076,559,963,974 < 3.78623·10⁵⁵,
    D_NM = 75,724,446,520,791,266,568,624,181,582,042,570,869,522,603,615,666,426,111 < 7.57245·10⁵⁵,
    21D_NM + 6 = 1,590,213,376,936,616,597,941,107,813,222,893,988,259,974,675,928,994,948,337 < 1.59022·10⁵⁷.

For the fixed seminorms of [[lem:uc-small-orders]] (d) also d_NM ≤ D_acc + D_* + d̄_Φ < 3.78623·10⁵⁵ ([[prop:uc-d-small]]
(b)). The losses of [[lem:iii-k-2-2]] and [[prop:iii-j2-4-3]] satisfy d_Ψ, d_FM ≤ 62N̄_Λ + 10 = 56,389,441,693,909,354.
Against these, for every admissible choice of the weights,

    d_NM ≥ d_acc ≥ 3R > 1.2250·10²⁷,     N_NM > 2.5725·10²⁸,                               {#eq:uc-lower}

and at the choice of [[def:uc-choice]], 3R > 1.2251·10²⁷, so that D_e < 1.0072 · 3R.

*Proof.* By [[prop:cs-cstar]], c_* ≤ C_*. The bounds at the levels above 3 are [[lem:uc-fourier-count]] and
[[lem:cs-levels]] (b). By [[lem:cs-sharp]], d_acc ≤ D_♭ = D_acc and d_R ≤ D_acc, and d_R ≥ d_acc ([[thm:loss-d]]). By
[[prop:uc-d-small]] (c) and (d), d_NM ≤ D_♭ + D′_* + d̄_Φ = D_NM for the fixed seminorms of [[lem:uc-small-orders]] (d)
and for those of [[rem:uc-small-reading]], and (b) there gives the bound with D_*; the integers are those of
[[eq:cs-sharp]] and [[prop:uc-d-small]] (c). N_NM = 21d_NM + 6 by [[thm:loss-d]], so N_NM ≤ 21D_NM + 6. The bounds for
d_FM and d_Ψ are [[lem:uc-lambda]] (d). [[eq:uc-lower]] is [[cor:is-lower]]. At the choice of [[def:uc-choice]],
[[prop:ec-rounds]] gives R > (1 − 3ε_K − 2δ̂ − δ̄)/(ε_Kδ̂), where 3ε_K + 2δ̂ + δ̄ < 1.98·10⁻⁸ and ε_Kδ̂ =
2.448645858·10⁻²⁷ < 2.44865·10⁻²⁷; so 3R > 3(1 − 1.98·10⁻⁸)/(2.44865·10⁻²⁷) > 1.2251·10²⁷, and 1.0072 · 1.2251·10²⁷ >
1.23382·10²⁷ = D_e. ∎
```

New (35 lines):

```new
**Theorem {#thm:uc-integer}** (The loss d at the computational point.) At the computational point, with the index sets of
[[def:uc-choice]], the admissible choice of the weights there and the free orders and inner products of
[[def:cs-choices]], let c_* be the largest of the numbers c(β_k) (1 ≤ k ≤ K), c_b, c′_b and c_0 defined before
[[prop:ec-upper]] and c^Ψ(β_k), c^Ψ_b, c′^Ψ_b and c^Ψ_0 of [[lem:uc-dr]]: the largest loss that [[def:ec-accounted-loss]]
assigns to a single step outside the long iterations. Then c_* ≤ C_* < 3.11338·10²⁸ ([[prop:cs-cstar]]); at a level β ∈
(3, α], 1 + n_ι ≤ c(β) ≤ C_lev = 2N_ι + N̄_Λ + 529 < 1.0378·10²⁸, with N_ι of [[eq:uc-n-iota]] and N̄_Λ of
[[lem:uc-lambda]] ([[lem:cs-levels]]); and

    d_acc ≤ d_R ≤ D_acc,     d_NM ≤ D_NM,     N_NM = 21d_NM + 6 ≤ 21D_NM + 6,            {#eq:uc-integer}

where D_acc := D_♭ of [[eq:cs-sharp]] and D_NM := D_♭ + D′_* + d̄_Φ, with D′_* of [[rem:uc-small-reading]] and d̄_Φ of
[[lem:uc-lambda]] (d):

    D_acc = 71,277,718,119,225,469,720,805,142,747,913,308,950 < 7.12778·10³⁷,
    D_NM = 142,555,436,217,695,100,271,475,851,685,218,689,090 < 1.42556·10³⁸,
    21D_NM + 6 = 2,993,664,160,571,597,105,700,992,885,389,592,470,896 < 2.99367·10³⁹.

For the fixed seminorms of [[lem:uc-small-orders]] (d) also d_NM ≤ D_acc + D_* + d̄_Φ < 7.12778·10³⁷ ([[prop:uc-d-small]]
(b)). The losses of [[lem:iii-k-2-2]] and [[prop:iii-j2-4-3]] satisfy d_Ψ, d_FM ≤ 62N̄_Λ + 10 = 228,357,817,892. Against
these, every admissible choice of the weights gives d_NM ≥ d_acc > 1.403·10²⁰ ([[thm:loss-d]] (ii)), and, for the index
sets as constructed ([[cor:is-lower]]),

    d_NM ≥ d_acc ≥ 3R > 1.2250·10²⁷,     N_NM > 2.5725·10²⁸,                               {#eq:uc-lower}

while at the choice of [[def:uc-choice]], 3R > 1.40639·10²⁰, so that D_e < 1.0071 · 3R.

*Proof.* By [[prop:cs-cstar]], c_* ≤ C_*. The bounds at the levels above 3 are [[lem:uc-fourier-count]] and
[[lem:cs-levels]] (b). By [[lem:cs-sharp]], d_acc ≤ D_♭ = D_acc and d_R ≤ D_acc, and d_R ≥ d_acc ([[thm:loss-d]]). By
[[prop:uc-d-small]] (c) and (d), d_NM ≤ D_♭ + D′_* + d̄_Φ = D_NM for the fixed seminorms of [[lem:uc-small-orders]] (d)
and for those of [[rem:uc-small-reading]], and (b) there gives the bound with D_*; the integers are those of
[[eq:cs-sharp]] and [[prop:uc-d-small]] (c). N_NM = 21d_NM + 6 by [[thm:loss-d]], so N_NM ≤ 21D_NM + 6. The bounds for
d_FM and d_Ψ are [[lem:uc-lambda]] (d). The bound 1.403·10²⁰ is [[thm:loss-d]] (ii), and [[eq:uc-lower]] is
[[cor:is-lower]]. At the choice of [[def:uc-choice]], [[prop:ec-rounds]] gives R > (1 − 3ε_K − 2δ̂ − δ̄)/(ε_Kδ̂), where
3ε_K + 2δ̂ + δ̄ < 2.015·10⁻⁸ and ε_Kδ̂ = 2.133116046·10⁻²⁰ < 2.13312·10⁻²⁰; so 3R > 3(1 − 2.015·10⁻⁸)/(2.13312·10⁻²⁰) >
1.40639·10²⁰, and 1.0071 · 1.40639·10²⁰ > 1.41633·10²⁰ = D_e. ∎
```

#### U20. 71-explicit-constants.md, lines 2833–2871 with P-D0 (HEAD 2825–2863)

Place: prop:uc-dependence, the whole proposition and its proof.

Old (39 lines):

```old
**Proposition {#prop:uc-dependence}** (The bound as a function of the choice.) Let a choice be made as in
[[def:uc-choice]], except that ε_K and ε_+ are any numbers with 0 < ε_K < ε_+ < 10⁻¹³ for which it is admissible and the
hypotheses of [[prop:ec-upper]] and of [[eq:ec-upper-counts]] hold with Δβ_0 := 0.999²ε_K and Δτ_0 := 0.999ε_Υ, as
[[lem:uc-admissible]] shows at the choice of [[def:uc-choice]], and let N̄_Λ ≥ N_Λ, k̄_0, J_* and l_* be integers with
which [[lem:uc-lambda]] (c) holds, with J′ := (J_* + 1)(l_* + 1). Put L_<, L_> and R_b as in [[eq:uc-levels]], N_ι as in
[[eq:uc-n-iota]], k̄_max := k̄_0 + J′N̄_Λ, d̄_Φ := 62N̄_Λ + 2, C_lev := 2N_ι + N̄_Λ + 529, I_lev := 34,268,829,852,
I_base := 935R_b + 466 + 23,524,832(R_b + 3), T_12 := C_lev + I_lev + 4k̄_max + 24, R_base := 22,097 + I_base,

    F_1 := 3((1 + Δβ_0/2)² + (1 + ε_K + Δβ_0/2)²)/(2Δβ_0Δτ_0) + 3(3 + 2ε_K)/Δβ_0 + 6 + 4/Δτ_0 + 8
           + 3((1 + ε_K)/Δβ_0 + 1)((1 + ε_+)/𝔡₁ + 2) + 16(0.4901/𝔡₁ + 1)((3 + ε_K)/Δβ_0 + 5),
    C_* := 6N_ι + 3N̄_Λ + 3I_lev + 8k̄_max + I_base + d̄_Φ + (N̄_Λ + 2)(d̄_Φ + 30) + 45,862,
    D′_* := T_12 + 18 + 20,565,308,337L_< + (C_lev + I_lev − 9)L_> + 2R_base,
    D_acc := D_e + 497L_< + L_>C_lev + 935R_b + 466 + C_*,     D_NM := D_acc + D′_* + d̄_Φ,

with D_e any number at least F_1, and suppose that 4k̄_max + 24 > I_base + 22,119. Then d_acc ≤ d_R ≤ D_acc, d_NM ≤ D_NM
and N_NM ≤ 21D_NM + 6. Each of N_ι, k̄_max, d̄_Φ, C_lev, I_base, T_12, R_base, C_*, D′_* and D_acc − D_e is a polynomial
with non-negative coefficients in N̄_Λ, k̄_0, J′, L_<, L_> and R_b; L_<, L_> and R_b are non-increasing in ε_K, and F_1
is non-increasing in ε_K and non-decreasing in ε_+. So, with D_e := F_1, D_acc and D_NM are non-decreasing in N̄_Λ, k̄_0,
J′ and ε_+ and non-increasing in ε_K. Moreover D_acc = L_>C_lev + D_e + 497L_< + 935R_b + 466 + C_*, and L_>C_lev >
J′N̄_Λ(N̄_Λ + 1)(1 + ε_K)/Δβ_0: the bound is at least quadratic in N̄_Λ and of the order 1/ε_K.

*Proof.* The proofs of [[prop:uc-explicit]], [[lem:cs-levels]], [[lem:cs-base]], [[lem:cs-iterations]], [[lem:cs-rest]],
[[prop:cs-cstar]], [[lem:cs-sharp]], [[lem:uc-small-orders]], [[rem:uc-small-reading]] and [[prop:uc-d-small]] use, of
the numbers of [[def:uc-choice]] and [[lem:uc-lambda]], only N_Λ ≤ N̄_Λ, k̄(λ_i) ≤ k̄_0 + J′i, Δβ ≥ Δβ_0, a♭_K − 2 ≥
Δβ_0, Δτ ≥ Δτ_0, ε_K < ε_+ < 10⁻¹³ and the bounds of [[lem:is-offsets]] (b), and, in Steps 4′ and 4 of
[[lem:uc-small-orders]] (d) and in [[rem:uc-small-reading]], T_11 < T_12 ([[lem:cs-rest]]), which is the inequality
supposed. With it every order of the smallness conditions is at most max(2R_base + 16, T_12 + 14, C_lev + I_lev +
R_base + 5) ≤ D′_* for the fixed seminorms of [[lem:uc-small-orders]] (d) (the proof of its (e)), and at most D′_* for
those of [[rem:uc-small-reading]]; so they give d_acc, d_R ≤ D_acc and d_NM ≤ D_NM with the expressions above. F_1 is the
bound for the first line of [[eq:ec-upper]] that [[eq:ec-upper-counts]], [[eq:uc-t2-w]], ℓ⁺_tf = 1, r_ι ≤ 16 and η_2 −
η_1 < ε_+ give, with N_< ≤ 1/Δβ_0, N_> ≤ (1 + ε_K)/Δβ_0 + 1 and N_b ≤ 1/Δβ_0 + 1 ([[eq:ec-upper-counts]]): 3(T_< + T_> +
T_2) + 4(1/Δτ + 2) + 16W(N_< + N_> + N_b + 3), 1/Δτ ≤ 1/Δτ_0, written out; 1/𝔡₁ may be replaced by any upper bound. C_*
is the right side of [[eq:cs-c0]] written out (1,587 + 44,227 + 48 = 45,862 and 2X_12 = 8k̄_max + 48), I_base is that of
[[eq:cs-iterations]] (469R_b + 466(R_b + 1) = 935R_b + 466 and 16 · 1,470,302 = 23,524,832), and 22,097 = 20,183 + 1,914.
These are sums of products of N̄_Λ, k̄_0, J′, L_<, L_>, R_b and positive constants, so they do not decrease when one of
these integers increases. As ε_K increases, Δβ_0 increases, and 1/Δβ_0 and (1 + ε_K)/Δβ_0 = 1/Δβ_0 + 1/0.998001 decrease,
and so do their integer parts; each term of F_1 is non-increasing in ε_K, as x ↦ (1 + cx)²/x decreases on (0, 1/c) and
(1 + ε_K)/Δβ_0 and (3 + ε_K)/Δβ_0 decrease, and ε_+ enters F_1 only through the factor 1 + ε_+. Finally C_lev > 2N_ι ≥
J′N̄_Λ(N̄_Λ + 1) and L_> > (1 + ε_K)/Δβ_0. ∎
```

New (56 lines):

```new
**Proposition {#prop:uc-dependence}** (The bound as a function of the choice.) Let a choice be made as in
[[def:uc-choice]], with the index sets there or with the index sets as constructed ([[sec:is]]), except that ε_K and
ε_+ are any numbers with 0 < ε_K < ε_+ and ε_K < 0.998ε_Υ for which it is admissible and the hypotheses of
[[prop:ec-upper]] and of [[eq:ec-upper-counts]] hold with Δβ_0 := 0.999²ε_K and Δτ_0 := 0.999ε_Υ, as
[[lem:uc-admissible]] shows at the choice of [[def:uc-choice]], and let N̄_Λ ≥ N_Λ, k̄_0, J_* and l_* be integers with
which [[lem:uc-lambda]] (c) holds, with J′ := (J_* + 1)(l_* + 1). Put L_<, L_> and R_b as in [[eq:uc-levels]], N_ι as in
[[eq:uc-n-iota]], k̄_max := k̄_0 + J′N̄_Λ, d̄_Φ := 62N̄_Λ + 2, C_lev := 2N_ι + N̄_Λ + 529, I_lev := 34,268,829,852,
I_base := 935R_b + 466 + 23,524,832(R_b + 3), R_base := 22,097 + I_base, T_11 := C_lev + I_lev + R_base + 22, T_12 :=
C_lev + I_lev + 4k̄_max + 24,

    F_1 := 3((1 + Δβ_0/2)² + (1 + ε_K + Δβ_0/2)²)/(2Δβ_0Δτ_0) + 3(3 + 2ε_K)/Δβ_0 + 6 + 4/Δτ_0 + 8
           + 3((1 + ε_K)/Δβ_0 + 1)((1 + ε_+)/𝔡₁ + 2) + 16(0.4901/𝔡₁ + 1)((3 + ε_K)/Δβ_0 + 5),
    C_* := 6N_ι + 3N̄_Λ + 3I_lev + 8k̄_max + I_base + d̄_Φ + (N̄_Λ + 2)(d̄_Φ + 30) + 45,862,
    D′_* := max(T_11, T_12) + 18 + 20,565,308,337L_< + (C_lev + I_lev − 9)L_> + 2R_base,
    D_acc := D_e + 497L_< + L_>C_lev + 935R_b + 466 + C_*,     D_NM := D_acc + D′_* + d̄_Φ,

with D_e any number at least F_1. Then d_acc ≤ d_R ≤ D_acc, d_NM ≤ D_NM and N_NM ≤ 21D_NM + 6. If T_11 < T_12, that is,
if 4k̄_max + 24 > I_base + 22,119, then D′_* is the number of [[rem:uc-small-reading]] for these inputs; at the choice of
[[def:uc-choice]] the inequality holds ([[lem:uc-small-orders]] (e)), and, with D_e of [[prop:uc-explicit]], D_acc, D′_*
and D_NM are the integers of [[thm:uc-integer]]. Each of N_ι, k̄_max, d̄_Φ, C_lev, I_base, R_base, T_11, T_12, C_* and
D_acc − D_e is a polynomial with non-negative coefficients in N̄_Λ, k̄_0, J′, L_<, L_> and R_b, and so is D′_* with
max(T_11, T_12) replaced by either of T_11 and T_12; L_<, L_> and R_b are non-increasing in ε_K, and F_1 is
non-increasing in ε_K and non-decreasing in ε_+. So, with D_e := F_1, D_acc and D_NM are non-decreasing in N̄_Λ, k̄_0, J′
and ε_+ and non-increasing in ε_K. Moreover D_acc = L_>C_lev + D_e + 497L_< + 935R_b + 466 + C_*, and L_>C_lev >
J′N̄_Λ(N̄_Λ + 1)(1 + ε_K)/Δβ_0: the bound is at least quadratic in N̄_Λ and of the order 1/ε_K.

*Proof.* The proofs of [[prop:uc-explicit]], [[lem:cs-levels]], [[lem:cs-base]], [[lem:cs-iterations]], [[lem:cs-rest]],
[[prop:cs-cstar]], [[lem:cs-sharp]], [[lem:uc-small-orders]], [[rem:uc-small-reading]] and [[prop:uc-d-small]] use, of
the index sets, only the least ℰ^C_I, which is the same for both choices ([[prop:is-ci-pp]] (a)), min Re ℰ_ind = min Re
ℰ^ι_ind = η_0 = 𝔡₁, which holds for both choices ([[lem:uc-gaps]]), and, in [[lem:cs-fourier]] (b), the reality of the
elements of Λ of real part at most 2.514, which holds for both ([[prop:is-lambda]], and Λ^φ ⊂ Λ by
[[thm:is-flat-serves]]). Of the numbers of [[def:uc-choice]] and [[lem:uc-lambda]] they use only N_Λ ≤ N̄_Λ, k̄(λ_i) ≤
k̄_0 + J′i, Δβ ≥ Δβ_0, a♭_K − 2 ≥ Δβ_0, Δτ ≥ Δτ_0, ε_K < ε_+, the bounds of [[lem:is-offsets]] (b), and three facts,
which hold here. (1) η_2 − η_1 < ε_+ < 10⁻⁷, for the bounds (1 + η_2 − η_1)/𝔡₁ + 2 < 3.000005·10⁶ of [[prop:uc-explicit]]
and 3,000,004 of [[lem:cs-iterations]]: admissibility gives ε_+ < ε_ind ≤ δ_50 < δ̄ < 10⁻⁷ ([[eq:iii-i9-1-1]],
[[prop:np-10-52]] (iii), [[def:ec-point]]), and (1 + 10⁻⁷) · 3.0000026·10⁶ + 2 < 3.000005·10⁶. (2) ε_K + ε < ε_g, for
the δ₄ of Step 4 of the proof of [[prop:iii-i11-3-1]] ([[lem:uc-admissible]]), and ε_K < ε_g − 2ε, by which the level
steps of the bases of [[lem:cs-rest]] and [[sec:cs-small]] have no transition face round: as ε_g = ε_Υ and ε ≤ 10⁻³ε_g,
both follow from ε_K < 0.998ε_Υ. (3) In Steps 4′ and 4 of the proof of [[lem:uc-small-orders]] (d) the reads are charged
at most C_lev − 11 + I_lev + X_12 < T_12 and T_11 ([[lem:cs-rest]]), so at most max(T_11, T_12), and a condition read at
a reference point (0, p⃗_b) with b ≠ b₀ has order at most C_lev + I_lev + R_base + 5 < T_11 + 14 (the proof of its (e));
that proof and [[rem:uc-small-reading]] use T_11 < T_12 only to write T_12 for max(T_11, T_12), and without it they hold
with max(T_11, T_12) in place of T_12. So every order of the smallness conditions is at most max(2R_base + 16, max(T_11,
T_12) + 14) for the fixed seminorms of [[lem:uc-small-orders]] (d) (the proof of its (e)), and at most D′_* for those of
[[rem:uc-small-reading]]; both are at most D′_*, and they give d_acc, d_R ≤ D_acc and d_NM ≤ D_NM with the expressions
above. F_1 is the bound for the first line of [[eq:ec-upper]] that [[eq:ec-upper-counts]], [[eq:uc-t2-w]], ℓ⁺_tf = 1, r_ι
≤ 16 and η_2 − η_1 < ε_+ give, with N_< ≤ 1/Δβ_0, N_> ≤ (1 + ε_K)/Δβ_0 + 1 and N_b ≤ 1/Δβ_0 + 1 ([[eq:ec-upper-counts]]):
3(T_< + T_> + T_2) + 4(1/Δτ + 2) + 16W(N_< + N_> + N_b + 3), 1/Δτ ≤ 1/Δτ_0, written out; 1/𝔡₁ may be replaced by any
upper bound. C_* is the right side of [[eq:cs-c0]] written out (1,587 + 44,227 + 48 = 45,862 and 2X_12 = 8k̄_max + 48),
I_base is that of [[eq:cs-iterations]] (469R_b + 466(R_b + 1) = 935R_b + 466 and 16 · 1,470,302 = 23,524,832), 22,097 =
20,183 + 1,914, and T_11 and T_12 are those of [[lem:cs-rest]]. These are sums of products of N̄_Λ, k̄_0, J′, L_<, L_>,
R_b and positive constants, so they do not decrease when one of these integers increases, and neither does the larger of
two of them. As ε_K increases, Δβ_0 increases, and 1/Δβ_0 and (1 + ε_K)/Δβ_0 = 1/Δβ_0 + 1/0.998001 decrease, and so do
their integer parts; each term of F_1 is non-increasing in ε_K, as x ↦ (1 + cx)²/x decreases on (0, 1/c) and (1 +
ε_K)/Δβ_0 and (3 + ε_K)/Δβ_0 decrease, and ε_+ enters F_1 only through the factor 1 + ε_+. Finally C_lev > 2N_ι ≥
J′N̄_Λ(N̄_Λ + 1) and L_> > (1 + ε_K)/Δβ_0. ∎
```

#### U21. 71-explicit-constants.md, lines 2894–2895 with P-D0 (HEAD 2886–2887)

Place: rem:uc-missing, second paragraph.

Old (2 lines):

```old
([[lem:cs-fourier]]). So the levels above 3 carry the bound: at most L_> = 59,831,791,007,643,520 of them, each charged
at most C_lev < 6.32812·10³⁸, make all of D_acc but less than 1.9·10³⁹ ([[lem:cs-sharp]]), far above D_e. C_lev counts
```

New (2 lines):

```new
([[lem:cs-fourier]]). So the levels above 3 carry the bound: at most L_> = 6,868,208,953 of them, each charged at most
C_lev < 1.0378·10²⁸, make all of D_acc but less than 3.12·10²⁸ ([[lem:cs-sharp]]), far above D_e. C_lev counts
```

#### U22. 71-explicit-constants.md, lines 3583 with P-D0 (HEAD 3572)

Place: cor:is-lower, statement: the clause on the former choice ε_K = 1.6747·10⁻¹⁷ removed.

Old (1 line):

```old
N_NM = 21d_NM + 6 > 2.5725·10²⁸; at ε_K = 1.6747·10⁻¹⁷, 3R > 1.2251·10²⁷.
```

New (1 line):

```new
N_NM = 21d_NM + 6 > 2.5725·10²⁸.
```

#### U22b. 71-explicit-constants.md, lines 3589–3590 with P-D0 (HEAD 3578–3579)

Place: cor:is-lower, proof: the sentence on the former choice ε_K = 1.6747·10⁻¹⁷ removed.

Old (2 lines):

```old
(ii), d_NM ≥ d_acc ≥ 3R > 1.2250·10²⁷, so N_NM > 21 · 1.2250·10²⁷ = 2.5725·10²⁸. At ε_K = 1.6747·10⁻¹⁷,
ε_Kδ̂ = 2.448645…·10⁻²⁷ < 2.44865·10⁻²⁷, and 3(1 − 1.98·10⁻⁸)/(2.44865·10⁻²⁷) > 1.2251·10²⁷. ∎
```

New (1 line):

```new
(ii), d_NM ≥ d_acc ≥ 3R > 1.2250·10²⁷, so N_NM > 21 · 1.2250·10²⁷ = 2.5725·10²⁸. ∎
```

#### U23. 71-explicit-constants.md, lines 4603–4604 with P-D0 (HEAD 4390–4391)

Place: sec:cs, the opening paragraph.

Old (2 lines):

```old
N̄_Λ + 529 ([[lem:cs-levels]], [[lem:cs-base]]), and c_0, whose bound counts three runs of the top level, less than
6N_ι + 5.13·10³¹ ([[lem:cs-rest]]). So c_* ≤ C_* < 1.89844·10³⁹ ([[prop:cs-cstar]]), and the levels above 3 give the
```

New (2 lines):

```new
N̄_Λ + 529 ([[lem:cs-levels]], [[lem:cs-base]]), and c_0, whose bound counts three runs of the top level, less than
6N_ι + 8.64·10²⁰ ([[lem:cs-rest]]). So c_* ≤ C_* < 3.11338·10²⁸ ([[prop:cs-cstar]]), and the levels above 3 give the
```

#### U24. 71-explicit-constants.md, lines 4916 with P-D0 (HEAD 4703)

Place: lem:cs-levels, the display eq:cs-clev.

Old (1 line):

```old
    c(β_k) ≤ C_lev := 2N_ι + N̄_Λ + 529 = 632,811,129,714,614,885,796,976,268,758,886,545,633.    {#eq:cs-clev}
```

New (1 line):

```new
    c(β_k) ≤ C_lev := 2N_ι + N̄_Λ + 529 = 10,377,919,276,459,687,944,791,764,540.           {#eq:cs-clev}
```

#### U25. 71-explicit-constants.md, lines 4990–4991 with P-D0 (HEAD 4777–4778)

Place: lem:cs-iterations, the display eq:cs-iterations.

Old (2 lines):

```old
    I_base := 469 R_b + 466 (R_b + 1) + 16 · 1,470,302 · (R_b + 3)
            = 1,407,588,774,438,516,741,154,802.                                      {#eq:cs-iterations}
```

New (2 lines):

```new
    I_base := 469 R_b + 466 (R_b + 1) + 16 · 1,470,302 · (R_b + 3)
            = 161,579,883,606,166,913.                                                {#eq:cs-iterations}
```

#### U26. 71-explicit-constants.md, lines 5073–5074 with P-D0 (HEAD 4860–4861)

Place: lem:cs-rest, proof: the map Φ.

Old (2 lines):

```old
*The map U ↦ Φ(U)* has the loss d_Φ of [[lem:uc-phi-loss]], at most d̄_Φ = 56,389,441,693,909,346 ([[lem:uc-lambda]]
(d)).
```

New (1 line):

```new
*The map U ↦ Φ(U)* has the loss d_Φ of [[lem:uc-phi-loss]], at most d̄_Φ = 228,357,817,884 ([[lem:uc-lambda]] (d)).
```

#### U27. 71-explicit-constants.md, lines 5093–5122 with P-D0 (HEAD 4880–4909)

Place: prop:cs-cstar and rem:cs-sharpness.

Old (30 lines):

```old
**Proposition {#prop:cs-cstar}** (The largest single-step loss.) At the computational point, with the index sets as
constructed and the choices of [[def:uc-choice]] and [[def:cs-choices]],

    c_* ≤ C_* := 6N_ι + 3N̄_Λ + 51,286,605,918,146,275,681,884,678,060,390
             = 1,898,433,440,430,450,575,537,204,488,161,337,695,702 < 1.89844·10³⁹.       {#eq:cs-cstar}

*Proof.* By [[lem:cs-levels]] and [[lem:cs-base]], c(β_k), c^Ψ(β_k) ≤ max(497, C_lev) = C_lev and c_b, c^Ψ_b ≤ 469, c′_b,
c′^Ψ_b ≤ 466. By [[lem:cs-rest]], c_0 and c^Ψ_0 are at most the right side of [[eq:cs-c0]]. With C_lev = 2N_ι + N̄_Λ +
529, this is

    2 · 20,183 + 2 · 1,914 + 33 + 3C_lev + 3I_lev + 2X_12 + I_base + d_Φ + (N̄_Λ + 2)(d_Φ + 30)
        ≤ 6N_ι + 3N̄_Λ + 1,587 + 44,227 + 102,806,489,556 + 5,566,189,536,725,815,534,196,808
          + 1,407,588,774,438,516,741,154,802 + 56,389,441,693,909,346 + 51,286,598,944,367,908,128,007,902,264,064,

with 3I_lev = 102,806,489,556, 2X_12 = 8k̄_max + 48 = 5,566,189,536,725,815,534,196,808, d_Φ ≤ d̄_Φ and (N̄_Λ + 2)(d_Φ +
30) ≤ 909,507,124,095,314 · 56,389,441,693,909,376 = 51,286,598,944,367,908,128,007,902,264,064. The seven numbers after
6N_ι + 3N̄_Λ add up to 51,286,605,918,146,275,681,884,678,060,390, and with 6N_ι =
1,898,433,389,143,844,657,390,926,077,755,287,349,376 and 3N̄_Λ = 2,728,521,372,285,936 the sum is the integer of
[[eq:cs-cstar]]. This bound exceeds C_lev, 469 and 466, so it bounds c_*. ∎

**Remark {#rem:cs-sharpness}** (What the bound counts.) Of the bound of [[eq:cs-cstar]], all but less than 5.13·10³¹ is
6N_ι: two counts of the logarithmic terms of Λ below 3 + ε_+ in each of the three runs of the top level counted in the
bound for c_0, each count being taken at the bound k̄(λ) of [[def:iii-i10-1-1]] for the logarithmic orders. The next
term, (N̄_Λ + 2)(d̄_Φ + 30) < 5.129·10³¹, comes from Step 2 of the proof of [[thm:iii-j1-2-1]], whose chain passes
through every exponent of Λ_* and composes the map Φ at each. A level step above 3 is charged at most C_lev, about C_*/3,
and c_0 enters the second line of [[eq:ec-upper]] once; the at most L_> levels above 3 carry the bound, L_>C_lev being
all of D_acc but less than 1.9·10³⁹ ([[lem:cs-sharp]]). The bound is crude in another way as well: n_ι and n_K count
every pair (λ, k) with k ≤ k̄(λ), while the logarithmic orders that the constructions produce are bounded in this paper
only by k̄(λ). Through N_ι, C_lev is quadratic in N̄_Λ and linear in J′ ([[eq:uc-n-iota]]), and L_> is about
1/(0.998001ε_K) ([[eq:uc-levels]]); [[prop:uc-dependence]] states the dependence.
```

New (29 lines):

```new
**Proposition {#prop:cs-cstar}** (The largest single-step loss.) At the computational point, with the choices of
[[def:uc-choice]] and [[def:cs-choices]],

    c_* ≤ C_* := 6N_ι + 3N̄_Λ + 863,788,102,143,966,870,129
             = 31,133,758,693,167,165,978,342,162,162 < 3.11338·10²⁸.                      {#eq:cs-cstar}

*Proof.* By [[lem:cs-levels]] and [[lem:cs-base]], c(β_k), c^Ψ(β_k) ≤ max(497, C_lev) = C_lev and c_b, c^Ψ_b ≤ 469, c′_b,
c′^Ψ_b ≤ 466. By [[lem:cs-rest]], c_0 and c^Ψ_0 are at most the right side of [[eq:cs-c0]]. With C_lev = 2N_ι + N̄_Λ +
529, this is

    2 · 20,183 + 2 · 1,914 + 33 + 3C_lev + 3I_lev + 2X_12 + I_base + d_Φ + (N̄_Λ + 2)(d_Φ + 30)
        ≤ 6N_ι + 3N̄_Λ + 1,587 + 44,227 + 102,806,489,556 + 22,541,150,583,188,308,680
          + 161,579,883,606,166,913 + 228,357,817,884 + 841,085,371,346,008,041,282,

with 3I_lev = 102,806,489,556, 2X_12 = 8k̄_max + 48 = 22,541,150,583,188,308,680, d_Φ ≤ d̄_Φ and (N̄_Λ + 2)(d_Φ + 30) ≤
3,683,190,613 · 228,357,817,914 = 841,085,371,346,008,041,282. The seven numbers after 6N_ι + 3N̄_Λ add up to
863,788,102,143,966,870,129, and with 6N_ι = 31,133,757,829,379,063,823,325,720,200 and 3N̄_Λ = 11,049,571,833 the sum is
the integer of [[eq:cs-cstar]]. This bound exceeds C_lev, 469 and 466, so it bounds c_*. ∎

**Remark {#rem:cs-sharpness}** (What the bound counts.) Of the bound of [[eq:cs-cstar]], all but less than 8.64·10²⁰ is
6N_ι: two counts of the logarithmic terms of Λ below 3 + ε_+ in each of the three runs of the top level counted in the
bound for c_0, each count being taken at the bound k̄(λ) of [[def:iii-i10-1-1]] for the logarithmic orders. The next
term, (N̄_Λ + 2)(d̄_Φ + 30) < 8.411·10²⁰, comes from Step 2 of the proof of [[thm:iii-j1-2-1]], whose chain passes
through every exponent of Λ_* and composes the map Φ at each. A level step above 3 is charged at most C_lev, about C_*/3,
and c_0 enters the second line of [[eq:ec-upper]] once; the at most L_> levels above 3 carry the bound, L_>C_lev being
all of D_acc but less than 3.12·10²⁸ ([[lem:cs-sharp]]). The bound is crude in another way as well: n_ι and n_K count
every pair (λ, k) with k ≤ k̄(λ), while the logarithmic orders that the constructions produce are bounded in this paper
only by k̄(λ). Through N_ι, C_lev is quadratic in N̄_Λ and linear in J′ ([[eq:uc-n-iota]]), and L_> is about
1/(0.998001ε_K) ([[eq:uc-levels]]); [[prop:uc-dependence]] states the dependence.
```

#### U28. 71-explicit-constants.md, lines 5140 with P-D0 (HEAD 4927)

Place: sec:cs-small, the display of R_base.

Old (1 line):

```old
    R_base := 20,183 + 1,914 + I_base = 1,407,588,774,438,516,741,176,899.
```

New (1 line):

```new
    R_base := 20,183 + 1,914 + I_base = 161,579,883,606,189,010.
```

#### U29. 71-explicit-constants.md, lines 5155–5156 with P-D0 (HEAD 4942–4943)

Place: lem:cs-sharp, the display eq:cs-sharp.

Old (2 lines):

```old
    d_acc ≤ D_♭,     d_R ≤ D_♭,     D_♭ := D_e + 497L_< + L_>C_lev + 469R_b + 466(R_b + 1) + C_*,
    D_♭ = 37,862,223,260,395,633,917,123,246,147,912,828,863,693,156,076,559,963,974 < 3.78623·10⁵⁵.    {#eq:cs-sharp}
```

New (2 lines):

```new
    d_acc ≤ D_♭,     d_R ≤ D_♭,     D_♭ := D_e + 497L_< + L_>C_lev + 469R_b + 466(R_b + 1) + C_*,
    D_♭ = 71,277,718,119,225,469,720,805,142,747,913,308,950 < 7.12778·10³⁷.               {#eq:cs-sharp}
```

#### U30. 71-explicit-constants.md, lines 5168–5172 with P-D0 (HEAD 4955–4959)

Place: lem:cs-sharp, proof: the integer.

Old (5 lines):

```old
*The integer.* L_>C_lev = 37,862,223,260,395,632,018,689,805,716,228,433,240,809,543,192,276,748,160, 497L_< =
29,736,400,130,798,828,446, and 469R_b + 466(R_b + 1) = 28,061,109,982,584,810,880 + 27,881,614,609,561,880,786 =
55,942,724,592,146,691,666. Adding these, D_e = 1,233,820,000,000,000,000,000,000,000 and C_* =
1,898,433,440,430,450,575,537,204,488,161,337,695,702 gives the integer of [[eq:cs-sharp]], whose leading digits are
3.786222. ∎
```

New (3 lines):

```new
*The integer.* L_>C_lev = 71,277,718,088,091,710,886,004,966,934,295,926,620, 497L_< = 3,413,499,848,647, and 469R_b +
466(R_b + 1) = 3,221,189,998,957 + 3,200,585,372,564 = 6,421,775,371,521. Adding these, D_e = 141,633,000,000,000,000,000
and C_* = 31,133,758,693,167,165,978,342,162,162 gives the integer of [[eq:cs-sharp]], with leading digits 7.127771. ∎
```

#### U31. 71-explicit-constants.md, lines 5181–5182 with P-D0 (HEAD 4968–4969)

Place: lem:uc-small-orders, the opening.

Old (2 lines):

```old
**Lemma {#lem:uc-small-orders}** (The orders of the smallness conditions.) At the computational point, with the index
sets as constructed and the choices of [[def:uc-choice]] and [[def:cs-choices]]:
```

New (2 lines):

```new
**Lemma {#lem:uc-small-orders}** (The orders of the smallness conditions.) At the computational point, with the choices
of [[def:uc-choice]] and [[def:cs-choices]]:
```

#### U32. 71-explicit-constants.md, lines 5187 with P-D0 (HEAD 4974)

Place: lem:uc-small-orders (b).

Old (1 line):

```old
(b) in [[eq:s20-d]] one may take k_1 = 10 and k_0 = k̂_0 := 20,602 + 466R_b = 27,881,614,609,561,900,922, and so the d of
```

New (1 line):

```new
(b) in [[eq:s20-d]] one may take k_1 = 10 and k_0 = k̂_0 := 20,602 + 466R_b = 3,200,585,392,700, and so the d of
```

#### U33. 71-explicit-constants.md, lines 5204 with P-D0 (HEAD 4991)

Place: lem:uc-small-orders (e), the display eq:uc-small.

Old (1 line):

```old
    D_* := T_12 + 14 = 632,811,129,714,617,668,891,744,631,700,922,473,903 < 6.32812·10³⁸,    {#eq:uc-small}
```

New (1 line):

```new
    D_* := T_12 + 14 = 10,377,919,287,730,263,270,654,748,746 < 1.0378·10²⁸,               {#eq:uc-small}
```

#### U34. 71-explicit-constants.md, lines 5319–5324 with P-D0 (HEAD 5106–5111)

Place: lem:uc-small-orders, proof of (e): the numbers.

Old (6 lines):

```old
*(e)* The orders of (a)–(c) are at most 2R_base + 16 = 2,815,177,548,877,033,482,353,814, which is less than T_12. Those
of (d) are at most ρ + 14 < T_12 + 14, or ρ + R_base + 16. Of the conditions of (d), one read at a reference point (0,
p⃗_b) with b ≠ b₀ occurs only at a level, where ρ ≤ C_lev − 11 + I_lev: Step 4′ is a step of [[thm:iii-i14-3-1]], at b₀,
and at a rotating b [[prop:iii-i15-2-5]] has no Step 4′ ([[sec:s23-base-points]]), its rotation coordinates being the A_b
read at the levels. So ρ + R_base + 16 ≤ C_lev + I_lev + R_base + 5 < T_12 + 14, as X_12 =
2,783,094,768,362,907,767,098,404 exceeds R_base + 22, so that also T_11 < T_12 in (d). The convention "h small" of
```

New (6 lines):

```new
*(e)* The orders of (a)–(c) are at most 2R_base + 16 = 323,159,767,212,378,036, which is less than T_12. Those of (d) are
at most ρ + 14 < T_12 + 14, or ρ + R_base + 16. Of the conditions of (d), one read at a reference point (0, p⃗_b) with b
≠ b₀ occurs only at a level, where ρ ≤ C_lev − 11 + I_lev: Step 4′ is a step of [[thm:iii-i14-3-1]], at b₀, and at a
rotating b [[prop:iii-i15-2-5]] has no Step 4′ ([[sec:s23-base-points]]), its rotation coordinates being the A_b read at
the levels. So ρ + R_base + 16 ≤ C_lev + I_lev + R_base + 5 < T_12 + 14, as X_12 = 11,270,575,291,594,154,340 exceeds
R_base + 22, so that also T_11 < T_12 in (d). The convention "h small" of
```

#### U35. 71-explicit-constants.md, lines 5331 with P-D0 (HEAD 5118)

Place: lem:uc-small-orders, proof of (e): the integer.

Old (1 line):

```old
T_12 = C_lev + I_lev + X_12 = 632,811,129,714,617,668,891,744,631,700,922,473,889, and D_* = T_12 + 14. ∎
```

New (1 line):

```new
T_12 = C_lev + I_lev + X_12 = 10,377,919,287,730,263,270,654,748,732, and D_* = T_12 + 14. ∎
```

#### U36. 71-explicit-constants.md, lines 5348–5353 with P-D0 (HEAD 5135–5140)

Place: rem:uc-small-reading, the display and the last sentence.

Old (6 lines):

```old
    D′_* := T_12 + 18 + 20,565,308,337L_< + (C_lev + I_lev − 9)L_> + 2R_base
         = 37,862,223,260,395,632,651,500,935,434,129,742,005,773,058,097,412,552,791 < 3.78623·10⁵⁵,

and d_* ≤ D′_*. Here 20,565,308,337L_< = 1,230,459,230,427,132,871,449,409,566 and (C_lev + I_lev − 9)L_> =
37,862,223,260,395,632,018,689,805,718,278,798,706,052,416,491,558,315,520, to which T_12 + 18 =
632,811,129,714,617,668,891,744,631,700,922,473,907 and 2R_base = 2,815,177,548,877,033,482,353,798 are added.
```

New (6 lines):

```new
    D′_* := T_12 + 18 + 20,565,308,337L_< + (C_lev + I_lev − 9)L_> + 2R_base
         = 71,277,718,098,469,630,550,670,708,708,947,562,256 < 7.12778·10³⁷,

and d_* ≤ D′_*. Here 20,565,308,337L_< = 141,246,834,800,258,324,487 and (C_lev + I_lev − 9)L_> =
71,277,718,088,091,711,121,370,450,870,822,110,999, to which T_12 + 18 = 10,377,919,287,730,263,270,654,748,750 and
2R_base = 323,159,767,212,378,020 are added.
```

#### U37. 71-explicit-constants.md, lines 5356 with P-D0 (HEAD 5143)

Place: prop:uc-d-small, the opening.

Old (1 line):

```old
with the index sets as constructed and the choices of [[def:uc-choice]] and [[def:cs-choices]], let d_F be the number
```

New (1 line):

```new
with the choices of [[def:uc-choice]] and [[def:cs-choices]], let d_F be the number
```

#### U38. 71-explicit-constants.md, lines 5367–5373 with P-D0 (HEAD 5154–5160)

Place: prop:uc-d-small (b) and (c).

Old (7 lines):

```old
(b) for the fixed seminorms of [[lem:uc-small-orders]] (d), d_NM ≤ D_♭ + D_* + d̄_Φ =
37,862,223,260,395,634,549,934,375,862,530,497,755,494,177,219,176,347,223, so d_NM < 3.78623·10⁵⁵, and N_NM = 21d_NM + 6
≤ 795,106,688,468,308,325,548,621,893,113,140,452,865,377,721,602,703,291,689 < 7.9511·10⁵⁶;

(c) for those of [[rem:uc-small-reading]], d_NM ≤ D_♭ + D′_* + d̄_Φ =
75,724,446,520,791,266,568,624,181,582,042,570,869,522,603,615,666,426,111 < 7.57245·10⁵⁵, and N_NM ≤
1,590,213,376,936,616,597,941,107,813,222,893,988,259,974,675,928,994,948,337 < 1.59022·10⁵⁷;
```

New (6 lines):

```new
(b) for the fixed seminorms of [[lem:uc-small-orders]] (d), d_NM ≤ D_♭ + D_* + d̄_Φ =
71,277,718,129,603,389,008,535,406,246,925,875,580, so d_NM < 7.12778·10³⁷, and N_NM = 21d_NM + 6 ≤
1,496,832,080,721,671,169,179,243,531,185,443,387,186 < 1.4969·10³⁹;

(c) for those of [[rem:uc-small-reading]], d_NM ≤ D_♭ + D′_* + d̄_Φ = 142,555,436,217,695,100,271,475,851,685,218,689,090
< 1.42556·10³⁸, and N_NM ≤ 2,993,664,160,571,597,105,700,992,885,389,592,470,896 < 2.99367·10³⁹;
```

#### U39. 71-explicit-constants.md, lines 5398–5405 with P-D0 (HEAD 5185–5192)

Place: prop:uc-d-small, proof of (b) and (c).

Old (8 lines):

```old
(b) By [[lem:cs-sharp]], d_F ≤ d_R ≤ D_♭; by [[lem:uc-small-orders]] (e), d_* ≤ D_*; and d_Φ ≤ d̄_Φ =
56,389,441,693,909,346 ([[lem:uc-lambda]] (d)). So both terms of [[eq:uc-d-small]] are at most D_♭ + D_* + d̄_Φ, the
integer printed: D_♭ + D_* = 37,862,223,260,395,634,549,934,375,862,530,497,755,437,787,777,482,437,877, and adding d̄_Φ
gives it. Its leading digits are 3.786222, and 21 times it plus 6 is the integer printed, with leading digits 7.951066.

(c) is (b) with D′_*: D_♭ + D′_* = 75,724,446,520,791,266,568,624,181,582,042,570,869,466,214,173,972,516,765, and adding
d̄_Φ gives the integer printed, with leading digits 7.572444; 21 times it plus 6 is the integer printed, with leading
digits 1.590213.
```

New (7 lines):

```new
(b) By [[lem:cs-sharp]], d_F ≤ d_R ≤ D_♭; by [[lem:uc-small-orders]] (e), d_* ≤ D_*; and d_Φ ≤ d̄_Φ = 228,357,817,884
([[lem:uc-lambda]] (d)). So both terms of [[eq:uc-d-small]] are at most D_♭ + D_* + d̄_Φ, the integer printed: D_♭ +
D_* = 71,277,718,129,603,389,008,535,406,018,568,057,696, and adding d̄_Φ gives it. Its leading digits are 7.127771, and
21 times it plus 6 is the integer printed, with leading digits 1.496832.

(c) is (b) with D′_*: D_♭ + D′_* = 142,555,436,217,695,100,271,475,851,456,860,871,206, and adding d̄_Φ gives the integer
printed, with leading digits 1.425554; 21 times it plus 6 is the integer printed, with leading digits 2.993664.
```

#### U40. 71-explicit-constants.md, lines 5611–5620 with P-D0 (HEAD 5398–5407)

Place: prop:uc-data-order (d).

Old (10 lines):

```old
(d) At the computational point, with the index sets as constructed and the choices of [[def:uc-choice]] and
[[def:cs-choices]], J ≤ 8; so L_P ≤ 39 in the class of [[eq:vii-0-1]] and L_P ≤ 44 in the class ℰ_0^½. With D_NM of
[[thm:uc-integer]],

    K ≤ 22D_NM + 345
      = 1,665,937,823,457,407,864,509,731,994,804,936,559,129,497,279,544,661,374,787 < 1.66594·10⁵⁷,

d_1 ≤ 22D_NM + 331 and N ≤ 22D_NM + 348. For the fixed seminorms of [[lem:uc-small-orders]] (d), K < 8.3297·10⁵⁶; and K >
22d > 2.695·10²⁸. In the class ℰ_0^½, k1 ≤ 22D_NM + 340 and 9.684·10⁵⁶ < K*(a, M, k1) < 1.11014·10¹¹⁵ for every a ∈ (ℓ0 −
1, 3).
```

New (9 lines):

```new
(d) At the computational point, with the choices of [[def:uc-choice]] and [[def:cs-choices]], J ≤ 8; so L_P ≤ 39 in the
class of [[eq:vii-0-1]] and L_P ≤ 44 in the class ℰ_0^½. With D_NM of [[thm:uc-integer]],

    K ≤ 22D_NM + 345
      = 3,136,219,596,789,292,205,972,468,737,074,811,160,325 < 3.13622·10³⁹,

d_1 ≤ 22D_NM + 331 and N ≤ 22D_NM + 348. For the fixed seminorms of [[lem:uc-small-orders]] (d), K < 1.5682·10³⁹; and K >
22d > 3.094058·10²¹. In the class ℰ_0^½, k1 ≤ 22D_NM + 340 and 1.27642·10⁴³ < K*(a, M, k1) < 3.93435·10⁷⁹ for every a ∈
(ℓ0 − 1, 3).
```

#### U41. 71-explicit-constants.md, lines 5702–5711 with P-D0 (HEAD 5489–5498)

Place: prop:uc-data-order, proof of (d).

Old (10 lines):

```old
22d + 306 + L_P ≤ 22d + 345. Here d is the d_NM of [[prop:uc-d-small]], and d_NM ≤ D_NM ([[thm:uc-integer]]); 22D_NM =
1,665,937,823,457,407,864,509,731,994,804,936,559,129,497,279,544,661,374,442, which with 345 added is the integer
printed, with leading digits 1.6659378. d_1 = K − 14 and N = K + 3 give the next two bounds. By [[prop:uc-d-small]] (b),
for the fixed seminorms of [[lem:uc-small-orders]] (d), d_NM is at most D_b :=
37,862,223,260,395,634,549,934,375,862,530,497,755,494,177,219,176,347,223, and 22D_b + 345 =
832,968,911,728,703,960,098,556,268,975,670,950,620,871,898,821,879,639,251 < 8.3297·10⁵⁶. By [[eq:uc-lower]], d ≥
d_acc > 1.2250·10²⁷, so K > 22d > 2.695·10²⁸. In the class ℰ_0^½, d_1 ≤ 22d + 336 and k1 = d_1 + 4 ≤ 22D_NM + 340 =: k̄,
and by (c) K*(a, M, k1) < k̄ + 4 + (4k̄ + 35)(k̄ + 3) = 4k̄² + 48k̄ + 109. As k̄ > 10⁵⁷, 48k̄ + 109 < 10⁻⁵⁵k̄², and as k̄
< 1.6659378235·10⁵⁷, k̄² < 2.775348832·10¹¹⁴; so K*(a, M, k1) < (4 + 10⁻⁵⁵) · 2.775348832·10¹¹⁴ < 1.11014·10¹¹⁵. And
K*(a, M, k1) > (4/3)k1², with k1 > 22d > 2.695·10²⁸, so K*(a, M, k1) > (4/3) · 7.263025·10⁵⁶ > 9.684·10⁵⁶. ∎
```

New (10 lines):

```new
22d + 306 + L_P ≤ 22d + 345. Here d is the d_NM of [[prop:uc-d-small]], and d_NM ≤ D_NM ([[thm:uc-integer]]); 22D_NM =
3,136,219,596,789,292,205,972,468,737,074,811,159,980, which with 345 added is the integer printed, with leading digits
3.1362195. d_1 = K − 14 and N = K + 3 give the next two bounds. By [[prop:uc-d-small]] (b), for the fixed seminorms of
[[lem:uc-small-orders]] (d), d_NM is at most D_b := 71,277,718,129,603,389,008,535,406,246,925,875,580, and 22D_b + 345 =
1,568,109,798,851,274,558,187,778,937,432,369,263,105 < 1.5682·10³⁹. At the choice of [[def:uc-choice]], d ≥ d_acc ≥ 3R >
1.40639·10²⁰ ([[thm:uc-integer]]), so K > 22d > 3.094058·10²¹. In the class ℰ_0^½, d_1 ≤ 22d + 336 and k1 = d_1 + 4 ≤
22D_NM + 340 =: k̄, and by (c) K*(a, M, k1) < k̄ + 4 + (4k̄ + 35)(k̄ + 3) = 4k̄² + 48k̄ + 109. As k̄ > 10³⁹, 48k̄ + 109 <
10⁻³⁷k̄², and as k̄ < 3.1362195968·10³⁹, k̄² < 9.83587336·10⁷⁸; so K*(a, M, k1) < (4 + 10⁻³⁷) · 9.83587336·10⁷⁸ <
3.93435·10⁷⁹. And K*(a, M, k1) > (4/3)k1², with k1 > 22d > 3.094058·10²¹, so K*(a, M, k1) > (4/3) · 9.573194907364·10⁴² >
1.27642·10⁴³. ∎
```

#### U41a. 71-explicit-constants.md, lines 5728–5730 with P-D0 (HEAD 5515–5517)

Place: sec:tr, the opening paragraph: the index sets.

Old (3 lines):

```old
[[thm:uc-integer]] bounds d at the computational point, which is not shown to lie in the set on which [[thm:settling]]
is proved ([[rem:ec-point-outside]]). This section keeps the gauge parameters (γ_Υ, e_Υ) = (1/100, 1/100) and lets h run
through [h_m, 10⁻⁶), h_m := 4.76·10⁻¹¹. In the proof of [[thm:uc-integer]] h enters through five inputs: (a) the number
```

New (6 lines):

```new
[[thm:uc-integer]] bounds d at the computational point, which is not shown to lie in the set on which [[thm:settling]] is
proved ([[rem:ec-point-outside]]). This section keeps the gauge parameters (γ_Υ, e_Υ) = (1/100, 1/100) and the index sets
as constructed ([[sec:is]]), and lets h run through [h_m, 10⁻⁶), h_m := 4.76·10⁻¹¹; this paper shows that the smaller
index sets of [[def:is-flat-set]], which [[thm:uc-integer]] takes, serve at the computational point
([[thm:is-flat-serves]]), and does not treat them at other h. In the proof of [[thm:uc-integer]], run with the index sets
as constructed ([[prop:uc-dependence]]), h enters through five inputs: (a) the number
```

#### U42. 71-explicit-constants.md, lines 5803–5804 with P-D0 (HEAD 5589–5590)

Place: thm:tr-transfer (iii), its last line: N̄_Λ := N̄(h), N₁ removed.

Old (2 lines):

```old
[[prop:uc-dependence]] at k̄_0 := 3, J_* := 15,000,015, l_* := 50 and N̄_Λ := max(N̄(h), N₁), N₁ the least integer with
3,060,003,264N₁ > I_base + 22,083.
```

New (1 line):

```new
[[prop:uc-dependence]] at k̄_0 := 3, J_* := 15,000,015, l_* := 50 and N̄_Λ := N̄(h).
```

#### U43a. 71-explicit-constants.md, lines 5809 with P-D0 (HEAD 5595)

Place: rem:tr-scope, the first sentence: the index sets.

Old (1 line):

```old
**Remark {#rem:tr-scope}** (What the theorem assumes.) [[thm:tr-transfer]] (iii) is conditional three times. First, it
```

New (2 lines):

```new
**Remark {#rem:tr-scope}** (What the theorem assumes.) [[thm:tr-transfer]] (iii), which concerns the index sets as
constructed, is conditional three times. First, it
```

#### U43. 71-explicit-constants.md, lines 5826–5827 with P-D0 (HEAD 5612–5613)

Place: rem:tr-scope: the threshold, and the index sets.

Old (2 lines):

```old
[[prop:tr-inputs]] (b), can fail, and where ε_ind(h) < 1.99·10⁻²⁸ the bounds of [[thm:uc-integer]] fail for every
admissible choice ([[prop:tr-fail]]). The lower bounds of (ii) use only admissibility.
```

New (5 lines):

```new
[[prop:tr-inputs]] (b), can fail, and where ε_ind(h) < 1.45·10⁻¹⁹ the bounds of [[thm:uc-integer]] fail for every
admissible choice ([[prop:tr-fail]]). The lower bounds of (ii) use only admissibility, and, like [[prop:tr-mu-small]],
which uses 𝔡₀ as an increment, they are proved for the index sets as constructed; for the smaller index sets of
[[def:is-flat-set]], which [[thm:uc-integer]] takes, this paper proves [[thm:is-flat-serves]] at the computational point
only.
```

#### U44a. 71-explicit-constants.md, lines 6330 with P-D0 (HEAD 6116)

Place: proof of thm:tr-transfer (iii): lem:uc-admissible with the index sets as constructed.

Old (1 line):

```old
part below 2 is unchanged. The proof of [[lem:uc-admissible]] applies at h with these ε_K and ε_+: (G) and (G⁺) hold, as
```

New (2 lines):

```new
part below 2 is unchanged. The proof of [[lem:uc-admissible]] applies at h with these ε_K and ε_+ and with the index sets
as constructed: (G) and (G⁺) hold, as
```

#### U44. 71-explicit-constants.md, lines 6336–6337 with P-D0 (HEAD 6122–6123)

Place: proof of thm:tr-transfer (iii): the hypotheses of prop:uc-dependence.

Old (2 lines):

```old
(c) holds with N̄_Λ, k̄_0 = 3, J_* and l_* as stated; for N̄_Λ ≥ N₁,
4k̄_max + 24 = 4·765,000,816N̄_Λ + 36 > I_base + 22,119, the inequality that [[prop:uc-dependence]] supposes. Of the
```

New (2 lines):

```new
(c) holds with N̄_Λ, k̄_0 = 3, J_* and l_* as stated; and ε_K < μ(h) ≤ μ_G < 0.998ε_Υ ([[eq:is-mu]]), as
[[prop:uc-dependence]] asks. Of the
```

#### U45. 71-explicit-constants.md, lines 6348 with P-D0 (HEAD 6134)

Place: proof of thm:tr-transfer (iii): the last sentence.

Old (1 line):

```old
[[prop:uc-dependence]] applies at h with N̄_Λ := max(N̄(h), N₁), k̄_0 = 3, J_* = 15,000,015 and l_* = 50, and gives the
```

New (2 lines):

```new
[[prop:uc-dependence]] applies at h, with the index sets as constructed, N̄_Λ := N̄(h), k̄_0 = 3, J_* = 15,000,015 and
l_* = 50, and gives the
```

#### U46. 71-explicit-constants.md, lines 6389–6401 with P-D0 (HEAD 6175–6187)

Place: prop:tr-fail, statement and proof: the numbers (line breaks kept).

Old (13 lines):

```old
**Proposition {#prop:tr-fail}** (The bound fails near a crossing.) Let 0 < h < 10⁻⁶, and suppose that the parameter point
(h, 1/100, 1/100) is admissible and that ε_ind(h) < 1.99·10⁻²⁸. Every admissible choice of the weights at (h, 1/100,
1/100) gives d_NM ≥ d_acc > 3(1 − 2.1·10⁻⁸)/ε_ind(h)², which exceeds 7.5755·10⁵⁵, and so the bounds for d_acc and d_NM of
[[thm:uc-integer]]. Let h_c := 1/1001992 = 9.98011…·10⁻⁷; then h_c ∈ 𝖩, ι_v(1000, h_c) = 4, and ε_ind(h) < 1.99·10⁻²⁸ for
0 < |h − h_c| < 1.986·10⁻³⁴.

*Proof.* [[lem:ec-lb-rounds]] applies with Θ_g := ε_ind(h) and Θ_η := δ̄: ε_g ≤ ε_ind ≤ ε_ind(h), ε_K < ε_+ < ε_ind,
η_2 < ε_+ < ε_ind ≤ δ_50 < δ̄, and 5Θ_g + Θ_η < 10⁻²⁷ + δ̄ < 2.1·10⁻⁸. It gives R > (1 − 2.1·10⁻⁸)/ε_ind(h)²; so by the
argument of [[thm:loss-d]] (ii), which does not use the computational point (proof of [[thm:ec-lb-proved]]),
d_NM ≥ d_acc ≥ 3R > 3(1 − 2.1·10⁻⁸)/ε_ind(h)² > 3(1 − 2.1·10⁻⁸)/(1.99·10⁻²⁸)² > 7.5755·10⁵⁵. At l = 1000,
κ = 1002000 and (n − 3)/((l + 1)² − (n − 1)²) = 1/1001992 at n = 4, so ι_v(1000, h_c) = 4 ([[lem:tr-c-v]] (b)) and
h_c ∈ 𝖩_v(1000, 4). By [[eq:tr-vslope]], 0 < ∂_hι_v ≤ (l + 1)² = 1002001, so for 0 < |h − h_c| < 1.986·10⁻³⁴,
0 < |ι_v(1000, h) − 4| < 1.99·10⁻²⁸, and the entry ι_v − 1 of ℛ^v_1000, of modulus below 50 and not an integer, bounds
```

New (13 lines):

```new
**Proposition {#prop:tr-fail}** (The bound fails near a crossing.) Let 0 < h < 10⁻⁶, and suppose that the parameter point
(h, 1/100, 1/100) is admissible and that ε_ind(h) < 1.45·10⁻¹⁹. Every admissible choice of the weights at (h, 1/100,
1/100) gives d_NM ≥ d_acc > 3(1 − 2.1·10⁻⁸)/ε_ind(h)², which exceeds 1.4268·10³⁸, and so the bounds for d_acc and d_NM of
[[thm:uc-integer]]. Let h_c := 1/1001992 = 9.98011…·10⁻⁷; then h_c ∈ 𝖩, ι_v(1000, h_c) = 4, and ε_ind(h) < 1.45·10⁻¹⁹ for
0 < |h − h_c| < 1.447·10⁻²⁵.

*Proof.* [[lem:ec-lb-rounds]] applies with Θ_g := ε_ind(h) and Θ_η := δ̄: ε_g ≤ ε_ind ≤ ε_ind(h), ε_K < ε_+ < ε_ind,
η_2 < ε_+ < ε_ind ≤ δ_50 < δ̄, and 5Θ_g + Θ_η < 10⁻¹⁸ + δ̄ < 2.1·10⁻⁸. It gives R > (1 − 2.1·10⁻⁸)/ε_ind(h)²; so by the
argument of [[thm:loss-d]] (ii), which does not use the computational point (proof of [[thm:ec-lb-proved]]),
d_NM ≥ d_acc ≥ 3R > 3(1 − 2.1·10⁻⁸)/ε_ind(h)² > 3(1 − 2.1·10⁻⁸)/(1.45·10⁻¹⁹)² > 1.4268·10³⁸. At l = 1000,
κ = 1002000 and (n − 3)/((l + 1)² − (n − 1)²) = 1/1001992 at n = 4, so ι_v(1000, h_c) = 4 ([[lem:tr-c-v]] (b)) and
h_c ∈ 𝖩_v(1000, 4). By [[eq:tr-vslope]], 0 < ∂_hι_v ≤ (l + 1)² = 1002001, so for 0 < |h − h_c| < 1.447·10⁻²⁵,
0 < |ι_v(1000, h) − 4| < 1.45·10⁻¹⁹, and the entry ι_v − 1 of ℛ^v_1000, of modulus below 50 and not an integer, bounds
```

#### U47. 71-explicit-constants.md, lines 6425 with P-D0 (HEAD 6211)

Place: sec:tr-exceptional, the paragraph after prop:tr-mu-small.

Old (1 line):

```old
d_NM > 0.3168h⁻², which exceeds 7.57245·10⁵⁵ for h ≤ 6.46·10⁻²⁹ ([[rem:ec-lb-unbounded]]).
```

New (1 line):

```new
d_NM > 0.3168h⁻², which exceeds 1.42556·10³⁸ for h ≤ 4.71·10⁻²⁰ ([[rem:ec-lb-unbounded]]).
```

#### U48. 00-front.md, lines 36–37 with P-D0 (HEAD 36–37)

Place: the front matter.

Old (2 lines):

```old
admissible choice of the weights, orders and inner products and the index sets as the proofs construct them,
1.2250 × 10²⁷ < d < 7.57245 × 10⁵⁵; at equality, μ0 = √72 l5², timelike
```

New (2 lines):

```new
admissible choice of the index sets, weights, orders and inner products, 1.403 × 10²⁰ < d < 1.42556 × 10³⁸; at equality,
μ0 = √72 l5², timelike
```

#### U49. 01-introduction.md, lines 155–157 with P-D0 (HEAD 155–157)

Place: the introduction.

Old (3 lines):

```old
lie in it, d > 1.2250 × 10²⁷ at every admissible choice of the weights, for the index sets as the proofs construct them
([[cor:is-lower]]), and d < 7.57245 × 10⁵⁵ at one admissible choice of the weights, orders and inner products
([[thm:uc-integer]]). A
```

New (3 lines):

```new
lie in it, d > 1.403 × 10²⁰ at every admissible choice of the weights ([[thm:loss-d]]) and d > 1.2250 × 10²⁷ for the
index sets as the proofs construct them ([[cor:is-lower]]), while d < 1.42556 × 10³⁸ at one admissible choice of the
index sets, weights, orders and inner products ([[thm:uc-integer]]). A
```

#### U50. 03-theorems.md, lines 316–319 with P-D0 (HEAD 316–319)

Place: the theorems chapter, after the main theorem.

Old (4 lines):

```old
computational point of [[def:ec-point]], which is not shown to lie in that set ([[rem:ec-point-outside]]), and at one
admissible choice of the
weights, orders and inner products, d is at most an integer below 7.57245 × 10⁵⁵ ([[thm:uc-integer]]), and K at most one
below 1.66594 × 10⁵⁷.
```

New (3 lines):

```new
computational point of [[def:ec-point]], which is not shown to lie in that set ([[rem:ec-point-outside]]), and at one
admissible choice of the index sets, weights, orders and inner products, d is at most an integer below 1.42556 × 10³⁸
([[thm:uc-integer]]), and K at most one below 3.13622 × 10³⁹.
```

#### U50a. 03-theorems.md, lines 363–367 with P-D0 (HEAD 363–367)

Place: the theorems chapter, the item on the constants: the transfer, for the index sets as constructed.

Old (5 lines):

```old
  explicit lower bounds ([[thm:loss-d]]) and explicit upper bounds for d and N_NM at one admissible choice of the
  weights, orders and inner products ([[thm:uc-integer]]), and at the other damping parameters h = 1/γ_C ∈ (0, 10⁻⁶) with
  the same gauge parameters lower bounds that are unbounded near some γ_C ∈ (10⁶, 2 × 10⁶), and, for γ_C ≤ 2.1 × 10¹⁰
  outside a set of h of total length below 1.7 × 10⁻¹¹, upper bounds under a condition decided only at γ_C = 10⁶
  ([[thm:tr-transfer]], [[prop:tr-mu-small]]); through the lower bounds, upper bounds for δ and for the
```

New (6 lines):

```new
  explicit lower bounds ([[thm:loss-d]]) and explicit upper bounds for d and N_NM at one admissible choice of the index
  sets, weights, orders and inner products ([[thm:uc-integer]]), and at the other damping parameters h = 1/γ_C ∈ (0,
  10⁻⁶) with the same gauge parameters, for the index sets as the proofs construct them, lower bounds that are unbounded
  near some γ_C ∈ (10⁶, 2 × 10⁶), and, for γ_C ≤ 2.1 × 10¹⁰ outside a set of h of total length below 1.7 × 10⁻¹¹, upper
  bounds under a condition decided only at γ_C = 10⁶ ([[thm:tr-transfer]], [[prop:tr-mu-small]]); through the lower
  bounds, upper bounds for δ and for the
```

#### U51. 90-scope.md, lines 73–77 with P-D0 (HEAD 73–77)

Place: the scope chapter: the upper bound.

Old (5 lines):

```old
([[thm:loss-d]] (ii), [[prop:ec-delta-cap]]), and d > 1.2250 × 10²⁷ and N_NM > 2.5725 × 10²⁸ at every admissible choice
of the weights, for the index sets as the proofs construct them ([[cor:is-lower]]). These are lower bounds for the
loss that this proof's choices produce, not for the least loss with which the tame estimates hold ([[thm:loss-d]]). At
that point, for those index sets and at one admissible choice of the weights and of the free orders and inner products,
d is at most an integer below 7.57245 × 10⁵⁵ and N_NM at most one below 1.59022 × 10⁵⁷ ([[thm:uc-integer]]). The order of
```

New (6 lines):

```new
([[thm:loss-d]] (ii), [[prop:ec-delta-cap]]), and d > 1.2250 × 10²⁷ and N_NM > 2.5725 × 10²⁸ at every admissible choice
of the weights, for the index sets as the proofs construct them ([[cor:is-lower]]). These are lower bounds for the loss
that this proof's choices produce, not for the least loss with which the tame estimates hold ([[thm:loss-d]]). At that
point, at one admissible choice of smaller index sets, which serve as well ([[thm:is-flat-serves]]), of the weights and
of the free orders and inner products, d is at most an integer below 1.42556 × 10³⁸ and N_NM at most one below
2.99367 × 10³⁹ ([[thm:uc-integer]]). The order of
```

#### U52. 90-scope.md, lines 79 with P-D0 (HEAD 79)

Place: the scope chapter: the order K.

Old (1 line):

```old
so that at that point K is at most an integer below 1.66594 × 10⁵⁷ ([[prop:uc-data-order]]). The
```

New (1 line):

```new
so that at that point K is at most an integer below 3.13622 × 10³⁹ ([[prop:uc-data-order]]). The
```

#### U53. 90-scope.md, lines 82–83 with P-D0 (HEAD 82–83)

Place: the scope chapter: the lower bound at other h, for the index sets as constructed.

Old (2 lines):

```old
gauge values and other values h ∈ (0, 10⁻⁶) of the damping parameter, d > 2.0517 × 10¹⁰/μ(h), μ(h) the least excess above
3 that the roots of real part below 3 of the damping polynomials give to the exponents of the construction, which tends
```

New (3 lines):

```new
gauge values and other values h ∈ (0, 10⁻⁶) of the damping parameter, and for the index sets as the proofs construct
them, d > 2.0517 × 10¹⁰/μ(h), μ(h) the least excess above 3 that the roots of real part below 3 of the damping
polynomials give to the exponents of the construction, which tends
```

### Crosswalk rows

No label is added, removed or renamed. For each changed label: its existing row keeps its fields and takes the note
below, appended with the text name and after P-D0's notes (which this file does not repeat; for eq:uc-choice,
eq:uc-deltas, def:uc-choice, lem:uc-admissible and lem:uc-lambda the values below supersede P-D0's); the four
tab-separated fields give the label, the source
"paper/reader/proofs/P-UB3.md@PENDING:N" (N the line of this file where the label's new text begins, PENDING to be
replaced by the commit of the merge), the source name and the note, for a merge that records the new source.

    ch:explicit-constants	paper/reader/proofs/P-UB3.md@PENDING:304	P-UB3, text U1	the opening: bounds at the choice (D_acc < 7.12778e37, D_NM < 1.42556e38, N_NM < 2.99367e39, K < 3.13622e39); "one admissible choice of the index sets"; the sentence on other h for the index sets as constructed (U1-U3)
    rem:ec-point-outside	paper/reader/proofs/P-UB3.md@PENDING:365	P-UB3, text U3a	last sentence: the transfer to other h for the index sets as constructed; "the count N_Λ of lem:uc-lambda" becomes "the count N_Λ"
    thm:loss-d	paper/reader/proofs/P-UB3.md@PENDING:388	P-UB3, text U4	closing paragraph: for the index sets of def:uc-choice (G) asks only ε_K < μ♭_Z; upper bounds at the new choice (U4, U5)
    rem:ec-lb-unbounded	paper/reader/proofs/P-UB3.md@PENDING:429	P-UB3, text U6	d_NM exceeds 1.42556e38 for h ≤ 4.71e-20; the last sentence for the same index sets (U6, U6a)
    rem:ec-upper-point	paper/reader/proofs/P-UB3.md@PENDING:475	P-UB3, text U7	at the choice ε_K = 1.4589e-10: first line < 1.41633e20, windows < 4.84721e17, < 1.0071 · 3R, 3R > 1.40639e20; L_< = 6,868,208,951, L_> = R_b = 6,868,208,953; C_lev < 1.0378e28, C_* < 3.11338e28
    rem:ec-upper-open	paper/reader/proofs/P-UB3.md@PENDING:529	P-UB3, text U8	(1) for the index sets of def:uc-choice (cor:is-flat, thm:is-flat-serves): N_Λ ≤ 3,683,190,611; the numbers at the new choice
    sec:uc-close	paper/reader/proofs/P-UB3.md@PENDING:592	P-UB3, text U9	opening: the smaller index sets serve; D_acc < 7.12778e37, D_NM < 1.42556e38, against 3R > 1.40639e20 at the choice
    lem:uc-fourier-count	paper/reader/proofs/P-UB3.md@PENDING:630	P-UB3, text U10	last sentence: J_* = 15,000,015 for both index sets; lem:uc-n-iota at the choice
    def:uc-choice	paper/reader/proofs/P-UB3.md@PENDING:647	P-UB3, text U11	ε_K = 1.4589e-10, ε_+ = 1.459e-10 (on P-D0 T6)
    eq:uc-choice	paper/reader/proofs/P-UB3.md@PENDING:647	P-UB3, text U11	display: ε_K := 1.4589·10⁻¹⁰, ε_+ := 1.459·10⁻¹⁰ (on P-D0 T6)
    lem:uc-admissible	paper/reader/proofs/P-UB3.md@PENDING:663	P-UB3, text U12	the constants at the new choice; ε_K < 0.998ε_Υ ≤ ε_g − 2ε added; ε′_0 = 5e-15 (U12-U14, on P-D0 T7-T9)
    eq:uc-deltas	paper/reader/proofs/P-UB3.md@PENDING:663	P-UB3, text U12	display: Δβ_0 = 1.4559836589·10⁻¹⁰ (on P-D0 T7)
    lem:uc-lambda	paper/reader/proofs/P-UB3.md@PENDING:743	P-UB3, text U15	N̄_Λ := 3,683,190,611, the count of cor:is-flat; k̄_max = 2,817,643,822,898,538,579, d̄_Φ = 228,357,817,884 (on P-D0 T12, whose larger N̄_Λ is no longer needed)
    lem:uc-n-iota	paper/reader/proofs/P-UB3.md@PENDING:774	P-UB3, text U16	N_ι = 5,188,959,638,229,843,970,554,286,700 < 5.18896e27 at N̄_Λ = 3,683,190,611 (U16, U17)
    prop:uc-explicit	paper/reader/proofs/P-UB3.md@PENDING:855	P-UB3, text U18	recomputed at ε_K = 1.4589e-10: L_<, L_>, R_b, the decimals and D_e = 1.41633e20; ε_+ < 1e-9 in the T_2 bound
    eq:uc-counts	paper/reader/proofs/P-UB3.md@PENDING:855	P-UB3, text U18	display: N < 6.86821e9, T < 2.35143e19, T_2 < 2.06047e16
    thm:uc-integer	paper/reader/proofs/P-UB3.md@PENDING:947	P-UB3, text U19	"with the index sets of def:uc-choice"; D_acc < 7.12778e37, D_NM < 1.42556e38, 21D_NM + 6 < 2.99367e39; eq:uc-lower stated for the index sets as constructed, beside 1.403e20 at every choice; 3R > 1.40639e20 at the choice, D_e < 1.0071 · 3R
    eq:uc-lower	paper/reader/proofs/P-UB3.md@PENDING:947	P-UB3, text U19	now introduced as the bound for the index sets as constructed (cor:is-lower)
    prop:uc-dependence	paper/reader/proofs/P-UB3.md@PENDING:1035	P-UB3, text U20	P-UB3 Part 1: hypothesis 4k̄_max + 24 > I_base + 22,119 removed (D′_* with max(T_11, T_12)); ε_+ < 1e-13 replaced by ε_K < 0.998ε_Υ; either family of index sets
    rem:uc-missing	paper/reader/proofs/P-UB3.md@PENDING:1107	P-UB3, text U21	L_> = 6,868,208,953, C_lev < 1.0378e28, all of D_acc but less than 3.12e28
    cor:is-lower	paper/reader/proofs/P-UB3.md@PENDING:1124	P-UB3, text U22	the clause and sentence at ε_K = 1.6747e-17 (the former choice) removed (U22, U22b)
    sec:cs	paper/reader/proofs/P-UB3.md@PENDING:1158	P-UB3, text U23	opening: c_0 < 6N_ι + 8.64e20, C_* < 3.11338e28
    eq:cs-clev	paper/reader/proofs/P-UB3.md@PENDING:1175	P-UB3, text U24	C_lev = 10,377,919,276,459,687,944,791,764,540
    eq:cs-iterations	paper/reader/proofs/P-UB3.md@PENDING:1192	P-UB3, text U25	I_base = 161,579,883,606,166,913
    lem:cs-rest	paper/reader/proofs/P-UB3.md@PENDING:1210	P-UB3, text U26	d̄_Φ = 228,357,817,884
    prop:cs-cstar	paper/reader/proofs/P-UB3.md@PENDING:1255	P-UB3, text U27	"with the choices of def:uc-choice"; recomputed at N̄_Λ = 3,683,190,611
    eq:cs-cstar	paper/reader/proofs/P-UB3.md@PENDING:1255	P-UB3, text U27	C_* = 31,133,758,693,167,165,978,342,162,162 < 3.11338e28
    rem:cs-sharpness	paper/reader/proofs/P-UB3.md@PENDING:1255	P-UB3, text U27	all but less than 8.64e20 is 6N_ι; next term < 8.411e20; L_>C_lev all of D_acc but less than 3.12e28
    sec:cs-small	paper/reader/proofs/P-UB3.md@PENDING:1299	P-UB3, text U28	R_base = 161,579,883,606,189,010
    lem:cs-sharp	paper/reader/proofs/P-UB3.md@PENDING:1316	P-UB3, text U29	D_♭ = 71,277,718,119,225,469,720,805,142,747,913,308,950 < 7.12778e37 (U29, U30)
    eq:cs-sharp	paper/reader/proofs/P-UB3.md@PENDING:1316	P-UB3, text U29	D_♭ < 7.12778e37
    lem:uc-small-orders	paper/reader/proofs/P-UB3.md@PENDING:1356	P-UB3, text U31	"with the choices of def:uc-choice"; k̂_0 = 3,200,585,392,700; D_* < 1.0378e28; X_12 = 11,270,575,291,594,154,340 > R_base + 22 (U31-U35)
    eq:uc-small	paper/reader/proofs/P-UB3.md@PENDING:1389	P-UB3, text U33	D_* = 10,377,919,287,730,263,270,654,748,746
    rem:uc-small-reading	paper/reader/proofs/P-UB3.md@PENDING:1452	P-UB3, text U36	D′_* = 71,277,718,098,469,630,550,670,708,708,947,562,256 < 7.12778e37
    prop:uc-d-small	paper/reader/proofs/P-UB3.md@PENDING:1473	P-UB3, text U37	"with the choices of def:uc-choice"; (b) d_NM < 7.12778e37, N_NM < 1.4969e39; (c) d_NM < 1.42556e38, N_NM < 2.99367e39 (U37-U39)
    prop:uc-data-order	paper/reader/proofs/P-UB3.md@PENDING:1554	P-UB3, text U40	(d) at the choices of def:uc-choice: K < 3.13622e39; fixed seminorms K < 1.5682e39; K > 22d > 3.094058e21; 1.27642e43 < K* < 3.93435e79 (U40, U41)
    sec:tr	paper/reader/proofs/P-UB3.md@PENDING:1614	P-UB3, text U41a	opening: the section keeps the index sets as constructed; the smaller sets are shown to serve at the computational point only
    thm:tr-transfer	paper/reader/proofs/P-UB3.md@PENDING:1636	P-UB3, text U42	(iii): N̄_Λ := N̄(h), N₁ removed, as prop:uc-dependence no longer needs it (the index sets as constructed are P-D0 T16)
    rem:tr-scope	paper/reader/proofs/P-UB3.md@PENDING:1652	P-UB3, text U43a	(iii) concerns the index sets as constructed; ε_ind(h) < 1.45e-19; the lower bounds of (ii) and prop:tr-mu-small for the index sets as constructed (U43a, U43)
    sec:tr-proof	paper/reader/proofs/P-UB3.md@PENDING:1690	P-UB3, text U44a	(iii): lem:uc-admissible with the index sets as constructed; ε_K < μ(h) ≤ μ_G < 0.998ε_Υ in place of N₁ (U44a, U44, U45)
    prop:tr-fail	paper/reader/proofs/P-UB3.md@PENDING:1754	P-UB3, text U46	ε_ind(h) < 1.45e-19 gives more than 1.4268e38, for 0 < |h − h_c| < 1.447e-25
    sec:tr-exceptional	paper/reader/proofs/P-UB3.md@PENDING:1782	P-UB3, text U47	the paragraph after prop:tr-mu-small: exceeds 1.42556e38 for h ≤ 4.71e-20
    sec:introduction-scope	paper/reader/proofs/P-UB3.md@PENDING:1818	P-UB3, text U49	d > 1.403e20 at every choice and 1.2250e27 for the index sets as constructed; d < 1.42556e38 at one choice of the index sets, weights, orders and inner products
    thm:settling	paper/reader/proofs/P-UB3.md@PENDING:1839	P-UB3, text U50	the paragraph after the theorem: d < 1.42556e38, K < 3.13622e39 at one choice of the index sets, weights, orders and inner products
    sec:further-results	paper/reader/proofs/P-UB3.md@PENDING:1861	P-UB3, text U50a	the item on the constants: "of the index sets"; the bounds at other h for the index sets as constructed
    sec:scope-constants	paper/reader/proofs/P-UB3.md@PENDING:1886	P-UB3, text U51	upper bounds at the smaller index sets: d < 1.42556e38, N_NM < 2.99367e39, K < 3.13622e39; the sentence on other h for the index sets as constructed (U51-U53)

Without a crosswalk label: 00-front (U48); the front matter has no labels.


## 7. Checks run

- P-D0's sixteen old texts (md5 1265f3bd…) were matched against chapter 71 at HEAD (md5 bb53f3e8…): each occurs once,
  as whole lines; applied in P-D0's order each still occurs once. The result (md5 1b1056fa…) is the base of the old
  texts above.
- Every old text of section 6 occurs exactly once in its chapter with P-D0 applied, and the texts are pairwise
  disjoint; U1–U10 and U16–U53 also occur verbatim once at HEAD.
- Scratch copy = the working tree (chapters 71, 00, 01, 03 and 90 equal to HEAD) + P-D0 (T1–T16) + U1–U53 (all sixty
  texts, parsed back from this file and applied by matching): `python3 -I lint.py --chapters`: 62 files, 5088
  labels, 0 hits; `python3 -I assemble.py --check`: labels 5088, computations cited 0, problems 0; the
  assembled-paper check (assemble.number, resolve, lint.scan_text with assembled=True) prints `[] 0`. Plain
  `assemble.py` was not run.
- Every new line has at most 121 characters, also after its labels resolve, and no wrapped line starts with "+ ", "- ",
  "* ", "> ", "#", "=" or "|". The new texts name no file, program or code.
- The chain formulas reproduce HEAD's 21 integers at HEAD's inputs and P-D0's two at P-D0's (section 3); all integers
  at the choice are exact, all decimals outward, and every comparison printed in a proof was asserted in exact rational
  arithmetic.

## 8. Merge notes

- Order: P-D0 (T1–T16) first, then these texts; or both together by matching old texts.
- P-D0's fix round has landed in the file (md5 1265f3bd…): T14 and T15 change thm:is-d0, T16 makes thm:tr-transfer (iii)
  take the index sets as constructed, and the new texts of T3 and T5 are revised. No text here touches thm:is-d0,
  lem:is-flat-uses or the first two lines of thm:tr-transfer (iii); U42 replaces only the last two lines of (iii)
  (N₁), so it is disjoint from T16 and applies before or after it. No text here cites thm:is-d0 by its title.
- R-P-D0 m4's list of sites is covered: rem:uc-missing (U21), R_base (U28), sec:cs opening (U23), rem:cs-sharpness
  (U27), prop:tr-fail (U46), the line after prop:tr-mu-small (U47), the sec:tr statements (U41a, U42, U43a, U43, U44a,
  U44, U45), the P-TR sentences in the chapter 71 opening (U2), rem:ec-point-outside (U3a), rem:ec-lb-unbounded (U6a),
  03-theorems (U50a) and 90-scope (U53), and the crosswalk notes of eq:uc-choice and eq:uc-deltas.
- prop:uc-dependence now allows the index sets as constructed (U20), which thm:tr-transfer (iii) uses (P-D0's T16);
  after P-D0's T6 "a choice as in def:uc-choice" alone would name ℰ^φ_ind.
- Not proved here and not claimed in any text: thm:is-flat-serves at h ≠ 10⁻⁶, and any bound for ℰ^φ_ind at other h.
