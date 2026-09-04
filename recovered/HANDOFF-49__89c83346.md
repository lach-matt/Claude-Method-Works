# HANDOFF-49 — The Method 1.6 — chat 96 → chat 97

- Written from **chat 96** for **chat 97**. Live files: **BUILD90 main** (unchanged since chat 62)
  and **BUILD125 compendia** (= BUILD124 + W-135 + DEF-96 + six new members). Register **1 to 1792**
  (unchanged — no Register entry since the chat-67 hold). W-135 IS seated; chat 97 seats nothing at
  open and writes W-136 at close.
- **Read RULINGS-R2.md at open, last block first.** The chat-95 block still governs and is still the
  last: **a finding is not a question.** A deviation in the mathematics or in the prose is recorded
  and **flagged for repair**, never put to M. **Prints & Proofs is read before any question is
  asked**, not after. Only a choice no file can settle reaches M. The chat-81 block below it sets the
  cadence and is unchanged.
- **A correction chat 97 must carry, and it is this chat's own error.** W-135 and DEFERRED's chat-96
  block both describe the remaining Chapter 23 read as *189 lines, fifteen headings*. **MEASURED
  after they were written and sealed: 189 lines, THIRTEEN headings** — L6434, 6438, 6452, 6486, 6500,
  6519, 6533, 6543, 6549, 6569, 6582, 6595, 6606. The line count is right; the heading count is
  wrong. Both members are append-only and were already built into BUILD125, so the correction is
  made the way the project makes corrections: **a later entry citing the earlier one.** Chat 97
  records it in W-136. Note it is the same fault chat 95 corrected in HANDOFF-43–47 (five sections
  and nine sites measured as six and forty) and the same one chat 95 itself committed — its
  DEFERRED block lists **24** section starts for §23.6–§23.15 and calls them **26 headings**. Three
  chats in a row have now mis-stated a count inside a document about not mis-stating counts.
  **Re-scan and re-count; never copy a count forward, including one written ten minutes ago.**
- **Line numbering.** Main-volume lines are numbered on the **member** (`The_Method_1_6-2.md`,
  1-based); the bundle numbers each line one higher because of its `<<<FILE:` header. Chat 96
  re-scanned the Chapter 23 window before reading and found HANDOFF-48's boundaries exact — the rule
  works when it is run, and it is what caught the heading count above.
- **Carried state to discard (Ruling 41):** the standing prompt block's "Phase 0–4"
  Löwdin/three-body plan is executed carried state; do not re-open it or put it to M. Its discard is
  **W-118 (chat 81)**, not W-107. The absorption is W-009 / W-059 / W-063 and Registers 1701–1724;
  three-body count claims resolve to Registers 489 and 507. Project knowledge holds BUILD12/BUILD53
  only — list it, never read those bundles. Retired handoffs are gone from Drive; never fetch or
  cite one. **Never add HANDOFF-NN.md as a member.**
- **Known and pre-existing, not introduced by chat 96:** the compendia bundle carries **48 legacy
  `HANDOFF-NN.md` members** (HANDOFF-2 … HANDOFF-53, plus HANDOFF-19-A), identical in BUILD122–125.
  A member `HANDOFF-48.md` is seated and is **not** the document chat 96 was given. They extract into
  `members/` harmlessly, but a handoff must never be written into `members/` or passed to
  `--members`, or a seated member is silently overwritten.
