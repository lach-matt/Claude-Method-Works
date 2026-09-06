# r2-ch12y.py — Phase R2, main §12.11.2 "Three excluded forms, and the fold has a name" (L3363–3393), chat 78.
# Re-measured on all cells or pairs: the conjugation symmetry terms(ℓᵏ) = terms(ℓ^(4ℓ+2−k)) for every k on the p and
# d shells (L3365–3366); max2J(ℓ,k) unimodal, peaking at half filling, 25 at f⁷, zero at closure (L3368–3369) and its
# conjugation symmetry; min(g, 4f+2−g) invariant under the fold (L3368); the axis-9 envelope gap parity 5 / fold 1 /
# both 1 and the axis-11 gap ceiling 16 / parity 24 / triangle 17 at the caps of §7.4 (L3371–3372); the five
# presentations of the exact coupling region and their closure failures 50,592 / 52,080 / 17,856 / 7,254 / 2,443 with
# the first meet failure manufacturing J = ½ from S = L = 0 (L3375–3378); the four-cap join/meet check of
# {|2L−2S| ≤ 2J ≤ 2L+2S} — 0 join failures and 2,862 / 12,489 / 40,887 / 110,229 failing meets at caps 6, 8, 10, 12,
# unordered pairs per MC L1256 — and the parity-congruence collapse, 1,848 join failures at cap 6 (L3385–3390).
# Cross-sites: main L8290 (U4), MC L1254/L1260. tower-2.py by path via r2lib. Deterministic (no wall-clock).
import importlib.util, os, itertools
from collections import Counter
H = os.path.dirname(os.path.abspath(__file__))
s = importlib.util.spec_from_file_location('r2lib', os.path.join(H, 'r2lib.py')); r2lib = importlib.util.module_from_spec(s); s.loader.exec_module(r2lib); T = r2lib.load_tower()
PHI = T.PHI

# lifted verbatim from r2-ch12q.py (chat 76) — LS terms of ℓ^k by microstate enumeration (L3059–3063)
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
def jc_values(l, k, S2): return sorted({j for (s2, L2), _ in terms(l, k).items() if s2 == S2 for j in range(abs(L2 - s2), L2 + s2 + 1, 2)})

def max2J(l, k): return max(s2 + L2 for (s2, L2) in terms(l, k))

# ---- L3365–3366: terms(ℓᵏ) = terms(ℓ^(4ℓ+2−k)) for every k on the p and d shells
print('== L3365–3366 conjugation symmetry of terms, as multisets:')
for l, nm in [(1, 'p'), (2, 'd')]:
    ok = all(terms(l, k) == terms(l, 4 * l + 2 - k) for k in range(0, 4 * l + 2 + 1))
    print(f'   {nm} shell, every k in 0..{4*l+2}: terms(ℓᵏ) == terms(ℓ^(4ℓ+2−k)) {ok}')

# ---- L3368–3369: max2J(ℓ,k) — unimodal, peak at half filling, 25 at f⁷, zero at closure; symmetric under the fold
print('== L3368–3369 max2J(ℓ,k):')
for l, nm in [(1, 'p'), (2, 'd'), (3, 'f')]:
    vals = [max2J(l, k) for k in range(0, 4 * l + 2 + 1)]
    pk = vals.index(max(vals))
    rising = all(vals[i] <= vals[i + 1] for i in range(pk)); falling = all(vals[i] >= vals[i + 1] for i in range(pk, len(vals) - 1))
    sym = all(vals[k] == vals[4 * l + 2 - k] for k in range(len(vals)))
    print(f'   {nm}: {vals} | unimodal {rising and falling} | peak at k = {pk} (half filling {2*l+1}: {pk == 2*l+1}) | zero at k=0 and closure {vals[0] == 0 and vals[-1] == 0} | symmetric under k↦4ℓ+2−k {sym}')
print(f'   25 at f⁷: max2J(3,7) = {max2J(3,7)}')

