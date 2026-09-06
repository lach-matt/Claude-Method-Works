#!/usr/bin/env python3
"""rel93.py -- S93 ITEM 2. Relaxation energies by named responder.
   E[Q'; P] frozen-orbital functional (hfc2.run2 form, I_a from the converged core+c solve).
   Rel(Z,core)  = E_frozen(core) - E_SCF(core)   with E_frozen(core) = E[core; P_{core+c}]
   Rel_b        = E_frozen(core) - E[core; shell b re-solved self-consistently, others frozen]
   systems: A=(Z*-1,cfg2) B=(Z*,cfg2) C=(Z*,cfg1); each with its N+1 partner (core+c).
usage: rel93.py ROW [--canfail A|B]"""
import sys, os, json, time, numpy as np
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'rt'))
os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'rt'))
import nlchain as NC, nlguard as NG, hfc2 as H
from t7c_kernel import C0
from t7b_hf import _c3j0sq
assert H.CORR is False, "sealed field is CORR=False"
OWN = {38: '5s', 56: '6s', 58: '5d', 90: '6d', 91: '6d'}
LEV = dict(s=0, p=1, d=2, f=3)
def tag(a): return f"{a[0]}{'spdf'[a[1]]}"

def solve(Z, cfg):
    for rung, (beta, maxit) in enumerate(NG.LADDER):
        h = H.HFC(Z, [tuple(x) for x in cfg], c=C0); E, _, it, eps = h.run2(beta=beta, maxit=maxit)
        if it < maxit: return h, float(E), rung
    raise RuntimeError("no convergence")

def clone(h, Z, occ):
    g = H.HFC(Z, [tuple(x) for x in occ], c=C0); g.P = {k: v.copy() for k, v in h.P.items()}; g.eps = dict(h.eps); return g

def pot(g, a):
    """(Vloc incl. -Z/r, X) for shell a from g's orbitals and occupancy, as in run2 (CORR=False)"""
    P = g.P; r = g.r; keys = [(n, l) for n, l, q in g.occ]; Q = {(n, l): q for n, l, q in g.occ}
    n, l = a; Y0 = {k: g.Yk(P[k], P[k], 0) for k in keys}
    Vloc = -g.Z / r + sum((Q[b] if b != a else g._ceff(a, Q)) * Y0[b] / r for b in keys); X = np.zeros(g.npts)
    for b in keys:
        nb, lb = b
        if b == a:
            c = g._ceff(a, Q) * (2 * l + 1) / (4 * l + 1)
            if abs(c) > 1e-14:
                for k in range(2, 2 * l + 1, 2): Vloc = Vloc - c * _c3j0sq(l, k, l) * g.Yk(P[a], P[a], k) / r
        else:
            for k in range(abs(l - lb), l + lb + 1, 2): X += 0.5 * Q[b] * _c3j0sq(l, k, lb) * g.Yk(P[a], P[b], k) / r * P[b]
    return Vloc, X

def Ione(h):
    """one-electron integrals I_a = <T - Z/r> from the converged object h (eps - <Vloc+Z/r> + <X>)"""
    I = {}
    for n, l, q in h.occ:
        a = (n, l); Vloc, X = pot(h, a); P = h.P[a]; dr = h.dr
        I[a] = float(h.eps[a] - np.sum(P * (Vloc + h.Z / h.r) * P * dr) + np.sum(P * X * dr))
    return I

def Efun(g, I):
    """E[Q; P] = sum_a Q_a [ I_a + 1/2(<Vloc + Z/r> - <X>) ] with Vloc, X built for g's occupancy from g's orbitals"""
    E = 0.0
    for n, l, q in g.occ:
        a = (n, l); Vloc, X = pot(g, a); P = g.P[a]; dr = g.dr
        E += q * (I[a] + 0.5 * (np.sum(P * (Vloc + g.Z / g.r) * P * dr) - np.sum(P * X * dr)))
    return float(E)

def relax_one(g, b, maxit=400, tol=2e-6, beta=0.4, dead=False):
    """re-solve shell b to self-consistency in the frozen field of the others; returns (g', iterations)"""
    g = clone(g, g.Z, g.occ); n, l = b
    if dead: return g, 0
    for it in range(maxit):
        Vloc, X = pot(g, b); u, e, nd, res = g.solve_one(l, n, Vloc, X, g.eps[b], g.P[b])
        if nd != n - l - 1: raise RuntimeError(f"nodes {nd} for {b}")
        if np.sum(u * g.P[b] * g.dr) < 0: u = -u
        d = abs(e - g.eps[b]); newP = (1 - beta) * g.P[b] + beta * u; newP /= np.sqrt(np.sum(newP ** 2 * g.dr))
        g.P[b] = newP; g.eps[b] = (1 - beta) * g.eps[b] + beta * e
        if d < tol and it > 2: return g, it + 1
    raise RuntimeError(f"shell {b} did not converge")

