#!/usr/bin/env python3
"""window5.py -- [Hin26]'s window [-3, 0] in five dimensions: which large indicial roots of the linearized gauge-fixed
Einstein operator, and which of their generalized states, the late-time expansion needs (N1STAR-PROOF.md section 10.35;
ROUTES-OPEN.md 4.36; D93).  Labels: computed (exact, sympy; numerical, mpmath at 50 digits, where said), deduced, READ.

[Hin26] (arXiv:2606.28253v2): a term t*^-alpha at iota+ meets a large indicial root mu of L-hat_b(0) at K+ as
t*^(-alpha + mu) ((1.23), p. 17); the nonlinear iteration needs u at O(t*^(-2-eps_K)), "due to the 2-admissibility of
L_b" (p. 273), the 2 being "the order of the 'pole' of L-hat_b(sigma)^-1 at sigma = 0" (p. 34), and so sources at
O(t*^(-4-eps_K)): every contribution to u not of size O(t*^(-4-eps_K)) must have its spatial dependence given by large
zero energy states (p. 273), and the pure gauge ones without t*^(-2-eps_K)-decay are eliminated (p. 218).  "Sources f
arising in the nonlinear iteration furthermore turn out to also cause a t*^-1-term at iota+" (p. 28; footnote 27: the
trace-free spherical part's radiation field couples into the (dt*)^2 component, the (7, 6)-entry of A_h in (5.28)), and
"The smallest lam for which we will apply this result is lam = 1, in which case the remainder in (9.41) has more than 4
orders of decay at K+" (p. 177): hence his roots with real part in [-3, 0] and Proposition 9.9's expansion (9.32).

  W1 (computed; numerical, mpmath at 50 digits, at lin5.py's point) The roots of det N_L itself with real part in [-3,
     0] (lin5.py's determinant, no cancellation rule), by type -- s0, s1, sl (2 <= l <= 6), v1, vl (2 <= l <= 5), and in
     five dimensions tl (2 <= l <= 5) -- each real and either an exact integer (the physical -l, box^Ups's -l + 2 at sl
     and -l + 1 at vl, s0's 0) or a class root less than 1/4 below one and a root of det N_Ups(lam - 1); the roots of
     det N_C(lam + 1) meet the window only at four-dimensional s0's 0 (box^C's root 1 shifted by -1, which his Lemma 8.4
     lists as 0, p. 149), and in five dimensions not at all.  Four dimensions (n = 3, trace weight 1) gives
     exactly his Lemma 8.4's roots in [-3, 0] (p. 149), which are (9.32)'s: the class roots -lam_sl,l+j + 1 for 0 <= l <=
     3, j = 0, 1, 1 <= l + j <= 3, the s0 and s2 root 0, -l + 2 at sl (l = 2, ..., 5), -l + 1 at vl (l = 2, 3, 4), -1 at
     s1 and v1, -2 at s2 and v2, -3 at s3 and v3; five dimensions the same and t2's -2 and t3's -3.  Controls: the five
     dimensional roots claimed without the tensor types; no root from box^C claimed in four dimensions (D93's claim).
  W2 (computed, exact) The bookkeeping.  A root mu fed by t*^-alpha at iota+ gives a(t*) = t*^(-alpha + mu) and the
     generalized companions a^(j)(t*), of K+ order alpha - mu + j (the exceptional s1 and v1 at -1: alpha - 1 + j and
     alpha + j, his a_s1 and a_v1 of (9.39a)); a state is needed while that order is at most 4, with k = floor(4 - order)
     companions, and the pure gauge ones of order at most 2 are eliminated.  At alpha = 1 this gives (9.32)'s orders --
     s1 4, v1 3, s0 3, -l + 2 at sl 5 - l, -l + 1 at vl 4 - l, s2 and v2 1, s3 and v3 0 -- and at most his 2 at the class
     roots.  For every alpha in (1, 2] the physical states needed are s2, v2 and t2 at -2, without companions, and none
     at l >= 3; at alpha = 2 the full list; at alpha = 3/2, the radiative order of W3 at d = 4, the window [-5/2, 0], the
     same physical states, and the pure gauge list longer by s2's and s3's class roots just below -2 (k = 0), with s0's
     and s1's class roots just below 0 at k = 2 and s1's and s2's just below -1 at k = 1 (D95).  Control: alpha = 1 with
     s3 and v3 claimed unneeded.
  W3 (computed, exact) In d + 1 dimensions the flat wave operator maps r^-p a(t - r) S, S a degree-l harmonic on
     S^(d-1), to (2p - d + 1) a' r^(-p-1) S + (p (p - d + 2) - l (l + d - 2)) a r^(-p-2) S exactly: the radiative order p
     = (d - 1)/2 kills the first term, the Coulombic order p = d - 2 at l = 0 the second, leaving (d - 3) a' r^(-d+1) --
     so a source quadratic in radiation fields, of order r^(-(d-1)), is met at the Coulombic order by an a with a'
     proportional to it, accumulating along I+: at d = 4 at r^-2, the order of Theorem M(c)'s mass aspect (bondi5.py B1);
     at d = 3 the two orders are one, 1, and the coefficient vanishes, which is why his (dt*)^2 component carries its
     r^-1 term through its gauge shift 2 gam_Ups (p. 85).  Control: p = (d - 1)/2 claimed to leave the a' term.

Deduced, not computed here (N1STAR-PROOF.md 10.35): for any iota+ order alpha_5 in (1, 2] the physical states needed
are s2, v2, t2 at -2 alone (W2): 10.34's l = 3 states and his generalized s2, v2 states are not needed; the pole order
is 2, on a reading, the s1 chains ending at the nonzero centre-of-mass pairing of Proposition 10.29(iii), so sources
need t*^(-4-eps_K) as in four dimensions and the window is [alpha_5 - 4, 0].  Which alpha_5 is a reading: 2, the mass
aspect's t*^-2 (W3 with Theorem M(c)), if nothing decays more slowly at iota+; 3/2 + O(gam), conservatively, if, as
his index sets at I+ do in four dimensions, the iteration carries the radiative order there (D95).

READ.  [Hin26] pp. 17-18 ((1.23)-(1.25)), 27-30 (section 1.4.3, footnotes 27-28), 32 (section 1.4.4), 34 (the "2" in
2-admissibility, footnote 35), 37, 85 (Definition 5.2), 92-93 (Proposition 5.11, (5.27)-(5.28)), 117 (Lemma 6.6), 128,
149 (Lemma 8.4), 169 (Proposition 9.4), 173-177 (Definition 9.8, Proposition 9.9, (9.32), Proposition 9.11,
(9.39a)-(9.39b)), 199 (Theorem 10.1), 218, 225 (Corollary 11.10), 228 (the proof of Lemma 11.15), 248 (the proof of
Proposition 11.32: E-sharp_+ "with smallest elements (1, 0) and (1 + (1 - e_Ups) gam_Ups, 0)"), 273, 279 (Remark
11.60), 324; also 16 ((1.19)) and 31 (Figure 1.7); alphaXiv, 2026-10-24.

sympy, mpmath; imports lin5.py.  python3 window5.py [--selftest | --mutants]   (--verbose lists every sub-check)
"""
import sys
import time

