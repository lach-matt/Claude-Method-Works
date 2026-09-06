# FACET 5 CLOSES ON THE Rn CORE — FROM THE BANK, WITHOUT A FETCH

*Bank `restore-point-2_13.tar.gz` verified by hash against `BANK-2_13-MANIFEST.txt`:
`8057709403ed2c795cc753f74e68b2cbfc3aeb9c67f45e7c0e38b3129fd857a5`, 708 entries
(694 files + 14 dirs). Ten files extracted, nothing else read. Nothing written to the
register, the store, `COORDINATES.tsv` or any generated artefact.*

---

## 1 · The premise of board item 2 was false, and the store says so

Bridge §9 item 2: *"Facets 4–5 by measurement. Needs measured d and f channels on the Rn core:
Fr I (unlikely in ASD), Ra II, Ac III."*

**`MEASUREMENTS.tsv` already holds Fr I's d channel.** Three Fr I series are in the store:

    Z=87 charge=1  l=0  2S   delta 5.07221  spread 0.10117  n  7–30  members 24
    Z=87 charge=1  l=1  2P*  delta 4.59521  spread 0.19183  n  7–30  members 48
    Z=87 charge=1  l=2  2D   delta 3.42371  spread 2.38116  n  6–30  members 50

`COORDINATES.tsv` carries **only ℓ = 0 and ℓ = 1** for Fr I as measured. **The d channel was
measured, stored, and never promoted to the index** — FLAG 1's pattern, second instance
(Rb I, R 1258, was the first). *A missing index row is not evidence of a missing measurement,
and "unlikely in ASD" was a guess where the file was on disk.*

## 2 · Reproduction gate — 3 of 3 series regenerate from raw

Recomputed with the project's own `store_gen.members()` from `spectra_raw/queue2/FrI.tsv`,
whose header quotes its `destination_url` from tool-result metadata. Limit 32,848.872 cm⁻¹
(Fr II 6p⁶ ¹S₀), assigned by `assign_limit` as *forced — sole published limit*.
R mass-corrected for ²²³Fr.

| ℓ | stored δ | recomputed median | members stored / found |
|---|---|---|---|
| 0 | 5.07221 | **5.07221** | 24 / 24 |
| 1 | 4.59521 | **4.59521** | 48 / 48 |
| 2 | 3.42371 | **3.42371** | 50 / 50 |

Exact to five decimals on all three. The instrument is checked before it is used.

## 3 · FACET 5, MEASURED AT THE Rn CORE

On the M = 8 diagonal, p = M − 2ℓ − 1 = 7 − 2ℓ, so ℓ = 2, 1, 0 give p = 3, 5, 7 and
facet 5 = v₃ − 2v₅ + v₇ = δ(d) − 2δ(p) + δ(s).

| ℓ | diagonal n | p | δ at that n | channel median |
|---|---|---|---|---|
| 2 | 6d | 3 | 3.43035 | 3.42371 |
| 1 | 7p | 5 | 4.69260 | 4.59521 |
| 0 | 8s | 7 | 5.10670 | 5.07221 |

    facet 5, channel medians   -0.69450   SATISFIED (< 0)
    facet 5, diagonal points   -0.84816   SATISFIED (< 0)

**Two routes, same verdict** (§2.8). The channel-median route is the one Finding III used at
Cs I and Ba II; the diagonal-point route uses only the three levels the diagonal actually names.

**Facet 5 holds by measurement at the Rn core.** With Hg II (facet 4 −0.86980, facet 5 −0.57840)
and Cs I / Ba II on M = 7, the M = 8 pair is now half closed on the core the generating steps
Ac, Th, Cm, Lr actually sit on.

## 4 · FACET 4 IS A NULL, AND THE NULL IS IN THE WORLD

Facet 4 = v₁ − 2v₃ + v₅ needs δ(nf) at the Rn core. **`FrI.tsv` has no f series and no g series
at all** — its own header states s/p/d only, to n = 30, and the configurations confirm it.

This is not a refusal and not a gap in our reading. It is E measuring the *world*: the Fr I f
channel has not been published. The remaining one-electron Rn-core species are **Ra II** and
**Ac III**, and neither is in `spectra_raw` — `store_gen.levels()` reads neutrals only
(`queue2/{sym}I.tsv`), and the Z = 88 rows in the store are **Ra I**, whose Rydberg electron sees
a Ra⁺(7s) core, not Rn. *Ra I's f channel (δ 1.14629, n 5–8) must not be read as an Rn-core
value — that is the language/domain boundary this project forbids crossing.*

**So the fetch, if M rules for it, is now exactly specified and minimal: Ra II, for the nf series.**
It would also give an independent Rn-core check of s, p and d against Fr I.

## 5 · What is owed

- The Fr I d row's promotion to `COORDINATES.tsv` — **a ruling, not an act.** It is the same
  operation FLAG 1 asks for on Rb I, and *a write to COORDINATES is not complete until every
  artefact is regenerated and both gates rerun*.
- Register entries: facets 1 ≡ 4 under the diagonal map; the 43-species facet population and its
  two domains; the δ(d)-collapse association (41/43); facet 5 measured at the Rn core by two
  routes; facet 4 as a published-data null; the second promotion failure.
