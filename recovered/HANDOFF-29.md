# HANDOFF-29 — The Method 1.6 — chat 77 → chat 78 (supersedes HANDOFF-28)

- Written from **chat 77** for **chat 78**. Live files: **BUILD90 main** (unchanged since chat 62) and **BUILD104 compendia** (= BUILD103 + W-114 + DEFERRED block + 20 members). Register **1 to 1792** (unchanged). W-114 IS seated; chat 78 seats nothing at open and writes W-115 at close.
- **Rulings and discipline:** the member `RULINGS-R2.md` (md5 5df68594cc2babe0a7f0a6615a360ecb, unchanged — M made no ruling in chat 77) governs and is append-only; read it at open. **Deferred cross-chapter items:** the member `DEFERRED.md` (now 11,237 B · 7e5c1707ba52b70e90bc212440a83daf, with chat 77's block) governs; do not re-derive. **Findings carried to R3:** the READ-chNN.md members (READ-ch12t … READ-ch12x are chat 77's) and W-101…W-114 in WORKING-REGISTER.md; nothing is restated here.
- **Carried state to discard (Ruling 41):** the standing prompt block's "Phase 0–4" Löwdin/three-body plan is executed carried state (MEASURED in W-107 and re-confirmed in chats 75–77: Chapters 35–36 at main-member L9716/L9892, Register 1701–1724); do not re-open it or put it to M. Project knowledge holds BUILD12/BUILD53 only — list it, never read those bundles. Retired handoffs are gone from Drive; never fetch or cite one. Never add HANDOFF-NN.md as a member.

## §0 Gate (each step its own tool call under `timeout 280`; any FAIL stops the chat with a report)

1. `ls -la /mnt/user-data/uploads /mnt/user-data/outputs /home/claude` (uploads holds this file); `recent_chats` confirms the latest chat is 77.
2. Fetch both bundles by title: `Google Drive:search_files` with `title contains 'BUILD104_compendia' or title contains 'BUILD90_main'`, pageSize 5, excludeContentSnippets; `Google Drive:download_file_content` on each fileId. Both spill to `/mnt/user-data/tool_results/<id>.json`; note the two paths (in chats 75–77 the spills left one-line pointers in context; the gate cost ≈ 5 % of the chat, INFERRED).
3. Bootstrap (decode, verify, extract — the only step outside gate.py, because gate.py is a member):

