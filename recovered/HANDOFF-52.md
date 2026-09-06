# HANDOFF-52 — The Method 1.6 — chat 99 → chat 100

- Written from **chat 99** for **chat 100**. Live files: **BUILD90 main** (unchanged since chat 62)
  and **BUILD128 compendia** (= BUILD127 + W-138 + DEF-99 + six new members). Register **1 to 1792**
  (unchanged — no Register entry since the chat-67 hold). W-138 IS seated; chat 100 seats nothing at
  open and writes W-139 at close.
- **Read RULINGS-R2.md at open, last block first.** The chat-95 block still governs and is still the
  last: **a finding is not a question.** A deviation in the mathematics or in the prose is recorded
  and **flagged for repair**, never put to M. **Prints & Proofs is read before any question is
  asked.** Only a choice no file can settle reaches M. The chat-81 cadence below it is unchanged.
- **Chapter 23 is closed** (chats 95–98). **Chapter 24 is open**: chat 99 read §24–§24.7, main
  L6623–L6740. Chat 100 takes **§24.8–§24.9, L6741–L6816**.
- **Never write an instrument that opens a `BUILDnnn` path** — the name changes every chat and the
  bundle comes to contain the instrument's own banked output. Chat 99's `r2-ch14r` and `r2-ch14s`
  read the six volume **members** by name and reproduced at their own bank.
- **Correcting a banked golden works**: `gate.py bank` refuses to overwrite, so remove the `.out` in a
  **delete-only** call and bank again (chat 98 exercised it; chat 99 did not need it).
- **Line numbering.** Main-volume lines are numbered on the **member** (`The_Method_1_6-2.md`,
  1-based); the bundle numbers each line one higher because of its `<<<FILE:` header. Chat 99
  re-scanned Chapter 24 and found HANDOFF-51's boundaries exact — **which is not a reason to carry
  the next set. Re-scan.**
- **Carried state to discard (Ruling 41):** the standing prompt block's "Phase 0–4"
  Löwdin/three-body plan is executed carried state; do not re-open it or put it to M. Its discard is
  **W-118 (chat 81)**, not W-107. The absorption is W-009 / W-059 / W-063 and Registers 1701–1724.
  Project knowledge holds BUILD12/BUILD53 only — list it, never read those bundles. Retired handoffs
  are gone from Drive; never fetch or cite one. **Never add HANDOFF-NN.md as a member.**
- **Known and pre-existing:** the compendia bundle carries **48 legacy `HANDOFF-NN.md` members**,
  identical in BUILD122–128. They extract into `members/` harmlessly, but a handoff must never be
  written into `members/` or passed to `--members`, or a seated member is silently overwritten.
