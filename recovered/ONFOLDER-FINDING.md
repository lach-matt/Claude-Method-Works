# WHAT THE FOLDER ANSWERS WITHOUT A FETCH

*M's instruction: review everything in the working project folder before fetching outside.
Computed by `onbank.py` and two inline scripts, from `COORDINATES-2_13.csv` (grade `measured`
only, 358 rows on 75 species). No fetch attempted. No computed-grade value read as evidence.
Nothing written to any index, register or artefact.*

---

## 0 · A convention audited before it was used

**`charge` in `COORDINATES.tsv` is 1-based — it is the SPECTRUM NUMBER, not the ion charge.**
charge = 1 is the neutral atom; Ra II is charge 2. My first pass queried charge = 0 for neutrals,
got zero rows, and was one keystroke from reporting *"Rb I, Fr I and Rn I are absent from the
index"* — a negative that would have been a statement about my query. R 1672's clause, fired.
The convention is consistent with the index's own arithmetic: charge runs 1…Z, so
Σ_{Z=1..120} Z = 7,260 pairs.

## 1 · The instrument reproduces

Bridge Finding III reported facets 1–2 at Cs I as −1.308, −3.281. Recomputed from
`COORDINATES-2_13.csv`: **−1.30781, −3.28301**. Ba II: −0.83270, −2.13390.

## 2 · THE DIAGONAL MAP MAKES FACETS 1 AND 4 ONE INEQUALITY

On a Madelung diagonal M = n + ℓ, p = n − ℓ − 1 = **M − 2ℓ − 1**, so ℓ alone fixes p and
consecutive ℓ steps p by two. Therefore:

| M parity | ℓ = 3, 2, 1, 0 maps to | facets living there |
|---|---|---|
| **M odd** (7) | p = 0, 2, 4, 6 | facets 1, 2 |
| **M even** (8) | p = 1, 3, 5, 7 | facets 4, 5 |

Written in the channel defects δ(ℓ) of one closed core:

    facet 1  =  facet 4  =  δ(f) − 2δ(d) + δ(p)
    facet 2  =            2δ(f) − 3δ(d) + δ(s)
    facet 5  =            δ(d) − 2δ(p) + δ(s)
    facet 3  =  the one chord that mixes parities — the cross-diagonal, as Finding II said

**Facets 1 and 4 are the same functional of the same four numbers, read on diagonals of
opposite parity.** Five facets, four distinct diagonal conditions.

**Consequence for the board.** Open item 2 read *"facets 4–5 UNTESTED — no measured d/f channel
for the Rn core."* Under the diagonal map, facets 4–5 need no Rn core: they need any species with
measured δ at ℓ = 0, 1, 2, 3. **The folder holds 43 such species.** The Rn-core instance is a
separate question and remains open; the facets themselves are not blocked on it.

## 3 · Facets 4 and 5, measured — 43 species

    facet 1 / facet 4   satisfied 10 / 43
    facet 2             satisfied 13 / 43
    facet 5             satisfied 31 / 43

Hg II carries all four channels and satisfies both M=8 facets: **facet 4 −0.86980,
facet 5 −0.57840** (v₁ 1.06220 · v₃ 2.87580 · v₅ 3.81960 · v₇ 4.18500, all four n inside the
compendium's stated n-ranges for that species).

**The 10/43 is a POOLED number and must not be read as a rate.** The population contains two
domains — hydrogenic light species where δ(d) and δ(f) are both ≈ 0, and heavy species where the
d channel has collapsed. Finding III's five cores are all of the second kind. Pooling them is the
operation this project forbids.

## 4 · Where facet 1/4 is satisfied, the d channel has collapsed

    facet 1/4 SATISFIED (n=10)   δ(d) median 1.8942   range 0.0014 – 2.8758
    facet 1/4 VIOLATED  (n=33)   δ(d) median 0.0772   range 0.0002 – 0.8917
    best single threshold on δ(d): 41 / 43

The two misses are hydrogenic rows (Li III, Be IV) whose facet value is at the 10⁻⁴ level — they
satisfy by rounding, not by shape. The smallest δ(d) among true satisfiers is **0.6202 — Ti IV**,
which is the exact value `SPECTRA.md` §"The Janet collapse" uses as its own boundary example.

**Stated as measured, not as a condition.** This is an association on 43 species with a threshold
accuracy, and P1-FINDING §2 records what happens when an enrichment of this kind is promoted to a
condition. What it does is connect Finding I's facets to an object already in the compendium: the
collapse threshold is a **Janet block boundary read from the periodic table and not fitted**
(R 1657), so the facet condition may be carried by a coordinate the index already holds.

## 5 · What is genuinely missing, named exactly

| want | on disk | missing |
|---|---|---|
| Rn-core M=8 diagonal | **Fr I** measured δ(s) 5.07221, δ(p) 4.59521 | δ(d) → facet 5; δ(d)+δ(f) → facet 4 |
| Ra II, Ac III | 8 rows each, **all computed** | every measured channel |
| facet 3 at Tl I | δ(s) 4.75066, δ(d) 3.11838, δ(f) 1.03131 | δ(p) — computed grade only |

**Before any NIST call: the bank already holds `spectra_raw/queue2/FrI.tsv` (3,332 bytes),
`RaI.tsv`, `AcI.tsv`, `RnI.tsv`, `TlI.tsv`, `HgI.tsv`, `PbI.tsv`.** Fr I reached the index with
two channels of the four its raw table may contain — which is the FLAG 1 pattern exactly
(Rb I: captured at R 1258, promoted for Sr II, not for Rb I). **A missing index row is not
evidence of a missing measurement.** The next act is to read `FrI.tsv`, not to query ASD.

## 6 · Not read, and named rather than glossed

`REGISTER-2_13.txt` (13,543 lines) consulted by targeted query only — collapse, R 1699/1700,
entry count. `The_Method_1_6-10.pdf` is **UTF-8 text, 11,108 lines**, not a PDF (R 1702), and is
the book Parts II–VII that every bridge names as unread — it is present and extractable in this
chat. `The_Register-4.pdf` likewise, 12,032 lines. The four compendium files are **zip archives
of page rasters** and carry no extractable text. `SPECTRA-2_13.txt` §II read as a table
(596 channels, 105 species) and not line by line; §III–IV not read.
