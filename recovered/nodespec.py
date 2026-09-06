#!/usr/bin/env python3
"""nodespec.py -- SESSION 66, T-D. THE NODE-COUNT NULL, MEASURED.

M's ruling 3: CLASS A IS TO BE DERIVED, NOT FORCED. So this instrument does not
manufacture an outcome and does not classify by which exception fired. It reports the
NODE SPECTRUM nd(e) across the bound range at the field where the sealed chain
declares the failure, and the class is a consequence of that spectrum:

    CLASS A   tgt never attained anywhere in e<0        -> field carries no such state
    CLASS B   tgt attained, log(nrm) has no zero there  -> s42: the SCF destroys it
    CLASS C   tgt attained, log(nrm) HAS a zero there   -> state present AND findable

Scan geometry (grid, bound range, shoot) is taken UNCHANGED from the sealed
`t7f_rep.NodeGated` so that PD-1 is a receipt against s42's own instrument.

Parent files NOT edited (F44.1 route): hfc2.py, t7c_hfsr.py, t7f_rep.py, nlchain.py
are imported, never modified. Prediction pack66/PREDICTION-T-D.md sha is verified at
every invocation; this driver HALTS without it.

usage:  python3 nodespec.py inert          PD-0
        python3 nodespec.py cells Z [Z..]  the scored cells at those Z
        python3 nodespec.py --show
"""
import os, sys, math, json, time, hashlib

HERE = os.path.dirname(os.path.abspath(__file__))
CACHE = os.path.join(HERE, 'nodespec.jsonl')
PRED = os.path.join(HERE, 'PREDICTION-T-D.md')
PSHA = os.path.join(HERE, 'PREDICTION-T-D.sha256')
BUDGET = 900

os.environ.setdefault("SIC_NOCLAMP", "1")
os.environ.setdefault("SUBCELL", "1")
import numpy as np
import hfc2
from t7c_kernel import C0


def gate_sha():
    """R 1449: the scorer halts unless the filed prediction is intact."""
    want = open(PSHA).read().strip()
    got = hashlib.sha256(open(PRED, 'rb').read()).hexdigest()
    if want != got:
        raise SystemExit(f"HALT: prediction sha mismatch\n  filed {want}\n  now   {got}")
    return got


class NodeSpectrum(Exception):
    def __init__(self, rec):
        self.rec = rec
        super().__init__(f"{rec['Z']} {rec['ch']} CLASS {rec['cls']}")


class NodeSpec(hfc2.HFC):
    """Inert on healthy channels. On nd != tgt, measures nd(e) and stops."""
    NSCAN = 160                      # identical to t7f_rep.NodeGated

    def solve_one(self, l, n, Vloc, X, e0, Pold=None):
        u, e, nd, res = super().solve_one(l, n, Vloc, X, e0, Pold)
        tgt = n - l - 1
        if nd == tgt:
            return u, e, nd, res     # INERT -- PD-0
        import t7e_probe as P
        cap = dict(l=l, n=n, Vloc=np.array(Vloc, float), X=np.array(X, float), Pold=Pold,
                   r=self.r, x=self.x, h=self.h, dr=self.dr, N=self.npts, c=self.c,
                   srcM=self.srcM, Z=self.Z)
        sh = P.make_shoot(cap)
        lo_e, hi_e = -abs(self.Z) ** 2 / 2.0, -1e-5
        es = -np.geomspace(abs(lo_e), abs(hi_e), self.NSCAN)

        spec, win = [], []
        for ee in es:
            o = sh(float(ee))
            if o is None:
                continue
            spec.append((float(ee), int(o['nd'])))
            if o['nd'] == tgt:
                win.append((float(ee), math.log(max(o['nrm'], 1e-300))))

        nds = [s[1] for s in spec]
        sign_changes = sum(1 for k in range(len(win) - 1)
                           if (win[k][1] > 0) != (win[k + 1][1] > 0))
        if not win:
            cls = 'A'
        elif sign_changes == 0:
            cls = 'B'
        else:
            cls = 'C'

        rec = dict(Z=self.Z, ch=f"{n}{'spdfg'[l]}", n=n, l=l, tgt=tgt,
                   nd_returned=int(nd), e_returned=round(float(e), 6),
                   cls=cls, npts=len(spec),
                   nd_max=(max(nds) if nds else None),
                   nd_values=sorted(set(nds)),
                   win_pts=len(win), sign_changes=sign_changes,
                   minlog=(round(min(v for _, v in win), 4) if win else None),
                   win_e=( [round(min(x for x, _ in win), 6),
                            round(max(x for x, _ in win), 6)] if win else None))
        raise NodeSpectrum(rec)


