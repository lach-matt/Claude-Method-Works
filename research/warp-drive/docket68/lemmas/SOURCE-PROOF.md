# SOURCE: the complete proof of its computations (SOURCEs and SOURCE; items 485-538)

*First written* 2026-10-20, on M's item 538: "anything COMPUTED-THEORIZED should have a complete proof for the
computations". SOURCEs and SOURCE are COMPUTED-THEORIZED since 534. This file proves every computation they name, from
the instruments that compute it: reader A1-D5, emitter_process A1-D4, hf_limit5 H1-H6, hf_core5 C1-C5, hf_theorem5
F1-F7, seed_escape E1-E5, seed_types T1-T7, seed_derive D1-D7, seed_second Q1-Q6.

Labels:
- proved: a complete argument here;
- computed (exact): an instrument's symbolic identity;
- computed (numerical): an instrument's numerical result, with its method, its error control and the margin by which
  it clears what it must clear;
- READ: a source read at the passage quoted, in the instrument named;
- criterion: an order-one physical criterion, not a theorem;
- M's: a ruling.

## 1. The theorem

**THM-SOURCE.** For a README of N bits in the theorem's domain (N >= 7.12e9), with r_h and E5(N) the corridor's
(G1, G3), there is a source that:
1. reads the object into the README exactly (the device);
2. emits E5(N) as a round null shell of the bulk's own gravitational waves, carrying none of the README, arriving at
   once across the face's 3-sphere, at rest;
3. delivers that energy into the README's hole to within half a bit, (1/2) k T_H ln2, the seed included.

The README's bits then cross by the plane's own channel during the write (WRITE, passage_est), and position 2
recovers them exactly (R1, r1_exact). Those are other rows' computations and are cited, not re-proved.

**Hypotheses.** General relativity in five dimensions (the bulk's Lambda is negligible at the hole's scale,
r_h/ell = 8e-16 at the small end). Quantum mechanics. M's rulings 130, 136, 146, 147, 162, 386, 432 (2), 438, 491, 508
and 509.

## 2. Part A -- the read (reader)

**A1 (the definition; proved, computed exact).** R = encode o measure.
- *measure* is one projective measurement of the labels of the object's last state (438): each site's Z, occupancy,
  bonds, defects; no isotope (438), no motion (147).
- *encode* is ENCODE's canonical Elias-gamma code. Elias-gamma is a prefix code on the positive integers, so a
  concatenation of codewords decodes uniquely. The labels are written in a canonical order fixed by the graph alone
  (encode_labels C1-C6), so R is injective on label graphs and independent of the order in which the atoms are met.
  Decoding returns the same graph (checked).
- N = len R(object). The computed N: water 22, ethanol 79 against dimethyl ether's different 79, a perfect copper
  cm^3 174, a 99.99 % piece 1.3e21 (estimate).

**A2 (the start; proved).** E5 is proportional to r_h^2 and N to r_h^3, so E5 is proportional to N^(2/3) and
dE5/dN = (2/3) E5/N > 0. E5 is therefore fixed only once N is, and the read completes before the opening (162: the face
takes the size that holds the README). The order is: choice (130), read, opening, write, release (432 (2)).

**A3 (one instant; deduced, with an estimate).** The README holds one instant's labels (438), so T_read < 1/Gamma, with
Gamma the object's rate of label changes. Copper's Gamma (464 per s per cm^3 at 300 K, 2.2e-94 per s at 77 K) uses
standard vacancy values, not READ: an estimate. The requirement itself is deduced.

**A4 (exact; proved).** Helstrom's least error for discriminating two pure records of overlap s is
(1 - sqrt(1 - s^2))/2 (a theorem of quantum detection). It is zero if and only if s = 0. R1 and 146 allow no error, so
every label's records must be orthogonal: a projective measurement. Quantum mechanics admits one for each label used:
- Z is a superselected charge;
- occupancy and site are a partition of space into cells, whose projectors commute;
- a bond is a pair of sites.

read_index's finite-window spectroscopic read has s > 0 and fails R1 (C1).

**A5 (fast enough; proved, READ).** The Mandelstam-Tamm and Margolus-Levitin bounds (READ in encode_read E5) give
orthogonal evolution no faster than tau = pi hbar/(2 Delta E). With Delta E the K-shell gap, the per-atom times are
2.5e-17 s (H), 5.1e-18 s (O), 1.5e-18 s (Fe) and 1.3e-18 s (Cu) (arithmetic).

