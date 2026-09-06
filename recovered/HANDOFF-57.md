# HANDOFF-57 — The Method 1.6 — chat 104 → chat 105

- Written from **chat 104** for **chat 105**. Live files: **BUILD90 main** (unchanged since chat
  62) and **BUILD133 compendia** (= BUILD132 + W-143 + DEF-104 + six new members). Register
  **1 to 1792** (1,628 numbered entries; unchanged — no Register entry since the chat-67 hold).
  W-143 IS seated; chat 105 seats nothing at open and writes W-144 at close.
- **Read RULINGS-R2.md at open, last block first.** The chat-95 block still governs and is still
  the last: **a finding is not a question.** A deviation in the mathematics or in the prose is
  recorded and **flagged for repair**, never put to M. **Prints & Proofs is read before any
  question is asked.** Only a choice no file can settle reaches M. The chat-81 cadence is
  unchanged.
- **Chapter 26 is CLOSED**, whole, in chat 104 — main L7117–L7202. **Chapter 27 is unread**:
  `## 27. Slack` opens at main **L7203**.
- **Chapter 27's extent is NOT measured — measure it first.** Nothing about Chapter 27 was scanned
  beyond confirming its `##` at L7203. Run a full heading scan on `The_Method_1_6-2.md` to the next
  `## ` before reading a line and cut the unit against the 141-line ceiling that has held since
  chat 82. Chapter 27 carries census rows: DEFECT-CENSUS.tsv holds eight `main`
  C9-OVERGENERALISATION-WORD rows between **L7266 and L7359** (ids 1148–1155), so the closure file
  will **not** be a header only — dispose of every row in range.
- **A structurally forced figure cannot be a deviation.** Chat 104's worst near-miss: σ₂ =
  1.8 × 10⁻¹⁴ is a double-precision zero that the rank-1 algebra guarantees for *any* input, and a
  sloppy deflation reported 7.63 × 10⁻⁶ against it — a seven-order "deviation" that was entirely
  my own arithmetic. **Before recording a spectacular discrepancy, ask whether the printed figure
  is forced by the structure**; if it is, the instrument is the suspect.
- **A convention held fixed is a convention untested.** The σ₁ sweep held the log base at e and
  reported failure; adding log₁₀ doubled the space and moved the nearest hit. Sweep the base, the
  centring, the rounding mode and the constant — chat 104 needed all four.
- **A corruption regex matches every file path in the book.** `\d\.\d*(?=[a-z]{3})` returned 34
  main "hits", nearly all `figures/figure-6.1.png`. Exclude paths, URLs, backticks and file
  extensions before counting, or an isolated defect becomes a spurious class.
- **Line numbering.** Main-volume lines are numbered on the **member** (`The_Method_1_6-2.md`,
  1-based, 11,855 lines); the bundle numbers each line one higher because of its `<<<FILE:` header.
- **Carried state to discard (Ruling 41):** the standing prompt block's "Phase 0–4"
  Löwdin/three-body plan is executed carried state; do not re-open it or put it to M. Its discard
  is **W-118 (chat 81)**, not W-107. The absorption is W-009 / W-059 / W-063 and Registers
  1701–1724. Project knowledge holds BUILD12/BUILD53 only — list it, never read those bundles.
  Retired handoffs are gone from Drive; never fetch or cite one. **Never add HANDOFF-NN.md as a
  member.**
- **Known and pre-existing:** the compendia bundle carries **48 legacy `HANDOFF-NN.md` members**,
  identical in BUILD122–133. They extract into `members/` harmlessly, but a handoff must never be
  written into `members/` or passed to `--members`, or a seated member is silently overwritten.
