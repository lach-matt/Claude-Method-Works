#!/usr/bin/env python3
"""sharp5.py -- [Hin26] sections 11.7-11.8 in the class: which terms of the late-time expansion of forward solutions
are eliminated, which are recorded, and the weights (N1STAR-PROOF.md section 10.46; ROUTES 4.48; D114).

[Hin26] Theorem 11.59 (p. 278): for f of K+ order 4 + eps_K there are unique modification parameters p' such that u =
chi_K u_exp + u~, u~ of K+ order 4 + eps_K, u_exp recording every term of lower K+ order -- the boost and centre-of-mass
remainders, the parameter change, the pure gauge states and the physical states s2, v2, s3, v3 (11.196b) -- after the
pure gauge terms "that have t*-order <= 2 + eps_K (so <= 2)" are eliminated (p. 289, (3)).  A root mu fed by t*^-alpha
at iota+ gives K+ order alpha - mu (window5.py W2).  In the class (10.43) the second order pole is absent (10.45): f
needs K+ order 3 + eps_K, u~ has it, and u_exp records the terms below it.

  K1 (computed, exact) The class's types among window5.py's (kind, l), from class5.py's counts: scalar at l = 0, 2, 4,
     6, tensor at l = 2, 4; no vector type, no odd l.  Control: without the reflections the vector type enters.
  K2 (computed; numerical, mpmath at 50 digits, at lin5.py's point) Their roots of det N_L in [-3, 0]: s0 c0 e0; s2 c-1
     c-2 e-2 e0; s4 e-2; t2 e-2; none at s6, t4 -- the class roots' distances below the integer (about 10^-6 at the
     point; lin5.py's scalar-type determinant takes most of the run), and the least iota+
     exponent alpha_min = 3/2 + (1 - e_Ups) gam_Ups (10.44(e)).  Control: s4 claimed to have no root in [-3, 0].
  K3 (computed, exact) The bookkeeping, for every iota+ exponent alpha in [alpha_min, 3] (a grid of 151 points, the
     orders linear in alpha): a state is recorded with k = floor(3 - order) generalized companions while its order is
     at most 3, and eliminated if pure gauge of order at most 2 (the class roots: below 2).  Eliminated: within {s0 e0,
     s0 c0, s2 e0}, all three at alpha_min; recorded: within those and s2 c-1; no physical state at any alpha; each
     recorded term's L_b-image of K+ order above 3 (his (11.232), Lemma 11.65).  Control: four dimensions at alpha =
     1, threshold 4, gives his eight eliminated parameters ((11.197); p. 289, (3)) and his physical s2, v2, s3, v3 with
     1, 1, 0, 0 companions ((11.196b)); mutant: the class at alpha = 1 claimed to record no physical state.
  K4 (computed, at the point) The weights: his I+ remainder weight 3 + eps_I lies in the five-dimensional non-resonant
     gap 3/2 + 2 gam_Ups < z < 3/2 + (1 - e_C)(1 - v) gam_C (iplus5.py P2), and his iota+ remainder 3 + eps_+ feeds
     only K+ orders above 3 in the class.  Control: the radiative order 3/2 claimed as I+ weight.

sympy, mpmath; imports window5.py, class5.py, iplus5.py.
python3 sharp5.py [--selftest | --mutants]   (about nine minutes each, K2's roots)
"""
import sys
import time

import sympy as sp

from damping5 import Checklist
import window5 as W
import class5 as C5

EPS = sp.Symbol("eps", positive=True)


