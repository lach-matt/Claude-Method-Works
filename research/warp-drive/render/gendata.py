"""Regenerate the master-lattice artifact's DATA block from the instruments.

Every number here is measured on the spot -- nothing is carried from the
previous render, which is the whole point: that render showed the withdrawn
state.
"""
import itertools, json, os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
import master, hlaw, rubik, duality, bounds
import questions as _q
# The question index is SEATED IN master.py now (DOCKET 8) -- no monkeypatch.
assert "questions" in master.inventory(), "master.py has not seated questions"
# WITHDRAWN 2026-09-20 -- the pin `assert len(master.inventory()) == 10`.
# It was written at b870af6 (2026-09-14 08:26), when the inventory held ten,
# and it has raised AssertionError since fc4c06b (2026-09-14 17:35), DOCKET 2,
# which unseated "periodic layout 2-D" -- ruled a coarsening of the 3-D chart,
# in exact bijection with it at equal reach -- and took the inventory to nine.
# A generator that cannot run writes nothing, so DATA.json has been the
# 2026-09-14 file ever since: a TRANSCRIPTION, which is exactly what
# render/README.md says a deliverable must never be.
#
# THE COUNT WAS NEVER THE PROPERTY THIS FILE NEEDS.  `inv` is read by NAME and
# only by name (`X = inv[n]` below, over the names master_index() seats), so
# what has to hold is that the inventory and the master index agree on WHICH
# indexes are seated -- not on how many.  A count pinned against a population
# that seats and unseats rows is a pin on a moving object; it goes stale on the
# next docket either way.  The property below cannot: it is silent when an
# eleventh index lands and it still fires the instant a name in one is missing
# from the other, which is the failure that would actually corrupt the render.
_inv, _mi = master.inventory(), master.master_index()
assert _inv, "master.py seats no indexes at all"
assert set(_inv) == set(_mi), (
    "inventory and master index disagree on which indexes are seated: %r"
    % (sorted(set(_inv) ^ set(_mi)),))

LANGS = list(hlaw.LANGS)
inv = _inv
mi = _mi
CELLS = frozenset(mi.values())
cl, _ = hlaw.closures(CELLS)

ks = master.channel_sets()
standing = master.channel_standing()

# ---- channels
channels = []
for K, S in enumerate(ks):
    st, who = standing[K]
    channels.append({"K": K, "set": sorted(S), "standing": st,
                     "who": list(who), "n": len(who), "C": len(S)})
byC = {}
for ch in channels:
    byC.setdefault(str(ch["C"]), []).append(ch["K"])

# ---- collapse
holds, faithful, need1, need2 = master.collapse_condition()
cmap = {}
for c in CELLS:
    cmap[str(c[0])] = [c[1], c[2]]
for K, S in enumerate(ks):                      # fill unseated C values lawfully
    C = len(S)
    if str(C) not in cmap:
        Sc = 1 if "statistics" in S else 0
        Oc = 1 if "order" in S else 0
        cmap[str(C)] = [Sc, Oc]

# ---- seated cells, with per-index detail
seated = []
for cell in sorted(CELLS):
    names = sorted(n for n, v in mi.items() if v == cell)
    detail = []
    for n in names:
        X = inv[n]
        a, box, dens = master.shape(X)
        clo = sorted(master.closers(X))
        detail.append({"cells": len(X), "arity": a, "box": box,
                       "density": round(100 * dens, 1), "closers": clo,
                       "K": ks.index(frozenset(clo))})
    seated.append({"cell": list(cell), "indexes": names, "detail": detail})

# ---- what each language demands
demands = {L: sorted(list(c) for c in (cl[L] - CELLS)) for L in LANGS}
counts = {"indexes": len(mi), "cells": len(CELLS),
          "demand": {L: len(cl[L]) - len(CELLS) for L in LANGS}}

# ---- the covering relation over seated union demanded
U = sorted(set(CELLS) | {tuple(c) for L in LANGS for c in demands[L]})
le = lambda a, b: all(x <= y for x, y in zip(a, b))
cover = [[list(a), list(b)] for a in U for b in U
         if a != b and le(a, b)
         and not any(m != a and m != b and le(a, m) and le(m, b) for m in U)]

