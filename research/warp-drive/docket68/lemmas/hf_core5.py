#!/usr/bin/env python3
"""hf_core5.py -- items 506-508: the shell's exact vacuum sequence onto its seed, computed inward to the record's own
quantum boundary x = 1 and not excised; the record's core (transition5q) beyond it.  (Header completed with the runs.)

python3 hf_core5.py [--selftest | --run i | --merge]
"""
import sys, os, json, time
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import hf_mirror5 as H

RUNS = os.path.join(HERE, "data", "hf_core5_runs.json")


def y_core(m, L):
    """the record's quantum boundary x = l5^2 sqrt(K) = 1 on the seed (K = 72 mu^2/r^8): r_q^4 = sqrt(72) mu l5^2, y = r^-1/2"""
    return (np.sqrt(72)*m/L)**-0.125


# (lam, A, Ny, Nx, seed m0, inner boundary y at x = 1 on the seed, cfl); L = mu0/l5^2 = 100 and 1000
SEQ = {100: [(0.1, 1.0, 20, 16), (0.05, 1.0, 24, 16), (0.025, 1.0, 28, 16)],
       1000: [(0.1, 1.0, 24, 16), (0.05, 1.0, 28, 16), (0.025, 1.0, 32, 16)]}
ALL = [(L,) + c + (1.0, round(y_core(1.0, L), 6), 2.0) for L in (100, 1000) for c in SEQ[L]]
key = lambda cfg: "_".join("%g" % c_ for c_ in cfg)


def run_one(i):
    cfg = ALL[i]
    t0 = time.time()
    hist = H.evolve(*cfg[1:], log=lambda h: print(h, flush=True))
    json.dump({key(cfg): hist}, open(RUNS.replace(".json", "_%d.json" % i), "w"))
    print(cfg, "%.0fs" % (time.time() - t0), flush=True)


def merge():
    out = json.load(open(RUNS)) if os.path.exists(RUNS) else {}
    for i in range(len(ALL)):
        f = RUNS.replace(".json", "_%d.json" % i)
        if os.path.exists(f):
            out.update(json.load(open(f)))
    json.dump(out, open(RUNS, "w"), indent=1)


def words():
    s = open(H.RULINGS).read()
    return "Redo the work without the inner horizon" in s and "There is always a seed" in s


def stats():
    R = json.load(open(RUNS))
    P = json.load(open(H.RUNS))
    out = {}
    for cfg in ALL:
        k = key(cfg)
        if k not in R:
            continue
        h = R[k]; e = H.end_stats(h)
        pk = H.key(cfg[1:5])                                  # 498's pinned row at the same (lam, A, Ny, Nx), excised at 1.15
        ext = None
        if pk in P:                                           # the exterior after the shell: mass and spread at infinity
            f = H.end_stats(P[pk])
            ext = dict(dM=abs(e["M_end"] - f["M_end"]), ds=abs(e["spread"] - f["spread"]), off=f["offset"], spr=f["spread"])
        e.update(L=cfg[0], lam=cfg[1], ext=ext, Wex_max=max(x["W_ex"] for x in h), nz_all=[x["nz"] for x in h],
                 hf_core=cfg[1]*cfg[2]*cfg[6]**3)            # lam A r^-3/2 at the core boundary
        out[k] = e
    return out


def checks(o):
    c = {}
    c["C0 words of 506 and 508"] = o["words"]
    s = o["stats"]
    for L in (100, 1000):
        ks = [key(cfg) for cfg in ALL if cfg[0] == L]
        if not all(k in s for k in ks):
            c["C* runs at L = %d present" % L] = False
            continue
        a, b, d = (s[k] for k in ks)
        c["C1 L=%d: the exterior is 498's after the shell (the boundary trapped)" % L] = (
            all(t["ext"] is not None and t["ext"]["dM"] < 0.15*t["ext"]["off"] and t["ext"]["ds"] < 0.15*t["ext"]["spr"]
                for t in (a, b, d)) and a["ext"]["dM"] > d["ext"]["dM"])
        c["C2 L=%d: every departure falls with lambda, the interior to x = 1 included" % L] = all(
            x[q] > y[q] for x, y in ((a, b), (b, d)) for q in ("spread", "offset", "dW", "dW_all", "P", "b"))
        c["C3 L=%d: one zero per column to x = 1 (no inner horizon); the core boundary trapped" % L] = all(
            t["nz_min"] == t["nz"] == 1 and t["Wex_max"] < 0 for t in (a, b, d))
        c["C4 L=%d: the horizon onto sqrt(mu) at first order" % L] = (b["dr"] < 0.6*a["dr"] and d["dr"] < 0.6*b["dr"]
                                                                       and b["width"] < 0.6*a["width"] and d["width"] < 0.6*b["width"])
    return c


def report():
    o = dict(words=words(), stats=stats())
    for k, v in checks(o).items():
        print("%-72s %s" % (k, "PASS" if v else "FAIL"))
    for k, t in o["stats"].items():
        print("  %-30s spread %.2e offset %.2e |W-W_V| %.2e (passage %.3f) P %.3f W_ex<=%.2f nz %d-%d dM_ext %.1e hf@core %.2f" % (
            k, t["spread"], t["offset"], t["dW"], t["dW_all"], t["P"], t["Wex_max"], t["nz_min"], t["nz"],
            t["ext"]["dM"] if t["ext"] is not None else -1, t["hf_core"]))
    return o


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        o = report(); c = checks(o)
        print("%s: %d/%d" % (os.path.basename(__file__), sum(c.values()), len(c))); sys.exit(0 if all(c.values()) else 1)
    if "--run" in sys.argv:
        run_one(int(sys.argv[sys.argv.index("--run") + 1])); sys.exit(0)
    if "--merge" in sys.argv:
        merge(); sys.exit(0)
    for i, c in enumerate(ALL):
        print(i, c)
