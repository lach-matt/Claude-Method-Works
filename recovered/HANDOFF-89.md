# HANDOFF-89 — The Method 1.6 — chat 136 → chat 137

Slim form (RULINGS-R2.md chat-127 item 5): identity, gate, next work, Drive actions, prompt. **The repair docket, the standing
method and the conventions live in `DOCKET.md` (index + chat-128 … chat-136 deltas); the findings in the READ-chNN.md /
READ-intake1.md members and WORKING-REGISTER.md; the deferred items in DEFERRED.md; the rulings in RULINGS-R2.md.** Read all
four at open, last blocks first.

## Identity

- Written from **chat 136** for **chat 137**. Live files: **BUILD90 main** (unchanged since chat 62) and **BUILD167 compendia**
  (= BUILD166 + W-176 + DEF-136 + DOCKET chat-136 delta + six members). Register **1 to 1792**. W-176 IS seated; chat 137 seats
  nothing at open. No rulings were taken in chat 136; nothing was put to M.
- **BUILD167** `The_Method_1_6_BUILD167_compendia_papers_audits.md` **4,678,944 B · md5 3874f9bd0afcc18769fc08f30cdf29f5 ·
  57,029 lines · 279 members** (reverse recovered 67448beb…). ARCHIVE1 (5a5c0829…, 394 members) is NOT fetched at the gate.
- **Governing state** unchanged from HANDOFF-88: RUL-128 items 1–4, chat-81 cadence, chat-95 bar, chat-127 items 1, 2, 3, 5
  (executed), Register append-only, no silent change; the intake is executed (DOCKET item 38).
- **Main volume 91.9 % read (L10897 of 11,855). All thirty-six chapters and Appendices A, B, C, D CLOSED** (READ-ch23a: the
  closed index rebuilt from its own seven tables reproduces the D.5 table exactly; eight findings, three of them the appendix
  restating a state its own later mathematics withdrew). **Appendix E is the next unit — DATA under chat-127 item 1** (Q, indexed
  and closed: every item resolved to its site and its register entry, every status marker tested against the entry and its WARNING).
- **MEASURED heading lines this chat, to be re-taken by your own scan:** `## Appendix E` L10898 (a list hit at L166 is excluded);
  the end of Appendix E and its sub-headings were NOT scanned this chat — take them fresh. PP `# Appendix E` P10437; PP's sub-headings
  under an appendix are UNMARKED (indented one space after a blank line) — scan them the same way (r2-ch23b §2 shows the method).
- **Discipline note:** chat 136 banked its goldens at the 34th and 43rd calls — the gate took 14 calls and the 436-line unit was read
  whole in five calls. Budget for chat 137: measure the unit at the first read call; if Appendix E exceeds ≈ 250 lines, split at a
  sub-heading of your own scan BEFORE reading; bank both instruments by the 30th call; begin the close by the 36th. Read every census
  row's class and detail BEFORE writing its verdict. A long-fibre table row may carry a 2-space column gap (DOCKET chat-136 convention).

## §0 Gate (each step its own tool call under `timeout 280`; any FAIL stops the chat with a report)

1. `ls -la /mnt/user-data/uploads /mnt/user-data/outputs /home/claude`; `recent_chats` (n=3) confirms the latest chat is 136.
   Read `/mnt/project/CLAUDE.md` (project instruction; never a member).
2. Fetch both bundles by title: `Google Drive:search_files` with
   `title contains 'BUILD167_compendia' or title contains 'BUILD90_main'`, pageSize 5, excludeContentSnippets;
   `Google Drive:download_file_content` on each fileId; note the spill paths `/mnt/user-data/tool_results/<id>.json`.
3. Bootstrap (the only step outside gate.py), verbatim, with the two spill paths filled in:

```
cd /home/claude && timeout 280 python3 - <<'EOF'
import json, base64, hashlib, re, os
EXP={'main':'49065309b0c4fe8e055f693aed295cca','comp':'3874f9bd0afcc18769fc08f30cdf29f5'}
NAME={'main':'/home/claude/The_Method_1_6_BUILD90_main_and_register.md','comp':'/home/claude/The_Method_1_6_BUILD167_compendia_papers_audits.md'}
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
   Expected: main 1,983,081 B · 18,470 lines; compendia **4,678,944 B · 57,029 lines**; **281 members extracted (2 + 279)**.
4. Fetch the Prints & Proofs original before step 7: folder `1vYctzLppUZ2vFPJDCZ6wvkgSdj3v_f6n`, fileId
   `1vsWwRT9BmUNeMrqokuo4jI4DJnoADubH`, **738,550 B · md5 49900cf41f818ab789bb90fc596ac977 · 11,371 lines**, decoded the same way
   to `/home/claude/PP_The_Method_1_6.md` (assert the md5 and `not os.path.exists`). r2-ch23b, r2-ch22b, r2-ch21a and r2-ch20a read it there.
5. `gate.py census` → `OK census: DEFECT-CENSUS.tsv byte-identical` (1,556 rows + header, ≈ 12 s).
6. `gate.py run --core` → five `OK` (tower 976/1,654/2,535/13,585/70,905/199,130; kinds 1565 · 1356 · 499 · 149; minmax;
   r2-tools-constants; extent "1 to 1792").
7. `gate.py manifest` → `MANIFEST OK`; MANIFEST.tsv **18,852 B · 4904dccd6e23a98d3f696851d1affe14 · 281 lines**;
   WORKING-REGISTER.md **847,430 B · 6847bec923b3533de3a10010106438c0 · 7,867 lines**, ends **W-176**; RULINGS-R2.md ends with
   the chat-128 block (unchanged); DEFERRED.md's last block is chat 136's; DOCKET.md ends with the chat-136 delta.
8. `gate.py run r2-ch23a r2-ch23b r2-ch22a r2-ch22b` → four `OK` (r2-ch23a.out 9,970 B · 76775e08 · 81 lines, ≈ 3 s, needs NumPy;
   r2-ch23b.out 17,355 B · 16400511 · 161 lines, **≈ 175 s — run it in its own call**, needs PP on disk; r2-ch22a needs NumPy, SymPy;
   r2-ch22b needs PP). r2-ch20a (the COORDINATES-2_13.csv golden) is not in the run list this chat; the project file must stay.
9. `gate.py cert 137` → `/home/claude/GATE-ch137.txt`, verdict PASS only if every step passed.
10. `rm -rf /home/claude/members/__pycache__` — its own delete-only call, after every run or bank, never chained.

## Chat 137's work order (two segments; each closed before the next opens)

**Segment A — the R2 unit: Appendix E, `## Appendix E` L10898 to `## Appendix F` (heading line to be re-taken; measure the unit
and its sub-headings first; read as **DATA** under chat-127 item 1 — Appendix E is Q, indexed and closed: every Q item's row resolves
to its site (section or register) under both resolvers, every status marker (closed / open / withdrawn) is tested against the entry it
restates and that entry's WARNING line, every printed count re-taken with its DATA-row set fixed and printed first, every ledger
totals line checked against its rows (17c-01's *nine things* lives in §E.5 — read it as a site of docket 34, not a new finding), and
E.4.1's ruling *an assertion is not an enumeration* (cited at L10520, L10538) located). If the unit will not fit one chat with the
close, split at a `### E.n` heading measured by your own scan, close the part, and never split a sub-section. Instruments
**r2-ch24a** (computable) and **r2-ch24b** (prose/pointers); import from r2lib by path; copy `rbody`, `body_range` and `lettered` from
r2-ch23a with provenance comments. Pre-PP: diff headings against PP from P10437 (strip the section number from BOTH sides; PP's
sub-headings are unmarked). Known twin sites from earlier reads: §E.5's broken fraction L11165–L11168 (docket 28), *nine things* vs
eleven ledger rows (17c-01), Appendix E's counts under docket 35 (15n-07 family) — measure them as sites of those items. Register
entries naming Appendix E: grep them yourself and read every WARNING line. Apply DOCKET.md's method throughout.

**Segment B — close:** bank the goldens; pycache delete-only; W-177 (ends with a blank line); DEF-137; DOCKET delta by
`--append`; close.py BUILD167 → BUILD168 (reverse must recover 3874f9bd…; `--append` before `--members`); HANDOFF-90 in this
form BEFORE the final verification; ≥ 8 calls left at the start. **Tool-call ceiling:** if calls run out mid-segment, close it as
failed with diagnosis and let M's *Continue* re-open the container (which persists within a chat).

**Standing after Appendix E:** F–G as data; the Index and References under docket 36 (Xia, Routh, Fourier, Motzkin on it); then
RUL-128 item 3's order — the Register WARNING sweep (the 1,748-vs-1,738 datum of DEF-133 item 5 goes there; Register 219–221 / 305
headings of 23b-03 join it), then the computable re-derivations (Chapter 34 re-take, docket 37, and the SCF chain first; the Sc VI chain
of 21a-02/-03 and the Appendix-D reconstruction ledger 23a-03 join docket 37). The three-body project owes a reply on intake1-01/-04
and 1756 (DEF-130 items 1, 5) — through M, when M chooses.

## Drive actions for M

- **Upload** to Materials (`1XX_5f3PZB6tjRtiZ2GIgd8Tt7i_4GgkY`): `HANDOFF-89.md` and
  `The_Method_1_6_BUILD167_compendia_papers_audits.md`.
