#!/usr/bin/env python3
"""ext5.py -- [Hin26] section 5 at n = 4 (proof5/PART-III-C-EXTERIOR.md): the leading part of the linearised
gauge-fixed Einstein operator at the corner I_0 cap I+, the corner coordinates, and the index-set bookkeeping of
Definition 5.3, Proposition 5.14 and (5.43) at n = 4.  Labels: computed (exact, sympy; exact rational arithmetic).

  E1 (the corner coordinates) With x^1 = t - |x|, rho_0 = 1/(2 - x^1), rho_I = (2 - x^1)/|x| (III.B (2.2)) and
     t_* = x^1 + C' - 8 mu_0/|x| (III.B (3.6)), exactly: d_(t_*) = rho_0 (X_0 - X_I) at fixed (rho, omega), and
     rho d_rho = X_I + 8 mu_0 rho_0^2 rho_I (X_0 - X_I) at fixed (t_*, omega), X_0 = rho_0 d_(rho_0), X_I = rho_I
     d_(rho_I).  For Tangherlini's null coordinates (III.B (4.1)-(4.3)), with d_0 r = f/2 and d_1 r = -f/2:
     d_0 = -(f/2) rho_0 rho_I X_I and d_1 = rho_0 (X_0 - X_I + (f/2) rho_I X_I).  Control: t_* without its
     8 mu_0/|x| term.
  E2 (the leading part, scalar check) On 4+1 Minkowski, for radial functions, (1/2) Box = 2 d_u d_v + (3/2) r^-1 (d_u -
     d_v) equals -rho_0^2 rho_I (X_I - 3/2)(X_0 - X_I) modulo rho_0^2 rho_I^2 Diff^2_b with polynomial coefficients
     (tested on rho_0^alpha rho_I^beta, alpha and beta symbolic).  Four-dimensional control: with r^-1 for 3/2 r^-1
     the same holds with 1 for 3/2 ([Hin26] (5.40)).  Control: 1 claimed at n = 4.
  E3 (A_0) scri5.py's five-dimensional (5.28) at h = 0 is lower triangular with off-diagonal entries exactly at (3, 1),
     (4, 1), (4, 3), (5, 2), (7, 3), (7, 4), and diagonal 2(1 - v)gC, (1 - v)gC, (1 - eC)(1 - v)gC, (1 - eU)gU, gU, 0,
     2 gU.  (C1 of scri5.py computes the matrix from S-bar.)  Control: a (7, 6) entry claimed zero-free.
  E4 (Definition 5.3 at n = 4) For sample parameters (gamma_Ups < 1/4) and seeds, the smallest E^C with min Re E^C >
     3/2 + 2 gamma_Ups and E^tot + (E^tot - 1) in E^C, E^tot := E^C u (3/2 + sigma_Ups, 0): exists (stabilises below
     the cut-off); E^C + 1/2 and E^tot + 1/2 lie in E^C; j E^tot lies in E^C (j >= 2); (2, 0), (3, 0) lie in E^C; the
     sets E_01, E_1/, E_0/, E_11 meet {Re z > 3/2 + 2 gamma_Ups} in E^C alone.  Control: gamma_Ups = 3/10.
  E5 (Proposition 5.14 at n = 4) Slot by slot, L_0 = -rho_0^2 rho_I (X_I - 3/2 - A_0)(X_0 - X_I) maps <E^C> into
     <E^C + 1>' -- slots 1-6 into E^C + 1, slot 7 into F_11 = 1 + (E^C u (3/2 + (1 - e_Ups) gamma_Ups, 0)) -- and so do
     the C-infinity error rho_0^2 rho_I^2 Diff^2_b (all slots into all) and the perturbation part, coefficients of
     I+-index E^tot; the leading-order classes: <(3, 0)>_0 into <(4, 0)>' (slots 1-6 (4, 0), slot 7 (3, 0)) with
     perturbation coefficients of index (2, 0).  Controls: a (7, 6) entry; F_11 without (3/2 + (1 - e_Ups) gamma_Ups,
     0).

sympy, fractions.  python3 ext5.py [--selftest | --mutants | --only k]
"""
import sys
import time
from fractions import Fraction as Fr
from itertools import product

import sympy as sp

from damping5 import Checklist

ZMAX = Fr(9)


