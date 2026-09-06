# The hosted Graphify index, and how it differs from `graphify-out/`

`https://api.graphify.com/mcp` serves a **second graph of this repository**, built by Graphify's
hosted pipeline and queried through the `Graphify` MCP server. It is not the graph in
`graphify-out/`, and the two disagree by 10,463 nodes. This file records what was measured on
2026-09-06 against build `93b5e258`, so that neither figure is quoted as the other's.

**Neither graph is a census of the tree.** That was already the standing caution for
`graphify-out/` (`CLAUDE.md`, `docs/GRAPH-FINDINGS.md`); it now applies twice over. A miss in
either is not evidence a file is absent — ask `COVERAGE.tsv`, `extracted/LEDGER.tsv`,
`recovered/LEDGER.tsv` or `HANDOFF-GAP.tsv`.

## The two graphs

| | `graphify-out/graph.json` | hosted (`api.graphify.com`) |
|---|---|---|
| nodes | 26,364 | 15,901 |
| edges | 36,150 | 17,626 |
| communities | 2,929 | 3,439 |
| hyperedges | 390 | not exposed by any MCP tool |
| nodes per community | 9.0 | 4.6 |
| commit | `1c33255e` | `f5e46b4a` |
| embedding model | not recorded in `graph.json` | `minishlab/potion-base-8M` |
| pipeline | `/graphify .`, 22 subagents, 3.45M tokens | `production-v1` |
| repository id | — | `78814414-4626-4503-9a66-3bb048e1731f` |
| workspace | — | `ml-research` |

The hosted graph has **more communities over fewer nodes**. That inversion is the shape of the
difference, not an anomaly on top of it: see §3.

## 1. The local snapshot is the stale one, by 70 commits

`graph.json` carries `built_at_commit: 1c33255ea2fbd41347d3ba16aef96361a0c9ff70` — the
2026-09-04 rebuild's commit. **HEAD is 70 commits ahead of it.** The hosted build reports
`commitSha f5e46b4a`, which *is* HEAD.

This corrects an intuition, not a claim: `CLAUDE.md` already says the local graph is a snapshot
and that six documents describe an earlier state of themselves in it. What is new is the size of
the lag and its direction — the hosted index, not the local one, is the current-commit graph.

Re-verify:

    python3 -c "import json;print(json.load(open('graphify-out/graph.json'))['built_at_commit'])"
    git log --oneline 1c33255..HEAD | wc -l

## 2. Both honour `.graphifyignore`. The scope is the same 4,090 files

This was the first hypothesis for the gap and it is **wrong**. The hosted pipeline builds from the
git checkout — 5,627 tracked files — but its indexed set respects the same exclusions:

- `graphify_rank_files` asked for "the BUILD snapshots of The Method 1.6 compendia, papers and
  audits" returns **exactly one file**, `The_Method_1_6_BUILD174_compendia_papers_audits.md`.
  That is precisely what `.graphifyignore` keeps (`The_Method_1_6_BUILD*` excluded,
  `!The_Method_1_6_BUILD174_*` re-included) out of the **146** BUILD Markdown files git tracks.
- `graphify_file_neighbors` on `drive/The Method Materials/The_Method_1_6_BUILD9_compendia_papers_audits.md`
  and on `drive/chats/2026-06/0da8fd78-….json` both return `no file matching`. Git tracks 354
  files under `drive/chats/`; the local manifest holds **0**.

A `no file matching` on its own would be weak — it means "no node is sourced from this path", not
"this path was never scanned" (§4 has a file that was in scope and still returns it). The
rank-files result is what carries the finding: a positive selection of the one BUILD file the
ignore rules re-include.

So the 10,463-node gap is **not scope**. Both graphs cover the same 4,090 files.

## 3. The AST layer agrees. The document layer does not

Per-file node counts, local against hosted (`n_symbols`):

