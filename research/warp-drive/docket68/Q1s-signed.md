# Q-1s — the signed / complex entropy of a quasi-probability (DOCKET 68). Not seated.

Instrument: `signed.py` (stdlib + numpy + sympy; z3-solver for § 4b, pip-installed and not vendored -- without it
the six z3 obligations are printed SKIPPED and not counted). `python3 signed.py` prints every table below as data;
`--selftest` runs **86 checks: 77 counted, all pass, 18 of them controls (cases built to fail, which do fail); 9 more
are printed STRUCTURAL** (they cannot fail, so they are neither counted nor cited as evidence); `--json` gives the
numbers. *Wave 4 first-said record:* "66 checks, 0 failed: 13 controls ... 2 STRUCTURAL"; wave 4 (R3-alone) added 20
checks for § 4b-4c and relabelled five STRUCTURAL (V2-0 problem 5 and the same test applied to the rest). Nothing here edits `measure.py`
(A3) or the board. `measure.py` and `tools/cypher.py` are **imported, never copied**.

**M's words (CHARTER.md, 2026-10-03), verbatim:** "we can define this. We plot it. With all its inverses, and
reflections on the same multi-axis graph and the positive values will triangulate the negative values".

Status words: **COMPUTED** (run by `signed.py`), **EXACT** (sympy, symbolic or algebraic), **READ** (at source, with
arXiv id, version and page), **DERIVED** (by hand, the step shown, not machine-checked), **NAMED-NOT-READ**, **OPEN**.

---

## 1. Defining it: H = −Σ p Log p for p with Σp = 1 and some p < 0

Under **H-PRINCIPAL** (principal branch, arg of a negative number = +π; the convention of Cerf–Hertz–Van Herstraeten
2310.19296v1 p.5):

- **Re H = −Σ p ln|p|.** It is the same on every branch, by definition: k enters only the imaginary part (the grid
  check, identical to 1e-12 across 25 branches, is printed STRUCTURAL in wave 4).
- **Im H = πN**, where N is the total negative weight. COMPUTED.
- **M = ln Σ|p|** (the mana of Veitch et al. 1307.7171v1, Def. 12 p.11) and **N = (Σ|p| − 1)/2**. COMPUTED.
- **The example.** p = (1.5, −0.5) gives H = **−0.954771 + 1.570796 i nats** (Re H = −1.377444 bits), N = 0.5,
  M = ln 2. The charter wrote "−0.95" and the task "−0.9548": both agree with this value.

**Branches.** The task asked for "all its inverses and reflections"; how that phrase is read here is **H-READING-M**.
- **Per-entry branches.** Put entry i on branch k_i, so that Log p_i = ln|p_i| + i(arg p_i + 2πk_i). Then H gains
  **−2πi k_i p_i**. This is **elementary**: a one-line consequence of the definition of Log_k (V2-0 problem 8). It is
  kept because it is the basis of discrepancy D1 against the charter.
  - For a negative entry that is +2πi k_i|p_i|. For p = (1.5, −0.5), taking k = 1 on the negative entry moves Im H
    by **+π, not 2π**. COMPUTED.
  - Positive entries have branches too: each unit of k moves Im H by −2πp_i.
- **The set of Im H values** is the lattice πN + Σ 2πk_i(−p_i). For (1.5, −0.5) it is {π/2 + mπ : m ∈ ℤ}, and every
  member is reached.
- **Uniform branch.** If every entry takes the same k, H moves by exactly **−2πik**, because Σp = 1 (one line;
  the computed k = ±1, ±2 check is printed STRUCTURAL in wave 4).
- **Reflection.** The conjugate, with arg = −π and Im → −Im, is itself one of the branches: put k = −1 on every
  negative entry and Im H becomes πN − 2πN = −πN.
- **The inverse axis** −Log p_i (the surprisal) has real part −ln|p_i| and imaginary part −arg p_i.
- **The exponential.** |e^H| = e^{Re H} = 0.384900 on every branch. The phase of e^H changes under a per-entry branch
  (for (1.5, −0.5), k = 1 on the negative entry flips its sign; this is a control) and does not change under a uniform
  branch. So the remark in 2310.19296v1 p.13 fn.7, that the branch choice may not matter once one exponentiates,
  holds for a uniform branch shift and not for per-entry choices. The footnote is itself hedged; this is a precision
  about it, not a discrepancy.

**Multi-axis table, p = (1.5, −0.5)** (COMPUTED; `multiaxis_table`). The data for M's "same multi-axis graph":

| i | p | ln\|p\| | arg (principal / reflected) | −p ln\|p\| (Re) | −p·arg (Im) | −Log p (re, im) | Im step per unit k_i |
|---|---|---|---|---|---|---|---|
| 0 | 1.5 | 0.405465 | 0 / 0 | −0.608198 | 0 | (−0.405465, 0) | −9.424778 (= −3π) |
| 1 | −0.5 | −0.693147 | π / −π | −0.346574 | 1.570796 | (0.693147, −π) | +3.141593 (= +π) |

**N-sweep, p = (1+N, −N)** (COMPUTED; `n_sweep`):

| N | Re H | Im H | reflected −Im H | M |
|---|---|---|---|---|
| 0 | 0 | 0 | 0 | 0 |
| 0.05 | −0.201016 | 0.157080 | −0.157080 | 0.095310 |
| 0.25 | −0.625503 | 0.785398 | −0.785398 | 0.405465 |
| 0.5 | −0.954771 | 1.570796 | −1.570796 | 0.693147 |
| 1.0 | −1.386294 | 3.141593 | −3.141593 | 1.098612 |
| 2.0 | −1.909543 | 6.283185 | −6.283185 | 1.609438 |

The full 25-row branch grid, giving Re H, Im H, |H|, arg H and e^H for each (k_pos, k_neg) ∈ [−2, 2]², is in the
report.

## 2. Independent products

Every identity below was COMPUTED on 400 random pairs of quasi-distributions and checked EXACT in sympy for
p = (1+a, −a), q = (1+b, −b).
- **Re H is additive.** Worst residual 3.1e-15; the sympy residual is exactly 0.
  - **Control:** with Σp = 2 the identity fails, with a residual of 2.4250. Additivity comes from normalisation.
    Cerf et al. (2310.19296v1 p.6) note the same for the continuous case.
