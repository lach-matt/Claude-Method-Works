#!/usr/bin/env python3
"""w102b.py -- S102 ITEM 1B. One-shell chord split (rot/perp) in the R2_parts gauge, row 58.
Prediction pack102/PREDICTION-S102-ITEM1B.md hash-gated. c the only number.
usage: w102b.py [--canfail]"""
import sys, os, json, time, hashlib, numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', 'rt')); os.chdir(os.path.join(HERE, '..', 'rt'))
p = os.path.join(HERE, 'PREDICTION-S102-ITEM1B.md')
if hashlib.sha256(open(p, 'rb').read()).hexdigest() != open(p + '.sha256').read().split()[0]:
    print("HALT rc=3 sha"); sys.exit(3)
CANFAIL = '--canfail' in sys.argv
import nlchain as NC, hfc2 as H
sys.path.insert(0, '../pack93'); from ffun93 import solve, clone, Ione, Efun, pot
assert H.CORR is False
ROW = 58; ent = (5, 2); Zs = 58; dq2 = 0.2
rows = NC.load(); cfg2 = NC.cfg_from_chain(56, rows)
def setq(cfg, a, q):
    d = {(n, l): qq for n, l, qq in cfg}; d[a] = d.get(a, 0) + q
    return [(n, l, qq) for (n, l), qq in sorted(d.items()) if qq > 1e-9]
t0 = time.time(); sol = {}
for q in (0.4, 0.5, 0.6):
    sol[q] = solve(Zs, setq(cfg2, ent, q))[0]
    print("  solved q=%.1f (%ds)" % (q, time.time() - t0), flush=True)
h5, hp, hm = sol[0.5], sol[0.6], sol[0.4]
keys = [(n, l) for n, l, q in h5.occ]; Q5 = {(n, l): q for n, l, q in h5.occ}
r = h5.r; dr = h5.dr
I5 = Ione(h5)
ref = json.load(open(os.path.join(HERE, '..', 'pack101', 'd101-58.json')))
R2p = {k: ref['R2_parts']["%d%s" % (k[0], 'spdf'[k[1]])] for k in keys}

# T-action per basis orbital from its OWN eigen-relation: T P = eps P - Vloc P + X  (radial eq)
def Taction(hh, k):
    Vloc, X = pot(hh, k)
    return hh.eps[k] * hh.P[k] - Vloc * hh.P[k] + X

# per shell k: basis {m: P_k^-, p: P_k^+, and same-l occupied k' at h5}
def build_basis(k):
    Pp, Pm = hp.P[k].copy(), hm.P[k].copy()
    Tp, Tm = Taction(hp, k), Taction(hm, k)
    if float(np.sum(Pp * h5.P[k] * dr)) < 0: Pp, Tp = -Pp, -Tp
    if float(np.sum(Pm * h5.P[k] * dr)) < 0: Pm, Tm = -Pm, -Tm
    B = {'m': (Pm, Tm), 'p': (Pp, Tp)}
    for kk in keys:
        if kk != k and kk[1] == k[1]:
            B["%d%s" % (kk[0], 'spdf'[kk[1]])] = (h5.P[kk], Taction(h5, kk))
    return B

def Imat(B, k):
    """I-op matrix <u|T - Z/r|v> on the basis, symmetrized; returns (mat, names, worst asymmetry)."""
    names = list(B); nb = len(names); M = np.zeros((nb, nb)); worst = 0.0
    for i, u in enumerate(names):
        for j, v in enumerate(names):
            Pu, _ = B[u]; Pv, Tv = B[v]
            M[i, j] = float(np.sum(Pu * (Tv - (Zs / r) * Pv) * dr))
    asym = np.max(np.abs(M - M.T)); worst = float(asym)
    return 0.5 * (M + M.T), names, worst

def coeffs(vec, B, names, k):
    """least-squares coords of vec in span(B) + residual norm (must be ~0 for chord/rot vectors)"""
    A = np.stack([B[n][0] for n in names], axis=1)
    G = A.T @ (A * dr[:, None]); b = A.T @ (vec * dr)
    x = np.linalg.solve(G, b)
    res = vec - A @ x
    return x, float(np.sqrt(np.sum(res * res * dr)))

