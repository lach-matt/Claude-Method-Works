# RESULT S101 ROUTE (a) -- INTERIM. PA1 SCORED AGAINST PREDICTION 75d8212e: FALSIFIED AS WRITTEN (0/13).
## SEVERITY LINE: one prediction fault (F101.6), one instrument fault (F101.5, two iterations, caught by
##   own scoring both times). MAJOR VERIFIED RESULT beneath the falsification: the defect's exact identity
##   chain is established at machine precision. No sealed number touched.
## VERIFIED (pack101/i101.py, receipt i101-58.json):
##   IDENTITY 1 (exact, 1e-12 per shell): dI_c/dq = deps_c/dq - d<P_cU_cP_c>/dq + d<P_cX_c>/dq, 13/13.
##   IDENTITY 2 (exact to all printed digits): N1 + N2 = R2 = +1.0588e-4, where
##     N1 = sum_c q_c dI_c/dq = +7.2439  (eigenvalue + one-electron response)
##     N2 = d(half two-electron part at occ5)/dq = -7.2438  (double-counting response)
##   The sealed +8.0e-5-band defect IS the cancellation residue of two 7.24-Ha response sums -- the
##   standard HF energy-derivative structure dE/dq = sum q deps/dq - d(double-counting)/dq, exact.
## F101.5 SEVERITY instrument (two iterations, both caught in-run by scoring): analytic kernel model of
##   the response pieces incomplete -- v1 omitted the cross-I (screening) block (sum -7.1); v2 (collapse
##   law, part_m = q_m[deps_m - 2<dP'(U-X)P> - SLOTW + XSLOTW]) still off by -1.6e-3 in total. The
##   transcription gap sits in the analytic kernel derivatives of du/dx (numeric du/dx verified; analytic
##   reconstruction unmatched). Localisation instrument exists (i101 piecewise pattern); next split: per
##   shell, analytic-vs-numeric du and dx separately.
## F101.6 SEVERITY prediction: PA1 (13/13 per-shell match) FALSIFIED as written. PA2 not run (conditional).
## STATE OF G5b AFTER S101: OPEN, but transformed:
##   - EXISTENCE + FORM: attributed (Pulay 1969 term of the q-parameter; NOTE-S101-Q6-ANSWERED-PULAY).
##   - EXACT DECOMPOSITION: verified at machine precision (identities 1-2 above).
##   - VALUE: derivation incomplete -- the analytic kernel reduction of N1/N2 has a located 1.6e-3 gap.
## CARRY TO S102: (i) close the analytic gap (piecewise du/dx isolation, then the collapse law re-derived
##   against the verified pieces); (ii) rows 90/91 same instruments (sign flip + d-selectivity); (iii) G4
##   per-row table (Item 3, receipts exist); (iv) refined scope + Rule A; T4 last, zero residue only.