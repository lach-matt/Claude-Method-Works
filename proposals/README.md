# proposals/

Policy proposals prepared for the California Legislature, and the one tree
here that is neither physics paper, mirror nor generated output. `papers/`
holds the physics; `method/` and `drive/` are resource material. Nothing here
writes to any of them.

## What is here

**`Title_III_Joinder_v0.2.md` is Title III, the joinder** (`tools/rebase3.py`), and **`Title_II_Aqua-Sovereign_v0.2.md` is Title II re-based** (`tools/rebase2.py`, same discipline). **`Title_I_Helios-3_v0.2.md` is Title I re-based on Helios-3** — rendered by `tools/rebase.py` from
the instruments, never hand-edited (the selftest asserts byte-identity with a fresh render), every
number labelled mid or critical. See `docs/REBASE.md`. v0.1 below is unchanged.


- **`California_Sovereign_Infrastructure_v0.1.md`** — the as-submitted merge
  of the author's two source proposals (Drive: *California Energy
  Independence Project*, 2026-09-09; *California Sovereign Water and Mineral
  Infrastructure Initiative*, 2026-09-10) into one document under one
  authority: Title I energy (Program Helios-1M), Title II water
  (Aqua-Sovereign), Title III joinder (reserved). **No figure was altered in
  the merge.** It is the baseline every repair is diffed against.
- **`FLAWS.tsv`** — the adversarial review of v0.1: 40 flaws, each with the
  claim as written, why it fails, the figure that shows it, what settles it,
  and a status. Tiers: `FATAL` (the program's central claim cannot be true as
  written), `CRITICAL` (a load-bearing figure is wrong by more than 2×, or a
  legal barrier blocks the stated path), `MAJOR` (a reviewer will catch it and
  it changes the answer), `MINOR` (drafting, consistency, or a defensible
  assumption left unstated). Status `AGREED` marks a flaw the author has
  already directed a fix for; `OPEN` is everything else.

## The decisions already recorded (2026-09-11)

1. **One program, two projects, severable.** One act, one authority, one
   balance sheet; Helios is Title I and closes alone, Aqua is Title II and
   closes on the Title I contract.
2. **Nitrate salt stays** in Title I — the proven medium at 290–565 °C — and
   chloride chemistry is excluded from every system on hazard grounds. This
   rules out magnesium metal (chlorine electrolysis) in Title II.
3. **Heliostats:** Noor III-class units (~178 m²) and 36 towers of Noor III
   class, not 11.4 million micro-heliostats on 12 record-size towers.
4. **Salt:** drop zero-liquid-discharge; recover Mg(OH)₂ and gypsum on a
   slipstream; return brine through the retired plant's existing permitted
   outfall at Ocean Plan concentration.

**Standing rule (author, 2026-09-11): simulate critical, not optimal.** Every banded constant
carries a NOMINAL and a CRITICAL value, the critical being the adverse end of its band; every
result prints in both columns; the design is held to the critical column and the nominal column
is margin. The point is a *front-end threshold band on critical events upstream*: a downstream
instrument hands its critical figure to the one above it (`receiver.py` → `cspchain.py`'s
receiver link) rather than the hoped-for one. A number quoted without its case is misquoted.
`tools/receiver.py` is the first instrument built under it; the selftest asserts critical ≤
nominal on every result. **The chain and the register now carry it too**: `cspchain.py`'s
`design(..., "critical")` and `helios3.py`'s `priced("critical")` — Helios-3 mitigated is
**$125/MWh at mid and $202 at critical** ($756 / $1,218 per household against $1,177 today),
the mirror 1.70× larger, driven by the receiver's 0.690 and the field's 0.58 before any adder.
(The critical receiver was 0.795 until the 2026-09-11 review of the record halved the critical
flux to 0.5 MW/m², below the 0.3–0.7 Sandia measured its curtain at.)

