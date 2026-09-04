const {
  Document, Packer, Paragraph, TextRun, HeadingLevel, AlignmentType,
  PageNumber, Footer, PageBreak, Table, TableRow, TableCell, WidthType,
  BorderStyle, ShadingType, ImageRun, convertInchesToTwip
} = require('docx');
const fs = require('fs');

const F='Cambria', M='Consolas';
const S=21, SM=17, XS=15, H1=30, H2=25, H3=22;

function t(x,o={}){return new TextRun({text:x,font:o.mono?M:F,size:o.size||S,
  bold:!!o.bold,italics:!!o.italic,color:o.color});}
function p(runs,o={}){return new Paragraph({
  children:Array.isArray(runs)?runs:[runs],
  spacing:o.spacing||{before:120,after:60,line:276},
  alignment:o.align||AlignmentType.JUSTIFIED,
  indent:o.indent,heading:o.heading,pageBreakBefore:!!o.pb,border:o.border});}
const h1=(x,pb)=>p([t(x,{bold:true,size:H1})],
  {spacing:{before:360,after:160},heading:HeadingLevel.HEADING_1,align:AlignmentType.LEFT,pb});
const h2=(x)=>p([t(x,{bold:true,size:H2})],
  {spacing:{before:280,after:120},heading:HeadingLevel.HEADING_2,align:AlignmentType.LEFT});
const h3=(x)=>p([t(x,{bold:true,italic:true,size:H3})],
  {spacing:{before:200,after:100},heading:HeadingLevel.HEADING_3,align:AlignmentType.LEFT});
function eq(x,num){const kids=[t('     '),t(x,{mono:true,size:S})];
  if(num)kids.push(t('          ('+num+')',{size:SM}));
  return p(kids,{align:AlignmentType.LEFT,spacing:{before:140,after:140}});}
function img(file,w,h){return new Paragraph({
  children:[new ImageRun({data:fs.readFileSync(file),
    transformation:{width:w,height:h},type:'png'})],
  alignment:AlignmentType.CENTER,spacing:{before:200,after:80}});}
function cap(n,txt){return p([t(`Figure ${n}. `,{bold:true,size:SM}),t(txt,{size:SM})],
  {spacing:{before:0,after:220},align:AlignmentType.JUSTIFIED,
   indent:{left:convertInchesToTwip(0.35),right:convertInchesToTwip(0.35)}});}
function tcap(n,txt){return p([t(`Table ${n}. `,{bold:true,size:SM}),t(txt,{size:SM})],
  {spacing:{before:140,after:80},align:AlignmentType.LEFT});}
function rule(){return p([t('')],{spacing:{before:60,after:60},
  border:{bottom:{color:'999999',style:BorderStyle.SINGLE,size:6}}});}
function cell(x,w,o={}){return new TableCell({
  children:[p([t(x,{size:o.size||SM,bold:o.bold,color:o.color})],
    {align:o.align||AlignmentType.CENTER,spacing:{before:40,after:40}})],
  width:{size:w,type:WidthType.DXA},
  shading:o.fill?{type:ShadingType.CLEAR,fill:o.fill}:undefined});}
function table(headers,rows,widths,hi=[]){
  const hr=new TableRow({children:headers.map((x,i)=>cell(x,widths[i],{bold:true,fill:'DCD8D0'}))});
  const drs=rows.map(r=>new TableRow({children:r.map((x,i)=>
    cell(String(x),widths[i],{fill:hi.includes(r[0])?'EAF3EC':undefined}))}));
  return new Table({rows:[hr,...drs],
    width:{size:widths.reduce((a,b)=>a+b,0),type:WidthType.DXA},columnWidths:widths});}

const B=[];

// ═══════════════════ TITLE ═══════════════════
B.push(p([t('')],{spacing:{before:820,after:0}}));
B.push(p([t('The Lach Elemental Lattice',{bold:true,size:42})],
  {align:AlignmentType.CENTER,spacing:{after:90}}));
