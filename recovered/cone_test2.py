"""Segment 1b — the equivalence test made two-sided.

Segment 1 agreed 16000/16000 but only 0.63% of draws were feasible, so it was
almost entirely a test of joint REFUSAL. Here tables are PLANTED: an entrant is
chosen as the true argmin of n - a*B0(p) for a drawn a and B0, so the table is
feasible by construction at B0. Random B are then tested against it, giving a
balanced mix of verdicts. Both sides must still agree exactly.
"""
from fractions import Fraction as F
import random
from cone import corridor, feasible_naive, inequalities, feasible_linear, random_increasing

def planted_table(rng, nsteps=25, nP=8):
    B0 = random_increasing(rng, nP)
    a = F(rng.randrange(1, 40), rng.randrange(1, 12))
    steps = []
    for _ in range(nsteps):
        cands = set()
        while len(cands) < rng.randrange(2, 6):
            cands.add((rng.randrange(1, 9), rng.randrange(0, nP)))
        cands = list(cands)
        vals = [(n - a * B0[p], (n, p)) for (n, p) in cands]
        vals.sort(key=lambda t: t[0])
        if vals[0][0] == vals[1][0]:
            continue                       # exact tie: no strict minimum, skip
        e = vals[0][1]
        rivals = [c for c in cands if c != e]
        steps.append((e, rivals))
    return steps, B0, a

if __name__ == "__main__":
    rng = random.Random(1969)              # Lowdin, 1969
    agree = disagree = 0
    nfeas = 0
    plant_ok = 0
    bad = []
    for trial in range(400):
        steps, B0, a = planted_table(rng)
        rows, refute = inequalities(steps)
        # the plant itself must be feasible under both tests
        if feasible_naive(steps, B0) and feasible_linear(rows, refute, B0):
            plant_ok += 1
        else:
            bad.append(("PLANT FAILED", trial))
        for _ in range(40):
            B = B0 if rng.random() < 0.15 else random_increasing(rng)
            x = feasible_naive(steps, B)
            y = feasible_linear(rows, refute, B)
            if x == y:
                agree += 1; nfeas += int(x)
            else:
                disagree += 1
                if len(bad) < 4: bad.append((steps, B, x, y))
    print(f"planted tables feasible at B0 : {plant_ok}/400")
    print(f"trials                        : {agree+disagree}")
    print(f"agree                         : {agree}")
    print(f"DISAGREE                      : {disagree}")
    print(f"feasible fraction             : {nfeas/max(agree,1):.4f}")
    for b in bad[:4]: print("FAULT:", b)
