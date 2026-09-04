#!/usr/bin/env python3
"""w104c.py -- S104 ITEM 1 closure. Derivation-1 (cross-asym identity) and Derivation-2
(exact quartic rot decomposition), row 58, shells 6s/5s, valence basis.
Prediction pack104/PREDICTION-S104-ITEM1-C.md hash-gated. c the only number.
usage: w104c.py [--canfail]"""
import sys, os, json, time, hashlib, numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', 'rt')); os.chdir(os.path.join(HERE, '..', 'rt'))
p = os.path.join(HERE, 'PREDICTION-S104-ITEM1-C.md')
if hashlib.sha256(open(p, 'rb').read()).hexdigest() != open(p + '.sha256').read().split()[0]:
    print("HALT rc=3 sha"); sys.exit(3)
CANFAIL = '--canfail' in sys.argv
import nlchain as NC, hfc2 as H
sys.path.insert(0, '../pack93'); from ffun93 import solve, clone, Ione, Efun, pot
assert H.CORR is False
Zs = 58; ent = (5, 2); dq2 = 0.2
VAL = {(5, 0), (5, 1), (5, 2), (6, 0)}
LAW = {'6s': +4.0626281199103220e-06, '5s': -7.8431534485281900e-06}
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
w104ref = json.load(open(os.path.join(HERE, 'w104-58.json')))

def Taction(hh, k):
    Vloc, X = pot(hh, k)
    return hh.eps[k] * hh.P[k] - Vloc * hh.P[k] + X

def build(k):
    Pp, Pm = hp.P[k].copy(), hm.P[k].copy()
    sp = 1.0 if float(np.sum(Pp * h5.P[k] * dr)) >= 0 else -1.0
    sm = 1.0 if float(np.sum(Pm * h5.P[k] * dr)) >= 0 else -1.0
    return sm * Pm, sp * Pp, sm, sp

def coeffs(vec, A):
    G = A.T @ (A * dr[:, None]); b = A.T @ (vec * dr)
    return np.linalg.solve(G, b)

def F(k, Pk, Ik):
    g = clone(h5, h5.Z, list(h5.occ)); g.P[k] = Pk
    I = dict(I5); I[k] = Ik
    return Efun(g, I)