- **Findings carried to R3:** the READ-chNN.md members (READ-ch14r is chat 99's) and W-101…W-138 in
  WORKING-REGISTER.md; nothing is restated here. **Deferred cross-chapter items:** `DEFERRED.md`
  (**143,252 B · `fadbe4ef` · 28 blocks**, chat 99's is the last) governs; do not re-derive.

## §0 Gate (each step its own tool call under `timeout 280`; any FAIL stops the chat with a report)

1. `ls -la /mnt/user-data/uploads /mnt/user-data/outputs /home/claude`; `recent_chats` confirms the
   latest chat is 99. Read `/mnt/project/CLAUDE.md` (project instruction; never a member).
2. Fetch both bundles by title: `Google Drive:search_files` with
   `title contains 'BUILD128_compendia' or title contains 'BUILD90_main'`, pageSize 5,
   excludeContentSnippets; `Google Drive:download_file_content` on each fileId. Both spill to
   `/mnt/user-data/tool_results/<id>.json`; note the two paths. MEASURED gate cost in chat 99: ≈ 17 %.
3. Bootstrap (the only step outside gate.py, because gate.py is a member):

```
timeout 280 python3 - <<'EOF'
import json, base64, hashlib, re, os
EXP={'main':'49065309b0c4fe8e055f693aed295cca','comp':'f2b9893f2f4483b07e5981ed3159f73e'}
NAME={'main':'/home/claude/The_Method_1_6_BUILD90_main_and_register.md','comp':'/home/claude/The_Method_1_6_BUILD128_compendia_papers_audits.md'}
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
   **5,224,787 B · f2b9893f2f4483b07e5981ed3159f73e · 64,839 lines**; **420 members extracted
   (2 + 418)**.
4. `python3 /home/claude/members/gate.py census` → `OK census: DEFECT-CENSUS.tsv byte-identical`
   (1,556 rows + header, ≈ 15 s).
5. `python3 /home/claude/members/gate.py run --core` → five `OK` (tower 976/1,654/2,535/13,585/
   70,905/199,130; kinds 1565 · 1356 · 499 · 149; minmax; r2-tools-constants; extent "1 to 1792").
6. `python3 /home/claude/members/gate.py manifest` → `MANIFEST OK`; MANIFEST.tsv **28,116 B ·
   ff9b5a7d882bea02b2c0eea41acb019b · 420 lines**; WORKING-REGISTER.md **702,192 B ·
   e0ff730f88b4c15301ef2dc0d755ef10 · 6,143 lines**, ends **W-138**; DEFERRED.md **143,252 B ·
   fadbe4ef · 28 blocks**; RULINGS-R2.md 9,844 B · 10a2ea7e · 82 lines (unchanged); r2lib.py
   21,022 B · 580d2ea2 · 453 lines (unchanged); gate.py 9,377 B · a01ef15a; close.py 6,456 B ·
   98acae67; r2-tools.py 6,529 B · 4702f5f9; tower-2.py c0bce27a; census.py f5a73e2b; kinds.py
   4262f7c5; minmax.py 26da1d78. If two `BUILD*_compendia` files are present after a close, pass
   `--comp <path>` explicitly.
7. `python3 /home/claude/members/gate.py run r2-ch14r r2-ch14s` → two `OK` (chat 99's goldens:
   r2-ch14r.out 18,200 B · 1693fbf1 · 232 lines; r2-ch14s.out 11,750 B · 692a7ecb · 126 lines). Both
   import the lifted r2lib and read members only; an AttributeError means the extraction seated a
   pre-lift r2lib and the chat stops.
8. `python3 /home/claude/members/gate.py cert 100` → writes `/home/claude/GATE-ch100.txt`, verdict
   PASS only if every logged step passed. A FAIL anywhere stops the chat and is reported.

## What chat 99 did (do not repeat)

**§24–§24.7 is closed** — main **L6623–L6740, 118 lines, eight headings**, boundaries re-scanned and
confirmed. **Twenty-five deviations, seventeen verified, seven incidentals, three census rows
closed** (1139 not a defect, 1140 defect, 1141 not a defect — all C9). All of it is in
`READ-ch14r.md` and `CENSUS-CLOSURES-ch14r.tsv`; **do not re-measure any of it.**

**The four findings that carry furthest:**

- **14r-01 — the collection's headline totals are stale, not wrong.** Chapter 24 prints 546 of 789
  interior cells at 69.2 %, 243 failures over 62 channels, and four further counts at L6632. **The
  Register agrees with the chapter** — 673 registers *869 to 930 interior cells*, 797 registers the
  789. **The Spectra Compendium does not**: it states its own totals at spectra-member L900 as **596
  channel rows across 28 elements · 2,269 interior cells**, and its bracket columns sum to **1,577 of
  1,738, 161 failures over 98 channels, 90.7 %**. A sweep of five row-filters, sixteen stage
  thresholds and two ℓ caps returns none of the six printed figures — the sweep is stated in full in
  `r2-ch14r.out`. R3 needs a **recomputation at the current basis**, and must first resolve 14r-19.
- **14r-19 — six channels are tabulated twice in the Spectra Compendium**, 68 interior cells
  double-counted: Ar II L326–L328/L331 repeated at L367–L369/L366, Si I L811/L812/L836 repeated at
  L839/L841/L837, under a second configuration notation, one copy bracket-tested and the other
  `untested`. **A compendium defect found from the main volume**, and it must be fixed before
  anything is recomputed from the table.
- **14r-05 / 14r-06 — hydrogen has no channel row, and the chapter gives it two cell counts.** Swept
  across all six volumes: **zero H I channel rows**; hydrogen appears only as an ionisation energy at
  spectra L1119 (which does corroborate §24.7's R_H). §24.7 says *5 cells*; **§24.9 L6781 says
  *13 of 64 interior cells***. **L6781 is in chat 100's unit — resolve it there.**
- **14r-07 / 14r-08 — §24.3 overstates and under-lists.** *The defect falls monotonically with ℓ* is
  false over He I's nine channels (|δ| rises at four consecutive steps), and L6671 prints **seven
  means for nine**, omitting the two channels — ¹D and ¹H° — that would show it. In the same section
  *members* means levels in one clause and interior cells in the next.

**Thirteen instrument faults, all self-caught and rewritten, none trimmed.** The three to carry are
in DEFERRED's chat-99 block; the shortest form: **compare bases before calling a carried figure
wrong** (596 rows and 477 rows are both right — 477 is the ≥3-level subset, 119 are two-member
channels); **match a printed figure at the source's precision, not at yours**; and **a convention
stated in the source is not a defect**.

## Chat 100's section read — Chapter 24, the collection (second of three)

MEASURED by heading scan on the member in chat 99: **Chapter 24 opens L6623 and runs to L6883; §25
opens L6884.** Headings: 24 (6623), 24.1 (6634), 24.2 (6653), 24.3 (6668), 24.4 (6688), 24.5 (6699),
24.6 (6710), 24.7 (6725), 24.8 (6741), 24.9 (6752), 24.10 (6817), 24.11 (6826), 24.12 (6844), 24.13
(6857). **Re-scan before reading a line.**

- **Chat 100: L6741–L6816 — §24.8 and §24.9**, 76 lines, two headings. §24.9 alone is 65 lines and is
  the chapter's longest section. Well inside the 141-line ceiling.
- Chat 101: §24.10–§24.13, L6817–L6883 (67 lines), closing the chapter.

**What this unit owes, beyond the read itself:**

- **L6781 settles 14r-06.** *Computed on H I, which is 38 % plain: only 13 of 64 interior cells —
  20 % — are independent tests.* 13/64 = 20.3 %, so the percentage is sound and the **5 vs 64**
  conflict with L6729 is the live question. There is **no H I channel row in the Spectra
  Compendium**, so neither figure can be checked against it — say so rather than leaving it open.
- **§24.8 is titled *On independence, and the most conservative reading*** and L6787 already names
  *He I's nine* and *H I's nd series*; independence claims interact with **Register 1625**
  (*independence is a property of triples, not of cells*), which chat 99 surfaced but did not read.
- **Every count and every ν attributed to a named species must be measured against that species'
  compendium rows** (14p-19, widened by 14r-01). The row format is
  `| species | series | n | levels | interior | bracket | n* range | δ | σ(δ) | fits | limit cm⁻¹ |`;
  **interior = levels − 2** on all 477 rows with three or more levels; the 119 two-member rows print
  interior 1 by stated convention; `bracket` reads `m/k`, `no-triple` or `untested`; the column headed
  **fits** actually holds the ionisation stage. Section II is spectra-member L293–L935 and its own
  totals line is L900.

Instruments: **r2-ch14t** (computable) and **r2-ch14u** (prose). Import `heading_line`,
`section_span`, `has_token` and `enclosing` from r2lib by path; **copy nothing**; **read members,
never a bundle**. Six functions are still owed to r2lib and DEFERRED lists them; note that
`heading_line` requires a trailing space after the number, so the Register's bare `### 96` headings
return None — locate Register entries with an explicit `^#{1,4}\s*N\s*$` match (chat 99's P2 does
this and works).

**Standing method, unchanged and all of it earned:** exact-token heading resolver, never prefix;
never span a section by heading rank; **r2lib's resolvers take the LINE LIST, not the member text**.
Grep lowercase `register NNN` by hand. Check every printed pair count against C(N, 2). Resolve every
pointer to the claim and not the heading, and before recording any pointer as unresolved **read the
target section and test for the claim as that section words it**, case-exact and word-bounded — and
if it fails there, grep the whole volume before recording it. Give every negative claim its own
witness. **State what a sweep covered before recording a negative from it.** Check the arithmetic of
every ratio and percentage; **never round with `round()`** — use `Decimal.quantize` and name the
convention. A formula numerator is not a value; a citation is not a declaration; a heading is not a
statement; a bound is not a measurement; a boundary case is not a violation; **a number beside a
species is not that species' ceiling** — read the header. Where the text prints a sample, measure the
population. Grep the Register for a later entry naming the section before recording any figure as
unreproducible — chat 99's 14r-01 turned on exactly this. **When an instrument disagrees with a hand
reading already taken from the file, the instrument is wrong until proved otherwise** — chats 94–99
hit that twice, four times, three, twice, twice and twice.

## The repair docket

Carried forward until R3 executes it. **None of these goes to M.** Chat 99's additions are in
DEFERRED's chat-99 block in full; the docket below is the standing list.

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
5. **The Ruling 45 class, now six members** — L6453 *An earlier draft claimed…*, the Figure 23.3
   caption at L6483–L6484, and chat 99's **L6628** and **L6632** (*An earlier version of this chapter
   read…*, *…not in hand*, *…which are owed*). Captions state facts only.
6. **The Ruling 46 class, new and sweepable in one pass** (14r-18) — **Build 9** at main L6693 and
   L7659, plus five Register sites (L20, L31, L65, L68 and one further). Seven build references
   visible to readers.
7. **§23.8.3's affine-invariance reason** (chat 96's 14l-16) — the docket's only *reason* item. R3
   must decide which invariance the chapter claims before rewriting, and check §29.2 L7881, §29.7
   L8052 and App D.4.1 L10377 for the same reasoning.
