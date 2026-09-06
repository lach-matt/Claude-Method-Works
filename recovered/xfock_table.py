"""xfock_table.py -- s26: TABLE-XFOCK from xfock.jsonl + TABLE-JANAK-SESSION-24.txt; evaluates GA0, PA1-PA4 and the (a)/(b) comparison rule."""
import json
X={d['Z']:d for d in map(json.loads,open('xfock.jsonl'))}
RJ={};RT={}
for line in open('TABLE-JANAK-SESSION-24.txt'):
    p=line.split('|')
    if len(p)==6:
        el=p[0].split()[0]
        try: a,b=p[5].split(); RT[el]=float(a); RJ[el]=float(b)
        except: pass
order=[55,39,57,64,71,21,22,24,26,28,29,68,69,70,66]
out=["Item (2)(a): first-order exact-exchange replacement for the entrant at f=1/2, chain Z orbitals. lsd_x = <n|v_x[n_s]-v_x[f n]>, exact_x = <K_others>, Delta_x = exact-lsd.",
     "resid from TABLE-JANAK-24 (chain - meas). All Ha.","el sh | lsd_x exact_x Delta_x | resid_TS resid_J | resid_TS+Dx resid_J+Dx | G0self vHself"]
rj=[];rjn=[];pos=0;impr=0;dxc=[];dxd=[]
for Z in order:
    d=X[Z]; el=d['el']; dx=d['Delta_x']; a=RJ[el]+dx; b=RT[el]+dx
    out.append(f"{el:2s} {d['sh']} | {d['lsd_x']:+.4f} {d['exact_x']:+.4f} {dx:+.4f} | {RT[el]:+.4f} {RJ[el]:+.4f} | {b:+.4f} {a:+.4f} | {d['G0self']:.5f} {d['vHself']:.5f}")
    if Z!=55:
        rj.append(RJ[el]); rjn.append(a); impr+=abs(a)<abs(RJ[el])
        if d['sh'] in ('3d','4f'): pos+=a>0; dxc.append(dx)
        if Z in (39,57,64,71): dxd.append(dx)
mc=sum(dxc)/len(dxc); md=sum(dxd)/len(dxd)
out+=[f"GA0 max|G0self-vHself| {max(abs(X[Z]['G0self']-X[Z]['vHself']) for Z in order):.6f} -> {'HELD' if max(abs(X[Z]['G0self']-X[Z]['vHself']) for Z in order)<=1e-5 else 'FAILED'}",
 f"PA1 Delta_x>0 all 15: {all(X[Z]['Delta_x']>0 for Z in order)} -> {'HELD' if all(X[Z]['Delta_x']>0 for Z in order) else 'FAILED'}",
 f"PA2 |resid_J+Dx|<|resid_J| on {impr}/14 -> {'HELD' if impr>=12 else 'FAILED'}",
 f"PA3 resid_J+Dx>0 on {pos}/10 3d/4f -> {'HELD' if pos>=8 else 'FAILED'}",
 f"PA4 mean Dx 3d/4f {mc:.4f} vs 4d/5d {md:.4f} ratio {mc/md:.2f} -> {'HELD' if mc>=2*md else 'FAILED'}",
 f"spread resid_J {max(rj)-min(rj):.4f} -> resid_J+Dx {max(rjn)-min(rjn):.4f}; mean|resid_J| {sum(map(abs,rj))/14:.4f} -> {sum(map(abs,rjn))/14:.4f}",
 f"COMPARISON RULE: (a) beats (b) iff PA2 and spread shrinks -> {'(a)' if impr>=12 and (max(rjn)-min(rjn))<(max(rj)-min(rj)) else '(b)'}"]
open('TABLE-XFOCK-SESSION-26.txt','w').write("\n".join(out)+"\n"); print("\n".join(out))