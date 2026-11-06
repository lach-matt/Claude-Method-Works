# CONSTANTS5 -- lambda0, d, lambda1 and delta made explicit as far as is true

*Status (2026-11-02).* New; not yet read by a verifier. Labels as in the record: **computed** (a program here, exact or
certified arithmetic unless it says floating point, with a control that must fail and does), **deduced** (an argument
written here from the cited lines), **READ** (quoted from the record or a source). Nothing here edits the paper, the
log, EFFECTIVE-CONSTANTS.md, LOSS-D.md or E2-PILOT.md. Programs: `checks/lzeroaudit5.py`, `checks/lzeroconst5.py`,
`checks/dweights5.py`, `checks/nrows5.py`, `checks/deltacap5.py`, each with its `.out`; all pass.

## 0. Summary

- **lambda0 (Theorem 1) is constructive** (deduced; the census `lzeroaudit5.py` A1-A3). Every step of N1STAR-PROOF.md
  sections 0-6 (Theorems E, A, D) is an energy or transport estimate, Gronwall, Sobolev, a mollifier bound, Picard or
  Kato-Majda iteration, or a perturbation of an explicit margin; no step of the kinds N1-N4 occurs. The one compactness
  argument (Lemma 6.4's weak-* Galerkin limit) gives existence, its bound being the uniform estimate. lambda0 is an
  explicit minimum of eight closed-form terms [Round 2, V-m4: nine; Proposition 6.5's ball invariance was missing]
  (section 1.3, checked `lzeroconst5.py` Z4). At the paper's numerical point its geometric leaves are certified
  (lambda_Omega <= 0.026986, tau_end - tau0 <= 5.937209, eps1 >= 5.2617e-4, C_S <= 43.216); **no number for lambda0**:
  its other leaves are bounds on the approximant's profiles g_1, ..., g_10 [Round 2, V-n4: "of stages 1-10" read loosely;
  the profiles come from stage 0 and the nine stage solves 1-9 of Lemma 5.3, as section 1.5 says], which nobody has
  computed (section 1.5). [Round 2, V-M2: lambda0 here is the threshold this proof delivers, the minimum of its own
  terms; it is not the largest lam for which Theorem 1's conclusions hold.] The same audit settles EFFECTIVE-CONSTANTS.md
  E5's first item: C_J and lambda_1.1 of PART-VII Lemma 1.1 are the same theorems at order k = J + 4, so they are
  constructive too.
- **d.** The weights now have numbers (section 2.1); (G) is checked against the generators pi_1 E^C_I and does not bind;
  at these weights the loops are counted exactly and **d >= 8,407,505,890,317,054** (computed, `dweights5.py` W3). Two of
  LOSS-D's open items are closed: the data's E^C_I **does carry logarithms below l_I** (the assembly's E_0 = {(j, 0) : j
  >= 2} meets E^C_I at 2 and 3), so the one-off application costs 12, 30 or 48 by reading, not 6 (W5); and III.I'
  Proposition 2.1 takes **5 steps, loss 10**, one above its floor (W6). The level-2 container grows to 52,025,761 points
  per level once E^C_I's chains are counted [Round 2, V-M1: round 1 printed 53,496,063, counting the chain of
  lambda_sharp + 1 = 2.5099 twice], so LD15's comparison cannot show that loop shorter (W4). The composition gives **d <=
  1.7892e16 + 1.0649e8 c** [V-M1: was 1.8127e16] on hypotheses H1-H4, c the uncounted per-level loss (W8): a conditional
  bound, not a certified one. The exact obstructions are in section 2.6.
- **lambda1 and delta.** No quantitative replacement is computed here. Each of the 35 non-effective rows has its
  replacement and the precise missing input (`nrows5.py` R1); a fifth kind the ledger's census did not search, bounds
  from the closed graph, open mapping and Banach-Steinhaus theorems, occurs at 16 lines of proof5, 13 of which carry a
  constant (R2) [Round 2, V-m2: 18 lines with a pattern that also finds "closed-graph" and "Banach and Steinhaus", 10
  carrying a constant or an order, one more with a constructive alternative beside it; R2.4 (b)]; and the replacements
  must be built in a fixed order, the covering and calculus constants first (R3). Upper bounds are certified: **log10
  delta < -7.666e16 and lambda1 < delta**, from the proof's own formulas, with the upper-bound constants taken >= 1
  (`deltacap5.py`).

## 1. lambda0 (Theorem 1)

### 1.1 The point

P*: l5 = 1/10 and mu0 = 1 (L = mu0/l5^2 = 100, the paper's first seed, `growth5.py`), A = 1, the numerics' envelope
sin^4(pi (v - 1/2)/3) on [1/2, 7/2], T = 1, tau0 = -2 (v_start - tau0 = 5/2 > sqrt(mu0) + 1), K = 6, hence k = 6 and N =
K + 3 = 9 (READ, N1STAR-PROOF.md 0.4, 6.4), and the free inner radius a := q0/2 (delta0 = q0/2). Theorem 1 states no
numerical point; this is the one its section 9 computes at.

- *The envelope is not admissible as it stands* (computed, `lzeroconst5.py` Z0). sin^4 x = (3 - 4 cos 2x + cos 4x)/8
  has derivatives 0, 0, 0, 0, 24 at 0, so the envelope is C^3 and not C^4 at v_start and v_end, and Theorem 1 asks
  env in C_c^inf. Every certified leaf below depends on the envelope only through mu_end = mu0 + (2/9) A^2 int env^2, so
  it holds for any smooth envelope with the same integral; the profile bounds of section 1.5 would not.

### 1.2 Constructivity (deduced; census computed, `lzeroaudit5.py`)

- *A1.* N1STAR-PROOF.md lines 1-805 (md5 57d896ae1da4845f3c94c66d7b087a41) searched for every word of the four kinds of
  EFFECTIVE-CONSTANTS.md section 3 (contradiction, compactness, Rellich, Fredholm, subsequence), for closed graph,
  Baire, weak limits, open conditions and "small enough", and for every threshold phrase (lam0, lam1, eps1, eps2, "lam
  small", "depending only on", Gronwall, Picard, "there is/are"): 61 hits, each read in context and classified: 35 X
  (no constant produced), 3 G (the Galerkin weak-* limit of Lemma 6.4, lines 744-745: existence; the constant is the
  uniform bound), 8 E (eps1 at lines 160, 170, 215; the Sobolev constant at 182-183; eps2 at 425), 15 T (thresholds),
  **0 of the kinds N1-N4**.
- *A2.* The T rows reach exactly the eight terms of the formula of section 1.3, and each term has a source line.
- *A3.* Every citation of those lines is classified: [BH17] enters through C_S (certified here); [GO13] and [DS23]
  Remark 2.3 enter through Lemma 6.4's constant (Moser and commutator bounds, effective at integer orders, s0 = 6, s =
  8 being admissible for s0 > 3/2 + 4); [AO14]'s Kato-Majda scheme is a contraction with an explicit factor; [SY21]'s
  extension enters through eps2 (an explicit operator); [DS23] Theorems 2.4, 2.6 and [LY22] give existence and
  restarts only, so their existence times never enter lambda0.
- *The open-and-closed argument* (line 402) and the uniqueness arguments (133, 446) produce no constant.
- Controls: a planted "by contradiction ... subsequence ... compactness" sentence is left unclassified (C1); the census
  finds the ledger's N1 site PART-I-C-LOWENERGY.md:495-498 (C2); removing one table row leaves one hit unclassified (C3).

### 1.3 The formula (deduced from Steps 1-3 and 7 of section 4, Proposition 6.5 and Lemma 6.3 (c); `lzeroconst5.py` Z4)

    lambda0 = min{ lambda_Omega,  eps1/(2 C_app),  [min(eps1, eps2)/(4 C_inf M)]^(1/(K-3)),  [1/(2 C_dw M)]^(1/(K-4)),
                   1/(C3 C_N M^2),  [m_c/(2 C_c C0)]^(1/(N-3)),  (2 C_k)^(-1/(N-3)),  m_s/C_s },

    M = C3 (C_D + 1 + C_R) + 1,    C3 = C_st C2 exp(C2 (tau_end - tau0)) (1 + tau_end - tau0),    K = 6, N = K + 3.

[Round 2, V-m4: a ninth term belongs in the minimum, (4 C_b C0)^(-1/(N-3)): Proposition 6.5's iterates stay in the ball
of radius 2 C0 lam^(N-2) (N1STAR-PROOF.md:771-772) only when 4 C_b C0 lam^(N-3) <= 1, C_b the constant of the quadratic
remainder; `lzeroconst5.py` and `lzeroaudit5.py` now carry it.]

- *The terms.* lambda_Omega = min(1, delta0)/10 (section 2's standing condition, the paper's lambda_Omega). Step 3
  needs g = g_app + w within eps1 of g0 (|g_app - g0| <= C_app lam, |w| <= C_inf lam^-3 N <= 2 C_inf M lam^(K-3), each
  within eps1/2 [Round 3, M1: the halves are this note's choice; Step 3 (N1STAR-PROOF.md:355-357) asks only the sum,
  so any split (1 - theta, theta) gives a valid closed form, and the proof's lambda0 is below eps1/C_app]), |w| <= eps2/2
  for Step 8's cut-off, and |dw| <= 2 C_dw M lam^(K-4) <= 1 so that M1 does not depend on M. Step 7 needs C3 C_N M^2 lam
  <= 1. Proposition 6.5 needs the frozen coefficients within their margin, 2 C_c C0 lam^(N-3) <= m_c, and the contraction
  factor C_k lam^(N-3) <= 1/2; Lemma 6.3 (c) needs the signs of alpha and S A0, C_s lam <= m_s. Here C_inf, C_dw are C_S
  times Step 1's constant, C2 the constant of Steps 4-6, C_st Step 2's, C_N the nonlinear one, C_R and C_D those of (E3)
  and (E4).
- *Z4 (computed, floating point).* On 400 random inputs the closed form meets every condition at lambda0 and fails one
  at lambda0 (1 + 10^-6); without its Step-7 term it violates a condition on 341 of them (control) [Round 3, nit:
  `lzeroconst5.out` prints 360].
- *Its shape* (deduced). lambda0 is polynomial in every constant except through exp(C2 (tau_end - tau0)), Gronwall's
  factor, which enters at most to the power 3 (the term 1/(C3 C_N M^2), M >= C3). Nothing like delta's
  theta0^-(8d+2) occurs: Theorem 1 loses no derivatives.

### 1.4 The certified leaves at P* (computed, exact rationals with certified roots, `lzeroconst5.py` Z1-Z3)

| leaf | value at P* | how |
|---|---|---|
| q0 = (sqrt72 mu0 l5^2)^(1/4) | 0.539717577 (width < 1e-25) | q0^8 = 9/1250, integer 8th root |
| a = delta0 = q0/2 | 0.269858789 | choice |
| mu_end | 227/192 = 1.182292 | int sin^8 over [1/2, 7/2] = 105/128 |
| q_end = q0 mu_end^(1/4), tau_end = V - q_end | 0.562791746, 3.937208254 | v - r_q(v) increasing (1 - q0 (2/9)/4 > 0) |
| b(tau0), tau_end - tau0 | 13.437208254, 5.937208254 | N1STAR-PROOF.md (1.1) |
| lambda_Omega = q0/20 | 0.026985879 | min(1, delta0)/10 |
| eps1 (Lemma 1.1 (e)) | >= 5.2617e-4 in the operator norm, 1.0523e-4 per entry | below |
| C_S (Lemma 2.1) | <= 43.2158 | below |

- *eps1.* sup_Omega |g0^-1|_op <= n := 1 + 2 mu_end/a^2 <= 33.470 (|L0 (x) L0| = |L0|^2 = 2; checked at 2000 random
  points, ratio <= 0.986), so |g^-1 - g0^-1| <= n^2 eps/(1 - n eps). The margins of (a)-(c) are 1, mu0/a^2 - 1 = 12.73,
  mu0/a^2 = 13.73 and 3/5 (d(v + tau) = 2 dtau + dr has Euclidean norm^2 5 and g0^-1 value -3 - mu/r^2); the least,
  3/5, gives eps1 := (3/5)/(n^2 + (3/5) n). Control: an explicit perturbation at r = a making d(v + tau) null has
  operator size 27.2 > eps1 (floating point), and refutes the claim that 1.01 times its size would do. eps1 is
  sufficient, not sharp. [Round 2, V-m5, bracket added in Round 3: this control, at r = a where d(v + tau) need not be
  timelike, accepted any eps1 below 27; replaced by the sharp one on the outer boundary, `eps1hyp5.py` H3.]
- *C_S.* For x in an annulus of width >= 1 in R^4 the cone of height 1/2 and aperture pi/3, outward when |x| <= (a +
  b)/2 and inward otherwise, lies in the annulus; with psi(t) = p(t/h), p(s) = (1 - s)^3 (1 + 3s + 6s^2), f(x) =
  (-1)^3/2! int_0^h t^2 d_t^3 (psi f) dt averaged over the cap (|S_pi/3| = 2 pi (pi/3 - sqrt3/4) >= 3.8587) and
  Cauchy-Schwarz give C_S = (h/sqrt2)/(2 |S_pi/3|^(1/2)) max_j C(3, j) h^-(3-j) sup|p^(3-j)| <= 43.216 (the sups
  1.003, 1.884, 5.793, 60.03, certified on a grid with a Lipschitz slack). Controls: test functions exp(-((x1 - c)/w)^2)
  reach ratio 0.079 <= C_S (floating point) and refute C_S/10^4; at m = 2 the cone integral diverges; a cone of height
  (b - a)/2 + 1/4 leaves the annulus. C_S is uniform over the annuli A(tau), all of width >= 1 + delta0, as Lemma 2.1
  needs.
- *What these already say* (computed). At P*, lambda0 <= lambda_Omega <= q0/10 < 0.0540 = 0.540 l5 for every choice of
  a, against the numerics' reduced wavelength 10 l5 = 1: the construction's own standing condition excludes it by a
  factor above 18.5 (37 at a = q0/2), before any profile enters. This agrees with the paper's section 9. [Round 2,
  V-M2: round 1 called this "a certified statement about Theorem 1 itself". It is not: lambda_Omega is one term of the
  proof's own minimum, a condition the construction imposes (the paper's lines 286-288), so the bound is on the lambda0
  this proof delivers, not on the largest lam for which Theorem 1's conclusions hold.]

### 1.5 What a number needs (the exact obstruction)

Every remaining leaf (C_app, C_inf and C_dw beyond C_S, C2, C_st, C_N, C_R, C_D with C0, C_c, C_k, m_c, and m_s, C_s,
eps2) is a finite expression in sup_{Omega x S^1} |d^i g_j| for the profiles g_1, ..., g_{N+1} = g_10 and i up to about
k + 5 = 11, in a, b(tau0) and tau_end - tau0, and in the constants of Lemma 6.4 at s0 = 6, s = 8. The profiles of stage
m >= 1 solve Lemma 5.3's linear hyperbolic systems (a wave equation for the mean m_m, transports for phi_m, Psi_m and
d_th gh_(m+1)) with stage data from Lemma 6.2, whose (F2) part is itself a solve of Lemma 6.4's parabolic-hyperbolic
system on Sigma. The record computes stage 0 in closed form and the structure of stage 1 only (`lead5.py`, `stage5.py`
S1). So a number for lambda0 is a certified solve of nine stages of linear PDE on Omega with derivative bounds to order
about 11: no step is non-constructive, but it has not been done, and nothing in this session does it. eps2 also needs
g_ext, that is a concrete extension of the profiles.

## 2. The loss d

### 2.1 Numbers for the weights (computed, `dweights5.py` W1)

At the record's point (gamma_Ups = e_Ups = 1/100, z = 4 e gamma^2 = 4e-6):

| weight | value | where constrained |
|---|---|---|
| eps_ind | 1.9e-8 | <= delta_50 = 1.94137056846e-8 (READ, `eindcert5.out` I1, certified) |
| eps_+ | 1.89e-8 | < min(delta_sharp = 0.0099, eps_ind, eps_I, l_I - 3) |
| eps_K | 1.88e-8 | < eps_+; (G) below (section 2.2) |
| eps = eps' | 1e-12 | eta_2 := eps_+ - 3 eps > eps_K; eps < eps_ind |
| eta_1, eta_2 | 1.88485e-8, 1.8897e-8 | in (eps_K, eps_+) |
| l_I = a_I | 13/4 | 3 + eps_+ < l_I <= a_I < l_I + 1/2, off 3/2 + sigma_Ups and Re pi_1 E^C_I |
| l_0 | 7/2 | VII (0.1): l_I in (3, l_0), l_0 in (3, 4) |
| alpha, alpha_1, beta-step | 4 + eps_K, 2 + eps_K/2, 0.999 eps_K | I15:305, 323-324 |

Seventeen inequalities decided by computed data hold (exact). Four cannot be decided from the record: (G) over the
generators it does not list (pi_1 E_++, pi_1 G, 2 + pi_1 E_col; I11:66-68); eta_1, eta_2 off Re Lambda at W's ends
(I12:58-60); the levels off I11:156-160's finite exclusion sets; eps, eps' off the finite sets of I9:290-291 and
I14:124-126. Each needs Lambda, or the roots -mu of L_b(0)-hat, as numbers. Control N1: eps_+ = eps_ind is rejected.

### 2.2 (G) through E^C_I (computed, certified, W2)

d1 = lambda_s1,2 - 2 is taken in a certified rational interval of width 3e-57 (and is irrational, z^2 + 4z + 16 not being
a rational square). With the increments d1 and 1, the chains of {lambda_sharp, 2, 3} come nearest to (2, 2 + eps_K] u (3,
3 + eps_K] at 3 + 5.0191e-8, from lambda_sharp + 4,470,304 d1: LOSS-D LD9 G7's value, reproduced. The least E^C_I of
III.C Definition 3.1, which every admissible E^C_I contains (Definition 3.1 (3) forces 2 + s + s'), adds 23 chains [Round
2, V-M1: round 1 said 24; lambda_sharp + 1 = 2.5099 is already a chain start] (26 points below 3, of which 2, 3 and
2.5099 start chains already); none comes nearer, their residues sitting near d1/2 and 3 d1/4 because 1/d1 =
3,000,002.5... So E^C_I, one of the four generators LD9 left unlisted, does not make (G) bind, and eps_ind stays the
binding cap on eps_K at the record's point.

### 2.3 The loop counts and an exact floor (computed, W3)

The beta-chain has K = 106,489,469 steps, K + 1 = 106,489,470 levels counting the top (53,244,734 below 3, 53,244,736
above, the top included) [Round 2, V-n1: round 1 wrote "K levels"; the two parts sum to K + 1]. Summed exactly by a
floor-sum (control: equal to the level-by-level sum on a scaled instance, W3c; the sum without its +1 per level differs,
N2):

- tf rounds of III.I'''''''' Step 3.4' at the levels below 3, #{i : tau_0 + i(eps_ind - eps) <= beta - eps'}, tau_0 =
  2 + eps_ind - 2 eps (I9:281-301): R2 = 1,401,250,931,461,121;
- level-3 rounds of III.I''''''''''''' at the levels above 3, #{i : tau_3 + i(eps_ind - eps) <= beta - 2}, tau_3 = 1 +
  eta_2 - 2 eps (I14:121-128): R3 = 1,401,251,031,977,897.

Each round is charged 3 in III.J''s accounting (LD16, `thetain5.py` T4, READ), so at these weights **d >= 3 (R2 + R3) =
8,407,505,890,317,054** and N = 21 d + 6 >= 1.7656e17 (computed). LOSS-D's 7.959e15 is the same estimate in a form
[Round 4, m1: N >= 1.765576e17, rounded down; `dweights5.py` W3 now prints it so.]
valid at every admissible weight (eps_K, eps_ind taken up to delta_50); this is its exact value at one admissible point
[Round 3, m1: at a point meeting every decidable condition; four admissibility conditions are undecided (2.1), and round
2 settled (G) only].

### 2.4 The log terms of the general class (computed, W5; deduced from the cited lines)

LD16 left open whether E^C_I has logarithms below l_I (loss 6 without them). The data's E^C_I is fixed by III.C'
(3.1)'s construction (PART-III-C2-POLYHOM.md:247-259): E^(0) the least set of III.C Definition 3.1 containing E_0, then
rounds E' := the least such set containing E_0 bar-cup E^C_I, the extended union adding log orders plus one where the
two sets share an exponent (PART-III-A-PREREQ.md:467). The assembly takes E_0 = {(j, 0) : j >= 2}
(PART-VII-ASSEMBLY.md:45), and (2, 0), (3, 0) lie in every E^C_I (III.C Lemma 3.2 (a)): they meet at 2 and 3, and
logarithms appear below l_I = 13/4. With `prop31loss5.py`'s own least_ECI and chain:

| reading | logs below l_I | (J, log steps, applications) | loss of the one-off application |
|---|---|---|---|
| E_0 empty (control; prop31loss5 Q2) | none | (2, 0, 3) | 6 |
| one corner union (R0) | 14 exponents, log order up to 2 (at 3) | (2, 3, 6) | 12 |
| III.C' (3.1) as written, M = 4 rounds (eta = 9/20) | | (2, 12, 15) | 30 |
| as written, M = 7 (the bound 4(l_I - l_flat_I) + 1) | | (2, 21, 24) | 48 |