- **Im H = π(N_p P_q + P_p N_q)**, where P = 1 + N is the positive mass. Worst residual 7.1e-15; sympy gives exactly 0.
  - Im H is therefore **superadditive, by exactly 2πN_pN_q** (sympy: excess 2ab).
  - **Control:** the hypothesis "Im H additive" is rejected; the smallest excess over the samples is 2.3e-2.
- **M is additive** (worst residual 5.6e-16; sympy 0). **M = 0 if and only if no entry is negative.**
- **N = (Σ|p| − 1)/2**: definitional (Σ|p| = P + N, Σp = P − N = 1); the residual check (2.7e-15) is STRUCTURAL.

## 3. Where Re H is negative, and its exact range

**The range.** For n entries with negativity N > 0, write P = 1 + N. DERIVED and COMPUTED:

    min Re H = −P ln P + N ln(N/(n−1))      (one positive entry; the negative weight spread evenly over n−1 entries)
    max Re H = −P ln(P/(n−1)) + N ln N      (n−1 equal positive entries; one negative entry)

The derivation is short. −x ln x is concave on the positive part and |x| ln|x| is convex on the negative part, so each
bound is a majorisation extreme. Three computed checks support it:
- both bounds are attained by the extremal vectors;
- 4,000 random quasi-distributions never leave the range (worst excursion 8.9e-16; this check can fail);
- **control:** lowering the maximum by 1e-3 is violated by its own extremal vector.

**Consequences.** The first two are COMPUTED and EXACT; the third follows from the formula for min Re H.
1. **For n = 2 every quasi-distribution has Re H < 0**, because the range collapses to a single value:
   −(1+N)ln(1+N) + N ln N.
2. **For n ≥ 3, Re H < 0 is never forced.** max Re H is convex in N, with derivative ln((n−1)N/(1+N)). Its smallest
   value over N is **exactly ln(n−2), reached at N = 1/(n−2)**. A golden-section search agrees with this closed form to
   1e-9 for n = 3, 4, 5, 8, 16. For n = 3 that smallest value is 0, reached only at N = 1, where p = (1, 1, −1) has
   Re H = 0.
3. **min Re H < 0 for every n and every N > 0.** Any negativity at all leaves room for a negative Re H, and min Re H
   → −∞ as N → ∞.
4. **(Added by Q1s-integrate, 2026-10-03.) For n ≥ 3, max Re H has no ceiling.** It grows without bound in N:
   for n = 3, (P/2, P/2, −N) gives Re H = 4.2736 nats at N = 10 and 64.3977 at N = 100, against ln 3 = 1.0986; for
   n = 5 it already exceeds ln 5 at N = 2 (2.2493). COMPUTED in `measure.holder_ceiling` on this file's extremal
   vectors. So Shannon's ceiling ln n, and with it "I bits need 2^I states", does not hold for Re H.

**Range table** (nats, COMPUTED; `range_table` gives all 25 rows):

| n | N = 0.05 | N = 0.5 | N = 1 | N = 2 |
|---|---|---|---|---|
| 2 | [−0.2010, −0.2010] | [−0.9548, −0.9548] | [−1.3863, −1.3863] | [−1.9095, −1.9095] |
| 3 | [−0.2357, +0.5268] | [−1.3013, +0.0850] | [−2.0794, 0.0000] | [−3.2958, +0.1699] |
| 5 | [−0.2703, +1.2546] | [−1.6479, +1.1247] | [−2.7726, +1.3863] | [−4.6821, +2.2493] |
| 8 | [−0.2983, +1.8422] | [−1.9277, +1.9641] | [−3.3322, +2.5055] | [−5.8014, +3.9282] |

At N → 0⁺ the maximum tends to ln(n−1), not ln n, because one slot must hold the negative entry. At N = 0 the range
is Shannon's [0, ln n].

## 4. Baez–Fritz–Leinster's axioms on signed measures; uniqueness

**BFL Theorem 2** (1106.1791v3 p.4, READ) concerns **FinProb**, whose measures are non-negative (p.3). Its hypotheses
are: functorial, convex-linear, continuous, and taking values in [0, ∞). Here those axioms are restated verbatim on
**FinSigned** (H-FINSIGNED: signed measures with total 1, measure-preserving functions, λ ∈ [0, 1]). In each case
F(f: p → q) = X(p) − X(q).

| axiom | Re H | M | Im H = πN |
|---|---|---|---|
| functoriality | STRUCTURAL: holds for any difference of a state function; cannot fail | STRUCTURAL | STRUCTURAL |
| convex linearity | **holds** (null space, below) | **fails**: λ = ½, (1.5, −0.5) → pt ⊕ (½, ½) → pt gives 0.405465 vs 0.346574 | **holds** |
| continuity (an entry crossing 0) | holds (jump 2e-8) | holds | holds (control: count_neg and Hartley jump) |
| codomain [0, ∞) | **fails**: crush (1.5, −0.5) → pt gives F = −0.954771; merge (1.6, −0.3, −0.3) → (1.6, −0.6) gives F = −0.6 ln 2 with N unchanged; random minimum −3.56 | holds (Σ\|p\| cannot grow under pushforward; random minimum −2e-16) | holds (triangle inequality; random minimum −4e-16) |

**The lawful family inside a 12-functional dictionary** (H-DICTIONARY; COMPUTED as SVD null spaces over 500 random
morphism pairs and 300 random products). The dictionary is h₊ = −Σ_{p>0} p ln p, J = Σ_{p<0}|p| ln|p| (so
Re H = h₊ + J), N, M, N², Σp², Σp|p|, N ln N, P ln P, count of negatives, Hartley, and signed Rényi-2 (−ln Σp²).
- **Convex-linear (BFL-sense):** span{**Re H**, **N**}. Of the pair (h₊, J), only the sum h₊ + J survives, so the
  |p|-weighted h₊ − J is excluded.
