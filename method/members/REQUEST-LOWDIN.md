# REQUEST — THE METHOD 1.6 BUILD (chat 128; BUILD90 main, BUILD157 compendia) TO THE LÖWDIN PROJECT

**Date:** 2026-09-01. **Deliver to:** the Materials folder `1XX_5f3PZB6tjRtiZ2GIgd8Tt7i_4GgkY`, in a
subfolder **`LOWDIN-DELIVERY-1/`**. **Baseline:** both projects worked from the Prints & Proofs folder
`1vYctzLppUZ2vFPJDCZ6wvkgSdj3v_f6n`; the original this build reads is `The Method 1.6.md`, 738,550 B,
md5 `49900cf41f818ab789bb90fc596ac977`.

## Why

The book's standard is that every figure is recomputed by an instrument that travels with the build,
is validated against a witnessed anchor, and is banked as a golden the gate re-runs every session.
Chapter 35 and Register entries 1701–1712 print the largest claim in the six volumes — the ordering
derived from the equation at **107 of 107** — and this build holds **no instrument for it**: the Register
names `ground.py` (1306) and the paper names no file at all. Until the objects below are seated, the
claim is carried on the record's word. Nothing below is a request to redo the work; it is a request
for the work as it was done.

## Form of delivery (applies to every item)

- Files **as produced** — never retyped, never reformatted; Drive may add a `-1` suffix, the md5 decides.
- A **`MANIFEST.tsv`**: `name  bytes  md5  purpose` for every file delivered.
- A **`README.md`**: Python / NumPy / SciPy / any solver library with exact versions; the exact command
  that produced each table or figure; expected output files with md5s; wall-clock run time.
- Every file **≤ 10 MB** (the Drive connector's cap); split larger files and say so in the manifest.
- **A run the gate can bank:** this build runs each instrument under a 280 s timeout. Where the full
  chain runs longer, deliver the full outputs with md5s **and** a reduced validation case that finishes
  in under 200 s (a few Z, or one Z from a stored converged field) exercising the same code path.
- **"Not held" is an answer.** If an object was never a file, say so; the book then labels that figure
  record-carried and re-derives it as a labelled reconstruction.

## The objects, by the claim each one witnesses

1. **The entrant operator — the SCF chain code (register 1701, §35.1).** The scalar-relativistic
   Koelling–Harmon atomic solver; the frontier-channel scan in the frozen field of the ion
   (Z, cfg(Z−1)); the chaining driver Z = 2–120; every module it imports; c = 137.035999 where it is
   declared; the grid, convergence and frozen-field conventions as code, not prose.
2. **Λ_chain, the chain as measured (1702).** The 119-row table Z = 2–120 — entrant, D_ent, margin,
   full candidate spectrum — as the run wrote it; the run log; the **scorer** that returns 107 of 107
   with its definition of a hit; the twelve unwitnessed rows (109–120) marked as such.
3. **`ground.py` (1306).** NIST ASD 5.12 GSIE, Z = 1–108, ground shells and ground level, with the
   retrieval record (ASD version, date, query). This build reconstructed the table in r2-ch16y §3 and
   validated it against every Register anchor; the original settles reconstruction against record.
4. **The prediction-first artefacts (1702).** The hashed predictions — inequality, direction,
   tolerance — as hashed before arithmetic, and the checker that verified them.
5. **Λ_cinf, the c → ∞ counterfactual (1706).** The 107-row table, the run parameters, and the code
   path that takes c to infinity (the eleven elements: Mn, Zn, Ag, Cd, Nd, Pm, Sm, Lu, Hg, Lr, Rf).
6. **The collapse criterion at the f openings (1703, §35.3).** The double-well collapse computation
   and its output at La, Ac and Th, and at the rows where it did not fire.
7. **The g channels (1704).** The walk's 5g/6g/7g/8g values across Z with the −1/(2n²) comparison
   (spread ≤ 1e-5 over 65 / 70 / 57 / 28 elements).
8. **The correlation clause (1705).** The second-order code — entrant pairs, core–core closure, the
   near-degenerate block resummed with the configuration gap — and its outputs at Z = 38, 56, 72, 89,
   105: dm2/margin, the envelopes, the per-row instrument biases.
9. **The audit of the instrument (1707–1711).** The Hellmann–Feynman-in-q discrepancy (the Pulay
   term); the Löwdin 1950 identity check (4/4, worst 2.6e-15); the exact-quartic Hessian extraction
   (five evaluations); the chord = rot + perp decomposition with the Gerratt–Mills first-order
   response — code and outputs for each.
10. **Z = 109–120 (1712).** The margins 0.058–0.264 Ha and the spin-orbit worst case 0.083 Ha — code
    and outputs.
11. **The six figures** (FIG1 filling index 2–120, FIG2 spectra index 2–120, FIG3 j-120 window, FIG4
    dm2 widening, FIG5 spectra index 3D, FIG6 relativistic vs non-relativistic): the plotting scripts
    and the data files they read.
12. **The paper and the project's own record.** The final `THE-LOWDIN-SOLUTION.md` as concluded, with
    its md5 (this build holds a 260-line member; a difference is a finding). The project's register or
    working register **with timestamps** — the book seated the Löwdin entries as 1701–1712 and the
    three-body entries after them as 1713–1724, and the timestamps settle any competing numbering. Its
    final handoff and its rulings.

## What this build does with the delivery

Each object enters the compendia bundle only through a guarded build with a Register entry in the
same build; each instrument gets a validation block against the Register's own anchors and a banked
golden; where the full run cannot bank, the outputs are banked by md5 and the reduced case witnesses
the code path. Deviations between a delivered output and a printed figure are recorded as findings
of R2 and flagged for R3 — they are not put back to the Löwdin project as questions.
