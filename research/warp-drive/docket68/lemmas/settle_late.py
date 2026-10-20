#!/usr/bin/env python3
"""settle_late.py -- item 540: whether the hole settles at late times, for the math to determine.  M: "whether the hole
settles at late times - for the math to determine".  Labels: computed (exact unless marked numerical), READ, deduced,
M's.  This file is its run part; the checks are added once the runs are pinned.

The runs: hf_mirror5's own nonlinear five-dimensional vacuum scheme (T^2 with both reflections, cohomogeneity three,
ingoing Bondi slices compactified at past null infinity), taken through the shell and then on to late times, the step
widened once the incoming waves have passed.  Checkpointed, so a container restart costs only the steps since the last
checkpoint.

python3 settle_late.py --run NAME     (NAME in RUNS; resumes from its checkpoint)
"""
import json, os, sys, time
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import hf_mirror5 as H

DATA = os.path.join(HERE, "data")
# name: (lam, A, Ny, Nx, m0, v_end); the shell passes past null infinity over 0.5 < v < 3.5
RUNS = {"a": (0.1, 1.0, 16, 10, 1.0, 40.0), "b": (0.1, 1.0, 20, 16, 1.0, 40.0)}
V_LATE, DV_LATE, CFL, EVERY = 4.0, 0.04, 0.8, 0.25
Y_PROBE = (0.5, 0.8, 1.0)


def probe(g, d, mu):
    """the non-round part at fixed y: the squashing fields' amplitude, W's spread over the sphere and its mean's
    departure from Tangherlini of mass mu; the shift's amplitude"""
    W = 1 + g.Y ** 3 * d["w"]
    out = []
    for y0 in Y_PROBE:
        i = int(np.argmin(np.abs(g.y - y0)))
        y = g.y[i]
        out.append(dict(y=float(y), F=float(np.abs(d["F"][i]).max()), G=float(np.abs(d["G"][i]).max()),
                        Wspread=float(W[i].max() - W[i].min()), Wmean=float(W[i].mean()),
                        dWt=float(W[i].mean() - (1 - mu * y ** 4)), q=float(np.abs(d["q"][i]).max())))
    return out


def run(name):
    lam, A, Ny, Nx, m0, v_end = RUNS[name]
    ck = os.path.join(DATA, "settle_late_%s.ckpt.npz" % name)
    hj = os.path.join(DATA, "settle_late_%s.json" % name)
    g = H.Grid(Ny, Nx, H.YEX)
    data = H.Data(lam, A, m0=m0)
    fb, fa = H.filters(g)
    mu_end = data.mu_pred(10.0)
    if os.path.exists(ck):
        z = np.load(ck)
        st = [z["s0"], z["s1"], z["s2"], z["s3"]]
        v, nxt = float(z["v"]), float(z["nxt"])
        hist = json.load(open(hj))["hist"]
    else:
        Z = np.zeros((Ny + 1, Nx + 1))
        st = [Z.copy(), Z.copy(), np.full(Nx + 1, -m0 * H.YEX), np.zeros(Nx + 1)]
        v, nxt, hist = 0.0, 0.0, []
    t0, i = time.time(), 0
    while True:
        k1, d = H.rhs(g, st, v, data)
        if v >= nxt - 1e-9:
            rec = H.diag(g, st, d, v, data)
            rec["probe"] = probe(g, d, mu_end)
            hist.append(rec)
            nxt += EVERY
            print(json.dumps({"v": rec["v"], "P": rec["P"], "q": rec["q"], "dW": rec["dW"],
                              "probe_F": [p["F"] for p in rec["probe"]]}), flush=True)
        if v >= v_end - 1e-9:
            break
        if v < V_LATE:
            dv = min(lam * 0.125, nxt - v)
        else:
            speed = H.YEX ** 3 * np.abs(1 + H.YEX ** 3 * st[2]).max() / 4       # the excision's outgoing speed
            dv = min(DV_LATE, CFL * (g.y[-1] - g.y[-2]) / speed, nxt - v)
        s2 = [a + 0.5 * dv * b for a, b in zip(st, k1)]; k2 = H.rhs(g, s2, v + dv / 2, data)[0]
        s3 = [a + 0.5 * dv * b for a, b in zip(st, k2)]; k3 = H.rhs(g, s3, v + dv / 2, data)[0]
        s4 = [a + dv * b for a, b in zip(st, k3)]; k4 = H.rhs(g, s4, v + dv, data)[0]
        st = [a + dv / 6 * (b1 + 2 * b2 + 2 * b3 + b4) for a, b1, b2, b3, b4 in zip(st, k1, k2, k3, k4)]
        st = [fb(st[0]), fb(st[1]), fa(st[2]), fa(st[3])]
        v += dv
        i += 1
        if not np.all(np.isfinite(st[0])) or np.abs(st[3]).max() > 1e3:
            raise FloatingPointError("blew up at v = %.3f" % v)
        if i % 10 == 0:
            np.savez(ck + ".tmp.npz", s0=st[0], s1=st[1], s2=st[2], s3=st[3], v=v, nxt=nxt)
            json.dump({"cfg": RUNS[name], "hist": hist}, open(hj + ".tmp", "w"))
            os.replace(ck + ".tmp.npz", ck)
            os.replace(hj + ".tmp", hj)
    json.dump({"cfg": RUNS[name], "hist": hist, "done": True, "mu_end": mu_end}, open(hj, "w"))
    print("done", name, "%.0fs this leg" % (time.time() - t0), flush=True)


