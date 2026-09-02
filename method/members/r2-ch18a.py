#!/usr/bin/env python3
# r2-ch18a.py — chat 131 — R2 computable batch for main L9939–L10053 (Appendix A part 1: the opener and A.3, A.8, A.9,
# A.10, A.11, A.12, A.13; split at the `### A.15` boundary), BUILD90. Reads MEMBERS only; imports r2lib by path and the
# tower through r2lib.load_tower(). Appendix A is PRE-PP: headings and Statement lines are diffed against the Prints &
# Proofs original (PP_The_Method_1_6.md at /home/claude, fetched at the gate; its `# APPENDICES` body found by scan).
# Every proved statement is re-derived on the rebuilt Λ₈ or its budget is stated. Conventions named before verdicts;
# Decimal, never round(); a count word counts DATA rows; a literal string is not a test; every negative carries its
# witness; passes recorded; the instrument is wrong before the book.
import os, re, io, sys, importlib.util, contextlib, itertools, random
from decimal import Decimal as D, ROUND_HALF_UP
import numpy as np
H = os.path.dirname(os.path.abspath(__file__))
def load(name, quiet=False):
    spec = importlib.util.spec_from_file_location(name.replace('-', '_'), os.path.join(H, name + '.py')); mod = importlib.util.module_from_spec(spec)
    if quiet:
        with contextlib.redirect_stdout(io.StringIO()): spec.loader.exec_module(mod)
    else: spec.loader.exec_module(mod)
    return mod
L = load('r2lib'); heading_line, section_span, has_token = L.heading_line, L.section_span, L.has_token
with contextlib.redirect_stdout(io.StringIO()): T = L.load_tower()
def rd(n): return open(os.path.join(H, n), encoding='utf-8').read().split('\n')
M = rd('The_Method_1_6-2.md'); R = rd('The_Method_1_6___The_Register-2.md')
PPP = '/home/claude/PP_The_Method_1_6.md'
PP = open(PPP, encoding='utf-8').read().split('\n') if os.path.exists(PPP) else None
VOL = {'main': M, 'reg': R, 'mc': rd('The_Method_1_6___Mathematical_Compendium-2.md'), 'pc': rd('The_Method_1_6___The_Physics_Compendium-2.md'),
       'ioi': rd('The_Method_1_6___The_Index_of_Indices-2.md'), 'sc': rd('The_Method_1_6___Spectra_Compendium-2.md')}
def hr(t): print('\n' + '=' * 96 + '\n' + t + '\n' + '=' * 96)
def body_range(M, sec):   # copied verbatim from r2-ch17e.py (there from r2-ch17c.py / r2-ch17a.py / r2-ch16z.py; owed to r2lib, DEFERRED): heading to next heading of any rank, body occurrence
    s = heading_line(M, sec)
    for i in range(s + 1, len(M) + 1):
        if re.match(r'^#{1,4} ', M[i - 1]): return (s, i)
    return (s, len(M) + 1)
def rbody(n):   # copied verbatim from r2-ch17e.py (there from r2-ch17c.py / r2-ch17b.py; owed to r2lib, DEFERRED): first non-blank line after '### n'
    i = next((i for i, l in enumerate(R) if l.strip() == '### %d' % n), None)
    return None if i is None else next(l for l in R[i + 1:] if l.strip())
def lettered(M, tag):   # copied verbatim from r2-ch17e.py (there from r2-ch17c.py; owed to r2lib, DEFERRED): lettered heading, exact token, hits in order; body = LAST
    hits = [i for i, l in enumerate(M, 1) if re.match(r'^#{2,4}\s*' + re.escape(tag) + r'(?!\.\d)(?!\d)\b', l)]
    return hits
def q(x, places): return str(D(str(x)).quantize(D(places), rounding=ROUND_HALF_UP))
norm = lambda s: re.sub(r'\s+', ' ', s.strip())
def sites(pat, vols=VOL, flags=0): return {v: [i + 1 for i, l in enumerate(t) if re.search(pat, l, flags)] for v, t in vols.items()}
def text(a, b): return '\n'.join(M[a - 1:b - 1])
def span_text(sec):
    a, b = section_span(M, sec); return text(a, b)

