#!/usr/bin/env python3
"""far_large.py -- item 350: the FAR row at the family's large end.  M: "We need to settle FAR at the large end" (350),
after FAR's small end was worked and seated as FARs (far_small.py, 347, 349).  The row: "FAR a far boundary at the
large end consistent with (Z), (G), 139 (1), 166" -- the record's (far_cypher, far_bridge, b4c_far), every computed
candidate failing a requirement.  Worked in the conversation (computed with sympy, exact where marked; READ where
marked; deduced where marked; not verified by a separate session; not seated); 2026-10-13.

  L0 (read) The words the row rests on, verbatim, each checked inside its own item: 139 (1), "1 - yes"; 166, M chose
     "Both planes at once"; 183, M chose "Yes: never violated as a pair"; 226, M chose "Its own values"; 256, M chose
     "One family, both ends (Recommended)" (the option's text: "keep the record's 4D results as the large end"); 273,
     "Quantum bounce to pos 2 (Recommended)"; 275, "Coincident everywhere"; 320, "A consequence of 275 with 276 - no
     bulk is ever empty. It will always contain something wether it is information or matter."; 336, "I think it is
     B"; 350, "We need to settle FAR at the large end".
  L1 (deduced) The question at the large end.  FAR's demand is FARs' (far_small F1): a far surface enclosing the
     corridor, strictly untrapped at every ell, in a bulk where (Z), (G), 139 (1) and 166 hold.  Read under 226, 275, 232
     (2) and 320 exactly as at the small end, the far model is the same coincident pair's two-sided bulk (far_small
     F2).  What differs is the hole.  At the large end it is the record's four-dimensional corridor: Schwarzschild on our
     plane at r0 = 2m (C3 F5, verified 261; 256), with r0 >> ell.  It is larger than the warp's scale, so its field
     reaches into the bulk.  ell itself runs from 14 um down to about 2 l_P (the board's question at 256), and the large
     end begins at N = (pi^2/2 ln2)(ell/l_P)^2: 5.3e60 bits at ell = 14 um, and 28 bits at 2 l_P (computed).
  L2 (computed, imported) The background: far_small F2 and F3 hold at both ends.  Every side of the pair is AdS, its
     warp decaying away from the pair at every position 2 the record holds, and on it every far surface with W >= U is
     strictly untrapped at every ell.
  L3 (READ; computed) The large hole's far field in the bulk.  READ: Garriga and Tanaka, arXiv:hep-th/9911055v4, eq.
     (16), the static Green's function with one point on the wall, "G(x, y, x', 0) ~ -(a^3/(8 pi ell)) (2 a^2 r^2 + 3
     ell^2)/(a^2 r^2 + ell^2)^(3/2)"; p. 5, "the metric perturbation decays rather steeply towards the AdS horizon ...
     (in fact even the relative metric perturbation h_munu/a^2 falls to zero as we move away from the source)"; p. 6,
     the metric components fall off as the Green's function does; eq. (23), on the wall h_00 = (2GM/r)(1 + 2 ell^2/
     (3 r^2)).  In conformal coordinates (a = ell/Z, Z the Poincare depth) the relative perturbation is proportional to
     (2 r^2 + 3 Z^2)/d^3, d^2 = r^2 + Z^2 (computed): 2m/r along the wall, as eq. (23) leads, and 3m/Z down the axis.
     The axis-to-wall ratio is 3/2, reproduced from the bulk graviton's own static mode Z^2 K_2(pZ), whose integral
     int q^2 K_2(q) dq = 3 pi/2 (computed).  The board's form H-GT-IN-WARP takes the spatial metric conformally flat,
     (ell/Z)^2 (1 + Phi) delta, Phi = m (2 u^2 + 3 Z^2)/d^3 -- Garriga-Tanaka's falloff and its angular profile,
     a test form like far_small's H-HOLE-IN-WARP, valid in the linear regime d >> m and d >> ell.  Its gradient obeys
     |grad Phi| <= 3 m/d^2, the maximum on the axis (computed).
  L4 (computed, exact in the test form; deduced where marked) The far surface around the large hole.  With z = ell + w,
     D and P as in far_small F3, and n the flat normal of T_E,
         theta+ = (z P - 3 w/W^2 + (3 z D/(2 f)) n . grad Phi)/(ell f^(1/2) D),      f = 1 + Phi
     (checked against b4c_far's level-set theta+ at sample points; the lapse does not enter).  (a) A round surface (W =
     U) is trapped at its tip exactly when 2 f ell (ell + U) < 3 m U, f = 1 + 3m/(ell + U) there: exactly when ell <
     (3/2) m and U > 2 ell (ell + 3m)/(3m - 2 ell) (computed).  At the large end (ell << m) that is every U past about 2
     ell, so every round surface in the test form's range (U >> m) is trapped, however large U is.  In AdS the round
     surface's tip is nearly marginal: in units of the AdS scale its expansion is 3 ell/U, the background carrying no
     margin in w (far_small F3, Q - 3 = 0 at K = 1), while the hole's pull, 9m/(2U) in the same units, does not fall
     with ell.  (b) An elongated surface, W > U, is strictly untrapped at every point and EVERY ell when U >= (9/4) m
     K/(K - 1), K = W^2/U^2 (deduced: Q - 3 >= 2 (K - 1), far_small F3's z3; d >= U and D <= 1/U on T_E; |grad Phi| <=
     3m/d^2).  With eq. (17)'s coefficient 5/4 as the plane's reading in place of Schwarzschild's 1 (M1 open at the large
     end), the bound is (45/16) m K/(K - 1).  (c) Computed: theta+ U is positive over T_E wherever (b) holds, at K = 1.5
     and 3, U/m from 30 to 4.2e5 and ell/m from 1e-6 to 10; the round surface's tip is negative at every ell/m up to 1
     and U/m from 30 to 1e9 sampled, and its sign follows (a)'s threshold on both sides of it.  So at the large end FAR
     has its answer in the test form: a far surface deeper than it is wide, and large enough, is strictly untrapped at
     every ell; a round one is not.
  L5 (READ; computed) The surface encloses the hole's bulk horizon, and the size it needs.  READ: Figueras and Wiseman,
     arXiv:1105.2558v2 -- static large black holes in RS II "with radius up to ~ 20 ell", the brane geometry tending to
     four-dimensional Schwarzschild with corrections O(ell^2/R_4^2), the bulk tending to the Poincare horizon far away,
     and "the horizon is pancake-like ... with a proper distance to the tip going as ~ ell log(R_4/ell)".  The proper
     depth below the wall at Poincare depth Z is ell ln(Z/ell), so the tip lies at Z of order R_4 = 2m (deduced).  The
     record's cover at its own README, U = 1.05 R_reach = 1.05 (2 + 2 T) m (b4c_far) with T = 199,702.19 clocks of m/c
     (o3_write), is U/m = 419,377, about 2e5 times that depth, and (b) holds for every K >= 1 + 5.4e-6 there
     (computed).  Near the large end's smallest READMEs (28 bits at ell = 2 l_P) the cover is U/m = 7.05 and the field is
     not weak there, but the surface can be taken as large as wanted: (b)'s bound K/(K - 1) <= 4U/(9m) loosens as U
     grows, so every K > 1 works at a large enough U, the linear regime included (deduced).
  L6 (deduced; computed where marked) Through the write, the arrival and the hole's life.  The field at T_E is the
     whole mass's at most, m: what crosses T_E as radiation is positive outside the face, and what the arrival brings
     in was counted in m before it crossed (energy conservation).  At the record's cover the relative perturbation is
     at most 3m/U = 7.2e-6 (computed), deep in the linear regime, and Garriga-Tanaka's KK correction is O(ell^2/d^2).
     The bulk's content (320) traps T_E only if its own mass enters the same bound, (9/4) m_content K/(K - 1) > U
     (deduced).
  L7 (deduced) (Z), (G), 139 (1) and 166 in this far model.  The bulk, the pair and the crossing rays are far_small
     F6's: each side Einstein, the summed tension positive at every position 2, matter pointwise (320).  (G) at the
     large end is the record's four-dimensional corridor (256; C3 F5); L4 needs only its monopole, so it holds whatever
     M1, open at the large end, gives as the plane's reading (Schwarzschild's 1 or eq. (17)'s 5/4).  The rays that meet
     the corridor are Z3b's, OPEN at the large end: FAR's (Z) is the far region's, and does not decide Z3b.
  L8 (computed, imported) FAR's question through the calculator, in the form C4's stands in (291): its classes at the
     large end -- t, the far surface W > U with U past L4 (b)'s bound, or W <= U; m, the coincident two-sided bulk
     with the large hole, or the record's column model -- have the populations of far_small F7 (f1: {(1, 1): {1},
     (0, 1): {0}, (1, 0): {0, 1}, (0, 0): {0}}, from L4 and b4c_far X2-X3; f2: (Z) the model coordinate's), so the
     calculator's answers are F7's: neither clause decided under either protocol, f2's index flagged and void.
  L9 (item 350, the residue pass of 314, applied from the start; deduced, and computed where marked) What L0-L8 claim
     without establishing, or rest on without naming.  (a) L0's words are checked inside the item each is cited to (348
     (Q11)).  (b) The test form's range.  H-GT-IN-WARP is linear in Phi: it needs d >> m and d >> ell, and d >= U on T_E,
     so it holds wherever U >> m; at the record's cover 3m/U = 7.2e-6 (computed).  Within it L4 (a)'s threshold is exact
     and L4 (b)'s bound sufficient, not sharp.  (c) What carries beyond the test form.  The round surface's failure needs
     only that the hole's pull at the tip be of order m/U^2: at ell << m it survives any change of the pull's
     coefficient by less than a factor (3m/2)/ell.  The elongated surface's success needs only a gradient bound |grad
     Phi| <= c m/d^2 with c of order one.  Its least theta+ U over T_E is at the rim, where T_E meets the pair: 2 + 1/K
     with no hole, lowered by 5.1e-6 of itself at the record's cover (computed, K = 1.5).  (d) The two-sided
     pair.  Garriga-Tanaka's field is the Z2-symmetric single wall's.  On the coincident pair each side's amplitude
     differs from it by a factor of order one -- at most 2 if one side carried the whole flux (estimate) -- and ell
     differs per side (ell+ = 2 ell at 139 (1)'s quarter), which (b)'s bound does not see.  At the record's cover the
     bound has a factor 6.2e4 to spare at K = 1.5 (computed).  (e) Time dependence.  L4 is static.  Through the write and
     the arrival the field at T_E changes, and an outgoing pulse crossing T_E focuses theta+ by Raychaudhuri's equation
     by at most of order its energy's share of m/U^2 (estimate): the order of the static lowering in (c), five orders
     below the margin at the record's cover.  (f) m is the hole's mass as read on our plane (r0 = 2m; 256, C3 F5).  With
     eq. (17)'s 5/4 (M1, open at the large end) the bound moves to (45/16) m K/(K - 1) and the round tip's threshold to
     ell < (15/8) m.  (g) The Figueras-Wiseman horizon's depth, Z of order R_4, is an order of magnitude deduced from
     their READ proper depth; T_E encloses it at any cover U >> R_4.  (h) "Every ell": L4 (b)'s bound does not contain
     ell; the round tip's threshold does.  The large end's ell runs from 14 um to 2 l_P (256), and near l_P the classical
     bulk is beyond control (the does-not list).  (i) The rests-on: M's 139 (1), 166, 183, 226, 256, 273, 275, 320, 336
     and 350, with 232 (2), 210 and 328 (B8); the verified C3 (261) and B5a (339); FARs' instrument (far_small F2, F3,
     F6, F7 -- FARs not yet finalized, 350 (a)); o3_write's floor; b4c_far's level-set theta+ and its cover; the READ
     Garriga-Tanaka and Figueras-Wiseman; and the board's readings -- H-GT-IN-WARP, the record's cover, and 166 under
     275 as at the small end.  (j) What is exact and what is not: L2 (far_small F2, F3), L3's transforms and integral,
     and L4 (a)'s tip and threshold are exact given the test form; L4 (c) is sampled; L5's depth, L6, (d) and (e) are
     orders of magnitude.  (k) Nothing in L0-L8 uses T_E in a censorship theorem: that use stays B4's and B4d's (the
     does-not list).
  L10 (item 351, M-ACCOUNT-BEFORE-VERIFY's gate, 330; deduced) The verifications so far, carried where they bear at the
     large end (verify_ledger's FAR column; far_small F10 carries the rest, F2-F7 being the background here too).  (a)
     261 (Q1)-(Q2): the large end's start, N = (pi^2/2 ln2)(ell/l_P)^2 (L1), is the two-end construct's switch, a
     convention, and the construct jumps there (its E by x1.88), while the physical family is one smooth branch
     (Figueras-Wiseman).  L4's bound holds at every ell and at every U past it, so the switch moves no conclusion; L1's
     28-bit end at 2 l_P is a Planck-scale extrapolation outside semiclassical control (261 (Q2)), as the does-not list
     says.  (b) 267 (Q6): the record's floor is the write's least time; a longer write's cover is larger, and L4 (b)'s
     bound loosens as U grows.  (c) 261 (Q3): the large end is four-dimensional Schwarzschild on the plane with
     corrections O(ell^2/r0^2), non-extremal; L4 uses only its monopole m.  (d) 310 (outside G5): the large end's figures
     are in m and ell; G5 enters only through each side's amplitude, L9 (d)'s factor of order one.  (e) 337 (Q9), 348
     (Q11): L0's 256, 273 and 275 are the options M chose, their texts the board's.

What this does not claim.
  - The exact large hole on the two-sided bulk: Figueras-Wiseman's construction is numerical, Z2-symmetric and
    reaches about 20 ell; beyond that it rests on their AdS5-CFT4 limit, against the conjecture they cite that large
    static brane holes do not exist (Tanaka; Emparan, Fabbri and Kaloper).
  - The use of T_E in a censorship theorem (CGS's pointwise null energy premise, global hyperbolicity): B4's and B4d's.
  - Z3b, the rays that meet the corridor at the large end; M1, the plane's reading of the mouth there.
  - ell near l_P: F3 holds at every ell, but the classical bulk at ell ~ l_P is beyond any controlled range.
  - The README's source on the plane at the large end (SOURCE, deferred, 344-346).

Imports far_small.py, b4c_far.py and o3_write.py by path.  Stdlib + sympy.  python3 far_large.py [--selftest | --mutants]
"""
import contextlib
import importlib.util
import io
import math
import os
import re
import sys

