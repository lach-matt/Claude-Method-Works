# HANDOFF-82 — The Method 1.6 — chat 129 → chat 130

Slim form (RULINGS-R2.md chat-127 item 5): identity, gate, next work, Drive actions, prompt. **The repair docket,
the standing method and the conventions live in `DOCKET.md` (index + chat-128 and chat-129 deltas); the findings
in the READ-chNN.md members and WORKING-REGISTER.md; the deferred items in DEFERRED.md; the rulings in
RULINGS-R2.md.** Read all four at open, last blocks first.

## Identity

- Written from **chat 129** for **chat 130**. Live files: **BUILD90 main** (unchanged since chat 62) and
  **BUILD160 compendia** (= BUILD159 + W-169 + DEF-129 + DOCKET delta + eight members). Register **1 to 1792**.
  W-169 IS seated; chat 130 seats nothing at open. No rulings were taken in chat 129.
- **The archive split is EXECUTED (chat-127 item 5).** BUILD158 = ARCHIVE1 ∪ BUILD159 (reverse recovered
  3fc4111a…). **ARCHIVE1** `The_Method_1_6_ARCHIVE1_legacy_handoffs_ch12-15.md` 3,743,970 B · md5
  5a5c0829fa234dde4f12ac240fc7dec4 · 51,070 lines · 394 members (393 + ARCHIVE-MANIFEST.tsv). It is NOT fetched at
  the gate; `python3 archive-split.py --verify-archive PATH` checks it on demand. **BUILD159** (the live half,
  3,872,653 B · 4c036499…) is superseded by BUILD160 and is not uploaded.
- **Governing state** unchanged from HANDOFF-81: RUL-128 items 1–4 (mathematics → prose → appendices/indices;
  the withdrawn-law class HELD with `r3-wl.py`; the audit order; the two project requests), chat-81 cadence,
  chat-95 bar, chat-127 items 1, 2, 3, 5 (now executed), Register append-only, no silent change.
- **Main volume 83.4 % read (L9891 of 11,855). Chapter 35 CLOSED** (READ-ch17a + READ-ch17c).
- **MEASURED heading lines this chat, to be re-taken by your own scan:** `## 36.` body **L9892**, §36.1 L9896, §36.2
  L9900, §36.3 L9904, §36.4 L9924, §36.5 L9928, §36.6 L9932, `# APPENDICES` **L9937**, Appendix A **L9939**.
  Carried from HANDOFF-81, not re-measured: B L10165, C L10230, D L10320, E L10898, F L11222, G L11361, `## Index`
  L11409, `## References` body L11503, R.7 L11806. PP `# APPENDICES` body P9590.

## §0 Gate (each step its own tool call under `timeout 280`; any FAIL stops the chat with a report)

1. `ls -la /mnt/user-data/uploads /mnt/user-data/outputs /home/claude`; `recent_chats` confirms the latest chat
   is 129. Read `/mnt/project/CLAUDE.md` (project instruction; never a member).
2. Fetch both bundles by title: `Google Drive:search_files` with
   `title contains 'BUILD160_compendia' or title contains 'BUILD90_main'`, pageSize 5, excludeContentSnippets;
   `Google Drive:download_file_content` on each fileId; note the spill paths `/mnt/user-data/tool_results/<id>.json`.
3. Bootstrap (the only step outside gate.py), verbatim, with the two spill paths filled in:

