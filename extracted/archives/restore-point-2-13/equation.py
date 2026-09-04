#!/usr/bin/env python3
"""equation.py -- the two-ladder channel equation.

The Kr-core capture (Rb I, Sr II, Y III at Ne = 37) showed that delta RISES with
charge at d and f where the ladder demands it fall. The direction test came back at
p = 0.024: rising sequences lie entirely below their collapse threshold.

WHY d AND f ARE DIFFERENT. An l >= 2 orbital with no core orbital of the same l
faces a centrifugal barrier that splits the potential into two wells. Below its
collapse threshold it sits in the OUTER well; raising the charge pulls it toward the
inner one, so penetration -- and delta -- INCREASE. An s or p orbital has no such
barrier, no outer well, and only the ordinary screening ladder.

So there are two ladders, distinguished by whether the core already holds an orbital
of the same l:

    p >= 1   PENETRATING.   delta = B_pen * ln(c+1)/c,  B falling with screening
    p == 0   OUTER WELL.    delta set by the distance to the collapse threshold,
                            and RISING with charge

Both carry the same ln(c+1)/c charge form -- it is the isoelectronic form of Edlen
1964 -- and they differ in the sign and in what sets the amplitude.
"""
import math, json
import numpy as np
from collections import defaultdict
from scipy.optimize import curve_fit

ORDER = [(1,0),(2,0),(2,1),(3,0),(3,1),(4,0),(3,2),(4,1),(5,0),(4,2),(5,1),(6,0),
         (4,3),(5,2),(6,1),(7,0),(5,3),(6,2),(7,1),(8,0)]
OPEN = {}; _z = 0
for _n, _l in ORDER: OPEN[(_n,_l)] = _z+1; _z += 2*(2*_l+1)

def load():
    ns = {}
    exec(open("aufbau.py", encoding="utf-8").read().split("with State(")[0]
         .replace("from zeno import State, step", ""), ns)
    return ns["config"], ns["mults"], dict(ns["measured"]())

config, mults, H = load()
H.update({
 (22,4,0,2):1.4153,(22,4,1,2):1.1506,(22,4,2,2):0.6202,(22,4,3,2):0.0774,
 (20,4,0,2):1.3280,(20,4,1,2):1.0703,(20,4,2,2):0.5526,(19,3,0,2):1.6589,
 (19,3,1,2):1.2110,
 # the Kr-core sequence, this session
 (37,1,0,2):3.1357,(37,1,1,2):2.6566,(37,1,2,2):1.3307,(37,1,3,2):0.0143,
 (38,2,0,2):2.7115,(38,2,1,2):2.3636,(38,2,2,2):1.4592,(38,2,3,2):0.0610,
 (38,2,4,2):0.0092,
 (39,3,0,2):2.4462,(39,3,1,2):2.1216,(39,3,2,2):1.3965,(39,3,3,2):0.1466,
 (39,3,4,2):0.0150,(39,3,5,2):0.0042})

def core_p(ne, l): return sum(1 for n, ll, o in config(ne) if ll == l and o > 0)
def n0(ne, l):
    v = [n for n, ll, o in config(ne) if ll == l and o > 0]
    return (max(v)+1) if v else l+1
def thresh(ne, l): return OPEN.get((n0(ne, l), l), 9999)
def parents(cfg):
    if not cfg: return 1
    n, l, occ = cfg[-1]; cap = 2*(2*l+1)
    return 1 if occ in (0, cap, 1, cap-1) else {0:1,1:3,2:16,3:119}.get(l, 8)

ROWS = []
for (Z, c, l, S), d in H.items():
    ne = Z - c + 1
    if Z > 92 or c > 10 or l > 5: continue
    if parents(config(ne-1)) > 1: continue
    ROWS.append(dict(Z=Z, c=c, l=l, S=S, d=d, ne=ne, p=core_p(ne-1, l),
                     T=thresh(ne-1, l)))

PEN = [r for r in ROWS if r["p"] >= 1]
OUT = [r for r in ROWS if r["p"] == 0]
print(f"  {len(ROWS)} in-region channels · {len(PEN)} penetrating · {len(OUT)} outer-well\n")

# ------------------------------------------------------------ ladder 1
print("  LADDER 1 — PENETRATING  (the core already holds an orbital of this ℓ)\n")
P  = np.array([r["p"] for r in PEN], float)
NE = np.array([r["ne"] for r in PEN], float)
C  = np.array([r["c"] for r in PEN], float)
LL = np.array([r["l"] for r in PEN], float)
Y  = np.array([r["d"] for r in PEN])
T1 = np.log(C+1)/C

def M1(_, a, e0, e1, k):
    e = np.maximum(e0 + e1*np.log(np.maximum(NE, 2)), 0.05)
    return a * np.power(np.maximum(P, 1e-9), e) * NE**k * T1

