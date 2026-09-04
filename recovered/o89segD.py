"""o89segD.py -- s78 ITEM 2. ZENO-SEGMENTED phase O under SEED D.
F77.3 REPAIR: PHASE A RUNS ON EVERY INVOCATION, BEFORE ANY SOLVE, AND A NON-ZERO
VERDICT HALTS THE DRIVER. The can-fail is reachable by the driver by construction.
THE RULING PATH IS UNTOUCHED: candidates, reference and every solve go through
nlchain's own helpers and NG.run_guarded. The ONLY variable is t7b_hf.HF.seed.
    python3 ../pack78/o89segD.py <Z> next
    python3 ../pack78/o89segD.py <Z> list
Receipts append to ../pack78/o89D_<Z>.jsonl; resume from the receipt file (F53.3).
"""
import sys, os, json, time
os.environ.setdefault("SIC_NOCLAMP", "1"); os.environ.setdefault("SUBCELL", "1")
sys.path.insert(0, os.getcwd())
sys.path.insert(0, os.path.abspath("../pack78"))
import seedD78 as SD
import nlchain as NC
import nlguard as NG

Z, cmd = int(sys.argv[1]), sys.argv[2]
REC = f"../pack78/o89D_{Z}.jsonl"

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
    print(f"Z={Z} seed=D  {len(done)}/{len(items)} done   remaining: {' '.join(todo) or 'NONE'}")
    sys.exit(0)

# ---- GATE. Runs first, every time. Nothing below executes if it does not pass. ----
rc = SD.phase_A(Zs=(19, Z))
if rc != 0:
    print("!!! DRIVER HALTED: PHASE A did not pass. No solve was attempted.")
    sys.exit(4)

if not todo:
    print(f"Z={Z} seed=D: COMPLETE {len(done)}/{len(items)}"); sys.exit(0)

it = todo[0]
SD.install("D")                                    # the ONLY variable
cfg = cfg_prev if it == "ref" else NC.add(cfg_prev, cmap[it])
t0 = time.time()
g = NG.run_guarded(Z, cfg, it)
r = dict(item=it, Z=Z, seed="D", E=g["E"], it_n=g["it"], rung=g["rung"],
         conv=g["conv"], err=g["err"], sec=int(time.time() - t0))
with open(REC, "a") as f:
    f.write(json.dumps(r) + "\n")
print(f"  {it:>3}  E={r['E']}  it={r['it_n']}  rung={r['rung']}  conv={r['conv']}  {r['sec']}s"
      f"   [{len(done)+1}/{len(items)}]")