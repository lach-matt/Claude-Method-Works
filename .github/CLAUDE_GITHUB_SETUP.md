# Turning on Claude in this repository

**You do not need to create a webhook by hand.** There is nothing to add under Settings → Webhooks,
and no URL to point anywhere. GitHub already delivers this repository's events to GitHub Actions;
the three steps below just tell it which of those events should wake Claude, and give Claude
permission to answer.

The workflow files in `.github/workflows/` are only half of the wiring. When something happens on
this repo — someone opens an issue, leaves a comment, pushes to a pull request — GitHub sends that
event to GitHub Actions. The workflow files decide which of those events are worth waking Claude
for. But a workflow only gets Claude *running*; it does not get Claude *permission to speak*. That
comes from the Claude GitHub App, which is what lets Claude read the issue, post a comment back,
and push a branch. So there are three manual steps below: install the App, give the workflows a key
so they can talk to Claude, and merge the workflows to `main`. None of these can be done from a
workflow file.

---

## 1. Install the Claude GitHub App

Go to **https://github.com/apps/claude** and install it on this repository.

You need **admin access** on the repo (or on the org, if the repo belongs to one) to do this. The
App requests read/write on Contents, Issues, and Pull requests — that is what Claude uses to read a
thread, reply to it, and commit changes.

This is also why the workflows deliberately do **not** pass a `github_token`. Leaving it out makes
the action authenticate as the App. If you pass `secrets.GITHUB_TOKEN` instead, CI will not run on
commits Claude pushes.

## 2. Add one repository secret

Pick **one** of these two. You do not need both.

| You have | Secret name | Where the value comes from |
| --- | --- | --- |
| A Claude API key | `ANTHROPIC_API_KEY` | https://platform.claude.com |
| A Claude subscription (Pro / Max / Team / Enterprise) | `CLAUDE_CODE_OAUTH_TOKEN` | Run `claude setup-token` locally and copy the output |

Add it here:

> **Settings** → **Secrets and variables** → **Actions** → **New repository secret**

Name the secret exactly as spelled in the table, paste the value, save.

**If you chose `CLAUDE_CODE_OAUTH_TOKEN`,** one line has to change in *both* workflow files. Each
one currently reads:

```yaml
          anthropic_api_key: ${{ secrets.ANTHROPIC_API_KEY }}
```

Replace it with:

```yaml
          claude_code_oauth_token: ${{ secrets.CLAUDE_CODE_OAUTH_TOKEN }}
```

Both files already carry that line commented out just below, so it is a delete-one-line,
uncomment-one-line edit. Do it in `.github/workflows/claude.yml` and
`.github/workflows/claude-code-review.yml`.

## 3. Merge this branch to `main`

Issue, comment and review events carry no branch of their own, so GitHub always runs those
workflows from the **default branch**. Until `claude.yml` is on `main`, `@claude` does nothing at
all, no matter which branch you are reading it on. Merge the pull request that added these files.

`claude-code-review.yml` is the exception: `pull_request` events run the workflow as it exists on
the pull request's own head branch, so that one will already fire on the PR that introduces it.

---

## What the two workflows do

| File | What wakes it | What Claude does |
| --- | --- | --- |
| `.github/workflows/claude.yml` | You write **@claude** in a new issue's title or body, an issue comment, a PR comment, or a PR review | Reads the thread and replies on it. Can also edit files and push a branch, since it has write permissions. |
| `.github/workflows/claude-code-review.yml` | A pull request is opened, updated, reopened, or marked ready for review — **unless** it only touches `drive/`, or it comes from a fork | Runs the `code-review` skill read-only and posts its findings as inline comments on the PR (or one summary comment if it finds nothing). |

The `drive/`-only exclusion is deliberate: PRs that just drop documents into the Drive mirror get
no review, because reviewing a half-gigabyte of PDFs produces nothing useful. A PR that touches
anything outside `drive/` is reviewed, and Claude sees the diff of the `drive/` files in it too.
It sees the changed hunks, not the whole files: the review checkout deliberately leaves `drive/`
off disk, so Claude cannot open one of those documents for surrounding context.

That decision is made by a small `changed-files` job that lists the PR's files through the API,
rather than by a `paths-ignore:` filter on the event. The filter would have been simpler but wrong
for this repo: GitHub evaluates event path filters against only the first 300 files of a pull
request, and the characteristic PR here is a bulk `drive/` drop of hundreds of files that also
touches one file sorting after it — exactly the case where the filter sees nothing but `drive/**`
and the review that was needed never happens. A skipped job also reports "skipped" and satisfies a
required status check, whereas a workflow the filter never creates leaves that check pending
forever.

