# DIGEST — what a session needs to hold before it works
Written 2026-08-15 (session 1.8), after a bounded read of the book and the four compendia.
Extended 2026-08-15 from `BRIDGE-1_7_2-to-next.md` §2 and §4, carrying **R 1660–1668**.
This is an orientation file, not a substitute for any of them. It records what was read,
what was not, and the load-bearing facts a fresh session must not have to rediscover.
Its test: a fact belongs here if a session would otherwise recompute it from source.

## The one claim
A **closed** index — closed under the meet and join of its own coordinates — cannot help
containing its own definition, cannot help containing its own contradiction, and determines
exactly what may be added to it. `E(X) = |ℛ(X)| − |X| = 0` is the closure test;
`|∏ᵢ Aᵢ| = |X| + E(X) + refused` is the partition identity.
Closure gives **six things and no others**: alphabet, bounds, totality of the membership
test, which cells may be added, which axes adjoined, which constraints imposed.
Three further mechanisms exist and none follows from closure: order recovered only across a
tree, a wrong value only from outside, a wrong derivation only along a second route.
**Closure never gives reference** — that the coordinates refer to anything.
An index that is not a fixed point is **not defective**: where a certificate exhibits an
operation reaching a fixed point, E measures the *drawing*; where none exists, E measures the
*world*. Openness is a measurement; closure is the case where it is zero.

## The objects
- **Λ** — 976 cells, eight coordinates (n, ℓ, k, q, e, f, g, 2S), seven bounds. A cell is a
  **transition, not a state**. E(Λ) = 0. E(periodic table) = 36 — the whole argument.
- **Λ_spectra** — the coordinate index: four coordinates (Z, charge, ℓ, 2S+1),
  **104,832 cells** at the Z=120 bound, E = 0. In `SPECTRA.md` and `COORDINATES.tsv`.
- **Λ_spectra^obs** — the *measured channel survey*, in `INDICES.md`: three coordinates
  (Z, core charge, ℓ), **1,664 cells**, E = 1,351, holding 596 channels across 313 cells.
  **The name collision of R 1657 was settled at R 1660** by naming the survey separately and
  relabelling its column headed E as **unwitnessed** — a RELABEL, which A.cert admits. They
  were never the same lattice; only the name was shared. Do not read the survey's E as a
  closure defect of the coordinate index.
- **Λ_phys, Λ_chem, Λ_PCA, Λ_xray** — in the Physics Compendium and INDICES.

## The shape of Λ_spectra, as computed (R 1651–1656)
Two rules generate it and nothing else:
1. **charge ≤ Z** — the triangle. At Z=120: 7,260 pairs = 120·121/2.
2. **mult = f(N)**, N = Z − charge + 1 — the isoelectronic count. Exact, zero exceptions.
   The 19 N whose fibre is a **singleton** are precisely the aufbau first-in-subshell counts
   [1,3,5,11,13,19,21,31,37,39,49,55,57,71,81,87,89,103,113]. The Madelung sequence is already
   inside the index, as a fibration rather than a coordinate.
ℓ runs 0–7 in full on every pair. Product 1,036,800 − 104,832 present = 931,968 refused by rule.
**E = 0 at any cutoff**, because both rules are total — so the Z bound is a declaration about
the world, not a property of the index. Z = 119, 120 are carried with the bound
"no nuclide synthesised; theoretically admitted — Janet left-step".

## The values, and what voids them (R 1660–1668) — do not recompute these
`COORDINATES.tsv` indexes cells. **Values live in `MEASUREMENTS.tsv` — 554 rows on 158 cells.**
- **The value store was scalar, and that was the fault (R 1662).** What looked like rival
  measurements colliding in one cell were never collisions: one slot was holding many readings.
  `MEASUREMENTS.tsv` is the repair — **a cell's members are its ROWS** (554 rows on 158 cells;
  Ti I alone carries 45). The `members` column is an integer COUNT of levels, not the levels —
  those live in `spectra_raw/queue2/` and were recovered at R 1675, not lost.
