# THE MATHEMATICS OF THE LÖWDIN WORK

*Registers 1249–1357. Each object is stated with its provenance: what is standard
and whose it is, what is arithmetic, and what this work introduces.*

---

## The corridor — a system of linear inequalities

**The object.** Requiring an observed subshell g to have least ν against every
admissible rival r gives one inequality per rival,

> **a(√p_r − √p_g) < n_r − n_g**,  with p = n − ℓ − 1

whose solution is an interval with endpoints

> **L, U = Δn(√p_g + √p_r)/(p_g − p_r)**

**Standard.** Linear programming in one variable; the feasible set of a finite
system of linear inequalities in ℝ¹ is an interval. *Fourier 1826; Motzkin 1936.*

**This work.** *That the coefficients are node counts, so the endpoints lie in
ℚ(√ℕ) and take only nineteen distinct values across the periodic table.* And that
all 106 intervals are non-empty — the system is consistent.

**The closed form** for every ns/(n−1)d competition:

> **a_cross = (√(n−1) + √(n−4))/3**

*giving 0.5773503, 1.0000000, 1.2168450, 1.3938270 at n = 4, 5, 6, 7 — four exact
hits, and the 3 in the denominator is p_g − p_r, invariant across the table.*

## The staircase algebra of a closed index

**`A.staircls`** states that E(ℛ) = 0 iff the held set is an intersection of
monotone staircases. **A closed index is therefore a system of inequalities and
its cells are the lattice points satisfying them.**

**Read off Λ_PCA**, whose cells satisfy **L(s) ≤ d ≤ U(s)** with

> **L(s) = ⌊s/2⌋**  and  **U(s) = s + ⌊s/3⌋**

*both exact on s ∈ {0,1,2,3}.* **And off Λ_amp**, whose twenty cells satisfy the
single inequality **0 ≤ i ≤ ℓ**.

**This work.** *That the algebra of a closed index can be read back out of it as
floor functions — the staircases are not merely asserted to exist but written.*

## The Slater triangle, and a parity defect resolved

**Standard.** The multipole expansion of 1/r₁₂ gives, for a pair of subshells,
**F^k for k even up to 2min(ℓ,ℓ′)** and **G^k for k ≡ ℓ+ℓ′ (mod 2) from |ℓ−ℓ′| to
ℓ+ℓ′.** *Slater 1929; Condon & Shortley 1935; the angular factors are Racah's
(1942–1949).*

**The angular factor of G^k is the 3j symbol squared**, and for an s electron
against an ℓ electron the sole exchange integral has angular factor **exactly
1/(2ℓ+1)** — verified 1, 1/3, 1/5, 1/7 to machine precision.

**This work.** *That indexing on the multipole rank k gives E = 1 with the single
defect **F¹**, a term parity forbids — and that reindexing on position within
sequence closes it at E = 0.* **The rank's parity is fixed by the kind and the ℓ
pair, so rank is not a free coordinate.**

## The falsification of a selection rule

**The object.** Given the corridor at every element, a walk needs a rule for where
in each interval to place the carried value. **Eight rules were tested; seven give
106/106**, including uniformly random interior points on **200 of 200 seeds**. Only
"move to the farther endpoint" fails, at 74/106, because it can overshoot.

**This work.** *That the ordering data constrains only membership of the interval,
not position within it — so the eighteen resets landing on exact surds is a
property of one chosen rule and not of the table.* **A different rule reproduces
the periodic table with a disjoint trajectory and a going negative at five
elements.**

*Recorded because the surd trajectory was reported as a result before the
falsification was run, and the falsification withdrew it.*

## The necessity of state

**The object.** For each admissible subshell, set a to that subshell's own crossing
value and ask whether it is then least-ν. **104 of 106 steps admit two to four
self-consistent subshells** — the observed one is always among them, never uniquely
determined.

**This work.** *That the periodic table is not computable from a single atom's
configuration. It requires one number carried forward: the arithmetic supplies the
values, the walk supplies the selection.*

## The observability boundary

**The object.** Across eleven closed indexes, the quantity each closure cannot fix
was identified. **Nine of eleven are expectation values ⟨Ψ|Ô|Ψ⟩.** The exception is
**Λ_cross**, whose value is a node count needing no measurement — **and it is the
only index with no statistics language.**

> **An index closes when its cells are enumerable. What it cannot supply is exactly
> what requires an operator.**

**This work.** *That the compendium's own language test detects this: the
statistics language is silent precisely where no observation is needed.* **One
confirming instance; the prediction is falsifiable and has been tested once.**

## Λ_spectra's closure, and what the limit leaves

**The object.** The index runs to the LAST AVAILABLE SPECIES and stops. Λ is
complete at 976 because its coordinates are bounded by the physics; Λ_spectra is
infinite unless capped, and *all cappings are closed when complete*.

Indexing every subshell any atom holds, (n, ℓ, k) over the observed ground
configurations: **98 cells, E = 58**. Of those 58, **38 require more electrons
than any atom has** — 6f¹ through 6f¹⁴ and beyond, needing Z past the table.
Past the limit, not defects. Applying the limit:

*Corrected at register 1426: the split was first reported as 47 / 11, using
`ground.py`'s own edge of Z = 108 as the limit while the synthesised table runs
to 118. The nine cells between — 6d⁷–6d¹⁰ and 7p²–7p⁶ — are real elements, not
absences. The eleven named exceptions below are unaffected; only the count of
beyond-limit cells was wrong.*

> **E = 11, and every cell is named.**