R1 compounds because each round re-takes the extended union with the whole previous set; R0 is what one corner
produces. The record states R1. Control N3: without the +1 of the extended union no logarithm appears. The one-off
application is once per call of III.I''''' (I6:103-108), so even 48 adds only 3.1e9 over the chain (W8).

### 2.5 One regularity step beyond its floor (deduced; computed, W6)

Where III.I''''' Step 4 applies III.I' Proposition 2.1 (I6:214-218), u = u_I + u_iota + u_flat has a priori I+-weight
min(3/2, alpha_+^sharp) - 3 eps (u_flat, I6:205-208), above l_+ := min(3/2, alpha_+^sharp) - 4 eps: Step 1 (I2:136-152)
takes no step. Step 2 (I2:154-161) integrates forward as in Lemma 2.2: its Step 2 (I2:95-104) is one step, to 3/2 +
eta' with eta' < (1 - e_Ups) gamma_Ups = 0.0099 (it needs the weight only above 1 + eta'), and its Step 3 (I2:111-134)
needs ceil((l_I - 1.5099)/(1/2)) = 4 steps of length below 1/2. So **5 steps, each one application of L~ (loss 2):
loss 10**, against D582's floor of 4 steps (8). At l_I = 3.6 it would be 6 (control N4).

### 2.6 The recursion, and why it gives no certified number (W4, W7, W8)

The elementary losses at these weights (W7): d_G = 11 on the iota+ window, III.G''' Lemma 2.2's l = 2 ceil(l_I) + 10 =
18, Proposition 2.4's l' = 30, an iota+ round 4 + d_G = 15, a tf, level-3 or level-2 round 3. The per-level ceilings
(W4, certified with the d1 interval): the iota+ loop at most ceil((2 - eps - lambda_sharp)/d1) = 1,470,302 rounds per
level below 3 (LD14, reproduced); N_* = ceil(5/d1) + 2 = 15,000,015; the level-2 container |Lambda' cap W| per level
above 3 is 7,470,307 for the named generators (LD15, reproduced) plus 44,555,454 from E^C_I's 23 chains, **52,025,761,
1.98 times a level's mean level-3 rounds** (2.6317e7) [Round 2, V-M1: round 1 printed 46,025,756 from 24 chains,
53,496,063 and 2.03, counting the chain of lambda_sharp + 1 twice; `dweights5.py` now checks the count on the
deduplicated union of the chain starts, control N5]: LD15's route (the container shorter than the level-3 loop when
the unlisted generators add at most six chains) is closed in the negative by E^C_I alone.

The composition (1.1) over the levels, on these hypotheses:

- H1: at each level above 3 the level-2 loop makes one application per exponent of Lambda cap W (LD16's
  redundancy-free reading), and E_++, G, E_col add no point to W;
- H2: the iota+ loop at its ceiling at each level below 3, 15 per round (the construction's reading, m_iota = d1);
- H3: at each call of III.I''''' one round raising alpha'_K, Proposition 2.1's 10 and the one-off application's 48;
- H4: III.J''s charges, and every other step of a level lumped into one unknown c,

gives **d <= 17,892,090,290,788,934 + 106,489,470 c** [V-M1: was 18,126,947,816,279,750] (computed, W8: rounds 8.408e15,
level-2 container 8.310e15 [was 8.545e15],
iota+ 1.174e15, the rest 3.1e9). This is conditional. [Round 3: c is not a small per-level constant. Among the steps it
lumps, III.A Proposition 4.2 (1) at III.I''''''''''' Proposition 3.1's Step 0, repeated at every level above 3, loses
1 + n_iota + 10, n_iota the number of (exponent, log order) pairs of E^flat below the weight, which the record bounds
only by sum over Lambda of (K(lambda) + 1) >= 5.6e22 per level (`dceiling5.py` D5-D6).] The exact obstructions to a
certified upper bound:

1. Lambda's generators pi_1 E_++ (the least choice of III.I'''''''' (1.1)), G and 2 + pi_1 E_col are not computed at
   n = 4; without them neither |Lambda cap W| (H1) nor (G) nor the admissibility of the levels is decided.
2. Steps whose count or charge is not given in the record or not read here: the forward map's loss (III.I Theorem
   5.3, (5.2)), the windows of
   III.I'''''''''' (at most N_* = 15,000,015 per call, the charge per window not read), the "pairs removed, finitely
   many" of III.I'''''''''''', the exponents of Lambda_* in III.J', and III.I Remark 5.5's rewritings.
3. Three readings the record leaves open and the count depends on: l_I <= a_I or a_I = l_I (both used here, equal);
   III.C' (3.1) as written (R1) or one corner union (R0); one application per exponent or per (alpha_0, k) (LD15: the
   latter gives at least 5.83e20 rounds at a single level).

## 3. lambda1 and delta (Theorem 4)

### 3.1 The non-effective steps, row by row (computed, `nrows5.py` R1)

The 35 N-rows of EFFECTIVE-LEDGER.tsv (6 N1, 15 N2, 1 N3, 13 N4) each carry the obstructions of its replacement:

- COVER (13 rows, every N4): a finite cover; explicit radii need the local estimates' constants written out.
- NORM (9): from per-harmonic L^2 bounds of E2-PILOT's kind to the record's variable-order b-Sobolev norms; this needs
  the elliptic and propagation constants of I.A-I.B, which are COVER rows.
- TENSOR (14): a system on 1-forms or symmetric 2-tensors (box^Ups, L_b, L~_b, N_tf, N_iota+); mode-by-mode
  certification needs the tensor-harmonic decomposition on S^3. E2-PILOT certifies the scalar wave only.
- LOWE (8): an inverse bound at zero energy in b-spaces (I.C, III.D'', III.F''').
- TRAP (4): the trapping estimate; E2-PILOT sections 3e-3j have the scalar one in a cut-off norm, not the record's.
- SIGMA (12): a Neumann series in the spectral parameter about a certified base; E2-PILOT does this in its own norm.
- BFAM (9): uniformity over b near b0; rotating Myers-Perry operators do not separate, so a Neumann series needs a base
  certified in the record's norm and an explicit Lipschitz bound in b in that norm.

Every N1 row needs at least one of NORM, TENSOR, LOWE, TRAP (R3), so **no N1 base bound can be certified in the
record's norms before the COVER constants and the norm passage are explicit**: the order is COVER < NORM < TENSOR <
LOWE < TRAP < SIGMA < BFAM. This is a statement of dependence, not of impossibility: no row has been shown to lack an
effective version, and EFFECTIVE-CONSTANTS.md section 4's methods (READ) apply to each.

### 3.2 A kind the ledger did not search (computed, R2)

The ledger's census searched contradiction, compactness, Rellich, Fredholm and subsequence. Bounds from Baire-category
theorems give a constant without a value too: proof5 has 16 lines with the closed graph, open mapping or
Banach-Steinhaus theorem, none among the ledger's N-rows; 13 carry a constant [Round 2, V-m2: corrected to 18 lines and
10 B rows in `nrows5.py`; II.A:986, 1538 and II.A2:811 are summaries, I4:274 offers a constructive bound beside the
theorem, II.A2:186 and J4:655 were missed; R2.4 (b)]: II.A:960, 986, 1538; II.A2:130, 188,
276, 281, 811 (the calculus); II.F:1400 (open mapping, beside the N1 row 1393); III.H:425 (Banach-Steinhaus, locally
uniform in sigma); III.I''':274; and III.J'':41, 82, where the closed graph theorem gives the tame constants C_k of
every membership statement (Lemma 1.2 (f)). These enter lambda1 and delta through the tame constants. Their
replacement is to read each bound off the proof of the membership statement it concerns, which is a chain of explicit
estimates; that is not done. [Round 2, V-m1: round 1 added "(The losses, and so d, are not affected: a membership
statement fixes its loss by its orders.)". That is too strong: closed-graph steps also hide orders and losses -- "for
some d0" (II.A-SETUP:960), "a seminorm" (II.A2:188), the weight loss eps'(eps, k) (J3:41) -- so d is unaffected only
where the membership statement's orders are themselves fixed by explicit estimates; see Round 2, R2.4 (b).]

### 3.3 How small the proof's own formulas make them (computed, certified, `deltacap5.py`)

EFFECTIVE-CONSTANTS.md Proposition 2.1 has theta0 >= 16, so eps_NM <= 16^-(8d+2); Proposition 2.2 gives delta = eps/2
<= eps_NM/(2 A_2d) and C_R lambda1 < eps/2. With A_2d, C_R >= 1 (upper-bound constants may be enlarged; Proposition
2.2's proof takes the tame constants so), delta <= 2^-(32 d + 9) and lambda1 < delta. With 2^196 > 10^59 (exact):

- d >= 7.959e15 (LOSS-D LD16, every admissible weight): **log10 delta < -7.6666e16**, and the same for lambda1;
- d >= 8,407,505,890,317,054 (section 2.3): log10 delta < -8.0987e16.

These bound what the proof can deliver from above. Controls: the claim delta >= 10^(-7 x 10^16) is refuted; at d = 1
the same formula allows 10^-12.3; without A_2d >= 1 the program prints no number.

## 4. Proved, computed, open

- *Deduced* (with programs): lambda0's constructivity and formula (1.2-1.3); C_J, lambda_1.1 constructive (1.2); the
  data's E^C_I carries logarithms below l_I (2.4); Proposition 2.1's count 5 at I6:216 (2.5); the order of the
  replacements (3.1); the Baire-category kind (3.2); delta, lambda1 < 10^(-7.66e16) given A_2d, C_R >= 1 (3.3).
- *Computed, exact or certified*: the leaves of 1.4; the weights and their 17 inequalities (2.1); (G) unmoved by E^C_I
  (2.2); K, R2, R3 and d >= 8,407,505,890,317,054 (2.3); the losses 12/30/48 (2.4); the container 52,025,761 (2.6)
  [V-M1: was 53,496,063].
- *Conditional, not proved*: d <= 1.7892e16 + 1.0649e8 c on H1-H4 (2.6) [V-M1: was 1.8127e16].
- *Open, with the exact obstruction*: lambda0's number (the profiles g_1..g_10 to order about 11, section 1.5); a
  certified upper bound for d (Lambda's generators E_++, G, E_col; five uncounted steps; three readings, section 2.6);
  every N-row and B-row constant (section 3.1-3.2).

## 5. Next steps

- lambda0: certified bounds for stage 1 at P* with a smooth envelope (m1, phi1 and gh_2 solve linear transports and one
  wave equation in the symmetric class), which give C_app and the first part of C2.
- d: E_++ at n = 4 (III.I'''''''' (1.1)'s least choice), the generator closest to deciding H1 and (G).
- lambda1, delta: the COVER constants of I.A section 7 and II.D section 6, first in the order of 3.1.

## 6. Sources

N1STAR-PROOF.md sections 0-6 (lines 1-805); the paper's sections 3, 5 and 9 (RESPONSE-HL-5D.md:258-357, 495-641,
1371-1427); EFFECTIVE-CONSTANTS.md sections 2-4; EFFECTIVE-LEDGER.tsv; LOSS-D.md sections 2-5 (LD9-LD16); E2-PILOT.md
section 4; proof5: PART-III-J3-TAME.md:41, 62-86, 247-293; PART-III-I2-SCRI.md:57-238; PART-III-I6-ALMOSTBDD.md:26-51,
96-110, 196-227; PART-III-I9-COMMOTION.md:276-302; PART-III-I14-LEVELS.md:118-130; PART-III-I15-AUGMENT5.md:305-330;
PART-III-I11-SPACETIME.md:63-80, 148-160; PART-III-C-EXTERIOR.md:144-200; PART-III-C2-POLYHOM.md:196-259;
PART-III-C3-BOOSTDATA.md:156-158, 227-229; PART-VII-ASSEMBLY.md:40-67, 102-138; PART-I-C-LOWENERGY.md:495-498; the
Baire sites of 3.2. Checks reused: `prop31loss5.py` (imported), `eindcert5.out` (READ), `thetain5.py` T4 (READ).

## Round 2

*Status (2026-11-02).* Appended to round 1; not yet read by a verifier. Round 1's text above is kept; where this round
found it wrong, the line carries a bracketed `[Round 2, V-...]` note with the old figure, and R2.1 says what was wrong.
New programs (each with its `.out`, every control failing as it must): `checks/envelope5.py`, `checks/eps1hyp5.py`,
`checks/stage0bd5.py`, `checks/gronwall5.py`, `checks/lambdagen5.py`, `checks/cover5.py`, `checks/baire5.py`. Round 1's
programs changed and rerun: `dweights5.py`, `nrows5.py`, `deltacap5.py`, `lzeroconst5.py`, `lzeroaudit5.py`.

### R2.0 Summary

- **(i) lambda0.** A C_c^inf envelope with int env^2 = 105/128 exactly (so round 1's leaves stand) and certified bounds
  on its derivatives to order 14 (computed). **eps1 can be any number below 3/5, and no eps1 above 0.60132 serves**
  (computed, exact; round 1's 5.2617e-4 is valid but 1140 times smaller) [Round 3, M1: 0.6013096 at the outer
  boundary's corner r = b(tau0), and both figures in the Euclidean operator norm, which N1STAR-PROOF.md lines 1-805
  never define for arrays; eps1 = 3/5 itself serves, by a direct cone argument: `eps1hyp5.py` H2-H3, `lzerotrace5.py`
  T2, T6]. Certified bounds to order 14 on every
[Round 4, A: eps1 = 3/5 serves Lemma 1.1 (e) only; Lemma 2.3 takes the same eps1 and needs it below g0's least
absolute eigenvalue on Omega, in [0.030768559, 0.030768560] (certified, `lzerotrace5.py` T7), so lambda0 < 0.0024433.]
  derivative of the explicit profiles: the wave W_TT, the second harmonic chi dv dv, and the stage-1 mean source S
  (computed). Every admissible C_app is at least 12.58, so **the lambda0 this proof delivers is at most 0.0239** at P*
  with this envelope (computed), below lambda_Omega [Round 3, M1: 0.0239 holds only at round 1's even split of eps1
  between g_app and w, a choice the proof does not make (N1STAR-PROOF.md:355-357 asks only |g_app - g0| + |w| <=
  eps1); for any split the term is < eps1*/C_app <= 0.0478, above lambda_Omega, so split-free the bound is
  lambda_Omega = 0.026986 itself (operator norm; largest-entry norm: 0.00955); "below lambda_Omega" is withdrawn;
  `lzerotrace5.py` T5]. Lemma 2.4's factor for Step 6's transport is e^11.0006 = 5.99e4 (computed) [Round 3, M2: was
  e^44.0 = 1.29e19, which took C = sup|c| and dropped the -int (3/r) phi^2 term of the lemma's own identity], and as
  Steps 6-7 are written it enters C2 and then a second exponential, so the literal C3 is doubly exponential, ln C3 >=
  3.56e5 [was 7.65e19] (a deduced reading: the proof's C is any valid constant, so C2 >= e^11 is not forced;
  `gronwall5.py`, corrected). **Stage 1 itself (m_1, phi_1, gh_2) is not
  bounded**: the exact cost is in R2.2.
- **(ii) d.** E_++ and G add no chain to Lambda (deduced; computed check). E_col's candidate bases, under the widest
  reading, are 11 (computed): they do not make (G) bind, though the nearest comes within 2.2 % of delta_50 (certified),
  and they lengthen the level-2 container to 85,025,783 per level. The windows of III.I'''''''''' Proposition 3.1 run
  at the levels above 3 too, and Lambda_* and the "pairs removed" cost no derivative (deduced). The conditional bound
  becomes **d <= 2.4338e16 + 1.0649e8 c** on widened H1-H4. **No proved upper bound**: it is blocked first by Lambda's
  increments, pi_1 E^iota_ind and the full root list of E_ind, which the record never lists (R2.3).
- **(iii) lambda1, delta.** The covering counts of I.A section 7 and II.D:1032 are explicit on the model, and two of the
  three coverings are not needed (an exact escape function and an exact time function) (computed) [Round 3, m4:
  computed exactly on the Tangherlini model at b0 only; that two coverings are not needed is a deduction at b0, which
  does not reach b != b0]. The 18 closed-graph-type sites [Round 3, nit: of which the 11 of classes B and A are
  classified here]: 1 effective as written, 6 by a calculus estimate, 2 by reading chained proofs, 1 given a base
  inverse bound (explicit Neumann series), 1 of the N1 kind (computed classification, deduced replacements) [Round 3,
  m4: a hand-written classification, `baire5.py`:44-70, whose coverage the program checks; since Round 3 K3 computes
  its constants, and `nkind5.py` K1 shows the N1 kind's non-determination]. No
  number for lambda1 or delta.

### R2.1 The verifier's findings on round 1 (commit 72850e1), folded in

- **V-M1 (major), `dweights5.py`:336.** Wrong: the E^C_I chains were taken as the least E^C_I minus {lambda_sharp, 2, 3},
  but lambda_sharp + 1 = 2.5099 is both a chain start (a named generator plus 1) and a point of the least E^C_I, so its
  1,470,302 points per level were counted twice. Corrected (computed, `dweights5.py` W4, control N5 on the deduplicated
  union of the 27 chain starts): **52,025,761 points per level, 1.98 times** the level-3 rounds (not 53,496,063 and
  2.03), from **23** further chains (not 24), and **W8: d <= 17,892,090,290,788,934 + 106,489,470 c** (not
  18,126,947,816,279,750). The verifier's figures, reproduced. The conclusion that the container is longer than the
  level-3 loop survives. The round-1 lines the verifier names (24-25, 160, 214-216, 226, 291 at 72850e1) carry the
  correction.
- **V-M2 (major), round 1 lines 16-17 and 115-118.** Wrong: "a certified statement about Theorem 1 itself".
  lambda0 <= lambda_Omega holds because lambda_Omega is one term of the proof's own minimum, a condition the
  construction imposes (RESPONSE-HL-5D.md:286-288, READ: "a condition the construction imposes, not a bound below
  which the theorem holds: that is lambda0"). It bounds the lambda0 this proof delivers, not the largest lam for which
  Theorem 1's conclusions hold. Every bound on lambda0 in this file, R2.2's included, is of the first kind.
- **V-m1, round 1 lines 270-271.** Wrong: "(The losses, and so d, are not affected ...)". Closed-graph steps also hide
  orders and losses -- "for some d0" (II.A-SETUP:960), "C times a seminorm" (II.A2:188), the weight loss eps'(eps, k)
  (J3:41) -- so d is unaffected only where those orders are fixed by explicit estimates (R2.4, `baire5.py` K4).
- **V-m2, `nrows5.py`:58.** Wrong: the pattern missed "closed-graph" (J4-EXACT:655) and, found here, "Banach and
  Steinhaus" (II.A2:186); C2 injected a hit and never tested the pattern; class B held three summaries (II.A:986,
  1538; II.A2:811) and I4:274, which prints a constructive bound beside the theorem. Now: **18 sites, 10 B, 1 A, 6 R,
  1 Q**; C2 tests the pattern on five phrasings, of which round 1's misses three.
- **V-m3, `deltacap5.py`:35-36.** Wrong: the assertion 2^196 > 10^59 was not tied to the ratio returned, so an unsound
  31/100 passed, and C1, C3 could not fail on their own. Now the soundness test is on the ratio itself; C1 refuses
  31/100; C3 shows the printed bound moves by log10 2 without the convention A_2d >= 1. The numbers are unchanged
  (log10 delta < -7.6666e16).
- **V-m4, `lzeroconst5.py`.** Z4 checks the closed form against its own transcription of the conditions, not against
  the proof: true, and inherent (the transcription is the deduction of round 1's 1.3); the docstring now says so.
  Proposition 6.5's ball invariance (N1STAR-PROOF.md:771-772) had no term: Lemma 6.4 keeps the iterates in the ball
  of radius 2 C0 lam^(N-2) when C0 lam^(N-2) + C_b (2 C0 lam^(N-2))^2 lam^-1 <= 2 C0 lam^(N-2), i.e. a **ninth term
  (4 C_b C0)^(-1/(N-3))**, C_b the constant of the quadratic remainder (deduced; now in `lzeroconst5.py` Z4/Z5 and
  `lzeroaudit5.py` A2).
- **V-m5, `lzeroconst5.py`:236-245.** Wrong: Z2's control perturbed g0 at r = a, where d(v + tau) need not be timelike,
  and its size 27.2 accepted any eps1 below 27. Replaced by the sharp control on the outer boundary (norm 0.60132,
  `eps1hyp5.py` H3).
- **Nits.** Line 166: the two parts sum to K + 1 = 106,489,470, not K (corrected in place). `lzeroconst5.py`:177 said
  "seven terms" of eight (now nine, V-m4). `lzeroaudit5.py` now pins the md5 (A0, 57d896ae...). Line 17's "stages 1-10"
  meant the profiles g_1..g_10, which come from stage 0 and the nine solves of stages 1-9 (corrected in place). The
  paper prints d > 7.95e15 (RESPONSE-HL-5D.md:1390, 1758, READ; [Round 3, nit: now 1403, 1782]); 7.959e15 is LOSS-D's
  sharper form of the same floor,
  which round 1 quotes under LOSS-D's name (`deltacap5.py`, 3.3); both stand.
- **Found here.** Round 1's eps1 is valid but not the right measure (R2.2 (b)); round 1's 1.5 "a nine-stage linear PDE
  solve" stands, with the cost now made specific (R2.2 (f)).

### R2.2 (i) lambda0

(a) *The envelope* (computed, `envelope5.py` E1-E3). env(v) = c cos^12(pi y/2) exp(-y^2/(1 - y^2)), y = (2v - 4)/3, on
[1/2, 7/2]; c in [1.3240711, 1.3241035] makes int env^2 = 105/128 exactly, so mu_end = 227/192 and every leaf of 1.4
stands [Round 3, m5: tau_end also needs v - r_q(v) increasing, which round 1 checked with sup env = 1; with this
envelope's peak c <= 1.3241035, 1 - q0 (2/9) c^2/4 >= 0.947 > 0, now checked in `lzeroconst5.py` Z1]. Certified e_k =
sup|env^(k)|, k = 0..14: 1.324, 3.077, 18.6, 95.75, 739.5, 5166, 4.611e4, 3.841e5, 3.780e6, 3.539e7, 3.733e8, 3.796e9,
4.214e10, 4.552e11, 5.248e12 (interval Taylor arithmetic in a centred form; the end intervals by the exact derivatives of
exp(-1/(2t))). Within a factor 2 of sampled values at every order (control C2). The plain bump exp(1 - 1/(1 - y^2)) gives
e_11 about 3.6e22: the cos^12 factor buys twelve orders of magnitude [Round 3, nit: no program printed 3.6e22;
`envelope5.py` P0 now computes e_11 ~ 3.29e18 (floating point), so the factor buys about nine orders of magnitude].

(b) *eps1* (computed, exact, `eps1hyp5.py` H1-H3; deduced H2). Lemma 1.1 (e)'s conditions are that Sigma_tau, {r = a}
and the outer boundary stay spacelike, i.e. that g restricted to ker dtau, ker dr, ker d(v + tau) stays positive
definite. On those hyperplanes, in Euclidean-orthonormal bases, g0 has least eigenvalues 1, min(1, mu/a^2 - 1) = 1 and
(3 + mu/r^2)/5 >= 3/5. So **every eps1 < 3/5 serves** (the time orientation and the causal containment follow along
g0 + t(g - g0)) [Round 3, m3: that path argument assumed the intermediate metrics Lorentzian; replaced by the direct
cone argument, `eps1hyp5.py` H2: |g - g0| <= 3/5 gives g >= g0 - (3/5) I, which is positive definite on ker dtau, ker
dr at r = a and ker d(v + tau) (least eigenvalues 2/5, 2/5, mu/(5 r^2)) and has exactly one negative eigenvalue, so
eps1 = 3/5 itself serves], and the perturbation -lambda n n^T at r = 67/5 on the outer boundary (norm 0.6013169, exact)
makes it null: **eps1* in [3/5, 0.60132]** [Round 3, M1: 0.6013096 at the corner r = b(tau0); operator norm]. Round 1
[Round 4, A: that is Lemma 1.1 (e)'s eps1*; Lemma 2.3 needs eps1 < 0.0307686 (R4.2).]
went through |g^-1 - g0^-1| <= n^2 eps with n = 33.47, which cost the factor 1140. In lambda0's formula, eps1 enters E-a
and E-b; Lemma 2.3's constants degrade as eps1 approaches 3/5, so the choice is a trade-off the formula does not yet
resolve.

(c) *Stage 0 and the stage-1 source* (computed, `stage0bd5.py` X1-X4). The Cartesian forms of W_TT, chi dv dv and S,
each smooth across both axes, are new here (deduced; equal to the EF pullbacks at 400 points to 1.5e-15; chi's f
recomputed from `lead5.py`). With D[n] := sup over Omega x S^1 and unit directions of the n-th directional derivative
in Frobenius norm (which bounds every component of every n-th derivative, by Banach's theorem), certified:

| n | 0 | 1 | 3 | 6 | 9 | 11 | 14 |
|---|---|---|---|---|---|---|---|
| W_TT | 154 | 6.18e3 | 1.88e7 | 1.67e13 | 6.91e19 | 3.21e24 | 6.28e31 |
| chi dv dv | 44.0 | 2.75e3 | 1.71e7 | 2.72e13 | 1.47e20 | 7.66e24 | 1.71e32 |
| S (stage-1 mean source) | 3.32e3 | 1.94e5 | 1.10e9 | 1.66e15 | 8.90e21 | 4.64e26 | 1.04e34 |

These bounds are certified but not sharp: the majorant calculus (Leibniz and Faa di Bruno along lines, homogeneity in
r, the worst radius r = a = 0.2699) loses about a factor 12 at order 0 (|W_TT|_op reaches 12.58, X4) and, at order 11,
up to about 1e5 in the composition for H = (2/(1 + cos^2 2th))^(1/2), whose complex singularities lie at imaginary
distance 0.44 in th. A first attempt with Cauchy estimates on complex polydiscs failed: rectangle arithmetic could not
certify H's branch beyond radius 0.04 r. *A bound the other way* (computed, X4): at v = 2, r = 0.27, |W_TT|_op >=
12.5836; since g_1 = m_1 + W(X, th + phi_1) and W_TT changes sign under th -> th + pi while m_1 and chi do not, every
admissible C_app is at least 12.58, and **lambda0 <= eps1/(2 C_app) <= 0.60132/25.17 < 0.0239** for every admissible
eps1 (the lambda0 of this proof, V-M2; with this envelope) [Round 3, M1: at round 1's even split only; for any split
lambda0 < eps1/C_app <= 0.6013096/12.5836 = 0.04779, above lambda_Omega; operator norm. At r = a itself (in Omega)
|W_TT|_op >= 12.5933, giving 0.023874 and 0.047748: `lzerotrace5.py` T3, T5].

(d) *A stage-independent constant* (computed, `gronwall5.py` G1-G3). Lemma 2.4 gives C = sup|c|; for Step 6's
transport c = 2/r <= 2/a, so its factor is **exp((2/a)(tau_end - tau0)) = 1.288e19 = e^44.00**. Along L0 the equation's
own growth is (r(tau0)/r)^2 <= (b(tau0)/a)^2 = 2479, so the exponential is the proof's, 5e15 above the equation's
(computed). [Round 3, M2: wrong. The lemma's own identity (N1STAR-PROOF.md:233-235) keeps -int (3/r) phi^2, and with
c = 2/r, 2c - 3/r = 1/r <= 1/a: the rate of ||Psi|| is 1/(2a) and the factor exp((tau_end - tau0)/(2a)) = e^11.0006 =
5.99e4; the equation's own growth is ((a + dtau)/a)^2 = 529 (round 2's 2479 is a looser bound), so the excess is
about 113, not 5e15; `gronwall5.py` G0-G2, corrected, with controls that mutate the code path.] *A finding about
Steps 6-7* (deduced from N1STAR-PROOF.md:382-401, the reading to be checked): Step 6
writes the Psi-part as "at most C (N(tau0) + int (N + ...))", a C that carries Lemma 2.4's factor, so C2 >= e^44 as
written; Step 7 then applies Gronwall again, C3 containing exp(C2 (tau_end - tau0)): **the literal constants are
doubly exponential, ln C3 >= 7.65e19**. One Gronwall on the summed differential inequalities (rate >= 2/a) gives ln C3
about 48 instead. Neither is a bound on lambda0 without lower bounds on C_N and C_st (taking them >= 1, ln lambda0 <=
-2.29e20 literally, <= -143.8 after the rewrite: estimates, not bounds). [Round 3, M2: with the identity's rate, C2 >=
e^11.0006 on this reading, ln C3 >= 3.56e5 literally and about 13.6 after one Gronwall; ln lambda0 <= -1.07e6 and
-40.7 on the same assumption. This is a deduced reading, not a forced bound: the proof's C is any valid constant, so
C2 >= e^11 is not implied by the proof.]

(e) *Stage 1, as far as it went.* Its explicit inputs are now bounded: the coefficients built from W and chi, and the
mean source S (`checks/stage5.py` S2's source, a dv dth component only). Not bounded: the oscillating part of R^(1)[g0 +
lam W] (nonzero in seven components, `stage5.out` S4), the linear operator's coefficients B-bar, C-bar, Mm, Wm (structure
in `stage5.py` S1, coefficients not extracted), the data (h_1, Q_1) of Lemma 6.2, which solve Lemma 6.4's radial
parabolic-hyperbolic system with an unwritten constant, and the solution.

(f) *The exact cost of the nine stages* (deduced from Lemmas 5.1-5.3, 6.2, 6.4 and the record's timings; not computed).
Per stage m = 1..9, in the T^2 x Z2 x Z2 class: m_m (8 components) by a wave system, phi_m and Psi_m by transports, and
Z = d_th gh_(m+1) (8 components per harmonic) by a transport, all functions of (tau, r, th); the data by Lemma 6.4 on
[a, b(tau0)] x S^3 reduced to (r, th). A certified bound needs, per stage: (1) the coefficients of R^(m) symbolically
(`stage5.py` needed 966 s for lam^1 with generic profiles and could not reach lam^2; R^(1)..R^(9) are needed); (2)
explicit energy constants for the coupled system (Lemma 2.3 at g0 with its deformation tensor bounded on Omega, and
Lemma 2.4, now explicit), commuted to the order required; (3) Lemma 6.4's constant written out; (4) the order: each
stage's source carries up to two derivatives of earlier profiles and its transports gain none, so for g_10 to order
14 (11, plus 3 for Sobolev) stage 1 is needed to order between about 22 and 30. With constants of the size above (e^44
per transport, 1e24-1e26 for the order-11 profile bounds at stage 0), (d) already places the number far below 1:
ln lambda0 <= -143.8 after a one-Gronwall rewrite of Step 7, -2.29e20 as written, if C_N, C_st >= 1 (not shown, so
an estimate) [Round 3, M2: e^11 per transport; -40.7 and -1.07e6].

### R2.3 (ii) d

(a) *E_++ and G* (deduced from I9:37-46, I11:127-134, I2:177-190, I8:37-41; computed check, `lambdagen5.py` L1-L2).
Below 2 lambda_sharp = 3.0198 the least E_++ is the least index set containing E^sharp_+ cap {Re < 2} closed under
+ (E^iota_ind u E_ind), and E^sharp_+ = {lambda_sharp} u pi_1 E^C_I (III.I' (3.2) with breve E_+ empty); the least
E^C_I has no point below 2. So pi_1 E_++ below 3.0198 is the chain of lambda_sharp, and pi_1 G = {2} u (2 + pi_1 E_ind)
the chain of 2: **neither adds a chain**. Round 1's obstruction 1 reduces to Lambda's increments and to E_col.

(b) *E_col* (deduced from I12:79-110; computed, certified, L3-L5). Its exponents are those of F = sum phi(s) s^m
r^(4-k+m) (Q w_m)(x), shifts sigma = q - 4 + k - m >= -5 of the classes (2, 0) u (2 + E_ind), (3, 0) u (3 + E_ind)
and the tower's (contained in E_ind). With the record's computed roots (d1 = delta_1, 1 + d0, the sl roots (l - 1) +
delta_l and l + delta'_l), the bases 2 + pi_1 E_col that are not chains of 2 or 3 are, on the widest reading (the
tower's exponents unshifted), **11**: 2 + d0, 2 + delta'_l (l = 1..5), 2 + delta_l (l = 2..6) (7 if the tower is read
as 2 + E_ind). Whether their coefficients vanish the record does not decide; an upper bound must admit them.

- *(G)* (certified, L4): their chains with d1 and 1 come nearest above 3 at **3 + 1.9841e-8**, from 2 + delta_3 +
  3,000,002 d1; delta_50 = 1.9414e-8 bounds eps_ind, so **(G) does not bind**, by a margin of 2.2 %. Round 1's
  generators give 5.0191e-8.
- *The container* (certified, L5): each adds about 3.0e6 points per level: **85,025,783 per level** above 3, and 3 per
  point over 53,244,736 levels adds 5.2712e15.

(c) *Round 1's uncounted steps* (deduced; READ I11:347-386, J2:95-145, I13:234-266).
- The windows of III.I'''''''''' Proposition 3.1 (b) (I11:369-386) belong to the construction at every level alpha <=
  4 + eps_K ("the new point is alpha <= 4 + eps_K", I11:347), at most 1,470,302 per call (width >= eta_0 = d1 below
  2), each one iota+ round (15). Round 1's H2 charged them below 3 only; above 3 they add **1.1743e15** (computed, L6).
- Lambda_* in III.J' (J2 Step 2) is an induction inside the proof that D_U Phi is injective: no map is built, **no
  derivative is charged**.
- The "pairs removed, finitely many" of III.I'''''''''''' Lemma 2.4 are subtractions of explicit tensors chi_K
  T_rho(a Y) with coefficients read off the expansion, linear and bounded at fixed index sets: **no derivative is
  charged**; the number of pairs enters C_k only.
- Not read: the forward map's loss (III.I Theorem 5.3, (5.2)) and III.I Remark 5.5's rewritings.

(d) *The bound* (computed, conditional, L8): with H1 widened to admit (b)'s bases and H2 to the windows above 3,
**d <= 24,337,610,296,395,590 + 106,489,470 c** (2.4338e16 + 1.0649e8 c), against the floor d >= 8,407,505,890,317,054.
[Round 3: c contains III.A Proposition 4.2's index-set count, bounded in the record only through K(lambda); with it
the record's own ceiling is at least 1.49e31 (R3.3).]

(e) *Why it is not proved, step by step.* (1) **Lambda's increments are not listed**: pi_1 E^iota_ind (III.G''
Theorem 4.2's index set, "depending only on L-bar and on whether lambda = 1") is never computed, and E_ind's exponents
are known only for the s0, s1 and sl roots; a certified upper bound needs every indicial root of the operators of
III.D'' Proposition 3.1, III.F''' Proposition 2.2 and III.G'' Theorem 4.2 with real part below 5 at n = 4. A further
fractional increment below 1 would multiply |Lambda cap W|. This is the first blocking step: without it |Lambda cap W|
has no upper bound, so H1 has no content. (2) The forward map's loss and Remark 5.5's rewritings (not read). (3) The
three readings of round 1 (l_I vs a_I; III.C' (3.1) as written or one union; one application per exponent or per
(alpha_0, k)). (4) c, the per-level loss of the steps no part of the record charges explicitly.

### R2.4 (iii) lambda1 and delta

(a) *COVER* (computed, exact, `cover5.py` V1-V5). On the model at b0 (five-dimensional Tangherlini, mass mu):
- I.A:1570, the sigma_0-cover: Lemma 7.1's J(sigma_*) = {|sigma_0 - sigma_*| < |sigma_*|/4} gives **N(I) = 1 +
  ceil(log(s_b/s_a)/log q)** neighbourhoods for any q < 5/3 (21 for [1/100, 100] at q = 8/5; q = 5/3 fails, C1).
- I.A:1602, region (B) at fibre infinity: G0 = f xi^2 + |eta|^2/r^2, and on the characteristic set xi' = -2 xi^2/r and
  **H r = 2 f < 0** inside the horizon: r is an exact escape function, one commutant replaces the finitely many curves;
  the time from r_h - eps to r0 - delta0 is int r^2 dr/(2(mu - r^2)) (0.2615 from 9/10 to 1/2 at mu = 1).
- I.A:1602, region (D) on the boundary face: on (xi + sigma0)^2 + |eta|^2 = sigma0^2, (4.5) gives
  **H log tan(phi/2) = -2 sigma0** exactly: an exact time function, and explicit transit times.
- II.D:1032, the trapped set: r_c = (2 mu)^(1/2), **Lyapunov exponent lambda_L^2 = 1/(2 mu)** (Schwarzschild time):
  the "bounded times" of the backward segments are log(D/delta) (2 mu)^(1/2) to first order.
- What stays non-explicit: the constant of each microlocal estimate (I.A Propositions 4.2, 4.6, 4.9, 5.1, 5.2; II.D's
  radial and trapping estimates), which comes from the calculus. The COVER rows thus reduce to these per-piece
  constants, multiplied along a chain of six pieces at each of N(I) frequency neighbourhoods.

(b) *The 18 closed-graph-type sites* (computed classification, deduced replacements, `baire5.py` K1-K4) [Round 3, m4:
a hand-written classification (`baire5.py`:44-70) whose coverage is checked; K3's constants are computed since Round
3].
- Effective as written: I4:274 (the constructive bound beside the theorem).
- Effective by a calculus estimate, of size a dimensional constant times one finite symbol or coefficient seminorm:
  II.A:960, II.A2:130, 186, 188, 276, 281 (Calderon-Vaillancourt, the composition remainder, integration by parts for
  separated supports, the multilinear bound with C = 2^r printed). Not computed here.
- Effective by reading the chained proofs, C_k a product of the composed statements' constants: J3:41, 82.
- Effective given a base inverse bound: III.H:425. The Taylor coefficients of R(s) = P(s)^-1, P quadratic in s, obey
  c_i = -R*(A c_(i-1) + P2 c_(i-2)), so **||R^(i)(s*)||/i! <= ||R*|| [h^i] 1/(1 - a h - p h^2)**, a = ||R*|| ||A||,
  p = ||R*|| ||P2||: locally uniform with no Banach-Steinhaus, polynomial of degree i + 1 in the SIGMA base ||R*||
  (checked on 200 random matrix families; without the P2 term it fails, C2).
- Not effective without a computed lower bound: II.F:1400 (open mapping). Its constant is 1/sigma_min(T on ker Pi),
  unbounded at fixed ||T|| and projection constant (K3): the N1 kind.
- Hidden orders and losses (V-m1): d0 (II.A:960), the seminorm order M (II.A2:188, 276), the residual order (II.A2:130),
  eps'(eps, k) (J3:41), the statement's loss (J3:82).

(c) No quantitative replacement of an N-row is computed; round 1's upper bounds (log10 delta < -7.6666e16, lambda1 <
delta) stand.

### R2.5 Proved, computed, open

- *Deduced (with programs)*: eps1 any value < 3/5 (R2.2 (b)); the Cartesian forms of W_TT, chi dv dv, S (R2.2 (c));
  E_++ and G add no chain, E_col's candidate bases (R2.3 (a)-(b)); Lambda_* and the pairs cost no derivative, the
  windows run above 3 (R2.3 (c)); the explicit escape and time functions (R2.4 (a)); the Baire classification and
  III.H:425's replacement (R2.4 (b)); the ninth term of lambda0 (R2.1, V-m4).
- *Computed, exact or certified*: the envelope's e_k (R2.2 (a)); eps1* in [3/5, 0.60132]; the D[n] table and C_app >=
  12.58, lambda0 (this proof) < 0.0239 (R2.2 (c)); e^44.00, and ln C3 >= 7.65e19 on the literal reading (R2.2 (d))
  [Round 3: eps1* in [3/5, 0.6013096]; lambda0 < 0.0239 at the even split only, < 0.0478 for any split, so <=
  lambda_Omega split-free (M1); e^11.0006 and ln C3 >= 3.56e5, a deduced reading (M2)]; (G)
  unbound at 3 + 1.9841e-8, the container 85,025,783 (R2.3 (b)); N(I), H r = 2f, H log tan(phi/2) = -2 sigma0, lambda_L^2
  = 1/(2 mu) (R2.4 (a)); the verifier's corrected figures (R2.1).
- *Conditional, not proved*: d <= 2.4338e16 + 1.0649e8 c (R2.3 (d)).
- *Open, with the exact obstruction*: stage 1's solution and stages 2-9 (R2.2 (e)-(f)); a proved upper bound for d,
  blocked first by Lambda's unlisted increments (R2.3 (e)); every N-row constant and the per-piece microlocal constants
  (R2.4).

### R2.6 Next steps

- lambda0: extract the stage-1 operator's coefficients from `stage5.py`'s expansion and write Lemma 2.3 at g0 with its
  deformation tensor bounded on Omega; then a certified L^2 bound for (m_1, phi_1, Psi_1, Z) at order 0, before any
  commuted order.
- d: compute every indicial root with real part below 5 of the operators behind E_ind and E^iota_ind at n = 4 (III.D''
  3.1, III.F''' 2.2, III.G'' 4.2); that decides H1.
- lambda1, delta: write one microlocal piece's constant out (I.A Proposition 5.1, the elliptic estimate, is the
  simplest), as the template for the others.

### R2.7 Sources (round 2)

N1STAR-PROOF.md:143-235, 339-450, 509-532, 624-662, 697-791; RESPONSE-HL-5D.md:286-288, 1390, 1758 [Round 3: now 1403,
1782]; proof5: PART-I-SPECTRAL.md:60-139, 1384-1404, 1463-1712; PART-II-D-REGULARITY.md:1015-1043;
PART-III-I9-COMMOTION.md:28-66; PART-III-I11-SPACETIME.md:28-166, 340-390; PART-III-I12-SPECTRAL.md:55-110;
PART-III-I13-EXPANSION.md:222-266; PART-III-I2-SCRI.md:177-195; PART-III-I8-UNPARAM.md:35-45;
PART-III-J2-LINEAR.md:18-30, 95-145; the 18 sites of `nrows5.py`; `lead5.py`, `checks/stage5.py` and `.out`,
`checks/gapsums5.py` (the sl roots' formula), `prop31loss5.py`.

## Round 3

*Status (2026-11-02).* Appended to rounds 1-2; not yet read by a verifier. The independent reader of rounds 1-2
(commit bbfb486) has reported; each of its findings is seated, in place where it corrects a line of rounds 1-2 (a
bracketed `[Round 3, ...]` note keeping the old figure) and listed in R3.1. New programs (each with its `.out`, every
control failing as it must): `checks/lzerotrace5.py`, `checks/dceiling5.py`, `checks/nkind5.py`. Changed and rerun:
`gronwall5.py` (rewritten, M2), `eps1hyp5.py` (H2 by the cone argument, H3 at the corner, C1 and C4), `lzeroconst5.py`
(m5), `stage0bd5.py` (X4's text, M1), `deltacap5.py` (C3, C4), `baire5.py` (K3, C3), `lambdagen5.py` (L5's
deduplication, N1, N3, docstring), `envelope5.py` (C1, P0), `nrows5.py` (R3, C3); `dweights5.py` (docstring only).

### R3.0 Summary

- **(i) lambda0: certified lambda0 <= 0.026986 at P*.** Every factor of the proof's lambda0 is traced to its line of
  N1STAR-PROOF.md (27 rows over the nine terms, each fragment asserted on its line, lines 1-805 md5-pinned;
  `lzerotrace5.py` T0). Two terms are evaluated: lam1 = min(1, delta0)/10 = q0/20 = 0.0269859 (:177; certified) and
  eps1/C_app < 0.6013096/12.5933 = 0.047748 (Step 3, :355-357; certified, operator norm), so **lambda0 <= 0.026986**
  for the operator and Frobenius readings of |.|, and **lambda0 < 0.009550** for the largest-entry reading, where the
  second term binds. Label: a certified upper bound on the lambda0 this proof delivers (V-M2), at P* with
  envelope5.py's envelope and a = q0/2; not a value. At round 1's even split of eps1 the term is 0.023874 (operator
  norm); the split is the note's, not the proof's (M1). The seven other terms need the profiles g_1..g_10 (R2.2 (f)).
  A definition of the pointwise norm for the supplement is proposed and checked (R3.2).
  [Round 4, A and m1: the term is < 0.0477484 (operator), and Lemma 2.3 bounds eps1 below 0.0307686, so lambda0 <
  0.0024433 (operator norm; < 0.0019950 Frobenius) and lam1 does not bind (R4.2); the halves' 0.023874 is 0.0238742.]
- **(ii) d: no number and no proved upper bound; the floor stands and the record's own ceiling is computed.** The
  indicial roots of box^Ups(0) below 7, every harmonic type, are now complete (ten non-integer roots; `dceiling5.py`
  D1). Which offsets are Lambda's increments is a reading the record leaves open ("E_ind ... may change from line to
  line", D3:46-48): on the construction reading (LD14) the floor **d >= 8,407,505,890,317,054** (computed, W3) stands;
  on the widest reading (G) binds at 3 + 4.679e-13 (certified, D3) and the floor rises to about 3e20 (estimate).
  The composing recursion, with every per-level step the record charges, gives on the construction reading the exact
  ceiling **d <= 4,527,175,422,273,024 L_0 + 2.9868e30 (l_* + 1) + 28,864,786,304,360,710 + 53,244,736 X_7 +
  106,489,470 c'** (level-2 rounds per exponent; 1.1947e31 (l_* + 1) per (alpha_0, k)), which is **at least 1.49e31**
  at the least admissible L_0 = 1 and l_* = 4 (computed, D6). The size comes from one step rounds 1-2 left inside c:
  III.A Proposition 4.2 (1) at every level above 3 counts the (exponent, log order) pairs of E^flat, which the record
  bounds only through K(lambda) (D5). So **N = 21 d + 6 >= 1.7656e17** and has no ceiling below 3.1e32 in the record's
  bookkeeping.
  [Round 4, m4 and m1: at that parameter point, on the construction reading (the ceiling moves with the weights,
  about 1.44e31 at eps_K near delta_50); N >= 1.765576e17. With l_* >= 10 (R4.3) the form gives 3.2855e31.]
- **(iii) lambda1, delta: upper bounds stand; no lower bound from this proof, the exact obstruction proved.** For each
  of the four kinds of non-effective step, an explicit family on which every input of the step is fixed or bounded
  while its output is unbounded shows that the argument as written gives no bound (`nkind5.py` K1-K4); for N2 and N4
  the effective replacement is computed on the model. So a lower bound for delta and lambda1 needs exactly seven
  certified inverse bounds, at the six N1 sites and the one N3 site (K5), with the Lipschitz moduli in b and sigma
  and the calculus constants of the B-rows; the upper bounds log10 delta < -7.6666e16 and lambda1 < delta stand.

### R3.1 The reader's findings on rounds 1-2 (commit bbfb486), seated

- **M1 (major), lambda0 <= 0.0239 "below lambda_Omega".** Correct. Step 3 (N1STAR-PROOF.md:355-357) asks only |g_app -
  g0| + |w| <= eps1; the halves are round 1's (1.3, `lzeroconst5.py`). Seated: in place at 1.3, R2.0 (i), R2.2 (b)-(c)
  and R2.5; `stage0bd5.py` X4 now prints both forms; `lzerotrace5.py` T5 states lambda0 <= 0.023874 at the even split
  and < 0.047748 for any split (operator norm; the reader's 0.04779 at r = 0.27, mine at r = a), so split-free
  lambda_Omega binds. The pointwise norm: the reader's largest-entry figures reproduced (eps1* <= 0.1202619; the term
  <= 0.00955 split-free, 0.004775 halved); the operator-norm definition is proposed with a computed check (R3.2).
  [Round 4, A: split-free lambda_Omega does not bind once Lemma 2.3 is read with the same eps1 (R4.2); m1: 0.0477484,
  0.0238742 and 0.12026192, rounded outward.]
- **M2 (major), e^44 and the doubly exponential C3.** Correct: the identity at :233-235 keeps -int (3/r) phi^2, and with
  c = 2/r the rate is 1/(2a). Seated: `gronwall5.py` rewritten (G0 the identity in R^4, sympy; G1 e^11.0006 = 5.99e4;
  G2 the equation's ((a + dtau)/a)^2 = 529, excess 113; G3 ln C3 >= 3.56e5 as a deduced reading), with controls that
  mutate the code path (C1 the identity without its -3/r term gives e^44 and fails G1; C2 round 2's b(tau0) bound fails
  G2; C3 the identity in R^3 fails G0). In place at R2.0 (i), R2.2 (d), (f), R2.5.
- **m1** "one admissible point" (2.3): now "a point meeting every decidable condition" (four remain undecided, 2.1).
- **m2** controls that could not fail on their own, each now mutating the code path it tests: `gronwall5.py` C1-C3
  (above); `deltacap5.py` C3 (P2 rerun with A_2d >= 2^-(32 d + 9): fails) and C4 (P2 rerun with theta0 >= 1: fails);
  `baire5.py` K3 now computes the a priori constant, ||T||, ||Pi|| and the open-mapping constant (SVD on ker Pi), and C3
  reruns K3 on T = diag(0, 1) (fails); `eps1hyp5.py` C1 reruns H3's degeneracy test at size 59/100 (no null boundary)
  and C4 reruns H2 at eps = 0.61 (fails); `lambdagen5.py` N1 runs L4's search, now a function, on the bases plus a
  planted one (returns it as binding), and N3 runs L5's new deduplication of L3's eleven bases (certified pairwise on
  distinct chains and off the 27 existing starts) with a planted duplicate (flagged); `envelope5.py` C1 reruns E3 with
  the flat factor exp(-1/(2t)) removed (fails); `nrows5.py` R3 now tests the claim itself (every N1 row needs one of
  NORM, TENSOR, LOWE, TRAP, after COVER) and C3 re-tags one row (fails).
- **m3** `eps1hyp5.py` H2: replaced by the direct cone argument (g >= g0 - eps I; at eps = 3/5 least eigenvalues 2/5,
  2/5 and mu/(5 r^2) on the three kernels; one negative eigenvalue), which also shows eps1 = 3/5 itself serves.
  [Round 4, A: for Lemma 1.1 (e) only.]
- **m4** labels: R2.0 (iii) and R2.4 (b) now say "computed on the Tangherlini model at b0; a deduction at b0, not
  reaching b != b0" and "a hand-written classification whose coverage is checked".
- **m5** tau_end needs v - r_q(v) increasing, which depends on sup env: `lzeroconst5.py` now checks 1 - q0 (2/9) c^2/4 >=
  0.9474 > 0 with c <= 1.3241035 (READ, envelope5.out E1); R2.2 (a) amended.
- **Nits.** 341 -> 360 (1.3); the V-m5 bracket at 1.4's old control; e_11 of the plain bump is 3.29e18 (`envelope5.py`
  P0, floating point), not 3.6e22, nine orders above 3.796e9; `dweights5.py` (23 chains) and `lambdagen5.py` (L3's
  eleven bases, N2's list) docstrings; RESPONSE-HL-5D.md's lines are now 1403 and 1782 (the paper moves: 1390, 1758 at
  round 2, 1398, 1772 at the reading); R2.0 (iii) "18 sites" are the 11 of classes B and A.
- **Numbers the reader vouches for**, all reproduced here: q0 = 0.539717577; tau_end - tau0 = 5.937208254; lambda_Omega =
  0.026985879; C_S <= 43.2158; eps1* in [3/5, 0.6013096]; C_app >= 12.583585 (r = 0.27; 12.5933 at r = a); c in
  [1.32407111, 1.32410349]; lambda0 <= 0.023893 at the even split (r = 0.27), < 0.047786 for any split; log10 delta <
  -7.6666e16; lambda1 < delta; K = 106,489,469, R2 = 1,401,250,931,461,121, R3 = 1,401,251,031,977,897, the floor and
  the conditional bounds of rounds 1-2.

### R3.2 (i) lambda0, complete as far as it goes

- *The trace* (READ, computed; `lzerotrace5.py` T0). The nine terms of 1.3 (with V-m4's) and their factors: lam1 at
  :177 with q0 at :145 and a := q0 - delta0 at :146; E-a at :160-162 (eps1, the lateral boundaries), :150 (the outer
  boundary), :356 (Step 3), :94-96 ((0.4), profiles bounded independently of lam), :113 (|g - g0| <= C lam), :541 (g1 =
  m1 + W(X, th + phi1(X)), g_j independent of lam), :461-462 (W = W_TT + chi dv dv); E-b at :348, :425, :427; E-c at
  :356-357; E-d at :400-401 and :92; D-a at :769 and :795; D-b at :772; D-c at :692; D-d at :771. Every fragment is
  asserted on its line; shifted by one line, 27 of 27 fail (C1).
- *The evaluated factors* (certified). q0 in a certified interval of width 1e-25, lam1 = q0/20 = 0.0269859 (T1). eps1:
  at the corner r = b(tau0) of the outer boundary (tau = tau0, mu = mu_end) the Lorentzian metric g0 - lam_n n n^T, n =
  (1, -2 xhat)/5^(1/2) in ker d(v + tau), lam_n = (3 + mu_end/r^2)/5 = 0.6013096, makes the boundary null (exact, T2).
  C_app: lead5.py's W_TT is diagonal in (th, phi1, phi2) with Euclidean eigenvalues -2(a1 + a2), 2 a1, 2 a2 (sympy),
  -2/3, 4/3, -2/3 times env(v) r^(-3/2) at th = 0, phase 0; at (v, r) = (2, a), a point of Omega, |W_TT| >= 12.5933
  (operator, largest entry) and 15.4236 (Frobenius), certified with c's lower end (T3); W_TT is odd under th -> th +
  pi and chi, m1 even, so every admissible C_app is at least sup |W_TT| (T4, deduced).
- *The bound* (certified, T5). Operator norm: eps1/C_app <= 0.047748, lambda0 <= 0.026986 split-free, <= 0.023874 at
  the halves; Frobenius: 0.038986, 0.026986, 0.019493; largest entry: 0.009550, 0.009550, 0.004775. Against the
  numerics' wavelength 10 l5 = 1, a factor above 37 at a = q0/2 (and above 18.5 for every a, lam1 <= q0/10).
- *Proposed definition for the supplement* (deduced; checked, T6 and `eps1hyp5.py` H2-H3). N1STAR-PROOF.md lines 1-805
  use |.| for arrays without defining it. Proposed, after (0.3): "For an array A of Cartesian components, |A| is the
  Euclidean operator norm (for symmetric A, the largest absolute eigenvalue)." With it Lemma 1.1 (e) holds with eps1 =
  3/5: |g - g0| <= 3/5 gives g >= g0 - (3/5) I as forms; g0 - (3/5) I is positive definite on ker dtau (least 2/5), on
  ker dr at r = a (least 2/5 at P*) and on ker d(v + tau) (least mu/(5 r^2)) and has exactly one negative eigenvalue,
  so its causal set is a double cone of convex halves on which dtau, dr (at r = a) and d(v + tau) keep their signs;
  and no eps1 above 0.6013096 serves. The Frobenius norm dominates it (same eps1); the largest-entry norm would give
  eps1* in [3/25, 0.1202619] and lambda0 < 0.00955.
  [Round 4, m1 and A: 12.593309 (rounded down), 15.423591, 0.0477484, 0.0389864, 0.0194932, 0.12026192, rounded
  outward (`lzerotrace5.py` T2-T5); and every reading's eps1 is below 0.0307686 (Lemma 2.3), so lambda0 < 0.0024433
  (operator, largest entry) and < 0.0019950 (Frobenius); the margin over 10 l5 is above 409, not 37 (R4.2).]
- *What a value needs* (unchanged, R2.2 (f)): certified solves of stages 1-9, with the profile bounds to order about 11.

### R3.3 (ii) d

- *D1 (exact; certified).* box^Ups(0)'s roots (gaugepot5.py G1's factors, READ): s0 gives 0, 3, (1 +- (9 + 4z)^(1/2))/2;
  vl gives -l, l + 2; sl gives l + 3, 1 - l and the roots of Q_l(lam (lam - 1)), whose discriminant is (z + 2)^2 + 4
  kappa, so that at z = 0 they are l + 1 and l + 2. At z = 4e-6 the non-integer roots in (0, 7) are exactly ten: 2 +
  d0 (d0 = 1.333e-6), l + 1 + delta_l (l = 1..5; delta_1 = d1 = 3.333e-7) and l + 2 + delta'_l (l = 1..4), every offset
  in (0, 1.4e-6); the integer roots there are 3, 4, 5, 6. Control C1: at z = 0 every offset vanishes.
- *D2 (READ, deduced).* E_ind is "an index set with min Re E_ind >= eps_ind, which may change from line to line"
  (D3:46-48, F4:28-30); I5:190 and I8:35 fix it as the index sets of III.D'' Proposition 3.1 and III.F''' Proposition
  2.2, built by III.A Lemma 1.4 from the roots above (F4:67-80). Which offsets enter Lambda's increments is therefore
  the reading of LD14 (only d1 below 1: the construction, checked state by state) or the widest one (every offset).
- *D3 (certified).* On the widest reading d0 and d1 alone bring 2 + n0 d0 + n1 d1 to 3 + 4.679010e-13 (n0 = 350,001, n1
  = 1,599,998; gapsums5.py G2 reproduced on certified intervals), 4.15e4 times below delta_50: round 1's weights are
  then inadmissible, eps_K < 4.68e-13, K > 4.27e12, and the floor rises to about 3.4e20 (estimate, W3 scaled). On the
  construction reading the same search gives 3 + 5.0191e-8 (control C3): (G) does not bind.
- *D4 (exact).* Construction reading, every generator of rounds 1-2: n_0 = |Lambda cap {Re < 2}| = 1,470,302, P_iota =
  |Lambda cap [2, 3 + eps_+ - eps]| = 85,025,784, P_W = 85,025,783 (round 2's container), n_W = 1,470,303. The record's
  log-order ceiling K(lambda) = L_0 + (N_* + 1)(l_* + 1)(n(lambda) + 1) (I11:72-80) summed over them: S_iota = 85,025,784
  (L_0 + 1) + 3,739,705,595,186,988 (N_* + 1)(l_* + 1) and S_W = 85,025,783 (L_0 + 1) + 3,739,705,593,716,685 (N_* + 1)
  (l_* + 1), N_* = 15,000,015 (control C2: the closed form against a brute-force sum).
- *D5 (deduced; READ I12:249-253, I14:120-121, I11:339-343, LOSS-D (2.1)).* III.I''''''''''' Proposition 3.1's Step 0
  applies III.A Proposition 4.2 (1) with E_iota = E^flat + 2, beta_iota = w_+ - eps and E_I = E_K empty;
  III.I''''''''''''' repeats it at every level above 3. Its loss is 1 + n_iota + 2 max(floor beta_K, floor B) = 11 +
  n_iota, n_iota the pairs (z, m) of E_iota below beta_iota, and the record bounds E^flat only by pi_1 E^flat in Lambda
  cap [2, 3 + eps_+) with log order <= K(lambda): n_iota <= S_iota, >= 5.6e22 per level at l_* = 0 (control C4: with
  E_iota empty, 11).
  [Round 4, m4: the bound is on S_iota: S_iota >= 5.6096e22 at l_* = 0, 2.80e23 at the least admissible l_* = 4.]
- *D6 (exact).* The composition over the levels, construction reading:

      d <= 3 (R2 + R3) + L_above [3 X_2 + 11 + S_iota + 15 W] + L_below [15 W + 58] + L_above X_7 + (K + 1) c',

  W = 1,470,302, L_above = 53,244,736, L_below = 53,244,734, X_2 the level-2 rounds per level (P_W per exponent, S_W per
  (alpha_0, k)), X_7 III.A Proposition 4.2 (2)'s loss at Step 7 (I12:389-394, E_K not bounded here), c' the remaining
  fixed per-level steps (FWD's loss is III.I Theorem 5.3's d = D_0 + D_1 + d' + d'' + 6, II.F2-TAME:529-535, with II.E's
  tame orders unnumbered; BG 2; the fixed MODs). Printed exactly as 4,527,175,422,273,024 L_0 + 2,986,797,742,916,004,
  835,692,267,122,688 (l_* + 1) + 28,864,786,304,360,710 (per exponent) and 18,108,701,529,357,888 L_0 +
  11,947,190,968,141,150,306,670,744,890,368 (l_* + 1) + 28,864,786,304,360,710 (per (alpha_0, k)), each + 53,244,736
  X_7 + 106,489,470 c'. At L_0 = 1 and l_* = l_C(R0) = 4 (D7): d <= 1.4934e31 and 5.9736e31; N <= 3.14e32 and 1.25e33.
- *D7 (exact).* The largest log order of E^C_I at Re <= 5 is 4 on one corner union (R0) and 16 on III.C' (3.1) as
  written with M = 4 (R1); l_* >= l_C by its definition (I11:72-75).
- *The exact obstruction to a proved upper bound.* (1) The reading of E_ind (D2): the record does not fix it, and
  the widest reading changes even the floor (D3). (2) l_*: besides E^C_I's log orders it bounds E_ind's and
  E^iota_ind's at Re <= 5 and the pole orders of N_iota+(L-bar, .)^-1, of which the record shows only that
  spec_iota+(L-bar) is discrete in Re >= 2 (III.G' Lemma 4.2 (a), G2-IOTA:428-431): the iota+ boundary spectrum below
  5, with its pole orders, has to be computed. (3) L_0: the log orders of the class's index sets E^0_src, E_++, G, 2 +
  E_col below 2 lambda_sharp (computable for the least class; not done). (4) X_7: the K+-exponents of III.G''''
  Proposition 4.4's zero-frequency terms. (5) c': II.E's tame orders d^E_0, d^E, d^S, d-tilde (II.F2-TAME:528-532),
  unnumbered there. (6) The three readings of round 1 (2.6). And the ceiling is a ceiling of the record's bookkeeping:
  the log orders actually produced are not computed, and only they could bring it near the floor.
  [Round 4, m5: l_* also bounds the multiplicities of the indicial roots of L-hat_b0(0) (I11:76-77). R4.3: the iota+
  pole orders are computed (all 1 at Re <= 5 in the class), and E_ind's Lemma 1.4 log orders reach 10 at Re 5.]

### R3.4 (iii) lambda1 and delta

- *The non-effective steps, made precise* (`nkind5.py`; computed, exact). N1 (I.C:494-498 and five more): on P_e =
  diag(e, 1, ..., 1), j = diag(1, 1/2, ..., 1/6), the a priori constant is 1/(1 + e) <= 1 (exact: the denominator is
  concave in the weights u_i^2, so the supremum is on an axis; 400 rational vectors checked exactly), ||P_e|| = 1, ker
  P_e = 0, and the output C' = 1/e (K1; control C1 at e = 1). N2: P_e(p) = diag(p + e, 1), Lipschitz 1, pointwise
  bounds finite, supremum 1/e; the Neumann cover with radius 1/(2 L M_i) bounds it by 2 max M_i in 4, 8, 11 explicit
  steps at e = 1/10, 1/100, 1/1000 (K2; C2: radius 1/(L M_i) breaks the factor 2). N3: diag(h l, 1), output 1/l, the
  inverse expansion rate the argument does not produce (K3). N4: radius e everywhere, ceil(1/(2e)) patches; with K2's
  radii the counts are computed (K4; C4).
- *The seven quantities* (K5; READ at the lines, deduced). A lower bound for delta and lambda1 from this proof needs,
  besides d, the calculus constants of the B-rows (`baire5.py`) and Lipschitz moduli in b and sigma: sigma_min of
  P-hat(0) on (3.2)'s b-Sobolev pair (I.C:497); the inverse of P'_{h,z} on the strip of I.B Theorem 1.3 (I.B:1685);
  ||P-hat(sigma)^-1|| in the middle range (I.B:1978); sigma_min of T on ker Pi (II.F:1393); the inverse of L-hat_b(sigma)
  off zero frequency (III.F'':223); the inverse of box-hat(sigma) on X_sigma -> Y_sigma (III.D:365); and the trapping
  multiplier constant (I.B:1513), whose rate is known at b0 (lambda_L^2 = 1/(2 mu), `cover5.py`).
- *The passage from E2-PILOT to the write-out's spaces* (deduced). E2-PILOT certifies ||chi_I R_l(sigma) chi_I|| <=
  11.477 on L^2(dr_*) for 3 <= sigma <= 384 and every l, with H^1 on I; III.D:365 asks the inverse on X_sigma ->
  Y_sigma, variable-order b-Sobolev spaces through the horizon with weights at infinity. The passage is a gluing of
  three bounds: E2-PILOT's on I, and bounds for sources and solutions near the horizon and near infinity, which in the
  write-out come from I.A's radial-point and propagation estimates (Propositions 4.2, 4.6, 4.9, 5.1, 5.2) with constants
  of the calculus that are not written out (R2.4 (a): only the cover counts are explicit, at b0). So the passage is
  blocked by those per-piece constants, not by E2-PILOT, and it covers only 3 <= sigma <= 384: I.C (sigma -> 0) and
  I.B (|sigma| large) need their own certified bounds.
- *Upper bounds* (stand): log10 delta < -7.6666e16 (d >= 7.959e15) and < -8.0987e16 (the W3 floor); lambda1 < delta
  (`deltacap5.py`, whose controls now fail on their own, R3.1 m2).

### R3.5 Proved, computed, open

- *Certified*: lambda0 <= 0.026986 at P* (operator and Frobenius readings), < 0.009550 (largest entry); eps1* in [3/5,
  0.6013096]; C_app >= 12.5933; the root census of box^Ups(0) below 7; (G) at 3 + 4.679e-13 on the widest reading.
- *Computed, exact*: the trace table; the ceiling's coefficients and the counts n_0, P_iota, P_W, n_W; l_C = 4 and 16;
  the models of K1-K4.
- *Deduced*: the split-free form of E-a; the proposed norm and the cone argument; D2, D5; the seven quantities and the
  gluing obstruction.
- *Open, with the exact obstruction*: a value of lambda0 (the nine stage solves); a number or proved ceiling for d and
  N (R3.3's six items, first the reading of E_ind and the iota+ boundary spectrum below 5); lower bounds for lambda1 and
  delta (the seven inverse bounds of R3.4, then the Lipschitz moduli and the B-row constants).
  [Round 4: lambda0 < 0.0024433 replaces lambda0 <= 0.026986 (A); the pole orders are no longer open (R4.3); the
  II.F:1393 constant also contains ||Pi|| (the Hahn-Banach projection), which the R3.4 list omitted.]

### R3.6 Proposed text for the paper's section 9 (for the bullets "Settling" and "Physical wavelengths")

    The threshold lambda0 that the proof of Theorem 1 delivers is traced factor by factor to the supplement; at the
    numerical point (l5 = 1/10, mu0 = 1, a = q0/2, a smooth envelope with the numerics' integral) it is at most
    0.0270 (certified, the proof's own standing condition; the term eps1/C_app is below 0.0478 with the pointwise norm
    read as the operator norm, which the supplement now states), so the wavelength 10 l5 lies more than 37 times
    beyond it; a value would need certified solves of the approximant's nine linear stages. The loss d is not a
    number: d >= 8.41 x 10^15 and N >= 1.77 x 10^17 at a parameter point meeting every decidable condition (computed),
    while the write-out's own bounds give no ceiling below 1.49 x 10^31, one index-set count being bounded only by the
    log-order ceiling of its construction; a proved ceiling needs the pole orders of the iota+-normal operator's
    inverse below real part 5. lambda1 and delta are bounded above, log10 delta < -7.66 x 10^16 and lambda1 < delta;
    no lower bound follows from this proof, whose arguments at six injectivity steps and one trapping estimate give
    no number: seven certified inverse bounds in the write-out's norms would have to be computed instead.
    [Round 4: superseded by R4.6, which seats the reader's corrections: 'term by term' for 'factor by factor' (m2),
    below 0.0025 (A), d >= 8.40 x 10^15 and N >= 1.76 x 10^17 (m1), 'at that parameter point' (m4).]

### R3.7 Sources (round 3)

N1STAR-PROOF.md:83-113, 143-177, 155-235, 339-401, 461-462, 538-541, 663-795; lead5.py:1-20, 58-67; gaugepot5.py G1
(docstring); proof5: PART-III-D3-SYMSTATES.md:36-48; PART-III-F4-ZERO.md:20-35, 60-84; PART-III-I5-UNBOOST.md:185-195;
PART-III-I8-UNPARAM.md:30-42; PART-III-I11-SPACETIME.md:20-110, 336-392; PART-III-I12-SPECTRAL.md:20-80, 240-256,
386-402; PART-III-I14-LEVELS.md:96-135; PART-III-I15-AUGMENT5.md:252-266; PART-III-G3-GRAFT.md:280-352;
PART-III-G2-IOTA.md:400-460; PART-III-I-CONE.md:394-450; PART-II-F2-TAME.md:525-545; PART-II-E-ENERGY.md:842-856,
1148-1170; PART-III-J3-TAME.md:30-300; the seven sites of R3.4; LOSS-D.md sections 1-2b, LD14-LD16; E2-PILOT.md
section 4; EFFECTIVE-CONSTANTS.md sections 3-5; EFFECTIVE-LEDGER.tsv; the reader's report (commit bbfb486).

## Round 4

*Status (2026-11-02).* Appended to rounds 1-3; not yet read by a verifier. The independent reader of round 3 has
reported; each finding is seated (R4.1), in place where it corrects a line of rounds 1-3 (a bracketed `[Round 4, ...]`
note after the line, the old figure kept). New programs (each with its `.out`, every control failing as it must):
`checks/iotapoles5.py`, `checks/zeroinv5.py`. Changed and rerun: `lzerotrace5.py` (re-pinned, T7, T5, controls),
`lzeroaudit5.py` (re-pinned), `dceiling5.py` (D5, D6), `nkind5.py` (C1, K4, C4, K5), `eps1hyp5.py` (H2 exact),
`dweights5.py` and `stage0bd5.py` (printing rounded outward).

### R4.0 Summary

- **(i) lambda0 < 0.0024433 (certified), and lam1 no longer binds.** Lemma 2.3 takes Lemma 1.1 (e)'s eps1 and needs it
  below g0's least absolute Euclidean eigenvalue on Omega (N1STAR-PROOF.md:89-92, :222; the reader's MAJOR A). That
  [Round 8, re-pointed by content (D623 moved sections 0-4 by 36 lines): N1STAR-PROOF.md 0.3, "Lemma 2.3 needs more of
  the same eps1: eps1 < s0, where s0 := inf over Omega of g0's least absolute eigenvalue", with "one fixed number with
  0 < eps1 < min(s0, mu0/a^2 - 1)"; Lemma 2.3 now carries "|gt^-1| <= (s0 - eps1)^-1". At the point mu0/a^2 - 1 > 12,
  so the minimum is s0 in [0.030768559, 0.030768560], and every lambda0 bound here (eps1 < s0, C_app >= 12.593309)
  agrees with the new 0.3.]
  infimum is (m*^2 + 1)^(1/2) - m*, m* = mu_end/a^2, attained at the corner (tau_end, r = a), and lies in [0.030768559,
  0.030768560] (`lzerotrace5.py` T7). With C_app >= 12.593309: **lambda0 < 0.0024433** in the operator norm the
  supplement now states (< 0.0019950 Frobenius), so 1/lambda0 > 409.2 against the wavelength 10 l5 = 1. No linear stage
  is solved; the exact obstruction is in R4.2.
  [Round 5, R5.1 (a): the Frobenius figure rests on a rank-one perturbation, not on the ball inclusion R4.2 states
  (`lzerorank5.py` R1); the largest-entry reading gives < 0.0012968 (R2).]
- **(ii) d: the iota+ pole orders are computed, and they are not what keeps the ceiling high.** By the Mellin transform
  the poles of N_iota+(L-bar, .)^-1 on one harmonic reduce to an explicit product of the indicial matrices (R4.3,
  deduced); computed exactly in the class (s0, t2, and every even l >= 2 at once): every pole with real part <= 5 is
  simple (`iotapoles5.py` M3-M4). On the narrowest reading the write-out supports (the construction's, LD14, fixed once
  at I5:190, I8:35, I10:38-40), III.A Lemma 1.4 gives E_ind log order 2w at the integer w, 10 at real part 5 (M5), so
  l_* >= 10 there and the record's form gives **d <= 3.2855e31 + 53,244,736 X_7 + 106,489,470 c'** at that parameter
  point (M6). The size is III.A Proposition 4.2's count through K(lambda): with log order at most 2 at every exponent of
  E^flat, a hypothesis the record does not prove, the same accounting gives d <= 3.7919e16 + 53,244,736 X_7 +
  106,489,470 c', 4.5 times the floor.
- **(iii) lambda1, delta: one of the seven inverse bounds attempted.** The cheapest site is I.C:497 (zero energy, an
  ODE per class harmonic with closed-form solutions at b0). For the scalar model at b0 the inverse on every even l >= 2
  is bounded by 1/(l (l + 2)) <= 1/8 in an exterior weighted L^2 norm (certified: an exact identity; `zeroinv5.py`); it
  is not yet in the write-out's norm, nor for L_b0 (R4.4).

### R4.1 The reader's findings on round 3, seated

- **Re-pinning (D614).** N1STAR-PROOF.md gained the norm paragraph at :87-92; every line above 86 moved by +7 from the
  pre-D612 text. `lzerotrace5.py` and `lzeroaudit5.py` now pin lines 1-812 (sections 0-6; md5 6e8947ad...) and the whole
  file (md5 02e76176..., 10853 lines); every trace fragment and census row is moved by +7, the new lines classified
  (:89, :90, class E), and both pass. Every round-3 citation of N1STAR-PROOF.md above line 86 (R3.2, R3.7: :94-96, :113,
  :145-177, :215, :348-401, :425-427, :461-462, :541, :692-795) reads +7 now: :101-103, :120, :152-184, :222, :355-408,
  :432-434, :468-469, :548, :699-802 (lines below 87 unchanged).
- **MAJOR A (lambda_Omega does not bind).** Correct, and the infimum asked for is computed: it equals the corner value
  (above). `lzerotrace5.py` T7 (new, certified) and T5 (now with the Lemma 2.3 term); control C6 (T7 run with mu0 for
  mu_end) fails as it must. In place at :361, :454, R3.0 (i), R3.1 M1, R3.1 m3, R3.2, R3.5 and R3.6 (notes). The figures:
  E-a < 0.0024433 (operator, largest entry), < 0.0019950 (Frobenius); the reader's 0.0024433 and "above 409" reproduced.
- **m1 (outward rounding).** `lzerotrace5.py` prints with `up`/`down` on exact Fractions; `dweights5.py` W3 prints N >=
  1.765576e17; `stage0bd5.py` X4 prints 12.583585 (floor). Notes at :195, R3.0, R3.1, R3.2, R3.6.
- **m2 (gaps in the trace).** Rows added for tau_end (:155), b(tau) (:159), mu' (:126), Lemma 2.3's eps1 (:222) and the
  D614 sentence (:91), C_S (:186), C_R (:108), C_D (:110), C2 (:406), C_c (:775): 37 rows, all found; "term by term".
- **m4.** "At that parameter point, construction reading" (notes at R3.0 (ii), R3.6); at :767 the bound is on S_iota
  (S_iota >= 5.6096e22 at l_* = 0, 2.80e23 at l_* = 4).
- **m5.** Obstruction (2) of R3.3 now names the multiplicities of the indicial roots of L-hat_b0(0) (I11:76-77); see
  R4.3.
- **m6.** T3's c from `iv.sqrt` (outward); T6's and `eps1hyp5.py` H2's signature checks exact at five m (sympy signs),
  "every m >= 0" labelled deduced from the closed form.
- **II.F:1393** also carries ||Pi|| (the Hahn-Banach projection of Lemma 5.2's proof): noted at R3.5; R4.4 counts it.
- **Controls that could not fail, now mutating their path.** `lzerotrace5.py`: C3 runs T4's parity test on the wave
  with its phase doubled (fails); C4 runs T3's own domain test (`in_omega`, which T3 now uses); T2's nullness is tested
  through gp^-1(d(v + tau), d(v + tau)) = 0, not by construction; the Frobenius figures are asserted (T3: 15.423591 <=
  Frobenius < 15.4236; T5: < 0.0389865). `dceiling5.py`: D5 computes its loss 1 + n_iota + 2 floor B from the weights,
  D6 asserts the exact forms and rebuilds the constant term from R2, R3, P_W, P_iota, W (the reader's mutants D_b, D_c,
  D_e change them). `nkind5.py`: C1 runs K1's own computation and test on the family held at e = 1; K4's test is now
  count x e >= 1/2 at every e, and C4 runs that same test on the effective counts [4, 8, 11] (fails); K5 reads each
  site's non-effective step on its line.
- **The reader's proposed R3.6 text** is folded into R4.6.

### R4.2 (i) lambda0

- *The Lemma 2.3 term* (certified; `lzerotrace5.py` T7, T5). g0 = eta + m U U^T, U = (1, xhat), m = mu/r^2, has the
  Euclidean eigenvalues 1 (three times) and m +- (m^2 + 1)^(1/2) (exact); the least absolute, (m^2 + 1)^(1/2) - m,
  decreases in m; mu <= mu_end and r >= a on Omega, and the corner (tau_end, r = a) lies in Omega with v > v_end. So inf
  over Omega = (m*^2 + 1)^(1/2) - m*, m* = mu_end/a^2 in [16.234970, 16.234971], in [0.030768559, 0.030768560]. Every
  reading's ball |g - g0| <= eps1 contains the operator-norm ball, so eps1 < 0.0307686 in each, and lambda0 <=
  min(lam1, eps1/C_app) < **0.0024433** (operator; largest entry the same), < 0.0019950 (Frobenius).
  [Round 5, R5.1 (a): the inclusion is false for the Frobenius ball, which lies inside the operator ball; the figure
  stands by the rank-one perturbation (s - m) e e^T, of equal operator and Frobenius size; largest entry < 0.0012968.]
- *What a value needs, and how far the stages went* (deduced; none solved). lambda0 is a minimum of the nine terms
  (R3.2's trace, 37 rows); each further term can only lower the bound, and a value needs lower bounds for all of them.
  Stage 0's profiles are certified to order 14 (round 2, `stage0bd5.py`). Stage 1 is Lemma 5.3 (a)-(c)
  (N1STAR-PROOF.md:521-539): a wave equation for m_1 coupled to transports for phi_1, Psi_1 and Z. Its source is
  explicit (`stage5.out` S2), but its lower-order coefficients B-bar, C-bar are not extracted by any instrument
  (`stage5.py` S1 checks the structure only), its data are Lemma 6.2's, and a certified a priori bound needs Lemma
  2.3's constant C(M1) at gt within 0.0307686 of g0, which is not written out. Interval arithmetic (Arb) cannot start
  before those three exist; stages 2-9 depend on stage 1.
  [Round 5, R5.1 (g): `checks/bbar5.py` (D569) extracts B-bar = B0 and C-bar = C0 + Delta C; stage 1's operator is
  box~ at g0, so it needs Lemma 2.3 at gt = g0, written out in R5.5; the data remain the obstruction.]

### R4.3 (ii) d

- *The reduction (deduced; checked on the free model, `iotapoles5.py` M1-M2).* On one harmonic of a type with K
  components, N_iota+(lam) h = f is (D - lam) L1(D) h + v N(D) h = F, D = v d_v, L1(x) = C - x (C constant, spec C =
  3/2 + a part of spec S-bar), N the indicial matrix of L~(0) (iota5.py I1; READ, G2-IOTA:27-30). (a) The Mellin
  transform h-hat(zeta) = int v^-zeta h dv/v gives (zeta - lam) L1(zeta) h-hat(zeta) + N(zeta - 1) h-hat(zeta - 1) =
  F-hat(zeta) (M1). (b) For Re lam >= 2 the K solutions that decay at v = oo (the K roots of det N with Re <= 0: checked,
  M3-M4) form V(lam), and their transforms are holomorphic on S = {0 < Re zeta < 3/2}, every exponent at v = 0 (lam,
  spec C) having real part >= 3/2. (c) h in V(lam) is pure (no v^lam) iff h-hat continues regularly to zeta = lam; the
  residue there is rho(lam) h = Pi_j(lam) h-hat(lam - j), Pi_j = -((j - 1)!)^-1 L1(lam)^-1 N(lam - 1) L1(lam - 1)^-1 ...
  L1(lam - j + 1)^-1 N(lam - j), with lam - j in S, off the exceptional set spec C + N_0. (d) h -> h-hat(lam - j) is
  injective on V(lam): if it vanishes, so do h-hat(lam - j + 1), ..., h-hat(lam - 1), and h-hat/(zeta - lam + 1) is a
  pure state at lam - 1 vanishing at lam - j; descending, a pure state at lam - j, Re < 3/2 < 2, which III.G Theorem
  5.1 (2) excludes. (e) Per harmonic the resolvent is h_p - B(lam) rho(lam)^-1 c(lam), h_p the solution vanishing near
  oo and c(lam) its v^lam coefficient at 0, which ranges over C^K as f ranges over C_c^oo; so the pole order at lam0 is
  that of Pi_j(lam)^-1, a product of N(lam - i)^-1 and L1(lam - i + 1): the poles lie at r + i, r a root of det N with
  0 < Re r <= Re lam0 - 1, i >= 1, and a single singular factor at a simple root gives order exactly 1. At an exceptional
  point with no root an integer distance from spec C, Pi_j^-1 is holomorphic and the order is at most c's, 1.
- *Computed (exact; M3-M4).* s0 (K = 4): spec C - 3/2 = {0.0099, 0.02, 499995.1171875, 10^6}; det N = x (x - 2)(x - 4)
  (250000 x^2 - 750000 x - 1)(cubic), four roots with Re <= 0, and in (0, 4] the simple roots 1.0000747438, 2, 3 + d0,
  4. Poles at Re <= 5: 2.0000747, 3.0000747, 4.0000747, 3, 4, 4 + d0 (order 1 each) and 5, where N(4) and N(2) are both
  singular: the exact Laurent expansion of Pi_4(5 + eps)^-1 has order 1, residue of rank 2 (control C4: the adjugate for
  N(2 + eps)^-1 gives order 0) [Round 5, R5.1 (b): C4 is (order - 1, rank) of this answer whatever it is, so it cannot
  fail on its own; `iotamut5.py` U3 and X1 replace it]. t2 (K = 1): det N = -(x - 4)(x + 2)/2, one pole, 5, order 1.
  Every even l >= 2: the
  physical root 4 at l = 2 only; box^Ups's roots plus 1 never in (0, 4]; box^C's roots minus 1 from damping5.py's
  sextic: its discriminant and its resultants with its shifts by 1, 2, 3, and its values at 5/2 + s + m, have no root
  kappa = l (l + 2) at any even l >= 2 (exact isolation), and at l = 2 no box^C root is an integer. So at every even l
  all roots of det N with 0 < Re <= 4 are simple, none two differ by 1, 2 or 3, none is exceptional: **every pole of
  N_iota+(L-bar, .)^-1 with real part <= 5 in the class is simple.** At l = 2 the s2 poles below 5 are 2.0000029,
  3.0000029, 4.0000029, 2.000193, 3.000193, 4.000193, 2.9998948, 3.9998948, 4.9998948 and 5. This places 10.37 (d)'s
  candidates and settles 10.37 (e)'s "not computed there": 2.0000747438 is a pure resonance at the record's point.
  Controls: C1 (the shift zeta + 1), C2 (the constant 1 for 3/2), C3 (the product without the shift) fail.
- *E_ind fixed by the narrowest supported reading, and its log orders (M5; READ III.A Lemma 1.4, A-PREREQ:176-182; F4
  Lemma 2.1, F4:66-80).* "May change from line to line" (D3:46-48) is the notation; at I5:190 and I8:35 E_ind is fixed
  once as the index sets of III.D'' Proposition 3.1 and III.F''' Proposition 2.2 at b0, enlarged at I10:38-40 by III.D'''
  Proposition 3.1's and (2,0), and D4:54-59 states that every exponent of the construction lies in M: so the narrowest
  reading is the construction's, whose offsets below 1 are {d1} (LD14). Its log orders are those the construction
  proves, which is III.A Lemma 1.4's set at each site: at F4 Lemma 2.1 (k = 2) the recursion with the integer roots
  3, 4, 5, ... gives log order 2w at k + w, so **E_ind has log order 10 at real part 5** (9 at k = 1); control C6 (plain
  unions) gives 0. So l_* >= 10 on this reading; the other constituent sites (III.D''' with bases <= 0, III.F''' 2.2,
  E^iota_ind's list at G3:338-339) are not computed, so 10 is a lower bound for l_*, not yet an upper one.
  [Round 5, R5.1 (c): M5's root set is every type's, on which E_ind also holds (d0, 0) below 1 (the widest reading);
  on the block reading that the lines support at b0 the offsets below 1 are {d1} and the log order at 5 is still 10,
  from v1 (`eflat5.py` F1, C3).]
- *l_*'s other items.* Pole orders: 1 (above). Multiplicities of the indicial roots of L-hat_b0(0): 1 at every class
  root with 0 < Re <= 4, and every box^C root simple at every even l (the discriminant). E^C_I: 4 (R0) or 16 (R1).
- *L_0, X_7, c' (deduced; not settled).* L_0 >= 2 on the same reading (G = (2,0) U (2 + E_ind) carries (3, 2)); its
  upper bound needs E_++'s and E_col's log orders below 2 lambda_sharp. X_7 needs Step 5's K+-exponents (III.G''''
  Proposition 4.4's zero-frequency terms; I12:389-394), not computed. c' needs II.E's tame orders d^E_0, d^E, d^S,
  d-tilde (II.F2-TAME:528-532), which II.E does not number.
- *The ceiling (M6, exact).* dceiling5.py D6's per-exponent form, its constant term rebuilt from its parts: at L_0 = 1,
  d <= 1.493399e31 (l_* = 4) and **3.285478e31 (l_* = 10)**, + 53,244,736 X_7 + 106,489,470 c'; N <= 6.8995e32 + ....
  Replacing K(lambda) by the pole orders is not what the record supports: E^flat's log orders accumulate along Lambda's
  chains (I11 Lemma 1.2 (c)), and the pole orders enter K(lambda) only through l_*. As a measure of where the size
  sits: with log order <= 2 at every exponent of E^flat (n_iota <= 3 P_iota), the same accounting gives d <=
  37,919,137,148,906,758 + 53,244,736 X_7 + 106,489,470 c' (3.7919e16; N <= 7.9630e17 + ...), 4.5 times the floor.
  [Round 5, R5.2: the construction's own log orders are <= 2 except at 26 points (excess 23 on R0, 44 on R1), so this
  is the ceiling on the construction's count, not a hypothesis (deduced; `eflat5.py`).]
  [Round 6, R6.0 M1-M2: R1's excess is 47, not 44 (the completion between (3.2)'s rounds); and "not a hypothesis" is
  withdrawn: it is a deduced ceiling on a step-by-step reading of I11:352-387, which the write-out does not state.]
- *The exact obstruction to a proved ceiling, now.* (1) The log orders of E^flat actually produced (the record's
  K(lambda) alone puts the ceiling at 1e31); (2) E_ind's and E^iota_ind's Lemma 1.4 log orders at every constituent
  site (one site computed, 10); (3) L_0; (4) X_7; (5) II.E's tame orders in c'; (6) round 1's three readings.

### R4.4 (iii) lambda1 and delta

- *The cheapest site* (deduced). I.C:497 is sigma_min of P-hat(0) on (3.2)'s pair H-bar^(s,alpha)_b ->
  H-bar^(s-1,alpha+2)_b (I.C:378-382). At sigma = 0 the family is stationary and, per class harmonic, an ODE system with
  closed-form zero-energy solutions at b0; the other six need sigma-dependent connection problems or microlocal
  constants (I.B:1513, :1685, :1978; III.F'':223; III.D:365) or a Hahn-Banach projection (II.F:1393, with ||Pi||).
- *Attempted, scalar model at b0* (`zeroinv5.py`; certified: exact). A_l u = -r^-3 (r^3 f u')' + l (l + 2) r^-2 u: the
  solution regular at the horizon is P_(l/2)(2 r^2/mu - 1), a polynomial growing like r^l (Z1), so no zero-energy kernel
  on an even l >= 2 in decaying weights; and r^3 conj(u) A_l u = -(r^3 f conj(u) u')' + r^3 f |u'|^2 + l (l + 2) r
  |u|^2 (Z2) gives ||r^-1 u|| <= ||r A_l u||/(l (l + 2)) in L^2(r^3 dr), the constant <= 1/8 on every even l >= 2.
  Controls: C1 (the next polynomial), C2 (l (l + 1)) fail.
  [Round 5, R5.1 (e): deduced from an exact identity, not certified; sharpened to 1/(l + 1)^2 for every l >= 0, sharp,
  in R5.6.]
- *Where it stops* (deduced). (3.2)'s norm crosses the horizon with s > 1/2 + theta_H derivatives, where f vanishes and
  the identity controls no u' (the radial-point estimate's constant is needed there); l = 0 needs a Hardy inequality with
  f's degeneracy; and the settling operator is L_b0 on 15 components, whose zero-energy kernel is eleven-dimensional
  (10.32 (c)), so I.C:497's sigma_min is on its complement, type by type (s0, s_l, t_l in the class).
- *How the seven glue* (deduced). By frequency: I.C:497 at sigma = 0, carried to |sigma| <= sigma_0 by a Neumann series
  with the Lipschitz modulus ||d_sigma P-hat|| (between the same spaces); I.B:1978 on sigma_0 <= |sigma| <= sigma_1
  (E2-PILOT's certified band 3 <= sigma <= 384, cut-off L^2, in the scalar model); I.B:1685 with the trapping constant
  I.B:1513 above sigma_1 (E2-PILOT 3j's per-harmonic bounds); III.F'':223 and III.D:365 are the same partition for the
  linearised and gauge-potential operators; II.F:1393 at iota+ (sigma_min of T on ker Pi, times ||Pi||). Each enters
  A_2d multiplicatively through the B-rows, and delta = eps/2 with eps <= eps_NM/A_2d (nkind5.py K5).
- *Upper bounds* (stand): log10 delta < -7.6666e16, lambda1 < delta.

### R4.5 Proved, computed, open

- *Certified*: lambda0 < 0.0024433 (operator; < 0.0019950 Frobenius); inf over Omega of g0's least absolute eigenvalue
  in [0.030768559, 0.030768560]; the zero-energy bound 1/(l (l + 2)) of the scalar model on even l >= 2.
- *Computed, exact*: the iota+ poles at Re <= 5 in the class, all simple (s0's at 5 of residue rank 2); E_ind's Lemma
  1.4 log orders 2w (k = 2); the ceiling at l_* = 10, 3.285478e31 + ...; the hypothetical 3.7919e16 + ....
- *Deduced*: the Mellin reduction (R4.3); the narrowest reading of E_ind; the gluing of R4.4.
- *Open, with the exact obstruction*: a value of lambda0 (stage 1's coefficients, data and Lemma 2.3's C(M1)); a
  proved ceiling for d (R4.3's six items, first E^flat's actual log orders); lower bounds for lambda1, delta (the seven
  inverse bounds in the write-out's norms, the Lipschitz moduli, ||Pi||, the B-row constants and d).

### R4.6 Proposed text for the paper's section 9 (replaces R3.6; the reader's proposal folded in)

    The threshold lambda0 that the proof of Theorem 1 delivers is traced term by term to the supplement. At the
    numerical point (l5 = 1/10, mu0 = 1, A = 1, T = 1, tau0 = -2, a = q0/2, a smooth envelope with the numerics'
    integral) it is below 0.0025 (certified): the energy estimate needs the pointwise bound eps1 below g0's least
    absolute eigenvalue on the domain, 0.0308, its value at r = a once the hole has grown, and C_app is at least 12.59
    with the pointwise norm read as the operator norm, as the supplement now states. So the wavelength 10 l5 lies more
    than 400 times beyond it. A value would need certified solves of the approximant's nine linear stages; none is done,
    and the first needs lower-order coefficients the record does not extract and the energy constant at that eps1.

    The loss d is not a number. On the construction reading of E_ind, at a parameter point meeting every condition
    decidable there, d >= 8.40 x 10^15 and N >= 1.76 x 10^17 (computed). The poles of the iota+-normal operator's
    inverse below real part 5 are all simple in the class (computed, exactly, through the Mellin transform), but the
    index sets E_ind carry logarithms up to order 10 at real part 5, so at that point the write-out's bookkeeping gives
    no ceiling below 3.29 x 10^31. The size comes from one count, bounded through the log-order ceiling of the parameter
    exponents; with at most two logarithms at each exponent the same accounting would give 3.8 x 10^16. A proved
    ceiling needs the log orders actually produced, then L_0, X_7 and II.E's tame orders.

    For what this proof's formulas can deliver (upper-bound constants at least 1), log10 delta < -7.66 x 10^16 and
    lambda1 < delta. No lower bound follows from this proof, whose arguments at six injectivity steps and one trapping
    estimate give no number: seven certified inverse bounds in the write-out's norms, with the Lipschitz moduli, the
    calculus constants and d, would have to be computed instead. The cheapest, at zero energy, is explicit harmonic by
    harmonic for the scalar model at the final black hole, but not yet in the write-out's norm.

### R4.7 Sources (round 4)

N1STAR-PROOF.md:87-92, 101-126, 152-186, 222-233, 355-408, 521-539, 548, 699-802 (D614 numbering); proof5:
PART-III-G2-IOTA.md:17-60, 205-240, 421-470; PART-III-G-SPECTRAL.md:60-135, 299-330, 890-930; PART-III-I11-SPACETIME.md:
60-110, 330-345; PART-III-I12-SPECTRAL.md:236-256, 380-402; PART-III-A-PREREQ.md:176-182, 658; PART-III-F4-ZERO.md:
20-35, 60-84; PART-III-D3-SYMSTATES.md:36-48; PART-III-D4-GENSTATES.md:50-60, 109-130; PART-III-I5-UNBOOST.md:185-195;
PART-III-I8-UNPARAM.md:30-42; PART-III-I10-CORR4.md:33-44; PART-III-G3-GRAFT.md:363-388; PART-I-C-LOWENERGY.md:372-400,
488-500; PART-II-F-IOTA.md:1378-1400; PART-I-B-HIGHENERGY.md:1500-1520; N1STAR-PROOF.md 10.37 (iota5.py); lin5.py E2;
damping5.py U3-U4; gaugepot5.py G1; class5.py C2; LOSS-D.md LD14; E2-PILOT.md sections 1, 4; the reader's report
(round 3) and its scripts.


## Round 5

*Status (2026-11-02).* Appended to rounds 1-4; not yet read by a verifier. Part A reads round 4 as an independent
verifier would; its findings are seated here (R5.1) and, where they correct a line of round 4, by a bracketed
`[Round 5, ...]` note after that line, the old figure kept. Part B pushes on the open items in the order asked
(R5.2-R5.6). New programs, each with its `.out` and controls that mutate the computed path and fail as they must:
`checks/lzerorank5.py`, `checks/iotamut5.py`, `checks/eflat5.py`, `checks/stage1rate5.py`, `checks/zerohardy5.py`. No
earlier program is changed.

### R5.0 Summary

- **(i) lambda0.** Round 4's lambda0 < 0.0024433 stands (certified), with one argument repaired: for the Frobenius
  reading the sentence "every reading's ball contains the operator-norm ball" is false, and the bound is now carried by
  an explicit rank-one perturbation whose operator and Frobenius sizes are equal (`lzerorank5.py` R1). The same
  perturbation gives the largest-entry reading **lambda0 < 0.0012968** (certified, R2). Stage 1 does not close: its
  coefficients are extracted (`bbar5.py`, D569, which round 4 missed), Lemma 2.3 at g0 is now explicit (certified:
  rate kappa <= 13.2197, factor e^39.244 = 1.105e17, `stage1rate5.py`), and what is missing is the stage data.
- **(ii) d. Settled the second way: the log orders are <= 2.** [Round 6, R6.0 M2: "settled" withdrawn, a deduced
  reading of I11:352-387; the write-out states K(lambda).] Followed step by step, the construction of
  III.I'''''''''' Proposition 3.1 writes E^flat with log order <= 2 at every exponent below 3 + eps_+ except at the 26
  points of pi_1 E^C_I in [2, 3], where it is <= 5 (R0) or <= 11 (R1) (deduced from the cited steps; the table
  computed, `eflat5.py` F4). So n_iota <= 3 P_iota + 23 (R0) or + 44 (R1), and **d <= 37,919,139,491,675,142 +
  53,244,736 X_7 + 106,489,470 c'** (3.7919e16; N <= 7.9630e17 + ...), 4.51 times the floor. The record's K(lambda),
  which allows a raise in every window, is not what the construction produces. X_7 reduces to the K+-exponents of Step 5
  (R5.3); c' is immaterial at this size unless it exceeds about 1e7 (R5.4). L_0 is in [2, 7] (R5.3).
- **(iii) lambda1, delta.** The scalar zero-energy bound now holds at every l >= 0 with the sharp constant 1/(l + 1)^2,
  l = 0 included, and crosses the horizon without loss (`zerohardy5.py`); in the class the zero-energy kernel the bound
  must avoid is one direction (s0). Still not in the norm of (3.2), and not for L_b0's fifteen components.
  [Round 6: R1's figure is 37,919,139,651,409,350 (R6.0 M1); "without loss" overreached: u' is bounded across the
  horizon by sup |A_l u| and, for l >= 1, sup |u| (R6.0 minor 5). The bound is now in (3.2)'s norm at s = 1 (R6.3).]

### R5.1 Round 4 read adversarially

(a) *lambda0, T7* (checked). The infimum is over all of Omega: g0's least absolute eigenvalue is s - m, s = (m^2 +
1)^(1/2), decreasing in m (an exact identity, `lzerotrace5.py` T7), and m = mu(v)/r^2 <= mu_end/a^2 on Omega because
mu is nondecreasing (N1STAR-PROOF.md:52) and r >= a ((1.1), :157); the corner (tau_end, r = a) lies in Omega with v >
v_end. The certification is interval throughout: rational square-root enclosures on [m_lo, m_hi], m from the certified
a-interval, mu_end = 227/192 exact. **Defect (minor), R4.2 and T5's comment:** "every reading's ball |g - g0| <= eps1
contains the operator-norm ball" holds for the largest-entry norm and is false for the Frobenius norm (|A|_op <=
|A|_F, so the Frobenius ball lies inside). Fixed (`lzerorank5.py` R1, exact): the eigenvector v = (m, 1 - s, 0, 0, 0)
of the negative eigenvalue gives the perturbation (s - m) e e^T, e = v/|v|, with det(g0 + (s - m) e e^T) = 0; its
operator and Frobenius sizes are both s - m, so eps1 < 0.0307686 and lambda0 < 0.0019950 (Frobenius) hold by a valid
argument. **Sharpening** (R2, certified): e e^T's largest entry is e_tau^2 = f(m) = m^2/(m^2 + (s - 1)^2) for every
direction xhat (e_tau^2 > e_x^2 iff m > 0), f decreasing, f(m*) <= 0.5307395; so the largest-entry reading has eps1 <
0.0163302 and **lambda0 < 0.0012968** (round 4's 0.0024433 there is valid, not sharp). Controls: the positive
eigenvector does not degenerate (C1); at the outer corner the bound is 0.9934 (C2).
[Round 6, R6.0 minor 2: t (e_tau - e_1)(e_tau - e_1)^T gives det(g0 + t v v^T) = 4 m t - 1 exactly, every entry t, so
the largest-entry eps1 < 1/(4 m*) <= 0.0153989 and lambda0 < 0.0012228 (`r6fixes5.py` F1); not claimed sharp.]

(b) *iotapoles5.py.* The recursion (zeta - lam) L1(zeta) h-hat(zeta) + N(zeta - 1) h-hat(zeta - 1) = F-hat(zeta) and the
product Pi_j = -((j - 1)!)^-1 L1(lam)^-1 N(lam - 1) ... L1(lam - j + 1)^-1 N(lam - j) re-derived (deduced:
h-hat(lam - i) = i^-1 L1(lam - i)^-1 N(lam - i - 1) h-hat(lam - i - 1), the factors 1/i multiplying to 1/(j - 1)!); step
(d)'s descent checked: h-hat/(zeta - lam + 1) satisfies the recursion with lam - 1 (deduced, one line). Findings, all
minor, each now computed (`iotamut5.py`):
- M3 *assigned* the order (1, 1) to every candidate with one singular factor (iotapoles5.py:233-234); its assertion
  cannot fail there. U2 computes the premises exactly instead: at each of the seven singleton candidates (s0: 2.0000747,
  3.0000747, 4.0000747, 3, 4, 4.0000013; t2: 5) the root is simple, Res_x(p(x), det N(x + i - i')) != 0 for every other
  factor, and Res_x(p(x), det(C - (x + i - i' + 1))) != 0 for every L1 factor; so the order is exactly 1 (deduced: a
  nullity-1 inverse between invertible factors).
- C4 cannot fail on its own: det N(2 + eps) has a simple zero, so adj N(2 + eps) = det N(2 + eps) N(2 + eps)^-1 and
  the control's (0, 2) is (order - 1, rank) of M3's answer, whatever that answer is (checked, C4dep). Replaced by U3, an
  independent route: Pi_4(5 + eps)^-1 in mpmath at 60 digits for eps = 1e-10, 1e-20, 1e-30 scales with slope -1.000000
  and eps Pi^-1 has singular values 47.98, 0.1674, 6.6e-26, 2.3e-27: order 1, residue rank 2 (computed).
- Mutations of the computed path, each changing the answer as it must (2233 s): X1 the Mellin shift N(lam0 + eps - i +
  1) in the product at 5 gives (order, rank) = (2, 1), not (1, 2); beside it, the true product with the L1 factors
  dropped also gives (2, 1), so the order 1 at 5 rests on the L1 factors; X2 a planted double root ((x - 4) on N's last
  row): root 4 of multiplicity 2, the simplicity test fails; X3 laurent_order returns (2, 1), (1, 2), (2, 1) on
  matrices of known structure, and a mutated routine returns (1, 1) on the last; X4 Lemma 1.4 with the inner extended
  union made plain: E_ind's log order at 5 is 5, not 10.
- R4.3 (b) says the K solutions with Re <= 0 "decay"; at s0 one of those roots is 0 (v^0, bounded). The strip S =
  {0 < Re zeta < 3/2} is unaffected (convergence at infinity needs Re zeta > 0 only). Wording.
- Not checked by round 4 and still not: that exactly K roots of det N_L have Re <= 0 at s_l, l >= 2 (M4 covers
  simplicity, integer differences and exceptional points there, not the count). V(lam)'s dimension at those types rests
  on lin5.py's factorisation (READ).

(c) *The E_ind reading* (R4.3; I5:190, I8:35, I10:38-40, D4:54-59 read). The lines fix E_ind once, at b0, as the
index sets of III.D'' Proposition 3.1 and III.F''' Proposition 2.2 (enlarged by III.D''' Proposition 3.1's and (2, 0)),
and D4:57-59 puts every exponent in M: a reading of what the construction yields, as round 4 says. **Defect (major for
the reading, not for the number):** M5 ran Lemma 1.4 with E(alpha) from *every* type's roots (the census), and on that
root set E_ind at k = 2 contains (d0, 0) as well as (d1, 0) (`eflat5.py` F1, C3): the widest reading of R3.3 D3, under
which (G) binds and the floor rises to about 3e20, not the construction's {d1}. The reading round 4 names is the
*block* reading: at b0 the indicial family preserves types (D4:84) and each source has one type (F4 Lemma 1.1: s0 for
mu-dot, v1 for A-dot; D3 (3.4): s1, v1), so Lemma 1.4 may be run on the source's type alone (deduced). Computed on it
(F1): s0 with F = (1, 0) gives E_ind log orders 1, 3, 5, 7, 9 at offsets 1..5; v1 with (2, 0) gives 2, 4, 6, 8, 10; s1
with (2, 0) gives 1, 3, 5, 7, 9; s1 with (1, 0) gives 1, 2, 4, 6, 8; the offsets below 1 are {d1} only (d0 enters as 1 +
d0, the s0 site having k = 1: LD9's open point "whether d0 is in E_ind" answered on this reading); and the largest log
order at real part <= 5 is **10, at 5, from v1**: round 4's l_* >= 10 stands, on the reading it names.

(d) *The ceiling and 3.7919e16* (checked). iotapoles5 M6 rebuilds A = 28,864,786,304,360,710 from R2, R3, P_W, P_iota,
W and the level counts and evaluates A + B L_0 + C (l_* + 1) at L_0 = 1, l_* = 10: 3.285478e31 (reproduced); the
hypothetical is A + L_above 2 P_iota = 37,919,137,148,906,758 (2 x 4,527,175,422,273,024 added; reproduced). The
forms are right; R5.2 changes which of the two the construction supports.

(e) *zeroinv5.py.* 1/(l (l + 2)) <= 1/8 on even l >= 2 is right (it holds for every l >= 1). The label "certified" is
too strong: the identity is exact, the inequality is deduced (boundary terms, Cauchy-Schwarz). Superseded by R5.6's
1/(l + 1)^2, which is sharp and includes l = 0.

(f) *Controls that cannot fail.* iotapoles5 C4 and M3's singleton assertion (above), both now replaced (U2, U3, X1).
The other round-4 controls mutate their paths.

(g) *R4.2's stage-1 obstruction* (defect). "Its lower-order coefficients B-bar, C-bar are not extracted by any
instrument" is wrong: `checks/bbar5.py` (D569) computes them, B-bar = B0 from g0 alone (K1), C-bar = C0 + Delta C,
Delta C the W_TT^2 means of order r^-3, chi contributing none (K2-K3). And "a certified a priori bound needs Lemma 2.3's
constant C(M1) at gt within 0.0307686 of g0" does not apply to stage 1: Lemma 5.3 (a)'s operator is box~ = g0^{ab} d_a
d_b, so stage 1 needs Lemma 2.3 at gt = g0 itself, which R5.5 writes out.

### R5.2 (ii) E^flat's log orders, and Lemma 1.4 at the other sites (B1; `eflat5.py`)

- *The steps* (deduced; READ I11:352-387, I2:165-177, G3:363-400). Step 2 treats the u-exponents below 2 in increasing
  order, window by window (I11:367-369). Below 2 every exponent has log order 0: they are the chain of lambda_sharp under
  the offsets of E^iota_ind cup E_ind below 2 - lambda_sharp = 0.4901, which are {d1} with log order 0 (F1-F3; "with the
  log orders of E_++", I11:384-386), and Corollary 4.3 adds the pole order l_0 = 0 there (spec_iota+ in Re >= 2,
  I11:373-374). A window lambda_0 writes exponents lambda_0 + w, w in E^iota_ind, with log order l(w) ((4.5), G3:375),
  and runs III.I' Proposition 3.1 on its own error, which by (3.2) raises log orders only at points of pi_1 E^C_I, of
  real part >= 5/2 (I11:382-384). Step 1 writes G = (2, 0) U (2 + E_ind) and (3.2)'s raises at pi_1 E^C_I; f_2 writes
  E^0_src + 2 (G's points below 3 + eps_+). A window's output joins the source and is not passed through a later
  window's III.I' step, so at an exponent of real part >= 2 the log order is the largest over the windows, not their
  sum: the (N_* + 1) factor of K(lambda) is the record's allowance, not something the construction does.
- *The inputs* (computed, F1-F2). E^iota_ind's offsets in (0, 3 + eps_+ - lambda_sharp] = (0, 1.4901]: d1 (log 0), 1
  (2, from v1), 1 + d1 (1), 1 + delta'_1 (0), 1 + d0 (0); the III.D''' towers add offset 1 with log order 0 (for each of
  the 14 class roots mu of D4 (R4), mu + 1 is not a root of its type); G on the window: (2, 0), (2 + d1, 0), (3, 2).
  On the literal reading (every type's roots) the largest log order at these offsets is also 2 (F1): there Lambda
  grows (d0 an increment), the log orders do not.
- *The result* (deduced; computed table, F4). E^flat has log order <= 2 at every exponent below 3 + eps_+ except at the
  26 points of pi_1 E^C_I in [2, 3]: on R0 at most 5 at 3, 4 at 2.5, 2.5099, 2.51, 2.52 and 3 at twelve points in
  (2.5, 2.56]; on R1 at most 11 at 3, 7 at the four, 5 at 2 and 3 at the twelve. Excess over 2: 23 (R0), 44 (R1).
  [Round 6, R6.0 M1: on R1 the raise at 2 (to 5) completes to (3, 5) before the round at 3, which gives 5 + 8 + 1 = 14
  there, not 11; excess 47; log order above 2 at 17 points (R0), 18 (R1), not 26 (`eflat5.py` f4_table, C4).]
- *The ceiling* (computed, F5). n_iota <= 3 P_iota + excess, so dceiling5's D6 per exponent gives
  **d <= 37,919,138,373,535,686 (R0), 37,919,139,491,675,142 (R1) + 53,244,736 X_7 + 106,489,470 c'**, N = 21 d + 6
  <= 7.96302e17 + .... The floor is 8,407,505,890,317,054: the ceiling is 4.51 times it. It is a ceiling on the
  record's bookkeeping with the construction's own log orders; it is not proved in the record's words (I11 Proposition
  3.1 (c) states K(lambda)), so it is a deduced ceiling resting on the reading above.
  [Round 6, R6.0 M1: R1's constant is 37,919,139,651,409,350 (+159,734,208); R0's stands. With X_7 summed exactly
  (R6.1): d <= 45,661,383,902,649,727 + 106,489,470 c' (R1).]
- *Controls* (each fails): C1 the windows' raises summed instead of maximised: log order 45,000,050 at 3; C2 the v1
  site's extended unions counted twice: log order 4 at offset 1; C3 every type's roots at k = 2: offsets below 1 {d0,
  d1}.
- *The other E_ind / E^iota_ind sites* (computed at four, read at two). Lemma 1.4 at the four box^Ups sites: R5.1 (c).
  The III.D''' towers' Lemma 1.4 part starts at offset 2 + d1 - m >= 2, and III.F''''s state (5.3) (F5:301-318) uses
  Lemma 1.4 with L-hat_b(0)'s roots above alpha - eps ~ 0 and Lemma 1.5's "(0, k) for some k" at offset 2: both live at
  offsets >= 2, so they bear on l_* (Re <= 5) and not on E^flat's window; their log orders are not computed here (the k
  of (5.3) is the pole order of N(L-hat_b(0), .)^-1 at 0, which l_*'s multiplicity item already bounds).

### R5.3 (ii) L_0 and X_7 (B2; `eflat5.py` F6-F7)

- *L_0* (computed on one reading). L_0 bounds the log orders of E^0_src U E_++ U G U (2 + E_col) below 2 lambda_sharp =
  3.0198 (I11:76-78). G has 2 at 3; E^0_src's part below 3.0198 is G's and the rows' (0 below 2); E_++ there is
  lambda_sharp + w, w in E^iota_ind cup E_ind (log <= 2): so **L_0 >= 2**. E_col (I12:93-104) comes from the classes
  (2, 0) U (2 + E_ind) (mu-dot: s0, k = 1) and (3, 0) U (3 + E_ind) (A-dot, h(S)) shifted by q - 4 + k - m; on round 2's
  reading that the shift is >= -5 (R2.3 (b)), 2 + E_col below 3.0198 reaches the s0 site's offset 4, log order 7:
  **L_0 <= 7** on that reading. L_0 enters the record's form with 4.53e15, so that form stays 3.2855e31 at L_0 = 7.
- *X_7* (deduced; READ A-PREREQ:650-704, I12:389-407). III.A Proposition 4.2 (2)'s loss is (2.26a)'s loss twice plus
  |E_iota,<=| (the factors of R_tf) and |E_K,<=| (those of R_zf). At Step 7 the iota+ weight is beta'_+ in (3/2 -
  (delta_sharp - eps_+), 3/2) (I12:407), below every iota+ exponent (>= lambda_sharp = 1.5099), so **|E_iota,<=| = 0**
  and X_7 = |E_K,<=| + (2.26a)'s losses, E_K the K+-exponents of Step 5 (III.G'''' Proposition 4.4's zf-terms and the
  zero-energy pieces) below alpha - 2 - eps <= 2 + eps_K. They are not computed: X_7 is the one count left open in the
  ceiling, and whether it is of the size of P_iota (an exponent lambda - 1 for each lambda of Lambda in [2, 3 + eps_K]
  would make it so) or small is what Step 5's K+-index sets decide.

### R5.4 (ii) II.E's tame orders in c' (B3; READ, counted)

II.F2-TAME:528-535 defines D_0 = max(d^E_0, d^S_0, d^T_0, d^U_0), D_1 = max(d^E, d^S, d-tilde) and FWD's loss d = D_0
+ D_1 + d' + d'' with d' = max(0, ceil(-inf s)), d'' = max(0, ceil(sup s)) (III.I Theorem 5.3 adds 6). Read at
source: the energy lemmas print d_0 = 2 (II.E:303, 342, 411, 424); Propositions 3.4, 4.3 and Theorem 6.1 say "d_0
depends only on s" (II.E:650, 812, 1155), which traces to II.A Lemma 8.5's d_0 (II.A:938-944, "there are d_0 in N"),
not numbered; II.E Proposition 4.4's tame order is d = d-tilde + 3 (II.E:853), with d-tilde from II.A Proposition 9.6,
which is explicit: **d-tilde = s-bar + 2 max(s-underline, s-underline_0) + 6** (II.A:1324-1325; s-bar = max(0, ceil sup
s), s-underline = max(0, ceil(-inf s))). So D_1 is explicit in the orders, D_0 is II.A Lemma 8.5's one unnumbered
multiplier order (>= 2), and c' >= D_0 + D_1 + d' + d'' + 6 + 2 (BG) (deduced). The orders s at the record's point are
not read here. **c' does not matter at this size** unless it exceeds about 1e7: c' = 1000 adds 1.06e11 to 3.79e16
(106,489,470 x 1000).

### R5.5 (i) Stage 1 (B4; `stage1rate5.py`)

- *The coefficients* (READ `bbar5.py` K0-K4, D569): B-bar = B0, the first-order part of the linearisation of Ric^H at
  g0, built from g0 alone; C-bar = C0 + Delta C, Delta C quadratic in W_TT with frame order r^-3. They are computed
  there symbolically; their certified sup norms on Omega are not taken here.
- *Lemma 2.3 at g0, written out* (certified, K1-K3). At xhat = e1, Y = -g0^-1 dtau = (1 + m, -m xhat), r pi = (2 m^2 -
  k, 2 m + 2 m^2 - k, 4 m + 2 m^2 - k; angular -2 m), k = mu'/r, r Gamma = (m, -m, 0, 0, 0) (exact). With E(tau) = int
  T(Y, Y) dx: dE/dtau <= kappa E + c_Y E^(1/2) ||box~ u||, **kappa <= 13.2197** on Omega at P* (attained at r = a),
  c_Y^2 = 2 exactly, T(Y, Y)'s form between 0.196683 and 280.545 times |du|^2 (q <= 1426.38). So for -(1/2) box~ u = f
  on Omega: **||du(tau)|| <= 4.174e18 ||du(tau0)|| + 7.048e17 int ||f||**, the Gronwall factor e^(kappa Dtau/2) <=
  e^39.244 = 1.105e17 (Dtau <= 5.937209). B-bar and C-bar add their sup norms (over q_lo^(1/2)) to kappa. Controls: the
  Gamma term removed changes kappa (C1); Y = d_tau is not coercive at m = 2 (C2).
  [Round 6, R6.0 minor 3: the coefficient of int ||f|| is c_Y q_lo^(-1/2) e^(kappa Dtau/2) < 3.525e17, not 7.048e17
  (y' <= (kappa/2) y + c_Y ||f|| from box~ u = -2 f; `r6fixes5.py` F2); and C-bar's sup norm enters only with ||u||
  inside the energy (Lemma 2.3's <u, d_tau u> step), not through du alone.]
- *Why stage 1 does not close* (deduced). With the energy constant explicit, a certified L^2 bound for (m_1, phi_1,
  Psi_1, Z) needs (1) the stage data (m_1, d_tau m_1, phi_1, gh_2) on Sigma_tau0, fixed by Lemma 6.2 through Lemma
  6.4's parabolic-hyperbolic constraint solve, whose constant is not written out (N1STAR-PROOF.md:631-755); (2) the
  coupling bounds (B-bar and C-bar sup norms; Mm of Lemma 5.2; the source S, certified <= 3.32e3 at order 0,
  stage0bd5); (3) for C_app in sup norm, the same commuted to order >= 3. (1) is the obstruction: no instrument solves
  Lemma 6.4. *What it would imply for lambda0*: a stage-1 bound bounds C_app's g1 part from above, which bounds no term
  of the minimum from below without the other eight; it lowers the upper bound only if sup |m_1 + W| exceeds sup |W_TT|
  (12.59).

### R5.6 (iii) The zero-energy bound (B5; `zerohardy5.py`)

- *Every l, sharp* (exact identities; deduced inequality). w = 1/r satisfies -(r^3 f w')' = (1 + mu r^-2) r w exactly
  (H1); the ground-state identity (H2) gives int r^3 f |u'|^2 >= int (1 + mu r^-2) r |u|^2 for u = o(r^-1), hence
  <A_l u, u> >= (l + 1)^2 ||r^-1 u||^2 and **||r^-1 u|| <= ||r A_l u||/(l + 1)^2 for every l >= 0**: constant 1 at l =
  0 (the harmonic round 4 left open), 1/9 at l = 2 (round 4: 1/8). Sharp: for u = r^(-1-delta) the quotient is exactly
  (l + 1)^2 + delta (H3). Control C2 refutes the constant raised by 1/10.
- *Across the horizon* (exact; deduced). r^3 f = r (r - r_h)(r + r_h), so for u smooth across r_h, r^3 f u' =
  int_{r_h}^r s^3 (l (l + 2) s^-2 u - A_l u) ds and |u'| <= sup |s^3 (l (l + 2) s^-2 u - A_l u)| / (r (r + r_h)) on both
  sides (H4): at zero energy the scalar model loses no derivative at the horizon (factor 1/(2 mu) there), so the
  radial-point constant is not needed at sigma = 0 for this model.
  [Round 6, R6.0 minor 5: overreached; u' is bounded there by sup |A_l u| and, for l >= 1, sup |u| (A_l u in C^k gives
  u in C^(k+1)); the L^2-level passage through the horizon is R6.3's multiplier identity. Minor 6: the inverse bound is
  sharp too, ||r A_l u||^2/||r^-1 u||^2 -> (l + 1)^4 on r^(-1-delta) (`zerohardy5.py` H3b).]
- *The kernel in the class* (READ N1STAR-PROOF.md:4983-4984; deduced, H5): L_b0's eleven zero-energy states are 1 (s0,
  mu-dot) + 6 (v1, so(4)) + 4 (s1, h_s1(S)); the class has even scalar harmonics and no vector type, so I.C:497's
  sigma_min is needed on the complement of one direction, in s0, and on s_l, t_l (l even >= 2) without a kernel.
- *Where it stops.* The bound is in L^2(r^3 dr) with weights r^-1, r on the exterior, plus an L^oo bound for u' at the
  horizon; (3.2)'s H-bar^(s, alpha)_b with s > 1/2 + theta_H and its b-weights at infinity is not reached, and L_b0 is
  a coupled system per type, for which no ground state is constructed here.

### R5.7 Proved, computed, open

- *Certified*: lambda0 < 0.0024433 (operator), < 0.0019950 (Frobenius, now by a rank-one perturbation), < 0.0012968
  (largest entry); Lemma 2.3 at g0 on Omega: kappa <= 13.2197, ||du(tau)|| <= 4.174e18 ||du(tau0)|| + 7.048e17 int
  ||f||.
- *Computed, exact*: E_ind's Lemma 1.4 log orders at four sites on the block reading (offsets below 1 {d1}, 10 at 5);
  the singleton pole orders' premises, and order 1, rank 2 at 5 by an independent route; E^flat's log-order table and
  the ceiling 3.7919e16 + 53,244,736 X_7 + 106,489,470 c'; the zero-energy constants 1/(l + 1)^2, sharp.
  [Round 6, R6.0 M2: E^flat's table and the ceiling move to *Deduced* (a reading of I11:352-387); M1: R1 47, 14 at 3.]
- *Deduced*: the block reading; E^flat's log orders from the construction's steps; X_7 = |E_K,<=| + (2.26a)'s losses;
  the tame orders' structure; stage 1 needs Lemma 2.3 at g0 only; the kernel in the class is one direction.
- *Open, with the exact obstruction*: lambda0's value (stage 1's data, Lemma 6.4); d's ceiling: X_7's E_K (Step 5's
  K+-exponents), and acceptance of R5.2's reading in place of I11 Proposition 3.1 (c)'s K(lambda); l_*'s remaining
  sites (III.F'''' (5.3), III.D''' Lemma 1.4 parts), which no longer enter the ceiling; lambda1 and delta: the seven
  inverse bounds in (3.2)'s norms (the scalar zero-energy one now explicit at every l in an exterior norm), the
  Lipschitz moduli, ||Pi||, the B-row constants.

### R5.8 Proposed text for the paper's section 9 (replaces R4.6)

    The threshold lambda0 that the proof of Theorem 1 delivers is traced term by term to the supplement. At the
    numerical point (l5 = 1/10, mu0 = 1, A = 1, T = 1, tau0 = -2, a = q0/2, a smooth envelope with the numerics'
    integral) it is below 0.0025 (certified): the energy estimate needs the pointwise bound eps1 below g0's least
    absolute eigenvalue on the domain, 0.0308, attained at r = a once the hole has grown, and C_app is at least 12.59
    with the pointwise norm read as the operator norm, as the supplement states. So the wavelength 10 l5 lies more than
    400 times beyond it. A value would need certified solves of the approximant's nine linear stages. For the first,
    the coefficients are computed and the energy constant at the background is explicit (a factor of about 10^17 over
    the domain); what is missing is the stage data, which come from solving the constraints.

    The loss d is not yet a number. At a parameter point meeting every condition decidable there, d >= 8.40 x 10^15
    and N >= 1.76 x 10^17 (computed). Followed step by step, the construction keeps at most two logarithms at every
    parameter exponent but 26, so the write-out's own bookkeeping gives d <= 3.80 x 10^16, plus 5.3 x 10^7 times one
    [Round 6: superseded by R6.6; "but 26" is "but 18 (R1)", and the figure is a deduced ceiling on a reading]
    uncounted loss, that of the inverse Fourier transform at the final joint step, which depends on the K+-exponents of
    the zero-frequency terms, and 1.1 x 10^8 times the fixed per-level loss, which matters only if it exceeds about
    10^7 (deduced; the record's own coarser bound, which allows a logarithm at every step of every window, gives
    3.3 x 10^31).

    For what this proof's formulas can deliver (upper-bound constants at least 1), log10 delta < -7.66 x 10^16 and
    lambda1 < delta. No lower bound follows from this proof, whose arguments at six injectivity steps and one trapping
    estimate give no number: seven certified inverse bounds in the write-out's norms, with the Lipschitz moduli, the
    calculus constants and d, would have to be computed instead. The cheapest, at zero energy, is explicit for the
    scalar model at the final black hole, harmonic by harmonic with the sharp constant 1/(l + 1)^2 and without loss at
    the horizon, but not yet in the write-out's norm or for the full linearised operator.

### R5.9 Sources (round 5)

N1STAR-PROOF.md:52, 87-92, 152-160, 211-233, 521-548, 631-755, 4983-4990; proof5: PART-III-I11-SPACETIME.md:66-80,
330-392; PART-III-I2-SCRI.md:165-200; PART-III-G3-GRAFT.md:280-400; PART-III-A-PREREQ.md:150-200, 563-704;
PART-III-F4-ZERO.md:20-80; PART-III-D3-SYMSTATES.md:36-48, 135-215; PART-III-D4-GENSTATES.md:50-135;
PART-III-F5-PAIRINGS.md:290-320; PART-III-I5-UNBOOST.md:185-195; PART-III-I8-UNPARAM.md:30-42;
PART-III-I10-CORR4.md:33-44; PART-III-I12-SPECTRAL.md:76-108, 380-407; PART-II-F2-TAME.md:468-545;
PART-II-E-ENERGY.md:300-430, 648-660, 727-745, 842-856, 1148-1170; PART-II-A-SETUP.md:938-944, 1314-1330; LOSS-D.md
LD9, LD14; checks: bbar5.py and its .out (D569), iotapoles5.py, lzerotrace5.py, dceiling5.py, dweights5.py (imported,
not copied).

## Round 6 (2026-11-02)

*Status.* Appended to rounds 1-5; not yet read by a verifier. R6.0 seats the round-5 verifier's report, each item
re-derived first; where it corrects a line of rounds 4-5 a bracketed `[Round 6, ...]` note follows that line, the old
figure kept. R6.1-R6.3 take the three items in the order asked. New programs, each with its `.out` and controls that
mutate the computed path and fail as they must: `checks/dnumber5.py`, `checks/r6fixes5.py`, `checks/zeroext5.py`,
`checks/stage1cap5.py`. Changed and rerun: `eflat5.py` (F4 as a function with the completion of (3.2), C1 rerun through
it, C4 new, F5's assert), `zerohardy5.py` (H3b, H4b, C3 replaced, H5's READ found by search). Found here: N1STAR-PROOF.md
has moved since D614 (D615 rewrote Lemma 6.2's proof; 10856 lines, the eleven states now at :4986), so
`lzerotrace5.py` T0 fails its md5 pin on a rerun (checked; `lzeroaudit5.py` pins the same md5); rows below :634 move
by +3 (not re-pinned here: the file was still changing while this round ran).

### R6.0 (verifier of round 5)

The verifier confirmed every certified figure of round 5, the byte-identical reruns, the ceiling arithmetic, its own
interval lambda0 (operator < 0.00244325, Frobenius < 0.00199491, largest entry < 0.00129673), and the windows'
"maximised, not summed" rule. Its findings, each re-derived before it is seated:

- **M1 (accepted; computed).** III.I' (3.2) takes extended unions round by round, and each completes the index set by
  (2.2) (A-PREREQ:122-130). On R1 the round at [2, 3) raises 2 to 0 + 4 + 1 = 5, the completion puts (3, 5), and the
  round at [3, 4) raises 3 to 5 + 8 + 1 = 14, not 11; on R0 the completion (3, 1) lies below G's (3, 2). `eflat5.py`
  f4_table now runs the rounds with the completion; C4 reruns it without and recovers round 5's 44 and 11. R1's excess
  is **47**, the constant **37,919,139,651,409,350** (+159,734,208, the verifier's figure); R0's 23 and
  37,919,138,373,535,686 stand. No other completion meets a later raise: the windows raise only at real part >= 5/2
  (I11:382-386) and complete above 3 + eps_+; folded into `dnumber5.py`, whose log tables call f4_table.
  [Round 7, R7.0 m2: false -- (lambda#, 0)'s completion at 2.5099 is raised in round 1 -- and harmless: the table is
  unchanged (`r7fixes5.py` R4).]
- **M2 (accepted).** The ceiling rests on a step-by-step reading of I11:352-387, while I11 Proposition 3.1 (c) and
  Lemma 1.2 (c) state K(lambda) only: it is a *deduced ceiling on that reading*, and R5.0's "settled", R5.7's "computed"
  and R4.3's bracketed "not a hypothesis" are withdrawn in place. The log order exceeds 2 at 17 points (R0) and 18 (R1),
  not 26. On the towers: every leading exponent of D4 Proposition 3.1's towers and of D4 (R4)'s class roots is <= -1,
  so Lemma 2.1's Lemma 1.4 part sits at offsets >= 3 + d1, and at offset 1 the formal solutions meet no root of
  box^Ups(0) at z = 4e-6 (-1, -2, -3 are not s0 or s1 roots, 0 is not a v1 root; `r6fixes5.py` F3, exact); at z = 0, -1
  is an s1 root (control C3), which is where the remark holds. III.F'''' (5.3) lives at offsets >= 2 (R5.2) and does not
  touch E^flat's window. What would make the ceiling proved: the reading written into the supplement as a sharpened I11
  Proposition 3.1 (c) (log order <= 2 off the 18 points, the table at them), whose proof is I11:352-387 with the inputs
  computed in eflat5.py; it is implied by and much smaller than K(lambda). Not done here (it edits the write-out).
  [Round 7, R7.0 m1: the tower list was incomplete; offset 1 lands on a root at (s0, -1), (s1, -1), (v1, -2), each
  simple, so log order <= 1 below offset 1's 2: the table and the ceiling are unchanged (`r7fixes5.py` R3).]
- **Minor 1 (accepted).** eflat5 C1 now reruns f4_table with the windows summed and F4's test fails on it.
- **Minor 2 (accepted; computed, certified).** det(g0 + t v v^T) = 4 m t - 1 for v = e_tau - e_1 (sympy), every entry of
  t v v^T being t or 0: the largest-entry reading gives eps1 < 1/(4 m*) <= 0.0153989 and **lambda0 < 0.0012228**
  (`r6fixes5.py` F1; control: the other sign never degenerates). Valid; not claimed sharp.
- **Minor 3 (accepted; deduced, computed).** stage1rate5's 7.048e17 carries a spurious 2: y = E^(1/2) obeys y' <=
  (kappa/2) y + c_Y ||f||, so the coefficient is c_Y q_lo^(-1/2) e^(kappa Dtau/2) < 3.525e17 (`r6fixes5.py` F2). The
  remark on C-bar is seated at R5.5.
- **Minor 4 (accepted; reproduced by rerunning the verifier's script).** At 5 the order 1 is a cancellation in the
  computed operator: with L1 replaced by L1 + 10^-3 R the norm of Pi_4(5 + eps)^-1 grows like eps^-2 (1.2e18 at 1e-8,
  1.2e34 at 1e-16). R4.3's "every pole <= 5 is simple" holds for the operator computed (exact), not generically; it does
  not enter (B1).
- **Minors 5, 6 (accepted).** zerohardy5's H4 now says u' is bounded across the horizon by sup |A_l u| and, for l >= 1,
  sup |u|; H3b shows the inverse bound sharp (||r A_l u||^2/||r^-1 u||^2 = ((l + 1)^2 - delta^2)^2 + O(delta)); C3 now
  reruns H4's integrated identity (H4b, exact on a polynomial u) with the l (l + 2) term dropped, and fails.
- **Minor 7** is item 1 (R6.1). **Minor 8 (accepted).** F2's "Lemma 1.4's part starts at 2 + d1 - m >= 2 + d1" needs
  m <= 0; every m used there is <= -1 (above), so the statement holds with that range. **Minor 9 (accepted).** The
  stage-1 energy constant covers the principal part; the sup norms of B-bar, C-bar are not taken (R6.2).
- **Nits.** c' reaches 1 % of the ceiling at about 4.3e6 now (3.6e6 against 3.79e16, the verifier's figure); iotamut5's
  run was 2233 s; eflat5 C3 changes the input (kept, labelled so); R5.8 superseded by R6.6.

### R6.1 (i) d: X_7 summed over the levels, and c' (`dnumber5.py`)

- *E_K, computed exactly* (deduced from I12:328-376, Step 5 (i)-(iv), and Lemma 2.3, I12:174-216; at every level by
  I14:131). By the dictionary (I12:46-49) a zf-term |sigma|^z log^m is t^(-z-1) log^m at K+, so E_K = 1 + the
  zf-exponents of the pieces. Only Lemma 2.3's c_tau(sigma) T_tau(sigma) at levels 1 and 2 have non-integer degree:
  alpha_0 - 3 + j + i (s1) and alpha_0 - 2 - mu + j + i (other rows), alpha_0 the tf-exponent at level j, of u-exponent
  lambda = alpha_0 + j - 1; so s1 gives lambda - 1 + i and the other rows lambda - mu + i (mu <= 0), with log order
  k(lambda), plus one where alpha_0 = 2 (c_s1 = -|sigma|^-1 log|sigma|; beta_0(2) = 0). Zero-energy pieces, P_int and
  columns have integer degree and no log|sigma|. Level 1 treats lambda in [2, 2 + eta_1) = {2}; level 2 treats
  [2 + eta_1, 3 + eta_2). With beta_K = beta - 2 - eps <= 2 + eps_K - eps and (G):
      E_K cap {Re <= beta_K} = {(1, <= k_1(2) + 1)} u {(lambda - 1, <= k_2(lambda)) : lambda in Lambda cap (2, 3)}
                               u {(2, <= max(k_2(3), k_1(2)) + 1)},   cut at beta_K;
  n_iota = 0 at Step 7, and LOSS-D (2.2) (verifier 166) gives X_7(beta) = n_K(beta) + ceil(beta - 5/2). [R5.3 wrote
  "(2.26a)'s losses" twice; (2.2) charges the first application in parallel, once: at most 2 per level less.]
- *The log orders* (deduced on round 5's reading, R6.0 M2; computed tables). The level-2 sources at lambda in (2, 3]:
  E^flat (eflat5 f4_table), 2 + E_col and 3 + E_col (Lemma 1.1, E_col := E cap {Re >= 0}, E's exponents b + w + sigma,
  b in {0, 2, 3}, w in E_ind, sigma >= -5: the reading under which lambdagen5's eleven E_col bases enter P_W; log
  order 10 at 0, 12 at 1, <= 5 off the integers), u_0's (Lemma 1.4 with the one root 2, meeting the sources only at 3:
  log 26 there on R1), and Proposition 4.4's remainders (alpha_0, k) + E_ind, whose only offset below 1 is d1 with log
  order 0, so a log order is carried along its d1-chain; the offset 1 lands above 3 except from the level-1 point 2
  (k_1(2) + 2 at 3). So k_2 <= 2 + e_c on each chain c, e_c the excess of the chain's first point in (2, 3) (each excess
  source is that point: asserted). R1: k_1(2) = 10, k_2(3) = 26, E_K log order 11 at 1 and 27 at 2; chain excesses 8
  (the chain of 2), 5 (2.5, 2.5099, 2.51, 2.52), 1 (the twelve), 3, 2, 2, 1, 1 (E_col's bases 2 + d0, 2 + delta'_1,
  2 + delta_2, 2 + delta'_2, 2 + delta_3); 15 chains carry <= 2.
- *The sum* (computed, certified: per chain and level range a floor sum, evaluated at both ends of the d1 and base
  intervals and equal). Over the 53,244,736 levels above 3 (R1, the wide E_col reading):
      SUM X_7 = 7,742,244,251,240,377 = 5,794,881,998,695,725 (3 per point) + 1,947,361,533,740,659 (excess)
                + 638,936,888 (the points 1, 2) + 79,867,105 (ceil(beta - 5/2));
  X_7(alpha) = 352,162,875 at the top level; the uniform bound L_above X_7(alpha) would add 1.10e16. On the shifted
  E_col reading 6,783,838,625,545,958; on R0 (wide) 7,512,059,369,168,913. Controls: C1 a brute-force simulation of
  levels 1-2 on a scaled instance (d1 = 1/97, 90 levels) equals the closed form (37,655), and both the closed form
  without the carried excess and the simulation without propagation differ; C2 the s1 rows at rate lambda (no
  dictionary shift) collapse E_K; C3 the excess dropped from K1; C4 a perturbed d1 moves a certified chain sum.
- *d* (computed on the deduced reading). **d <= 45,661,383,902,649,727 + 106,489,470 c'** (R1; 45,431,197,742,704,599
  on R0), **N = 21 d + 6 <= 958,889,061,955,644,273 + 2,236,278,870 c'**; 5.43 times the floor 8,407,505,890,317,054.
  c' = 10 gives d <= 45,661,384,967,544,427; c' = 10^6 gives 4.5768e16; c' moves d by 1 % only above about 4.3e6.
- *c'* (READ; deduced). c' >= D_0 + D_1 + d' + d'' + 6 (III.I Theorem 5.3's FWD loss, II.F2-TAME (3.2)-(3.3)) + 2 (BG)
  + the fixed MODs of a level (among them III.A Proposition 4.2 (2) at I12:350 and in Lemma 2.4, III.I'' Lemmas
  4.1-4.2, III.H Proposition 3.2: closed forms in LOSS-D section 2b, in s_c and the thresholds), so c' >= 14 + D_0
  (D_1 >= d-tilde >= 6). D_0 = max(d^E_0, d^S_0, d^T_0, d^U_0) has no number: d^T_0 is II.A Proposition 9.6's d_0, which
  is II.A Lemma 8.5's d_* + K + 1 with d_* from the closed graph theorem (II.A:955-967); d^E_0 and d^S_0 rest on
  (L3)-(L4) and Lemma 8.6, whose d_0 the write-out fixes by d_0 - 2 >= M_2.4 + 2 (II.A2:722-723), M_2.4 again a
  closed-graph seminorm count (II.A2:277-279). The calculus it rests on gives no count either (READ [SBG]: Proposition
  3.32 cites [Hin23a] Corollary 4.34 for uniformly bounded symbols, Theorem 3.44 is "an immediate consequence", variable
  orders "mutatis mutandis", p. 66). So **d is not an integer from this record**: numbering D_0 needs a quantitative
  boundedness theorem (Calderon-Vaillancourt with a seminorm count) for variable-order symbols of finite regularity in
  [SBG]'s calculus, carried through Lemma 8.5, Proposition 2.4 and (L3)-(L4); the write-out has none, and none is
  proved here. Everything else in the chain is an integer.
  [Round 7, R7.0 m4: unsupported, withdrawn; the orders are read and D_0, D_1 bounded in R7.2, the MODs remain.]

### R6.2 (ii) stage 1 of lambda0 (`stage1cap5.py`)

- *What stage 1 can do* (computed, exact; deduced). W_TT is a first harmonic in the phase and chi a second (closed
  forms of stage0bd5.py), so for g(s) = M + W_TT(s) + chi(s) D: g(s) - g(s + pi) = 2 W_TT(s), (g(s) + g(s + pi))/2 =
  M + chi(s) D and (g(s) + g(s + pi)) - (g(s + pi/2) + g(s + 3 pi/2)) = 4 chi(s) D. Hence every admissible C_app is
  >= max(sup |W_TT|, sup |m_1 + chi dv dv|) >= max(sup |W_TT|, 2 sup |chi|), |dv dv|_op = 2.
- *Stage 0's second harmonic does not move the bound* (certified). The angular factor of chi is <= 1/3 exactly
  (36 (1 + q^2)^2/9 - 16 q^2 - (1 - q^2)^2 = 3 (1 - q^2)^2); the radial factor is largest at r = a on Omega; so
  2 sup_Omega |chi| <= 11.8821 < 12.593309 (Arb over 4000 cells of v). Control: at r = a/2, outside Omega, it is 52.4.
- *The criterion* (deduced). Stage 1 lowers the certified bound lambda0 < 0.0024433 iff a certified *lower* bound of
  sup |m_1 + chi dv dv|_op exceeds 12.593309; a stage-1 *upper* bound, which is what Lemma 6.4's estimate yields,
  cannot. With 2 sup |chi| at 11.88, an m_1 of order one at the right point would do it.
  [Round 7, R7.0 MAJOR 1: the "iff" is false in its "only if" direction; the criterion is a certified lower bound
  on sup |m_1 + W_TT + chi dv dv|_op above 12.593309, and m_1(X*) e_phi1 != 0 suffices (R7.3).]
- *Lemma 6.4's principal constants at the background on Sigma_tau0* (certified; Lemma 6.3 (a)'s closed forms, READ):
  alpha = 3 r^3/(r^2 + mu)^2 >= 0.0374252 (r = a, mu_end; 0.0512241 with mu = mu0, its value there), angular
  ellipticity and min eig S A0 >= 0.00550234 (r = b(tau0)), speed^2 <= 157.778 (r = a).
- *Why the stage-1 data are not produced, exactly* (deduced). Lemma 6.2 (iii) at m = 1 is the linearised constraint
  system P(h_1, Q_1) + B_1(h_1) = S_1 in (a_1, w_1, q_1), solved by Lemma 6.4 from zero data at r = a. Its source S_1
  and B_1 are the order-1 means of the constraint map at the approximant's slice data, products of W (and chi) with
  themselves and with gh_2 of Lemma 6.2 (i): a second-order two-scale expansion of (J, rho), one order beyond data5.py
  (which reaches the linearisation, S2-S6), and of the size of stage5.py's lam^1 Ricci expansion (966 s). Not
  computed. A certified solve then needs Lemma 6.4's constant: at the index s > 7/2 that the lemma states it contains
  the Moser and Kato-Ponce constants on S^3 ([GO13], [DS23]), not numbered in the record; an L^2-level estimate needs
  only the constants above and sup norms of the lower-order coefficients b, c, e, c', f, f', c'' at the background,
  computable but not computed. Stages 2-9 each need R^(m) to order m symbolically, which stage5.py could not reach at
  m = 2. So no stage is solved and lambda0 has no value; its certified bounds are those of R4-R6 (operator < 0.0024433,
  Frobenius < 0.0019950, largest entry < 0.0012228), unchanged by stage 1 until a lower bound on m_1 exists.
  [Round 7, R7.0 MAJOR 2: Frobenius < 0.0019079, moved by stage 0 for every m_1; "unchanged by stage 1 until a lower
  bound on m_1" holds for the operator norm only.]

### R6.3 (iii) the inverse bounds (`zeroext5.py`; `zerohardy5.py` changed)

- *The zero-energy bound in (3.2)'s norm, scalar model at b0* (computed, exact identities; certified constants;
  deduced inequalities). On harmonic l, with P = r^3 - mu r, L = l (l + 2) and the extended domain [r_h/2, oo) (the
  artificial boundary inside the horizon at which nothing is imposed), N(u)^2 = int (r |u|^2 + r^3 |u'|^2 + L r |u|^2) dr
  is ||u||^2 in Hbar^(1,-1)_b (the b-fields r d_r and the so(4) Killing fields) and F^2 = int r^5 |A_l u|^2 dr is
  ||A_l u||^2 in Hbar^(0,1)_b; alpha + 2 = 1 lies in the model's gap (0, 2) at infinity (roots -l, l + 2). The
  multiplier w = r gives, for every b > 1, the exact identity of Z1 with bulk int r^3 |u'|^2 + L int r |u|^2 and every
  boundary term non-negative, the one at the inner boundary because P < 0 inside the horizon (Z2); with the exterior
  Hardy bound (zerohardy5 H1-H2) and a choice of b in [6/5, 2]:
      ||u||_{Hbar^(1,-1)_b} <= 2.8002 ||A u||_{Hbar^(0,1)_b}   on [r_h/2, oo) x S^3, every l at once,
  sup_l C_l^2 = C_0^2 < 7.85 (exact rationals). Scale invariant in mu. The family u = r^(-1-delta) (exact) reaches
  N/F = 1.318 at delta = 1/100, l = 0, tending to 2^(1/2): the constant is within a factor 2.1 of the best. Controls: w =
  1 loses positivity at r = 1/2; the identity fails with the boundary term's sign flipped; the claim C/4 is refuted
  by r^(-1.01). At s = 1 the threshold s > 1/2 + theta_H of (3.2) holds if theta_H < 1/2 for the model (deduced: a real,
  formally symmetric scalar operator, theta_H = 0); the estimate itself gives H^1 through the horizon.
- *What remains, and why* (deduced). (a) I.C:497 itself is sigma_min of L-hat_b0(0) on fifteen components, type by type
  in the class (s0 on the complement of the one state, s_l and t_l at even l): the multiplier and Hardy arguments use
  the scalar operator's symmetric form and its ground state 1/r; for the coupled, non-self-adjoint system no such
  identity is written, so the input needed is that system's per-type ODEs (lin5.py, class5.py) with a coercive identity
  or a validated solve per harmonic and a uniform-in-l tail: computable, not done. (b) The other six (I.B:1513, :1685,
  :1978; III.F'':223; III.D:365; II.F:1393 with ||Pi||) are estimates whose constants, in the write-out, are products
  of the constants of I.A's microlocal estimates and of the finite-regularity calculus; those the write-out fixes by
  the closed graph theorem (II.A2 Proposition 2.4, II.A Lemma 8.5, (L3)-(L4)), the same input R6.1 finds missing for
  D_0, and the trapping and middle-range ones need besides certified spectral bounds in the write-out's norms (E2-PILOT
  has them only in its own norm, for the scalar wave). So no lower bound for lambda1 or delta; the upper bounds stand
  (log10 delta < -7.6666e16, lambda1 < delta).

### R6.4 Proved, computed, open

- *Certified*: lambda0 < 0.0012228 (largest entry, R6.0); 2 sup_Omega |chi| <= 11.8821; Lemma 6.4's principal
  constants on Sigma_tau0; the scalar zero-energy bound 2.8002 in (3.2)'s norm at s = 1.
  [Round 7, R7.0 m7: deduced, with certified arithmetic, for one choice of generators; not certified as a whole.]
- *Computed, exact*: the completion at 3 (14, R1 excess 47, constant 37,919,139,651,409,350); E_K below beta_K; SUM X_7
  = 7,742,244,251,240,377 and d <= 45,661,383,902,649,727 + 106,489,470 c' (on the reading); the four-point identities;
  the multiplier identity; the tower roots at -k; stage1rate5's coefficient 3.525e17.
- *Deduced*: E_K's form; X_7 = n_K + ceil(beta - 5/2) by LOSS-D (2.2); the criterion for stage 1; c' >= 14 + D_0 and
  D_0's closed-graph origin; the obstructions of R6.2 and R6.3.
- *Open, with the exact obstruction*: d as an integer (D_0: a quantitative boundedness count in [SBG]'s calculus);
  the ceiling as a theorem (the sharpened I11 Proposition 3.1 (c) written into the supplement); lambda0's value (S_1,
  B_1 and a solve of Lemma 6.4; then stages 2-9); lambda1, delta from below (L_b0's zero-energy system; the six
  others through the same calculus constants and certified spectral bounds in the write-out's norms).

### R6.5 Sources (round 6)

N1STAR-PROOF.md:355-357, 461-462, 548, 521-548, 631-805 (now +3 below :634), 4986; proof5: PART-III-I12-SPECTRAL.md:
1-420; PART-III-I14-LEVELS.md:1-213; PART-III-G5-TF.md:380-520; PART-III-A-PREREQ.md:115-135, 170-182, 455-470,
560-704; PART-III-I2-SCRI.md:160-240; PART-III-D4-GENSTATES.md:50-135; PART-III-J3-TAME.md:90-180, 240-300;
PART-II-F2-TAME.md:440-560; PART-II-E-ENERGY.md:640-660, 840-860, 1148-1172; PART-II-A-SETUP.md:340-445, 900-1010,
1110-1170, 1290-1335; PART-II-A2-STANDARD.md:170-306, 722-723; PART-I-C-LOWENERGY.md:32-100, 360-400; LOSS-D.md
sections 1-3, LD16; [SBG] arXiv:2408.06651v1 Proposition 3.32, Remark 3.33, Theorem 3.44, Remark 3.47, Definition 4.6
(READ 2026-11-02); the round-5 verifier's report and scratch (iotasub.py rerun); checks imported, not copied:
dweights5, dceiling5, eflat5, lambdagen5, prop31loss5, iotapoles5, lzerotrace5.out, envelope5.out, stage1rate5.out.

### R6.6 Proposed text for the paper's section 9 (replaces R5.8; 14 lines)

  The threshold lambda0 that the proof of Theorem 1 delivers is traced term by term to the supplement. At the numerical
  point it is below 0.0025 (certified; below 0.0013 with the pointwise norm read as the largest entry), so the wavelength
  10 l5 lies more than 400 times beyond it. The first linear stage can lower this only through a certified lower bound on
  its mean correction (stage 0's second harmonic cannot: certified); its data, which solve the constraints linearised
  about the background with the wave as source, are not computed, so no value of lambda0 is given.
  The loss d: d >= 8.40 x 10^15 at a parameter point meeting every condition decidable there (computed). Reading the
  construction's logarithms step by step (deduced) and summing every count the write-out fixes over its 1.06 x 10^8
  levels gives d <= 4.567 x 10^16 + 1.07 x 10^8 c' and N = 21 d + 6 <= 9.59 x 10^17 + 2.24 x 10^9 c' (computed), c' the
  fixed loss per level, which is at least 14 plus a coefficient-regularity order the write-out fixes only by the closed
  graph theorem: d is not an integer here, and any c' below 4 x 10^6 changes it by less than one per cent.
  For what the proof's formulas can deliver, log10 delta < -7.66 x 10^16 and lambda1 < delta; no lower bound follows. Of
  the seven inverse bounds a lower bound needs, the zero-energy one is proved for the scalar model in the supplement's
  norm (exact identities, certified constant 2.81, every harmonic, through the horizon); the others rest on calculus
  constants that the write-out also fixes only by the closed graph theorem.

## Round 7 (2026-11-06)

*Status.* Appended to rounds 1-6; not yet read by a verifier. R7.0 seats the round-6 verifier's report, each item
re-derived first; R7.1 is the re-pin; R7.2-R7.4 take the three items in the order asked; R7.A is the appendix item 1
asked for. New programs, each with its `.out` and controls that mutate the computed path and fail as they must:
`checks/r7fixes5.py` (11/11), `checks/x7indep5.py` (9/9), `checks/tensorzero5.py` (11/11), `checks/d0count5.py`
(12/12).
Changed and rerun: `lzerotrace5.py` (14/14), `lzeroaudit5.py` (7/7), `dnumber5.py` (10/10; aggregation made a
function, K4-K5 pinned; output byte-identical), `stage1cap5.py` (7/7), `zeroext5.py` (10/10), `r6fixes5.py` (6/6, F2-F3
annotated); `zerohardy5.py` rerun (10/10, now :4988). N1STAR-PROOF.md is not edited; no change to it is needed.

### R7.0 (verifier of round 6)

The verifier reran the six round-6 programs (byte-identical), reproduced every headline integer by an independent route,
and confirmed R6.0 M1, M2 and minors 2, 3, 5, 6, 8, 9, the [SBG] READ and the 2.8002 derivation (C_0 = 2.8001561 in
interval arithmetic). Its findings, each re-derived before it is seated:

- **MAJOR 1 (accepted; computed, `r7fixes5.py` R1; found independently here before the report arrived).** The stage-1
  [Round 8, R8.0 (n1): "found independently here before the report arrived" cannot be checked from the record;
  withdrawn as a claim.]
  "iff" (R6.2, R6.4, stage1cap5 S3) is false in its "only if" direction. At X* := (theta = 0, v = 2, r = a), tau =
  2 - a, in the frame (tau, x1, ..., x4) with xhat = e1, W_TT(s) = K cos s diag(0, 0, 4/3, -2/3, -2/3) and D = U U^T,
  U = (1, 1, 0, 0, 0) (exact); for every symmetric M, e2^T (M + W(s) + chi D) e2 = M_22 + (4/3) K cos s, so sup_s
  |M + W + chi D|_op >= (4/3) K + |M_22|, and a coupling w (e2 e3^T + e3 e2^T) raises the top eigenvalue to K/3 +
  (K^2 + w^2)^(1/2) > (4/3) K. So any certified nonzero m_1(X*) e_phi1 lowers lambda0, whatever sup |m_1 + chi dv dv|
  is; R6.2's "an m_1 of order one" overstated what is needed. The criterion is now: stage 1 lowers the operator-norm
  bound iff a certified lower bound on sup_{Omega x S^1} |m_1 + W_TT + chi dv dv|_op exceeds 12.593309; the four-point
  bound is sufficient only. The reason stage 0 cannot move it is the block structure, now computed: W_TT U = 0, so
  |W_TT + chi D|_op = max(|W_TT|_op, 2 |chi|) pointwise, and 2 sup |chi| <= 11.8821. stage1cap5 S3 corrected.
  [Round 8, R8.0 (1): r7fixes5 R1 certifies the excess K/3 + (K^2 + w^2)^(1/2) - (4/3) K only for M = w (e2 e3^T +
  e3 e2^T). In the class no other M occurs at X*: m_1(X*) e_phi1 = M_22 e_phi1 exactly, and e2 is an eigenvector of
  g(s) for every s (computed, exact, `classm5.py` K1-K2), so the excess is |M_22| and the general case cannot arise.]
- **MAJOR 2 (accepted; computed, certified, R2).** In the Frobenius reading stage 0 moves the bound, for every m_1:
  sum_{j=0}^3 |M + W(s + j pi/2) + chi(s + j pi/2) D|_F^2 = 4 |M|_F^2 + 2 (|W(s)|_F^2 + |W(s + pi/2)|_F^2) + 4 chi^2
  |D|_F^2, |D|_F = 2 (exact; cross terms cancel in pairs), so sup_s |g_1|_F^2 >= B := (|W(s)|_F^2 + |W(s +
  pi/2)|_F^2)/2 + 4 chi(s)^2. A grid search over (theta, v, s) at r = a puts the maximum at X*, s = pi/4 (B =
  260.098); certified there **C_app >= 16.127553 and lambda0 < 0.0019079 (Frobenius)**, against round 4-5's
  [Round 8, R8.0 C: rounded the wrong way. The certified lower end of B^(1/2) is 16.1275529788 (r7fixes5's ball
  [16.127553 +/- 2.12e-8]): read C_app >= 16.127552. lambda0 < 0.0019079 stands (0.0019078257 at the ball's end).]
  0.0019950; the point lies in Omega (lzerotrace5.in_omega). With m_1 = 0 the sup there is 16.8866 (floating point,
  not a bound). "Certified" and "unchanged until a lower bound on m_1" are limited to the operator norm (R7.3).
- **MAJOR 3 (accepted; computed, `x7indep5.py`).** dnumber5's headline figures were protected by no check. Now: the
  verifier's swapped-order sum, with its own floor sum (3000 random cases against brute force and dweights5), equals
  dnumber5's chain_level_sum chain by chain and at both interval ends, and gives the four Sum X_7 values, d and N
  exactly (I1, I3); chain_level_sum itself equals brute-force enumeration on 600 random small instances (I2, the
  [Round 8, R8.0 (2): I3 is independent in the summation only (the chains, excesses, n_a and A are dnumber5's); I2's
  generator reached the levels that count every point in 1 instance of 600; widened, 299 (`x7indep5.py`, rerun 9/9).]
  production path, replacing C1's scaled closed form); dnumber5 K4 and K5 now compare with pinned integers; and the
  four mutations of the production path (top level dropped, ceil term 1, two per point, excess 0) each change a pinned
  total (M1-M4), with chain_level_sum's top level dropped disagreeing with brute force (M5). The two-ends
  certification rests on monotonicity: with n_a fixed (asserted equal at both ends), each indicator [g + n d1 < 3,
  g + n d1 <= beta_k - 1 - eps] is nonincreasing in g and d1, so the true sum lies between the ends (I4 checks the
  midpoint of one chain). R6.0's "controls that mutate the computed path and fail" was false for K4-K5 then; true now.
- **m1 (accepted; computed, R3).** The tower list of r6fixes5 F3 was incomplete. D4 Proposition 3.1 (READ D4:113-150)
  has s0 terms at 0, -1, ..., -4, s1 at 0, -1, ..., -4 and v1 at -1, -2, -3, -4; at z = 4e-6 offset 1 lands on a root
  exactly at (s0, -1), (s1, -1) (on 0) and (v1, -2) (on -1), each simple; at z = 0 also at (s0, -2), (s1, -2), (s1, -3),
  each simple. A simple resonance raises the formal solution's log order from the source's 0 to at most 1 (Lemma 1.5),
  and E^iota_ind's offset 1 already has log order 2 from v1 (R5.2): the maximum stays 2, so R5.2's table, E^flat's log
  orders and the ceiling are unchanged (deduced). R6.0 M2's "at offset 1 the formal solutions meet no root" is withdrawn.
- **m2 (accepted; computed, R4).** (3.2)'s E^#(1) contains (lambda#, 0) (I2:175), whose (2.2)-completion puts (2.5099,
  0) in the set before the round at [2, 3), where R1 raises it. eflat5.f4_table with it added: every row and both
  excesses (23, 47) unchanged. R6.0 M1's "no other completion meets a later raise" is false and harmless.
- **m3 (accepted; certified, R5).** r6fixes5 F2's inputs were rounded the wrong way: q_lo >= 0.1966827 (not 0.196683),
  e^(kappa Dtau/2) <= 1.1051725e17 (not 1.105e17); in Arb from stage1rate5's forms the coefficient is <= 3.52422e17, so
  3.525e17 stands; stage1rate5's factor-2 figure is <= 7.04843e17 (it printed 7.048e17, rounded down; superseded). F2's
  [Round 8, R8.0 (3): r6fixes5.out still printed "<= 3.5237e+17 ... True", below the certified value; its inputs are
  now rounded outward and it prints 3.5242e17 (`r6fixes5.py` rerun, 6/6).]
  symbolic "check" and C2 proved nothing; the certified recomputation replaces them (r6fixes5 annotated).
- **m4 (accepted).** R6.1's "Everything else in the chain is an integer" was unsupported (the orders at the record's
  point were not read; d^E's three pieces not read). Withdrawn; R7.2 reads the orders and bounds D_1, and names what is
  still missing (the fixed MODs). R6.4's route to the ceiling as a theorem also needs K3's level-2 log orders (E_col's
  wide reading, u_0, Proposition 4.4's chain carry): recorded.
- **m5, m6, m10 (accepted; stage1cap5 changed).** C_HI is now envelope5 E1's upper end 1.3241034918 and S2's value is
  pinned in [11.8820, 11.8822] (halving C_HI or moving to r = 1.05 a now fails S2); alpha0 is printed rounded down,
  0.0374251 (0.0512240 with mu0 at r = a); the points (v - a, a) are tested in Omega with lzerotrace5.in_omega at
  the 4001 cell ends.
- **m7 (accepted; zeroext5 changed).** Z5, Z5b and C3 now test against Z4's computed C; Z4 pins C_0^2 in [7.84, 7.85];
  C4 drops the kappa (1 - a^2) piece (C = 2.44) and fails Z4. No test function is known that needs that piece, so the
  derivation stays a valid, not a sharp, one; its label is "deduced, certified arithmetic" (R6.4's "certified" for the
  whole bound is corrected), and the norm is (3.2)'s for one choice of generators (r d_r and so(4) fields) at s = 1,
  alpha = -1, a = r_h/2 (fixed up to equivalence).
- **m8 (accepted)** in R7.7. **m9 (accepted).** zerohardy5 H3b computes A_l u_delta's closed form and the limit of
  ((l + 1)^2 - delta^2)^2 only; the norm ratio's O(delta) is not computed: R6.0's sentence overstated it.
- **Nits (accepted).** dnumber5 runs in seconds (docstring corrected); R6's ':4986' is now :4988 (zerohardy5 rerun);
  106,489,470 is 1.065 x 10^8 (R6.6 wrote 1.06 and 1.07); "d is not an integer here" reads "no value of d follows";
  "below 0.0013" reads "below 0.00123"; R6.1's log|sigma| list omits the beta_mu(alpha_0) = 0 cases (READ I12:175-178:
  |sigma|^floor(-mu) log|sigma| at alpha_0 = 2 + mu, 3 + mu, 4 + mu), seated on the verifier's reading that they land
  at K+-exponents >= 3 and change nothing (not re-derived beyond the citation); eflat5's f4_ok is a pin, so its C4
  fails only because 44 != 47; "within a factor 2.1" holds against the limit 2^(1/2) (1.98), 2.125 against the 1.318
  witness.

### R7.1 The re-pin (D615, D616)

N1STAR-PROOF.md is md5 709c63be1748117de9fadf6410eb53a2, 10858 lines (split on newlines; `wc -l` 10857). Against the
[Round 8, R8.0 (4): 10857 lines (the split counted the empty string after the final newline); lzerotrace5.py:12
still says "lines 1-805". N1STAR-PROOF.md has moved since (D618-D623; 11025 lines, md5 9e5363f1... when this round
ended, section 7 at line 919), so T0, A0 and A1 fail at HEAD; the re-pin is left to the main session's final pass.]
D614 file (git 82a7e95, md5 02e76176...), D616 replaced line 632 by 632-634 and D615 lines 634-637 by 636-642; every
other D614 line maps to identical text (checked line by line: lines <= 631 unmoved, 633 -> 635, every line above 637
+5). lzerotrace5 T0: PIN 39acbcf0640c253b3d40f1dc2bd929dd (lines 1-817, section 7's heading at 817 as before at 812),
FILE_PIN 709c63be..., the six trace rows above D614's 637 moved +5 (Lemma 6.3 (c) at 704, Proposition 6.5 at 780,
781, 783, 784, N := K + 3 at 807), all 37 fragments found on their lines; lzeroaudit5 A0/A1: the same pins, TABLE rows
above 637 +5, C3's row now (757, limit); A1 63 hits, 0 unclassified, class N 0. Both rerun, all pass. The md5 is
re-checked at the end of this round (R7.6).

### R7.2 (i) d: the closed-graph orders counted (Appendix R7.A, `d0count5.py`)

- *What is fixed by the closed graph theorem* (READ, located by content, Q0). In Part II exactly three things: II.A
  Lemma 8.5 (a)-(b) (the multiplication and pseudolocality order d_*, II.A:955-967), II.A2 Lemma 1.2 and Proposition
  2.4 (the finite-regularity calculus order M, II.A2:130, 276-281); the other six "closed graph" lines are summaries.
  Every other d_0 of Part II is a statement, a largest-of, an explicit increment d_0 - k (k <= 4) or an explicit
  constant (Q5: the 89 lines classified, 0 unclassified). III.J'':41 fixes a weight loss eps'(eps, k), not an order,
  and III.J'':82 tame constants; neither enters D_0.
- *The replacements* (deduced, R7.A; counts computed). Theorem A.1: a Calderon-Vaillancourt bound with N = 2n + 1 = 11
  pure x- and pure xi-derivatives, S^0_{delta,delta} weights, 0 <= delta < 2/(2 + 5n) = 2/27, proved by Cotlar-Stein
  on a dyadic-shell lattice (Q1: the distant-shell exponent is -0.4325 at delta = 1/100). Lemma A.5 (= 8.5 (a)): D_a =
  J + 2 M0 by a Taylor expansion of the coefficient inside each chart kernel, the remainder bounded by Schur's test.
  Lemma A.6 (= 8.5 (b)). Proposition A.7 (= 2.4 (a)): conjugation by the quantised weights Lambda_(t-m), Lambda'_t,
  two expansions, Theorem A.1 on the main terms, kernel bounds with Peetre's inequality on the remainders.
  Proposition A.8 (= 2.4 (b)-(f) and Lemma 1.2): one composition remainder and one change of chart. Every
  integrability condition is checked as an inequality (Q2, Q3).
- *The orders at the record's point* (READ; deduced, Q4). III.I Theorem 5.3 applies II.F' with II.C Proposition 5.1 at
  eta = m0 = 3 + delta + aleph = 5 (II.F2 Lemma 2.3; delta = 0, aleph = 2), theta_H <= 2 (> theta_L, LOSS-D 2b),
  theta_out >= 2 S-bar - 2 eps with S-bar = 0 (II.C Lemma 2.6), alpha_+ = beta_+ - 5/2, beta_+ in (1/2, 3/2): s_in = 9
  (an integer above 8.5) and s_out = -8 (below -6 - beta_+ - eps for every admissible beta_+). So s in [-8, 9], s0 = s -
  [Round 8, R8.0 (9): Q4 reads only the first branch of s_in (II.C:767-768's alpha_K/theta^3b_in branch is not read)
  and the alpha_K = -2 behind "-6 - beta_+ - eps" is not sourced; recorded, not re-derived.]
  2, the slab order s + 1, s_u = -10; every order at which a closed-graph site is invoked in D_0's chain lies in
  [-14, 11] with N <= 14 (deduced from the cited statements: shifts by m <= 2, by 1 and 2, error orders -N; the proofs'
  internal orders not all re-read).
- *The counts* (computed, at n = 5, delta = 1/100, orders in [-14, 11], N = 14). D_a = 49 (J = 33, M0 = 8), D_b = 64,
  Lemma 8.6's d_0 = 60, M_a = 73, M_2.4 = 171 (composition and chart change included), (L3) d_0 <= 173, (L4) d_0 <=
  175 (II.A2:722-723's d_0 - 2 >= M_2.4 + 2), II.D's trapped-set symbols in C^(d_0 - 4) (II.D:684, 725) d_0 <= 177:
  **D_0 <= 177**, an explicit integer upper bound (deduced on Q4's order range and Q5's census), the closed-graph
  [Round 8, R8.0 A: not established. Proposition A.7's left remainder was weighted by sup t (d0count5 M2); it acts
  through H^(t0), t0 = floor(inf t) - 1: 193 on Q4's range, 203 with the record's input order -N - m = -16, 230 with
  Proposition 2.4 (f) counted (A2), and 399 once every operator order of the chain is admitted (the commutants of
  II.A2 sections 4-5, orders s - 1/2 + delta, |s| <= 10, and their products): `d0count5.py` Q3b, R8.1.]
  obstruction of round 6 removed. Generous, not sharp: a sharper Calderon-Vaillancourt ([n/2] + 1) or a region split
  in place of Peetre would lower it.
- *c'* (computed; deduced). d' = 8, d'' = 9; II.A Proposition 9.6 at s - 2 (Lemma 2.8, Corollary 9.7) d_1 = 20,
  d-tilde = 33; II.E Proposition 4.4 d = d-tilde + 3 >= 35; every tame order in D_1 is d-tilde + 3 with d-tilde =
  s-bar + 2 max(s-under, s-under_0) + 6 at orders in Q4's range, so D_1 <= 48. So FWD + BG = D_0 + D_1 + d' + d'' + 6
  + 2 lies in [D_0 + 60, 250], and **c' = (FWD + BG) + the fixed MODs of a level**, c' >= 62 (round 6: c' >= 14 + D_0).
  [Round 8, R8.0 A: "d = d-tilde + 3 >= 35" reads 36 (d-tilde = 33); c' >= 62 assumed D_0 >= 2, which Q5's d_0 >= 5
  gives; the upper end 250 falls with D_0: FWD <= 474 on the order box, and with the MODs counted c' = 632 (R8.1).]
  At MODs = 0 the bound would be d <= 45,661,383,902,649,727 + 106,489,470 x 250 = 45,661,410,525,017,227.
- *What remains for d* (deduced). **No integer upper bound on d follows yet**: the single missing input is now the
  fixed per-level steps (MODs) of I14's Lemma 2.2 with their losses at the record's weights (among them III.A
  Proposition 4.2 (2) at I12:350 and in Lemma 2.4, III.I'' Lemmas 4.1-4.2, III.H Proposition 3.2; closed forms in
  LOSS-D section 2b). Nothing weaker suffices: by LOSS-D (1.1) c' is the sum of the losses of exactly these steps, and
  each enters d with coefficient 106,489,470, so an upper bound on d is an upper bound on each. This is a reading of
  the record, possible here and not done in this round; it is not the calculus count round 6 named.

### R7.3 (ii) lambda0: stage 1 decided as far as it can be (`r7fixes5.py` R1-R2; `stage1cap5.py` S3)

- *The certified bounds* (certified). Operator norm lambda0 < 0.0024433 (unchanged); **Frobenius lambda0 < 0.0019079**
  (R7.0 MAJOR 2: stage 0 moves it for every m_1); largest entry lambda0 < 0.0012228 (unchanged: entrywise
  sup_s |g_ij| >= |W_ij| + |M_ij + chi D_ij| gives no more without m_1, and chi D's largest entry is |chi| <= 5.95).
- *What stage 1 can do* (deduced; computed, R1). Stage 1 lowers the operator-norm bound iff sup_{Omega x S^1} |m_1 +
  W_TT + chi D|_op > 12.593309 is certified; m_1(X*) e_phi1 != 0 at W_TT's maximiser X* (tau = 2 - a, r = a, theta =
  0) suffices, with a certified excess |m_1(X*)_22| or K/3 + (K^2 + w^2)^(1/2) - (4/3) K. In the Frobenius reading
  any m_1 != 0 at X* raises B by |m_1|_F^2.
- *The single missing input* (deduced). A certified enclosure of m_1(X*) e_phi1 (or of m_1 on a neighbourhood of the
  [Round 8, R8.2: in the class m_1(X*) e_phi1 = M_22 e_phi1 (`classm5.py` K1); the input is the one number M_22.]
  maximisers X*, sigma(X*)), excluding 0. Nothing weaker suffices: (a) with m_1 = 0 the sup is exactly sup |W_TT|_op
  (R1's block structure), so no information that leaves m_1 free can move the bound; (b) an upper bound on m_1, which
  is all Lemma 6.4's or Lemma 2.3's estimates give (stage1rate5: Gronwall factor 1.105e17), cannot; (c) m_1(X*) is the
  value, at a point of Omega inside the hole (r = a < r_h = 1) and off Sigma, of the solution of Lemma 5.3 (a)-(c)
  with Lemma 6.2's data, and changes with the sources on its past in Omega (Duhamel), so a certified value is a
  validated solve of that coupled linear system on Omega; (d) the stage-1 constraint data on Sigma, which the asked
  second-order expansion would give, fix only m_1|_Sigma = a_1 dr dr (Lemma 6.2: phi_1 = 0, (m_1)_{tau .} = 0), and on
  Sigma (r >= v_start - tau0 = 5/2 where W_TT is nonzero) |W_TT|_op <= (4/3) 2^(1/2) c (5/2)^(-3/2) < 0.64, so they
  could decide only through |a_1| > 11.9, which the size of S_1 (quadratic in W, r^-3) makes implausible and only a
  solve could certify. The second-order expansion of the constraints was therefore not carried out: it cannot decide.
  [Round 8, R8.0 (6): "it cannot decide" is too strong; the argument shows it implausible. The bound on Sigma is now
  computed: sup |W_TT|_op <= 0.22189 there (`classm5.py` K3, the angular maximum being exactly 1, so the factor
  2^(1/2) above is not needed), and the data would need |a_1| > 12.37.]
- *What m_1 is known to be* (READ stage5.out S2, S4). Its mean source is nonzero only in dv dth, -(4/9) A^2 E^2 h^2
  sin 2th r^-3, and R^(1)[g0 + lam W] is odd under sigma (th -> pi/2 - th, phi1 <-> phi2) with s -> 3 pi/2 - s, so
  sigma^* m_1 = -m_1: m_1(sigma X*) e_phi2 = -m_1(X*) e_phi1. Neither forces m_1(X*) e_phi1 = 0; whether it vanishes
  is what the solve decides.
- *Stages 2-9* (deduced). They cannot change C_app's forced lower bound, which is the lam -> 0 limit of (g_app -
  g0)/lam and sees g_1 only. They enter lambda0's other terms through C_R, C_D (forced lower bounds: the order-K
  profiles of Ric^H(g_app) and of the constraint residual, which need R^(m) to order K = 8, out of symbolic reach,
  stage5.py stopping at m = 1) and through M, but only in combination with constants the proof may enlarge (C3,
  C_inf, C_dw, C_N; Round 3 M2), which no certified bound fixes from below. So stages 2-9 cannot raise the certified
  bounds and cannot lower them by this method: for the certification used here the bounds are final beyond stage 1.
  [Round 8, R8.0 (6): true of the lam -> 0 limit of (g_app - g0)/lam only. At a finite lambda0 the forced bound is a
  sup over lam in (0, lambda0], which g_2 and later stages can raise by O(lambda0): "final" is relative to this
  method.]

### R7.4 (iii) the inverse bounds: the tensor blocks proved (`tensorzero5.py`)

- *The tensor blocks* (computed, exact; deduced inequalities, certified arithmetic). In the class, I.C:497's sigma_min
  splits into the s0 block (on the complement of its one state), the s_l and the t_l blocks at even l >= 2 (class5 C2).
  The class's TT harmonic at each even l is solved (T1: l = 2, A = 1, B = 1 - 3 cos^2 th; l = 4 printed). For h = r^2
  H(r) T on 5D Tangherlini: tr h = 0, div h = 0, iota_{dt#} h = 0, so E^Ups h = 0, delta_{E^Ups} G h = 0 and the gauge
  term of L_b vanishes; and D Ric(h) = (1/2) r^2 (A_l H) T exactly, every other component 0 (T2-T3, l = 2 and 4).
  As an operator identity, D Ric(r^2 H T) = (1/2) r^2 [(-r^-3 (P H')') T + r^-2 H (-lap T + 2 T)] for every traceless
  [Round 8, R8.0 (7): T3b evaluated this at one r and one H; it now evaluates it at 108 points (three A, three H, four
  r, one inside the horizon, three angles; `tensorzero5.py` rerun): an evaluation, not a symbolic identity.]
  class tensor with div T = 0 (T3b, evaluated at 50 digits; residual below 1e-40; with -lap T + T it fails, C4), so
  with the harmonics' eigen-equation it holds at every even l: the t_l block of L-hat_b0(0) is one half of zeroext5's
  scalar model A_l at the same l. The norm's angular weight is the
  so(4) Casimir on TT harmonics, sum ||L_K T||^2 = (l (l + 2) + 4) ||T||^2 (T4, computed at l = 2: 12; the scalar
  harmonic gives 8). zeroext5's pieces with that weight give C_T,l^2 = (2 + 5/L)(1 + kappa q) + q + 4 q^2 + q/f(b1),
  sup over even l >= 2 at l = 2, **C_T^2 = 55289/14256, C_T = 1.9693**: on [r_h/2, oo) x S^3, every t_l block at once,
  ||h||_{Hbar^(1,-1)_b} <= 3.939 ||L-hat_b0(0) h||_{Hbar^(0,1)_b} = 1.970 ||2 L-hat_b0(0) h|| (T5; T6's 300 test
  functions reach 0.54). Controls: the trace part (s-type) breaks T2-T3 (C1); the scalar weight is refuted at l = 2
  (C2); the constant with the scalar weight leaves T5's pinned interval (C3); T3b with the wrong shift fails (C4).
- *What remains for I.C:497* (deduced). **The single missing input: a lower bound for sigma_min of the scalar-type
  blocks of L-hat_b0(0)** (the s0 block on the complement of its state, four radial functions; the s_l blocks at even l
  >= 2, seven), in (3.2)'s norm, uniform in l. They carry the gauge terms E^C (gam_C = 10^6, e_C = 1/102400, v = 1/2)
  and E^Ups (gam_U = e_U = 1/100), are not formally symmetric, and no multiplier identity is written for them; the
  factorisation det N_L = c (lam + l)(lam - l - 2) det N_Ups(lam - 1) det N_C(lam + 1)/D (lin5 E2) suggests the route
  through box^C(0) and box^Ups(0) on scalar-type 1-forms. Nothing weaker suffices: L-hat_b0(0) commutes with SO(4)
  (b0 is the static Tangherlini point) and the norm is SO(4)-invariant, so the isotypic blocks are orthogonal and the
  inverse's norm is the largest of the blocks' (Schur's lemma); a bound for L-hat_b0(0)^-1 is a bound for each block,
  and the tensor blocks and the scalar model, being other blocks, say nothing about the scalar-type ones.
- *The other six* (I.B:1513, :1685, :1978; III.F'':223; III.D:365; II.F:1393 with ||Pi||). R7.A makes the orders of the
  calculus explicit; their constants are explicit in principle (Theorem A.1's C(n, delta), the Taylor and Peetre
  constants) but the microlocal estimates the six rest on (elliptic, real principal type, radial points, the trapped
  set) carry further constants (ellipticity margins, the positive-commutator symbols' norms, the threshold margins).
  The single missing input for them: those estimates' constants at L_b0 evaluated in the write-out's variable-order
  norms, with certified spectral bounds in the same norms (E2-PILOT has them for the scalar wave in its own norm).
  So no lower bound for lambda1 or delta; the upper bounds stand (log10 delta < -7.6666e16, lambda1 < delta).

### R7.5 Proved, computed, open

- *Certified*: lambda0 < 0.0024433 (operator), < 0.0019079 (Frobenius, new), < 0.0012228 (largest entry); the tensor
  [Round 8, R8.0 (8): C_T is deduced with certified arithmetic, not certified (as m7 for zeroext5). The tensor
  identities were computed at l = 2, 4 and the Casimir at l = 2 only (now l = 2, 4, with the so(4) Casimir for every
  l, `tensorzero5.py` T4); x7indep5's route is independent in the summation only.]
  blocks' constant C_T = 1.9693 (deduced inequalities, certified arithmetic); r6fixes5 F2's coefficient < 3.52422e17.
- *Computed, exact*: the re-pin; the stage-1 block structure at X*; the four-phase identity; the tower resonances;
  Sum X_7, d, N by an independent route; the tensor block identities D Ric(h) = (1/2) r^2 (A_l H) T and the Casimir.
- *Deduced (counts computed)*: Appendix R7.A's theorems; D_0 <= 177 and D_1 <= 48 on Q4's order range; c' in [62,
  [Round 8, R8.0 A: withdrawn; D_0 <= 399 and D_1 <= 52 on the order box, c' = 632, d an integer (R8.1).]
  250] + MODs.
- *Open, each with its single missing input*: d as an integer (the per-level MODs at the record's weights, a reading);
  lambda0's value or a lower certified bound from stage 1 (a certified m_1(X*) e_phi1); I.C:497 for L_b0 (the
  scalar-type blocks); the other six inverse bounds (their microlocal constants at L_b0 and certified spectral bounds
  in the write-out's norms). The ceiling as a theorem (round 6) still needs I11 Proposition 3.1 (c) sharpened in the
  supplement and K3's level-2 log orders (R7.0 m4).

### R7.6 Sources (round 7)

N1STAR-PROOF.md (md5 709c63be1748117de9fadf6410eb53a2 at the start and, re-checked, at the end of this round; D614's
file from git 82a7e95) lines 1-817, 461-462, 548, 631-642; proof5: PART-II-A-SETUP.md:330-445, 825-1010, 1130-1225,
1312-1330, 1366-1372; PART-II-A2-STANDARD.md:100-306, 308-425, 543-786, 811, 832; PART-II-C-OPERATORS.md:284-330,
700-790; PART-II-D-REGULARITY.md:573-725, 1040, 1082-1084; PART-II-D2-BREGULARITY.md:240-250; PART-II-E-ENERGY.md:
640-660, 810-870, 1140-1205; PART-II-F2-TAME.md:210-262, 440-560; PART-III-I-CONE.md:330-440; PART-III-J3-TAME.md:
36-46, 80-84; PART-III-D4-GENSTATES.md:113-150; PART-III-I12-SPECTRAL.md:170-180; PART-III-I2-SCRI.md:175; LOSS-D.md
sections 1-4; the round-6 verifier's report and scratch scripts (x7indep.py, chi_iv.py, s1rate_exact.py,
lsharp_completion.py, ecolmatch.py; the first, third and fourth adopted into checks/); checks imported, not copied:
lzeroconst5, lzerotrace5, eflat5, dweights5, stage1rate5, dnumber5, class5, zeroext5.

### R7.A Appendix: a quantitative calculus for II.A's classes (item 1, every step)

*Setting.* n = 5 (M-tilde has dimension 1 + 4). [SBG]'s charts are unit cells with uniformly C^infinity transitions,
finite multiplicity, and the rescaled phase; in rescaled coordinates every chart operator is Op_psi(p)u(x) :=
(2 pi)^-n int int e^{i(x - y).xi} p(x, xi) psi(x - y) u(y) dy dxi, psi a fixed cut-off, and Op_psi(p) = Op(p_psi),
p_psi(x, .) = (2 pi)^-n psi-hat * p(x, .), which has the same pure derivative bounds up to constants (Peetre). The
classes of II.A2 Definition 1.3, C^(M)_nu S-tilde^m, have, by II.A2 Lemma 2.2's coordinates (d_zeta = e^-tau times
bounded combinations of d_omega, d_tau), |d_x^gamma d_zeta^beta a| <= C <log>^(nu j) <zeta>^(m - |beta|) for j =
|gamma| + |beta| <= M, and <log>^(nu j) <= C_delta <zeta>^(delta j): a finite-regularity symbol of type (1 - delta,
delta) for every delta > 0; variable orders (S8) add log factors only. Fix delta = 1/100. Constants C below depend on
n, delta, the orders and the smooth calculus, never on the coefficient being counted; only derivative counts matter.

**Theorem A.1 (Calderon-Vaillancourt with a count).** Let 0 <= delta < 2/(2 + 5n), N := 2n + 1, and let p have
continuous pure derivatives d_x^gamma p, d_xi^beta p, |gamma|, |beta| <= N, with A_x := max sup <xi>^(-delta|gamma|)
|d_x^gamma p| and A_xi := max sup <xi>^(delta|beta|) |d_xi^beta p|. Then ||Op(p)||_{L^2 -> L^2} <= C (A_x A_xi)^(1/2).

*Proof.* (1) Partitions: psi_k (k >= 0) dyadic in xi (supp psi_k in 2^(k-1) <= |xi| <= 2^(k+1), |d^beta psi_k| <= C
2^(-k|beta|)); with h_k := 2^(k delta), theta, chi in C_c^infinity([-1, 1]^n) with sum_i theta(. - i) = sum_j chi(. -
j) = 1. Put p_I := chi(h_k x - j) theta(xi/h_k - i) psi_k(xi) p, I = (k, i, j), T_I := Op(p_I). (2) On supp p_I,
<xi> is within a factor 2 of 2^k, so |d_x^gamma p_I| <= C A_x h_k^|gamma| and |d_xi^beta p_I| <= C A_xi h_k^-|beta|
(delta < 1). (3) T_I T_J^* has kernel (2 pi)^-n int e^{i(x - y)xi} p_I(x, xi) conj p_J(y, xi) dxi, zero unless the
xi-supports meet (|k - k'| <= 1, adjacent boxes); N integrations by parts in xi give |kernel| <= C A_xi^2 h_k^n (1 +
h_k |x - y|)^-N, and Schur's test over the x-boxes (side 2/h_k) gives ||T_I T_J^*|| <= C A_xi^2 (1 + |j - j'|)^-N;
summing ||.||^(1/2) over J converges iff N/2 > n. (4) T_I^* T_J has, on the Fourier side, the kernel L(xi, xi') =
(2 pi)^-2n int e^{iz(xi' - xi)} p_J(z, xi') conj p_I(z, xi) dz over the overlap of the x-boxes (volume <= C
min(h_k, h_k')^-n); N integrations by parts in z give |L| <= C A_x^2 min(h)^-n min(1, ((h_k + h_k')/|xi - xi'|)^N),
and the operator norm is at most sup |L| times (|box_xi(I)| |box_xi(J)|)^(1/2) = (h_k h_k')^(n/2). For |k - k'| <= 1
the sum over J converges iff N/2 > n. (5) For k' >= k + 2: |xi - xi'| >= 2^(k'-2), the factor is <= 2^(-(k'(1 -
delta) - 3)N), the prefactor (h_k'/h_k)^(n/2), the number of j' overlapping j at most C 2^((k'-k) delta n), the
number of i' in shell k' at most C 2^(k'(1 - delta)n); the sum of ||.||^(1/2) over shell k' is at most C A_x
2^(k' E), E := delta n/4 + delta n + (1 - delta) n - (1 - delta) N/2, and E < 0 iff (1 - delta)/2 > (5/4) delta n at N
= 2n + 1, i.e. delta < 2/(2 + 5n) (d0count5 Q1: E = -0.4325 at delta = 1/100; E = 0 at 2/27, control C2). k' <= k -
[Round 8, R8.0 (10): shells k and k + 2 can touch (both meet |xi| = 2^(k+1)), so |xi - xi'| >= 2^(k'-2) needs k' >=
k + 3, and the near group of steps (4)-(5) is |k - k'| <= 2. Constants only.]
2 is symmetric, with at most k shells and a polynomial factor. (6) Cotlar-Stein: sum_I T_I converges strongly with
norm <= C (A_x A_xi)^(1/2); on Schwartz functions the partial sums converge pointwise to Op(p)u (dominated
convergence), so the limit is Op(p). []

**Lemma A.5 (= II.A Lemma 8.5 (a), explicit).** For a variable order t put t0 := floor(inf t) - 1, M0 := ceil(max(0,
-t0)/2), J the least integer with J (1 - delta) > sup t + 2 M0 + n + delta, D_a(t) := max(J + 2 M0, |t0|). Then
||l u||_{H^t} <= C ||l||_{C^(D_a)_e3b} ||u||_{H^t}, the norm of H^t being ||Lambda_t u||_{L^2} + ||u||_{H^t0},
Lambda_t := sum_alpha phi_alpha^* Op_alpha(lambda_alpha), lambda = <zeta>^t (equivalent to (S8)'s by the smooth
calculus).

*Proof.* (1) H^t0 part: t0 is an integer; Leibniz (t0 >= 0) or duality with the uniformly positive density (t0 < 0)
gives ||l u||_{H^t0} <= C ||l||_{C^|t0|} ||u||_{H^t0}, chart by chart (multiplication commutes with the chart
cut-offs). (2) In chart alpha, Taylor's formula l(y) = sum_{|b| < J} d^b l(x) (y - x)^b/b! + R_J(x, y), R_J =
sum_{|b| = J} (J/b!) (y - x)^b int_0^1 (1 - th)^(J-1) d^b l(x + th (y - x)) dth, and (y - x)^b e^{i(x - y)xi} =
(i d_xi)^b e^{i(x - y)xi} with one integration by parts in xi, give exactly Op_alpha(lambda)(l v) = sum_{|b| < J}
(d^b l/b!) Op_alpha(D_xi^b lambda) v + Rem_J v. (3) |b| = 0 sums to l Lambda_t u, of norm <= ||l||_inf ||Lambda_t
u||. (4) 1 <= |b| < J: the chartwise sums are bounded in L^2 by C ||l||_{C^(J-1)} (sum_alpha ||Op_alpha(D_xi^b
lambda_alpha) u_alpha||^2)^(1/2) <= C ||l||_{C^(J-1)} ||u||_{H^t}, as D_xi^b lambda has order t - (1 - delta)|b| (the
smooth calculus; no coefficient). (5) Rem_J: for v = (1 - Delta)^M0 w, ||w||_{L^2} <= ||v||_{H^t0} (-2 M0 <= t0);
moving (1 - Delta_y)^M0 onto the kernel puts at most 2 M0 more derivatives on d^b l(x + th (y - x)) (factor th^.. <=
1), on psi and on e^{-iy xi} (factors xi^gamma, |gamma| <= 2 M0): the kernel is at most C ||l||_{C^(J + 2 M0)} int
<xi>^(sup t + delta - J(1 - delta) + 2 M0) dxi, finite by the choice of J, and supported in |x - y| <= R_psi; Schur's
test gives ||Rem_J v|| <= C ||l||_{C^(J + 2 M0)} ||v||_{H^t0} (control C1: J - 1 fails). (6) Finite multiplicity and
[Round 8, R8.0 (11): [SBG]'s cut-off localises to cells of B, not of rho B ((3.27), p. 44), so in rescaled
coordinates it is psi(rho (x - y)) and "supported in |x - y| <= R_psi" is not uniform. The decay comes instead from
integrating by parts in xi on the smooth factor: (x - y)^gamma e^{i(x - y)xi} = D_xi^gamma e^{i(x - y)xi}, the
derivatives falling on D_xi^b lambda, which lowers its order by |gamma| and costs no derivative of l; with |gamma|
= n + 1 Schur's test applies uniformly. The count D_a is unchanged.]
sum_alpha ||theta_alpha u||^2_{H^t0} <= C ||u||^2_{H^t0} sum the charts. The b-regularity part is Leibniz on top. The
direct proof needs no closed graph and no mollification. []

**Lemma A.6 (= II.A Lemma 8.5 (b), explicit).** With sigma := max(0, ceil(sup t)), t'0 := floor(inf t') - 1, M1 :=
ceil(max(0, -t'0)/2), Jb the least integer with Jb (1 - delta) > sigma + 2 M1 + n + delta, D_b := Jb + sigma + 2 M1:
||B l (I - B#) u||_{H^t} <= C ||l||_{C^(D_b)} ||u||_{H^t'}. *Proof.* As A.5 (2) for B = Op(b): B l = sum_{|b| < Jb}
(d^b l/b!) Op(D_xi^b b) + Rem. Op(D_xi^b b)(I - B#) is residual (disjoint WF', the smooth calculus): H^t' -> H^sigma;
multiplication by d^b l maps H^sigma to itself at the cost of sigma more derivatives (Leibniz); H^sigma is in H^t.
Rem (I - B#): (I - B#) is bounded on H^t', H^t' is in H^t'0, and Rem: H^t'0 -> H^sigma by A.5 (5) with sigma
x-derivatives added to the kernel (they cost sigma derivatives of l and raise the xi-exponent by sigma). []
Lemma 8.6 then has d_0 = max(D_a(s - m), D_b(s - m, -N - m)) (its proof uses 8.5 (a) at s - m and (b) at s0 = -N - m).

**Proposition A.7 (= II.A2 Proposition 2.4 (a), explicit).** Op(a): H^t -> H^(t - m) for a in C^(M) S-tilde^m once M >=
M_a := max(P1, ..., P5) of d0count5.M_a. *Proof.* ||Op(a)u||_{t - m} = ||Lambda_(t-m) Op(a) u|| + ||Op(a)u||_{H^tau0}.
(1) The chart changes act on the smooth Lambda's only (each chart piece of Op(a) is composed with Lambda written in that
chart, modulo residual errors of the smooth calculus), so they cost no derivative of a. (2) Left: Lambda_(t-m) Op(a) =
Op(lambda # a), lambda # a = sum_{|al| < J1} d_xi^al lambda D_x^al a/al! + r_J1, r_J1 = sum_{|al| = J1} (J1/al!) int_0^1
(1 - th)^(J1-1) (2 pi)^-n int int e^{-iy.eta} d_xi^al lambda(x, xi + th eta) (D_x^al a)(x + y, xi) dy deta dth. (3) The
master estimate: inserting <y>^-2L (1 - Delta_eta)^L and <eta>^-2L' (1 - Delta_y)^L' (2L > n, 2L' > n + |mu_f|, mu_f the
order of d_xi^al lambda, by Peetre <xi + th eta>^mu <= 2^|mu| <xi>^mu <eta>^|mu|) gives |r_J1| <= C <xi>^mu1 sup
|d_x^<=2L' D^al a|, mu1 = (t - m)_hi + m_hi + delta - J1 (1 - 2 delta). (4) Right: for the main terms c_al, write u =
Lambda'_t Lambda_t u + R u (R residual), Op(c_al) Lambda'_t = Op(c_al # lambda') with the expansion of length J2 and its
remainder by (3) with the roles exchanged (the eta-integrations hit c_al: 2L xi-derivatives; Peetre falls on the smooth
lambda'). (5) The main terms p are of order 0 in S^0_{delta,delta} and Theorem A.1 needs N pure derivatives of each: P1
= (J1 - 1) + (J2 - 1) + N. (6) The remainders are of order below -n after their weights (J1, J2 so chosen; checked), so
their kernels converge absolutely; Schur's test needs decay in x - y, given by 2K = n + 1 xi-derivatives: P2 = J1 +
2L'_1 + 2K, P3 = (J1 - 1) + J2 + 2L + 2K. (7) R u and the H^tau0 part at constant orders: P4 = (J1 - 1) + N, P5 likewise
with tau0 = floor((t - m)_lo) - 1 (right composition with <D>^-t0 is exact). Every condition is checked in d0count5 Q3
(control C4: 2L dropped fails). []

**Proposition A.8 (= II.A2 Proposition 2.4 (b)-(f) and Lemma 1.2, explicit).** For smooth symbols, (b): Op(a1)Op(a2)
- Op(a1 a2) = Op(r_1), r_1 the J = 1 remainder of (2), whose derivatives by (3) cost 1 + max(2L, 2L') derivatives of
each factor beyond those taken; pieces in different charts need one change of chart of a finite-seminorm factor
(Kuranishi: kappa(x) - kappa(y) = Phi(x, y)(x - y); the amplitude a(kappa(x), Phi^-T eta) reduced to a left symbol,
each term al costing 2|al| xi-derivatives for a gain |al|, the remainder by (3)): C_ch := 2 J1 + 2L'_1 + 2K. So M_b :=
M_a(t, m1 + m2 - 1 + delta) + 1 + max(2L, 2L') + C_ch; (c) and (f) are the same count; (d) adds 1 (II.A2's (M + 1));
[Round 8, R8.0 A2: "(c) and (f) are the same count" is unproved for (f), which II.A2:682-695 applies to [D_a,
Op(a-check)], [[D_a, .], .] and i[L_R, D A]: up to three order drops, each needing one more term of every
expansion. Counted in R8.1 (Lemma A.9) and `d0count5.py` M_f.]
(e) (Lemma 1.2, disjoint supports) has no main terms, every Taylor term vanishing on disjoint supports, so it costs
the remainder alone at order -N_e, at most M_b. The record's mollification (II.A2 Lemma 2.2) then carries these to
symbols in C^(M + 2). M_2.4 := M_b + 1 = 171 at the record's orders (d0count5 Q3). []

*Reading off D_0* (deduced; computed). (L3) needs Proposition 2.4 at its symbol class C^(d_0) (d_0 >= M_2.4 + 2) and
Lemmas 8.5-8.6; (L4) d_0 - 2 >= M_2.4 + 2 (II.A2:722-723); II.D's symbols in C^(d_0 - 4): d_0 >= M_2.4 + 6; the
energy and slab estimates of II.E, II.D', II.F2 take the largest of these or add 2 (II.D2:248, II.E:868 over Lemma
8.5's number). So D_0 <= max(M_2.4 + 6, d_0(8.6) + 2, D_a + 2) = 177 at the orders of R7.2.
[Round 8, R8.0 A, (12): II.D's C^(d_0 - 3)/C^(d_0 - 4) multiplications add D_b + 4 to the maximum (68; no effect);
A.7 (1)'s cut-off and residual errors were not shown free of derivatives of a: charged one change of chart they
cost M_a + C_ch < M_2.4, inside the maximum. With A and A2 the figure is 399 on the order box (R8.1).]

### R7.7 Proposed text for the paper's section 9 (replaces R6.6; claims only what is proved or computed)
[Round 8, R8.0 B: superseded by R8.7. Three claims exceed the record: "only through its mean correction at the point
where the first-order wave is largest" (R7.3's criterion is a sup over Omega x S^1 with X* sufficient: "for example
through"); "an explicit calculus bound in the supplement ... at most 177 ... at most 250" (the bound is in
CONSTANTS5.md, not the supplement, and the figures fall with A); "in the supplement's norm" without "for one choice
of generators" (m7).]

  The threshold lambda0 that the proof of Theorem 1 delivers is traced term by term to the supplement. At the numerical
  point it is below 0.0025 in the operator norm, 0.0020 in the Frobenius norm and 0.00123 in the largest entry
  (certified), so the wavelength 10 l5 lies more than 400 times beyond it. The first linear stage can lower the
  operator-norm bound only through its mean correction at the point where the first-order wave is largest, inside the
  hole on the inner boundary; that value needs a certified solve of the stage's linear system and is not computed, so
  no value of lambda0 is given. The loss d: d >= 8.40 x 10^15 at a parameter point meeting every condition decidable
  there (computed). Reading the construction's logarithms step by step (deduced) and summing over its 1.065 x 10^8
  levels gives d <= 4.567 x 10^16 + 1.065 x 10^8 c' (computed), c' the fixed loss per level: the coefficient orders
  the write-out fixes by the closed graph theorem are now counted (an explicit calculus bound in the supplement,
  deduced, with the counts computed: at most 177 at the record's orders), and c' is at least 62 and at most 250 plus
  the losses of the level's other fixed steps, which are not yet read, so no value of d follows. For what the proof's
  formulas can deliver, log10 delta < -7.66 x 10^16 and lambda1 < delta; no lower bound follows. Of the seven inverse
  bounds a lower bound needs, the zero-energy one is proved for the scalar model (constant 2.81) and for the tensor-type
  part of the linearised operator in the symmetry class (constant 3.94), in the supplement's norm, every harmonic,
  through the horizon; for its scalar-type part it is not done, and the others need constants of the write-out's
  microlocal estimates and certified spectral bounds in its norms.

## Round 8 (2026-11-06)

*Status.* Appended to rounds 1-7; not yet read by a verifier. R8.0 seats the round-7 verifier's report and the
coordinator's two notes, each item re-derived first; bracketed `[Round 8, ...]` notes now follow the lines of round 7
they correct (and R4.0 (i)), the old text kept. R8.1-R8.4 take the four items in the order asked; R8.7 is the proposed
replacement for the paper's section 9 text. New programs, each with its `.out` and controls that mutate the computed
path and must fail (they do): `checks/modcount5.py` (12/12), `checks/classm5.py` (9/9). Changed and rerun:
`d0count5.py` (18/18; the verifier's A and A2, pins, five new controls), `dnumber5.py` (10/10; K6's text annotated,
output otherwise identical), `x7indep5.py` (9/9; I2's generator widened), `r6fixes5.py` (6/6; F2's inputs rounded
outward), `tensorzero5.py` (11/11; T3b at 108 points, T4 at l = 2 and 4), `gronwall5.py` (docstring re-pointed by
content; output identical). Not rerun: `lzerotrace5.py`, `lzeroaudit5.py` (their whole-file pins fail at HEAD since
D618-D623; the re-pin is the main session's). N1STAR-PROOF.md and the paper are not edited.

### R8.0 (verifier of round 7; the coordinator's notes)

The verifier reran the eleven round-7 programs (byte-identical outputs), recomputed the l = 2 tensor block with a
full-matrix Ricci routine, the four-phase identity, C_T^2 = 55289/14256 and the excesses, and ran a mutation harness.
Its findings, each re-derived before it is seated:

- **A (accepted; computed, `d0count5.py`).** Proposition A.7's left remainder Op(r_J1) acts on u through the lower
  part of the norm, ||u||_{H^t0}, t0 = floor(inf t) - 1 (or through Lambda'_t, of order -t, up to -inf t), so its
  weight is 2 M2 >= -t0, not sup t: d0count5.py:131 had M2 = ceil(max(0, sup t)/2). Re-derived: with M2 = ceil(-t0/2)
  the program reproduces the verifier's table (M_2.4 + 6 on Q4's range: 185 with -inf t, 193 with -t0; with T_LO =
  -16, the record's own input order -N - m of II.A2:389-391, 195 and 203). Both figures are below what the chain needs
  once A2 and the operator orders are counted (R8.1): D_0 <= 399, FWD <= 474, c' = 632. Pinned now: D_a = 53, D_b = 64,
  [R9, R9.0 M1: on the box M_f was counted with factor order 2 (Peetre's 2L' = 8); with A.7 (3)'s exponent over the
  factors' orders, M_2.4 = 376, M_f = 429, D_0 <= 435, FWD <= 510, c' = 668 (d0count5 and modcount5 re-pinned).]
  M_a = 81, M_2.4 = 197, M_f = 224, D_0 = 230 on round 7's operator orders, and M_a = 138, M_2.4 = 374, M_f = 393,
  D_0 = 399, FWD = 474 on the box. `OK['D0'] = D0 > 0` is replaced by the pins; the four mutations the verifier found
  undetected (2K = 2, C_ch = 0, delta = 1/20, M2 corrected) are controls C5-C8, and C9 is round 7's range. The
  statements at :1701, :1707, :1787-1788 and :1918-1919 carry bracketed notes.
- **A2 (accepted; counted, R8.1 Lemma A.9).** Proposition 2.4 (f) is applied at II.A2:682-695 to [D_R, A-check],
  [[D_a, Op(a-check)], Op(a-check)] and i[L_R, D_a-check A-check]: up to three order drops, each an exact cancellation
  of main terms that needs one more term of every expansion. "(c) and (f) are the same count" (:1897) is withdrawn;
  (f) is counted at those instances (M_f).
- **B (accepted; R8.7).** R7.7 repeated the round-6 "only through" at :1911-1913 (R7.3's criterion is a sup over
  Omega x S^1, X* sufficient): "for example through". The calculus bound is in CONSTANTS5.md, not the supplement, and
  its figures fall with A. "In the supplement's norm" needs "for one choice of generators" (m7). R8.7 is written so.
  [R9, nit 7: "in CONSTANTS5.md, not the supplement" reads: in CONSTANTS5.md (a note of the supplement's tree),
  not in the write-out; R8.7 uses the paper's broad "supplement".]
- **C (accepted).** r7fixes5 prints C_app (Frobenius) as the ball [16.127553 +/- 2.12e-8], whose lower end is
  16.1275529788; the text's "C_app >= 16.127553" (:1615) rounded the ball's midpoint, the wrong way. Read >= 16.127552;
  lambda0 < 0.0019079 stands (0.0019078257 at the ball's end).
- **(1) MAJOR 1's excess (accepted, and resolved in the class; computed, `classm5.py` K1-K2).** r7fixes5:115-118
  certifies the excess only for M = w (e2 e3^T + e3 e2^T); in general it needs a lower bound on u^T g u, so all of
  m_1(X*). In the class the general case does not occur: the eight invariant components (vv, vr, rr, v th, r th, th th,
  phi1 phi1, phi2 phi2; stage5.py's COMP) have no phi1-cross component, and at phi1 = 0, d_x2 = d_phi1/(r cos th) while
  no other coordinate field has a d_phi1 part, so the x2 column of every class tensor there is (0, 0,
  M_phi1phi1/(r cos th)^2, 0, 0) (K1, exact, every th; by continuity on the axis th = 0); at X* e2 is an eigenvector of
  g(s) = M + W(s) + chi D for every s, with eigenvalue M_22 + (4/3) K cos s (K2, exact). So the excess is |M_22| and the
  enclosure needed is of the one number M_22 = (m_1)_phi1phi1(X*)/a^2 (R8.2). Control: a v phi1 component, outside the
  class, breaks K1 (C1); an off-class M_23 breaks K2 (C2).
- **(2) MAJOR 3 (accepted; `x7indep5.py`).** I3 is independent in the summation only (the chains, excesses, n_a and A
  are dnumber5's). I2's generator reached the levels counting every point in 1 instance of 600 (re-derived: kb =
  ceil((Tb - alpha1)/s), Tb - alpha1 about 2, exceeds K - 1 unless s > 2/K); every second instance is now drawn with
  s, K and d1 large enough, 299 of 600 reach those levels, and I2 requires at least 100.
- **(3) r6fixes5.out (accepted).** It printed "<= 3.5237e+17 ... True", below the certified 3.52422e17: its inputs were
  the round-6 roundings. They are now rounded outward (q_lo >= 0.1966827, e^(kappa Dtau/2) <= 1.1051725e17) and it
  [R9, minor 4: the %.4e print still rounded the computed 3.524212e17 down to 3.5242e17; it is now printed rounded
  up, 3.5243e17 (r6fixes5.py rerun, 6/6).]
  prints 3.5242e17.
- **(4) R7.1 (accepted; reported).** 10857 lines, not 10858; lzerotrace5.py:12 says "lines 1-805". N1STAR-PROOF.md has
  moved since (11025 lines, md5 9e5363f1..., section 7 at 919 when this round ended): T0, A0, A1 fail at HEAD; not
  re-pinned here, as instructed.
- **(5) The coordinator's note on D623 (accepted; checked).** N1STAR-PROOF.md 0.3 now fixes "one fixed number with 0 <
  eps1 < min(s0, mu0/a^2 - 1)" and Lemma 2.3 carries "|gt^-1| <= (s0 - eps1)^-1". At the numerical point mu0/a^2 - 1 >
  12 (R4: mu0/a^2 = 13.73), so the minimum is s0 in [0.030768559, 0.030768560] (lzerotrace5 T7); every lambda0 bound
  here uses eps1 < s0 with C_app >= 12.593309 (operator), so lambda0 < 0.0024433 agrees with the new 0.3, and the
  Frobenius and largest-entry figures are readings of the same eps1 in other norms (R5.1, R6.0). R4.0 (i)'s line
  numbers (:89-92, :222) and gronwall5.py's (:230-235) are re-pointed by quoted content.
- **(6) R7.3 (accepted).** "It cannot decide" (:1735) is too strong: implausible. The Sigma bound is now computed
  (`classm5.py` K3): the angular maximum of |W_TT|_op/((4/3) E r^(-3/2)) is exactly 1 (H^2 (4 C^4 + S^4) = 5/2 + 3q/(1 +
  q^2) <= 4, equality at q = 1; H^2 (C^4 + S^4) = 1), so sup_Sigma |W_TT|_op <= 0.22189 (certified; round 7's 0.64
  carried a needless factor 2^(1/2)), and Sigma's data would need |a_1| > 12.37. "Stages 2-9 cannot change C_app's
  [R9, nit 10: dropping 2^(1/2) alone gives 0.4466; the rest of the drop to 0.22189 is the envelope bounded cell by
  cell on Sigma (E(v) small near v = 1/2, where r^(-3/2) is largest).]
  forced lower bound" holds for the lam -> 0 limit only; at a finite lambda0 the forced bound is a sup over lam in (0,
  lambda0], which g_2 and later stages can raise by O(lambda0): "final" is relative to this method.
- **(7) R7.4 (accepted; `tensorzero5.py` rerun).** T3b evaluated the identity at one r with one H; it now evaluates it
  at 108 points (three A, three H, four r with one inside the horizon, three angles; largest residual 7.3e-158 at 50
  digits): still an evaluation, so "operator identity" (:1754) is read as one. T4 ran l = 2 only; it now runs l = 2, 4
  (12, 28), beside the so(4) Casimir 2 [j1 (j1 + 1) + j2 (j2 + 1)], (j1, j2) = (l/2 + 1, l/2 - 1), which gives l (l + 2)
  + 4 at every l (the verifier's argument, now printed).
- **(8) R7.5's labels (accepted).** C_T is deduced with certified arithmetic, not certified; the tensor identities were
  computed at l = 2, 4 and the Casimir at l = 2; x7indep5 is independent in the summation only. Noted at :1783.
- **(9) Q4 (accepted; recorded).** Q4 reads only the first branch of s_in (II.C:767-768's alpha_K/theta^3b_in branch is
  not read) and alpha_K = -2 behind "-6 - beta_+ - eps" is not sourced. Recorded, not re-derived: R8.1's order box
  [R9, R9.0 M2: read and settled (d0count5 Q4b): alpha_K = -2 is III.I Theorem 5.3's ("uses them over K^+ with
  weights alpha_+, -2"), theta^3b_in = theta_in = 0, and the second branch needs only s_in > 11/2.]
  takes s in [-10, 10], and a second branch giving s_in > 9 would widen the box and raise D_0 with it.
- **(10) Theorem A.1 (accepted).** Shells k and k + 2 touch (both meet |xi| = 2^(k+1)), so the near group of steps
  (4)-(5) is |k - k'| <= 2 and |xi - xi'| >= 2^(k'-2) needs k' >= k + 3. Constants only; noted at :1838.
- **(11) Lemmas A.5/A.6 (accepted; re-derived).** [SBG] (3.27), p. 44, localises the cut-off to cells of B, not of rho
  B: in rescaled coordinates it is psi(rho (x - y)), and the support claim at :1860-1861 is not uniform. The kernel's
  decay is obtained instead by integrating by parts in xi on the smooth factor D_xi^b lambda ((x - y)^gamma e^{i(x -
  y)xi} = D_xi^gamma e^{i(x - y)xi}), which lowers its order by |gamma| = n + 1 and takes no derivative of l: Schur's
  test then applies uniformly, and D_a, D_b keep their form (noted at :1861).
- **(12) Minor counts (accepted).** "d = d-tilde + 3 >= 35" reads 36; c' >= 62 assumed D_0 >= 2 (Q5's d_0 >= 5);
  II.D's C^(d_0 - 3)/C^(d_0 - 4) multiplications (D_b + 4 = 68) now enter D_0's maximum (no effect); A.7 (1)'s cut-off
  and residual errors, if charged one change of chart, cost M_a + C_ch < M_2.4 (inside the maximum). dnumber5.out K6
  said D_0 comes "from the closed graph theorem": annotated as superseded.
- **(13) stage1cap5 S3 is print-only (accepted).** Its content is now computed in `classm5.py` K1-K2 (the criterion's
  reduction to M_22 at X*) and r7fixes5 R1; S3 stays a printed statement, labelled deduced there.
- **(14) "found independently here before the report arrived" (:1601) cannot be checked (accepted):** withdrawn.

### R8.1 (i) d as an integer (`modcount5.py`; `d0count5.py` corrected)

- *What a level does* (READ, I15:323-352; the ranges below are found by content and the files pinned by md5). III.I
  with fourteen primes, Theorem 3.1's Step 2, at each beta-level forms G~ = F - Delta_q(p') - R_q u (BG) and G' (rows,
  FIN) and applies to the same u III.I''''''''''''' Lemma 2.2 above 3 or III.I'''''''' Lemma 3.2 below 3. Lemma 2.2 is
  III.I''''''''''' Lemma 3.2's proof (I12:414-428) with III.I'''''''''' Proposition 3.1 at beta (I11:349-403) and
  III.I''''''''''''' Proposition 2.1 (I14:101-150 over I12:246-401, with I12's Lemmas 2.1-2.5, I12:110-236). Lemma 3.2
  below 3 is I9:239-342 with Lemma 3.1's Steps 1-2 (I9:219-234) and III.I'''''' Proposition 2.1's Steps 3-3.3 and 4-6
  (I7:190-333; its Steps 3.4-3.5 are replaced by I9's 3.4'-3.5').
- *The census* (READ; computed, M1). Every invocation in those ranges of a family J3 Lemma 2.1 lists (FWD, BG, the
  transforms and model inverses of (e)-(g)), of L-hat(sigma) or L_b applied, of the parts' own lemmas and of a routing
  citation is matched (212 hits) and classified: charged here (35 hits, 31 charges), counted in dnumber5's constant A'
  (10: the tf, level-2 and level-3 rounds, Step 0's III.A Proposition 4.2 (1), X_7, the windows and the iota+ loop,
  below 3 the one-off application), a statement or a lemma's own text charged where it is applied (129), FIN or INT
  of loss 0 (14), base level only (12), top level only (1), replaced at this use (2), routing to a scanned range (9).
  0 unclassified, no stale row. Controls: a row dropped leaves one hit unclassified (C1); the L-hat pattern dropped
  [R9, nit 5: classified per (line, tag); the four doubled hits are single applications, and "none left" means none
  left among the matched families (the verifier sorted the unmatched citations: none carries a loss).]
  loses 26 hits and four charges (C2); a range anchor one line off fails (C6).
- *The charges* (deduced from J3 Lemma 2.1 and LOSS-D 2b at each site; computed at dweights5 W1's weights, at the
  worst level of each range; every charge an upper bound, branches of a sum summed rather than maximised). Above 3:
  BG 2 + 2 (I15's R_q u and Delta_q; Lemma 3.2's (L - L_b0) u); III.I' Proposition 3.1 at I11's Step 1, the one-off
  application to the general class E^C_I, 2 (1 + J + L) = 48 (prop31loss5's chain on R1 with seven rounds; 12 on R0,
  30 with four, so the largest reading); III.I'' Lemma 4.1 (v_hi) 18 (II.G' Corollary 4.5 charged J3 (f)'s l + 1 = 11,
  l = 2 l_3 + l_4 + l_5 = 2 x 3 + 4 + 0 at output weights (3/2 - eps, 21/10, 21/10), s <= 3, r_in - r_out <= 2, N = 1;
  plus (2.25a) 1, (2.25b) 0, Corollary 4.2 (2)'s (2.3) 2, Proposition 3.5 (1) 2 and (2) 2); the zero-energy solves of
  levels 0-3, each III.H Proposition 3.2 (1) with III.A Lemma 1.4, which J3 does not list, charged 2 per application
  ((ceil(mu' - mu) + 1) applications): 7, 7, 5 and, at the levels above 4 only, 5; L-hat(sigma) in Lemma 2.2 at levels
  0-2 and in g_J above 4: 2 each; III.G'''' Proposition 4.4 at level 1, at the exponent 2, per (alpha_0, k): 3 (k_1(2)
  + 1) = 33 (dnumber5 K3's k_1(2) = 10; the constant reads level 2 per exponent, and level 1 is charged the larger);
  III.I'' Lemma 4.2 at level 3: (2.4) = 2; II.G' (2.26a) at Step 5 (iii): 4; III.A Proposition 4.2 (2) for the last
  level's column pieces (Lemma 2.4 at j = 3, plain weights, n_iota = n_K = 0): 3 + 2; III.I' Proposition 2.1 at Step
  7: 2 x (5 + 1) = 12 (dweights5's count, one step allowed for its Step 1). Sum 158. Below 3: BG 2 + 2; III.I'' Lemma
  4.1 (u_hi) 20 (l_5 = 1 there); (2.25a) 1; Steps 3.1 and 3.3: III.H Proposition 3.2 1 + L-hat 2, twice; Step 3.2's
  single Proposition 5.1 application 3; Step 3.4''s Lemma 4.2 2 (its rounds' row data are FIN, I7 Lemma 1.3); (2.26a)
  at Steps 4 and 5: 2 + 2; III.I' Proposition 2.1 at Step 8: 12. Sum 52.
- *FWD* (deduced; computed, `d0count5.py`, the verifier's A and A2). Proposition 2.4's count must cover the symbol
  orders at which the chain applies it, and round 7 took every operator order <= 2. The propagation estimates of II.A2
  sections 4-5 use commutants a-check of order s - 1/2 + delta (II.A2:641-668: b_eps of order s + delta, z_eps of order
  -(m - 1)/2, a-check = z b), s in [s_out - 2, s_in + 1] = [-10, 10], and their products and commutators with L
  (order 2); every symbol and composite order of the chain therefore lies in [-22, 22], and the count is taken with
  every order variable in that box. At the Sobolev orders [-16, 11] (Q4 with the record's input order -16):
  D_a = 53, D_b = 64, d_0(8.6) = 60; on the box M_a = 138 (J1 = 80), M_2.4 = 374 (C_ch = 218), M_f = 393 (Lemma A.9),
  D_0 <= max(M_2.4 + 6, M_f + 6, d_0(8.6) + 2, D_a + 2, D_b + 4) = 399 and D_1 <= 52 (d-tilde + 3 over [-16, 11]), so
  [R9, R9.0 M1: 435 and FWD <= 510 with the Peetre exponents over the factors' orders (18 for (b)-(e), 20 for (f)).]
  FWD = D_0 + D_1 + d' + d'' + 6 <= 474. On round 7's operator orders, corrected, D_0 <= 230 (203 without (f)); that
  reading is not the chain's and is not used.
- **Lemma A.9 (= II.A2 Proposition 2.4 (f) at its instances, explicit; deduced, counts computed).** Let T be a sum of
  compositions of Op(a_i) and adjoints whose smooth-symbol order is the product's minus q (q exact cancellations of
  main terms: adjoint defects and commutators), each factor passing through at most p binary operations. Then T has
  the order (f) states for a_i in C^(M_f) with M_f := M_a(t, mu) + p (q + 1 + max(2L, 2L')) + C_ch + 1, mu the
  composite order. *Proof.* Expand each operation to depth q + 1 by A.7 (2): the cancellations are identities among
  the main terms, symbol by symbol, as for smooth symbols, so what remains is a finite sum of main terms of order mu,
  bounded by Theorem A.1 after the conjugation by Lambda's (M_a), each having taken at most q more derivatives of a
  factor per operation, and remainders, each bounded by A.7's master estimate (3) with q + 1 + max(2L, 2L') derivatives
  of the factors it involves; one change of chart per factor (C_ch, A.8); the +1 is (d)'s Hamilton term. At
  [R9, R9.0 M1: max(2L, 2L') here is A.7 (3)'s Peetre exponent for a factor differentiated to depth q + 1, maximised
  over the factors' orders (s - 1/2 + delta in [-10.49, 9.51]): 2L' = 20 at q = 3. Nit 6: (f) is also used at
  II.D:198 (q = 1), dominated by the II.A2 count.]
  II.A2:682-695, q <= 3 ([[D_a, A-check], A-check] and i[L_R, D_a-check A-check] with D_R inside L_R) and p <= 3. []
- *The steps outside the levels* (deduced on a coarse reading; computed, M4). III.I with fourteen primes, Theorem
  3.1's Step 0 (FWD), Step 1 (the base level: III.I'''''''' Proposition 4.1 at alpha_1, Lemma 3.1 with III.I'''''
  Proposition 2.1's rounds and at most one Lemma 3.2), Steps 3, 4' (FIN) and Step 4 (III.I'''''''''''' Theorem 3.1 at
  the top, whose Step 0 runs one more level's maps and whose Steps 1-6 subtract towers and read coefficients) are not
  in A' + (K + 1) c', a term round 7's chain omitted. Each is at most one level's composition with its loops, the base
  [R9, minor 1: itemised in R9.1 (the top's Step 1 (vi), (viii), (ix) apply III.A Proposition 4.2 (2) three times):
  B_once = 3,943,746,411.]
  at most four levels below 3: B_once := 2 (M_a + 4 M_b) + 1000 = 3,524,217,980, M_a = 1,042,275,846 and M_b =
  179,958,161 the largest totals of one level (the per-level maxima of the rounds at W1's weights, P_W, P_iota, W, the
  excess 47 and X_7(alpha) = 352,162,875, read from dnumber5.out, pinned). It is 7.7e-8 of d.
- **The integer** (deduced on the reading; computed exactly). c'_above = 474 + 158 = 632, c'_below = 474 + 52 = 526,
  c' = 632; with A' = 45,661,383,902,649,727 (dnumber5, R1, the wide E_col reading) and K + 1 = 106,489,470:

      d <= A' + (K + 1) c' + B_once = 45,661,383,902,649,727 + 67,301,345,040 + 3,524,217,980
        =  45,661,454,728,212,747   (4.5661455 x 10^16),      N = 21 d + 6 <= 958,890,549,292,467,693 (9.588905 x 10^17).
  [R9: with R9.0 M1 and minor 1, d <= 45,661,458,981,362,098 and N <= 958,890,638,608,604,064 (R9.1).]

  The floor at the same point is 8,407,505,890,317,054 (0.184 of the bound). The reading is: round 5-6's step-by-step
  log orders of E^flat (a deduced ceiling: the write-out states only K(lambda), I11 Proposition 3.1 (c)), the
  construction's E_ind, III.C' (3.1) as written (R1), one level-2 application per exponent, the wide E_col, the
  weights of W1 (four admissibility conditions undecided, 2.1), the order box above and the charges as listed, every
  one an upper bound. Each figure moves only by its own term: the MODs (158) and FWD (474) together move d by 1.5e-6 of
  itself.
- *What is not a number and why it does not matter here.* Nothing in d's chain is now symbolic. What separates the
  integer from a theorem about the write-out is the reading, not a missing count: the log-order ceiling holds on the
  step-by-step reading of I11:352-387 (round 6's M2: a sharpened I11 Proposition 3.1 (c) written into the write-out
  would make it a statement of the write-out), and the order box and the coarse one-off reading are generous by
  choice. None of these is an obstacle to the integer bound; they are the reading it is deduced on.

### R8.2 (ii) lambda0, stage 1: the enclosure attempted (`classm5.py`)

- *The input is one number* (computed, exact, K1-K2). In the class, m_1(X*) e_phi1 = M_22 e_phi1, M_22 :=
  (m_1)_phi1phi1(X*)/a^2, and e2 is an eigenvector of g_1(X*, s) for every s; so sup_s |g_1(X*, s)|_op >= (4/3) K +
  |M_22| (deduced), with (4/3) K >= [12.5934637 +/- 2.51e-8] (READ r7fixes5). A certified enclosure [lo, hi] of M_22,
  0 not in it, would give C_app >= 12.593309 + min(|lo|, |hi|) and multiply the operator-norm bound 0.0024433 by
  12.593309/(12.593309 + min(|lo|, |hi|)) (K4: 0.9921, 0.9264, 0.7158 at 1/10, 1, 5).
- *The validated solve, step by step* (deduced; what each step needs, READ N1STAR-PROOF.md Lemmas 5.3, 6.2, 6.4, by
  content; D623 did not change them). (S1) The data on Sigma: Lemma 6.2 (iii) at m = 1 is the linearised constraint
  system P(h_1, Q_1) + B_1(h_1) = S_1, solved by Lemma 6.4 from zero data at r = a, with h_1 = a_1 dr dr, phi_1 = 0,
  (m_1)_{tau .} = 0. S_1 and B_1 are the order-1 means of the constraint map at the approximant's slice data: a
  second-order two-scale expansion of (J, rho), one order beyond data5.py. (S2) The evolution: Lemma 5.3 (a)-(c) at m
  = 1 on the past of X* in Omega (tau from -2 to tau* = 2 - a; v <= 2, so only the shell's half [1/2, 2] is a source):
  the mean's eight class components coupled by box~ (componentwise in Cartesian components) and by B-bar, C-bar, with
  phi_1, Psi_1 = box~ phi_1 and Z = d_th gh_2 transported along ell, the source S_1 nonzero only in dv dth (stage5.py
  S2). (S3) The error control: an approximate solution with residual rho is within C ||rho|| of m_1 in the energy norm,
  C the stability constant of (S2), and M_22 is a point value, so a higher-order energy and a Sobolev embedding enter.
- *Which step fails, and why* (computed, K5; deduced). (S1) fails first: neither the record nor this supplement has
  S_1 or B_1 in closed form or in a program, and without them (S2) has no data. With them, (S3) fails on what the
  record provides: its only stability constant for stage 1 is Lemma 2.3's energy estimate, whose rate for the principal
  part is kappa <= 13.2197 (stage1rate5 K3), so over X*'s past (Dtau* = 4 - a = 3.7301412) the growth factor alone is
  <= 5.103 x 10^10 (certified, K5): an a posteriori (Newton-Kantorovich) closure would need the residual of an
  approximate solution of the coupled 2+1-dimensional system below about 2 x 10^-11 |M_22| in the energy norm, before
  the lower-order coefficients' sup norms (not computed: round 6's minor 9) and the Sobolev constant of the point
  evaluation (Lemma 6.4's at s > 7/2, which contain the Moser and Kato-Ponce constants on S^3, not numbered in the
  record) are added. And m_1 depends on the envelope beyond its integral (its source is quadratic in the wave, whose
  amplitude carries env), while the numerics' sin^4 envelope is C^3 and not admissible (1.1): a value of M_22 exists
  only for a chosen smooth envelope, and the lowered bound would be a statement about that envelope, not about P* as
  [R9, minor 2: the certified bounds are themselves statements about one smooth envelope, round 2's (envelope5.py,
  with the numerics' integral): C_app goes through its peak c (lzerotrace5's K_lo = c_lo a^(-3/2)), not only through
  int env^2. So M_22 is to be enclosed for that envelope too.]
  the certified leaves are. No ball or interval method was run: there is no system to enclose until (S1) exists.
- *The single missing input* (deduced). A certified enclosure, excluding 0, of the one number M_22 = (m_1)_phi1phi1(X*)
  /a^2 for a fixed smooth envelope with the numerics' integral. Nothing weaker suffices (R7.3 (a)-(d), sharpened by K2):
  with M_22 free the operator-norm bound at X* is exactly sup |W_TT|_op; an upper bound on m_1 cannot raise a lower
  bound; and the Sigma data alone would need |a_1| > 12.37 (K3). The Frobenius bound 0.0019079 already moves for every
  m_1 (round 7); the largest-entry bound 0.0012228 needs the same M_22.

### R8.3 (iii) the scalar-type blocks of L-hat_b0(0) (attempted; not obtained)

- *What was tried, and where each route stops* (deduced; READ lin5.py's definitions, round 7's block structure). The
  s0 block (four radial functions) on the complement of its state and the s_l blocks (seven) carry L_b's gauge terms
  E^C w = gam_C (2 c (x)_s w - m (1 - e_C) g <c, w>), c = r^-1 (dt - v dr), gam_C = 10^6, applied to Ups(h) =
  delta_{E^Ups} G h, which is first order in h and couples the components at one angular derivative, sqrt(l (l + 2)).
  (a) A quadratic form with the multiplier of zeroext5 (w = r) and the Hardy bound, for large l: the gauge coupling is
  not symmetric and its coefficient is gam_C = 10^6 against the angular term l (l + 2) r^-2, so such a form can only
  start at an l that grows with gam_C; that threshold was not computed (the block operators at symbolic l were not
  reached in this round's time: lin5.py's indicial computation at one numeric l did not finish in ten minutes), so no
  large-l statement is made. (b) Interval Galerkin with a residual bound for each l below such a threshold: a certified
  lower bound for the singular values of a non-self-adjoint 7 x 7 system on [r_h/2, oo) in (3.2)'s b-weighted norm,
  per l. Not run. (c) The factorisation round 7 named: with Ups :=
  delta_{E^Ups} G h, the linearised contracted Bianchi identity at the Ricci-flat b0 (delta G D Ric = 0; standard, not
  computed here) gives 2 delta G L_b0 h = box^C Ups
  (box^C := 2 delta G delta*_{E^C}, lin5.py's definition), so L_b0 h = f gives Ups = (box^C(0))^-1 2 delta G f, then
  D Ric(h) = f - delta*_{E^C} Ups (the static scalar-type master equation of Kodama-Ishibashi type at zero frequency)
  [R9, nit 9: that equation is gauge-dependent; it "reduces to" the static master equation, not "is" it.]
  and h's gauge part from (1/2) box^Ups(0) omega = Ups - Ups(h_RW): three inverse bounds (box^C(0) and box^Ups(0) on
  scalar-type 1-forms, the static master operator), each per harmonic, with the composition constants of delta G,
  delta*_{E^C} and the reconstruction in the norms of (3.2). The gam_C-dependence then sits in box^C(0) alone. This is
  a route, not a result: none of the three is certified here.
- *The single missing input* (deduced). Unchanged from round 7: a lower bound, uniform in l, for sigma_min of the
  scalar-type blocks of L-hat_b0(0) in (3.2)'s norm (s0 on the complement of its state, s_l at every even l >= 2).
  Nothing weaker suffices (R7.4, Schur's lemma: L-hat_b0(0) commutes with SO(4), the norm is SO(4)-invariant, so the
  inverse's norm is the largest block's). Route (c) is a sufficient decomposition, not a weaker input: it replaces the
  one bound by three, each again uniform in l. With the tensor blocks' 3.939 (round 7) it would give
  ||L-hat_b0(0)^-1|| in the class.

### R8.4 (iv) the next inverse bound: which, and why it is not done

Of the six (I.B:1513, :1685, :1978; III.F'':223; III.D:365; II.F:1393), the closest to done is I.B:1978, the
middle-range resolvent ||P-hat(sigma)^-1||: E2-PILOT certifies ||chi_I R_l(sigma) chi_I|| <= 11.477 for the scalar wave
on 3 <= sigma <= 384 with H^1 bounds for every harmonic (round 3, R3.4), so of its three pieces (the trapping
neighbourhood, the horizon, infinity) one is certified for the scalar model. What stands between that and I.B:1978's
constant is the same as for the others, R7.4: the radial-point and propagation estimates' constants at L_b0 near the
horizon and infinity, in the write-out's variable-order norms, and the passage from the scalar wave to the full
linearised operator. Not attempted this round: items (i)-(iii) and the verifier's report took the round.

### R8.5 Proved, computed, open

- *Computed, exact*: the class reduction m_1(X*) e_phi1 = M_22 e_phi1 and the eigenvector at X* (classm5 K1-K2); the
  angular maximum of W_TT (K3); the census of 212 per-level citations (modcount5 M1); the four counts of d0count5 at
  each order range, with pins.
- *Certified*: sup_Sigma |W_TT|_op <= 0.22189; the amplification 5.103e10 over X*'s past (from stage1rate5's kappa);
  r6fixes5's coefficient now printed outward-rounded, < 3.5243e17.
  [R9, minor 4: printed 3.5242e17 until this round; now 3.5243e17, rounded up.]
- *Deduced (counts computed)*: Lemma A.9; D_0 <= 399, D_1 <= 52, FWD <= 474 on the order box; the 31 charges of a level
  [R9: D_0 <= 435, FWD <= 510, c' = 668, B_once = 3,943,746,411, d <= 45,661,458,981,362,098 (R9.1).]
  (158 above 3, 52 below), c' = 632, B_once = 3,524,217,980; **d <= 45,661,454,728,212,747 and N <= 958,890,549,
  292,467,693, deduced on the reading R8.1 states.**
- *Withdrawn*: D_0 <= 177, FWD + BG <= 250, c' in [62, 250 + MODs], "C_app >= 16.127553" (read 16.127552), the stage-1
  excess for general M (not needed in the class), "it cannot decide", "final beyond stage 1" (method-relative), "found
  independently".
- *Open, each with its single missing input*: lambda0's value or a lower certified bound from stage 1 (a certified
  enclosure of M_22, for a fixed smooth envelope); I.C:497 for L_b0 (the scalar-type blocks' sigma_min, uniform in l);
  the other six inverse bounds (their microlocal constants at L_b0 and certified spectral bounds in the write-out's
  norms). d is no longer open as a number; as a theorem about the write-out it rests on the reading above.

### R8.6 Sources (round 8)

The round-7 verifier's report and scratch (`report-vD7.md`, `vD7/`); the coordinator's notes on D623. N1STAR-PROOF.md
read by content (0.3's eps1 sentences, Lemma 2.3, Lemma 2.4, Lemmas 5.3, 6.2, 6.4; md5 9e5363f1... at the end of this
round, not pinned). proof5 (md5s pinned in modcount5.FILES and d0count5's sources): PART-III-I15-AUGMENT5.md:253-452;
PART-III-I14-LEVELS.md:93-188; PART-III-I12-SPECTRAL.md:110-436; PART-III-I11-SPACETIME.md:260-403;
PART-III-I13-EXPANSION.md:224-447; PART-III-I9-COMMOTION.md:195-345; PART-III-I7-PARAMS.md:143-333;
PART-III-I6-ALMOSTBDD.md:85-227; PART-III-I3-ALMOST.md:216-300; PART-III-I2-SCRI.md:56-235; PART-III-J3-TAME.md:88-300;
PART-II-G2-DECAY.md:422-540, 760-870; PART-III-A-PREREQ.md:160-200, 563-580; PART-II-A2-STANDARD.md:230-306, 640-700;
LOSS-D.md sections 1-3 and LD16; stage5.py, lead5.py (READ, the class and W_TT); checks imported, not copied: dweights5,
prop31loss5, d0count5, dnumber5, stage1cap5.

### R8.7 Proposed replacement for the paper's section 9 constants text (replaces R7.7)
[R9: superseded by R9.7 (the round-8 verifier's MAJOR 2 and minors 2, 3, 5).]

Three old/new pairs. Each old text occurs exactly once in paper/RESPONSE-HL-5D.md as it stands (checked by content when
this round ended); the new texts claim only what R8.1-R8.4 prove or compute, with their statements, and fold in the
round-7 verifier's B (no "only through", no calculus bound "in the supplement", "for one choice of generators" kept).

1. Section 9, "Settling", the loss d (old: the last sentence of the d passage).

```old
Still open: numbers for the
  weights the write-out chooses under its inequalities (ℓ_I among them), the logarithmic terms of one index set, the
  count of one regularity step beyond its floor, the loop counts themselves, and the evaluation of the recursion that
  composes them (`LOSS-D.md` section 4; the logarithmic terms and the regularity step, its finding LD16); so d is still
  not a number.
```

```new
That bookkeeping has since been
  carried to an integer (supplement `docket68/n1star/CONSTANTS5.md`, rounds 1–8): the weights are taken at a point
  meeting every condition decidable there, the loops are counted exactly over the write-out's 1.065 × 10⁸ levels
  (`checks/dnumber5.py`, `checks/x7indep5.py`), every fixed step of a level is read at its source and charged an upper
  bound (`checks/modcount5.py`: 212 citations classified, none left), and the coefficient orders the write-out fixes by
  the closed graph theorem are replaced by explicit calculus estimates whose derivative counts are computed over a box
  containing every symbol order of the chain (`checks/d0count5.py`). On that reading d ≤ 45,661,454,728,212,747 ≈ 4.566 ×
  10¹⁶ and N = 21d + 6 ≤ 9.589 × 10¹⁷ (deduced on the reading, the arithmetic exact), 5.4 times the floor at the same
  point. One step of the reading is the supplement's, not the write-out's: the logarithmic orders of one index set are a
  ceiling deduced step by step from the proof of the write-out's coarser bound. So the integer bounds the loss this
  proof's bookkeeping produces on that reading,
  not the optimal loss.
```

2. Section 9, "Settling", lambda1 and delta (old: the bullet's last sentence).

```old
The passage to the write-out's own function spaces and the
  other constants are not done, so λ1 and δ are still not evaluated.
```

```new
The passage to the write-out's own function spaces and the
  other constants are not done, so λ1 and δ are not evaluated: what the proof's own formulas deliver is bounded above,
  log₁₀ δ < −7.66 × 10¹⁶ and λ1 < δ (computed, `docket68/n1star/checks/deltacap5.py`), and no lower bound follows. Of
  the seven inverse bounds a lower bound needs, the zero-energy one is proved for the scalar model (constant 2.81) and
  for the tensor-type blocks of the linearised operator in the symmetry class (constant 3.94), every harmonic, through
  the horizon, in the supplement's norm for one choice of generators (deduced, with certified arithmetic,
  `checks/zeroext5.py`, `checks/tensorzero5.py`). For its scalar-type blocks, whose gauge-damping terms neither vanish
  nor are symmetric, the one input missing is a lower bound for their least singular value, uniform in the harmonic;
  the other six need the constants of the write-out's microlocal estimates at the final black hole and certified
  spectral bounds in its norms (supplement `CONSTANTS5.md` R8.3-R8.4).
```

3. Section 9, "Physical wavelengths", lambda0 (old: the bullet's opening words, to the line's end).

```old
λ0 is not evaluated, and a high-frequency theorem, whose expansion parameter is λ over the
```

```new
λ0 is not evaluated. The threshold the proof of Theorem 1 delivers is traced term by term
  (supplement `docket68/n1star/CONSTANTS5.md`): at the numerical point, with a smooth envelope of the numerics'
  integral, it is below 0.0025 in the operator norm, 0.0020 in the Frobenius norm and 0.00123 in the largest entry
  (certified), so the wavelength 10 l5 lies more than 400 times beyond it. A value, or a lower certified bound, needs
  the approximant's linear stages solved. The first can lower the operator-norm bound, for example through its mean
  correction at the point where the first-order wave is largest, which the symmetry class reduces to one number
  (computed, `checks/classm5.py`); a certified value of that number needs a validated solve of the first stage for a
  fixed smooth envelope, whose data on the initial slice are not computed. And a high-frequency theorem, whose
  expansion parameter is λ over the
```

Statuses behind the new texts: d's integer, deduced on R8.1's reading with exact arithmetic (modcount5 12/12,
d0count5 18/18, dnumber5 10/10, x7indep5 9/9); the floor, computed (dweights5 W3); delta and lambda1's upper bounds,
computed (deltacap5); the zero-energy constants, deduced with certified arithmetic (zeroext5 10/10, tensorzero5
11/11); lambda0's three bounds, certified (lzerotrace5 T7, r7fixes5 R2, r6fixes5 F1; eps1 < s0 as N1STAR-PROOF.md
0.3 now states); the reduction to one number, computed exactly (classm5 9/9).