# ------------------------------------------------------------------------------------------------- E1 coordinates
def e1(control=0, verbose=False):
    chk = Checklist(verbose, quiet=control != 0)
    p0, pI, mu0, Cp = sp.symbols("rho_0 rho_I mu_0 C_p", positive=True)
    tstar = 2 - 1 / p0 + Cp - (0 if control == 1 else 8 * mu0 * p0 * pI)
    rho = p0 * pI
    # V = a X_0 + b X_I acts on a function F(p0, pI) as a p0 F_p0 + b pI F_pI
    a, b = sp.symbols("a b")

    def act(fn):
        return a * p0 * sp.diff(fn, p0) + b * pI * sp.diff(fn, pI)

    s1 = sp.solve([act(tstar) - 1, act(rho)], [a, b], dict=True)[0]
    s2 = sp.solve([act(tstar), act(rho) - rho], [a, b], dict=True)[0]
    al = 8 * mu0 * p0**2 * pI
    good = sp.simplify(s1[a] - p0) == 0 and sp.simplify(s1[b] + p0) == 0
    chk("d_(t_*) = rho_0 (X_0 - X_I) at fixed (rho, omega)", good)
    good2 = sp.simplify(s2[a] - al) == 0 and sp.simplify(s2[b] - (1 - al)) == 0
    chk("rho d_rho = X_I + 8 mu_0 rho_0^2 rho_I (X_0 - X_I) at fixed (t_*, omega)", good2)
    # null coordinates (x^0, x^1): a function G(x^1, r) has d_0 G = G_r f/2 and d_1 G = G_(x^1) - G_r f/2
    x1, rr, mu = sp.symbols("x1 r mu", positive=True)
    f = 1 - mu / rr**2
    P0, PI = 1 / (2 - x1), (2 - x1) / rr
    d0 = lambda G: sp.diff(G, rr) * f / 2
    d1 = lambda G: sp.diff(G, x1) - sp.diff(G, rr) * f / 2
    g3 = True
    for dd, want0, wantI in ((d0, 0, -(f / 2) * P0 * PI**2), (d1, P0**2, -P0 * PI + (f / 2) * P0 * PI**2)):
        g3 &= sp.simplify(dd(P0) - want0) == 0 and sp.simplify(dd(PI) - wantI) == 0
    chk("d_0 = -(f/2) rho_0 rho_I X_I and d_1 = rho_0 (X_0 - X_I + (f/2) rho_I X_I) (III.B (4.3))", g3)
    return good and good2 and g3


# ------------------------------------------------------------------------------------------------- E2 leading part
def e2(control=0, verbose=False):
    chk = Checklist(verbose, quiet=control != 0)
    u, v = sp.symbols("u v", real=True)
    al, be = sp.symbols("alpha beta")
    p0, pI = sp.symbols("rho_0 rho_I", positive=True)
    ok = True
    for n, c in ((4, sp.Rational(3, 2)), (3, 1)):
        k = sp.Rational(n - 1, 2)
        r = (v - u) / 2
        P0, PI = 1 / (2 - u), 2 * (2 - u) / (v - u)
        F = P0**al * PI**be
        half_box = 2 * sp.diff(F, u, v) + k * (sp.diff(F, u) - sp.diff(F, v)) / r
        cc = sp.Rational(1) if (control == 1 and n == 4) else c
        # L_0 F with X_0 F = alpha F, X_I F = beta F
        L0 = -P0**2 * PI * (be - cc) * (al - be) * F
        q = sp.simplify((half_box - L0) / (F * P0**2 * PI**2))
        q = sp.simplify(q.subs(u, 2 - 1 / p0).subs(v, 2 - 1 / p0 + 2 / (p0 * pI)))
        poly = sp.expand(q)
        good = poly.is_polynomial(p0, pI, al, be)
        chk(f"n = {n}: (1/2) Box - L_0 = rho_0^2 rho_I^2 x (polynomial in rho_0, rho_I, X_0, X_I): {poly}", good)
        ok &= good
    return ok


