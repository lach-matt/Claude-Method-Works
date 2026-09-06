# HANDOFF-90 — The Method 1.6 — chat 137 → chat 138

Slim form (RULINGS-R2.md chat-127 item 5): identity, gate, next work, Drive actions, prompt. **The repair docket, the standing
method and the conventions live in `DOCKET.md` (index + chat-128 … chat-137 deltas); the findings in the READ-chNN.md /
READ-intake1.md members and WORKING-REGISTER.md; the deferred items in DEFERRED.md; the rulings in RULINGS-R2.md.** Read all
four at open, last blocks first.

## Identity

- Written from **chat 137** for **chat 138**. Live files: **BUILD90 main** (unchanged since chat 62) and **BUILD168 compendia**
  (= BUILD167 + W-177 + DEF-137 + DOCKET chat-137 delta + six members). Register **1 to 1792**. W-177 IS seated; chat 138 seats
  nothing at open. No rulings were taken in chat 137; nothing was put to M.
- **BUILD168** `The_Method_1_6_BUILD168_compendia_papers_audits.md` **4,780,462 B · md5 78daa717065a58b0698a18c27f20a0aa ·
  57,851 lines · 285 members** (reverse recovered 3874f9bd…). ARCHIVE1 (5a5c0829…, 394 members) is NOT fetched at the gate.
- **Governing state** unchanged from HANDOFF-89: RUL-128 items 1–4, chat-81 cadence, chat-95 bar, chat-127 items 1, 2, 3, 5
  (executed), Register append-only, no silent change; the intake is executed (DOCKET item 38).
- **Main volume 93.2 % read (L11053 of 11,855). All thirty-six chapters and Appendices A–D CLOSED; Appendix E part 1 (lead,
  E.1–E.1.5, E.2) CLOSED** (READ-ch24a: eleven findings — E.2 cites §23.10.4's 499 as *518*, a *Gröbner basis of eight* §30.4.1
  narrates as superseded, the accelerator identity to §26.6 which is Aitken only; E.4 is cited but has no heading; Register 239 and
  256 have no heading; E(Q) = 0 fibred at fourteen REPRODUCES under ℛ). **Appendix E part 2 is the next unit — E.3 to E.8, DATA
  under chat-127 item 1.**
- **MEASURED heading lines this chat, to be re-taken by your own scan:** `### E.3` L11054, `### E.4.1` L11132, `### E.4.2` L11137,
  `### E.5` L11143, `### E.6` L11189, `### E.7` L11201, `### E.8` L11212, `## Appendix F` L11222 (a list hit at L168 is excluded);
  **there is no `### E.4` — its text is an unmarked body line at L11105 (finding 24b-02; PP P10618 the same).** PP `# Appendix E`
  P10437, `E.3` P10567 unmarked, `# Appendix F` P10761; PP's sub-headings are unmarked and THREE of them (E.1.1, E.1.3, E.4) have
  no blank line above — scan heading-form lines and read them (r2-ch24b §1 shows the method).
- **Discipline note:** chat 137 banked its goldens at the 38th call (gate 15 calls, governing reads 5, scan 2, read 2, instruments
  and six self-caught faults 12). Budget for chat 138: the unit is 168 lines — read whole; bank both instruments by the 30th call;
  begin the close by the 36th. Read every census row's class and detail BEFORE writing its verdict. A whitespace-table row may
  carry a 2-space gap (chat-136 / chat-137 convention: parse on ≥ 2 spaces where the ≥ 3-space split changes the column count).

## §0 Gate (each step its own tool call under `timeout 280`; any FAIL stops the chat with a report)

1. `ls -la /mnt/user-data/uploads /mnt/user-data/outputs /home/claude`; `recent_chats` (n=3) confirms the latest chat is 137.
   Read `/mnt/project/CLAUDE.md` (project instruction; never a member).
2. Fetch both bundles by title: `Google Drive:search_files` with
   `title contains 'BUILD168_compendia' or title contains 'BUILD90_main'`, pageSize 5, excludeContentSnippets;
   `Google Drive:download_file_content` on each fileId; note the spill paths `/mnt/user-data/tool_results/<id>.json`.