- **Findings carried to R3:** the READ-chNN.md members (READ-ch15b is chat 104's) and W-101…W-143
  in WORKING-REGISTER.md; nothing is restated here. **Deferred cross-chapter items:** `DEFERRED.md`
  (**33 blocks**, chat 104's is the last) governs; do not re-derive.

## §0 Gate (each step its own tool call under `timeout 280`; any FAIL stops the chat with a report)

1. `ls -la /mnt/user-data/uploads /mnt/user-data/outputs /home/claude`; `recent_chats` confirms the
   latest chat is 104. Read `/mnt/project/CLAUDE.md` (project instruction; never a member).
2. Fetch both bundles by title: `Google Drive:search_files` with
   `title contains 'BUILD133_compendia' or title contains 'BUILD90_main'`, pageSize 5,
   excludeContentSnippets; `Google Drive:download_file_content` on each fileId. Both spill to
   `/mnt/user-data/tool_results/<id>.json`; note the two paths. MEASURED gate cost in chat 104:
   ≈ 16 %.
3. Bootstrap (the only step outside gate.py, because gate.py is a member):

```
timeout 280 python3 - <<'EOF'
import json, base64, hashlib, re, os
EXP={'main':'49065309b0c4fe8e055f693aed295cca','comp':'2eaa2f1523778581fabc996800de49ea'}
NAME={'main':'/home/claude/The_Method_1_6_BUILD90_main_and_register.md','comp':'/home/claude/The_Method_1_6_BUILD133_compendia_papers_audits.md'}
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
   **5,585,336 B · `2eaa2f1523778581fabc996800de49ea` · 70,401 lines**; **450 members extracted
   (2 + 448)**.
4. `python3 /home/claude/members/gate.py census` → `OK census: DEFECT-CENSUS.tsv byte-identical`
   (1,556 rows + header, ≈ 15 s).
5. `python3 /home/claude/members/gate.py run --core` → five `OK` (tower 976/1,654/2,535/13,585/
   70,905/199,130; kinds 1565 · 1356 · 499 · 149; minmax; r2-tools-constants; extent "1 to 1792").
6. `python3 /home/claude/members/gate.py manifest` → `MANIFEST OK`; MANIFEST.tsv **30,125 B ·
   85c9fc95dd662aa6d4db16366e9e1d51 · 450 lines**; WORKING-REGISTER.md **729,145 B ·
   e401cd224ac96d6f41a255bc042d08f3 · 6,488 lines**, ends **W-143**; DEFERRED.md **33 blocks**;
   RULINGS-R2.md 9,844 B · 10a2ea7e · 82 lines (unchanged); r2lib.py 21,022 B · 580d2ea2 · 453
   lines (unchanged); gate.py 9,377 B · a01ef15a; close.py 6,456 B · 98acae67; r2-tools.py 6,529 B
   · 4702f5f9; tower-2.py c0bce27a; census.py f5a73e2b; kinds.py 4262f7c5; minmax.py 26da1d78.
   If two `BUILD*_compendia` files are present after a close, pass `--comp <path>` explicitly.
7. `python3 /home/claude/members/gate.py run r2-ch15b r2-ch15c` → two `OK` (chat 104's goldens:
   r2-ch15b.out 9,045 B · a438e85b · 125 lines; r2-ch15c.out 11,439 B · bdfc010d · 156 lines).
   **r2-ch15b imports numpy** (2.4.4 in chat 104's container) as well as r2lib; both read members
   only. An AttributeError means the extraction seated a pre-lift r2lib and the chat stops.
8. `python3 /home/claude/members/gate.py cert 105` → writes `/home/claude/GATE-ch105.txt`, verdict
   PASS only if every logged step passed. A FAIL anywhere stops the chat and is reported.

## What chat 104 did (do not repeat)

**Chapter 26 is closed whole** — main **L7117–L7202, 86 lines, seven `###` subsections**,
boundaries measured by heading scan before a line was read and confirmed by `section_span`.
**Twelve deviations, twelve verified, six incidentals, zero census rows in range** (measured — the
nearest `main` rows are L7266 onward, so CENSUS-CLOSURES-ch15b.tsv is a header only). All of it is
in `READ-ch15b.md`; **do not re-measure any of it.**

**The findings that carry:**

- **15b-01/02 — a spliced sentence, its source located, the class bounded to one.** L7156 prints
  *measuring C₆ to 1% fixes ν to about 0.0the searched bound of §29.8 — from 1/p_eff at n =*. The
  intruding string is a verbatim cell of **§29.8's own claims table at main L8089**. **Prints &
  Proofs carries the identical line at P7082** — authoring defect, not production loss. The lost
  figure is recoverable: 1/p_eff(100) = 0.087416, so it read **about 0.09 %**. **Six volumes swept
  for the shape: one genuine site, L7156 itself.**
- **15b-03/04 — the Aitken table's constant and one truncated cell.** The column is **4/4 exact at
  R = 109737.30** under the window (n−1, n, n+1) and **3/4 at the book's R = 109737.31568**, where
  T(10) prints 1097.3730 against 1097.3732. T(20)/3 = 91.44775 prints as **91.4477** where either
  convention gives 91.4478.
- **15b-05/06 — σ₁ unreproducible over 120 bases; σ₂ structurally forced.** 9.49 × 10¹ has one
  site in six volumes and no base reproduces it (nearest 91.59, span 11.98–505.1); the fifteen
  quantities and forty ν values are printed nowhere and the table names eight observables.
  σ₂ = 1.8 × 10⁻¹⁴ is a double-precision zero the rank-1 algebra forces for any input — and
  **main L297 already calls the result *a tautology once §26.1's* rule is granted**, while §26.2
  presents it as a measurement and mc L2078 repeats it. **14z-01's shape again.**
- **15b-07/08 — two pointer failures, both targets located.** L7185's *λ² of §23.11* → §23.11
  carries zero λ; λ² = (2/3)T is at **§23.8.1 L6345** and **App D.4.1 L10368**. mc **L1932**'s
  *Proved — M §24.6* → §24.6 is *The isoelectronic pairs* with Aitken 0; the result is **§26.6**.
  **Docket 9 now stands at eighteen**, and §24.6 has absorbed two mis-aimed pointers.
- **15b-09/10/11 — Rb has no row in six volumes** while §26.5 prices the chapter's only empirical
  test on it; *Bracket 66 of 66* has no population of 66 and the only 66-population in the book is
  the triplet-above-singlet pair count, **withdrawn at register 1168** (pc L653); and the **cost
  law is never stated** — two sites, neither defining it, and no fit reproduces 1.05 % / 1.83 %.
- **15b-12 — Ruling 45's nineteenth member:** L7201, *stated rather than discovered by a reader.*

**What reproduced exactly, so R3 does not re-derive it:** the assembly rule p = 2a + 3b on all five
rows; (ν²)⁴/ν⁻³ = ν¹¹; kε to first order; **Singer's 12.58 and 11.44 exactly** at the published Rb
coefficients, monotone falling across nine points; T′²/T″ = (2/3)T at four ν; the Aitken column's
convergence to T/3 from below with the deficit falling as 1/n²; **91 and 23 cm⁻¹**; Singer and
Aitken both fully attributed (main L11589, L11634); **Figure 19.1 is a live, different figure**
(L5414/L5416), so the renumbering left no stale citation; docket 19 gains no member and 14q-06
stays at three.

**Ten instrument faults, self-caught and rewritten, none trimmed.** The four in W-143; the two
worth repeating are in the bullets above.

## Chat 105's section read — Chapter 27, opening at L7203

- **Measure the chapter first.** `## 27. Slack` is at main **L7203** and **nothing else about
  Chapter 27 is measured.** Run a full heading scan to the next `## `, then cut the unit — one
  section read, never split, never over the 141-line ceiling.
- **The unit will carry census rows.** Ids **1148–1155**, all `C9-OVERGENERALISATION-WORD`, at
  L7266, L7273, L7281 (×2), L7286 (×2), L7287 and L7359. CLAUDE.md §5's precedent applies: a
  C7/C9 row whose flagged token is a live figure, label, or the cited section's own claim is a
  regex artefact (precedents 678, 680–687, 1067, 1069). Dispose of every row **in range**, and
  only those in range.
- **What the docket already owes anywhere in the volume**, and what chat 105 should test if its
  unit touches it: docket 5's Ruling 45 sweep (now **nineteen** members, chat 104 adding L7201);
  docket 9's pointer sweep (**eighteen** members) — with a claim-locator beside every token test,
  and **§24.6 tested as a magnet, not just a target**; docket 19's false-universal sweep; docket
  20's absent-member sweep, which now covers Sr, C IV, the sulphur-like sequence and **Rb**.
- **The channel table remains the arbiter for every species figure.** Section II is spectra-member
  **L293–L934**; its own totals line is **L900**: *596 channel rows across 28 elements · 2,269
  interior cells parsed.* Row format
  `| species | series | n | levels | interior | bracket | n* range | δ | σ(δ) | fits | limit cm⁻¹ |`;
  the column headed **fits** holds the ionisation stage; `bracket` reads `m/k`, `no-triple` or
  `untested` (**392 / 78 / 126 rows**, 1,577 bracketed cells, 70 species, 61 of them tested).
  Bound every parse to that span and check it against L900 before trusting one figure from it.

Instruments: **r2-ch15d** (computable) and **r2-ch15e** (prose). Import `heading_line`,
`section_span`, `has_token` and `enclosing` from r2lib by path; **copy nothing**; **read members,
never a bundle**; **pass the resolvers the LINE LIST, not the member text**. Six functions are
still owed to r2lib and DEFERRED lists them; note that `heading_line` requires a trailing space
after the number, so the Register's bare `### 96` headings return None — locate Register entries
with an explicit `^#{1,4}\s*N\s*$` match, and **quote an entry's headline before citing it — a
Register line number is not an entry number.**

**Standing method, unchanged and all of it earned:** exact-token heading resolver, never prefix;
never span a section by heading rank; grep lowercase `register NNN` by hand; check every printed
pair count against C(N, 2); resolve every pointer to the claim and not the heading, **and locate
where the claim does live**; test on the **raw** line, case-insensitively, word-bounded, and in the
word's other forms — *cost law* and *cost-law* are different sweeps. Give every negative claim its
own witness and **state what a sweep covered before recording a negative from it**. Check the
arithmetic of every ratio and percentage; **never round with `round()`** — use `Decimal.quantize`
and name the convention, and sweep **both** conventions when the last place is in doubt. A formula
numerator is not a value; a citation is not a declaration; a heading is not a statement; a bound is
not a measurement; a boundary case is not a violation; a number beside a species is not that
species' ceiling; **and a structurally forced figure is not a finding**. Where the text prints a
sample, measure the population. **Compare bases before calling a carried figure wrong**, and
**match a printed figure at the source's precision, not at yours**. **Grep the Register for a later
entry naming the section before recording any figure as unreproducible.** **When an instrument
disagrees with a hand reading already taken from the file, or with a totals line the source states
about itself, the instrument is wrong until proved otherwise** — chats 94–104 hit that twice, four
times, three, twice, twice, twice, twice, once, three times, four times and **ten times**.

## The repair docket

Carried forward until R3 executes it. **None of these goes to M.** Chat 104's additions are in
DEFERRED's chat-104 block in full; the docket below is the standing list.

1. **§14.5.2–§14.5.7 — six heading-only sections, forty citations. R3's largest single item.**
   MEASURED against the Prints & Proofs original (738,550 B · md5 49900cf41f818ab789bb90fc596ac977):
   **authoring gap, not production loss.** Citations: §14.5.2 → 4, §14.5.3 → 1, §14.5.4 → 4,
   §14.5.5 → 4, §14.5.6 → 3, **§14.5.7 → 24**. **Order:** read the Register's nine §14.5.7
   citations first and author to what they already say, then §21.5.4, then the Mathematical
   Compendium's twelve. Chat 90's **seed(Λ₈) = 7** is the settled material §14.5.7 owes.
2. **The §18.4.1 one-dimensional refinement — a missing Register entry** (main L5977–L5980).
   Register 319, which the passage cites, states a different claim.
3. **The Register has no entry for the correction §23.10.2 cites** (14n-A3) — a second missing
   entry, written when the chat-67 hold lifts, and interacting with 5 below.
4. **The σ collision — flagged for correction.** Rule 4 (main L6047) defines σ = 2R Z_eff² ·
   SE_pred / ν³; §22.5 (L6168) uses σ as the levels' measured uncertainty, and substituting Rule
   4's σ into §22.5's r = 2Z²R/(ν³σ) cancels ν³ identically — MEASURED r = 100.000000 at ν = 10,
   20, 40, 80. **Paired with 14x-04**, the same rule block's factor of two.
5. **The Ruling 45 class, nineteen members** — L6453, the Figure 23.3 caption at L6483–L6484,
   L6628, L6632, chat 100's seven in 76 lines (L6748, L6756, L6791, L6801, L6803, L6810–L6812,
   L6813), L6887, L6907, chat 103's L6993, L6999 and L7040, and **chat 104's L7201**. **L6812 —
   *it should be written that way wherever the figure carries weight* — is an instruction to the
   author printed in a reader-facing volume; L6999 — *That is stated here so a referee does not
   have to ask* — addresses a referee; L7201 — *stated rather than discovered by a reader* —
   addresses the reader.** Captions state facts only; *fetch\** is established vocabulary and is
   not a member.
6. **The Ruling 46 class, sweepable in one pass** (14r-18) — **Build 9** at main L6693 and L7659,
   plus five Register sites (L20, L31, L65, L68 and one further). Run 5 and 6 together.
7. **§23.8.3's affine-invariance reason** (chat 96's 14l-16) — the docket's only *reason* item. R3
   must decide which invariance the chapter claims before rewriting, and check §29.2 L7881, §29.7
   L8052 and App D.4.1 L10377 for the same reasoning. **Chat 104's 15b-07 lands in the same
   neighbourhood: §23.8.1 L6345 is λ²'s home and L7185 should point there.**
