# HANDOFF-81 — The Method 1.6 — chat 128 → chat 129

Slim form (RULINGS-R2.md chat-127 item 5): identity, gate, next work, Drive actions, prompt. **The repair docket,
the standing method and the conventions live in `DOCKET.md` (read its chat-128 delta with the index); the findings
in the READ-chNN.md members and WORKING-REGISTER.md; the deferred items in DEFERRED.md; the rulings in
RULINGS-R2.md.** Read all four at open, last blocks first.

## Identity

- Written from **chat 128** for **chat 129**. Live files: **BUILD90 main** (unchanged since chat 62) and
  **BUILD158 compendia** (= BUILD157 + W-168 + RUL-128 + DEF-128 + DOCKET delta + ten members). Register
  **1 to 1792**. W-168 IS seated; chat 129 seats nothing at open.
- **Governing state after chat 128's rulings** (RULINGS-R2.md, last block; M verbatim there): (1) every claim
  true and proven; the order of correction is **mathematics → prose → appendices/indices**; (2) the
  withdrawn-law class (chat-127 item 4) is **HELD** — wording approved, `r3-wl.py` + `r3-wl.out` specify the
  repair on BUILD90, BUILD91 NOT built; it executes in R3 after docket 37's re-take; (3) the audit order
  approved: close the main volume; then the Register WARNING sweep and every computable claim re-derived by
  instrument (Chapter 34 re-take and the SCF chain first); then R3 in the order of (1); then R4; (4) the Löwdin
  and three-body projects are asked for their instruments (REQUEST-LOWDIN.md, REQUEST-THREEBODY.md, members);
  deliveries arrive in Materials subfolders **`LOWDIN-DELIVERY-1/`** and **`THREEBODY-DELIVERY-1/`**.
  Everything else stands: chat-81 cadence, chat-95 bar, chat-127 items 1, 2, 3, 5, no other corrections,
  Register append-only, no silent change.
- **Main volume 82.7 % read (L9805 of 11,855).** Chapter 35's first unit is CLOSED (READ-ch17a.md).
- **MEASURED heading lines this chat, to be re-taken by your own scan:** §35.4 **L9806**, §35.5 **L9858**,
  §35.6 **L9872**, `## 36.` body **L9892**, `# APPENDICES` **L9937**, Appendix A **L9939**. Carried from
  HANDOFF-80, not re-measured: B L10165, C L10230, D L10320, E L10898, F L11222, G L11361, `## Index` L11409,
  `## References` body L11503 (R.7 L11806 MEASURED). **Chat 129's R2 unit is §35.4–§35.6, L9806–L9891, 86
  lines** (closes Chapter 35). PP's `# APPENDICES` body is **P9590** (own scan; HANDOFF-80's 9591 was off by one).

## §0 Gate (each step its own tool call under `timeout 280`; any FAIL stops the chat with a report)

1. `ls -la /mnt/user-data/uploads /mnt/user-data/outputs /home/claude`; `recent_chats` confirms the latest chat
   is 128. Read `/mnt/project/CLAUDE.md` (project instruction; never a member).
2. Fetch both bundles by title: `Google Drive:search_files` with
   `title contains 'BUILD158_compendia' or title contains 'BUILD90_main'`, pageSize 5, excludeContentSnippets;
   `Google Drive:download_file_content` on each fileId; note the spill paths `/mnt/user-data/tool_results/<id>.json`.
3. Bootstrap (the only step outside gate.py): HANDOFF-80's script verbatim with
   `EXP={'main':'49065309b0c4fe8e055f693aed295cca','comp':'3fc4111aea078f7b78fdc5b5cd1f4b0e'}` and the comp
   NAME `/home/claude/The_Method_1_6_BUILD158_compendia_papers_audits.md`. Expected: main 1,983,081 B ·
   18,470 lines; compendia **7,617,311 B · 100,429 lines**; **600 members extracted (2 + 598)**.
4. Fetch the Prints & Proofs original before step 7: folder `1vYctzLppUZ2vFPJDCZ6wvkgSdj3v_f6n`, title
   `The Method 1.6.md`, fileId `1vsWwRT9BmUNeMrqokuo4jI4DJnoADubH`, **738,550 B · md5
   49900cf41f818ab789bb90fc596ac977 · 11,371 lines**, to `/home/claude/PP_The_Method_1_6.md` (assert the md5
   and `not os.path.exists`). r2-ch17a reads it.