The fork exclusion is defensive rather than load-bearing: this repository is private, so fork PRs
are not something you will meet in practice. Fork runs get no secrets and no `id-token: write`, so
the review could not authenticate anyway; skipping them keeps the PR from going red after paying
for a runner.

## Try it

Once steps 1–3 are done, open any issue in this repo and post a comment like:

```
@claude what's in drive/MANIFEST.tsv, and roughly how is the material organised?
```

Within a few seconds you should see a reaction appear on your comment. The reply takes
considerably longer: the runner has to fetch the ~508 MB checkout before Claude starts work, so
give it several minutes before concluding anything is wrong. Check the **Actions** tab meanwhile —
it shows whether a run started at all, which is the useful signal.

## When nothing happens

Work down this list; it is almost always one of these.

- **`@claude` has to be a whole word.** `/claude`, `@claude-bot`, `@claudebot` and `email@claude.com`
  do not trigger it. Just `@claude`.
- **The person who commented needs write access** to the repo. Comments from users without write
  access are ignored, and so are comments from bots.
- **The App has to actually be installed** on *this* repository — an org-wide install that excludes
  this repo will not work. Re-check https://github.com/apps/claude.
- **The secret has to exist**, under the exact name the workflow references. A workflow pointing at
  `ANTHROPIC_API_KEY` while the secret is named `CLAUDE_CODE_OAUTH_TOKEN` will start a run and then
  fail in the Claude step.
- **Actions has to be enabled** for the repository. If workflows are disabled in
  Settings → Actions, no event reaches anything.
- **The workflow files have to be on `main`** (step 3). A comment on an issue runs the version of
  the workflow that is on the default branch, not the version on your branch.

## What this costs

Two meters run at once. GitHub charges **Actions minutes** for the runner while the job is alive,
and Anthropic charges **tokens** for what Claude reads and writes during the run.

This repo makes the first meter worse than usual: a full checkout is about **508 MB** of Drive
documents, so a run can spend real time and bandwidth fetching files before Claude does anything.
Both workflows blunt this, in different ways:

- `claude.yml` takes the full tree — it has to, since answering a question about the corpus means
  reading it — but shallow, at `fetch-depth: 1`, and only after a bot-authored event has been
  filtered out.
- `claude-code-review.yml` never materialises `drive/` at all. A sparse checkout excludes it, which
  takes the working tree from 508 MB to a few kilobytes; the review reads the diff from the pull
  request API rather than from local git. A separate one-minute gate job decides whether the PR
  touches anything outside `drive/` and skips the review entirely if it does not.

Both also carry a 30-minute `timeout-minutes` ceiling and a `concurrency` group holding each issue
or PR to one run at a time.

If costs still run high, cap the agent loop with `--max-turns`. The two files need opposite edits:
in `claude.yml` the whole `claude_args` block is commented out, so uncomment it and set a limit
there; in `claude-code-review.yml` `claude_args` already exists and is load-bearing, so append to
that line rather than replacing it.

**Know what that concurrency group does to a burst of comments.** It does not queue them all up.
GitHub keeps at most **one** pending run per group, and each new run that enters the group cancels
the one that was already pending. So posting three `@claude` comments in a row on the same thread
answers the first and the third and silently drops the second — no reply, no error, just a run
marked "cancelled" in the Actions tab. Only genuine mentions compete for the group — it is
declared on the job rather than the whole workflow, so ordinary chatter with no `@claude` in it is
filtered out before anything queues and cannot evict a waiting request. Note that one review
submission can still collide with itself: a review body and two inline comments that all say
`@claude` are three events entering the same group. Wait for one answer before asking the next
thing, and re-ask anything that went unanswered. If you would rather every single mention be
answered at the cost of overlapping runners, delete the `concurrency:` block from
`.github/workflows/claude.yml` and rely on `timeout-minutes` alone.

## Uninstalling

Reverse of the setup, and you can stop at any level:

1. **Stop the workflows.** Delete `.github/workflows/claude.yml` and
   `.github/workflows/claude-code-review.yml` and merge that to `main`. Nothing will run after
   this, whatever else is still configured.
2. **Remove the key.** Settings → Secrets and variables → Actions → delete `ANTHROPIC_API_KEY`
   (or `CLAUDE_CODE_OAUTH_TOKEN`). Do this too if the key might be used elsewhere.
3. **Uninstall the App** (optional). Settings → GitHub Apps → Claude → uninstall, or remove just
   this repository from its installation. Only worth doing if you want Claude to have no standing
   access to the repo; with the workflows gone it has nothing to run from anyway.
