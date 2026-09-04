# HANDOFF-92 — The Method 1.6 — chat 139 → chat 140

Slim form (RULINGS-R2.md chat-127 item 5): identity, gate, next work, Drive actions, prompt. **The repair docket, the standing
method and the conventions live in `DOCKET.md` (index + chat-128 … chat-139 deltas); the findings in the READ-chNN.md /
READ-intake1.md members and WORKING-REGISTER.md; the deferred items in DEFERRED.md; the rulings in RULINGS-R2.md.** Read all
four at open, last blocks first.

## Identity

- Written from **chat 139** for **chat 140**. Live files: **BUILD90 main** (unchanged since chat 62) and **BUILD170 compendia**
  (= BUILD169 + W-179 + DEF-139 + DOCKET chat-139 delta + six members). Register **1 to 1792**. W-179 IS seated; chat 140 seats
  nothing at open. No rulings were taken in chat 139; nothing was put to M.
- **BUILD170** `The_Method_1_6_BUILD170_compendia_papers_audits.md` **4,960,242 B · md5 dfb7544cf940100ce93f6eab6f1f5bfa ·
  59,146 lines · 297 members** (reverse recovered 92f26e13…). ARCHIVE1 (5a5c0829…, 394 members) is NOT fetched at the gate.
- **Governing state** unchanged from HANDOFF-91: RUL-128 items 1–4, chat-81 cadence, chat-95 bar, chat-127 items 1, 2, 3, 5
  (executed), Register append-only, no silent change; the intake is executed (DOCKET item 38).
- **Main volume 95.8 % read (L11360 of 11,855). All thirty-six chapters and Appendices A–F CLOSED** (READ-ch26a: eight
  findings — *Chapters 6, 12 and 24* where the third citer is §22.1.1.1; Register 1779's *Z − charge* one short of the electron
  count, the (iii) claim itself holding on all 7,260 pairs; *nine stable cells, named at F.3.1* where the rebuilt F.3.1 names none;
  §32.1.3 / §32.1.4.1 citing F.4.1 for a withdrawn ratio; §32.1.4's *Appendix F, the numbers 33* vs 3; *several … this rule firing*
  with 0 Register matches; *as the chapters cite it* with no chapter site; Register 1786's *never an F.3.1 or F.3.2* against PP's
  headings; nine Ruling 45 sites. 24b-06 corrected: F.4.3 is not a #P-complete site). **Appendix F is a post-PP rebuild (Register
  1780; 1786 renumbered F.3.3 → F.3.1) sharing zero body lines with PP's 231-line appendix; PP has NO Appendix G.**
- **Appendix G is the next unit — from `## Appendix G` L11361 (LAST hit) to `## References` L11503 (LAST hit), ≈ 142 lines,
  DATA under chat-127 item 1. G is post-PP: no pre-PP diff exists; the Register entry that seated it is the witness — find it
  (grep the Register for `Appendix G` / `G\.\d`) and read its WARNING lines before scoring any figure.**
- **MEASURED heading lines this chat, to be re-taken by your own scan:** `## Appendix G` L11361; `## References` L11503 (the LAST
  `References` hit; the first is the contents list). *#P-complete* sites: §14.6 L4080, §28.10 L8227, E.1.5 L11024, R.5 L11762–L11763.
  Appendix G is cited from the unit's neighbours: §23.8 (*Newton decrement* at G L11654 per DEF-138 item 7), §30.3.4's *three
  quarters* restated at G L11670 (READ-ch25a §B) — test both.
- **Discipline note:** chat 139 banked at the 33rd and 38th calls (gate 15, governing reads 5, scan 1, read 1, sources 3,
  instruments with five self-caught faults 10, pycache 2, READ / census 2). Budget for chat 140: bank both instruments by the
  30th call; begin the close by the 36th. The coordinate file's `charge` column is the ionisation stage (1 = neutral): an
  electron count is Z − charge + 1. A wrapped phrase (*Chapters 6, 12 and 24*) scores 0 on raw lines — read the join.

