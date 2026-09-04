# DEF-153K — the Rubik sweep over Appendix D. Reordering is ruled out by measurement.

M's method, from register 1524: **E depends on the ORDER of a coordinate's values.** `rubik.py`
swept 7! × 4! = 120,960 orderings of the law index; E ran from 0 to 21 and **288 reached zero**,
and the closing carrier order — `u < p < ℓ−ℓ_core < Z−T` — turned out to be monotone in how LOCAL
the variable is. The ordering that closed it was itself the finding.

Applied to Appendix D. §D.2 declares three ordered coordinates:

    status        withdrawn < conjectured < measured < verified < unwitnessed < proved
    verification  cited < sampled < exhaustive
    precedent     none found < found

All 6! × 3! × 2! = **8,640 orderings** swept, ℛ imported from `cypher.py` (never reimplemented),
E recomputed over the ten fibres that carry more than one cell.

## The result

    §D.2 as declared                            total E = 5, across 2 non-closing fibres
    best ordering found                         total E = 2, across 2 non-closing fibres
    orderings closing ALL TEN live fibres       0 of 8,640

    law · physics       closes alone under      2,160 of 8,640
    theorem · physics   closes alone under      4,320 of 8,640
    both together                               1,440 of 8,640
    both AND the other eight                    **0**

**No ordering closes Appendix D.** Each failing fibre is individually orderable to closure — and
1,440 orderings close both at once — but every one of those breaks a fibre that closes today. The
ordering is a global constraint and the fibres want incompatible ones.

That is the opposite of the law index's result, and the contrast is the point: there, a reordering
existed and it MEANT something. Here none exists, and the least-bad ordering
(`withdrawn < conjectured < verified < proved < measured < unwitnessed`, with measured ranked above
proved) is semantically incoherent, so it would not be worth taking even if it closed.

**Reordering is therefore ruled out as a route.** The defect is not an artefact of §D.2's choice of
order. It is in the elements.

## One question the sweep did raise

`law · physics` closes under §D.2's declared STATUS order untouched, if `precedent` is reversed to
**`found < none found`**. That is a real subject-matter question rather than a mechanical one.
§D.5.2 reads the coordinate as *"a record of the search, not of the world — none found means this
work found none"*. Under that reading, is finding a precedent MORE than finding none, or less? The
declared direction says more. The closure prefers less. Recorded, not resolved.

## What it does to the ruling

Option C — fill the six named cells — is not weakened by this; it is what is left. Option B —
correct §D.1 and §D.5.10 to say E = 0 in twenty-two of twenty-four — remains available and is now
the honest fallback rather than a concession, since no ordering rescues the claim as written.
Option A (restore the necessity of state to `verified · exhaustive`) closes theorem · physics but
leaves law · physics open at E = 3 and trades a true statement about verification for it.
