#!/usr/bin/env python3
"""pjj.py -- P.jj tested on the RAW LEVELS rather than on built channels.

Register 818. P.jj rests on 65 J-pairs and needs 275 to halve its interval. The 65 came
from built channels, and a pair only forms when BOTH J components survive channel
construction — which requires each to reach three members independently. The raw levels
carry pairs that never became channels.

Zeno phases, each closed before the next opens, each checkpointed so a reopen costs
nothing:

    fetch    read every species file into (series-key -> [(n, J, E)])
    read     compute the defect of every (series, J) with enough members
    analyse  form J-pairs, separate the trivially identical from the testable
    report

The phases are separate step() calls so the expensive one — fetch — runs once and is
reused if analyse is rewritten, which it will be.
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

# ---------------------------------------------------------------- PHASE: FETCH
def fetch():
    """every level, keyed by series WITHOUT J — so J becomes the free coordinate"""
    LIM = limits()
    out = {}
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
            # key WITHOUT J: (file, core, orbital, term)
            ser[(nm, mm.group(1), mm.group(3), p[1])].append((int(mm.group(2)), p[2], E))
        for k, v in ser.items(): out[k] = (v, lim, Z)
    return out

# ----------------------------------------------------------------- PHASE: READ
def read(raw):
    """the defect of every (series, J) that reaches two members or more"""
    out = {}
    for k, (v, lim, Z) in raw.items():
        byJ = defaultdict(list)
        for n, J, E in v: byJ[J].append((n, E))
        for J, w in byJ.items():
            w = sorted(set(w))
            if len(w) < 2: continue
            d = [n - Z*math.sqrt(R/(lim-E)) for n, E in w]
            out[k + (J,)] = (st.mean(d), st.pstdev(d) if len(d) > 1 else 0.0, len(w))
    return out

# -------------------------------------------------------------- PHASE: ANALYSE
def analyse(defects):
    byser = defaultdict(dict)
    for k, v in defects.items(): byser[k[:4]][k[4]] = v
    triv, ok, bad = [], [], []
    for k, d in byser.items():
        if len(d) < 2: continue
        vals = [x[0] for x in d.values()]
        spread = max(vals) - min(vals)
        if spread < 1e-9: triv.append((k, len(d)))
        elif spread < 0.05: ok.append((k, spread, len(d)))
        else: bad.append((k, spread, len(d)))
    return triv, ok, bad

with State("pjj") as s:
    raw     = step(s, "fetch every level, keyed without J",        fetch,   budget=300)
    defects = step(s, "read the defect of every (series, J)", lambda: read(raw),    budget=300)
    triv, ok, bad = step(s, "analyse: form and classify J-pairs",
                         lambda: analyse(defects), budget=300)

n = len(ok) + len(bad)
print(f"  {len(raw)} series (J free) · {len(defects)} (series, J) with 2+ members\n")
print(f"  J-PAIRS FORMED           {len(triv)+n}")
print(f"      trivially identical  {len(triv)}   excluded — cannot fail (register 775)")
print(f"      TESTABLE             {n}")
print(f"          consistent < 0.05 {len(ok)}   ({100*len(ok)//n if n else 0}%)")
print(f"          not               {len(bad)}")
print()
print(f"  against the built-channel figure of 52 of 65 (register 775)")
print(f"  this is {len(ok)} of {n} — {n/65:.1f}x the sample")
print()
print(f"  the widest disagreements:")
for k, sp, c in sorted(bad, key=lambda x: -x[1])[:10]:
    print(f"      {k[0]:<14}{(k[1]+'n'+k[2]+' '+k[3])[:30]:<32}{c} J   spread {sp:.4f}")
