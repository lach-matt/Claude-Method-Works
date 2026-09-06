# HANDOFF-83 — The Method 1.6 — chat 130 → chat 131

Slim form (RULINGS-R2.md chat-127 item 5): identity, gate, next work, Drive actions, prompt. **The repair docket,
the standing method and the conventions live in `DOCKET.md` (index + chat-128, chat-129 and chat-130 deltas); the
findings in the READ-chNN.md / READ-intake1.md members and WORKING-REGISTER.md; the deferred items in DEFERRED.md;
the rulings in RULINGS-R2.md.** Read all four at open, last blocks first.

## Identity

- Written from **chat 130** for **chat 131**. Live files: **BUILD90 main** (unchanged since chat 62) and
  **BUILD161 compendia** (= BUILD160 + W-170 + DEF-130 + DOCKET chat-130 delta + thirty members). Register
  **1 to 1792**. W-170 IS seated; chat 131 seats nothing at open. No rulings were taken in chat 130; nothing was put
  to M.
- **BUILD161** `The_Method_1_6_BUILD161_compendia_papers_audits.md` **4,158,576 B · md5
  2c8d3a9a51daa11d25cddb17b7c9c038 · 52,663 lines · 243 members** (reverse recovered 23c045d1…). ARCHIVE1
  (5a5c0829…, 394 members) is NOT fetched at the gate.
- **Governing state** unchanged from HANDOFF-82: RUL-128 items 1–4, chat-81 cadence, chat-95 bar, chat-127 items
  1, 2, 3, 5 (executed), Register append-only, no silent change. **The intake (RUL-128 item 4) is EXECUTED** —
  Löwdin object 3 and three-body objects 1–4, 7, 9 reproduced; the rest record-carried (DOCKET item 38, DEF-130
  item 6). The next deliveries, if any, follow the same intake (DEF-130 item 7).
- **Main volume 83.8 % read (L9936 of 11,855). All thirty-six chapters CLOSED** (Chapter 36: READ-ch17e). The
  appendices, the Index and the References remain.
- **MEASURED heading lines this chat, to be re-taken by your own scan:** `# APPENDICES` body **L9937**, Appendix A
  **L9939**, `## References` body L11503, R.7 L11806. Carried from HANDOFF-81, not re-measured: B L10165, C L10230,
  D L10320, E L10898, F L11222, G L11361, `## Index` L11409. PP `# APPENDICES` body P9590.

## §0 Gate (each step its own tool call under `timeout 280`; any FAIL stops the chat with a report)

1. `ls -la /mnt/user-data/uploads /mnt/user-data/outputs /home/claude`; `recent_chats` (n=3) confirms the latest
   chat is 130. Read `/mnt/project/CLAUDE.md` (project instruction; never a member).
2. Fetch both bundles by title: `Google Drive:search_files` with
   `title contains 'BUILD161_compendia' or title contains 'BUILD90_main'`, pageSize 5, excludeContentSnippets;
   `Google Drive:download_file_content` on each fileId; note the spill paths `/mnt/user-data/tool_results/<id>.json`.
3. Bootstrap (the only step outside gate.py), verbatim, with the two spill paths filled in:

```
cd /home/claude && timeout 280 python3 - <<'EOF'
import json, base64, hashlib, re, os
EXP={'main':'49065309b0c4fe8e055f693aed295cca','comp':'2c8d3a9a51daa11d25cddb17b7c9c038'}
NAME={'main':'/home/claude/The_Method_1_6_BUILD90_main_and_register.md','comp':'/home/claude/The_Method_1_6_BUILD161_compendia_papers_audits.md'}
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
   Expected: main 1,983,081 B · 18,470 lines; compendia **4,158,576 B · 52,663 lines**; **245 members extracted
   (2 + 243)**.
4. Fetch the Prints & Proofs original before step 7: folder `1vYctzLppUZ2vFPJDCZ6wvkgSdj3v_f6n`, fileId
   `1vsWwRT9BmUNeMrqokuo4jI4DJnoADubH`, **738,550 B · md5 49900cf41f818ab789bb90fc596ac977 · 11,371 lines**, decoded
   the same way to `/home/claude/PP_The_Method_1_6.md` (assert the md5 and `not os.path.exists`). r2-ch17f reads it.
5. `gate.py census` → `OK census: DEFECT-CENSUS.tsv byte-identical` (1,556 rows + header, ≈ 15 s).
6. `gate.py run --core` → five `OK` (tower 976/1,654/2,535/13,585/70,905/199,130; kinds 1565 · 1356 · 499 · 149;
   minmax; r2-tools-constants; extent "1 to 1792").
7. `gate.py manifest` → `MANIFEST OK`; MANIFEST.tsv **16,444 B · 8a391280a9ddbdecfc90f68f75cd5ceb · 245 lines**;
   WORKING-REGISTER.md **830,030 B · 10fff88265e54a54e29477565f5f0b71 · 7,742 lines**, ends **W-170**; RULINGS-R2.md
   ends with the chat-128 block (unchanged); DEFERRED.md's last block is chat 130's; DOCKET.md ends with the
   chat-130 delta.
8. `gate.py run r2-lw1 r2-tb1 r2-ch17e r2-ch17f` → four `OK` (r2-lw1.out 5,606 B · 94ce2246 · 65 lines; r2-tb1.out
   10,827 B · 7f79293d · 120 lines; r2-ch17e.out 12,178 B · d869dcce · 104 lines; r2-ch17f.out 7,740 B · 6daf47c5 ·
   69 lines). r2-tb1 runs the delivered `TB1-*.py` by subprocess (NumPy, SymPy required); r2-ch17e imports r2-tb1.
9. `gate.py cert 131` → `/home/claude/GATE-ch131.txt`, verdict PASS only if every step passed.
10. `rm -rf /home/claude/members/__pycache__` — its own delete-only call, after every run or bank, never chained.

## Chat 131's work order (two segments; each closed before the next opens)

**Segment A — the R2 unit: Appendix A, `## Appendix A — Proofs` L9939 to the next `## Appendix` heading** (measure
it: HANDOFF-81 carried B at L10165, so ≈ 226 lines — if the appendix is larger than one cadence unit, split at a
`### A.n` boundary by your own scan and read the first part whole; never split a section). Chat-127 item 1: Appendices
D–G are read as data; A–C as prose with their proofs re-derived where computable. Instruments **r2-ch18a**
(computable) and **r2-ch18b** (prose); import from r2lib by path; copy `rbody`, `body_range` and `lettered` from
r2-ch17e with provenance comments (`lettered` resolves `§A.n` — last hit = body; `heading_line` is numeric-only).
Appendix A is pre-PP: diff its headings and proof statements against PP (PP `# APPENDICES` body P9590; strip the
section number from BOTH sides of a heading comparison). Read the WARNING line on every Register entry a proof
cites; every proved statement re-derived on the rebuilt lattice (tower-2 by `r2lib.load_tower()`) or its budget stated.

**Segment B — close:** bank both goldens; pycache delete-only; W-171 (ends with a blank line); DEF-131; DOCKET delta
by `--append`; close.py BUILD161 → BUILD162 (reverse must recover 2c8d3a9a…; `--append` before `--members`);
HANDOFF-84 in this form BEFORE the final verification; ≥ 8 calls left at the start.

**Standing after the appendices:** the Index and References under docket 36 (Xia and Routh now on it), then
RUL-128 item 3's order — the Register WARNING sweep, then the computable re-derivations (the Chapter 34 re-take,
docket 37 — which now holds intake1-01 and intake1-04 — and the SCF chain first). The three-body project owes a
reply on intake1-01/-04 and 1756 (DEF-130 items 1, 5) — through M, when M chooses; not a question for chat 131.

## Drive actions for M

