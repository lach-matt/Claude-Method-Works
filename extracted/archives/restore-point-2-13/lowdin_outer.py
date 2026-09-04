import math, statistics as st
import numpy as np
from collections import defaultdict
src=open("channels_principle.py",encoding="utf-8").read()
src=src[:src.index('print("  THE PRINCIPAL STRUCTURE')]
g={}; exec(src,g)
CH=g["CH"]; config=g["config"]; L="spdfghi"
def outer(ne):
    cfg=config(ne)
    return cfg[-1] if cfg else (0,0,0)
def nmax(ne):
    cfg=config(ne)
    return max((n for n,l,o in cfg if o>0), default=0)
def lmax(ne):
    cfg=config(ne)
    return max((l for n,l,o in cfg if o>0), default=0)
for x in CH:
    n_,l_,o_=outer(x["ne"]-1)
    x["on"]=n_; x["ol"]=l_; x["oo"]=o_
    x["nmax"]=nmax(x["ne"]-1); x["lmax"]=lmax(x["ne"]-1)
    x["dl"]=x["l"]-l_          # how far the outer ℓ is from the core's outermost ℓ
    x["nl_core"]=n_+l_
allf=np.array([x["frac"] for x in CH]); tot=allf.var()
def ve(key):
    gr=defaultdict(list)
    for x in CH: gr[key(x)].append(x["frac"])
    gr={k:v for k,v in gr.items() if len(v)>=2}
    if not gr: return None,0
    w=sum(np.var(v)*len(v) for v in gr.values())/sum(len(v) for v in gr.values())
    return 100*(1-w/tot), len(gr)
print("  WHAT PART OF THE CORE CONFIGURATION CARRIES frac(δ)?\n")
print(f"      {'grouping':<34}{'groups':>8}{'explained':>12}")
TESTS=[
 ("ℓ alone", lambda x:x["l"]),
 ("(ℓ, whole core config)", lambda x:(x["l"],x["ne"]-1)),
 ("(ℓ, outer core subshell n,ℓ)", lambda x:(x["l"],x["on"],x["ol"])),
 ("(ℓ, outer core n)", lambda x:(x["l"],x["on"])),
 ("(ℓ, outer core ℓ)", lambda x:(x["l"],x["ol"])),
 ("(ℓ, outer core n+ℓ)", lambda x:(x["l"],x["nl_core"])),
 ("(ℓ, outer occupancy)", lambda x:(x["l"],x["oo"])),
 ("(ℓ, ℓ − outer core ℓ)", lambda x:(x["l"],x["dl"])),
 ("(ℓ, p)", lambda x:(x["l"],x["p"])),
 ("(ℓ, p, outer core n)", lambda x:(x["l"],x["p"],x["on"])),
 ("(ℓ, n_max of core)", lambda x:(x["l"],x["nmax"])),
 ("(ℓ, ℓ_max of core)", lambda x:(x["l"],x["lmax"])),
]
for lab,k in TESTS:
    v,n=ve(k)
    if v is None: continue
    print(f"      {lab:<34}{n:>8}{v:>11.1f}%")
print()
print("  THE OUTER CORE SUBSHELL, ALONE, AGAINST THE WHOLE CONFIGURATION\n")
a,_=ve(lambda x:(x["l"],x["on"],x["ol"])); b,_=ve(lambda x:(x["l"],x["ne"]-1))
print(f"      outer subshell only : {a:.1f}%")
print(f"      whole configuration : {b:.1f}%")
print(f"      the outer subshell recovers {100*a/b:.0f}% of what the whole config gives")
print()
print("  AND WHAT frac(δ) LOOKS LIKE ON (ℓ, outer core subshell)\n")
gr=defaultdict(list)
for x in CH: gr[(x["l"],x["on"],x["ol"])].append(x["frac"])
print(f"      {'ℓ':>3}{'core outer':>12}{'n':>5}{'median frac':>14}{'sd':>8}")
for k in sorted(gr):
    v=gr[k]
    if len(v)<4: continue
    print(f"      {L[k[0]]:>3}{f'{k[1]}{L[k[2]]}':>12}{len(v):>5}{st.median(v):>14.3f}{st.pstdev(v):>8.3f}")
