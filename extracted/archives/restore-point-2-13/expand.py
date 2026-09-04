#!/usr/bin/env python3
"""expand.py -- take P.trunc, P.lens and P.termsplit from single digits to scale.

Register 826. Three mechanisms sit at 100% on four instances or fewer, and all three
can be tested on data already collected. Each becomes a measurement rather than an
anecdote.

    P.TRUNC     truncation removes most channels, not a proportional share.
                Testable by SIMULATION: truncate every species at n <= 8 and count
                what survives. No new data needed; the counterfactual is computable.

    P.LENS      near the limit the defect is measured through a worsening lens.
                Testable on every channel with six or more members: split into a low-n
                and a high-n half and compare the spread. The claim predicts the high
                half is wider, and by roughly (n_hi/n_lo)^3.

    P.TERMSPLIT at l=3 the defect splits by the core's TERM while J-pairs stay together.
                Testable wherever one species has two or more terms at one l with J
                resolved: the within-term spread should be smaller than the between-term
                spread.

Zeno phases: fetch once, then three independent analyses over the same fetch.
"""
import re, math, glob, os, statistics as st
from collections import defaultdict
from zeno import State, step

R = 109737.31568

def limits():
    src = open("channels.py", encoding="utf-8").read()
    i = src.index("LIM = {"); depth = 0; j = i + 6
    while True:
        if src[j] == "{": depth += 1
        elif src[j] == "}":
            depth -= 1
            if depth == 0: break
        j += 1
    return eval(src[i+6:j+1])

def fetch():
    LIM = limits(); out = {}
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
            ser[(nm, mm.group(1), mm.group(3), p[1], p[2])].append((int(mm.group(2)), E))
        for k, v in ser.items(): out[k] = (sorted(set(v)), lim, Z)
    return out

# ------------------------------------------------------------------- P.TRUNC
def trunc(raw, cut=8):
    """how many channels survive if every series is cut at n <= cut"""
    by = defaultdict(lambda: [0, 0])       # species -> [full, truncated]
    for k, (v, lim, Z) in raw.items():
        if len(v) >= 3: by[k[0]][0] += 1
        if len([x for x in v if x[0] <= cut]) >= 3: by[k[0]][1] += 1
    out = []
    for sp, (full, tr) in by.items():
        if full == 0: continue
        out.append((sp, full, tr, tr/full))
    return out

# -------------------------------------------------------------------- P.LENS
def lens(raw):
    """does the spread grow toward the limit within one channel?"""
    out = []
    for k, (v, lim, Z) in raw.items():
        if len(v) < 6: continue
        d = [n - Z*math.sqrt(R/(lim-E)) for n, E in v]
        h = len(d)//2
        lo, hi = st.pstdev(d[:h]), st.pstdev(d[h:])
        if lo <= 0: continue
        out.append((k, lo, hi, hi/lo, v[0][0], v[-1][0]))
    return out

# --------------------------------------------------------------- P.TERMSPLIT
def termsplit(raw):
    """within-term spread against between-term spread, at one species and l"""
    grp = defaultdict(lambda: defaultdict(list))
    for k, (v, lim, Z) in raw.items():
        if len(v) < 3: continue
        d = st.mean([n - Z*math.sqrt(R/(lim-E)) for n, E in v])
        grp[(k[0], k[1], k[2])][k[3]].append((k[4], d))     # term -> [(J, delta)]
    out = []
    for key, terms in grp.items():
        if len(terms) < 2: continue
        within = [max(x[1] for x in v) - min(x[1] for x in v)
                  for v in terms.values() if len(v) > 1]
        means = [st.mean([x[1] for x in v]) for v in terms.values()]
        between = max(means) - min(means)
        if not within: continue
        out.append((key, st.mean(within), between, len(terms)))
    return out

def wilson(k, n, z=1.96):
    if n == 0: return (0.0, 1.0)
    p = k/n; dd = 1 + z*z/n
    c = (p + z*z/(2*n))/dd
    h = z*math.sqrt(p*(1-p)/n + z*z/(4*n*n))/dd
    return (max(0.0, c-h), min(1.0, c+h))

with State("expand") as s:
    raw = step(s, "fetch every series once", fetch, budget=300)
    T   = step(s, "P.trunc by simulated truncation", lambda: trunc(raw),     budget=300)
    L   = step(s, "P.lens by half-split spread",     lambda: lens(raw),      budget=300)
    S   = step(s, "P.termsplit by within vs between", lambda: termsplit(raw), budget=300)

print(f"  P.TRUNC — every species cut at n <= 8, channels counted\n")
k = sum(1 for _, f, t, r in T if r < 0.5)
lo, hi = wilson(k, len(T))
print(f"  {'species':<16}{'full':>6}{'cut':>6}{'kept':>8}")
for sp, f, t, r in sorted(T, key=lambda x: x[3])[:10]:
    print(f"  {sp:<16}{f:>6}{t:>6}{100*r:>7.0f}%")
print(f"\n  {k} of {len(T)} species lose MORE THAN HALF their channels — "
      f"{100*k/len(T):.0f}%, interval {100*lo:.0f}-{100*hi:.0f}%")
tot_f = sum(f for _, f, _, _ in T); tot_t = sum(t for _, _, t, _ in T)
print(f"  overall: {tot_f} channels become {tot_t} — {100*tot_t/tot_f:.0f}% survive a cut at n=8")

print(f"\n  P.LENS — spread in the high-n half against the low-n half\n")
k = sum(1 for _, lo_, hi_, r, *_ in L if r > 1)
w = wilson(k, len(L))
print(f"  {k} of {len(L)} channels have a WIDER spread in the high half — "
      f"{100*k/len(L):.0f}%, interval {100*w[0]:.0f}-{100*w[1]:.0f}%")
print(f"  median ratio high/low: {st.median([r for *_, r, _, _ in L]):.2f}")

print(f"\n  P.TERMSPLIT — within-term spread against between-term spread\n")
k = sum(1 for _, wi, be, _ in S if be > wi)
w = wilson(k, len(S))
print(f"  {k} of {len(S)} groups have terms separating by MORE than their J-pairs do — "
      f"{100*k/len(S):.0f}%, interval {100*w[0]:.0f}-{100*w[1]:.0f}%")
print(f"  median within {st.median([x[1] for x in S]):.4f} · "
      f"median between {st.median([x[2] for x in S]):.4f}")