hr('§0 BOUNDARY — own heading scan; the unit is Appendix A from its body heading to the `### A.15` heading (split at an A.n boundary)')
appA = [i for i, l in enumerate(M, 1) if re.match(r'^## Appendix A ', l)]; appB = [i for i, l in enumerate(M, 1) if re.match(r'^## Appendix B ', l)]
apx = [i for i, l in enumerate(M, 1) if re.match(r'^# APPENDICES\s*$', l)]
print('  `# APPENDICES`', apx, '; `## Appendix A` (contents, body)', appA, '; `## Appendix B`', appB, '; body = last hit')
An = [(i, l) for i, l in enumerate(M, 1) if i > appA[-1] and i < appB[-1] and re.match(r'^#{2,4}\s*A\.\d', l)]
print('  `### A.n` headings inside Appendix A (%d):' % len(An), [(i, l.split()[1]) for i, l in An])
a15 = [i for i, l in An if l.split()[1] == 'A.15'][0]
unit = (appA[-1], a15); print('  unit:', unit[0], 'to', unit[1] - 1, '=', unit[1] - unit[0], 'lines; whole Appendix A =', appB[-1] - appA[-1], 'lines (part 2 opens at L%d)' % a15)
print('  lettered(M, "A.13") =', lettered(M, 'A.13'), '; lettered(M, "A.1") =', lettered(M, 'A.1'), '(exact token: A.1 does not match A.10–A.19; a heading for A.1 does not exist — its row is in the table)')
U = text(*unit); UL = M[unit[0] - 1:unit[1] - 1]
def uline(pat): return [unit[0] + i for i, l in enumerate(UL) if re.search(pat, l)]

hr('§1 THE OPENER — "Nine proofs … cross-referenced here. The remaining ten … nineteen in all" (convention: a count word counts DATA rows; a section count counts `### A.n` headings with a one-dot number)')
tab = [l for l in UL if re.match(r'^\s+A\.\d+\s', l)]; print('  table DATA rows (lines starting with an A.n label):', len(tab), [l.split()[0] for l in tab])
secs = [x.split()[1] for _, x in An]; top = [s for s in secs if s.count('.') == 1]; sub = [s for s in secs if s.count('.') == 2]
print('  `### A.n` one-dot sections in Appendix A:', len(top), top, '; two-dot sub-sections:', sub)
print('  9 + 10 = 19:', len(tab) + len(top) == 19, '; "nine … cross-referenced" =', len(tab) == 9, '; "remaining ten" =', len(top) == 10, '; the union of table labels and section labels is exactly A.1–A.19 with no overlap:', sorted(set(int(l.split()[0][2:]) for l in tab) | set(int(s[2:]) for s in top)) == list(range(1, 20)), set(l.split()[0] for l in tab) & set(top) == set())
print('  the nine table rows are exactly the statements with no `### A.n` section (C1 of READ-ch13n re-measured):', set(l.split()[0] for l in tab) == set('A.%d' % n for n in range(1, 20)) - set(top))

hr('§2 THE NINE "IN FULL" POINTERS — each resolved to the CLAIM under section_span (exact-token heading resolver), not to the heading; witness printed')
ptr = {'A.1': ('7.3', r'closed'), 'A.2': ('14.1', r'ℛ\(X\)\s*=\s*X|X\s*=\s*ℛ\(X\)'), 'A.4': ('16.1', r'dim\s*q\s*[−-]\s*dim\s*p|ⅅ'), 'A.5': ('16.5', r'χ_Λ|χ'), 'A.6': ('24.2', r'adjunction|adjoin|repair|closure'),
       'A.7': ('16.3', r'may precede'), 'A.14': ('12.11.2', r'monotone[- ]envelope|envelope'), 'A.16': ('12.11.2', r'triangle|exact coupling'), 'A.17': ('12.11.3', r'dichotomy')}
for a, (sec, pat) in ptr.items():
    sp = section_span(M, sec); tx = text(*sp); n = len(re.findall(pat, tx, re.I))
    print(f'  {a} → §{sec} span L{sp[0]}–L{sp[1]-1} ({sp[1]-sp[0]} lines): /{pat}/ hits {n}', '' if n else ' — ZERO: the target says nothing of the claim')
