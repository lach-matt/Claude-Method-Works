# DEF-153L — §D.5.5's governing claim about fibration is false at seventy-seven elements.

M asked what if the two failing fibres are not fibres, or are not what we think. Tested four ways.

## 1. They are fibres, and the law/theorem split is not what breaks them

    law · physics       alone    cells 3  box 8   E = 3
    theorem · physics   alone    cells 2  box 4   E = 2
    MERGED into one · physics    cells 5  box 12  E = 3

Merging them does not close them. §D.5.5 already ran the same test on the word *law* itself and kept
the classification "not because it is right but because it is the coarsest of the three and
therefore the strongest available statement".

## 2. But §D.5.5's reason for that is measurably false now

§D.5.5 states: **"E falls as the fibration is refined, and reaches zero by refinement alone."**
It measured that on thirty-two elements, and it is the load-bearing claim of the section — the
promotion question is settled with it ("Reading B adds a fibre and reading A adds two, so both make
E = 0 cheaper than it already is").

Measured at seventy-seven, on §D.5.5's own convention (E summed across fibres):

    fibration            fibres   total E        §D.5.5's table at 32
    none — one fibre        1        4                  4
    language only           6        6                  3
    kind only               7        9                  2
    kind × language        24        5                  0

**It is not monotone.** E rises from 4 to 9 as the fibration refines, then falls to 5. At
thirty-two elements refinement did fall monotonically to zero, and the appendix generalised that
observation into a principle. The principle does not survive the index growing.

If refining does not reliably reduce E, then "adding a fibre makes E = 0 cheaper" does not follow,
and §D.5.5's settlement of the promotion question rests on a premise that no longer holds. The
classification may still be right; the argument given for it is not.

## 3. And the appendix's chosen fibration is COSTING it, not sheltering it

§D.5.5's worry is that fibring is a place to hide: *"Λ's E(Λ) = 0 is computed at the coarsest
fibration there is — a single fibre, 976 cells, no categorical axis to hide behind. That is the
strong form. This appendix's is the weak form, and the book has been printing both under one name."*

At seventy-seven elements the strong form is the BETTER one:

    all 24 fibres collapsed to one    cells 13  box 20  **E = 4**
    as printed, kind × language                          E = 5

The appendix closes better undivided than divided. Whatever else the fibration is doing, at this
size it is not concealing a defect — it is manufacturing one.

## 4. The route that does close them is §D.5.6's, and half of it is already done

§D.5.6 is the precedent, same shape as ours: `theorem · order` admitted `proved · sampled · none
found` and held nothing there, and the repair was **not** a new element. *"The re-closure found a
defect that was not in the index but in the evidence for one of its elements, and the repair was to
prove a thing that had been sampled."*

Tested per element:

    THEOREM · PHYSICS — the necessity of state at
      verified · sampled · none found      E = 2   (as printed)
      verified · exhaustive · none found   E = 0
      proved · exhaustive · none found     E = 0
      unwitnessed · exhaustive · none found E = 0

    LAW · PHYSICS — the observability boundary at
      verified · sampled · found           E = 3   (as printed)
      verified · exhaustive · found        E = 1
      proved · exhaustive · found          E = 0
      unwitnessed · exhaustive · found     E = 2

**theorem · physics turns on the verification alone, not on the status** — any status closes it so
long as the verification is `exhaustive`. Register 1460 demoted it to `sampled` because the *104 of
106* figure was not independently reproducible. §34.6 no longer rests on that figure: BUILD96 has it
resting on the hull geometry, which is proved and which `tools/slopeaxis.py --selftest` checks at
**0 mismatches over all 106 steps in both forms**. So the sampling is no longer necessary, exactly
as ℛ's sampling was not necessary at §D.5.6. **This is not promoting to fit; the evidence actually
changed.**

**law · physics is a different case.** It closes only if the observability boundary is `proved`, and
nobody has proved it. §D.5.6's route is unavailable there, and C — find or write the element that
occupies `proved · exhaustive · found` — remains what is left.
