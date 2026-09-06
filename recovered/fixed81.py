#!/usr/bin/env python3
"""fixed81.py -- SESSION 81, ITEM 1.  THE FIXED-FIELD CROSS-CHANNEL COMPARISON AT Z=90.

M's s80 item 3, carried forward.  fixed79.py generalised from Z=89 to Z=90, WITH THE
THREE REPAIRS s79 DID NOT HAVE.  fixed79.py IS NOT REUSED UNPATCHED (M's order).

THE OBJECT.  CLOSE-S78 §3: freeze the field at the converged entrant solution and the
clause-1 inequality reduces to a CROSS-CHANNEL eigenvalue comparison at ONE FIXED FIELD.
At Z=89 the pair was 6f (l=3, 2 nodes, 3rd) against 6d (l=2, 3 nodes, 4th).
AT Z=90 THE PAIR IS THE ROW'S OWN RANK 1 AND RANK 2:
    6d  dE = -0.19094 Ha   rank 1, the entrant
    5f  dE = -0.13689 Ha   rank 2          m(90) = 54.05 mHa
so the fixed-field object here is  eps_2^{l=3} > eps_4^{l=2}  -- 5f has ONE node and 6d
has THREE.  The node counts run the wrong way MORE STRONGLY than at Z=89, so §2's
adverse-Courant-Fischer finding is sharper here, not weaker.

DECLARED CONSTRUCTION.  E1-E5 are fixed79's, unchanged.  E6-E9 are this session's.
  E1  the probe makes no contribution to its own field; the field is built from the
      CORE occupancies alone.
  E2  Vc = 0 for the probe.  fixed79's declared choice, kept, and applied to l=2 and
      l=3 IDENTICALLY so the comparison is like-for-like.
  E3  only the probe orbital iterates; the core Y0 is computed ONCE.
  E4  when solve_one returns the wrong node count, a scan locates the zero of log(nrm)
      carrying the TARGET node count.
  E5  the scan bound is wide (fixed79's amendment): [SLO,SHI] x |e|, NOT 0.15*e.
  E6  **THE ENTRANT'S OCCUPANCY IS REDUCED BY ONE, NOT DELETED.**  fixed79 removed the
      whole (6,2) key, which at Z=89 (6d^1) left a CLOSED [Rn]7s2 core and 89 electrons
      -- correct.  The same deletion at Z=90 (6d^2) would leave 89 electrons for a
      90-electron atom.  The differentiating electron is ONE electron: q -> q-1.
      At Z=89 this is bit-identical to fixed79.  At Z=90 the core carries 6d^1.
  E7  **THE FIELD IS BUILT EXACTLY AS run2 BUILDS IT FOR SHELL a**, with the core
      occupancies in place of Q.  hfc2 run2 line 45 uses _ceff(a,Q) = Q[a]-1 for the
      probe's own shell, which IS the reduced core occupancy of E6, so the direct term
      needs no special case.  The same-shell exchange correction (run2 lines 48-51) is
      applied when the probe's shell is present in the core, from the FROZEN core
      orbital.  CONSEQUENCE, DECLARED: the l=2 probe has a same-shell partner and the
      l=3 probe does not.  That asymmetry is the SCHEME's and is present in the sealed
      dE currency too; it is not introduced here.
  E8  **F80.1.  THE WHOLE TARGET-NODE ZERO SET IS RETURNED, SORTED MOST-BOUND FIRST,
      AND THE SELECTION IS AN EXPLICIT ARGUMENT.  BOTH BRANCHES ARE RUN.**  fixed79's
      fine() took win[sc[0]] -- the first crossing of its own geomspace argument order.
      That is exactly F80.1 and M's order names it.  n_zeros and spread are recorded on
      every firing.
  E9  **F80.2.  THE FROZEN FIELD IS RESTARTED TO STATIONARITY BEFORE IT IS FROZEN.**
      run2 stops on eigenvalue drift; Step 0(ii) is stated on the ENERGY.  A field
      frozen at a still-descending point is not the converged solution.  The reference
      is restarted from its own converged orbitals until |dE| < ESTAT.
  F80.3 IS CARRIED AS A FLOOR, NOT A TOLERANCE: no gap smaller than FLOOR mHa may be
      stated as a verdict, and no figure is quoted finer than the s79 beta-dependence.

usage:
    python3 fixed81.py ref                 # E9: converge + restart ladder, cache
    python3 fixed81.py control             # can-fail: 4f, MUST report ORDERING FAILS
    python3 fixed81.py machinery           # can-fail: 6d probe vs the SCF's own eps(6d)
    python3 fixed81.py run most-bound      # the question, branch 1
    python3 fixed81.py run least-bound     # the question, branch 2
"""
import os, sys, math, json, time, hashlib

