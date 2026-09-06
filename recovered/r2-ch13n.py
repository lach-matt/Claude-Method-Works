# r2-ch13n.py — chat 84, computable batch for the section read §16.1–§16.5.1 (main L4332–L4481).
# Deterministic: no wall-clock, no randomness outside a fixed seed. Imports r2lib by path.
import importlib.util, os, math, random, itertools, collections
H = os.path.dirname(os.path.abspath(__file__))
s = importlib.util.spec_from_file_location('r2lib', os.path.join(H, 'r2lib.py'))
r2lib = importlib.util.module_from_spec(s); s.loader.exec_module(r2lib)
T = r2lib.load_tower()

def head(t): print('\n== ' + t + ' ==')

# ---------------------------------------------------------------- rank helper
def rank(Mx, tol=1e-7):
    A = [row[:] for row in Mx]; m = len(A); n = len(A[0]) if m else 0; r = 0
    for c in range(n):
        piv = max(range(r, m), key=lambda i: abs(A[i][c])) if r < m else None
        if piv is None or abs(A[piv][c]) < tol: continue
        A[r], A[piv] = A[piv], A[r]
        pv = A[r][c]
        for i in range(m):
            if i != r and abs(A[i][c]) > 0:
                f = A[i][c] / pv
                for j in range(c, n): A[i][j] -= f * A[r][j]
        r += 1
        if r == m: break
    return r

def jac(F, p, dq, h=1e-5):
    dp = len(p); J = [[0.0] * dp for _ in range(dq)]
    for i in range(dp):
        a = list(p); b = list(p); a[i] += h; b[i] -= h
        fa = F(a); fb = F(b)
        for j in range(dq): J[j][i] = (fa[j] - fb[j]) / (2 * h)
    return J

# ------------------------------------- C1/C2/C3  L4338, L4342, L4344, L4442
head('C1-C3  the counting argument: D >= dim q - dim p, on 7 dimension pairs x 60 maps')
PAIRS = [(2, 3), (3, 4), (3, 5), (4, 6), (5, 7), (2, 4), (4, 4)]
rng = random.Random(160401)
tot = 0; bound_ok = 0; corr_ok = 0; corr_n = 0; eq_full = 0; eq_n = 0
for (dp, dq) in PAIRS:
    for _ in range(60):
        A = [[rng.uniform(-2, 2) for _ in range(dp)] for _ in range(dq)]
        B = [[rng.uniform(-2, 2) for _ in range(dp)] for _ in range(dq)]
        C = [rng.uniform(-1, 1) for _ in range(dq)]
        def F(p, A=A, B=B, C=C, dq=dq, dp=dp):
            return [sum(A[j][i] * math.sin(B[j][i] * p[i] + C[j]) for i in range(dp))
                    + C[j] * math.prod(p[:min(dp, 2)]) for j in range(dq)]
        p0 = [rng.uniform(0.3, 1.7) for _ in range(dp)]
        rk = rank(jac(F, p0, dq)); D = dq - rk
        tot += 1
        if D >= dq - dp and rk <= min(dp, dq): bound_ok += 1
        if dq > dp:
            corr_n += 1
            if D >= 1: corr_ok += 1
        if dq == dp:
            eq_n += 1
            if D == 0: eq_full += 1
print(f'maps run                                    {tot}   (7 pairs x 60)')
print(f'D = dim q - rank >= dim q - dim p           {bound_ok} of {tot}')
print(f'corollary  dim q > dim p  =>  D >= 1        {corr_ok} of {corr_n}')
print(f'dim q = dim p  and  D = 0 (generic maps)    {eq_full} of {eq_n}')

# L4442 / L11622: "That is D = 0, in the special case dim q = dim p".
# Construct a rank-deficient map with dim q = dim p: q4 is a function of q1..q3.
def Fdeg(p):
    a = math.sin(p[0]) + p[1] ** 2
    b = math.cos(p[1]) + p[2]
    c = p[2] * p[3] + p[0]
    return [a, b, c, a * b - c]          # fourth output functionally dependent
rk = rank(jac(Fdeg, [0.4, 0.9, 1.3, 0.7], 4))
print(f'constructed dim q = dim p = 4, rank         {rk}   => D = {4 - rk}  '
      f'(so dim q = dim p does NOT force D = 0)')