- **Product-additive:** span{Re H, M, Hartley, signed Rényi-2}. N is not in it.
- **Both:** **Re H alone.**
- **With BFL's codomain kept as well:** consider the family a·Re H + b·N. The merge-negatives morphism leaves N
  unchanged and gives F_{Re H} < 0, so a ≤ 0. Probability morphisms give F_{Re H} ≥ 0, so a ≥ 0. Hence a = 0, and only
  **b·πN (b ≥ 0) survives — and it vanishes on every probability measure.** Inside this dictionary, **no functional
  extends Shannon and keeps all four BFL hypotheses on signed measures.** **Inside H-DICTIONARY, and (§ 4b) inside
  H-SEPARABLE**, extending Shannon to signed measures forces dropping non-negativity of information loss: a
  measure-preserving map can *raise* Re H. **The general case is OPEN**: a measure such as (1.6, −0.3, −0.3) has no
  convex decomposition with λ ∈ [0, 1] and blocks of total 1 (computed: `convex_decompositions` returns none), so
  convex linearity does not constrain a non-separable X there, and the dictionary argument does not extend by itself.
  *Wave 3 first said* "Extending Shannon to signed measures forces dropping non-negativity of information loss", an
  impossibility stated without the qualifier the previous sentence carried (V2-0 problem 3).
- **M among functions of N alone.** If f(N) is product-additive then, since 1 + 2N is multiplicative under products,
  f = c·ln(1 + 2N) = c·M. This is DERIVED from Cauchy's logarithmic equation under continuity. The equation's general
  solution is READ as cited in 2410.15976v5 p.10, Lemma A.1, which cites Aczél–Dhombres.

**Brandenburger–La Mura** (2410.15976v5, READ pp.2–4, 9–11). Their Theorem 1 (p.4) uses Axioms 0 (real values),
2′ (continuity), 3 (calibration), 4 (extensivity) and 5′ (a mean-value rule weighted by **|w|**). It gives signed Rényi
of order α (α ≠ 1) and excludes the |p|-weighted "signed Shannon" of their eq. (11). The checks run here (COMPUTED):
- **Their Example 1 reproduced:** −2 and −12 against −4 (p.4).
- **Re H (p-weighted) on the same measures:** −2 + −2 = **−4**, which is extensive. It is also extensive on random
  measures (residual 1.1e-13) and passes calibration (1 bit). Their exclusion therefore concerns the |p|-weighted
  form, not Re H. Both statements hold; this is a note on scope.
- **Re H fails 5′.** Take P = (−0.5), Q = (1.5): the union gives −1.377444, the |w|-mean −0.377444 (control).
  - **Re H is not a signed Rényi entropy for any α in (0.05, 6):** the closest is α = 1.95, still 0.416 bits off.
    This agrees with their theorem.
- **Re H satisfies the same rule with signed weights w in place of |w|.** On the example the signed-weight mean is
  −1.377444, equal to the union; on random splits the worst residual is 5e-14. With signed weights, the affine-g term
  e·Σp_i/Σp_i cancels exactly, whereas their |w| version keeps it (their Lemma A.3).
- **The exponential branch of the signed-weight rule fails their Axiom 0.** On a measure with Σp = 1 the argument
  Σ sign(p)|p|^α is ≤ 0. Values: α = 0.1: −0.794; 0.5: −0.586; 0.9: −0.134; 1.1: −0.067; 2: −0.5; 3: −0.778; 5: −0.949.
  A limit argument covers every α ≠ 1 (DERIVED): for α > 1 use many small positive entries; for α < 1 use many small
  negative entries.
- **Their eq. (45)**, the renormalised α = 1 case, equals −M in bits. This is STRUCTURAL: two formulas that agree by
  definition.

**What is shown about uniqueness, exactly:**
- (a) Under BFL's axioms extended verbatim, inside the dictionary **and over every continuous separable functional
  (§ 4b)**, the lawful family does **not** contain Re H; it is {b·πN}, which vanishes on probabilities.
- (b) Drop the codomain and it is span{Re H, N} -- inside the dictionary, and over every continuous separable
  functional (§ 4b, derived and machine-checked). Add product additivity and it is Re H alone.
- (c) **(Re H, M) is not forced** by BFL-type axioms, because M is not convex-linear. **Within H-DICTIONARY, or among
  continuous functions of N alone**, M is the product-additive member that vanishes on probabilities. Outside those
  it is not unique: g₃(p) = ln(Σ|p|³ / |Σp³|) is product-additive (residual 1.1e-14), is 0 on every probability vector,
  and gives g₃(1.5, −0.5) = 0.0741 against M = ln 2 (COMPUTED, `m_uniqueness_counterexample`; V2-0 problem 4). M is the
  exponent-1 member of that family, ln(Σ|p| / |Σp|). g₃ is undefined where Σp³ = 0, so it is a counterexample to
  uniqueness, not a proposed measure. *Wave 3 first said* "M is **the** product-additive member that vanishes on
  probabilities".
- (d) In Brandenburger–La Mura's framework the selection turns on **one axiom**: with |w| in 5′ it is signed Rényi; with
  w in 5′ it is Re H. The second is **DERIVED-CONDITIONAL**: it follows their appendix proof (pp.10–11) step by step,
  carrying **H-RD** (the Rényi 1961 / Daróczy 1963 step is NAMED-NOT-READ) and the Lemma A.2 induction with signed
  weights. That induction needs an ordering whose partial sums never vanish: put the entries of the total's sign first.
  It is not machine-checked.
- (e) **Uniqueness over all continuous functionals:** derived for separable ones (§ 4b); CLAIMED-IN-LITERATURE under
  signed-weight recursivity (Kontsevich, § 4c); **OPEN over non-separable functionals under BFL's axioms.** *Wave 3
  first said* "Uniqueness over all continuous functionals is OPEN."
- (d′) The substance of (d) -- signed weights select Re H where |w|-weights exclude it -- is the same phenomenon as
  Kontsevich's: his (B) admits weights of either sign, and under it N is excluded (§ 4c). (d) is its form inside
  Brandenburger-La Mura's mean-value framework, not a new selection.

