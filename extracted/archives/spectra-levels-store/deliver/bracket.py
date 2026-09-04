#!/usr/bin/env python3
"""bracket.py -- run the bracketing test on every channel, for real.

Register 796. `channels.py` wrote the bracket column as {interior}/{interior} —
passing by construction, never computed (register 782). This computes it.

THE TEST. For three consecutive members of a Rydberg series at n-1, n, n+1, the
outer two are used to predict the middle one, and the prediction is a BRACKET, not
a point. The true value either falls inside or it does not.

    from the limit and each neighbour, the quantum defect it implies:
        d(m) = m - Z sqrt(R / (limit - E(m)))
    the two neighbours give d(n-1) and d(n+1); the bracket for the middle is the
    energy range spanned by those two defects:
        E_lo = limit - Z^2 R / (n - min(d(n-1), d(n+1)))^2
        E_hi = limit - Z^2 R / (n - max(d(n-1), d(n+1)))^2
    and the test is whether the MEASURED E(n) lies in [E_lo, E_hi].

WHY THIS CAN FAIL. If the defect were exactly constant the bracket would collapse
to a point and nothing would pass. If the defect varied wildly the bracket would be
wide and everything would pass. It fails when the defect is NOT monotone across the
three — when a perturber sits between them, or when P.lens's amplification makes the
neighbours disagree in the wrong direction. On an unperturbed converging series the
middle defect lies between its neighbours' and the test passes; on a perturbed one it
does not.

The bracket is only defined for INTERIOR members — those with a measured neighbour
on each side. That is what "interior cells" has always counted.
"""
import re, math, glob, os, sys
from collections import defaultdict
from zeno import State, step

R = 109737.31568
LM = {"s":0,"p":1,"d":2,"f":3,"g":4,"h":5,"i":6,"k":7}

def load_limits():
    """Read LIM straight out of channels.py by executing only its assignment.

    Parsing it with a regex assumed the block ends with a newline and a brace; it
    closes inline, so the match failed silently and returned None. Evaluating the
    real object cannot drift from the source (register 796).
    """
    src = open("channels.py", encoding="utf-8").read()
    i = src.index("LIM = {")
    depth, j = 0, i + len("LIM = ")
    while True:
        if src[j] == "{": depth += 1
        elif src[j] == "}":
            depth -= 1
            if depth == 0: break
        j += 1
    return eval(src[i+len("LIM = "):j+1])

def run():
    LIM = load_limits()
    res = defaultdict(lambda: [0, 0, []])      # key -> [passed, tested, failures]
    for f in sorted(glob.glob("spectra_raw/*.tsv")):
        nm = os.path.basename(f)[:-4]
        if nm not in LIM: continue
        lim, Z = LIM[nm]
        ser = defaultdict(list)
        for line in open(f, encoding="utf-8"):
            if line.startswith("#") or line.startswith("config") or not line.strip(): continue
            p = line.rstrip("\n").split("\t")
            if len(p) < 4: continue
            mm = re.match(r"^(.*?)(\d+)([spdfghik])$", p[0].strip())
            if not mm: continue
            try: E = float(p[3])
            except ValueError: continue
            if E >= lim: continue
            ser[(mm.group(1), mm.group(3), p[1], p[2])].append((int(mm.group(2)), E))
        for key, v in ser.items():
            v = sorted(set(v))
            if len(v) < 3: continue
            d = {n: n - Z*math.sqrt(R/(lim-E)) for n, E in v}
            byn = dict(v)
            for i in range(1, len(v)-1):
                n = v[i][0]
                a, b = v[i-1][0], v[i+1][0]
                if a != n-1 or b != n+1: continue     # only true neighbours
                dl, dh = sorted((d[a], d[b]))
                lo = lim - Z*Z*R/(n-dl)**2
                hi = lim - Z*Z*R/(n-dh)**2
                lo, hi = min(lo, hi), max(lo, hi)
                E = byn[n]
                k = (nm, f"{key[0]}n{key[1]} {key[2]} J={key[3]}")
                res[k][1] += 1
                if lo <= E <= hi: res[k][0] += 1
                else: res[k][2].append((n, E, lo, hi))
    return dict(res)

with State("bracket") as s:
    res = step(s, "run the bracketing test on every channel", run, budget=900)

tot = sum(v[1] for v in res.values())
ok  = sum(v[0] for v in res.values())
print(f"  {len(res)} channels have three or more consecutive members")
print(f"  {tot} interior cells tested")
print(f"  {ok} pass, {tot-ok} FAIL   ({100*ok//tot if tot else 0}%)")
print()
bad = [(k, v) for k, v in res.items() if v[2]]
if bad:
    print(f"  {len(bad)} channels contain a failure:\n")
    print(f"  {'species':<14}{'series':<30}{'pass/test':>11}")
    for k, v in sorted(bad, key=lambda x: x[1][0]/max(x[1][1],1))[:14]:
        print(f"  {k[0]:<14}{k[1][:28]:<30}{f'{v[0]}/{v[1]}':>11}")
else:
    print("  no failures — which would itself be suspect (register 784)")