```
cd /home/claude && timeout 280 python3 - <<'EOF'
import json, base64, hashlib, re, os
EXP={'main':'49065309b0c4fe8e055f693aed295cca','comp':'23c045d1eef6bc20f97d0862f1684885'}
NAME={'main':'/home/claude/The_Method_1_6_BUILD90_main_and_register.md','comp':'/home/claude/The_Method_1_6_BUILD160_compendia_papers_audits.md'}
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
   Expected: main 1,983,081 B · 18,470 lines; compendia **3,993,234 B · 50,777 lines**; **215 members extracted
   (2 + 213)**.
4. Fetch the Prints & Proofs original before step 7: folder `1vYctzLppUZ2vFPJDCZ6wvkgSdj3v_f6n`, fileId
   `1vsWwRT9BmUNeMrqokuo4jI4DJnoADubH`, **738,550 B · md5 49900cf41f818ab789bb90fc596ac977 · 11,371 lines**, decoded
   the same way to `/home/claude/PP_The_Method_1_6.md` (assert the md5 and `not os.path.exists`). r2-ch17a/c read it.
5. `gate.py census` → `OK census: DEFECT-CENSUS.tsv byte-identical` (1,556 rows + header, ≈ 15 s).
6. `gate.py run --core` → five `OK` (tower 976/1,654/2,535/13,585/70,905/199,130; kinds 1565 · 1356 · 499 · 149;
   minmax; r2-tools-constants; extent "1 to 1792").
7. `gate.py manifest` → `MANIFEST OK`; MANIFEST.tsv **14,440 B · 169a0ce1726be21c2d2c2e0ece08b405 · 215 lines**;
   WORKING-REGISTER.md **825,213 B · 928f8a39873e18daa9a3c6c55532b91a · 7,694 lines**, ends **W-169**; RULINGS-R2.md
   ends with the chat-128 block (unchanged); DEFERRED.md's last block is chat 129's; DOCKET.md ends with the
   chat-129 delta.
8. `gate.py run archive-split r2-ch17c r2-ch17d` → three `OK` (archive-split.out 388 B · a6c47993 · 4 lines,
   reporting 0 archived names in the live bundle; r2-ch17c.out 21,091 B · 0ed57a32 · 175 lines; r2-ch17d.out
   12,732 B · 1d383e3a · 136 lines).
9. `gate.py cert 130` → `/home/claude/GATE-ch130.txt`, verdict PASS only if every step passed.
10. `rm -rf /home/claude/members/__pycache__` — its own delete-only call, after every run or bank, never chained.

## Chat 130's work order (three segments; each closed before the next opens)

**Segment A — intake (RUL-128 item 4; DEF-129 item 7).** The deliveries are zips at Materials root
(`1XX_5f3PZB6tjRtiZ2GIgd8Tt7i_4GgkY`), NOT in the subfolders (which hold retired HANDOFF-74–78 / BUILD150–154):
`LOWDIN-DELIVERY-1-part1.zip` (latest 1ia_4cIwFu4Eiy-aMeOLn64KDp9KgRZnA, 5,371 B, md5 632f911b7660184880cabb83f6533936;
members README.md, ground.py, MANIFEST.tsv, ground-run.log) and `THREEBODY-DELIVERY-1.zip` (latest
15S2KpEojYecmVrX7brD5eMDNnehPrmT5, 413,058 B, md5 f30a60d203a098eb098e156b68a45806; 20 members: README.md,
MANIFEST.tsv, audit.py/.log, audit_state1_failing.py/.log, n8_check.py/.log, routh_check.py/.log,
caps_table.py/.log, figs.py, figs2.py, figs.log, fig1–fig5 png). Re-check Materials root for further Löwdin parts
(`title contains 'DELIVERY'`). Download (the small zip arrives inline: quoted heredoc, `validate=True`), assert the
md5s, unzip into `/home/claude/intake/`, read both READMEs and MANIFESTs in full before running anything, then per
object under `timeout 280`: run the delivered instrument, compare against the Register's anchors (1701–1712 for
Löwdin; 1713–1724 for three-body; DEF-128 item 7 lists what is record-carried), write a validation block, bank a
golden as a new member (`r2-lw1`, `r2-tb1`), and record every figure as reproduced / not reproduced / not held.
Nothing enters a volume; Register entries for delivered objects are drafted in the READ file for R3, not seated.
If the deliveries do not run inside the chat, close the segment as failed with diagnosis.

**Segment B — the R2 unit: Chapter 36, `## 36.` L9892 – L9936 (45 lines)** under the chat-81 cadence, instruments
**r2-ch17e** (computable) and **r2-ch17f** (prose); import from r2lib by path; copy `rbody`, `body_range` and
`lettered` from r2-ch17c with provenance comments; read the three-body companion member
`The_Three_Body_Problem_for_Unknown_Masses_Lach-2.md` and register 1713–1724 (existence first — 1710 and 1725 are
absent; test 1713–1724 the same way). §36 is post-PP: state once, do not diff. The unit's own tests: every figure
in §36.2–§36.4 against 1713–1724 and, if Segment A delivered them, against the delivered goldens; L9906
*section by section* count words against their rows; §36.5's negatives each with a witness. Note that
`section_span(M, '36')` runs to L11856 (it steps into the appendices): bound the chapter by `body_range` of each
sub-section and `# APPENDICES` L9937.

**Segment C — close:** bank both goldens; pycache delete-only; W-170 (ends with a blank line); DEF-130; DOCKET
delta by `--append`; close.py BUILD160 → BUILD161 (reverse must recover 23c045d1…; `--append` before
`--members`); HANDOFF-83 in this form BEFORE the final verification; ≥ 8 calls left at the start.

