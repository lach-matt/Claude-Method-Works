# RETRACTION-AUDIT — do withdrawn figures still stand in the volumes?

`PROSE-ONLY.tsv` showed that 212 corrections were made in conversation and never written into the
repository. This asks the consequent question: **for each of those corrections, is the superseded
value or claim still standing in a published volume?**

`RETRACTION-AUDIT.tsv` is the standing list — **391 rows**, one per (correction, number) pair in the
numeric pass and one per correction in the claim pass. **Nothing has been repaired.** Filed for R3.

## Two passes, and neither alone is enough

| pass | scope | rows |
|---|---|---:|
| **numeric** | every distinctive number in a correction, fingerprinted against the nine live volumes | 303 |
| **claim** | the 88 corrections whose numbers appear in no volume, adjudicated on the claim itself | 88 |

1. **Candidate generation (mechanical).** From each of the 212 `CORRECTION` rows, extract every
   distinctive number (≥3 significant digits, or decimal, or thousands-separated). Search the nine
   live volumes for each. **124 of 212 corrections had at least one number that occurs in a volume**
   — 303 pairs. The remaining **88** carried no number in any volume and became the claim pass.
2. **Adjudication.** Each row went to a subagent with the correction quote *and* the volume text
   around the match, to assign a verdict. Agents were told to use `CANNOT-TELL` freely rather than
   guess, because a `LIVE-SUPERSEDED` verdict is a claim about a published volume.
3. **Verification (here, not delegated).** Every `LIVE-SUPERSEDED` was re-checked directly against
   the volumes, and every `CANNOT-TELL` was read again. Six numeric rows were resolved on that
   second reading; one claim row changed grade and one changed its reason entirely.

## Result

| verdict | numeric | claim | total | meaning |
|---|---:|---:|---:|---|
| UNRELATED | 187 | — | 187 | digit coincidence — a different quantity, a register id, a page or year |
| CORRECTLY-UPDATED | 90 | 52 | 142 | the volume already carries the replacement |
| NOT-IN-VOLUMES | — | 29 | 29 | the claim is nowhere in the nine volumes — **see the scope limit below** |
| **LIVE-SUPERSEDED** | **21** | **4** | **25** | the volume asserts the withdrawn value or claim as current |
| CANNOT-TELL | 4 | 3 | 7 | genuinely two-sided; the volume both corrects and retains |
| CORRECTION-SUPERSEDED | 1 | — | 1 | the *correction* is the stale record, not the volume |

