# SETTLEs: the complete proof of its computations (item 542)

*First written* 2026-10-20, on M's item 542 ("strengthen the existing lemmas, and ad more for support") and item 538
("anything COMPUTED-THEORIZED should have a complete proof for the computations"). SETTLEs is COMPUTED-THEORIZED. Item
540 determined it in settle_late.py (S0-S5). This file proves every computation it names and names what is theorized.
The large end's row, SETTLE, is PROVED (settle_large.py E0-E4) and is summarised in section 5.

Labels: proved, computed (exact), computed (numerical; with method, error control and margin), READ, theorized, M's.

## 1. The theorem

**THM-SETTLEs.** Take the delivery's class: five-dimensional vacuum, invariant under T^2 with both reflections phi_1 ->
-phi_1 and phi_2 -> -phi_2, of cohomogeneity three (settle5 T1). In it:
1. any stationary end state is Tangherlini of the final mass (proved);
2. linear perturbations decay, the metric included, to a change of mass (proved);
3. the record's own nonlinear evolution through the shell settles, to the scheme's resolution (computed);
4. a proof of the nonlinear statement in the class is open in the field (theorized, named).

**Hypotheses.** General relativity in five dimensions. At the hole's scale the bulk's Lambda is negligible:
r_h/ell = 8.0e-16 to 6.5e-13 at the example README (ell_si L2). At finite ell the end state is the static brane hole of
G0s and GMID; S1 is its flat-limit statement, and G0s carries it to finite ell order by order.

## 2. Proofs

**P1 (S1; READ, computed exact, proved).**
1. A stationary vacuum solution in the class has three commuting Killing fields, d_t, d_phi1 and d_phi2, the phi-ones
   vanishing on the axes.
2. By Emparan and Reall's integrability (hep-th/0110258v2, p. 5, READ), the 2-planes orthogonal to them are
   integrable. So the metric is a Killing block in (t, phi1, phi2) plus a 2-metric in (r, theta).
3. Under phi_i -> -phi_i the components odd in phi_i are g_(t phi_i) and g_(phi1 phi2). A metric invariant under both
   reflections equals its average over the reflection group, so those components vanish. settle_late's endpoint()
   performs exactly this average on the general block with every component a function of (r, theta).
4. Then the lowered time Killing field xi = g_tt dt has zero twist, xi ^ d xi = 0 (computed: the sum of the squares of
   the twist's components simplifies to zero). Control: without the average the twist does not vanish.
5. So d_t is hypersurface orthogonal and the end state is static. Gibbons, Ida and Shiromizu (gr-qc/0203004, READ) make
   the only asymptotically flat, static, non-degenerate vacuum black hole in five dimensions Tangherlini. Its mass is
   the final mass.

**P2 (S2; READ, computed exact, proved).**
1. The class carries only scalar- and tensor-type modes of even l >= 2, and the l = 0 mode (settle5 T1). Kodama and
   Ishibashi (hep-th/0305147v3, READ): the k = 0 mode is "a shift of the mass parameter of the black hole".
2. Hung, Keller and Wang (1809.05144v1, Theorem 2, READ through settle5): the master quantities of every type decay as
   tau^-2 in energy at every order, in dimension six and below.
3. In Kodama and Ishibashi's gauge the metric is built from the master field and its derivatives ((3.12), (3.14); the
   tensor type H_T = r^(-3/2) Phi). The coefficients carry H = m + 6x in their denominators, with m = l(l + 2) - 3 >= 5
   and x = r_h^2/r^2 in (0, 1]. H is linear in x, so its least value on the exterior is at an end: H >= m >= 5 > 0
   (computed). face_grav W2 checks every coefficient's numerator and denominator for zeros on (0, 1] exactly, for l =
   2-10, the vector type's included. Control: H = m - 30x vanishes outside the horizon and fails.
4. Kodama and Ishibashi's scalar potential, written out in settle_late's linear(), equals settle5's identically (sympy
   simplifies the difference to zero at l = 2).
5. So the linearised metric settles, in that gauge, to a change of mass.

**P3 (S3-S4; computed, numerical).**
- *Method.* hf_mirror5's scheme for the class: five-dimensional vacuum, T^2 with both reflections, cohomogeneity three,
  in characteristic form. It is run at lam = 0.1, A = 1, seed 1 through the shell, which passes past null infinity over
  0.5 < v < 3.5, and on to v = 40. That is thirty-seven times the final horizon radius and nine e-folds of the
  least-damped mode. Two resolutions: run a at 16 x 10 and run b at 20 x 16. Both are checkpointed
  (data/settle_late_a.json, _b.json).
- *Results.* The round part is Tangherlini of one mass at every radius probed (y = 0.5, 0.8, 1.0), to 2e-7, unchanged
  in v. mu_f = 1.18689: the Isaacson prediction 1.18229 plus hf_mirror5 X5's second-order offset 4.6e-3. The apparent
  horizon closes onto sqrt(mu_f), round to 1e-4. The non-round part falls from 1.15e-2 at the shell's end to 6.6e-5 at
  v = 40 (run a), 175-fold. Its late maximum lies below its maximum at v = 14-24: no growth.
- *Error control and margins.* These are settle_late's checks():
  - the mass spread across probes is below 1e-5 and its drift below 1e-6;
  - mu_f lies between the horizon's least and greatest radius squared to 1e-4, and those radii agree to 2e-4;
  - the fall is below 2e-2 and the late maximum below the middle one;
  - S4: the two resolutions agree on mu_f to 1e-4, and both bound the late non-round part below 5e-4.

  Below about 1e-3 the non-round part's fall is at the scheme's floor (constraint residuals 1e-4 at 16 x 10). So the
  late rate is not resolved and is not claimed. The early fall, v = 6-14, is at about the least-damped mode's rate.
