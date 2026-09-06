#!/usr/bin/env python3
"""g1probe.py -- S100 G1 (F95.4). Prediction pack100/PREDICTION-S100-G1.md (88b7b4af) hashed BEFORE this file.
Dense build copied VERBATIM from pack99/f954probe.py (sym branch); npts a parameter; SCF re-solved per grid.
usage: g1probe.py NPTS [--canfail A|B]   (one npts per call; receipt pack100/g1-NPTS.json)"""
import sys, os, json, time, hashlib, numpy as np, scipy.linalg as sla
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, '..', 'rt')); os.chdir(os.path.join(HERE, '..', 'rt'))
PRED = os.path.join(HERE, 'PREDICTION-S100-G1.md')
want = open(PRED + '.sha256').read().split()[0]
got = hashlib.sha256(open(PRED, 'rb').read()).hexdigest()
if want != got: print("HALT rc=3 sha"); sys.exit(3)
import nlchain as NC, nlguard as NG, hfc2 as H
from t7c_kernel import C0, _derivs
from t7b_hf import _c3j0sq
npts = int(sys.argv[1]); cf = sys.argv[sys.argv.index('--canfail') + 1] if '--canfail' in sys.argv else None
ROWS = {d['Z']: d for d in map(json.loads, open('nlchain.jsonl'))}
Z = 88; cfg = NC.cfg_from_chain(88, ROWS)   # core side, row 89 (as f954probe)

def solve(Z, cfg, npts):
    for beta, maxit in NG.LADDER:
        g = H.HFC(Z, [tuple(x) for x in cfg], npts=npts, c=C0); E, _, it, eps = g.run2(beta=beta, maxit=maxit)
        if it < maxit: return g, E
    raise RuntimeError

t0 = time.time(); g, E = solve(Z, cfg, npts); print("solved core npts=%d E=%.6f (%.1fs)" % (npts, E, time.time() - t0), flush=True)
r, x, h, dr, N = g.r, g.x, g.h, g.dr, g.npts; P = g.P; eps = g.eps
keys = [(n, l) for n, l, q in g.occ]; Q = {(n, l): q for n, l, q in g.occ}; c = C0
Y0 = {k: g.Yk(P[k], P[k], 0) for k in keys}; Vdir = -Z / r + sum(Q[b] * Y0[b] / r for b in keys)

def Gk(k):
    ri = r[:, None]; rj = r[None, :]; lo = np.minimum(ri, rj); hi = np.maximum(ri, rj); return lo**k / hi**(k + 1)

def exch_S(l):
    S = np.zeros((N, N))
    for b in keys:
        nb, lb = b
        for k in range(abs(l - lb), l + lb + 1, 2):
            coef = 0.5 * Q[b] * _c3j0sq(l, k, lb)
            if coef > 1e-14: S += coef * (P[b][:, None] * Gk(k) * P[b][None, :])
    return S

ltest = 0
D2 = (np.diag(-2 * np.ones(N)) + np.diag(np.ones(N - 1), 1) + np.diag(np.ones(N - 1), -1)) / (h * h)
FD2 = np.linalg.solve(np.eye(N) + h * h * D2 / 12.0, D2); FD2 = 0.5 * (FD2 + FD2.T)
Vp, Vpp = _derivs(x, Vdir)

def build(l, Eref, S):
    M = 1 + (Eref - Vdir) / (2 * c * c); Mp = -Vp / (2 * c * c); Mpp = -Vpp / (2 * c * c)
    Dref = -Mp / (r * M) - Mpp / (2 * M) + 3 * Mp * Mp / (4 * M * M)
    A = -FD2 + np.diag((l + 0.5)**2 + r * r * (2 * M * Vdir + Dref)); Bd = 2 * r * r * M; Bi = 1 / np.sqrt(Bd)
    C = A * Bi[:, None] * Bi[None, :]
    X = np.sqrt(r)[:, None] * S * np.sqrt(r)[None, :] * h
    C -= X; C = 0.5 * (C + C.T)
    return C

S = exch_S(ltest)
a = [k for k in keys if k[1] == ltest][-1]
tgt = eps[a] + (1e-4 if cf == 'A' else 0.0)
t1 = time.time(); C = build(ltest, eps[a], S)

def inv_iter(C, sig):
    n = C.shape[0]; A = C - sig * np.eye(n)
    lu, piv = sla.lu_factor(A, overwrite_a=True); v = np.ones(n) / np.sqrt(n)
    lam = sig
    for _ in range(60):
        w = sla.lu_solve((lu, piv), v); w /= np.linalg.norm(w)
        lam_new = float(w @ (C @ w))
        if abs(lam_new - lam) < 1e-13: lam = lam_new; v = w; break
        lam = lam_new; v = w
    return lam

lam_ii = inv_iter(C.copy(), eps[a])
res = dict(npts=N, h=h, Z=Z, shell=str(a), eps=float(eps[a]), lam_ii=float(lam_ii),
           dE=float(lam_ii - tgt), canfail=cf, sec=int(time.time() - t0))
if N <= 4200 or cf == 'B':
    w = sla.eigvalsh(C); j = int(np.argmin(np.abs(w - eps[a]))); lam_full = float(w[j])
    res['lam_full'] = lam_full; res['ii_vs_full'] = float(lam_ii - lam_full)
    if abs(lam_ii - lam_full) > 1e-9:
        print("CF-B FIRE: ii vs full %.3e rc=4" % (lam_ii - lam_full), flush=True)
        json.dump(res, open(os.path.join(HERE, 'g1-%d%s.json' % (N, '-cf' + cf if cf else '')), 'w'), indent=1); sys.exit(4)
print("npts=%d h=%.6e eps=%.8f lin=%.8f dE=%+.4e rel=%.3e (%.1fs build+eig)" %
      (N, h, eps[a], lam_ii, res['dE'], abs(res['dE'] / eps[a]), time.time() - t1), flush=True)
json.dump(res, open(os.path.join(HERE, 'g1-%d%s.json' % (N, '-cf' + cf if cf else '')), 'w'), indent=1)
