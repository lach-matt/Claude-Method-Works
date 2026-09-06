# RULING — F63.2. QUARANTINE AND RE-RUN. Remedy (a).
# SESSION 64, at the open, before any row at Z = 57, 58, 89, 91 was read.
# Ruled by M. Registered by the session before the instrument was started.

## THE RULING
Remedy **(a) QUARANTINE AND RE-RUN** is adopted. The reported `pack64/ctrl64.jsonl`
of unestablished authorship is **NOT ADOPTED, NOT READ, AND NOT SCORED.** The four
tie-break control rows are re-derived under this session's hand and scored against
`pack63/PREDICTION-TIEBREAK-CONTROLS.md`, sha
`0b12ef684c1e39b3b26fc9d0ebf988cda1929e2e658047f8ee2e3b88f0b61c20`, verified in this
container at the open.

Remedy (b) was available and is declined on the ground the s63 fault file states and
this session affirms: the F62.1 adopt precedent rested on `seedO.jsonl`, an
independent sealed artefact against which every number of the adopted instrument was
checked BEFORE the ruling. A RESULT answering the open question has no such check.
The only comparison available to it is the hypothesis it arrived to confirm.

## WHAT THIS SESSION VERIFIED BEFORE RULING (Standing 5, survey only)
    pack64/ in the handed-over tree          ABSENT
    pack sequence present                    5..61, 63   (no 62, no 64)
    any ctrl64* artefact anywhere            NONE
    tree at open                             1091/1091 root=MATCH  (9830f18a...)
    canary                                   CLEAN (float/kernel/numpy/physics)
    prediction sha 0b12ef68...               VERIFIED against the sealed file
    prediction sha cdc0d2b1...               VERIFIED against pack63/*.sha256

**NO HASH OF THE REPORTED ARTEFACT TRAVELLED WITH THE s63 HANDOFF.** It is therefore
unpinned from here and this session cannot detect whether it changed between the
report and any later reading. Under (a) that no longer matters for the result; it
remains on the register as the sixth appearance of the unpinned-citation failure mode.

## THE READING DISCIPLINE, RESTATED AS A CONSTRAINT ON THIS SESSION
No row, clause, count or margin of any foreign result at Z = 57, 58, 89, 91 has been
read by this session, and none may be. §2.13 is not recoverable once broken.
Should the foreign file later be produced, it may be COMPARED to this session's rows
but may not be merged with them, and its provenance stays unestablished.

## NAMING, TO KEEP THE QUARANTINE LEGIBLE
This session's output is `pack64/tbctrl64.jsonl`, **deliberately not** the reported
filename `ctrl64.jsonl`. A future session that finds both must be able to tell them
apart by name alone, without reading either. `ctrl64.jsonl` is a reserved,
quarantined name in this project and must not be written by any session.

## INSTRUMENT
`rt/nlchain.py restart Z` — the sealed walker, restart mode, reference = the OBSERVED
configuration of Z-1 from `ground.py`, c = C0 = 137.035999, CORR=False, every solve
through `nlguard.run_guarded`. This is the same instrument that produced pack53
`ctrl137.jsonl` and closed Rung 2 (pack53/ctrl137.sh). It is not modified. Restart
mode prints to stdout and does not append to `nlchain.jsonl`; the sealed chain is not
touched.

## BUDGET, DECLARED BEFORE THE RUN (§2.20)
    per row       1800 s wall, one Z at a time
    whole task    7200 s
    rows          Z = 57, 58, 89, 91, in that order
    write         each row appended to pack64/tbctrl64.jsonl BEFORE the next starts
    rerun cost    a row already in the file is skipped
    overrun       reports as OVERRUN and the row is NO-DATA, not a fail
Non-convergence of a channel returns no number and joins `fail` (guard behaviour).
Non-convergence of the REFERENCE is NO-DATA for that row (F59.3), not a pass.

## WHAT WOULD FALSIFY, CARRIED FORWARD FROM 0b12ef68 SO IT IS IN VIEW
Any entrant flipping to the Madelung order — 4f at Z=57 or 5f at Z=89 — under the
observed reference WITHDRAWS the s63 tie-break restatement and collapses Rung 2's
immunity finding to n+l <= 6. That is reported first, before anything else, if it
occurs. Ruling 2 (the restatement wording) is held by M until this is closed.
