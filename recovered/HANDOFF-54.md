# HANDOFF-54 — The Method 1.6 — chat 101 → chat 102

- Written from **chat 101** for **chat 102**. Live files: **BUILD90 main** (unchanged since chat 62)
  and **BUILD130 compendia** (= BUILD129 + W-140 + DEF-101 + six new members). Register **1 to 1792**
  (unchanged — no Register entry since the chat-67 hold; 1,628 entries measured in the main bundle).
  W-140 IS seated; chat 102 seats nothing at open and writes W-141 at close.
- **Read RULINGS-R2.md at open, last block first.** The chat-95 block still governs and is still the
  last: **a finding is not a question.** A deviation in the mathematics or in the prose is recorded
  and **flagged for repair**, never put to M. **Prints & Proofs is read before any question is
  asked.** Only a choice no file can settle reaches M. The chat-81 cadence below it is unchanged.
- **Chapter 24 is closed** (chats 99–101). **Chapter 25 is unread.** Chat 102 opens it at L6884 and
  must decide its own cut from a fresh heading scan.
- **Never write an instrument that opens a `BUILDnnn` path** — the name changes every chat and the
  bundle comes to contain the instrument's own banked output. Chat 101's `r2-ch14v` and `r2-ch14w`
  read the six volume **members** by name and reproduced at their own bank.
- **A handoff naming N sites for a token must name the form each site carries.** HANDOFF-53 and
  DEFERRED's chat-100 block state *thirty-five* appears twice in Chapter 24, at L6632 and L6792.
  MEASURED word-bounded: **once, at L6792**; L6632 carries the numeral **35**. Nothing else in the
  chat-100 record moved — 1,442 reproduces at 13 chapter sites and 30 volume sites exactly. This is
  the fifth chat running to correct a count inside documents about not mis-stating counts, and the
  cause each time is a form or a base left unnamed beside the number.
- **Line numbering.** Main-volume lines are numbered on the **member** (`The_Method_1_6-2.md`,
  1-based, 11,855 lines); the bundle numbers each line one higher because of its `<<<FILE:` header.
  Chat 101 re-scanned Chapter 24 and found HANDOFF-53's boundaries exact — **which is not a reason to
  carry the next set. Re-scan.**
- **Carried state to discard (Ruling 41):** the standing prompt block's "Phase 0–4"
  Löwdin/three-body plan is executed carried state; do not re-open it or put it to M. Its discard is
  **W-118 (chat 81)**, not W-107. The absorption is W-009 / W-059 / W-063 and Registers 1701–1724.
  Project knowledge holds BUILD12/BUILD53 only — list it, never read those bundles. Retired handoffs
  are gone from Drive; never fetch or cite one. **Never add HANDOFF-NN.md as a member.**
- **Known and pre-existing:** the compendia bundle carries **48 legacy `HANDOFF-NN.md` members**,
  identical in BUILD122–130. They extract into `members/` harmlessly, but a handoff must never be
  written into `members/` or passed to `--members`, or a seated member is silently overwritten.
