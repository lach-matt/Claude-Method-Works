# F77.1 — THE s76 HANDOFF WAS TARRED WITHOUT ITS SEAL LINE.
# Raised at s77 open. Severity: RECORD (bookkeeping), NOT content.

## WHAT HALTED
`bash pack58/open58.sh` STEP 1 returned:
    CONDENSE-CHECK: s76 NOT IN LINEAGE -- cannot verify
LINEAGE.txt's last sealed row is **s75, 1215 files, root ff11fa8d…bd62e**.
`condense.py 76 --seal` was never run at the close of s76.

## WHAT WAS DONE INSTEAD — INTEGRITY ESTABLISHED WITHOUT WRITING A SEAL
The current tree carries 1228 sealable files. Removing exactly the 13 paths new at
s76 (pack76/* — 12 files — and SESSION-76-COMBINED.md) and recomputing the root by
condense.py's own `root_hash` gives:
    subset files 1215/1215   subset root ff11fa8d…bd62e   **MATCH**
**Therefore: every byte sealed at s75 survives unaltered; s76 added 13 files,
changed 0, removed 0.** The archive is intact. Only the LINEAGE row is missing.

## WHAT WAS NOT DONE, AND WHY
No seal was written. A retroactive s76 row would record a root computed at s77 open,
not at s76 close — that is a different claim wearing the same name, and F76.1's
standing consequence (a citation by name is not a citation; hypotheses must be
matched term by term) applies to our own records first. **AWAITING M's RULING.**
  Option A  write the row as `s76` and note in LINEAGE that it was computed at s77.
  Option B  write no s76 row; the next seal is `s77` and s76 is covered by it,
            with this fault file as the record of why s76 has no row of its own.

## OPEN STEPS 2 AND 3 WERE COMPLETED BY HAND, UNCHANGED
STEP 2 runtime: rt/ rebuilt from sealed packs 5..76, 401 files; libshoot.so,
libshoot_sr.so, libshoot_x.so compiled clean. STATE CARD read — VERDICT: CLEAN,
packs 5..76, derivation 107 rows Z=2..108, live chain 119 rows, ledger 0 jobs.
STEP 3 canary: float OK, kernel OK, numpy OK, physics OK — **CANARY: CLEAN.**
No escalation to full replay is required.

## STANDING CONSEQUENCE PROPOSED
**A SESSION IS NOT CLOSED UNTIL `condense.py N --seal` HAS RUN AND THE LINEAGE ROW
EXISTS.** Tarring is not sealing. Add the LINEAGE row count to the close checklist
so the omission cannot be silent again.