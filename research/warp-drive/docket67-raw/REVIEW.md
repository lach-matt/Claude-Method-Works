# DOCKET 67 — the review package for M

**Status: verified, NOT seated, nothing repaired.** Everything below waits on M's review. Sources: `VERIFIED-GRADES.tsv`
(one row per result), `adjudications/` (30), `REAUDIT-GRADES.tsv` (22), `REOPEN.json`, `REOPEN-VERIFY.json`,
`REOPEN-ADJUDICATE.json`, `TREE-CORRECTIONS.tsv`, and the shard audits in `shards/`.

## 1. The grades — 431 external results, every one verified

| grade | count |
|---|---|
| NARROWED | 280 |
| STANDS | 140 |
| DATA-DEPENDENT | 7 |
| WRONG | 4 |
| OPEN or unresolved | 0 |

How each was settled: 380 by the shard rule (audit at source, three adversarial verifiers; the audit's grade stands
unless two or more refute), 30 by an independent adjudicator (verifiers split, a unanimous overturn, an OPEN that
rested only on the alphaXiv outage, or the GMMPS WRONG), 21 by a re-audit on a source M retrieved. Read statuses
follow M-D67-1 and M-D67-2: where M has not confirmed a pair, a finding is stated against the arXiv version read.

**NARROWED almost always records the TREE's drift, not a fault in the source:** the tree uses the result on a wider
class than the source supports, or drops a hypothesis the source states.

## 2. WRONG — 4, against two papers

| result | what is wrong | the tree |
|---|---|---|
| Kuo & Ford, gr-qc/9304008 v1, qualitative conclusion | "fluctuations of order unity wherever rho < 0" fails: a displaced squeezed state at theta = pi/2, \|alpha\|^2 = (1 - e^{-2r})/8, has rho < 0 with Delta = 0 exactly | carries it (`fluctuation.py`, KF_QUALITATIVE_CONCLUSION_SURVIVES = False) |
| Kuo & Ford, eqs. (3.7)-(3.8) | (3.8) gives Delta = -0.3452, but Delta is defined as an absolute value; (3.7) is off by 1/(1+eps^2) | carries it |
| Kuo & Ford, the claim after (3.8) | refuted by the same computation | carries it |
| GMMPS, arXiv 2604.01047, Thm 3.6, S half only | the paper's own covariant procedure (used for the TT half, p. 39) gives alpha~^S_1 = 0; the printed 1/(64 pi^2) comes from holding mu fixed to the background -- an inconsistency inside the paper, not an algebra slip. The TT half and Prop. 3.1 STAND | **not yet carried**: `linstab.py:181-183` uses the constant to set b_0 and says "not adjudicated here" -- for M to rule |

Kuo & Ford's journal version carries these under M's comparison (COMPARED-BY-M, M-D67-1).

## 3. DATA-DEPENDENT — 7

`0705.3704` (Flambaum, variation of constants), `0909.0948` (Asplund et al., solar composition), `1711.00578`,
`icrp-23-reference-man`, `icrp-reference-adult-and-ci-chondrite`, `lodders-2003-apj-591-1220`,
`lodders-2003-ci-chondrite`. The conclusion moves with a datum that has moved or is contested. ICRP 23 Table 108
(pp. 289-324, as an image PDF) and the ICRP 89 reference-male composition would move some of them; without them
the grades stand as they are.

## 4. What the grades reopen on the board — computed, verified, adjudicated

287 of the 291 grades below STANDS move no verdict (the use that carries each verdict sits inside what holds). Four
do:

| finding | what reopens | what stays | direction |
|---|---|---|---|
| D29 (1809.06923) | D29's THEOREM grade, decay conjunct only, rests on an unnamed bridge H-BRIDGE ("a region whose particle masses differ and which destroys what it meets forms no atomic mass of ours"). Wider: S12's "priced, not refused" rests on the same bridge -- on its failure the board's own link flips S12 to refused | S10 REFUSED on all six readings; D29's sum-of-squares part; every specthm class verdict | neither, net |
| S-2 (sturm-comparison-theorem) | class S-2 ("Sturm-universal seating over a uniform ball") EMPTY -> OPEN for balls with T_kk > u along the chord: a perfect fluid on a diameter with w >= pi^2/6 - 1 = 0.6449, or a magnetised ball probed across B; fact SR2 refused, requirement SR2 THEOREM -> OPEN | radius chords (would need w > 5.58, violating DEC); pressureless matter; S-1 | removes a refusal; builds no witness |
| S4 (2309.10848-eft-breakdown) | the xi < 0 sub-class of S4 in ONE window only: 1 <= 8 pi G\|xi\| phi_max^2 < 1.300608 (l_UV >= 2.091911 l_P). The only ground against it there is an order-of-magnitude argument nobody computed. Sign convention: FFKP eq. (109), shared by Fewster-Osterbrink and Barcelo-Visser (xi < 0 is the Higgs-inflation sign) | S4 at xi > 0; xi < 0 with eps < 1; S8 (not widened); O1; every class | toward M, narrowly |
| W2 (ford-roman-qi-and-fewster-casimir-fraction) | one reading of W2's premise: whether the Casimir density saturates the unknown SHARP bound at the midplane (bracket 6.70%-100%) is OPEN, not refuted | W2 stays WITHDRAWN on four counts, as adjudicated: Fewster's own Eq. (4) bound (3.20%-6.70%); across the slab, with the off-midplane ceiling; 'not an exception' against the uncapped Eq. (1); 'known saturated'. (The EM case against an EM bound was never computed: OPEN, not a carried count -- corrected from this file's first version.) W1 | against M, narrowly |

## 5. Corrections to the tree's prose — `TREE-CORRECTIONS.tsv`

1,162 sites across 290 results where only wording needs correcting and no verdict moves: a dropped hypothesis, an
overstated scope, a stale number or line, a misattribution. Most-touched files: ledger.py (103), address.py (77),
specthm.py (69), massform.py (65), permute.py (46), tolman.py (45), candidates.py (44), branelink.py (42),
bounds.py (41), achievable.py (41).

## 6. What M is asked to rule

1. **Accept the verified grades** as DOCKET 67's record.
2. **The four reopenings:** seat each as computed -- name H-BRIDGE on D29 and S12, move S-2 to OPEN in its
   sub-case, record the S4 window and the W2 reading as OPEN -- or rule otherwise.
3. **GMMPS:** `linstab.py:181-183` uses the constant DOCKET 67 grades WRONG.
4. **The prose corrections:** repair the tree's wording at the 1,162 sites (a multi-file pass, shown to M before
   it runs), or a subset.
5. Then, by M's earlier rulings: the per-source comments (`COMMENTS-PLAN.md`), and DOCKET 68.
