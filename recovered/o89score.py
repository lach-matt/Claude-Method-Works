"""o89score.py -- assemble a segmented seed run into a chain-step verdict and score it
against the sealed row. Margins are compared BOTH raw and on a COMMON candidate set
(F76.2: a raw margin comparison across different candidate sets compares gaps to
DIFFERENT runner-ups)."""
import sys, os, json
sys.path.insert(0, os.getcwd())
import nlchain as NC
Z = int(sys.argv[1]); seeds = sys.argv[2:]
rows = NC.load(); sealed = rows[Z]
sealedD = {k: v for k, v in sealed["order"]}
out = {}
for s in seeds:
    rec = {r["item"]: r for r in map(json.loads, open(f"../pack77/o89_{Z}_{s}.jsonl"))}
    Eref = rec["ref"]["E"]
    D = {k: round(v["E"] - Eref, 5) for k, v in rec.items() if k != "ref" and v["conv"]}
    srt = sorted(D, key=lambda k: D[k])
    out[s] = dict(Eref=Eref, D=D, order=srt, ent=srt[0],
                  margin=round(D[srt[1]] - D[srt[0]], 5) if len(srt) > 1 else None,
                  nfail=sum(1 for k, v in rec.items() if k != "ref" and not v["conv"]))
print(f"SEALED  Z={Z}  ent {sealed['ent']}  margin {sealed['margin']}  nfail {sealed['nfail']}")
print(f"        order {' '.join(k for k,_ in sealed['order'])}")
for s in seeds:
    o = out[s]
    common = [k for k in o["D"] if k in sealedD]
    d = {k: (o["D"][k] - sealedD[k]) * 1000 for k in common}          # mHa
    com = sum(d.values()) / len(d)
    dif = {k: d[k] - com for k in common}
    mx = max(abs(v) for v in dif.values())
    print(f"\nSEED {s}  ent {o['ent']}  margin {o['margin']}  nfail {o['nfail']}"
          f"   ENT_MATCH={o['ent']==sealed['ent']}"
          f"  ORDER_MATCH={o['order']==[k for k,_ in sealed['order']]}")
    print(f"        order {' '.join(o['order'])}")
    print(f"        raw dmargin  {None if o['margin'] is None else round((o['margin']-sealed['margin'])*1000,4)} mHa"
          f"   candidates common with sealed: {len(common)}/{len(sealedD)}")
    print(f"        COMMON mode  {com:+.6f} mHa      max|DIFFERENTIAL| {mx:.6f} mHa")
    print(f"        criterion    2*D={2*mx:.6f} mHa   vs m(Z)={sealed['margin']*1000:.3f} mHa"
          f"   -> {'HOLDS' if 2*mx < sealed['margin']*1000 else 'FAILS'}"
          f"   headroom {sealed['margin']*1000-2*mx:+.3f} mHa")