B.push(p([t('An Order-Theoretic Account of the Periodic System',{bold:true,size:27})],
  {align:AlignmentType.CENTER,spacing:{after:280}}));
B.push(rule());
B.push(p([t('in five parts, with a postscript',{italic:true,size:20,color:'555555'})],
  {align:AlignmentType.CENTER,spacing:{before:150,after:120}}));
[['I','Construction'],['II','The Lattice as an Ordered Set'],
 ['III','The Periodic System within the Lattice'],
 ['IV','The Lattice among Sorting Systems'],['V','Limits']].forEach(([r,n])=>{
  B.push(p([t(`${r}  ·  ${n}`,{size:21})],{align:AlignmentType.CENTER,spacing:{after:48}}));
});
B.push(p([t('Postscript  ·  An Exploratory Application to Deuteride Host Selection',
  {size:20,color:'444444'})],{align:AlignmentType.CENTER,spacing:{before:24,after:300}}));
B.push(p([t('Matthew Lach',{size:24})],{align:AlignmentType.CENTER,spacing:{after:40}}));
B.push(p([t('with computational assistance from Claude (Anthropic)',
  {italic:true,size:19,color:'555555'})],{align:AlignmentType.CENTER,spacing:{after:200}}));
B.push(p([t('2026',{size:21,color:'666666'})],{align:AlignmentType.CENTER,spacing:{after:360}}));

// ═══════════════════ ABSTRACT ═══════════════════
B.push(p([t('Abstract',{bold:true,size:23})],
  {align:AlignmentType.LEFT,spacing:{before:200,after:100}}));
B.push(p([t('This paper assigns every chemical element a coordinate (n, ℓ, k) given by the quantum numbers of its ground-state valence configuration — principal shell, subshell type, and occupancy — and studies the resulting integer lattice Λ as a mathematical object. The construction is a change of coordinates and introduces no new physics; what it produces is a partial order on configurations, and the paper is an account of that order.')]));
B.push(p([t('Part I builds the lattice. Of the 630 cells in the enclosing 7 × 5 × 18 box, 210 are admissible, of which 118 are occupied by known elements; the remainder divide into 180 void cells where the subshell cannot exist and 240 reactive cells where the electron count exceeds Pauli capacity. The displacement vector ΔQ from a cell to the midpoint of its excited neighbours sorts the elements into three geometric classes.')]));
B.push(p([t('Part II establishes the order structure. Exhibiting a standard example S₃ among the admissible cells shows that the order dimension of Λ is exactly three: no two linear orders can encode its containment relation, so the third coordinate is necessary rather than convenient. Λ is a bounded distributive lattice whose unique minimum is hydrogen at (1, 0, 1), a consequence of the constraints rather than a chosen anchor, and closure follows from a standard sublattice argument that also shows why the hydrogenic labelling (n, ℓ, m, s) fails. Counting cells at fixed n returns the Pauli capacities 2n² for n ≤ 5. The lattice is Sperner without being rank-symmetric, and its rank generating function decomposes into shifted q-integers and vanishes at q = −1, an exact parity balance forced by spin degeneracy. The Madelung rule appears as a linear functional whose level sets pair to give the observed period lengths, and projection along it reproduces the Janet left-step table exactly; fibration along the n-axis instead reproduces the conventional chemical groups, placing helium with the alkaline earths by a second and independent route. The orientation of the lattice is rigid: exactly one of the 120 orderings of the subshell types admits the elements and preserves the structure.')]));
B.push(p([t('Part III locates the periodic system inside the lattice. The 118 occupied cells form an order ideal, closed downward without exception, which follows from aufbau filling being a monotone accumulation and which survives every extension to excited states that could be constructed. The ideal is all-or-nothing by column: of the twenty-five (n, ℓ) columns, nineteen are filled to capacity and six are empty, none partially, so the realised system is one of only 120 down-sets of the column poset. Its three maximal cells leave five covering addresses for any further element — a constraint on valence configuration alone, not on nuclear stability.')]));
B.push(p([t('Part IV compares the lattice with the three established ways of ordering the elements: quantum sorting by the Madelung rule, structural sorting by the Pettifor and Villars scales, and integral sorting by atomic number. The central result is an order-theoretic one. Atomic number and Madelung order are both linear extensions of Λ, reversing none of its 3,742 comparable pairs, whereas Pettifor\'s Mendeleev number reverses 960 of 1,684 and is not order-compatible in either orientation. Λ is therefore a coarsening of atomic number that never contradicts it, and is orthogonal to structural sorting. The obstruction to a linear relationship between Λ and the Pettifor scale is proved rather than observed: the slope ∂MN/∂k is positive in the p- and d-blocks and negative in the f-block, and a linear function cannot have a sign-changing partial derivative.')]));
B.push(p([t('Part V sets the limits, and does so in detail because they define the object as sharply as the positive results do. Every axis of Λ is a count, so Λ ⊆ ℕ³ and every quantity built from the coordinates is dimensionless; no metric coordinate can be adjoined, since an informative one would be a function of the others and a functional graph is not a sublattice. Five predictive applications were attempted and all five failed or were outperformed, and each failure is reported with its diagnosis. The lattice organises; it does not predict.')]));
B.push(p([t('A postscript records an exploratory application to deuteride host selection. It is placed outside the numbered parts because nothing in the account of the lattice depends on it.')]));