8. **CLOSED as a finding (14z-08), not as a repair.** §23.6 L6319's pointer into §25.6 has no
   target anywhere in the volume; R3 authors the explanation or drops the clause — the clause is
   load-bearing for the novelty claim beside it, and it **cannot be repaired by redirection**.
9. **The pointer-off-by-one class, eighteen members, one withdrawn, one closed** — 14n-A1, 14n-A2,
   14n-A7, 14k-01, 14m-01, 14q-02/03/04, 14r-21, 14x-07 (two in one sentence), 14z-05/06/07, and
   **chat 104's 15b-07 (§23.11, target §23.8.1) and 15b-08 (mc L1932 → §24.6, target §26.6)**.
   **14r-22 struck; 14t-06 closed at §25.2.** R3 sweeps **every §-pointer in the six volumes
   against the claim rather than the heading, in every form of the word**, **on the raw line**,
   and **with a claim-locator**. **New: §24.6 is a magnet — two mis-aimed pointers now land on it,
   so sweep what points AT a section as well as what a section points to.**
10. **The unprinted-input class, now thirty members** — §22.1.2's δ = 0.35; §22.4.1's δ₂ = 0.06;
    L6060's 446×, L6068's 1,577, L6093's 3.47 %, L6104's *factor of 17*; §23.1 L6189's *agreement
    under 1 %*; §23.9.3's two columns; §23.10.3's displacement row; §23.12's window; the +0.86 Hill
    slope; the Kirkwood floor; the hydrogen row and Li II's s→f selection; the per-level provenance
    and the survival table's 0.125 printed 0.12; §24.13's δ basis and §24.11's unlabelled *cells*
    column; §25.2's fine-structure base and its 17-vs-16 interior count; ±1,594 and ±2,169; the
    892,700 ± 400 limit; *thirty-five other species* against 70/61; the unstated series term of
    δ(4s)/δ(5s); and **chat 104's six: the Aitken table's Rydberg constant and its window, the
    fifteen quantities, the forty ν values, Singer's c₀/c₁/c₂, the population of 66, and the cost
    law itself.** R3 splits the class into *conventions unstated* and *inputs absent*. **Q item P
    (L10958) already records the provenance split as owed** — repair them together, and with
    14v-06's B.1 shape.