import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
D68 = os.path.dirname(HERE)
RULINGS = os.path.join(D68, "M-RULINGS-2026-10-03.md")
MUT = {}
WORDS = ((139, 'M, verbatim: "1 - yes 2 - positive, and you have to prove it.'), (166, 'M chose: "Both planes at once"'),
         (183, 'M chose: "Yes: never violated as a pair"'), (226, 'M chose: "Its own values"'),
         (256, 'M chose, verbatim: "One family, both ends (Recommended)"'),
         (256, "keep the record's 4D results as the large end"), (273, '"Quantum bounce to pos 2 (Recommended)"'),
         (275, 'verbatim: "Coincident everywhere"'),
         (320, '"A consequence of 275 with 276 - no bulk is ever empty. It will always contain something wether it is '
               'information or matter."'), (336, '"I think it is B"'), (350, '"We need to settle FAR at the large end"'))
HBAR, C_LIGHT, G_N = 1.054571817e-34, 299792458.0, 6.67430e-11
ELL_MAX = 13.964e-6
_MOD = {}


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


def FS():
    return _load("far_small.py", "fl_fs")


# ---------------------------------------------------------------------------------- L1 the large end's range
def l1():
    lP = math.sqrt(HBAR * G_N / C_LIGHT ** 3)
    nl = lambda ell: (math.pi ** 2 / (2 * math.log(2))) * (ell / lP) ** 2
    return dict(N_L_max=nl(ELL_MAX), N_L_min=nl(2 * lP))


