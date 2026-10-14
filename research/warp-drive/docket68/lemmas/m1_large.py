#!/usr/bin/env python3
"""m1_large.py -- item 356: M1, the plane's reading of the corridor's mouth, at the family's large end, re-posed on the
one-way object.  C3 (corridor_family F5, verified 261) fixed the large end as the large brane hole: the plane reads
four-dimensional Schwarzschild with corrections O(ell^2/r0^2), its T and S Schwarzschild's at fixed ADM mass to first
order.  The record's M1 was posed on Bronnikov-Kim's eq. (17), whose surface gravity at r0 = 2m is zero; it is
superseded at this end and kept as the record (m1_bulk.py, d_minus.py).  M1's clauses are F1-AUDIT's, as m1_small.py
states them -- (a) a vacuum bulk; (b) the corridor exclusive to the bulk, bounded by our plane P1 and position 2's
piece P2; (c) on P1 the induced metric of the mouth; (d) no added matter on P1; (e) regular, a smooth Killing horizon;
(f) P2 admissible -- and item 232's three, the kink, 203 and (e) through the whole bulk under the corridor.  Worked in
the conversation (computed with sympy, exact where marked; READ where marked, quoted from the two papers read in full
at item 356; deduced where marked; not verified by a separate session; not seated); 2026-10-13.

  M0 (read) M's words, verbatim in the rulings file: 356, 232 (6), (7) and (9), 203, 256, 273, 275, 276, 284 (4).
  M1 (READ; computed) Clause (a), the bulk.  Figueras and Wiseman, arXiv:1105.2558v2 (FW): "The 5d metric g_AB obeying
     R_AB = - 4/ell^2 g_AB", their static large holes solving the Einstein-DeTurck problem, and "phi_max -> 0 in the
     continuum limit, which provides evidence that our solutions are not Ricci solitons".  Abdolrahimi, Cattoen, Page
     and Yaghoobpour-Tari, arXiv:1206.0708v4 (AFPY), independently: "the vacuum Einstein equation in the 5-dimensional
     bulk is E_ab ≡ R_ab + 4 g_ab = 0" (units Lambda = -6).  Computed: the Poincare form ell^2/z^2 (dz^2 + eta) has R_AB
     = -(4/ell^2) g_AB and Kretschmann 40/ell^4, and every null k gives R_AB k^A k^B = 0 on such a bulk, so the five-
     dimensional null energy is zero on every ray of the static bulk.  (a) holds at warp order, in F1-AUDIT's own words
     -- stronger than the small end's flat order (m1_small N2 (a)).
  M2 (READ; computed) The kink and clause (d).  FW's Israel condition, their eq. (3), 8 pi G4 T^brane = (2/ell)(K_mn -
     K gamma_mn + (3/ell) gamma_mn), and on the brane "we impose the vacuum Israel matching conditions (eq.(3) with the
     l.h.s. equal to zero)"; AFPY: "Assuming no matter on the brane, in our units with Lambda = -6, the Israel junction
     condition is [K_mn] = -2 gamma_mn".  Computed: on the Poincare form at z = eps, FW's K_mn = gamma_mn/ell exactly,
     the l.h.s. of (3) vanishes, and its 3/ell term is a tension lambda = 3/(4 pi G4 ell^2) -- with G4 = G, our plane's
     sigma = 3 c^4/(4 pi G ell^2) (B6'), q = 1.  So the plane carries our tension and nothing else, (d), and the warp's
     kink K_mn = gamma_mn/ell holds on it everywhere the solution reaches, the brane horizon included: a bulk in which
     the kink follows our plane into the corridor, built as a real five-dimensional construction, which 232 (a) asks
     for (230 (a) overruled).  Through the faces the condition is carried by continuity of a smooth horizon (deduced,
     M5), as at the small end, where Kudoh-Tanaka-Nakamura compute only outside the horizon (m1_small N2, the kink).
     The ring at the fold that blocked (d) on the record (m1_cypher M1) does not arise: the plane is smooth.
  M3 (READ) Existence, and the sizes it covers.  FW: "we have been able to construct braneworld black holes with
     R_4/ell in [0.07, 20]".  Beyond that, FW's section II builds the large holes perturbatively in eps, the brane
     curvature against ell, from the AdS5-CFT4 solution with Schwarzschild boundary metric (Figueras, Lucietti and
     Wiseman, 1104.4489) -- "Subject to the assumption that the AdS5-CFT4 solution exists for boundary metric (4) we
     have constructed a braneworld solution ... perturbatively in eps" -- and "For large radius the RSII solutions are
     indeed close to the associated AdS5-CFT4 solution".  FW's two assumptions are named there: the AdS5-CFT4 solution
     exists, with "the metric tends to the Poincare horizon of AdS" -- met by FLW's numerical solution and by AFPY's
     independent one -- and "We further assume that solutions exist for regular perturbations of the boundary metric
     ... in some finite neighbourhood of eps = 0".  AFPY's construction is "independent of the Ricci-DeTurck-flow
     method" and "agrees closely".  FW on stability: "Our numerical solutions indicate the RSII black holes are
     dynamically stable for axisymmetric perturbations for all radii."  So the large end proper, r0 >> ell, is the
     regime FW's construction is made for; its assumptions are FW's, named here and in M10.
  M4 (READ; computed) Clause (c), P1's reading of the mouth.  AFPY's brane metric, their eq. (13), to first order in
     1/(-Lambda M^2): g_rr = [1 - (rho - 2M)(F - rho F')/((-Lambda rho^2)(rho - 1.5M))] / (1 - 2M/rho), g_tt = -(1 -
     2M/rho), the sphere's area radius^2 = rho^2 + F/(-Lambda), with FW's data fitted by their eq. (15), F_FLW = 1 -
     1.062 y + 0.554 y^2 - 0.120 y^3, y = 2M/rho; AFPY: "The bulk Einstein equation plus the Israel junction condition
     for a brane with the RSII value of the tension and without matter imply that the Ricci scalar of the brane metric
     is zero."  Computed from (13): (i) R = 0 to first order for every F -- the transcription checked against AFPY's
     own statement; (ii) g_RR = 1 + 2M/R + O(R^-2) in the area radius, so the ADM mass is M (AFPY: "the ADM mass is
     precisely M"); (iii) the surface gravity is 1/(4M) exactly at this order (AFPY: "exactly 1/(4M)"); (iv) the
     horizon's area exceeds 4 pi (2M)^2 by 4 pi F(1) ell^2/6 = 0.779 ell^2, 0.062 (ell/r0)^2 of itself (C3's Q3).  So
     P1 reads four-dimensional Schwarzschild with r0 = 2GM/c^2, corrections O(ell^2/r0^2) (FW: "the solutions become
     Ricci flat with corrections going as O(ell^2/R_4^2)").  (v) The plane's own reading of the mouth, from (13) with
     F_FLW: its energy density and its radial and tangential null readings are negative outside the horizon, of order
     (ell/r0)^2/r0^2 and falling as rho^-5; the radial reading is zero on the horizon.  It is FW's eq. (7), delta G_mn
     = 16 pi G4 <T^CFT_mn> (READ), the dual stress the braneworld reads as the bulk's projected Weyl term
     (Shiromizu-Maeda-Sasaki; standard-not-READ): the appearance, while the five-dimensional null energy is zero (M1)
     -- the large end's counterpart of the small end's -2 r_h^2/r^4 (Z1t-s).
  M5 (READ; computed; standard-not-READ where marked) Clause (e), regular.  FW: "regularity at the horizon r = 0
     requires T = 4A there and tau ~ tau + pi"; AFPY: "y = 1 is the black hole horizon where we impose the regularity
     requirement B = C".  The surface gravity is 1/(4M), not zero (M4 (iii)): a smooth, non-degenerate Killing horizon,
     against eq. (17)'s extremal throat.  232 (c), through the whole bulk under the corridor: the static bulk beneath
     the hole is FW's whole domain -- the brane to the Poincare horizon, the axis to the hole's horizon -- on which the
     elliptic problem is solved; b4_static S2's singular surface belongs to eq. (17)'s static bulk, which this is not.
     The bulk's far edge is FW's boundary condition, "the metric tends to the Poincare horizon of AdS" (FAR's Q8, 355).
     Classical control (computed): the background's curvature in five-dimensional Planck units is 40 (l5/ell)^4 = 40
     (l_P/ell)^(8/3), with l5^3 = l_P^2 ell -- 5.9e-79 at the window's floor, 6.2 at its top; below 1% of the Planck
     scale for ell >= 22.4 l_P, w <= 189.9 of the window's 196.885 doublings.  The large hole adds less at its face
     (12/r0^4 on the plane, r0 >= 10 ell where the large end is controlled).  Through the faces: a static region with a
     non-degenerate Killing horizon extends smoothly through it (Racz and Wald; standard-not-READ), and FW's metric
     functions, smooth in the polar pair (r, tau) and independent of tau, are smooth functions of r^2 (Whitney's
     theorem on even functions; standard-not-READ).  (estimate) The state.  The one-way object is formed, so its state
     is the collapse-formed one, outgoing Hawking flux; m1_small N4's Hartle-Hawking bath is the eternal manifold's.
     Its energy density near the face is at most the blackbody's at the hole's temperature, g* (pi^2/30) (k T)^4/(hbar
     c)^3 with k T = hbar c/(4 pi r0): over sigma, g* (l_P ell/r0^2)^2/(5760 pi) (computed) -- 1.2e-9 at r0 = 10 ell
     and ell = 22.4 l_P with the Standard Model's 106.75, less everywhere else in the large end.  At the small end the
     flux was 0.29 sigma (c4_oneway P5); at the large end the plane's quantum load is negligible, and C4's "classical"
     holds there with room.  The interiors' regularity down to your 273's region is O1b's and O1c's at the large end,
     as at the small end (m1_small N2 (e), item 259).
  M6 (READ; computed) Clause (b), the corridor in the bulk.  FW: "the horizon is pancake-like [32], with a proper
     distance to the tip going as ~ ell log(R_4/ell) for large R_4/ell".  The hole's horizon is a bulk object; it meets
     P1 along the brane's horizon.  On the one-way object (282): P1 is our side up to our black-hole face, P2 the same
     surface on position 2's side from its white-hole face, joined through the interiors and the bounce (273).
     Computed: the bounce's map (U, V) -> (-U, -V) is an isometry of every static, axisymmetric metric in Kruskal form
     whose components depend on UV and the bulk angle x, FW's dr dx cross term included (r^2 = -UV, so 2 r dr = -(U dV
     + V dU) is invariant) -- c4_oneway P2's spherically symmetric computation carried to FW's ansatz (9).  The gluing
     exists at the large end on the same footing as at the small end; what the interior is between the faces is O1b and
     O1c's.
  M7 (computed; READ where marked) 203, the corridor's own energy.  The ADM mass is M (M4 (ii)); the plane carries the
     RS tension alone (M2), and on the Poincare form the brane at z = eps is flat (computed: its induced metric is
     ell^2/eps^2 eta), so the tension adds no four-dimensional energy.  E = M c^2 is the bulk's own.  AFPY: "to first
     order in 1/(-Lambda M^2), the Hawking temperature and entropy for the RSII black hole have the same values as they
     do for the Schwarzschild metric", so S = 4 pi G M^2/(hbar c) = N ln2 gives r0 = 2GM/c^2 = (N A_bit/4 pi)^(1/2) and
     E = c^4 r0/(2G) = 459,404,002.42 J x sqrt(N) (computed; C3's F1).  203's equality holds at the large end by C3's
     definition with E the ADM mass, the energy the bulk's own -- not 230 (b)'s sheet energy, which 232 (7) overruled.
     Position 2 reads its own face's mass, its own under its laws (240; M1P2x).
  M8 (computed; deduced) Clause (f), P2 admissible: 139 (2) where it bears (284 (4), 285).  At the small end the README
     alone supplies it within 2.0e-15 m (e_positive E7).  At the large end it does not: the README's mean density inside
     r0 is 2 ell^2/r0^2 of sigma/4 (computed, exact), at most 0.02 where the large end is controlled (r0 >= 10 ell).
     It is not needed.  What a ray crossing position 2's plane picks up is the side's total, tau sigma + S2 = sigma/2 =
     (2/3) lambda_RS > 0 with no matter at all (tau_share T4, imported; c4_oneway P19), so the crossing share Sigma+
     sin a + w c^2/sin a, w >= 0, is positive at every angle (m1p2x_sixth W1's direction-neutral form; deduced).  The C4
     verifier's (7), accepted at 310, took the side total as (f)'s a fortiori route; at the large end it is the route.
     Sigma+ comes from 275 and 276 with 139 (1)'s ratio, at both ends.  284 (4)'s mechanism, the README itself, is the
     small end's; its requirement, positivity where the rays cross, holds at both.
  M9 (computed; calculator.py, items 286-291; the encoding the board's, 192) M1's question at the large end clause by
     clause (291), the attributes C4's construction choices -- the continuation (b_interior's cells, whose properties
     are the interiors' and not the end's), P2's tension, P2's matter -- with (f) entered as M8 computes it: positive in
     every configuration on the side total.  Logic joins (a), (b)/(e) and (f): 1, 1, 1, M1 holds.  Control (named):
     with (f) entered on P2's own stress, the README not supplying it at the large end, every known cell keeping 139 (1)
     has (f) = 0; statistics admits only 0, information only 1 (the question's cell the join of a cell keeping 139 (1)
     and a +sigma cell carrying the README), so the calculator refuses, and analysis ranks 0 at +1.7 decades (2
     ell^2/r0^2 = 0.02 at r0 = 10 ell, more below it).  The README-alone reading does not give 1 at the large end, as
     M8 says.
  M10 (deduced) The ledger, and what is narrowed.  Holding at the large end on the one-way object: (a) at warp order,
     (c), (d), (e) on the static bulk and through the faces, the kink, 203, (b) through the bounce's map, (f) on the
     side total.  Narrowed openly (314 (b)), not residue: (i) to first order in (ell/r0)^2 for M4's figures (AFPY's
     order), FW's numerics being non-perturbative up to R_4 = 20 ell; (ii) to FW's construction beyond 20 ell, whose one
     assumption is FW's own, that the AdS5-CFT4 solution persists under a regular perturbation of its boundary metric
     -- supported by FW's spectrum, a single negative mode and no zero modes at every size computed; (iii) to the
     classical bulk, ell >= 22.4 l_P (w <= 189.9), the window's top being Planck-scale as C3's verifier said (261 (2));
     (iv) within one family member at a time: position 2's face and its own mass are M1P2x's.  Left to other rows: the
     interiors between the faces (O1b, O1c, large end).

What this does not claim: the large hole's interior; position 2's side at the large end (M1P2x); the plane's reading
beyond first order in (ell/r0)^2; anything about eq. (17), which this end no longer uses.

Imports tau_share.py, calculator.py, index_audit.py and b_interior.py by path.  Stdlib + sympy.
python3 m1_large.py [--selftest | --mutants]
"""
import contextlib
import importlib.util
import io
import itertools
import math
import os
import re
import sys

