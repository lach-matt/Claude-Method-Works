# W2C-seat — the S5 seat route, as concrete as the board allows (DOCKET 68, wave 2)

Not seated. Instrument: `seat.py` (`--selftest`: 47 of 47 pass; 26 CONTROLS, 16 GROUND, 5 STRUCTURAL not counted, so
42 of 42 counted; *wave 2 first said* 44 of 44 with 13 GROUND -- the W2-fix pass, section G, added three GROUND checks).
Every board figure is imported from its owner (stock, stockgate, formation, massform, foliation, transit, nopath,
ladder, branelink; docket68's measure and settle). Outside figures were READ this pass, route given with each.

## The question

M, 2026-10-04 (M-RULINGS item 7): **"S5 counts (Recommended)"**. O-SEAT, the supply of substance at the seat (O-MATTER
relocated by item 5, "Yes, from the seat"), is OPEN via S5 (reconstruction from stock at the destination) and the D25
stock gate, until both are shown. This item asks what each half of that pathway would have to be for a 70 kg payload
(`stock.HUMAN`) at Proxima.

## The answer, first

**O-SEAT stays OPEN.** No part of the pathway is shown and no part is refused. What this pass adds is a narrower,
named list of what is unchecked, with three computed results that are new on the board:

1. **The gate's binding element is measured nowhere in the Proxima system, in the sources read.** At a CI-like body
   the binder is P (10.70 kg per kg) and the runner-up is N (8.08). Neither P nor N is among the 21 species Morel 2018
   measures in α Cen A and B. **N is measured in α Cen A elsewhere** (W2-fix): Porto de Mello, Lyra & Keller 2008
   (READ, p.12) find from the literature that "the C, N and O abundance ratios of α Cen A are solar", and Laird 1985
   measured N in A and B (offset −0.65 dex, too-cool atmospheres, per Hinkel & Kane 2013 p.2, READ; the primary studies
   are NAMED-NOT-READ). **P is measured in no Proxima-system star** in any source read. Proxima's own photosphere has
   only an iron abundance in the sources read, and that is a spread (four studies, +0.16 to −0.07). No body in the
   system has a measured composition. So **at Proxima the gate cannot be evaluated at its binder, on any data READ**.
   The measured α Cen ratios move the other factors by up to 21 % (Na). They do not move the binder: P shifts 10.70 →
   10.43 kg/kg, and that shift is renormalisation only, since [P/Fe] is unmeasured and is set to 0 under H-ACEN-RATIO;
   N carries [N/Fe] ≈ 0 as a measured ("solar") value, not an assumed one. *Wave 2 first said* "Neither P nor N ... is
   measured", and N was "unmeasured, set 0".
2. **The primitive conjunct, element by element.** Suppose the body were devolatilised (stockgate's crust as proxy,
   H-DEVOL-PROXY). Then at the mass the gate needs for a primitive (CI) body, it fails on **N (458.6 kg/kg), C (114.7),
   H (71.3) and P (17.0)**. Three of these are the most volatile of the payload's elements (T_c 123, 40, 182 K). P is
   refractory (1229 K) and fails anyway at the crust's P. On the board's data, "primitive" is therefore what carries
   the gate. Brugger 2016 (READ) **leaves the primitive conjunct unconstrained**: it admits a water mass fraction of 0
   to 50 % (dry only for in-situ pebble accretion), but its model holds only a Fe/FeS core, silicate mantles, ice and
   liquid water, with Earth's compositional parameters -- no C, N or P -- so it neither admits nor excludes the CI
   volatile budget (binder P, runner-up N) the conjunct tests. Its radii are also computed at 1.10-1.46 M⊕ with
   sin i = 1, not at Faria's 1.07. *Wave 2 first said* "Brugger 2016 (READ) still admits both kinds of body".
3. **DOCKET 56's owed instrument, made exact.** `seat.py` §E lists the quantities it must compute and marks which of
   them can now be computed (conditionally) and which are computed nowhere:
   - the specification's bit count N, taken from measure: 9.5e27 to 1.09e29 bits under named counts;
   - a floor on the channel's received energy for a declared schedule;
   - the amortisation identity k\*;
   - the fabrication energy E_fab and the setup mass m_set, which are **computed nowhere**.

   The channel law the O6/O7 pass used for S5 (`branelink.py`'s A(N), read from its source) turns out to be
   Lachmann–Newman–Moore eq. (8) at **one polarisation**. This is checked symbolically. A control shows that two
   polarisations give exactly a factor of 2.

## A. What the destination must hold (H-PAYLOAD: 70 kg × stock.HUMAN)

The payload is mostly six elements: O 42.95 kg, C 15.98, H 6.99, N 1.80, Ca 1.00 and P 0.779. The remaining eight
elements make up 0.50 kg together. The binders on the board's stocks (`stock.processing_factors` over
`stockgate.DESTS`, imported):

| stock (H-STOCK-PROXY) | binder | runner-up | third | feedstock for 70 kg |
|---|---|---|---|---|
| CI chondrite | P 10.70 | N 8.08 | C 6.52 | 749.1 kg |
| Sun's hybrid photosphere (gas: excluded by the gate's first conjunct) | P 1911 | Li 1753 | K 652 | 1.338e5 kg |
| Jupiter (3× solar) | P 654 | Li 600 | K 223 | — |
| Earth continental crust (devolatilised proxy) | N 458.6 | C 114.7 | H 71.3 | 3.21e4 kg |

