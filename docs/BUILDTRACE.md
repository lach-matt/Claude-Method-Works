# `tools/buildtrace.py` — provenance across the BUILD series

The archive holds the build series as snapshots — `The_Method_1_6_BUILD<N>_*.md`, **BUILD9 to
BUILD179 in two streams, 581 MiB across 135 canonical files**. They are the only record of *when* a
figure entered the books and *when* it changed. Answering that by hand means grepping a third of a
gigabyte, which `CLAUDE.md` forbids outright:

> Do not read or grep the tree wholesale: start from `MANIFEST.tsv`, then run targeted `ls`/`grep`
> against specific paths.

So this starts from `MANIFEST.tsv`, and every mode that touches the tree states its byte budget
first.

```sh
python3 tools/buildtrace.py --builds                     # from the manifest; reads no build file
python3 tools/buildtrace.py --first "146 of 163 = 92%" --stream compendia
python3 tools/buildtrace.py --trace "Theorem 7.1" --stream main
python3 tools/buildtrace.py --verify 90
python3 tools/buildtrace.py --selftest
```

Stdlib only, Python 3.9+.

## Three things it refuses to do

**1. It never scans the tree wholesale without saying what that costs.** Every tree-touching mode
prints its budget, and `--trace` refuses over `--budget` (default 256 MiB) rather than quietly
reading 448:

```
budget: 107 files, 448.1 MiB

REFUSED: 448.1 MiB exceeds the 256.0 MiB budget.
  --first bisects the same question in about 8 reads.
  --stream main is 22.7 MiB; raise the ceiling with --budget.
```

`DOCKET.md` §2: *state a budget rather than a negative when a computation is too large.*

**2. It never reports a first appearance from a bisect without checking monotonicity.** A bisect is
valid only if a token, once introduced, stays. So both endpoints are measured before the search
starts, and there are three ways for it not to be a first appearance:

| result | meaning |
| --- | --- |
| `FIRST APPEARANCE BUILD<N>` | absent at the old end, present at the new, and the build before N is absent |
| present in the oldest build | its introduction predates the archive, which cannot date it |
| `WITHDRAWN, so NON-MONOTONE` | present at the old end and absent at the new; a bisect would return a meaningless number |
| `ABSENT from both endpoints` | **not** absence from the series — a token added and later withdrawn is absent at both ends, and only `--trace` settles it |

**3. It never merges a build's variant copies.** A `.REPAIRED`, a `-1` and a `__<driveFileId>` copy
are all deliberate — `CLAUDE.md`: *"Both are intentional — do not merge or delete either"* — so the
canonical plain name is traced and the variants are listed, never silently averaged in. The series
also has copies of BUILD150–157 in `LOWDIN-DELIVERY-1` and `THREEBODY-DELIVERY-1`; tracing across
both would interleave two histories, so the trace runs in the folder holding the series proper and
`--builds` shows the others.

## `--builds`, which reads nothing

```
compendia stream (compendia_papers_audits): 123 files, 558.8 MiB, BUILD9 to BUILD179
    The Method Materials                           107: 9, 10, 54, 55, …, 178, 179
    The Method Materials/LOWDIN-DELIVERY-1           8: 150, …, 157
    The Method Materials/THREEBODY-DELIVERY-1        8: 150, …, 157
    4 variant copies not traced: BUILD53.REPAIRED, BUILD79__16qZ…, BUILD95-1, BUILD174__1rS8…

main stream (main_and_register): 12 files, 22.7 MiB, BUILD9 to BUILD90
    The Method Materials                            12: 9, 10, 54, 55, 56, 76, 82, 84, 86, 87, 88, 90
    1 variant copy not traced: BUILD53.REPAIRED
```

**The series has gaps and they matter.** The compendia stream jumps 10 → 54 and 155 → 157; the main
stream holds twelve builds between 9 and 90. So a first appearance is *the first build present in
the archive that carries the token*, never *the build that introduced it*, and the tool says so in
those words every time.

The two streams end where they should: main at **BUILD90**, which is the live main bundle, unchanged
since chat 62; compendia at **BUILD179**, with BUILD180 built in the repository after the chat-151
store move and so never mirrored to Drive.

## What it is for

