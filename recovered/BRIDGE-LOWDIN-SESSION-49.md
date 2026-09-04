# BRIDGE — LOWDIN SESSION 49

Open Session 50 with **`bash open49.sh`** and nothing else. It enforces what this session had to
learn the hard way. Everything below is DERIVED in s49 or RECALLED and flagged. The only number
ever entered into this chain remains **c = 137.035999**.

---

## §1 · WHAT SESSION 49 DID

The walk ran **Z=76 → 102, twenty-seven steps**, closing the 5d block, the 6p block, the 7s pair,
the actinide opening and the 5f shell. The chain stands at **101 rows, Z = 2..102**, every step at
rung 0. Three prediction files were filed BEFORE their runs and scored. Two standing directives
were written and enforced in instrument form.

    scores at 101 rows      STEP (`ok`) 92/101      CONFIG 68/101
    FIRST STEP DIVERGENCE   25 — unmoved across all twenty-seven steps

---

## §2 · THE PHYSICS RESULT OF THE SESSION — THE ORDERING CLAUSE HAS NEVER FAILED

Filing PREDICTION-OPENINGS-89 forced a correction that earlier sessions had carried wrongly.
**La(57) was described as "where the ordering fails". It is not an ordering failure.** 5d and 4f
both carry n+ℓ = 7; La is a TIE-BREAK failure. The same is true of Ac(89), where 6d and 5f both
carry n+ℓ = 8.

**In 101 rows the ORDERING clause has not failed once.** The TIE-BREAK clause stands at:

    HELD   4s/3d   4p/5s   4d/5p   6p/7s        — every s, p or d pair
    FAILED 4f/5d (La 57)   5f/6d (Ac 89)        — both f openings, and only those

**And the mechanism is now measured, not named.** 5f sat pinned at −0.0313 Ha for nine protons
(Z=81..89, moving 3×10⁻⁵), then fell to −0.13689 at Th(90) and −0.30535 at Pa(91) — a factor of
three thousand in step size across two protons. It crosses 6d between 90 and 91 and takes the
electron at 91, the record's own element.

> **The tie-break clause presupposes that the channel exists in the field. An uncollapsed f
> channel does not. Orbital collapse decides when an f channel starts existing, and that — not a
> defect in n+ℓ — is what stands between the rule and the record at La and Ac.**

Second physics finding: **the margin widens monotonically with Z**, 0.19 at Os to **0.52 at
No(102)**, the widest in the chain. The ordering becomes LESS ambiguous down the table, not more.
The anomalies at the bottom are promotions inside a decided ordering, never contests over which
channel wins.

---

## §3 · M'S RULING — THE EVIDENTIARY BOUNDARY IS Z = 108

Carried verbatim in `RULING-EVIDENTIARY-BOUNDARY-108.md`:

> "The Löwdin solution will be derived solely from the 108. 109 to 120 will be predicted and
> stated as such, based on the Löwdin solution, which will give future researchers values to
> test once our tech allows us to witness and measure the continued spectra."

Configurations above 108 are themselves derived, often FROM Madelung. Scoring against them would
read our own premise back as confirmation. The derivation's support is **107 steps, Z = 2..108**;
rows above carry `prov = PREDICTED`, are reported in a separate table, and enter no denominator.
Mixing them into one denominator is a fault.

---

## §4 · PREDICTIONS FILED AND SCORED

**PREDICTION-5dBLOCK-72-80 — 7 of 7 HELD.** PD-6's two integers filed exactly: ok (71,79),
cfg (58,79). First time both columns were predicted to the integer. PD-4 held: cfg matches where
ok fails, third occurrence, at Hg(80) — structural, as filed.

**PREDICTION-6pBLOCK-81-88 — ALL HELD.** The n+ℓ=7 tie-break tested at a fourth distinct pair:
6p opened before 7s, lower n first, with 6p full at Rn(86) and 7s taking 87 at −0.13186 over
6d(−0.06232) and 5f(−0.03129). PE-5 filed (79,87) and (66,87); both exact.

**PREDICTION-OPENINGS-89 — PF-1, PF-2, PF-4, PF-6 HELD. PF-5 FAILED by one element.** cfg parted
from the record at 91, not 92: Pa's record is 5f2 6d1 7s2 against Th's 6d2 7s2, so the promotion
is INSIDE the first 5f step. The walk is one 5f behind AND one 6d ahead — two offsets where the
lanthanide block had one, which is why the Gd(64) cfg-passes-where-ok-fails structure did NOT
repeat at Cm(96).

**PREDICTION-5fCLOSE-97-108 — filed, PG-1/2/3 held at 97..102, six of twelve steps run.**
Live at open: PG-4 (Lr 103, record says 7p, walk must say 5f), PG-5, PG-6, PG-7, and PG-8's
terminal integers **ok (97,107)** and **cfg (68,107)** — the final scores of the derivation.

---

## §5 · FAULTS — ALL FOUR ARE MINE, AND ALL FOUR ARE NOW MACHINE-BLOCKED

