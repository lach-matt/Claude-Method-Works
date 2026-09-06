
---

# Appendix E — Margins, and what was recomputed

**A referee should treat two classes of claim differently**, and this appendix
separates them.

## E.1 Margins on the load-bearing conclusions

**How far is each result from the threshold that would overturn it?**

| conclusion | statistic | margin | breaks down at |
|---|---|---|---|
| the periodic table is not closed | **E = 36** | exact arithmetic | — |
| closure ⟺ 𝓡(X) = X | 200/200 agreements | exact | — |
| 𝒟 ≥ dim *q* − dim *p* | 420 random maps | exact — rank–nullity | — |
| ***V* > 2 for any monotone sequence** | Proposition 14.1 | **exact, proved** | — |
| Rydberg floor *V* ≥ 32/11 | 2.909091 at ν = 2 | exact | — |
| E3 admissibility criterion | 2,513/2,513, nine functions | exact | — |
| χ_Λ total | 30,000 ambient points | exact | — |
| order recovery on a tree | 20/20, two cap settings | — | a cyclic constraint graph |
| **the bracket holds** | **1,442/1,442** | — | **one reordering** |
| perturbation bounds | tightest **1.40 cm⁻¹** | deductive | a 1.4 cm⁻¹ shift at that cell |
| isoelectronic interpolation | 1.3% median | **13× better than at an end** | the sequence end |
| *V* = 4ν/3 on real channels | 0.06%–4.4% median | — | coarse quotation |
| void-free fraction stable | 27.7–30.1% | 2.4 points over a 100× range | — |
| filled-*d* core raises δ | +0.35 at low ℓ | — | ℓ ≥ 3, where cores converge |

**Three rows deserve a sceptic's attention first.**

**The bracket's 1,442/1,442 breaks on a single reordering.** §16.3 states the
condition exactly — |Δ*T*| > 2*Z*²*R*/ν³ — and §16.4 argues that the collection
never enters the regime where it can occur. **That argument, not the count, is
what a critic should attack.**

**The perturbation bounds are as strong as the failure condition and no
stronger.** If the condition is wrong, 1,061 bounds go with it.

**The isoelectronic interpolation is quoted at 1.3% and used at the end of a
sequence**, where the measured cost is 2.1% for a hold-out and **3.5% for a
genuine fifth member.** The Sc VI route of §16.6 uses the last figure, not the
first.

## E.2 What was computed in this revision

**Fourteen results rest on computations performed for this book**, each
reproducible from Appendix C's tables and the rules of Part III:

E(X) for seven indices, the periodic table among them · closure ⟺ 𝓡(X) = X on
200 constructions · 𝒟 ≥ dim *q* − dim *p* on 420 random nonlinear maps · the
E3 criterion on 2,513 tests · χ_Λ totality on 30,000 uniformly sampled ambient
points · order recovery by tree propagation, 20/20 · **the 1,105 cells added
here, across all 153 channels** · the failure condition and its inversion to
1,061 perturbation bounds · the isoelectronic hold-out and fifth-member tests ·
the C₆ cost-law check against Singer *et al.* · the antiprotonic-helium
two-route check at 0.09σ · the census by antisymmetric-state enumeration ·
Proposition 14.1 re-derived · **the three falsification tests of §21.5.**

## E.3 What was inherited and not recomputed

**Six results come from earlier work and were not re-run:**

the rule-ablation costs of §13.2 · the Sr I node coverages and fine-structure
figures of §16.2 · the Ti I channel inventory · the multi-target failure counts
of §10.4 · the Sc VI prediction's input defects · the earlier verification's
per-species medians.

**These rest on methods described in Appendix B but were performed before this
revision.** Chapter 18 records forty-eight errors found in work of exactly that
kind — **which is reason to re-run them rather than to trust them.**

> **The Sc VI defects are the most consequential of the six**, because the
> book's single prediction rests on them, and §16.6's arithmetic was
> independently reproduced here — 735,091 against 735,092 — while its *inputs*
> were not.

**One inconsistency was found in the inherited material and is recorded.** The
exclusion discussion of §16.2 states that Sc VI's "highest measured level is 5s
at 696,400 cm⁻¹". **That figure and the stated δ(5s) = 0.9812 cannot both
describe the ⁴S° channel**: from 696,400 the defect is 0.514, and the stated
defect requires 5s at 648,096. **The 696,400 is Sc VI's highest measured level
overall, not the ⁴S° 5s**, and the prose ran them together. The prediction is
unaffected, having been computed from the defects.

## E.4 Computational methods

All computations in Python 3 with NumPy. **Closure tests are either exhaustive
over all pairs — stated where so — or on uniform random samples with the sample
size reported.** Box searches enumerate all 2^*d* corners of candidate base
cells.

**Ritz fits** use ordinary least squares on δ against 1/*n*², with σ from the
standard prediction error including the leverage term
*s*·√(1 + 1/*k* + (*x*₀ − *x̄*)²/*S*ₓₓ).

**Quotation granularity *q*** is read from the source table as the smallest
nonzero increment appearing in it — 10⁻³ cm⁻¹ for most ASD entries, coarsening
to 0.1 or 1 cm⁻¹ in the high-*n* regions of several channels — and enters ν_V
directly.

**Weighted centroids** over fine-structure components use statistical weights
2*J* + 1.

**Where a channel's neighbours are not consecutive in *n*, the bracket is still
evaluated but *V* is not**, since *V* = 4*x*/(*h*|*p*−1|) assumes unit step.
That exclusion is applied silently in the totals and is the reason the *V*
counts are smaller than the cell counts in Appendix C.