# HANDOFF-80 — The Method 1.6 — chat 127 → chat 128 (REBUILT after the chat-127 rulings)

This rebuilt handoff supersedes the HANDOFF-80 presented earlier in chat 127; only this one is
uploaded. It is written in the slim form of RULINGS-R2.md chat-127 item 5: identity, gate, next
work, Drive actions, prompt. **The repair docket, the standing method and the conventions now live
in `DOCKET.md`; the findings live in the READ-chNN.md members and WORKING-REGISTER.md; the deferred
items in DEFERRED.md; the rulings in RULINGS-R2.md.** Read all four at open, last blocks first.

## Identity

- Written from **chat 127** for **chat 128**. Live files: **BUILD90 main** (unchanged since chat 62)
  and **BUILD157 compendia** (= BUILD156 + W-167 + the chat-127 RULINGS block + DOCKET.md +
  R3-CLASS-WL.md; BUILD156 was superseded before it was ever gated). Register **1 to 1792**. W-167
  IS seated; chat 128 seats nothing at open.
- **Governing state after chat 127's five rulings** (RULINGS-R2.md, last block; M verbatim
  *"Implement all 5 please, and then rebuild the handoff for the next chat"*): (1) Appendices D–G
  are censused as data; (2) the compendia are audited by class across six volumes — chat 113's
  scope question is CLOSED; (3) authoring runs in parallel with R2; (4) the chat-67 hold is lifted
  for the withdrawn-law class only; (5) handoff slimmed, bundle to be split. Everything else stands:
  the chat-81 cadence, the chat-95 bar (a finding is not a question; Prints & Proofs before any
  question), no other corrections, Register append-only, no silent change.
- **Chapter 34 is CLOSED** (chats 126–127). **Main volume 81.9 % read (L9715 of 11,855).**
- **MEASURED heading lines, to be re-taken by your own scan:** `## 35.` body **L9716**, §35.1
  **L9727**, §35.2 **L9744**, §35.3 **L9784**, §35.4 **L9806**, §35.5 **L9858**, §35.6 **L9872**,
  `## 36.` body **L9892**; `# APPENDICES` L9937; Appendix A L9939, B L10165, C L10230, D L10320,
  E L10898, F L11222, G L11361; `## Index` L11409; `## References` body L11503. Chapter 35 is
  L9716–L9891, 176 lines, above the band: **the R2 unit is L9716–L9805 (head, epigraph, §35.1–§35.3),
  90 lines**, cut at the end of §35.3; chat 129 takes §35.4–§35.6, L9806–L9891.

## §0 Gate (each step its own tool call under `timeout 280`; any FAIL stops the chat with a report)

1. `ls -la /mnt/user-data/uploads /mnt/user-data/outputs /home/claude`; `recent_chats` confirms the
   latest chat is 127. Read `/mnt/project/CLAUDE.md` (project instruction; never a member).
2. Fetch both bundles by title: `Google Drive:search_files` with
   `title contains 'BUILD157_compendia' or title contains 'BUILD90_main'`, pageSize 5,
   excludeContentSnippets; `Google Drive:download_file_content` on each fileId; note the two spill
   paths `/mnt/user-data/tool_results/<id>.json`.
3. Bootstrap (the only step outside gate.py):

