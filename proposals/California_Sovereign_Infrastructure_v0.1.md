# California Sovereign Infrastructure Act — Merged Proposal, v0.1

**Status: AS-SUBMITTED MERGE. No figure, claim or sentence has been altered.**

This document joins two source proposals into one, under one authority and one
balance sheet, as the author's decision of 2026-09-11 directed: *one program,
two projects, severable.* Title I is the energy proposal and Title II the water
proposal, each carried verbatim from its source. Where a source table was
flattened by PDF extraction it has been re-set as a table; every cell is the
source's own. Section numbers inside each Title are the source's own.

The merge deliberately carries every figure the adversarial review
(`FLAWS.tsv`) will then contest. Nothing is repaired here, so that every repair
is visible as a diff against this version.

| Title | Source document | Drive id | Author's date |
|---|---|---|---|
| I | *California Energy Independence Project* (PDF) | `1UqsvwqcZkpKLi_pUX5KoB4Fv5lROJAri` | 2026-09-09 |
| II | *California Sovereign Water and Mineral Infrastructure Initiative* (Google Doc) | `19lpGhiBxFBfMnnaMfZq4dT9QnIpG1ShpP5LkBeijAYM` | 2026-09-10 |

Author of both: Matthew Lach.

---

# TITLE I — STATE LEGISLATIVE & EXECUTIVE POLICY PROPOSAL FOR SOVEREIGN ENERGY INDEPENDENCE

By: Matthew Lach 2026-09-09

**Program Identifier:** Program Helios-1M (California Sovereign Model)
**Sponsoring Entity:** California Power Authority (CPA) Sovereign Infrastructure Network
**Target Beneficiaries:** 3,000,000 California Households ($0.00 / kWh Generation Rate)
**Export Strategy:** Out-of-State & WEIM Evening Peak Arbitrage via Existing 500 kV Transmission Corridors

## 1. EXECUTIVE SUMMARY & SYSTEM ARCHITECTURE

California's energy market suffers from extreme volatility: mid-day wholesale prices regularly plunge toward zero due to photovoltaic overproduction (the "Duck Curve"), while evening peak hours face severe capacity constraints and high wholesale clearing prices. Program Helios-1M constructs a 5,250 MWe (5.25 GWe) state-owned Concentrated Solar Thermal (CST) network across three desert nodes. By charging 197,184 MWh_th of binary molten salt storage during low-value daytime hours and dispatching firm power during the evening ramp, the state eliminates household generation charges for 3,000,000 families while capturing premium out-of-state export revenues to fund the program.

## 2. ENGINEERING & THERMODYNAMIC SPECIFICATIONS

```
+-----------------------------------------------------------------------------------+
| HELIOS-1M STATEWIDE NODE BALANCING (3 NODES)                                      |
|                                                                                   |
| GROSS INSTALLED GENERATION: 5,250 MW_e                                            |
| ├── In-State Municipal Delivery: 3,000 MW_e ($0.00/kWh Generation Tariff)         |
| ├── Internal Parasitic Load: 735 MW_e (Pumps, ACC Fans, Heat Exchangers)          |
| └── Net Out-of-State Export: 1,515 MW_e (Evening Peak WEIM Dispatch)              |
|                                                                                   |
| THERMAL STORAGE & FIELD SPECS:                                                    |
| ├── Total Storage Capacity: 197,184 MWh_th (16-Hour Full Discharge)               |
| ├── Molten Salt Inventory: 1,665,000 Metric Tons (Binary Nitrate Salt)            |
| └── Micro-Heliostat Aperture: 45.6M m² Total (Solar Multiple = 5.0)               |
+-----------------------------------------------------------------------------------+
```

### 2.1 Thermodynamic Performance Matrix

| Engineering Parameter | Per-Node Specification | Statewide Network Total | Design Standard |
|---|---|---|---|
| Gross Nameplate Output | 1,750 MWe | 5,250 MWe | Multi-module supercritical Rankine steam cycle |
| Solar Multiple (SM) | 5.0 | 5.0 | Guaranteed 16-hr storage charge during winter DNI minimums |
| Thermal Storage Capacity | 65,728 MWh_th | 197,184 MWh_th | Dual-tank hot (565 °C) / cold (290 °C) salt system |
| Active Mirror Surface | 15.2M m² | 45.6M m² | Dual-axis tracking 2 m × 2 m micro-heliostat arrays |
| Central Tower Structures | 4 × 220 m towers | 12 Concrete Towers | Slip-form concrete with 360-degree cavity receivers |
| Water Consumption (ACC) | ~135 acre-ft/yr | ~405 acre-ft/yr | Dry-air cooling (<8% of conventional wet-cooled plants) |

