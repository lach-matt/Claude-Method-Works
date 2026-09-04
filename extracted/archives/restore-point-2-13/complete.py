#!/usr/bin/env python3
"""complete.py -- every cell in the spectra index carries a statement.

Register 888. The index has 624 cells and 160 are measured. Register 841 bracketed 128
more from cells adjacent to a measurement. The remaining 336 carry nothing, and the
compendium should not hold cells about which it says nothing at all.

Bounds PROPAGATE. P.lcollapse gives delta(l) < delta(l-1); if delta(l-1) is itself only
bounded above by B, then delta(l) < B follows. The same holds down the l axis and along
an isoelectronic sequence. Iterating to a fixed point reaches cells many steps from any
measurement.

But a bound that travelled ten steps is not the same claim as one that travelled none,
and register 843 established that a bound restating what a mechanism already says carries
no information. Every cell is therefore graded:

    MEASURED      a defect computed from levels
    BRACKETED     bounded above AND below, by DIFFERENT mechanisms, adjacent to measurement
    BOUNDED       bounded on one side, adjacent to measurement
    PROPAGATED    bound inherited through a chain; the chain length is recorded
    FORMAL        the only bound is one a mechanism already implies (l >= 4 is near zero)

The target is zero cells with no grade at all. It is NOT zero cells graded FORMAL —
that grade exists to say "the structure admits this and constrains it only trivially",
which is a true statement and a different one from a prediction.
"""
import re, statistics as st
from collections import defaultdict
from zeno import State, step

LM = {"s":0,"p":1,"d":2,"f":3,"g":4,"h":5,"i":6,"k":7}
ZNUM = {"H":1,"He":2,"Li":3,"Be":4,"B":5,"C":6,"N":7,"O":8,"F":9,"Ne":10,"Na":11,
        "Mg":12,"Al":13,"Si":14,"P":15,"S":16,"Cl":17,"Ar":18,"K":19,"Ca":20,
        "Sc":21,"Ti":22,"Fe":26,"Zn":30,"Ga":31,"Cd":48,"Ba":56,"Hg":80,"Bi":83}
INV = {v: k for k, v in ZNUM.items()}
ROM = {1:"I",2:"II",3:"III",4:"IV",5:"V"}

def measured():
    rows = [l.rstrip().split("\t") for l in open("SPECTRA-DATA.tsv", encoding="utf-8")][1:]
    out = defaultdict(list)
    for r in rows:
        m = re.search(r"n([spdfghik])\b", r[1]); el = re.match(r"([A-Z][a-z]?)", r[0].strip())
        if not (m and el) or el.group(1) not in ZNUM: continue
        try: out[(ZNUM[el.group(1)], int(r[9]), LM[m.group(1)])].append(float(r[7]))
        except Exception: pass
    return {k: st.mean(v) for k, v in out.items()}

def cells(H):
    """the complete index over the alphabets in use, with charge < Z"""
    Zs = sorted({k[0] for k in H}); Cs = sorted({k[1] for k in H}); Ls = sorted({k[2] for k in H})
    return [(Z, c, l) for Z in Zs for c in Cs for l in Ls if c < Z]

def _neighbours(ALL):
    """the next value PRESENT in each alphabet, not the next integer.

    The charge alphabet is sparse — [1,2,3,4,5,9,11,15] — so stepping to c+1 looks
    for a spectrum the index does not contain and the chain breaks. Fe XV never
    reached Fe XI for exactly this reason (register 964).
    """
    Zs = sorted({c[0] for c in ALL}); Cs = sorted({c[1] for c in ALL})
    Ls = sorted({c[2] for c in ALL})
    nxt = lambda seq: {v: (seq[i+1] if i+1 < len(seq) else None) for i, v in enumerate(seq)}
    prv = lambda seq: {v: (seq[i-1] if i > 0 else None) for i, v in enumerate(seq)}
    return (nxt(Zs), prv(Zs), nxt(Cs), prv(Cs), nxt(Ls), prv(Ls))

def propagate(H, ALL):
    """iterate the monotone relations to a fixed point, recording chain length"""
    nZ, pZ, nC, pC, nL, pL = _neighbours(ALL)
    lo = {k: (0.0, 0, None) for k in ALL}    # (bound, steps, which relation)
    hi = {}
    for k, d in H.items():
        lo[k] = (d, 0, "self"); hi[k] = (d, 0, "self")
    changed = True; rounds = 0
    while changed and rounds < 40:
        changed = False; rounds += 1
        for (Z, c, l) in ALL:
            k = (Z, c, l)
            if k in H: continue
            # UPPER: from l-1 (P.lcollapse), the previous ISOELECTRONIC member (P.iso),
            # and the previous SAME-ELEMENT charge state (P.charge, register 963).
            # The third axis is exact at s and p — 23 of 23 monotone — and fails at
            # l >= 2 where P.dcollapse governs, so it is applied only where it holds.
            srcs = [((Z, pL.get(l), l is not None and pL.get(l)), "l")] if False else []
            if pL.get(l) is not None: srcs.append(((Z, c, pL[l]), "l"))
            if pZ.get(Z) is not None and pC.get(c) is not None:
                srcs.append(((pZ[Z], pC[c], l), "iso"))
            if l <= 1 and pC.get(c) is not None: srcs.append(((Z, pC[c], l), "elem"))
            for src, why in srcs:
                if src in hi:
                    v, s = hi[src][0], hi[src][1]
                    if k not in hi or v <= hi[k][0]:
                        if k not in hi or v < hi[k][0] - 1e-12 or s+1 < hi[k][1]:
                            hi[k] = (v, s+1, why); changed = True
            # LOWER: from l+1 and from the next sequence member
            lows = []
            if nL.get(l) is not None: lows.append(((Z, c, nL[l]), "l"))
            if nZ.get(Z) is not None and nC.get(c) is not None:
                lows.append(((nZ[Z], nC[c], l), "iso"))
            if l <= 1 and nC.get(c) is not None: lows.append(((Z, nC[c], l), "elem"))
            for src, wlo in lows:
                # A LOWER bound on delta(k) from delta(k) >= delta(src) needs a LOWER
                # bound on the source. The code took hi[src] — an UPPER bound — which
                # licenses nothing, and where hi[src] had itself been inherited down
                # the l chain the same number travelled back up as if it were two
                # independent facts. That is what made 1,050 bounds degenerate and put
                # 33 deduced lower bounds above twice Seaton's prediction (R 1084).
                #
                # A lower bound is valid only from a MEASURED source, where the lower
                # and upper bounds coincide because the value is known.
                if src in H:
                    v = H[src]
                    if v > lo[k][0] + 1e-12:
                        lo[k] = (v, 1, wlo); changed = True
                elif lo.get(src) and lo[src][2] is not None and lo[src][0] > lo[k][0] + 1e-12:
                    lo[k] = (lo[src][0], lo[src][1]+1, wlo); changed = True
    return lo, hi, rounds

