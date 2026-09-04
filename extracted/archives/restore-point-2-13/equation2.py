#!/usr/bin/env python3
"""equation2.py -- the channel equation with the charge exponent measured.

Two corrections came out of the mercury-core capture (Tl II, Pb III, Bi IV at
Ne = 80, charges 2, 3, 4, sigma(delta) = 0.008):

    1  the charge dependence is NOT ln(c+1)/c. Fitting delta ~ c^(-x) within each
       isoelectronic sequence, x falls monotonically with electron count: about
       0.7 at helium-like, 0.47 at Ne = 12, 0.31 at 19, 0.21 at 37, and 0.141
       measured directly at 80. r^2 = 0.68 against ln Ne over nineteen sequences.

       ln(c+1)/c is stiff: over c = 1 to 4 it falls as c^(-0.39). That is why it
       fitted the light sequences at r^2 = 0.999 and the krypton sequence at 0.61.
       It was never general -- it is c^(-0.4), and 0.4 is the value of x near
       Ne = 13.

    2  the ion's ground configuration is not the neutral's at the same electron
       count. Tl II's core is 5d10 6s, and aufbau at 79 electrons gives
       [Xe]4f14 5d9 -- no 6s at all, so n_out comes out 5 instead of 6 and the
       channel is classed regime 1 when it is regime 2.

THE FORM

    delta = A(regime) * sqrt(p) * Ne^k * c^(-x(Ne))

with x(Ne) = x0 + x1 ln Ne, and A carrying the regime and its boundaries.
"""
import math
import numpy as np
from scipy.optimize import curve_fit
from collections import Counter

ORDER = [(1,0),(2,0),(2,1),(3,0),(3,1),(4,0),(3,2),(4,1),(5,0),(4,2),(5,1),(6,0),
         (4,3),(5,2),(6,1),(7,0),(5,3),(6,2),(7,1),(8,0)]
HYD = sorted(ORDER, key=lambda t: (t[0], t[1]))
OPEN = {}; _z = 0
for _n, _l in ORDER: OPEN[(_n,_l)] = _z+1; _z += 2*(2*_l+1)
L = "spdfg"

def build(ne, order):
    left, out = ne, []
    for n, l in order:
        if left <= 0: break
        cap = 2*(2*l+1); o = min(left, cap); out.append((n,l,o)); left -= o
    return out
def cfg_c(ne, c): return build(ne, ORDER if c <= 2 else HYD)
def cp(ne, l, c): return sum(1 for n, ll, o in cfg_c(ne, c) if ll == l and o > 0)
def out_(ne, c):
    z = cfg_c(ne, c); return z[-1] if z else (0,0,0)
def n0_(ne, l, c): return cp(ne, l, c) + l + 1
def thr_(ne, l, c): return OPEN.get((n0_(ne, l, c), l), 9999)
def regime(Z, c, l):
    ne = Z-c+1; p = cp(ne-1,l,c)
    if p >= 1: return 1 if n0_(ne-1,l,c) > out_(ne-1,c)[0] else 2
    return 3 if Z < thr_(ne-1,l,c) else 4
def near24(Z, c, l):
    ne = Z-c+1
    if regime(Z,c,l) != 2: return 0.0
    if n0_(ne-1,l,c) >= out_(ne-1,c)[0]: return 0.0
    T = thr_(ne-1,l,c)
    return 0.5*(1+math.tanh(0.5*max(-60., min(60., (Z-T+1.5)/0.40))))

def load():
    ns = {}
    exec(open("aufbau.py", encoding="utf-8").read().split("with State(")[0]
         .replace("from zeno import State, step", ""), ns)
    return dict(ns["measured"]())
H = load()
H.update({
 (22,4,0,2):1.4153,(22,4,1,2):1.1506,(22,4,2,2):0.6202,(22,4,3,2):0.0774,
 (20,4,0,2):1.3280,(20,4,1,2):1.0703,(19,3,0,2):1.6589,(19,3,1,2):1.2110,
 (37,1,0,2):3.1357,(37,1,1,2):2.6566,(37,1,2,2):1.3307,(37,1,3,2):0.0143,
 (38,2,0,2):2.7115,(38,2,1,2):2.3636,(38,2,2,2):1.4592,(38,2,3,2):0.0610,
 (38,2,4,2):0.0092,
 (39,3,0,2):2.4462,(39,3,1,2):2.1216,(39,3,2,2):1.3965,(39,3,3,2):0.1466,
 (39,3,4,2):0.0150,(39,3,5,2):0.0042,
 # the mercury-core sequence: 5d10 6s core, p = 4, regime 2
 (81,2,1,2):3.7167,(82,3,1,2):3.5402,(83,4,1,2):3.3684})

