# HANDOFF-28 — The Method 1.6 — chat 76 → chat 77 (supersedes HANDOFF-27)

- Written from **chat 76** for **chat 77**. Live files: **BUILD90 main** (unchanged since chat 62) and **BUILD103 compendia** (= BUILD102 + W-113 + DEFERRED block + 12 members). Register **1 to 1792** (unchanged). W-113 IS seated; chat 77 seats nothing at open and writes W-114 at close.
- **Rulings and discipline:** the member `RULINGS-R2.md` (md5 5df68594cc2babe0a7f0a6615a360ecb, unchanged — M made no ruling in chat 76; M asked whether errors were being repaired as found and, told they are recorded only under the chat 67 ruling, replied "Continue as planned") governs and is append-only; read it at open. **Deferred cross-chapter items:** the member `DEFERRED.md` (now 7,961 B · b0d5e48e1215686283dc9f69db01db25, with chat 76's block) governs; do not re-derive. **Findings carried to R3:** the READ-chNN.md members (READ-ch12q … READ-ch12s are chat 76's) and W-101…W-113 in WORKING-REGISTER.md; nothing is restated here.
- **Carried state to discard (Ruling 41):** the standing prompt block's "Phase 0–4" Löwdin/three-body plan is executed carried state (MEASURED in W-107 and re-confirmed in chats 75 and 76: Chapters 35–36 at main-member L9716/L9892, Register 1701–1724); do not re-open it or put it to M. Project knowledge holds BUILD12/BUILD53 only — list it, never read those bundles. Retired handoffs are gone from Drive; never fetch or cite one. Never add HANDOFF-NN.md as a member.

## §0 Gate (each step its own tool call under `timeout 280`; any FAIL stops the chat with a report)

1. `ls -la /mnt/user-data/uploads /mnt/user-data/outputs /home/claude` (uploads holds this file); `recent_chats` confirms the latest chat is 76.
2. Fetch both bundles by title: `Google Drive:search_files` with `title contains 'BUILD103_compendia' or title contains 'BUILD90_main'`, pageSize 5, excludeContentSnippets; `Google Drive:download_file_content` on each fileId. Both spill to `/mnt/user-data/tool_results/<id>.json`; note the two paths (in chats 75 and 76 the spills left one-line pointers in context; the gate cost ≈ 5 % of the chat, INFERRED).
3. Bootstrap (decode, verify, extract — the only step outside gate.py, because gate.py is a member):

