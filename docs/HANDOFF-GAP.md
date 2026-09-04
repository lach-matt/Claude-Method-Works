# HANDOFF-GAP — the handoffs the corpus names, holds nowhere, and the chats carry

`COVERAGE.tsv` censuses artefact names of **filename shape** and knows 61 handoffs. The two live
bundles also cite **88 distinct `HANDOFF-<n>` by bare number**, and **26 of those are held nowhere in
the repository** — not in `method/`, `drive/`, `extracted/` or `recovered/`.

**Twenty-three had a complete body in the chat export — 596 KB, extracted exactly — and all
twenty-three are now seated.** They are in `recovered/` under the status **`RECOVERED-BY-NUMBER`**,
with `recovered/LEDGER.tsv` carrying the md5, the source shard and the conversation for each.
`HANDOFF-GAP.tsv` is the provenance record: byte length, line count, md5, the message that holds
each one, and `seated_as`.

**Three remain held nowhere** — `HANDOFF-2`, `HANDOFF-103`, `HANDOFF-104` — and each is
`MENTION-ONLY`: the name is spoken and no body exists in the export. That is not a finding of loss.

| | |
|---|---:|
| `HANDOFF-<n>` cited by bare number in the two live bundles | 88 |
| held before this recovery | 62 |
| **seated by it** | **23** |
| still held nowhere | 3 |

## The status is its own, and that is deliberate

They are ledgered **`RECOVERED-BY-NUMBER`**, not `RECOVERED`. How a file was found is part of what it
is here: these were reachable only through a bare-number citation, never through the wanted-set every
other recovered row came from. Flattening them to `RECOVERED` would lose exactly the fact that made
them findable — the same discipline that keeps `RECOVERED` distinct from `RECOVERED-BY-HEADING` and
`RECONSTRUCTED` from `RECOVERED`.

**`COVERAGE.tsv` does not move, and that is the confirmation.** Re-running `coverage.py --chats`
after seating gives a byte-identical file. It should: the 23 were never in the census's artefact
column, which is the whole reason they were missed. A census that counted them now would mean the
mechanism described below was wrong.

**The generator excludes its own recoveries from the held-test.** Otherwise this file erases its own
history the first time it is regenerated — the 23 are seated, a naive held-test drops them, and the
record of where they came from goes with them. It reads `recovered/LEDGER.tsv` for the
`RECOVERED-BY-NUMBER` rows and holds them out.

## Why they were missed, and it is a clean mechanism

`recover.py` builds its wanted-set from `COVERAGE.tsv`'s artefact column. That column holds names of
filename shape. **Twenty-five of these twenty-six never appear in filename shape** — the bundles cite
them as `HANDOFF-71`, never as `HANDOFF-71.md` — so they were never in the wanted-set, never wanted,
and never recovered. The census and the recovery pass are both working correctly; the names fall
between them.

This is a **different** limitation from the one `docs/RECOVER.md` records. That one was the tool not
being idempotent, and it was fixed. This one is the shape of the wanted-set itself.

## How the export is read, and why it matters

**A handoff is written by a tool call, so its body is the literal value of that call's
`file_text`/`content`.** Walking each message's blocks and matching a `tool_use` whose path ends
`HANDOFF-<n>.md` recovers the document **exactly** — not by pattern, and with no guess about where it
ends.

That distinction was not academic. A first version of this file classified by regex over the
serialised message and reported **15** exact bodies plus 8 "read back from an upload, possibly
truncated". **It was too pessimistic by eight.** A session that read a handoff back also wrote it out
again elsewhere in the export, and the structural walk finds a write for all 23. The truncation
caveat that version carried does not apply to any of them.

| class | count | what it means |
|---|---:|---|
| **`BODY-EXACT`** | **23** | the body is the content of the tool call that wrote the file; md5 recorded |
| `MENTION-ONLY` | 3 | the name is spoken and nothing more — `HANDOFF-2`, `HANDOFF-103`, `HANDOFF-104` |

## They are the documents they claim to be

Each title line chains, and the chat that writes it is the chat it is written *from*:

> `# HANDOFF-71 — The Method 1.6 — chat 118 → chat 119`, written in the conversation titled **118**

All 23 line up that way. They open with the title and close with the standing directive block
(*"…Timeout on every call. Never copy over an existing file."*), which is what a complete handoff of
this corpus looks like.

**One is different, and it is not a fault.** `HANDOFF-33` is titled
`# THE METHOD 1.6 — HANDOFF (chat 31 → chat 32)` — the earlier convention, before the documents were
numbered in their own titles. It is `HANDOFF-33.md` by its write path, not by its heading.

## What this does not establish

- **`MENTION-ONLY` is not a finding of loss.** A name in prose is not proof a file existed. The three
  are the conservative call, not an absence.
- **No extracted body was compared against a held copy**, because none is held — that is the
  premise. The md5 is of what the export carries, so a recovery pass can be checked against this
  file, and it is not a claim of identity with anything.
- **Where a handoff was written more than once, the longest write is the row.** `writes_seen` says
  how many were found; earlier drafts of the same document are not reconciled here.
- **Seating is not verification against a lost original.** No held copy exists to compare against —
  that is the premise. The md5 is of what the export carries, and the seating asserts only that the
  bytes in `recovered/` are the bytes the tool call wrote.
- **`HANDOFF-33` keeps its earlier-convention title.** It was seated as written, not retitled.

## Two traps, both of which produced a wrong answer here first

1. **The bodies are in tool calls, not prose.** An extractor reading only `text` blocks reports
   **all twenty-six as `MENTION-ONLY`**, which the first pass did.
2. **The export nests JSON inside JSON.** A message's own newlines arrive double-escaped once it is
   re-serialised, so a `^`-anchored heading pattern matches nothing at all; `coverage.py` carries a
   comment on the same trap one level down. And an *unanchored* `cat` matches the middle of
   "trun**cat**ed", which is how a pass claimed a written body for `HANDOFF-54` from the phrase
   *"truncated middle of HANDOFF-54"*.

Both are arguments for reading the export **structurally** rather than as text, which is what the
generator now does and why the count rose from 15 to 23.

## Re-verification

```bash
# referenced by bare number, held nowhere
python3 - <<'EOF'
import re, pathlib
b = ''.join(pathlib.Path(p).read_text(errors='replace') for p in (
    'method/The_Method_1_6_BUILD180_compendia_papers_audits.md',
    'method/The_Method_1_6_BUILD90_main_and_register.md'))
ref = {int(m.group(1)) for m in re.finditer(r'\bHANDOFF-(\d{1,3})\b', b)}
held = {int(m.group(1)) for p in pathlib.Path('.').rglob('*')
        if p.is_file() for m in [re.match(r'(?i)^handoff[-_]?(\d{1,3})[.-]', p.name)] if m}
print(len(ref), 'referenced,', len(ref & held), 'held,', len(ref - held), 'not')
EOF

# why they were missed: not in the census's artefact column
cut -f1 COVERAGE.tsv | grep -c '^HANDOFF'     # 61, all of filename shape
grep -c 'HANDOFF-71' COVERAGE.tsv             # 0
```

## Columns

`handoff`, `number`, `class`, `prose_mentions`, `bytes`, `lines`, `md5` (of the extracted body),
`writes_seen`, `conversation`, `conversation_title`, `date`, `msg`, `seated_as`, `title_line`.
