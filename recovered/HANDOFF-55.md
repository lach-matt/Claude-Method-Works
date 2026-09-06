# HANDOFF-55 — The Method 1.6 — chat 102 → chat 103

- Written from **chat 102** for **chat 103**. Live files: **BUILD90 main** (unchanged since chat 62)
  and **BUILD131 compendia** (= BUILD130 + W-141 + DEF-102 + six new members). Register **1 to 1792**
  (unchanged — no Register entry since the chat-67 hold). W-141 IS seated; chat 103 seats nothing at
  open and writes W-142 at close.
- **Read RULINGS-R2.md at open, last block first.** The chat-95 block still governs and is still the
  last: **a finding is not a question.** A deviation in the mathematics or in the prose is recorded
  and **flagged for repair**, never put to M. **Prints & Proofs is read before any question is
  asked.** Only a choice no file can settle reaches M. The chat-81 cadence below it is unchanged.
- **Chapter 25 is half read.** §25–§25.5 closed in chat 102 (L6884–L6990). **§25.6–§25.6.6 is
  unread**: chat 103 opens it at **L6991** and closes the chapter there.
- **Chapter 25's extent is MEASURED, not carried:** L6884–L7116, 233 lines, fourteen headings, the
  end taken from the next `## ` (26. Collective sections, **L7117**). §25.6 L6991, §25.6.1 L7003,
  §25.6.2 L7021, §25.6.3 L7039, §25.6.4 L7059, §25.6.5 L7071, §25.6.6 L7093. **Re-scan anyway** — the
  rule is not that the last scan was wrong, it is that a carried boundary is not a measurement.
- **Never write an instrument that opens a `BUILDnnn` path** — the name changes every chat and the
  bundle comes to contain the instrument's own banked output. Chat 102's `r2-ch14x` and `r2-ch14y`
  read the six volume **members** by name and reproduced at their own bank.
- **Two form assumptions nearly cost two verified findings this chat, and both are now rules.**
  (1) **Emphasis-stripping destroys the underscore**: `ν_V` is invisible to a stripped test, and the
  raw line then gave **15 main sites**. Run every symbol test on the RAW line, and assume this fault
  hides every subscripted symbol in the volumes. (2) **A case-sensitive search for *four* missed
  §24.11's own heading word *Four*** and would have recorded the front matter's L62 as unsupported.
  Sixth and seventh chats running that a form or a base left unnamed produced a near-miss.
- **Line numbering.** Main-volume lines are numbered on the **member** (`The_Method_1_6-2.md`,
  1-based, 11,855 lines); the bundle numbers each line one higher because of its `<<<FILE:` header.
- **Carried state to discard (Ruling 41):** the standing prompt block's "Phase 0–4"
  Löwdin/three-body plan is executed carried state; do not re-open it or put it to M. Its discard is
  **W-118 (chat 81)**, not W-107. The absorption is W-009 / W-059 / W-063 and Registers 1701–1724.
  Project knowledge holds BUILD12/BUILD53 only — list it, never read those bundles. Retired handoffs
  are gone from Drive; never fetch or cite one. **Never add HANDOFF-NN.md as a member.**
- **Known and pre-existing:** the compendia bundle carries **48 legacy `HANDOFF-NN.md` members**,
  identical in BUILD122–131. They extract into `members/` harmlessly, but a handoff must never be
  written into `members/` or passed to `--members`, or a seated member is silently overwritten.
