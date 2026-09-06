#!/usr/bin/env python3
"""ts93.py -- S93 ITEM 3. Slater's relation in the field. Systems A=(Z*-1,cfg2) B=(Z*,cfg2) C=(Z*,cfg1), channel c = own.
   At q in 3-point Gauss-Legendre nodes on [0,1]: SCF solve with q_c = q; g(q) = dE/dq at fixed orbitals (central difference of the
   frozen functional, exact for the quadratic-in-Q functional); eps_c(q) the SCF eigenvalue. D from pack93/rel93-*.json.
usage: ts93.py ROW [--canfail A|B]"""
import sys, os, json, time, numpy as np
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'rt'))
os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'rt'))
import nlchain as NC, nlguard as NG, hfc2 as H
from t7c_kernel import C0
sys.path.insert(0, '../pack93'); from rel93 import solve, clone, Ione, Efun   # rel93 runs its main at import? guard below
assert H.CORR is False
OWN = {38: '5s', 56: '6s', 58: '5d', 90: '6d', 91: '6d'}
LEV = dict(s=0, p=1, d=2, f=3)
NODES = [0.5 - np.sqrt(3 / 20), 0.5, 0.5 + np.sqrt(3 / 20)]; W = [5 / 18, 8 / 18, 5 / 18]

def setq(cfg, a, q):
    d = {(n, l): qq for n, l, qq in cfg}; d[a] = d.get(a, 0) + q
    return [(n, l, qq) for (n, l), qq in sorted(d.items()) if qq > 1e-9]

def g_of(h, a, dq=1e-3):
    """dE/dq_a at fixed orbitals: central difference of the frozen functional around h's occupancy"""
    I = Ione(h); Q = {(n, l): q for n, l, q in h.occ}
    def E_at(q):
        occ = [(n, l, (q if (n, l) == a else qq)) for n, l, qq in h.occ]
        return Efun(clone(h, h.Z, occ), I)
    return (E_at(Q[a] + dq) - E_at(Q[a] - dq)) / (2 * dq)

def system(Z, core, a, cf):
    out = dict(Z=Z, N=sum(q for _, _, q in core), nodes=[], g=[], eps=[], rungs=[])
    for q in NODES:
        qq = 1.0 if cf == 'A' else q
        h, E, r = solve(Z, setq(core, a, qq))
        out['nodes'].append(round(q, 6)); out['g'].append(float(g_of(h, a))); out['eps'].append(float(h.eps[a])); out['rungs'].append(r)
    out['quad'] = float(sum(w * g for w, g in zip(W, out['g'])))
    return out

if __name__ == '__main__':
    Zs = int(sys.argv[1]); cf = sys.argv[3] if len(sys.argv) > 3 else None
    rows = NC.load(); t = OWN[Zs]; a = (int(t[0]), LEV[t[1]])
    cfg1 = NC.cfg_from_chain(Zs - 1, rows); cfg2 = NC.cfg_from_chain(Zs - 2, rows)
    rel = json.load(open(f'../pack93/rel93-{Zs}.json'))
    D = {k: rel[k]['E_N1'] - rel[k]['E_N'] + (1e-4 if cf == 'B' else 0.0) for k in 'ABC'}
    t0 = time.time(); res = dict(Z=Zs, own=t, canfail=cf, sys={})
    for k, (Z, core) in dict(A=(Zs - 1, cfg2), B=(Zs, cfg2), C=(Zs, cfg1)).items():
        s = system(Z, core, a, cf); s['D'] = round(D[k], 6); s['T1'] = round(s['quad'] - D[k], 6)
        s['T2'] = round(s['g'][1] - s['eps'][1], 6); s['T3'] = round(s['g'][1] - D[k], 6)
        if abs(s['T1']) > 3e-5: print(f"T1 FAIL/CONTROL: sys {k} quad {s['quad']:.6f} D {D[k]:.6f} diff {s['T1']:.2e} rc=4", flush=True); json.dump(dict(res, fail=k, sys_fail=s), open(f'../pack93/ts93-{Zs}{"-cf"+cf if cf else ""}.json', 'w'), indent=1); sys.exit(4)
        res['sys'][k] = s
        print(f"  {k} Z={Z} N={s['N']} g={[round(x,5) for x in s['g']]} eps={[round(x,5) for x in s['eps']]} quad={s['quad']:.6f} D={D[k]:.6f} T1={s['T1']:+.1e} T2={s['T2']:+.5f} T3={s['T3']:+.5f} rungs={s['rungs']}", flush=True)
    gA, gB, gC = (res['sys'][k]['g'][1] for k in 'ABC')
    sw = json.load(open(f'../pack91/swing91-{Zs}.json'))['rows'][t]
    res['rho_sealed'] = round(sw['S'] / abs(sw['P']), 4); res['rho_TS'] = round((gC - gB) / abs(gB - gA), 4)
    res['S_TS'] = round(gC - gB, 5); res['P_TS'] = round(gB - gA, 5); res['S'] = sw['S']; res['P'] = sw['P']
    res['S_quad'] = round(res['sys']['C']['quad'] - res['sys']['B']['quad'], 5); res['P_quad'] = round(res['sys']['B']['quad'] - res['sys']['A']['quad'], 5)
    res['sec'] = int(time.time() - t0)
    print({k: res[k] for k in ('Z', 'own', 'rho_sealed', 'rho_TS', 'S', 'S_TS', 'S_quad', 'P', 'P_TS', 'P_quad', 'sec')}, flush=True)
    json.dump(res, open(f'../pack93/ts93-{Zs}{"-cf"+cf if cf else ""}.json', 'w'), indent=1)
