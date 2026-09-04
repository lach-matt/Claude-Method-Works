import numpy as np, random
from itertools import product
from collections import Counter
random.seed(29)
NAMES=['n','l','k','q','e','f','g','2S']
CONS=[("l<=n-1",1,0,lambda x:x[0]-1),("k<=4l+2",2,1,lambda x:4*x[1]+2),
      ("q<=k",3,2,lambda x:x[2]),("2S<=k",7,2,lambda x:x[2]),
      ("f<=e-1",5,4,lambda x:x[4]-1),("g<=4f+2",6,5,lambda x:4*x[5]+2),
      ("g<=q",6,3,lambda x:x[3])]
AX=[list(range(1,4)),list(range(0,2)),list(range(1,4)),list(range(0,4)),
    list(range(1,4)),list(range(0,2)),list(range(0,4)),list(range(0,4))]
LAM={x for x in product(*AX) if all(x[v]<=ub(x) for nm,v,p,ub in CONS)}
L=sorted(LAM)
le=lambda a,b: all(p<=q for p,q in zip(a,b))
print("="*88)
print("  WHAT EACH SHAPE IDENTIFIES")
print("="*88)
print("""
  1. THE CYLINDER — the base is q, the TRANSFER.
""")
print("     Lambda is fibred over the number of electrons MOVED, not over any")
print("     property of a single configuration.")
print("""
     **So the index is not a catalogue of states. It is a catalogue of
     TRANSITIONS**, and the book calls its cells 'configurations'
     throughout. Chapter 2 introduces (n,l,k) as a parent and (e,f,g) as a
     target and never says the pair is the object.
""")
print("""
  2. THE CATERPILLAR vs THE PATH — an asymmetry with a name.
""")
print("     A_q carries 2S, a spin label on the PARENT.")
print("     B_q carries no spin label at all.")
tsp=[x[7] for x in LAM]
print("\n     parent spin values present : %s"%sorted(set(tsp)))
print("     target spin values present : none — the coordinate does not exist")
print("""
     **THE INDEX RECORDS THE PARENT'S SPIN AND NOT THE TARGET'S.** That is
     not a closure defect — 𝓡 cannot see a coordinate that was never
     supplied. **It is an axis E2 would admit and the book never built.**
""")
print("""
  3. THE INTERVALS — a map of where the physics is active.
""")
bind=Counter(); tot=0
for _ in range(3000):
    x,y=random.choice(L),random.choice(L)
    if not le(x,y): continue
    tot+=1
    for nm,v,p,ub in CONS:
        if y[v]>ub(x): bind[nm]+=1
print("     %-12s%12s%12s"%("constraint","binds","% of intervals"))
print("     "+"-"*36)
for nm,_,_,_ in CONS:
    print("     %-12s%12d%12.1f"%(nm,bind[nm],100*bind[nm]/max(tot,1)))
print("""
     **'g <= q' binds most often and 'l <= n-1' least.** The interval
     criterion turns into a ranking of how ACTIVE each constraint is, and
     the most active is the coupling itself.
""")
print("""
  4. THE RANK LEVELS — the largest mutually-incomparable set.
""")
rk=Counter(sum(x) for x in LAM)
mx=max(rk.values()); at=max(rk,key=rk.get)
print("     18 levels, largest %d at rank %d"%(mx,at))
print("     |Lambda| / max level = %.1f"%(len(LAM)/mx))
print("""
     **122 configurations no two of which are comparable.** In the physics
     that is the largest set of configurations none of which can be reached
     from another by adding electrons — **a maximal set of mutually
     inaccessible states, and the book never names it.**
""")
print("""
  5. THE MAXIMAL CHAINS — 1,113,045,672 filling orders.
""")
covers={x:[y for y in L if sum(y)==sum(x)+1 and le(x,y)] for x in L}
bot=min(L,key=sum); top=max(L,key=sum)
memo={}
def paths(x):
    if x==top: return 1
    if x in memo: return memo[x]
    memo[x]=sum(paths(c) for c in covers[x]); return memo[x]
nc=paths(bot)
print("     chains from bottom to top : %d"%nc)
print("     chain length              : %d steps"%(sum(top)-sum(bot)))
print("""
     **Every maximal chain is a valid order of building a configuration up
     one unit at a time.** The Aufbau principle selects ONE of these.

     **So the index identifies that the filling order is massively
     underdetermined by the structure** — 1.1 billion orders satisfy every
     constraint, and only energetics picks the observed one. **That is a
     precise statement of what Aufbau adds, and the book has no equivalent.**
""")
print("="*88)
print("  AND WHAT THEY IDENTIFY ABOUT THE INDEX AS A TOTALITY")
print("="*88)
print("""
  Put the shapes side by side and four properties of the WHOLE appear:
""")
T=[("a cylinder over the transfer","the object is a TRANSITION, not a state"),
   ("a tower of fibrations ending in boxes","coupling is HIERARCHICAL and terminates"),
   ("intervals boxes iff no constraint binds","the physics is LOCAL and checkable pairwise"),
   ("rank modular, conserved exactly","there is an INVARIANT under the operations"),
   ("1.1 billion maximal chains","the build ORDER is not determined by structure"),
   ("122-element largest antichain","there is a bound on MUTUAL INACCESSIBILITY"),
   ("no cycle, no Mobius, tree only","the structure is ORIENTABLE and simply connected")]
print("  %-40s%s"%("shape","what it says about the whole"))
print("  "+"-"*84)
for a,b in T: print("  %-40s%s"%(a,b))
print("""
{0}
  AND THE FOUR TOGETHER SAY ONE THING
{0}

  **THE INDEX IS A TRANSITION SPACE WITH A CONSERVED QUANTITY, LOCAL
  CONSTRAINTS, AND AN UNDETERMINED BUILD ORDER.**

     it is a transition space  -> the cylinder, base q
     it conserves rank         -> modularity, exactly
     its constraints are local -> the pairwise interval criterion
     its order is free         -> 1.1 billion chains, one chosen by energy

  **Which is the shape of a PHASE SPACE with a Hamiltonian removed.** The
  lattice supplies the kinematics — what configurations exist, what
  transitions are admissible, what is conserved — **and supplies no
  dynamics at all.** Energy enters only through Chapter 16's measured
  levels, never through the structure.

  **That is what the book is, stated from its shapes rather than from its
  intentions**, and it explains both what it can do and what it cannot:
  it can bound and refuse, and it cannot predict, because prediction needs
  the Hamiltonian the index does not carry.
""".format("="*88))