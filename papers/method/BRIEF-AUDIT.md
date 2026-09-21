# Audit brief

You are auditing one drafted paper under `papers/method/<dir>/`. Read `PAPER-SPEC.md` beside this file
first (§4, §5, §8, §10 bind the audit). The audit is written to `<dir>/AUDIT.md` and is not published.

## Part A — content audit (against the sources and the checks)

1. Read `PAPER.md` in full. Then read `SOURCES.md` and open every source passage it names (with
   `sed -n A,Bp` on the volume under `/home/user/Claude-Method-Works/method/members/`). For every
   definition, lemma, theorem, corollary, law and number in the paper, record: where the source states
   it; whether the paper's statement is the source's, weaker, or stronger; whether the proof in the
   paper is complete (every step justified; nothing assumed that is not defined; no "clearly").
2. Run `python3 check.py` and `python3 check.py --selftest` (after
   `export PATH=/home/user/Claude-Method-Works/method/bin:$PATH`). Match every printed number in the
   paper to a line of the check's output. A number with no check is a finding. A check that does not
   test what the sentence claims is a finding.
3. Read every z3 obligation in `check.py`: is the encoding the operator the paper defines? Are both
   guards run before the result is reported? Is the box named in the paper? A claim marked
   MACHINE-CHECKED for a box the check does not cover is a finding.
4. Read every figure (the image itself, with the Read tool) against its caption and the text.
5. Run `python3 papers/method/lint.py <dir>`.
6. **Typography in the rendered PDF, not in the source.** Render the paper, screenshot the pages
   (`/opt/pw-browsers/chromium-1194/chrome-linux/chrome --headless --disable-gpu --no-sandbox
   --screenshot=<out>.png --window-size=1000,1400 --hide-scrollbars file://<abs path to the .html>`)
   and read them. Check: subscripts and superscripts are Unicode throughout and never fall back to
   an underscore or a caret in prose (δ₀ not delta_0, α_d written with a real subscript); no literal
   asterisks, backslashes or stray markup on the page; every table fits its column and no cell is
   clipped; every figure appears, is legible at print size, and sits with its caption; no heading is
   orphaned at a page foot. A defect visible on the page is a finding even when the source is clean.

## Part B — reader audits, three points of view, each written in the first person as that reader

- **A mathematician** (lattice theory / order / combinatorics) who has never seen this material: is
  every object defined before use, is every proof a proof, what is unmotivated, what would a referee
  in *Order* or *Algebra Universalis* reject?
- **An atomic physicist** who works with NIST spectra: are the physical quantities right, the units,
  the provenance, the claims about spectra; what is overstated?
- **A journal referee**: novelty against the literature the paper cites (and the literature it should
  cite: name any missing standard reference with full author list and year), correctness, clarity,
  whether the abstract and §0 promise exactly what the body delivers, whether the verification record
  is honest.

Each reader lists findings as `R-n` with the line of PAPER.md, severity (BLOCKING / MAJOR / MINOR),
and the exact change that would resolve it. A reader who finds nothing says so and says why.

## Part C — the record

`AUDIT.md` ends with a table of every finding (A-n and R-n), its severity, and the disposition column
left blank for the drafter. The audit does not edit `PAPER.md`.

Your final message: the count of findings by severity, the three BLOCKING findings that matter most
(or that there are none), and one sentence on whether the paper is ready for the author's review.
