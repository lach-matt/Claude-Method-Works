# HANDOFF-91 — The Method 1.6 — chat 138 → chat 139

Slim form (RULINGS-R2.md chat-127 item 5): identity, gate, next work, Drive actions, prompt. **The repair docket, the standing
method and the conventions live in `DOCKET.md` (index + chat-128 … chat-138 deltas); the findings in the READ-chNN.md /
READ-intake1.md members and WORKING-REGISTER.md; the deferred items in DEFERRED.md; the rulings in RULINGS-R2.md.** Read all
four at open, last blocks first.

## Identity

- Written from **chat 138** for **chat 139**. Live files: **BUILD90 main** (unchanged since chat 62) and **BUILD169 compendia**
  (= BUILD168 + W-178 + DEF-138 + DOCKET chat-138 delta + six members). Register **1 to 1792**. W-178 IS seated; chat 139 seats
  nothing at open. No rulings were taken in chat 138; nothing was put to M.
- **BUILD169** `The_Method_1_6_BUILD169_compendia_papers_audits.md` **4,877,851 B · md5 92f26e130032af5368dede03d5ddb6a8 ·
  58,535 lines · 291 members** (reverse recovered 78daa717…). ARCHIVE1 (5a5c0829…, 394 members) is NOT fetched at the gate.
- **Governing state** unchanged from HANDOFF-90: RUL-128 items 1–4, chat-81 cadence, chat-95 bar, chat-127 items 1, 2, 3, 5
  (executed), Register append-only, no silent change; the intake is executed (DOCKET item 38).