HERE = os.path.dirname(os.path.abspath(__file__))
PRED = os.path.join(HERE, 'PREDICTION-S81-ITEM1-Z90FIXED.md')
PSHA = os.path.join(HERE, 'PREDICTION-S81-ITEM1-Z90FIXED.sha256')
REF = os.path.join(HERE, 'fixed81_ref.npz')
REFJ = os.path.join(HERE, 'fixed81_ref.json')
LOG = os.path.join(HERE, 'fixed81.jsonl')

os.environ.setdefault("SIC_NOCLAMP", "1")
os.environ.setdefault("SUBCELL", "1")
sys.path.insert(0, os.getcwd())
import numpy as np
import hfc2
from t7c_kernel import C0
from t7b_hf import _c3j0sq

Z = 90
ZPREV = 89
ENT = (6, 2)                 # the sealed entrant at Z=90
NFINE = 400                  # scan points (de80's NSCAN)
SLO, SHI = 0.20, 8.0         # E5/G2 window, x |e|
FLOOR = 0.035                # mHa.  F80.2's measured stopping resolution.
QUOTE = 0.5                  # mHa.  s79 note 2: beta-dependence of the frozen probe.
ESTAT = 1e-10                # Ha.  E9 stationarity test on the ENERGY.
SEALED = {'6d': -0.19094, '5f': -0.13689, '7p': -0.13206}   # dE, sealed chain row Z=90
M90 = 0.05405                # Ha.  sealed margin at Z=90


def gate_sha():
    """R 1449.  The driver halts unless the filed prediction is intact."""
    want = open(PSHA).read().strip().split()[0]
    got = hashlib.sha256(open(PRED, 'rb').read()).hexdigest()
    if want != got:
        raise SystemExit(f"HALT: prediction sha mismatch\n  filed {want}\n  now   {got}")
    return got


def put(rec):
    with open(LOG, 'a') as f:
        f.write(json.dumps(rec) + '\n')