# ---------------------------------------------------------------------------------- L3 the far field in the bulk
def l3():
    r, Z, ell, a, d, al = sp.symbols("r Z ell a d alpha", positive=True)
    G = a ** 3 * (2 * a ** 2 * r ** 2 + 3 * ell ** 2) / (a ** 2 * r ** 2 + ell ** 2) ** sp.Rational(3, 2)   # eq. (16)
    rel = sp.simplify((G / a ** 2).subs(a, ell / Z))              # the relative perturbation, up to its constant
    want = ell ** 2 * (2 * r ** 2 + 3 * Z ** 2) / (r ** 2 + Z ** 2) ** sp.Rational(3, 2) / ell ** 2
    shape_ok = not (sp.simplify(rel / want).free_symbols & {r, Z})  # the same shape in r and Z, up to a constant
    ratio = sp.limit((2 * r ** 2 + 3 * Z ** 2) / (r ** 2 + Z ** 2) ** sp.Rational(3, 2) * Z, r, 0) / \
        sp.limit((2 * r ** 2 + 3 * Z ** 2) / (r ** 2 + Z ** 2) ** sp.Rational(3, 2) * r, Z, 0)
    q = sp.Symbol("q", positive=True)
    kint = sp.integrate(q ** 2 * sp.besselk(2, q), (q, 0, sp.oo))
    # |grad Phi|^2 d^4/m^2 for Phi = m (2 + cos^2 alpha)/d, over the angle
    t = sp.Symbol("t", nonnegative=True)                           # t = cos^2 alpha in [0, 1]
    g2 = sp.expand((2 + t) ** 2 + 4 * t * (1 - t))
    c2 = max(g2.subs(t, tv) for tv in sp.solve(sp.diff(g2, t), t) + [0, 1] if 0 <= tv <= 1)
    c = 2.5 if MUT.get("profile_wall_only") else float(sp.sqrt(c2))  # the mutant: the wall's coefficient taken
    return dict(rel=rel, shape_ok=shape_ok, ratio=ratio, kint=kint, c=c)


