#!/usr/bin/env python3
# r3-q6-measure.py — R3 (Q5 pass 6): the seed-cap finding's figures (SEED-CAP-FINDING.md, EXPANSION-MC54.md; registers
# 603–605 corrected) re-derived with the standard library. Chat 65's seedcensus.py, seedenum3.py (numpy) and
# coverscheck.py are followed definition by definition — the envelope-step census as the law prints it (a STEP (i,j,t):
# t minimal in coordinate j's alphabet at which φ̂_ij(t) = max{c_i : c_j ≤ t} changes; plus the alphabet slots (j,v)),
# the duplicate-free branch and bound over the most constrained uncovered element with the top-r gain bound, the
# checks coverscheck.py makes on covers8.json — with Λ₈ from the seated tower-2.py and the witness sets as bit-masks
# (one Python integer per cell) where seedenum3.py used a numpy matrix. The cap sweep follows SEED-CAP-FINDING's table:
# caps (n,e,ℓ,k,f) as tower-2's loop with caps in place of its constants; a condition is ELEMENT-FORCED at a cap when
# some element of the census is carried only by cells of that type (a cover is infeasible without the type).
import os, sys, io, contextlib, importlib.util, json, hashlib, heapq, statistics
from collections import Counter
H = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(H))
COVERS8 = os.path.join(H, 'covers8.json'); COVERS8_MD5 = '5bb92ebb6cd122115b8b3a96372868e9'   # the seated member: the mirror's bytes (drive/MANIFEST.tsv md5) plus the closing newline the bundle format requires
spec = importlib.util.spec_from_file_location('tower2', os.path.join(H, 'tower-2.py')); T2 = importlib.util.module_from_spec(spec)
with contextlib.redirect_stdout(io.StringIO()): spec.loader.exec_module(T2)
FAIL = []
def check(tag, got, exp):
    ok = got == exp; print('   %-72s %-22s %s' % (tag, repr(got)[:22], 'OK' if ok else 'EXPECTED ' + repr(exp)))
    if not ok: FAIL.append(tag)
N = 8
def lattice(capn, cape, capl, capk, capf):
    out = []
    for n in range(1, capn + 1):
        for l in range(0, min(capl, n - 1) + 1):
            for k in range(1, min(capk, 4 * l + 2) + 1):
                for q in range(0, k + 1):
                    for e in range(1, cape + 1):
                        for f in range(0, min(capf, e - 1) + 1):
                            for g in range(0, min(4 * f + 2, q) + 1):
                                for S2 in range(0, k + 1):
                                    out.append((n, l, k, q, e, f, g, S2))
    return out
def census(cells):
    """alphabet slots (j,v) and envelope steps (i,j,t,phi), as seedcensus.py; witness masks per cell; carriers per element."""
    alph = {j: sorted(set(c[j] for c in cells)) for j in range(N)}
    slots = [(j, v) for j in range(N) for v in alph[j]]
    steps = []
    for i in range(N):
        for j in range(N):
            if i == j: continue
            prev = None
            for t in alph[j]:
                phi = max(c[i] for c in cells if c[j] <= t)
                if phi != prev: steps.append((i, j, t, phi)); prev = phi
    elems = [('A',) + s for s in slots] + [('S', i, j, t) for (i, j, t, phi) in steps]; M = len(elems)
    W = []
    for c in cells:
        m = 0
        for k, (j, v) in enumerate(slots):
            if c[j] == v: m |= 1 << k
        for k, (i, j, t, phi) in enumerate(steps):
            if c[j] <= t and c[i] == phi: m |= 1 << (len(slots) + k)
        W.append(m)
    carriers = [0] * M
    for s, m in enumerate(W):
        mm = m
        while mm:
            b = mm & -mm; carriers[b.bit_length() - 1] |= 1 << s; mm ^= b
    return alph, slots, steps, elems, W, carriers
def bits(m):
    while m:
        b = m & -m; yield b.bit_length() - 1; m ^= b
