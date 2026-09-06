#!/usr/bin/env python3
"""t7e_probe.py -- s42 item 0. READ-ONLY DIAGNOSTIC. Decides F39.2: (a) 4d unbound vs (b) 4d missed.

Captures the ACTUAL (Vloc, X, e0) handed to solve_one for the l=2 channel at the failing step, then
re-expresses shoot(e) OUTSIDE its closure using the SAME module-level objects from t7c_hfsr
(qlog, _derivs, _lib.shoot_x, _D) and the SAME grid. Not new numerics: the parent kernel called directly.
That claim is TESTED by PP-0 before any 4d number is read.

Edits nothing. t7c_hfsr.py, t7b_hf.py, hfc2.py untouched -> gates 1-71 stay byte-identical.
"""
import os, sys, math, json
os.environ.setdefault("SIC_NOCLAMP", "1")
import numpy as np
import hfc2
from t7c_hfsr import _lib, _D
from t7c_kernel import qlog, _derivs, C0, eigen_sr
from t5_scf import ground_occ

CAP = []            # capture log: dicts of the inputs/outputs of solve_one


class CapHFC(hfc2.HFC):
    """Records solve_one's inputs and outputs. Behaviour identical to the parent (pure passthrough)."""
    WANT = None     # (l, n) to capture; None = all

    def solve_one(self, l, n, Vloc, X, e0, Pold=None):
        u, e, nd, res = super().solve_one(l, n, Vloc, X, e0, Pold)
        if self.WANT is None or (l, n) == self.WANT:
            CAP.append(dict(l=l, n=n, Vloc=np.array(Vloc, float), X=np.array(X, float),
                            e0=float(e0), e=float(e), nd=int(nd),
                            Pold=(None if Pold is None else np.array(Pold, float)),
                            r=self.r.copy(), x=self.x.copy(), h=self.h, dr=self.dr.copy(),
                            N=self.npts, c=self.c, srcM=self.srcM, Z=self.Z))
        return u, e, nd, res


def make_shoot(cap):
    """Re-express solve_one's inner shoot(e) verbatim against the captured state."""
    r, x, h, N, c = cap['r'], cap['x'], cap['h'], cap['N'], cap['c']
    Vloc, X, l, srcM = cap['Vloc'], cap['X'], cap['l'], cap['srcM']
    dr = cap['dr']
    Vp, Vpp = _derivs(x, Vloc)
    Pold = cap['Pold']
    yold = (Pold * np.exp(-x / 2)) if (Pold is not None and np.any(X)) else np.zeros(N)

    def shoot(e):
        q, M = qlog(r, Vloc, Vp, Vpp, e, l, c)
        f = 1 - h * h * q / 12.0
        s = -2.0 * (M if srcM else 1.0) * r ** 1.5 * X
        allowed = np.where(q < 0)[0]
        m = int(allowed[-1]) if len(allowed) else N // 2
        if m > N - 4: m = N - 4
        if m < 2: m = 2
        sq = np.sqrt(np.maximum(q, 0)); cum = np.cumsum(sq[m:]) * h
        beyond = np.where(cum > (20.0 if np.any(s) else 60.0))[0]
        ie = m + int(beyond[0]) if len(beyond) else N - 1
        if ie < m + 3: ie = min(m + 3, N - 1)
        yoh, yop, yih, yip = (np.zeros(N) for _ in range(4))
        _lib.shoot_x(N, h, f.ctypes.data_as(_D), s.ctypes.data_as(_D), m, ie, 1e-30,
                     1e-30 * math.exp((l + 0.5) * h), float(yold[ie]), float(yold[ie - 1]),
                     yoh.ctypes.data_as(_D), yop.ctypes.data_as(_D),
                     yih.ctypes.data_as(_D), yip.ctypes.data_as(_D))
        Mm = np.array([[yoh[m], -yih[m]], [yoh[m + 1], -yih[m + 1]]])
        rhs = np.array([yip[m] - yop[m], yip[m + 1] - yop[m + 1]])
        if not np.any(s):
            A, B = 1.0, (yoh[m] / yih[m] if yih[m] != 0 else 0.0)
        else:
            try: A, B = np.linalg.solve(Mm, rhs)
            except np.linalg.LinAlgError: return None
        y = np.concatenate([yop[:m + 1] + A * yoh[:m + 1], yip[m + 1:] + B * yih[m + 1:]])
        u = np.exp(x / 2) * y * np.sqrt(np.maximum(M, 1e-300))
        nrm = float(np.sum(u * u * dr))
        uu = u[:m + 1]; a = np.abs(uu); keep = a > 1e-7 * a.max()
        sg = np.sign(uu[keep]); nd = int(np.sum(sg[1:] != sg[:-1]))
        # nd_full: nodes over the WHOLE grid, to expose PP-5 (a node sitting outside m)
        af = np.abs(u); keepf = af > 1e-7 * af.max()
        sgf = np.sign(u[keepf]); ndf = int(np.sum(sgf[1:] != sgf[:-1]))
        return dict(u=u, nrm=nrm, nd=nd, nd_full=ndf, m=m, ie=ie, rmax_m=float(r[m]))
    return shoot


def capture(Z, cfg, want):
    CAP.clear()
    CapHFC.WANT = want
    try:
        CapHFC(Z, [tuple(t) for t in cfg], c=C0).run2(maxit=1)
    except RuntimeError:
        pass                      # hfc2's node check; the capture already happened
    CapHFC.WANT = None
    return CAP[0] if CAP else None
