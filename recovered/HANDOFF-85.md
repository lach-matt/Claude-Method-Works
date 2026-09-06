# HANDOFF-85 — The Method 1.6 — chat 132 → chat 133

Slim form (RULINGS-R2.md chat-127 item 5): identity, gate, next work, Drive actions, prompt. **The repair docket, the standing
method and the conventions live in `DOCKET.md` (index + chat-128 … chat-132 deltas); the findings in the READ-chNN.md /
READ-intake1.md members and WORKING-REGISTER.md; the deferred items in DEFERRED.md; the rulings in RULINGS-R2.md.** Read all
four at open, last blocks first.

## Identity

- Written from **chat 132** for **chat 133**. Live files: **BUILD90 main** (unchanged since chat 62) and **BUILD163 compendia**
  (= BUILD162 + W-172 + DEF-132 + DOCKET chat-132 delta + six members). Register **1 to 1792**. W-172 IS seated; chat 133 seats
  nothing at open. No rulings were taken in chat 132; nothing was put to M.
- **BUILD163** `The_Method_1_6_BUILD163_compendia_papers_audits.md` **4,354,454 B · md5 599e1e3b6500a0a9c76d63c51e10a9b1 ·
  54,313 lines · 255 members** (reverse recovered 1f081b1f…). ARCHIVE1 (5a5c0829…, 394 members) is NOT fetched at the gate.
- **Governing state** unchanged from HANDOFF-84: RUL-128 items 1–4, chat-81 cadence, chat-95 bar, chat-127 items 1, 2, 3, 5
  (executed), Register append-only, no silent change; the intake is executed (DOCKET item 38).
- **Main volume 85.7 % read (L10164 of 11,855). All thirty-six chapters and Appendix A CLOSED** (READ-ch18a, READ-ch19a).
  Appendix B is the next unit.
- **MEASURED heading lines this chat, to be re-taken by your own scan:** `# APPENDICES` L9937; `## Appendix A` body L9939;
  `## Appendix B` L10165, C L10230, D L10320, E L10898, F L11222, G L11361, `## Index` L11409, `## References` L11503. PP
  `# APPENDICES` P9590; PP's `Appendix B` heading P9815 (its A.n headings were unmarked plain lines; check B's sub-headings).

## §0 Gate (each step its own tool call under `timeout 280`; any FAIL stops the chat with a report)

1. `ls -la /mnt/user-data/uploads /mnt/user-data/outputs /home/claude`; `recent_chats` (n=3) confirms the latest chat is 132.
   Read `/mnt/project/CLAUDE.md` (project instruction; never a member).
2. Fetch both bundles by title: `Google Drive:search_files` with
   `title contains 'BUILD163_compendia' or title contains 'BUILD90_main'`, pageSize 5, excludeContentSnippets;
   `Google Drive:download_file_content` on each fileId; note the spill paths `/mnt/user-data/tool_results/<id>.json`.
3. Bootstrap (the only step outside gate.py), verbatim, with the two spill paths filled in:

```
cd /home/claude && timeout 280 python3 - <<'EOF'
import json, base64, hashlib, re, os
EXP={'main':'49065309b0c4fe8e055f693aed295cca','comp':'599e1e3b6500a0a9c76d63c51e10a9b1'}
NAME={'main':'/home/claude/The_Method_1_6_BUILD90_main_and_register.md','comp':'/home/claude/The_Method_1_6_BUILD163_compendia_papers_audits.md'}
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
   Expected: main 1,983,081 B · 18,470 lines; compendia **4,354,454 B · 54,313 lines**; **257 members extracted (2 + 255)**.
4. Fetch the Prints & Proofs original before step 7: folder `1vYctzLppUZ2vFPJDCZ6wvkgSdj3v_f6n`, fileId
   `1vsWwRT9BmUNeMrqokuo4jI4DJnoADubH`, **738,550 B · md5 49900cf41f818ab789bb90fc596ac977 · 11,371 lines**, decoded the same way
   to `/home/claude/PP_The_Method_1_6.md` (assert the md5 and `not os.path.exists`). r2-ch18a and r2-ch19a/b read it at that path.
5. `gate.py census` → `OK census: DEFECT-CENSUS.tsv byte-identical` (1,556 rows + header, ≈ 12 s).
6. `gate.py run --core` → five `OK` (tower 976/1,654/2,535/13,585/70,905/199,130; kinds 1565 · 1356 · 499 · 149; minmax;
   r2-tools-constants; extent "1 to 1792").
7. `gate.py manifest` → `MANIFEST OK`; MANIFEST.tsv **17,248 B · ed5d0b66c5889fa568b408aa57b0a218 · 257 lines**;
   WORKING-REGISTER.md **835,658 B · 2925c3c87e033aa0cca27318adf2bc21 · 7,795 lines**, ends **W-172**; RULINGS-R2.md ends with
   the chat-128 block (unchanged); DEFERRED.md's last block is chat 132's; DOCKET.md ends with the chat-132 delta.
8. `gate.py run r2-ch19a r2-ch19b r2-ch18a r2-tb1` → four `OK` (r2-ch19a.out 21,844 B · a04625ba · 156 lines; r2-ch19b.out
   23,097 B · 170804d8 · 178 lines). r2-ch19a/b and r2-ch18a need PP on disk (step 4) and NumPy; r2-tb1 needs NumPy, SymPy.
9. `gate.py cert 133` → `/home/claude/GATE-ch133.txt`, verdict PASS only if every step passed.
10. `rm -rf /home/claude/members/__pycache__` — its own delete-only call, after every run or bank, never chained.

## Chat 133's work order (two segments; each closed before the next opens)

**Segment A — the R2 unit: Appendix B, `## Appendix B` L10165 to `## Appendix C` L10230** (measure it: ≈ 65 lines; read as
PROSE under chat-127 item 1, with every printed figure still re-taken on the rebuilt lattice or its budget stated). Instruments
**r2-ch20a** (computable) and **r2-ch20b** (prose); import from r2lib by path; copy `rbody`, `body_range` and `lettered` from
r2-ch19a with provenance comments. Pre-PP: diff headings and any Statement/Definition lines against PP from P9815 (strip the
section number from BOTH sides; PP's appendix sub-headings may be unmarked plain lines — scan, don't assume). Resolve every
pointer under both resolvers to the claim, not the heading; read the WARNING line on every Register entry cited; grep the Register
for a later entry naming the appendix before recording any figure as unreproducible. Apply DOCKET.md's method throughout,
including chat 132's new convention (a failing-meet count is an unordered pair on [0, cap]). If Appendix B is short enough,
Appendix C (L10230–L10319, ≈ 90 lines) may follow as a second read segment in the same chat, each with its own two instruments
and its own READ file — never split a unit across chats.

**Segment B — close:** bank the goldens; pycache delete-only; W-173 (ends with a blank line); DEF-133; DOCKET delta by
`--append`; close.py BUILD163 → BUILD164 (reverse must recover 599e1e3b…; `--append` before `--members`); HANDOFF-86 in this
form BEFORE the final verification; ≥ 8 calls left at the start. **Tool-call ceiling:** chat 132 banked both instruments at its
26th tool call and closed at its 40th — budget likewise; if calls run out mid-segment, close it as failed with diagnosis and let
M's *Continue* re-open the container (which persists within a chat).

**Standing after Appendix B:** Appendix C as prose, D–G as data (chat-127 item 1); the Index and References under docket 36
(Xia and Routh on it; Rota and Birkhoff are in the body); then RUL-128 item 3's order — the Register WARNING sweep, then the
computable re-derivations (Chapter 34 re-take, docket 37, and the SCF chain first). The three-body project owes a reply on
intake1-01/-04 and 1756 (DEF-130 items 1, 5) — through M, when M chooses.

## Drive actions for M

