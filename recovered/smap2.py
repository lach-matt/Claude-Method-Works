import numpy as np, json, eldata as ed
from collections import Counter
rows=json.load(open('/home/claude/ab.json'))
MN={int(k):v for k,v in json.load(open('/home/claude/mn.json')).items()}
CAP=lambda l:2*(2*l+1)
st=np.array([r['st'] for r in rows])
def feats(kind,std=True):
    X=[]
    for r in rows:
        za,zb=r['za'],r['zb']
        mna,mnb=MN[za],MN[zb]
        # Pettifor convention: ordered pair, smaller MN first
        m1,m2=(mna,mnb) if mna<=mnb else (mnb,mna)
        ka,kb=ed.E[za][2],ed.E[zb][2]
        la,lb=ed.E[za][1],ed.E[zb][1]
        # order k,l consistently with the MN ordering
        if mna<=mnb: k1,k2,l1,l2=ka,kb,la,lb
        else:        k1,k2,l1,l2=kb,ka,lb,la
        if kind=='pettifor':        v=[m1,m2]
        elif kind=='pettifor+k':    v=[m1,m2,k1,k2]
        elif kind=='pettifor+l':    v=[m1,m2,l1,l2]
        elif kind=='pettifor+k+l':  v=[m1,m2,k1,k2,l1,l2]
        elif kind=='pettifor+frac': v=[m1,m2,k1/CAP(l1),k2/CAP(l2)]
        elif kind=='k only':        v=[k1,k2]
        elif kind=='lattice only':  v=[l1,l2,k1,k2]
        X.append(v)
    X=np.array(X,float)
    if std: X=(X-X.mean(0))/(X.std(0)+1e-12)
    return X
def loo_nn(X,y):
    n=len(y); correct=0
    D=((X[:,None,:]-X[None,:,:])**2).sum(-1)
    np.fill_diagonal(D,np.inf)
    for i in range(n):
        j=int(np.argmin(D[i]))
        if y[j]==y[i]: correct+=1
    return correct/n
print("="*74)
print("STRUCTURE-MAP SEPARATION: leave-one-out nearest-neighbour accuracy")
print("="*74)
print(f"  {len(rows)} binary AB compounds, {len(set(st))} structure types")
print(f"  majority-class baseline: {max(Counter(st).values())/len(st):.3f}")
print()
print(f"  {'coordinate set':<24}{'dims':>6}{'LOO-NN acc':>12}{'gain':>9}")
print("  "+"-"*52)
base=None
for kind in ['pettifor','k only','lattice only','pettifor+l','pettifor+k','pettifor+frac','pettifor+k+l']:
    X=feats(kind); a=loo_nn(X,st)
    if kind=='pettifor': base=a
    g=f"{a-base:+.3f}" if base is not None and kind!='pettifor' else ''
    print(f"  {kind:<24}{X.shape[1]:>6}{a:>12.3f}{g:>9}")
print()
# unstandardised, to check the scaling choice isn't driving it
print("  unstandardised (raw units):")
for kind in ['pettifor','pettifor+k']:
    X=feats(kind,std=False); print(f"    {kind:<22}{loo_nn(X,st):>12.3f}")