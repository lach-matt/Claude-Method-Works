# The 61-species intake — register 1638

**Capture only.** M's instruction: retrieve all sixty-one, do nothing with
them, verify, and only then incorporate.

So each response is written here VERBATIM as it arrives, with its
`destination_url` recorded beside it, and NOTHING is extracted — no limits
read, no defects computed, no cells entered — until the last one is in.

**Why the discipline is worth the wait.** Register 1627 read seventeen species
and found four wrong limits and an energy column misread as an uncertainty.
Those were caught because the seventeen were read TOGETHER and their faults
showed as a pattern. Reading one at a time and acting on each would have
buried them.

## The rules, per file

- the `destination_url` is checked against what was sent BEFORE anything is
  written, and if they differ nothing is written (R 1595, R 1629)
- the response is stored as received; no reformatting, no column renaming
- the limit is NOT read yet, the terms are NOT parsed yet
- a file that arrives as an error page is recorded AS an error page

## Progress

`captures/FETCH-QUEUE.tsv` carries the TODO column. 0 of 61 in.

## M's note, held for the reading pass — register 1639

> **"Multiplicity is definable per problem, but has a calculatable mean
> for all problems."**

Recorded verbatim and NOT acted on. It bears directly on register 1626,
which found that stepping along 2S+1 changes the NUMBER OF BODIES in the
problem — so the axis moves BETWEEN problems while Z, charge and ℓ move
WITHIN one. That entry closed with the remedy failing: recoding as a
valence count bought 0.06 of lift, because a coarsening is a relabel and
relabels add no information.

**M's note points at a third possibility that register 1626 did not test.**
If multiplicity is definable per problem, then within a problem it is a
proper coordinate and R 1626's failure is a failure of POOLING, not of
the axis. And if it has a calculable mean across problems, that mean is
an object in its own right — one number per problem rather than a shared
axis, which is a KEY in register 1599's sense and not a coordinate.

**What Ti II supplies as evidence, captured today:** its terms carry
LETTER PREFIXES — `a 4F` at 0.0 and `b 4F` at 907.97 are both quartet-F
and are different channels. NIST already distinguishes what the index
cannot. That is the per-problem definability, printed in the source.

**The test this implies, statable now and runnable after the fetch:**
compute the within-problem multiplicity distribution for each species
separately, then its mean across species. If the per-species distributions
are tight and the cross-species mean is stable, M's reading holds and
R 1626's null result was pooling. If the per-species distributions are as
broad as the pooled one, it does not.

DO NOT RUN IT YET. Fourteen species are in and forty-six are not; a mean
across fourteen would be exactly the partial-pool error the note warns of.

## M's second note, held for the reading pass — register 1639

> **"Identify and index electron behaviour specific to each electron shell."**

Recorded verbatim and NOT acted on.

**Why it is not a restatement of what the index already does.** Λ_spectra's
coordinates are (Z, charge, ℓ, 2S+1). ℓ is the SUBSHELL LETTER — s, p, d, f —
and it is shared across every shell: the s in 2s and the s in 7s are one
coordinate value. **The index has no shell coordinate at all.** n appears only
inside a channel, as the running index of its members, never as a place a cell
sits.

So the note asks for something the index cannot currently express: does an
electron in the n = 3 shell behave in a way an electron in n = 5 does not,
INDEPENDENTLY of which subshell it is in?

**The captures already hold the material to test it.** Sixteen species with
series running n = 3 to n = 38, and three isoelectronic sequences where the
same subshell occurs at different n:

    Al-like    K VII, Ca VIII, Sc IX, Ti X     3s2.nl, n = 3..7
    Ar-like    K II, Ca III, Sc IV, Ti V       3p5.nl, n = 3..11
    Ti-like    V IV                            3d.nl,  n = 3..6
    Sc I                                       4s2.nf, n = 4..23
    Sc I                                       3d.4s.np, n = 9..38

**What makes it a real question rather than a relabelling.** If shell
behaviour is nothing but n's appearance in the defect formula, the note
dissolves — δ is already defined against n. It survives only if something
about the SHELL, not the principal quantum number, is measurable: a property
shared by 3s, 3p and 3d that 4s, 4p and 4d do not share.

**The obvious candidate, stated so the test can fail:** the defect's
DEPENDENCE ON n within a channel. If shells behave alike, dδ/dn is a function
of ℓ alone. If shells behave differently, dδ/dn depends on which shell the
channel's lowest member sits in. Register 1607's penetration regime is the
nearest thing already measured, and it is defined by ℓ against the CORE's
outermost ℓ — which is a shell property in disguise.

DO NOT RUN IT YET. Same reason as the first note: sixteen of sixty.
