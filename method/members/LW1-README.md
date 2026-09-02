# LOWDIN-DELIVERY-1 — README (interim; supersedes on bank receipt)

Delivered by the Löwdin project, 2026-09-01, in answer to REQUEST — THE METHOD 1.6 BUILD
(chat 128; BUILD90 main, BUILD157 compendia). Files are as produced; the md5 decides.

## Status of the twelve objects

| object | status | where it is |
|---|---|---|
| 3  ground.py (1306) | DELIVERED | this folder; byte-exact from CODE-LOWDIN-2_13.txt (bank restore-point-2_13, sha256 80577094…); recorded sha256 3aa24998a0f1a6d6… reproduced |
| 1, 2, 4, 5, 6, 7, 8, 10 | PENDING BANK | LOWDIN-HANDOFF-103.tgz (sha256 05ea7bd5…, 1870 sealed files, root c6bcdd21) — the last sealed archive; awaiting upload to the Löwdin chat |
| 9 (1707–1711) | PENDING BANK (packs 93–103) + NOT HELD (S104 restatement w104.py) | see note on S104 |
| 11 six figures | NOT HELD as files unless M supplies S104 outputs | fig1–6.py and the PNGs were archived in pack104, never sealed (see note) |
| 12 THE-LOWDIN-SOLUTION.md | PENDING M's copy | the .md and .pdf were delivered to M on 2026-08-23; the .pdf is in Prints & Proofs (Drive id 1r5_KE69TLo7dqcU3jhS8qbdHFQfC7rz7, 879,791 B); project register/rulings are in the archive above |

**Note on Session 104.** S104 (chat LCP101, 48 turns) produced the paper, Chapter 35 (Body 2),
the compendium additions (Body 3) and the figures, all archived in pack104 — but S104 was never
sealed: LOWDIN-HANDOFF-104.tgz was offered and not built. pack104 existed only in that chat's
container. What survives of S104 is what present_files handed M. Any pack104 object M does not
hold is "not held"; the book labels it record-carried. This is a finding of the Löwdin project,
severity FOUNDATIONAL for object 11 and the S104 part of object 9.

## ground.py (object 3)

- Retrieval record as held: NIST ASD ver. 5.12, GSIE interface, retrieved 2026-08-09, citation
  and DOI in the docstring. No query string or URL is stored in the file or anywhere in the bank;
  the query itself is NOT HELD. The file's own fields are: ground shells as printed, ground level,
  Z = 1–108.
- Environment: Python 3.12.3, standard library only (re). No NumPy/SciPy.
- Command: `python3 ground.py`
- Expected output: `ground-run.log` (md5 6bc5a6196d6de9348b6618fb92d27fe4): 108 elements,
  electron count checks 108/108; opening sequence 1s 2s 2p 3s 3p 4s 3d 4p 5s 4d 5p 6s 5d 4f 6p 7s
  6d 5f 7p; 19 subshells opened across Z = 1 to 108 (matches Register 1306, 1307).
- Wall-clock: 0.03 s.
- Gate: the electron-count check is the file's own can-fail (any edited configuration with the
  wrong count prints `mismatched: [Z]` and the tally drops below 108/108).

## Form

Every file ≤ 10 MB. MANIFEST.tsv: name, bytes, md5, purpose. Drive may add a `-1` suffix; the
md5 decides.