## 3. TRANSMISSION INTEGRATION & OUT-OF-STATE EXPORT ROUTING

```
MOJAVE NODE (1.75 GW)          IMPERIAL NODE (1.75 GW)        CENTRAL VALLEY NODE (1.75 GW)
        │                              │                              │
        ▼                              ▼                              ▼
Lugo / Victorville Subs      Devers-Colorado River Sub        Path 15 / Gates Sub
        │                              │                              │
        ├──> Path 26 (CAISO North)     ├──> SDG&E / Palo Verde Hub    └──> PG&E / Pacific DC Intertie
        └──> NV Energy WEIM Hub        └──> Arizona / Southwest WEIM       └──> Pacific Northwest (BPA)
```

1. **Mojave Desert Node (Kramer Junction Area):** Interconnects with the Lugo and Victorville 500 kV substations, utilizing Path 26 for internal state balancing and feeding directly into the NV Energy WEIM hub for out-of-state evening sales.
2. **Imperial Valley Node (Desert Center Area):** Interconnects with the Devers-Colorado River 500 kV corridor, creating an export bridge into Arizona utilities and the Palo Verde wholesale hub.
3. **Central Valley Node (Westside Corridor):** Interconnects with Path 15 and Gates 500 kV substations, linking northern load centers to the Pacific DC Intertie (±500 kV DC) for seasonal Pacific Northwest power exchanges.

## 4. MACROECONOMIC & FINANCIAL CROSS-SUBSIDY MODEL

### 4.1 Capital Expenditure & Debt Service (Audited Baseline)

- Total Turnkey EPC & Switchyard CapEx: **$27.2 Billion**
- Financing Structure: 30-Year Tax-Exempt California Power Authority Revenue Bonds @ 3.85% Fixed.
- Annual Bond Debt Service: **$1,523 Million / year**
- Annual System O&M & Grid Interconnect Fees: **$410 Million / year**
- Total Annual Program Carrying Cost: **$1,933 Million / year**

### 4.2 Out-of-State Evening Peak Revenue Math (1,515 MWe Net Export)

Annual Export Volume = 1,515 MWe × 8,760 hours = **13,271,400 MWh / year**

| Out-of-State Export Market Scenario | Realized Evening Peak Price | Annual Export Energy Revenue | CAISO Resource Adequacy (RA) Value | Total Program Revenue | Net Cost Coverage ($1.933 B Req) | Annual Net Surplus to CA State Treasury |
|---|---|---|---|---|---|---|
| Conservative Evening Peak | $0.190 / kWh ($190/MWh) | $2,521.6 M | $450.0 M | $2,971.6 Million | 153.7% Covered | +$1,038.6 Million / yr |
| Target WEIM Regional Peak | $0.270 / kWh ($270/MWh) | $3,583.3 M | $450.0 M | $4,033.3 Million | 208.6% Covered | +$2,100.3 Million / yr |
| High-Scarcity Intertie Peak | $0.350 / kWh ($350/MWh) | $4,645.0 M | $480.0 M | $5,125.0 Million | 265.1% Covered | +$3,192.0 Million / yr |

## 5. RESIDENTIAL RATE TRANSFORMATION (CALIFORNIA)

```
===================================================================================
CALIFORNIA HOUSEHOLD MONTHLY BILL COMPARISON (1,000 kWh/mo)
===================================================================================

EXISTING IOU TARIFF (SCE / PG&E / SDG&E Weighted Average)
├── Generation Supply Charge ($0.195/kWh) .................... $195.00
├── Distribution & Local Delivery ($0.145/kWh) .............. $145.00
└── Public Purpose & Wildfire Surcharges ($0.040/kWh) ........ $40.00
-----------------------------------------------------------------------------------
TOTAL MONTHLY BILL: $380.00 / month        ANNUAL HOUSEHOLD OUTLAY: $4,560.00 / year

PROPOSED CALIFORNIA POWER AUTHORITY (CPA) SOVEREIGN TARIFF
├── Generation Supply Charge (CPA Export Cross-Subsidy) ..... $0.00
├── Distribution & Local Delivery ($0.120/kWh) .............. $120.00
└── Wildfire Mitigation Trust Fee ($0.020/kWh) .............. $20.00
-----------------------------------------------------------------------------------
TOTAL MONTHLY BILL: $140.00 / month        ANNUAL HOUSEHOLD OUTLAY: $1,680.00 / year

===================================================================================
NET HOUSEHOLD SAVINGS: $2,880.00 / year (-63%)
===================================================================================
```