import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
D68 = os.path.dirname(HERE)
RULINGS = os.path.join(D68, "M-RULINGS-2026-10-03.md")
MUT = {}
WORDS = ((356, "I still see a lot, including items that rest on M1 and B4d"),
         (232, '(9) "Board reading on clause (e): M1\'s regularity holds inside the verified layer.'),
         (232, "M1's regularity is to hold through the whole bulk under the corridor"),
         (203, "If so, does its energy equal the README's E, read the same from both sides (your 111)"),
         (256, "keep the record's 4D results as the large end"), (273, '"Quantum bounce to pos 2 (Recommended)"'),
         (275, 'verbatim: "Coincident everywhere"'),
         (284, "Positivity is needed where the README lands and the corridor's rays cross position 2's plane."))
QUOTES = ("R_AB = - 4/ell^2 g_AB", "phi_max -> 0 in the continuum limit", "E_ab ≡ R_ab + 4 g_ab = 0",
          "we impose the vacuum Israel matching conditions (eq.(3) with the l.h.s. equal to zero)",
          "Assuming no matter on the brane", "R_4/ell in [0.07, 20]", "Subject to the assumption that the AdS5-CFT4",
          "the ADM mass is precisely M", "exactly 1/(4M)", "regularity at the horizon r = 0",
          "the horizon is pancake-like [32]",
          "the Hawking temperature and entropy for the RSII black hole have the same")
