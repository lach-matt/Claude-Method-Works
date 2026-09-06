#!/usr/bin/env python3
"""jan93.py -- S93 ITEM 3. D(c;Z,core) = INT_0^1 dE/df df, dE/df = eps_c(f) + [qc - ceff(f)] U_cc(f); 5-pt Gauss-Legendre.
   systems: A=(Z*-1,cfg2) B=(Z*,cfg2) C=(Z*,cfg1), c = own shell.  usage: jan93.py ROW [--canfail A|B]"""
import sys, os, json, time, numpy as np
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'rt'))
os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'rt'))
import nlchain as NC, nlguard as NG, hfc2 as H
from t7c_kernel import C0
from t7b_hf import _c3j0sq
assert H.CORR is False
OWN = {38: '5s', 56: '6s', 58: '5d', 90: '6d', 91: '6d'}
LEV = dict(s=0, p=1, d=2, f=3)
GLX, GLW = np.polynomial.legendre.leggauss(5); NODES = 0.5 * (GLX + 1); WTS = 0.5 * GLW

def solve(Z, cfg, frac=None):
    for rung, (beta, maxit) in enumerate(NG.LADDER):
        h = H.HFC(Z, [tuple(x) for x in cfg], c=C0); h.frac = frac
        E, _, it, eps = h.run2(beta=beta, maxit=maxit)
        if it < maxit: return h, float(E), rung
    raise RuntimeError("no convergence")

def Ucc(h, a):
    P = h.P[a]; r = h.r; dr = h.dr; n, l = a; w = (2 * l + 1) / (4 * l + 1)
    V = h.Yk(P, P, 0) / r
    for k in range(2, 2 * l + 1, 2): V = V - w * _c3j0sq(l, k, l) * h.Yk(P, P, k) / r
    return float(np.sum(P * V * P * dr))

def withfrac(core, a, qc, f):
    occ = [(n, l, q) for n, l, q in core if (n, l) != a] + [(a[0], a[1], qc + f)]
    return sorted(occ), {a: (qc, f)}

def dEdf(h, a, qc, f, drop=False):
    ceff = (qc * (qc - 1.0) + 2.0 * f * qc) / (qc + f)
    return float(h.eps[a]) + (0.0 if drop else (qc - ceff) * Ucc(h, a))

def system(Z, core, a, cf):
    qc = dict(((n, l), q) for n, l, q in core).get(a, 0.0)
    hN, EN, rN = solve(Z, core); hN1, EN1, rN1 = solve(Z, NC.add(core, a))
    D = EN1 - EN + (1e-4 if cf == 'B' else 0.0)
    g = []; rungs = [rN, rN1]
    for f in NODES:
        occ, fr = withfrac(core, a, qc, float(f)); h, E, rg = solve(Z, occ, fr); rungs.append(rg)
        g.append(dEdf(h, a, qc, float(f), drop=(cf == 'A' and qc > 0)))
    I = float(np.dot(WTS, g))
    # J2 finite-difference check at f=1/2
    occ, fr = withfrac(core, a, qc, 0.5); hm, Em, rg = solve(Z, occ, fr); gm = dEdf(hm, a, qc, 0.5, drop=(cf == 'A' and qc > 0))
    Ep = solve(Z, *withfrac(core, a, qc, 0.52))[1]; Emn = solve(Z, *withfrac(core, a, qc, 0.48))[1]
    fd = (Ep - Emn) / 0.04
    return dict(Z=Z, N=sum(q for _, _, q in core), qc=qc, D=round(D, 6), I=round(I, 6), D_minus_I=round(D - I, 6), g=[round(x, 6) for x in g],
                monotone_dec=bool(all(g[i] > g[i + 1] for i in range(4))), g_half=round(gm, 6), fd_half=round(fd, 6), fd_err=round(fd - gm, 6),
                TS_err=round(D - gm, 6), eps_half=round(float(hm.eps[a]), 6), U_half=round(Ucc(hm, a), 6), rungs=rungs)

Zs = int(sys.argv[1]); cf = sys.argv[3] if len(sys.argv) > 3 else None
rows = NC.load(); t = OWN[Zs]; a = (int(t[0]), LEV[t[1]])
cfg1 = NC.cfg_from_chain(Zs - 1, rows); cfg2 = NC.cfg_from_chain(Zs - 2, rows); sealed = dict(rows[Zs]['order'])[t]
t0 = time.time(); out = dict(Z=Zs, own=t)
for name, Z, core in (('C', Zs, cfg1), ('B', Zs, cfg2), ('A', Zs - 1, cfg2)):
    s = system(Z, core, a, cf); out[name] = s
    if name == 'C' and abs(s['D'] - sealed) > 1.5e-5: print(f"CONTROL INVALID: Drep {s['D']:.5f} sealed {sealed} rc=4"); sys.exit(4)
    if abs(s['D_minus_I']) > 2e-5: print(f"IDENTITY FAILS at {name}: D-I = {s['D_minus_I']:.6f} (qc={s['qc']}) rc=4"); json.dump(out, open(f'../pack93/jan93-{Zs}{"-cf"+cf if cf else ""}.json', 'w'), indent=1); sys.exit(4)
    print(name, {k: v for k, v in s.items() if k != 'g'}, flush=True)
    if cf == 'A' and name == 'C': break
A, B, C = out['A'], out['B'], out['C']
out['S_int'] = round(C['I'] - B['I'], 6); out['P_int'] = round(B['I'] - A['I'], 6)
out['rho_int'] = round(out['S_int'] / abs(out['P_int']), 4); out['rho_sealed'] = round((C['D'] - B['D']) / abs(B['D'] - A['D']), 4)
out['rho_TS'] = round((C['g_half'] - B['g_half']) / abs(B['g_half'] - A['g_half']), 4); out['sec'] = int(time.time() - t0)
print({k: out[k] for k in ('S_int', 'P_int', 'rho_int', 'rho_sealed', 'rho_TS', 'sec')}, flush=True)
json.dump(out, open(f'../pack93/jan93-{Zs}{"-cf"+cf if cf else ""}.json', 'w'), indent=1)