print('  A.6 "adjunction never repairs closure" — where the claim lives: main lines with adjunction/adjoin and their sections:', [(i, L.enclosing(M, i)) for i, l in enumerate(M, 1) if re.search(r'adjunction|adjoin', l, re.I) and i < 9939], '; L4806:', norm(M[4805])[:90], '; Appendix D L10558 names Theorem 17.1 as A.6:', 'Theorem 17.1 is A.6' in M[10557], '— the index row sends A.6 to §24.2, a table of contributors (docket 9a, wrong target)')
sp153 = section_span(M, '15.3'); print('  13l-03 re-measured: "may precede" in §15.3 span L%d–L%d: %d; in §16.3: %d; §15.3 heading: %s' % (sp153[0], sp153[1] - 1, len(re.findall('may precede', text(*sp153), re.I)), len(re.findall('may precede', span_text('16.3'), re.I)), M[sp153[0] - 1].strip()[:70]))
print('  A.17 "forced by A.16": §12.11.3 lines naming the triangle or A.16:', [i for i in range(*section_span(M, '12.11.3')) if re.search(r'triangle|A\.16', M[i - 1])])
sp184 = section_span(M, '18.4'); print('  A.3 Remark "§18.4 exhibits a counterexample" — §18.4 span L%d–L%d: /counterexample|projection|converse/ lines:' % (sp184[0], sp184[1] - 1), [i for i in range(*sp184) if re.search(r'counterexample|projection|converse', M[i - 1], re.I)][:8])
print('  A.12 Consequence "antiprotonic-helium cells of §25.6" — §25.6 span', section_span(M, '25.6'), 'lines with antiprotonic:', [i for i in range(*section_span(M, '25.6')) if 'antiprotonic' in M[i - 1]], '— ZERO; the cells\' homes (every main site with its enclosing section):', [(i, L.enclosing(M, i)) for i, l in enumerate(M, 1) if 'antiprotonic' in l], '; the twin sentence L6135 (§22.3) makes the same §25.6 pointer — 14h-05 carries it; the A.12 site is its second member (docket 9a)')
print('  A.11 "the bracket of Part V operates along chains" — Part V heading:', [(i, M[i - 1].strip()[:60]) for i, l in enumerate(M, 1) if re.match(r'^# PART V\b', l)], '; A.9 Rota 1964 in the References body:', [(i, M[i - 1][:70]) for i, l in enumerate(M, 1) if i > 11500 and re.search(r'Rota, G', l)], '; "crosscut" in References:', [i for i, l in enumerate(M, 1) if i > 11500 and 'crosscut' in l])

hr('§3 A.1 / A.3 — Λ₈ IS CLOSED, AND EVERY PROJECTION π_F(Λ₈) IS CLOSED (all 255 non-empty F ⊆ {1..8}; convention: closed = componentwise ∨ and ∧ of every pair land in the set)')
L8 = np.array(T.L8(), dtype=np.int64); n8 = len(L8); print('  |Λ₈| =', n8, '(tower-2 by r2lib.load_tower, caps (3,3,1,3,1))')
def packed(A):  # rows of small non-negative ints → one int64 per row (each coordinate < 16 here: max value is 3, 2S ≤ 3)
    assert A.max() < 16; w = 16 ** np.arange(A.shape[1], dtype=np.int64); return A @ w
def closed(A):
    P = np.unique(A, axis=0); K = packed(P); J = packed(np.maximum(P[:, None, :], P[None, :, :]).reshape(-1, P.shape[1])); Mt = packed(np.minimum(P[:, None, :], P[None, :, :]).reshape(-1, P.shape[1]))
    return bool(np.isin(J, K).all()), bool(np.isin(Mt, K).all()), len(P)
cj, cm, _ = closed(L8); print('  A.1: Λ₈ closed under ∨:', cj, '; under ∧:', cm, '(all %s ordered pairs)' % f'{n8*n8:,}')
bad = []; sizes = {}
for r in range(1, 9):
    for F in itertools.combinations(range(8), r):
        j, m, sz = closed(L8[:, list(F)]); sizes[F] = sz
        if not (j and m): bad.append((F, j, m))
print('  A.3: subsets F tested:', sum(1 for r in range(1, 9) for _ in itertools.combinations(range(8), r)), '; projections NOT closed:', len(bad), bad[:5], '— every projection of Λ₈ is closed:', not bad)
print('  projection sizes (|π_F|) for the singletons, coordinate order n l k q e f g 2S:', [sizes[(i,)] for i in range(8)], '; for the 28 pairs min/max:', min(sizes[F] for F in sizes if len(F) == 2), max(sizes[F] for F in sizes if len(F) == 2))
# the converse: a set whose every proper projection is closed but which is not closed — the Remark's claim, exhibited on a 2-cell set
X = np.array([[0, 1], [1, 0]]); print('  Remark witness (converse fails): X = {(0,1),(1,0)} — π_1, π_2 closed:', closed(X[:, [0]])[:2], closed(X[:, [1]])[:2], '; X closed:', closed(X)[:2], '(join (1,1) absent)')

hr('§4 A.8 — THE d = 2 CRITERION ON THE 28 COORDINATE-PAIR PROJECTIONS OF Λ₈ (convention: "u may precede v" iff ∀b₁∈F(u), b₂∈F(v): min∈F(u) and max∈F(v); F(u) = fibre over u; 13l-01 re-measured at the appendix site)')
names = ['n', 'l', 'k', 'q', 'e', 'f', 'g', '2S']
def may_precede(X):   # X: set of (a0, a1); returns relation dict on A0 values
    fib = {}
    for a, b in X: fib.setdefault(a, set()).add(b)
    A0 = sorted(fib); rel = {}
    for u in A0:
        for v in A0:
            if u == v: continue
            rel[(u, v)] = all(min(b1, b2) in fib[u] and max(b1, b2) in fib[v] for b1 in fib[u] for b2 in fib[v])
    return A0, fib, rel