C_LIGHT, G_N, H_PL = 299792458.0, 6.67430e-11, 6.62607015e-34
HBAR = H_PL / (2 * math.pi)
ELL_MAX, W_TOP = 13.964e-6, 196.885
F_FLW = (1, -1.062, 0.554, -0.120)                              # AFPY eq. (15), the fit to FW's data
_MOD, _C = {}, {}


def _load(name, key):
    if key in _MOD:
        return _MOD[key]
    saved = list(sys.path)
    sys.path[:0] = [HERE, D68]
    try:
        spec = importlib.util.spec_from_file_location(key, os.path.join(HERE, name))
        mod = importlib.util.module_from_spec(spec)
        with contextlib.redirect_stdout(io.StringIO()):
            spec.loader.exec_module(mod)
    finally:
        sys.path[:] = saved
    _MOD[key] = mod
    return mod


def _item(n):
    txt = open(RULINGS, encoding="utf-8").read()
    m = re.search(r"^%d\. .*?(?=^\d{3}\. |\Z)" % n, txt, re.M | re.S)
    return " ".join(m.group(0).split()) if m else ""


def _curv(g, x):
    """Christoffels, Ricci (diagonal metrics only where used) and the Ricci scalar of a metric in coordinates x"""
    n = len(x)
    gi = g.inv()
    Gam = [[[sp.simplify(sum(gi[a, d] * (sp.diff(g[d, b], x[c]) + sp.diff(g[d, c], x[b]) - sp.diff(g[b, c], x[d]))
                             for d in range(n)) / 2) for c in range(n)] for b in range(n)] for a in range(n)]
    Ric = sp.zeros(n, n)
    for b in range(n):
        for c in range(n):
            Ric[b, c] = sp.simplify(sum(sp.diff(Gam[a][b][c], x[a]) - sp.diff(Gam[a][b][a], x[c])
                                        + sum(Gam[a][a][d] * Gam[d][b][c] - Gam[a][c][d] * Gam[d][b][a]
                                              for d in range(n)) for a in range(n)))
    return gi, Gam, Ric


