#!/usr/bin/env python3
"""slater93.py -- S93 ITEM 3. D(c;Z,core) = int_0^1 g_c(q) dq, g_c = eps_c(q) + u_cc(q)/2, 3-point Gauss-Legendre.
   systems A=(Z*-1,cfg2) B=(Z*,cfg2) C=(Z*,cfg1), channel c = own shell.  usage: slater93.py ROW [--canfail A|B]"""
import sys, os, json, time, numpy as np
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'rt'))
os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'rt'))
import nlchain as NC, nlguard as NG, hfc2 as H
from t7c_kernel import C0
from t7b_hf import _c3j0sq
assert H.CORR is False, "sealed field is CORR=False"
OWN = {38: '5s', 56: '6s', 58: '5d', 90: '6d', 91: '6d'}
LEV = dict(s=0, p=1, d=2, f=3)
GLX = np.array([0.5 - np.sqrt(3 / 5) / 2, 0.5, 0.5 + np.sqrt(3 / 5) / 2]); GLW = np.array([5 / 18, 8 / 18, 5 / 18])

def solve(Z, cfg):
    for rung, (beta, maxit) in enumerate(NG.LADDER):
        h = H.HFC(Z, [tuple(x) for x in cfg], c=C0); E, _, it, eps = h.run2(beta=beta, maxit=maxit)
        if it < maxit: return h, float(E), rung
    raise RuntimeError("no convergence")

def setq(cfg, a, q):
    d = {(n, l): x for n, l, x in cfg}; d[a] = d.get(a, 0.0) + q
    return [(n, l, x) for (n, l), x in sorted(d.items()) if x > 1e-9]

def u_cc(h, a, dead=False):
    if dead: return 0.0
    n, l = a; P = h.P[a]; r = h.r; dr = h.dr
    V = h.Yk(P, P, 0) / r
    for k in range(2, 2 * l + 1, 2): V = V - (2 * l + 1) / (4 * l + 1) * _c3j0sq(l, k, l) * h.Yk(P, P, k) / r
    return float(np.sum(P * V * P * dr))

def system(Z, core, a, cf):
    h1, E1, r1 = solve(Z, setq(core, a, 1.0)); h0, E0, r0 = solve(Z, core)
    D = E1 - E0 + (1e-4 if cf == 'B' else 0.0)
    g = []; e = []; u = []; rungs = [r1, r0]
    for q in GLX:
        hq, Eq, rq = solve(Z, setq(core, a, float(q))); rungs.append(rq)
        eq = float(hq.eps[a]); uq = u_cc(hq, a, dead=(cf == 'A')); e.append(eq); u.append(uq); g.append(eq + 0.5 * uq)
    g = np.array(g); e = np.array(e); u = np.array(u)
    GL3 = float(np.sum(GLW * g)); INTe = float(np.sum(GLW * e)); INTu = float(np.sum(GLW * u))
    u1 = u_cc(h1, a); g1 = float(h1.eps[a]) + 0.5 * u1
    return dict(Z=Z, N=round(sum(x for _, _, x in core), 3), D=round(D, 6), GL3=round(GL3, 6), J1=round(D - GL3, 6),
                int_eps=round(INTe, 6), J2=round(D - INTe, 6), half_int_u=round(0.5 * INTu, 6), TS=round(float(g[1]), 6), J3=round(D - float(g[1]), 6),
                g_nodes=[round(float(x), 6) for x in g], eps_nodes=[round(float(x), 6) for x in e], u_nodes=[round(float(x), 6) for x in u],
                monotone=bool(g[0] < g[1] < g[2]), eps1=round(float(h1.eps[a]), 6), u1=round(u1, 6), g1=round(g1, 6),
                deficit=round(GL3 - g1, 6), Rel=round(D - float(h1.eps[a]), 6), Rel_check=round(0.5 * u1 - (g1 - GL3), 6), rungs=rungs)

Zs = int(sys.argv[1]); cf = sys.argv[3] if len(sys.argv) > 3 else None
rows = NC.load(); t = OWN[Zs]; a = (int(t[0]), LEV[t[1]])
cfg1 = NC.cfg_from_chain(Zs - 1, rows); cfg2 = NC.cfg_from_chain(Zs - 2, rows)
sealed = dict(rows[Zs]['order'])[t]; sw = json.load(open(f'../pack91/swing91-{Zs}.json'))['rows'][t]
t0 = time.time()
C = system(Zs, cfg1, a, cf)
if abs(C['D'] - sealed) > 1.5e-5: print(f"CONTROL INVALID: Drep {C['D']} sealed {sealed} rc=4"); sys.exit(4)
if abs(C['J1']) > 1e-3: print(f"IDENTITY FAILS on C: D-GL3 = {C['J1']}  rc=4"); sys.exit(4)
B = system(Zs, cfg2, a, cf); A = system(Zs - 1, cfg2, a, cf)
S_int = C['GL3'] - B['GL3']; P_int = B['GL3'] - A['GL3']
res = dict(Z=Zs, own=t, A=A, B=B, C=C, S_sealed=sw['S'], S_int=round(S_int, 6), P_sealed=sw['P'], P_int=round(P_int, 6),
           rho_sealed=round(sw['S'] / abs(sw['P']), 4), rho_int=round(S_int / abs(P_int), 4), sec=int(time.time() - t0))
print(json.dumps({k: v for k, v in res.items() if k not in 'ABC'}), flush=True)
for s in 'ABC':
    x = res[s]; print(s, x['Z'], x['N'], 'D', x['D'], 'GL3', x['GL3'], 'J1', x['J1'], 'J2', x['J2'], 'J3', x['J3'], 'mono', x['monotone'],
                      'deficit', x['deficit'], 'Rel', x['Rel'], 'Rel_chk', x['Rel_check'], 'rungs', x['rungs'], flush=True)
json.dump(res, open(f'../pack93/slater93-{Zs}{"-cf"+cf if cf else ""}.json', 'w'), indent=1)
