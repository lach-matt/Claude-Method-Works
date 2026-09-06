# THE METHOD 1.6 — HANDOFF (chat 13 → chat 14), 2026-08-25
Chat: 13. Build described: BUILD-14. Register range: 165–1768.
Those three agree with the files. (HANDOFF-14 did not; that is why this line exists.)

## 0. THE READING GATE — EXECUTE BEFORE ANY OTHER WORK. NO EXCEPTIONS.
The fatal fault of every session since chat 11 is one thing: work begun before the record
was read. R1685 and R1697 registered it twice as a practice clause; a clause with no gate
behind it does not hold. It is a gate now. Segment 0 of every session is:

  G1  recent_chats n=20, then again with before= to reach the earliest. There are TWELVE
      chats: Rebuild 1 … Rebuild 12, plus this one. Read every summary.
  G2  Split both BUILD bundles. Bundle 1 = main + Register (2 members).
      Bundle 2 = 65 members. If a bundle looks absent, RE-LIST — /mnt/project syncs late.
  G3  Read WORKING-REGISTER.md in full. It carries THREE rulings and all 119 excised entries.
  G4  Print the certificate below. Until it prints, state NOTHING about the work and
      change NO file.

      CERT: chats read = N/12 · bundle members = 2 + 65 · rulings in force = 1–28 + amendment
            · Register headings = ____ · Register numbers = ____ · instruments present = ____

  Failure mode, stated so the gate can fail: if any count is recited from a directive or a
  prompt rather than READ from a file, the gate has not passed.

## 1. INSTRUMENTS — WHAT EXISTS AND WHAT DOES NOT
IN BUNDLE 2 (65 members): build.py · split.py · appf.py · kinds.py · register_cites.py ·
index_gen.py · index_pages.py · bookindex.py · dclose.py · rclose.py · excise.py · qgraph.py ·
tb_audit.py · run489.py · ruled_bracket.py · spectra_count.py · channels_LIMB.py · heii.py ·
crop_titles.py · fig_rerender.py · trueres.py — plus the six volumes, both papers, the audits,
HANDOFF-2/4/5/6/7/8/9/10/11/14, EXCISE-LIST.md, MANIFEST.md, the TSV captures and JSON results.

**guard.py DOES NOT EXIST.** M's ruling, chat 13, verbatim: "It was built after chat 11 the
first time and was thus deleted because every chat after 11 had a fatal flaw. That is why we
started over again from 11." The standing directive clause "guard.py OLD_DIR NEW_DIR runs
before any bundle is declared current" NAMES AN INSTRUMENT THAT WAS NEVER SHIPPED. Do not ask
for it. Do not reconstruct it without a ruling. The no-silent-change rule stands on its own;
what it lacks is a gate, and that is M's call, not an assumption to be made.
Likewise never shipped and never to be asked for: press_all.py, bundle.py, mkref.py, figs.py,
pageproof.py, ratios.py, regsize.py, RESTORE-PACKS.md. A directive naming a tool is not
evidence the tool exists.