# ---- L3368: min(g, 4f+2−g) invariant under g ↦ 4f+2−g (the fold), f = 0, 1
inv = all(min(g, 4 * f + 2 - g) == min(4 * f + 2 - g, g) and min(g, 4 * f + 2 - g) == min(4 * f + 2 - (4 * f + 2 - g), 4 * f + 2 - g) for f in (0, 1) for g in range(0, 4 * f + 3))
print(f'== L3368 min(g, 4f+2−g) invariant under the fold g ↦ 4f+2−g, f = 0..1, all g: {inv}')

# ---- stages
L8, L9, L10 = T.L8(), T.L9(), T.L10()
spin = {}
for (f, g) in sorted({(c[5], c[6]) for c in L8}):
    spin[(f, g)] = sorted({s2 for (s2, _) in terms(f, g)})

# ---- L3371–3372 axis 9's gap at the caps of §7.4: parity / fold / both over the (f, g) support
print('== L3371–3372 axis 9 gap — support = realised (f, g) of Λ8; envelope 2S′ ∈ [0, g]; exact = spin set of f^g by microstate enumeration:')
par = fld = both = adm = rea = 0
for (f, g) in sorted(spin):
    ex = set(spin[(f, g)]); cap = min(g, 4 * f + 2 - g)
    chk = ex == {sv for sv in range(0, g + 1) if (g - sv) % 2 == 0 and sv <= cap}
    adm += g + 1; rea += len(ex); det = []
    for sv in range(0, g + 1):
        if sv in ex: continue
        p = (g - sv) % 2 == 1; fl = sv > cap
        if p and fl: both += 1; det.append(f'{sv}:both')
        elif p: par += 1; det.append(f'{sv}:parity')
        elif fl: fld += 1; det.append(f'{sv}:fold')
    print(f'   (f,g)=({f},{g}): exact {sorted(ex)} == parity∧fold set {chk} | excluded {" ".join(det) if det else "—"}')
print(f'   TOTAL admitted {adm}, realised {rea}, gap {adm - rea}: parity {par}, fold {fld}, both {both}   (printed: parity 5, fold 1, both 1)')

# ---- L3372 axis 11's gap: support = realised (ℓ, k, 2S) of Λ10; envelope 2J_c ∈ [0, φ̂(k)]; exact = jc_values(ℓ, k, 2S);
# attribution in order: ceiling (2J_c > max2J(ℓ,k)) → parity (2J_c ≢ k mod 2) → triangle (the rest)
sup = sorted({(c[1], c[2], c[7]) for c in L10})
full = sorted({(l, k, s2) for (l, k) in {(c[1], c[2]) for c in L10} for s2 in range(0, k + 1)})
print(f'== L3372 axis 11 gap — support = realised (ℓ,k,2S) of Λ10 ({len(sup)} triples) == all 2S ∈ [0,k] over realised (ℓ,k): {sup == full} | φ̂ = {PHI}')
ce = pa = tr = adm = rea = 0; ce_i = pa_i = tr_i = 0
for (l, k, s2) in sup:
    ex = set(jc_values(l, k, s2)); m = max2J(l, k)
    adm += PHI[k] + 1; rea += len(ex); det = []
    for j in range(0, PHI[k] + 1):
        if j in ex: continue
        # independent (overlapping) counts, for the record
        if j > m: ce_i += 1
        if (j - k) % 2: pa_i += 1
        if j <= m and (j - k) % 2 == 0: tr_i += 1
        # attribution, ceiling first
        if j > m: ce += 1; det.append(f'{j}:ceiling')
        elif (j - k) % 2: pa += 1; det.append(f'{j}:parity')
        else: tr += 1; det.append(f'{j}:triangle')
    print(f'   (ℓ,k,2S)=({l},{k},{s2}): exact {sorted(ex) if ex else "∅"} | max2J {m} | excluded {" ".join(det) if det else "—"}')
print(f'   TOTAL admitted {adm}, realised {rea}, gap {adm - rea}: ceiling {ce}, parity {pa}, triangle {tr}   (printed: ceiling 16, parity 24, triangle 17)')
print(f'   independent (overlapping) counts for the record: >max2J {ce_i}, wrong parity {pa_i}, within-ceiling right-parity unrealised {tr_i}')

