# HANDOFF-50 — The Method 1.6 — chat 97 → chat 98

- Written from **chat 97** for **chat 98**. Live files: **BUILD90 main** (unchanged since chat 62)
  and **BUILD126 compendia** (= BUILD125 + W-136 + DEF-97 + six new members). Register **1 to 1792**
  (unchanged — no Register entry since the chat-67 hold). W-136 IS seated; chat 98 seats nothing at
  open and writes W-137 at close.
- **Read RULINGS-R2.md at open, last block first.** The chat-95 block still governs and is still the
  last: **a finding is not a question.** A deviation in the mathematics or in the prose is recorded
  and **flagged for repair**, never put to M. **Prints & Proofs is read before any question is
  asked**, not after. Only a choice no file can settle reaches M. The chat-81 block below it sets
  the cadence and is unchanged.
- **The count correction is now recorded and closed.** W-135 and DEF-96 said the Chapter 23
  remainder was *189 lines, fifteen headings*; it is **189 lines, thirteen**. Chat 97 re-scanned,
  confirmed thirteen, and recorded the correction in **W-136 citing W-135**. Nothing further is owed
  on it. The rule that caught it is the re-scan: **never carry a count forward, including one
  written ten minutes ago.**
- **A gate step failed in chat 97 and the repair is already applied.** Chat 96's `r2-ch14l` and
  `r2-ch14m` open `/home/claude/The_Method_1_6_BUILD124_compendia_papers_audits.md` **by name** and
  both died at chat 97's gate. Chat 97 fetched BUILD124, md5-asserted it, and both goldens
  reproduced byte-identically, so nothing they recorded is in doubt; `GATE-ch97.txt` carries ERROR
  then OK for each and certifies PASS, the later line governing. **Chat 98's gate does not hit
  this**: its step 7 runs `r2-ch14n` and `r2-ch14o`, which read the six volume **members** by name
  and never a bundle. **Never write an instrument that reads a `BUILDnnn` path** — the name changes
  every chat, and the bundle comes to contain the instrument's own banked output, so a whole-bundle
  census cannot reproduce even under a corrected path.
- **Line numbering.** Main-volume lines are numbered on the **member** (`The_Method_1_6-2.md`,
  1-based); the bundle numbers each line one higher because of its `<<<FILE:` header. Chat 97
  re-scanned the whole Chapter 23 tail before reading and found HANDOFF-49's boundaries exact.
- **Carried state to discard (Ruling 41):** the standing prompt block's "Phase 0–4"
  Löwdin/three-body plan is executed carried state; do not re-open it or put it to M. Its discard is
  **W-118 (chat 81)**, not W-107. The absorption is W-009 / W-059 / W-063 and Registers 1701–1724;
  three-body count claims resolve to Registers 489 and 507. Project knowledge holds BUILD12/BUILD53
  only — list it, never read those bundles. Retired handoffs are gone from Drive; never fetch or
  cite one. **Never add HANDOFF-NN.md as a member.**
- **Known and pre-existing:** the compendia bundle carries **48 legacy `HANDOFF-NN.md` members**,
  identical in BUILD122–126. They extract into `members/` harmlessly, but a handoff must never be
  written into `members/` or passed to `--members`, or a seated member is silently overwritten.
