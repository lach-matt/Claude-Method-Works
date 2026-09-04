import sys,json,os,warnings; warnings.filterwarnings("ignore")
import ground as G
from hfs import L
from hfs_pol import scf_pol
from step3 import steps
done={}
if os.path.exists("testE.jsonl"):
    for l in open("testE.jsonl"): r=json.loads(l); done[r["Z"]]=r
if sys.argv[1].startswith('r'): zlo,zhi=map(int,sys.argv[1][1:].split('-')); want=set(range(zlo,zhi+1))
else: want=set(int(a) for a in sys.argv[1:])
for Z,pr,obs,cand in steps():
    if Z in done or Z not in want: continue
    base=list(G.expand(Z-1)); E={}
    try:
        for n,l in cand:
            occ=[list(t) for t in base]; found=False
            for t in occ:
                if t[0]==n and t[1]==l: t[2]+=0.5; found=True
            if not found: occ.append([n,l,0.5])
            probe,Es,h=scf_pol(Z,1,occ=[tuple(t) for t in occ])
            # channel of the half-electron: down if core already had >=2l+1 in this shell, else up
            k0=sum(t[2] for t in base if t[0]==n and t[1]==l); s="d" if k0>=2*l+1 else "u"
            E[(n,l)]=(Es[(n,l,s)],s,len(h))
        eB=min(E,key=lambda c:E[c][0])
        r=dict(Z=Z,el=G.GROUND[Z][0],obs=f"{obs[0]}{L[obs[1]]}",B=f"{eB[0]}{L[eB[1]]}",hitB=eB==obs,
               EB={f"{n}{L[l]}{s}":round(v,5) for (n,l),(v,s,it) in E.items()})
    except Exception as ex:
        r=dict(Z=Z,el=G.GROUND[Z][0],error=str(ex),hitB=False)
    open("testE.jsonl","a").write(json.dumps(r)+"\n")
    print(Z,r["el"],r.get("obs"),r.get("B"),"✓" if r["hitB"] else "✗",r.get("EB",r.get("error")),flush=True)