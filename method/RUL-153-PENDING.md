
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

## Put to M by chat 153-R after reading the consolidation branch (DEF-153P) — three questions, unanswered

Each is stated so that a one-word answer rules it; the recommendation is the chat's and binds nothing.

**Q1 — Is a chat transcript a source R3 may repair *from*, or only a lead R3 may read the volumes *by*?**
The retraction audit lists 25 figures or claims withdrawn in conversation and still printed as current. Chat-67 records
findings from readings of the volumes; nothing in the rulings names a transcript as a witness. One of the audit's own
rows shows a chat correction that was itself stale (the Register does begin at entry 1). *Recommended: a lead only —
a row is executed when the volumes themselves witness the withdrawal (register 402 against the closure rule's four
sites; 2,475; 1790 against its own table; 24,585 against 602), and otherwise it is docketed as a chat-witnessed
claim awaiting a Register entry of M's.*

**Q2 — Which object does register 66 quantify over: the observed ground configurations (`LW1-ground.py`, register
1306), or the aufbau-built table it was measured on?** On the observed table the occupied set is not downward
closed (Cr, Cu, Pd, Pt leave holes at 3d⁴, 3d⁹, 4d⁹, 5d⁸) and 0 of 120 ℓ-orderings are admissible against the
entry's 1 of 120. *Recommended: the entry's own words — "ground-state configuration" — name the observed table; if M
agrees, R3 appends an entry recording the re-measurement beside 66, in 1807's shape, and 66 is not edited.*

**Q3 — Are the thirteen numbers seated in neither register (176, 177, 661–663, 670–672, 682, 683, 687, 688, 1138)
withdrawn, or never issued?** A collection log quotes *Register 661* as a live instruction, so at least that one was
issued once. Every other gap in 1..1792 is a relocation to the Working Register under an EXCISED marker. This joins
the census retirement question of DEF-153O. *Recommended: 176 and 177 never issued (no trace anywhere); 661–688 and
1138 withdrawn, each to be recorded with a one-line reason in the Working Register, no renumbering.*

**Q4 — May R3 seat the recovered chapter 12–15 readings from the consolidation branch — 56 `READ-*.md`, 29
`CENSUS-CLOSURES-*.tsv`, 48 cited instruments — into the compendia bundle as one pass, each carrying its recovery status
(`RECOVERED` / `RECOVERED-BY-HEADING` / `RECOVERED-BY-WRITE`) and ledger provenance?** The store seats no reading of
chapters 12–15 though W-112 … W-121, DEFERRED and DOCKET cite them (DEF-153Q). *Recommended: yes for the readings and
closures, which are documents with an md5 and a source shard; the instruments only with a golden proved on the bundle
they were banked against, otherwise seated unproved as `r3-wl2` is; the 22 closures and 3 readings the export does not
hold recorded as ABSENT, not loss.*

## M's answers (chat 153-R, 4 September 2026), verbatim, and what each binds

> *1-lead only* · *2- the aufbau table* · *3-this can only be answered by the chat transcripts/information stated only
> in prose, which the other chat has made readable and identifiable for you* · *4-yes, following you specific
> recommendation*

- **Q1 — RULED: a chat transcript is a lead only.** A retraction-audit row is executed when the volumes themselves witness
  the withdrawal; otherwise it is docketed as chat-witnessed and waits for a Register entry of M's.
- **Q2 — RULED: register 66 quantifies over the aufbau table.** The entry is not wrong about its object; its object is not
  the observed table `LW1-ground.py` holds. R3 records this beside 66 as an entry naming the object and carrying the
  re-measurement on the observed table; 66 is not edited.
- **Q3 — RULED: the thirteen are to be answered from the chat transcripts**, which `drive/chats/` and the branch's
  `REGISTER-GAPS.tsv` make readable; R3 reads them and records each number's answer with its witness.
- **Q4 — RULED: seat the recovered chapter 12–15 readings, per the recommendation as stated** — readings and closures as
  members carrying their recovery status and ledger provenance; instruments only with a golden proved on the bundle they
  were banked against, otherwise seated unproved; the 22 closures and 3 readings the export lacks recorded ABSENT.
- **Q4 — WITHDRAWN by the chat, not executed: its premise was wrong.** The readings are archived, not lost — W-169 (chat 129)
  executed M's archive split into `The_Method_1_6_ARCHIVE1_legacy_handoffs_ch12-15.md`, held in the mirror byte-exact with
  the goldens (DEF-153Q, corrected). Seating the branch's `recovered/` copies would reverse that split and seat drafts
  (116 of 244 differ from the archived member). Open for M instead: whether `method/` carries ARCHIVE1 under `verify.py`.
