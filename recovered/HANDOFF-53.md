# HANDOFF-53 — The Method 1.6 — chat 100 → chat 101

- Written from **chat 100** for **chat 101**. Live files: **BUILD90 main** (unchanged since chat 62)
  and **BUILD129 compendia** (= BUILD128 + W-139 + DEF-100 + six new members). Register **1 to 1792**
  (unchanged — no Register entry since the chat-67 hold). W-139 IS seated; chat 101 seats nothing at
  open and writes W-140 at close.
- **Read RULINGS-R2.md at open, last block first.** The chat-95 block still governs and is still the
  last: **a finding is not a question.** A deviation in the mathematics or in the prose is recorded
  and **flagged for repair**, never put to M. **Prints & Proofs is read before any question is
  asked.** Only a choice no file can settle reaches M. The chat-81 cadence below it is unchanged.
- **Chapter 23 is closed** (chats 95–98). **Chapter 24 is nearly closed**: chat 99 read §24–§24.7
  (L6623–L6740), chat 100 read §24.8–§24.9 (L6741–L6816). Chat 101 takes **§24.10–§24.13,
  L6817–L6883**, which closes the chapter.
- **Never write an instrument that opens a `BUILDnnn` path** — the name changes every chat and the
  bundle comes to contain the instrument's own banked output. Chat 100's `r2-ch14t` and `r2-ch14u`
  read the six volume **members** by name and reproduced at their own bank.
- **A Register line number is not a Register entry number.** HANDOFF-52 sent chat 100 to *Register
  1625* for *independence is a property of triples*; Register 1625 is the 4D-in-1D refutation and
  carries *independence* zero times. The entry is **Register 437** (Register-member L1623) — and
  *13 of 64* sits at Register-member **line 1625**, inside 437's body. §24.9 L6792's own citation was
  correct throughout. **This handoff therefore prints an entry's headline beside every number it
  cites**, and chat 101 should do the same.
- **Line numbering.** Main-volume lines are numbered on the **member** (`The_Method_1_6-2.md`,
  1-based); the bundle numbers each line one higher because of its `<<<FILE:` header. Chat 100
  re-scanned Chapter 24 and found HANDOFF-52's boundaries exact — **which is not a reason to carry
  the next set. Re-scan.**
- **Carried state to discard (Ruling 41):** the standing prompt block's "Phase 0–4"
  Löwdin/three-body plan is executed carried state; do not re-open it or put it to M. Its discard is
  **W-118 (chat 81)**, not W-107. The absorption is W-009 / W-059 / W-063 and Registers 1701–1724.
  Project knowledge holds BUILD12/BUILD53 only — list it, never read those bundles. Retired handoffs
  are gone from Drive; never fetch or cite one. **Never add HANDOFF-NN.md as a member.**
- **Known and pre-existing:** the compendia bundle carries **48 legacy `HANDOFF-NN.md` members**,
  identical in BUILD122–129. They extract into `members/` harmlessly, but a handoff must never be
  written into `members/` or passed to `--members`, or a seated member is silently overwritten.
