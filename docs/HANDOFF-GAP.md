# HANDOFF-GAP — the handoffs the corpus names, holds nowhere, and the chats still carry

`COVERAGE.tsv` censuses artefact names of **filename shape** and knows 61 handoffs. The two live
bundles also refer to **88 distinct `HANDOFF-<n>` by bare number**, and **26 of those are held
nowhere in the repository** — not in `method/`, not in `drive/`, not in `extracted/`, not in
`recovered/`.

**Twenty-three of the twenty-six have a body in the chat export.** `HANDOFF-GAP.tsv` is the standing
list: one row per unheld handoff, with the conversation and message index to open.

**Nothing was recovered and nothing was written into `recovered/`.** Regenerating a tree is the
author's call; the chat-67 full hold governs.

## Why they were missed, and it is a clean mechanism

`recover.py` builds its wanted-set from `COVERAGE.tsv`'s artefact column. That column holds names of
filename shape. **Twenty-five of these twenty-six never appear in filename shape** — the bundles cite
them as `HANDOFF-71`, never as `HANDOFF-71.md` — so they were never in the wanted-set, never wanted,
and never recovered. The census and the recovery pass are both working correctly; the names simply
fall between them.

This is a **different** limitation from the one `docs/RECOVER.md` already records. That one was the
tool not being idempotent, and it was fixed. This one is the shape of the wanted-set itself.

## What is there

| class | count | what it means |
|---|---:|---|
| **`BODY-WRITTEN`** | **15** | a tool call writes `HANDOFF-<n>.md` and carries the content with it — the body is in the export in full |
| **`BODY-READ-BACK`** | **8** | the file was uploaded and read into the chat; a body is present, but the read was paged |
| `MENTION-ONLY` | 3 | the name is spoken and nothing more — `HANDOFF-2`, `HANDOFF-103`, `HANDOFF-104` |

Every one of the 23 is a real handoff document. The title lines chain exactly:

> `# HANDOFF-71 — The Method 1.6 — chat 118 → chat 119`

and that title is found in the conversation titled **119** — the chat it was written *for*. All 23
line up that way, which is the strongest single check that these are the documents they claim to be
and not stray references.

## The truncation notes are reassuring, not alarming

Seven of the eight `BODY-READ-BACK` rows carry a truncation note **about that very document**, and
none of the fifteen `BODY-WRITTEN` rows does — exactly the split you would predict, since a written
file is not paged and an uploaded one is. But read what the notes say:

> `"description": "Read the truncated middle of HANDOFF-55"`

> `"description": "Read handoff lines 87-280 (truncated portion, first half)"`

**That is a session noticing the truncation and going back for the missing part.** The note is
evidence the gap was addressed, not that content is lost. Whether the union of those reads covers the
whole file is a question for a recovery pass to answer file by file — it is **not** asserted here.

## What this does not establish

- **`MENTION-ONLY` is not a finding of loss.** A name in prose is not proof a file existed. The three
  are reported as the conservative call, not as absences.
- **`chars_after_title` is an upper bound, not a length.** It counts from the title line to the end
  of the containing message, which for a read-back is the whole megabyte-scale message. It says
  material is there; it does not say how much of it is the handoff.
- **No body was extracted, verified against a hash, or compared with a held copy.** The row names a
  conversation and a message. Opening it is the next step, and it has not been taken.

## Two traps, both of which produced a wrong answer here first

1. **The bodies are in tool calls, not prose.** A handoff is *written* by a tool, so its body lives
   in a `tool_use` input. An extractor reading only `text` blocks reports **all twenty-six as
   `MENTION-ONLY`**, which is what the first pass here did.
2. **The export nests JSON inside JSON.** A message's own newlines arrive double-escaped once it is
   re-serialised, so a `^`-anchored heading pattern matches nothing at all. `coverage.py` carries a
   comment about the same trap one level down. And an *unanchored* `cat` matches the middle of
   "trun**cat**ed" — which is how a first pass claimed a written body for `HANDOFF-54` on the strength
   of the phrase *"truncated middle of HANDOFF-54"*. Every pattern in the generator is word-anchored.

## Re-verification

```bash
# the count that starts it: referenced by bare number, held nowhere
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

# and that they are not in the census's artefact column, which is why they were missed
cut -f1 COVERAGE.tsv | grep -c '^HANDOFF'        # 61 of filename shape
grep -c 'HANDOFF-71' COVERAGE.tsv                # 0
```

## Columns

`handoff`, `number`, `class`, `prose_mentions`, `chars_after_title` (upper bound — see above),
`truncation_warning` (the note, verbatim, when one names this document), `conversation`,
`conversation_title`, `date`, `msg`, `title_line`.