class Frozen81(hfc2.HFC):
    P0 = None            # E9: restart seed
    EPS0 = None
    SELECT = 'least-bound'

    def seed(self, qtail):
        if self.P0 is None:
            return super().seed(qtail)
        return {k: v.copy() for k, v in self.P0.items()}, dict(self.EPS0)

    # ---- E6/E3: freeze the core at the converged field, entrant q reduced by one
    def freeze(self, P, cQ):
        self.cP = {k: P[k].copy() for k in cQ}
        self.cQ = dict(cQ)
        self.cY0 = {k: self.Yk(self.cP[k], self.cP[k], 0) for k in self.cP}

    # ---- E1/E2/E7: the field run2 would build for shell a, from core occupancies
    def field(self, n, l, Pp):
        r = self.r
        a = (n, l)
        Vloc = -self.Z / r + sum(self.cQ[b] * self.cY0[b] / r for b in self.cP)
        if a in self.cP:                                  # E7: same-shell exchange
            c = self.cQ[a] * (2 * l + 1) / (4 * l + 1)
            if abs(c) > 1e-14:
                for k in range(2, 2 * l + 1, 2):
                    Vloc = Vloc - c * _c3j0sq(l, k, l) * self.Yk(self.cP[a], self.cP[a], k) / r
        X = np.zeros(self.npts)
        for b in self.cP:
            if b == a:
                continue
            nb, lb = b
            for k in range(abs(l - lb), l + lb + 1, 2):
                X = X + 0.5 * self.cQ[b] * _c3j0sq(l, k, lb) * self.Yk(Pp, self.cP[b], k) / r * self.cP[b]
        return Vloc, X

    # ---- E8 (F80.1): every crossing bisected; the whole zero set returned
    def _bisect(self, sh, a, b, fa):
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
        return 0.5 * (a + b)

    def fine(self, l, n, Vloc, X, Pold, lo_e, hi_e):
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
            return None, dict(win_pts=len(win), n_zeros=0)
        zs = sorted(self._bisect(sh, win[k][0], win[k + 1][0], win[k][1]) for k in sc)
        z = zs[0] if self.SELECT == 'most-bound' else zs[-1]      # E8: declared
        o = sh(float(z))
        u = o['u'] / math.sqrt(o['nrm'])
        meta = dict(win_pts=len(win), n_zeros=len(zs), select=self.SELECT,
                    zeros=[round(v, 9) for v in zs],
                    spread=(round((zs[-1] - zs[0]) * 1000, 4) if len(zs) > 1 else 0.0),
                    scan=[round(lo_e, 8), round(hi_e, 8)])
        return (u, z, int(o['nd'])), meta

    def probe(self, n, l, e0, Pstart, beta=0.4, tol=2e-6, maxit=120):
        Pp, e = Pstart.copy(), float(e0)
        used_fine, fb = 0, []
        hist = []
        for it in range(maxit):
            Vloc, X = self.field(n, l, Pp)
            try:
                u, en, nd, res = self.solve_one(l, n, Vloc, X, e, Pp)
                if nd != n - l - 1:
                    raise RuntimeError('nd')
            except Exception:
                lo_e, hi_e = -SLO * abs(e), -SHI * abs(e)
                got, meta = self.fine(l, n, Vloc, X, Pp, lo_e, hi_e)
                meta['it'] = it
                fb.append(meta)
                if got is None:
                    return dict(ch=f"{n}{'spdfg'[l]}", ok=False, select=self.SELECT,
                                note='no zero at target node count', it=it, fb=fb)
                u, en, nd = got
                used_fine += 1
            if np.sum(u * Pp * self.dr) < 0:
                u = -u
            d = abs(en - e)
            hist.append(round(float(en), 9))
            Pp = (1 - beta) * Pp + beta * u
            Pp = Pp / np.sqrt(np.sum(Pp ** 2 * self.dr))
            e = (1 - beta) * e + beta * en
            if d < tol and it > 2:
                return dict(ch=f"{n}{'spdfg'[l]}", ok=True, select=self.SELECT,
                            eps=round(float(e), 9), nodes=int(nd), tgt=n - l - 1,
                            it=it, fine_used=used_fine, dlast=float(d),
                            tail=hist[-3:], fb=fb)
        return dict(ch=f"{n}{'spdfg'[l]}", ok=False, select=self.SELECT,
                    note='probe did not converge', eps=round(float(e), 9),
                    it=maxit, fine_used=used_fine, tail=hist[-3:], fb=fb)


# ---------------------------------------------------------------- reference
def cfg90():
    import nlchain as NC
    rows = NC.load()
    return [tuple(t) for t in NC.add(NC.cfg_from_chain(ZPREV, rows), ENT)]


def build_ref():
    """E9: converge, then restart to stationarity on the ENERGY.  Cache."""
    t0 = time.time()
    cfg = cfg90()
    h = Frozen81(Z, cfg, c=C0)
    Frozen81.P0 = None
    E, Ec, it, eps = h.run2()
    ladder = [float(E)]
    for k in range(12):
        Frozen81.P0, Frozen81.EPS0 = h.P, h.eps
        h2 = Frozen81(Z, cfg, c=C0)
        E2, _, it2, eps2 = h2.run2()
        ladder.append(float(E2))
        h, eps = h2, eps2
        done = abs(float(E2) - E) < ESTAT
        E = float(E2)
        if done:
            break
    Frozen81.P0 = None
    np.savez(REF, **{f"{n}_{l}": h.P[(n, l)] for (n, l) in h.P})
    out = dict(Z=Z, cfg=[list(x) for x in cfg], E=float(E), ladder=ladder,
               drop_mHa=round((ladder[-1] - ladder[0]) * 1000, 6),
               passes=len(ladder) - 1,
               eps={f"{n}{'spdfg'[l]}": round(float(v), 9) for (n, l), v in eps.items()},
               it=it, sec=int(time.time() - t0))
    json.dump(out, open(REFJ, 'w'), indent=1)
    print(f"  REF Z=90 E={E:.9f}  passes={out['passes']}  drop={out['drop_mHa']:+.6f} mHa"
          f"  {out['sec']}s")
    print(f"  ladder {[round(v,9) for v in ladder]}")
    print(f"  eps(6d)={out['eps'].get('6d')}  eps(7s)={out['eps'].get('7s')}")
    return out