import mpmath as mpm
import sympy as sp

from damping5 import Checklist

# ------------------------------------------------------------------------------------------------- W1
SPEC4 = {("s", 0): ["c0", "e0"], ("s", 1): ["c0", "c-1", "e-1"], ("s", 2): ["c-1", "c-2", "e-2", "e0"],
         ("s", 3): ["c-2", "e-3", "e-1"], ("s", 4): ["e-2"], ("s", 5): ["e-3"], ("s", 6): [],
         ("v", 1): ["e-1"], ("v", 2): ["e-2", "e-1"], ("v", 3): ["e-3", "e-2"], ("v", 4): ["e-3"], ("v", 5): []}
SPEC5 = {**SPEC4, ("t", 2): ["e-2"], ("t", 3): ["e-3"], ("t", 4): [], ("t", 5): []}
_R = {}


def roots(n, kind, L):
    """the roots of det N_L itself at lin5.py's point (no cancellation rule), and, for attribution only, those of its
    factors det N_Ups(lam - 1) and det N_C(lam + 1): {"L": [...], "U": [...], "C": [...]}"""
    if (n, kind, L) in _R:
        return _R[(n, kind, L)]
    import lin5
    mpm.mp.dps = 50
    lam, l = lin5.lam, lin5.l
    typ = f"{kind}{L}" if L <= 1 else f"{kind}l"
    dU, dC, dL, _, _ = lin5.dets(n, typ)

    def rts(e):
        e = sp.sympify(e)
        if not e.has(lam):
            return []
        P = sp.Poly(sp.expand(sp.numer(sp.together(e.subs(l, L).subs(lin5.POINT)))), lam)
        return [complex(q) for q in mpm.polyroots([mpm.mpf(sp.Rational(c)) for c in P.all_coeffs()], maxsteps=600,
                                                  extraprec=600)]
    _R[(n, kind, L)] = {"L": rts(dL), "U": rts(sp.sympify(dU).subs(lam, lam - 1)),
                        "C": rts(sp.sympify(dC).subs(lam, lam + 1))}
    return _R[(n, kind, L)]