- **Findings carried to R3:** the READ-chNN.md members (READ-ch14n is chat 97's) and W-101…W-136 in
  WORKING-REGISTER.md; nothing is restated here. **Deferred cross-chapter items:** `DEFERRED.md`
  (**130,567 B · 26 blocks**, chat 97's is the last) governs; do not re-derive.

## §0 Gate (each step its own tool call under `timeout 280`; any FAIL stops the chat with a report)

1. `ls -la /mnt/user-data/uploads /mnt/user-data/outputs /home/claude`; `recent_chats` confirms the
   latest chat is 97. Read `/mnt/project/CLAUDE.md` (project instruction; never a member).
2. Fetch both bundles by title: `Google Drive:search_files` with
   `title contains 'BUILD126_compendia' or title contains 'BUILD90_main'`, pageSize 5,
   excludeContentSnippets; `Google Drive:download_file_content` on each fileId. Both spill to
   `/mnt/user-data/tool_results/<id>.json`; note the two paths. The gate cost chat 97 ≈ 25 %
   MEASURED, against ≈ 18 % for chats 95–96 — the difference is the third fetch (BUILD124) that
   step 7's failure forced. Chat 98 should be back near 18 %.
3. Bootstrap (the only step outside gate.py, because gate.py is a member):

```
timeout 280 python3 - <<'EOF'
import json, base64, hashlib, re, os
EXP={'main':'49065309b0c4fe8e055f693aed295cca','comp':'8a43b95743867e3e41bc24c08ecc3db6'}
NAME={'main':'/home/claude/The_Method_1_6_BUILD90_main_and_register.md','comp':'/home/claude/The_Method_1_6_BUILD126_compendia_papers_audits.md'}
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
   **5,038,070 B · 8a43b95743867e3e41bc24c08ecc3db6 · 62,386 lines**; **408 members extracted
   (2 + 406)**.
4. `python3 /home/claude/members/gate.py census` → `OK census: DEFECT-CENSUS.tsv byte-identical`
   (1,556 rows + header, ≈ 15 s).
5. `python3 /home/claude/members/gate.py run --core` → five `OK` (tower 976/1,654/2,535/13,585/
   70,905/199,130; kinds 1565 · 1356 · 499 · 149; minmax; r2-tools-constants; extent "1 to 1792").
6. `python3 /home/claude/members/gate.py manifest` → `MANIFEST OK`; MANIFEST.tsv **27,306 B ·
   525c9da9ab87ddd0c9f1be3af168c8d1 · 408 lines**; WORKING-REGISTER.md **692,320 B ·
   c1f12ad94ae0eb7f55c6bed5251deaa7 · 6,065 lines**, ends **W-136**; DEFERRED.md **130,567 B · 26
   blocks**; RULINGS-R2.md 9,844 B · 10a2ea7ebdf2cc3ca8761bc3cb8d61a6 · 82 lines (unchanged);
   r2lib.py 21,022 B · 580d2ea2e43c2ddf78018afcba2f7de7 · 453 lines (unchanged); gate.py 9,377 B ·
   a01ef15a; close.py 6,456 B · 98acae67; tower-2.py c0bce27a; census.py f5a73e2b; kinds.py 4262f7c5;
   minmax.py 26da1d78; r2-tools.py 4702f5f9. If two `BUILD*_compendia` files are present after a
   close, pass `--comp <path>` explicitly.
7. `python3 /home/claude/members/gate.py run r2-ch14n r2-ch14o` → two `OK` (chat 97's goldens:
   r2-ch14n.out 5,540 B · 0259aeae · 49 lines; r2-ch14o.out 9,247 B · 9923bc2d · 89 lines). Both
   import the lifted r2lib and read members only; an AttributeError means the extraction seated a
   pre-lift r2lib and the chat stops.
8. `python3 /home/claude/members/gate.py cert 98` → writes `/home/claude/GATE-ch98.txt`, verdict
   PASS only if every logged step passed. A FAIL anywhere stops the chat and is reported.

## What chat 97 did (do not repeat)

**§23.10–§23.11.2 is closed** — main **L6434–L6548, 115 lines, eight headings**, the break point
HANDOFF-49 proposed, boundaries re-scanned and confirmed. **Fourteen deviations, fourteen verified,
nine incidentals, one census row closed** (row 1137, a C9 artefact — "never of one cell" is the
section's own scoped rule). All of it is in `READ-ch14n.md` and `CENSUS-CLOSURES-ch14n.tsv`; **do
not re-measure any of it.**

**The three findings that carry furthest:**

< truncated lines 104-209 >
   volumes against the claim rather than the heading**; `enclosing` makes the test cheap: find the
   claim's sites, resolve each to its section, compare with the section cited.
9. **The unprinted-input class, now nine members** — §22.1.2 needs δ = 0.35; §22.4.1 needs
   δ₂ = 0.06; L6060's 446×, L6068's 1,577, L6093's 3.47 %, L6104's *factor of 17*; §23.1 L6189's
   *agreement under 1 %*; §23.9.3's two columns (the one member reproducing under nothing at all);
   and **§23.10.3's displacement row** (14n-A13), which reproduces exactly once the definition is
   supplied.
10. **The 32/11 scope docket** (14j-01), with six measured main-volume sites — L6193, L6213, L6233,
    L6237, L6381, L10245 — plus 2.909 at four. L6381 claims the floor as an original result and must
    be repaired **after** the scope decision, not with it.
11. **The truncation-printed-as-equality class** (14l-02, 14l-03, now 14n-A10) — sweep every display
    equation whose own table disagrees with it, and every site printing 4ν/3.
12. **The two unsourced counts of L6517** (14n-A6, 14n-A7) — *619 refusals* and *§25.5's 1,061
    order-1 bounds*. Neither can be repaired without **recomputing the collection at matched order**;
    this is the phase's first item needing a recomputation rather than a corrected figure, and it
    should be sized before it is scheduled.
13. **The Nesterov name-form sweep** (14m-07) — five forms in five places, one substantive (L8052
    credits Nesterov alone for a result §23.8.1 credits to both).
14. **The single-witness class** — fourteen figures in chat 97's 115 lines, seventeen in chat 96's
    131, thirteen in chat 95's 125. R4 should state which figures are unverifiable rather than
    leaving them looking checked, and distinguish *unverifiable* from *uncorroborated*.

## Close (chat 98)

`gate.py bank r2-ch14p r2-ch14q`; delete pycache in its own delete-only call; write `W-137.md`
(begins `### W-`, **ends with a blank line** — close.py asserts this); append a DEFERRED block as
`DEF-98.md`; then

```
timeout 280 python3 members/close.py --old The_Method_1_6_BUILD126_compendia_papers_audits.md \
  --new The_Method_1_6_BUILD127_compendia_papers_audits.md --w W-137.md \
  --main The_Method_1_6_BUILD90_main_and_register.md --append DEFERRED.md DEF-98.md \
  --members members/READ-ch14p.md members/CENSUS-CLOSURES-ch14p.tsv members/r2-ch14p.py \
  members/r2-ch14p.out members/r2-ch14q.py members/r2-ch14q.out
```

It must print **reverse recovers md5 8a43b95743867e3e41bc24c08ecc3db6 == old: True** before writing;
if it does not, nothing is written and the failure is reported. `--append` arguments must precede
`--members`, and `--members` may be omitted entirely if nothing new is seated. **A changed
append-only member is grown with `--append <member> <delta-file>`, never passed to `--members`** —
close.py refuses a name collision, and a member needing *replacement* rather than growth has no
mechanism at all. After a close, `gate.py manifest` reports FAIL on changed members because the
extracted copies stay at pre-close state; **verify appends by reading the new bundle directly.**
`gate.py bank` refuses to overwrite an existing `.out`; correcting an instrument after banking needs
a **delete-only** call to remove the golden, then bank again. Then copy BUILD127, HANDOFF-51 and the
READ file to `/mnt/user-data/outputs` and present them.

## Drive actions for M

- **Upload** to Materials (`1XX_5f3PZB6tjRtiZ2GIgd8Tt7i_4GgkY`): `HANDOFF-50.md` and
  `The_Method_1_6_BUILD126_compendia_papers_audits.md`.
- **Retire** once BUILD126 gates PASS in chat 98: HANDOFF-49 and BUILD125, plus any earlier
  compendia builds still present (BUILD107–BUILD123).
- **Keep BUILD124** for now — it is the only input under which chat 96's `r2-ch14l` and `r2-ch14m`
  reproduce, and §23.9.1's eight exact V values live in `r2-ch14l.out`. Retire it once R3 has
  re-banked those two against members or accepted them as historical.
- **Keep:** BUILD90 main (unchanged since chat 62), the **Prints & Proofs** folder
  (`1vYctzLppUZ2vFPJDCZ6wvkgSdj3v_f6n`) — the authentication baseline under Ruling 56 — the
  certificates, OWED-REGISTER-EXPANSIONS.md, OWED-EXPANSIONS-2.md, covers8.json, factor.py.

## Prompt for chat 98

"Chat 98. READ EVERYTHING BEFORE YOU DO ANYTHING. Live files: BUILD90 main (1,983,081 B, md5
49065309b0c4fe8e055f693aed295cca) and BUILD126 compendia (5,038,070 B, md5
8a43b95743867e3e41bc24c08ecc3db6, 62,386 lines, 406 members). List uploads, outputs and /home/claude
first. Run HANDOFF-50's §0 gate in full and in order — fetch both bundles by title, bootstrap
(decode, md5, extract, expect 408 files), then gate.py census, run --core, manifest, run r2-ch14n
r2-ch14o, cert 98; any FAIL stops the chat with a report. Read RULINGS-R2.md last block first: the
chat-95 block governs and it says a finding is not a question — deviations in the mathematics and in
the prose are recorded and flagged for repair, never put to M, and Prints & Proofs is read before
any question is asked. Do not ask M to rule on a defect. Read DEFERRED.md; chat 97's block is the
last of twenty-six. The standing block's Phase 0–4 Löwdin/three-body plan is executed carried state;
discard it per Ruling 41 — its discard is W-118, not W-107. Line numbers are MEMBER line numbers and
are never carried between chats, and neither is any count: re-scan every heading on
The_Method_1_6-2.md before reading a line. Then continue Phase R2 under the chat-81 cadence: the
section read is Chapter 23 §23.12–§23.15, main L6549–L6622, 74 lines, five headings, closing the
chapter; Chapter 24 opens L6623. Take the whole remainder as one unit. Read it all, census its
claims into computable and prose, then run exactly two instrument batches, r2-ch14p computable and
r2-ch14q prose, importing heading_line, section_span, has_token and enclosing from r2lib — copy
nothing, and read the six volume MEMBERS, never a BUILDnnn bundle path, which is what broke chat
96's goldens at chat 97's gate. This read closes chat 95's ν_V docket: read §23.15 once, then test
L6270 and L6923 and the Ga I attribution against it, noting that §23.11.1 L6538 does name Ga I with
one refusal but gives it no ν_V. Confirm §23.14 L6585 as the true home of r ≥ 5 and ν_V, which
L6501 miscites to §23.13. §23.13's empirically recovered exponents are testable against the exact V
values chat 96 banked in r2-ch14l.out — read them out of the golden rather than re-running it, since
it needs BUILD124 on disk. §23.14's claim about the book's own vocabulary must be tested against
actual usage, word-bounded. Chat 97 measured the §23.10.2 V table as monotone in k across every row,
the sign rule exact at j = 0…6, and 560 containments with zero failures — check any restatement
against those rather than re-measuring. Use the exact-token heading resolver, not prefix matching,
and never span a section by heading rank; note heading_line needs a trailing space after the number,
so the Register's bare '### 96' headings return None. Grep lowercase 'register NNN' by hand. Resolve
every pointer to the claim and not the heading, and if it fails at the named target grep the whole
volume before recording it. Give every negative claim its own witness. Never round with Python's
round() — use Decimal.quantize and name the convention, and convert exact Fractions
numerator/denominator. A heading is not a statement, the object under test is never its own witness,
a bound is not a measurement, and a boundary case is not a violation. Re-read every verdict against
the numbers printed above AND below it. When an instrument disagrees with a hand reading, suspect
the instrument first. Close the section read before the next opens. At close: bank both goldens with
gate.py bank, write W-137 ending with a blank line, build BUILD127 with close.py (reverse must
recover 8a43b957…), write HANDOFF-51. A changed append-only member is grown with --append, never
--members. No corrections, no Register entries, no TASK 1 until the review closes. Handoff at 90–95 %
of context or on a closed section read — never earlier, never mid-section. Timeout on every call.
Delete-only calls for pycache, never chained to gate.py bank. Never copy over an existing file."