# ------------------------------------------------------------------ the determination
import importlib.util
import sympy as sp

RULINGS = os.path.join(HERE, "..", "M-RULINGS-2026-10-03.md")
WORDS = "whether the hole settles at late times - for the math to determine"
MUT = set()
QNM_S2, QNM_T2 = 0.9477 + 0.2561j, 1.5106 + 0.3575j        # [CLY03b] Tables 1 and 3, n = 0, l = 2 (via settle5, READ)
ER_READ = ("Let xi(i), 1 <= i <= D-2 be commuting Killing vector fields such that for each i, (a) ... vanishes at at "
           "least one point of the spacetime ... and (b) ... Then the two planes orthogonal to the xi(i) are "
           "integrable")                                    # Emparan-Reall, hep-th/0110258v2 p. 5
GIS_READ = "We prove the uniqueness theorem for asymptotically flat static vacuum black hole solutions in higher " \
           "dimensional space-times"                        # Gibbons-Ida-Shiromizu, gr-qc/0203004 abstract
KI_READ = ("all gauge-invariant variables can be represented as combinations of this field and its derivatives",
           "H_T is gauge-invariant by itself", "a shift of the mass parameter of the black hole")   # hep-th/0305147v3
DH_READ = ("orbitally stable (in the fully non-linear theory) with respect to vacuum perturbations of initial data "
           "preserving triaxial Bianchi IX symmetry")       # Dafermos-Holzegel, gr-qc/0510051 abstract


def _settle5():
    spec = importlib.util.spec_from_file_location("sl_settle5", os.path.join(HERE, "..", "n1star", "settle5.py"))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def words():
    return WORDS in open(RULINGS, encoding="utf-8").read()


def endpoint(control=False):
    """S1: a stationary T^2-invariant metric in the class, in the block form the integrability theorem gives, loses its
    t-phi and phi1-phi2 terms under the reflections, so the time Killing field is hypersurface orthogonal (static)"""
    r, th = sp.symbols("r theta", positive=True)
    X = sp.symbols("t r theta p1 p2")
    names = ["tt", "t1", "t2", "11", "12", "22"]
    c = {k: sp.Function("g" + k)(r, th) for k in names}
    full = sp.Matrix([[c["tt"], 0, 0, c["t1"], c["t2"]], [0, 1, 0, 0, 0], [0, 0, r ** 2, 0, 0],
                      [c["t1"], 0, 0, c["11"], c["12"]], [c["t2"], 0, 0, c["12"], c["22"]]])
    keep = full
    for i in (3, 4):                                         # phi_i -> -phi_i: components odd in phi_i must vanish
        R = sp.eye(5); R[i, i] = -1
        inv = R * keep * R
        if not control:
            keep = (keep + inv) / 2
    xi = [keep[0, j] for j in range(5)]                      # the lowered time Killing field
    dxi = [[sp.diff(xi[b], X[a]) - sp.diff(xi[a], X[b]) for b in range(5)] for a in range(5)]
    tw = 0
    for a in range(5):
        for b in range(5):
            for d in range(5):
                if len({a, b, d}) == 3:
                    tw += sp.simplify(xi[a] * dxi[b][d]) ** 2
    return sp.simplify(tw) == 0 and keep[0, 3] == 0 and keep[3, 4] == 0


