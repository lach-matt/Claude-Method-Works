# HANDOFF-87 — The Method 1.6 — chat 134 → chat 135

Slim form (RULINGS-R2.md chat-127 item 5): identity, gate, next work, Drive actions, prompt. **The repair docket, the standing
method and the conventions live in `DOCKET.md` (index + chat-128 … chat-134 deltas); the findings in the READ-chNN.md /
READ-intake1.md members and WORKING-REGISTER.md; the deferred items in DEFERRED.md; the rulings in RULINGS-R2.md.** Read all
four at open, last blocks first.

## Identity

- Written from **chat 134** for **chat 135**. Live files: **BUILD90 main** (unchanged since chat 62) and **BUILD165 compendia**
  (= BUILD164 + W-174 + DEF-134 + DOCKET chat-134 delta + six members). Register **1 to 1792**. W-174 IS seated; chat 135 seats
  nothing at open. No rulings were taken in chat 134; nothing was put to M.
- **BUILD165** `The_Method_1_6_BUILD165_compendia_papers_audits.md` **4,545,822 B · md5 7049c21ebdaef17a2cbeb5b84ecb0fd6 ·
  55,933 lines · 267 members** (reverse recovered 390159e3…). ARCHIVE1 (5a5c0829…, 394 members) is NOT fetched at the gate.
- **Governing state** unchanged from HANDOFF-86: RUL-128 items 1–4, chat-81 cadence, chat-95 bar, chat-127 items 1, 2, 3, 5
  (executed), Register append-only, no silent change; the intake is executed (DOCKET item 38).
- **Main volume 87.0 % read (L10319 of 11,855). All thirty-six chapters, Appendices A, B and C CLOSED** (READ-ch21a). Appendix D
  is the next unit — **DATA under chat-127 item 1**, not prose.
- **MEASURED heading lines this chat, to be re-taken by your own scan:** `# APPENDICES` L9937; `## Appendix C` L10230; `## Appendix
  D` L10320; `## Appendix E` L10898; F L11222; G L11361; `## Index` L11409; `## References` L11503. PP `# Appendix C` P9877, `# Appendix
  D` P9967. Appendix D's sub-headings are marked (`### D.5.4` L10633, `### D.6` L10885 were seen in passing) — scan, don't assume.
- **Discipline note:** chat 134 banked both goldens at its 31st call (budget the 30th) and began the close at its 36th with the
  container intact. Budget stands: bank both instruments by the 30th call; begin the close by the 36th.

## §0 Gate (each step its own tool call under `timeout 280`; any FAIL stops the chat with a report)

1. `ls -la /mnt/user-data/uploads /mnt/user-data/outputs /home/claude`; `recent_chats` (n=3) confirms the latest chat is 134.
   Read `/mnt/project/CLAUDE.md` (project instruction; never a member).
2. Fetch both bundles by title: `Google Drive:search_files` with
   `title contains 'BUILD165_compendia' or title contains 'BUILD90_main'`, pageSize 5, excludeContentSnippets;
   `Google Drive:download_file_content` on each fileId; note the spill paths `/mnt/user-data/tool_results/<id>.json`.
3. Bootstrap (the only step outside gate.py), verbatim, with the two spill paths filled in:

