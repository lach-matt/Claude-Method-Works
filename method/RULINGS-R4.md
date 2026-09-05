# RULINGS-R4.md — M's rulings on the publication plan (Phase 0), given 5 September 2026

M, on `PLAN-R4-PUBLICATION.md`: **"approved, proceed with phase 0 rulings as recommended. however, with 2, any math
that does not resolve to the claims of this book must be flagged to me for review."**

This member records what was ruled, what each ruling permits and forbids, which phase executes it, and — plainly —
which rulings were **not** given, because the plan offered no recommendation for them and a ruling cannot be inferred.
It is the authority the remaining phases work under. It is a member: it is never edited in place; a change is a
successor.

## 1. The plan, approved

The four things the plan asked for are approved as written:

1. **The finishing line** (plan §1). The set is publishable when the press, run from the archive over the seated
   volumes, produces six documents in which every recorded finding has a disposition, no work matter reaches the
   reader, every pointer, figure and count resolves, the audit instruments and the census run green over the
   **pressed** text as well as the source, and the archive records the path so the edition is regenerable byte for
   byte. M signs the pressed proofs.
2. **The eight phases and their order** (plan §3): 0 rulings · 1 mathematics · 2 the Register · 3 the main-volume
   prose · 4 the compendia and the Index of Indices · 5 the census · 6 the instrument estate and the archive ·
   7 R4, the cross-volume audit · 8 the press and the proofs.
3. **The Phase 0 rulings as recommended**, recorded below.
4. **The plan is a member**, rewritten by successor at each phase close, with the docket consolidated into it, so
   there is one place the remaining work is counted. Seated at W-239 with `PLAN-R4-ANNEX.tsv`, the item inventory
   behind it.

Three standing forms are unchanged by any of this and govern every ruling below. A change to a reader-facing volume
happens only through a guarded build carrying a Register entry. A finding is recorded, never silently repaired. A
seated member is never edited in place. And a **press-time substitution is not an edit**: it maps an exact string in
a seated source to an exact string in the printed document, is recorded in the press table, and leaves the source
untouched — which is why several rulings below take that route rather than a volume build.

## 2. Ruling 2, and the condition M attached to it

**Ruled.** The fifteen main-volume sentences that spell the Register's size in words — "one thousand six hundred and
thirty-five", the entry count at BUILD90 — are re-typed to the live count **by press-time substitution**, one recorded
pair per site, keeping each sentence's own word form. Register entry 1815 repaired the digit-form counts and left
these deliberately; this ruling closes them.

**The condition, and it governs more than this ruling.** M: *any math that does not resolve to the claims of this book
must be flagged to me for review.* Operationally, and this is now the standing rule for every count the plan touches:

- Before any figure is substituted, **what the sentence counts is measured, not assumed**. A sentence that says
  "entries" and a sentence that says "corrections" are not the same claim, and the live figure for one is not the
  live figure for the other.
- Where the measured unit has a live figure the book itself carries, the substitution is written and executed.
- **Where it does not resolve — where the book's own instruments measure something the sentence's unit contradicts —
  nothing is substituted.** The site is flagged to M with the sentence, the unit it names, the figure the book
  measures for that unit, and the size of the gap. That is a finding about the text, not a stale number, and it is
  M's to rule.
- No site is repaired into a different false claim to make a count agree.

The measurement of all sixteen sites (fifteen in the main volume, one in the Register) is carried in
`DRAFT-R4-COUNT-SITES.md` and the flagged sites go to M there. **No substitution is written until M has ruled on the
flagged sites.**

## 3. The rulings given

**1 — The Register is published as the record of the work.** Option (a). It keeps its chronicle form. A reader's key
is added up front stating what a build, a chat, an instrument and a docket are, so the vocabulary is interpretable.
Only handles that name nothing a reader can hold are pressed out: build numbers, working-register numbers, file paths,
byte counts and hash fragments. Instrument names stay, because in this volume an instrument is the evidence for a
registered claim and the key makes it readable. *Executes in Phase 2 (the key, by build) and Phase 8 (the press pairs).
Forbids: rewriting 1,677 entry bodies into subject language, and publishing a reduced "reader's Register".*

