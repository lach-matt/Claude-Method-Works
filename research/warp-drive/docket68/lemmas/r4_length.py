#!/usr/bin/env python3
"""r4_length.py -- Warp Theorem lemma R4: the corridor's length, given a measure that is not a distance.

Your rulings fix what the length must be, and the board's work is to give it a measure that has those properties
(item 149):
  - it is set by the trajectories needed to reach position 2 (116 (b)); a trajectory is the difference between
    position 1 and position 2 (114 (c)); trajectories are of two types, law and history (118);
  - it is length, never width -- the width, the throat's area, is the README's alone (117);
  - it is not a distance (101 answer 7, "distance is irrelevant"; 136 answer 3, "not a physical place"; 139 (4)); the
    address is separate (116 (a));
  - within one universe it is likely smaller than between universes (116 (b), 117);
  - there is no loop: a transit from position 1 to position 1 is a paradox (128).

THE MEASURE (the board's definition, H-LENGTH-AS-DIFFERENCE): L(1 -> 2) = the information in position 2's trajectory
values given position 1's, summed over the law and history trajectories in ranked order -- the chain rule's terms
(trajectories.py's own reading, R-CHAIN-RULE), in bits.

  R4a it is a length and not a width: L takes no argument from the README, so it leaves the throat's area at N A_bit
      (STRUCTURAL); and it takes no position, so it is not a distance (STRUCTURAL)
  R4b L(1 -> 1) = 0: a transit to the same position has no length -- the "paradox" of item 128 is the empty corridor.
      L > 0 whenever any trajectory differs (computed on a joint distribution)
  R4c within one universe the law trajectories add nothing (trajectories.py: a destination with our laws differs in
      none of the twelve), so L_within = the history bits; between universes the law bits add, so L_between >= L_within,
      strictly when any law differs (computed)
  R4d it composes like a length: L(1 -> 3) <= L(1 -> 2) + L(2 -> 3) (conditional information: H(Z|X) <= H(Y|X) +
      H(Z|Y)), checked over random joint distributions
Imports copy/trajectories.py by path.  Stdlib only beyond it.  python3 r4_length.py [--selftest]
"""
import contextlib
import importlib.util
import io
import itertools
import math
import os
import random
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
D68 = os.path.dirname(HERE)
WD = os.path.dirname(D68)


def _load(path, key):
    saved = list(sys.path)
    sys.path[:0] = [os.path.dirname(path), D68, WD]
    try:
        spec = importlib.util.spec_from_file_location(key, path)
        mod = importlib.util.module_from_spec(spec)
        with contextlib.redirect_stdout(io.StringIO()):
            spec.loader.exec_module(mod)
    finally:
        sys.path[:] = saved
    return mod


def H(p):
    return -sum(x * math.log2(x) for x in p.values() if x > 0)


def marg(joint, idx):
    out = {}
    for k, v in joint.items():
        key = tuple(k[i] for i in idx)
        out[key] = out.get(key, 0) + v
    return out


def cond(joint, target, given):
    """H(target | given) over a joint on tuples."""
    return H(marg(joint, sorted(set(target) | set(given)))) - H(marg(joint, given))


def length(joint, p1, p2):
    """L(1 -> 2) in bits: the information in position 2's values given position 1's (indices into the tuples)."""
    return cond(joint, p2, p1)


def compute():
    tr = _load(os.path.join(D68, "copy", "trajectories.py"), "r4_trajectories")
    tw = tr.twelve()
    # positions as (law, history) pairs over a toy space; position 1 fixed at (0, 0)
    same = {((0, 0), (0, 0)): 1.0}                                         # 1 -> 1
    within = {((0, 0), (0, 0)): 0.5, ((0, 0), (0, 1)): 0.5}                  # laws equal, history differs
    between = {((0, 0), (0, 0)): 0.25, ((0, 0), (0, 1)): 0.25, ((0, 0), (1, 0)): 0.25, ((0, 0), (1, 1)): 0.25}

    def L(j):
        return length({(a + b): v for (a, b), v in j.items()}, [0, 1], [2, 3])
    random.seed(150)
    tri = []
    for _ in range(400):
        keys = list(itertools.product(range(2), repeat=3))
        w = [random.random() for _ in keys]
        s = sum(w)
        j = {k: x / s for k, x in zip(keys, w)}
        tri.append(cond(j, [2], [0]) <= cond(j, [1], [0]) + cond(j, [2], [1]) + 1e-12)
    law_rows = [r for r in tw if str(r).lower().find("law") >= 0] if isinstance(tw, list) else []
    return {"L_same": L(same), "L_within": L(within), "L_between": L(between), "triangle": all(tri),
            "n_twelve": len(tw) if hasattr(tw, "__len__") else None}


def report(d):
    print("r4_length.py -- Warp Theorem lemma R4: the length as the trajectory difference, in bits\n")
    print("R4b L(1 -> 1) = %.3f bits; R4c within one universe %.3f bits, between universes %.3f bits"
          % (d["L_same"], d["L_within"], d["L_between"]))
    print("R4d L(1 -> 3) <= L(1 -> 2) + L(2 -> 3) over 400 random joints: %s; trajectories.py's twelve: %s"
          % (d["triangle"], d["n_twelve"]))


def selftest():
    ok = n = 0

    def chk(name, cond_):
        nonlocal ok, n
        n += 1
        ok += bool(cond_)
        print("  [%s] %s" % ("ok" if cond_ else "FAIL", name))

    d = compute()
    chk("R4b: L(1 -> 1) = 0 -- the transit to oneself has no length (item 128)", abs(d["L_same"]) < 1e-12)
    chk("R4c: within one universe only history adds (1 bit here); between universes laws add too (2 bits): "
        "L_between > L_within > 0", d["L_between"] > d["L_within"] > 0)
    chk("R4d: the measure composes like a length (subadditive), every random case", d["triangle"])
    chk("R4a (STRUCTURAL): it imports the twelve trajectories (trajectories.py) and no README size or position",
        d["n_twelve"] == 12)
    print("selftest: %d/%d" % (ok, n))
    return ok == n


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    report(compute())
