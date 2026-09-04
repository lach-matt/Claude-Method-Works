import eldata as ed
from math import log10
CAP={0:2,1:6,2:10,3:14,4:18}
cols=[(n,l) for n in range(1,8) for l in range(0,min(n,5))]
CI={c:i for i,c in enumerate(cols)}
AUF=[(1,0),(2,0),(2,1),(3,0),(3,1),(4,0),(3,2),(4,1),(5,0),(4,2),(5,1),(6,0),
     (4,3),(5,2),(6,1),(7,0),(5,3),(6,2),(7,1)]
def gvec(Z):
    v=[0]*len(cols); rem=Z
    for c in AUF:
        t=min(rem,CAP[c[1]]); v[CI[c]]=t; rem-=t
        if rem<=0: break
    return tuple(v)
G=[gvec(z) for z in range(1,119)]
def vleq(a,b): return all(x<=y for x,y in zip(a,b))

print("="*78)
print("READING B1 CONTINUED: WHAT THE CHAIN STRUCTURE GIVES")
print("="*78)
print("""  In Λ the periodic system is an order IDEAL (a down-set).
  In V the periodic system is a CHAIN (totally ordered).
  These are different and complementary descriptions.""")
print()
# excited states as points of V ABOVE the chain
print("  An excited configuration of element Z is a vector with the same")
print("  total Σv = Z but a different distribution. Where does it sit?")
def excited_of(Z, promote_from, promote_to):
    v=list(gvec(Z))
    i,j=CI[promote_from],CI[promote_to]
    if v[i]==0 or v[j]>=CAP[promote_to[1]]: return None
    v[i]-=1; v[j]+=1
    return tuple(v)
ex=excited_of(11,(3,0),(3,1))     # Na 3s->3p
print(f"\n  Na ground : Σ={sum(gvec(11))}")
print(f"  Na* 3s→3p : Σ={sum(ex)}")
print(f"  is Na* ≥ Na in V?  {vleq(gvec(11),ex)}")
print(f"  is Na* ≤ Na in V?  {vleq(ex,gvec(11))}")
print(f"  → INCOMPARABLE. Excitation moves sideways in V, not up.")
print()
# where does Na* sit relative to the chain?
above=[z for z in range(1,119) if vleq(gvec(z),ex)]
below=[z for z in range(1,119) if vleq(ex,gvec(z))]
print(f"  ground states below Na*: Z ≤ {max(above) if above else '—'}")
print(f"  ground states above Na*: Z ≥ {min(below) if below else '—'}")
print(f"  → Na* is comparable to ground states Z≤{max(above)} and Z≥{min(below)},")
print(f"     incomparable to those in between.")
print()
print("="*78)
print("THE PICTURE THIS PRODUCES")
print("="*78)
print("""  V is a 25-dimensional box of ~1.4e22 configurations.
  The periodic system is a single monotone PATH of 118 points through it,
  each step adding one electron.
  Excited states are points OFF that path, at the same total Σv = Z.
  They are incomparable to the ground state of their own element and to
  a band of neighbours, and comparable only to distant members.

  So Reading B gives: ground states = a chain; excitation = lateral
  displacement off the chain at constant Σv. That is a clean and correct
  picture, but note what it is NOT — it is not a new lattice with new
  structure. V is a product of chains, so all its order theory is the
  trivial product theory. The interesting object was always the SUBSET.""")
print()
print("="*78)
print("READING B2: THE PROMOTION ORDER")
print("="*78)
print("""  Order configurations of FIXED Z by promotion: c ≤ c' iff c' is
  obtained from c by moving electrons to higher-energy columns. Take Z=11
  and enumerate all configurations with Σv=11 within the first few columns.""")
# enumerate configurations of Z=11 over first 6 columns
import itertools
sub=cols[:8]
caps=[CAP[c[1]] for c in sub]
confs=[]
def rec(i,rem,cur):
    if i==len(sub):
        if rem==0: confs.append(tuple(cur))
        return
    for t in range(0,min(caps[i],rem)+1):
        rec(i+1,rem-t,cur+[t])
rec(0,11,[])
print(f"\n  configurations of 11 electrons over the first 8 columns: {len(confs)}")
# promotion order: c <= c' if partial sums of c dominate those of c'
def psum(v): 
    s=[];t=0
    for x in v: t+=x; s.append(t)
    return s
def prom_leq(a,b):
    return all(x>=y for x,y in zip(psum(a),psum(b)))
g=tuple(list(gvec(11))[:8])
print(f"  ground state restricted: {g}")
mins=[c for c in confs if not any(prom_leq(d,c) and d!=c for d in confs)]
print(f"  minimal elements under promotion order: {len(mins)}")
print(f"  is the ground state the unique minimum? {mins==[g]}")
if mins!=[g]:
    print(f"    minima found: {mins[:4]}")
print("""
  The promotion order is the DOMINANCE ORDER on partial sums — a
  well-studied object (it is the dominance lattice on partitions).
  Its minimum is the configuration packing electrons into the lowest
  columns, i.e. the aufbau ground state.""")