8. **The §25.6 pointer with no target** (chat 96's 14m-01) — author the explanation or drop the
   clause; the clause is load-bearing for the novelty claim beside it.
9. **The pointer-off-by-one class, now ten members and never yet swept as a class** — 14n-A1, 14n-A2,
   14n-A7, chat 95's 14k-01, chat 96's 14m-01, chat 98's 14q-02/03/04, and chat 99's **14r-21**
   (L6686 → §24.7 for a Ritz distinction it does not carry) and **14r-22** (L6666 → §24.12 for an
   exclusion it does not state). R3 sweeps **every §-pointer in the six volumes against the claim
   rather than the heading**; `enclosing` makes the test cheap.
10. **The unprinted-input class, now fourteen members** — §22.1.2's δ = 0.35; §22.4.1's δ₂ = 0.06;
    L6060's 446×, L6068's 1,577, L6093's 3.47 %, L6104's *factor of 17*; §23.1 L6189's *agreement
    under 1 %*; §23.9.3's two columns; §23.10.3's displacement row; §23.12's window; the +0.86 Hill
    slope; the Kirkwood floor; and chat 99's **hydrogen row** (5 cells and a 0.006 median with no H I
    channel row anywhere — *inputs absent*) and **Li II's s→f selection** (*conventions unstated*).
    R3 splits the class into *conventions unstated* and *inputs absent*.