- **Main volume 94.6 % read (L11221 of 11,855). All thirty-six chapters and Appendices A–E CLOSED** (READ-ch25a: eleven
  findings — item R has no E.3 entry; *§32.2 asserted |Q| = 7* has no §32.2 site; E.4.1 / E.4.2 say *thirteen* beside fourteen rows;
  §30.3.5 → §30.3.8 for realisability; E.7's *§2.10 … now does* is false; *Sixty-odd from §30.3 alone* vs 17 + 40 shared with §32.2;
  two of item C's four vocabulary terms not at §29.7; *six independent tests* single witness; E.6 ↔ §30.3.9 mutual citation. K, M, N,
  O's coordinates are printed nowhere in Appendix E — 24a-05 stays on docket 37 / 38). **Appendix F is the next unit — from
  `## Appendix F` L11222, DATA under chat-127 item 1.**
- **MEASURED heading lines this chat, to be re-taken by your own scan:** `## Appendix F` L11222 (a list hit at L168 is excluded);
  `### F.3` L11278, `### F.3.1` L11301 (no F.3.2 / F.3.3 — 24b-05); F.4.3 exists (L11762 *#P-complete*, 24b-06); `## Appendix G`
  and `## References` L11503 (the LAST `References` hit; the first is the contents list) bound what follows. Measure Appendix F
  whole first; if over ≈ 250 lines with the close, **split at a `### F.n` heading by your own scan before reading**. PP
  `# Appendix F` P10761; PP's sub-headings are unmarked and may lack the blank line above or carry a leading space — probe
  `^\s*(#{1,4}\s*)?F\.n\s+[A-Z]` and read the hits (r2-ch25b §0 shows the method).
- **Discipline note:** chat 138 banked at the 36th and 41st calls (gate 15, governing reads 5, scan 1, read 2, sources 3,
  instruments with four self-caught faults 12). Budget for chat 139: bank both instruments by the 30th call; begin the close by the
  36th. Read every census row's class and detail BEFORE writing its verdict. A section's rows may be question paragraphs (a
  paragraph start is a non-blank line after a blank OR after the heading); a fraction may be printed in words — probe both forms.

## §0 Gate (each step its own tool call under `timeout 280`; any FAIL stops the chat with a report)

1. `ls -la /mnt/user-data/uploads /mnt/user-data/outputs /home/claude`; `recent_chats` (n=3) confirms the latest chat is 138.
   Read `/mnt/project/CLAUDE.md` (project instruction; never a member).
2. Fetch both bundles by title: `Google Drive:search_files` with
   `title contains 'BUILD169_compendia' or title contains 'BUILD90_main'`, pageSize 5, excludeContentSnippets;
   `Google Drive:download_file_content` on each fileId; note the spill paths `/mnt/user-data/tool_results/<id>.json`.
3. Bootstrap (the only step outside gate.py), verbatim, with the two spill paths filled in:

```
cd /home/claude && timeout 280 python3 - <<'EOF'
import json, base64, hashlib, re, os
EXP={'main':'49065309b0c4fe8e055f693aed295cca','comp':'92f26e130032af5368dede03d5ddb6a8'}
NAME={'main':'/home/claude/The_Method_1_6_BUILD90_main_and_register.md','comp':'/home/claude/The_Method_1_6_BUILD169_compendia_papers_audits.md'}
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
   Expected: main 1,983,081 B · 18,470 lines; compendia **4,877,851 B · 58,535 lines**; **293 members extracted (2 + 291)**.
4. Fetch the Prints & Proofs original before step 7: folder `1vYctzLppUZ2vFPJDCZ6wvkgSdj3v_f6n`, fileId
   `1vsWwRT9BmUNeMrqokuo4jI4DJnoADubH`, **738,550 B · md5 49900cf41f818ab789bb90fc596ac977 · 11,371 lines**, decoded the same way
   to `/home/claude/PP_The_Method_1_6.md` (assert the md5 and `not os.path.exists`). r2-ch25a, r2-ch25b, r2-ch24b read it there.
5. `gate.py census` → `OK census: DEFECT-CENSUS.tsv byte-identical` (1,556 rows + header, ≈ 14 s).
6. `gate.py run --core` → five `OK` (tower 976/1,654/2,535/13,585/70,905/199,130; kinds 1565 · 1356 · 499 · 149; minmax;
   r2-tools-constants; extent "1 to 1792").
7. `gate.py manifest` → `MANIFEST OK`; MANIFEST.tsv **19,657 B · 5d7068c4ad91b52c177774aebe16213f · 293 lines**;
   WORKING-REGISTER.md **855,509 B · 317be90d89e3ef4ff75fb8fb3b0adbdc · 7,881 lines**, ends **W-178**; RULINGS-R2.md ends with
   the chat-128 block (unchanged); DEFERRED.md's last block is chat 138's; DOCKET.md ends with the chat-138 delta.
8. `gate.py run r2-ch25a r2-ch25b r2-ch24a r2-ch24b` → four `OK` (r2-ch25a.out 12,009 B · 9c68ffc6 · 90 lines, ≈ 18 s — needs
   PP on disk and tower-2.py; r2-ch25b.out 20,682 B · acf7ca5a · 175 lines, 1 s, needs PP; r2-ch24a 1 s; r2-ch24b 1 s, needs PP).
   r2-ch23a / r2-ch22a (NumPy, SymPy), r2-ch23b (175 s) and r2-ch22b are not in the run list this chat; r2-ch20a (the
   COORDINATES-2_13.csv golden) neither — the project file must stay.
9. `gate.py cert 139` → `/home/claude/GATE-ch139.txt`, verdict PASS only if every step passed.
10. `rm -rf /home/claude/members/__pycache__` — its own delete-only call, after every run or bank, never chained.

## Chat 139's work order (two segments; each closed before the next opens)

**Segment A — the R2 unit: Appendix F, `## Appendix F` L11222 to `## Appendix G` (heading lines to be re-taken; measure the
appendix and its sub-headings first; split at a `### F.n` heading before reading if it will not fit with the close; read as
**DATA** under chat-127 item 1).** Appendix F is *The numbers, indexed*: every printed figure re-taken on the rebuilt tower or
located at its source section under both resolvers with its home heading; every table's DATA-row set fixed and printed first (a
`|` at line start is a table row only outside a code line; a whitespace row parsed on ≥ 2 spaces where ≥ 3 changes the column
count, printed); every count word re-taken; every status / withdrawn marker tested against the entry it restates and that entry's
WARNING line (grep the Register for a later entry naming Appendix F before recording any figure as unreproducible); F.3's
sub-sections against Register 371 (24b-05: *F.3.3* → *F.3.1* at three E.1 sites; does F.3.1 carry *nine stable cells* / *a count
… cannot be printed as prose*?); F.4.3's *#P-complete* (24b-06); §12.11.3.1's *assert the law, compute the extent* re-probe on
its own words; the 20a-01 / 21a-04 / 16z-01 figures (1,105 / 1,442 / 1,061 / Chapter 34's) wherever Appendix F prints them,
against the Register's WARNING lines (1309, 1350, 1401, 1403, 1461) and docket 35. Instruments **r2-ch26a** (computable) and
**r2-ch26b** (prose / pointers); import from r2lib by path; copy `rbody`, `body_range`, `lettered` from r2-ch25a with
provenance comments; read MEMBERS never a bundle path. Pre-PP: diff headings against PP from P10761 (strip the section number
from BOTH sides). Apply DOCKET.md's method throughout.

**Segment B — close:** bank the goldens; pycache delete-only; W-179 (ends with a blank line); DEF-139; DOCKET delta by
`--append`; close.py BUILD169 → BUILD170 (reverse must recover 92f26e13…; `--append` before `--members`); HANDOFF-92 in this
form BEFORE the final verification; ≥ 8 calls left at the start. **Tool-call ceiling:** if calls run out mid-segment, close it as
failed with diagnosis and let M's *Continue* re-open the container (which persists within a chat).

**Standing after Appendix F:** G as data; the Index and References under docket 36 (Xia, Routh, Fourier, Motzkin, Gröbner on
it); then RUL-128 item 3's order — the Register WARNING sweep (the 1,748-vs-1,738 datum of DEF-133 item 5; Register 219–221 /
305 / 239 / 256 headings of 23b-03 / 24b-03 join it), then the computable re-derivations (Chapter 34 re-take, docket 37, and the
SCF chain first; the Sc VI chain of 21a-02/-03 with E.3's bracket site, the Appendix-D reconstruction ledger 23a-03, Appendix E's
256-code ledger 24a-05 with its coordinates unprinted, §23.10's 499 / 518, §28.7.4's forty for 25b-03 join docket 37). The
three-body project owes a reply on intake1-01/-04 and 1756 (DEF-130 items 1, 5) — through M, when M chooses.

