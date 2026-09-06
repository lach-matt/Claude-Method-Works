# HANDOFF-59 — The Method 1.6 — chat 106 → chat 107

- Written from **chat 106** for **chat 107**. Live files: **BUILD90 main** (unchanged since chat
  62) and **BUILD135 compendia** (= BUILD134 + W-145 + DEF-106 + six new members). Register
  **1 to 1792** (no Register entry since the chat-67 hold). W-145 IS seated; chat 107 seats nothing
  at open and writes W-146 at close.
- **Read RULINGS-R2.md at open, last block first.** The chat-95 block still governs and is still
  the last: **a finding is not a question.** A deviation in the mathematics or in the prose is
  recorded and **flagged for repair**, never put to M. **Prints & Proofs is read before any
  question is asked.** Only a choice no file can settle reaches M. The chat-81 cadence is unchanged.
- **Chapter 27 is CLOSED. Chapter 28 is OPEN.** Chat 106 read **L7332–L7457** (§27.6, PART VI,
  §28–§28.5, 126 lines). **§28.6 opens at L7458**; the chapter runs to **L7855** and `## 29.` opens
  at **L7856**. Re-measure by heading scan anyway — a handoff figure is not a measurement — and
  resolve every chapter heading to its **body** occurrence: the contents entries sit at L147–L151.
- **Chapter 28 is long (490 lines) and its subsections are uneven.** MEASURED heading line numbers,
  to be re-taken: 28.6 L7458, 28.7 L7481, 28.7.1 L7506, 28.7.2 L7531, 28.7.3 L7559, 28.7.4 L7644,
  28.7.5 L7664, 28.7.6 L7677, 28.7.7 L7678, 28.7.8 L7684, 28.7.9 L7689, 28.8 L7721, 28.9 L7772,
  28.9.1 L7774, **28.10 at L8222 — inside Chapter 29**. Cut one unit at a section boundary under
  the 141-line ceiling; **§28.6 through §28.7.2 is L7458–L7558, 101 lines**, and is the natural
  next unit. Never split a section read across chats.
- **Census rows in that unit, MEASURED from DEFECT-CENSUS.tsv with `member == 'main'`:** 1160
  (L7466, C9, *never*) and whatever else falls in the range — measure it, do not carry this figure.
  The census column is `member`, not `volume`; keying on the wrong name silently returns zero rows.
- **Chapter 28 is the chapter that describes the Register's own size, and it does so three ways.**
  Chat 106 measured 1,635 as a **heading** count (1,628 bare + 7 grouped headings carrying 32
  numbers), **1,660 distinct numbered entries**, and L7658's separate *1,631*. Chat 107 will read
  L7658 in situ. Do not re-derive the counts; they are in READ-ch15f.md and DEF-106 item 2.
- **A heading match is not a body match; a theorem number is not a section number; test a symbol as
  a symbol.** All three still bite. And **a lettered heading (§E.1.4) is invisible to
  `heading_line`** — match `^#{2,4}\s*E\.1\.4\b` explicitly, as r2-ch15g does.
- **Line numbering.** Main-volume lines are numbered on the **member** (`The_Method_1_6-2.md`,
  1-based, 11,855 lines); the bundle numbers each line one higher because of its `<<<FILE:` header.
- **Carried state to discard (Ruling 41):** the standing prompt block's "Phase 0–4"
  Löwdin/three-body plan is executed carried state; do not re-open it or put it to M. Its discard
  is **W-118 (chat 81)**. Project knowledge holds BUILD12/BUILD53 only — list it, never read those
  bundles. Retired handoffs are gone from Drive; never fetch or cite one. **Never add HANDOFF-NN.md
  as a member.**
- **Known and pre-existing:** the compendia bundle carries **48 legacy `HANDOFF-NN.md` members**,
  identical in BUILD122–135. They extract into `members/` harmlessly, but a handoff must never be
  written into `members/` or passed to `--members`, or a seated member is silently overwritten.
