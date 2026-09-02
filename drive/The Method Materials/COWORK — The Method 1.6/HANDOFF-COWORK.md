# HANDOFF-COWORK.md — The Method 1.6 — from claude.ai chat 143 into a Claude Cowork project

Written from chat 143 (BUILD174, Register 1 to 1792, W-183 seated). This file carries the project into Cowork; HANDOFF-96.md
(in Materials) carries the WORK — chat 144's gate and work order are unchanged and are executed by the first Cowork session.
Nothing in the governing files changes: CLAUDE.md, RULINGS-R2.md, DOCKET.md, DEFERRED.md, WORKING-REGISTER.md govern as before.
Where this file and a ruling disagree, the ruling governs.

## 1. What changes and what does not

- **Drive stays the store of record** (chat-68 ruling; chat-74 item 1). Cowork reads Materials through the same Google Drive
  connector the chats used, by title search and fileId, and WRITES each close's new BUILD and HANDOFF back into Materials as NEW
  files (the connector cannot edit an existing Drive file — which matches the regime: a build is always a new upload, never an edit).
- **The gate and the close are instruments** (chat-74 item 2) and they travel INSIDE the compendia bundle as members (gate.py,
  close.py, r2lib.py, tower-2.py, the goldens). Nothing needs to be installed locally: the bootstrap extracts them. The Cowork
  project's local folder is a scratchpad only; never point it at a Drive-for-Desktop mount (Cowork cannot use one).
- **A Cowork session still opens on a fresh context.** The handoff shrinks (no bootstrap script to carry once the kit below is
  proven) but does not vanish: every session still opens by reading the last HANDOFF, the four governing members' last blocks, and
  the READ file of the previous session, and still closes with W-NNN, DEF-NNN, the DOCKET delta, close.py and a HANDOFF.
- **The Drive spill path changes.** In the chats a large download spilled to `/mnt/user-data/tool_results/<id>.json`. In Cowork the
  connector's return is handled by the sandbox; the first session MEASURES where the bytes land and how they decode (base64 with
  `validate=True`, md5 asserted) and records the measured path and decode in W-184 and in HANDOFF-97 — never assumes the chat path.
- **Chat numbering continues:** the first Cowork session is chat 144. `recent_chats` may not exist in Cowork; if it does not, the
  G1 identity step is the HANDOFF's own chat number plus the Register range and build md5 agreeing with the files (self-identifying
  handoffs), and W-184 records that `recent_chats` was unavailable.
- **Everything else is identical:** two segments per session, each closed before the next; bank by the 25th call; handoff at
  90–95 % context or on a closed segment, never mid-segment; `timeout 280` on every call; delete-only calls stand alone; never copy
  over an existing file; a finding is not a question; nothing goes to M that a file can settle.

## 2. The Drive map (fileIds are stable; titles are searched, never assumed)

