#!/usr/bin/env python3
"""whatis.py -- what is the channel equation actually describing?

Register 1175. The equation fits 311 channels at rms 0.244 and R^2 0.924, and fails the
index's own defences: 6 hydrogenic violations, 21 exchange, 49 l-ordering, against 5 for
the measured data. It gets magnitudes right and orderings wrong. So it may be describing
a DIFFERENT QUANTITY that correlates with delta.

Run in Zeno phases, each closed before the next opens, each checkpointed. A timeout costs
one phase, not the run.

    PHASE 1  the exchange signature   does it describe an exchange-free atom?
    PHASE 2  the n signature          does it describe delta at some finite n?
    PHASE 3  the term signature       does it describe the term-averaged defect?
    PHASE 4  the hydrogenic signature what does it say where the answer is known exactly?
    PHASE 5  the verdict              which hypothesis survives all four

Each phase states in advance what would confirm and what would refute, so that a null
result is a result and not an absence.
"""
import json, math, re, statistics as st
import numpy as np
from collections import defaultdict
from zeno import State, step

# ------------------------------------------------------------------ shared setup
def setup():
    ns = {}
    exec(open("alpha.py", encoding="utf-8").read().split("with State(")[0]
         .replace("from zeno import State, step", ""), ns)
    exec(open("aufbau.py", encoding="utf-8").read().split("with State(")[0]
         .replace("from zeno import State, step", ""), ns)
    AL = ns["measured_alpha"]()
    for k, (a, src) in ns["PUB"].items(): AL[k] = a
    pr = np.load("/tmp/final2.npy")
    LM = {"s":0,"p":1,"d":2,"f":3,"g":4,"h":5,"i":6,"k":7}
    ROM = {"I":1,"II":2,"III":3,"IV":4,"V":5,"VI":6,"IX":9,"XI":11,"XV":15,"XVI":16}
    SUP = str.maketrans("⁰¹²³⁴⁵⁶⁷⁸⁹","0123456789")
    ZN = ns["ZN"]; config = ns["config"]
    RZ = {}
    for nm, orb, term, Zc, d0, d2, r0, r1, n in json.load(open("RITZ.json")):
        if orb not in LM: continue
        p = nm.split(); el = p[0]
        if el not in ZN: continue
        c = ROM.get(p[-1], 1) if len(p) > 1 else 1
        mu = re.search(r"(\d)[SPDFG]", term.translate(SUP))
        RZ[(ZN[el], c, LM[orb], int(mu.group(1)) if mu else 0)] = (d0, d2)
    H = ns["measured"]()
    return dict(AL=AL, pr=pr, RZ=RZ, H=H, config=config, ZN=ZN)

def make_delta(S):
    AL, pr, config = S["AL"], S["pr"], S["config"]
    q, a0, a1, g, k_, C, s3 = pr
    def corb(ne, l): return sum(1 for n, ll, occ in config(ne) if ll == l and occ > 0)
    def n0f(ne, l):
        v = [n for n, ll, occ in config(ne) if ll == l and occ > 0]
        return (max(v)+1) if v else l+1
    def Kf(l): return l*(l+1)*(2*l-1)*(2*l+1)*(2*l+3) if l >= 1 else 1.0
    def delta(Z, c, l, mult):
        ne = Z-c+1
        B = min(corb(ne-1, l), n0f(ne-1, l)-l-1)
        a = max(a0 + a1*ne**(-1/3), 0.05)
        pen = -q*math.exp(-a*l)*math.exp(k_/ne)*c**g
        pol = 0.0
        if l >= 4:
            al = AL.get((Z, c))
            pol = 3.0*al*c*c/Kf(l) if al is not None else C*c*c/Kf(l)
        return (B + pen + pol)*(1 + s3*(mult == 3))
    return delta, corb, n0f

# ------------------------------------------------------------------ the phases
def phase1(S):
    """EXCHANGE. A one-electron model potential has no exchange, so its singlet and
    triplet coincide. CONFIRMS the model-potential reading if the equation's gap is
    near zero where the measured gap is not. REFUTES it if the gaps match."""
    delta, _, _ = make_delta(S); RZ = S["RZ"]
    pairs = [(k, (k[0],k[1],k[2],3)) for k in RZ if k[3] == 1 and (k[0],k[1],k[2],3) in RZ]
    dm = [abs(RZ[a][0]-RZ[b][0]) for a, b in pairs]
    de = [abs(delta(*a)-delta(*b)) for a, b in pairs]
    return dict(n=len(pairs),
                measured=st.median(dm) if dm else 0,
                equation=st.median(de) if de else 0,
                ratio=(st.median(de)/st.median(dm)) if dm and st.median(dm) else float("nan"))

