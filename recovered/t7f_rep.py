#!/usr/bin/env python3
"""t7f_rep.py -- s42 item 0b. THREE CANDIDATE REPAIRS FOR F39.2, run side by side.
M's ruling: test all three, comparison decides. Criteria D1-D5 fixed in PREDICTION-REPAIR-4D.md.

(i)   NodeGated  -- restrict the root search to the e-window where nd == tgt (tgt is computed by the
                    parent and never used). Raises NoRootInNodeWindow rather than returning another state.
(ii)  Damped     -- no code change at all; run2(beta=b). beta cannot move a fixed point.
(iii) ChannelHold-- on nd != tgt, hold that channel's P/eps for the iteration and let the others relax.

Parent files NOT edited: t7c_hfsr.py, t7b_hf.py, hfc2.py untouched -> gates 1-71 byte-identical.
"""
import os, sys, math, json, time
os.environ.setdefault("SIC_NOCLAMP", "1")
import numpy as np
import hfc2
from t7c_kernel import C0


class NoRootInNodeWindow(Exception):
    pass


# ---------------------------------------------------------------- (i) node-gated bracket
class NodeGated(hfc2.HFC):
    """Root search confined to the node-correct window. Uses t7e_probe's faithful shoot."""
    NSCAN = 160

    def solve_one(self, l, n, Vloc, X, e0, Pold=None):
        u, e, nd, res = super().solve_one(l, n, Vloc, X, e0, Pold)
        tgt = n - l - 1
        if nd == tgt:
            return u, e, nd, res                                  # inert on healthy channels
        import t7e_probe as P
        cap = dict(l=l, n=n, Vloc=np.array(Vloc, float), X=np.array(X, float), Pold=Pold,
                   r=self.r, x=self.x, h=self.h, dr=self.dr, N=self.npts, c=self.c,
                   srcM=self.srcM, Z=self.Z)
        sh = P.make_shoot(cap)
        # locate the contiguous e-window where nd == tgt, on a grid spanning the bound range
        lo_e, hi_e = -abs(self.Z) ** 2 / 2.0, -1e-5
        es = -np.geomspace(abs(lo_e), abs(hi_e), self.NSCAN)
        win = []
        for ee in es:
            o = sh(float(ee))
            if o is not None and o['nd'] == tgt:
                win.append((float(ee), math.log(max(o['nrm'], 1e-300))))
        if not win:
            raise NoRootInNodeWindow(f"no nd=={tgt} window: l={l} n={n} Z={self.Z}")
        for k in range(len(win) - 1):
            if np.sign(win[k][1]) != np.sign(win[k + 1][1]):
                a, b = win[k][0], win[k + 1][0]
                for _ in range(80):
                    mid = 0.5 * (a + b)
                    om = sh(mid)
                    v = math.log(max(om['nrm'], 1e-300))
                    if v > 0: b = mid
                    else: a = mid
                e2 = 0.5 * (a + b); o2 = sh(e2)
                return o2['u'] / math.sqrt(o2['nrm']), e2, o2['nd'], 0.0
        raise NoRootInNodeWindow(
            f"nd=={tgt} window exists but log(nrm) has no zero in it: l={l} n={n} Z={self.Z} "
            f"minlog={min(v for _, v in win):+.4f}")


# ---------------------------------------------------------------- (iii) channel hold
class ChannelHold(hfc2.HFC):
    """On nd != tgt, return the PREVIOUS orbital for that channel instead of a wrong-node one."""
    def solve_one(self, l, n, Vloc, X, e0, Pold=None):
        u, e, nd, res = super().solve_one(l, n, Vloc, X, e0, Pold)
        tgt = n - l - 1
        if nd == tgt or Pold is None:
            return u, e, nd, res
        return np.array(Pold, float), float(e0), tgt, res          # hold: P and eps unchanged this iteration


# ---------------------------------------------------------------- harness
CFG_CA = [(1, 0, 2.), (2, 0, 2.), (2, 1, 6.), (3, 0, 2.), (3, 1, 6.), (4, 0, 2.)]


def run(cls, cfg, Z=21, **kw):
    t0 = time.time()
    try:
        E, Ec, it, eps = cls(Z, [tuple(t) for t in cfg], c=C0).run2(**kw)
        return dict(ok=True, E=round(E, 6), it=it,
                    eps={f"{n}{'spdfg'[l]}": round(float(v), 6) for (n, l), v in eps.items()},
                    sec=round(time.time() - t0, 1))
    except Exception as ex:
        return dict(ok=False, err=type(ex).__name__ + ": " + str(ex)[:150],
                    sec=round(time.time() - t0, 1))


def D_of(cls, cand, Z=21, **kw):
    """chain D = E(cfg_prev + cand) - E(cfg_prev), both at nuclear charge Z (F40.1)."""
    ref = run(cls, CFG_CA, Z, **kw)
    add = run(cls, CFG_CA + [cand], Z, **kw)
    if not (ref['ok'] and add['ok']):
        return dict(ok=False, ref=ref, add=add)
    return dict(ok=True, D=round(add['E'] - ref['E'], 6), it=[ref['it'], add['it']],
                eps_ent=add['eps'].get(f"{cand[0]}{'spdfg'[cand[1]]}"),
                sec=round(ref['sec'] + add['sec'], 1))