- **Findings carried to R3:** the READ-chNN.md members (READ-ch14x is chat 102's) and W-101…W-141 in
  WORKING-REGISTER.md; nothing is restated here. **Deferred cross-chapter items:** `DEFERRED.md`
  (**31 blocks**, chat 102's is the last) governs; do not re-derive.

## §0 Gate (each step its own tool call under `timeout 280`; any FAIL stops the chat with a report)

1. `ls -la /mnt/user-data/uploads /mnt/user-data/outputs /home/claude`; `recent_chats` confirms the
   latest chat is 102. Read `/mnt/project/CLAUDE.md` (project instruction; never a member).
2. Fetch both bundles by title: `Google Drive:search_files` with
   `title contains 'BUILD131_compendia' or title contains 'BUILD90_main'`, pageSize 5,
   excludeContentSnippets; `Google Drive:download_file_content` on each fileId. Both spill to
   `/mnt/user-data/tool_results/<id>.json`; note the two paths. MEASURED gate cost in chat 102: ≈ 17 %.
3. Bootstrap (the only step outside gate.py, because gate.py is a member):

```
timeout 280 python3 - <<'EOF'
import json, base64, hashlib, re, os
EXP={'main':'49065309b0c4fe8e055f693aed295cca','comp':'1b7bd7d4ebb895e82fc0a09758920a19'}
NAME={'main':'/home/claude/The_Method_1_6_BUILD90_main_and_register.md','comp':'/home/claude/The_Method_1_6_BUILD131_compendia_papers_audits.md'}
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
   **5,436,504 B · 1b7bd7d4ebb895e82fc0a09758920a19 · 68,085 lines**; **438 members extracted
   (2 + 436)**.
4. `python3 /home/claude/members/gate.py census` → `OK census: DEFECT-CENSUS.tsv byte-identical`
   (1,556 rows + header, ≈ 15 s).
5. `python3 /home/claude/members/gate.py run --core` → five `OK` (tower 976/1,654/2,535/13,585/
   70,905/199,130; kinds 1565 · 1356 · 499 · 149; minmax; r2-tools-constants; extent "1 to 1792").
6. `python3 /home/claude/members/gate.py manifest` → `MANIFEST OK`; MANIFEST.tsv **29,321 B ·
   6191d5fd10aca18abcf6f274068e4d00 · 438 lines**; WORKING-REGISTER.md **719,941 B ·
   910cc154eec99524d90cd6d891b30c16 · 6,365 lines**, ends **W-141**; DEFERRED.md **31 blocks**;
   RULINGS-R2.md 9,844 B · 10a2ea7e · 82 lines (unchanged); r2lib.py 21,022 B · 580d2ea2 · 453 lines
   (unchanged); gate.py 9,377 B · a01ef15a; close.py 6,456 B · 98acae67; r2-tools.py 6,529 B ·
   4702f5f9; tower-2.py c0bce27a; census.py f5a73e2b; kinds.py 4262f7c5; minmax.py 26da1d78. If two
   `BUILD*_compendia` files are present after a close, pass `--comp <path>` explicitly.
7. `python3 /home/claude/members/gate.py run r2-ch14x r2-ch14y` → two `OK` (chat 102's goldens:
   r2-ch14x.out 11,760 B · 6921d279 · 170 lines; r2-ch14y.out 12,494 B · e04bc1fb · 171 lines). Both
   import the lifted r2lib and read members only; an AttributeError means the extraction seated a
   pre-lift r2lib and the chat stops.
8. `python3 /home/claude/members/gate.py cert 103` → writes `/home/claude/GATE-ch103.txt`, verdict
   PASS only if every logged step passed. A FAIL anywhere stops the chat and is reported.

## What chat 102 did (do not repeat)

**§25–§25.5 is closed** — main **L6884–L6990, 107 lines, six headings**, cut decided from a full
chapter re-scan before a line was read. **Ten deviations, fourteen verified, nine incidentals, two
census rows closed** (1146 and 1147, both C9 heading artefacts, both *not a defect*). All of it is in
`READ-ch14x.md`; **do not re-measure any of it.**

**The findings that carry:**

- **14x-02 — the Register rules against the volume's own body text.** **Register 1751, Ruling 21**
  rules the Figure 25.1 caption to read *each of the 1,061 cells that yield a perturbation bound* and
  records that *the plot, §25.5 and seven other places count 1,061*. §25.5's body says the opposite
  twice — L6970 and L6986 assert a bound at all **1,442**. MEASURED: 1,061 at seven main sites (L60,
  L6517, L6683, L6958, L9354, L10266, L10277). **The difference is 381 cells; the caption is right.**
  New shape: **a ruled correction applied to a caption and not to the prose it captions** — R3 sweeps
  every Register ruling naming a caption or figure and checks the surrounding text moved with it.
- **14x-03 / 14x-04 — a printed quantity that does not follow, and a factor of two.** L6936's Hg II
  half-spacing prints **24,634 cm⁻¹** where 2*Z*²*R*/ν³ at *Z* = 2, ν = 5.3 gives **5,896.8**; the
  same section's ν_fail table reproduces **8 of 8 exactly** from that formula and R = 109,737.31568,
  so neither is in doubt. Separately L6932 states the condition on 2*Z*²*R*/ν³, L6934 requires a shift
  exceeding **half** the local spacing, and L6936 calls 2*Z*²*R*/ν³ itself the half-spacing —
  2*Z*²*R*/ν³ is the **full** spacing. **Load-bearing beyond §25**: the same condition is inverted
  into the 1,061 bounds at L9354 and defended at L10266.
- **14x-05 — the absent-member class, now with a measurement attached.** §25.2's exclusion (i) is
  worked on **Sr I** and prints *79 % coverage across the node* and *100 % on 11 cells*. **Sr has no
  row at any ionisation stage anywhere in six volumes.** No k/n with n < 40 gives 79.0 %.
- **14x-09 / 14x-10 — two compendium data defects found from the main volume.** Spectra **L562**
  prints `n 41–5` (the only malformed range in 596 rows; it is 41–55), and a whole-table sweep on
  identical (species, series label) returns **9 duplicated keys, 18 rows** — Ba III, **Ca II** and
  seven Si I channels — each pair **one bracket-tested, one untested**. That is 14r-19's shape;
  **that sweep and this one are complementary and both must run before any recount.**

**Two dockets resolve. 14t-06 closes** — §18's two exclusion tokens (L4927, L5152) are about excluded
functional forms; **the target is §25.2**, as the docket hypothesised, tested in five word-forms.
**The front matter's L62 closes** — §24.11's heading is *Four ways a species declines* and its table
gives four causes across five species rows; §25.2's five/N is a third, independent pairing, not a
contradiction. Remove both from the docket.

**A negative withdrawn before it was recorded:** §25.2 cites *Rule 3's direction-agnostic bracket* and
*Rule 3's min/max form*; Rule 3 is **Separation**, and reading L6045–L6046 shows the min/max form is
stated inside Rule 3's own paragraph and is direction-agnostic. **Both citations are supported.**

**Seven instrument faults, all self-caught and rewritten, none trimmed.** The four to carry: **run
symbol tests on the raw line** (emphasis-stripping killed `ν_V`); **case matters** (*Four* in a
heading); **match a printed figure at the source's precision** — test the band the printed ν's own
decimal allows and compare at that precision, which alone saved Al I's 1.398 and Ga I's 1.585 from
being recorded as deviations; and **identify the base before comparing** — a fine-structure splitting
is not a channel row, and the first version compared 17 against 29 before the question was asked
correctly.

## Chat 103's section read — §25.6–§25.6.6, which closes Chapter 25

MEASURED in chat 102 by full-chapter heading scan: **§25.6 L6991 through L7116**, 126 lines, seven
headings (L6991, 7003, 7021, 7039, 7059, 7071, 7093), the chapter ending before `## 26.` at L7117.
**Re-scan before reading.** The 141-line ceiling has held since chat 82 and 126 lines fits it, so the
chapter can close in one read.

- **What this unit already owes, from the docket:**
  - **14m-01 (docket 8)** — the §25.6 pointer with no target anywhere; the clause is **load-bearing
    for the novelty claim beside it**. Resolve it here and record whether the claim survives without
    it. This is the last docket item naming §25.6.
  - **14x-07's live half** — L6922 sends *r < 5* to §25.6, and `r < 5` has **one site in the whole
    main volume, L6922 itself**. Read §25.6 for the threshold in **its own words and every form** —
    a ratio stated as *five*, as *5:1*, or as a separation criterion is the same claim. Only record
    the pointer as failed after that test; testing one form is what wrongly produced 14r-22.
  - **The Sc VI deduction.** L6919 says *one further measurement would move Sc VI out of the
    exclusion entirely — which is what makes it the deduction of §25.6*. §25.6 is titled *The one
    deduction, and why it is not a prediction*. MEASURED: **Sc VI has 30 main-volume sites and no row
    in any compendium**; Sc carries stage III only in the channel table. §25.6.5 is *Nothing was
    fetched* and §25.6.3 is *What was already solved — not a prediction* — measure the deduction
    against the collection before accepting either.
  - **§25.6.4's *the one that was wrong*** — a point estimate the work records as wrong. Grep the
    Register for the entry that records it **before** calling any figure unreproducible.
  - **L7066 is one of the eight *An earlier version* sites** (docket 15) and sits in §25.6.4.
- **The channel table remains the arbiter for every species figure.** Section II is spectra-member
  **L293–L934**; its own totals line is **L900**: *596 channel rows across 28 elements · 2,269
  interior cells parsed.* Row format
  `| species | series | n | levels | interior | bracket | n* range | δ | σ(δ) | fits | limit cm⁻¹ |`;
  the column headed **fits** holds the ionisation stage; `bracket` reads `m/k`, `no-triple` or
  `untested`. Chat 102's parse agreed at **596 / 28 / 2,269** — bound every parse to that span and
  check it against L900 before trusting one figure from it. **B.1 Sources** is at spectra
  **L975–L986** and records no species held from two sources (14v-06).

Instruments: **r2-ch14z** (computable) and **r2-ch15a** (prose). Import `heading_line`,
`section_span`, `has_token` and `enclosing` from r2lib by path; **copy nothing**; **read members,
never a bundle**; **pass the resolvers the LINE LIST, not the member text**. Six functions are still
owed to r2lib and DEFERRED lists them; note that `heading_line` requires a trailing space after the
number, so the Register's bare `### 96` headings return None — locate Register entries with an
explicit `^#{1,4}\s*N\s*$` match (chats 99–102 all do this and it works).

**Standing method, unchanged and all of it earned:** exact-token heading resolver, never prefix; never
span a section by heading rank; grep lowercase `register NNN` by hand; check every printed pair count
against C(N, 2); resolve every pointer to the claim and not the heading, and before recording any
pointer as unresolved **read the target section and test for the claim as that section words it**,
case-exact, word-bounded, **and in the word's other forms**. Give every negative claim its own
witness and **state what a sweep covered before recording a negative from it**. Check the arithmetic
of every ratio and percentage; **never round with `round()`** — use `Decimal.quantize` and name the
convention. A formula numerator is not a value; a citation is not a declaration; a heading is not a
statement; a bound is not a measurement; a boundary case is not a violation; **a number beside a
species is not that species' ceiling** — read the header. Where the text prints a sample, measure the
population. **Compare bases before calling a carried figure wrong**, and **match a printed figure at
the source's precision, not at yours**. A convention stated in the source is not a defect. **Grep the
Register for a later entry naming the section before recording any figure as unreproducible** — that
is what produced 14x-02. **When an instrument disagrees with a hand reading already taken from the
file, or with a totals line the source states about itself, the instrument is wrong until proved
otherwise** — chats 94–102 hit that twice, four times, three, twice, twice, twice, twice, once and
three times.

## The repair docket

Carried forward until R3 executes it. **None of these goes to M.** Chat 102's additions are in
DEFERRED's chat-102 block in full; the docket below is the standing list, with **14t-06 struck** and
the front matter's L62 closed.

1. **§14.5.2–§14.5.7 — six heading-only sections, forty citations. R3's largest single item.**
   MEASURED against the Prints & Proofs original (738,550 B · md5 49900cf41f818ab789bb90fc596ac977):
   **authoring gap, not production loss.** Citations: §14.5.2 → 4, §14.5.3 → 1, §14.5.4 → 4,
   §14.5.5 → 4, §14.5.6 → 3, **§14.5.7 → 24**. **Order:** read the Register's nine §14.5.7 citations
   first and author to what they already say, then §21.5.4, then the Mathematical Compendium's
   twelve. Chat 90's **seed(Λ₈) = 7** is the settled material §14.5.7 owes.
2. **The §18.4.1 one-dimensional refinement — a missing Register entry** (main L5977–L5980).
   Register 319, which the passage cites, states a different claim.
3. **The Register has no entry for the correction §23.10.2 cites** (14n-A3) — a second missing entry,
   written when the chat-67 hold lifts, and interacting with 5 below.
4. **The σ collision — flagged for correction.** Rule 4 (main L6047) defines σ = 2R Z_eff² ·
   SE_pred / ν³; §22.5 (L6168) uses σ as the levels' measured uncertainty, and substituting Rule 4's
   σ into §22.5's r = 2Z²R/(ν³σ) cancels ν³ identically — MEASURED r = 100.000000 at ν = 10, 20, 40, 80.
   **Now paired with 14x-04**, which is the same rule block's factor of two.
5. **The Ruling 45 class, fifteen members** — L6453, the Figure 23.3 caption at L6483–L6484, chat 99's
   L6628 and L6632, chat 100's seven in 76 lines (L6748, L6756, L6791, L6801, L6803, L6810–L6812,
   L6813), and **chat 102's L6887 and L6907**. **L6812 — *it should be written that way wherever the
   figure carries weight* — is an instruction to the author printed in a reader-facing volume.**
   Captions state facts only; *fetch\** is established vocabulary and is not a member.
6. **The Ruling 46 class, sweepable in one pass** (14r-18) — **Build 9** at main L6693 and L7659,
   plus five Register sites (L20, L31, L65, L68 and one further). Run 5 and 6 together.
7. **§23.8.3's affine-invariance reason** (chat 96's 14l-16) — the docket's only *reason* item. R3
   must decide which invariance the chapter claims before rewriting, and check §29.2 L7881, §29.7
   L8052 and App D.4.1 L10377 for the same reasoning.