# ------------------------------------------------------------------------------------------------- E3 A_0
def e3(control=0, verbose=False):
    chk = Checklist(verbose, quiet=control != 0)
    import scri5 as S
    from sbar5 import v, eC, gC, eU, gU
    A = S.five528()
    nz = {(i + 1, j + 1) for i in range(7) for j in range(7) if i != j and sp.simplify(A[i, j]) != 0}
    want = {(3, 1), (4, 1), (4, 3), (5, 2), (7, 3), (7, 4)}
    if control == 1:
        want = want | {(7, 6)}
    tri = all(A[i, j] == 0 for i in range(7) for j in range(i + 1, 7))
    diag = [2 * (1 - v) * gC, (1 - v) * gC, (1 - eC) * (1 - v) * gC, (1 - eU) * gU, gU, 0, 2 * gU]
    gd = all(sp.simplify(A[i, i] - diag[i]) == 0 for i in range(7))
    good = tri and gd and nz == want
    chk(f"A_0 lower triangular, off-diagonal support {sorted(nz)}, diagonal as stated", good)
    return good


# ------------------------------------------------------------------------------------------------- index sets
def closure(S):
    """the smallest index set containing S, below ZMAX: (z, k) -> (z + j, l), l <= k"""
    out = set()
    for (z, k) in S:
        j = 0
        while z + j <= ZMAX:
            for l in range(k + 1):
                out.add((z + j, l))
            j += 1
    return out


def plus(S, T):
    return closure({(z + w, k + l) for (z, k) in S for (w, l) in T if z + w <= ZMAX})


def shift(S, c):
    return {(z + c, k) for (z, k) in S if z + c <= ZMAX}


def build(gU, eU, seed):
    sig = [Fr(0), (1 - eU) * gU, gU, 2 * gU]
    radiative = closure({(Fr(3, 2) + s, 0) for s in sig})
    EC = closure(seed)
    for _ in range(60):
        Et = EC | radiative
        new = EC | plus(Et, shift(Et, -1)) | plus(Et, Et)
        if new == EC:
            return EC, Et, sig
        EC = new
    return None, None, sig


def lt(S, c):
    return {(z, k) for (z, k) in S if z > c}


def sub(S, T, cut=ZMAX):
    return all((z, k) in T for (z, k) in S if z <= cut)


SAMPLES = [(Fr(1, 5), Fr(1, 3), {(Fr(39, 20), 0)}), (Fr(1, 10), Fr(1, 2), set()),
           (Fr(1, 8), Fr(1, 4), {(Fr(17, 8), 1), (Fr(5, 2), 0)}), (Fr(6, 25), Fr(9, 10), {(Fr(21, 10), 0)})]


def e4(control=0, verbose=False):
    chk = Checklist(verbose, quiet=control != 0)
    ok = True
    samples = SAMPLES if control != 1 else [(Fr(3, 10), Fr(1, 3), set())]
    for gU, eU, seed in samples:
        EC, Et, sig = build(gU, eU, seed)
        if EC is None:
            chk(f"gU = {gU}: E^C stabilises", False)
            ok = False
            continue
        lo = Fr(3, 2) + 2 * gU
        cut = ZMAX - 1
        g = [min(z for z, _ in EC) > lo,
             sub(shift(EC, Fr(1, 2)), EC, cut), sub(shift(Et, Fr(1, 2)), EC, cut),
             sub(plus(Et, Et), EC, cut), sub(plus(plus(Et, Et), Et), EC, cut),
             (2, 0) in EC and (3, 0) in EC, sub(shift(Et, 1), EC, cut), sub(plus(Et, Et), shift(EC, 1), cut)]
        for s in sig:
            Es = EC | closure({(Fr(3, 2) + s, 0)})
            g.append(lt(Es, lo) == lt(EC, lo))
        E11 = EC | closure({(Fr(3, 2) + (1 - eU) * gU, 0), (Fr(3, 2) + 2 * gU, 0)})
        g.append(lt(E11, lo) == lt(EC, lo))
        good = all(g)
        chk(f"gU = {gU}, eU = {eU}, seed {sorted(seed)}: min Re E^C = {min(z for z, _ in EC)} > {lo}; "
            f"E^C + 1/2, E^tot + 1/2, 2E^tot, 3E^tot, E^tot + 1 in E^C; 2E^tot in E^C + 1; (2,0), (3,0); "
            f"the component sets agree above 3/2 + 2 gU: {g}", good)
        ok &= good
    return ok


# ------------------------------------------------------------------------------------------------- E5 Prop 5.14
def apply_L0(slots, diag, offd):
    """index sets of (X_I - 3/2 - A_0) applied slot by slot (before the factor rho_0^2 rho_I)"""
    out = []
    for j, S in enumerate(slots):
        c = Fr(3, 2) + diag[j]
        T = set()
        for (z, k) in S:
            if z == c:
                if k > 0:
                    T.add((z, k - 1))
            else:
                T.add((z, k))
        for (i, jj) in offd:
            if jj == j:
                T |= slots[i]
        out.append(closure(T))
    return out


