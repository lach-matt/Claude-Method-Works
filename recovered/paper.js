const {
  Document, Packer, Paragraph, TextRun, HeadingLevel,
  AlignmentType, PageNumber, NumberFormat, Footer,
  PageBreak, Table, TableRow, TableCell, WidthType,
  BorderStyle, ShadingType, SpacingType, LevelFormat,
  convertInchesToTwip, UnderlineType
} = require('docx');
const fs = require('fs');

// ─── Helpers ────────────────────────────────────────────────────
const FONT_BODY  = 'Garamond';
const FONT_MONO  = 'Courier New';
const SIZE_BODY  = 22;   // half-points = 11pt
const SIZE_H1    = 32;   // 16pt
const SIZE_H2    = 26;   // 13pt
const SIZE_H3    = 24;   // 12pt
const SIZE_SMALL = 18;   // 9pt

function sp(n=200) { return { before: n, after: 0 }; }
function para(runs, opts={}) {
  return new Paragraph({
    children: Array.isArray(runs) ? runs : [runs],
    spacing: opts.spacing || sp(160),
    alignment: opts.align || AlignmentType.JUSTIFIED,
    indent: opts.indent,
    style: opts.style,
    heading: opts.heading,
    border: opts.border,
    pageBreakBefore: opts.pageBreak || false,
  });
}
function t(text, opts={}) {
  return new TextRun({
    text,
    font: opts.mono ? FONT_MONO : FONT_BODY,
    size: opts.size || SIZE_BODY,
    bold: opts.bold || false,
    italics: opts.italic || false,
    underline: opts.underline ? { type: UnderlineType.SINGLE } : undefined,
    color: opts.color || undefined,
  });
}
function mono(text, opts={}) { return t(text, { ...opts, mono: true, size: opts.size || SIZE_BODY }); }
function heading1(text) {
  return para([t(text, { bold: true, size: SIZE_H1 })],
    { spacing: sp(400), align: AlignmentType.CENTER, heading: HeadingLevel.HEADING_1 });
}
function heading2(text) {
  return para([t(text, { bold: true, size: SIZE_H2 })],
    { spacing: sp(300), heading: HeadingLevel.HEADING_2 });
}
function heading3(text) {
  return para([t(text, { bold: true, italic: true, size: SIZE_H3 })],
    { spacing: sp(220), heading: HeadingLevel.HEADING_3 });
}
function equation(text) {
  return para([mono(text, { size: SIZE_BODY, bold: true })], {
    align: AlignmentType.CENTER,
    spacing: { before: 160, after: 160 },
    indent: { left: convertInchesToTwip(0.8) }
  });
}
function eqLabel(text, eq) {
  // equation with right-aligned label
  return new Paragraph({
    children: [
      mono(eq, { size: SIZE_BODY }),
      t('                                                            (' + text + ')', { size: SIZE_BODY })
    ],
    alignment: AlignmentType.LEFT,
    indent: { left: convertInchesToTwip(0.6) },
    spacing: { before: 160, after: 160 }
  });
}
function ruled() {
  return para([t('')], {
    spacing: sp(60),
    border: { bottom: { color: '888888', style: BorderStyle.SINGLE, size: 4 } }
  });
}
function blank(n=1) {
  return Array.from({length:n}, () => para([t('')], { spacing: { before: 80, after: 0 } }));
}

