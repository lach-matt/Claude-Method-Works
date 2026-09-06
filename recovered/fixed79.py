#!/usr/bin/env python3
"""fixed79.py -- SESSION 79, ITEM 1. THE FIXED-FIELD CROSS-CHANNEL COMPARISON AT Z=89.

CLOSE-S78 §3's residual claim, computed for the first time:
    eps_3^{l=3}(F_core[Phi_d*])  >  eps_4^{l=2}(F_core[Phi_d*])
ONE field. The core is frozen at the converged 6d solution and never updates.

DECLARED CONSTRUCTION, from sealed rt/hfc2.py run2 lines 44-56:
  E1  the field sum runs over CORE keys only; the probe is absent from occ, so it makes
      no contribution to its own field. This is what _ceff(a,Q)=Q[a]-1.0=0 already does
      for a singly occupied valence orbital in the sealed walk.
  E2  Vc = 0 for the probe. Declared in the filed prediction. Applied to l=2 and l=3
      IDENTICALLY, so the comparison is like-for-like.
  E3  only the probe orbital iterates. Y0 over the core is computed ONCE.
  E4  when solve_one returns the wrong node count, the refined scan of pack79/refine79.py
      locates the zero carrying the TARGET node count, most-bound crossing first.

Prediction sha verified at every invocation; HALTS without it.
usage: python3 fixed79.py control    -- the 4f can-fail, MUST report the ordering FAILING
       python3 fixed79.py run        -- the question
"""
import os, sys, math, json, time, hashlib

HERE = os.path.dirname(os.path.abspath(__file__))
PRED = os.path.join(HERE, 'PREDICTION-S79-ITEM1-FIXEDFIELD.md')
PSHA = os.path.join(HERE, 'PREDICTION-S79-ITEM1-FIXEDFIELD.sha256')
OUT = os.path.join(HERE, 'fixed79.json')

os.environ.setdefault("SIC_NOCLAMP", "1")
os.environ.setdefault("SUBCELL", "1")
import numpy as np
import hfc2
from hfc2 import HFC
from t7c_kernel import C0
from t7b_hf import _c3j0sq

NFINE = 1200


def gate_sha():
    want = open(PSHA).read().strip().split()[0]
    got = hashlib.sha256(open(PRED, 'rb').read()).hexdigest()
    if want != got:
        raise SystemExit(f"HALT: prediction sha mismatch\n  filed {want}\n  now   {got}")
    return got


