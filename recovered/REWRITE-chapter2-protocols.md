# Rewrite — Chapter 2, "The protocols"

**Treatment (reader-volume reduction, standing rule).** The reader-facing volume keeps the protocol *rules* — the method by which the work is done. It drops the workshop material: the worked examples run on the book's own sections, the instrument-histories, and the self-audits. Those are retained in the process/working record, not deleted. Kept here: §2.1–§2.14 (the fourteen core protocols), the rule statements of §2.15, §2.16, §2.17, and §2.20's prime directive. Cut to the workshop record: §2.15.1–.3, §2.16.1–.3, §2.17.1–.3, §2.18–§2.18.1, §2.19–§2.19.1, and §2.21–§2.24 (the last being a known source-defect block belonging to the editing project).

Bare formulas are glossed; terms of art kept. §-references that survive are preserved; references *into* the cut sections are noted in the dependency map at the foot.

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

### 2.9 Refuse rather than coerce
    No third state. A quantity is admissible or it is refused; it is never silently defaulted.

A guard returning a null that a caller then read as "false" produced false conclusions that did not look wrong. **Totality — insisting every quantity be one of exactly two states — is the only mechanism that catches this**, and it works by preventing the computation from running rather than by detecting the error after it has spread.

### 2.10 Retrieval
    Enumerate targets from the index before searching. List routes per cell. Prefer high-ρ cells. Read every retrieved source for its successors. When a route is blocked, move along the route set. Record ρ for cells that fail. And re-enumerate whenever the set the targets are drawn from grows.

Chapter 19 develops this. A blocked cell with retrieval redundancy ρ = 1 (one known route, now closed) is a **stated gap**, not an unexplained absence.

    Enumerating once is not a protocol. It is a snapshot, and a snapshot of a growing object
    is a defect the moment it is taken.

### 2.11 Provenance
    Every number traces to a compilation, table and page, or to a database entry with its stated uncertainty.

Appendix B carries this at channel level for all 153 channels.

### 2.12 Withdrawal
    Every retracted claim is logged with what replaced it.

Chapter 28 holds the record. The register is the evidence for Chapter 16, not an apology for it.

### 2.13 Commit before you look
    A prediction is written down before the measurement is requested. A method is chosen before its answer is visible.

This is the process index of §28.8 enforced by hand — the constraint *visible ≤ committed*, of §16.4 form, closed, with E = 0. **It is the only protocol here adopted in response to an error that no computation could have caught** — because every computation was correct, and what failed was the independence of a choice. The deduction of §25.6 was committed under it.

### 2.14 Compute, then write
    The result is computed before the sentence describing it is written.

State the number before you state what it means. A sentence that names a conclusion while the output contradicting it stands unread is the failure this protocol exists to prevent, and it is the one that most needed stating.

### 2.15 Every failure is a bound
    Every failed attempt is a true answer, and by P8 a true answer is a bound. Record what each failure excludes, and collect the exclusions.

A failed attempt is a true answer about where the target is *not*. Recorded rather than discarded, failures accumulate into bounds — lower bounds say the answer contains something, upper bounds say it is contained in something, negatives remove whole methods, and structural failures name an object that was the wrong one. When the lower and upper bounds meet, the answer lies between them.

### 2.16 The grid — read the empty cells
    Every open question is a set of requirements, and requirements form an index. Lay them out as a grid, mark what is occupied, and read the empty cells rather than hunting for them.

It is Chapter 6 applied to a question rather than to the elements: a table with unfilled cells does not need to be searched, because the layout shows what is missing.

    The first empty cell in a column is the whole obstacle. Everything below it is downstream.

And a reduction does not close a question — it moves the difficulty to a new object, where it is not yet visible. State the reduction and the residue in the same sentence: not "this reduces to a constraint problem" but "this reduces to a constraint problem whose constraints are most of the object's pairs and are not yet handled."

### 2.17 Triangulation — three results locate a fourth
    For every three results or bounds that measure the same object, triangulate: they identify a related data point that none of them states.

Three measurements of one thing are not three facts; they are a position. And the check runs both ways: three measurements that locate a consistent fourth give a result, while three that locate no consistent fourth give a correction instead — one of the three is wrong. Both outcomes are useful, and the protocol does not distinguish them in advance.

### 2.20 The prime directive — nothing runs unbounded
Every action, computation, tabulation, build and verification is executed in a **Zeno structure**: the work is divided until each piece fits inside a declared budget, each piece writes its result before the next begins, and a rerun costs only what has not already succeeded.

**One exception, and it is the only one: fetched literature is exempt.** A computation may be halved and rerun on half; an external source cannot, because halving what was read changes what was read. A source consulted at half length is a different source, and the record would then carry a claim about a document nobody has seen. So a fetch runs to completion or is not made, and its budget is declared before it rather than enforced during it.

    No operation runs unbounded. A step declares a budget; work that exceeds it is halved and
    retried; a step that has succeeded is never recomputed.

Three guarantees are the reason for the rule. Nothing is lost to a timeout, because the last completed step is on disk before the next starts. A rerun costs only the remainder. And a step that overruns *reports* its overrun rather than dying silently — the part that matters most, since a computation quietly growing toward a limit is invisible until the run it kills.

---

**Cut to the workshop record (not in the reader volume):** §2.15.1–.3 (the procedure and the ten-failures example worked on §30.3); §2.16.1–.3 (the grid worked on the book's own open questions); §2.17.1–.3 (triangulation worked on §30.3); §2.18–§2.18.1 (computable vs decided; the decisions-form-a-DAG finding); §2.19–§2.19.1 (safe repair, worked on the register's headings); §2.21–§2.24 (the source-defect block, belonging to the editing project).

**Dependency map for the cuts (for write-back):**
- §2.18 cited §3.8 and §3.1–7; §2.19 cited §3.8 — both cut sections citing cut sections, no dangling reference into the reader volume.
- Nothing in the surviving reader volume points *into* §2.15.1–.3, §2.16.1–.3, §2.17.1–.3, §2.18, §2.19, or §2.21–.24 except via those sections themselves. (To be reconfirmed by the cross-reference sweep at write-back.)
- §2.20 names the Zeno tooling in the source; per Ruling 46/61 the tool name is handled at press, separate from this pass. The directive itself is kept as method.