nec_ok = 0; ties = []; nontotal = []; refl = 0
for i, j in itertools.combinations(range(8), 2):
    X = set(map(tuple, L8[:, [i, j]].tolist())); A0, fib, rel = may_precede(X)
    nec = all(rel[(u, v)] for u, v in itertools.combinations(A0, 2)); nec_ok += nec   # natural order u<v ⇒ u may precede v (necessity, closed X)
    tie = [(u, v) for u, v in itertools.combinations(A0, 2) if rel[(u, v)] and rel[(v, u)]]; ties.append(((names[i], names[j]), len(tie)))
    tot = all(rel[(u, v)] or rel[(v, u)] for u, v in itertools.combinations(A0, 2))
    if not tot: nontotal.append((names[i], names[j]))
print('  necessity (closed ⇒ natural order ⊆ may-precede) holds on', nec_ok, 'of 28 pairs; may-precede total (u≼v or v≼u for every u≠v) on', 28 - len(nontotal), 'of 28', nontotal)
print('  antisymmetry fails (u≼v and v≼u, both fibres equal-or-nested both ways) on', sum(1 for _, t in ties if t), 'of 28 pairs; tie counts per pair:', [(p, t) for p, t in ties if t])
print('  → on Λ₈ itself may-precede is a total PREORDER on every pair projection; a total ORDER on', sum(1 for _, t in ties if not t), 'of 28 — 13l-01 stands at the A.8 site (the statement says "total order … that order is the relabelling")')
# sufficiency, independently: random 2-D sets whose may-precede is a total preorder must be closed; a set with a non-total relation may or may not be
rng = random.Random(1808); suff = tot_n = 0; conv = 0
for _ in range(2000):
    m, kk = rng.randint(2, 5), rng.randint(2, 5); X = {(a, b) for a in range(m) for b in range(kk) if rng.random() < 0.6}
    if len({a for a, _ in X}) < 2: continue
    A0, fib, rel = may_precede(X); tot = all(rel[(u, v)] or rel[(v, u)] for u, v in itertools.combinations(A0, 2))
    if tot:
        tot_n += 1; order = sorted(A0, key=lambda u: sum(rel[(w, u)] for w in A0 if w != u)); pos = {u: order.index(u) for u in A0}
        Y = np.array([[pos[a], b] for a, b in X]); suff += closed(Y)[0] and closed(Y)[1]
print('  sufficiency on seeded random sets (seed 1808, 2000 draws): relation total on', tot_n, '; relabelled by the preorder, closed on', suff, 'of', tot_n, '(convention: ties broken by rank — any tie order works, as 13l-01 found)')
print('  "Verified on 120 constructed sets; 274 of 274" — sites:', sites(r'274 of 274')['main'], '; Register:', sites(r'\b274 of 274\b')['reg'], '; §15.3 L4302 reads "Verified on 120 sets; 274 of 274 constructed total orders" (same figures, no population in any volume — 13l-01/13l-04 carry)')

hr('§5 A.9 — μ_Λ₈ AGAINST THE ANTICHAIN FORMULA (convention: μ by the recursive definition μ(x,x)=1, μ(x,y) = −Σ_{x≤z<y} μ(x,z); P = join-irreducibles = elements covering exactly one element; Q = J(y)∖J(x))')
cells = [tuple(c) for c in T.L8()]; idx = {c: i for i, c in enumerate(cells)}; A = L8
leq = (A[:, None, :] <= A[None, :, :]).all(axis=2)   # leq[i,j] : cell i ≤ cell j
lt = leq & ~np.eye(n8, dtype=bool); cover = lt & ~(lt.astype(np.int64) @ lt.astype(np.int64)).astype(bool)
ncov_below = cover.sum(axis=0); JI = [i for i in range(n8) if ncov_below[i] == 1]; bottom = [i for i in range(n8) if ncov_below[i] == 0]
print('  comparable pairs (x<y):', int(lt.sum()), '; covering pairs:', int(cover.sum()), '; bottom elements:', [cells[i] for i in bottom], '; join-irreducibles |P| =', len(JI), '(main L2017 "a 17-element poset"; A.19 "seventeen generators")')
# distributivity witnessed: componentwise lattice — check the identity on 20,000 seeded triples
rng = random.Random(1809); dist = 0; NT = 20000
for _ in range(NT):
    x, y, z = (A[rng.randrange(n8)] for _ in range(3)); dist += np.array_equal(np.minimum(x, np.maximum(y, z)), np.maximum(np.minimum(x, y), np.minimum(x, z)))
