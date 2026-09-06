// ═══════════════════ POSTSCRIPT ═══════════════════
B.push(new Paragraph({children:[new PageBreak()]}));
B.push(h1('POSTSCRIPT'));
B.push(p([t('An Exploratory Application to Deuteride Host Selection',{bold:true,size:26})],
  {align:AlignmentType.LEFT,spacing:{before:0,after:180}}));
B.push(p([t('This postscript sits outside the numbered parts, and deliberately. Nothing in the account of the lattice depends on it: every result of Parts I through V stands whether or not the work recorded here is read, and the postscript is included because the attempt was made and reporting it is more useful than suppressing it. It records an application that does not succeed, and the analysis of why occupies more space than the application itself.')],
  {spacing:{before:0,after:200}}));

B.push(h2('P1.  Motivation'));
B.push(p([t('The 1989 Fleischmann–Pons experiments used palladium, and palladium has dominated the subsequent literature. The choice was reasonable on practical grounds — palladium absorbs hydrogen readily, is workable, is not toxic, and was available — but it was not the product of a search over host materials guided by any structural principle, because no such principle was available.')]));
B.push(p([t('The adjacency result of Section 17 suggests a line of attack. If the late f-block and the late 5d metals form a coherent region in configuration space, and palladium sits at the edge of that region rather than within it, then the lattice identifies neighbouring elements that a palladium-centred literature would not naturally have reached. Section 23.1 gives the idea a firmer footing than geometry alone would: hydride formation enthalpy, which determines whether a metal loads hydrogen and how tightly it holds it, is predicted from ℓ and k at cross-validated R² = 0.51. Loading is the precondition for any deuteride experiment. That claim extends to the chemistry of loading and no further.')]));

B.push(h2('P2.  A Heuristic Index'));
B.push(p([t('We construct an index intended to capture two intuitions: that an element deep in configuration space presents a more complex electronic environment at interstitial sites, and that higher-ℓ subshells contribute more interstitial density at appreciable filling. The index is')]));
B.push(eq('H_cp(n, ℓ, k)  =  √(n² + ℓ² + k²) · ( k / 2(2ℓ+1) )^(ℓ/4)','16'));
B.push(p([t('the first factor being the configuration-space distance from the origin and the second the fractional subshell filling raised to a power increasing with ℓ, normalised by the lattice ceiling ℓ_max = 4.')]));
B.push(p([t('This expression is a choice, and it is flagged as such rather than presented as derived. Infinitely many monotone functions of ℓ and k satisfy the stated intuitions; the exponent ℓ/4 was selected for its normalisation against the lattice ceiling and because it is the simplest such form, not because the framework requires it. A different exponent gives a different index and, as Section P4 shows, a different ordering. The index has no dimensions and no interpretation as a rate, an energy or a probability. It is a sorting device.')]));

B.push(h2('P3.  The Screen'));
B.push(p([t('Two filters are applied to all 118 elements. The first is chemical: the host must form a well-characterised interstitial hydride or deuteride, since a metal that does not absorb deuterium cannot serve as a loading matrix. The second is structural. In a face-centred cubic lattice the octahedral interstitial sites are all equivalent by symmetry and occur six to the unit cell, so three deuterons can occupy translationally equivalent positions; in hexagonal close packing the octahedral sites are not all equivalent and the geometry depends on the c/a ratio, and in double hexagonal packing the layer alternation breaks equivalence outright. FCC is therefore taken as the permissive case. Neither filter derives from the lattice — both are ordinary crystallography, imported. The lattice contributes only the index by which survivors are sorted.')]));
B.push(img('F16_screening.png',620,232));
B.push(cap(16,'Screening across the elements. (a) Configuration-space distance |Q₀| against atomic number, with elements passing both filters ringed; the three labelled entries are Pd, Pt and Yb. (b) The two-filter funnel: 118 elements reduce to nine candidates.'));
B.push(tcap(3,'Candidates passing both filters, ordered by the heuristic index. The ordering is convention-dependent — see Section P4.'));
B.push(table(
  ['Rank','El.','(n, ℓ, k)','|Q₀|','H_cp','Class','Note'],
  [['1','Yb','(4, 3, 13)','13.93','13.18','C','apparently untested'],
   ['2','Au','(5, 2, 9)','10.49','9.95','B','poor absorber'],
   ['3','Ag','(4, 2, 9)','10.05','9.53','B','weak absorber'],
   ['4','Pt','(5, 2, 8)','9.64','8.63','B','well studied'],
   ['5','Pd','(4, 2, 8)','9.17','8.20','B','historical host'],
   ['6','Ni','(3, 2, 8)','8.78','7.85','C','well studied'],
   ['7','Ir','(5, 2, 7)','8.83','7.39','B','little studied'],
   ['8','Rh','(4, 2, 7)','8.31','6.95','B','little studied'],
   ['9','Th','(5, 3, 1)','5.92','0.82','B','radioactive']],
  [700,700,1500,900,900,900,2200],['1']));
