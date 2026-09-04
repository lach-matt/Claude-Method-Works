#!/usr/bin/env python3
"""delta_grouping.py — is delta per CHANNEL, per GROUP, or per JANET BLOCK?

The separation hypothesis: a result conditioned on a coordinate holds exactly
when that coordinate SEPARATES. So the question is not whether delta can be
labelled by block -- anything can be labelled -- but whether the labelling
partitions the variance.

CONTROL FIRST. delta depends strongly on l: it is large for s, small for high l,
and that is textbook. Any grouping tested against delta must therefore be tested
WITHIN fixed l, or l will do the work and the grouping will take the credit.

Reported for each candidate coordinate: the fraction of the within-l variance it
explains (eta-squared), against a permutation null that shuffles the labels while
keeping the group sizes. A coordinate that separates does better than its own
shuffle; one that does not, does not.
"""
import csv, re, math, random, statistics as st
from collections import defaultdict

SYM = ("H He Li Be B C N O F Ne Na Mg Al Si P S Cl Ar K Ca Sc Ti V Cr Mn Fe Co Ni Cu Zn Ga "
       "Ge As Se Br Kr Rb Sr Y Zr Nb Mo Tc Ru Rh Pd Ag Cd In Sn Sb Te I Xe Cs Ba La Ce Pr Nd "
       "Pm Sm Eu Gd Tb Dy Ho Er Tm Yb Lu Hf Ta W Re Os Ir Pt Au Hg Tl Pb Bi Po At Rn Fr Ra Ac "
       "Th Pa U Np Pu Am Cm Bk Cf Es Fm Md No Lr Rf").split()
Zof = {s: i + 1 for i, s in enumerate(SYM)}
ROM = {"I": 1, "II": 2, "III": 3, "IV": 4, "V": 5, "VI": 6, "VII": 7, "VIII": 8,
       "IX": 9, "X": 10, "XI": 11, "XII": 12, "XV": 15, "XVI": 16}
STARTS = [1, 3, 5, 13, 21, 39, 57, 89]
blk = lambda Z: max(i for i, s in enumerate(STARTS) if s <= Z) + 1

rows = list(csv.DictReader(open("SPECTRA-DATA.tsv", encoding="utf-8"), delimiter="\t"))
D = []
for r in rows:
    sp = r["species"].split()
    if len(sp) != 2 or sp[0] not in Zof or sp[1] not in ROM:
        continue
    m = re.search(r"n([spdfg])", r["channel"])
    if not m:
        continue
    try:
        d = float(r["delta"])
    except ValueError:
        continue
    rng = re.match(r"(\d+)", r["n"].strip())
    if not rng:
        continue
    Z, c, l, n0 = Zof[sp[0]], ROM[sp[1]], "spdfg".index(m.group(1)), int(rng.group(1))
    D.append({"Z": Z, "c": c, "l": l, "d": d, "blk": blk(Z),
              "M": n0 + l, "Mpar": (n0 + l) % 2, "core": Z - c + 1,
              "per": sum(1 for s in STARTS if s <= Z)})

print(f"  {len(D)} channels parsed with a Z, a charge, an ℓ and a δ\n")
print("  STEP 1 — how much of δ's variance is ℓ alone?\n")
byl = defaultdict(list)
for r in D:
    byl[r["l"]].append(r["d"])
gm = st.mean([r["d"] for r in D])
tot = sum((r["d"] - gm) ** 2 for r in D)
bet = sum(len(v) * (st.mean(v) - gm) ** 2 for v in byl.values())
print(f"    η² of ℓ = {bet/tot:.3f}   ({', '.join(f'{k}:{len(v)}' for k,v in sorted(byl.items()))})")
print(f"    mean |δ| by ℓ: " +
      ", ".join(f"{'spdfg'[k]}={st.mean([abs(x) for x in v]):.3f}" for k, v in sorted(byl.items())))

print("\n  STEP 2 — WITHIN each ℓ, does another coordinate separate what is left?\n")


def eta2_within(key):
    num = den = 0.0
    for l, grp in [(l, [r for r in D if r["l"] == l]) for l in sorted(byl)]:
        if len(grp) < 6:
            continue
        m0 = st.mean([r["d"] for r in grp])
        den += sum((r["d"] - m0) ** 2 for r in grp)
        sub = defaultdict(list)
        for r in grp:
            sub[r[key]].append(r["d"])
        num += sum(len(v) * (st.mean(v) - m0) ** 2 for v in sub.values() if v)
    return num / den if den else 0.0


def null_for(key, n=400, seed=0):
    rng = random.Random(seed)
    out = []
    for _ in range(n):
        pool = defaultdict(list)
        for l in sorted(byl):
            grp = [r for r in D if r["l"] == l]
            labs = [r[key] for r in grp]
            rng.shuffle(labs)
            for r, lab in zip(grp, labs):
                pool[l].append((lab, r["d"]))
        num = den = 0.0
        for l, pairs in pool.items():
            if len(pairs) < 6:
                continue
            m0 = st.mean([d for _, d in pairs])
            den += sum((d - m0) ** 2 for _, d in pairs)
            sub = defaultdict(list)
            for lab, d in pairs:
                sub[lab].append(d)
            num += sum(len(v) * (st.mean(v) - m0) ** 2 for v in sub.values())
        out.append(num / den if den else 0.0)
    return out


print(f"    {'coordinate':<26}{'η² within ℓ':>13}{'null mean':>11}{'p':>8}")
for key, name in [("blk", "Janet block of Z"),
                  ("M", "Madelung M of the channel"),
                  ("Mpar", "parity of M"),
                  ("c", "charge state"),
                  ("core", "core electron count"),
                  ("per", "period of Z")]:
    e = eta2_within(key)
    nl = null_for(key)
    p = sum(1 for x in nl if x >= e) / len(nl)
    print(f"    {name:<26}{e:>13.3f}{st.mean(nl):>11.3f}{p:>8.3f}")

print("\n    η² above its own shuffle means the coordinate separates; at or below")
print("    it means the labelling is doing nothing the group sizes did not.")
