#!/usr/bin/env python3
# r2-ch13r.py — chat 86, computable batch for the section read of main Chapter 17
# (L4789-L4921: §17.1 E1 cells, §17.2 E2 axes, §17.3 E3 constraints, §17.4 the worked
# extension, §17.5 E is derived).  Deterministic; prints no wall-clock time.
#
# Functions owed to r2lib and carried here verbatim with provenance:
#   therm / untherm  — thermometer bit-packing, chat 85's r2-ch13p (join = OR, meet = AND).
# Everything else is computed here or imported from r2lib.

import importlib.util, os, itertools
H = os.path.dirname(os.path.abspath(__file__))
s = importlib.util.spec_from_file_location('r2lib', os.path.join(H, 'r2lib.py'))
r2lib = importlib.util.module_from_spec(s); s.loader.exec_module(r2lib)
T = r2lib.load_tower()

L8 = T.L8(); L9 = T.L9()
NAMES = ['n', 'l', 'k', 'q', 'e', 'f', 'g', '2S']
MAXV = [max(c[i] for c in L8) for i in range(8)]
MINV = [min(c[i] for c in L8) for i in range(8)]

# ---- therm / untherm : lifted verbatim from r2-ch13p.py (chat 85) ----
OFF = []; _o = 0
for m in MAXV:
    OFF.append(_o); _o += m
WIDTH = _o
def therm(c):
    v = 0
    for i, x in enumerate(c):
        if x: v |= ((1 << x) - 1) << OFF[i]
    return v
def untherm(v):
    return tuple(bin((v >> OFF[i]) & ((1 << MAXV[i]) - 1)).count('1') for i in range(8))

print('== r2-ch13r : main Chapter 17, computable batch ==')
print('L8 %d cells, L9 %d cells; thermometer width %d bits' % (len(L8), len(L9), WIDTH))

# =====================================================================================
print('\n-- 1. §17.1 L4795/L4797 : E1, which cells may be added; "100%% over 288 tests" --')
BOX = 1
for m, mn in zip(MAXV, MINV):
    BOX *= (m - mn + 1)
SET8 = set(L8); P8 = [therm(c) for c in L8]; PS8 = set(P8)
ranges = [range(MINV[i], MAXV[i] + 1) for i in range(8)]
outside = [c for c in itertools.product(*ranges) if c not in SET8]
print('ambient box %d cells; inside %d; outside %d' % (BOX, len(L8), len(outside)))
addable = []
for x in outside:
    px = therm(x); ok = True
    for py in P8:
        if (px | py) not in PS8 and (px | py) != px: ok = False; break
        if (px & py) not in PS8 and (px & py) != px: ok = False; break
    if ok: addable.append(x)
print('cells x outside L8 with L8 u {x} closed (the E1 criterion, exhaustive): %d' % len(addable))
print('  the printed test count is 288; population of E1 tests over the box is %d' % len(outside))
print('  288 == addable? %s ; 288 == outside? %s' % (len(addable) == 288, len(outside) == 288))
for x in addable[:8]:
    print('   addable:', dict(zip(NAMES, x)))

# =====================================================================================
print('\n-- 2. §17.2 L4800/L4802 : E2, Lambda x h closed iff h is a lattice homomorphism --')
# For h a function of coordinates (i, j), the (i, j) part of a join is (max, max) and of a
# meet is (min, min), so the test quantifies exactly over pairs of REALISED (i, j) values.
# Every pair of realised values is attained by some pair of cells, so this is exhaustive.
def proj(idx):
    return sorted({tuple(c[i] for i in idx) for c in L8})
def test_h(idx, fn):
    P = proj(idx); jf = mf = 0; tests = 0
    for a in P:
        for b in P:
            tests += 1
            jv = tuple(max(u, v) for u, v in zip(a, b))
            mv = tuple(min(u, v) for u, v in zip(a, b))
            if fn(jv) != max(fn(a), fn(b)): jf += 1
            if fn(mv) != min(fn(a), fn(b)): mf += 1
    return jf, mf, tests
CLASSES = {}
CLASSES['projection'] = [((i,), (lambda a: a[0]), NAMES[i]) for i in range(8)]
CLASSES['constant'] = [((0,), (lambda a, c=c: c), 'const %d' % c) for c in (0, 1, 2)]
pairs = [(i, j) for i in range(8) for j in range(i + 1, 8)]
CLASSES['maximum'] = [(p, (lambda a: max(a)), 'max(%s,%s)' % (NAMES[p[0]], NAMES[p[1]])) for p in pairs]
CLASSES['minimum'] = [(p, (lambda a: min(a)), 'min(%s,%s)' % (NAMES[p[0]], NAMES[p[1]])) for p in pairs]
CLASSES['sum'] = [(p, (lambda a: a[0] + a[1]), '%s+%s' % (NAMES[p[0]], NAMES[p[1]])) for p in pairs]
CLASSES['product'] = [(p, (lambda a: a[0] * a[1]), '%s*%s' % (NAMES[p[0]], NAMES[p[1]])) for p in pairs]
CLASSES['difference'] = [((i, j), (lambda a: a[0] - a[1]), '%s-%s' % (NAMES[i], NAMES[j]))
                         for i in range(8) for j in range(8) if i != j]
