# Repository size audit

Measured **2026-09-02** on branch `claude/google-drive-github-sync-3833rb`
(`github.com/lach-matt/Claude-Method-Works`), at 8 commits.

Every number below was taken directly from the working tree with `find`, `du`,
`git count-objects -vH` and `git ls-tree`. The commands are shown so the audit
can be re-run.

---

## 1. What is actually here

| Measure | Value |
| --- | --- |
| Files under `drive/` | 415 |
| Tracked files at `HEAD` (incl. `README.md`) | 416 |
| **Unique blobs** at `HEAD` | **297** |
| Bytes under `drive/` (sum of file sizes) | 531,208,218 B — 506.6 MiB |
| Working tree on disk (`du`, excludes `.git`) | 508 MiB |
| `.git` on disk (`du`) | 84 MiB |
| Packed history (`size-pack`) | **83.37 MiB** (333 objects, 1 pack) |
| Total checkout on disk | 592 MiB |
| Largest single file | 14,238,681 B — **13.58 MiB** (`drive/The Method Materials/restore-point-2_13.tar.gz`) |
| Files > 5 MB | 26 |
| Files > 50 MB | **0** |
| Files > 100 MB | **0** |

```sh
find drive -type f | wc -l
find . -path ./.git -prune -o -type f -printf '%s\n' | awk '{t+=$1} END{print t}'
du -sh --exclude=.git . ; du -sh .git
git count-objects -vH
git ls-tree -r HEAD | awk '{print $3}' | sort -u | wc -l
```

### Composition of `drive/`

| Type | Files | Bytes | Share |
| --- | ---: | ---: | ---: |
| `.md` | 225 | 386,349,023 (368.4 MiB) | 72.7% |
| `.pdf` | 31 | 61,543,881 (58.7 MiB) | 11.6% |
| `.zip` | 15 | 36,676,183 (35.0 MiB) | 6.9% |
| `.gz` | 12 | 28,369,084 (27.1 MiB) | 5.3% |
| `.csv` | 1 | 10,912,381 (10.4 MiB) | 2.1% |
| `.json` | 1 | 4,523,682 (4.3 MiB) | 0.9% |
| `.tsv` | 51 | 1,973,982 (1.9 MiB) | 0.4% |
| `.png` | 7 | 545,932 | 0.1% |
| `.py` | 43 | 279,048 | 0.05% |
| `.txt` | 12 | 23,438 | — |
| `.log` | 17 | 11,584 | — |
| **Total** | **415** | **531,208,218** | 100% |

### Two facts that matter more than the headline number

**A. The clone is 83 MiB, not 508 MiB.** 470.0 MiB of unique content packs down
to 83.37 MiB — roughly 5.6:1. That is not luck: the bulk of `drive/` is 225
Markdown files that are successive builds of the same lineage
(`The_Method_1_6_BUILD*_compendia_papers_audits.md`), and git delta-compresses
each build against its neighbours. A single one of those files gzips to 31% of
its size on its own; the pack does far better by storing deltas. **Clone and
push cost is governed by the 83 MiB pack, not by the 508 MiB checkout.**

**B. 119 of the 416 tracked paths are byte-identical duplicates.** 416 paths
resolve to only 297 unique blobs — the `__<driveFileId>` copies and the files
that appear in both `LOWDIN-DELIVERY-1` and `THREEBODY-DELIVERY-1`. Those
duplicate paths cost about 38.4 MB (36.6 MiB) of *checkout* size but cost
essentially **nothing** in the pack, because identical content is already stored
once. Deleting duplicates is therefore a poor size lever — it shrinks the
working tree and buys almost no clone or push savings.

---

## 2. GitHub's published limits

| Limit | Value | Behaviour |
| --- | --- | --- |
| Per-file **warning** | 50 MiB | Push succeeds; GitHub emits a warning |
| Per-file **hard block** | 100 MiB | Push is **rejected**; the file must be removed from history |
| Max **push size** | 2 GB | A single push exceeding this is rejected; split into smaller pushes |
| Repository **soft limit** | ~5 GB | GitHub may contact the owner and ask them to reduce it |
| Repository **recommended** | < 1 GB | GitHub's stated recommendation for a healthy repo |

