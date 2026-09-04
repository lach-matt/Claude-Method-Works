# HANDOFF-56 — The Method 1.6 — chat 103 → chat 104

- Written from **chat 103** for **chat 104**. Live files: **BUILD90 main** (unchanged since chat 62)
  and **BUILD132 compendia** (= BUILD131 + W-142 + DEF-103 + six new members). Register **1 to 1792**
  (1,628 numbered entries, measured; unchanged — no Register entry since the chat-67 hold). W-142 IS
  seated; chat 104 seats nothing at open and writes W-143 at close.
- **Read RULINGS-R2.md at open, last block first.** The chat-95 block still governs and is still the
  last: **a finding is not a question.** A deviation in the mathematics or in the prose is recorded
  and **flagged for repair**, never put to M. **Prints & Proofs is read before any question is
  asked.** Only a choice no file can settle reaches M. The chat-81 cadence below it is unchanged.
- **Chapter 25 is CLOSED.** §25–§25.5 in chat 102, §25.6–§25.6.6 in chat 103. **Chapter 26 is
  unread**: `## 26. Collective sections` opens at main **L7117**.
- **Chapter 26's extent is NOT measured — measure it first.** No heading scan of Chapter 26 was run
  this chat beyond confirming its `##` at L7117 and `### 26.1 The assembly rule` at L7119. Scan the
  whole chapter on `The_Method_1_6-2.md` before reading a line and cut the unit against the 141-line
  ceiling that has held since chat 82.
- **A token test that fails names no target.** Chat 103's three failed pointers only became
  repairable when a **claim-locator** sweep ran beside the token test — where does *3.5%* actually
  live, where does *deductive* live. Add a locator to every pointer test from now on; a bare negative
  is half a finding.
- **Print a window around the match, not the head of the line.** These volumes carry lines past 200
  characters. Chat 103's first prose batch printed line heads and two clauses under test were
  invisible, which looked exactly like two mis-cited line numbers.
- **Identify the population before comparing.** The channel table supports three different bases and
  the volume's claims use all three words: **596 rows**, **2,269 interior cells**, **1,577 bracketed
  (verified) cells**. Chat 103's first computable batch compared a *verified cell* claim against
  interior cells.
- **Line numbering.** Main-volume lines are numbered on the **member** (`The_Method_1_6-2.md`,
  1-based, 11,855 lines); the bundle numbers each line one higher because of its `<<<FILE:` header.
- **Carried state to discard (Ruling 41):** the standing prompt block's "Phase 0–4"
  Löwdin/three-body plan is executed carried state; do not re-open it or put it to M. Its discard is
  **W-118 (chat 81)**, not W-107. The absorption is W-009 / W-059 / W-063 and Registers 1701–1724.
  Project knowledge holds BUILD12/BUILD53 only — list it, never read those bundles. Retired handoffs
  are gone from Drive; never fetch or cite one. **Never add HANDOFF-NN.md as a member.**
- **Known and pre-existing:** the compendia bundle carries **48 legacy `HANDOFF-NN.md` members**,
  identical in BUILD122–132. They extract into `members/` harmlessly, but a handoff must never be
  written into `members/` or passed to `--members`, or a seated member is silently overwritten.