out = {}; q1a = q1b = q2a = q2b = q2c = 0
for k, kpart in [((6, 0), (5, 0)), ((5, 0), (6, 0))]:
    tag = "%d%s" % (k[0], 'spdf'[k[1]])
    ptag = "%d%s" % (kpart[0], 'spdf'[kpart[1]])
    Pm, Pp, sm, sp = build(k)
    Tm, Tp = sm * Taction(hm, k), sp * Taction(hp, k)
    Pu = h5.P[kpart]; Tu = Taction(h5, kpart)
    epsU = h5.eps[kpart]
    VlU, XU = pot(h5, kpart)
    # ---- Derivation 1: four cross elements ----
    d1 = {}
    for nm, Pv, Tv, hh, sgn in (('m', Pm, Tm, hm, sm), ('p', Pp, Tp, hp, sp)):
        epsV = hh.eps[k]; VlV, XV = pot(hh, k)
        Muv = float(np.sum(Pu * (Tv - (Zs / r) * Pv) * dr))          # T-on-v (endpoint)
        Mvu = float(np.sum(Pv * (Tu - (Zs / r) * Pu) * dr))          # T-on-u (partner)
        asym_meas = Muv - Mvu
        S = float(np.sum(Pu * Pv * dr))
        term_eps = (epsV - epsU) * S
        term_V = -float(np.sum(Pu * Pv * (VlV - VlU) * dr))
        term_X = float(np.sum(Pu * sgn * XV * dr)) - float(np.sum(Pv * XU * dr))
        asym_id = term_eps + term_V + term_X
        ok_a = abs(asym_id - asym_meas) <= 1e-12
        ok_b = abs(term_eps) >= 10 * abs(asym_meas)
        q1a += ok_a; q1b += ok_b
        d1["%s|%s" % (nm, ptag)] = dict(asym_meas=asym_meas, asym_id=asym_id,
                                        d=asym_id - asym_meas, term_eps=term_eps,
                                        term_V=term_V, term_X=term_X, S=S,
                                        PQ1a=bool(ok_a), PQ1b=bool(ok_b))
        print("D1 %s %s|%s: meas %+.6e id %+.6e d %.1e | eps*S %+.3e V %+.3e X %+.3e %s%s"
              % (tag, nm, ptag, asym_meas, asym_id, abs(asym_id - asym_meas),
                 term_eps, term_V, term_X, "a" if ok_a else "A!", "b" if ok_b else "B!"))
    # ---- Derivation 2: exact quartic decomposition of rot ----
    B = {'m': (Pm, Tm), 'p': (Pp, Tp), ptag: (Pu, Tu)}
    names = list(B); nb = len(names)
    M = np.zeros((nb, nb))
    for i, u in enumerate(names):
        for j, v in enumerate(names):
            M[i, j] = float(np.sum(B[u][0] * (B[v][1] - (Zs / r) * B[v][0]) * dr))
    M = 0.5 * (M + M.T)
    A = np.stack([B[n][0] for n in names], axis=1)
    def Fq(vec):
        cv = coeffs(vec, A)
        return F(k, vec, float(cv @ M @ cv))
    D = Pp - Pm
    sOv = float(np.sum(D * Pu * dr))
    Dr = sOv * Pu
    # rot reconstruction check (branch-A machinery)
    Fm0, Fp0 = Fq(Pm), Fq(Pp)
    rot = 0.5 * ((Fq(Pm + Dr) - Fm0) + (Fp0 - Fq(Pp - Dr))) / dq2
    d_rec = rot - w104ref['parts'][tag]['rot_val']
    # exact quartic fits: t in {0, +-1/2, +-1}
    ts = np.array([-1.0, -0.5, 0.0, 0.5, 1.0])
    Vm = np.array([Fq(Pm + t * Dr) for t in ts])
    Vp = np.array([Fq(Pp + t * Dr) for t in ts])   # expansion at Pp along +Dr; c-odd flip below
    Wm = np.polyfit(ts, Vm, 4)[::-1]               # Wm[i] = coeff of t^i at Pm
    Wp = np.polyfit(ts, Vp, 4)[::-1]
    c1m, c2m, c3m, c4m = Wm[1], Wm[2], Wm[3], Wm[4]
    c1p, c2p, c3p, c4p = Wp[1], Wp[2], Wp[3], Wp[4]
    if CANFAIL and tag == '6s':
        c2m += 1e-6
    term1 = 0.5 * (c1m + c1p) / dq2
    term2 = 0.5 * (c2m - c2p) / dq2
    term3 = 0.5 * (c3m + c3p) / dq2
    term4 = 0.5 * (c4m - c4p) / dq2
    total = term1 + term2 + term3 + term4
    ok2a = abs(total - rot) <= 1e-12 and abs(d_rec) <= 1e-9
    rem = rot - term1 - term2
    ok2b = abs(rem) <= 2e-7 and np.sign(term2) > 0
    gap1 = term1 - LAW[tag]
    reach = 2 * abs(sOv) * max(abs(d1[x]['asym_meas']) for x in d1) / dq2
    ok2c = abs(gap1) <= 1.5e-6 and abs(gap1) <= reach
    q2a += ok2a; q2b += ok2b; q2c += ok2c
    out[tag] = dict(D1=d1, rot=rot, d_reconstruct=d_rec, term1=term1, term2=term2,
                    term3=term3, term4=term4, total=total, d_total=total - rot,
                    remainder=rem, law=LAW[tag], gap1=gap1, reach=reach, s=sOv,
                    PQ2a=bool(ok2a), PQ2b=bool(ok2b), PQ2c=bool(ok2c))
    print("D2 %s: rot %+.6e (d_rec %.1e) = T1 %+.4e + T2 %+.4e + T3 %+.1e + T4 %+.1e  d_tot %.1e"
          % (tag, rot, abs(d_rec), term1, term2, term3, term4, abs(total - rot)))
    print("   remainder(rot-T1-T2) %+.1e | T1-law %+.2e (reach %.1e)" % (rem, gap1, reach))
if CANFAIL:
    bad = abs(out['6s']['d_total'])
    print("CANFAIL (c2m skew 1e-6 at 6s): d_total=%.1e -> %s"
          % (bad, "rc=4 BREAK OK" if bad > 1e-12 else "rc=5 VACUOUS"))
    sys.exit(4 if bad > 1e-12 else 5)
PQ1a = q1a == 4; PQ1b = q1b == 4; PQ2a = q2a == 2; PQ2b = q2b == 2; PQ2c = q2c == 2
print("PQ1.a identity:   %d/4  %s" % (q1a, "HIT" if PQ1a else "MISS"))
print("PQ1.b structure:  %d/4  %s" % (q1b, "HIT" if PQ1b else "MISS"))
print("PQ2.a decomp:     %d/2  %s" % (q2a, "HIT" if PQ2a else "MISS"))
print("PQ2.b hessian:    %d/2  %s" % (q2b, "HIT" if PQ2b else "MISS"))
print("PQ2.c law gap:    %d/2  %s" % (q2c, "HIT" if PQ2c else "MISS"))
json.dump(dict(row=58, PQ1a=bool(PQ1a), PQ1b=bool(PQ1b), PQ2a=bool(PQ2a), PQ2b=bool(PQ2b),
               PQ2c=bool(PQ2c), parts=out, sec=int(time.time() - t0)),
          open(os.path.join(HERE, 'w104c-58.json'), 'w'), indent=1, default=float)
print("receipt w104c-58.json (%ds)" % (time.time() - t0))
