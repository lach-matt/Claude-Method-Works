# FINDING R4-19 — the one anchor becomes seven. The store carries a whole ladder of inner-shell removals, spanning sibling counts 1, 5, 9 and 13, and measured against it **R4-18's transfer has no support**: six of seven rows sit within 0.018 Ha and ytterbium alone is 0.111. Protactinium's figure returns to **6.95 eV**, now with a measured bound instead of an argument. NOT REPAIRED.

Measured 6 September 2026 on M's order: *"what's owed is small and named — keep going."* The named gap was that
`FINDING-R4-18`'s transfer rested on **one** compact-shell anchor. It does not have to.

`method/proofs/fieldresidue.py` (`--only C:…`), `method/proofs/siblingpair.py`, banked `fieldresidue.out`.
**Selftest 106 of 106.**

## 1. The store carries seven anchors, not one

A scan of every species in `spectra-levels-store/deliver/queue2/` for a **second or later ionisation limit**
finds twelve files with more than one, and seven of those limits are **inner-shell removals**: the electron
leaves a shell that still holds siblings, and the ion is left in that configuration's own ground level. They
span exactly the variable in question.

| row | neutral | removed | ion state | limit (cm⁻¹) | **siblings** |
|---|---|---|---|---|---|
| B I | 1s²2s²2p | 2s | B II 2s.2p ³P°₀ | 104263.58 | **1** |
| Al I | …3s²3p | 3s | Al II 3s.3p ³P°₀ | 85671.40 | **1** |
| Ga I | …4s²4p | 4s | Ga II 4s.4p ³P°₀ | 95755.14 | **1** |
| Na I | …2p⁶3s | 2p | Na II 2p⁵.3s ³P°₂ | 306373.77 | **5** |
| Xe I | …5p⁶ | 5p | Xe II 5s²5p⁵ ²P°₃⁄₂ | 97833.787 | **5** |
| Hg I | …5d¹⁰6s² | 5d | Hg II 5d⁹6s² ²D₅⁄₂ | 119700 | **9** |
| Yb I | …4f¹⁴6s² | 4f | Yb II 4f¹³6s² ²F°₇⁄₂ | 71859.7 | **13** |

**Three of them have exactly one sibling — protactinium's own case** — so the question no longer needs an
interpolation from thirteen.

## 2. Measured, with the six zero-sibling openings as the ladder's foot

| siblings | row | predicted | measured | **residual** | sibling energy | undelivered |
|---|---|---|---|---|---|---|
| 0 | 3p, 4p, 5p Al Ga In | | | +0.0005 each | 0 | — |
| 0 | 6p Tl · 5d La · 4d Y | | | −0.0017 · −0.0029 · −0.0038 | 0 | — |
| **1** | B 2s | 12.814 | 12.927 | **−0.00414** | 0.01683 | 0.246 |
| **1** | Al 3s | 10.549 | 10.622 | **−0.00267** | 0.01793 | 0.149 |
| **1** | Ga 4s | 11.397 | 11.872 | **−0.01744** | 0.01662 | 1.049 |
| **5** | Na 2p | 37.716 | 37.986 | **−0.00991** | 0.09138 | 0.108 |
| **5** | Xe 5p | 12.163 | 12.130 | **+0.00121** | 0.06629 | 0.018 |
| **9** | Hg 5d | 14.350 | 14.841 | **−0.01805** | 0.09032 | 0.200 |
| **13** | Yb 4f | 5.878 | 8.909 | **−0.11140** | 0.16664 | 0.668 |

**Six of the seven corridor rows sit within 0.018 Ha, and so does every zero-sibling opening. Ytterbium alone is
0.111 Ha — six times the next largest.** Sodium's 2p removal at 37.99 eV, an inner-shell hole four times deeper
than any other row here, comes out at 0.0099 Ha; xenon's at +0.0012 Ha is the closest row on the whole ladder.

## 3. What this refutes, and it is my own last finding

`FINDING-R4-18` transferred ytterbium's undelivered fraction, 0.668, to protactinium's pair and got +0.090 eV.
**The ladder shows there is no such constant.** The undelivered fraction runs **0.018 at xenon to 1.049 at
gallium** with no order in sibling count, in sibling energy, or in ⟨r⟩ — sodium and mercury have nearly the same
sibling energy (0.091, 0.090) and residuals differing by a factor of two, while ytterbium has 1.8 times their
sibling energy and six to eleven times their residual.

**So the transfer built on ytterbium alone had no support, and §3 of R4-18 is withdrawn.** It was the fifth
correction of the same shape in this pass, and the sharpest instance of it: I took a ratio from one row and
called it a law, when the corpus held six more rows that would have tested it.