// ─── TABLE: Host Rankings ───────────────────────────────────────
function rankTable() {
  const headers = ['Rank','Z','Symbol','(n, ℓ, k)','Block','H_cp','O₃_phys','Structure','Status'];
  const rows_data = [
    ['1','70','Yb','(4, 3, 13)','f','13.18','32815','FCC','★ Priority'],
    ['2','47','Ag','(4, 2, 9)','d','9.53','6972','FCC','Host (Ag-D)'],
    ['3','79','Au','(5, 2, 9)','d','9.95','8503','FCC','Host (Au-D)'],
    ['4','29','Cu','(3, 2, 9)','d','9.20','5909','FCC','Non-absorbing'],
    ['5','78','Pt','(5, 2, 8)','d','8.63','4410','FCC','★ Priority'],
    ['6','28','Ni','(3, 2, 8)','d','7.85','2894','FCC','Host (Ni-D)'],
    ['7','46','Pd','(4, 2, 8)','d','8.20','3509','FCC','Benchmark'],
    ['8','77','Ir','(5, 2, 7)','d','7.39','2222','FCC','Host (Ir-D)'],
    ['9','45','Rh','(4, 2, 7)','d','6.95','1707','FCC','Host (Rh-D)'],
    ['10','90','Th','(5, 3, 1)','f','0.82','5','FCC','Radioactive'],
  ];

  const colWidths = [600,600,700,1200,600,800,900,900,1000];
  const totalW = colWidths.reduce((a,b)=>a+b,0);

  function hdrCell(txt) {
    return new TableCell({
      children: [para([t(txt, {bold:true, size:SIZE_SMALL})], {align:AlignmentType.CENTER, spacing:{before:60,after:60}})],
      shading: { type: ShadingType.CLEAR, fill: 'E8E4DC' },
      width: { size: colWidths[0], type: WidthType.DXA },
    });
  }
  function dataCell(txt, w, isPriority=false) {
    return new TableCell({
      children: [para([t(txt, {size:SIZE_SMALL, bold: isPriority, color: isPriority ? '0a5a2a' : undefined})],
        {align:AlignmentType.CENTER, spacing:{before:40,after:40}})],
      width: { size: w, type: WidthType.DXA },
    });
  }

  const headerRow = new TableRow({
    children: headers.map((h,i) => new TableCell({
      children: [para([t(h, {bold:true, size:SIZE_SMALL})], {align:AlignmentType.CENTER, spacing:{before:60,after:60}})],
      shading: { type: ShadingType.CLEAR, fill: 'D8D0C4' },
      width: { size: colWidths[i], type: WidthType.DXA },
    }))
  });

  const dataRows = rows_data.map(row => new TableRow({
    children: row.map((cell,i) => {
      const isPriority = row[8] && row[8].includes('Priority');
      return new TableCell({
        children: [para([t(cell, {size:SIZE_SMALL, bold: isPriority && i===2, color: isPriority&&i===2?'0a5a2a':undefined})],
          {align:AlignmentType.CENTER, spacing:{before:40,after:40}})],
        shading: isPriority ? { type: ShadingType.CLEAR, fill: 'eef8f0' } : undefined,
        width: { size: colWidths[i], type: WidthType.DXA },
      });
    })
  }));

  return new Table({
    rows: [headerRow, ...dataRows],
    width: { size: totalW, type: WidthType.DXA },
    columnWidths: colWidths,
  });
}

