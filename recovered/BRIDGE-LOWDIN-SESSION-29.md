# BRIDGE — THE LÖWDIN SESSION 29 (2026-08-17)
Successor to BRIDGE-LOWDIN-SESSION-28.md. Bank restore-point-2_13 (R 1700) UNCHANGED; nothing written to register/index/store.
Archive verified at open: HANDOFF-28 576/576. Gates 1-35 PASSED at open (pack29/GATES-1-35-SESSION-29-OPEN.log). §H.10: handoff at ~85 %.
## 1 · Rulings (M, s29)
(1) SUBCELL=1 ADOPTED as standing convention (SUBCELL unset only to reproduce pre-s28 rows). (2) The one-function correlation term was ruled in s28
("combine both into ONE mathematical function", option (i)); s29 re-asked it in error — carried, not re-ruled, on record. (3) "on the 5d/6s rows it is not,
and the remainder is the open object — pursue it; the 0.002 (Sc) means we are on the right path." (4) On the d-row excess: "do BOTH and let the comparison
decide" -> SPEC-DROW-EXCESS-SESSION-30.md. GENERAL carried: predictions before runs; R 1449 timing flags; comparison decides; no scans; T4 writing chat LAST.
## 2 · Findings (no constant beyond c; no measured input beyond banked meas/so columns; Cs/Y RECALLED-NOT-ENTERED) — files in pack29
(1) (a') TABLE ON THE ONE FUNCTION, all six class rows (FINDING-FRACHF-CLASS, TABLE): I(Cs Sc Y La Gd Lu) = 0.1301 0.2924 0.2154 0.2237 0.2082 0.1788.
    Janak <= 6e-4 except Sc (1.2e-3: Simpson on a twice-steeper eps(f) with extrapolated eps(0) — quadrature, not Janak). gap_sc <= 0.001 all rows.
    Remainder with SO/Hund column: Cs -0.0130 Y -0.0131 La -0.0103 Lu -0.0123 Gd -0.0262 Sc -0.0022. Failed: PA1/PA3 Sc, PA4 Lu (calibration).
(2) MECHANISM B (FINDING-CUTFRAC): eps_c>=0 cut fraction F_out Cs 0.87 · Y 0.08 · La 0.10 · Lu 0.11 · Sc 0.02. Cs: missing/req 0.84 <= 0.87 — B is
    the whole of Cs. d rows: missing/req 0.35-0.39 vs F_out ~0.1 — correlation missing INSIDE the domain: excess ~0.009 Y La Lu, ~0.001 Sc. PB4 d-rows FAILED (by design).
(3) MECHANISM A adiabatic build (FINDING-COREPOL; corepol.py Sternheimer, cutoff-free): H gate 4.5001; He HFS 2.50 (uncoupled-Xalpha inflation ~1.8x,
    stated). Cs E_A ~0.016 corrected — one object with B, twice named. d rows 20-200x too large, largest on Sc: adiabatic form inadmissible for an entrant
    inside the responding shell. PC2 FAILED decisively; adiabatic route closed by prediction. Non-adiabatic second order is the admissible test (Route N).
STANDING: not a closure. Cs settled (cut region == core-valence region). d-row excess ~0.009 open: Route P (object property) vs Route N (physics), s30.
Failed predictions s29: PA1 PA3 (Sc), PA4 (Lu), PB4 (d rows, discriminating), PC0 (He), PC1 (Cs window), PC2 (d rows), PC4. Timing flags: none;
build errors caught by gate before reading: cutfrac so-sign; corepol r^{-1/2}; corepol outer-s2 (3s vs 4s on Sc) — all on record in the FINDINGs.
Overrun: frachf batch La+Lu exceeded the tool budget after La wrote; Lu rerun alone (Zeno as designed).
## 3 · Next chat, in order (rulings first; predictions before runs)
(1) SPEC-DROW-EXCESS-SESSION-30: gates 1-40; PREDICTION-DROW; Route P; Route N build; COMPARE-DROW decides. (2) Sc quadrature: compute eps(0) slope
(f=1e-3 run) instead of extrapolating — small, bounded, prediction first; needed before Sc's Janak row is clean. (3) 4f +0.09 as ONE object via Yb (needs the
second radial function for q_c>=1; prediction first). (4) Term-resolved SCF Fe/Ni conditional. (5) T4 writing chat LAST: R 1701-1872 + s29: R 1873 (a')
one-function table + Sc 0.002 · R 1874 mechanism B / Cs settled · R 1875 adiabatic A closed, d-row excess stated · R 1876 failed predictions s29.
## 4 · Figures (§H.6): MEASURED none entered. RECALLED-NOT-ENTERED Cs 0.14310, Y 0.2285 (banked meas/so columns used for the residual, as chain).
CHOSEN: prediction thresholds; r_e ladder every 40th mesh point (corepol); Simpson eps(0) extrapolation inherited (stated). DERIVED: r_cut, F_out, F_self,
E2(r_e), alpha. No new constants. Reading only: uncoupled-HFS inflation factor ~1.8 (He gate) — a reading, enters nothing.
## 5 · Files (pack29): PREDICTION/FINDING-FRACHF-CLASS + TABLE · frachf.jsonl (six rows) · PREDICTION/FINDING-CUTFRAC · cutfrac.py/.jsonl ·
PREDICTION/FINDING-COREPOL · corepol.py/.jsonl · SPEC-DROW-EXCESS-SESSION-30 · GATES-1-35 log · this bridge · README-29.
## 6 · Unread / owed: unchanged (R 1668; Dabo 2010, Borghi 2014 beyond abstract). Owed: T4 (R 1701-1876); Kitagawara&Barut/Schwarz corrections.
Container clean at close: rt/ holds nothing outside the packs except __pycache__, .so, out/ (pack5), /tmp backups (discarded).