# ---------------------------------------------------------------------------------- M1 the bulk
def m1():
    if "m1" in _C:
        return _C["m1"]
    z, ell = sp.symbols("z ell", positive=True)
    t, x1, x2, x3 = sp.symbols("t x1 x2 x3", real=True)
    X = [t, x1, x2, x3, z]
    w = ell ** 2 / z ** 2
    g = sp.diag(-w, w, w, w, w)
    gi, Gam, Ric = _curv(g, X)
    lam_ = -4 / ell ** 2 if not MUT.get("bulk_sign") else 4 / ell ** 2      # FW's (1): R_AB = -(4/ell^2) g_AB
    einstein = all(sp.simplify(Ric[i, j] - lam_ * g[i, j]) == 0 for i in range(5) for j in range(5))
    # Riemann for the Kretschmann scalar
    n = 5
    Riem = [[[[sp.simplify(sp.diff(Gam[a][b][d], X[c]) - sp.diff(Gam[a][b][c], X[d])
                           + sum(Gam[a][c][e] * Gam[e][b][d] - Gam[a][d][e] * Gam[e][b][c] for e in range(n)))
               for d in range(n)] for c in range(n)] for b in range(n)] for a in range(n)]
    K = sp.simplify(sum(Riem[a][b][c][d] ** 2 * g[a, a] * gi[b, b] * gi[c, c] * gi[d, d]
                        for a in range(n) for b in range(n) for c in range(n) for d in range(n)))
    k = sp.Matrix([1, 1, 0, 0, 0])                                 # a null vector of the form
    null = sp.simplify((k.T * (lam_ * g) * k)[0, 0])
    _C["m1"] = dict(einstein=einstein, K=K, null=null)
    return _C["m1"]