- **Findings carried to R3:** the READ-chNN.md members (READ-ch14z is chat 103's) and W-101…W-142 in
  WORKING-REGISTER.md; nothing is restated here. **Deferred cross-chapter items:** `DEFERRED.md`
  (**32 blocks**, chat 103's is the last) governs; do not re-derive.

## §0 Gate (each step its own tool call under `timeout 280`; any FAIL stops the chat with a report)

1. `ls -la /mnt/user-data/uploads /mnt/user-data/outputs /home/claude`; `recent_chats` confirms the
   latest chat is 103. Read `/mnt/project/CLAUDE.md` (project instruction; never a member).
2. Fetch both bundles by title: `Google Drive:search_files` with
   `title contains 'BUILD132_compendia' or title contains 'BUILD90_main'`, pageSize 5,
   excludeContentSnippets; `Google Drive:download_file_content` on each fileId. Both spill to
   `/mnt/user-data/tool_results/<id>.json`; note the two paths. MEASURED gate cost in chat 103: ≈ 17 %.
3. Bootstrap (the only step outside gate.py, because gate.py is a member):

```
timeout 280 python3 - <<'EOF'
import json, base64, hashlib, re, os
EXP={'main':'49065309b0c4fe8e055f693aed295cca','comp':'8f2f9e70fefca6f02374c25365d9fe91'}
NAME={'main':'/home/claude/The_Method_1_6_BUILD90_main_and_register.md','comp':'/home/claude/The_Method_1_6_BUILD132_compendia_papers_audits.md'}
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
   **5,517,320 B · 8f2f9e70fefca6f02374c25365d9fe91 · 69,373 lines**; **444 members extracted
   (2 + 442)**.
4. `python3 /home/claude/members/gate.py census` → `OK census: DEFECT-CENSUS.tsv byte-identical`
   (1,556 rows + header, ≈ 15 s).
5. `python3 /home/claude/members/gate.py run --core` → five `OK` (tower 976/1,654/2,535/13,585/
   70,905/199,130; kinds 1565 · 1356 · 499 · 149; minmax; r2-tools-constants; extent "1 to 1792").
6. `python3 /home/claude/members/gate.py manifest` → `MANIFEST OK`; MANIFEST.tsv **29,723 B ·
   13f3c5cd8fe1295a0ece0f5c3ad8500e · 444 lines**; WORKING-REGISTER.md **724,126 B ·
   8d118bd2211e2ad758ad4bc3a24d730f · 6,420 lines**, ends **W-142**; DEFERRED.md **32 blocks**;
   RULINGS-R2.md 9,844 B · 10a2ea7e · 82 lines (unchanged); r2lib.py 21,022 B · 580d2ea2 · 453 lines
   (unchanged); gate.py 9,377 B · a01ef15a; close.py 6,456 B · 98acae67; r2-tools.py 6,529 B ·
   4702f5f9; tower-2.py c0bce27a; census.py f5a73e2b; kinds.py 4262f7c5; minmax.py 26da1d78. If two
   `BUILD*_compendia` files are present after a close, pass `--comp <path>` explicitly.
7. `python3 /home/claude/members/gate.py run r2-ch14z r2-ch15a` → two `OK` (chat 103's goldens:
   r2-ch14z.out 7,712 B · c6edbfac · 117 lines; r2-ch15a.out 18,539 B · 8c76814b · 284 lines). Both
   import the lifted r2lib and read members only; an AttributeError means the extraction seated a
   pre-lift r2lib and the chat stops.
8. `python3 /home/claude/members/gate.py cert 104` → writes `/home/claude/GATE-ch104.txt`, verdict
   PASS only if every logged step passed. A FAIL anywhere stops the chat and is reported.

## What chat 103 did (do not repeat)

**§25.6–§25.6.6 is closed, and with it Chapter 25** — main **L6991–L7116, 126 lines, seven
headings**, boundaries re-scanned before a line was read (the scan reproduced HANDOFF-55's figures
exactly). **Sixteen deviations, fifteen verified, eight incidentals, zero census rows in range**
(DEFECT-CENSUS.tsv carries no main-member row between L6991 and L7116 — measured, so the closure file
is a header only). All of it is in `READ-ch14z.md`; **do not re-measure any of it.**

**The findings that carry:**

- **14z-01 — the Register rules against a whole section.** **Register 801** — *BUT THERE ARE TWO
  BRACKETS IN THE BOOK, AND ONLY ONE OF THEM IS A DEDUCTION* — quotes §25.6.1's own sentence and
  rules *§22.1's bracket is a genuine deduction carrying no information; §25.6.1's carries
  information and is not a deduction*, closing *the book calls the bracket "a deduction, not a
  prediction" — true of the first, false of the second.* **Register 802** measures the premise:
  209 channels, δ monotone in 147, **91 fall and 56 rise**; 16 of the 52 with range above 0.1 are not
  monotone at all. **Register 803** states the trade-off. §25.6's body has not moved — L6991's
  heading, L7005, L7018, L7042, L7055. This is 14x-02's shape at section scale, and R3 must settle
  what §25.6 may call its result **before** touching the section's prose. The decision reaches §22.1,
  §23.10.1 and Figure 25.2's caption.
- **14z-02 — a bracket that inherits the estimate its own section forbids.** L7050's 7s lower edge
  784,128 solves back to **δ = 0.967887**, the *estimated* δ(6s) = 0.967891; L7057 says *a bracket
  that inherits an estimate is not a bracket*. From the last measured defect the edge is 783,646.
- **14z-03 / 14z-04 — a false universal and its dependent clause.** L7075's *every verified cell …
  at Z_eff between 1 and 3* against **60 bracket-tested rows and 172 bracketed cells above stage 3**,
  up to **Fe XVI**; *double the highest charge state tested* fails on either base — the tested
  maximum is **16**.
- **14z-05/06/07 — three failed pointers, and this time their real targets are located.** §24.2
  carries neither 3.5% nor 17% nor *tight end* nor Rule 4a; **3.5% lives at §22.2.3 (L6096–L6098),
  which names §25.6 and Sc VI in its own text**, and **17%'s other three main sites are all "17% of
  264 inputs"**, so that clause is unsupported anywhere. §24.6 is *The isoelectronic pairs* and
  carries no *deductive*, no *bracket*, no *monoton* — while L7115's "it" **is** the isoelectronic
  route. **The pointer-off-by-one class now stands at sixteen.**
- **14z-13 — the absent-member class takes a whole isoelectronic sequence.** Sc VI: 30 main sites,
  **0 in the other five volumes**; Sc appears only as **Sc III, 11 rows**; and **none of S I, Cl II,
  Ar III, K IV, Ca V has any row**, while L7099 says *both tabulated for all five*.

**Two dockets close as findings. 14m-01 (docket 8)** — §23.6 L6319's *the field abandoned the
variable* → §25.6: the unit carries **abandon/variable/literature/field/neglect/disuse/no
longer/out of use/dropped/unfashionab at 0× each**, and *abandon\** has three main sites in the whole
volume. Not repairable by redirection. **14x-07's live half** — `r < 5` → §25.6 tested in seven forms
on raw lines, **0× in every one**; `r < 5` has one main site, L6922 itself.

**What reproduced exactly, so R3 does not re-derive it:** the two-point Ritz solve (1.0889 / 0.9376 /
0.9679), **all nine printed energies** from limit **892,700**, R = 109,737.31568, Z_eff = 6, the four
widths (2,687 / 1,520 / 1,081 / 478), the factor 1.8, the convex tangent 0.9567, the nm window
(13.5743 / 13.5615 / 13.5895) and 91.338 eV. **735,091 is a boundary case, not a violation** — it
sits on the edge of the band its own δ's four decimals admit. The channel-table parse agrees with
spectra L900 at **596 / 28 / 2,269** and gives **1,577 bracketed cells**, independently reproducing
chat 100's figure. Brudno is properly attributed (main L11834, register L6395, math L3302/L3306, IoI
L1536) — **not a 14x-08 collision**.

**Four instrument faults, self-caught and rewritten, none trimmed.** Wrong population (interior vs
bracketed cells); head-truncated display hiding the clauses under test; the *thirty-five* sweep
contaminated by *one thousand six hundred and thirty-five* (20 sites → 5); and a comma-only numeral
sweep of the Register. **Faults 2 and 3 would each have produced a false record.**

## Chat 104's section read — Chapter 26, opening at L7117

- **Measure the chapter first.** `## 26. Collective sections` is at main **L7117** and `### 26.1 The
  assembly rule` at **L7119**; **nothing else about Chapter 26 is measured.** Run a full heading scan
  to the next `## `, then cut the unit — one section read, never split, never over the 141-line
  ceiling.
- **What the docket already owes anywhere in the volume**, and what chat 104 should test if its unit
  touches it: docket 5's Ruling 45 sweep (now **eighteen** members, chat 103 adding L6993, L6999 and
  L7040); docket 9's pointer sweep (**sixteen** members) — with a claim-locator beside every token
  test; docket 19's false-universal sweep (*every X in this work* is a computable claim about the
  collection); docket 20's absent-member sweep, which now covers Sr, C IV and the whole sulphur-like
  sequence.
