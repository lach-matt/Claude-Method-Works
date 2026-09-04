# DEF-153Q — the chapter 12–15 readings are not lost: M archived them at W-169. CORRECTED the same day; nothing seated.

**Correction, written after M answered Q4.** The first version of this file (commit bf46405) read the live bundles only and
said the readings were "held nowhere". They are held: **W-169 (chat 129) executed M's archive split** (chat-127 item 5) —
`archive-split.py`, seated, reverse-guarded — moving exactly 393 members out of BUILD158 into
`The_Method_1_6_ARCHIVE1_legacy_handoffs_ch12-15.md`: 48 handoffs, 207 instruments and goldens, 69 readings, 69 census
closures. The mirror holds it at `drive/The Method Materials/`, **3,743,970 B · md5 5a5c0829fa234dde4f12ac240fc7dec4 ·
394 members**, exactly as W-169 records. Re-measured here: of the 59 / 48 / 43 names below, 57 / 48 / 42 are in ARCHIVE1
byte-exact, 103 of the 104 archived instruments with their golden; the three not there are the pattern names `READ-ch2`,
`READ-chNN`, `CENSUS-CLOSURES-chNN`, not files. **The consolidation branch's `recovered/` copies are drafts for 116 of
244**: identical to the archived member for 128, different for 116. Its coverage census does not look inside a bundle, so
its "held nowhere" is wrong for these and for the handoffs it seated by number (see the note at the end).

**Q4 is therefore not executed.** Seating `recovered/` copies into the live bundle would reverse M's own archive split and,
for 116 files, seat a draft over the seated version. The census accounting corrected: the live closures close 699 of the
census's 1,557 ids, ARCHIVE1's 144 more (10 overlap), 833 by either, 724 by neither. What remains open is only whether
`method/` should carry ARCHIVE1 beside the two live bundles under `verify.py` (it is in the mirror, not the store) — M's.

---

*The first version, kept as written:*


Measured 2026-09-04 at BUILD103 main / BUILD213 compendia against `claude/consolidate-project-artifacts-ov8es9` at
9196725, after M's note that more had been pushed.

## The gap

The Working Register's W-112 … W-121 (chats 75–83, 30 August 2026) record Phase R2's reading of main §12.11.0.8 through
Chapter 15 and name the readings, instruments and census closures those chats wrote. **None of them is a member of either
bundle**, and DEFERRED.md and DOCKET.md cite them as if seated (13a-01, 13b-01, 13j-01, 12q-04, 12q-05, 12s …).

| named in WORKING-REGISTER / DEFERRED / DOCKET / RULINGS-R2 | cited | seated | missing | recovered on the branch |
|---|---:|---:|---:|---|
| `READ-*.md` | 102 | 43 | **59** (ch12 16, ch13 16, ch14 13, ch15 12, `READ-ch2`, `READ-chNN`) | 56 — 55 `RECOVERED-BY-HEADING`, 1 `RECOVERED`; not: `READ-ch15k`, `READ-ch15n`, `READ-chNN` |
| `r2-*.py` instruments | 99 | 51 | **48** (ch12 26, ch13 12, ch14 8, ch15 2) | 48 of 48 (2 exact, 25 by heading, 21 by write); 73 more ch13–ch15 instruments by write that no governance file names |
| `CENSUS-CLOSURES-*.tsv` | 80 | 37 | **43** (ch12 13, ch13 11, ch14 11, ch15 7, `chNN`) | 21 by write (+8 uncited); **22 not recovered**, thirteen of them ch12l–ch12x |

The seated closure files cover **709 of the census's 1,557 ids**; the 29 recovered closure files close **92 ids that have no
seated closure**, every one of them a live census id. Spot-checked: `recovered/READ-ch13b.md` opens with the segment, the
instrument and the golden's md5 that W-116 records (7,892 B, chat 79).

How it happened, as far as the record says: W-108 … W-116 closed their work *to Drive*; the store was adopted from Drive at
chat 151; `drive/MANIFEST.tsv` and `extracted/LEDGER.tsv` hold none of these names. The files existed only in the chat
export until the branch's `recover.py` and its tool-call walk found them.

## What it means for R3

- Every DEFERRED and DOCKET item keyed to a chapter 12–15 reading (`12q-`, `12s-`, `13a-`, `13b-`, `13j-`, `14`, `15` …)
  rests on a document the store cannot show. R3 has executed some of them (13a-01's residue sites; 13j-01) from the
  DEFERRED summary alone.
- The gate's estate is short 48 cited instruments and their goldens; the census-closure accounting is short at least 92 ids.
- The readings' instruments are positional in the main volume at the lines of BUILD97–105 (`main §12.11.4 (L3457–3461)`),
  the class W-207 / W-214 repaired for chapters 16–28. Seating them means proving each on the bundle it was banked against
  (`tools/proveanchor.py`) or seating it without a golden, as `r3-wl2` is.

## The pass proposed, and not run

One seating pass, from the branch's `recovered/` tree, each file carried with its ledger row (md5, status, shard, chat):
1. the 56 recovered `READ-*.md` and the 29 recovered `CENSUS-CLOSURES-*.tsv` as members, their recovery status stated in
   the W entry and in a `RECOVERED-INDEX.tsv` member, never flattened to "seated at the chat's close";
2. the 48 cited instruments, each with a golden only where `proveanchor.py` proves it on the bundle W-112 … W-121 name,
   otherwise seated without one and listed as unproved;
3. the census-closure accounting re-taken after (1).
It spans many files and rests on bodies whose names were inferred from headings for 55 of 56 readings. **It waits for M**
(RUL-153-PENDING, Q4). Nothing under `recovered/` is a member until then.

**Closed 2026-09-04 (DEF-153R):** chat-127's ruling 5 answers the one question this file left — the archive is verified by
md5 on demand, not by the gate. `verify.py` is not changed.