**R-12 provenance is listed rather than asserted (`tools/studies.py`, `docs/STUDIES.md`).** Twelve
technologies, 49 study rows each with a status (OPERATED / TESTED / DESIGNED / AUTHOR) and a source —
complete over technologies, a floor over studies, **reviewed against the web on 2026-09-11 where
the proxy reached and corrected in place** — one recommendation per technology placed on the
ladder's rungs (7.5 years of study on the critical path, run against the build), and the cost of
delay: **$0.97 B per year at mid, $1.64 B at critical**, the price drifting 3.8 / 6.1 $/MWh a year
at the 3 % construction escalation. The review also found that two of the three largest salt towers
built (Crescent Dunes, Noor III) have each lost more than a year to a hot-salt tank leak, which is
R-13's BENEFIT row and the salt-block fallback's failure mode.

**The hour-by-hour (`tools/hourly3.py`, `docs/HOURLY3.md`) is the first study on that list and it is
run.** As sized by the static chain, Helios-3 serves **87 %** of the load — the sCO₂ block cannot carry
the evening peak after sunset in any month, so the shortfall is year-round and evening-led, 14 % in July
and 20 % in December, the worst month. Closing it to 1 % takes **block ×1.25, field ×1.5 and a second
day of store**; the heater and PV overbuild were never the lever. **+$34/MWh at mid, +$56 at critical —
about $159 and $258/MWh** to serve the whole load from the plant alone. (Corrected 2026-09-11: the
reconstructed load shape had its seasonal term inverted; `docs/LOADSHAPE.md` records the before and after.) Re-basing Title I on that sizing, or
serving December from something other than December's sun, is the author's decision. The author's
objection — California's deserts keep their winter sun — was checked: the model already gives the
desert nodes 0.77–0.79 of their annual-mean DNI in December, above the ~0.65 of the desert record;
December is short on hours and angle, not clouds, and moving the Central Valley node to the desert
is worth two points of service and does not change the closing sizing.

## Resolved so far

