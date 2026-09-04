
## Chat 153 (4 September 2026) — the append-only directive is lifted for structural and prose edits; content stays untouchable

**M, in the repository session**, on being shown that Ruling 29 admits only one Register edit class — pointer
removal — and that tying register 1448 to 1332 could therefore only be done by a new entry:

> *the append only directive was something I put in place early on to protect the integrity of the work in
> these volumes. you'd have to agree that it's very extensive and carries a lot of scope, so the register was
> my way to show my work to the referees and readers. now that we are in the actual editing phase, that
> directive can be lifted with regards to structural edits like this one, and prose corrects. subject
> matter/content remains untouchable*

1. **The append-only directive is LIFTED for structural edits and prose corrections, in R3 and after.** It was
   put in place to protect the integrity of the volumes while they were being built; the editing phase is what
   it was protecting them for.
2. **Subject matter and content remain untouchable.** No figure, count, verdict, claim, attribution or
   register number changes under this ruling. A structural edit that would alter what an entry *says* is not a
   structural edit.
3. **The operative boundary, as this chat will apply it** (stated so a later chat applies it the same way, and
   correctable by M):
   - **Structural — permitted in place:** adding or repairing a cross-reference or pointer; correcting a stale
     line number, § pointer or register number that names the wrong target; heading level, table alignment,
     column order and formatting; restating an extent or count that the record itself has already moved.
   - **Prose — permitted in place:** wording, grammar, punctuation and phrasing that leaves every figure,
     verdict and claim identical.
   - **Content — forbidden:** any figure, count, percentage, date, name, attribution, status value, verdict,
     claim or its scope; removing an entry; renumbering an entry; moving an entry.
4. **Ruling 29 is superseded in part.** Pointer removal is no longer the only Register edit class; pointer
   *addition and repair* join it. Ruling 29's purpose — that the Register is not quietly rewritten — is carried
   by item 5 instead.
5. **A structural edit still leaves a record — in the WORKING register, not the Register.** M, correcting the
   first draft of this item: *"I agree, but these are working register, not to be included in the publishable
   volumes — work matter not subject matter."* An in-place edit that left no trace would satisfy the new
   ruling and defeat its own purpose, so **every in-place structural or prose edit is carried by a
   `WORKING-REGISTER.md` entry in the same build, naming the sites and what changed**, and the reverse-md5
   guard and count-asserted substitutions stand untouched. What is lifted is the requirement that a
   correction take the form of a new entry; what is not lifted is that it be recorded.
   **This is §2's standing distinction applied, not a new one:** the Register is a reader-facing compendium
   and records subject matter only; `WORKING-REGISTER.md` is the audit log and every editorial entry belongs
   there and is forbidden from the books. A structural or prose edit is **work matter**. It gets no Register
   entry, and nothing about it reaches a publishable volume.
   **What still earns a Register entry is unchanged:** a correction to the subject matter itself — something
   written wrong in the mathematics or the record and put right, with both states kept. Entries 1798, 1799 and
   1800 are of that kind and stand.
6. **The close route has to change with it.** `close.py` mechanically enforces append-only: it asserts that
   among old members only WORKING-REGISTER.md, MANIFEST.tsv and the `--append` targets differ, and that each
   grown body equals old body plus appended text. **An in-place Register edit cannot pass it.** A structural
   edit therefore goes through a class instrument in the form of `r3-wl2` / `r3-arith-01` — count-asserted
   substitutions with a reverse guard — and not through `close.py --append`. No instrument is loosened to
   permit it.