```
timeout 280 python3 - <<'EOF'
import json, base64, hashlib, re, os
EXP={'main':'49065309b0c4fe8e055f693aed295cca','comp':'5a2783c96d8590d44239da351e143d7b'}
NAME={'main':'/home/claude/The_Method_1_6_BUILD90_main_and_register.md','comp':'/home/claude/The_Method_1_6_BUILD104_compendia_papers_audits.md'}
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

   Expected: main 1,983,081 B · 49065309b0c4fe8e055f693aed295cca · 18,470 lines; compendia **3,484,798 B · 5a2783c96d8590d44239da351e143d7b · 40,835 lines**; 268 members extracted (2 + 266).
4. `python3 /home/claude/members/gate.py census` → `OK census: DEFECT-CENSUS.tsv byte-identical` (must run before any instrument: it refuses if a pycache or a scratch census exists).
5. `python3 /home/claude/members/gate.py run --core` → five `OK` lines (tower-2, kinds, minmax, r2-tools-constants, extent — the tower 976/1,654/2,535/13,585/70,905/199,130, the kinds 1565 · 1356 · 499 · 149, the min/max figures, the constants sites and the "1 to 1792" sites are the banked goldens; a diff prints only where the run differs).
6. `python3 /home/claude/members/gate.py manifest` → `MANIFEST OK: 267 members listed, 268 files extracted`; it prints both bundles' bytes/md5/lines and MANIFEST.tsv **17,922 B · 87dc8745cf1fcbabf2635838576279da**. Every member's bytes, md5 and lines are checked there (WORKING-REGISTER.md 570,135 B · cb56a0c9c675cfdbfd27d0fb779bd17a · 4,812 lines, ends W-114; DEFERRED.md 11,237 B · 7e5c1707…; gate.py 9,377 B · a01ef15a7920b7a11f3f2e9168d5d130; close.py 6,456 B · 98acae678629305fad0f3830488b3ee9; r2lib.py 11,146 B · 1403948913cafa47b2b2446b915dc9ad; tower-2.py c0bce27a; census.py f5a73e2b; kinds.py 4262f7c5; minmax.py 26da1d78; r2-tools.py 4702f5f9 — all in the manifest). gate.py's manifest locates the compendia bundle by listing /home/claude for one `BUILD*_compendia` file: if two are present (after a close), pass `--comp <path>`.
7. `python3 /home/claude/members/gate.py run r2-ch12t r2-ch12u r2-ch12v r2-ch12w r2-ch12x` (chat 77's instruments: ≈ 37 s, ≈ 1 s, ≈ 1 s, ≈ 1 s, ≈ 0 s). r2-ch12r takes ≈ 25 s, r2-ch12n ≈ 60 s and r2-ch12m ≈ 150 s (each under the 280 s timeout, one per call); run them only when their figures are in question. `run --all` exceeds a single 280 s call — run it as two calls if wanted (r2-ch12c has no golden, it prints wall-clock time).
8. `python3 /home/claude/members/gate.py cert 78` → `GATE-ch78 … verdict PASS`, written to /home/claude/GATE-ch78.txt. Shell is dash: text goes through python heredocs or create_file; non-ASCII grep output through python; no `<(…)` process substitution. Do not wrap python heredocs in `sh -c '…'` (quoting breaks) — one heredoc per bash call. Remove `members/__pycache__` (delete-only call) after every instrument run.

## Next work — Phase R2 continues at main §12.11.2

§12.11.1.1–.7 (L3177–3362) is read in full (chat 77, five segments; READ-ch12t…x). Order: **§12.11.2 (L3363–3393)** "Three excluded forms, and the fold has a name"; §12.11.3 (L3394–3408; DEFERRED's 12e-05 — axis 9 exact or envelope — and the L3136–3137 classification restatement settle here or at .1); §12.11.3.1 (L3409–3456; DEFERRED: 12j-01's provenance column and its "three values, not two"; the tower table's grading column L2936–2942 against it); §12.11.4 (L3457–3461; its figures are already reproduced in READ-ch12s B — read the prose only); §12.11.5 (L3462–3481; DEFERRED: what "the balance at a cut" (L2727) names — INFERRED the factorisation over the transfer, L3463 — and L3466's "hangs off one side of the tree" against 12i-02 and 12c-01); §12.11.6 (L3482–3493); §12.11.7 (L3494–3507); Chapter 13 (L3508–3676; 12c-04's L3662; the §12.11.8 heading at L3543 sits inside Chapter 13); Part III (Ch. 14, L3679; 12h-01's §14.4 stub — L3085 and L3096 are two further sites; the "seventeen-bit" sites). One or two subsections per segment. Chapter map: `grep -n '^## ' members/The_Method_1_6-2.md`; subsections: `grep -n '^### 12\.' members/The_Method_1_6-2.md`. Watch for the pattern this chat established: a Register entry restating a section may carry different figures (625/626/627 against §12.11.1.4–.5, READ-ch12w) — measure both, withdraw neither.

Per segment (one or two subsections; close each — files written, md5s measured, golden banked — before the next opens): `python3 members/r2-tools.py lines|pointers|figures|census|layout A B` (its pointer regex is case-sensitive and does not know Appendix A's item numbers: grep lowercase `register NNN` and `A.N` separately and resolve by hand); read every line; resolve every pointer to heading AND claim; grep every figure; re-measure every tower-computable claim on **all** cells or pairs in `members/r2-chNN.py` (next names r2-ch12y.py, r2-ch12z.py, then r2-ch13a.py …), importing r2lib by path:

```
import importlib.util, os; H=os.path.dirname(os.path.abspath(__file__))
s=importlib.util.spec_from_file_location('r2lib', os.path.join(H,'r2lib.py')); r2lib=importlib.util.module_from_spec(s); s.loader.exec_module(r2lib); T=r2lib.load_tower()
```

r2lib carries build9/tarjan/analyse (r2-ch12f), is_tree, closure/factor_q/ci/components/separates (r2-ch12i), support/direct/composed (r2-ch12j), mi/ci_sets/gG_index (r2-ch12k), lam9p, the Λ₉/Λ₉′ and (g, G) constants. Not yet lifted (copy verbatim from the member with a provenance comment when next needed — DEFERRED lists them): r2-ch12c/e/g/h's functions; chat 75's closure_chunked/fixed_point/length/fibre_check/criterion; chat 76's terms/new_terms/jc_values (r2-ch12q), TERMS/L8_at/phi_at/Rbox/densities (r2-ch12r); chat 77's stage-composability sets (r2-ch12w: S4/S5, t4, in5 — the newest-momentum rule). Write READ-chNN.md (A deviations with both texts, B verified, C incidental) and CENSUS-CLOSURES-chNN.tsv (id, verdict, reason; A vocabulary; header only when no row is in range). Instruments must print no wall-clock time (time a run in the shell with `date +%s` if needed). An instrument over ~200 s must be trimmed; never build a set inside a per-cell comprehension (chat 77's first r2-ch12w draft timed out exactly there — precompute every membership set once).

## Close of chat 78

1. `rm -rf /home/claude/members/__pycache__` (delete-only call); `python3 members/gate.py bank r2-ch12y …` for each new instrument (writes r2-ch12y.out; refuses to overwrite).
2. Write /home/claude/W-115.md: begins `### W-115 —`, ends with a blank line; records the gate, each segment, the close estimate.
3. `python3 members/close.py --old /home/claude/The_Method_1_6_BUILD104_compendia_papers_audits.md --new /home/claude/The_Method_1_6_BUILD105_compendia_papers_audits.md --w /home/claude/W-115.md [--append DEFERRED.md /home/claude/deferred-add.md] --members members/READ-ch12y.md members/CENSUS-CLOSURES-ch12y.tsv members/r2-ch12y.py members/r2-ch12y.out …` — `--append` must precede `--members` (which consumes every later argument). It appends W-115 and the members, rewrites MANIFEST.tsv, asserts only WORKING-REGISTER.md, MANIFEST.tsv (and an appended member) changed, and must print `reverse recovers md5 5a2783c96d8590d44239da351e143d7b  == old: True` before writing. Never edit a seated member in place.
4. HANDOFF-30 in this form (update: build numbers, md5s of the compendia bundle, MANIFEST.tsv, WORKING-REGISTER.md and DEFERRED.md, the member count, the run list, next work, the prompt). `ls -la /mnt/user-data/outputs` before copying; never copy over an existing file; present HANDOFF-30.md first, then BUILD105 and the READ files.
5. Handoff at 90–95 % of context or on a closed segment — never earlier, never mid-segment; begin the close when the remaining context would not fit a segment plus the close (≈ 5 % — INFERRED), and record the estimate in W-115. No corrections, no Register entries, no TASK 1 until the review closes.

