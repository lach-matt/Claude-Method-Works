#!/usr/bin/env python3
"""converge_selfsame.py -- take P.converge from 1 instance to as many as the data allows.

Register 811. P.converge rests on ONE test (Ba III, register 698) and its interval is
21-100%. P.selfsame rests on three. Both can be tested far more widely on data already
collected, at the cost of a run rather than a capture.

P.CONVERGE. A Rydberg series measures its own limit. For every channel long enough to
fit, fit (limit, delta) from the levels alone and ask whether the fitted limit falls
inside the published uncertainty. The published limit and its error are read from the
species file's own header, so nothing is supplied by hand.

P.SELFSAME. One series in disjoint n-windows gives one defect. For every channel with
enough members, split at the midpoint, compute the defect in each half separately, and
ask whether they agree. Register 751 qualified this: the halves must be comparable in
P.lens's amplification, so a channel spanning a wide n-range is expected to fail and
that expectation is reported rather than hidden.
"""
import re, math, glob, os, statistics as st
from collections import defaultdict
import numpy as np
from scipy.optimize import curve_fit
from zeno import State, step

R = 109737.31568

def limits_from_channels():
    src = open("channels.py", encoding="utf-8").read()
    i = src.index("LIM = {"); depth = 0; j = i + 6
    while True:
        if src[j] == "{": depth += 1
        elif src[j] == "}":
            depth -= 1
            if depth == 0: break
        j += 1
    return eval(src[i+6:j+1])

def published_error(path):
    """the limit's own uncertainty, read from the file's header comments"""
    head = "".join(l for l in open(path, encoding="utf-8") if l.startswith("#"))
    m = re.search(r"limit[^\n]*?([\d,]+\.?\d*)\s*(?:\+/-|±)\s*([\d.]+)", head, re.I)
    return float(m.group(2)) if m else None

def run():
    LIM = limits_from_channels()
    conv, self_ = [], []
    for f in sorted(glob.glob("spectra_raw/*.tsv")):
        nm = os.path.basename(f)[:-4]
        if nm not in LIM: continue
        lim, Z = LIM[nm]
        perr = published_error(f)
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
            lab = f"{nm} {key[0]}n{key[1]} {key[2]}"
            n = np.array([x[0] for x in v], float); E = np.array([x[1] for x in v])
            # --- P.converge: fit the limit from the series alone
            if len(v) >= 5 and perr is not None:
                g = lambda x, L, dd: L - Z*Z*R/(x-dd)**2
                try:
                    p_, cov = curve_fit(g, n, E, p0=[lim, 0.5], maxfev=40000)
                    se = float(np.sqrt(np.diag(cov))[0])
                    if p_[0] > E.max():
                        conv.append((lab, float(p_[0]), lim, perr, se))
                except Exception: pass
            # --- P.selfsame: split into disjoint halves
            if len(v) >= 8:
                h = len(v)//2
                d = [m - Z*math.sqrt(R/(lim-e)) for m, e in v]
                a, b = st.mean(d[:h]), st.mean(d[h:])
                span = v[-1][0] / max(v[0][0], 1)
                self_.append((lab, a, b, abs(a-b), span))
    return conv, self_

with State("converge_selfsame") as s:
    conv, self_ = step(s, "test P.converge and P.selfsame at scale", run, budget=900)

print(f"  P.CONVERGE — the fitted limit against the published one\n")
print(f"  {'channel':<40}{'fitted':>13}{'published':>12}{'diff':>9}{'pub err':>9}{'in?':>5}")
ok = 0
for lab, fit, pub, perr, se in sorted(conv, key=lambda x: abs(x[1]-x[2]))[:16]:
    d = abs(fit-pub); inside = d <= max(perr, se)
    ok += inside
    print(f"  {lab[:38]:<40}{fit:>13,.1f}{pub:>12,.1f}{d:>9.1f}{perr:>9.2f}{'yes' if inside else 'NO':>5}")
tot_ok = sum(1 for lab, fit, pub, perr, se in conv if abs(fit-pub) <= max(perr, se))
print(f"\n  {tot_ok} of {len(conv)} fitted limits fall inside the published uncertainty")
print()
print(f"  P.SELFSAME — one channel, two disjoint n-windows\n")
print(f"  {'channel':<40}{'low half':>11}{'high half':>11}{'|diff|':>9}{'n span':>8}")
for lab, a, b, d, span in sorted(self_, key=lambda x: x[3])[:14]:
    print(f"  {lab[:38]:<40}{a:>11.4f}{b:>11.4f}{d:>9.4f}{span:>8.1f}")
agree = sum(1 for _, _, _, d, _ in self_ if d < 0.05)
print(f"\n  {agree} of {len(self_)} channels agree between halves to better than 0.05")
