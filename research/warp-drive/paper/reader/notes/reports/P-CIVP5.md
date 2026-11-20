# P-CIVP5: Tier 5 (further dust families at the axes), proof file report

Output: research/warp-drive/paper/reader/proofs/P-CIVP5.md (913 lines). Nothing in chapters/ or crosswalk/ was edited;
nothing committed. Read: S-T5, GN-T5, GN-T3, S-T3, GN-T4 §1, chapters 81 and 83 (relevant parts), P-CIVP (Tier 1).
P-CIVP3 (Tier 3) and P-CIVP4 did not exist; Tier 3 is cited by pending markers.

## Blocks
- **A1 (ch 81, after rem:class-leaf-numerics):** lem:class-leaf-arc (two states compared along ONE arc: pointwise one-sided
  bound eq:class-leaf-arc and L² bound on any G-invariant set closed under the arcs of V only; Volterra + Hardy average,
  no elliptic step, no ball) = GN-T5 C7 and C2; lem:class-leaf-tame (lem:class-leaf-differences (a) on the lower ball 𝔅′,
  bound linear in 𝒩_k) = GN-T5's "lighter form".
- **A2 (ch 81, after rem:class-kato-model):** space-time norms 𝒳^s, trace eq:class-trace, extension E_b;
  lem:class-mixed-product; lem:class-kato-history (linear problem, forcing in H^s of space-time, history matched);
  thm:class-kato-memory (memory m; hypotheses (M0) causality, (M1) ‖F(u)‖_{H^s([t1,t2])} ≤ C_F(t2−t1+m)^{1/2},
  (M2) integrated L² Lipschitz with memory; (a) existence/uniqueness/continuation on a ball, (b) stability with (M1′));
  rem:class-kato-memory. S-T5 M4 step 3 is not used (C1).
- **B (ch 83, new section sec:loc-t5 "Further dust families at the axes"):** def:loc-t5-family ((F-a) no density near
  corner axis circles = C3; (F-b) density only where the family crosses the face, which implies (H×); (F-c) corner
  compatibility at density points on S); lem:loc-t5-dichotomy; lem:loc-t5-tubes (C3 needed, proved by continuous
  dependence); carrying families with ξ_A (C4); lem:loc-t5-jets (M0); lem:loc-t5-times with eq:loc-t5-times
  (t_A := τ0 − χψ_AĜ_Aρ², τ := τ0 + Kρ²χ, K ≥ 1 + sup|Ĝ_A|; (a)–(d) proved); lem:loc-t5-faces (M2); the system with
  memory; lem:loc-t5-forcing ((M0)–(M2),(M1′) by Fubini over each t_A-foliation; time-extension beyond t̄);
  lem:loc-t5-residual (M6, in full in the t_A-slicing); lem:loc-t5-existence; lem:loc-t5-energy (integrated Gronwall);
  lem:loc-t5-past (M5 P, one-sided, C7); lem:loc-t5-constraints (M5 F on F ∩ {τ ≤ s*}, Lie transport for p_A = du_A,
  tubes 𝒦_A″ closed under arcs); lem:loc-t5-uniqueness (Lemma R on rectangles with past faces in the cones, by
  exhaustion with triangles {Φ_N ≤ 1}; C5, interior faces excluded with reason); thm:loc-t5; prop:loc-t5-cut
  (statement W with W1 (N1), W2 (phase unused via ξ_A), W3 (Λ spacelike off the axes), W4 (Λ carries the causal bound,
  no C0), and N closed under generators (needed: re-solving the constraints changes data beyond the cut on each
  generator)); rem:loc-t5-scope.

## The theorem as stated (thm:loc-t5)
Data of the Tier 3 theorem, size ε in C^m, plus further families with (F-a)–(F-c) instead of Tier 3's vanishing near
face–axis points. For ε ≤ ε0: (a) a class solution with N_f families on Q1 × S³, further phases defined near supp q_A,
**of class C^(k−3)**, double-null form, inducing the data; (b) C^(k−3) estimate Cε; (c) uniqueness on every rectangle
[0,u′]×[0,v′] ⊂ Q1 among solutions within ε2 (k−2 derivatives) with the same data on its faces; (d) localisation on
such rectangles. Crossing families: any number. Tangent ("grazing") families with density on a tangency set: only
prop:loc-t5-cut (development on regions D′ avoiding that axis, bounded by ∂F∖N, a spacelike Λ off the axes and Q1's
future faces).

## Pending markers (16 lines) and exactly what each needs from Tier 3
- t3-setting (7): Q1^η, chart time τ0 = Φ(u,v), Φ_u,Φ_v>0, s* with max_Q1 τ0 < s*, F∩{τ0≤s*}⊂Q1^η; chart x; data
  extended past u1,v1; Û (= Ů on {τ0 ≤ τ_init}, formal jets on ∂F, ‖Û−Ů‖_{C^{k+3}} ≤ Cε); Ĝ as gauge reference; ξ;
  system 𝔄_ξ of the form eq:class-kato-system with A^0 ≥ c1 I, local terms vanishing outside a compact set at Ů;
  gauge residual 𝔄_ξ(Ů) bounded in C^k by Cε; τ0-face sections are the data's double-null spheres.
- t3-cone-data (1): prop:loc-cones / lem:loc-cone-in through the axis generators (T3-0) with a general smooth stress.
- t3-jets (2): lem:loc-cone-jets / prop:loc-cone-formal through the axis generators (local residuals flat on ∂F).
- t3-leaf-criterion (2): GN-T3 §1.2 criterion (S is V's A-leaf iff p_A(TS)=0 and Θ_A = −tr_TS p_A(∇_X Y)), with its proof's
  mean-curvature identity.
- t3-residual (1): GN3 for the adapted families on τ0-slices incl. the τ-continuity case at the corner.
- t3-gauge (1): T3-7 double-null coordinates through the axes (needed at class C^(k−3)).
- t3-wave-map (2): L10 conversion of a solution in the double-null gauge to the wave gauge relative to Ĝ, identity to
  infinite order on the faces.
- t3-theorem (1): the Tier 3 theorem's data hypotheses.
Placement item 6 asks the Tier 3 section to carry its further families with ξ_A (C4).

## What remains open / caveats
- Smoothness: the solution is given in C^(k−3); persistence of regularity for the memory system (a higher-norm bound
  linear in the top norm, incl. time derivatives) is not proved (rem:loc-t5-scope (v)). Tier 3 claims smooth.
- Grazing families through the axis (S-T5 §5.1): open; rem (i) proves the face is characteristic and that no face section
  of any slicing is a leaf unless a(u0) = 0.
- lem:class-leaf-tame is written at the level of detail of lem:class-leaf-differences (a) (itself a sketch); readers
  should check its induction (low orders by lem:class-interior-regularity j=0, high orders tame with ‖ζ‖_{C²}).
- prop:loc-t5-cut requires N closed under generators; GN-T5's W domain (N on 𝒞_out only near the corner) ignored this.
- Densities on S off the axes need (F-c) (corner compatibility of phase and density jets).

## Checks (scratch copy pcivp5/: chapters + P-CIVP Blocks A,B + this file applied, Tier 1 item 4 + new loss sentences)
- lint.py --chapters: 17 hits = 16 pending lines + "reference to undefined label thm:civp-large" (Tier 1 text citing
  Tier 2, not this file).
- assemble.py --check: labels 4732, 1 problem (the same thm:civp-large).
- All lines of the file ≤ 121 characters also with every non-pending reference counted as 18 characters and eq tags
  as "(83.12)"; no wrapped line starts with a Markdown marker.
