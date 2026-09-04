#!/usr/bin/env python3
"""t7c_6s.py -- session 20 (i): is the SR kernel's s-contraction right?  (a) hydrogenic ns at Z=57 vs exact Dirac ns1/2 (derivable, exact);
(b) SR-pol TS 6s removal at Cs (6s1->1S0) and Ba (6s2->6s 2S1/2), nr and SR; recalled IPs (Cs 0.14310, Ba 0.19153 Ha) for COMPARISON ONLY, not entered.
Pi1: |kernel-Dirac| < 0.002 for 5s,6s at Z=57.  Pi2: SR 6s TS within 5 % of the recalled IP; SR shift on 6s negative, 0.005-0.010."""
import sys, json, numpy as np, warnings; warnings.filterwarnings("ignore")
from t7c_kernel import numerov_wf_sr, C0
from t5_scf import ground_occ, minus
from t7c_pol import scf_pol_sr
if sys.argv[1]=='hyd':
    Z=57; V=lambda r:-Z/np.asarray(r,float); g=np.sqrt(1-(Z/C0)**2)
    for n in (5,6):
        ed=C0**2*((1+(Z/C0)**2/(n-1+g)**2)**-0.5-1); es=numerov_wf_sr(V,0,n,1.0,Z)[3]; en=numerov_wf_sr(V,0,n,1.0,Z,c=1e6)[3]
        print(dict(Z=Z,n=n,nonrel=round(en,4),sr=round(es,4),dirac_s12=round(ed,4),d=round(es-ed,4),sr_shift=round(es-en,4)))
else:
    IP={55:0.14310,56:0.19153}
    for Z in map(int,sys.argv[1:]):
        occ=minus(ground_occ(Z),6,0,0.5); s="u"
        _,Es,h1=scf_pol_sr(Z,1,occ=occ,c=1e6); _,Er,h2=scf_pol_sr(Z,1,occ=occ,c=C0)
        e0,e1=float(Es[(6,0,s)]),float(Er[(6,0,s)])
        row=dict(Z=Z,sh='6s',nr=round(e0,4),sr=round(e1,4),sr_shift=round(e1-e0,4),ip_recalled=-IP[Z],dev_sr_pct=round(100*(e1+IP[Z])/IP[Z],1),it=[len(h1),len(h2)])
        open('t7c_6s.jsonl','a').write(json.dumps(row)+'\n'); print(row,flush=True)