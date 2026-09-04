# HANDOFF-58 — The Method 1.6 — chat 105 → chat 106

- Written from **chat 105** for **chat 106**. Live files: **BUILD90 main** (unchanged since chat
  62) and **BUILD134 compendia** (= BUILD133 + W-144 + DEF-105 + six new members). Register
  **1 to 1792** (1,628 numbered entries; unchanged — no Register entry since the chat-67 hold).
  W-144 IS seated; chat 106 seats nothing at open and writes W-145 at close.
- **Read RULINGS-R2.md at open, last block first.** The chat-95 block still governs and is still
  the last: **a finding is not a question.** A deviation in the mathematics or in the prose is
  recorded and **flagged for repair**, never put to M. **Prints & Proofs is read before any
  question is asked.** Only a choice no file can settle reaches M. The chat-81 cadence is
  unchanged.
- **Chapter 27 is OPEN, not closed.** Chat 105 read **L7203–L7331** (§27.1–§27.5.1, 129 lines).
  **§27.6 — `### 27.6 What this buys, and what it does not` at main L7332 — is unread**, and the
  chapter ends at **L7363**; `# PART VI — THE RECORD AND THE REACH` opens at L7364. That is
  **32 lines**, MEASURED by heading scan in chat 105. Re-measure it anyway before reading: a
  handoff figure is not a measurement.
- **§27.6 carries exactly one census row: id 1155**, `C9-OVERGENERALISATION-WORD`, main **L7359**,
  token *never*, in *The three languages were never in competition.* Chat 105 left it undisposed
  on purpose — only rows in range are closed. Chat 106's closure file will carry that one row.
  **A 32-line unit is well under the ceiling; consider carrying the read on into Chapter 28**
  (`## 28. Withdrawals`) after scanning its extent, rather than spending a whole chat on 32 lines.
- **Grep the volume before recording a figure as unreproducible.** Chat 105's worst near-miss:
  §27.2's bracket rows were priced against the asymptotic V = 4ν/3, missed 13.378 by 0.33 %, and
  **three figures — 13.378, 53.344 and 1.54 — were on their way into the record as
  unreproducible**. The excess scaled as 1/ν², which named the next term, and **main L6237** then
  supplied the exact form outright: *the exact V is rational at every ν — 32/11, 54/13, 256/47,
  250/37, 4000/299 — and 4ν/3 + 4/(9ν) is its asymptote.* All five satisfy
  **V(ν) = 4ν³/(3ν² − 1)**; ν = 10 gives 4000/299 = 13.378 and ν = 40 gives 256000/4799 = 53.344,
  and **log₂(32/11) = 1.5406 → 1.54** is Proposition 23.1's floor in bits.
- **Identify the denominator before comparing a percentage.** §27.5.1's 11.3 % reproduces exactly
  (11.3211 %) only as comparable **unordered** pairs over the **ordered** count n(n−1); over
  C(n,2) it is 22.6422 %. Same for the 0.3 % overlap (0.3248 %). The section states neither.
- **A heading match is not a body match.** The first heading scan for `## 27. Slack` hit **L147**,
  the contents entry, and measured the chapter as three lines. Every chapter heading in this book
  occurs at least twice; resolve to the body occurrence before taking an extent.
- **Test a symbol as a symbol.** §17.3's claim-locator was reported ABSENT because the instrument
  searched the word *delta* where the section prints **δ**. Test both, on the raw line.
- **A theorem number is not a section number.** *Theorem 18.2* (main L7321) is stated at
  **L4940**; §18.2 (L4970) is *ν is inadmissible as an axis*, a different object. Resolving the
  citation as a §-pointer produces a false pointer defect.
- **Line numbering.** Main-volume lines are numbered on the **member** (`The_Method_1_6-2.md`,
  1-based, 11,855 lines); the bundle numbers each line one higher because of its `<<<FILE:` header.
- **Carried state to discard (Ruling 41):** the standing prompt block's "Phase 0–4"
  Löwdin/three-body plan is executed carried state; do not re-open it or put it to M. Its discard
  is **W-118 (chat 81)**, not W-107. The absorption is W-009 / W-059 / W-063 and Registers
  1701–1724. Project knowledge holds BUILD12/BUILD53 only — list it, never read those bundles.
  Retired handoffs are gone from Drive; never fetch or cite one. **Never add HANDOFF-NN.md as a
  member.**
