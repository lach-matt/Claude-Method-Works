import eldata as ed
from itertools import combinations
CAP={0:2,1:6,2:10,3:14,4:18}
cols=[(n,l) for n in range(1,8) for l in range(0,min(n,5))]
CI={c:i for i,c in enumerate(cols)}
AUF=[(1,0),(2,0),(2,1),(3,0),(3,1),(4,0),(3,2),(4,1),(5,0),(4,2),(5,1),(6,0),
     (4,3),(5,2),(6,1),(7,0),(5,3),(6,2),(7,1)]

def ground_vector(Z):
    v=[0]*len(cols); rem=Z
    for c in AUF:
        t=min(rem,CAP[c[1]]); v[CI[c]]=t; rem-=t
        if rem<=0: break
    return tuple(v)

print("="*78)
print("READING B1: THE OCCUPANCY-VECTOR SPACE")
print("="*78)
print("""  A configuration is a vector v ∈ ℕ^25, one coordinate per (n,ℓ) column,
  with 0 ≤ v_c ≤ 2(2ℓ+1). This represents an atom EXACTLY, excited or not,
  because it records every subshell simultaneously. The box
      V = ∏_c [0, cap(c)]
  is a product of chains, hence a distributive lattice automatically.""")
tot=1
for c in cols: tot*= (CAP[c[1]]+1)
print(f"\n  |V| = ∏(cap+1) = {tot:,}")
print(f"  log10 = {__import__('math').log10(tot):.2f}")
print()
print("  The 118 ground states are 118 points of V. Where do they sit?")
G=[ground_vector(z) for z in sorted(ed.E)]
print(f"  ground vectors: {len(set(G))} distinct (should be 118): {len(set(G))==118}")
# Are they a chain?
def vleq(a,b): return all(x<=y for x,y in zip(a,b))
chain=all(vleq(G[i],G[i+1]) for i in range(len(G)-1))
print(f"  are the ground states a CHAIN in V (each ≤ the next)? {chain}")
if not chain:
    bad=[(i+1,i+2) for i in range(len(G)-1) if not vleq(G[i],G[i+1])]
    print(f"    breaks at Z pairs: {bad[:8]}{'...' if len(bad)>8 else ''}")
    for i,j in bad[:3]:
        a,b=G[i-1],G[j-1]
        d=[(cols[t],a[t],b[t]) for t in range(len(cols)) if a[t]!=b[t]]
        print(f"      Z={i}->{j}: {[(f'{c[0]}{chr(115) if c[1]==0 else \"spdfg\"[c[1]]}',x,y) for c,x,y in d]}")
print()
print("="*78)
print("IS THE GROUND-STATE SEQUENCE A MAXIMAL CHAIN OF V?")
print("="*78)
print(f"  |V| is astronomically larger than 118, so the ground states form a")
print(f"  path of length 118 in a space of {tot:.2e} points.")
print(f"  Each step Z -> Z+1 adds exactly one electron, so consecutive")
print(f"  vectors differ by 1 in a single coordinate — EXCEPT at anomalies.")
one_step=sum(1 for i in range(len(G)-1)
             if sum(abs(a-b) for a,b in zip(G[i],G[i+1]))==1)
print(f"  steps that move exactly one electron by one: {one_step}/{len(G)-1}")