tot_tests = 0
for name in ('projection', 'constant', 'maximum', 'minimum', 'sum', 'product', 'difference'):
    good = []; bad = []
    for idx, fn, lab in CLASSES[name]:
        jf, mf, t = test_h(idx, fn); tot_tests += t
        (good if (jf == 0 and mf == 0) else bad).append((lab, jf, mf))
    print('%-11s %3d functions : %3d ARE homomorphisms on L8, %3d are not'
          % (name, len(CLASSES[name]), len(good), len(bad)))
    if name in ('maximum', 'minimum') and good:
        print('             qualify on L8 :', ', '.join(l for l, _, _ in good[:12]))
    if name in ('maximum', 'minimum') and bad:
        print('             FAIL on L8    :', ', '.join(l for l, _, _ in bad[:12]))
print('total (h, value-pair) tests run in this class sweep: %d' % tot_tests)
print('the printed figure is "100%% over 424 tests"; 424 == this total? %s' % (tot_tests == 424))

# the classification line, L4802, stated class by class
print('\n  L4802 classification line, measured class by class on L8:')
for name in ('projection', 'maximum', 'minimum', 'constant', 'sum', 'product', 'difference'):
    n_ok = sum(1 for idx, fn, lab in CLASSES[name] if test_h(idx, fn)[:2] == (0, 0))
    n = len(CLASSES[name])
    verdict = 'ALL qualify' if n_ok == n else ('NONE qualify' if n_ok == 0 else '%d of %d qualify' % (n_ok, n))
    print('    %-11s printed %-13s measured %s' % (name, 'qualify' if name in
          ('projection', 'maximum', 'minimum', 'constant') else 'do not qualify', verdict))
# the general (off-Lambda) fact, to separate "true on this object" from "true in general"
print('  in a general product of chains max/min are NOT homomorphisms; witness on a 2x2 box:')
a, b = (1, 0), (0, 1)
print('    max: h(a^b)=%d but min(h(a),h(b))=%d ; min: h(avb)=%d but max(h(a),h(b))=%d'
      % (max(min(a[0], b[0]), min(a[1], b[1])), min(max(a), max(b)),
         min(max(a[0], b[0]), max(a[1], b[1])), max(min(a), min(b))))

# =====================================================================================
print('\n-- 3. §17.2 L4809 : "seven functions including the identity and a constant; none repairs" --')
# Theorem 17.1 is CLEARED (READ-ch13p B9) and is not re-derived.  Only the witness count and
# the "none repairs" claim are measured, on a non-closed subset of L8.
import random
rnd = random.Random(17)
S = [c for c in L8 if not (c[3] == 0)]          # a non-closed subset: drop q = 0
def closed(X):
    PX = set(therm(c) for c in X)
    for u in PX:
        for v in PX:
            if (u | v) not in PX or (u & v) not in PX: return False
    return True
print('witness set S = L8 minus {q = 0}: %d cells, closed? %s' % (len(S), closed(S)))
HS = [('identity', lambda c: 0), ('constant 1', lambda c: 1)] + \
     [('projection %s' % NAMES[i], (lambda c, i=i: c[i])) for i in (0, 2, 4, 6)] + \
     [('n+k', lambda c: c[0] + c[2])]
rep = 0
for lab, h in HS:
    G = set((therm(c), h(c)) for c in S); ok = True
    for (u, hu) in G:
        for (v, hv) in G:
            if (u | v, max(hu, hv)) not in G or (u & v, min(hu, hv)) not in G: ok = False; break
        if not ok: break
    if ok: rep += 1
print('functions tested here: %d ; number that repair closure: %d' % (len(HS), rep))
print('  printed: seven functions, none repairs. count matches 7? %s ; none repairs? %s'
      % (len(HS) == 7, rep == 0))

# =====================================================================================
print('\n-- 4. §17.3 L4819-L4825 : the interval property, all pairs of L9 --')
NP = len(L9) * (len(L9) - 1) // 2
print('|L9| = %d ; C(|L9|,2) = %d ; printed "all 1,367,031 pairs" : %s'
      % (len(L9), NP, NP == 1367031))
