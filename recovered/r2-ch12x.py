# r2-ch12x.py — Phase R2, main §12.11.1.6–.7 (L3318–3362), chat 77.
# The population — 4,325 cells (Z, n, ℓ, k, q, e, f, g) built from the 118 real configurations of the 18,288-test pass
# (L4195, Register 529) — is used by the book but printed in no member, so the counts are record-carried; what is
# measurable is every ratio, sum, difference and cross-site restatement: L3324–3326, L3343–3348, L3350–3352,
# L3360–3361 against Registers 628–629 (R L2347–2353), MC L2574 and the section's own text. Deterministic; no tower.
R = [('all', 4325, 982, 0.227, 3686, 0.852), ('EM-allowed', 2673, 309, 0.116, 2399, 0.897), ('EM-forbidden', 1652, 673, 0.407, 1287, 0.779), ('parity-conserving', 606, 233, 0.384, 544, 0.898), ('parity-changing', 3719, 749, 0.201, 3142, 0.845)]
print('== L3343–3348 population | cells | within | rate | across | rate — every ratio to the printed precision:')
for name, n, w, rw, a, ra in R:
    print(f'   {name:<17} {n:>5,} {w:>5,} {w/n:.3f} (printed {rw}: {"OK" if round(w/n,3)==rw else "MISMATCH"}) {a:>5,} {a/n:.3f} (printed {ra}: {"OK" if round(a/n,3)==ra else "MISMATCH"})')
S = {name: (n, w, a) for name, n, w, a in [(x[0], x[1], x[2], x[4]) for x in R]}
print(f'== partitions: EM 2,673 + 1,652 = {2673+1652:,} | within 309 + 673 = {309+673} | across 2,399 + 1,287 = {2399+1287:,} | parity 606 + 3,719 = {606+3719:,} | within 233 + 749 = {233+749} | across 544 + 3,142 = {544+3142:,} — all equal the all-row {all(x==y for x,y in [(2673+1652,4325),(309+673,982),(2399+1287,3686),(606+3719,4325),(233+749,982),(544+3142,3686)])}')
print(f'== L3324–3326: 982 / 4,325 = {100*982/4325:.2f}% (printed 22.71) | 3,686 / 4,325 = {100*3686/4325:.2f}% (printed 85.23) | gained 3,686 − 982 = {3686-982:,} (printed +2,704) | {100*3686/4325-100*982/4325:.1f} points (printed +62.5)')
print(f'== L3350–3352 / L3360–3361 the percent forms: 0.116→11.6, 0.407→40.7, 0.897→89.7, 0.779→77.9, 0.384→38.4, 0.201→20.1 — all consistent with the table above | L3329 "six-sevenths" = {100*6/7:.1f}% against 85.23%')
print('== restating sites (record match, texts read): Register 628 (982 of 4,325 — 22.71%; 3,686 — 85.23%; E 972,862 with Z against 28,503 without) and Register 629 (11.6% against 40.7%; 89.7% against 77.9%; 38.4% conserving against 20.1% changing) restate the section; MC L2574 restates 11.6 / 40.7 / 89.7 / 77.9. E = 972,862 and 28,503 are record-carried (the cells are not in any member).')
print(f'   the 77.9% here (1,287 / 1,652 = {100*1287/1652:.1f}) is the EM-forbidden across rate — a different quantity from §12.11.1.1\'s 77.9% axis-11 density (10,585 / 13,585 = {100*10585/13585:.1f}); same numeral, distinct objects')