B.push(new Paragraph({children:[new PageBreak()]}));

// ═══════════════════ PART I ═══════════════════
B.push(h1('PART I — CONSTRUCTION'));

B.push(h2('1.  Introduction'));
B.push(p([t('The periodic table, in the two-dimensional form that Mendeleev gave it and the twentieth century refined, remains the most productive organising device in chemistry. Its rows track the principal quantum number and its columns track valence behaviour, and it encodes real periodicity. But the layout imposes compromises that are cartographic rather than physical. The f-block is removed from the body of the table and printed beneath it, for reasons of page width alone. Subshell type and occupancy are conflated into a single positional axis, so two elements in one group may share electron count while occupying different subshells. And the table has no vocabulary for absence: a gap either holds an undiscovered element or is nothing at all, with no way of saying which vacancies are physically possible and which are forbidden.')]));
B.push(p([t('This paper treats the three quantum numbers as three independent axes and asks what becomes visible. The construction is deliberately minimal. No new physics is introduced; the Pauli principle and the angular-momentum condition are taken as given, and everything that follows is a consequence of writing them as coordinate constraints. What the change of coordinates produces is not another arrangement of the elements but a different kind of object: a partial order, where every previous scheme produces a sequence.')]));
B.push(p([t('That difference organises the paper. Part I builds the lattice and classifies its empty space. Part II studies Λ as an abstract ordered set — its dimension, its closure, its invariants, its correspondences with the Madelung rule and the Janet table, and the rigidity of its orientation. Part III asks where the 118 known elements sit within it. Part IV compares the lattice with the quantum, structural and integral sorting systems already in the literature, and establishes the relation that most sharply distinguishes it from them. Part V sets out what the lattice cannot do, at length, because a boundary drawn precisely is itself a result. A postscript records one exploratory application; the lattice does not depend on it.')]));

