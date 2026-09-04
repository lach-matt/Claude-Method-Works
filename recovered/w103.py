#!/usr/bin/env python3
"""w103.py -- S103 ITEM 2 (amended per RULING-M-S102-POST-SEAL). Prediction pack103/PREDICTION-S103-ITEM2.md
(2542083a) hashed BEFORE this file. defect(q) = dE_SCF/dq - g(q) at the ts93 5pt Gauss nodes.
g READ FROM SEALED ts93-*-5pt receipts. Stencils: central Richardson h=0.2/0.1 at nodes 2-5;
5-pt one-sided forward O(h^4) h=0.1 at node 1 (q=0.04691). usage: w103.py ROW   ROW in {58,90,91}"""
import sys, os, json, time, hashlib, numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', 'rt')); os.chdir(os.path.join(HERE, '..', 'rt'))
PRED = os.path.join(HERE, 'PREDICTION-S103-ITEM2.md')
want = open(PRED + '.sha256').read().split()[0]
got = hashlib.sha256(open(PRED, 'rb').read()).hexdigest()
if want != got: print("HALT rc=3 sha"); sys.exit(3)
import nlchain as NC, hfc2 as H
sys.path.insert(0, '../pack93'); from ffun93 import solve, clone, Ione, Efun
assert H.CORR is False
ROW = int(sys.argv[1])
OWN = {58: (5, 2), 90: (6, 2), 91: (6, 2)}
SYS = {58: 'B', 90: 'A', 91: 'A'}
a = OWN[ROW]; rows = NC.load()
cfg2 = NC.cfg_from_chain(ROW - 2, rows)
Zs = ROW if SYS[ROW] == 'B' else ROW - 1

def setq(cfg, aa, q):
    d = {(n, l): qq for n, l, qq in cfg}; d[aa] = d.get(aa, 0) + q
    return [(n, l, qq) for (n, l), qq in sorted(d.items()) if qq > 1e-9]

# sealed exposure receipts
ts = json.load(open(f'../pack93/ts93-{ROW}-5pt.json'))
s = ts['sys_fail'] if (ts.get('fail') == SYS[ROW]) else ts['sys'][SYS[ROW]]
assert s['Z'] == Zs, (s['Z'], Zs)
NODES = s['nodes']; G = s['g']; QUAD = s['quad']; D = s['D']; T1 = s['T1']
_x, _w = np.polynomial.legendre.leggauss(5); W = list(0.5 * _w)

# grid of required solves
need = set()
for i, qn in enumerate(NODES):
    if i == 0: [need.add(round(qn + j * 0.1, 6)) for j in range(5)]
    else: [need.add(round(qn + d_, 6)) for d_ in (-0.2, -0.1, 0.1, 0.2)]
need.add(0.5)
t0 = time.time(); E = {}
for q in sorted(need):
    h, e, r = solve(Zs, setq(cfg2, a, q)); E[q] = e
    if abs(q - 0.5) < 1e-9: h5 = h
    print("  solved q=%.6f E=%.8f rung=%d (%ds)" % (q, e, r, time.time() - t0), flush=True)

def dEdq(i, qn):
    if i == 0:
        f = [E[round(qn + j * 0.1, 6)] for j in range(5)]
        return (-25*f[0] + 48*f[1] - 36*f[2] + 16*f[3] - 3*f[4]) / (12 * 0.1)
    d1 = (E[round(qn + 0.1, 6)] - E[round(qn - 0.1, 6)]) / 0.2
    d2 = (E[round(qn + 0.2, 6)] - E[round(qn - 0.2, 6)]) / 0.4
    return (4 * d1 - d2) / 3

# own g_frozen at midpoint, cross-check only
I5 = Ione(h5); Q5 = {(n, l): q for n, l, q in h5.occ}
def E_at(qv):
    occ = [(n, l, (qv if (n, l) == a else qq)) for n, l, qq in h5.occ]
    return Efun(clone(h5, h5.Z, occ), I5)
g5_own = (E_at(Q5[a] + 1e-3) - E_at(Q5[a] - 1e-3)) / 2e-3

DEF = []
for i, qn in enumerate(NODES):
    d_ = dEdq(i, qn); DEF.append(d_ - G[i])
    print("  node q=%.6f dE/dq=%.8f g_sealed=%.8f defect=%+.3e" % (qn, d_, G[i], DEF[i]), flush=True)
SUM = float(sum(w * x for w, x in zip(W, DEF)))
out = dict(row=ROW, system=SYS[ROW], Z=Zs, shell="%d%s" % (a[0], "spdf"[a[1]]),
           nodes=NODES, g_sealed=G, dEdq=[float(dEdq(i, q)) for i, q in enumerate(NODES)],
           defect=[float(x) for x in DEF], gauss_sum=SUM, neg_T1=float(-T1), quad=QUAD, D=D,
           sum_vs_negT1=float(SUM - (-T1)), mid_defect=float(DEF[2]),
           g5_own=float(g5_own), g5_sealed=float(G[2]), g5_drift=float(g5_own - G[2]),
           all_nodes_positive=bool(all(x > 0 for x in DEF)),
           any_node_below_noise=bool(any(x < -2e-5 for x in DEF)), sec=int(time.time() - t0))
json.dump(out, open(os.path.join(HERE, 'w103-%d.json' % ROW), 'w'), indent=1)
print("ROW %d sys %s: SUM=%+.3e  -T1=%+.3e  diff=%+.2e  mid=%+.3e  all_pos=%s  g5_drift=%+.1e"
      % (ROW, SYS[ROW], SUM, -T1, SUM - (-T1), DEF[2], out['all_nodes_positive'], out['g5_drift']), flush=True)