print('  distributive identity x∧(y∨z) = (x∧y)∨(x∧z) on', NT, 'seeded triples (seed 1809):', dist, 'of', NT, '(componentwise min/max on ℤ⁸ is distributive identically; Λ₈ closed (§3) is a sublattice)')
Jset = [frozenset(p for p in JI if leq[p, i]) for i in range(n8)]
print('  Birkhoff check: distinct down-sets J(x) over the 976 cells:', len(set(Jset)), '= 976:', len(set(Jset)) == n8, '; x ≤ y ⟺ J(x) ⊆ J(y) on all pairs:', all((Jset[i] <= Jset[j]) == bool(leq[i, j]) for i in range(n8) for j in range(n8)))
def mu_rec(x, y):
    I = [z for z in range(n8) if leq[x, z] and leq[z, y]]; I.sort(key=lambda z: int(A[z].sum())); mu = {x: 1}
    for z in I:
        if z == x: continue
        mu[z] = -sum(mu[w] for w in I if w in mu and leq[w, z] and w != z)
    return mu[y], len(I)
def mu_formula(x, y):
    Q = Jset[y] - Jset[x]; anti = all(not lt[p, r] for p in Q for r in Q); return (-1) ** len(Q) if anti else 0, len(Q), anti
rng = random.Random(1810); pairs = [(i, j) for i in range(n8) for j in range(n8) if cover[i, j]]; cpairs = rng.sample(pairs, 60)
comp = [(i, j) for i in range(n8) for j in range(n8) if lt[i, j] and not cover[i, j]]; cpairs += rng.sample(comp, 140)
agree = 0; vals = set(); isz = []; nonzero_nonanti = 0; big = 0
for x, y in cpairs:
    m1, sz = mu_rec(x, y); m2, k, anti = mu_formula(x, y); agree += (m1 == m2); vals.add(m1); isz.append(sz)
print('  200 seeded comparable pairs (60 covering + 140 non-covering, seed 1810): recursive μ = antichain formula on', agree, 'of 200; values taken:', sorted(vals), '; interval sizes min/max:', min(isz), max(isz), '— "47 comparable pairs, values only in {−1, 0, +1}" reproduces in kind (the 47 has no population: main L2017, L9996 only; Register sites:', sites(r'\b47 comparable')['reg'], ')')
print('  μ = −1 on every covering pair (|Q| = 1, trivially an antichain):', all(mu_formula(x, y)[0] == -1 for x, y in pairs), 'over', len(pairs), 'covering pairs; μ ∈ {−1,0,+1} on ALL comparable pairs by the formula:', set(mu_formula(x, y)[0] for x, y in comp + pairs) <= {-1, 0, 1}, '; non-zero on', sum(1 for x, y in comp + pairs if mu_formula(x, y)[0] != 0), 'of', len(comp) + len(pairs))
print('  crosscut clause witnessed: for the 140 non-covering pairs, formula 0 ⟺ Q not an antichain ⟺ join of the atoms of J(Q) ≠ Q:', all((mu_formula(x, y)[0] == 0) == (not mu_formula(x, y)[2]) for x, y in cpairs[60:]))

hr('§6 A.10 — THE CONSTRAINT GRAPH OF Λ₈ IS A TREE; THE BOX COUNT FACTORISES (convention: one edge per binary Heaviside constraint as tower-2 codes them; boxes are coordinate intervals [lo_i, hi_i]; seeded random boxes plus the full box)')
edges = [('n', 'l'), ('l', 'k'), ('k', 'q'), ('e', 'f'), ('f', 'g'), ('q', 'g'), ('k', '2S')]
adj = {v: set() for v in names}
for a, b in edges: adj[a].add(b); adj[b].add(a)
seen = {'n'}; stack = ['n']
while stack:
    v = stack.pop(); [stack.append(w) or seen.add(w) for w in adj[v] if w not in seen]
print('  constraints as coded (tower-2 L8): l≤n−1, k≤4l+2, q≤k, f≤e−1, g≤4f+2, g≤q, 2S≤k → 7 edges on 8 nodes, connected:', len(seen) == 8, '; |E| = |V| − 1:', len(edges) == 7, '⇒ a tree (cap constraints l≤1, k≤3, e≤3, f≤1 are unary and add no edge)')
print('  degrees:', {v: len(adj[v]) for v in names}, '— the graph\'s leaves are n, e, 2S (degree 1); g has degree 2 (neighbours q and f): the printed "leaves 2S and g" names g as a leaf; g is innermost in the nested sum with BOTH its neighbours fixed — the factor #{g | q, f} is still independent (incidental wording, measured below)')
proj6 = set(map(tuple, L8[:, :6].tolist()))
def direct(lo, hi): return int(((A >= lo) & (A <= hi)).all(axis=1).sum())
def factor(lo, hi):
    tot = 0
    for c in proj6:
        if all(lo[i] <= c[i] <= hi[i] for i in range(6)):
            n_, l_, k_, q_, e_, f_ = c
            n2S = max(0, min(hi[7], k_) - lo[7] + 1); ng = max(0, min(hi[6], q_, 2 * (2 * f_ + 1)) - lo[6] + 1); tot += n2S * ng
    return tot