def F(k, Pk, Ik):
    """Efun of hybrid: shell k -> (Pk, Ik); everything else h5."""
    g = clone(h5, h5.Z, list(h5.occ)); g.P[k] = Pk
    I = dict(I5); I[k] = Ik
    return Efun(g, I)

skew_done = False
out = {}; hits4 = hits5 = 0; p6a = []; p6b = []; worst_asym = 0.0
print("shell  chord(F)     R2part(d101)  d      | rot          perp         rot/R2p")
for k in keys:
    tag = "%d%s" % (k[0], 'spdf'[k[1]])
    B = build_basis(k)
    M, names, asym = Imat(B, k); worst_asym = max(worst_asym, asym)
    if CANFAIL and tag == '4p' and not skew_done:
        M[0, 1] += 1e-7; M[1, 0] += 1e-7; skew_done = True
    idx = {n: i for i, n in enumerate(names)}
    def Iq(cvec): return float(cvec @ M @ cvec)
    Pm, Pp = B['m'][0], B['p'][0]
    D = Pp - Pm
    # rotation part of the chord onto same-l occupied (h5) partners
    Dr = np.zeros_like(D); s = {}
    for n in names:
        if n in ('m', 'p'): continue
        ov = float(np.sum(D * B[n][0] * dr)); s[n] = ov; Dr += ov * B[n][0]
    Dp = D - Dr
    # coordinates of the four evaluation points in the basis
    pts = {'Pm': Pm, 'Pp': Pp, 'PmDr': Pm + Dr, 'PpMDr': Pp - Dr}
    Fv = {}
    for nm, vec in pts.items():
        cv, res = coeffs(vec, B, names, k)
        if res > 1e-9: print("  WARN span residual %s %s %.1e" % (tag, nm, res))
        Fv[nm] = F(k, vec, Iq(cv))
    chord = (Fv['Pp'] - Fv['Pm']) / dq2
    rot = 0.5 * ((Fv['PmDr'] - Fv['Pm']) + (Fv['Pp'] - Fv['PpMDr'])) / dq2
    perp = 0.5 * ((Fv['Pp'] - Fv['PmDr']) + (Fv['PpMDr'] - Fv['Pm'])) / dq2
    t = R2p[k]
    d4 = chord - t; ok4 = abs(d4) <= 1e-8; hits4 += ok4
    d5 = rot + perp - chord; ok5 = abs(d5) <= 1e-12; hits5 += ok5
    if tag in ('5s', '5p', '5d', '6s'):
        p6a.append(abs(rot) >= 0.5 * abs(t) and np.sign(rot) == np.sign(t))
    if tag in ('1s', '2s', '2p', '3s', '3p', '3d'):
        p6b.append(abs(rot) <= 0.2 * abs(t))
    out[tag] = dict(chord=chord, R2p=t, rot=rot, perp=perp, s=s, asym=asym,
                    d_repro=d4, d_ident=d5)
    print(" %-4s %+11.4e %+11.4e %+.0e | %+11.4e %+11.4e  %+.2f"
          % (tag, chord, t, d4, rot, perp, rot / t if t else float('nan')))
if CANFAIL:
    bad = out['4p']['d_repro']
    print("CANFAIL (4p I_cross skew 1e-7): d_repro(4p)=%.1e -> %s" % (bad, "rc=4 BREAK OK" if abs(bad) > 1e-8 else "rc=5 VACUOUS"))
    sys.exit(4 if abs(bad) > 1e-8 else 5)
P4 = hits4 == 13; P5 = hits5 == 13
P6 = all(p6a) and all(p6b) and len(p6a) == 4 and len(p6b) == 6
print("P4 reproduction: %d/13  %s   worst I asym %.1e" % (hits4, "HIT" if P4 else "MISS", worst_asym))
print("P5 identity:     %d/13  %s" % (hits5, "HIT" if P5 else "MISS"))
print("P6 localization: anomalous %d/4  core %d/6  %s" % (sum(p6a), sum(p6b), "HIT" if P6 else "MISS"))
json.dump(dict(row=ROW, P4=bool(P4), P5=bool(P5), P6=bool(P6), worst_asym=worst_asym,
               parts=out, sec=int(time.time() - t0)),
          open(os.path.join(HERE, 'w102b-58.json'), 'w'), indent=1, default=float)
print("receipt w102b-58.json (%ds)" % (time.time() - t0))