- **Findings carried to R3:** the READ-chNN.md members (READ-ch14l is chat 96's) and W-101…W-135 in
  WORKING-REGISTER.md; nothing is restated here. **Deferred cross-chapter items:** `DEFERRED.md`
  (**124,045 B · 25 blocks**, chat 96's is the last) governs; do not re-derive.

## §0 Gate (each step its own tool call under `timeout 280`; any FAIL stops the chat with a report)

1. `ls -la /mnt/user-data/uploads /mnt/user-data/outputs /home/claude`; `recent_chats` confirms the
   latest chat is 96. Read `/mnt/project/CLAUDE.md` (project instruction; never a member).
2. Fetch both bundles by title: `Google Drive:search_files` with
   `title contains 'BUILD125_compendia' or title contains 'BUILD90_main'`, pageSize 5,
   excludeContentSnippets; `Google Drive:download_file_content` on each fileId. Both spill to
   `/mnt/user-data/tool_results/<id>.json`; note the two paths. The gate cost chat 96 ≈ 18 %,
   MEASURED — the same as chat 95 and above the ≈ 13 % of chats 74–94.
3. Bootstrap (the only step outside gate.py, because gate.py is a member):

```
timeout 280 python3 - <<'EOF'
import json, base64, hashlib, re, os
EXP={'main':'49065309b0c4fe8e055f693aed295cca','comp':'03feb9343ca1fd6527e90a4d1c799022'}
NAME={'main':'/home/claude/The_Method_1_6_BUILD90_main_and_register.md','comp':'/home/claude/The_Method_1_6_BUILD125_compendia_papers_audits.md'}
SPILL={'main':'/mnt/user-data/tool_results/<main-id>.json','comp':'/mnt/user-data/tool_results/<comp-id>.json'}
for tag in ('main','comp'):
    b=base64.b64decode(json.loads(json.load(open(SPILL[tag]))[0]['text'])['content'], validate=True)
    m=hashlib.md5(b).hexdigest(); print(tag, f'{len(b):,} B', m, b.count(b'\n'), 'lines', 'OK' if m==EXP[tag] else 'FAIL'); assert m==EXP[tag]
    assert not os.path.exists(NAME[tag]); open(NAME[tag],'wb').write(b)
os.makedirs('/home/claude/members'); n=0
for tag in NAME:
    for m in re.finditer(rb'^<<<FILE: (.+?)>>>\n(.*?)<<<END FILE: \1>>>\n', open(NAME[tag],'rb').read(), re.S|re.M):
        p='/home/claude/members/'+m.group(1).decode(); assert not os.path.exists(p); open(p,'wb').write(m.group(2)); n+=1
print('members extracted', n)
EOF
```

   Expected: main 1,983,081 B · 49065309b0c4fe8e055f693aed295cca · 18,470 lines; compendia
   **4,975,877 B · 03feb9343ca1fd6527e90a4d1c799022 · 61,480 lines**; **402 members extracted
   (2 + 400)**.
4. `python3 /home/claude/members/gate.py census` → `OK census: DEFECT-CENSUS.tsv byte-identical`
   (1,556 rows + header, ≈ 15 s).
5. `python3 /home/claude/members/gate.py run --core` → five `OK` (tower 976/1,654/2,535/13,585/
   70,905/199,130; kinds 1565 · 1356 · 499 · 149; minmax; r2-tools-constants; extent "1 to 1792").
6. `python3 /home/claude/members/gate.py manifest` → `MANIFEST OK`; MANIFEST.tsv **26,907 B ·
   b51cd75770759b265899c67ea3d3ed6c · 402 lines**; WORKING-REGISTER.md **687,335 B ·
   848873b9c559ec8aeff8d76f358a719a · 6,005 lines**, ends **W-135**; DEFERRED.md **124,045 B · 25
   blocks**; RULINGS-R2.md 9,844 B · 10a2ea7ebdf2cc3ca8761bc3cb8d61a6 · 82 lines (unchanged);
   r2lib.py 21,022 B · 580d2ea2e43c2ddf78018afcba2f7de7 · 453 lines (unchanged); gate.py 9,377 B ·
   a01ef15a; close.py 6,456 B · 98acae67; tower-2.py c0bce27a; census.py f5a73e2b; kinds.py 4262f7c5;
   minmax.py 26da1d78; r2-tools.py 4702f5f9. If two `BUILD*_compendia` files are present after a
   close, pass `--comp <path>` explicitly.
7. `python3 /home/claude/members/gate.py run r2-ch14l r2-ch14m` → two `OK` (chat 96's goldens:
   r2-ch14l.out 12,977 B · c4803f26 · 124 lines; r2-ch14m.out 13,398 B · fc3fee6a · 97 lines).
   **Both import the lifted r2lib**; an AttributeError means the extraction seated a pre-lift r2lib
   and the chat stops.
8. `python3 /home/claude/members/gate.py cert 97` → writes `/home/claude/GATE-ch97.txt`, verdict
   PASS only if every logged step passed. A FAIL anywhere stops the chat and is reported.

## What chat 96 did (do not repeat)

**§23.6–§23.9.3 is closed** — main **L6303–L6433, 131 lines, eleven headings**, exactly the unit
HANDOFF-48 proposed, boundaries re-scanned and confirmed. **Thirteen deviations, twenty-two verified,
six incidentals, one census row closed** (row 1136, closed as a C9 artefact — the flagged "in every
case" is scoped by its own sentence). All of it is in `READ-ch14l.md` and
`CENSUS-CLOSURES-ch14l.tsv`; **do not re-measure any of it.**

**The three findings that carry furthest:**

- **14l-16 — §23.8.3's reason contradicts §23.8.1's formula.** L6368 explains the Z/R cancellation by
  *under an affine map the decrement cannot change*; L6345's λ² = (2/3)Z²R/ν² scales by Z², MEASURED
  45.7239 / 182.8955 / 1646.0597 at Z = 1, 2, 6, ν = 40. The cancellation is real (V = 4r³/(3r²−1)
  at every Z); the reason is wrong. **The repair is a reason, not a figure** — the first of its kind
  this phase.
- **14m-01 — a pointer with no correct target anywhere.** L6319 sends the reader to §25.6 for why the
  field abandoned the variable; §25.6 is the Sc VI deduction and carries *abandoned*, *variable*,
  *literature*, *field* zero times each, and *abandon\** has only three main-volume sites in total.
  Chat 95's 14k-01 could be redirected to §23.15; this one cannot.
- **14l-13 — one wrong digit contradicting its own section.** §23.8.2's Z = 1 row prints ν ≤ 406;
  the threshold is 405.717 and the ratio at 406 is 1.000698 > 1, while L6361 twelve lines below
  states the crossing correctly. Z = 2 and Z = 6 floor correctly.

**Also measured:** 731.5820 (L6347) does not reproduce under R = 109737.31568, the only Rydberg
constant printed in either bundle (17 sites) — it gives 731.5821; *a twelfth* at L6402 is a tenth
(9.7812), the twelfth belonging to the row below; §23.9.3's V-on-T column reproduces only under
ν = n − 1.35, h = 1, and its V-on-ν column reproduces under nothing at all. The exact
V = 4r³/(3r²−1) was independently re-derived from §23.6's fractional forms, confirming chat 95.

**Eleven instrument faults, all self-caught and rewritten, none trimmed.** The three to carry are in
DEFERRED's chat-96 block; the shortest form is: **re-read a verdict against the numbers printed
immediately above it** (a verdict asserted "no Figure 23.1 exists" three lines under a printed list
of four figures); **the object under test is never its own witness** (a claiming sentence and a
heading were counted as evidence for the claim they announce); and **a bound is not a measurement**
(a self-concordance threshold was read as a channel depth). All three are chat 94's
*gain*-inside-*against* in new dress.

## Chat 97's section read — Chapter 23, §23.10 to the end

MEASURED this chat by heading scan on the member: **§23.10 L6434 through §23.15, ending L6622;
189 lines, THIRTEEN headings** — §23.10 6434, §23.10.1 6438, §23.10.2 6452, §23.10.3 6486, §23.10.4
6500, §23.11 6519, §23.11.1 6533, §23.11.2 6543, §23.12 6549, §23.13 6569, §23.14 6582, §23.14.1
6595, §23.15 6606. Chapter 24 opens **L6623**. **Re-scan them before reading a line** — this list is
a measurement of chat 96, not a licence to skip the scan, and chat 96's own heading count was wrong
until it was re-measured.

**Take the whole remainder as one unit.** 189 lines is above the 141-line ceiling chat 94 proved and
the 131 chat 96 read, but the alternative splits §23.10's order axis or separates §23.11 from
§23.15, which the ν_V docket needs read together. If the read will not close, the natural break is
after §23.11.2 (L6434–L6548, 115 lines, eight headings), leaving §23.12–§23.15 (L6549–L6622, 74
lines, five headings) — **decide before reading, not during; a section read is never split across
chats.**

**What this unit owes, beyond the read itself:**

- **§23.15 closes chat 95's ν_V docket.** Read it once, then test both citing sites — main **L6270**
  and **L6923**, which cite §23.11 for the ν_V ceiling — against §23.15 as it words the claim, and
  test the **Ga I attribution**: §23.15 gives Al I nf's failing cells as n = 48, 51, 53, 54 and
  prints no ν_V for Ga I anywhere, while L6270 names *Al I at n = 51 and Ga I at n = 53*. Both are
  repair items under the chat-95 ruling, not questions.
- **§23.11 is a citation class, not a site** (chat 95's 14k-01) — the section carries ν_V, ceiling,
  granularity, quotation, curvature and resolve **zero times each**. Confirm from the section, then
  record; the index at L11448 already reads *§2.3 · §23.14 · §23.15* and is correct.
- **§23.12 "The optimal order is a boundary, not a peak"** and **§23.13 "Inversion"** are the
  computable core: §23.13 L6573 recovers exponents empirically (Na I −1.993, K I −1.998, C₃ 3.999,
  α 6.990), which is a fitted-exponent claim testable against the exact V of each observable — chat
  96 measured all eight of §23.9.1's exact V values and they are in r2-ch14l.out.
- **§23.14 "Two kinds of bound, and the book has been calling them"** is a vocabulary claim about the
  book's own usage: it must be tested against the volumes' actual usage, word-bounded, not read.

Instruments: **r2-ch14n** (computable) and **r2-ch14o** (prose). Import `heading_line`,
`section_span`, `has_token` and `enclosing` from r2lib by path; **copy nothing**. Six functions are
still owed to r2lib and DEFERRED lists them; Chapter 23 has needed none of them.

**Standing method, unchanged and all of it earned:** use the exact-token heading resolver, never
prefix matching; never span a section by heading rank — the book sets §23.10 and §23.10.1 at the same
`###` depth. Grep lowercase `register NNN` by hand. Check every printed pair count against C(N, 2).
Resolve every pointer to the claim and not the heading, and before recording any pointer as
unresolved **read the target section and test for the claim as that section words it**, case-exact
and word-bounded — and if it fails there, grep the whole volume for the claim before recording it, as
chat 96 did for §25.6. Give every negative claim its own witness, measured separately. Check the
arithmetic of every ratio and percentage; **never round with `round()`** — it is binary — use
`Decimal.quantize` and name the convention; convert exact Fractions numerator/denominator, since
`Decimal(str(Fraction))` raises ConversionSyntax. A formula numerator is not a value; word-bounding
applies to numbers as much as to words; a citation is not a declaration; a heading is not a
statement; a bound is not a measurement; a boundary case is not a violation. Where the text prints a
sample, measure the population. Grep the Register for a later entry naming the section before
recording any figure as unreproducible. **When an instrument disagrees with a hand reading already
taken from the file, the instrument is wrong until proved otherwise** — chat 94 hit that twice, chat
95 four times, chat 96 three.

## The repair docket

Carried forward until R3 executes it. **None of these goes to M.** Chat 96's additions are in
DEFERRED's chat-96 block in full; the docket below is the standing list.

1. **§14.5.2–§14.5.7 — six heading-only sections, forty citations. R3's largest single item.**
   MEASURED against the Prints & Proofs original (738,550 B · md5 49900cf41f818ab789bb90fc596ac977):
   **authoring gap, not production loss** — the text never existed, so no earlier print carries it.
   Citations: §14.5.2 → 4, §14.5.3 → 1, §14.5.4 → 4, §14.5.5 → 4, §14.5.6 → 3, **§14.5.7 → 24**.
   **Order:** the Register is append-only, so read its nine §14.5.7 citations first and author to
   what they already say, then §21.5.4, then the Mathematical Compendium's twelve. Chat 90's
   **seed(Λ₈) = 7** is the settled material §14.5.7 owes. Full docket in DEFERRED's *Chat 95B*.
2. **The §18.4.1 one-dimensional refinement — a missing Register entry** (main L5977–L5980). Register
   319, which the passage cites, states a different claim. Append-only, so this is a missing entry
   and not a wrong one; written when the chat-67 hold lifts.
3. **The σ collision — flagged for correction.** Rule 4 (main L6047) defines σ = 2R Z_eff² ·
   SE_pred / ν³; §22.5 (L6168) uses σ as the levels' measured uncertainty, and substituting Rule 4's
   σ into §22.5's r = 2Z²R/(ν³σ) cancels ν³ identically — MEASURED r = 100.000000 at ν = 10, 20, 40,
   80. Chapter 23's σ sites are none of them Rule 4's quantity (chat 95, nine sites).
4. **§23.8.3's affine-invariance reason** (14l-16) — new, and the docket's only *reason* item. See
   DEFERRED's chat-96 block: R3 must decide which invariance the chapter claims before rewriting,
   and must check §29.2 L7881, §29.7 L8052 and App D.4.1 L10377 for the same reasoning.
5. **The §25.6 pointer with no target** (14m-01) — author the explanation or drop the clause; the
   clause is load-bearing for the novelty claim beside it.
6. **The ν_V pointer class and the Ga I attribution** (chat 95's 14k-01, 14k-02) — closes in chat
   97's read.
7. **§32.3 is a citation class, not a site** (chat 94's 14h-05) — four prose citations, three
   disagreeing with the section. Read §32.3 once, then test all four.
8. **The unprinted-input class, now eight members** — §22.1.2 needs δ = 0.35; §22.4.1 needs
   δ₂ = 0.06; L6060's 446×, L6068's 1,577, L6093's 3.47 %, L6104's *factor of 17*; §23.1 L6189's
   *agreement under 1 %*; and **§23.9.3's two columns** (14l-24), the first member whose figures
   cannot be reproduced at all. The census R3 owes is **every site in the six volumes that prints a
   derived figure beside its inputs**.
9. **The 32/11 scope docket** (14j-01), now with six measured main-volume sites — L6193, L6213,
   L6233, L6237, **L6381**, L10245 — plus 2.909 at four. L6381 claims the floor as an original
   result and must be repaired **after** the scope decision, not with it.
10. **The truncation-printed-as-equality class** (14l-02, 14l-03) — sweep for every display equation
    whose own table disagrees with it.
11. **The Nesterov name-form sweep** (14m-07) — five forms in five places, one of them substantive
    (L8052 credits Nesterov alone for a result §23.8.1 credits to both).
12. **The single-witness class** — seventeen figures in chat 96's 131 lines, thirteen in chat 95's
    125, seventeen in chat 94's 141. R4 should state which figures are unverifiable rather than
    leaving them looking checked, and should distinguish *unverifiable* from *uncorroborated*.

## Close (chat 97)

`gate.py bank r2-ch14n r2-ch14o`; delete pycache in its own delete-only call; write `W-136.md`
(begins `### W-`, **ends with a blank line** — close.py asserts this, and it must record the
thirteen-not-fifteen correction citing W-135); append a DEFERRED block as `DEF-97.md`; then

```
timeout 280 python3 members/close.py --old The_Method_1_6_BUILD125_compendia_papers_audits.md \
  --new The_Method_1_6_BUILD126_compendia_papers_audits.md --w W-136.md \
  --main The_Method_1_6_BUILD90_main_and_register.md --append DEFERRED.md DEF-97.md \
  --members members/READ-ch14n.md members/CENSUS-CLOSURES-ch14n.tsv members/r2-ch14n.py \
  members/r2-ch14n.out members/r2-ch14o.py members/r2-ch14o.out
```

It must print **reverse recovers md5 03feb9343ca1fd6527e90a4d1c799022 == old: True** before writing;
if it does not, nothing is written and the failure is reported. `--append` arguments must precede
`--members`, and `--members` may be omitted entirely if nothing new is seated. **A changed
append-only member is grown with `--append <member> <delta-file>`, never passed to `--members`** —
close.py refuses a name collision, and a member needing *replacement* rather than growth has no
mechanism at all. After a close, `gate.py manifest` reports FAIL on changed members because the
extracted copies stay at pre-close state; **verify appends by reading the new bundle directly.**
`gate.py bank` refuses to overwrite an existing `.out`; correcting an instrument after banking needs
a **delete-only** call to remove the golden, then bank again. Then copy BUILD126, HANDOFF-50 and the
READ file to `/mnt/user-data/outputs` and present them.

## Drive actions for M

- **Upload** to Materials (`1XX_5f3PZB6tjRtiZ2GIgd8Tt7i_4GgkY`): `HANDOFF-49.md` and
  `The_Method_1_6_BUILD125_compendia_papers_audits.md`.
- **Retire** once BUILD125 gates PASS in chat 97: HANDOFF-48 and BUILD124, plus any earlier compendia
  builds still present (BUILD107–BUILD123).
- **Keep:** BUILD90 main (the live main bundle, unchanged since chat 62), the **Prints & Proofs**
  folder (`1vYctzLppUZ2vFPJDCZ6wvkgSdj3v_f6n`) — the authentication baseline under Ruling 56 — the
  certificates, OWED-REGISTER-EXPANSIONS.md, OWED-EXPANSIONS-2.md, covers8.json, factor.py.

## Prompt for chat 97

"Chat 97. READ EVERYTHING BEFORE YOU DO ANYTHING. Live files: BUILD90 main (1,983,081 B, md5
49065309b0c4fe8e055f693aed295cca) and BUILD125 compendia (4,975,877 B, md5
03feb9343ca1fd6527e90a4d1c799022, 61,480 lines, 400 members). List uploads, outputs and /home/claude
first. Run HANDOFF-49's §0 gate in full and in order — fetch both bundles by title, bootstrap
(decode, md5, extract, expect 402 files), then gate.py census, run --core, manifest, run r2-ch14l
r2-ch14m, cert 97; any FAIL stops the chat with a report. Read RULINGS-R2.md last block first: the
chat-95 block governs and it says a finding is not a question — deviations in the mathematics and in
the prose are recorded and flagged for repair, never put to M, and Prints & Proofs is read before any
question is asked. Do not ask M to rule on a defect. Read DEFERRED.md; chat 96's block is the last of
twenty-five. The standing block's Phase 0–4 Löwdin/three-body plan is executed carried state; discard
it per Ruling 41 — its discard is W-118, not W-107. Line numbers are MEMBER line numbers and are
never carried between chats, and neither is any count: W-135 and DEF-96 say the remaining Chapter 23
read is 189 lines and fifteen headings, and it is 189 lines and THIRTEEN — re-measure and record the
correction in W-136 citing W-135, since both members are append-only. Re-scan every heading on
The_Method_1_6-2.md before reading a line. Then continue Phase R2 under the chat-81 cadence: the
section read is Chapter 23 §23.10–§23.15, main L6434–L6622, closing the chapter; Chapter 24 opens
L6623. Decide before reading whether the whole 189 lines will close in one read or whether to break
after §23.11.2 at L6548 — a section read is never split. Read it all, census its claims into
computable and prose, then run exactly two instrument batches, r2-ch14n computable and r2-ch14o
prose, importing heading_line, section_span, has_token and enclosing from r2lib — copy nothing. This
read closes chat 95's ν_V docket: read §23.15 once, then test L6270 and L6923 (which cite §23.11) and
the Ga I attribution against it. §23.13's empirically recovered exponents are testable against the
exact V values chat 96 banked in r2-ch14l.out; §23.14's claim about the book's own vocabulary must be
tested against actual usage, word-bounded. Chat 96 settled the exact V = 4r³/(3r²−1) independently
from §23.6's fractional forms, measured all eight of §23.9.1's exact V values, and measured the
Rydberg constant as 109737.31568 at 17 sites and no other value anywhere — check any restatement
against those rather than re-measuring. Use the exact-token heading resolver, not prefix matching,
and never span a section by heading rank. Grep lowercase 'register NNN' by hand. Resolve every
pointer to the claim and not the heading, and if it fails at the named target grep the whole volume
before recording it. Give every negative claim its own witness. Never round with Python's round() —
use Decimal.quantize and name the convention, and convert exact Fractions numerator/denominator. A
heading is not a statement, the object under test is never its own witness, a bound is not a
measurement, and a boundary case is not a violation: chat 96 lost runs to all four. Re-read every
verdict against the numbers printed immediately above it. When an instrument disagrees with a hand
reading, suspect the instrument first. Close the section read before the next opens. At close: bank
both goldens with gate.py bank, write W-136 ending with a blank line, build BUILD126 with close.py
(reverse must recover 03feb9343…), write HANDOFF-50. A changed append-only member is grown with
--append, never --members. No corrections, no Register entries, no TASK 1 until the review closes.
Handoff at 90–95 % of context or on a closed section read — never earlier, never mid-section. Timeout
on every call. Delete-only calls for pycache, never chained to gate.py bank. Never copy over an
existing file."
