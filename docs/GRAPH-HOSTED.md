# The hosted Graphify index, and how it differs from `graphify-out/`

`https://api.graphify.com/mcp` serves a **second graph of this repository**, built by Graphify's
hosted pipeline and queried through the `Graphify` MCP server that `.mcp.json` seats. It is not the
graph in `graphify-out/`, and the two disagree by about ten thousand nodes. This file records what
was measured, and — in §6 — what an earlier revision of this file got wrong.

**Neither graph is a census of the tree.** That was already the standing caution for
`graphify-out/` (`CLAUDE.md`, `docs/GRAPH-FINDINGS.md`); it now applies twice over. A miss in
either is not evidence a file is absent — ask `COVERAGE.tsv`, `extracted/LEDGER.tsv`,
`recovered/LEDGER.tsv` or `HANDOFF-GAP.tsv`.

**Every hosted figure below is stamped with the build that produced it.** The hosted index rebuilds
without notice (§2), so a figure without a `buildId` beside it is not re-verifiable.

## The two graphs

Hosted figures are from build `f4ba753a` at commit `c5ff5ca8`, read 2026-09-06.

| | `graphify-out/graph.json` | hosted, build `f4ba753a` |
|---|---|---|
| nodes | 26,364 | 16,216 |
| edges | 36,150 | 17,690 |
| communities | 2,929 | 3,637 |
| hyperedges | 390 | not exposed by any MCP tool |
| nodes per community | 9.0 | 4.5 |
| commit | `1c33255e` | `c5ff5ca8` |
| embedding model | not recorded in `graph.json` | `minishlab/potion-base-8M` |
| pipeline | `/graphify .`, 22 subagents, 3.45M tokens | `production-v1` |

## 1. Scope is the same 4,090 files

The hosted pipeline builds from the git checkout — 5,627 tracked files — but its indexed set
respects the same exclusions `.graphifyignore` states:

- `graphify_rank_files` asked for "the BUILD snapshots of The Method 1.6 compendia, papers and
  audits" returns **exactly one file**, `The_Method_1_6_BUILD174_compendia_papers_audits.md`. That
  is precisely what `.graphifyignore` keeps (`The_Method_1_6_BUILD*` excluded,
  `!The_Method_1_6_BUILD174_*` re-included) out of the **146** BUILD Markdown files git tracks.
- `graphify_file_neighbors` on `drive/…/The_Method_1_6_BUILD9_compendia_papers_audits.md` and on
  `drive/chats/2026-06/0da8fd78-….json` both return `no file matching`. Git tracks 354 files under
  `drive/chats/`; the local manifest holds **0**.

The rank-files result is what carries this, because a `no file matching` on its own is weak — see
§5. **The node gap is not scope.**

## 2. Both graphs are stale, in different ways, and the hosted one moves under you

`graph.json` carries `built_at_commit: 1c33255ea2fbd41347d3ba16aef96361a0c9ff70` — the 2026-09-04
rebuild's commit. **`main` is 81 commits ahead of it.** That is a fixed snapshot: it will not move
until someone runs `/graphify .`.

The hosted index moves on its own, and **not to HEAD**. Within a single session on 2026-09-06 it
was observed at two builds:

| read at | buildId | commitSha | nodes | edges | communities |
|---|---|---|---|---:|---:|
| first | `93b5e258` | `f5e46b4a` | 15,901 | 17,626 | 3,439 |
| ~20 min later | `f4ba753a` | `c5ff5ca8` | 16,216 | 17,690 | 3,637 |

`c5ff5ca8` is PR #13's merge — an **ancestor** of `main`, five commits behind it at the time of
reading. So the hosted index tracks the default branch with a rebuild lag, and **"the hosted index
is at HEAD" is false**; it was true only by coincidence at the first reading. Stamp the `buildId`
on anything you quote from it.

## 3. The AST layers agree, and where they differ the hosted one extracts nested functions

This is the one layer both graphs can be compared on like-for-like, by counting **callables and
classes** on each side: `_callable` in `graph.json`, the `symbols` list from
`graphify_file_neighbors` (at a `limit` high enough not to truncate).

| file | local `_callable` | hosted `symbols` | hosted extras |
|---|---:|---:|---|
| `tools/cypher.py` | 23 | **25** | `cross()` L276 in `_hull2`, `block()` L543 in `_periodic` |
| `tools/populate.py` | 31 | **33** | `aufbau()` L781 in `check_B`, `check()` L848 in `selftest` |
| `recovered/hartman_check.py` | 2 | **4** | `up()` L9, `dn()` L12, both in `close` |
| `tools/coverage.py` | 9 | **10** | `check()` L210 in `selftest` |
| `recovered/frachf.py` | 4 | 4 | — |
| `recovered/level4.py` | 6 | 6 | — |
| `method/verify.py` | 1 | 1 | — |
| `recovered/frac1.py` | 1 | 1 | — |
| `recovered/sq.py` | 0 | 0 | — |
| `recovered/t7a_sic_all.py` | 0 | 0 | — |

**Every difference is a nested `def`.** Where a file has no inner function the two agree exactly;
where it has one, the hosted pass emits it and the local pass does not. Whole-graph, labels
containing `()` number **7,405 locally against 7,942 hosted** (+7.3 %), which is the same effect at
corpus scale.

## 4. The document layers cannot be compared with the tools available

**This is UNDECIDED, and it is the interesting half of the gap.** Local semantic nodes are counted
exactly: **15,345**, `_origin != 'ast'`. The hosted side cannot be counted, because no MCP tool
enumerates its nodes by kind, and the obvious proxy is a trap — see §6.

