#!/usr/bin/env python3
"""conf82.py -- SESSION 82, ITEM 4.  R81.6: 7d AND 8d AT THE **CONVERGED** FIELD.

de81 searched the field at the iteration where de80's fallback fires.  M ruled (R81.6)
that the four refusals stay CLASS B until the search is repeated against the CONVERGED
field.  For 7d and 8d no converged SCF exists -- the channel the SCF needs is the one
being searched for -- so the converged field is borrowed from the row that DOES converge.

DECLARED LINES:
  P1  **fixed81 IS IMPORTED UNMODIFIED.**  Nothing is written into pack80 or pack81.
      The precedent is de81 importing de80.  Frozen81 is used at Z=89 with cfg88+6d.
  P2  **RESTART TO STATIONARITY, BOTH THE REFERENCE AND EVERY PROBE (R81.2).**
  P3  **THE MEASUREMENT IS A NODE CENSUS, NOT A TARGET-NODE HIT.**  nd is recorded at
      EVERY scan energy.  de81 asked "is there a 4-node zero"; this asks "what node
      counts exist at all", which distinguishes a ladder that terminates from a counter
      that does.
  P4  **THE FROZEN FIELD IS FROZEN ONLY IN ITS LOCAL PART.**  field(n,l,Pp)'s exchange
      term depends on the probe orbital Pp.  The census fixes Pp at the converged 6d
      orbital and DECLARES it.  The can-fail (Y1) is what tests whether that choice can
      still recover a known state; it is not assumed to be harmless.
  P5  **THE GRID IS MEASURED, NOT ASSUMED.**  r_max, npts and the 6d orbital's outer
      amplitude are reported, because H2 -- that the grid cannot represent a Rydberg d
      state -- is a filed hypothesis and must be decidable from this instrument's own
      output.
  P6  R82.1 does not bind here: this is not a corpus scanner.  Its controls are physical.

usage:  python3 conf82.py ref        # converge + stationarise cfg88+6d, cache, grid report
        python3 conf82.py census l n # node census for channel (n,l) at the converged field
        python3 conf82.py all        # ref, then 6d control, then 7d, then 8d
"""
import os, sys, math, json, time, hashlib

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
PRED = os.path.join(HERE, 'PREDICTION-S82-ITEM4-CONVERGED-FIELD.md')
PSHA = os.path.join(HERE, 'PREDICTION-S82-ITEM4-CONVERGED-FIELD.sha256')
LOG = os.path.join(HERE, 'conf82.jsonl')
REFJ = os.path.join(HERE, 'conf82_ref.json')
REFP = os.path.join(HERE, 'conf82_ref.npz')

os.environ.setdefault("SIC_NOCLAMP", "1")
os.environ.setdefault("SUBCELL", "1")
sys.path.insert(0, os.getcwd())
sys.path.insert(0, os.path.join(ROOT, 'pack81'))
import numpy as np
import hfc2
import fixed81 as FX                     # P1: imported unmodified
from t7c_kernel import C0

Z, ZPREV, ENT = 89, 88, (6, 2)
ESTAT = 1e-10
NREST = 12
# the de81 window, in Ha.  Shallow bound is the -2e-4 the project adopted at s79.
WLO, WHI = 2.0e-4, 0.700
NSCAN = 1200


def gate_sha():
    want = open(PSHA).read().split()[0]
    got = hashlib.sha256(open(PRED, 'rb').read()).hexdigest()
    if want != got:
        raise SystemExit(f"HALT: prediction sha mismatch\n filed {want}\n now   {got}")


def put(rec):
    with open(LOG, 'a') as f:
        f.write(json.dumps(rec) + '\n')


def cfg89():
    import nlchain as NC
    rows = NC.load()
    return [tuple(t) for t in NC.add(NC.cfg_from_chain(ZPREV, rows), ENT)]


def build_ref():
    """P2: converge cfg88+6d and restart to stationarity.  P5: measure the grid."""
    gate_sha()
    t0 = time.time()
    cfg = cfg89()
    FX.Frozen81.P0 = None
    h = FX.Frozen81(Z, cfg, c=C0)
    E, Ec, it, eps = h.run2()
    ladder = [float(E)]
    for k in range(NREST):
        FX.Frozen81.P0, FX.Frozen81.EPS0 = h.P, h.eps
        h2 = FX.Frozen81(Z, cfg, c=C0)
        E2, _, it2, eps2 = h2.run2()
        ladder.append(float(E2))
        h, eps = h2, eps2
        done = abs(float(E2) - E) < ESTAT
        E = float(E2)
        if done:
            break
    FX.Frozen81.P0 = None

    # ---- P5: the grid, measured
    r = h.r
    P6d = h.P[ENT]
    amp = np.abs(P6d)
    pk = float(amp.max())
    # outermost radius where |P| still exceeds 1e-6 of its peak
    idx = np.nonzero(amp > 1e-6 * pk)[0]
    r_outer = float(r[idx[-1]]) if len(idx) else 0.0
    # <r> of the 6d orbital
    rmean = float(np.sum(P6d ** 2 * r * h.dr) / np.sum(P6d ** 2 * h.dr))
    # tail amplitude at the grid edge, as a fraction of peak
    edge_frac = float(amp[-1] / pk)

    np.savez(REFP, **{f"{n}_{l}": h.P[(n, l)] for (n, l) in h.P})
    out = dict(Z=Z, cfg=[list(x) for x in cfg], E=float(E), ladder=ladder,
               offset_mHa=round((ladder[-1] - ladder[0]) * 1000, 6),   # SIGNED (R81.7)
               passes=len(ladder) - 1,
               eps={f"{n}{'spdfg'[l]}": round(float(v), 9) for (n, l), v in eps.items()},
               grid=dict(npts=int(h.npts), r_min=float(r[0]), r_max=float(r[-1]),
                         r6d_outer_1e6=round(r_outer, 4), r6d_mean=round(rmean, 4),
                         edge_amp_frac=edge_frac),
               it=it, sec=int(time.time() - t0))
    json.dump(out, open(REFJ, 'w'), indent=1)
    put(dict(kind='ref', **{k: out[k] for k in ('E', 'offset_mHa', 'passes', 'grid')}))
    print(f"  REF Z=89 E={E:.9f}  passes={out['passes']}  "
          f"restart offset={out['offset_mHa']:+.6f} mHa (SIGNED)")
    print(f"  eps(6d) = {out['eps'].get('6d')}")
    g = out['grid']
    print(f"  GRID  npts={g['npts']}  r_max={g['r_max']:.3f} a0  "
          f"r_min={g['r_min']:.3e}")
    print(f"  6d orbital: <r>={g['r6d_mean']:.3f} a0 · outer(1e-6 of peak)="
          f"{g['r6d_outer_1e6']:.3f} a0 · amplitude at grid edge="
          f"{g['edge_amp_frac']:.3e} of peak")
    print(f"  **H2 TEST: a 7d Rydberg state has <r> ~ 80 a0. r_max = {g['r_max']:.1f} a0.**")
    return out


