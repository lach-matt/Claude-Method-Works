#!/usr/bin/env python3
"""shellsum.py -- the defect as a sum over EVERY shell, occupied or not.

The equation has been summarising the core into three numbers -- p, n_out, l_core --
standing in for up to nine subshells. That is why it fails at the four block
openings: at Z = 21, 39, 57, 89 the incoming orbital is a PLACE that exists before
it is occupied, and a summary of the occupied shells cannot see it.

So write the defect as a sum with one term per subshell:

    delta(Z, c, l) = sum over (n', l') of  W(n', l', o')  *  scale(Ne, c)

Each subshell contributes according to how much of the Rydberg orbital's inner
region it occupies. Three regimes, and each is a statement rather than a fit:

    SAME l, occupied     the Rydberg function must carry an extra node to stay
                         orthogonal. Contributes ~1 -- this is floor(delta) = p.

    LOWER l, occupied    the Rydberg electron passes through this shell but is
                         not orthogonal to it. Contributes a fraction, falling
                         with how far the shells are separated in n.

    HIGHER l, or EMPTY   contributes nothing directly, BUT an empty shell of the
                         same l is the inner well the orbital collapses into, so
                         its presence sets where collapse happens.

The point of the sum is that the last case is now a TERM rather than a threshold
lookup: the shell is in the sum whether or not it holds electrons.
"""
import math
import numpy as np
from scipy.optimize import curve_fit

ORDER = [(1,0),(2,0),(2,1),(3,0),(3,1),(4,0),(3,2),(4,1),(5,0),(4,2),(5,1),(6,0),
         (4,3),(5,2),(6,1),(7,0),(5,3),(6,2),(7,1),(8,0)]
HYD = sorted(ORDER, key=lambda t: (t[0], t[1]))
OPEN = {}; _z = 0
for _n, _l in ORDER: OPEN[(_n,_l)] = _z+1; _z += 2*(2*_l+1)

def build(ne, order):
    left, out = ne, []
    for n, l in order:
        if left <= 0: break
        cap = 2*(2*l+1); o = min(left, cap); out.append((n,l,o)); left -= o
    return out

def cfg_c(ne, c): return build(ne, ORDER if c <= 2 else HYD)

def load():
    ns = {}
    exec(open("aufbau.py", encoding="utf-8").read().split("with State(")[0]
         .replace("from zeno import State, step", ""), ns)
    return dict(ns["measured"]())

H = load()
H.update({
 (22,4,0,2):1.4153,(22,4,1,2):1.1506,(22,4,2,2):0.6202,(22,4,3,2):0.0774,
 (20,4,0,2):1.3280,(20,4,1,2):1.0703,(20,4,2,2):0.5526,(19,3,0,2):1.6589,
 (19,3,1,2):1.2110,
 (37,1,0,2):3.1357,(37,1,1,2):2.6566,(37,1,2,2):1.3307,(37,1,3,2):0.0143,
 (38,2,0,2):2.7115,(38,2,1,2):2.3636,(38,2,2,2):1.4592,(38,2,3,2):0.0610,
 (38,2,4,2):0.0092,
 (39,3,0,2):2.4462,(39,3,1,2):2.1216,(39,3,2,2):1.3965,(39,3,3,2):0.1466,
 (39,3,4,2):0.0150,(39,3,5,2):0.0042})

def parents(cfg):
    if not cfg: return 1
    n, l, occ = cfg[-1]; cap = 2*(2*l+1)
    return 1 if occ in (0, cap, 1, cap-1) else {0:1,1:3,2:16,3:119}.get(l, 8)

# every shell the sum runs over -- ALL of them, occupied or not
SHELLS = [(n, l) for n in range(1, 8) for l in range(0, min(n, 5))]

