#!/usr/bin/env python3
"""w102.py -- S102 ITEM 1. Piecewise du/dx isolation, row 58. Prediction pack102/PREDICTION-S102-ITEM1.md
hash-gated. Symmetrized EXACT split of every endpoint difference into wavefunction response (outer P) and
potential/slot response (U, X functions):
  f(a,b) := <P_a U_b P_a>  (dir)   g(a,b) := <P_a X_b>  (exch; X_b = exchange function from solution b)
  du_wf  = (1/2)[f(+,+)-f(-,+) + f(+,-)-f(-,-)]/dq2 ; du_pot = (1/2)[f(-,+)-f(-,-) + f(+,+)-f(+,-)]/dq2
  (same for dx with g). Telescoping: du_wf + du_pot == du_num EXACT. c the only number.
usage: w102.py [--canfail]"""
import sys, os, json, time, hashlib, numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', 'rt')); os.chdir(os.path.join(HERE, '..', 'rt'))
p = os.path.join(HERE, 'PREDICTION-S102-ITEM1.md')
if hashlib.sha256(open(p, 'rb').read()).hexdigest() != open(p + '.sha256').read().split()[0]:
    print("HALT rc=3 sha"); sys.exit(3)
CANFAIL = '--canfail' in sys.argv
import nlchain as NC, hfc2 as H
sys.path.insert(0, '../pack93'); from ffun93 import solve, clone, Ione, Efun, pot
assert H.CORR is False
ROW = 58; ent = (5, 2); Zs = 58; dq2 = 0.2
rows = NC.load(); cfg2 = NC.cfg_from_chain(56, rows)
def setq(cfg, a, q):
    d = {(n, l): qq for n, l, qq in cfg}; d[a] = d.get(a, 0) + q
    return [(n, l, qq) for (n, l), qq in sorted(d.items()) if qq > 1e-9]
t0 = time.time(); sol = {}
for q in (0.4, 0.5, 0.6):
    sol[q] = solve(Zs, setq(cfg2, ent, q))[0]
    print("  solved q=%.1f (%ds)" % (q, time.time() - t0), flush=True)
h5, hp, hm = sol[0.5], sol[0.6], sol[0.4]
assert np.array_equal(h5.r, hp.r) and np.array_equal(h5.r, hm.r)
keys = [(n, l) for n, l, q in h5.occ]; Q5 = {(n, l): q for n, l, q in h5.occ}
r = h5.r; dr = h5.dr
# potential slots per shell per endpoint solution
U = {}; X = {}
for tag, hh in (('p', hp), ('m', hm), ('5', h5)):
    for c in keys:
        V, Xc = pot(hh, c); U[(tag, c)] = V + hh.Z / r; X[(tag, c)] = Xc
P = {('p', c): hp.P[c] for c in keys}; P.update({('m', c): hm.P[c] for c in keys})
# sign-fix endpoint orbitals against h5 (as a101) for dP; raw split uses squared/paired forms
dP = {}
for c in keys:
    Pp, Pm = hp.P[c].copy(), hm.P[c].copy()
    if float(np.sum(Pp * h5.P[c] * dr)) < 0: Pp = -Pp
    if float(np.sum(Pm * h5.P[c] * dr)) < 0: Pm = -Pm
    P[('p', c)], P[('m', c)] = Pp, Pm
    d = (Pp - Pm) / dq2; d -= float(np.sum(d * h5.P[c] * dr)) * h5.P[c]
    dP[c] = d