**A6 (fine enough; proved).** By the Heisenberg microscope, dx >= lambda/(2 sin theta), so fixing a site to half a
spacing needs lambda <= spacing. For copper (2.556 A) that is 4.85 keV for photons and 23 eV for electrons. The K edge
(11.4 keV) exceeds it, so one probe at or above E_K resolves both site and Z (arithmetic).

**A7 (complete and parallel; arithmetic).** 8.49e22 records at 1.3e-18 s each is 1.1e5 s in sequence. Within A3's
2.2 ms that needs at least 5.3e7 channels.

**A8 (energy; proved, computed exact).**
- Each bit carries (3/2) k T_H ln2 at the face, Smarr's share of Landauer's in five dimensions (encode_read E2, exact).
- The read's least energy is pi hbar N/(2 T_read) (A5 summed over N records).
- Resetting the device costs N k T ln2 (Landauer).
- E5(N) is paid by the object's rest energy when N <= N*(m) (encode_read E4, 136 (4)). For the real piece,
  N* = 1.37e24 > 1.3e21, so E5 is 0.96 % of its m c^2.

**A9 (the execution; proved by composition).** The read follows A4-A7 within A3, then the encode (A1). N is handed to
the emitter (Part B), the write is passage_est's (D4) and the release face2_release's (D5).

## 3. Part B -- the emitter (emitter_process)

**B1 (one bit; proved).** For the 5D Tangherlini hole, E5 = 3 pi hbar c r_h^2/(8 l5^3) and N = 2 pi^2 r_h^3/(4 l5^3 ln2).
Then dE5/dN = (3 pi hbar c r_h/(4 l5^3)) / (6 pi^2 r_h^2/(4 l5^3 ln2)) = hbar c ln2/(2 pi r_h) = k T_H ln2, with
T_H = hbar c/(2 pi k r_h): the first law with S = N k ln2.

