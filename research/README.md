# `research/`

Original research produced **from** the corpus, never **into** it.

Nothing in this tree is a bundle member, a Register entry, or mirrored Drive content. Nothing here is
read by the §0 gate. `method/`, `drive/`, `extracted/` and `recovered/` are inputs to this tree and are
never written to by it — the chat-67 full hold governs, so a finding made here is **recorded, never
repaired** into a volume.

Each subdirectory holds one paper and the instrument that computes its numbers. Every instrument is
stdlib-only and takes a `--selftest` whose fixtures are the corpus's own printed figures and the
literature's own printed figures — never a number the paper invented. Run the selftest before trusting
a report.

| paper | instrument | subject |
|---|---|---|
| `warp-drive/WARP-DRIVE.md` | `warp-drive/warpdrive.py` | where a warp drive sits in the fifteen-letter violation index, what warp energy is, and which engine can be built |
| `warp-drive/ENGINE-ASSESSMENT.md` | `warp-drive/warpdrive.py` | *Warp Drive Theory* (the Drive design deliverable) checked against the physics it invokes |
| `warp-drive/ROTATING-SHELL.md` | `warp-drive/warpdrive.py` | whether counter-rotation can be carried onto a positive-energy warp shell, and what it costs |

## `warp-drive/`

Seats the warp drive — cited twice in `method/members/Transitions.md` and never named again — as an
object threshold in that paper's own index, and computes its energy budget and engine specification
against the primary literature.

```
python3 research/warp-drive/warpdrive.py --selftest   # 33 fixtures
python3 research/warp-drive/warpdrive.py              # the full report
```

`WARP-DRIVE.md` answers the question from the index and the literature. `ENGINE-ASSESSMENT.md`
reviews `drive/The Method Materials/warp drive theory.pdf` — the design deliverable, seated in the
mirror by `drive_sync.py --adopt` at status `ok-adopted` — against the same physics, and computes
every claim in it that is computable.

`pdftext.py` beside them is not an audit instrument and takes no selftest: it is a PDF text extractor
written because this container has neither poppler nor `pypdf`, and because the producer of that file
puts page layout in `q`/`cm`/`Q` graphics transforms, encodes glyphs as two-byte hex through
`/ToUnicode`, and emits spaces as explicit glyphs. It tracks the full CTM and never inserts a space
heuristically.

The three papers run in order: `WARP-DRIVE.md` places the object and gives the buildable specification, `ENGINE-ASSESSMENT.md` reviews M's design deliverable against it, and `ROTATING-SHELL.md` takes the one idea in that deliverable which survived review and carries it onto the buildable solution.

The instrument copies the fifteen-letter closure rules verbatim from `recovered/objects15.py` with a
provenance comment, per the standing rule that an instrument imports a seated form and never silently
reimplements one. It reproduces `TRANSITIONS` §7.1's printed 18,888 / 18,072 / 816 before reporting
anything.