def f(a, b, c): return float(np.sum(P[(a, c)]**2 * U[(b, c)] * dr))
def g(a, b, c): return float(np.sum(P[(a, c)] * X[(b, c)] * dr))
# a101 model slot terms (for the pot-column comparison)
from t7b_hf import _c3j0sq
Qp = dict(Q5); Qp[ent] = 0.6
Qm = dict(Q5); Qm[ent] = 0.4
dceff = (h5._ceff(ent, Qp) - h5._ceff(ent, Qm)) / dq2
def J0(a, b): return float(np.sum(h5.P[a]**2 * (h5.Yk(h5.P[b], h5.P[b], 0) / r) * dr))
def Kk(a, b, k): return float(np.sum(h5.P[a] * h5.P[b] * (h5.Yk(h5.P[a], h5.P[b], k) / r) * dr))
ref = json.load(open(os.path.join(HERE, '..', 'pack101', 'd101-58.json')))
R2p = ref['R2_parts']; R2 = ref['R2_chain']
out = {}; tot_law = 0.0; sum_wf_col = 0.0; sum_pot_col = 0.0; worst_id = 0.0
print("shell   du_num      du_wf+du_pot resid | dx_num      dx_wf+dx_pot resid")
for c in keys:
    n, l = c
    du_num = (f('p', 'p', c) - f('m', 'm', c)) / dq2
    du_wf = 0.5 * ((f('p', 'p', c) - f('m', 'p', c)) + (f('p', 'm', c) - f('m', 'm', c))) / dq2
    du_pot = 0.5 * ((f('m', 'p', c) - f('m', 'm', c)) + (f('p', 'p', c) - f('p', 'm', c))) / dq2
    dx_num = (g('p', 'p', c) - g('m', 'm', c)) / dq2
    dx_wf = 0.5 * ((g('p', 'p', c) - g('m', 'p', c)) + (g('p', 'm', c) - g('m', 'm', c))) / dq2
    dx_pot = 0.5 * ((g('m', 'p', c) - g('m', 'm', c)) + (g('p', 'p', c) - g('p', 'm', c))) / dq2
    if CANFAIL and c == (5, 1):
        du_wf += 1e-8  # lever: identity below must break
    r1 = du_wf + du_pot - du_num; r2 = dx_wf + dx_pot - dx_num
    worst_id = max(worst_id, abs(r1), abs(r2))
    deps = (hp.eps[c] - hm.eps[c]) / dq2
    # a101 model columns
    mwf_du = 2 * float(np.sum(dP[c] * U[('5', c)] * h5.P[c] * dr))
    mwf_dx = 2 * float(np.sum(dP[c] * X[('5', c)] * dr))
    if c == ent:
        kap = (2 * l + 1) / (4 * l + 1)
        mslot = dceff * (J0(c, c) - kap * sum(_c3j0sq(l, k, l) * Kk(c, c, k) for k in range(2, 2 * l + 1, 2)))
        mxslot = 0.0
    else:
        mslot = J0(c, ent)
        mxslot = sum(0.5 * _c3j0sq(l, k, ent[1]) * Kk(c, ent, k)
                     for k in range(abs(l - ent[1]), l + ent[1] + 1, 2) if _c3j0sq(l, k, ent[1]) > 1e-14)
    # gap columns (model - exact), law-signed: gap contribution to part = q[-(du_model-du) + (dx_model-dx)]
    wf_cell = Q5[c] * (-(mwf_du - du_wf) + (mwf_dx - dx_wf))
    pot_cell = Q5[c] * (-(mslot - du_pot) + (mxslot - dx_pot))
    sum_wf_col += wf_cell; sum_pot_col += pot_cell
    part_exact = Q5[c] * (deps - du_wf - du_pot + dx_wf + dx_pot)
    tot_law += part_exact
    k = "%d%s" % (n, 'spdf'[l])
    out[k] = dict(du_num=du_num, du_wf=du_wf, du_pot=du_pot, dx_num=dx_num, dx_wf=dx_wf, dx_pot=dx_pot,
                  id_resid=max(abs(r1), abs(r2)), model_wf_du=mwf_du, model_slot=mslot,
                  model_wf_dx=mwf_dx, model_xslot=mxslot, wf_cell=wf_cell, pot_cell=pot_cell,
                  part_exact=part_exact, chain=R2p.get(k))
    print(" %-4s %+11.4e %+11.4e %+.0e | %+11.4e %+11.4e %+.0e" % (k, du_num, du_wf + du_pot, r1, dx_num, dx_wf + dx_pot, r2))
if CANFAIL:
    print("CANFAIL lever active (5p du_wf +1e-8): worst_id=%.2e -> %s" % (worst_id, "rc=4 BREAK OK" if worst_id > 1e-9 else "rc=5 VACUOUS"))
    sys.exit(4 if worst_id > 1e-9 else 5)
# P1 score
p1 = worst_id <= 1e-12
# P2 score
tgap = sum_wf_col + sum_pot_col
p2 = (abs(sum_pot_col) >= 0.80 * abs(tgap)) and (abs(sum_wf_col) <= 0.20 * abs(tgap)) if tgap != 0 else False
# P3 score
ok = 0
for k, v in out.items():
    t = v['chain']
    if t is None: continue
    tol = max(0.15 * abs(t), 4e-6)
    if abs(v['part_exact'] - t) <= tol: ok += 1
p3 = (abs(tot_law - R2) <= 5e-6) and ok == 13
print("P1 identity: worst=%.2e  %s" % (worst_id, "HIT" if p1 else "MISS"))
print("P2 columns: wf=%+.4e  pot=%+.4e  total gap=%+.4e  (a101 gap ref -1.6e-3)  %s" % (sum_wf_col, sum_pot_col, tgap, "HIT" if p2 else "MISS"))
print("P3 law: total=%+.6e  R2=%+.6e  diff=%+.1e  shells %d/13  %s" % (tot_law, R2, tot_law - R2, ok, "HIT" if p3 else "MISS"))
json.dump(dict(row=ROW, worst_id=worst_id, wf_col=sum_wf_col, pot_col=sum_pot_col, tot_gap=tgap,
               tot_law=tot_law, R2=R2, shells_ok=ok, P1=bool(p1), P2=bool(p2), P3=bool(p3),
               parts=out, sec=int(time.time() - t0)),
          open(os.path.join(HERE, 'w102-58.json'), 'w'), indent=1)
print("receipt w102-58.json (%ds)" % (time.time() - t0))