B.push(p([t('The entry that stands out is ytterbium. It has the largest configuration-space distance of any candidate, forms YbH₂ and YbH₃ under accessible conditions, adopts an FCC structure, is stable and commercially available — and a survey of the deuteride-loading literature turns up no report of its use as a primary host. Whatever the status of the index that ranked it, the observation that a chemically suitable, structurally suitable, commercially available metal appears never to have been tried is independent of the index and stands on its own.')],
  {spacing:{before:160,after:120}}));

B.push(h2('P4.  Why the Ordering Is Not a Prediction'));
B.push(p([t('Table 3 sorts by the index alone. The screen involves further modelling choices, and varying them within the range of defensible options is decisive.')]));
B.push(p([t('A phase term may be introduced to represent the geometric relationship between occupied interstitial sites, requiring a lattice parameter. That parameter may be taken from measurement or estimated from the lattice via a screening model — Slater\'s rules, or Clementi–Raimondi values, applied either to the valence orbital or to the bonding orbital. Each is a reasonable choice, and each yields a different ordering.')]));
B.push(img('F17_convention.png',520,288));
B.push(cap(17,'Candidate ordering under three modelling conventions. Ytterbium ranks first under two and fourth under the third; palladium moves between third and fifth. Because the ordering is not stable across defensible choices, it is a property of the convention adopted rather than a result derived from the lattice.'));
B.push(p([t('Ytterbium ranks first under two conventions and fourth under a third; platinum ranks fourth, sixth and eighth. When a result depends on which of several equally justifiable conventions the analyst adopts, that result characterises the choice and not the structure under study. The ordering is therefore reported as one convention\'s output, not as a prediction.')]));
B.push(p([t('Two intermediate steps in the exploratory work were initially presented as derivations and were not. An interaction term of the form γ·Q̂⊗Q̂ was described as the natural coupling; it is one choice among many, and alternatives give different functional forms downstream. The exponent ℓ/4 in Equation (16) was described as the unique form satisfying the stated constraints; it is not unique, and it was selected after the index it appears in had already been written down. Both are recorded here as choices.')]));

