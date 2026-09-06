"""nlstep47.py -- Z=57 (La) through the GUARD.  s47.

The chain step of nlchain.step, with hfc2.run2 replaced by nlguard.run_guarded so
a cycling channel is REPAIRED (rung 1) or REFUSED (no rung converges), never
silently returned.  F47.2.  Reference is the previous NEUTRAL's configuration on
the CURRENT nucleus (F40.1).  Configs built via nlchain.add (F42.2).
Does NOT write nlchain.jsonl -- prints only.  Sealing is a separate decision.
"""
import os, sys, json, time
os.environ.setdefault("SIC_NOCLAMP", "1"); os.environ.setdefault("SUBCELL", "1")
import nlguard as GD
import nlchain as NC

Z = int(sys.argv[1]) if len(sys.argv) > 1 else 57
rows = {d['Z']: d for d in map(json.loads, open('nlchain.jsonl'))}
cfg = NC.cfg_from_chain(Z - 1, rows)
print(f"Z={Z}  ref electrons={sum(k for _,_,k in cfg)}  "
      f"ref_cfg={''.join(f'{n}{chr(0)}'[:0] or f'{n}' + 'spdfg'[l] + str(k) for n,l,k in cfg)}",
      flush=True)

t0 = time.time()
ref = GD.run_guarded(Z, cfg)
print(f"REF  E={ref['E']}  it={ref['it']}  rung={ref['rung']}  conv={ref['conv']}",
      flush=True)
assert ref['conv'], "reference did not converge -- step cannot be scored"

cands = NC.candidates(cfg)
D, fail = {}, {}
for c in cands:
    tag = NC.tagof(c)
    r = GD.run_guarded(Z, NC.add(cfg, c))
    if r['conv']:
        D[tag] = dict(D=round(r['E'] - ref['E'], 5), it=r['it'], rung=r['rung'])
        print(f"   {tag:>3}  D={D[tag]['D']:+.5f}  it={r['it']:>4}  rung={r['rung']}",
              flush=True)
    else:
        fail[tag] = r['err']
        print(f"   {tag:>3}  FAIL  {r['err'][:70]}", flush=True)

srt = sorted(D, key=lambda k: D[k]['D'])
print(f"\n  ORDER: " + "  ".join(f"{k}:{D[k]['D']:+.5f}" for k in srt))
print(f"  ENTRANT = {srt[0]}   margin over {srt[1]} = "
      f"{D[srt[1]]['D'] - D[srt[0]]['D']:+.5f}  (F44.2: runner-up named)")
print(f"  rungs used: {sorted(set(v['rung'] for v in D.values()))}   "
      f"failures: {list(fail)}")
print(f"  total {int(time.time()-t0)}s")
