# DIRECTIVES.md — the three directives as three index axes

`tools/directives.py` places every substantive result in the three papers on three axes at once, one
axis per project directive, and reads off the cell where all three coincide. Run it with no argument
for the whole reading; `--axes`, `--cell`, `--gaps` and `--selftest` give the parts.

## Why an index rather than prose

The project has three directives and they are not one question:

| axis | directive |
|---|---|
| **X** | identify and **prove** a self-sustaining cold fusion reaction |
| **Y** | identify the **materials** needed |
| **Z** | lay out the laboratory **procedure** that would witness it |

Prose can answer one of those while sounding like it answered three, and for most of this project's
life it did. An index cannot. Each of the 64 rows carries a grade 0–3 on each axis, so a result that
settles the balance but names no apparatus is visibly a one-axis result, and the cell where all three
meet is a computation rather than a claim.

## The rubric

Grades are applied uniformly and are stated in the instrument itself.

- **X** — 3 DECIDES (closes the question for a named configuration) · 2 BOUNDS (a hard bound no later
  work may cross) · 1 BEARS (an input to the balance, not a bound on it) · 0 SILENT.
- **Y** — 3 SPECIFIES (a procurable specification: substance, quantity, tolerance) · 2 CONSTRAINS ·
  1 IMPLIES · 0 SILENT.
- **Z** — 3 PROTOCOL (executable, outcomes committed before the run) · 2 MEASURE (a named measurement
  on named apparatus) · 1 IMPLIES · 0 SILENT.

**X carries a sign, and that is the point.** A result that *forbids* self-sustaining operation is a
grade-3 result on the proof axis, and an index that scored it as progress would be lying by
arithmetic. `+` supports, `−` forbids, `0` neither — and a grade-3 row at sign `0` is a measurement
that *would* decide and has not.

## What is mechanical and what is judgement

The grade is a judgement. Three things are not:

1. **Every row names a section that exists.** `--selftest` matches all 64 rows against the headings of
   the three papers as they are on disk. A row cannot cite a section that is not there.
2. **The sign discipline.** A sign is carried only at grade ≥ 2 — nothing that merely bears on the
   balance is allowed a direction.
3. **The coincidence cell is computed.** The instrument does not assert which rows sit on all three
   axes; it filters and prints them, and the verdict text is generated from that filter.

## The standing refusal, and its state

The instrument watches one cell in particular: **X = 3, sign +, and Z = 3** — a result that decides
the balance favourably *and* carries an executable protocol.

**On the first reading of this index that cell was empty.** The three directives were each answered
somewhere and never at the same point: 20 results specified materials, 15 carried protocols, 12
decided the balance — and every protocol was attached to a bench-scale or staged measurement, none to
a configuration shown to be net-positive. The nearest point, `SP:5.2` ("the binder does not have to be
bought"), stood at X3+ Y3 **Z2**: proved, provisioned, and unrunnable as written.

**It is now occupied, by `SP:6`.** Writing the procedure for that configuration — apparatus, gating,
committed rate, and what each outcome settles — is what closed it, and closing it also produced a
correction to `SP:5.2` itself: its 90 percent capture row compared a collector's acceptance with a
fuel target's stopping fraction and is withdrawn. See `papers/Cold_Fusion_Specification_and_Procedure_v1.0.md`
§5.2 and §6, and `python3 tools/collector.py --insitu`.

The selftest **reports** this cell rather than failing on it. Its state is a finding about the
repository, and a finding is recorded, never repaired.

## The reading, as of this writing

- **Directive 1** is answered in both directions: 9 results forbid the standalone configuration by
  theorem, 4 support a co-product one. The answer to the question as asked is **no standalone, yes as
  a co-product**, and both halves are proved rather than asserted.
- **Directive 2** is answered: 21 results specify a procurable material, quantity or tolerance, across
  the bench column, the reactor column and the in-situ cell.
- **Directive 3** is answered: 16 results carry an executable protocol, and **one** of them is
  attached to a configuration the index shows to be net-positive.
- **The coincidence**: 17 results sit on all three axes at grade ≥ 2; 3 at the top of all three; and
  exactly **one** of those carries a positive proof sign — `D63`, `SP:6`.

Two of the three top-grade rows are `BE:10.2` and `BE:10.4`, Stages B and D of the laboratory
programme, and both are sign 0. They sit at the top of all three axes because they *would* decide the
balance, not because they have. **A cell filled by undecided measurements is not an answered
directive**, and the instrument says so in those words.

## The open questions, worked

Nine open questions were carried, and the first pass of this work sorted them into categories. A
category is not an answer, and six of the nine were calculations this repository could already do.
`python3 tools/collector.py --open` runs them; `python3 tools/mucf.py --selftest` reproduces the three
that come off the cycle count.

| | question | status |
|---|---|---|
| Q1 | the acceptance, never measured end to end | **narrowed** — floor from a second capture simulation with transport removed; the span falls from 2131× to **5.97×** |
| Q2 | which sticking branch is operative | **closed** — the witnessed 150 cycles, inverted, give **0.517–0.547 %**, inside the measured trio and below theory |
| Q3 | the service-life model over-predicts by 2.24 | **closed** — at the corrected sticking it returns **150.5** against 150 |
| Q4 | fuel purity bounded by no experiment | **closed** — the fuel behind the 150 carried at most **10.93 ppm**, under the **31.10 ppm** parity level |
| Q5 | the temperature axis is confounded | **closed** — every balance already runs the cycle rate *at* its ceiling |
| Q6 | the 2.37 is unexplained | **explained, not adopted** — a normalisation; **2.389** interacting nucleons reproduce it to 0.8 % |
| Q7 | a 0.186 sr wedge is uncovered | **closed** — interpolation puts it at **1.072** against a bound of 1.10 |
| Q8 | transport, cooling, stopping unmodelled | **closed** — retired by §6 |
| Q9 | the composed sticking 0.234 unresolved | **closed** — superseded |

**One measurement answered three of them.** The 150-cycle result, read backwards through the
service-life expression, returns a sticking by a route that uses neither published sticking
measurement (Q2), disposes of the 2.24 over-prediction as an artefact of the superseded value (Q3),
and bounds the contamination that fuel can have carried (Q4).

**Q6 reverses.** Beam energy was the last candidate standing, and HARP's own 3/5/8/12 GeV columns on
the same target refute it in the opposite direction: production is **1.63× dearer** at 3 GeV, not
cheaper. What survives is a normalisation — per beam particle against per interaction — which
reproduces the number rather than being bounded away from it, and is declined because it reproduces it
for pions *produced* while a thick target also reabsorbs them.

**Seven closed, one narrowed, one explained and declined.** The two that still move a number are
measurements rather than calculations: the acceptance (Stage A) and whether the thick-target
normalisation survives to capture (Stage C). The answer's magnitude is now **2.01 % to 12.01 %** of the
host beam, and the sign is open at no value of any of them: at the floor and one fusion per binder it
still returns 0.01341 %.

## Re-verify

```
python3 tools/directives.py --selftest     # 64 rows against the papers on disk
python3 tools/directives.py                # the whole reading
python3 tools/collector.py --insitu        # the apparatus and its ceiling
python3 tools/collector.py --open          # every open question, and what it can move
python3 tools/verify_paper.py papers/Cold_Fusion_Specification_and_Procedure_v1.0.md
```
