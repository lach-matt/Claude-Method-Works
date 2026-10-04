# W2C-seat — the S5 seat route, as concrete as the board allows (DOCKET 68, wave 2)

Not seated. Instrument: `seat.py` (`--selftest`: 44 of 44 pass; 26 CONTROLS, 13 GROUND, 5 STRUCTURAL not counted).
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

1. **The gate's binding element is measured nowhere in the Proxima system.** At a CI-like body the binder is P
   (10.70 kg per kg) and the runner-up is N (8.08). Neither P nor N is among the 21 species Morel 2018 measures in
   α Cen A and B. Proxima's own photosphere has only an iron abundance in the sources read, and that is a spread (four
   studies, +0.16 to −0.07). No body in the system has a measured composition. So **at Proxima the gate cannot be
   evaluated at its binder, on any data READ**. The measured α Cen ratios move the other factors by up to 21 % (Na).
   They do not move the binder: P shifts 10.70 → 10.43 kg/kg, and that shift is renormalisation only, since [P/Fe] is
   unmeasured and is set to 0 under H-ACEN-RATIO.
2. **The primitive conjunct, element by element.** Suppose the body were devolatilised (stockgate's crust as proxy,
   H-DEVOL-PROXY). Then at the mass the gate needs for a primitive (CI) body, it fails on **N (458.6 kg/kg), C (114.7),
   H (71.3) and P (17.0)**. Three of these are the most volatile of the payload's elements (T_c 123, 40, 182 K). P is
   refractory (1229 K) and fails anyway at the crust's P. On the board's data, "primitive" is therefore what carries
   the gate. Brugger 2016 (READ) still admits both kinds of body at Proxima b: water mass fraction 0 to 50 %, and dry
   only for in-situ pebble accretion.
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
| primitive | unmeasured | Brugger 2016: radius 0.94–1.40 R⊕, water mass fraction 0–50 %, built on solar-system values for lack of host abundances (p.1) | unmeasured; both kinds admitted |
| accessible | unmeasured | — | unmeasured (H-BODY-ACCESS) |
| mass ≥ M·m | 749.1 kg (CI) | b's minimum total mass is 8.5e21 × that | NOT the accessible mass: unmeasured |
| composition (sets M) | — | P and N measured in no star and no body | unmeasured |

`formation.gate` (imported) returns **UNDETERMINED** at Proxima b on a synthetic aperture and **NOT-EVALUABLE** with no
aperture. Its control shows the same gate returns False when b is measured as devolatilised. This pass reads at source
the m sin i that formation.py carries second-hand. Faria's 1.07 M⊕ replaces nothing on the board; it only sharpens the
figure.

## C. Fabricator, survey, receiver (D23)

- **Arrival at ≤ c:** the earliest is the light time, **4.2465 yr** (`foliation.proxima_span_m`). Illustrative
  slower values: 21.2 yr at 0.2 c, 42.5 yr at 0.1 c, 425 yr at 0.01 c.
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
| gate at the binder (P, N) at Proxima | **not evaluable on READ data** | Morel 2018's species list; no body composition |
| primitive conjunct | **OPEN**; both kinds admitted (Brugger 2016) | H-DEVOL-PROXY for the element list |
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
- formation.py's Proxima b at 1.3 M⊕ (second-hand, "kept as read") stands as the board's record. Faria 2022's 1.07 M⊕
  is READ here at source.
- An earlier draft of this file's selftest claimed "measured α Cen ratios move every factor < 5 %". That claim failed
  on Na (−21.5 %) and was restated as "the binder P moves only by renormalisation".
- An earlier draft printed LNM eq. (6) as a floor. That was withdrawn once the mode count (< 1) showed its assumption
  fails.

## Sources READ (route)

- Faria et al. 2022, arXiv:2202.05188v1. READ via alphaXiv, Table C.1 p.17, Table 1 p.2, p.9.
- Brugger, Mousis, Deleuil & Lunine 2016, arXiv:1609.09757v3. READ via alphaXiv, pp.1–5.
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
