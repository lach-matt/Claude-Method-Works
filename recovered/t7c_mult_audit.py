#!/usr/bin/env python3
"""t7c_mult_audit.py -- session 20 (ii): bookkeeping audit of the Hund-II CI in t7c_mult.py (Dy over-binding).
A1 degeneracies: max-S manifold of f^k must split as f4: I13 G9 F7 D5 S1 (35); f5: H11 F7 P3 (21); f3: I13 G9 F7 D5 S1 (35); f2: H11 F7 P3 (21).
A2 particle-hole: term energies rel. to manifold average identical for k and 7-k (f4=f3, f5=f2).
A3 closed forms f2 (Condon-Shortley, F_2=F2/225 F_4=F4/1089 F_6=25F6/184041): 3H=-25F2-51F4-13F6, 3F=-10F2-33F4-286F6, 3P=45F2+33F4-1287F6 (rel. F0).
Uses Dy's banked F^k. Predictions: A1 HOLDS, A2 HOLDS, A3 HOLDS (if any fails, the CI is the fault, not the bookkeeping)."""
import numpy as np, itertools, json, sys
import t7c_mult as M
F={2:0.5013,4:0.3114,6:0.2232}   # Dy banked (t7c_mult.jsonl)
def spec(k):
    dets=[tuple(c) for c in itertools.combinations(list(M.MS),k)]; n=len(dets); H=np.zeros((n,n)); idx={d:i for i,d in enumerate(dets)}
    # rebuild H exactly as ci() does, but keep the spectrum
    src=open('t7c_mult.py').read(); body=src[src.index('def ci(k,F):'):src.index('    w=np.linalg.eigvalsh(H)')]
    g=dict(M.__dict__); exec(body.replace('def ci(k,F):','def _b(k,F):')+'    return H\n',g); H=g['_b'](k,F)
    w=np.linalg.eigvalsh(H); w=w-np.mean(np.diag(H)); return np.round(w,6)
def groups(w):
    out=[]; 
    for v in w:
        if out and abs(v-out[-1][0])<1e-5: out[-1][1]+=1
        else: out.append([v,1])
    return [(round(a,5),c) for a,c in out]
for k in (2,3,4,5):
    print('f%d'%k, groups(spec(k)))
F2,F4,F6=F[2]/225,F[4]/1089,25*F[6]/184041
H3=-25*F2-51*F4-13*F6; F3=-10*F2-33*F4-286*F6; P3=45*F2+33*F4-1287*F6
avg=(11*H3+7*F3+3*P3)/21
print('A3 closed-form f2 rel avg: 3H',round(H3-avg,5),'3F',round(F3-avg,5),'3P',round(P3-avg,5))