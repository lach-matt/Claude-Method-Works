# `tools/consolidate.py` — one location for everything the mirror had sealed

## What problem this solves

`drive/` is a byte-exact mirror, and byte-exactness is the reason things were hard to find. Thirty-one
of its files are archives and nine are Claude project exports; between them they hold **2,504 file
occurrences** that no `grep` over the tree can see, because they are inside `.zip`, `.tar.gz` and
JSON `content` fields. Instruments, transcripts, figures and data tables were all in that condition.

Unpacking them naively would have written 2,504 files, most of them copies of each other or of files
already tracked. This writes **779**.

## The contract

Read `drive/` (and `method/`, `tools/`, `docs/` as the "already have" index). Write only
`extracted/`. Never modify `drive/` — the 819-row `MANIFEST.tsv` ↔ 819-file bijection is
load-bearing, and `drive_sync.py --prune` deletes anything under `drive/` without a manifest row.

Every source occurrence gets exactly one row in `extracted/LEDGER.tsv` with one of four
dispositions:

| Disposition | Rows | Written? |
| --- | ---: | --- |
| `EXTRACTED` | 779 | yes, to `target_path` |
| `DUP-OF-EXTRACTED` | 1,198 | no — md5 already written; `target_path` names the one copy |
| `PRESENT-IN-REPO` | 523 | no — already tracked; `target_path` names the existing file |
| `SKIPPED-DERIVED` | 4 | no — `.pyc` bytecode, excluded by `.gitignore` |

Deduplication is md5 over the body, applied in that precedence order. **188,280,626 bytes** of
duplicate content resolved to a pointer rather than a file.

## Rules that are not obvious

**Canonical copy first.** Archives are visited sorted so that a plain name beats a
`__<driveFileId>` or `-1` variant. A body therefore lands under the archive a reader would name.
The consequence: `method16_rp_A_instruments.tar.gz`, `method16_rp_C_figures.tar.gz` and
`The_Method_1_6_figures_complete.zip` produce **no directory of their own** — every member was
already written from `restore-point-2_13.tar.gz`, which sorts first. This is not data loss; the
ledger resolves each member to its target. It is why the session transcripts from `rp_C` live at
`extracted/archives/restore-point-2-13/transcripts/`.

**A project doc named `.pdf` or `.docx` holds text, not that binary.** The export's `content` field
is a string; no binary survives it. Such docs are written with `.txt` appended and the substitution
recorded in the ledger's `note` column. The genuine PDFs are in `drive/`. Four docs are affected.

**Near-identical is not identical.** `INTEGRATION-transitions.md` and `RESPONSE-TO-METHOD-1_6.md`
differ from their `CORPUS` twins by one trailing newline. They are kept. A one-byte difference is a
finding to record, not a duplicate to collapse — the same rule the audit instruments follow.

## Running it

```sh
python3 tools/consolidate.py            # regenerate extracted/ and both TSVs
python3 tools/consolidate.py --verify   # re-hash every extracted file against the ledger
```

Stdlib only, and idempotent: deleting `extracted/` and rerunning reproduces the same 779 files and
the same ledger. `--verify` re-hashes each `EXTRACTED` row and resolves every pointer row, and
reports `0 bad, 0 dangling` on a clean tree.

## Size

`extracted/` adds **57,400,492 bytes** across 779 files. The largest is `COORDINATES.tsv` at
10.8 MB — under the 40 MiB trigger in [`REPO-SIZE.md`](REPO-SIZE.md), and 9× under GitHub's 100 MiB
block. Most of the volume is `.tsv` and `.json`, which delta-compress well.

## What it does not reach

The two 388 MB `conversations.json` chat exports are not in `drive/` at all — they are in
`drive/PENDING.tsv`, above GitHub's per-file limit and above the Drive connector's payload ceiling.
`extracted/` contains four transcripts recovered from a restore point; those are **not** a
substitute for that store. Sharding remains the route:
[`../tools/shard_conversations.py`](../tools/shard_conversations.py).
