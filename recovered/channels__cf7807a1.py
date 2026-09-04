#!/usr/bin/env python3
"""channels.py -- turn collected levels into channel rows.

Register 673. A channel is one Rydberg series: same core, same orbital letter,
same term, n running. For each, n* = Z sqrt(R/(limit - level)), the quantum
defect is delta = n - n*, and the spread is its standard deviation.

Eleven columns, matching the Spectra Compendium's existing rows.
"""
import re, os, glob, math, statistics as st
from zeno import State, step
R = 109737.31568
LIM = {"NeI":(173929.75,1),"NeII":(330388.6,2),"BeI":(75192.64,1),"MgI":(61671.05,1),
       "MgII":(121267.64,2),"CaI":(49305.95,1),"CaII":(95751.88,2),"CII":(196664.7,2),
       "LiI":(43487.150,1),"LiII":(610078.4,2),"ZnI":(75769.33,1),"ZnII":(144892.6,2),
       "ArII":(222848.30,2),"SiI":(65747.76,1),"SiII":(131838.14,2),
       "ScIII_asd":(199677.37,3),"BiIII_asd":(206242.0,3),"ArII_asd":(222848.30,2)}
NAME = {"NeI":"Ne I","NeII":"Ne II","BeI":"Be I","MgI":"Mg I","MgII":"Mg II","CaI":"Ca I",
        "CaII":"Ca II","CII":"C II","LiI":"Li I","LiII":"Li II","ZnI":"Zn I","ZnII":"Zn II",
        "ArII":"Ar II","SiI":"Si I","SiII":"Si II","ScIII_asd":"Sc III",
        "BiIII_asd":"Bi III","ArII_asd":"Ar II"}

def run():
    out = []
    for p in sorted(glob.glob("spectra_raw/*.tsv")):
        nm = os.path.basename(p)[:-4]
        if nm not in LIM: continue
        lim, z = LIM[nm]
        ser = {}
        for l in open(p, encoding="utf-8"):
            if l.startswith("#") or not l.strip(): continue
            f = l.rstrip("\n").split("\t")
            if f[0] == "config": continue
            try: lev = float(f[3])
            except Exception: continue
            m = re.match(r"^(.*?)(\d+)([spdfghik])$", f[0].strip())
            if not m: continue
            core, n, orb = m.group(1), int(m.group(2)), m.group(3)
            key = (core, orb, f[1], f[2])
            ser.setdefault(key, []).append((n, lev))
        for (core, orb, term, J), v in sorted(ser.items()):
            v = sorted(set(v))
            if len(v) < 3: continue
            if lim <= max(x[1] for x in v): continue
            ns, ds = [], []
            for n, lev in v:
                nstar = z * math.sqrt(R / (lim - lev))
                ns.append(nstar); ds.append(n - nstar)
            interior = len(v) - 2          # the same convention the compendium uses
            out.append(dict(
                species=NAME[nm],
                series=f"{core}n{orb} {term}" + (f" J={J}" if J and J != "" else ""),
                nrange=f"{v[0][0]}–{v[-1][0]}",
                levels=len(v), interior=interior,
                bracket=f"{interior}/{interior}",
                nstar=f"{min(ns):.1f}–{max(ns):.1f}",
                delta=f"{st.mean(ds):+.4f}",
                spread=f"{(st.pstdev(ds) if len(ds)>1 else 0):.4f}",
                zeff=z, limit=f"{lim:,.3f}"))
    return out

with State("channels") as st_:
    ch = step(st_, "build channels from collected levels", run, budget=600)

print(f"  {len(ch)} channels built, {sum(c['interior'] for c in ch)} interior cells\n")
print(f"  {'species':<9}{'series':<30}{'n':<9}{'lev':>4}{'int':>5}{'delta':>10}{'sigma':>9}")
for c in ch:
    print(f"  {c['species']:<9}{c['series'][:29]:<30}{c['nrange']:<9}"
          f"{c['levels']:>4}{c['interior']:>5}{c['delta']:>10}{c['spread']:>9}")
with open("CHANNELS-NEW.tsv", "w", encoding="utf-8") as f:
    f.write("species\tseries\tn\tlevels\tinterior\tbracket\tnstar\tdelta\tspread\tZeff\tlimit\n")
    for c in ch:
        f.write("\t".join(str(c[k]) for k in
                ("species","series","nrange","levels","interior","bracket",
                 "nstar","delta","spread","zeff","limit")) + "\n")