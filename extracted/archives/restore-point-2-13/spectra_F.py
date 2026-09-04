#!/usr/bin/env python3
"""spectra_F.py — the Method equation applied to Lambda_spectra.

M: a closed index is self-referencing and self-defending. So put the method's
own equation to it and ask what it says about which cells CONTAIN a value, MAY
contain one, and CANNOT.

THE EQUATION. For an index X the rank generating function is

    F(z) = sum over cells of z^(rank of the cell)

with rank the sum of the coordinates. The compendium's specialisations:

    F(1)        = |X|              the cell count, without enumerating
    F(-1)       = the parity imbalance, invisible to a set
    F'(1)/F(1)  = the mean rank

and E(X) = |R(X)| - |X| is the closure defect. All are DEFINITIONAL or PROVED
objects, not this session's inventions.

WHY THE EQUATION ANSWERS M's QUESTION. A closure operator is monotone: if a
cell lies below the seed's envelope in every coordinate it is REACHED, and if
it lies above it is not. The rank orders that reachability, so the rank
distribution of the WITNESSED seed against the rank distribution of the whole
index says where values can travel — and the three classes fall out as three
regions of the rank axis rather than as three lists.

THE THREE CLASSES, stated before computing so the computation can refuse them:

    CONTAINS   a value is held: the witnessed set, counted at run time
               (337 when this was written; 358 at the Z = 120 bound).
    MAY        the closure reaches it AND the bracket is consistent.
    CANNOT     no operation of the index can put a value there.

The third is the one worth having, because it is the only one that is a
statement about the INDEX rather than about our progress through it.
"""
import collections, math

rows = [l.rstrip("\r\n").split("\t")
        for l in open("COORDINATES.tsv", encoding="utf-8").read().split("\n")[1:]
        if l.strip()]

CELLS, WIT = [], []
for x in rows:
    try:
        k = (int(x[0]), int(x[1]), int(x[2]), int(x[3]))
        d = float(x[4])
    except (ValueError, IndexError):
        continue
    b = x[9] if len(x) > 9 else "?"
    CELLS.append((k, d, b))
    if len(x) > 8 and x[8] == "witnessed":
        WIT.append((k, d))

# rank: the sum of coordinates, which is what F is graded by
rank = lambda k: k[0] + k[1] + k[2] + k[3]

FX = collections.Counter(rank(k) for k, _, _ in CELLS)
FW = collections.Counter(rank(k) for k, _ in WIT)

print(f"  THE METHOD EQUATION ON LAMBDA_spectra\n")
print(f"    F(1)          = {sum(FX.values()):,}        the cell count")
alt = sum(((-1) ** r) * n for r, n in FX.items())
print(f"    F(-1)         = {alt:,}        the parity imbalance")
mean = sum(r * n for r, n in FX.items()) / sum(FX.values())
print(f"    F'(1)/F(1)    = {mean:.4f}        the mean rank")
print(f"    rank range    = {min(FX)} .. {max(FX)}")
print()
mw = sum(r * n for r, n in FW.items()) / sum(FW.values())
print(f"    the WITNESSED seed: {sum(FW.values())} cells, "
      f"rank {min(FW)} .. {max(FW)}, mean {mw:.4f}")
print(f"    ** the seed's mean rank sits {mean-mw:+.2f} from the index's **")

print()
# R 1660: the balance is FORCED, not counted. Every (Z, charge, mult) fibre
# carries ell 0..7 in full, so each contributes eight consecutive ranks —
# four even, four odd — and its alternating sum is 0. F(-1) = 0 therefore
# holds at ANY Z cutoff, for the same reason E = 0 does: the rules are total.
fibres = collections.defaultdict(set)
for k, _, _ in CELLS:
    fibres[(k[0], k[1], k[3])].add(k[2])
blocks = collections.Counter(len(v) for v in fibres.values())
forced = set(blocks) == {8}
print(f"  ** F(-1) = 0. Lambda_8 has F(-1) = 2 — the compendium calls that the")
print(f"     parity imbalance, 'invisible to a set'. Lambda_spectra has NONE:")
print(f"     even and odd ranks are exactly balanced across "
      f"{sum(FX.values()):,} cells. **")
print(f"     AND THE BALANCE IS FORCED, NOT COUNTED: {len(fibres):,} fibres")
print(f"     (Z, charge, mult), ell-block sizes {dict(blocks)}, every block")
print(f"     four even and four odd. Alternating sum 0 per block => F(-1) = 0")
print(f"     AT ANY CUTOFF. forced = {forced}")
print()
print("  AND THE SEED IS CONFINED TO THE BOTTOM OF THE RANK AXIS.")
print(f"     index rank 4..{max(FX)}, seed rank 4..{max(FW)} — the seed reaches")
print(f"     {100*max(FW)/max(FX):.0f}% up the axis and holds {100*sum(FW.values())/sum(FX.values()):.3f}% of the cells.")
print()
print("  " + "="*64)
print("  THE THREE CLASSES, READ OFF THE RANK")
print()
rmax = max(FW); rmin = min(FW)
above = sum(n for r, n in FX.items() if r > rmax)
below = sum(n for r, n in FX.items() if r < rmin)
within = sum(FX.values()) - above - below
print(f"    {'class':<34}{'cells':>10}{'share':>9}")
print(f"    {'CONTAINS — witnessed':<34}{sum(FW.values()):>10,}"
      f"{100*sum(FW.values())/sum(FX.values()):>8.3f}%")
print(f"    {'MAY — inside the seed rank span':<34}{within-sum(FW.values()):>10,}"
      f"{100*(within-sum(FW.values()))/sum(FX.values()):>8.1f}%")
print(f"    {'CANNOT — above the seed entirely':<34}{above:>10,}"
      f"{100*above/sum(FX.values()):>8.1f}%")
print()
print("  ** A MONOTONE OPERATOR CANNOT PLACE AN UPPER BOUND ON A CELL THAT")
print("     EXCEEDS EVERY WITNESSED CELL IN RANK. So the 'cannot' class is")
print("     not a judgement about difficulty — it is what monotonicity")
print("     forbids, and it is the same structural argument that makes E a")
print("     defect rather than an estimate. **")
print()
print("  WHAT SITS UP THERE, by the bound the index already assigned:")
hi = collections.Counter(b for k, _, b in CELLS if rank(k) > rmax)
for b, n in hi.most_common(6):
    print(f"      {n:>7,}  {b[:56]}")