## 4b. Every continuous separable functional (wave 4, R3-alone; V2-1 problem 5)

**The claim.** Let F on FinSigned (H-FINSIGNED: signed measures of total 1, measure-preserving functions, λ ∈ [0, 1])
be functorial, convex-linear and continuous, and suppose X(p) := F(!_p) is **separable**: X(p) = Σᵢ g(pᵢ) with
g: ℝ → ℝ continuous (**H-SEPARABLE**). Then **X = c·Re H + b·N** for constants c, b, and conversely both Re H and N
satisfy the three axioms. `signed.py` § (4b) carries every step; the status of each is stated.

| step | statement | status |
|---|---|---|
| (0) | F(id) = F(id ∘ id) = 2F(id), so F(id) = 0; and since !_p = !_q ∘ f, F(f: p → q) = X(p) − X(q) (BFL 1106.1791v3 p.9 eq. 8, READ) | STRUCTURAL: holds for any functor into (ℝ, +); not counted |
| (1) | convex linearity applied to !_p and !_q: X(λp ⊕ (1−λ)q) = X(λ, 1−λ) + λX(p) + (1−λ)X(q), λ ∈ [0, 1] (BFL p.4 eq. 2, READ) | STRUCTURAL: the axiom restated on terminal maps |
| (2) | g(1) = X(pt) = 0; then (1) at λ = 1 with p = pt, q = (s, 1−s) gives g(0) = 0 | **Z3** (`z3_g0`: negation unsat) |
| (3) | put φ_λ(x) = g(λx) − λg(x). Instances of (1) for (x, y, 1−x−y) ⊕ pt and (x+y, 1−x−y) ⊕ pt, subtracted, give **φ_λ(x) + φ_λ(y) = φ_λ(x+y)** for all real x, y and λ ∈ (0, 1) | **Z3** (`z3_cauchy`: negation unsat over an uninterpreted g). Control: with the second instance dropped, z3 returns a countermodel |
| (4) | φ_λ continuous and additive ⇒ φ_λ(x) = A(λ)x | DERIVED (Cauchy's equation; READ as cited in 2410.15976v5 p.10, Lemma A.1, which cites Aczél–Dhombres; Kontsevich takes the same step for measurable ψ_λ, math/0008089v1 p.43) |
| (5) | on x > 0 put h = g/x: h(λx) = h(x) + B(λ) with B(λ) = A(λ)/λ = g(λ)/λ (as h(1) = 0); B(λμ) = B(λ) + B(μ) and B continuous ⇒ B = a ln λ; so g(x) = a·x ln x on (0, 1), and h(1) = h(x) + B(1/x) extends it to x > 1 | DERIVED (Cauchy on the half-line t = ln λ < 0) |
| (6) | on x < 0 put u(x) = h(x) − a ln\|x\|: u(λx) = u(x) for every λ ∈ (0, 1), and any two negatives are related by such a λ, so u = β is constant: g(x) = a·x ln\|x\| + βx | DERIVED (elementary) |
| (7) | Σᵢ g(pᵢ) = −a·Re H − β·N, i.e. **X = c·Re H + b·N** with c = −a, b = −β. The solution identity g(λx) − λg(x) = aλ ln λ·x holds on each sign | **SYMPY** (`sep_sympy`: residual 0 on both signs) |
| (8) | conversely, Re H is convex-linear (sympy residual exactly 0 on a sign pattern) and N is (λ, 1−λ ≥ 0 keep every sign, and N(λ, 1−λ) = 0; one line) | SYMPY / by hand |

**Guards** (PROOF-ASSISTANT.md). *Vacuity:* the premises are satisfiable by a non-zero member -- g = min(x, 0), i.e.
X = −N, satisfies every encoded instance **for all** λ ∈ [0, 1], x, y (z3: negation unsat), and g(−1) = −1 ≠ 0.
*Encoding drift:* the Python twin of the encoded instance has residual 2.7e-15 on Re H's g and 4.4e-16 on −N's, and
0.85 or more on g = x² (control). **Corroboration (COMPUTED):** in a 14-function separable basis (x ln|x|, x, x², x³,
x ln²|x|, |x|^1.5, |x|^2.5, on each sign) 400 random convex-linearity rows plus X(pt) = 0 leave a null space of
dimension 2, equal to span{Re H, N} (residuals 2.8e-13 and 3.9e-13); without the convex-linearity rows it has
dimension 13 (control). This rebuilds the FOR verifier's scratch check.

**Consequences, over every continuous separable functional (each checked):**
- **BFL's codomain kept ⇒ c = 0 and b ≥ 0.** A probability merge (½, ½) → pt has F = c ln 2 ≥ 0; the merge
  (1.6, −0.3, −0.3) → (1.6, −0.6) has F = −0.6 ln 2 · c with N unchanged; the crush (1.5, −0.5) → pt has
  F = −0.954771 c + 0.5 b. z3: the three constraints force c = 0, b ≥ 0 (negation unsat); with b > 0 they are
  satisfiable (vacuity); without the merge-negatives morphism c > 0 is consistent (control). So **no separable
  functional extends Shannon and keeps the codomain**: only b·N survives, and it vanishes on probabilities.
- **Shannon on FinProb does not fix b.** N vanishes on every probability measure, so "extends Shannon" leaves the b·N
  freedom open.
- **Product additivity ⇒ b = 0.** N(pq) − N(p) − N(q) = 2N_pN_q (sympy: 2ab for p = (1+a, −a), q = (1+b, −b)), while
  Re H is exactly additive (§ 2). So **Re H is the unique continuous separable functional that is functorial,
  convex-linear and product-additive on FinSigned** (up to c). This needs neither H-RD nor the Brandenburger-La Mura
  fork.

**Not claimed.** Nothing about non-separable functionals. Convex linearity (λ ∈ [0, 1], blocks of total 1) cannot
reach a **convex atom**, a signed measure with no split into two blocks whose totals lie in (0, 1). Every n = 2
signed measure is one (block totals 1 + N and −N), and so is (1.6, −0.3, −0.3). Over 2,000 random signed measures the
fraction with no decomposition is 1.0 at n = 2, 0.54 at n = 3, 0.37 at n = 4 and 0.25 at n = 5. H-SEPARABLE is the
named hypothesis that closes this gap here; without it, uniqueness under BFL's axioms is OPEN.

## 4c. Kontsevich's 1½-logarithm, READ at source; where Q-1s stands (wave 4; V2-0 problem 1)

READ through alphaXiv: **arXiv:math/0008089v1** (Elbaz-Vincent & Gangl, *On poly(ana)logs I*, with the appendix
*The 1½-logarithm* by M. Kontsevich, his unpublished note of 1995), pp.1-2, 10-11, 42-44; and **arXiv:1903.06961v3**
(Leinster, *Entropy modulo a prime*), pp.1-4, 8, 26-27. No 403.

**What the appendix states (p.42-44).**
- For a prime p, H_p(x) = Σ_{k<p} x^k/k on ℤ/p satisfies **(A)** H(1−x) = H(x), **(B)** H(x+y) = H(y) +
  (1−y)H(x/(1−y)) + yH(−x/y) for y ≠ 0, 1, and **(C)** xH(1/x) = −H(x). These are **proved** for H_p (p.42).
- p.43, verbatim in substance: *"Claim: there is only one (up to a scalar factor) nonzero continuous solution of
  equations (A), (B), (C) in maps from ℝ to itself. It is H_∞(x) = −(x log|x| + (1−x) log|1−x|)."*
- The argument given is a **cohomological sketch** for measurable H: φ(x, y) = (x+y)H(x/(x+y)), set to 0 when
  x + y = 0, is a symmetric, degree-1 homogeneous 2-cocycle of (ℝ, +); *"there are no non-trivial measurable
  cohomology classes in H²(ℝ, ℝ)"* (asserted, not proved there), so φ(x, y) = ψ(x) + ψ(y) − ψ(x+y); homogeneity
  makes ψ_λ(x) = ψ(λx) − λψ(x) additive, hence linear for measurable maps, and *"one can easily deduce"*
  ψ(x)/x = a log|x| + b. (C) is called irrelevant to the argument.
- p.44: the entropy of a variable with **probabilities** p₁ … p_k, the chain rule ("main identity"), the reduction
  by induction to the two-valued case, and the statement that the entropy so computed *"is well-defined iff
  functional equations (A) and (B) are satisfied"*, offered as easily checked.
- Elbaz-Vincent & Gangl (p.10, Prop. 2.13) cite the differentiable case as "well-known (cf. [22])", [22] being this
  note; p.10-11, Rem. 2.14, cite Aczél–Dhombres for locally integrable solutions of the fundamental equation on
  ]0, 1[. Cathelineau reached the same equation from Hilbert's third problem (p.2; NAMED-NOT-READ).
- Leinster (p.27): over ℝ the binary Shannon function is, up to scale, the only measurable solution of the fundamental
  equation with F(0) = F(1), and Shannon entropy of finite **real probability** distributions is characterised by
  measurability, symmetry and the chain rule (Lee 1964, NAMED-NOT-READ); Remark 9.6: symmetry is essential to that
  approach (F(π) = π also solves it). p.8: mod-p "probabilities" can be non-zero and sum to zero -- the analogue of
  a signed block of total 0.

**What it proves, exactly.** (A)-(C) for H_p on ℤ/p. **On ℝ it claims**, with a sketch whose two key steps are
asserted, that the binary functional equation (A)+(B)(+C) on **all of ℝ** -- x and y of any sign, so weights of either
sign -- has the unique continuous solution H_∞ up to scale. **H_∞(x) is exactly Re H of the two-entry signed measure
(x, 1−x)** (`kontsevich_checks`: Re H satisfies (A), (B), (C) on random reals, worst residuals 0, 4.4e-15, 1.3e-15).

**What it does not.**
- It gives no n-entry theorem for **signed** measures: p.44's reduction is written for probabilities. Carrying it to
  signed n-entry measures needs an order of grouping whose block totals never vanish (φ is *defined* 0 on a zero-total
  block), the ordering § 4(d) uses. Re H does satisfy the chain rule with signed outer weights (residual 2.7e-15,
  computed), but the source does not state the signed n-entry uniqueness.
- It does not use BFL's axioms. (B), with weights y and 1−y of any sign, is **stronger** than BFL's convex linearity,
  whose λ lies in [0, 1]. Computed control: N, which is convex-linear in BFL's sense, **fails (B)** (x = 0.5, y = −1:
  0.5 against 1.0) and fails the signed-weight chain rule (max residual 4.1). That is exactly why span{Re H, N} survives
  BFL's axioms (§ 4b) and only Re H survives Kontsevich's.