```
cd /home/claude && timeout 280 python3 - <<'EOF'
import json, base64, hashlib, re, os
EXP={'main':'49065309b0c4fe8e055f693aed295cca','comp':'7049c21ebdaef17a2cbeb5b84ecb0fd6'}
NAME={'main':'/home/claude/The_Method_1_6_BUILD90_main_and_register.md','comp':'/home/claude/The_Method_1_6_BUILD165_compendia_papers_audits.md'}
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
   Expected: main 1,983,081 B · 18,470 lines; compendia **4,545,822 B · 55,933 lines**; **269 members extracted (2 + 267)**.
4. Fetch the Prints & Proofs original before step 7: folder `1vYctzLppUZ2vFPJDCZ6wvkgSdj3v_f6n`, fileId
   `1vsWwRT9BmUNeMrqokuo4jI4DJnoADubH`, **738,550 B · md5 49900cf41f818ab789bb90fc596ac977 · 11,371 lines**, decoded the same way
   to `/home/claude/PP_The_Method_1_6.md` (assert the md5 and `not os.path.exists`). r2-ch20a and r2-ch21a/b read it there.
5. `gate.py census` → `OK census: DEFECT-CENSUS.tsv byte-identical` (1,556 rows + header, ≈ 15 s).
6. `gate.py run --core` → five `OK` (tower 976/1,654/2,535/13,585/70,905/199,130; kinds 1565 · 1356 · 499 · 149; minmax;
   r2-tools-constants; extent "1 to 1792").
7. `gate.py manifest` → `MANIFEST OK`; MANIFEST.tsv **18,052 B · c4f540190799036d914a14deead3df70 · 269 lines**;
   WORKING-REGISTER.md **842,367 B · cd295a4a32ab55c5e76dce9430965846 · 7,853 lines**, ends **W-174**; RULINGS-R2.md ends with
   the chat-128 block (unchanged); DEFERRED.md's last block is chat 134's; DOCKET.md ends with the chat-134 delta.
8. `gate.py run r2-ch21a r2-ch21b r2-ch20a r2-tb1` → four `OK` (r2-ch21a.out 26,331 B · 74f4d9bd · 178 lines; r2-ch21b.out
   12,052 B · aee2c49f · 117 lines). r2-ch21a, r2-ch21b and r2-ch20a need PP on disk (step 4); r2-ch20a reads the project file
   `/mnt/project/COORDINATES-2_13.csv` (104,832 rows) — if absent it prints a BUDGET line and the golden will FAIL: report, don't rebank.
   r2-tb1 needs NumPy, SymPy.
9. `gate.py cert 135` → `/home/claude/GATE-ch135.txt`, verdict PASS only if every step passed.
10. `rm -rf /home/claude/members/__pycache__` — its own delete-only call, after every run or bank, never chained.

## Chat 135's work order (two segments; each closed before the next opens)

**Segment A — the R2 unit: Appendix D, `## Appendix D` L10320 to `## Appendix E` L10898** (measure it: ≈ 578 lines; read as **DATA**
under chat-127 item 1 — the appendix indexes the mathematics; every row's pointer is resolved under both resolvers to the claim, every
printed figure re-taken or its budget stated; the DATA-row set of each table is fixed and printed before any count word is scored; a
whitespace table's row carries a ≥ 3-space column gap, per the chat-134 convention). If the unit will not fit one chat with the close,
split it at a `### D.n` heading measured by your own scan, close the part, and never split a sub-section. Instruments **r2-ch22a**
(computable) and **r2-ch22b** (prose/pointers); import from r2lib by path; copy `rbody`, `body_range` and `lettered` from r2-ch21a with
provenance comments. Pre-PP: diff headings against PP from P9967 (strip the section number from BOTH sides; check whether PP's D.n
headings are marked or unmarked — scan). Read the WARNING line on every Register entry cited; grep the Register for a later entry naming
the appendix before recording any figure as unreproducible. Apply DOCKET.md's method throughout. Known twin sites inside the unit from
earlier reads: D.5.4 L10644 (30,000 — 21a-07), L10552 / L10590 (1,442 — 20a-01 family), L10571 / L10640 (4ν/3 — docket 11), L10549 / L10585
(order recovery, tree propagation), D.6 L10886 (20 of 20) — measure them as sites of those items, not as new findings.

**Segment B — close:** bank the goldens; pycache delete-only; W-175 (ends with a blank line); DEF-135; DOCKET delta by
`--append`; close.py BUILD165 → BUILD166 (reverse must recover 7049c21e…; `--append` before `--members`); HANDOFF-88 in this
form BEFORE the final verification; ≥ 8 calls left at the start. **Tool-call ceiling:** bank by the 30th; if calls run out
mid-segment, close it as failed with diagnosis and let M's *Continue* re-open the container (which persists within a chat).

**Standing after Appendix D:** E–G as data; the Index and References under docket 36 (Xia and Routh on it); then RUL-128 item 3's
order — the Register WARNING sweep (the 1,748-vs-1,738 datum of DEF-133 item 5 goes there), then the computable re-derivations
(Chapter 34 re-take, docket 37, and the SCF chain first; the Sc VI chain of 21a-02/-03 joins docket 37). The three-body project owes a
reply on intake1-01/-04 and 1756 (DEF-130 items 1, 5) — through M, when M chooses.

## Drive actions for M

- **Upload** to Materials (`1XX_5f3PZB6tjRtiZ2GIgd8Tt7i_4GgkY`): `HANDOFF-87.md` and
  `The_Method_1_6_BUILD165_compendia_papers_audits.md`.