11. **The 32/11 scope docket** (14j-01), with six measured main-volume sites — L6193, L6213,
    L6233, L6237, L6381, L10245 — plus 2.909 at four. L6381 claims the floor as an original result
    and must be repaired **after** the scope decision, not with it.
12. **The truncation-printed-as-equality class** (14l-02, 14l-03, 14n-A10, **15b-04**) — sweep
    every display equation whose own table disagrees with it, every site printing 4ν/3, and **every
    table cell that truncates where its neighbours round.**
13. **The two unsourced counts of L6517** (14n-A6, 14n-A7) — *619 refusals* and *§25.5's 1,061
    order-1 bounds*. §32.5 does carry the 1,061, so the pointer resolves; the recomputation at
    matched order is still owed. L6517 supersedes §25.5 while 1,061 stands at six further main
    sites with no pointer to the supersession — repair with 14x-02.
14. **The main-volume/compendium contradiction class** (14p-19, 14r-01/02/03, 14t-02/07/08,
    14v-06, 14x-05, 14z-03/04/13, and **chat 104's 15b-06: mc L2078 repeats σ₂ as a compendium
    finding while main L297 calls the result a tautology**) — every figure the main volume
    attributes to a named channel or to the collection, against the compendium's current rows and
    totals. **Resolve K I *n*d 45.7 first**, **Ne I 16/131** and **K I 4/105**. **14r-19's
    double-tabulation must be settled before any recount — and it is nine keys and 18 rows wider
    (14x-10).**
