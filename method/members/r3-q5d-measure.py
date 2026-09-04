#!/usr/bin/env python3
# r3-q5d-measure.py — R3 (Q5 pass 4): the chat-57 batch 2b slip B2-C2 re-derived with the standard library. Chat 57's own
# instruments (mc10.py, mc10b.py, mc10c.py, mc10d.py; extracted from chat57-instruments.tar.gz) need numpy, and M ruled
# (RUL-153, passes 3–5) that the re-run is a standard-library instrument of R3's. This one follows their definitions
# exactly — the same seven constraints on the box [x∧y, x∨y] of every unordered pair, the same tree order for the chain
# rule, the same strata, the same cap settings and the same sampling (random.seed(11), randrange, 400,000 pairs where the
# pair count exceeds 600,000) — so that each figure is comparable to the pack's output, which is also recorded (W-227).
# Λ₈ is taken from the seated tower-2.py, imported by path; the cap-parameterised lattice below is tower-2's loop with
# caps in place of its constants. Deterministic; no wall clock.
import os, sys, importlib.util, io, contextlib, random
from itertools import combinations
H = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location('tower2', os.path.join(H, 'tower-2.py')); T2 = importlib.util.module_from_spec(spec)
with contextlib.redirect_stdout(io.StringIO()): spec.loader.exec_module(T2)
FAIL = []
def check(tag, got, exp):
    ok = got == exp; print('   %-66s %-26s %s' % (tag, repr(got)[:26], 'OK' if ok else 'EXPECTED ' + repr(exp)))
    if not ok: FAIL.append(tag)
def build(capn, cape, capl, capk, capf):
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
# coordinate order: 0 n, 1 l, 2 k, 3 q, 4 e, 5 f, 6 g, 7 2S; the seven constraints as hi_i <= phi(lo_j)
CONS = [('l<=n-1', lambda lo, hi: hi[1] <= lo[0] - 1), ('k<=2(2l+1)', lambda lo, hi: hi[2] <= 4 * lo[1] + 2),
        ('q<=k', lambda lo, hi: hi[3] <= lo[2]), ('g<=q', lambda lo, hi: hi[6] <= lo[3]),
        ('g<=2(2f+1)', lambda lo, hi: hi[6] <= 4 * lo[5] + 2), ('f<=e-1', lambda lo, hi: hi[5] <= lo[4] - 1),
        ('2S<=k', lambda lo, hi: hi[7] <= lo[2])]
NAMES = [n for n, _ in CONS]
cells = T2.L8(); check('|Λ₈| from tower-2.py', len(cells), 976); check('tower-2.py\'s Λ₈ is build(3,3,1,3,1)', build(3, 3, 1, 3, 1) == cells, True)

print('== the base-cap pairs: rates, product, joint, factor (mc10.py)')
rows = []; LO = []; HI = []
for a, b in combinations(cells, 2):
    lo = tuple(min(u, v) for u, v in zip(a, b)); hi = tuple(max(u, v) for u, v in zip(a, b))
    rows.append(tuple(1 if f(lo, hi) else 0 for _, f in CONS)); LO.append(lo); HI.append(hi)
N = len(rows); check('unordered pairs', N, 475800)
p = [sum(r[i] for r in rows) / N for i in range(7)]
for nm, v in zip(NAMES, p): print('   %-14s %6.2f%%' % (nm, v * 100))
check('individual range, two decimals', (round(min(p) * 100, 2), round(max(p) * 100, 2)), (69.95, 98.06))
prod = 1.0
for v in p: prod *= v
joint = sum(1 for r in rows if all(r)) / N
check('product, four decimals (%)', round(prod * 100, 4), 20.1311); check('joint, four decimals (%)', round(joint * 100, 4), 28.3462)
check('factor joint/product', round(joint / prod, 4), 1.4081)

print('== the chain rule in tree order (mc10b.py)')
order = [0, 1, 2, 6, 3, 4, 5]; mask = [True] * N; lifts = []; raw_lifts = []
for i in order:
    sel = [r for r, m in zip(rows, mask) if m]; cond = sum(r[i] for r in sel) / len(sel); lift = cond / p[i]; lifts.append(round(lift, 4)); raw_lifts.append(lift)
    print('   P(%-11s| previous) = %.4f   marginal %.4f   lift %.4f' % (NAMES[i], cond, p[i], lift))
    mask = [m and bool(r[i]) for r, m in zip(rows, mask)]
check('the six edge lifts in tree order', lifts[1:], [1.0838, 1.0854, 1.1212, 1.0522, 1.0125, 1.0022])
pl = 1.0
for x in raw_lifts: pl *= x   # unrounded, as mc10b.py multiplies them
check('product of the lifts = the factor', round(pl, 4), 1.4081)

print('== conditional independence given the shared coordinate\'s interval (mc10d.py test 1)')
def lift_on(a, b, sel):
    n = len(sel); pa = sum(rows[t][a] for t in sel) / n; pb = sum(rows[t][b] for t in sel) / n; pab = sum(rows[t][a] & rows[t][b] for t in sel) / n
    return pab / (pa * pb) if pa * pb > 0 else float('nan')