- **Known and pre-existing:** the compendia bundle carries **48 legacy `HANDOFF-NN.md` members**,
  identical in BUILD122–134. They extract into `members/` harmlessly, but a handoff must never be
  written into `members/` or passed to `--members`, or a seated member is silently overwritten.
- **Findings carried to R3:** the READ-chNN.md members (READ-ch15d is chat 105's) and W-101…W-144
  in WORKING-REGISTER.md; nothing is restated here. **Deferred cross-chapter items:** `DEFERRED.md`
  (**34 blocks**, chat 105's is the last) governs; do not re-derive.

## §0 Gate (each step its own tool call under `timeout 280`; any FAIL stops the chat with a report)

1. `ls -la /mnt/user-data/uploads /mnt/user-data/outputs /home/claude`; `recent_chats` confirms the
   latest chat is 105. Read `/mnt/project/CLAUDE.md` (project instruction; never a member).
2. Fetch both bundles by title: `Google Drive:search_files` with
   `title contains 'BUILD134_compendia' or title contains 'BUILD90_main'`, pageSize 5,
   excludeContentSnippets; `Google Drive:download_file_content` on each fileId. Both spill to
   `/mnt/user-data/tool_results/<id>.json`; note the two paths. MEASURED gate cost in chat 105:
   ≈ 18 %.
3. Bootstrap (the only step outside gate.py, because gate.py is a member):

```
timeout 280 python3 - <<'EOF'
import json, base64, hashlib, re, os
EXP={'main':'49065309b0c4fe8e055f693aed295cca','comp':'fb59fd89d62332f6917cdaa403000fae'}
NAME={'main':'/home/claude/The_Method_1_6_BUILD90_main_and_register.md','comp':'/home/claude/The_Method_1_6_BUILD134_compendia_papers_audits.md'}
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
   **5,664,255 B · `fb59fd89d62332f6917cdaa403000fae` · 71,543 lines**; **456 members extracted
   (2 + 454)**.
4. `python3 /home/claude/members/gate.py census` → `OK census: DEFECT-CENSUS.tsv byte-identical`
   (1,556 rows + header, ≈ 15 s).
5. `python3 /home/claude/members/gate.py run --core` → five `OK` (tower 976/1,654/2,535/13,585/
   70,905/199,130; kinds 1565 · 1356 · 499 · 149; minmax; r2-tools-constants; extent "1 to 1792").
6. `python3 /home/claude/members/gate.py manifest` → `MANIFEST OK`; MANIFEST.tsv **30,530 B ·
   6927e1a9df56e928df10726723afe6a1 · 456 lines**; WORKING-REGISTER.md **734,169 B ·
   bf4e1e0b48c42f8ebbca40bfc8d0279e · 6,555 lines**, ends **W-144**; DEFERRED.md **34 blocks**;
   RULINGS-R2.md 9,844 B · 10a2ea7e · 82 lines (unchanged); r2lib.py 21,022 B · 580d2ea2 · 453
   lines (unchanged); gate.py 9,377 B · a01ef15a; close.py 6,456 B · 98acae67; r2-tools.py 6,529 B
   · 4702f5f9; tower-2.py c0bce27a; census.py f5a73e2b; kinds.py 4262f7c5; minmax.py 26da1d78.
   If two `BUILD*_compendia` files are present after a close, pass `--comp <path>` explicitly.
7. `python3 /home/claude/members/gate.py run r2-ch15d r2-ch15e` → two `OK` (chat 105's goldens:
   r2-ch15d.out 11,551 B · 556b83a6 · 157 lines; r2-ch15e.out 19,655 B · a2c06d90 · 275 lines).
   **r2-ch15d imports numpy** and `fractions`; **r2-ch15e reads
   `/home/claude/PP_The_Method_1_6.md`** — the Prints & Proofs original — so **fetch that file
   before step 7 or r2-ch15e will fail on a missing path.** Fetch it from Prints & Proofs
   (`1vYctzLppUZ2vFPJDCZ6wvkgSdj3v_f6n`), title `The Method 1.6.md`, fileId
   `1vsWwRT9BmUNeMrqokuo4jI4DJnoADubH`, **738,550 B · md5 49900cf41f818ab789bb90fc596ac977**, and
   write it to `/home/claude/PP_The_Method_1_6.md`.
8. `python3 /home/claude/members/gate.py cert 106` → writes `/home/claude/GATE-ch106.txt`, verdict
   PASS only if every logged step passed. A FAIL anywhere stops the chat and is reported.

## What chat 105 did (do not repeat)

**Chapter 27's extent measured and the chapter opened.** L7203–L7363, 161 lines, seven `###`
subsections: 27.1 L7207, 27.2 L7228, 27.3 L7243, 27.4 L7276, 27.5 L7289, 27.5.1 L7299, 27.6 L7332.
**Unit read: L7203–L7331.** Six deviations, ten verified groups, six incidentals, seven census
rows disposed. All of it is in `READ-ch15d.md`; **do not re-measure any of it.**

**The findings that carry:**

- **15d-01 — the same passage printed twice, in two chapters, with two Register entries.**
  §9.2 **L1961–L1990** and §27.5.1 **L7299–L7330**. Shared verbatim: the display sentence *Between
  any two points there is an interval, and the method returns its measure* (L1963 / L7314); all
  three rows of the interval table (L1970–L1974 / L7304–L7308); *Theorem 18.2 permits it* (L1980 /
  L7321); *…separately bounded and rarely both* (L1984 / L7327). **§9.2 closes Register 438,
  §27.5.1 closes Register 446.** Detail diverges both ways — §9.2 alone has *five forms*, *range
  [3, 23]*, §14.3 and §18.4.1; §27.5.1 alone has 11.3 %/24.7 %, §17.3's δ = f − ℓ and convexity.
  **Each copy says the other left the thing unsaid** (L1977–L1978 against L7301–L7302). Only
  **2 of 24 lines are byte-identical** — the copies are wrapped differently, so a line-identity
  check finds nothing; the test that works is a normalised phrase match.
- **15d-02 — §27.2's periodic-table log column, L7236.** 0.337 printed; ln(126/90) = 0.336472 →
  **0.336** under both conventions, and no base gives 0.337. The other four rows are exact under
  ln. exp(0.337) = 1.400739, so the printed log needs a ratio of 1.4007.
- **15d-03 — the unstated denominator.** 11.3 % and 0.3 % reproduce only over n(n−1).
  **24.7 % is NOT RECONSTRUCTED** — my composition relation (tgt(a) = src(b)) gives 3.03 %, and
  under the standing rule the reconstruction is the suspect. **Do not carry 3.03 % forward as a
  finding.** mc **L1284** describes the relation with a direction, source signature (n, ℓ, k, 2S)
  against target (e, f, g, 2S′) — start there.
- **15d-04 — §27.1's table is shattered mid-word** (`orde`/`r`, `geo`/`metr`/`y`, `calcu`/`lus`) and
  is **identical in Prints & Proofs at P7133–P7150** — carried from the original input. Adjacent:
  **only §27.3 is a markdown pipe table**; §27.1, §27.2, §27.4 and §27.5.1 are space-aligned.
- **15d-05 — an assertion cited as a proof.** L7301 and **Register 446's own headline** both credit
  §27.2 with proving the identification; *prove* does not occur in §27.2's span.
- **15d-06 — Ruling 45 reaches twenty-one:** L7244 (*The name was chosen before the quantity was
  analysed*) and L7312 (*Three sections computing one shape, none citing the other two*).

**What reproduced exactly, so R3 does not re-derive it:** the 6,912 bounding box measured on the
lattice (widths 3×2×3×4×3×2×4×4) and its 7.082 / 1.958; **13.378 and 53.344 from the exact rational
V**, with their ln and log₂ columns; **1.54 = log₂(32/11)**; the bits table at all four computable
rows (105.1, 47.4, 0.0, 0.0) and the bits/cell column dividing by |X|; the calendar row entire;
d = ∏(|Δᵢ|+1) = τ(lcm/gcd) as **structurally forced**; V > 2 ⟺ log₂V > 1 as an identity of the
base; **every section pointer in the unit** — docket 9 gains no member; Figure 27.1's two sites and
its caption, Ruling 45 clean.

**Seven instrument faults, self-caught and rewritten, none trimmed.** Both instruments were deleted
in delete-only calls before rewriting. The five worth repeating are in the bullets above and in
READ-ch15d's closing section.

## Chat 106's section read — §27.6, and probably Chapter 28

- **Re-measure §27.6 by heading scan before reading a line**, resolving `### 27.6` to its body
  occurrence. Chat 105 measured L7332–L7363, 32 lines; that is a figure to re-take, not to trust.
- **Dispose of census row 1155 (L7359) and only it.** The next `main` rows above and below are
  outside §27.6.
- **32 lines is a third of the ceiling.** Scan `## 28. Withdrawals` (main **L7364** region — the
  `# PART VI` banner sits at L7364, so 28's `##` follows it) and cut one unit that closes Chapter
  27 and opens Chapter 28 against the 141-line ceiling, rather than spending a chat on 32 lines.
  Never split a section read across chats.
- **What the docket owes anywhere in the volume**, and what chat 106 should test if its unit
  touches it: docket 5's Ruling 45 sweep (**twenty-one** members); docket 9's pointer sweep
  (eighteen members) — with a claim-locator beside every token test, symbols tested as symbols,
  and **§24.6 tested as a magnet, not just a target**; docket 19's false-universal sweep; docket
  20's absent-member sweep (Sr, C IV, the sulphur-like sequence, Rb); and **the new duplicated-
  section sweep** (DEF-105 item 1).
- **The channel table remains the arbiter for every species figure.** Section II is spectra-member
  **L293–L934**; its own totals line is **L900**: *596 channel rows across 28 elements · 2,269
  interior cells parsed.* Row format
  `| species | series | n | levels | interior | bracket | n* range | δ | σ(δ) | fits | limit cm⁻¹ |`;
  the column headed **fits** holds the ionisation stage; `bracket` reads `m/k`, `no-triple` or
  `untested` (**392 / 78 / 126 rows**, 1,577 bracketed cells, 70 species, 61 of them tested).
  Bound every parse to that span and check it against L900 before trusting one figure from it.

Instruments: **r2-ch15f** (computable) and **r2-ch15g** (prose). Import `heading_line`,
`section_span`, `has_token` and `enclosing` from r2lib by path; **copy nothing**; **read members,
never a bundle**; **pass the resolvers the LINE LIST, not the member text**. Six functions are
still owed to r2lib and DEFERRED lists them; note that `heading_line` requires a trailing space
after the number, so the Register's bare `### 96` headings return None — locate Register entries
with an explicit `^#{1,4}\s*N\s*$` match, and **quote an entry's headline before citing it — a
Register line number is not an entry number.**

**Standing method, unchanged and all of it earned:** exact-token heading resolver, never prefix,
and **resolved to the body occurrence, not the contents entry**; never span a section by heading
rank; grep lowercase `register NNN` by hand; check every printed pair count against C(N, 2) **and
name the denominator**; resolve every pointer to the claim and not the heading, **and locate where
the claim does live**; test on the **raw** line, case-insensitively, word-bounded, in the word's
other forms, **and in the symbol as well as the name**. Give every negative claim its own witness
and **state what a sweep covered before recording a negative from it**. Check the arithmetic of
every ratio and percentage; **never round with `round()`** — use `Decimal.quantize` and name the
convention, and sweep **both** conventions when the last place is in doubt. **Sweep the convention,
not just the base** — log base, centring, rounding mode, denominator and physical constant have all
moved a verdict. A formula numerator is not a value; a citation is not a declaration; a heading is
not a statement; a bound is not a measurement; a boundary case is not a violation; **an assertion is
not a proof**; **a theorem number is not a section number**; **a structurally forced figure is not
a finding**. Where the text prints a sample, measure the population. **Match a printed figure at
the source's precision, not at yours.** **Grep the volume and the Register for a later or exact
statement before recording any figure as unreproducible — that was worth three findings in chat
105.** **When an instrument disagrees with a hand reading already taken from the file, or with a
totals line the source states about itself, the instrument is wrong until proved otherwise** —
chats 94–105 hit that twice, four times, three, twice, twice, twice, twice, once, three times, four
times, ten times and **seven times**.

## The repair docket

Carried forward until R3 executes it. **None of these goes to M.** Chat 105's additions are in
DEFERRED's chat-105 block in full; the docket below is the standing list, unchanged from HANDOFF-57
except where chat 105 moved it.

1. **§14.5.2–§14.5.7 — six heading-only sections, forty citations. R3's largest single item.**
   MEASURED against the Prints & Proofs original: **authoring gap, not production loss.**
   Citations: §14.5.2 → 4, §14.5.3 → 1, §14.5.4 → 4, §14.5.5 → 4, §14.5.6 → 3, **§14.5.7 → 24**.
   **Order:** read the Register's nine §14.5.7 citations first and author to what they already say,
   then §21.5.4, then the Mathematical Compendium's twelve. Chat 90's **seed(Λ₈) = 7** is the
   settled material §14.5.7 owes.
2. **The §18.4.1 one-dimensional refinement — a missing Register entry** (main L5977–L5980).
   Register 319, which the passage cites, states a different claim.
3. **The Register has no entry for the correction §23.10.2 cites** (14n-A3) — a second missing
   entry, written when the chat-67 hold lifts, and interacting with 5 below.
4. **The σ collision — flagged for correction.** Rule 4 (main L6047) defines σ = 2R Z_eff² ·
   SE_pred / ν³; §22.5 (L6168) uses σ as the levels' measured uncertainty, and substituting Rule
   4's σ into §22.5's r = 2Z²R/(ν³σ) cancels ν³ identically — MEASURED r = 100.000000 at ν = 10,
   20, 40, 80. **Paired with 14x-04**, the same rule block's factor of two.
5. **The Ruling 45 class, twenty-one members** — L6453, the Figure 23.3 caption at L6483–L6484,
   L6628, L6632, chat 100's seven in 76 lines (L6748, L6756, L6791, L6801, L6803, L6810–L6812,
   L6813), L6887, L6907, chat 103's L6993, L6999 and L7040, chat 104's L7201, and **chat 105's
   L7244 and L7312**. L6812 instructs the author, L6999 addresses a referee, L7201 and L7244
   address the reader, **L7312 remarks on the book's own citation practice — and states 15d-01's
   duplication in the volume's own voice, so repair the two together.** Captions state facts only;
   *fetch\** is established vocabulary and is not a member.
6. **The Ruling 46 class, sweepable in one pass** (14r-18) — **Build 9** at main L6693 and L7659,
   plus five Register sites (L20, L31, L65, L68 and one further). Run 5 and 6 together.
7. **§23.8.3's affine-invariance reason** (chat 96's 14l-16) — the docket's only *reason* item. R3
   must decide which invariance the chapter claims before rewriting, and check §29.2 L7881, §29.7
   L8052 and App D.4.1 L10377. **15b-07 lands in the same neighbourhood: §23.8.1 L6345 is λ²'s
   home and L7185 should point there.**
8. **CLOSED as a finding (14z-08), not as a repair.** §23.6 L6319's pointer into §25.6 has no
   target anywhere in the volume; R3 authors the explanation or drops the clause — the clause is
   load-bearing for the novelty claim beside it, and it **cannot be repaired by redirection**.
9. **The pointer-off-by-one class, eighteen members, one withdrawn, one closed** — 14n-A1, 14n-A2,
   14n-A7, 14k-01, 14m-01, 14q-02/03/04, 14r-21, 14x-07 (two in one sentence), 14z-05/06/07,
   15b-07 (§23.11, target §23.8.1) and 15b-08 (mc L1932 → §24.6, target §26.6). **14r-22 struck;
   14t-06 closed at §25.2. Chat 105 adds none** — every pointer in its unit resolved. R3 sweeps
   **every §-pointer in the six volumes against the claim rather than the heading, in every form of
   the word, in the symbol as well as the name**, **on the raw line**, and **with a
   claim-locator**. **§24.6 is a magnet — two mis-aimed pointers land on it.**
10. **The unprinted-input class, now thirty-two members** — the HANDOFF-57 list of thirty, plus
    **chat 105's two: §27.3's subnet |ℛ(X)| ∈ {255, 256} and |X| ∈ {247, 248}, neither fixed by the
    section.** R3 splits the class into *conventions unstated* and *inputs absent*. **Q item P
    (L10958) already records the provenance split as owed** — repair them together, and with
    14v-06's B.1 shape. **New sub-class from 15d-03: denominators unstated** — every
    percentage-of-pairs figure in the six volumes.
11. **The 32/11 scope docket** (14j-01), with six measured main-volume sites — L6193, L6213,
    L6233, L6237, L6381, L10245 — plus 2.909 at four. L6381 claims the floor as an original result
    and must be repaired **after** the scope decision, not with it. **L6237 is also the site that
    states the exact rational V, which chat 105 needed to verify §27.2 — do not disturb it
    without re-checking Chapter 27.**
12. **The truncation-printed-as-equality class** (14l-02, 14l-03, 14n-A10, 15b-04, **15d-02 and
    L7308's asymptote-as-price**) — sweep every display equation whose own table disagrees with it,
    every site printing 4ν/3 **where the exact rational is meant**, and **every table cell that
    truncates where its neighbours round.**
13. **The two unsourced counts of L6517** (14n-A6, 14n-A7) — *619 refusals* and *§25.5's 1,061
    order-1 bounds*. §32.5 does carry the 1,061, so the pointer resolves; the recomputation at
    matched order is still owed. L6517 supersedes §25.5 while 1,061 stands at six further main
    sites with no pointer to the supersession — repair with 14x-02.
14. **The main-volume/compendium contradiction class** (14p-19, 14r-01/02/03, 14t-02/07/08,
    14v-06, 14x-05, 14z-03/04/13, 15b-06) — every figure the main volume attributes to a named
    channel or to the collection, against the compendium's current rows and totals. **Resolve K I
    *n*d 45.7 first**, **Ne I 16/131** and **K I 4/105**. **14r-19's double-tabulation must be
    settled before any recount — and it is nine keys and 18 rows wider (14x-10).**
15. **The retired-basis class** (14t-01), bounded to §24.8–§24.9 for Chapter 24. R3 sweeps every
    *An earlier version…* / *supersedes* / *and it does not* / *sharper than it was written* site
    in the six volumes and greps the retired wording forward from each — **in every form the figure
    takes**, word and numeral. MEASURED: *An earlier version* has **8 main sites** (L6066, L6280,
    L6483, L6628, L6632, L6907, L7066, L8676), **0 lower-case sites**, 1 register site. **Related
    and distinct: unretired text surviving its own correction** (14t-03/04/05), all inside §24.9.
    **Adjacent: pc L653's *Withdrawn at register 1168* against §26.5's live *66 of 66*** — sweep
    every withdrawn figure for a surviving reuse of its token.
16. **The Nesterov name-form sweep** (14m-07) — five forms in five places, one substantive (L8052
    credits Nesterov alone for a result §23.8.1 credits to both), plus *"KI"* without its space at
    L6657, L6716 and L6704, *"neon II"* spelled out at L6704, and the Edlén Handbuch chapter dated
    1960 at two sites and 1964 at five (14r-20), which also makes L6683's *sixty-five years old*
    wrong under both. **14x-08: *Cooper-type node* at L6896 is unattributed** — R3 sweeps every
    physics eponym against the bibliography. Brudno, Singer and Aitken all came back clean.
17. **The single-witness class** — chat 102's seven, chat 103's six, chat 104's four. **Chat 105
    adds none: all twelve of its single-site figures are internally reproduced**, and **1.54 left
    the class** once log₂(32/11) was computed. R4 should state which figures are unverifiable
    rather than leaving them looking checked, and distinguish *unverifiable* from *uncorroborated*.
18. **Heading sentences finishing in the body** (14q-06) — **three**: L4407 (+ "routes"), L6582
    (+ "one"), L8659 (+ "disanalogy"). Chats 101–105 confirmed none of their thirty-one headings
    joins them.
19. **The false-universal class** (14v-01, the He I monotone-fall claim, L6970, and L7075 broken
    twice over). A sentence of the form *every X in this work…* is a computable claim about the
    collection and must be measured against the channel table. **Chat 105's universals — *an
    interval is total*, *every pair of cells has a meet and a join* — are about the algebra, not
    the collection, and are correctly not members.**
20. **The absent-member class** (14v-02, 14x-05, 14z-13, 15b-09). C IV has no row while C I, C II,
    C III and C V do; **Sr has no row at any stage**; no member of the sulphur-like sequence has a
    row while §25.6.6 prices a route on all five; and **Rb has no row in six volumes** while §26.5
    prices the chapter's only empirical test on Rb ns–ns. MEASURED stage lists: Ca I II IX;
    Ba II III; Ti III XI; Sc III; Hg II; Al I II III IV; Ga I II; Li I II III; **Sr none; Sc VI
    none; Rb none.**
21. **The end-rule overstatement** (14v-07) — §24.13's L6877 and L6879 generalise from the neutral
    end to both ends against the section's own table. Repair L6877 and L6879, not L6869. **A
    summary row that outruns the prose above it is its own shape** — sweep for it.
22. **The census anchor** (14v-08) — §24.12 must state which member of a sequence D is computed on,
    and print the census's range (27 + 12 + 5 = 44 sequences, range stated nowhere).
23. **The caption-corrected-but-not-the-prose class** (14x-02), **now a section-scale class
    (14z-01), a cross-volume one (15b-06), and a Register-scale one (15d-05)**. A Register ruling
    repaired the Figure 25.1 caption and its prose still says the superseded thing; Registers
    801–803 rule on §25.6's *deduction* and the whole section still says the superseded thing;
    main L297 calls §26.2's result a tautology while §26.2 and mc L2078 present it as a
    measurement; and **Register 446's headline credits §27.2 with a proof it does not contain.**
    R3 sweeps **every Register ruling naming a caption, a figure or a section**, and **every
    self-assessment the volume makes of its own result**, and checks the surrounding text moved
    with it. **This is the largest live class after item 1.**
24. **Two compendium data defects** (14x-09, 14x-10): spectra **L562**'s malformed `n 41–5`
    (read 41–55), and **nine duplicated (species, series) keys over 18 rows** with one copy tested
    and one untested in every pair.
25. **The inherited-estimate class** (14z-02). A bracket whose edge is set by an estimated rather
    than a measured input, in a section that disqualifies exactly that. Sweep every bracket in the
    six volumes for an edge that traces back to an estimate.
26. **The spliced-text class, bounded to one member** (15b-01/02) — main **L7156**, repaired by
    restoring **about 0.09 %** *and* cutting §29.8's table cell. **Six volumes swept: no second
    site.** Adjacent and separate: **§29.8's L8089 cell cites its own section.**
27. **NEW — the duplicated-section class (15d-01).** §9.2 L1961–L1990 and §27.5.1 L7299–L7330 are
    one passage with two Register entries, 438 and 446, and divergent detail in each copy. R3
    decides which site holds it, merges, and reconciles the entries with a **new** entry citing
    both — append-only, neither removed. **Sweep owed across the six volumes**, by normalised
    phrase match on display sentences and table rows, **not** by line identity: only 2 of these 24
    lines are byte-identical because the copies are wrapped differently.
28. **NEW — table formatting (15d-04).** Four of Chapter 27's five tables are space-aligned plain
    text and §27.1's is shattered mid-word; the shattering is in Prints & Proofs too. R3 rebuilds
    them and sweeps the six volumes for both shapes.

## Close (chat 106)

`gate.py bank r2-ch15f r2-ch15g`; delete pycache in its own delete-only call; write `W-145.md`
(begins `### W-`, **ends with a blank line** — close.py asserts it); append a DEFERRED block as
`DEF-106.md`; then

```
timeout 280 python3 members/close.py --old The_Method_1_6_BUILD134_compendia_papers_audits.md \
  --new The_Method_1_6_BUILD135_compendia_papers_audits.md --w W-145.md \
  --main The_Method_1_6_BUILD90_main_and_register.md --append DEFERRED.md DEF-106.md \
  --members members/READ-ch15f.md members/CENSUS-CLOSURES-ch15f.tsv members/r2-ch15f.py \
  members/r2-ch15f.out members/r2-ch15g.py members/r2-ch15g.out
```

It must print **reverse recovers md5 fb59fd89d62332f6917cdaa403000fae == old: True** before
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
BUILD135, HANDOFF-59 and the READ file to `/mnt/user-data/outputs` and present them.

## Drive actions for M

- **Upload** to Materials (`1XX_5f3PZB6tjRtiZ2GIgd8Tt7i_4GgkY`): `HANDOFF-58.md` and
  `The_Method_1_6_BUILD134_compendia_papers_audits.md`.
- **Retire** once BUILD134 gates PASS in chat 106: HANDOFF-57 and BUILD133, plus any earlier
  compendia builds still present (BUILD107–BUILD132) **except BUILD124**.
- **Keep BUILD124** for now — it is the only input under which chat 96's `r2-ch14l` and `r2-ch14m`
  reproduce, and §23.9.1's eight exact V values live in `r2-ch14l.out`. Read those values out of
  the **member** rather than re-running the instrument; that is the pattern R3 should adopt before
  BUILD124 is retired.
- **Keep:** BUILD90 main (unchanged since chat 62), the **Prints & Proofs** folder
  (`1vYctzLppUZ2vFPJDCZ6wvkgSdj3v_f6n`) — the authentication baseline under Ruling 56, used again
  this chat to settle §27.1's table, **and now required by the gate itself because r2-ch15e reads
  it** — the certificates, OWED-REGISTER-EXPANSIONS.md, OWED-EXPANSIONS-2.md, covers8.json,
  factor.py.

## Prompt for chat 106

"Chat 106. READ EVERYTHING BEFORE YOU DO ANYTHING. Live files: BUILD90 main (1,983,081 B, md5
49065309b0c4fe8e055f693aed295cca) and BUILD134 compendia (5,664,255 B, md5
fb59fd89d62332f6917cdaa403000fae, 71,543 lines, 454 members). List uploads, outputs and
/home/claude first. Run HANDOFF-58's §0 gate in full and in order — fetch both bundles by title,
bootstrap (decode, md5, extract, expect 456 files), fetch the Prints & Proofs original 'The Method
1.6.md' (738,550 B, md5 49900cf41f818ab789bb90fc596ac977) to /home/claude/PP_The_Method_1_6.md
because r2-ch15e reads it, then gate.py census, run --core, manifest, run r2-ch15d r2-ch15e, cert
106; any FAIL stops the chat with a report. Read RULINGS-R2.md last block first: the chat-95 block
governs and it says a finding is not a question — deviations in the mathematics and in the prose
are recorded and flagged for repair, never put to M, and Prints & Proofs is read before any
question is asked. Do not ask M to rule on a defect. Read DEFERRED.md; chat 105's block is the last
of thirty-four. The standing block's Phase 0–4 Löwdin/three-body plan is executed carried state;
discard it per Ruling 41 — its discard is W-118, not W-107. Line numbers are MEMBER line numbers
and are never carried between chats, and neither is any count or any heading list. Chapter 27 is
OPEN: §27.1–§27.5.1 (L7203–L7331) are read and closed; §27.6 at L7332 is unread and the chapter
ends at L7363. Re-measure it by heading scan, resolving the heading to its BODY occurrence — a
chapter heading also appears in the contents, and that mistake measured Chapter 27 as three lines
in chat 105. §27.6 is only 32 lines, so scan Chapter 28 as well and cut one unit against the
141-line ceiling that closes 27 and opens 28; never split a section read across chats. This unit
carries exactly one census row, id 1155 at L7359 — dispose of it and only it. A Register line
number is not a Register entry number — quote an entry's headline before citing it. Then continue
Phase R2 under the chat-81 cadence: read the unit in full, census its claims into computable and
prose, then run exactly two instrument batches, r2-ch15f computable and r2-ch15g prose, importing
heading_line, section_span, has_token and enclosing from r2lib — copy nothing, pass them the LINE
LIST and not the member text, and read the six volume MEMBERS, never a BUILDnnn bundle path. Give
every pointer test a claim-locator beside it, test symbols as symbols and not only as their names
(δ was reported absent from §17.3 because the instrument searched for the word delta), remember
that a theorem number is not a section number (Theorem 18.2 is at L4940, §18.2 is a different
object), and sweep what points AT a section as well as what it points to. Print a window around
each match, never the head of the line. Before recording a figure as unreproducible, grep the
volume and the Register for a later or exact statement — chat 105 was one step from recording
13.378, 53.344 and 1.54 as unreproducible when main L6237 states the exact V outright as
4ν³/(3ν²−1), whose values are 4000/299 and 256000/4799, and log₂(32/11) = 1.54. Sweep the
convention, not just the base: log base, rounding mode, and now the DENOMINATOR — §27.5.1's 11.3%
reproduces only as unordered pairs over the ordered count n(n−1). When your reconstruction of a
relation disagrees with a printed figure, the reconstruction is the suspect: 24.7% is logged NOT
RECONSTRUCTED, not as a deviation. Exclude paths, URLs, backticks and file extensions before
counting a corruption regex. Test every token in both its hyphenated and spaced forms. Identify the
population before comparing: the channel table is 596 rows, 2,269 interior cells and 1,577
bracketed cells. Section II is spectra L293–L934 with its own totals at L900; the column headed
fits carries the ionisation stage. Run symbol tests on the RAW line. Make every token test
case-insensitive and word-bounded, and filter compound numerals before counting a spelled-out
number. Match a printed figure at the source's precision, not at yours, and sweep both rounding
conventions when the last place is in doubt — never round with Python's round(), use
Decimal.quantize and name the convention. Digit-bound every numeral sweep and sweep both the comma
and comma-free forms. Give every negative claim its own witness, and state what a sweep covered
before recording a negative from it. Never enumerate a domain with a fixed map. Where the text
prints a sample, measure the population. An assertion is not a proof, a heading is not a statement,
a bound is not a measurement, a citation is not a declaration, and a structurally forced figure is
not a finding. When an instrument disagrees with a hand reading, or with a totals line the source
states about itself, suspect the instrument first — that fired seven times in chat 105 alone. Close
the section read before the next opens. At close: bank both goldens with gate.py bank, write W-145
ending with a blank line, build BUILD135 with close.py (reverse must recover fb59fd89…), write
HANDOFF-59. A changed append-only member is grown with --append, never --members; correcting a
banked golden needs a delete-only call first, and so does rewriting an instrument before it is
banked. No corrections, no Register entries, no TASK 1 until the review closes. Handoff at 90–95%
of context or on a closed section read — never earlier, never mid-section. Timeout on every call.
Delete-only calls for pycache, never chained to gate.py bank. Never copy over an existing file."