15. **The retired-basis class** (14t-01), bounded to §24.8–§24.9 for Chapter 24. R3 sweeps every
    *An earlier version…* / *supersedes* / *and it does not* / *sharper than it was written* site
    in the six volumes and greps the retired wording forward from each — **in every form the figure
    takes**, word and numeral. MEASURED: *An earlier version* has **8 main sites** (L6066, L6280,
    L6483, L6628, L6632, L6907, L7066, L8676), **0 lower-case sites**, 1 register site. **Related
    and distinct: unretired text surviving its own correction** (14t-03/04/05), all inside §24.9.
    **Adjacent, new: pc L653's *Withdrawn at register 1168* against §26.5's live *66 of 66*** —
    sweep every withdrawn figure for a surviving reuse of its token.
16. **The Nesterov name-form sweep** (14m-07) — five forms in five places, one substantive (L8052
    credits Nesterov alone for a result §23.8.1 credits to both), plus *"KI"* without its space at
    L6657, L6716 and L6704, *"neon II"* spelled out at L6704, and the Edlén Handbuch chapter dated
    1960 at two sites and 1964 at five (14r-20), which also makes L6683's *sixty-five years old*
    wrong under both. **14x-08: *Cooper-type node* at L6896 is unattributed, and the only Cooper in
    the bibliography is Cooper 1989 on k-consistency** — R3 sweeps every physics eponym against the
    bibliography. **Chat 103's Brudno check and chat 104's Singer and Aitken checks are the pattern
    and all three came back clean.**
