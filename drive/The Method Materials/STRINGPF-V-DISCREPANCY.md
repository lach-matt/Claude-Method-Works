# FLAG — string partition function: log d(N) concavity vs §31.2.2 "convex"

## What the source says (§31.2.2, BUILD56 main line ~8674)
"log d(N) is monotone, convex and 3-monotone, with V ≈ 147 at N ≈ 14 — an ordinary bracketable
channel, steeper than a Rydberg series."

## What I measured this session (stringpf.py, d(N) from ∏(1−qⁿ)⁻²⁴)
- log d(N) MONOTONE increasing: CONFIRMED.
- second differences of log d(N): all NEGATIVE (−0.31, −0.21, −0.15, …, −0.039 near N=13).
  => log d(N) is CONCAVE in the calculus sense, NOT convex.

## Status: UNRESOLVED — not an error I can assert either way, and NOT carried into the IoI entry.
Two possible readings, and I do not have the book's exact definition of "convex", "3-monotone",
and "V" in this bracket context to decide:
 (1) The book's bracket vocabulary ("3-monotone", "V") may use "convex" in a methodology-specific
     sense (a property of the bracket / the sequence d(N) itself and its higher differences), not the
     second-derivative sign of log d(N). "V ≈ 147" is a bracket-count quantity, not a convexity claim.
 (2) Or "convex" is loose/erroneous and log d(N) is simply concave (as measured).
The IoI entry is about the INDEX and its E-signature; it carries ONLY verified content (coordinates,
the counts d(N), E=0 by independence) and does NOT import the convex / 3-monotone / V≈147 claim,
which is a separate statement in the spectra-bracket methodology (§31.2.2), not part of the index's
closure. That claim needs the book's definitions of V and "3-monotone" checked before it is affirmed
or corrected — deferred to the author / a bracket-methodology pass, not resolved here.

## Note (measured d(N), for the record — verified from the generating function)
d(0..14) = 1, 24, 324, 3200, 25650, 176256, 1073720, 5930496, 30178575, 143184000, 639249300,
2705114880, 10914317934, 42189811200, 156883829400.  (d(1)=24 = one excitation in 24 transverse
dims; d(2)=324 = 24 [mode-2] + 300 [two mode-1] — both hand-checked.)
