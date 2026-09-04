#!/usr/bin/env python3
"""coords.py -- the coordinate supply, as a table the book can read.

Register 1215. The Spectra Compendium's purpose is to hand Λ values. Everything
else in it — the mechanisms, the equation, the propagation — exists to produce
those values or to state their standing. This writes the values themselves.

    (Z, charge, l, 2S+1)  ->  delta,  grade,  source

GRADES, in order of standing:
    exact        forced by symmetry: delta = 0 at Ne = 1
    measured     fitted to captured levels against a limit
    derived      propagated along a sequence, or bounded by aufbau
    computed     supplied by the channel equation, domain stated

Nothing is ungraded. A value with no provenance is not a coordinate.
"""
import json, math, csv
from collections import Counter

ORDER = [(1,0),(2,0),(2,1),(3,0),(3,1),(4,0),(3,2),(4,1),(5,0),(4,2),(5,1),(6,0),
         (4,3),(5,2),(6,1),(7,0),(5,3),(6,2),(7,1),(8,0)]
OPEN = {}; _z = 0
for _n, _l in ORDER: OPEN[(_n,_l)] = _z+1; _z += 2*(2*_l+1)

A, E0, E1, K, HH = 0.3772, 0.8297, -0.0900, 0.4942, 0.5415

def _load():
    ns = {}
    exec(open("aufbau.py", encoding="utf-8").read().split("with State(")[0]
         .replace("from zeno import State, step", ""), ns)
    return ns["config"], ns["mults"], ns["measured"]()

config, mults, MEAS = _load()
MEAS = dict(MEAS)
# the five out-of-sample captures of this session
MEAS.update({(38,2,0,2):2.7113,(38,2,1,2):2.3501,(38,2,2,2):1.4577,(38,2,3,2):0.0618,
             (38,2,4,2):0.0098,(22,4,0,2):1.4153,(22,4,1,2):1.1506,(22,4,2,2):0.6202,
             (22,4,3,2):0.0774,(7,4,0,1):0.2948,(7,4,1,1):0.1782,(7,4,2,1):0.0335,
             (20,4,0,2):1.3280,(20,4,1,2):1.0703,(20,4,2,2):0.5526,
             (19,3,0,2):1.6589,(19,3,1,2):1.2110})
# Register 1576. Nine cells from Theodosiou, Manson & Inokuti, Phys. Rev. A 34,
# 943 (1986), Tables I, IV and V — the EXPERIMENT column, which is derived from
# spectroscopic term values and not from their Hartree-Slater calculation.
# ONLY the one-electron-outside-a-closed-shell species are entered: Na I and
# Ca X are Ne core plus one electron, Fe VIII is Ar core plus one, so the
# doublet is unambiguous and the paper's multiplet average is over a single
# term. Ca I (two valence electrons) and Ca III (the paper's own remark: "open-
# shell core begins") are a weighted MEAN over several terms and are NOT
# entered — a mean under a single 2S+1 key would fabricate precision the
# source does not have.
MEAS.update({(11,1,0,2):1.35, (11,1,1,2):0.85, (11,1,2,2):0.012,
             (11,1,3,2):0.001,
             (26,8,1,2):0.80, (26,8,2,2):0.40, (26,8,3,2):0.12,
             (20,10,0,2):0.44, (20,10,2,2):0.093})
# Register 1627. THREE cells from the reading list, read off level tables
# already on disk rather than fetched — the first return on `READING-LIST.tsv`.
# Each is a TRIPLET, a single LS term, so the 2S+1 key is exact and register
# 1576's multiplicity rule is satisfied.
#   Ca I  4s.np 3P*  limit Ca II 2S1/2 = 49,305.95  (published)
#   Sc II 3d.np 3P*  limit Sc III 3d 2D3/2 = 103,237.1  (published)
#   Zn I  4s.np 3P*  limit Zn II 2S1/2 = 75,769.33  (published, SM95)
# The same pass reproduced 37 of 39 ALREADY-MEASURED cells to within 0.05,
# which is what makes these three trustworthy: the method was verified on the
# cells whose answer was already held before it was used on cells that were not.
MEAS.update({(20,1,1,3):2.0672, (21,2,1,3):1.5485, (30,1,1,3):2.4109})
# Provenance is per-cell, not per-grade. A measured cell read from a published
# table is not a measured cell read from levels we captured, and the source
# column must say which.
SRC = {k: "Theodosiou, Manson & Inokuti 1986, PRA 34 943, experiment column"
       for k in [(11,1,0,2),(11,1,1,2),(11,1,2,2),(11,1,3,2),
                 (26,8,1,2),(26,8,2,2),(26,8,3,2),
                 (20,10,0,2),(20,10,2,2)]}
SRC.update({(20,1,1,3): "read from CaI.tsv levels, R 1627",
            (21,2,1,3): "read from ScII.tsv levels, R 1627",
            (30,1,1,3): "read from ZnI.tsv levels, R 1627"})

def corb(ne, l): return sum(1 for n, ll, o in config(ne) if ll == l and o > 0)
def n0f(ne, l):
    v = [n for n, ll, o in config(ne) if ll == l and o > 0]
    return (max(v)+1) if v else l+1
def parents(cfg):
    if not cfg: return 1
    n, l, occ = cfg[-1]; cap = 2*(2*l+1)
    return 1 if occ in (0, cap, 1, cap-1) else {0:1, 1:3, 2:16, 3:119}.get(l, 8)