17. **The single-witness class** — chat 102's seven (3.25, 24,634, 892,700, 55,000, 42,000, 79 %
    and the factor of 60), chat 103's six (±1,594, ±2,169, 1,081, 13.5743, 784,416, 785,209) and
    **chat 104's four: 9.49 × 10¹, 1.05 %, 1.83 % and the cost law's name.** R4 should state which
    figures are unverifiable rather than leaving them looking checked, and distinguish
    *unverifiable* from *uncorroborated*. **Counter-case: δ(4s), δ(5s) and δ̄ all recur at L6114,
    so grep before recording.**
18. **Heading sentences finishing in the body** (14q-06) — **three**: L4407 (+ "routes"), L6582
    (+ "one"), L8659 (+ "disanalogy"). Chats 101–104 confirmed none of their twenty-four headings
    joins them.
19. **The false-universal class** (14v-01, the He I monotone-fall claim, L6970, and L7075 broken
    twice over). A sentence of the form *every X in this work…* is a computable claim about the
    collection and must be measured against the channel table. **Chat 104's three universals are
    about the algebra, not the collection, and are correctly not members** — the distinction is the
    test R3 applies.
20. **The absent-member class** (14v-02, 14x-05, 14z-13, **15b-09**). C IV has no row while C I,
    C II, C III and C V do; **Sr has no row at any stage**; no member of the sulphur-like sequence
    S I, Cl II, Ar III, K IV, Ca V has a row while §25.6.6 prices a route on all five; and **Rb has
    no row in six volumes while §26.5 prices the chapter's only empirical test on Rb ns–ns.**
    MEASURED stage lists for the species Chapter 25 names: Ca I II IX; Ba II III; Ti III XI;
    Sc III; Hg II; Al I II III IV; Ga I II; Li I II III; **Sr none; Sc VI none; Rb none.**
21. **The end-rule overstatement** (14v-07) — §24.13's L6877 and L6879 generalise from the neutral
    end to both ends against the section's own table. Repair L6877 and L6879, not L6869. **A
    summary row that outruns the prose above it is its own shape** — sweep for it.
22. **The census anchor** (14v-08) — §24.12 must state which member of a sequence D is computed on,
    and print the census's range (27 + 12 + 5 = 44 sequences, range stated nowhere).