# ---------------------------------------------------------------------------------- L4 the far surface
def _phi_metric(s=1):
    B = FS().BF()
    u, w, ell = B.u, B.w, B.ell
    m = sp.Symbol("m", positive=True)
    Z = ell + w
    d2 = u ** 2 + Z ** 2
    Phi = m * (2 * u ** 2 + 3 * Z ** 2) / d2 ** sp.Rational(3, 2)
    if MUT.get("profile_isotropic"):                               # the mutant: four-dimensional 2m/d, not GT's profile
        Phi = 2 * m / sp.sqrt(d2)
    return B, m, Phi


def _closed():
    B, m, Phi = _phi_metric()
    u, w, U, W, ell = B.u, B.w, B.U, B.W, B.ell
    D = sp.sqrt(u ** 2 / U ** 4 + w ** 2 / W ** 4)
    P = 1 / (U ** 2 * W ** 2 * D ** 2) + 2 / U ** 2
    z = ell + w
    f = 1 + Phi
    ndphi = (u / U ** 2 * sp.diff(Phi, u) + w / W ** 2 * sp.diff(Phi, w)) / D
    k = -1 if MUT.get("field_sign") else 1                        # the mutant: the hole's pull taken outward
    return (z * P - 3 * w / W ** 2 + k * 3 * z * D / (2 * f) * ndphi) / (ell * sp.sqrt(f) * D), m


