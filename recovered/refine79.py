#!/usr/bin/env python3
"""refine79.py -- SESSION 79, ITEM 2. THE FIVE CLASS-B CHANNELS AT Z=89, RESOLVED.

DECLARED LINES FROM SEALED pack77/nodespec77.py. Nothing else is changed.
  D1  NSCAN 160 -> NFINE, and the scan is BOUNDED to a neighbourhood of the sealed
      s77 window rather than the whole bound range. Shoot, field and hook: UNCHANGED.
  D2  maxlog is recorded alongside minlog. s77 recorded only the minimum, which for a
      window with log(nrm) < 0 throughout is the FARTHEST point from zero, not the
      nearest. This is F79.1.
  D3  on a sign change the zero is BISECTED and its node count reported.
  D4  TGT IS AN ARGUMENT. Called with tgt = n-l-1 it asks the question; called with
      tgt = nd_returned it is the CAN-FAIL CONTROL, which MUST return C because the
      sealed solver itself found a zero at that node count.

Parent files NOT edited. Prediction sha verified at every invocation; HALTS without it.
usage: python3 refine79.py <ch>          e.g. 6f      -- the question
       python3 refine79.py <ch> control  -- the can-fail control
"""
import os, sys, math, json, time, hashlib

HERE = os.path.dirname(os.path.abspath(__file__))
CACHE = os.path.join(HERE, 'refine79.jsonl')
PRED = os.path.join(HERE, 'PREDICTION-S79-ITEM2-Z89RESOLVE.md')
PSHA = os.path.join(HERE, 'PREDICTION-S79-ITEM2-Z89RESOLVE.sha256')

os.environ.setdefault("SIC_NOCLAMP", "1")
os.environ.setdefault("SUBCELL", "1")
import numpy as np
import hfc2
from t7c_kernel import C0

NFINE = 3000                     # D1
PAD = 3.0                        # window widened by this factor either side

# sealed s77 windows, pack77/nodespec77.jsonl, Z=89
SEALED = {
    '6f': dict(n=6, l=3, win=[-0.037058, -0.019884], nd_ret=3, minlog=-6.5292),
    '7d': dict(n=7, l=2, win=[-0.053839, -0.032719], nd_ret=3, minlog=0.0897),
    '7f': dict(n=7, l=3, win=[-0.028889, -0.013686], nd_ret=4, minlog=-6.0059),
    '8d': dict(n=8, l=2, win=[-0.028889, -0.022521], nd_ret=4, minlog=0.0401),
    '8f': dict(n=8, l=3, win=[-0.017556, -0.015501], nd_ret=5, minlog=-5.4466),
}


def gate_sha():
    """R 1449: the scorer halts unless the filed prediction is intact."""
    want = open(PSHA).read().strip().split()[0]
    got = hashlib.sha256(open(PRED, 'rb').read()).hexdigest()
    if want != got:
        raise SystemExit(f"HALT: prediction sha mismatch\n  filed {want}\n  now   {got}")
    return got


class Refined(Exception):
    def __init__(self, rec):
        self.rec = rec
        super().__init__(f"{rec['Z']} {rec['ch']} CLASS {rec['cls']}")


class Refine(hfc2.HFC):
    """Inert on healthy channels. On nd != n-l-1, measures nd(e) finely and stops."""
    TGT = None                   # D4: set by the driver

    def solve_one(self, l, n, Vloc, X, e0, Pold=None):
        u, e, nd, res = super().solve_one(l, n, Vloc, X, e0, Pold)
        if nd == n - l - 1:
            return u, e, nd, res                      # INERT -- PD-0
        import t7e_probe as P
        cap = dict(l=l, n=n, Vloc=np.array(Vloc, float), X=np.array(X, float), Pold=Pold,
                   r=self.r, x=self.x, h=self.h, dr=self.dr, N=self.npts, c=self.c,
                   srcM=self.srcM, Z=self.Z)
        sh = P.make_shoot(cap)
        ch = f"{n}{'spdfg'[l]}"
        tgt = self.TGT if self.TGT is not None else n - l - 1
        w = SEALED[ch]['win']
        lo_e, hi_e = w[0] * PAD, w[1] / PAD            # D1: bounded neighbourhood
        es = -np.geomspace(abs(lo_e), abs(hi_e), NFINE)

        spec, win = [], []
        for ee in es:
            o = sh(float(ee))
            if o is None:
                continue
            spec.append((float(ee), int(o['nd'])))
            if o['nd'] == tgt:
                win.append((float(ee), math.log(max(o['nrm'], 1e-300))))

        sc = [k for k in range(len(win) - 1) if (win[k][1] > 0) != (win[k + 1][1] > 0)]
        cls = 'A' if not win else ('B' if not sc else 'C')

        zero = None
        if sc:                                          # D3: bisect the first crossing
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
            om = sh(float(0.5 * (a + b)))
            zero = dict(e=round(0.5 * (a + b), 9),
                        nd=(int(om['nd']) if om else None),
                        logn=(round(math.log(max(om['nrm'], 1e-300)), 6) if om else None))

        raise Refined(dict(
            Z=self.Z, ch=ch, n=n, l=l, tgt=tgt, mode=('control' if self.TGT is not None else 'question'),
            nd_returned=int(nd), e_returned=round(float(e), 6), res_returned=round(float(res), 9),
            cls=cls, cls_sealed='B', nfine=NFINE, npts=len(spec),
            scan_e=[round(lo_e, 6), round(hi_e, 6)],
            win_pts=len(win), sign_changes=len(sc),
            minlog=(round(min(v for _, v in win), 4) if win else None),
            maxlog=(round(max(v for _, v in win), 4) if win else None),   # D2
            minlog_sealed=SEALED[ch]['minlog'],
            win_e=([round(min(x for x, _ in win), 6), round(max(x for x, _ in win), 6)]
                   if win else None),
            zero=zero))


def put(rec):
    with open(CACHE, 'a') as f:
        f.write(json.dumps(rec) + '\n')


def run(ch, control=False):
    gate_sha()
    import nlchain as NC
    rows = NC.load()
    s = SEALED[ch]
    cfg = NC.cfg_from_chain(88, rows)
    Refine.TGT = s['nd_ret'] if control else None
    t0 = time.time()
    try:
        Refine(89, [tuple(t) for t in NC.add(cfg, (s['n'], s['l']))], c=C0).run2()
        rec = dict(Z=89, ch=ch, cls='NO-RAISE', note='channel converged')
    except Refined as ex:
        rec = ex.rec
    rec['sec'] = int(time.time() - t0)
    put(rec)
    print(f"  Z=89 {ch} [{rec.get('mode')}] tgt={rec.get('tgt')} -> CLASS {rec['cls']}"
          f"  win={rec.get('win_pts')}/{rec.get('npts')}  sc={rec.get('sign_changes')}")
    print(f"    minlog={rec.get('minlog')} (s77 {rec.get('minlog_sealed')})  "
          f"maxlog={rec.get('maxlog')}  win_e={rec.get('win_e')}")
    print(f"    zero={rec.get('zero')}  e_ret={rec.get('e_returned')} "
          f"res_ret={rec.get('res_returned')}  {rec['sec']}s")
    return rec


if __name__ == "__main__":
    run(sys.argv[1], control=(len(sys.argv) > 2 and sys.argv[2] == 'control'))