## 6. ENVIRONMENTAL MITIGATION & ECOLOGICAL COMPLIANCE

- **Zero Groundwater Depletion:** Utilization of closed-loop Air-Cooled Condensers (ACCs) cuts water consumption by 92%, restricting total site water use to mirror washing (~405 acre-feet/year across all 3 nodes).
- **Avian Flux Protection:** Implementation of automated micro-heliostat tracking defocus algorithms prevents concentrated solar flux hot spots during standby, keeping ambient flux below 10 kW/m².
- **Wildlife Protection Corridors:** Elevated pylons (1.8 m clearance) combined with designated 12-meter wide unpaved ground corridors preserve natural migration paths for desert tortoises and local fauna.
- **Decarbonization Impact:** Displacing fossil-fueled peaking plants during high-demand evening hours eliminates 11.8 Million Metric Tons of CO₂ annually from the Western Interconnection.

## 7. ECONOMIC DEVELOPMENT & LABOR COMMITMENTS

- **Project Labor Agreements (PLAs):** Mandatory state-level PLAs ensuring prevailing wage standards, union health/pension contributions, and local apprenticeship utilization.
- **Job Creation Metrics:**
  - Construction Phase: 22,500 skilled union craft jobs over a 4-year structured buildout.
  - Permanent Operations: 1,350 high-paying engineering and operations roles managed by the State Power Authority.
  - Economic Multiplier: An estimated $4.2 Billion in regional economic activity injected into San Bernardino, Imperial, and Kern counties.

## 8. LEGISLATIVE IMPLEMENTATION TIMELINE

- **Phase 1 (Q3–Q4 2026):** Introduction of the California Power Authority Energy Sovereignty Act in the State Legislature; authorization of $28B in tax-exempt revenue bonding.
- **Phase 2 (Q1–Q4 2027):** Programmatic Environmental Impact Review (PEIR) under CEQA; finalization of state desert land leases and CAISO interconnection switchyard agreements.
- **Phase 3 (2028–2029):** Civil grading, tower slip-forming, binary salt tank fabrication, and micro-heliostat field deployment.
- **Phase 4 (Q2 2030):** Commercial Operation Date (COD); activation of the export cross-subsidy engine; 3,000,000 California households transition to $0.00/kWh generation supply tariffs.

## SECTION 9: RISK MATRIX & MITIGATION PROTOCOLS

Deploying a state-backed infrastructure network of this magnitude requires transparent identification of project risks and structural countermeasures. The California Power Authority (CPA) framework embeds direct risk mitigation into its engineering, financial, and legal structures.

| Risk Category | Identified Threat Vector | Impact Severity | CPA Mitigation & Countermeasure Protocol |
|---|---|---|---|
| Geological & Seismic | Active fault line proximity in Southern/Central California desert zones. | High | All central towers and thermal storage tanks are engineered to CBC Title 24 Seismic Zone 4 standards, capable of withstanding peak ground acceleration (PGA) up to 0.75 g. Dual-walled hot/cold salt tanks include automated seismic shut-off valves to isolate fluid loops instantly. |
| Supply Chain & Material | Global bottlenecks in high-purity battery-grade or solar-grade nitrate salts (NaNO₃ / KNO₃). | Medium | The binary salt requirement (1.665M metric tons) is phased across a 36-month procurement window. Pre-negotiated supply agreements with domestic industrial chemical manufacturers and South American producers bypass single-source dependencies. |
| Regulatory & Permitting | CEQA litigation delays or endangered species habitat disputes (Desert Tortoise). | Medium | Program Helios-1M sites are restricted strictly to state-owned or previously disturbed agricultural/industrial buffer lands. The legislative bill includes a statutory CEQA streamlining provision modelled after critical infrastructure fast-track mandates, capping judicial review windows at 180 days. |
| Wholesale Market Price Volatility | Compression of out-of-state evening peak pricing due to regional battery storage deployment. | Low-Medium | Even under conservative base-case export pricing ($0.19/kWh), debt coverage sits at 153.7%. Furthermore, the inclusion of multi-year Resource Adequacy (RA) capacity contracts with out-of-state load-serving entities guarantees baseline revenue irrespective of spot market fluctuations. |
| Hydrological Constraints | Local opposition regarding water usage in arid desert environments. | Low | The complete elimination of wet-cooling towers in favor of Air-Coupled Condensers (ACCs) reduces total project water consumption by 92%. Total annual water demand is capped at ~405 acre-feet across all three nodes, sourced via pre-secured non-potable agricultural water rights. |

