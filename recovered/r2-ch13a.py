# r2-ch13a.py — Phase R2, main §12.11.3.1 "Where each bound comes from" (L3409–3456), chat 78.
# Measured: the thirteen printed bounds verified against the construction cell by cell on Λ₁₃ (L3413–3428); φ̂ observed
# {1:3, 2:4, 3:5} against the realised maxima — max 2J_c per k over Λ₁₁ (MC L1264's wording) AND max 2J per k over Λ₁₃
# (the main's L3439 wording, tested); 39,375 of Λ₁₂'s 70,905 cells at f below the cap (L3435–3436); the tight-K
# variant's cuts at Λ₁₂ and Λ₁₃ (2K ≤ 2J_c + 2f with the cell's own f) against L3434's withdrawn 2,475 (withdrawn at
# L3477; breakage figures 15,150 / 45,450 are §12.11.5's segment); the grading column (L2937–2942) against the
# provenance column (L3413–3426), tabulated; L3448's bracket rule against §22's own statement L6027 (census row 1073).
# tower-2.py by path via r2lib. Deterministic (no wall-clock).
import importlib.util, os, re
H = os.path.dirname(os.path.abspath(__file__))
s = importlib.util.spec_from_file_location('r2lib', os.path.join(H, 'r2lib.py')); r2lib = importlib.util.module_from_spec(s); s.loader.exec_module(r2lib); T = r2lib.load_tower()
PHI, FMAX, NMAX, EMAX = T.PHI, T.FMAX, 3, 3
L11, L12, L13 = T.L11(), T.L12(), T.L13()

# ---- L3413–3428 the thirteen bounds, cell by cell on Λ13 (coords n ℓ k q e f g 2S 2S′ v 2Jc 2K 2J)
def bounds(c):
    n, l, k, q, e, f, g, S2, S2p, v, Jc2, K2, J2 = c
    return [1 <= n <= NMAX, l <= n - 1, 1 <= k <= 4 * l + 2, q <= k, 1 <= e <= EMAX, f <= e - 1,
            g <= min(4 * f + 2, q), S2 <= k, S2p <= g, S2p <= v <= g, Jc2 <= PHI[k], K2 <= Jc2 + 2 * FMAX, abs(J2 - K2) <= 1]
viol = [sum(1 for c in L13 if not b) for b in zip(*[bounds(c) for c in L13])]
print(f'== L3428 all thirteen bounds against the construction, every cell of Λ13 ({len(L13):,}): violations per bound {viol} | all zero {all(x == 0 for x in viol)}')

# ---- L3439–3442 φ̂ observed against the realised maxima
mJc = {k: max(c[10] for c in L11 if c[2] == k) for k in sorted({c[2] for c in L11})}
mJ  = {k: max(c[12] for c in L13 if c[2] == k) for k in sorted({c[2] for c in L13})}
print(f'== L3439–3440 φ̂ = {PHI} | largest 2J_c realised per k (Λ11): {mJc} | equal {mJc == PHI}   (MC L1264\'s wording)')
print(f'   largest 2J realised per k (Λ13): {mJ} | equal to φ̂ {mJ == PHI}   (the main\'s L3439 says "the largest 2J")')

# ---- L3435–3436 cells of Λ12 at f below the cap
below = sum(1 for c in L12 if c[5] < FMAX)
print(f'== L3435–3436 Λ12 cells with f < f_max: {below:,} of {len(L12):,} (printed 39,375 of 70,905) | match {below == 39375}')

# ---- L3433–3434 the tight two-parent K (2K ≤ 2J_c + 2f, the cell\'s own f): the cuts, against the withdrawn 2,475
t12 = sum(1 for c in L12 if c[11] <= c[10] + 2 * c[5]); t13 = sum(1 for c in L13 if c[11] <= c[10] + 2 * c[5])
print(f'== L3433–3434 tight-K cuts: Λ12 {len(L12):,} → {t12:,} (cut {len(L12)-t12:,}) | Λ13 {len(L13):,} → {t13:,} (cut {len(L13)-t13:,})')
print(f'   neither cut is 2,475: {len(L12)-t12 != 2475 and len(L13)-t13 != 2475} — the figure L3477 withdraws corresponds to no cut here; the factorisation breakage is §12.11.5\'s segment')

# ---- the grading column against the provenance column, tabulated (12j-01)
grading = {9: 'exact', 10: 'exact', 11: 'envelope', 12: 'envelope', 13: 'envelope'}
prov = {9: 'law', 10: 'law', 11: 'extent', 12: 'law, weakened', 13: 'law'}
chain = {}
bad = None
for d in (9, 10, 11, 12, 13):
    chain[d] = 'intact' if all(prov[x] == 'law' for x in range(9, d + 1)) else 'extent/weakened at or below'
    pred_boxed = 'exact' if prov[d] == 'law' else 'envelope'
    pred_chain = 'exact' if chain[d] == 'intact' else 'envelope'
    ok_boxed = pred_boxed == grading[d]; ok_chain = pred_chain == grading[d]
    if not ok_boxed and bad is None: bad = d
    print(f'   D{d}: provenance [{prov[d]}] | grading [{grading[d]}] | boxed rule per axis predicts [{pred_boxed}] {"OK" if ok_boxed else "FAILS"} | per chain (L3436–3437 inheritance) predicts [{pred_chain}] {"OK" if ok_chain else "FAILS"}')
print(f'== 12j-01: the boxed rule read per axis first fails at D{bad} (law-taken, graded envelope); read per chain with D13 inheriting through K, all five rows agree')

# ---- L3448 against §22\'s own rule (census row 1073)
M = r2lib.read_member('The_Method_1_6-2.md').split('\n')
a = re.sub(r'\s+', ' ', M[3447].strip() + ' ' + M[3448].strip())
b = re.sub(r'\s+', ' ', M[6026].strip() + ' ' + M[6027].strip())
key = 'from the law that generates the widths, never from the pattern the widths make'
print(f'== L3448 vs §22 L6027: operative clause present at both sites {key in a and key in b} — the flagged "never" is the cited section\'s own rule')