def load_ref():
    cfg = cfg90()
    d = np.load(REF)
    P = {tuple(int(v) for v in k.split('_')): d[k] for k in d.files}
    meta = json.load(open(REFJ))
    cQ = {}
    for (n, l, q) in cfg:
        q2 = q - 1 if (n, l) == ENT else q
        if q2 > 0:
            cQ[(n, l)] = float(q2)
    h = Frozen81(Z, cfg, c=C0)
    h.freeze(P, cQ)
    h.P = P
    return h, meta, cfg


def run_pair(pairs, select, tag):
    gate_sha()
    t0 = time.time()
    h, meta, cfg = load_ref()
    Frozen81.SELECT = select
    h.SELECT = select
    out = dict(tag=tag, Z=Z, select=select, E_ref=meta['E'],
               core=[[k[0], k[1], q] for k, q in h.cQ.items()])
    print(f"  core: {len(h.cQ)} shells, entrant {ENT[0]}{'spdfg'[ENT[1]]} reduced to "
          f"q={h.cQ.get(ENT)}")
    for (n, l) in pairs:
        key = (n, l)
        Pstart = h.P[key] if key in h.P else h.P[ENT]
        e0 = meta['eps'].get(f"{n}{'spdfg'[l]}", meta['eps']['6d'])
        r = h.probe(n, l, e0, Pstart)
        r['sec'] = int(time.time() - t0)
        out[f"{n}{'spdfg'[l]}"] = r
        print(f"  probe {n}{'spdfg'[l]}: ok={r.get('ok')} eps={r.get('eps')} "
              f"fine={r.get('fine_used')} it={r.get('it')} nz="
              f"{[m['n_zeros'] for m in r.get('fb', [])]}")
    a, b = pairs[1], pairs[0]
    ka, kb = f"{a[0]}{'spdfg'[a[1]]}", f"{b[0]}{'spdfg'[b[1]]}"
    if out[ka].get('ok') and out[kb].get('ok'):
        gap = (out[ka]['eps'] - out[kb]['eps']) * 1000.0
        out['gap_mHa'] = round(gap, 4)
        out['ordering_holds'] = bool(gap > 0)
        out['above_floor'] = bool(abs(gap) > FLOOR)
        print(f"  ** {ka} - {kb} = {gap:+.4f} mHa   ORDERING "
              f"{'HOLDS' if gap>0 else 'FAILS'}   "
              f"{'ABOVE' if abs(gap)>FLOOR else 'BELOW'} the {FLOOR} mHa floor **")
    json.dump(out, open(os.path.join(HERE, f"fixed81_{tag}.json"), 'w'), indent=1)
    put(out)
    return out


def machinery():
    """CAN-FAIL: the l=2 probe in the frozen field must return the SCF's own eps(6d).
    E6+E7 make this a real test -- at Z=90 the core carries 6d^1 and the probe is the
    SECOND 6d electron, which is exactly what run2's _ceff(a,Q)=1 describes."""
    gate_sha()
    h, meta, cfg = load_ref()
    h.SELECT = 'least-bound'
    r = h.probe(*ENT, meta['eps']['6d'], h.P[ENT])
    d = (r['eps'] - meta['eps']['6d']) * 1000 if r.get('ok') else None
    print(f"  MACHINERY: probe eps(6d)={r.get('eps')}  SCF eps(6d)={meta['eps']['6d']}"
          f"  diff={d if d is None else round(d,4)} mHa")
    rec = dict(tag='machinery', probe=r, scf_eps_6d=meta['eps']['6d'],
               diff_mHa=(None if d is None else round(d, 4)))
    json.dump(rec, open(os.path.join(HERE, 'fixed81_machinery.json'), 'w'), indent=1)
    put(rec)
    return rec


if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else 'ref'
    if cmd == 'ref':
        build_ref()
    elif cmd == 'machinery':
        machinery()
    elif cmd == 'control':
        run_pair([(6, 2), (4, 3)], 'least-bound', 'control')
    elif cmd == 'run':
        sel = sys.argv[2] if len(sys.argv) > 2 else 'least-bound'
        run_pair([(6, 2), (5, 3)], sel, f"run_{sel}")
    else:
        raise SystemExit(f"unknown cmd {cmd}")