ROWS = []
for (Z, c, l, S), d in H.items():
    ne = Z - c + 1
    if Z > 92 or c > 10 or l > 5: continue
    cfg = cfg_c(ne-1, c)
    if parents(cfg) > 1: continue
    occ = {(n_, l_): o_ for n_, l_, o_ in cfg}
    # the Rydberg orbital's own n: the first Pauli-allowed one
    same = [n_ for (n_, l_) in occ if l_ == l and occ[(n_, l_)] > 0]
    n0 = (max(same)+1) if same else l+1
    ROWS.append(dict(Z=Z, c=c, l=l, d=d, ne=ne, n0=n0,
                     occ=[occ.get(s, 0) for s in SHELLS]))

print(f"  {len(ROWS)} in-region channels · {len(SHELLS)} shells in the sum\n")

OC = np.array([r["occ"] for r in ROWS], float)          # occupancy of each shell
CAPS = np.array([2*(2*l+1) for (n, l) in SHELLS], float)
FILL = OC / CAPS                                         # fraction filled, 0 to 1
SN = np.array([n for (n, l) in SHELLS], float)
SL = np.array([l for (n, l) in SHELLS], float)
LL = np.array([r["l"] for r in ROWS], float)[:, None]
N0 = np.array([r["n0"] for r in ROWS], float)[:, None]
NE = np.array([r["ne"] for r in ROWS], float)
C  = np.array([r["c"] for r in ROWS], float)
Y  = np.array([r["d"] for r in ROWS])
T  = np.log(C+1)/C
ZZ = np.array([r["Z"] for r in ROWS], float)

DL = LL - SL[None, :]        # how far the Rydberg l is above this shell's l
DN = N0 - SN[None, :]        # how far its n is above this shell's n
SAME = (DL == 0).astype(float)
BELOW = ((DL > 0) & (DN > 0)).astype(float)
EMPTYSAME = ((DL == 0) & (FILL == 0)).astype(float)

def sig(x): return 0.5*(1+np.tanh(0.5*np.clip(x, -60, 60)))

def model(_, a, g, s, u, w, k):
    """one term per shell:
       same-l occupied   : contributes a, damped by separation in n
       lower-l occupied  : contributes g, damped by separation in n
       same-l EMPTY      : the inner well -- contributes u once Z passes it
    """
    sep = np.exp(-np.maximum(DN, 0)/max(abs(s), 1e-6))
    t1 = a * SAME * FILL * sep
    t2 = g * BELOW * FILL * sep
    t3 = u * EMPTYSAME * sig((ZZ[:, None] - np.maximum(SN, 1)*np.maximum(SL, 1)*4.0)
                             / max(abs(w), 1e-6))
    return (t1+t2+t3).sum(axis=1) * NE**k * T

best = None
for p0 in ([0.4,0.1,3.0,0.5,4.0,0.47],[0.3,0.05,2.0,0.6,5.0,0.5],
           [0.5,0.2,4.0,0.4,3.0,0.45]):
    try:
        pr, _ = curve_fit(model, np.arange(len(Y)), Y, p0=p0, maxfev=900000)
        r = Y - model(None, *pr); s_ = float(np.sqrt(np.mean(r**2)))
        if best is None or s_ < best[1]: best = (pr, s_)
    except Exception: pass

if best is None:
    print("  fit failed")
else:
    pr, s_ = best; r = Y - model(None, *pr)
    print("  THE SHELL-SUM EQUATION\n")
    print("      δ = [ Σ_shells W ] · Nₑ^k · ln(c+1)/c\n")
    print(f"      a = {pr[0]:.4f}  (same ℓ, occupied)")
    print(f"      g = {pr[1]:.4f}  (lower ℓ, occupied)")
    print(f"      s = {pr[2]:.4f}  (separation damping in n)")
    print(f"      u = {pr[3]:.4f}  (same ℓ, EMPTY — the inner well)")
    print(f"      w = {pr[4]:.4f}  (collapse width)")
    print(f"      k = {pr[5]:.4f}\n")
    print(f"      {len(ROWS)} channels · rms {s_:.4f} · R² {1-np.var(r)/np.var(Y):.4f}")
    print(f"      (summary-form best: rms 0.1133 · R² 0.9803)")
    np.save("/tmp/eqshell.npy", pr)
