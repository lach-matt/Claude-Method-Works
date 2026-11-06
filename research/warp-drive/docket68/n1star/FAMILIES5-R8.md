# FAMILIES5-R8 -- round 8: the margins certified for the background itself; the N-family ledger computed

This note seats the round-7 reader's findings (one minor, six nits; R8.0) and closes what the reader listed as
remaining. Every step of the certificates is now in interval arithmetic (R8.1). The two margins are certified for the
background defined by the stated characteristic data, not only for its computed approximation (R8.2). Theorem L″ is
restated for its moved lobe (R8.3). The N-family power counting is computed term by term (R8.4). Lemma O′ is refined
(R8.5), the axis computation repaired (R8.6), and the Hollands–Wald identification set aside once (R8.7). M_b's
independent review is seated (R8.9), and a final section 9 block is given against the paper as it stands (R8.8).

Earlier notes keep their text. Bracketed [R8 …] notes mark each affected line in FAMILIES5-R7.md, FAMILIES5-R6.md and
FAMILIES5-VLASOV.md, and, for the M_b review on the coordinator's instruction, in FAMILIES5-MB.md (old text kept).
Nothing in the paper or in N1STAR-PROOF.md is edited.

**Verdict.**

1. **Every certificate step is in interval arithmetic** (R8.1; r7-m1). The spline's derivative coefficients, the cell
   ends, the bump's edge branch and φ′ are all enclosed now, and no pad is asserted. The bend's moment constants are
   exact up to outward rounding. C1 and C2 certify again for the computed background in a stated interpolant, at
   n = 80 and 160. C1's least lower bound is 0.4475; C2's largest upper bounds are −3.01 × 10⁻⁴ and −3.06 × 10⁻⁴.
