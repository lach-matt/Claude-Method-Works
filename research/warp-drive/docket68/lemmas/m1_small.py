#!/usr/bin/env python3
"""m1_small.py -- items 251, 256: M1, the plane's reading of the corridor's mouth, at the family's small end (the
localized five-dimensional hole).  M1's clauses as F1-AUDIT states them -- (a) a vacuum bulk; (b) the corridor exclusive
to the bulk, bounded by our plane P1 and, in the bridge form, position 2's piece P2; (c) on P1 the induced metric of the
mouth (eq. (17) on the record; the hole's equator here); (d) no added matter on P1; (e) regular, a smooth Killing horizon;
(f) P2 admissible -- and item 232's three, the kink, 203 and (e) through the whole bulk.  Worked in the conversation
(computed with sympy, exact where marked; READ where marked; not verified by a separate session; not seated);
2026-10-11.

  N0 (read) M's item-256 words, verbatim in the rulings file.
  N1 (computed, exact) 203 -- the corridor's own energy.  The hole's Komar mass, with the timelike Killing vector of the
     static region and the five-dimensional normalisation (D - 2)/(16 pi G5 (D - 3)), integrated over the 3-sphere at
     any r: M = 3 pi r_h^2 / (8 G5), independent of r (computed).  So the corridor's own energy is E = 3 pi c^4 r_h^2 /
     (8 G5) -- C3's small-end E(N), the energy whose first-law entropy is N ln2 (C2).  There is no separate sheet
     energy: the plane is stress-free (C1 H2), so 230 (b)'s static-sheet energy q (m/ell) E has nothing to carry it.
     203's equality -- the corridor's energy equals the README's E -- holds at the small end, through the first law and
     the count, not by assignment.
  N2 (computed, from C1) the clauses at the small end:
     (a) vacuum bulk -- Ricci-flat (C1 H1).
     (b) the corridor in the bulk, bridging P1 and P2: the hole and its Einstein-Rosen bridge are bulk objects; P1 is
         the equator in position 1's exterior and P2 the same surface in the second exterior (C1 H4).  The hole's
         horizon meets the plane along a 2-sphere (the plane's own horizon), orthogonally by the reflection symmetry.
     (c) P1 reads the hole's equator, -f dt^2 + dr^2/f + r^2 dOmega^2, f = 1 - r_h^2/r^2, for r_h << r << ell
         (C1 H3, verifier qualification 2).
     (d) no added matter on P1: the plane is totally geodesic, its stress zero at flat order (C1 H2).  The ring at the
         fold that blocked (d) on the record (m1_cypher M1, item 231) does not arise: the plane is smooth through the
         equator.
     (e) as F1-AUDIT words it -- no curvature singularity in the static spacetime's closure, a smooth Killing horizon:
         the static region and its horizon are regular (C1 H5; Kruskal crossing H4).  Item 232's "through the whole bulk
         under the corridor": the static bulk beneath the corridor, down to the horizon, and the bridge's slice are
         regular; the hole's future and past interiors hold r = 0 -- O1b/O1c's step, M's to rule.
     (f) P2 admissible: the plane's continuation carries the same positive tension and no matter stress; the 5D null
         energy is zero along every ray (vacuum), so (Z) holds net per ray; the plane's own four-dimensional reading on
         tangential rays (-2 r_h^2/r^4) is the bulk's Weyl term, the appearance (C1 verifier, item 254).
     the kink: at flat order the plane is the exact equator through the bridge; at warp order the plane's tension bends
         it by r_h/ell -- the real five-dimensional construction is Kudoh-Tanaka-Nakamura's numerical small brane holes,
         whose brane condition K = -h/ell they solve and which go smoothly to five-dimensional Schwarzschild as
         ell/rho_h grows (READ in full by the C1 verifier, item 254).  Not computed here.
  N3 (deduced) So at the small end M1 holds on every clause the record words -- (a)-(f), 203 and the kink (flat order
     exact, warp order the literature's construction) -- with one question left for M: whether item 232's (e) "through
     the whole bulk" admits the hole's interior singularity, which lies outside the static bulk and outside the bridge's
     slice the README's information uses (item 251: the README crosses as information, not along a causal path).

Imports nothing beyond sympy; reads the rulings file.  python3 m1_small.py [--selftest | --mutants]
"""
import os
import sys

