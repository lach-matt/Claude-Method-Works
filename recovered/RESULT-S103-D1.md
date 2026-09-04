# RESULT-S103-D1 -- F103.1 mechanism LOCATED. Criteria e4cb83c0 filed pre-run; receipt d1-s103.json.
## Fork scoring (honest): NEITHER branch as written. S(eps) varies 2x over eps (rules out (ii),
## first-order-constant), but S(1)/S(1e-3) = 0.49 at 6s, 0.64 at 5s -- below (i)'s >2 threshold.
## Criteria were too coarse; filed as such, no reinterpretation.
## LOCATED (per-partner gradient probe, 6s): true <Pn|grad F> vs law's 2q<Pn|F_k|Pm>:
##   self 1.00, 5s 0.98 (LAW HOLDS on valence-partner + normalization channels);
##   4s 1.9x, 3s 27x, 2s 165x, 1s 1207x -- ratio grows with core depth.
## MECHANISM: the w102b F() one-body part I[k] = cMc uses the SYMMETRIZED M; its transpose halves
## <Pm|T|P_core> carry core-eps-scale x overlap content (F102.3 species). d(cMc) along a core
## partner = 2M_{n,m}, dominated by that content. Magnitude CLOSES: sum s_n x true-gradient /dq2
## = 2.84e-4 vs S(eps->0) = 3.18e-4 at 6s (rest = normalization channel, <Dr|Pm> x self-gradient).
## 1s channel alone = 38% of rot(6s). CONSEQUENCE for G5b: s-channel rot dominance is part
## instrument content (symmetrized-M core channel), part physics (valence channel, law-obeying).
## REPAIR PATH (S104): restate rot in a core-projected basis (valence partners only) OR
## de-symmetrized M with F102.3-repaired T-action; the valence-channel law then scores as filed.