- **Retire** once BUILD167 gates PASS in chat 137: HANDOFF-88 and BUILD166 (HANDOFF-87 and BUILD165 were due under HANDOFF-88).
- **Keep:** BUILD90 main (still live — no BUILD91 was built); BUILD124; ARCHIVE1 permanently; the Prints & Proofs folder; the
  certificates; OWED-REGISTER-EXPANSIONS.md; OWED-EXPANSIONS-2.md; covers8.json; factor.py; the two delivery zips in their
  subfolders; **the project file COORDINATES-2_13.csv (r2-ch20a's golden reads it).**
- **When convenient:** DEF-130 items 1 and 5 to the three-body project; the pending bank to the Löwdin project (DEF-130 item 6).
  New this chat, for R3 (no action now): A.5 is *proved · exhaustive* by Register 222 / 248 but D.5.4 still prints *sampled* (23a-01);
  D.5.1 describes a sixteen-fibre table beside the twenty-four-fibre one (23a-02); Register 219, 220, 221 and 305 are cited by
  Appendix D but carry no heading (23b-03); Fourier and Motzkin are unbibliographed (23b-04).

## Prompt for chat 137

"Chat 137. READ EVERYTHING BEFORE YOU DO ANYTHING. Live files: BUILD90 main (1,983,081 B, md5
49065309b0c4fe8e055f693aed295cca) and BUILD167 compendia (4,678,944 B, md5 3874f9bd0afcc18769fc08f30cdf29f5, 57,029 lines,
279 members); ARCHIVE1 (md5 5a5c0829fa234dde4f12ac240fc7dec4) is not fetched at the gate. List uploads, outputs and
/home/claude first. Run HANDOFF-89's §0 gate in full and in order — fetch both bundles by title, bootstrap with the script in
the handoff (decode, md5, extract, expect 281 files), fetch the Prints & Proofs original 'The Method 1.6.md' (738,550 B, md5
49900cf41f818ab789bb90fc596ac977) to /home/claude/PP_The_Method_1_6.md, then gate.py census, run --core, manifest, run
r2-ch23a r2-ch23b r2-ch22a r2-ch22b (r2-ch23b takes ≈ 175 s — its own call), cert 137; any FAIL stops the chat with a report.
Then read, last blocks first: RULINGS-R2.md (the chat-128 block), DOCKET.md (index plus the chat-128 to chat-136 deltas),
DEFERRED.md (chat 136's block is the last), READ-ch23a.md. The standing block's Phase 0–4 Löwdin/three-body plan is executed
carried state; discard it per Ruling 41; the intake is executed too. Line numbers are MEMBER line numbers and are never carried
between chats, nor is any count or heading list. Work in two segments and close each before the next opens. Segment A: the R2
unit Appendix E, from `## Appendix E` to `## Appendix F`, measured by your own scan at the first read call (split at a `### E.n`
heading of your own scan BEFORE reading if it exceeds ≈ 250 lines with the close; never split a sub-section), read as DATA under
chat-127 item 1 with every Q row resolved to its site and its register entry under both resolvers, every status marker tested against
its entry and that entry's WARNING line, every printed count re-taken with the DATA-row set fixed and printed first, every ledger
totals line checked against its rows; instruments r2-ch24a computable and r2-ch24b prose, importing from r2lib by path, copying
nothing but rbody, body_range and lettered from r2-ch23a with provenance comments, reading MEMBERS never a bundle path; the appendix
is pre-PP — diff its headings against PP from P10437 (PP's sub-headings are unmarked); read the WARNING line on every cited entry; grep
the Register for a later entry naming the appendix before recording any figure as unreproducible. Apply DOCKET.md's method
throughout: name every convention before scoring, Decimal not round(), a Register entry body is the first non-blank line after its
heading, a first-person probe carries mine and myself and excludes the Roman numeral of a species, a literal string is not a test, a
count word counts DATA rows and the DATA-row set is fixed first, a whitespace table's DATA row carries a ≥ 3-space column gap except
that a long-fibre row may carry a 2-space gap and is parsed on its own grammar, a tie or constraining count names its quantifier or
test, a wrapped phrase is read on the markup-stripped join, a | at line start is a table row only outside a code line, a numeral regex
admits a trailing non-thousands comma, read every census row's class and detail before writing its verdict, give every negative its
witness, record passes as well as failures, expect the instrument to be wrong before the book. Bank both instruments by the 30th
tool call. Segment B: bank the goldens, pycache delete-only and never chained, W-177 ending with a blank line, DEF-137, DOCKET delta
by --append, close.py to BUILD168 with the reverse guard, HANDOFF-90 in this form BEFORE the final verification, begin the close with
at least eight tool calls left. Handoff at 90–95 % of context or on a closed segment — never mid-segment. Timeout on every call.
Never copy over an existing file."