- **Findings carried to R3:** the READ-chNN.md members (READ-ch15f is chat 106's) and W-101…W-145
  in WORKING-REGISTER.md; nothing is restated here. **Deferred cross-chapter items:** `DEFERRED.md`
  (**35 blocks**, chat 106's is the last) governs; do not re-derive.

## §0 Gate (each step its own tool call under `timeout 280`; any FAIL stops the chat with a report)

1. `ls -la /mnt/user-data/uploads /mnt/user-data/outputs /home/claude`; `recent_chats` confirms the
   latest chat is 106. Read `/mnt/project/CLAUDE.md` (project instruction; never a member).
2. Fetch both bundles by title: `Google Drive:search_files` with
   `title contains 'BUILD135_compendia' or title contains 'BUILD90_main'`, pageSize 5,
   excludeContentSnippets; `Google Drive:download_file_content` on each fileId. Both spill to
   `/mnt/user-data/tool_results/<id>.json`; note the two paths. MEASURED gate cost in chat 106:
   ≈ 20 %.
3. Bootstrap (the only step outside gate.py, because gate.py is a member):

```
timeout 280 python3 - <<'EOF'
import json, base64, hashlib, re, os
EXP={'main':'49065309b0c4fe8e055f693aed295cca','comp':'255fac94aff1232dc221750c1eb938d5'}
NAME={'main':'/home/claude/The_Method_1_6_BUILD90_main_and_register.md','comp':'/home/claude/The_Method_1_6_BUILD135_compendia_papers_audits.md'}
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

   Expected: main 1,983,081 B · `49065309b0c4fe8e055f693aed295cca` · 18,470 lines; compendia
   **5,744,660 B · `255fac94aff1232dc221750c1eb938d5` · 72,779 lines**; **462 members extracted
   (2 + 460)**.
4. **Fetch the Prints & Proofs original before step 7** — `r2-ch15e` reads it and will fail on a
   missing path. Folder `1vYctzLppUZ2vFPJDCZ6wvkgSdj3v_f6n`, title `The Method 1.6.md`, fileId
   `1vsWwRT9BmUNeMrqokuo4jI4DJnoADubH`, **738,550 B · md5 49900cf41f818ab789bb90fc596ac977**,
   written to `/home/claude/PP_The_Method_1_6.md`.
5. `python3 /home/claude/members/gate.py census` → `OK census: DEFECT-CENSUS.tsv byte-identical`
   (1,556 rows + header, ≈ 15 s).
6. `python3 /home/claude/members/gate.py run --core` → five `OK` (tower 976/1,654/2,535/13,585/
   70,905/199,130; kinds 1565 · 1356 · 499 · 149; minmax; r2-tools-constants; extent "1 to 1792").
7. `python3 /home/claude/members/gate.py manifest` → `MANIFEST OK`; MANIFEST.tsv **30,935 B ·
   bab70edb57fa1b7771bcda42dbd41e12 · 462 lines**; WORKING-REGISTER.md **737,784 B ·
   8125b8b01ea648df86cc453b1d4a9306 · 6,603 lines**, ends **W-145**; DEFERRED.md **35 blocks**;
   RULINGS-R2.md 9,844 B · 10a2ea7e · 82 lines (unchanged); r2lib.py 21,022 B · 580d2ea2 · 453
   lines (unchanged); gate.py 9,377 B · a01ef15a; close.py 6,456 B · 98acae67; r2-tools.py 6,529 B
   · 4702f5f9; tower-2.py c0bce27a; census.py f5a73e2b; kinds.py 4262f7c5; minmax.py 26da1d78.
   If two `BUILD*_compendia` files are present after a close, pass `--comp <path>` explicitly.
8. `python3 /home/claude/members/gate.py run r2-ch15f r2-ch15g` → two `OK` (chat 106's goldens:
   r2-ch15f.out 18,740 B · 91d6b149 · 233 lines; r2-ch15g.out 13,831 B · 6df20834 · 208 lines).
9. `python3 /home/claude/members/gate.py cert 107` → writes `/home/claude/GATE-ch107.txt`, verdict
   PASS only if every logged step passed. A FAIL anywhere stops the chat and is reported.

## What chat 106 did (do not repeat)

**Unit L7332–L7457 read, censused, instrumented in two batches, closed.** Nine deviations, eight
verified groups, six incidentals, five census rows disposed. All of it is in `READ-ch15f.md`;
**do not re-measure any of it.** The five that carry:

- **15f-01 — the per-cell σ coverage is printed twice, differently.** §22.2.1 **L6063** 69.6 %,
  §28.4 **L7442** 68.1 % *"the expected figure"*; erf(1/√2) = **68.2689 %** → 68.3 under both
  conventions. Same error, same pooled 96.2 %, 1.5 pp apart.
- **15f-02 — "1,635 entries" is a heading count.** 1,628 bare `### N` + **7 grouped headings**
  (reg L1319, L1323, L1327, L1331, L1335, L1339, L1343) carrying **32** numbers, none duplicated
  in the bare set → headings 1,635, **entries 1,660**, extent 1 to 1792 with 132 numbers unused.
  L7658 prints a third figure, 1,631.
- **15f-03 — the chapter's head sentence counts 26 post-closure withdrawals; its own headings list
  262.** 6 + 8 + 12 is exact for §28.7–28.7.2, but 28.7.3/.4/.6/.7 add 75 + 40 + 2 + 119.
- **15f-05 — §28.10 is printed inside Chapter 29**, at L8222 between §29.11.2 and §29.12. The
  review's first measured out-of-order section.
- **15f-06 / 15f-07 — "exactly one infinity in the whole construction"** is contradicted by Λ_cinf
  (c → ∞) and by L = −∞ at the node floor; and **§6.1 does not state `max ∅ = −∞`** (it is at mc
  L326) although both L7340 and **Register 447's headline** cite it for that.

**Five instrument faults, self-caught, rewritten, none trimmed.** Two of them had the instrument
disagreeing with a hand reading of §28.2 and §28.4 — **the book was right both times**; a phrase
sweep called "10 of 16" absent when it is wrapped across L7416–17; F1 called 1,628-against-1,635 a
deviation before reading the seven grouped headings; G5 counted block boundaries as mid-sentence
breaks. **Sweep phrases on the two-line join as well as the raw line** — this book wraps.

## Chat 107's section read — §28.6 through §28.7.2

- **Re-measure the extent by heading scan before reading a line.** The proposed unit is
  **L7458–L7558, 101 lines** (§28.6, §28.7, §28.7.1, §28.7.2), closing before §28.7.3's 75-item
  block at L7559. Cut it yourself; do not trust the figure above.
- **This unit prints counts of withdrawals by class.** Every one is computable against the Register
  and against 15f-02's measured entry count — count the items in each section against its own
  heading numeral, as F4 did, and expect the instrument to be wrong before the book is.
- **What the docket owes anywhere in the volume**, to test if the unit touches it: docket 5's
  Ruling 45 sweep (twenty-one members plus chat 106's seven candidates); **docket 6's Ruling 46
  sweep, now MEASURED at seventeen main-volume sites** — run 5 and 6 in one pass; docket 9's
  pointer sweep (eighteen members, §24.6 a magnet); docket 19's false-universal sweep, which
  15f-06 has just widened; docket 20's absent-member sweep (Sr, C IV, the sulphur-like sequence,
  Rb); the duplicated-section sweep (DEF-105 item 1); and **the new heading-order sweep** (DEF-106
  item 5).
- **The channel table remains the arbiter for every species figure.** Section II is spectra-member
  **L293–L934**; its totals line is **L900**: *596 channel rows across 28 elements · 2,269 interior
  cells parsed.* The column headed **fits** holds the ionisation stage; `bracket` reads `m/k`,
  `no-triple` or `untested` (**392 / 78 / 126 rows**, 1,577 bracketed cells, 70 species, 61 tested).
  Bound every parse to that span and check it against L900 before trusting one figure from it.

Instruments: **r2-ch15h** (computable) and **r2-ch15i** (prose). Import `heading_line`,
`section_span`, `has_token` and `enclosing` from r2lib by path; **copy nothing**; **read members,
never a bundle**; **pass the resolvers the LINE LIST, not the member text**. Six functions are
still owed to r2lib and DEFERRED lists them; `heading_line` requires a trailing space after the
number, so the Register's bare `### 96` headings return None — locate Register entries with an
explicit `^#{1,4}\s*N\s*$` match, **and now also `^#{1,4}\s*N\s*,` for the seven grouped
headings**. **Quote an entry's headline before citing it — a Register line number is not an entry
number.**

**Standing method, unchanged and all of it earned:** exact-token heading resolver, never prefix,
resolved to the **body** occurrence; never span a section by heading rank; grep lowercase
`register NNN` by hand; check every printed pair count against C(N, 2) **and name the
denominator**; resolve every pointer to the claim and not the heading, **and locate where the claim
does live**; test on the **raw** line, case-insensitively, word-bounded, in the word's other forms,
**in the symbol as well as the name**, **and on the two-line join as well as the line**. Give every
negative claim its own witness and **state what a sweep covered before recording a negative from
it**. Check the arithmetic of every ratio and percentage; **never round with `round()`** — use
`Decimal.quantize` and name the convention, sweeping **both** when the last place is in doubt.
**Sweep the convention, not just the base** — log base, centring, rounding mode, denominator and
physical constant have all moved a verdict, and **so has the definition of what is being counted**
(15f-02: headings against entries). A formula numerator is not a value; a citation is not a
declaration; a heading is not a statement; a bound is not a measurement; an assertion is not a
proof; a theorem number is not a section number; a structurally forced figure is not a finding;
**a count of headings is not a count of what they contain**. Where the text prints a sample,
measure the population. **Match a printed figure at the source's precision, not at yours.** **Grep
the volume and the Register for a later or exact statement before recording any figure as
unreproducible.** **When an instrument disagrees with a hand reading already taken from the file,
or with a totals line the source states about itself, the instrument is wrong until proved
otherwise** — chats 94–106 hit that twice, four times, three, twice, twice, twice, twice, once,
three times, four times, ten times, seven times and **five times**.

## The repair docket

Carried forward until R3 executes it. **None of these goes to M.** Chat 106's additions are in
DEFERRED's chat-106 block in full; the docket below is the standing list, unchanged from
HANDOFF-58 except where chat 106 moved it.

1. **§14.5.2–§14.5.7 — six heading-only sections, forty citations. R3's largest single item.**
   MEASURED against Prints & Proofs: **authoring gap, not production loss.** Citations: §14.5.2 → 4,
   §14.5.3 → 1, §14.5.4 → 4, §14.5.5 → 4, §14.5.6 → 3, **§14.5.7 → 24**. **Order:** read the
   Register's nine §14.5.7 citations first and author to what they already say, then §21.5.4, then
   the Mathematical Compendium's twelve. Chat 90's **seed(Λ₈) = 7** is the settled material.
2. **The §18.4.1 one-dimensional refinement — a missing Register entry** (main L5977–L5980).
   Register 319, which the passage cites, states a different claim.
3. **The Register has no entry for the correction §23.10.2 cites** (14n-A3) — a second missing
   entry, written when the chat-67 hold lifts, interacting with 5 below.
4. **The σ collision — flagged for correction.** Rule 4 (main L6047) defines σ = 2R Z_eff² ·
   SE_pred / ν³; §22.5 (L6168) uses σ as the levels' measured uncertainty, and substituting cancels
   ν³ identically — MEASURED r = 100.000000 at ν = 10, 20, 40, 80. **Paired with 14x-04.**
   **Now also paired with 15f-01**, which is the same rule's per-cell justification priced twice.
5. **The Ruling 45 class, twenty-one members plus chat 106's seven candidates** — L6453, the Figure
   23.3 caption L6483–84, L6628, L6632, chat 100's seven in 76 lines, L6887, L6907, L6993, L6999,
   L7040, L7201, L7244, L7312, and now L7357, L7361, L7368, L7372–75, L7381, L7426's heading tag
   *retained in the compendium*, L7456. Captions state facts only; *fetch\** is established
   vocabulary and is not a member.
6. **The Ruling 46 class — re-scoped by MEASUREMENT to seventeen main-volume sites** (15f-04):
   L994, L1401, L4151, L6693, L7373, L7374, L7658, L7659 and nine further, plus five Register
   sites (L20, L31, L65, L68 and one further). Run 5 and 6 together.
7. **§23.8.3's affine-invariance reason** (14l-16) — the docket's only *reason* item; check §29.2
   L7881, §29.7 L8052, App D.4.1 L10377. **15b-07 lands in the same neighbourhood: §23.8.1 L6345 is
   λ²'s home and L7185 should point there.**
8. **CLOSED as a finding (14z-08), not as a repair.** §23.6 L6319's pointer into §25.6 has no
   target anywhere in the volume; the clause is load-bearing and **cannot be repaired by
   redirection**.
9. **The pointer-off-by-one class, nineteen members, one withdrawn, one closed** — 14n-A1/A2/A7,
   14k-01, 14m-01, 14q-02/03/04, 14r-21, 14x-07 (two in one sentence), 14z-05/06/07, 15b-07,
   15b-08, and **15f-07 (main L7340 and Register 447 → §6.1 for a convention that lives at mc
   L326)**. R3 sweeps **every §-pointer in the six volumes against the claim rather than the
   heading**, on the raw line, with a claim-locator. **§24.6 is a magnet.**
10. **The unprinted-input class, thirty-two members.** R3 splits it into *conventions unstated* and
    *inputs absent*; Q item P (L10958) records the provenance split as owed. **Sub-class from
    15d-03: denominators unstated.** **New sub-class from 15f-02: the unit of a count unstated** —
    heading against entry.
11. **The 32/11 scope docket** (14j-01), six measured main sites — L6193, L6213, L6233, L6237,
    L6381, L10245 — plus 2.909 at four. **L6237 also states the exact rational V** and Chapter 27
    depends on it; do not disturb it without re-checking §27.2.
12. **The truncation-printed-as-equality class** (14l-02/03, 14n-A10, 15b-04, 15d-02, L7308's
    asymptote-as-price). **15d-02 now also falsifies §27.6's universal at L7357** (item 9 of
    DEF-106) — repair them together.
13. **The two unsourced counts of L6517** (14n-A6/A7) — *619 refusals* and *§25.5's 1,061 order-1
    bounds*; the recomputation at matched order is still owed.
14. **The main-volume/compendium contradiction class** (14p-19, 14r-01/02/03, 14t-02/07/08, 14v-06,
    14x-05, 14z-03/04/13, 15b-06). **Resolve K I *n*d 45.7 first**, **Ne I 16/131** and **K I
    4/105**. 14r-19's double-tabulation must be settled before any recount.
15. **The retired-basis class** (14t-01). MEASURED: *An earlier version* has **8 main sites**
    (L6066, L6280, L6483, L6628, L6632, L6907, L7066, L8676). **Adjacent: pc L653's *Withdrawn at
    register 1168* against §26.5's live *66 of 66***.
16. **The Nesterov name-form sweep** (14m-07) — five forms in five places, one substantive (L8052);
    *"KI"* without its space at L6657/L6716/L6704; *"neon II"* at L6704; Edlén dated 1960 at two
    sites and 1964 at five (14r-20), which makes L6683's *sixty-five years old* wrong under both.
    **14x-08: *Cooper-type node* at L6896 is unattributed.** Birkhoff, Brudno, Singer, Aitken and
    the 2004 survey all came back clean.
17. **The single-witness class** — chat 102's seven, 103's six, 104's four, **chat 106's two
    (*2,163* L7429, *473 million* L7338)**. R4 should state which figures are unverifiable rather
    than leaving them looking checked.
18. **Heading sentences finishing in the body** (14q-06) — three: L4407, L6582, L8659. Chats
    101–106 confirmed none of their headings joins them.
19. **The false-universal class** (14v-01, the He I monotone-fall claim, L6970, L7075 broken twice
    over) — **and now 15f-06, *exactly one infinity in the whole construction*, broken by Λ_cinf
    and by L = −∞ at the node floor.** A sentence of the form *every X in this work…* is a
    computable claim and must be measured.
20. **The absent-member class** (14v-02, 14x-05, 14z-13, 15b-09). C IV, **Sr at any stage**, the
    sulphur-like sequence, **Rb in six volumes**. MEASURED stage lists: Ca I II IX; Ba II III;
    Ti III XI; Sc III; Hg II; Al I II III IV; Ga I II; Li I II III; **Sr none; Sc VI none; Rb none.**
21. **The end-rule overstatement** (14v-07) — §24.13's L6877 and L6879. **A summary row that
    outruns the prose above it is its own shape** — and **15f-03 is the same shape running the
    other way**, a summary that undercounts the sections below it. Sweep for both.
22. **The census anchor** (14v-08) — §24.12 must state which member of a sequence D is computed on,
    and print the census's range (27 + 12 + 5 = 44 sequences).
23. **The caption-corrected-but-not-the-prose class** (14x-02), at section scale (14z-01),
    cross-volume (15b-06) and Register-scale (15d-05). **15f-07 adds a fourth Register-scale
    member: Register 447's headline carries the same failed pointer as the prose.** R3 sweeps every
    Register ruling naming a caption, a figure or a section. **The largest live class after item 1.**
24. **Two compendium data defects** (14x-09/10): spectra **L562**'s malformed `n 41–5` (read
    41–55), and **nine duplicated (species, series) keys over 18 rows**.