B.push(h2('P5.  The Dimensional Obstruction'));
B.push(p([t('A more fundamental limitation applies regardless of convention, and no refinement of the screening model addresses it. It is the obstruction of Section 22, restated in the setting where it was first encountered.')]));
B.push(p([t('The index is dimensionless, being assembled from three integers. Deuteron–deuteron fusion proceeds through Coulomb barrier penetration, whose probability goes as exp(−G) with the Gamow factor built from the reduced mass in kilograms, the barrier height in joules, and the internuclear separation in metres. Converting a dimensionless lattice ratio into a rate requires a dimensional scale, and Section 22.1 establishes that the framework supplies none — not by omission but by construction, since Λ ⊆ ℕ³.')]));
B.push(p([t('One might attempt to supply a scale from the physical geometry of the deuterium configuration, an interstitial separation of order 10⁻¹⁰ m. But the relevant separation for tunnelling is the distance of closest approach, some five orders of magnitude smaller, and any assumed relation between the index and that separation is precisely the physical content one is trying to derive. The exponential sensitivity of exp(−G) makes this fatal rather than merely imprecise.')]));
B.push(img('F18_scalegap.png',620,226));
B.push(cap(18,'The dimensional obstruction. (a) The lattice produces dimensionless quantities; barrier penetration requires dimensional ones, and the framework provides no bridge. (b) Sensitivity of the predicted Yb : Pd rate ratio to an assumed relation between the index and the effective separation. Varying the exponent over a modest range moves the predicted ratio across twenty orders of magnitude.'));
B.push(p([t('Figure 18(b) makes the point quantitatively. A ratio of roughly six in the index is compatible with a rate ratio of unity, or of 10²⁰, according to an exponent that nothing constrains. It follows that this postscript cannot yield a falsifiable prediction in the ordinary sense: were ytterbium to show no anomalous behaviour whatever, no quantity in this framework would be contradicted, because none was ever committed to a magnitude.')]));
B.push(p([t('A further caution. The three-body treatment in the exploratory work was motivated by the lattice having three axes. But (n, ℓ, k) are quantum numbers — a shell index, an angular momentum, a count — and their being three in number is not a statement about physical space. Reasoning from the dimensionality of the coordinate system to the geometry of a physical configuration conflates two distinct senses of the word.')]));
B.push(p([t('Nor does the chemical-scale result of Section 23.1 bridge the gap. Hydride formation enthalpies are of order 10⁻¹ eV over interatomic distances of order 10⁻¹⁰ m; Coulomb barriers are of order 10⁵ eV over separations of order 10⁻¹⁵ m. A correlation demonstrated at the first scale carries no implication for the second — that six-order gap in energy and five-order gap in length is the whole reason the problem is difficult. Equation (15) predicts how much deuterium a metal will absorb. It says nothing about what happens to the deuterons once absorbed.')]));

B.push(h2('P6.  What the Postscript Offers'));
B.push(p([t('Stripped of the claims it cannot support, the work recorded here leaves three things.')]));
B.push(p([t('First, a candidate-generation heuristic. The lattice, combined with two crystallographic filters, reduces 118 elements to nine and directs attention to a region of the periodic system that a palladium-centred literature has not systematically explored. Heuristics of this kind are legitimate and useful provided they are not mistaken for theories.')]));
B.push(p([t('Second, a specific and checkable observation. Ytterbium satisfies every practical criterion for a deuteride-loading host — FCC structure, established hydride chemistry, stability, availability — and appears absent from the experimental record. That absence is a fact about the literature, not a consequence of the index, and it would remain interesting if Equation (16) were discarded entirely.')]));
B.push(p([t('Third, a worked negative result. The dimensional obstruction is not peculiar to this framework; it applies to any scheme that attempts to reason from combinatorial or configuration-space quantities to nuclear rates. Documenting where the boundary lies has some value in a field with a long history of frameworks that did not identify their own.')]));