## Drive actions for M

- **Upload** to Materials (`1XX_5f3PZB6tjRtiZ2GIgd8Tt7i_4GgkY`): `HANDOFF-91.md` and
  `The_Method_1_6_BUILD169_compendia_papers_audits.md`.
- **Retire** once BUILD169 gates PASS in chat 139: HANDOFF-90 and BUILD168 (HANDOFF-89 and BUILD167 were due under HANDOFF-90).
- **Keep:** BUILD90 main (still live — no BUILD91 was built); BUILD124; ARCHIVE1 permanently; the Prints & Proofs folder; the
  certificates; OWED-REGISTER-EXPANSIONS.md; OWED-EXPANSIONS-2.md; covers8.json; factor.py; the two delivery zips in their
  subfolders; **the project file COORDINATES-2_13.csv (r2-ch20a's golden reads it).**
- **When convenient:** DEF-130 items 1 and 5 to the three-body project; the pending bank to the Löwdin project (DEF-130 item 6).
  New this chat, for R3 (no action now): item R needs an E.3 entry (25a-01); E.4.1's *§32.2* pointer (25a-02); E.7 asserts a
  change §2.10 never received (25b-02); E.8's *sixty-odd* (25b-03).

## Prompt for chat 139

"Chat 139. READ EVERYTHING BEFORE YOU DO ANYTHING. Live files: BUILD90 main (1,983,081 B, md5
49065309b0c4fe8e055f693aed295cca) and BUILD169 compendia (4,877,851 B, md5 92f26e130032af5368dede03d5ddb6a8, 58,535 lines,
291 members); ARCHIVE1 (md5 5a5c0829fa234dde4f12ac240fc7dec4) is not fetched at the gate. List uploads, outputs and
/home/claude first. Run HANDOFF-91's §0 gate in full and in order — fetch both bundles by title, bootstrap with the script in
the handoff (decode, md5, extract, expect 293 files), fetch the Prints & Proofs original 'The Method 1.6.md' (738,550 B, md5
49900cf41f818ab789bb90fc596ac977) to /home/claude/PP_The_Method_1_6.md, then gate.py census, run --core, manifest, run
r2-ch25a r2-ch25b r2-ch24a r2-ch24b, cert 139; any FAIL stops the chat with a report. Then read, last blocks first:
RULINGS-R2.md (the chat-128 block), DOCKET.md (index plus the chat-128 to chat-138 deltas), DEFERRED.md (chat 138's block is the
last), READ-ch25a.md. The standing block's Phase 0–4 Löwdin/three-body plan is executed carried state; discard it per Ruling 41;
the intake is executed too. Line numbers are MEMBER line numbers and are never carried between chats, nor is any count or
heading list. Work in two segments and close each before the next opens. Segment A: the R2 unit Appendix F, from `## Appendix F`
to `## Appendix G`, measured by your own scan at the first read call (split at a `### F.n` heading before reading if it will not
fit with the close), read as DATA under chat-127 item 1 with every printed figure re-taken on the rebuilt tower or located at its
source under both resolvers with its home heading, every table's DATA-row set fixed and printed first, every count word re-taken,
every status or withdrawn marker tested against its entry and that entry's WARNING line, F.3's sub-sections against Register 371
(24b-05) and F.4.3's #P-complete (24b-06), the 1,105 / 1,442 / 1,061 / Chapter 34 figures against the Register's WARNING lines
wherever Appendix F prints them; instruments r2-ch26a computable and r2-ch26b prose, importing from r2lib by path, copying nothing
but rbody, body_range and lettered from r2-ch25a with provenance comments, reading MEMBERS never a bundle path; the appendix is
pre-PP — diff its headings against PP from P10761 (PP's sub-headings are unmarked, may lack the blank line above or carry a
leading space); read the WARNING line on every cited entry; grep the Register for a later entry naming the appendix before
recording any figure as unreproducible. Apply DOCKET.md's method throughout: name every convention before scoring, Decimal not
round(), a Register entry body is the first non-blank line after its heading, a first-person probe carries mine and myself and
excludes the Roman numeral of a species, a literal string is not a test, a count word counts DATA rows and the DATA-row set is
fixed first, a paragraph start is a non-blank line after a blank or after the heading, a fraction may be printed in words, a
whitespace table row is parsed on a ≥ 2-space split where the ≥ 3-space split changes the column count and the difference is
printed, a tie or constraining count names its quantifier or test, a wrapped phrase is read on the markup-stripped join, a | at
line start is a table row only outside a code line, a numeral regex admits a trailing non-thousands comma, `## References` is
the LAST heading hit not the first, read every census row's class and detail before writing its verdict, give every negative its
witness, record passes as well as failures, expect the instrument to be wrong before the book. Bank both instruments by the 30th
tool call. Segment B: bank the goldens, pycache delete-only and never chained, W-179 ending with a blank line, DEF-139, DOCKET
delta by --append, close.py to BUILD170 with the reverse guard, HANDOFF-92 in this form BEFORE the final verification, begin the
close with at least eight tool calls left. Handoff at 90–95 % of context or on a closed segment — never mid-segment. Timeout on
every call. Never copy over an existing file."
