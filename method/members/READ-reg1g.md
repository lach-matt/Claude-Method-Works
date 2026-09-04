# READ-reg1g — R3: the Register front matter's citation figures and load-bearing table, re-taken (reg1-G / H / I). BUILD102 → BUILD103 main.

**What was owed.** READ-reg104 (ii) named the class and left it: the front matter's citation paragraph (571 entries
cited by other entries, recomputed 2026-08-26), its table of the entries cited seven times or more, and the sentence
*387 entries are cited in the main volume's chapters and appendices; 701 counting the four compendia and the two
papers; 970 counting citations by other entries*. Their writer is `register_cites.py`, a seated member that prints
and never writes, and `r2-reg1a2` scored them as deviations reg1-G / reg1-H / reg1-I.

**What was measured, and how.** `r3-reg1g.py` runs the seated tool unmodified (runpy, `run_name='__main__'`) in a
staging directory that holds the Register as it will stand with entry 1816 appended, beside the other volumes, and
takes the tool's own counters — not the `top 12` line it prints. With the recording entry counted:

| figure | printed (2026-08-26) | measured (2026-09-04) |
|---|---:|---:|
| entries cited by other entries | 571 | 651 |
| cited in the main volume | 387 | 407 |
| counting the four compendia and the two papers | 701 | 879 |
| counting citations by other entries | 970 | 1,077 |
| entries cited seven times or more | 11 | 13 |

The thirteen: 1460 (21×), 1445 (14×), 1475 (10×), 1649 (10×), 784, 1578, 1581, 1664 (9×), 1020, 1448, 1526 (8×),
1462, 1595 (7×). Every one of the printed eleven is cited at least as often as before; 1448 and 1526 are reached for
the first time. Their rows carry their entries' own headlines in sentence case, asserted against the headline with
case and punctuation aside — the same relation the eleven printed rows bear to theirs, which is checked and not
rewritten. Rows are ordered by count, then entry number.

**Two conventions of the tool the printed sentence did not state**, now stated at entry 1816: the superseded stretch
95–164 is not counted as a citer (its seventy stubs each say *see register 313*, which would otherwise make 313 the
most-cited entry at 71×), and a range — *registers 1701–1712* — counts each entry it spans.

**Entry 1815's class moved with the entry, as it will with every entry**: the front matter's total (1,658, 1 to 1816),
the mature record (165 to 1816, 1,494), the back matter, the kinds table (correction 169; 1,588 headings classified),
and the main volume's two *at this build* sentences — re-taken in the same build by the same instrument;
`register_counts.py` exits 0 on BUILD103.

**One press anchor moves with the date.** `build.py` L214 strips *by `register_cites.py`* from the recount sentence
for the print edition and anchors on the old date with it; the instrument asserts that this is the only anchor of the
press's 232 that moves, and records it (entry 1816; docket 38's class — the press's anchor list is the press's).

**The instrument's own floor, found and named.** `r2-reg1a2` read the ≥7 set from the tool's printed `top 12`, which
clips at twelve: on BUILD102 it scored 1595 as *None* and "the 11" as 12, where the tool's counter holds 1595 at 7
and thirteen at seven or more. `r2-reg1a3` takes the counter itself; reads the citation sentence's figures in the
front matter's own thousands convention; and bounds the front matter by its own scan (`### 1` is the first numeric
heading) rather than the literal 75, which the two added rows moved to 77 — the positional class of W-207. On the
BUILD102 tree its output differs from `r2-reg1a2.out` in exactly those lines (the tag, 1595 at 7, thirteen, one
fewer deviation), stated in its header. On BUILD103 it exits 0 with one deviation left, reg1-E — *the ten grouped
headings* against seven measured — which is r2-reg1a's finding and not this class's.

**Not touched.** The fifteen word-form sites and everything READ-reg104 left to M. Nothing outside the class moved:
main +0 lines, Register +2 (table) +4 (entry).