def l4():
    B, m, Phi = _phi_metric()
    u, w, U, W, ell = B.u, B.w, B.U, B.W, B.ell
    th, _ = _closed()
    Om = ell / (ell + w)
    rec = B.theta_plus(B.ELLIPSE, (Om, Om ** 2 * (1 + Phi), Om ** 2 * (1 + Phi), Om ** 2 * (1 + Phi) * u ** 2))
    agree = True
    for row in (("17/10", "23/10", "11", "1/50", "11/10"), ("2", "5", "3", "1/10", "1"), ("3", "4", "1/2", "1/5", "2")):
        Uv, Wv, lv, mv, uv = (sp.Rational(x) for x in row)
        sub = {U: Uv, W: Wv, ell: lv, m: mv, u: uv, w: Wv * sp.sqrt(1 - (uv / Uv) ** 2)}
        a1, a2 = sp.N(rec.subs(sub), 40), sp.N(th.subs(sub), 40)
        agree &= abs(a1 - a2) < sp.Float("1e-30") * max(1, abs(a1))
    # (a) the round surface's tip
    tip = sp.simplify((th * ell * sp.sqrt(1 + Phi) * sp.sqrt(u ** 2 / U ** 4 + w ** 2 / W ** 4)).subs(W, U).subs(
        {u: 0, w: U}))
    fz = 1 + 3 * m / (ell + U)
    tip_want = 3 * ell / U ** 2 - 9 * m / (2 * fz * U * (ell + U))
    lin = 2 * ell * (ell + 3 * m) - (3 * m - 2 * ell) * U            # the tip's sign, times 2 U^2 (ell + U + 3m)/3 > 0
    tip_ok = sp.simplify(tip - tip_want) == 0 and sp.simplify(tip_want * 2 * U ** 2 * (ell + U + 3 * m) / 3 - lin) == 0
    # (c) sampled
    thf = sp.lambdify((u, w, U, W, ell, m), th, "math")
    c = l3()["c"]
    pos, cnt = True, 0
    for Kv in (1.5, 3.0):
        bound = 0.75 * c * Kv / (Kv - 1)
        for Um in (30.0, 1e3, 4.19377e5):
            if Um < bound:
                continue
            for lm in (1e-6, 1e-3, 0.1, 1.0, 10.0):
                for i in range(1, 50):
                    tau = i / 50.0
                    uv, wv = Um * (1 - tau ** 2) / (1 + tau ** 2), math.sqrt(Kv) * Um * 2 * tau / (1 + tau ** 2)
                    val = thf(uv, wv, Um, math.sqrt(Kv) * Um, lm, 1.0) * Um
                    pos &= val > 0
                    cnt += 1
    # the least theta+ U over T_E, at the record's cover: where, and how far the hole lowers it
    Ur, Kr, lr = 419376.69, 1.5, 1e-3
    pts = [(Ur * (1 - t ** 2) / (1 + t ** 2), math.sqrt(Kr) * Ur * 2 * t / (1 + t ** 2)) for t in
           (i / 400.0 for i in range(401))]
    with_m = [thf(a_, b_, Ur, math.sqrt(Kr) * Ur, lr, 1.0) * Ur for a_, b_ in pts]
    no_m = [thf(a_, b_, Ur, math.sqrt(Kr) * Ur, lr, 0.0) * Ur for a_, b_ in pts]
    rim = dict(at=with_m.index(min(with_m)), least=min(with_m), bare=min(no_m), low=1 - min(with_m) / min(no_m))
    tipf = sp.lambdify((U, ell, m), tip_want, "math")
    # the large end (ell << m), the test form's range (U >> m): every round tip trapped, however large U is
    round_trapped = all(tipf(Um, lm, 1.0) < 0 for Um in (30.0, 1e3, 4.19377e5, 1e9) for lm in (1e-6, 1e-3, 0.1, 1.0))
    # the threshold, both sides: trapped exactly when ell < 3m/2 and U > 2 ell (ell + 3m)/(3m - 2 ell)
    thr = lambda lm: 2 * lm * (lm + 3) / (3 - 2 * lm)
    round_free = all((tipf(Um, lm, 1.0) < 0) == (lm < 1.5 and Um > thr(lm)) for lm in (0.1, 1.0, 1.4, 1.6, 2.0, 10.0)
                     for Um in (0.5, 3.0, 30.0, 61.0, 62.0, 1e3, 1e6)) and tipf(30.0, 1.4, 1.0) > 0 < tipf(1e3, 2.0, 1.0)
    return dict(agree=agree, tip_ok=tip_ok, pos=pos, cnt=cnt, round_trapped=round_trapped, round_free=round_free,
                rim=rim)


