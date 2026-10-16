# `tools/sitecheck.mjs` — the site, clicked through

`tools/webindex.py --selftest` checks the data the site is built from; it cannot press a button.
`sitecheck.mjs` does: it opens the site in headless Chromium, clicks, types, goes Back and Forward,
reloads, rotates a phone, and checks what a reader would see. It was written when the Papers dialog
learnt to open a paper from its cite address (PRs #51 and #52) and the routing, focus and history
behaviour around it needed proving in a browser; its scenarios are the ones those reviews found.

## The address is always the site's own

Every run opens the page at **`https://lach-matt.github.io/Claude-Method-Works/`**, so the page's
origin, its history entries and every address it writes are the deployed site's — the history
behaviour under test depends on them. What changes between targets is only where the bytes come from:

| `--target` | The files served at that address | Use it to |
| --- | --- | --- |
| `worktree` (default) | this checkout's `public/` | check a change before committing it |
| `commit[=REV]` | `public/` of a commit, by `git archive` (default `origin/main`) | check what Pages deployed |
| `live` | the network | check GitHub's own serving, where the proxy allows it |

**`commit` holds the commit's key files against the copy GitHub serves** for that commit, from
`raw.githubusercontent.com` (reachable through this environment's proxy, which refuses
`lach-matt.github.io`), and stops if any differs: `index.html`, `script.js`, `style.css`,
`data/index.js`, `data/papers.js` and the Everything Is Relative PDF. The Pages workflow uploads
`public/` from the commit it deploys, so these are the bytes a reader receives; what the run does
not exercise is GitHub's server sending them.

**`live` needs the session's network access to allow `lach-matt.github.io`.** Where it does not, the
run stops at once with exit status 2 and says so, rather than reporting a page it never loaded.

The page Back must reach before the site is a stand-in (`https://elsewhere.example/`) the harness
serves itself, and fonts and other hosts are refused: no target needs any other host.

## Running it

```
node tools/sitecheck.mjs                          # all scenarios, this checkout's public/
node tools/sitecheck.mjs --target commit          # the deployed main
node tools/sitecheck.mjs --target commit=HEAD~1   # any commit
node tools/sitecheck.mjs --target live            # the network, where allowed
node tools/sitecheck.mjs --suite papers,review    # some suites
node tools/sitecheck.mjs --nonav                  # a browser without the Navigation API
node tools/sitecheck.mjs --list                   # name the scenarios, run nothing
node tools/sitecheck.mjs --root /tmp/copy/public  # serve another directory (a built or a broken copy)
```

About six minutes for all scenarios. It needs Node and Playwright with Chromium, which this
environment carries (`/opt/node22/lib/node_modules/playwright`, `/opt/pw-browsers/chromium`);
`PLAYWRIGHT_MODULE` and `CHROMIUM` point it elsewhere. Exit status: **0** every check passed and the
page threw nothing, **1** a check failed or the page threw, **2** the run could not start.

## What it checks — 26 scenarios, 102 checks

Each scenario runs in fresh browser contexts, closed when it ends, so one cannot leak into the next;
a scenario that throws is reported as a failure and the run goes on.

- **`papers`** — the Papers dialog has a card for every held paper, Everything Is Relative last;
  its reader shows the front matter's title block (title, standfirst, byline, no YAML), contents for
  every section heading, the PDF served whole and "matches the released copy", at desktop and phone
  width with no horizontal scroll; and what the renderer must get right: escaped pipes in table
  cells, no backslash escape printed, the JHEP DOIs linked whole, the versioned old-style arXiv id
  linked, a lazy list continuation kept in its item, and in five papers no escape printed and no
  dead link, the index paper's `cl[L](X)` printed as written.
- **`routing`** — a paper's cite address: opening it, Back and Forward, closing by Escape, ✕ and the
  list; reading another paper and reloading; every loose form a pasted citation takes; focus and the
  keyboard on every path; the Papers button; a close raced by a new citation; the explorer's own
  routes; all the Cite addresses, each opening its own paper; and the history after citations are
  read and closed, with a real page before the site.
- **`review`** — what the reviews of that routing found, kept found: Back closing a paper without
  moving the explorer's camera or a phone's scroll; a paper never stepping back onto an older entry
  for itself; a selection that lands late behind an open paper; a rotation keeping the reading
  position; a reload on a paper closing onto the element behind it; a citation from another page; an
  address changed during the first load; and the explorer's own keys still acting with no dialog open.

The checks name specific papers (Löwdin, Tower, Bracket, Lattice, the index paper, Everything Is
Relative) and elements (Fe, Cu, U III), and pin some of their text, as `--selftest` pins figures: a
change to one of them is a reason to read the failure, not a fault in the site.

## Without the Navigation API

`--nonav` removes `window.navigation`. The page then writes every address by replacing the history
entry, as its explorer routes always have (docs/WEB-INDEX.md): nothing navigates wrongly, but a paper
read from the list is not an entry of its own, and a citation closed inside the page leaves one entry
Back passes through. The checks that need the API are marked and reported **n/a** under `--nonav`,
so the run still fails on anything else.