# ------------------------------------------------------------------------------------------------- K1
def class_types(reflections=True, lmax=6):
    """the (kind, l) of window5.py's lists with a G-fixed harmonic"""
    out = [("s", l) for l in range(lmax + 1) if C5.scalar_count(l)]
    if C5.vector_count(reflections):
        out += [("v", l) for l in range(1, lmax)]
    out += [("t", l) for l in range(2, lmax) if C5.tensor_count(l, l // 2 + 1)]
    return out


SPEC_G = {key: W.SPEC5[key] for key in (("s", 0), ("s", 2), ("s", 4), ("s", 6), ("t", 2), ("t", 4))}


def k1(control=0, verbose=False):
    chk = Checklist(verbose, quiet=control != 0)
    got = class_types(reflections=control != 1)
    chk(f"G-fixed types among window5.py's: {got} (scalar at even l, tensor at even l >= 2, no vector)",
        sorted(got) == sorted(SPEC_G))
    return chk.ok


# ------------------------------------------------------------------------------------------------- K2
def alpha_min():
    import iplus5
    return sp.Rational(3, 2) + (1 - iplus5.eU) * iplus5.gU


def k2(control=0, verbose=False):
    chk = Checklist(verbose, quiet=control != 0)
    spec = dict(SPEC_G)
    if control == 1:
        spec[("s", 4)] = []
    got = {key: W.window(4, *key) for key in SPEC_G}
    rep = "; ".join(f"{a}{b}: {' '.join(got[(a, b)][0]) or '-'}" for (a, b) in got)
    chk(f"roots in [-3, 0], real, class roots of box^Ups less than 1/4 below the integer: {rep}",
        all(ok for _, ok, _ in got.values()) and all(sorted(spec[key]) == got[key][0] for key in spec))
    dist = {}
    for (a, b) in (("s", 0), ("s", 2)):
        for q in W.roots(4, a, b)["L"]:
            k = int(W.mpm.ceil(q.real))
            if -3 <= q.real < 0 and abs(q.real - round(q.real)) > 1e-30:
                dist[f"{a}{b} c{k}"] = float(k - q.real)
    chk(f"the class roots' distances below the integer: {dist}", set(dist) == {"s0 c0", "s2 c-1", "s2 c-2"}
        and all(0 < d < 0.25 for d in dist.values()))
    import iplus5
    am = alpha_min()
    chk(f"alpha_min = {am} = {float(am.subs(iplus5.POINT)):.6g} at the point (10.44(e))",
        1 < am.subs(iplus5.POINT) < sp.Rational(3, 2) + sp.Rational(1, 4))
    return chk.ok


# ------------------------------------------------------------------------------------------------- K3
def count(alpha, t, kind, thr):
    """k = floor(thr - order), None if the state is not recorded (order above thr); the class roots' eps small"""
    q = thr - W.order(alpha, t, kind).subs(EPS, 0)
    if kind == "class":
        return None if q <= 0 else int(sp.ceiling(q)) - 1
    return None if q < 0 else int(sp.floor(q))


def book(spec, alpha, thr=3, gauge=2, s1v1_gauge=True):
    """(eliminated, recorded {state: k}, physical recorded) at iota+ exponent alpha"""
    elim, rec, phys = set(), {}, {}
    for s, t, kind in W.states(spec):
        k = count(alpha, t, kind, thr)
        if k is None:
            continue
        o = W.order(alpha, t, kind).subs(EPS, 0)
        pure = kind in ("gauge", "class") or (s1v1_gauge and kind in ("s1", "v1"))
        if pure and (o < gauge if kind == "class" else o <= gauge):
            elim.add((s, t))
        (phys if kind == "phys" else rec)[(s, t)] = k
    return elim, rec, phys


def k3(control=0, verbose=False):
    chk = Checklist(verbose, quiet=control != 0)
    am = alpha_min()
    import iplus5
    a0 = am.subs(iplus5.POINT)
    grid = [a0 + (3 - a0) * sp.Rational(m, 150) for m in range(151)]
    E3 = {("s0", "e0"), ("s0", "c0"), ("s2", "e0")}
    ok, lb = True, True
    for al in grid:
        el, rec, ph = book(SPEC_G, al)
        ok &= el <= E3 and set(rec) <= E3 | {("s2", "c-1")} and not ph
        lb &= all(W.order(al, t, "class" if t[0] == "c" else "gauge").subs(EPS, 0) + k + 1 > 3
                  for (s, t), k in rec.items())
    el0, rec0, ph0 = book(SPEC_G, a0)
    chk(f"alpha = alpha_min: eliminated {sorted(el0)}; recorded {rec0}; physical {ph0 or 'none'}",
        el0 == E3 and rec0 == {("s0", "e0"): 1, ("s0", "c0"): 1, ("s2", "e0"): 1, ("s2", "c-1"): 0} and not ph0)
    chk("alpha in [alpha_min, 3] (151 points): eliminated within {s0 e0, s0 c0, s2 e0}, recorded within those and s2 "
        "c-1, no physical state; each recorded term's L_b-image of K+ order above 3", ok and lb)
    al = sp.Integer(1)
    el4, rec4, ph4 = book(W.SPEC4, al, thr=4)
    his8 = {("s1", "e-1"), ("v1", "e-1"), ("s0", "e0"), ("s2", "e0"), ("s0", "c0"), ("s1", "c0"), ("s3", "e-1"),
            ("v2", "e-1")}
    chk(f"control: four dimensions, alpha = 1, threshold 4: eliminated {sorted(el4)} -- his eight ((11.197), p. 289); "
        f"physical {ph4} -- his s2, v2, s3, v3 of (11.196b)",
        el4 == his8 and ph4 == {("s2", "e-2"): 1, ("v2", "e-2"): 1, ("s3", "e-3"): 0, ("v3", "e-3"): 0})
    a1 = al if control == 1 else a0
    _, _, ph1 = book(SPEC_G, a1)
    chk(f"the class at alpha = {a1}: physical states recorded {ph1 or 'none'}", not ph1)
    return chk.ok


# ------------------------------------------------------------------------------------------------- K4
def k4(control=0, verbose=False):
    chk = Checklist(verbose, quiet=control != 0)
    import iplus5
    v, eC, gC, gU = iplus5.v, iplus5.eC, iplus5.gC, iplus5.gU
    pt = iplus5.POINT
    epsI = sp.Rational(1, 10**6)
    lI = sp.Rational(3, 2) + gU if control == 1 else 3 + epsI
    lo, hi = (sp.Rational(3, 2) + 2 * gU).subs(pt), (sp.Rational(3, 2) + (1 - eC) * (1 - v) * gC).subs(pt)
    lo4, hi4 = (1 + 2 * gU).subs(pt), (1 + (1 - eC) * (1 - v) * gC).subs(pt)
    lIv = lI.subs(pt)
    chk(f"I+ weight {lIv} in the five-dimensional gap ({lo}, {float(hi):.6g}) and in his ({lo4}, {float(hi4):.6g})",
        lo < lIv < hi and lo4 < lIv < hi4)
    beta = 3 + sp.Rational(1, 10**6)
    feed = min(W.order(beta, t, kind).subs(EPS, 0) for _, t, kind in W.states(SPEC_G) if t[1:] in ("0", "-1", "-2"))
    chk(f"iota+ remainder 3 + eps_+ feeds K+ orders >= {feed} > 3 in the class", feed > 3)
    return chk.ok


CHECKS = [("K1 the class's types: scalar at l = 0, 2, 4, 6, tensor at l = 2, 4 (class5.py's counts)", k1),
          ("K2 their roots in [-3, 0] at the point; class roots' distances; alpha_min = 3/2 + (1 - e_U) gam_U", k2),
          ("K3 the bookkeeping: eliminated s0 e0, s0 c0, s2 e0; recorded with s2 c-1; no physical state", k3),
          ("K4 the weights: 3 + eps_I in the five-dimensional I+ gap; 3 + eps_+ at iota+ harmless", k4)]


def run(only=None, verbose=False):
    ok = True
    for k, (name, f) in enumerate(CHECKS, 1):
        if only and k != only:
            continue
        t0 = time.time()
        res = f(0, verbose)
        ok &= res
        print(f"{name[:104]:<104} {'PASS' if res else 'FAIL'} {time.time() - t0:3.0f}s", flush=True)
    print(f"sharp5.py: {len(CHECKS) if ok else 'not all'}/{len(CHECKS)}")
    return ok


def mutants():
    caught = total = 0
    for name, f in CHECKS:
        total += 1
        res = f(1, False)
        caught += not res
        print(f"mutant 1 of {name[:2]}: {'caught' if not res else 'NOT caught'}", flush=True)
    print(f"sharp5.py mutants: {caught}/{total}")
    return caught == total


if __name__ == "__main__":
    args = sys.argv[1:]
    vb = "--verbose" in args
    if "--selftest" in args:
        sys.exit(0 if run(verbose=vb) else 1)
    elif "--mutants" in args:
        sys.exit(0 if mutants() else 1)
    elif "--only" in args:
        sys.exit(0 if run(int(args[args.index("--only") + 1]), vb) else 1)
    print(__doc__)
