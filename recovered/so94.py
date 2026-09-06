#!/usr/bin/env python3
"""so94.py -- S94 ITEM 1 (Law B). Spin-orbit splitting of the SEALED entrant vs the SEALED margin, all rows.
   For row Z: system = nucleus Z, cfg(Z-1)_chain + entrant (n,l) [the nlchain reference object], solved in the sealed field
   (hfc2, SR, CORR=False, c=C0). On the converged object:
     zeta_loc = (1/(2 c^2)) <P| (1/r) dVloc/dr |P>,   Vloc = -Z/r + direct Coulomb (self-shell ceff=Q-1 as in run2)   [PRIMARY]
     zeta_X   = same with Vloc + X/P (Slater-local projection of the nonlocal exchange)                               [SENSITIVITY ONLY]
     Delta_SO = zeta*(2l+1)/2 ;  r(Z) = Delta_SO / m(Z), m(Z) = sealed margin (nlchain.jsonl).
   l=0 entrants: Delta_SO = 0 by construction; reported, not scored.
   DECLARED: the nonlocal HF exchange has no dV/dr; zeta is taken on the LOCAL potential (primary), exchange-projected as sensitivity.
   DECLARED: pack19/t7c_so.py computed zeta on the t7c_pol TS-SR-pol field (scf_pol_sr), NOT on hfc2. B5 is therefore a cross-field
             comparison, not a reproduction. The in-field lever check (can-fail B) perturbs the ROW-103 7p/6d zeta against a frozen
             reference written by the first clean run of this instrument (pack94/so94-ref103.json).
   CLIGHT env override: CLIGHT=1e6 for can-fail A (lever-dead).
usage: so94.py Z1 Z2 [--canfail A|B]     appends pack94/so94.jsonl (key Z); rc=4 on a fired can-fail.
"""
import sys, os, json, time, numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', 'rt')); os.chdir(os.path.join(HERE, '..', 'rt'))
import nlchain as NC, nlguard as NG, hfc2 as H
from t7c_kernel import C0 as C0_SEALED
from t7b_hf import _c3j0sq
assert H.CORR is False, "sealed field is CORR=False"
C = float(os.environ.get('CLIGHT', C0_SEALED))
OUT = os.path.join(HERE, 'so94.jsonl'); REF = os.path.join(HERE, 'so94-ref103.json')
ROWS = {d['Z']: d for d in map(json.loads, open('nlchain.jsonl'))}

def solve(Z, cfg):
    for rung, (beta, maxit) in enumerate(NG.LADDER):
        h = H.HFC(Z, [tuple(x) for x in cfg], c=C); E, _, it, eps = h.run2(beta=beta, maxit=maxit)
        if it < maxit: return h, float(E), rung, it
    raise RuntimeError("no convergence")

def pot(g, a):
    """(Vloc incl. -Z/r, X) for shell a, as in hfc2.run2 (CORR=False); verbatim form of rel93.pot"""
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

def zeta(g, a, c):
    Vloc, X = pot(g, a); P = g.P[a]; r = g.r; dr = g.dr
    norm = float(np.sum(P * P * dr)); P = P / np.sqrt(norm)
    dV = np.gradient(Vloc, r)
    z_loc = float(np.sum(P * P * dV / r * dr) / (2 * c * c))
    with np.errstate(divide='ignore', invalid='ignore'):
        Vx = np.where(np.abs(P) > 1e-8, X / np.where(np.abs(P) > 1e-8, P, 1.0), 0.0)
    dVx = np.gradient(Vloc + Vx, r)
    z_x = float(np.sum(P * P * dVx / r * dr) / (2 * c * c))
    return z_loc, z_x, norm

def row(Z, canfail=None):
    d = ROWS[Z]; n, l = d['ent_nl']; m = float(d['margin'])
    cfg = NC.add(NC.cfg_from_chain(Z - 1, ROWS), (n, l))
    t0 = time.time(); g, E, rung, it = solve(Z, cfg)
    Drep = E - None if False else None
    zl, zx, norm = zeta(g, (n, l), C)
    dso_l = zl * (2 * l + 1) / 2; dso_x = zx * (2 * l + 1) / 2
    out = dict(Z=Z, ent=d['ent'], n=n, l=l, label=d['label'], margin=m, zeta_loc=zl, zeta_x=zx, dso_loc=dso_l, dso_x=dso_x,
               r_loc=(dso_l / m if l > 0 else 0.0), r_x=(dso_x / m if l > 0 else 0.0), eps_ent=float(g.eps[(n, l)]),
               E=E, rung=rung, it=it, norm=norm, c=C, scored=(l > 0 and Z <= 108), sec=round(time.time() - t0, 1))
    return out, g

if __name__ == '__main__':
    cf = None
    if '--canfail' in sys.argv: cf = sys.argv[sys.argv.index('--canfail') + 1]
    args = [int(a) for a in sys.argv[1:] if a.isdigit()]
    if cf == 'A':
        assert C > 1e5, "can-fail A requires CLIGHT=1e6"
        bad = []
        for Z in (58, 90, 103):
            o, _ = row(Z); print('CF-A', Z, o['ent'], 'zeta_loc', o['zeta_loc'], flush=True)
            if abs(o['zeta_loc']) >= 1e-9: bad.append(Z)
        if not bad: print("CF-A: lever-dead -> every zeta < 1e-9 (c=1e6). FIRES rc=4 as designed."); sys.exit(4)
        print("CF-A: FAILED TO FIRE (zeta survives c->inf): instrument broken"); sys.exit(1)
    if cf == 'B':
        ref = json.load(open(REF)); o, g = row(103)
        # lever: perturb the in-field 7p zeta by 10% and test the 3-sf reproduction gate
        zp = o['zeta_loc'] * 1.10
        rel = abs(zp - ref['zeta_loc']) / abs(ref['zeta_loc'])
        print('CF-B', 'row103', o['ent'], 'zeta_loc', o['zeta_loc'], 'ref', ref['zeta_loc'], 'perturbed rel err', rel)
        if rel > 5e-3: print("CF-B: 10% perturbation trips the 3-sf gate. FIRES rc=4 as designed."); sys.exit(4)
        print("CF-B: FAILED TO FIRE: gate vacuous"); sys.exit(1)
    Z1, Z2 = args
    for Z in range(Z1, Z2 + 1):
        o, g = row(Z)
        print(json.dumps({k: (round(v, 7) if isinstance(v, float) else v) for k, v in o.items()}), flush=True)
        open(OUT, 'a').write(json.dumps(o) + '\n')
        if Z == 103 and not os.path.exists(REF) and abs(C - C0_SEALED) < 1e-9:
            json.dump(o, open(REF, 'w'))
