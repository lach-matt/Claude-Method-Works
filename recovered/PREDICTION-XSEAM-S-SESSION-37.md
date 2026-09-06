# PREDICTION-XSEAM-S (s37, item b) — BEFORE the run. Frozen-orbital removal exchange, LSD+PZ-SIC minus HF (average of configuration), on the chain's spin-averaged
HFS neutral orbitals (xseam.py convention, s34): the s MEMBER of the pair (one electron of ns^2, spin-averaged removal, own-shell exchange 0) on the 13 d/s rows,
and the singly-occupied d member on Ce(5d) Ac Pa U Cm (own shell k=1). Hf Th Rf d members (k=2) NOT run (intra-shell average-of-configuration term not built; stated).
xseam_s.py -> xseam_s.jsonl. Nothing entered; no constant.
PXS-1  Delta_x(s) has the entrant's sign (LSD+SIC deeper) on every row; size 0.02-0.05 (Sc largest, ~0.05: the pair offset is 0 at Sc so s and d carry it equally).
PXS-2  Delta_x(d) - Delta_x(s) on Y La Gd Lu Ce Ac Pa U Cm = the frozen image of the relaxed pair offset (SR-local minus HF+corr, +0.020 +- 0.007): sign positive on
       all, size 0.01-0.04 (frozen overshoots the relaxed seam by <= 2x, as XSEAM found on the entrant); at Sc |d - s| <= 0.008.
PXS-3  Delta_x(s) is class-flat: sd <= 0.010 across the 12 n>=4 rows (it is not the row-differential term either).