# ---- L3375–3378 the five presentations of the exact coupling region
def first_fail(X):
    """first unordered pair (lexicographic scan) whose componentwise meet leaves X; returns (a, b, meet) or None"""
    S = set(X); L = sorted(X)
    for i in range(len(L)):
        for j in range(i + 1, len(L)):
            mt = tuple(min(a, b) for a, b in zip(L[i], L[j]))
            if mt not in S: return L[i], L[j], mt
    return None

E9  = [c for c in L9 if c[8] in spin[(c[5], c[6])]]
PAR = [c for c in L9 if (c[6] - c[8]) % 2 == 0]
CAP = [c for c in L9 if c[8] <= 4 * c[5] + 2 - c[6]]
PC  = [c[:8] + ((c[6] - c[8]) // 2,) for c in E9]
print('== L3375–3378 five presentations — r2lib.closure over ordered pairs incl. self (n², join fails, meet fails); halves are the unordered counts:')
for X, lab, printed in [(E9, 'as 2S′ (exact: parity ∧ fold)', '50,592'), (PAR, 'as parity alone', '52,080'), (CAP, 'as the min-cap alone', '17,856'), (PC, 'as pair count p = (g−2S′)/2 on the exact set', '7,254')]:
    n2, jl, ml = r2lib.closure(X)
    print(f'   [{lab}] n {len(X):,} | join fails {jl:,} (unord {jl//2:,}) | meet fails {ml:,} (unord {ml//2:,}) | j+m {jl+ml:,} (unord {(jl+ml)//2:,})   printed {printed}')

def levels(shells):
    out = set()
    for (l, k) in shells:
        for (s2, L2) in terms(l, k):
            for j in range(abs(L2 - s2), L2 + s2 + 1, 2): out.add((s2, L2, j))
    return sorted(out)
print('== L3377 (2S,2L,2J) presentation — candidate level populations:')
cands = [('levels of the realised shells at caps (s¹ s² p¹ p² p³)', [(0,1),(0,2),(1,1),(1,2),(1,3)]),
         ('levels of the p shell, every k', [(1,k) for k in range(0,7)]),
         ('levels of p and d, every k', [(1,k) for k in range(0,7)] + [(2,k) for k in range(0,11)]),
         ('levels of s, p and d, every k', [(0,k) for k in range(0,3)] + [(1,k) for k in range(0,7)] + [(2,k) for k in range(0,11)]),
         ('levels of s, p, d and f, every k', [(0,k) for k in range(0,3)] + [(1,k) for k in range(0,7)] + [(2,k) for k in range(0,11)] + [(3,k) for k in range(0,15)])]
for lab, sh in cands:
    X = levels(sh); n2, jl, ml = r2lib.closure(X); ff = first_fail(X)
    print(f'   [{lab}] n {len(X)} | join fails {jl:,} (unord {jl//2:,}) | meet fails {ml:,} (unord {ml//2:,}) | first failing meet {ff[0]} ∧ {ff[1]} = {ff[2]}' if ff else f'   [{lab}] n {len(X)} | no meet failure')

# ---- L3385–3390 the four-cap check of the triangle, unordered pairs (MC L1256)
print('== L3385–3390 T = {(2L,2S,2J): |2L−2S| ≤ 2J ≤ 2L+2S} on the box {0..cap}³:')
for cap, printed in [(6, '2,862'), (8, '12,489'), (10, '40,887'), (12, '110,229')]:
    Tset = [(a, b, j) for a in range(cap + 1) for b in range(cap + 1) for j in range(abs(a - b), min(a + b, cap) + 1)]
    n2, jl, ml = r2lib.closure(Tset)
    print(f'   cap {cap}: |T| {len(Tset):,} | join fails {jl} | meet fails unordered {ml//2:,}   printed {printed}')
    if cap == 6:
        ff = first_fail(Tset)
        print(f'      first failing meet: {ff[0]} ∧ {ff[1]} = {ff[2]}')
        Tp = [t for t in Tset if (t[0] + t[1] - t[2]) % 2 == 0]
        n2p, jlp, mlp = r2lib.closure(Tp)
        print(f'      + parity congruence 2J ≡ 2L+2S (mod 2): |T∩par| {len(Tp):,} | join fails unordered {jlp//2:,} (ordered {jlp:,})   printed 1,848 | meet fails unordered {mlp//2:,}')
