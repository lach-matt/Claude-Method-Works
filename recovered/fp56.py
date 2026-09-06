# fp56.py -- THE FIRST PROTON, READ. No solve. Sealed rows only.
# s55 RULING: every table comparing entrants carries n+l for BOTH channels.
import json, sys
L="spdfghi"
rows={x["Z"]:x for x in (json.loads(l) for l in open("nlchain.jsonl"))}
def nl(c):
    n=int(c[0]); l=L.index(c[1]); return n+l
def table(Z):
    r=rows[Z]
    ch=r["chan"]
    items=[]
    for k,v in (ch.items() if isinstance(ch,dict) else ch):
        if v is None: continue
        items.append((k,float(v)))
    items.sort(key=lambda t:t[1])
    return r,items
for Z in (57,89):
    r,items=table(Z)
    ent=r["ent"]; S=nl(ent)
    print(f"=== Z={Z}  sealed ent={ent} (n+l={S})  margin={r['margin']}  D_ent={r['D_ent']}")
    print(f"    {'chan':>6}{'n+l':>5}{'D (Ha)':>12}   rank")
    for i,(k,v) in enumerate(items,1):
        mark=" <-- ENTRANT" if k==ent else ""
        same="*" if nl(k)==S else " "
        print(f"    {k:>6}{nl(k):>5}{v:>12.5f}{same:>4}{i:>4}{mark}")
    same_shell=[(k,v) for k,v in items if nl(k)==S]
    print(f"    shell n+l={S} members, deepest first: "+", ".join(f"{k}({v:.5f})" for k,v in same_shell))
    fch=[(k,v) for k,v in same_shell if k[1]=="f"]
    dch=[(k,v) for k,v in same_shell if k[1]=="d"]
    if fch and dch:
        print(f"    shortfall_f = D({dch[0][0]}) - D({fch[0][0]}) = {dch[0][1]-fch[0][1]:.5f}")
    print()