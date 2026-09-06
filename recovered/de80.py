#!/usr/bin/env python3
"""de80.py -- SESSION 80, ITEM 1.  F79.2's REPAIR.

F79.2: the Z=89 margin table compares ONE-ELECTRON EIGENVALUES against TOTAL-ENERGY
DIFFERENCES.  The repair is to obtain the f channels in the currency the ranking is
actually in: dE = E(cfg + channel) - E(ref), E(ref) = -25694.384010 (pack77/o89_89_A.jsonl).

s79's refine79.py PROVED the target-node state exists and located it, then RAISED.
This instrument does the one thing more: it RETURNS that state to the SCF, so the
field can converge on it and a TOTAL ENERGY exists to difference.

DECLARED LINES FROM THE SEALED PATH.  Nothing else is changed.
  G1  hfc2.run2 raises RuntimeError when nd != n-l-1.  Here solve_one intercepts
      BEFORE that raise: on nd != n-l-1 it scans for the zero of log(nrm) carrying
      the TARGET node count and returns it in solve_one's own contract,
      (u/sqrt(nrm), e, nd, |log nrm|).  On nd == n-l-1 it is INERT -- the ruling
      path is bit-for-bit untouched on every healthy channel.
  G2  THE SCAN BOUND IS ADAPTIVE AND DECLARED.  refine79's bounds were the sealed
      s77 windows, which describe the field at ONE iteration; inside a live SCF the
      field moves every iteration.  The window is [SLO,SHI] x |e_returned|,
      geometric, NSCAN points.  F79.1's lesson: an instrument must not report on
      what its own bound admitted as though it reported on the field.  Every
      fallback record therefore carries edge_lo/edge_hi -- whether the found zero
      sat within EDGEFRAC of a scan edge -- and a zero found at an edge is a FLAG,
      not a result.
  G3  WARM START, cost only.  After a channel's first successful fallback the next
      iteration scans NARROW x the previous zero first.  If narrow finds nothing the
      WIDE window runs anyway; the answer is never the narrow window's alone.
  G4  FORCE.  With FORCE set to a channel key the fallback fires on that channel even
      when it is HEALTHY, with tgt = n-l-1.  It must then return the state the
      standard bracket already returns and the SCF must land on the sealed energy.
      This is the can-fail for the FALLBACK PATH ITSELF.
  G5  The ladder is nlguard.LADDER, replicated verbatim; only the class instantiated
      differs.  Node-count failures are NOT retried across rungs -- but under G1 a
      node-count failure can no longer occur on a channel the scan can reach.

usage:
    python3 de80.py control-machinery    # C1: 6d, fallback inert -> sealed E
    python3 de80.py control-fallback     # C2: 6d, fallback FORCED -> same E
    python3 de80.py control-scorer       # C3: both verdicts reachable
    python3 de80.py run 6f|7f|8f         # the question
    python3 de80.py score                # the table, in dE
"""
import os, sys, math, json, time, hashlib

HERE = os.path.dirname(os.path.abspath(__file__))
CACHE = os.path.join(HERE, 'de80.jsonl')
FBLOG = os.path.join(HERE, 'de80_fallback.jsonl')
PRED = os.path.join(HERE, 'PREDICTION-S80-ITEM1-CURRENCY.md')
PSHA = os.path.join(HERE, 'PREDICTION-S80-ITEM1-CURRENCY.sha256')

os.environ.setdefault("SIC_NOCLAMP", "1")
os.environ.setdefault("SUBCELL", "1")
import numpy as np
import hfc2
from t7c_kernel import C0

# ---- sealed comparands, pack77/o89_89_A.jsonl.  READ, never recomputed here.
E_REF = -25694.38401018016
SEALED_E = {'6d': -25694.541630577907, '7p': -25694.509298091765,
            '5f': -25694.41547324462}
NL = {'6f': (6, 3), '7f': (7, 3), '8f': (8, 3), '6d': (6, 2), '7p': (7, 1), '5f': (5, 3)}

NSCAN = 400          # G2
SLO, SHI = 0.20, 8.0  # G2: window = [SLO,SHI] x |e_returned|
NARROW = (0.55, 1.8)  # G3
EDGEFRAC = 0.05      # G2: a zero this close to an edge is flagged


def gate_sha():
    """R 1449: the driver halts unless the filed prediction is intact."""
    want = open(PSHA).read().strip().split()[0]
    got = hashlib.sha256(open(PRED, 'rb').read()).hexdigest()
    if want != got:
        raise SystemExit(f"HALT: prediction sha mismatch\n  filed {want}\n  now   {got}")
    return got


