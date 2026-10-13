"""the lambda leg of an hr_run, restartable: from the s-leg's last state (or from this script's own checkpoint if one
exists), stepped by hand with progress lines and a checkpoint every 25 steps"""
import numpy as np, pickle, sys, os
import interior_fw as IF, interior_damp as ID, interior_gauge as IG
src, lam_end = sys.argv[1], float(sys.argv[2])
P = pickle.load(open(src, "rb")); b, Nx, kap, at = P["b"], P["Nx"], P["kap"], P["at"]
st = dict(file="fw_bt%g_24_24.npy" % b, Ns=24, Nx=24)
I = ID.Damped(Nx, b, st, kap, at); I.lastbr = ID.static_brane(b); m = I.m
for k in range(len(P["t"])):
    I.brane_values(P["t"][k], P["y"][:5 * m, k].reshape(5, m), P["y"][5 * m:, k].reshape(5, m))
s0, Y0 = P["t"][-1], P["y"][:, -1]
ck = src.replace("_s.pkl", "_lam.pkl")
prior_lt, prior_ly = None, None
for f in (ck, ck + ".part"):                   # a finished segment, then a segment cut off by a timeout
    if os.path.exists(f):
        C = pickle.load(open(f, "rb"))
        if prior_lt is None:
            prior_lt, prior_ly = C["lt"], C["ly"]
        elif C["lt"][-1] > prior_lt[-1]:
            prior_lt = np.concatenate([prior_lt, C["lt"][1:]])
            prior_ly = np.concatenate([prior_ly, C["ly"][:, 1:]], axis=1)
if prior_lt is not None:
    pickle.dump(dict(lt=prior_lt, ly=prior_ly, Nx=P["Nx"], b=P["b"], kap=P["kap"], at=P["at"], src=src), open(ck, "wb"))
    if os.path.exists(ck + ".part"):
        os.remove(ck + ".part")
    for k in range(len(prior_lt)):
        s, Y = IF.state_s(I, prior_lt[k], prior_ly[:, k])
        I.brane_values(s, Y[:5 * m].reshape(5, m), Y[5 * m:].reshape(5, m))
    s0, Y0 = IF.state_s(I, prior_lt[-1], prior_ly[:, -1])
    print("resuming from %s at lambda %.4f (s %.3f), %d steps saved" % (ck, prior_lt[-1], s0, len(prior_lt)), flush=True)
else:
    print("starting the lambda leg at s %.3f" % s0, flush=True)
meta = dict(Nx=Nx, b=b, kap=kap, at=at, src=src)
lt, ly = IG.run_steps(I, Y0, s0, lam_end, rtol=1e-8, save=ck + ".part", meta=meta)
if prior_lt is not None:
    lt, ly = np.concatenate([prior_lt, lt[1:]]), np.concatenate([prior_ly, ly[:, 1:]], axis=1)
pickle.dump(dict(lt=lt, ly=ly, **meta), open(ck, "wb"))
print("saved %s: lambda %.4f -> %.4f" % (ck, lt[0], lt[-1]), flush=True)
