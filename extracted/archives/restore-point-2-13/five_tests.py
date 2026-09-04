#!/usr/bin/env python3
"""five_tests.py -- five falsifiable tests, predictions committed (§2.13).

T1  Does a necessary core exist at OTHER caps, or only at the book's?
    PREDICTED: yes, a core exists at every cap setting, and its SIZE grows with
    the cell count. FALSIFIER: any cap setting with zero necessary cells.

T2  Is the core a property of Λ, or of any closed set of that size?
    PREDICTED: random ℛ-closed sets of comparable size will ALSO have necessary
    cells, so the phenomenon is generic — the interesting number is the FRACTION
    (4 of 7 = 57%). FALSIFIER: random sets show a materially different fraction.

T3  Does the core persist up the tower?
    PREDICTED: Λ₉ and Λ₁₀ have necessary cells, and the core fraction FALLS as
    the tower adds coordinates. FALSIFIER: it rises, or vanishes.

T4  Does the statistical language agree with the others on objects OTHER than Λ?
    PREDICTED: it recovers the cell count on every closed object but DISAGREES on
    the open ones — it will not reproduce the periodic table's 36 or the
    calendar's 7, because marginals cannot see a hole. FALSIFIER: it matches.

T5  Is the redundancy gradient uniform or heavy-tailed?
    PREDICTED: heavy-tailed — a few cells in very many triples, most in few.
    FALSIFIER: roughly uniform, i.e. max/median under 3.
"""
import itertools, random, statistics as st
from collections import Counter
from zeno import State, step
from method_tower import base

def clos(X, d):
    X = list(X); A = [sorted({c[i] for c in X}) for i in range(d)]
    def e(a, b):
        m = {}
        for c in X: m[c[b]] = max(m.get(c[b], -99), c[a])
        z = -99; o = {}
        for t in sorted(m): z = max(z, m[t]); o[t] = z
        return o
    ph = {(a, b): e(a, b) for a in range(d) for b in range(d) if a != b}
    return {x for x in itertools.product(*A)
            if all(x[a] <= ph[(a, b)][x[b]] for a in range(d) for b in range(d) if a != b)}

def elements(X, d):
    A = [sorted({c[i] for c in X}) for i in range(d)]
    el, wit = [], {}
    for i in range(d):
        for j in range(d):
            if i == j: continue
            m = {}
            for c in X: m[c[j]] = max(m.get(c[j], -99), c[i])
            r = -99
            for v in sorted(m):
                if m[v] > r:
                    r = m[v]; k = ("s", i, j, v, r); el.append(k)
                    wit[k] = frozenset(c for c in X if c[j] == v and c[i] == r)
    for i in range(d):
        for v in A[i]:
            k = ("a", i, v); el.append(k); wit[k] = frozenset(c for c in X if c[i] == v)
    return el, wit

def necessary(X, d):
    """cells that uniquely cover at least one element — no substitute exists"""
    el, wit = elements(X, d)
    need = [e for e in el if len(wit[e]) == 1]
    core = {next(iter(wit[e])) for e in need}
    return len(core), len(el)

def greedy_seed(X, d):
    el, wit = elements(X, d)
    S = set(X); cov = {c: {e for e in el if c in wit[e]} for c in X}
    un = set(el); G = []
    while un:
        b = max(X, key=lambda c: len(cov[c] & un))
        if not (cov[b] & un): break
        G.append(b); un -= cov[b]
    i = 0
    while i < len(G):
        cd = G[:i] + G[i+1:]
        if len(cd) >= 2 and clos(cd, d) == S: G = cd
        else: i += 1
    return len(G)