# ------------------------------------------------ C4  L4347 the Lambda example
head('C4  L4347  p = (T,n,Z,sigma), q = (nu,delta,V,r,w,e): rank 4, D = 2')
print(f'dim p = 4, dim q = 6, dim q - dim p         {6 - 4}')
# the two named relations, as functions on q = (nu, delta, V, r, w, e)
def g1(q): return q[2] - 4.0 * q[0] / 3.0          # (a)  V = 4nu/3
def g2(q): return q[4] - q[2] * q[5]               # (b)  w = V.e
q0 = [1.3, 0.7, 1.9, 0.55, 2.4, 1.1]
G = [jac(lambda z: [g1(z)], q0, 1)[0], jac(lambda z: [g2(z)], q0, 1)[0]]
print(f'rank of the two relation gradients on q     {rank(G)}   (2 = functionally independent)')

# ------------------------------------------ C10/C11  L4385-4396 the D1 tripwire
head('C10-C11  L4385-4396  the tripwire table, and 150 of 216 rejected')
SUB = {'s': 0, 'p': 1, 'd': 2, 'f': 3}
def dets(l, k):
    orbs = [(ml, ms) for ml in range(-l, l + 1) for ms in (1, -1)]
    return [(sum(o[1] for o in c), sum(o[0] for o in c)) for c in itertools.combinations(orbs, k)]
def spin_table(l, k):
    N = collections.Counter()
    for tms, tml in dets(l, k): N[tms] += 1
    return N
def allowed_2S(l, k):
    N = spin_table(l, k)
    return sorted(x for x in range(k % 2, k + 1, 2) if N[x] - N[x + 2] > 0)
ROWS = [('s', 1, [1], 1, 2), ('s', 2, [0], 2, 3), ('p', 2, [0, 2], 1, 3), ('p', 3, [1, 3], 2, 4),
        ('p', 5, [1], 5, 6), ('d', 4, [0, 2, 4], 2, 5), ('d', 7, [1, 3], 6, 8),
        ('d', 9, [1], 9, 10), ('f', 4, [0, 2, 4], 2, 5)]
bad = 0
for sub, k, adm, rej, off in ROWS:
    a = allowed_2S(SUB[sub], k)
    ok_set = (a == adm); ok_off = (off == k + 1); ok_rej = (rej == off - len(a))
    if not (ok_set and ok_off and ok_rej): bad += 1
    print(f'  {sub}{k:<3} printed {str(adm):<12} measured {str(a):<12} '
          f'rejected/offered {rej}/{off} -> measured {off - len(a)}/{k + 1}  '
          f'{"OK" if ok_set and ok_off and ok_rej else "MISMATCH"}')
print(f'printed rows disagreeing with measurement   {bad} of 9')
off_tot = 0; adm_tot = 0
for sub, l in SUB.items():
    for k in range(1, 4 * l + 3):
        off_tot += k + 1; adm_tot += len(allowed_2S(l, k))
print(f'offered, s+p+d+f complete, k = 1..4l+2      {off_tot}   (printed 216)')
print(f'admissible                                  {adm_tot}')
print(f'rejected                                    {off_tot - adm_tot}   (printed 150)')
print(f'share rejected                              {100.0 * (off_tot - adm_tot) / off_tot:.4f} %'
      f'   (printed 69.4 %)')

# --------------------------------------- C12  L4398-4400 seniority and core J
head('C12  L4398-4400  d4 with 2S = 2 admits v in {2,4}; d3 with 2S = 3 admits 2J_c')
def terms(l, k):
    X = collections.Counter()
    for tms, tml in dets(l, k): X[(tms, tml)] += 1
    out = collections.Counter()
    mx = 2 * l * k if k else 0
    for tS in range(k % 2, k + 1, 2):
        for L in range(0, l * k + l + 2):
            D = (X[(tS, L)] - X[(tS + 2, L)]) - (X[(tS, L + 1)] - X[(tS + 2, L + 1)])
            if D > 0: out[(tS, L)] = D
    return out
def seniorities(l, k, tS):
    vs = []
    for v in range(k % 2, min(k, 4 * l + 2 - k) + 1, 2):
        tv = terms(l, v); tp = terms(l, v - 2) if v >= 2 else collections.Counter()
        if any(L for (S2, L), c in tv.items() if S2 == tS and c - tp.get((S2, L), 0) > 0) or \
           any((S2 == tS and c - tp.get((S2, L), 0) > 0) for (S2, L), c in tv.items()):
            vs.append(v)
    return vs
print(f'd4, 2S = 2, seniorities                     {seniorities(2, 4, 2)}   (printed {{2, 4}})')
t3 = terms(2, 3)
q_terms = sorted((S2, L) for (S2, L), c in t3.items() if S2 == 3)
J2 = sorted({j2 for (S2, L) in q_terms for j2 in range(abs(2 * L - S2), 2 * L + S2 + 1, 2)})
print(f'd3, 2S = 3, terms (2S, L)                   {q_terms}')
print(f'd3, 2S = 3, admissible 2J_c                 {J2}   (printed {{1, 3, 5, 7, 9}})')

