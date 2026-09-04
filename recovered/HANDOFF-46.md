# HANDOFF-46 — The Method 1.6 — chat 93 → chat 94

- Written from **chat 93** for **chat 94**. Live files: **BUILD90 main** (unchanged since chat 62) and
  **BUILD121 compendia** (= BUILD120 + W-131 + chat 93's DEFERRED block + six new members). Register
  **1 to 1792** (unchanged — no Register entry has been written since the chat-67 hold). W-131 IS
  seated; chat 94 seats nothing at open and writes W-132 at close.
- **Rulings and discipline:** the member `RULINGS-R2.md` (6,041 B · 30 lines, unchanged this chat)
  governs and is append-only; **read it at open, last block first** — the chat-81 block sets the
  cadence, and chats 82–93 have all run it. **Deferred cross-chapter items:** `DEFERRED.md`
  (**100,557 B · 578 lines · 21 blocks**, with chat 93's block) governs; do not re-derive. **Findings
  carried to R3:** the READ-chNN.md members (READ-ch14f is chat 93's) and W-101…W-131 in
  WORKING-REGISTER.md; nothing is restated here.
- **Line numbering, so it is not rediscovered a third time.** r2-tools, every prior chat and this
  handoff number main-volume lines on the **member** (`The_Method_1_6-2.md`, 1-based). The *bundle*
  file numbers each line one higher because of its `<<<FILE:` header, so a raw scan of the bundle
  reports Chapter 22 at 5940 where the record says 5939. Read and measure on the member. Chat 93 hit
  this at its heading scan and recorded it in W-131.
- **Carried state to discard (Ruling 41):** the standing prompt block's "Phase 0–4" Löwdin/three-body
  plan is executed carried state; do not re-open it or put it to M. Its discard is recorded in
  **W-118 (chat 81)**, not W-107 — do not reintroduce the W-107 pointer. The absorption itself is
  W-009 / W-059 / W-063 and Registers 1701–1724; subject-matter claims about the three-body count
  resolve to Registers 489 and 507. Project knowledge holds BUILD12/BUILD53 only — list it, never read
  those bundles. Retired handoffs are gone from Drive; never fetch or cite one. Never add
  HANDOFF-NN.md as a member.
- **Known and pre-existing, not introduced by chat 93:** the compendia bundle carries **48 legacy
  `HANDOFF-NN.md` members** (HANDOFF-2 … HANDOFF-53, plus HANDOFF-19-A), identical in BUILD120 and
  BUILD121. Their numbering collides with the current handoff series — a member `HANDOFF-45.md` is
  seated and is **not** the document chat 93 was given. They extract into `members/` harmlessly, but a
  handoff must never be written into `members/` and never passed to `--members`, or a seated member is
  silently overwritten. Flagged for M; no action taken.

## §0 Gate (each step its own tool call under `timeout 280`; any FAIL stops the chat with a report)

1. `ls -la /mnt/user-data/uploads /mnt/user-data/outputs /home/claude`; `recent_chats` confirms the
   latest chat is 93. Read `/mnt/project/CLAUDE.md` (project instruction; never a member).
2. Fetch both bundles by title: `Google Drive:search_files` with
   `title contains 'BUILD121_compendia' or title contains 'BUILD90_main'`, pageSize 5,
   excludeContentSnippets; `Google Drive:download_file_content` on each fileId. Both spill to
   `/mnt/user-data/tool_results/<id>.json`; note the two paths (the gate costs ≈ 13 %, MEASURED).
3. Bootstrap (the only step outside gate.py, because gate.py is a member):

```
timeout 280 python3 - <<'EOF'
import json, base64, hashlib, re, os
EXP={'main':'49065309b0c4fe8e055f693aed295cca','comp':'2e26cf21a6f9726767500b6a5741791b'}
NAME={'main':'/home/claude/The_Method_1_6_BUILD90_main_and_register.md','comp':'/home/claude/The_Method_1_6_BUILD121_compendia_papers_audits.md'}
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
   **4,645,439 B · 2e26cf21a6f9726767500b6a5741791b · 56,862 lines**; **384 members extracted (2 + 382)**.
4. `python3 /home/claude/members/gate.py census` → `OK census: DEFECT-CENSUS.tsv byte-identical`
   (1,556 rows + header, ≈ 11 s).
5. `python3 /home/claude/members/gate.py run --core` → five `OK` (tower 976/1,654/2,535/13,585/70,905/
   199,130; kinds 1565 · 1356 · 499 · 149; minmax; r2-tools-constants; extent "1 to 1792").
6. `python3 /home/claude/members/gate.py manifest` → `MANIFEST OK`; MANIFEST.tsv **25,695 B ·
   414ce1de55e6a8839e45f61c50d0f73d · 384 lines**; WORKING-REGISTER.md **662,802 B ·
   97293b2ee195e7e5554cb0afaffdf206 · 5,746 lines**, ends **W-131**; DEFERRED.md **100,557 B · 578
   lines · md5 882525f5 · 21 blocks**; RULINGS-R2.md 6,041 B · 4cce8039; **r2lib.py 18,486 B ·
   3344ca87 · 396 lines** (unchanged this chat); gate.py 9,377 B · a01ef15a; close.py 6,456 B ·
   98acae67; tower-2.py c0bce27a; census.py f5a73e2b; kinds.py 4262f7c5; minmax.py 26da1d78;
   r2-tools.py 4702f5f9. If two `BUILD*_compendia` files are present after a close, pass
   `--comp <path>` explicitly.
7. `python3 /home/claude/members/gate.py run r2-ch14f r2-ch14g` → two `OK` (chat 93's goldens:
   r2-ch14f.out 7,784 B · 35f7068c · 125 lines, ≈ 0 s; r2-ch14g.out 14,016 B · 436ae11b · 192 lines).
8. `python3 /home/claude/members/gate.py cert 94` → writes `/home/claude/GATE-ch94.txt`, verdict PASS
   only if every logged step passed. A FAIL anywhere stops the chat and is reported, not worked around.

## What chat 93 did (do not repeat)

Chapter 22's opening read whole — main **L5937–L6035, 99 lines, five headings** (PART V, ch 22, §22.1,
§22.1.1, §22.1.1.1, §22.1.2) — every boundary measured before a line was read. **Four deviations,
thirteen verified, nine incidentals, three census rows closed** (702, 1132, 1133, all *not a defect*,
C7/C9 regex artefacts) in `READ-ch14f.md` and `CENSUS-CLOSURES-ch14f.tsv`.

The load-bearing finding is a **standard the book sets and then misses**: §22.1.1.1 claims *F.3's
highest standard* while naming three of F.3's four columns — the method, the input set, the inputs —
and putting its four-defect recomputation where **the refutation** belongs. F.3 (L11278–L11300) states
in its own words that a statement carrying fewer than four *is a different kind of object*, and
`refut` appears nowhere in the ninety-nine lines. One subsection later the same standard breaks the
other way: §22.1.2's seven widths are reproducible only at **δ = 0.35**, which the section never
prints, and §22.1.1's *N ≈ √(M/m)* needs an **M** it never prints (it solves to the deuteron mass).
Second: **L5983 and L6004 attribute a single run to §22.1**, whose nine body lines carry two digits,
no defect, no energy and no count. Third: **Register 319 is cited one paragraph late** — 0 of 6 topic
tokens against the paragraph it is attached to, while stating that section's *other* claim nearly
verbatim. Fourth: **918 ÷ 207, both printed in the same sentence, is 4.43**, not the printed 4.44,
which needs the unrounded muon mass. Full detail is in READ-ch14f.md and W-131; do not re-measure any
of it.

Everything the chapter computes reproduces: the containment table exactly at all four defects
including all eight energy extremes, 36 of 36, seven interior held at every defect, the seven widths
at δ = 0.35 with maximum deviation 0.0, all six ratios, the true next width 281.7474, the presumed
274.10, and **the printed 2.72 % as 2.715 % against the true width** — exact to the printed precision.
The ν⁻³ ratio 0.7640 → 0.764. Note for any later touch of this material: the law-derived presumption
is **9.3× more accurate** than the pattern-derived one (0.29 % against 2.72 %), which the book does
not claim and which supports its argument.

**Chat 93's own errors, carried as method.** Four instrument faults, all rewritten rather than
trimmed. The one that matters: F11's verdict printed *LARGER* comparing 0.29 % with 2.72 % and
concluded the book's argument was undercut — the arithmetic was right and the sentence built on it
inverted it, which is chat 92's inverted-verdict class in a new form. G8's summary generalised over
nineteen sites before classifying them and described eleven unrelated ones as records of this section;
rewriting it is what produced the §33.4 twin finding. F3 printed a bare `CHECK` without naming which
half of a compound condition failed, and F6 asserted a reading it had never measured.

## Chat 94's section read — Chapter 22 remainder, *The four rules* onward

MEASURED by heading scan in chat 93: **§22.2 L6036**, §22.2.1 L6056, §22.2.2 L6071, §22.2.3 L6087,
§22.2.4 L6101, §22.2.5 L6107, §22.3 L6129, §22.4 L6138, §22.4.1 L6148, §22.5 L6168, §22.6 L6175;
the chapter ends **L6178** and Chapter 23 opens L6179. That is **143 lines, eleven headings** —
larger than chats 90/92/93 closed (93, 63, 99). Scan the headings forward again and confirm every
boundary before reading a line, then take as much as will close in one chat: **§22.2–§22.2.5
(L6036–L6128, 93 lines) is the natural unit**, with §22.3–§22.6 (L6129–L6178, 50 lines) left to chat
95, or take the whole chapter if the census looks light after the read. A section read is never split
across chats.

Instruments: **r2-ch14h** (computable) and **r2-ch14i** (prose). Use chat 88's exact-token heading
resolver, never prefix matching. Grep lowercase `register NNN` by hand; r2-tools' pointer regex is
case-sensitive. Check every printed pair count against C(N, 2), this volume's convention. Resolve
every pointer to the claim and not the heading; before recording any pointer as unresolved, read the
target section and test for the claim **as that section words it**, case-exact and word-bounded
(chat 92). Measure a claim and its stated witness separately; check the arithmetic of every ratio and
percentage; where the text prints a sample, measure the population; read a section's *What survives*
block as well as its *What this withdraws* block; grep the Register for a later entry naming the
section before recording any figure as unreproducible (chat 91); and — **new, from chat 93's own
errors** — **after writing any verdict that compares two measured numbers, re-read the comparison
against the numbers**, and never write a summary line that generalises over a list before the list is
printed.

Chapter 22 is arithmetic on a Rydberg series and pointer resolution, with no tower computation at all;
r2-ch14f imports no r2lib and §22.2's ablation is likely the same. Expect **§22.2.1's ablation table**
and **§22.2.3's one-step-beyond cost** to be the computable core, and §22.3's *limit-free* claim with
§22.4's *price of limit-freedom* to be where the prose batch sits. Note that §22.2.4 (*Rule 1's second
clause is not redundant*) and §22.2.2 (*Rule 1 is not about n*) are both negative claims, which need a
witness each, measured separately from the claim.

## Close (chat 94)

`gate.py bank r2-ch14h r2-ch14i`; delete pycache in its own delete-only call; write `W-132.md`
(begins `### W-`, **ends with a blank line** — close.py asserts this); append a DEFERRED block as
`DEF-94.md`; then

```
timeout 280 python3 members/close.py --old The_Method_1_6_BUILD121_compendia_papers_audits.md \
  --new The_Method_1_6_BUILD122_compendia_papers_audits.md --w W-132.md \
  --main The_Method_1_6_BUILD90_main_and_register.md --append DEFERRED.md DEF-94.md \
  --members members/READ-ch14h.md members/CENSUS-CLOSURES-ch14h.tsv members/r2-ch14h.py \
  members/r2-ch14h.out members/r2-ch14i.py members/r2-ch14i.out
```

It must print **reverse recovers md5 2e26cf21a6f9726767500b6a5741791b == old: True** before writing;
if it does not, nothing is written and the failure is reported. Then copy BUILD122, HANDOFF-47 and
the READ file to `/mnt/user-data/outputs` and present them. `--append` arguments must precede
`--members`. Note that after a close, `gate.py manifest` reports FAIL on changed members because the
extracted copies stay at pre-close state — verify appends by reading the new bundle directly.
`gate.py bank` refuses to overwrite an existing `.out`; if an instrument is corrected after banking,
delete the golden in a **delete-only** call, then bank again.

## Drive actions for M

- **Upload** to Materials (`1XX_5f3PZB6tjRtiZ2GIgd8Tt7i_4GgkY`): `HANDOFF-46.md` and
  `The_Method_1_6_BUILD121_compendia_papers_audits.md`.
- **Retire** once BUILD121 gates PASS in chat 94: HANDOFF-45 and BUILD120, plus any earlier compendia
  builds still present (BUILD107–BUILD119).
- **Keep:** BUILD90 main (the live main bundle, unchanged since chat 62), the Prints & Proofs folder
  (`1vYctzLppUZ2vFPJDCZ6wvkgSdj3v_f6n`, the original-input witness per Ruling 56), the certificates,
  OWED-REGISTER-EXPANSIONS.md, OWED-EXPANSIONS-2.md, covers8.json, factor.py.

## Two items needing M's ruling before R3 can move

1. Carried unchanged from chats 90–93 and now **four chats old**: **§14.5.7 is heading-only, zero body
   lines**, and is cited from nine sites including the one §21.5.4's whole construction rests on. A
   production loss and an authoring gap have different repairs and the file cannot tell them apart —
   **Prints & Proofs is where the evidence would be.**
2. New from chat 93, and stated here because it is a subject-matter gap rather than an editorial one:
   **no Register entry carries the one-dimensional refinement of §18.4.1's criterion** — *for a bracket
   on one chain, monotone in either direction suffices; only closure in a product requires increasing*
   (main L5977–L5980). Register 319, which the passage cites, states a different claim. Entries are
   append-only, so this is a missing entry rather than a wrong one, and writing it is held by the
   chat-67 hold until the review closes. Recorded now so R3 does not read the gap as a citation error.

## Prompt for chat 94

"Chat 94. READ EVERYTHING BEFORE YOU DO ANYTHING. Live files: BUILD90 main (1,983,081 B, md5
49065309b0c4fe8e055f693aed295cca) and BUILD121 compendia (4,645,439 B, md5
2e26cf21a6f9726767500b6a5741791b, 56,862 lines, 382 members). List uploads, outputs and /home/claude
first. Run HANDOFF-46's §0 gate in full and in order — fetch both bundles by title, bootstrap (decode,
md5, extract, expect 384 files), then gate.py census, run --core, manifest, run r2-ch14f r2-ch14g,
cert 94; any FAIL stops the chat with a report. Read RULINGS-R2.md and DEFERRED.md from the members;
chat 93's DEFERRED block is the last of twenty-one. The standing block's Phase 0–4 (Löwdin/three-body)
plan is executed carried state; discard it per Ruling 41 — its discard is W-118, not W-107. Line
numbers are MEMBER line numbers: the bundle file is one higher because of its FILE header, so measure
on The_Method_1_6-2.md. Then continue Phase R2 under the chat-81 cadence: the section read is the
Chapter 22 remainder from main L6036 (§22.2 L6036, §22.2.1 L6056, §22.2.2 L6071, §22.2.3 L6087,
§22.2.4 L6101, §22.2.5 L6107, §22.3 L6129, §22.4 L6138, §22.4.1 L6148, §22.5 L6168, §22.6 L6175,
chapter ends L6178). Scan the headings forward and confirm every boundary before reading a line;
§22.2–§22.2.5 (93 lines) is the natural unit and §22.3–§22.6 can follow if the census is light. Read it
all, census its claims into computable and prose, then run exactly two instrument batches, r2-ch14h
computable and r2-ch14i prose. Chapter 22 needs no tower computation — chat 93's computable batch
imports no r2lib. Chat 90 settled seed(Λ₈) = 7, chat 91 settled the star's seed at 6 and Register
1790's thirteen-node Λ₁₃ graph, chat 92 rebuilt the 102-element cover model as 25 value slots + 77
raising steps, and chat 93 settled Chapter 22's Rydberg series as R = 109,737.31568, Z = 1, δ = 0.35
for §22.1.2's widths; check any restatement against those rather than re-measuring. Use chat 88's
exact-token heading resolver, not prefix matching; grep lowercase 'register NNN' by hand. Check every
printed pair count against C(N, 2). Resolve every pointer to the claim and not the heading, and before
recording any pointer as unresolved read the target section and test for the claim as that section
words it, case-exact and word-bounded. Give every negative claim its own witness, measured separately.
Check the arithmetic of every ratio and percentage as well as every count; where the text prints a
sample, measure the population; and grep the Register for a later entry naming the section before
recording any figure as unreproducible. After writing any verdict that compares two measured numbers,
re-read the comparison against the numbers — chat 93 inverted one — and never write a summary line
that generalises over a list before the list is printed. Close the section read before the next opens.
At close: bank both goldens with gate.py bank, write W-132 ending with a blank line, build BUILD122
with close.py (reverse must recover 2e26cf21…), write HANDOFF-47. No corrections, no Register entries,
no TASK 1 until the review closes. Handoff at 90–95 % of context or on a closed section read — never
earlier, never mid-section. Timeout on every call. Delete-only calls for pycache, never chained to
gate.py bank. Never copy over an existing file."