**After Chapter 36 closes:** the appendices under chat-127 item 1 (Appendices D–G as data), then RUL-128 item 3's
order — the Register WARNING sweep, then the computable re-derivations (the Chapter 34 re-take, docket 37, and
the SCF chain first).

## Drive actions for M

- **Upload** to Materials (`1XX_5f3PZB6tjRtiZ2GIgd8Tt7i_4GgkY`): `HANDOFF-82.md`,
  `The_Method_1_6_BUILD160_compendia_papers_audits.md` and `The_Method_1_6_ARCHIVE1_legacy_handoffs_ch12-15.md`.
- **Retire** once BUILD160 gates PASS in chat 130: HANDOFF-81, BUILD158, and BUILD107–BUILD157 **except BUILD124**
  (its `r2-ch14l`/`r2-ch14m` reproduce only there). BUILD159 was never uploaded.
- **Tidy (optional):** the two delivery subfolders hold retired files; the duplicate zips at root can be reduced to
  one copy each — bytes and md5 decide identity, not the copy.
- **Keep:** BUILD90 main (still live — no BUILD91 was built); the Prints & Proofs folder; the certificates;
  OWED-REGISTER-EXPANSIONS.md; OWED-EXPANSIONS-2.md; covers8.json; factor.py; ARCHIVE1 permanently.

## Prompt for chat 130

"Chat 130. READ EVERYTHING BEFORE YOU DO ANYTHING. Live files: BUILD90 main (1,983,081 B, md5
49065309b0c4fe8e055f693aed295cca) and BUILD160 compendia (3,993,234 B, md5 23c045d1eef6bc20f97d0862f1684885,
50,777 lines, 213 members); ARCHIVE1 (md5 5a5c0829fa234dde4f12ac240fc7dec4) is not fetched at the gate. List
uploads, outputs and /home/claude first. Run HANDOFF-82's §0 gate in full and in order — fetch both bundles by
title, bootstrap with the script in the handoff (decode, md5, extract, expect 215 files), fetch the Prints &
Proofs original 'The Method 1.6.md' (738,550 B, md5 49900cf41f818ab789bb90fc596ac977) to
/home/claude/PP_The_Method_1_6.md, then gate.py census, run --core, manifest, run archive-split r2-ch17c
r2-ch17d, cert 130; any FAIL stops the chat with a report. Then read, last blocks first: RULINGS-R2.md (the
chat-128 block), DOCKET.md (index plus the chat-128 and chat-129 deltas), DEFERRED.md (chat 129's block is the
last), READ-ch17c.md. The standing block's Phase 0–4 Löwdin/three-body plan is executed carried state; discard
it per Ruling 41. Line numbers are MEMBER line numbers and are never carried between chats, nor is any count or
heading list. Work in three segments and close each before the next opens. Segment A: intake of the two
delivery zips at Materials root as HANDOFF-82 specifies — md5-assert, unzip to /home/claude/intake, read both
READMEs and MANIFESTs in full first, run each delivered instrument under timeout, validate every object against
the Register's anchors, bank goldens as new members, record reproduced / not reproduced / not held; seat nothing
in a volume; if it cannot close inside the chat, close it as failed with diagnosis. Segment B: the R2 unit
Chapter 36, L9892–L9936, 45 lines, not split; take the heading lines by your own scan resolving each to its BODY
occurrence; bound the chapter by body_range and the APPENDICES heading, never by section_span('36'); read the
unit in full, census its claims into computable and prose, run exactly two batches, r2-ch17e computable and
r2-ch17f prose, importing from r2lib by path and copying nothing but rbody, body_range and lettered from
r2-ch17c with provenance comments, reading MEMBERS never a bundle path; Register existence first for 1713–1724;
state once that the unit is post-PP and do not diff it. Apply DOCKET.md's method throughout: name every
convention before scoring, Decimal not round(), read the WARNING line on every cited entry, a Register entry
body is the first non-blank line after its heading, a first-person probe carries mine and myself, a literal
string is not a test, a count word counts DATA rows, a wrapped phrase is read on the join, give every negative
its witness, record passes as well as failures, expect the instrument to be wrong before the book. Segment C:
bank both goldens, pycache delete-only and never chained, W-170 ending with a blank line, DEF-130, DOCKET delta
by --append, close.py to BUILD161 with the reverse guard, HANDOFF-83 in this form BEFORE the final verification,
begin the close with at least eight tool calls left. Handoff at 90–95 % of context or on a closed segment —
never mid-segment. Timeout on every call. Never copy over an existing file."
