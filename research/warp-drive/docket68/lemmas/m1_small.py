#!/usr/bin/env python3
"""m1_small.py -- items 251, 256: M1, the plane's reading of the corridor's mouth, at the family's small end (the
localized five-dimensional hole).  M1's clauses as F1-AUDIT states them -- (a) a vacuum bulk; (b) the corridor exclusive
to the bulk, bounded by our plane P1 and, in the bridge form, position 2's piece P2; (c) on P1 the induced metric of the
mouth (eq. (17) on the record; the hole's equator here); (d) no added matter on P1; (e) regular, a smooth Killing horizon;
(f) P2 admissible -- and item 232's three, the kink, 203 and (e) through the whole bulk.  Worked in the conversation
(computed with sympy, exact where marked; READ where marked; verified once -- item 269, CONFIRMED with
qualifications, all seated below in [Verifier, item 269] notes (205/206); not seated); 2026-10-11.  First headed "...
not verified by a separate session ...".

  N0 (read) M's item-256 words, verbatim in the rulings file.
  N1 (computed, exact) 203 -- the corridor's own energy.  The hole's Komar mass, with the timelike Killing vector of the
     static region and the five-dimensional normalisation (D - 2)/(16 pi G5 (D - 3)), integrated over the 3-sphere at
     any r: M = 3 pi r_h^2 / (8 G5), independent of r (computed).  So the corridor's own energy is E = 3 pi c^4 r_h^2 /
     (8 G5) -- C3's small-end E(N), the energy whose first-law entropy is N ln2 (C2).  There is no separate sheet
     energy: the plane is stress-free (C1 H2), so 230 (b)'s static-sheet energy q (m/ell) E has nothing to carry it.
     203's equality -- the corridor's energy equals the README's E -- holds at the small end, through the first law and
     the count, not by assignment.
     [Verifier, item 269: "at any r" holds at flat order only -- with the bulk's AdS term (f + r^2/ell^2) the Komar
     integral grows as 3 pi r^4/(8 G5 ell^2) and needs a background subtraction at warp order (computed, N4); the full
     3-sphere is C2's R1 both-sides convention -- a hemisphere gives 3 pi r_h^2/(16 G5), the first law holding for it
     too since it is homogeneous (computed, N4; item 258); "not by assignment" is overstated: C3 defines the small end's
     E(N) as this hole's mass at R1's radius, so 203 holds by that definition with Komar = ADM -- its content is that
     the energy is the bulk's own, r-independent at flat order, against 230 (b)'s sheet energy, read the same from
     exteriors I and II by the isometry between them.]
  N2 (from C1, verified -- cited, not recomputed here [verifier, item 269]) the clauses at the small end:
     (a) vacuum bulk -- Ricci-flat (C1 H1).
         [Verifier, item 269: at flat order; F1-AUDIT words M1-a as R_AB = -(4/ell^2) g_AB, met at warp order on
         Kudoh-Tanaka-Nakamura's numerical bulk, Lambda = -6/ell^2 (READ).]
     (b) the corridor in the bulk, bridging P1 and P2: the hole and its Einstein-Rosen bridge are bulk objects; P1 is
         the equator in position 1's exterior and P2 the same surface in the second exterior (C1 H4).  The hole's
         horizon meets the plane along a 2-sphere (the plane's own horizon), orthogonally by the reflection symmetry.
         [Verifier, item 269: unsaid -- the plane is one connected surface running through both interiors to r = 0
         (m1p2x_small X3); "exclusive" holds for stress, not place, the horizon cutting P1; the bridge form rests on
         251, 232 (2) having set a single bridge aside as "the connection", and exterior II exists only in the eternal
         solution (254 (3), 267 (5)).]
     (c) P1 reads the hole's equator, -f dt^2 + dr^2/f + r^2 dOmega^2, f = 1 - r_h^2/r^2, for r_h << r << ell
         (C1 H3, verifier qualification 2).
     (d) no added matter on P1: the plane is totally geodesic, its stress zero at flat order (C1 H2).  The ring at the
         fold that blocked (d) on the record (m1_cypher M1, item 231) does not arise: the plane is smooth through the
         equator.
     (e) as F1-AUDIT words it -- no curvature singularity in the static spacetime's closure, a smooth Killing horizon:
         the static region and its horizon are regular (C1 H5; Kruskal crossing H4).  Item 232's "through the whole bulk
         under the corridor": the static bulk beneath the corridor, down to the horizon, and the bridge's slice are
         regular; the hole's future and past interiors hold r = 0 -- O1b/O1c's step, M's to rule.
         [Item 259 has ruled it: admitted, the interior outside the passage.  Verifier, item 269: "regular" is
         computed, "complete for the passage" is M's 259 -- geodesic completeness is not computed, and the region is
         incomplete: a radial fall from the horizon reaches r = 0 in at most r_h/c (hold_small L5).]
     (f) P2 admissible: the plane's continuation carries the same positive tension and no matter stress; the 5D null
         energy is zero along every ray (vacuum), so (Z) holds net per ray; the plane's own four-dimensional reading on
         tangential rays (-2 r_h^2/r^4) is the bulk's Weyl term, the appearance (C1 verifier, item 254).
         [Verifier, item 269: within one universe only -- on the board's H-WITHIN-IS-SAME-PLANE (m1p2_cypher L7),
         not M's word; between universes 139 (1) puts -sigma/4 there (m1p2x_small, m1p2x_index).  And the orders were
         mixed: the 5D null energy is zero in the bulk and on rays tangent to the plane; a ray crossing the +sigma plane
         sees +sigma sin a >= 0 (far_cypher F8) -- the NEC holds, the null energy is not zero there.]
     the kink: at flat order the plane is the exact equator through the bridge; at warp order the plane's tension bends
         it by r_h/ell -- the real five-dimensional construction is Kudoh-Tanaka-Nakamura's numerical small brane holes,
         whose brane condition K = -h/ell they solve and which go smoothly to five-dimensional Schwarzschild as
         ell/rho_h grows (READ in full by the C1 verifier, item 254).  Not computed here.
         [Verifier, item 269: "exact at flat order" is vacuous -- at flat order there is no kink (K = 0); at warp
         order K = -h/ell on KTN's static exterior (eq. (21), READ; a numerical existence result, disputed, item 261),
         the deviation first order in rho_h/ell (consistent with their Table I, computed from READ numbers; KTN do not
         state "r_h/ell"); KTN compute only outside the horizon, so the kink through the horizon and the bridge is
         deduced, not read.  KTN is gr-qc/0301089 (the board's brief to the verifier miscited it as hep-th).
         Unnamed before: C4 is classical.  The eternal hole (b) and (f) need is static quantum-mechanically only in
         the Hartle-Hawking state, whose bath on P1 at the Hawking temperature is rho_bath/sigma = 0.305 at the example
         and bends the plane 0.92 as much as the tension does -- K r_h = 7.4e-16 against 8.0e-16 (computed, N4).]
  N3 (deduced) So at the small end M1 holds on every clause the record words -- (a)-(f), 203 and the kink (flat order
     exact, warp order the literature's construction) -- with one question left for M: whether item 232's (e) "through
     the whole bulk" admits the hole's interior singularity, which lies outside the static bulk and outside the bridge's
     slice the README's information uses (item 251: the README crosses as information, not along a causal path).
     [M answered it: item 259, admitted.  Verifier, item 269: M1 holds at the small end at flat order in classical
     GR, within one universe, with the qualifications above.]

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


def n4():
    """item 269: the Komar integral with the bulk's AdS term; the hemisphere and its first law; the Hartle-Hawking bath
    on the plane against the tension at the example"""
    ell = sp.symbols("ell", positive=True)
    f = 1 - rh ** 2 / r ** 2 + r ** 2 / ell ** 2
    fp = sp.diff(f, r)
    nab_up = sp.simplify(f * (-1 / f) * (sp.diff(-f, r) - (fp / (2 * f)) * (-f)))
    M_ads = sp.simplify(3 / (16 * sp.pi * G5 * 2) * 2 * nab_up * r ** 3 * 2 * sp.pi ** 2)
    M_half = sp.simplify(komar(5)["M"] / 2)
    S_half = sp.pi ** 2 * rh ** 3 / (4 * G5)                    # A/(4 G5) over one side: pi^2 r_h^3 / (4 G5)
    T = 1 / (2 * sp.pi * rh)
    first_law_half = sp.simplify(sp.diff(M_half, rh) - T * sp.diff(S_half, rh)) == 0
    import contextlib, importlib.util, io, math
    spec = importlib.util.spec_from_file_location("m1s_pg", os.path.join(HERE, "p2_gravity.py"))
    PG = importlib.util.module_from_spec(spec)
    with contextlib.redirect_stdout(io.StringIO()):
        spec.loader.exec_module(PG)
    Gs, cs, hbs, ellx, kB = PG.G, PG.C, PG.HBAR, PG.ELL_MAX, 1.380649e-23
    l5 = (hbs * Gs * ellx / cs ** 3) ** (1 / 3)
    rh_ex = (2 * 2742570311524972 * math.log(2) / math.pi ** 2) ** (1 / 3) * l5
    kT = hbs * cs / (2 * math.pi * rh_ex)                         # the Hawking temperature, k T in joules
    rho_bath = 106.75 * math.pi ** 2 / 30 * kT ** 4 / (hbs * cs) ** 3
    sigma = 3 * cs ** 4 / (4 * math.pi * Gs * ellx ** 2)          # p2_planck, the offset dropped
    ratio = rho_bath / sigma
    # Israel: K_ab = -(kappa^2/2)(S_ab - S h_ab/3); tension -> (kappa^2/6) sigma = 1/ell; traceless radiation ->
    # (kappa^2/2) rho = 3 (rho/sigma) / ell
    return dict(M_ads=M_ads, M_half=M_half, first_law_half=first_law_half, ratio=ratio, K_ratio=3 * ratio,
                K_tension=rh_ex / ellx, K_bath=3 * ratio * rh_ex / ellx)


def compute():
    k5 = komar(5)
    k4 = komar(4)                                           # control: 4D Schwarzschild, r_h = 2 G M -> M = r_h/(2G)
    return dict(k5=k5, k4=k4, n4=n4())


def report(o):
    print("m1_small.py -- M1 at the family's small end (items 251, 256)\n")
    print("N1 Komar: nabla^r xi^t = %s; M = %s (independent of r: %s); control 4D: M = %s" % (
        o["k5"]["nab_up"], o["k5"]["M"], o["k5"]["r_free"], o["k4"]["M"]))
    v = o["n4"]
    print("N4 (item 269) Komar with the AdS term %s; hemisphere %s (first law: %s); Hartle-Hawking bath rho/sigma = %.3f, "
          "K bath/tension %.3f, K r_h %.2g against %.2g" % (v["M_ads"], v["M_half"], v["first_law_half"], v["ratio"],
                                                            v["K_ratio"], v["K_bath"], v["K_tension"]))


def checks(o):
    res = []
    add = lambda n, ok: res.append((n, bool(ok)))
    rul = " ".join(open(RULINGS, encoding="utf-8").read().split())
    add("N0 M's item-256 words verbatim in the rulings file", M256 in rul)
    ok = sp.simplify(o["k5"]["M"] - 3 * sp.pi * rh ** 2 / (8 * G5)) == 0 and o["k5"]["r_free"]
    ok &= sp.simplify(o["k4"]["M"] - rh / (2 * G5)) == 0
    add("N1 the hole's Komar mass is 3 pi r_h^2/(8 G5) at every r (control: 4D Schwarzschild r_h/(2G)) -- the corridor's "
        "own energy is C3's small-end E", ok)
    v = o["n4"]
    ell = sp.symbols("ell", positive=True)
    ok = sp.simplify(v["M_ads"] - (3 * sp.pi * rh ** 2 / (8 * G5) + 3 * sp.pi * r ** 4 / (8 * G5 * ell ** 2))) == 0
    ok &= sp.simplify(v["M_half"] - 3 * sp.pi * rh ** 2 / (16 * G5)) == 0 and v["first_law_half"]
    ok &= "%.3f" % v["ratio"] == "0.305" and "%.2f" % v["K_ratio"] == "0.92"
    ok &= "%.2g" % v["K_bath"] == "7.4e-16" and "%.2g" % v["K_tension"] == "8e-16"
    add("N4 (item 269) with the AdS term the Komar integral grows by 3 pi r^4/(8 G5 ell^2); the hemisphere gives 3 pi "
        "r_h^2/(16 G5), the first law holding; the Hartle-Hawking bath is 0.305 of the tension and bends the plane 0.92 "
        "as much", ok)
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
