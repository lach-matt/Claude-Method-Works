#!/usr/bin/env python3
"""a101.py -- S101 ROUTE (a). Prediction pack101/PREDICTION-S101-ROUTEA.md (hashed) gated below.
DERIVED PER-SHELL LAW (both-ways collapse theorem + I-path bookkeeping; U/X projections cancel):
  part_c = q_c [ deps_c/dq - 2 w_cc <dP_c'(Y0(c)/r)P_c> + 2 <dP_c' ownX_c P_c> - SLOTW_c + XSLOTW_c ]
  c != ent: SLOTW_c = J0(c,ent);  XSLOTW_c = sum_k 0.5 c3(l_c,k,l_ent) K^k(c,ent)
  c == ent: SLOTW_c = dceff/dq [ J0(c,c) - kappa sum_k c3 K^k(c,c) ];  XSLOTW_c = 0
Scored per shell against d101-58.json R2_parts (PA1). usage: a101.py ROW"""
import sys, os, json, time, hashlib, numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', 'rt')); os.chdir(os.path.join(HERE, '..', 'rt'))
for nm in ('PREDICTION-S101-ROUTEA.md', 'PREDICTION-S101-ITEM1.md'):
    p = os.path.join(HERE, nm)
    if hashlib.sha256(open(p, 'rb').read()).hexdigest() != open(p + '.sha256').read().split()[0]:
        print("HALT rc=3 sha", nm); sys.exit(3)
import nlchain as NC, hfc2 as H
from t7c_kernel import C0
from t7b_hf import _c3j0sq
sys.path.insert(0, '../pack93'); from ffun93 import solve, pot
assert H.CORR is False
ROW = int(sys.argv[1])
OWN = {58: (5, 2), 90: (6, 2), 91: (6, 2)}; SYS = {58: 'B', 90: 'A', 91: 'A'}
SEALED = {58: +8.0e-5, 90: -5.90e-5, 91: -4.10e-5}
ent = OWN[ROW]; rows = NC.load(); cfg2 = NC.cfg_from_chain(ROW - 2, rows)
Zs = ROW if SYS[ROW] == 'B' else ROW - 1

def setq(cfg, a, q):
    d = {(n, l): qq for n, l, qq in cfg}; d[a] = d.get(a, 0) + q
    return [(n, l, qq) for (n, l), qq in sorted(d.items()) if qq > 1e-9]

t0 = time.time(); sol = {}
for q in (0.4, 0.5, 0.6):
    h, E, rung = solve(Zs, setq(cfg2, ent, q)); sol[q] = h
    print("  solved q=%.1f E=%.8f (%ds)" % (q, E, time.time() - t0), flush=True)
h5, hp, hm = sol[0.5], sol[0.6], sol[0.4]
keys = [(n, l) for n, l, q in h5.occ]; Q5 = {(n, l): q for n, l, q in h5.occ}
r = h5.r; dr = h5.dr
dP = {}; deps = {}
for k in keys:
    Pp, Pm = hp.P[k].copy(), hm.P[k].copy()
    if float(np.sum(Pp * h5.P[k] * dr)) < 0: Pp = -Pp
    if float(np.sum(Pm * h5.P[k] * dr)) < 0: Pm = -Pm
    d = (Pp - Pm) / 0.2; d -= float(np.sum(d * h5.P[k] * dr)) * h5.P[k]
    dP[k] = d; deps[k] = (hp.eps[k] - hm.eps[k]) / 0.2

dceff = (h5._ceff(ent, dict(Q5, **{ent: 0.6})) - h5._ceff(ent, dict(Q5, **{ent: 0.4}))) / 0.2

def J0(a, b): return float(np.sum(h5.P[a]**2 * (h5.Yk(h5.P[b], h5.P[b], 0) / r) * dr))
def Kk(a, b, k): yk = h5.Yk(h5.P[a], h5.P[b], k) / r; return float(np.sum(h5.P[a] * h5.P[b] * yk * dr))