8. **The §25.6 pointer with no target** (chat 96's 14m-01) — author the explanation or drop the
   clause; the clause is load-bearing for the novelty claim beside it. **Chat 103 reads this
   section.**
9. **The pointer-off-by-one class, thirteen members, one withdrawn, one closed** — 14n-A1, 14n-A2,
   14n-A7, chat 95's 14k-01, chat 96's 14m-01, chat 98's 14q-02/03/04, chat 99's 14r-21, and chat
   102's **14x-07 (two in one sentence: *r < 5* → §25.6 and *ν > ν_V* → §23.11, both wrong)**.
   **14r-22 struck; 14t-06 closed at §25.2.** R3 sweeps **every §-pointer in the six volumes against
   the claim rather than the heading, in every form of the word**, and **on the raw line**.
10. **The unprinted-input class, now twenty members** — §22.1.2's δ = 0.35; §22.4.1's δ₂ = 0.06;
    L6060's 446×, L6068's 1,577, L6093's 3.47 %, L6104's *factor of 17*; §23.1 L6189's *agreement
    under 1 %*; §23.9.3's two columns; §23.10.3's displacement row; §23.12's window; the +0.86 Hill
    slope; the Kirkwood floor; chat 99's hydrogen row and Li II's s→f selection; chat 100's
    per-level provenance and the survival table's 0.125 printed 0.12; chat 101's §24.13 δ basis and
    §24.11's unlabelled *cells* column; and **chat 102's §25.2 fine-structure base (14x-06, whose J
    partner does not exist) and its 17-vs-16 interior count**. R3 splits the class into *conventions
    unstated* and *inputs absent*. **Q item P (L10958) already records the provenance split as
    owed** — repair them together, and with 14v-06's B.1 shape.
11. **The 32/11 scope docket** (14j-01), with six measured main-volume sites — L6193, L6213, L6233,
    L6237, L6381, L10245 — plus 2.909 at four. L6381 claims the floor as an original result and must
    be repaired **after** the scope decision, not with it.
12. **The truncation-printed-as-equality class** (14l-02, 14l-03, 14n-A10) — sweep every display
    equation whose own table disagrees with it, and every site printing 4ν/3.
13. **The two unsourced counts of L6517** (14n-A6, 14n-A7) — *619 refusals* and *§25.5's 1,061
    order-1 bounds*. §32.5 does carry the 1,061, so the pointer resolves; the recomputation at matched
    order is still owed. **Chat 102 read §25.5 and found L6517 supersedes it while 1,061 stands at
    six further main sites with no pointer to the supersession** — repair with 14x-02.
14. **The main-volume/compendium contradiction class** (14p-19, widened by 14r-01/02/03, chat 100's
    14t-02/07/08, chat 101's 14v-06 and **chat 102's 14x-05**) — every figure the main volume
    attributes to a named channel or to the collection, against the compendium's current rows and
    totals. **Resolve K I *n*d 45.7 first** (chat 98), **Ne I 16/131** (chat 99) and **K I 4/105**.
    **14r-19's double-tabulation must be settled before any recount — and it is now nine keys and 18
    rows wider (14x-10).**
15. **The retired-basis class** (14t-01), bounded to §24.8–§24.9 for Chapter 24. R3 sweeps every
    *An earlier version…* / *supersedes* / *and it does not* / *sharper than it was written* site in
    the six volumes and greps the retired wording forward from each — **in every form the figure
    takes**, word and numeral. MEASURED: *An earlier version* has **8 main sites** (L6066, L6280,
    L6483, L6628, L6632, **L6907**, **L7066**, L8676) and 1 register site. **Related and distinct:
    unretired text surviving its own correction** (14t-03/04/05), all inside §24.9.
16. **The Nesterov name-form sweep** (14m-07) — five forms in five places, one substantive (L8052
    credits Nesterov alone for a result §23.8.1 credits to both), plus *"KI"* without its space at
    L6657, L6716 and L6704, *"neon II"* spelled out at L6704, and the Edlén Handbuch chapter dated
    1960 at two sites and 1964 at five (14r-20), which also makes L6683's *sixty-five years old* wrong
    under both. **Chats 101 and 102 measured no name-form defect in their units.** **New and adjacent
    (14x-08): *Cooper-type node* at L6896 is unattributed, and the only Cooper in the bibliography is
    Cooper 1989 on k-consistency** — R3 sweeps every physics eponym against the bibliography for the
    same collision.
17. **The single-witness class** — chat 102 adds seven: **3.25, 24,634, 892,700, 55,000, 42,000,
    79 % and the factor of 60**. R4 should state which figures are unverifiable rather than leaving
    them looking checked, and distinguish *unverifiable* from *uncorroborated*.
18. **Heading sentences finishing in the body** (14q-06) — **three**: L4407 (+ "routes"), L6582
    (+ "one"), L8659 (+ "disanalogy"). Chats 101 and 102 confirmed none of their ten headings joins
    them.
19. **The false-universal class** (14v-01, and chat 99's He I monotone-fall claim). A sentence of the
    form *every X in this work…* is a computable claim about the collection and must be measured
    against the channel table. **Chat 102 adds L6970's *Every verified cell yields a bound*, refuted
    by Register 1751's own ruling** — see 14x-02. R3 sweeps every such construction in six volumes.
20. **The absent-member class** (14v-02, widened by **14x-05**). C IV has no row while C I, C II,
    C III and C V do; **Sr has no row at any stage at all**, and §25.2 prints coverage percentages
    for Sr I. MEASURED stage lists for the species Chapter 25 names: Ca I II IX; Ba II III; Ti III XI;
    Sc III; Hg II; Al I II III IV; Ga I II; Li I II III; **Sr none**. R3 sweeps every sequence and
    every worked example the main volume treats as present against the compendium's stage list.
21. **The end-rule overstatement** (14v-07) — §24.13's L6877 and L6879 generalise from the neutral end
    to both ends against the section's own table. Repair L6877 and L6879, not L6869. **A summary row
    that outruns the prose above it is its own shape** — sweep for it.
22. **The census anchor** (14v-08) — §24.12 must state which member of a sequence D is computed on,
    and print the census's range (27 + 12 + 5 = 44 sequences, range stated nowhere).
23. **The caption-corrected-but-not-the-prose class — new in chat 102** (14x-02). A Register ruling
    repaired the Figure 25.1 caption and the prose it captions still says the superseded thing. R3
    sweeps **every Register ruling naming a caption or a figure** and checks the surrounding text
    moved with it.
24. **Two compendium data defects — new in chat 102** (14x-09, 14x-10): spectra **L562**'s malformed
    `n 41–5` (read 41–55), and **nine duplicated (species, series) keys over 18 rows** with one copy
    tested and one untested in every pair.

## Close (chat 103)

`gate.py bank r2-ch14z r2-ch15a`; delete pycache in its own delete-only call; write `W-142.md`
(begins `### W-`, **ends with a blank line** — close.py asserts it); append a DEFERRED block as
`DEF-103.md`; then

```
timeout 280 python3 members/close.py --old The_Method_1_6_BUILD131_compendia_papers_audits.md \
  --new The_Method_1_6_BUILD132_compendia_papers_audits.md --w W-142.md \
  --main The_Method_1_6_BUILD90_main_and_register.md --append DEFERRED.md DEF-103.md \
  --members members/READ-ch14z.md members/CENSUS-CLOSURES-ch14z.tsv members/r2-ch14z.py \
  members/r2-ch14z.out members/r2-ch15a.py members/r2-ch15a.out
```

It must print **reverse recovers md5 1b7bd7d4ebb895e82fc0a09758920a19 == old: True** before writing;
if it does not, nothing is written and the failure is reported. `--append` arguments must precede
`--members`, and `--members` may be omitted entirely if nothing new is seated. **A changed
append-only member is grown with `--append <member> <delta-file>`, never passed to `--members`** —
close.py refuses a name collision, and a member needing *replacement* rather than growth has no
mechanism at all. After a close, `gate.py manifest` reports FAIL on changed members because the
extracted copies stay at pre-close state; **verify appends by reading the new bundle directly** —
and note the Register member lives in the **main** bundle, not the compendia bundle. `gate.py bank`
refuses to overwrite an existing `.out`; correcting an instrument after banking needs a
**delete-only** call to remove the golden, then bank again. Then copy BUILD132, HANDOFF-56 and the
READ file to `/mnt/user-data/outputs` and present them.

## Drive actions for M

- **Upload** to Materials (`1XX_5f3PZB6tjRtiZ2GIgd8Tt7i_4GgkY`): `HANDOFF-55.md` and
  `The_Method_1_6_BUILD131_compendia_papers_audits.md`.
- **Retire** once BUILD131 gates PASS in chat 103: HANDOFF-54 and BUILD130, plus any earlier
  compendia builds still present (BUILD107–BUILD129) **except BUILD124**.
- **Keep BUILD124** for now — it is the only input under which chat 96's `r2-ch14l` and `r2-ch14m`
  reproduce, and §23.9.1's eight exact V values live in `r2-ch14l.out`. Read those values out of the
  **member** rather than re-running the instrument; that is the pattern R3 should adopt before
  BUILD124 is retired.
- **Keep:** BUILD90 main (unchanged since chat 62), the **Prints & Proofs** folder
  (`1vYctzLppUZ2vFPJDCZ6wvkgSdj3v_f6n`) — the authentication baseline under Ruling 56 — the
  certificates, OWED-REGISTER-EXPANSIONS.md, OWED-EXPANSIONS-2.md, covers8.json, factor.py.

## Prompt for chat 103

"Chat 103. READ EVERYTHING BEFORE YOU DO ANYTHING. Live files: BUILD90 main (1,983,081 B, md5
49065309b0c4fe8e055f693aed295cca) and BUILD131 compendia (5,436,504 B, md5
1b7bd7d4ebb895e82fc0a09758920a19, 68,085 lines, 436 members). List uploads, outputs and /home/claude
first. Run HANDOFF-55's §0 gate in full and in order — fetch both bundles by title, bootstrap
(decode, md5, extract, expect 438 files), then gate.py census, run --core, manifest, run r2-ch14x
r2-ch14y, cert 103; any FAIL stops the chat with a report. Read RULINGS-R2.md last block first: the
chat-95 block governs and it says a finding is not a question — deviations in the mathematics and in
the prose are recorded and flagged for repair, never put to M, and Prints & Proofs is read before any
question is asked. Do not ask M to rule on a defect. Read DEFERRED.md; chat 102's block is the last of
thirty-one. The standing block's Phase 0–4 Löwdin/three-body plan is executed carried state; discard
it per Ruling 41 — its discard is W-118, not W-107. Line numbers are MEMBER line numbers and are never
carried between chats, and neither is any count or any heading list: re-scan Chapter 25 on
The_Method_1_6-2.md before reading a line. A Register line number is not a Register entry number —
quote an entry's headline before citing it. Chapter 25's §25–§25.5 closed in chat 102. Then continue
Phase R2 under the chat-81 cadence: read §25.6–§25.6.6, L6991 through L7116, 126 lines, seven
headings, which closes the chapter; the next ## heading is 26. at L7117. Read the unit in full, census
its claims into computable and prose, then run exactly two instrument batches, r2-ch14z computable and
r2-ch15a prose, importing heading_line, section_span, has_token and enclosing from r2lib — copy
nothing, pass them the LINE LIST and not the member text, and read the six volume MEMBERS, never a
BUILDnnn bundle path. Resolve 14m-01 there: the §25.6 pointer with no target, whose clause is
load-bearing for the novelty claim beside it. Test §25.6 for 'r < 5' in every form — a ratio stated as
five, as 5:1, or as a separation criterion is the same claim — because L6922 is the only site of that
string in the main volume and testing one form is what wrongly produced 14r-22. Measure the Sc VI
deduction against the collection: Sc VI has 30 main-volume sites and no row in any compendium, and Sc
carries stage III only. Grep the Register for the entry recording §25.6.4's point estimate that was
wrong before calling any figure unreproducible — that is what produced 14x-02, where Register 1751
ruled the Figure 25.1 caption to 1,061 and §25.5's body still asserts a bound at all 1,442. L7066 is
one of the eight 'An earlier version' sites. The Spectra Compendium's channel table is section II at
spectra L293–L934 and states its own totals at L900: 596 rows across 28 elements carrying 2,269
interior cells; bound every parse to that span and check it against L900 before trusting one figure
from it. The column headed fits carries the ionisation stage. Run symbol tests on the RAW line —
emphasis-stripping destroys the underscore and made ν_V invisible in chat 102. Make every token test
case-insensitive where a heading may carry the word capitalised. Match a printed figure at the
source's precision, not at yours: test the band the printed value's own decimal allows and compare at
that precision, because a boundary case is not a violation. Identify the base before comparing — a
fine-structure splitting is not a channel row. Digit-bound every numeral sweep. Give every negative
claim its own witness, and state what a sweep covered before recording a negative from it. Never
enumerate a domain with a fixed map. Where the text prints a sample, measure the population. A number
beside a species is not that species' ceiling — read the header. ν is not n. Never round with Python's
round() — use Decimal.quantize and name the convention. A heading is not a statement, a bound is not a
measurement, a citation is not a declaration. Read every verdict against the numbers printed above it
AND below it. When an instrument disagrees with a hand reading, or with a totals line the source
states about itself, suspect the instrument first. Close the section read before the next opens. At
close: bank both goldens with gate.py bank, write W-142 ending with a blank line, build BUILD132 with
close.py (reverse must recover 1b7bd7d4…), write HANDOFF-56. A changed append-only member is grown
with --append, never --members; correcting a banked golden needs a delete-only call first. No
corrections, no Register entries, no TASK 1 until the review closes. Handoff at 90–95 % of context or
on a closed section read — never earlier, never mid-section. Timeout on every call. Delete-only calls
for pycache, never chained to gate.py bank. Never copy over an existing file."
