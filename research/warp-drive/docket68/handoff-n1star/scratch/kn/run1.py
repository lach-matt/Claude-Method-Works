import sys, os, io, contextlib, importlib.util
D="/home/user/Claude-Method-Works/research/warp-drive/docket68"
f=sys.argv[1]
p=os.path.join(D,"lemmas",f)
if not os.path.exists(p): p=os.path.join(D,"bulk",f)
sys.path[:0]=[os.path.dirname(p), D, os.path.dirname(D)]; os.chdir(D)
spec=importlib.util.spec_from_file_location("wt_"+f[:-3],p); mod=importlib.util.module_from_spec(spec)
try:
    with contextlib.redirect_stdout(io.StringIO()):
        spec.loader.exec_module(mod); ok=mod.selftest()
    print(f, "PASS" if ok else "FAIL", flush=True)
except Exception as ex:
    print(f, "RAISE", type(ex).__name__, str(ex)[:100], flush=True)