B.push(h2('2.  The Coordinate System'));
B.push(p([t('Each element is assigned the coordinate (n, ℓ, k) of its ground-state valence configuration, where n is the principal quantum number, ℓ ∈ {0, 1, 2, 3, 4} denotes the subshell types s, p, d, f, g, and k counts the electrons occupying that subshell. The admissible lattice is')]));
B.push(eq('Λ  =  { (n, ℓ, k) ∈ ℤ³  :  1 ≤ n ≤ 7,   0 ≤ ℓ ≤ min(n−1, 4),   1 ≤ k ≤ 2(2ℓ+1) }','1'));
B.push(p([t('The two upper bounds are the angular-momentum condition ℓ ≤ n−1 and the Pauli capacity of a subshell, 2(2ℓ+1). The ceilings n ≤ 7 and ℓ ≤ 4 are modelling choices reflecting the elements presently known, and their consequences are noted wherever they bind. Hydrogen occupies (1, 0, 1). Section 8 shows that this is the unique minimum of the order rather than a chosen origin.')]));
B.push(p([t('Two features of the construction deserve emphasis, because both bear on results later in the paper. First, the axes are quantum numbers, not lengths: n indexes a shell, ℓ indexes angular momentum, and k is a count. Distances in Λ are combinatorial rather than metric, and Part V shows that this is not a removable feature. Second, the axes are coupled — the range of ℓ depends on n and the range of k depends on ℓ. Section 9 shows that the particular form of this coupling is what makes the lattice work.')]));
B.push(p([t('A note on convention. Where a measured ground-state configuration departs from strict aufbau filling, an assignment must be chosen. The data used here follow the conventional block assignment: lanthanum and actinium are placed in the d-block at (5, 2, 1) and (6, 2, 1) as their measured configurations require, while the d-block anomalies such as chromium and copper are assigned their idealised occupancies. Both conventions were tested. They differ for thirty elements individually but produce the same set of 118 occupied cells, and every structural result in Parts II and III is identical under either. The convention therefore affects the labelling of cells but not the geometry.')]));

B.push(h2('3.  The Classification of Empty Space'));
B.push(p([t('Every cell of the enclosing box not occupied by a known element falls into exactly one of three regimes, and drawing this distinction is the first substantive product of the coordinate change.')]));
B.push(p([t('Void cells satisfy ℓ ≥ n. The subshell does not exist for that shell, and no element can occupy the cell under any conditions whatever. Reactive cells satisfy ℓ < n but k > 2(2ℓ+1): the electron count exceeds Pauli capacity, so the configuration cannot be a ground state; under the reading proposed here they correspond to transient overflow states in which an excess electron is promoted to a new shell. Reserved cells satisfy both constraints and yet hold no known element. These are valid, physically permitted configurations that are simply unoccupied.')]));
B.push(p([t('A census of the 7 × 5 × 18 box is given in Figure 1. Of 630 cells, 180 are void, 240 reactive, 92 reserved and 118 occupied. The figure of 92 reserved cells corrects the value of 78 quoted in an earlier draft of this work; the recount is exact and is reproduced by the classification code accompanying the paper.')]));
B.push(img('F01_census.png',600,250));
B.push(cap(1,'Census of the configuration-space box. (a) The 630 cells partition into four regimes, with void and reactive cells together accounting for two-thirds of the volume. (b) Distribution of the 92 reserved cells across (n, ℓ). Reserved cells concentrate at n = 6–7 in the d, f and g layers — the region corresponding to elements beyond Z = 118.'));
B.push(p([t('The concentration visible in Figure 1(b) is the substantive point. Reserved cells are not scattered uniformly through the empty volume: forty-two of the ninety-two lie at n = 7 and a further thirty-two at n = 6, overwhelmingly in the higher-ℓ layers. In the two-dimensional table this region is simply the blank space past oganesson. Here it is a set of addressed coordinates, each with a defined neighbourhood.')]));

B.push(h2('4.  The Elements in Place'));
B.push(p([t('Figure 2 shows all 118 elements at their ground-state coordinates. No manual grouping is applied: the block structure emerges from the ℓ-axis alone, and within each block the elements stratify along n by period. The f-block, which the conventional table detaches entirely, sits in the body of the structure at ℓ = 3.')]));
B.push(img('F02_elements.png',620,282));
B.push(cap(2,'The 118 known elements at their ground-state coordinates (n, ℓ, k). Colour denotes block; the gold ring marks hydrogen at (1, 0, 1). (a) Oblique view. (b) Near-edge view showing the separation of blocks along the ℓ-axis. The clustering is a consequence of the coordinates, not of any imposed arrangement.'));