| object | where | id / search |
|---|---|---|
| Materials (restore packs, deliveries, HANDOFFs, BUILDs) | folder | `1XX_5f3PZB6tjRtiZ2GIgd8Tt7i_4GgkY` |
| **COWORK — The Method 1.6** (this file; Cowork's own notes) | folder in Materials | `14gpvC0sxSgJHxUCKBHXiak9a5xWvaqnp` |
| Prints & Proofs folder (original-input witness, Ruling 56) | folder | `1vYctzLppUZ2vFPJDCZ6wvkgSdj3v_f6n` |
| Prints & Proofs original `The Method 1.6.md` | file | `1vsWwRT9BmUNeMrqokuo4jI4DJnoADubH` · 738,550 B · md5 49900cf41f818ab789bb90fc596ac977 |
| BUILD90 main (live; unchanged since chat 62) | file in Materials | `1lJ9R3vqAz3TNriJOyxJIKJGh5HqwY7GH` · 1,983,081 B · md5 49065309b0c4fe8e055f693aed295cca |
| BUILD174 compendia (live after chat 143) | file in Materials | search `title contains 'BUILD174_compendia'` · 5,321,034 B · md5 ca9319a8cf94c4ff276b3ccb5ab14a79 · 317 members |
| HANDOFF-96.md (chat 144's gate and work order) | file in Materials | search `title contains 'HANDOFF-96'` |
| ARCHIVE1 (never fetched at the gate) | file in Materials | md5 5a5c0829fa234dde4f12ac240fc7dec4 |
| LOWDIN-DELIVERY-1/, THREEBODY-DELIVERY-1/ | subfolders of Materials | `parentId = '1XX_5f3PZB6tjRtiZ2GIgd8Tt7i_4GgkY' and title contains 'DELIVERY'` |
| COORDINATES-2_13.csv | claude.ai project file — **must be copied into the Cowork project's files** | r2-ch20a / r2-ch26a goldens read `/mnt/project/COORDINATES-2_13.csv`; in Cowork the first session measures the path it lands at and, if it differs, records the substitution as an instrument fault repaired in place (never trimmed) |
| CLAUDE.md | claude.ai project file — **paste as the Cowork project instructions** (never a bundle member) | §3 below |

**Do not duplicate BUILD90, BUILD174 or Prints & Proofs into the COWORK folder.** The gate finds bundles by title search across
Drive; a second copy makes `title contains 'BUILD90_main'` return two files and the gate must then stop. One copy, in Materials.

## 3. Setting up the Cowork project (M does this once)

1. Update Claude Desktop; open Cowork; create a project from a NEW empty local folder (e.g. `~/Method-1.6-cowork`). Name it
   *The Method 1.6*.
2. Connectors: connect Google Drive (the same account that owns Materials). Confirm the connector lists `search_files`,
   `download_file_content`, `create_file`, `get_file_metadata` — the four the gate and the close use.
3. Project **instructions**: paste the whole of CLAUDE.md, then append this line at the end:
   *"This is a Cowork session. Drive is the store: fetch by title and fileId through the Google Drive connector, decode with
   validate=True, assert every md5; write each close's BUILD and HANDOFF back to Materials as new files; never point the project at
   a Drive mount; measure the download path and decode before relying on them."*
4. Project **files**: add COORDINATES-2_13.csv (from the claude.ai project) and this HANDOFF-COWORK.md. Nothing else — the bundles
   are fetched, never stored in the project.
5. **Global instructions** (Settings → Cowork): the one-line style rule from the standing block — *focused and brief; caveats short;
   deliver what was asked, raise a better approach in one sentence, then proceed as asked; keep internal tags out of responses.*
6. Permissions: leave approvals ON for Drive writes (the close uploads two files; approve them); do not use "skip all approvals".
7. Retirements are unchanged: after BUILD174 gates PASS in chat 144, retire HANDOFF-95 and BUILD173 (HANDOFF-94 and BUILD172 now).

## 4. The first Cowork session (chat 144) — what differs from HANDOFF-96's §0

Run HANDOFF-96's §0 gate exactly, with these measured substitutions recorded in W-184:

- Step 1: list the Cowork working folder and the project files instead of `/mnt/user-data/uploads`; find COORDINATES-2_13.csv and
  CLAUDE.md by listing, record their paths. `recent_chats` if available; else the self-identity check of §1.
- Step 2–3: fetch BUILD90 main and BUILD174 by title; **measure how the connector returns a 5 MB file in this sandbox** (spill file,
  inline base64, or a saved path) BEFORE writing the bootstrap; then run HANDOFF-96's bootstrap verbatim with the measured source
  filled in. Expected: main 1,983,081 B · 18,470 lines; compendia 5,321,034 B · 61,837 lines; 319 members extracted. Any md5 FAIL
  stops the session with a report.
- Step 4: Prints & Proofs by fileId, same decode, md5 49900cf4…, to `<workdir>/PP_The_Method_1_6.md`. If r2-ch28b's golden hard-codes
  `/home/claude/PP_The_Method_1_6.md`, create that path if the sandbox allows, else record the fault, repair the instrument's path
  constant in place, re-bank under a delete-only call first, and note it as *instrument wrong, book right*: 0 — a path, not a claim.
- Steps 5–10 unchanged: `gate.py census` / `run --core` / `manifest` / `run r2-ch34re r2-warn r2-ch28b` / `cert 144` / pycache delete-only.
- Then HANDOFF-96's work order: Segment A the SCF chain (`r2-scf.py`), Segment B the close to BUILD175 — and at the close, upload
  BUILD175 and HANDOFF-97 into Materials through the connector (`create_file`, contentMimeType text/markdown, conversion disabled),
  then read them back by fileId and assert bytes and md5 before declaring the close done. That replaces "Drive actions for M: upload".
- HANDOFF-97 is written in HANDOFF-96's form PLUS a §0a *Cowork measured environment* block: the download path/decode, the PP path,
  the COORDINATES path, whether `recent_chats` exists, and the tool-call and context behaviour observed — so chat 145 assumes nothing.

## 5. The prompt for the first Cowork session

"Chat 144 — first Cowork session. READ EVERYTHING BEFORE YOU DO ANYTHING: this project's instructions (CLAUDE.md), the project
file HANDOFF-COWORK.md in full, then HANDOFF-96.md from Materials (search title contains 'HANDOFF-96'). Live files: BUILD90 main
(1,983,081 B, md5 49065309b0c4fe8e055f693aed295cca) and BUILD174 compendia (5,321,034 B, md5 ca9319a8cf94c4ff276b3ccb5ab14a79,
61,837 lines, 317 members); ARCHIVE1 is not fetched. Run HANDOFF-96's §0 gate in full and in order with HANDOFF-COWORK §4's
measured substitutions — measure how the Drive connector delivers a large file in this sandbox before writing the bootstrap; decode
with validate=True; assert every md5; any FAIL stops the session with a report. Then read, last blocks first: RULINGS-R2.md (the
chat-128 block), DOCKET.md (index plus the chat-128 to chat-143 deltas), DEFERRED.md (chat 143's block is the last), READ-ch34re.md,
READ-warn.md §0. The main volume is read in full, the Register WARNING sweep and the Chapter 34 re-take are closed; no section read
remains. Work in two segments and close each before the next opens: Segment A the SCF chain as r2-scf.py per HANDOFF-96 (locate the
family by reading first; every convention named; Decimal not round(); the Register grepped before any figure is called
unreproducible; a rebuild that contradicts an entry a finding about the rebuild; READ-scf.md and CENSUS-CLOSURES-scf.tsv; bank by the
25th tool call); Segment B the close (bank, pycache delete-only and never chained, W-184 ending with a blank line and recording the
measured Cowork environment, DEF-144, DOCKET delta by --append, close.py to BUILD175 with the reverse guard, HANDOFF-97 in
HANDOFF-96's form plus the §0a environment block BEFORE the final verification, then upload BUILD175 and HANDOFF-97 to Materials
through the connector and read them back to assert bytes and md5). Handoff at 90–95 % of context or on a closed segment — never
mid-segment. Timeout on every call. Never copy over an existing file. Never duplicate a bundle into the COWORK folder."
