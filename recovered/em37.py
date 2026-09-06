# em37.py — verification instrument for OWED row 37 (§12.11.8 quotient-not-extension; MI near-independence)
import sys, math
import numpy as np
sys.path.insert(0, '.')
from em36 import L9c, dl, ds, multipole

MP = {'M1': 0, 'E1': 1, 'E2': 2, 'E3': 3}

def closure_np(cells):
    """Iterative join/meet closure to a fixed point in the product of integer chains (vectorised).
    Returns (closure_size, rounds)."""
    A = np.array(cells, dtype=np.int64)
    off = A.min(axis=0); A = A - off                     # shift to non-negative for keying
    rounds = 0
    while True:
        rounds += 1
        base = A.max(axis=0) + 1
        w = np.cumprod(np.concatenate(([1], base[:-1])))
        keys = A @ w
        keyset = np.unique(keys)
        new_rows = []
        for i in range(len(A)):
            J = np.maximum(A[i], A); M = np.minimum(A[i], A)
            kj = J @ w; km = M @ w
            nj = ~np.isin(kj, keyset); nm = ~np.isin(km, keyset)
            if nj.any(): new_rows.append(J[nj])
            if nm.any(): new_rows.append(M[nm])
        if not new_rows:
            return len(A), rounds
        N = np.unique(np.vstack(new_rows), axis=0)
        A = np.unique(np.vstack([A, N]), axis=0)

def H(p):
    return 0.0 if p in (0, 1) else -(p*math.log2(p) + (1-p)*math.log2(1-p))

def MI(a, b):
    n = len(a); c = {}
    for x, y in zip(a, b): c[(x, y)] = c.get((x, y), 0) + 1
    pa = sum(a)/n; pb = sum(b)/n
    mi = 0.0
    for (x, y), k in c.items():
        pxy = k/n; px = pa if x else 1-pa; py = pb if y else 1-pb
        mi += pxy*math.log2(pxy/(px*py))
    return mi

if __name__ == '__main__':
    part = sys.argv[1] if len(sys.argv) > 1 else 'A'
    L9 = L9c()
    if part == 'A':
        cands = {
            'δ (signed Δℓ)':            lambda c: (dl(c),),
            'σ (signed ΔS)':            lambda c: (ds(c),),
            'δ, σ (signed)':            lambda c: (dl(c), ds(c)),
            '|δ|, |σ|':                 lambda c: (abs(dl(c)), abs(ds(c))),
            'δ, σ, multipole':          lambda c: (dl(c), ds(c), MP[multipole(c)]),
            '|δ|, |σ|, multipole':      lambda c: (abs(dl(c)), abs(ds(c)), MP[multipole(c)]),
            'multipole only':           lambda c: (MP[multipole(c)],),
            '|σ| only':                 lambda c: (abs(ds(c)),),
            'δ, |σ|':                   lambda c: (dl(c), abs(ds(c))),
            '|δ|, σ':                   lambda c: (abs(dl(c)), ds(c)),
        }
        for name, h in cands.items():
            S = [c + h(c) for c in L9]
            n, r = closure_np(S)
            print(f'adjoin {name:24s}: |Λ9′| = {len(S)}  closure = {n}  E = {n-len(S)}  rounds {r}')
    elif part == 'B':
        comp = [1 if c[6] >= 1 else 0 for c in L9]
        preds = {
            'E1 ∧ ΔS=0 (LS-allowed dipole)': lambda c: multipole(c) == 'E1' and ds(c) == 0,
            'E1 (|Δℓ|=1)':                   lambda c: multipole(c) == 'E1',
            'ΔS=0':                          lambda c: ds(c) == 0,
            'E1 ∧ ΔS≠0 (intercombination)':  lambda c: multipole(c) == 'E1' and ds(c) != 0,
            'M1 ∧ ΔS=0':                     lambda c: multipole(c) == 'M1' and ds(c) == 0,
        }
        print(f'composable: {sum(comp)} cells, H = {H(sum(comp)/len(L9)):.4f} bits')
        for name, p in preds.items():
            a = [1 if p(c) else 0 for c in L9]
            print(f'{name:32s} cells {sum(a):4d}  H = {H(sum(a)/len(L9)):.4f}  MI(with composable) = {MI(a, comp):.6f} bits')