def e5(control=0, verbose=False):
    chk = Checklist(verbose, quiet=control != 0)
    ok = True
    for gU, eU, seed in SAMPLES:
        EC, Et, sig = build(gU, eU, seed)
        gC, vC, eC = Fr(7), Fr(1, 2), Fr(1, 10)
        diag = [2 * (1 - vC) * gC, (1 - vC) * gC, (1 - eC) * (1 - vC) * gC, (1 - eU) * gU, gU, Fr(0), 2 * gU]
        offd = {(0, 2), (0, 3), (2, 3), (1, 4), (2, 6), (3, 6)}            # (column, row), 0-based: (i, j) = A[j, i]
        if control == 1:
            offd = offd | {(5, 6)}
        rad = lambda s: closure({(Fr(3, 2) + s, 0)})
        slots = [EC, EC, EC, EC | rad((1 - eU) * gU), EC | rad(gU), EC | rad(Fr(0)),
                 EC | rad((1 - eU) * gU) | rad(2 * gU)]
        F11 = shift(EC | (rad((1 - eU) * gU) if control != 2 else set()), 1)
        target = [shift(EC, 1)] * 6 + [F11]
        cut = ZMAX - 3
        lead = [shift(S, 1) for S in apply_L0(slots, diag, offd)]
        allin = set().union(*slots)
        err = shift(allin, 2)                                              # rho_0^2 rho_I^2 C^oo: +1 beyond rho_I
        pert = plus(Et, allin)                                             # coefficients of index E^tot
        g = [sub(lead[j], target[j], cut) and sub(err, target[j], cut) and sub(pert, target[j], cut)
             for j in range(7)]
        good = all(g)
        chk(f"gU = {gU}: <E^C> -> <E^C + 1>' slot by slot (leading, C^oo error, perturbation): {g}", good)
        ok &= good
        # leading-order classes
        L = [closure({(Fr(3), 0)})] * 6 + [closure({(Fr(2), 0)})]
        tL = [closure({(Fr(4), 0)})] * 6 + [closure({(Fr(3), 0)})]
        leadL = [shift(S, 1) for S in apply_L0(L, diag, offd)]
        allL = set().union(*L)
        gl = [sub(leadL[j], tL[j], cut) and sub(shift(allL, 2), tL[j], cut) and
              sub(plus(closure({(Fr(2), 0)}), allL), tL[j], cut) for j in range(7)]
        good = all(gl)
        chk(f"gU = {gU}: <(3,0)>_0 -> <(4,0)>' slot by slot: {gl}", good)
        ok &= good
    return ok


CHECKS = [("E1 the corner coordinates: d_t*, rho d_rho, d_0, d_1 in X_0, X_I", e1, 1),
          ("E2 (1/2) Box = -rho_0^2 rho_I (X_I - 3/2)(X_0 - X_I) mod rho_0^2 rho_I^2 Diff^2_b; n = 3 his (5.40)", e2, 1),
          ("E3 A_0: lower triangular, its off-diagonal support and diagonal", e3, 1),
          ("E4 Definition 5.3 at n = 4: the smallest E^C and its closure properties", e4, 1),
          ("E5 Proposition 5.14 at n = 4: <E^C> -> <E^C + 1>' and <(3,0)>_0 -> <(4,0)>', slot by slot", e5, 2)]


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
    print(f"ext5.py: {len(CHECKS) if ok_all else 'FAILED'}/{len(CHECKS)}")
    return ok_all


def mutants():
    caught = total = 0
    for name, fn, nc in CHECKS:
        for k in range(1, nc + 1):
            total += 1
            res = fn(control=k)
            caught += (not res)
            print(f"mutant {k} of {name[:2]}: {'caught' if not res else 'NOT caught'}", flush=True)
    print(f"ext5.py mutants: {caught}/{total}")
    return caught == total


if __name__ == "__main__":
    args = sys.argv[1:]
    verbose = "--verbose" in args
    if "--only" in args:
        k = int(args[args.index("--only") + 1])
        name, fn, nc = CHECKS[k - 1]
        print(name, "PASS" if fn(verbose=True) else "FAIL")
    elif "--mutants" in args:
        sys.exit(0 if mutants() else 1)
    else:
        sys.exit(0 if selftest(verbose) else 1)