- It says nothing about the codomain [0, ∞), Im H, branches, N or M.
- It is a claim with a sketch, not a complete proof.

**Where Q-1s stands -- prior art cited, not hidden.**
- **The selection of Re H by signed-weight recursivity** -- the substance of fork § 4(d) -- **was claimed in 1995**
  (printed 2000/2002) by Kontsevich, as a cohomological sketch, with zero-total blocks excluded. OPEN 1 is restated
  accordingly: **CLAIMED-IN-LITERATURE** under chain rule (recursivity on ℝ), symmetry and continuity; **derived here**
  under BFL's convex-linear axioms for separable functionals (§ 4b); **OPEN** under BFL's axioms for non-separable ones.
- **2310.19296v1** (Cerf, Hertz, Van Herstraeten) holds the definition on the principal branch, Im ∝ negative volume,
  Re additive and Im superadditive -- for **continuous** Wigner functions. § 1-2's discrete forms are that definition's
  finite-set analogue, not a new definition.
- **What this file adds, as a floor and not a priority claim:** BFL's categorical axioms restated on FinSigned with the
  codomain's failure computed; the separable derivation c·Re H + b·N with its algebraic steps machine-checked; the
  computed contrast between BFL convex linearity (admits N) and signed recursivity (excludes N); the finite-set range of
  Re H (§ 3); the g₃ counterexample to M's uniqueness; the triangulation computations (an established principle, § 5).

## 5. M's triangulation, computed