- **Upload** to Materials (`1XX_5f3PZB6tjRtiZ2GIgd8Tt7i_4GgkY`): `HANDOFF-85.md` and
  `The_Method_1_6_BUILD163_compendia_papers_audits.md`.
- **Retire** once BUILD163 gates PASS in chat 133: HANDOFF-84 and BUILD162 (HANDOFF-83 and BUILD161 were due under HANDOFF-84).
- **Keep:** BUILD90 main (still live — no BUILD91 was built); BUILD124; ARCHIVE1 permanently; the Prints & Proofs folder; the
  certificates; OWED-REGISTER-EXPANSIONS.md; OWED-EXPANSIONS-2.md; covers8.json; factor.py; the two delivery zips in their
  subfolders.
- **When convenient:** DEF-130 items 1 and 5 to the three-body project; the pending bank to the Löwdin project (DEF-130 item 6).
  New this chat, for R3 (no action now): §14.4 is a pre-PP two-line lead-in cited as the admissibility theorem at seven sites in
  two volumes (19a-02); A.15's *Register 230* is a wrong target (19a-01).

## Prompt for chat 133

"Chat 133. READ EVERYTHING BEFORE YOU DO ANYTHING. Live files: BUILD90 main (1,983,081 B, md5
49065309b0c4fe8e055f693aed295cca) and BUILD163 compendia (4,354,454 B, md5 599e1e3b6500a0a9c76d63c51e10a9b1, 54,313 lines,
255 members); ARCHIVE1 (md5 5a5c0829fa234dde4f12ac240fc7dec4) is not fetched at the gate. List uploads, outputs and
/home/claude first. Run HANDOFF-85's §0 gate in full and in order — fetch both bundles by title, bootstrap with the script in
the handoff (decode, md5, extract, expect 257 files), fetch the Prints & Proofs original 'The Method 1.6.md' (738,550 B, md5
49900cf41f818ab789bb90fc596ac977) to /home/claude/PP_The_Method_1_6.md, then gate.py census, run --core, manifest, run
r2-ch19a r2-ch19b r2-ch18a r2-tb1, cert 133; any FAIL stops the chat with a report. Then read, last blocks first: RULINGS-R2.md
(the chat-128 block), DOCKET.md (index plus the chat-128 to chat-132 deltas), DEFERRED.md (chat 132's block is the last),
READ-ch19a.md. The standing block's Phase 0–4 Löwdin/three-body plan is executed carried state; discard it per Ruling 41; the
intake is executed too. Line numbers are MEMBER line numbers and are never carried between chats, nor is any count or heading
list. Work in two segments and close each before the next opens. Segment A: the R2 unit Appendix B, from `## Appendix B` to
`## Appendix C`, measured by your own scan, read as prose under chat-127 item 1 with every printed figure re-taken; instruments
r2-ch20a computable and r2-ch20b prose, importing from r2lib by path, copying nothing but rbody, body_range and lettered from
r2-ch19a with provenance comments, reading MEMBERS never a bundle path; the appendix is pre-PP — diff its headings and any
Statement lines against PP from P9815; read the WARNING line on every cited entry; grep the Register for a later entry naming the
appendix before recording any figure as unreproducible. Apply DOCKET.md's method throughout: name every convention before
scoring, Decimal not round(), a Register entry body is the first non-blank line after its heading, a first-person probe carries
mine and myself, a literal string is not a test, a count word counts DATA rows, a wrapped phrase is read on the markup-stripped
join, a | at line start is a table row only outside a code line, a failing-meet count is an unordered pair on [0, cap], give every
negative its witness, record passes as well as failures, expect the instrument to be wrong before the book. Segment B: bank the
goldens, pycache delete-only and never chained, W-173 ending with a blank line, DEF-133, DOCKET delta by --append, close.py to
BUILD164 with the reverse guard, HANDOFF-86 in this form BEFORE the final verification, begin the close with at least eight tool
calls left. Handoff at 90–95 % of context or on a closed segment — never mid-segment. Timeout on every call. Never copy over an
existing file."