B.push(rule());
B.push(h2('References'));
[
 'Birkhoff, G. (1967). Lattice Theory, 3rd ed. Providence: American Mathematical Society Colloquium Publications, vol. 25.',
 'Bohr, N. (1913). On the constitution of atoms and molecules. Philosophical Magazine, 26(151), 1–25.',
 'Clementi, E., & Raimondi, D. L. (1963). Atomic screening constants from SCF functions. Journal of Chemical Physics, 38(11), 2686–2689.',
 'Dirac, P. A. M. (1930). The Principles of Quantum Mechanics. Oxford: Oxford University Press.',
 'Dushnik, B., & Miller, E. W. (1941). Partially ordered sets. American Journal of Mathematics, 63(3), 600–610.',
 'Fleischmann, M., & Pons, S. (1989). Electrochemically induced nuclear fusion of deuterium. Journal of Electroanalytical Chemistry, 261(2A), 301–308.',
 'Gamow, G. (1928). Zur Quantentheorie des Atomkernes. Zeitschrift für Physik, 51(3–4), 204–212.',
 'Glawe, H., Sanna, A., Gross, E. K. U., & Marques, M. A. L. (2016). The optimal one-dimensional periodic table: a modified Pettifor chemical scale from data mining. New Journal of Physics, 18, 093011.',
 'Janet, C. (1929). La classification hélicoïdale des éléments chimiques. Beauvais: Imprimerie Départementale de l\'Oise.',
 'Leal, W., & Restrepo, G. (2019). Formal structure of periodic system of elements. Proceedings of the Royal Society A, 475(2224), 20180581.',
 'Madelung, E. (1936). Die mathematischen Hilfsmittel des Physikers, 3rd ed. Berlin: Springer.',
 'Mendeleev, D. (1869). On the relationship of the properties of the elements to their atomic weights. Zeitschrift für Chemie, 12, 405–406.',
 'Miedema, A. R., de Châtel, P. F., & de Boer, F. R. (1980). Cohesion in alloys — fundamentals of a semi-empirical model. Physica B+C, 100(1), 1–28.',
 'Moseley, H. G. J. (1913). The high-frequency spectra of the elements. Philosophical Magazine, 26(156), 1024–1034.',
 'Pauli, W. (1925). Über den Zusammenhang des Abschlusses der Elektronengruppen im Atom mit der Komplexstruktur der Spektren. Zeitschrift für Physik, 31(1), 765–783.',
 'Pettifor, D. G. (1984). A chemical scale for crystal-structure maps. Solid State Communications, 51(1), 31–34.',
 'Pyykkö, P. (2011). A suggested periodic table up to Z ≤ 172, based on Dirac–Fock calculations on atoms and ions. Physical Chemistry Chemical Physics, 13(1), 161–168.',
 'Quintero, N. Y., Brüggemann, R., & Restrepo, G. (2018). Mapping posets into low dimensional spaces: the case of uranium trappers. MATCH Communications in Mathematical and in Computer Chemistry, 80(3), 793–820.',
 'Scerri, E. R. (2007). The Periodic Table: Its Story and Its Significance. Oxford: Oxford University Press.',
 'Schrödinger, E. (1926). An undulatory theory of the mechanics of atoms and molecules. Physical Review, 28(6), 1049–1070.',
 'Seaborg, G. T. (1945). The transuranium elements. Science, 104(2704), 379–386.',
 'Slater, J. C. (1930). Atomic shielding constants. Physical Review, 36(1), 57–64.',
 'Trotter, W. T. (1992). Combinatorics and Partially Ordered Sets: Dimension Theory. Baltimore: Johns Hopkins University Press.',
 'Villars, P., Brandenburg, K., Berndt, M., LeClair, S., et al. (2001). Binary, ternary and quaternary compound former/nonformer prediction via Mendeleev number. Journal of Alloys and Compounds, 317–318, 26–38.',
 'Widom, A., & Larsen, L. (2006). Ultra low momentum neutron catalyzed nuclear reactions on metallic hydride surfaces. European Physical Journal C, 46(1), 107–111.',
].forEach((r,i)=>B.push(p([t(`[${i+1}]  ${r}`,{size:SM})],{spacing:{before:60,after:60}})));

// ═══════════════════ DOCUMENT ═══════════════════
const doc=new Document({
  styles:{default:{document:{run:{font:F,size:S,color:'111111'}}}},
  sections:[{
    properties:{page:{size:{width:12240,height:15840},
      margin:{top:convertInchesToTwip(1.0),bottom:convertInchesToTwip(1.0),
              left:convertInchesToTwip(1.15),right:convertInchesToTwip(1.15)}}},
    footers:{default:new Footer({children:[p([
      t('Lach — The Lach Elemental Lattice  ·  ',{size:16,color:'888888'}),
      new TextRun({children:[PageNumber.CURRENT],font:F,size:16,color:'888888'})],
      {align:AlignmentType.CENTER,spacing:{before:0,after:0}})]})},
    children:B}]});
Packer.toBuffer(doc).then(b=>{
  fs.writeFileSync('/home/claude/v2/Lach_Elemental_Lattice_2026.docx',b);
  console.log('built');
});
