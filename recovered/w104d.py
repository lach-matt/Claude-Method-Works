#!/usr/bin/env python3
"""w104d.py -- S104 ITEM 3. perp_k exact quartic decomposition along Dp, row 58, four shells.
Prediction pack104/PREDICTION-S104-ITEM3.md hash-gated. c the only number.
usage: w104d.py [--canfail]"""
import sys, os, json, time, hashlib, numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', 'rt')); os.chdir(os.path.join(HERE, '..', 'rt'))
p = os.path.join(HERE, 'PREDICTION-S104-ITEM3.md')
if hashlib.sha256(open(p, 'rb').read()).hexdigest() != open(p + '.sha256').read().split()[0]:
    print("HALT rc=3 sha"); sys.exit(3)
CANFAIL = '--canfail' in sys.argv
import nlchain as NC, hfc2 as H
sys.path.insert(0, '../pack93'); from ffun93 import solve, clone, Ione, Efun, pot
assert H.CORR is False
Zs = 58; ent = (5, 2); dq2 = 0.2
VAL = {(5, 0), (5, 1), (5, 2), (6, 0)}
rows = NC.load(); cfg2 = NC.cfg_from_chain(56, rows)
def setq(cfg, a, q):
    d = {(n, l): qq for n, l, qq in cfg}; d[a] = d.get(a, 0) + q
    return [(n, l, qq) for (n, l), qq in sorted(d.items()) if qq > 1e-9]
t0 = time.time(); sol = {}
for q in (0.4, 0.5, 0.6):
    sol[q] = solve(Zs, setq(cfg2, ent, q))[0]
    print("  solved q=%.1f (%ds)" % (q, time.time() - t0), flush=True)
h5, hp, hm = sol[0.5], sol[0.6], sol[0.4]
keys = [(n, l) for n, l, q in h5.occ]; r = h5.r; dr = h5.dr
I5 = Ione(h5)
ref = json.load(open(os.path.join(HERE, 'w104-58.json')))

def Taction(hh, k):
    Vloc, X = pot(hh, k)
    return hh.eps[k] * hh.P[k] - Vloc * hh.P[k] + X

def machinery(k):
    Pp, Pm = hp.P[k].copy(), hm.P[k].copy()
    Tp, Tm = Taction(hp, k), Taction(hm, k)
    if float(np.sum(Pp * h5.P[k] * dr)) < 0: Pp, Tp = -Pp, -Tp
    if float(np.sum(Pm * h5.P[k] * dr)) < 0: Pm, Tm = -Pm, -Tm
    B = {'m': (Pm, Tm), 'p': (Pp, Tp)}
    for kk in keys:
        if kk != k and kk[1] == k[1] and kk in VAL:
            B["%d%s" % (kk[0], 'spdf'[kk[1]])] = (h5.P[kk], Taction(h5, kk))
    names = list(B); nb = len(names)
    M = np.zeros((nb, nb))
    for i, u in enumerate(names):
        for j, v in enumerate(names):
            M[i, j] = float(np.sum(B[u][0] * (B[v][1] - (Zs / r) * B[v][0]) * dr))
    M = 0.5 * (M + M.T)
    A = np.stack([B[n][0] for n in names], axis=1)
    def Fq(vec):
        G = A.T @ (A * dr[:, None]); b = A.T @ (vec * dr)
        cv = np.linalg.solve(G, b)
        g = clone(h5, h5.Z, list(h5.occ)); g.P[k] = vec
        I = dict(I5); I[k] = float(cv @ M @ cv)
        return Efun(g, I)
    return B, names, Fq, Pm, Pp

