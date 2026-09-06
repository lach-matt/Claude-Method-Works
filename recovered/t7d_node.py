#!/usr/bin/env python3
"""t7d_node.py -- F39.2 REPAIR. Session 41.

F39.2: t7c_hfsr.solve_one computes tgt = n-l-1 and NEVER USES IT. The eigenvalue search is a
bare log-norm bracket seeded from eigen_sr; where that seed sits too deep the bracket converges
on a LOWER-node state and hfc2.py:55 raises.

Incidence measured s41: 5d 11/11 = 100%; 4d 10/10 at every step since Z=21; 5g 6/11. That blocks
the 4d row (Z=39..48) where 4d must WIN. PROMOTED under M's test: it now furthers n+l.

THE REPAIR, stated exactly as implemented. For a fixed potential and fixed l, the radial node
count identifies the bound state UNIQUELY. The parent's bracket is correct machinery pointed at
the wrong state by its seed. So: re-seed. eigen_sr(V, l, n') rises with n', and the returned node
count rises with it, so walking n' outward from n and accepting the FIRST seed whose returned
node count equals tgt lands on the target state. The eigenvalue returned is then the true one for
(n, l) regardless of which n' seeded it, because nd == tgt identifies the state.

This calls only the parent's own kernel. The shooting numerics are NOT reimplemented, so nothing
outside the failing channels can drift. On any channel already returning nd == tgt this module is
INERT and returns the identical number -- which is the comparison that decides.

t7c_hfsr.py and t7b_hf.py are NOT edited (gates 1-71 stay byte-identical).
"""
import numpy as np
from t7c_hfsr import HFSR


class HFSRN(HFSR):
    """HFSR with the node target enforced. Drop-in: same signature, same return tuple."""

    MAXWALK = 10

    def solve_one(self, l, n, Vloc, X, e0, Pold=None):
        tgt = n - l - 1
        u, e, nd, res = super().solve_one(l, n, Vloc, X, e0, Pold)
        if nd == tgt:
            return u, e, nd, res                       # inert on healthy channels
        for k in range(1, self.MAXWALK + 1):
            for nn in (n + k, n - k):
                if nn - l - 1 < 0:
                    continue
                try:
                    u2, e2, nd2, res2 = super().solve_one(l, nn, Vloc, X, e0, Pold)
                except Exception:
                    continue
                if nd2 == tgt:
                    return u2, e2, nd2, res2
        raise RuntimeError(f"F39.2 repair exhausted: l={l} n={n} tgt={tgt} got nd={nd}")