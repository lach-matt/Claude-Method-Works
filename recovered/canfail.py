import sys, os, time
sys.path.insert(0, '/home/claude/s77/rt')
sys.argv = ['x', '--show']
import importlib.util
spec = importlib.util.spec_from_file_location("ns77", "/home/claude/s77/pack77/nodespec77.py")
ns = importlib.util.module_from_spec(spec)
try: spec.loader.exec_module(ns)
except SystemExit: pass
import nlchain as NC
rows = NC.load(); cfg = NC.cfg_from_chain(88, rows)
for ch,(n,l) in (('5f',(5,3)),('5g',(5,4))):
    t0=time.time()
    try:
        E = ns.energy(89, NC.add(cfg,(n,l)))
        print(f"  {ch}: NO-RAISE (channel converged)  E={E}  {int(time.time()-t0)}s")
    except ns.NodeSpectrum as ex:
        print(f"  {ch}: RAISED CLASS {ex.rec['cls']}  <-- CAN-FAIL BROKEN if this is a converged channel")
    except Exception as ex:
        print(f"  {ch}: ERR {type(ex).__name__}: {str(ex)[:80]}")