stockgate's 59-element payload, D25's own, binds on the same element at CI (P 10.7012).

**Measured in the Proxima system, per element (READ):**
- **Proxima's photosphere:** Fe only (restated by Morel 2018 p.16). Na is "roughly consistent with solar" (Pavlenko 2017,
  restated; NAMED-NOT-READ).
- **α Cen AB (Morel 2018, Table 1 p.7):** of the payload's elements, O, C, Na, Mg, Ca, Fe and Zn are measured.
  **P, N, K, S, Cl and Li are not**, and H is the reference element.
- **α Cen A, N (W2-fix):** solar, [N/Fe] ≈ 0, as the literature summarised by Porto de Mello et al. 2008 p.12 and Fig. 8
  p.14 (READ) has it; their own Table 4 p.12 carries no N. Laird 1985 measured C and N in A and B; Hinkel & Kane 2013
  p.2 (READ) report its [N/Fe] offset by −0.65 dex and exclude it. Primary studies NAMED-NOT-READ.
- **P (W2-fix):** in no source read -- not in Morel 2018, Porto de Mello 2008 Table 4 or Hinkel & Kane 2013 Table 1. The
  verifier W2V-1 also READ Maas 2017 (1704.08282, Table 1, no P) and a Hypatia P sample (2608.30484 p.3: 11-463 pc, so
  no α Cen); those two are the verifier's reads, not re-read here.
- **Any body:** none.

A stellar abundance constrains what a body might hold only through H-CONATAL and a formation model. Kervella 2017
(READ, abstract) shows the triple is gravitationally bound. Morel 2018 p.16 calls co-natal formation "not completely
settled".

## B. D25's gate at Proxima, conjunct by conjunct

`stockgate.GATE`: within the arrival aperture there is a condensed body, primitive rather than devolatilised, holding
at least M(p,s) × m_payload of accessible mass.

