# HANDOFF-84 — The Method 1.6 — chat 131 → chat 132

Slim form (RULINGS-R2.md chat-127 item 5): identity, gate, next work, Drive actions, prompt. **The repair docket, the standing
method and the conventions live in `DOCKET.md` (index + chat-128 … chat-131 deltas); the findings in the READ-chNN.md /
READ-intake1.md members and WORKING-REGISTER.md; the deferred items in DEFERRED.md; the rulings in RULINGS-R2.md.** Read all
four at open, last blocks first.

## Identity

- Written from **chat 131** for **chat 132**. Live files: **BUILD90 main** (unchanged since chat 62) and **BUILD162 compendia**
  (= BUILD161 + W-171 + DEF-131 + DOCKET chat-131 delta + six members). Register **1 to 1792**. W-171 IS seated; chat 132 seats
  nothing at open. No rulings were taken in chat 131; nothing was put to M.
- **BUILD162** `The_Method_1_6_BUILD162_compendia_papers_audits.md` **4,247,153 B · md5 1f081b1f605f74593e7ab76759c0a2aa ·
  53,438 lines · 249 members** (reverse recovered 2c8d3a9a…). ARCHIVE1 (5a5c0829…, 394 members) is NOT fetched at the gate.
- **Governing state** unchanged from HANDOFF-83: RUL-128 items 1–4, chat-81 cadence, chat-95 bar, chat-127 items 1, 2, 3, 5
  (executed), Register append-only, no silent change; the intake is executed (DOCKET item 38).
- **Main volume 84.8 % read (L10053 of 11,855). All thirty-six chapters CLOSED; Appendix A part 1 (opener, A.3, A.8–A.13)
  CLOSED** (READ-ch18a). Appendix A is split at `### A.15`; part 2 is the next unit.
- **MEASURED heading lines this chat, to be re-taken by your own scan:** `# APPENDICES` L9937; `## Appendix A` body L9939;
  `### A.15` L10054 · A.18 L10073 · A.19 L10091 · A.19.0 L10113 · A.19.1 L10153; `## Appendix B` L10165, C L10230, D L10320,
  E L10898, F L11222, G L11361, `## Index` L11409, `## References` L11503. PP `# APPENDICES` P9590; PP's A.15 is P9705 (its A.n
  headings are unmarked plain lines).

## §0 Gate (each step its own tool call under `timeout 280`; any FAIL stops the chat with a report)

1. `ls -la /mnt/user-data/uploads /mnt/user-data/outputs /home/claude`; `recent_chats` (n=3) confirms the latest chat is 131.
   Read `/mnt/project/CLAUDE.md` (project instruction; never a member).
2. Fetch both bundles by title: `Google Drive:search_files` with
   `title contains 'BUILD162_compendia' or title contains 'BUILD90_main'`, pageSize 5, excludeContentSnippets;
   `Google Drive:download_file_content` on each fileId; note the spill paths `/mnt/user-data/tool_results/<id>.json`.
3. Bootstrap (the only step outside gate.py), verbatim, with the two spill paths filled in:

```
cd /home/claude && timeout 280 python3 - <<'EOF'
import json, base64, hashlib, re, os
EXP={'main':'49065309b0c4fe8e055f693aed295cca','comp':'1f081b1f605f74593e7ab76759c0a2aa'}
NAME={'main':'/home/claude/The_Method_1_6_BUILD90_main_and_register.md','comp':'/home/claude/The_Method_1_6_BUILD162_compendia_papers_audits.md'}
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
   Expected: main 1,983,081 B · 18,470 lines; compendia **4,247,153 B · 53,438 lines**; **251 members extracted (2 + 249)**.
4. Fetch the Prints & Proofs original before step 7: folder `1vYctzLppUZ2vFPJDCZ6wvkgSdj3v_f6n`, fileId
   `1vsWwRT9BmUNeMrqokuo4jI4DJnoADubH`, **738,550 B · md5 49900cf41f818ab789bb90fc596ac977 · 11,371 lines**, decoded the same way
   to `/home/claude/PP_The_Method_1_6.md` (assert the md5 and `not os.path.exists`). r2-ch18a reads it at that path.
5. `gate.py census` → `OK census: DEFECT-CENSUS.tsv byte-identical` (1,556 rows + header, ≈ 15 s).
6. `gate.py run --core` → five `OK` (tower 976/1,654/2,535/13,585/70,905/199,130; kinds 1565 · 1356 · 499 · 149; minmax;
   r2-tools-constants; extent "1 to 1792").
7. `gate.py manifest` → `MANIFEST OK`; MANIFEST.tsv **16,844 B · d956604168a330a5885a6db6997b1b80 · 251 lines**;
   WORKING-REGISTER.md **832,891 B · b5251382b2bb9426540516bfb8a4be0d · 7,769 lines**, ends **W-171**; RULINGS-R2.md ends with
   the chat-128 block (unchanged); DEFERRED.md's last block is chat 131's; DOCKET.md ends with the chat-131 delta.
8. `gate.py run r2-ch18a r2-ch18b r2-ch17e r2-tb1` → four `OK` (r2-ch18a.out 20,364 B · d5b741a9 · 166 lines; r2-ch18b.out
   9,256 B · 0d29a486 · 70 lines). r2-ch18a needs PP on disk (step 4) and NumPy; r2-ch17e imports r2-tb1 (NumPy, SymPy).
9. `gate.py cert 132` → `/home/claude/GATE-ch132.txt`, verdict PASS only if every step passed.
10. `rm -rf /home/claude/members/__pycache__` — its own delete-only call, after every run or bank, never chained.

## Chat 132's work order (two segments; each closed before the next opens)

**Segment A — the R2 unit: Appendix A part 2, `### A.15` L10054 to `## Appendix B` L10165** (measure it: ≈ 111 lines — A.15
*Two bands, and only one of them is a sublattice*, A.18 *The triangle region is join-closed and meet-broken*, A.19 *The
seventeen generators, written out*, A.19.0, A.19.1). Instruments **r2-ch19a** (computable) and **r2-ch19b** (prose); import
from r2lib by path; copy `rbody`, `body_range` and `lettered` from r2-ch18a with provenance comments. Pre-PP: diff headings and
Statement lines against PP from P9705 (strip the section number from BOTH sides). Re-derive on the rebuilt lattice: A.15's two
bands and its 12,654 meet failures against r2-ch12y's 12,489 (DEF chat-70 carry: distinct regions); A.18's join-closed /
meet-broken triangle (r2-tb1's operator is upstream); A.19's seventeen generators against r2-ch18a §5's 17 join-irreducibles
of Λ₈ (name the convention: join-irreducible = covers exactly one element); A.19.0's alphabet and A.19.1's two counted sets as
DATA rows. Read the WARNING line on every Register entry a proof cites. Apply DOCKET.md's method throughout.

**Segment B — close:** bank both goldens; pycache delete-only; W-172 (ends with a blank line); DEF-132; DOCKET delta by
`--append`; close.py BUILD162 → BUILD163 (reverse must recover 1f081b1f…; `--append` before `--members`); HANDOFF-85 in this
form BEFORE the final verification; ≥ 8 calls left at the start. **Tool-call ceiling:** chat 131's first turn ran out of calls
mid-segment; budget the read so that both instruments bank inside the first turn, or close the segment as failed with diagnosis
and let M's *Continue* re-open the container (which persists within a chat).

**Standing after Appendix A:** Appendices B and C as prose, D–G as data (chat-127 item 1); the Index and References under
docket 36 (Xia and Routh on it; Rota and Birkhoff are in the body); then RUL-128 item 3's order — the Register WARNING sweep,
then the computable re-derivations (Chapter 34 re-take, docket 37, and the SCF chain first). The three-body project owes a reply
on intake1-01/-04 and 1756 (DEF-130 items 1, 5) — through M, when M chooses.

## Drive actions for M

- **Upload** to Materials (`1XX_5f3PZB6tjRtiZ2GIgd8Tt7i_4GgkY`): `HANDOFF-84.md` and
  `The_Method_1_6_BUILD162_compendia_papers_audits.md`.
- **Retire** once BUILD162 gates PASS in chat 132: HANDOFF-83 and BUILD161 (HANDOFF-82 and BUILD160 were due under HANDOFF-83).
- **Keep:** BUILD90 main (still live — no BUILD91 was built); BUILD124; ARCHIVE1 permanently; the Prints & Proofs folder; the
  certificates; OWED-REGISTER-EXPANSIONS.md; OWED-EXPANSIONS-2.md; covers8.json; factor.py; the two delivery zips in their
  subfolders.
- **When convenient:** DEF-130 items 1 and 5 to the three-body project; the pending bank to the Löwdin project (DEF-130 item 6).
  New this chat, for R3 (no action now): 14h-05's antiprotonic target choice now covers two sites (L6135, L10035).

## Prompt for chat 132

"Chat 132. READ EVERYTHING BEFORE YOU DO ANYTHING. Live files: BUILD90 main (1,983,081 B, md5
49065309b0c4fe8e055f693aed295cca) and BUILD162 compendia (4,247,153 B, md5 1f081b1f605f74593e7ab76759c0a2aa, 53,438 lines,
249 members); ARCHIVE1 (md5 5a5c0829fa234dde4f12ac240fc7dec4) is not fetched at the gate. List uploads, outputs and
/home/claude first. Run HANDOFF-84's §0 gate in full and in order — fetch both bundles by title, bootstrap with the script in
the handoff (decode, md5, extract, expect 251 files), fetch the Prints & Proofs original 'The Method 1.6.md' (738,550 B, md5
49900cf41f818ab789bb90fc596ac977) to /home/claude/PP_The_Method_1_6.md, then gate.py census, run --core, manifest, run
r2-ch18a r2-ch18b r2-ch17e r2-tb1, cert 132; any FAIL stops the chat with a report. Then read, last blocks first: RULINGS-R2.md
(the chat-128 block), DOCKET.md (index plus the chat-128 to chat-131 deltas), DEFERRED.md (chat 131's block is the last),
READ-ch18a.md. The standing block's Phase 0–4 Löwdin/three-body plan is executed carried state; discard it per Ruling 41; the
intake is executed too. Line numbers are MEMBER line numbers and are never carried between chats, nor is any count or heading
list. Work in two segments and close each before the next opens. Segment A: the R2 unit Appendix A part 2, from `### A.15`
to `## Appendix B`, measured by your own scan; instruments r2-ch19a computable and r2-ch19b prose, importing from r2lib by
path, copying nothing but rbody, body_range and lettered from r2-ch18a with provenance comments, reading MEMBERS never a
bundle path; the appendix is pre-PP — diff its headings and Statement lines against PP; re-derive every proved statement on
the rebuilt lattice or state the budget; read the WARNING line on every cited entry. Apply DOCKET.md's method throughout: name
every convention before scoring, Decimal not round(), a Register entry body is the first non-blank line after its heading, a
first-person probe carries mine and myself, a literal string is not a test, a count word counts DATA rows, a wrapped phrase is
read on the markup-stripped join, a | at line start is a table row only outside a code line, give every negative its witness,
record passes as well as failures, expect the instrument to be wrong before the book. Segment B: bank both goldens, pycache
delete-only and never chained, W-172 ending with a blank line, DEF-132, DOCKET delta by --append, close.py to BUILD163 with the
reverse guard, HANDOFF-85 in this form BEFORE the final verification, begin the close with at least eight tool calls left.
Handoff at 90–95 % of context or on a closed segment — never mid-segment. Timeout on every call. Never copy over an existing
file."