for lab, i, j in (('delta = f - l', 5, 1), ('sigma = 2S\' - 2S', 8, 7)):
    vals = [(c[i], c[j]) for c in L9]
    bad = 0
    for p in range(len(vals)):
        ap, aq = vals[p]
        da = ap - aq
        for r in range(p + 1, len(vals)):
            bp, bq = vals[r]
            db = bp - bq
            dj = max(ap, bp) - max(aq, bq)
            dm = min(ap, bp) - min(aq, bq)
            lo, hi = (da, db) if da <= db else (db, da)
            if not (lo <= dj <= hi and lo <= dm <= hi): bad += 1
    print('  %-18s violations over all %d pairs: %d' % (lab, NP, bad))

# =====================================================================================
print('\n-- 5. §17.3 L4827-L4831 : the convexity criterion and its share of the closed sets --')
AMB = {'2x2x2': [2, 2, 2], '3x3': [3, 3], '2x2x2x2': [2, 2, 2, 2]}
PRINTED = {'2x2x2': (73, 8.2), '3x3': (146, 10.3), '2x2x2x2': (731, 0.8)}
for lab, dims in AMB.items():
    cells = list(itertools.product(*[range(d) for d in dims]))
    idx = {c: i for i, c in enumerate(cells)}
    n = len(cells)
    subs = []
    for m in range(1 << n):
        X = [cells[i] for i in range(n) if m >> i & 1]
        SX = set(X); ok = True
        for a in X:
            for b in X:
                if tuple(max(u, v) for u, v in zip(a, b)) not in SX or \
                   tuple(min(u, v) for u, v in zip(a, b)) not in SX: ok = False; break
            if not ok: break
        if ok: subs.append(frozenset(X))
    conv = set()
    for i in range(len(dims)):
        for j in range(len(dims)):
            if i == j: continue
            d = {c: c[i] - c[j] for c in cells}
            rng = sorted(set(d.values()))
            for lo in range(len(rng)):
                for hi in range(lo, len(rng)):
                    Tset = set(rng[lo:hi + 1])
                    conv.add(frozenset(c for c in cells if d[c] in Tset))
    inboth = [X for X in subs if X in conv]
    every_convex_closed = all(X in [frozenset(y) for y in subs] for X in conv)
    tot, pct = PRINTED[lab]
    print('  %-9s cells %2d : closed subsets %4d (printed %4d) ; convex preimages that are closed %3d'
          % (lab, n, len(subs), tot, len(inboth)))
    print('             share of closed subsets %.1f%% (printed %.1f%%) ; every convex preimage closed? %s'
          % (100.0 * len(inboth) / len(subs), pct, every_convex_closed))

# =====================================================================================
print('\n-- 6. §17.3 L4860-L4871 : {h <= q} closure, and "a+b <= 3 closed where a+b <= 4 is not" --')
hits3, hits4, both = 0, 0, []
for (i, j) in pairs:
    P = proj((i, j))
    for thr in (3, 4):
        ok = True
        for a in P:
            for b in P:
                if a[0] + a[1] <= thr and b[0] + b[1] <= thr:
                    if max(a[0], b[0]) + max(a[1], b[1]) > thr: ok = False; break
            if not ok: break
        if thr == 3 and ok: hits3 += 1
        if thr == 4 and ok: hits4 += 1
        if thr == 3: ok3 = ok
    if ok3 and not ok:
        both.append('%s+%s' % (NAMES[i], NAMES[j]))
print('  coordinate pairs of L8 : %d ; {a+b<=3} closed for %d of them, {a+b<=4} closed for %d'
      % (len(pairs), hits3, hits4))
print('  pairs closed at 3 and NOT closed at 4 (the printed pattern): %d %s' % (len(both), both))
# meet never breaks it
mb = 0
for (i, j) in pairs:
    P = proj((i, j))
    for a in P:
        for b in P:
            for thr in range(0, 8):
                if a[0] + a[1] <= thr and b[0] + b[1] <= thr and \
                   min(a[0], b[0]) + min(a[1], b[1]) > thr: mb += 1
print('  L4866 "meet never breaks it" : meet failures over all pairs and thresholds: %d' % mb)
# the seven constraints
CONS = [('l <= n-1', 1), ('k <= 4l+2', 1), ('q <= k', 1), ('f <= e-1', 1),
        ('g <= min(4f+2, q)', 2), ('2S <= k', 1)]
print('  L4871 : the constraints of L8 as tower-2 builds them, by how many coordinates each reads:')
for lab, nread in CONS:
    print('     %-20s reads %d coordinate%s%s' % (lab, nread, '' if nread == 1 else 's',
          ' (a minimum of two)' if nread == 2 else ''))
print('     constraints listed here: %d ; the text says seven; none is a sum: %s'
      % (len(CONS), all('+' not in lab.split('<=')[0] for lab, _ in CONS)))

