# PREDICTION S102 ITEM 1 -- PIECEWISE du/dx ISOLATION (row 58). Filed BEFORE any arithmetic. Zeno.
# RULE B: instrument VALUE-exact throughout. Object: the F101.5 located gap (-1.6e-3, a101 v2 total vs R2).
# METHOD: symmetrized exact split of every endpoint difference f(P,U) = <P U P> (and <P X>):
#   du_wf  = (1/2)[f(P+,U+)-f(P-,U+) + f(P+,U-)-f(P-,U-)]/0.2   (wavefunction response)
#   du_pot = (1/2)[f(P-,U+)-f(P-,U-) + f(P+,U+)-f(P+,U-)]/0.2   (potential/occupation response)
#   These telescope: du_wf + du_pot = du_num ALGEBRAICALLY EXACT (same for dx). No truncation.
#
# P1 (identity; inequality |du_wf + du_pot - du_num| <= 1e-12 per shell, 13/13; same for dx):
#   the symmetrized split closes each numeric derivative at machine precision. Direction: residual -> 0.
#   VALUE-exact. CAN-FAIL: perturb one split term by 1e-8 -> identity must break above 1e-9 (rc=4 if not).
#
# P2 (localization; inequality sum_valence |gap-cell| >= 0.80 * |total gap|):
#   the -1.6e-3 a101 gap localizes in the POTENTIAL-RESPONSE column -- i.e. per shell,
#   gap_c = q_c[(model slotw/xslotw) - (exact du_pot/dx_pot combination)] carries >= 80% of the total
#   gap magnitude, concentrated in the valence block {5s,5p,5d,6s} (the |N1|>=0.5 shells);
#   the wf column (2<dP'(U-X)P> vs exact du_wf/dx_wf) contributes <= 20%. Direction: localized, pot-side.
#   VALUE-exact.
#
# P3 (rescore; inequality |law_total - R2| <= 5e-6 and 13/13 shells within a101 tolerance):
#   the collapse law re-derived with the exact isolated pot-piece substituted per shell
#   (part_c = q_c[deps_c - du_wf_c - du_pot_c + dx_wf_c + dx_pot_c]) reproduces R2_parts 13/13 and
#   the total to <= 5e-6 of R2 = +1.0588e-4. Direction: gap -> 0 when the located piece is exact.
#   VALUE-exact. (This closes the DECOMPOSITION frame; the remaining analytic object is then the
#   pot-piece alone, named per shell with its exact value as the S102 derivation target.)
#
# SCORING: against pack101/d101-58.json R2_parts + R2_chain and pack101/a101-58.json parts. No sealed
# file touched. Faults, if any, registered per object with severity lines.