def _frozen(h_cfg):
    """E6/E7: core frozen at the converged field, entrant occupancy reduced by one."""
    cfg = cfg89()
    dat = np.load(REFP)
    P = {}
    for k in dat.files:
        n, l = k.split('_')
        P[(int(n), int(l))] = dat[k]
    cQ = {}
    for (n, l, q) in [(t[0], t[1], t[2]) for t in cfg]:
        cQ[(n, l)] = q
    cQ[ENT] = cQ[ENT] - 1                       # E6
    h = FX.Frozen81(Z, cfg, c=C0)
    h.freeze(P, cQ)
    return h, P


def census(l, n):
    """P3: node count at EVERY scan energy in the de81 window, at the CONVERGED field."""
    gate_sha()
    t0 = time.time()
    ref = json.load(open(REFJ))
    h, P = _frozen(None)
    import t7e_probe as PR
    Pp = P[ENT]                                  # P4: exchange fixed at converged 6d
    Vloc, X = h.field(n, l, Pp)
    cap = dict(l=l, n=n, Vloc=np.array(Vloc, float), X=np.array(X, float), Pold=Pp,
               r=h.r, x=h.x, h=h.h, dr=h.dr, N=h.npts, c=h.c, srcM=h.srcM, Z=h.Z)
    sh = PR.make_shoot(cap)
    tgt = n - l - 1
    es = -np.geomspace(WHI, WLO, NSCAN)          # deep -> shallow
    hist, seen, prev, mono = [], {}, None, True
    for ee in es:
        o = sh(float(ee))
        if o is None:
            continue
        nd = int(o['nd'])
        seen[nd] = seen.get(nd, 0) + 1
        if prev is not None and nd < prev:
            mono = False
        prev = nd
        hist.append((float(ee), nd, math.log(max(o['nrm'], 1e-300))))

    # target-node zeros, exactly as fine() does, but reported not selected
    win = [(e, f) for (e, nd, f) in hist if nd == tgt]
    sc = [k for k in range(len(win) - 1) if (win[k][1] > 0) != (win[k + 1][1] > 0)]
    zs = sorted(h._bisect(sh, win[k][0], win[k + 1][0], win[k][1]) for k in sc)

    ch = f"{n}{'spdfg'[l]}"
    rec = dict(kind='census', ch=ch, l=l, n=n, tgt=tgt,
               window=[-WHI, -WLO], nscan=NSCAN, pts=len(hist),
               nd_seen={str(k): v for k, v in sorted(seen.items())},
               nd_min=(min(seen) if seen else None), nd_max=(max(seen) if seen else None),
               monotone=mono, tgt_pts=len(win), n_zeros=len(zs),
               zeros=[round(v, 9) for v in zs], sec=int(time.time() - t0))
    put(rec)
    print(f"  {ch}: target nodes {tgt} · scanned {len(hist)}/{NSCAN} pts over "
          f"[{-WHI}, {-WLO}] Ha")
    print(f"      node counts present : {rec['nd_seen']}")
    print(f"      monotone in E       : {mono}")
    print(f"      points at target nd : {len(win)}")
    print(f"      target-node zeros   : {len(zs)}  {rec['zeros'] if zs else ''}")
    if zs and ch == '6d':
        e_scf = ref['eps'].get('6d')
        d = (zs[-1] - e_scf) * 1000
        print(f"      **Y1 CONTROL: census zero {zs[-1]:.9f} vs SCF eps(6d) {e_scf} "
              f"-> {d:+.6f} mHa**")
        rec['y1_diff_mHa'] = round(d, 6)
        put(dict(kind='y1', diff_mHa=round(d, 6), census=zs[-1], scf=e_scf))
    return rec


if __name__ == '__main__':
    a = sys.argv[1:]
    if not a:
        print(__doc__)
    elif a[0] == 'ref':
        build_ref()
    elif a[0] == 'census':
        census(int(a[1]), int(a[2]))
    elif a[0] == 'all':
        if not os.path.exists(REFJ):
            build_ref()
        print("\n=== Y1 CONTROL: 6d at the converged field ===")
        census(2, 6)
        for nn in (7, 8):
            print(f"\n=== QUESTION: {nn}d at the converged field ===")
            census(2, nn)
    else:
        print(__doc__)