| file | local | hosted |
|---|---:|---:|
| `tools/populate.py` | 49 | **51** |
| `tools/cypher.py` | 36 | **38** |
| `tools/coverage.py` | 15 | **16** |
| `method/verify.py` | 2 | 2 |
| `recovered/frachf.py` | 6 | 6 |
| `CLAUDE.md` | 14 | **2** |
| `docs/GRAPH-FINDINGS.md` | 14 | **0** |
| `recovered/HANDOFF-5.md` | 12 | **0** |
| `docs/PROSE-ONLY.md` | 11 | **1** |
| `docs/RECOVER.md` | 10 | **1** |
| `docs/DRIVE-SYNC.md` | 10 | **2** |
| `docs/COVERAGE.md` | 9 | **1** |
| `README.md` | 8 | **2** |
| `recovered/HANDOFF-9.md` | 7 | **1** |

Code files agree within one or two nodes, and where they differ the **hosted graph is the richer
one**. A whole-graph label census says the same: labels containing `()` — the callable form —
number **7,405 locally against 7,919 hosted**, +6.9 % for the hosted AST pass.

Documents run the other way by roughly an order of magnitude, and the labels are a different kind
of thing. Local document nodes are prose propositions:

    "Absence is measured against reach, never reported as loss"

Hosted document nodes are identifiers and paths — `tools/recover.py`, `drive`, `HANDOFF 9`. The
census shows it: labels containing the letter `e` are **21,103 of 26,364 locally (80 %)** but only
**10,142 of 15,901 hosted (64 %)**, because a long English sentence almost always contains an `e`
and a short identifier often does not.

**The layer split is INFERRED, not measured.** No MCP tool enumerates hosted nodes by origin, so
the attribution of the gap to the document layer rests on the fourteen per-file probes and the two
label censuses above, not on a count. Local *is* measured: `_origin` is 11,019 `ast` against 15,345
semantic.

## 4. `docs/GRAPH-FINDINGS.md` is in no hosted node, and that is not a currency effect

The file exists at `1c33255` and at `f5e46b4`. The local graph gives it 14 nodes. The hosted graph,
built at HEAD, returns `no file matching`. Same for `recovered/HANDOFF-5.md` — 12 nodes locally,
none hosted, while `recovered/HANDOFF-9.md` *is* present hosted with 1.

So the hosted document layer misses whole files, not just detail within them. Recorded, not
repaired: it is a property of the hosted pipeline, and there is nothing in this repository to fix.

## What follows for a reader

- **Quote the graph you queried.** 26,364 / 36,150 / 2,929 is `graphify-out/`. 15,901 / 17,626 /
  3,439 is the hosted index. They are not versions of one number.
- **For code — symbols, callers, imports, blast radius — prefer the hosted index.** It is at HEAD,
  it is marginally richer per file, and `graphify_callers` / `graphify_trace` / `graphify_impact`
  answer directly.
- **For the corpus's propositions — findings, rulings, what a document argues — the hosted index is
  the wrong instrument.** Its document layer carries filenames where the local one carries claims.
  Use `graphify-out/graph.json`, and remember it stands 70 commits back.
- **Neither is a census.** Unchanged.

## Re-verifying these numbers

The hosted figures need the `Graphify` MCP server and cannot be checked offline, so
**`tools/docfigures.py` does not pin them** — it pins only figures a local instrument can
re-measure. To re-run this comparison:

    # local side
    python3 -c "
    import json,collections
    g=json.load(open('graphify-out/graph.json')); n=g['nodes']
    print(len(n), len(g['links']), len(g['hyperedges']), g['built_at_commit'])
    print(collections.Counter(x.get('_origin') for x in n))
    f=collections.Counter(x.get('source_file') for x in n)
    for p in ['CLAUDE.md','tools/cypher.py','docs/GRAPH-FINDINGS.md']: print(p, f.get(p,0))
    "

    # hosted side, through the MCP server
    graph_stats(repository_id='lach-matt/Claude-Method-Works')
    graphify_file_neighbors(file='CLAUDE.md')
    graphify_find(term='()', limit=1)          # read n, not the matches
    graphify_rank_files(question='Which files are the BUILD snapshots …')

One quirk to expect: `graphify_file_neighbors` with `limit=1` can return an empty `symbols` array
while `n_symbols` reports the true count. Read `n_symbols`.
