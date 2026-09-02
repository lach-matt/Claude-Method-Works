# REQUEST — THE METHOD 1.6 BUILD (chat 128; BUILD90 main, BUILD157 compendia) TO THE THREE-BODY PROJECT

**Date:** 2026-09-01. **Deliver to:** the Materials folder `1XX_5f3PZB6tjRtiZ2GIgd8Tt7i_4GgkY`, in a
subfolder **`THREEBODY-DELIVERY-1/`**. **Baseline:** both projects worked from the Prints & Proofs
folder `1vYctzLppUZ2vFPJDCZ6wvkgSdj3v_f6n`; the original this build reads is `The Method 1.6.md`,
738,550 B, md5 `49900cf41f818ab789bb90fc596ac977`.

## Why

Every figure in the book is to be recomputed by an instrument that travels with the build, validated
against a witnessed anchor and banked as a golden. Chapter 36 and Register entries 1713–1724 print
figures the build cannot re-run: the record names `tb_audit.py` (1756) and `3B.tri` (1716), and holds
neither. This is a request for the work as it was done, not for it to be redone.

## Form of delivery (applies to every item)

- Files **as produced** — never retyped or reformatted; Drive may add a `-1` suffix, the md5 decides.
- A **`MANIFEST.tsv`**: `name  bytes  md5  purpose` for every file.
- A **`README.md`**: Python / NumPy / SciPy / SymPy and any other library with exact versions; the
  exact command for each table and figure; expected outputs with md5s; run times.
- Every file **≤ 10 MB**; split larger files and say so.
- **A run the gate can bank:** instruments run under a 280 s timeout here. Where a run is longer,
  deliver the full outputs with md5s **and** a reduced case under 200 s on the same code path.
- **"Not held" is an answer.** If an object was never a file, say so; the book then labels the figure
  record-carried and re-derives it as a labelled reconstruction.

## The objects, by the claim each one witnesses

1. **`tb_audit.py` (1756; §36.2; the paper's §8 audit paragraph).** The six checks A–F over the
   thirteen mass order-types, 78 of 78; its inputs; its output log; the definition of the thirteen
   order-types and the symmetry orders 6, 2, 1 by coincident masses (1717).
2. **The triangle-form closure at caps 3–12 (1716).** `3B.tri` and the instrument that computes the
   join and meet closures on it — 344 cells, 0 join failures, 8,385 meet failures at cap 8; the
   per-cap table for caps 3–12; the two-body chain (0). The book's own closure operator is
   `tower-2.py`; state whether the project's closure is that operator or its own.
3. **The norm N₈ (1719, 1720).** The code that computes Lagrange's resolvent norm over (ℤ/2)³; the
   withdrawn degree-8 polynomial with its coefficients as first written; the second-route check
   (register 784's protocol) that caught the U⁴ and U² terms.
4. **The shape-potential audit, both states (1718, 1722, 1723).** The first run that failed check A
   13 of 13 and the corrected run — both logs, since the record keeps both states; the line where the
   hyper-radius division was carried in and the line where it was removed; the Montgomery c_ij/d_ij
   normalisation used.
5. **Mass-uniformity (§36.4, the law the chapter adds).** Whatever verifies that every mass-dependent
   quantity enters through c_ij = (m_i m_j)^{3/2}/√(m_i + m_j) and the three collision rays b_ij, and
   that the manifold, the metric, the norm polynomial and the constraint graph are mass-free — code
   if it exists, the derivation if it does not.
6. **The stratification as an index (1713, 1714).** The five asymptotic classes of ℳ_{E,L} as data —
   the object E(𝔉) = 0 was computed on — and the computation of E on it; the Brudno step (§25.6).
7. **The five points and the threshold (§36.3).** Euler's three collinear roots and Lagrange's two
   equilateral points for the mass triples used; the source of the L4/L5 stability threshold
   μ < 0.0385209 (Routh) as cited or as computed.
8. **The eight attribution questions (1721; §E.5, audit 7).** The residue-to-question ledger as
   formed before deriving, the seven closures with their sources (Montgomery, Saari, Painlevé,
   Moore / Chenciner–Montgomery, Maupertuis / Jacobi, Alekseev / Moser, Monaghan / Stone–Leigh / Kol,
   Brudno, Hill / …), and the eighth's closure to Lagrange 1770.
9. **The five figures** (shape sphere, closure defect, tower, equator potential, constraint graphs):
   the plotting scripts and the data they read.
10. **The paper and the project's own record.** The final `The_Three_Body_Problem_for_Unknown_Masses`
    source as concluded, with its md5 (this build holds a 215-line member; a difference is a finding).
    The project's register or working register **with timestamps** — the three-body work concluded
    after the Löwdin work, and the book seated its entries as 1713–1724 after Löwdin's 1701–1712; the
    timestamps settle any competing numbering. Its final handoff and its rulings.

## What this build does with the delivery

Each object enters the compendia bundle only through a guarded build with a Register entry in the
same build; each instrument gets a validation block against the Register's own anchors and a banked
golden; where the full run cannot bank, outputs are banked by md5 and the reduced case witnesses the
code path. Deviations between a delivered output and a printed figure are recorded as R2 findings
and flagged for R3 — never put back to the three-body project as questions.