parts = {}; tot = 0.0
for c in keys:
    n, l = c; w_cc = h5._ceff(c, Q5)
    t_eps = deps[c]
    t_dir = -2 * w_cc * float(np.sum(dP[c] * (h5.Yk(h5.P[c], h5.P[c], 0) / r) * h5.P[c] * dr))
    ownX = np.zeros(h5.npts)
    cc = w_cc * (2 * l + 1) / (4 * l + 1)
    if l > 0 and abs(cc) > 1e-14:
        for k in range(2, 2 * l + 1, 2): ownX += cc * _c3j0sq(l, k, l) * h5.Yk(h5.P[c], h5.P[c], k) / r
    t_own = 2 * float(np.sum(dP[c] * ownX * h5.P[c] * dr))
    if c == ent:
        kap = (2 * l + 1) / (4 * l + 1)
        slotw = dceff * (J0(c, c) - kap * sum(_c3j0sq(l, k, l) * Kk(c, c, k) for k in range(2, 2 * l + 1, 2)))
        xslotw = 0.0
    else:
        slotw = J0(c, ent)
        xslotw = sum(0.5 * _c3j0sq(l, k, ent[1]) * Kk(c, ent, k)
                     for k in range(abs(l - ent[1]), l + ent[1] + 1, 2) if _c3j0sq(l, k, ent[1]) > 1e-14)
    pc = Q5[c] * (t_eps + t_dir + t_own - slotw + xslotw)
    parts["%d%s" % (n, 'spdf'[l])] = dict(part=pc, eps=Q5[c] * t_eps, dir=Q5[c] * t_dir, own=Q5[c] * t_own,
                                          slotw=-Q5[c] * slotw, xslotw=Q5[c] * xslotw)
    tot += pc

ref = json.load(open(os.path.join(HERE, 'd101-%d.json' % ROW))) if os.path.exists(os.path.join(HERE, 'd101-%d.json' % ROW)) else None
score = {}
if ref:
    R2p = ref['R2_parts']; ok = 0; nsc = 0
    for k, v in parts.items():
        t = R2p.get(k)
        if t is None: continue
        tol = max(0.15 * abs(t), 4e-6); hit = abs(v['part'] - t) <= tol and (abs(t) <= 1e-5 or np.sign(v['part']) == np.sign(t))
        score[k] = dict(analytic=v['part'], chain=t, diff=v['part'] - t, hit=bool(hit))
        nsc += 1; ok += hit
    print("PA1: %d/%d shells in tolerance; SUM analytic=%+.4e  chain R2=%+.4e  direct R1=%+.4e  sealed=%+.1e"
          % (ok, nsc, tot, ref['R2_chain'], ref['R1_direct'], SEALED[ROW]), flush=True)
else:
    print("SUM analytic=%+.4e  sealed=%+.1e" % (tot, SEALED[ROW]), flush=True)
for k in sorted(parts):
    v = parts[k]; s = score.get(k, {})
    print("  %-4s part=%+.3e chain=%+.3e %s   [eps %+..0e dir %+.0e own %+.0e slotw %+.0e xw %+.0e]".replace('..','.')
          % (k, v['part'], s.get('chain', float('nan')), 'HIT ' if s.get('hit') else 'MISS' if s else '',
             v['eps'], v['dir'], v['own'], v['slotw'], v['xslotw']), flush=True)
json.dump(dict(row=ROW, Z=Zs, total=float(tot), sealed=SEALED[ROW], dceff=float(dceff),
               parts={k: {kk: float(vv) for kk, vv in v.items()} for k, v in parts.items()},
               score={k: {kk: (float(vv) if not isinstance(vv, bool) else vv) for kk, vv in v.items()} for k, v in score.items()},
               sec=int(time.time() - t0)),
          open(os.path.join(HERE, 'a101-%d.json' % ROW), 'w'), indent=1)
