#!/usr/bin/env python3
"""w104b.py -- S104 ITEM 1 branch B. B1: tight-SCF valence-basis rot (6s, 5s). B2: direct-
quadrature I chord gate (6s). Row 58. Prediction pack104/PREDICTION-S104-ITEM1-B.md hash-gated.
c the only number. usage: w104b.py [--canfail]"""
import sys, os, json, time, hashlib, numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', 'rt')); os.chdir(os.path.join(HERE, '..', 'rt'))
p = os.path.join(HERE, 'PREDICTION-S104-ITEM1-B.md')
if hashlib.sha256(open(p, 'rb').read()).hexdigest() != open(p + '.sha256').read().split()[0]:
    print("HALT rc=3 sha"); sys.exit(3)
CANFAIL = '--canfail' in sys.argv
import nlchain as NC, hfc2 as H
sys.path.insert(0, '../pack93'); from ffun93 import clone, Ione, Efun, pot
assert H.CORR is False
Zs = 58; ent = (5, 2); dq2 = 0.2
VAL = {(5, 0), (5, 1), (5, 2), (6, 0)}
LAW = {'6s': +4.0626281199103220e-06, '5s': -7.8431534485281900e-06}
ASYM_REF = 1.36e-4
rows = NC.load(); cfg2 = NC.cfg_from_chain(56, rows)
def setq(cfg, a, q):
    d = {(n, l): qq for n, l, qq in cfg}; d[a] = d.get(a, 0) + q
    return [(n, l, qq) for (n, l), qq in sorted(d.items()) if qq > 1e-9]

TLADDER = [(0.4, 400), (0.2, 2000), (0.1, 6000)]
def solve_tight(Z, cfg, tol):
    for beta, maxit in TLADDER:
        h = H.HFC(Z, [tuple(x) for x in cfg], c=137.035999)
        E, _, it, eps = h.run2(beta=beta, maxit=maxit, tol=tol)
        if it < maxit: return h
    raise RuntimeError("no tight convergence")

t0 = time.time(); sol = {}
for q in (0.4, 0.5, 0.6):
    sol[q] = solve_tight(Zs, setq(cfg2, ent, q), 2e-9)
    print("  tight-solved q=%.1f (%ds)" % (q, time.time() - t0), flush=True)
h5, hp, hm = sol[0.5], sol[0.6], sol[0.4]
keys = [(n, l) for n, l, q in h5.occ]; r = h5.r; dr = h5.dr
I5 = Ione(h5)
ref = json.load(open(os.path.join(HERE, '..', 'pack102', 'w102b-58.json')))

def Taction(hh, k):
    Vloc, X = pot(hh, k)
    return hh.eps[k] * hh.P[k] - Vloc * hh.P[k] + X

def build_basis(k):
    Pp, Pm = hp.P[k].copy(), hm.P[k].copy()
    Tp, Tm = Taction(hp, k), Taction(hm, k)
    if float(np.sum(Pp * h5.P[k] * dr)) < 0: Pp, Tp = -Pp, -Tp
    if float(np.sum(Pm * h5.P[k] * dr)) < 0: Pm, Tm = -Pm, -Tm
    B = {'m': (Pm, Tm), 'p': (Pp, Tp)}
    for kk in keys:
        if kk != k and kk[1] == k[1] and kk in VAL:
            B["%d%s" % (kk[0], 'spdf'[kk[1]])] = (h5.P[kk], Taction(h5, kk))
    return B

def Imat(B):
    names = list(B); nb = len(names); M = np.zeros((nb, nb))
    for i, u in enumerate(names):
        for j, v in enumerate(names):
            Pu, _ = B[u]; Pv, Tv = B[v]
            M[i, j] = float(np.sum(Pu * (Tv - (Zs / r) * Pv) * dr))
    cross = 0.0
    for i, u in enumerate(names):
        for j in range(i + 1, nb):
            if names[i] in ('m', 'p') and names[j] not in ('m', 'p'):
                cross = max(cross, abs(M[i, j] - M[j, i]))
            if names[j] in ('m', 'p') and names[i] not in ('m', 'p'):
                cross = max(cross, abs(M[i, j] - M[j, i]))
    return 0.5 * (M + M.T), names, cross

def coeffs(vec, B, names):
    A = np.stack([B[n][0] for n in names], axis=1)
    G = A.T @ (A * dr[:, None]); b = A.T @ (vec * dr)
    x = np.linalg.solve(G, b)
    res = vec - A @ x
    return x, float(np.sqrt(np.sum(res * res * dr)))

def F(k, Pk, Ik):
    g = clone(h5, h5.Z, list(h5.occ)); g.P[k] = Pk
    I = dict(I5); I[k] = Ik
    return Efun(g, I)