import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
D68 = os.path.dirname(HERE)
RULINGS = os.path.join(D68, "M-RULINGS-2026-10-03.md")
MUT = {}
M256 = "One family, both ends (Recommended)"

t, r, rh, G5 = sp.symbols("t r r_h G5", positive=True)


def komar(D=5):
    """M = (D-2)/(16 pi G (D-3)) x the integral over the (D-2)-sphere of 2 nabla^r xi^t r^(D-2), for -f dt^2 + dr^2/f +
    r^2 dOmega_(D-2); nabla^r xi^t = f'/2 for xi = d/dt (computed from the Christoffel symbols)"""
    f = 1 - rh ** 2 / r ** 2 if D == 5 else 1 - rh / r
    if MUT.get("four_d_norm"):
        D_norm = 4
    else:
        D_norm = D
    # nabla_r xi_t = d_r xi_t - Gamma^t_{rt} xi_t, xi_t = -f, Gamma^t_{rt} = f'/(2f)
    fp = sp.diff(f, r)
    nab_r_xi_t = sp.diff(-f, r) - (fp / (2 * f)) * (-f)
    nab_up = sp.simplify(f * (-1 / f) * nab_r_xi_t)          # g^rr g^tt nabla_r xi_t
    Omega = {3: 2 * sp.pi ** 2, 2: 4 * sp.pi}[D - 2]
    integral = 2 * nab_up * r ** (D - 2) * Omega
    M = sp.simplify((D_norm - 2) / (16 * sp.pi * G5 * (D_norm - 3)) * integral)
    return dict(nab_up=nab_up, M=M, r_free=r not in M.free_symbols)


def compute():
    k5 = komar(5)
    k4 = komar(4)                                           # control: 4D Schwarzschild, r_h = 2 G M -> M = r_h/(2G)
    return dict(k5=k5, k4=k4)


def report(o):
    print("m1_small.py -- M1 at the family's small end (items 251, 256)\n")
    print("N1 Komar: nabla^r xi^t = %s; M = %s (independent of r: %s); control 4D: M = %s" % (
        o["k5"]["nab_up"], o["k5"]["M"], o["k5"]["r_free"], o["k4"]["M"]))


def checks(o):
    res = []
    add = lambda n, ok: res.append((n, bool(ok)))
    rul = " ".join(open(RULINGS, encoding="utf-8").read().split())
    add("N0 M's item-256 words verbatim in the rulings file", M256 in rul)
    ok = sp.simplify(o["k5"]["M"] - 3 * sp.pi * rh ** 2 / (8 * G5)) == 0 and o["k5"]["r_free"]
    ok &= sp.simplify(o["k4"]["M"] - rh / (2 * G5)) == 0
    add("N1 the hole's Komar mass is 3 pi r_h^2/(8 G5) at every r (control: 4D Schwarzschild r_h/(2G)) -- the corridor's "
        "own energy is C3's small-end E", ok)
    return res


MUTANTS = {"four_d_norm": "the Komar normalisation taken in four dimensions"}


def selftest():
    r_ = checks(compute())
    for n, ok in r_:
        print("  [%s] %s" % ("ok" if ok else "FAIL", n))
    k = sum(ok for _, ok in r_)
    print("selftest: %d/%d" % (k, len(r_)))
    return k == len(r_)


def mutants():
    caught = 0
    for kk, desc in MUTANTS.items():
        MUT.clear()
        MUT[kk] = True
        try:
            failed = [n.split()[0] for n, ok in checks(compute()) if not ok]
        except Exception as ex_:
            failed = ["raised %s" % type(ex_).__name__]
        MUT.clear()
        caught += bool(failed)
        print("  mutant %-11s %-48s %s" % (kk, desc, "caught by " + ", ".join(failed) if failed else "NOT CAUGHT"))
    print("mutants: %d/%d caught" % (caught, len(MUTANTS)))
    return caught == len(MUTANTS)


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    if "--mutants" in sys.argv:
        sys.exit(0 if mutants() else 1)
    report(compute())
