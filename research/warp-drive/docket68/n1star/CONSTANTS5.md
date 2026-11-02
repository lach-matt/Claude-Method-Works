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
  explicit minimum of eight closed-form terms (section 1.3, checked `lzeroconst5.py` Z4). At the paper's numerical
  point its geometric leaves are certified (lambda_Omega <= 0.026986, tau_end - tau0 <= 5.937209, eps1 >= 5.2617e-4,
  C_S <= 43.216); **no number for lambda0**: its other leaves are bounds on the approximant's profiles of stages 1-10,
  which nobody has computed (section 1.5). The same audit settles EFFECTIVE-CONSTANTS.md E5's first item: C_J and
  lambda_1.1 of PART-VII Lemma 1.1 are the same theorems at order k = J + 4, so they are constructive too.
- **d.** The weights now have numbers (section 2.1); (G) is checked against the generators pi_1 E^C_I and does not bind;
  at these weights the loops are counted exactly and **d >= 8,407,505,890,317,054** (computed, `dweights5.py` W3). Two
  of LOSS-D's open items are closed: the data's E^C_I **does carry logarithms below l_I** (the assembly's E_0 =
  {(j, 0) : j >= 2} meets E^C_I at 2 and 3), so the one-off application costs 12, 30 or 48 by reading, not 6 (W5); and
  III.I' Proposition 2.1 takes **5 steps, loss 10**, one above its floor (W6). The level-2 container grows to 53,496,063
  points per level once E^C_I's chains are counted, so LD15's comparison cannot show that loop shorter (W4). The
  composition gives **d <= 1.8127e16 + 1.0649e8 c** on hypotheses H1-H4, c the uncounted per-level loss (W8): a
  conditional bound, not a certified one. The exact obstructions are in section 2.6.
- **lambda1 and delta.** No quantitative replacement is computed here. Each of the 35 non-effective rows has its
  replacement and the precise missing input (`nrows5.py` R1); a fifth kind the ledger's census did not search, bounds
  from the closed graph, open mapping and Banach-Steinhaus theorems, occurs at 16 lines of proof5, 13 of which carry a
  constant (R2); and the replacements must be built in a fixed order, the covering and calculus constants first (R3).
  Upper bounds are certified: **log10 delta < -7.666e16 and lambda1 < delta**, from the proof's own formulas, with the
  upper-bound constants taken >= 1 (`deltacap5.py`).

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
  factor above 18.5 (37 at a = q0/2), before any profile enters. This agrees with the paper's section 9 and is now a
  certified statement about Theorem 1 itself.

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

d1 = lambda_s1,2 - 2 is taken in a certified rational interval of width 3e-57 (and is irrational, z^2 + 4z + 16 not
being a rational square). With the increments d1 and 1, the chains of {lambda_sharp, 2, 3} come nearest to (2, 2 +
eps_K] u (3, 3 + eps_K] at 3 + 5.0191e-8, from lambda_sharp + 4,470,304 d1: LOSS-D LD9 G7's value, reproduced. The
least E^C_I of III.C Definition 3.1, which every admissible E^C_I contains (Definition 3.1 (3) forces 2 + s + s'),
adds 24 chains (26 points below 3); none comes nearer, their residues sitting near d1/2 and 3 d1/4 because 1/d1 =
3,000,002.5... So E^C_I, one of the four generators LD9 left unlisted, does not make (G) bind, and eps_ind stays the
binding cap on eps_K at the record's point.

### 2.3 The loop counts and an exact floor (computed, W3)

The beta-chain has K = 106,489,469 levels (53,244,734 below 3, 53,244,736 above, the top included). Summed exactly by a
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
above 3 is 7,470,307 for the named generators (LD15, reproduced) plus 46,025,756 from E^C_I's 24 chains, **53,496,063,
2.03 times a level's mean level-3 rounds** (2.6317e7): LD15's route (the container shorter than the level-3 loop when
the unlisted generators add at most six chains) is closed in the negative by E^C_I alone.

The composition (1.1) over the levels, on these hypotheses:

- H1: at each level above 3 the level-2 loop makes one application per exponent of Lambda cap W (LD16's
  redundancy-free reading), and E_++, G, E_col add no point to W;
- H2: the iota+ loop at its ceiling at each level below 3, 15 per round (the construction's reading, m_iota = d1);
- H3: at each call of III.I''''' one round raising alpha'_K, Proposition 2.1's 10 and the one-off application's 48;
- H4: III.J''s charges, and every other step of a level lumped into one unknown c,

gives **d <= 18,126,947,816,279,750 + 106,489,470 c** (computed, W8: rounds 8.408e15, level-2 container 8.545e15,
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
Banach-Steinhaus theorem, none among the ledger's N-rows; 13 carry a constant: II.A:960, 986, 1538; II.A2:130, 188,
276, 281, 811 (the calculus); II.F:1400 (open mapping, beside the N1 row 1393); III.H:425 (Banach-Steinhaus, locally
uniform in sigma); III.I''':274; and III.J'':41, 82, where the closed graph theorem gives the tame constants C_k of
every membership statement (Lemma 1.2 (f)). These enter lambda1 and delta through the tame constants. Their
replacement is to read each bound off the proof of the membership statement it concerns, which is a chain of explicit
estimates; that is not done. (The losses, and so d, are not affected: a membership statement fixes its loss by its
orders.)

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
  (2.2); K, R2, R3 and d >= 8,407,505,890,317,054 (2.3); the losses 12/30/48 (2.4); the container 53,496,063 (2.6).
- *Conditional, not proved*: d <= 1.8127e16 + 1.0649e8 c on H1-H4 (2.6).
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