The 100 MiB per-file limit applies to the blob **as it exists in history**, not
just at `HEAD`. A large file that was committed and later deleted still blocks
pushes until it is removed from history.

---

## 3. Headroom

| Against | Now | Limit | Headroom |
| --- | --- | --- | --- |
| Largest file vs. 50 MiB warning | 13.58 MiB | 50 MiB | **3.7×** — 36 MiB spare |
| Largest file vs. 100 MiB block | 13.58 MiB | 100 MiB | **7.4×** — 86 MiB spare |
| Pack vs. 2 GB push limit | 83.37 MiB | 2 GB | **~24×** — using 4.1% |
| Pack vs. 1 GB recommendation | 83.37 MiB | 1 GB | using 8.1% |
| Pack vs. 5 GB soft limit | 83.37 MiB | ~5 GB | **~61×** — using 1.6% |

**This repo is comfortable.** Nothing is close to any GitHub limit, and no
action is required today. Git LFS would add operational cost (a filter every
collaborator must have installed, a separate quota, a history rewrite to adopt)
in exchange for no present benefit.

### Projected size once the 31 missing files land

31 Drive files (BUILD143–BUILD158, some duplicated across the two DELIVERY
subfolders) could not be pulled through the Google Drive connector, which has a
hard payload ceiling near 6 MiB. They are 6.07–7.26 MB each.

- **Per-file risk: none.** The largest is 7.26 MB, seven times under the 50 MiB
  warning line.
- **Working tree: +~190–225 MB**, taking the checkout to roughly 720–760 MB.
- **Pack: modest.** They are further builds of the same Markdown lineage that
  already delta-compresses 5.6:1, and several are byte-identical duplicates that
  will share a blob. Estimated pack after they land: **~110–150 MiB** — still
  under 3% of the 5 GB soft limit. (This is an estimate, not a measurement;
  re-run `git count-objects -vH` once they are committed.)

Even in that state, no limit is approached.

---

## 4. Trigger points — when to actually act

Re-check these with `git count-objects -vH` and
`find . -path ./.git -prune -o -type f -size +40M -print` after any large import.

| # | Trigger | Action |
| --- | --- | --- |
| 1 | **Any single file ≥ 40 MiB** | Do not commit it. Approaching the 50 MiB warning. Publish it as a GitHub release asset (2 GB per asset) or put that one path in LFS, and record it in `drive/MANIFEST.tsv` as external. |
| 2 | **Any single file ≥ 100 MiB** | Hard stop — GitHub rejects the push. Must be kept out of history entirely, not committed-then-deleted. |
| 3 | **Packed `.git` ≥ 1 GiB** (≈12× today) | Migrate `drive/` to Git LFS. This is the real trigger for LFS: clone times and CI checkout costs become the problem well before any GitHub limit does. |
| 4 | **Any single push ≥ 1.5 GiB** | Split the push into smaller batches now; migrate before the next bulk import. |
| 5 | **Repository ≥ 5 GB** | GitHub may intervene. Should never be reached if trigger 3 is respected. |

### Order of remedies, cheapest first

1. **Stop committing every intermediate BUILD snapshot.** 225 Markdown files
   holding successive builds of one document is the single largest driver of
   growth. Keeping only the latest build plus tagged milestones would cut future
   growth sharply, and costs nothing to adopt.
2. **Move the already-compressed archives to release assets.** `.zip`, `.tar.gz`
   and `.pdf` are 126.6 MB and do not delta-compress; they are the part of the
   repo that git handles worst. Attaching them to a release and leaving only the
   manifest rows in git removes them from every clone.
3. **Only then, Git LFS.** LFS is a history rewrite plus a permanent tooling
   dependency for everyone who clones. See the LFS block at the bottom of
   `/.gitattributes` for the exact migration procedure. Do not add `filter=lfs`
   lines to `.gitattributes` by hand — `git lfs migrate import` writes them as
   part of the rewrite, and adding them without the rewrite breaks checkout for
   everyone.

---

## 5. Related

- `/.gitattributes` — binary/text declarations for `drive/`, why no EOL
  normalization is applied (it would invalidate the Drive md5s in the manifest),
  and the LFS migration procedure.
- `drive/MANIFEST.tsv` — per-file Drive id, size, modified time, md5 and status.
