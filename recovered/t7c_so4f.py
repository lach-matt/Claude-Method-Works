#!/usr/bin/env python3
"""t7c_so4f.py -- session 20, candidate (d) of bridge-19 s6: first-order LEVEL-TO-LEVEL spin-orbit on the 4f rows of t7c_mult.
zeta_4f as t7c_so.py (alpha^2/2 <P|(1/r)dV/dr|P> on the converged SR-pol TS potential, own channel, neutral TS occ = ground - 0.5 on 4f).
Lande on a more-than-half-filled shell: lambda = -zeta/(2S), ground J = L+S  ->  E_SO(ground) = -zeta*L/2.
Level-to-level object: E' = corr + (zeta/2)(L_ion - L_neutral).  Terms (Hund): 4f10 5I L=6, 4f9 6H L=5, 4f12 3H L=5, 4f11 4I L=6, 4f13 2F L=3, 4f14 1S L=0.
PREDICTION PD1: Dy over-binding grows ~0.005, (d) does not close it.  PD2: all four rows end shallow (dev>0), Yb ~ +0.02.  No constant, no measured input.
usage: python3 t7c_so4f.py 66 68 69 70   (appends to t7c_so4f.jsonl)
"""
import sys, json, numpy as np, warnings; warnings.filterwarnings("ignore")
from t5_scf import ground_occ, minus
from t7c_pol import scf_pol_sr
from t7c_kernel import numerov_wf_sr, C0
LT = {10: 6, 9: 5, 12: 5, 11: 6, 13: 3, 14: 0}     # Hund ground-term L by 4f count (more than half full)
def zeta(Z, q, occ, n, l):
    probe, Es, h = scf_pol_sr(Z, q, occ=occ, c=C0)
    cells = {nm: c.cell_contents for nm, c in zip(probe.__code__.co_freevars, probe.__closure__)}
    Vf = cells['Vf']; occd = {(a, b): k for a, b, k in occ}; s = "d" if occd.get((n, l), 0) >= 2*l+1 else "u"
    rr, drr, u, E, nd = numerov_wf_sr(Vf[s][0], l, n, 1.0, Z, C0, Vp=Vf[s][1], Vpp=Vf[s][2]); u = u/np.sqrt(np.sum(u*u*drr))
    return E, float((1.0/C0**2)/2*np.sum(u*u*Vf[s][1](rr)/rr*drr)), len(h)
M = {json.loads(l)['Z']: json.loads(l) for l in open('t7c_mult.jsonl')}
for Z in map(int, sys.argv[1:]):
    m = M[Z]; nf = 14 - m['holes'][0]; occ = minus(ground_occ(Z), 4, 3, 0.5)
    E, z, it = zeta(Z, 1, occ, 4, 3)
    Ln, Li = LT[nf], LT[nf-1]; sh = 0.5*z*(Li - Ln); e1 = m['corr'] + sh
    row = dict(Z=Z, el=m['el'], nf=nf, E_ts=round(E, 4), zeta_4f=round(z, 5), L_n=Ln, L_i=Li, shift_so=round(sh, 4), corr=m['corr'],
               corr_so=round(e1, 4), meas=m['meas'], dev1=m['dev1'], dev2=round(100*(e1-m['meas'])/abs(m['meas']), 1), it=it)
    open('t7c_so4f.jsonl', 'a').write(json.dumps(row)+'\n'); print(row, flush=True)
