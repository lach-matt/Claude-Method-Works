#!/usr/bin/env python3
"""w103a.py -- S103 ITEM 1. Analytic rot_k law (overlap x Fock off-diagonal), row 58,
scored vs SEALED pack102/w102b-58.json rot at the four <=1e-10 shells (5s,5p,5d,6s).
Prediction pack103/PREDICTION-S103-ITEM1.md (be23917c) hash-gated. c the only number.
usage: w103a.py [--canfail]"""
import sys, os, json, time, hashlib, numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', 'rt')); os.chdir(os.path.join(HERE, '..', 'rt'))
p = os.path.join(HERE, 'PREDICTION-S103-ITEM1.md')
if hashlib.sha256(open(p, 'rb').read()).hexdigest() != open(p + '.sha256').read().split()[0]:
    print("HALT rc=3 sha"); sys.exit(3)
CANFAIL = '--canfail' in sys.argv
import nlchain as NC, hfc2 as H
sys.path.insert(0, '../pack93'); from ffun93 import solve, clone, pot
assert H.CORR is False
ROW = 58; ent = (5, 2); Zs = 58; dq2 = 0.2
SHELLS = [(5, 0), (5, 1), (5, 2), (6, 0)]
rows = NC.load(); cfg2 = NC.cfg_from_chain(56, rows)
def setq(cfg, a, q):
    d = {(n, l): qq for n, l, qq in cfg}; d[a] = d.get(a, 0) + q
    return [(n, l, qq) for (n, l), qq in sorted(d.items()) if qq > 1e-9]
t0 = time.time(); sol = {}
for q in (0.4, 0.5, 0.6):
    sol[q] = solve(Zs, setq(cfg2, ent, q))[0]
    print("  solved q=%.1f (%ds)" % (q, time.time() - t0), flush=True)
h5, hp, hm = sol[0.5], sol[0.6], sol[0.4]
Q5 = {(n, l): q for n, l, q in h5.occ}; r = h5.r; dr = h5.dr
ref = json.load(open(os.path.join(HERE, '..', 'pack102', 'w102b-58.json')))['parts']
def TP(hh, k):
    Vloc, X = pot(hh, k)
    return hh.eps[k] * hh.P[k] - Vloc * hh.P[k] + X
def Felem(kp, k, hend, skew=0.0):
    Pe = hend.P[k].copy(); Te = TP(hend, k)
    if float(np.sum(Pe * h5.P[k] * dr)) < 0: Pe, Te = -Pe, -Te
    g = clone(h5, h5.Z, list(h5.occ)); g.P[k] = Pe
    Vloc, X = pot(g, k)
    return float(np.sum(h5.P[kp] * (Te + Vloc * Pe - X) * dr)) + skew
tg = lambda k: "%d%s" % (k[0], 'spdf'[k[1]])
DOM = {(5, 0): '6s', (6, 0): '5s', (5, 1): '4p', (5, 2): '4d'}
out = {}; h1 = 0; h2 = 0
print("shell  rot_AN        rot_w102b     d          tol   | dom term      signOK")
for k in SHELLS:
    t = tg(k); s = ref[t]['s']; rotW = ref[t]['rot']
    tol = 2e-6 if k[1] == 0 else 1e-7
    terms = {}
    for nm, sv in s.items():
        kp = (int(nm[0]), 'spdf'.index(nm[1]))
        skew = 1e-5 if (CANFAIL and t == '6s' and nm == '5s') else 0.0
        terms[nm] = sv * (Felem(kp, k, hm, skew) + Felem(kp, k, hp, skew))
    rotAN = (Q5[k] / dq2) * sum(terms.values())
    d = rotAN - rotW
    ok1 = abs(d) <= tol and np.sign(rotAN) == np.sign(rotW); h1 += ok1
    dt = (Q5[k] / dq2) * terms[DOM[k]]
    ok2 = np.sign(dt) == np.sign(rotW); h2 += ok2
    out[t] = dict(rot_AN=rotAN, rot_w102b=rotW, d=d, tol=tol, dom=DOM[k],
                  terms={nm: (Q5[k] / dq2) * v for nm, v in terms.items()})
    print(" %-4s %+12.5e %+12.5e %+.1e %.0e | %s:%+.2e  %s"
          % (t, rotAN, rotW, d, tol, DOM[k], dt, "Y" if ok2 else "N"))
if CANFAIL:
    bad = out['6s']['d']
    print("CANFAIL (F_{5s,6s} skew +1e-5): d(6s)=%.1e -> %s"
          % (bad, "rc=4 BREAK OK" if abs(bad) > 2e-6 else "rc=5 VACUOUS"))
    sys.exit(4 if abs(bad) > 2e-6 else 5)
P1 = h1 == 4; P2 = h2 == 4
print("P103.1 value+sign: %d/4  %s" % (h1, "HIT" if P1 else "MISS"))
print("P103.2 dominant-partner sign: %d/4  %s" % (h2, "HIT" if P2 else "MISS"))
json.dump(dict(row=ROW, P1=bool(P1), P2=bool(P2), parts=out, sec=int(time.time() - t0)),
          open(os.path.join(HERE, 'w103a-58.json'), 'w'), indent=1, default=float)
print("receipt w103a-58.json (%ds)" % (time.time() - t0))