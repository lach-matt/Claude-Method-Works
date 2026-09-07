# RULINGS-R4g.md — the three rulings that close Phase 2. M, 7 September 2026. Successor to RULINGS-R4f.md.

Governs where it differs from `RULINGS-R4f.md`, `RULINGS-R4e.md`, `RULINGS-R4d.md`, `RULINGS-R4c.md` and
`RULINGS-R4.md`, all members and all unedited. Phase 2 of `PLAN-R4-PUBLICATION.md` had been carried to 36 DONE,
1 REFUTED, 1 PART and 8 OPEN, and every one of the eight reduced to one of the three questions below. They were
put to M in question form, with the context each needed and nothing else, and answered one by one.

## 1. The bracket result

**1(a) — Seat it.** *"yes"*

The original-works return of 2026-08-28 (Request 3, M directing) proved register 334's sentence — composition seen
from above is a bracket and not a map — down the whole tower. It was drafted as a Register entry, reserved the
number **1836**, and that number was then spent on 6 September by the §34.4 qualifier entry, whose build read
"the Register runs to 1835, so the next free number is 1836" and did not look for a reserved draft. **A Register
number is assigned at seating**; the draft takes the next free number now. It seats with `r3-br-measure.py`, its
golden, and **`factor.py` — the return's own script — seated byte-exact beside it**, which is what the ruling
asked for. The instrument was already written to read `factor.py` from `members/` and to fall back to the mirror
only *before* seating, so the seating closes its own fallback.

**1(b) — Its kind is BOTH.** *"both"*

Drafted as *a finding*; *a measurement* was the alternative; M ruled both. **The mechanism is the absence of a
tag.** `kinds.py` reads a trailing `(a finding.)` and, where it finds one, **collapses the entry to that single
kind** — `if t: kinds={t[-1]}`. Where there is no tag it infers, and its kinds *overlap by design*: the file's
own second line says so. An untagged entry whose headline carries a digit is counted **a measurement** by the
digit and **a finding** by the fallback rule, which is exactly "both". So the entry seats with its tag removed,
and that is the ordinary form and not an invention: **only 105 of the 1,721 seated entries carry a kind tag at
all.**

**1(c) — The Compendium object stays with the compendium task.** *"it stays with the MC task"*

The entry names a Mathematical Compendium expansion (the bracket-system theorem, MC-55) as owed and does not
write it; R3 does not author compendium objects. M's reason is a **scheduling ruling and is recorded as one**:
*"the compendiums must be finished before the prose work, so the main volume pointers can be fixed during the
prose phase."* The compendia therefore close before Phase 3 opens, and the main volume's pointers into them are
repaired inside the prose pass rather than ahead of it.

## 2. Register 1797

**2 — Seat it.** *"yes"*

A staged entry holds that register 1176's agreement theorem — *"E(X) = 0 if and only if the languages agree —
six indexes, three operators … without exception"* — has a counterexample among the book's own mathematical
objects. Its siblings 1793–1796 were seated by the cypher-audit queue and it was not, so **1797 has stood as a
hole**: 1796 and 1798 are both seated and no `<!-- EXCISED 1797 -->` marker covers it, which `RULING 27 — TWO
REGISTERS` does not allow. It seats as a correction citing 1176, at the next free number, and the hole at 1797
stays a hole: **a Register number is not reused, and a gap with no marker is a fault of the record that a later
entry reports rather than back-fills.**

## 3. Whether a chat transcript is a source R3 may repair FROM

**3(a) — Yes, and exhaustively.** *"yes, but the chat must be reviewed exhaustively because context frames the
object in question; and usually they are also a lead with an attached instrument for verification"*

This was the open question `DEF-153P-PENDING.md` put: chat-67 records findings from readings of the volumes, and
whether a transcript is a source a repair may be made *from* — as against a lead by which the volume is *read* —
was M's to rule. It is a source. **Two conditions travel with the ruling and are part of it.** The first is that
the review is **exhaustive**: a withdrawal read out of one message is not evidence, because the context is what
frames the object, and a partial read can invert the finding. The second is M's observation that such a chat
**usually carries an instrument with it**, so the ordinary route to a repair is to re-run that instrument rather
than to quote the prose — which puts these repairs under the same discipline as every other entry in this leg.

**3(b) — Findings are recorded AND repaired.** *"findings need to be recorded and repaired"*

Twelve Register entries — **230, 314, 500, 502, 599, 602, 807, 1148, 1450, 1461, 1595, 1628** — assert what a
chat withdrew and carry no `WITHDRAWN` / `WARNING` / `REFUTED` / `SUPERSEDED` marker; **1395 carries `WARNING`**.
Four can be settled on the volumes alone; the rest could not be, and under 3(a) they now can. **A Register entry
is never edited: each repair is a new appended entry citing the superseded one**, and each is owed the exhaustive
review 3(a) requires before it is written. This ruling does not shorten that.

**3(c) — Seat the four intake drafts.** *"seat them at the next free number"*

`READ-intake1.md` §C drafted four entries at numbers **1795–1798** and said "wording is M's to rule on at R3".
Those numbers were spent by the cypher-audit queue, so the drafts have sat unseated and unnumbered. They seat at
the next free numbers. **Each rests on a delivered script and its banked log, and both are already seated
members**, so every one is re-run before it is seated rather than taken from the draft that states it.

## 4. What this file does not decide

The four intake drafts were written with kind tags outside the Register's vocabulary — `(a reproduction.)`,
`(a reproduction, of a reconstruction.)` and `(a computation.)`. **No seated entry carries a non-standard tag**:
the eight kinds are the whole tagged vocabulary and 105 entries use them. Seating three new reader-facing kind
names is an editorial decision M has not made, and the smaller act is available and now ruled: **the four seat
untagged**, which is the form 94 % of the Register already uses and which ruling 1(b) has just established as the
way a kind is left to inference. If M wants the words, one line restores them.
