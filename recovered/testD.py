import sys,json,os,warnings; warnings.filterwarnings("ignore")
import ground as G
from hfs import L
from hfs_pol import scf_pol
from step3 import steps
done={}
if os.path.exists("testD.jsonl"):
    for l in open("testD.jsonl"): r=json.loads(l); done[r["Z"]]=r
want=set(int(a) for a in sys.argv[1:]) if len(sys.argv)>1 and not sys.argv[1].startswith('r') else None
if sys.argv[1].startswith('r'): zlo,zhi=map(int,sys.argv[1][1:].split('-')); want=set(range(zlo,zhi+1))
for Z,pr,obs,cand in steps():
    if Z in done or Z not in want: continue
    try:
        probe,Es,h=scf_pol(Z,1); E={}; S={}
        for n,l in cand: e,s=probe(n,l); E[(n,l)]=e; S[(n,l)]=s
        eB=min(E,key=E.get)
        r=dict(Z=Z,el=G.GROUND[Z][0],obs=f"{obs[0]}{L[obs[1]]}",B=f"{eB[0]}{L[eB[1]]}",hitB=eB==obs,it=len(h),
               EB={f"{n}{L[l]}{S[(n,l)]}":round(v,5) for (n,l),v in E.items()})
    except Exception as ex:
        r=dict(Z=Z,el=G.GROUND[Z][0],error=str(ex),hitB=False)
    open("testD.jsonl","a").write(json.dumps(r)+"\n")
    print(Z,r["el"],r.get("obs"),r.get("B"),"✓" if r["hitB"] else "✗",r.get("EB",r.get("error")),flush=True)