**B2 (the carrier is gravity, round only on average; proved, READ).**
- For a round metric, G^t_r is proportional to d_t b (bounce_close C2's computation). So round vacuum is static
  (Birkhoff), and no exactly round wave exists.
- The round shell is the high-frequency average of non-round vacuum waves (Part C).
- Bizon, Chmaj and Schmidt's 4+1 radial vacuum waves (READ) squash the 3-sphere homogeneously. Such a squashing has no
  mirror: a reflection through a great 2-sphere conjugates SU(2)_L into SU(2)_R, so a metric invariant under the
  reflection and under SU(2)_L is invariant under both and hence round (computed defects 0.07-1.7, 1e-15 for the round
  sphere). The plane is a mirror, so the opening shell is the mirror-symmetric average, not their wave.

**B3 (causal hand-off and simultaneity; proved).** The plane's fields reach the bulk emitter, since rays leave the plane
and never return (emitter E2), so N's 141 bits (Elias-gamma) travel as information only (386). The warped bulk is
conformally flat, and conformal factors leave null geodesics unchanged as curves. Inward radial rays from a coordinate
sphere of radius R therefore reach the centre at coordinate time R from every direction (spread 0 in 10^4 random
directions, computed).

**B4 (within half a bit; deduced from M's).** The face takes the size that holds the README upon opening (162) and N
is an integer, so the shell's energy must lie within +-(1/2) k T_H ln2 of E5(N): 2.6e-22 of E5 for the copper piece.

**B5 (the price in time; proved).** A massless shell's arrival amplitude is the Fourier transform of its energy
amplitude phi(E). Take phi supported in a band of width W = k T_H ln2 and in H^1_0 (a jump at the band edge would make
<t^2> infinite). Then <t^2> = hbar^2 int |phi'|^2 / int |phi|^2 >= hbar^2 (pi/W)^2, because the least Dirichlet
eigenvalue of -d^2/dE^2 on an interval of length W is (pi/W)^2. So sigma_t >= pi hbar/(k T_H ln2) = 2 pi^2 r_h/(c ln2):
28.5 face clocks at the small end and 8 pi^2/ln2 = 113.9 GM/c^3 at the large end.

**B6 (at rest; proved).** Let a packet set be invariant under the four coordinate reflections R_i, one of them the
plane's own mirror.
- Its total momentum P satisfies R_i P = P for each i, so every component vanishes.
- Its angular momentum L_ij changes sign under R_i, and is invariant because the set is, so L_ij = 0 (1e-15 over
  1,024 random sets, computed).

The hole formed is therefore the static, non-spinning one (scope C1).

**B7 (high frequency, captured; arithmetic and Part C).** At r_h/10 the copper shell is 3.4e18 quanta of 14 TeV each,
fewer than the README's bits, so it carries energy and not the README. The derived wavelength is lam_P (D5).

## 4. Part C -- the high-frequency limit (hf_limit5, hf_theorem5)

**C1 (the plane wave; computed exact).** For ds^2 = -2 du dv + Sum_a e^(2 beta_a(u)) dx_a^2, the only nonzero Ricci
component is R_uu = -Sum_a (beta_a'' + beta_a'^2).

**C2 (an exact vacuum sequence; proved).** Let w = cos(A u/sqrt2) and beta_a = ln w + lam A sin(u/lam + 2 pi a/3), for
a = 1, 2, 3. Using Sum_a sin(phi + 2 pi a/3) = Sum_a cos(phi + 2 pi a/3) = 0 and Sum_a cos^2(phi + 2 pi a/3) = 3/2:
- Sum beta_a'' = 3 (ln w)'' (the 1/lam terms cancel);
- Sum beta_a'^2 = 3 (ln w)'^2 + (3/2) A^2.

Hence R_uu = -(3 w''/w + (3/2) A^2) = 0, since w''/w = -A^2/2. Every g_lam is exact vacuum.

As lam -> 0, |e^(2 lam A sin) - 1| <= e^(2 lam A) - 1, so g_lam -> g_0 uniformly while d_u g stays bounded and does
not converge. The limit has R_uu = (3/2) A^2 > 0 and all other components zero: null dust, energy nonnegative.
x_a -> -x_a is an isometry of every g_lam, so the mirror is kept.

**C3 (any profile; computed exact, with a numerical rate).** With A(u), the vacuum condition is exactly the linear
equation w'' + (1/2)(A^2 + lam^2 A'^2) w = 0, whose limit has R_uu = (3/2) A^2. So every rho >= 0 arises
(A = sqrt(2 rho/3)), and the error in w falls as lam^2 (ratios 4.0, 4.0, computed).

**C4 (the opening shell, locally; computed exact).** 5D Vaidya has G_vv = 3 mu'/(2 r^3) and zero trace. Matching gives
A^2 = mu'/r^3. For the least-spread shell (B5), A r_h = 0.119, so the focusing length is 11.9 r_h, against waves of
r_h/10 in a region of r_h/3. The scales separate (arithmetic).

**C5 (the whole shell; THM-HF5, hf_theorem5).**
- (iv) is proved exactly. With Phi = r - r_q(v), g^-1(dPhi, dPhi) = f - 2 r_q', which is < 0 inside the horizon
  because r_q' = r_q mu'/(4 mu) >= 0. So the boundary x = 1 is spacelike. Outgoing rays have dr/dv = f/2 < 0 <= r_q',
  so every characteristic leaves D (machine-checked, Z3).
- The limit in (ii) is proved exactly. R_vv's part quadratic in the wave rates is -2 (P1_v^2 + P1_v P2_v + P2_v^2) and
  no other component carries one. The phase average is A^2 env^2 y^6/6, round. Hence mu' = (2/9) A^2 env^2: Isaacson's
  flux, derived. 4(a^2 + ab + b^2) = (2a + b)^2 + 3b^2, so the dust's energy is nonnegative (Lean 4 and Z3). The same
  is cross-checked in Wolfram 15.
- (iii) is exact in the limit: f = 1 - mu/r^2 has one positive root. It is computed for every run (hf_core5 C3: one
  zero per column, no inner apparent horizon).
- (i), existence for every lam with lam-uniform estimates (N1*, which is L-UNIF'), is completed in its own session:
  docket68/n1star/N1STAR-PROOF.md on branch ccr-66909215-gi0qa5 at acd79676 (D21: Theorems E, A and D written out, every
  standard theorem READ at source, seven verifiers). It is cited and not copied, by M's 534.
- The rates are computed (hf_core5 C1-C5: the C^0 departure halves with lam, the mean-mass offset quarters, the horizon
  converges at first order). The coefficients are exact (hf_anchor5: sqrt2 A, and (2/9) A^2 int env'^2 = 0.45693, the
  runs agreeing to 0.01 %).
- The coupling (F5, proved on the full ansatz): g^vv = 0, so the fronts never move their own cone. The hypersurface
  equations hold no v-derivative, and the evolution equations carry only the waves' rates, linearly. The one product
  of rates is R_vv's, the dust. So the nonlinear coupling is O(1) only through the limit itself.

## 5. Part D -- delivery within half a bit (seed_escape, seed_types, seed_derive, seed_second)

**D1 (the barriers; computed exact, READ).** A massless field Phi = r^(-3/2) psi Y_l on Tangherlini obeys
psi'' + (w^2 - V) psi = 0 with V = f(((l+1)^2 - 1/4)/r^2 + 9 mu/(4 r^4)). Kodama and Ishibashi (5.2)-(5.3), READ, at
n = 3, K = 1, give k_T^2 + 2K = l(l+2): the tensor type meets exactly this barrier. Their scalar-type V_S, (3.6)-(3.7)
READ, is transcribed and reproduces Zerilli's potential exactly at n = 2.

**D2 (the record's waves split exactly; proved, computed exact).**
- *No vector type.* The two reflections forbid components odd in phi1 or phi2, and a divergence-free torus-invariant
  vector field with only a theta component is C/(s c), singular.
- *The tensor-type harmonics.* Divergence-free fixes B in terms of A, and the rough Laplacian gives Gegenbauer's
  equation, A_j = C_j^(3/2)(cos 2 theta) with k_T^2 = l(l+2) - 2, l = 2j + 2.
- *The split.* The record's trace-free perturbation projects in the energy norm to 0.639 scalar type and 0.361 tensor
  type, summing to 1 to 1e-15. l = 2 holds 0.988.

**D3 (the reflection coefficients; computed, numerical).**
- *Method.* R_l(x), x = w r_h, comes from DOP853 at rtol 1e-11, ingoing at the horizon and matched to Hankel waves at
  r* = 150 r_h; l = 2k, k <= 45, on a grid of step 1/4; 1681 (tensor) and 1655 (scalar) integrations.
- *Error control.*
  - Flux conservation R + T = 1 holds to 1.2e-9.
  - seed_second's independent linearised system reproduces R at x = 1.5-2.5 to 1e-4 (tensor 0.557119 at 1.5) and the
    scalar type at 2.1 to 9e-4.
  - At l = 0 the far fall is e^(-2 pi x), the law set by the potential's singularity at Im r* = pi r_h/2.
- *Beyond the window.* R is extended by that e^(-2 pi x) law from its last value above 1e-15. That fall is slower than
  the computed one, so the extension over-states the escape: conservative.

**D4 (the escape law and its monotonicity; proved).** As the hole grows from r_h0 by absorbing the shell
(E = (3 pi/8)(r_h/l5)^2 E_P5 for Tangherlini), the energy let out is
E_esc = (3/(16 pi)) (lam/l5)^2 I(2 pi r_h0/lam) E_P5, with I(x0) = int_x0^inf x S(x) dx and
S = Sum_k (p^S_k R_S(2k) + p^T_k R_T(2k)) >= 0.
- I'(x0) = -x0 S(x0) <= 0, so I is decreasing. E_esc falls with r_h0 at fixed lam and rises with lam at fixed r_h0.
- Hence the least seed mu0(lam) is increasing, and the least seed over the window lies at its floor (checked at 60
  wavelengths and four anchors).
- The scattering is adiabatic where escape is decided. The hole grows by at most 7.6e-6 (copper) per light-crossing,
  and the strain at the horizon is at most 2.6e-4, so the hole as it stands is the scatterer to that order (computed).

**D5 (the floor; criterion).** A quantum of energy 2 pi hbar c/lam has horizon radius r_q^2 = (16/3) l5^3/lam. It is
not a hole of its own while lam > lam_P = (64 pi^2/3)^(1/3) l5 = 5.949 l5 (the hoop criterion). The constant is an
order-one criterion, not a theorem; the delivery below holds at every lam >= lam_P with mu0 >= mu0*(lam).

**D6 (the delivery at first order; proved, with a computed threshold).**
- *Half a bit.* At the small end half a bit is (ln2/(4 pi))(l5/r_hf) E_P5 (B1). At the large end it is
  (ln2/(8 pi))(l5/r0) E_P5 (k T_H = hbar c^3/(8 pi G M)), equal to E/(4N) of earth_cap's figures.
- *The derived seeds.* E_esc(lam_P, mu0) = half a bit at mu0* = 102 l5^2 (copper), 61 (the example README), 808
  (r0 = 20 ell) and 917 (the Earth cap). By D4, every mu0 >= mu0* delivers within half a bit at first order.
- *Robust to R's accuracy.* E_esc depends on R through I. A relative error epsilon in R moves mu0* by a relative
  ~ epsilon/(d ln I/d ln mu0), and d ln I/d ln mu0 is large at x0* near 10. With epsilon <= 1e-4 (D3), mu0* moves by
  under 1e-4 of itself.
- *Robust to the labelling.* Moving the harmonic labelling by one moves the copper threshold by 9-11 % (seed_escape E5),
  far more than the numerical error. The verdicts stand.
- *The law.* x0* = 0.577 ln(r_hf/l5) + 1.75. Its slope is 1/ln((1 + sqrt2)^2) to 2 %, from the poles of
  h = sqrt(2/(1 + x^2)) at x = +-i.

**D7 (the delivery at second order; computed exact, with a conservative extrapolation).**
- *The equations.* The record's own 2+1 equations are expanded to second order about Tangherlini exactly (sympy). The
  order 0 is identically zero, each row is cleared of denominators, projected exactly and reduced to lowest terms. The
  l = 2 waves of both types close the tower with three modes, exactly.
- *Validation.* The first order reproduces D1's barriers to 1e-4. The supplementary rows hold at R/2 to 1e-11 (first
  order) and 1e-6 (second). The outgoing projection is gauge-clean to 1e-15, and a pure-gauge admixture of the wave's
  size moves C by the recorded amount. R = 100 against 150 moves C by 2e-5.
- *C(x) computed.* C(x) = P_out(2w)/P_in(w) at x = 1.0, 1.5, 2.1, 2.5, 3.0 for both types: tensor 8.99e-4, 7.51e-4,
  4.34e-7, 1.44e-9, 1.38e-12; scalar 2.29, 1.51e-3, 8.04e-8, 1.90e-10, 1.38e-13.
- *The extrapolation.* C is taken from x = 3.0 to x* (10.69, copper) with a slope of 6 in ln C, against the measured
  13.5-15.4 above the barrier tops. The exponential fall is set by the singularity at Im r* = pi r_h/2 (the law of D3).
  A slope of 6 over-states C at x* by about e^((13.5 - 6)(7.7)) ~ 1e25: conservative.
- *The result.* At the derived point the second order lets out 2.0e-18 half bits (copper), seventeen orders below the
  half bit allowed.
- *Every other channel* (Q6, deduced). The pattern's tail beyond l = 2 (1.2 % of the power) reflects at first order
  (D3-D6). Its square cannot exceed its reflected power times the strain, so it is bounded by the first-order escape
  times h_H^2.

**D8 (the large end; computed).** The derived seed is 28-30 l5 against ell = 9.07e19 l5, so (r_h0/ell)^2 = 1e-37. The
seed phase is five-dimensional Tangherlini, with the warp at that order. The shell (sigma_t = 113.9 GM/c^3) reaches it
at 3e-5 of its length, and the second order lets out below 1e-35 half bits.

## 6. Part E -- the theorem from its parts (proved by composition)

- 1 is Part A.
- 2 is Part B with Part C: emitted at one coordinate time from a mirrored sphere in the bulk (B3), band-limited to
  half a bit (B4-B5), reflection-symmetric (B6), high-frequency gravitational waves whose limit is 5D Vaidya null dust
  (C1-C5). The face forms holding exactly N, with one horizon and no partner.
- 3 is Part D: at lam_P (or any lam in the window) with mu0 >= mu0*(lam), the first order delivers within half a bit
  (D4-D6), and the second order adds at most 2.0e-18 half bits (D7).

No inner or Cauchy horizon enters anywhere (U2, C5 (iii), hf_theorem5 F1).

## 7. What is computed rather than derived, and what is theorized -- why the status is COMPUTED-THEORIZED

**Computed numerically, each with its error control and its margin:**

| Quantity | Error control | Margin |
|---|---|---|
| R_l(x) | 1.2e-9 flux | conservative extension |
| C(x) | 1e-4 to 1e-6 | seventeen orders |
| mu0* | under 1e-4 | the labelling's 10 % is the larger effect |
| The powers 0.639/0.361 | 1e-15 | -- |
| hf_core5's rates | -- | four wavelengths |

**Theorized, named:**
- the floor's constant (D5, the hoop criterion);
- linear adiabatic scattering in the seed phase, validated by the second order (D4, D7);
- the second order taken monochromatic at the envelope's peak on mu = 1 Tangherlini, and extrapolated by a
  conservative slope (D7);
- A3's copper rates (standard values, not READ);
- N1* (C5 (i)), proved in its own session and cited, not re-checked here (534).

**Not a computation:** the gap between the read's demonstrated technology and its requirement (source_spec U7: 23
orders). The device is defined as quantum mechanics admits it (A4), not built.
