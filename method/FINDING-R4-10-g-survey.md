# FINDING R4-10 — the spectroscopic survey exists, it covers the ions, and it settles the factual half of R4-09. My "no observation distinguishes them" was wrong. NOT REPAIRED.

M, 6 September 2026, on finding R4-09: *"you stated that no neutral atom contains a g subshell, but
what about non neutrals? … I am supposed to have the entire spectroscopic data for all 120 and their
ions. there was weeks spent on that before and during the Löwdin works."*

**The data is here, and it settles the question R4-09 put to M as a ruling.**
`method/proofs/gchannel.py` measures it; the selftest asserts eighteen of the survey's own figures
and the law's arithmetic.

## The survey

**`extracted/archives/method16-rp-b-data/COORDINATES.tsv`** — and it is exactly what M described.

| | |
|---|---|
| rows | **104,832** |
| atomic number | **Z = 1 to 120** |
| core charge | **1 to 120** |
| angular momentum | **ℓ = 0 to 7** — s, p, d, f, **g, h, i** and beyond |
| per row | quantum defect, grade, source, bound, witness flag |
| measured and witnessed | **358** |
| exact | 929 |

The same object is held three more ways in the same directory — `survey.json`, `channels_map.json`,
`index_final.json` — and **none of the four is a seated member.** The seated tree holds only
per-species tables (`BiIII_asd.tsv`, `CdII_full.tsv`, `HgII_full.tsv`, `ScIII_asd.tsv`). That is
recorded because a book cannot cite what is not seated, and this survey is the evidence for a
chapter's central claim.

## Thirty-six measured g channels, and thirty-two of them are ions

| | |
|---|---|
| measured g channels (ℓ = 4) | **36** |
| **in ions** | **32** |
| in neutrals | 4 — He I, Na I, Al I, Cs I |
| \|δ\| range | **0.00000 to 0.04010** |
| exceeding 0.001 | **24 of 36** |
| measured h channels (ℓ = 5) | **1** — Na I, δ = 0.00013 |
| species whose level tables carry a g term | **34 of 61** in the levels store |

The ions run from Li II to Bi III and up to core charge 6 (S VI), sourced as *captured levels* and,
for four of them, as NIST ASD fetched 2026-08-14.

**So my statement in R4-09 — that no observation distinguishes the two candidate sets — was wrong,
and M caught it.** The observation exists, it was built deliberately, and it covers exactly the
charge states the neutral table cannot reach.

## And the levels store behind it, which carries the depth of each channel

The flat survey gives a defect per channel. **`extracted/archives/spectra-levels-store/deliver/`
gives the levels it was read from**, and with them the member count and the n range that the survey
drops.

| | |
|---|---|
| species level tables | **61**, neutrals and ions to core charge 10 (Co IX, Ni X) |
| level lines | **9,200** |
| species carrying a g term in their levels | **34 of 61** |
| channels in `MEASUREMENTS.tsv` | 554, of which **12 are g** and **one is h** |

And the g channels are not thin:

| species | term | members | n range | δ |
|---|---|---|---|---|
| **Ba I** | 3G | **29** | **8–25** | **0.05145** |
| Cs I | 2G | 28 | 5–25 | 0.00667 |
| Ba I | 1G | 18 | 8–25 | 0.05072 |
| Na I | 2G | 18 | 5–20 | 0.00042 |
| Hg I | 3G | 9 | 5–11 | 0.00379 |
| Sr I | 2[5/2] | 6 | 5–10 | 0.03533 |

**A twenty-nine-member series running from n = 8 to n = 25 with a defect of 0.05 is not a channel
sitting at hydrogenic depth.** Four of the twelve carry ten or more members.

## And it tests Chapter 35's criterion, which is the ground R4-09 rested on

**§35 (main L9794):** *"Every g channel the walk ever offers … sits at its hydrogenic depth
−1/(2n²) to the storage precision, across a hundred protons … **A channel that does not respond to
the nucleus is not in the field.**"*

