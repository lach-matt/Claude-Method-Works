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