```
timeout 280 python3 - <<'EOF'
import json, base64, hashlib, re, os
EXP={'main':'49065309b0c4fe8e055f693aed295cca','comp':'10d3b13cf0c3ce627c0f6624c7c08bc6'}
NAME={'main':'/home/claude/The_Method_1_6_BUILD90_main_and_register.md','comp':'/home/claude/The_Method_1_6_BUILD157_compendia_papers_audits.md'}
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
   **7,518,739 B · `10d3b13cf0c3ce627c0f6624c7c08bc6` · 99,290 lines**; **590 members extracted
   (2 + 588)**.
4. Fetch the Prints & Proofs original before step 7 — twenty-three banked instruments read it.
   Folder `1vYctzLppUZ2vFPJDCZ6wvkgSdj3v_f6n`, title `The Method 1.6.md`, fileId
   `1vsWwRT9BmUNeMrqokuo4jI4DJnoADubH`, **738,550 B · md5 49900cf41f818ab789bb90fc596ac977 ·
   11,371 lines**, written to `/home/claude/PP_The_Method_1_6.md` (decode as in step 3, assert the
   md5 and `not os.path.exists`).
5. `gate.py census` → `OK census: DEFECT-CENSUS.tsv byte-identical` (1,556 rows + header, ≈ 14 s).
6. `gate.py run --core` → five `OK` (tower 976/1,654/2,535/13,585/70,905/199,130; kinds
   1565 · 1356 · 499 · 149; minmax; r2-tools-constants; extent "1 to 1792").
7. `gate.py manifest` → `MANIFEST OK`; MANIFEST.tsv **39,537 B · 2b3f0931298e97eb4ce4a5f50acdc4fb
   · 590 lines**; WORKING-REGISTER.md **813,714 B · dff29aabf313e8c8e6a49eeadd04821a · 7,575
   lines**, ends **W-167**; RULINGS-R2.md now ends with the **chat-127 block (five rulings)**;
   DEFERRED.md **56 `##` headings / 55 chat blocks**, chat 127's last; DOCKET.md 12,247 B;
   r2lib.py 21,022 B · 580d2ea2 (unchanged); gate.py a01ef15a; close.py 98acae67 (note: `--comp`
   is gate.py's option, not close.py's).
8. `gate.py run r2-ch16y r2-ch16z` → two `OK` (r2-ch16y.out 15,307 B · 979f92ae · 174 lines;
   r2-ch16z.out 18,831 B · a41471e0 · 203 lines; r2-ch16z reads the Prints & Proofs path).
9. `gate.py cert 128` → `/home/claude/GATE-ch128.txt`, verdict PASS only if every step passed.
10. `rm -rf /home/claude/members/__pycache__` — its own delete-only call, after every run or bank.

## Chat 128's work order (three segments; each closed before the next opens)