- **The channel table remains the arbiter for every species figure.** Section II is spectra-member
  **L293–L934**; its own totals line is **L900**: *596 channel rows across 28 elements · 2,269
  interior cells parsed.* Row format
  `| species | series | n | levels | interior | bracket | n* range | δ | σ(δ) | fits | limit cm⁻¹ |`;
  the column headed **fits** holds the ionisation stage; `bracket` reads `m/k`, `no-triple` or
  `untested` (**392 / 78 / 126 rows**, 1,577 bracketed cells, 70 species, 61 of them tested).
  Bound every parse to that span and check it against L900 before trusting one figure from it.

Instruments: **r2-ch15b** (computable) and **r2-ch15c** (prose). Import `heading_line`,
`section_span`, `has_token` and `enclosing` from r2lib by path; **copy nothing**; **read members,
never a bundle**; **pass the resolvers the LINE LIST, not the member text**. Six functions are still
owed to r2lib and DEFERRED lists them; note that `heading_line` requires a trailing space after the
number, so the Register's bare `### 96` headings return None — locate Register entries with an
explicit `^#{1,4}\s*N\s*$` match (chats 99–103 all do this and it works), and **quote an entry's
headline before citing it — a Register line number is not an entry number.**

**Standing method, unchanged and all of it earned:** exact-token heading resolver, never prefix;
never span a section by heading rank; grep lowercase `register NNN` by hand; check every printed pair
count against C(N, 2); resolve every pointer to the claim and not the heading, **and locate where the
claim does live**; test on the **raw** line, case-insensitively, word-bounded, and in the word's
other forms. Give every negative claim its own witness and **state what a sweep covered before
recording a negative from it**. Check the arithmetic of every ratio and percentage; **never round
with `round()`** — use `Decimal.quantize` and name the convention. A formula numerator is not a
value; a citation is not a declaration; a heading is not a statement; a bound is not a measurement; a
boundary case is not a violation; **a number beside a species is not that species' ceiling**. Where
the text prints a sample, measure the population. **Compare bases before calling a carried figure
wrong**, and **match a printed figure at the source's precision, not at yours**. **Grep the Register
for a later entry naming the section before recording any figure as unreproducible** — that produced
14x-02 and, this chat, 14z-01. **When an instrument disagrees with a hand reading already taken from
the file, or with a totals line the source states about itself, the instrument is wrong until proved
otherwise** — chats 94–103 hit that twice, four times, three, twice, twice, twice, twice, once,
three times and four times.

