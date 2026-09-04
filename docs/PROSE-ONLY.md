# PROSE-ONLY — what the chat history holds that the repository does not

**`PROSE-ONLY.tsv` is the standing list: 1,101 statements that exist only in the conversation
transcripts and have no artefact, register row, docket entry or file anywhere else in this
repository.** This document explains how that list was measured, what it means, and — importantly —
what it does *not* mean.

Measured 2026-09-04 over the whole of `drive/chats/` (352 conversations, 11,879 messages).
**Nothing here has been repaired.** The chat-67 full hold governs this file exactly as it governs a
section read: a finding is recorded, never repaired.

## What "prose-only" means here, precisely

A row in `PROSE-ONLY.tsv` is a statement that:

1. appears in the `text` of a chat message — not in a code block, not in a heredoc, not in a tool
   result; and
2. carries a verbatim fingerprint that **does not occur anywhere in the repository outside
   `drive/chats/`** — checked against every `.md`, `.tsv`, `.txt`, `.py`, `.json`, `.csv`, `.out`
   and `.log` file, 4,132 of them.

It does **not** mean the content is lost. The transcripts are in the repository, mirrored and
sharded. It means the content has **no label, no home and no index** — a future session cannot find
it by looking for it, only by reading 15 MB of conversation.

## The corpus, measured

`drive/chats/` is 411 MB on disk, but that is not 411 MB of conversation:

| block type | count | size |
|---|---:|---:|
| `tool_result` | 30,322 | 214.8 MB |
| `tool_use` | 30,335 | 111.2 MB |
| **`text` — the prose** | **22,844** | **19.6 MB** |
| `thinking` | 14,411 | 11.4 MB |
| attachments / files | 1,164 | 4.2 MB |

`tool_use` is where `tools/recover.py` already mined the heredocs into `recovered/`. The prose is the
19.6 MB of `text`; stripped of fenced code blocks it is **15.1 MB across 295 conversations** — the
57 conversations with no substantive prose are excluded.

## Two independent passes, and why both were needed

**Stage A — the identifier census (mechanical, exhaustive).** Every governance identifier in the
prose, cross-checked against the repository:

| identifier kind | named in prose | present in repo | **prose-only** |
|---|---:|---:|---:|
| `W-` register entries | 164 | 195 | **0** |
| Rulings | 47 | 53 | **0** |
| Dockets | 19 | 35 | **0** |
| **Faults `F##.#`** | 225 | 196 | **40** |
| Registers | 734 | 933 | **178** |
| `MC` entries | 6 | 39 | **1** |

**The governance spine is intact.** Zero prose-only rulings, dockets or W-entries. The loss is in
the working layer.

**Stage B — the reading pass (45 subagents, capped).** The 15.1 MB was split into 45 chunks of
≤340 KB and read in full. Each agent reported at most 30 findings, ranked by load-bearing weight,
quoting verbatim, and was explicitly told **not** to check the repository — that verification is
done here, mechanically, so no row rests on an agent's judgement about absence.

**Neither pass alone is sufficient, and the overlap proves it.** Stage B surfaced only **11 of the
40** fault ids Stage A proved prose-only — the other 29 lost to bigger items under the 30-finding
cap. Those 29 are merged into the list from Stage A (`_chunk = stage-a-identifier-census`). Read
that the other way: **the list is a floor, not a census.** Many agents reported cutting strong
material at the cap and named what they dropped.

## The result

1,256 candidate findings were checked. **184 turned out to be already banked** and were dropped.
**1,072 survived**, plus the 29 merged faults = **1,101 rows**.

| category | rows | what it is |
|---|---:|---|
| MEASUREMENT | 275 | a number, count, md5 or result asserted as established |
| FAULT | 217 | a defect found in an instrument, a document or a claim |
| CORRECTION | 199 | a claim withdrawn, amended or superseded |
| DEFINITION | 179 | a named concept given its meaning |
| STANDING-RULE | 142 | a rule declared to govern future work |
| DECISION | 65 | a choice made, with its reason |
| NAMED-ARTEFACT | 24 | a file or instrument named as produced |

1,084 HIGH confidence, 17 MEDIUM. Concentrated in: *The Method 1.6* (168), *indexing without
prediction* (152), *transitions* (84), *The Method 1.7* (65), *Cold fusion exploration* (59).

## The mechanism, named by the corpus itself

**88% of prose-only faults belong to sessions that left no artefact at all**, against 19% for banked
faults. Of sessions 1–104 in the Löwdin programme, 36 left no artefact; the barren stretch is
s42–s70, and that is exactly where the prose-only faults cluster.

The corpus diagnosed this itself, in a fault that is — fittingly — prose-only. **F18.3**:

> *"container failure mid-run after the seal; **work after a seal that is not re-sealed survives only
> in the transcript**"*

## The finding that most needs a ruling

**Register 66 is contradicted by an unbanked re-measurement.** The seated Register states:

> *"THE OCCUPIED CELLS FORM AN ORDER IDEAL OF Λ — DOWNWARD CLOSED WITHOUT EXCEPTION. …no violations
> across all 118 cells… if an element has **ground-state configuration** (n,ℓ,k)… A property that
> does not appear to have been noted."*