# ---------------------------------------------------------------------------------- M2 the kink, (d)
def m2():
    z, ell, eps, G4 = sp.symbols("z ell epsilon G4", positive=True)
    eta = sp.diag(-1, 1, 1, 1)
    gt = (ell ** 2 / z ** 2) * eta
    K = (-sp.Rational(1, 2) * (z / ell) * sp.diff(gt, z)).subs(z, eps)          # FW's K_mn at z = eps
    gam = gt.subs(z, eps)
    trK = sum((gam.inv() * K)[i, i] for i in range(4))
    three = 3 if not MUT.get("tension_twice") else 6
    lhs = sp.simplify((2 / ell) * (K - trK * gam + sp.Rational(three, 1) / ell * gam))
    tension = sp.simplify((2 / ell) * (3 / ell) / (8 * sp.pi * G4))               # the 3/ell term as -T = lambda
    sigma = 3 / (4 * sp.pi * G4 * ell ** 2)                                       # B6' with c = 1, G4 = G
    flat = sp.simplify(gam - (ell ** 2 / eps ** 2) * eta) == sp.zeros(4, 4)
    return dict(K_is_gamma=sp.simplify(K - gam / ell) == sp.zeros(4, 4), vacuum=lhs == sp.zeros(4, 4),
                q=sp.simplify(tension / sigma), flat=flat)


# ---------------------------------------------------------------------------------- M4 the plane's reading, eq. (13)
def _brane(Fexpr=None):
    rho, M, lam = sp.symbols("rho M lambda", positive=True)
    t, th, ph = sp.symbols("t theta phi", real=True)
    F = sp.Function("F")(rho) if Fexpr is None else Fexpr(rho, M)
    f = 1 - 2 * M / rho
    c15 = sp.Rational(3, 2) if not MUT.get("afpy_misread") else 1
    grr = (1 - lam / rho ** 2 * (rho - 2 * M) / (rho - c15 * M) * (F - rho * sp.diff(F, rho))) / f
    R2 = rho ** 2 + lam * F
    g = sp.diag(-f, grr, R2, R2 * sp.sin(th) ** 2)
    return g, [t, rho, th, ph], (rho, M, lam, F, grr, R2)


def m4():
    if "m4" in _C:
        return _C["m4"]
    g, X, (rho, M, lam, F, grr, R2) = _brane()
    gi, Gam, Ric = _curv(g, X)
    Rs = sp.simplify(sum(gi[a, a] * Ric[a, a] for a in range(4)))
    R1 = sp.simplify(sp.series(Rs, lam, 0, 2).removeO())
    Gmix = [sp.simplify(sp.series(sp.simplify(gi[a, a] * Ric[a, a] - Rs / 2), lam, 0, 2).removeO()) for a in range(4)]
    cf = F_FLW if not MUT.get("fit_sign") else (1, 1.062, 0.554, -0.120)
    FF = sum(sp.nsimplify(c) * (2 * M / rho) ** i for i, c in enumerate(cf))
    sub = lambda e: sp.simplify(e.subs(F, FF).doit())
    grrF = grr.subs(F, FF).doit()
    k2 = sp.simplify(sp.limit(sp.diff(1 - 2 * M / rho, rho) ** 2 / (4 * (1 - 2 * M / rho) * grrF), rho, 2 * M))
    u = sp.Symbol("u", positive=True)
    Rar = sp.sqrt(rho ** 2 + lam * FF)
    gRR = sp.simplify(grrF / sp.diff(Rar, rho) ** 2)
    adm = sp.simplify(sp.series(gRR.subs(rho, 1 / u), u, 0, 2).removeO())
    F1 = FF.subs(rho, 2 * M)
    G = [sub(e) for e in Gmix]
    ev = lambda e, r: float((e * M ** 2 / lam).subs({M: 1, lam: 1}).subs(rho, r))
    pts = (2.0, 2.5, 3.0, 4.0, 6.0, 10.0, 30.0)
    dens = [ev(-G[0], r) for r in pts]                             # 8 pi G rho_E = -G^t_t
    radial = [ev(-G[0] + G[1], r) for r in pts]
    tang = [ev(-G[0] + G[2], r) for r in pts]
    tail = float(sp.limit((-G[0] + G[2]) * rho ** 5 / (lam * M), rho, sp.oo))
    _C["m4"] = dict(R1=R1, k2=k2, adm=adm, F1=F1, dA=float(4 * sp.pi * F1 / 6), rel=float(F1 / 6), dens=dens,
                    radial=radial, tang=tang, tail=tail, pts=pts, generic_G=Gmix)
    return _C["m4"]


