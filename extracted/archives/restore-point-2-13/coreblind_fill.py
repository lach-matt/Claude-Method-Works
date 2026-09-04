#!/usr/bin/env python3
"""coreblind_fill.py -- from bounding to DETERMINING, via P.coreblind.

Register 845. Every relation so far gives a bound. P.coreblind gives a value: the
defect depends on l and the core's charge, not on which STATE the core is in, and it
holds 9 of 9 (register 815) including Ne II's cores 26,000 cm-1 apart and Si I's 287
apart.

So where a species has one parent core measured at some l and another core NOT
measured at that l, P.coreblind determines the missing one. That is a value with an
uncertainty — the observed spread between cores — rather than an interval between
two different mechanisms.

The core was always in the series label; the (Z, charge, l) key of register 785
discarded it. This reads it back out.

Every determination is marked DETERMINED and carries the spread P.coreblind itself
shows, which is the honest error on it. A determination is a stronger claim than a
bracket and must carry a stronger warning: it rests on ONE mechanism at nine
instances, interval 70-100%.
"""
import re, statistics as st
from collections import defaultdict
from zeno import State, step

LM = {"s":0,"p":1,"d":2,"f":3,"g":4,"h":5,"i":6,"k":7}

def load():
    """channels keyed by (species, parent core, l) — the core RESTORED"""
    rows = [l.rstrip().split("\t") for l in open("SPECTRA-DATA.tsv", encoding="utf-8")][1:]
    out = defaultdict(list)
    for r in rows:
        m = re.search(r"n([spdfghik])\b", r[1])
        if not m: continue
        core = r[1][:m.start()].strip() or "(ground)"
        try: out[(r[0].rstrip(" *"), core, LM[m.group(1)])].append(float(r[7]))
        except Exception: pass
    return {k: (st.mean(v), len(v)) for k, v in out.items()}

def spread_between_cores(H):
    """P.coreblind's own error: how far apart do two cores actually sit?"""
    by = defaultdict(dict)
    for (sp, core, l), (d, n) in H.items(): by[(sp, l)][core] = d
    sp_ = [max(v.values()) - min(v.values()) for v in by.values() if len(v) > 1]
    return (st.median(sp_), max(sp_), len(sp_)) if sp_ else (0, 0, 0)

def determine(H):
    """a core with no channel at l, where another core of the same species has one"""
    cores = defaultdict(set); atl = defaultdict(dict)
    for (sp, core, l), (d, n) in H.items():
        cores[sp].add(core); atl[(sp, l)][core] = (d, n)
    out = []
    for (sp, l), got in atl.items():
        for core in cores[sp] - set(got):
            # only if that core is measured at SOME l — otherwise it may not exist
            if not any((sp, core, ll) in H for ll in range(8)): continue
            vals = [d for d, _ in got.values()]
            out.append((sp, core, l, st.mean(vals), max(vals)-min(vals) if len(vals) > 1 else None,
                        sorted(got)))
    return out

with State("coreblind_fill") as s:
    H   = step(s, "load channels with the parent core restored", load, budget=180)
    err = step(s, "P.coreblind's own spread between cores",
               lambda: spread_between_cores(H), budget=120)
    DET = step(s, "determine every missing core-l cell", lambda: determine(H), budget=180)

med, mx, n = err
print(f"  P.COREBLIND'S OWN ERROR — how far apart two cores actually sit\n")
print(f"      {n} species-l groups hold two or more cores")
print(f"      median spread between cores : {med:.4f}")
print(f"      largest                     : {mx:.4f}")
print()
print(f"  DETERMINED CELLS — a core with no channel at l, another core of the")
print(f"  same species measured there\n")
print(f"  {'species':<10}{'missing core':<28}{'l':>3}{'determined delta':>19}{'from':>7}")
for sp, core, l, d, spread, srcs in sorted(DET, key=lambda x: (x[0], x[2]))[:22]:
    e = f"+/- {spread:.4f}" if spread else f"+/- {med:.4f}"
    print(f"  {sp:<10}{core[:26]:<28}{'spdfghik'[l]:>3}{f'{d:.4f} {e}':>19}{len(srcs):>7}")
if len(DET) > 22: print(f"  ... and {len(DET)-22} more")
print()
print(f"  {len(DET)} cells DETERMINED, against 128 merely bracketed (register 841).")
print(f"  Each rests on ONE mechanism at nine instances, interval 70-100% —")
print(f"  a stronger claim on weaker support, and marked as such.")
