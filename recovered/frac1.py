import math, statistics as st
from collections import defaultdict
src=open("channels_principle.py",encoding="utf-8").read()
src=src[:src.index('print("  THE PRINCIPAL STRUCTURE')]
g={}; exec(src,g)
CH=g["CH"]; config=g["config"]; L="spdfghi"
EL={3:"Li",4:"Be",11:"Na",12:"Mg",13:"Al",19:"K",20:"Ca",21:"Sc",22:"Ti",
    37:"Rb",38:"Sr",39:"Y",55:"Cs",56:"Ba",57:"La",29:"Cu",30:"Zn",31:"Ga",
    47:"Ag",48:"Cd",49:"In",79:"Au",80:"Hg",81:"Tl",83:"Bi",5:"B",6:"C",
    14:"Si",15:"P",16:"S",17:"Cl",18:"Ar",7:"N",8:"O",9:"F",10:"Ne",26:"Fe"}
RO={1:"I",2:"II",3:"III",4:"IV",5:"V",6:"VI",9:"IX",11:"XI",15:"XV",16:"XVI"}
def cstr(ne):
    return "".join(f"{n}{L[l]}{o}" for n,l,o in config(ne) if o>0)
print("  DO WE ALREADY HOLD THE TWO SHAPES?\n")
print("  A · ISOELECTRONIC — one core, varying Z. Is frac(δ) constant along it?\n")
seq=defaultdict(list)
for x in CH: seq[x["ne"]].append(x)
best=[]
for ne,v in seq.items():
    sp={(y["Z"],y["c"]) for y in v}
    if len(sp)>=3: best.append((ne,len(sp),len(v)))
best.sort(key=lambda t:-t[2])
print(f"      {'Nₑ':>4}{'species':>9}{'channels':>10}   core")
for ne,ns,nc in best[:8]:
    print(f"      {ne:>4}{ns:>9}{nc:>10}   {cstr(ne-1)}")
print()
for ne,ns,nc in best[:3]:
    v=seq[ne]
    print(f"      Nₑ = {ne}  ({cstr(ne-1)} core)\n")
    byl=defaultdict(dict)
    for y in v: byl[y["l"]][(y["Z"],y["c"])]=y["frac"]
    hdr=sorted({k for d in byl.values() for k in d})
    print(f"          {'ℓ':>3}" + "".join(
        f"{EL.get(z,z)+' '+RO.get(c,str(c)):>11}" for z,c in hdr) + f"{'spread':>9}")
    for l in sorted(byl):
        row=byl[l]
        vals=[row.get(k) for k in hdr]
        sp=max(x for x in vals if x is not None)-min(x for x in vals if x is not None) if sum(x is not None for x in vals)>1 else float('nan')
        print(f"          {L[l]:>3}" + "".join(
            f"{(f'{x:.3f}' if x is not None else '—'):>11}" for x in vals) + f"{sp:>9.3f}")
    print()