- **The store's statistic is the MEDIAN, and this was measured, not chosen (R 1673, 1675).**
  Of 358 series whose member count reproduces exactly from raw, the median equals the stored δ
  in **353 — 98.6%**; the mean in 3, all of them series too short to distinguish the two.
  **T2 asked which statistic to declare; the computation had already declared it.**
- **`store_gen.py` is the store's partial generator (R 1674–1675).** Nothing built
  `MEASUREMENTS.tsv` — `phase4.py` only reads it — so the store sat outside C3 and could not be
  shown not to have drifted. The generator recovers members from raw and derives all three
  perspectives. **It inherits the LIMIT ASSIGNMENT from the store, so it closes the VALUE
  derivation and not the SERIES construction.** Residue: 68 series recover no members, 128
  recover a count disagreeing with the store. Neither diagnosed.
- **The captures speak four languages (R 1663): LS 426 · jK 96 · jj 31 · unresolved 1.**
  Four parsing faults, each caught by a different instrument. This is the concrete form of
  *never fit across a language boundary*: a coupling scheme is not a style of notation.
- **`mult` is a ground-state property; the measurements carry the parent's (R 1665).** One
  coordinate name doing two jobs — 69 series need 28 refused cells. A.cert does not admit
  adding a coordinate, so **this is a definition question, not an extension one** (T7, pending,
  and it blocks further neutral incorporation).
- **145 of the 554 δ are void (R 1664)** — defected against the wrong core. R 1649's fallback
  was exactly the silent default §2.9 forbids. **409 remain usable; the index itself is clean.**
  Where a parent's limit was never published the series **cannot be defected at all** — that is
  E measuring the *world*, not the drawing, and may want a named bound (T8).
- **306 of the 554 span a single n (R 1666)** — fine structure graded as convergence. The
  A/B/C tier thresholds therefore graded the wrong quantity on 55% of rows. **Zero of this
  reached the index**; it is a fault of the grading, not of Λ_spectra.
- **F(−1) = 0 is forced by ℓ-totality (R 1661)**, at any cutoff. The cell count was never the
  content — consistent with E = 0 being independent of the Z bound.
- **Nothing from the Gemini items has entered any index.** The fourth was tested: Madelung as
  minimisation of I(n,ℓ) = (n+ℓ) − ε/n reproduces the order for **every ε from 0.01 to 11.99**,
  breaking only at 12 — so ε carries no physics and the functional is a **relabel** of
  Madelung's second rule, which R 1626 settled buys nothing. It does not touch Löwdin.

## The law that governs changes: A.cert

### Two things a session must know before it searches
- **`spectra_raw` CONTAINS A DIRECTORY.** `spectra_raw/queue2/` holds 66 further level tables
  (R 1639) and is where all 24 of the store's species live. A listing of `spectra_raw` shows 92
  entries and one of them is that directory. **R 1672: I read the listing as the population and
  reported the archives disjoint. They are not — coverage is 24 of 24, 554 of 554.** A NEGATIVE
  RESULT FROM A SEARCH IS A STATEMENT ABOUT THE SEARCH UNTIL THE SEARCH'S SCOPE IS AUDITED.
- **The store is authoritative — M's ruling, session 1.7.3 (T6 CLOSED).** Each cell is a
  statistical value, and **all three perspectives are carried per cell, because each is a
  perspective of one definition** (median, mean, asymptotic). Where a cell holds one member the
  columns agree and are written, not refused: refusal belongs where an operation is UNDEFINED,
  never where its result is unsurprising. The bracket flag rides alongside as an EVIDENCE GRADE
  — NIST's interpolated levels are 1.9% of members and 74% of those are sodium (R 1675).
Four admitted operations and no fifth: **RELABEL · RE-COORDINATISE · REFINE A FIBRATION ·
DROP A COORDINATE**. *Add-a-coordinate is not admitted* — four attempts, four failures
(R 1581, 1599, 1602, 1608). A fibration must be decidable from **that coordinate alone**.

## The principles that bite most often
- **P5** compute the result before assuming it. **§2.14** compute, then write — *the most
  violated protocol in the book*, and the fault recurred four times in session 1.8 alone.