**2 — The word-form count sites.** As §2 above.

**8 — None of the 110 withdrawn entries is reinstated.** They stay recovered in the archive and out of the volume.
The four absent numbers that reader text cites — 287, 1000, 1002 and 1725 — are repaired **at their citing sites**,
by entry, so that no printed pointer reaches a number the Register does not carry. *Executes in Phase 2. Forbids:
reinstating an entry to satisfy a pointer.*

*Measured before this ruling was written, and the four are not one case.* All four are absent from the Register's
headings and all four are cited in reader-facing text: 287 at main L1503 (the §2.19 protocol table, "reg. 286, 287");
1000 at Register L4666; 1002 at Register L6528; 1725 at Register L10, the front matter's own account of the entry
form. **1002 is the special one:** the entry citing it exists to supersede it, and the Register's front matter states
that a correction never replaces what it corrects and names the entry corrected. A pointer from a correcting entry to
the entry it corrects is the volume's discipline working, not a broken pointer — so at that site the repair is to
explain the excision, not to remove the citation. The other three point at nothing and are repaired. Phase 2 reads
each of the four before it writes, and reports any further distinction it finds rather than flattening them.

**9 — A withdrawn thing may be named by number in reader text; the form stands.** Figure 15.3, named in the main
volume as withdrawn and placed nowhere, stands as it is. The C7 class's pointer form — "(the figure §12.11.5
withdraws; register 1819)" — stands, and the withdrawn numbers surviving inside those pointers are not defects.
*Executes in Phase 5 as a closure verdict over the 34 open C7 rows. Forbids: rewording the pointers, and treating a
surviving withdrawn number inside a withdrawal pointer as a defect.*

**10 — Unheaded pointer targets get headings.** Chapter 4's protocol rows, cited as §4.1 to §4.7 at thirty-seven sites
across three volumes, and Appendix E's E.4, whose children E.4.1 and E.4.2 have no parent, receive real headings by
guarded build, so that every pointer resolves against a heading the reader can find. *Executes in Phase 3. Forbids:
ruling that a prefix resolves, and silently repointing the citations instead.*

**11 — The four compendia are hand-maintained volumes.** `mathreg.py`, `compendium.py`, `indices.py`, `physics.py`
and `mathverify.py` are not members and cannot be; the volumes have been hand-edited since those generators last ran,
so a regeneration would drop seated work. The compendia are ruled hand-maintained: their "generated from … on …"
datelines, their rebuild commands, and the Löwdin sentence deferring verification to `mathverify.py` are pressed out
or reworded, and the volumes' counts are maintained by measurement against the Register rather than by regeneration.
*Executes in Phase 4 (the reworded sentences, by build) and Phase 8 (the press pairs). Forbids: writing generators to
reproduce hand-edited text, and any regeneration of a compendium from a script.*

**12 — `COORDINATES-2.13` is seated as a member**, with the instruments, under M's ruling of 5 September that every
tool goes in the archive. The Spectra Compendium calls it the volume's data companion; a companion a reader is
promised must be in the store of record, not only in the mirror. *Executes in Phase 6. Forbids: publishing the
promise while the file exists only in the Drive mirror.*

**13 — The archive pass runs.** Every predecessor instrument with a seated successor moves out of the live set on
ARCHIVE1's precedent, so that the gate's full walk is green and the red names in the record are the ones that mean
something. Nothing is deleted: a predecessor stays seated and stays readable; it stops being walked. *Executes in
Phase 6. Forbids: deleting a superseded member, and re-banking a predecessor to make it green.*