The task asked whether positive values triangulate the negative ones. **Within one distribution**, the positive
entries fix only N (N = P − 1; STRUCTURAL). Where the negativity lies has to come from projections.

**Continuous case: filtered back-projection.** The method is the inverse Radon transform with a Ram-Lak kernel
(Lvovsky–Raymer quant-ph/0511044v2 eqs. 19–20 p.7, READ). The marginals are exact Born densities
pr(s, θ) = |Σ c_n e^{−inθ} ψ_n(s)|², so they are non-negative (minimum 1e-20). Results (COMPUTED, H-FBP):

| state | angles K | max\|W_rec − W\| | min (exact → reconstructed) | IoU of the region W < −0.02 |
|---|---|---|---|---|
| (\|0⟩+\|1⟩)/√2 | 180 | 1.0e-4 | −0.11332 → −0.11338 at (−0.5, 0) | 1.000 |
| (\|0⟩+\|1⟩)/√2 | 12 | 5.3e-3 | → −0.11339 | 1.000 |
| (\|0⟩+\|1⟩)/√2 | **2 (control)** | **0.230** | → −0.14014, displaced to (−0.45, 2.05) | **0.037**: fails, as it must |
| vacuum (W ≥ 0) | 180 | 1.0e-4 | min −7.9e-5 (non-negative within tolerance) | — |
| vacuum | **3 (control)** | 0.096 | **min −0.0683**: the non-negativity test fails, as it can | — |
| Fock \|1⟩ | 180 | 1.0e-4 | −1/π → −0.31839 at the origin | 1.000 |

**Finite-sample run.** With 72 angles × 20,000 sampled quadratures per angle, the 5×5 patch at the exact minimum
averages **−0.1056** against an exact −0.1133. The patch's spatial spread is 0.018, which is **not** a standard error.
This is one seeded run, so H-NOISELESS is relaxed only illustratively.

**Continuous complex Wigner entropy.** Two values READ at source are reproduced:
- vacuum Re h_c = 2.1447299 = ln π + 1 (2310.19296v1 eq. 49, p.8);
- Fock |1⟩ Im h_c = π·Vol₋ = 0.669353 against π(4e^{−1/2} − 2)/2 = 0.669352 (quant-ph/0406015v1 eq. 4.11, p.7).
- The other value computed for Fock |1⟩ is Re h_c = 2.695729. For (|0⟩+|1⟩)/√2: Re 2.235740, Im 0.219016.

**Discrete case: exact.** The positive marginals determine the negative entry exactly.
- **The rule.** Each line operator Q(λ) = (1/d)Σ_{a∈λ}A(a) is checked EXACT to be a rank-1 projector, so
  P(λ) = Tr(ρQ(λ)) ≥ 0 is a Born probability. The negative entry then follows from Gibbons–Hoffman–Wootters
  quant-ph/0401155v6 eq. (55), p.27: **W(a) = (1/d)(Σ_{λ∋a} P(λ) − 1)**.
- **Qubit** (H-QUBIT-NET, net +1). Bloch vector (−1, −1, −1)/√3; the line probabilities have minimum 0.2113.
  Reconstruction gives **W(0,0) = 1/4 − √3/4**, equal to Tr(ρA)/2. EXACT.
- **Qutrit** (H-ODD-WIGNER). The strange state (|1⟩ − |2⟩)/√2; the line probabilities are all ≥ 0. Reconstruction
  gives **W(0,0) = −1/3** and every other entry 1/6. EXACT, agreeing with Gross quant-ph/0602001v3 eq. 24, p.10.
- **Control: d striations instead of d+1.** With 3 of the qutrit's 4 striations the line-sum map has rank 7 < 9.
  - ρ = 0.9|S⟩⟨S| + 0.1·I/3 and ρ′ = ρ + 0.02K (K built from a kernel vector; ρ′ ≥ 0, smallest eigenvalue 0.0031)
    share every kept marginal (gap 6e-17).
  - Yet **W(0,0) = −0.2889 against −0.2689**, and the dropped striation differs by 0.06. Too few directions cannot fix
    the negative entry. COMPUTED.

**What is not new here.** This is the established tomographic principle: GHW for discrete systems, and optical homodyne
tomography for continuous ones since Smithey et al. 1993. That first experiment reconstructed a *squeezed* state,
whose W ≥ 0 (quant-ph/0511044v2 p.3; the original PRL is NAMED-NOT-READ). A *negative* W was first reconstructed
optically by Lvovsky et al. 2001, a single photon at efficiency 0.55 (review p.17–18; the original is NAMED-NOT-READ).
M's triangulation is that principle. What `signed.py` adds is the computation and the controls, not a new method.

## 6. Literature READ at source this pass (alphaXiv; short paraphrase, pages given)

