#!/usr/bin/env python3
"""vi_feasible.py — is the residual a CANCELLATION, or was the search weak?

Eight attacks (R 619) left +16 on NEC >= 2 and -9 on NEC >= 3 unmoved. R 593
noted they miss in OPPOSITE directions, "which a missing constraint does not
do". This session showed (R 1462) that opposite-direction demands unmoved by
every repair is the signature of a Farkas certificate: the family cannot contain
the answer, and the search is not at fault.

All eight attacks asked WHICH RULE SET HITS THE TARGET. This asks whether the
target is reachable by the family at all.

THE STRUCTURE THAT MAKES IT ASKABLE. Each rule is  A >= a -> (B1 >= b1 v ...),
and the cells it REMOVES are {A >= a} & {B1 < b1} & ... & {Bk < bk} — an
AXIS-ALIGNED BOX. So the held set is the complement of a UNION OF BOXES, which
is a far sharper characterisation than "an implication cut" and is what makes
the question finite.

SPACE, DECLARED BEFORE THE RUN. Sample rule sets of the recorded size from the
same generator the search used, keep only those whose TOTAL cell count is at or
near the exact 2,370 — the one column already solved — and look at where the two
NEC errors land. Then:

    if the errors SCATTER around (0,0), the search was weak and a ninth
    attack is justified;

    if they lie on a LINE or in a CONE that excludes (0,0), that is a
    cancellation, the family is refuted, and no further search will help.

Nothing is chosen after seeing the answer: the two outcomes and their readings
are written here before the sampling.
"""
import numpy as np, itertools, random, json

R = [4, 3, 3, 3, 5, 2, 2, 3, 3]
NAMES = ["X", "S", "IC", "U", "NEC", "L", "SD", "DNc", "DNd"]
B = np.array(list(itertools.product(*[range(r) for r in R])), dtype=np.int8)
COL = [B[:, i] for i in range(9)]
T = np.array([2370, 2196, 1764, 1146, 1374, 558])


def prof(m):
    return np.array([m.sum(),
                     (m & (COL[4] >= 1)).sum(), (m & (COL[4] >= 2)).sum(),
                     (m & (COL[4] >= 3)).sum(),
                     (m & (COL[0] >= 2)).sum(), (m & (COL[0] == 3)).sum()])


def rule_mask(a, va, heads):
    bm = COL[a] >= va
    h = np.zeros(len(B), bool)
    for b, vb in heads:
        h |= COL[b] >= vb
    return ~(bm & ~h)


def setmask(rs):
    m = np.ones(len(B), bool)
    for a, va, heads in rs:
        m &= rule_mask(a, va, heads)
    return m


rng = random.Random(0)


def rand_rules(k):
    rs = []
    for _ in range(k):
        a = rng.randrange(9)
        va = rng.randrange(1, R[a])
        nh = rng.choice([1, 1, 2, 3])
        heads = []
        for _ in range(nh):
            b = rng.randrange(9)
            if b == a:
                continue
            heads.append([b, rng.randrange(1, R[b])])
        if heads:
            rs.append((a, va, heads))
    return rs


print("  SAMPLING RULE SETS AND WATCHING WHERE THE TWO NEC ERRORS LAND\n")
best = json.load(open("/home/claude/work/vi_best.json"))
bm = setmask([(a, va, h) for a, va, h in best["rules"]])
print(f"    vi_best reproduces its recorded profile: "
      f"{list(prof(bm)) == best['prof']}   {list(prof(bm))}\n")

pts, near = [], []
for trial in range(240000):
    rs = rand_rules(rng.choice([8, 12, 17, 17, 22]))
    if not rs:
        continue
    p = prof(setmask(rs))
    if p[0] == 0:
        continue
    d = p - T
    pts.append((d[0], d[2], d[3]))
    if abs(d[0]) <= 40:                    # cells at or near exact
        near.append((d[0], d[2], d[3]))

print(f"    rule sets sampled            : {len(pts)}")
print(f"    with |Δcells| ≤ 40           : {len(near)}")
if near:
    a = np.array(near)
    print(f"\n    among those, the two NEC errors:")
    print(f"      Δ(NEC≥2)  min {a[:,1].min():>6}  max {a[:,1].max():>6}  "
          f"mean {a[:,1].mean():>8.1f}")
    print(f"      Δ(NEC≥3)  min {a[:,2].min():>6}  max {a[:,2].max():>6}  "
          f"mean {a[:,2].mean():>8.1f}")
    both0 = ((a[:, 1] == 0) & (a[:, 2] == 0)).sum()
    oppos = ((a[:, 1] > 0) & (a[:, 2] < 0)).sum()
    same = ((a[:, 1] > 0) & (a[:, 2] > 0)).sum() + ((a[:, 1] < 0) & (a[:, 2] < 0)).sum()
    print(f"\n      both errors ZERO            : {both0}")
    print(f"      OPPOSITE signs (+ then −)   : {oppos}   ({100*oppos/len(a):.1f}%)")
    print(f"      SAME sign                   : {same}   ({100*same/len(a):.1f}%)")
    if len(a) > 3:
        c = np.corrcoef(a[:, 1], a[:, 2])[0, 1]
        print(f"      correlation of the two errors: {c:+.3f}")
    print(f"\n      vi_best sits at (+16, −9); best sampled distance to (0,0): "
          f"{np.min(np.abs(a[:,1]) + np.abs(a[:,2]))}")
print("\n  READ AGAINST THE TWO OUTCOMES DECLARED ABOVE.")
