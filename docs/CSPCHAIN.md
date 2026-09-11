# cspchain.py — how a solar-thermal plant works, link by link, and where it can be made smaller while producing more

`tools/cspchain.py` is the second pass on the path the author chose: **CSP,
made better** — *"scale down in size while simultaneously increasing output."*
That is a statement about the energy chain. A tower plant turns direct
sunlight into electricity through seven multiplications:

    E = A × DNI × opt × rec × tes × dispatch × cycle × (1 − par) × avail

Size is the aperture A; output is E; so "smaller and more" means a larger
product of the seven efficiencies. The file states each link as Helios
carries it (`helios.py`'s own constants, imported, and two measured from its
hourly run), as the best achieved or credibly designed (SOURCED), and at its
physical bound — then builds two plants on the same 18.1 TWh requirement and
prices them through `heliocost.py`'s lines, so the improvement lands in the
same column as the baseline.

    python3 tools/cspchain.py
    python3 tools/cspchain.py --selftest

## The chain

| link | Helios | best | bound | what sets it |
|---|---|---|---|---|
| field optical efficiency, annual | **0.536** | 0.64 | 0.70 | SOURCED: optimised surround fields 58–64 %; mono-tower limit ~70 % |
| receiver thermal efficiency, annual | 0.88 | 0.90 | 0.95 | SOURCED: 84.7 % annual / 87.4 % design at 336–650 °C salt; particle 85–90 % |
| storage round trip | 0.995 | — | 1.0 | no gain claimed |
| dispatch: spill, start-up, part load | 0.996 | — | 1.0 | SM 2.1 rarely fills the tank; the loss is winter under-supply (F-06), not spill |
| power cycle, gross | **0.43** | **0.50** | 0.63 / 0.70* | SOURCED: subcritical reheat steam 41–44 %; sCO₂ RCBC ~50 % at 700–715 °C (STEP) |
| 1 − parasitic | 0.88 | 0.92 | 0.97 | SOURCED: sCO₂ needs ~1/6 the cooling airflow of steam; ACC fans dominate |
| availability | 0.95 | 0.96 | 1.0 | band |
| **product, sun to socket** | **0.168** | **0.252** | | **ratio 1.50** |
| kWh_e per m² of mirror per year | 432 | 649 | | |

\* Carnot at 565 °C salt / 310 K dry-cooled is 0.630; at 775 °C particles 0.704.

Three links are the story. **The cycle**: 565 °C nitrate caps steam at 43 %,
and 57 % of the heat is thrown at the desert through a fan-cooled condenser;
sCO₂ at 715 °C on particles reaches 50 % and its turbine is a tenth the size.
**The optics**: Helios's fields lose 46 % of the light before the receiver —
cosine of a sun never overhead, blocking and attenuation in fields too large
for their towers; Noor III-class fields reach 64 %. **Dispatch** claims no
gain because the model barely spills — its loss is under-supply in winter,
which a second charging path fixes.

**And one thing no link can fix: a thermal plant serves daytime load at 43 %
when a panel serves it at 100 %.** Every daytime MWh sent through the salt
costs 2.3 MWh of sunlight; sent straight from PV it costs one. So the daytime
third of a household's day should never touch the mirrors, and the heliostat
field should be sized for the **night**. That is the DEWA architecture, and it
is the single largest "smaller."

## Three plants on the same 18.1 TWh, state-owned, same lines

| | Helios as proposed | **Helios-2** | Helios-3 |
|---|---|---|---|
| mirror aperture, M m² | 42.9 | **22.5** | 18.1 |
| towers, Noor III class | 34 | 18 | 14 |
| turbine, MW | 4,941 | 2,620 | 2,620 |
| thermal storage, GWh_th | 186 | 97 | 84 |
| PV, MW_AC | 0 | 2,894 | 2,894 |
| kWh_e per m² of mirror | 422 | 522 | 649 |
| land, acres | 212,453 | 45,211 | 39,762 |
| capex net of credit, $B | 53.6 | **37.0** | 30.0 |
| **$/MWh needed** | 205 | **141** | **117** |
| $/household/yr (today 1,177) | 1,239 | **849** | 706 |
| status | as submitted | **BUILT** | PILOT |

**Helios-2** — nitrate salt, steam, PV-direct daytime, heliostat field sized
for the night, PV-fed heaters for winter — is **1.9× smaller in mirror and
delivers the same energy**, with every part already built somewhere: Noor
III's fields, Helios's own tanks and steam block, DEWA Noor Energy 1's PV-CSP
split (700 MW CSP + 250 MW PV), Midelt's PV-fed electric heaters. What it
costs is sun-only purity: a third of the energy is photovoltaic. What it buys
is a household charge of **$849 against $1,239** — and against $1,177 today.

**Helios-3** — the same architecture on Gen3 particles and sCO₂ — is 2.4×
smaller and reaches **$117/MWh, inside the firm-clean band**. It is the right
CSP: sand at 775 °C, no salt to freeze, no nitrate ceiling, a turbine the size
of a desk. It is a >1 MW_t pilot at Sandia and a 10 MWe sCO₂ demonstrator in
San Antonio, not a 2030 plant. It is priced so the author can see what the
technology is worth; it is not offered as the build.

## Status

ASSUMED, each named in the source: the daytime share (0.35, `firmpower.py`'s
band), the night-peak ratio (1.3), the winter heater sizing (a quarter of the
night block's thermal input, 20 % PV overbuild), the sCO₂ block ($900–1,250
/kWe) and particle storage ($10–22/kWh_th) unit rates. SOURCED: every link's
best value; the built plants; STEP (10 MWe, 715 °C final phase, turbine at
27,000 rpm, first power May 2024) and G3P3 (>1 MW_t, ~800 °C particles,
bauxite at $2/kg); the hybrid LCOE reductions the literature reports (PV-CSP
up to 22 %, with electric heaters 14 %, sCO₂ a further 42 % at small scale);
and the 2025 particle-sCO₂ TEA's whole-system **$5,900/kWe** at design point,
against which Helios-3's thermal block lands within the selftest's 40 %.

The selftest asserts the chain reproduces `helios.py`'s per-m² yield to 10 %
before it is used, every Helios value is at or below its best and every best
at or below its bound, both cycles sit under Carnot at their temperatures,
two links claim no gain, both designs deliver exactly the requirement, the
price ordering is proposed > Helios-2 > Helios-3, the credit lands on storage
and heaters only, the PV share is a minority, and the report refuses to offer
the pilot as the build.

## What it does not do

It does not run Helios-2 hour by hour — that is `helios.py`'s job and the
next step, so the dispatch link is the literature's rather than the model's.
It does not choose between 2 and 3; it says 2 is buildable and 3 is better.

## The critical case (added 2026-09-11)

`design(kind, case="critical")` runs the author's standing rule — simulate critical, not
optimal. `CRITICAL_LINKS` takes optics to the bottom of the sourced surround-field band (0.58),
the sCO₂ cycle to 0.45 (dry-cooled at hot ambient, ASSUMED band 0.45–0.50), parasitics to 0.90
and availability to 0.92; PV to its low capacity factor; every cost band to its top; and for
Helios-3 the receiver link to `receiver.py`'s critical open-aperture figure (0.690 after the
2026-09-11 review of the record; 0.795 before it) by a lazy import, because `receiver.py`
imports this file. Storage and dispatch claim no gain either way. Helios-3 at critical: 30.9 M m²
against 18.1, and `helios3.py` prices it at $202/MWh against $125. Mid is unchanged and remains the default.