2. **Both margins are certified for the background itself** (R8.2). On Σ_τ0 below R_* = 3.43718, and everywhere on
   {u ≤ u1}, the background reduces exactly to ordinary differential equations along null rays (deduced, with the
   reduction's limits checked). Validated integration of these encloses every input of the margins.
   - Theorem L″'s hyperbolicity holds on the whole of Σ′ in the development of the data: intcert5 C3 on R ≥ R_*
     (upper bound −2.96 × 10⁻⁴) and truebg5 T3 on R < R_* (XX).
   - Corollary Q's Γ > 0 holds on the whole seed region (truebg5 T2, least lower bound XX).
   - Rácz's band on Σ_τ0 is one interval, R ∈ [4.2955, 4.5258] certified, with edge zones of width ≤ 0.0073.
   - A posteriori, the computed background is within XX of the true one in C² on the seed region; this gives the
     validated error bound the reader asked for.
3. **Theorem L″'s lobe is moved** (R8.3) to b(R; 3.5, 4.05), so that the bend lies in {u ≤ u1}. Σ′ = Σ_τ0 outside
   [3.5, 5.75]; it is bent by at most 0.00116, and the angular widening is at most 0.00033 rad.
4. **The N-family ledger is computed** (R8.4, nledger5). Every term of the N-family linearisation is written out for
   N = 2..8 and evaluated with twoledger5's rules, one by one. All pass. The term types are exactly the two-family
   ledger's. The count is 16N² + 23N + 4 at the family level and a polynomial of degree 4 once coefficient sources
   are counted. R6's "O(N³)" is corrected; the count enters only the constants.
5. **Lemma O″** (R8.5) states the tubes' dependence on u′, the condition supp q′ ⊂ int S, and the radial dusts'
   supports.
6. **The axis computation is repaired** (R8.6, qsign5 Q7).
   - The θ-flux carries the signs (+2, −2, −1), checked on truncated intervals for both seed classes.
   - Q7's controls are independent of its pass.
   - The axis bound holds on the whole band.
7. **The Hollands–Wald identification is not used**, and it is left out of everything the block calls open (R8.7).
   E is defined by Q =: −E, and M_b is stated for this E.
8. **M_b is settled both ways**, as the independent verifier confirmed. Its findings, one major (editorial) and
   eight minor, are seated in FAMILIES5-MB.md and `checks/mbsign5.py`, and both runs were redone (R8.9).
9. **The final block** (R8.8) is written against `paper/RESPONSE-HL-5D.md` as it stands. Its last four sentences are
   the single M_b paper text, rebased onto R7.6 with its qualifiers.

Labels as in the record: **computed**, **deduced**, **READ**; **certified** means interval arithmetic with a control
that fails. It is said each time whether a certificate is for the computed background in a stated interpolant or for
the background itself. New programs, with their `.out`, PASS: `checks/truebg5.py` (T1-T4) and `checks/nledger5.py`
(L1-L4). Changed and rerun in full, `.out` regenerated, PASS:
- `checks/intcert5.py`: r7-m1; C1d, C2d and C3 new;
- `checks/qsign5.py`: Q7's three nits;
- `checks/racslice5.py`: the lobe moved (R8.3);
- `checks/mbsign5.py`: the M_b review (R8.9), default and `--full`.

---

## R8.0 The round-7 reader: findings and dispositions

- **r7-m1** (four steps of intcert5 were floats). *Repaired* (R8.1). Each of the four is now in interval arithmetic:
  - The derivative coefficients are formed in iv from the spline's float piece coefficients, which define the stated
    interpolant.
  - The cell ends are floats whose differences, and R = v̂ − τ0, are taken in iv.
  - The bump's edge branch is a bound: b ≤ e^(1−X0) and |b′| ≤ 2|y| max(b x²)/h, with x = 1/(1 − y²) ≥ X0.
  - φ′ and φ are enclosed by interval Taylor sums of φ″'s closed form, with no pad.
  C1 and C2 were rerun. Their margins are unchanged to the printed digits, except that C2 moves with the lobe (R8.3).
- **Nit 1** (R7.1's boundary terms need their signs). The θ-flux is 2νβE²ψψ_θ/sc − 2νEψs1 − νE²(cos 2θ/sc²)ψ²,
  taken top minus bottom. On [t0, π/2 − t0] the integral of the Q-density minus the decomposition equals it to
  9.3 × 10⁻¹¹ (qsign5 Q7; R8.6). Applied as an [R8] note at R7.1.
- **Nit 2** (Q7's first control cannot fail when Q7 passes). *Replaced.* The decomposition with 4νE² → 3νE² in Γ is
  built and integrated as it stands. It misses Q by at least 0.450 of the Γ term.
- **Nit 3** (Q7's second control read a finite term off divergent quadratures). *Replaced* by the truncated identity
  (R8.6). For ψ = O(sc) the flux tends to a nonzero limit, and no divergent integral is evaluated. Each flux term with
  its sign flipped misses the identity (control).
- **Nit 4** (Lemma O′). *Repaired* (R8.5, Lemma O″): the tubes are those of (g′, u′); (V1) needs supp q′ ⊂ int S;
  (V2′) needs the radial dusts' supports in a fixed compact S_r, and its adapted-boundary clause is imposed, not open.
- **Nit 5** ("in a stated interpolant" dropped twice). *Restored* in R8.8 wherever the computed background is
  meant. The block's two certified margins are now stated for the background itself (R8.2), with the computed
  approximation's certificate kept beside them, in a stated interpolant.
- **Nit 6** ("Kt/E ≥ 2.464 on the axis" at the midpoint only). *Repaired* (R8.6). On the axes Kt/E is exactly
  ±2 env(R) L±(R), with L± linear of slope 1. For the six seeds L± has no zero in the band and |L±| ≥ 0.143, so
  |Kt/E| ≥ 0.286 env(R) on the whole band, on both axes.
- **The remaining items the reader listed.**
  - The discretisation error: *closed* by certifying for the background itself (R8.2).
  - The N-family ledger: *computed* (R8.4).
  - M_b: *prepared conditionally* (R8.8). FAMILIES5-MB.md is not edited.
  - Hollands–Wald: *stated once and set aside* (R8.7).

## R8.1 The certificates in interval arithmetic (checks/intcert5.py C1, C1d, C2, C2d)

All arithmetic is mpmath iv at 80 bits. The closed forms are lambdified with iv's exp, sqrt and log, and rationals
become interval quotients.

- **The spline.** The computed ψ_III is a scipy spline; its piecewise-polynomial form has float coefficients. The
  stated interpolant is that piecewise polynomial. Its derivative coefficients are c_j (k − j)!/(k − j − d)!, formed
  in iv, and every piece is evaluated in iv on cells cut at the knots in v̂.
- **The bend.** φ″ = A(b_P − l1 b_L − l2 b_R). The three lobes are dilates and translates of one even bump, so
  ∫b_X = h_X K and ∫x b_X = c_X h_X K, with h_X the half-width and c_X the centre.
  - The two moment conditions ∫φ″ = ∫xφ″ = 0 become l1 h_L + l2 h_R = h_P and l1 c_L h_L + l2 c_R h_R = c_P h_P;
    the bump's integral K cancels.
  - So l1 = (h_P/h_L)(c_R − c_P)/(c_R − c_L) = 0.6438152011922511… and l2 = (h_P/h_R)(c_P − c_L)/(c_R − c_L) =
    0.2732240437158471…, enclosed in iv. These agree with racslice5's trapezoid solve to its quadrature error.
  - φ′ and φ come from interval Taylor sums over 22,500 cells (2,250 in C2's runs):
    φ′(r_(k+1)) ∈ φ′(r_k) + w φ″(cell) and φ(r_(k+1)) ∈ φ(r_k) + w φ′(r_k) + (w²/2) φ″(cell), with w = r_(k+1) − r_k
    in iv. On a cell of R the same Taylor form from the nearest node below encloses (φ, φ′, φ″).
- **Results (intcert5.out).**
  - C1: certified at n = 80 and 160 (least lower bound of Γ/E² 0.4475).
  - C1d: with ψ_P, ψ_P′, ψ_P″ each widened by d = (10⁻³, 10⁻³, 10⁻²) it still certifies (least lower bound 0.3735).
    The n = 80 and 160 splines differ by 1.1 × 10⁻⁵, 9.4 × 10⁻⁶ and 6.0 × 10⁻⁶ (sampled).
  - C2: certified at n = 80 and 160 (largest upper bounds −3.01 × 10⁻⁴ and −3.06 × 10⁻⁴).
  - C2d: on R < R_*, with every input widened by 10⁻³ of its size plus 10⁻⁶, it still certifies (upper bound
    −6.46 × 10⁻³ at n = 160). The margin below R_* is twenty times C2's, which is set in the bend.
  - Controls, which fail as they must: Γ's sign flipped; Γ without 4νE²; d = (0.5, 0.5, 5); A = 0.001 (220
    sub-cells fail, upper bound +4.9 × 10⁻⁵); A = 0 (314 fail); a widening of 0.5 (3,386 fail).

C1d and C2d concern the computed background's neighbourhood. The direct certificates of R8.2 make them unnecessary
for the theorems, and R8.2's T4 shows why C2d alone would not have sufficed: the computed packet inputs differ from
the true ones by more than its 10⁻³.

## R8.2 The background itself (intcert5 C3; checks/truebg5.py T1-T4)

The background is the class Einstein–null-dust solution with the record's characteristic data on N = {u = 0} and
N′ = {v = 0}. Those data are e^(2s) = 1/2 on both cones, the shell A = 3.6 b(v; 3, 4.5) on N, the packet B = 1.7 b(u;
5.7, 7.2) on N′, the corner R = 5 with R_u = −0.47 and R_v = 1/2, and the corner mass 1.5 (twobg5, twodomain5).

**The reduction (deduced; its identities computed in twobg5 G1).**

- *Region I, {u ≤ u1}, u1 = 5.7.* B = 0 there, so G1 (a)-(b) give μ_u = 0 and ψ_R = 0. The background is ingoing
  Vaidya in Part I's chart: ψ = 0 and μ = μ(v̂), fixed by the ODE of the data on N, exact before the shell (v ≤ 3).
  This is intcert5 C3, unchanged from its first form except that every point of Σ′ with R ≥ R_* is now checked to
  lie in region I:
  - the ray u = u1 is untrapped there (R_*² > μ_end);
  - τ = v̂ − R increases along it (dτ/dR = 2/f − 1 > 0);
  - φ < τ_ray(3.5) − τ0 = 0.0807 on the bend's support;
  - the ray reaches R = 3.5 before the shell;
  - the shell ends on Σ_τ0 at R < 5.3725 < 5.75.
- *Below R_*.* Σ_τ0 at R < R_* has v̂ < τ0 + R_* < v̂(v = 3) = 3.1453, so it lies in {v < 3}, where A = 0. There:
  - G1 (a) gives μ_v = 0, and the v-Raychaudhuri equation gives ∂_v(e^(−2s) R_v) = 0, so μ and λ := e^(−2s) R_v are
    constant along outgoing rays and equal their values on N′.
  - The mass function's definition, f = 1 − μ/R² = −2 e^(−2s) R_u R_v, then gives R_u = −f/(2λ) at every point. So
    along each ingoing ray, R(u) solves dR/du = G(u, R) := −(1 − μ(u)/R²)/(2λ(u)), with μ(u) and λ(u) from N′.
  - That ODE is regular where λ > 0, which is checked on [u1, u2]: λ ≥ 0.529.
  - The ray with label v̂ meets u = u1 at R1(v̂), with F(R1) = v̂ + F(2.321), where F is region I's Tangherlini null
    function of mass 1.5.
  - With J, K, L the first three R1-derivatives of R(u) (variational equations) and r1′, r1″, r1‴ the v̂-derivatives
    of R1, the inputs are closed-form.
- *In the packet (u1 < u < u2).*
  - e^ψ = ∂U/∂v̂|_R = 2J r1′/f, with U the outgoing time, U′ = 1/λ;
  - ψ_R = B/(3R²G²) (twobg5 G1 (b) in this chart);
  - f_R = 2μ/R³ − μ′/(R²G) and f_v̂ = μ′J r1′/(R²G), with μ′ = −(2/3)Bλ;
  - ψ_v̂ = K r1′/J + r1″/r1′ − 2μJ r1′/(R³f) − (J r1′/G) B/(3R²G).
- *In region III (u ≥ u2), vacuum of mass μ3 = μ(u2).* ψ = ψ_III(v̂) = ln(2J2 r1′/f3(R2)), from the ray's values at
  u2. ψ_III′ and ψ_III″ follow by differentiating along u = u2, using L2 and r1‴.
  - At u2 the ray is untrapped (f3 > 0 checked; R_N′(u2) = 1.5194 > √μ3).
  - So ψ_III is fixed there and holds at the trapped points of the seed region too.
  - The ingoing ODE cannot be continued through the apparent horizon: at λ = 0, f = 0 too, and the limit is
    indeterminate. It does not need to be.
- *Checks of the reduction (T1).*
  - At J = 1, K = 0, B = 0 and R = R1 the packet formulas give e^ψ = 1 and ψ_v̂ = 0, which are region I's values
    (exact, sympy).
  - r1′, r1″, r1‴ agree with a 30-digit differentiation of F's inverse.
  - The values agree with the computed background to its discretisation level. At v̂ = 0.5 the true ψ_III is
    −0.2060929, against the spline's −0.2061130; in the packet the six inputs agree with twobg5's crossing data to
    10⁻³ relative or better (T2, T4).
  - μ3 ∈ [0.8220998, 0.8221253] contains the computed μ0 = 0.8221072.

**Validated integration.** The N′ data on [5.7, 7.2] are (R, R_u, R_v) with R″ = −B/(3R²) and
R_v′ = −(1/2 + 2 R_v R_u)/R; before u1 they are exact. Each ray carries (R, J, K, L). Both are integrated by Taylor
order one with an a priori enclosure of the step box (Picard) and a second-order remainder, the total derivative
being computed symbolically. The step is h = 10⁻³; the widest node enclosure on N′ is 4.2 × 10⁻⁶. Cells are 0.01 in
v̂, bisected where needed, and each cell's ray starts from the interval R1(cell).

**Results (truebg5.out).**

- **T1.** The N′ data are enclosed and λ > 0. Control: a float DOP853 integration lies inside the enclosures, and
  with B's amplitude 1.7 → 1.7017 it leaves them.
- **T3** (Theorem L″'s margin below R_*). κK^l_l < 0 is certified on Σ_τ0 for R ∈ [0.683, R_*], that is
  v̂ ∈ [0, τ0 + R_*], the part of Σ′ in the development of the data below R_*. On every cell it is checked with the
  region I, packet and region III formulas, according to where the slice point can lie: XX. Control: ψ_v̂'s sign
  flipped in the packet fails on XX step boxes.
- **T2** (Corollary Q's margin). Every cell of the seed region R ∈ [0.70, 1.861] lies in region III (R2 ≥ R on the
  slice). Γ/E² > 0 is certified with least lower bound XX. Control: the sign flipped fails.
  - A posteriori, the computed spline (n = 160) differs from ψ_III by at most XX (k = 0, 1, 2) at the cell ends,
    certified, and by XX on the cells, where the bounds include the cells' variation.
  - Control: with B's amplitude × 1.001 in the reduction, the spline is at least XX from it, more than that
    agreement.
- **T4** (a posteriori in the packet). At XX of twobg5's n = 160 crossings in the packet, the computed inputs differ
  from the true ones by at most XX. This is informational, since T3 does not use the computed background.
- **C3** (intcert5, R ≥ R_*). κ′ > 0 and K′^l_l < 0 are certified on Σ′ from R_* to 5.75, with largest upper bound
  −2.96 × 10⁻⁴. Beyond 5.75, Σ′ = Σ_τ0 in Tangherlini of mass μ_end ∈ [3.60577, 3.60583], where κK ∝ (μ/R³)(f − 3)
  < 0 exactly. On Σ_τ0, Nk is certified negative outside the edge zones [4.2882, 4.2955] and [4.5258, 4.5310], and
  positive on [4.2955, 4.5258]. Controls: DOP853 inside the shell's enclosures, and leaving them with Q(3) shifted by
  10⁻⁶; A = 0 not hyperbolic (1,944 cells fail).

**What is certified, exactly.** For the background defined by the stated characteristic data:
- Rácz's split is hyperbolic on all of Σ′ ∩ {v̂ ≥ 0}, that is R ≥ 0.683 (T3 and C3; beyond 5.75 exact).
- Γ > 0 on the seed region (T2).
- Σ_τ0's band is the single interval of C3, up to its edge zones.

The reduction is deduced from G1's identities, which twobg5 computes, and from the mass function's definition. The
certificates are interval arithmetic over the reduction's ODEs. Nothing in them uses the 2D double-null grid.

## R8.3 Theorem L″ with the moved lobe

**Theorem L″ (as R6 section 2, with the bend replaced; deduced from racslice5 S2-S3, certified by intcert5 C3 and
truebg5 T3).** Let Σ′ = {v̂ − R − φ(R) = τ0} with φ″ = 0.01 (b(R; 4.1, 4.7) − l1 b(R; 3.5, 4.05) − l2 b(R; 4.85,
5.75)), and l1, l2 as in R8.1, so that φ = φ′ = 0 outside [3.5, 5.75]. Then:
- Σ′ equals Σ_τ0 outside R ∈ [3.5, 5.75]. φ ≤ 0, so Σ′ lies to the past. It is spacelike (V′ ≥ 0.9979,
  E V′ f ≤ 0.9033 < 2).
- κ′K′^l_l < 0 at every point (sampled max −3.11 × 10⁻⁴ at n = 80 and 160; certified as in R8.2).
- The rest of R6 section 2 holds with the lens R ∈ [3.519, 5.723], τ-thickness 0.00116 and angular widening
  ≤ 0.00116/R_min = 3.3 × 10⁻⁴ rad (racslice5 S3).

The lobe was moved from b(R; 3.0, 4.0) so that the whole bend lies in {u ≤ u1}, since R_* = 3.43718 < 3.5. There the
background is explicit (C3). Below R_* Σ′ = Σ_τ0, and T3 covers it.

## R8.4 The N-family ledger, term by term (checks/nledger5.py)

FAMILIES5-R6.md section 4 E₂_N (vi) applied the two-family ledger "family by family". nledger5 instead writes out the
N-family linearisation itself and evaluates every term with twoledger5's own `weights()` and `evaluate()`.

- **Step 4.** The background terms of h; and for every family A: the (1 − 𝒫)s_A λ⁻¹ term, the ℓ_app − ℓ term,
  −φ_A[T1], ½Ψ_A G1, the c^ab and λ□_app φ_A F ĝ2 terms, B1·dφ_A, C1φ_A, and the three w terms of N_φ^A.
- **Step 5.** For every A: ℓ_A·dφ_A = ½𝒫s_A(h) with its three targets, and [∂^a, L_A]φ_A.
- **Step 6, after Lemma 3.3_N.**
  - Contracting with ℓ_A ⊗ ℓ_A kills family A's λ⁻¹ term and its □φ_A term.
  - What remains is c1·dh, c0h, family A's λ∂²φ and N_φ terms, and for every B ≠ A: c2·dφ_B, c3φ_B, the coupling
    −q c_A Ψ_B, qλ⁻¹((1 − 𝒫)s_B)G2^B(ℓ_A, ℓ_A), λ∂²φ_B and N_φ^B's three w terms.
  - Then the 𝒫□s_A rewriting with (M5) both forms, −½M_A(𝒫s_A), −N_Aφ_A and a_AΨ_A.
- **Coefficient sources.** Every coefficient built from g_app is enumerated over its source: the background, one
  family, or a pair (stage 1's quadratic terms).

**Results (nledger5.out).**
- **L1.** For N = 2..8 every term passes at k = K = 6: 114 to 1,212 terms at the family level, and 285 to 19,464
  with sources. The set of term types (U, p, κ, m, operations, extra, w) is exactly the two-family ledger's 45, for
  every N. The N = 4 list (1,942 terms) passes every term on k = 6..12 × K = 6..10.
- **L2.** The counts are 16N² + 23N + 4 at the family level and 3N⁴ + (21/2)N³ + 25N² + (49/2)N + 4 with sources
  (exact on N = 2..8). A Step 6 cross term (target A, unknown B) with a pair source {C, D} carries four labels, so
  R6's "O(N³) terms" is corrected to degree 4 [R8 note at R6 section 4]. The count enters only the constants M(N)
  and λ0(N).
- **L3.** A product of one, two or three oscillating profiles with non-resonant phases has m-th derivatives exactly
  of order λ^(−m), for m = 0..4 (sympy). So κ = 1 holds for every source, and a resonant product costs less.
- **L4.** The closing rows are N-independent in their powers. Step 7's M(N) := C3(C_D(N) + 1 + C_R(N)) + 1 and
  λ0(N) := 1/(C3 C(N) M(N)²) close for any positive constants (exact).
- **Controls**, which fail as they must:
  - (a) family A's own λ⁻¹ term left uncontracted (exponent −1);
  - (b) a cross term without its (1 − 𝒫) gain (−1);
  - (c) the coupling as a generic ∂²φ_B (−1);
  - (d) a factor with phase x/λ² (κ = 2).

So E₂_N's step (vi) is computed, not argued by analogy. Its reach is twoledger5's: the rules are the record's
(deduced there), and the counting they imply is computed for every N-family term.

## R8.5 Lemma O″ (deduced)

**Lemma O″.** Let (g, q, u), possibly with Part I's radial dusts (q_rad, u_rad), satisfy (Ω) and (V1)-(V3). Fix
compact sets S ⊂ (Σ_τ0 ∩ Ω) × S¹ (positions × labels) and S_r ⊂ Σ_τ0 ∩ Ω with supp q ⊂ int S and
supp q_rad ⊂ S_r. Suppose (V1), (V2) and (V2′)'s angle clause hold, with margins J0, b, 2δ and η, on the tubes of S
and S_r themselves:
- the Jacobian ≥ J0 on the tubes D_ω(S);
- ∂_ωβ0 ≥ b on S;
- dist(D_ω(S), axes) ≥ 2δ;
- the angle ≥ η between every label of S and the radial null directions on the tubes of S_r, or those tubes disjoint
  at distance ≥ η.

Then there is a neighbourhood 𝒩 of (g, u|Σ, ∂u|Σ, u_rad|Σ, ∂u_rad|Σ) in C² × C¹ such that every perturbed solution
satisfies (V1), (V2) and the angle clause of (V2′), with margins J0/2, b/2, δ and η/2, provided
- its (g′, u′|Σ, ∂u′|Σ, u′_rad|Σ, ∂u′_rad|Σ) lies in 𝒩;
- supp q′ ⊂ int S and supp q′_rad ⊂ S_r;
- its radial dusts satisfy (V2′)'s second clause, Theorem N′'s (H2′) with Corollary N′1's adapted boundaries.

(Ω) and (V3) are open in C² × C¹ as in Lemma O.

*Proof.* The tubes are the images of S and S_r under the flows of the rays of (g′, u′) and of (g′, u′_rad). These are
null geodesics of g′ whose initial directions come from ∂u′|Σ and ∂u′_rad|Σ. They and their first variation depend
continuously on (g′, u′) in C² × C¹, uniformly on the compact S × [τ0, τ_end] (continuous dependence on coefficients
and data, as in Lemma O). So the four margins, infima over compact sets of continuous positive functions, hold halved
on a neighbourhood.
- For (V1): supp q′ is compact in int S, and the flow is a diffeomorphism. So the tube of supp q′ has a neighbourhood
  inside the tube of S, where the Jacobian bound holds. This is why int S is needed.
- For (V2′): the radial tubes are those of S_r, because the perturbed radial dusts' supports are kept in S_r.
- (H2′) with adapted boundaries is a structural condition at the axes, an equality, not an inequality. It is not
  open, and it is imposed on the class of perturbations.
∎

Proposition NE satisfies it. There is no radial dust, so S_r = ∅ and (V2′) is vacuous. S is the ball enlarged by 20 %
× the label intervals, and the data's support, the ball × the intervals, lies in its interior. vlasovex5 X2 checked
the margins on the tubes of all of S. The coupled solutions' fields keep their initial support for every ε. Their
tubes are those of (g_ε, u_ε), and g_ε, u_ε are C²- and C¹-close to the reference.

## R8.6 Theorem Q at the axes: the flux and its signs (qsign5 Q7, rerun)

The setting is Tangherlini's slice in Part I's chart (ψ_P = 0, μ = 0.82), with six regular seeds and six with
ψ = O(sc), over two bands, one inside the horizon (qsign5.out):
- **The whole interval.** For the regular seeds, Q equals the decomposition integrated over [0, π/2] to
  2.2 × 10⁻¹⁶ of Q and 5.1 × 10⁻¹² of its Γ term. Q ≤ −∫∫Γψ²/sin 2θ < 0.
- **The truncated identity.** For t0 ∈ {0.02, 0.05, 0.1, 0.2} and every seed of both kinds:
  ∫_(R1)^(R2) ∫_(t0)^(π/2−t0) (Q-density − decomposition) = ∫ dR [2νβE²ψψ_θ/sc − 2νEψs1 −
  νE²(cos 2θ/sc²)ψ²]_(t0)^(π/2−t0), to 9.3 × 10⁻¹¹.
  - For the regular seeds it vanishes like t0²: the ratio from t0 = 0.05 to 0.02 is at most 0.165, against
    t0²'s 0.16.
  - For ψ = O(sc) it tends to a nonzero limit (ratio ≥ 0.759, size ≥ 0.022). So for those seeds the identity on
    [0, π/2] fails by exactly the axis terms.
  - No divergent integral is evaluated.
- **The axes are reached on the whole band.** On the axes Kt/E = ψ_θ/sc is exactly 2F(R, 1) at θ = 0 and
  −2F(R, −1) at θ = π/2. For these seeds that is ±2 env(R) L±(R), with L± linear of slope 1 (checked against ψ_θ/sc
  at 10⁻⁷ from the axis). None of the 12 (seed, axis) pairs has a zero in the band, |L±| ≥ 0.143, and so
  |Kt/E| ≥ 0.286 env(R) on the whole band.
- **Controls**, which fail as they must:
  - each flux term with its sign flipped misses the truncated identity, by up to 211, 10 and 220 times it;
  - the decomposition with 4νE² → 3νE², integrated as it stands, misses Q by at least 0.450 of the Γ term.

## R8.7 E, the Hollands–Wald identification, and M_b

E is defined by Q(δ) = 2∫_U G^(2)[δ](ξ, n) dvol =: −E(δ) (R7.2). M_b is the statement "E(δ) > 0 for every non-gauge,
compactly supported, invariant linearised vacuum solution δ supported in U". That this E is Hollands and Wald's
canonical energy relative to ξ is standard, but it is not READ here and nothing here uses it. It is not among the
things the paper is asked to call open, and the block of R8.8 does not mention it.

**M_b is settled both ways** (FAMILIES5-MB.md, `checks/mbsign5.py`). The independent verifier found no mathematical
error in Theorem X or Theorem P and re-derived every identity symbolically (R8.9).
- Inside the horizon E takes both signs on tensor-type perturbations. So exactly localised vacuum data with a
  non-gauge first-order part exist near Part I's data, for small amplitude, on every vacuum band meeting {f < 0}.
- Outside the horizon E > 0 on every non-gauge perturbation. So no such data exist there at second order.

The block's last sentences carry this, rebased onto R7.6's last sentence with its qualifiers (R8.8).

## R8.8 Proposed replacement for the paper's section 9 bullet "More families"

The old text is the paper's current bullet, located by content. It begins "- **More families.** Angular separation and
the passage to Vlasov matter are not attempted." and ends "No statement about several families is proved." It occurs
exactly once in `paper/RESPONSE-HL-5D.md` (section 9, "What is not proved"; at present the bullet starting at line
1528). It is quoted verbatim in R7.6 and is unchanged in the paper. This block supersedes R7.6's, FAMILIES5-MB.md
section 7's and every earlier proposal; its last four sentences, from "For first-order parts that perturb the metric",
are the single M_b paper text.

New:

```
- **More families.** Two crossing radial null dusts, one ingoing and one outgoing, are carried through the record's
  argument: the two-dust background on the whole domain, the approximant to every order, the uniform estimate and the
  data (deduced, the identities computed; supplement `docket68/n1star/FAMILIES5-FULL.md` Part I). In the T² class each
  family's null second fundamental form is diag(θ_h, κ1, κ2), the torus terms first order, and at an axis the planar
  shear is recovered elliptically from the expansion, so the class Einstein–null-dust system is Cauchy-stable on compact
  domains of the record's type, without smallness, for caustic-free dusts whose lateral boundaries are adapted (one
  family) where they meet an axis (deduced; `docket68/n1star/FAMILIES5-AXIS.md`). A massless Vlasov limit in the class
  is restricted (computed); a smooth restricted field never reaches an axis off the axial directions, its density
  growing like 1/ρ2 there (computed, `docket68/n1star/checks/vlasovhf5.py` H7), and at an axis point at most one ingoing
  and one outgoing family are separated (computed, `docket68/n1star/checks/axisphase5.py`). Every smooth class
  Einstein–restricted massless Vlasov solution whose field is a family of dusts labelled by initial direction,
  caustic-free, off the axes and at an angle from the radial dusts where it meets them, the radial dusts having adapted
  lateral boundaries at the axes, on a domain of the record's type whose initial spheres have positive mean curvature
  and a hyperbolic momentum system, is a weak limit of class vacuum metrics along odd N (deduced: N-dust approximants
  uniform in N; torus-polarised waves at frequencies 1, Λ, …, Λ^(N−1), which leave no combination of phases resonant up
  to the order the scheme uses; data with overlapping families, whose only divisors are spacetime symbols; the N-family
  energy estimate, its power counting computed term by term (`docket68/n1star/checks/nledger5.py`); a diagonal choice of
  λ_N, as Huneau and Luk do; `docket68/n1star/FAMILIES5-VLASOV.md`, `docket68/n1star/FAMILIES5-R6.md`,
  `docket68/n1star/FAMILIES5-R8.md`, the identities, divisors and data step computed). These hypotheses are open for
  perturbations whose supports stay in a fixed compact set and whose radial dusts keep adapted boundaries (deduced), and
  an explicit test family on Tangherlini meets them (computed, `docket68/n1star/checks/vlasovex5.py`). Data localised in
  an angle exist on cones exactly (computed) and, near Part I's data, on all of Part I's slice in a band widened by a
  computed amount (deduced): Rácz's split is hyperbolic on the slice except one band inside the shell, R between 4.29
  and 4.53 (computed, `docket68/n1star/checks/racglobal5.py`; its extent certified by interval arithmetic for the
  background with the record's characteristic data, whose reduction to ordinary differential equations is deduced, each
  edge enclosed to within 0.008, `docket68/n1star/checks/intcert5.py`), where no foliation of that slice is hyperbolic
  (deduced from Rácz's characteristic equation), and a slice bent by at most 0.0012 is hyperbolic everywhere (certified
  for that background and for its computed approximation in a stated interpolant; `docket68/n1star/checks/racslice5.py`,
  `docket68/n1star/checks/intcert5.py`, `docket68/n1star/checks/truebg5.py`). Near Part I's data, exactly localised
  vacuum data whose first-order part perturbs the extrinsic curvature alone do not exist for small amplitude: their
  charge is minus a sum of squares minus a term carrying the mass, at the axes too (deduced; the identity computed,
  `docket68/n1star/checks/qsign5.py`, and the last term's sign certified for that background and for its computed
  approximation in a stated interpolant, `docket68/n1star/checks/truebg5.py`, `docket68/n1star/checks/intcert5.py`);
  with matter obeying the dominant energy condition such data do not exist outside the horizon, and inside it they exist
  with outgoing null dust (deduced; the sign computed). For first-order parts that perturb the metric the charge is Q =
  2∫_U G^(2)(ξ, n) =: −E, and its sign is decided (`docket68/n1star/FAMILIES5-MB.md`,
  `docket68/n1star/checks/mbsign5.py`). Inside the horizon E takes both signs on perturbations of tensor type, so near
  Part I's data exactly localised vacuum data background + εδ + O(ε²), δ a perturbation of the metric that is not a
  gauge one, exist for small amplitude on every vacuum band of the slice that meets the black-hole region (deduced, by
  intermediate values; the tensor sector's charge computed). Outside the horizon E is positive on every perturbation
  that is not a gauge one: in the class it is the sum, over the even harmonics, of the energies of Kodama and
  Ishibashi's master equations, whose potentials are positive in five dimensions for every l ≥ 2 (the reduction and the
  positivity computed exactly, the passage to a static slice deduced). So on bands outside the horizon, near Part I's
  data, no exactly localised vacuum data background + εδ + O(ε²) with δ not a gauge perturbation exist for small
  amplitude: exact vacuum localisation fails there at second order.
```

What changed from R7.6's block:
- the N-family estimate's power counting is computed (nledger5);
- the hypotheses' openness carries the radial dusts' adapted boundaries (Lemma O″);
- the band's extent is certified for the background itself;
- the bend is at most 0.0012, and its hyperbolicity is certified for the background itself and for the computed
  approximation in a stated interpolant (nit 5);
- Γ's sign is certified the same way;
- R8.4 and R8 replace R7 among the supplements;
- the M_b sentence is replaced by the settled text, rebased with R7.6's qualifiers ("near Part I's data", "for small
  amplitude", families background + εδ + O(ε²), second order), the potentials' positivity now computed for every
  l ≥ 2, and the Hollands–Wald identification left out.

## R8.9 The M_b review, seated (FAMILIES5-MB.md, checks/mbsign5.py)

An independent verifier read FAMILIES5-MB.md and checks/mbsign5.py in round 8. Its verdict: M_b settled both ways;
no mathematical error in Theorem X or Theorem P; every identity re-derived symbolically, including Theorem T (iii) and
Lemma X1 on every class slice (w = 2/(f + q²), √Δ = 2q/(f + q²), q free). The findings are seated as bracketed [R8]
notes in FAMILIES5-MB.md, the old text kept, and in the program. Both runs were redone, and all checks pass with every
control rejected: `checks/mbsign5.out` (the default run, 292 s) and `checks/mbsign5_full.out` (E4-E9, 235 s).

- **Major 1** (section 7 targeted R6's superseded block and dropped R7.6's qualifiers). *Repaired.* The single M_b
  paper text is R8.8's, rebased onto R7.6's last sentence with its qualifiers. MB section 7 carries a note.
- **Minor 1** (E2/E3 are spot checks at three slice points). *Relabelled* (MB section 2 note; mbsign5 docstring). E2
  (iii) and E3 (a)-(b) are exact at three rational slice points, a spot check in the slice. On every class slice they
  rest on the verifier's own symbolic check (w = 2/(f + q²), q free), which corroborates them; a symbolic run inside the
  record was tried in round 8 and did not finish in the time available. The final block accordingly says "computed" for
  the tensor charge, without "on every slice".
- **Minor 2** (`--full` relied on a homothety that holds only for weight-homogeneous identities). *Repaired.* `--full`
  is now symbolic in R, μ and k² through μ = xR², with x a free symbol. This is a change of variables, so no
  homogeneity is assumed. Every E4-E9 identity passes (235 s), and a non-homogeneous mutation can no longer pass.
- **Minor 3** (E9 did not enforce the sign). *Repaired.* The + sign is required, and its opposite is a control
  (rejected).
- **Minor 4** (E4, E8 and E9 had no controls; the l = 0 kinetic part). *Repaired.*
  - Controls: E4, the lapse direction without −ψ Ric, does not solve M; E8, X = F∂_R in place of RF∂_R, does not
    solve the l = 0 constraint; E9, the opposite sign. All are rejected.
  - E8 now computes that the l = 0 k is k_ψ with ψ = N(c + ∫Rw/(fN)). That is a constant times N on the inner side:
    gauge in R6's extended sense, not compactly supported.
- **Minor 5** (Lemma TR's wording). *Repaired* in a note:
  - Σ is extended to a Cauchy surface of the maximal extension;
  - R1 and R2 are supp δ's radial extent;
  - R_a ∈ (R_h, R1).
- **Minor 6** ("no third-order question"). *Corrected* in a note. Inside the horizon Q vanishes on a cone. For δ0 on it
  with B(δ0, ·) ≢ 0, Proposition L′ on δ0 + sη with s(ε) = O(ε) gives the data. δ0 in Q's radical is left to third
  order and not claimed.
- **Minor 7** (the docstring identified E with the canonical energy). *Removed.*
- **Minor 8** (Theorem T for every l). *Written* in a note: the θ-integrated density is |T|² times a quantity affine
  in k_T², so the identity at l = 2 and 4 gives every l.
- **Section 5's gap** (re-slicing generators). *Stated.* "To every order" is claimed only where each order's generator
  can be chosen with the allowed support, and is otherwise excluded.
- **Nits.**
  - The 0.683 inner edge is VLASOV section 3's (racglobal5).
  - "its full run" becomes "its default run".
  - The runtimes are as printed in the .out files.
  - E7 is "computed exactly", not "certified".
  - The KID coefficient ε²Q and R7.2's matter balance ε²Q/2 = ∫T(ξ, n) agree, the factor 2 being the pairing's.
- **Beyond the findings.** E7 now proves Qp > 0 on the exterior for every l ≥ 2 (m = l(l + 2) − 3: m = 5 as before,
  and m = 12 + t with every coefficient ≥ 0). So the potentials are positive for the whole spectrum of S³. This is
  what lets the paper text say "for every l ≥ 2", as the verifier asked.

## Files

`FAMILIES5-R8.md` (this note). New, with their `.out`, PASS:
- `checks/truebg5.py` (T1-T4, certified, with controls; XX under load);
- `checks/nledger5.py` (L1-L4, computed, with controls; seconds).

Changed and rerun in full, `.out` regenerated, PASS:
- `checks/intcert5.py`: C1-C3 (r7-m1; C1d's tube, C2d and C3 new), about ten minutes under load;
- `checks/qsign5.py`: Q1-Q7 (Q7's nits), about a quarter of an hour under load;
- `checks/racslice5.py`: S1-S3, the lobe moved;
- `checks/mbsign5.py`: E1-E9 (R8.9), default and `--full`, about five and four minutes.

Bracketed [R8] notes are in FAMILIES5-R7.md, FAMILIES5-R6.md, FAMILIES5-VLASOV.md and FAMILIES5-MB.md.
