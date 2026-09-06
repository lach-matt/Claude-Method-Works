import eldata as ed
from itertools import combinations
CAP=lambda l: 2*(2*l+1)
AUF=sorted({(n,l) for s in range(1,20) for n in range(1,20) for l in range(0,5)
            if n+l==s and l<=n-1}, key=lambda c:(c[0]+c[1], c[0]))
def valence_ideal(Z):
    rem=Z; last=None
    for (n,l) in AUF:
        t=min(rem,CAP(l))
        if t>0: last=(n,l,t)
        rem-=t
        if rem<=0: break
    return last
IDEAL={z:valence_ideal(z) for z in range(1,119)}
MEAS=dict(ed.E)
L=[(n,l,k) for n in range(1,8) for l in range(0,min(n,5)) for k in range(1,CAP(l)+1)]
def leq(a,b): return all(x<=y for x,y in zip(a,b))

print("="*78); print("WHICH ASSIGNMENT IS THE MODULE USING?"); print("="*78)
for z in [57,58,64,24,29,46,78]:
    print(f"  Z={z:>3} {ed.SYM[z]:>3}: module {str(MEAS[z]):>12}  strict-aufbau {str(IDEAL[z]):>12}")
print("""
  La measured ground state is [Xe]5d¹6s² → (5,2,1). The module has that.
  Strict aufbau would give 4f¹ → (4,3,1). So the MODULE uses MEASURED
  configurations and my 'independent' version used idealised aufbau.
  My printed note in AUDIT 0 had this backwards.""")

print()
print("="*78); print("DO THE STRUCTURAL RESULTS HOLD UNDER BOTH ASSIGNMENTS?"); print("="*78)
def check(name, occ):
    S=set(occ.values())
    ideal_ok = not any(leq(y,x) and y not in S for x in S for y in L)
    cols=set((n,l) for (n,l,k) in S)
    partial=[]
    for (n,l) in cols:
        h=max(k for (nn,ll,k) in S if (nn,ll)==(n,l))
        if h!=CAP(l): partial.append(((n,l),h))
    # Z linear extension?
    zs=sorted(occ)
    pairs=[(a,b) for a in zs for b in zs if a!=b and leq(occ[a],occ[b])]
    vz=sum(1 for a,b in pairs if a>b)
    return dict(cells=len(S), ideal=ideal_ok, partial=partial,
                cols=len(cols), pairs=len(pairs), zviol=vz)
for nm,occ in [('MEASURED (module)',MEAS),('IDEALISED aufbau',IDEAL)]:
    r=check(nm,occ)
    print(f"\n  {nm}")
    print(f"    distinct cells occupied : {r['cells']}")
    print(f"    order ideal             : {r['ideal']}")
    print(f"    occupied columns        : {r['cols']}")
    print(f"    partially-filled columns: {r['partial'] if r['partial'] else 'none'}")
    print(f"    comparable pairs        : {r['pairs']}")
    print(f"    Z-order violations      : {r['zviol']}  "
          f"{'→ Z IS a linear extension' if r['zviol']==0 else '→ NOT'}")
print()
print("  Same 118 cells under both? ", set(MEAS.values())==set(IDEAL.values()))
diff=[z for z in range(1,119) if MEAS[z]!=IDEAL[z]]
print(f"  elements assigned differently: {len(diff)}")