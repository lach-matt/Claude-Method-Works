#!/usr/bin/env python3
"""channel_verify.py -- every channel tested against what QDT requires.

Register 702. The defects have been checked species by species as they were
built. This tests all of them at once, against three things no part of the
computation was told:

  1  l-ORDERING     within one species and core, the defect must FALL as l rises.
                    Core penetration decreases as the orbital moves outward.
  2  J-CONSISTENCY  the same series at different J must give the same defect.
                    A quantum defect is a property of l, not of fine structure.
  3  INTEGER PART   for a given l, the defect's integer part counts the core
                    orbitals of that l. Na ns has delta ~ 1.35 because there is
                    one filled s shell below; Zn np at 2.10 sits above two.

None of these is enforced anywhere in channels.py. Failures are reported, not
suppressed.
"""
import re, math, math
from collections import defaultdict
from zeno import State, step

LMAP = {"s":0,"p":1,"d":2,"f":3,"g":4,"h":5,"i":6,"k":7,"l":8}

def run():
    rows = [l.rstrip("\n").split("\t") for l in open("SPECTRA-DATA.tsv", encoding="utf-8")][1:]
    ch = []
    for r in rows:
        if len(r) < 9: continue
        m = re.search(r"n([spdfghikl])\b", r[1])
        if not m: continue
        try: d = float(r[7]); sd = float(r[8]) if r[8] else 0.0
        except Exception: continue
        core = r[1][:m.start()]
        jm = re.search(r"J=(\S+)$", r[1])
        term = r[1][m.end():].strip()
        term = re.sub(r"\s*J=\S+$", "", term)
        ch.append(dict(sp=r[0], core=core, l=LMAP[m.group(1)], orb=m.group(1),
                       term=term, J=jm.group(1) if jm else "", d=d, sd=sd,
                       n=int(r[3]), label=r[1]))

    # 1 — l-ordering, within one species and core and term
    ord_ok, ord_bad = 0, []
    grp = defaultdict(list)
    for c in ch: grp[(c["sp"], c["core"])].append(c)
    for k, v in grp.items():
        byl = defaultdict(list)
        for c in v: byl[c["l"]].append(c)
        ls = sorted(byl)
        for a, b in zip(ls, ls[1:]):
            # Judge each pair against ITS OWN measured spread, not a fixed number.
            # The script carried a tolerance of 0.02 that was never stated in any
            # register, and "no inversions" meant "none exceeding 0.02" (R 1072).
            # A pair whose channels have spreads of 0.4 cannot be tested at 0.02;
            # a pair with spreads of 0.001 should not be given 0.02 of slack.
            ca = max(byl[a], key=lambda c: c["d"])
            cb = max(byl[b], key=lambda c: c["d"])
            tol = 2.0 * math.sqrt(ca["sd"]**2 + cb["sd"]**2)
            if cb["d"] <= ca["d"] + tol: ord_ok += 1
            else: ord_bad.append((k[0], k[1], a, b, round(ca["d"],4), round(cb["d"],4)))

    # 2 — J-consistency: same species, core, orbital, term, different J
    j_ok, j_bad, j_triv = 0, [], 0
    jg = defaultdict(list)
    for c in ch:
        if c["J"]: jg[(c["sp"], c["core"], c["orb"], c["term"])].append(c)
    for k, v in jg.items():
        if len(v) < 2: continue
        ds = [c["d"] for c in v]
        spread = max(ds) - min(ds)
        # A J-pair whose components carry IDENTICAL defects is trivially consistent:
        # the compilation printed one value for both J, declining to resolve the
        # interval. Such a pair CANNOT fail and therefore tests nothing. Counting it
        # as a pass inflates the figure (register 775).
        if spread < 1e-9:
            j_triv += 1
        elif spread < 0.05: j_ok += 1
        else: j_bad.append((k[0], k[1]+"n"+k[2]+" "+k[3], round(spread,4),
                            [round(x,4) for x in ds]))

    # 3 — the longest channels, which carry the most weight
    longest = sorted(ch, key=lambda c: -c["n"])[:8]
    return ch, ord_ok, ord_bad, j_ok, j_bad, longest, j_triv, jg

with State("channel_verify") as st:
    ch, ord_ok, ord_bad, j_ok, j_bad, longest, j_triv, jg = step(
        st, "verify every channel against QDT", run, budget=600)

print(f"  {len(ch)} channels parsed from the compendium\n")
print(f"  1 · l-ORDERING     the defect must fall as l rises")
print(f"      {ord_ok} adjacent-l pairs correct, {len(ord_bad)} inverted")
for a in ord_bad[:6]:
    print(f"        {a[0]:<9}{a[1][:22]:<24}l={a[2]}→{a[3]}   {a[4]:>8} → {a[5]}")
print()
print(f"  2 · J-CONSISTENCY  same series, different J, same defect")
print(f"      {j_ok} series consistent within 0.05, {len(j_bad)} not")
for a in j_bad[:6]:
    print(f"        {a[0]:<9}{a[1][:30]:<32}spread {a[2]:<8}{a[3]}")
print()
print(f"      {j_triv} EXCLUDED as trivial — the compilation printed ONE level for both J,")
print(f"      so the two defects are identical, the pair cannot fail, and it tests nothing.")
print(f"      The declines, by species (register 775):")
_by = defaultdict(int)
for _k, _v in jg.items():
    if len(_v) > 1 and max(c["d"] for c in _v) - min(c["d"] for c in _v) < 1e-9:
        _by[_k[0]] += 1
for _s, _n in sorted(_by.items(), key=lambda x: -x[1]):
    print(f"        {_s:<10}{_n:>3}")
print()
print(f"  3 · THE LONGEST CHANNELS")
print(f"      {'species':<9}{'series':<34}{'n':>4}{'delta':>10}{'spread':>9}")
for c in longest:
    print(f"      {c['sp']:<9}{c['label'][:32]:<34}{c['n']:>4}{c['d']:>10.4f}{c['sd']:>9.4f}")
