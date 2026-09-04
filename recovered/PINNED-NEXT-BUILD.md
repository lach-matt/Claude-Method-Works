# Pinned for the next build — the interval form

## The statement

> **Between any two points there is an interval, and the method returns its measure.**

Not an equation connecting two points: the orders are partial and share 0.3%.
An interval between two points: total, because every pair of cells has a meet
and a join whether or not either order relates them.

## The three legs, each already computed and none pointing at the others

| between | the interval | its measure | verified |
|---|---|---|---|
| two **cells** | [x∧y, x∨y] | d = ∏(\|Δᵢ\|+1) = τ(lcm/gcd), five forms | §9.2 |
| two **states** under composition | [min, max] output rank | 17% of 264 inputs single-valued, worst spread 12, range [3, 23] | §12.11.0.12 |
| two **measurements** | [T(n−1), T(n+1)] | w, priced at V = 4ν/3 | §20.1 |

All five composition figures reproduced exactly this session: 41,682 pairs,
264 inputs, 46 single-valued (17%), worst spread 12, range [3, 23].

## Why the form survives what "an equation" did not

- **Thm 11.2** permits it: an interval carries LESS than the coordinates, not more.
- **§18.6** permits it: an interval is a bound on where something already is, not
  a proposal about an unlisted cell — §23.6.3's own correction.
- **The 0.3% overlap becomes the content**: two intervals per pair, nearly
  disjoint, so what a thing IS and what it can BECOME are separately bounded.

## Where it goes

§9.2, §13.1 and §25 — three sections each holding one leg and none citing the
other two. §25 already proves the three MEASURES are one quantity (E, the void,
V, under slack); what is missing is that the three OBJECTS are one shape.

## What it costs

Universal over indices whose constraints are pairwise monotone envelopes, per
§14.3 — not over all mathematics. And it explains the title: an equation returns
a value; this returns an interval AND a verdict on what the interval is about,
which by the promoted §18.4.1 is whether E measures the drawing or the world.
That second half is not expressible as an equation, which is why the object had
to be a method.