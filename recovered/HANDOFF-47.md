# HANDOFF-47 — The Method 1.6 — chat 94 → chat 95

- Written from **chat 94** for **chat 95**. Live files: **BUILD90 main** (unchanged since chat 62)
  and **BUILD122 compendia** (= BUILD121 + W-132 + chat 94's DEFERRED block + six new members).
  Register **1 to 1792** (unchanged — no Register entry has been written since the chat-67 hold).
  W-132 IS seated; chat 95 seats nothing at open and writes W-133 at close.
- **Rulings and discipline:** the member `RULINGS-R2.md` (6,041 B · 30 lines, unchanged this chat)
  governs and is append-only; **read it at open, last block first** — the chat-81 block sets the
  cadence, and chats 82–94 have all run it. **Deferred cross-chapter items:** `DEFERRED.md`
  (**107,402 B · 22 blocks**, with chat 94's block) governs; do not re-derive. **Findings carried to
  R3:** the READ-chNN.md members (READ-ch14h is chat 94's) and W-101…W-132 in WORKING-REGISTER.md;
  nothing is restated here.
- **Line numbering — measure it, never carry it.** r2-tools, every prior chat and this handoff
  number main-volume lines on the **member** (`The_Method_1_6-2.md`, 1-based); the *bundle* numbers
  each line one higher because of its `<<<FILE:` header. HANDOFF-46 stated this rule and then
  carried eleven bundle-numbered boundaries in its own next-work list — every §22.2.1-onward figure
  was one high, corrected in chat 94's opening scan and recorded in W-132. **The rule that works is
  not "read the member" but "re-scan every boundary on the member before reading a line."** Chat 95
  must do this for Chapter 23 and must not trust the figures in the section below without a scan.
- **Carried state to discard (Ruling 41):** the standing prompt block's "Phase 0–4"
  Löwdin/three-body plan is executed carried state; do not re-open it or put it to M. Its discard is
  recorded in **W-118 (chat 81)**, not W-107. The absorption itself is W-009 / W-059 / W-063 and
  Registers 1701–1724; subject-matter claims about the three-body count resolve to Registers 489 and
  507. Project knowledge holds BUILD12/BUILD53 only — list it, never read those bundles. Retired
  handoffs are gone from Drive; never fetch or cite one. Never add HANDOFF-NN.md as a member.
- **Known and pre-existing, not introduced by chat 94:** the compendia bundle carries **48 legacy
  `HANDOFF-NN.md` members** (HANDOFF-2 … HANDOFF-53, plus HANDOFF-19-A), identical in BUILD121 and
  BUILD122. Their numbering collides with the current handoff series — a member `HANDOFF-46.md` is
  seated and is **not** the document chat 94 was given. They extract into `members/` harmlessly, but
  a handoff must never be written into `members/` and never passed to `--members`, or a seated
  member is silently overwritten. Flagged for M; no action taken.

## §0 Gate (each step its own tool call under `timeout 280`; any FAIL stops the chat with a report)

1. `ls -la /mnt/user-data/uploads /mnt/user-data/outputs /home/claude`; `recent_chats` confirms the
   latest chat is 94. Read `/mnt/project/CLAUDE.md` (project instruction; never a member).
2. Fetch both bundles by title: `Google Drive:search_files` with
   `title contains 'BUILD122_compendia' or title contains 'BUILD90_main'`, pageSize 5,
   excludeContentSnippets; `Google Drive:download_file_content` on each fileId. Both spill to
   `/mnt/user-data/tool_results/<id>.json`; note the two paths (the gate costs ≈ 13 %, MEASURED).
3. Bootstrap (the only step outside gate.py, because gate.py is a member):

```
timeout 280 python3 - <<'EOF'
import json, base64, hashlib, re, os
EXP={'main':'49065309b0c4fe8e055f693aed295cca','comp':'ac1f2310cc19e7fd60686cb90861134a'}
NAME={'main':'/home/claude/The_Method_1_6_BUILD90_main_and_register.md','comp':'/home/claude/The_Method_1_6_BUILD122_compendia_papers_audits.md'}
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
   **4,746,122 B · ac1f2310cc19e7fd60686cb90861134a · 58,350 lines**; **390 members extracted (2 + 388)**.
4. `python3 /home/claude/members/gate.py census` → `OK census: DEFECT-CENSUS.tsv byte-identical`
   (1,556 rows + header, ≈ 12 s).
5. `python3 /home/claude/members/gate.py run --core` → five `OK` (tower 976/1,654/2,535/13,585/70,905/
   199,130; kinds 1565 · 1356 · 499 · 149; minmax; r2-tools-constants; extent "1 to 1792").
6. `python3 /home/claude/members/gate.py manifest` → `MANIFEST OK`; MANIFEST.tsv **26,099 B ·
   1435646cd2618b59f2d747d56762d9fa · 390 lines**; WORKING-REGISTER.md **669,833 B ·
   d860b8eeb1def3d61855a0a4fe90de9f · 5,772 lines**, ends **W-132**; DEFERRED.md **107,402 B · 22
   blocks**; RULINGS-R2.md 6,041 B · 4cce8039; **r2lib.py 18,486 B · 3344ca87 · 396 lines**
   (unchanged this chat); gate.py 9,377 B · a01ef15a; close.py 6,456 B · 98acae67; tower-2.py
   c0bce27a; census.py f5a73e2b; kinds.py 4262f7c5; minmax.py 26da1d78; r2-tools.py 4702f5f9. If two
   `BUILD*_compendia` files are present after a close, pass `--comp <path>` explicitly.
7. `python3 /home/claude/members/gate.py run r2-ch14h r2-ch14i` → two `OK` (chat 94's goldens:
   r2-ch14h.out 17,870 B · b788fa4d · 263 lines, ≈ 0 s; r2-ch14i.out 14,454 B · de696a7a · 208 lines).
8. `python3 /home/claude/members/gate.py cert 95` → writes `/home/claude/GATE-ch95.txt`, verdict PASS
   only if every logged step passed. A FAIL anywhere stops the chat and is reported, not worked around.

## What chat 94 did (do not repeat)

**Chapter 22 is closed.** The remainder read whole — main **L6036–L6177, 141 lines, eleven
headings**, larger than any prior section read (93, 63, 99) — with every boundary re-measured
first, which is what caught HANDOFF-46's eleven carried line numbers. **Ten deviations, thirteen
verified, eight incidentals, one census row closed** (1134, *not a defect*, C9 regex artefact) in
`READ-ch14h.md` and `CENSUS-CLOSURES-ch14h.tsv`.

Two load-bearing findings, both internal contradictions and both subject matter. First: **§22.5's
admissibility ratio cancels against Rule 4's own σ.** `r = 2Z²R/(ν³σ)` is said to fall as ν⁻³, but
Rule 4 (L6047) defines σ = 2R Z_eff² · SE_pred / ν³, and substituting it makes ν³ cancel identically
— MEASURED r = 100.000000 at ν = 10, 20, 40, 80. Under the levels-uncertainty reading of σ, which
is what L6168 says, r falls as ν⁻³ exactly. One symbol, two quantities, and §22.5 is the chapter's
stated domain boundary. Second: **"ν, δ and V all need the ionisation limit" is false of V**, at
main L6133 and again at App A.12 L10035. V = w/e is a first difference over a second, so I cancels
— MEASURED identical at I = 0, 10⁵, 10⁶ — by the same argument A.12 proves for containment and
§22.4 states for δ₀.

Also: **§22.2.2's "same magnitude of asymmetry" is false by 193×** (1,592.86 against 8.24), its
table carrying a ratio and an absolute error in the same columns; **"agreement to four figures"** is
claimed of a pair sharing three digits and a pair sharing one; **§22.6's "the only linearly rising
quantity"** is contradicted by L = n/3 printed thirty-two lines above it; **"true for some species,
false for others"** has no witness among its own two ranges (2 × 0.4 = 0.8 against the tightest
bracket 1.398); **§22.4.1's predicted column needs δ₂ = 0.06**, never printed. **Five printed
< truncated lines 103-146 >
and not the heading; before recording any pointer as unresolved, read the target section and test
for the claim **as that section words it**, case-exact and word-bounded. Measure a claim and its
stated witness separately; check the arithmetic of every ratio and percentage; where the text prints
a sample, measure the population; read a section's *What survives* block as well as its *What this
withdraws* block; grep the Register for a later entry naming the section before recording any figure
as unreproducible; after writing any verdict that compares two measured numbers, re-read the
comparison against the numbers; never write a summary line that generalises over a list before the
list is printed; and — **new, from chat 94** — **never round with `round()`, and when an instrument
disagrees with a hand reading, suspect the instrument first.**

## Close (chat 95)

`gate.py bank r2-ch14j r2-ch14k`; delete pycache in its own delete-only call; write `W-133.md`
(begins `### W-`, **ends with a blank line** — close.py asserts this); append a DEFERRED block as
`DEF-95.md`; then

```
timeout 280 python3 members/close.py --old The_Method_1_6_BUILD122_compendia_papers_audits.md \
  --new The_Method_1_6_BUILD123_compendia_papers_audits.md --w W-133.md \
  --main The_Method_1_6_BUILD90_main_and_register.md --append DEFERRED.md DEF-95.md \
  --members members/READ-ch14j.md members/CENSUS-CLOSURES-ch14j.tsv members/r2-ch14j.py \
  members/r2-ch14j.out members/r2-ch14k.py members/r2-ch14k.out
```

It must print **reverse recovers md5 ac1f2310cc19e7fd60686cb90861134a == old: True** before writing;
if it does not, nothing is written and the failure is reported. Then copy BUILD123, HANDOFF-48 and
the READ file to `/mnt/user-data/outputs` and present them. `--append` arguments must precede
`--members`. Note that after a close, `gate.py manifest` reports FAIL on changed members because the
extracted copies stay at pre-close state — verify appends by reading the new bundle directly.
`gate.py bank` refuses to overwrite an existing `.out`; if an instrument is corrected after banking,
delete the golden in a **delete-only** call, then bank again. If r2lib.py is changed to lift the
three functions, it must be passed in `--members` and its new md5 recorded in HANDOFF-48's step 6.

## Drive actions for M

- **Upload** to Materials (`1XX_5f3PZB6tjRtiZ2GIgd8Tt7i_4GgkY`): `HANDOFF-47.md` and
  `The_Method_1_6_BUILD122_compendia_papers_audits.md`.
- **Retire** once BUILD122 gates PASS in chat 95: HANDOFF-46 and BUILD121, plus any earlier
  compendia builds still present (BUILD107–BUILD120).
- **Keep:** BUILD90 main (the live main bundle, unchanged since chat 62), the Prints & Proofs folder
  (`1vYctzLppUZ2vFPJDCZ6wvkgSdj3v_f6n`, the original-input witness per Ruling 56), the certificates,
  OWED-REGISTER-EXPANSIONS.md, OWED-EXPANSIONS-2.md, covers8.json, factor.py.

## Three items needing M's ruling before R3 can move

1. Carried unchanged from chats 90–94 and now **five chats old**: **§14.5.7 is heading-only, zero
   body lines**, and is cited from nine sites including the one §21.5.4's whole construction rests
   on. A production loss and an authoring gap have different repairs and the file cannot tell them
   apart — **Prints & Proofs is where the evidence would be.**
2. Carried from chat 93: **no Register entry carries the one-dimensional refinement of §18.4.1's
   criterion** — *for a bracket on one chain, monotone in either direction suffices; only closure in
   a product requires increasing* (main L5977–L5980). Register 319, which the passage cites, states
   a different claim. Entries are append-only, so this is a missing entry rather than a wrong one,
   and writing it is held by the chat-67 hold until the review closes.
3. New from chat 94, and stated here because the repair is a subject-matter choice rather than an
   editorial one: **§22.5's r and Rule 4's σ cannot both stand as written.** If σ in §22.5 is the
   levels' measured uncertainty, the section is correct and Rule 4's symbol should differ; if it is
   Rule 4's prediction standard error, then r is constant in ν and the admissibility rule states the
   wrong scaling. Only M can say which quantity the admissibility criterion was built on. The same
   ruling governs whether *Every channel eventually leaves the domain* survives.

## Prompt for chat 95

"Chat 95. READ EVERYTHING BEFORE YOU DO ANYTHING. Live files: BUILD90 main (1,983,081 B, md5
49065309b0c4fe8e055f693aed295cca) and BUILD122 compendia (4,746,122 B, md5
ac1f2310cc19e7fd60686cb90861134a, 58,350 lines, 388 members). List uploads, outputs and /home/claude
first. Run HANDOFF-47's §0 gate in full and in order — fetch both bundles by title, bootstrap
(decode, md5, extract, expect 390 files), then gate.py census, run --core, manifest, run r2-ch14h
r2-ch14i, cert 95; any FAIL stops the chat with a report. Read RULINGS-R2.md and DEFERRED.md from
the members; chat 94's DEFERRED block is the last of twenty-two. The standing block's Phase 0–4
(Löwdin/three-body) plan is executed carried state; discard it per Ruling 41 — its discard is W-118,
not W-107. Line numbers are MEMBER line numbers and are never carried between chats: HANDOFF-46
carried eleven boundaries that were each one high, so re-scan every heading on The_Method_1_6-2.md
before reading a line. Then continue Phase R2 under the chat-81 cadence: the section read is Chapter
23, The cost surface, which opens at main L6178 and runs to L6622 — 445 lines, three times any read
yet closed, so scan the headings, confirm every boundary, and take §23.1–§23.2.x as the unit rather
than the chapter. A section read is never split. Read it all, census its claims into computable and
prose, then run exactly two instrument batches, r2-ch14j computable and r2-ch14k prose. Lift
section_span(), has_token() and the appendix-aware enclosing() from r2-ch14i.py into r2lib rather
than copying them a third time; if r2lib changes it must be passed in --members. Chapter 23 is where
two of chat 94's findings resolve — V = w/e at L6183 and V(x,p) = 4x/(h|p−1|) at L6187 — so confirm
them from the chapter rather than re-deriving. Chat 90 settled seed(Λ₈) = 7, chat 91 settled the
star's seed at 6 and Register 1790's thirteen-node Λ₁₃ graph, chat 92 rebuilt the 102-element cover
model as 25 value slots + 77 raising steps, chat 93 settled Chapter 22's Rydberg series as R =
109,737.31568, Z = 1, δ = 0.35, and chat 94 settled δ₂ = 0.06 for §22.4.1 and V = w/e as
limit-free; check any restatement against those rather than re-measuring. Use chat 88's exact-token
heading resolver, not prefix matching, and never span a section by heading rank — the book sets
§25.6 and §25.6.1 at the same ### depth. Grep lowercase 'register NNN' by hand. Check every printed
pair count against C(N, 2). Resolve every pointer to the claim and not the heading, and before
recording any pointer as unresolved read the target section and test for the claim as that section
words it, case-exact and word-bounded. Give every negative claim its own witness, measured
separately. Check the arithmetic of every ratio and percentage; never round with Python's round(),
which is binary — use Decimal.quantize and name the convention. After writing any verdict that
compares two measured numbers, re-read the comparison against the numbers, and when an instrument
disagrees with a hand reading, suspect the instrument first — chat 94 hit that twice. Close the
section read before the next opens. At close: bank both goldens with gate.py bank, write W-133
ending with a blank line, build BUILD123 with close.py (reverse must recover ac1f2310…), write
HANDOFF-48. No corrections, no Register entries, no TASK 1 until the review closes. Handoff at
90–95 % of context or on a closed section read — never earlier, never mid-section. Timeout on every
call. Delete-only calls for pycache, never chained to gate.py bank. Never copy over an existing
file."