ALL = list(range(N))
tests = [('q<=k', 'g<=q', 3, 'q'), ('k<=2(2l+1)', 'q<=k', 2, 'k'), ('q<=k', '2S<=k', 2, 'k'), ('l<=n-1', 'k<=2(2l+1)', 1, 'l'), ('g<=q', 'g<=2(2f+1)', 6, 'g')]
means = []
for a, b, ci, cn in tests:
    ia, ib = NAMES.index(a), NAMES.index(b); raw = lift_on(ia, ib, ALL); ls = []; ws = []
    for v_lo in range(4):
        for v_hi in range(4):
            sel = [t for t in ALL if LO[t][ci] == v_lo and HI[t][ci] == v_hi]
            if len(sel) < 500: continue
            l = lift_on(ia, ib, sel)
            if l == l: ls.append(l); ws.append(len(sel))
    avg = sum(l * w for l, w in zip(ls, ws)) / sum(ws); means.append(round(avg, 4))
    print('   %-11s & %-11s share %s: raw lift %.4f -> mean lift given (%slo,%shi) %.4f  (strata %d)' % (a, b, cn, raw, cn, cn, avg, len(ls)))
check('conditional lift 1.0000 in every shared pair', means, [1.0] * 5)
print('== non-adjacent pairs (test 2)')
na = []
for a, b in [('l<=n-1', 'g<=q'), ('l<=n-1', 'f<=e-1'), ('f<=e-1', '2S<=k'), ('l<=n-1', '2S<=k'), ('k<=2(2l+1)', 'f<=e-1')]:
    l = round(lift_on(NAMES.index(a), NAMES.index(b), ALL), 4); na.append(l); print('   %-11s & %-11s: lift %.4f' % (a, b, l))
check('non-adjacent lifts', na, [1.0022, 0.9999, 1.0, 1.0101, 1.0001])
print('== the narrowness mechanism (test 3)')
nar = {}
for nm, ci in [('q<=k', 2), ('g<=q', 3), ('2S<=k', 2)]:
    i = NAMES.index(nm); vals = []
    for w in range(4):
        sel = [t for t in ALL if HI[t][ci] - LO[t][ci] == w]
        if len(sel) > 200: vals.append(round(sum(rows[t][i] for t in sel) / len(sel), 3))
    nar[nm] = vals; print('   P(%-11s) by width of coord %d: %s' % (nm, ci, ' '.join('w=%d:%.3f' % (w, v) for w, v in enumerate(vals))))
check('q<=k by width', nar['q<=k'], [1.0, 0.599, 0.319]); check('g<=q by width', nar['g<=q'], [1.0, 0.672, 0.446, 0.294]); check('2S<=k by width', nar['2S<=k'], [1.0, 0.726, 0.5])

print('== the factor across cap settings (mc10c.py: exhaustive to 600,000 pairs, else 400,000 sampled, random.seed(11))')
random.seed(11)
def stats(cs, nsamp=400000):
    n_ = len(cs); tot = n_ * (n_ - 1) // 2
    it = combinations(cs, 2) if tot <= 600000 else ((cs[random.randrange(n_)], cs[random.randrange(n_)]) for _ in range(nsamp))
    cnt = [0] * 7; joint_ = 0; m = 0
    for a, b in it:
        lo = tuple(min(u, v) for u, v in zip(a, b)); hi = tuple(max(u, v) for u, v in zip(a, b)); ok = True; m += 1
        for i, (_, f) in enumerate(CONS):
            if f(lo, hi): cnt[i] += 1
            else: ok = False
        if ok: joint_ += 1
    pp = [c / m for c in cnt]; pr = 1.0
    for v in pp: pr *= v
    return n_, tot, min(pp), max(pp), pr, joint_ / m, (joint_ / m) / pr
caps = [(3, 3, 1, 3, 1), (4, 4, 1, 3, 1), (4, 4, 2, 5, 1), (5, 5, 2, 6, 1), (5, 5, 2, 8, 2), (6, 6, 3, 10, 2), (7, 7, 3, 14, 3)]
print('   %-22s%7s%12s%7s%7s%8s%8s%8s' % ('caps', 'cells', 'pairs', 'min%', 'max%', 'prod%', 'joint%', 'factor'))
factors = []; ncells = []
for c in caps:
    cs = build(*c); n_, tot, mn, mx, pr, j, f = stats(cs); factors.append(round(f, 3)); ncells.append(n_)
    print('   %-22s%7d%12d%7.1f%7.1f%8.2f%8.2f%8.3f' % (str(c), n_, tot, mn * 100, mx * 100, pr * 100, j * 100, f))
check('cells at the seven settings', ncells, [976, 1968, 8847, 25748, 55682, 234340, 800958])
check('the factor at the seven settings, three decimals', factors, [1.408, 1.372, 1.366, 1.326, 1.526, 1.456, 1.66])
check('the factor is cap-dependent: its range beyond the base', (min(factors[1:]), max(factors[1:])), (1.326, 1.66))
print('\n   integrity checks: %s' % ('ALL OK' if not FAIL else 'FAILED: ' + '; '.join(FAIL)))
sys.exit(1 if FAIL else 0)
