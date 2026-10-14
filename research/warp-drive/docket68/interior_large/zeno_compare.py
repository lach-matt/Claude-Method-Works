"""zeno_compare.py -- item 396: is g_ss -> 0 at x = 0.22 by s = -0.80 the solution or the scheme?

The record's own scheme -- B7's damped single grid, Nx = 28, kap = 4, tilt 0.5, the brane rows algebraic -- continued from
the trusted state (s = -0.503) to s = -0.80, stepped one step at a time with its history kept and a 20-minute stop.  A(x)
and the DeTurck norm are then set beside the third attempt's (zeno_half_satw_10.pkl, item 395) at the same s, the
brane root marched in order along the steps (README B5).

python3 zeno_compare.py run       -- the continuation (saves zeno_compare_28.pkl)
python3 zeno_compare.py table     -- the comparison
"""
import numpy as np, sys, time, pickle
import core_fw as C, interior_fw as IF, interior_damp as ID
import zeno_run as Z
from scipy.integrate import Radau

S_END = -0.80
OUT = "zeno_compare_28.pkl"
XS = (0.10, 0.14, 0.18, 0.22, 0.26, 0.30, 0.50, 0.75, 1.00)
TARGETS = (-0.503, -0.55, -0.60, -0.65, -0.70, -0.75, -0.79)


def run():
    T = pickle.load(open(Z.TRUSTED, "rb"))
    I = ID.Damped(28, Z.B, Z.STATIC, Z.KAP, Z.AT); I.lastbr = T["br"].copy()
    t0 = time.time()

    def rhs(s, Y):
        if time.time() - t0 > Z.WALL:
            raise TimeoutError("20-minute stop")
        d = I.rhs(s, Y)
        if not np.all(np.isfinite(d)):
            raise FloatingPointError("non-finite right-hand side at s = %.6f" % s)
        return d
    ts, ys = [T["s"]], [T["Y"].copy()]; status, msg = 0, "reached the end"
    try:
        sol = Radau(rhs, T["s"], T["Y"].copy(), S_END, rtol=1e-8, atol=1e-10)
        while sol.status == "running":
            err = sol.step()
            if sol.status == "failed":
                status, msg = -1, str(err); break
            ts.append(sol.t); ys.append(sol.y.copy())
    except (TimeoutError, FloatingPointError, ValueError, np.linalg.LinAlgError) as ex:
        status, msg = -2, "%s: %s" % (type(ex).__name__, ex)
    took = time.time() - t0
    pickle.dump(dict(t=np.array(ts), y=np.array(ys).T, status=status, msg=msg, took=took), open(OUT, "wb"))
    print("single grid: status %d (%s), %d steps, %.0f s, reached s = %.4f" % (status, msg, len(ts) - 1, took, ts[-1]),
          flush=True)


def single_states():
    """the single grid's fields at each target s (nearest step at or past it), the brane root marched in order"""
    T = pickle.load(open(Z.TRUSTED, "rb")); R = pickle.load(open(OUT, "rb"))
    I = ID.Damped(28, Z.B, Z.STATIC, Z.KAP, Z.AT); I.lastbr = T["br"].copy(); m = I.m
    out, todo = {}, [t for t in TARGETS if t >= R["t"][-1] - 1e-12]
    for k in range(len(R["t"])):
        s = R["t"][k]; Y = R["y"][:, k]
        Xf, Vf = I.brane_values(s, Y[:5 * m].reshape(5, m), Y[5 * m:].reshape(5, m))
        if todo and s <= todo[0] + 1e-12:
            phi = np.nanmax(np.abs(IF.phi_at(I, s, Y)))
            out[todo.pop(0)] = (s, Xf.copy(), phi, I.xn.copy())
    if R["t"][-1] > TARGETS[-1]:
        s = R["t"][-1]; Y = R["y"][:, -1]
        out[s] = (s, I.brane_values(s, Y[:5 * m].reshape(5, m), Y[5 * m:].reshape(5, m))[0].copy(),
                  np.nanmax(np.abs(IF.phi_at(I, s, Y))), I.xn.copy())
    return out, R


def zeno_states():
    """the third attempt's fields at the same s (nearest step at or past it), on its folded mesh"""
    R = pickle.load(open("zeno_half_satw_10.pkl", "rb")); ts, ys = R["t"], R["y"]
    I = Z.FoldedSATWeak(10, Z.B, Z.STATIC, Z.KAP, Z.AT, n0=Z.SAT_N0, ns=Z.SAT_NS); m = I.m
    P = np.repeat(Z.P_EXP, m); sv = 1 - np.exp(ts); out = {}
    for tgt in TARGETS + (sv[-1],):
        k = int(np.argmin(np.abs(sv - tgt))) if tgt >= sv[-1] - 1e-12 else None
        if k is None:
            continue
        lam = ts[k]; e = np.exp(-P * lam); X = (e * ys[:5 * m, k]).reshape(5, m)
        Xs = (-(e * (ys[5 * m:, k] - P * ys[:5 * m, k])) / np.exp(lam)).reshape(5, m)
        with np.errstate(all="ignore"):
            phi = np.nanmax(np.abs(IF.phi_at(I, sv[k], np.concatenate([X.ravel(), Xs.ravel()]))))
        out[tgt] = (sv[k], X, phi)
    return out, I


def interp_zeno(I, X, x):
    """a field on the folded mesh at x, by its own part's polynomial"""
    full, P, Mi = I.fold
    for k, (idx, Dl, D2l, w, loc) in enumerate(I.blk):
        if k == 0 and x <= loc[-1] + 1e-15:
            vals = np.zeros(len(full)); vals[P] = X[idx]; vals[Mi] = X[idx]
            return float(C.bary_interp(full, vals, [x])[0])
        if k > 0 and loc[0] - 1e-15 <= x <= loc[-1] + 1e-15:
            return float(C.bary_interp(loc, X[idx], [x])[0])
    raise ValueError(x)


def table():
    S, R = single_states(); Zs, I = zeno_states()
    print("single grid: status %d (%s), reached s = %.4f in %.0f s" % (R["status"], R["msg"], R["t"][-1], R["took"]))
    print("A(x) -- single grid (record's scheme, Nx = 28)  |  third attempt (folded, coupled, weak brane)")
    print("   s       " + " ".join("x=%-6.2f" % x for x in XS) + "   min A (where)      phi_max")
    for tgt in sorted(set(S) | set(Zs), reverse=True):
        if tgt in S:
            s, Xf, phi, xn = S[tgt]
            A = [float(C.bary_interp(xn, Xf[2], [x])[0]) for x in XS]
            fine = np.linspace(0, 1, 2001); Af = C.bary_interp(xn, Xf[2], fine).ravel(); j = int(np.argmin(Af))
            print("S %7.4f  " % s + " ".join("%+.4f" % a for a in A) + "  %+.4f (x=%.3f)  %.1e" % (Af[j], fine[j], phi))
        if tgt in Zs:
            s, X, phi = Zs[tgt]
            A = [interp_zeno(I, X[2], x) for x in XS]
            fine = np.linspace(0, 1, 2001); Af = np.array([interp_zeno(I, X[2], x) for x in fine]); j = int(np.argmin(Af))
            print("Z %7.4f  " % s + " ".join("%+.4f" % a for a in A) + "  %+.4f (x=%.3f)  %.1e" % (Af[j], fine[j], phi))


if __name__ == "__main__":
    {"run": run, "table": table}[sys.argv[1]]()
