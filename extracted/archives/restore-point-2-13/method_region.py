#!/usr/bin/env python3
"""method_region.py -- the Method equation, applied where the spectra index fails.

Register 1196. The Method equation is the pair (R, C_tau) with two defects:

    E(X)   = |R(X)| - |X|        what the index ADMITS and does not hold     ORDINAL
    E_W(X) = |W(X)| - |X|        what the steps REACH and it does not have   METRIC

It was built for Lambda, where the second half is empty because a cell of Lambda carries
no value. On Lambda_spectra the second half is the whole difficulty, and that is exactly
where the fitted equation keeps failing: the l-tilt, the polarisation floor, the l = 2
band. Those are all failures of VALUATION, not of placement.

So this runs the Method equation properly on the region the existence partition says is
real — verified plus possible, 277 measured channels — and asks what its two defects say
that a least-squares residual cannot.

WHAT THE TWO DEFECTS DISTINGUISH

    a cell R admits and W cannot reach     the index says it belongs and no step gets
                                           a value to it — a PLACEMENT success and a
                                           VALUATION failure, which is a capture
    a cell W reaches and R excludes        the steps produce a value for a cell the
                                           order refuses — the walk is extrapolating
                                           beyond the index's own admission
    a cell both reach                      valued and placed: the working part
    a cell neither reaches                 outside the method entirely

The four counts are the Method equation's own reading of where an index is hard, and
they are computed rather than argued.
"""
import json, math, re, statistics as st
from itertools import product
from collections import defaultdict, deque
from zeno import State, step

def load():
    ns = {}
    exec(open("aufbau.py", encoding="utf-8").read().split("with State(")[0]
         .replace("from zeno import State, step", ""), ns)
    config, mults, H = ns["config"], ns["mults"], ns["measured"]()
    NEW = {(38,2,0,2):2.7113,(38,2,1,2):2.3501,(38,2,2,2):1.4577,(38,2,3,2):0.0618,
           (38,2,4,2):0.0098,(22,4,0,2):1.4153,(22,4,1,2):1.1506,(22,4,2,2):0.6202,
           (22,4,3,2):0.0774,(7,4,0,1):0.2948,(7,4,1,1):0.1782,(7,4,2,1):0.0335,
           (20,4,0,2):1.3280,(20,4,1,2):1.0703,(20,4,2,2):0.5526,
           (19,3,0,2):1.6589,(19,3,1,2):1.2110}
    H = dict(H); H.update(NEW)
    return config, mults, H

def parents(cfg):
    if not cfg: return 1
    n, l, occ = cfg[-1]; cap = 2*(2*l+1)
    return 1 if occ in (0, cap, 1, cap-1) else {0:1, 1:3, 2:16, 3:119}.get(l, 8)

def region(Z, c, l, config):
    ne = Z-c+1
    return Z <= 92 and c <= 10 and l <= 4 and parents(config(ne-1)) <= 1

def op_R(X, d=4):
    """PLACEMENT: the book's own operator, ordinal"""
    X = set(X); vals = [sorted({x[i] for x in X}) for i in range(d)]
    def env(i, j):
        m = {}
        for x in X: m[x[j]] = max(m.get(x[j], -10**9), x[i])
        b, o = -10**9, {}
        for t in sorted(m): b = max(b, m[t]); o[t] = b
        return o
    phi = {(i,j): env(i,j) for i in range(d) for j in range(d) if i != j}
    return {x for x in product(*vals)
            if all(x[i] <= phi[(i,j)][x[j]] for i in range(d) for j in range(d) if i != j)}

def op_S(H, config):
    """derive the STEP SET from the measured cells only — never from a walked result"""
    D = [(0,0,0,1,0), (0,0,1,0,0), (1,1,0,0,0), (0,1,0,0,0), (0,0,0,0,1)]
    NAMES = ["multiplicity", "ℓ", "isoelectronic", "charge", "—"]
    out = {}
    for name, dv in zip(NAMES[:4], D[:4]):
        r = []
        for (Z,c,l,S), v in H.items():
            t = (Z+dv[0], c+dv[1], l+dv[2], S+2*dv[3] if dv[3] else S)
            if t in H and abs(v) > 1e-3 and abs(H[t]) > 1e-3:
                r.append(H[t]/v)
        if len(r) < 8: continue
        lg = [math.log(abs(x)) for x in r if x > 0]
        if len(lg) < 8: continue
        out[name] = (math.exp(st.median(lg)), math.exp(st.pstdev(lg)), len(lg), dv)
    return out

