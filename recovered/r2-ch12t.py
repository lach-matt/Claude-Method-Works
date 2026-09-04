# r2-ch12t.py — Phase R2, main §12.11.1.1 (L3177–3204), chat 77.
# L3183–3192: "for each cell of Λ₁₀, enumerate the terms of the source shell by vector coupling and take the largest 2J_c
# that occurs; sum those over the cells to get the exact count. Divide by |Λ₁₁|, which is the same enumeration with 2J_c
# bounded by φ̂(k) instead" — the four printed rows (caps, |Λ₁₁|, exact, density) re-measured on every Λ₁₀ cell at each
# cap under the method as written and under its candidate readings; L3194–3195 monotonicity; L3197–3199 the causes
# ("when the d shell opens"; "the envelope grows faster than the exact set"); §12.11.1's own axis-11 figure (L3084 17.0 %,
# realised values) at the same caps. terms / new_terms / jc_values lifted verbatim from r2-ch12q.py (chat 76), TERMS / L8_at /
# phi_at verbatim from r2-ch12r.py (chat 76) — all owed to r2lib. tower-2.py by path via r2lib. Deterministic.
import importlib.util, os, itertools, math
from collections import Counter, defaultdict
H = os.path.dirname(os.path.abspath(__file__))
s = importlib.util.spec_from_file_location('r2lib', os.path.join(H, 'r2lib.py')); r2lib = importlib.util.module_from_spec(s); s.loader.exec_module(r2lib); T = r2lib.load_tower()

# lifted verbatim from r2-ch12q.py (chat 76)
def terms(l, k):
    if k == 0: return Counter({(0, 0): 1})
    orbs = [(ml, ms) for ml in range(-l, l + 1) for ms in (-1, 1)]
    ms_count = Counter((2 * sum(o[0] for o in c), sum(o[1] for o in c)) for c in itertools.combinations(orbs, k))
    out = Counter()
    while ms_count:
        ML2 = max(m for m, _ in ms_count); MS2 = max(sv for m, sv in ms_count if m == ML2)
        out[(MS2, ML2)] += 1
        for ml2 in range(-ML2, ML2 + 1, 2):
            for ms2 in range(-MS2, MS2 + 1, 2):
                ms_count[(ml2, ms2)] -= 1
                if ms_count[(ml2, ms2)] == 0: del ms_count[(ml2, ms2)]
                assert ms_count.get((ml2, ms2), 0) >= 0
    return out
# lifted verbatim from r2-ch12q.py (chat 76)
def new_terms(l, v): return terms(l, v) - terms(l, v - 2) if v >= 2 else terms(l, v)   # multiset difference (L3081)
# lifted verbatim from r2-ch12q.py (chat 76)
def jc_values(l, k, S2): return sorted({j for (s2, L2), _ in terms(l, k).items() if s2 == S2 for j in range(abs(L2 - s2), L2 + s2 + 1, 2)})
# lifted verbatim from r2-ch12r.py (chat 76)
_T = {}
def TERMS(l, k):
    if (l, k) not in _T: _T[(l, k)] = terms(l, k)
    return _T[(l, k)]
# lifted verbatim from r2-ch12r.py (chat 76)
def L8_at(caps):
    n_max, e_max, l_max, k_max, f_max = caps
    return [(n, l, k, q, e, f, g, S2) for n in range(1, n_max + 1) for l in range(0, min(l_max, n - 1) + 1) for k in range(1, min(k_max, 4 * l + 2) + 1)
            for q in range(0, k + 1) for e in range(1, e_max + 1) for f in range(0, min(f_max, e - 1) + 1) for g in range(0, min(4 * f + 2, q) + 1) for S2 in range(0, k + 1)]
# lifted verbatim from r2-ch12r.py (chat 76)
def phi_at(caps):
    n_max, e_max, l_max, k_max, f_max = caps
    raw = {k: max(L2 + s2 for l in range(l_max + 1) if k <= 4 * l + 2 for (s2, L2) in TERMS(l, k)) for k in range(1, k_max + 1)}
    env = {}; run = 0
    for k in range(1, k_max + 1): run = max(run, raw[k]); env[k] = run
    return raw, env