rng = random.Random(1811); mx = A.max(axis=0); ok = 0; NB = 40; ex = []
for t in range(NB):
    lo = [rng.randint(0, int(mx[i])) for i in range(8)]; hi = [rng.randint(lo[i], int(mx[i])) for i in range(8)]; d, f = direct(lo, hi), factor(lo, hi); ok += (d == f)
    if t < 3: ex.append((lo, hi, d, f))
print('  seeded random boxes (seed 1811), %d drawn: direct = factorised on' % NB, ok, 'of', NB, '; first three:', ex)
print('  full box: direct', direct([0] * 8, mx.tolist()), '= factorised', factor([0] * 8, mx.tolist()), '= 976:', direct([0] * 8, mx.tolist()) == factor([0] * 8, mx.tolist()) == 976, '; "eight random intervals" sites:', sites(r'eight random intervals')['main'], 'Register:', sites(r'eight random intervals')['reg'])
c2S = bool((A[:, 7] <= A[:, 2]).all()); cg = bool((A[:, 6] <= A[:, 3]).all()) and bool((A[:, 6] <= 4 * A[:, 5] + 2).all())
att = bool((A[:, 7] == A[:, 2]).any()) and bool((A[:, 6] == np.minimum(A[:, 3], 4 * A[:, 5] + 2)).any())
print('  the two leaf formulas as printed: #{2S} = max(0, min(hi7, k) - lo7 + 1) - coordinate 7 = 2S with 2S <= k:', c2S, '; #{g} = max(0, min(hi6, q, 2(2f+1)) - lo6 + 1) - coordinate 6 = g with g <= q and g <= 4f+2:', cg, '; both bounds attained somewhere (2S = k, g = min(q, 4f+2)):', att)

hr('§7 A.11 — ν = e − δ IS NOT A LATTICE HOMOMORPHISM (convention: δ = f − ℓ as §17.3 L4819/L4825 and 13t-05 record; the Statement needs one witness; the 86 is 13t-04\'s, re-measured under two readings)')
nu = A[:, 4] - (A[:, 5] - A[:, 1]); jn = np.maximum(A[:, None, :], A[None, :, :]); nu_j = jn[:, :, 4] - (jn[:, :, 5] - jn[:, :, 1])
hom_fail = int((nu_j != np.maximum(nu[:, None], nu[None, :])).sum()); print('  ordered pairs with ν(x∨y) ≠ max(ν(x), ν(y)):', f'{hom_fail:,}', 'of', f'{n8*n8:,}', '— ν is not a join-homomorphism (the Statement\'s witness); zero would refute A.11')
dec_comp = int(((nu[:, None] > nu[None, :]) & lt).sum()); dec_cov = int(((nu[:, None] > nu[None, :]) & cover).sum())
print('  ν decreasing on comparable pairs x<y:', f'{dec_comp:,}', 'of', f'{int(lt.sum()):,}', '; on covering pairs:', dec_cov, 'of', int(cover.sum()), '— neither is 86 (13t-04: none of fifteen readings at three caps gives 86; stands); main sites of "86 violations":', sites(r'86 violations')['main'], 'Register:', sites(r'86 violations')['reg'])
print('  "ν grades every chain of Λ" — reading: ν strictly monotone along every covering step? covering steps with ν equal:', int(((nu[:, None] == nu[None, :]) & cover).sum()), '; with ν increasing:', int(((nu[:, None] < nu[None, :]) & cover).sum()), '; decreasing:', dec_cov, '— ν is NOT monotone along covers under δ = f − ℓ (§12.2 L2328 says the same in different figures: "24 of 70", 12a-01 no population)')

hr('§8 A.12 — THE min/max REVERSAL UNDER T = I − E (an algebraic identity; measured on seeded triples with Decimal, and stated exactly)')
rng = random.Random(1812); ok = 0; NT = 5000
for _ in range(NT):
    I = D(rng.randint(-1000, 1000)) / 7; E = [D(rng.randint(-99999, 99999)) / 13 for _ in range(3)]; Tt = [I - e for e in E]
    lhs = min(Tt[0], Tt[2]) <= Tt[1] <= max(Tt[0], Tt[2]); rhs = min(E[0], E[2]) <= E[1] <= max(E[0], E[2]); ok += (lhs == rhs)
