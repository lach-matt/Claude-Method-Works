#!/usr/bin/env python3
"""w104.py -- S104 ITEM 1 branch A. rot restated in the core-projected basis, row 58.
Twin of sealed pack102/w102b.py; basis restricted to the <=1e-10 valence set.
Prediction pack104/PREDICTION-S104-ITEM1.md hash-gated. c the only number.
usage: w104.py [--canfail]"""
import sys, os, json, time, hashlib, numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', 'rt')); os.chdir(os.path.join(HERE, '..', 'rt'))
p = os.path.join(HERE, 'PREDICTION-S104-ITEM1.md')
if hashlib.sha256(open(p, 'rb').read()).hexdigest() != open(p + '.sha256').read().split()[0]:
    print("HALT rc=3 sha"); sys.exit(3)
CANFAIL = '--canfail' in sys.argv
import nlchain as NC, hfc2 as H
sys.path.insert(0, '../pack93'); from ffun93 import solve, clone, Ione, Efun, pot
assert H.CORR is False
ROW = 58; ent = (5, 2); Zs = 58; dq2 = 0.2
VAL = {(5, 0), (5, 1), (5, 2), (6, 0)}                      # the <=1e-10 set
LAW = {'6s': +4.0626281199103220e-06, '5s': -7.8431534485281900e-06}   # sealed w103a-58.json
SREF = {('6s', '5s'): +2.4053e-03, ('5s', '6s'): -2.4032e-03}          # sealed w102b-58.json
rows = NC.load(); cfg2 = NC.cfg_from_chain(56, rows)
def setq(cfg, a, q):
    d = {(n, l): qq for n, l, qq in cfg}; d[a] = d.get(a, 0) + q
    return [(n, l, qq) for (n, l), qq in sorted(d.items()) if qq > 1e-9]
t0 = time.time(); sol = {}
for q in (0.4, 0.5, 0.6):
    sol[q] = solve(Zs, setq(cfg2, ent, q))[0]
    print("  solved q=%.1f (%ds)" % (q, time.time() - t0), flush=True)
h5, hp, hm = sol[0.5], sol[0.6], sol[0.4]
keys = [(n, l) for n, l, q in h5.occ]
r = h5.r; dr = h5.dr
I5 = Ione(h5)
ref = json.load(open(os.path.join(HERE, '..', 'pack102', 'w102b-58.json')))

def Taction(hh, k):
    Vloc, X = pot(hh, k)
    return hh.eps[k] * hh.P[k] - Vloc * hh.P[k] + X

def build_basis(k):
    """RESTATEMENT: partners restricted to same-l shells within VAL. Core excluded from basis."""
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
    asym = float(np.max(np.abs(M - M.T)))
    return 0.5 * (M + M.T), names, asym

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

FOUR = [(5, 0), (5, 1), (5, 2), (6, 0)]
out = {}; ok1 = ok2 = ok3 = ok4 = 0; n2 = n3 = 0; worst_asym = 0.0
print("shell  chord        d_chord | rot_val      law          d_law    | perp_val     ident")
for k in FOUR:
    tag = "%d%s" % (k[0], 'spdf'[k[1]])
    B = build_basis(k)
    M, names, asym = Imat(B); worst_asym = max(worst_asym, asym)
    def Iq(cvec): return float(cvec @ M @ cvec)
    Pm, Pp = B['m'][0], B['p'][0]
    D = Pp - Pm
    Dr = np.zeros_like(D); s = {}
    for n in names:
        if n in ('m', 'p'): continue
        ov = float(np.sum(D * B[n][0] * dr)); s[n] = ov; Dr += ov * B[n][0]
        if (tag, n) in SREF and abs(ov - SREF[(tag, n)]) <= 1e-9: ok1 += 1
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
    dch = chord - ref['parts'][tag]['chord']
    if abs(dch) <= 1e-8: ok1 += 1
    ident = rot + perp - chord
    if abs(ident) <= 1e-12: ok4 += 1
    dlaw = None
    if tag in LAW:
        n2 += 1; n3 += 1
        if np.sign(rot) == np.sign(LAW[tag]): ok2 += 1
        dlaw = rot - LAW[tag]
        if abs(dlaw) <= 2e-6: ok3 += 1
    out[tag] = dict(chord=chord, d_chord=dch, rot_val=rot, perp_val=perp, s=s,
                    law=LAW.get(tag), d_law=dlaw, asym=asym, ident=ident)
    print(" %-4s %+11.4e %+.0e | %+11.4e %s %s | %+11.4e %+.0e"
          % (tag, chord, dch, rot,
             ("%+11.4e" % LAW[tag]) if tag in LAW else "     --     ",
             ("%+.0e" % dlaw) if dlaw is not None else "   --  ",
             perp, ident))
if CANFAIL:
    bad = out['6s']['d_law']
    print("CANFAIL (6s Dr skew 1e-5*P5s): d_law(6s)=%.1e -> %s"
          % (bad, "rc=4 BREAK OK" if abs(bad) > 2e-6 else "rc=5 VACUOUS"))
    sys.exit(4 if abs(bad) > 2e-6 else 5)
PA1 = ok1 == 6      # 2 s-overlaps + 4 chords
PA2 = ok2 == n2 == 2
PA3 = ok3 == n3 == 2
PA4 = ok4 == 4
zdef = abs(out['5p']['rot_val']) == 0.0 and abs(out['5d']['rot_val']) == 0.0
print("PA.1 repro:    %d/6  %s   worst asym %.1e" % (ok1, "HIT" if PA1 else "MISS", worst_asym))
print("PA.2 sign:     %d/2  %s" % (ok2, "HIT" if PA2 else "MISS"))
print("PA.3 value:    %d/2  %s" % (ok3, "HIT" if PA3 else "MISS"))
print("PA.4 identity: %d/4  %s" % (ok4, "HIT" if PA4 else "MISS"))
print("declared: rot_val(5p)=rot_val(5d)=0 exact -> %s" % ("CONFIRMED" if zdef else "VIOLATED"))
json.dump(dict(row=ROW, PA1=bool(PA1), PA2=bool(PA2), PA3=bool(PA3), PA4=bool(PA4),
               zero_partner_exact=bool(zdef), worst_asym=worst_asym, parts=out,
               sec=int(time.time() - t0)),
          open(os.path.join(HERE, 'w104-58.json'), 'w'), indent=1, default=float)
print("receipt w104-58.json (%ds)" % (time.time() - t0))
