#!/usr/bin/env python3
"""corr94.py -- S94 ITEM 4. Correlation forms Z/R/S as a lever on the sealed margin at rows 38 56 72 89 105.
   Patches hfc2's correlation (T.v_gbz potential, H.eps_c energy) per form, as corr_ring.py documents; CORR toggled via H.CORR.
usage: corr94.py ROW [forms]   (default forms: none Z R S)  |  corr94.py 89 --canfail A|B   rc=4 on a fired can-fail.
output: pack94/corr94-ROW.json"""
import sys, os, json, time, numpy as np
HERE = os.path.dirname(os.path.abspath(__file__)); RT = os.path.join(HERE, '..', 'rt')
sys.path.insert(0, RT); os.chdir(RT)
import nlchain as NC, nlguard as NG, hfc2 as H, t7c_cuaudit as T, corr_ring as CR, corr_sosex as CS
from t7c_kernel import C0
ROWS = {d['Z']: d for d in map(json.loads, open('nlchain.jsonl'))}
V0, E0 = T.v_gbz, H.eps_c                      # the Z form (hfc2 default)
FORMS = {'none': None, 'Z': (V0, E0), 'R': (CR.v_R, CR.eps_R), 'S': (CS.v_S, CS.eps_S)}

def set_form(f, scale=1.0):
    if f == 'none': H.CORR = False; return
    v, e = FORMS[f]
    if scale == 1.0: T.v_gbz, H.eps_c = v, e
    else:
        T.v_gbz = lambda nu, nd: tuple(scale * x for x in v(nu, nd)); H.eps_c = lambda nu, nd: scale * e(nu, nd)
    H.CORR = True

def solve(Z, cfg):
    for rung, (beta, maxit) in enumerate(NG.LADDER):
        h = H.HFC(Z, [tuple(x) for x in cfg], c=C0); E, _, it, eps = h.run2(beta=beta, maxit=maxit)
        if it < maxit: return float(E), rung, it
    raise RuntimeError("no convergence")

def tag2nl(t): return (int(t[0]), 'spdfg'.index(t[1]))

def row(Z, forms, scale=1.0):
    d = ROWS[Z]; ent = tag2nl(d['order'][0][0]); run = tag2nl(d['order'][1][0]); m0 = d['order'][1][1] - d['order'][0][1]
    ref = NC.cfg_from_chain(Z - 1, ROWS); out = dict(Z=Z, ent=d['order'][0][0], run=d['order'][1][0], m_sealed=m0, D_ent_sealed=d['order'][0][1],
                                                    D_run_sealed=d['order'][1][1], forms={})
    for f in forms:
        set_form(f, scale); t0 = time.time()
        Er, r0, i0 = solve(Z, ref); Ee, r1, i1 = solve(Z, NC.add(ref, ent)); Eu, r2, i2 = solve(Z, NC.add(ref, run))
        De, Du = Ee - Er, Eu - Er; m = Du - De
        out['forms'][f] = dict(D_ent=De, D_run=Du, m=m, dm=m - m0, rungs=[r0, r1, r2], its=[i0, i1, i2], sec=round(time.time() - t0, 1))
        print(Z, f, 'D_ent %.5f D_run %.5f m %.5f dm %+.5f rungs %s' % (De, Du, m, m - m0, [r0, r1, r2]), flush=True)
    return out

if __name__ == '__main__':
    Z = int(sys.argv[1]); cf = sys.argv[sys.argv.index('--canfail') + 1] if '--canfail' in sys.argv else None
    if cf == 'A':
        o = row(Z, ['Z'], scale=0.0); dm = o['forms']['Z']['dm']
        print('CF-A dm under zeroed correlation = %+.2e' % dm); sys.exit(4 if abs(dm) < 1e-6 else 1)
    if cf == 'B':
        o1 = row(Z, ['Z']); o10 = row(Z, ['Z'], scale=10.0); a, b = o1['forms']['Z']['dm'], o10['forms']['Z']['dm']
        print('CF-B dm x1 %+.5f  x10 %+.5f  ratio %.2f' % (a, b, b / a if a else float('inf'))); sys.exit(4 if abs(b) > 3 * abs(a) else 1)
    forms = [a for a in sys.argv[2:] if a in FORMS] or ['none', 'Z', 'R', 'S']
    o = row(Z, forms); p = os.path.join(HERE, 'corr94-%d.json' % Z)
    old = json.load(open(p)) if os.path.exists(p) else o; old['forms'].update(o['forms']); json.dump(old, open(p, 'w'), indent=1)