def parents(cfg):
    if not cfg: return 1
    n, l, occ = cfg[-1]; cap = 2*(2*l+1)
    return 1 if occ in (0,cap,1,cap-1) else {0:1,1:3,2:16,3:119}.get(l,8)

# THE OBSERVED GROUND CONFIGURATIONS, where aufbau differs from reality.
# Keyed by ELECTRON COUNT, since that is what fixes the configuration for a
# neutral and for the low charges where Madelung ordering still holds. The
# value is the principal number of the outermost occupied subshell.
#
# Aufbau fills 4f before 5d and 5d before 6s, so at 70 electrons it returns
# [Xe]4f14 with n_out = 4. Ytterbium is [Xe]4f14 6s2 with n_out = 6. The same
# error runs through the whole lanthanide and actinide range, and through the
# post-transition metals where aufbau leaves the ns shell unfilled.
NOUT = {}
for _ne, _n in [
    # the lanthanides: 4f fills but 6s2 is already there
    (57,6),(58,6),(59,6),(60,6),(61,6),(62,6),(63,6),(64,6),(65,6),(66,6),
    (67,6),(68,6),(69,6),(70,6),(71,6),
    # the 5d series: 6s2 outside
    (72,6),(73,6),(74,6),(75,6),(76,6),(77,6),(78,6),(79,6),(80,6),
    # post-transition: 6s and 6p
    (81,6),(82,6),(83,6),
    # the actinides: 7s2 outside 5f
    (89,7),(90,7),(91,7),(92,7),(93,7),(94,7),(95,7),(96,7),(97,7),(98,7),
    (99,7),(100,7),(101,7),(102,7),(103,7),
    # the 4d series: 5s outside 4d
    (39,5),(40,5),(41,5),(42,5),(43,5),(44,5),(45,5),(46,5),(47,5),(48,5),
    # the 3d series: 4s outside 3d
    (21,4),(22,4),(23,4),(24,4),(25,4),(26,4),(27,4),(28,4),(29,4),(30,4)]:
    NOUT[_ne] = _n

def real_nout(ne_core, c):
    """the outermost principal number of the core's ground configuration.
    Uses the observed value where aufbau is known to differ; otherwise aufbau."""
    if c <= 2 and ne_core in NOUT: return NOUT[ne_core]
    return out_(ne_core, c)[0]

FIX = {}

ROWS = []
for (Z, c, l, S), d in H.items():
    ne = Z-c+1
    if Z > 92 or c > 10 or l > 5: continue
    if parents(cfg_c(ne-1, c)) > 1: continue
    non = real_nout(ne-1, c)
    p = cp(ne-1, l, c); n0 = n0_(ne-1, l, c)
    rg = (1 if (p >= 1 and n0 > non) else 2 if p >= 1 else
          3 if Z < thr_(ne-1,l,c) else 4)
    ROWS.append(dict(Z=Z, c=c, l=l, d=d, ne=ne, p=p, n0=n0, non=non,
                     T=thr_(ne-1,l,c), reg=rg, b24=near24(Z,c,l)))

print(f"  {len(ROWS)} channels")
print("      " + " · ".join(f"regime {k}: {v}"
      for k, v in sorted(Counter(r["reg"] for r in ROWS).items())) + "\n")

A_ = lambda rows, k: np.array([r[k] for r in rows], float)
G = {r_: [x for x in ROWS if x["reg"] == r_] for r_ in (1,2,3,4)}
OUTR = G[3]+G[4]
P1,N1,C1 = A_(G[1],"p"),A_(G[1],"ne"),A_(G[1],"c"); D1 = A_(G[1],"n0")-A_(G[1],"non")
P2,N2,C2 = A_(G[2],"p"),A_(G[2],"ne"),A_(G[2],"c"); B2 = A_(G[2],"b24")
Zo,To,No,Co,Lo = (A_(OUTR,"Z"),A_(OUTR,"T"),A_(OUTR,"ne"),A_(OUTR,"c"),A_(OUTR,"l"))
Y1 = np.array([r["d"] for r in G[1]]); Y2 = np.array([r["d"] for r in G[2]])
Yo = np.array([r["d"] for r in OUTR])
Do = Zo-To
YA = np.concatenate([Y1, Y2, Yo])
HTAB = {2:0.40, 3:0.468, 4:0.468*math.sqrt(20/12)}
HL = np.array([HTAB.get(int(l), 0.40) for l in Lo])
def sig(x): return 0.5*(1+np.tanh(0.5*np.clip(x,-60,60)))

def chg(C, N, x0, x1):
    x = np.maximum(x0 + x1*np.log(np.maximum(N,2)), 0.02)
    return C**(-x)

