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

## 6. Outside the class (SETTLEa, COMPUTED-THEORIZED; item 548)

M, 547: "Do we need the nonlinear settlings to be symmetric or asymmetric in class? And would having both be helpful
and preferred?"; 548: "Yes, add the asymmetric settling row to the register". SETTLEs and SETTLE settle the record's own
solution, which keeps the class's symmetry: a symmetry of the data is an isometry of their maximal development, which
is unique up to isometry (Choquet-Bruhat and Geroch, as Hintz 2606.28253v2 p. 1 states it, READ). SETTLEa is the row
for a perturbation that breaks the symmetry. Its computations are settle_asym.py A0-A3.

**THM-SETTLEa.** (i) Outside the class the end state near Tangherlini is a five-dimensional Myers-Perry hole, its spin
A in so(4) (dimension 6) and its momentum P in R^4; with T^2 alone, a two-spin hole at rest; in the class, Tangherlini.
(ii) For the one perturbation of the class the record computes, the inflow's random spin a/r_h = 7.6e-8, the Myers-Perry
hole of the formed hole's mass differs from Tangherlini by -2.9e-15 in horizon area and in surface gravity. (iii) At the
large end a perturbation breaking the symmetry, small enough, settles to a nearby Kerr hole, to O((ell/r0)^2) (Hintz's
theorem, READ). (iv) At the small end the linear settling is proved for every type of perturbation (O3gs); the
nonlinear settling without symmetry is theorized, named.

**Q1 (A1; computed exact, proved).**
1. The stationary perturbations of Tangherlini below l = 2 are the l = 1 vector type, the six Killing fields of S^3
   (rotations), the l = 1 scalar type, the four degree-one harmonics (translations and boosts, no physical degree of
   freedom), and l = 0, the mass (Kodama and Ishibashi, READ in face_grav W4). At l >= 2 there is no static mode (G0s).
   The counts 6 and 4 are dim so(4) and the degree-one harmonic polynomials of R^4; on S^2 they are 3 and 3.
2. A symmetry g of the data is an isometry of the development and so of its end state: g A g^-1 = A for the
   rotations, R A R = A for the reflections, and g P = P, R P = P.
3. Commuting with both rotation generators J_12 and J_34 confines A to their span (computed: the rank of the linear
   conditions on the six coefficients). The reflection phi_1 -> -phi_1 sends J_12 to -J_12 and fixes J_34, the other
   the reverse, so the class leaves A = 0; T^2 alone leaves the span, dimension 2. A vector fixed by J_12 has x_1 = x_2
   = 0 and by J_34 x_3 = x_4 = 0, so P = 0 under T^2.
4. With no symmetry A ranges over so(4), dimension 6, and P over R^4. A boost carries Tangherlini to Tangherlini, so
   reaching Tangherlini itself asks the six spins to vanish: codimension 6 in the linearised count.
5. Control, four dimensions: an axial rotation with the reflection phi -> -phi leaves J = 0 and P along the axis, Hintz's
   account of Klainerman and Szeftel's class ("though its center-of-mass may move along the symmetry axis", p. 6,
   READ); no symmetry leaves so(3), dimension 3, Dafermos, Holzegel, Rodnianski and Taylor's codimension 3 (Hintz p. 6,
   READ). Mutant: one reflection only leaves one spin, caught.

**Q2 (A2; READ, computed exact, proved).**
1. Emparan and Reall (0801.3471v2, READ) at d = 5: Pi = (r^2 + a^2)(r^2 + b^2) (p. 16, (44)), the horizon Pi(r0) =
   mu r0^2 ((45)), A_H = (Omega_3/(2 kappa)) mu (2 - 2a^2/(r0^2 + a^2) - 2b^2/(r0^2 + b^2)) with Omega_3 = 2 pi^2
   ((46)), kappa = (Pi'(r0) - 2 mu r0)/(2 mu r0^2) (p. 17, (47)), M = 3 pi mu/(8G) and J_i = (2/3) M a_i (p. 14,
   (34)).
2. With Omega_i = a_i/(r0^2 + a_i^2), the angular velocities of the horizon's null generator, the first law dM =
   kappa dA_H/(8 pi G) + Omega_a dJ_a + Omega_b dJ_b holds identically in (r0, a, b) (sympy, exact). Mutant: Omega_i
   halved, the law fails, caught.
3. At b = 0, kappa = r0/(r0^2 + a^2), their (38)'s 2 pi T_H at d = 5; at a = b = 0, kappa = 1/r0 and A_H = 2 pi^2 r0^3,
   Tangherlini. In d = 5 the family has no ultraspinning regime (p. 17, READ).

**Q3 (A3; computed exact to O(a^4), numbers).**
1. At fixed mass take mu = r_h^2 = 1 and b = 0: r0^2 = 1 - a^2, A_H/(2 pi^2) = r0 and kappa = r0 (Q2), so both differ
   from Tangherlini's by -a^2/2 + O(a^4) (exact series).
2. The inflow's random angular momentum, sqrt(n) hbar over the README's inflow quanta, gives a/r_h = 7.6e-8 at the
   example (scope C1, imported). So -2.9e-15 in area and in surface gravity, and Omega r_h = 7.6e-8.

**What is READ and deduced for (iii).** Hintz (2606.28253v2, p. 2, Theorem 1.1, READ): initial data satisfying the
constraints, equal to subextremal Kerr data outside a compact set and close to them in H^d, have a development
containing a region isometric to (Omega, g) with |g - g_b| <~ (1 + t)^(-2-eps_K) for "subextremal parameters b = (m, a)
close to b0"; "This settles the Kerr stability conjecture in the full subextremal range" (p. 2); no symmetry is
assumed, and "Restricting to axisymmetry, ultimately Schwarzschildean spacetimes, or small angular momenta would not
lead to simplifications in our arguments" (p. 5). The plane reads the large hole as Schwarzschild to O((ell/r0)^2)
(section 5, item 4), so (iii) holds on SETTLE's footing: the threshold is not quantified, and both margins fall with N.

**Theorized, named: (iv)'s nonlinear step.** The five-dimensional counterpart of Hintz's theorem is open in the field.
Its linear half is proved: O3gs (face_grav W0-W6), Hung, Keller and Wang's decay of every type in dimension six and
below (1809.05144v1 Theorem 2, READ), below l = 2 the mass or the Myers-Perry member. What the class removed returns
outside it: the vector type, the boosts' second-order pole at zero energy, the six rotations and the Myers-Perry end
states, whose linearised stability Emparan and Reall call "largely an open problem" (p. 20, 2008). The route is the N1*
session's route B, whose inputs already follow Hintz without symmetry (N1STAR-PROOF 10.29-10.36 on main at 308c527a),
[AHW24]'s rigidity beyond zero spin still OPEN there. SETTLEs and SETTLE are unchanged.
