#!/usr/bin/env python3
# r2-ch13c.py — Phase R2, chat 79, segment 2: main §12.11.6 (L3482-3493) and §12.11.7 (L3494-3507).
# (1) The E1 selection index on (2J, 2J'), |D2J| <= 2: closed under join and meet at every cap tested;
#     with the forbidden cell (0,0) removed, the failing meets, their value, and E = |R(X)| - |X|.
# (2) The parity half as a congruence: whether it breaks joins.
# (3) §12.11.7 L3497-3498: the earlier bound 2J_c <= k against the physical region, per term and per
#     occupancy, and whether the failures number four beginning with p^1.
# No wall-clock output.
import itertools
from collections import Counter

CAPS = (4, 6, 8, 10, 12, 20)

def E1(N):
    return {(a, b) for a in range(N + 1) for b in range(N + 1) if abs(a - b) <= 2}

def R(X):
    """The book's envelope on a two-coordinate index: close under pairwise join and meet to a fixed
    point.  E(X) = |R(X)| - |X| (§31.3.4's join failures and meet failures)."""
    S = set(X)
    while True:
        add = set()
        for x, y in itertools.combinations(S, 2):
            j = (max(x[0], y[0]), max(x[1], y[1])); m = (min(x[0], y[0]), min(x[1], y[1]))
            if j not in S: add.add(j)
            if m not in S: add.add(m)
        if not add: return S
        S |= add

def failing(X, op):
    """Unordered pairs of distinct cells whose join (op='j') or meet (op='m') leaves X, with values."""
    out = Counter(); pairs = []
    for x, y in itertools.combinations(sorted(X), 2):
        z = (max(x[0], y[0]), max(x[1], y[1])) if op == 'j' else (min(x[0], y[0]), min(x[1], y[1]))
        if z not in X: out[z] += 1; pairs.append((x, y, z))
    return out, pairs

print('=== §12.11.6 L3483-3486: the E1 index on (2J, 2J\'), |D2J| <= 2 ===')
print('cap N | cells | join fails | meet fails | E(X) || (0,0) removed: cells | join fails | meet fails | E | meet values')
for N in CAPS:
    X = E1(N); jf, _ = failing(X, 'j'); mf, _ = failing(X, 'm')
    Y = X - {(0, 0)}; jf2, _ = failing(Y, 'j'); mf2, pm = failing(Y, 'm')
    print('%5d | %5d | %10d | %10d | %4d || %5d | %10d | %10d | %2d | %s' % (
        N, len(X), sum(jf.values()), sum(mf.values()), len(R(X)) - len(X),
        len(Y), sum(jf2.values()), sum(mf2.values()), len(R(Y)) - len(Y), dict(mf2)))

print()
print('the four failing meets at cap 6, in full:')
Y6 = E1(6) - {(0, 0)}
for x, y, z in failing(Y6, 'm')[1]:
    print('   %s ^ %s = %s' % (x, y, z))

print()
print('=== §12.11.6 L3487: the parity half as a congruence (2J + 2J\' odd) on the same index ===')
print('cap N | cells | join fails | meet fails | E(X)')
for N in CAPS:
    Z = {c for c in E1(N) if (c[0] + c[1]) % 2 == 1}
    jf, _ = failing(Z, 'j'); mf, _ = failing(Z, 'm')
    print('%5d | %5d | %10d | %10d | %4d' % (N, len(Z), sum(jf.values()), sum(mf.values()), len(R(Z)) - len(Z)))

# ---- lifted verbatim from r2-ch12q.py (chat 76), provenance per DEFERRED; owed to r2lib ----
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
# ---- end lift ----

SYM = {0: 'S', 2: 'P', 4: 'D', 6: 'F'}
CONF = [(0, 1), (0, 2), (1, 1), (1, 2), (1, 3)]   # the configurations at the caps of §7.4

print()
print('=== §12.11.7 L3497-3498: the earlier bound 2J_c <= k against the physical region ===')
fails = []
for l, k in CONF:
    for (S2, L2), _ in sorted(terms(l, k).items(), key=lambda t: (-t[0][1], -t[0][0])):
        j2 = L2 + S2                      # largest 2J the term carries
        tag = '%s^%d %d%s' % ('spdf'[l], k, S2 + 1, SYM[L2])
        if j2 > k: fails.append((tag, j2, k))
print('per term (configuration, term, largest 2J, k) failing 2J <= k:', len(fails))
for t, j2, k in fails: print('   %-10s 2J = %d > %d' % (t, j2, k))
print('per occupancy k, largest physical 2J_c over all l at the caps (§12.11.0.6\'s table):')
for k in (1, 2, 3):
    m = max(L2 + S2 for l, kk in CONF if kk == k for (S2, L2) in terms(l, kk))
    print('   k = %d  largest physical 2J_c = %d  2J_c <= k admits %d  fails: %s' % (k, m, k, m > k))
print('per configuration failing:', [t for l, k in CONF for t in ['%s^%d' % ('spdf'[l], k)]
                                     if max(L2 + S2 for (S2, L2) in terms(l, k)) > k])
