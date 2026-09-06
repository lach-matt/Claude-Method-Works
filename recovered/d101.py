#!/usr/bin/env python3
"""d101.py -- S101 ITEM 1 (G5b). Prediction pack101/PREDICTION-S101-ITEM1.md (56c319fc) hashed BEFORE this file.
Object: defect(q) = dE_SCF/dq - g(q) at the fractional-q midpoint, and its derived reduction to the
G1 content projection  R3 = + sum_a 2 q_a int (sqrt(M_a)-1) X_a (dP_a/dq) dr
(F_shoot P = eps P exact on the path; F_shoot - F_Efun = -(sqrt(M)-1) X per s100 G1 T1; T2 slot content
term-matched to -1.16e-7, negligible at the 1e-5 band).
Rungs: R1 direct = Richardson(h=0.2,0.1) dE_SCF/dq - g(0.5)   [in-run reproduction of the sealed measurement]
       R2 chain  = d/dq Efun[Q(0.5); P(q)] at fixed Q          [chain-rule identity check vs R1]
       R3 proj   = the derived G1-content projection            [the SCORED object, Rule B]
Controls: --canfail Z (D set to zero: R3 must land OUTSIDE the window; non-vacuous lever)
usage: d101.py ROW [--canfail Z]     ROW in {58, 90, 91}; system B for 58, A for 90/91 (the failing systems)"""
import sys, os, json, time, hashlib, numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', 'rt')); os.chdir(os.path.join(HERE, '..', 'rt'))
PRED = os.path.join(HERE, 'PREDICTION-S101-ITEM1.md')
want = open(PRED + '.sha256').read().split()[0]
got = hashlib.sha256(open(PRED, 'rb').read()).hexdigest()
if want != got: print("HALT rc=3 sha"); sys.exit(3)
import nlchain as NC, hfc2 as H
from t7c_kernel import C0
sys.path.insert(0, '../pack93'); from ffun93 import solve, clone, Ione, Efun, pot
assert H.CORR is False
c = C0
ROW = int(sys.argv[1]); cf = sys.argv[sys.argv.index('--canfail') + 1] if '--canfail' in sys.argv else None
OWN = {58: (5, 2), 90: (6, 2), 91: (6, 2)}
SYS = {58: 'B', 90: 'A', 91: 'A'}          # the failing system per sealed receipts
SEALED = {58: +8.0e-5, 90: -5.90e-5, 91: -4.10e-5}
a = OWN[ROW]; rows = NC.load()
cfg2 = NC.cfg_from_chain(ROW - 2, rows)
Zs = ROW if SYS[ROW] == 'B' else ROW - 1    # A=(Zs-1,cfg2), B=(Zs,cfg2) as ts93

def setq(cfg, a, q):
    d = {(n, l): qq for n, l, qq in cfg}; d[a] = d.get(a, 0) + q
    return [(n, l, qq) for (n, l), qq in sorted(d.items()) if qq > 1e-9]

t0 = time.time(); sol = {}
for q in (0.3, 0.4, 0.5, 0.6, 0.7):
    h, E, r = sol[q] = solve(Zs, setq(cfg2, a, q)) if False else (None, None, None)
# foreground, sequential, receipts printed per solve (Zeno: visible progress, no detached jobs)
for q in (0.3, 0.4, 0.5, 0.6, 0.7):
    h, E, rung = solve(Zs, setq(cfg2, a, q)); sol[q] = (h, E, rung)
    print("  solved q=%.1f E=%.8f rung=%d (%ds)" % (q, E, rung, time.time() - t0), flush=True)
h5, E5, _ = sol[0.5]

# R1: direct defect. Richardson: D'(h) = (E(q+h)-E(q-h))/2h; R = (4 D'(0.1) - D'(0.2)) / 3
d1 = (sol[0.6][1] - sol[0.4][1]) / 0.2
d2 = (sol[0.7][1] - sol[0.3][1]) / 0.4
dE_rich = (4 * d1 - d2) / 3
I5 = Ione(h5); Q5 = {(n, l): q for n, l, q in h5.occ}
def g_frozen(dq=1e-3):
    def E_at(qv):
        occ = [(n, l, (qv if (n, l) == a else qq)) for n, l, qq in h5.occ]
        return Efun(clone(h5, h5.Z, occ), I5)
    return (E_at(Q5[a] + dq) - E_at(Q5[a] - dq)) / (2 * dq)
