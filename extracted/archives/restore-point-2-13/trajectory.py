#!/usr/bin/env python3
"""trajectory.py — the walk with the leak closed, on the witness principle.

THE PROBLEM (registers 1440 and 1445 together).

    the LAW admits         at least 100 of 106   (midpoint placement, R 1440)
    the trajectory delivers    99 of 106 fitted  (R 1413)
    held out                   90 of 106         (R 1445)

So there is a gap of at least ten between what the corridor system ADMITS and
what any walk has DELIVERED without leaking. Closing it is "solve for
trajectory".

THE LEAK, EXACTLY. `scorer.py` at step Z reads IVL[Z] — the corridor for the
CURRENT element — places a on it, and only then predicts that element. But
`brack.py` builds IVL[Z] FROM the observed entrant at Z. The answer sets the
parameter that produces the answer.

THE INSTRUMENT IS THE ONE BUILT AT REGISTER 1578. A corridor is WITNESSED once
its step has been revealed and UNWITNESSED before. The held-out rule is then one
sentence:

    ** a may be placed only on WITNESSED corridors. **

At step Z the walk sees IVL[Z'] for Z' < Z, places a, predicts Z, and only then
is IVL[Z] revealed and admitted to the witnessed set. Nothing else changes — the
law, the corridors, the tie-break and the reset trigger are all as recorded.

WHAT IS BEING SOLVED FOR. Register 1331: the ordering data constrains only that
a lies in each interval; WHERE INSIDE IS FREE. Register 1440 measured that this
freedom is worth seven points fitted — floor 99, midpoint 100, ceiling 93. This
asks what it is worth HELD OUT, which nobody has measured.

*** THIS IS NOT A SEVENTH PLACEMENT RULE (P4 prohibits that). It is the same
    placements already on record, measured on the honest information set. ***
"""
import sys, io, contextlib, re

src = open("scorer.py", encoding="utf-8").read()
head = src.split("def run(")[0]
ns = {}
with contextlib.redirect_stdout(io.StringIO()):
    exec(head, ns)

STEPS, IVL, OBS, EPS = ns["STEPS"], ns["IVL"], ns["OBS"], ns["EPS"]
OPENS = ns.get("OPENS", set())
occ, candidates, choose = ns["occ"], ns["candidates"], ns["choose"]

INF = 1e9


def held_out(place, a0=1.0, higher_n=True):
    """The walk, with a placed ONLY on corridors already revealed.

    place: how to sit inside the witnessed running intersection —
           'floor', 'mid', 'ceil', or 'stay' (move only when forced out).
    """
    a = a0
    lo, hi = -INF, INF          # the WITNESSED running intersection
    hits, misses, resets = 0, [], []

    for Z in STEPS:
        # ---- place a using ONLY what is witnessed --------------------------
        if lo > -INF or hi < INF:
            L = lo if lo > EPS else None
            U = hi if hi < 1e8 else None
            if place == "floor" and L is not None:
                a = L
            elif place == "ceil" and U is not None:
                a = U
            elif place == "mid" and L is not None and U is not None:
                a = (L + U) / 2
            elif place == "mid" and L is not None:
                a = L
            elif place == "stay":
                if L is not None and a < L:
                    a = L
                elif U is not None and a > U:
                    a = U

        # ---- predict, before the step is revealed --------------------------
        prev = occ(Z - 1)
        pick = choose(candidates(prev), prev, a, higher_n)
        if pick == OBS[Z]:
            hits += 1
        else:
            misses.append((Z, OBS[Z], pick))

        # ---- NOW reveal this step and admit its corridor -------------------
        Lo, Up = IVL[Z]
        nlo, nhi = max(lo, Lo), min(hi, Up)
        if nlo >= nhi:                      # the witnessed intersection empties
            resets.append(Z)
            lo, hi = Lo, Up
        else:
            lo, hi = nlo, nhi

    return hits, misses, resets


print(f"  THE HELD-OUT TRAJECTORY — a placed only on WITNESSED corridors\n")
print(f"  {len(STEPS)} steps, Z = {min(STEPS)} to {max(STEPS)}\n")
print(f"    {'placement inside the witnessed window':<40}{'score':>12}{'resets':>9}")
best = None
for pl in ("floor", "mid", "ceil", "stay"):
    h, ms, rs = held_out(pl)
    if best is None or h > best[0]:
        best = (h, pl, ms, rs)
    print(f"    {pl:<40}{h:>6} / {len(STEPS)}{len(rs):>9}")

h, pl, ms, rs = best
print(f"\n    best held-out placement: {pl.upper()} at {h} of {len(STEPS)}")
print(f"\n  AGAINST THE RECORD:")
print(f"    R 1413 fitted walk                    99 / 106")
print(f"    R 1445 held out                       90 / 106")
print(f"    R 1440 law's ceiling (midpoint)      100 / 106")
print(f"    plain Madelung                        96 / 106")
print(f"    THIS, held out, best placement        {h} / {len(STEPS)}")
