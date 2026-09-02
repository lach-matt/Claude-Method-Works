# HANDOFF-96 — The Method 1.6 — chat 143 → chat 144

Slim form (RULINGS-R2.md chat-127 item 5): identity, gate, next work, Drive actions, prompt. **The repair docket, the standing
method and the conventions live in `DOCKET.md` (index + chat-128 … chat-143 deltas); the findings in the READ-chNN.md /
READ-intake1.md / READ-warn.md / READ-ch34re.md members and WORKING-REGISTER.md; the deferred items in DEFERRED.md; the rulings
in RULINGS-R2.md.** Read all four at open, last blocks first.

## Identity

- Written from **chat 143** for **chat 144**. Live files: **BUILD90 main** (unchanged since chat 62) and **BUILD174 compendia**
  (= BUILD173 + W-183 + DEF-143 + DOCKET chat-143 delta + four members). Register **1 to 1792**. W-183 IS seated; chat 144 seats
  nothing at open. No rulings were taken in chat 143; nothing was put to M.
- **BUILD174** `The_Method_1_6_BUILD174_compendia_papers_audits.md` **5,321,034 B · md5 ca9319a8cf94c4ff276b3ccb5ab14a79 ·
  61,837 lines · 317 members** (reverse recovered 0fe1bce2…). ARCHIVE1 (5a5c0829…, 394 members) is NOT fetched at the gate.
- **Governing state** unchanged from HANDOFF-95: RUL-128 items 1–4, chat-81 cadence, chat-95 bar, chat-127 items 1, 2, 3, 5
  (executed), Register append-only, no silent change; the intake is executed (DOCKET item 38). The main volume is read in full;
  the Register WARNING sweep is closed (READ-warn.md).
- **RUL-128 item 3 (ii), second half, first family — the Chapter 34 re-take under docket 37 — is CLOSED** (r2-ch34re.py, golden
  846745bc, READ-ch34re.md). Measured on the delivered observed order (`LW1-ground.py`, Register 1306): the fourteen forced resets
  of 1401 / 1463 reproduce EXACTLY under form A (p = n−ℓ−1), 1403's eight a values 8 of 8, 106 of 106 corridors non-empty, nineteen
  surds under the n ≤ 8 generator; under form B (q/2(2ℓ+1)) the forced set is eleven. Seven A findings (34re-01 … 07): 16z-04's
  fifth-decimal numerals confirmed at main L9620 / Register 1330; the 8 / 6 / 4 reset split does not partition the record's eighteen
  on the delivered order (Rf 104 a fifth return; 1333 overlapping); *never resets mid-subshell* fails at Mo 42 / Rh 45 of 1401's own
  list; 1.785 / 1.028 is 0.25 % from √3 not 0.19 %, 1.028 unreproducible; the five withdrawn restatements re-confirmed; 15 of 19
  vs 17 by inversions; 5f opens with p = 1. Every walk figure beyond the corridor is a labelled reconstruction — walk.py / brack.py /
  scorer.py are not held (REQUEST-LOWDIN). DEF-143 items 1–11 and the DOCKET delta carry it.
- **Next work is RUL-128 item 3 (ii), second half — the SCF chain,** then in DEF-143 item 11's order: 21a-02/-03 with E.3's
  bracket site, 23a-03, 24a-05, 25b-03, 26b-04, 26b-02/-03, 27a-02's seven entries, 28a-06's author-and-year match, 28b-06's
  reading of 1721. One instrument per figure family, each banked; none edits a volume (chat-67 hold; R3 executes). A re-derivation
  that disagrees with a Register entry is a finding about the re-derivation until the original instrument is found (G0c).