- **Retire** once BUILD165 gates PASS in chat 135: HANDOFF-86 and BUILD164 (HANDOFF-85 and BUILD163 were due under HANDOFF-86).
- **Keep:** BUILD90 main (still live — no BUILD91 was built); BUILD124; ARCHIVE1 permanently; the Prints & Proofs folder; the
  certificates; OWED-REGISTER-EXPANSIONS.md; OWED-EXPANSIONS-2.md; covers8.json; factor.py; the two delivery zips in their
  subfolders; **the project file COORDINATES-2_13.csv (r2-ch20a's golden reads it).**
- **When convenient:** DEF-130 items 1 and 5 to the three-body project; the pending bank to the Löwdin project (DEF-130 item 6).
  New this chat, for R3 (no action now): Appendix C cites §24.2 three times for §22.2.1 / §25.2 material (21a-01); its 696,400
  quotation has no source sentence (21a-02); 735,091 / 735,092 narrate §25.6.4's withdrawn row (21a-03); 1,061 is superseded at
  §23.10.4 yet live at eight sites (21a-04); 1,442/1,442 stands against Register 783 (21a-05).

## Prompt for chat 135

"Chat 135. READ EVERYTHING BEFORE YOU DO ANYTHING. Live files: BUILD90 main (1,983,081 B, md5
49065309b0c4fe8e055f693aed295cca) and BUILD165 compendia (4,545,822 B, md5 7049c21ebdaef17a2cbeb5b84ecb0fd6, 55,933 lines,
267 members); ARCHIVE1 (md5 5a5c0829fa234dde4f12ac240fc7dec4) is not fetched at the gate. List uploads, outputs and
/home/claude first. Run HANDOFF-87's §0 gate in full and in order — fetch both bundles by title, bootstrap with the script in
the handoff (decode, md5, extract, expect 269 files), fetch the Prints & Proofs original 'The Method 1.6.md' (738,550 B, md5
49900cf41f818ab789bb90fc596ac977) to /home/claude/PP_The_Method_1_6.md, then gate.py census, run --core, manifest, run
r2-ch21a r2-ch21b r2-ch20a r2-tb1, cert 135; any FAIL stops the chat with a report. Then read, last blocks first: RULINGS-R2.md
(the chat-128 block), DOCKET.md (index plus the chat-128 to chat-134 deltas), DEFERRED.md (chat 134's block is the last),
READ-ch21a.md. The standing block's Phase 0–4 Löwdin/three-body plan is executed carried state; discard it per Ruling 41; the
intake is executed too. Line numbers are MEMBER line numbers and are never carried between chats, nor is any count or heading
list. Work in two segments and close each before the next opens. Segment A: the R2 unit Appendix D, from `## Appendix D` to
`## Appendix E`, measured by your own scan, read as DATA under chat-127 item 1 with every pointer resolved to the claim under both
resolvers and every printed figure re-taken; split at a `### D.n` heading of your own scan only if the whole will not fit with the
close, and never split a sub-section; instruments r2-ch22a computable and r2-ch22b prose, importing from r2lib by path, copying
nothing but rbody, body_range and lettered from r2-ch21a with provenance comments, reading MEMBERS never a bundle path; the
appendix is pre-PP — diff its headings against PP from P9967 (scan whether PP's D.n headings are marked); read the WARNING line on
every cited entry; grep the Register for a later entry naming the appendix before recording any figure as unreproducible. Apply
DOCKET.md's method throughout: name every convention before scoring, Decimal not round(), a Register entry body is the first
non-blank line after its heading, a first-person probe carries mine and myself and excludes the Roman numeral of a species, a
literal string is not a test, a count word counts DATA rows and the DATA-row set is fixed first, a whitespace table's DATA row
carries a ≥ 3-space column gap, a wrapped phrase is read on the markup-stripped join, a | at line start is a table row only outside a
code line, a numeral regex admits a trailing non-thousands comma, give every negative its witness, record passes as well as
failures, expect the instrument to be wrong before the book. Bank both instruments by the 30th tool call. Segment B: bank the
goldens, pycache delete-only and never chained, W-175 ending with a blank line, DEF-135, DOCKET delta by --append, close.py to
BUILD166 with the reverse guard, HANDOFF-88 in this form BEFORE the final verification, begin the close with at least eight tool
calls left. Handoff at 90–95 % of context or on a closed segment — never mid-segment. Timeout on every call. Never copy over an
existing file."
