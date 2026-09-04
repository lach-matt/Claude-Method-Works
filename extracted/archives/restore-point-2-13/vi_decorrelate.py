#!/usr/bin/env python3
"""vi_decorrelate.py — the ninth attack, aimed ACROSS the grain rather than along it.

Register 1494: within this rule family the two NEC errors move together at
r = +0.905, and the target needs them moved in OPPOSITE directions — sixteen
down on NEC >= 2 and nine up on NEC >= 3. Eight attacks moved along the grain.

So this does not search over rules. It searches over rules OF ONE KIND: those
whose removed box straddles the NEC = 2 boundary ASYMMETRICALLY, since only
those can separate the two marginals.

A removed box is  {A >= a} & {B1 < b1} & ... & {Bk < bk}. Its NEC extent is:
  · the whole NEC range, if NEC appears in neither body nor heads — then the box
    contributes PROPORTIONALLY to both marginals and moves them TOGETHER;
  · an upper interval, if NEC is the BODY letter;
  · a lower interval, if NEC appears among the HEADS.

Only the last two touch the marginals unequally. That is the whole idea, and it
follows from the box structure rather than from tuning.

SEEDED from vi_best.json (register 591: never search this blind), and the seed's
own profile is printed first so any change is visible against it.
"""
import numpy as np, itertools, random, json, copy

R = [4, 3, 3, 3, 5, 2, 2, 3, 3]
NEC = 4
B = np.array(list(itertools.product(*[range(r) for r in R])), dtype=np.int8)
COL = [B[:, i] for i in range(9)]
T = np.array([2370, 2196, 1764, 1146, 1374, 558])
W = np.array([4, 1, 3, 3, 1, 1])


def prof(m):
    return np.array([m.sum(),
                     (m & (COL[4] >= 1)).sum(), (m & (COL[4] >= 2)).sum(),
                     (m & (COL[4] >= 3)).sum(),
                     (m & (COL[0] >= 2)).sum(), (m & (COL[0] == 3)).sum()])


def rmask(r):
    a, va, heads = r
    bm = COL[a] >= va
    h = np.zeros(len(B), bool)
    for b, vb in heads:
        h |= COL[b] >= vb
    return ~(bm & ~h)


def mask(rs):
    m = np.ones(len(B), bool)
    for r in rs:
        m &= rmask(r)
    return m


def dist(rs):
    return int((W * np.abs(prof(mask(rs)) - T)).sum())


def touches_nec(r):
    a, va, heads = r
    return a == NEC or any(b == NEC for b, _ in heads)


seed = [(a, va, [list(x) for x in h]) for a, va, h in
        json.load(open("/home/claude/work/vi_best.json"))["rules"]]
p0 = prof(mask(seed))
print("  SEED — vi_best.json\n")
print(f"    profile {list(p0)}   target {list(T)}   distance {dist(seed)}")
print(f"    Δ = {list(p0 - T)}")
n_nec = sum(1 for r in seed if touches_nec(r))
print(f"\n    rules touching NEC in body or head: {n_nec} of {len(seed)}")
print(f"    rules NOT touching NEC             : {len(seed)-n_nec}"
      f"  — these move the two marginals TOGETHER\n")

rng = random.Random(7)


def nec_rule():
    """a rule whose removed box has an ASYMMETRIC NEC extent."""
    if rng.random() < 0.5:
        a, va = NEC, rng.randrange(1, R[NEC])          # NEC in the body
        heads = []
        for _ in range(rng.choice([1, 1, 2])):
            b = rng.randrange(9)
            if b != NEC:
                heads.append([b, rng.randrange(1, R[b])])
        return (a, va, heads) if heads else None
    a = rng.choice([i for i in range(9) if i != NEC])   # NEC among the heads
    va = rng.randrange(1, R[a])
    heads = [[NEC, rng.randrange(1, R[NEC])]]
    if rng.random() < 0.5:
        b = rng.randrange(9)
        if b != a:
            heads.append([b, rng.randrange(1, R[b])])
    return (a, va, heads)


best = list(seed); bd = dist(best)
print(f"  SEARCHING — every move adds, swaps or drops a NEC-ASYMMETRIC rule only\n")
for it in range(60000):
    cur = list(best)
    op = rng.random()
    if op < 0.45 or len(cur) < 4:
        r = nec_rule()
        if r:
            cur.append(r)
    elif op < 0.8:
        idx = [i for i, r in enumerate(cur) if touches_nec(r)]
        if not idx:
            continue
        r = nec_rule()
        if r:
            cur[rng.choice(idx)] = r
    else:
        idx = [i for i, r in enumerate(cur) if touches_nec(r)]
        if len(idx) < 2:
            continue
        cur.pop(rng.choice(idx))
    d = dist(cur)
    if d < bd:
        best, bd = cur, d
        p = prof(mask(best))
        print(f"    {it:>6}  distance {bd:>4}  rules {len(best):>3}  "
              f"Δ = {list(p - T)}")

p = prof(mask(best))
print(f"\n  RESULT\n")
print(f"    seed distance {dist(seed)} → {bd}")
print(f"    profile {list(p)}   target {list(T)}")
print(f"    Δ = {list(p - T)}   rules {len(best)}")
if bd < dist(seed):
    json.dump({"d": bd, "rules": [[a, va, h] for a, va, h in best],
               "prof": [int(x) for x in p]},
              open("/home/claude/work/vi_best2.json", "w"))
    print(f"\n    IMPROVED — saved to vi_best2.json")
else:
    print(f"\n    NO IMPROVEMENT. Aiming across the grain did not help either,")
    print(f"    which would make the correlation a property of the TARGET and")
    print(f"    not only of the search direction.")