- **P8/§2.15** every failure is a true answer and therefore a bound; record what it excludes.
- **P22** a complete index converts deception into disagreement: error survives, concealment
  does not. **P23** completeness is a standing claim, held until a question arrives.
- **§2.8** two independent routes — an identity computed along one path is vacuous.
- **§2.9** refuse rather than coerce; no silent default. **§2.20** the Zeno directive: nothing
  runs unbounded; fetched literature is the single exception.
- **§H.10** the handoff begins at 90%, not at exhaustion. **§H.11** no tool call returns more
  than ~25 lines — a census is written to a file and reported by its shape; gates run at
  baseline and at close and otherwise only when something generated has changed; rulings that
  share a subject are batched. Both clauses were adopted from session 1.7.2's own accounting.

## The gates
`The_Method_1_6_audits.py` — 25 prime audits: LATTICE · EQUATIONS · CONSISTENCY · REDUNDANCY ·
ARTEFACT · COHERENCE · ATTRIBUTION · CELL · DISTINCTNESS · SCOPE · ANTECEDENT · MARKUP ·
AGREEMENT · ARITHMETIC · ENUMERATION · FIDELITY · MEASURE · REPRODUCTION · SEQUENCE ·
PROJECTION · INPUT · CENSUS · GRAPH · CYCLE · NOMENCLATURE.
`roundtrip.py` — 5 generated artefacts must regenerate identically: COMPENDIUM, INDICES,
PHYSICS, SPECTRA, REGISTER. **A write to COORDINATES.tsv is not complete until every artefact
generated from it has been regenerated** (learned R 1655).


## PART III — THE LAW, read in full (Ch. 14, 17, 18 and §18.4.1)

### Closure (Ch. 14)
`X` is closed iff `X = ℛ(X)`. **This is Bergman's double-projection theorem** specialised to
products of chains, itself a consequence of **Baker–Pixley (1975)** for any algebra with a majority
term. E(X)=0 is *global consistency* of a binary constraint network — **Montanari 1974**,
**Dechter 1992** (the book had been citing **Freuder 1982** for Dechter's theorem; corrected at
R 400). The constraint class is a **staircase** constraint (Deville, Barták & Van Hentenryck 1999).
So **E(Λ)=0 is the discovery that Λ is a sublattice**, and sublattices have been binary-determined
since 1975. ℛ is extensive, monotone, idempotent — 150/150. The book claims no novelty for the
machinery; the application is computing the closure defect *of an index*.

**Scope:** each coordinate must be presented as a chain. Bundling two chains into one non-chain
coordinate hides structure from ℛ.

**The seed.** No cell of Λ is removable — ℛ(Λ\{x}) = Λ for all 976. **seed(Λ₈) = 7, exact by
branch and bound** — a compression of 139:1. Prune-greedy said 10–13 for twelve cycles and every
law fitted to its output was fitted to its failures (§14.5.9; the protocol §2.24 *never one
heuristic* is what that earned). Laws now exact: a down-set seeds at d+c−1, a full box at d+c−2.
**seed = Carathéodory number + alphabet cost**, and the breadth of a product of d chains is d.
Every one of 219 minimum covers contains an s→s, s→p, p→s, p→p, a NULL (q=0) and a FULL (q=k)
transition — **the constraint is on the channel, not the cell.**

**The family of closed indexes is open.** Every member has E=0; the family is closed under
intersection, not union; **E(Cl(U)) = 2^|U| − |Cl(U)|**, i.e. ℛ(Cl(U)) is the entire power set.
The one index in this work whose cost of statement exceeds its content.

### Extension (Ch. 17) — the three operations and only three
- **E1 cells:** `Λ ∪ {x}` closed iff for every y, both x∨y and x∧y land in Λ ∪ {x}. 100%/288.
- **E2 axes:** `Λ × h` closed iff h is a lattice homomorphism. 100%/424. **Theorem 10.1 —
  adjunction never repairs:** a non-closed set cannot be repaired by adjoining any function of its
  coordinates. Three repair routes only: **enlarge, restrict, reorder.**