def op_W(H, S, config, tau, inreg):
    """VALUATION: every cell reachable from a valued one by steps in S, least error first"""
    val = {k: (v, 1.0) for k, v in H.items()}
    q = deque(sorted(H))
    while q:
        k = q.popleft()
        v0, e0 = val[k]
        for name, (f, sc, n, dv) in S.items():
            for sgn in (1, -1):
                t = (k[0]+sgn*dv[0], k[1]+sgn*dv[1], k[2]+sgn*dv[2],
                     k[3]+2*sgn if dv[3] else k[3])
                if t[0] < 1 or t[1] < 1 or t[2] < 0 or t[3] < 0: continue
                if t[1] > t[0] or not inreg(t[0], t[1], t[2], config): continue
                e = e0*sc
                if e > tau: continue
                nv = v0*(f if sgn > 0 else 1/f)
                if t not in val or e < val[t][1]:
                    val[t] = (nv, e); q.append(t)
    return val

def run():
    config, mults, H = load()
    Hin = {k: v for k, v in H.items() if region(k[0], k[1], k[2], config)}
    S = op_S(Hin, config)
    R = op_R(set(Hin))
    W = op_W(Hin, S, config, 1.5, region)
    return config, H, Hin, S, R, W

with State("method_region") as s:
    config, H, Hin, S, R, W = step(s, "run S, R and W on the in-region index",
                                   run, budget=1200)

print("  THE METHOD EQUATION ON Λ_spectra, IN-REGION\n")
print(f"      |X| = {len(Hin)} measured channels inside verified+possible\n")
print("  S — THE STEP SET, derived from the measured cells only\n")
print(f"      {'direction':<18}{'factor':>9}{'scatter':>10}{'pairs':>8}")
for k, (f, sc, n, dv) in sorted(S.items(), key=lambda x: x[1][1]):
    print(f"      {k:<18}{f:>9.4f}{sc:>10.4f}{n:>8}")
print()
print("  THE TWO DEFECTS\n")
Xs = set(Hin)
print(f"      |X|        {len(Xs):>7}")
print(f"      |ℛ(X)|     {len(R):>7}      E(X)   = {len(R)-len(Xs):>6}   ORDINAL")
print(f"      |W(X)|     {len(W):>7}      E_W(X) = {len(W)-len(Xs):>6}   METRIC")
print()
print("  AND THE FOUR QUADRANTS — where placement and valuation agree and differ\n")
Rs = R; Ws = set(W)
q1 = len(Rs & Ws - Xs); q2 = len((Rs - Ws) - Xs); q3 = len((Ws - Rs) - Xs)
print(f"      {'quadrant':<44}{'cells':>8}")
print(f"      {'held — measured':<44}{len(Xs):>8}")
print(f"      {'ℛ admits AND W reaches — placed and valued':<44}{q1:>8}")
print(f"      {'ℛ admits, W cannot reach — a CAPTURE':<44}{q2:>8}")
print(f"      {'W reaches, ℛ excludes — EXTRAPOLATION':<44}{q3:>8}")
print()
print("  WHERE THE CAPTURES ARE — the cells ℛ places and no step values\n")
gap = sorted((Rs - Ws) - Xs)
if gap:
    byl = defaultdict(int); byc = defaultdict(int)
    for Z, c, l, Sm in gap: byl[l] += 1; byc[c] += 1
    print("      by ℓ     : " + "  ".join(f"{'spdfghik'[l]}:{byl[l]}" for l in sorted(byl)))
    print("      by charge: " + "  ".join(f"{c}:{byc[c]}" for c in sorted(byc)))
else:
    print("      none — every placed cell is reachable by some step")
