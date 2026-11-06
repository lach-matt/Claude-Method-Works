# INVERSE5-SIX -- the six inverse bounds behind lambda1 and delta, made explicit as far as is true

*Status.* Written 2026-11-06 for workstream D of `paper/RESPONSE-HL-5D.md` (CONSTANTS5.md rounds 6-9, item (iii)); not
yet read by a verifier. It takes the six inverse bounds that CONSTANTS5.md R6.3 (b), R7.4, R8.4 and R9.5 leave open
with the stated missing input "their microlocal constants at L_b0, plus certified spectral bounds in the write-out's
norms": I.B:1513, I.B:1685, I.B:1978, III.F'':223, III.D:365 and II.F:1393 (the seventh, I.C:497's scalar-type blocks,
is INVERSE5-SCALAR.md's and is not touched here). For each it states the bound and its norms (READ at the site), what
its proof's constant is made of, what is proved, computed or deduced here, and the explicit constant or the exactly
stated input at which it stops. CONSTANTS5.md, N1STAR-PROOF.md and the paper are not edited; section 7 proposes old/new
text for CONSTANTS5.md R9.7 block 2 and R9.5.
[R4: read since by two verifiers (report-vINV.md, report-vINV2.md, no Major); rounds 3-4 seat their findings on this
file; section 7 and R2.2 are superseded (R2.2 by CONSTANTS5.md R12.7).]
[R5: read by a third (the confirming reader of round 4: no Major, no minor; Round 5); CONSTANTS5.md R12.7 is itself
superseded by its R13.7, so R2.2 is now superseded by R13.7.]

