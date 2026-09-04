# `tools/coverage.py` — what the corpus names, against what the repo holds

Consolidation answered *where is everything*. This answers the harder one:
**for every artefact the books refer to by name, is it actually here?**

`python3 tools/coverage.py` walks the two live bundles, collects every filename-shaped token,
resolves each against the whole repo, and writes `COVERAGE.tsv`. `--selftest` asserts the corpus's
own recorded numbers.

## The census

| family | named | held | via alias | ABSENT |
| --- | ---: | ---: | ---: | ---: |
| instrument (`.py`) | 338 | 245 | 0 | 93 |
| data (`.tsv`/`.csv`/`.json`) | 218 | 137 | 0 | 81 |
| other | 150 | 75 | 0 | 75 |
| `READ-*` | 119 | 114 | 0 | 5 |
| figure (`.png`) | 117 | 75 | 15 | 27 |
| `HANDOFF-*` | 58 | 54 | 0 | 4 |
| `DEF-*` | 3 | 0 | 0 | 3 |
| `REGISTER-*`, `RULING-*` | 2 | 2 | 0 | 0 |
| **Total** | **1,005** | **702** | **15** | **288** |

**These figures moved when `extracted/` and `recovered/` landed, and by a lot.** The census above
previously read 559 held against 431 ABSENT; consolidation and recovery raised `held` by 143 and cut
`ABSENT` by 143 without a single new fetch — `READ-*` from 48 held to **114**, `HANDOFF-*` from 12 to
**54**. Anything quoting the old figures is quoting a repository that no longer exists.

## Resolved against the chats (`--chats`)

With the sharded export in `drive/chats`, `--chats` re-resolves everything the repo does not hold
against 352 conversations, and the census becomes a **recovery index**: `held_as` names the
conversation to open.

| family | named | held | alias | in-body | in-chat | ABSENT |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| instrument | 338 | 245 | 0 | 0 | 93 | 0 |
| data | 218 | 137 | 0 | 0 | 81 | 0 |
| other | 150 | 75 | 0 | 8 | 63 | 4 |
| `READ-*` | 119 | 114 | 0 | 3 | 2 | 0 |
| figure | 117 | 75 | 15 | 0 | 27 | 0 |
| `HANDOFF-*` | 58 | 54 | 0 | 0 | 4 | 0 |
| `DEF-*` | 3 | 0 | 0 | 0 | 3 | 0 |
| **Total** | **1,005** | **702** | **15** | **11** | **273** | **4** |

**`--chats` is not optional if you want these numbers.** A plain `python3 tools/coverage.py`
overwrites `COVERAGE.tsv` with the 288-ABSENT census and drops every `IN-CHAT` resolution — the file
in the repository is the `--chats` run, and it reproduces byte-for-byte only with the flag.

`IN-CHAT-BODY` means a shard carries the document's own title line, so the body is recoverable from
that conversation. `IN-CHAT` means only that the name is spoken there — possibly a passing mention.
The distinction is deliberate and the weaker status is never reported as the stronger. It used to
carry most of the handoff family — 41 of 46 by body — and now carries almost none of it: **54 of the
58 handoffs are held outright**, and the remaining 4 are mentions.

The heading test is not line-anchored, because inside a shard the newlines are JSON-escaped `\n`
literals and a `^`-anchored pattern matches nothing at all. Headings only evidence a body for
Markdown, so `IN-CHAT-BODY` is claimed for `.md` artefacts only.

**Four names remain ABSENT, and none is a missing document:** `HANDOFF96.md`, `HANDOFF98.md`,
`5e655873-HANDOFF100.md` and `a4dd0e54-HANDOFF99.md` — unhyphenated and uuid-prefixed spellings of
handoffs the repo already holds as `HANDOFF-96.md`, `HANDOFF-98.md`, `HANDOFF-99.md` and
`HANDOFF-100.md`. The census is literal and does not guess at such mappings, which is why it reports
them rather than silently resolving them.

## What ABSENT does and does not mean

**ABSENT means "not reachable from any source in this repo". It is not a claim that anything was
lost.** A name appearing in prose is not proof a file ever existed, and much of what the work
produced was never exported from the chat that made it. The same refusal discipline the audit
instruments follow applies here: an `ABSENT` may not be quoted as a finding of loss.

Every count is also a **floor, not a total**, because extraction is deliberately literal. The
bundles name 58 handoffs in filename shape but refer to **88 distinct `HANDOFF-<n>` by bare
number** — of which **62 are held and 26 are not** (was 20 held and 68 not, before recovery):
2, 33, 54, 55, 56, 63, 65, 66, 68–71, 81, 82, 85–87, 89–95, 103, 104. Counting prose references
still raises every ABSENT figure, but by far less than it once did.

## Figures are in better shape than the raw count suggests

The books embed figures under names that a rename produced. `CORPUS/FIGURE_ASSETS.md` maps all
**33 main-volume figures** from their pre-rename source (`fig00.png`, `fig-sections.png`, …) to
their current name (`figure-6.1.png`, …). **All 33 source images are held.** Fifteen of the renamed
copies were never written, so they resolve as `HELD-VIA-ALIAS` — the image is present, only the new
filename is not.

Adding the 12 compendia figures and the 15 already in project knowledge, the figure set the corpus
describes is complete at source level: **78 distinct figures**, up from the 7 that were loose in
`drive/` before consolidation.

Two genuine figure gaps remain, and they are specific:

* **The papers' `f<N>_<M>.png` set — 25 files, none present.** Referenced from the papers section of
  the compendia bundle. They are in no archive, no project export and no manifest row.
* **`figure-D.1-prior-32-elements.png`.** `FIGURE_ASSETS.md` says the archived 32-element/16-fibre
  plot was kept when D.1 was re-rendered at register 1742. That kept copy is not in any source here.

(A third, `file.png`, is a prose artefact of literal extraction, not a real reference.)

## The books themselves are complete

None of the above touches the store of record. `method/verify.py` passes: **343 members, 0
mismatched**, and both live bundles recover byte-exact from their spliced members. What is absent is
*working* material — handoffs, reading slips, per-chat instruments — not the corpus.

## Where the absent material would be

Almost all of it in the two 388 MB `conversations.json` chat exports, which are still listed in
`drive/PENDING.tsv`: above GitHub's 100 MB per-file block and far above the Drive connector's
~6 MiB payload ceiling. That store is the only remaining place a handoff for chat 40, or a
`READ-ch12*` slip, could still be recovered from. `tools/shard_conversations.py` is the route in.

Until it lands, `COVERAGE.tsv` is the standing list of what to look for.
