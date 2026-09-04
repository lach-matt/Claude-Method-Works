import numpy as np
from itertools import product
from collections import Counter
CONS=[(1,0,lambda x:x[0]-1),(2,1,lambda x:4*x[1]+2),(3,2,lambda x:x[2]),(7,2,lambda x:x[2]),
      (5,4,lambda x:x[4]-1),(6,5,lambda x:4*x[5]+2),(6,3,lambda x:x[3])]
AX=[list(range(1,4)),list(range(0,2)),list(range(1,4)),list(range(0,4)),
    list(range(1,4)),list(range(0,2)),list(range(0,4)),list(range(0,4))]
LAM={z for z in product(*AX) if all(z[v]<=ub(z) for v,p,ub in CONS)}
NAME={0:'n',1:'l',2:'k',3:'q',4:'e',5:'f',6:'g',7:'2S'}
print("="*88)
print("  IS Λ A TWO-BODY SYSTEM?")
print("="*88)
print("""
     n --- l --- k --- q --- g --- f --- e
                 |
                 2S

  **The tree has two ends.** One end is a PARENT configuration (n, l, k)
  with its spin 2S; the other is a TARGET configuration (e, f) with its
  occupancy g. They meet at q — the number transferred.

  **That is the shape of a two-body problem: two objects and a coupling.**
  Test whether Λ factorises that way.
""")
A_ax=[0,1,2,7]; B_ax=[4,5,6]; C_ax=[3]
PA={tuple(z[i] for i in A_ax) for z in LAM}
PB={tuple(z[i] for i in B_ax) for z in LAM}
PQ={z[3] for z in LAM}
print("     body A  (n, l, k, 2S) : %d distinct states"%len(PA))
print("     body B  (e, f, g)     : %d distinct states"%len(PB))
print("     coupling q            : %d values"%len(PQ))
print("     product |A|x|B|x|q|   : %d"%(len(PA)*len(PB)*len(PQ)))
print("     |Lambda|              : %d"%len(LAM))
print("     ratio                 : %.4f"%(len(LAM)/(len(PA)*len(PB)*len(PQ))))
print("""
  **IT DOES NOT FACTORISE AS A BARE PRODUCT.** The two bodies are coupled
  through q twice over: q <= k ties the transfer to the parent, and g <= q
  ties the target's occupancy to the transfer.
""")
print("="*88)
print("  BUT IT DOES SEPARATE — CONDITIONALLY, AS A TWO-BODY PROBLEM DOES")
print("="*88)
print("""
  A two-body problem separates into centre-of-mass and RELATIVE motion.
  The analogue: fix the coupling q and ask whether A and B become
  independent.
""")
print("  %6s%12s%12s%16s%14s%10s"%("q","|A| given q","|B| given q","product","actual","factors?"))
print("  "+"-"*72)
allok=True
for qv in sorted(PQ):
    S={z for z in LAM if z[3]==qv}
    a={tuple(z[i] for i in A_ax) for z in S}
    bq={tuple(z[i] for i in B_ax) for z in S}
    ok=len(S)==len(a)*len(bq)
    allok&=ok
    print("  %6d%12d%12d%16d%14d%10s"%(qv,len(a),len(bq),len(a)*len(bq),len(S),"YES" if ok else "no"))
print("\n     **separates at every fixed q : %s**"%allok)
print("""
  **THAT IS EXACTLY THE TWO-BODY STRUCTURE.** Conditioned on the coupling,
  the parent and the target are independent — the lattice is a product of
  two lattices at each value of the transferred quantity, summed over the
  transfer:

        |Lambda| = SUM_q  |A(q)| x |B(q)|
""")
tot=0
for qv in sorted(PQ):
    S={z for z in LAM if z[3]==qv}
    a={tuple(z[i] for i in A_ax) for z in S}
    bq={tuple(z[i] for i in B_ax) for z in S}
    tot+=len(a)*len(bq)
print("     SUM_q |A(q)| x |B(q)| = %d      |Lambda| = %d      match: %s"%(tot,len(LAM),tot==len(LAM)))
print("="*88)
print("  AND THE CYLINDER IS THE SAME FACT SEEN GEOMETRICALLY")
print("="*88)
print("""
  Chapter 7 finds the shape is a cylinder over nu. **A cylinder is a
  product: a base times a fibre.** The two-body separation is that product
  named in the lattice's own coordinates —

     the BASE   is the coupling q, the axis along the cylinder
     the FIBRE  is A(q) x B(q), the cross-section at each q

  **and the cross-section is itself a product of two lattices.**
""")
print("  %6s%16s"%("q","cross-section"))
for qv in sorted(PQ):
    S={z for z in LAM if z[3]==qv}
    print("  %6d%16d"%(qv,len(S)))
print("""
  **The cylinder is not a metaphor. It is the fibration over the transfer
  coordinate, and its fibres are two-body products.**
""")
print("="*88)
print("  ON 10D AND 11D — WHAT THIS BOOK CAN AND CANNOT SAY")
print("="*88)
print("""
  **CANNOT:** Section 22.6's dimension test showed Λ closes at every
  dimension from 2 to 8 with E = 0 throughout. **There is no critical
  dimension in an index**, so nothing here explains why 10 and 11 are
  special and 12 is not. That comes from anomaly cancellation and
  supersymmetry representation theory, neither of which is an order
  property.

  **CAN:** the book's own vocabulary does distinguish the two regimes you
  name, and distinguishes them sharply:

     a LINEAR family      p = 1, V = infinite, second difference zero.
                          **Exactly determined by two points.** L4, L5 and
                          the string mass spectrum all sit here.

     an OSCILLATING family  the sign of a finite difference CHANGES.
                          **That is a refusal**, and Section 15.10.4 counts
                          them: it is the signature of a perturbation or a
                          bifurcation, not of stability.

  **So in this book's terms the two states are not two kinds of stability.
  One is exactness and the other is refusal**, and they sit at opposite
  ends of the same measure. Whether that maps onto 10D and 11D is not
  something the index can decide, and saying otherwise would be the
  coherent fabrication of Section 10.7.2.
""")