## The repair docket

Carried forward until R3 executes it. **None of these goes to M.** Chat 103's additions are in
DEFERRED's chat-103 block in full; the docket below is the standing list, with **docket 8 closed as a
finding**.

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
   **Paired with 14x-04**, the same rule block's factor of two.
5. **The Ruling 45 class, eighteen members** — L6453, the Figure 23.3 caption at L6483–L6484, chat
   99's L6628 and L6632, chat 100's seven in 76 lines (L6748, L6756, L6791, L6801, L6803,
   L6810–L6812, L6813), chat 102's L6887 and L6907, and **chat 103's L6993, L6999 and L7040**.
   **L6812 — *it should be written that way wherever the figure carries weight* — is an instruction
   to the author printed in a reader-facing volume; L6999 — *That is stated here so a referee does
   not have to ask* — addresses a referee.** Captions state facts only; *fetch\** is established
   vocabulary and is not a member.
6. **The Ruling 46 class, sweepable in one pass** (14r-18) — **Build 9** at main L6693 and L7659,
   plus five Register sites (L20, L31, L65, L68 and one further). Run 5 and 6 together.
7. **§23.8.3's affine-invariance reason** (chat 96's 14l-16) — the docket's only *reason* item. R3
   must decide which invariance the chapter claims before rewriting, and check §29.2 L7881, §29.7
   L8052 and App D.4.1 L10377 for the same reasoning.