- *Controls.* settle_late's mutants: a late growth put into the non-round part after v = 20, and one probe's round
  part moved off the common mass. Each is caught.

## 3. What is computed rather than proved

S3-S4 only: the nonlinear evolution to the scheme's resolution, two resolutions agreeing.

## 4. Theorized, named

**Nonlinear settling in the class.** The nearest theorems READ are:
- Dafermos and Holzegel (gr-qc/0510051): Tangherlini "orbitally stable (in the fully non-linear theory) with respect to
  vacuum perturbations of initial data preserving triaxial Bianchi IX symmetry". Those are solutions in (t, r) alone;
  the class here depends on (t, r, theta).
- Klainerman and Szeftel's polarized axisymmetric case, in four dimensions.
- Dafermos, Holzegel, Rodnianski and Taylor's full four-dimensional theorem (2104.08222). Its five-dimensional
  counterpart is absent: DHR's Teukolsky engine is four-dimensional (gauge5 G5).

The five-dimensional statement in this class is open in the field. The physical wavelength, 10 l5, is the N1*
session's (M, 540).

**Since 544 (M: "Theorem P carried, and 10 l5 left with the N1* seesion - are now ready. The nonlinear settlings are
still being worked").** Carried from the N1* session (N1STAR-PROOF.md section 10; merged by PRs #62-#64, its
instruments re-run here):
- *Linear settling, every metric component (Proposition 10.1; deduced from READ).* In Kodama and Ishibashi's gauge
  f_a = 0 = H_T, every component of a perturbation in the class settles to a change of mass at Hung, Keller and Wang's
  rate, tau^-2 in energy with two derivatives lost. That is P2 above, written out mode by mode. settle5 T5: no growing
  mode for l = 2..10 in either type to tau = 275 r_h, a finite-time observation excluding rates above 0.08/r_h. T6: the
  late tail is t^-7 at l = 2, Cardoso, Yoshida, Dias and Lemos's law (READ).
- *The harmonic gauge's objects (Proposition 10.2; computed exact, wavegauge5 W1-W5).* The Lichnerowicz equation;
  the tensor type is harmonic as it stands; the scalar gauge vector's three 1+1 equations per mode; the stationary
  one-form W* regular at the horizon; the gauge-fixed mass change K*, linear in t. The decay estimate for that system
  (Hung's sections 5-8 in five dimensions) is named and not attempted: linear stability in the wave-map gauge in which
  the nonlinear problem is posed is still open.
- *The physical wavelength (growth5 G0-G5; derived_go D0-D4).* At 10 l5 the record's own scheme fails its premise at
  both seeds before the shell's peak: the interior of the seed's horizon untraps from the inside outward in the
  scheme's gauge *[the round spheres' expansion only: no marginally trapped surface forms there, 545]*. At the
  record's own lam_P on the least seeds it fails too, before or at the peak (derived_go). No
  approximant at the physical wavelength comes from it, so S3-S4's settling run, made at lam/sqrt(mu0) = 0.1, cannot
  be repeated there with this scheme. The exterior of the event horizon is unaffected. The question is re-posed as the
  characteristic problem in double-null gauge, which is not built.
- *The nonlinear settling is still being worked in the N1* session (M, 544).* It stays theorized here, named as above.
- *Since 545 (M: "Does 519 cover this? - no it does not. Please investigate this exhaustively ...").* At the physical
  wavelength no inner marginally trapped surface forms on the record's slices (mots545 M0-M12). On every slice where
  the core boundary is outflow the outer horizon is the only marginally trapped surface of any shape, so the formed
  hole has one horizon there too. What stops the scheme at the small end is that boundary turning inflow, so S3-S4's
  run is still not repeated there; a seed of mu0 >= 808.5 l5^2 at lam_P keeps it outflow. At the large end the run
  past v = 1.83 is not converged. The settling's statement is unchanged: theorized, named.

## 5. The large end (SETTLE, PROVED)

settle_large.py E0-E4:
1. On the plane the delivery's class is axisymmetric. The plane is the fixed set of one reflection, so one rotation
   survives.
2. The other reflection, phi -> -phi, removes every g_(a phi) off the diagonal. Then F_ab = d_a g_(b phi) - d_b g_(a phi)
   vanishes for a, b != phi, and g^(t phi) = g^(r phi) = 0, so the Komar integral of d_phi vanishes identically
   (proved; computed exactly on random polynomial components; normalised on slowly rotating Kerr, which returns J).
3. Dafermos, Holzegel, Rodnianski and Taylor's Corollary III.3.1 (2104.08222v1, p. 16, READ) then applies: data close to
   Schwarzschild that are "axisymmetric and have vanishing Komar angular momentum, are contained in the codimension-3
   'submanifold' M_stable ... consequences (i), (ii) and (iii) apply". By (iii) the metric "asymptotes, inverse
   polynomially, to a Schwarzschild metric with mass M_final".
4. Closeness: the plane reads the large hole as Schwarzschild to O((ell/r0)^2), 2.5e-3 at r0 = 20 ell, and the
   formation's roundness is 10 l5/r0, at most 4.4e-18. Both fall with N, so the corollary's threshold, unquantified in
   the paper, is met for every N above a finite value.
