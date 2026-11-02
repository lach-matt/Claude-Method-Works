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
  within eps1/2), |w| <= eps2/2 for Step 8's cut-off, and |dw| <= 2 C_dw M lam^(K-4) <= 1 so that M1 does not depend on
  M. Step 7 needs C3 C_N M^2 lam <= 1. Proposition 6.5 needs the frozen coefficients within their margin, 2 C_c C0
  lam^(N-3) <= m_c, and the contraction factor C_k lam^(N-3) <= 1/2; Lemma 6.3 (c) needs the signs of alpha and S A0,
  C_s lam <= m_s. Here C_inf, C_dw are C_S times Step 1's constant, C2 the constant of Steps 4-6, C_st Step 2's, C_N the
  nonlinear one, C_R and C_D those of (E3) and (E4).
- *Z4 (computed, floating point).* On 400 random inputs the closed form meets every condition at lambda0 and fails one
  at lambda0 (1 + 10^-6); without its Step-7 term it violates a condition on 341 of them (control).
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
  sufficient, not sharp.
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
valid at every admissible weight (eps_K, eps_ind taken up to delta_50); this is its exact value at one admissible point.

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
iota+ 1.174e15, the rest 3.1e9). This is conditional. The exact obstructions to a certified upper bound:

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
  (computed, exact; round 1's 5.2617e-4 is valid but 1140 times smaller). Certified bounds to order 14 on every
  derivative of the explicit profiles: the wave W_TT, the second harmonic chi dv dv, and the stage-1 mean source S
  (computed). Every admissible C_app is at least 12.58, so **the lambda0 this proof delivers is at most 0.0239** at P*
  with this envelope (computed), below lambda_Omega. Lemma 2.4's factor for Step 6's transport is e^44.0 = 1.29e19 as
  the proof derives it (computed). **Stage 1 itself (m_1, phi_1, gh_2) is not bounded**: the exact cost is in R2.2.
- **(ii) d.** E_++ and G add no chain to Lambda (deduced; computed check). E_col's candidate bases, under the widest
  reading, are 11 (computed): they do not make (G) bind, though the nearest comes within 2.2 % of delta_50 (certified),
  and they lengthen the level-2 container to 85,025,783 per level. The windows of III.I'''''''''' Proposition 3.1 run
  at the levels above 3 too, and Lambda_* and the "pairs removed" cost no derivative (deduced). The conditional bound
  becomes **d <= 2.4338e16 + 1.0649e8 c** on widened H1-H4. **No proved upper bound**: it is blocked first by Lambda's
  increments, pi_1 E^iota_ind and the full root list of E_ind, which the record never lists (R2.3).
- **(iii) lambda1, delta.** The covering counts of I.A section 7 and II.D:1032 are explicit on the model, and two of the
  three coverings are not needed (an exact escape function and an exact time function) (computed). The 18
  closed-graph-type sites: 1 effective as written, 6 by a calculus estimate, 2 by reading chained proofs, 1 given a
  base inverse bound (explicit Neumann series), 1 of the N1 kind (computed classification, deduced replacements). No
  number for lambda1 or delta.

### R2.1 The verifier's findings on round 1 (commit 72850e1), folded in

- **V-M1 (major), `dweights5.py`:336.** Wrong: the E^C_I chains were taken as the least E^C_I minus {lambda_sharp, 2,
  3}, but lambda_sharp + 1 = 2.5099 is both a chain start (a named generator plus 1) and a point of the least E^C_I, so
  its 1,470,302 points per level were counted twice. Corrected (computed, `dweights5.py` W4, control N5 on the
  deduplicated union of the 27 chain starts): **52,025,761 points per level, 1.98 times** the level-3 rounds (not
  53,496,063 and 2.03), from **23** further chains (not 24), and **W8: d <= 17,892,090,290,788,934 + 106,489,470 c**
  (not 18,126,947,816,279,750). The verifier's figures, reproduced. The conclusion that the container is longer than
  the level-3 loop survives. Round 1's lines 24-25, 160, 214-216, 226 and 291 carry the correction.
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
  paper prints d > 7.95e15 (RESPONSE-HL-5D.md:1390, 1758, READ); 7.959e15 is LOSS-D's sharper form of the same floor,
  which round 1 quotes under LOSS-D's name (`deltacap5.py`, 3.3); both stand.
- **Found here.** Round 1's eps1 is valid but not the right measure (R2.2 (b)); round 1's 1.5 "a nine-stage linear PDE
  solve" stands, with the cost now made specific (R2.2 (f)).

### R2.2 (i) lambda0

(a) *The envelope* (computed, `envelope5.py` E1-E3). env(v) = c cos^12(pi y/2) exp(-y^2/(1 - y^2)), y = (2v - 4)/3, on
[1/2, 7/2]; c in [1.3240711, 1.3241035] makes int env^2 = 105/128 exactly, so mu_end = 227/192 and every leaf of 1.4
stands. Certified e_k = sup|env^(k)|, k = 0..14: 1.324, 3.077, 18.6, 95.75, 739.5, 5166, 4.611e4, 3.841e5, 3.780e6,
3.539e7, 3.733e8, 3.796e9, 4.214e10, 4.552e11, 5.248e12 (interval Taylor arithmetic in a centred form; the end
intervals by the exact derivatives of exp(-1/(2t))). Within a factor 2 of sampled values at every order (control C2).
The plain bump exp(1 - 1/(1 - y^2)) gives e_11 about 3.6e22: the cos^12 factor buys twelve orders of magnitude.

(b) *eps1* (computed, exact, `eps1hyp5.py` H1-H3; deduced H2). Lemma 1.1 (e)'s conditions are that Sigma_tau, {r = a}
and the outer boundary stay spacelike, i.e. that g restricted to ker dtau, ker dr, ker d(v + tau) stays positive
definite. On those hyperplanes, in Euclidean-orthonormal bases, g0 has least eigenvalues 1, min(1, mu/a^2 - 1) = 1 and
(3 + mu/r^2)/5 >= 3/5. So **every eps1 < 3/5 serves** (the time orientation and the causal containment follow along
g0 + t(g - g0)), and the perturbation -lambda n n^T at r = 67/5 on the outer boundary (norm 0.6013169, exact) makes it
null: **eps1* in [3/5, 0.60132]**. Round 1 went through |g^-1 - g0^-1| <= n^2 eps with n = 33.47, which cost the factor
1140. In lambda0's formula, eps1 enters E-a and E-b; Lemma 2.3's constants degrade as eps1 approaches 3/5, so the
choice is a trade-off the formula does not yet resolve.

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
eps1 (the lambda0 of this proof, V-M2; with this envelope).

(d) *A stage-independent constant* (computed, `gronwall5.py`). Lemma 2.4 gives C = sup|c|; for Step 6's transport c =
2/r <= 2/a, so its factor is **exp((2/a)(tau_end - tau0)) = 1.288e19 = e^44.00**, and C3 = C_st C2 e^(C2 (tau_end -
tau0)) (1 + ...) carries at least that, as Steps 6-7 derive C2. Along L0 the equation's own growth is (r(tau0)/r)^2 <=
(b(tau0)/a)^2 = 2479: a weighted energy would remove 5e15 of it (deduced; not a repair of the proof).

(e) *Stage 1, as far as it went.* Its explicit inputs are now bounded: the coefficients built from W and chi, and the
mean source S (the stage-5.py S2 source, a dv dth component only). Not bounded: the oscillating part of R^(1)[g0 + lam
W] (nonzero in seven components, `stage5.out` S4), the linear operator's coefficients B-bar, C-bar, Mm, Wm (structure in
`stage5.py` S1, coefficients not extracted), the data (h_1, Q_1) of Lemma 6.2, which solve Lemma 6.4's radial
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
per transport, 1e24-1e26 for the order-11 profile bounds at stage 0), the number lambda0 would come out is already
below e^-130 from (d) alone if C2 >= 2/a enters to the third power (1/(C3 C_N M^2), M >= C3) and C_N >= 1; that last
step assumes C_N >= 1, which is not shown, so it is recorded as an estimate, not a bound.

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

(b) *The 18 closed-graph-type sites* (computed classification, deduced replacements, `baire5.py` K1-K4).
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
  12.58, lambda0 (this proof) < 0.0239 (R2.2 (c)); e^44.00 (R2.2 (d)); (G) unbound at 3 + 1.9841e-8, the container
  85,025,783 (R2.3 (b)); N(I), H r = 2f, H log tan(phi/2) = -2 sigma0, lambda_L^2 = 1/(2 mu) (R2.4 (a)); the
  verifier's corrected figures (R2.1).
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

N1STAR-PROOF.md:143-235, 339-450, 509-532, 624-662, 697-791; RESPONSE-HL-5D.md:286-288, 1390, 1758; proof5:
PART-I-SPECTRAL.md:60-139, 1384-1404, 1463-1712; PART-II-D-REGULARITY.md:1015-1043; PART-III-I9-COMMOTION.md:28-66;
PART-III-I11-SPACETIME.md:28-166, 340-390; PART-III-I12-SPECTRAL.md:55-110; PART-III-I13-EXPANSION.md:222-266;
PART-III-I2-SCRI.md:177-195; PART-III-I8-UNPARAM.md:35-45; PART-III-J2-LINEAR.md:18-30, 95-145; the 18 sites of
`nrows5.py`; `lead5.py`, `checks/stage5.py` and `.out`, `checks/gapsums5.py` (the sl roots' formula), `prop31loss5.py`.