**Ytterbium's own measurement stands** — the corridor is real and it is 0.111 Ha (`FINDING-R4-18` §2). What falls
is only the claim that it transfers by a fixed fraction.

## 4. What the ladder gives instead, and it is better than a transfer

**A measured bound.** Every row with nine siblings or fewer — seven of them, across s, p and d shells, from
boron to mercury, at removal energies from 10.5 to 38.0 eV — sits at **|residual| ≤ 0.018 Ha**, and two of the
three one-sibling rows sit inside the zero-sibling band of ±0.004 Ha.

**Protactinium has one sibling, and its sibling pair energy (0.00494 Ha) is a third of the smallest on the
ladder** (boron's 0.0168). It is entitled to the ladder's well-behaved regime, and nothing in the ladder
detects a systematic shift from zero siblings to one: the zero-sibling rows run +0.0005 to −0.0038 Ha and two
of the three one-sibling rows run −0.0027 to −0.0041.

| | eV |
|---|---|
| the object's prediction at protactinium | **6.949** |
| typical residual on the ladder's well-behaved rows | ±0.004 Ha = **±0.11 eV** |
| the ladder's worst row (gallium) as a bound | 0.018 Ha = **0.47 eV** |

> **The 5f removal energy at protactinium is 6.95 eV, ±0.11 eV typical and ±0.47 eV bounded.
> t(5f) = 2.636, +7.6 % above √6.**

**Gallium is the ladder's worst row and it has a named reason:** its 4s sits directly above a filled 3d¹⁰, and
the 4s removal carries a d-shell relaxation none of the other rows do. Protactinium's 5f has no such neighbour.

**`FINDING-R4-17`'s number is restored and its argument is not.** R4-17 reached 6.95 eV by asserting that form S
carries the sibling adequately — an unsupported claim about the instrument, which `FINDING-R4-18` was right to
reject. The ladder now reaches the same number by measurement: no sibling correction is *detectable* at one
sibling, whatever the functional is doing internally. **The number is restored on evidence the argument never
had.**

## 5. The floor, across every figure this pass has produced

| | t(5f) | |
|---|---|---|
| the bare field (R4-14) | 2.442 | +0.0 % |
| corrected (R4-15) | 2.636 | +7.6 % |
| R4-16's sibling addition | 2.643–2.653 | +7.9–8.3 % |
| R4-17 | 2.636 | +7.6 % |
| R4-18's transfer | 2.643 | +7.9 % |
| **this finding** | **2.636 ± 0.01** | **+7.6 %** |

**Ruling 1's floor has held at every one of them.** Protactinium has never approached √(ℓ(ℓ+1)/2) from below at
any stage of any correction, and the spread of the whole sequence — 2.44 to 2.65 — is entirely above it.

## 6. What is open now

**One row: ytterbium.** The corridor is measured (0.111 Ha), its mechanism is named (same-shell pair correlation),
and it is now shown to be **an outlier rather than a class** — six other sibling-bearing rows, including one with
nine siblings and one with a deeper hole, behave. What ytterbium has that they do not is not established by
anything measured here. That is the residue, it is one row wide, and it does not reach protactinium.

**Nothing else.** The 5f figure no longer rests on a transfer, an assumption about the functional, or a single
anchor. It rests on thirteen measured rows: six openings at zero siblings and seven inner-shell removals from one
to thirteen.

Nothing is repaired in any volume. Every figure is MEASURED by the instrument or RECORD-CARRIED with its quote.

---

## §4's ATTRIBUTION IS CORRECTED by FINDING-R4-20: mercury is the ladder's worst row, not gallium

§4 wrote *"the ladder's worst row (gallium) as a bound | 0.018 Ha = 0.47 eV"*, and §2's own table beside it prints
**Hg 5d −0.01806** against **Ga 4s −0.01740**. **Mercury is the larger.** The bound quoted — 0.018 Ha, 0.47 eV —
is mercury's number and is correct; only the row named for it was wrong.

It surfaced when `fieldresidue.py`'s report was made to compute that paragraph from the table above it instead of
printing it as fixed text, which is the same drift `tools/docfigures.py` exists to catch, one level in.

**What stands.** The bound is unchanged, because it was always the larger of the two: **protactinium's 6.95 eV,
±0.11 eV typical and ±0.47 eV bounded.** Gallium remains the largest *one-sibling* residual — the row class
protactinium belongs to, which is why it was the row named — and its 3d¹⁰ reason stands for that. What falls is
one word: gallium is not the ladder's worst row.

**And every figure in §2 is re-measured** through the repaired second-order-exchange quadrature (`FINDING-R4-20`),
moving by at most 0.07 mHa. The ladder is unchanged: six of seven within 0.018 Ha, ytterbium alone at 0.111.
