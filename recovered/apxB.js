B.push(new Paragraph({children:[new PageBreak()]}));
B.push(h1('APPENDIX B'));
B.push(p([t('A Lattice Bound on Maximum Oxidation State',{bold:true,size:26})],
  {align:AlignmentType.LEFT,spacing:{before:0,after:60}}));
B.push(p([t('Matthew Lach',{size:21})],{align:AlignmentType.LEFT,spacing:{after:180}}));
B.push(p([t('Abstract',{bold:true,size:22})],{align:AlignmentType.LEFT,spacing:{before:80,after:80}}));
B.push(p([t('This appendix applies the lattice of the accompanying paper to the maximum oxidation state an element can reach. It is placed outside the numbered parts on the same terms as Appendix A: nothing in the account of the lattice depends on it, and it may be removed without consequence. It differs from Appendix A in one respect that must be stated at the outset — the application is not refuted.')]));
B.push(p([t('The rule is this. The maximum oxidation state of an element is bounded above by the number of electrons outside its last noble-gas core, less any inner d, f or g shell that has completed and is now buried beneath a shell filling later in the sequence. Every term is a lattice quantity: a noble-gas core is a completed down-set of columns, burial is a position in the filling order, and the subtraction is of column capacities. No energy, radius or other metric quantity enters, which is why the rule survives where the six applications of Part V do not.')]));
B.push(p([t('Tested against 93 elements with established maxima and 33 further cases drawn from published superheavy predictions, the bound is violated nowhere and attained exactly in about four fifths of them. It reproduces iridium at +9, the highest oxidation state experimentally verified; hassium at +8, matching the measured HsO₄; and the whole actinide series from actinium to plutonium. Applied to Pyykkö\'s superheavy estimates it returns his own figures, including i = 12 for the hypothetical (E148)O₆.')]));
B.push(p([t('Two deflations are recorded rather than buried. In the d-block the bound reduces to the textbook rule that maximum oxidation state cannot exceed group number, so it is not new there; what the lattice supplies is a uniform derivation across all blocks, an extension into the superheavy region where group assignment is ambiguous, and a rule for where the bound ceases to be attained. And an attempt to extrapolate that second rule to darmstadtium produced a prediction of +10 which the calculated ionisation energies refute. That failure is reported in full, because its cause — extrapolating a metric trend the lattice cannot represent — is the same one Part V diagnoses elsewhere.')],
  {spacing:{before:0,after:200}}));

B.push(h2('B.1  The rule'));
B.push(p([t('An element can lose only those electrons that lie outside a closed, chemically inert core. The lattice identifies both parts of that statement. A noble-gas core is the point at which the occupied columns form a completed down-set — the configuration is closed under the order and no partially filled column remains. Electrons above that core are candidates for removal. But not all of them: an inner d, f or g shell that has filled completely and now lies beneath a shell occurring later in the filling order becomes compact and inert, and its electrons do not ionise. Subtracting those gives')]));
B.push(eq('q_max  ≤  ( Z − Z_core )  −  Σ  cap(c)','B1'));
B.push(p([t('where the sum runs over columns c that are complete and buried. The criterion for burial is positional in the filling order rather than in the shell index, and that distinction is not cosmetic: at ytterbium the 4f shell has just completed and no 5d electron has appeared, so the 4f is still the frontier and its electrons remain available, whereas at lutetium the 5d has begun and the 4f is buried. Taking burial to mean the presence of any higher-n shell instead gives ytterbium and nobelium a bound of 2 against observed maxima of 3, and the rule fails. Taking it positionally, it does not.')]));

B.push(h2('B.2  The test'));
B.push(tcap('B1','Performance of the bound of Equation (B1). Known elements are those with established maximum oxidation states; superheavy cases are drawn from Pyykkö (2011) and from the transactinide literature. A case is tight when the observed or predicted maximum equals the bound exactly.'));
B.push(table(
  ['Group','Cases','Violations','Tight','Notable'],
  [['main group, s and p','24','0','21','Cl, Br, I, At all at +7'],
   ['3d, 4d, 5d series','29','0','23','Ir at +9, the highest verified'],
   ['lanthanides','15','0','3','La, Ce, Lu tight; the rest slack'],
   ['actinides','15','0','7','Ac through Pu tight, +3 to +8'],
   ['6d and 7p transactinides','15','0','10','Sg, Bh, Hs confirmed by measurement'],
   ['Pyykkö superheavy estimates','18','0','12','includes (E148)O₆ at i = 12'],
   ['TOTAL','126','0','76','']],
  [2600,900,1100,900,3100],['TOTAL']));
B.push(p([t('The strongest single case is hassium. Twenty-two electrons lie above radon; the 5f shell has completed and is buried beneath the 6d, so fourteen are subtracted, leaving eight. HsO₄ is a measured compound, prepared one atom at a time, and hassium in it is +8. Osmium reaches the same figure by the same subtraction of a completed 4f. The bound is a lattice-derived integer matching a measurement at the edge of what can be synthesised.')],
  {spacing:{before:160,after:120}}));
B.push(p([t('Applied to the superheavy region the rule returns Pyykkö\'s own estimates without adjustment. His (E144)F₈ and (E144)O₄ sit at eight, which is twenty-six electrons above oganesson less the buried 5g¹⁸. His (E148)O₆ sits at twelve, which is thirty less eighteen. His (E158)X₈ sits at eight, which is forty less the buried 5g¹⁸ and 6f¹⁴. These are not fitted; they follow from the same subtraction applied to his filling order.')]));

