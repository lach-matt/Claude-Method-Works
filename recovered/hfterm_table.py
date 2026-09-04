"""hfterm_table.py -- s27: TABLE-HFTERM from hfterm.jsonl + TABLE-JANAK-24 (meas RECALLED = chain eps(1/2)+so/hund-resid_TS) + chain SO-only column.
SO_chain: 3d from t7c_3dhund.jsonl (so_n - so_i); 4f = soh(TABLE-JANAK-24) - (stab_n - stab_i) of t7c_mult.jsonl. Hund part NOT added (term-resolved here)."""
import json
H={d['Z']:d for d in map(json.loads,open('hfterm.jsonl'))}
H26={d['Z']:d for d in map(json.loads,open('hfdscf.jsonl'))}
J={}
for line in open('TABLE-JANAK-SESSION-24.txt'):
    p=line.split('|')
    if len(p)==6:
        try:
            el=p[0].split()[0]; e=p[1].split(); eps5=float(e[1]); soh=float(p[4]); rT,rJ=map(float,p[5].split())
            J[el]=dict(soh=soh,rT=rT,rJ=rJ,meas=eps5+soh-rT)
        except: pass
SO={}
for d in map(json.loads,open('t7c_3dhund.jsonl')): SO[d['Z']]=d['so_n']-d['so_i']
for d in map(json.loads,open('t7c_mult.jsonl')):
    if d['Z'] in (66,68,69,70): SO[d['Z']]=J[d['el']]['soh']-(d['stab_n']-d['stab_i'])
order=[21,22,24,26,28,29,66,68,69,70]
out=["Term-resolved (Hund ground term, highest-weight determinant, first order in relaxation) exact-exchange DSCF + s26 chain-Z correlation. s27.",
     "obj_term = -D_term + Delta_c; resid = obj + SO_chain - meas. resid_HFc26 = s26 avg-of-config result (with the chain's full so/hund column). All Ha.",
     "el sh | D_avg dE_neu dE_ion D_term | Delta_c | obj_term | SO_chain | meas | resid_HFterm | resid_HFc26 resid_J"]
wins=0; better26=[]; signs={}
for Z in order:
    h=H[Z]; j=J[h['el']]; so=SO[Z]; res=h['obj_term']+so-j['meas']
    r26=H26[Z]['obj']+j['soh']-j['meas']
    out.append(f"{h['el']:2s} {h['sh']} | {h['D_avg']:+.4f} {h['dE_term_neu']:+.4f} {h['dE_term_ion']:+.4f} {h['D_term']:+.4f} | {h['Delta_c']:+.4f} | {h['obj_term']:+.4f} | {so:+.4f} | {j['meas']:+.4f} | {res:+.4f} | {r26:+.4f} {j['rJ']:+.4f}")
    if abs(res)<abs(j['rJ']): wins+=1
    better26.append((h['el'],abs(res)<abs(r26)))
    signs[h['el']]=h['D_term']-h['D_avg']
cr,yb=dict(better26)['Cr'],dict(better26)['Yb']
out+=[f"PT1 |resid_HFterm|<|resid_J| on {wins}/10 -> {'HELD' if wins>=7 else 'FAILED'}",
      f"PT2 Cr better than s26 avg: {cr}; Yb better: {yb} -> {'HELD' if cr and yb else 'FAILED'}",
      f"PT3 Cr |D_term-D_avg| {abs(signs['Cr']):.4f} in [0.05,0.12] -> {'HELD' if 0.05<=abs(signs['Cr'])<=0.12 else 'FAILED'}",
      f"PT4 Sc D_term-D_avg {signs['Sc']:+.5f} -> {'HELD' if abs(signs['Sc'])<1e-5 else 'FAILED'}",
      f"PT5 sign of (D_term-D_avg) [+ deepens removal energy]: " + " ".join(f"{k}{'+' if v>1e-6 else ('-' if v<-1e-6 else '0')}" for k,v in signs.items())
      + "  predicted: Fe- Ni- Cr+ Cu+ Tm+ Yb+"]
open('TABLE-HFTERM-SESSION-27.txt','w').write("\n".join(out)+"\n"); print("\n".join(out))
