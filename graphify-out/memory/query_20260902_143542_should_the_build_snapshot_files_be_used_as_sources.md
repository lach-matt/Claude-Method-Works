---
type: "query"
date: "2026-09-02T14:35:42.308571+00:00"
question: "Should the BUILD snapshot files be used as sources?"
contributor: "graphify"
outcome: "dead_end"
source_nodes: ["The Method 1.6 BUILD174 Compendia, Papers and Audits", "The Drive Mirror", "Register Entries Are Append-Only"]
---

# Q: Should the BUILD snapshot files be used as sources?

## Answer

The Drive mirror carries 104 successive BUILD snapshots (The_Method_1_6_BUILD*_compendia_papers_audits.md, 4-6 MB each) plus 42 byte-identical duplicates. Together they are ~450 MB and ~60M words of the ~63.6M total, and they are almost entirely restatements of one another.

Do NOT graph or query them as separate sources. Only the latest, BUILD174, carries current content; earlier BUILDs are superseded history and querying them returns stale claims that later registers withdrew (e.g. Q.exch's s = -0.0782 was WITHDRAWN at register 1168, and MC-52 / MC-53 were RETIRED as sample artefacts). The .graphifyignore in the repo root encodes this scoping. Duplicates carry a __<driveFileId> suffix or a -1 suffix and are byte-identical to their unsuffixed sibling.

For history questions, prefer the register entries and the HANDOFF chain, which are append-only and cite what they supersede, over diffing BUILD snapshots.

## Outcome

- Signal: dead_end

## Source Nodes

- The Method 1.6 BUILD174 Compendia, Papers and Audits
- The Drive Mirror
- Register Entries Are Append-Only