## §0 Gate (each step its own tool call under `timeout 280`; any FAIL stops the chat with a report)

1. `ls -la /mnt/user-data/uploads /mnt/user-data/outputs /home/claude`; `recent_chats` (n=3) confirms the latest chat is 139.
   Read `/mnt/project/CLAUDE.md` (project instruction; never a member).
2. Fetch both bundles by title: `Google Drive:search_files` with
   `title contains 'BUILD170_compendia' or title contains 'BUILD90_main'`, pageSize 5, excludeContentSnippets;
   `Google Drive:download_file_content` on each fileId; note the spill paths `/mnt/user-data/tool_results/<id>.json`.
3. Bootstrap (the only step outside gate.py), verbatim, with the two spill paths filled in:

```
cd /home/claude && timeout 280 python3 - <<'EOF'
import json, base64, hashlib, re, os
EXP={'main':'49065309b0c4fe8e055f693aed295cca','comp':'dfb7544cf940100ce93f6eab6f1f5bfa'}
NAME={'main':'/home/claude/The_Method_1_6_BUILD90_main_and_register.md','comp':'/home/claude/The_Method_1_6_BUILD170_compendia_papers_audits.md'}
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
   Expected: main 1,983,081 B · 18,470 lines; compendia **4,960,242 B · 59,146 lines**; **299 members extracted (2 + 297)**.
4. Fetch the Prints & Proofs original before step 7: folder `1vYctzLppUZ2vFPJDCZ6wvkgSdj3v_f6n`, fileId
   `1vsWwRT9BmUNeMrqokuo4jI4DJnoADubH`, **738,550 B · md5 49900cf41f818ab789bb90fc596ac977 · 11,371 lines**, decoded the same way
   to `/home/claude/PP_The_Method_1_6.md` (assert the md5 and `not os.path.exists`). r2-ch26b, r2-ch25a, r2-ch25b read it there.
5. `gate.py census` → `OK census: DEFECT-CENSUS.tsv byte-identical` (1,556 rows + header, ≈ 14 s).
6. `gate.py run --core` → five `OK` (tower 976/1,654/2,535/13,585/70,905/199,130; kinds 1565 · 1356 · 499 · 149; minmax;
   r2-tools-constants; extent "1 to 1792").
7. `gate.py manifest` → `MANIFEST OK`; MANIFEST.tsv **20,060 B · 81c5d9e0d156e351df0915c18f5000fd · 299 lines**;
   WORKING-REGISTER.md **859,882 B · fdb11bb8c24f7d04d8c439646a042c95 · 7,888 lines**, ends **W-179**; RULINGS-R2.md ends with
   the chat-128 block (unchanged); DEFERRED.md's last block is chat 139's; DOCKET.md ends with the chat-139 delta.
8. `gate.py run r2-ch26a r2-ch26b r2-ch25a r2-ch25b` → four `OK` (r2-ch26a.out 13,321 B · 2e0ea41c · 113 lines, 1 s — needs
   COORDINATES-2_13.csv in the project folder; r2-ch26b.out 13,135 B · 68e21543 · 112 lines, 0 s, needs PP; r2-ch25a 17 s, needs
   PP and tower-2.py; r2-ch25b 1 s, needs PP). r2-ch24a/b, r2-ch23a/b, r2-ch22a/b and r2-ch20a are not in the run list this chat;
   **the project file COORDINATES-2_13.csv must stay (r2-ch20a's and r2-ch26a's goldens read it).**
9. `gate.py cert 140` → `/home/claude/GATE-ch140.txt`, verdict PASS only if every step passed.
10. `rm -rf /home/claude/members/__pycache__` — its own delete-only call, after every run or bank, never chained.

## Chat 140's work order (two segments; each closed before the next opens)

**Segment A — the R2 unit: Appendix G, `## Appendix G` L11361 to `## References` L11503 (heading lines to be re-taken; measure
the appendix and its sub-headings first; split at a `### G.n` heading before reading if it will not fit with the close; read as
**DATA** under chat-127 item 1).** Appendix G is *Transitions, indexed*: every printed figure re-taken on the rebuilt tower or
located at its source section under both resolvers with its home heading; every table's DATA-row set fixed and printed first (a
`|` at line start is a table row only outside a code line; a whitespace row parsed on ≥ 2 spaces where ≥ 3 changes the column
count, printed); every count word re-taken on raw lines AND the join; every status / withdrawn marker tested against the entry it
restates and that entry's WARNING line; grep the Register for the entry that seated Appendix G (post-PP) and for any later entry
naming it before recording a figure as unreproducible; the *Newton decrement* (DEF-138 item 7) and *three quarters* (READ-ch25a)
sites tested; the 20a-01 / 21a-04 / 16z-01 figures (1,105 / 1,442 / 1,061 / Chapter 34's) wherever G prints them, against the
Register's WARNING lines (1309, 1350, 1401, 1403, 1461) and docket 35. Instruments **r2-ch27a** (computable) and **r2-ch27b**
(prose / pointers); import from r2lib by path; copy `rbody`, `body_range`, `lettered` from r2-ch26b with provenance comments; read
MEMBERS never a bundle path. No pre-PP diff (PP has no Appendix G — state it with the witness). Apply DOCKET.md's method throughout.

**Segment B — close:** bank the goldens; pycache delete-only; W-180 (ends with a blank line); DEF-140; DOCKET delta by
`--append`; close.py BUILD170 → BUILD171 (reverse must recover dfb7544c…; `--append` before `--members`); HANDOFF-93 in this
form BEFORE the final verification; ≥ 8 calls left at the start. **Tool-call ceiling:** if calls run out mid-segment, close it as
failed with diagnosis and let M's *Continue* re-open the container (which persists within a chat).

**Standing after Appendix G:** the Index and References under docket 36 (Xia, Routh, Fourier, Motzkin, Gröbner, Seaton on it) —
the main volume closes there; then RUL-128 item 3's order — the Register WARNING sweep (the 1,748-vs-1,738 datum of DEF-133 item 5;
Register 219–221 / 305 / 239 / 256 headings of 23b-03 / 24b-03; 1779's and 1786's wording of 26a-02 / 26b-06 join it), then the
computable re-derivations (Chapter 34 re-take, docket 37, and the SCF chain first; the Sc VI chain of 21a-02/-03 with E.3's bracket
site, the Appendix-D reconstruction ledger 23a-03, Appendix E's 256-code ledger 24a-05 with its coordinates unprinted, §23.10's
499 / 518, §28.7.4's forty for 25b-03, the Register's firings of F.3's rule for 26b-04, the 188 only-PP lines of the withdrawn
Appendix F for 26b-02 / 26b-03). The three-body project owes a reply on intake1-01/-04 and 1756 (DEF-130 items 1, 5) — through
M, when M chooses.

