#!/usr/bin/env python3
"""relax92.py -- S92 ITEM 2. Split S - S1 and P - P1 into the channel's own response (frozen-field eigen-solve)
and everyone else's response. Potentials built exactly as hfc2.run2 builds them (incl. SIC V_c). c the only number.
usage: relax92.py ROW [--canfail A|B]
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

def solve(Z, cfg):
    for rung, (beta, maxit) in enumerate(NG.LADDER):
        h = H.HFC(Z, [tuple(x) for x in cfg], c=C0)
        E, _, it, eps = h.run2(beta=beta, maxit=maxit)
        if it < maxit: return h, float(E), rung
    raise RuntimeError("no convergence")

def clone(h, Z, occ):
    """HFC object at nuclear charge Z with occupancy occ, carrying h's orbitals frozen"""
    g = H.HFC(Z, [tuple(x) for x in occ], c=C0); g.P = {k: v.copy() for k, v in h.P.items()}; g.eps = dict(h.eps); return g

def pot(g, a):
    """(Vloc, X) for channel a from g's frozen orbitals/occupancy, as in run2 (with V_c)"""
    P = g.P; r = g.r; keys = [(n, l) for n, l, q in g.occ]; Q = {(n, l): q for n, l, q in g.occ}
    n, l = a; Y0 = {k: g.Yk(P[k], P[k], 0) for k in keys}; Vc = g.corr_pot(P) if H.CORR else {k: 0.0 for k in keys}
    Vloc = -g.Z / r + sum((Q[b] if b != a else g._ceff(a, Q)) * Y0[b] / r for b in keys) + Vc[a]; X = np.zeros(g.npts)
    for b in keys:
        nb, lb = b
        if b == a:
            c = g._ceff(a, Q) * (2 * l + 1) / (4 * l + 1)
            if abs(c) > 1e-14:
                for k in range(2, 2 * l + 1, 2): Vloc = Vloc - c * _c3j0sq(l, k, l) * g.Yk(P[a], P[a], k) / r
        else:
            for k in range(abs(l - lb), l + lb + 1, 2): X += 0.5 * Q[b] * _c3j0sq(l, k, lb) * g.Yk(P[a], P[b], k) / r * P[b]
    return Vloc, X

def efrozen(g, a):
    """<a|h|a> with a's orbital frozen (first order)"""
    Vloc, X = pot(g, a); n, l = a; P = g.P[a]; r, dr = g.r, g.dr
    # kinetic+nuclear via the eigenvalue identity: eps = <T+Vloc> - <X P>; use SCF eps of the parent to get <T> once
    return Vloc, X

def esolve(g, a):
    Vloc, X = pot(g, a); n, l = a
    u, e, nd, res = g.solve_one(l, n, Vloc, X, g.eps[a], g.P[a])
    if nd != n - l - 1: raise RuntimeError(f"nodes {nd} for {a}")
    return float(e)

def main():
    Zs = int(sys.argv[1]); canfail = sys.argv[3] if len(sys.argv) > 3 else None
    rows = NC.load(); tags = ROWS[Zs]
    cfg1 = NC.cfg_from_chain(Zs - 1, rows); cfg2 = NC.cfg_from_chain(Zs - 2, rows)
    ent = tuple(rows[Zs - 1]['ent_nl']); dq = 0 if canfail == 'A' else 1
    sw = json.load(open(f'../pack91/swing91-{Zs}.json'))['rows']; sp = json.load(open(f'../pack92/sp92-{Zs}.json'))['rows']
    print(f"Z*={Zs} tags={tags} entrant={NC.tagof(ent)} dq={dq}", flush=True)
    t0 = time.time(); res = dict(Z=Zs, entrant=NC.tagof(ent), canfail=canfail, rows={})
    for t in tags:
        a = ch(t)
        G, EG, rG = solve(Zs, NC.add(cfg1, a)); Hh, EH, rH = solve(Zs - 1, NC.add(cfg2, a))
        # --- Q8 / can-fail B: frozen eigen-solve reproduces SCF eigenvalue
        e_rep = esolve(G, a) + (0.01 if canfail == 'B' else 0.0)
        if abs(e_rep - G.eps[a]) > 1e-5:
            print(f"CONTROL INVALID: e_rep {e_rep:.6f} vs eps {G.eps[a]:.6f}  rc=4", flush=True); sys.exit(4)
        # --- S pieces on G: with entrant (G itself) vs without (entrant occupancy - dq)
        occ_wo = [(n, l, q - (dq if (n, l) == ent else 0)) for n, l, q in G.occ]; occ_wo = [x for x in occ_wo if x[2] > 1e-9]
        Gwo = clone(G, Zs, occ_wo)
        Vw, Xw = pot(G, a); Vo, Xo = pot(Gwo, a); Pa = G.P[a]; dr = G.dr
        S1c = float(np.sum(Pa * (Vw - Vo) * Pa * dr) - np.sum(Pa * (Xw - Xo) * dr))
        if abs(S1c) < 1e-6:
            print(f"LEVER DEAD: S1c={S1c}  rc=4", flush=True); sys.exit(4)
        e_w = G.eps[a]; e_o = esolve(Gwo, a)
        S_self = (e_w - e_o) - S1c
        S = sw[t]['S']; S1 = sp[t]['S1']; S_c = S1c - S1; S_oth = S - S1c - S_self
        # --- P pieces on H: Z*-1 (H itself) vs Z* with all else frozen
        Hz = clone(Hh, Zs, Hh.occ)
        P1 = -float(np.sum(Hh.P[a] ** 2 / Hh.r * Hh.dr))
        e_z = esolve(Hz, a); e_h = Hh.eps[a]
        P_self = (e_z - e_h) - P1
        P = sw[t]['P']; P_oth = P - P1 - P_self
        rho2 = (S1c + S_self) / abs(P1 + P_self)
        row = dict(S=S, S1=S1, S1c=round(S1c, 5), S_c=round(S_c, 5), S_self=round(S_self, 5), S_oth=round(S_oth, 5),
                   P=P, P1=round(P1, 5), P_self=round(P_self, 5), P_oth=round(P_oth, 5),
                   rho_sealed=round(S / abs(P), 3), rho2=round(rho2, 3), e_rep_err=round(e_rep - G.eps[a], 7),
                   rungs=[rG, rH], own=(a == ent))
        res['rows'][t] = row
        print(f"  {t}{' OWN' if a==ent else ''}: S {S} = S1c {row['S1c']} (S_c {row['S_c']}) + self {row['S_self']} + oth {row['S_oth']} | "
              f"P {P} = P1 {row['P1']} + self {row['P_self']} + oth {row['P_oth']} | rho sealed {row['rho_sealed']} rho2 {row['rho2']}", flush=True)
    res['sec'] = int(time.time() - t0)
    with open(f'../pack92/relax92-{Zs}{"-cf"+canfail if canfail else ""}.json', 'w') as f: json.dump(res, f, indent=1)
    print("sec", res['sec'])

if __name__ == '__main__': main()
