# F64.2 — A CHAIN ROW IS INDIVISIBLE AND SO IS NOT UNDER THE PRIME DIRECTIVE
# Raised 2026-08-20T20:04Z, SESSION 64, during the F63.2 re-run at Z=89.
# REPAIRED THIS SESSION. The repair is `pack64/tbstep.py` and it was can-failed
# against the sealed instrument before any row was scored on it.

## WHAT HAPPENED
Twice.

1. The four rows were first launched detached (`pack64/tb64.sh`, 19:52:17Z). The
   container terminated the background process between calls. Z=57 had COMPLETED —
   its full record was on disk in `.row57.tmp` — and was lost from the driver's
   accounting because the process died between the solve and the append.
2. Re-run in the foreground, Z=57 (108 s) and Z=58 (119 s) completed. **Z=89 did
   not.** It was killed at the wall-clock limit after ten of its fourteen channels
   had converged. Every one of those ten was discarded.

## THE DEFECT, NAMED PRECISELY
`nlchain.py restart Z` is ONE PROCESS PER ROW. It holds all fourteen channel solves
in a single unit of work that either completes or returns nothing. **A row is
therefore an atom that this project's own prime directive (§2.20) forbids: it does not
divide, it does not write intermediate results, and a rerun costs the whole row over
again including everything that had already succeeded.**

At Z <= 40 this never showed. Each row fitted a budget and the atom was never tested
against one. At Z = 89 the row is 310 s of compute across fourteen channels and it
does not fit, so the defect that was always there became visible. **This is a defect
of the harness, not of the physics, and it costs only time — but it costs it
repeatedly and silently, which is the shape §2.20 exists to prevent.**

## THE REPAIR
`pack64/tbstep.py`. It divides the row at its natural seam — the channel — and:
  * solves the reference once, caching E_ref, its iteration count and its guard rung
  * solves each channel in turn, **writing the cache before the next begins**, by
    atomic replace so a process killed mid-write cannot corrupt it
  * stops when its declared budget is spent and reports PARTIAL with what remains
  * assembles and emits the row ONLY when every channel is resolved
A rerun costs exactly the channels that have not succeeded. Z=89 was completed in two
slices of 240 s; Z=91 in one.

**IT DOES NOT TOUCH THE INSTRUMENT.** It calls the same sealed functions —
`nlchain.candidates`, `nlchain.add`, `nlchain.tagof`, `nlguard.run_guarded`,
`ground.expand` — with the same arguments in the same order, and assembles the record
with the same expressions as `nlchain.step`. `nlchain.py` was not edited and was not
sed-ed (rule 4).

## THE CAN-FAIL, WHICH IS THE ONLY REASON THE REPAIR IS ADMISSIBLE
A new driver producing rows in the sealed format is worth nothing unless it produces
the sealed instrument's rows. Run on Z=57 and Z=58, where `nlchain.py restart` had
already returned a record this session:

    Z=57   differing fields: NONE
    Z=58   differing fields: NONE

excluding two fields that differ by construction and are declared in the driver's own
docstring: `sec` (wall time of one process there, summed compute time here) and
`driver` (absent there, present here as provenance, §2.11).
Receipts: `RECEIPT-CANFAIL-TBSTEP-Z57.jsonl`, `RECEIPT-CANFAIL-TBSTEP-Z58.jsonl`.

## THE UNSOUGHT DETERMINISM RECEIPT
The Z=57 row orphaned by the first killed process was NOT used as a result. Z=57 was
re-run under the sealed instrument and the two records are **identical in every
field, including `sec`.** Kept as `RECEIPT-DETERMINISM-Z57-ORPHAN.jsonl`. That is a
sixth determinism receipt, in a sixth session, and it arrived from a failure.

## WHAT THIS SESSION DID NOT DO
It did not re-run the sealed chain on the new driver, and it makes no claim that
`tbstep.py` reproduces `nlchain.py` in CHAIN mode — it was written for restart mode
and exercised on four rows. Two agreements are two agreements.

## PROPOSED, FOR M
The repair currently lives beside the four rows it was written for. Two questions:
  (a) Should the channel-level division be folded into `nlchain.step` itself, so that
      the sealed instrument is under §2.20 rather than a driver beside it? That edits
      the most load-bearing file in the project and would need a full replay to seal.
  (b) Or does `tbstep.py` stand as the declared route for heavy rows, with
      `nlchain.py` kept untouched and used where a row fits a budget?
(b) is the conservative reading and is what this session did. (a) is the correct one
if any future work walks rows above Z=91, where nothing fits. **Not decided here.**