# ------------------------------------------------------------------ cache
def load_cache():
    if not os.path.exists(CACHE):
        return {}
    return {(d['Z'], d['ch']): d for d in map(json.loads, open(CACHE))}


def put(rec):
    tmp = CACHE + '.tmp'
    old = [json.dumps(v) for v in load_cache().values()]
    with open(tmp, 'w') as f:
        f.write('\n'.join(old + [json.dumps(rec)]) + '\n')
    os.replace(tmp, CACHE)


def energy(Z, cfg):
    E, Ec, it, eps = NodeSpec(Z, [tuple(t) for t in cfg], c=C0).run2()
    return E, it


# ------------------------------------------------------------------ PD-0
def inert():
    import nlchain as NC
    rows = NC.load()
    cfg = NC.cfg_from_chain(20, rows)
    t0 = time.time()
    Eref, it0 = energy(21, cfg)
    Eadd, it1 = energy(21, NC.add(cfg, (3, 2)))
    D = Eadd - Eref
    d = abs(D - (-0.26664))
    print(f"PD-0 INERTNESS  Z=21 3d  D={D:.6f}  banked=-0.26664  |d|={d:.2e}  "
          f"it={[it0, it1]}  {int(time.time()-t0)}s")
    print("  ->", "PASS" if d <= 3e-6 else "** FAIL -- T-D DOES NOT RUN **")
    return d <= 3e-6


# ------------------------------------------------------------------ cells
def cells(zs):
    import re
    import nlchain as NC
    rows = NC.load()
    pat = re.compile(r'nodes (\d+)')
    cache = load_cache()
    t_all = time.time()
    for Z in zs:
        cfg = NC.cfg_from_chain(Z - 1, rows)
        targets = []
        for ch, msg in sorted((rows[Z].get('fail') or {}).items()):
            m = pat.search(str(msg))
            if not m:
                continue
            n, l = int(ch[0]), 'spdfg'.index(ch[1])
            if l != 2:
                continue
            targets.append((ch, n, l, n - l - 1, int(m.group(1))))
        for ch, n, l, tgt, got in targets:
            if (Z, ch) in cache:
                print(f"  Z={Z} {ch}: cached"); continue
            t0 = time.time()
            try:
                energy(Z, NC.add(cfg, (n, l)))
                rec = dict(Z=Z, ch=ch, cls='NO-RAISE', tgt=tgt, note='channel converged')
            except NodeSpectrum as ex:
                rec = ex.rec
            except Exception as ex:
                rec = dict(Z=Z, ch=ch, cls='ERR', tgt=tgt,
                           note=type(ex).__name__ + ': ' + str(ex)[:90])
            rec['short_sealed'] = tgt - got
            rec['got_sealed'] = got
            rec['sec'] = int(time.time() - t0)
            rec['driver'] = 'pack66/nodespec.py'
            put(rec)
            print(f"  Z={Z:>3} {ch}  tgt={tgt} short={tgt-got}  -> CLASS {rec['cls']}"
                  f"  nd_max={rec.get('nd_max')}  win={rec.get('win_pts')}"
                  f"  minlog={rec.get('minlog')}  {rec['sec']}s", flush=True)
            if time.time() - t_all > BUDGET:
                print("  OVERRUN -- declared budget spent, segment stops"); return


def show():
    for k, v in sorted(load_cache().items()):
        print(f"  Z={k[0]:>3} {k[1]:>3}  short={v.get('short_sealed')}  "
              f"CLASS {v['cls']}  nd_max={v.get('nd_max')}  minlog={v.get('minlog')}")


if __name__ == '__main__':
    print("prediction sha verified:", gate_sha()[:16], "...")
    a = sys.argv[1:]
    if not a or a[0] == '--show':
        show()
    elif a[0] == 'inert':
        inert()
    elif a[0] == 'cells':
        cells([int(x) for x in a[1:]])
