# HANDOFF-51 — The Method 1.6 — chat 98 → chat 99

- Written from **chat 98** for **chat 99**. Live files: **BUILD90 main** (unchanged since chat 62)
  and **BUILD127 compendia** (= BUILD126 + W-137 + DEF-98 + six new members). Register **1 to 1792**
  (unchanged — no Register entry since the chat-67 hold). W-137 IS seated; chat 99 seats nothing at
  open and writes W-138 at close.
- **Read RULINGS-R2.md at open, last block first.** The chat-95 block still governs and is still the
  last: **a finding is not a question.** A deviation in the mathematics or in the prose is recorded
  and **flagged for repair**, never put to M. **Prints & Proofs is read before any question is
  asked**, not after. Only a choice no file can settle reaches M. The chat-81 block below it sets the
  cadence and is unchanged.
- **Chapter 23 is closed.** Four reads, chats 95–98, main L6178–L6622. Chat 99 opens **Chapter 24**.
- **The chat-97 gate fault does not recur and must not be re-introduced.** Chat 98's `r2-ch14p` and
  `r2-ch14q` read the six volume **members** by name and reproduced at their own bank. **Never write
  an instrument that opens a `BUILDnnn` path** — the name changes every chat and the bundle comes to
  contain the instrument's own banked output.
- **Correcting a banked golden works, and chat 98 did it.** Two faults landed after `r2-ch14p` was
  banked; `r2-ch14p.out` was removed in a **delete-only** call and re-banked. `gate.py bank` refuses
  to overwrite, so that is the only route. The golden in BUILD127 is the corrected one
  (15,920 B · `fee8fd64`).
- **Line numbering.** Main-volume lines are numbered on the **member** (`The_Method_1_6-2.md`,
  1-based); the bundle numbers each line one higher because of its `<<<FILE:` header. Chat 98
  re-scanned §23.12–§23.15 and found HANDOFF-50's boundaries exact — which is not a reason to carry
  the next set. Re-scan.
- **Carried state to discard (Ruling 41):** the standing prompt block's "Phase 0–4"
  Löwdin/three-body plan is executed carried state; do not re-open it or put it to M. Its discard is
  **W-118 (chat 81)**, not W-107. The absorption is W-009 / W-059 / W-063 and Registers 1701–1724;
  three-body count claims resolve to Registers 489 and 507. Project knowledge holds BUILD12/BUILD53
  only — list it, never read those bundles. Retired handoffs are gone from Drive; never fetch or cite
  one. **Never add HANDOFF-NN.md as a member.**
- **Known and pre-existing:** the compendia bundle carries **48 legacy `HANDOFF-NN.md` members**,
  identical in BUILD122–127. They extract into `members/` harmlessly, but a handoff must never be
  written into `members/` or passed to `--members`, or a seated member is silently overwritten.