**Dating a finding.** `tools/arith.py` reports MC L2930's `146 of 163 = 92%`, which is 89.57%. Is it
a recent regression?

```
$ python3 tools/buildtrace.py --first "146 of 163 = 92%" --stream compendia
series: compendia BUILD9 to BUILD179, 107 builds
bisect reads about 8 of them

present in the OLDEST build in the series (BUILD9), 1 occurrence
  Its introduction predates the series; the archive cannot date it.
read: 2 files, 6.1 MiB
```

The claim and its wrong percentage are in the oldest archived build, verbatim. Two reads, 6.1 MiB,
0.05 s — against 448 MiB for the same answer by grep.

**Dating a withdrawal.** `DEFECT-CENSUS.tsv` row 2 records *"Theorem 7.1 is absent — withdrawn"* and
does not say when:

```
$ python3 tools/buildtrace.py --trace "Theorem 7.1" --stream main
  BUILD9     2      first appears
  BUILD54    1      changes
```

Two occurrences through BUILD10 — the statement and a citation — and one from BUILD54 on. **The
withdrawal happened at BUILD54**, and the surviving occurrence is the citation the census flags.
That is asserted in the self-test on two targeted reads.

**Counting, not just presence.** `--trace` prints only the builds where the count *changes*, so a
figure restated 43 times, then 40, then 41 shows as three lines rather than twelve.

## `--verify`

The mirror's own guarantee re-asserted from the other side: the on-disk file against the md5 the
manifest records for it. `--verify` with no argument checks the whole series, which states its
budget first.

## The cache

A build is a snapshot and never changes, so a count once measured is permanent. Counts are cached in
`.buildtrace-cache.json` keyed by the file's **manifest md5** and the token — so a re-mirrored file
with a new md5 is re-counted rather than trusted. `--no-cache` skips it; `--trace`'s budget counts
only the files it still has to read.

## `--selftest`

29 fixtures, and only two of them read a build file. The rest are the manifest, the parser and the
pure parts:

| fixture | what it asserts |
| --- | --- |
| series shape | both streams present, compendia starting at BUILD9, strictly increasing in build number |
| bijection | every canonical build row in the manifest has a file on disk (`CLAUDE.md`'s manifest/tree bijection) |
| variants | `.REPAIRED`, `-1` and `__<driveFileId>` all parse, and `select()` never leaks one into the canonical series |
| `count_in` at nine chunk sizes | a token straddling a chunk boundary is still counted — without the carried tail a 448 MiB scan silently loses roughly one occurrence per boundary |
| `transitions()` | five count sequences, including absent-throughout (which must yield **nothing**, not a withdrawal that never happened) and a token withdrawn and reintroduced |
| **store against archive** | the live main bundle is BUILD91 (md5 `7d056e31…`, R3 class CINF, 2026-09-24), which the archive does not mirror; the superseded BUILD90 kept beside it in `method/` is byte-identical to the archive's mirror — md5 `49065309…`, 1,983,081 B — and BUILD91 reverses to it under `tools/r3_cinf.py`'s guard, so the store of record and the original-input witness of Ruling 56 still agree |
| the dated withdrawal | `Theorem 7.1` twice in BUILD10 and once in BUILD54 |

Current state: `SELFTEST OK`.

## Known gaps

- **A gap in the series is not dated.** The archive holds 107 of the 171 build numbers between 9 and
  179 in the compendia stream. A first appearance names the first *archived* build carrying a token;
  the build that actually introduced it may be one of the missing ones.
- **Fixed strings only, no regex.** The count is a byte-level `bytes.count`, which is what makes a
  448 MiB scan cheap. A regex would need a different scanner and a different budget.
- **A count is not a claim.** `--trace` says a token's frequency changed at BUILD54; it does not say
  which occurrence went or what replaced it. Diffing the two builds at that point is the next step
  and this tool does not do it.
- **The two 388 MB `conversations.json` exports are not in scope.** They are in `drive/PENDING.tsv`,
  not in the tree, and are not build snapshots.
- **`CLAUDE.md`'s own counts of the series were stale** and are corrected in the same commit as this
  file: it recorded *BUILD9 to BUILD174* with *91* compendia files, against a measured BUILD9 to
  BUILD179 and 123 (107 in the folder holding the series proper). `--builds` is now the way to ask.