## SECTION 10: GOVERNANCE, TRANSPARENCY, & OVERSIGHT

To ensure absolute public trust and prevent fiscal mismanagement, the California Power Authority (CPA) operates under strict transparency mandates and multi-agency oversight.

```
[ CPA GOVERNANCE & OVERSIGHT STRUCTURE ]

        CALIFORNIA STATE LEGISLATURE / GOVERNOR
                        │
                        ▼
        ┌───────────────────────────────────────┐
        │   CPA Board of Directors (5 Members)  │
        │   (State Treasurer, Energy, Labor,    │
        │    Environmental Justice, Public)     │
        └──────────────────┬────────────────────┘
                           │
            ┌──────────────┴──────────────┐
            ▼                             ▼
   [ Independent Auditor ]      [ Citizens Advisory Panel ]
   (Annual Financial Audit &    (Ecosystem Monitoring, Ratepayer
    CapEx Verification)          Advocacy & Local Community Impact)
```

- **Board Composition:** The CPA is governed by a 5-member Board of Directors consisting of the State Treasurer (Chair), the President of the California Public Utilities Commission (CPUC), a representative appointed by the State Building and Construction Trades Council, an environmental justice delegate, and a consumer ratepayer advocate.
- **Independent Financial Auditing:** Every fiscal year, an independent Big-Four accounting firm conducts a comprehensive audit of the CPA export revenue accounts, debt service coverage ratios, and General Fund surplus distributions, with all reports published publicly on an open-data state portal.
- **Open-Access Energy Tracking:** Real-time generation data, thermal storage capacity levels, and out-of-state export volumes are integrated directly into CAISO and CEC dashboards, ensuring transparent tracking of the program's performance against the zero-generation-rate mandate.

## SECTION 11: CONCLUSION & ACTIONABLE DIRECTIVE

Program Helios-1M transforms California's energy landscape from a fragmented market vulnerable to price shocks and evening capacity shortages into a sovereign, self-funding power network. By anchoring utility infrastructure in proven, scalable Concentrated Solar Thermal technology with 16-hour thermal storage, the state achieves what traditional intermittent renewables alone cannot: firm, dispatchable round-the-clock generation paired with an out-of-state revenue engine. The economics are self-sustaining, the engineering is fully audited, and the public benefit is undeniable. For 3,000,000 California households, the elimination of generation charges represents an immediate, permanent boost to family financial stability. For the state as a whole, Helios-1M secures long-term energy independence, massive carbon reduction, and a recurring multi-billion-dollar sovereign revenue stream.

---

# TITLE II — CALIFORNIA SOVEREIGN WATER AND MINERAL INFRASTRUCTURE INITIATIVE: THE AQUA-SOVEREIGN NETWORK

State-owned, utility-scale water production requires escaping the trap of private debt, energy vulnerability, and ecological degradation. The Aqua-Sovereign Network is a state-operated public utility framework designed to secure California's water future through autonomous, zero-impact infrastructure. By anchoring the network in the strategic conversion of retired coastal brownfield facilities and coupling low-temperature desalination with advanced mineral recovery, closed-loop chemical cleaning, and flexible 100% on-site power generation, this initiative transforms a traditional municipal expense into a self-funding state asset that delivers direct fiscal returns to local communities and households.

## 1. Executive Pitch & Sovereign Mandate

California's historical approach to water security has relied on fragile private-public partnerships, vulnerable coastal ecosystems, and exposure to volatile energy and chemical markets. The Aqua-Sovereign Network redefines water as a protected public trust asset owned directly by the state.

Operating under state sovereign authority via drought-resilience emergency legislation, each facility repurposes dormant industrial coastal footprints to achieve absolute environmental, communal, and fiscal neutrality. The program eliminates taxpayer subsidies by transforming former waste streams into high-value industrial commodities, ensuring that water generation directly subsidizes local municipal budgets and household utility rates while maintaining a commodity stabilization buffer against global market swings.

## 2. Core System Architecture & Engineering

The technical design achieves operational independence without introducing toxic industrial hazards or relying on delicate, high-failure components.