- **Upload** to Materials (`1XX_5f3PZB6tjRtiZ2GIgd8Tt7i_4GgkY`): `HANDOFF-83.md` and
  `The_Method_1_6_BUILD161_compendia_papers_audits.md`.
- **Retire** once BUILD161 gates PASS in chat 131: HANDOFF-82 and BUILD160. (BUILD107–BUILD158 except BUILD124 were
  already due for retirement under HANDOFF-82; BUILD159 was never uploaded.)
- **Keep:** BUILD90 main (still live — no BUILD91 was built); BUILD124; ARCHIVE1 permanently; the Prints & Proofs
  folder; the certificates; OWED-REGISTER-EXPANSIONS.md; OWED-EXPANSIONS-2.md; covers8.json; factor.py; the two
  delivery zips in their subfolders (the PNGs live only there — the bundle carries the text files).
- **For the three-body project (when convenient, not owed to chat 131):** DEF-130 items 1 and 5 — the absent 1756,
  the 13-label/12-ordering case dict, and the reconstructed constant term. **For the Löwdin project:** objects 1, 2,
  4–10, 12 remain pending their bank (DEF-130 item 6).

## Prompt for chat 131

"Chat 131. READ EVERYTHING BEFORE YOU DO ANYTHING. Live files: BUILD90 main (1,983,081 B, md5
49065309b0c4fe8e055f693aed295cca) and BUILD161 compendia (4,158,576 B, md5 2c8d3a9a51daa11d25cddb17b7c9c038,
52,663 lines, 243 members); ARCHIVE1 (md5 5a5c0829fa234dde4f12ac240fc7dec4) is not fetched at the gate. List
uploads, outputs and /home/claude first. Run HANDOFF-83's §0 gate in full and in order — fetch both bundles by
title, bootstrap with the script in the handoff (decode, md5, extract, expect 245 files), fetch the Prints &
Proofs original 'The Method 1.6.md' (738,550 B, md5 49900cf41f818ab789bb90fc596ac977) to
/home/claude/PP_The_Method_1_6.md, then gate.py census, run --core, manifest, run r2-lw1 r2-tb1 r2-ch17e
r2-ch17f, cert 131; any FAIL stops the chat with a report. Then read, last blocks first: RULINGS-R2.md (the
chat-128 block), DOCKET.md (index plus the chat-128, chat-129 and chat-130 deltas), DEFERRED.md (chat 130's block
is the last), READ-ch17e.md, READ-intake1.md. The standing block's Phase 0–4 Löwdin/three-body plan is executed
carried state; discard it per Ruling 41; the intake is executed too. Line numbers are MEMBER line numbers and are
never carried between chats, nor is any count or heading list. Work in two segments and close each before the
next opens. Segment A: the R2 unit Appendix A, from its `## Appendix A — Proofs` body heading to the next
`## Appendix` heading, measured by your own scan; if it exceeds one cadence unit, split at a `### A.n` boundary
and read the first part whole, never splitting a section; instruments r2-ch18a computable and r2-ch18b prose,
importing from r2lib by path, copying nothing but rbody, body_range and lettered from r2-ch17e with provenance
comments, reading MEMBERS never a bundle path; the appendix is pre-PP — diff its headings and proof statements
against PP; re-derive every proved statement on the rebuilt lattice or state the budget; read the WARNING line on
every cited entry. Apply DOCKET.md's method throughout: name every convention before scoring, Decimal not
round(), a Register entry body is the first non-blank line after its heading, a first-person probe carries mine
and myself, a literal string is not a test, a count word counts DATA rows, a wrapped phrase is read on the join,
give every negative its witness, record passes as well as failures, expect the instrument to be wrong before the
book. Segment B: bank both goldens, pycache delete-only and never chained, W-171 ending with a blank line, DEF-131,
DOCKET delta by --append, close.py to BUILD162 with the reverse guard, HANDOFF-84 in this form BEFORE the final
verification, begin the close with at least eight tool calls left. Handoff at 90–95 % of context or on a closed
segment — never mid-segment. Timeout on every call. Never copy over an existing file."