- **Findings carried to R3:** the READ-chNN.md members (READ-ch14v is chat 101's) and W-101…W-140 in
  WORKING-REGISTER.md; nothing is restated here. **Deferred cross-chapter items:** `DEFERRED.md`
  (**157,161 B · 30 blocks**, chat 101's is the last) governs; do not re-derive.

## §0 Gate (each step its own tool call under `timeout 280`; any FAIL stops the chat with a report)

1. `ls -la /mnt/user-data/uploads /mnt/user-data/outputs /home/claude`; `recent_chats` confirms the
   latest chat is 101. Read `/mnt/project/CLAUDE.md` (project instruction; never a member).
2. Fetch both bundles by title: `Google Drive:search_files` with
   `title contains 'BUILD130_compendia' or title contains 'BUILD90_main'`, pageSize 5,
   excludeContentSnippets; `Google Drive:download_file_content` on each fileId. Both spill to
   `/mnt/user-data/tool_results/<id>.json`; note the two paths. MEASURED gate cost in chat 101: ≈ 17 %.
3. Bootstrap (the only step outside gate.py, because gate.py is a member):

```
timeout 280 python3 - <<'EOF'
import json, base64, hashlib, re, os
EXP={'main':'49065309b0c4fe8e055f693aed295cca','comp':'16b9f2c4c495cca4a8c03bda939861e4'}
NAME={'main':'/home/claude/The_Method_1_6_BUILD90_main_and_register.md','comp':'/home/claude/The_Method_1_6_BUILD130_compendia_papers_audits.md'}
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
   **5,359,260 B · 16b9f2c4c495cca4a8c03bda939861e4 · 66,969 lines**; **432 members extracted
   (2 + 430)**.
4. `python3 /home/claude/members/gate.py census` → `OK census: DEFECT-CENSUS.tsv byte-identical`
   (1,556 rows + header, ≈ 15 s).
5. `python3 /home/claude/members/gate.py run --core` → five `OK` (tower 976/1,654/2,535/13,585/
   70,905/199,130; kinds 1565 · 1356 · 499 · 149; minmax; r2-tools-constants; extent "1 to 1792").
6. `python3 /home/claude/members/gate.py manifest` → `MANIFEST OK`; MANIFEST.tsv **28,917 B ·
   afe5b82c87e4cefdd146b1d9cb04bd26 · 432 lines**; WORKING-REGISTER.md **714,199 B ·
   b6ca96c501cb58fe685a1be18b15d15c · 6,292 lines**, ends **W-140**; DEFERRED.md **157,161 B ·
   30 blocks**; RULINGS-R2.md 9,844 B · 10a2ea7e · 82 lines (unchanged); r2lib.py 21,022 B ·
   580d2ea2 · 453 lines (unchanged); gate.py 9,377 B · a01ef15a; close.py 6,456 B · 98acae67;
   r2-tools.py 6,529 B · 4702f5f9; tower-2.py c0bce27a; census.py f5a73e2b; kinds.py 4262f7c5;
   minmax.py 26da1d78. If two `BUILD*_compendia` files are present after a close, pass
   `--comp <path>` explicitly.
7. `python3 /home/claude/members/gate.py run r2-ch14v r2-ch14w` → two `OK` (chat 101's goldens:
   r2-ch14v.out 5,685 B · 1c7abe16 · 84 lines; r2-ch14w.out 5,950 B · 2e314571 · 99 lines). Both
   import the lifted r2lib and read members only; an AttributeError means the extraction seated a
   pre-lift r2lib and the chat stops.
8. `python3 /home/claude/members/gate.py cert 102` → writes `/home/claude/GATE-ch102.txt`, verdict
   PASS only if every logged step passed. A FAIL anywhere stops the chat and is reported.

## What chat 101 did (do not repeat)

**§24.10–§24.13 is closed, and with it Chapter 24** — main **L6817–L6883, 67 lines, four headings**,
boundaries re-scanned and confirmed. **Eight deviations, thirteen verified, eight incidentals, no
census rows in range** (CENSUS-CLOSURES-ch14v.tsv is header only). All of it is in `READ-ch14v.md`;
**do not re-measure any of it.**

**The findings that carry furthest:**

- **14v-01 — a false universal, and the cleanest the phase has broken.** L6882: *every sequence in
  this work was entered through its neutral or first ion. It was not convenience; it was forced.*
  MEASURED over all 596 channel rows via the `fits` column (which carries the ionisation stage):
  28 elements, **18 enter at I, 4 at II, six enter above the first ion** — Ge, O, S, Sc, Ti at III
  and **Fe at XV**. R3 must decide scope, not soften wording; *it was forced* is load-bearing.
- **14v-02 — the absent-member class is new.** §24.13's lithium-like column holds out four points;
  its Z = 4 member is C IV. The compendium carries **36 carbon channels — C I, C II, C III and C V —
  and no C IV row anywhere in six volumes.** The printed column 11.1 / 1.4 / 0.8 / 1.8 has no basis
  at all. Distinct from *inputs absent*: the species is missing from a collection carrying its
  neighbours on both sides, and the gap is invisible from the main volume. **R3 should sweep every
  sequence the main volume treats as complete against the compendium's stage list per element.**
- **14v-03 — the sodium-like column reproduces in shape and in no digit.** ns rows give
  24.6 / 2.6 / 1.4 / 2.6 % against printed **23.4 / 2.4 / 1.3 / 2.5**; J-resolved 19.5 / 2.0 / 1.1 /
  2.1; np 34.7 / 3.5 / 1.8 / 3.5; *Z* as nuclear charge 2.5 / 0.9 / 0.9 / 2.7. **Every printed value
  sits below the ns measurement by 0.1–1.2 points** — systematic, not scatter. Name the δ basis
  before recomputing.
- **14v-08 — a rule whose own quantity admits its worked example.** §24.12 excludes on D ≥ 19;
  §24.11 offers Cu II as the first instance; L6837 prints Cu II's channel as **3d⁹5s**, and
  **D(3d⁹) = 2** by §24.12's own enumeration — the admission threshold. D = 19 arises for Ni-like
  only at the neutral member's 3d⁷ core. **D is member-dependent and §24.12 does not say which member
  it is computed on.** The five sequences do reproduce **19 to 37** on ionic 3d³…3d⁷ cores.

**Two dockets close.** **14t-01 is bounded to §24.8–§24.9** — the chapter's closing four sections
carry **zero** collection-wide totals (1,442 / 1,105 / 869 / 930 / 546 all have 0 sites in the unit).
**14r-22 is withdrawn** — L6666's pointer resolves at §24.12, which writes *excluded structurally*;
chat 99's negative came from testing the token *exclude*. Remove both from the docket.

**Six instrument faults, all self-caught and rewritten, none trimmed.** The four to carry: **a fixed
enumeration of a domain is a fault waiting for the datum that exceeds it** (a six-entry Roman map
died on `IX`, and the collection carries **XV** — the fault was pointing at 14v-01); **match by term
before taking a ratio between two-electron species** (averaging He I's ¹S with its ³S moved the
printed 0.53 to 0.59 and would have recorded a verified span as a deviation); **a numeral sweep must
be digit-bounded** (raw substring counting returned 14 chapter sites for *1,442* against chat 100's
13 — chat 100 was right, and the instrument was suspected first, as the rule requires); and **strip
markdown emphasis before any word-bounded token test** — `open-*f*` is invisible to `has_token`.

## Chat 102's section read — Chapter 25, first read

MEASURED by heading scan on the member in chat 101: **§25 opens L6884**; the headings visible in the
scan window are 25 (6884), 25.1 (6886), 25.2 (6890), 25.3 (6931), 25.4 (6949). **The scan was
windowed to L6580–L6960 and is not a chapter boundary measurement — re-scan the whole chapter before
reading a line**, and take the chapter's end from the next `## ` heading, not from this handoff.
HANDOFF-53 recorded fourteen headings through §25.6.6 (L7093) from chat 98's scan; treat that as a
hypothesis, not a finding.

- **Decide the cut before reading.** The 141-line ceiling has held since chat 82. §25.1–§25.2 alone
  is ~45 lines and §25.2 is *Five exclusions, which are three mechanisms* — the section chat 100's
  14t-06 identified as the true target of L6809's *§18's exclusions*.
- **What this chapter already owes, from the docket:**
  - **14t-06** — L6809 points at *§18's exclusions*; §18 carries the token zero times in 459 lines;
    the target is **§25.2**. Resolve it at §25.2 and record whether §25.2 states the claim L6809
    attributes to it.
  - **The front matter's L62** — *a structural exclusion covering five isoelectronic sequences from
    four decline modes* — was verified in chat 101 against §24.11 and §24.12. **§25.2's *five
    exclusions, which are three mechanisms* is a second, different five/N pairing**: check whether
    §25.2's five are §24.12's five (Cr-, Mn-, Fe-, Co-, Ni-like) or a different set, and whether
    *three mechanisms* is consistent with §24.11's four decline modes. This is the first thing to
    measure in the chapter.
  - **14n-A6 / 14n-A7** — §25.5's *1,061 order-1 bounds* (chat 99 confirmed §32.5 carries the 1,061;
    what is owed is recomputation at matched order) and the *619 refusals* of L6517.
  - **14m-01** — the §25.6 pointer with no target anywhere; the clause is load-bearing for the
    novelty claim beside it.
  - **Chat 98's ν_V / K I 45.7** — §25.5 prints 51.7 beside Ga I as a **ν**, read from its header;
    do not re-derive, and do not let a number beside a species be read as that species' ceiling.
- **The channel table remains the arbiter for every species figure.** Section II is spectra-member
  **L293–L934**, its own totals line is **L900**: *596 channel rows across 28 elements · 2,269
  interior cells parsed.* Row format
  `| species | series | n | levels | interior | bracket | n* range | δ | σ(δ) | fits | limit cm⁻¹ |`;
  **interior = levels − 2** on all 477 rows with three or more levels; the 119 two-member rows print
  interior 1 by stated convention; `bracket` reads `m/k`, `no-triple` or `untested`; the column headed
  **fits** actually holds the ionisation stage. **Bound every parse to that span and check it against
  L900 before trusting one figure from it** — chat 101's parse agreed at 596 / 28 / 2,269.
  The **B.1 Sources** table is at spectra **L975–L986** and is per-species; nothing in it records a
  species held from two sources (14v-06).

Instruments: **r2-ch14x** (computable) and **r2-ch14y** (prose). Import `heading_line`,
`section_span`, `has_token` and `enclosing` from r2lib by path; **copy nothing**; **read members,
never a bundle**. Six functions are still owed to r2lib and DEFERRED lists them; note that
`heading_line` requires a trailing space after the number, so the Register's bare `### 96` headings
return None — locate Register entries with an explicit `^#{1,4}\s*N\s*$` match (chat 99's P2, chat
100's P9 and chat 101's Register-extent check all do this and work).

**Standing method, unchanged and all of it earned:** exact-token heading resolver, never prefix;
never span a section by heading rank; **r2lib's resolvers take the LINE LIST, not the member text**.
Grep lowercase `register NNN` by hand. Check every printed pair count against C(N, 2). Resolve every
pointer to the claim and not the heading, and before recording any pointer as unresolved **read the
target section and test for the claim as that section words it**, case-exact and word-bounded —
**and test the word's other forms**, which is what withdrew 14r-22. If it fails there, grep the whole
volume before recording it. Give every negative claim its own witness. **State what a sweep covered
before recording a negative from it.** Check the arithmetic of every ratio and percentage; **never
round with `round()`** — use `Decimal.quantize` and name the convention. A formula numerator is not a
value; a citation is not a declaration; a heading is not a statement; a bound is not a measurement; a
boundary case is not a violation; **a number beside a species is not that species' ceiling** — read
the header. Where the text prints a sample, measure the population. **Compare bases before calling a
carried figure wrong**, and **match a printed figure at the source's precision, not at yours**. A
convention stated in the source is not a defect. Grep the Register for a later entry naming the
section before recording any figure as unreproducible. **When an instrument disagrees with a hand
reading already taken from the file, or with a totals line the source states about itself, the
instrument is wrong until proved otherwise** — chats 94–101 hit that twice, four times, three, twice,
twice, twice, twice and once.

## The repair docket

Carried forward until R3 executes it. **None of these goes to M.** Chat 101's additions are in
DEFERRED's chat-101 block in full; the docket below is the standing list, with 14r-22 struck and
14t-01 bounded.

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
5. **The Ruling 45 class, thirteen members and unchanged this chat** — L6453, the Figure 23.3 caption
   at L6483–L6484, chat 99's L6628 and L6632, and chat 100's seven in 76 lines: L6748, L6756, L6791,
   L6801, L6803, L6810–L6812 and L6813. **L6812 — *it should be written that way wherever the figure
   carries weight* — is an instruction to the author printed in a reader-facing volume**, and L6813
   prints the Q index's cost grading. **Chat 101's unit added none**, and cleared three candidates:
   *fetch\** is established vocabulary (main 11, register 94, spectra 2). Captions state facts only.
6. **The Ruling 46 class, sweepable in one pass** (14r-18) — **Build 9** at main L6693 and L7659,
   plus five Register sites (L20, L31, L65, L68 and one further). Run 5 and 6 together.
7. **§23.8.3's affine-invariance reason** (chat 96's 14l-16) — the docket's only *reason* item. R3
   must decide which invariance the chapter claims before rewriting, and check §29.2 L7881, §29.7
   L8052 and App D.4.1 L10377 for the same reasoning.
