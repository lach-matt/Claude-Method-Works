# HANDOFF-26 — The Method 1.6 — chat 74 → chat 75 (supersedes HANDOFF-25, retired unused)

- Written from **chat 74** for **chat 75**. Live files: **BUILD90 main** (unchanged since chat 62) and **BUILD101 compendia** (= BUILD100 + W-111 + 21 members). Register **1 to 1792** (unchanged). W-111 IS seated; chat 75 seats nothing at open and writes W-112 at close.
- **Rulings and discipline:** the member `RULINGS-R2.md` (md5 5df68594cc2babe0a7f0a6615a360ecb) governs and is append-only; read it at open. **Deferred cross-chapter items:** the member `DEFERRED.md` (f3c9d2b09413a7e0e7f4695f922b64dd) governs; do not re-derive. **Findings carried to R3:** the READ-chNN.md members and W-101…W-111 in WORKING-REGISTER.md; nothing is restated here.
- **Carried state to discard (Ruling 41):** the standing prompt block's "Phase 0–4" Löwdin/three-body plan is executed carried state (MEASURED in W-107: Chapters 35–36 seated under Part VII, Register 1701–1724); do not re-open it or put it to M. Project knowledge holds BUILD12/BUILD53 only — list it, never read those bundles. Retired handoffs are gone from Drive; never fetch or cite one. The compendia bundle carries an older HANDOFF-2…53 member series; never add HANDOFF-NN.md as a member.

## §0 Gate (each step its own tool call under `timeout 280`; any FAIL stops the chat with a report)

1. `ls -la /mnt/user-data/uploads /mnt/user-data/outputs /home/claude` (uploads holds this file); `recent_chats` confirms the latest chat is 74.
2. Fetch both bundles by title: `Google Drive:search_files` with `title contains 'BUILD101_compendia' or title contains 'BUILD90_main'`, pageSize 5, excludeContentSnippets; `Google Drive:download_file_content` on each fileId. Both spill to `/mnt/user-data/tool_results/<id>.json`; note the two paths. (Each fetch leaves a ~65 KB base64 preview in context — expected; the bytes decide, not the name.)
3. Bootstrap (decode, verify, extract — the only step outside gate.py, because gate.py is a member):