- **E3 constraints:** `{h ≤ q}` closed iff h(x∨y) ≤ q whenever h(x),h(y) ≤ q. 100%/2,513.
  **Admissibility belongs to the pair (h,q), not to h.** Meet never breaks it; only the join can.
  **Sums and products fail** because a join raises every coordinate at once.
  For a constraint on a *difference*: **δ⁻¹(T) is a sublattice iff T ∩ range(δ) is convex.**
- **§17.4 the repair procedure:** a sum bound cannot be imposed, but a sum can be **indexed** —
  replace (g₁,g₂) by (g₁, G=g₁+g₂). Price: it makes comparable some pairs that were incomparable.
  *Coverage and closure are available together; coverage, closure and the original order are not.*

### What the law forbids (Ch. 18)
- **Thm 11.1/11.2:** every lattice quantity is a deterministic function of the coordinates,
  *whatever formula the join takes*. No cleverer order carries what the coordinates do not; the
  escape is a further measurement, which is by definition a new coordinate.
- **§18.4 closure is not locally determined** — every proper projection can be a fixed point while
  the set fails. ~1 in 5 such sets fail. Closure is a d-dimensional condition.
- **§18.6 E(X) is the prediction budget.** The number of predictions an index can make is E(X).
  Periodic table 36 (all impossible), calendar 7 (all impossible), Λ 0. **An index may be complete
  or predictive; it cannot be both.** Prediction lives in the *value*, never the cell: the cell is
  indexed with nothing to predict, δ is the value's departure from what the index determines.

### §18.4.1 — THE LAW OF REALISED CLOSURE (A.cert's home; the second named law)
> **An open index does not close itself, except where a certificate exhibits an operation on its
> coordinate system reaching a fixed point of ℛ — and that certificate is the realiser.**

Admitted operations: **relabel values · re-coordinatise the same content · refine a fibration ·
drop a coordinate.** *If no certificate exists, nothing realises ℛ and the open half applies.*
**The realiser is exhibited, never found. What is falsifiable is the exhibition.** Certificates on
record: calendar E=7 → months relabelled by length → 0; periodic table E=36 → period = n+ℓ, block
order f,d,p,s → 0; audits E=16 → drop DEPTH → 0; nuclide chart E=9 → **none**; bibliography E=6 →
**none**, floor at 2 over 5,184 relabellings.
**In every closed row something can be named; in every open row nothing can.** E=0 is never a
property of an object alone — always of an object *plus* the structure realising its closure.
**Two levers (R 275): E falls as a fibration is refined and rises as coordinates are added.**
Corrected cap criterion: **an occupancy coordinate is admissible iff its cap is a MORPHISM for the
operation the index must preserve** (arity was a proxy and the proxy was mistaken for the
property). And: *a bound taken from the index's own extent gives its envelope and never its law.*

### Why this matters for the current work
Λ_spectra's two rules pass every test above: charge ≤ Z and mult = f(N) are single-argument
monotone bounds over chains, so both are meet- and join-morphisms; neither sums. Extending the Z
alphabet is a **relabel/re-coordinatise of the value set**, not an added coordinate — which is why
E did not move. The four failed extensions of R 1581–1608 each added a coordinate, which §18.4.1
does not admit and Theorem 10.1 says can never repair anything anyway.

## What was read, and what was not
**Reading is on demand, not a queue.** M's ruling, session 1.7.2: *reading will be done as
necessary.* The list below is a statement of record — it exists so a gap cannot close over
quietly (§H.8 C7) — and not a task with an owner. When a session reads to answer a question,
it extends this list with what it found.
READ IN FULL: front matter and the collaborator's note; Part 0 (preface); Part I §1 (principles
P1–P23) and §2 (protocols 2.1–2.20); the twenty-five audits by name; **Part III — Ch. 14 Closure
(incl. §14.5 the seed, §14.6 the family), Ch. 17 Extension (E1/E2/E3, §17.4), Ch. 18 What the law
forbids (incl. §18.4.1 the law of realised closure, §18.4.2 the n-body index, §18.6 the prediction
budget)**; each compendium's declaration and full heading structure; INDICES §"The spectra index";
SPECTRA §0 and §I (incl. the Janet collapse).
NOT READ, and named rather than glossed: Part II (Ch. 6–13, the construction of Λ), Ch. 15–16
(self-reference and self-defence), Ch. 19, Parts IV–VII (the languages, the method, the record,
the challenges — including Ch. 34 the Löwdin challenge), and all appendices; plus the bodies of
COMPENDIUM.md, INDICES.md, PHYSICS.md and SPECTRA.md. Roughly 150,000 words remain.