# ---------------------------------------------------------------------------------- L5 the cover and the horizon
def l5():
    O = _load("o3_write.py", "fl_o3")
    T_rec = float(O.t_min(3).subs({O.N: 2742570311524972, O.Z: sp.Rational(10875, 100)}))
    reach = (lambda T: 2 + T) if MUT.get("cover_reach") else (lambda T: 2 + 2 * T)   # the mutant: the gas ball's radius
    U_rec = 1.05 * reach(T_rec)
    c = l3()["c"]
    kmin = lambda Um: 1 + 1 / (Um / (0.75 * c) - 1)                 # K/(K-1) <= 4U/(3cm)
    T_small = float(O.t_min(3).subs({O.N: l1()["N_L_min"], O.Z: sp.Rational(10875, 100)}))
    U_small = 1.05 * reach(T_small)
    return dict(T_rec=T_rec, U_rec=U_rec, kmin_rec=kmin(U_rec), U_small=U_small, kmin_small=kmin(U_small),
                h_rec=3 / U_rec, kmin_100=kmin(100.0), spare=U_rec / (0.75 * c * 1.5 / 0.5))


def compute():
    return dict(l1=l1(), l3=l3(), l4=l4(), l5=l5(), fs=dict(f2=FS().f2(), f3=FS().f3(), f7=FS().f7()))


