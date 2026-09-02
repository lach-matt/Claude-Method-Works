# r2-ch6.py — Phase R2, main Chapter 6 (chat 69). Re-measures every E(X) the chapter prints under the chapter's
# own definition of ℛ (§6.1, L1535–1540: value sets Â_i and one-sided upper bounds φ̂_ij) and, for comparison,
# under the two-sided bound closure of r2-ch1.py. Every line printed is MEASURED; inputs the book does not
# print are marked INFERRED where they are built. The read decides.
import itertools, importlib.util, re, sys
TOWER = sys.argv[1] if len(sys.argv) > 1 else '../members94/tower-2.py'
MAIN = sys.argv[2] if len(sys.argv) > 2 else '../members94/The_Method_1_6-2.md'
def R1(X):   # §6.1: ℛ(X) = { x ∈ ∏ Â_i : x_i ≤ φ̂_ij(x_j) ∀ i≠j }, φ̂_ij(v) = max{ x_i : x ∈ X, x_j ≤ v }
    X = set(X); d = len(next(iter(X))); A = [sorted({x[i] for x in X}) for i in range(d)]
    phi = {(i, j, v): max(x[i] for x in X if x[j] <= v) for i in range(d) for j in range(d) if i != j for v in A[j]}
    return {x for x in itertools.product(*A) if all(x[i] <= phi[(i, j, x[j])] for i in range(d) for j in range(d) if i != j)}
def R2(X):   # r2-ch1/r2-ch3: lower and upper bounds on the box
    X = set(X); d = len(next(iter(X))); lo = [min(x[i] for x in X) for i in range(d)]; hi = [max(x[i] for x in X) for i in range(d)]
    F = {}; G = {}
    for i in range(d):
        for j in range(d):
            if i == j: continue
            for v in range(lo[j], hi[j] + 1):
                le = [x[i] for x in X if x[j] <= v]; ge = [x[i] for x in X if x[j] >= v]
                F[(i, j, v)] = max(le) if le else -1; G[(i, j, v)] = min(ge) if ge else 10 ** 6
    return {x for x in itertools.product(*[range(lo[i], hi[i] + 1) for i in range(d)])
            if all(G[(i, j, x[j])] <= x[i] <= F[(i, j, x[j])] for i in range(d) for j in range(d) if i != j)}
def E(X, R=R1): return len(R(X)) - len(X)
def show(tag, X, printed):
    print('%-46s |X|=%4d  §6.1 ℛ: admits %4d E=%3d | two-sided E=%3d   (printed: %s)' % (tag, len(X), len(R1(X)), E(X), E(X, R2), printed))
# ---- periodic tables ------------------------------------------------------------------------------------
def table18(he_group=18):
    X = {(1, 1), (1, he_group)}
    for p in (2, 3): X |= {(p, g) for g in (1, 2, 13, 14, 15, 16, 17, 18)}
    for p in (4, 5, 6, 7): X |= {(p, g) for g in range(1, 19)}      # La, Ac in group 3; 14+14 f-block set aside
    return X
