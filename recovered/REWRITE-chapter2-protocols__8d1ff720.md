# Rewrite — Chapter 2, "The protocols"

**Treatment (reader-volume reduction, standing rule).** The reader-facing volume keeps the protocol *rules* — the method by which the work is done — and drops the workshop material (worked examples run on the book's own sections, instrument-histories, self-audits, and the account of how the work itself runs), which is retained in the process/working record. One rule is folded in from the cut Chapter 4: the former §4.6, "a test must be able to fail," placed **thematically after §2.8** (with §2.7 and §2.8 it forms the group on what makes a check trustworthy), and the later protocols renumbered +1 to accommodate it.

**Kept, in final numbering:** §2.1–§2.8 (unchanged), new **§2.9** (a test must be able to fail — folded from §4.6), then §2.10–§2.18 (the former §2.9–§2.17). **Cut to the workshop record:** the worked/meta subsections of §2.16–§2.18 (former §2.15–§2.17), the former §2.18–§2.19 (computable-vs-decided; safe repair), the former §2.20 (Zeno directive), and the former §2.21–§2.24 (source-defect block).

**Renumber cascade (for write-back).** Former §2.9→§2.10, §2.10→§2.11, §2.11→§2.12, §2.12→§2.13, §2.13→§2.14, §2.14→§2.15, §2.15→§2.16, §2.16→§2.17, §2.17→§2.18. All 33 references to former §2.9–§2.17 across the volume shift +1. The four Chapter-4 references to §4.6 (Ch 13, 14, 17, 18) re-point to the new §2.9. Cut-section references also shift (Ch 18→ former §2.18 = computable/decided; Ch 14/21→ former §2.24; Ch 15→ former §2.23; Ch 30→ former §2.15.2) and are handled with the cuts.

---

## 2. The protocols

### 2.1 Channel construction
    A channel is one parent term, one ℓ, one series in n.

No channel may mix parents, mix ℓ, or cross a coupling-scheme boundary. Where the source's labelling changes scheme partway up a series — from LS to jK coupling — **the channel ends there**, and the cells above are not claimed. This is what limits Si I to four cells and P II to one.

### 2.2 Admissibility
    r = 2Z²R / (ν³σ) ≥ 5

Levels must be separated by more than five times their uncertainty. The ratio r measures that separation: Z is the nuclear charge, R the Rydberg constant, ν the effective quantum number of the level, and σ its measurement uncertainty. Because r falls as ν⁻³, every channel eventually drops below the threshold and leaves the domain — and the rule states where that happens, in advance, rather than discovering it after the fact.

### 2.3 Cost resolvability
    ν ≤ ν_V = (3Z²R / 5q)^{1/4}

The bracket needs levels *separated*; a second test, the cost, needs the curvature of the series *resolved*, and curvature washes out first. The threshold ν_V (with q the number of electrons removed) marks where. Cells above ν_V are dropped from the cost test but kept for the bracket — a distinction applied ahead of time in Li I and after the fact in Al I.

### 2.4 Dilution
    cells per channel ≈ (measured shells / D) − 2, with D the number of J levels in the core's ground configuration

**Dilution divides; it does not forbid.** The more finely the core's ground state splits into J levels — the larger D — the fewer usable cells each channel yields, but a large D does not rule a species out. Ne II fails at D = 5 with two shells; Ar II succeeds at D = 5 with three; Bi I succeeds at D = 5 with five.

### 2.5 Census before search
    Compute which species could work before looking for data.

D is obtained from the core configuration by enumerating its antisymmetric states; no spectroscopic data enters. On that basis, **27 sequences were admitted, 12 flagged as needing exceptional depth, and 5 excluded structurally** — all before a single measurement was sought.

### 2.6 Declines are recorded
    A collection reporting only successes cannot be checked.

Every species examined and rejected is listed with its cause. Four causes have been identified — dilution, depth, coupling-scheme change, and core-excited interleaving — and §23.11 gives a worked case of each.

### 2.7 Exhaustive verification where possible
    Sampling n cells with no failure bounds the failure rate at ρ ≤ 3/n at 95% confidence. It never certifies ρ = 0.

Where a claim is made about every cell of a finite lattice, it is checked on **every** cell, not a sample. Where sampling is unavoidable, the sample size is stated — because sampling can bound how often a thing fails, but it can never prove it never does.

### 2.8 Two independent routes
    For every quantity that matters, build a second derivation that does not pass through the first.

This is the self-defence law (ⅅ_def) made operational. It is realised experimentally in the antiprotonic-helium check of §16.4, where two laser measurements agree to within 0.09σ with no shared step. **An identity computed along a single path proves nothing**: *w* = *V*·*e* cannot fail if *V* was itself defined as *w*/*e* — the two sides share the road, so their agreement is empty.

### 2.9 A test must be able to fail
    A check counts as evidence only once it has been shown capable of returning a failure. Before relying on a test, exhibit the input that would make it fail.

A test that has never failed and cannot be made to fail tells you nothing when it passes — its passing is indistinguishable from a test that checks nothing at all. So a criterion is not trusted on the strength of a clean result; it is trusted once a failing case has been demonstrated for it. A pass reported as support, from a check whose ability to fail was never shown, is disclosure dressed as evidence.

### 2.10 Refuse rather than coerce
    No third state. A quantity is admissible or it is refused; it is never silently defaulted.

A guard returning a null that a caller then read as "false" produced false conclusions that did not look wrong. **Totality — insisting every quantity be one of exactly two states — is the only mechanism that catches this**, and it works by preventing the computation from running rather than by detecting the error after it has spread.

### 2.11 Retrieval
    Enumerate targets from the index before searching. List routes per cell. Prefer high-ρ cells. Read every retrieved source for its successors. When a route is blocked, move along the route set. Record ρ for cells that fail. And re-enumerate whenever the set the targets are drawn from grows.

Chapter 19 develops this. A blocked cell with retrieval redundancy ρ = 1 (one known route, now closed) is a **stated gap**, not an unexplained absence.

    Enumerating once is not a protocol. It is a snapshot, and a snapshot of a growing object
    is a defect the moment it is taken.

### 2.12 Provenance
    Every number traces to a compilation, table and page, or to a database entry with its stated uncertainty.

Appendix B carries this at channel level for all 153 channels.

### 2.13 Withdrawal
    Every retracted claim is logged with what replaced it.

Chapter 28 holds the record. The register is the evidence for Chapter 16, not an apology for it.

### 2.14 Commit before you look
    A prediction is written down before the measurement is requested. A method is chosen before its answer is visible.

This is the process index of §28.8 enforced by hand — the constraint *visible ≤ committed*, of §16.4 form, closed, with E = 0. **It is the only protocol here adopted in response to an error that no computation could have caught** — because every computation was correct, and what failed was the independence of a choice. The deduction of §25.6 was committed under it.

### 2.15 Compute, then write
    The result is computed before the sentence describing it is written.

State the number before you state what it means. A sentence that names a conclusion while the output contradicting it stands unread is the failure this protocol exists to prevent, and it is the one that most needed stating.

### 2.16 Every failure is a bound
    Every failed attempt is a true answer, and by P8 a true answer is a bound. Record what each failure excludes, and collect the exclusions.

A failed attempt is a true answer about where the target is *not*. Recorded rather than discarded, failures accumulate into bounds — lower bounds say the answer contains something, upper bounds say it is contained in something, negatives remove whole methods, and structural failures name an object that was the wrong one. When the lower and upper bounds meet, the answer lies between them.

### 2.17 The grid — read the empty cells
    Every open question is a set of requirements, and requirements form an index. Lay them out as a grid, mark what is occupied, and read the empty cells rather than hunting for them.

It is Chapter 6 applied to a question rather than to the elements: a table with unfilled cells does not need to be searched, because the layout shows what is missing.

    The first empty cell in a column is the whole obstacle. Everything below it is downstream.

And a reduction does not close a question — it moves the difficulty to a new object, where it is not yet visible. State the reduction and the residue in the same sentence: not "this reduces to a constraint problem" but "this reduces to a constraint problem whose constraints are most of the object's pairs and are not yet handled."

### 2.18 Triangulation — three results locate a fourth
    For every three results or bounds that measure the same object, triangulate: they identify a related data point that none of them states.

Three measurements of one thing are not three facts; they are a position. And the check runs both ways: three measurements that locate a consistent fourth give a result, while three that locate no consistent fourth give a correction instead — one of the three is wrong. Both outcomes are useful, and the protocol does not distinguish them in advance.

---

**Cut to the workshop record (not in the reader volume):** the worked/meta subsections of §2.16–§2.18 (the former §2.15.1–.3, §2.16.1–.3, §2.17.1–.3 — worked on §30.3 and the book's own questions); the former §2.18–§2.18.1 (computable vs decided; the decisions-form-a-DAG finding); the former §2.19–§2.19.1 (safe repair, worked on the register's headings); the former §2.20 (the Zeno prime directive — how the work itself runs, with the tooling named); the former §2.21–§2.24 (the source-defect block, belonging to the editing project).

**Dependency map for the cuts (measured, for write-back).** Several surviving argument chapters reference the cut sections, so write-back must inline or re-point each — and all references below carry the +1 renumber shift:
- **Ch 18 and Ch 32 → former §2.18** (computable vs decided) — if cut, state the distinction where they use it.
- **Ch 14 and Ch 21 → former §2.24** (the spread/heuristic point).
- **Ch 15 → former §2.23** (expression-not-verdict).
- **Ch 30 → former §2.15.2** (ten-failures example; re-pointable to the surviving §2.16 rule).
- **Ch 5 ("What the protocols are for") → seven cut sections** — Chapter 5 is itself being cut as workshop.
- **Ch 13, 14, 17, 18 → former §4.6** — re-point to the new **§2.9**.
- Harmless: cut-section-to-cut-section refs, Ch 3's source-defect refs, Ch 28 (register), Appendices D/E, Index (updated at production), References.