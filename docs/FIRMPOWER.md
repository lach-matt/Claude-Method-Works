# firmpower.py — the second pass: what equipment makes a firm megawatt-hour

`tools/firmpower.py` answers the question the first pass through
`proposals/FLAWS.tsv` ended on. At the scale proposed, priced from unit rates,
the salt-tower plant needs $171–253/MWh and charges a household **more** for
generation than the IOU does today; no size fixes that, because the three
largest cost lines scale with the plant. The author then set the second pass
exactly: *3 million households is a minimum, growing with population; one
facility or a hundred, the equipment is the same — make the system smaller,
and make it produce more.* That is a question about equipment.

    python3 tools/firmpower.py
    python3 tools/firmpower.py --selftest

## The requirement and the criterion — imported, not restated

18.1 TWh/yr firm (`helios.hh_demand_twh()`: 3 M × EIA 2024's 6,036 kWh/yr),
growing 1.70× over the term; state-owned at 3.85 %; groundbreaking 2028–2030;
heliocost.py's escalation and ownership lines; the household compared against
today's $1,177/yr IOU generation charge. The CSP row is heliocost.py's own
mid case, imported and scaled, so the comparison shares the first pass's
baseline by construction and the selftest asserts it to 2 %.

## The table (mid case)

| candidate | MW | $B net | **$/MWh** | $/household/yr | vs today | acres |
|---|---|---|---|---|---|---|
| Enhanced geothermal (Fervo class) | 2,297 | 11.1 | **57** | 343 | −71 % | 3,445 |
| **Salton Sea geothermal, flash** | 2,297 | 11.9 | **62** | 375 | −68 % | 4,594 (2 % over the field's cap) |
| Small modular reactor | 2,247 | 24.5 | 102 | 617 | −48 % | 1,123 — **BARRED** (PRC §25524.2) |
| PV-charged nitrate salt (Helios tanks + turbines) | 13,040 PV | 49.9 | 193 | 1,168 | −1 % | 78,240 |
| PV + 100-hour iron-air | 13,609 PV | 52.8 | 199 | 1,203 | +2 % | 81,651 |
| Salt-tower CSP as proposed (heliocost mid) | 4,941 | 53.6 | 205 | 1,239 | +5 % | 212,453 |
| today, IOU generation charge | | | 195 | 1,177 | | |
| firm-clean contract band | | | 80–120 | | | |

## Smaller and produces more, literally

Salton Sea geothermal delivers the same 18.1 TWh from **2,297 MW instead of
4,941 — 2.15× less nameplate — on 4,594 acres instead of 212,453, 46× less
land, at a capacity factor of 0.90 against 0.49.** It runs at night, in
winter and through a week of cloud, because it does not use the sun. It needs
no mirrors, towers, receivers or salt. And it sits in the proposal's own
Imperial node: the field is rated at **2,250 MW developable now** and 2,950 MW
in all, of which 400 MW has been built — the developable figure alone is
**17.7 TWh/yr, 0.98 of the requirement.**

**It meets the criterion.** At $62/MWh a household pays $375/yr, −68 %
against today. It lands *below* the contract band, and two things put it
there: the bond rate, and a federal credit that is real for geothermal where
it is zero for the solar field — §48E survives for geothermal at 100 % through
2033, so a public owner takes 50 % back as direct pay. **Without the credit it
is $103/MWh, still inside the band**: the credit is a margin, not the case.
Enhanced geothermal prices the same, is not capped by one field, and SCE
already holds 320 MW of it under a 15-year contract; Google signed 396 MW in
September 2026.

## What runs against it — each real, none moving the price by CSP's factor

The Salton Sea brine is hypersaline — a quarter salt by mass — and it scales
and corrodes; that is why the field has sat at 400 MW for thirty years and why
Hell's Kitchen has slipped its milestones twice. The capex band ($6,000–9,000
/kW) carries a hypersaline penalty over NREL ATB's flash figure and is
**ASSUMED, not sourced** — Hell's Kitchen's $1.8 B / 49.9 MW includes a
lithium plant and is not a power figure. The 2,250 MW is a resource estimate,
not a drilling programme. A forty-year plant budgets makeup wells or its
capacity factor walks down toward The Geysers' 53 %. Brine handling, H₂S,
induced seismicity and subsidence are permit conditions with a record.

## The portfolio the numbers point at

| | MW | TWh | $B net | $/MWh |
|---|---|---|---|---|
| Salton flash to its cap | 2,250 | 17.7 | 11.6 | 62 |
| remainder, PV-charged salt | small | 0.4 | — | ~190 |
| growth to 1.70×, PV-charged salt | ~9,100 PV | 12.6 | ~35 | ~190 |

Base on what exists; grow on what is cheap. The PV-charged-salt row keeps
Helios's tanks, turbines and nitrate — everything the author decided — and
replaces the one line with no provenance, the heliostat field, with the
most-built generator on earth feeding resistance heaters. It is the least
sourced row (heater and night-peak terms ASSUMED), and it is only marginally
cheaper than CSP because a 0.42 round trip through the turbine makes the night
share cost 2.4 PV MWh per MWh delivered. For growth, EGS at $57 is the
cheaper option if a second field is drilled; the table prices both.

## What the file refuses

It does not choose. Nuclear is priced and marked **BARRED** because California
law bars it, not because the number is wrong. Offshore wind is out of the
sized table because it is not firm and two of three Morro Bay leases are gone.
Gen3 particle CSP — sand at 700 °C into an sCO₂ turbine, a sixth more
electricity per unit of heat, no salt to freeze — is the right CSP and is a
pilot at Sandia; it is not a 2030 plant.

## The author's larger point, in the arithmetic

A firm plant that is not sun-bound needs no 16-hour store for the night, so a
fleet of them holds reserve in the plants themselves; as neighbours adopt the
model the export a state must carry falls, and what stays is a plant sized to
its own households with the geothermal base as the emergency capability.
That is the shape of a scaled-down local operation, and the geothermal row
already has it.

## Sources reached in the 2026-09-11 survey

Salton Sea KGRA: 400 MW built, 2,250 MW developable, 2,950 MW total (CEC /
LBNL); lithium 150–200 mg/L, 4.1–18 Mt LCE (LBNL 2023). Fervo Cape Station:
$7,000/kW phase 1, $5,500 target, $3,000 long-term (Q2 2026 results); SCE
320 MW / 15 yr; Google 396 MW (2026-09-01); EGS LCOE $90–140. Lazard 2025:
geothermal $71–111/MWh unsubsidized; 4-h BESS LCOS $115–254. EIA 2024:
geothermal fleet CF 65 %, The Geysers 53 %. IID–CTR PPA $69 → $93/MWh.
LBNL 2025: utility PV $1.61/W_AC (2024). EIA: CAISO curtailed 3.4 TWh in
2024, 93 % solar. Form Energy: $20/kWh target, ~$33 implicit, 100 h. TVA IRP
2025: Clinch River $17,949/kW first unit, $12,471 subsequent; Darlington
C$20.9 B / 1,200 MW. Diablo Canyon: NRC renewed to 2044/2045 (2026-04-02);
operation past 2030 needs the Legislature. Offshore wind: LCOE+LCOT $95–121
(2035); two of three Morro Bay leases terminated. G3P3: ≥700 °C particles,
sCO₂, bauxite at $2/kg, pilot. Kyoto 56 MWh Heatcube (2025); Rondo $20–30
/kWh_th. OBBBA: §48E retained for geothermal, storage, nuclear at 100 %
through 2033; solar terminated for construction after 2026-07-04; elective
pay retained; domestic content mandatory for public >1 MW from 2026.