11. **The 32/11 scope docket** (14j-01), with six measured main-volume sites — L6193, L6213, L6233,
    L6237, L6381, L10245 — plus 2.909 at four. L6381 claims the floor as an original result and must
    be repaired **after** the scope decision, not with it.
12. **The truncation-printed-as-equality class** (14l-02, 14l-03, 14n-A10) — sweep every display
    equation whose own table disagrees with it, and every site printing 4ν/3.
13. **The two unsourced counts of L6517** (14n-A6, 14n-A7) — *619 refusals* and *§25.5's 1,061
    order-1 bounds*. Chat 99 confirmed **§32.5 does carry the 1,061**, so the pointer resolves; what
    is still owed is the recomputation at matched order.
14. **The main-volume/compendium contradiction class** (14p-19, widened by 14r-01, 14r-02, 14r-03) —
    every figure the main volume attributes to a named channel or to the collection, against the
    compendium's current rows and totals. **Resolve K I *n*d 45.7 first** (chat 98) and **Ne I 16/131
    and K I 4/105** (chat 99, matching no species in the table); they decide whether the class is a
    table defect or a short compendium. **14r-19's double-tabulation must be settled before any
    recount.**
15. **The Nesterov name-form sweep** (14m-07) — five forms in five places, one substantive (L8052
    credits Nesterov alone for a result §23.8.1 credits to both). Chat 99 adds **"KI" without its
    space** at L6657 and L6716, **"neon II"** spelled out at L6704, and **the Edlén Handbuch chapter
    dated 1960 at two sites and 1964 at five** (14r-20), which also makes L6683's *sixty-five years
    old* wrong under both.
