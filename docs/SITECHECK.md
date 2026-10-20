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
run stops at once with exit status 2 and says why — the proxy refusing the host, or a certificate the
browser does not trust — rather than reporting a page it never loaded. The session's proxy re-signs
TLS with its own CA, which curl and Node are given; Chromium is told to trust the same keys
(`--ignore-certificate-errors-spki-list`, read from `SSL_CERT_FILE`, `NODE_EXTRA_CA_CERTS` or
`/root/.ccr/ca-bundle.crt`) and nothing else is relaxed. For a commit, a key file the commit does not
hold (an older commit, before a paper) is noted and skipped; a commit without `public/index.html`
stops the run.

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
page reported no error, **1** a check failed or the page reported an error, **2** the run could not
start — an unknown argument or suite, a missing value, `--root` with another target, a commit that
cannot be extracted, files that differ from GitHub's copy, an unreachable live site, a browser that
will not launch, or no check run at all. Every argument is checked: a misspelt flag stops the run
rather than being ignored.

**A page error is anything the page throws or logs as an error**: the site catches a failed draw,
boot or element load and reports it on the console only, so console errors count — except a request
the harness itself turns away from another host (the fonts). Each scenario has three minutes; one
that stops responding is reported as failed and the run goes on.

## What it checks — 31 scenarios, 142 checks

Each scenario runs in fresh browser contexts, closed when it ends, so one cannot leak into the next;
a scenario that throws is reported as a failure and the run goes on.

- **`papers`** — the Papers dialog has a card for every held paper, Everything Is Relative last;
  its reader shows the front matter's title block (title, standfirst, byline, no YAML), contents for
  every section heading and a contents link that scrolls to its heading, the PDF served whole and
  "matches the released copy", at desktop and phone width with no horizontal scroll; and what the
  renderer must get right: escaped pipes in table cells, no backslash escape printed (`R^{tr}_{tr}`
  as written), every arXiv and DOI identifier the paper cites linked — the JHEP DOIs whole, the
  versioned old-style arXiv id as printed at both its sites — a lazy list continuation kept in its
  item, and in five papers no escape printed and no dead link, the index paper's `cl[L](X)` printed
  as written.
- **`routing`** — a paper's cite address: opening it, Back and Forward, closing by Escape, ✕ and the
  list; reading another paper and reloading; every loose form a pasted citation takes; focus and the
  keyboard on every path, no key acting behind the dialog even with focus fallen to the page; the
  Papers button; a close raced by a new citation; the explorer's own
  routes; all the Cite addresses, each opening its own paper; and the history after citations are
  read and closed, with a real page before the site.
- **`review`** — what the reviews of that routing found, kept found: Back closing a paper without
  moving the explorer's camera or a phone's scroll; a paper never stepping back onto an older entry
  for itself; a selection that lands late behind an open paper, with the element load really held
  back past the Papers press; a rotation keeping the reading position; a reload on a paper closing
  onto the element behind it; a citation from another page; an address changed while a reload is
  still restoring the element behind a paper, which must open no paper and leave the explorer where
  the reader put it; and the explorer's own keys still acting, and writing the address, with no
  dialog open.

- **`solvers`** — the solver suite runs, and answers what a reader asks of it: every mode loads and
  each of the eleven selftests passes, in two scenarios (the record's own modes, then the chemistry
  and gravity modes); on a phone, the builder gives water its molar mass (18.015 g/mol) and its most
  abundant isotopologue (A = 18, 18.010565 u), glucose 180.156 g/mol, and sends "electron" to the
  gravity mode; the gravity mode gives iron a χ from its ground term with the bound decided at
  D = 4 and the χ ratio against ¹H, gives ¹²C exactly 12 u at the ground (not the banked excited
  level), reads "proton" as the baryon p, refuses a photon's χ as undefined rather than infinite,
  and lists the three pions rather than choosing one; and the search box offers a particle's plate
  and its gravity by its common name, the gravity suggestion opening the mode on it. These are the
  readings that were refusals or wrong before 2026-10-17 (docs/WEB-INDEX.md, the eleventh mode).

- **`caveats`** — the caveats as reviewed on 2026-10-17 (docs/CAVEATS.md). The root plate lists
  eleven, each with its state, and every repaired one prints what it read before. The Z > 108 caveat
  names NIST's neutral ground levels and no longer says "because measurement does". On the plates:
  - Na I s gives the csv's B as the range of the series' defects, not a bound, and its series limit
    with its unit, cm⁻¹, inside the equation's domain;
  - Fe IV s is outside the domain, with the reason;
  - Rf's ground level is NIST's lone level, its ionisation energy ab initio;
  - Z = 119's B is named a bare 0, not a bound;
  - n₀ is `RECOVERED`;
  - Fe's plate lists its Λ cells as the record builds them (14, five composable within iron), with
    the ionisation ladder labelled a reconstruction;
  - H, with one listed subshell, has no cell.

**Each of those was proved to fail on the bug it guards against.** The review that hardened the
tool put ten known bugs back into copies of the site — the `#paper=` branch removed, `paperAddress`
replace-only, the dialog key guard removed, `focusPapers` a no-op, `select()` writing the address
unconditionally, the rotation observer removed, `entryBehind` returning nothing, the first-load
guard removed, a dead link in a paper, the dialog left open when the address moves on — plus a
canvas that throws on every draw, and served each with `--root`: every one now fails the run.

**The `solvers` suite was proved the same way, against the site it replaced.** Run on the deployed `main` of
2026-10-17 (`--target commit --suite solvers`), before the solver fixes, it fails all ten of its reader checks
and passes the twelve selftest checks. Those selftests had pinned the old behaviour, a mass refused without
isotopes and an excited level's energy included, which is how a suite that answered nothing useful reported
itself healthy. The reader checks are there so that cannot happen again.

The checks name specific papers (Löwdin, Tower, Bracket, Lattice, the index paper, Everything Is
Relative) and elements (Fe, Cu, U III), and pin some of their text, as `--selftest` pins figures: a
change to one of them is a reason to read the failure, not a fault in the site.

## Without the Navigation API

`--nonav` removes `window.navigation`. The page then writes every address by replacing the history
entry, as its explorer routes always have (docs/WEB-INDEX.md): nothing navigates wrongly, but a paper
read from the list is not an entry of its own, and a citation closed inside the page leaves one entry
Back passes through. The checks that need the API are marked and reported **n/a** under `--nonav`,
so the run still fails on anything else.