def search(W, carriers, M, K, limit_nodes=None, first_only=False):
    """all K-covers, each once (seedenum3.py's scheme: branch on the least-carried uncovered element, exclude each tried
    carrier from the later branches; prune when the r largest gains cannot cover what remains)."""
    FULL = (1 << M) - 1; ALL = (1 << len(W)) - 1; found = []; nodes = [0]; stop = [False]
    def rec(cov, allowed, chosen, depth):
        if stop[0]: return
        nodes[0] += 1
        if limit_nodes and nodes[0] > limit_nodes: stop[0] = True; return
        unc = FULL & ~cov
        if unc == 0: found.append(tuple(chosen)); stop[0] = first_only; return
        r = K - depth
        if r == 0: return
        best = None; bestc = 1 << 30
        for k in bits(unc):
            cm = carriers[k] & allowed; n = cm.bit_count()
            if n == 0: return
            if n < bestc: bestc, best, bestcm = n, k, cm
        if r == 1:
            fin = allowed
            for k in bits(unc): fin &= carriers[k]
            for s in bits(fin): found.append(tuple(chosen + [s]))
            if found: stop[0] = first_only
            return
        nu = unc.bit_count(); gains = []
        for s in bits(allowed):
            g = (W[s] & unc).bit_count()
            if g: gains.append(g)
        if sum(heapq.nlargest(r, gains)) < nu: return
        for s in bits(bestcm):
            rec(cov | W[s], allowed, chosen + [s], depth + 1)
            allowed &= ~(1 << s)
    rec(0, ALL, [], 0)
    return found, nodes[0], stop[0] and not first_only
# ---- Λ₈ ------------------------------------------------------------------------------------------------------------
cells = T2.L8(); check('|Λ₈| from tower-2.py, equal to lattice(3,3,1,3,1) in order', (len(cells), cells == lattice(3, 3, 1, 3, 1)), (976, True))
alph, slots, steps, elems, W, carriers = census(cells); M = len(elems)
print('== the envelope-step census on Λ₈ (seedcensus.py)')
check('alphabet slots', len(slots), 25); check('envelope steps', len(steps), 77); check('universe', M, 102)
check('elements with a unique carrier (Chvátal forcing at the root)', [elems[k] for k in range(M) if carriers[k].bit_count() == 1], [])
print('   steps by stepped coordinate j (n l k q e f g 2S): %s; least-carried element has %d carriers' % ([Counter(s[1] for s in steps)[j] for j in range(N)], min(carriers[k].bit_count() for k in range(M))))
print('== every minimum cover of the 102 elements by cells of Λ₈, duplicate-free branch and bound (seedenum3.py)')
f6, n6, _ = search(W, carriers, M, 6); check('6-covers', len(f6), 0); print('   nodes %d' % n6)
f7, n7, _ = search(W, carriers, M, 7)
covs = sorted(set(tuple(sorted(cells[s] for s in f)) for f in f7))
check('7-covers found', len(f7), 24585); check('distinct as sets', len(covs), 24585); print('   nodes %d' % n7)
print('== against the banked enumeration covers8.json (coverscheck.py)')
raw = open(COVERS8, 'rb').read(); check('covers8.json: the seated member ends in one newline; md5 of the rest (drive/MANIFEST.tsv)', (raw.endswith(b'\n'), hashlib.md5(raw[:-1]).hexdigest()), (True, COVERS8_MD5))
d = json.loads(raw); bank = [tuple(sorted(tuple(x) for x in cv)) for cv in d['covers']]
check('n_covers field / listed / distinct', (d['n_covers'], len(bank), len(set(bank))), (24585, 24585, 24585))
check('sizes', dict(Counter(len(c) for c in bank)), {7: 24585})
S = set(cells); check('every listed cell is in Λ₈', all(x in S for cv in bank for x in cv), True)
idx = {c: i for i, c in enumerate(cells)}; FULL = (1 << M) - 1
def covm(cv): 
    m = 0
    for x in cv: m |= W[idx[x]]
    return m