def run():
    R = {}
    # ---- T1: other caps
    T1 = []
    for caps in [(2,2,1,2,1), (3,2,1,2,1), (2,3,1,3,1), (3,3,1,3,1), (3,3,1,4,1)]:
        X = [tuple(c) for c in base(caps)]
        if not X or len(X) > 3000: continue
        core, ne = necessary(X, 8)
        T1.append((caps, len(X), ne, core))
    R["T1"] = T1
    # ---- T2: random closed sets
    L8 = [tuple(c) for c in base((3,3,1,3,1))]
    random.seed(4); T2 = []
    for _ in range(6):
        G0 = random.sample(L8, 7)
        Y = clos(G0, 8)
        core, ne = necessary(Y, 8)
        s = greedy_seed(list(Y), 8)
        T2.append((len(Y), ne, core, s))
    R["T2"] = T2
    # ---- T3: up the tower
    T3 = []
    L9 = [c + (s,) for c in L8 for s in range(0, c[2] + 1)]
    for nm, X, d in (("Λ₈", L8, 8), ("Λ₉", L9[:4000], 9)):
        core, ne = necessary(X, d)
        T3.append((nm, len(X), d, ne, core))
    R["T3"] = T3
    # ---- T4: statistics on other objects
    def stat_close(X, d):
        pm = {(i, j): Counter((c[i], c[j]) for c in X)
              for i in range(d) for j in range(i+1, d)}
        A = [sorted({c[i] for c in X}) for i in range(d)]
        return {x for x in itertools.product(*A)
                if all(pm[(i, j)].get((x[i], x[j]), 0) for i in range(d) for j in range(i+1, d))}
    G = {1:[1,18], 2:[1,2]+list(range(13,19)), 3:[1,2]+list(range(13,19))}
    for p in (4,5,6,7): G[p] = list(range(1,19))
    TAB = {(p, g) for p in G for g in G[p]}
    D = [31,28,31,30,31,30,31,31,30,31,30,31]
    CAL = {(m+1, d) for m in range(12) for d in range(1, D[m]+1)}
    T4 = []
    for nm, X, d in (("Λ₈", set(L8), 8), ("periodic table", TAB, 2), ("calendar", CAL, 2)):
        e_ord = len(clos(X, d)) - len(X)
        e_stat = len(stat_close(X, d)) - len(X)
        T4.append((nm, len(X), e_ord, e_stat))
    R["T4"] = T4
    # ---- T5: the redundancy gradient
    el, wit = elements(L8, 8)
    cov = {c: {e for e in el if c in wit[e]} for c in L8}
    FORCED = [(1,0,2,2,3,1,2,2), (2,1,3,3,1,0,0,3), (2,1,3,3,2,1,3,0), (3,1,1,0,3,1,0,0)]
    F = set()
    for c in FORCED: F |= cov[c]
    rem = set(el) - F
    cands = [c for c in L8 if cov[c] & rem]
    trip = [t for t in itertools.combinations(cands, 3)
            if rem <= (cov[t[0]] | cov[t[1]] | cov[t[2]])]
    use = Counter(c for t in trip for c in t)
    v = sorted(use.values())
    R["T5"] = (len(trip), len(use), min(v), int(st.median(v)), max(v), max(v)/st.median(v))
    return R

with State("five_tests") as st_:
    R = step(st_, "five falsifiable tests", run, budget=1700)

print("  T1 · DOES A NECESSARY CORE EXIST AT OTHER CAPS?")
print(f"     {'caps':<18}{'cells':>7}{'elements':>10}{'necessary':>11}")
for caps, n, ne, core in R["T1"]:
    print(f"     {str(caps):<18}{n:>7}{ne:>10}{core:>11}")
print("\n  T2 · IS IT GENERIC? random ℛ-closed sets")
print(f"     {'cells':>7}{'elements':>10}{'necessary':>11}{'seed':>7}{'core/seed':>11}")
for n, ne, core, s in R["T2"]:
    print(f"     {n:>7}{ne:>10}{core:>11}{s:>7}{(core/s if s else 0):>10.0%}")
print(f"     Λ₈ for comparison: core 4, seed 7 → {4/7:.0%}")
print("\n  T3 · UP THE TOWER")
print(f"     {'stage':<8}{'cells':>7}{'d':>4}{'elements':>10}{'necessary':>11}")
for nm, n, d, ne, core in R["T3"]:
    print(f"     {nm:<8}{n:>7}{d:>4}{ne:>10}{core:>11}")
print("\n  T4 · STATISTICS ON OTHER OBJECTS")
print(f"     {'object':<18}{'cells':>7}{'E under ℛ':>12}{'E under stat':>14}")
for nm, n, a, b in R["T4"]:
    print(f"     {nm:<18}{n:>7}{a:>12}{b:>14}")
t, u, mn, md, mx, ratio = R["T5"]
print(f"\n  T5 · THE REDUNDANCY GRADIENT")
print(f"     {t} triples over {u} cells   min {mn}  median {md}  max {mx}"
      f"   max/median {ratio:.1f}")
