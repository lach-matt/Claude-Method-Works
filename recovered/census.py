import json
D=json.load(open("covers8.json"))
covers=[[tuple(c) for c in cv] for cv in D["covers"]]
N=len(covers)
def has(cv,pred): return any(pred(c) for c in cv)
tests={
 "s->s (l=0,f=0)":      lambda c: c[1]==0 and c[5]==0,
 "s->p (l=0,f=1)":      lambda c: c[1]==0 and c[5]==1,
 "p->s (l=1,f=0)":      lambda c: c[1]==1 and c[5]==0,
 "p->p (l=1,f=1)":      lambda c: c[1]==1 and c[5]==1,
 "null q=0":            lambda c: c[3]==0,
 "full q=k":            lambda c: c[3]==c[2],
 "unit (3,0,1,1,*,0,1,1)": lambda c: (c[0],c[1],c[2],c[3],c[5],c[6],c[7])==(3,0,1,1,0,1,1),
 "corner3 (2,1,3,3,2,1,3,0)": lambda c: c==(2,1,3,3,2,1,3,0),
 "corner4 11001100":    lambda c: c==(3,1,1,0,3,1,0,0),
}
print(f"census over ALL {N} exact minimum covers:")
for name,p in tests.items():
    k=sum(1 for cv in covers if has(cv,p))
    print(f"  {name:32s} {k:6d}/{N}  {'UNIVERSAL' if k==N else ''}")