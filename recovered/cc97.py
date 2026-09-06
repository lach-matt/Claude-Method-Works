#!/usr/bin/env python3
"""cc97.py -- S97 Item 1: core-core term at a row, slot-rule can-fail (PR1) + two-state resummation of the entrant-own-slot s^2 block (PR2-PR4).
Reads ONLY sealed pack96 jsons (no new spectra). usage: cc97.py Z --delta 0.47 [--canfail] ; --canfail poisons Delta -> 1e9 (resummation must collapse onto PT)."""
import json,sys,math,os
Z=int(sys.argv[1]); Delta=float(sys.argv[sys.argv.index('--delta')+1]); cf='--canfail' in sys.argv
if cf: Delta=1e9
L=lambda s,r: json.load(open('pack96/v5d-%d-%s.e2%s-20.json'%(Z,s,r)))['parts']
core=L('core','w'); ent_w=L('ent','w'); run_w=L('run','w'); ent_x=L('ent',''); run_x=L('run','')
corepairs=[k for k in core]                                        # pairs touching only core shells
ss=[k for k in corepairs if k.split('-')[0]==k.split('-')[1] and k[1]=='0'][-1]   # outer s^2 pair, e.g. 70-70
sp=[k for k in corepairs if k.endswith('-'+ss.split('-')[0]) and k!=ss][-1]     # outer p-s pair, e.g. 61-70
print("row",Z,"outer s2 pair",ss,"reference pair",sp)
r_w=ent_w[sp]/core[sp]-1; r_x=ent_x[sp]/core[sp]-1
print("PR1 (1-f): ent/core-1 = %+.3f -> %s ; exclusion: %+.3f -> %s"%(r_w,'PASS' if abs(r_w)<0.15 else 'FAIL',r_x,'FAIL(expected)' if abs(r_x)>0.30 else 'UNEXPECTED PASS'))
Ept=ent_w[ss]-ent_x[ss]                                            # own-slot block, PT
Eex=-(Delta/2)*(math.sqrt(1+4*abs(Ept)/Delta)-1)
print("PR2 block: E_PT %+.5f  E_exact %+.5f  ratio %.3f"%(Ept,Eex,Eex/Ept))
dcc_pt =sum(run_w[k]-core[k] for k in corepairs)-sum(ent_w[k]-core[k] for k in corepairs)
dcc_ex =dcc_pt-(Eex-Ept)*(-1)   # ent side less negative by (Eex-Ept)>0 -> dcc decreases by that amount
print("PR3 dcc PT %+.5f  resummed %+.5f  change %+.5f  sign %s"%(dcc_pt,dcc_ex,dcc_ex-dcc_pt,'POS' if dcc_ex>0 else 'NEG'))
dm2_ent=0.04121 if Z==89 else float('nan')
print("PR4 dm2 total (entrant-pair filed + core-core resummed) = %+.5f  margin %s"%(dm2_ent+dcc_ex,{89:0.03233}.get(Z)))
if cf: sys.exit(0 if abs(Eex-Ept)<1e-6 else 1)