# heliocost.py — what Program Helios-1M costs to build, line by line (F-05)

`tools/heliocost.py` resolves `proposals/FLAWS.tsv` **F-05**. Title I §4.1
states a capital cost of **$27.2 billion** and calls it an *"Audited
Baseline"*; no audit is cited, no line is given, and at $5.18/W it is below
every salt tower ever built. `helios.py` had shown that the author's criterion
— *the plant pays for itself after the build bonds* — turns on this one number,
so it is built from unit rates rather than asserted.

    python3 tools/heliocost.py
    python3 tools/heliocost.py --selftest

## The plant, as decided

45.6 M m² in **Noor III-class heliostats (256 k units)**, **36 towers** of
250 m with 1,700 m² receivers at 722 MW_th each, 197,184 MWh_th of salt,
5,250 MWe gross — the author's 2026-09-11 decisions on F-07 and F-08 carried
into the cost. State ownership, groundbreaking 2028–2030 (the author's own
estimate), four-year build.

## The result

| | $B net of credit | $/W | carrying $M/yr | **$/MWh needed** | at 1.25× |
|---|---|---|---|---|---|
| Title I §4.1 | 27.2 | 5.18 | 1,933 | 102 | 127 |
| **low** | 46.1 | 8.79 | 3,292 | **171** | 214 |
| **mid** | 57.0 | 10.85 | 3,966 | **206** | 258 |
| **high** | 71.5 | 13.62 | 4,871 | **253** | 317 |
| firm-clean contract band | | | | 80–120 | |

**The proposal's $27.2 B is 1.70× below the low case and 2.09× below the
mid.** The low case takes the best heliostat price ever reported ($80/m²),
SAM's 7 % contingency on a plant thirteen times larger than any built, and
the federal storage credit in full; nothing in it is generous to the proposal
and it still does not reach $27.2 B. **The criterion does not close at the
scale proposed in any case**: the low case needs 1.43× the top of the band
California pays for firm clean energy.

The mid case sits at $10.85/W, inside the built record (Crescent Dunes 8.86,
Cerro Dominador 10.45, Gemasolar 11.17) — which is the corroboration that
matters, because those are what tower CSP with long storage has actually
cost.

## The mid-case stack

| line | $M | status |
|---|---|---|
| site improvements | 938 | RECONSTRUCTED |
| heliostat field | 7,034 | SOURCED band |
| towers | 2,341 | RECONSTRUCTED |
| receivers | 5,382 | RECONSTRUCTED |
| thermal storage (tanks, salt, HX) | 6,083 | RECONSTRUCTED |
| power block | 7,761 | RECONSTRUCTED |
| balance of plant | 1,957 | RECONSTRUCTED |
| 500 kV switchyards + gen-tie | 771 | ASSUMED band |
| **direct** | **32,267** | |
| contingency 15 % | 4,840 | SOURCED band 7–30 % |
| EPC + owner 13 % | 4,195 | RECONSTRUCTED |
| CA sales tax, 8 % on 80 % | 2,065 | SOURCED — public agencies pay it |
| developer margin | 0 | state: none |
| **overnight, 2022 $** | **43,367** | |
| escalation to 2031 | ×1.305 | 3 %/yr ASSUMED |
| interest during construction, 3.85 % over 4 yr | 4,357 | |
| **gross capex** | **60,941** | |
| federal storage credit, direct pay, 50 % of storage line | −3,969 | SOURCED |
| federal solar credit | 0 | terminated for 2028+ construction |
| **net capex** | **56,973** | $10.85/W |

## What the ownership form is worth (mid case)

| | state | private |
|---|---|---|
| developer margin | 0 | 2,420 |
| IDC at 3.85 % vs 9 % | 4,357 | 10,754 |
| storage credit (energy-community bonus only for public) | −3,969 | −3,175 |
| **net capex $M** | **56,973** | **67,320** |
| O&M base (Title I) | 410 | 410 |
| CalPERS on-cost adder | 36 | 0 |
| property tax | 0 | 673 |
| PILOT to host counties, 50 % of exempted tax | 285 | 0 |
| **carrying $M/yr** | **3,966** | **7,636** |
| **$/MWh needed** | **206** | **397** |

Public ownership nearly halves the required price. It is the single largest
lever in the plant, and it is already taken. The PILOT fraction is `DESIGN` —
the author sets it; the file carries 50 % as a placeholder, not a decision.

## Status discipline

NREL's servers (`atb.nrel.gov`, `sam.nrel.gov`, `docs.nrel.gov`) are
unreachable from this environment, so the SAM default unit rates are
**RECONSTRUCTED** from the Turchi et al. 2019 cost model as carried in SAM.
Built raw, in Turchi's 2018 dollars, they rebuild the one whole-plant figure
the search did reach — **NREL ATB 2024's representative tower at $7,912/kWe
(2022 $)** — to **0.778**, the gap being four years of escalation and ATB's
own cost update. So the **level** is taken from the sourced anchor (every line
scaled by 1.285) and only the **split** between lines is the reconstruction's.
The selftest asserts the raw rebuild lands inside 0.70–1.00 (or the split is
not credible enough to calibrate), that the calibrated rebuild returns the
anchor exactly, and that the calibration is one factor on every line so the
split is unmoved. A reconstruction that reproduces a sourced anchor is
corroborated, not sourced.

Federal credits (SOURCED): elective pay under §6417 retained by the 2025 Act;
the §48E energy-storage credit at 100 % for construction beginning through
2033, so a 2028–2030 groundbreaking qualifies; domestic content mandatory for
public projects over 1 MW taking direct pay from 2026; the solar credit
terminated for facilities not under construction by 2026-07-04 unless in
service by end-2027 — Helios earns nothing on field, receivers or power block.

## What moves it

The three largest lines are the power block, the storage and the field, and
all three scale with the plant. **The number that moves the answer is not a
unit rate; it is the size** — and the size was set by a household count that
F-17 shows was computed at three different consumptions. The ownership form
and the storage credit are worth what their lines show and are already in.
Nothing else in this file is a lever.

## What it does not do

It does not resize the plant, choose a smaller first phase, or price a
PV-plus-heater alternative; those are redesigns and belong to the second pass
through the register. It prices the plant as proposed, and says the word
*"audited"* may not be used of any figure in it until an EPC has priced a
tower.

## Selftest

Twenty-seven checks: the raw reconstruction lands inside its band against the
ATB anchor and the calibrated one returns it exactly, with the split unmoved;
the decided class gives under 300 k heliostats and receivers near Noor III's
rating and SAM's reference area; low < mid < high; every line carries a
status; the three largest lines are the three that scale; escalation above
one, IDC positive and bounded; the storage credit on the storage line only
and the solar credit exactly zero; no developer margin under state
ownership; Title I's figure below the low case by more than 1.5×; the mid
case inside the built $/W record and inside helios.py's F-05 band; the
required price above the band's top at every case; state below private; the
PILOT exactly a fraction of the exempted tax; and the report names its
status, says the criterion does not close in any case, names the size as the
lever, forbids "audited", and names what it does not do.