**14 — The census's C8 class is a listing, not a defect class.** All 299 `C8-NAMED-STATEMENT` rows — "this name is
used as a statement; is it set out in bold in the main volume?" — close on this one ruling rather than row by row.
The class records where the book names a statement it does not separately state, which is information about the
book's vocabulary, not a defect in it. *Executes in Phase 5 as one closure file citing this ruling. Forbids: reading
299 rows individually, and repairing a volume to satisfy a C8 row.*

**15 — Merge order and the mirror.** The consolidation branch lands on main first; then this branch merges to main,
its two conflicting hunks in `CLAUDE.md`'s tools list resolved in favour of the current tool set. Drive is reconciled
**once, at the end**, not per build: the repository is the store of record and the mirror follows it. *Executes in
Phase 6. Forbids: per-build Drive reconciliation, and opening a chat from the stale mirror.*

**5 — Entry 1836, the bracket result, is seated as drafted, kind *a finding*.** Taken on the DRAFT's own
recommendation rather than on the plan's, which offered none: `DRAFT-R3-LEAD-bracket.md` proposes *a finding* with
*a measurement* as the alternative, and the draft's proposal is followed. Seated with `r3-br-measure.py`, its golden,
and `factor.py` byte-exact from the mirror at md5 `55c518c9…`. The draft's third question — whether the Mathematical
Compendium's bracket-system object (MC-55) stays with the compendium task line — is answered by ruling 11's phase: it
is Phase 4 work, and R3 does not author compendium objects. *Executes in Phase 2.* **Reversible on a word from M**,
this one ruling being an inference from a draft rather than a recommendation M approved; nothing is seated on it
before Phase 2 opens.

## 4. The rulings NOT given, and what they block

The plan asked fifteen things. Five of them carried no recommendation, so "as recommended" cannot reach them and
none is inferred here. Each is M's, and each blocks the work named:

**3 — The nine heading-only sections.** §14.5.2 to §14.5.7, §2.22, §28.7.6, §28.9 (and §21.5.4, and the Mathematical
Compendium's twelve) are headings with no body. Either M authors them, or they are withdrawn by entry. *Blocks the
close of Phase 3: the prose leg can run around them but cannot finish while a printed contents promises nine sections
that are not there.*

**4 — Entry 1797.** The agreement theorem's counterexample, staged since W-196; its instrument `audit_math.py` is now
seated and exits 1 by design, printing the counterexample. Seat the entry, or withdraw it and release the number.
*Blocks: the Register's extent has a hole at 1797 that no instrument can explain to a reader, and census row 1321
(register 1176's "without exception") waits on it.*

**6 — The language roster.** Dockets 20x-04 and 20x-09. Register 1173, §33.1 and §20.2 print three different rosters;
measured on Λ the operator-bearing five are order, algebra, geometry, information and statistics — 1173's count with
a different membership, `statistics` in and `analysis` out, `analysis` and `documentary` special in different ways.
`cypher.py` refuses to resolve it in code and keeps the rosters as data. *Blocks: §33's and §20.2's prose in Phase 3,
and the cypher figures in Phase 1.*

**7 — The retraction and prose-only triage.** Twenty retraction rows witnessed only by conversation (DEF-153P) and
1,168 statements held only in chat prose (DEF-153R). A triage rule is wanted: which become M's entries, which are
recorded as leads and stay leads. *Blocks: Phase 2's entry list cannot be closed, and the volumes cannot be declared
complete against the record while 1,168 statements have no disposition.*

**Ruling 5's residue is not open**: the draft's own recommendation supplied it, as recorded above.

## 5. What opens now

Phase 1, the mathematics leg, opens on the rulings given. Phase 5, the census, opens beside it under rulings 9 and 14.
Phase 2 opens on ruling 5's seating and on rulings 1 and 8, and closes only when rulings 4 and 7 are given. Phase 3
cannot close without ruling 3. Phase 6 runs throughout on rulings 12, 13 and 15. The count sites of ruling 2 are
measured and the flagged ones are with M in `DRAFT-R4-COUNT-SITES.md`.