def B10(g): return sum(g - s + 1 for s in range(g + 1))                      # Λ₁₀ cells over a Λ₈ cell: (2S′, v), 0 ≤ 2S′ ≤ v ≤ g (tower-2.py's fibre)
SH = 'spdf'
def own_max(l, k): return max(L2 + s2 for (s2, L2) in TERMS(l, k))          # the largest 2J_c that occurs among the terms of ℓᵏ
def own_max_S(l, k, S2):                                                     # … among the terms of ℓᵏ carrying the cell's own 2S (L3082's restriction)
    j = jc_values(l, k, S2); return max(j) if j else None

def table(caps):
    raw, env = phi_at(caps); L8c = L8_at(caps)
    n10 = 0; env_cells = 0; env_sum = 0
    A = B = C = D = E = F = 0        # candidate exact counts
    by_shell = defaultdict(lambda: [0, 0])
    for c in L8c:
        l, k, S2, g = c[1], c[2], c[7], c[6]; w = B10(g); n10 += w
        env_cells += w * (env[k] + 1); env_sum += w * env[k]
        om = own_max(l, k); A += w * (om + 1)                                # A: every 2J_c in [0, own max] (all integers)
        oms = own_max_S(l, k, S2); B += w * ((oms + 1) if oms is not None else 0)   # B: [0, own max among terms with the cell's 2S]
        C += w * len(jc_values(l, k, S2))                                   # C: realised values only (§12.11.1 L3082, r2-ch12q)
        D += w * om                                                          # D: the largest 2J_c summed literally
        E += w * ((om - k % 2) // 2 + 1)                                     # E: [k mod 2, own max] in steps of 2
        F += w * (raw[k] + 1)                                                # F: [0, raw φ̂(k)] (the un-enveloped bound over all shells)
        by_shell[(l, k)][0] += w * (om + 1); by_shell[(l, k)][1] += w * (env[k] + 1)
    return dict(raw=raw, env=env, n8=len(L8c), n10=n10, n11=env_cells, envsum=env_sum, A=A, B=B, C=C, D=D, E=E, F=F, shells=by_shell)

ROWS = [((3, 3, 1, 3, 1), 13585, 10585, 77.9), ((4, 4, 1, 6, 1), 226609, 106421, 47.0), ((4, 4, 2, 6, 2), 1225415, 616725, 50.3), ((5, 5, 2, 6, 2), 2341841, 1228816, 52.5)]

# ---- control at the book's caps: the tower's own Λ₁₀ / Λ₁₁ against the fibre sums
L10, L11 = T.L10(), T.L11(); t0 = table((3, 3, 1, 3, 1))
jc11 = defaultdict(set)
for c in L11: jc11[c[2]].add(c[10])
print(f'== control (3,3,1,3,1): tower Λ10 {len(L10):,} = fibre sum {t0["n10"]:,} {len(L10)==t0["n10"]} | tower Λ11 {len(L11):,} = Σ(φ̂(k)+1) over Λ10 {t0["n11"]:,} {len(L11)==t0["n11"]} | 2J_c per k in the tower {dict(sorted((k, (min(v), max(v), len(v))) for k, v in jc11.items()))} = every integer in [0, φ̂(k)] {all(sorted(v)==list(range(max(v)+1)) for v in jc11.values())}')
print(f'   φ̂ raw {t0["raw"]} envelope {t0["env"]} | own max 2J_c by shell: ' + ', '.join(f'{SH[l]}{k} {own_max(l,k)}' for l in range(2) for k in range(1, min(3, 4*l+2)+1)))

# ---- the four rows under the method as written and its readings
print('== L3188–3192 caps | Λ8 | Λ10 | |Λ11| envelope (printed) | exact under A [0,own max] · B [0,own max at own 2S] · C realised (§12.11.1) · D Σ own max · E parity interval · F [0,raw φ̂] (printed) | densities')
dens = {}
for caps, p11, pex, pd in ROWS:
    t = table(caps); dens[caps] = {K: 100 * t[K] / t['n11'] for K in 'ABCDEF'}
    hit = [K for K in 'ABCDEF' if t[K] == pex]
    print(f'   {caps}: Λ8 {t["n8"]:,} | Λ10 {t["n10"]:,} | |Λ11| {t["n11"]:,} (printed {p11:,} {"OK" if t["n11"]==p11 else "MISMATCH"}) | A {t["A"]:,} B {t["B"]:,} C {t["C"]:,} D {t["D"]:,} E {t["E"]:,} F {t["F"]:,} (printed exact {pex:,}: reproduced by {hit if hit else "none"}) | density A {dens[caps]["A"]:.1f} B {dens[caps]["B"]:.1f} C {dens[caps]["C"]:.1f} D/Σφ̂ {100*t["D"]/t["envsum"]:.1f} E {dens[caps]["E"]:.1f} F {dens[caps]["F"]:.1f} | printed {pd}')
    print(f'      shells present {sorted({SH[l] for (l, k) in t["shells"]})} | φ̂ raw {list(t["raw"].values())} envelope {list(t["env"].values())} | per (ℓ,k) exact/envelope under A: ' + ' '.join(f'{SH[l]}{k}:{a:,}/{b:,}' for (l, k), (a, b) in sorted(t["shells"].items())))

# ---- L3194–3195 monotonicity, L3197–3199 the causes
seq = [dens[c]['A'] for c, _, _, _ in ROWS]
print(f'== L3194 "not monotone in the caps" under A: {[round(x, 1) for x in seq]} — falls then rises {seq[0] > seq[1] < seq[2] < seq[3]}; under C (§12.11.1\'s definition): {[round(dens[c]["C"], 1) for c, _, _, _ in ROWS]} monotone falling {all(dens[ROWS[i][0]]["C"] > dens[ROWS[i+1][0]]["C"] for i in range(3))}')
print('== L3194/L3197 "falls … when the d shell opens": ℓ_max by row ' + ', '.join(f'{c} ℓ_max={c[2]}' for c, _, _, _ in ROWS) + ' — the d shell is absent at the 47.0 % row and enters at the 50.3 % row (ℓ ≤ ℓ_max; L3186 names the tuple (n_max, e_max, ℓ_max, k_max, f_max))')
def growth(c1, c2):
    a, b = table(c1), table(c2); return a['A'], b['A'], a['n11'], b['n11']
for c1, c2 in [((3, 3, 1, 3, 1), (4, 4, 1, 6, 1)), ((4, 4, 1, 6, 1), (4, 4, 2, 6, 2)), ((4, 4, 2, 6, 2), (5, 5, 2, 6, 2))]:
    a1, a2, e1, e2 = growth(c1, c2); print(f'   {c1} → {c2}: exact ×{a2/a1:.2f}, envelope ×{e2/e1:.2f} — envelope grows faster {e2/e1 > a2/a1}')
# what each cap change does on its own, from the book's caps: one coordinate at a time, and the d shell alone
print('== single-cap variations from (3,3,1,3,1) under A (which coordinate moves the density):')
for caps in [(4, 3, 1, 3, 1), (3, 4, 1, 3, 1), (3, 3, 2, 3, 1), (3, 3, 1, 6, 1), (3, 3, 1, 3, 2), (4, 4, 1, 3, 1), (4, 4, 1, 6, 1), (4, 4, 2, 6, 1), (4, 4, 2, 3, 1), (3, 3, 2, 6, 1)]:
    t = table(caps); print(f'   {caps}: |Λ11| {t["n11"]:,} exact {t["A"]:,} density {100*t["A"]/t["n11"]:.1f} | φ̂ envelope {list(t["env"].values())}')
# where the shortfall sits at the 47.0 % row: p⁴, p⁵, p⁶ under the running envelope
t = table((4, 4, 1, 6, 1))
print('   (4,4,1,6,1) shortfall by (ℓ,k), envelope − exact under A: ' + ', '.join(f'{SH[l]}{k} {b-a:,} (own max {own_max(l,k)} vs φ̂ {t["env"][k]})' for (l, k), (a, b) in sorted(t['shells'].items()) if b > a) + f' | total {t["n11"]-t["A"]:,}')
