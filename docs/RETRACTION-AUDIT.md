# RETRACTION-AUDIT — do withdrawn figures still stand in the volumes?

`PROSE-ONLY.tsv` showed that 212 corrections were made in conversation and never written into the
repository. This asks the consequent question: **for each of those corrections, is the superseded
value still standing in a published volume?**

`RETRACTION-AUDIT.tsv` is the standing list — 303 rows, one per (correction, number) pair.
**Nothing has been repaired.** Filed for R3.

## Method

1. **Candidate generation (mechanical).** From each of the 212 `CORRECTION` rows, extract every
   distinctive number (≥3 significant digits, or decimal, or thousands-separated). Search the nine
   live volumes for each. **124 of 212 corrections had at least one number that occurs in a volume**
   — 303 pairs.
2. **Adjudication.** Each pair went to a subagent with the correction quote *and* ±260 characters of
   the volume text around the number, to assign one of four verdicts. Agents were told to use
   `CANNOT-TELL` freely rather than guess, because a `LIVE-SUPERSEDED` verdict is a claim about a
   published volume.
3. **Verification (here, not delegated).** Every `LIVE-SUPERSEDED` was re-checked directly against
   the volumes.

## Result

| verdict | rows | meaning |
|---|---:|---|
| UNRELATED | 187 | digit coincidence — a different quantity, a register id, a page or year |
| CORRECTLY-UPDATED | 87 | the volume already carries the replacement value |
| **LIVE-SUPERSEDED** | **19** | the volume asserts the withdrawn value as current |
| CANNOT-TELL | 10 | context too thin to decide |

**87 corrections did land.** That is the reassuring half: in most cases where a correction's numbers
appear in a volume, the volume has the corrected form — often printing the retraction explicitly
(*"an earlier version of this work reported 735,091 ± 1,398"*, *"Withdrawn, and recorded in
Chapter 28"*, register 1493's *"WARNING: The cancellation reading in this entry is REFUTED at
register 1494"*).

That convention is what makes the 19 legible: **the corpus marks a withdrawn entry when it knows.**

## The verified case — 2,475, in the main volume

The strongest finding, and the only one I can demonstrate from a single file. `The_Method_1_6-2.md`
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

## The register cases, and the strength of the evidence

The other 17 flags rest on **register entries** rather than measured values: the matched number is an
entry id, and the claim is that the entry still asserts what a conversation withdrew. That is weaker
evidence than the 2,475 case, so it was checked a second way.

The Register marks superseded entries. Of the 12 flagged entries that exist:

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
- **`PO-0087` / registers 500, 502** — the main volume's §14.5 withdraws registers 497–500 and 502,
  but those entries stand unmarked in the Register. Again: volume against volume.
- **`PO-0145`** — registers 1595 and 1628 still carry the fetch-cache explanation the correction
  withdrew.

## An error caught in verification, worth recording

For `PO-0190` an agent reported the live claim in `The_Method_1_6-2.md`, quoting *"the unique
dimension at which time exists"*. That phrase **does not occur in the main volume**; it is in
`The_Method_1_6___Mathematical_Compendium-2.md`. Right finding, wrong volume. The `volume` column in
the TSV carries the agent's attribution as given — treat it as a pointer to check, not as located
evidence.

## What this does not establish

- **Absence of a number is not clearance.** Only numeric fingerprints were searched. A correction
  that withdrew a *claim* carrying no distinctive number cannot be found this way — and 88 of the
  212 corrections had no number in any volume at all, so they are simply untested here.
- **`UNRELATED` is a judgement, not a proof.** 187 rows were dismissed as digit coincidence on ±260
  characters of context. Spot-checking is cheap: the row carries the quote and the volume name.
- **The register-entry cases are inference.** An unmarked entry asserting a withdrawn claim is strong
  circumstantial evidence and nothing more. Each needs the entry read in full before repair.
- **No repair was made anywhere.** The chat-67 full hold governs.

## Re-verification

```bash
# the one case that needs no interpretation
grep -c '2,475' method/members/The_Method_1_6-2.md          # 3
grep -o '[^.]\{0,120\}2,475[^.]\{0,120\}\.' method/members/The_Method_1_6-2.md

# does a flagged register entry carry a withdrawal marker?
python3 - <<'EOF'
import re, pathlib
t = pathlib.Path('method/members/The_Method_1_6___The_Register-2.md').read_text(errors='replace')
p = re.split(r'\n### (\d+)\n', t); e = {int(p[i]): p[i+1] for i in range(1, len(p), 2)}
M = re.compile(r'WITHDRAWN|WARNING|REFUTED|SUPERSEDED|RETRACTED|DEACTIVATED', re.I)
for n in (230, 314, 502, 599, 602, 807, 1148, 1395, 1461, 1595, 1628):
    m = M.search(e[n][:1500]) if n in e else None
    print(f'{n:>5}  {"MARKED: " + m.group(0) if m else "-- unmarked --"}')
EOF
```

## Columns

`id` (the `PROSE-ONLY.tsv` row), `number`, `verdict`, `confidence`, `volume` (as attributed by the
adjudicator — verify before use), `reason`, `register_entry_marker` (my check, on LIVE-SUPERSEDED
rows only), `correction_label`, `correction_quote`, `conversation`, `conversation_title`, `msg`.
