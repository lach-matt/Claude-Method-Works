# Title III — The Joinder (v0.2)

**What this document is.** The relation between Title I (Helios-3) and Title II (Aqua-Sovereign)
that v0.1 reserved and never wrote: the power-supply agreement, the single financial statement, the
severability, and the one decision that joins them. It is **rendered by `tools/rebase3.py` from the
instruments** and carries no number they did not compute; every number is labelled **mid** or
**critical**. The author's four standing decisions govern it: one program, two projects, severable;
nitrate stays and chloride chemistry is excluded everywhere; Noor III-class heliostats; ZLD dropped and
brine returned through the existing outfall.

## 1. The relation

One Authority, two projects, two revenue accounts. Title I sells electricity at cost recovery to
in-state load-serving entities and to Title II; Title II sells water at cost recovery to districts.
Neither subsidises the other: each carries its own capital, its own debt service and its own price,
and the joinder is two contracts and one asset.

**The power-supply agreement.** Title II buys its electricity from Title I at Title I's required
price, mid or critical, for the bond term of 30 years:

| | mid | critical |
|---|---|---|
| contract price, $/MWh (Title I with its register) | 125 | 202 |
| volume per module, GWh/yr at 3.0–3.6 kWh/m³ | 185 | 222 |
| energy's share of the water's cost | 15% | 19% |

**The one shared asset.** Title I's summer surplus — the field it would otherwise defocus — lifts
Title II's product water to an elevated reservoir, and the October-to-April delivery returns through
pump-turbines to Title I's evenings. The reservoir and the pump-turbines are Title I's (they close
its season); the modules are Title II's (they make its water); the lift energy is the surplus, priced
at nothing because it was worth nothing.

## 2. The decision

Hour by hour, Title I as sized serves 87 % of its load, the shortfall year-round and evening-led.
Two routes close it; what separates them is water and the size of the block. **The author chose
both** (2026-09-11): the water returns half the season and the field and store carry the other half,
so the plant is served by two things that fail differently (`both.py`).

| | mirrors, mid | mirrors, critical | water, mid | water, critical | **both, mid** | **both, critical** |
|---|---|---|---|---|---|---|
| Title I additional capital, $B | 5.7 | 9.5 | 11.2 | 17.0 | **7.7** | **12.7** |
| Title I price, $/MWh | 159 | 258 | 192 | 303 | **171** | **277** |
| block, field, store | ×1.25, ×1.5, 2 d | ×1.25, ×1.5, 2 d | ×2.00, ×1, 1 d | ×2.00, ×1, 1 d | ×1.25, ×1.25, 2.0 d | ×1.25, ×1.25, 2.0 d |
| Title II modules | 0 | 0 | 16 | 17 | 8 | 9 |
| Title II capital, financed, $B | 0 | 0 | 30 | 50 | 15 | 25 |
| water, million acre-feet a year | 0 | 0 | 0.79 | 0.87 | 0.40 | 0.44 |
| water price with the lift, $/acre-foot | — | — | 3,268 | 5,030 | 3,268 | 5,030 |
| left to the grid | 0.8% | 1.0% | 0.7% | 0.7% | 0.8% | 1.0% |
| with the water withheld | — | — | — | — | 1.5% | 1.7% |
| with the field at design | — | — | — | — | 5.6% | 5.9% |

Both costs more than mirrors alone on Title I's account, because the pump-turbine plant is bought
whole whatever share it returns. What it buys: with either route out, 1%–6% of the load
is left to the grid against 13% with neither, and 0.40–0.44 million acre-feet a year of
water. The even split is the author's word read literally; the ladder over the water's share is in
`both.py` and the split can be moved.

**The takers.** The adopted route delivers 0.4–0.4 million acre-feet a year from October to
April. The San Joaquin Valley's groundwater overdraft under SGMA is about 1.8–2.5 million
acre-feet a year, and winter is when recharge basins take water. That is the match of supply to
demand the joinder rests on, and it is a contract question: recharge districts under contract for
firm winter water at three to five thousand dollars an acre-foot, which is what firm water costs.

**The decision is the author's, and it is made**: both. Title I at the combined price, Title II at
half the season's scale, and firm winter water California does not otherwise have.

## 3. The single financial statement

| | mid | critical |
|---|---|---|
| Title I capital with its register, $B | 32.3 | 54.6 |
| Title I closing the season, mirrors / water, $B | 5.7 / 11.2 | 9.5 / 17.0 |
| Title II modules at the water route, $B | 30 | 50 |
| program at the water route, $B | 73 | 122 |
| **program at the adopted route (both), $B** | **55** | **93** |
| Title I debt service, $M/yr | 1,836 | 3,100 |
| Title I debt-service reserve, $M | 1,836 | 3,100 |
| contingency carried | 15% | 30% |
| Title I price at 1.25× coverage, $/MWh | 151 | 245 |

The security behind both projects' bonds is contracted offtake at the required price — electricity
to load-serving entities, water to districts — with a state general-obligation backstop for the
first-of-kind rungs of Title I's ladder. Priced to each security in Title I §5; the same ladder of
securities applies to Title II's modules. The downside case is the critical column, by the author's
standing rule; a revenue bond's coverage is stated above it.

## 4. Severability

- **Title I without Title II** stands: the field and store grow to the mirrors route's sizing, the
  season closes at that price in §2, and no water is made.
- **Title II without Title I** stands: a module buys its electricity from the grid instead of the
  Authority, at the grid's price rather than the contract's, and makes the same water; the water
  route's reservoir and pump-turbines are not built, and the water is delivered by the aqueduct.
- **What does not sever** is the water route itself: it exists only as the pair, because its lift is
  Title I's surplus and its winter is Title I's shortfall. It is the joinder, and it is optional.

## 5. What Title III does not settle

- The site of the reservoir, and so the head: 500 m is assumed and each doubling halves the modules.
- The recharge contracts: a million acre-feet a year of winter takers at firm-water prices.
- The brine as a carbonate sink for the power block's maintenance vents: noted, not priced.
- The split of the season between the two routes: adopted even, movable on `both.py`'s ladder.

*Rendered by `tools/rebase3.py`; do not edit by hand. Re-render after any change to the instruments.*
