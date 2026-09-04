# F64.1 — THE s63 HANDOFF QUOTES A TREE COUNT ITS OWN TREE NO LONGER HAD
# Raised 2026-08-20, SESSION 64, at the open, by survey, before any work.
# COSMETIC. No physics, no margin, no entrant, no score, no prediction sha is touched.
# Recorded, not repaired. No sealed file is edited (F44.1 route).

## WHAT WAS FOUND
`SESSION-63-COMBINED.md` (header) and `pack63/FAULT-F63.2-REPORTED-UNSHIPPED-RESULT.md`
both state the s63 tree as **1089/1089 root=MATCH**. `LINEAGE.txt` row 63 and the
open of this session both give **1091**:

    LINEAGE row 63    63    1091    9830f18a1522c1ceb4251edbc7ac5de7a0276b5dfdfe885bcf332edfd0fadda9
    open, s64         CONDENSE-CHECK s63: files=1091/1091 root=MATCH

## CAUSE — AND IT IS THE SAME CAUSE AS THE SECOND HALF OF F63.1
The arithmetic reconciles: 1089 + 2 = 1091. Two files entered `pack63/` after the
count was taken — `FAULT-F63.2-REPORTED-UNSHIPPED-RESULT.md` (which itself quotes
1089) and `SESSION-63-COMBINED.md`. **1089 is an intermediate count quoted in
documents that were then sealed into the tree they describe.**

This is exactly the shape of F63.1's second discrepancy, where
`pack61/RULING-F62.1-ADOPTED.md` quoted 1077 files and root 1ca50bff for a tree that
sealed at 1080 and dc77adda. **Third instance. 9830f18a… / 1091 is the operative s63
seal and is the one that verifies.**

## WHY IT IS ENTERED AT ALL, GIVEN THAT NOTHING IS WRONG WITH THE TREE
Because the previous instance of it cost a session its open. A quoted root that does
not verify is indistinguishable, on its face, from a tree that has been altered. A
reader who trusts the fault file's 1089 over LINEAGE's 1091 concludes the archive
gained two unaccounted files between the seal and the handoff. It did not; the two
files are the fault file and the combined handoff, and both are named in the tree.

It also has a live consequence for the class of fault F63.2 is about. F63.2's own
strongest argument is that a citation with no artefact behind it cannot be checked —
and F63.2 is itself the document quoting the stale count. The discipline is harder to
hold than the rule makes it sound: **a document that describes the tree it will be
sealed into cannot state that tree's size correctly from inside itself.**

## PROPOSED, FOR M
A structural remedy rather than a rule asking for more care:
  (a) A session states its tree count and root ONLY in `LINEAGE.txt`, which is written
      by the seal and not by hand, and every other document REFERS to the LINEAGE row
      rather than transcribing its numbers. s59's precedent — the root is not quoted
      in the bridge, it lives in the body of LINEAGE.txt — already does this for the
      root and should extend to the count.
  (b) Or the seal refuses to run when a file in `packN/` transcribes a root or count
      that disagrees with the row it is about to write. This is checkable: the seal
      knows both numbers at the moment it writes them.
(a) costs nothing and removes the failure mode rather than detecting it. Recommended.

## STATUS
OPEN, cosmetic, carried into the s64 seal. No repair attempted this session.
Any future citation of the s63 seal must use **9830f18a… / 1091**.