# ------------------------------------------------- C13/C14  L4415 and L4423-26
head('C13-C14  L4415 the 540.0 / 1215.0 pair; L4423-4426 the 0.09 sigma')
print(f'w = 3.nu.e over w = V.e with V = 4nu/3       ratio {3.0 / (4.0 / 3.0):.4f}'
      f'   printed {1215.0 / 540.0:.4f}')
a, sa, b, sb = 804633059.0, 8.2, 804633057.8, 10.6
d = abs(a - b); sc = math.sqrt(sa * sa + sb * sb)
print(f'difference {d:.1f} MHz, combined sigma {sc:.3f} MHz, agreement {d / sc:.4f} sigma'
      f'   (printed 0.09)')

# ---------------------------- C15/C18  L4428 the tree; L4450-4457 totality, 6912
head('C15  L4428  Lambda constraint graph is a tree: exactly one path between coordinates')
L8 = T.L8()
axes = list(range(8)); alpha = [sorted({c[i] for c in L8}) for i in axes]
sizes = [len(a) for a in alpha]
box = math.prod(sizes)
print(f'Lambda-8 cells {len(L8)}, alphabet sizes {tuple(sizes)}, ambient box {box}   (printed 6,912)')
EDGES = [(0, 1), (1, 2), (2, 3), (3, 6), (6, 5), (5, 4), (2, 7)]   # n-l-k-q-g-f-e, 2S off k
print(f'edges {len(EDGES)} on 8 nodes, is_tree                 {r2lib.is_tree(8, EDGES)}')
adj = collections.defaultdict(list)
for u, v in EDGES: adj[u].append(v); adj[v].append(u)
def paths(a, b):
    out = []; st = [(a, [a])]
    while st:
        x, pth = st.pop()
        if x == b: out.append(pth); continue
        for y in adj[x]:
            if y not in pth: st.append((y, pth + [y]))
    return out
mult = [(a, b) for a in axes for b in axes if a < b and len(paths(a, b)) != 1]
print(f'coordinate pairs with != 1 path             {len(mult)} of {8 * 7 // 2}')

head('C18-C19  L4454-4456  chi total on every ambient point; 30,000 draws vs 6,912 cells')
cells = set(L8)
undec = 0; agree = 0
for pt in itertools.product(*alpha):
    chi = 1 if pt in cells else 0
    if chi not in (0, 1): undec += 1
    if (chi == 1) == (pt in cells): agree += 1
print(f'ambient points enumerated                   {box}')
print(f'chi undecided anywhere                      {undec}')
print(f'chi agrees with membership                  {agree} of {box}; on cells {len(cells)} of {len(cells)}')
print(f'30,000 uniform draws vs box of {box}        more draws than cells: {30000 > box}')

# ------------------------------------- C21  L4475 / L7740  the process index, 36
head('C21  L4475 and L7740  the process index: 36 cells, closed, E = 0')
WIT = (2, 2, 3, 0)   # (step, visible, alternatives, committed) named at L7742, outside the index
found = []
for a in range(2, 6):
    for b in range(2, 6):
        for c in range(2, 6):
            for d in range(2, 6):
                for base in (0, 1):
                    S = [x for x in itertools.product(range(base, base + a), range(base, base + b),
                                                      range(base, base + c), range(base, base + d))
                         if x[1] <= x[3]]
                    if len(S) != 36: continue
                    amb = list(itertools.product(range(base, base + a), range(base, base + b),
                                                 range(base, base + c), range(base, base + d)))
                    E = len(r2lib.Rset(set(S))) - len(S)
                    adm = all(base <= WIT[i] < base + [a, b, c, d][i] for i in range(4))
                    found.append((base, a, b, c, d, E, adm, WIT in S))
print(f'readings (base, |step|, |visible|, |alternatives|, |committed|) giving exactly 36 cells: {len(found)}')
for f in found:
    print(f'  base {f[0]}  sizes {f[1:5]}  E = {f[5]}  witness cell in ambient: {f[6]}  '
          f'witness inside index: {f[7]}')
adm = [f for f in found if f[6]]
print(f'of those, readings admitting the L7742 witness cell (2,2,3,0): {len(adm)}')
print(f'of those, with E = 0 and the witness refused:                  '
      f'{len([f for f in adm if f[5] == 0 and not f[7]])}')
