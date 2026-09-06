B.push(h2('8.  Testing the Coordinates Against Measured Data'));
B.push(p([t('Sections 3 to 7 establish structural facts about the lattice. None of them involves a measurement. It is reasonable to ask whether the coordinates carry information about physical quantities, and equally reasonable to ask how any such information compares with what established descriptors already provide. This section reports both tests. The second is the more important, and it is unflattering.')]));

B.push(h3('8.1  The regression'));
B.push(p([t('The quantity chosen is the enthalpy of hydride formation, ΔH_f, in kJ per mole of hydrogen: measured, tabulated, dimensional, independent of this framework, and the quantity that governs whether a metal absorbs hydrogen and how strongly it binds it. Values were taken for 39 transition metals, lanthanides and actinides with well-established binary hydride data. Ordinary least squares on the lattice coordinates gives')]));
B.push(eq('ΔH_f  =  +136.2  −  89.5·ℓ  +  6.4·k        (kJ · mol⁻¹ H)', '7'));
B.push(p([t('with both coefficients significant — ℓ at p = 3.1 × 10⁻⁸, k at p = 8.1 × 10⁻⁴ — an in-sample R² of 0.592, and a leave-one-out cross-validated R² of 0.514. Adding n, |Q₀| or H_cp does not improve the cross-validated fit; the five-term model gains in-sample R² while losing it out of sample, the signature of overfitting. Atomic number alone gives a negative cross-validated R², carrying no predictive information on this data. Figure 5 presents the fit.')]));
B.push(img('fig5b_hydride.png', 640, 243));
B.push(cap(5, 'The lattice coordinates against hydride formation enthalpy for 39 metals. (a) Measured versus predicted for the model of Equation (7); the dashed line is parity. (b) Variance explained by candidate models, in-sample and cross-validated. (c) Permutation null for the contribution of k: the observed gain of 0.15 in R² lies outside the distribution from 10,000 shuffles (p = 0.0004).'));
B.push(p([t('Taken alone this looks encouraging. It should not be taken alone.')]));

B.push(h3('8.2  Benchmarked against established descriptors'));
B.push(p([t('Two schemes address this problem and have done so for decades. Pettifor\'s Mendeleev number is a one-dimensional chemical scale constructed so that structure maps separate cleanly; Miedema\'s model predicts formation enthalpies from an electronegativity parameter φ* and an electron-density term n_ws^(1/3). Both were fitted to the same 39 elements under identical cross-validation. The comparison is given in Figure 6 and Table 1.')]));
B.push(img('fig5c_benchmark.png', 640, 223));
B.push(cap(6, 'The lattice weighed against prior art. (a) Cross-validated R² for each scheme, with the number of fitted predictors marked. Pettifor\'s single-variable scale outperforms the two-variable lattice model by a wide margin, and Miedema\'s full form outperforms both. (b) Absolute correlation of the lattice coordinates with the established descriptors. The block index ℓ is strongly correlated with all three — it encodes information they already carry — whereas the occupancy k is uncorrelated with all three. (c) Cross-validated R² of each established scheme before and after adding k, with permutation significance. The occupancy coordinate improves Pettifor\'s scale and the two-parameter Miedema form, but adds nothing to the full Miedema model.'));

B.push(tcap(1, 'Prediction of hydride formation enthalpy across 39 metals, all schemes fitted and cross-validated identically. Paired Wilcoxon tests compare squared leave-one-out errors against the lattice model.'));
B.push(table(
  ['Scheme', 'Predictors', 'Fit R²', 'CV R²', 'CV RMSE', 'vs. lattice'],
  [
    ['Miedema, full form', '4', '0.934', '0.895', '18.1', 'p < 0.0001'],
    ['Pettifor, MN + MN²', '2', '0.854', '0.828', '23.2', 'p < 0.0001'],
    ['Miedema, φ* + n_ws', '2', '0.842', '0.808', '24.6', 'p = 0.0001'],
    ['Pettifor, MN alone', '1', '0.808', '0.790', '25.7', 'p = 0.0003'],
    ['Lattice, ℓ + n + k', '3', '0.608', '0.504', '39.4', '—'],
    ['Lattice, ℓ + k', '2', '0.592', '0.514', '39.1', '—'],
    ['Atomic number Z', '1', '0.028', '−0.076', '58.1', 'p < 0.0001'],
  ],
  [2300, 1300, 1000, 1000, 1100, 1500],
  ['ℓ + k']
));
B.push(p([t('The result is unambiguous and runs against the framework. Pettifor\'s scale, using a single variable, achieves a cross-validated R² of 0.790 against the lattice\'s 0.514 with two. Miedema\'s full form reaches 0.895. Paired Wilcoxon tests on the leave-one-out squared errors reject equality against every established scheme, the weakest at p = 0.0003. On the task of predicting hydride formation enthalpy, the lattice coordinates are substantially outperformed by prior art that has been available since the 1980s.')], { spacing: { before: 160, after: 120 } }));
B.push(p([t('Nor does combining them rescue the position. Adding ℓ and k to the full Miedema model changes its cross-validated R² from 0.895 to 0.888 — a decrease. Whatever the lattice contributes on this task is already contained in the established descriptors.')]));

B.push(h3('8.3  What survives: the occupancy coordinate'));
B.push(p([t('One result does survive the benchmark, and it is worth isolating precisely because the rest did not.')]));
B.push(p([t('Figure 6(b) shows that the two lattice coordinates behave quite differently. The block index ℓ correlates strongly with every established descriptor — |r| between 0.68 and 0.77 — which is expected, since ℓ is the block label and every chemical scale encodes block membership. The occupancy k, by contrast, is uncorrelated with all three: r = −0.05 against the Mendeleev number, +0.14 against φ*, −0.13 against n_ws^(1/3), none approaching significance. The occupancy coordinate is orthogonal to the established descriptors.')]));
B.push(p([t('Figure 6(c) tests whether that orthogonal information is useful. Adding k to Pettifor\'s Mendeleev number raises cross-validated R² from 0.790 to 0.844, a gain of 0.054 significant at p = 0.001 by permutation. Smaller but significant gains follow for the quadratic Pettifor form (+0.014, p = 0.029) and the two-parameter Miedema form (+0.009, p = 0.043). Against the full four-parameter Miedema model the gain vanishes (−0.002, p = 0.363), which is unsurprising: with four fitted per-element parameters that model has already absorbed the available variance.')]));
B.push(p([t('The defensible claim is therefore narrow and specific. Valence subshell occupancy carries information about hydride stability that Pettifor\'s chemical scale does not encode, and appending it to that scale improves prediction measurably. This is a modest contribution to an existing method rather than a competitive alternative to it, and it is stated here in those terms.')]));
B.push(p([t('Two further points. The classification by ΔQ direction from Section 6, derived purely from the angular-momentum constraint, separates the same data: Class C elements average −61.9 kJ · mol⁻¹ H against −15.7 for Class B, significant at p = 0.010 by Welch\'s test. And the ℓ term in Equation (7) is not a discovery — that f-block metals form more stable hydrides than late d-block metals is long-established descriptive chemistry, which the lattice recovers rather than reveals.')]));
B.push(p([t('It is equally important to state the limit. Everything in this section concerns bonding energetics of order 10⁻¹ eV over interatomic distances of order 10⁻¹⁰ m. It establishes that the lattice has dimensional content in the chemical regime, empirically and by regression against measured values, in the same tradition as the schemes it was benchmarked against. It carries no implication for quantities at nuclear scale, and Section 15 returns to this.')]));
