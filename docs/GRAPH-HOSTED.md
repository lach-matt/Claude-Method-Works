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

Hosted figures below are the last row of `HOSTED-GRAPH.tsv`, which
`tools/hostedgraph.py` writes and `tools/docfigures.py` pins this document against (§7):

    build            f4fbeee4-d7cd-4b67-9b01-11f5046c8bcc
    commit           3f65d1715b6ffd15e47c9d20fe4ac7a44c91876a
    nodes            16201
    edges            17673
    communities      3725
    labels_paren     7971

| | `graphify-out/graph.json` | hosted, build `f4fbeee4` |
|---|---|---|
| nodes | 26,364 | 16,201 |
| edges | 36,150 | 17,673 |
| communities | 2,929 | 3,725 |
| hyperedges | 390 | not exposed by any MCP tool |
| nodes per community | 9.0 | 4.3 |
| commit | `1c33255e` | `3f65d17` |
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
rebuild's commit. **`main` is 83 commits ahead of it.** That is a fixed snapshot: it will not move
until someone runs `/graphify .`.

The hosted index moves on its own, and **not to HEAD**. Within a single session on 2026-09-06 it
was observed at two builds:

| read at | buildId | commitSha | nodes | edges | communities |
|---|---|---|---|---:|---:|
| 16:04 | `93b5e258` | `f5e46b4a` | 15,901 | 17,626 | 3,439 |
| 16:19 | `f4ba753a` | `c5ff5ca8` | 16,216 | 17,690 | 3,637 |
| 16:29 | `f4fbeee4` | `3f65d17` | 16,201 | 17,673 | 3,725 |

All three rows are in `HOSTED-GRAPH.tsv`. Note the third: **nodes fell while communities rose** — a
rebuild is not monotone, so "the newer index is the bigger one" is not safe either.

`c5ff5ca8` is PR #13's merge — an **ancestor** of `main`, five commits behind it at the time of
reading. So the hosted index tracks the default branch with a rebuild lag, and **"the hosted index
is at HEAD" is false**; it was true only by coincidence at the first and third readings. Stamp the
`buildId` on anything you quote from it — §7 is what makes that stamp checkable.

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
containing `()` number **7,405 locally against 7,971 hosted** (+7.6 %), which is the same effect at
corpus scale.

## 4. The document layers cannot be compared with the tools available

**This is UNDECIDED, and it is the interesting half of the gap.** Local semantic nodes are counted
exactly: **15,345**, `_origin != 'ast'`. The hosted side cannot be counted, because no MCP tool
enumerates its nodes by kind, and the obvious proxy is a trap — see §6.

What can be established is a **bound**. Hosted labels containing `()` number 7,971 and every one
sampled is `file_type: code`, so hosted code nodes ≥ 7,971 and therefore hosted **non-code nodes
≤ 8,230** of the 16,201. Against local's 15,345 semantic nodes, the hosted document layer is at
most **53.6 %** the size — smaller, certainly, but nothing like the order of magnitude an earlier
revision of this file claimed.

The two document layers also differ in *kind*, and that much is directly observable. Local document
labels are propositions:

    "Absence is measured against reach, never reported as loss"

Hosted ones are shorter and more citational — `W-137 chat 98`, `Chapter 14 Sections 14.5.8 to
14.6.6`, `HANDOFF-6`. The whole-graph label census registers it: labels containing the letter `e`
are **21,103 of 26,364 locally (80.0 %)** against **10,463 of 16,201 hosted (64.6 %)**, because a
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
(§2, now 83 commits rather than 70).

## 7. The record, and what pins this document to it

Every other figure in this repository can be re-counted by a stdlib program, and
`tools/docfigures.py` re-counts them. The hosted figures could not be: reading them needs the MCP
server, so nothing could catch them drifting. They were the one unguarded class of number here.

`HOSTED-GRAPH.tsv` closes that. It is the record — one row per measurement, append-only, written by
`tools/hostedgraph.py --record` from figures an agent read off the MCP server. The tool never calls
the service (a stdlib script cannot, and an HTTP client here would make a checked figure depend on
an unchecked network); it writes the numbers down, does the arithmetic, and refuses a partial
measurement rather than storing half a row.

`docfigures.py` then pins **this document against that record**, and the direction matters:

> Pinning the prose against the *live* service would go STALE every time the service rebuilt —
> three times in the session that produced this file — and a check that cries wolf is a check
> nobody reads. Re-recording is a deliberate act. Forgetting to update the prose afterwards is the
> real error, and that is the one caught.

So a `STALE` hosted row means **the record has moved and this document has not** — re-read §2's
stamped block and correct it. It does *not* mean the hosted index has rebuilt; it rebuilds
constantly, and the record stays true about the build it names.

    python3 tools/hostedgraph.py            # the last recorded measurement, and the bound
    python3 tools/hostedgraph.py --age      # how old the record is (information, not a failure)
    python3 tools/hostedgraph.py --selftest # the arithmetic and the refusals

To record a fresh measurement, read `graph_stats` and two `graphify_find` censuses off the MCP
server and hand them over:

    echo '{"build_id":"…","commit_sha":"…","pipeline":"production-v1",
           "model":"minishlab/potion-base-8M","nodes":0,"edges":0,"communities":0,
           "labels_paren":0,"labels_e":0,"labels_e_code":0}' \
      | python3 tools/hostedgraph.py --record --json -

## What follows for a reader

- **Quote the graph you queried, and stamp the build.** 26,364 / 36,150 / 2,929 is `graphify-out/`
  at `1c33255e`. 16,201 / 17,673 / 3,725 is hosted build `f4fbeee4`. They are not versions of one
  number, and the hosted one will have moved — `HOSTED-GRAPH.tsv` holds the last one recorded.
- **For code — symbols, callers, imports, blast radius — prefer the hosted index.** It is nearer
  the default branch than the local snapshot, it resolves nested functions, and
  `graphify_callers` / `graphify_trace` / `graphify_impact` answer directly.
- **For what a document argues, prefer `graphify-out/`** — its labels are propositions where the
  hosted layer's are citations — while remembering it stands 83 commits back.
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