**F49.1** — `ok_fail` was declared chain-length-invariant; Hg(80) falsified it. RECLASSIFIED
PREFIX-invariant on the same two binding conditions as cfg_fail. Mechanism named: the walk cannot
vacate 6s2.

**F49.2 — I DISOWNED MY OWN WORK.** Met chain rows I did not remember producing, declared an
"unattributed append", quarantined a correct file and began recomputing a block. The rows
reproduced IDENTICALLY on every non-timing field. Cause: a LOST TOOL RESULT — a process that ran
to completion while the call that launched it returned an error. I had used my memory of acting
as the test of provenance.

**F49.3 — I DECLARED A COLD START IN A LIVE SESSION.** Three turns after writing F49.2's remedy
as a practice, I told M this was "Session 45, cold start, no runtime" while the runtime I had
built that chat sat live at 79 rows. **A practice that depends on my remembering to apply it
fails by the exact mechanism it exists to correct.** Hence the law.

**F49.4 — ZENO VIOLATED BY UNBOUNDED SLEEP.** I held long waits inside tool calls; two died.
Repaired at the instrument: `run.sh --wait TAG SECONDS` is a bounded segment that ALWAYS returns.

**Container restart, 20:5x.** Killed a detached job mid-row. Cost: ONE row. The receipts and the
state card resolved it in two calls with no quarantine and no re-verification. Clause 3a added:
detached jobs survive a lost tool result but NOT a restart; after any gap, recompute only units
with no completion line, never the block.

---

## §6 · THE TWO DIRECTIVES, AND WHY BOTH WERE NEEDED

`PRIME-CONTINUITY-DIRECTIVE.md` is carried verbatim and stands with the Prime Handoff and Prime
Zeno directives. Six clauses, of which the load-bearing three:

1. **My recollection is not evidence, in either direction** — not that work WAS done, not that it
   was NOT done. The record has standing: manifests, provenance fields, ledger, reproduction.
2. **Nothing is said about state until `prime.py` has run in the same turn.** The STATE CARD is
   the only admissible source. No card read this turn → the answer is "I have not read the
   record", never a recollection.
3. **Every run is launched through `run.sh`**, which detaches it, writes a receipt and appends to
   `SESSION-LEDGER.tsv`, so a lost result is recovered by READING, never by recalling.

Neither directive alone was sufficient and today proved it twice: Continuity keeps the work when
the tool call is lost; Zeno keeps the tool call from having to outlive its segment.

**Instruments, all can-failed in both directions:** `prime.py` (STATE CARD, exit 1 real fault /
2 unreceipted), `run.sh` (launch, `--wait`, `--poll`, `--list`), `continuity.py`, `open49.sh`.

---

## §7 · GATES

Gates 1..71 diffed to **ZERO** against sealed GATES-48-OPEN.log — gate 6 `sec` did not even
drift. 72 PT8 dsum ≤ 2.78e-17. 77: 0 UNSAFE. 79+80 PASS. 84 PASS. **Gate 83 restated for 101
rows**: cfg_score (68,101), ok_score (92,101), cfg_first 24, ok_first 25. Its `cfg_fail`,
`ok_fail` and `disagree` are PREFIX-invariant; every append this session sat above the previous
extension point and every one was named in advance in a filed prediction.

---

## §8 · ORDERED WORK LIST FOR SESSION 50

1. **`bash open49.sh`.** Not the old recipe. It halts on any failed step and prints the STATE CARD
   before anything may be said about state.
2. **Walk Z=103..108 under PREDICTION-5fCLOSE-97-108, already filed.** Two rows per job,
   `run.sh` + `--wait`. **PG-4 at Lr(103) is the sharp one**: the record opens 7p (n+ℓ=10) while
   an n+ℓ=8 channel is still open in the walk. PG-4 says the walk holds 5f and `ok` fails. If the
   field instead follows the record there, that is an ordering violation larger than anything in
   101 rows and it must be registered as such, not explained away.
3. **At Z=108 the derivation is COMPLETE — 107 steps.** Score PG-8's two integers. Restate gate 83
   a final time for the derivation's length.
4. **Then, and only then, walk 109..120 as OUTPUT.** `prov = PREDICTED`, separate table, no
   scoring, published with channel depths and margins so each is testable.
5. Deferred, and not on the n+ℓ path per M's ruling: the −8.021 mHa residue at Z=59, the coupled
   4f2·5d SO check, the promotion operator as an object. All three are the Cr(24) class.
6. Cheap and owed: the period-length sequence 2, 8, 8, 18, 18, 32, 32 falls out of the n+ℓ
   diagonals as 2m², m = ⌊(k+1)/2⌋ — verified arithmetic, parameter-free, and it is Löwdin's
   second deliverable. It is downstream of the ordering and must be stated as such.
7. **T4 (R 1701 onward) — LAST. Not opened in any working session.**

Bank restore-point-2_13 (R 1700) untouched throughout s49.