print('  min(T(n−1),T(n+1)) ≤ T(n) ≤ max(…) ⟺ the same for E, on', NT, 'seeded triples (seed 1812), agreement', ok, 'of', NT, '; exact reason: T = I − E is order-reversing and I cancels: min(I−a, I−b) = I − max(a,b)')
print('  "ν, δ and V all require I" (A.12 Consequence, L10035) — 14h-02 carries (main L6133 twin site): V = w/e needs I only as 4ν/3; the site count:', sites(r'all require I|all need the ionis')['main'])

hr('§9 A.13 — THE HALF-SPACING 2Z²R/ν³, ν_fail AT Z = 2, AND THE STRICTNESS OF "iff" (convention: R = the constant the book\'s ν_fail table uses; Decimal HALF_UP)')
Rc = [(i, M[i - 1][:120]) for i, l in enumerate(M, 1) if re.search(r'109\s?73\d', l)][:4]; print('  R sites in main:', Rc)
Rv = D('109737.316'); Z = D(2); dT = D(3000)
nuf = (D(2) * Z * Z * Rv / dT) ** (D(1) / D(3)); print('  ν_fail = (2Z²R/|ΔT|)^{1/3} at Z = 2, ΔT = 3,000 cm⁻¹, R = 109737.316:', q(nuf, '0.001'), '→ "ν ≈ 6.6":', q(nuf, '0.1') == '6.6', '; at Z = 1:', q((D(2) * Rv / dT) ** (D(1) / D(3)), '0.1'), '(the §25.6 table L6942 prints 4.2 | 6.6)')
print('  d/dν (Z²R/ν²) = −2Z²R/ν³ (exact; a power rule); half of |T(n−1) − T(n+1)| ≈ |dT/dn| = 2Z²R/ν³ to first order — the proof says "to leading order" and the Statement says "iff": measured gap asymmetry at ν = 5.3, Z = 2:')
for nuv in (D('5.3'), D('3'), D('6.6')):
    Tn = lambda v: Z * Z * Rv / (v * v); up, dn = Tn(nuv - 1) - Tn(nuv), Tn(nuv) - Tn(nuv + 1); hs = D(2) * Z * Z * Rv / nuv ** 3
    print('    ν =', nuv, ': gap to n−1', q(up, '1'), '; gap to n+1', q(dn, '1'), '; 2Z²R/ν³', q(hs, '1'), '; half of |T(n−1)−T(n+1)|', q((up + dn) / 2, '1'), '; the smaller one-sided gap / 2Z²R/ν³ =', q(dn / hs, '0.001'))
print('  → a displacement between the smaller one-sided gap and 2Z²R/ν³ reorders the level while the Statement\'s "iff" says it does not: the Statement is exact only to leading order in 1/ν (the proof says so; the Statement does not) — recorded, docket 12/34 kind')
print('  "a maximum ν = 5.3 reached by that channel" — main sites of "ν = 5.3":', sites(r'ν = 5\.3')['main'], '; the channel is §25.6\'s Hg II 5d¹⁰np (L6936); "no channel in this work enters the failure regime" — the ν_fail table L6940–L6945 and its conclusion L6947 (DEF chat-107 block: 8 of 8 reproduce)')

