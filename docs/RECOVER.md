# `tools/recover.py` — the artefacts the chats wrote

`COVERAGE.tsv` could say *which conversation* holds a missing artefact. That still left a person
opening 352 shards by hand. This extracts the bodies instead.

```sh
python3 tools/recover.py            # rebuild recovered/ and its LEDGER.tsv
python3 tools/recover.py --verify   # re-hash every recovered file against the ledger
python3 tools/recover.py --selftest # assert the corpus's own recorded numbers
```

## What it recovers, and how surely

| Status | Files | The claim |
| --- | ---: | --- |
| `RECOVERED` | 2,196 | A shell heredoc wrote the file and **named its own target**: `cat > …/HANDOFF-16.md <<'EOF'`. Filename and body both come from the source. |
| `RECOVERED-BY-HEADING` | 141 | A `code_block` carried the body but no filename, so the name is **inferred from the document's own Markdown heading**. Weaker, and separately labelled. |
| `PRESENT-IN-REPO` | 2 | Byte-identical to something already tracked; not written again. |

**2,337 files, 8.7 MB.** Among them **71 handoffs**, **68 `READ-*` slips** and over a thousand `.py`
instruments. Every one is verified: `--verify` re-hashes the tree against `LEDGER.tsv` and reports
`0 bad`.

The heading rule is applied **only to names `COVERAGE.tsv` already reports the corpus asking for**.
That restriction is the point: it recovers what is known to be missing and manufactures nothing out
of arbitrary headings.

## RECOVERED is not mirrored

The status word is the corpus's own. These bytes were **measured out of the chat export**, not
fetched from the file they were written to, and no claim is made that a recovered file is
byte-identical to a copy held anywhere else. Nothing in `recovered/` is a member of any bundle;
`method/` remains the store of record and `drive/` the mirror.

Versions are kept rather than resolved: **147 names were written more than once with differing
content**, because the work evolved across chats. The body from the newest conversation keeps the
plain name; the others take a `__<md5 prefix>` suffix before the extension, mirroring how `drive/`
already distinguishes same-titled Drive copies. The ledger carries the conversation and its date for
every version, so the order is evidence rather than assertion.

## What it will not recover, and why

* **Files uploaded into a chat.** They appear in the export as a `files` entry with `file_name` and
  `file_uuid` and **no content whatsoever**. The bytes are not in the export, so no tool can produce
  them. `HANDOFF-16-1.md` is such an entry.
* **Bodies shown only as a `view` tool result.** Those carry line numbers and a tab per line.
  De-numbering them would be reconstruction, not recovery, so they are left alone.

## What it changed

Re-running `python3 tools/coverage.py --chats` afterwards, since recovered files now count as held:

| family | held before | held after | named |
| --- | ---: | ---: | ---: |
| `HANDOFF-*` | 12 | **54** | 58 |
| `READ-*` | 48 | **114** | 119 |
| instrument | 213 | **245** | 338 |
| **Total** | **559** | **702** | **1,005** |

**1,995 of the 2,015 recovered names are ones the books never mention** — work that existed only
inside the conversations. That is the larger half of what this pass found, and none of it was in
`COVERAGE.tsv`, because a census can only look for what the corpus names.
