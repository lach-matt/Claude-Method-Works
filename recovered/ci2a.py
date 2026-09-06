"""ci2a.py -- s71, route C-b, THE ANGULAR HALF ONLY.
Scores PREDICTION-CI2x2 clauses CI-1, CI-3, CI-4, CI-5 -- the SELECTION RULE.
It does NOT score CI-6 or CI-7, which need radial integrals and the diagonaliser.
Object: for a one-electron replacement a->b with spectator shell k, the off-diagonal
element <A|H|B> is carried by exchange R^kappa(a k; k b), whose angular factor is the
product 3j(l_a,kappa,l_k;000)*3j(l_k,kappa,l_b;000). Zero/nonzero only; no magnitude.
CAN-FAIL: the new 3j must reproduce the SEALED t7b_hf._c3j0sq on the diagonal, and must
return zero on cases known forbidden and nonzero on cases known allowed.
No constant. Nothing empirical. ref_cfg is the CHAIN's own reference (mode=chain).
"""
import json, math, sys
from t7b_hf import _c3j0sq

def c3j0(a,k,b):
    """3j(a k b; 0 0 0), exact closed form. Zero if a+k+b odd or triangle violated."""
    J=a+k+b
    if J%2 or k<abs(a-b) or k>a+b: return 0.0
    g=J//2; f=math.factorial
    return ((-1)**g)*math.sqrt(f(J-2*a)*f(J-2*k)*f(J-2*b)/f(J+1))*f(g)/(f(g-a)*f(g-k)*f(g-b))

# ---- CAN-FAIL GATE, BEFORE ANY ROW ----
bad=[]
for a in range(0,5):
    for b in range(0,5):
        for k in range(0,9):
            if abs(c3j0(a,k,b)**2 - _c3j0sq(a,k,b)) > 1e-12: bad.append((a,k,b))
assert not bad, f"CAN-FAIL A: new 3j disagrees with sealed _c3j0sq at {bad[:5]}"
assert c3j0(0,2,2)!=0.0, "CAN-FAIL B1: (0,2,2) must be NONZERO"
assert c3j0(0,1,2)==0.0, "CAN-FAIL B2: (0,1,2) must be ZERO"
assert c3j0(2,2,2)!=0.0, "CAN-FAIL B3: (2,2,2) must be NONZERO"
print("CAN-FAIL: PASS -- 3j reproduces the sealed helper on 225 diagonal cases,")
print("          and returns nonzero AND zero on the two directions demanded.")

def onebody(la,lb): return la==lb          # <a|h|b>, h spherically symmetric
def direct(la,lb):                          # <ak|g|bk>: spectator absorbs kappa=0 only
    return any(c3j0(la,k,lb)!=0.0 and c3j0(lk,0,lk)!=0.0 and k==0
               for k in range(0,9) for lk in range(0,4))
def exch(la,lb,lk):                         # <ak|g|kb>: R^kappa(a k; k b)
    return [k for k in range(0,9) if c3j0(la,k,lk)!=0.0 and c3j0(lk,k,lb)!=0.0]

LMAP={'s':0,'p':1,'d':2,'f':3}
def parse(cfg):
    """ref_cfg like '1s2 2s2 ...' -> list of (l, q, cap) for shells that are OPEN."""
    out=[]
    for t in cfg.split():
        l=LMAP[t[1]]; q=int(t[2:]); cap=2*(2*l+1)
        out.append((t,l,q,cap))
    return out

rows={r['Z']:r for r in (json.loads(x) for x in open('nlchain.jsonl'))}
CASES=[(24,'Cr','4s','3d','ALLOWED  s<->d, promotion anomaly'),
       (29,'Cu','4s','3d','ALLOWED  s<->d, promotion anomaly'),
       (58,'Ce','5d','4f','FORBIDDEN d<->f, tie-break row'),
       (90,'Th','6d','5f','FORBIDDEN d<->f, tie-break row'),
       (21,'Sc','4s','3d','FIRST-ENTRY, 3d opens'),
       (57,'La','6s','5d','FIRST-ENTRY, 5d opens'),
       (89,'Ac','7s','6d','FIRST-ENTRY, 6d opens')]
print(f"\n{'Z':>4} {'el':<3} {'a->b':<9} {'l_a+l_b':>7} {'open spectators':<22} {'kappa':<10} V")
print("-"*78)
res={}
for Z,el,a,b,note in CASES:
    la,lb=LMAP[a[1]],LMAP[b[1]]
    cfg=rows[Z]['ref_cfg']
    opens=[(t,l,q,cap) for t,l,q,cap in parse(cfg) if 0<q<cap]
    ks=set(); carriers=[]
    for t,l,q,cap in opens:
        kk=exch(la,lb,l)
        if kk: ks|=set(kk); carriers.append(t)
    V = 'NONZERO' if ks else 'ZERO'
    res[Z]=dict(el=el,a=a,b=b,parity=(la+lb)%2,V=V,kappa=sorted(ks),
                opens=[t for t,_,_,_ in opens],carriers=carriers,note=note,ref_cfg=cfg,
                onebody=onebody(la,lb),direct=direct(la,lb))
    print(f"{Z:>4} {el:<3} {a}->{b:<5} {la+lb:>7} {','.join(t for t,_,_,_ in opens) or '(none open)':<22} "
          f"{str(sorted(ks)) if ks else '-':<10} {V}")
json.dump(res,open('ci2a.json','w'),indent=1)
print("\nonebody nonzero anywhere:", any(v['onebody'] for v in res.values()))
print("direct  nonzero anywhere:", any(v['direct']  for v in res.values()))