## Session 1.8.2 — carried into the digest (R 1685–1696)
- **A session states nothing about the work until it has read `DIGEST.md` (R 1685).** Two
  consecutive sessions opened by fabricating state; the clause is now REGISTERED, not merely bridged.
- **M's standing direction: everything needed is contained in the record.** Consult the register
  and §H before bringing a ruling; five of six pending rulings were answered by the record.
- **T2 CLOSED (R 1690):** the stored δ is the MEDIAN — declared in `spectra.py` §0, inside C3.
- **T7 CLOSED (R 1689):** the store's `mult` column stays; on language = jj its 0 is a NULL BY
  LANGUAGE (relabel), not a multiplicity. Authored rows not rewritten.
- **T10 CLOSED (R 1691):** duplicates → 1215a/1476a (the 368a precedent); audit 19's uniqueness
  guard reads {3,4} digits, one-space delimiter, can-fail verified. The ORDERING clause is NOT
  widened: 1165 sits after 1171 in the archive — history, not a fault. Audits line 213 holds a
  sibling 3-digit expression, named and untouched.
- **Board 4b CLOSED (R 1686):** temperature is a COLUMN of the value store, never an axis; closure
  cannot discriminate a free axis (product of lattices is a lattice) — the question is ADMISSION.
- **T8 CLOSED (R 1693–1696).** `store_gen.py` GENERATES the limit: parent-matched · forced ·
  positional (NIST table convention, a reading) · UNWITNESSED (M's wording: needs a witnessed
  measurement science has yet to provide — a named bound). 145 voided → 145 unwitnessed; 222
  fallback → 117 forced + 108 positional. NIST ordinal rules letter-prefixed parents (M).
  **T8-J open, owner M:** may a J-resolved parent borrow the parent ion's own level table?
- **THE INDEX CLOSES AT Z = 120, E = 0, WITH 119 AND 120 PRESENT (R 1696) — no rebuild.** And
  the instrument warning: `mult` is a FIBRATION over N; a raw join/meet on 4-tuples is the wrong ℛ.
- **COMPENDIUM L767 stands as history (§H.4, R 1688)** — the bridge is the saying-so.

## Session 1.8.3 — carried into the digest (R 1697–1700)
- **R 1685 broke a third time (R 1697).** The opening turn arrives before the bank does; the fix is
  procedural: acknowledge the directives, state NOTHING about the work until the upload lands.
- **T8-J: M ruled YES; applied NARROW (R 1699).** `store_gen.py` fifth status `ion-derived (T8-J)`:
  limit(J) = printed limit(J₀) + ion fine-structure offset, ion table read from disk. Unwitnessed
  162 → 147. Kr II not on disk. **The WIDE form (limit = IE + E_ion(parent), 145 rows) and the
  LADDER form (267 ground-parent ladders with no Limit row, R 1590's premise) are the same second-
  source operation and are M's to widen — not regexed.**
- **No series constructor existed; `series_gen.py` is it (R 1700).** Validated two-route against
  the store: 485/485 members, 351/351 medians. Reading list: 1,564 rows staged in
  `captures/READING-LIST-STAGING.tsv`, 327 true series, **93 not in the store on 62 cells** —
  nothing written to the store yet. **T9's 65 no-member series do not exist as printed keys in
  raw: a 1.7 staging fault, not a store fault.**
- **Rebuild REGISTER.md by `python3 register_gen.py > REGISTER.md`** — running the generator
  without redirect leaves the held copy stale and fails C3 (repeated this session; caught by the gate).