```
timeout 280 python3 - <<'EOF'
import json, base64, hashlib, re, os
EXP={'main':'49065309b0c4fe8e055f693aed295cca','comp':'893a9826a02ce6065715425d5603a796'}
NAME={'main':'/home/claude/The_Method_1_6_BUILD90_main_and_register.md','comp':'/home/claude/The_Method_1_6_BUILD101_compendia_papers_audits.md'}
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

   Expected: main 1,983,081 B · 49065309b0c4fe8e055f693aed295cca · 18,470 lines; compendia **3,204,034 B · 893a9826a02ce6065715425d5603a796 · 38,782 lines**; 216 members extracted (2 + 214).
4. `python3 /home/claude/members/gate.py census` → `OK census: DEFECT-CENSUS.tsv byte-identical` (must run before any instrument: it refuses if a pycache or a scratch census exists).
5. `python3 /home/claude/members/gate.py run --core` → five `OK` lines (tower-2, kinds, minmax, r2-tools-constants, extent — the tower 976/1,654/2,535/13,585/70,905/199,130, the kinds 1565 · 1356 · 499 · 149, the min/max figures, the constants sites and the "1 to 1792" sites are the banked goldens; a diff prints only where the run differs).
6. `python3 /home/claude/members/gate.py manifest` → `MANIFEST OK: 215 members listed, 216 files extracted`; it prints both bundles' bytes/md5/lines and MANIFEST.tsv **14,448 B · 609281651c9aeddf9e6681af77bb0d30**. Every member's bytes, md5 and lines are checked there (WORKING-REGISTER.md 550,024 B · cef9816839ab8d0165c881c20d9c45f1 · 4,762 lines, ends W-111; gate.py 9,377 B · a01ef15a7920b7a11f3f2e9168d5d130; close.py 6,456 B · 98acae678629305fad0f3830488b3ee9; r2lib.py 11,146 B · 1403948913cafa47b2b2446b915dc9ad; tower-2.py c0bce27a; census.py f5a73e2b; kinds.py 4262f7c5; minmax.py 26da1d78; r2-tools.py 4702f5f9 — all in the manifest).
7. `python3 /home/claude/members/gate.py run r2-ch12i r2-ch12j r2-ch12k` (chat 74's instruments; ~3 s) — or `run --all` for all fifteen goldens (~55 s; r2-ch12c has no golden, it prints wall-clock time).
8. `python3 /home/claude/members/gate.py cert 75` → `GATE-ch75 … verdict PASS`, written to /home/claude/GATE-ch75.txt. Shell is dash: text goes through python heredocs or create_file; non-ASCII grep output through python.

## Next work — Phase R2 continues at main §12.11.0.8

Order: **§12.11.0.8 (L2842–2897)** "Past, present and future — a path, not a triangle" (389 at L2886 — read against r2-ch12f.out's split 182,719 : 9,331 and its 389 reversible edges); §12.11.0.9 (L2898–2931; 389 at L2909/L2915); §12.11.0.10 (L2932–2956; the tower table — the Λ₉′ row L2938 reproduces 1,561 / 27,648 / 5.65 %); §12.11.0.11 (L2957–2998); §12.11.0.12 (L2999–3031); §12.11.1–12.11.1.7 (L3032–3362; DEFERRED.md's items); §12.11.2–12.11.7 (L3363–3507); Chapter 13 (L3508–3676); Part III (Ch. 14, L3679). Chapter map: `grep -n '^## ' members/The_Method_1_6-2.md`; subsections: `grep -n '^### 12\.' members/The_Method_1_6-2.md`.

Per segment (one or two subsections; close each — files written, md5s measured — before the next opens): `python3 members/r2-tools.py lines|pointers|figures|census|layout A B` (its pointer regex is case-sensitive: grep lowercase "register NNN" separately); read every line; resolve every pointer to heading AND claim; grep every figure; re-measure every tower-computable claim on **all** cells or pairs in `members/r2-chNN.py` (next names r2-ch12l.py, r2-ch12m.py …), importing r2lib by path:

```
import importlib.util, os; H=os.path.dirname(os.path.abspath(__file__))
s=importlib.util.spec_from_file_location('r2lib', os.path.join(H,'r2lib.py')); r2lib=importlib.util.module_from_spec(s); s.loader.exec_module(r2lib); T=r2lib.load_tower()
```

r2lib carries build9/tarjan/analyse (r2-ch12f), is_tree, closure/factor_q/ci/components/separates (r2-ch12i), support/direct/composed (r2-ch12j), mi/ci_sets/gG_index (r2-ch12k), lam9p, the Λ₉/Λ₉′ and (g, G) constants; functions of r2-ch12c/e/g/h are lifted verbatim when next needed (DEFERRED.md). Write READ-chNN.md (A deviations with both texts, B verified, C incidental) and CENSUS-CLOSURES-chNN.tsv (id, verdict, reason; A vocabulary; header only when no row is in range). Instruments must print no wall-clock time (goldens must be deterministic).

## Close of chat 75

1. `rm -rf /home/claude/members/__pycache__` (delete-only call); `python3 members/gate.py bank r2-ch12l …` for each new instrument (writes r2-ch12l.out; refuses to overwrite).
2. Write /home/claude/W-112.md: begins `### W-112 —`, ends with a blank line; records the gate, each segment, the close estimate.
3. `python3 members/close.py --old /home/claude/The_Method_1_6_BUILD101_compendia_papers_audits.md --new /home/claude/The_Method_1_6_BUILD102_compendia_papers_audits.md --w /home/claude/W-112.md --members members/READ-ch12l.md members/CENSUS-CLOSURES-ch12l.tsv members/r2-ch12l.py members/r2-ch12l.out …` — it appends W-112 and the members, rewrites MANIFEST.tsv, asserts only WORKING-REGISTER.md and MANIFEST.tsv changed, and must print `reverse recovers md5 893a9826a02ce6065715425d5603a796  == old: True` before writing. If RULINGS-R2.md or DEFERRED.md must grow, write the new dated block to a scratch file and pass `--append DEFERRED.md /home/claude/deferred-add.md` (or RULINGS-R2.md); close.py appends it before the member's END marker under the same guards as the W text and lists the member among the changed ones. Never edit a seated member in place.
4. HANDOFF-27 in this form (update: build numbers, md5s of the compendia bundle, MANIFEST.tsv and WORKING-REGISTER.md, the member count, the run list, next work, the prompt). `ls -la /mnt/user-data/outputs` before copying; never copy over an existing file; present HANDOFF-27.md first, then BUILD102 and the READ files.
5. Handoff at 90–95 % of context or on a closed segment — never earlier, never mid-segment; begin the close when the remaining context would not fit a segment plus the close (≈ 5 % — INFERRED), and record the estimate in W-112. No corrections, no Register entries, no TASK 1 until the review closes.

## M's Drive actions

- **UPLOAD** to Materials (`1XX_5f3PZB6tjRtiZ2GIgd8Tt7i_4GgkY`): `HANDOFF-26.md` and `The_Method_1_6_BUILD101_compendia_papers_audits.md` (893a9826…).
- **RETIRE:** HANDOFF-24, HANDOFF-25 (if uploaded), BUILD99, BUILD100 (if uploaded) once BUILD101 gates in chat 75; and any of BUILD84–98 compendia still present.
- **KEEP:** BUILD90 main, tower-2.py, chat65/66/67-instruments.tar.gz, SWEEP-B-C-chat67.md, convert.py, the certificates, OWED-REGISTER-EXPANSIONS.md, OWED-EXPANSIONS-2.md, covers8.json, factor.py.

## Prompt for chat 75

"Chat 75. READ EVERYTHING BEFORE YOU DO ANYTHING. Live files: BUILD90 main (1,983,081 B, md5 49065309b0c4fe8e055f693aed295cca) and BUILD101 compendia (3,204,034 B, md5 893a9826a02ce6065715425d5603a796, 38,782 lines, 214 members). List uploads, outputs and /home/claude first. Run HANDOFF-26's §0 gate in full and in order — fetch both bundles by title, bootstrap (decode, md5, extract), then gate.py census, run --core, manifest, run r2-ch12i r2-ch12j r2-ch12k, cert 75; any FAIL stops the chat with a report. Read RULINGS-R2.md and DEFERRED.md from the members. The standing block's Phase 0–4 (Löwdin/three-body) plan is executed carried state — discard it per Ruling 41; HANDOFF-25 is retired. Then continue Phase R2 at main §12.11.0.8 (L2842–2897), one or two subsections per segment, re-measuring every general claim on all cells or pairs with an r2-chNN.py that imports r2lib, closing each segment before the next. At close: bank each new instrument's golden with gate.py bank, write W-112, build BUILD102 with close.py (reverse must recover 893a9826…), write HANDOFF-27. No corrections, no Register entries, no TASK 1 until the review closes. Handoff at 90–95 % of context or on a closed segment — never earlier, never mid-segment. Timeout on every call. Never copy over an existing file."
