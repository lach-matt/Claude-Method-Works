import math
from collections import Counter, defaultdict
src=open("/tmp/ryd.py",encoding="utf-8").read()
src=src[:src.index('print("  A VARIABLE FOR THE RYDBERG')]
g={}; exec(src,g)
R=g["R"]; cfg_c,cp,out_,n0_,ORDER=g["cfg_c"],g["cp"],g["out_"],g["n0_"],g["ORDER"]
L="spdfg"
EL={1:"H",2:"He",3:"Li",4:"Be",5:"B",6:"C",7:"N",8:"O",9:"F",10:"Ne",11:"Na",
    12:"Mg",13:"Al",14:"Si",15:"P",16:"S",17:"Cl",18:"Ar",19:"K",20:"Ca",21:"Sc",
    22:"Ti",23:"V",24:"Cr",25:"Mn",26:"Fe",27:"Co",28:"Ni",29:"Cu",30:"Zn",
    31:"Ga",32:"Ge",37:"Rb",38:"Sr",39:"Y",40:"Zr",48:"Cd",49:"In",55:"Cs",
    56:"Ba",57:"La",58:"Ce",80:"Hg",81:"Tl",83:"Bi",88:"Ra",89:"Ac",90:"Th"}
RO={1:"I",2:"II",3:"III",4:"IV",5:"V",6:"VI",9:"IX",11:"XI",15:"XV",16:"XVI"}
for r in R:
    r["reg"]=(1 if (r["p"]>=1 and r["n0"]>r["on"]) else
              2 if r["p"]>=1 else
              3 if r["Z"]<r["T"] else 4)
print("  WHAT IS REGIME 2?   penetrating, but n₀ ≤ n_out\n")
print("  The Rydberg orbital's principal number is AT OR BELOW the core's")
print("  outermost — it lives inside the outer shell rather than beyond it.\n")
v=[r for r in R if r["reg"]==2]
print(f"      {len(v)} channels\n")
print(f"      {'species':<10}{'ℓ':>3}{'n₀':>4}{'n_out':>7}{'ℓ_out':>7}{'δ':>9}")
seen=set()
for r in sorted(v,key=lambda x:(x["Z"],x["c"],x["l"])):
    key=(r["Z"],r["c"],r["l"])
    if key in seen: continue
    seen.add(key)
    n_,l_,o_=out_(r["ne"]-1,r["c"])
    sp=f"{EL.get(r['Z'],r['Z'])} {RO.get(r['c'],r['c'])}"
    print(f"      {sp:<10}{L[r['l']]:>3}{r['n0']:>4}{n_:>7}{L[l_]:>7}{r['d']:>9.4f}")
print()
print("  THE ELEMENTS THIS PICKS OUT\n")
c=Counter(EL.get(r["Z"],r["Z"]) for r in v)
print("      " + "  ".join(f"{k}:{n}" for k,n in c.most_common()))
print()
print("  AND WHICH ℓ\n")
c2=Counter(L[r["l"]] for r in v)
print("      " + "  ".join(f"{k}:{n}" for k,n in c2.most_common()))
print()
print("  THE CHEMISTRY\n")
print("      n₀ ≤ n_out means the incoming electron enters a shell the atom has")
print("      ALREADY passed — an inner shell being filled after an outer one has")
print("      begun. That is the definition of a TRANSITION element.")
print()
print("      regime 1  the electron goes outside everything      main group")
print("      regime 2  it goes INSIDE the outermost shell        transition / f-block")
print("      regime 3  no orbital of its ℓ exists in the core, and it stays out")
print("      regime 4  no orbital of its ℓ exists, and it has collapsed in")
print()
print("      The chemical signature of regime 2 is VARIABLE VALENCE: because the")
print("      incoming electron sits inside the valence shell, it is shielded from")
print("      bonding, and the atom can lose the outer s electrons without touching")
print("      it — or lose it too. That is why transition metals show many oxidation")
print("      states and main-group elements show one or two.")
