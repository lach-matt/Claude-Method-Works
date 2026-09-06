

# ---------------------------------------------------------------------------------------------
# Lifted in chat 82 (HANDOFF-34's standing instruction: a batch that copies functions verbatim is
# worse than the library carrying them).  Verbatim from r2-ch13j.py, which generalised them from
# r2-ch13h.py §3/§4 (chat 81); Rset came to r2-ch13h from r2-ch13g.py, and to that from r2-ch12r.py's
# Rbox.  Nothing here is called by any instrument banked before chat 82.
import itertools as _it
import numpy as _np


def Rset(X):
    """ℛ(X): every cell of the ambient box ∏ Âᵢ(X) with xᵢ ≤ φ̂ᵢⱼ(xⱼ) for all i ≠ j (§6.1 L1540)."""
    A = _np.array(sorted(set(X)), dtype=_np.int64); d = A.shape[1]
    vals = [_np.unique(A[:, i]) for i in range(d)]
    phi = {}
    for i in range(d):
        for j in range(d):
            if i == j: continue
            m = _np.full(int(A[:, j].max()) + 1, -1, dtype=_np.int64)
            for v in vals[j]: m[v] = A[A[:, j] <= v, i].max()
            phi[(i, j)] = m
    G = _np.array(_np.meshgrid(*vals, indexing='ij')).reshape(d, -1).T
    ok = _np.ones(len(G), dtype=bool)
    for (i, j), m in phi.items(): ok &= G[:, i] <= m[G[:, j]]
    return set(map(tuple, G[ok]))


def cover_model(cells):
    """§14.5.7's seed definition as a covering problem (§14.5.9 L3923–3925).  Elements are the value
    slots of the ambient box and the envelope steps (i, j, v) → top; a cell covers a step it witnesses;
    the sixth field of a 'phi' element says whether that step RAISES the envelope (the book's 102-element
    model at Λ₈ is the value slots plus the raising steps).  G ⊆ X covers everything ⟺ ℛ(G) = ℛ(X)."""
    cells = sorted(set(tuple(int(x) for x in c) for c in cells))
    A = _np.array(cells, dtype=_np.int64); n, d = A.shape
    vals = [sorted(set(int(v) for v in A[:, i])) for i in range(d)]
    elems = []; rows = []
    for i in range(d):
        for v in vals[i]:
            elems.append(('val', i, v, v)); rows.append(A[:, i] == v)
    for i in range(d):
        for j in range(d):
            if i == j: continue
            prev = -1
            for v in vals[j]:
                sel = A[:, j] <= v
                top = int(A[sel, i].max())
                elems.append(('phi', i, j, v, top, top > prev)); rows.append(sel & (A[:, i] == top))
                prev = max(prev, top)
    return cells, elems, _np.array(rows), vals


def cover_reduce(Mx):
    """Two exact reductions: drop element e when another element's candidate set is contained in e's;
    then drop any cell whose cover is contained in another cell's.  Returns (kept element indices,
    per-cell bitmasks, non-dominated masks, FULL)."""
    E, n = Mx.shape
    P = _np.packbits(Mx, axis=1)
    keep = []
    for e in range(E):
        sub = ~(P & ~P[e]).any(axis=1)
        dom = False
        for e2 in _np.flatnonzero(sub):
            e2 = int(e2)
            if e2 == e: continue
            if bool((P[e2] == P[e]).all()):
                if e2 < e: dom = True; break
            else:
                dom = True; break
        if not dom: keep.append(e)
    K = Mx[keep]
    masks = []
    for c in range(K.shape[1]):
        m = 0
        for t in _np.flatnonzero(K[:, c]): m |= 1 << int(t)
        masks.append(m)
    uniq = sorted(set(masks))
    nd = [m for m in uniq if m and not any(m != m2 and (m | m2) == m2 for m2 in uniq)]
    return keep, masks, nd, (1 << len(keep)) - 1


def exact_seed(nd, FULL, cap=16):
    """The minimum seed, by branch and bound on the reduced model.  Returns (size, witness masks).
    Settled seed(Λ₈) = 7, seed(Λ₉) = 8, seed(Λ₁₀) = 9 in chat 82."""
    CAND = {}
    def cands(e):
        if e not in CAND: CAND[e] = [m for m in nd if m >> e & 1]
        return CAND[e]
    best = [None]
    def bb(cov, chosen, limit):
        if cov == FULL:
            best[0] = list(chosen); return True
        if len(chosen) >= limit: return False
        rest = FULL & ~cov; pick = None
        while rest:
            b = rest & -rest; e = b.bit_length() - 1; rest ^= b
            c = cands(e)
            if pick is None or len(c) < len(pick): pick = c
            if len(pick) <= 1: break
        for m in pick:
            if bb(cov | m, chosen + [m], limit): return True
        return False
    for limit in range(1, cap + 1):
        best[0] = None
        if bb(0, [], limit): return limit, best[0]
    return None, None


def enum_min_covers(pool, FULL, size):
    """Every minimum cover, as a set of frozensets of cell-cover masks.  Pass the full mask list, not
    only the non-dominated ones, when the count of cell-level covers is what is wanted."""
    CAND = {}
    def cands(e):
        if e not in CAND: CAND[e] = [m for m in pool if m >> e & 1]
        return CAND[e]
    out = set()
    def rec(cov, chosen):
        if cov == FULL:
            if len(chosen) == size: out.add(frozenset(chosen))
            return
        if len(chosen) >= size: return
        rest = FULL & ~cov; pick = None
        while rest:
            b = rest & -rest; e = b.bit_length() - 1; rest ^= b
            c = cands(e)
            if pick is None or len(c) < len(pick): pick = c
            if len(pick) <= 1: break
        for m in pick:
            if m in chosen: continue
            rec(cov | m, chosen + [m])
    rec(0, [])
    return out


def closure_mask(cellsA, mask):
    """ℛ on a subset of a small ambient, by the same box sweep as Rset, on bitmasks.  Validated against
    Rset on every non-empty subset of the 8- and 9-cell ambients (r2-ch13h §4)."""
    if mask == 0: return 0
    X = [cellsA[i] for i in range(len(cellsA)) if mask >> i & 1]
    w = len(X[0])
    vs = [sorted({x[i] for x in X}) for i in range(w)]
    phi = {}
    for i in range(w):
        for j in range(w):
            if i == j: continue
            for v in vs[j]: phi[(i, j, v)] = max(x[i] for x in X if x[j] <= v)
    out = 0
    for n, c in enumerate(cellsA):
        if any(c[i] not in vs[i] for i in range(w)): continue
        if all(c[i] <= phi[(i, j, c[j])] for i in range(w) for j in range(w) if i != j): out |= 1 << n
    return out


def staircase(d, c):
    """Non-increasing d-tuples over {0..c−1}: the 'down-set, c' of §14.5.8 / §14.5.9, ℛ-closed, seeding
    at d + c − 1 exactly (chat 82).  The simplex reading Σx ≤ c−1 has the same cell counts and E > 0."""
    return [t for t in _it.product(range(c), repeat=d) if all(t[i] >= t[i + 1] for i in range(d - 1))]