**Segment A — the withdrawn-law repair (ruling 4).** Read `R3-CLASS-WL.md` in full. Put its
candidate wording to M as the chat's ONE question, four lines or fewer, and stop at the question
mark. On his word: enumerate every `1 to 1792` extent site across all six volumes with a sweep and
`register_cites.py`; apply the six status-sentence substitutions to the main member with build.py's
count-asserted SUBS; grow the Register member by entries 1793–1794 (M's wording governs); recompute
`kinds.py` and restate its table; drive the extent to a fixed point everywhere; reverse-md5 guard
`== old: True` before writing; write **BUILD91 main**; re-bank `r2-tools-constants` and `extent`
(their FAIL on the new extent is expected and is why they are re-banked in the same build); update
MANIFEST; verify by reading the new bundle. If the machinery does not close inside the chat, close
the segment as failed with diagnosis — never leave a half-built main bundle as live.

**Segment B — the R2 unit L9716–L9805** under the chat-81 cadence, instruments **r2-ch17a**
(computable) and **r2-ch17b** (prose). Before scoring anything Chapter 35 says about Chapter 34,
read DEF-127 item 1: L9718–L9721 and L9731–L9732 are members of 16z-01 and, after Segment A, are
repaired sites — measure them on BUILD91. The unit's own big tests, sighted and not measured: §35.2
*107 of 107 across Z = 2–108 … hence the 106 transitions Chapter 34 counted* (107 against 106 in one
sentence — name the convention; register 1446 puts the observational edge at Z = 102 and NIST's
listing at 108); *except at exactly La, Ac and Th* — three, against 1437's ten conditional-Madelung
misses and 1451's nineteen, reading both texts because the n+ℓ tie-break is a different rule;
*register entries 1701–1712 carry the record* — all twelve at their headlines, existence first;
c = 137.035999; §E.5's *nine things* counted at §E.5's body; *the twenty-two audits* against §3;
attributions Pulay 1969, Löwdin 1950, Griffin, Andrew and Cowan 1969/1971 against the References
BODY and R.7. The chained SCF walk of §35.1 is a different object from §34's ν walk. PP has no
Chapter 35 or 36 (`# APPENDICES` follows §34.10 at P9591): state once that the unit is post-PP
authoring and do not diff it. The NIST table lives in r2-ch16y.py §3, validated — import it by
path, never retype it, and label anything computed from it a reconstruction.

**Segment C — close:** bank both goldens; pycache delete-only; W-168 (ends with a blank line);
DEF-128; **rewrite DOCKET.md where the chat moved an item** (it is a normal member — pass the new
copy through `--members` only if close.py accepts a replacement; if it refuses an existing name,
grow it with `--append DOCKET.md DOCKET-delta.md` and note the choice in W-168); close.py from
BUILD157 to BUILD158 (reverse must recover `10d3b13c…`; `--append` before `--members`); HANDOFF-81
in this slim form BEFORE the final verification; ≥ 8 calls left at the start of the close.

**Chat 129 opens with the archive split (ruling 5),** after its gate on BUILD158: partition
MEASURED in W-167 — archive = the 48 legacy `HANDOFF-*.md` + `r2-ch12*…r2-ch15*` instruments and
goldens + `READ-ch1[2-5]*` and `CENSUS-CLOSURES-ch1[2-5]*` (393 members, 3.7 MB); live = the rest
(193 members). Write the archive bundle first, the live bundle second, each with its own manifest
and reverse-recovery guard; gate.py must then verify the live bundle alone and the archive by md5
on demand; record both identities in W-169 and HANDOFF-82. Standing archive reads: `r2-ch14l.out`
(§23.9.1's eight V values) and BUILD124's reproducing instruments.

**After the main volume closes (about 16 sessions at the measured 116 lines/session; fewer with
ruling 1):** the compendia by class in ruling 2's order, the Register WARNING sweep first.

## The authoring track (ruling 3) — M writes, the audit verifies, the build seats

- **To author:** §14.5.2–§14.5.7 (six heading-only sections, forty citations; DOCKET item 1 gives
  the citation order and the settled material — seed(Λ₈) = 7, register 573 for §14.5.6); §2.22
  (urgent), §28.7.6, §28.9; the Chapter 34 rewrite (registers 1437, 1445, 1460, 1465, 1470 hold the
  corrected content; R3-CLASS-WL.md holds the status sentences that go in first).
- **Entry condition:** authored text is uploaded to Materials as `AUTH-<section>.md`; a chat
  censuses it in two kinds and instruments it (every figure recomputed) BEFORE seating; it enters a
  volume only through a guarded build with a Register entry in the same build. Authored prose is
  never edited by Claude; deviations found in it are flagged back to M.

## Drive actions for M

- **Upload** to Materials (`1XX_5f3PZB6tjRtiZ2GIgd8Tt7i_4GgkY`): **this** `HANDOFF-80.md` and
  `The_Method_1_6_BUILD157_compendia_papers_audits.md`. Do NOT upload the earlier HANDOFF-80 or
  BUILD156 presented in chat 127 (both superseded); if BUILD156 was uploaded, retire it.
- **Retire** once BUILD157 gates PASS in chat 128: HANDOFF-79, BUILD155, BUILD156 and BUILD107–
  BUILD154 **except BUILD124** (its `r2-ch14l`/`r2-ch14m` reproduce only there).
- **Keep:** BUILD90 main until BUILD91 gates PASS, then retire it; the Prints & Proofs folder
  (`1vYctzLppUZ2vFPJDCZ6wvkgSdj3v_f6n`), the authentication baseline read by twenty-three banked
  instruments; the certificates; OWED-REGISTER-EXPANSIONS.md; OWED-EXPANSIONS-2.md; covers8.json;
  factor.py.

## Prompt for chat 128

"Chat 128. READ EVERYTHING BEFORE YOU DO ANYTHING. Live files: BUILD90 main (1,983,081 B, md5
49065309b0c4fe8e055f693aed295cca) and BUILD157 compendia (7,518,739 B, md5
10d3b13cf0c3ce627c0f6624c7c08bc6, 99,290 lines, 588 members). List uploads, outputs and /home/claude
first. Run HANDOFF-80's §0 gate in full and in order — fetch both bundles by title, bootstrap
(decode, md5, extract, expect 590 files), fetch the Prints & Proofs original 'The Method 1.6.md'
(738,550 B, md5 49900cf41f818ab789bb90fc596ac977) to /home/claude/PP_The_Method_1_6.md, then gate.py
census, run --core, manifest, run r2-ch16y r2-ch16z, cert 128; any FAIL stops the chat with a
report. Then read, last blocks first: RULINGS-R2.md (the chat-127 block carries five rulings — the
chat-95 bar still governs: a finding is not a question, deviations are recorded and flagged, never
put to M), DOCKET.md (the repair docket, the standing method and every convention — it replaces the
handoff's docket), DEFERRED.md (chat 127's block is the last of fifty-five), READ-ch16z.md, and
R3-CLASS-WL.md. The standing block's Phase 0–4 Löwdin/three-body plan is executed carried state;
discard it per Ruling 41 (W-118). Line numbers are MEMBER line numbers and are never carried between
chats, nor is any count or heading list. Work in three segments and close each before the next
opens. Segment A: put R3-CLASS-WL.md's candidate wording to M once, in four lines or fewer, and stop
at the question mark; on his word execute the withdrawn-law repair as the file specifies — extent
sites enumerated first, count-asserted substitutions, Register entries 1793–1794 in his wording, the
kinds table recomputed, the extent driven to a fixed point in all six volumes, reverse-md5 guard,
BUILD91 main, the extent and r2-tools-constants goldens re-banked in the same build, verified by
reading the new bundle; if it cannot close inside the chat, close it as failed with diagnosis and
leave BUILD90 live. Segment B: the R2 unit L9716–L9805, the Chapter 35 head, epigraph and
§35.1–§35.3, 90 lines, cut at the end of §35.3, not split; take the heading lines by your own scan
resolving each to its BODY occurrence; resolve every pointer under both body_range and section_span
and bound the unit by body_range; read the unit in full, census its claims into computable and
prose, run exactly two batches, r2-ch17a computable and r2-ch17b prose, importing heading_line,
section_span, has_token, enclosing, Rset, L8_at and is_tree from r2lib by path and the NIST table
from r2-ch16y.py §3 by path, copying nothing, passing the resolvers the LINE LIST, reading MEMBERS
never a bundle path; measure the unit's own claims listed in HANDOFF-80 Segment B; treat L9718–L9721
and L9731–L9732 as members of 16z-01 repaired in Segment A; state once that the unit is post-PP and
do not diff it. Apply DOCKET.md's method throughout: name every convention before scoring, Decimal
not round(), read the WARNING line on every cited entry, a first-person probe carries mine and
myself, a literal string is not a test, a count word counts DATA rows, give every negative its
witness, record passes as well as failures, expect the instrument to be wrong before the book.
Segment C: bank both goldens, pycache delete-only, W-168 ending with a blank line, DEF-128, DOCKET.md
rewritten where an item moved, close.py from BUILD157 to BUILD158 with reverse recovering 10d3b13c…,
HANDOFF-81 in this slim form BEFORE the final verification, begin the close with at least eight tool
calls left. Handoff at 90–95% of context or on a closed segment — never mid-segment. Timeout on
every call. Delete-only calls for pycache, never chained. Never copy over an existing file."