## Drive actions for M

- **Upload** to Materials (`1XX_5f3PZB6tjRtiZ2GIgd8Tt7i_4GgkY`): `HANDOFF-92.md` and
  `The_Method_1_6_BUILD170_compendia_papers_audits.md`.
- **Retire** once BUILD170 gates PASS in chat 140: HANDOFF-91 and BUILD169 (HANDOFF-90 and BUILD168 were due under HANDOFF-91).
- **Keep:** BUILD90 main (still live — no BUILD91 was built); BUILD124; ARCHIVE1 permanently; the Prints & Proofs folder; the
  certificates; OWED-REGISTER-EXPANSIONS.md; OWED-EXPANSIONS-2.md; covers8.json; factor.py; the two delivery zips in their
  subfolders; **the project file COORDINATES-2_13.csv (r2-ch20a's and r2-ch26a's goldens read it).**
- **When convenient:** DEF-130 items 1 and 5 to the three-body project; the pending bank to the Löwdin project (DEF-130 item 6).
  New this chat, for R3 (no action now): two Register-entry findings — 1779's *Z − charge* (26a-02) and 1786's *never an F.3.1 or
  F.3.2* (26b-06) — each corrected by a new entry citing the old, never by editing it.

## Prompt for chat 140

"Chat 140. READ EVERYTHING BEFORE YOU DO ANYTHING. Live files: BUILD90 main (1,983,081 B, md5
49065309b0c4fe8e055f693aed295cca) and BUILD170 compendia (4,960,242 B, md5 dfb7544cf940100ce93f6eab6f1f5bfa, 59,146 lines,
297 members); ARCHIVE1 (md5 5a5c0829fa234dde4f12ac240fc7dec4) is not fetched at the gate. List uploads, outputs and
/home/claude first. Run HANDOFF-92's §0 gate in full and in order — fetch both bundles by title, bootstrap with the script in
the handoff (decode, md5, extract, expect 299 files), fetch the Prints & Proofs original 'The Method 1.6.md' (738,550 B, md5
49900cf41f818ab789bb90fc596ac977) to /home/claude/PP_The_Method_1_6.md, then gate.py census, run --core, manifest, run
r2-ch26a r2-ch26b r2-ch25a r2-ch25b, cert 140; any FAIL stops the chat with a report. Then read, last blocks first:
RULINGS-R2.md (the chat-128 block), DOCKET.md (index plus the chat-128 to chat-139 deltas), DEFERRED.md (chat 139's block is the
last), READ-ch26a.md. The standing block's Phase 0–4 Löwdin/three-body plan is executed carried state; discard it per Ruling 41;
the intake is executed too. Line numbers are MEMBER line numbers and are never carried between chats, nor is any count or
heading list. Work in two segments and close each before the next opens. Segment A: the R2 unit Appendix G, from `## Appendix G`
to `## References` (both the LAST hit), measured by your own scan at the first read call (split at a `### G.n` heading before
reading if it will not fit with the close), read as DATA under chat-127 item 1 with every printed figure re-taken on the rebuilt
tower or located at its source under both resolvers with its home heading, every table's DATA-row set fixed and printed first,
every count word re-taken on raw lines and on the join, every status or withdrawn marker tested against its entry and that
entry's WARNING line, the Register entry that seated Appendix G found and read (G is post-PP; PP has no Appendix G — no pre-PP
diff, say so with the witness), the Newton-decrement and three-quarters sites tested, the 1,105 / 1,442 / 1,061 / Chapter 34
figures against the Register's WARNING lines wherever G prints them; instruments r2-ch27a computable and r2-ch27b prose,
importing from r2lib by path, copying nothing but rbody, body_range and lettered from r2-ch26b with provenance comments, reading
MEMBERS never a bundle path; read the WARNING line on every cited entry; grep the Register for a later entry naming the appendix
before recording any figure as unreproducible. Apply DOCKET.md's method throughout: name every convention before scoring,
Decimal not round(), a Register entry body is the first non-blank line after its heading, a first-person probe carries mine and
myself and excludes the Roman numeral of a species, a literal string is not a test, a count word counts DATA rows and the
DATA-row set is fixed first, a paragraph start is a non-blank line after a blank or after the heading, a fraction may be printed
in words, a whitespace table row is parsed on a ≥ 2-space split where the ≥ 3-space split changes the column count and the
difference is printed, a tie or constraining count names its quantifier or test, a wrapped phrase is read on the markup-stripped
join, a | at line start is a table row only outside a code line, a numeral regex admits a trailing non-thousands comma, `##
References` is the LAST heading hit not the first, the coordinate file's charge column is the ionisation stage so an electron
count is Z − charge + 1, read every census row's class and detail before writing its verdict, give every negative its witness,
record passes as well as failures, expect the instrument to be wrong before the book. Bank both instruments by the 30th tool
call. Segment B: bank the goldens, pycache delete-only and never chained, W-180 ending with a blank line, DEF-140, DOCKET delta
by --append, close.py to BUILD171 with the reverse guard, HANDOFF-93 in this form BEFORE the final verification, begin the close
with at least eight tool calls left. Handoff at 90–95 % of context or on a closed segment — never mid-segment. Timeout on every
call. Never copy over an existing file."