Conversation `f5fb44a9-a6b3-4c15-ab61-64a7115fcfbb` ("Cold fusion exploration"), msg 171:

> *"The accumulation argument was **wrong**, and testing it properly overturned three headline
> results."*

| | register 66 | re-measured |
|---|---|---|
| distinct cells | 118 | **110** |
| order ideal | yes | **NO — 172 violations, 7 holes** |
| Z a linear extension | 0 violations | **9 violations** |
| admissible ℓ-orderings | 1 of 120 | **0 of 120** |

Verified four ways: verbatim in the prose; verbatim in the source shard (12 occurrences); **absent
from every repository file**; and the named mechanism confirmed against the corpus's own seated
member `method/members/LW1-ground.py` — V `3d3` → Cr `3d5` (nothing has 3d⁴), Ni → Cu `3d10` (no
3d⁹), Rh `4d8` → Pd `4d10` (no 4d⁹), Ir `5d7` → Pt `5d9` (no 5d⁸). That member's own line 9 reads
*"patched the exceptions by hand. That table was wrong at Pd."*

**The order-ideal computation has not been re-run here.** What is recorded is that the corpus holds
two contradictory records of one claim under the same stated convention, that the later is unbanked,
and that its mechanism is present in the repository's own ground-state data. Which stands is the
author's ruling to make.

## Other material of the same weight

- **`P19`–`P23`** — five principles retained by the author as Laws, in prose only.
- **The construction defect** — §3.3's printed caps `(3,3,2,3)` do not give 976 cells; `(3,3,1,3)`
  plus a nowhere-stated eighth constraint `k ≥ 1` does. *"A reader rebuilding from §2.1 and §3.3 as
  printed obtained a different object"* — a reader following the book gets 1,584 cells.
- **"The null was 96, not 28"** — the headline Löwdin comparison collapses from 99-against-28 to
  99-against-96, and the 99 was *fitted*: held out it is 90; free-running from hydrogen, 72 against
  Madelung's 94.
- **`dim(Λ₈) = 8` is false** — the derivation gives 7, with an explicit 7-element antichain.
- **Λ₈ is not maximal**; **Λ₈ composability 50.3% → zero**; **register 596 withdrawn**;
  **register 1395's 47/11 superseded by 1426's 38/20**.
- **Two admitted fabrications** — twenty-one Ca I level values generated rather than read
  (register 695), and `channels.py` writing `bracket = f"{interior}/{interior}"` so a verification
  column passed *by construction* across 280 of 413 channels, carried into printed Chapter 24.
- **An entire paper** — *The Lach Elemental Lattice* — whose full intellectual record exists only in
  one conversation's prose.

## The open item this list creates

**199 unbanked CORRECTIONs.** Multiple agents independently flagged the same hazard: a superseded
number may sit in the repository *with its withdrawal missing*. Register 66 is the confirmed
instance. Finding the rest is a distinct job — take each `CORRECTION` row, extract the superseded
value, and search the repository for it. That audit has **not** been run.

## Re-verification

```bash
# rebuild the prose corpus and the repo index, then re-run the whole check
#   (the generator lives in the session scratchpad; the two inputs are reproducible)

# 1. the corpus decomposition quoted above
python3 - <<'EOF'
import json, pathlib, collections
sizes=collections.Counter(); counts=collections.Counter()
for sh in pathlib.Path('drive/chats').rglob('*.json'):
    try: d=json.loads(sh.read_text(encoding='utf-8',errors='replace'))
    except Exception: continue
    for m in d.get('chat_messages',[]):
        for b in (m.get('content') or []):
            if isinstance(b,dict):
                sizes[b.get('type','?')]+=len(json.dumps(b)); counts[b.get('type','?')]+=1
for t,s in sizes.most_common(): print(f'{t:<16}{counts[t]:>8,}{s/1e6:>10.1f} MB')
EOF

# 2. spot-check any row: its quote must be in the shard and absent from the repo.
#    NOTE: exclude this file and PROSE-ONLY.tsv — they now quote the finding themselves,
#    so a naive grep matches them and looks like the claim has been falsified.
grep -c '172 violations' drive/chats/2026-*/f5fb44a9-*.json          # expect >0
grep -rl '172 violations' --include='*.md' . \
  | grep -v drive/chats | grep -v 'docs/PROSE-ONLY.md'               # expect nothing

# 3. the fault census
grep -rn 'F51\.2' --include='*.md' . | grep -v drive/chats           # expect nothing
```

## How to use the list

`PROSE-ONLY.tsv` columns: `id` (stable `PO-NNNN`), `category`, `label`, `quote` (verbatim),
`conversation` (uuid — the shard is `drive/chats/<yyyy-mm>/<uuid>.json`), `conversation_title`,
`msg` (message index), `identifiers`, `why`, `confidence`.

To read the full context of any row, open its shard and go to the message index. The row's `quote`
is verbatim, so it greps.

**A row is a candidate for a home, not an instruction to create one.** Deciding which of these
1,101 statements deserves a register entry, a fault file, a docket row or nothing at all is the
author's call. This list only guarantees that the decision can now be made deliberately, instead of
depending on whether anyone happens to re-read the right conversation.