```
                  [ AQUA-SOVEREIGN FACILITY ARCHITECTURE ]

  [ Retrofitted Brownfield Intake / ] ──► [ LT-MED Evaporator ] ──► Pure Distillate (100% Water Yield)
  [ Hybrid Subsurface Slant Wells ]      (<60°C Thermal Loop)          │
                                                                       ▼
  [ 100% On-Site Power / ]   ──► [ Closed-Loop CIP ] ──► [ ZLD Crystallization Train ]
  [ 50/50 Grid Peaking Mode ]                                          │
                                        ┌──────────────────────────────┴──────────────────────┐
                                        ▼                                                     ▼
                               Battery-Grade Lithium                                  Industrial Salts (NaCl)
                               & Magnesium Recovery                                   & Agricultural Gypsum
```

- **Brownfield Conversion & Hybrid Intakes:** Facilities are sited by converting retired coastal power plant brownfields. This strategy reuses heavy-duty marine intake channels retrofitted with physical barrier screens or pairs them with diagonal subsurface slant wells drilled beneath the seabed (or hybrid low-velocity screened channels where local geology dictates), eliminating 100% of fish and plankton entrainment while slashing civil engineering costs.
- **Low-Temperature Evaporation (LT-MED):** Operating strictly under vacuum below 60 °C, the Low-Temperature Multi-Effect Distillation system prevents mineral scaling, eliminates fragile water-filtration membranes from the water path, and runs on low-grade thermal energy.
- **Dual Power Strategy (100% Capacity + Grid Peaking):** Each plant integrates a dedicated on-site solar and steam-topping turbine array providing 100% internal power capacity. Under normal operations, the plant draws 50% cheap or negative-price power from the CAISO grid (via modernized bidirectional brownfield substation switchyards) while exporting its own clean power, but it maintains 100% full-load islanding capability, allowing it to sever grid ties instantly and run entirely on-site during heatwaves or blackouts.
- **Hermetic Closed-Loop Cleaning:** Routine maintenance utilizes an automated Clean-In-Place (CIP) architecture. Safe, food-grade organic buffers (such as citric acid) flow through sealed, dry-disconnect lines from locked reservoirs via one-way check valves. Spent wash solutions route directly into the mineral recovery train, requiring zero manual vessel opening and producing zero liquid waste.

## 3. Zero Environmental and Communal Impact

Traditional desalination plants damage local ecosystems through brine dumping and heavy noise/visual pollution. The Aqua-Sovereign Network enforces strict ecological shielding:

- **Zero Liquid Discharge (ZLD):** Reject brine is routed through an advanced high-pressure reverse osmosis (HPRO) and thermal/mechanical vacuum crystallization cascade, transforming 100% of the liquid stream into pure water and dry, marketable solid minerals. Zero brine is returned to the ocean.
- **Subterranean & Acoustic Isolation:** All mechanical pumps, crystallizers, and vacuum loops are housed within repurposed, bunker-reinforced industrial brownfield structures landscaped with native vegetation. Acoustic damping keeps boundary noise below 40 dBA (quieter than a library), preserving coastal property values and recreation.
- **Pipeline-Safe Remineralization:** Distilled water is passed through natural limestone and calcite contactor beds before grid entry. This matches the exact mineral balance of natural spring water, completely preventing lead and copper leaching from older municipal distribution pipes.

## 4. Build Assessment, Production Cost, and Timelines

To ensure the Aqua-Sovereign Network is fiscally transparent and rapidly deployable across California's coast, the project uses a standardized modular build framework anchored by brownfield site conversion.

### Capital Expenditure (CAPEX) & Production Cost Model

A standard utility-scale module sized at **50,000 AFY (Acre-Feet per Year)**—roughly 16.3 million gallons per day—serves as the baseline unit.

```
                  [ UNIT PRODUCTION COST BREAKDOWN ($/m³) ]

   Total Operating Cost: ~$0.85 per m³ (before mineral offset credits)
   ┌──────────────────────────────────────────────────────────────┐
   │ [ Energy / 50% Grid Draw ]:   $0.35                          │
   │ [ Maintenance / Labor / CIP ]: $0.20                         │
   │ [ Subsurface Well Upkeep ]:   $0.15                          │
   │ [ Consumables & General ]:    $0.15                          │
   └──────────────────────────────────────────────────────────────┘
   Net Production Cost After Mineral Sales (Lithium/Magnesium/NaCl): < $0.00 (Net-Positive Revenue)
```