| conjunct | board | READ this pass | state |
|---|---|---|---|
| aperture | `formation.APERTURE_STATUS`: NOT EVALUABLE | — | unbound |
| condensed | Proxima b found (1.3 M⊕, Anglada 2017 second-hand) | Faria 2022, Table C.1 p.17: m sin i 1.07 ± 0.06 M⊕ at 0.04856 au. Proxima d is a candidate (0.26 M⊕ at 0.02885 au) | True (a body exists) |
| primitive | unmeasured | Brugger 2016: radius 0.94–1.40 R⊕, water mass fraction 0–50 %, built on solar-system values for lack of host abundances (p.1); layers core, mantles, ice, water only -- no C, N or P; masses 1.10–1.46 M⊕ at sin i = 1 | unmeasured; **unconstrained** by Brugger (*wave 2 first said* "both kinds admitted") |
| accessible | unmeasured | — | unmeasured (H-BODY-ACCESS) |
| mass ≥ M·m | 749.1 kg (CI) | b's minimum mass m sin i is 8.53e21 × that, so its mass is **at least** 8.53e21 × that (a floor; i unknown) | NOT the accessible mass: unmeasured |
| composition (sets M) | — | P measured in no star of the system (sources read) and no body; N in α Cen A only ("solar") and no body | unmeasured |

`formation.gate` (imported) returns **UNDETERMINED** at Proxima b on a synthetic aperture and **NOT-EVALUABLE** with no
aperture. Its control shows the same gate returns False when b is measured as devolatilised. This pass reads at source
the m sin i that formation.py carries second-hand. Faria's minimum mass, m sin i = 1.07 ± 0.06 M⊕, replaces nothing on
the board; it only sharpens the figure, and every ratio built on it is a floor.

## C. Fabricator, survey, receiver (D23)

- **Arrival at ≤ c:** the earliest is the light time, **4.2465 yr** (4.24646, `phase1.L_PROXIMA` imported through
  settle; *wave 2 first used* `foliation.proxima_span_m`, the same value rounded to four decimals). Illustrative
  slower values: 21.2 yr at 0.2 c, 42.5 yr at 0.1 c, 425 yr at 0.01 c. **Proxima's distance has two READ values**
  (W2-fix): phase1's, from the Gaia DR3 parallax 768.066539 mas (READ via restatement, DOCKET 67), 4.24646 ly; and
  Faria 2022 Table 1 p.2's, 768.50 ± 0.20 mas and 1.3012 ± 0.0003 pc (referenced there to Gaia Collaboration 2016),
  4.2439 ± 0.0010 ly. They differ by 0.056 %: 2.17 σ on Faria's parallax error alone (2.10 σ on both errors; 2.57 σ
  against Faria's printed, rounded 1.3012 pc). phase1's is imported for every computation; on Faria's the arrival is
  4.244 yr and the report home 8.488 yr. No verdict moves (`settle.proxima_distances`, G40-G42).
- **Survey:** Proxima b does not transit (Faria 2022 p.9; Brugger p.1 gives a 1.5 % transit probability). So no radius
  or density has been measured, and no bulk composition can be measured remotely. The gate's composition conjunct
  therefore needs an **in-situ survey**, which D23 delivers no earlier than 4.2465 yr. If the gate must be checked at
  the origin before a specification is committed (H-CHECK-AT-ORIGIN), the earliest answer is **8.493 yr**. If the
  fabricator decides locally, nothing has to come back.
- **Receiver:** it must hold ≥ 2^I distinguishable states. Its Bekenstein floor (measure, imported) is 33–379 J at
  R = 1 m, below 1e-14 of the payload's Mc². This is not a constraint in practice.
- **Fabricator:** it must process the feedstock and place 6.71e27 atoms. Its rate and energy are **computed nowhere**,
  and stockgate refuses to price separation energy. The erasure floor of the specification register (Landauer,
  310 K) is 2.8e7–3.2e8 J. That is not E_fab.
- **Amortisation (sympy):** under H-KINETIC, S5 pays back after more reconstructions than
  `k* = m_set·K / (m_pay·K − E_rec)`, with K = (γ−1)c². As E_rec → 0 this gives **k\* → m_set / m_pay**: the number of
  later trips is just the setup-to-payload mass ratio. There is **no k\* at all once E_rec ≥ m_pay·K**. That ceiling,
  the one number DOCKET 56's instrument must come in under, is 1.30e17 J at 0.2 c, 3.17e16 J at 0.1 c and 3.15e14 J at
  0.01 c, for 70 kg. m_set is specified nowhere.