# =====================================================================================
print('\n-- 7. §17.4 L4879-L4907 : the worked extension, its cell counts and its pair counts --')
def C2(n): return n * (n - 1) // 2
for figure, name in ((979300, 'L4887 "979,300 sampled pairs"'),
                     (540280, 'L4901 "all 540,280 pairs"'),
                     (1367031, 'L4824 "all 1,367,031 pairs"')):
    n = 1
    while C2(n) < figure: n += 1
    print('  %-32s = C(%d,2) exactly? %s' % (name, n, C2(n) == figure))
print('  L4901 prints 1,040 cells with 540,280 pairs : C(1040,2) = %d, agrees %s'
      % (C2(1040), C2(1040) == 540280))
print('  L4887 prints 979,300 pairs : C(1400,2) = %d, so its cell count is 1,400'
      % C2(1400))
print('  L4904 states the repair is a BIJECTION from the conserving lattice onto the repaired')
print('  one, which forces the two cell counts equal. 1,400 vs 1,040 : equal? %s' % (1400 == 1040))
print('  a sample of 979,300 pairs drawn from a 1,040-cell lattice is impossible: C(1040,2) = %d < 979,300'
      % C2(1040))

# the reading sweep: does any monotone reading of the printed construction give the counts?
def two_triple(nmax, lmax, kmax, emax, fmax, capq, canon, use2S):
    dropped = cons = 0
    for n in range(1, nmax + 1):
        for l in range(0, min(lmax, n - 1) + 1):
            for k in range(1, min(kmax, 4 * l + 2) + 1):
                for q in range(0, k + 1):
                    mult = (k + 1) if use2S else 1
                    tg = [(e, f, g) for e in range(1, emax + 1) for f in range(0, min(fmax, e - 1) + 1)
                          for g in range(0, (min(4 * f + 2, q) if capq else 4 * f + 2) + 1)]
                    d = c = 0
                    for t1 in tg:
                        for t2 in tg:
                            if canon and t1[0] > t2[0]: continue
                            d += 1
                            if t1[2] + t2[2] <= q: c += 1
                    dropped += mult * d; cons += mult * c
    return dropped, cons
readings = 0; hit_d = []; hit_c = []
for nmax in range(1, 5):
    for lmax in (1, 2):
        for kmax in (2, 3, 4):
            for emax in (2, 3, 4):
                for fmax in (1, 2, 3):
                    for capq in (True, False):
                        for canon in (True, False):
                            for use2S in (True, False):
                                readings += 1
                                d, c = two_triple(nmax, lmax, kmax, emax, fmax, capq, canon, use2S)
                                if d == 45690: hit_d.append((nmax, lmax, kmax, emax, fmax, capq, canon, use2S))
                                if c in (1040, 1400): hit_c.append((c, nmax, lmax, kmax, emax, fmax, capq, canon, use2S))
print('  reading sweep of the construction as printed (two triples, e1<=e2 canonical,')
print('  g1+g2<=q conservation, L8 constraints per triple): %d readings swept' % readings)
print('    readings giving 45,690 cells with conservation dropped : %d' % len(hit_d))
print('    readings giving 1,040 or 1,400 cells with conservation : %d' % len(hit_c))
d0, c0 = two_triple(3, 1, 3, 3, 1, True, True, True)
print('    at L8\'s own caps (3,1,3,3,1) the construction gives %d cells without conservation'
      % d0)
print('    and %d with it; printed are 45,690 and (implied) 1,400 / (printed) 1,040' % c0)

# the counterexample of L4889, and the order cost of L4906
a = (1, 0); b = (0, 1); q = 1
print('  L4889 counterexample a=(g1=1,g2=0,q=1), b=(g1=0,g2=1,q=1): both conserve (1<=1, 1<=1);')
print('    their join is (g1=%d, g2=%d) with g1+g2 = %d > q = %d : %s'
      % (max(a[0], b[0]), max(a[1], b[1]), max(a[0], b[0]) + max(a[1], b[1]), q,
         'transfers two having removed one' if max(a[0], b[0]) + max(a[1], b[1]) == 2 else 'DOES NOT'))
for qq in (2, 3, 4):
    cells = [(g1, g2) for g1 in range(qq + 1) for g2 in range(qq + 1) if g1 + g2 <= qq]
    old = sum(1 for x in cells for y in cells if x != y and x[0] <= y[0] and x[1] <= y[1])
    new = sum(1 for x in cells for y in cells if x != y and x[0] <= y[0] and x[0] + x[1] <= y[0] + y[1])
    print('  L4906 at q = %d : %2d cells, ordered pairs old %2d, new %2d, new-and-not-old %2d'
          % (qq, len(cells), old, new, new - old))
print('  printed: "Fifteen of forty ordered pairs are new"')

print('\n== end r2-ch13r ==')