16. **The single-witness class** — five of twenty-one distinctive figures in chat 99's 118 lines, six
    of twelve in chat 98's 74, fourteen in chat 97's 115, seventeen in chat 96's 131, thirteen in
    chat 95's 125. R4 should state which figures are unverifiable rather than leaving them looking
    checked, and distinguish *unverifiable* from *uncorroborated*.
17. **Heading sentences finishing in the body** (14q-06) — **now three, not four**: L4407
    (+ "routes"), L6582 (+ "one"), L8659 (+ "disanalogy"). **L6634 closes** — chat 99 confirmed it is
    a table header, not a sentence continuation.

## Close (chat 100)

`gate.py bank r2-ch14t r2-ch14u`; delete pycache in its own delete-only call; write `W-139.md`
(begins `### W-`, **ends with a blank line** — close.py asserts this); append a DEFERRED block as
`DEF-100.md`; then

```
timeout 280 python3 members/close.py --old The_Method_1_6_BUILD128_compendia_papers_audits.md \
  --new The_Method_1_6_BUILD129_compendia_papers_audits.md --w W-139.md \
  --main The_Method_1_6_BUILD90_main_and_register.md --append DEFERRED.md DEF-100.md \
  --members members/READ-ch14t.md members/CENSUS-CLOSURES-ch14t.tsv members/r2-ch14t.py \
  members/r2-ch14t.out members/r2-ch14u.py members/r2-ch14u.out
```

It must print **reverse recovers md5 f2b9893f2f4483b07e5981ed3159f73e == old: True** before writing;
if it does not, nothing is written and the failure is reported. `--append` arguments must precede
`--members`, and `--members` may be omitted entirely if nothing new is seated. **A changed
append-only member is grown with `--append <member> <delta-file>`, never passed to `--members`** —
close.py refuses a name collision, and a member needing *replacement* rather than growth has no
mechanism at all. After a close, `gate.py manifest` reports FAIL on changed members because the
extracted copies stay at pre-close state; **verify appends by reading the new bundle directly** —
and note the Register member lives in the **main** bundle, not the compendia bundle. `gate.py bank`
refuses to overwrite an existing `.out`; correcting an instrument after banking needs a
**delete-only** call to remove the golden, then bank again. Then copy BUILD129, HANDOFF-53 and the
READ file to `/mnt/user-data/outputs` and present them.

## Drive actions for M

- **Upload** to Materials (`1XX_5f3PZB6tjRtiZ2GIgd8Tt7i_4GgkY`): `HANDOFF-52.md` and
  `The_Method_1_6_BUILD128_compendia_papers_audits.md`.
- **Retire** once BUILD128 gates PASS in chat 100: HANDOFF-51 and BUILD127, plus any earlier
  compendia builds still present (BUILD107–BUILD126) **except BUILD124**.
- **Keep BUILD124** for now — it is the only input under which chat 96's `r2-ch14l` and `r2-ch14m`
  reproduce, and §23.9.1's eight exact V values live in `r2-ch14l.out`. Read those values out of the
  **member** rather than re-running the instrument; that is the pattern R3 should adopt before
  BUILD124 is retired.
- **Keep:** BUILD90 main (unchanged since chat 62), the **Prints & Proofs** folder
  (`1vYctzLppUZ2vFPJDCZ6wvkgSdj3v_f6n`) — the authentication baseline under Ruling 56 — the
  certificates, OWED-REGISTER-EXPANSIONS.md, OWED-EXPANSIONS-2.md, covers8.json, factor.py.

