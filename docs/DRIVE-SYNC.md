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

**819 of the 823 Drive files across the two mirrored folders are in `drive/`, each verified by md5
against the copy Drive served.** Four remain outstanding.

Getting there took two passes, and the difference between them is the whole lesson of this document:

| Pass | Route | Result |
| --- | --- | --- |
| First | Claude Drive connector, from a chat session | 413 files, and a wrong idea of the total |
| Second | [Colab](#route-4--google-colab-if-you-would-rather-install-nothing), mounting Drive as a filesystem | 283 more files in one run, all byte-exact |

The first pass missed more than it knew. It never walked six subfolders of "The Method Materials"
(CORPUS with 346 files, BUILD175-PARTS, Claude Memories, Claude Metadata, Claude Projects and
Claude Chats, 361 files between them), 18 files were added to Drive after it ran, and 31 files were
above a payload ceiling it could not cross. What it did mirror was sound: all 444 of its rows
re-checked against Drive with no drift and no md5 mismatch.

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

## 2. Four routes

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

### Route 4 — Google Colab, if you would rather install nothing

[`tools/drive_sync_colab.ipynb`](../tools/drive_sync_colab.ipynb) does Route 2's job from a browser
tab. Colab mounts *your own* Drive as a filesystem with `google.colab.drive.mount`, so the files are
just files: **no local Python, no Google Cloud project, no OAuth client, no `credentials.json` — and
no size ceiling, because nothing is being passed through an API payload.** The notebook copies what
`drive/PENDING.tsv` still lists, size-verifies it, commits and pushes.

What you pay for that:

| | Route 2 — local script | Route 4 — Colab |
| --- | --- | --- |
| Setup | Cloud project, OAuth desktop client, `pip install` | a GitHub token; one click to authorise Drive |
| Size ceiling | none | none |
| Credential exposed | a Google **read-only** refresh token, on your own machine | a **GitHub write token, pasted into a VM you do not own** |
| Rewrites `MANIFEST.tsv` | yes, from Drive | **no** — it prints provisional rows only |
| Google-native Docs/Sheets/Slides | exported properly | **cannot fetch them** — a mount shows a ~200-byte `.gdoc` pointer, not the document |
| Verification | Drive md5, per file | **size only** — `PENDING.tsv` carries no md5 |
| Duplicate titles | resolved by Drive file id | **cannot be told apart** — a filesystem shows one name once |
| Persistence | a machine you own | **ephemeral** — when the runtime is recycled the VM, the clone and the token copy are gone |

That last row is the real cost: the runtime dies on idle, so an interrupted transfer restarts from
cell 1. And the token is a *write* credential on the repository, sitting on Google's hardware for the
life of the session. Mint it with a short expiry and revoke it when you are done.

#### Before you start

1. **A GitHub personal access token.** Classic: `repo` scope. Fine-grained: *Contents: read and
   write* on `lach-matt/Claude-Method-Works`. <https://github.com/settings/tokens>. Short expiry.
2. **The Google account that owns the two Method folders**, to authorise the mount.
3. **Open the notebook in Colab.** This repository is private, so the dependable way is
   <https://colab.research.google.com> → **File → Upload notebook** → your local copy of
   `tools/drive_sync_colab.ipynb`. Colab's **GitHub** tab works too, but only after you grant it
   private-repository access.

#### The cells, and what each one actually does

Run them in order, once each. Every cell checks its own preconditions and stops with a readable
message rather than guessing, so one run out of order tells you what to run first.

* **Cell 1 — mount Drive and resolve the two source folders.** Pops the authorisation dialog, mounts
  at `/content/drive`, then finds `The Method Materials` and `The Method Prints & Proofs` under
  `/content/drive/MyDrive`. It matches names ignoring surrounding whitespace and dots — the real
  Drive title of the first folder has a **trailing space**, which no path you type by hand will match
  — and prints the resolved paths with `repr()` so that space is visible. If two entries match after
  normalisation it raises rather than picking one. Ends with a file/subfolder/MiB count per folder.
* **Cell 2 — clone the repository.** Reads the token with `getpass` (hidden input), writes it to a
  credential-store file at `/content/.git-credentials`, mode `0600`, and points git at it with
  `credential.helper store`. That indirection is deliberate: a `https://TOKEN@github.com/...` clone
  URL would leave the token in `.git/config`, the process list and any error git prints. The cell
  then clones — or, if `/content/repo` already exists, fetches and checks out — branch
  `claude/google-drive-github-sync-3833rb`, sets the commit author, asserts that `.git/config`
  contains no credential, and scrubs every subprocess's output before showing it.
* **Cell 3 — copy the missing files in.** Driven entirely by `drive/PENDING.tsv`, so there is no
  second inventory to keep in step. For each row it walks `repo_path`'s directory components down the
  mount with the same whitespace-tolerant matching, copies to a `.part` file and renames into place
  (an interrupted run never leaves a truncated file that looks finished), and records what it did in
  `/content/drive_sync_colab_state.json`. It **skips** two kinds of row: any whose `reason` mentions
  the 100 MB limit — the two `conversations.json` exports, see [§5](#5-the-two-370-mib-chat-exports) —
  and any marked *held back*, the Claude account records, unless you set `INCLUDE_HELD_BACK = True`
  at the top of the cell. Where a title is duplicated in Drive (`conversations.json`, and
  `The_Method_1_6_BUILD178_compendia_papers_audits.md`, whose two copies are both 5,619,374 bytes) it
  says so loudly instead of pretending to know which copy is which.
* **Cell 4 — verify against `drive_size_bytes`.** A byte count is a weak checksum but it is the only
  one available here, and it catches what actually goes wrong on a mount: a truncated copy, a
  Google-native doc that appeared as a small `.gdoc` pointer, or the wrong copy of a duplicated
  title. **Any mismatch stops the run** and leaves `verified: false` in the state file.
* **Cell 5 — manifest rows for the new files.** The notebook cannot regenerate `MANIFEST.tsv` and
  does not pretend to: two of the eight columns are unknowable from a mount, so `mime_type` is
  guessed from the extension and `drive_modified` is written as `unknown`. The md5 it computes is
  real. Rows are printed and saved to `/content/manifest-additions.tsv`, which is outside the clone
  so it cannot be committed by accident.
* **Cell 6 — commit and push.** Stages **only the individual files cell 3 recorded**, by path from
  the state file — not the whole `drive/` tree, so nothing cell 4 did not size-verify (a shard tree
  from the appendix, say) can be swept into the commit. Refuses to commit if cell 4 did not verify, or
  if the clone is not on `claude/google-drive-github-sync-3833rb`. "Nothing to commit" is treated as
  an ordinary outcome. It deletes `/content/.git-credentials` and unsets the global credential helper
  after a successful push **and on the "nothing to commit" path**; the one case it keeps them is a
  failed push, so a retry does not re-prompt for the token.
* **Section 7 (markdown only) — what to do when the push is rejected.** `non-fast-forward` (someone
  pushed after cell 2 cloned: `git pull --rebase`, then push), `403` (the token lacks scope or has
  expired), how to revoke the token, and how to disconnect the runtime.
* **Appendix cell — the two 370 MiB exports.** Commits nothing. `APPENDIX_MODE = "checksum"` (the
  default) md5s every copy the mount exposes and says whether they are genuinely the same bytes;
  `APPENDIX_MODE = "shard"` hands one to `tools/shard_conversations.py`, dry-running until you set
  `SHARD_CONFIRM = True`, and writing to `/content/chats-shards` — outside the clone, so moving the
  shards into `drive/chats` stays a deliberate step. Note that a Drive **mount** normally exposes only
  one file per name per folder, so the checksum mode usually cannot settle whether the two Drive
  copies are identical; that needs the Drive API (Route 2) or the Drive web UI.
  See [§5](#5-the-two-370-mib-chat-exports).

#### Afterwards, two things

```sh
python3 tools/drive_sync.py        # from a machine that has the OAuth client
```

The notebook leaves both inventories stale: `MANIFEST.tsv` is missing the true mime types, Drive
modification times and verified md5s for whatever it copied, and `PENDING.tsv` still names files that
are now in the repo. One ordinary Route 2 run rewrites `MANIFEST.tsv` from Drive itself — but **not**
`PENDING.tsv`, which no tool in this repo generates. That one is hand-maintained, so its stale rows
have to be edited out by hand (or rebuilt from `MANIFEST.tsv` plus a Drive listing).

Then **revoke the token** at <https://github.com/settings/tokens>. Cell 6 removes the credential file
and the VM is destroyed when the runtime is recycled, but a token that still exists on GitHub is
still a live write credential.

**Use this route for:** clearing the backlog once, from a machine you do not want to install anything
on, or from a Chromebook or a phone.
**Do not use it for:** Google-native documents, a scheduled mirror (that is Route 3), or any situation
where a GitHub write token on rented hardware is not acceptable.

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

**GitHub's 100 MiB per-file hard limit — 104,857,600 bytes.** Pushes containing a file over that
size are rejected outright, with no override, and the limit applies to the blob *anywhere in
history* — committing a large file and deleting it later does not help; the history has to be
rewritten. GitHub warns at 50 MiB and blocks at 100 MiB. Measured against this repo on 2026-09-02:
the largest tracked file is **14,238,681 B (13.58 MiB)** — `restore-point-2_13.tar.gz`;
the largest outstanding file that *can* be committed is 7.26 MiB; and **no** tracked file exceeds
even the 50 MiB warning line. There are exactly two exceptions, and they are the two copies of
`conversations.json` in `Claude Chats` at **388,264,753 bytes (370.3 MiB) each** — 3.7× the hard
limit, and the only files in either Drive folder that cannot enter this repo as ordinary git objects
by any route. [§5](#5-the-two-370-mib-chat-exports) is about what to do with them;
[`REPO-SIZE.md`](REPO-SIZE.md) has the full audit and the trigger points at which Git LFS would
genuinely be worth its cost.

**The Claude Drive connector's ~6 MiB payload ceiling.** Also a measurement, taken on 2026-09-02 by
bisecting what did and did not arrive: `The_Method_1_6_BUILD142_compendia_papers_audits.md` at
**6,303,034 bytes (6.011 MiB) succeeded**, and `The_Method_1_6_BUILD143_compendia_papers_audits.md`
at **6,365,840 bytes (6.071 MiB) failed**. Everything at or below the first size came through;
everything at or above the second did not; the ceiling sits somewhere in the 62,806-byte gap between
them. It is a ceiling, not a flaky link — three retries of the smallest failing file failed
immediately and identically with `MCP server "Google_Drive" session expired`, while a
`get_file_metadata` call on that same file through that same connector succeeded in between, so the
oversized response payload is what tears the MCP session down. `drive/PENDING.tsv` marks **34 rows**
with this reason today. Routes 2, 3 and 4 have no such ceiling, because none of them passes file
bytes through an MCP response; see
[Route 1](#route-1--the-claude-google-drive-connector-what-produced-the-current-mirror) for the full
account.

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

## 5. The two 370 MiB chat exports

### The facts

`The Method Materials/Claude Chats` holds two files, both titled `conversations.json`, and both
**exactly 388,264,753 bytes** (370.3 MiB). Their `drive/PENDING.tsv` rows, with the size column:

```
The Method Materials/Claude Chats/conversations.json                                     1HDX_rVzgr_JYFylw5MhwFPGumLLj-lsc  388264753
The Method Materials/Claude Chats/conversations__1S4_14PIRBPs39v0tetd98RHiU3JcEkaQ.json  1S4_14PIRBPs39v0tetd98RHiU3JcEkaQ   388264753
```

Identical title, identical byte count: they are almost certainly the same export saved twice.
**Keep one.** Confirm before deleting anything — same size is strong evidence, not proof:

```sh
# both copies, into a scratch directory OUTSIDE the repo (740 MiB of download)
python3 tools/drive_sync.py --dest ~/drive-scratch --only "Claude Chats" -v
md5sum ~/drive-scratch/"The Method Materials/Claude Chats/"conversations*.json
```

`--dest` is what keeps them out of the working tree; without it they land in `drive/` and the next
`git add drive` stages a file GitHub will refuse. (The Colab notebook's appendix cell will md5 them
too, but a mounted filesystem cannot show two files with the same name in one folder, so it can only
ever see one of the two.)

### Why no transfer method fixes this on its own

GitHub **rejects any single file over 100 MiB** (104,857,600 bytes) at push time, with no override,
and the limit applies to the blob *anywhere in history* — committing one and deleting it in a later
commit does not help; only a history rewrite does. Every route in [§2](#2-four-routes) produces the
same 388,264,753-byte file, so this is not a transfer problem and no transfer method solves it. The
file has to change shape before it can enter git, or stay outside git.

The obvious dodge — `split -b 90M` into parts under the limit — technically pushes, and is still the
wrong answer:

* it adds **~740 MiB** for both copies (370 MiB for one) to a working tree already measured at
  **508 MiB** ([`REPO-SIZE.md`](REPO-SIZE.md));
* arbitrary byte ranges of dense JSON do not delta-compress, so unlike the Markdown builds this
  weight lands in the pack roughly at full size, on every clone, forever;
* and the parts are inert. Nothing can read, diff, grep or index them until someone `cat`s them back
  into a 370 MiB file. You would be paying git's price for none of git's benefits.

### The three real options

#### (a) RECOMMENDED — shard it with `tools/shard_conversations.py`

One readable JSON file per conversation, an `INDEX.tsv` beside them, nothing anywhere near the
limit — and it is the only option that makes the content **searchable in the repo** (`git grep`,
GitHub code search, ordinary diffs when a conversation changes) and **indexable by Graphify**, which
wants many small files and can do nothing with one opaque blob.

```sh
# 0. one-time: a streaming JSON parser, so a 370 MiB input is read at flat memory.
#    Without ijson the script falls back to json.load, which needs roughly 3 GB of
#    RAM for this file. It always warns on stderr; it never does that silently.
python3 -m pip install ijson

# 1. if you have not already: the exports into a scratch directory outside the repo.
#    --only matches both copies, so this fetches 740 MiB; you shard one of them.
python3 tools/drive_sync.py --dest ~/drive-scratch --only "Claude Chats" -v

# 2. look before writing: parser, detected schema, conversation and message counts,
#    projected output size, and whether --max-files would refuse. Writes nothing.
python3 tools/shard_conversations.py \
    ~/drive-scratch/"The Method Materials/Claude Chats/conversations.json" --dry-run

# 3. write the shards (see the note below on why drive/chats and not Claude Chats/)
python3 tools/shard_conversations.py \
    ~/drive-scratch/"The Method Materials/Claude Chats/conversations.json" \
    --out drive/chats

# 4. sanity check: nothing anywhere near the limit. Step 3's summary also names
#    the largest shard it wrote, and re-parses every one of them.
find drive/chats -type f -size +40M -print          # expect no output at all
du -sh drive/chats

# 5. commit
git add drive/chats
git commit -m "drive: shard the Claude Chats conversations.json export into drive/chats"
git push origin HEAD
```

What you get: `drive/chats/<YYYY-MM>/<conversation-id>.json`, one file per conversation, grouped by
creation month, with undated conversations in `drive/chats/undated/`; plus `INDEX.tsv` (seven
columns — `shard_path conversation_id title created_at updated_at message_count bytes`) and
`SUMMARY.json` recording the input size, the detected schema and the verification result. The script
re-reads and re-parses every shard it wrote before reporting success, and exits `0` only if all of
them parse (`1` on a refusal or a failed verification, `2` on bad arguments). The shards are not
part of the Drive mirror, so `MANIFEST.tsv` will never describe them — `INDEX.tsv` and
`SUMMARY.json` are their inventory.

Three things worth knowing before you run it:

* **`--out drive/chats`, not inside a mirrored folder.** `--prune` walks the mirrored root
  directories and deletes anything Drive does not have, so shards written into
  `drive/The Method Materials/Claude Chats/` would be deleted by the next
  `python3 tools/drive_sync.py --prune`. `drive/chats/` sits inside `drive/` but outside both
  mirrored roots, so it survives. `/.gitattributes` already covers it: `drive/**/*.json` gets a real
  line-by-line diff with no EOL translation, and `drive/**` is `linguist-generated=true`, so several
  thousand shards stay out of the language statistics and collapsed in pull-request diffs.
* **`--max-files` defaults to 5000.** Tens of thousands of tiny files is its own problem for git, so
  the script refuses past that limit rather than discovering it halfway through; the `--dry-run` in
  step 2 tells you the count in advance, and it prints the exact `--max-files N` to re-run with if
  that really is what you want.
* **`--force` is required to write into a non-empty `--out` directory.** A second run into
  `drive/chats` will otherwise stop and tell you to move it aside or choose another path.

Sharding does not make the content free — the conversations still add their weight to every clone.
But it is weight you can read, and the shards do at least compress and delta like the text they are.

#### (b) `--gzip` — one small object, and nothing else

```sh
python3 tools/shard_conversations.py \
    ~/drive-scratch/"The Method Materials/Claude Chats/conversations.json" \
    --gzip --out drive/chats
```

`--gzip` applies the same non-empty-directory rule as sharding: if `drive/chats` already holds a
shard run, it refuses rather than dropping a `.gz` beside those shards and overwriting the
`SUMMARY.json` that is the only record of what they are. Use a separate `--out`, or `--force` if you
have decided the shards are disposable.

Writes a single `drive/chats/conversations.json.gz`. JSON compresses roughly ten to one, so expect
around 35 MiB — comfortably under the 100 MiB limit. The script measures the real ratio rather than
trusting that estimate, verifies that the result decompresses back to exactly 388,264,753 bytes, and
**refuses to leave the file behind at all** if it still came out over 100 MB, pointing you at
sharding instead. `--gzip --dry-run` compresses the first 64 MiB to measure the ratio and projects
the final size. This mode never parses the JSON, so it needs neither `ijson` nor any real memory.

The cost is everything the file was worth having in the repo for: no diffs, no `git grep`, no GitHub
code search, no Graphify value. It is a backup that happens to live in git.

#### (c) Keep it out of git

* **Git LFS.** GitHub's free tier is **1 GB of LFS storage and 1 GB/month of bandwidth**, per
  account, shared across every repository you own. Both copies at 740 MiB would take roughly three
  quarters of the storage allowance immediately, and a single clone that fetched them would take
  roughly three quarters of the month's bandwidth; one copy at 370 MiB is still about 40% of each.
  Adoption is also a history rewrite plus a filter every collaborator has
  to have installed — see the LFS block at the bottom of [`/.gitattributes`](../.gitattributes) for
  the procedure and [`REPO-SIZE.md`](REPO-SIZE.md) for the trigger point at which it becomes worth
  its cost (packed `.git` at 1 GiB, roughly 12× today's 83 MiB).
* **A GitHub release asset.** 2 GB per asset, and it never enters history or the working tree, so it
  costs nothing on clone:

  ```sh
  gh release create chat-export-2026-09 \
      ~/drive-scratch/"The Method Materials/Claude Chats/conversations.json" \
      --title "Claude chat export" --notes "Full conversations.json, 388,264,753 bytes."
  ```

  This is the cheapest way to have the exact original bytes reachable from the repository. It is a
  fine complement to (a): shard the content for reading and searching, attach the original for
  fidelity.

Whichever you choose, the two `PENDING.tsv` rows stay — correctly. Those Drive files are still not
mirrored, and the reason column already says why.

**The recommendation, in one line:** md5 both copies, delete the duplicate in Drive, shard the
survivor into `drive/chats/`, and attach the original as a release asset if you want the exact bytes
kept somewhere.

---

## Related

* [`../tools/drive_sync.py`](../tools/drive_sync.py) — the sync script (`--help` prints the flags)
* [`../tools/requirements.txt`](../tools/requirements.txt) — its three dependencies
* [`../tools/drive_sync_colab.ipynb`](../tools/drive_sync_colab.ipynb) — the Colab notebook of Route 4
* [`../tools/shard_conversations.py`](../tools/shard_conversations.py) — shards or gzips a chat export (§5)
* [`../drive/MANIFEST.tsv`](../drive/MANIFEST.tsv) — per-file Drive id, size, modified time, md5, status
* [`REPO-SIZE.md`](REPO-SIZE.md) — size audit, GitHub limits, and when LFS would be worth it
* [`../.gitattributes`](../.gitattributes) — why `drive/` gets no EOL translation
