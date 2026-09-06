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
| `warp-drive/SHIFT-CEILING.md` | `warp-drive/warpdrive.py` | a closed form for the shift-vector limit Fuchs et al. left open, and the top speed it implies |
| `warp-drive/SHELL-PROFILE.md` | `warp-drive/warpdrive.py` | the shell reconstructed by TOV integration; corrects the ceiling and gives the fill-fraction design rule |
| `warp-drive/ACCELERATION.md` | `warp-drive/warpdrive.py` | why a positive-ADM-mass drive cannot self-accelerate, and what starting one costs |
| `warp-drive/SOURCE-CODE.md` | `warp-drive/warpdrive.py` | what reading Warp Factory changed, including a factor of two against this series |
| `warp-drive/MEASURED.md` | `warp-drive/warpdrive.py` + `octave/` | Warp Factory actually run; the ceiling measured at 0.0218 c and the prediction confirmed |
| `warp-drive/WHAT-BINDS.md` | `warp-drive/warpdrive.py` + `octave/` | the fill curve measured — overturning a design rule — and where the NEC actually fails |
| `warp-drive/THE-DESIGN-EQUATION.md` | `warp-drive/warpdrive.py` + `octave/` | the three bounds composed into a design equation, and a measured 1.6x speed gain from one line |
| `warp-drive/DENSITY-IS-CLOSED.md` | `warp-drive/warpdrive.py` + `octave/` | shaped density built and measured: a closed lever, and the domain of the design equation |

## `warp-drive/`

Seats the warp drive — cited twice in `method/members/Transitions.md` and never named again — as an
object threshold in that paper's own index, and computes its energy budget and engine specification
against the primary literature.

```
python3 research/warp-drive/warpdrive.py --selftest   # 84 fixtures
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

The eleven papers run in order. `WARP-DRIVE.md` places the object and gives the buildable
specification. `ENGINE-ASSESSMENT.md` reviews M's design deliverable against it.
`ROTATING-SHELL.md` takes the one idea in that deliverable which survived review and carries it onto
the buildable solution. `SHIFT-CEILING.md` answers the one number Fuchs et al. named as open — how
far the shift vector can be pushed before the drive stops being physical — and finds a closed form.
`SHELL-PROFILE.md` then replaces that paper's eyeballed input with a TOV integration and corrects it
downward, and `ACCELERATION.md` prices the problem all five defer. A paper is never edited to match a
later finding: `SHIFT-CEILING.md` and `SHELL-PROFILE.md` carry notes naming what superseded them, and
every state stands. `SOURCE-CODE.md` is where the series corrects itself — it reads the authors'
published toolkit and finds two of this series' own inferences wrong, both in the flattering
direction. `MEASURED.md` then runs that toolkit under GNU Octave and replaces every inferred number
with a measured one, and `WHAT-BINDS.md` measures the two things that paper left open — overturning
a design rule this series had published, and raising one careful question about the instrument
everything downstream depends on. `THE-DESIGN-EQUATION.md` then applies **P8** — *any true answer,
good or bad, is a bound*, and *three bounds on one object are a coordinate* (`The_Method_1_6-2.md`
§2.15, §2.17.3) — to the bounds the first nine established, and turns them from a limit into a design
equation with a measured 1.6x gain and a bound on the whole family. `DENSITY-IS-CLOSED.md` then
builds the first of the two levers that bound named, measures it, and closes it — leaving one.

The instrument copies the fifteen-letter closure rules verbatim from `recovered/objects15.py` with a
provenance comment, per the standing rule that an instrument imports a seated form and never silently
reimplements one. It reproduces `TRANSITIONS` §7.1's printed 18,888 / 18,072 / 816 before reporting
anything.