# ---------------------------------------------------------------------------------- M5 classical control
def m5():
    lP = math.sqrt(HBAR * G_N / C_LIGHT ** 3)
    curv = lambda ell: 40 * (lP / ell) ** (8.0 / 3)                # 40 (l5/ell)^4, l5^3 = l_P^2 ell
    ell_top = ELL_MAX * 2 ** (-W_TOP / 2)
    ell_1pc = lP * 4000 ** (3.0 / 8)
    w_1pc = 2 * math.log2(ELL_MAX / ell_1pc)
    gstar = 106.75                                                 # the Standard Model's effective count
    bath = lambda r0_ell, ell: gstar * (lP * ell / (r0_ell * ell) ** 2) ** 2 / (5760 * math.pi)
    # the blackbody bound itself, from its parts: g* (pi^2/30) (kT)^4/(hbar c)^3 over sigma = 3 c^4/(4 pi G ell^2)
    ell_c, r0_c = 22.4 * lP, 10 * 22.4 * lP
    kT = HBAR * C_LIGHT / (4 * math.pi * r0_c)
    if MUT.get("bath_hot"):
        kT *= 4 * math.pi                                         # the mutant drops the 4 pi of T_H = hbar c/(4 pi r0)
    u = gstar * math.pi ** 2 / 30 * kT ** 4 / (HBAR * C_LIGHT) ** 3
    sig = 3 * C_LIGHT ** 4 / (4 * math.pi * G_N * ell_c ** 2)
    return dict(floor=curv(ELL_MAX), top=curv(ell_top), top_over_lP=ell_top / lP, ell_1pc=ell_1pc / lP, w_1pc=w_1pc,
                bath=bath(10, ell_c), bath_parts=u / sig)


# ---------------------------------------------------------------------------------- M6 the bounce's map
def m6():
    U, V, x = sp.symbols("U V x", real=True)
    dU, dV, dx = sp.symbols("dU dV dx", real=True)
    A, B, C, D, Fc = [sp.Function(nm) for nm in ("A", "B", "C", "D", "Fc")]
    w = U * V
    # FW's (9) near the horizon in Kruskal form: -A dU dV + B dx^2 + C dOmega^2 (scalar part) + Fc x d(UV) dx
    ds = -A(w, x) * dU * dV + B(w, x) * dx ** 2 + C(w, x) + Fc(w, x) * x * (U * dV + V * dU) * dx
    if MUT.get("map_half"):
        img = ds.subs({U: -U, dU: -dU}, simultaneous=True)       # the mutant reflects one null coordinate only
    else:
        img = ds.subs({U: -U, V: -V, dU: -dU, dV: -dV}, simultaneous=True)
    return dict(isometry=sp.simplify(img - ds) == 0)


# ---------------------------------------------------------------------------------- M7 203
def m7():
    N, Mm, G, hb, c = sp.symbols("N M G hbar c", positive=True)
    S = 4 * sp.pi * G * Mm ** 2 / (hb * c)                        # Schwarzschild's at fixed M (AFPY, first order)
    Msol = sp.solve(sp.Eq(S, N * sp.log(2)), Mm)[0]
    r0 = 2 * G * Msol / c ** 2
    lP2 = hb * G / c ** 3
    Abit = 4 * sp.log(2) * lP2
    same_r0 = sp.simplify(r0 - sp.sqrt(N * Abit / (4 * sp.pi))) == 0
    E = c ** 4 * r0 / (2 * G)
    coef = float((E / sp.sqrt(N)).subs({G: G_N, hb: HBAR, c: C_LIGHT}))
    coef_h = math.sqrt(H_PL * C_LIGHT ** 5 * math.log(2) / (8 * math.pi ** 2 * G_N))
    return dict(same_r0=same_r0, coef=coef, coef_h=coef_h)


# ---------------------------------------------------------------------------------- M8 clause (f)
def m8():
    Mm, r0, ell, G, c = sp.symbols("M r0 ell G c", positive=True)
    rho_bar = 3 * Mm * c ** 2 / (4 * sp.pi * r0 ** 3)
    sigma = 3 * c ** 4 / (4 * sp.pi * G * ell ** 2)
    ratio = sp.simplify((rho_bar / (sigma / 4)).subs(Mm, r0 * c ** 2 / (2 * G)))
    TS = _load("tau_share.py", "m1l_ts")
    cq = TS.consequences(TS.tau_value())
    side2 = cq["side2"]                                           # position 2's side total over lambda_RS
    if MUT.get("own_only"):
        side2 = sp.Rational(-1, 3)                                # the mutant counts P2's own tension alone
    s, w, sig = sp.symbols("s w sigma", positive=True)
    share = side2 * sig * s + w / s                               # crossing share, direction-neutral (W1)
    return dict(ratio=ratio, at10=float(ratio.subs(r0, 10 * ell)), side2=side2, share_pos=bool(share.is_positive))


# ---------------------------------------------------------------------------------- M9 the calculator, clause by clause
CONTS = [(1, "none"), (0, "quantum"), (0, "shell")]
NAMED = {(1, "none"): (1, 1), (0, "quantum"): (0, 0), (0, "shell"): (0, 1)}
CLAUSES = (("a", ["b_interior B5", "273"]), ("be", ["b_interior B6", "273", "m1_large M6"]),
           ("f", ["139 (1)", "275", "276", "284", "285", "tau_share T4", "m1_large M8"]))


