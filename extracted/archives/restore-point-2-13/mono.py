#!/usr/bin/env python3
"""mono.py -- the monotonicity law, tested on every step the data can resolve.

Register 821. §25.6.1 rests on "within a channel, delta falls monotonically with n".
Register 806 got 44 of 54 — 81% — on the five species carrying quoted uncertainties,
and register 807 named what was missing: per-level uncertainties, which 44 of 49
species do not supply.

This makes the best of what exists, in Zeno phases:

    fetch     every level with whatever uncertainty its file supplies
    read      the defect and its propagated error at each level
    analyse   every ADJACENT step, classified by whether it is resolvable
    report

The resolvability cut is the whole point. A step smaller than its own error is a coin
flip and counting it dilutes the measurement toward 50%; register 805 showed Si I's
last twenty members doing exactly that. Where a file gives no uncertainty the quoted
decimals are used, and those rows are reported SEPARATELY because register 806
established that quotation understates the real error near a limit.
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

def quoted(s):
    s = s.strip().rstrip("?").strip("[]()")
    return 10**(-len(s.split(".")[1])) if "." in s else 1.0

# ---------------------------------------------------------------- PHASE: FETCH
def fetch():
    LIM = limits(); out = {}
    for f in sorted(glob.glob("spectra_raw/*.tsv")):
        nm = os.path.basename(f)[:-4]
        if nm not in LIM: continue
        lim, Z = LIM[nm]
        hdr = [l for l in open(f, encoding="utf-8") if l.startswith("config")]
        has_unc = bool(hdr) and "unc" in hdr[0]
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
            u = None
            if has_unc and len(p) > 4:
                try:
                    u = float(p[4])
                    if u <= 0: u = None
                except ValueError: u = None
            ser[(nm, mm.group(1), mm.group(3), p[1], p[2])].append(
                (int(mm.group(2)), E, u, quoted(p[3])))
        for k, v in ser.items(): out[k] = (v, lim, Z, has_unc)
    return out

# ----------------------------------------------------------------- PHASE: READ
def read(raw):
    """defect and its propagated error at every level"""
    out = {}
    for k, (v, lim, Z, has_unc) in raw.items():
        v = sorted(set(v))
        if len(v) < 2: continue
        rows = []
        for n, E, u, q in v:
            d = n - Z*math.sqrt(R/(lim-E))
            e_real = Z*math.sqrt(R)*0.5*u/(lim-E)**1.5 if u else None
            e_quot = Z*math.sqrt(R)*0.5*q/(lim-E)**1.5
            rows.append((n, d, e_real, e_quot))
        out[k] = (rows, has_unc)
    return out

# -------------------------------------------------------------- PHASE: ANALYSE
def analyse(dd):
    """every adjacent step, bucketed by resolvability and by error provenance"""
    res = defaultdict(lambda: [0, 0])
    for k, (rows, has_unc) in dd.items():
        for a, b in zip(rows, rows[1:]):
            if b[0] != a[0] + 1: continue
            step_ = abs(b[1] - a[1])
            real = a[2] is not None and b[2] is not None
            e = (math.sqrt(a[2]**2 + b[2]**2) if real
                 else math.sqrt(a[3]**2 + b[3]**2))
            if e <= 0: continue
            r = step_ / e
            src = "quoted uncertainty" if real else "decimals only"
            band = ("unresolved (<3x)" if r < 3 else
                    "resolved (3-10x)" if r < 10 else "well resolved (>10x)")
            key = (src, band)
            res[key][1] += 1
            if b[1] <= a[1]: res[key][0] += 1     # delta FELL
    return dict(res)

def wilson(k, n, z=1.96):
    if n == 0: return (0.0, 1.0)
    p = k/n; d = 1 + z*z/n
    c = (p + z*z/(2*n))/d
    h = z*math.sqrt(p*(1-p)/n + z*z/(4*n*n))/d
    return (max(0.0, c-h), min(1.0, c+h))

with State("mono") as s:
    raw = step(s, "fetch every level with its uncertainty",   fetch,             budget=300)
    dd  = step(s, "read the defect and its error",       lambda: read(raw),      budget=300)
    res = step(s, "analyse every adjacent step",         lambda: analyse(dd),    budget=300)

print(f'  §25.6.1: "within a channel, delta falls monotonically with n"\n')
print(f"  {'error from':<22}{'resolvability':<24}{'steps':>7}{'falling':>9}{'rate':>7}{'95% interval':>16}")
for src in ["quoted uncertainty", "decimals only"]:
    for band in ["unresolved (<3x)", "resolved (3-10x)", "well resolved (>10x)"]:
        k, n = res.get((src, band), [0, 0])
        if not n: continue
        lo, hi = wilson(k, n)
        print(f"  {src:<22}{band:<24}{n:>7}{k:>9}{100*k/n:>6.0f}%"
              f"{f'{100*lo:.0f}–{100*hi:.0f}%':>16}")
kk = sum(res.get(("quoted uncertainty", b), [0,0])[0] for b in ["resolved (3-10x)","well resolved (>10x)"])
nn = sum(res.get(("quoted uncertainty", b), [0,0])[1] for b in ["resolved (3-10x)","well resolved (>10x)"])
lo, hi = wilson(kk, nn)
print()
print(f"  THE CLEANEST FIGURE — real uncertainties, step resolved 3x or better:")
print(f"      {kk} of {nn} fall — {100*kk/nn:.0f}%, 95% interval {100*lo:.0f}–{100*hi:.0f}%")
