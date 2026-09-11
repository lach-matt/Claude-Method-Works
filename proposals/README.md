# proposals/

Policy proposals prepared for the California Legislature, and the one tree
here that is neither physics paper, mirror nor generated output. `papers/`
holds the physics; `method/` and `drive/` are resource material. Nothing here
writes to any of them.

## What is here

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
run.** As sized by the static chain, Helios-3 serves **84 %** of the load — the sCO₂ block cannot carry
the evening peak after sunset in any month, and December loses a third of its load while June defocuses
a quarter of its field. Closing it takes **block ×1.5 with its store, a second day of store, and field
×2**; the heater and PV overbuild were never the lever. **+$60/MWh at mid, +$100 at critical — about
$185 and $302/MWh** to serve the whole load from the plant alone. Re-basing Title I on that sizing, or
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
nothing in `FLAWS.tsv` is deleted. The same standard as `papers/` applies once
the instruments exist: every figure in the proposal is computed, carries a
status, and fails a harness if the prose states a number the model does not
produce.

## Title III joinder items

**Can Title II return Title I's winter? (`tools/joinder.py`, `docs/JOINDER.md`, 2026-09-11.)** The
author: desalinate on the summer surplus, hold the water, and return the offset from the
desalination plants' turbines. Two turbines that can mean. **Steam-topping turbines** (Title II's own
architecture) return electricity they were given as heat, less what the water took — the water costs
6.4× reverse osmosis in electricity and the turbine returns in winter only what heat is there in
winter, which F-13/F-27 found is none: it does not return a winter. **Hydraulic turbines on the water
itself** do: summer surplus desalinates and lifts the product to an elevated reservoir, winter
delivery comes back through pump-turbines. Bounded by the surplus (3.2 TWh_e thrown away), the scheme
makes **0.7 km³ of water a year** and returns **46 % of the winter at mid, 27 % at critical**, for
**$2.2 / $3.3 B** — per TWh of winter, cheaper than the field oversizing at both cases — conditional
on head and a reservoir sited where the water is wanted below it. **And the author's follow-up — more modules rather than
more storage — closes the whole winter**: with the water on Title II's own account and the surplus
spent on the lift alone, **25 modules at 500 m of head (1.25 MAF/yr) close mid for $4.8 B and 27
close critical for $8.2 B**, against $10.2 / $16.9 B of mirrors; head halves the water for each
doubling and is the lever worth more, and the water needs winter takers, which SGMA recharge is.

- **Brine carbonate sink.** Desalination brine is rich in Mg and Ca; CO₂ bubbled through it
  precipitates carbonates permanently. A disposal route for the power block's maintenance
  vents, tonnes a year, and a BENEFIT row if the numbers hold. It is **not** a release
  mitigation (`helios3.py` R-05): a loop empties in a minute and CO₂ dissolves at ~1.5 g/L,
  and the coastal modules are far from the inland nodes. Noted 2026-09-11.