23. **The caption-corrected-but-not-the-prose class** (14x-02), **now a section-scale class
    (14z-01) and a cross-volume one (15b-06)**. A Register ruling repaired the Figure 25.1 caption
    and its prose still says the superseded thing; Registers 801–803 rule on §25.6's *deduction*
    and the whole section still says the superseded thing; and **main L297 calls §26.2's result a
    tautology while §26.2 and mc L2078 present it as a measurement.** R3 sweeps **every Register
    ruling naming a caption, a figure or a section**, and **every self-assessment the volume makes
    of its own result**, and checks the surrounding text moved with it. **This is the largest live
    class after item 1.**
24. **Two compendium data defects** (14x-09, 14x-10): spectra **L562**'s malformed `n 41–5`
    (read 41–55), and **nine duplicated (species, series) keys over 18 rows** with one copy tested
    and one untested in every pair.
25. **The inherited-estimate class** (14z-02). A bracket whose edge is set by an estimated rather
    than a measured input, in a section that disqualifies exactly that. Sweep every bracket in the
    six volumes for an edge that traces back to an estimate.
26. **The spliced-text class, bounded to one member** (15b-01/02) — main **L7156**, repaired by
    restoring **about 0.09 %** *and* cutting §29.8's table cell. **Six volumes swept: no second
    site.** Adjacent and separate: **§29.8's L8089 cell cites its own section.**

## Close (chat 105)

`gate.py bank r2-ch15d r2-ch15e`; delete pycache in its own delete-only call; write `W-144.md`
(begins `### W-`, **ends with a blank line** — close.py asserts it); append a DEFERRED block as
`DEF-105.md`; then

```
timeout 280 python3 members/close.py --old The_Method_1_6_BUILD133_compendia_papers_audits.md \
  --new The_Method_1_6_BUILD134_compendia_papers_audits.md --w W-144.md \
  --main The_Method_1_6_BUILD90_main_and_register.md --append DEFERRED.md DEF-105.md \
  --members members/READ-ch15d.md members/CENSUS-CLOSURES-ch15d.tsv members/r2-ch15d.py \
  members/r2-ch15d.out members/r2-ch15e.py members/r2-ch15e.out
```

It must print **reverse recovers md5 2eaa2f1523778581fabc996800de49ea == old: True** before
writing; if it does not, nothing is written and the failure is reported. `--append` arguments must
precede `--members`, and `--members` may be omitted entirely if nothing new is seated. **A changed
append-only member is grown with `--append <member> <delta-file>`, never passed to `--members`** —
close.py refuses a name collision, and a member needing *replacement* rather than growth has no
mechanism at all. After a close, `gate.py manifest` reports FAIL on changed members because the
extracted copies stay at pre-close state; **verify appends by reading the new bundle directly** —
and note the Register member lives in the **main** bundle, not the compendia bundle. `gate.py bank`
refuses to overwrite an existing `.out`; correcting an instrument after banking needs a
**delete-only** call to remove the golden, then bank again. **Rewriting an instrument before
banking also takes a delete-only call first** — never copy over an existing file. Then copy
BUILD134, HANDOFF-58 and the READ file to `/mnt/user-data/outputs` and present them.

## Drive actions for M

- **Upload** to Materials (`1XX_5f3PZB6tjRtiZ2GIgd8Tt7i_4GgkY`): `HANDOFF-57.md` and
  `The_Method_1_6_BUILD133_compendia_papers_audits.md`.
- **Retire** once BUILD133 gates PASS in chat 105: HANDOFF-56 and BUILD132, plus any earlier
  compendia builds still present (BUILD107–BUILD131) **except BUILD124**.
- **Keep BUILD124** for now — it is the only input under which chat 96's `r2-ch14l` and `r2-ch14m`
  reproduce, and §23.9.1's eight exact V values live in `r2-ch14l.out`. Read those values out of
  the **member** rather than re-running the instrument; that is the pattern R3 should adopt before
  BUILD124 is retired.
- **Keep:** BUILD90 main (unchanged since chat 62), the **Prints & Proofs** folder
  (`1vYctzLppUZ2vFPJDCZ6wvkgSdj3v_f6n`) — the authentication baseline under Ruling 56, and used
  again this chat to settle L7156 — the certificates, OWED-REGISTER-EXPANSIONS.md,
  OWED-EXPANSIONS-2.md, covers8.json, factor.py.

## Prompt for chat 105

