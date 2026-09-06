# r2-ch12w.py — Phase R2, main §12.11.1.4–.5 (L3269–3317), chat 77.
# L3274–3280 the stage table (cells, composable, fraction, axis, kind) re-measured on every cell of every stage under the
# role matching the two sections define: source (n, ℓ, k, 2S) gaining 2J_c at Λ₁₁, target (e, f, g, 2S′) gaining 2K at Λ₁₂
# and 2J at Λ₁₃ (L3310's five-tuple; kind 2 pairs 2J against 2J_c); Register 625/626's differing Λ₁₂/Λ₁₃ fractions
# (0.6394 / 0.6186) tested against labeled candidate readings. L3298–3301 the Λ₁₀ peak's missing set (485 g = 0 cells,
# five target signatures at 97 each, L.c8 = k ≥ 1); L3306–3311 the Λ₁₃ three-kind partition (35,630 / 13,750 / 22,680 /
# 72,060). tower-2.py by path via r2lib. Deterministic.
import importlib.util, os
from collections import Counter
H = os.path.dirname(os.path.abspath(__file__))
s = importlib.util.spec_from_file_location('r2lib', os.path.join(H, 'r2lib.py')); r2lib = importlib.util.module_from_spec(s); s.loader.exec_module(r2lib); T = r2lib.load_tower()

L8, L9, L10, L11, L12, L13 = T.L8(), T.L9(), T.L10(), T.L11(), T.L12(), T.L13()
# coordinate layout control: (n, ℓ, k, q, e, f, g, 2S) + 2S′(8) + v(9) + 2J_c(10) + 2K(11) + 2J(12)
phi = {k: max(c[10] for c in L11 if c[2] == k) for k in {c[2] for c in L11}}
ok = (all(c[8] <= c[9] <= c[6] for c in L10) and all(c[10] <= phi[c[2]] for c in L11)
      and all(c[11] <= c[10] + 2 for c in L12) and all(max(0, c[11] - 1) <= c[12] <= c[11] + 1 for c in L13))
print(f'== layout control: v∈[2S′,g], 2J_c≤φ̂(k), 2K≤2J_c+2f_max, |2J−2K|≤1 on every cell: {ok} | φ̂ {phi}')

S4 = {(c[0], c[1], c[2], c[7]) for c in L8}                                   # source (n, ℓ, k, 2S)
S5 = {(c[0], c[1], c[2], c[7], c[10]) for c in L11}                           # source with the core's 2J_c (Λ₁₁ on)
t4 = lambda c: (c[4], c[5], c[6], c[8])
rows = []
rows.append(('Λ8 ', L8, sum(1 for c in L8 if (c[4], c[5], c[6]) in S4)))      # three against four
rows.append(('Λ9 ', L9, sum(1 for c in L9 if t4(c) in S4)))
rows.append(('Λ10', L10, sum(1 for c in L10 if t4(c) in S4)))
rows.append(('Λ11', L11, sum(1 for c in L11 if t4(c) in S4)))                 # the added axis is source-side; target unchanged
rows.append(('Λ12', L12, sum(1 for c in L12 if t4(c) + (c[11],) in S5)))      # target (e,f,g,2S′,2K) against source (n,ℓ,k,2S,2J_c)
rows.append(('Λ13', L13, sum(1 for c in L13 if t4(c) + (c[12],) in S5)))      # target (e,f,g,2S′,2J) — L3310's five-tuple
PRN = {'Λ8 ': (976, 0, '0.0000'), 'Λ9 ': (1654, 1169, '0.7068'), 'Λ10': (2535, 2050, '0.8087'), 'Λ11': (13585, 9450, '0.6956'), 'Λ12': (70905, 46740, '0.6592'), 'Λ13': (199130, 127070, '0.6381')}
REG = {'Λ12': 0.6394, 'Λ13': 0.6186}
print('== L3274–3280 stage | cells | composable | fraction | printed | Register 625/626')
for name, X, comp in rows:
    pc, pcomp, pf = PRN[name]; f = comp / len(X)
    tail = f' | Register 625/626 {REG[name]}' if name in REG else ''
    print(f'   {name} {len(X):>8,} (printed {pc:,} {"OK" if len(X)==pc else "MISMATCH"}) | composable {comp:>8,} (printed {pcomp:,} {"OK" if comp==pcomp else "MISMATCH"}) | {f:.4f} (printed {pf} {"OK" if f"{f:.4f}"==pf else "MISMATCH"}){tail}')