check('listed covers covering all 102 elements', sum(1 for cv in bank if covm(cv) == FULL), 24585)
check('listed covers with a redundant cell', sum(1 for cv in bank if any(covm([y for y in cv if y != x]) == FULL for x in cv)), 0)
check('the enumeration here == covers8.json, set for set', sorted(set(bank)) == covs, True)
print('== what the 24,585 minimum covers have in common (SEED-CAP-FINDING; registers 602–605)')
n = len(covs); freq = Counter(x for cv in covs for x in cv); common = [x for x, k in freq.items() if k == n]
check('cells common to every cover', common, [(2, 1, 3, 3, 2, 1, 3, 0)])
CORE = [(1, 0, 2, 2, 3, 1, 2, 2), (2, 1, 3, 3, 1, 0, 0, 3), (2, 1, 3, 3, 2, 1, 3, 0), (3, 1, 1, 0, 3, 1, 0, 0)]   # §14.5.10's four; corners 1–4 of §14.5.14
pct = lambda k: round(100 * k / n, 1)
for i, x in enumerate(CORE, 1): print('   corner %d %s in %d covers = %.1f%%' % (i, x, freq[x], 100 * freq[x] / n))
check('corner 3 (2,1,3,3,2,1,3,0) in every cover; corner 4 (11001100) in 13.7%', (freq[CORE[2]] == n, pct(freq[CORE[3]])), (True, 13.7))
check('corners 1 and 2, percent of covers (register 1820\'s 59 % and 28 %)', (pct(freq[CORE[0]]), pct(freq[CORE[1]])), (58.9, 27.8))
unit = [x for x in cells if x[0] == 3 and x[1] == 0 and x[2] == 1 and x[3] == 1 and x[5] == 0 and x[6] == 1 and x[7] == 1]
has = lambda pred: sum(1 for cv in covs if any(pred(x) for x in cv))
u = has(lambda x: x in unit); check('unit template (3,0,1,1,*,0,1,1): cells %s; percent of covers' % unit, pct(u), 10.0)
ue = {e: has(lambda x, e=e: x == (3, 0, 1, 1, e, 0, 1, 1)) for e in (1, 2, 3)}
check('unit template by its free coordinate: covers with e = 1, e = 2, e = 3 (register 604 allows 1 or 3 only)', (ue[1], ue[2], ue[3], ue[1] + ue[2] + ue[3] == u), (684, 290, 1478, True))
COND = {'s→s (l=0,f=0)': lambda x: x[1] == 0 and x[5] == 0, 's→p (l=0,f=1)': lambda x: x[1] == 0 and x[5] == 1, 'p→s (l=1,f=0)': lambda x: x[1] == 1 and x[5] == 0,
        'p→p (l=1,f=1)': lambda x: x[1] == 1 and x[5] == 1, 'null q=0': lambda x: x[3] == 0, 'full q=k': lambda x: x[3] == x[2], 'full q=k=3': lambda x: x[3] == x[2] == 3}
res = {k: pct(has(p)) for k, p in COND.items()}
for k, v in res.items(): print('   %-16s in %.1f%% of covers' % (k, v))
check('the six channel conditions of register 603 over the exact covers', [res[k] for k in ('s→s (l=0,f=0)', 's→p (l=0,f=1)', 'p→s (l=1,f=0)', 'p→p (l=1,f=1)', 'null q=0', 'full q=k')], [70.8, 100.0, 100.0, 100.0, 100.0, 100.0])
def forced(cellsX, W, carriers, M, pred):
    """some element carried only by cells satisfying pred."""
    tm = 0
    for s, c in enumerate(cellsX):
        if pred(c): tm |= 1 << s
    return any(carriers[k] & ~tm == 0 for k in range(M))