best = None
for p0 in ([0.377,0.830,-0.090,0.494],[0.3,1.0,-0.1,0.5],[0.5,0.6,0.0,0.45]):
    try:
        pr, _ = curve_fit(M1, np.arange(len(Y)), Y, p0=p0, maxfev=600000)
        r = Y - M1(None, *pr); s = float(np.sqrt(np.mean(r**2)))
        if best is None or s < best[1]: best = (pr, s)
    except Exception: pass
PR1, rms1 = best
r = Y - M1(None, *PR1)
print(f"      δ = a·p^e(Nₑ)·Nₑ^k·ln(c+1)/c")
print(f"      a = {PR1[0]:.4f}   e(Nₑ) = {PR1[1]:.4f} {PR1[2]:+.4f}·ln Nₑ   k = {PR1[3]:.4f}")
print(f"      {len(PEN)} channels · rms {rms1:.4f} · R² {1-np.var(r)/np.var(Y):.4f}\n")

# ------------------------------------------------------------ ladder 2
print("  LADDER 2 — OUTER WELL  (no core orbital of this ℓ; a barrier, two wells)\n")
Z2 = np.array([r["Z"] for r in OUT], float)
T2 = np.array([r["T"] for r in OUT], float)
NE2= np.array([r["ne"] for r in OUT], float)
C2 = np.array([r["c"] for r in OUT], float)
L2 = np.array([r["l"] for r in OUT], float)
Y2 = np.array([r["d"] for r in OUT])
D  = Z2 - T2                       # distance to the collapse threshold
CH2 = np.log(C2+1)/C2

def sig(x):
    return 0.5*(1.0 + np.tanh(0.5*np.clip(x, -60, 60)))

def M2(_, h, w, k):
    """a logistic in the distance to threshold, gated to zero at Ne = 1.

    h is the SATURATED amplitude -- what the defect reaches once the orbital has
    fully collapsed -- and w is the width of the collapse in units of Z. With m
    absorbed into h the fit is no longer degenerate: for D << 0 the tail is
    h*exp(D/w), and only that product was determined before.
    """
    g = sig(D/max(abs(w), 1e-6))
    return h * g * ((NE2-1)/NE2) * NE2**k * CH2

best = None
for p0 in ([0.5,4.0,0.5],[1.0,2.0,0.3],[2.0,8.0,0.6],[5.0,6.0,0.5]):
    try:
        pr, _ = curve_fit(M2, np.arange(len(Y2)), Y2, p0=p0, maxfev=600000)
        rr = Y2 - M2(None, *pr); s = float(np.sqrt(np.mean(rr**2)))
        if best is None or s < best[1]: best = (pr, s)
    except Exception: pass
PR2, rms2 = best
rr = Y2 - M2(None, *PR2)
print(f"      δ = h·σ((Z−T)/w)·(Nₑ−1)/Nₑ·Nₑ^k·ln(c+1)/c     σ the logistic")
print(f"      h = {PR2[0]:.4f}   w = {PR2[1]:.4f}   k = {PR2[2]:.4f}")
print(f"      {len(OUT)} channels · rms {rms2:.4f} · R² {1-np.var(rr)/np.var(Y2):.4f}\n")

# ------------------------------------------------------------ together
print("  THE TWO TOGETHER\n")
allY = np.concatenate([Y, Y2]); allR = np.concatenate([r, rr])
print(f"      {len(ROWS)} channels · rms {float(np.sqrt(np.mean(allR**2))):.4f}"
      f" · R² {1-np.var(allR)/np.var(allY):.4f}")
print(f"      SEVEN fitted numbers — four penetrating, three outer-well\n")

def delta(Z, c, l):
    ne = Z-c+1; p = core_p(ne-1, l); t = math.log(c+1)/c
    if p >= 1:
        a, e0, e1, k = PR1
        e = max(e0 + e1*math.log(max(ne,2)), 0.05)
        return a * p**e * ne**k * t
    h, w, k = PR2
    D = Z - thresh(ne-1, l)
    x = max(-60.0, min(60.0, D/max(abs(w), 1e-6)))
    g = 0.5*(1.0 + math.tanh(0.5*x))
    return h * g * ((ne-1)/ne) * ne**k * t

np.save("/tmp/eq.npy", np.concatenate([PR1, PR2]))
print("  CHECKS\n")
w = max(abs(delta(Z, Z, l)) for Z in (1,2,8,26,56,90) for l in range(4))
print(f"      hydrogenic, δ at Nₑ = 1 : worst {w:.6f}")
bad = sum(1 for r_ in ROWS
          if math.floor(delta(r_["Z"], r_["c"], r_["l"])) >
             min(r_["p"], n0(r_["ne"]-1, r_["l"]) - r_["l"] - 1))
print(f"      Pauli bound             : {len(ROWS)-bad}/{len(ROWS)}")