def system(Z, core, a, cf):
    """all relaxation quantities for (Z, core) with removal of one electron from shell a"""
    hN1, EN1, r1 = solve(Z, NC.add(core, a)); hN, EN, r0 = solve(Z, core)
    I = Ione(hN1)
    Erep = Efun(hN1, I)                                     # functional reproduces SCF E on its own solve
    gF = clone(hN1, Z, [tuple(x) for x in core]); EF = Efun(gF, I) + (1e-4 if cf == 'B' else 0.0)
    K = EN1 - EF - float(hN1.eps[a])                        # Koopmans defect (exact 0 expected)
    if abs(K) > 1e-5: print(f"CONTROL INVALID: Koopmans defect {K:.2e} rc=4"); sys.exit(4)
    Rel = EF - EN; D = EN1 - EN; Rel1 = D - float(hN1.eps[a])
    relb = {}; its = {}
    for n, l, q in core:
        b = (n, l); gb, it = relax_one(gF, b, dead=(cf == 'A')); relb[tag(b)] = round(EF - Efun(gb, I), 6); its[tag(b)] = it
    return dict(Z=Z, N=sum(q for _, _, q in core), E_N1=round(EN1, 6), E_N=round(EN, 6), E_frozen=round(EF, 6), eps_c=round(float(hN1.eps[a]), 6),
                Erep_err=round(Erep - EN1, 8), K=round(K, 8), D=round(D, 5), Rel=round(Rel, 6), Rel_item1=round(Rel1, 6), Rel_b=relb, iters=its,
                rungs=[r1, r0], top=max(relb, key=lambda k: relb[k]))

Zs = int(sys.argv[1]); cf = sys.argv[3] if len(sys.argv) > 3 else None
rows = NC.load(); t = OWN[Zs]; a = (int(t[0]), LEV[t[1]])
cfg1 = NC.cfg_from_chain(Zs - 1, rows); cfg2 = NC.cfg_from_chain(Zs - 2, rows)
sealed = dict(rows[Zs]['order'])[t]
t0 = time.time()
C = system(Zs, cfg1, a, cf)
if abs(C['D'] - sealed) > 1.5e-5: print(f"CONTROL INVALID: Drep {C['D']} sealed {sealed} rc=4"); sys.exit(4)
B = system(Zs, cfg2, a, cf); A = system(Zs - 1, cfg2, a, cf)
SdN = C['Rel'] - B['Rel']; PdZ = B['Rel'] - A['Rel']
Relc1 = C['Rel_b'].get(t, 0.0); Relc2 = B['Rel_b'].get(t, 0.0)
if abs(Relc1) < 1e-7: print(f"LEVER DEAD: Rel_c(cfg1)={Relc1} rc=4"); sys.exit(4)
oth = sum(v for k, v in C['Rel_b'].items() if k != t) - sum(v for k, v in B['Rel_b'].items() if k != t)
res = dict(Z=Zs, own=t, A=A, B=B, C=C, S_minus_dN=round(SdN, 6), P_minus_dZ=round(PdZ, 6),
           Relc_diff=round(Relc1 - Relc2, 6), R1_ratio=round((Relc1 - Relc2) / SdN, 3), R2_ratio=round(oth / SdN, 3),
           R3_ratio=round(Relc1 / C['Rel'], 3), R4_ratio=round(abs(PdZ) / SdN, 3), R4_same_top=(A['top'] == B['top']), sec=int(time.time() - t0))
print(json.dumps({k: v for k, v in res.items() if k not in ('A', 'B', 'C')}), flush=True)
for s in 'ABC': print(s, res[s]['Z'], res[s]['N'], 'Rel', res[s]['Rel'], 'item1', res[s]['Rel_item1'], 'K', res[s]['K'], 'top', res[s]['top'], res[s]['Rel_b'], flush=True)
json.dump(res, open(f'../pack93/rel93-{Zs}{"-cf"+cf if cf else ""}.json', 'w'), indent=1)