| flaw | instrument | finding |
|---|---|---|
| F-01, F-02 | `tools/helios.py` | 19.2 TWh net at the scale proposed, not 39.6 sold; the export is negative; $693 M at 2024 prices against $1,933 M carrying. Inverted: $102/MWh needed at Title I's own capex — inside the firm-clean band — so F-05 decides. |
| F-17 | `tools/helios.py` | 3 M households at EIA's 6,036 kWh/yr is 18.1 TWh; the plant makes 19.2 — the size was right, the export was wrong, and growth needs 1.3–1.7× by 2060. At the built cost a household pays **more** for generation than today ($1,244 vs $1,177). No size answers it; the equipment does. |
| F-06 | `tools/hourly3.py`, `tools/joinder.py` | The solar multiple was a label; run hour by hour Helios-3 as chained serves 87 % of the load, the block cannot carry the evening in any month. Closed by block ×1.25, field ×1.5 + store 2 days (mirrors, +$34/MWh mid, +$56 critical); water alone has no feasible point on this load (its surplus cannot lift what closes). The author chose both, delivered year-round (`both.py`): block ×1.5, field ×1.25, 1,500 MW, 15–17 modules, +$38 / +$61, 0.75–0.83 MAF/yr. |
| F-18, F-20, F-21, F-22, F-23, F-25, F-29, F-30, F-31 | `tools/majors.py`, `tools/rebase3.py` | No export RA; washing 1,394–2,378 AFY from the program's own water; land 62,160–94,980 acres with Westside fallowed land claimed; the Central Valley node kept at a larger share; no nitrate in Helios-3; NEPA budgeted on the Mojave node; the downside case is critical ($151/245 at 1.25× coverage); contingency 15/30 %, DSRF one year. `Title_III_Joinder_v0.2.md` written: the agreement, the shared asset, the decision table, the takers, the statement, severability. |
| F-03, F-04, F-11, F-12, F-13, F-15, F-26, F-27, F-28, F-35, F-36 | `tools/titletwo.py`, `tools/rebase2.py` | Title II's process rows: no mineral revenue (one module's Mg(OH)₂ is 0.76–1.27 of the US market); brine through the outfall at a 17:1 diffuser dilution; RO the default; first water 2034–2037 from the record, not 24 months; energy at the contract price with Title I's surplus at 7% of hours; on-site PV 13%–6% of the draw, islanding for critical loads; screened open intake as default. `Title_II_Aqua-Sovereign_v0.2.md` rendered from the instruments. |
| F-09, F-10, F-19, F-24 | `tools/titleone.py` | Export negative so no export right; one 500 kV circuit per node (1,196 / 1,179 MW). Tariff is the household bill at cost recovery ($756 / $1,218 vs $1,177), CCA-form LSE. Bonds priced to the security: GO $125/202, revenue $140/227, unrated $161/262 per MWh. Schedule is the ladder 2029–2041 with tranches by rung. |
| F-14, F-16 | `tools/aquacost.py` | A module is **$1,883 M / $2,886 M** financed against $250–320 M submitted, from the record (Carlsbad, Huntington Beach) escalated; water at cost recovery with the energy at Title I's price is **$3,034 / $4,790 per acre-foot** against $400 claimed and Carlsbad's $2,700–2,900. The adopted route's modules are $28 / $48 B of Title II capital. |
| F-32, F-33, F-34, F-37, F-38, F-39, F-40 | `tools/minors.py` | The seven minors: the cycle relabelled (sCO₂ Brayton 0.50; salt fallback subcritical reheat 0.43); ASCE 7 with the 0.75 g target above the mapped MCE at every node; CO₂ avoided **6.33 / 5.51 MMT** as sized and 7.24 / 6.34 closed against 11.8 claimed; the Authority as a statutory LSE on the SB 6X pattern with §8571 cited only for what it does; jobs from built plants per MW (1,632 / 1,063 permanent, 17,545 construction peak); one EPC per node under an owner's engineer; 40 dBA at 13 / 79 m with a $19 / $58 M enclosure per module. **Forty of forty resolved.** |
| F-05, F-07, F-08 | `tools/heliocost.py` | $46–71 B net of the storage credit ($57 B mid, $10.85/W) against $27.2 B stated; needs $171–253/MWh against a band of $80–120. **The criterion does not close at the scale proposed in any case.** |

## The second pass: the equipment (`tools/firmpower.py`, `docs/FIRMPOWER.md`)

The author's instruction after the first pass: *3 million households is a
minimum, growing with population — make the system smaller, and make it
produce more.* Every candidate that can make a firm MWh in California, sized
to the same 18.1 TWh, priced the same way, state-owned:

| | MW | $/MWh | $/household/yr vs $1,177 today |
|---|---|---|---|
| Salton Sea geothermal (in the proposal's own Imperial node; 2,250 MW developable, 0.98 of the requirement) | 2,297 | **62** ($103 without the federal credit) | 375 (−68 %) |
| Enhanced geothermal (Fervo class; SCE holds 320 MW) | 2,297 | 57 | 343 |
| PV-charged nitrate salt (Helios tanks + turbines, no heliostats) | 13,040 PV | 193 | 1,168 |
| Salt-tower CSP as proposed | 4,941 | 205 | 1,239 (+5 %) |
| SMR — **barred** by PRC §25524.2 | 2,247 | 102 | 617 |

Geothermal is *smaller and produces more* literally: 2.15× less nameplate,
46× less land, CF 0.90 against 0.49, firm through night and winter. The file
does not choose; the decision is the author's.

### The author's decision: CSP, made better (`tools/cspchain.py`, `docs/CSPCHAIN.md`)

*"CSP is the best path; we just have to learn enough about how it works to do
it better — scale down in size while simultaneously increasing output."* The
energy chain, link by link, and two plants on the same 18.1 TWh:

| | as proposed | **Helios-2 (built parts)** | Helios-3 (pilot) |
|---|---|---|---|
| mirror, M m² | 42.9 | **22.5** | 18.1 |
| $/MWh | 205 | **141** | 117 |
| $/household/yr vs $1,177 | 1,239 | **849** | 706 |

Helios-2 keeps the nitrate salt and steam block, sizes the heliostat field
for the night, serves the daytime third from PV directly (DEWA), and fires
PV-fed heaters in winter (Midelt) — 1.9× smaller in mirror, same energy, every
part built. Helios-3 is the same on Gen3 particles and sCO₂ — the right CSP,
and a pilot.

### The author's decision: Helios-3, each cost mitigated upfront (`tools/helios3.py`, `docs/HELIOS3.md`)

Sixteen rows graded before and after mitigation, each carried by a named part
of the build, each marked **DESIGN** (retired by specification), **HOURS**
(retired only by operating time) or **BENEFIT**. Before: 7 MODERATE / 3 MAJOR
/ 2 DOMINANT; after: 6 MINOR / 4 MODERATE / 2 MAJOR / 0 DOMINANT. Six rows
retire by design; six can only be retired by hours — the receiver, the
exchanger, the turbine, the chemistry, the scale, the provenance — and the
file refuses to flatten them. Priced, the mitigations take Helios-3 from
**$117 to $125/MWh** ($756 per household), still under Helios-2's $141 and $5
above the band's top. The plan that buys the hours: common field, towers and
PV; one 100 MWe Helios-3 module first; salt block as fallback.

## How the flaws are worked

One at a time, in register order, each resolved by an instrument where the
flaw is numerical and by a named legal or contractual mechanism where it is
not. A resolved flaw moves to `RESOLVED` with the version that resolved it;
nothing in `FLAWS.tsv` is deleted. **As of 2026-09-11 all forty rows are `RESOLVED`** (`docs/MINORS.md` closes the last seven). The same standard as `papers/` applies once
the instruments exist: every figure in the proposal is computed, carries a
status, and fails a harness if the prose states a number the model does not
produce.

## Title III joinder items

**Can Title II return Title I's winter? (`tools/joinder.py`, `docs/JOINDER.md`, 2026-09-11.)** The
author: desalinate on the summer surplus, hold the water, return the offset from the desalination
plants' turbines; then, not more storage on the power side — more modules. Two turbines that can
mean. **Steam-topping turbines** (Title II's own architecture) return electricity they were given as
heat, less what the water took — the water costs 6.4× reverse osmosis — and have no winter heat to
return (F-13/F-27): they do not return a winter. **Hydraulic turbines on the water itself** do: summer
surplus lifts the product to an elevated reservoir, delivery October to April comes back through
pump-turbines. Hour by hour the shortfall is a seven-month season plus the evening, not a winter, and
the hydro plant must be sized to the evening. With the water on Title II's own account and the surplus
on the lift alone, **the author then decided the water comes down year-round** (summer irrigation, winter recharge), the
reservoir holding weeks rather than a season. On the corrected load shape (`docs/LOADSHAPE.md`) **water
alone is not a route**: with the field and store at design no point both closes and lifts its water inside
the plant's own surplus, because the block that closes the evening eats the spill the lift runs on, and a
lift bought from the grid is not this route. Water with a larger field is, and that is the adopted route
(`both.py`). The lift does not depend on head.

**The decision: both (`tools/both.py`, `docs/BOTH.md`, 2026-09-11).** Asked which route closes the
season, the author answered *both*. Read literally as the even split — the water returns half the
season, the field and store carry the other half — the adopted sizing is block ×1.5, field ×1.25, store 1 d,
1,500 MW of pump-turbines and 15–17 modules (0.75–0.83 MAF/yr), every point required to lift its
water inside its own surplus: **$6.4 / $10.3 B on Title I's account, +$38 / +$61 per MWh**, 1.12× /
1.15× mirrors alone ($5.7 / $9.5 B), and a plant that with the water withheld leaves 3.6–4.0 % to the
grid and with the field at design 1.3–1.4 %, against 13 % with neither. Figures on the corrected load
shape with year-round delivery (`docs/LOADSHAPE.md`). The ladder over the water's share is printed so the split can be moved.

**The pilot aperture as an acceptance protocol (`tools/pilot.py`, `docs/PILOT.md`, 2026-09-11).** The
receiver's real efficiency is the one open item no instrument can close, so the test is fixed before it
is built: one 30 MW_th aperture (60 m × 1 m at critical), five measurements, and a pass mark from
`receiver.py`'s own figures with a 3.3 % calorimetric uncertainty — PASS-DESIGN at **0.713**, UNDECIDED
between 0.667 and 0.713, FAIL below (the salt-block fallback, and no first module). 1,000 on-sun hours,
2031–2033, $71 M.

**The sites, scored (`tools/sites.py`, `docs/SITES.md`, 2026-09-11).** The site-specific terms that
survive the register cannot be computed without a site, so the three Title I nodes and eight coastal
brownfields are graded MET / CONDITIONAL / OPEN / FAIL on the terms each Title needs and ranked, each
with the study that would settle its worst term. At mid the Westside ties the Mojave for first and at
critical the Mojave leads on the seismic margin; on the coast the Oxnard plain leads and Huntington
Beach carries its 2022 denial as a FAIL. The adopted route's 15–17 modules against eight sites is a
finding. A ranked list of site studies, not a choice.

**The studies and surveys as the first line (`tools/predev.py`, `docs/PREDEV.md`, 2026-09-11).** The
author's instruction: every study and survey is its own upfront line item, first in priority. Priced
at mid and critical from the class of study (ASSUMED bands): Title I **$213 / $463 M** — resource, site,
environmental, permit, interconnection and reservoir studies that gate the field, and the technology
studies on the ladder — carried in the capital ahead of every plant line; Title II **$4.3 / $17.8 M per
module**. The schedule opens with tranche zero (2027 to the field start), the field waits on the longest
gating study, and at critical the whole ladder slides two years. Register price $126 / $205, water
$3,044 / $4,830 per acre-foot.

**The complete proposal and the pitch (`tools/proposal.py`, `docs/PROPOSAL.md`, 2026-09-12).** The author asked
for the whole proposal in one document, every item expanded, each location addressed in full, figures, tables and
cited studies, with a two-to-three page bullet pitch beside it. `California_Sovereign_Infrastructure_v0.2.md`
(twenty-one sections, twelve figures under `figures/`) and `Pitch_v0.2.md` are rendered from the instruments, both
emitted as `.docx` and `.pdf` too, and the selftest holds that the pitch carries no number the proposal does not. The three
Titles stay as the diff against v0.1; the proposal is the whole.

**Reviewed adversarially (2026-09-12, `docs/PROPOSAL-REVIEW.md`).** Twenty-five flags; six were faults in the
instruments and are corrected there, the rest in the renderer. The largest: the closing plant carried no O&M, so
the whole-load price is now $172 / $279 per MWh ($1,036 / $1,682 per household during the bonds, $190 / $263 after);
RA, washing, land and jobs are now at the adopted route (3,616 / 3,537 MW; 872 / 1,486 AFY; 45,361 / 66,339 acres;
1,901 / 1,214 and 601 / 664 permanent); the water with its lift is $3,280 / $5,234 an acre-foot at one head. The
capital, the register price, the studies line, the schedule and the site rankings did not move.

- **Brine carbonate sink.** Desalination brine is rich in Mg and Ca; CO₂ bubbled through it
  precipitates carbonates permanently. A disposal route for the power block's maintenance
  vents, tonnes a year, and a BENEFIT row if the numbers hold. It is **not** a release
  mitigation (`helios3.py` R-05): a loop empties in a minute and CO₂ dissolves at ~1.5 g/L,
  and the coastal modules are far from the inland nodes. Noted 2026-09-11.
