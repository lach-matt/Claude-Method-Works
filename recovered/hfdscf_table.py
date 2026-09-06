"""hfdscf_table.py -- s26: TABLE-HFCORR from hfdscf.jsonl + TABLE-JANAK-24 (meas RECALLED = chain eps(1/2)+so/hund - resid_TS). Evaluates PB1-PB5."""
import json
H={d['Z']:d for d in map(json.loads,open('hfdscf.jsonl'))}
J={}
for line in open('TABLE-JANAK-SESSION-24.txt'):
    p=line.split('|')
    if len(p)==6:
        try:
            el=p[0].split()[0]; e=p[1].split(); eps5=float(e[1]); DEJ=float(p[2]); soh=float(p[4]); rT,rJ=map(float,p[5].split())
            J[el]=dict(eps5=eps5,DEJ=DEJ,soh=soh,rT=rT,rJ=rJ,meas=eps5+soh-rT)
        except: pass
order=[55,39,57,64,71,21,22,24,26,28,29,68,69,70,66]
out=["(a') exact-exchange DSCF (HFSR 'hf', c=C0, avg-of-config, integer occ) + first-order chain-Z correlation (v_gbz+PZ SIC, neutral HF orbitals, entrant weight 1/2).",
     "obj = -D_HF + Delta_c. meas RECALLED from TABLE-JANAK-24. so/hund column of the chain added to obj for the resid (same as chain). All Ha.",
     "el sh | -D_HF eps_koop relax | Delta_c | obj | so/hund | meas | resid_HFc | resid_TS resid_J (chain)"]
r=[];rj=[];sd=[]
for Z in order:
    h=H[Z]; j=J[h['el']]; obj=h['obj']+j['soh']; res=obj-j['meas']
    out.append(f"{h['el']:2s} {h['sh']} | {-h['D_HF']:+.4f} {h['eps_koop']:+.4f} {h['eps_koop']+h['D_HF']:+.4f} | {h['Delta_c']:+.4f} | {h['obj']:+.4f} | {j['soh']:+.4f} | {j['meas']:+.4f} | {res:+.4f} | {j['rT']:+.4f} {j['rJ']:+.4f}")
    if Z!=55: r.append(res); rj.append(j['rJ'])
    if Z in (39,57,64,71,21): sd.append(res)
sc=H[21];la=H[57]
out+=[f"PB1 -D_HF Sc {-sc['D_HF']:+.4f} in [-0.31,-0.21] -> {'HELD' if -0.31<=-sc['D_HF']<=-0.21 else 'FAILED'}",
 f"PB2 Delta_c<0 all: {all(H[Z]['Delta_c']<0 for Z in order)}; |Dc| Sc..Lu range [{min(abs(H[Z]['Delta_c']) for Z in (39,57,64,71,21)):.4f},{max(abs(H[Z]['Delta_c']) for Z in (39,57,64,71,21)):.4f}] -> {'HELD' if all(H[Z]['Delta_c']<0 for Z in order) and all(0.010<=abs(H[Z]['Delta_c'])<=0.035 for Z in (39,57,64,71,21)) else 'FAILED'}",
 f"PB3 |resid_HFc| Sc {abs(sc['obj']+J['Sc']['soh']-J['Sc']['meas']):.4f} La {abs(la['obj']+J['La']['soh']-J['La']['meas']):.4f} <=0.015 -> {'HELD' if abs(sc['obj']+J['Sc']['soh']-J['Sc']['meas'])<=0.015 and abs(la['obj']+J['La']['soh']-J['La']['meas'])<=0.015 else 'FAILED'}",
 f"PB4 mean|resid| s/d rows (Y La Gd Lu Sc): HFc {sum(map(abs,sd))/5:.4f} vs J {sum(abs(J[H[Z]['el']]['rJ']) for Z in (39,57,64,71,21))/5:.4f} -> {'HELD' if sum(map(abs,sd))/5<=0.012 else 'FAILED'}",
 f"PB5 (HFS vs HF): banked hfs TS Sc -0.2686 vs HF Koopmans {sc['eps_koop']:+.4f} / -D_HF {-sc['D_HF']:+.4f}: different objects, stated.",
 f"14 non-Cs rows: mean|resid_HFc| {sum(map(abs,r))/14:.4f} (resid_J {sum(map(abs,rj))/14:.4f}); spread {max(r)-min(r):.4f} (resid_J {max(rj)-min(rj):.4f}); |resid_HFc|<|resid_J| on {sum(abs(a)<abs(b) for a,b in zip(r,rj))}/14"]
open('TABLE-HFCORR-SESSION-26.txt','w').write("\n".join(out)+"\n"); print("\n".join(out))