def grade(H, ALL, lo, hi):
    """Grade every cell — and a cell is BOUNDED only if its two bounds come from
    DIFFERENT relations.

    Register 1078. The compendium already defines BRACKETED as "bounded above AND
    below by different mechanisms" (register 831), and never applied that rule to
    PROPAGATED. The consequence, measured: of 1,356 bounded cells, 1,050 had ZERO
    WIDTH — a value asserted as a deduction — and 70 were INVERTED, upper below
    lower. Two bounds from the same relation are the same statement made twice.

    Sorted by which pair of relations supplied the bounds:

        iso / elem   45% genuine intervals
        elem / l     35%
        l / iso      33%
        iso / l      13%
        iso / iso    4.6%
        l / l        0.7%

    The more different the relations, the better the interval. So a two-sided grade
    now requires two different ones, and everything else is graded one-sided.
    """
    out = []
    for k in ALL:
        Z, c, l = k
        if k in H:
            out.append((k, "MEASURED", H[k], H[k], 0)); continue
        h = hi.get(k); lv, ls = lo[k][0], lo[k][1]
        if h is None:
            # No upper bound — but a LOWER one is still a statement, and the seed
            # cells (l = 0, lowest charge) can only ever be bounded from below:
            # they have no l-1 and no earlier sequence member. Discarding them as
            # unconstrained threw away 227 cells that P.iso does constrain (R 889).
            if lv > 1e-9:
                out.append((k, "BOUNDED" if ls <= 1 else "PROPAGATED", lv, None, ls))
            else:
                out.append((k, "UNCONSTRAINED", None, None, None))
            continue
        hv, hs = h[0], h[1]
        ax_hi = h[2] if len(h) > 2 else None
        ax_lo = lo[k][2] if len(lo[k]) > 2 else None
        # a two-sided statement requires two DIFFERENT relations (register 1078)
        two_sided = (lv > 1e-9 and hv > lv + 1e-12
                     and ax_hi is not None and ax_lo is not None and ax_hi != ax_lo)
        steps = max(hs, ls)
        if l >= 4 and lv <= 1e-9 and hv < 0.01:
            g = "FORMAL"
        elif not two_sided:
            # one relation speaking twice is one bound, however it was reached
            g = "BOUNDED" if (lv > 1e-9 or hv < 1e9) else "UNCONSTRAINED"
        elif steps <= 1:
            g = "BRACKETED"
        else:
            g = "PROPAGATED"
        out.append((k, g, lv, hv, steps))
    return out

with State("complete") as s:
    H   = step(s, "read what is measured", measured, budget=120)
    ALL = step(s, "generate the complete index", lambda: cells(H), budget=120)
    lo, hi, rounds = step(s, "propagate bounds to a fixed point",
                          lambda: propagate(H, ALL), budget=600)
    G   = step(s, "grade every cell", lambda: grade(H, ALL, lo, hi), budget=180)

from collections import Counter
cnt = Counter(g for _, g, *_ in G)
print(f"  THE COMPLETE SPECTRA INDEX — {len(ALL)} cells, fixed point in {rounds} rounds\n")
for g in ["MEASURED","BRACKETED","BOUNDED","PROPAGATED","FORMAL","UNCONSTRAINED"]:
    if cnt[g]: print(f"      {g:<16}{cnt[g]:>5}   {100*cnt[g]/len(ALL):>5.1f}%")
print()
un = [x for x in G if x[1] == "UNCONSTRAINED"]
print(f"  cells with NO statement at all: {len(un)}")
if un:
    for k, *_ in un[:10]:
        print(f"      {INV.get(k[0],k[0]):>4} {ROM.get(k[1],k[1]):<5}{'spdfghik'[k[2]]}")
print()
pr = sorted([x for x in G if x[1] == "PROPAGATED"], key=lambda x: x[4])
print(f"  PROPAGATED bounds, by how far they travelled:")
c2 = Counter(x[4] for x in pr)
for s_ in sorted(c2): print(f"      {s_} steps: {c2[s_]}")