## M's Drive actions

- **UPLOAD** to Materials (`1XX_5f3PZB6tjRtiZ2GIgd8Tt7i_4GgkY`): `HANDOFF-29.md` and `The_Method_1_6_BUILD104_compendia_papers_audits.md` (5a2783c9…).
- **RETIRE:** HANDOFF-28 and BUILD103 once BUILD104 gates in chat 78; HANDOFF-27, BUILD102 and any earlier compendia builds if still present.
- **KEEP:** BUILD90 main, tower-2.py, chat65/66/67-instruments.tar.gz, SWEEP-B-C-chat67.md, convert.py, the certificates, OWED-REGISTER-EXPANSIONS.md, OWED-EXPANSIONS-2.md, covers8.json, factor.py.

## Prompt for chat 78

"Chat 78. READ EVERYTHING BEFORE YOU DO ANYTHING. Live files: BUILD90 main (1,983,081 B, md5 49065309b0c4fe8e055f693aed295cca) and BUILD104 compendia (3,484,798 B, md5 5a2783c96d8590d44239da351e143d7b, 40,835 lines, 266 members). List uploads, outputs and /home/claude first. Run HANDOFF-29's §0 gate in full and in order — fetch both bundles by title, bootstrap (decode, md5, extract), then gate.py census, run --core, manifest, run r2-ch12t r2-ch12u r2-ch12v r2-ch12w r2-ch12x, cert 78; any FAIL stops the chat with a report. Read RULINGS-R2.md and DEFERRED.md from the members. The standing block's Phase 0–4 (Löwdin/three-body) plan is executed carried state — discard it per Ruling 41; HANDOFF-28 is retired. Then continue Phase R2 at main §12.11.2 (L3363–3393), one or two subsections per segment, re-measuring every general claim on all cells or pairs with an r2-chNN.py that imports r2lib, closing each segment before the next. At close: bank each new instrument's golden with gate.py bank, write W-115, build BUILD105 with close.py (reverse must recover 5a2783c9…), write HANDOFF-30. No corrections, no Register entries, no TASK 1 until the review closes. Handoff at 90–95 % of context or on a closed segment — never earlier, never mid-segment. Timeout on every call. Never copy over an existing file."