| absent | Madelung predicts at | observed |
|---|---|---|
| 3d⁴ · 3d⁹ | Cr 24 · Cu 29 | 3d⁵ · 3d¹⁰ |
| 4d³ · 4d⁶ · 4d⁹ | Nb 41 · Ru 44 · Ag 47 | 4d⁴ · 4d⁷ · 4d¹⁰ |
| 4f² · 4f⁸ | Ce 58 · Gd 64 | 4f¹ · 4f⁷ |
| 5d⁸ | Pt 78 | 5d⁹ |
| 5f¹ · 5f⁵ · 5f⁸ | Ac 89 · Np 93 · Cm 96 | 5f⁰ · 5f⁴ · 5f⁷ |

*The Madelung exceptions, recovered as closure defects rather than looked up —
E.nuclide's shape, a defect whose every missing cell can be named.*

**This work — rival = donor iff the donor is not full.** Twelve walk steps have a
subshell empty as another fills. A subshell at capacity has nowhere to put an
electron, so it is not Pauli-admissible and cannot be a rival in anyone's bracket,
including its own. An s shell holds 2 and is full when it donates:

| donor | occupancy before | binding rival |
|---|---|---|
| 4s, 5s, 6s (Cr, Cu, Nb, Ru, Pt) | **2, full** | 4p, 5p, 6p |
| 5s (Pd) | **1, partial** | 5s |
| 5d, 6d, 7p (Pr, Tb, Pa, Pu, Bk, Rf) | partial | itself |

**Holds 12 of 12, with no fitted term.** *Pd is its own control: the only s donor
that is not full, and it sits with the d and f donors. Were the rule about angular
momentum it would sit with Cr.* The anomalous steps differ from ordinary ones in
WHICH RIVALS EXIST, and that is fixed by occupancy — which ν already carries in q.
Registers 1395–1398.

## Attributions

**The ⅔ scaling.** *Thomas–Fermi's.* The quadratic in nuclear charge along an
isoelectronic sequence is **Krug & von Lilienfeld, arXiv:2406.18416 (2024)**,
fitted on Z = 1–86. **Carcassés & González, Phys. Rev. A 80 (2009) 024502**, give
E_ioniz = Z²N^(−2/3)g(N/Z) and flag that it fails for neutrals — the same domain
this work's residuals bow in.

**Configuration crossings along isoelectronic sequences** are a computed object:
**Berengut et al., arXiv:1204.0603** locate the 6p–5f crossing in the thallium
sequence by Dirac–Fock.

**The node theorem**, **Pauli's exclusion principle** and the **centrifugal term
ℓ(ℓ+1)** are standard and this work introduces none of them.

**Seaton's ratio** δ₂/δ₀ = −ℓ(ℓ+1)/3 is **Seaton's**; *the domain restriction to
p = 0 is this work's.*

**Slater's rules and integrals** are Slater's; *the observation that the count of
discarded exchange integrals equals the count of bracket failures is this work's.*

---

## What this work introduces, in one list

| object | |
|---|---|
| **the corridor** | 106 consistent linear inequalities with node-count coefficients |
| **the nineteen surds** | the complete set of endpoints across the table |
| **a_cross = (√(n−1)+√(n−4))/3** | closed form for the ns/(n−1)d family |
| **the staircase algebra** | ⌊s/2⌋ ≤ d ≤ s + ⌊s/3⌋, read out of a closed index |
| **the sequence-index fix** | rank parity is not a free coordinate |
| **the selection-rule falsification** | the corridor is forced, the path is not |
| **the necessity of state** | 104 of 106 steps ambiguous without memory |
| **the observability boundary** | closure enumerates; observation values |
| **the singleton-output rule** | an index is closed when its reading is unique |
| **the domain prohibition** | no parameter of this work is universal, so no pooled fit across regions is admissible |
| **the limit** | Λ_spectra closes at the last available species; E = 11, all named |
| **rival = donor iff not full** | the twelve anomalous steps, from Pauli alone |

---

# The Löwdin indexes — Λ_law and Λ_const

*Owed since register 1296; written at register 1571. Nothing here answers
Löwdin's challenge — the amplitude law remains three fitted numbers.*

## Λ_law — seven laws on (law, carrier). E = 0.

An arbitrary ordering gave E = 7. Across all 7! x 4! = **120,960 orderings** the
defect runs 0 to 21, and **288 reach zero.**

**The closing carrier order is u < p < l - l_core < Z - T**, monotone in **how
LOCAL the variable is**: u is the whole atom, p counts one l's shells,
l - l_core compares two angular momenta, Z - T is one distance to one threshold.
Two laws sit on u, three on p, one on each of the others.

The held cells form a **staircase**, which by `A.staircls` is exactly the
condition for E(R) = 0.

**What only this index contributes: THE CARRIER.** Fitting a law in the wrong
carrier is what took the l-spread from a spurious r2 of 0.868 to a real 0.356.

## Lambda_const — fourteen constants on (role, carrier). E = 0 at 2 of 576.

Role order **exponent < centre < width < scale**. Standing: three fitted, six
measured, five derived or attributed.

**Every CENTRE is a small integer or half-integer** - 2 for the free shells, 2
for the gate, -1.5 for the switch, 2.5 for the l-validity, u0 = 4. **No SCALE
is.** The role axis orders by how much physics a number has absorbed.

**beta = 2/3 is load-bearing**: the only constant of arity three, in the
amplitude, the exponent and the validity, **and the one that is attributed.**

### The refusal, which is the more useful half

**`standing` cannot be a coordinate.** With attributed/derived/measured/fitted
on an axis the index closes at NO ordering; without it, at once.

> **An index whose coordinates mix the OBJECT with the OBSERVER cannot close,
> because the observer's axis has no order the object respects.**

The same fault is `origin` in Lambda_var, `kind` in Lambda_phys and `state` in
Lambda_ladder - four occurrences of one mistake, stated here as a rule.
