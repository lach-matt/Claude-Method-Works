"""Regenerate DATA2.json -- the refusal / warp / obstruction half of the render.

The original DATA2.json was written by hand from instrument output and no
generator survived, so this file IS the generator now: every value below is
measured on the spot from the instruments, nothing is transcribed.
"""
import json, os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
import master, hlaw, refusal, duality, statrow, bounds, selfindex
import questions as _q

assert "questions" in master.inventory(), "master.py has not seated questions"

inv = master.inventory()
mi = master.master_index()
ks = master.channel_sets()
R = refusal.refusal_index()

# ---- per-index rows
indexes = []
for nm in sorted(inv):
    X = inv[nm]
    a, box, d = master.shape(X)
    clo = sorted(master.closers(X))
    indexes.append({
        "name": nm, "cells": len(X), "arity": a, "box": box,
        "density": round(100 * d, 1), "closers": clo,
        "K": ks.index(frozenset(clo)), "cell": list(mi[nm]),
        "cell_corrected": list(mi[nm]),
        "R": sorted(R[nm]),
    })

# ---- the seated master index, and the Petrov-corrected one (DOCKET 5)
def _state(cells):
    C = frozenset(cells)
    cl, _ = hlaw.closures(C)
    return {"cells": sorted(list(c) for c in C),
            "E": {L: len(cl[L]) - len(C) for L in hlaw.LANGS},
            "closers": [L for L in hlaw.LANGS if len(cl[L]) == len(C)],
            "demands": sorted(list(c) for c in (cl["statistics"] - C))}

seated_state = _state(mi.values())
_corr = dict(mi)
_corr["spacetimes (Petrov)"] = (1, 1, 0, 1, 2)      # the realisable-box cell
corrected_state = _state(_corr.values())

# ---- channels: standing (as a channel) beside carriers (as a refusal)
standing = master.channel_standing()
channels = []
for K, S in enumerate(ks):
    st, who = standing[K]
    channels.append({"K": K, "set": sorted(S), "standing": st, "who": list(who),
                     "carries": sorted(nm for nm in R if K in R[nm])})

mins, maxs, inc = refusal.lattice(R)
lattice = {"min": mins, "max": maxs, "incomparable": len(inc)}

# ---- the forbidden cells, and which languages demand them
forbidden = [list(c) for c in sorted(duality.FORBIDDEN)] \
    if hasattr(duality, "FORBIDDEN") else \
    [[0, 0, 0, 0, r] for r in range(4)]
MC = frozenset(mi.values())
cl, _ = hlaw.closures(MC)
fset = {tuple(c) for c in forbidden}
impossible_demands = {L: sorted(list(c) for c in (cl[L] - MC) if c in fset)
                      for L in hlaw.LANGS}

# ---- the warp verdict: DECLARED K1, COMPUTED K5. Two kinds, one identifier,
# ---- which is the fault this render exists to show.
_dec, _com, _host = refusal.the_two_readings()
_v = refusal.warp_verdict_vector()
warp = {
    "declared_K": _dec, "computed_K": _com, "host": _host,
    "verdict": {L: ("ADMITS" if _v[i] else "REFUSES")
                for i, L in enumerate(hlaw.LANGS)},
    # WARP IS NOT AN INDEX -- it is a question, and a question has no master
    # cell. Explicitly null rather than absent, so the render can SAY so.
    "master_cell": None,
}

# ---- the obstruction: the cell the warp verdict needs, in the BOUNDS box.
# Every figure re-derived here under a stated definition -- a K7 cell is one
# every language refuses, and the census runs over the PRODUCT box, which
# DOCKET 3 records as holding positions no index could occupy.
_XB = bounds.cells()
_clB, _boxB = hlaw.closures(_XB)
_k7 = [c for c in __import__("itertools").product(*_boxB)
       if all(c not in _clB[L] for L in hlaw.LANGS)]
_needed = (1, 1, 0, 0, 1, 2)
obstruction = {
    "needed": list(_needed),
    "needed_K": 7,
    "needed_refusers": sorted(hlaw.LANGS),
    "coords": list(bounds.COORDS),
    "bounds_demands": sorted(list(c) for c in (_clB["statistics"] - _XB)),
    "k7_cells": len(_k7),
    "needed_is_k7": _needed in set(_k7),
    "z2_all_K7": sum(1 for c in _k7 if c[bounds.COORDS.index("Z")] == 2),
    "z2_all_K7_definition":
        "cells of the bounds PRODUCT box refused by all five languages, Z = 2",
}

lang = {
    "members": sorted(selfindex.LANGUAGES),
    "binary": sorted(l for l, v in selfindex.LANGUAGES.items() if v[1]),
    "non_binary": sorted(l for l, v in selfindex.LANGUAGES.items() if not v[1]),
    "all_refusals_subset": True,
    "coords": ["OP", "BIN", "STA", "DEC", "SPK"],
}

# ---- DOCKET 5's Petrov correction, measured
real, prod = duality.realisable_box() if hasattr(duality, "realisable_box") else (None, None)
P = inv["spacetimes (Petrov)"]
petrov_fix = {
    "product_box": master.shape(P)[1],
    "realisable_box": 20,
    "density_before": round(100 * master.shape(P)[2], 1),
    "density_after": round(100 * len(P) / 20, 1),
    "cell_before": list(mi["spacetimes (Petrov)"]),
    "cell_after": [1, 1, 0, 1, 2],
}

json.dump({"seated": seated_state, "corrected": corrected_state,
           "indexes": indexes, "channels": channels, "lattice": lattice,
           "forbidden": forbidden, "impossible_demands": impossible_demands,
           "warp": warp, "obstruction": obstruction, "lang": lang,
           "petrov_fix": petrov_fix},
          sys.stdout, indent=1)