FOUR = [(5, 0), (5, 1), (5, 2), (6, 0)]
out = {}; pp1 = pp2 = pp3 = pp4 = 0
print("shell  perp        d_seal  | T1p         T2p        T3+4p     d_tot   | rem/perp T1p/perp")
for k in FOUR:
    tag = "%d%s" % (k[0], 'spdf'[k[1]])
    B, names, Fq, Pm, Pp = machinery(k)
    D = Pp - Pm
    Dr = np.zeros_like(D)
    for n in names:
        if n in ('m', 'p'): continue
        Dr += float(np.sum(D * B[n][0] * dr)) * B[n][0]
    Dp = D - Dr
    Fm0, Fp0 = Fq(Pm), Fq(Pp)
    chord = (Fp0 - Fm0) / dq2
    rot = 0.5 * ((Fq(Pm + Dr) - Fm0) + (Fp0 - Fq(Pp - Dr))) / dq2
    perp = 0.5 * ((Fp0 - Fq(Pm + Dr)) + (Fq(Pp - Dr) - Fm0)) / dq2
    d_seal = perp - ref['parts'][tag]['perp_val']
    ident = rot + perp - chord
    ok1 = abs(ident) <= 1e-12; pp1 += ok1
    ts = np.array([-1.0, -0.5, 0.0, 0.5, 1.0])
    Vm = np.array([Fq(Pm + t * Dp) for t in ts])
    Vp = np.array([Fq(Pp + t * Dp) for t in ts])
    Wm = np.polyfit(ts, Vm, 4)[::-1]; Wp = np.polyfit(ts, Vp, 4)[::-1]
    c1m, c2m, c3m, c4m = Wm[1], Wm[2], Wm[3], Wm[4]
    c1p, c2p, c3p, c4p = Wp[1], Wp[2], Wp[3], Wp[4]
    if CANFAIL and tag == '6s':
        c1m += 1e-6
    T1 = 0.5 * (c1m + c1p) / dq2
    T2 = 0.5 * (c2m - c2p) / dq2
    T34 = 0.5 * (c3m + c3p) / dq2 + 0.5 * (c4m - c4p) / dq2
    total = T1 + T2 + T34
    ok2 = abs(total - perp) <= 2e-11; pp2 += ok2
    ok3 = abs(T34) <= 0.1 * abs(perp); pp3 += ok3
    ok4 = abs(T1) >= 0.8 * abs(perp) and np.sign(T1) == np.sign(perp); pp4 += ok4
    out[tag] = dict(chord=chord, rot=rot, perp=perp, d_seal=d_seal, ident=ident,
                    T1p=T1, T2p=T2, T34p=T34, total=total, d_total=total - perp,
                    PP1=bool(ok1), PP2=bool(ok2), PP3=bool(ok3), PP4=bool(ok4))
    print(" %-4s %+10.4e %+.0e | %+10.4e %+9.2e %+9.2e %.1e | %+.3f  %+.3f"
          % (tag, perp, d_seal, T1, T2, T34, abs(total - perp),
             T34 / perp if perp else float('nan'), T1 / perp if perp else float('nan')))
if CANFAIL:
    bad = abs(out['6s']['d_total'])
    print("CANFAIL (c1m skew 1e-6 at 6s): d_total=%.1e -> %s"
          % (bad, "rc=4 BREAK OK" if bad > 2e-11 else "rc=5 VACUOUS"))
    sys.exit(4 if bad > 2e-11 else 5)
PP1 = pp1 == 4; PP2 = pp2 == 4; PP3 = pp3 == 4; PP4 = pp4 == 4
PP5 = PP1 and PP2
print("PP.1 identity:   %d/4  %s" % (pp1, "HIT" if PP1 else "MISS"))
print("PP.2 decomp:     %d/4  %s" % (pp2, "HIT" if PP2 else "MISS"))
print("PP.3 remainder:  %d/4  %s" % (pp3, "HIT" if PP3 else "MISS"))
print("PP.4 dominance:  %d/4  %s" % (pp4, "HIT" if PP4 else "MISS"))
print("PP.5 (F101.5 discharge clause): %s" % ("HIT" if PP5 else "MISS"))
json.dump(dict(row=58, PP1=bool(PP1), PP2=bool(PP2), PP3=bool(PP3), PP4=bool(PP4),
               PP5=bool(PP5), parts=out, sec=int(time.time() - t0)),
          open(os.path.join(HERE, 'w104d-58.json'), 'w'), indent=1, default=float)
print("receipt w104d-58.json (%ds)" % (time.time() - t0))
