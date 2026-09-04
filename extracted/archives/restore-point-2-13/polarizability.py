#!/usr/bin/env python3
"""polarizability.py -- fit alpha_d from the compendium and check it against the literature.

Register 788. The precedent search found P.polar established since Freeman & Kleppner
1976, and found published core polarizabilities obtained from exactly the series this
compendium holds. That makes an external check possible for the first time: fit the
polarizability from our own high-l defects and compare.

The core polarization model (Mayer & Mayer 1933; Freeman & Kleppner PRA 14 1614 1976):

    delta_l  =  (3/4) * alpha_d * <r^-4>  +  (35/16) * alpha_q * <r^-6>   (in a.u.)

with, for a hydrogenic Rydberg electron of effective charge Z at (n, l),

    <r^-4> = Z^4 * (3 n^2 - l(l+1)) / (2 n^5 * (l-1/2) * l * (l+1/2) * (l+1) * (l+3/2))

Fitting only the dipole term against our measured defects gives alpha_d. Published
comparisons available: Zn+ 18.33 +/- 0.95 a0^3 (from the 4snf series, the same one
this compendium holds), Na+ 1.0015(15) a.u., Rb+ 9.12(2) a0^3.

A defect that is NOT dominated by polarization -- one with residual penetration -- will
give a wrong alpha_d, so the comparison also tests where P.polar actually applies.
"""
import re, math, statistics as st
from collections import defaultdict
from zeno import State, step

ROM = {1:'I',2:'II',3:'III',4:'IV',5:'V'}
LM = {"s":0,"p":1,"d":2,"f":3,"g":4,"h":5,"i":6,"k":7}
PUB = {   # published dipole polarizabilities of the CORE ion, a0^3
    ("Zn", 1): (18.33, 0.95, "Zn+ from the 4snf series, core polarization model"),
    ("Na", 1): (1.0015, 0.0015, "Na+ from l=3,4,5 splittings, Freeman & Kleppner 1976"),
}

def alpha_from_delta(delta, n, l, Z):
    """alpha_d from a measured quantum defect.

    The polarization model gives an ENERGY shift, not a defect:
        Delta E = -(1/2) alpha_d <r^-4>
    and the defect enters through
        Delta E = -Z^2/(2 n*^2) + Z^2/(2 n^2)  ~  -Z^2 delta / n^3
    so
        delta = (n^3 / (2 Z^2)) * alpha_d * <r^-4>
    With the hydrogenic expectation value
        <r^-4> = Z^4 (3n^2 - l(l+1)) / (2 n^5 (l-1/2) l (l+1/2) (l+1) (l+3/2))
    this collapses to
        delta = alpha_d Z^2 (3n^2 - l(l+1)) / (4 n^2 (l-1/2) l (l+1/2) (l+1) (l+3/2))
    which is very nearly n-INDEPENDENT for large n, as a defect must be.

    An earlier version equated alpha_d to (4/3) delta / <r^-4>, omitting the n^3/(2Z^2)
    conversion, and returned values up to 464,700 a0^3 against a physical range of
    0.1 to 20. The absurdity was the check (register 788).
    """
    D = (l-0.5) * l * (l+0.5) * (l+1) * (l+1.5)
    num = 4 * n*n * D
    den = Z*Z * (3*n*n - l*(l+1))
    return delta * num / den

def run():
    rows = [l.rstrip("\n").split("\t") for l in open("SPECTRA-DATA.tsv", encoding="utf-8")][1:]
    out = defaultdict(list)
    for r in rows:
        m = re.search(r"n([spdfghik])\b", r[1])
        if not m: continue
        l = LM[m.group(1)]
        if l < 3: continue                      # polarization dominates only above penetration
        el = re.match(r"([A-Z][a-z]?)", r[0].strip())
        try:
            Z = int(r[9]); d = float(r[7])
            lo, hi = (int(x) for x in re.findall(r"\d+", r[2])[:2])
        except Exception: continue
        nbar = (lo + hi) / 2                    # the series' central n
        out[(el.group(1), Z, l)].append(alpha_from_delta(d, nbar, l, Z))
    return out

with State("polarizability") as s:
    fits = step(s, "fit alpha_d from every high-l channel", run, budget=300)

print(f"  alpha_d fitted from the DIPOLE TERM ALONE, by species and l   (a0^3)\n")
print(f"  {'species':<9}{'l':<4}{'channels':>9}{'alpha_d':>12}{'spread':>10}")
byel = defaultdict(list)
for k in sorted(fits, key=lambda x: (x[0], x[1], x[2])):
    v = fits[k]
    m = st.mean(v); sd = st.pstdev(v) if len(v) > 1 else 0.0
    print(f"  {k[0]+' '+ROM[k[1]]:<9}{'spdfghik'[k[2]]:<4}{len(v):>9}{m:>12.3f}{sd:>10.3f}")
    byel[(k[0], k[1])].append((k[2], m))
print()
print("  AGAINST PUBLISHED VALUES")
for k, (pv, pe, src) in PUB.items():
    got = [m for l, m in byel.get(k, [])]
    if not got:
        print(f"  {k[0]}+ : no high-l channel in the compendium")
        continue
    m = st.mean(got)
    ok = abs(m - pv) <= 3 * max(pe, 0.05 * pv)
    print(f"  {k[0]}+ : ours {m:8.3f}   published {pv:8.4f} +/- {pe}   {'AGREES' if ok else 'DISAGREES'}")
    print(f"        {src}")
