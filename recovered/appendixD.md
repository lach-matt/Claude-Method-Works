
---

# Appendix D — Principles and protocols

**Everything in this book was produced under a stated set of rules.** They are
collected here so that a reader can apply them, check them, or reject them —
and so that the claims of Chapter 22 have something concrete to be tested
against.

**Two kinds appear.** *Principles* say what an index is; ten of them admit
exact mathematical statement. *Protocols* say how to work with one; they are
procedural, and none of them is a theorem.

---

## D.1 The principles

### Formalised — ten

| | principle | expression | where |
|---|---|---|---|
| **P1** | a complete index is self-referencing | **𝓡(Λ) = Λ** | §7.1, Ch. 8 |
| **P2** | a complete index is self-defending | **𝒟 = dim *q* − rank ∂Φ/∂*p* ≥ 1** | Ch. 9 |
| **P3** | when the path is not found, work backwards from the desired output to an established input | invert Φ; if the fibre is non-trivial, find the datum that separates it | §14.4 |
| **P7** | all questions must close | ∃N : Ω_N = ∅ — **terminal, not monotone** | §20.5 |
| **P8** | any true answer, good or bad, is a bound | A_n ⊆ A_{n−1}, a decreasing filtration | §16.4 |
| **P9** | if the first dimension is a single all-encompassing definition, every other dimension is a perspective of it | **rank(log **q**) = 1** | §17.2 |
| **P10** | allow continued expansions | §9.4-form constraints preserve closure | Ch. 10 |
| **P12** | every test must be run against every cell | ρ = 0 certain ⟺ *n* = \|Λ\| | D.2.7 |
| **P13** | coherence cannot be claimed while any caveat, gap or contradiction stands | **COHERENT ⟺ Ω = ∅** | §20.5 |
| **P17** | the path is always through the bounds | following a bound costs 1/N of searching the volume | §16.4, Ch. 12 |

**Three of these were corrected by the act of formalising them.** P7 was stated
as though the open-item count decreases; it does not — across this work it ran
5 → 4 → 3 → 4 → 3 → 7 → 3 → 3. Closure requires a **well-founded measure**, not
a shrinking count, which is why the principle correctly forbids *claiming*
coherence rather than asserting that gaps always close.

### Procedural — seven

| | principle |
|---|---|
| **P4** | always audit results |
| **P5** | always compute the result before assuming the result |
| **P6** | when a question is confusing, reframe the question |
| **P11** | close all gaps before continuing |
| **P14** | a structural problem suggests a structural solution |
| **P15** | for fetching: use the index to navigate; data can be retrieved in pieces |
| **P16** | treat bounds, constraints and limits as coordinate values |

**These have no expressions, and saying so is better than manufacturing one.**
They govern how an agent uses an index, not what an index is. P15 is the
exception in one respect: it has a *measure* — retrieval redundancy ρ, Chapter
12 — without being reducible to it.

### The reflexive principle

| | principle | expression |
|---|---|---|
| **P18** | if the index is complete, a work that comprehends it completely is itself an index, and is itself self-referencing and self-defending | Chapter 22 |

---

## D.2 The protocols

### D.2.1 Channel construction

> **A channel is one parent term, one ℓ, one series in *n*.**

No channel may mix parents, mix ℓ, or cross a coupling-scheme boundary. Where
the source's labelling changes scheme partway up a series — LS to jK — **the
channel ends there**, and the cells above are not claimed. This is what limits
Si I to four cells and P II to one.

### D.2.2 Admissibility

> **r = 2*Z*²*R* / (ν³σ) ≥ 5**

Levels must be separated by more than five times their uncertainty. *r* falls
as ν⁻³, so every channel eventually leaves the domain; the rule states where,
in advance.

### D.2.3 Cost resolvability

> **ν ≤ ν_V = (3*Z*²*R* / 5*q*)^{1/4}**

The bracket needs levels *separated*; the cost needs curvature *resolved*.
**Curvature washes out first.** Cells above ν_V are excluded from the cost test
and retained for the bracket — a distinction applied prospectively in Li I and
diagnostically in Al I.

### D.2.4 Dilution

