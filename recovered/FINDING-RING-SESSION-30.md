# FINDING — candidate C (form R = full RPA ring + E0B in place of the truncated GB expansion) on the class rows.  s30.
# Files: PREDICTION-RING-SESSION-30.md (before any run), ring_table.py + ring_table.json (41 r_s x 11 zeta, ring_zeta integrand, nan-masked cancellation cell),
# corr_ring.py (eps_R, v_R; same interface as the chain's; small-r_s limit = chain form), frachf_ring.py + frachf_ring.jsonl (f=1/f=0 on the sc path).
# No constant chosen; numerics stated in the prediction file. Cs/Y RECALLED-NOT-ENTERED. Literature: Nozieres-Pines 1958 (GB valid r_s <~ 1); RPA overbinding.
## Table (Ha). delivered = -DEc/required; excess = (1 - delivered - F_out)*required; resid = meas + so + D_tot (chain sign: + = form still short).
row  DEc_Z     DEc_R     deliv_Z deliv_R  gain  | F_out_Z F_out_R | excess_Z excess_R | resid_R   (resid_Z s29)
Sc  -0.026011 -0.032164  0.930   1.150   +0.22  | 0.020   0.000   | +0.0014  -0.0042  | -0.0040   (-0.0022)
Y   -0.020192 -0.027778  0.614   0.845   +0.23  | 0.076   0.002   | +0.0102  +0.0051  | +0.0054   (-0.0131)
La  -0.018297 -0.026534  0.650   0.943   +0.29  | 0.096   0.002   | +0.0072  +0.0016  | +0.0019   (-0.0103)
Lu  -0.019484 -0.027346  0.622   0.873   +0.25  | 0.112   0.005   | +0.0083  +0.0038  | +0.0043   (-0.0123)
Cs  -0.002430 -0.006891  0.159   0.450   +0.29  | 0.869   0.312   | -0.0004  +0.0036  | +0.0086   (-0.0130)
## Predictions scored
PR0 small-r_s gate HELD (3e-5 Ha at r_s 1e-3). "No cut anywhere" FAILED at zeta ~ 1, r_s > ~9 (E0B, zeta-independent in the chain, exceeds the ring there):
    Cs still cut 31 %. The zeta-dependence of the second-order exchange constant is a DERIVABLE refinement, owed (Onsager constant at zeta=1), not entered.
PR1 HELD on La (0.943), Lu (0.873), Sc (1.150, the predicted overshoot); Y 0.845 misses the [0.85,1.05] window by 0.005; Cs 0.45 FAILED ([0.6,0.9]) — the
    zeta~1 cut above. PR2 HELD on La Lu (0.0016, 0.0038), FAILED on Y (0.0051): the excess is HALVED-to-quartered, not removed.
PR3 not run (pieces A/B/R under form R) — owed. 
PR4 FAILED, and it is the finding: the gain is UNIFORM, +0.22 (Sc) to +0.29 (Cs La), Sc/Y = 0.95 (predicted < 0.6). The truncation under-delivers every row by
    the same fraction; it does not carry the 3d / nd>=4 contrast. Under R the contrast is still there, now as Sc OVER by 15 % against Y La Lu 6-15 % UNDER
    (ratio Sc/<Y La Lu> 1.50 -> 1.30). Two forms bracketing the exact UEG from opposite sides both show it. An exact local form (RPA overbinds ~15 % at
    r_s 1-3, nearly flat) would put Sc at ~1.0 and Y La Lu at ~0.75-0.82: the class object is NOT a property of the local form's r_s accuracy.
## Statement
(1) The truncation of the high-density expansion is a real object of the chain: it costs 22-29 % of the delivered correlation on every class row, and its
    r_s -> large failure is Cs's cut (mechanism B) — B and the truncation are one object; form R halves the d-row excess and lifts Cs from 0.16 to 0.45.
(2) It is NOT the d-row discriminator (PR4). The nd>=4-vs-3d contrast survives the change of local form intact: a non-local property of the nd>=4 rows,
    the object COMPARE-DROW named, now with one more candidate refused and its size sharpened: ~0.004 (Y Lu), ~0.002 (La) under R; ~0.005-0.008 against an
    exact local form. Sc's overshoot under R is the ring's own overbinding (known, ~0.035 Ry flat) — a form property, statable with attribution (GB 1957 ring;
    Onsager-Mittag-Stephen 1966 SOX; BRM 2024 integrand; Nozieres-Pines 1958 validity).
(3) Not a ruling: whether form R (derived, valid at all r_s, overbinding known) or form Z (derived, valid r_s <~ 1) is the chain's correlation is M's; the
    comparison says R is the more honest UEG object and Z the one that happened to be right on Sc by cancellation (truncation under x RPA over ~ CA at r_s ~1.5).
Failed predictions: PR0(no-cut half), PR1 (Y by 0.005, Cs), PR2 (Y), PR4. Timing flags: none (all predictions before the first run).
Gates for HANDOFF-30: python3 corr_ring.py -> "rs 0.001 z 0.0: R -0.26164  Z -0.26161"; python3 frachf_ring.py 39 21 57 71 55 -> must SKIP all; if Y deleted
reprints DEc_R -0.027778 delivered_R 0.845 (27 s); python3 ring_table.py -> SKIP all 11 zeta.