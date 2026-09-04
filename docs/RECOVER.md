# `tools/recover.py` — the artefacts the chats wrote

`COVERAGE.tsv` could say *which conversation* holds a missing artefact. That still left a person
opening 352 shards by hand. This extracts the bodies instead.

```sh
python3 tools/recover.py            # rebuild recovered/ and its LEDGER.tsv
python3 tools/recover.py --verify   # re-hash every recovered file against the ledger
python3 tools/recover.py --selftest # assert the corpus's own recorded numbers
```

## What it recovers, and how surely

| Status | Rows | The claim |
| --- | ---: | --- |
| `RECOVERED` | 2,196 | A shell heredoc wrote the file and **named its own target**: `cat > …/HANDOFF-16.md <<'EOF'`. Filename and body both come from the source. |
| `RECOVERED-BY-HEADING` | 163 | A `code_block` carried the body but no filename, so the name is **inferred from the document's own Markdown heading**. Weaker, and separately labelled. |
| `RECOVERED-TRUNCATED` | 23 | The body carries a `< truncated lines N-M >` marker — the chat was showing an **elided view**, so the text is incomplete by the stated count. Kept, because a partial document is still evidence, but never to be read as whole. |
| `PRESENT-IN-REPO` | 51 | Byte-identical to something already tracked; not written again. |

**2,382 files, 9.4 MB** (2,433 rows; the `PRESENT-IN-REPO` rows write nothing).

## Two defects found by the graph pass, and fixed

**Truncated bodies were labelled as whole.** A chat that shows a file through a paging viewer elides the middle and says so. That display is valid text and hashes cleanly, so `--verify` passed it and the ledger called it `RECOVERED`. Twenty-three files are affected — **every one from the code-block rule, none from the heredoc rule** — the worst being `HANDOFF-53.md` at 160 lines missing. They now carry `RECOVERED-TRUNCATED` and a note stating the line count.

**A truncated body could hold the canonical name.** Versions were ordered by conversation date
alone, so the newest won the plain name and older ones took the `__<md5>` suffix. But for
`HANDOFF-37`, `-38`, `-39` and `-53` the newest conversation is the one showing an *elided* view, so
the plain name held the truncated text while the full document hid behind a suffix — the exact
inversion of what a reader expects. Completeness now outranks recency: a body with no truncation
marker takes the plain name, and only among equals does the newest win. `HANDOFF-53.md` went from
16,165 to **29,951 bytes** on that change alone.

**The tool was not idempotent.** Its code-block rule asked `COVERAGE.tsv` which names the repo still lacked — but `COVERAGE.tsv` is regenerated *from* `recovered/`, so every name this tool recovered turned `HELD` and vanished from the next run's wanted-set. A second run produced 2,196 rows where the first produced 2,337, with the extra files still on disk and no longer in the ledger. The rule now reads the artefact column unfiltered, making it a pure function of the corpus. That also widened its reach: 163 by-heading recoveries where the status-filtered version found 141. Among them **71 handoffs**, **68 `READ-*` slips** and over a thousand `.py`
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