def m9():
    if "m9" in _C and not MUT:
        return _C["m9"]
    CA = _load("calculator.py", "m1l_calc")
    IA = _load("index_audit.py", "m1l_ia")
    BI = _load("b_interior.py", "m1l_bi")
    e8 = m8()
    side_pos = bool(e8["side2"] > 0)
    cells = {k: v for k, v in BI.cells().items() if k[2] == "pos2"}
    q = ((0, "quantum"), "-sigma/4", 1)
    attrs = ["c1", "c2", "t", "m"]

    def run(f_rule, analysis):
        cfg = {}
        for (inner, bounce, _), p in cells.items():
            for t, m in itertools.product(("-sigma/4", "+sigma"), (0, 1)):
                cfg[((inner, bounce), t, m)] = dict(a=int(bounce != "shell"), be=p["complete"], f=f_rule(t, m))
        enc = lambda k: NAMED[k[0]] + (int(k[1] == "-sigma/4"), k[2])
        at = enc(q)
        out = {}
        for cl, cites in CLAUSES:
            known = [enc(k) + (r[cl],) for k, r in cfg.items() if k != q]
            r = CA.ask(attrs + [cl], known, at, analysis=analysis if cl == "f" else None, citations=cites)
            aud = IA.audit_index(attrs + [cl], known + [at + (CA.U,)])
            r["void"] = bool(aud["keys"] or aud["onehot"])
            out[cl] = r
        ans = tuple(out[cl]["answer"] for cl, _ in CLAUSES)
        return dict(ans=ans, join=1 if all(a == 1 for a in ans) else 0 if 0 in ans else "not binary",
                    void=any(out[cl]["void"] for cl, _ in CLAUSES))

    # (f) on the side total: positive exactly when what position 2 receives exceeds its own -1/3 lambda_RS
    received_over_own = max(float((e8["side2"] + sp.Rational(1, 3)) / sp.Rational(1, 3)), 1e-12)
    side = run(lambda t, m: int(side_pos or t == "+sigma"),
               {"witness": "tau_share T4: received over P2's own tension", "magnitude": received_over_own,
                "threshold": 1.0})
    own = run(lambda t, m: int(t == "+sigma"),
              {"witness": "m1_large M8: the README's mean density over sigma/4", "magnitude": e8["at10"],
               "threshold": 1.0})
    res = dict(side=side, own=own)
    if not MUT:
        _C["m9"] = res
    return res


def compute():
    return dict(m1=m1(), m2=m2(), m4=m4(), m5=m5(), m6=m6(), m7=m7(), m8=m8(), m9=m9())


def report(o):
    print("m1_large.py -- M1 at the large end, on C3's large brane hole (item 356)\n")
    a = o["m1"]
    print("M1 the Poincare form Einstein with Lambda = -6/ell^2: %s; Kretschmann %s; R(k,k) on a null k: %s"
          % (a["einstein"], a["K"], a["null"]))
    b = o["m2"]
    print("M2 K_mn = gamma_mn/ell: %s; FW (3) vacuum: %s; the tension over sigma: %s; the brane flat: %s"
          % (b["K_is_gamma"], b["vacuum"], b["q"], b["flat"]))
    c = o["m4"]
    print("M4 eq. (13): R to first order %s; kappa^2 %s; g_RR %s; F(1) %s, dA = %.4f ell^2 (%.4f (ell/r0)^2)"
          % (c["R1"], c["k2"], c["adm"], c["F1"], c["dA"], c["rel"]))
    print("   the plane's reading (x lambda/M^2) at rho/M = %s:" % (c["pts"],))
    for nm in ("dens", "radial", "tang"):
        print("     %-7s %s" % (nm, " ".join("%+.3g" % v for v in c[nm])))
    print("   tangential tail rho^5 (G) / (lambda M) -> %.4g" % c["tail"])
    d = o["m5"]
    print("M5 40 (l5/ell)^4: %.2g at the floor, %.2g at the top (ell = %.3f l_P); 1%% at ell = %.1f l_P, w = %.1f; "
          "the flux's bound %.2g of sigma (from parts %.2g)" % (d["floor"], d["top"], d["top_over_lP"], d["ell_1pc"],
                                                               d["w_1pc"], d["bath"], d["bath_parts"]))
    print("M6 (U, V) -> (-U, -V) an isometry of the axisymmetric Kruskal form: %s" % o["m6"]["isometry"])
    e = o["m7"]
    print("M7 r0 from S = N ln2: %s; E/sqrt(N) = %.2f J (from h: %.2f J)" % (e["same_r0"], e["coef"], e["coef_h"]))
    f = o["m8"]
    print("M8 the README's mean density / (sigma/4) = %s, %.3g at r0 = 10 ell; the side total %s lambda_RS; share "
          "positive: %s" % (f["ratio"], f["at10"], f["side2"], f["share_pos"]))
    g = o["m9"]
    print("M9 the calculator: on the side total %s, join %s; on P2's own stress (control) %s, join %s"
          % (g["side"]["ans"], g["side"]["join"], g["own"]["ans"], g["own"]["join"]))