3. Bootstrap (the only step outside gate.py), verbatim, with the two spill paths filled in:

```
cd /home/claude && timeout 280 python3 - <<'EOF'
import json, base64, hashlib, re, os
EXP={'main':'49065309b0c4fe8e055f693aed295cca','comp':'78daa717065a58b0698a18c27f20a0aa'}
NAME={'main':'/home/claude/The_Method_1_6_BUILD90_main_and_register.md','comp':'/home/claude/The_Method_1_6_BUILD168_compendia_papers_audits.md'}
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
   Expected: main 1,983,081 B · 18,470 lines; compendia **4,780,462 B · 57,851 lines**; **287 members extracted (2 + 285)**.
4. Fetch the Prints & Proofs original before step 7: folder `1vYctzLppUZ2vFPJDCZ6wvkgSdj3v_f6n`, fileId
   `1vsWwRT9BmUNeMrqokuo4jI4DJnoADubH`, **738,550 B · md5 49900cf41f818ab789bb90fc596ac977 · 11,371 lines**, decoded the same way
   to `/home/claude/PP_The_Method_1_6.md` (assert the md5 and `not os.path.exists`). r2-ch24b, r2-ch23b, r2-ch22b read it there.
5. `gate.py census` → `OK census: DEFECT-CENSUS.tsv byte-identical` (1,556 rows + header, ≈ 12 s).
6. `gate.py run --core` → five `OK` (tower 976/1,654/2,535/13,585/70,905/199,130; kinds 1565 · 1356 · 499 · 149; minmax;
   r2-tools-constants; extent "1 to 1792").
7. `gate.py manifest` → `MANIFEST OK`; MANIFEST.tsv **19,255 B · 7a7bb3fcedfcb415c6c0619686ac3610 · 287 lines**;
   WORKING-REGISTER.md **851,233 B · 6cdce5f3ea2518a3fe3e7b600a71ed17 · 7,874 lines**, ends **W-177**; RULINGS-R2.md ends with
   the chat-128 block (unchanged); DEFERRED.md's last block is chat 137's; DOCKET.md ends with the chat-137 delta.
8. `gate.py run r2-ch24a r2-ch24b r2-ch23a r2-ch22a` → four `OK` (r2-ch24a.out 11,806 B · f3cef85d · 97 lines, 0 s; r2-ch24b.out
   29,490 B · 78620065 · 322 lines, 1 s, needs PP on disk; r2-ch23a needs NumPy, ≈ 4 s; r2-ch22a needs NumPy, SymPy, ≈ 5 s).
   r2-ch23b (175 s) and r2-ch22b are not in the run list this chat; r2-ch20a (the COORDINATES-2_13.csv golden) neither — the project
   file must stay.
9. `gate.py cert 138` → `/home/claude/GATE-ch138.txt`, verdict PASS only if every step passed.
10. `rm -rf /home/claude/members/__pycache__` — its own delete-only call, after every run or bank, never chained.

## Chat 138's work order (two segments; each closed before the next opens)

**Segment A — the R2 unit: Appendix E part 2, `### E.3` L11054 to `## Appendix F` L11222 (heading lines to be re-taken; measure the
unit and its sub-headings first; 168 lines by this chat's scan — read whole; read as **DATA** under chat-127 item 1).** E.3 gives
each open item in full: every item's row resolves to its site (section or register) under both resolvers, and E.3 is where K, M, N,
O's coordinates should be printed — take them, then re-take the **thirteen-state (E(Q) = 0 fibred, 1 unfibred, Register 256 / 1729)
and the eleven-state (E.1.3's *4 unfibred*, E.1.4's *4 → 10*)** under §6.1's ℛ with r2-ch24a's `E_R`, `boxA / boxB / boxF` copied
with provenance (24a-05 stays open until they are). Every status marker (closed / open / withdrawn) is tested against the entry it
restates and that entry's WARNING line; every printed count re-taken with its DATA-row set fixed and printed first; **every ledger
totals line checked against its rows** — §E.5's *nine things* vs eleven ledger rows (17c-01, docket 34: a site, not a new finding),
§E.5's broken fraction L11165–L11168 (docket 28), Appendix E's counts under docket 35 (15n-07 family), E.4.1's ruling *an assertion is
not an enumeration* (cited at L10520, L10538, and Register 211), the unmarked *E.4 The grid, read on the current set* line at L11105
(24b-02's site — read the paragraph it heads), E.6's complexity claim against §29.8 / §30.3 (Stahl & Wille, Yannakakis), E.8's *what
closed* list against E.1.1's lineage rows and E.2's eight. Instruments **r2-ch25a** (computable) and **r2-ch25b** (prose/pointers);
import from r2lib by path; copy `rbody`, `body_range`, `lettered` from r2-ch24a with provenance comments. Pre-PP: diff headings
against PP from P10567 (strip the section number from BOTH sides; heading-form lines without a blank line above are heading
candidates — read them). Register entries naming Appendix E: grep them yourself and read every WARNING line; 239 and 256 have no
heading (24b-03) — search their numerals inside other entries. Apply DOCKET.md's method throughout.

**Segment B — close:** bank the goldens; pycache delete-only; W-178 (ends with a blank line); DEF-138; DOCKET delta by
`--append`; close.py BUILD168 → BUILD169 (reverse must recover 78daa717…; `--append` before `--members`); HANDOFF-91 in this
form BEFORE the final verification; ≥ 8 calls left at the start. **Tool-call ceiling:** if calls run out mid-segment, close it as
failed with diagnosis and let M's *Continue* re-open the container (which persists within a chat).

**Standing after Appendix E:** F–G as data (F.3's sub-sections: 24b-05's F.3.3 → F.3.1 question is resolved there); the Index and
References under docket 36 (Xia, Routh, Fourier, Motzkin, Gröbner on it); then RUL-128 item 3's order — the Register WARNING sweep
(the 1,748-vs-1,738 datum of DEF-133 item 5; Register 219–221 / 305 / 239 / 256 headings of 23b-03 / 24b-03 join it), then the
computable re-derivations (Chapter 34 re-take, docket 37, and the SCF chain first; the Sc VI chain of 21a-02/-03, the Appendix-D
reconstruction ledger 23a-03, Appendix E's 256-code ledger 24a-05 and §23.10's 499 / 518 join docket 37). The three-body project
owes a reply on intake1-01/-04 and 1756 (DEF-130 items 1, 5) — through M, when M chooses.

## Drive actions for M

- **Upload** to Materials (`1XX_5f3PZB6tjRtiZ2GIgd8Tt7i_4GgkY`): `HANDOFF-90.md` and
  `The_Method_1_6_BUILD168_compendia_papers_audits.md`.
- **Retire** once BUILD168 gates PASS in chat 138: HANDOFF-89 and BUILD167 (HANDOFF-88 and BUILD166 were due under HANDOFF-89).
- **Keep:** BUILD90 main (still live — no BUILD91 was built); BUILD124; ARCHIVE1 permanently; the Prints & Proofs folder; the
  certificates; OWED-REGISTER-EXPANSIONS.md; OWED-EXPANSIONS-2.md; covers8.json; factor.py; the two delivery zips in their
  subfolders; **the project file COORDINATES-2_13.csv (r2-ch20a's golden reads it).**
- **When convenient:** DEF-130 items 1 and 5 to the three-body project; the pending bank to the Löwdin project (DEF-130 item 6).
  New this chat, for R3 (no action now): E.2 prints *518* where §23.10.4 prints 499 (24a-01); E.2's *Gröbner basis of eight* is the
  state §30.4.1 says was superseded at 18 (24a-02); E.4 has no heading (24b-02); Register 239 and 256 have no heading (24b-03).

## Prompt for chat 138

"Chat 138. READ EVERYTHING BEFORE YOU DO ANYTHING. Live files: BUILD90 main (1,983,081 B, md5
49065309b0c4fe8e055f693aed295cca) and BUILD168 compendia (4,780,462 B, md5 78daa717065a58b0698a18c27f20a0aa, 57,851 lines,
285 members); ARCHIVE1 (md5 5a5c0829fa234dde4f12ac240fc7dec4) is not fetched at the gate. List uploads, outputs and
/home/claude first. Run HANDOFF-90's §0 gate in full and in order — fetch both bundles by title, bootstrap with the script in
the handoff (decode, md5, extract, expect 287 files), fetch the Prints & Proofs original 'The Method 1.6.md' (738,550 B, md5
49900cf41f818ab789bb90fc596ac977) to /home/claude/PP_The_Method_1_6.md, then gate.py census, run --core, manifest, run
r2-ch24a r2-ch24b r2-ch23a r2-ch22a, cert 138; any FAIL stops the chat with a report. Then read, last blocks first:
RULINGS-R2.md (the chat-128 block), DOCKET.md (index plus the chat-128 to chat-137 deltas), DEFERRED.md (chat 137's block is the
last), READ-ch24a.md. The standing block's Phase 0–4 Löwdin/three-body plan is executed carried state; discard it per Ruling 41;
the intake is executed too. Line numbers are MEMBER line numbers and are never carried between chats, nor is any count or
heading list. Work in two segments and close each before the next opens. Segment A: the R2 unit Appendix E part 2, from
`### E.3` to `## Appendix F`, measured by your own scan at the first read call (≈ 168 lines — read whole; there is no `### E.4`
heading, its text is an unmarked line inside E.3), read as DATA under chat-127 item 1 with every Q item's E.3 entry resolved to its
site and its register entry under both resolvers, K, M, N and O's coordinates taken from E.3 and the thirteen-state and eleven-state
E(Q) re-taken under §6.1's ℛ with r2-ch24a's E_R and boxes copied with provenance, every status marker tested against its entry
and that entry's WARNING line, every printed count re-taken with the DATA-row set fixed and printed first, every ledger totals line
checked against its rows (§E.5's nine things vs eleven rows is 17c-01's site; L11165–L11168 the broken fraction), E.4.1's ruling
located, E.6 tested against §29.8 / §30.3, E.8's closures against E.1.1 and E.2; instruments r2-ch25a computable and r2-ch25b prose,
importing from r2lib by path, copying nothing but rbody, body_range and lettered from r2-ch24a with provenance comments, reading
MEMBERS never a bundle path; the appendix is pre-PP — diff its headings against PP from P10567 (PP's sub-headings are unmarked and
may lack the blank line above); read the WARNING line on every cited entry; Register 239 and 256 have no heading — search their
numerals inside other entries; grep the Register for a later entry naming the appendix before recording any figure as
unreproducible. Apply DOCKET.md's method throughout: name every convention before scoring, Decimal not round(), a Register entry
body is the first non-blank line after its heading, a first-person probe carries mine and myself and excludes the Roman numeral of
a species, a literal string is not a test, a count word counts DATA rows and the DATA-row set is fixed first, a whitespace table row
is parsed on a ≥ 2-space split where the ≥ 3-space split changes the column count and the difference is printed, a tie or
constraining count names its quantifier or test, a wrapped phrase is read on the markup-stripped join, a | at line start is a table
row only outside a code line, a numeral regex admits a trailing non-thousands comma, `## References` is the LAST heading hit not
the first, read every census row's class and detail before writing its verdict, give every negative its witness, record passes as
well as failures, expect the instrument to be wrong before the book. Bank both instruments by the 30th tool call. Segment B: bank
the goldens, pycache delete-only and never chained, W-178 ending with a blank line, DEF-138, DOCKET delta by --append, close.py to
BUILD169 with the reverse guard, HANDOFF-91 in this form BEFORE the final verification, begin the close with at least eight tool
calls left. Handoff at 90–95 % of context or on a closed segment — never mid-segment. Timeout on every call. Never copy over an
existing file."
