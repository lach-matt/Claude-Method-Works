# PROSE-ONLY — what the chat history holds that the repository does not

**`PROSE-ONLY.tsv` is the standing list: 1,168 statements that exist only in the conversation
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
| **Faults `F##.#`** | 225 | 196 | **40** → **16** |
| Registers | 734 | 933 | **178** |
| `MC` entries | 6 | 39 | **1** |

**The governance spine is intact.** Zero prose-only rulings, dockets or W-entries. The loss is in
the working layer.

**And the working layer has since been largely recovered.** Re-measured after the
`RECOVERED-BY-WRITE` pass seated 759 artefacts found by walking the export's tool calls
(`docs/RECOVER.md`), the fault census reads **233 named in chat prose, 217 present in the repo, 16
prose-only** — down from 40. The 16 that remain are `F1.3 F1.4 F5.1 F5.2 F6.2 F6.3 F7.3 F10.3 F10.4
F11.3 F11.4 F12.3 F18.4 F46.2 F55.4 F56.5`. **The registers count has not been re-measured** and
should be treated as the older figure until it is.

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

1,341 candidate findings were checked. **197 turned out to be already banked** and were dropped.
**1,144 survived**, plus 24 merged faults = **1,168 rows**, drawn from **194 conversations**.

| category | rows | what it is |
|---|---:|---|
| MEASUREMENT | 275 | a number, count, md5 or result asserted as established |
| FAULT | 224 | a defect found in an instrument, a document or a claim |
| CORRECTION | 212 | a claim withdrawn, amended or superseded |
| DEFINITION | 201 | a named concept given its meaning |
| STANDING-RULE | 158 | a rule declared to govern future work |
| DECISION | 74 | a choice made, with its reason |
| NAMED-ARTEFACT | 24 | a file or instrument named as produced |

1,164 HIGH confidence, 4 MEDIUM. Concentrated in: *The Method 1.6* (185), *indexing without
prediction* (152), *transitions* (93), *Cold fusion exploration* (68), *The Method 1.7* (65).

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

**The computation has since been re-run — see `docs/ORDER-IDEAL.md` and `tools/orderideal.py`.**
On the seated member (Z = 1..108) the occupied set is **not** downward closed: 98 cells, 197
violations, 5 subshells with an occupancy gap, 6 Z-order breaks, and **0 of 120** admissible
ℓ-orderings — the last matching the unbanked re-measurement exactly, against register 66's 1 of 120.
The three records disagree on the cell count (118 / 110 / 98) before they disagree on the property,
because they quantify over different element ranges. **No verdict is offered on register 66**; the
narrowed question for R3 is which object it quantifies over.

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

### A decision whose *reason* was never recorded

The live main volume's tower runs Λ₈ (49 mentions) … Λ₁₃ (26), and **Λ₁₄ appears zero times**;
`tower-2.py` likewise stops at `|Λ13| = 199130`. Read from the volume alone this looks like
unfinished work, and `On_the_Matter_of_Time_Travel.pdf` — held at `drive/The Method Materials/` and
described in conversation `52` as how the lattice was built from 7D to 14D — makes it look like a
gap against a foundational source.

It is not a gap. The author's reason is stated in that conversation:

> *"1D and 14D share coordinates because 14D is an axis which is an order of transition. But no
> matter how you try to build it, its appearance was always 1D"*

Λ₁₄ was found to collapse onto 1D, and that collapse is recorded as the seed of *"nothing is
something definable."* Before this list, that sentence existed in no file. A deliberate,
load-bearing decision left no trace, and a later reader would reasonably have re-opened it.

**Status note that must travel with these rows.** Conversation `52` also carries provenance the
author supplied from outside the record, and marks its status carefully — the multiverse reading is
graded unclosable at §29.2.2, and *"what was computed stands and does not support it."* Those rows
are records of what was said, not results. Do not flatten them.

## The open item this list creates

**212 unbanked CORRECTIONs.** That audit **has now been run** — see `RETRACTION-AUDIT.tsv` and
`docs/RETRACTION-AUDIT.md`. 124 of the 212 had a number occurring in a live volume (303 pairs);
187 were digit coincidence, **87 corrections had already landed**, 10 were undecidable, and
**19 are withdrawn values still standing as current**. The one that needs no interpretation:
`The_Method_1_6-2.md` prints *"the 2,475 previously printed here is withdrawn"* in one passage and
asserts *"costs the cylinder 2,475 cells"* in two others.

What remains untested: **88 corrections carried no number that appears in any volume**, so a
correction that withdrew a claim rather than a figure is out of that audit's reach.

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
#    IMPORTANT: exclude this file AND PROSE-ONLY.tsv. Both now quote the findings they
#    describe, so a naive grep matches them and looks like the claim has been falsified.
#    Use this helper for any row's quote:
notbanked() {  # usage: notbanked '<verbatim phrase>'
  grep -rl "$1" --include='*.md' --include='*.tsv' --include='*.txt' . 2>/dev/null \
    | grep -v '^./drive/chats' | grep -v 'PROSE-ONLY'
}
grep -c '172 violations' drive/chats/2026-*/f5fb44a9-*.json   # expect >0 (it is in the shard)
notbanked '172 violations'                                    # expect nothing
notbanked '14D is an axis'                                    # expect nothing

# 3. the fault census
notbanked 'F51.2'                                             # expect nothing
```

## How to use the list

`PROSE-ONLY.tsv` columns: `id` (stable `PO-NNNN`), `category`, `label`, `quote` (verbatim),
`conversation` (uuid — the shard is `drive/chats/<yyyy-mm>/<uuid>.json`), `conversation_title`,
`msg` (message index), `identifiers`, `why`, `confidence`.

To read the full context of any row, open its shard and go to the message index. The row's `quote`
is verbatim, so it greps.

**A row is a candidate for a home, not an instruction to create one.** Deciding which of these
1,168 statements deserves a register entry, a fault file, a docket row or nothing at all is the
author's call. This list only guarantees that the decision can now be made deliberately, instead of
depending on whether anyone happens to re-read the right conversation.