8. **The §25.6 pointer with no target** (chat 96's 14m-01) — author the explanation or drop the
   clause; the clause is load-bearing for the novelty claim beside it. **Chat 102 reads this chapter.**
9. **The pointer-off-by-one class, eleven members, one withdrawn** — 14n-A1, 14n-A2, 14n-A7, chat
   95's 14k-01, chat 96's 14m-01, chat 98's 14q-02/03/04, chat 99's 14r-21, and chat 100's 14t-06
   (L6809 → *§18's exclusions*; the target is §25.2). **14r-22 is struck**: it resolved once the
   target was tested in the target's own word-form. R3 sweeps **every §-pointer in the six volumes
   against the claim rather than the heading, in every form of the word**; `enclosing` makes the test
   cheap.
10. **The unprinted-input class, now eighteen members** — §22.1.2's δ = 0.35; §22.4.1's δ₂ = 0.06;
    L6060's 446×, L6068's 1,577, L6093's 3.47 %, L6104's *factor of 17*; §23.1 L6189's *agreement
    under 1 %*; §23.9.3's two columns; §23.10.3's displacement row; §23.12's window; the +0.86 Hill
    slope; the Kirkwood floor; chat 99's hydrogen row and Li II's s→f selection; chat 100's
    **per-level provenance** and the survival table's 0.125 printed 0.12; and chat 101's **§24.13 δ
    basis** (14v-03) and **§24.11's unlabelled *cells* column** (14v-04). R3 splits the class into
    *conventions unstated* and *inputs absent*. **Q item P (L10958) already records the provenance
    split as owed** — repair them together, and with 14v-06's B.1 shape.
11. **The 32/11 scope docket** (14j-01), with six measured main-volume sites — L6193, L6213, L6233,
    L6237, L6381, L10245 — plus 2.909 at four. L6381 claims the floor as an original result and must
    be repaired **after** the scope decision, not with it.
12. **The truncation-printed-as-equality class** (14l-02, 14l-03, 14n-A10) — sweep every display
    equation whose own table disagrees with it, and every site printing 4ν/3.
13. **The two unsourced counts of L6517** (14n-A6, 14n-A7) — *619 refusals* and *§25.5's 1,061
    order-1 bounds*. Chat 99 confirmed **§32.5 does carry the 1,061**, so the pointer resolves; what
    is still owed is the recomputation at matched order. **Chat 102 reads §25.5.**
14. **The main-volume/compendium contradiction class** (14p-19, widened by 14r-01/02/03, chat 100's
    14t-02/07/08 and chat 101's **14v-06**) — every figure the main volume attributes to a named
    channel or to the collection, against the compendium's current rows and totals. **Resolve K I
    *n*d 45.7 first** (chat 98) and **Ne I 16/131** (chat 99, witnessed twice) and **K I 4/105**.
    **14r-19's double-tabulation (six channels, 68 interior cells) must be settled before any
    recount.**
15. **The retired-basis class** (14t-01), **now bounded**: Chapter 24 retires its headline figures at
    L6628 and L6632 and leaves **twelve 1,442 sites and one *thirty-five*** standing in §24.8–§24.9;
    the chapter's closing four sections carry no collection-wide total at all. R3 still sweeps every
    *An earlier version…* / *supersedes* / *and it does not* / *sharper than it was written* site in
    the six volumes and greps the retired wording forward from each — **in every form the figure
    takes**, word and numeral. **Related and distinct: unretired text surviving its own correction**
    (14t-03/04/05), all inside §24.9.
16. **The Nesterov name-form sweep** (14m-07) — five forms in five places, one substantive (L8052
    credits Nesterov alone for a result §23.8.1 credits to both), plus chat 99's *"KI"* without its
    space at L6657, L6716 (§24.6's own pair table) and L6704, *"neon II"* spelled out at L6704, and
    the Edlén Handbuch chapter dated 1960 at two sites and 1964 at five (14r-20), which also makes
    L6683's *sixty-five years old* wrong under both. Chat 101 measured **no name-form defect** in its
    unit: Kaufman & Martin, ASD, NIST, Cu II, Ne II and Bi each take one form.
17. **The single-witness class** — chat 101 adds nine: 47379.140, 47379.7, 0.560, 107,942, 111,124,
    108,014, 110,366, *19 to 37* and 23.4. R4 should state which figures are unverifiable rather than
    leaving them looking checked, and distinguish *unverifiable* from *uncorroborated*.
18. **Heading sentences finishing in the body** (14q-06) — **three**: L4407 (+ "routes"), L6582
    (+ "one"), L8659 (+ "disanalogy"). Chat 101 confirmed none of its four headings joins them.
19. **The false-universal class — new in chat 101** (14v-01, and chat 99's He I monotone-fall claim).
    A sentence of the form *every X in this work…* is a computable claim about the collection and must
    be measured against the channel table, not read as summary. R3 sweeps **every *every … in this
    work / in the collection* construction in the six volumes**.
20. **The absent-member class — new in chat 101** (14v-02). C IV has no row anywhere while C I, C II,
    C III and C V do, and §24.13's lithium-like column needs it. R3 sweeps every sequence the main
    volume treats as complete against the compendium's stage list per element.
21. **The end-rule overstatement** (14v-07) — §24.13's L6877 and L6879 generalise from the neutral end
    to both ends against the section's own table (upper end 1.8 % and 2.5 %). Repair L6877 and L6879,
    not L6869. **A summary row that outruns the prose above it is its own shape** — sweep for it.
22. **The census anchor** (14v-08) — §24.12 must state which member of a sequence D is computed on,
    and print the census's range (27 + 12 + 5 = 44 sequences, range stated nowhere).

## Close (chat 102)

`gate.py bank r2-ch14x r2-ch14y`; delete pycache in its own delete-only call; write `W-141.md`
(begins `### W-`, **ends with a blank line** — close.py asserts this); append a DEFERRED block as
`DEF-102.md`; then

```
timeout 280 python3 members/close.py --old The_Method_1_6_BUILD130_compendia_papers_audits.md \
  --new The_Method_1_6_BUILD131_compendia_papers_audits.md --w W-141.md \
  --main The_Method_1_6_BUILD90_main_and_register.md --append DEFERRED.md DEF-102.md \
  --members members/READ-ch14x.md members/CENSUS-CLOSURES-ch14x.tsv members/r2-ch14x.py \
  members/r2-ch14x.out members/r2-ch14y.py members/r2-ch14y.out
```

It must print **reverse recovers md5 16b9f2c4c495cca4a8c03bda939861e4 == old: True** before writing;
if it does not, nothing is written and the failure is reported. `--append` arguments must precede
`--members`, and `--members` may be omitted entirely if nothing new is seated. **A changed
append-only member is grown with `--append <member> <delta-file>`, never passed to `--members`** —
close.py refuses a name collision, and a member needing *replacement* rather than growth has no
mechanism at all. After a close, `gate.py manifest` reports FAIL on changed members because the
extracted copies stay at pre-close state; **verify appends by reading the new bundle directly** —
and note the Register member lives in the **main** bundle, not the compendia bundle. `gate.py bank`
refuses to overwrite an existing `.out`; correcting an instrument after banking needs a
**delete-only** call to remove the golden, then bank again. Then copy BUILD131, HANDOFF-55 and the
READ file to `/mnt/user-data/outputs` and present them.

## Drive actions for M

- **Upload** to Materials (`1XX_5f3PZB6tjRtiZ2GIgd8Tt7i_4GgkY`): `HANDOFF-54.md` and
  `The_Method_1_6_BUILD130_compendia_papers_audits.md`.
- **Retire** once BUILD130 gates PASS in chat 102: HANDOFF-53 and BUILD129, plus any earlier
  compendia builds still present (BUILD107–BUILD128) **except BUILD124**.
- **Keep BUILD124** for now — it is the only input under which chat 96's `r2-ch14l` and `r2-ch14m`
  reproduce, and §23.9.1's eight exact V values live in `r2-ch14l.out`. Read those values out of the
  **member** rather than re-running the instrument; that is the pattern R3 should adopt before
  BUILD124 is retired.
- **Keep:** BUILD90 main (unchanged since chat 62), the **Prints & Proofs** folder
  (`1vYctzLppUZ2vFPJDCZ6wvkgSdj3v_f6n`) — the authentication baseline under Ruling 56 — the
  certificates, OWED-REGISTER-EXPANSIONS.md, OWED-EXPANSIONS-2.md, covers8.json, factor.py.

## Prompt for chat 102

"Chat 102. READ EVERYTHING BEFORE YOU DO ANYTHING. Live files: BUILD90 main (1,983,081 B, md5
49065309b0c4fe8e055f693aed295cca) and BUILD130 compendia (5,359,260 B, md5
16b9f2c4c495cca4a8c03bda939861e4, 66,969 lines, 430 members). List uploads, outputs and /home/claude
first. Run HANDOFF-54's §0 gate in full and in order — fetch both bundles by title, bootstrap
(decode, md5, extract, expect 432 files), then gate.py census, run --core, manifest, run r2-ch14v
r2-ch14w, cert 102; any FAIL stops the chat with a report. Read RULINGS-R2.md last block first: the
chat-95 block governs and it says a finding is not a question — deviations in the mathematics and in
the prose are recorded and flagged for repair, never put to M, and Prints & Proofs is read before any
question is asked. Do not ask M to rule on a defect. Read DEFERRED.md; chat 101's block is the last
of thirty. The standing block's Phase 0–4 Löwdin/three-body plan is executed carried state; discard
it per Ruling 41 — its discard is W-118, not W-107. Line numbers are MEMBER line numbers and are
never carried between chats, and neither is any count or any heading list: re-scan the whole of
Chapter 25 on The_Method_1_6-2.md before reading a line, and take its end from the next ## heading. A
Register line number is not a Register entry number — quote an entry's headline before citing it. A
handoff naming N sites for a token must name the form each site carries: thirty-five appears once, at
L6792; L6632 carries the numeral 35. Chapter 24 closed in chat 101. Then continue Phase R2 under the
chat-81 cadence: open Chapter 25 at L6884, decide the cut before reading — §25.1 is at L6886, §25.2
at L6890, §25.3 at L6931, §25.4 at L6949, from a windowed scan that is a hypothesis, not a
measurement. Read the unit in full, census its claims into computable and prose, then run exactly two
instrument batches, r2-ch14x computable and r2-ch14y prose, importing heading_line, section_span,
has_token and enclosing from r2lib — copy nothing, pass them the LINE LIST and not the member text,
and read the six volume MEMBERS, never a BUILDnnn bundle path. Measure §25.2's 'five exclusions,
which are three mechanisms' against §24.12's five sequences (Cr-, Mn-, Fe-, Co-, Ni-like) and against
§24.11's four decline modes and the front matter's L62 — chat 101 verified L62 against Chapter 24, so
any disagreement is §25.2's. Resolve 14t-06 there: L6809 points at §18's exclusions and §18 carries
the token zero times; §25.2 is the target. The Spectra Compendium's channel table is section II at
spectra L293–L934 and states its own totals at L900: 596 rows across 28 elements carrying 2,269
interior cells; bound every parse to that span and check it against L900 before trusting one figure
from it. The column headed fits carries the ionisation stage. B.1 Sources is at spectra L975–L986 and
records no species held from two sources. Strip markdown emphasis before any word-bounded token test.
Digit-bound every numeral sweep. Test a pointer's target in every form of the word before recording a
negative — that withdrew 14r-22. Never enumerate a domain with a fixed map; the collection carries an
ionisation stage XV. Where the text prints a sample, measure the population. Compare bases before
calling a carried figure wrong. Match a printed figure at the source's precision, not at yours. A
convention stated in the source is not a defect. Use the exact-token heading resolver, never prefix
matching, and never span a section by heading rank. Grep lowercase 'register NNN' by hand. Give every
negative claim its own witness, and state what a sweep covered before recording a negative from it. A
number beside a species is not that species' ceiling — read the header. ν is not n. Never round with
Python's round() — use Decimal.quantize and name the convention. A heading is not a statement, a
bound is not a measurement, a boundary case is not a violation. Re-read every verdict against the
numbers printed above it AND below it. When an instrument disagrees with a hand reading, or with a
totals line the source states about itself, suspect the instrument first. Close the section read
before the next opens. At close: bank both goldens with gate.py bank, write W-141 ending with a blank
line, build BUILD131 with close.py (reverse must recover 16b9f2c4…), write HANDOFF-55. A changed
append-only member is grown with --append, never --members; correcting a banked golden needs a
delete-only call first. No corrections, no Register entries, no TASK 1 until the review closes.
Handoff at 90–95 % of context or on a closed section read — never earlier, never mid-section. Timeout
on every call. Delete-only calls for pycache, never chained to gate.py bank. Never copy over an
existing file."
