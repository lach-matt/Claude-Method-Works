# F35.1 (s35, TIMING FLAG, R 1449) — (b1) as designed in PREDICTION-B2 (exchange-only relaxation of the E-path removal) is refused on SIZE, and the
design is changed AFTER seeing the result. First run (xseam_relax.py, Sc/Cs): frozen Dx reproduces xseam exactly (Sc -0.34397, Cs -0.03334, gate);
b1 = Dx_rel - Dx_frz = Sc +0.122 (12x the row target -0.010), Cs -0.021 (sign against PB2-2). Reading: the exchange piece alone relaxes by ~0.1 Ha and is
cancelled by kinetic+Hartree relaxation (virial); the seam remainder is the TOTAL relaxation difference between the paths, relax_E - relax_O, not the
exchange piece of one path. Redesign (post-result, flagged): E-path total energy on the SAME t5 orbitals under the E functional (T + V_ne + H + LSD-x + SIC + S),
neutral / frozen ion / relaxed ion -> relax_E := D_rel - D_frz; O path relax_O := D_HF - (-eps_koop) from hfdscf.jsonl (record). PB2-1..4 stand as
written and are scored against b1 as first defined (PB2-1 sign HELD size FAILED; PB2-2 FAILED). New, post-result (weight reduced): PB2-5 relax_E - relax_O
has the SIGN of the row target (negative on d rows, positive Cs) and lands within x0.5-2 of it on >=4 of 6 rows.