*Programs* (new; each with `--selftest`, named checks, failing controls, full run in its `.out`):
`checks/inverse6_5.py` (the microlocal constants at L_b0 and the replacements' arithmetic; 17/17: K1-K8, controls
C1-C9; about a minute) and `checks/inverse6_5m.py` (certified spectral bounds for the mode-decomposed operators;
12/12: M0-M7, controls C1-C4; about two minutes). Imported, not copied: `strap5.py` (III.F (4.2)'s matrix A),
`e2certify5.py` (r_*(t), decimal rounding), `modes5.py` M2-M3 and `gmodes5.py` G1 (the master relations, rerun inside
M7).
[R4: now 17/17, 13/13 (control C5 added in round 3) and, for the companion `checks/inverse6_5a.py` of round 2, 11/11;
each exits 1 on a failed check in either mode; about three and five minutes under load (R4.5).]

*Labels.* Proved (a lemma with its proof here); computed (exact, sympy or exact rationals); certified (interval
arithmetic, mpmath.iv at 30-40 digits, printed decimals rounded outward; given mpmath.iv's correctness, as in
E2-PILOT); deduced (from cited statements of the record); READ (a cited line). Units: five-dimensional Tangherlini
at mu = 1 (r_h = 1, r_ph = 2^(1/2)), as every instrument of the record; nu, gamma_+-, kappa scale as mu^(-1/2), the
rest is homothety invariant.

## 0. Summary

- **B1, I.B:1513** (Prop. 6.4, (6.6), the trapping estimate with loss 1). Non-constructive: a defect-measure
  contradiction gives no (C, h_0). Here: the (Gamma.1)-(Gamma.4) data at b0, exact; lam_max(p_1^Gamma) for 2 L_b0,
  certified, with its exact leading order; the admissible fibre metrics and their condition numbers. Stops at: an
  explicit (C, h_0) in (6.6).
- **B2, I.B:1685** (Prop. 6.7, the absorbed inverse). No non-constructive step of its own. Here: absorption at
  h_0 = (2 C_a)^(-1/N) and (6.11) with the constant 4 F C_a, F <= 1.002659 (certified). Stops at: C_a, the a priori
  constant of Prop. 6.7 (a).
  [R3: "no non-constructive step of its own" holds at b0, for one operator; the constants uniform over b in B_*-bar
  come by compactness and contradiction (I.B section 9), R3.2. With R3 (a)'s notation the constant is 8 F C_a, R3.3.]
  [R4: the absorption threshold is h_0 = min(h_ch', (2 C_a)^(-1/N)), h_ch' the threshold of Prop. 6.7 (a)'s own chain,
  which contains (6.6)'s h_0 (R4.1).]
  [R5: this h_0 is the chain's threshold and the absorption threshold together, not "the absorption threshold".]
- **B3, I.B:1978** (Thm 1.3 (3), high-energy invertibility). No non-constructive step of its own. Here: the inverse
  bound is 2 C_8.1 |sigma|^(-1+delta) with C_0 explicit in C_8.1; every threshold the chain reads, computed. Stops at:
  C_8.1, the chain constant of Prop. 8.1.
  [R3: the bound carries the factor (1 - nu'^2)^(-(1-delta)/2) when h = |Re sigma|^-1 and holds in the h-dependent
  semiclassical norms, not uniformly in X_sigma's (R3.1); "no non-constructive step" holds at b0 only, and even there
  Prop. 8.1's finite cover and nu_1 are compactness choices (R3.2).]
  [R4: C_0 is not explicit in C_8.1 alone: C_0 = min(h_ch, (4 C)^(-1/N), (4 C C_K)^-1)^-1 (1 - nu'^2)^(-1/2), h_ch the
  threshold of Prop. 8.1's own chain, which contains B1's h_0; "2 C_8.1" here is twice the constant before absorption
  (R4.1, R4.2).]
- **B4, III.F'':223** (Prop. 3.1, L_b0 at sigma != 0). Non-constructive: Fredholm index 0 and injectivity. Here:
  certified cut-off bounds for every Kodama-Ishibashi master operator at every l and every real sigma != 0; the exact
  transfer to the tensor-type blocks; a gluing lemma. Stops at: the gauge reconstruction of the vector and scalar types,
  and C_ext(sigma), the absorbed problem's inverse in the write-out's norms.
- **B5, III.D:365** (Prop. 6.2, box on 1-forms at sigma != 0). The same, with V_0, V_1, V_2 certified and the exact
  transfer to the vector-type blocks. Stops at: the scalar-type reconstruction, and C_ext(sigma).
- **B6, II.F:1393** (Lemma 5.2, the weak-remainder estimate). Non-constructive: a Hahn-Banach projection and the open
  mapping theorem. Here: eliminated; (5.5) holds with max(||Q'||, ||R'||) of the parametrix its proof already builds.
  Stops at: the two parametrix norms (and, downstream of the site, the inverse of N^0(sigma)).

No lower bound for lambda1 or delta follows yet; the upper bounds stand (log10 delta < -7.6666e16, lambda1 < delta).
What changed: one of the six (B6) needs no inverse bound, two (B2, B3) have no non-constructive step of their own and
reduce to the trapping estimate's constant and the calculus constants, the trapping estimate's symbol data are now
numbers, and the two mode-stability bounds (B4, B5) have their spectral input certified harmonic by harmonic.
[R4: "no non-constructive step of their own" holds at b0, for one operator, Prop. 8.1's cover and nu_1 aside; the
uniformity over b is by compactness and contradiction (R3.2); and their thresholds contain the chains' own (R4.1).]

## 1. The six, read

- **B1, I.B:1513** (PART-I-B-HIGHENERGY.md:1499-1592, Proposition 6.4). For beta > gamma_- and U near Gamma there are
  B, E, G in Psi^0 microsupported in U with, for z in z_0 + i[h beta, nu'] and h < h_0,
  ||Bu|| <= C (h^-2 ||G P u|| + h^-1 ||Eu|| + h^N ||u||_(-N)) (6.6), semiclassical L^2 and H^(-N)_h norms.
  The proof supposes (6.6) false for every C and extracts a defect measure (line 1513, "after passing to a
  subsequence"); Steps 1-4 use the data of (Gamma.1)-(Gamma.4): nu_min, {phi_u, phi_s} (Step 2's c_Gamma),
  q^Gamma, p_1^Gamma in the fibre metric h_Gamma, gamma_+-, and Proposition 4.5/Corollary 4.6. It yields no (C, h_0).
  Theorem 6.8, Proposition 6.7 (a) and Proposition 8.1's kind (Gamma) use (6.6); so every high-energy bound does.
- **B2, I.B:1685** (lines 1663-1696, Proposition 6.7). P'_(h,z) : H^(2,0,0)_h -> L^2 is invertible for
  z in z_0 + i[h beta, h beta'], h < h_0, with ||(P'_(h,z))^-1|| <= C h^(-1-(beta' - Im(z/h))/(beta' - beta)) (6.11).
  (a) is an a priori estimate ||u|| <= C_a h^-2 ||P'u|| + C_a h^N ||u||_(-N 1) from Prop. 4.2, Cor. 4.6 and (6.6); (b)
  is "Fredholm, and by (a) injective" (line 1685), which loses nothing: the inverse bound is (a)'s constant; (c)
  interpolates with Lemma 6.6.
- **B3, I.B:1978** (lines 1963-1978, Theorem 1.3 (3)). P-hat(sigma) : X_sigma -> Y_sigma is invertible for
  Im sigma >= 0, |sigma| >= C_0, the orders read at h = |Re sigma|^-1 (variable-order semiclassical scattering Sobolev
  spaces through the artificial boundary). "Fredholm, so it is invertible": the inverse bound is (1.6)/(8.1)'s,
  ||P-hat(sigma)^-1||_(Y_sigma -> X_sigma) <= C_8.1 |sigma|^(-1+delta), and C_0 = h_0^-1 comes from the absorption at
  the end of Proposition 8.1 (a). CONSTANTS5.md R4.4 and R8.4 assign the "middle range" sigma_0 <= |sigma| <= sigma_1
  to this site; the statement at the site is |sigma| >= C_0, and the band below C_0 is B4's and B5's (and III.D''s
  for box^Ups), by mode stability.
  [R3: read "<= 2 C_8.1 (1 - nu'^2)^(-(1-delta)/2) |sigma|^(-1+delta) in the semiclassical norms at h = h(sigma)",
  R3.1.]
  [R4: here C_8.1 is the record's constant of (8.1), after absorption, twice R3 (b)'s C; the bracket's "2 C_8.1" is
  read "C_8.1" in that sense (R4.2), and C_0 also comes from Prop. 8.1 (a)'s own h_0 (I.B:1881), not from the
  absorption alone (R4.1).]
- **B4, III.F'':223** (PART-III-F3-MODES.md:219-245, Proposition 3.1). For sigma != 0, Im sigma >= 0,
  L-hat_b0(sigma) : X_sigma -> Y_sigma is invertible; "Fredholm of index 0, so injectivity suffices" (line 223), and
  injectivity is shown type by type: box^C's mode stability, the Kodama-Ishibashi master equations (Theorem 2.2),
  box^Ups's mode stability, Gronwall inside the horizon. No inverse bound.
- **B5, III.D:365** (PART-III-D-GAUGEPOT.md:362-410, Proposition 6.2). The same for box on 1-forms, through the
  three ODE steps (a) scalar (V_0), (b) Maxwell (V_1 vector type, V_2 scalar type, l = 0 by M_r), (c) gauge (Cartan).
- **B6, II.F:1393** (PART-II-F-IOTA.md:1393-1403, Lemma 5.2). If T : X -> Y is Fredholm and j : X -> W continuous
  injective, ||x||_X <= C (||Tx||_Y + ||jx||_W); the proof builds a projection Pi onto ker T from Hahn-Banach
  functionals and applies the open mapping theorem on ker Pi: C = ||Pi|| + (1 + ||Pi||)/sigma_min(T on ker Pi),
  unbounded at fixed ||T|| (baire5.py K3). Its only use is Lemma 5.5 (b) (line 1534), estimate (5.5) for the compact
  model P-hat = chi_3 L_sigma + (1 - chi_3) Delta at iota+, which feeds Lemma 5.6 and Proposition 5.1.

## 2. The effective replacements (proved)

**Lemma R1 (a parametrix gives the weak-remainder estimate).** Let X, Y, Z be Banach spaces, T : X -> Y and Q' : Y ->
X bounded, and suppose R' := I - Q'T extends to a bounded map Z -> X, with X -> Z continuous. Then for x in X,
||x||_X <= ||Q'||_(Y->X) ||Tx||_Y + ||R'||_(Z->X) ||x||_Z.
*Proof.* x = Q'Tx + R'x. []
*At II.F:1534.* Lemma 5.5 (a)'s proof constructs, from [0C] Theorem 3.4, Q' with Q' P-hat = I - R',
R' in Psi^(-inf,(alpha_1, inf)), alpha_1 > 2 gamma_I, and shows Q' bounded x^(2gamma_I) H^(m-2)_0 -> x^(2gamma_I) H^m_0.
Its step (i) (Schur, with a in (2 gamma_I, alpha_1) and b arbitrary, the right index being inf) and the conormality of
the kernel under 0-vector fields on either side show R' bounded x^beta H^(-N')_0 -> x^(2gamma_I) H^m_0 for every beta
(deduced from the lines of that proof). So the first estimate of (5.5) holds with C = max(||Q'||, ||R'||). The second
follows from P-hat Q = I - R, R in Psi^(-inf,(inf, 3 - alpha_0)), alpha_0 < 2 gamma_I, by duality: for v in
(x^(2gamma_I) H^(m-2)_0)^*, v = Q^* P-hat^* v + R^* v and ||R^* v|| <= ||R||_(Y -> W^*) ||v||_W with W =
x^(beta') H^(-N')_0, W^* = x^(-beta') H^(N')_0, R being bounded into W^* (left index inf) from Y (right index
3 - alpha_0 > 3 - 2 gamma_I). No Hahn-Banach functional, no open mapping constant, no sigma_min. Computed on an exact
model with a kernel (inverse6_5 K7; control C8: without the R' term it fails on the kernel).

**Lemma R2 (an a priori estimate and a quantitative injectivity give the inverse).** If ||x||_X <= C_A (||Tx||_Y +
||Kx||_V) and ||Kx||_V <= C_B ||Tx||_Y for all x, then ||x||_X <= C_A (1 + C_B) ||Tx||_Y. *Proof.* Substitute. []
This is the effective form of every "Fredholm and injective, so invertible" with an inverse bound needed (B4, B5, and
Proposition 5.1 downstream of B6): the content is C_B.

**Lemma R3 (absorption).** (a) If ||u|| <= C_a h^-2 ||P'u|| + C_a h^N ||u||_(-N 1) and ||u||_(-N 1) <= ||u||, then
||u|| <= 2 C_a h^-2 ||P'u|| for h <= h_0 := (2 C_a)^(-1/N). (b) If ||u||_o <= C (h^(-1-delta) ||Pu||_o' + h^N ||u||_o
+ ||u||_(-K 1)) and ||u||_(-K 1) <= C_K h ||u||_o (Prop. 8.1, "Absorption"), then ||u||_o <= 2 C h^(-1-delta) ||Pu||_o'
for h <= h_0 := min((4C)^(-1/N), (4 C C_K)^-1); Theorem 1.3 (3) then holds with C_0 = h_0^-1 (1 - nu'^2)^(-1/2) and
||P-hat(sigma)^-1|| <= 2 C |sigma|^(-1+delta) (|sigma| >= C_0, by 8.4's choice of h). *Proof.* Move the absorbed terms
to the left (each is at most half the left side). []
[R3, the verifier's minor 3: the last bound omits (1 - nu'^2)^(-(1-delta)/2) in the case h = |Re sigma|^-1 and holds in
the h-dependent semiclassical norms ||.||_o, ||.||_o', not uniformly in X_sigma's; corrected in R3.1.]
[R4, the reader's minor 1: (a)'s hypothesis holds only for h below Prop. 6.7 (a)'s own threshold h_ch', and (b)'s only
below Prop. 8.1's h_ch (I.B:1881, :1704 and (6.6)'s h_0 within it); so (a) holds for h <= min(h_ch', (2 C_a)^(-1/N)) and
(b) for h <= min(h_ch, (4C)^(-1/N), (4 C C_K)^-1), with C_0 that minimum's inverse times (1 - nu'^2)^(-1/2) (R4.1).]
[R5: read "h < min(...)" in both places, strict, as R4.1 proves.]

**Lemma R4 (the interpolation constant of Proposition 6.7).** Let C_a be (a)'s constant on Im sigma in [beta, beta']
(and C_a |sigma|^-1 on Im sigma = beta'), kappa := beta' - beta, and F := sup over sigma_0 >= h_0^-1 of
exp(3 log sigma_0 e^(-pi sigma_0/(2 kappa))). Then ||(P'_(h,z))^-1|| <= 4 F C_a h^(-1-(beta' - Im(z/h))/kappa).
*Proof.* Lemma 6.6 on the rectangle of (c), L = 2 sigma_0/kappa, Lambda = log sigma_0, gives
||P-hat'(sigma)^-1|| <= F C_a sigma_0^(-theta), theta = (Im sigma - beta)/kappa in [0, 1], for Re sigma in
[2 sigma_0, 4 sigma_0]; there h = 1/Re sigma lies in [1/(4 sigma_0), 1/(2 sigma_0)], so sigma_0^(-theta) <= (4h)^theta
<= 4 h^theta, and (P'_(h,z))^-1 = h^-2 P-hat'(z/h)^-1. []
*At b0* q^Gamma = 4 on Gamma (K1), so (1.4)'s f(eta) = lam_max - 4 eta exactly, and with beta = gamma_- + eps,
beta' = gamma_+ + eps, kappa = gamma_+ - gamma_- = nu/8 = 2^(-3/2) for every operator (K1-K2): F <= 1.002659 for every
h_0 <= 1 (certified, K6), so (6.11) holds with the constant 4.01064 C_a. Lemma 6.6's last inequality,
cosh(a)/cosh(2a) <= 2 e^(-a), is checked on a grid (K6; control C7: with kappa = nu/4, F = 1.04617).
[R3, the verifier's n6: R4's C_a is the constant of (a) after absorption, R3 (a)'s 2 C_a; in R3 (a)'s notation (6.11)'s
constant is 8 F C_a <= 8.02128 C_a.]

**Lemma R5 (Schur at b0).** P-hat_b0(sigma) for box, box on 1-forms and L_b0 commutes with SO(4); in any
SO(4)-invariant pair of norms the inverse's norm is the largest of its isotypic blocks' (R7.4). The norm of
L^2(I x S^3, r^3 dr dw) with the static frame's pointwise norm, I = {r in [1.2, 4]}, is SO(4)-invariant, so a cut-off
bound C_D(sigma) := ||chi_I P-hat(sigma)^-1 chi_I|| is the sup over (type, l). (The write-out's X_sigma, Y_sigma are
invariant only up to equivalence: averaging over SO(4) gives invariant norms equivalent with constant
sup_g ||g||_(X->X) ||g||_(Y->Y), a calculus constant; not computed.)

**Lemma R6 (gluing through complex absorption).** Let Q := chi W chi with chi supported in I, W bounded, P_1 :=
P-hat(sigma) - iQ, and suppose P-hat(sigma) and P_1 invertible X_sigma -> Y_sigma. With C_ext := ||P_1^-1||_(Y->X),
e_X := ||chi||_(X -> L^2(I)), e_Y := ||chi||_(L^2(I) -> Y) (W smoothing when L^2(I) is not in Y_sigma,
s > 1) and C_D as in R5,
||P-hat(sigma)^-1||_(Y_sigma -> X_sigma) <= C_ext + C_ext^2 e_X e_Y ||W|| (1 + ||W|| C_D).
*Proof.* P-hat^-1 = P_1^-1 - i P_1^-1 Q P-hat^-1 and P-hat^-1 = P_1^-1 - i P-hat^-1 Q P_1^-1; inserting the second in
the first, P-hat^-1 = P_1^-1 - i P_1^-1 Q P_1^-1 - P_1^-1 (Q P-hat^-1 Q) P_1^-1, and ||Q P-hat^-1 Q|| <= ||W||^2 C_D
on L^2(I). [] (Checked exactly over Q(i) on random rational matrices, with its norm bound: inverse6_5 K8; control C9.)
So once the cut-off bound C_D is certified, an inverse bound in the write-out's norms needs only C_ext(sigma), the
inverse of the absorbed problem, whose proof needs no trapping estimate and no mode stability (the absorption covers
the photon sphere r = 2^(1/2) in I): the radial-point estimates at the horizon and at infinity, real principal type
propagation, the elliptic estimate and the absorbing region. Its invertibility at a given sigma is a hypothesis of R6,
not proved here (it holds for the symmetric scalar wave by the flux identity; for the bundle operators it is part of
the input).
[R3, the verifier's n6: "the absorption covers the photon sphere" is moot here: at a fixed sigma there is no trapping,
and C_ext's proof is the Fredholm estimate's chain at that sigma with the absorbing term; the parenthesis is withdrawn.]

**Lemma R7 (the Morawetz certificates).** For V = P(y) (y = 1/r^2, V' = -(2 f/r^3) P'(y), ' = d/dr_*) and phi = tanh g,
g(x_c) = 0, g' = 1/s_R + (1/s_L - 1/s_R)/(1 + e^((r_* - x_c)/k_s)), s_L <= s_R:
(a) if x_c = r_*(2^(1/2)), then -phi U' >= 0 on R (U = f y, U' = (2 f/r^3)(2y - 1) changes sign exactly at
r = 2^(1/2), where phi does), so w = -phi V' - phi'''/2 for V = a U + b Q (Q = f y^2) is nondecreasing in a and affine
in b: w >= 0 at (a_0, b_lo) and (a_0, b_hi) gives w >= 0 for every a >= a_0, b in [b_lo, b_hi], with min_I w no less
than the two endpoints' least;
(b) |phi'''| <= sech^2 g (|g'''| + 6|g'||g''| + 4|g'|^3) <= 4 e^(-2|g|) K, K = D/(10 k_s^2) + 6D/(4 k_s s_L) + 4/s_L^3,
D = 1/s_L - 1/s_R (|tanh| <= 1, |4 tanh^2 - 2 sech^2| <= 4, |sigma'| <= 1/4, |sigma''| <= 1/(6 3^(1/2)) < 1/10);
g <= (r_* - x_c)/s_L + D k_s log 2 for r_* < x_c and g >= (r_* - x_c)/s_R for r_* > x_c;
(c) left tail: for r <= r_L, 2f/r^3 = 2 (r + 1)^2 e^(-2r) r^-5 e^(2 r_*) >= 8 e^(-2 r_L) r_L^-5 e^(2 r_*), so with
beta_L := inf over [y_L, 1] of -P' (minus the majorant of a perturbation), the ratio (phi'''/2)/(-phi V') is at most
K_L e^(2 r_*(1/s_L - 1)), decreasing toward the horizon iff s_L < 1; right tail: with beta_R := inf over [0, y_R] of P',
r <= r_* + d_R, the ratio is at most K_R e^(-2(r_* - x_c)/s_R)(r_* + d_R)^3, decreasing once r_* + d_R > 3 s_R/2.
Then Lemma E2.8 (E2-PILOT.md 3e, READ) gives, for real sigma != 0 and f in L^2(I), ||chi_I R(sigma) chi_I||_(L^2(dr_*))
<= B(sigma) = ((2/m' + (M' + 2|sigma|)^2/w_I)/w_I)^(1/2), and Lemma E2.10 (3h) the same with 4|sigma| when
Im sigma > 0 (V >= 0 and q = 0 for every potential here). *Proof.* (a) is E2-PILOT's Lemma E2.9 with the asymmetric g;
(b) differentiates tanh g and bounds the logistic factors; (c) is e2certify5's tail argument with beta_L, beta_R as
interval lower bounds of the potential's own P'. [] (The elementary inequalities used, exact: inverse6_5m M0.)

**Lemma R8 (the exact transfers).** On the blocks where the operator is its master operator the cut-off bound
transfers with the factor max_I f = 15/16: for box on functions (u = r^(-3/2) Phi S, G = f r^(3/2) g; E2-PILOT (1.1)),
for box on the vector-type 1-forms A = r^(-1/2) Phi Y (box = delta d there, modes5 M3: -f r^(1/2) (delta d A)_i =
(f (f Phi')' + sigma^2 Phi - V_1 Phi) Y_i, so G = f r^(1/2) F_Y), and for 2 L_b0 on the tensor-type blocks
h = 2 r^2 H T (gmodes5 G1: D Ric(h)_ij = -r^2 (box H + (3/r) Dr.DH - (k_T^2 + 2) H/r^2) T_ij, all other components 0,
and f r^(3/2) times that bracket is the V_T master operator for Phi = r^(3/2) H; the gauge term vanishes on TT angular
tensors: tr h = 0, delta h = 0, iota_(c_Ups^#) h = iota_(c_Ups,H^#) h = 0),
||chi_I P-hat(sigma)^-1 chi_I||_(L^2(I x S^3)) <= (15/16) B(sigma) (for L_b0: of (2 L-hat_b0(sigma))^-1).
*Proof.* Pointwise, per unit dr_* and with the harmonic's L^2(S^3) norm c factored out, |u|^2 r^3 dr = c f |Phi|^2 dr_*
and |G|^2 = f (|F|^2 r^3 f) (exact, M7), so ||u||_I^2 <= c (max_I f) ||Phi||_I^2, ||G||^2 <= (max_I f) ||F||_I^2/c, and
||Phi||_I <= B ||G|| (Lemma R7) because Phi is the solution in the operator's class (regular across the future
horizon, outgoing: III.D Prop. 6.2's and III.F'' Prop. 3.1's class), unique by mode stability. f increases, so
max_I f = f(4) = 15/16. For the tensor type c = 4 and F = 2 L h: ||h||_I <= 2 (15/16) B ||L h||_I. []

## 3. The microlocal constants at L_b0 (computed; `checks/inverse6_5.py`)

*Trapping* (K1, exact in mu). Gamma = {r^2 = 2 mu, xi = 0, C = 4 mu}; H phi_1 = -nu_1 phi_1, H phi_2 = nu_2 phi_2 on
Sigma^s with VI.A (3.2)'s rates; on Gamma **nu = nu_min = 4 (2 mu)^(-1/2)**, **c_Gamma = {phi_u, phi_s} = (2/mu)^(1/2)**,
**q^Gamma = 4**, **beta_0^Gamma = 2**, and the rate in the time t is nu/q^Gamma = (2 mu)^(-1/2) (cover5.py's
lambda_L). Control C1: H phi_1 = +nu_1 phi_1 fails.

*(Gamma.4) for the 1-form operators* (K2, exact; box and box^Ups: E^Ups vanishes near Gamma). In h_Gamma(eps) =
diag(1, 1/eps, 1/eps^2) on III.D 5.2 (c)'s normalised frame, plus g on V_perp, p_1^Gamma has characteristic polynomial
lam^3 (lam^2 - 2 eps): **lam_max = (2 eps)^(1/2)**; gamma_+ = lam_max/4, gamma_- = (lam_max - nu/2)/4,
**delta_Gamma(0) = 2 lam_max/nu = (eps mu)^(1/2)**, (Gamma.4) iff eps < 1/mu; the frame at Gamma is orthonormal for the
static coframe's Euclidean form (exact), so **cond(h_Gamma) = eps^-2** (16 at delta_Gamma(0) = 1/2, mu = 1). Control C2
refutes lam_max = 2 eps.

*(Gamma.4) for 2 L_b0* (K3; III.F Proposition 4.1 states lam_max <= C eta with no C). At Gamma the record's damping
1-form is (10.49)'s inner piece (2 r_0)^-1 (dt + dr/4) (Kerr-Schild t, r_0 = 100 r_h; PART-IV5-CDMODES.md:36-38),
exactly c = (-1/200, -1/(160 2^(1/2)), -1/200, 0, 0) in the normalised frame, gam = 2 gamma_C, so gam c_2 =
-gamma_C/100; e_C = 1/102400. Computed: charpoly(A) = lam^10 (lam + 2 gam c_2)^3 (lam + 4 gam c_2)(lam + 2 (1 - e_C)
gam c_2) (strap5 P2's, reproduced); A never raises III.F's grading W (W = 0, 2, 4, 5, 6, 8 on the seven pieces); the
W-preserving part's symmetric part is <= 0. In h_Gamma(eta) = sum_P eta^(-2W(P)) <,>_0:

- gamma_C = 10^6: lam_max in [52.143, 52.149], [0.52072, 0.52078], [5.2071, 5.2077] x 10^-3,
  [5.2071, 5.2077] x 10^-5 at eta = 10^-1, ..., 10^-4; (Gamma.4) holds at eta = 0.01647 and fails at 0.01648;
  delta_Gamma(0) <= 1/2 holds at 0.01165 and fails at 0.01166; cond(h_Gamma) = 3.41 x 10^28, resp. 8.69 x 10^30.
- gamma_C = 10^7: [521.53, 521.59], [5.2082, 5.2089], [5.2082, 5.2088] x 10^-2, [5.2082, 5.2088] x 10^-4;
  (Gamma.4) at 0.00521 (fails at 0.00522); delta_Gamma(0) <= 1/2 at 0.00368 (fails at 0.00369); cond 3.39 x 10^36,
  8.84 x 10^38.
- gamma_C = 10^8: [5215.4, 5216.1], [52.083, 52.090], [0.52083, 0.52089], [5.2083, 5.2089] x 10^-3; (Gamma.4) at
  0.00164 (fails at 0.00165); delta_Gamma(0) <= 1/2 at 0.00116 (fails at 0.00117); cond 3.65 x 10^44, 9.30 x 10^46.

(lam_max(p_1^Gamma), certified brackets: interval LDL of t I - p_1 above, a Rayleigh quotient below; "fails" is
certified too, with no monotonicity in eta claimed.) **The exact leading order** (K3 (d), gamma_C symbolic): the
eta^1 term vanishes on ker M_0, and the second-order matrix has the top eigenvalue (gamma_C - 80 2^(1/2))^2/(192
gamma_C), so

    lam_max(p_1^Gamma(eta)) = eta^2 (gamma_C - 80 2^(1/2))^2/(192 gamma_C) + O(eta^3),

which the certified rows match (0.0052072 at gamma_C = 10^6, eta = 10^-4).
[R3, the verifier's n6: the number is lam_max/(gamma_C eta^2), certified in [0.005207, 0.005208] at gamma_C = 10^6,
eta = 10^-4, against the leading order's (1 - 80 2^(1/2)/gamma_C)^2/192 = 0.0052072.] So (Gamma.4) needs eta below about
16.48 gamma_C^(-1/2) and delta_Gamma(0) <= 1/2 below about 11.65 gamma_C^(-1/2); h_Gamma's eigenvalues relative to
<,>_0 span eta^0 to eta^-16, so its condition number is eta^-16, about (gamma_C/271.5)^8 at the threshold: **the norm
equivalence that converts the trapping estimate from h_Gamma to the frame's metric costs eta^-8, 1.85e14 at gamma_C =
10^6**, a factor of C in (6.6) the record leaves implicit. (The record's gamma_C is 1/h with h < h_* = min(10^-6, h_0,
h_tf), not a fixed number: the factor grows as gamma_C^4.) Controls: C3 (eta = 1: (Gamma.4) fails), C4 (c -> -c, a
future-pointing damping: lam_max >= 4 10^4 at every eta), C5 (trace weight 1: the last factor moves).

*The horizon* (K4, exact). beta_0 = f'(r_h) = 2 mu^(-1/2) (the red-shift rate of (H3)); the thresholds of I.A (1.5):
box 0; box^Ups 1 (s > 3/2, III.D Lemma 5.1); 2 L_b0: with (10.49)'s inner piece in the ingoing chart,
(2 r_0)^-1 (dv - (3/4) dr), a_v = 1/(2 r_0), **x = a_v gamma_C r_h = gamma_C/200** and y = 0 (c_Ups,H = -(1/2) chi dr):
III.F'' (1.1)'s fifteen roots are 0 (6), 1 - x (3), 2 - 2x, -(1 - e_C) x, -1 (3), -2, so **vartheta_L = 0 for gamma_C
>= 200**: the horizon threshold of L_b0 at b0 is any number above 0 (s > 1/2 + delta in a fibre metric depending on
delta), where the record carries the bound 2 (LOSS-D 2b), an upper bound that stands. Control C6: a_v < 0 gives
vartheta_L = 10002. Not computed: the condition number of the fibre metric that makes K's Hermitian part
<= vartheta_L + delta (K has entries of size x; lhor5.py's K is not rerun here).

*Infinity* (K5, exact). spec S-bar of III.F (3.1) at (v_C, e_C) = (1/2, 1/102400) has least element 0, so S-bar = 0 for
box, box^Ups and 2 L_b0, and with theta_in = 0 (thetain5) the decay order must exceed -1/2 at R_in and lie below -1/2
at R_out (I.B section 1.4): at real sigma != 0 no constant decay order is admissible, so X_sigma is genuinely of
variable order there. s_C = (1 - e_C)(1 - v_C) gamma_C = 63999375/128 > 100 at gamma_C = 10^6.

*Interpolation* (K6, certified): F <= 1.002659 (section 2, Lemma R4).

## 4. Certified spectral bounds for the mode-decomposed operators (`checks/inverse6_5m.py`)

The master operators -d^2/dr_*^2 + V - sigma^2 (M0, exact): III.D (M2)-(M4) give V_0 = (k + 3/4) U + (9/4) Q,
V_1 = (k + 3/4) U + (5/4) Q, V_2 = (k + 3/4) U - (7/4) Q (k = l(l + 2)); III.F'' Theorem 2.2 via gmodes5 G1-G3 gives
V_T = V_0 (l >= 2), V_V = (k + 3/4) U - (27/4) Q (l >= 2) and V_S = f Q_S/(16 r^2 H^2) (l >= 2), whose exact partial
fraction is V_S = (k + 3/4) U - (39/4) Q + U (24 y (5y - 3)/H + 288 y^2 (1 - y)/H^2), H = m + 6y, m = k - 3, so
P_S' = P'_(a, -39/4) + E(y, 1/m) with

    E(y, eps) = -48 eps y (162 eps^2 y^4 - 144 eps^2 y^3 + 18 eps^2 y^2 + 75 eps y^3 - 72 eps y^2 + 9 eps y + 10 y^2
                - 12 y + 3)/(1 + 6 eps y)^3.

Certificates (each: w >= 0 on R by adaptive bisection on t = log(r - 1) in [-120, log 119] plus the two tail bounds of
Lemma R7; then m', M', min_I w over 2000 pieces of I). Each row: the certificate, its multiplier (s_L, s_R, k_s, centre
minus r_*(2^(1/2))), what it covers, then min_I w, m', M' and B at sigma = 0+, 1, 3, 10.

- M1, family A at (a, b) = (15/4, 5/4), (15/4, 9/4); (23/25, 4, 1, 0); V_0 and V_1 at every l >= 1;
  0.071345, 0.066138, 0.69999; **22.81, 43.09, 96.14, 290.9**.
- M2, family B at (35/4, -7/4), (35/4, 9/4); (49/50, 4, 1, 0); V_0, V_1, V_2, V_T at every l >= 2;
  0.15881, 0.070729, 0.66610; **13.99, 21.45, 44.05, 130.9**.
- M3, family C at (63/4, -39/4), (63/4, 9/4); (49/50, 2, 1, 0); every a U + b Q with b in [-39/4, 9/4] at l >= 3, so
  V_V at every l >= 3; 0.23036, 0.040543, 0.76964; **15.02, 18.94, 32.83, 91.35**.
- M4, the V_S majorant at (99/4, -39/4), eps <= 1/21; (49/50, 2, 1, 0); V_S at every l >= 4;
  0.28670, 0.040543, 0.76964; **13.39, 16.30, 27.02, 73.63**.
- M5, V_2 at l = 1; (49/50, 3/2, 1/2, 3/10); 0.012006, 0.041579, 0.85611; **95.35, 246.2, 574.6, 1739**.
- M5, V_V at l = 2; (49/50, 3/2, 1/2, 4/5); 0.12423, 0.078951, 0.85621; **15.86, 27.07, 57.01, 168.5**.
- M5, V_S at l = 2; (49/50, 3/2, 1/2, 7/10); 0.018958, 0.069537, 0.85619; **59.64, 155.7, 363.8, 1101**.
- M5, V_S at l = 3; (49/50, 2, 1, 0); 0.25443, 0.040543, 0.76964; **14.25, 17.68, 30.04, 82.82**.

(V_0 at l = 0 is E2-PILOT 3g's certificate: 164.5, 183.5, 275.2, 725.0; and on 3 <= sigma <= 384 E2-PILOT 3j's band
certificate, 11.477 for every l, is the better bound for V_0 = V_T.) **So every master operator of III.D (M2)-(M4) and
of III.F'' Theorem 2.2 has, at every harmonic in its range and every real sigma != 0, a certified bound
||chi_I R(sigma) chi_I|| <= B(sigma), uniformly in l** (the uniformity is the photon-centred families' monotonicity in
a, from l = 1, 2, 3, 4; below them four harmonics are certified one by one); the largest, at sigma = 0+, 1, 3, 10, is
95.35, 246.2, 574.6, 1739 (V_2 at l = 1); B is increasing in |sigma| and stays bounded as sigma -> 0. For Im sigma > 0
the same with 4|sigma| (Lemma E2.10). The bounds grow linearly in |sigma| (one multiplier per certificate); at large
sigma E2-PILOT's sigma-dependent multipliers are the route, not repeated here.

*The exact transfers* (M7, deduced; modes5 M2-M3 and gmodes5 G1 rerun): with Lemma R8,

    ||chi_I box-hat_b0(sigma)^-1 chi_I|| <= (15/16) B_(V_1)(sigma)  on the vector-type 1-form blocks
        (l = 1: 21.39, 40.39, 90.14, 272.7; l >= 2: 13.12, 20.11, 41.30, 122.7 at sigma = 0+, 1, 3, 10),
    ||chi_I (2 L-hat_b0(sigma))^-1 chi_I|| <= (15/16) B_T(sigma)  on the tensor-type blocks, every l >= 2
        (13.12, 20.11, 41.30, 122.7),

and (15/16) times E2-PILOT's bounds for box on functions; by Lemma R5 these are the sup over the blocks of the type.

Controls (each fails as it must): C1 the family-C multiplier centred at r_*(2^(1/2)) + 1/2 has -phi U' <= -0.005476
at r = 1.45, so no monotonicity in a; C2 V_V at l = 1 (the Killing sector, where no master equation is used) with
phi_A: the bisection fails and w <= -0.3617 at t = -3.4975; C3 the V_S majorant from l = 3 (eps <= 1/12): W_S <=
-0.1777 at t = -3.83; C4 s_L = 3/2: the left tail exponent is negative.

## 5. Per bound: statement, what is proved, the constant or the single missing input

**B1. I.B:1513, the trapping estimate (6.6).** *Computed at b0* (section 3): every datum of (Gamma.1)-(Gamma.4) the
proof uses -- nu_min = 4(2 mu)^(-1/2), c_Gamma = (2/mu)^(1/2), q^Gamma = 4, beta_0^Gamma = 2, kappa = gamma_+ -
gamma_- = nu/8; for box and box^Ups lam_max = (2 eps)^(1/2), delta_Gamma(0) = (eps mu)^(1/2), cond(h_Gamma) = eps^-2;
for 2 L_b0 lam_max = eta^2 (gamma_C - 80 2^(1/2))^2/(192 gamma_C) + O(eta^3) (certified brackets at twelve points),
(Gamma.4) iff eta below about 16.48 gamma_C^(-1/2), cond(h_Gamma) = eta^-16. *Not obtained:* (C, h_0). The proof is by
contradiction (defect measures, Steps 1-4), and no step of it produces a number; nothing in the record replaces it.
**The single missing input: an explicit pair (C, h_0) in (6.6) for 2 L_b0 (and box^Ups) at Gamma_b0**, as a function
of the data above and of finitely many symbol seminorms: a constructive normally hyperbolic trapping estimate (an
Ehrenfest-time positive commutator argument with explicit remainders in place of Steps 1-4). At b0, for the scalar-type
master operators, the per-harmonic Morawetz bounds (E2-PILOT, section 4) are a constructive substitute for the global
cut-off estimate, but not for (6.6) on the bundles: there E^C does not vanish near Gamma (gam c_2 = -gamma_C/100), the
blocks are coupled systems, and the master decomposition is global, not microlocal.

**B2. I.B:1685, the absorbed inverse (6.11).** *Proved:* the step at 1685 costs nothing (the inverse bound is (a)'s
constant); absorption with h_0 = (2 C_a)^(-1/N) (Lemma R3 (a)); (6.11) with the explicit constant 4 F C_a, F <= 1.002659
(Lemma R4, certified at kappa = nu/8, valid for box, box^Ups and 2 L_b0 alike). **The single missing input: C_a**, the
constant of Proposition 6.7 (a)'s a priori estimate, a composition of Proposition 4.2 (elliptic, outside
Gamma(3 delta_0/4)), Corollary 4.6 (propagation into the absorbing region, along curves that leave Gamma(delta_0) in
explicit time at b0, phi_u, phi_s being explicit) and (6.6) [B1's input].
[R3: at b0 only; the uniform constants over b (I.B section 9: compactness of B and the absorption of Prop. 6.7 (a) run
by contradiction with sequences b_j) are a further input, R3.2; in R3 (a)'s notation the constant is 8 F C_a, R3.3.]
[R4: h_0 = min(h_ch', (2 C_a)^(-1/N)), h_ch' Prop. 6.7 (a)'s chain threshold (R4.1).]

**B3. I.B:1978, high-energy invertibility.** *Proved:* "Fredholm, so invertible" loses nothing: ||P-hat(sigma)^-1|| <=
2 C_8.1 |sigma|^(-1+delta) for |sigma| >= C_0 = h_0^-1 (1 - nu'^2)^(-1/2), h_0 = min((4 C_8.1)^(-1/N), (4 C_8.1
C_K)^-1) (Lemma R3 (b)). *Computed:* every threshold and rate the chain of Proposition 8.1 reads at b0 (section 3: s >
1/2 + vartheta_H with vartheta_H = 0, 1, 0 for box, box^Ups, 2 L_b0; the decay order across -1/2 between R_in and
R_out, S-bar = 0; beta_0 = 2; the trapping data). **The single missing input: C_8.1**, the constant of (8.1), the
product along the cover's chain (R) radial (Props. 5.2-5.3), (A) propagation (Cor. 4.6), (Gamma) Theorem 6.8 [B1, B2],
(U), (O) (Prop. 5.5) and the artificial boundary (7.2), each a microlocal estimate whose constant is a calculus
constant (CONSTANTS5.md R7.A made the orders explicit, not these constants). The middle range R4.4 assigns here is B4's
and B5's.
[R3: the bound is 2 C_8.1 (1 - nu'^2)^(-(1-delta)/2) |sigma|^(-1+delta) in the semiclassical norms (R3.1); Prop.
8.1's finite cover and nu_1 are compactness choices, and uniformity over b is by compactness and contradiction (R3.2).]
[R4: C_0 = min(h_ch, (4 C_8.1)^(-1/N), (4 C_8.1 C_K)^-1)^-1 (1 - nu'^2)^(-1/2), h_ch Prop. 8.1's chain threshold
(R4.1); here C_8.1 is the constant before absorption, the record's (8.1) constant being twice it (R4.2).]
[R5: so read "**The single missing input: C_8.1**, the constant of (8.1)" above as "(8.1)'s chain constant before
absorption"; the record's (8.1) constant is 2 C_8.1 in this paragraph's sense (R4.2).]

**B4. III.F'':223, L_b0 at sigma != 0.** *Proved/computed:* by Lemmas R5 and R6, ||L-hat_b0(sigma)^-1||_(Y_sigma ->
X_sigma) <= C_ext + C_ext^2 e_X e_Y ||W|| (1 + ||W|| C_D(sigma)) with C_D = sup over types and l of the cut-off bounds.
Certified (section 4): every Kodama-Ishibashi master operator (V_T, V_V, V_S) at every l >= 2 and every real sigma != 0,
uniformly in l; and on the tensor-type blocks C_D <= (15/16) B_T exactly (Lemma R8). *Where it stops, exactly:* (i) for
the vector- and scalar-type blocks, C_D needs the reconstruction of h from the master function and the gauge 1-form of
Theorem 2.2 (Steps 1-6, the radial ODE for omega) with the inverses of box^C-hat(sigma) and box^Ups-hat(sigma) (the
modified 1-form operators, whose mode stability is III.E and III.D', not among the six) -- a per-harmonic ODE bound,
computable, not computed; (ii) **C_ext(sigma)**, the inverse of the absorbed problem in X_sigma -> Y_sigma (with its
invertibility), the non-trapping part of the write-out's Fredholm estimate: the radial-point constants at the horizon
and at infinity in the variable-order norms, whose thresholds section 3 computes. Beside these, e_X, e_Y (a cut-off's
norms between the write-out's spaces and L^2(I)) and ||W|| are explicit once the norms are fixed, calculus constants of
the same kind.

**B5. III.D:365, box on 1-forms at sigma != 0.** The same structure. *Certified:* V_0 (every l; E2-PILOT and section 4),
V_1 and V_2 (every l >= 1), every real sigma != 0; on the vector-type 1-form blocks C_D <= (15/16) B_(V_1) exactly
(21.39 at sigma -> 0, l = 1). *Where it stops, exactly:* (i) the scalar-type blocks' C_D needs the reconstruction of
steps (a)-(c): omega from delta omega (V_0), F_tr (V_2) and the gauge step omega = (i/sigma)(d phi + iota_T d omega),
phi = omega(T), with its 1/|sigma|, and the l = 0 sector -- per harmonic, not computed (the sources of steps (b)-(c) are
not supported in I, so the cut-off bounds do not compose; global weighted forms of Lemma E2.8 are the route);
(ii) C_ext(sigma) as in B4.

**B6. II.F:1393, the weak-remainder estimate.** *Proved:* Lemma 5.2 is not needed (Lemma R1): (5.5) holds with
max(||Q'||, ||R'||) and max(||Q||, ||R||) from the parametrices Lemma 5.5 (a) already builds; sigma_min of T on ker Pi
and ||Pi|| disappear. *Computed at b0:* the weight window of Lemma 5.4, I_sigma = (-2 Im sigma, 2(3/2 + S-bar)) =
(-2 Im sigma, 3) (S-bar = 0), so gamma_I < 3/2. **The single missing input at the site: the two parametrix norms**
(0-calculus constants of [0C] Theorem 3.4 for the compact model at the weight 2 gamma_I). Downstream (not at the site),
Proposition 5.1's inverse of N^0(sigma) is again "Fredholm index 0 and trivial kernel" (Lemmas 5.6, 5.8): its effective
form (Lemma R2) needs a quantitative injectivity ||u||_(Z_N) <= C_B ||N^0(sigma) u||_(Y^(s-2)); at b0 N^0(sigma)
commutes with SO(4) and is, harmonic by harmonic, an explicit ODE in R (Bessel at scri, I.C's b-structure at K+),
computable, not computed.

## 6. Proved, computed, open

- *Proved:* Lemmas R1-R8 (R1 eliminates II.F Lemma 5.2's constant; R3-R4 make B2-B3's absorption and interpolation
  explicit; R6 reduces the mode-stability bounds to C_D and C_ext; R7-R8 the certificates' analysis and the transfers).
- *Computed (exact):* (Gamma.1)-(Gamma.4) data at b0 for box, box^Ups, 2 L_b0; the leading-order law of lam_max for
  2 L_b0; the horizon roots and vartheta_L = 0 at the record's damping; S-bar = 0; the master potentials and V_S's
  partial fraction; the pointwise norm identities.
- *Certified:* lam_max brackets and the admissible eta; F <= 1.002659; w >= 0 on R and the constants of eight
  certificates; the master bounds of section 4 at every l and real sigma != 0.
- *Deduced:* the transfers (15/16) B to the vector-type 1-form and tensor-type 2-tensor blocks; Lemma E2.10's extension
  to Im sigma > 0; R1's boundedness of R' from Lemma 5.5's proof.
- *Open, each with its single missing input:* B1 (C, h_0) in (6.6); B2 C_a; B3 C_8.1; B4 the vector/scalar-type
  reconstruction and C_ext(sigma); B5 the scalar-type reconstruction and C_ext(sigma); B6 the two parametrix norms (and
  N^0(sigma)'s quantitative injectivity downstream). B2 and B3 contain B1; B4 and B5 share C_ext. So no lower bound for
  lambda1 or delta yet.

## 7. Proposed text for CONSTANTS5.md (in this file; CONSTANTS5.md is not edited)

1. R9.7 block 2 (the text proposed for the paper's "Settling" bullet), its last clause. The old text occurs exactly
   once in CONSTANTS5.md (checked):

```old
the other six need the constants of the write-out's microlocal estimates at the final black hole and
  certified spectral bounds in its norms (supplement `CONSTANTS5.md` R8.3-R8.4).
```

```new
of the other six, one (a weak-remainder estimate at future timelike infinity) needs no inverse
  bound once the parametrix its proof already builds is used; one, the trapping estimate, still has no constant, its
  proof being by contradiction, though its symbol data at the final black hole are now computed, among them the fibre
  metric it needs, of condition number about (gamma_C/271.5)^8; two (the high-energy inverses) have no non-constructive
  step of their own and reduce to that constant and to calculus constants, their absorption and interpolation steps
  being explicit; and the two mode-stability ones have their spectral input certified harmonic by harmonic (every
  master equation, every harmonic, every real frequency, in a cut-off norm, and exactly on the tensor-type and
  vector-type blocks), so that what remains for them is the gauge reconstruction of the other types and the inverse of
  the absorbed, non-trapping problem in the write-out's norms (supplement `docket68/n1star/INVERSE5-SIX.md`,
  `checks/inverse6_5.py`, `checks/inverse6_5m.py`).
```

2. R9.5, the open bullet's clause on the six (optional, for the record's own status line). The old text occurs
   exactly once in CONSTANTS5.md (checked):

```old
the other six inverse bounds (their microlocal constants at L_b0 and certified spectral bounds in
  the write-out's norms).
```

```new
the other six inverse bounds, as INVERSE5-SIX.md section 5 states them: I.B:1513 an explicit
  (C, h_0) in (6.6) (its symbol data computed); I.B:1685 and :1978 the a priori constants C_a and C_8.1, which contain
  it (absorption and interpolation explicit); III.F'':223 and III.D:365 the gauge reconstruction of the non-tensor,
  resp. scalar, types and the absorbed problem's inverse C_ext(sigma) (the master bounds certified); II.F:1393 none at
  the site (the parametrix's two norms), Proposition 5.1's quantitative injectivity downstream.
```

Statuses behind the new texts: the elimination and the reductions, proved (section 2); the symbol data, exact
(inverse6_5 K1-K5); the brackets, F and the master bounds, certified (inverse6_5 K3, K6; inverse6_5m M1-M6); the
transfers, deduced from exact identities (M7).

## 8. Sources

proof5 (READ by content): PART-I-B-HIGHENERGY.md:26-235, 1499-1760, 1860-2055 (md5 df7e5206...);
PART-II-F-IOTA.md:1353-1600, 1646-1660, 1755-1775 (51c14571...); PART-III-F3-MODES.md:1-40, 180-289 (a826f9d0...);
PART-III-D-GAUGEPOT.md:1-60, 230-420 (e146c30e...); PART-III-F-LINEARISED.md:20-215 (f3836aae...); PART-VI-DYN.md:19-310
(e9479209...); PART-III-B-FAMILY.md:425-500; PART-IV5-CDMODES.md:24-45; PART-VI4-PARAMS.md:20-70; N1STAR-PROOF.md 10.14
(10.48)-(10.49) (by content; md5 7400212b... when read); E2-PILOT.md sections 1-4 (d156cd3b...); CONSTANTS5.md rounds
6-9; instruments imported: strap5.py, e2certify5.py, modes5.py, gmodes5.py; read: lhor5.py, nkind5.py, cover5.py
(lambda_L), thetain5 (theta_in = 0, via CONSTANTS5.md R9.0).

## Round 2 (2026-11-06): closing the inputs, and where the explicit-constant computation stops

*Status.* Appended; round 1 (sections 0-8) stands as written and is not edited. Asked: close, in order, (1) the gauge
reconstruction of B4-B5, (2) C_ext(sigma) and the absorbed problem's invertibility for box, box^Ups, box^C and L_b0,
(3) (C, h_0) in (6.6), (4) C_a and C_8.1, (5) B6's parametrix norms and N^0(sigma)'s quantitative injectivity, (6) the
lower bounds for lambda1 and delta through CONSTANTS5's chain, and (7) where an input cannot be made explicit at an
affordable cost, stop and state what holds. New program `checks/inverse6_5a.py` (9/9: A0-A4, controls C1-C4; seconds);
`checks/inverse6_5.py` (17/17) and `checks/inverse6_5m.py` (12/12) are unchanged and their round-1 outputs stand.
CONSTANTS5.md (its round 10 read: md5 0320dd90...), N1STAR-PROOF.md, the paper and the scalar-block files are not
edited; INVERSE5-SCALAR.md does not exist yet, and `checks/scalarblock5.py` (read: its docstring, no `.out`) is that
work's state.

### R2.0 Outcome

**lambda1 and delta are positive (proved: Theorem 4's proof, as the record has it); explicit lower bounds are not
computed.** Of the seven items, one is closed further here (the absorbed problem's invertibility, for box on functions
at b0), one is assembled exactly (the chain to lambda1 and delta, as a monotone formula in its inputs, with every input's
status), and the others stop at inputs that are not numbers in the record. The decisive finding is upstream of all six
bounds and was not named in round 1: **the write-out does not fix its operators and spaces numerically.** The gauge and
damping parameters are chosen below thresholds that the record proves to exist without a value (gamma_Ups,H in
(0, eps_0] with "There is eps_0 > 0" (III.D' Proposition 4.1), e_Ups and gamma_Ups below eps_1, eps_L and gamma_1, and
gamma_C = 1/h with h < h_* = min(10^-6, h_0, h_tf) off a countable set; PART-VI4-PARAMS.md rows u2-u5, c2), and the
record's own computational point gamma_C = 10^6 lies "outside the proved set" (PART-VI4-PARAMS.md:124, READ, A0); the
cut-offs zeta, chi of c_Ups, c_Ups,H, the smoothing of c_C near r_0/2 and 2 r_0, and the variable orders and
quantisation of X_sigma, Y_sigma are "any admissible" and not chosen. A certified constant of an operator that is not
specified, in a norm that is not specified, is not a number; so items (1), (2), (4), (5), and (3) for 2 L_b0 and
box^Ups, stop at the same first input: **explicit admissibility thresholds for the gauge and damping parameters, and
explicit choices of the cut-offs, orders and quantisation**. This is a limit of the explicit-constant computation, not
of the theorem: each threshold exists, by the cited statements.

### R2.1 Item by item

1. **Gauge reconstruction (B4, B5): not computed.** Per mode, box^C and box^Ups are non-self-adjoint ODE systems
   (scalar type: three components) whose first-order coefficients carry gamma_C c_C, of size gamma_C/100 = 10^4 at the
   photon sphere at the record's point (computed, inverse6_5 K3) and gamma_C/200 at the horizon (K4); a certificate
   uniform in l at real sigma != 0 needs the operator fixed (the smoothing of c_C beyond r = r_0/2, zeta, chi, and
   gamma_Ups,H, which the record leaves "in (0, eps_0]", not a number; scalarblock5.py's docstring records the same for
   gamma_H). The master parts of B4 and B5 stay certified (round 1, section 4); the reconstruction steps (a)-(c), the
   l = 0 sector and the 1/sigma factor are not computed.
2. **C_ext(sigma) and the absorbed problem.** *Proved and computed for box on functions at b0* (Lemma R9 below,
   inverse6_5a A4): with Q = chi q chi, q >= 0, the absorbed operator box-hat(sigma) - i sgn(sigma) Q is invertible
   X_sigma -> Y_sigma at every real sigma != 0, so R6's hypothesis holds for it. *Not proved* for box^Ups, box^C and
   L_b0 as wholes: their blocks' imaginary parts are not sign-definite (the gauge terms are not symmetric), so the flux
   argument does not apply, and no other argument is given; *not computed*: C_ext's value in the write-out's norms
   (the norms are not fixed, R2.0).
   [R4, the reader's nit 3: Lemma R9 holds for radial q >= 0 (R3.3 n4), which is what R6 needs.]
3. **(C, h_0) in (6.6): not computed.** The record's proof is a defect-measure contradiction; a constructive
   replacement needs explicit semiclassical calculus constants for operators B, E, G that Proposition 6.4 chooses
   without formulas, in a fibre metric whose condition number is eta^-16, about (gamma_C/271.5)^8 at the threshold
   (certified, round 1: the factor eta^-8 = 1.85e14 at gamma_C = 10^6 multiplies any such C). For the scalar master
   operators the per-harmonic route gives global cut-off bounds (certified: E2-PILOT's band 3 <= sigma <= 384, and every
   real sigma with linear growth, round 1 section 4), which are not (6.6): (6.6) is microlocal and concerns the bundle
   operators, near whose trapped set E^C does not vanish.
4. **C_a and C_8.1: explicit in form, not computed in value.** Lemmas R3-R4 give them as functions of (C, h_0) and the
   other estimates' constants (the absorption thresholds, the interpolation factor F <= 1.002659, certified); with (3)
   not computed, neither is evaluated.
   [R4: and of the chains' own thresholds h_ch' (Prop. 6.7 (a)) and h_ch (Prop. 8.1), not computed either; so are
   B2's h_0 and B3's C_0 (R4.1).]
5. **B6: not computed.** The parametrix of [0C] Theorem 3.4 is not quantified (the 0-calculus construction gives no
   norms), and N^0(sigma)'s quantitative injectivity, per harmonic an explicit ODE at b0, is not computed.
6. **The chain to lambda1 and delta: assembled** (inverse6_5a A1-A3; EFFECTIVE-CONSTANTS.md Propositions 2.1-2.2, READ
   by content, A0). With alpha = 8d + 2, K1 <= 2 C_d (delta_G <= 1), K2 = C_(N-2d)(C_(N-d) + 1), K3 = C_(3d,d) K1, K4 =
   2 C_(N,N-2d) K2, K5 = 2 C_(3d,N-2d) K2,

       theta0 = max{16, 16 eta_G^-2, (4 K3/delta_G)^(1/(6d+2)), 1 + K4, C1 K5 + C2 K3^2/2},   eps_NM = theta0^-alpha,
       delta = (1/2) min{1, eps_NM/A_2d, eps_NM^G/A_2d, eps_dat},
       lambda1 = min(lambda_1.1, eta_gl/C_R, 2 delta/(4 C_R)),

   and the formula is monotone (computed, A1: raising an upper-bound constant never raises delta or lambda1, raising a
   threshold never lowers them, on 3000 random points and at engineered points where each branch binds; control C1),
   so certified one-sided bounds of the inputs give certified lower bounds of delta and lambda1 (deduced). At the loss
   d = 46,236,449,175,331,158 (CONSTANTS5 R10.1, deduced on its reading; a larger loss is admissible) and every other
   input at its floor, theta0 = 16 and **log10 delta = -(8d + 2) log10 16 - log10 2 = -4.4539386 x 10^17** (A2, exact;
   control C2): the formula at that d delivers no more. When eps_NM/A_2d binds, log10 delta >= -(8d + 2) log10
   theta0_bar - log10(2 A_bar) for any certified theta0_bar >= theta0, A_bar >= A_2d (deduced; at theta0_bar = 10^6,
   A_bar = 10^12 it is -2.219 x 10^18). The inputs and their statuses (A3): d explicit on a reading; the tame constants
   C_k to order N = 21d + 6 ~ 9.7 x 10^17, C1, C2, A_2d, the admissible pair (delta_K, eps_dat, among them two further
   Nash-Moser thresholds eps_ext, eps_slab of Parts IV-IV''' and the data map's modulus), C_J, lambda_1.1, eta_gl and
   C_R not computed; the G-sup equivalence constants explicit in principle; eps_m, eps_t, eps_K chosen. The seven
   inverse bounds enter the C_k, C1, C2, A_2d and delta_K through III.J's inverses and the linear theory; they are not
   the only inputs missing.
   [R4, the reader's nit 5: d moved: CONSTANTS5.md R12.2 has d <= 46,236,517,538,883,361 (R10.1's is withdrawn by
   R12.5), and there log10 delta = -4.4539452 x 10^17 at the floors (inverse6_5a A2, rerun); the formula's monotonicity
   is proved by inspection (R3.3 n6); the inventory A3 is updated (R4.3).]
7. **The stated limit.** lambda1, delta > 0 exist (proved). Explicit lower bounds follow from item 6's formula once its
   inputs are bounded; the inputs certified or explicit are listed above and in round 1; the first input not computed is
   the numerical specification of the operators and spaces (R2.0), after which come (C, h_0), the gauge
   reconstruction, C_ext, the parametrix norms, the scalar-type blocks' sigma_min (scalarblock5.py, in progress) and the
   chain's other inputs.

**Lemma R9 (the absorbed scalar problem is invertible).** At b0 let q >= 0 be smooth with compact support in {r_h < r}, Q
the multiplication by q, s = sgn sigma, sigma real and nonzero. Then box-hat(sigma) - i s Q : X_sigma -> Y_sigma is
invertible. *Proof.* It is a compact perturbation of box-hat(sigma) (Q maps X_sigma into H^s functions supported in a
fixed compact set, which embed compactly into Y_sigma's H^(s-1) there, Rellich), which is Fredholm of index 0 (I.A
Theorem 7.2 (3), I.B Theorem 1.3 (3)); so it suffices that its kernel is trivial. On each harmonic the kernel solves
-Phi'' + (V_l - sigma^2 - i s f q) Phi = 0 in the class (regular across the future horizon, outgoing). The exact identity
Im((equation) conj Phi) = -(Im Phi' conj Phi)' - s f q |Phi|^2 (inverse6_5a A4) integrates, with the end values sigma
|c_+|^2 and -sigma |c_-|^2 (A4), to 0 = -sigma (|c_+|^2 + |c_-|^2) - s int f q |Phi|^2; both terms have the sign of
-sigma, so c_+ = 0 and Phi is a multiple of the outgoing Jost solution with coefficient 0: Phi = 0. Inside the horizon,
Phi = 0 follows as in III.D Proposition 6.2 (d) (the system (r - r_h) Y' = M Y and Gronwall). [] With the wrong sign (s =
-sgn sigma) the two terms can cancel (control C3).
[R3, the verifier's n4: the harmonic-by-harmonic proof presumes q radial, q = q(r); the statement is restricted to radial
q. A non-radial q would need the global flux identity on the slice and unique continuation from the support of q; not
done. R6 needs only some Q = chi W chi with W >= 0, which can be taken radial, so the restriction costs nothing.]
[R4, the reader's nit 3: read "q >= 0 radial": R9's operator is P-hat - i sgn(sigma) Q, so in R6's notation W =
sgn(sigma) q, and R6 needs no sign of W.]

### R2.2 Proposed texts (final; checked against the files as they stand)
[R3: superseded by CONSTANTS5.md R12.7, which folds in pair 1 with the verifier's wording fixes (its minors 1-2: "the
record's fibre metric", "on its reading", the convention that constants are taken >= 1); no new paper pair is given
here. Pair 2's last sentence, "For d, the two finite avoidance conditions stay part of its reading", is no longer true
(rootavoid5 decides them).]
[R5: R12.7 is superseded in turn by CONSTANTS5.md R13.7; read "R13.7" for "R12.7" here.]

These supersede section 7's two pairs: section 7's first old text now occurs twice in CONSTANTS5.md (R9.7 and R10.7
carry the same block 2), and its second (R9.5's clause) is superseded by R10.5's, targeted below.

1. The paper, section 9, "Settling", the bullet's last sentence (occurs exactly once in paper/RESPONSE-HL-5D.md,
   md5 7193c56e... when checked; this pair supersedes CONSTANTS5.md R10.7 block 2, which targets the same sentence):

```old
The passage to the write-out's own function spaces and the
  other constants are not done, so λ1 and δ are still not evaluated.
```

```new
λ1 and δ are positive, as the proof gives them; their
  values are not computed, and the supplement states where the computation of explicit constants stops (supplement
  `docket68/n1star/INVERSE5-SIX.md`, round 2). What the proof's own formulas deliver is bounded above,
  log₁₀ δ < −7.66 × 10¹⁶ and λ1 < δ (computed, `docket68/n1star/checks/deltacap5.py`), and with the loss taken at its
  bound d ≤ 4.624 × 10¹⁶ (supplement `CONSTANTS5.md` R10.1) the formula gives at most log₁₀ δ = −4.45 × 10¹⁷ even with
  every other input at its least value (computed, `checks/inverse6_5a.py`); a lower bound is that formula, monotone in
  each input (computed), evaluated at certified bounds of its inputs. In hand: the zero-energy inverse bound for the
  scalar model (constant 2.81) and for the tensor-type blocks of the linearised operator (3.94), every harmonic, through
  the horizon (deduced from exact identities, with certified arithmetic, `checks/zeroext5.py`, `checks/tensorzero5.py`);
  the trapped set's data at the final black hole (exact), with the fibre metric the trapping estimate needs, of condition
  number about (γ_C/271.5)⁸ (certified, `checks/inverse6_5.py`); the absorption and interpolation steps of the
  high-energy inverses (explicit; the interpolation factor at most 1.00266, certified); the removal of one of the seven
  inverse bounds, which a parametrix replaces; and the resolvent of every master operator behind the two mode-stability
  bounds, every harmonic and every real frequency, in a cut-off norm, carried exactly to the tensor-type blocks of the
  linearised operator and the vector-type blocks of the 1-form wave operator (certified, `checks/inverse6_5m.py`). Not
  computed: the constant of the trapping estimate, which the write-out obtains by a defect-measure contradiction, and the
  a priori constants built on it; the gauge reconstruction and the absorbed problem's inverse in the write-out's norms
  (the latter proved invertible for the scalar wave); the parametrix norms at future timelike infinity; the least
  singular value of the scalar-type zero-energy blocks; and the chain's other inputs (the tame constants to order N, the
  Nash–Moser thresholds of the exterior and slab problems, the gluing's constants). Upstream of all of these: the
  write-out fixes its gauge and damping parameters only below thresholds it proves to exist, and the cut-offs and orders
  of its function spaces only up to admissibility, so explicit constants first need those choices made numerically. This
  is a limit of the explicit computation, not a gap in Theorem 4.
```

2. CONSTANTS5.md, R10.5's open bullet, its clause on the six (occurs exactly once, md5 0320dd90... when checked):

```old
the other six inverse bounds
  (their microlocal constants at L_b0 and certified spectral bounds in the write-out's norms). For d, the two finite
  avoidance conditions stay part of its reading.
```

```new
the other six inverse bounds, as
  INVERSE5-SIX.md states them (round 1 section 5; round 2): I.B:1513's (C, h_0), its symbol data computed; I.B:1685's
  and :1978's a priori constants, which contain it, their absorption and interpolation explicit; III.F'':223's and
  III.D:365's gauge reconstruction and absorbed-problem inverse, their master parts certified (the absorbed problem
  proved invertible for the scalar wave); II.F:1393 eliminated at its site, the parametrix norms and N^0(sigma)'s
  injectivity not computed; and, upstream of all six, numerical admissibility thresholds for the gauge and damping
  parameters and numerical choices of the spaces' cut-offs and orders, which the write-out does not make. The chain to
  lambda1 and delta is assembled as a monotone formula in its inputs (checks/inverse6_5a.py), whose other inputs (the
  tame constants to order N, the admissible pair, the gluing's constants) are not computed either. For d, the two
  finite avoidance conditions stay part of its reading.
```

### R2.3 Programs (md5 at the end of this round)

`checks/inverse6_5a.py` 9/9 (A0-A4, C1-C4); `checks/inverse6_5.py` 17/17 (K1-K8, C1-C9); `checks/inverse6_5m.py` 12/12
(M0-M7, C1-C4); each with its `.out`; md5s in the round's report. Sources read this round: EFFECTIVE-CONSTANTS.md
sections 2-3 (md5 a45e90dc...); proof5/PART-VI4-PARAMS.md sections 1-3 (e7eebbb5...); proof5/PART-III-D2-ZEROENERGY.md
section 4 (cdbe8fe8...); CONSTANTS5.md round 10 (0320dd90...); paper/RESPONSE-HL-5D.md section 9 (7193c56e...);
checks/scalarblock5.py's docstring.

## Round 3 (2026-11-06): the verifier's findings seated

*Status.* Appended; rounds 1-2 keep their text, with bracketed `[R3: ...]` notes after the lines corrected here. The
independent verifier (report-vINV.md) found no Major and confirmed R1, R2-R4, R6, R8, R9, the chain's monotonicity with
the relaxation K1 <= 2 C_d, the uniform-in-l certification (its mutations caught) and the stated limit at source. Seated
here: its minors 3 and 4 and its nits 4, 5 and 6, the ones on this file. Its minors 1-2 (coordination, the paper's
wording) belong to CONSTANTS5.md round 12: **R2.2 is superseded by CONSTANTS5.md R12.7**, and no paper pair is given
here. Its minor 5 and nits 1-3 are INVERSE5-SCALAR's. Changed and rerun, each with its `.out`:
`checks/inverse6_5m.py` (13/13: M7's tensor row from gmodes5's bracket, the factor derived and tested; control C5) and
`checks/inverse6_5a.py` (9/9: A1 labelled proved by inspection). `checks/inverse6_5.py` is unchanged (17/17).
CONSTANTS5.md, N1STAR-PROOF.md and the paper are not edited.
[R5: R12.7 is superseded by CONSTANTS5.md R13.7; read "R13.7" for "R12.7" in this paragraph.]

### R3.1 Minor 3: the high-energy inverse, its factor and its norms (Lemma R3 (b); B3)

*Corrected statement (proved).* Under Lemma R3 (b)'s hypotheses, for Im sigma >= 0 and |sigma| >= C_0 :=
h_0^-1 (1 - nu'^2)^(-1/2), with h and z as in I.B section 8.4 and ||.||_o, ||.||_o' the semiclassical norms at that h,

    ||u||_o <= 2 C (1 - nu'^2)^(-(1-delta)/2) |sigma|^(-1+delta) ||P-hat(sigma) u||_o'    (h = |Re sigma|^-1, the case
                                                                                            Im sigma < nu' |sigma|),
    ||u||_o <= 2 C |sigma|^-1 ||P-hat(sigma) u||_o'                                       (h = |sigma|^-1, delta = 0).

*Proof.* R3 (b) gives ||u||_o <= 2 C h^(-1-delta) ||P_(h,z) u||_o' and P_(h,z) = h^2 P-hat(sigma), so ||u||_o <=
2 C h^(1-delta) ||P-hat u||_o'. In the first case |Re sigma| >= |sigma| (1 - nu'^2)^(1/2) (I.B 8.4), so h^(1-delta) =
|Re sigma|^(-(1-delta)) <= (1 - nu'^2)^(-(1-delta)/2) |sigma|^(-(1-delta)); and h < h_0 holds once |sigma| >= C_0. In
the second, delta = 0 (Theorem 1.3 (2)). [] *The norms.* ||.||_o is H-bar^((s, r + alpha_+, b))_h at h = h(sigma); at
each fixed h it is equivalent to X_sigma's norm (I.B 8.4, "up to an equivalent norm"), with constants depending on h.
So the bound is uniform in sigma in the semiclassical norms, not in X_sigma's; a bound in X_sigma's norms needs those
equivalence constants as functions of h, which are calculus constants and are not computed. B3's statement in round 1,
"||P-hat(sigma)^-1||_(Y_sigma -> X_sigma) <= C_8.1 |sigma|^(-1+delta)", is read the same way (bracketed there).
[R4: C_0 := min(h_ch, (4C)^(-1/N), (4 C C_K)^-1)^-1 (1 - nu'^2)^(-1/2), h_ch the chain's own threshold (R4.1); C is
the larger of Prop. 8.1 (a)'s and (b)-(c)'s constants before absorption (R4.2); and the first display covers the second
case too, as C_0 >= 1 (R4.2).]

### R3.2 Minor 4: uniformity in b

B2 and B3's "no non-constructive step of its own" holds at b0, for one operator, and even there not for every step:
Proposition 8.1 chooses its cover "By compactness, finitely many of these neighbourhoods cover K_Sigma" (I.B:1912-1913)
and "Take nu_1 so small that all of this holds" (I.B:1916-1917). At b0 the dynamics is explicit (VI.A), so an explicit
cover and nu_1 are possible, but they are not made. The chain needs more: constants uniform over b in B_*-bar ("Every
operator family of Parts I-IV is then taken over B_*-bar", proof5/PART-VI4-PARAMS.md step (5), READ), and I.B
section 9 obtains that uniformity by compactness of the parameter set ("by compactness of B, finitely many suffice")
and by running "the two arguments by contradiction (Proposition 6.4 and the absorption in Proposition 6.7 (a))" with
sequences (h_j, z_j, b_j), b_j -> b_inf (I.B:2044-2053, READ; md5 df7e5206...). So **constants uniform in b are a
further input, not computed**, even if every constant at b0 were explicit; the same holds for the mode-stability
bounds near b0 (III.F'' Proposition 4.1 and III.D Proposition 6.3 cover a compact set of sigma by I.A Theorem 8.1's
neighbourhoods). At b != b0 the operators do not separate, so the per-mode certificates of section 4 do not reach them;
explicit uniform constants would need Lipschitz bounds in b in the write-out's norms (the BFAM rows of CONSTANTS5.md
section 3.1).

### R3.3 The nits

- *n4 (Lemma R9).* Restricted to radial q (bracketed at R9): the harmonic-by-harmonic proof presumes q = q(r). A
  non-radial q would need the global flux identity on the slice and unique continuation from the support of q, not done
  here. R6 needs only some Q = chi W chi with W >= 0, which can be taken radial.
  [R4: read "q >= 0 radial"; in R6's notation W = sgn(sigma) q, and R6 needs no sign.]
- *n5 (inverse6_5m M7).* The tensor row is now written in gmodes5 G1's variables: h = 2 r^2 H T, F := L h = D Ric(h) =
  -r^2 B[H] T with B[H] = box2 H + 3 f H_r/r - (k_T^2 + 2) H/r^2, and the master source G = -f r^(3/2) B, since
  f r^(3/2) B[r^(-3/2) Phi] = -Phi_tt + f (f Phi_r)_r - V_T Phi (checked here exactly, independently of gmodes5's code).
  Per unit dr_*, |h|^2 r^3 f = 4 f |Phi|^2 (c = 4) and |G|^2 = f (|F|^2 r^3 f) (k = 1), so ||h||_I <= (c k)^(1/2)
  (max_I f) B ||L h||_I = 2 (15/16) B ||L h||_I and ||chi_I (2 L-hat_b0)^-1 chi_I|| <= (15/16) B. The program derives
  (c k)^(1/2) (max_I f)/(operator factor) for each of the three rows and tests it against the printed 15/16; control C5:
  round 1's G = 2 f r^(3/2) B (k = 4) gives 15/8 and fails. The printed bounds (13.12, 20.11, 41.30, 122.7 and 21.39)
  are unchanged.
- *n6.* (i) Section 3's "0.0052072 at gamma_C = 10^6, eta = 10^-4" is lam_max/(gamma_C eta^2), certified in [0.005207,
  0.005208], against the leading order's 0.0052072 (bracketed there). (ii) R6's "the absorption covers the photon
  sphere" is moot at fixed sigma, where there is no trapping; withdrawn (bracketed there). (iii) A1's monotonicity is
  proved by inspection (with K1 <= 2 C_d each K_i, theta0, eps_NM, delta and lambda1 are monotone compositions of
  monotone maps) and checked numerically; inverse6_5a now says so. (iv) R4's C_a is R3 (a)'s constant after
  absorption, 2 C_a in R3 (a)'s notation, so (6.11)'s constant is 8 F C_a <= 8.02128 C_a there (bracketed at R4).
  (v) Path styles: R2.2, which mixed "supplement `CONSTANTS5.md`" and "`docket68/n1star/...`", is superseded; this
  round names files relative to docket68/n1star.

### R3.4 The stated limit, amended

R2.1 item 7 stands with one addition, before the chain's other inputs: **constants uniform over b in B_*-bar**, which
the write-out obtains by compactness and by arguments by contradiction (I.B section 9; III.F'' Proposition 4.1;
III.D Proposition 6.3) and which no explicit computation here supplies. So the order is: the numerical specification
of the operators and spaces; at b0, (C, h_0) in (6.6), the compactness choices of Proposition 8.1, the gauge
reconstruction, C_ext, the parametrix norms and the scalar-type blocks' sigma_min; uniformity in b; and the chain's
other inputs. lambda1, delta > 0 exist (proved); their explicit lower bounds are not computed. This is a limit of the
explicit computation, not a gap in Theorem 4.
[R4, the reader's nit 4: two additions, not one: Proposition 8.1's compactness choices at b0, and the uniformity in
b.]

### R3.5 Programs and sources (round 3)

`checks/inverse6_5m.py` 13/13 (M0-M7, C1-C5; 185 s), md5 5a8c3b3f...; its `.out` 07defe14...; the printed bounds of
rounds 1-2 unchanged (the transfers 13.12, 20.11, 41.30, 122.7 and 21.39, 40.39, 90.14, 272.7). `checks/inverse6_5a.py`
9/9 (A0-A4, C1-C4), md5 92712dbf...; its `.out` ed5d26cd... (A0 prints CONSTANTS5.md's current md5; its quotes are
found by content). `checks/inverse6_5.py` unchanged, 17/17, md5 650c62d0..., `.out` 781d06cf.... Sources read this
round: the verifier's report-vINV.md; proof5/PART-I-B-HIGHENERGY.md:1905-1925, 2038-2055 (md5 df7e5206...);
proof5/PART-VI4-PARAMS.md step (5) (e7eebbb5...).

## Round 4 (2026-11-06): the second reader's findings seated

*Status.* Appended; rounds 1-3 keep their text, with bracketed `[R4: ...]` notes after the lines amended here. The
second independent reader (report-vINV2.md, on md5 0753ef7b...) CONFIRMED this file with no Major: it re-derived R3.1,
found round 3's items seated correctly and raised one new minor here. Seated below, each re-derived: its minor 1 (the
thresholds, R4.1), nits 1-2 (both cases of the bound, one name for the constant, R4.2), minor 3 (inverse6_5a's
inventory and d, R4.3), nits 3-5 and its three optional remarks (R4.4). Its minor 2 and nits 6-8 are
INVERSE5-SCALAR.md's; its inconsistency (a) (CONSTANTS5.md R12.5 and R12.7 pair 1 against A.1 and R2.0) is for
CONSTANTS5.md's reader; neither is touched here. Rerun, each with its `.out`: `checks/inverse6_5a.py` 11/11 (A5 and
control C5 new), `checks/inverse6_5.py` 17/17 and `checks/inverse6_5m.py` 13/13 (their exit code only changed).
CONSTANTS5.md, INVERSE5-SCALAR.md, N1STAR-PROOF.md and the paper are not edited.

### R4.1 Minor 1: the chains' own thresholds (Lemma R3; B2, B3)

*The finding.* Lemma R3's thresholds are the absorption's alone, but its hypotheses are the record's displays before
absorption, which hold only below thresholds of their own. *READ* (proof5/PART-I-B-HIGHENERGY.md, md5 df7e5206...).
Prop. 8.1 (a): "There are nu_1 > 0, h_0 and C such that for z in z_0 + i[0, nu_1], h < h_0" (:1881-1882). Its proof
assembles the display before absorption from Propositions 5.2, 5.3 and 5.5, Corollary 4.6, (7.2) and Theorem 6.8, the
last "for z in z_0 + i[h beta, nu'], h < h_0" (:1704) and proved from (6.4), (6.6) and Proposition 6.7 (:1707-1716),
(6.6) itself holding "for z in z_0 + i[h beta, nu'], h < h_0" (:1505); then "for h < h_0 the last two terms are
absorbed, which is (8.1)" (:1929-1930). Prop. 6.7 (a) builds its display from Proposition 4.2, Corollary 4.6 and
Proposition 6.4, i.e. (6.6) (:1674-1681), and "the last term is absorbed for h < h_0" (:1682-1683). So each record h_0
is the minimum of a chain threshold and an absorption threshold, and Lemma R3 supplied only the second.

*Corrected statement (proved).* Let h_ch' be the threshold below which Prop. 6.7 (a)'s display before absorption
holds, and h_ch the smallest of those below which Prop. 8.1 (a)'s, (b)'s and (c)'s displays before absorption hold
((b)-(c) run the same cover and absorption with delta = 0, :1931-1938). Both are at most B1's h_0, (6.6)'s: (6.6)
enters Prop. 6.7 (a) directly and Prop. 8.1 (a) through Theorem 6.8.
(a) If ||u|| <= C_a h^-2 ||P'u|| + C_a h^N ||u||_(-N 1) for h < h_ch' and ||u||_(-N 1) <= ||u||, then
||u|| <= 2 C_a h^-2 ||P'u|| for h < h_0' := min(h_ch', (2 C_a)^(-1/N)).
(b) If ||u||_o <= C (h^(-1-delta) ||Pu||_o' + h^N ||u||_o + ||u||_(-K 1)) for h < h_ch and ||u||_(-K 1) <=
C_K h ||u||_o, then ||u||_o <= 2 C h^(-1-delta) ||Pu||_o' for h < h_1 := min(h_ch, (4C)^(-1/N), (4 C C_K)^-1), and
R3.1's bounds hold for Im sigma >= 0, |sigma| >= C_0 := h_1^-1 (1 - nu'^2)^(-1/2).
*Proof.* (a) For h < h_0', the display holds and C_a h^N <= 1/2, so its last term is at most ||u||/2 and moves to the
left (||u|| is finite). (b) For h < h_1, the display holds, C h^N <= 1/4 and C C_K h <= 1/4, so the last two terms are
at most ||u||_o/2. For R3.1: if Im sigma < nu' |sigma|, then |Re sigma|^2 = |sigma|^2 - (Im sigma)^2 > |sigma|^2
(1 - nu'^2), so h = |Re sigma|^-1 < (1 - nu'^2)^(-1/2) |sigma|^-1 <= h_1 when |sigma| >= C_0; otherwise h = |sigma|^-1
<= C_0^-1 = h_1 (1 - nu'^2)^(1/2) < h_1, as nu' > 0. So h < h_1 in both cases, the record's strict thresholds
included, and R3.1's proof goes through unchanged. []
*What it changes.* B2's threshold is h_0', not (2 C_a)^(-1/N); B3's C_0 is h_1^-1 (1 - nu'^2)^(-1/2), not explicit in
C alone. The constants do not change: (6.11)'s 4 F C_a (8 F C_a in R3 (a)'s notation) and R3.1's 2 C. Nor does F:
it is a sup over sigma_0 >= h_0'^-1, a set that shrinks with h_0', and K6 certifies F <= 1.002659 for every h_0' <= 1
(C_a >= 1/2 may be assumed, as enlarging C_a keeps the hypothesis true, and then h_0' <= 1). The stated limit does not
change: h_ch' and h_ch are composed, like C_a and C, of (6.6)'s (C, h_0) and the calculus constants of the other
estimates in their chains, so "B2 and B3 contain B1" stands and no item is added to R3.4's order. [R4] notes: the
status line, section 0 (B2, B3, "What changed"), section 1 (B3), Lemma R3, section 5 (B2, B3), R2.1 item 4, R3.1.

### R4.2 Nits 1-2: both cases of I.B 8.4, and one name for the constant

*Nit 1 (proved).* C may be taken >= 1/4 (enlarging C keeps R3 (b)'s hypothesis true), so h_1 <= (4C)^(-1/N) <= 1 and
C_0 >= (1 - nu'^2)^(-1/2) >= 1. For |sigma| >= C_0 and delta in [0, 1] the second case's bound lies under the first's:
2 C |sigma|^-1 <= 2 C |sigma|^(-1+delta) <= 2 C (1 - nu'^2)^(-(1-delta)/2) |sigma|^(-1+delta). So one bound covers the
whole range of Theorem 1.3 (3),

    ||u||_o <= 2 C (1 - nu'^2)^(-(1-delta)/2) |sigma|^(-1+delta) ||P-hat(sigma) u||_o'   (Im sigma >= 0, |sigma| >= C_0),

delta = delta_Gamma(Im sigma - epsilon) in [0, 1], in the semiclassical norms at h = h(sigma) (R3.1). *Computed*
(floats on a sample; the proof is the line above): inverse6_5a A5 draws 2 x 10^5 random (sigma, nu', h_1, delta) with
|sigma| > C_0 (h_1 is the program's h_0) and finds h^(1 - delta_case) <= (1 - nu'^2)^(-(1-delta)/2) |sigma|^(-1+delta),
h <= h_1 and C_0 >= 1 in both cases of I.B 8.4's h: 0 violations. Control C5, the exponent -(1-delta)/4: 18,694
violations (the reader's mutant of the same exponent: 18,968 on its own sample).
violations (the reader's mutant of the same exponent: 18,968 on its own sample).
[R5: that sample had |sigma| = C_0 (1 + 10^U(0, 3)) >= 2 C_0 and never reached the threshold region; widened to
U(-8, 3) in R5.2, still 0 violations, and the mutant M2 is killed there.]
*Nit 2 (a convention, fixed from this round).* C is R3 (b)'s constant before absorption, the larger of the constants
of Prop. 8.1 (a)'s and (b)-(c)'s displays before absorption (case 1 of I.B 8.4 is part (1) with nu = 2 nu', so (a) and
possibly (b); case 2 is (c), Theorem 1.3 (2)); C_8.1 := 2 C, the constant with which (8.1) then holds after absorption.
Round 1 used C_8.1 in both senses: in section 0 (B3) and section 5 (B3), "2 C_8.1" and "(4 C_8.1)^(-1/N)" have C_8.1
for C; in section 1 (B3), "C_8.1 |sigma|^(-1+delta)" is (8.1)'s constant, 2 C. Each site carries an [R4] note saying
which. In either reading the bound is 2 C (1 - nu'^2)^(-(1-delta)/2) |sigma|^(-1+delta) = C_8.1 (1 - nu'^2)^(-(1-delta)
/2) |sigma|^(-1+delta). The same factor 2 for C_a was settled in R3.3 n6 (iv).

### R4.3 Minor 3: inverse6_5a's inventory, and d

*The finding.* A3 still printed "two avoidance conditions undecided" and "I.C:497 ... not computed (in progress,
scalarblock5.py)", had no row for uniformity in b, and pinned R10.1's d, which CONSTANTS5.md R12.5 withdraws.
*Seated* in `checks/inverse6_5a.py` (rerun, 11/11):
- d's row: "d <= 46,236,517,538,883,361 (CONSTANTS5 R12.2; deduced on its reading, Lambda on (1, 3 + eps_K] as R9.1
  takes it; the avoidance conditions decided, rootavoid5 23/23)"; D_BAR and A0's quote of d are R12.2's (A0 finds it
  by content in CONSTANTS5.md, md5 e4728113...).
  [R5: the row now reads "... as R9.1 takes it, at the record's computational point (R13.2); the avoidance conditions
  decided, rootavoid5 26/26)"; d is unchanged; CONSTANTS5.md's md5 is now b9617854... (R5.3).]
- I.C:497's row: "sigma_* not computed; computed: sigma_min(L_2) <= 2.6180e-7 at (s, alpha) = (1, -1), so the inverse
  constant >= 3.81e6, at the record's computational point (INVERSE5-SCALAR.md A.6)", fed by "sigma_* > 0, a lower
  bound uniform in l (A.8)"; the value is INVERSE5-SCALAR's, not recomputed here.
- A new row: "constants uniform over b in B_*-bar | not computed | I.B section 9 ...; III.F'' Proposition 4.1, III.D
  Proposition 6.3 | every bound of B1-B6 near b0 (R3.2)". A3 checks the inventory's 15 rows.
*Re-derived* (A2, mpmath at 60 digits, the formula matched to 10^-30): at d = 46,236,517,538,883,361 with every
other input at its floor, theta0 = 16 and log10 delta = -(8d + 2) log10 16 - log10 2 = -4.45394517576 x 10^17, inside
A2's pin [-4.4540, -4.4539] x 10^17 and agreeing with R12.2's -4.453945 (CONSTANTS5.md:3190) and the reader's value;
R2.1 item 6's -4.4539386 x 10^17 is R10.1's d (bracketed there). At theta0_bar = 10^6, A_bar = 10^12 the bound is
-22.1935 x 10^17, item 6's -2.219 x 10^18 to the figures printed. Control C2 still fails at alpha = 8d. The paper's
-4.45e17 is unaffected.

### R4.4 Nits 3-5 and the optional remarks

- *Nit 3.* R2.1 item 2 now carries the radial note: Lemma R9 holds for radial q >= 0 (R3.3 n4), which is all R6 needs.
  The wording "W >= 0" in R3.3 n4 and at R9 is read "q >= 0 radial": R9's operator is P-hat - i sgn(sigma) Q, Q = chi
  q chi, so in R6's notation (P_1 = P-hat - i chi W chi) W = sgn(sigma) q, and R6's proof is the resolvent identity
  with ||W|| = ||q|| (inverse6_5 K8), no sign used. Bracketed at R2.1 item 2, at R9 and at R3.3 n4.
- *Nit 4.* R3.4 adds two items to R2.1 item 7's order, not one: Prop. 8.1's compactness choices at b0, and the
  uniformity in b (compared line by line: item 7 lists the specification, (C, h_0), the gauge reconstruction, C_ext,
  the parametrix norms, sigma_min and the chain's other inputs). Bracketed at R3.4.
- *Nit 5.* d moved (R4.3); bracketed at R2.1 item 6.
- *Optional.* The status line (:3) now says the file has been read by two verifiers, and section 0's "What changed"
  paragraph (:52-55) carries the R3.2 caveat on "no non-constructive step of their own" (at b0, for one operator,
  Prop. 8.1's cover and nu_1 aside). All three programs now end with `sys.exit(0 if all(OK.values()) else 1)` in
  every mode, `--selftest` or not: a probe that forces inverse6_5a's A4 to fail in full mode exits 1, the unforced full
  run exits 0 (the probe lives in the scratchpad, not in the tree).

### R4.5 Programs and sources (round 4)

`checks/inverse6_5a.py` 11/11 (A0-A5, C1-C5; 11 s), md5 132a57af...; its `.out` 9209e219.... `checks/inverse6_5.py`
17/17 (171 s), md5 efa230b1... (round 3's 650c62d0... with the exit line changed), `.out` 595a36d5....
`checks/inverse6_5m.py` 13/13 (278 s), md5 9f2eca91... (round 3's 5a8c3b3f... with the exit line changed), `.out`
77de537c.... The printed values are unchanged: F <= 1.002659 and 4.01064 C_a; the transfers 13.12, 20.11, 41.30, 122.7
and 21.39, 40.39, 90.14, 272.7. Sources read this round: report-vINV2.md; proof5/PART-I-B-HIGHENERGY.md:200-224,
1498-1510, 1668-1717, 1878-1945, 1955-1980 (md5 df7e5206...); CONSTANTS5.md R12.2, R12.5 (md5 e4728113...);
INVERSE5-SCALAR.md A.6, A.8 (read at md5 4e72dc60...; it has since moved, to 2c600b5b... at this writing, by its own
round, with A.6's 2.6180 x 10^-7 and 3.81 x 10^6 and A.8's sigma_* > 0 uniform in l standing as A3 quotes them).

## Round 5 (2026-11-06): the confirming reader's nits

*Status.* Appended; rounds 1-4 keep their text, with bracketed `[R5: ...]` notes after the lines amended here. The
confirming reader of round 4 CONFIRMED this file with no Major and no minor, and re-derived R4.1's strict threshold.
Seated below: its nits 1-4, 8 and 9 (the others are not on this file), and the supersession of CONSTANTS5.md R12.7 by
its R13.7. Rerun with its `.out`: `checks/inverse6_5a.py`, 12/12 (control C6 new); nothing else changes, so
`checks/inverse6_5.py` and `checks/inverse6_5m.py` are not rerun. CONSTANTS5.md, INVERSE5-SCALAR.md, N1STAR-PROOF.md
and the paper are not edited; no earlier note is edited.

### R5.1 Nits 1-3: wording

- *Nit 1 (Lemma R3's [R4] note).* It wrote "h <= min(...)"; R4.1 proves the conclusions for h < min(h_ch',
  (2 C_a)^(-1/N)) and h < min(h_ch, (4C)^(-1/N), (4 C C_K)^-1) only, the record's chain thresholds being strict
  ("h < h_0", I.B:1505, :1704, :1881). Read "<" (bracketed there). R3.1 is unaffected: |sigma| >= C_0 gives h < h_1
  (R4.1).
- *Nit 2 (section 5, B3).* "The single missing input: C_8.1, the constant of (8.1)" read with the [R4] note below it
  (C_8.1 before absorption there) said two things; it is read "(8.1)'s chain constant before absorption", the
  record's (8.1) constant being twice it (R4.2; bracketed there).
- *Nit 3 (section 0, B2).* h_0 = min(h_ch', (2 C_a)^(-1/N)) is the chain's threshold and the absorption threshold
  together, not "the absorption threshold" (bracketed there).

### R5.2 Nit 4: A5 now samples the threshold region

*The finding.* A5 drew |sigma| = C_0 (1 + 10^U(0, 3)), so |sigma| >= 2 C_0 always and the region |sigma| -> C_0, where
the threshold binds, was never tested; the reader's mutant M2 (C_0 = h_0^-1 (1 - nu'^2)^(-1/4)) survived. *Seated.*
|sigma| = C_0 (1 + 10^U(-8, 3)), the rest unchanged (seed 3, 2 x 10^5 draws). *Computed* (inverse6_5a, rerun): A5, 0
violations; new control C6, M2: 11,440 violations under U(-8, 3), and 0 under round 4's U(0, 3), printed beside it,
which is the reader's finding reproduced. Why M2 needs the region (deduced): in case 1, h <= h_0 needs |Re sigma| >=
h_0^-1, and |Re sigma| > |sigma| (1 - nu'^2)^(1/2); under M2, |sigma| >= C_0 gives only |Re sigma| > h_0^-1 (1 -
nu'^2)^(1/4), short of h_0^-1, while |sigma| >= 2 C_0 gives 2 h_0^-1 (1 - nu'^2)^(1/4) >= h_0^-1 whenever nu'^2 <=
15/16, which holds in all but a small corner of the draw nu' in [0.01, 0.99]. Control C5 is unchanged at 18,694: its
violation, h^(1-delta) against the factor with exponent -(1-delta)/4, reduces to (cos theta)^(-(1-delta)) > (1 -
nu'^2)^(-(1-delta)/4), which does not involve |sigma|.

### R5.3 Nits 8-9: the inventory's d row, and A0's md5

- *Nit 8.* The A3 row reads "d <= 46,236,517,538,883,361 (CONSTANTS5 R12.2; deduced on its reading, Lambda on (1, 3 +
  eps_K] as R9.1 takes it, at the record's computational point (R13.2); the avoidance conditions decided, rootavoid5
  26/26)". CONSTANTS5.md R13.2 names the point as part of d's bound ("the loss at the record's computational point,
  which lies outside the proved set", READ) and leaves the integer unmoved ("d's integer does not move", R13 status);
  `checks/rootavoid5.out` (md5 d4b4e2a2..., the one CONSTANTS5.md R13 pins) ends "26/26", 26 PASS, 0 FAIL (counted
  here). D_BAR, A0's quote of d and A2's -4.45394517576 x 10^17 are unchanged (bracketed at R4.3).
- *Nit 9.* `checks/inverse6_5a.out` is regenerated: A0 finds its ten quotes by content in CONSTANTS5.md at md5
  b96178545d67619ab2bed9ecf1af714f and prints it.
- *R12.7 -> R13.7.* CONSTANTS5.md R13.7, "Final replacement text for the paper (supersedes R12.7)" (READ), supersedes
  R12.7; the three notes here that send R2.2 to R12.7 (the status line, R2.2's [R3] note, round 3's status) now carry
  `[R5]` notes reading R13.7. Round 4's mention of "R12.7 pair 1" names what the second reader read and is left.

### R5.4 Programs (round 5)

`checks/inverse6_5a.py` 12/12 (A0-A5, C1-C6; about 11 s), md5 550e88be...; its `.out` a70ec796.... Unchanged since
round 4: `checks/inverse6_5.py` 17/17 (efa230b1..., `.out` 595a36d5...) and `checks/inverse6_5m.py` 13/13 (9f2eca91...,
`.out` 77de537c...). Sources read this round: CONSTANTS5.md R13 status, R13.2 and R13.7's heading (md5 b9617854...);
checks/rootavoid5.out.