| id (version) | used for |
|---|---|
| 2310.19296v1 Cerf, Hertz, Van Herstraeten | the principal-branch complex Wigner entropy, Im ∝ negative volume, Re additive, Im superadditive with Δ = (2/π)h_i h_i (pp.5–7); the real-valued extensions are not concave (p.5); thermal value (p.8); branch remark fn.7 (p.13). **Continuous variables only.** |
| 2512.03505v1 Park, Jeong | an application of the same quantity (h_i = πN) to billiard modes (pp.1–4) |
| 2410.15976v5 Brandenburger, La Mura | signed-measure axioms; signed Rényi Theorem 1 (p.4); exclusion of the \|p\|-weighted Shannon (p.4); eq. (45) (p.9); proof (pp.10–11) |
| 2503.03759v1 Li, Xu, Cao | −Σ P log P with the complex principal log for complex-valued P (p.9); no uniqueness result |
| 1307.7171v1 Veitch, Mousavian, Gottesman, Emerson | sum negativity, mana, additivity (pp.10–11); Theorem 15, uniqueness of sn under its conditions (p.12); strange state sn = 1/3 (p.15) |
| 1201.1256v4 Veitch, Ferrie, Gross, Emerson | discrete-Wigner negativity is necessary for speed-up and for distillation (pp.1–2) |
| quant-ph/0401155v6 Gibbons, Hoffman, Wootters | line sums equal Born probabilities and the reconstruction formula (pp.23, 27); non-uniqueness of the quantum net (pp.28–33); tensor-product A (p.38) |
| quant-ph/0602001v3 Gross | discrete Hudson theorem (pp.1–2); A(0) = parity (p.5); antisymmetric qutrit state (p.10) |
| quant-ph/0406015v1 Kenfack, Życzkowski | δ = ∫\|W\| − 1 (p.2); δ(\|1⟩) (p.7) |
| quant-ph/0511044v2 Lvovsky, Raymer (review) | Smithey 1993 (p.3); projections (p.6); FBP (p.7); ripples and MaxLik (p.9); single-photon negativity (pp.17–18) |
| 1106.1791v3 Baez, Fritz, Leinster | FinProb with non-negative measures (p.3); Theorem 2 and its continuity (p.4); Faddeev with I ≥ 0 (pp.7–8) |
| math/0008089v1 Elbaz-Vincent, Gangl; appendix by Kontsevich (wave 4) | (A), (B), (C) proved for H_p on ℤ/p (p.42); the CLAIM of a unique continuous solution on ℝ, H_∞ = Re H on (x, 1−x), with a cohomological sketch (p.43); chain rule for probabilities and the reduction to two values (p.44); differentiable case "well-known" (p.10); Aczél–Dhombres on ]0, 1[ (pp.10–11); Cathelineau (p.2) |
| 1903.06961v3 Leinster (wave 4) | builds on Kontsevich (pp.1–4); mod-p probabilities summing to zero (p.8); real reduction to two elements (p.26); real Shannon characterised by measurability, symmetry and chain rule, and symmetry essential to the fundamental-equation approach (p.27, Rem. 9.6) |

NAMED-NOT-READ: Smithey et al. PRL 70, 1244 (1993); Wootters, Ann. Phys. 176, 1 (1987); Rényi 1961 and Daróczy 1963
(H-RD); Lvovsky et al. PRL 87, 050402 (2001); Cathelineau, Math. Scand. 63 (1988) and Ann. Inst. Fourier 46 (1996);
Lee, Ann. Math. Stat. 35 (1964); Aczél–Dhombres (1989). Search depth: two alphaXiv discovery searches plus targeted
reads, and in wave 4 the two READs above (math/0008089v1 was found by the AGAINST verifier, not by this file's
searches -- the earlier search missed it). **A fuller prior-art search is OPEN.**

**What is known and what was not found.** This avoids over-representation in both directions.
- **Known**, and in the papers above:
  - the definition; Re/Im = (−Σp ln|p|, πN); Re additive; the Im product law (2310.19296v1, continuous);
  - mana and sum negativity, and their additivity (1307.7171v1);
  - signed-measure axioms that select signed Rényi (2410.15976v5);
  - exact discrete reconstruction (GHW) and FBP tomography;
  - (wave 4) the binary functional equation on all of ℝ whose unique continuous solution is Re H on two entries,
    claimed with a sketch by Kontsevich (math/0008089v1 p.43), and the chain-rule reduction to it (p.44, stated for
    probabilities).
- **Not found in the sources read.** These are a floor, not a priority claim:
  - (i) the finite-set range of Re H for given (n, N), the fact that negative Re H is forced only at n = 2, and
    min_N max Re H = ln(n−2);
  - (ii) BFL Theorem 2's **categorical** axioms on signed measures: Re H fails the codomain, the lawful family is
    span{Re H, N} (dictionary, and in wave 4 every continuous separable functional), and keeping the codomain leaves
    only πN. *Qualified in wave 4:* uniqueness of Re H under signed recursivity is Kontsevich's claim (§ 4c); what is
    not found is the BFL-axiom form and the N-versus-recursivity contrast;
  - (iii) the one-axiom fork (|w| vs w in 5′) separating signed Rényi from Re H -- *qualified in wave 4:* its substance
    (signed weights select Re H) is Kontsevich's 1995 claim; only its form inside Brandenburger-La Mura's framework is
    not found;
  - *Wave 3 listed* (iv) per-entry branch accounting (−2πik_i p_i; uniform branch −2πik) here. It is **elementary**, a
    one-line consequence of Log_k z = ln|z| + i(arg z + 2πk), and is dropped from this list (V2-0 problem 8); it stays
    the basis of D1.

## 7. Applications: computed signed cases for Q-1

- **(a) Qubit** (H-QUBIT-NET), Bloch vector (−1, −1, −1)/√3. EXACT/COMPUTED.
  - Net +1: W = (1/4 − √3/4, then 1/4 + √3/12 three times), **N = (√3−1)/4 = 0.183013**, Re H = 0.790058 nats,
    Im H = 0.574951, M = ln((1+√3)/2) = 0.311905 nats.
  - Net −1: the same state has **W ≥ 0** (N = 0, Re H = 0.972824). Whether this state counts as negative depends on
    the net (control).
  - Over pure states, the largest N on the grid is 0.183008, which approaches (√3−1)/4.
- **(b) A3's Bell pair** (`measure.BELL`, imported; H-PRODUCT-PS): 12 entries +1/8 and 4 entries −1/8.
  - **N = 1/2, Re H = 3 bits, Im H = π/2, M = 1 bit.** Each marginal has Re H = 2 bits.
  - So Re H(AB) − Re H(B) = **+1 bit**, while A3's von Neumann S(A|B) = **−1 bit**
    (`measure.conditional_entropy_bell`, imported).
  - **Re H does not reproduce the quantum conditional entropy.** This is a computed non-correspondence and is not to
    be read either way.
- **(c) The Method's index Λ** (cypher via A3's route; H-MOBIUS-WEIGHT). The import gives 976 cells, a box of 6,912
  (equal to the product of the alphabet sizes, 3·2·3·4·3·2·4·4) and E(order) = 0. The Möbius inverse of Λ's indicator
  reconstructs that indicator exactly, and Σp = 1 (the bottom cell is admitted).
  - **The weighting p** has 317 cells in its support: 159 at +1 and 158 at −1. So **N = 158**, M = log₂ 317 =
    8.308 bits, and **Re H = 0 exactly**: every |p| = 1, so Re H is blind here.
  - **The box-mixture weighting q** (q = p·|↓x|/976, a signed mixture of uniform box distributions, Σq = 1):
    N = 81.70, Re H = −3.033 bits, M = 7.361 bits.
  - **The non-negative baseline**, the uniform measure on Λ, has Re H = log₂ 976 = 9.930737 bits, equal to A3's
    figure.
  - **Control:** a full box has a one-point Möbius weight and N = 0.
  - **What this does and does not say.** Λ admits a signed decomposition with this negativity; Λ itself carries no
    negative probability. It says nothing about register 66 (the order ideal), which is outside this stage.