- **The SCF chain is UNLOCATED as a family in this handoff** (INFERRED): chat 144 must locate it by reading before designing —
  grep the Register and the Mathematical Compendium for `SCF`, `self-consistent field`, `Hartree`, `Pulay`, `DIIS` and Chapter 35
  (`## 35.` main L9716 to `## 36.` L9892, measured this chat as section_span('34')'s end; re-take), read every entry the hits name,
  and census the printed figures before writing `r2-scf.py`. If the chain's inputs are delivered objects, they are the `LW1-*`
  members (READ-intake1.md: object 3 reproduced, the rest pending / not held) — a figure whose instrument is not held is
  UNREPRODUCIBLE with a stated budget, never withdrawn.
- **Open question of the standing block, still not put to M:** whether the five compendia need full source-order reads or the
  transversal sweeps suffice. Do not raise it unless M asks; the re-derivations are approved work.
- **Discipline note:** chat 143 banked at the 33rd call (budget 25th) and began the close at the 39th at ≈ 55 % context
  (INFERRED); seven instrument faults self-caught (the doubled-backslash regex and the endpoint-tie placement the instructive
  ones). Budget for chat 144: read the family's entries BEFORE the chapter, census first, ONE instrument; if the family will not fit
  with its close, split by figure sub-family BEFORE reading. Conventions earned this chat: entrant = the subshell that grows most;
  surds distinct at 10 dp with zero counted once; mid-subshell reset = entrant unchanged from Z−1.

## §0 Gate (each step its own tool call under `timeout 280`; any FAIL stops the chat with a report)

1. `ls -la /mnt/user-data/uploads /mnt/user-data/outputs /home/claude`; `recent_chats` (n=3) confirms the latest chat is 143.
   Read `/mnt/project/CLAUDE.md` (project instruction; never a member).
2. Fetch both bundles by title: `Google Drive:search_files` with
   `title contains 'BUILD174_compendia' or title contains 'BUILD90_main'`, pageSize 5, excludeContentSnippets;
   `Google Drive:download_file_content` on each fileId; note the spill paths `/mnt/user-data/tool_results/<id>.json`.
3. Bootstrap (the only step outside gate.py), verbatim, with the two spill paths filled in:

```
cd /home/claude && timeout 280 python3 - <<'EOF'
import json, base64, hashlib, re, os
EXP={'main':'49065309b0c4fe8e055f693aed295cca','comp':'ca9319a8cf94c4ff276b3ccb5ab14a79'}
NAME={'main':'/home/claude/The_Method_1_6_BUILD90_main_and_register.md','comp':'/home/claude/The_Method_1_6_BUILD174_compendia_papers_audits.md'}
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
   Expected: main 1,983,081 B · 18,470 lines; compendia **5,321,034 B · 61,837 lines**; **319 members extracted (2 + 317)**.
4. Fetch the Prints & Proofs original before step 7: folder `1vYctzLppUZ2vFPJDCZ6wvkgSdj3v_f6n`, fileId
   `1vsWwRT9BmUNeMrqokuo4jI4DJnoADubH`, **738,550 B · md5 49900cf41f818ab789bb90fc596ac977 · 11,371 lines**, decoded the same way
   to `/home/claude/PP_The_Method_1_6.md` (assert the md5 and `not os.path.exists`). r2-ch28b reads it there.
5. `gate.py census` → `OK census: DEFECT-CENSUS.tsv byte-identical` (1,556 rows + header, ≈ 14 s).
6. `gate.py run --core` → five `OK` (tower 976/1,654/2,535/13,585/70,905/199,130; kinds 1565 · 1356 · 499 · 149; minmax;
   r2-tools-constants; extent "1 to 1792").
7. `gate.py manifest` → `MANIFEST OK`; MANIFEST.tsv **21,406 B · 0cc1feaadf374928c1f0ab804c74ff26 · 319 lines**;
   WORKING-REGISTER.md **875,278 B · 5447e791085961bbf4e291af283d67d9 · 7,916 lines**, ends **W-183**; RULINGS-R2.md ends with
   the chat-128 block (unchanged); DEFERRED.md's last block is chat 143's; DOCKET.md ends with the chat-143 delta.
8. `gate.py run r2-ch34re r2-warn r2-ch28b` → three `OK` (r2-ch34re.out 20,928 B · 846745bc · 250 lines, ≈ 1 s, reads
   LW1-ground.py and tower-2 by path; r2-warn.out 38,680 B · 3616f059; r2-ch28b.out 25,818 B · b279000e, ≈ 22 s, needs PP).
   **The project file COORDINATES-2_13.csv must stay** (r2-ch20a's and r2-ch26a's goldens read it).
9. `gate.py cert 144` → `/home/claude/GATE-ch144.txt`, verdict PASS only if every step passed.
10. `rm -rf /home/claude/members/__pycache__` — its own delete-only call, after every run or bank, never chained.

## Chat 144's work order (two segments; each closed before the next opens)

**Segment A — the SCF chain (RUL-128 item 3 (ii), second half, second family), instrument `r2-scf.py`, one banked golden.**
Locate first (see Identity): grep the Register, the Mathematical Compendium and the Physics Compendium for the chain's tokens; read
every Register entry named, rbody and the whole entry to the next heading of either form, WARNING lines first; then the main-volume
section(s) that print the chain (Chapter 35 is the likely home — measure with heading_line('35') body occurrence, section_span AND
body_range; never span by rank). Census every printed figure (numeral regex digit-bounded, trailing non-thousands comma admitted;
count words). Re-derive each on the instruments the bundle holds (tower-2 via r2lib.load_tower(); the `LW1-*` members by path) —
Decimal, never round(); name every convention before scoring. For every figure: MEASURED equal / MEASURED differs (with the
Register's later statement, grepped first) / UNREPRODUCIBLE with a stated budget. Write READ-scf.md (A / B / C) and
CENSUS-CLOSURES-scf.tsv (header only if no row is engaged). Copy `rbody`, `body_range`, `lettered` from r2-ch34re.py with
provenance comments; read MEMBERS never a bundle path; expect the instrument to be wrong before the book.

**Segment B — close:** bank the golden; pycache delete-only; W-184 (ends with a blank line); DEF-144; DOCKET delta by
`--append`; close.py BUILD174 → BUILD175 (reverse must recover ca9319a8…; `--append` before `--members`); HANDOFF-97 in this
form BEFORE the final verification; ≥ 8 calls left at the start. **Tool-call ceiling:** if calls run out mid-segment, close it as
failed with diagnosis and let M's *Continue* re-open the container (which persists within a chat).

**Standing after the SCF chain:** the listed re-derivations in DEF-143 item 11's order, one instrument per family, each banked;
then R3 by class in mathematics-first order (RUL-128 item 1; the held withdrawn-law class executes after — DOCKET item 12's 16z-04
numerals now measured are R3's first arithmetic item), each change through a guarded build with a Register entry; then R4.
The three-body project owes a reply on intake1-01/-04 and 1756 (DEF-130 items 1, 5) — through M, when M chooses.

## Drive actions for M

- **Upload** to Materials (`1XX_5f3PZB6tjRtiZ2GIgd8Tt7i_4GgkY`): `HANDOFF-96.md` and
  `The_Method_1_6_BUILD174_compendia_papers_audits.md`.
- **Retire** once BUILD174 gates PASS in chat 144: HANDOFF-95 and BUILD173 (HANDOFF-94 and BUILD172 were due under HANDOFF-95 —
  BUILD173 gated PASS in chat 143, so they may go now).
- **Keep:** BUILD90 main (still live — no BUILD91 was built); BUILD124; ARCHIVE1 permanently; the Prints & Proofs folder; the
  certificates; OWED-REGISTER-EXPANSIONS.md; OWED-EXPANSIONS-2.md; covers8.json; factor.py; the two delivery zips in their
  subfolders; **the project file COORDINATES-2_13.csv.**
- **When convenient:** DEF-130 items 1 and 5 to the three-body project; the pending bank to the Löwdin project (DEF-130 item 6) —
  now also the walk instruments behind 1402 / 1445 / 1448 (walk.py / brack.py / scorer.py) and the per-element a values, which
  DEF-143 items 2 and 4 budget against; the muon paper's instrument for L11600–L11602 (DEF-141 item 4).

## Prompt for chat 144

"Chat 144. READ EVERYTHING BEFORE YOU DO ANYTHING. Live files: BUILD90 main (1,983,081 B, md5
49065309b0c4fe8e055f693aed295cca) and BUILD174 compendia (5,321,034 B, md5 ca9319a8cf94c4ff276b3ccb5ab14a79, 61,837 lines,
317 members); ARCHIVE1 (md5 5a5c0829fa234dde4f12ac240fc7dec4) is not fetched at the gate. List uploads, outputs and
/home/claude first. Run HANDOFF-96's §0 gate in full and in order — fetch both bundles by title, bootstrap with the script in
the handoff (decode, md5, extract, expect 319 files), fetch the Prints & Proofs original 'The Method 1.6.md' (738,550 B, md5
49900cf41f818ab789bb90fc596ac977) to /home/claude/PP_The_Method_1_6.md, then gate.py census, run --core, manifest, run
r2-ch34re r2-warn r2-ch28b, cert 144; any FAIL stops the chat with a report. Then read, last blocks first: RULINGS-R2.md (the
chat-128 block), DOCKET.md (index plus the chat-128 to chat-143 deltas), DEFERRED.md (chat 143's block is the last),
READ-ch34re.md, READ-warn.md §0. The standing block's Phase 0–4 Löwdin/three-body plan is executed carried state; discard it
per Ruling 41; the intake is executed too. The main volume is read in full, the Register WARNING sweep and the Chapter 34
re-take are closed; no section read remains — do not open one. Line numbers are MEMBER line numbers and are never carried
between chats, nor is any count, heading list or figure list. Work in two segments and close each before the next opens.
Segment A: the SCF chain (RUL-128 item 3 (ii), second half, second family) as instrument r2-scf.py — locate the family by
reading first (grep the Register, the Mathematical and Physics Compendia for SCF / self-consistent field / Hartree / Pulay /
DIIS and Chapter 35; read every entry named, WARNING lines first), then measure the printing section under both resolvers,
census every printed figure, re-derive each on the instruments the bundle holds, Decimal not round(), every convention named
before scoring, the Register grepped for a later statement before any figure is called unreproducible, a rebuild that
contradicts an entry a finding about the rebuild, a figure whose instrument is not held UNREPRODUCIBLE with a budget and never
withdrawn; READ-scf.md and CENSUS-CLOSURES-scf.tsv; import from r2lib by path, copy nothing but rbody, body_range and lettered
from r2-ch34re.py with provenance comments, read MEMBERS never a bundle path; split by figure sub-family BEFORE reading if the
family will not fit with the close. Apply DOCKET.md's method throughout: a Register entry body is the first non-blank line after
its heading and headings come in two forms, a WARNING: marker is the colon form, a literal string is not a test, a count word
counts DATA rows, give every negative its witness, record passes as well as failures, expect the instrument to be wrong before
the book. Bank the golden by the 25th tool call. Segment B: bank, pycache delete-only and never chained, W-184 ending with a
blank line, DEF-144, DOCKET delta by --append, close.py to BUILD175 with the reverse guard, HANDOFF-97 in this form BEFORE the
final verification, begin the close with at least eight tool calls left. Handoff at 90–95 % of context or on a closed segment —
never mid-segment. Timeout on every call. Never copy over an existing file."
