import lam8
L8 = lam8.L8()   # (n,l,k,q,e,f,g,2S)
assert len(L8)==976
idx = {'n':0,'l':1,'k':2,'q':3,'e':4,'f':5,'g':6,'S':7}

print("=== MC-18 §12.6.1: bare product vs conditioned separation ===")
# A side = (n,l,k,2S), B side = (e,f,g); coupled by q<=k and g<=q
# bare product |A|*|B|*|q| claim 2244
from collections import defaultdict
Aall=set(); Ball=set(); Qall=set()
for x in L8:
    Aall.add((x[0],x[1],x[2],x[7]))
    Ball.add((x[4],x[5],x[6]))
    Qall.add(x[3])
print("bare |A|,|B|,|q| =", len(Aall), len(Ball), len(Qall), "-> product", len(Aall)*len(Ball)*len(Qall))
# per-q separation
Aq=defaultdict(set); Bq=defaultdict(set)
for x in L8:
    q=x[3]
    Aq[q].add((x[0],x[1],x[2],x[7]))  # n,l,k,2S
    Bq[q].add((x[4],x[5],x[6]))       # e,f,g
tot=0
print("q | |A(q)| |B(q)| product")
for q in sorted(Qall):
    a=len(Aq[q]); b=len(Bq[q]); p=a*b; tot+=p
    print(f"{q} | {a} {b} {p}")
print("sum of products =", tot, "(claim 976)")

print("\n=== MC-17 §12.1: bipartite / no odd reversal — structural, no numeric to recompute here ===")
print("(the numeric anchor is that the constraint graph is a tree; verified in MC-21 block)")

print("\n=== MC-19 §12.7: A_q(1)=33,33,23,8 ; B_q(1)=5,10,15,17 ===")
# A_q(1) should = number of distinct (n,l,k) with 2S pendant expanded? 
# The fibre A_q counts (n,l,k) with k>=max(q,1) and the 2S chain (k+1 values). 
# But |A(q)| above counted (n,l,k,2S) tuples. Let's check closed-form A_q(1) as stated: 33,33,23,8
# A_q(z)=sum n z^n sum l z^l sum_{k=max(q,1)}^{min(4l+2,3)} z^k (1-z^{min(k,3)+1})/(1-z)
def Aq1(q):
    tot=0
    for n in range(1,4):
        for l in range(0,min(n-1,1)+1):
            for k in range(max(q,1),min(4*l+2,3)+1):
                tot += (min(k,3)+1)  # (1-z^{m+1})/(1-z) at z=1 = m+1 where m=min(k,3)
    return tot
def Bq1(q):
    tot=0
    for e in range(1,4):
        for f in range(0,min(e-1,1)+1):
            tot += (min(q,4*f+2)+1)
    return tot
print("A_q(1):", [Aq1(q) for q in range(4)], "claim 33,33,23,8")
print("B_q(1):", [Bq1(q) for q in range(4)], "claim 5,10,15,17")