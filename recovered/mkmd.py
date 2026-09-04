#!/usr/bin/env python3
"""Generate Transitions.md from the cached datasets, so numbers stay synced with the PDF."""
import json
D = json.load(open('/home/claude/paper/data.json'))
V2=D['v2']; T=D['tower']; O=D['order']; Q=D['quiver']; R=D['routes']
H=D['hasse']; MOL=D['molecular']; CN=D['containment']; PT=V2['ptable']; CV=V2['coverage']
f=lambda n: f'{n:,}'
FIG='figures/'

def objrow(o): return f"| {o['name']} | `{o['threshold']}` | {f(o['cells'])} | {'**yes**' if o['here'] else 'no'} | {f(o['reachable'])} |"

md = f"""# TRANSITIONS

### The closure defect of an index, and what it costs to leave a universe

**Matthew Lach** · Independent Researcher

---

**Abstract.** For a finite set of integer tuples X we compute **E(X) = |R(X)| − |X|**, where R is the closure of X
under its monotone pairwise envelopes. We prove R is a closure operator and that E ≥ 0, and we identify E = 0 with
global consistency of a binary constraint network. Applied to an atomic-structure lattice Λ of 976 cells and its
tower to {f(T['cells'][-1])}, the defect is zero at every level, verified by ambient-box sweep to
{f(T['box'][-1])} tuples; the certificates are Freuder (1982) for the tree levels and Montanari (1974) for the
monotone ones. Applied to an index of which physical laws must break to reach another universe, the defect is
**{V2['defect']}**, and it collapses exactly to **one cell times a multiplicity of thirty**. The core is a single
profile: macroscopic exotic matter with no preferred frame and unitary evolution. We show the cause is one ternary
constraint with a unique minimal support, verified over {V2['support']['subsets_checked']} coordinate subsets;
that **six distinct operations on the coordinate system all fail to repair it**, including an exhaustive search
over all {f(V2['relabel']['tested'])} axis relabellings; and that the periodic table's own defect of 36, by
contrast, vanishes under mere re-placement. A universe is a globally consistent constraint network; a transition
between universes is not expressible as one.

> **What this paper does not claim.** Nothing here bears on whether other universes exist, or whether transit
> between them is physically achievable. Every result is a statement about an *index* — what a coordinate system
> can and cannot carry. The precedent is the periodic table, whose defect of 36 is a fact about a drawing and not
> about chemistry.

![The result]({FIG}f6_1.png)

*Figure 6.1 (shown first). One object is decidable by local consistency; the two that cross between universes are
not, and for the same reason.*

---

## Contents

- [Part 0 · Procedure](#part-0--procedure)
- [Part I · The operator](#part-i--the-operator)
- [Part II · Λ verified](#part-ii--λ-verified)
- [Part III · Transit structures on Λ](#part-iii--transit-structures-on-λ)
- [Part IV · The violation index](#part-iv--the-violation-index)
- [Part V · The multilattice](#part-v--the-multilattice)
- [Part VI · Results](#part-vi--results)
- [Part VII · Register of withdrawals](#part-vii--register-of-withdrawals)
- [Part VIII · The finish line, located](#part-viii--the-finish-line-located)
- [Part IX · Open](#part-ix--open)
- [Appendix A · Equations](#appendix-a--equations)
- [Appendix B · References and sources](#appendix-b--references-and-sources)
- [Appendix C · Verification](#appendix-c--verification)

---

## Part 0 · Procedure

The protocols below were in force throughout and are reported because several results in this paper are
corrections of earlier results obtained without them.

### 0.1 Protocols

| protocol | |
|---|---|
| commit before looking | a position is written down before any retrieval; the retrieval scores it |
| compute before writing | numerical claims are computed, then reported, never the reverse |
| refuse rather than coerce | an ambiguous instruction is queried, not defaulted |
| enumerate before searching | targets are listed before the first search and re-listed when the set grows |
| record what a failure excludes | a falsified prediction is logged with the class of claim it rules out |

### 0.2 The Admission Law

> An open index admits any content, and admits it only together with its verification grade. An entry's grade
> bounds the operations it may enter. **A derived entry carries the minimum grade of its inputs, and no derivation
> raises a grade.** Content contradicting the index is admitted and flagged as a collision; a collision is
> discharged by re-deriving the internal result, never by refusing the content.

The last clause matters. An index that refuses contradicting content closes itself against exactly the information
that would correct it. Every substantive repair in this work arrived as a collision. The bibliography in Appendix B
carries an access grade per source for the same reason.

### 0.3 The merge rule

Five coordinate merges were attempted. One was licensed by a stated biconditional; four by a one-way implication or
an intuitive ordering. All four failed, and the survivor failed under grading.

| merge | basis | outcome |
|---|---|---|
| cloning ≡ discrimination | stated biconditional | holds at the perfect rung only |
| nonlinearity → signalling | one-way implication | failed — Polchinski nonlinearities do not signal |
| microcausality → signalling | one-way implication | failed — converse denied by Sorkin scenarios |
| signalling on the CHSH scale | intuitive ordering | failed — PR boxes reach 4 without signalling |
| discrimination into correlation | intuitive ordering | failed — different quantities |

> **Rule.** A biconditional licenses a merge only if it holds at every rung of the graded axis. Merging on a fact
> true at one point and then grading the axis is the error.

### 0.4 Operator reliability, measured

Prediction accuracy was tracked by target class rather than assumed uniform. Predictions aimed at logical structure
— which hypotheses a theorem takes, which way an entailment runs, what a conclusion licenses — scored 4/4 on three
consecutive tests. Predictions aimed at how a field regards a claim scored 1/4. Predictions of implications not yet
in the index scored about 1 in 5. Under 0.2 the last class was therefore barred from entering content: every clause
in Part IV was entered from retrieval, never from assessment.

---

## Part I · The operator

### 1.1 Definitions

For a finite X ⊆ ∏Aᵢ of integer tuples, write **Âᵢ(X) = {{xᵢ : x ∈ X}}** for the value sets and
**φ̂ᵢⱼ(v) = max{{xᵢ : x ∈ X, xⱼ ≤ v}}** for the monotone upper envelope of coordinate i against coordinate j.
Then R(X) collects every point of the observed product box respecting all envelopes, and E(X) is its excess.
Equations (1)–(4) of Appendix A give these in full. No outside knowledge enters R(X): it is what a reader could
reconstruct from the cells alone.

### 1.2 Proposition. X ⊆ R(X), hence E ≥ 0

> *Proof.* Let x ∈ X. Each xᵢ ∈ Âᵢ(X) by definition. For any i ≠ j the set {{yᵢ : y ∈ X, yⱼ ≤ xⱼ}} contains xᵢ,
> since x satisfies xⱼ ≤ xⱼ. Hence φ̂ᵢⱼ(xⱼ) ≥ xᵢ, so x ∈ R(X). ∎

The word *defect* is therefore justified: E counts cells the structure admits and the index denies, and can never
count in the other direction.

### 1.3 Proposition. R is a closure operator

Extensive by 1.2. Monotone and idempotent by computation: R(R(X)) = R(X) on Λ₈ and on the violation index;
monotonicity held on thirty nested random pairs with no failure. The closed sets therefore form a Moore family.

### 1.4 Identification

R is the closure of a binary constraint network under monotone binary projections, and **E(X) = 0 if and only if
the network is globally consistent** — every tuple satisfying all binary projections is a solution.

### 1.5 R against the full minimal network

Writing BPC(X) for closure under the *full* binary projections rather than their monotone envelopes,
X ⊆ BPC(X) ⊆ R(X) — equation (5). So E > 0 is in principle ambiguous between genuine inconsistency and envelope
coarseness. Computed for both objects here, **the ambiguity does not arise**: R = BPC exactly, so R is the minimal
network and the whole defect is global-consistency failure.

![Nested sets]({FIG}f1_1.png)

*Figure 1.1. For Λ₈ all three coincide at 976. For the violation index X = {f(V2['cells'])} while
BPC = R = {f(V2['R'])} — {V2['defect']} tuples in the minimal network that are not solutions, and
{V2['env_coarse']} envelope coarseness.*

### 1.6 Six blindnesses

| blind to | instance | effect on E |
|---|---|---|
| decreasing bounds (exclusion) | a preferred frame forbids chronology violation | 0 → 6 |
| non-monotone relations (congruence) | seniority parity on axis 10 | 0 → 678 |
| multi-coordinate (ternary) constraints | conjugation ceiling / coupling triangle | 186 / 35,570 |
| unoccupied dimensions | a fifth axis nothing occupies | unchanged |
| the measure | two universes, same cells, different energies | unchanged |
| derived coordinates | an axis defined as a function of others | {V2['defect']} → 120 |

**A derived coordinate cannot repair closure.** R reconstructs from cells alone, so a reader given the cells cannot
see that a coordinate was *defined* as a function of others; meanwhile the ambient box grows by that coordinate's
value count while |X| stays fixed. This excludes the entire class of derived-coordinate repairs, for any index.

![Blindness panels]({FIG}f1_2.png)

*Figure 1.2. What an upper envelope cannot cut. Black: solutions. Red: admitted by R, denied by the constraint.*

### 1.7 The closure rule

> **A tightening preserves E = 0 if and only if it binds one coordinate by a monotone function of one other.**

![Closure rule]({FIG}f1_3.png)

*Figure 1.3. Four tightenings of the lattice, two on each side of the rule.*

### 1.8 Named theorems

| result | statement |
|---|---|
| Freuder 1982 | a tree-structured constraint network is globally consistent after arc consistency |
| Montanari 1974 | for monotone constraints, path consistency implies global consistency |
| van Beek & Dechter 1995 | generalisation of monotone to row-convex constraints |
| van Beek & Dechter 1997 | constraint tightness — the exact/admissible ratio |

These two theorems cover the lattice between them: Λ₉ is a tree and every level is monotone. Neither applies to the
violation index, which is neither.

---

## Part II · Λ verified

Λ is an atomic-structure lattice. Cells are 8-tuples (n, ℓ, k, q, e, f, g, 2S) built by nested bounds — equations
(6)–(12). The tower Λ₉–Λ₁₃ adds target spin, seniority, the core's J, K and the outer J, equations (13)–(17).
Caps (n, e, ℓ, k, f) = (3, 3, 1, 3, 1) are unique in the search range for 976 cells.

### 2.1 The tower closes at every level

| level | {' | '.join(str(l) for l in T['level'])} |
|---|{'---|'*len(T['level'])}
| cells | {' | '.join(f(c) for c in T['cells'])} |
| ambient box | {' | '.join(f(b) for b in T['box'])} |
| E | {' | '.join('0' for _ in T['level'])} |

Every level was swept against its entire ambient box, to {f(T['box'][-1])} tuples at Λ₁₃. Global consistency in the
strict sense also holds: |BPC(Λ₈)| = 976 = |Λ₈|.

![The tower]({FIG}f2_1.png)

*Figure 2.1. Cells and ambient box diverge on a log scale while E stays zero.*

### 2.2 Why it closes

Λ₉'s constraint graph has nine nodes and eight edges and is a tree, so Freuder applies. Λ₉′ — the same lattice with
the admissible Pauli cut 2S′ ≤ 2f+1, which removes 93 cells, leaving {f(T['L9prime'])} — gains the cycle f–g–2S′
and loses the guarantee. Λ₁₀ has ten nodes and ten edges and is also not a tree, so **Λ₉ is the last tree level**.

![Constraint graphs]({FIG}f2_2.png)

*Figure 2.2. One added edge converts a tree into a cycle.*

### 2.3 Where the exactness goes

All six density values reproduce once three non-obvious exact sets are used: the spin set of f^g by microstate
enumeration at axis 9; terms genuinely *new* at occupancy v, conjoined with the parity congruence and the
conjugation ceiling, at axis 10; and the J values of terms of ℓᵏ carrying the cell's own multiplicity 2S at axis 11.
Without the third, axis 11 computes to 43.1% instead of {D['density']['11']}%.

![Densities]({FIG}f2_3.png)

*Figure 2.3. Density per axis: {' / '.join(str(D['density'][k]) for k in ['9',"9'",'10','11','12','13'])}.*

### 2.4 Closure and exactness are incompatible

Imposing the exact coupling triangle on axis 12 cuts the lattice from {f(D['axis12']['loose_cells'])} to
{f(D['axis12']['tight_cells'])} cells and takes E from zero to {f(D['axis12']['tight_E'])} — because the exact
bound is ternary, outside the closure-preserving class.

> **Λ is loose by design.** Every coupling coordinate's exact physical bound requires either two parents or a
> congruence, and a tree carries only one.

![Closure vs exactness]({FIG}f2_4.png)

*Figure 2.4. The same axis, loose and exact.*

### 2.5 The periodic table's defect is placement, not coordinates

The eighteen-column table has E = {PT['E']} — sixteen cells in period 1, ten each in periods 2 and 3. It is standard
to say the Janet left-step table removes them by re-indexing period as n + ℓ. **That is not what does the work.**

> Placing the *same ninety elements* contiguously within each period, with period untouched, gives
> **E = {PT['contiguous_E']}**. The defect comes from putting hydrogen at group 1 and helium at group 18 with
> sixteen empty cells between — an interior hole, which an upper envelope cannot cut because it must reach group 18
> to admit helium.

So the 36 do not vanish under Janet; they stop being *visible*. And they are not absent objects: **{PT['law']} of
them** — 1p, 1d and 2d — could never hold an element, being forbidden by ℓ ≤ n−1. They are the footprint of a law
the coordinate system has no axis for. The remaining **{PT['convention']}** are 3d, which exists and is merely
deferred past 4s by the Madelung order: those are convention.

**The 36 is two constraints casting a thirty-six-cell shadow, not thirty-six facts.**

![Periodic table]({FIG}f2_5.png)

*Figure 2.5. Three presentations of the same chemistry. Contiguity, not the choice of period, is what closes the
table. Janet: {f(PT['janet_cells'])} cells, E = {PT['janet_E']}.*

This makes the periodic table the **control** for the rest of the paper rather than an analogy. It is an arity-2
defect and therefore removable, which is what makes the violation index's irremovability in Part IV a measurement
rather than a failure to search.

---

## Part III · Transit structures on Λ

### 3.1 Λ₉ is the transit level

A cell's target is a legal source exactly when 2S′ ≤ g — which *is* axis 9, equation (19). Of {f(T['cells'][1])}
cells, {f(Q['arcs'])} are composable. So Λ₉ is simultaneously the first level at which a transition has a defined
endpoint and the last level that is a tree.

![The window]({FIG}f3_1.png)

*Figure 3.1. First composable, last tree.*

### 3.2 The composition graph is a line digraph

Composable cells are the arcs of a quiver Q on {Q['states']} atomic states. The composition graph is the line
digraph L(Q) and its edge count is **{f(Q['line_edges'])} = Σ(in × out)** exactly, equation (20). The
{Q['loops']} degenerate cells are Q's loops, and because Q has a loop at every vertex **return is available in one
step from every state**.

![Quiver]({FIG}f3_2.png)

*Figure 3.2. The quiver and its line digraph.*

### 3.3 The Hasse diagram, and girth exactly 4

Unit-step adjacency on Λ₉ coincides with the covering relation exactly — {f(H['edges'])} edges either way, so the
lattice is gap-free. Degrees run {H['deg_min']} to {H['deg_max']}, mean {H['deg_mean']}, connected.

> **Proposition.** The girth is exactly 4. *Proof.* Three mutually adjacent cells are impossible: if a–b differ in
> coordinate i and b–c in j ≠ i then a–c differ in two coordinates; if i = j then a–c differ by 0 or 2. So no
> triangle exists and the girth is at least 4. A square c, c+eᵢ, c+eᵢ+eⱼ, c+eⱼ is exhibited. ∎

![Girth]({FIG}f3_3.png)

*Figure 3.3. Girth exactly 4, proved rather than sampled.*

### 3.4 Molecular transit

A molecule moves as one fibre, so all its atoms take the same displacement and a circuit is a square. Feasibility
is an intersection question — equations (21)–(22).

| atoms | {' | '.join(str(r['m']) for r in MOL)} |
|---|{'---|'*len(MOL)}
| feasibility | {' | '.join(f"{r['rate']:.3g}%" for r in MOL)} |
| trials | {' | '.join(f"{r['N']//1000}k" for r in MOL)} |

The decay is geometric at roughly a factor of 1.9 per atom. Homonuclear molecules are unconstrained.

![Molecular feasibility]({FIG}f3_4.png)

*Figure 3.4. Joint 4-cycle feasibility against atom count, 95% Wilson intervals.*

### 3.5 The Helly number

> **The Helly number is at least {V2['helly']['lower']} and at most {V2['helly']['upper']}.** A critical family of
> size five is exhibited: every four of its members intersect and the five do not. The upper bound is the ground
> set — all C(9,2) × 4 = {V2['helly']['possible']} square directions occur, and a minimal family with empty
> intersection can have at most one member per omitted point.

So molecular transit is not reducible to pairwise or four-wise checks, and is reducible to 144-wise, which is a
bound and a useless one.

> An earlier version of this work reported the Helly number as unbounded, on the strength of a joint-given-pairwise
> ratio falling without saturation to m = 6. That ratio measures how often random families intersect, not the Helly
> number, and the inference was invalid. See Part VII.

![Helly]({FIG}f3_5.png)

*Figure 3.5. Helly failure.*

---

## Part IV · The violation index

### 4.1 Coordinates and rungs

> **Notation.** E denotes the closure defect throughout. The null-energy coordinate of the violation index is
> written NEC to avoid the collision.

| axis | rungs |
|---|---|
| **X** causal ladder | Lorentz invariant / preferred threading / preferred foliation / chronology violated |
| **S_corr** correlation | local ≤2 / quantum ≤2√2 / post-quantum ≤4 |
| **IC** information causality | holds / violated at m>0 / violated at m=0 |
| **U** unitarity | unitary / local, energy-momentum-conserving non-unitarity / requiring locality to break |
| **NEC** null energy | intact / pointwise / ANEC arbitrarily small / macroscopic QI-bounded / QI-violating |
| **L** linearity | linear / nonlinear |
| **SD** microcausality | holds / fails |
| **DN_c** cloning | quantum-optimal / beyond / perfect deterministic |
| **DN_d** discrimination | quantum-optimal / beyond / perfect |

### 4.2 Our own position, two components fixed by measurement

The origin is **{tuple(V2['origin'])}**. **S_corr = 1**: quantum mechanics violates Bell locality while respecting
microcausality. **NEC = 1**: Casimir energy is measured, gives negative energy density, and violates the null energy
condition pointwise while satisfying its averaged form.

![Nine axes]({FIG}f4_1.png)

*Figure 4.1. The nine axes and our position.*

### 4.3 Routes, and the cost of a formalism

| CTC model | destination floor | steps |
|---|---|---|
| Deutsch (D-CTC) | {tuple(R['D-CTC']['dest'])} | {R['D-CTC']['steps']} |
| post-selected (P-CTC) | {tuple(R['P-CTC']['dest'])} | {R['P-CTC']['steps']} |
| model-independent | {tuple(R['model-independent']['dest'])} | {R['model-independent']['steps']} |

Model-independently, chronology violation requires the causal ladder, non-unitarity at the Lindblad rung, and
arbitrarily small ANEC violation — and **not** signalling, cloning, nonlinearity or loss of microcausality, each of
which appears in the destination under Deutsch's prescription and not otherwise.

![Three routes]({FIG}f4_2.png)

*Figure 4.2. The formalism choice is load-bearing on the destination, not only on the path.*

### 4.4 The defect, and its collapse

The index holds {f(V2['cells'])} cells; its minimal network holds {f(V2['BPC'])}. **The defect is
{V2['defect']}**, all of it genuine global-consistency failure — envelope coarseness contributes
{V2['env_coarse']}.

> **It is not thirty findings.** The excess is exactly the product of a core with a multiplicity:
> **1 × {V2['multiplicity']}**, and the product is exact. The thirty is not a property of the defect at all — it is
> the number of configurations the index itself admits alongside X = 0, U = 0, SD = 0, computed independently and
> matching.

**The core is one cell: (X = 0, U = 0, NEC = 3)** — macroscopic exotic matter, no preferred frame, unitary
evolution. Coarsening the NEC axis all the way to *violated or not* still leaves it, and the envelope calculation
says why in two lines:

```
φ(NEC | X = 0)  must permit the value, because X = 0 cells with U ≥ 1 reach it
φ(NEC | U = 0)  must permit the value, because U = 0 cells with X ≥ 1 reach it
```

**Both conditioning coordinates individually admit what the pair forbids.**

![The collapse]({FIG}f4_3.png)

*Figure 4.3. The defect collapses to a single cell times a multiplicity.*

### 4.5 Cause, and the unique minimal support

The constraint the envelope cannot see is a two-payer branch. Three independent literatures give it, from unrelated
starting points, and **none gives a single payer**: Buniy–Hsu–Murray from effective field theory;
Hartman–Kundu–Tajdini from microcausality, whose theorem assumes unitary *and* Lorentz-invariant *and* interacting,
so violating its conclusion breaks one of three; and Wall from the generalised second law.

> **The support is unique.** Of {V2['support']['subsets_checked']} coordinate subsets that exclude
> {{X, U, NEC}}, **{V2['support']['failing']}** fail to close. The triple is the only minimal failing subset, and
> every larger failure is it carried up by free coordinates. The index has **arity exactly 3, with one generator**.

### 4.6 The repair space is closed

| operation | outcome | E | why |
|---|---|---|---|
| merge by identification | not licensed | — | no pair among {{X, U, NEC}} is biconditional at every rung |
| merge by linearisation | worse | {V2['repairs'][1]['E']} | collapsing two axes forces every constraint on either through one envelope |
| relabel axis values | never zero | min {V2['relabel']['min_E']} | exhaustive: {V2['relabel']['zeros']} of {f(V2['relabel']['tested'])} |
| slide within rows | never better | {V2['repairs'][3]['E']} | the hole is a row that should not exist, not a gap within one |
| add a derived coordinate | worse | {V2['repairs'][4]['E']} | a defined axis inflates the box and adds nothing R can see |
| split an axis | neutral or worse | {V2['repairs'][5]['E']} | pins the antecedent as well as the consequent |

> **Adding fails because the box inflates; merging fails because the envelopes coarsen.** Both directions are
> excluded, for opposite reasons, and the two-line envelope argument covers all six at once.

![Six repairs]({FIG}f4_5.png)

*Figure 4.5. Six operations, none of which repairs the defect.*

### 4.7 Objects are thresholds, not cells

The index defines by cost. An object is definable in it only if the object requires a law to break — which is why a
classical black hole, a vacuum solution of ordinary general relativity, is invisible to it.

| object | threshold | cells | here? | reachable |
|---|---|---|---|---|
{chr(10).join(objrow(o) for o in V2['objects'])}

Of the {f(V2['wormhole_cost']['total'])} cells permitting a macroscopic wormhole,
{f(V2['wormhole_cost']['frame'])} pay with a preferred frame, {f(V2['wormhole_cost']['nonunitary'])} with
non-unitarity, {f(V2['wormhole_cost']['signalling'])} with signalling — and **{V2['wormhole_cost']['free']} pay
with none of the three**. That zero is the core, seen from inside.

An evaporating black hole *is* available at our own profile: Hawking radiation needs pointwise NEC violation, which
is the Casimir rung we occupy. It is the one object here that requires breaking a law, and we have it.

![Thresholds]({FIG}f4_6.png)

*Figure 4.6. Objects as thresholds on profiles.*

> **What this does not license.** A cell is not a wormhole; permission is not existence; reachability is not
> achievability; and the core is not a place — none of its cells is in the index, and none overlaps the unreachable
> set.

### 4.8 The defect does not scale

| coordinates | {' | '.join(str(p['coords']) for p in V2['projection'])} |
|---|{'---|'*len(V2['projection'])}
| defect | {' | '.join(str(p['E']) for p in V2['projection'])} |
| core | {' | '.join(str(p['core']) for p in V2['projection'])} |
| multiplicity | {' | '.join(str(p['mult']) for p in V2['projection'])} |

The core is invariant at one cell at every resolution; only the number of free-coordinate configurations moves,
which is arithmetic rather than structure. An earlier version reported the sequence itself as a scaling law; that
reading is withdrawn in Part VII.

![Projection]({FIG}f4_7.png)

*Figure 4.7. The core is constant; the multiplicity is what grows.*

---

## Part V · The multilattice

### 5.1 Statistics

Post-quantum correlation breaks the spin-statistics theorem, hence Pauli exclusion. Generalising to m particles per
spin-orbital gives capacity m(4ℓ+2), equation (25). At m = 1 the construction reproduces the canonical tower exactly
— 976, 1,654, 2,535, 13,585. **E = 0 at levels 8 through 11 for m = 1, 2 and 3.**

### 5.2 Lorentz violation does not change the lattice

The Standard-Model Extension computes energy shifts in the existing basis. The Coulomb accidental degeneracy lifts;
the quantum numbers do not move, because ℓ ≤ n−1 follows from node counting.

> **Corollary.** The lattice does not individuate universes. Our Lorentz-violating neighbour has the same 976 cells
> and a different energy ordering — invisible to R.

### 5.3 Which modifications close

Four monotone ℓ-bound variants close; two non-monotone variants do not, at E = 61,845 and 19,245. The decisive pair
is ℓ ≤ ⌊n/2⌋ and ℓ ≤ |n−3|, which have **identical cardinality** at 32,535 cells, one closed and one open.

![l-bounds]({FIG}f5_1.png)

*Figure 5.1. Monotone φ closes; peaked φ does not.*

### 5.4 Transit admissibility

| direction | cells lost |
|---|---|
| ours → relaxed ({f(CN['m1'])} into {f(CN['m2'])}) | **{CN['outward_lost']}** |
| relaxed → ours | {f(CN['inward_lost'])} |

**Transit outward is unobstructed; inward is not.** A cell with occupancy beyond our Pauli bound fails our 1D index
outright, before any question of joint structure arises.

![Containment]({FIG}f5_2.png)

*Figure 5.2. Transit admissibility is directional.*

### 5.5 What the index cannot carry

Three things locate a transition and the index certifies only the first. **The lattice says what exists.**
**The order says what is near** — of {f(O['pairs'])} pairs of Λ₈ cells only {O['comparable_pct']:.1f}% are ordered
by componentwise domination. **The measure says what it costs** — and it is external.

Our own measure is not faithful to our own order. Of the {f(O['comparable'])} ordered pairs,
**{O['samen_pct']:.1f}%** share the principal quantum number and are indistinguishable to a Coulomb energy function.

![Order and measure]({FIG}f5_3.png)

*Figure 5.3. Red: ordered pairs our own measure cannot separate.*

---

## Part VI · Results

**1. A universe is a globally consistent constraint network.** Λ is binary, monotone, tree-structured at Λ₉ and
monotone above it; E = 0 at every level and profile tested; the certificates are Freuder 1982 and Montanari 1974.

**2. A transition between universes is not expressible as one.** The cost of leaving is a ternary disjunction
carrying defect {V2['defect']}, which collapses to one cell. What may be carried has Helly number at least 5.

**3. The defect is one cell, and it is irremovable.** Unique minimal support verified over
{V2['support']['subsets_checked']} subsets; six coordinate operations tried and all failing;
{f(V2['relabel']['tested'])} relabellings exhausted.

**4. Time travel, model-independently.** Destination floor X = 3, U = 1, NEC = 2. Transit domain Λ₉. Circuit floor
girth 4. Feasibility decaying geometrically to {MOL[-1]['rate']:.4g}% at twelve atoms.

**5. Openness is the signature, not a failure.** A closed index is a universe. The violation index does not close.

---

## Part VII · Register of withdrawals

Reported in full because several are corrections of results this work previously held, and because the pattern of
failure is itself a finding.

| claim | cause |
|---|---|
| sixteen destinations; 57 profiles; E = 0 | the table was silently Deutsch-model, the assumption unmarked |
| surviving addresses {{Rd}} and {{E, Rd}} | computed over merges since undone |
| path-reachability distinct from jump | closure supplies satisfying disjuncts automatically |
| E = 0 for the violation index | inherited from one mis-typed edge at all six reconstructions |
| "global parabolicity" | the author's own term, not in the source literature |
| 0.03% feasibility at ten atoms | one hit in 4,000 draws; true value {[r for r in MOL if r['m']==10][0]['rate']:.4g}% |
| the 6/20/60 trend as reported | read across separately-built indices; required a controlled projection |
| **the violation index's defect of 60, with the disjunction at NEC ≥ 2** | the constraint is about *scale*: macroscopic wormholes are excluded, Planck-scale ones are not. Imposing it at the wrong rung cost 30 admissible universes and doubled the defect |
| **Helly number unbounded** | a falling joint-given-pairwise ratio measures how often random families intersect, not the Helly number. True value: between 5 and 144 |
| **projection-covariance as a scaling law** | the defect does not scale; the core is 1 at every resolution |
| **X ≥ 1 → U ≥ 1 (the closed 1,404-cell variant)** | the ordinary second law survives Lorentz violation — stated by the authors of the result the edge rested on |
| **instability routed to (¬U ∨ X ≥ 1)** | Buniy is scoped to Lorentz-invariant theories; the second disjunct was mine, not theirs |

### 7.2 Errors of attribution and status

Two theorems were attributed to the wrong authors and two conjectures were carried in a theorem column. One entry
was circular: a singularity theorem cited as evidence for the censorship conjecture that the theorem *requires as
input* to say anything about black holes.

### 7.3 The recurring failure

Seven instances of one class: a conclusion drawn from a comparison that was not licensed. The arithmetic was correct
in every case. The warrant was not.

---

## Part VIII · The finish line, located

The defect of one cell is not an open-ended uncertainty. Seven propositions were enumerated, any one of which would
close the index; four were examined against the literature; and the residue is a single named conjecture.

| proposition | verdict |
|---|---|
| X ≥ 1 → U ≥ 1 — Lorentz violation costs unitarity | **refuted.** Eling, Foster, Jacobson and Wall distinguish the ordinary from the generalised second law and state that the ordinary one should remain valid in Lorentz-violating theories. The chain is severed at its second link by the authors of its first. |
| U ≥ 1 → IC = 2 — non-unitarity signals | **refuted.** The U = 1 rung is occupied: Nikolić shows high Hamiltonian degeneracy permits local, energy-momentum-conserving non-unitary evolution, and computes the Lindblad operators explicitly. |
| NEC ≥ 3 → X ≥ 1 — exotic matter needs a preferred frame | **refuted.** Buniy's theorem is scoped to causal, Lorentz-invariant theories; inside that scope the conclusion is instability, with no superluminal branch. |
| NEC ≥ 3 → U ≥ 1 — exotic matter costs unitarity | **conditional.** Proven in flat space for any reasonable QFT. In curved spacetime it rests on the self-consistent achronal ANEC (Graham–Olum 2007), which is a conjecture. |

> **The index closes if and only if the self-consistent achronal ANEC holds in four dimensions.** A holographic
> counterexample exists (Ishibashi, Maeda and Mefford 2019), but the same group's later work identifies it as a
> conformal-frame artefact — the ANEC is not conformally invariant, so a conformal transformation can magnify a
> local violation — and supplies the repair, a conformally invariant ANEC. In odd boundary dimensions the repair is
> clean; in four dimensions the conformal anomaly leaves a weighted lower bound, which is exactly the quantity that
> would settle this.

Six proofs, indexed by geometry, field content, coupling, curvature and backreaction, cover **{CV['covered']} of
{CV['cases']}** cases; the {CV['uncovered']} uncovered are all curved with interacting or non-minimally coupled
fields, and the wormhole case is among them. The count is framing-dependent — it ranges from 6 to 72 across
reasonable models — but the *fraction* is invariant under the number of axes and moves only with how generously two
specific results are read.

![Coverage]({FIG}f6_2.png)

*Figure 6.2. What each ANEC proof covers, and what moves the fraction left open.*

**Every curved-space proof crosses at the same place** — free, minimally coupled fields — just as every path from
source to target in Λ₉ crosses at **q**, the unique articulation point separating the two halves of the lattice.
Extending any single proof relaxes one pin and leaves the other.

---

## Part IX · Open

| item | state |
|---|---|
| the 4d weighted ANEC bound | the quantity that decides the defect; Iizuka–Ishibashi–Maeda, JHEP 10 (2020) 106 |
| profile → lattice for seven of nine coordinates | no demonstrated action on Λ |
| Λ₁₂, Λ₁₃ closure under parastatistics | ambient box exceeds the sweep limit |
| the two halves | the composition graph moves cells within a lattice; the violation index between lattices; no map joins them |
| P4, P6, P7 | unexamined; two are pure disjuncts of theorems already used |
| a name for the joint-square condition | the literature supplies Helly numbers but no theorem for this system |

---

## Appendix A · Equations

### A.1 The operator

**(1)** Âᵢ(X) = {{ xᵢ : x ∈ X }} — value sets

**(2)** φ̂ᵢⱼ(v) = max{{ xᵢ : x ∈ X, xⱼ ≤ v }} — monotone upper envelope; a staircase function, non-decreasing in v

**(3)** R(X) = {{ x ∈ ∏ᵢ Âᵢ(X) : xᵢ ≤ φ̂ᵢⱼ(xⱼ) ∀ i ≠ j }} — the minimal network of the binary constraint system

**(4)** E(X) = |R(X)| − |X| ≥ 0 — the closure defect

**(5)** X ⊆ BPC(X) ⊆ R(X), BPC(X) = {{ x : (xᵢ, xⱼ) ∈ projᵢⱼ(X) ∀ i < j }}

### A.2 The lattice Λ

**(6)** 1 ≤ n ≤ n_max — principal quantum number
**(7)** 0 ≤ ℓ ≤ n − 1 — from the hydrogenic radial solution, n = n_r + ℓ + 1, n_r ≥ 0
**(8)** 1 ≤ k ≤ 4ℓ + 2 — Pauli exclusion
**(9)** 0 ≤ q ≤ k — counting
**(10)** 0 ≤ f ≤ e − 1 — the target shell
**(11)** 0 ≤ g ≤ min(4f + 2, q)
**(12)** 0 ≤ 2S ≤ k — vector coupling

### A.3 The tower

**(13)** 0 ≤ 2S′ ≤ g — axis 9
**(14)** 2S′ ≤ v ≤ g — axis 10, seniority
**(15)** 0 ≤ 2J_c ≤ φ̂(k) — axis 11
**(16)** |2J_c − 2f| ≤ 2K ≤ 2J_c + 2f (step 2) — axis 12, the *exact* triangle; the lattice admits the loose form
**(17)** |2J − 2K| ≤ 1 — axis 13

### A.4 Exactness

**(18)** density(axis) = Σ_parents |exact fibre| ÷ Σ_parents |admissible fibre|

### A.5 Transit

**(19)** src(c) = (n, ℓ, k, 2S), tgt(c) = (e, f, g, 2S′); c composes iff tgt(c) is a legal source
**(20)** |E(L(Q))| = Σ_v deg⁻(v) × deg⁺(v)
**(21)** Sq(c) = {{ (i, sᵢ, j, sⱼ) : c + sᵢeᵢ, c + sⱼeⱼ, c + sᵢeᵢ + sⱼeⱼ ∈ Λ₉ }}
**(22)** a molecule {{c₁, …, c_m}} may circuit ⟺ ∩ₜ Sq(cₜ) ≠ ∅

### A.6 The violation index

**(23)** I_V = ∮(ρ + p_r) dV — the volume-integral quantifier grading the NEC axis

**(24)** NEC ≥ 3 ⟹ (¬U ∨ X ≥ 1) — the two-payer branch; composed with the IC route it is irreducibly ternary, and
is the sole cause of the defect

**(25)** capacity(ℓ) = m(4ℓ + 2) — parastatistics of order m; m = 1 is fermionic

**(26)** 2 ≤ S_CHSH ≤ 2√2 ≤ 4 — local, Tsirelson and algebraic bounds

**(27)** ⟨T_kk⟩ ≥ (ℏ/2π) S″_out — the quantum null energy condition; a bound, not a forcing edge

**(28)** {V2['defect']} = 1 × {V2['multiplicity']} — core times multiplicity, exact

### A.7 Order and measure

**(29)** x ≤ y ⟺ xᵢ ≤ yᵢ ∀ i — componentwise order; {O['comparable_pct']:.1f}% of Λ₈ pairs are comparable

**(30)** a measure μ is *faithful* to the order iff x < y ⟹ μ(x) ≠ μ(y) — the Coulomb measure is unfaithful on
{O['samen_pct']:.1f}% of ordered pairs

---

## Appendix B · References and sources

**Access grades.** Under 0.2 every source carries the level at which it was consulted. **[F]** full text read.
**[A]** abstract or published summary. **[S]** secondary — reached through a review or citing work.
**[B]** blocked.

### B.1 Constraint satisfaction, consistency and closure

- Freuder, E. C. (1982). A sufficient condition for backtrack-free search. *Journal of the ACM* 29(1), 24–32. **[S]**
- Montanari, U. (1974). Networks of constraints. *Information Sciences* 7, 95–132. **[S]**
- Mackworth, A. K. (1977). Consistency in networks of relations. *Artificial Intelligence* 8(1), 99–118. **[S]**
- Dechter, R. (1992). From local to global consistency. *Artificial Intelligence* 55(1), 87–107. **[S]**
- van Beek, P. & Dechter, R. (1995). On the minimality and global consistency of row-convex constraint networks. *JACM* 42(3), 543–561. **[S]**
- van Beek, P. & Dechter, R. (1997). Constraint tightness and looseness versus local and global consistency. *JACM* 44(4), 549–566. **[S]**
- Jeavons, P., Cohen, D. & Cooper, M. C. (1998). Constraints, consistency and closure. *Artificial Intelligence* 101(1–2), 251–265. **[S]**
- Zhang, Y. & Freuder, E. C. (2008). Properties of tree convex constraints. *Artificial Intelligence* 172(12–13), 1605–1612. **[A]**
- Cooper, M. C., Jeavons, P. G. & Salamon, A. Z. (2010). Generalizing constraint satisfaction on trees. *Artificial Intelligence* 174, 570–584. **[A]**
- Brylawski, T. (1973). The lattice of integer partitions. *Discrete Mathematics* 6(3), 201–219. **[S]**
- Helly, E. (1923). Über Mengen konvexer Körper mit gemeinschaftlichen Punkten. *Jahresbericht der DMV* 32, 175–176. **[S]**

### B.2 Atomic structure

- Racah, G. (1943). Theory of complex spectra III. *Physical Review* 63, 367–382. **[S]**
- Condon, E. U. & Shortley, G. H. (1935). *The Theory of Atomic Spectra*. Cambridge University Press. **[S]**
- Janet, C. (1929). The left-step periodic table. **[S]**

### B.3 Energy conditions and wormholes

- Buniy, R. V., Hsu, S. D. H. & Murray, B. M. (2006). The null energy condition and instability. *Physical Review D* 74, 063518. **[F]**
- Visser, M., Kar, S. & Dadhich, N. (2003). Traversable wormholes with arbitrarily small energy condition violations. *PRL* 90, 201102. **[A]**
- Kar, S., Dadhich, N. & Visser, M. (2004). Quantifying energy condition violations in traversable wormholes. *Pramana* 63, 859–864. **[F]**
- Fewster, C. J. & Roman, T. A. (2005). On wormholes with arbitrarily small quantities of exotic matter. *PRD* 72, 044023. **[F]**
- Ford, L. H. & Roman, T. A. (1996). Quantum field theory constrains traversable wormhole geometries. *PRD* 53, 5496–5507. **[S]**
- Morris, M. S. & Thorne, K. S. (1988). Wormholes in spacetime. *American Journal of Physics* 56, 395–412. **[S]**
- Kontou, E.-A. & Sanders, K. (2020). Energy conditions in general relativity and quantum field theory. *CQG* 37, 193001. **[F]**
- Graham, N. & Olum, K. D. (2007). Achronal averaged null energy condition. *PRD* 76, 064001. **[F]**
- Kontou, E.-A. & Olum, K. D. (2015). Proof of the ANEC in a classical curved spacetime using a null-projected quantum inequality. arXiv:1507.00297. **[A]**
- Kelly, W. R. & Wall, A. C. (2014). Holographic proof of the averaged null energy condition. *PRD* 90, 106003. **[A]**
- Hartman, T., Kundu, S. & Tajdini, A. (2017). Averaged null energy condition from causality. *JHEP* 07, 066. **[F]**
- Wall, A. C. (2010). Proving the achronal ANEC from the generalized second law. arXiv:0910.5751. **[F]**
- Ishibashi, A., Maeda, K. & Mefford, E. (2019). Achronal ANEC, weak cosmic censorship, and AdS/CFT duality. *PRD* 100, 066008. **[F]**
- Iizuka, N., Ishibashi, A. & Maeda, K. (2020). Conformally invariant averaged null energy condition from AdS/CFT. *JHEP* 03, 161. **[A]**
- Iizuka, N., Ishibashi, A. & Maeda, K. (2020). The ANECs in even dimensional curved spacetimes from AdS/CFT duality. *JHEP* 10, 106. **[A]**
- Urban, D. & Olum, K. D. (2010). ANEC violation in a conformally flat spacetime. *PRD* 81, 024039. **[A]**
- Alcubierre, M. (1994). The warp drive. *CQG* 11, L73–L77. **[S]**
- Bobrick, A. & Martire, G. (2021). Introducing physical warp drives. *CQG* 38, 105009. **[F]**

### B.4 Causal structure, chronology and Lorentz violation

- Penrose, R. (1965). Gravitational collapse and space-time singularities. *PRL* 14, 57–59. **[S]**
- Landsman, K. (2022). Penrose's 1965 singularity theorem. *GRG* 54, 115. **[F]**
- Hawking, S. W. (1992). Chronology protection conjecture. *PRD* 46, 603–611. **[S]**
- Friedman, J. L. (2004). The Cauchy problem on spacetimes that are not globally hyperbolic. gr-qc/0401004. **[F]**
- Arefeva, I. Ya., Ishiwatari, T. & Volovich, I. V. (2009). Cauchy problem on non-globally hyperbolic spacetimes. arXiv:0903.0567. **[A]**
- Hořava, P. (2009). Quantum gravity at a Lifshitz point. *PRD* 79, 084008. **[S]**
- Jacobson, T. & Mattingly, D. (2001). Gravity with a dynamical preferred frame. *PRD* 64, 024028. **[S]**
- Berglund, P., Bhattacharyya, J. & Mattingly, D. (2013). Towards thermodynamics of universal horizons in Einstein-aether theory. *PRL* 110, 071301. **[F]**
- Colladay, D. & Kostelecký, V. A. (1998). Lorentz-violating extension of the standard model. *PRD* 58, 116002. **[F]**

### B.5 Quantum foundations

- Bell, J. S. (1964). On the Einstein Podolsky Rosen paradox. *Physics* 1, 195–200. **[S]**
- Tsirelson, B. S. (1980). Quantum generalizations of Bell's inequality. *LMP* 4, 93–100. **[S]**
- Popescu, S. & Rohrlich, D. (1994). Quantum nonlocality as an axiom. *Foundations of Physics* 24, 379–385. **[S]**
- Pawłowski, M. et al. (2009). Information causality as a physical principle. *Nature* 461, 1101–1104. **[A]**
- Wootters, W. K. & Zurek, W. H. (1982). A single quantum cannot be cloned. *Nature* 299, 802–803. **[S]**
- Polchinski, J. (1991). Weinberg's nonlinear quantum mechanics and the EPR paradox. *PRL* 66, 397–400. **[A]**
- Abrams, D. S. & Lloyd, S. (1998). Nonlinear quantum mechanics implies polynomial-time solution for NP-complete and #P problems. *PRL* 81, 3992–3995. **[F]**
- Simon, C., Bužek, V. & Gisin, N. (2001). No-signaling condition and quantum dynamics. *PRL* 87, 170405. **[A]**
- Soulas, A. (2025). A proof that no-signalling implies microcausality in QFT. *Foundations of Physics* 55, 22. **[A]**
- Sorkin, R. D. (1993). Impossible measurements on quantum fields. *Directions in General Relativity* vol. 2. **[S]**
- Rastegin, A. E. (2009). A note on general no-cloning theorem for black boxes. arXiv:0908.1668. **[F]**

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
- Glorioso, P. & Liu, H. (2016). The second law of thermodynamics from symmetry and unitarity. arXiv:1612.07705. **[A]**

### B.8 Measurements

- Abbott, B. P. et al. (2017). GW170817 and GRB 170817A. *ApJL* 848, L13. **[S]**
- Touboul, P. et al. (2022). MICROSCOPE final results. *PRL* 129, 121102. **[S]**
- Lamoreaux, S. K. (1997). Demonstration of the Casimir force in the 0.6 to 6 µm range. *PRL* 78, 5–8. **[S]**
- Hensen, B. et al. (2015). Loophole-free Bell inequality violation. *Nature* 526, 682–686. **[S]**

---

## Appendix C · Verification

Twenty-six numerical claims were re-audited against fresh computation with zero failures. Two propositions replaced
sampled claims with proofs (1.2 and 3.3). One error was found inside a correction — a parameter used with two
meanings in the same computation — caught only because the fermionic case failed to reproduce 13,585.

The document was then run against twenty-one structural audits covering lattice properties, equation reproduction,
internal consistency, undefined terms, encoding artefacts, coherence, attribution, figure coverage, distinctness,
scoping, antecedents, markup, dataset agreement, arithmetic, enumeration, fidelity, artifact measure,
reproducibility, sequence, projection and input. **All twenty-one pass.**

All figures are computed from cached datasets. The computation script, dataset, build script and audit script
accompany this paper.
"""

open('/mnt/user-data/outputs/Transitions.md','w').write(md)
print('written', len(md), 'chars')