fo = {k: forced(cells, W, carriers, M, p) for k, p in COND.items()}
check('element-forced at Λ₈: s→p, p→s, p→p, null, full; s→s not', [fo[k] for k in ('s→p (l=0,f=1)', 'p→s (l=1,f=0)', 'p→p (l=1,f=1)', 'null q=0', 'full q=k', 's→s (l=0,f=0)')], [True, True, True, True, True, False])
core4 = [cv for cv in covs if all(x in cv for x in CORE)]; others = Counter(x for cv in core4 for x in cv if x not in CORE)
check('covers containing all four core cells (the 519 completions)', len(core4), 519)
check('distinct completing cells; none in all; min / median / max', (len(others), max(others.values()) < len(core4), min(others.values()), int(statistics.median(others.values())), max(others.values())), (66, True, 3, 12, 157))
print('== the cap sweep (SEED-CAP-FINDING\'s table): cells, the seed by branch and bound, element-forced conditions')
CAPS = [(2, 2, 1, 3, 1), (3, 3, 1, 3, 1), (4, 4, 1, 3, 1), (3, 3, 2, 6, 2)]
EXP = {(2, 2, 1, 3, 1): (328, 7), (3, 3, 1, 3, 1): (976, 7), (4, 4, 1, 3, 1): (1968, 7), (3, 3, 2, 6, 2): (7605, 10)}
def c3type(c, alph):   # corner 3's type: l, k, q, f, g at their maxima with q = k, 2S at its minimum; n and e free
    return c[1] == max(alph[1]) and c[2] == max(alph[2]) and c[3] == c[2] and c[5] == max(alph[5]) and c[6] == max(alph[6]) and c[7] == min(alph[7])
CONDC = dict(COND); CONDC.update({'s→d (l=0,f=2)': lambda x: x[1] == 0 and x[5] == 2, 'd→s (l=2,f=0)': lambda x: x[1] == 2 and x[5] == 0})
for cap in CAPS:
    cx = lattice(*cap); a, sl, st, el, Wx, cr = census(cx); Mx = len(el)
    exp_cells, exp_seed = EXP[cap]
    seed = None; note = ''
    if cap[2] == 1:   # the seed decided exactly: no (seed−1)-cover, a seed-cover exhibited
        fk, nk, cut = search(Wx, cr, Mx, exp_seed - 1); assert not fk and not cut
        fk, nk, cut = search(Wx, cr, Mx, exp_seed, first_only=True); assert fk; seed = exp_seed
    else:             # 7,605 cells: branch and bound does not finish in the instrument's budget; greedy set cover bounds the seed above
        FULLx = (1 << Mx) - 1; cov = 0; g = []
        while cov != FULLx:
            s_ = max(range(len(cx)), key=lambda s: (Wx[s] & ~cov).bit_count()); g.append(s_); cov |= Wx[s_]
        note = 'greedy cover of %d cells exhibited, so seed ≤ %d; the recorded %d is SEED-CAP-FINDING\'s and is not re-derived here' % (len(g), len(g), exp_seed)
    fx = {k: forced(cx, Wx, cr, Mx, p) for k, p in CONDC.items()}; fx['corner-3-type'] = forced(cx, Wx, cr, Mx, lambda c: c3type(c, a))
    print('   cap %-14s cells %5d  universe %3d  seed %s %s' % (cap, len(cx), Mx, seed, note))
    print('      element-forced: %s' % ', '.join(k for k, v in fx.items() if v))
    check('cap %s: cells, seed decided here' % (cap,), (len(cx), seed), (exp_cells, exp_seed if cap[2] == 1 else None))
    if cap[2] == 1: check('cap %s: s→p, p→s, p→p, null, full, corner-3-type forced; s→s not' % (cap,), [fx[k] for k in ('s→p (l=0,f=1)', 'p→s (l=1,f=0)', 'p→p (l=1,f=1)', 'null q=0', 'full q=k', 'corner-3-type', 's→s (l=0,f=0)')], [True] * 6 + [False])
    else: check('cap %s: s→d, d→s, null, full forced; s→p, p→s, s→s, corner-3-type not' % (cap,), [fx[k] for k in ('s→d (l=0,f=2)', 'd→s (l=2,f=0)', 'null q=0', 'full q=k', 's→p (l=0,f=1)', 'p→s (l=1,f=0)', 's→s (l=0,f=0)', 'corner-3-type')], [True] * 4 + [False] * 4)
print('\n   integrity checks: %s' % ('ALL OK' if not FAIL else 'FAILED: ' + '; '.join(FAIL)))
sys.exit(0 if not FAIL else 1)