What can be established is a **bound**. Hosted labels containing `()` number 7,942 and every one
sampled is `file_type: code`, so hosted code nodes ≥ 7,942 and therefore hosted **non-code nodes
≤ 8,274** of the 16,216. Against local's 15,345 semantic nodes, the hosted document layer is at
most **54 %** the size — smaller, certainly, but nothing like the order of magnitude an earlier
revision of this file claimed.

The two document layers also differ in *kind*, and that much is directly observable. Local document
labels are propositions:

    "Absence is measured against reach, never reported as loss"

Hosted ones are shorter and more citational — `W-137 chat 98`, `Chapter 14 Sections 14.5.8 to
14.6.6`, `HANDOFF-6`. The whole-graph label census registers it: labels containing the letter `e`
are **21,103 of 26,364 locally (80.0 %)** against **10,486 of 16,216 hosted (64.7 %)**, because a
long English sentence almost always contains an `e` and a short citation often does not. That
comparison is like-for-like — a substring count over every node label on each side.

## 5. Two traps in the hosted MCP surface

Both of these produced published errors. They are recorded here so the next reader does not repeat
them.

**`n_symbols` is not the number of symbols.** `graphify_file_neighbors('tools/cypher.py')` reports
`n_symbols: 38` and lists **25** symbols at `limit=100`. It is not a truncation and not an
off-by-one; it counts something the tool does not return. Local `graph.json` has 36 nodes for that
file. **Do not compare `n_symbols` to anything** — count the `symbols` array.

**`symbols` lists code symbols only.** `graphify_file_neighbors('recovered/W-137.md')` returns
`symbols: []`, yet `graphify_find('W-137')` returns node `w_137_chat_98`, `file_type: document`,
`src: recovered/W-137.md` — a node in that file the neighbors call did not list. An empty `symbols`
on a document means "no code symbols here", **never** "no nodes here". `docs/GRAPH-FINDINGS.md`
likewise returned `no file matching` on build `93b5e258` and `n_symbols: 6` on `f4ba753a`.

## 6. What an earlier revision of this file claimed, and why it was wrong

Commit `02328ab` (merged to `main` as PR #15) stated a per-file table comparing hosted `n_symbols`
against local total node counts, and concluded from it that the hosted document layer was "roughly
an order of magnitude thinner", citing `CLAUDE.md` at 2 nodes against 14 and `docs/GRAPH-FINDINGS.md`
at **0 against 14**. It also stated that the hosted index "is at HEAD".

Three of those are withdrawn:

- **The per-file table was not like-for-like.** It compared `n_symbols` — a number that counts
  neither nodes nor listed symbols (§5) — against a local node total that includes module and
  docstring nodes. §3 replaces it with callables against listed symbols.
- **"The document layer is an order of magnitude thinner" is withdrawn.** It rested on `.md` files
  reporting 0–2 symbols, which is what `symbols` does for every document regardless of how many
  nodes it holds (§5). The measured bound is ≤ 54 %, not ≤ 10 % (§4).
- **"`docs/GRAPH-FINDINGS.md` is in no hosted node" is withdrawn.** It has nodes; the first build
  did not match the path and the second reports `n_symbols: 6` with an empty `symbols` list.
- **"The hosted index is at HEAD" is withdrawn.** It tracks the default branch with a lag and was
  observed five commits behind (§2).

What survives, on better evidence than it was first given: the scope finding (§1), the AST
agreement and the nested-`def` mechanism (§3, which the first revision asserted from the wrong
numbers but got the direction of), the label-shape census (§4), and the local snapshot's staleness
(§2, now 81 commits rather than 70).

## What follows for a reader

- **Quote the graph you queried, and stamp the build.** 26,364 / 36,150 / 2,929 is `graphify-out/`
  at `1c33255e`. 16,216 / 17,690 / 3,637 is hosted build `f4ba753a`. They are not versions of one
  number, and the hosted one will have moved.
- **For code — symbols, callers, imports, blast radius — prefer the hosted index.** It is nearer
  the default branch than the local snapshot, it resolves nested functions, and
  `graphify_callers` / `graphify_trace` / `graphify_impact` answer directly.
- **For what a document argues, prefer `graphify-out/`** — its labels are propositions where the
  hosted layer's are citations — while remembering it stands 81 commits back.
- **Neither is a census.** Unchanged.

## Re-verifying these numbers

The hosted figures need the `Graphify` MCP server and cannot be checked offline, so
**`tools/docfigures.py` does not pin them** — it pins only figures a local instrument can
re-measure. The local side:

    python3 -c "
    import json
    g=json.load(open('graphify-out/graph.json')); n=g['nodes']
    print(len(n), len(g['links']), len(g['hyperedges']), g['built_at_commit'])
    print('callable', sum(1 for x in n if x.get('_callable')))
    print('semantic', sum(1 for x in n if x.get('_origin')!='ast'))
    print('labels ()', sum(1 for x in n if '()' in (x.get('label') or '')))
    "
    git log --oneline 1c33255..origin/main | wc -l

The hosted side, through the MCP server — read `buildId` and `commitSha` off every response:

    graph_stats(repository_id='lach-matt/Claude-Method-Works')
    graphify_file_neighbors(file='tools/cypher.py', limit=100)   # count symbols, ignore n_symbols
    graphify_find(term='()', limit=1)                            # read n
    graphify_find(term='W-137', limit=5)                         # document nodes are here, not in symbols
    graphify_rank_files(question='Which files are the BUILD snapshots …')