## D. The information that must arrive, against the channels

measure.py's counts are imported unchanged: 9.51e27 (species sequence), 4.14e28 (1 Å grid), 1.09e29 (0.1 Å grid) and
2.84e28 (thermal) bits. Each is conditional on its named count.

- **Teleportation (H-FAITHFUL, quantum definition):** 2 classical bits and 1 pre-distributed ebit per qubit, so 1.9e28
  to 2.2e29 classical bits. The message arrives D/c after it is sent, and `transit.advantage_over_light` is 0.
- **Drift channel (settle, imported; conditional on H-C2, H-MAP, H-TRANSFER, H-SPIN, H-DILUTION and F1):**
  - Pairs: at least 7 drift pairs per teleported qubit (CMAX 0.3219 bits per pair), so 8 pairs per qubit in all and
    7.6e28 to 8.7e29 pairs for the payload.
  - Window: OPEN at Proxima on the READ (abstract) Weinberg-family limits under both H-MAP readings. That means "not
    excluded", never "found".
  - Drift time at the largest ε those limits permit: 4.8e4 s (reading A) and 9.6e4 s (reading B).
  - Distribution: every pair must be distributed. **In S5's one-end case nothing beats light.** A one-end source reads
    at 4.2465 yr. A midpoint source must itself first be carried to the midpoint at ≤ c, so the earliest read is again
    4.2465 yr + T_drift. The 2.12 yr midpoint read (settle.first_transit_times) needs a source that is already at the
    midpoint.
- **Energy floor of the classical channel (H-EM-CARRIER; 100 m dishes, `branelink.DISH_D`; T DECLARED):**
  - The floor on received energy (LNM eq. 8, under H-FEW-MODES) runs from 6.9e13–1.4e14 J (species sequence, T = 1 yr)
    to 9.0e15–1.8e16 J (0.1 Å grid, T = 1 yr). At T = 100 yr each is 100× lower.
  - LNM eq. (6) gives larger values (up to 2.6e16 J). Its many-mode assumption fails here (< 1 transverse mode in every
    case, max 0.20), so it is context, not a floor. The transmitted energy, diffraction loss included, is **not
    established**.
  - Each figure prices a schedule. As T grows the energy falls (1/T in 1D, T^−1/3 in 3D), so S5's transfer has **no
    energy floor independent of T**.
  - At a 1 yr schedule and the 0.1 Å count, the received-energy floor alone is 0.3–0.6 of the 0.1 c ceiling in §C. At
    100 yr it is 6e-3 of it. This is a comparison of figures, not a verdict on k\*, since E_fab is unknown.

## E. What DOCKET 56's owed instrument would have to compute

`seat.DOCKET56_OWED`:

1. **N(spec)**, from the specification. It must never come from inverting a channel law, because branelink's round
   trip A(N(A)) = A proves nothing. *Computed here (imported from measure):* 9.5e27 to 1.09e29 bits. Which count is
   the specification is H-ALT, a choice.
2. **E_tx(N, T, d, apertures).** *Computed here* as a received-energy floor for a declared T. It prices a schedule, not
   the route.
3. **E_fab**, the separation of M(p,s) × 70 kg of feedstock plus the assembly of 6.7e27 atoms. *Computed nowhere on the
   board.*
4. **E_hold.** *Imported* as a Bekenstein floor. It is negligible.
5. **m_set**, the mass of the fabricator, survey and receiver. *Specified nowhere.*
6. **k\*.** *Computed here as an identity* in m_set and E_rec = E_tx + E_fab (+ erasure).

## F. The grade, with every premise named

`grade_o_seat` returns **OPEN** on today's state. Its controls move it: every conjunct True plus S5 shown gives
REMOVABLE, pending seating and M; primitive measured False for the sole body gives LEFT.

