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
| contract price, $/MWh (Title I with its register) | 126 | 205 |
| volume per module, GWh/yr at 3.0–3.6 kWh/m³ | 185 | 222 |
| energy's share of the water's cost | 15% | 19% |

**The one shared asset.** Title I's summer surplus — the field it would otherwise defocus — lifts
Title II's product water to an elevated reservoir, and the year-round delivery returns through
pump-turbines to Title I's evenings. The reservoir and the pump-turbines are Title I's (they close
its season); the modules are Title II's (they make its water); the lift energy is the surplus, priced
at nothing because it was worth nothing.

## 2. The decision

Hour by hour, Title I as sized serves 87 % of its load, the shortfall year-round and evening-led.
Two routes close it; what separates them is water and the size of the block. **The author chose
both** (2026-09-11): the water returns half the shortfall and the field and store carry the other half,
so the plant is served by two things that fail differently (`both.py`).

| | mirrors, mid | mirrors, critical | water, mid | water, critical | **both, mid** | **both, critical** |
|---|---|---|---|---|---|---|
| Title I additional capital, $B | 5.7 | 9.5 | no feasible point | no feasible point | **6.4** | **10.3** |
| Title I price, $/MWh | 168 | 272 | — | — | **172** | **279** |
| block, field, store | ×1.25, ×1.5, 2 d | ×1.25, ×1.5, 2 d | field and store at design | field and store at design | ×1.50, ×1.25, 1.0 d | ×1.50, ×1.25, 1.0 d |
| Title II modules | 0 | 0 | — | — | 15 | 17 |
| Title II capital, financed, $B | 0 | 0 | — | — | 28 | 48 |
| water, million acre-feet a year | 0 | 0 | — | — | 0.75 | 0.83 |
| water price with the lift, $/acre-foot | — | — | — | — | 3,280 | 5,234 |
| left to the grid | 0.8% | 1.0% | — | — | 0.6% | 0.7% |
| with the water withheld | — | — | — | — | 3.6% | 4.0% |
| with the field at design | — | — | — | — | 1.3% | 1.4% |

Water alone is not a route on this load: with the field and store at design no point both closes and lifts
its water inside the plant's own surplus, since the block that closes the evening eats the spill the lift
runs on. Both costs 1.12× / 1.09× the mirrors on Title I's account, the pump-turbine plant being bought
whole whatever share it returns. What it buys: with either route out, 1%–4% of the load
is left to the grid against 13% with neither, and 0.75–0.83 million acre-feet a year of
water. The even split is the author's word read literally; the ladder over the water's share is in
`both.py` and the split can be moved.

**The takers.** The adopted route delivers 0.8–0.8 million acre-feet a year, year-round: summer
irrigation on the Westside and winter recharge, where the San Joaquin Valley's groundwater overdraft under
SGMA is about 1.8–2.5 million acre-feet a year. That is the match of supply to demand the joinder
rests on, and it is a contract question: irrigation and recharge districts under contract for firm water
at three to five thousand dollars an acre-foot, which is what firm water costs.

**The decision is the author's, and it is made**: both. Title I at the combined price, Title II at
half the shortfall's scale, and firm water California does not otherwise have.

## 3. The single financial statement

| | mid | critical |
|---|---|---|
| Title I capital with its register, $B | 32.7 | 55.4 |
| Title I closing the load, mirrors / both, $B | 5.7 / 6.4 | 9.5 / 10.3 |
| Title II modules at the adopted route, $B | 28 | 48 |
| **program at the adopted route (both), $B** | **67** | **114** |
| Title I debt service, $M/yr | 1,855 | 3,148 |
| Title I debt-service reserve, $M | 1,855 | 3,148 |
| contingency carried | 15% | 30% |
| Title I price at 1.25× coverage, $/MWh | 152 | 248 |

The security behind both projects' bonds is contracted offtake at the required price — electricity
to load-serving entities, water to districts — with a state general-obligation backstop for the
first-of-kind rungs of Title I's ladder. Priced to each security in Title I §5; the same ladder of
securities applies to Title II's modules. The downside case is the critical column, by the author's
standing rule; a revenue bond's coverage is stated above it.

## 4. Severability

- **Title I without Title II** stands: the field and store grow to the mirrors route's sizing, the
  load closes at that price in §2, and no water is made.
- **Title II without Title I** stands: a module buys its electricity from the grid instead of the
  Authority, at the grid's price rather than the contract's, and makes the same water; the water
  route's reservoir and pump-turbines are not built, and the water is delivered by the aqueduct.
- **What does not sever** is the water route itself: it exists only as the pair, because its lift is
  Title I's surplus and its winter is Title I's shortfall. It is the joinder, and it is optional.

## 5. What Title III does not settle

- The site of the reservoir, and so the head: 500 m is assumed and each doubling halves the modules.
- The takers: irrigation and recharge districts under contract, year-round, at firm-water prices.
- The brine as a carbonate sink for the power block's maintenance vents: noted, not priced.
- The split of the shortfall between the two routes: adopted even, movable on `both.py`'s ladder.

*Rendered by `tools/rebase3.py`; do not edit by hand. Re-render after any change to the instruments.*