**142 corrections did land.** That is the reassuring half: in most cases where a correction is
traceable into a volume, the volume has the corrected form — often printing the retraction explicitly
(*"an earlier version of this work reported 735,091 ± 1,398"*, *"Withdrawn, and recorded in
Chapter 28"*, register 1493's *"WARNING: The cancellation reading in this entry is REFUTED at
register 1494"*, §14.5.10's *"this section first said otherwise"*).

That convention is what makes the 25 legible: **the corpus marks a withdrawn entry when it knows.**

## The verified case — 2,475, in the main volume

The strongest finding, and the only one demonstrable from a single file. `The_Method_1_6-2.md`
contains three occurrences of `2,475`:

> *"The tight K has two parents and costs the cylinder **2,475 cells**."*

> *"§A.15 and register 230 record what it costs, **2,475 cells** of the cylinder."*

> *"…it breaks the factorisation by **15,150 cells at Λ₁₂ and 45,450 at Λ₁₃**, 21.4% and 22.8% of
> the product — recomputed; **the 2,475 previously printed here is withdrawn**."*

**The volume prints its own withdrawal in one passage and asserts the withdrawn figure in two
others.** The correction says the price was wrong by roughly a factor of six. The phrase *"previously
printed **here**"* is the tell: the passage being edited was fixed, and the two other sites were not.

This needs no external evidence. It is a self-contradiction inside one published volume, and it is
`PO-0019` / `PO-0080` in `PROSE-ONLY.tsv`.

## The four claim-pass cases, each re-checked here

The claim pass found only four, and each was verified against the volumes directly rather than taken
from the adjudicator. Two came back stronger than graded, one came back with a different reason.

- **`PO-0081` — the closure rule is printed one-sided, and the operator is two-sided (HIGH).**
  *"A tightening preserves E = 0 if and only if it binds one coordinate by a monotone function of one
  other"* stands unmarked at **four live sites** — `Transitions.md` §1.8 (L202), the main volume's
  Appendix F.4.3 table (L11379, `A.rule`), the Index of Indices (L2022) and the Mathematical
  Compendium (L516). **Register 402 states the correction outright**: *"THE CLOSURE RULE WAS ONE-SIDED
  AND THE OPERATOR IS TWO-SIDED — φ̂ runs over ordered pairs, so a band closes at E = 0 where the
  stated rule refuses it."* No withdrawal marker within three lines of any of the four. Raised from
  MEDIUM. `DEFERRED.md` docket 9(a) touches L11379, but for a *pointer* fault (which section prints
  the form), not for the rule being one-sided.

- **`PO-0158` — "not a lattice" where only "not a sublattice of the product" was shown (MEDIUM).**
  Main L3375 prints *"The exact coupling region is not a lattice in any presentation tried"* over five
  componentwise meet/join failure counts, unmarked, and the three-body paper repeats it as Law 3
  (*"Therefore the exact three-body region is not a lattice"*, L79 and L157). Componentwise failure
  refutes sublattice-hood of the product, not lattice-hood — a distinction the corpus holds elsewhere
  (`READ-ch16b.md`: *"zero join leaks, zero meet leaks — Λ₈ is a sublattice"*; MC L516: *"the index is
  a sublattice of a product of chains"*). Not docketed: `WORKING-REGISTER.md` W-101's *"not a lattice"*
  is a different object (max/min as a homomorphism).

- **`PO-0013` — the seven constraints' correlation (HIGH), already docketed.** Main L2049 prints
  *"The correlation is not a coincidence: all seven constraints descend from two origins"* unmarked,
  while the Mathematical Compendium carries the corrected cause — two decreasing functions of one
  width variable, Chebyshev's sum inequality, *"positive for this reason and no other"*. **Already
  recorded as finding `10-04` in `READ-ch10.md`.**

- **`PO-0091` — "the whole tower", and the most interesting row in the file (MEDIUM).**
  *"The shortfall of one level holds for the whole tower and not only for a K₃"* stands unmarked at
  main L5751 (the Figure 21.1 caption) and L5773 (§21.5.3's table), and Register 1953 repeats it. The
  same caption says *"The base Λ₈ is a caterpillar"* and that each two-parent axis adds a cycle from
  Λ₁₀ onward; MC L1644 gives Λ₈ as *"8 nodes, 7 edges, a caterpillar; treewidth 1"*, and MC L1324
  states **treewidth 1 ⟺ exact closure under ℛ**. So by the volumes' own figures ℛ is exactly
  sufficient at Λ₈, not one level short.

  **But the adjudicator did not have this:** register **1790**, a *banked correction*, re-asserts the
  scope — *"its treewidth is still 2, so §21.5.1's **ONE-LEVEL SHORTFALL STANDS** … now inside the
  tower itself and not only in the bracket"* — while its own stage table gives cycle rank
  `(0, 0, 1, 1, 2, 2)`, i.e. Λ₈ and Λ₉ carry no cycle and are trees. **A later correction and the
  volume agree with each other and disagree with the correction's own data.** Confidence is held at
  MEDIUM for that reason, and this row is the one an R3 reader should open first.

  Docketing is *partial and for different fields*: register 1790 and the chat-81 `WORKING-REGISTER`
  entry already own the Figure 21.1 caption — for node count, edge count, girth, radius, leaves and
  the triangle. **Neither touches the tower-wide scope, which 1790 endorses.**

## The register cases, and the strength of the evidence

Most numeric flags rest on **register entries** rather than measured values: the matched number is an
entry id, and the claim is that the entry still asserts what a conversation withdrew. That is weaker
evidence than the 2,475 case, so it was checked a second way. The Register marks superseded entries.
Of the 12 flagged entries that exist:

| register | withdrawal marker present? |
|---|---|
| 1395 | **yes** — `WARNING` |
| 230, 314, 502, 599, 602, 807, 1148, 1461, 1595, 1628 | **none** |

**Eleven flagged entries carry no marker of any kind**, in a Register that demonstrably marks
elsewhere. That is corroboration, not proof: the convention is not provably universal, and an entry
could be superseded by a *later* entry without the earlier one being annotated. Register 1395 having
a `WARNING` is the useful counter-example — it shows the check can come out the other way, and it
downgrades `PO-0128` accordingly.

Highest-value register cases, all in `The_Method_1_6___The_Register-2.md`:

- **`PO-0105` / 0.922 (HIGH)** — the entry still asserts `k = 0.9220 ± 0.0324 … and k = 1 is EXCLUDED
  at t = −2.41` as a standing finding; the correction voids that functional form.
- **`PO-0026` / register 602** — still prints *"219 distinct minimum covers; the same four cells
  appear in every one"*. Exact enumeration gives **24,585** covers with only corner 3 common. The
  Mathematical Compendium **has** been updated (it carries 24,585 and calls 219 a biased sample) —
  so the two volumes now disagree with each other.
- **`PO-0087` / registers 500, 502 (500 raised to HIGH here)** — the main volume's §14.5 withdraws
  registers 497–500 and 502, but those entries stand unmarked in the Register, 500 still stating
  `κ = 0.2506·S − 0.765` at `+0.980`. Again: volume against volume.
- **`PO-0051` / register 1450 (raised to HIGH here)** — Kitagawara appears **0** times in the Register
  or the main volume; Belokolos **8**. The priority misattribution stands and the correcting citation
  is absent.
- **`PO-0145`** — registers 1595 and 1628 still carry the fetch-cache explanation the correction
  withdrew.

## A category the audit did not start with: `CORRECTION-SUPERSEDED`

`PO-0006` says the Register does not begin at entry 1. It does — **Ruling 66 later seated the genesis
block flat.** The chat correction is the stale record and the volume is right. One row, and it is a
warning about the whole exercise: **an unbanked correction can itself have been overtaken.** A row in
`PROSE-ONLY.tsv` is a candidate for R3, never an instruction to it.

## An error caught in verification, worth recording

For `PO-0190` an agent reported the live claim in `The_Method_1_6-2.md`, quoting *"the unique
dimension at which time exists"*. That phrase **does not occur in the main volume**; it is in
`The_Method_1_6___Mathematical_Compendium-2.md`. Right finding, wrong volume. The `volume` column in
the TSV carries the agent's attribution as given — treat it as a pointer to check, not as located
evidence. The exception is the four claim-pass `LIVE-SUPERSEDED` rows, whose volumes and line numbers
were re-located here by hand.

## What this does not establish

- **`NOT-IN-VOLUMES` is not "not in the repo".** The claim pass searched the **nine live volumes**
  only. Several corrections' audit trails live in `WORKING-REGISTER.md`, `READ-ch*.md`, `DOCKET.md`
  and `DEFERRED.md` — members deliberately outside the nine — so a `NOT-IN-VOLUMES` row may be fully
  recorded in the governance tree. Check there before treating one as a gap.
- **`already_docketed` is two different things.** On the four claim rows it is my own hand check
  against `READ-*.md`, `DOCKET.md`, `DEFERRED.md`, `WORKING-REGISTER.md`, `RULINGS-R2.md` and
  `MAIN_AUDIT.md`. On numeric rows it is a **bare number-string search** over those same files and is
  labelled `number string seen in:` for that reason — it says the digits occur there, **not** that the
  finding is docketed. Do not quote a numeric row's value as "already known".
- **Absence of a number is not clearance.** The numeric pass can only find corrections carrying a
  distinctive figure; the claim pass covers the rest, but on inference rather than fingerprint.
- **`UNRELATED` is a judgement, not a proof.** 187 rows were dismissed as digit coincidence on ±260
  characters of context. Spot-checking is cheap: the row carries the quote and the volume name.
- **The register-entry cases are inference.** An unmarked entry asserting a withdrawn claim is strong
  circumstantial evidence and nothing more. Each needs the entry read in full before repair.
- **The TSV is a record, not a regenerable artefact.** It was produced from a chat corpus pass whose
  intermediate results do not survive the session. Re-verify rows; do not expect to rebuild the file.
- **No repair was made anywhere.** The chat-67 full hold governs.

## Re-verification

```bash
# the one case that needs no interpretation
grep -c '2,475' method/members/The_Method_1_6-2.md          # 3
grep -o '[^.]\{0,120\}2,475[^.]\{0,120\}\.' method/members/The_Method_1_6-2.md

# PO-0081: the one-sided rule, four live sites, and the register that corrects it
grep -rn 'binds one coordinate by a monotone' method/members/*.md    # 4 sites, none marked
grep -n 'THE CLOSURE RULE WAS ONE-SIDED' method/members/The_Method_1_6___The_Register-2.md

# PO-0091: the scope claim, and the caption that contradicts it
grep -rn 'whole tower and not only for a K' method/members/*.md
grep -n '8 nodes, 7 edges, a caterpillar' method/members/The_Method_1_6___Mathematical_Compendium-2.md
grep -n 'ONE-LEVEL SHORTFALL STANDS' method/members/The_Method_1_6___The_Register-2.md   # register 1790

# PO-0158: the inference, in the main volume and in the three-body paper
grep -rn 'is not a lattice' method/members/*.md

# does a flagged register entry carry a withdrawal marker?
python3 - <<'EOF'
import re, pathlib
t = pathlib.Path('method/members/The_Method_1_6___The_Register-2.md').read_text(errors='replace')
p = re.split(r'\n### (\d+)\n', t); e = {int(p[i]): p[i+1] for i in range(1, len(p), 2)}
M = re.compile(r'WITHDRAWN|WARNING|REFUTED|SUPERSEDED|RETRACTED|DEACTIVATED', re.I)
for n in (230, 314, 500, 502, 599, 602, 807, 1148, 1395, 1461, 1595, 1628):
    m = M.search(e[n][:1500]) if n in e else None
    print(f'{n:>5}  {"MARKED: " + m.group(0) if m else "-- unmarked --"}')
EOF
```

## Columns

`id` (the `PROSE-ONLY.tsv` row), `pass` (`numeric` / `claim`), `number` (or `(claim, no number)`),
`verdict`, `confidence`, `volume` (as attributed by the adjudicator — verify before use, except on
the four claim `LIVE-SUPERSEDED` rows, re-located by hand), `already_docketed` (see the caveat above),
`reason`, `register_entry_marker` (my check, on numeric LIVE-SUPERSEDED rows only), `correction_label`,
`correction_quote`, `conversation`, `conversation_title`, `msg`.