**A quantum defect of zero is hydrogenic depth.** Measured over the survey:

| ℓ | measured | median \|δ\| |
|---|---|---|
| s | 92 | 1.03980 |
| p | 81 | 0.69910 |
| d | 89 | 0.11090 |
| f | 59 | 0.02480 |
| **g** | **36** | **0.00505** |
| h | 1 | 0.00013 |

**The ℓ-collapse is exact and monotone across six orders of magnitude**, which is the corpus's own
law `P.lcollapse` reproduced from the survey. **And the g defects are small but not zero**: they run
to 0.04010, twenty-four of thirty-six exceed 0.001, and **r(Z, |δ|) = +0.330** over the thirty-six.
They rise with the nucleus, which is the corpus's own high-ℓ mechanism — the defect following core
polarisability beyond ℓ = 3, `P.polar`.

**So the observed g channels do respond to the nucleus.** §35's measurement was made in the derived
Hartree-Fock field; the survey is the observation, and at the level of 10⁻² in δ the two disagree.
**Neither ground for excluding g survives the data**: not "there is no g data", and not "g does not
respond".

## What admitting g actually costs the law, which turns out to be nothing

Measured over the 106 steps, with the two candidate sets differing only in whether ℓ = 4 is offered:

| | |
|---|---|
| g candidates offered | 80 step-pairs |
| of those, **binding** | **16** |
| giving exactly **a > 0** | **11** — the parameter's own domain, no information |
| giving a real bound | **5** — Rf 104 to Hs 108, each **a > 1/√3** |
| corridors non-empty, ℓ ≤ 3 | **106 of 106** |
| corridors non-empty, ℓ ≤ 4 | **106 of 106** |
| a g subshell ever wins a step | **never** |

**Admitting g never changes which subshell the law selects and never empties a corridor.** It moves
the floor at sixteen steps, and at eleven of those it moves it only to *a > 0*, which is the
positivity of the parameter and not a constraint from a rival. **That is why register 1403 calls
protactinium's floor "degenerate at zero" — it is degenerate.**

The five that are not degenerate are the superheavy 6d steps, where 5g requires **a > 1/√3**. The
walk's own value there is 1.9841, so the bound is satisfied and never binds on the trajectory.

## What is left for M, and it is narrower than R4-09 made it

**Not** *"does g exist"* — it does, in thirty-six measured channels, thirty-two of them ions.
**Not** *"does g respond to the nucleus"* — measured, it does.

**The question is whether the law may consider a channel that exists, is measured, and is never a
ground entrant.** The law's own admissibility test *q < 2(2ℓ+1)* admits it and says nothing about ℓ.
The ground data never exercises it, because no element below Z = 121 has a g electron in its ground
configuration. And the cost of admitting it is one moved floor at sixteen steps.

**Two printed statements still turn on the answer**, exactly as R4-09 set out: register 1414's
*"106 of 106"* iff, and §34.9's conclusion at 5f. **What has changed is that the choice is now
between two defensible readings rather than between a convention and an absence of evidence.**

## What is owed beyond the ruling

**The survey and its levels store should be seated.** Together they are the evidence for Chapter
34's corridor and Chapter 35's g-channel claim: 104,832 survey rows over Z = 1 to 120 and every
charge state, and 9,200 level lines over 61 species with their sources named. **Both are held only
in generated trees** — `extracted/archives/method16-rp-b-data/` and
`extracted/archives/spectra-levels-store/` — and neither is a seated member. The seated tree holds
four per-species tables. Under Ruling 46 a reader cannot be pointed at any of it as it stands.

**And §35's g-channel claim is owed a re-test against it.** *"Sits at its hydrogenic depth to the
storage precision"* is a statement about the derived field; the survey measures defects up to 0.04
that rise with Z. Both can be true of different objects, but the chapter states the derived result
as though it settled the observed one.

**Nothing is repaired here.**
