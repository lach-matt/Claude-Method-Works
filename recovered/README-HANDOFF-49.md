# LOWDIN-HANDOFF-49 — single superset archive (session 49). Supersedes HANDOFF-48.

**OPEN WITH `bash open49.sh` AND NOTHING ELSE.** It runs seals → runtime → STATE CARD → smoke
gates, halts on any failure, and launches the full gate replay DETACHED. The old hand-typed
recipe is superseded because s49 proved it does not prevent the faults below.

## THE THREE LAWS THIS ARCHIVE ENFORCES

**PRIME CONTINUITY (§H.0, `pack49/PRIME-CONTINUITY-DIRECTIVE.md`, carried verbatim):**
1. My recollection is not evidence, in EITHER direction — neither that work was done nor that it
   was not. The record has standing: manifests, provenance fields, ledger, reproduction.
2. **Nothing is said about state until `prime.py` has been run in the same turn.** The STATE CARD
   is the only admissible source. No card → "I have not read the record", never a recollection.
3. Every run is launched through **`run.sh`** — detached, receipted, ledgered. A lost tool result
   is then recovered by READING, never by recalling.
4. Unexplained state is CONTINUITY until proved otherwise. Reproduce ONE object, never the block.
   Quarantine is the last resort.
5. When the record and my account disagree, the presumption is that MY ACCOUNT IS WRONG.
6. Nothing asserted before the bank is read (the mirror fault, R 1685).

**PRIME ZENO, at the instrument:** `bash run.sh --wait TAG SECONDS` is a bounded segment that
ALWAYS returns before the tool limit. Long waits are NEVER held inside a tool call (F49.4).
Clause 3a: detached jobs survive a lost tool result but NOT a container restart — after any gap,
recompute only units with NO completion line in the job log. Never the block.

**M'S BOUNDARY RULING:** the derivation is Z = 1..108, 107 steps. 109..120 are OUTPUT, labelled
PREDICTED, in a separate table, in no denominator.

## Verify

`bash verify49.sh` — expect **bad=0 extra=0, BOTH halves** (F43.1: integrity AND completeness).
The exact ok= count is deliberately not written here (F48.1); read it off the run.
Can-fail: `touch pack49/PLANTED && bash verify49.sh` -> extra=1, exit 1. Remove it after.

## Runtime

`open49.sh` rebuilds it if absent: packs 5..49 layered in strict numeric order, extensions
`py jsonl c json sh` (F38.1 — `.json` is load-bearing; `.sh` is new in 49 for `run.sh`), then the
three kernels compiled. CHECK, do not assume:

    wc -l rt/nlchain.jsonl    -> 101    (Z = 2..102)

## State

Chain **101 rows, Z=2..102**, all rung 0. 5d, 6p, 7s, the actinide opening and 5f all closed this
session — twenty-seven steps. **STEP 92/101, CONFIG 68/101, FIRST STEP DIVERGENCE 25 — unmoved.**

**The ordering clause has never failed in 101 rows.** La(57) and Ac(89) are TIE-BREAK failures,
not ordering failures — 5d/4f and 6d/5f each share n+ℓ — and both are the f channel not yet
collapsed: 5f moved 3e-5 across nine protons, then 0.105 in one, then 0.168 in the next.

Work list is §8 of `pack49/BRIDGE-LOWDIN-SESSION-49.md`. **T4 (R 1701 onward) is LAST.**