# RESULT-S104-ITEM3 -- perp_k exact decomposition, row 58, four shells. Prediction 50e3fc0d.
# Instrument pack104/w104d.py; receipt w104d-58.json. Scored vs sealed w104-58.json.

## SCORE:
PP.1 HIT 4/4 (rot + perp = chord <= 1e-12; perp reproduces sealed EXACTLY, d_seal = 0 all four).
PP.2 HIT 4/4 (decomposition total - perp: worst 1.9e-11 <= 2e-11; the R7 floor statement held).
PP.3 MISS 3/4. Remainder below 10% at 5s (-0.0%), 5p (-2.8%), 5d (+8.8%); at 6s the quartic
     tail is -47.5% of perp -- with T2p = +1.93e-5 and T34p = -1.31e-5 in near-cancellation
     (net nonlinear content +22% of perp). Prediction miss, scored as filed.
PP.4 MISS 3/4. First-order dominance holds at 5s (1.000), 5p (0.986), 5d (1.044); 6s at 0.776
     sits under the 0.8 bar (sign correct 4/4). The diffuse outer 6s carries genuine derived
     curvature in its perpendicular relaxation -- every term an exact quartic coefficient of
     the sealed functional, so this is DERIVED content, not residue.
PP.5 HIT (= PP.1 AND PP.2 as filed): the commensurate-gauge closure holds --
     chord = rot(derived, TRACE-S104-R1) + perp(exactly decomposed).
CAN-FAIL run (armed by primary HIT): c1m skew 1e-6 at 6s -> d_total 2.5e-6 >> 2e-11,
     rc=4 BREAK OK. Non-vacuous.

## F101.5 -- DISCHARGED-AS-DERIVED (per PP.5 and SWEEP-S104-CARRIED-FAULTS). The -1.6e-3
## located gap was the incommensurate-gauge artifact S102 named; in the commensurate gauge the
## chord decomposes exactly with every term a stated closed-form object. Ledger status updated.

## ITEM 3 CLOSED. perp_k = first-order perturbed-HF response content (Gerratt-Mills line),
## dominant at 3/4 shells, with exact derived quadratic/cubic content at 6s. The perp question
## needs no further object.
