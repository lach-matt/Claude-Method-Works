# DEF-153I — Appendix D does not close in two of its twenty-four fibres. RECORDED, NOT REPAIRED.

## What was done

Appendix D's element set was extracted and the closure recomputed per fibre with
`tools/cypher.py --index`, under §D.2's own declared value orders.

The extraction reconciles against **four independently stated numbers**, which is why it is
trusted: **77 elements** (§D.5.10's sum), **24 fibres** (the same sum), **theorem · order = 21**
(§D.5's census) and **law · physics = 4** (§D.5.10's caption). It is 72 tabulated rows across six
element tables plus §D.5.3's five, which that section says outright are elements the table never
carried: *"the five are elements, and §D.5's table is short by five rows, not the count by five."*

## The result

**Twenty-two of twenty-four fibres return E = 0. Two do not.**

    law · physics        4 elements   3 cells   box 8   E = 2 or 3   (order, algebra)
    theorem · physics    2 elements   2 cells   box 4   E = 1 or 2   (order, algebra)

E is language-dependent: geometry, information and statistics return 0 on both; order and algebra
do not. §D.1's E is |ℛ(X)| − |X| with ℛ the closure operator of §14.2 — the ORDER language — so the
non-zero readings are the ones that count.

The cells, verified verbatim against the volume:

    law · physics       L10832 LS.law                    proved · exhaustive · none found
                        L10890 observability boundary    verified · sampled · found
                        L10892 the domain prohibition    verified · exhaustive · none found
                        L10894 rival = donor             verified · exhaustive · none found

    theorem · physics   L10834 LS.pin                    measured · exhaustive · none found
                        L10889 the necessity of state    verified · sampled · none found

## Which edit caused which — measured, not inferred

**law · physics: NOT this session's doing.** Recomputed with the observability boundary at its
BUILD94 coordinates (`conjectured · sampled · found`) the fibre still returns E = 2 or 3. It did not
close before BUILD95 and does not close now. §D.5.10's caption — *"Law · physics now holds four
elements over three cells and closes"* — was already false when written.

**theorem · physics: caused by a coordinate change, and it is reversible.** With the necessity of
state at `verified · exhaustive · none found` the fibre gives box 2, cells 2, **E = 0**. With
`verified · sampled · none found` it gives box 4, cells 2, E = 1 or 2. The demotion to `sampled` is
register 1460's ("the second is stated at 1332 and not independently reproducible"), which predates
this session. That correction was right about the evidence and broke the closure.

## A method note, because it nearly went the other way

The first run of this computation reported **four** broken fibres. It was wrong. `cypher.py` emitted

    warning: coordinate 'status': no declared value order, fell back to lexicographic.
    R depends on this order — declare it (§20.3).

Lexicographically `status` orders conjectured < measured < proved < unwitnessed < verified <
withdrawn; §D.2 declares withdrawn < conjectured < measured < verified < unwitnessed < proved. Every
E in that first run was computed on the wrong order. Declaring §D.2's three orders removed two of
the four failures. **The instrument's refusal is the only reason the number is trustworthy**, and
the first four-fibre reading must never be quoted.

## Consequence for DEF-153G / DEF-153H

The theorem/law split adds a row to `law · physics` — a fibre that does not close. It must not be
taken until this is settled: adding an element to a non-closing fibre compounds the defect and
would be scored as though the split caused it. The split stays NOT TAKEN, and the reason has
changed from "the element set is missing" (DEF-153H, since corrected) to "the index it would be
added to does not close".
