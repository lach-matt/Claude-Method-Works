# Getting Google Drive into this repository

This repository mirrors two Google Drive folders — **The Method Materials** (with its subfolders
`COWORK`, `LOWDIN-DELIVERY-1`, `THREEBODY-DELIVERY-1`, `CORPUS`, `BUILD175-PARTS`,
`Claude Memories`, `Claude Metadata`, `Claude Projects` and `Claude Chats`) and
**The Method Prints & Proofs** — into [`drive/`](../drive/).

Short answer to "how do I get my Drive content into my GitHub repo?":
**run [`tools/drive_sync.py`](../tools/drive_sync.py) on your own machine, then commit and push.**
It has no file-size ceiling, it is incremental, and it rewrites `drive/MANIFEST.tsv` for you.
The full walkthrough is [Route 2](#route-2--toolsdrive_syncpy-run-locally-recommended).

---

## 1. What is already mirrored

Drive holds **823 files** across the two mirrored folders. They arrived in the repo in three waves,
and it matters which is which, because each has a different reason for being incomplete:

| Group | Files | Where it is recorded |
| --- | --- | --- |
| Inventoried by the first mirroring pass | 444 | `drive/MANIFEST.tsv` |
| Added to Drive *after* that pass ran | 18 | `drive/PENDING.tsv` |
| In six subfolders the first pass never walked | 361 | `drive/PENDING.tsv` |

The six subfolders missed entirely were `CORPUS` (346 files), `BUILD175-PARTS`, `Claude Memories`,
`Claude Metadata`, `Claude Projects` and `Claude Chats`. The five folders that *were* mirrored are
intact: every one of the 444 manifest rows was re-checked against Drive and each is still present,
in the folder its `repo_path` implies, with no size drift and no md5 mismatch.

### The two inventories

`drive/MANIFEST.tsv` is what the mirror contains. Tab-separated, header row, eight columns:

```
repo_path  drive_id  drive_title  mime_type  drive_size_bytes  drive_modified  md5  status
```

`drive/PENDING.tsv` is what it is still missing, and why. Six columns:

```
repo_path  drive_id  drive_title  drive_size_bytes  source  reason
```

Regenerate the second one after any sync; a file drops out of it as soon as the local copy matches
the size Drive reports.

### Why files are still outstanding

There are only four reasons, and only one of them needs a decision from you:

1. **Not yet transferred.** Ordinary backlog. `tools/drive_sync.py` clears these.
2. **Above the ~6 MiB connector ceiling.** These cannot come through the Claude Drive connector at
   all — see [Route 1](#route-1--the-claude-google-drive-connector-what-produced-the-current-mirror).
   The script has no such limit.
3. **Above GitHub's 100 MB per-file hard limit.** Two copies of `conversations.json` in
   `Claude Chats` are 370 MB each. No transfer method puts these in the repo as ordinary git
   objects; they need Git LFS or storage outside the repo. See [`REPO-SIZE.md`](REPO-SIZE.md).
4. **Held back pending your decision.** `Claude Metadata/users.json` and
   `Claude Metadata/login_history.json` are Claude account records; the second contains login IP
   addresses, timestamps and user agents. They were left out because git history is permanent and
   awkward to purge, so including them should be a deliberate choice rather than a side effect of a
   bulk sync. To include them, sync that folder explicitly:
   `python3 tools/drive_sync.py --only "Claude Metadata"`

Useful one-liners, from the repo root:

```sh
# everything in the manifest that is not a clean transfer
awk -F'\t' 'NR>1 && $8 !~ /^ok/ {print $8"\t"$1}' drive/MANIFEST.tsv

# what is still outstanding, grouped by reason
awk -F'\t' 'NR>1 {print $6}' drive/PENDING.tsv | sort | uniq -c | sort -rn

# outstanding files by size, largest first
awk -F'\t' 'NR>1 {print $4"\t"$1}' drive/PENDING.tsv | sort -rn | head
```

---

## 2. Three routes

### Route 1 — the Claude Google Drive connector (what produced the current mirror)

The 413 files already here came through the Google Drive MCP connector inside a Claude session.
There is nothing to install and nothing to authorise beyond connecting Drive to Claude once; you
ask for a folder to be mirrored and it happens in the conversation.

**It has a hard payload ceiling just above 6 MiB, and that is why 31 files are missing.**
This is a measured boundary, not a guess:

| | Size | Result |
| --- | ---: | --- |
| Largest file that transferred (`The_Method_1_6_BUILD142_compendia_papers_audits.md`) | 6,303,034 B = 6.011 MiB | **succeeded** |
| Smallest file that failed (`The_Method_1_6_BUILD143_compendia_papers_audits.md`) | 6,365,840 B = 6.071 MiB | **failed** |

Every file at or below 6,303,034 B came through. Every file at or above 6,365,840 B failed. The
ceiling sits somewhere in the 62,806-byte gap between them.

It is a ceiling, not a flaky connection. On 2026-09-02 the smallest failing file
(`1jkCLwgZ_nLrqI3mGx5OrCUdX7B4hSbhm`, 6,365,840 B) was re-tested:

* three separate `download_file_content` calls failed **immediately and identically** with
  `MCP server "Google_Drive" session expired`;
* a `get_file_metadata` call on that same file, through that same connector, **succeeded in
  between**, returning the correct size and mime type.

So the connector and its OAuth session were live throughout. The oversized response payload itself
tears the MCP session down. Retrying cannot help, and neither can `read_file_content`.

All 31 files were re-checked in Drive the same day: 31 of 31 still exist, every reported byte count
matches what was expected, nothing has been modified since 2026-09-01. They are simply out of reach
of this route.

> Seven files in `drive/` are larger than the ceiling (up to 14.2 MB — the `restore-point` tarball,
> `COORDINATES-2_13.csv`, the `figures_BUILD8/9` zips). They did not come through the connector; the
> owner uploaded them directly, and the eight manifest rows concerned say so in their `status`.

**Use this route for:** ad-hoc pulls, small files, exploratory work in a chat session.
**Do not use it for:** anything over ~6 MiB, or for a repeatable scheduled mirror.

---

### Route 2 — `tools/drive_sync.py` run locally (RECOMMENDED)

[`tools/drive_sync.py`](../tools/drive_sync.py) talks to the Drive v3 API directly. Every download is
streamed to a temporary file in 8 MiB chunks and then atomically moved into place, so **nothing is
ever held whole in memory and there is no size ceiling** — only your disk. It skips files whose local
md5 already matches Drive, it verifies the md5 of everything it downloads, and it regenerates
`drive/MANIFEST.tsv` with the exact same eight columns and naming rules the current mirror uses.

Setup is a one-time, roughly ten-minute job.

#### Step 1 — a Google Cloud project with the Drive API enabled

1. Open <https://console.cloud.google.com/projectcreate>, signed in as **lach.matthew@gmail.com**
   (the account that owns the Drive folders). Name the project anything — `drive-sync` is fine —
   and click **Create**.
2. With that project selected, open
   <https://console.cloud.google.com/apis/library/drive.googleapis.com> and click **Enable**.

#### Step 2 — configure the consent screen

1. Open <https://console.cloud.google.com/auth/overview> and click **Get started**.
2. App name: `drive-sync`. User support email: your own address. **Audience: External.**
   Contact email: your own address. Agree and create.
3. Go to the **Audience** page. While the app's publishing status is **Testing**, only listed test
   users can authorise it, so under **Test users** click **Add users** and add
   `lach.matthew@gmail.com`.

> Testing mode is fine for running the script by hand. It matters for
> [Route 3](#route-3--scheduled-sync-from-github-actions): refresh tokens issued by an app in
> Testing status **expire after 7 days**.

#### Step 3 — create a Desktop-app OAuth client and save the JSON

1. Open <https://console.cloud.google.com/auth/clients> and click **Create client**.
2. **Application type: Desktop app.** Name it `drive-sync desktop`. Click **Create**.
3. In the dialog, click **Download JSON**. The file is named something like
   `client_secret_1234567890-abcdef.apps.googleusercontent.com.json`.
4. Move it to the path the script looks in by default:

```sh
mkdir -p ~/.config/drive-sync
mv ~/Downloads/client_secret_*.apps.googleusercontent.com.json \
   ~/.config/drive-sync/credentials.json
chmod 600 ~/.config/drive-sync/credentials.json
```

If you would rather keep it elsewhere, pass `--credentials /path/to/file.json` or set
`GOOGLE_DRIVE_CREDENTIALS=/path/to/file.json`.

The script only ever requests `https://www.googleapis.com/auth/drive.readonly`. It cannot modify or
delete anything in Drive.

#### Step 4 — install the dependencies

Python 3.9 or newer. From the repo root (clone it first with
`git clone https://github.com/lach-matt/Claude-Method-Works.git` if you have not):

```sh
python3 -m pip install -r tools/requirements.txt
```

That installs `google-api-python-client`, `google-auth-oauthlib` and `google-auth-httplib2`. A
virtualenv works too:

```sh
python3 -m venv .venv && . .venv/bin/activate
python3 -m pip install -r tools/requirements.txt
```

#### Step 5 — first run: consent, then a dry run

```sh
python3 tools/drive_sync.py --dry-run -v
```

The first run opens your browser at Google's consent screen. Sign in as
**lach.matthew@gmail.com**, and on the "Google hasn't verified this app" screen click
**Advanced → Go to drive-sync (unsafe)** — that warning is expected for an unverified app you
created yourself. Grant the "See and download all your Google Drive files" permission.

The resulting token is cached at `~/.config/drive-sync/token.json` (mode 600) and refreshed
automatically; the browser flow only runs again if the refresh fails.

`--dry-run` writes **nothing** — not even the manifest. It ends with a summary like:

```
Drive sync summary (/path/to/Claude-Method-Works/drive - DRY RUN):
  added      31
  updated    0
  unchanged  413
  exported   0
  skipped    0
  failed     0
```

That is the confirmation that auth works and that the script sees the same 444 files.

#### Step 6 — fetch just the 31 missing files

`--only` is a plain substring test against the repo path, and it is repeatable:

```sh
python3 tools/drive_sync.py --only BUILD14 --only BUILD15 -v
```

`BUILD14` and `BUILD15` together match BUILD140–BUILD159, which covers all 16 outstanding builds
plus a handful already mirrored. The already-mirrored ones are hashed locally, matched against
Drive's md5, and reported `unchanged` — no bytes are re-downloaded. Expect roughly 112 MB of
transfer (the 16 unique files; the duplicate copies in `LOWDIN-DELIVERY-1` and
`THREEBODY-DELIVERY-1` are fetched as separate paths, so budget ~220 MB of downloading if you want
the pessimistic number).

Files **not** matched by `--only` keep their existing manifest rows, so a narrowed run does not
damage the rest of the inventory.

Then check that nothing is outstanding:

```sh
awk -F'\t' 'NR>1 && $8 !~ /^ok/ {print $8"\t"$1}' drive/MANIFEST.tsv
```

Empty output means all 444 rows are `ok`.

#### Step 7 — full re-sync

With no flags it syncs both folders in full:

```sh
python3 tools/drive_sync.py
```

Every flag, as the script actually defines them:

| Flag | Default | What it does |
| --- | --- | --- |
| `--dest PATH` | `<repo>/drive` | Where the mirror is written; the manifest is `PATH/MANIFEST.tsv` |
| `--folder NAME` | `The Method Materials`, `The Method Prints & Proofs` | Drive folder name to sync. Repeatable. **Overrides the defaults.** |
| `--folder-id ID` | — | Drive folder id to sync. Repeatable. **Overrides the defaults.** |
| `--only SUBSTRING` | — | Only sync files whose repo path contains SUBSTRING. Repeatable. Unmatched files keep their manifest rows. |
| `--credentials PATH` | `$GOOGLE_DRIVE_CREDENTIALS`, else `~/.config/drive-sync/credentials.json` | OAuth client secrets |
| `--token PATH` | `~/.config/drive-sync/token.json` | Cached OAuth token |
| `--jobs N` | `4` | Parallel download workers |
| `--dry-run` | off | Report what would change; write nothing, not even the manifest |
| `--prune` | off | Delete local files that are no longer in Drive (otherwise they are only reported) |
| `--verbose`, `-v` | off | Debug logging |

Exit code is `0` when nothing failed, `1` if any file failed or any prune failed.

If a folder name is ambiguous (two folders in Drive share it), the script refuses to guess and
prints the exact `--folder-id ...` lines to choose from. Folder ids are also visible in the Drive
URL: `https://drive.google.com/drive/folders/<ID>`. Confirmed ids for this mirror:

```
1XX_5f3PZB6tjRtiZ2GIgd8Tt7i_4GgkY   The Method Materials
1aQe7IofPbSQrudSYr_Iq0hgUtTZDlw3Q   The Method Materials/LOWDIN-DELIVERY-1
1iMguyEFqM7OiNa5NQXhVITlvrd7NLVL1   The Method Materials/THREEBODY-DELIVERY-1
```

#### Step 8 — commit and push

```sh
git add drive
git status --short | head
git commit -m "Sync the remaining large Drive builds (BUILD143-BUILD158)"
git push origin HEAD
```

The current work is on branch `claude/google-drive-github-sync-3833rb` of
`github.com/lach-matt/Claude-Method-Works`. Pushing ~220 MB of new Markdown will take a few minutes;
git delta-compresses these builds against each other well, so the pack grows far less than the
working tree does. See [`REPO-SIZE.md`](REPO-SIZE.md) for the measured numbers and the trigger points
for when the repo would actually need Git LFS.

---

### Route 3 — scheduled sync from GitHub Actions

If you want Drive changes to land in the repo without you doing anything, run the same script on a
schedule in Actions. The only hard part is credentials: an Actions runner cannot open a browser, so
you hand it the token you already minted locally in Step 5.

**How it works.** `~/.config/drive-sync/token.json` contains an access token, a **refresh token**,
the token URI, and your OAuth client id and secret. Given that file, the script refreshes itself and
never needs `credentials.json` or a browser. So: store the file's contents as a repository secret,
write it back to disk at the start of the job, run the sync, commit whatever changed.

```sh
# locally, after Step 5 has succeeded
cat ~/.config/drive-sync/token.json
```

Copy that JSON into **Settings → Secrets and variables → Actions → New repository secret**, named
`GOOGLE_DRIVE_TOKEN`.

`.github/workflows/drive-sync.yml`:

```yaml
name: Drive sync

on:
  schedule:
    - cron: "17 6 * * 1"        # Mondays, 06:17 UTC
  workflow_dispatch:            # and on demand from the Actions tab

permissions:
  contents: write

jobs:
  sync:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - uses: actions/setup-python@v5
        with:
          python-version: "3.12"

      - run: python -m pip install -r tools/requirements.txt

      - name: Restore the cached OAuth token
        env:
          DRIVE_TOKEN_JSON: ${{ secrets.GOOGLE_DRIVE_TOKEN }}
        run: |
          mkdir -p ~/.config/drive-sync
          printf '%s' "$DRIVE_TOKEN_JSON" > ~/.config/drive-sync/token.json
          chmod 600 ~/.config/drive-sync/token.json

      - name: Sync Drive into drive/
        run: python tools/drive_sync.py --jobs 4

      - name: Refuse to commit anything GitHub would reject
        run: |
          big=$(find drive -type f -size +99M -print)
          if [ -n "$big" ]; then
            echo "These files exceed GitHub's 100 MiB per-file limit:"; echo "$big"; exit 1
          fi

      - name: Commit and push any changes
        run: |
          git config user.name  "drive-sync"
          git config user.email "actions@github.com"
          git add drive
          git diff --cached --quiet && { echo "no changes"; exit 0; }
          git commit -m "Drive sync $(date -u +%Y-%m-%dT%H:%MZ)"
          git push
```

**Read these warnings before enabling it.**

* **It puts a long-lived Google credential in GitHub secrets.** `token.json` holds a refresh token
  *and* your OAuth client secret. Anyone who can push a workflow to this repository can print that
  secret. Only do this in a repository you fully control, with a short collaborator list. Revoke
  access any time at <https://myaccount.google.com/permissions>; rotate by deleting the OAuth client
  in the Cloud console.
* **Keep the scope at `drive.readonly`.** That is all `drive_sync.py` requests, and it means a leaked
  token cannot delete or overwrite anything in Drive. Do not substitute a token minted with a broader
  scope.
* **It commits large files automatically, with no review.** A new 7 MB build lands in history the
  moment the schedule fires, and history is expensive to undo. The size-guard step above stops the
  one case GitHub hard-rejects (100 MiB), but nothing stops steady growth. Re-read
  [`REPO-SIZE.md`](REPO-SIZE.md) occasionally.
* **A Testing-status OAuth app issues refresh tokens that expire after 7 days.** The scheduled job
  will start failing about a week after you create the secret. Either publish the app
  (Google Auth Platform → **Audience** → **Publish app**, which moves it to "In production" and
  makes refresh tokens long-lived), or plan to re-mint `GOOGLE_DRIVE_TOKEN` weekly.
* **Actions has no view of Drive deletions unless you ask for them.** The workflow above does not
  pass `--prune`, so files removed from Drive stay in the repo and are merely reported in the job log.
  That is the safe default; add `--prune` only deliberately.

---

### Alternative — rclone, if you would rather not run a bespoke script

[rclone](https://rclone.org/drive/) is a mature off-the-shelf Drive client with the same streaming
(so, no size limit) behaviour:

```sh
rclone config                      # n) new remote -> name: gdrive -> storage: drive -> scope: 2 (drive.readonly)
rclone copy "gdrive:The Method Materials" "drive/The Method Materials" \
    --drive-export-formats md,csv,pdf,png --checksum --progress
```

Trade-off: rclone will not produce `drive/MANIFEST.tsv`, and it resolves same-title files differently
from the `__<driveFileId>` convention this mirror uses, so paths can drift from the manifest. If you
pull with rclone, follow it with `python3 tools/drive_sync.py --dry-run` to see what the manifest
thinks, and a real run to rewrite it (files rclone already fetched correctly hash as `unchanged`).

---

## 3. Keeping it in sync afterwards

Re-running is the whole workflow. From the repo root:

```sh
python3 tools/drive_sync.py --dry-run     # what would change?
python3 tools/drive_sync.py               # do it
git add drive && git commit -m "Drive sync" && git push origin HEAD
```

**Incremental by default.** For an ordinary file the script compares the local md5 against Drive's
`md5Checksum`; equal means `unchanged` and nothing is downloaded. For an exported Google-native doc
(Drive publishes no md5 for those) it compares the manifest's recorded md5 against the local file and
checks that Drive's `modifiedTime` has not advanced. So a no-op re-sync of all 444 files costs one
listing pass plus local hashing.

**`--dry-run`** writes nothing at all — no files, no manifest — and prints the same summary table
with `- DRY RUN` in the heading. Use it before every real run; it is the cheapest way to see whether
Drive has changed.

**`--prune`** deletes local files inside the mirrored folders that Drive no longer has, then removes
any directories they leave empty. Without it, orphans are only listed:

```
3 local file(s) are no longer in Drive (re-run with --prune to delete):
  The Method Materials/old-draft.md
  ...
```

`--prune` is ignored under `--dry-run`. It only walks the mirrored root directories, so
`drive/MANIFEST.tsv` and `drive/README.md` are never candidates, and a file named `README.md` or
`MANIFEST.tsv` inside a mirrored folder is protected by name as well. It will, however, delete
anything *you* put inside `drive/` by hand — treat that tree as generated.

**The manifest is the change log.** It is rewritten on every non-dry run, sorted by `repo_path`, so
`git diff` on it is a precise account of what the sync did:

```sh
git diff --stat -- drive/MANIFEST.tsv    # how many rows moved
git diff -- drive/MANIFEST.tsv           # which ones, and what changed
```

Status strings you will see:

| `status` | Meaning |
| --- | --- |
| `ok` | Downloaded or exported and verified |
| `skipped: unsupported Google-native type ...` | A Drive type with no export format (Forms, Sites, …) |
| `export-too-large: Drive will not export documents over 10 MB` | Drive's own `files.export` ceiling |
| `failed: ...` | Transport or API error, or an md5 mismatch after download |
| `not-checked: excluded by --only` | A `--only` run that had no previous row to carry forward |

The console summary counts the same outcomes under `added / updated / unchanged / exported /
skipped / failed`, and lists every failure with its status line.

---

## 4. Limits and gotchas

**GitHub's 100 MiB per-file hard limit.** Pushes containing a file over 100 MiB are rejected
outright, and the limit applies to the blob *anywhere in history* — committing a large file and
deleting it later does not help; the history has to be rewritten. GitHub warns at 50 MiB. The largest
file here today is 13.58 MiB and the largest outstanding one is 7.26 MiB, so there is a lot of
headroom; [`REPO-SIZE.md`](REPO-SIZE.md) has the full audit and the trigger points at which Git LFS
would genuinely be worth its cost.

**Google-native docs are exports, not byte-exact copies.** Google Docs, Sheets, Slides and Drawings
have no downloadable bytes, so the script asks Drive to export them:

| Drive type | Exported as |
| --- | --- |
| Google Docs | Markdown (`.md`) |
| Google Sheets | CSV (`.csv`) |
| Google Slides | PDF (`.pdf`) |
| Google Drawings | PNG (`.png`) |

The recorded size is the size of the export, which will not match what the Drive UI shows for the
native file, and formatting that Markdown or CSV cannot express is lost. Drive also refuses to export
a native document larger than 10 MB — that shows up as `export-too-large` in the manifest, and the
only fix is to split the document in Drive. Five Google Docs in the current mirror are exports.

**The `__<fileId>` duplicate-title rule.** Drive lets several files in one folder share a title;
a filesystem does not. Within each folder the **most recently modified** copy keeps the plain name and
every older copy gets `__<driveFileId>` inserted before the extension, for example:

```
The_Method_1_6_figures_BUILD9.zip
The_Method_1_6_figures_BUILD9__1AtBAHB7Dwr8QlUmiV1_EaPNMR1X2g-kN.zip
```

Ties are broken by ascending Drive file id, so the assignment is stable across runs. One consequence:
if you edit the *older* copy in Drive so it becomes the newest, the two names swap on the next sync
and git will show it as two modified files.

**The mirror is one-way — Drive → repo, never the reverse.** The script holds `drive.readonly` and
has no upload path. Editing a file under `drive/` does not push anything to Drive; it just makes the
local md5 disagree with Drive's, and the next sync will **overwrite your edit** with the Drive copy.
Make changes in Drive, then sync. If you need a derived or annotated version, keep it outside
`drive/`.

**A narrowed run can narrow the manifest.** `--only` is safe: unmatched files keep their existing
rows. `--folder` and `--folder-id` are not — they replace the default folder list, and the manifest is
regenerated from what the run actually walked, so syncing one folder alone drops the other folder's
rows from `MANIFEST.tsv`. Use `--only` to do less work; use `--folder`/`--folder-id` only when you
mean to change what the mirror covers.

**A full re-sync rewrites hand-edited manifest notes.** A few rows currently carry human annotations
(`ok (uploaded directly by owner, size matches Drive)`). The script writes plain `ok` for anything it
verifies, so those notes disappear on the next full run. That is correct — the file will have been
verified by the script at that point — but do not expect prose to survive in that column.

**Consent needs a browser on the machine running the script.** `run_local_server` opens a local
listener and a browser window. On a headless box, do Step 5 on a desktop and copy
`~/.config/drive-sync/token.json` across (mode 600), or forward the port over SSH.

**No line-ending translation.** `/.gitattributes` deliberately disables EOL normalisation for
everything under `drive/`: six mirrored files genuinely contain CRLF because that is what is in
Drive, and rewriting line endings on checkout would silently invalidate the md5s recorded in
`MANIFEST.tsv`.

---

## Related

* [`../tools/drive_sync.py`](../tools/drive_sync.py) — the sync script (`--help` prints the flags)
* [`../tools/requirements.txt`](../tools/requirements.txt) — its three dependencies
* [`../drive/MANIFEST.tsv`](../drive/MANIFEST.tsv) — per-file Drive id, size, modified time, md5, status
* [`REPO-SIZE.md`](REPO-SIZE.md) — size audit, GitHub limits, and when LFS would be worth it
* [`../.gitattributes`](../.gitattributes) — why `drive/` gets no EOL translation