X18 = table18(); print('18-column, He at 18: admitted-and-absent =', sorted(R1(X18) - X18) == sorted({(1, g) for g in range(2, 18)} | {(2, g) for g in range(3, 13)} | {(3, g) for g in range(3, 13)}), '(L1523)')
show('18-column, f-block detached, He at 18', X18, '90 / 126 / 36 (L1519–1521, L1583)')
show('18-column, He at group 2', table18(2), '90 / 20 (L1572)')
X32 = {(1, 1), (1, 32)} | {(p, g) for p in (2, 3) for g in (1, 2, 27, 28, 29, 30, 31, 32)} | {(p, g) for p in (4, 5) for g in list(range(1, 3)) + list(range(17, 33))} | {(p, g) for p in (6, 7) for g in range(1, 33)}
show('32-column', X32, '118 / 106 (L1584)')
# Janet left-step: row = n+ℓ (1..8); widths 2,2,8,8,18,18,32,32; blocks f,d,p,s left to right.
widths = [2, 2, 8, 8, 18, 18, 32, 32]
janet_from_left = {(r + 1, c) for r, w in enumerate(widths) for c in range(33 - w, 33)}   # column 1 = leftmost f
janet_from_s = {(r + 1, 33 - c) for (r, c) in [(r, c) for r, w in enumerate(widths) for c in range(33 - w, 33)]}  # column 1 = s end
show('Janet left-step, column counted from the f end', janet_from_left, '120 / 0 (L1585)')
show('Janet left-step, column counted from the s end', janet_from_s, '120 / 0 (L1585)')
# ---- §6.2's other indices ----------------------------------------------------------------------------------------
box = {(l, w, h) for l in range(1, 7) for w in range(1, l + 1) for h in range(1, w + 1)}
show('a box ordering l ≥ w ≥ h, sides 1..6', box, '56 / 0 (L1599)')
show('a chessboard 8 × 8', {(r, c) for r in range(1, 9) for c in range(1, 9)}, '64 / 0 (L1603)')
spec = importlib.util.spec_from_file_location('tower', TOWER); tw = importlib.util.module_from_spec(spec); spec.loader.exec_module(tw)
L8 = set(tw.L8()); show('Λ8', L8, '976 / 0 (L1607)')
days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
cal = {(m + 1, dd) for m in range(12) for dd in range(1, days[m] + 1)}
show('the calendar (month, day)', cal, '365 / 7 (L1611)')
print('   the seven:', sorted(R1(cal) - cal), '(L1677)')
order = [2, 4, 6, 9, 11, 1, 3, 5, 7, 8, 10, 12]    # §6.3 relabelling by length
cal2 = {(order.index(m) + 1, dd) for (m, dd) in cal}
show('the calendar relabelled by length (§6.3)', cal2, '365 / 0 (L1708)')
feb_first = [2, 1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
show('the calendar with February first only', {(feb_first.index(m) + 1, dd) for (m, dd) in cal}, 'not printed')
# ---- the audit index under §6.1's ℛ ------------------------------------------------------------------------------
lines = open(MAIN, encoding='utf-8').read().split('\n')
READS = ['object', 'source', 'artefact', 'outside']; COMP = ['itself', 'other places', 'a computation']
COST = ['wrong', 'unreadable', 'unusable', 'dishonest']; PRES = ['nothing', 'claims individually true', 'also mutually consistent']
cells = []
for ln in lines[1116:1138]:
    m = re.match(r'\s*(\d+)\s+([A-Z]+)\s+(object|source|artefact|outside)\s+(itself|other places|a computation)\s+(wrong|unreadable|unusable|dishonest)\s+(.+?)\s*$', ln)
    p = 'claims individually true' if m.group(6) == 'labels are addressable' else m.group(6)
    cells.append((READS.index(m.group(3)), COMP.index(m.group(4)), COST.index(m.group(5)), PRES.index(p)))
print('audit index (§2.21 table) — E(audits) under §6.1 ℛ / two-sided; printed 11, 0, 19, 18, 17, 16:')
for n, coords in [(7, 3), (18, 3), (18, 4), (19, 4), (20, 4), (21, 4), (22, 4)]:
    X = {c[:coords] for c in cells[:n]}
    print('   first %2d at %d coords: §6.1 E=%2d  two-sided E=%2d' % (n, coords, E(X), E(X, R2)))
# ---- the measured nuclide chart (INFERRED input: the book prints only the nine absent cells) -----------------------
bound = {1: [0, 1, 2], 2: [1, 2, 4, 6], 3: [3, 4, 5, 6, 8], 4: [3, 5, 6, 7, 8, 10], 5: [3, 5, 6, 7, 8, 9, 10, 12, 14],
         6: list(range(3, 15)) + [16], 7: list(range(5, 17)), 8: list(range(5, 17)), 9: list(range(8, 19)) + [20, 22]}
names = {1: 'H', 2: 'He', 3: 'Li', 4: 'Be', 5: 'B', 6: 'C', 7: 'N', 8: 'O', 9: 'F'}
print('measured nuclides (Z, N), particle-bound, reconstructed from standard data — INFERRED input; printed rows L1691–1694:')
for zmax, printed in [(5, '27 / 33 / 6'), (6, '40 / 48 / 8'), (7, '52 / 61 / 9'), (9, '80 / 89 / 9')]:
    X = {(z, n) for z in range(1, zmax + 1) for n in bound[z]}
    absent = sorted(R1(X) - X)
    print('   Z ≤ %d: nuclides %2d admitted %2d E=%d  %s   (printed %s)' % (zmax, len(X), len(R1(X)), E(X), ', '.join('%s-%d' % (names[z], z + n) for z, n in absent), printed))
# ---- ionization energies (L1643–1644): monotonicity refusals ---------------------------------------------------------------
ie = {2: [5.392, 9.323, 8.298, 11.260, 14.534, 13.618, 17.423, 21.565], 3: [5.139, 7.646, 5.986, 8.152, 10.487, 10.360, 12.968, 15.760]}
ref = [(p, i + 1) for p in ie for i in range(7) if ie[p][i + 1] < ie[p][i]]
print('ionization energies: refused steps (period, position):', ref, '; interior cells 2×6 =', 12, '; admissible', 12 - len(ref), '/ 12 = %.0f%%' % (100 * (12 - len(ref)) / 12), '(L1646–1649 "four steps refused, 67% admissible")')