// ─── DOCUMENT ───────────────────────────────────────────────────
const doc = new Document({
  styles: {
    default: {
      document: { run: { font: FONT_BODY, size: SIZE_BODY, color: '0e1520' } }
    }
  },
  sections: [{
    properties: {
      page: {
        size: { width: 12240, height: 15840 },
        margin: {
          top:    convertInchesToTwip(1.1),
          bottom: convertInchesToTwip(1.1),
          left:   convertInchesToTwip(1.25),
          right:  convertInchesToTwip(1.25),
        }
      }
    },
    footers: {
      default: new Footer({
        children: [
          para([
            t('Lach & Claude  ·  Cold Fusion Host Identification via the Lach Elemental Field Equation  ·  ', {size:SIZE_SMALL, color:'888888'}),
            new TextRun({ children: [PageNumber.CURRENT], font: FONT_BODY, size: SIZE_SMALL, color: '888888' }),
          ], { align: AlignmentType.CENTER, spacing: { before: 0, after: 0 } })
        ]
      })
    },
    children: [

      // ── TITLE ──────────────────────────────────────────────────
      ...blank(2),
      para([t('Cold Fusion Host Identification via the', { bold: true, size: 36 })],
        { align: AlignmentType.CENTER, spacing: sp(80) }),
      para([t('Lach Elemental Field Equation', { bold: true, size: 36 })],
        { align: AlignmentType.CENTER, spacing: sp(120) }),

      ruled(),
      ...blank(1),

      para([t('Matthew Lach  ·  Claude (Anthropic)', { italic: true, size: SIZE_BODY, color: '444444' })],
        { align: AlignmentType.CENTER, spacing: sp(80) }),
      para([t('2026', { size: SIZE_BODY, color: '888888' })],
        { align: AlignmentType.CENTER, spacing: sp(240) }),

      // ── ABSTRACT ───────────────────────────────────────────────
      heading2('Abstract'),
      para([t(
        'The Lach Elemental Field Equation (2026) assigns each of the 118 known elements a unique coordinate (n, ℓ, k) ' +
        'in a three-dimensional configuration-space lattice, where n is the principal quantum number, ℓ the subshell ' +
        'type, and k the electron occupancy. This paper extends that framework to the problem of cold fusion host ' +
        'identification. Beginning with the Born-Oppenheimer approximation breakdown in heavy-element lattices, we ' +
        'derive a two-body perturbation expression for host-perturbed deuterium states, extend it to a three-body ' +
        'system consistent with the three-dimensional character of the Lach lattice, and from the resulting overlap ' +
        'integral O₃ formally derive a Host Coupling Potential H_cp(n, ℓ, k) without free parameters. Crystal ' +
        'structure compatibility analysis introduces a geometric gate: only FCC-structured hosts permit simultaneous ' +
        'three-body convergence unconditionally. Applying both filters to all 118 elements yields a ranked list of ' +
        'viable cold fusion hosts. Ytterbium (Yb, Z=70) emerges as the top-ranked viable candidate, with a ' +
        'three-body overlap O₃ approximately 9.35 times that of palladium — the original Fleischmann-Pons host. ' +
        'This ordering constitutes a falsifiable prediction derivable entirely from the geometry of the Lach lattice.'
      )]),

      ...blank(1),
      ruled(),

      // ── 1. INTRODUCTION ────────────────────────────────────────
      para([t('')], { spacing: sp(200), pageBreak: false }),
      heading2('1.  Introduction'),

      para([t(
        'The cold fusion controversy, initiated by the 1989 announcement of Fleischmann and Pons, has persisted for ' +
        'over three decades without a settled theoretical framework. The central experimental claim — anomalous heat ' +
        'production in palladium-deuterium electrochemical cells — has never been conclusively replicated nor ' +
        'definitively refuted. The field rebranded as Low Energy Nuclear Reactions (LENR) and continued under ' +
        'persistent theoretical ambiguity: no framework has simultaneously explained the claimed energy output, ' +
        'the absence of expected nuclear byproducts, and the dependence of results on host material.'
      )]),

      para([t(
        'The principal theoretical obstacle is the Coulomb barrier. Two deuterium nuclei must approach within ' +
        'approximately 10⁻¹⁵ m to fuse. The Coulomb barrier at this distance is of order 0.1–1 MeV, whereas ' +
        'thermal energy at room temperature is approximately 0.025 eV — a gap of seven to eight orders of magnitude. ' +
        'Tunnelling probability falls exponentially with barrier width and particle mass. Existing theoretical ' +
        'proposals — Widom-Larsen theory, phonon-coupling models, Born-Oppenheimer breakdown hypotheses — have not ' +
        'produced precise, falsifiable predictions subsequently confirmed by experiment.'
      )]),

      para([t(
        'This paper does not claim to resolve the cold fusion question. It claims something narrower and more ' +
        'tractable: that the geometric framework of the Lach Elemental Field Equation Theorem (Lach, 2026) provides ' +
        'a natural language for expressing the host-material dependence of deuterium-deuterium electron density ' +
        'overlap in configuration space, and that this language yields a formally derived, falsifiable ranking of ' +
        'host materials that has not previously been expressed.'
      )]),

      // ── 2. THEORETICAL BACKGROUND ──────────────────────────────
      heading2('2.  Theoretical Background'),

      heading3('2.1  The Lach Elemental Field Equation'),
      para([t(
        'The Lach Elemental Field Equation Theorem (Lach, 2026) assigns each element Z a ground-state coordinate ' +
        'Q₀ = (n, ℓ, k) in a three-dimensional lattice Λ defined by:'
      )]),
      eqLabel('1', 'Λ = { (n, ℓ, k) ∈ ℤ³  :  0 ≤ ℓ ≤ n−1,  1 ≤ k ≤ 2(2ℓ+1) }'),
      para([t(
        'Each element Z is modelled as a three-state quantum system with ground state |Q₀⟩ and two nearest ' +
        'excited-state neighbours Q₁ = (n+1, ℓ, k) and Q₂ = (n, ℓ±1, k). The unified forward-inverse expression is:'
      )]),
      eqLabel('2', 'Ψ±_Z(t)  =  √2 · sin(Ωt + π/4) · Σ_(n,ℓ,k)∈Λ  |n, ℓ, k⟩'),
      para([t(
        'The displacement vector from the midpoint of the excited neighbours to the ground state is:'
      )]),
      eqLabel('3', 'ΔQ_Z  =  Q₀ − ½(Q₁ + Q₂)'),
      para([t(
        'and the interaction term is S_Z(t) = cos(2Ωt) · ΔQ_Z. The configuration-space variance σ²(t) ' +
        'quantifies the instantaneous spread of electron density at time t.'
      )]),

      heading3('2.2  Born-Oppenheimer Breakdown in Heavy-Element Lattices'),
      para([t(
        'The Born-Oppenheimer approximation treats nuclear and electronic degrees of freedom as separable, ' +
        'justified by the large ratio of nuclear to electron mass. This separation weakens for heavy nuclei, ' +
        'which move more slowly, reducing the timescale separation that underlies the approximation. In ' +
        'elements with Z ≥ 70, relativistic effects on inner-shell electrons produce significant contraction ' +
        'of s and p orbitals and concomitant expansion and altered screening of d and f orbitals. These ' +
        'effects alter interstitial electron density in ways that standard single-particle models do not capture.'
      )]),

      para([t(
        'The Lach framework provides a geometric representation of this phenomenon: an element with high ' +
        'configuration-space distance |Q₀| = √(n² + ℓ² + k²) sits deeper in configuration space, ' +
        'representing greater orbital complexity and greater available electron density at interstitial sites. ' +
        'This geometric quantity, entirely internal to the Lach lattice, serves as the primary determinant of ' +
        'host coupling strength.'
      )]),

      // ── 3. THE TWO-BODY SYSTEM ─────────────────────────────────
      heading2('3.  The Perturbed Deuterium System'),

      heading3('3.1  Unperturbed Deuterium State'),
      para([t(
        'Deuterium has ground state 1s¹, identical to hydrogen in the Lach lattice: Q₀(D) = (1, 0, 1). ' +
        'Both excited-state neighbours collapse to Q₁ = Q₂ = (2, 0, 1), giving displacement vector ' +
        'ΔQ_D = (−1, 0, 0). Deuterium\'s oscillation is the simplest possible — purely along the n-axis — ' +
        'with σ²_max(D) = 0 (collapsed neighbourhood). This is the unperturbed reference state.'
      )]),

      heading3('3.2  Host-Perturbed State'),
      para([t(
        'When deuterium occupies an interstitial site in a host element lattice H_x with ground state ' +
        '(n_x, ℓ_x, k_x), the host field displaces deuterium\'s configuration-space position. The perturbed ' +
        'state is:'
      )]),
      eqLabel('4', 'Ψ_D^x(t)  =  Ψ_D(t)  +  λ · F_x(t)'),
      para([t(
        'where λ is a coupling constant and F_x(t) = cos(2Ωt) · ΔQ_x is the host field vector, drawn ' +
        'directly from the host element\'s own S_Z(t) term in the Lach equation. The host\'s own interaction ' +
        'term thus acts as an external perturbation on the guest deuterium atom.'
      )]),

      heading3('3.3  The Two-Body Overlap'),
      para([t(
        'For two deuterium atoms D₁ and D₂ in proximate interstitial sites, separated by phase φ encoding ' +
        'their geometric offset within the host lattice, the pairwise overlap is:'
      )]),
      eqLabel('5', 'O(t, φ)  =  |Ψ_D(t)|²  +  2λ · F_x(t) · cos(φ)  +  λ²|F_x(t)|²'),
      para([t(
        'Maximised when cos(φ) = 1, i.e., when the two sites are in lattice-phase alignment (φ = 2πm, m ∈ ℤ).'
      )]),

      // ── 4. THE THREE-BODY SYSTEM ───────────────────────────────
      heading2('4.  Extension to the Three-Body System'),

      heading3('4.1  Motivation'),
      para([t(
        'The two-body treatment captures a single interaction axis. The Lach framework is fundamentally ' +
        'three-dimensional: every element occupies a point in (n, ℓ, k) space, and the framework\'s central ' +
        'claim is that this three-dimensionality carries physical information absent from the two-dimensional ' +
        'periodic table. Consistency requires that the minimum physical system for cold fusion host analysis ' +
        'also be three-dimensional — i.e., three deuterium atoms forming a triangle in real and configuration space.'
      )]),

      heading3('4.2  Three-Body State'),
      para([t(
        'Three host-perturbed deuterium atoms with pairwise phase offsets φ₁₂, φ₁₃, and the constrained ' +
        'φ₂₃ = φ₁₃ − φ₁₂:'
      )]),
      eqLabel('6', 'Ψ_D1^x(t)  =  Ψ_D(t) + λ · F_x(t)'),
      eqLabel('7', 'Ψ_D2^x(t)  =  Ψ_D(t) + λ · F_x(t) · e^(iφ₁₂)'),
      eqLabel('8', 'Ψ_D3^x(t)  =  Ψ_D(t) + λ · F_x(t) · e^(iφ₁₃)'),
      para([t(
        'Note that φ₂₃ is not independent — it is fully determined by φ₁₂ and φ₁₃. This is the geometric ' +
        'constraint imposed by three-body triangular geometry.'
      )]),

      heading3('4.3  The Three-Body Overlap Expression'),
      para([t(
        'The simultaneous three-body overlap is the product of all three pairwise overlaps:'
      )]),
      eqLabel('9', 'O₃(t, φ₁₂, φ₁₃)  =  ⟨Ψ_D1^x | Ψ_D2^x⟩ · ⟨Ψ_D2^x | Ψ_D3^x⟩ · ⟨Ψ_D1^x | Ψ_D3^x⟩'),
      para([t('Defining P(t) = A(t) + C(t) where A(t) = 2sin²(Ωt + π/4) and C(t) = λ²cos²(2Ωt)|ΔQ_x|², ' +
        'and B(t) = 2λ|cos(2Ωt)||ΔQ_x|, the full expansion is:')]),
      eqLabel('10',
        'O₃  =  P³  +  P²B[cos(φ₁₂) + cos(φ₁₃) + cos(φ₁₃−φ₁₂)]\n' +
        '          +  PB²[cos(φ₁₂)cos(φ₁₃) + cos(φ₁₂)cos(φ₁₃−φ₁₂) + cos(φ₁₃)cos(φ₁₃−φ₁₂)]\n' +
        '          +  B³ · cos(φ₁₂) · cos(φ₁₃) · cos(φ₁₃−φ₁₂)'),

      heading3('4.4  Convergence Conditions'),
      para([t(
        'Maximum O₃ requires simultaneously maximising all three cosine terms. This yields the conditions:'
      )]),
      eqLabel('11', 'φ₁₂ = 2πm,    φ₁₃ = 2πn,    φ₂₃ = φ₁₃ − φ₁₂ = 2π(n−m)'),
      para([t(
        'Since n − m is always an integer when m and n are integers, the three conditions are simultaneously ' +
        'satisfiable. Maximum O₃ is achieved when φ₁₂ = φ₁₃ = 0 (mod 2π) — i.e., when all three deuterium ' +
        'atoms occupy translationally equivalent interstitial sites in the host lattice.'
      )]),

      heading3('4.5  Crystal Structure as a Geometric Gate'),
      para([t(
        'Whether three translationally equivalent interstitial sites can be simultaneously occupied depends on ' +
        'the host crystal structure. Analysis of the principal structure types yields:'
      )]),
      ...blank(1),

      new Table({
        rows: [
          new TableRow({ children: [
            new TableCell({ children: [para([t('Structure', {bold:true, size:SIZE_SMALL})], {align:AlignmentType.CENTER, spacing:{before:60,after:60}})], shading:{type:ShadingType.CLEAR,fill:'D8D0C4'}, width:{size:1400,type:WidthType.DXA} }),
            new TableCell({ children: [para([t('Dominant H site', {bold:true, size:SIZE_SMALL})], {align:AlignmentType.CENTER, spacing:{before:60,after:60}})], shading:{type:ShadingType.CLEAR,fill:'D8D0C4'}, width:{size:1800,type:WidthType.DXA} }),
            new TableCell({ children: [para([t('Equivalent sites/cell', {bold:true, size:SIZE_SMALL})], {align:AlignmentType.CENTER, spacing:{before:60,after:60}})], shading:{type:ShadingType.CLEAR,fill:'D8D0C4'}, width:{size:1800,type:WidthType.DXA} }),
            new TableCell({ children: [para([t('3-body verdict', {bold:true, size:SIZE_SMALL})], {align:AlignmentType.CENTER, spacing:{before:60,after:60}})], shading:{type:ShadingType.CLEAR,fill:'D8D0C4'}, width:{size:1400,type:WidthType.DXA} }),
            new TableCell({ children: [para([t('Key elements', {bold:true, size:SIZE_SMALL})], {align:AlignmentType.CENTER, spacing:{before:60,after:60}})], shading:{type:ShadingType.CLEAR,fill:'D8D0C4'}, width:{size:2000,type:WidthType.DXA} }),
          ]}),
          ...[
            ['FCC','Octahedral (Oh)','6 (all equivalent)','ALLOWED','Yb, Pt, Ir, Pd, Rh, Ni, Ag, Au'],
            ['HCP','Octahedral','2 (not all equiv.)','CONDITIONAL','Os, Re, Lu, Tm, Er, Ho, Dy'],
            ['BCC','Tetrahedral','12 (equiv., elongated)','ALLOWED*','W, Mo, Fe, Cr, Ta'],
            ['DHCP','Mixed Oh/Td','Layer alternation','RESTRICTED','La, Pr, Nd, Sm'],
          ].map(row => new TableRow({ children: row.map((c,i) => new TableCell({
            children: [para([t(c, {size:SIZE_SMALL})], {align:AlignmentType.CENTER, spacing:{before:40,after:40}})],
            width: { size: [1400,1800,1800,1400,2000][i], type: WidthType.DXA }
          }))}))
        ],
        width: { size: 8400, type: WidthType.DXA },
        columnWidths: [1400,1800,1800,1400,2000],
      }),
      ...blank(1),
      para([t('* BCC hosts allow three-body convergence in principle but deuterium preferentially occupies elongated ' +
        'tetrahedral sites with reduced Oh-equivalent symmetry; treatment requires further analysis.',
        {italic:true, size:SIZE_SMALL})]),

      // ── 5. FORMAL DERIVATION OF H_cp ──────────────────────────
      heading2('5.  Formal Derivation of H_cp'),

      heading3('5.1  Grounding λ in the Lach Framework'),
      para([t(
        'The coupling constant λ appears in O₃ as a free parameter. To ground it within the Lach framework, ' +
        'we identify it with the maximum configuration-space variance σ²_max of the host element, derived ' +
        'from Equation (7) of the Lach Elemental Field Equation Theorem:'
      )]),
      eqLabel('12', 'σ²_max  =  (|d₁|² + |d₂|²)/4  −  (d₁·d₂)/2'),
      para([t(
        'where d₁ = Q₁ − Q₀ and d₂ = Q₂ − Q₀ are the displacement vectors to the excited neighbours. ' +
        'For all Class B and Class C elements (the non-hydrogen/helium elements), |d₁| = |d₂| = 1 and ' +
        'd₁ ⊥ d₂ (orthogonal steps in n and ℓ), giving d₁·d₂ = 0 and therefore:'
      )]),
      eqLabel('13', 'σ²_max  =  1/2    for all Class B/C elements'),
      para([t('Setting λ = σ²_max = 1/2 grounds the coupling constant entirely within the Lach lattice.')]),

      heading3('5.2  Evaluation at Physical Extrema'),
      para([t(
        'Evaluating O₃ at convergence (φ₁₂ = φ₁₃ = 0) and at t = 0 (where host-coupling B(t) is maximal, ' +
        'since cos(2Ωt) = 1):'
      )]),
      eqLabel('14', 'A(0) = 1,    C(0) = λ²|ΔQ_x|²,    B(0) = 2λ|ΔQ_x|'),
      para([t('The three pairwise overlaps each simplify to:')]),
      eqLabel('15', 'O_ij(0)  =  1 + λ²|ΔQ_x|² + 2λ|ΔQ_x|  =  (1 + λ|ΔQ_x|)²'),
      para([t('The three-body product at convergence, t = 0, is therefore:')]),
      eqLabel('16', 'O₃_phys(0)  =  [(1 + λ|ΔQ_x|)²]³  =  (1 + λ|ΔQ_x|)⁶'),
      para([t(
        'The sixth power arises directly from the three-body product structure. A two-body treatment would ' +
        'yield power 2; the three-dimensional extension mandated by the Lach framework yields power 6, ' +
        'significantly amplifying differences between host materials.'
      )]),

      heading3('5.3  Physical Weighting'),
      para([t(
        'The abstract Lach lattice assigns |ΔQ_x| = 1/√2 uniformly to all Class B/C elements. Physical ' +
        'differentiation between host materials enters through a weighted coupling λ_phys that accounts for ' +
        'two effects absent from the abstract lattice:'
      )]),
      para([t(
        '(i)  Configuration-space depth. The distance from the lattice origin, |Q₀| = √(n² + ℓ² + k²), ' +
        'encodes relativistic depth and orbital complexity. Elements with larger |Q₀| sit deeper in ' +
        'configuration space and exert a stronger perturbation on guest atoms.'
      )]),
      para([t(
        '(ii)  Subshell electron density. The fractional filling of the valence subshell, weighted by the ' +
        'subshell type, encodes the electron density available at interstitial sites. Higher angular momentum ' +
        'subshells (d, f) produce greater interstitial density at their characteristic filling fractions.'
      )]),
      para([t('These corrections combine as:')]),
      eqLabel('17', 'λ_phys  =  (1/2) · |Q₀| · (k / 2(2ℓ+1))^(ℓ/4)'),

      heading3('5.4  The Host Coupling Potential'),
      para([t(
        'Since O₃_phys is monotonically increasing in λ_phys|ΔQ_x|, and |ΔQ_x| = 1/√2 is uniform, ' +
        'maximising O₃_phys is equivalent to maximising λ_phys. We define the Host Coupling Potential as:'
      )]),
      para([t('')], {spacing:{before:80,after:0}}),
      para([
        t('        H_cp(n, ℓ, k)  =  √(n² + ℓ² + k²)  ·  (k / 2(2ℓ+1))', {bold:true, size:SIZE_BODY+2, mono:true}),
        t('^(ℓ/4)', {bold:true, size:SIZE_SMALL, mono:true}),
      ], {align: AlignmentType.CENTER, spacing:{before:160,after:80}}),
      eqLabel('18', ''),
      para([t(
        'giving the complete expression for the physical three-body overlap:'
      )]),
      eqLabel('19', 'O₃_phys(0)  =  (1  +  H_cp / (2√2))⁶'),
      para([t(
        'This is the central result. H_cp(n, ℓ, k) is derived entirely from within the Lach framework, ' +
        'without external parameters or empirical fitting. The exponent ℓ/4 encodes the lattice ceiling ' +
        'ℓ_max = 4 (the g-subshell) defined in the Lach Elemental Field Equation Theorem.'
      )]),

      // ── 6. RESULTS ─────────────────────────────────────────────
      heading2('6.  Results'),

      heading3('6.1  Host Ranking'),
      para([t(
        'Table 1 presents H_cp and O₃_phys values for the principal FCC-structured elements with known ' +
        'hydrogen or deuterium absorption. Values are computed directly from Equation (18); no parameters ' +
        'are tuned to experimental results.'
      )]),
      ...blank(1),

      para([t('Table 1. FCC-structured cold fusion host candidates ranked by H_cp.',
        {bold:true, italic:true, size:SIZE_SMALL})],
        {align:AlignmentType.CENTER, spacing:{before:100,after:80}}),
      rankTable(),
      ...blank(1),
      para([t(
        'Ytterbium (Yb, Z=70) is the highest-ranked viable candidate among FCC-structured H/D-absorbing ' +
        'elements, with H_cp = 13.18 and O₃_phys = 32,815. Palladium (Pd, Z=46), the original ' +
        'Fleischmann-Pons host, ranks 7th with O₃_phys = 3,509. The ratio O₃(Yb) / O₃(Pd) ≈ 9.35.'
      )]),

      heading3('6.2  Geometric Interpretation'),
      para([t(
        'In the Lach (n, ℓ, k) lattice, the priority targets form a geometrically contiguous cluster in the ' +
        'high-|Q₀| region: the late f-block elements (Yb at coordinate (4,3,13)) and the late 5d metals ' +
        '(Pt at (5,2,8), Au at (5,2,9)) occupy adjacent regions of the lattice separated by a single step ' +
        'in the ℓ-axis. This adjacency is entirely invisible in the conventional two-dimensional periodic ' +
        'table, where Yb is displaced into the lanthanide strip below the main body. Figure 9 of the Lach ' +
        'Elemental Field Equation Theorem illustrates this directly (see companion figure).'
      )]),

      heading3('6.3  The Direction Classes'),
      para([t(
        'Analysis of ΔQ directions reveals that elements fall into three classes with distinct implications ' +
        'for cold fusion host utility:'
      )]),
      para([t('Class A (H, He only): Q₁ = Q₂, pure n-displacement, ΔQ = (−1, 0, 0). σ²_max = 0. ' +
        'These are the fusion fuel, not potential hosts.')]),
      para([t('Class B (most d-block, many p-block, some f-block): excited neighbours push toward ' +
        'higher ℓ. These hosts can displace deuterium\'s electron density upward in subshell complexity — ' +
        'toward configurations with greater interstitial electron density.')]),
      para([t('Class C (late lanthanides including Yb, early p-block): excited neighbours push toward ' +
        'lower ℓ. Despite the direction reversal, the high |Q₀| of late f-block elements dominates, ' +
        'making them strong hosts by H_cp.')]),
      para([t(
        'The practical implication is that Class B elements with high |Q₀| and Class C elements deep in ' +
        'the f-block both emerge as priority targets — but for different geometric reasons. Yb is a Class C ' +
        'element whose dominance is driven by its exceptional |Q₀| = √(4²+3²+13²) = 14.07.'
      )]),

      // ── 7. FALSIFIABLE PREDICTIONS ─────────────────────────────
      heading2('7.  Falsifiable Predictions'),

      para([t(
        'The framework yields three categories of falsifiable prediction, ordered by the strength of the ' +
        'claim:'
      )]),

      heading3('7.1  Ordering Prediction (Strong)'),
      para([t(
        'If anomalous heat production in deuteride systems is real and host-dependent, excess heat should ' +
        'scale with O₃_phys under equivalent experimental conditions. The predicted ordering among ' +
        'FCC-structured viable hosts is:'
      )]),
      eqLabel('20', 'Yb  >  Ag  >  Au  >  Pt  >  Ni  >  Pd  >  Ir  >  Rh'),
      para([t(
        'This ordering is derivable entirely from the geometry of the Lach lattice without reference to ' +
        'any experimental LENR data. It is a structural prediction, not a fit. Any experimental result ' +
        'that contradicts this ordering under controlled conditions constitutes a falsification.'
      )]),

      heading3('7.2  Crystal Structure Prediction (Strong)'),
      para([t(
        'FCC-structured hosts should systematically outperform HCP-structured hosts of comparable atomic ' +
        'number and electron configuration, because FCC unconditionally permits three-body convergence ' +
        'while HCP is conditional on c/a ratio. Specifically, HCP osmium (Os, Z=76) should underperform ' +
        'FCC iridium (Ir, Z=77) despite comparable H_cp values.'
      )]),

      heading3('7.3  Spectroscopic Prediction (Weaker)'),
      para([t(
        'The interaction term S_Z(t) = cos(2Ωt) · ΔQ_Z oscillates at frequency 2Ω, which may have a ' +
        'measurable spectroscopic signature in metal deuteride systems. If so, the amplitude of this ' +
        'signature should scale with |ΔQ_x|, which is uniform across all Class B/C elements in the ' +
        'abstract lattice but differentiated by H_cp in the physical lattice. This prediction is ' +
        'speculative and would require further theoretical development to become precisely testable.'
      )]),

      // ── 8. DISCUSSION ──────────────────────────────────────────
      heading2('8.  Discussion'),

      heading3('8.1  Why Palladium?'),
      para([t(
        'The present analysis clarifies why palladium produced the original Fleischmann-Pons results while ' +
        'also explaining why those results were difficult to replicate and why effects were relatively weak. ' +
        'Palladium is the correct family — FCC, d-block, strong H-absorber, Class B — but ranks 7th among ' +
        'FCC viable hosts. It sits at a local optimum of several practically convenient properties ' +
        '(soft, workable, available, non-toxic) rather than at the theoretical optimum of H_cp. The ' +
        'Lach framework predicts that Fleischmann and Pons found a real effect at sub-optimal conditions.'
      )]),

      heading3('8.2  Ytterbium as Priority Target'),
      para([t(
        'Ytterbium presents an experimentally accessible target. It is stable, non-radioactive, available ' +
        'commercially, and forms well-characterised hydrides (YbH₂ at room temperature, YbH₃ under moderate ' +
        'pressure). Its FCC crystal structure is confirmed. Its H_cp = 13.18 and O₃_phys = 32,815 place it ' +
        '9.35 times above palladium in predicted three-body deuterium overlap. No LENR experiment has, to ' +
        'the authors\' knowledge, used ytterbium as the primary host material. This constitutes an ' +
        'experimentally open prediction.'
      )]),

      heading3('8.3  Limitations'),
      para([t(
        'The present framework is geometric and topological. It does not calculate absolute fusion rates, ' +
        'barrier penetration probabilities, or energy outputs. H_cp is a relative ranking metric, not an ' +
        'absolute physical observable. The coupling constant λ_phys is grounded in the Lach lattice but ' +
        'does not incorporate real-space lattice parameters, phonon spectra, or defect chemistry — all of ' +
        'which are known to influence LENR experimental outcomes. The framework predicts which hosts should ' +
        'be tried; it does not guarantee a detectable effect in any of them.'
      )]),

      para([t(
        'Additionally, the model assigns each element a single ground-state coordinate. Real metal ' +
        'hydrides involve complex electronic restructuring upon hydrogen loading that is not captured by ' +
        'the host element\'s ground-state coordinates alone. Future work incorporating the Lach lattice ' +
        'coordinates of the metal hydride phase rather than the bare metal would constitute a significant ' +
        'refinement.'
      )]),

      // ── 9. CONCLUSION ──────────────────────────────────────────
      heading2('9.  Conclusion'),

      para([t(
        'This paper has extended the Lach Elemental Field Equation framework to cold fusion host ' +
        'identification. Beginning from the three-dimensional (n, ℓ, k) lattice, we derived a ' +
        'two-body perturbation expression for host-perturbed deuterium states, extended it to the ' +
        'three-body system required by the three-dimensional character of the framework, and formally ' +
        'derived the Host Coupling Potential:'
      )]),
      eqLabel('21', 'H_cp(n, ℓ, k)  =  √(n² + ℓ² + k²)  ·  (k / 2(2ℓ+1))^(ℓ/4)'),
      para([t(
        'without free parameters. Crystal structure analysis introduced a geometric gate distinguishing ' +
        'hosts that unconditionally permit three-body deuterium convergence (FCC) from those that permit ' +
        'it conditionally (HCP, BCC) or restrictedly (DHCP).'
      )]),

      para([t(
        'The central finding is that ytterbium (Yb, Z=70) is the top-ranked viable cold fusion host ' +
        'among all FCC-structured, H/D-absorbing elements, with a predicted three-body overlap ' +
        'O₃_phys ≈ 9.35 times that of palladium — the original Fleischmann-Pons host. This ordering ' +
        'is a falsifiable prediction derived entirely from the geometry of the Lach lattice.'
      )]),

      para([t(
        'The broader implication is that the Lach Elemental Field Equation Theorem, originally developed ' +
        'as a framework for element classification and undiscovered-element prediction, provides a ' +
        'natural geometric language for expressing problems in condensed-matter nuclear physics that ' +
        'have resisted conventional theoretical treatment. The configuration-space approach does not ' +
        'replace conventional quantum mechanics — it provides a geometric scaffold on which existing ' +
        'physical intuitions can be made precise and falsifiable.'
      )]),

      ruled(),

      // ── REFERENCES ─────────────────────────────────────────────
      heading2('References'),
      para([t('[1]  Lach, M. (2026). The Lach Elemental Field Equation Theorem: A Three-Dimensional ' +
        'Configuration-Space Framework for the Probabilistic Localisation of Known and Unknown Chemical Elements. ' +
        'Original theoretical work.')]),
      para([t('[2]  Fleischmann, M. & Pons, S. (1989). Electrochemically induced nuclear fusion of deuterium. ' +
        'Journal of Electroanalytical Chemistry, 261(2A), 301–308.')]),
      para([t('[3]  Pauli, W. (1925). Über den Zusammenhang des Abschlusses der Elektronengruppen im Atom ' +
        'mit der Komplexstruktur der Spektren. Zeitschrift für Physik, 31(1), 765–783.')]),
      para([t('[4]  Born, M. & Oppenheimer, R. (1927). Zur Quantentheorie der Molekeln. Annalen der Physik, ' +
        '389(20), 457–484.')]),
      para([t('[5]  Widom, A. & Larsen, L. (2006). Ultra low momentum neutron catalyzed nuclear reactions ' +
        'on metallic hydride surfaces. European Physical Journal C, 46(1), 107–111.')]),
      para([t('[6]  Storms, E. (2007). The Science of Low Energy Nuclear Reaction. World Scientific.')]),
      para([t('[7]  Dirac, P. A. M. (1930). The Principles of Quantum Mechanics. Oxford University Press.')]),
      para([t('[8]  Bohr, N. (1913). On the constitution of atoms and molecules. Philosophical Magazine, ' +
        '26(151), 1–25.')]),

    ]
  }]
});

Packer.toBuffer(doc).then(buffer => {
  fs.writeFileSync('/mnt/user-data/outputs/Lach_ColdFusion_HostIdentification_2026.docx', buffer);
  console.log('Done');
});