25. **The inherited-estimate class** (14z-02) — sweep every bracket for an edge tracing back to an
    estimate.
26. **The spliced-text class, one member** (15b-01/02) — main **L7156**. **Adjacent: §29.8's L8089
    cell cites its own section.** **15f-08's mid-sentence break at L7405–07 is the formatting
    cousin** — sweep both together.
27. **The duplicated-section class (15d-01).** §9.2 L1961–L1990 and §27.5.1 L7299–L7330 are one
    passage with two Register entries, 438 and 446. **Chat 106 ran the sweep on its own unit: 0 of
    71 long lines recur** — the class has no second member yet.
28. **Table formatting (15d-04)** — four of Chapter 27's five tables are space-aligned and §27.1's
    is shattered mid-word, in Prints & Proofs too. **Now joined by 15f-09: thirty main-volume
    sections open in lower case directly under their heading.** One formatting pass.
29. **NEW — section order (15f-05).** **§28.10 is printed inside Chapter 29 at L8222.** R3 moves or
    renumbers it and re-checks the contents list, the Index of Indices and every pointer assuming
    source order. **Sweep owed: heading order across every chapter of the six volumes.**
30. **NEW — the Register's own size (15f-02).** Three figures in one chapter — 1,635 (headings),
    1,631 (L7658), and a measured 1,660 entries. R3 fixes the unit of the count, states it once,
    and drives every site to it, with the kinds table and the extent sites.