8. **CLOSED as a finding (14z-08), not as a repair.** §23.6 L6319's pointer into §25.6 has no target
   anywhere in the volume; R3 authors the explanation or drops the clause — the clause is
   load-bearing for the novelty claim beside it, and it **cannot be repaired by redirection**.
9. **The pointer-off-by-one class, sixteen members, one withdrawn, one closed** — 14n-A1, 14n-A2,
   14n-A7, chat 95's 14k-01, chat 96's 14m-01, chat 98's 14q-02/03/04, chat 99's 14r-21, chat 102's
   **14x-07** (two in one sentence, both now confirmed dead) and **chat 103's 14z-05, 14z-06,
   14z-07**. **14r-22 struck; 14t-06 closed at §25.2.** R3 sweeps **every §-pointer in the six
   volumes against the claim rather than the heading, in every form of the word**, **on the raw
   line**, and **with a claim-locator** so each failure names its candidate target.
10. **The unprinted-input class, now twenty-four members** — §22.1.2's δ = 0.35; §22.4.1's δ₂ = 0.06;
    L6060's 446×, L6068's 1,577, L6093's 3.47 %, L6104's *factor of 17*; §23.1 L6189's *agreement
    under 1 %*; §23.9.3's two columns; §23.10.3's displacement row; §23.12's window; the +0.86 Hill
    slope; the Kirkwood floor; chat 99's hydrogen row and Li II's s→f selection; chat 100's
    per-level provenance and the survival table's 0.125 printed 0.12; chat 101's §24.13 δ basis and
    §24.11's unlabelled *cells* column; chat 102's §25.2 fine-structure base (14x-06) and its
    17-vs-16 interior count; and **chat 103's ±1,594 and ±2,169 (84 bases swept, nothing within 13),
    the 892,700 ± 400 limit (one main site, L6914, none in the Register), *thirty-five other species*
    against 70/61, and the unstated series term of δ(4s)/δ(5s)**. R3 splits the class into
    *conventions unstated* and *inputs absent*. **Q item P (L10958) already records the provenance
    split as owed** — repair them together, and with 14v-06's B.1 shape.
11. **The 32/11 scope docket** (14j-01), with six measured main-volume sites — L6193, L6213, L6233,
    L6237, L6381, L10245 — plus 2.909 at four. L6381 claims the floor as an original result and must
    be repaired **after** the scope decision, not with it.
12. **The truncation-printed-as-equality class** (14l-02, 14l-03, 14n-A10) — sweep every display
    equation whose own table disagrees with it, and every site printing 4ν/3.
13. **The two unsourced counts of L6517** (14n-A6, 14n-A7) — *619 refusals* and *§25.5's 1,061
    order-1 bounds*. §32.5 does carry the 1,061, so the pointer resolves; the recomputation at matched
    order is still owed. Chat 102 found L6517 supersedes §25.5 while 1,061 stands at six further main
    sites with no pointer to the supersession — repair with 14x-02.
