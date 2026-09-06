# F62.1 — FOUR FILES OF UNESTABLISHED PROVENANCE ENTERED THE TREE AND WERE SEALED
# Raised 2026-08-20T17:52Z, SESSION 62, at the moment of staging deliverables.
# REGISTERED BEFORE ANY OF THEIR CONTENT WAS ADOPTED OR PRESENTED.

## WHAT HAPPENED
Four files appeared in `pack61/`, all stamped **17:40:27**, which I did not author:
    ADDENDUM-P3-INTERSECTION.md          FAULT-F61.2-DROPPED-CHANNEL-MARGIN.md
    SCORE-P3-INTERSECTION.log            seedscore.py
The s61 archive was sealed at 17:34:47 with 1066 files and BUILT BEFORE 17:40, so
**LOWDIN-HANDOFF-61.tar.gz is clean.** The s62 seal at 17:49 counted 1077 files and
**DOES include all four.** I signed that root without having authored its full contents.

## WHY THIS IS REGISTERED RATHER THAN QUIETLY ACCEPTED
Their content is on-topic and, on inspection, CORRECT: F61.2 registers exactly the defect
I named in SCORE-SEED-INDEPENDENCE §P3 — that `dmargin` and `ORDER_MATCH` compared unlike
channel sets once a seed dropped a channel — and the addendum rescores P3 on the
INTERSECTION of channels converging under both seeds, which is the right comparison and
the one Standing 8 demands. Its numbers match `seedO.jsonl` to the digit
(Z=19 dmargin 0.03555; Z=20 0.03095; Z=39 1e-05).
**But it also carries a Z=20 seed-C row that I never ran.** Something executed the runtime
in this container outside my tool calls. Correct content from an unestablished source is
still an unestablished source, and this project's whole claim is attributability.

## WHAT IS AND IS NOT COMPROMISED
NOT compromised: every number in `SCORE-SEED-INDEPENDENCE.md`, `SCORE-RUNG-5-9-7.md`,
`FAULT-F61.1`, and both prediction files was produced by tool calls in the session
transcript, from the sealed runtime, and each is reproducible from the archive.
COMPROMISED: the **provenance of root adbce8f2… (s62, 1077 files)**, which mixes authored
and unauthored files under one signature.

## REMEDY — M'S RULING REQUIRED, NOT TAKEN UNILATERALLY
The four files are NOT deleted: Standing 3 forbids undeclared removal, and if they are
M's own or a parallel session's legitimate work, deleting them destroys real work.
Three options, for M:
  (a) ADOPT — declare the source, attribute them in the ledger, keep root adbce8f2.
  (b) QUARANTINE — declare retirement in `pack62/RETIRE.txt`, re-seal without them, and
      re-derive the P3 intersection rescoring under my own hand. The rescoring is worth
      keeping on the merits; it should simply be earned again rather than inherited.
  (c) LEAVE AS IS, with this fault carried open in the bridge so no reader mistakes the
      s62 root for a single-author seal.
**Pending M's ruling, option (c) is in force and this file is the disclosure.**

## STANDING CONSEQUENCE PROPOSED
A seal should assert authorship, not merely integrity. `condense.py` verifies that files
match their hashes; nothing verifies that a file was WRITTEN BY THE SESSION SEALING IT.
Proposed for the next session: the seal records a count of files created during the
session's own transcript, and any excess HALTS the seal exactly as an undeclared removal
does. **A hash proves a file did not change. It does not prove where it came from.**