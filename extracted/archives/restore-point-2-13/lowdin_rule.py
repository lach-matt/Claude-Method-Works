import math
from collections import Counter, defaultdict
import statistics as st
src=open("madelung.py",encoding="utf-8").read()
src=src[:src.index('print(f"  {len(CH)} measured channels')]
g={}; exec(src,g)
CH=g["CH"]; config=g["config"]
L="spdfghi"
EL={3:"Li",4:"Be",5:"B",6:"C",7:"N",8:"O",9:"F",10:"Ne",11:"Na",12:"Mg",13:"Al",
    14:"Si",15:"P",16:"S",17:"Cl",18:"Ar",19:"K",20:"Ca",21:"Sc",22:"Ti",26:"Fe",
    30:"Zn",31:"Ga",32:"Ge",37:"Rb",38:"Sr",48:"Cd",55:"Cs",56:"Ba",80:"Hg",83:"Bi",
    1:"H",2:"He"}
RO={1:"I",2:"II",3:"III",4:"IV",5:"V",6:"VI",9:"IX",11:"XI",15:"XV",16:"XVI"}
def core_p(ne,l): return sum(1 for n,ll,o in config(ne) if ll==l and o>0)
def pred(p,l): return p - min(p, max(2-l,0))
print("  THE RULE AS A PREDICTOR   floor(δ) = p − min(p, max(2−ℓ, 0))\n")
ok=0; off=Counter(); rows=[]
for x in CH:
    p=core_p(x["ne"]-1,x["l"])
    f=math.floor(x["d"]); q=pred(p,x["l"])
    off[f-q]+=1
    if f==q: ok+=1
    rows.append((x,p,f,q))
print(f"      {len(CH)} channels · exact {ok} ({100*ok/len(CH):.1f}%)")
print("      residual floor(δ) − prediction: " + "  ".join(
    f"{k:+d}: {v}" for k,v in sorted(off.items())))
print()
print("  BY ℓ\n")
print(f"      {'ℓ':>3}{'n':>6}{'exact':>8}{'rate':>8}{'median residual':>18}")
for l in sorted({x["l"] for x in CH}):
    v=[(x,p,f,q) for x,p,f,q in rows if x["l"]==l]
    e=sum(1 for _,_,f,q in v if f==q)
    print(f"      {L[l]:>3}{len(v):>6}{e:>8}{100*e/len(v):>7.1f}%"
          f"{st.median([f-q for _,_,f,q in v]):>18.1f}")
print()
print("  THE CASES THAT MISS, AT s\n")
miss=[(x,p,f,q) for x,p,f,q in rows if x["l"]==0 and f!=q]
print(f"      {len(miss)} of {sum(1 for x in CH if x['l']==0)}\n")
print(f"      {'species':<10}{'Nₑ':>5}{'p':>4}{'δ':>9}{'floor':>7}{'pred':>6}{'diff':>6}")
for x,p,f,q in sorted(miss,key=lambda z:-abs(z[2]-z[3]))[:14]:
    sp=f"{EL.get(x['Z'],'Z'+str(x['Z']))} {RO.get(x['c'],x['c'])}"
    print(f"      {sp:<10}{x['ne']:>5}{p:>4}{x['d']:>9.3f}{f:>7}{q:>6}{f-q:>6}")
print()
print("  AND WHAT THE ALTERNATIVE 'free = shells with n ≤ 2' GIVES\n")
def pred2(ne,l):
    # count core shells of this l with n <= 2
    return core_p(ne,l) - sum(1 for n,ll,o in config(ne) if ll==l and o>0 and n<=2)
ok2=0
for x in CH:
    if math.floor(x["d"])==pred2(x["ne"]-1,x["l"]): ok2+=1
print(f"      exact {ok2} of {len(CH)} ({100*ok2/len(CH):.1f}%)")