class Frozen(HFC):
    def freeze(self, P, occ_core):
        """E3: the core field, built once and never updated."""
        self.cP = {(n, l): P[(n, l)] for n, l, q in occ_core}
        self.cQ = {(n, l): q for n, l, q in occ_core}
        self.cY0 = {k: self.Yk(self.cP[k], self.cP[k], 0) for k in self.cP}

    def field(self, l, Pp):
        """E1/E2: Vloc and X for a probe of angular momentum l, from the CORE only."""
        r = self.r
        Vloc = -self.Z / r + sum(self.cQ[b] * self.cY0[b] / r for b in self.cP)
        X = np.zeros(self.npts)
        for b in self.cP:
            nb, lb = b
            for k in range(abs(l - lb), l + lb + 1, 2):
                X = X + 0.5 * self.cQ[b] * _c3j0sq(l, k, lb) * self.Yk(Pp, self.cP[b], k) / r * self.cP[b]
        return Vloc, X

    def fine(self, l, n, Vloc, X, Pold, lo_e, hi_e):
        """E4: locate the zero of log(nrm) carrying the TARGET node count."""
        import t7e_probe as P
        cap = dict(l=l, n=n, Vloc=np.array(Vloc, float), X=np.array(X, float), Pold=Pold,
                   r=self.r, x=self.x, h=self.h, dr=self.dr, N=self.npts, c=self.c,
                   srcM=self.srcM, Z=self.Z)
        sh = P.make_shoot(cap)
        tgt = n - l - 1
        es = -np.geomspace(abs(lo_e), abs(hi_e), NFINE)
        win = []
        for ee in es:
            o = sh(float(ee))
            if o is None:
                continue
            if o['nd'] == tgt:
                win.append((float(ee), math.log(max(o['nrm'], 1e-300))))
        sc = [k for k in range(len(win) - 1) if (win[k][1] > 0) != (win[k + 1][1] > 0)]
        if not sc:
            return None, len(win), 0
        a, b = win[sc[0]][0], win[sc[0] + 1][0]
        fa = win[sc[0]][1]
        for _ in range(80):
            m = 0.5 * (a + b)
            o = sh(float(m))
            if o is None:
                break
            fm = math.log(max(o['nrm'], 1e-300))
            if abs(fm) < 1e-11 or abs(b - a) < 1e-14:
                a = b = m
                break
            if (fm > 0) == (fa > 0):
                a, fa = m, fm
            else:
                b = m
        e = 0.5 * (a + b)
        o = sh(float(e))
        u = o['u'] / math.sqrt(o['nrm'])
        return (u, e, int(o['nd'])), len(win), len(sc)

    def probe(self, n, l, e0, P0, beta=0.4, tol=2e-6, maxit=120):
        """Only the probe iterates. The core never moves."""
        Pp, e = P0.copy(), e0
        used_fine = 0
        hist = []
        for it in range(maxit):
            Vloc, X = self.field(l, Pp)
            try:
                u, en, nd, res = self.solve_one(l, n, Vloc, X, e, Pp)
                if nd != n - l - 1:
                    raise RuntimeError('nd')
            except Exception:
                lo_e, hi_e = 4.0 * e if e < 0 else -1.0, 0.15 * e if e < 0 else -1e-4
                got, wp, sc = self.fine(l, n, Vloc, X, Pp, lo_e, hi_e)
                if got is None:
                    return dict(ch=f"{n}{'spdfg'[l]}", ok=False,
                                note=f'no zero at target node count, win_pts={wp}', it=it)
                u, en, nd = got
                used_fine += 1
            if np.sum(u * Pp * self.dr) < 0:
                u = -u
            d = abs(en - e)
            hist.append(round(en, 9))
            Pp = (1 - beta) * Pp + beta * u
            Pp = Pp / np.sqrt(np.sum(Pp ** 2 * self.dr))
            e = (1 - beta) * e + beta * en
            if d < tol and it > 2:
                return dict(ch=f"{n}{'spdfg'[l]}", ok=True, eps=round(float(e), 9),
                            nodes=int(nd), tgt=n - l - 1, it=it, fine_used=used_fine,
                            dlast=float(d), tail=hist[-3:])
        return dict(ch=f"{n}{'spdfg'[l]}", ok=False, note='probe did not converge',
                    eps=round(float(e), 9), it=maxit, fine_used=used_fine, tail=hist[-3:])


def main(mode):
    gate_sha()
    import nlchain as NC
    rows = NC.load()
    cfg = NC.cfg_from_chain(88, rows)
    occ_d = [tuple(t) for t in NC.add(cfg, (6, 2))]
    t0 = time.time()
    h = Frozen(89, occ_d, c=C0)
    E, Ec, it, eps = h.run2()
    sealed6d = float(eps[(6, 2)])
    print(f"  Phi_d* converged: it={it}  sealed eps(6d)={sealed6d:.6f}  {int(time.time()-t0)}s")
    occ_core = [(n, l, q) for n, l, q in occ_d if (n, l) != (6, 2)]
    h.freeze(h.P, occ_core)
    print(f"  core frozen: {len(occ_core)} shells, 6d removed")

    pairs = [(6, 2), (4, 3)] if mode == 'control' else [(6, 2), (6, 3)]
    out = dict(mode=mode, Z=89, sealed_eps_6d=round(sealed6d, 9), core_shells=len(occ_core))
    for n, l in pairs:
        P0 = h.P[(n, l)] if (n, l) in h.P else h.P[(6, 2)]
        e0 = float(eps[(n, l)]) if (n, l) in eps else sealed6d
        r = h.probe(n, l, e0, P0)
        r['sec'] = int(time.time() - t0)
        out[f"{n}{'spdfg'[l]}"] = r
        print(f"  probe {n}{'spdfg'[l]}: {r}")
    a, b = pairs[1], pairs[0]
    ka, kb = f"{a[0]}{'spdfg'[a[1]]}", f"{b[0]}{'spdfg'[b[1]]}"
    if out[ka].get('ok') and out[kb].get('ok'):
        gap = (out[ka]['eps'] - out[kb]['eps']) * 1000.0
        out['gap_mHa'] = round(gap, 4)
        out['ordering_holds'] = bool(gap > 0)
        print(f"  ** {ka} - {kb} = {gap:+.4f} mHa   ORDERING "
              f"{'HOLDS' if gap>0 else 'FAILS'} **")
    json.dump(out, open(OUT.replace('.json', f'_{mode}.json'), 'w'), indent=1)
    return out


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else 'run')
