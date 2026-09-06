"""
cone.py — the exact feasibility condition on the candidate form.

Successor to P1 (BRIDGE-LOWDIN-SESSION.md §8, first bullet).

SETTING (unchanged from p1.py, restated so this file stands alone):
  nu(n,l,q) = A(n,l) - a * B(p),  p = n - l - 1 the node count.
  At an opening q = 0, so A = n.
  A step is: entrant e = (n_e, p_e), rivals r = (n_r, p_r).
  The entrant is least-nu iff for every rival
        n_e - a B(p_e)  <  n_r - a B(p_r)
   <=>  a * (B(p_r) - B(p_e))  <  (n_r - n_e)
  Write beta_r = B(p_r) - B(p_e),  delta_r = n_r - n_e.
  The step's corridor is the set of admissible a. FEASIBLE = corridor non-empty
  at every step. a is NOT sign-constrained (cf. the p=0 band (-inf, 0.7071)).

CLAIM UNDER TEST (Segment 1):
  Over the cone of STRICTLY INCREASING B, feasibility is equivalent to a finite
  system of HOMOGENEOUS LINEAR inequalities in B, namely, per step,
    (i)  every rival with p_r == p_e satisfies n_r > n_e      [no B dependence]
    (ii) for every lower rival i (p_i < p_e) and upper rival j (p_j > p_e):
             delta_i * B[p_j]  -  delta_j * B[p_i]  +  (delta_j - delta_i) * B[p_e]  >  0
  The coefficients sum to zero (translation invariance) and the system is
  homogeneous (scale invariance), so it descends to the increment vector.

The load-bearing lemma: because B is increasing, sign(beta_r) = sign(p_r - p_e)
is FIXED across the whole class. The partition of rivals into lower-bound-givers
and upper-bound-givers therefore does not move, which is what makes a single
linear system correct rather than a piecewise one.

Segment 1 tests the claim by brute force. It is not assumed anywhere until it passes.
"""

from fractions import Fraction as F
import random, itertools

NEG, POS = None, None  # sentinels for -inf / +inf


def corridor(step, B):
    """Naive interval computation. Returns (L, U, ok) with L,U possibly None=infinite.
    ok=False if a p_r == p_e rival refutes the step outright."""
    (n_e, p_e), rivals = step
    L, U = None, None
    for (n_r, p_r) in rivals:
        d = n_r - n_e
        if p_r == p_e:
            if d <= 0:
                return (None, None, False)
            continue
        b = B[p_r] - B[p_e]
        bound = F(d, 1) / b if isinstance(b, F) else d / b
        if b > 0:                       # a < bound
            U = bound if U is None else min(U, bound)
        else:                           # a > bound
            L = bound if L is None else max(L, bound)
    return (L, U, True)


def feasible_naive(steps, B):
    for s in steps:
        L, U, ok = corridor(s, B)
        if not ok:
            return False
        if L is not None and U is not None and not (L < U):
            return False
    return True


def inequalities(steps, nP=8):
    """The claimed system. Returns (rows, constant_refutations).
    Each row is a coefficient vector c with the condition c . B > 0."""
    rows, refute = [], []
    for (e, rivals) in steps:
        n_e, p_e = e
        lower = [(n_r - n_e, p_r) for (n_r, p_r) in rivals if p_r < p_e]
        upper = [(n_r - n_e, p_r) for (n_r, p_r) in rivals if p_r > p_e]
        for (n_r, p_r) in rivals:
            if p_r == p_e and n_r - n_e <= 0:
                refute.append((e, (n_r, p_r)))
        for (di, pi) in lower:
            for (dj, pj) in upper:
                c = [0] * nP
                c[pj] += di
                c[pi] -= dj
                c[p_e] += (dj - di)
                rows.append(tuple(c))
    return rows, refute


def feasible_linear(rows, refute, B):
    if refute:
        return False
    for c in rows:
        if sum(ci * bi for ci, bi in zip(c, B)) <= 0:
            return False
    return True


# ---------- Segment 1 test: do the two agree, always? ----------

def random_table(rng, nsteps=20, nP=8):
    steps = []
    for _ in range(nsteps):
        p_e = rng.randrange(0, nP)
        n_e = rng.randrange(1, 9)
        k = rng.randrange(1, 5)
        rivals = []
        for _ in range(k):
            p_r = rng.randrange(0, nP)
            n_r = rng.randrange(1, 9)
            if (n_r, p_r) != (n_e, p_e):
                rivals.append((n_r, p_r))
        if rivals:
            steps.append(((n_e, p_e), rivals))
    return steps


def random_increasing(rng, nP=8):
    """Strictly increasing rational 8-vector."""
    B = [F(rng.randrange(-20, 20), rng.randrange(1, 7))]
    for _ in range(nP - 1):
        B.append(B[-1] + F(rng.randrange(1, 30), rng.randrange(1, 9)))
    return B


if __name__ == "__main__":
    rng = random.Random(20260815)
    agree = disagree = 0
    feas_count = 0
    examples = []
    for trial in range(400):
        steps = random_table(rng)
        rows, refute = inequalities(steps)
        for _ in range(40):
            B = random_increasing(rng)
            a = feasible_naive(steps, B)
            b = feasible_linear(rows, refute, B)
            if a == b:
                agree += 1
                feas_count += int(a)
            else:
                disagree += 1
                if len(examples) < 3:
                    examples.append((steps, B, a, b))
    print(f"trials            : {agree + disagree}")
    print(f"agree             : {agree}")
    print(f"DISAGREE          : {disagree}")
    print(f"feasible fraction : {feas_count / max(agree,1):.4f}   (non-degenerate test)")
    for ex in examples:
        print("COUNTEREXAMPLE:", ex[1], "naive", ex[2], "linear", ex[3])