def dP(u):
    """derivative on the radial grid (2nd-order nonuniform)"""
    return np.gradient(u, r)

def Iquad(u, v, l):
    return float(0.5 * np.sum(dP(u) * dP(v) * dr) + 0.5 * l * (l + 1) * np.sum(u * v / r**2 * dr)
                 - Zs * np.sum(u * v / r * dr))

out = {}; pb1 = pb2s = pb2v = pb3 = 0
print("shell  chord        d_seal   | rot_val      law          d_law    | cross_asym")
for k in [(6, 0), (5, 0)]:
    tag = "%d%s" % (k[0], 'spdf'[k[1]])
    B = build_basis(k)
    M, names, cross = Imat(B)
    if cross <= 1.4e-5: pb1 += 1
    def Iq(cvec): return float(cvec @ M @ cvec)
    Pm, Pp = B['m'][0], B['p'][0]
    D = Pp - Pm
    Dr = np.zeros_like(D); s = {}
    for n in names:
        if n in ('m', 'p'): continue
        ov = float(np.sum(D * B[n][0] * dr)); s[n] = ov; Dr += ov * B[n][0]
    if CANFAIL and tag == '6s':
        Dr = Dr + 1e-5 * B['5s'][0]
    pts = {'Pm': Pm, 'Pp': Pp, 'PmDr': Pm + Dr, 'PpMDr': Pp - Dr}
    Fv = {}
    for nm, vec in pts.items():
        cv, res = coeffs(vec, B, names)
        if res > 1e-9: print("  WARN span residual %s %s %.1e" % (tag, nm, res))
        Fv[nm] = F(k, vec, Iq(cv))
    chord = (Fv['Pp'] - Fv['Pm']) / dq2
    rot = 0.5 * ((Fv['PmDr'] - Fv['Pm']) + (Fv['Pp'] - Fv['PpMDr'])) / dq2
    perp = 0.5 * ((Fv['Pp'] - Fv['PmDr']) + (Fv['PpMDr'] - Fv['Pm'])) / dq2
    dseal = chord - ref['parts'][tag]['chord']
    if abs(dseal) <= 1e-6: pb3 += 1
    dlaw = rot - LAW[tag]
    if np.sign(rot) == np.sign(LAW[tag]): pb2s += 1
    if abs(dlaw) <= 2e-6: pb2v += 1
    out[tag] = dict(chord=chord, d_seal=dseal, rot_val=rot, perp_val=perp, s=s,
                    law=LAW[tag], d_law=dlaw, cross_asym=cross)
    print(" %-4s %+11.4e %+.0e | %+11.4e %+11.4e %+.0e | %.2e"
          % (tag, chord, dseal, rot, LAW[tag], dlaw, cross))
# B2 at 6s: direct-quadrature I for the four evaluation points, chord only
k = (6, 0); B = build_basis(k)
Pm, Pp = B['m'][0], B['p'][0]
ch_B2 = (F(k, Pp, Iquad(Pp, Pp, 0)) - F(k, Pm, Iquad(Pm, Pm, 0))) / dq2
d_B2 = ch_B2 - ref['parts']['6s']['chord']
PB4 = abs(d_B2) > 1e-8
print("B2 6s chord (direct quadrature): %+11.4e  d_seal %+.2e -> gate %s"
      % (ch_B2, d_B2, "FAIL (as predicted)" if PB4 else "PASS (competes)"))
if CANFAIL:
    bad = out['6s']['d_law']
    print("CANFAIL (6s Dr skew): d_law(6s)=%.1e -> %s"
          % (bad, "rc=4 BREAK OK" if abs(bad) > 2e-6 else "rc=5 VACUOUS"))
    sys.exit(4 if abs(bad) > 2e-6 else 5)
PB1 = pb1 == 2; PB2 = (pb2s == 2 and pb2v == 2); PB3 = pb3 == 2
print("PB.1 asym gate:  %d/2  %s" % (pb1, "HIT" if PB1 else "MISS"))
print("PB.2 law tight:  sign %d/2 value %d/2  %s" % (pb2s, pb2v, "HIT" if PB2 else "MISS"))
print("PB.3 chord stab: %d/2  %s" % (pb3, "HIT" if PB3 else "MISS"))
print("PB.4 B2 gate:    %s" % ("HIT (fails gate as predicted)" if PB4 else "MISS (B2 passes)"))
json.dump(dict(row=58, PB1=bool(PB1), PB2=bool(PB2), PB3=bool(PB3), PB4=bool(PB4),
               chord_B2=ch_B2, d_B2=d_B2, parts=out, sec=int(time.time() - t0)),
          open(os.path.join(HERE, 'w104b-58.json'), 'w'), indent=1, default=float)
print("receipt w104b-58.json (%ds)" % (time.time() - t0))