## Close (chat 107)

`gate.py bank r2-ch15h r2-ch15i`; delete pycache in its own delete-only call; write `W-146.md`
(begins `### W-`, **ends with a blank line** — close.py asserts it); append a DEFERRED block as
`DEF-107.md`; then

```
timeout 280 python3 members/close.py --old The_Method_1_6_BUILD135_compendia_papers_audits.md \
  --new The_Method_1_6_BUILD136_compendia_papers_audits.md --w W-146.md \
  --main The_Method_1_6_BUILD90_main_and_register.md --append DEFERRED.md DEF-107.md \
  --members members/READ-ch15g.md members/CENSUS-CLOSURES-ch15g.tsv members/r2-ch15h.py \
  members/r2-ch15h.out members/r2-ch15i.py members/r2-ch15i.out
```

It must print **reverse recovers md5 255fac94aff1232dc221750c1eb938d5 == old: True** before
writing; if it does not, nothing is written and the failure is reported. `--append` arguments must
precede `--members`, and `--members` may be omitted if nothing new is seated. **A changed
append-only member is grown with `--append <member> <delta-file>`, never passed to `--members`.**
After a close, `gate.py manifest` reports FAIL on changed members because the extracted copies stay
at pre-close state; **verify appends by reading the new bundle directly** — and note the Register
member lives in the **main** bundle. `gate.py bank` refuses to overwrite an existing `.out`;
correcting an instrument after banking needs a **delete-only** call first, and so does rewriting an
instrument before it is banked with `create_file`. Then copy BUILD136, HANDOFF-60 and the READ file
to `/mnt/user-data/outputs` and present them.

