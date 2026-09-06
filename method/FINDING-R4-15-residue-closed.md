# FINDING R4-15 — the residue closes. The field's shortfall at an opening is correlation plus spin-orbit, computed from the corpus's own instruments with no fitted constant, and the corrected removal energy lands on the corpus's own measurements to half a millihartree at p. The 5f binding at protactinium follows. And R4-14's headline is WITHDRAWN. NOT REPAIRED.

Measured 6 September 2026, on M's ruling: *"you just gave the path to the solution … this is residue of the
last open question, thus the question is still open … so much math was done … much layeth within the repo.
let's solve this properly and close it so we may move on."*

`method/proofs/fieldresidue.py`, its banked output `fieldresidue.out`, the field file `fieldresidue-field.json`
and the correlation tables `fieldresidue-tables.json`. **Selftest 106 of 106.**

## 1. What the residue was, and that the record had already built both halves of it

R4-14 measured the ruling field's removal energy at every two-sided opening and found it **underbinds** the
observed removal energy by about half an electron-volt, naming the two causes: the field is average-of-configuration
scalar-relativistic Hartree–Fock with **no correlation and no spin–orbit** (`FINDING-CHAIN-SESSION-40` §7:
*"No terms, no SO, no correlation … No constant beyond c"*). It then treated that as a limit.

**It is not a limit. The Löwdin work built both corrections, and they are in this repository.**

- **Correlation.** Sessions 21–34 built a functional with **no fitted constant**, and derived in-project the two
  pieces the published high-density series leaves open: the ring constant c₀(ζ) from the RPA ring integral
  (`ring_zeta.py`, `FINDING-GB-ZETA-RING-SESSION-23`), and the second-order exchange — bare
  E0B = 0.0241792 Ha (Onsager–Mittag–Stephen 1966), then **statically screened by the ring's own Lindhard
  function** (`sox_qres.py`, `sox_scr.py`, `FINDING-SOSEX-SESSION-32`). The standing form is **S**,
  ε_c^S = ε_ring/2 + ε_2x^scr (`FINDING-FRACHFS5-SESSION-34`, `FINDING-HFCORR-SESSION-37`), applied with a
  Perdew–Zunger orbital self-interaction correction and the session-28 cell-cut rule for the ε_c < 0 domain.
- **Spin–orbit.** Session 19 built the first-order Landé term and **session 94 carried it onto this very field**
  (`so94.py`): ζ_nl = (α²/2)⟨P|(1/r)dV/dr|P⟩ on hfc2's own local potential, ΔSO = ζ(2ℓ+1)/2. The record scored it
  against published relativistic data — *"E113 7p3/2 − 7p1/2 = 24758 cm⁻¹ = 0.1128 Ha; so94 first-order
  Delta_SO(113) = 0.1176 Ha (+4.2 %)"* (`LEDGER-J-S94-V5-PRIOR-ART.md:8`). **ζ here is `so94.zeta` verbatim.**
- **Terms.** Session 27 built the Hund-ground-term correction on top of the configuration average (`hfterm.py`).

**What the record never did was run any of it at a p opening, at the 5f opening, or read t from it.**

## 2. The correlation form rebuilt, and certified twice

Regenerated from the record's own generators, loaded by path, nothing under `recovered/` edited.

**The derived ring constant reproduces exactly, at every ζ the record printed:**

| ζ | here | `FINDING-GB-ZETA-RING-SESSION-23` |
|---|---|---|
| 0.0 | −0.07115 | −0.07115 |
| 0.4 | −0.06824 | −0.06824 |
| 0.6 | −0.06436 | −0.06436 |
| 0.8 | −0.05828 | −0.05828 |
| 0.9 | −0.05399 | −0.05399 |
| 1.0 | −0.04991 | −0.04991 |

