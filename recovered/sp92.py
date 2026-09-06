#!/usr/bin/env python3
"""sp92.py -- S92 ITEM 1 (ruling Y). Derive S/|P| from the field: frozen-orbital Slater-integral
screening S1 and bare-proton P1, built exactly as hfc2.run2 builds Vloc and X. c the only number.
usage: sp92.py ROW [--canfail A|B]   ROW in 38 56 58 90 91
"""
import sys, os, json, time, numpy as np
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'rt'))
os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'rt'))
import nlchain as NC, nlguard as NG, hfc2 as H
from t7c_kernel import C0
from t7b_hf import _c3j0sq

ROWS = {38: ['4d', '5s'], 56: ['5d', '6s'], 58: ['4f', '5d'], 90: ['6d', '5f'], 91: ['5f', '6d']}
LEV = dict(s=0, p=1, d=2, f=3)
def ch(tag): return (int(tag[0]), LEV[tag[1]])

def solve(Z, cfg, tag):
    """rung-0 first, same ladder as nlguard; returns object (orbitals) + E + rung"""
    for rung, (beta, maxit) in enumerate(NG.LADDER):
        h = H.HFC(Z, [tuple(x) for x in cfg], c=C0)
        E, _, it, eps = h.run2(beta=beta, maxit=maxit)
        if it < maxit: return h, float(E), rung
    raise RuntimeError(f"no convergence {Z} {tag}")

def S1_of(h, a, e, dq):
    """first-order change of channel a's one-electron energy when dq electrons enter shell e, orbitals frozen"""
    r, dr = h.r, h.dr; P = h.P; n, l = a; ne, le = e
    if a != e:
        F0 = float(np.sum(P[a] * P[a] * h.Yk(P[e], P[e], 0) / r * dr))
        G = 0.0
        for k in range(abs(l - le), l + le + 1, 2):
            G += 0.5 * _c3j0sq(l, k, le) * float(np.sum(P[a] * h.Yk(P[a], P[e], k) / r * P[e] * dr))
        return dq * (F0 - G), dq * F0, dq * G
    F0 = float(np.sum(P[a] * P[a] * h.Yk(P[a], P[a], 0) / r * dr))
    X = 0.0
    for k in range(2, 2 * l + 1, 2):
        X += (2 * l + 1) / (4 * l + 1) * _c3j0sq(l, k, l) * float(np.sum(P[a] * P[a] * h.Yk(P[a], P[a], k) / r * dr))
    return dq * (F0 - X), dq * F0, dq * X

def main():
    Zs = int(sys.argv[1]); canfail = sys.argv[3] if len(sys.argv) > 3 else None
    rows = NC.load(); tags = ROWS[Zs]
    cfg1 = NC.cfg_from_chain(Zs - 1, rows); cfg2 = NC.cfg_from_chain(Zs - 2, rows)
    ent = tuple(rows[Zs - 1]['ent_nl'])
    dq = 0 if canfail == 'A' else 1
    sealed = {t: dict(rows[Zs]['order']).get(t) for t in tags}
    sw = json.load(open(f'../pack91/swing91-{Zs}.json'))['rows']
    print(f"Z*={Zs} tags={tags} entrant={NC.tagof(ent)} dq={dq}", flush=True)
    t0 = time.time(); res = dict(Z=Zs, entrant=NC.tagof(ent), canfail=canfail, rows={})
    # reference at Z*: cfg(Z*-1)  (for D reproduction, can-fail B)
    _, Eref, rr = solve(Zs, cfg1, 'ref')
    _, Eref1, rr1 = solve(Zs - 1, cfg2, 'ref1')
    for t in tags:
        a = ch(t)
        hZ, EZ, r1 = solve(Zs, NC.add(cfg1, a), t)           # sealed state: has ch and entrant
        Drep = round(EZ - Eref, 5)
        if canfail == 'B': Drep = round(Drep + 0.01, 5)     # control: a wrong reproduction must be caught
        if sealed[t] is None or abs(Drep - sealed[t]) > 1.5e-5:
            print(f"CONTROL INVALID: D repro {Drep} vs sealed {sealed[t]}  rc=4", flush=True); sys.exit(4)
        h1, E1, r2 = solve(Zs - 1, NC.add(cfg2, a), t + '-1')  # D(Z*-1) state, no entrant
        S1, F0, X = S1_of(hZ, a, ent, dq)
        if abs(S1) < 1e-6:
            print(f"LEVER DEAD: S1={S1}  rc=4", flush=True); sys.exit(4)
        P1 = -float(np.sum(h1.P[a] ** 2 / h1.r * h1.dr))
        S, P = sw[t]['S'], sw[t]['P']
        row = dict(D_repro=Drep, D_sealed=sealed[t], D1_repro=round(E1 - Eref1, 5),
                   S1=round(S1, 5), F0=round(F0, 5), X=round(X, 5), S=S, P=P, P1=round(P1, 5),
                   rho_sealed=round(S / abs(P), 3), rho1=round(S1 / abs(P), 3), rho0=round(S1 / abs(P1), 3),
                   rel=round((S1 - S) / S, 3), rungs=[rr, rr1, r1, r2], own=(a == ent))
        res['rows'][t] = row
        print(f"  {t}{' OWN' if a==ent else ''}: Drep {Drep} sealed {sealed[t]} | S1 {row['S1']} (F0 {row['F0']} X {row['X']}) "
              f"S {S} rel {row['rel']} | P1 {row['P1']} P {P} | rho sealed {row['rho_sealed']} rho1 {row['rho1']} rho0 {row['rho0']}", flush=True)
    res['sec'] = int(time.time() - t0)
    with open(f'../pack92/sp92-{Zs}{"-cf"+canfail if canfail else ""}.json', 'w') as f: json.dump(res, f, indent=1)
    print("sec", res['sec'])

if __name__ == '__main__': main()
