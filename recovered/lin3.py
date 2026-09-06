import numpy as np, eldata as ed
from collections import Counter
MN={21:19,22:51,23:54,24:57,26:61,27:64,28:67,29:72,39:20,40:49,41:53,42:56,
44:62,45:65,46:69,47:71,57:33,58:32,59:31,60:30,62:28,63:18,64:27,65:26,66:25,
67:24,68:23,69:22,70:17,71:21,72:50,73:52,74:55,75:58,77:63,78:66,79:70,90:47,92:45,
1:92,3:1,4:77,5:86,6:95,7:100,8:101,9:102,11:11,12:73,13:80,14:85,15:90,16:94,17:99,
19:10,20:16,30:76,31:81,32:84,33:89,34:93,35:98,37:9,38:15,48:75,49:79,50:83,51:88,
52:92,53:97,55:8,56:14,80:74,81:78,82:82,83:87,84:91,85:96}
com=sorted(z for z in MN if z in ed.E)
print("="*80); print("WHY Er/Tm/Yb/Lu FIT EXACTLY — the design is confounded"); print("="*80)
c=Counter()
for z in ed.E: c[ed.E[z][2]]+=1
print("  which ℓ-blocks contain each k value?")
for kv in range(1,15):
    ls=sorted(set(ed.E[z][1] for z in ed.E if ed.E[z][2]==kv))
    tag='  ← f-block ONLY' if ls==[3] else ''
    print(f"    k={kv:>2}: ℓ ∈ {ls}{tag}")
print("""
  k ≥ 11 occurs ONLY at ℓ=3. So a one-hot parameter h(k=11..14) is fitted
  from lanthanides alone and reproduces them exactly. The additive model
  is not capturing a sign flip — it is exploiting the fact that ℓ and k
  are CONFOUNDED in the data. High k implies f-block.

  Consequence: the additive R²=0.69 is not evidence that MN is additively
  separable. It is evidence that the design cannot distinguish 'k behaves
  differently in f' from 'high k values simply have low MN'.""")

print()
print("="*80); print("THE ORDER-THEORETIC QUESTION: IS MN A LINEAR EXTENSION OF Λ?"); print("="*80)
print("""  Λ is a partial order of dimension 3, i.e. the intersection of three
  linear extensions [Dushnik–Miller]. A ranking of the elements is
  ORDER-PRESERVING on Λ iff a ≤ b in Λ implies rank(a) ≤ rank(b).
  If MN were such a ranking, MN would be a linear extension of Λ and the
  connection would be exact. Test it.""")
def leq(a,b): return all(x<=y for x,y in zip(a,b))
pairs=[(a,b) for a in com for b in com if a!=b and leq(ed.E[a],ed.E[b])]
viol=[(a,b) for a,b in pairs if MN[a]>MN[b]]
print(f"\n  comparable pairs among the {len(com)} elements: {len(pairs)}")
print(f"  pairs where MN reverses the lattice order: {len(viol)}  ({100*len(viol)/len(pairs):.1f}%)")
print(f"  → MN is NOT a linear extension of Λ.")
print(f"  example reversals:")
for a,b in viol[:6]:
    print(f"    {ed.SYM[a]}{ed.E[a]} ≤ {ed.SYM[b]}{ed.E[b]} in Λ, but MN {MN[a]} > {MN[b]}")

# how do the other systems do?
print()
print("  Same test for the other sorting systems:")
Zr={z:z for z in com}
Mad={z:i for i,z in enumerate(sorted(com,key=lambda z:(ed.E[z][0]+ed.E[z][1],ed.E[z][0],ed.E[z][2])))}
for nm,R in [('atomic number Z',Zr),('Madelung order',Mad),('Pettifor MN',MN)]:
    v=sum(1 for a,b in pairs if R[a]>R[b])
    print(f"    {nm:<20} order-violations: {v:>4} / {len(pairs)}   "
          f"{'LINEAR EXTENSION' if v==0 else f'{100*v/len(pairs):.1f}% reversed'}")