# candidate readings for Register 625/626's Λ₁₂ / Λ₁₃ figures
c12a = sum(1 for c in L12 if t4(c) in S4)                                     # 2K ignored
c12b = sum(1 for c in L12 if t4(c) + (c[11],) in S5)                          # 2K ↔ 2J_c (the section's)
c13a = sum(1 for c in L13 if t4(c) + (c[12],) in S5)                          # 2J ↔ 2J_c (the section's)
c13b = sum(1 for c in L13 if t4(c) + (c[11],) in S5)                          # 2K ↔ 2J_c at Λ₁₃
c13c = sum(1 for c in L13 if t4(c) + (c[11],) in S5 and t4(c) + (c[12],) in S5)   # both
S6 = {(c[0], c[1], c[2], c[7], c[10], c[11]) for c in L12}
c13d = sum(1 for c in L13 if t4(c) + (c[12], ) in S5 and (c[4], c[5], c[6], c[8], c[12]) in {(x[0], x[1], x[2], x[7], x[10]) for x in L12})
print(f'== Register 625/626 candidates: Λ12 — 2K ignored {c12a:,} = {c12a/len(L12):.4f}, 2K↔2J_c {c12b:,} = {c12b/len(L12):.4f} (0.6394 ⇒ {round(0.6394*len(L12)):,} cells; neither {"matches" if round(c12a/len(L12),4)!=0.6394 and round(c12b/len(L12),4)!=0.6394 else "…"}) | Λ13 — 2J↔2J_c {c13a:,} = {c13a/len(L13):.4f}, 2K↔2J_c {c13b:,} = {c13b/len(L13):.4f}, both {c13c:,} = {c13c/len(L13):.4f} (0.6186 ⇒ {round(0.6186*len(L13)):,} cells)')
# L3298–3301 the Λ₁₀ peak's missing set
nc10 = [c for c in L10 if t4(c) not in S4]
g0 = [c for c in L10 if c[6] == 0]
sigs = Counter(t4(c) for c in nc10)
print(f'== L3298–3301 Λ10: non-composable {len(nc10)} (printed 485) | all g = 0 {all(c[6]==0 for c in nc10)} | every g = 0 cell non-composable {set(map(tuple,g0))==set(map(tuple,nc10))} — {len(g0)} for {len(nc10)} | failing target signatures {len(sigs)} (printed five) at {sorted(set(sigs.values()))} cells each (printed 97): {sorted(sigs)} | the failing coordinate is k: g = 0 target needs source k = 0, and min k over sources = {min(c[2] for c in L8)} (L.c8 k ≥ 1)')
# L3306–3311 the Λ₁₃ three kinds
nc13 = [c for c in L13 if t4(c) + (c[12],) not in S5]
k1 = [c for c in nc13 if c[6] == 0]; k2 = [c for c in nc13 if c[6] >= 1 and c[12] >= 6]; k3 = [c for c in nc13 if c[6] >= 1 and c[12] <= 5]
maxJc = max(c[10] for c in L11); maxJ = max(c[12] for c in L13)
print(f'== L3306–3311 Λ13 kinds: g = 0 {len(k1):,} (printed 35,630) | 2J ∈ {{6,7,8}} with g ≥ 1 {len(k2):,} (printed 13,750), 2J values {sorted({c[12] for c in k2})} | combination only {len(k3):,} (printed 22,680), single-coordinate check: every kind-3 cell has g ≥ 1 and 2J ≤ {maxJc} {all(c[12]<=maxJc for c in k3)} | total {len(nc13):,} (printed 72,060) of {len(L13):,} = {100*len(nc13)/len(L13):.2f}% (printed 36.19%) | exhaustive {len(k1)+len(k2)+len(k3)==len(nc13)}')
print(f'   L3313 2J reaches {maxJ} and 2J_c reaches {maxJc}; 2K max {max(c[11] for c in L12)} = φ̂_max + 2f_max = {max(phi.values())} + 2 | three values of 2J with no source counterpart: {sorted(set(range(maxJc+1, maxJ+1)))}')