def phase2(S):
    """THE n SIGNATURE. If the equation describes delta at a finite n, the residual
    against delta(n) has a clear minimum there. CONFIRMS if the minimum is sharp and
    at small n. REFUTES if the curve is flat above n ~ 6."""
    delta, _, _ = make_delta(S); RZ = S["RZ"]
    out = []
    for n in list(range(2, 31)) + [40, 60, 100]:
        r = []
        for k, (d0, d2) in RZ.items():
            if n - d0 <= 0.5: continue
            r.append(delta(*k) - (d0 + d2/(n-d0)**2))
        if len(r) < 50: continue
        out.append((n, float(np.sqrt(np.mean(np.square(r)))), len(r)))
    r0 = [delta(*k) - RZ[k][0] for k in RZ]
    best = min(out, key=lambda x: x[1])
    flat = max(x[1] for x in out if x[0] >= 8) - min(x[1] for x in out if x[0] >= 8)
    return dict(curve=out, best=best, limit=float(np.sqrt(np.mean(np.square(r0)))),
                spread_above_8=flat)

def phase3(S):
    """THE TERM SIGNATURE. If the equation describes a term-AVERAGED defect it should
    fit the average better than the resolved value. CONFIRMS if the averaged rms is
    materially lower. REFUTES if they are within noise of each other."""
    delta, _, _ = make_delta(S); RZ = S["RZ"]
    byLS = defaultdict(list)
    for (Z,c,l,Sm), (d0,d2) in RZ.items(): byLS[(Z,c,l)].append(d0)
    ra, rr = [], []
    for (Z,c,l), v in byLS.items():
        if len(v) < 2: continue
        m = st.mean(v)
        for Sm in (1, 3):
            if (Z,c,l,Sm) in RZ:
                ra.append(delta(Z,c,l,Sm) - m)
                rr.append(delta(Z,c,l,Sm) - RZ[(Z,c,l,Sm)][0])
    f = lambda x: float(np.sqrt(np.mean(np.square(x)))) if x else float("nan")
    return dict(n=len(ra), averaged=f(ra), resolved=f(rr))

def phase4(S):
    """THE HYDROGENIC SIGNATURE. At Ne = 1 there is no core and delta = 0 exactly, by
    symmetry, for every l. This is the one place the true answer is known with no
    measurement. Whatever the equation returns there names what it thinks a cell is."""
    delta, corb, n0f = make_delta(S)
    rows = []
    for Z in (1, 2, 3, 5, 8, 12, 20, 26, 56):
        c = Z                                  # one electron
        for l in range(5):
            B = min(corb(0, l), n0f(0, l)-l-1)
            rows.append((Z, c, l, delta(Z, c, l, 2), B))
    return rows

with State("whatis") as s:
    S  = step(s, "phase 0 — load the equation, the Ritz curves and the index", setup, budget=300)
    P1 = step(s, "phase 1 — the exchange signature",   lambda: phase1(S), budget=200)
    P2 = step(s, "phase 2 — the n signature",          lambda: phase2(S), budget=400)
    P3 = step(s, "phase 3 — the term signature",       lambda: phase3(S), budget=200)
    P4 = step(s, "phase 4 — the hydrogenic signature", lambda: phase4(S), budget=200)

print("  WHAT IS THE EQUATION DESCRIBING?\n")
print("  PHASE 1 — THE EXCHANGE SIGNATURE\n")
print(f"      {P1['n']} singlet/triplet pairs")
print(f"      measured gap  {P1['measured']:.4f}")
print(f"      equation gap  {P1['equation']:.4f}")
print(f"      ratio         {P1['ratio']:.2f}")
print(f"      → the equation carries {100*P1['ratio']:.0f}% of the real exchange splitting\n")

print("  PHASE 2 — THE n SIGNATURE\n")
print(f"      {'n':>5}{'rms':>10}")
for n, r, k in P2["curve"]:
    if n in (2,3,4,5,6,8,10,15,20,30,60,100): print(f"      {n:>5}{r:>10.4f}")
print(f"\n      best      n = {P2['best'][0]}, rms {P2['best'][1]:.4f}")
print(f"      the limit δ₀      rms {P2['limit']:.4f}")
print(f"      spread above n=8  {P2['spread_above_8']:.5f}\n")

print("  PHASE 3 — THE TERM SIGNATURE\n")
print(f"      {P3['n']} channels in multi-term groups")
print(f"      against the term-AVERAGED δ₀  rms {P3['averaged']:.4f}")
print(f"      against the term-RESOLVED δ₀  rms {P3['resolved']:.4f}\n")

print("  PHASE 4 — THE HYDROGENIC SIGNATURE\n")
print(f"      {'ion':<10}{'ℓ':>3}{'B':>4}{'the equation':>15}{'the truth':>11}")
for Z, c, l, v, B in P4:
    if l <= 2:
        print(f"      {'Z='+str(Z)+', c='+str(c):<10}{'spdfg'[l]:>3}{B:>4}{v:>15.4f}{0.0:>11.1f}")