- **Findings carried to R3:** the READ-chNN.md members (READ-ch14p is chat 98's) and W-101…W-137 in
  WORKING-REGISTER.md; nothing is restated here. **Deferred cross-chapter items:** `DEFERRED.md`
  (**136,458 B · `1ad0d7c5` · 27 blocks**, chat 98's is the last) governs; do not re-derive.

## §0 Gate (each step its own tool call under `timeout 280`; any FAIL stops the chat with a report)

1. `ls -la /mnt/user-data/uploads /mnt/user-data/outputs /home/claude`; `recent_chats` confirms the
   latest chat is 98. Read `/mnt/project/CLAUDE.md` (project instruction; never a member).
2. Fetch both bundles by title: `Google Drive:search_files` with
   `title contains 'BUILD127_compendia' or title contains 'BUILD90_main'`, pageSize 5,
   excludeContentSnippets; `Google Drive:download_file_content` on each fileId. Both spill to
   `/mnt/user-data/tool_results/<id>.json`; note the two paths. MEASURED cost of the gate in chat 98:
   ≈ 17 % of context, against chat 97's ≈ 25 % (which carried a third fetch).
3. Bootstrap (the only step outside gate.py, because gate.py is a member):

```
timeout 280 python3 - <<'EOF'
import json, base64, hashlib, re, os
EXP={'main':'49065309b0c4fe8e055f693aed295cca','comp':'4dceeceede860686704b4f07f793f5db'}
NAME={'main':'/home/claude/The_Method_1_6_BUILD90_main_and_register.md','comp':'/home/claude/The_Method_1_6_BUILD127_compendia_papers_audits.md'}
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
   **5,125,193 B · 4dceeceede860686704b4f07f793f5db · 63,510 lines**; **414 members extracted
   (2 + 412)**.
4. `python3 /home/claude/members/gate.py census` → `OK census: DEFECT-CENSUS.tsv byte-identical`
   (1,556 rows + header, ≈ 15 s).
5. `python3 /home/claude/members/gate.py run --core` → five `OK` (tower 976/1,654/2,535/13,585/
   70,905/199,130; kinds 1565 · 1356 · 499 · 149; minmax; r2-tools-constants; extent "1 to 1792").
6. `python3 /home/claude/members/gate.py manifest` → `MANIFEST OK`; MANIFEST.tsv **27,710 B ·
   390c77236c459eda38ef94fc945c257c · 414 lines**; WORKING-REGISTER.md **696,698 B ·
   71f9745af1a6dc40c0f1f5c9152a7dd2 · 6,123 lines**, ends **W-137**; DEFERRED.md **136,458 B ·
   1ad0d7c5 · 27 blocks**; RULINGS-R2.md 9,844 B · 10a2ea7e · 82 lines (unchanged); r2lib.py
   21,022 B · 580d2ea2 · 453 lines (unchanged); gate.py 9,377 B · a01ef15a; close.py 6,456 B ·
   98acae67; r2-tools.py 6,529 B · 4702f5f9; tower-2.py c0bce27a; census.py f5a73e2b; kinds.py
   4262f7c5; minmax.py 26da1d78. If two `BUILD*_compendia` files are present after a close, pass
   `--comp <path>` explicitly.
7. `python3 /home/claude/members/gate.py run r2-ch14p r2-ch14q` → two `OK` (chat 98's goldens:
   r2-ch14p.out 15,920 B · fee8fd64 · 167 lines; r2-ch14q.out 12,769 B · 88b2d69d · 115 lines). Both
   import the lifted r2lib and read members only; an AttributeError means the extraction seated a
   pre-lift r2lib and the chat stops.
8. `python3 /home/claude/members/gate.py cert 99` → writes `/home/claude/GATE-ch99.txt`, verdict PASS
   only if every logged step passed. A FAIL anywhere stops the chat and is reported.

## What chat 98 did (do not repeat)

**§23.12–§23.15 is closed, and with it Chapter 23** — main **L6549–L6622, 74 lines, five headings**,
boundaries re-scanned and confirmed. **Eleven deviations, twenty verified, seven incidentals, one
census row closed** (row 1138, a C9 artefact — "never creates an interior peak" is §23.12's own
scoped rule). All of it is in `READ-ch14p.md` and `CENSUS-CLOSURES-ch14p.tsv`; **do not re-measure
any of it.**

**The four findings that carry furthest:**

- **14p-19 — the main volume and the Spectra Compendium disagree about the compendium's own rows.**
  §23.15's "ν reached" column: Al I *n*f 55.0 is exact; **Na I *n*s** is printed at 20.0 where its row
  reaches **18.7** (20.0 belongs to *n*d, *n*f, *n*g); **K I *n*d** is printed at **45.7** where the
  nd row reaches 12.7 and no K I channel passes 15.8. The K I row cannot be a sibling-channel slip,
  so at least one figure points outside the six volumes. **The first main-volume/compendium
  contradiction of the phase**; DEFERRED's chat-98 block sets the sweep.
< truncated lines 105-215 >
10. **The 32/11 scope docket** (14j-01), with six measured main-volume sites — L6193, L6213, L6233,
    L6237, L6381, L10245 — plus 2.909 at four. L6381 claims the floor as an original result and must
    be repaired **after** the scope decision, not with it.
11. **The truncation-printed-as-equality class** (14l-02, 14l-03, 14n-A10) — sweep every display
    equation whose own table disagrees with it, and every site printing 4ν/3.
12. **The two unsourced counts of L6517** (14n-A6, 14n-A7) — *619 refusals* and *§25.5's 1,061
    order-1 bounds*. Neither can be repaired without **recomputing the collection at matched order**;
    the phase's first item needing a recomputation rather than a corrected figure. **Note chat 98's
    14p-17**: two counts that looked unsourced were recovered from the Spectra Compendium's channel
    table, so try that table before scheduling the recomputation.
13. **The main-volume/Spectra contradiction class** (14p-19) — new, and the sweep is stated in
    DEFERRED's chat-98 block: every figure the main volume attributes to a named channel, against
    that channel's compendium row. Resolve **K I *n*d 45.7** first; it decides whether the class is a
    table defect or a short compendium.
14. **The Nesterov name-form sweep** (14m-07) — five forms in five places, one substantive (L8052
    credits Nesterov alone for a result §23.8.1 credits to both).
15. **The single-witness class** — six of twelve distinctive figures in chat 98's 74 lines, fourteen
    in chat 97's 115, seventeen in chat 96's 131, thirteen in chat 95's 125. R4 should state which
    figures are unverifiable rather than leaving them looking checked, and distinguish *unverifiable*
    from *uncorroborated*.
16. **Heading sentences finishing in the body** (14q-06) — L4407, L6582, L6634, L8659. Read all four
    before repairing any; L6634 is a table header, not a sentence.

## Close (chat 99)

`gate.py bank r2-ch14r r2-ch14s`; delete pycache in its own delete-only call; write `W-138.md`
(begins `### W-`, **ends with a blank line** — close.py asserts this); append a DEFERRED block as
`DEF-99.md`; then

```
timeout 280 python3 members/close.py --old The_Method_1_6_BUILD127_compendia_papers_audits.md \
  --new The_Method_1_6_BUILD128_compendia_papers_audits.md --w W-138.md \
  --main The_Method_1_6_BUILD90_main_and_register.md --append DEFERRED.md DEF-99.md \
  --members members/READ-ch14r.md members/CENSUS-CLOSURES-ch14r.tsv members/r2-ch14r.py \
  members/r2-ch14r.out members/r2-ch14s.py members/r2-ch14s.out
```

It must print **reverse recovers md5 4dceeceede860686704b4f07f793f5db == old: True** before writing;
if it does not, nothing is written and the failure is reported. `--append` arguments must precede
`--members`, and `--members` may be omitted entirely if nothing new is seated. **A changed
append-only member is grown with `--append <member> <delta-file>`, never passed to `--members`** —
close.py refuses a name collision, and a member needing *replacement* rather than growth has no
mechanism at all. After a close, `gate.py manifest` reports FAIL on changed members because the
extracted copies stay at pre-close state; **verify appends by reading the new bundle directly** —
and note the Register member lives in the **main** bundle, not the compendia bundle. `gate.py bank`
refuses to overwrite an existing `.out`; correcting an instrument after banking needs a
**delete-only** call to remove the golden, then bank again (chat 98 did this and it works). Then copy
BUILD128, HANDOFF-52 and the READ file to `/mnt/user-data/outputs` and present them.

## Drive actions for M

- **Upload** to Materials (`1XX_5f3PZB6tjRtiZ2GIgd8Tt7i_4GgkY`): `HANDOFF-51.md` and
  `The_Method_1_6_BUILD127_compendia_papers_audits.md`.
- **Retire** once BUILD127 gates PASS in chat 99: HANDOFF-50 and BUILD126, plus any earlier compendia
  builds still present (BUILD107–BUILD125).
- **Keep BUILD124** for now — it is the only input under which chat 96's `r2-ch14l` and `r2-ch14m`
  reproduce, and §23.9.1's eight exact V values live in `r2-ch14l.out`. Chat 98 read those values out
  of the **member** rather than re-running the instrument, which is the pattern R3 should adopt
  before BUILD124 is retired.
- **Keep:** BUILD90 main (unchanged since chat 62), the **Prints & Proofs** folder
  (`1vYctzLppUZ2vFPJDCZ6wvkgSdj3v_f6n`) — the authentication baseline under Ruling 56 — the
  certificates, OWED-REGISTER-EXPANSIONS.md, OWED-EXPANSIONS-2.md, covers8.json, factor.py.

## Prompt for chat 99

"Chat 99. READ EVERYTHING BEFORE YOU DO ANYTHING. Live files: BUILD90 main (1,983,081 B, md5
49065309b0c4fe8e055f693aed295cca) and BUILD127 compendia (5,125,193 B, md5
4dceeceede860686704b4f07f793f5db, 63,510 lines, 412 members). List uploads, outputs and /home/claude
first. Run HANDOFF-51's §0 gate in full and in order — fetch both bundles by title, bootstrap
(decode, md5, extract, expect 414 files), then gate.py census, run --core, manifest, run r2-ch14p
r2-ch14q, cert 99; any FAIL stops the chat with a report. Read RULINGS-R2.md last block first: the
chat-95 block governs and it says a finding is not a question — deviations in the mathematics and in
the prose are recorded and flagged for repair, never put to M, and Prints & Proofs is read before any
question is asked. Do not ask M to rule on a defect. Read DEFERRED.md; chat 98's block is the last of
twenty-seven. The standing block's Phase 0–4 Löwdin/three-body plan is executed carried state;
discard it per Ruling 41 — its discard is W-118, not W-107. Line numbers are MEMBER line numbers and
are never carried between chats, and neither is any count: re-scan every heading on
The_Method_1_6-2.md before reading a line. Chapter 23 closed in chat 98. Then continue Phase R2 under
the chat-81 cadence: Chapter 24 runs L6623–L6883, fourteen headings, too large for one read — take
§24 through §24.7, main L6623–L6740, 118 lines, eight headings, and decide the cut before reading.
Read it all, census its claims into computable and prose, then run exactly two instrument batches,
r2-ch14r computable and r2-ch14s prose, importing heading_line, section_span, has_token and enclosing
from r2lib — copy nothing, pass them the LINE LIST and not the member text, and read the six volume
MEMBERS, never a BUILDnnn bundle path. Chat 98 measured that the Spectra Compendium's channel table
(477 rows: species, channel, n range, members, usable, fit, ν range, δ̄, spread, Z, limit) settles
cell counts and ν ranges exactly, and that §23.15's ν-reached column disagrees with it in two of
three rows — so measure every count and every ν this chapter attributes to a named species against
that species' compendium rows, and resolve K I nd 45.7 if the chapter touches it. Where the text
prints a sample, measure the population. Use the exact-token heading resolver, never prefix matching,
and never span a section by heading rank. Grep lowercase 'register NNN' by hand. Resolve every
pointer to the claim and not the heading, and if it fails at the named target grep the whole volume
before recording it. Give every negative claim its own witness, and state what a sweep covered before
recording a negative from it. A number beside a species is not that species' ceiling — read the
header. ν is not n. Never round with Python's round() — use Decimal.quantize and name the convention.
A heading is not a statement, a bound is not a measurement, a boundary case is not a violation.
Re-read every verdict against the numbers printed above it AND below it. When an instrument disagrees
with a hand reading, suspect the instrument first. Close the section read before the next opens. At
close: bank both goldens with gate.py bank, write W-138 ending with a blank line, build BUILD128 with
close.py (reverse must recover 4dceecee…), write HANDOFF-52. A changed append-only member is grown
with --append, never --members; correcting a banked golden needs a delete-only call first. No
corrections, no Register entries, no TASK 1 until the review closes. Handoff at 90–95 % of context or
on a closed section read — never earlier, never mid-section. Timeout on every call. Delete-only calls
for pycache, never chained to gate.py bank. Never copy over an existing file."
