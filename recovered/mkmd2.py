#!/usr/bin/env python3
"""Full expanded edition. Reads data.json (earlier parts) and data3.json (this session)."""
import json
D = json.load(open('/home/claude/paper/data.json'))
E = json.load(open('/home/claude/paper/data3.json'))
f = lambda n: f'{n:,}'
FIG = 'figures/'

V2=D['v2']; T=D['tower']; O=D['order']; Q=D['quiver']; R=D['routes']
H=D['hasse']; MOL=D['molecular']; CN=D['containment']; PT=V2['ptable']

N15=E['fifteen']; F15=E['frontier15']; RP=E['repairs15']; LM=E['lattice_map']
SY=E['system']; AX=E['axis_index']; A22=E['audit22']; PM=E['ptable_mono']

def row(cells): return '| ' + ' | '.join(str(c) for c in cells) + ' |'
def hdr(cells): return row(cells) + '\n|' + '|'.join('---' for _ in cells) + '|'

md = f"""# TRANSITIONS

### What an index can carry, and one cell that no index can

**Matthew Lach** — Independent researcher
Draft v2.0. Prepared with a computing collaborator under the protocols of The Method v1.4.
Supersedes v1.x, *The closure defect of an index*.

---

## Abstract

For a finite set of integer tuples X we compute **E(X) = |R(X)| − |X|**, where R closes X under its monotone
pairwise envelopes. We prove R is a closure operator, that E ≥ 0, and that E = 0 is global consistency of a binary
constraint network. E then measures whether an index can carry a constraint, and we identify **two failure modes
and no third**.

**Sub-case A, ordering.** The term is present and determined but non-monotone. The eighteen-column periodic table
carries ℓ as a function of group — 0, 0, 2, …, 2, 1, …, 1 — which no envelope can read, giving E = {PM['E_18col']}.
Dropping group and keeping ℓ gives **E = {PM['E_period_l']} immediately**. Repairable by re-ordering; this is what
Janet's table does, and it is the block order f, d, p, s rather than the choice of period that does the work.

**Sub-case B, arity.** Every term is monotone but the constraint names more coordinates than an envelope has
arguments. An index of which physical laws must break to reach another universe has **all
{72 if True else 0} of its pairwise relations monotone** and a defect nonetheless, from a constraint of arity 3
with a unique minimal support. Six coordinate operations fail to repair it, including exhaustive relabelling.

We then **double the alphabet**. Five of nine coordinates are shown to conflate distinct physical notions — each
against a named theorem's stated hypothesis — and splitting them, plus adding the derivative-order axis that is
Buniy's operative hypothesis, gives fifteen letters. **Every structural result survives**: arity 3, core one cell,
six repairs failing, the two-line envelope argument, the frontier formulas exact. The multiplicity moves from 30 to
{N15['E']} and carries no information.

Finally the defect is located outside the index altogether. The chargers — the theorems that levy a price — draw
their hypotheses from **seven vocabularies**, so each is a map between indices rather than a constraint within one.
The resulting system graph has {len(SY['nodes'])} nodes and {SY['edges_all']} edges, is not a tree, and **severs
into {SY['components_live']} components once the vacuous charger is removed**. The theorem that would exclude
macroscopic wormholes lives in the component the law index cannot reach.

> **What this paper does not claim.** Nothing here bears on whether other universes exist, or whether transit
> between them is achievable. Every result is about an *index* — what a coordinate system can and cannot carry.
> The precedent is the periodic table, whose defect of {PM['E_18col']} is a fact about a drawing.

![The result]({FIG}f6_1.png)

*Figure 0.1. One object is decidable by local consistency; the two that cross between universes are not, and for
different reasons.*

---

## Contents

- [Part 0 · Procedure](#part-0--procedure)
- [Part I · The operator, and two failure modes](#part-i--the-operator-and-two-failure-modes)
- [Part II · Λ verified](#part-ii--λ-verified)
- [Part III · The periodic table: ordering failure, repaired](#part-iii--the-periodic-table-ordering-failure-repaired)
- [Part IV · Transit structures on Λ](#part-iv--transit-structures-on-λ)
- [Part V · The violation index at nine letters](#part-v--the-violation-index-at-nine-letters)
- [Part VI · The alphabet](#part-vi--the-alphabet)
- [Part VII · The violation index at fifteen letters](#part-vii--the-violation-index-at-fifteen-letters)
- [Part VIII · Chargers, jurisdiction, and the system of indices](#part-viii--chargers-jurisdiction-and-the-system-of-indices)
- [Part IX · The axis index, and what was never named](#part-ix--the-axis-index-and-what-was-never-named)
- [Part X · Results](#part-x--results)
- [Part XI · Register](#part-xi--register)
- [Part XII · Open](#part-xii--open)
- [Appendix A · Equations](#appendix-a--equations)
- [Appendix B · References](#appendix-b--references)
- [Appendix C · Verification](#appendix-c--verification)

---

## Part 0 · Procedure

### 0.1 Protocols

{hdr(['protocol',''])}
{row(['commit before looking','a position is written down before any retrieval; the retrieval scores it'])}
{row(['compute before writing','numerical claims are computed, then reported, never the reverse'])}
{row(['refuse rather than coerce','an ambiguous instruction is queried, not defaulted'])}
{row(['enumerate before searching','targets are listed before the first search and re-listed when the set grows'])}
{row(['record what a failure excludes','a falsified prediction is logged with the class of claim it rules out'])}

### 0.2 The Admission Law

> An open index admits any content, and admits it only together with its verification grade. An entry's grade
> bounds the operations it may enter. **A derived entry carries the minimum grade of its inputs, and no derivation
> raises a grade.** Content contradicting the index is admitted and flagged as a collision; a collision is
> discharged by re-deriving the internal result, never by refusing the content.

Every substantive repair in this work arrived as a collision. The bibliography carries an access grade per source
for the same reason.

### 0.3 The merge rule

> A biconditional licenses a merge only if it holds at **every rung** of the graded axis. Merging on a fact true at
> one point and then grading the axis is the error.

Part VI shows that this rule, correctly applied, would have caught five of the nine coordinates before they were
built.

### 0.4 Operator reliability, measured

Predictions aimed at logical structure — which hypotheses a theorem takes, which way an entailment runs — scored
4/4 on three consecutive tests. Predictions aimed at how a field regards a claim scored 1/4. Predictions of
implications not yet in the index scored about 1 in 5. Under 0.2 the last class was therefore barred from entering
content.

---

## Part I · The operator, and two failure modes

### 1.1 Definitions

For finite X ⊆ ∏Aᵢ of integer tuples, write **Âᵢ(X) = {{xᵢ : x ∈ X}}** for the value sets and
**φ̂ᵢⱼ(v) = max{{xᵢ : x ∈ X, xⱼ ≤ v}}** for the monotone upper envelope of coordinate i against j. Then R(X)
collects every point of the observed box respecting all envelopes, and E(X) is its excess — equations (1)–(4).
No outside knowledge enters R(X): it is what a reader could reconstruct from the cells alone.

### 1.2 Proposition. X ⊆ R(X), hence E ≥ 0

> *Proof.* Let x ∈ X. Each xᵢ ∈ Âᵢ(X). For i ≠ j the set {{yᵢ : y ∈ X, yⱼ ≤ xⱼ}} contains xᵢ, since x satisfies
> xⱼ ≤ xⱼ. Hence φ̂ᵢⱼ(xⱼ) ≥ xᵢ, so x ∈ R(X). ∎

### 1.3 Proposition. R is a closure operator

Extensive by 1.2. Monotone and idempotent by computation: R(R(X)) = R(X) on Λ₈ and on both violation indices;
monotonicity held on thirty nested random pairs with no failure. The closed sets form a Moore family.

### 1.4 Identification

R is the closure of a binary constraint network under monotone binary projections, and **E(X) = 0 iff the network
is globally consistent**.

### 1.5 R against the full minimal network

X ⊆ BPC(X) ⊆ R(X) — equation (5) — so E > 0 is in principle ambiguous between genuine inconsistency and envelope
coarseness. Computed for every object here, **the ambiguity does not arise**: R = BPC exactly.

![Nested sets]({FIG}f1_1.png)

### 1.6 THE TWO FAILURE MODES

This is the paper's thesis and everything after it is instances.

> An index can carry a constraint only if it holds the constraint's terms **in an order the envelope can read**,
> and in **as many places as the constraint names**. Failure of either produces E.
>
> **Sub-case A — ordering.** The term is present and determined but non-monotone. Repairable by re-ordering.
>
> **Sub-case B — arity.** Every term is monotone; the constraint names more coordinates than an envelope has
> arguments. Not repairable by any operation on coordinates.

Four objects, and the diagnosis separates them cleanly:

{hdr(['object','non-monotone relations','arity','E','verdict'])}
{chr(10).join(row([m['object'], m['nonmono'], m['arity'], f(m['E']), m['verdict']]) for m in E['failure_modes'])}

**No third mode was found.** The axis index of Part IX looked like one — it fails at arity 2 with all 21 pairs
failing — and resolved to sub-case A, with {AX['nonmono']} of 42 relations non-monotone. What distinguishes it from
the periodic table is only that its ordering failure is **unrepairable**, since nine axes have no natural
re-placement.

### 1.7 Six blindnesses

{hdr(['blind to','instance','effect on E'])}
{row(['decreasing bounds','a preferred frame forbids chronology violation','0 → 6'])}
{row(['non-monotone relations','seniority parity on axis 10','0 → 678'])}
{row(['multi-coordinate constraints','the conjugation ceiling; the coupling triangle','186 / 35,570'])}
{row(['unoccupied dimensions','a fifth axis nothing occupies','unchanged'])}
{row(['the measure','two universes, same cells, different energies','unchanged'])}
{row(['derived coordinates','an axis defined as a function of others','30 → 120'])}

**A derived coordinate cannot repair closure.** R reconstructs from cells alone, so a reader cannot see that a
coordinate was *defined* from others, while the box grows by that coordinate's value count and |X| stays fixed.
This excludes the entire class of derived-coordinate repairs, for any index.

![Blindness panels]({FIG}f1_2.png)

### 1.8 The closure rule

> **A tightening preserves E = 0 if and only if it binds one coordinate by a monotone function of one other.**

![Closure rule]({FIG}f1_3.png)

### 1.9 E requires density, asymmetrically

A late finding, and it qualifies every number in the paper.

{hdr(['object','cells','box','density','E informative?'])}
{chr(10).join(row([d['object'], f(d['cells']), f(d['box']), str(d['pct'])+'%',
   'yes' if d['E_informative'] else 'measures sparsity']) for d in E['density_ladder'])}

> **E = 0 is informative at any density. E > 0 at low density measures sparsity rather than structure.**

Λ₁₃ sits at {[d for d in E['density_ladder'] if d['object']=='Lambda_13'][0]['pct']}% and E = 0 there is a *strong*
result — 47.8 million possible tuples, {f(199130)} cells, and the envelope admits exactly those. The axis index at
{AX['density']}% is the case where E > 0 says nothing.

### 1.10 Named theorems

{hdr(['result','statement'])}
{row(['Freuder 1982','a tree-structured constraint network is globally consistent after arc consistency'])}
{row(['Montanari 1974','for monotone constraints, path consistency implies global consistency'])}
{row(['van Beek & Dechter 1995','generalisation of monotone to row-convex constraints'])}
{row(['van Beek & Dechter 1997','constraint tightness — the exact/admissible ratio'])}

These two cover Λ between them. Neither applies to either violation index, nor to the system of Part VIII.

---

## Part II · Λ verified

Λ is an atomic-structure lattice: 8-tuples (n, ℓ, k, q, e, f, g, 2S) built by nested bounds — equations (6)–(12) —
with the tower Λ₉–Λ₁₃ adding target spin, seniority, the core's J, K and the outer J, equations (13)–(17). Caps
(n, e, ℓ, k, f) = (3, 3, 1, 3, 1) are unique in the search range for 976 cells.

### 2.1 The tower closes at every level, for every statistics order

Generalising Pauli exclusion to parastatistics of order m gives capacity m(4ℓ+2), equation (25). At m = 1 the
construction reproduces the canonical tower exactly, which verifies the generalisation at the fermionic point.

{hdr(['m','Λ₈','Λ₉','Λ₁₀','Λ₁₁','Λ₁₂','Λ₁₃'])}
{chr(10).join(row([m]+[f(s) for s in E['tower_para'][m]['sizes']]) for m in ('1','2','3'))}

**E = 0 at every cell of that table.** Boxes swept to {f(E['tower_para']['3']['boxes'][-1])} at m = 3, Λ₁₃, by a
backtracking counter with early pruning — the feasible region is a staircase, so most branches die at depth three
or four.

Previously this was established to Λ₁₁ only. **The parastatistics neighbours are globally consistent to the top of
the tower**, and the closure never depended on the fermionic value: capacity m(4ℓ+2) is monotone in ℓ for every m,
so §1.8's form is preserved and Montanari's certificate applies unchanged.

![The tower]({FIG}f2_1.png)

### 2.2 Why it closes

Λ₉'s constraint graph has nine nodes and eight edges and is a tree, so Freuder applies. Λ₉′ — the same lattice with
the admissible Pauli cut 2S′ ≤ 2f+1, removing 93 cells and leaving {f(T['L9prime'])} — gains the cycle f–g–2S′ and
loses the guarantee. Λ₁₀ has ten nodes and ten edges. **Λ₉ is the last tree level.**

![Constraint graphs]({FIG}f2_2.png)

### 2.3 Where the exactness goes

All six density values reproduce once three non-obvious exact sets are used: the spin set of f^g by microstate
enumeration at axis 9; terms genuinely *new* at occupancy v, conjoined with the parity congruence and the
conjugation ceiling, at axis 10; and the J values of terms of ℓᵏ carrying the cell's own multiplicity 2S at axis 11.
Without the third, axis 11 computes to 43.1% instead of {D['density']['11']}%.

![Densities]({FIG}f2_3.png)

### 2.4 Closure and exactness are incompatible

Imposing the exact coupling triangle on axis 12 cuts the lattice from {f(D['axis12']['loose_cells'])} to
{f(D['axis12']['tight_cells'])} cells and takes E from zero to {f(D['axis12']['tight_E'])} — the exact bound is
ternary, outside the closure-preserving class.

> **Λ is loose by design.** Every coupling coordinate's exact bound needs two parents or a congruence, and a tree
> carries one. **The tree or the tightness.** Part VIII finds the same trade one level up.

![Closure vs exactness]({FIG}f2_4.png)

---

## Part III · The periodic table: ordering failure, repaired

The control, and the only object here whose answer is independently known.

### 3.1 The mechanism is ordering, not placement

The eighteen-column table has E = {PM['E_18col']}. It is standard to say Janet's left-step table removes this by
re-indexing period as n + ℓ. **That is not what does the work**, and neither is contiguity as such.

**ℓ is fully determined by group** — s at 1–2, d at 3–12, p at 13–18. The term is present, recoverable,
unambiguous. And the defect is {PM['E_18col']} anyway, because

```
ℓ by group 1..18 :  {', '.join(str(v) for v in PM['l_by_group'])}
```

rises then falls. **Non-monotone in both directions**, so no envelope can use it. In Janet's block order f, d, p, s,
ℓ decreases monotonically along every row.

{hdr(['presentation','cells','E'])}
{row(['(period, group) — ℓ present, non-monotone in group','90',PM['E_18col']])}
{row(['(period, position) contiguous','90',PM['E_contig']])}
{row(['Janet (n+ℓ, position) — ℓ monotone','120',PM['E_janet']])}
{row(['**(period, ℓ)** — group dropped','90',f"**{PM['E_period_l']}**"])}
{row(['(period, group, ℓ) — ℓ named explicitly','90',PM['E_with_l']])}

**Drop group, keep ℓ, and the table closes immediately.** And naming ℓ explicitly makes it *worse*, E =
{PM['E_with_l']}. **Naming the term does not help. Ordering it does.**

### 3.2 What the 36 are

They decompose: **{PT['law']}** of them — 1p, 1d, 2d — could never hold an element, being forbidden by ℓ ≤ n−1.
They are the footprint of a law the coordinate system has no axis for. The remaining **{PT['convention']}** are 3d,
which exists and is merely deferred past 4s by the Madelung order.

**Two constraints casting a thirty-six-cell shadow, not thirty-six facts.**

![Periodic table]({FIG}f2_5.png)

### 3.3 Why the control matters

The periodic table is not an analogy for the violation index. **It is the other failure mode**, and having both is
what makes the distinction visible. Ordering failures are repairable because re-ordering acts on one relation at a
time — exactly enough for sub-case A and exactly not enough for sub-case B.

---

## Part IV · Transit structures on Λ

### 4.1 Λ₉ is the transit level

A cell's target is a legal source exactly when 2S′ ≤ g — which *is* axis 9, equation (19). Of {f(T['cells'][1])}
cells, {f(Q['arcs'])} are composable. Λ₉ is simultaneously the first level at which a transition has a defined
endpoint and the last level that is a tree.

![The window]({FIG}f3_1.png)

### 4.2 The composition graph is a line digraph

Composable cells are the arcs of a quiver Q on {Q['states']} atomic states; the composition graph is L(Q) and its
edge count is **{f(Q['line_edges'])} = Σ(in × out)** exactly, equation (20). The {Q['loops']} degenerate cells are
Q's loops, and because Q has a loop at every vertex, **return is available in one step from every state.**

![Quiver]({FIG}f3_2.png)

### 4.3 Girth exactly 4

Unit-step adjacency coincides with the covering relation exactly — {f(H['edges'])} edges either way, so the lattice
is gap-free. Degrees run {H['deg_min']} to {H['deg_max']}, mean {H['deg_mean']}, connected.

> **Proposition.** The girth is exactly 4. *Proof.* Three mutually adjacent cells are impossible: if a–b differ in
> coordinate i and b–c in j ≠ i then a–c differ in two; if i = j then a–c differ by 0 or 2. No triangle exists. A
> square c, c+eᵢ, c+eᵢ+eⱼ, c+eⱼ is exhibited. ∎

![Girth]({FIG}f3_3.png)

### 4.4 Molecular transit, and sub-case B at higher arity

A molecule moves as one fibre, so all its atoms take the same displacement and a circuit is a square. Feasibility is
an intersection question — equations (21)–(22).

{hdr(['atoms']+[str(r['m']) for r in MOL])}
{row(['feasibility']+[f"{r['rate']:.3g}%" for r in MOL])}

Decay is geometric at roughly 1.9 per atom. Homonuclear molecules are unconstrained.

> **The Helly number is at least {V2['helly']['lower']} and at most {V2['helly']['upper']}.** A critical family of
> five is exhibited: every four intersect and the five do not. The upper bound is the ground set — all C(9,2) × 4 =
> {V2['helly']['possible']} square directions occur.

This is **sub-case B at arity 5**, showing the mode scales beyond the ternary case.

![Molecular feasibility]({FIG}f3_4.png)
![Helly]({FIG}f3_5.png)

---

## Part V · The violation index at nine letters

Presented as originally built, because Part VI shows five of its nine letters are conflated, and the correction is
only legible against what it corrects.

### 5.1 Coordinates

> **Notation.** E is the closure defect throughout. The null-energy coordinate is written NEC to avoid the
> collision.

{hdr(['axis','rungs'])}
{row(['**X** causal ladder','Lorentz invariant / preferred threading / preferred foliation / chronology violated'])}
{row(['**S_corr** correlation','local ≤2 / quantum ≤2√2 / post-quantum ≤4'])}
{row(['**IC** information causality','holds / violated at m>0 / violated at m=0'])}
{row(['**U** unitarity','unitary / local energy-momentum-conserving non-unitarity / requiring locality to break'])}
{row(['**NEC** null energy','intact / pointwise / ANEC arbitrarily small / macroscopic QI-bounded / QI-violating'])}
{row(['**L** linearity','linear / nonlinear'])}
{row(['**SD** microcausality','holds / fails'])}
{row(['**DN_c** cloning','quantum-optimal / beyond / perfect deterministic'])}
{row(['**DN_d** discrimination','quantum-optimal / beyond / perfect'])}

Our position is **{tuple(E['nine']['origin'])}**, with two components fixed by measurement: S_corr = 1 because
quantum mechanics violates Bell locality while respecting microcausality, and NEC = 1 because Casimir energy is
measured and violates the null energy condition pointwise.

![Nine axes]({FIG}f4_1.png)

### 5.2 Routes, and the cost of a formalism

{hdr(['CTC model','destination floor','steps'])}
{row(['Deutsch (D-CTC)',tuple(R['D-CTC']['dest']),R['D-CTC']['steps']])}
{row(['post-selected (P-CTC)',tuple(R['P-CTC']['dest']),R['P-CTC']['steps']])}
{row(['model-independent',tuple(R['model-independent']['dest']),R['model-independent']['steps']])}

Model-independently, chronology violation requires the causal ladder, non-unitarity at the Lindblad rung, and
arbitrarily small ANEC violation — and **not** signalling, cloning, nonlinearity or loss of microcausality, each of
which appears under Deutsch's prescription and not otherwise.

![Three routes]({FIG}f4_2.png)

### 5.3 The defect and its collapse

{f(E['nine']['cells'])} cells; **E = {E['nine']['E']}**, all of it genuine global-consistency failure. The excess is
exactly **1 × {V2['multiplicity']}**, and the core is one cell: **(X = 0, U = 0, NEC = 3)**.

The envelope calculation says why in two lines:

```
φ(NEC | X = 0)  must permit the value, because X = 0 cells with U ≥ 1 reach it
φ(NEC | U = 0)  must permit the value, because U = 0 cells with X ≥ 1 reach it
```

**Both conditioning coordinates individually admit what the pair forbids.**

![The collapse]({FIG}f4_3.png)

### 5.4 Unique minimal support

Of {V2['support']['subsets_checked']} coordinate subsets excluding {{X, U, NEC}}, **{V2['support']['failing']}**
fail. The triple is the only minimal failing subset. **Arity exactly 3, one generator.**

### 5.5 The repair space is closed

{hdr(['operation','outcome','E','why'])}
{row(['merge by identification','not licensed','—','no pair among {X, U, NEC} is biconditional at every rung'])}
{row(['merge by linearisation','worse',V2['repairs'][1]['E'],'collapsing two axes forces every constraint through one envelope'])}
{row(['relabel axis values','never zero',f"min {V2['relabel']['min_E']}",f"exhaustive: {V2['relabel']['zeros']} of {f(V2['relabel']['tested'])}"])}
{row(['slide within rows','never better',V2['repairs'][3]['E'],'the hole is a row that should not exist'])}
{row(['add a derived coordinate','worse',V2['repairs'][4]['E'],'the box inflates and |X| does not'])}
{row(['split an axis','neutral or worse',V2['repairs'][5]['E'],'pins the antecedent as well as the consequent'])}

> **Adding fails because the box inflates; merging fails because the envelopes coarsen.** Both directions excluded,
> for opposite reasons, and the two-line argument covers all six.

![Six repairs]({FIG}f4_5.png)

### 5.6 Objects are thresholds

{hdr(['object','threshold','cells','here?','reachable'])}
{chr(10).join(row([o['name'],'`'+o['threshold']+'`',f(o['cells']),'**yes**' if o['here'] else 'no',f(o['reachable'])]) for o in V2['objects'])}

Of the {f(V2['wormhole_cost']['total'])} cells permitting a macroscopic wormhole, {f(V2['wormhole_cost']['frame'])}
pay with a preferred frame, {f(V2['wormhole_cost']['nonunitary'])} with non-unitarity,
{f(V2['wormhole_cost']['signalling'])} with signalling — and **{V2['wormhole_cost']['free']} pay with none.**

![Thresholds]({FIG}f4_6.png)

### 5.7 The defect does not scale

{hdr(['coordinates']+[str(p['coords']) for p in V2['projection']])}
{row(['defect']+[str(p['E']) for p in V2['projection']])}
{row(['core']+[str(p['core']) for p in V2['projection']])}
{row(['multiplicity']+[str(p['mult']) for p in V2['projection']])}

The core is one cell at every resolution. Only the free-coordinate count moves, which is arithmetic.

![Projection]({FIG}f4_7.png)

---

## Part VI · The alphabet

The central methodological result, and it was invisible from inside the index.

### 6.1 Five of nine coordinates conflate distinct notions

{hdr(['letter','status','merges','shown by'])}
{chr(10).join(row([c[0],c[2],c[3],c[4] if len(c)>4 and c[4] else '—']) for c in E['conflations'])}

**{E['conflation_counts']['full']} fully conflated, {E['conflation_counts']['partial']} partially,
{E['conflation_counts']['clean']} clean.**

### 6.2 Every conflation merges an inert rung with a potent one

In each case the rung as graded has **no lattice action**, and its partner either acts or abolishes the lattice
outright. That is not coincidence: **the index was graded from papers about what breaks, and the papers that matter
for atomic structure are about what holds.** Two different literatures.

### 6.3 None was findable from inside

**All five surfaced from a specific question about a named theorem** — which spin-statistics hypothesis does U
encode? does nonlinearity destroy vector coupling? observables or fields? which exclusion theorem applies to a long
wormhole? is the ghost condensate inside Buniy's jurisdiction? Inspecting the coordinate list finds none of them.

> **An index's conflations are invisible from inside it. They are visible only from the theorems it is meant to
> carry.**

This is why twenty-one structural audits passed on a document containing all five. Those audits compare the index
against itself — coherence, scoping, arithmetic, attribution — and **no self-audit can catch a word that means
something else elsewhere.**

### 6.4 Audit 22 — term match, and the vocabulary debt

**For every coordinate whose term appears in a cited theorem: state what the theorem means by it, state what the
rung means, record match / conflation / unchecked.** Its output is a debt, not a pass.

```
coordinates                {A22['coordinates']}
theorems naming one        {A22['theorems']}
term-sharing pairs         {A22['pairs']}
checked                    {A22['checked']}   ({round(100*A22['checked']/A22['pairs'])}%)
   conflations             {A22['conflations']}
   partial                 {A22['partial']}
   matches                 {A22['matches']}
UNCHECKED                  {A22['unchecked']}
```

Unchecked by coordinate: {', '.join(f"{k} {v}" for k,v in A22['by_coord'].items())} — of which **IC has never been
checked once**, and IC is load-bearing: it is the unique principle forbidding post-quantum correlations.

The 56% conflation rate among those checked should **not** be extrapolated. The sixteen were selected because
something forced them, so they are enriched for trouble. The rate among the remaining {A22['unchecked']} is lower,
unknown, and not zero.

### 6.5 The corrected alphabet

{hdr(['letter','meaning','rungs','provenance'])}
{chr(10).join(row([f"**{a['letter']}**",a['meaning'],a['rungs'],a['provenance']]) for a in E['alphabet'])}

**What becomes expressible.** The ghost condensate — X_exp = 0, X_spon = 1, EOM = higher — a Lorentz-invariant
*theory* with a Lorentz-violating *vacuum*, which in the nine-letter alphabet could not be written. The MMP
wormhole — NEC_pt = 2, NEC_ach = 0 — violating the ANEC while satisfying the achronal ANEC. Buniy's jurisdiction in
full. And **SD_field = 1 marks a cell that is not a universe at all**, by Burgoyne: the fields vanish identically.

That last removes **{f(N15['removed_no_theory'])} of {f(N15['closed_before_charge'])}** closed cells as describing
no theory.

---

## Part VII · The violation index at fifteen letters

### 7.1 Every structural result survives

```
closed cells                    {f(N15['closed_before_charge'])}
minus SD_field = 1 (no theory)  {f(N15['cells']+816)} → after charge {f(N15['cells'])}
ambient box                     {f(N15['box'])}
density                         {N15['density']}%      (informative range)
E                               {f(N15['E'])}
core                            {N15['core']}    ONE cell
collapse exact                  {N15['collapse_exact']}   ({f(N15['E'])} = 1 × {f(N15['patterns'])})
arity                           {N15['arity']}
```

**The core is (X_exp = 0, U_ghost = 0, NEC_pt = 3, EOM = 2nd-order)** — macroscopic exotic matter, no explicit
Lorentz violation, no ghosts, second-order equations of motion. The same profile as at nine letters, in four precise
conditions rather than three approximate ones.

**Two minimal supports, not one**: {' and '.join('{'+', '.join(m)+'}' for m in N15['minimal_supports'])}. The split
created a second path, since U_ghost = 1 → X_spon = 1 makes X_spon a proxy for ghosts. Both share {{X_exp, NEC_pt}}.

**EOM does not appear in either**, though it is Buniy's jurisdiction — Ostrogradsky gives EOM = higher → U_ghost, so
the closure carries the jurisdiction into the currency letter. **A jurisdiction condition forced by an existing
letter costs nothing.**

### 7.2 The repair space is still closed

{hdr(['operation','E at fifteen','note'])}
{row(['merge by identification','n/a','no pair among the support is biconditional at every rung'])}
{row(['merge by linearisation','7,734','coarsens every envelope on either axis'])}
{row(['relabel — exhaustive',f"min {RP['relabel_min']}",f"{RP['relabel_zeros']} of {f(RP['relabel_tested'])} close"])}
{row(['slide within rows','8,856','the hole is a row that should not exist'])}
{row(['add a derived coordinate','2,196','the box inflates, |X| does not'])}
{row(['split an axis further',f(N15['E']),'no change'])}

And the envelope argument transfers verbatim:

```
φ(NEC_pt | X_exp = 0)   = {RP['phi_NEC_given_Xexp0']}    X_exp = 0 cells with ghosts reach it
φ(NEC_pt | U_ghost = 0) = {RP['phi_NEC_given_Ughost0']}    ghost-free cells with X_exp ≥ 1 reach it
```

### 7.3 The frontier formulas, exact

**d(c) = X_exp + U_ghost + |NEC_pt − 3| + EOM + d_P(eleven free letters)**
**s(c) = 1{{X_exp>0}} + 1{{U_ghost>0}} + 1{{NEC_pt≠3}} + 1{{EOM>0}} + s_P**

Verified on {f(F15['sampled'])} sampled cells: **{F15['d_mismatch']} distance mismatches,
{F15['s_mismatch']} support mismatches.**

**Our own values are unchanged: d = {F15['our_d']}, s = {F15['our_s']}.** Two rungs of one letter from the core,
and the letter is still NEC_pt.

But the pinned set changed: **SD dropped out and EOM came in.** The SD that mattered was never the observable one.
And the corner is less exclusive — {F15['single_letter_pct']}% of cells see the frontier along a single letter
against 8.9% at nine letters, mean support {F15['mean_s']} against 3.35. **Support and distance are
alphabet-dependent. The core is not.**

### 7.4 The lattice map, now exact

The spin-statistics hypotheses have three letters and no proxies: **X_exp = 0, SD_obs = 0, U_ghost = 0.**

{hdr(['hypothesis','letter','indexable?'])}
{chr(10).join(row([h[0],'`'+h[1]+'`',h[2]]) for h in LM['hypotheses'])}

**{f(LM['guaranteed'])} of {f(LM['of'])} cells — {LM['pct']}% — have the Pauli lattice guaranteed, and we are among
them.** For the rest, parastatistics becomes available and Λ₈ can be 1,600 rather than 976: a different periodic
table, and different everything built from atoms.

> **The lattice distinguishes exactly one thing: whether spin-statistics holds.** Two universes share a lattice iff
> they agree on that, and may differ arbitrarily in energy conditions, signalling, cloning and discrimination
> without any atom noticing.

**U_open and L_dyn are provably inert**; their split partners U_ghost and L_kin are what act. That was the entire
content of two conflations, now visible in the alphabet rather than buried in a rung.

---

## Part VIII · Chargers, jurisdiction, and the system of indices

### 8.1 A charge relation has three parts, not two

**Trigger** — what incurs the charge. **Currency** — what may pay. **Jurisdiction** — where the charger has standing
to collect.

{hdr(['charger','trigger','currency','jurisdiction'])}
{row(['Buniy–Hsu–Murray','NEC violation','instability → ghosts','causal, Lorentz-invariant, second-order EOM'])}
{row(['Hartman–Kundu–Tajdini','ANEC violation','¬unitary, ¬Lorentz, ¬microcausal','**exactly flat spacetime**'])}
{row(['Wall (GSL)','achronal ANEC','via the generalised second law','curved, minimally coupled, GSL axioms'])}
{row(['Graham–Olum','achronal ANEC','causality violation','**asymptotically flat, simply connected**'])}
{row(['Ostrogradsky','higher-derivative EOM','ghosts','**non-degenerate** (Galileons escape)'])}

### 8.2 A jurisdicted forcing and an unjurisdicted disjunction are the same object

{hdr(['constraint','arity','cells','E','core'])}
{row(['NEC ≥ 3 → U ≥ 1','2','1,938','**0**','—'])}
{row(['NEC ≥ 3 ∧ X = 0 → U ≥ 1','3','2,370','**30**','1'])}
{row(['NEC ≥ 3 ∧ U = 0 → X ≥ 1','3','2,370','**30**','1'])}
{row(['NEC ≥ 3 → (IC ∨ U ∨ X)','4','2,370','**30**','1'])}

> **"Something must pay and we can't say what" and "unitarity must pay, but only in Lorentz-invariant theories" are
> the same constraint.** The unnamed currency and the scoped jurisdiction are one phenomenon.

That resolves what looked like missing information. **Buniy names the price precisely — ghosts. What it also names
is a jurisdiction, and the jurisdiction costs the extra coordinate.** A theorem holding only under a scope condition
is inherently ternary, and no further physics removes the scope.

**And the size behaves counterintuitively.** Arity ≥ 3 is what makes a defect *possible*; jurisdiction *narrowness*
is what makes it small. The defect is **largest at exactly one scope condition** — 30, 30, 20, 20, 10 as conditions
are added. The theorems hardest to index are the **nearly universal** ones with a single hypothesis, and Buniy is
exactly that.

### 8.3 Buniy's jurisdiction is necessary, and its operative hypothesis is not the one I indexed

The counterexample exists: **Creminelli, Luty, Nicolis and Senatore, *Stable Violation of the Null Energy Condition*
(2006)**, built on the ghost condensate. And it escapes **not** through Lorentz violation — its Lagrangian
ℒ = √−g M⁴P(X) is manifestly Lorentz-invariant, the *vacuum* breaks the symmetry — but through **higher-derivative
terms**, which supply the leading spatial kinetic term for the perturbations.

Corroborated from the other side: standard two-derivative theories generically develop ghosts or gradient
instabilities on NEC-violating backgrounds, with Galileons escaping because their higher-derivative terms are
combined so the equations of motion stay second order in each field.

**So the load-bearing hypothesis is derivative order, and the index used Lorentz invariance as a proxy.** The proxy
gave the right answer because the core cell satisfies both — a coincidence that concealed the error. It also means
**Route 1 stays open**: Buniy may extend to Lorentz-violating second-order theories, and nothing known bears on that.

### 8.4 The vocabularies

The nineteen-odd hypotheses across the chargers do not belong to one vocabulary. Sorting them:

{hdr(['vocabulary','terms'])}
{row(['V1 laws','the fifteen letters'])}
{row(['V2 theory','causal, field content, interacting, d > 2'])}
{row(['V3 geometry','flat, asymptotically flat, simply connected, globally hyperbolic, generic'])}
{row(['V4 algebra','determinism, ultralocality, stability, vacuum lowest energy, vacuum not annihilated'])}
{row(['V5 coupling','minimal coupling'])}
{row(['V6 solution','self-consistent semiclassical'])}
{row(['V7 degeneracy','non-degenerate higher-derivative'])}

**No vocabulary can fully state any charger. Zero of {len(SY['spans'])}, minimum span two.**

Doubling the alphabet raised indexable hypotheses from {E['hyp_coverage']['indexable_old']} of
{E['hyp_coverage']['total_old']} to {E['hyp_coverage']['indexable_new']} of {E['hyp_coverage']['total_new']} —
{E['hyp_coverage']['pct_old']}% to {E['hyp_coverage']['pct_new']}% — and **moved nothing across the threshold.**

> **Enlarging the alphabet imported a charger, and the charger imported a vocabulary the alphabet doesn't have.**
> V7 arrived because EOM did. **Letters recruit chargers faster than they discharge them.**

### 8.5 The system graph

Chargers are maps between indices. The system:

```
nodes       {len(SY['nodes'])}
edges       {SY['edges_all']}
components  {SY['components_all']}
cycles      {SY['cycles_all']}    NOT a tree
```

Degrees: {', '.join(f"{k} {v}" for k,v in SY['degrees'].items())}. **V1 is the hub and a cut vertex; V3 is the
other.** The two cycles come from the two three-index chargers, Hartman spanning laws–theory–geometry and Wall
spanning laws–algebra–coupling.

**Freuder does not apply**, for exactly the reason it fails at Λ₉′: an added edge makes a cycle. **Montanari does
not rescue it**, because cross-index constraints are conjunctions of conditions in different vocabularies, not
monotone bounds.

### 8.6 The system is severed

Hartman is **vacuous in this index**: its trigger is ANEC violation and its jurisdiction is flat spacetime, and ANEC
violation requires curvature. The two are mutually exclusive, so the charge never fires.

**Hartman is the only V1–V3 edge.** Removing it:

```
edges       {SY['edges_live']}
components  {SY['components_live']}
   reachable from the law index : {', '.join(SY['components_live_detail'][0])}
   UNREACHABLE                  : {', '.join(SY['unreachable'])}
```

**Graham–Olum is the edge inside the unreachable component.** The theorem that excludes macroscopic wormholes and
time machines lives on V3–V6, and the law index is not an endpoint of that edge.

> **The exclusion of macroscopic wormholes lives in a component the law index cannot reach.**

That is a property of the **system graph**, not of the index — which is why six operations failed, why
{f(RP['relabel_tested'])} relabellings closed nothing, and why doubling the alphabet left the core at one cell.
**None of those touch the graph.**

Every earlier diagnosis was a shadow of this one:

{hdr(['earlier statement','what it was seeing'])}
{row(['envelope blindness','V1 has no term for the constraint'])}
{row(['unnamed currency','the charger holding the currency is unreachable'])}
{row(['jurisdiction creates arity','the jurisdiction lives in V2 and V3'])}
{row(['vocabulary mismatch','the statement spans indices'])}
{row(['**the component is severed**','**the graph is disconnected**'])}

### 8.7 Connectivity against acyclicity

{hdr(['configuration','edges','components','cycles','verdict'])}
{row(['Hartman dead, Wall live (actual)','6','2','1','**disconnected**'])}
{row(['Hartman live (3 indices), Wall live','8','1','2','connected, 2 cycles'])}
{row(['Hartman reduced to V1–V3, Wall live','7','1','1','connected, 1 cycle'])}
{row(['Hartman live, Wall reduced','6','2','1','disconnected'])}
{row(['both reduced to two-index','5','2','0','disconnected — V5 isolated'])}

**No configuration is a connected tree.** The best available is Hartman reduced to V1–V3. And reducing Wall
backfires: its V1–V5 edge is coupling's *only* connection.

**Hartman must drop V2, not V3** — dropping *flat* leaves V1–V2 and never reaches geometry; dropping *interacting*
and *d > 2* leaves V1–V3 and connects without triangulating. So the requirement is precise: **Hartman must hold for
interacting theories in any dimension on curved backgrounds.**

**This is the same trade as §2.4, one level up.** Λ₉: the tree or the tightness. The system: connected or acyclic.
Both resolve the same way — *a statement that needs fewer places.*

### 8.8 That extension does not exist

Checked twice, including through an adjacent literature.

The general ANEC-from-causality argument is **flat-space**; earlier derivations were restricted to free or
superrenormalisable theories, or to two dimensions. Curved-space results exist only with a V2 condition retained:
CFTs in conformally flat spacetimes, maximally symmetric backgrounds, free minimally coupled fields at small
curvature, or via the GSL with minimal coupling.

**The QNEC lineage goes further and still not far enough.** The modular crossed-product construction defines entropy
differences in general curved spacetime and proves the Bekenstein bound there — but its **QNEC proof is on Rindler
horizon cuts in Minkowski**, and the paper's own future-work list names the generalised second law, which is Wall's
route to the achronal ANEC, as *not yet done.*

**So the system stays severed and the core cell stands.**

---

## Part IX · The axis index, and what was never named

### 9.1 Three measures, and the third did not exist

**E** measures what an index cannot carry. **The vocabulary debt** measures what it has not checked it carries
correctly — {A22['unchecked']} of {A22['pairs']}. **Nothing measured what it never named at all.**

Seven law-classes appear in sources this paper already cites and have no letter: CPT, energy-momentum conservation,
the generalised second law, weak cosmic censorship, the holographic bound, global symmetry conservation, the
equivalence principle. Two are sharp:

**CPT.** Greenberg gives CPT violation ⟹ Lorentz violation — **an edge into X_exp.** Its absence is a missing
forcing, not merely a missing axis.

**Energy-momentum conservation.** Banks–Susskind–Peskin's disjunction is *¬locality ∨ ¬energy-momentum
conservation.* **The index encodes the first disjunct and silently drops the second** — precisely the mis-typing
corrected in Part XI, sitting uncorrected at the root of the U axis.

### 9.2 Indexing the axes

```
cells (axes)     {AX['cells']}
box              {f(AX['box'])}
E                {AX['E']}
density          {AX['density']}%
non-monotone     {AX['nonmono']} of 42
verdict          OPEN
```

**The axis set is open**, at nine axes and at fifteen. But at {AX['density']}% density its excess predicts nothing —
the envelope admits nearly the whole box. **This is exactly the case §1.9 excludes.**

And adding the six known-missing axes made density *worse*, 0.17% → 0.11%: **an index of few cells over many
coordinates cannot be densified by adding cells one at a time**, because the box grows multiplicatively in
value-set size while the cell count grows additively.

### 9.3 Pair-completion — an instrument that does work

The nine leave **four** value-directions unoccupied: {', '.join(f"{k} missing {v}" for k,v in AX['unoccupied'].items())}.

Four directions give six pairs, and **every hand-found axis outside the box occupies a pair — never one direction,
never three.**

{hdr(['pair','status'])}
{chr(10).join(row([' + '.join(p['pair']), ('OCCUPIED: '+', '.join(p['occupied_by'])) if p['occupied_by'] else '**empty — predicts an axis**']) for p in AX['pairs'])}

**Four empty pairs, four predictions:**

{hdr(['pair','the axis it predicts','candidate'])}
{chr(10).join(row([' + '.join(p['pair']),p['description'],p['candidate'] or '— describable, not nameable']) for p in AX['predictions'])}

**Weak cosmic censorship** is the strongest: named by Penrose, Landsman, Senovilla and Ishibashi–Maeda–Mefford,
carrying no experimental bound, and terminal in the edge set. **It has been used as a hypothesis throughout this
work and never given an axis.**

> **Pair-completion found a missing coordinate rather than recording one I noticed.** It works not through E, which
> is uninformative at this density, but through the completion of occupied directions.

**One confirmation from six hand-chosen cases is suggestive, not established.** The four directions come from seven
properties I chose, and the six axes were chosen by me. The method is a search heuristic.

---

## Part X · Results

**1. E measures whether an index can carry a constraint, and there are two failure modes.** Ordering — the term is
present but non-monotone, repairable. Arity — every term is monotone and the constraint needs more places,
not repairable. Four objects, one of each and two of the second at different arities. No third mode found.

**2. A universe is a globally consistent constraint network.** Λ closes at every level of the tower, for
parastatistics orders 1, 2 and 3, to Λ₁₃ — boxes swept to {f(E['tower_para']['3']['boxes'][-1])}. The certificates
are Freuder and Montanari.

**3. A transition between universes is not expressible as one.** Defect {E['nine']['E']} at nine letters and
{f(N15['E'])} at fifteen, both collapsing to **one core cell**, with arity 3 throughout.

**4. The core survived doubling the alphabet.** Five conflations split, one axis added, half the cells removed as
non-theories, two generators instead of one, twenty-seven times the multiplicity — and the core stayed one cell for
reasons expressible in two lines. **The structural results are about the operator, not the encoding.**

**5. The unnamed currency was a conflation.** At nine letters Buniy looked like a disjunction with an unspecified
price. At fifteen it is a forcing with a single currency — ghosts — and the appearance of a disjunction was the
alphabet merging ghosts with Lindblad evolution.

**6. Jurisdiction creates arity.** A jurisdicted forcing and an unjurisdicted disjunction give identical defects.
The defect is largest at exactly one scope condition, so nearly-universal theorems are the hardest to index.

**7. The defect is a property of the system graph.** Seven indices, eight edges, two cycles, and severed into two
components once the vacuous charger is removed. **The wormhole exclusion lives on an edge the law index is not an
endpoint of** — which is why nothing done to the alphabet could touch it.

**8. An index's conflations are invisible from inside it.** Twenty-one audits passed on a document containing five.
Audit 22 is external by construction and its output is a debt: {A22['unchecked']} of {A22['pairs']} pairs unchecked.

**9. Openness is the signature, not a failure.** A closed index is a universe. Neither violation index closes, and
neither does the axis index that contains them.

---

## Part XI · Register

### 11.1 The promotion ledger

{hdr(['claim','status','basis'])}
{chr(10).join(row([p[0],'**'+p[1]+'**',p[2]]) for p in E['promotions'])}

**Everything promoted is about the method. Everything held is either a general claim or a physical number.** That
split was not planned and is the correct diagnosis: the instrument is better characterised than anything it measured.

### 11.2 Withdrawals

{hdr(['claim','cause'])}
{chr(10).join(row([w[0],w[1]]) for w in E['withdrawals'])}

### 11.3 The recurring class

**{E['error_class']['instances']} instances of one class: {E['error_class']['description']}.** The arithmetic was
correct in every case; the warrant was not. Subtypes:

{chr(10).join('- '+s for s in E['error_class']['subtypes'])}

**Two were caught by data already on screen**, and one is a straight repeat of a logged correction rather than a new
variant. The register is reported in full because the pattern of failure is itself a finding, and because it is the
evidence that the checking apparatus works.

### 11.4 The seven propositions

{hdr(['','proposition','verdict','basis'])}
{chr(10).join(row([p[0],'`'+p[1]+'`','**'+p[2]+'**',p[3]]) for p in E['propositions'])}

**Four refuted, two unassertable, one conditional. None closes the index**, and with Buniy's jurisdiction
established as necessary, P5's conditionality no longer decides the matter.

---

## Part XII · Open

{hdr(['item','state'])}
{row(['the self-consistent achronal ANEC in 4d','no proof, no counterexample, 19 years. Null QEIs have **no finite lower bounds** in four dimensions (Fewster–Roman), which is why the Kontou–Olum route cannot be extended by that path'])}
{row(['Hartman for interacting theories on curved backgrounds','the single change that connects the system; does not exist, checked in both the ANEC and QNEC literatures'])}
{row(['whether Buniy extends to Lorentz-violating second-order theories','reopened once the operative hypothesis was identified as derivative order'])}
{row(['the '+str(A22['unchecked'])+' unchecked term pairs','IC has six and has never been checked once'])}
{row(['Λ’s own conflations','the symmetric question, never asked: thirteen coordinates against Condon–Shortley and Racah'])}
{row(['the four predicted axes','cosmic censorship strongest; three have plausible occupants, none verified'])}
{row(['a completeness criterion for the coordinate set','none exists. Pair-completion is a heuristic with one confirmation'])}
{row(['whether the two failure modes hold for indices not built here','needs someone else’s index'])}
{row(['the two halves','any joining map is cross-vocabulary; the bare product multiplies the defect by 976 and adds nothing'])}

### 12.1 The join, and why it stays open

For a product with no linking constraint every cross-envelope is vacuous, so **R(A × B) = R(A) × R(B)** and

**E(A × B) = |A|·E_B + |B|·E_A + E_A·E_B**

For Λ and the violation index, with E(Λ) = 0: **E = 976 × 30 = {f(29280)}.** The defect is **extensive** — multiply
an index by anything and it scales with the other factor. **The core is the invariant across products; E is not.**

So the halves are not unjoined for want of a map. **There is nothing to gain and a factor of 976 to lose**, and any
linking constraint is cross-vocabulary, so neither index could carry it.

---

## Appendix A · Equations

### A.1 The operator

**(1)** Âᵢ(X) = {{ xᵢ : x ∈ X }}
**(2)** φ̂ᵢⱼ(v) = max{{ xᵢ : x ∈ X, xⱼ ≤ v }} — a staircase, non-decreasing in v
**(3)** R(X) = {{ x ∈ ∏ᵢ Âᵢ(X) : xᵢ ≤ φ̂ᵢⱼ(xⱼ) ∀ i ≠ j }}
**(4)** E(X) = |R(X)| − |X| ≥ 0
**(5)** X ⊆ BPC(X) ⊆ R(X), BPC(X) = {{ x : (xᵢ, xⱼ) ∈ projᵢⱼ(X) ∀ i < j }}

### A.2 The lattice Λ

**(6)** 1 ≤ n ≤ n_max  **(7)** 0 ≤ ℓ ≤ n − 1  **(8)** 1 ≤ k ≤ 4ℓ + 2  **(9)** 0 ≤ q ≤ k
**(10)** 0 ≤ f ≤ e − 1  **(11)** 0 ≤ g ≤ min(4f + 2, q)  **(12)** 0 ≤ 2S ≤ k

### A.3 The tower

**(13)** 0 ≤ 2S′ ≤ g  **(14)** 2S′ ≤ v ≤ g  **(15)** 0 ≤ 2J_c ≤ φ̂(k)
**(16)** |2J_c − 2f| ≤ 2K ≤ 2J_c + 2f (step 2) — the *exact* triangle; the lattice admits the loose form
**(17)** |2J − 2K| ≤ 1

### A.4 Exactness

**(18)** density(axis) = Σ_parents |exact fibre| ÷ Σ_parents |admissible fibre|

### A.5 Transit

**(19)** src(c) = (n, ℓ, k, 2S), tgt(c) = (e, f, g, 2S′); c composes iff tgt(c) is a legal source
**(20)** |E(L(Q))| = Σ_v deg⁻(v) × deg⁺(v)
**(21)** Sq(c) = {{ (i, sᵢ, j, sⱼ) : c + sᵢeᵢ, c + sⱼeⱼ, c + sᵢeᵢ + sⱼeⱼ ∈ Λ₉ }}
**(22)** a molecule {{c₁, …, c_m}} may circuit ⟺ ∩ₜ Sq(cₜ) ≠ ∅

### A.6 The violation index

**(23)** I_V = ∮(ρ + p_r) dV — the volume-integral quantifier grading the null-energy axis
**(24)** NEC_pt ≥ 3 ∧ X_exp = 0 ∧ EOM = 2nd → U_ghost = 1 — Buniy as a jurisdicted forcing, arity 4, reduced to
arity 3 by Ostrogradsky
**(25)** capacity(ℓ) = m(4ℓ + 2) — parastatistics of order m
**(26)** 2 ≤ S_CHSH ≤ 2√2 ≤ 4
**(27)** ⟨T_kk⟩ ≥ (ℏ/2π) S″_out — the quantum null energy condition; a bound, not a forcing edge
**(28)** {f(N15['E'])} = 1 × {f(N15['patterns'])} — core times multiplicity, exact

### A.7 The frontier

**(29)** d(c) = X_exp + U_ghost + |NEC_pt − 3| + EOM + d_P(free letters)
**(30)** s(c) = 1{{X_exp>0}} + 1{{U_ghost>0}} + 1{{NEC_pt≠3}} + 1{{EOM>0}} + s_P

### A.8 Products

**(31)** R(A × B) = R(A) × R(B) when no constraint links the factors
**(32)** E(A × B) = |A|·E_B + |B|·E_A + E_A·E_B

### A.9 Order and measure

**(33)** x ≤ y ⟺ xᵢ ≤ yᵢ ∀ i — {O['comparable_pct']:.1f}% of Λ₈ pairs are comparable
**(34)** a measure μ is *faithful* iff x < y ⟹ μ(x) ≠ μ(y) — the Coulomb measure is unfaithful on
{O['samen_pct']:.1f}% of ordered pairs

---

## Appendix B · References

**Access grades.** **[F]** full text read. **[A]** abstract or published summary. **[S]** secondary. **[B]** blocked.

### B.1 Constraint satisfaction, consistency and closure

- Freuder, E. C. (1982). A sufficient condition for backtrack-free search. *JACM* 29(1), 24–32. **[S]**
- Montanari, U. (1974). Networks of constraints. *Information Sciences* 7, 95–132. **[S]**
- Mackworth, A. K. (1977). Consistency in networks of relations. *Artificial Intelligence* 8(1), 99–118. **[S]**
- Dechter, R. (1992). From local to global consistency. *Artificial Intelligence* 55(1), 87–107. **[S]**
- van Beek, P. & Dechter, R. (1995). On the minimality and global consistency of row-convex constraint networks. *JACM* 42(3), 543–561. **[S]**
- van Beek, P. & Dechter, R. (1997). Constraint tightness and looseness versus local and global consistency. *JACM* 44(4), 549–566. **[S]**
- Jeavons, P., Cohen, D. & Cooper, M. C. (1998). Constraints, consistency and closure. *Artificial Intelligence* 101(1–2), 251–265. **[S]**
- Cooper, M. C., Jeavons, P. G. & Salamon, A. Z. (2010). Generalizing constraint satisfaction on trees. *Artificial Intelligence* 174, 570–584. **[A]**
- Helly, E. (1923). Über Mengen konvexer Körper mit gemeinschaftlichen Punkten. *Jahresbericht der DMV* 32, 175–176. **[S]**

### B.2 Atomic structure and statistics

- Racah, G. (1943). Theory of complex spectra III. *Physical Review* 63, 367–382. **[S]**
- Condon, E. U. & Shortley, G. H. (1935). *The Theory of Atomic Spectra*. Cambridge. **[S]**
- Janet, C. (1929). The left-step periodic table. **[S]**
- Greenberg, O. W. (1993). (Para)bosons, (para)fermions, quons and other beasts in the menagerie of particle statistics. hep-ph/9306225. **[F]**
- Greenberg, O. W. (1997). Spin-statistics, spin-locality, and TCP: three distinct theorems. hep-th/9707220. **[F]**
- Lüders, G. & Zumino, B. (1958). Connection between spin and statistics. *Physical Review* 110, 1450. **[S]**
- Bernabéu, J. et al. (VIP collaboration) (2006). An experiment to search for a violation of the Pauli exclusion principle. quant-ph/0608088. **[F]**

### B.3 Energy conditions and wormholes

- Buniy, R. V., Hsu, S. D. H. & Murray, B. M. (2006). The null energy condition and instability. *PRD* 74, 063518. **[F]**
- Creminelli, P., Luty, M. A., Nicolis, A. & Senatore, L. (2006). Starting the universe: stable violation of the null energy condition and non-standard cosmologies. *JHEP* 12, 080. **[F]**
- Arkani-Hamed, N., Cheng, H.-C., Luty, M. A. & Mukohyama, S. (2004). Ghost condensation and a consistent infrared modification of gravity. *JHEP* 05, 074. **[S]**
- Cheng, H.-C., Luty, M. A., Mukohyama, S. & Thaler, J. (2006). Spontaneous Lorentz breaking at high energies. *JHEP* 05, 076. **[A]**
- Feldstein, B. (2009). Spontaneous Lorentz violation, negative energy and the second law of thermodynamics. arXiv:0904.1212. **[A]**
- Visser, M., Kar, S. & Dadhich, N. (2003). Traversable wormholes with arbitrarily small energy condition violations. *PRL* 90, 201102. **[A]**
- Fewster, C. J. & Roman, T. A. (2005). On wormholes with arbitrarily small quantities of exotic matter. *PRD* 72, 044023. **[F]**
- Ford, L. H. & Roman, T. A. (1996). Quantum field theory constrains traversable wormhole geometries. *PRD* 53, 5496–5507. **[S]**
- Morris, M. S. & Thorne, K. S. (1988). Wormholes in spacetime. *AJP* 56, 395–412. **[S]**
- Maldacena, J., Milekhin, A. & Popov, F. (2018). Traversable wormholes in four dimensions. arXiv:1807.04726; *CQG* 40, 155016 (2023). **[F]**
- Kontou, E.-A. & Sanders, K. (2020). Energy conditions in general relativity and quantum field theory. *CQG* 37, 193001. **[F]**
- Kontou, E.-A. (2024). Wormhole restrictions from quantum energy inequalities. *Universe* 10, 291. **[F]**
- Graham, N. & Olum, K. D. (2007). Achronal averaged null energy condition. *PRD* 76, 064001. **[F]**
- Kontou, E.-A. & Olum, K. D. (2015). Proof of the ANEC in a classical curved spacetime using a null-projected quantum inequality. arXiv:1507.00297. **[F]**
- Kelly, W. R. & Wall, A. C. (2014). Holographic proof of the averaged null energy condition. *PRD* 90, 106003. **[A]**
- Hartman, T., Kundu, S. & Tajdini, A. (2017). Averaged null energy condition from causality. *JHEP* 07, 066. **[F]**
- Faulkner, T., Leigh, R. G., Parrikar, O. & Wang, H. (2016). Modular Hamiltonians for deformed half-spaces and the ANEC. *JHEP* 09, 038. **[S]**
- Wall, A. C. (2010). Proving the achronal ANEC from the generalized second law. arXiv:0910.5751. **[F]**
- Ishibashi, A., Maeda, K. & Mefford, E. (2019). Achronal ANEC, weak cosmic censorship, and AdS/CFT duality. *PRD* 100, 066008. **[F]**
- Iizuka, N., Ishibashi, A. & Maeda, K. (2020). Conformally invariant averaged null energy condition from AdS/CFT. *JHEP* 03, 161. **[A]**
- Iizuka, N., Ishibashi, A. & Maeda, K. (2020). The averaged null energy conditions in even dimensional curved spacetimes from AdS/CFT duality. *JHEP* 10, 106; arXiv:2008.07942. **[F]**
- Urban, D. & Olum, K. D. (2010). ANEC violation in a conformally flat spacetime. *PRD* 81, 024039. **[A]**
- Visser, M. (1994). Scale anomalies imply violation of the averaged null energy condition. gr-qc/9409043. **[A]**
- Ceyhan, F. & Faulkner, T. (2018). Recovering the QNEC from the ANEC. arXiv:1812.04683. **[A]**
- Balakrishnan, S., Faulkner, T., Khandker, Z. U. & Wang, H. (2019). A general proof of the quantum null energy condition. *JHEP* 09, 020. **[A]**
- Kudler-Flam, J., Leutheusser, S., Rahman, A. A., Satishchandran, G. & Speranza, A. J. (2025). Covariant regulator for entanglement entropy: proofs of the Bekenstein bound and the quantum null energy condition. *PRD* 111, 105001; arXiv:2312.07646. **[F]**
- Freivogel, B., Kontou, E.-A. & Krommydas, D. (2020). The return of the singularities: applications of the smeared null energy condition. arXiv:2012.11569. **[A]**
- Alcubierre, M. (1994). The warp drive. *CQG* 11, L73–L77. **[S]**
- Bobrick, A. & Martire, G. (2021). Introducing physical warp drives. *CQG* 38, 105009. **[F]**

### B.4 Causal structure, chronology and Lorentz violation

- Penrose, R. (1965). Gravitational collapse and space-time singularities. *PRL* 14, 57–59. **[S]**
- Landsman, K. (2022). Penrose's 1965 singularity theorem. *GRG* 54, 115. **[F]**
- Hawking, S. W. (1992). Chronology protection conjecture. *PRD* 46, 603–611. **[S]**
- Gao, S. & Wald, R. M. (2000). Theorems on gravitational time delay and related issues. *CQG* 17, 4999. **[S]**
- Friedman, J. L. (2004). The Cauchy problem on spacetimes that are not globally hyperbolic. gr-qc/0401004. **[F]**
- Hořava, P. (2009). Quantum gravity at a Lifshitz point. *PRD* 79, 084008. **[S]**
- Jacobson, T. & Mattingly, D. (2001). Gravity with a dynamical preferred frame. *PRD* 64, 024028. **[S]**
- Berglund, P., Bhattacharyya, J. & Mattingly, D. (2013). Towards thermodynamics of universal horizons in Einstein-aether theory. *PRL* 110, 071301. **[F]**
- Colladay, D. & Kostelecký, V. A. (1998). Lorentz-violating extension of the standard model. *PRD* 58, 116002. **[F]**
- Greenberg, O. W. (2002). CPT violation implies violation of Lorentz invariance. *PRL* 89, 231602. **[S]**

### B.5 Quantum foundations

- Bell, J. S. (1964). On the Einstein Podolsky Rosen paradox. *Physics* 1, 195–200. **[S]**
- Tsirelson, B. S. (1980). Quantum generalizations of Bell's inequality. *LMP* 4, 93–100. **[S]**
- Popescu, S. & Rohrlich, D. (1994). Quantum nonlocality as an axiom. *Foundations of Physics* 24, 379–385. **[S]**
- Pawłowski, M. et al. (2009). Information causality as a physical principle. *Nature* 461, 1101–1104. **[A]**
- Wootters, W. K. & Zurek, W. H. (1982). A single quantum cannot be cloned. *Nature* 299, 802–803. **[S]**
- Weinberg, S. (1989). Testing quantum mechanics. *Annals of Physics* 194, 336. **[S]**
- Polchinski, J. (1991). Weinberg's nonlinear quantum mechanics and the EPR paradox. *PRL* 66, 397–400. **[A]**
- Abrams, D. S. & Lloyd, S. (1998). Nonlinear quantum mechanics implies polynomial-time solution for NP-complete and #P problems. *PRL* 81, 3992–3995. **[F]**
- Simon, C., Bužek, V. & Gisin, N. (2001). No-signaling condition and quantum dynamics. *PRL* 87, 170405. **[A]**
- Soulas, A. (2025). A proof that no-signalling implies microcausality in QFT. *Foundations of Physics* 55, 22. **[A]**
- Sorkin, R. D. (1993). Impossible measurements on quantum fields. *Directions in General Relativity* vol. 2. **[S]**
- Rastegin, A. E. (2009). A note on general no-cloning theorem for black boxes. arXiv:0908.1668. **[F]**
- Sbisà, F. (2015). Classical and quantum ghosts. *European Journal of Physics* 36, 015009; arXiv:1406.4550. **[A]**

### B.6 Closed timelike curves in quantum theory

- Deutsch, D. (1991). Quantum mechanics near closed timelike lines. *PRD* 44, 3197–3217. **[S]**
- Lloyd, S. et al. (2011). Closed timelike curves via postselection. *PRL* 106, 040403. **[F]**
- Brun, T. A., Harrington, J. & Wilde, M. M. (2009). Localized CTCs can perfectly distinguish quantum states. *PRL* 102, 210402. **[S]**
- Bennett, C. H., Leung, D., Smith, G. & Smolin, J. A. (2009). Can CTCs or nonlinear QM improve quantum state discrimination? *PRL* 103, 170502. **[A]**
- Oreshkov, O., Costa, F. & Brukner, Č. (2012). Quantum correlations with no causal order. *Nature Communications* 3, 1092. **[S]**

### B.7 Black hole thermodynamics and unitarity

- Banks, T., Susskind, L. & Peskin, M. E. (1984). Difficulties for the evolution of pure states into mixed states. *Nuclear Physics B* 244(1), 125–134. **[A]**
- Nikolić, H. (2015). Violation of unitarity by Hawking radiation does not violate energy-momentum conservation. *JCAP* 04, 002. **[A]**
- Dubovsky, S. L. & Sibiryakov, S. M. (2006). Spontaneous breaking of Lorentz invariance, black holes and perpetuum mobile of the 2nd kind. *PLB* 638, 509–514. **[F]**
- Eling, C., Foster, B. Z., Jacobson, T. & Wall, A. C. (2007). Lorentz violation and perpetual motion. *PRD* 75, 101502(R). **[F]**
- Wall, A. C. (2012). A proof of the generalized second law for rapidly changing fields and arbitrary horizon slices. *CQG* 30, 165003. **[A]**
- Casini, H. (2008). Relative entropy and the Bekenstein bound. *CQG* 25, 205021. **[S]**
- Witten, E. (2022). Gravity and the crossed product. *JHEP* 2022, 8. **[S]**

### B.8 Measurements

- Abbott, B. P. et al. (2017). GW170817 and GRB 170817A. *ApJL* 848, L13. **[S]**
- Touboul, P. et al. (2022). MICROSCOPE final results. *PRL* 129, 121102. **[S]**
- Lamoreaux, S. K. (1997). Demonstration of the Casimir force in the 0.6 to 6 µm range. *PRL* 78, 5–8. **[S]**
- Hensen, B. et al. (2015). Loophole-free Bell inequality violation. *Nature* 526, 682–686. **[S]**

---

## Appendix C · Verification

Twenty-six numerical claims were re-audited against fresh computation with zero failures. Two propositions replaced
sampled claims with proofs (1.2 and 4.3). One error was found inside a correction — a parameter used with two
meanings in the same computation — caught only because the fermionic case failed to reproduce 13,585.

The document runs against twenty-one structural audits covering lattice properties, equation reproduction, internal
consistency, undefined terms, encoding artefacts, coherence, attribution, figure coverage, distinctness, scoping,
antecedents, markup, dataset agreement, arithmetic, enumeration, fidelity, artifact measure, reproducibility,
sequence, projection and input.

**Audit 22 — term match — is external by construction and cannot join them.** Its output is the vocabulary debt:
**{A22['unchecked']} of {A22['pairs']} pairs unchecked.** That number, not the twenty-one passes, is what tells a
reader how far to trust the rest.

All figures are computed from cached datasets. The computation scripts, datasets, build script and audit script
accompany this paper.
"""

open('/mnt/user-data/outputs/Transitions.md','w').write(md)
print('written', len(md), 'chars')