(ζ = 1 is where the printed Eq. 16 evaluates 0·log 0 and returns nan; its limit is exactly half of c_L(0), which is
the record's own PZ5. Taken as the limit, not as a change to the formula.)

**And the correlated ΔSCF reproduces every sealed row of the standing form S:**

| | D_HF | ΔEc here | sealed (`FINDING-FRACHFS5-SESSION-34`) | diff |
|---|---|---|---|---|
| Sc 3d | 0.26664 | −0.03188 | −0.03188 | −0.00000 |
| Y 4d | 0.19561 | −0.02747 | −0.02747 | +0.00000 |
| La 5d | 0.20585 | −0.02619 | −0.02618 | −0.00001 |
| Lu 5d | 0.15979 | −0.02696 | −0.02696 | −0.00000 |
| Cs 6s | 0.12779 | −0.00675 | −0.00675 | −0.00000 |

**Five of five.** The form here is the record's form.

## 3. The gates are the corpus's own measurements, not the corpus's own opinions

`extracted/archives/spectra-levels-store/deliver/` holds NIST level lists captured by the spectra work. Two
quantities come out of them at six of the seven openings, and both are measurements:

- **the entrant's fine-structure interval** — Al I 112.061, Ga I 826.190, In I 2212.599, Tl I 7792.7,
  Y I 530.351, La I 1053.164 cm⁻¹ — which fixes the measured ζ;
- **the entrant's own removal energy**, as the series limit to the closed-shell ion — Al II 3s² 48278.480,
  Ga II 4s² 48387.634, In II 5s² 46670.107, Tl II 6s² 49266.66, Y II 5s² 50145.6, La II 6s² **52376** cm⁻¹.

**The La anchor is worth its own sentence.** Lanthanum's *first* ionisation energy removes a 6s electron, so
register 1337's 5d reading is of the wrong electron. The store carries the La II 6s² ¹S₀ limit at 52376 cm⁻¹,
which is the **5d electron's own removal**, and this is the first time the right number has been read at that
opening. At yttrium the first IE already is the 4d removal (Y II's ground *is* 5s²), so nothing moves there.

## 4. Measured: the residue is correlation plus spin–orbit, and it closes

All energies eV; the residual is (predicted − measured) at the actual ground level.

| opening | field | field deficit | correlation supplies | + spin–orbit | predicted | measured | **residual** |
|---|---|---|---|---|---|---|---|
| **3p Al** | 5.489 | −0.488 | +0.507 | +0.008 | 5.999 | 5.986 | **+0.0136** (+0.50 mHa) |
| **4p Ga** | 5.444 | −0.487 | +0.513 | +0.062 | 6.013 | 5.999 | **+0.0142** (+0.52 mHa) |
| **5p In** | 5.125 | −0.479 | +0.508 | +0.175 | 5.800 | 5.786 | **+0.0141** (+0.52 mHa) |
| 6p Tl | 4.880 | −0.584 | +0.498 | +0.692 | 6.061 | 6.108 | −0.0473 (−1.74 mHa) |
| 4d Y | 5.323 | −0.855 | +0.748 | +0.049 | 6.114 | 6.217 | −0.1036 (−3.81 mHa) |
| 5d La | 5.601 | −0.814 | +0.713 | +0.107 | 6.415 | 6.494 | −0.0788 (−2.90 mHa) |

**The three light p openings close to +0.50, +0.52, +0.52 mHa — flat to two hundredths of a millihartree across
Z = 13 to 49.** The field's half-electron-volt deficit is correlation, quantitatively: it supplies +0.507, +0.513,
+0.508 eV against a deficit of 0.488, 0.487, 0.479. Nothing in that chain is fitted.

The other three are larger and their causes are named, not guessed. **6p** at −1.74 mHa is thallium, where the
scalar field's j-average and a first-order Landé term cannot carry a 0.69 eV splitting — ζ there measures 1.075 of
the true interval, the only opening where first order runs high at p. **The two d rows** at −3.8 and −2.9 mHa are
under-bound by the same class-flat amount the record found on its own d rows, and ζ overestimates the d splitting
by 24 % and 36 % — first order on a scalar field, which the measured intervals expose and which no correction here
claims to fix.

**ζ against the store, all six:** 0.910, 0.914, 0.955, 1.075 at 3p 4p 5p 6p; 1.237, 1.360 at 4d 5d. Low at p, high
at d. Recorded, not repaired.

## 5. The 5f binding energy at protactinium, from an object certified at six openings

Protactinium has **no anchor in the corpus** — every Z = 91 row of the survey is *computed, unwitnessed*, and the
store holds no Pa level list. What follows is therefore the prediction of the object the six openings certify.

| | Ha | eV |
|---|---|---|
| D_HF, the 5f removal from the observed ground 5f² 6d¹ 7s² | +0.18054 | 4.913 |
| correlation, ΔEc^S | −0.03270 | +0.890 |
| Hund term (neutral ⁴K −0.05991, ion ³H −0.01949) | +0.04042 | +1.100 |
| spin–orbit (neutral −0.02900, ion −0.02712) | +0.00188 | +0.051 |
| **predicted 5f removal energy** | **+0.25536** | **6.949** |

ζ(5f) = 1631.5 cm⁻¹ and ζ(6d) = 1490.9 cm⁻¹ in the neutral; 1848.0 and 2188.5 in the ion.

**The one piece no anchored opening tests is the term correction**, because every other opening has a single open
electron and no term splitting at all — and at Pa it is the largest single correction, +1.10 eV of the +2.04 eV
total. It has one gate and it is a good one: **the Hund highest-weight construction reproduces the ground term
symbol the seated member records at 103 of the 104 elements that carry one** — Pa's own **⁴K11/2** among them —
and its single exception is **cerium**, where the observed ¹G°₄ is famously not the Hund term of 4f 5d 6s².
Without the term correction the prediction is 5.849 eV. **The honest statement is the bracket: 5.849 to 6.949 eV.**

## 6. And now the correction to my own work: R4-14's headline is WITHDRAWN

R4-14 read t on the bare field and reported that *"with the entrant's own electron the entry point sits at
√(ℓ(ℓ+1)/2) within one percent at p, d and f alike"* — p −0.75 %, d +0.58 %, f −0.30 %.

**That agreement was the field's error standing in for the law's excess.** The bare field underbinds by half an
electron-volt at p and by 0.8 eV at d; correcting it moves every t up, and the excess returns:

| | field (R4-14) | + correlation | predicted | **measured** |
|---|---|---|---|---|
| p, four openings | −0.75 % | +2.75 % | +4.05 % | **+4.04 %** |
| d, two openings | +0.58 % | +4.55 % | +4.93 % | **+5.37 %** |
| f, one opening | −0.31 % | +3.65 % | +7.61 % | — |

**And the certification is that the predicted column reproduces the measured column**, opening by opening:
1.0937/1.0925 at 3p, 1.0338/1.0331 at 4p, 1.0131/1.0124 at 5p, 1.0213/1.0237 at 6p, 1.8361/1.8453 at 4d,
1.7986/1.8049 at 5d. The object predicts t. R4-14's f value of 2.4420 (−0.3 %) is superseded by **2.6359 (+7.6 %)**,
or 2.5437 (+3.8 %) without the term correction.

**So register 1337's *"not derived: a common factor of 1.029, both p and d 2.9 % high"* is confirmed as a real
feature of measurement.** It is not an artefact of reading the wrong electron, and no correction the corpus holds
removes it — every correction makes it larger. Two things about it are now measured that were not:

1. **It is not common: it grows with ℓ.** On measurement, +4.04 % at p and +5.37 % at d; predicted +7.61 % at f.
   Three cells, one number each — reported ordinally, as register 1355 requires of exactly this shape, and **not
   fitted**: the domain protocol (register 1339) blocks a fit on three points.
2. **Reading the right electron makes it bigger, not smaller.** The d figure moves from +3.04 % to +5.37 %
   precisely because the store's La II 6s² limit binds the 5d electron deeper than lanthanum's first ionisation
   energy does. R4-13 supposed the wrong electron was inflating the f point; at d, the wrong electron was
   *deflating* the excess.

## 7. What this closes, and the one thing it makes into a bound

**Closed.** The residue is named, computed and measured: the ruling field's shortfall at an opening is correlation
(≈ 0.5 eV at p, ≈ 0.75 eV at d) plus spin–orbit (0.008 to 0.69 eV), both from the corpus's own instruments with no
fitted constant, and the sum lands on the corpus's own measured removal energy — to half a millihartree at 3p, 4p
and 5p, to 1.7 mHa at 6p, and to 3–4 mHa at the two d openings. R4-13's *"what would close it, and none of it is
here"* is answered: all of it was here.

**And the excess itself becomes a bound rather than a discrepancy.** Read on the actual ground level — which is
what an ionisation energy is — **t is above √(ℓ(ℓ+1)/2) at every one of the six measured openings**, 1.0925,
1.0331, 1.0124, 1.0237, 1.0654, 1.0421, and above it on the certified object at all seven including Pa. Six of six
measured, seven of seven computed, none below. **The form is a floor, approached from above** — which is what
§34.7 already says of it along n (*"a limit approached along n, not a constant"*), now measured along ℓ as well.
On configuration centroids rather than ground levels the statement weakens: 6p falls 1.1 % below. Stated both ways.

## 8. What is owed to M, and none of it is done

1. **§34.7 and register 1337 print t as a value with a 2.9 % excess "not derived".** The excess is now measured on
   the right electron at six openings, is not common, grows with ℓ, and is one-signed. Whether the volume says
   *the form is a floor* is M's ruling, not mine.
2. **The La 5d reading is wrong in register 1334/1337** — it is lanthanum's first ionisation energy, which removes
   a 6s electron. The store carries the right number (La II 6s² ¹S₀, 52376 cm⁻¹, t = 1.8049). Recorded, not repaired.
3. **The 5f prediction is a bracket, 5.849–6.949 eV**, because the term correction has no anchored opening. If M
   wants it narrowed, the route exists: an opening with two open shells whose removal the store measures.
4. **Three reconstruction limits are recorded, not repaired**: the g_2b quadrature runs 1.0 % low at the recovered
   defaults (measured by doubling the grid: +0.69 % at q = 0.516), which the sealed ΔEc rows show costs nothing on
   the O path; first-order Landé ζ is 9 % low at p and 36 % high at 5d; and `t7c_cuaudit.py` is still absent, its
   S-form potential rebuilt here from `corr_ring.py`'s interface.

Nothing is repaired in any volume. Every figure is MEASURED by the instrument or RECORD-CARRIED with its quote.
