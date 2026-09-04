# HANDOFF-42 — The Method 1.6 — chat 89 → chat 90

- Written from **chat 89** for **chat 90**. Live files: **BUILD90 main** (unchanged since chat 62) and
  **BUILD117 compendia** (= BUILD116 + W-127 + chat 89's DEFERRED block + six new members). Register
  **1 to 1792** (unchanged — no Register entry has been written since the chat-67 hold). W-127 IS
  seated; chat 90 seats nothing at open and writes W-128 at close.
- **Rulings and discipline:** the member `RULINGS-R2.md` (6,041 B · 30 lines, unchanged this chat)
  governs and is append-only; **read it at open, last block first** — the chat-81 block sets the
  cadence, and chats 82–89 have all run it. **Deferred cross-chapter items:** `DEFERRED.md`
  (**79,866 B · 353 lines**, with chat 89's block) governs; do not re-derive. **Findings carried to
  R3:** the READ-chNN.md members (READ-ch13x is chat 89's) and W-101…W-127 in WORKING-REGISTER.md;
  nothing is restated here.
- **Carried state to discard (Ruling 41):** the standing prompt block's "Phase 0–4" Löwdin/three-body
  plan is executed carried state (MEASURED in W-107, re-confirmed in chats 75–89); do not re-open it
  or put it to M. Its **residue is live and lands in chat 90**: §21.5.1 *And the three-body count is
  exactly one* (L5690) is checked against W-107, not re-derived. Project knowledge holds BUILD12/
  BUILD53 only — list it, never read those bundles. Retired handoffs are gone from Drive; never fetch
  or cite one. Never add HANDOFF-NN.md as a member.

## §0 Gate (each step its own tool call under `timeout 280`; any FAIL stops the chat with a report)

1. `ls -la /mnt/user-data/uploads /mnt/user-data/outputs /home/claude`; `recent_chats` confirms the
   latest chat is 89. Read `/mnt/project/CLAUDE.md` (project instruction; never a member).
2. Fetch both bundles by title: `Google Drive:search_files` with
   `title contains 'BUILD117_compendia' or title contains 'BUILD90_main'`, pageSize 5,
   excludeContentSnippets; `Google Drive:download_file_content` on each fileId. Both spill to
   `/mnt/user-data/tool_results/<id>.json`; note the two paths (the gate costs ≈ 13 %, MEASURED).
3. Bootstrap (the only step outside gate.py, because gate.py is a member):

```
timeout 280 python3 - <<'EOF'
import json, base64, hashlib, re, os
EXP={'main':'49065309b0c4fe8e055f693aed295cca','comp':'2d9cdedc114e1f0ea5f3d4ad08284460'}
NAME={'main':'/home/claude/The_Method_1_6_BUILD90_main_and_register.md','comp':'/home/claude/The_Method_1_6_BUILD117_compendia_papers_audits.md'}
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
   **4,367,039 B · 2d9cdedc114e1f0ea5f3d4ad08284460 · 52,498 lines**; **360 members extracted (2 + 358)**.
4. `python3 /home/claude/members/gate.py census` → `OK census: DEFECT-CENSUS.tsv byte-identical`
   (1,556 rows + header, ≈ 14 s).
5. `python3 /home/claude/members/gate.py run --core` → five `OK` (tower 976/1,654/2,535/13,585/70,905/
   199,130; kinds 1565 · 1356 · 499 · 149; minmax; r2-tools-constants; extent "1 to 1792").
6. `python3 /home/claude/members/gate.py manifest` → `MANIFEST OK: 359 members listed, 360 files
   extracted`; MANIFEST.tsv **24,087 B · 8831c4759268a41b19d0d035299b2f43 · 360 lines**;
   WORKING-REGISTER.md **638,271 B · e23e9343439211be26573064ccf85d99 · 5,442 lines**, ends **W-127**;
   DEFERRED.md **79,866 B · 8aa88adc · 353 lines**; RULINGS-R2.md 6,041 B · 4cce8039;
   **r2lib.py 18,486 B · 3344ca87 · 396 lines** (unchanged this chat); gate.py 9,377 B · a01ef15a;
   close.py 6,456 B · 98acae67; tower-2.py c0bce27a; census.py f5a73e2b; kinds.py 4262f7c5;
   minmax.py 26da1d78; r2-tools.py 4702f5f9. If two `BUILD*_compendia` files are present after a
   close, pass `--comp <path>` explicitly.
7. `python3 /home/claude/members/gate.py run r2-ch13x r2-ch13y` → two `OK` (chat 89's goldens:
   r2-ch13x.out 2,440 B · 938fa1f6 · 57 lines, ≈ 16 s; r2-ch13y.out 7,206 B · 92ddfa23 · 109 lines).
8. `python3 /home/claude/members/gate.py cert 90` → writes `/home/claude/GATE-ch90.txt`, verdict PASS
   only if every logged step passed. A FAIL anywhere stops the chat and is reported, not worked around.

## What chat 89 did (do not repeat)

Chapter 20 read whole — main **L5551–L5596, 46 lines, three sections**, all boundaries measured and
reproduced. Twenty-five claims censused (ten computable, fifteen prose), two instrument batches run
and banked, **twelve deviations, eight verified, five incidentals, two census rows closed** in
`READ-ch13x.md` and `CENSUS-CLOSURES-ch13x.tsv`. The load-bearing finding: §20.3's worked example is
exact at **E = 750** and false at **E = 0** — the spectroscopic naming leaves the same 840 cells, and
over all six relabellings of the value alphabet (|X|, E) is invariantly (840, 750), so no naming of
values can move a closure defect. Its general criterion, by contrast, holds exactly: 686 of 686
preimages, 434 of 434 congruences. Two cross-volume doctrinal findings — §20.2's six languages are
not §11.1's six, and logic is a language in main and not a language in the Register and the
Mathematical Compendium. Full detail is in READ-ch13x.md and W-127; do not re-measure them.

## Chat 90's section read — Chapter 21, first part

MEASURED by heading scan in chat 89: Chapter 21 *Translation, and what it costs* opens **L5597**;
§21.1 L5599, §21.2 L5616, §21.3 L5624, §21.4 L5636, §21.5 L5645, §21.5.1 L5690, §21.5.2 L5708,
§21.5.3 L5761, §21.5.4 L5797, §21.5.5 L5835, §21.6 L5874, §21.6.1 L5905, §21.6.2 L5924; **PART V
opens L5937**, Chapter 22 at L5939. The chapter is 340 lines and thirteen headings — larger than any
single read in Phase R2 — so **chat 90 takes L5597–L5689 (§21.1 through §21.5's opening, 93 lines)**
and leaves §21.5.1 onward for chat 91. Confirm every boundary by scan before reading a line anyway.

Carried in, already measured, not to be re-derived: the |Δℓ| ≤ 1 band named at **L5606** is the whole
of Λ₉ (1,654 of 1,654) with **E = 0**, excluding nothing; the **L5610** row identifying E in order,
the void in geometry and V in calculus agrees with §27 (L7203–L7363), which carries all three names.
§19.5.1 L5492 sends *this is §21.5's obstruction* forward into §21.5.

Instruments: **r2-ch13z** (computable) and **r2-ch14a** (prose). §21.1's title claims one object under
two namings with E as the price — that is the general form of the claim 20x-01 refuted in its
instance, so re-use r2-ch13x's **relabelling sweep** (recompute (|X|, E) over every bijection of a
coordinate's value alphabet) before accepting any sentence of the form *this naming makes it close*.
Use chat 88's exact-token heading resolver, never prefix matching, or §21.5 resolves to §21.5.5 and
§21.6 to §21.6.2. Grep lowercase `register NNN` by hand; r2-tools' pointer regex is case-sensitive.
Check every printed pair count against C(N, 2), this volume's convention. Resolve every pointer to the
claim and not the heading; measure a claim and its stated witness separately; check the arithmetic of
every ratio and percentage; where the text prints a sample, measure the population.

## Close (chat 90)

`gate.py bank r2-ch13z r2-ch14a`; delete pycache in its own delete-only call; write `W-128.md`
(begins `### W-`, ends with a blank line); append a DEFERRED block as `DEF-90.md`; then

```
timeout 280 python3 members/close.py --old The_Method_1_6_BUILD117_compendia_papers_audits.md \
  --new The_Method_1_6_BUILD118_compendia_papers_audits.md --w W-128.md \
  --main The_Method_1_6_BUILD90_main_and_register.md --append DEFERRED.md DEF-90.md \
  --members members/READ-ch13z.md members/CENSUS-CLOSURES-ch13z.tsv members/r2-ch13z.py \
  members/r2-ch13z.out members/r2-ch14a.py members/r2-ch14a.out
```

It must print **reverse recovers md5 2d9cdedc114e1f0ea5f3d4ad08284460 == old: True** before writing;
if it does not, nothing is written and the failure is reported. Then copy BUILD118, HANDOFF-43 and
the READ file to `/mnt/user-data/outputs` and present them. `--append` arguments must precede
`--members`. Note that after a close, `gate.py manifest` reports FAIL on changed members because the
extracted copies stay at pre-close state — verify appends by reading the new bundle directly.

## Drive actions for M

- **Upload** to Materials (`1XX_5f3PZB6tjRtiZ2GIgd8Tt7i_4GgkY`): `HANDOFF-42.md` and
  `The_Method_1_6_BUILD117_compendia_papers_audits.md`.
- **Retire** once BUILD117 gates PASS in chat 90: HANDOFF-41 and BUILD116, plus any earlier compendia
  builds still present (BUILD107–BUILD115).
- **Keep:** BUILD90 main (the live main bundle, unchanged since chat 62), the Prints & Proofs folder
  (`1vYctzLppUZ2vFPJDCZ6wvkgSdj3v_f6n`, the original-input witness per Ruling 56), the certificates,
  OWED-REGISTER-EXPANSIONS.md, OWED-EXPANSIONS-2.md, covers8.json, factor.py.

## Prompt for chat 90

"Chat 90. READ EVERYTHING BEFORE YOU DO ANYTHING. Live files: BUILD90 main (1,983,081 B, md5
49065309b0c4fe8e055f693aed295cca) and BUILD117 compendia (4,367,039 B, md5
2d9cdedc114e1f0ea5f3d4ad08284460, 52,498 lines, 358 members). List uploads, outputs and /home/claude
first. Run HANDOFF-42's §0 gate in full and in order — fetch both bundles by title, bootstrap (decode,
md5, extract, expect 360 files), then gate.py census, run --core, manifest, run r2-ch13x r2-ch13y, cert
90; any FAIL stops the chat with a report. Read RULINGS-R2.md and DEFERRED.md from the members; chat
89's DEFERRED block is the last one. The standing block's Phase 0–4 (Löwdin/three-body) plan is
executed carried state; discard it per Ruling 41, but its residue is live — §21.5.1's 'the three-body
count is exactly one' is checked against W-107, not re-derived, when it is reached in chat 91. Then
continue Phase R2 under the chat-81 cadence: the section read is Chapter 21 first part, main L5597–
L5689, §21.1 L5599, §21.2 L5616, §21.3 L5624, §21.4 L5636, §21.5 L5645 — scan the headings and confirm
every boundary before reading a line. Do not take §21.5.1 onward; that is chat 91's, and a section read
is never split across chats. Read it all, census its claims into computable and prose, then run exactly
two instrument batches, r2-ch13z computable and r2-ch14a prose. §21.1 claims one object under two
namings with E as the price — chat 89 refuted the instance of that claim at §20.3 and proved the
class result that E is invariant under any relabelling of a coordinate's values, so re-use r2-ch13x's
relabelling sweep before accepting any sentence of the form 'this naming makes it close'. Use chat
88's exact-token heading resolver, not prefix matching, or §21.5 will resolve to §21.5.5; grep
lowercase 'register NNN' by hand, since r2-tools' pointer regex is case-sensitive. Check every printed
pair count against C(N, 2). Resolve every pointer to the claim and not the heading; measure a claim and
its stated witness separately; check the arithmetic of every ratio and percentage as well as every
count; where the text prints a sample, measure the population; and where a section corrects a
neighbour, grep the neighbour's captions and tables too, not only its sentences. Close the section read
before the next opens. At close: bank both goldens with gate.py bank, write W-128, build BUILD118 with
close.py (reverse must recover 2d9cdedc…), write HANDOFF-43. No corrections, no Register entries, no
TASK 1 until the review closes. Handoff at 90–95 % of context or on a closed section read — never
earlier, never mid-section. Timeout on every call. Delete-only calls for pycache, never chained to
gate.py bank. Never copy over an existing file."