def linear(control=False):
    """S2: the class carries only scalar- and tensor-type modes (settle5 T1); Kodama-Ishibashi's reconstruction of the
    scalar-type metric from the master field has the coefficient H = m + 6x in its denominators, positive on the whole
    exterior for l >= 2, and their potential is settle5's"""
    S5 = _settle5()
    l, x = sp.symbols("l x", positive=True)
    m = l * (l + 2) - 3
    H = m + 6 * x if not control else m - 30 * x
    pos = all(sp.N(H.subs({l: L, x: X0})) > 0 for L in (2, 4, 6) for X0 in (0, sp.Rational(1, 2), 1))
    r, rh, V = S5.potentials(2, "scalar")
    xx = rh ** 2 / r ** 2
    m2 = 5
    Q = (81 * 16 * xx ** 3 + 12 * (4 * 13 * m2 + 3 * (-1) * 4 * 1) * xx ** 2 - 36 * (-m2 + 12) * m2 * xx
         + 16 * m2 ** 3 + 60 * m2 ** 2)
    VKI = (1 - xx) * Q / (16 * r ** 2 * (m2 + 6 * xx) ** 2)
    return bool(S5.t1() and pos and sp.simplify(VKI - V) == 0)


def _maxima(v, a, v0):
    out = []
    for i in range(1, len(a) - 1):
        if v[i] >= v0 and a[i] > a[i - 1] and a[i] >= a[i + 1]:
            out.append((v[i], a[i]))
    return out


def analyse(name, v0=8.0):
    J = json.load(open(os.path.join(DATA, "settle_late_%s.json" % name)))
    h = J["hist"]
    mu = H.Data(*J["cfg"][:2], m0=J["cfg"][4]).mu_pred(10.0)
    rh = mu ** 0.5
    v = np.array([r["v"] for r in h])
    res = {"v_end": float(v[-1]), "mu": mu, "rh": rh, "probes": []}
    for k in range(len(h[0]["probe"])):
        a = np.array([max(r["probe"][k]["F"], r["probe"][k]["G"]) for r in h])
        w = np.array([r["probe"][k]["Wspread"] for r in h])
        mx = _maxima(v, a, v0)
        if MUT and "flat" in MUT:
            mx = [(vv, a[np.searchsorted(v, v0)]) for vv, _ in mx]
        rate = -np.polyfit([p[0] for p in mx], np.log([p[1] for p in mx]), 1)[0] if len(mx) >= 3 else float("nan")
        gap = float(np.median(np.diff([p[0] for p in mx]))) if len(mx) >= 3 else float("nan")
        i0, i1 = int(np.searchsorted(v, v0)), len(v) - 1
        res["probes"].append(dict(y=h[0]["probe"][k]["y"], rate=float(rate), gap=gap, n=len(mx),
                                  ratio=float(a[i1] / a[i0]), wratio=float(w[i1] / w[i0]),
                                  dWt_end=float(h[-1]["probe"][k]["dWt"]),
                                  drift=float(abs(h[-1]["probe"][k]["Wmean"] - h[-9]["probe"][k]["Wmean"]) / 2.0)))
    return res


if __name__ == "__main__":
    if "--run" in sys.argv:
        run(sys.argv[sys.argv.index("--run") + 1])
