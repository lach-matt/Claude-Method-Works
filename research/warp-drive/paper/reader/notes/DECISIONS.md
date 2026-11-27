# Author's decisions (coordinator's record; not part of the paper)

## 2026-11-20: printing the certified approximant

The certified approximant of the continuation theorem (chapter 87) is printed in the paper in full, so that a reader
without any other material can check it. Placement, as the scoping report notes/reports/S-APP.md recommends (§0, item 4),
chosen by the author:

- a new Appendix C after Appendix B, about 10-15 pages: the definition of the printed approximant (element map,
  partition of unity, seed form), the format and its checks, the certification procedure as mathematics, and the
  certified outcomes;
- the coefficient tables in a separate final part after the references ("Tables of the approximant"), paginated on,
  which can be bound as a second volume.

Order, from the same recommendation: D_A first (one seed, about 400-450 pages, double-double); then D* at seed 2
(about 1,160 pages), whose table supersedes seed 2's D_A table (if seed 2's D* closing is firm before printing starts,
only the D* table is printed); seed 1's D* is not printed until its closing is GO. Every page figure is extrapolated
from measured decay rates and could be about 3.3x larger if the decay is 30 % slower.

Update the same day, by the author: print both seeds. Each seed is printed on the largest domain its closing certifies:
seed 1 on D_A (GO) and on D* once its closing is shown GO (then its D* table replaces its D_A table); seed 2 on D*
(GO; its table covers D_A). Estimated totals: about 1,600 pages (seed 1 D_A plus seed 2 D*), about 2,900 if seed 1's
D* is printed, each up to about 3.3x larger if the decay is 30 % slower than measured.

## 2026-11-20: improving the upper bound on d

The author asked for both improvements to be pursued, beside the proved bound (which does not wait for them):
- whether the offset d0 can be dropped from the index set (it would bring d_NM from about 10^56 to about 10^38 if a
  coefficient c_b vanishes at rotating b, or can be made to vanish by a free choice of the paper);
- moving the computational point h from 10^-6 to a better point (about 84x smaller at h = 9.6e-7, numerically), scoped
  first for cost and robustness.

## 2026-11-27: the level of the a priori estimate

The author: "We should also start level 4, if we haven't already. We need to keep level 6, but including the level 4
version expands on completeness of the paper." So the level-6 estimate (sec:tl5-hf, merged) stays as it is, and a
level-4 version is added beside it, not in its place, citing the level-independent results of sec:tl5-hf by label.
Level 3 is not possible for the double-null step (the C^2 distance needs |D^2 h| pointwise; level-3 face energies do
not give it), as rem:tl5-hf-level records.

## 2026-11-27: the offset d0 and the computational point

P-D0 dropped d0 in full by another route (recording relative to order 1), so h stays at 10^-6; the move to
gamma_C = 1,007,860 that S-HPT scoped is not needed. Merged with the chain re-evaluation (P-UB3: the chain's
inequality removed and its cap relaxed to eps_K < 0.998 eps_Upsilon, both by proof): d_NM < 1.42556e38,
K < 3.13622e39 at h = 10^-6 (merge a6a0974f).

## Earlier decisions in this segment

- Admissible points (P-ADM): the cap h <= 10^-6 is removed from the definition; the lower bounds on d state it as an
  added hypothesis (the minimal form).
- The data supplement is replaced by printing everything in the paper (the paper must stand alone).