class Fallback(hfc2.HFC):
    """Inert on healthy channels.  On nd != n-l-1, returns the TARGET-node state."""
    FORCE = None          # G4
    LOG = None            # list, appended per fallback firing
    LAST = {}             # G3: channel -> previous zero

    def _scan(self, sh, tgt, lo_e, hi_e, npts):
        es = -np.geomspace(abs(lo_e), abs(hi_e), npts)
        win = []
        for ee in es:
            o = sh(float(ee))
            if o is None:
                continue
            if o['nd'] == tgt:
                win.append((float(ee), math.log(max(o['nrm'], 1e-300))))
        sc = [k for k in range(len(win) - 1) if (win[k][1] > 0) != (win[k + 1][1] > 0)]
        if not sc:
            return None, win
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
        return 0.5 * (a + b), win

    def solve_one(self, l, n, Vloc, X, e0, Pold=None):
        u, e, nd, res = super().solve_one(l, n, Vloc, X, e0, Pold)
        ch = f"{n}{'spdfg'[l]}"
        tgt = n - l - 1
        if nd == tgt and ch != self.FORCE:
            return u, e, nd, res                      # INERT -- ruling path untouched
        import t7e_probe as P
        cap = dict(l=l, n=n, Vloc=np.array(Vloc, float), X=np.array(X, float), Pold=Pold,
                   r=self.r, x=self.x, h=self.h, dr=self.dr, N=self.npts, c=self.c,
                   srcM=self.srcM, Z=self.Z)
        sh = P.make_shoot(cap)

        base = abs(float(e))
        mode = 'wide'
        z = None
        prev = self.LAST.get(ch)
        if prev is not None:                          # G3: narrow first, cost only
            z, win = self._scan(sh, tgt, -NARROW[0] * abs(prev), -NARROW[1] * abs(prev),
                                max(60, NSCAN // 4))
            if z is not None:
                mode = 'narrow'
                lo_e, hi_e = -NARROW[0] * abs(prev), -NARROW[1] * abs(prev)
        if z is None:                                 # G3: wide always available
            lo_e, hi_e = -SLO * base, -SHI * base
            z, win = self._scan(sh, tgt, lo_e, hi_e, NSCAN)
            mode = 'wide'
        if z is None:
            raise RuntimeError(f"Z={self.Z} {ch} FALLBACK FOUND NO TARGET-NODE ZERO "
                               f"in [{lo_e:.6g},{hi_e:.6g}] tgt={tgt} nd={nd}")

        o = sh(float(z))
        span = math.log(abs(hi_e) / abs(lo_e))
        d_lo = math.log(abs(z) / abs(lo_e)) / span
        d_hi = math.log(abs(hi_e) / abs(z)) / span
        if self.LOG is not None:
            self.LOG.append(dict(ch=ch, tgt=tgt, nd_std=int(nd), e_std=round(float(e), 9),
                                 e_fb=round(float(z), 9), nd_fb=int(o['nd']),
                                 logn=round(math.log(max(o['nrm'], 1e-300)), 6),
                                 mode=mode, win_pts=len(win),
                                 scan=[round(lo_e, 8), round(hi_e, 8)],
                                 edge_lo=bool(d_lo < EDGEFRAC), edge_hi=bool(d_hi < EDGEFRAC),
                                 forced=bool(ch == self.FORCE)))
        self.LAST[ch] = z
        nrm = float(o['nrm'])
        return o['u'] / math.sqrt(nrm), float(z), int(o['nd']), abs(math.log(nrm))


def guarded(Z, cfg, force=None):
    """G5: nlguard.LADDER, replicated verbatim.  Only the class differs."""
    import nlguard as NG
    last = None
    for rung, (beta, maxit) in enumerate(NG.LADDER):
        t = time.time()
        Fallback.FORCE = force
        Fallback.LOG = []
        Fallback.LAST = {}
        try:
            E, _, it, eps = Fallback(Z, [tuple(x) for x in cfg], c=C0).run2(
                beta=beta, maxit=maxit)
        except Exception as e:
            return dict(E=None, it=None, beta=beta, rung=rung, conv=False,
                        err=type(e).__name__ + ": " + str(e)[:160],
                        sec=int(time.time() - t), fb=Fallback.LOG)
        if it < maxit:
            return dict(E=float(E), it=it, beta=beta, rung=rung, conv=True, err=None,
                        sec=int(time.time() - t), fb=Fallback.LOG,
                        eps={f"{k[0]}{'spdfg'[k[1]]}": round(float(v), 9)
                             for k, v in eps.items()})
        last = (E, it, beta, maxit)
    E, it, beta, maxit = last
    return dict(E=None, it=it, beta=beta, rung=len(NG.LADDER) - 1, conv=False,
                err="NoConvergence", sec=None, fb=Fallback.LOG)


def put(rec):
    with open(CACHE, 'a') as f:
        f.write(json.dumps(rec) + '\n')


def cfgs(ch):
    import nlchain as NC
    rows = NC.load()
    cfg = NC.cfg_from_chain(88, rows)
    return NC.add(cfg, NL[ch])


def verdict(dE, baseline_dE):
    """G5: BOTH verdicts must be reachable.  Returns the entrant question's answer."""
    return "ENTRANT CHANGES" if dE < baseline_dE else "ROW HOLDS"


def run(ch, force=None, tag=None):
    gate_sha()
    t0 = time.time()
    g = guarded(89, cfgs(ch), force=force)
    dE = None if g['E'] is None else g['E'] - E_REF
    rec = dict(kind=(tag or 'question'), ch=ch, Z=89, forced=force,
               E=g['E'], dE=(None if dE is None else round(dE, 9)),
               it=g['it'], rung=g['rung'], conv=g['conv'], err=g['err'],
               n_fb=len(g['fb']), sec=int(time.time() - t0),
               eps_ch=(g.get('eps') or {}).get(ch),
               edge_flags=sum(1 for f in g['fb'] if f['edge_lo'] or f['edge_hi']),
               fb_first=(g['fb'][0] if g['fb'] else None),
               fb_last=(g['fb'][-1] if g['fb'] else None))
    put(rec)
    with open(FBLOG, 'a') as f:
        for x in g['fb']:
            f.write(json.dumps(dict(kind=rec['kind'], ch=ch, **x)) + '\n')
    print(f"  Z=89 {ch:>3} [{rec['kind']}] E={rec['E']}  dE={rec['dE']}  "
          f"it={rec['it']} rung={rec['rung']} conv={rec['conv']}  "
          f"fb={rec['n_fb']} edge={rec['edge_flags']}  {rec['sec']}s")
    if rec['err']:
        print(f"    err={rec['err']}")
    if rec['fb_last']:
        x = rec['fb_last']
        print(f"    last fallback: e_std={x['e_std']} -> e_fb={x['e_fb']} "
              f"nd {x['nd_std']}->{x['nd_fb']} logn={x['logn']} mode={x['mode']} "
              f"edge=({x['edge_lo']},{x['edge_hi']})")
    return rec


if __name__ == "__main__":
    cmd = sys.argv[1]
    if cmd == 'control-machinery':
        r = run('6d', force=None, tag='C1')
        want = SEALED_E['6d']
        ok = r['E'] is not None and abs(r['E'] - want) < 1e-9
        print(f"  C1 sealed {want}  got {r['E']}  -> {'PASS' if ok else 'FAIL'}")
    elif cmd == 'control-fallback':
        r = run('6d', force='6d', tag='C2')
        want = SEALED_E['6d']
        ok = r['E'] is not None and abs(r['E'] - want) < 1e-6 and r['n_fb'] > 0
        print(f"  C2 sealed {want}  got {r['E']}  fired {r['n_fb']}x  "
              f"-> {'PASS' if ok else 'FAIL'}")
    elif cmd == 'control-scorer':
        gate_sha()
        d6d = SEALED_E['6d'] - E_REF
        d7p = SEALED_E['7p'] - E_REF
        d5f = SEALED_E['5f'] - E_REF
        a = verdict(d6d, d7p)
        b = verdict(d5f, d6d)
        print(f"  C3 direction A: 6d dE={d6d:.6f} vs baseline 7p dE={d7p:.6f} -> {a}")
        print(f"  C3 direction B: 5f dE={d5f:.6f} vs baseline 6d dE={d6d:.6f} -> {b}")
        ok = (a == "ENTRANT CHANGES") and (b == "ROW HOLDS")
        print(f"  C3 both verdicts reachable -> {'PASS' if ok else 'FAIL'}")
    elif cmd == 'run':
        run(sys.argv[2])
    elif cmd == 'score':
        gate_sha()
        import subprocess
        rows = [json.loads(l) for l in open(CACHE)]
        q = {r['ch']: r for r in rows if r['kind'] == 'question'}
        d6d = SEALED_E['6d'] - E_REF
        d7p = SEALED_E['7p'] - E_REF
        m = d7p - d6d
        print(f"  baseline: 6d dE={d6d*1000:.3f} mHa (rank 1), 7p dE={d7p*1000:.3f} mHa "
              f"(rank 2), m(89)={m*1000:.3f} mHa")
        print(f"  {'ch':>4} {'dE (mHa)':>12} {'above 6d':>12} {'above 7p':>12} "
              f"{'x m':>8}  verdict")
        for ch in ('6f', '7f', '8f'):
            if ch not in q or q[ch]['dE'] is None:
                print(f"  {ch:>4}  NOT CONVERGED")
                continue
            d = q[ch]['dE']
            print(f"  {ch:>4} {d*1000:12.3f} {(d-d6d)*1000:12.3f} {(d-d7p)*1000:12.3f} "
                  f"{(d-d7p)/m:8.3f}  {verdict(d, d7p)}")
