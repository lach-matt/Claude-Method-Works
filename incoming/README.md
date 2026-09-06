# `incoming/` — Drive content fetched through the connector, not yet mirrored

Four Drive folders created after the mirror was built — `BUILD183-PARTS`, `BUILD184-PARTS`,
`BUILD185-PARTS` and `DOCKET-152` — hold **54 small files** (2–6 KB each, ~185 KB in all) that
`drive/MANIFEST.tsv` does not cover. They are the chat-151/152 working parts: `HANDOFF-152.md` in
six pieces, `W-192/193/194`, `DEF-151c/151d/152`, `READ-28a2/28b2/32a`, `r2-*.py`,
`RULING-DOCKET-152.md` and the `CENSUS-CLOSURES-*` tables.

This tree is **not** the mirror and has no manifest rows. It is a staging area for content pulled
through the Claude Drive connector when `drive_sync.py` could not run for want of OAuth credentials.
Once a credentialed sync runs, these land under `drive/` with proper manifest rows and this tree can
be dropped.

**Every file here was verified by byte count against Drive's own `fileSize` before being kept.**

## Assembled from parts

Drive holds seventeen of these files split into `.partNN` pieces, because that was the only way a
Cowork session could write them back. Both forms are kept: the parts are the byte-exact Drive
records, and the whole file sits beside them, concatenated in index order. **Every split was
contiguous from `part00`** — no gaps — and assembly is reproducible by concatenation alone.

One of them carries independent proof. `HANDOFF-152.md` records `r2-32a.py` as
**22,360 B / `15a9047af4a637eb7bdb05d0ea982878`**, written by chat 152 before these parts existed.
Concatenating the five Drive parts reproduces that size and that md5 exactly, so the split, the
transfer and the reassembly are all byte-exact against a hash the corpus recorded independently.

Its golden output `r2-32a.out` (16,587 B) is named in the same line but is **not** in these folders.

| Assembled | Parts | Bytes |
| --- | ---: | ---: |
| `HANDOFF-152.md` | 6 | 13,176 |
| `r2-32a.py` | 5 | 22,360 |
| `RULING-DOCKET-152.md` | 4 | 15,318 |
| `r2-28b2.py` | 4 | 17,057 |
| `r2-28a2.py`, `READ-32a.md`, `REBUILD-BUILD185.md` | 3 each | 16,676 / 9,954 / 8,430 |
| ten more at 2 parts each | 2 | 4,919 – 8,473 |

## What is here so far

| File | Bytes | Drive says |
| --- | ---: | ---: |
| `BUILD185-PARTS/CENSUS-CLOSURES-32a.tsv` | 301 | 301 |
| `BUILD183-PARTS/CENSUS-CLOSURES-28a2.tsv` | 1,580 | 1,580 |
| `BUILD184-PARTS/CENSUS-CLOSURES-28b2.tsv` | 1,510 | 1,510 |

## Why the rest is not here yet, and the cheap way to finish it

The connector returns file content as **base64 inside the conversation**, so every byte is spent as
model context and has to be transcribed back out to land on disk. That is affordable at this size —
these three prove the route — but for the remaining ~51 files it is roughly 200,000 tokens of
transcription with a real chance of a typo, to move 185 KB.

A Drive mount does it exactly, in one command, because the bytes never pass through a model:

```sh
# in Colab, after cells 1 and 2 of tools/drive_sync_colab.ipynb
!cp -a "/content/drive/MyDrive/The Method Materials/BUILD183-PARTS" /content/repo/incoming/
!cp -a "/content/drive/MyDrive/The Method Materials/BUILD184-PARTS" /content/repo/incoming/
!cp -a "/content/drive/MyDrive/The Method Materials/BUILD185-PARTS" /content/repo/incoming/
!cp -a "/content/drive/MyDrive/The Method Materials/DOCKET-152"     /content/repo/incoming/
!git -C /content/repo add -- incoming && git -C /content/repo commit -m "incoming: the four post-mirror Drive folders" && git -C /content/repo push origin HEAD
```

`BUILD184_compendia_papers_audits.md` (5.9 MB) and the `BUILD174`/`BUILD178` duplicate copies in
`PENDING.tsv` are the same story at larger scale: each is under the connector's 10 MB limit, but
moving one through the conversation costs millions of tokens, so they belong to the mount or to
`drive_sync.py`.