## Drive actions for M

- **Upload** to Materials (`1XX_5f3PZB6tjRtiZ2GIgd8Tt7i_4GgkY`): `HANDOFF-59.md` and
  `The_Method_1_6_BUILD135_compendia_papers_audits.md`.
- **Retire** once BUILD135 gates PASS in chat 107: HANDOFF-58 and BUILD134, plus any earlier
  compendia builds still present (BUILD107–BUILD133) **except BUILD124**.
- **Keep BUILD124** for now — it is the only input under which chat 96's `r2-ch14l` and `r2-ch14m`
  reproduce, and §23.9.1's eight exact V values live in `r2-ch14l.out`. Read those values out of
  the **member** rather than re-running the instrument.
- **Keep:** BUILD90 main (unchanged since chat 62), the **Prints & Proofs** folder
  (`1vYctzLppUZ2vFPJDCZ6wvkgSdj3v_f6n`) — the authentication baseline under Ruling 56 and now
  required by the gate itself, since r2-ch15e reads it — the certificates,
  OWED-REGISTER-EXPANSIONS.md, OWED-EXPANSIONS-2.md, covers8.json, factor.py.

## Prompt for chat 107

"Chat 107. READ EVERYTHING BEFORE YOU DO ANYTHING. Live files: BUILD90 main (1,983,081 B, md5
49065309b0c4fe8e055f693aed295cca) and BUILD135 compendia (5,744,660 B, md5
255fac94aff1232dc221750c1eb938d5, 72,779 lines, 460 members). List uploads, outputs and
/home/claude first. Run HANDOFF-59's §0 gate in full and in order — fetch both bundles by title,
bootstrap (decode, md5, extract, expect 462 files), fetch the Prints & Proofs original 'The Method
1.6.md' (738,550 B, md5 49900cf41f818ab789bb90fc596ac977) to /home/claude/PP_The_Method_1_6.md
because r2-ch15e reads it, then gate.py census, run --core, manifest, run r2-ch15f r2-ch15g, cert
107; any FAIL stops the chat with a report. Read RULINGS-R2.md last block first: the chat-95 block
governs and it says a finding is not a question — deviations in the mathematics and in the prose
are recorded and flagged for repair, never put to M, and Prints & Proofs is read before any
question is asked. Do not ask M to rule on a defect. Read DEFERRED.md; chat 106's block is the last
of thirty-five. The standing block's Phase 0–4 Löwdin/three-body plan is executed carried state;
discard it per Ruling 41 — its discard is W-118. Line numbers are MEMBER line numbers and are never
carried between chats, and neither is any count or any heading list. Chapter 27 is CLOSED. Chapter
28 is OPEN: §28–§28.5 (L7332–L7457) are read and closed; §28.6 opens at L7458 and the chapter runs
to L7855. Re-measure by heading scan, resolving each heading to its BODY occurrence — the contents
entries sit at L147–L151. Cut one unit at a section boundary under the 141-line ceiling; §28.6
through §28.7.2 (L7458–L7558, 101 lines) is the natural one, closing before §28.7.3's 75-item
block. Never split a section read across chats. Measure the census rows in range yourself from
DEFECT-CENSUS.tsv keyed on the column named member, not volume, and dispose of those and only
those. A Register line number is not a Register entry number — quote an entry's headline before
citing it, and note that seven Register headings are GROUPED ('### 203, 215, 218, …'), so a bare
'^#{1,4}\\s*N\\s*$' rule misses 32 entries; that is 15f-02, already measured, do not re-derive it.
Then continue Phase R2 under the chat-81 cadence: read the unit in full, census its claims into
computable and prose, then run exactly two instrument batches, r2-ch15h computable and r2-ch15i
prose, importing heading_line, section_span, has_token and enclosing from r2lib — copy nothing,
pass them the LINE LIST and not the member text, and read the six volume MEMBERS, never a BUILDnnn
bundle path. This unit prints counts of withdrawals by class: count the items in each section
against its own heading numeral, and expect the instrument to be wrong before the book is — that
fired twice in chat 106 on §28.2 and §28.4 and the book was right both times. Sweep every phrase on
the TWO-LINE JOIN as well as the raw line ('10 of 16' was reported absent when it is wrapped across
L7416–17). Give every pointer test a claim-locator, test symbols as symbols, match lettered
headings like §E.1.4 explicitly because heading_line cannot see them, and remember a theorem number
is not a section number. Before recording a figure as unreproducible, grep the volume and the
Register for a later or exact statement. Sweep the convention, not just the base — log base,
rounding mode, denominator, and now the UNIT OF THE COUNT: 1,635 reproduces as a count of Register
headings and not of entries, which number 1,660. Never round with Python's round(); use
Decimal.quantize and name the convention. Digit-bound every numeral sweep and sweep both the comma
and comma-free forms. Give every negative claim its own witness and state what a sweep covered.
Where the text prints a sample, measure the population. An assertion is not a proof, a heading is
not a statement, a bound is not a measurement, a citation is not a declaration, a structurally
forced figure is not a finding, and a count of headings is not a count of entries. When an
instrument disagrees with a hand reading, or with a totals line the source states about itself,
suspect the instrument first — that fired five times in chat 106. Close the section read before the
next opens. At close: bank both goldens with gate.py bank, write W-146 ending with a blank line,
build BUILD136 with close.py (reverse must recover 255fac94…), write HANDOFF-60. A changed
append-only member is grown with --append, never --members; correcting a banked golden needs a
delete-only call first, and so does rewriting an instrument with create_file before it is banked.
No corrections, no Register entries, no TASK 1 until the review closes. Handoff at 90–95% of
context or on a closed section read — never earlier, never mid-section. Timeout on every call.
Delete-only calls for pycache, never chained to gate.py bank. Never copy over an existing file."