B.push(h2('B.3  Where the bound is slack, and why'));
B.push(p([t('The bound holds everywhere and is attained in about four fifths of cases. The remaining fifth is not random. Slack begins past half-filling of the differentiating subshell: below or at half-filling the mean slack is 0.69 and 37 of 45 cases are exact, while above it the mean is 5.36 and only 12 of 36 are exact, a difference significant at p = 9.6 × 10⁻⁷ by Welch\'s test.')]));
B.push(p([t('Restricted to elements past half-filling, the slack behaves differently in each block. In the d-block it is almost perfectly linear in the number of electrons past half-filling, at r = +0.949 over twenty elements, each such electron costing about one and a half units of unrealised oxidation state. In the p-block there is essentially no slack at all, a mean of 0.2 — main-group elements reach their full valence. In the f-block the slack is large and uncorrelated, a mean of 8.5 at r = −0.10: the 4f and 5f electrons simply do not ionise and how many lie past half-filling makes no difference. Pooling the three destroys the signal, which is the same lesson Section 20 draws about the subshell coordinate marking where a relationship changes character.')]));

B.push(h2('B.4  A prediction, and its refutation'));
B.push(p([t('In each of the 3d, 4d and 5d series the bound is attained up to k = n + 2 and the peak oxidation state is n + 4: manganese at +7 with k = 5 and n = 3, ruthenium at +8 with k = 6 and n = 4, iridium at +9 with k = 7 and n = 5. Both quantities are functions of the shell coordinate alone, and the fit is exact across three series. Extrapolated to the 6d series it predicts that darmstadtium, at k = 8, should attain +10 — an oxidation state higher than any proposed.')]));
B.push(p([t('The prediction is wrong, and the data refuting it already existed. Darmstadtium\'s first ionisation energy is calculated at 9.77 electronvolts against platinum\'s 8.96: higher, not lower, because relativistic stabilisation of the 7s orbital binds the valence electrons more tightly, and its covalent radius of 128 picometres is smaller than platinum\'s 139. Platinum, the easier to ionise, reaches +6. The published consensus places darmstadtium at +6 with a volatile DsF₈ raised as a possibility. Nothing supports +10.')]));
B.push(p([t('The failure is worth dissecting because its cause is diagnosable. The pattern k = n + 2 was tested only in the d-block; applied to the p-block it holds in one series of five, and in the f-block in none. It was never a property of the lattice. Its mechanism is the fall of ionisation energies down a group, which permits one further electron per row — a metric trend, of the kind Section 22 establishes the lattice cannot compute. And that trend reverses at the 6d series, where relativistic contraction outweighs the expansion. So the extrapolation assumed monotonicity in a quantity the lattice does not represent, on three points, in the one regime where the trend is known to break. It is the error of Section 12.3 repeated in a new place, and it was found by checking the literature rather than by any further computation.')]));

B.push(h2('B.5  What this appendix offers'));
B.push(p([t('Three things, stated at their proper size.')]));
B.push(p([t('A bound that holds without exception across 126 cases and is attained in four fifths of them, expressed entirely in lattice quantities and therefore free of the metric obstruction that defeats the applications of Part V. In the d-block it coincides with the textbook rule about group number and is not new; across the blocks together, and into the superheavy region where group assignment is contested, the uniform derivation is worth something.')]));
B.push(p([t('A rule for its own slackness: the bound is attained while the differentiating subshell is less than half full and slackens after, with the slackness in the d-block tracking distance past half-filling at r = 0.949. This is the first instance in this work of a metric effect that the lattice cannot compute being located ordinally by the lattice.')]));
B.push(p([t('And a refuted prediction, reported in full. Section 25 of the accompanying paper concedes that six predictive applications failed; this is a seventh that does not fail, together with an eighth extrapolation from it that does. Both belong in the record.')]));

B.push(rule());
B.push(p([t('References for Appendix B',{bold:true,size:23})],{align:AlignmentType.LEFT,spacing:{before:200,after:100}}));
[
 'Düllmann, C. E., Brüchle, W., Dressler, R., et al. (2002). Chemical investigation of hassium (element 108). Nature, 418, 859–862.',
 'Even, J., Yakushev, A., Düllmann, C. E., et al. (2014). Synthesis and detection of a seaborgium carbonyl complex. Science, 345(6203), 1491–1493.',
 'Lach, M. (2026). The Lach Elemental Lattice: An Order-Theoretic Account of the Periodic System. Accompanying paper.',
 'Pyykkö, P. (2011). A suggested periodic table up to Z ≤ 172, based on Dirac–Fock calculations on atoms and ions. Physical Chemistry Chemical Physics, 13(1), 161–168.',
 'Riedel, S., & Kaupp, M. (2009). The highest oxidation states of the transition metal elements. Coordination Chemistry Reviews, 253(5–6), 606–624.',
 'Schädel, M. (2006). Chemistry of superheavy elements. Angewandte Chemie International Edition, 45(3), 368–401.',
 'Wang, G., Zhou, M., Goettel, J. T., et al. (2014). Identification of an iridium-containing compound with a formal oxidation state of IX. Nature, 514, 475–477.',
].forEach((r,i)=>B.push(p([t(`[B${i+1}]  ${r}`,{size:SM})],{spacing:{before:60,after:60}})));
