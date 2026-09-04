# `tools/coverage.py` — what the corpus names, against what the repo holds

Consolidation answered *where is everything*. This answers the harder one:
**for every artefact the books refer to by name, is it actually here?**

`python3 tools/coverage.py` walks the two live bundles, collects every filename-shaped token,
resolves each against the whole repo, and writes `COVERAGE.tsv`. `--selftest` asserts the corpus's
own recorded numbers.

## The census

| family | named | held | via alias | ABSENT |
| --- | ---: | ---: | ---: | ---: |
| instrument (`.py`) | 338 | 213 | 0 | 125 |
| data (`.tsv`/`.csv`/`.json`) | 218 | 136 | 0 | 82 |
| other | 150 | 73 | 0 | 77 |
| `READ-*` | 119 | 48 | 0 | 71 |
| figure (`.png`) | 117 | 75 | 15 | 27 |
| `HANDOFF-*` | 58 | 12 | 0 | 46 |
| `DEF-*` | 3 | 0 | 0 | 3 |
| `REGISTER-*`, `RULING-*` | 2 | 2 | 0 | 0 |
| **Total** | **1,005** | **559** | **15** | **431** |

## Resolved against the chats (`--chats`)

With the sharded export in `drive/chats`, `--chats` re-resolves everything the repo does not hold
against 352 conversations, and the census becomes a **recovery index**: `held_as` names the
conversation to open.

| family | named | held | alias | in-body | in-chat | ABSENT |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| instrument | 338 | 213 | 0 | 0 | 125 | 0 |
| data | 218 | 136 | 0 | 0 | 82 | 0 |
| other | 150 | 73 | 0 | 10 | 63 | 4 |
| `READ-*` | 119 | 48 | 0 | 44 | 27 | 0 |
| figure | 117 | 75 | 15 | 0 | 27 | 0 |
| `HANDOFF-*` | 58 | 12 | 0 | 41 | 5 | 0 |
| `DEF-*` | 3 | 0 | 0 | 0 | 3 | 0 |
| **Total** | **1,005** | **559** | **15** | **95** | **332** | **4** |

`IN-CHAT-BODY` means a shard carries the document's own title line, so the body is recoverable from
that conversation. `IN-CHAT` means only that the name is spoken there — possibly a passing mention.
The distinction is deliberate and the weaker status is never reported as the stronger: **41 of the
46 handoffs have a body; the other 5 are mentions.**

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
number** — of which 20 are held and **68 are not**. Counting prose references would raise every
ABSENT figure.

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