| part | status | premises |
|---|---|---|
| fabricator/survey/receiver arrival ≥ 4.2465 yr (≥ 8.493 yr if checked at origin) | **shown** (arithmetic on D23) | D23; H-CHECK-AT-ORIGIN for the second figure |
| k\* identity, → m_set/m_pay as E_rec → 0; no k\* above m_pay·K | **shown** (sympy) as an identity | H-KINETIC |
| channel energy floor for a declared schedule | **computed, conditional** | H-EM-CARRIER, H-FEW-MODES, H-ONE-POL, T and dishes DECLARED |
| gate at the binder (P; runner-up N) at Proxima | **not evaluable on READ data** | P in no source read; N in α Cen A only ("solar"); no body composition |
| primitive conjunct | **OPEN**; unconstrained by Brugger 2016, which models water only (*wave 2 first said* "both kinds admitted") | H-DEVOL-PROXY for the element list |
| accessible mass, aperture | **OPEN** (unchanged) | H-BODY-ACCESS; formation's APERTURE_STATUS |
| S5's price per reconstruction | **OPEN**: E_fab and m_set computed nowhere | DOCKET 56 owed |
| S5 sooner than light | **already refused on the board** (transit BEATS_LIGHT False; restated, not new) | D23, linear QM; the drift route is conditional and still one-end-bound |

Nothing is removed by assertion, and nothing is refused that the board did not already refuse. The new limits are
named hypotheses: H-STOCK-PROXY, H-ACEN-RATIO/H-CONATAL, H-BODY-ACCESS, H-DEVOL-PROXY, H-KINETIC, H-EM-CARRIER,
H-ONE-POL, H-FEW-MODES, H-MODE-CONTINUUM and H-CHECK-AT-ORIGIN.

## History kept

- **Wave 5** (M-combine) graded O-SEAT "LEFT" in every variant, with the {S10, S13} restriction unnamed. **Wave 6**
  (F-alone) named that restriction H-SEAT-ROUTES and graded OPEN via N_S5. **M** then ruled "S5 counts".
- `measure.seat_route_s5` priced D25's mass conjunct (749.1 kg CI, 1.338e5 kg photosphere) for the 59-element payload.
  This file agrees for stock.HUMAN: 749.07 kg, a 0.002 % payload-table difference.
- formation.py's Proxima b at 1.3 M⊕ (second-hand, "kept as read") stands as the board's record. Faria 2022's minimum
  mass m sin i = 1.07 M⊕ is READ here at source. *Wave 2's report first called it "mass" and "total mass"; the file's
  table already said minimum.*
- An earlier draft of this file's selftest claimed "measured α Cen ratios move every factor < 5 %". That claim failed
  on Na (−21.5 %) and was restated as "the binder P moves only by renormalisation".
- An earlier draft printed LNM eq. (6) as a floor. That was withdrawn once the mode count (< 1) showed its assumption
  fails.

## Sources READ (route)

- Faria et al. 2022, arXiv:2202.05188v1. READ via alphaXiv, Table C.1 p.17, Table 1 p.2, p.9 (re-READ W2-fix: Table 1
  p.2 parallax and distance).
- Brugger, Mousis, Deleuil & Lunine 2016, arXiv:1609.09757v3. READ via alphaXiv, pp.1–5 (re-READ W2-fix: the layers
  p.1-2, Table 1 p.2, the masses at sin i = 1 p.1 and p.3).
- Porto de Mello, Lyra & Keller 2008, arXiv:0804.3712v2. READ via alphaXiv (W2-fix), p.12, Table 4 p.12, Fig. 8 p.14.
- Hinkel & Kane 2013, arXiv:1304.0450v1. READ via alphaXiv (W2-fix), p.2, Table 1 p.4.
- Morel 2018, arXiv:1805.00929v1. READ via alphaXiv, Table 1 p.7, p.8, p.16. Proxima's four [Fe/H] studies and
  Pavlenko 2017 are restated there and are NAMED-NOT-READ themselves.