14. **The main-volume/compendium contradiction class** (14p-19, widened by 14r-01/02/03, chat 100's
    14t-02/07/08, chat 101's 14v-06, chat 102's 14x-05 and **chat 103's 14z-03/04 and 14z-13**) —
    every figure the main volume attributes to a named channel or to the collection, against the
    compendium's current rows and totals. **Resolve K I *n*d 45.7 first** (chat 98), **Ne I 16/131**
    (chat 99) and **K I 4/105**. **14r-19's double-tabulation must be settled before any recount —
    and it is nine keys and 18 rows wider (14x-10).**
15. **The retired-basis class** (14t-01), bounded to §24.8–§24.9 for Chapter 24. R3 sweeps every
    *An earlier version…* / *supersedes* / *and it does not* / *sharper than it was written* site in
    the six volumes and greps the retired wording forward from each — **in every form the figure
    takes**, word and numeral. MEASURED and re-confirmed in chat 103: *An earlier version* has
    **8 main sites** (L6066, L6280, L6483, L6628, L6632, L6907, **L7066**, L8676), **0 lower-case
    sites**, and 1 register site. **Related and distinct: unretired text surviving its own
    correction** (14t-03/04/05), all inside §24.9.
16. **The Nesterov name-form sweep** (14m-07) — five forms in five places, one substantive (L8052
    credits Nesterov alone for a result §23.8.1 credits to both), plus *"KI"* without its space at
    L6657, L6716 and L6704, *"neon II"* spelled out at L6704, and the Edlén Handbuch chapter dated
    1960 at two sites and 1964 at five (14r-20), which also makes L6683's *sixty-five years old* wrong
    under both. **New and adjacent (14x-08): *Cooper-type node* at L6896 is unattributed, and the only
    Cooper in the bibliography is Cooper 1989 on k-consistency** — R3 sweeps every physics eponym
    against the bibliography for the same collision. **Chat 103's Brudno check is the pattern for that
    sweep and came back clean.**
17. **The single-witness class** — chat 102's seven (3.25, 24,634, 892,700, 55,000, 42,000, 79 % and
    the factor of 60) plus chat 103's **±1,594, ±2,169, 1,081, 13.5743, 784,416 and 785,209**. R4
    should state which figures are unverifiable rather than leaving them looking checked, and
    distinguish *unverifiable* from *uncorroborated*. **Chat 103's counter-case: δ(4s), δ(5s) and δ̄
    all recur at L6114, so grep before recording.**
18. **Heading sentences finishing in the body** (14q-06) — **three**: L4407 (+ "routes"), L6582
    (+ "one"), L8659 (+ "disanalogy"). Chats 101, 102 and 103 confirmed none of their seventeen
    headings joins them.
