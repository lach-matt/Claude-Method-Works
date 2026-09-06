# F63.1 — `open58.sh` INFERS THE SEAL NUMBER FROM DIRECTORY NAMES AND HALTS FALSELY
# Raised 2026-08-20T18:08:28Z, SESSION 63, at the OPEN, before any work.
# Registered before the open was completed by hand. No sealed file edited.

## WHAT HAPPENED
`bash pack58/open58.sh` HALTED at STEP 1:

    CONDENSE-CHECK s61: files=1080/1066 root=MISMATCH
      sealed root : 65127fc0887188984e5d8ead86b3264839954bf963bc366281a6c4b4c02f45a1
      computed    : dc77addaf2d9d5233cf2ce0c44e345b39b7d91d5beb089139832771457d2e481

## CAUSE — NOT A TREE DEFECT. THE TREE IS CLEAN.
`open58.sh:31` derives the session number from the filesystem:

    N=$(ls -d pack* 2>/dev/null | sed 's/pack//' | sort -n | tail -1)

**Session 62 wrote all of its deliverables into `pack61/` and never created a
`pack62/` directory.** The highest pack directory is therefore 61, so the open
checked the tree against the s61 LINEAGE row (1066 files) instead of the s62 row.

`LINEAGE.txt` carries the s62 row and it is correct:

    62     1080    dc77addaf2d9d5233cf2ce0c44e345b39b7d91d5beb089139832771457d2e481

Run against the right row, the check is clean, first time, no repair:

    $ python3 pack58/condense.py 62 --check
    CONDENSE-CHECK s62: files=1080/1080 root=MATCH
    CONDENSE-CHECK: CLEAN

**THE COMPUTED ROOT AT THE OPEN — dc77adda… — IS EXACTLY THE SEALED s62 ROOT.**
The tree handed over is byte-for-byte the tree that was sealed. Nothing is wrong
with the archive. The instrument asked the wrong question.

## THE SECOND DISCREPANCY, FOUND WHILE DIAGNOSING THE FIRST
`pack61/RULING-F62.1-ADOPTED.md` states the s62 root as **1ca50bff45f603ce…**
with **1077 files**. `LINEAGE.txt` row 62 states **dc77adda… / 1080 files**.
These are not the same seal. The arithmetic reconciles them: three files were
added to `pack61/` after that ruling was written —
`FAULT-F62.1-FOREIGN-PROVENANCE.md`, `RULING-F62.1-ADOPTED.md` itself, and
`SESSION-62-COMBINED.md` — and 1077 + 3 = 1080. **1ca50bff is an intermediate
root quoted in a document that was itself subsequently sealed into the tree it
was describing.** dc77adda is the operative s62 root and is the one that verifies.
Recorded, not repaired: no sealed file is edited (F44.1 route). Any future
citation of the s62 root must use dc77adda… and not the figure in the ruling.

## WHY THIS IS A FAULT AND NOT A NUISANCE
A false HALT at the open is more dangerous than a silent pass, in one specific
way: the documented escalation for a failed open is to distrust the handoff. A
session that took this at face value would have spent itself re-verifying a
chain that was never broken — or, worse, "repaired" a tree that was already
correct. **The open's own halt message names a MISMATCH of the root, which is
the archive's most serious possible finding, on evidence that shows the exact
opposite.**

It is also the fourth appearance of the register's most productive failure mode
(F44.2, F59.1, F60.3, F61.1, Standing 8): **a comparison run against the wrong
reference.** Here the variable under test was the tree and the reference was the
wrong session's row. Standing 8 caught it in the sense that the rule made the
diagnosis immediate — the first question asked was "is the reference right?"

## SCOPE — SURVEYED, NOT ASSUMED
    pack directories present         pack5 .. pack61 (no pack62)
    LINEAGE rows present             through 62
    tree files                       1080
    s62 row files                    1080          MATCH
    s62 row root vs computed         MATCH
    canary                           CLEAN (float, kernel, numpy, physics)
    prime.py                         VERDICT CLEAN
No other pack is skipped or shadowed by the N-inference; the defect is confined
to which LINEAGE row STEP 1 selects.

## REMEDY
1. **The open was completed by hand for s63**, executing STEP 2 (runtime rebuild
   from sealed packs, three kernels compiled) and STEP 3 (canary) exactly as the
   script specifies, after STEP 1 was verified against row 62 directly. All three
   steps passed. `open58.sh` IS NOT EDITED — Standing 4 ("never sed a verify
   script") governs, and the sealed instrument stays as sealed.
2. **Session 63 creates `pack63/` at its first write** — this file. That restores
   the invariant the script assumes and the open will infer correctly at s64.
   The invariant is hereby made explicit rather than implicit:
   **A SESSION THAT SEALS AS N MUST OWN A DIRECTORY `packN`.** s62 broke it.
3. Proposed for the seal, alongside s62's own authorship proposal: `condense.py`
   should take the session number from the LINEAGE tail, not from `ls`, or refuse
   to run when the two disagree. A seal number is a fact about the chain, not a
   fact about the filesystem.

## WHAT THIS DOES AND DOES NOT TOUCH
DOES NOT touch any physics, any margin, any entrant, any score, any prediction
sha. Nothing computational was read before this was registered.
DOES mean the s62 handoff, as shipped, cannot be opened by its own documented
one-line procedure without a hand correction. That is a defect in the handoff and
it is entered as one.