"""frozen_split_table.py -- s26: TABLE-FROZEN-SPLIT from frozen_split.jsonl + frozen_scan.jsonl (Z) + frozen_scan_corrnone.jsonl (none). Evaluates P26.0-P26.6."""
import json, numpy as np
from scipy.integrate import trapezoid
def mask_fr(path,Z):
    d=[x for x in map(json.loads,open(path)) if x['Z']==Z]; f=np.array([x['f'] for x in d]); E=np.array([x['E_fr'] for x in d]); o=np.argsort(f); f=f[o];E=E[o]
    x=f**(1/3); xs=np.linspace(0,1,20001); Ei=np.interp(xs,x,E); I=float(trapezoid(Ei,xs**3)); return I-float(E[list(f).index(0.5)])
S=[json.loads(l) for l in open('frozen_split.jsonl')]
order=[55,39,57,64,71,21,22,24,26,28,29,68,69,70,66]
out=["Frozen-mask split, s26. mask_fr from the s25 frozen scan (7-pt grid, f^(1/3) interp). M_T = midpoint defect of term T on the frozen reference",
     "densities, grid convention (fine-grid in FINDING). law = 0.0583*E_x[n_ent]. resp = mask_fr - (xtot+ctot+xsic+csic). All entries in Ha; r_ = ratio to law.",
     "chain | el sh | E_x[n_ent] rmean | law | mask_fr | M_xtot M_ctot M_xsic M_csic M_resp | r_xtot r_ctot r_xsic r_csic r_resp | r_total"]
R={}
for chain,path in (("Z","frozen_scan.jsonl"),("none","frozen_scan_corrnone.jsonl")):
    for Z in order:
        d=[x for x in S if x['Z']==Z and x['corr']==chain][0]; m=mask_fr(path,Z); law=d['law']
        parts=[d['M_xtot_grid'],d['M_ctot_grid'],d['M_xsic_grid'],d['M_csic_grid']]; resp=m-sum(parts)
        rs=[p/law for p in parts]+[resp/law]
        R[(chain,Z)]=dict(el=d['el'],law=law,mask=m,parts=parts,resp=resp,rs=rs,rtot=m/law,rmean=d['rmean'],Ex=d['Ex_ent'],
                          xsic_fine=d['M_xsic_fine'],xsic_grid=d['M_xsic_grid'])
        out.append(f"{chain:4s} | {d['el']:2s} {d['sh']} | {d['Ex_ent']:+.4f} {d['rmean']:.3f} | {law:+.5f} | {m:+.5f} | "
                   +" ".join(f"{p:+.5f}" for p in parts)+f" {resp:+.5f} | "+" ".join(f"{x:+.3f}" for x in rs)+f" | {m/law:.3f}")
non_cs=[Z for Z in order if Z!=55]
def rng(v): return f"[{min(v):+.3f},{max(v):+.3f}] spread {max(v)-min(v):.3f}"
out.append("")
# P26.0
g0=[abs(R[('Z',Z)]['xsic_fine']-R[('Z',Z)]['law']) for Z in order]+[abs(R[('none',Z)]['xsic_fine']-R[('none',Z)]['law']) for Z in order]
g1=[abs(R[(c,Z)]['xsic_grid']-R[(c,Z)]['xsic_fine']) for c in ('Z','none') for Z in order]
out.append(f"P26.0 fine M_xsic==law: max|diff| {max(g0):.6f} -> {'HELD' if max(g0)<=1e-4 else 'FAILED'}; grid-vs-fine max {max(g1):.6f} -> {'HELD' if max(g1)<=3e-4 else 'FAILED'}")
# P26.1
rz=[R[('Z',Z)]['rs'][4] for Z in non_cs]; rn=[R[('none',Z)]['rs'][4] for Z in non_cs]
allneg=all(R[(c,Z)]['resp']<0 for c in ('Z','none') for Z in order)
out.append(f"P26.1 M_resp<0 all 30: {allneg}; r_resp Z {rng(rz)}; none {rng(rn)} -> {'HELD' if allneg and all(0.02<=x<=0.12 for x in rz+rn) else 'FAILED'}")
# P26.2
x2=[R[('none',Z)]['rs'][0]+R[('none',Z)]['rs'][4] for Z in non_cs]
out.append(f"P26.2 x-only (r_xtot+r_resp) {rng(x2)}; Sc total {R[('none',21)]['rtot']:.3f} Yb total {R[('none',70)]['rtot']:.3f} (PF8 1.09/1.07) -> {'HELD' if all(0.03<=x<=0.15 for x in x2) and abs(R[('none',21)]['rtot']-1.09)<=0.011 and abs(R[('none',70)]['rtot']-1.07)<=0.011 else 'FAILED'}")
# P26.3
c3=[R[('Z',Z)]['rs'][1]+R[('Z',Z)]['rs'][3] for Z in non_cs]; c3n=[R[('Z',Z)]['parts'][1]+R[('Z',Z)]['parts'][3] for Z in non_cs]
out.append(f"P26.3 chain Z corr part (r_ctot+r_csic) {rng(c3)}; all negative in Ha: {all(v<0 for v in c3n)} -> {'HELD' if all(0.03<=x<=0.12 for x in c3) and all(v<0 for v in c3n) else 'FAILED'}")
# P26.4
p4=[abs(R[('Z',Z)]['resp']/R[('Z',Z)]['mask']) for Z in non_cs]
out.append(f"P26.4 |M_resp/mask_fr| chain Z {rng(p4)} -> {'HELD' if max(p4)<=0.15 else 'FAILED'}")
# P26.5
sp=max(c3)-min(c3); cr=[ (R[('Z',Z)]['parts'][1]+R[('Z',Z)]['parts'][3])*R[('Z',Z)]['rmean'] for Z in non_cs]
cv_ex=np.std(c3)/abs(np.mean(c3)); cv_rm=np.std(cr)/abs(np.mean(cr))
out.append(f"P26.5 corr-part ratio spread {sp:.3f} (<=0.05?); CV vs |E_x| {cv_ex:.3f}, CV of M_c*rmean {cv_rm:.3f} -> {'HELD' if sp<=0.05 and cv_rm>cv_ex else 'FAILED'}")
# P26.6
row=[21,22,24,26,28,29]; tot=[R[('Z',Z)]['rtot'] for Z in row]; resp=[R[('Z',Z)]['rs'][4] for Z in row]; xt=[R[('Z',Z)]['rs'][0] for Z in row]; co=[R[('Z',Z)]['rs'][1]+R[('Z',Z)]['rs'][3] for Z in row]
out.append(f"P26.6 3d Sc->Cu: r_total {tot[0]:.3f}->{tot[-1]:.3f} (d {tot[-1]-tot[0]:+.3f}); r_resp d {resp[-1]-resp[0]:+.3f}; r_xtot d {xt[-1]-xt[0]:+.3f}; corr d {co[-1]-co[0]:+.3f} -> {'HELD' if abs(resp[-1]-resp[0])>abs(xt[-1]-xt[0]) and abs(resp[-1]-resp[0])>abs(co[-1]-co[0]) else 'FAILED'}")
open('TABLE-FROZEN-SPLIT-SESSION-26.txt','w').write("\n".join(out)+"\n"); print("\n".join(out))
