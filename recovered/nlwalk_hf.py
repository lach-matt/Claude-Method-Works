"""nlwalk_hf.py -- s37 Stage 2 of the n+l walk: SR HF (hfc2, no corr) DSCF removals on the frontier of the neutral. lwalk_hf.py generalised:
entrant g derived from ground.expand; removals = g and every OCCUPIED frontier partner (channels rule of nlwalk.py: (N,0)(N,1)(N-1,2)(N-2,3)).
D_rel(x) = E_neu - E(neu minus x) (negative = bound). Shallowest removal = walk's first-ionised subshell (comparison column only).
usage: python3 nlwalk_hf.py Z ...  appends nlwalk_hf.jsonl (key Z,tag). No constant; no measured input."""
import sys,os,json,time
os.environ.setdefault("SIC_NOCLAMP","1"); os.environ.setdefault("SUBCELL","1")
import hfc2 as H; from t7c_kernel import C0; from t5_scf import ground_occ,minus; import ground as G
H.CORR=False
def entrant(Z):
    a={(n,l):k for n,l,k in G.expand(Z)}; b={(n,l):k for n,l,k in G.expand(Z-1)}
    up=[nl for nl in a if a[nl]-b.get(nl,0)>1e-9]; assert len(up)==1,(Z,up); return up[0]
def channels(Z):
    N=max(n for n,l,k in G.expand(Z)); ch=[(N,0),(N,1),(N-1,2)]
    if N>=6: ch.append((N-2,3))
    return ch
def tagof(c): return f"{c[0]}{'spdf'[c[1]]}"
OUT='nlwalk_hf.jsonl'; done={(d['Z'],d['tag']) for d in map(json.loads,open(OUT))} if os.path.exists(OUT) else set()
MAXIT=int(os.environ.get("HFMAXIT","100"))
for Z in map(int,sys.argv[1:]):
    g=entrant(Z); occ0=ground_occ(Z); od={(n,l):k for n,l,k in occ0}
    rem=[g]+[c for c in channels(Z) if c!=g and c[1]!=1 and od.get(c,0)>1e-9]
    todo=[c for c in rem if (Z,tagof(c)) not in done]
    for c in rem:
        if (Z,tagof(c)) in done: print("SKIP",Z,tagof(c))
    if not todo: continue
    t0=time.time(); h0=H.HFC(Z,occ0,c=C0); E0,_,it0,eps0=h0.run2()
    for c in todo:
        t1=time.time(); hs=H.HFC(Z,minus(occ0,c[0],c[1],1.0),c=C0); Es,_,its,_=hs.run2()
        o=dict(Z=Z,tag=tagof(c),ent=tagof(g),kind='ent' if c==g else 'swap',D_rel=round(E0-Es,5),eps=round(float(eps0[c]),5),E_neu=round(E0,5),
               it=[it0,its],conv=bool(its<MAXIT),sec=int(time.time()-t1))
        open(OUT,'a').write(json.dumps(o)+'\n'); print(o,flush=True)