hr('§10 PRE-PP DIFF — headings and Statement lines of the unit against the Prints & Proofs original (section number stripped from BOTH sides of a heading comparison; whitespace-normalised)')
if PP is None: print('  PP not on disk — BUDGET: fetched at the gate to /home/claude/PP_The_Method_1_6.md; re-run there')
else:
    pa = [i for i, l in enumerate(PP, 1) if re.match(r'^# APPENDICES\s*$', l)]; print('  PP `# APPENDICES`:', pa, '; PP `# Appendix A`:', [i for i, l in enumerate(PP, 1) if re.match(r'^#+ Appendix A ', l)], '; PP A.n lines (unmarked headings, plain `A.n Title` at line start):')
    ppA = [(i, l.strip()) for i, l in enumerate(PP, 1) if i > pa[-1] and re.match(r'^ ?A\.\d+(\.\d+)? \S', l) and not re.match(r'^ ?A\.\d+\s{2,}', l)]
    ppB = [i for i, l in enumerate(PP, 1) if re.match(r'^#+ Appendix B ', l)]; ppA = [(i, l) for i, l in ppA if i < ppB[-1]]
    print('   ', [(i, l.split()[0]) for i, l in ppA])
    volH = {l.split()[1]: (i, norm(re.sub(r'^#+\s*A\.\d+(\.\d+)?\s*', '', l))) for i, l in An if i < unit[1]}; ppH = {l.split()[0]: (i, norm(re.sub(r'^A\.\d+(\.\d+)?\s*', '', l))) for i, l in ppA}
    for k in sorted(volH, key=lambda s: [int(t) for t in s[2:].split('.')]):
        v = volH[k]; p = ppH.get(k); print(f'  {k}: volume L{v[0]} "{v[1]}" | PP', 'ABSENT' if p is None else f'P{p[0]} "{p[1]}"', '| equal:', p is not None and v[1] == p[1])
    print('  PP sections after the unit (part 2 will diff them):', [k for k in ppH if k not in volH])
    def stmt(lines, start, stop):
        return [(i, norm(lines[i - 1])) for i in range(start, stop) if re.match(r'^\s*Statement\.', lines[i - 1])]
    vs = stmt(M, unit[0], unit[1]); ps = stmt(PP, pa[-1], ppB[-1])
    print('  Statement lines: volume', len(vs), '; PP', len(ps))
    for (vi, vt), (pi, pt) in zip(vs, ps): print(f'   L{vi} vs P{pi}: first-line equal:', vt == pt, '' if vt == pt else f'\n      V: {vt[:150]}\n      P: {pt[:150]}')
    op = [(i, norm(M[i - 1])) for i in range(unit[0], unit[1]) if re.search(r'proofs are given in full', M[i - 1])]; pop = [(i, norm(PP[i - 1] + ' ' + PP[i])) for i in range(pa[-1], ppB[-1]) if re.search(r'proofs are given in full', PP[i - 1])]
    print('  opener: volume L%d: %s' % (op[0][0], op[0][1][:130])); print('          PP P%d: %s' % (pop[0][0], pop[0][1][:130]))
    print('  PP table DATA rows:', len([l for i, l in enumerate(PP, 1) if pa[-1] < i < ppB[-1] and re.match(r'^\s+A\.\d+\s{2,}', l)]), '; PP one-dot A.n sections:', len([k for k in ppH if k.count('.') == 1]), '→ PP\'s "Ten … in full; remaining seven" against its own 9 rows and its own section count: the post-PP rewrite corrected the opener (record-carried as PP\'s state; volume now 9 + 10 = 19, MEASURED in §1)')
    # body-level diff of each section in the unit: paragraphs present in volume but not PP and vice versa (normalised, stripped of markdown emphasis)
    def paras(lines, a, b): return [norm(re.sub(r'[*_`]', '', lines[i - 1])) for i in range(a, b) if lines[i - 1].strip()]
    pv = paras(M, unit[0], unit[1]); pstart = pa[-1]; pend = [i for i, l in ppA if l.startswith('A.15')]; pend = pend[0] if pend else ppB[-1]; pp_ = paras(PP, pstart, pend)
    onlyV = [x for x in pv if x not in pp_]; onlyP = [x for x in pp_ if x not in pv]
    print('  non-blank lines: volume', len(pv), '; PP (to A.15)', len(pp_), '; in volume not PP:', len(onlyV), '; in PP not volume:', len(onlyP))
    for x in onlyV[:14]: print('    V+ ', x[:170])
    for x in onlyP[:14]: print('    P+ ', x[:170])

hr('§11 REGISTER — entries naming A.3/A.8–A.13 and the unit\'s named objects; WARNING lines read (a Register entry body is the first non-blank line after its heading)')
hitsA = [i + 1 for i, l in enumerate(R) if re.search(r'\bA\.(3|8|9|10|11|12|13)\b', l)]; print('  Register lines naming A.3/A.8–A.13:', hitsA, [R[i - 1][:110] for i in hitsA])
kw = {'Möbius|Mobius': r'Möbius|Mobius', 'crosscut': 'crosscut', 'projection of a closed|projections of closed': r'projections? of (a )?closed', 'total order': r'total order', 'may precede': r'may precede', 'tree factor': r'tree factor|factoris', 'limit-free': r'limit-free', 'ν_fail|half-spacing': r'ν_fail|half-spacing', 'join-irreducible': r'join-irreducible'}
ent = lambda ln: next((int(re.match(r'^#{1,4}\s*(\d+)\s*$', R[j - 1]).group(1)) for j in range(ln, 0, -1) if re.match(r'^#{1,4}\s*\d+\s*$', R[j - 1])), None)
for name, pat in kw.items():
    ls = [i + 1 for i, l in enumerate(R) if re.search(pat, l, re.I)]; es = sorted(set(e for e in map(ent, ls) if e))
    print(f'  {name}: {len(ls)} Register lines, entries {es[:16]}{" …" if len(es) > 16 else ""}')
    for e in es[:16]:
        b = rbody(e); w = 'WARNING' in (b or '')
        if w: print(f'     {e} WARNING: {b[:140]}')
print('  unit lines containing "register" (lowercase, G0i) or "Register":', uline(r'[Rr]egister'), '— the appendix cites no Register entry by number')