def report(o):
    print("far_large.py -- the FAR row at the large end (item 350)\n")
    a = o["l1"]
    print("L1 the large end begins at N = %.3g (ell = 14 um) and %.3g (ell = 2 l_P)" % (a["N_L_max"], a["N_L_min"]))
    b = o["l3"]
    print("L3 Garriga-Tanaka (16) in conformal coordinates: %s; axis/wall %s; int q^2 K_2 = %s; |grad Phi| d^2/m <= %s"
          % (b["rel"], b["ratio"], b["kint"], b["c"]))
    c = o["l4"]
    print("L4 closed form = b4c_far's theta+: %s; the round tip exact: %s; elongated surfaces positive (%d points): %s;"
          " round tip trapped at the large end: %s (threshold both sides: %s); least theta+ U at the rim (point %d): "
          "%.6f, %.6f with no hole, lowered by %.2g" % (c["agree"], c["tip_ok"], c["cnt"], c["pos"], c["round_trapped"],
                                                      c["round_free"], c["rim"]["at"], c["rim"]["least"],
                                                      c["rim"]["bare"], c["rim"]["low"]))
    d = o["l5"]
    print("L5 the record's floor %.2f clocks, cover U/m = %.0f, K >= %.7f there; smallest READMEs U/m = %.2f (K >= %.2f "
          "at that cover; %.4f at U/m = 100); 3m/U = %.2g" % (d["T_rec"], d["U_rec"], d["kmin_rec"], d["U_small"],
                                                            d["kmin_small"], d["kmin_100"], d["h_rec"]))