```
timeout 280 python3 - <<'EOF'
import json, base64, hashlib, re, os
EXP={'main':'49065309b0c4fe8e055f693aed295cca','comp':'fcf00e08efeaf4b43daa90d403fe1120'}
NAME={'main':'/home/claude/The_Method_1_6_BUILD90_main_and_register.md','comp':'/home/claude/The_Method_1_6_BUILD103_compendia_papers_audits.md'}
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

   Expected: main 1,983,081 B · 49065309b0c4fe8e055f693aed295cca · 18,470 lines; compendia **3,397,534 B · fcf00e08efeaf4b43daa90d403fe1120 · 40,226 lines**; 248 members extracted (2 + 246).
4. `python3 /home/claude/members/gate.py census` → `OK census: DEFECT-CENSUS.tsv byte-identical` (must run before any instrument: it refuses if a pycache or a scratch census exists).
5. `python3 /home/claude/members/gate.py run --core` → five `OK` lines (tower-2, kinds, minmax, r2-tools-constants, extent — the tower 976/1,654/2,535/13,585/70,905/199,130, the kinds 1565 · 1356 · 499 · 149, the min/max figures, the constants sites and the "1 to 1792" sites are the banked goldens; a diff prints only where the run differs).
6. `python3 /home/claude/members/gate.py manifest` → `MANIFEST OK: 247 members listed, 248 files extracted`; it prints both bundles' bytes/md5/lines and MANIFEST.tsv **16,590 B · b0b16eb8a8302834d335108adaf620ae**. Every member's bytes, md5 and lines are checked there (WORKING-REGISTER.md 564,594 B · da224def173f8b4d14cf43dcb516236a · 4,792 lines, ends W-113; DEFERRED.md 7,961 B · b0d5e48e…; gate.py 9,377 B · a01ef15a7920b7a11f3f2e9168d5d130; close.py 6,456 B · 98acae678629305fad0f3830488b3ee9; r2lib.py 11,146 B · 1403948913cafa47b2b2446b915dc9ad; tower-2.py c0bce27a; census.py f5a73e2b; kinds.py 4262f7c5; minmax.py 26da1d78; r2-tools.py 4702f5f9 — all in the manifest). gate.py's manifest locates the compendia bundle by listing /home/claude for one `BUILD*_compendia` file: if two are present (after a close), pass `--comp <path>`.
7. `python3 /home/claude/members/gate.py run r2-ch12q r2-ch12r r2-ch12s` (chat 76's instruments: ≈ 10 s, ≈ 25 s, ≈ 2 s — r2-ch12r sweeps every cell of Λ₁₃'s 47,775,744-cell ambient box). r2-ch12n takes ≈ 60 s and r2-ch12m ≈ 150 s (each under the 280 s timeout, one per call); run them only when their figures are in question. `run --all` exceeds a single 280 s call — run it as two calls if wanted (r2-ch12c has no golden, it prints wall-clock time).
8. `python3 /home/claude/members/gate.py cert 77` → `GATE-ch77 … verdict PASS`, written to /home/claude/GATE-ch77.txt. Shell is dash: text goes through python heredocs or create_file; non-ASCII grep output through python; no `<(…)` process substitution. Do not wrap python heredocs in `sh -c '…'` (quoting breaks) — one heredoc per bash call. Remove `members/__pycache__` (delete-only call) after every instrument run.

## Next work — Phase R2 continues at main §12.11.1.1

§12.11.1 (L3032–3176) is read in full (chat 76, three segments; all of its DEFERRED items closed; READ-ch12q/r/s). Order: **§12.11.1.1 (L3177–3204)** "The eleventh axis's density, computed under variation"; §12.11.1.2 (L3205–3232; both denominators 904 of 1,654 and 739 of 1,169 — r2lib.analyse prints them); §12.11.1.3 (L3233–3268); §12.11.1.4 (L3269–3295); §12.11.1.5 (L3296–3317); §12.11.1.6 (L3318–3337); §12.11.1.7 (L3338–3362) — one or two subsections per segment; §12.11.2–12.11.7 (L3363–3507; DEFERRED's 12e-05, 12c-01, 12j-01 items; §12.11.4's figures are already reproduced in READ-ch12s B — read its prose only; the §12.11.8 heading at L3543 sits inside Chapter 13); Chapter 13 (L3508–3676; 12c-04's L3662); Part III (Ch. 14, L3679; 12h-01's §14.4 stub — L3085 and L3096 are two further sites of it; the "seventeen-bit" sites). Chapter map: `grep -n '^## ' members/The_Method_1_6-2.md`; subsections: `grep -n '^### 12\.' members/The_Method_1_6-2.md`. Two conditions the density definition omits are now on record (12q-01 parity; 12r-01 the conjugation ceiling) — the §12.11.1.x density recomputations under variation must be read against them.

Per segment (one or two subsections; close each — files written, md5s measured, golden banked — before the next opens): `python3 members/r2-tools.py lines|pointers|figures|census|layout A B` (its pointer regex is case-sensitive and does not know Appendix A's item numbers: grep lowercase `register NNN` and `A.N` separately and resolve by hand); read every line; resolve every pointer to heading AND claim; grep every figure; re-measure every tower-computable claim on **all** cells or pairs in `members/r2-chNN.py` (next names r2-ch12t.py, r2-ch12u.py …), importing r2lib by path:

```
import importlib.util, os; H=os.path.dirname(os.path.abspath(__file__))
s=importlib.util.spec_from_file_location('r2lib', os.path.join(H,'r2lib.py')); r2lib=importlib.util.module_from_spec(s); s.loader.exec_module(r2lib); T=r2lib.load_tower()
```

r2lib carries build9/tarjan/analyse (r2-ch12f), is_tree, closure/factor_q/ci/components/separates (r2-ch12i), support/direct/composed (r2-ch12j), mi/ci_sets/gG_index (r2-ch12k), lam9p, the Λ₉/Λ₉′ and (g, G) constants. Not yet lifted (lift verbatim with provenance when next needed — DEFERRED lists them): r2-ch12c/e/g/h's functions; chat 75's closure_chunked/fixed_point/length/fibre_check/criterion; chat 76's terms/new_terms/jc_values (r2-ch12q), TERMS/L8_at/phi_at/Rbox/densities (r2-ch12r) — copy them verbatim from the member with a provenance comment, as r2-ch12r and r2-ch12s did. Write READ-chNN.md (A deviations with both texts, B verified, C incidental) and CENSUS-CLOSURES-chNN.tsv (id, verdict, reason; A vocabulary; header only when no row is in range). Instruments must print no wall-clock time (time a run in the shell with `date +%s` if needed). An instrument over ~200 s must be trimmed (r2-ch12r went from 237 s to 25 s by caching term enumeration at the call site).

## Close of chat 77

1. `rm -rf /home/claude/members/__pycache__` (delete-only call); `python3 members/gate.py bank r2-ch12t …` for each new instrument (writes r2-ch12t.out; refuses to overwrite).
2. Write /home/claude/W-114.md: begins `### W-114 —`, ends with a blank line; records the gate, each segment, the close estimate.
3. `python3 members/close.py --old /home/claude/The_Method_1_6_BUILD103_compendia_papers_audits.md --new /home/claude/The_Method_1_6_BUILD104_compendia_papers_audits.md --w /home/claude/W-114.md [--append DEFERRED.md /home/claude/deferred-add.md] --members members/READ-ch12t.md members/CENSUS-CLOSURES-ch12t.tsv members/r2-ch12t.py members/r2-ch12t.out …` — `--append` must precede `--members` (which consumes every later argument). It appends W-114 and the members, rewrites MANIFEST.tsv, asserts only WORKING-REGISTER.md, MANIFEST.tsv (and an appended member) changed, and must print `reverse recovers md5 fcf00e08efeaf4b43daa90d403fe1120  == old: True` before writing. Never edit a seated member in place.
4. HANDOFF-29 in this form (update: build numbers, md5s of the compendia bundle, MANIFEST.tsv, WORKING-REGISTER.md and DEFERRED.md, the member count, the run list, next work, the prompt). `ls -la /mnt/user-data/outputs` before copying; never copy over an existing file; present HANDOFF-29.md first, then BUILD104 and the READ files.
5. Handoff at 90–95 % of context or on a closed segment — never earlier, never mid-segment; begin the close when the remaining context would not fit a segment plus the close (≈ 5 % — INFERRED), and record the estimate in W-114. No corrections, no Register entries, no TASK 1 until the review closes.

