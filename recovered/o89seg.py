"""o89seg.py -- s77. ZENO-SEGMENTED phase O: ONE guarded solve per invocation.
Detached jobs do not survive a tool-call boundary in this container (observed at s77),
so the run is segmented instead. THE RULING PATH IS UNTOUCHED: the candidate list, the
reference and every solve go through nlchain's own helpers and NG.run_guarded.
    python3 ../pack77/o89seg.py <Z> <seed> next     # do the next unfinished item, exit
    python3 ../pack77/o89seg.py <Z> <seed> list     # what is done, what remains
Receipts append to ../pack77/o89_<Z>_<seed>.jsonl. Resume is from the receipt file (F53.3).
"""
import sys, os, json, time
os.environ.setdefault("SIC_NOCLAMP", "1"); os.environ.setdefault("SUBCELL", "1")
sys.path.insert(0, os.getcwd())
import seedtest as ST          # sealed instrument: seeds + install()
import nlchain as NC
import nlguard as NG

Z, seed, cmd = int(sys.argv[1]), sys.argv[2], sys.argv[3]
REC = f"../pack77/o89_{Z}_{seed}.jsonl"

rows = NC.load()
cfg_prev = NC.cfg_from_chain(Z - 1, rows)
items = ["ref"] + [NC.tagof(c) for c in NC.candidates(cfg_prev)]
cmap = {NC.tagof(c): c for c in NC.candidates(cfg_prev)}

done = {}
if os.path.exists(REC):
    for ln in open(REC):
        if ln.strip():
            r = json.loads(ln); done[r["item"]] = r
todo = [i for i in items if i not in done]

if cmd == "list":
    print(f"Z={Z} seed={seed}  {len(done)}/{len(items)} done   remaining: {' '.join(todo) or 'NONE'}")
    sys.exit(0)

if not todo:
    print(f"Z={Z} seed={seed}: COMPLETE {len(done)}/{len(items)}"); sys.exit(0)

it = todo[0]
ST.install(seed)                                   # the ONLY variable
cfg = cfg_prev if it == "ref" else NC.add(cfg_prev, cmap[it])
t0 = time.time()
g = NG.run_guarded(Z, cfg, it)
r = dict(item=it, Z=Z, seed=seed, E=g["E"], it_n=g["it"], rung=g["rung"],
         conv=g["conv"], err=g["err"], sec=int(time.time() - t0))
with open(REC, "a") as f:
    f.write(json.dumps(r) + "\n")
print(f"  {it:>3}  E={r['E']}  it={r['it_n']}  rung={r['rung']}  conv={r['conv']}  {r['sec']}s"
      f"   [{len(done)+1}/{len(items)}]")