> **cells per channel ≈ (measured shells / D) − 2**, with D the number of J
> levels in the core's ground configuration

**Dilution divides; it does not forbid.** Ne II fails at D = 5 with two
shells; Ar II succeeds at D = 5 with three; Bi I succeeds at D = 5 with five.

### D.2.5 Census before search

> **Compute which species could work before looking for data.**

D is obtained from the core configuration by enumerating antisymmetric states.
No spectroscopic data enters. **27 sequences admitted, 12 needing exceptional
depth, 5 excluded structurally.**

### D.2.6 Declines are recorded

> **A collection reporting only successes cannot be checked.**

Every species examined and rejected is listed with its cause. Four causes have
been identified — dilution, depth, coupling-scheme change, and core-excited
interleaving — and §15.9 gives a worked case of each.

### D.2.7 Exhaustive verification where possible

> **Sampling *n* cells with no failure bounds the failure rate at ρ ≤ 3/*n* at
> 95% confidence. It never certifies ρ = 0.**

Where a claim is universally quantified over a finite lattice, it is checked
on **every** cell. Where sampling is used, the sample size is stated.

### D.2.8 Two independent routes

> **For every quantity that matters, build a second derivation that does not
> pass through the first.**

This is 𝒟_def made operational. It caught a mis-stated relation in Chapter 9,
and it is realised experimentally in the antiprotonic-helium check of §9.4,
where two laser measurements agree at 0.09σ with no shared step.

**An identity computed along one path is vacuous.** *w* = *V*·*e* cannot fail
if *V* is *defined* as *w*/*e*.

### D.2.9 Refuse rather than coerce

> **No third state. A quantity is admissible or it is refused; it is never
> silently defaulted.**

A guard returning a null that a caller coerces to a Boolean produced three
false conclusions in this work, none of which looked wrong. **Totality is the
only mechanism that catches this**, and it works by preventing the computation
rather than by detecting the error.

### D.2.10 Retrieval

> **Enumerate targets from the index before searching. List routes per cell.
> Prefer high-ρ cells. Read every retrieved source for its successors. When a
> route is blocked, move along the route set. Record ρ for cells that fail.**

Chapter 12. A blocked cell with ρ = 1 is a **stated gap**, not an unexplained
absence.

### D.2.11 Provenance

> **Every number traces to a compilation, table and page, or to a database
> entry with its stated uncertainty.**

Appendix C carries this at channel level for all 153 channels.

### D.2.12 Withdrawal

> **Every retracted claim is logged with what replaced it.**

Chapter 18. Forty-eight entries. **The register is the evidence for Chapter 9,
not an apology for it.**

### D.2.13 Compute, then write

> **The result is computed before the sentence describing it is written.**

**This is the protocol most often violated in the production of this book.**
The dominant failure recorded in Chapter 18 is prose asserting a conclusion
while the output contradicting it stands on the same screen. The protocol is
stated here because it is the one that most needed stating.

---

## D.3 What the protocols are for

Each prevents a specific failure, and each failure occurred:

| protocol | failure it prevents | instance |
|---|---|---|
| D.2.1 channel construction | claiming cells across a label change | Si I, P II |
| D.2.2 admissibility | bracketing unresolved levels | — |
| D.2.3 cost resolvability | reading rounding as physics | Al I *n*f |
| D.2.4 dilution | excluding a viable species | Ar II, Bi I |
| D.2.5 census first | searching without targets | 27 sequences enumerated |
| D.2.6 declines recorded | an uncheckable collection | Ne II, Cu II |
| D.2.7 exhaustive testing | a claim resting on a sample | A.4 on all cells |
| D.2.8 two routes | an undetectable derivation error | *w* = 3ν·*e* |
| D.2.9 refuse, don't coerce | a missing value read as a real one | the cap discard |
| D.2.10 retrieval | abandoning a cell when a source is blocked | ρ = 6 vs ρ = 1 |
| D.2.11 provenance | an untraceable number | 153 channels |
| D.2.12 withdrawal | an unfalsifiable record | 48 entries |
| D.2.13 compute then write | **the dominant failure** | most of Chapter 18 |

**The protocols are not advice. They are the failure modes of this work,
inverted.**