## 8. In use in Q-1 (Q1s-integrate, 2026-10-03)

`measure.py` (A3) now imports this file, lazily, and copies nothing. Its `q1(p)` returns Shannon (case SHANNON) when
no weight is negative, and this file's (Re H, Im H, N, M) (case SIGNED, under A3's H-SIGNED-CELLS) when some weight
is. On non-negative vectors Re H **is** A3's H, by definition (the same float expression): the bit-for-bit agreement
on 301 vectors and of the signed loss with `F_shannon` on 300 morphisms is printed STRUCTURAL in wave 4 and is not
evidence (*Q1s-integrate first said* "The ordinary case is recovered **exactly**"; V2-0 problem 5). R-INDEX on Λ under H-MOBIUS-WEIGHT
reproduces § 7(c) through `q1`. No A3 grade moves; the reasons are in A3-measure.md § (vii). For this,
`lambda_mobius` gained one keyword, `vectors=True`, which returns the two normalised weightings as lists. Nothing else
here changed, and the selftest count is unchanged.

## Discrepancies and history (first said … now)

- **D1, charter line 325:** "the other branches add 2 pi i k per negative entry". That is the shift of the **log**. The
  shift of **H** is −2πik_i p_i, which is +2πik_i|p_i| for a negative entry. Positive entries also have branches, and a
  uniform k shifts H by −2πik. COMPUTED in the selftest (elementary). *Q1s-build first said* "The charter itself is not
  edited: it is not this stage's file." **Wave 4 (R3-alone, tasked with it):** a dated correction note now stands in
  CHARTER.md **below** M's verbatim text and the Q-1s bullets; no word of M's or of the bullets was changed.
- **First coded:** a threshold N\*(n) above which Re H < 0 would be forced for every n. The bisection diverged for
  n ≥ 4. **Now:** forcing occurs only at n = 2, and min_N max Re H = ln(n−2) (EXACT, matching the search).
- **First run of the null space:** columns that were identically zero were rescaled into noise, so one mixed vector was
  reported. **Now** those columns are treated as null on their own, and the results are span{Re H, N} and
  span{Re H, M, Hartley, signed Rényi-2}.
- **No discrepancy found in any paper read.** 2310.19296v1 fn.7 is a hedged remark; per §1 it holds for uniform branch
  shifts.

## Named hypotheses

| hypothesis | what it fixes |
|---|---|
| H-PRINCIPAL | the branch convention |
| H-READING-M | the reading of "inverses and reflections" (ASKED of M) |
| H-NORM | Σp = 1 |
| H-FINSIGNED | the category used for BFL on signed measures |
| H-DICTIONARY | the 12 functionals the lawful-family results range over |
| H-SEPARABLE | (wave 4) X(p) = Σ g(pᵢ) with g continuous: the class § 4b's derivation covers |
| H-RECURSIVE-R | (wave 4) Kontsevich's setting: (A), (B) with weights of either sign, continuity on ℝ; zero-total blocks set to 0 |
| H-RD | the Rényi 1961 / Daróczy 1963 step, NAMED-NOT-READ |
| H-QUBIT-NET | the choice of qubit quantum net |
| H-ODD-WIGNER | Gross's odd-d Wigner function |
| H-PRODUCT-PS | the tensor-product phase space for two qubits |
| H-FBP / H-NOISELESS | Ram-Lak filter, finite grid, finite K, analytic marginals |
| H-MOBIUS-WEIGHT | the signed weighting on Λ |
| H-UNIFORM | A3's equiprobable cells |

## OPEN

1. Uniqueness over all continuous functionals. **Wave 4 restatement:** CLAIMED-IN-LITERATURE under chain rule
   (recursivity with weights of either sign), symmetry and continuity on ℝ (Kontsevich, math/0008089v1 p.43, a
   sketch); DERIVED, with the algebraic steps machine-checked, under BFL's convex-linear axioms for continuous separable
   functionals (§ 4b: c·Re H + b·N; Re H alone with product additivity; b·N alone with the codomain); **OPEN** under
   BFL's axioms for non-separable functionals, whose behaviour on convex atoms the axioms do not reach. *Wave 3 first
   said* "Uniqueness over all continuous functionals, both with and without BFL's codomain."
2. A machine-checked version of the signed-weight Brandenburger–La Mura derivation (H-RD is still NAMED-NOT-READ).
3. Which mean-value weighting (|w| or w) is *lawful* for The Method. That is a ruling for M, not a computation.
4. A fuller prior-art search on finite-set signed entropy (wave 4 found Kontsevich and Leinster through the verifier;
   the polylogarithm and information-cohomology literature -- Cathelineau, Baudot–Bennequin, Vigneaux -- is
   NAMED-NOT-READ).
5. The meaning of M's "inverses and reflections" (H-READING-M).
6. Whether any operational meaning attaches to Re H once p has negative entries. 2310.19296v1 p.13 says this is
   missing for the continuous case as well.

On M's paper instruction ("if this does prove useful"): whether it has proved useful is M's call. The material a paper
would need is in sections 3, 4(a)–(d), 4b, 4c, 5 and 7. The prior art it would have to position against is
2310.19296v1, 2410.15976v5 and 1307.7171v1, **and** (wave 4, V2-0 problem 1) Kontsevich's 1½-logarithm
(math/0008089v1, appendix, pp.42-44), Elbaz-Vincent & Gangl (same paper), Cathelineau (NAMED-NOT-READ) and Leinster
1903.06961v3 (p.27). *Wave 3 first listed* only the first three.