## 2. RULINGS 27, 28 AND THE AMENDMENT — VERBATIM, FROM WORKING-REGISTER.md
R27 TWO REGISTERS: "There is the register compendium (and its citations in the other book)
which is only for entries regarding the subject matter of the books, nothing more. It is a
show of thought process and proof of work for the subject matter of the books only. All
reader-perspective audits (including the book's 23 - 25) and all editorial entries are
strictly for your working register and are forbidden from entry into the books as they are
irrelevant to any reader."

R27 AMENDMENT: "or the truth of a number the books state - these too must be removed. They
too are irrelevant." Operative: verifying the books' OWN PRINTED NUMBERS is EDITORIAL and
excised. Verifying a physical or mathematical result AGAINST THE WORLD is SUBJECT MATTER and
kept.

R28 PAPERS ABSORBED: "The lowdin and TB papers are not being rebuilt, they are being absorbed
into the books as is specified in the project details." Löwdin = Ch 35 (1701–1712), three-body
= Ch 36 (1713–1724). The deliverable set is SIX volumes, not eight.

Rulings 1–26 are carried in HANDOFF-2/4/5/7/9/11 inside bundle 2. Read them there.

## 3. STATE AS MEASURED THIS CHAT
Register: 1,447 HEADINGS · 1,472 distinct entry NUMBERS · 165–1768 · 7 grouped headings
carrying 32 numbers. Both figures are true of different objects.
**This is a HELD item, not a new finding.** R1478 recorded it (1,270 headings / 1,300 numbers);
R1564 put it to M as PR1 and M HELD IT for book time, on the ground that no computation
consumes it. DO NOT REOPEN. Report it if it moves; do not re-ask.
F.4.2 currently reads 1,447 · 369 · 3.92 : 1 · p 0.203 · 0.728 bits — i.e. on the heading count.

## 4. CLOSED THIS CHAT — W-001 (main volume; editorial, so WORKING-REGISTER not the Register)
Chapter 3's residue of the three removed register-audits. Chat 12 removed rows 23 GRAPH /
24 CYCLE / 25 NOMENCLATURE and moved eight count phrases; FIVE sites survived:
  §3.0 heading "Ten of the twenty-five … three test the register" → "Ten of the twenty-two
       test the index; twelve test the book"  (10 + 12 = 22)
  1029 "All twenty-five run on every build" → twenty-two
  1033–1043 the "And three test the REGISTER…" paragraph REMOVED. Chat 12's removal had left
       an ORPHAN PREDICATE — " are ordered by the cost of the failure each one catches." with
       no subject. Both closed by: " **The twenty-two are ordered by the cost of the failure
       each one catches.**"
  1149 "Twenty-five audits over twenty-five distinct cells" → twenty-two (sound without
       recomputation: a subset of distinct cells is still distinct)
  1316 "**The twenty-five.**" → "**The twenty-two.**"
Verified after: GRAPH/CYCLE/NOMENCLATURE occur 0 times in main; no audit-count "twenty-five"
remains. Unrelated "twenty-five" (cells, chapters, seeds, fibres) untouched at 1574, 2043,
5682, 8822, 8823, 8920. Backup: /tmp/main.bak (container-local; gone at reset).
THE MAIN VOLUME IN BUILD-14 BUNDLE 1 CARRIES THIS EDIT. BUILD-13's does not.

## 5. TASK 2 — MEASURED, NOT STARTED. 28 entries, 66 sites.
Method (repeatable, do not re-derive): parse entry numbers with
  re.finditer(r"^### ([\d,\s]+?)\s*$", txt, re.M)  — GROUPED HEADINGS MUST BE EXPANDED.
A naive ^### (\d+) parse produced a phantom class of 16 entries / 29 sites. With grouping
expanded that class is ZERO: every pre-existing citation resolves. Diff BUILD-12 vs BUILD-13
Register to isolate chat 12's excision (119 numbers).

Rule already given by chat 12: "Under Ruling 27 the citations go with the entries."

  199 x1 MAIN · 202 x1 MAIN · 210 x2 MAIN · 269 x2 MAIN · 287 x5 MAIN+Reg · 324 x1 Reg
  341 x3 Reg · 344 x3 MAIN · 358 x1 MAIN · 363 x1 MAIN · 366 x1 MAIN · 560 x2 Reg
  571 x3 MAIN+Reg · 1000 x1 Reg · 1013 x1 Reg · 1223 x1 Reg · 1443 x12 Reg · 1537 x2 Reg
  1571 x4 Math+Phys+Reg · 1572 x1 Reg · 1594 x2 Reg · 1710 x2 Math · 1725 x3 MAIN+Reg
  1731 x1 MAIN · 1732 x1 Reg · 1735 x1 MAIN · 1756 x7 MAIN+Spectra+Reg · 1766 x1 Spectra
Heaviest: 1443's twelve sites are all one Register load-bearing table row (| **1443** | 13× |).
Full site list with line numbers: EXCISE-LIST.json in bundle 2 of BUILD-14.

## 6. OPEN, IN ORDER, FOR CHAT 14
1. Task 2 — the 66 sites. Start with 1443's twelve (one class, one table).
2. Task 3 — press all six volumes; sample the PRESSED OBJECT at every change, INCLUDING
   inside the Spectra Part II continuation blocks (the R1764 fault). Figures for the press:
   The_Method_1_6_figures_BUILD13.zip, Drive id 1q7pvnxMPILD9AVoH6XjymZHXX79YzITd, 6.3 MB,
   under the 10 MB connector cap. Decode: json.loads(d[0]['text'])['content'] → b64decode.
3. Phase 2 reader audits, one volume per segment, against the compendium gold standard.

## 7. DO NOT START WITHOUT M's RULING
- The 126 unreconciled Spectra rows.
- The five narrow-bracket FAIL rows named in R1763.
- Any reconstruction of a deleted instrument.
- The 1,447 / 1,472 count question (HELD by M at PR1).