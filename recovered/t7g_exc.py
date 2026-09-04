"""t7g_exc.py -- s43, M's ruling (2): adopt NodeGated's EXCEPTION ONLY, not its bracket.

The parent (hfc2.HFC.scf, line 55) raises  RuntimeError("Z=21 42 nodes 0")  when the
converged channel carries the wrong node count. That message names the symptom and
loses the channel's identity, the eigenvalue and the target -- every s41/s42 diagnosis
had to be reconstructed by hand from it.

This subclass raises a NAMED exception carrying (Z, n, l, e, nd, target) at the same
condition. It performs NO scan, NO bracket, NO re-seeding: where the parent raises,
this raises; where the parent returns, this returns the parent's own tuple unchanged.

Inertness is the whole claim and it is testable: on any healthy channel the object
returned is `super().solve_one(...)` itself, so D is bit-identical, not merely equal
to 5 dp. Verified against the s42 D1 reference in GATE 80.

No number changes. No row opens. Diagnostic only.
"""
import hfc2


class NodeCountMismatch(RuntimeError):
    """The converged channel has the wrong node count. Subclass of RuntimeError, so
    every existing `except RuntimeError` site keeps catching it (F39.2 guard included)."""

    def __init__(self, Z, n, l, e, nd, tgt):
        self.Z, self.n, self.l, self.e, self.nd, self.tgt = Z, n, l, e, nd, tgt
        super().__init__(
            f"Z={Z} {n}{'spdfgh'[l]} nodes {nd} (target {tgt}) at e={e:.6f} "
            f"-- no normalisable {tgt}-node solution in THIS field"
        )


class HFCN(hfc2.HFC):
    """hfc2.HFC with the node condition named rather than numbered."""

    def solve_one(self, l, n, Vloc, X, e0, Pold=None):
        out = super().solve_one(l, n, Vloc, X, e0, Pold)
        nd, tgt = out[2], n - l - 1
        if nd != tgt:
            raise NodeCountMismatch(self.Z, n, l, out[1], nd, tgt)
        return out