## Prompt for chat 100

"Chat 100. READ EVERYTHING BEFORE YOU DO ANYTHING. Live files: BUILD90 main (1,983,081 B, md5
49065309b0c4fe8e055f693aed295cca) and BUILD128 compendia (5,224,787 B, md5
f2b9893f2f4483b07e5981ed3159f73e, 64,839 lines, 418 members). List uploads, outputs and /home/claude
first. Run HANDOFF-52's §0 gate in full and in order — fetch both bundles by title, bootstrap
(decode, md5, extract, expect 420 files), then gate.py census, run --core, manifest, run r2-ch14r
r2-ch14s, cert 100; any FAIL stops the chat with a report. Read RULINGS-R2.md last block first: the
chat-95 block governs and it says a finding is not a question — deviations in the mathematics and in
the prose are recorded and flagged for repair, never put to M, and Prints & Proofs is read before any
question is asked. Do not ask M to rule on a defect. Read DEFERRED.md; chat 99's block is the last of
twenty-eight. The standing block's Phase 0–4 Löwdin/three-body plan is executed carried state;
discard it per Ruling 41 — its discard is W-118, not W-107. Line numbers are MEMBER line numbers and
are never carried between chats, and neither is any count: re-scan every heading on
The_Method_1_6-2.md before reading a line. Chapter 23 closed in chat 98; chat 99 read §24–§24.7. Then
continue Phase R2 under the chat-81 cadence: take §24.8–§24.9, main L6741–L6816, 76 lines, two
headings, and decide the cut before reading. Read it all, census its claims into computable and
prose, then run exactly two instrument batches, r2-ch14t computable and r2-ch14u prose, importing
heading_line, section_span, has_token and enclosing from r2lib — copy nothing, pass them the LINE
LIST and not the member text, and read the six volume MEMBERS, never a BUILDnnn bundle path. Chat 99
measured that the Spectra Compendium's channel table is 596 rows across 28 elements carrying 2,269
interior cells — it states this itself at spectra-member L900 — that interior = levels − 2 on all 477
rows with three or more levels, that the 119 two-member rows print interior 1 by stated convention,
that the column headed 'fits' holds the ionisation stage, and that six channels are tabulated twice
for 68 double-counted cells. Chapter 24's own totals (546/789, 930, 869, 1,105, 1,442) agree with
Registers 673 and 797 and match nothing in the compendium under any of nineteen bases swept, so the
class is staleness rather than error — measure every count this unit attributes to the collection or
to a named species against the compendium's current rows and say which basis you used. Resolve
L6781's '13 of 64 interior cells' against §24.7's 'H I gives 5 cells'; there is no H I channel row
anywhere in the six volumes. Read Register 1625 on independence before judging §24.8. Where the text
prints a sample, measure the population. Compare bases before calling a carried figure wrong. Match a
printed figure at the source's precision, not at yours. A convention stated in the source is not a
defect. Use the exact-token heading resolver, never prefix matching, and never span a section by
heading rank. Grep lowercase 'register NNN' by hand. Resolve every pointer to the claim and not the
heading, and if it fails at the named target grep the whole volume before recording it. Give every
negative claim its own witness, and state what a sweep covered before recording a negative from it. A
number beside a species is not that species' ceiling — read the header. ν is not n. Never round with
Python's round() — use Decimal.quantize and name the convention. A heading is not a statement, a
bound is not a measurement, a boundary case is not a violation. Re-read every verdict against the
numbers printed above it AND below it. When an instrument disagrees with a hand reading, suspect the
instrument first. Close the section read before the next opens. At close: bank both goldens with
gate.py bank, write W-139 ending with a blank line, build BUILD129 with close.py (reverse must
recover f2b9893f…), write HANDOFF-53. A changed append-only member is grown with --append, never
--members; correcting a banked golden needs a delete-only call first. No corrections, no Register
entries, no TASK 1 until the review closes. Handoff at 90–95 % of context or on a closed section read
— never earlier, never mid-section. Timeout on every call. Delete-only calls for pycache, never
chained to gate.py bank. Never copy over an existing file."