19. **The false-universal class** (14v-01, chat 99's He I monotone-fall claim, chat 102's L6970, and
    **chat 103's L7075, broken twice over**). A sentence of the form *every X in this work…* is a
    computable claim about the collection and must be measured against the channel table. R3 sweeps
    every such construction in six volumes.
20. **The absent-member class** (14v-02, widened by 14x-05 and **14z-13**). C IV has no row while
    C I, C II, C III and C V do; **Sr has no row at any stage**; and **no member of the sulphur-like
    sequence S I, Cl II, Ar III, K IV, Ca V has a row**, while §25.6.6 prices a route on all five.
    MEASURED stage lists for the species Chapter 25 names: Ca I II IX; Ba II III; Ti III XI; Sc III;
    Hg II; Al I II III IV; Ga I II; Li I II III; **Sr none; Sc VI none**. R3 sweeps every sequence and
    every worked example the main volume treats as present against the compendium's stage list.
21. **The end-rule overstatement** (14v-07) — §24.13's L6877 and L6879 generalise from the neutral end
    to both ends against the section's own table. Repair L6877 and L6879, not L6869. **A summary row
    that outruns the prose above it is its own shape** — sweep for it.
22. **The census anchor** (14v-08) — §24.12 must state which member of a sequence D is computed on,
    and print the census's range (27 + 12 + 5 = 44 sequences, range stated nowhere).
23. **The caption-corrected-but-not-the-prose class** (14x-02), **now a section-scale class
    (14z-01)**. A Register ruling repaired the Figure 25.1 caption and its prose still says the
    superseded thing; Registers 801–803 rule on §25.6's *deduction* and the whole section still says
    the superseded thing. R3 sweeps **every Register ruling naming a caption, a figure or a section**
    and checks the surrounding text moved with it. **This is the largest live class after item 1.**
24. **Two compendium data defects** (14x-09, 14x-10): spectra **L562**'s malformed `n 41–5`
    (read 41–55), and **nine duplicated (species, series) keys over 18 rows** with one copy tested and
    one untested in every pair.
25. **The inherited-estimate class — new in chat 103** (14z-02). A bracket whose edge is set by an
    estimated rather than a measured input, in a section that disqualifies exactly that. Sweep every
    bracket in the six volumes for an edge that traces back to an estimate.

## Close (chat 104)

`gate.py bank r2-ch15b r2-ch15c`; delete pycache in its own delete-only call; write `W-143.md`
(begins `### W-`, **ends with a blank line** — close.py asserts it); append a DEFERRED block as
`DEF-104.md`; then

```
timeout 280 python3 members/close.py --old The_Method_1_6_BUILD132_compendia_papers_audits.md \
  --new The_Method_1_6_BUILD133_compendia_papers_audits.md --w W-143.md \
  --main The_Method_1_6_BUILD90_main_and_register.md --append DEFERRED.md DEF-104.md \
  --members members/READ-ch15b.md members/CENSUS-CLOSURES-ch15b.tsv members/r2-ch15b.py \
  members/r2-ch15b.out members/r2-ch15c.py members/r2-ch15c.out
```

It must print **reverse recovers md5 8f2f9e70fefca6f02374c25365d9fe91 == old: True** before writing;
if it does not, nothing is written and the failure is reported. `--append` arguments must precede
`--members`, and `--members` may be omitted entirely if nothing new is seated. **A changed
append-only member is grown with `--append <member> <delta-file>`, never passed to `--members`** —
close.py refuses a name collision, and a member needing *replacement* rather than growth has no
mechanism at all. After a close, `gate.py manifest` reports FAIL on changed members because the
extracted copies stay at pre-close state; **verify appends by reading the new bundle directly** —
and note the Register member lives in the **main** bundle, not the compendia bundle. `gate.py bank`
refuses to overwrite an existing `.out`; correcting an instrument after banking needs a
**delete-only** call to remove the golden, then bank again. **Rewriting an instrument before banking
also takes a delete-only call first** — never copy over an existing file. Then copy BUILD133,
HANDOFF-57 and the READ file to `/mnt/user-data/outputs` and present them.

## Drive actions for M

- **Upload** to Materials (`1XX_5f3PZB6tjRtiZ2GIgd8Tt7i_4GgkY`): `HANDOFF-56.md` and
  `The_Method_1_6_BUILD132_compendia_papers_audits.md`.
- **Retire** once BUILD132 gates PASS in chat 104: HANDOFF-55 and BUILD131, plus any earlier
  compendia builds still present (BUILD107–BUILD130) **except BUILD124**.
- **Keep BUILD124** for now — it is the only input under which chat 96's `r2-ch14l` and `r2-ch14m`
  reproduce, and §23.9.1's eight exact V values live in `r2-ch14l.out`. Read those values out of the
  **member** rather than re-running the instrument; that is the pattern R3 should adopt before
  BUILD124 is retired.
- **Keep:** BUILD90 main (unchanged since chat 62), the **Prints & Proofs** folder
  (`1vYctzLppUZ2vFPJDCZ6wvkgSdj3v_f6n`) — the authentication baseline under Ruling 56 — the
  certificates, OWED-REGISTER-EXPANSIONS.md, OWED-EXPANSIONS-2.md, covers8.json, factor.py.

## Prompt for chat 104

"Chat 104. READ EVERYTHING BEFORE YOU DO ANYTHING. Live files: BUILD90 main (1,983,081 B, md5
49065309b0c4fe8e055f693aed295cca) and BUILD132 compendia (5,517,320 B, md5
8f2f9e70fefca6f02374c25365d9fe91, 69,373 lines, 442 members). List uploads, outputs and /home/claude
first. Run HANDOFF-56's §0 gate in full and in order — fetch both bundles by title, bootstrap
(decode, md5, extract, expect 444 files), then gate.py census, run --core, manifest, run r2-ch14z
r2-ch15a, cert 104; any FAIL stops the chat with a report. Read RULINGS-R2.md last block first: the
chat-95 block governs and it says a finding is not a question — deviations in the mathematics and in
the prose are recorded and flagged for repair, never put to M, and Prints & Proofs is read before any
question is asked. Do not ask M to rule on a defect. Read DEFERRED.md; chat 103's block is the last of
thirty-two. The standing block's Phase 0–4 Löwdin/three-body plan is executed carried state; discard
it per Ruling 41 — its discard is W-118, not W-107. Line numbers are MEMBER line numbers and are never
carried between chats, and neither is any count or any heading list. Chapter 25 is CLOSED. Chapter 26
opens at L7117 and its extent is NOT measured: run a full heading scan on The_Method_1_6-2.md to the
next ## before reading a line, then cut one section read against the 141-line ceiling. A Register line
number is not a Register entry number — quote an entry's headline before citing it, as chat 103 did
for Registers 801–803. Then continue Phase R2 under the chat-81 cadence: read the unit in full,
census its claims into computable and prose, then run exactly two instrument batches, r2-ch15b
computable and r2-ch15c prose, importing heading_line, section_span, has_token and enclosing from
r2lib — copy nothing, pass them the LINE LIST and not the member text, and read the six volume
MEMBERS, never a BUILDnnn bundle path. Give every pointer test a claim-locator beside it: a token test
that fails names no target, and chat 103's three failed pointers only became repairable when the
locator found where 3.5% and deductive actually live. Print a window around each match, never the head
of the line — these lines run past 200 characters and chat 103's first prose batch hid the very
clauses under test. Identify the population before comparing: the channel table is 596 rows, 2,269
interior cells and 1,577 bracketed cells, and the volumes' claims use all three words. Section II is
spectra L293–L934 with its own totals at L900; the column headed fits carries the ionisation stage.
Run symbol tests on the RAW line. Make every token test case-insensitive where a heading may carry
the word capitalised, and filter compound numerals before counting a spelled-out number. Match a
printed figure at the source's precision, not at yours — a boundary case is not a violation. Digit-
bound every numeral sweep and sweep both the comma and comma-free forms. Give every negative claim its
own witness, and state what a sweep covered before recording a negative from it. Never enumerate a
domain with a fixed map. Where the text prints a sample, measure the population. A number beside a
species is not that species' ceiling — read the header. ν is not n. Never round with Python's round()
— use Decimal.quantize and name the convention. A heading is not a statement, a bound is not a
measurement, a citation is not a declaration. Grep the Register before recording any figure as
unreproducible or as a single witness — that produced 14x-02 and 14z-01, and it saved three
single-witness entries this chat. When an instrument disagrees with a hand reading, or with a totals
line the source states about itself, suspect the instrument first. Close the section read before the
next opens. At close: bank both goldens with gate.py bank, write W-143 ending with a blank line, build
BUILD133 with close.py (reverse must recover 8f2f9e70…), write HANDOFF-57. A changed append-only
member is grown with --append, never --members; correcting a banked golden needs a delete-only call
first, and so does rewriting an instrument before it is banked. No corrections, no Register entries,
no TASK 1 until the review closes. Handoff at 90–95 % of context or on a closed section read — never
earlier, never mid-section. Timeout on every call. Delete-only calls for pycache, never chained to
gate.py bank. Never copy over an existing file."
