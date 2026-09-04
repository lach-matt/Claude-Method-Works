# DEF-153O — DEF-152 executed: what M's four rulings became, and what they left. RECORDED.

## Executed (BUILD98 → BUILD100 main; BUILD202 → BUILD204 compendia)

| DEF-152 item | ruling | where |
|---|---|---|
| 1 (26c-02, c) | origins measured; entry cites 332, 373, 375 | entry 1807 |
| 8 (32a-04) | loss stated, not filled | entry 1808 |
| 4, 5 (28a-06 a; 28a-08) | fifty-two, the 172-row figure beside it; 16 not cited | entry 1809, References |
| 6 (28b-07 b) | lead-ins re-worded; Montgomery stands | entry 1810, §R.7 |
| 7 (28b-08) | twelve, not eight | entry 1811 |
| 2, 3 (27a-02 a; 27a-07; 27a-08) | rows 8.2 / 8.4 / 10.4c re-taken; the six placed at 10.4e; 1403 dropped | entry 1812, Appendix G |
| 9 (32a-03) | qualification route; six of seven sites | entry 1813, §2.21 + six sites |
| 10 (census 293, 387–672) | measured and closed | `r2-bib`, CENSUS-CLOSURES-d152.tsv |

## Decisions I took that M may reverse

1. **Row 10.4e gained three pointers** (1035, 1483, 1484). M ruled on rows 8.2, 8.4, 10.4c and left the six's home to R3; ruling that their home is 10.4e and writing it there is the ruling executed, but 10.4e was not one of the rows M named. Reversible by a new entry.
2. **The 172-row fifty-nine is kept beside the fifty-two** ("owed and not decided" in DEF-152 item 4). Taken on 1736's own precedent, *the prior count kept beside it*.
3. **The readouts carry the qualification rather than the scripts becoming members** (DEF-152 item 9's two routes). The restore-point's scripts are stale against the volumes.
4. **The register's span carries no qualification at its site** — its only site is the Register's front matter, under Ruling A.
5. **mc 387–672 closed as one class defect**, not 286 verdicts and not "not a defect". The column prints identifiers the volume never defines; that is the defect, and the census's 286 rows are one instance of it.

## Open, and named

- 1019 and 1020 against §10.4e: NEAR. Row 10.4d (`M.C2`): unread.
- 28a-09 (1736's *never listed*, Janet 1928/1929): unruled.
- 1721's ten owner-groups against seven closures: the audit-7 ledger is not a member.
- The handle vocabulary of the Mathematical Compendium: 137 handles resolve nowhere; the repair is the generator's.
- The register's span: qualified at entry 1813, not at its site, until reg1-04 is repaired with its class.

## The census, and two seated tools that cannot follow a build that moves a line

Measured while closing. `census.py` line 50 reads `if n>1792 or n not in regnums` — the Register's extent as a
literal — so a fresh census flags every citation of 1793–1813 as C5-REGISTER-POINTER-UNRESOLVED (16 new rows,
three of them citations inside the Register itself), which is DEF-151r3 item 5's class in a fourth instrument.
`close_census.py` keys id stability to (class, volume, line), so a build that moves a main-volume line moves every
id below it and the guard refuses (1,280 ids). Both are seated members; neither is edited. `gate.py census` was red
at BUILD98 on the first mechanism and stays red on both. The seated census stands at BUILD188's lines; every
CENSUS-CLOSURES file cites ids, not lines, so no closure is wrong. Also in the fresh census and not in the seated:
two C7 rows whose site counts grew, four C13 rows for `BUILD95`–`BUILD97` printed inside entries 1805 and 1806
(ruling 46's class, my own), five C9 words in §34.6's rewrite and entries 1804/1805, and two C8 named statements
(*witness rule*, *reading cannot bound*). Twelve seated rows have no fresh match — §34.6's old "always / never"
sentence, the C7 counts, `slack = kernel … always admitted` — because their text was repaired or moved.

**Owed, and neither is a re-bank:** a census successor that reads the extent as data, and a regeneration that
re-addresses an id by (class, volume, item, text) and retires — never deletes — a row whose site no longer exists.
The retired rows are the ones the closures cite as repaired; how they are marked is M's.
