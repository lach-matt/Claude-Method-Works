#!/usr/bin/env python3
"""t7c_4d.py -- session 20: predictive test of FINDING-T7C-SHELL. Y I 4d1 5s2 -> Y II 5s2 1S0, SR-pol TS on 4d (nr and SR).
Recalled IP Y 0.2285 Ha for COMPARISON ONLY (not entered). Prediction: shallow by 0.01-0.03; |SR shift| < 0.01."""
import sys, json, warnings; warnings.filterwarnings("ignore")
from t7c_kernel import C0
from t5_scf import ground_occ, minus
from t7c_pol import scf_pol_sr
IP={39:0.2285}
for Z in map(int,sys.argv[1:]):
    g=ground_occ(Z); print('ground',g[-3:])
    occ=minus(g,4,2,0.5); s="u"
    _,En,h1=scf_pol_sr(Z,1,occ=occ,c=1e6); _,Er,h2=scf_pol_sr(Z,1,occ=occ,c=C0)
    e0,e1=float(En[(4,2,s)]),float(Er[(4,2,s)])
    row=dict(Z=Z,sh='4d',nr=round(e0,4),sr=round(e1,4),sr_shift=round(e1-e0,4),ip_recalled=-IP[Z],sr_minus_meas=round(e1+IP[Z],4),dev_sr_pct=round(100*(e1+IP[Z])/IP[Z],1),it=[len(h1),len(h2)])
    open('t7c_4d.jsonl','a').write(json.dumps(row)+'\n'); print(row,flush=True)