- Kervella, Thévenin & Lovis 2017, arXiv:1611.03495. READ (abstract) via Firecrawl research inspect.
- Lachmann, Newman & Moore 1999, arXiv:cond-mat/9907500v1. READ via alphaXiv, eq. (6) p.6, eq. (8) p.7. Both printed
  fixtures (1.61e21 and 2.03e17 bits/s) are reproduced in the selftest, with controls (ħ for h; one polarisation)
  that fail.
- Bekenstein 1981, PRL 46, 623. READ (abstract) via Firecrawl scrape of the publisher's public abstract page. The
  abstract prints no coefficient, and none is taken from it.

No paywall or login wall was circumvented. Nothing was committed, pushed, stashed, reset or checked out. ledger.py,
index3.py, specthm.py, LEDGER.md and paper/ were not edited.

## G. W2-fix (2026-10-04): the two re-verifications, every item resolved

The verifiers W2V-0 (AGAINST M) and W2V-1 (FOR M), `wave2/WAVE2-RESULT.json` key `result.verify`. No grade moves:
O-SEAT stays OPEN via S5/D25. Wave 2's sentences are kept above, marked *wave 2 first said*.

| verifier item | resolution |
|---|---|
| W2V-0 #2 / W2V-1 #4: 1.07 M⊕ called the planet's mass; it is M_p sin i, the minimum mass (Faria 2022 Table C.1 p.17; p.9) | **Applied.** Every site now reads minimum mass m sin i = 1.07 ± 0.06 M⊕, and the ratio reads **≥ 8.53e21 × the CI threshold, a floor** (`seat.gate_conjuncts` key renamed; GROUND check names it). The open item is accessible mass (H-BODY-ACCESS), unchanged. |
| W2V-0 #5: Brugger 2016 read as admitting both kinds of body; it models only core, mantle and water, no C, N or P, at 1.10-1.46 M⊕ with sin i = 1 | **Applied, re-READ at source** (alphaXiv: p.1 the five layers, Table 1 p.2, p.1 and p.3 the masses). "Unconstrained by Brugger" everywhere; `BRUGGER_2016` carries `models_C_N_P: False`; a GROUND check holds the primitive conjunct at None. |
| W2V-1 #2: "P and N are measured in no star of the system" without the scope; N IS measured in α Cen A | **Applied, re-READ at source.** Porto de Mello et al. 2008 p.12 (READ): "The available literature data also suggests that the C, N and O abundance ratios of α Cen A are solar"; Fig. 8 p.14 plots N. Note what it is: a summary of other studies, qualitative ("suggests", "solar"), with no number printed in the text, and their own Table 4 carries no N. Hinkel & Kane 2013 p.2 (READ): Laird 1985 measured C and N in A and B, [N/Fe] offset −0.65 dex, excluded. So under H-ACEN-RATIO N carries [N/Fe] ≈ 0 as a measured value; P stays unmeasured in every source read. The binder P is unchanged and O-SEAT stays OPEN. `seat.proxima_measured` now tells P from N (GROUND check). |
| W2V-1 #3: Proxima's distance labelled NAMED-NOT-READ while Faria 2022 Table 1 prints it; D23 times on 4.2465 ly | **Applied, with a correction to the verifier's own "correct" text.** The board's distance is READ already: `phase1.L_PROXIMA`, Gaia DR3 parallax 768.066539 mas (READ via restatement, DOCKET 67) -- so 4.2465 ly is not "the task's figure", and this file does not call it that. Both READ values are recorded (`settle.PROXIMA_DISTANCES_READ`), the discrepancy computed (0.056 %; 2.17 σ on Faria's parallax error alone, 2.57 σ against Faria's rounded printed distance -- the verifier's "2.6 σ"), phase1's imported for the computation. On Faria's value the D23 arrival is 4.244 yr and the report home 8.488 yr; no verdict moves (G42 in settle). |

Recorded, not changed: W2V-1 #5 is the verifier's own process note.