def checks(o):
    res = []
    add = lambda n, ok: res.append((n, bool(ok)))
    add("L0 139 (1), 166, 183, 226, 256, 273, 275, 320, 336 and 350 verbatim, each inside its own item",
        all(" ".join(w.split()) in _item(n) for n, w in WORDS))
    a = o["l1"]
    add("L1 the large end begins at 5.3e60 bits at ell = 14 um and 28 bits at 2 l_P",
        "%.2g" % a["N_L_max"] == "5.3e+60" and round(a["N_L_min"]) == 28)
    fs = o["fs"]
    add("L2 the background imported: far_small F2 (every position 2's side decaying) and F3 (W >= U untrapped at every "
        "ell, z3 with its guard)", all(d["sigma_plus"] > 0 for d in fs["f2"]["dest"].values())
        and fs["f3"]["proved"] and fs["f3"]["vacuity_guard"] and fs["f3"]["floor_ok"])
    b = o["l3"]
    add("L3 Garriga-Tanaka's (16) as (2 r^2 + 3 Z^2)/d^3 in conformal coordinates; axis/wall 3/2; int q^2 K_2(q) dq = "
        "3 pi/2; |grad Phi| <= 3 m/d^2", b["shape_ok"] and b["ratio"] == sp.Rational(3, 2)
        and sp.simplify(b["kint"] - 3 * sp.pi / 2) == 0 and abs(b["c"] - 3) < 1e-12)
    c = o["l4"]
    add("L4 the closed form is b4c_far's theta+; the round tip trapped exactly when 2 f ell (ell + U) < 3 m U; "
        "elongated surfaces past (9/4) m K/(K - 1) positive at every point sampled and every ell; the round tip "
        "trapped at the large end at every U sampled, its sign following the threshold on both sides",
        c["agree"] and c["tip_ok"] and c["pos"] and c["cnt"] > 500 and c["round_trapped"] and c["round_free"])
    d = o["l5"]
    add("L5 the record's floor 199,702.19 clocks, cover U/m = 419,377, any K >= 1 + 5.4e-6; the smallest READMEs' "
        "cover U/m = 7.05, every K > 1 at a large enough U; 3m/U = 7.2e-6 at the record's cover",
        abs(d["T_rec"] - 199702.19) < 0.01 and round(d["U_rec"]) == 419377 and "%.2g" % (d["kmin_rec"] - 1) ==
        "5.4e-06" and "%.3g" % d["U_small"] == "7.05" and "%.2g" % d["h_rec"] == "7.2e-06" and d["kmin_100"] < 1.03)
    z = fs["f7"]
    r_ = c["rim"]
    add("L8 the calculator: FARs' populations at the large end, its answers F7's -- neither clause decided",
        z["f1"]["out"][2].get(("both",)) == 96 and z["f2"]["flagged"] == 96)
    add("L9 the residue's figures: the least theta+ U over T_E at the rim, 2 + 1/K with no hole, lowered by 5.1e-6 at "
        "the record's cover; the bound's spare factor 6.2e4 at K = 1.5", r_["at"] == 0 and abs(r_["bare"] - 8 / 3.0)
        < 1e-4 and "%.2g" % r_["low"] == "5.1e-06" and "%.2g" % d["spare"] == "6.2e+04")
    # [item 351] the gate's rows at the large end, each named in L10 (the mutant: L10 left unwritten)
    doc = __doc__ if not MUT.get("gate_unwritten") else __doc__.split("  L10 (item 351")[0]
    l10 = " ".join(doc.split("  L10 (item 351")[1].split("What this does not claim")[0].split()) \
        if "  L10 (item 351" in doc else ""
    add("L10 (item 351) the gate: every row carried at the large end named in L10",
        all(g in l10 for g in ("261 (Q1)-(Q2)", "267 (Q6)", "261 (Q3)", "310 (outside G5)", "337 (Q9)")))
    return res


MUTANTS = {"profile_wall_only": "the far field's gradient taken at the wall's coefficient, not the axis's (L3)",
           "field_sign": "the hole's pull on the far surface taken outward (L4)",
           "profile_isotropic": "the far field taken as four-dimensional 2m/d, not Garriga-Tanaka's profile (L4)",
           "cover_reach": "the cover taken on the write's gas ball (2 + T) m, not R_reach = (2 + 2T) m (L5)",
           "gate_unwritten": "the verifications' rows that bear at the large end left uncarried (L10; item 351)"}


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
            failed = sorted({n.split()[0] for n, ok in checks(compute()) if not ok})
        except Exception as ex_:
            failed = ["raised %s" % type(ex_).__name__]
        MUT.clear()
        caught += bool(failed)
        print("  mutant %-17s %-70s %s" % (kk, desc, "caught by " + ", ".join(failed) if failed else "NOT CAUGHT"))
    print("mutants: %d/%d caught" % (caught, len(MUTANTS)))
    return caught == len(MUTANTS)


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    if "--mutants" in sys.argv:
        sys.exit(0 if mutants() else 1)
    report(compute())
