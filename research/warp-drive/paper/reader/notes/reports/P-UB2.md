# Report P-UB2 (upper-bound chain of ch. 71 as a function of the admissible choice)

Proof file: research/warp-drive/paper/reader/proofs/P-UB2.md — 1946 lines, md5 eb5f55fcc614dcad6625c8778ac03c70.
Old texts from chapters at HEAD (df9a4c35 = f37d0636 for chapters/; 71 md5 427412e02c74261f1f87da24b60ddbca). Nothing
else in the repository edited; nothing committed by me (a coordinator snapshot picked up an intermediate version).

## Inputs and how each output depends on them
Changed by the error: ε_K (every admissible ε_K < 1.67488·10⁻¹⁷), ε_+, N̄_Λ ≥ N_Λ (≈ 9.1·10¹⁴). Unchanged (P-UB1 to
confirm k̄_0, J_*, l_*): ε_Υ = 1.4619·10⁻¹⁰, 𝔡₁ = η_0, k̄_0 = 3, J_* = 15,000,015, l_* = 50 (J′ = 765,000,816),
ℓ⁺_tf = 1, d_BG = 11, r_ι ≤ 16, every per-step charge (497, 469, 466, 20,183, 1,914, 407, 30, 11), W ≤ 1,470,302,
I_lev = 34,268,829,852 (needs only ε_+ < 10⁻¹³). C_lev, C_*, N_ι, M_c, K̄, D_e are outputs.
With u = 1/Δβ_0 = 1/(0.998001ε_K), N̄ = N̄_Λ: L_< = ⌊u⌋, L_> = ⌊(1+ε_K)u⌋ + 1, R_b = L_< + 2; D_e = F_1 ≈ 3u/Δτ_0;
N_ι = (k̄_0+1)N̄ + J′N̄(N̄+1)/2; k̄_max = k̄_0 + J′N̄; d̄_Φ = 62N̄ + 2; C_lev = 2N_ι + N̄ + 529;
I_base = 935R_b + 466 + 23,524,832(R_b+3); R_base = 22,097 + I_base; T_12 = C_lev + I_lev + 4k̄_max + 24;
C_* = 6N_ι + 3N̄ + 3I_lev + 8k̄_max + I_base + d̄_Φ + (N̄+2)(d̄_Φ+30) + 45,862;
D_acc = D_♭ = D_e + 497L_< + L_>C_lev + 469R_b + 466(R_b+1) + C_* (~ J′N̄²u);
D′_* = T_12 + 18 + 20,565,308,337L_< + (C_lev + I_lev − 9)L_> + 2R_base; D_* = T_12 + 14;
d_NM ≤ D_b = D_acc + D_* + d̄_Φ (seminorms of (d)), d_NM ≤ D_NM = D_acc + D′_* + d̄_Φ (both readings, ~2J′N̄²u);
N_NM ≤ 21D_NM + 6; K ≤ 22D_NM + 345; k̄ = 22D_NM + 340, K* < 4k̄² + 48k̄ + 109.
All proved in the drafted texts; new prop:uc-dependence proves the formulas and monotonicity (non-decreasing in N̄_Λ,
k̄_0, J′; non-increasing in ε_K). The formulas reproduce every printed integer of the old chain exactly.

Findings in the step-by-step check: (1) lem:uc-lambda (c) and the proof of lem:cs-fourier (b) used that Λ ∩ {Re ≤ 3+ε_+}
is real — false for the repaired Λ; repaired (order by non-decreasing real part; only "elements of real part ≤ 2 are
real" + (G) is needed). (2) Proved slack, new: only the ≤ L_> levels above 3 cost C_lev, the ≤ L_< below 3 cost 497;
same split in rem:uc-small-reading's recursion. Halves D_♭ and D′_*. Crude D_e + M_c C_* dropped; thm:uc-integer now
states D_acc := D_♭ and D_NM (covers both readings). (3) No other order-changing improvement is proved.

## Provisional evaluation (ε_K = 1.6747·10⁻¹⁷, ε_+ = 1.67475·10⁻¹⁷, N̄_Λ = 910,000,000,000,000)
L_< = 59,831,791,007,643,518, L_> = R_b = 59,831,791,007,643,520; D_e < 1.23382·10²⁷; N_ι < 3.16749·10³⁸;
C_lev < 6.33498·10³⁸; C_* < 1.9005·10³⁹; D_acc < 3.79033·10⁵⁵; D_NM < 7.58066·10⁵⁵; N_NM < 1.59194·10⁵⁷;
K < 1.66775·10⁵⁷ (seminorms of (d): K < 8.3388·10⁵⁶); K* < 1.11255·10¹¹⁵; 3R > 1.2251·10²⁷, D_e < 1.0072·3R;
rem:ec-lb-unbounded threshold h ≤ 6.46·10⁻²⁹. For comparison: crude form 4.5484·10⁵⁶ (K 1.00065·10⁵⁸); old
level-by-level form d_acc 7.58066·10⁵⁵, d_NM 1.51614·10⁵⁶. (At the old inputs the split form would give 2.61926·10⁴⁹.)

## Sites (full table in the proof file §4)
Main set M1–M26 + O1–O4: 00-front:37; 01:156; 03:318–319; 90:77–79; 71: 24–28, 33, 1497–1499, 1810, rem:ec-upper-point,
rem:ec-upper-open, sec:uc-close opening, thm:uc-reduction (iii), lem:uc-lambda, lem:uc-n-iota, prop:uc-explicit,
thm:uc-integer (+ new prop:uc-dependence, eq:uc-levels), rem:uc-missing, sec:cs opening, lem:cs-fourier (b) proof,
lem:cs-levels (b), lem:cs-iterations, lem:cs-rest (2 lines), prop:cs-cstar, rem:cs-sharpness, sec:cs-small notation,
lem:cs-sharp, lem:uc-small-orders (b), (e), rem:uc-small-reading, prop:uc-d-small (b)–(d), prop:uc-data-order (d).
Fallback F1–F9, FO1–FO7 (also 03:363–366, 63:70–71, 63:298–299, 71:425) plus a mechanical rule for the inner lemmas.
P-UB1's (not drafted): rem:gap-sums end, sec:is opening, prop:is-lambda, thm:is-gap, prop:is-count, rem:is-summary,
def:uc-choice, lem:uc-admissible. Outside chapters: PAPER.md, STATUS.md, INTEGRATION.md, proofs/P-TR.md (inherits;
its "N_Λ etc. unchanged in h" fails for the repaired Λ).
Requirements on P-UB1 (R1–R5 in the proof file §1.4): keep eq:uc-deltas (0.999 factors), ε_K < ε_+ < 10⁻¹³;
prop:is-count gives integer N̄_Λ; prop:is-lambda says non-real elements below 3 + ε_+ have Re > 2; thm:is-gap carries
"every ε_K with (G) is < 1.67488·10⁻¹⁷"; ch. 41 names 1 + 𝒵.
All texts: ≤ 121 chars, wrap rule, labels lowercase; scratch lint --chapters 0 hits (main, and fallback + rest).

## Redo with P-UB1's inputs
cd /tmp/claude-0/-home-user-Claude-Method-Works/36602a96-aefb-52fa-89f4-29a4ab038dc7/scratchpad/pub2 &&
python3 mkproof.py EPS_K EPS_PLUS NBAR_LAMBDA [KBAR0 JSTAR LSTAR] --final
(regenerates every number, rechecks, lints scratch copies, rewrites the proof file).