5. `gate.py census` → `OK census: DEFECT-CENSUS.tsv byte-identical` (1,556 rows + header, ≈ 15 s).
6. `gate.py run --core` → five `OK` (tower 976/1,654/2,535/13,585/70,905/199,130; kinds 1565 · 1356 · 499 ·
   149; minmax; r2-tools-constants; extent "1 to 1792").
7. `gate.py manifest` → `MANIFEST OK`; MANIFEST.tsv **40,202 B · 0b183e882278921e3259c4559bf89a7a · 600
   lines**; WORKING-REGISTER.md **817,714 B · 2ad8b45f3b3f44a53805a52a6e062895 · 7,618 lines**, ends **W-168**;
   RULINGS-R2.md ends with the **chat-128 block (four items)**; DEFERRED.md's last block is chat 128's;
   DOCKET.md ends with the chat-128 delta.
8. `gate.py run r2-ch17a r2-ch17b r3-wl` → three `OK` (r2-ch17a.out 9,917 B · 95c21429 · 107 lines;
   r2-ch17b.out 11,834 B · b3983a50 · 117 lines; r3-wl.out 3,638 B · 1bb27e47 · 31 lines — its dry run
   writes only a fresh /tmp scratch).
9. `gate.py cert 129` → `/home/claude/GATE-ch129.txt`, verdict PASS only if every step passed.
10. `rm -rf /home/claude/members/__pycache__` — its own delete-only call, after every run or bank, **never
    chained** (chat 128 chained one and recorded it, W-168).
11. **Intake check (one call):** `Google Drive:search_files` with `parentId = '1XX_5f3PZB6tjRtiZ2GIgd8Tt7i_4GgkY'`
    and `title contains 'DELIVERY'`, excludeContentSnippets. If `LOWDIN-DELIVERY-1` or `THREEBODY-DELIVERY-1`
    exists, list it, record its manifest in W-169, and schedule intake as chat 130's first segment under
    RUL-128 item 4 (validation block + golden + Register entry per object); do not seat anything in chat 129.

## Chat 129's work order (three segments; each closed before the next opens)

**Segment A — the archive split (chat-127 item 5)**, as HANDOFF-80 specified: partition MEASURED in W-167 —
archive = the 48 legacy `HANDOFF-*.md` + `r2-ch12*…r2-ch15*` instruments and goldens + `READ-ch1[2-5]*` and
`CENSUS-CLOSURES-ch1[2-5]*` (393 members, 3.7 MB); live = the rest. Re-measure the partition on BUILD158 first
(598 members now). Write the archive bundle first, the live bundle second, each with its own manifest and
reverse-recovery guard (close.py cannot do this: write a `split.py`-class instrument as a new member, bank
its dry run as a golden, as `r3-wl.py` did); gate.py then verifies the live bundle alone and the archive by
md5 on demand; record both identities in W-169 and HANDOFF-82. If the machinery does not close inside the
chat, close the segment as failed with diagnosis and leave BUILD158 live. The bundle is at 7.6 MB against
Drive's 10 MB cap: the split is due.

**Segment B — the R2 unit L9806–L9891** under the chat-81 cadence, instruments **r2-ch17c** (computable) and
**r2-ch17d** (prose); import heading_line, section_span, has_token, enclosing from r2lib by path, the NIST
table from r2-ch16y.py §3 by path (stdout captured, as r2-ch17a does), and copy `rbody` and `body_range` from
r2-ch17a/b with provenance comments. DEF-128 item 8 lists the unit's own tests: §E.5's *nine things* counted
at §E.5's body; *the twenty-two audits* L9824 against §3; Pulay / Griffin / Andrew / Cowan against the
References body (1 / 2 / 3 / 4 measured) and R.7 (1 / 2 / 2 / 2); L9866–L9867's table restating eleven elements
and twelve rows; L9870 *No parameter is fitted. No observation enters upstream of the score* is the
derivation's own claim, not a 16z-01 site; *unwitnessed* against register 1446 (edge 102, 17a-02). State once
that the unit is post-PP and do not diff it.

**Segment C — close:** bank both goldens; pycache delete-only; W-169 (ends with a blank line); DEF-129; DOCKET
delta by `--append`; close.py from the live bundle to the next (reverse must recover its md5; `--append`
before `--members`); HANDOFF-82 in this form BEFORE the final verification; ≥ 8 calls left at the start.

