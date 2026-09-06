"""Faster sublattice closure to fixpoint using numpy pairwise min/max.
Equivalent to em_verify.R_closure but scales better for a few-thousand-cell set."""
import numpy as np

def R_closure_fast(cells):
    A = np.array(sorted(set(cells)), dtype=np.int16)
    seen = set(map(tuple, A.tolist()))
    while True:
        n = A.shape[0]
        # pairwise min and max over all pairs (including self) -> generate candidates
        # do it in blocks to bound memory
        new_rows = []
        B = A
        for i in range(n):
            ai = A[i]
            mn = np.minimum(ai, B)   # (n,d)
            mx = np.maximum(ai, B)
            for row in mn:
                t = tuple(int(x) for x in row)
                if t not in seen:
                    seen.add(t); new_rows.append(t)
            for row in mx:
                t = tuple(int(x) for x in row)
                if t not in seen:
                    seen.add(t); new_rows.append(t)
        if not new_rows:
            return seen
        A = np.array(sorted(seen), dtype=np.int16)

def E_fast(cells):
    s=set(map(tuple,cells))
    return len(R_closure_fast(s)) - len(s)