def equation(Z, c, l):
    ne = Z-c+1; p = corb(ne-1, l); t = math.log(c+1)/c
    if p > 0:
        return A*(p**max(E0 + E1*math.log(max(ne,2)), 0.05))*ne**K*t
    thr = OPEN.get((n0f(ne-1, l), l), 999)
    C = min(max((Z-thr+4.0)/8.0, 0.0), 1.0)
    return HH*C*((ne-1)/ne)*ne**K*t

# Register 1578. The status column used to grade cells VERIFIED, POSSIBLE or
# IMPROBABLE. "Improbable" is a judgement about the future, not a fact about the
# record — and register 1287 had already established the rule it breaks: an
# index whose coordinates mix the OBJECT with the OBSERVER cannot close, because
# the observer's axis has no order the object respects. The same fault as
# `standing` in the constant index, `origin` in Lambda_var, `kind` in
# Lambda_phys and `state` in Lambda_ladder.
#
# It is replaced by a fact and a reason:
#     witness   WITNESSED   reality has been consulted for this cell
#               UNWITNESSED reality has not
#     bound     WHY it is unwitnessed. Not a probability — an obstacle, named.
#
# Nothing is lost: every old reason survives as a bound. What is lost is the
# claim to know which obstacles will be overcome, which the index never had
# standing to make. The charge > 10 bound is the case in point: it read "no
# analysed data at this charge" while the index held twelve measured cells above
# it (R 1577).


_FILL = [(1,0,2),(2,0,2),(2,1,6),(3,0,2),(3,1,6),(3,2,10),(4,0,2),(4,1,6),
         (4,2,10),(4,3,14),(5,0,2),(5,1,6),(5,2,10),(5,3,14),(6,0,2),(6,1,6)]

def _one_outside(ne):
    """True when exactly one electron sits outside a closed shell."""
    r = ne
    for n, l, cap in _FILL:
        if r <= cap:
            return r == 1
        r -= cap
    return False

def bound(Z, c, l):
    """Why reality has not been consulted for this cell. A named obstacle."""
    ne = Z-c+1
    if Z > 103:  return "no long-lived isotope"
    if l > 4:    return "series unresolved above ng in any published analysis"
    if parents(config(ne-1)) > 1:
        return f"open-shell core, {parents(config(ne-1))} parents"
    # R 1597. A defect needs a single 2S+1 key, so a species with a HOLE plus
    # an electron, or two valence electrons, yields only a multiplet MEAN.
    # Of 369 unbounded species only 56 have one electron outside a closed
    # shell. This is a bound on KEYABILITY, not on existence or on data.
    if not _one_outside(ne):
        return "not keyable: no single 2S+1 (hole+electron or multi-valence)"
    if c > 10:   return "no analysis located at this charge (NOT a bound on existence)"
    # R 1587: this bound is a CONVENTION and it is faulty at four elements.
    # Technetium (43) and promethium (61) lie BELOW 92 with no primordial
    # isotope; neptunium (93) and plutonium (94) lie above it and occur in
    # trace amounts in uranium ore. The correct test is primordial abundance,
    # not atomic number. Left as-is until a primordial-abundance list is held,
    # so the fault is VISIBLE rather than silently patched.
    if Z in (43, 61): return "no primordial isotope (R 1587)"
    if Z > 92:   return "not naturally occurring"
    return "none — separable series, simply not yet measured"

rows = []
for Z in range(1, 119):
    for c in range(1, Z+1):
        ne = Z-c+1
        for S in mults(ne):
            for l in range(8):
                k = (Z, c, l, S)
                B = min(corb(ne-1, l), n0f(ne-1, l)-l-1)
                if k in MEAS:
                    rows.append((Z, c, l, S, round(MEAS[k], 5), "measured",
                                 SRC.get(k, "captured levels"), B,
                                 "witnessed", "-"))
                elif ne == 1:
                    # DERIVED, not witnessed. delta = 0 follows from symmetry and
                    # no hydrogenic ion has been measured to establish it here.
                    rows.append((Z, c, l, S, 0.0, "exact",
                                 "one electron, delta = 0 by symmetry", B,
                                 "unwitnessed", "derived by symmetry; no measurement required"))
                else:
                    rows.append((Z, c, l, S, round(equation(Z, c, l), 5), "computed",
                                 "the channel equation", B,
                                 "unwitnessed", bound(Z, c, l)))

with open("COORDINATES.tsv", "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f, delimiter="\t")
    w.writerow(["Z","charge","l","mult","delta","grade","source","B","witness","bound"])
    w.writerows(rows)

g = Counter(r[5] for r in rows); s = Counter(r[8] for r in rows)
bd = Counter(r[9] for r in rows if r[8] == "unwitnessed")
print(f"  COORDINATES.tsv — {len(rows):,} rows")
print("      by grade : " + " · ".join(f"{k} {v:,}" for k, v in g.most_common()))
print("      by witness: " + " · ".join(f"{k} {v:,}" for k, v in s.most_common()))
print(f"      WITNESSED {s.get('witnessed',0):,} of {len(rows):,} "
      f"= {100*s.get('witnessed',0)/len(rows):.3f}% of the index has been "
      f"checked against reality")
print("      bounds on the unwitnessed:")
for k, v in bd.most_common():
    print(f"        {v:>7,}  {k}")