def window(n, kind, L, lo=-3):
    """the roots of det N_L with real part in [lo, 0], as 'e<k>' (exact integer) or 'c<k>' (less than 1/4 below k);
    whether each is real and each class root a root of det N_Ups(lam - 1); and det N_C(lam + 1)'s roots in [lo, 0]"""
    tags, ok = [], True
    rs = roots(n, kind, L)
    inw = lambda q: lo - 1e-20 <= q.real <= 1e-20
    for q in rs["L"]:
        if not inw(q):
            continue
        k = round(q.real)
        ok &= abs(q.imag) < 1e-30
        if abs(q - k) < 1e-30:
            tags.append(f"e{k}")
        else:
            k = int(mpm.ceil(q.real))
            ok &= k - 0.25 < q.real < k and any(abs(q - u) < 1e-25 for u in rs["U"])
            tags.append(f"c{k}")
    return sorted(tags), ok, [q.real for q in rs["C"] if inw(q)]


def w1(control=0, verbose=False):
    chk = Checklist(verbose, quiet=control != 0)
    cin = {}
    for n, spec in ((3, SPEC4), (4, SPEC5)):
        if control == 1 and n == 4:
            spec = {k: v for k, v in spec.items() if k[0] != "t"}
        got = {key: window(n, *key) for key in SPEC5 if not (n == 3 and key[0] == "t")}
        good = all(ok for _, ok, _ in got.values()) and set(got) == set(spec)
        good &= all(sorted(spec[key]) == got[key][0] for key in spec if key in got)
        rep = "; ".join(f"{a}{b}: {' '.join(got[(a, b)][0]) or '-'}" for (a, b) in got)
        chk(f"n + 1 = {n + 1}: the roots of det N_L itself in [-3, 0] (e exact, c a class root of box^Ups just below), "
            f"real, as Lemma 8.4{' and (9.32)' if n == 3 else ''} {'has them' if n == 3 else 'with t2, t3 added'}: "
            f"{rep}", good)
        cin[n] = {key: c for key, (_, _, c) in got.items() if c}
    want = {3: [("s", 0)], 4: []} if control != 2 else {3: [], 4: []}
    cgood = sorted(cin[3]) == want[3] and sorted(cin[4]) == want[4]
    cgood &= all(abs(q) < 1e-30 for c in cin[3].values() for q in c) and sum(len(c) for c in cin[3].values()) == 1
    chk(f"det N_C(lam + 1)'s roots in [-3, 0]: four dimensions {cin[3]} (s0's 0, box^C's root 1 shifted), five "
        f"dimensions {cin[4] or 'none'}" + (" (control: none claimed in four dimensions)" if control == 2 else ""),
        cgood)
    return chk.ok


# ------------------------------------------------------------------------------------------------- W2
def states(spec):
    """(label, root tag, kind): kind phys (-l, l >= 2), s1/v1 (the exceptional -1), class, or gauge"""
    out = []
    for (a, L), tags in spec.items():
        for t in tags:
            k = int(t[1:])
            if t[0] == "c":
                kind = "class"
            elif (a, L) in (("s", 1), ("v", 1)) and k == -1:
                kind = f"{a}1"
            elif L >= 2 and k == -L:
                kind = "phys"
            else:
                kind = "gauge"
            out.append((f"{a}{L}", t, kind))
    return out


def order(alpha, t, kind):
    """the K+ order of a state's leading term, eps standing for the class roots' small distance below the integer"""
    eps = sp.Symbol("eps", positive=True)
    k = int(t[1:])
    if kind == "s1":
        return alpha - 1
    if kind == "v1":
        return alpha
    return alpha - k + (eps if kind == "class" else 0)