g5 = g_frozen()
R1 = dE_rich - g5

# orbital path derivative dP/dq per shell (central, h=0.1), sign-aligned, norm-projected
hp, hm = sol[0.6][0], sol[0.4][0]
keys = [(n, l) for n, l, q in h5.occ]; dr = h5.dr
dP = {}
for k in keys:
    Pp = hp.P[k] if k in hp.P else None; Pm = hm.P[k] if k in hm.P else None
    if Pp is None or Pm is None: dP[k] = np.zeros(h5.npts); continue
    if float(np.sum(Pp * h5.P[k] * dr)) < 0: Pp = -Pp
    if float(np.sum(Pm * h5.P[k] * dr)) < 0: Pm = -Pm
    d = (Pp - Pm) / 0.2
    d = d - float(np.sum(d * h5.P[k] * dr)) * h5.P[k]      # kill norm drift; <dP,P>=0
    dP[k] = d

# R2: chain defect = d/dq Efun[Q(0.5); P(q)] at fixed occupancy (orbital path only)
def E_orb(hh):
    g = clone(hh, h5.Z, list(h5.occ))                       # occupancy fixed at q=0.5 occ; orbitals from hh
    return Efun(g, I5)
R2 = (E_orb(hp) - E_orb(hm)) / 0.2

# R3: derived projection.  M_a = 1 + (eps_a - Vdir)/(2 c^2); Vdir = -Z/r + sum Q_b Y0_b / r  (G1 form)
rr = h5.r
Y0 = {k: h5.Yk(h5.P[k], h5.P[k], 0) for k in keys}
Vdir = -h5.Z / rr + sum(Q5[b] * Y0[b] / rr for b in keys)
R3 = 0.0; parts = {}
for k in keys:
    _, X = pot(h5, k)                                       # nonlocal exchange source (other shells); own local (T2-matched)
    M = 1 + (h5.eps[k] - Vdir) / (2 * c * c)
    w = (np.sqrt(np.maximum(M, 1e-12)) - 1) if cf != 'Z' else np.zeros_like(M)
    t = 2 * Q5[k] * float(np.sum(w * X * dP[k] * dr))
    parts["%d%s" % (k[0], 'spdf'[k[1]])] = t; R3 += t
# same-l orthogonality cross terms: diagnostic size only
xterms = {}
for i, k1 in enumerate(keys):
    for k2 in keys[i + 1:]:
        if k1[1] == k2[1]:
            xterms["%d%s-%d%s" % (k1[0], 'spdf'[k1[1]], k2[0], 'spdf'[k2[1]])] = float(np.sum(dP[k1] * h5.P[k2] * dr))

sealed = SEALED[ROW]; lo, hi = sorted((0.7 * sealed, 1.3 * sealed))
in_win = (lo <= R3 <= hi) and (np.sign(R3) == np.sign(sealed))
res = dict(row=ROW, system=SYS[ROW], Z=Zs, shell="%d%s" % (a[0], 'spdf'[a[1]]), canfail=cf,
           dE_rich=float(dE_rich), g=float(g5), R1_direct=float(R1), R2_chain=float(R2), R3_proj=float(R3),
           parts={k: float(v) for k, v in parts.items()}, xterms=xterms,
           sealed=sealed, window=[lo, hi], R3_in_window=bool(in_win),
           R1_vs_sealed=float(R1 - sealed), R2_vs_R1=float(R2 - R1), R3_vs_R1=float(R3 - R1),
           sec=int(time.time() - t0))
print("ROW %d sys %s: R1(direct)=%+.3e  R2(chain)=%+.3e  R3(proj)=%+.3e  sealed=%+.1e  window=[%.2e,%.2e]  %s"
      % (ROW, SYS[ROW], R1, R2, R3, sealed, lo, hi, "IN-WINDOW" if in_win else "OUTSIDE"), flush=True)
json.dump(res, open(os.path.join(HERE, 'd101-%d%s.json' % (ROW, '-cf' + cf if cf else '')), 'w'), indent=1)
sys.exit(0 if (in_win or cf) else 4)
