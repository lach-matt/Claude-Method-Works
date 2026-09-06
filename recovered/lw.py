import math, statistics as st
from itertools import product
from collections import defaultdict, Counter
src=open("method_region.py",encoding="utf-8").read()
src=src[:src.index("\nwith State(")].replace("from zeno import State, step","")
g={}; exec(src,g)
load,op_S,op_R,op_W,region=g["load"],g["op_S"],g["op_R"],g["op_W"],g["region"]
config,mults,H=load()
Hin={k:v for k,v in H.items() if region(k[0],k[1],k[2],config)}
S=op_S(Hin,config); R=op_R(set(Hin)); Xs=set(Hin)
print("  IS W(X) AN INDEX IN ITS OWN RIGHT?\n")
print("  A set is an index if it has coordinates and a closure. Test: apply R to")
print("  W(X) itself. If W(X) is CLOSED under R, it is an index. If not, it is")
print("  a reachable set and nothing more.\n")
print(f"  {'tau':>6}{'|W|':>8}{'|R(W)|':>9}{'E(W)':>8}{'  closed?':<11}{'W ∩ R(X)':>10}")
for tau in (1.8,3.0,6.0,10.0,20.0,50.0):
    W=op_W(Hin,S,config,tau,region); Ws=set(W)
    RW=op_R(Ws)
    print(f"  {tau:>6.1f}{len(Ws):>8}{len(RW):>9}{len(RW)-len(Ws):>8}"
          f"{'  YES' if len(RW)==len(Ws) else '  no':<11}{len(Ws&R):>10}")
print()
W=op_W(Hin,S,config,20.0,region); Ws=set(W)
out=sorted(Ws-R)
print(f"  THE {len(out)} CELLS THE STEPS REACH AND THE ORDER REFUSES\n")
byl=Counter(x[2] for x in out); byc=Counter(x[1] for x in out)
byS=Counter(x[3] for x in out); byne=Counter(min(x[0]-x[1]+1,40) for x in out)
print("      by ℓ          : " + "  ".join(f"{'spdfghik'[l]}:{byl[l]}" for l in sorted(byl)))
print("      by charge     : " + "  ".join(f"{c}:{byc[c]}" for c in sorted(byc))[:76])
print("      by multiplicity: " + "  ".join(f"{s}:{byS[s]}" for s in sorted(byS)))
print()
print("  AND WHAT MAKES THEM DIFFERENT FROM THE ONES ℛ ADMITS\n")
inn=sorted((Ws&R)-Xs)
print(f"      {'':<16}{'reached AND placed':>20}{'reached, REFUSED':>19}")
print(f"      {'cells':<16}{len(inn):>20}{len(out):>19}")
for lab,f in (("median ℓ",lambda x:x[2]),("median charge",lambda x:x[1]),
              ("median Nₑ",lambda x:x[0]-x[1]+1),("median Z",lambda x:x[0])):
    a=st.median([f(x) for x in inn]) if inn else 0
    b=st.median([f(x) for x in out])
    print(f"      {lab:<16}{a:>20.1f}{b:>19.1f}")
print()
print("  the VALUES the walk assigns to the refused cells:\n")
v=[abs(W[k][0]) for k in out]
vi=[abs(W[k][0]) for k in inn] if inn else [0]
print(f"      refused : median {st.median(v):.4f}   range {min(v):.4f} – {max(v):.3f}")
print(f"      placed  : median {st.median(vi):.4f}   range {min(vi):.4f} – {max(vi):.3f}")