**After the main volume closes (about 11 sessions at 116 lines/session, INFERRED; fewer with chat-127 item 1
on Appendices D–G):** RUL-128 item 3's order — the Register WARNING sweep first, then the computable
re-derivations, the Chapter 34 re-take (docket 37) and the SCF chain (when delivered) first among them.

## Drive actions for M

- **Upload** to Materials (`1XX_5f3PZB6tjRtiZ2GIgd8Tt7i_4GgkY`): `HANDOFF-81.md` and
  `The_Method_1_6_BUILD158_compendia_papers_audits.md`.
- **Hand to the two projects:** `REQUEST-LOWDIN.md` and `REQUEST-THREEBODY.md`; their deliveries go to
  Materials subfolders `LOWDIN-DELIVERY-1/` and `THREEBODY-DELIVERY-1/`.
- **Retire** once BUILD158 gates PASS in chat 129: HANDOFF-80, BUILD157, and BUILD107–BUILD156 **except
  BUILD124** (its `r2-ch14l`/`r2-ch14m` reproduce only there).
- **Keep:** BUILD90 main (still live — no BUILD91 was built); the Prints & Proofs folder; the certificates;
  OWED-REGISTER-EXPANSIONS.md; OWED-EXPANSIONS-2.md; covers8.json; factor.py.

## Prompt for chat 129

"Chat 129. READ EVERYTHING BEFORE YOU DO ANYTHING. Live files: BUILD90 main (1,983,081 B, md5
49065309b0c4fe8e055f693aed295cca) and BUILD158 compendia (7,617,311 B, md5 3fc4111aea078f7b78fdc5b5cd1f4b0e,
100,429 lines, 598 members). List uploads, outputs and /home/claude first. Run HANDOFF-81's §0 gate in full
and in order — fetch both bundles by title, bootstrap (decode, md5, extract, expect 600 files), fetch the
Prints & Proofs original 'The Method 1.6.md' (738,550 B, md5 49900cf41f818ab789bb90fc596ac977) to
/home/claude/PP_The_Method_1_6.md, then gate.py census, run --core, manifest, run r2-ch17a r2-ch17b r3-wl,
cert 129, the intake check; any FAIL stops the chat with a report. Then read, last blocks first: RULINGS-R2.md
(the chat-128 block: mathematics before prose before appendices; the withdrawn-law class HELD; the audit
order; the two project requests), DOCKET.md (index plus its chat-128 delta), DEFERRED.md (chat 128's block is
the last), READ-ch17a.md, and R3-CLASS-WL.md with r3-wl.py. The standing block's Phase 0–4 Löwdin/three-body
plan is executed carried state; discard it per Ruling 41. Line numbers are MEMBER line numbers and are never
carried between chats, nor is any count or heading list. Work in three segments and close each before the
next opens. Segment A: the archive split as HANDOFF-81 specifies — re-measure the partition on BUILD158,
write the archive bundle then the live bundle through a new split instrument with its own reverse-recovery
guard, bank its dry run, verify by reading both bundles; if it cannot close inside the chat, close it as
failed with diagnosis and leave BUILD158 live. Segment B: the R2 unit L9806–L9891, §35.4–§35.6, 86 lines,
closing Chapter 35, not split; take the heading lines by your own scan resolving each to its BODY occurrence;
resolve every pointer under both body_range and section_span and bound the unit by body_range; read the unit
in full, census its claims into computable and prose, run exactly two batches, r2-ch17c computable and
r2-ch17d prose, importing from r2lib by path and the NIST table from r2-ch16y.py §3 by path with stdout
captured, copying nothing but rbody and body_range with provenance comments, reading MEMBERS never a bundle
path; measure the unit's own claims listed in DEF-128 item 8; the 16z-01 sites are unrepaired on BUILD90 —
record members, do not score them twice; state once that the unit is post-PP and do not diff it. Apply
DOCKET.md's method throughout: name every convention before scoring, Decimal not round(), read the WARNING
line on every cited entry, a Register entry body is the first non-blank line after its heading, a
first-person probe carries mine and myself, a literal string is not a test, a count word counts DATA rows,
give every negative its witness, record passes as well as failures, expect the instrument to be wrong before
the book. Segment C: bank both goldens, pycache delete-only and never chained, W-169 ending with a blank line,
DEF-129, DOCKET delta by --append, close.py to the next live bundle with the reverse guard, HANDOFF-82 in this
form BEFORE the final verification, begin the close with at least eight tool calls left. Handoff at 90–95 % of
context or on a closed segment — never mid-segment. Timeout on every call. Never copy over an existing file."