def M(_, a, q, a2, b, k, x0, x1):
    return np.concatenate([
      (a+q*D1)*np.sqrt(np.maximum(P1,1e-9))*N1**k*chg(C1,N1,x0,x1),
      a2*(1+b*B2)*np.sqrt(np.maximum(P2,1e-9))*N2**k*chg(C2,N2,x0,x1),
      HL*sig((Do+1.5)/0.40)*((No-1)/No)*No**k*chg(Co,No,x0,x1)])

best = None
for p0 in ([0.35,-0.035,0.36,0.20,0.45,0.86,-0.18],
           [0.3,-0.03,0.3,0.2,0.5,0.8,-0.15],
           [0.4,-0.04,0.4,0.25,0.42,0.9,-0.2]):
    try:
        pr, _ = curve_fit(M, np.arange(len(YA)), YA, p0=p0, maxfev=900000)
        r = YA-M(None,*pr); s = float(np.sqrt(np.mean(r**2)))
        if best is None or s < best[1]: best = (pr, s)
    except Exception: pass
pr, s = best; r = YA-M(None,*pr); a,q,a2,b,k,x0,x1 = pr
print("  THE EQUATION\n")
print("      δ = A · √p · Nₑ^k · c^(−x(Nₑ))        x(Nₑ) = x₀ + x₁·ln Nₑ\n")
print(f"      regime 1   A = a + q·(n₀−n_out)          a = {a:.4f}   q = {q:+.4f}")
print(f"      regime 2   A = a₂·(1 + b·Σ)              a₂ = {a2:.4f}  b = {b:+.4f}")
print(f"      regime 3/4 A = h(ℓ)·Σ·(Nₑ−1)/Nₑ         h(d)=0.40 measured, "
      f"h(f)=0.468 from ⟨r⟩")
print(f"      k = {k:.4f}   x(Nₑ) = {x0:.4f} {x1:+.4f}·ln Nₑ\n")
for n_ in (12, 20, 40, 80):
    print(f"          x({n_:>3}) = {max(x0+x1*math.log(n_),0.02):.3f}")
print(f"\n      {len(ROWS)} channels · rms {s:.4f} · R² {1-np.var(r)/np.var(YA):.4f}")
np.save("/tmp/eq2.npy", pr)

def delta(Z, c, l):
    ne = Z-c+1; p = cp(ne-1,l,c)
    non = real_nout(ne-1, c)
    n0 = n0_(ne-1,l,c)
    t = c**(-max(x0+x1*math.log(max(ne,2)), 0.02))
    rg = (1 if (p>=1 and n0>non) else 2 if p>=1 else
          3 if Z < thr_(ne-1,l,c) else 4)
    if rg == 1: return (a+q*(n0-non))*math.sqrt(p)*ne**k*t
    if rg == 2: return a2*(1+b*near24(Z,c,l))*math.sqrt(p)*ne**k*t
    T = thr_(ne-1,l,c); xx = max(-60., min(60., (Z-T+1.5)/0.40))
    return HTAB.get(l,0.40)*sig(xx)*((ne-1)/ne)*ne**k*t

def cap(l): return 2*(2*l+1)
def occ(cfg, n, l):
    for X, Yl, O in cfg:
        if X == n and Yl == l: return O
    return 0
ok = bad = 0; BAD = []
for Z in range(3, 104):
    ne = Z; c1 = cfg_c(ne-1,1); full = cfg_c(ne,1)
    cand = []
    for n, l in ORDER:
        if l > 4 or n > 8: continue
        if occ(c1,n,l) >= cap(l): continue
        if n != cp(ne-1,l,1)+l+1 and occ(c1,n,l) == 0: continue
        cand.append((n, l, n-delta(Z,1,l)))
    if len(cand) < 2: continue
    got = None
    for n, l in ORDER:
        if occ(full,n,l) > occ(c1,n,l): got = (n,l); break
    if got is None: continue
    pick = min(cand, key=lambda x: x[2])
    if (pick[0], pick[1]) == got: ok += 1
    else: bad += 1; BAD.append((Z, got, pick))
print(f"\n      FILLING ORDER: {ok} of {ok+bad} ({100*ok/(ok+bad):.1f}%)")
if BAD:
    print("      failures: " + "  ".join(
        f"Z{Z}:{gt[0]}{L[gt[1]]}→{pk[0]}{L[pk[1]]}" for Z, gt, pk in BAD))
wz = max(abs(delta(Z,Z,l)) for Z in (1,2,8,26,56,90) for l in range(4))
badp = sum(1 for r_ in ROWS if math.floor(delta(r_["Z"],r_["c"],r_["l"])) >
           min(r_["p"], n0_(r_["ne"]-1,r_["l"],r_["c"])-r_["l"]-1))
print(f"      hydrogenic {wz:.6f} · Pauli {len(ROWS)-badp}/{len(ROWS)}")
