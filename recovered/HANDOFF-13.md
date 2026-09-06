# HANDOFF-13 — The Method 1.6

## SELF-IDENTIFICATION (the three must agree with the files)
- Written from **chat 63** (project title; HANDOFF-11-1.md called this session "chat 62" — the chat that produced BUILD75/HANDOFF-11 is titled 62), for **chat 64**.
- Builds it describes: **BUILD76 main** + **BUILD79 compendia** (BUILD77/78 were intra-chat steps).
- Register range: **1 to 1787** (1787 appended this chat; extent restated at all 17 main-volume sites + front matter; kinds table recomputed).

## §0 GATE (run first in chat 64 — executable, able to FAIL)
1. Fetch from Drive Materials (folder 1XX_5f3PZB6tjRtiZ2GIgd8Tt7i_4GgkY): `The_Method_1_6_BUILD76_main_and_register.md`, `The_Method_1_6_BUILD79_compendia_papers_audits.md`, `tower-2.py` (id 1IyXbZhMH5pemrSoahnDRJSR4horhRpZY).
   Large files spill to /mnt/user-data/tool_results/<id>.json → `base64.b64decode(json.loads(json.load(open(p))[0]['text'])['content'], validate=True)`. Small files: use download_file_content (inline base64; decode with validate=True; check byte count against Drive's fileSize) — read_file_content mangles indentation.
2. Verify: **BUILD76 main 1,977,372 B · md5 a4fbbc49d58ec6c6d6dd71a13f116765 · 18,452 lines**; **BUILD79 compendia 2,462,001 B · md5 d0201721d2793a9c000f5af18e89d6c8 · 32,793 lines**; tower-2.py 1,213 B · md5 c0bce27abe23ad939d297ac1022a01d7.
3. Rebuild: tower.py must print **976 / 1,654 / 2,535 / 13,585 / 70,905 / 199,130** exactly.

## WHAT CLOSED IN CHAT 63 (all M-approved by slip; every build measured-diff guarded, reverse diff recovers the prior md5)
- **PRIORITY DEFECT CLOSED (BUILD56 → BUILD76 main).** §31.2.2 said log d(N) "convex"; measured concave (2nd differences −0.313…−0.032, N=2..15), monotone ✔, 3-monotone ✔ (3rd diffs +0.104…+0.003), V(log d) at N=14 = 146.6 = the book's V≈147. §23.10.1 defines the order words as finite-difference signs (ordinary sense). Book wrong on one word; reconstruction right. d(N) verified by two routes (series; Euler σ-recurrence). §31.2.2 restated with the three signs + "recorded at register 1787"; **Register 1787** appended (a correction; cites no register — none exists behind §31.2). Exhaustive casualty sweep: ONE site in the six volumes; IoI string-PF entry NOT revised (M asked; nothing in it touched). Certificate: STRINGPF-CONVEXITY-RESOLVED.md (on Drive).
- **TASK 1 COMPENDIUM REVIEW PASS — steps 1–3 done (BUILD75 → 77 → 78 → 79 compendia).**
  Rulings (M): all 266 old-form entries convert now; captions reduced to stated facts (no volume describes a figure not present for the reader); titles: L.c1/L.c4 → node counting, ℓ ≤ n − 1 / f ≤ e − 1; L.c2/L.c5 → Pauli, k ≤ 4ℓ + 2 / g ≤ 4f + 2; Q.delta/Q.final → the channel equation, first form / final form; "· **GRADED OPEN**" suffixes dropped; section V chains CONVERTED; PRIOR ART → Prior art.
  Step 1 (BUILD77): convert.py (banked on Drive) — 266 headers → descriptive titles; 266 `grade·source·depends·depth` lines → `Grade — citations.`; 309 handle mentions → titles with pointer on first mention per entry; 0 handles left in the four reader compendia; 13 backticked instrument/data file names remain (Ruling 60 press-time substitution); bibliography citing-objects column (410 tokens) UNTOUCHED → task 3. Certificate CONVERSION-CERTIFICATE-BUILD77.md (Drive).
  Step 2 (BUILD78): IoI's 8 figure captions → stated facts (7 changed; Figure 4 took 11.6/40.7 and 89.7/77.9 from the entry beneath).
  Step 3 (BUILD79): remaining 9 captions (Math 2, Spectra 5, Physics 2) read, left standing; rhetoric screen run; 7 aside sites cut (IoI "certifies nothing" clause; "sits beside"; 2× "of the session"; Physics "which is the point", "looks like luck"; Math prior-art "the books move"; 2× "not a coincidence").
  All three steps recorded in the bundle's WORKING REGISTER as **W-092** (editorial; never reader-facing). W-092 follows W-091 (chat 52); chats 53–62 are recorded in the Drive certificates (B7/B8/B9/B10/NUCLEON-E9/STRINGPF), not in the bundle.

## TASK 1 — STILL OWED (open the review pass here in chat 64)
1. **Accuracy read of every entry** (Math 334 entries; Spectra; IoI; Physics) — verified-before-written: each stated figure re-measured on the rebuilt tower where it can be; discrepancies are OPEN DEFECTS to close, not carry (finding is first about the reconstruction).
2. **Emphasis capitals in prose**: 431 occurrences of 298 all-caps words across the four compendia; most are journal acronyms/defined labels (JPCRD, CODATA, HSMI, UNWITNESSED, WITHDRAWN…); the emphasis ones (METRIC/ORDINAL, WHOLE, MOVE, LEAST, COUNT, OBJECT, BOTH…) need one read each — slip per family, not per word.
3. Math §I (line ~13559) "**Knowing which is the point of…**" — line-spanning sentence, not drafted.
4. The screen's instrument pattern is in this handoff's W-092 description; rebuild it from the list above (workshop/process · editorial aside · scene-painting · shouted emphasis) — do not treat "picture" (Thomas–Fermi picture, citations), "sealed" (the book's term), or "the session" inside register-derived measurements as offences.

## REST OF THE TASK LINE (M's order, unchanged)
2. RENUMBER each compendium (stable §-numbers for [MC-NN]/[PC-NN]/[IoI-NN]/[SC-NN] resolution).
3. COMPILE BIBLIOGRAPHY (includes converting the Math bibliography's citing-objects column — 410 handle tokens — to titles).
4. ABSORB OWED-REGISTER-EXPANSIONS (Drive id 1EEUiDyayJnLLOiij7o3CIleqfXo_1E6X; R-01–05, correction batches, the nucleon E=9 entry citing R-1550) into the Register, append-only, guard.py before any bundle is current.
5. RETURN TO MAIN-VOLUME PROSE WORK.

## STILL-OPEN LEDGER (measured this chat unless marked; close at the proper pass)
- register_cites.py (banked in the bundle) on the split per-volume files: **584 / 391 / 856 / 1050** vs printed **571 / 387 / 701 / 970** (2026-08-26 press); load-bearing ranking moved (1649 now 10×, 1526 8×) → recompute at Phase 4 press, not by hand.
- kinds.py printed measurement 498 vs measured 499 BEFORE 1787 (stale-by-one); now written 499, correction 144, 1,560 headings.
- **31 register numbers cited without an entry heading** (incl. 1710); the three-body block 1713–1724 is NOT in the Register → Register pass (task 4).
- Nucleon E=9 → new append-only Register entry citing R-1550 (task 4).
- Token resolution [XX-NN]→§ and the final tower-block reorder: LAST (MC-40/41 exempt).
- B6 deferred Register items (fill-limit undecidability; Last-Stage theorem; Door/Closure separation).
- R-04 Freuder-for-Dechter: working-register only.
- Press copies in Prints & Proofs (2026-08-26) predate BUILD53+ and carry the old §31.2.2 and old compendium form until re-pressed (Phase 4).
- Register front matter says "Build 9, 2026-08-26" and "the Build 16 column": press-time stamps, not restated this chat.

## STANDING DISCIPLINE (carried)
Executorial: execute, don't decide; a message with a question ends at the question mark; never announce a next action with a question; read before asking. Verified-before-written; measure from files; model-recalled numbers refused. No silent change: every edit by measured diff with discriminators + reverse-md5 check; editorial changes recorded in the bundle WORKING REGISTER (W-NNN) in the same build, subject-matter changes by an append-only book Register entry in the same build (1784's rule: an appended entry restates the extent everywhere it is stated). Entry-by-entry slips. Prose standard: plain statement + verified figures, then stop. Handles forbidden reader-facing. Never change an instrument to resolve a discrepancy. Zeno segmentation; ruling round at 75%; handoff at 90% or on a closed segment.

## UPLOAD / RETIRE (in Drive Materials before the chat-64 gate)
UPLOAD: The_Method_1_6_BUILD79_compendia_papers_audits.md · this HANDOFF-13.md.
KEEP: BUILD76 main; tower-2.py; convert.py; CONVERSION-CERTIFICATE-BUILD77.md; STRINGPF-CONVEXITY-RESOLVED.md; OWED-REGISTER-EXPANSIONS.md; OWED-EXPANSIONS-2.md.
RETIRE: BUILD75/77/78 compendia (superseded); BUILD56 main and STRINGPF-V-DISCREPANCY.md (already superseded); HANDOFF-11-1.md (stale); CHAT61-WORKING-RECORD.md.

## OPENING PROMPT FOR CHAT 64
"Run the §0 gate against BUILD76 main (1,977,372 B, md5 a4fbbc49d58ec6c6d6dd71a13f116765, 18,452 lines) and BUILD79 compendia (2,462,001 B, md5 d0201721d2793a9c000f5af18e89d6c8, 32,793 lines), rebuilding the tower to 976/1,654/2,535/13,585/70,905/199,130. Then continue TASK 1 of the compendium review pass where HANDOFF-13 leaves it: the accuracy read of every entry, family by family, each stated figure re-measured on the rebuilt tower where it can be, discrepancies raised as open defects; the emphasis-capitals read, one slip per family; and the one undrafted Math §I sentence. Proceed one measured-diff-guarded build at a time, recording each step as W-093 in the bundle's working register; put every subject-matter finding to me before any edit."