def companions(alpha, t, kind):
    """k = floor(4 - order), None if the state is not needed (order > 4), the class roots' eps small and positive"""
    o = order(alpha, t, kind)
    eps = sp.Symbol("eps", positive=True)
    q = 4 - o.subs(eps, 0)
    if kind == "class":
        return None if q <= 0 else int(sp.ceiling(q)) - 1
    return None if q < 0 else int(sp.floor(q))


HIS = {("s1", "e-1"): 4, ("v1", "e-1"): 3, ("s0", "e0"): 3, ("s2", "e0"): 3, ("s3", "e-1"): 2, ("s4", "e-2"): 1,
       ("s5", "e-3"): 0, ("v2", "e-1"): 2, ("v3", "e-2"): 1, ("v4", "e-3"): 0, ("s2", "e-2"): 1, ("v2", "e-2"): 1,
       ("s3", "e-3"): 0, ("v3", "e-3"): 0}


def w2(control=0, verbose=False):
    chk = Checklist(verbose, quiet=control != 0)
    one = sp.Integer(1)
    st4 = states(SPEC4)
    ks = {(s, t): companions(one, t, kind) for s, t, kind in st4}
    if control == 1:
        ks[("s3", "e-3")] = ks[("v3", "e-3")] = None
    good = all(ks[key] == v for key, v in HIS.items())
    good &= all(ks[(s, t)] is not None and ks[(s, t)] <= 2 for s, t, kind in st4 if kind == "class")
    good &= all(v is not None for v in ks.values())
    chk("alpha = 1: (9.32)'s orders -- s1 4, v1 3, s0 3, -l + 2 at sl 5 - l, -l + 1 at vl 4 - l, s2 and v2 1, s3 and "
        "v3 0 -- and at most 2 at his six class roots; every root of [-3, 0] needed", good)
    st5 = states(SPEC5)
    grid = [one + sp.Rational(m, 100) for m in range(1, 101)]
    phys = []
    ok = True
    for al in grid:
        need = {(s, t): companions(al, t, kind) for s, t, kind in st5 if kind == "phys"}
        need = {key: v for key, v in need.items() if v is not None}
        ok &= need == {("s2", "e-2"): 0, ("v2", "e-2"): 0, ("t2", "e-2"): 0}
        phys = need
    lin = all(sp.simplify(order(sp.Symbol("a"), t, kind) - order(sp.Integer(0), t, kind) - sp.Symbol("a")) == 0
              for _, t, kind in st5)
    chk(f"alpha in (1, 2] (alpha = 1 + m/100, m = 1, ..., 100, the orders linear in alpha): the physical states "
        f"needed are {sorted(phys)} -- s2, v2, t2 at -2 without companions, none at l >= 3", ok and lin)
    two = sp.Integer(2)
    full = [(s, t, kind, companions(two, t, kind)) for s, t, kind in st5]
    needed = [(s, t, k) for s, t, kind, k in full if k is not None]
    gauge = [(s, t) for s, t, kind, k in full if kind != "phys" and k is not None
             and sp.simplify(order(two, t, kind).subs(sp.Symbol("eps", positive=True), 0) - 2) <= 0]
    want_gauge = {("s0", "e0"), ("s1", "e-1"), ("s2", "e0"), ("v1", "e-1"), ("s0", "c0"), ("s1", "c0")}
    rep = ", ".join(f"{s} {t} k={k}" for s, t, k in needed)
    chk(f"alpha = 2: the window [-2, 0]: {rep}; pure gauge of order at most 2 (the class roots at 2 + eps): "
        f"{sorted(gauge)}", set(gauge) == want_gauge and all(t[1:] != "-3" for _, t, _ in needed))
    ok32 = True
    for al in (sp.Rational(3, 2), sp.Rational(3, 2) + sp.Rational(1, 100)):
        k32 = {(s, t): companions(al, t, kind) for s, t, kind in st5}
        k2 = {(s, t): k for s, t, kind, k in full}
        more = {key: v for key, v in k32.items() if v is not None and k2[key] is None}
        up = {key: (k2[key], v) for key, v in k32.items() if v is not None and k2[key] is not None and v != k2[key]}
        ok32 &= more == {("s2", "c-2"): 0, ("s3", "c-2"): 0}
        ok32 &= up == {("s0", "c0"): (1, 2), ("s1", "c0"): (1, 2), ("s1", "c-1"): (0, 1), ("s2", "c-1"): (0, 1)}
        ok32 &= all(k2[key] is None or k32[key] is not None for key in k2)
    chk(f"alpha = 3/2 and 3/2 + 1/100 (the radiative order, W3 at d = 4): the window [-5/2, 0]; beyond alpha = 2's list "
        f"{sorted(more)} at k = 0, and companions raised {up}; the physical states unchanged", ok32)
    return chk.ok