def checks(o):
    res = []
    add = lambda n, ok: res.append((n, bool(ok)))
    add("M0 356, 232 (9) and its reading (c), 203, 256, 273, 275 and 284 (4) verbatim, each inside its own item",
        all(" ".join(w.split()) in _item(n) for n, w in WORDS))
    doc = " ".join(__doc__.split())
    add("M0 the READ quotations of FW and AFPY carried in the clauses", all(qq in doc for qq in QUOTES))
    a = o["m1"]
    add("M1 the Poincare form has R_AB = -(4/ell^2) g_AB and Kretschmann 40/ell^4; the null energy zero on a null ray",
        a["einstein"] and sp.simplify(a["K"] - 40 / sp.Symbol("ell", positive=True) ** 4) == 0 and a["null"] == 0)
    b = o["m2"]
    add("M2 FW's K_mn = gamma_mn/ell on the Poincare form; (3)'s l.h.s. zero; the tension our sigma (q = 1); the brane "
        "flat", b["K_is_gamma"] and b["vacuum"] and b["q"] == 1 and b["flat"])
    c = o["m4"]
    add("M4 AFPY (13): R = 0 to first order for every F; surface gravity 1/(4M); ADM mass M; F(1) = 0.372, dA = "
        "0.779 ell^2, 0.062 (ell/r0)^2", c["R1"] == 0 and sp.simplify(c["k2"] - 1 / (16 * sp.Symbol("M", positive=True)
                                                                             ** 2)) == 0
        and sp.simplify(c["adm"] - (1 + 2 * sp.Symbol("M", positive=True) * sp.Symbol("u", positive=True))) == 0
        and c["F1"] == sp.Rational(93, 250) and "%.3f" % c["dA"] == "0.779" and "%.3f" % c["rel"] == "0.062")
    add("M4 (v) the plane's reading negative outside the horizon -- energy density, radial and tangential null -- the "
        "radial zero on the horizon, the tangential falling as rho^-5",
        all(v < 0 for v in c["dens"]) and abs(c["radial"][0]) < 1e-15 and all(v < 0 for v in c["radial"][1:])
        and all(v < 0 for v in c["tang"]) and c["tail"] < 0 and all(abs(c["tang"][i + 1]) < abs(c["tang"][i])
                                                                    for i in range(len(c["tang"]) - 1)))
    d = o["m5"]
    add("M5 the background's curvature in 5D Planck units 5.9e-79 at the floor, 6.2 at the top; 1% at 22.4 l_P, w = "
        "189.9", "%.2g" % d["floor"] == "5.9e-79" and "%.2g" % d["top"] == "6.2" and "%.1f" % d["ell_1pc"] == "22.4"
        and "%.1f" % d["w_1pc"] == "189.9")
    add("M5 (estimate) the state: the outgoing flux's density near the face at most g* (l_P ell/r0^2)^2/(5760 pi) of "
        "sigma, 1.2e-9 at r0 = 10 ell, ell = 22.4 l_P, g* = 106.75 -- the closed form and the blackbody's parts agree",
        "%.2g" % d["bath"] == "1.2e-09" and abs(d["bath_parts"] / d["bath"] - 1) < 1e-9)
    add("M6 the bounce's map an isometry of the static axisymmetric Kruskal form, FW's dr dx term included",
        o["m6"]["isometry"])
    e = o["m7"]
    add("M7 S = 4 pi G M^2/(hbar c) = N ln2 gives C3's r0; E = 459,404,002.42 J x sqrt(N)",
        e["same_r0"] and abs(e["coef"] - 459404002.42) < 0.5 and abs(e["coef_h"] - e["coef"]) < 0.5)
    f = o["m8"]
    add("M8 the README's mean density inside r0 is 2 ell^2/r0^2 of sigma/4 (0.02 at r0 = 10 ell); the side total "
        "2/3 lambda_RS, the crossing share positive", sp.simplify(f["ratio"] - 2 * sp.Symbol("ell", positive=True) ** 2
                                                                  / sp.Symbol("r0", positive=True) ** 2) == 0
        and abs(f["at10"] - 0.02) < 1e-12 and f["side2"] == sp.Rational(2, 3) and f["share_pos"])
    g = o["m9"]
    add("M9 the calculator clause by clause: 1, 1, 1 on the side total, logic joining 1; the control on P2's own stress "
        "refuses (f), never 1; no verdict void", g["side"]["ans"] == (1, 1, 1) and g["side"]["join"] == 1
        and g["own"]["ans"][2] == "refused" and not g["side"]["void"])
    return res


MUTANTS = {"bulk_sign": "the bulk's Einstein constant taken as +4/ell^2 (M1)",
           "tension_twice": "the Israel term taken as 6/ell, twice the RS tension (M2)",
           "afpy_misread": "AFPY's (rho - 1.5M) read as (rho - M) in eq. (13) (M4)",
           "fit_sign": "F_FLW's linear coefficient taken with the wrong sign (M4)",
           "map_half": "the bounce's map reflecting one null coordinate only (M6)",
           "own_only": "position 2's side counted as its own tension alone, -1/3 lambda_RS (M8, M9)",
           "bath_hot": "the Hawking temperature taken as hbar c/r0, the 4 pi dropped (M5)"}


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
        _C.clear()
        MUT[kk] = True
        try:
            failed = sorted({n.split()[0] for n, ok in checks(compute()) if not ok})
        except Exception as ex_:
            failed = ["raised %s" % type(ex_).__name__]
        MUT.clear()
        _C.clear()
        caught += bool(failed)
        print("  mutant %-14s %-72s %s" % (kk, desc, "caught by " + ", ".join(failed) if failed else "NOT CAUGHT"))
    print("mutants: %d/%d caught" % (caught, len(MUTANTS)))
    return caught == len(MUTANTS)


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    if "--mutants" in sys.argv:
        sys.exit(0 if mutants() else 1)
    report(compute())