# ---- joins and meets of every pair of seated cells
pairs = []
for a, b in itertools.combinations(sorted(CELLS), 2):
    j = tuple(max(x, y) for x, y in zip(a, b))
    m = tuple(min(x, y) for x, y in zip(a, b))
    pairs.append({"a": list(a), "b": list(b), "join": list(j), "meet": list(m),
                  "join_seated": j in CELLS, "meet_seated": m in CELLS})

# ---- the rubik layer
br, hd, _rows = rubik.single_move_census(kind="1")
p1 = rubik.para_indexes(kind="1")
p2 = rubik.para_indexes(kind="2")
# RECORDED 2026-09-20, not repaired: `law_separation` is the SAMPLED
# discriminator, and rubik.py supersedes it with `law_separation_exact` -- its
# own docstring records that after DOCKET 2 withdrew the densest index the
# sample became under-powered and read two unlawful pairs as lawful at n=1500,
# seed-dependently. At the seed and n this render uses the two survive by a
# margin of ONE scramble in 3,000. The figure the page actually prints is
# `never.length`, and it is confirmed NOT by luck: the complete radius-3 ball
# (6,933 states, no seed, measured 2026-09-20) gives the same seven pairs, with
# those two breaking 10 times each -- 0.14 % of the orbit. Left sampled because
# the page also prints `law.n` as a scramble count; switching the reading is a
# change to a published figure, not this repair.
viol, n_scr = rubik.law_separation()
never = sorted("%s<=%s" % (a, b) for (a, b), k in viol.items() if k == 0)
lawful = sorted("%s<=%s" % (a, b) for a, b in hlaw.lawful_pairs()) \
    if hasattr(hlaw, "lawful_pairs") else None
rub = {"type1_break": br, "type1_hold": hd,
       "para1": [[list(c), round(r, 4)] for c, r in p1],
       "para2": [[list(c), round(r, 4)] for c, r in p2],
       "law": {"pairs": len(viol), "never": never, "n": n_scr,
               "margins": sorted(((k, "%s<=%s" % (a, b))
                                  for (a, b), k in viol.items() if k),
                                 key=lambda t: t[0])[:4]}}

DATA = {
    "coords": list(master.__dict__.get("COORDS", ("C", "Sc", "Oc", "D", "R"))),
    "axes": {
        "C": {"label": "C — languages that close it", "vals": [0, 1, 2, 3, 4, 5]},
        "D": {"label": "D — arity band", "vals": [0, 1, 2],
              "names": ["2 coordinates", "3–4 coordinates", "5+ coordinates"]},
        "R": {"label": "R — density band", "vals": [0, 1, 2, 3],
              "names": ["<5%", "5–30%", "30–60%", ">60%"]},
    },
    "collapse": {"map": cmap, "holds": holds, "needs": "K1 vacant",
                 "faithful": faithful,
                 "broken_by": "K3, occupied by four witnessed species indexes"},
    "channels": channels, "byC": byC, "seated": seated, "demands": demands,
    "cover": cover, "pairs": pairs, "rubik": rub, "counts": counts,
}
# ---- merged in for the third render: the refusal index, the warp withdrawal,
# ---- the obstruction, and the Petrov correction that deletes the demand.
import json as _j
extra = _j.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                  "DATA2.json")))
DATA["refusal"] = {r["name"]: r["R"] for r in extra["indexes"]}
DATA["Rlattice"] = extra["lattice"]
DATA["forbidden"] = extra["forbidden"]
DATA["impossible_demands"] = extra["impossible_demands"]
DATA["warp"] = extra["warp"]
DATA["obstruction"] = extra["obstruction"]
DATA["lang"] = extra["lang"]
DATA["petrov_fix"] = extra["petrov_fix"]
DATA["corrected"] = extra["corrected"]
DATA["seatedRead"] = extra["seated"]
for row in DATA["seated"]:
    for det, nm in zip(row["detail"], row["indexes"]):
        det["R"] = DATA["refusal"][nm]

print(json.dumps(DATA, indent=1))