- **Findings carried to R3:** the READ-chNN.md members (READ-ch14t is chat 100's) and W-101…W-139 in
  WORKING-REGISTER.md; nothing is restated here. **Deferred cross-chapter items:** `DEFERRED.md`
  (**150,151 B · 29 blocks**, chat 100's is the last) governs; do not re-derive.

## §0 Gate (each step its own tool call under `timeout 280`; any FAIL stops the chat with a report)

1. `ls -la /mnt/user-data/uploads /mnt/user-data/outputs /home/claude`; `recent_chats` confirms the
   latest chat is 100. Read `/mnt/project/CLAUDE.md` (project instruction; never a member).
2. Fetch both bundles by title: `Google Drive:search_files` with
   `title contains 'BUILD129_compendia' or title contains 'BUILD90_main'`, pageSize 5,
   excludeContentSnippets; `Google Drive:download_file_content` on each fileId. Both spill to
   `/mnt/user-data/tool_results/<id>.json`; note the two paths. MEASURED gate cost in chat 100: ≈ 17 %.
3. Bootstrap (the only step outside gate.py, because gate.py is a member):

```
timeout 280 python3 - <<'EOF'
import json, base64, hashlib, re, os
EXP={'main':'49065309b0c4fe8e055f693aed295cca','comp':'b5fd5d3a6dd81a3a2ea4f8077784ad76'}
NAME={'main':'/home/claude/The_Method_1_6_BUILD90_main_and_register.md','comp':'/home/claude/The_Method_1_6_BUILD129_compendia_papers_audits.md'}
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
   **5,300,989 B · b5fd5d3a6dd81a3a2ea4f8077784ad76 · 66,046 lines**; **426 members extracted
   (2 + 424)**.
4. `python3 /home/claude/members/gate.py census` → `OK census: DEFECT-CENSUS.tsv byte-identical`
   (1,556 rows + header, ≈ 15 s).
5. `python3 /home/claude/members/gate.py run --core` → five `OK` (tower 976/1,654/2,535/13,585/
   70,905/199,130; kinds 1565 · 1356 · 499 · 149; minmax; r2-tools-constants; extent "1 to 1792").
6. `python3 /home/claude/members/gate.py manifest` → `MANIFEST OK`; MANIFEST.tsv **28,519 B ·
   e9dd6201719046507f1fe091de9c98d8 · 426 lines**; WORKING-REGISTER.md **709,869 B ·
   1b1285b5ba7ff66b21a6adefacdf55c5 · 6,239 lines**, ends **W-139**; DEFERRED.md **150,151 B ·
   29 blocks**; RULINGS-R2.md 9,844 B · 10a2ea7e · 82 lines (unchanged); r2lib.py 21,022 B ·
   580d2ea2 · 453 lines (unchanged); gate.py 9,377 B · a01ef15a; close.py 6,456 B · 98acae67;
   r2-tools.py 6,529 B · 4702f5f9; tower-2.py c0bce27a; census.py f5a73e2b; kinds.py 4262f7c5;
   minmax.py 26da1d78. If two `BUILD*_compendia` files are present after a close, pass
   `--comp <path>` explicitly.
7. `python3 /home/claude/members/gate.py run r2-ch14t r2-ch14u` → two `OK` (chat 100's goldens:
   r2-ch14t.out 6,683 B · 36d7afbc · 117 lines; r2-ch14u.out 12,726 B · 3eaa668d · 179 lines). Both
   import the lifted r2lib and read members only; an AttributeError means the extraction seated a
   pre-lift r2lib and the chat stops.
8. `python3 /home/claude/members/gate.py cert 101` → writes `/home/claude/GATE-ch101.txt`, verdict
   PASS only if every logged step passed. A FAIL anywhere stops the chat and is reported.

## What chat 100 did (do not repeat)

**§24.8–§24.9 is closed** — main **L6741–L6816, 76 lines, two headings**, boundaries re-scanned and
confirmed. **Eleven deviations, twelve verified, seven incidentals, two census rows closed** (1142
defect, 1143 not a defect — both C9 on *never*). All of it is in `READ-ch14t.md` and
`CENSUS-CLOSURES-ch14t.tsv`; **do not re-measure any of it.**

**The four findings that carry furthest:**

- **14t-01 — the chapter retires its own headline figures in print, and then runs two sections on
  them.** L6632: *An earlier version of this chapter read "1,442 interior cells across 35 atomic
  systems, the bracket holds in every one." That figure matches neither Appendix B's totals line
  (1,105) nor its table (869) nor the present tested count (930).* MEASURED across Chapter 24:
  **1,442 appears 13 times — L6632 and twelve times in §24.8–§24.9**; *thirty-five* appears twice,
  at L6632 and **L6792**; the retired no-failure claim is restated at L6746 and L6750; and **1,105,
  869 and 930 appear once each, at L6632 alone**. The current basis is named once; the retired basis
  carries the argument. **30 main-volume sites for 1,442.** This subsumes chat 99's 14r-01 — the
  class is not undetected staleness but staleness **retired in the same chapter and left
  load-bearing**. L6628 is a second retirement quotation in the same chapter; sweep them as a class.
- **14t-03 — unretired text surviving its own correction, three times in one 65-line section.**
  L6760–L6762 withdraws the reading of `[ ]` as ab initio and L6767 concludes He I's 189 cells are
  *not independent tests*; **L6807–L6809 and L6815, the section's closing paragraph**, still call
  them *ab initio QED calculations* and *genuine tests… sharper than any measurement here*.
  **Register 436 — *He I HAS NO OBSERVED LEVEL VALUES IN THE ASD* — sides with L6767** and names the
  `[ ]`-as-ab-initio reading as the error. Also L6791 *supersedes "an unknown proper subset"* while
  L6811 prints it, and L6801 *never counted the three* against L6781's count.
- **14t-B3 — 14r-06 is settled, against §24.7.** **Register 437 — *INDEPENDENCE IS A PROPERTY OF
  TRIPLES, NOT OF CELLS*** — carries H I at *38 % plain, 13 of 64 interior cells independent*, and
  the nd series at *six plain levels of ten and not one clean triple*, corroborating L6781 in full.
  **§24.7's *H I gives 5 cells* at L6729 stands alone.** R3 repairs L6729, not L6781. There is still
  no H I channel row in the six volumes.
- **14t-02 / 14t-07 / 14t-08 — three more main-volume/compendium contradictions.** *None produced a
  failure* (L6750) against **98 failing channels, 161 failing cells, 1,577 of 1,738 at 90.7 %**, and
  against the chapter's own *243 failures across 62 channels* at L6626. *Ne I's sixteen … 131*
  against Ne I 7/39 and Ne II 37/69 — the same pair chat 99 found in §24.2. *The largest single
  block* against **Si I's 290**. He I's **nine channels / 189 cells is exact**, the only one of the
  four that reproduces.

**Two instrument faults, both self-caught and rewritten, neither trimmed.** The one to carry: an
unbounded channel-table regex silently absorbed Section V's capture-groups table and returned 600
rows / 2,317 interior / 32 elements against the compendium's own **596 / 2,269 / 28**. The instrument
was suspected first, as the standing rule requires. **The compendium states its own totals at spectra
L900 — check any parse against that line before trusting one figure from it.**

## Chat 101's section read — Chapter 24, the collection (third of three, closing)

MEASURED by heading scan on the member in chat 100: **Chapter 24 opens L6623 and runs to L6883; §25
opens L6884.** Headings: 24 (6623), 24.1 (6634), 24.2 (6653), 24.3 (6668), 24.4 (6688), 24.5 (6699),
24.6 (6710), 24.7 (6725), 24.8 (6741), 24.9 (6752), 24.10 (6817), 24.11 (6826), 24.12 (6844), 24.13
(6857). **Re-scan before reading a line.**

- **Chat 101: L6817–L6883 — §24.10 through §24.13**, 67 lines, four headings, closing the chapter.
  Well inside the 141-line ceiling, and the chapter's last unit.
- Chat 102 opens Chapter 25 at L6884. §25 has fourteen headings through §25.6.6 (L7093) and will need
  at least two reads; decide the cut from a fresh heading scan, not from this line.

**What this unit owes, beyond the read itself:**

- **§24.11 is *Four ways a species declines* (L6826–L6843, 18 lines)** and L6837 already names
  *Cu II's is a structural exclusion*, with level values 107,942–111,124 cm⁻¹. **L6809 pairs
  §24.11's decline modes with "§18's exclusions", and §18 carries no exclusions at all** (14t-06) —
  the target is §25.2. Chat 101 should check whether §24.11 itself names four modes and whether the
  front matter's L62 (*a structural exclusion covering five isoelectronic sequences from four decline
  modes*) agrees with it.
- **§24.12 is *The census, computed rather than searched* (L6844–L6856)** — chat 99 recorded
  **14r-22**, that L6666 points at §24.12 for a structural exclusion it does not state (*exclude*
  appears zero times there against one site in the whole main volume). Resolve it in this unit.
- **Every retired figure must be swept forward.** 1,442, *thirty-five*, and the no-failure claim are
  retired at L6632; measure whether §24.10–§24.13 carry any of them, and whether the chapter's
  closing sections use the current basis (1,105 / 869 / 930) or the retired one. That decides whether
  14t-01 is a two-section defect or a whole-chapter one.
- **Every count and every ν attributed to a named species must be measured against that species'
  compendium rows** (14p-19, widened by 14r-01 and 14t-02/07/08). The row format is
  `| species | series | n | levels | interior | bracket | n* range | δ | σ(δ) | fits | limit cm⁻¹ |`;
  **interior = levels − 2** on all 477 rows with three or more levels; the 119 two-member rows print
  interior 1 by stated convention; `bracket` reads `m/k`, `no-triple` or `untested`; the column headed
  **fits** actually holds the ionisation stage. Section II is spectra-member **L293–L934** and its own
  totals line is **L900**: *596 channel rows across 28 elements · 2,269 interior cells parsed.*
  The table carries **70 species across 28 elements**; largest blocks by interior cells are Si I 290,
  He I 189, Al I 94, Na I 80, Ne II 69, Li II 62.

Instruments: **r2-ch14v** (computable) and **r2-ch14w** (prose). Import `heading_line`,
`section_span`, `has_token` and `enclosing` from r2lib by path; **copy nothing**; **read members,
never a bundle**. Six functions are still owed to r2lib and DEFERRED lists them; note that
`heading_line` requires a trailing space after the number, so the Register's bare `### 96` headings
return None — locate Register entries with an explicit `^#{1,4}\s*N\s*$` match (chat 99's P2 and chat
100's P9 both do this and work).

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
population. **Compare bases before calling a carried figure wrong**, and **match a printed figure at
the source's precision, not at yours**. A convention stated in the source is not a defect. Grep the
Register for a later entry naming the section before recording any figure as unreproducible.
**When an instrument disagrees with a hand reading already taken from the file, or with a totals line
the source states about itself, the instrument is wrong until proved otherwise** — chats 94–100 hit
that twice, four times, three, twice, twice, twice and twice.

## The repair docket

Carried forward until R3 executes it. **None of these goes to M.** Chat 100's additions are in
DEFERRED's chat-100 block in full; the docket below is the standing list.

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
5. **The Ruling 45 class, now thirteen members and the docket's fastest-growing** — L6453, the Figure
   23.3 caption at L6483–L6484, chat 99's L6628 and L6632, and chat 100's **seven in 76 lines**:
   L6748, L6756, L6791, L6801, L6803, L6810–L6812 and L6813. **L6812 — *it should be written that way
   wherever the figure carries weight* — is an instruction to the author printed in a reader-facing
   volume**, and L6813 prints the Q index's cost grading to the reader. Captions state facts only.
6. **The Ruling 46 class, sweepable in one pass** (14r-18) — **Build 9** at main L6693 and L7659,
   plus five Register sites (L20, L31, L65, L68 and one further). Seven build references visible to
   readers. Run 5 and 6 together.
7. **§23.8.3's affine-invariance reason** (chat 96's 14l-16) — the docket's only *reason* item. R3
   must decide which invariance the chapter claims before rewriting, and check §29.2 L7881, §29.7
   L8052 and App D.4.1 L10377 for the same reasoning.
8. **The §25.6 pointer with no target** (chat 96's 14m-01) — author the explanation or drop the
   clause; the clause is load-bearing for the novelty claim beside it.
9. **The pointer-off-by-one class, now eleven members and never yet swept as a class** — 14n-A1,
   14n-A2, 14n-A7, chat 95's 14k-01, chat 96's 14m-01, chat 98's 14q-02/03/04, chat 99's 14r-21 and
   14r-22, and chat 100's **14t-06** (L6809 → *§18's exclusions*; §18 carries the token zero times in
   459 lines; the target is §25.2). R3 sweeps **every §-pointer in the six volumes against the claim
   rather than the heading**; `enclosing` makes the test cheap.
10. **The unprinted-input class, now sixteen members** — §22.1.2's δ = 0.35; §22.4.1's δ₂ = 0.06;
    L6060's 446×, L6068's 1,577, L6093's 3.47 %, L6104's *factor of 17*; §23.1 L6189's *agreement
    under 1 %*; §23.9.3's two columns; §23.10.3's displacement row; §23.12's window; the +0.86 Hill
    slope; the Kirkwood floor; chat 99's hydrogen row and Li II's s→f selection; and chat 100's
    **per-level provenance** (*inputs absent* — no volume records it: spectra provenance rows 0,
    lines carrying both *observed* and *derived* are main 4 / register 5 / math 1 / physics 1 /
    index 0 / spectra 0, so L6753's Al I comparison and the three-way split of the 1,442 cannot be
    recomputed at all) and **the survival table's 0.125 printed 0.12** (*conventions unstated*).
    R3 splits the class into *conventions unstated* and *inputs absent*. **Q item P (L10958, one
    claim / retrievable / hours) already records the provenance split as owed** — repair them together.
11. **The 32/11 scope docket** (14j-01), with six measured main-volume sites — L6193, L6213, L6233,
    L6237, L6381, L10245 — plus 2.909 at four. L6381 claims the floor as an original result and must
    be repaired **after** the scope decision, not with it.
12. **The truncation-printed-as-equality class** (14l-02, 14l-03, 14n-A10) — sweep every display
    equation whose own table disagrees with it, and every site printing 4ν/3.
13. **The two unsourced counts of L6517** (14n-A6, 14n-A7) — *619 refusals* and *§25.5's 1,061
    order-1 bounds*. Chat 99 confirmed **§32.5 does carry the 1,061**, so the pointer resolves; what
    is still owed is the recomputation at matched order.
14. **The main-volume/compendium contradiction class** (14p-19, widened by 14r-01/02/03 and chat
    100's 14t-02/07/08) — every figure the main volume attributes to a named channel or to the
    collection, against the compendium's current rows and totals. **Resolve K I *n*d 45.7 first**
    (chat 98) and **Ne I 16/131** (chat 99, now witnessed twice — §24.2 and L6746) and **K I 4/105**;
    they decide whether the class is a table defect or a short compendium. **14r-19's
    double-tabulation (six channels, 68 interior cells) must be settled before any recount.**
15. **The retired-basis class — new in chat 100, and it reframes 14** (14t-01). A chapter that quotes
    its own earlier wording is issuing a retirement notice; the retired figures must then be grepped
    forward. Chapter 24 does this twice (L6628, L6632) and leaves **twelve 1,442 sites and one
    *thirty-five*** standing in §24.8–§24.9, with the current-basis figures appearing once each. R3
    sweeps every *An earlier version…* / *supersedes* / *and it does not* / *sharper than it was
    written* site in the six volumes and greps the retired wording forward from each. **Related and
    distinct: unretired text surviving its own correction** (14t-03/04/05) — He I's provenance,
    *an unknown proper subset*, and *never counted the three*, all inside §24.9.
16. **The Nesterov name-form sweep** (14m-07) — five forms in five places, one substantive (L8052
    credits Nesterov alone for a result §23.8.1 credits to both), plus chat 99's *"KI"* without its
    space at L6657 and L6716, *"neon II"* spelled out at L6704, and the Edlén Handbuch chapter dated
    1960 at two sites and 1964 at five (14r-20), which also makes L6683's *sixty-five years old*
    wrong under both. Chat 100 measured **no name-form defect** in its unit: NIST, ASD, Drake,
    Kandula, Ritz and QED each take one form.
17. **The single-witness class** — chat 100 adds five of the unit's distinctive figures.
    R4 should state which figures are unverifiable rather than leaving them looking checked, and
    distinguish *unverifiable* from *uncorroborated*.
18. **Heading sentences finishing in the body** (14q-06) — **three**: L4407 (+ "routes"), L6582
    (+ "one"), L8659 (+ "disanalogy"). Chat 100 confirmed neither of its two headings joins them.

## Close (chat 101)

`gate.py bank r2-ch14v r2-ch14w`; delete pycache in its own delete-only call; write `W-140.md`
(begins `### W-`, **ends with a blank line** — close.py asserts this); append a DEFERRED block as
`DEF-101.md`; then

```
timeout 280 python3 members/close.py --old The_Method_1_6_BUILD129_compendia_papers_audits.md \
  --new The_Method_1_6_BUILD130_compendia_papers_audits.md --w W-140.md \
  --main The_Method_1_6_BUILD90_main_and_register.md --append DEFERRED.md DEF-101.md \
  --members members/READ-ch14v.md members/CENSUS-CLOSURES-ch14v.tsv members/r2-ch14v.py \
  members/r2-ch14v.out members/r2-ch14w.py members/r2-ch14w.out
```

It must print **reverse recovers md5 b5fd5d3a6dd81a3a2ea4f8077784ad76 == old: True** before writing;
if it does not, nothing is written and the failure is reported. `--append` arguments must precede
`--members`, and `--members` may be omitted entirely if nothing new is seated. **A changed
append-only member is grown with `--append <member> <delta-file>`, never passed to `--members`** —
close.py refuses a name collision, and a member needing *replacement* rather than growth has no
mechanism at all. After a close, `gate.py manifest` reports FAIL on changed members because the
extracted copies stay at pre-close state; **verify appends by reading the new bundle directly** —
and note the Register member lives in the **main** bundle, not the compendia bundle. `gate.py bank`
refuses to overwrite an existing `.out`; correcting an instrument after banking needs a
**delete-only** call to remove the golden, then bank again. Then copy BUILD130, HANDOFF-54 and the
READ file to `/mnt/user-data/outputs` and present them.

## Drive actions for M

- **Upload** to Materials (`1XX_5f3PZB6tjRtiZ2GIgd8Tt7i_4GgkY`): `HANDOFF-53.md` and
  `The_Method_1_6_BUILD129_compendia_papers_audits.md`.
- **Retire** once BUILD129 gates PASS in chat 101: HANDOFF-52 and BUILD128, plus any earlier
  compendia builds still present (BUILD107–BUILD127) **except BUILD124**.
- **Keep BUILD124** for now — it is the only input under which chat 96's `r2-ch14l` and `r2-ch14m`
  reproduce, and §23.9.1's eight exact V values live in `r2-ch14l.out`. Read those values out of the
  **member** rather than re-running the instrument; that is the pattern R3 should adopt before
  BUILD124 is retired.
- **Keep:** BUILD90 main (unchanged since chat 62), the **Prints & Proofs** folder
  (`1vYctzLppUZ2vFPJDCZ6wvkgSdj3v_f6n`) — the authentication baseline under Ruling 56 — the
  certificates, OWED-REGISTER-EXPANSIONS.md, OWED-EXPANSIONS-2.md, covers8.json, factor.py.

## Prompt for chat 101

"Chat 101. READ EVERYTHING BEFORE YOU DO ANYTHING. Live files: BUILD90 main (1,983,081 B, md5
49065309b0c4fe8e055f693aed295cca) and BUILD129 compendia (5,300,989 B, md5
b5fd5d3a6dd81a3a2ea4f8077784ad76, 66,046 lines, 424 members). List uploads, outputs and /home/claude
first. Run HANDOFF-53's §0 gate in full and in order — fetch both bundles by title, bootstrap
(decode, md5, extract, expect 426 files), then gate.py census, run --core, manifest, run r2-ch14t
r2-ch14u, cert 101; any FAIL stops the chat with a report. Read RULINGS-R2.md last block first: the
chat-95 block governs and it says a finding is not a question — deviations in the mathematics and in
the prose are recorded and flagged for repair, never put to M, and Prints & Proofs is read before any
question is asked. Do not ask M to rule on a defect. Read DEFERRED.md; chat 100's block is the last
of twenty-nine. The standing block's Phase 0–4 Löwdin/three-body plan is executed carried state;
discard it per Ruling 41 — its discard is W-118, not W-107. Line numbers are MEMBER line numbers and
are never carried between chats, and neither is any count: re-scan every heading on
The_Method_1_6-2.md before reading a line. A Register line number is not a Register entry number —
HANDOFF-52 lost a chat's worth of confidence to that, so quote an entry's headline before citing it.
Chapter 23 closed in chat 98; chat 99 read §24–§24.7 and chat 100 read §24.8–§24.9. Then continue
Phase R2 under the chat-81 cadence: take §24.10–§24.13, main L6817–L6883, 67 lines, four headings,
closing the chapter, and decide the cut before reading. Read it all, census its claims into
computable and prose, then run exactly two instrument batches, r2-ch14v computable and r2-ch14w
prose, importing heading_line, section_span, has_token and enclosing from r2lib — copy nothing, pass
them the LINE LIST and not the member text, and read the six volume MEMBERS, never a BUILDnnn bundle
path. Chat 100 measured that Chapter 24 retires its own headline figures at L6632 — '1,442 interior
cells across 35 atomic systems, the bracket holds in every one' matches neither Appendix B's totals
line (1,105) nor its table (869) nor the present tested count (930) — and that §24.8–§24.9 then use
1,442 twelve times and thirty-five once while 1,105, 869 and 930 appear once each in the whole
chapter. Measure whether §24.10–§24.13 carry the retired figures or the current ones; that decides
whether the defect is two sections or the whole chapter. Resolve 14r-22, L6666's pointer at §24.12
for a structural exclusion it does not state. Check §24.11's four decline modes against the front
matter's L62. The Spectra Compendium's channel table is section II at spectra L293–L934 and states
its own totals at L900: 596 rows across 28 elements carrying 2,269 interior cells, 70 species, 119
two-member rows, 477 rows with three or more levels, largest blocks Si I 290 and He I 189 — bound
every parse to that span and check it against L900 before trusting one figure from it. Where the text
prints a sample, measure the population. Compare bases before calling a carried figure wrong. Match a
printed figure at the source's precision, not at yours. A convention stated in the source is not a
defect. Use the exact-token heading resolver, never prefix matching, and never span a section by
heading rank. Grep lowercase 'register NNN' by hand. Resolve every pointer to the claim and not the
heading, and if it fails at the named target grep the whole volume before recording it. Give every
negative claim its own witness, and state what a sweep covered before recording a negative from it. A
number beside a species is not that species' ceiling — read the header. ν is not n. Never round with
Python's round() — use Decimal.quantize and name the convention. A heading is not a statement, a
bound is not a measurement, a boundary case is not a violation. Re-read every verdict against the
numbers printed above it AND below it. When an instrument disagrees with a hand reading, or with a
totals line the source states about itself, suspect the instrument first. Close the section read
before the next opens. At close: bank both goldens with gate.py bank, write W-140 ending with a blank
line, build BUILD130 with close.py (reverse must recover b5fd5d3a…), write HANDOFF-54. A changed
append-only member is grown with --append, never --members; correcting a banked golden needs a
delete-only call first. No corrections, no Register entries, no TASK 1 until the review closes.
Handoff at 90–95 % of context or on a closed section read — never earlier, never mid-section. Timeout
on every call. Delete-only calls for pycache, never chained to gate.py bank. Never copy over an
existing file."