## M's Drive actions

- **UPLOAD** to Materials (`1XX_5f3PZB6tjRtiZ2GIgd8Tt7i_4GgkY`): `HANDOFF-28.md` and `The_Method_1_6_BUILD103_compendia_papers_audits.md` (fcf00e08…).
- **RETIRE:** HANDOFF-27 and BUILD102 once BUILD103 gates in chat 77; HANDOFF-26, BUILD101 and any earlier compendia builds if still present.
- **KEEP:** BUILD90 main, tower-2.py, chat65/66/67-instruments.tar.gz, SWEEP-B-C-chat67.md, convert.py, the certificates, OWED-REGISTER-EXPANSIONS.md, OWED-EXPANSIONS-2.md, covers8.json, factor.py.

## Prompt for chat 77

"Chat 77. READ EVERYTHING BEFORE YOU DO ANYTHING. Live files: BUILD90 main (1,983,081 B, md5 49065309b0c4fe8e055f693aed295cca) and BUILD103 compendia (3,397,534 B, md5 fcf00e08efeaf4b43daa90d403fe1120, 40,226 lines, 246 members). List uploads, outputs and /home/claude first. Run HANDOFF-28's §0 gate in full and in order — fetch both bundles by title, bootstrap (decode, md5, extract), then gate.py census, run --core, manifest, run r2-ch12q r2-ch12r r2-ch12s, cert 77; any FAIL stops the chat with a report. Read RULINGS-R2.md and DEFERRED.md from the members. The standing block's Phase 0–4 (Löwdin/three-body) plan is executed carried state — discard it per Ruling 41; HANDOFF-27 is retired. Then continue Phase R2 at main §12.11.1.1 (L3177–3204), one or two subsections per segment, re-measuring every general claim on all cells or pairs with an r2-chNN.py that imports r2lib, closing each segment before the next. At close: bank each new instrument's golden with gate.py bank, write W-114, build BUILD104 with close.py (reverse must recover fcf00e08…), write HANDOFF-29. No corrections, no Register entries, no TASK 1 until the review closes. Handoff at 90–95 % of context or on a closed segment — never earlier, never mid-segment. Timeout on every call. Never copy over an existing file."