"Chat 105. READ EVERYTHING BEFORE YOU DO ANYTHING. Live files: BUILD90 main (1,983,081 B, md5
49065309b0c4fe8e055f693aed295cca) and BUILD133 compendia (5,585,336 B, md5
2eaa2f1523778581fabc996800de49ea, 70,401 lines, 448 members). List uploads, outputs and
/home/claude first. Run HANDOFF-57's §0 gate in full and in order — fetch both bundles by title,
bootstrap (decode, md5, extract, expect 450 files), then gate.py census, run --core, manifest, run
r2-ch15b r2-ch15c, cert 105; any FAIL stops the chat with a report. Read RULINGS-R2.md last block
first: the chat-95 block governs and it says a finding is not a question — deviations in the
mathematics and in the prose are recorded and flagged for repair, never put to M, and Prints &
Proofs is read before any question is asked. Do not ask M to rule on a defect. Read DEFERRED.md;
chat 104's block is the last of thirty-three. The standing block's Phase 0–4 Löwdin/three-body plan
is executed carried state; discard it per Ruling 41 — its discard is W-118, not W-107. Line numbers
are MEMBER line numbers and are never carried between chats, and neither is any count or any
heading list. Chapter 26 is CLOSED. Chapter 27 opens at L7203 and its extent is NOT measured: run a
full heading scan on The_Method_1_6-2.md to the next ## before reading a line, then cut one section
read against the 141-line ceiling. This unit WILL carry census rows — ids 1148–1155, all
C9-OVERGENERALISATION-WORD, at L7266–L7359 — so dispose of every row in range and only those in
range. A Register line number is not a Register entry number — quote an entry's headline before
citing it. Then continue Phase R2 under the chat-81 cadence: read the unit in full, census its
claims into computable and prose, then run exactly two instrument batches, r2-ch15d computable and
r2-ch15e prose, importing heading_line, section_span, has_token and enclosing from r2lib — copy
nothing, pass them the LINE LIST and not the member text, and read the six volume MEMBERS, never a
BUILDnnn bundle path. Give every pointer test a claim-locator beside it, and sweep what points AT a
section as well as what it points to — §24.6 has now absorbed two mis-aimed pointers. Print a window
around each match, never the head of the line. Before recording a spectacular discrepancy, ask
whether the printed figure is structurally forced: chat 104's σ₂ 'deviation' was its own deflation
error, and the rank-1 algebra forces that value for any input. Sweep the convention, not just the
base — log base, centring, rounding mode and physical constant all moved chat 104's verdicts, and
the Aitken table turned out to use R = 109737.30, not the book's R = 109737.31568. Exclude paths,
URLs, backticks and file extensions before counting a corruption regex, or one defect becomes a
34-member class. Test every token in both its hyphenated and spaced forms. Identify the population
before comparing: the channel table is 596 rows, 2,269 interior cells and 1,577 bracketed cells, and
the volumes' claims use all three words. Section II is spectra L293–L934 with its own totals at
L900; the column headed fits carries the ionisation stage. Run symbol tests on the RAW line. Make
every token test case-insensitive and word-bounded, and filter compound numerals before counting a
spelled-out number. Match a printed figure at the source's precision, not at yours, and sweep both
rounding conventions when the last place is in doubt — never round with Python's round(), use
Decimal.quantize and name the convention. Digit-bound every numeral sweep and sweep both the comma
and comma-free forms. Give every negative claim its own witness, and state what a sweep covered
before recording a negative from it. Never enumerate a domain with a fixed map. Where the text
prints a sample, measure the population. A number beside a species is not that species' ceiling —
read the header. ν is not n. A heading is not a statement, a bound is not a measurement, a citation
is not a declaration. Grep the Register before recording any figure as unreproducible or as a single
witness. When an instrument disagrees with a hand reading, or with a totals line the source states
about itself, suspect the instrument first — that fired ten times in chat 104 alone. Close the
section read before the next opens. At close: bank both goldens with gate.py bank, write W-144
ending with a blank line, build BUILD134 with close.py (reverse must recover 2eaa2f15…), write
HANDOFF-58. A changed append-only member is grown with --append, never --members; correcting a
banked golden needs a delete-only call first, and so does rewriting an instrument before it is
banked. No corrections, no Register entries, no TASK 1 until the review closes. Handoff at 90–95 %
of context or on a closed section read — never earlier, never mid-section. Timeout on every call.
Delete-only calls for pycache, never chained to gate.py bank. Never copy over an existing file."
