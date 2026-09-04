# fp56.py -- THE FIRST PROTON, READ. No solve. Sealed rows only (nlchain.jsonl 'order').
# s55 RULING: every table comparing entrants carries n+l for BOTH channels.
import json
L="spdfghi"
rows={x["Z"]:x for x in (json.loads(l) for l in open("nlchain.jsonl"))}
nl=lambda c:int(c[0])+L.index(c[1])
out={}
for Z in (57,89):
    r=rows[Z]; ent=r["ent"]; S=nl(ent); od=[(k,v) for k,v in r["order"]]
    print(f"=== Z={Z}   sealed ent={ent} (n+l={S})   D_ent={r['D_ent']}   margin={r['margin']}")
    print(f"    ref_cfg tail: ...{r['ref_cfg'][-14:]}    rec_ent={r['rec_ent']}")
    print(f"    {'rank':>4}{'chan':>6}{'n+l':>5}{'D (Ha)':>12}  in-shell")
    for i,(k,v) in enumerate(od,1):
        print(f"    {i:>4}{k:>6}{nl(k):>5}{v:>12.5f}{'  *' if nl(k)==S else '   '}"
              +("   <-- ENTRANT" if k==ent else ""))
    shell=[(k,v) for k,v in od if nl(k)==S]
    print(f"    SHELL n+l={S}: "+", ".join(f"{k} {v:.5f}" for k,v in shell))
    lower=[(k,v) for k,v in od if nl(k)<S]
    print(f"    channels of LOWER n+l present in the candidate set: {lower if lower else 'NONE'}")
    f=[x for x in shell if x[0][1]=="f"]; d=[x for x in shell if x[0][1]=="d"]
    p=[x for x in shell if x[0][1]=="p"]
    rank_f=[k for k,_ in shell].index(f[0][0])+1 if f else None
    print(f"    f channel {f[0][0] if f else '-'}  rank within its own shell = {rank_f} of {len(shell)}")
    if f and d:
        sf=d[0][1]-f[0][1]
        print(f"    shortfall_f = D({d[0][0]}) - D({f[0][0]}) = {sf:.5f}")
        out[Z]=dict(ent=ent,S=S,f=f[0],d=d[0],p=(p[0] if p else None),rank_f=rank_f,
                    shortfall=sf,nlower=len(lower))
    print()
json.dump(out,open("/tmp/fp56.json","w"),indent=1)
print("wrote /tmp/fp56.json")