B.push(h2('5.  Neighbourhoods, Displacement, and the Field Equation'));
B.push(p([t('Each element is modelled as a three-state system: its ground configuration Q₀ = (n, ℓ, k) together with its two nearest excited neighbours,')]));
B.push(eq('Q₁ = (n+1, ℓ, k)          [shell excitation]','2'));
B.push(eq('Q₂ = (n, ℓ±1, k)          [subshell excitation]','3'));
B.push(p([t('with Q₂ taking ℓ+1 where the angular-momentum condition permits and ℓ−1 otherwise. The displacement from the midpoint of the excited pair back to the ground state,')]));
B.push(eq('ΔQ  =  Q₀ − ½(Q₁ + Q₂)','4'));
B.push(p([t('is a static vector characterising the geometry of each element\'s neighbourhood. Writing the state as a superposition over the accessible cells and requiring normalisation at all t, ground-state occupancy at t = 0, and sinusoidal evolution at base frequency Ω gives coefficients c₀ = cos(Ωt) and c₁ = c₂ = sin(Ωt)/√2. Phase-shifting by π/2 yields the emission expression, and combining the two gives a unified form, designated here the Lach elemental field equation,')]));
B.push(eq('Ψ±(t)  =  √2 · sin(Ωt + π/4) · Σ(n,ℓ,k)∈Λ  |n, ℓ, k⟩','5'));
B.push(p([t('with expectation position ⟨Q⟩(t) tracing a bounded path through configuration space and variance')]));
B.push(eq('σ²(t)  =  ⟨Q²⟩(t) − ⟨Q⟩(t)²','6'));
B.push(p([t('measuring the instantaneous spread.')]));
B.push(p([t('Three cautions are required, and they are stated here rather than deferred because they determine how the rest of the paper should be read. Equation (5) is a construction on the lattice, not a solution of a Hamiltonian derived from physical potentials. Ω is a formal parameter, and nothing in this paper establishes a correspondence between Ω and a measurable frequency in any material. And the expression is element-independent: the summation carries no element label and the prefactor is common to all, so every element shares a single envelope. The identities on which it rests were verified symbolically and hold exactly — the normalisation cos²(Ωt) + 2·[sin(Ωt)/√2]² = 1 is identically satisfied, as is cos(Ωt) + sin(Ωt) = √2 sin(Ωt + π/4) — but a correct identity is not a physical law. What distinguishes one element from another is not Equation (5) but the displacement vector ΔQ and the spread σ²(t), which are geometric quantities read off the lattice. The results of this paper depend on the geometry and not on any dynamical reading of the field equation.')]));

B.push(h2('6.  Three Geometric Classes'));
B.push(p([t('Evaluating ΔQ across all 118 elements yields a sharply degenerate result. The magnitude |ΔQ| takes exactly two values: unity for hydrogen and helium, and 1/√2 for every other element. The elements are differentiated not by the size of the displacement but by its direction, which falls into three cases.')]));
B.push(p([t('Class A comprises hydrogen and helium alone. Here n = 1 admits only ℓ = 0, so both excited neighbours collapse onto the same cell, Q₁ = Q₂; the neighbourhood is one-dimensional and the spread at maximum excitation vanishes. Class B comprises elements for which ℓ+1 ≤ n−1, so subshell excitation moves toward higher angular momentum. Class C comprises elements for which only ℓ−1 is available, so subshell excitation moves toward lower angular momentum.')]));
B.push(img('F08_classes.png',600,229));
B.push(cap(3,'Direction classes of the displacement vector ΔQ. (a) Schematic of the three cases. (b) Class membership across atomic number. The 3d series and the lanthanides fall in Class C; the 4d and 5d series fall in Class B. The classification follows entirely from the angular-momentum constraint ℓ ≤ n−1 and requires no additional input.'));
B.push(p([t('The classification is not arbitrary bookkeeping. It states which direction in configuration space each element\'s accessible excitations lie, it separates the 3d and 4f series from the 4d and 5d series on purely geometric grounds, and Section 24 reports that it separates hydride formation enthalpies at p = 0.010 — the only instance in this paper of a purely geometric construction tracking a measured quantity.')]));