# ------------------------------------------------------------------------------------------------- W3
def w3(control=0, verbose=False):
    chk = Checklist(verbose, quiet=control != 0)
    t, r, p, d, l = sp.symbols("t r p d l", positive=True)
    a = sp.Function("a")
    phi = r**-p * a(t - r)
    box = -sp.diff(phi, t, 2) + sp.diff(phi, r, 2) + (d - 1) / r * sp.diff(phi, r) - l * (l + d - 2) / r**2 * phi
    u = sp.Symbol("u")
    form = ((2 * p - d + 1) * sp.Subs(sp.diff(a(u), u), u, t - r).doit() * r**(-p - 1)
            + (p * (p - d + 2) - l * (l + d - 2)) * a(t - r) * r**(-p - 2))
    exact = sp.simplify(sp.expand(box - form.doit())) == 0
    c1 = sp.expand(2 * p - d + 1)
    c2 = sp.expand(p * (p - d + 2) - l * (l + d - 2))
    rad = c1.subs({d: 4, p: sp.Rational(3, 2)}) == 0 and c1.subs({d: 3, p: 1}) == 0
    if control == 1:
        rad = c1.subs({d: 4, p: sp.Rational(3, 2)}) != 0
    coul = c2.subs({d: 4, p: 2, l: 0}) == 0 and c1.subs({d: 4, p: 2}) == 1 and c2.subs({d: 3, p: 1, l: 0}) == 0
    one = c1.subs({d: 3, p: 1}) == 0
    chk(f"box(r^-p a(t - r) S) = ({c1}) a' r^(-p-1) S + ({sp.factor(c2)}) a r^(-p-2) S exactly; the radiative order "
        f"p = (d - 1)/2 kills the first, the Coulombic p = d - 2 at l = 0 the second, leaving (d - 3) a': 1 at d = 4 "
        f"(r^-2), 0 at d = 3 (r^-1, the two orders one)", exact and rad and coul and one)
    return chk.ok


CHECKS = [("W1 lin5.py's roots in [-3, 0], four dimensions (his Lemma 8.4, (9.32)) and five (the same and t2, t3)",
           w1, 2),
          ("W2 the bookkeeping: alpha = 1 gives (9.32); alpha in (1, 2] needs s2, v2, t2 at -2 alone; alpha = 2 in full",
           w2, 1),
          ("W3 the radiative and Coulombic orders of the flat wave operator in d + 1 dimensions; d - 3 at the latter",
           w3, 1)]


def selftest(verbose=False):
    ok_all = True
    for name, fn, nc in CHECKS:
        t0 = time.time()
        good = fn(verbose=verbose)
        control = any(fn(control=k) for k in range(1, nc + 1))
        state = "PASS" if good and not control else "FAIL"
        ok_all &= state == "PASS"
        print(f"{name:<112} {state}  {time.time() - t0:.0f}s" + ("" if not control else "  (control passed: vacuous)"),
              flush=True)
    print(f"window5.py: {len(CHECKS) if ok_all else 'FAILED'}/{len(CHECKS)}")
    return ok_all


def mutants():
    caught = total = 0
    for name, fn, nc in CHECKS:
        for k in range(1, nc + 1):
            total += 1
            res = fn(control=k)
            caught += (not res)
            print(f"mutant {k} of {name[:2]}: {'caught' if not res else 'NOT caught'}", flush=True)
    print(f"window5.py mutants: {caught}/{total}")
    return caught == total


if __name__ == "__main__":
    args = sys.argv[1:]
    if "--mutants" in args:
        sys.exit(0 if mutants() else 1)
    if "--only" in args:
        k = int(args[args.index("--only") + 1])
        name, fn, _ = CHECKS[k - 1]
        print(name, fn(verbose=True))
        sys.exit(0)
    sys.exit(0 if selftest(verbose="--verbose" in args) else 1)
