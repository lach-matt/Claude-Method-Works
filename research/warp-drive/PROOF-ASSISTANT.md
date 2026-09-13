# The proof assistant in this repository

**There is one, it is Z3, and getting it was the non-obvious part.** This note exists so no future
session repeats the search.

---

## What is available, and what is not

| | |
|---|---|
| **Z3 (SMT solver)** | **AVAILABLE.** `pip install z3-solver` — pypi is on the egress-proxy allowlist |
| Lean 4 | **NOT available.** `elan` needs github; the proxy answers 403 to CONNECT |
| Coq | **NOT available.** `opam` needs github, same refusal |
| pandoc / LaTeX | not installed (PDFs render through headless Chromium — see `render_pdf.py`) |

`pypi.org` and `files.pythonhosted.org` sit in the proxy's `noProxy` list, which is why the Python
route works when the others do not. Check the current state with:

```
curl -sS "$HTTPS_PROXY/__agentproxy/status"
```

**Do not vendor Z3 into the repository.** It is ~53 MB installed. This is a document corpus; the
install is one command and the wheel does not belong in git.

---

## The files

| file | what it is |
|---|---|
| **`prover.py`** | the reusable harness — start here for a *new* claim |
| **`machinecheck.py`** | the obligations behind `paper/THE-HIERARCHY-LAW.md`, 21 of 21 discharged |
| **`lawfigures.py`** | not a prover — recomputes every *number* the paper states |

```
pip install z3-solver
python3 prover.py            # worked example, 4 obligations
python3 machinecheck.py      # the paper's 15, with soundness guards first
```

---

## What a machine-check here actually means

**It is not enumeration.** A claim is stated as a formula whose variables range over **every** subset
`X` of a finite box — and, where the generated sublattice `⟨X⟩` appears, over **every** closed
superset `S` as well. The harness asserts the **negation** and asks Z3 for a model. `unsat` means no
counterexample exists.

> At `d = 3` over a 3×3×3 box that is **2²⁷ = 134,217,728 subsets.** Enumeration in the same document
> reached `|X| ≤ 5`. Machine-checking covers cases enumeration cannot.

It is still a statement **about that box**. A proof for 3×3×3 is not a proof for all `d`. The paper
keeps `PROVED` (a written argument, general), `EXHAUSTIVE` (a stated finite frontier) and
`MACHINE-CHECKED` (this) as three separate columns for exactly that reason.

---

## The two encodings that make it decidable

Both are the difference between a claim you can check and one you cannot.

**1 · No `max`, no `φ`.** The staircase test `x_i ≤ max{ y_i : y ∈ X, y_j ≤ x_j }` is not directly
expressible. But a maximum is attained exactly when a witness exists:

> `x ∈ R(X)`  **iff**  for all `i ≠ j` there is `y ∈ X` with `y_j ≤ x_j` and `y_i ≥ x_i`

which is first-order. That is `prover.in_R`.

**2 · No fixed point.** `⟨X⟩` is a *least fixed point*, which SMT cannot express. Use the other
definition — the intersection of all closed supersets — so

> `R(X) ⊆ ⟨X⟩`  becomes  *"for every `S` with `X ⊆ S` and `S` closed, `R(X) ⊆ S`"*

which is first-order. That is `prover.closed`, used with an unknown `S`.

---

## Always run the guards

**A machine-check is worthless in two specific ways, and both are silent.**

**Vacuity.** If the hypothesis is unsatisfiable, the implication is vacuously true and `unsat` proves
nothing at all. `prover.non_vacuous` checks the hypothesis is satisfiable — and should be given a
non-triviality demand too (for instance that `S` is strictly inside the box), since a hypothesis
satisfiable only by the whole box is nearly as empty.

**Encoding drift.** If the encoded predicate is not the operator you meant, Z3 proves something else
and reports success. `prover.encoding_matches` compares the encoding against the operator the
repository actually computes, cell by cell.

`machinecheck.py` runs both before reporting any obligation, and refuses to report if either fails.
**Copy that discipline.** A green run with an unchecked encoding is worse than no run, because it
looks like evidence.

---

## Adding a new obligation

Write a function returning a Z3 formula that should hold for **all** `X`:

```python
import z3
from prover import prove, in_R, closed, observed, contains

def my_claim(X, S, cells, d, shape):
    # "if X observes every value, then everything in R(X) lies in
    #  every closed superset of X"  --  i.e. R(X) subset <X>
    hyp = z3.And(observed(X, cells, shape), contains(X, S, cells), closed(S, cells))
    return z3.Implies(hyp, z3.And([z3.Implies(in_R(X, c, cells, d), S[c])
                                   for c in cells]))

prove("my claim, 3x3x3", (3, 3, 3), my_claim)
```

Then **guard it** before you believe it, and record the box you proved it over — not "machine-checked"
without qualification.

---

## What is not machine-checked, and why

Clauses D–H of `THE-HIERARCHY-LAW.md` and the cited lift (Baker–Pixley) are **not** machine-checked.
They are not of this logical shape: **D** quantifies over *operators*, **E** and **H** are statements
about five specific named operators, **F** quantifies over relabellings, and the lift is a theorem
whose proof lives in the literature. Machine-checking them would mean formalizing the five operators
themselves — a larger undertaking than that document represents. Each carries a written proof and,
where applicable, an explicit witness instead.