- **Brownfield Conversion Economics:** Repurposing retired coastal power plants reduces total capital expenditures by 30–40% compared to greenfield site development. By utilizing existing structural foundations, heavy-haul road access, industrial-zoned real estate, and integrating modernized bidirectional substation switchyards, total facility CAPEX for a brownfield conversion module spans **$250 million to $320 million**.
- **Net Water Cost to Public:** Because secondary commodity recovery (battery-grade lithium hydroxide, high-purity magnesium, and industrial salts) fully offsets operational and capital amortization expenses—backed by a state mineral stabilization reserve—wholesale water is transferred to municipal districts at cost recovery under **$400 per acre-foot**, driving the household utility bill reduction.

### Phased Deployment Timeline

Leveraging existing industrial footprints under state sovereign drought-emergency authority compresses the lifecycle timeline to **under 24 months from breaking ground to first water delivery**.

```
                         [ BROWNFIELD DEPLOYMENT SCHEDULE ]

   Months 1–3   │ State Sovereign Brownfield Acquisition & Environmental Due Diligence
   Months 4–7   │ Site Remediation, Substation Retrofitting, & Intake/Slant Well Prep
   Months 8–14  │ Factory Fabrication of Modular LT-MED, ZLD Crystallizers, & Solar-Thermal Skids
   Months 15–20 │ On-Site Assembly, Dry-Disconnect Plumbing, & Hermetic CIP Integration
   Months 21–24 │ Commissioning, Mineral Recovery Testing, & Municipal Grid Interconnect Switchover
```

- **Months 1–3 (Siting & Acquisition):** Securing decommissioned coastal industrial/power plant land under state sovereign authorization.
- **Months 4–7 (Remediation & Substation Retrofitting):** Brownfield site prep, electrical switchyard modernization for bidirectional power draw, and intake retrofitting.
- **Months 8–14 (Modular Fabrication):** Parallel factory manufacturing of standardized LT-MED evaporators, ZLD crystallizers, and solar-thermal skids.
- **Months 15–20 (Assembly & Integration):** Craning modules into position, connecting flexible earthquake-resistant HDPE pipelines, and sealing closed-loop CIP lines.
- **Months 21–24 (Commissioning):** System stress-testing, automated sensor calibration, and initiation of water delivery to municipal reservoirs.

## 5. Financial Benefits for Municipalities and Households

By capturing the market value of dissolved seawater minerals, the facility generates surplus revenue that is redistributed directly to the public and participating municipalities.

```
                      [ VALUE-STACKED FINANCIAL MODEL ]

  [ Revenue Streams ] ─────────────► [ Public & Municipal Allocation ]
  ├─ Battery-Grade Lithium (LiOH)   ├─ 40% Offset Municipal Water Purchase Costs
  ├─ High-Purity Magnesium          ├─ 30% Direct Household Utility Bill Credit
  ├─ Industrial NaCl / Gypsum       ├─ 20% Local Infrastructure Reserve Fund
  ├─ Peak Grid Energy Export        └─ 10% State Sovereign Maintenance & Stabilization Buffer
  └─ Commodity Stabilization Buffer
```

### Direct Household Financial Impacts

- **Reduced Water Utility Bills:** Mineral sales cover 100% of facility operational and capital costs, delivering wholesale water at a fraction of traditional costs and translating to an estimated **25–40% reduction in monthly household water bills**.
- **Eliminated Infrastructure Repair Costs:** State-funded, pre-remineralized water prevents pipe scale and corrosion, saving individual homeowners thousands in premature plumbing and appliance replacements.

### Municipal & Regional Financial Impacts

- **Zero Taxpayer Burden & Subsidies:** Entirely self-funding from day one with zero municipal bond debt, special tax assessments, or ongoing state general-fund subsidies.
- **Municipal Revenue-Sharing Dividends:** Net profits generated from high-value mineral recovery are placed into a municipal dividend pool, returning funds directly to local city budgets for schools, roads, and services.
- **Guaranteed Drought Immunity:** Municipalities locked into long-term sovereign contracts receive guaranteed water allocations regardless of drought cycles, protecting regional economies from supply shocks.

---

# TITLE III — JOINDER (placeholder, v0.1)

*Reserved.* The as-submitted sources contain no contract, balance sheet or
operating relation between Title I and Title II. The joinder — the power-supply
agreement, the shared authority, the severability clause and the single
financial statement — is the first thing the review below asks for and is
written only after the flaws in each Title are resolved. Nothing is asserted
here in v0.1.
