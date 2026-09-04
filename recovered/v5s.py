#!/usr/bin/env python3
"""v5s.py -- S96 item 2c: valence singles in V^{N-1} at one row. E2s(c) = f_c sum_v e_v^2 |<P_c|F_v>|^2/(eps_c - e_v), v = core-spectrum roots of l_c with
e_v < E_cut, excluding roots that ARE core-occupied (|<F_v|P_occ>| > 0.5). Uses v5d-Z-SIDE.npz (side occupied + core spectrum). Can-fails: --cf core (5d of the core side must
vanish ~1e-3 rel of eps^2: lever-dead) and --cf root (the core's own 6d root as P_c: exactly 0).  usage: v5s.py Z SIDE nl [--ecut 20] [--cf core|root]"""
import sys,os,json,numpy as np
HERE=os.path.dirname(os.path.abspath(__file__)); Z=int(sys.argv[1]); side=sys.argv[2]; n,l=int(sys.argv[3][0]),'spdf'.index(sys.argv[3][1])
ecut=float(sys.argv[sys.argv.index('--ecut')+1]) if '--ecut' in sys.argv else 20.0
cf=sys.argv[sys.argv.index('--cf')+1] if '--cf' in sys.argv else None
D=np.load(os.path.join(HERE,'v5d-%d-%s.npz'%(Z,side))); r=D['r']; dr=D['dr']
eps={tuple(json.loads(k.replace('(','[').replace(')',']'))):v for k,v in json.loads(str(D['eps'])).items()}
occ=[tuple(o) for o in json.loads(str(D['occ']))]; Q={(a,b):q for a,b,q in occ}
C=np.load(os.path.join(HERE,'v5d-%d-core.npz'%Z)); cocc=[tuple(o) for o in json.loads(str(C['occ']))]
w=D['w%d'%l]; F=D['F%d'%l]; keep=w<ecut; w=w[keep]; F=F[:,keep]
core_l=[k for k in cocc if k[1]==l]; Oc=np.stack([C['P%d%d'%k] for k in core_l],1)
ov=np.abs((Oc*dr[:,None]).T@F).max(0); isocc=ov>0.5
Pc=D['P%d%d'%(n,l)]; ec=eps[(n,l)]; f=Q[(n,l)]/(2*(2*l+1))
if cf=='root':   # the core's own root nearest ec as P_c -> exactly 0 by orthogonality of eigenvectors
    j=np.argmin(abs(w-ec)+1e9*isocc); Pc=F[:,j]; ec=w[j]; f=1.0
s=(F*dr[:,None]).T@Pc; s[isocc]=0.0
num=w*w*s*s; den=ec-w; mask=np.abs(den)>1e-12
E2s=f*np.sum(num[mask]/den[mask])
print("Z=%d side=%s P_c=%d%s eps_c=%.6f f=%.4f  nvirt=%d (core-occ dropped %d)  sum|<c|v>|^2=%.6f  E2s=%.6f Ha  cf=%s"%(Z,side,n,'spdf'[l],ec,f,int((~isocc).sum()),int(isocc.sum()),float(np.sum(s*s)),E2s,cf))
j=np.argsort(-np.abs(num/np.where(mask,den,1)))[:3]; print("  top terms (e_v, <c|v>, contrib):",[(round(float(w[i]),4),round(float(s[i]),4),round(float(f*num[i]/den[i]),6)) for i in j])
json.dump(dict(Z=Z,side=side,nl=sys.argv[3],ecut=ecut,E2s=float(E2s),cf=cf),open(os.path.join(HERE,'v5s-%d-%s-%s%s.json'%(Z,side,sys.argv[3],'-cf'+cf if cf else '')),'w'))