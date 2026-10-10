#!/usr/bin/env python3
"""forming_rim.py -- the rim while the corridor forms (198 (a)): can the README's inflow, at a rim that moves, supply
both the force balance and the null energy?  Put to the cypher (computed, deduced; flat limit; thin sheets; checked by
four independent verifiers whose findings are folded in below; not seated; 2026-10-10).

rim_readme.py left the static finite-ell rim with no closing arrangement on M's guess 198 and named what was left: the
forming phase (198 (a): "the README comes in while the corridor forms, with no partner, the size growing as it comes in
(94) and fixed once the whole README is in").  R7 fixed a tension count at the rim -- outside sigma, inside ours sigma
and position 2's sigma, corridor -sigma (R5) -- and nothing computed pins the geometry.

  F0 (deduced; checked by enumeration) R7's count cannot be realised as a line junction of three one-sided planes
     (bulk on one side, nothing on the other) and a two-sided corridor (position 1's bulk against position 2's): going
     round the rim each one-sided sheet switches bulk and nothing, a closed loop switches an even number of times, and
     three is odd.  So the arrangements below are FORCE DIAGRAMS, not spacetimes.  R7's count is realisable in the Z2
     double cover (every plane two-sided, its mirror image across our plane reaching the rim), which brings the images
     of the corridor and of position 2's sheet into the balance (F3b (i))
  Arrangements run (the board's; none is M's; 202 says the meeting is symmetric "by this item, not by a reflection",
  so it fixes only that ours and position 2's sheets mirror each other across the corridor -- it chooses none of these):
     B  corridor_shape.py's frame: our plane flat through the rim (kink 0), the corridor at theta, position 2's sheet
        its mirror at 2 theta.  The steep angle of the marginal corridor was measured in this frame
     C  the outside sheet collinear with the corridor, ours and position 2's at +-theta (our plane kinks by theta,
        out of its own bulk, so that the corridor lies on its bulk side)
     A  R7's own force check (both inside sheets along the plane, the corridor tilted): a force diagram only -- it
        leaves no room for position 2's bulk, against 203, at theta != 0
  F1 (computed) a pure-tension sheet's stress is invariant under boosts along itself, so the sheets that lie along the
     rim's sliding direction are unchanged in the rim's rest frame; a tilted sheet is not (L T L^T - T is proportional
     to sin alpha) -- it must co-move with the rim, and its angle aberrates, tan alpha' = tan alpha / gamma.  So B's
     mirror relation holds in one frame only.  The verdicts below still transfer, because each holds at every theta
     and B's holds for every tilt of position 2's sheet (F3 B)
  F2 (computed) a flow arriving along sheet i and leaving along sheet j pushes the rim by -T^nn (e_i + e_j): to the rim
     it is a pressure added to both sheets, with T^nn = (rho + p) gamma^2 v^2 + p the flow's momentum flux along the
     sheet.  The NEC (rho + p >= 0) gives only T^nn >= p: T^nn >= 0 holds for dust, null dust and radiation (p >= 0),
     not for every NEC-obeying README -- rho = 2 sigma, p = -1.5 sigma, v^2 = 1/2 obeys the NEC strictly with T^nn =
     -sigma
  F3 (computed) premises: (P1) the flow leaves the rim with the flux it brought, forward (no reflection, no absorption);
     (P2) T^nn >= 0; (P3) no stress at the rim itself (no ring); (P4) no Z2 images at the rim.  With g_k = e_out + e_k,
     the pure-tension residual is sigma (g_ours + g_p2 - g_corr) and a split w pushes -T^nn sum w_k g_k.  Then:
     B  the split solves uniquely as position 2's share +sigma and the corridor's -sigma, at every theta: opposite
        signs, so no forward split of one flow balances, of either sign -- for ANY tilt phi of position 2's sheet,
        since det[g_p2, g_corr] = 4 sin(theta/2) sin(phi/2) sin((phi - theta)/2) != 0 unless they coincide
     C  the flux onto the two plane sheets must be exactly 2 sigma (any share into the corridor is free and exerts no
        force); the README's pressure then cancels the inside sheets' tension
     A  the corridor's share needs T^nn = -sigma -- excluded by (P2), allowed by the NEC (F2)
     So in corridor_shape's frame, under (P1)-(P4), the README's inflow cannot balance the steep rim
  F3b (computed) each premise dropped, the value it takes:
     (i)   Z2 images at the rim, B: the normal force cancels by symmetry; README into the corridor and its image balances
           at every theta in (0, pi/2) with T^nn = 2 sigma (1 + 2 cos theta) -- the route 198 (a) and R0 name
     (ii)  a ring at the rim (a 2-sphere of radius a, tension lambda, pulling 2 lambda / a toward the mouth's axis,
           in the plane): C balances with lambda = a sigma (1 - cos theta); B with images with
           lambda = a sigma (1 - cos theta)(1 + 2 cos theta); A and B without images never (their residual has a
           component normal to the plane).  A ring with energy density equal to its tension obeys the NEC.  Static:
           it needs no README, so it lasts through the hold
     (iii) a README carrying tension: A balances with T^nn = -sigma (NEC-compatible, F2)
     (iv)  a kink in our plane: with the corridor at kappa and ours, position 2's at kappa -+ theta, a non-negative
           split balances for every kappa strictly between B's (pi - theta) and pi + theta; C is kappa = pi
     (v)   reflection: B balances at theta = pi/3 with pure reflection back along the outside sheet, T^nn = sigma/2
           (absorption needs the rim to have stress-energy of its own -- a ring)
     [CORRECTED, item 208 (ring_consistent.py; the item-208 critics confirmed the sign): this ring is positive only b
     ecause the corridor's sheet is given -sigma at the rim (TENS['corr'] = -1, rim_readme R5's coincidence law for f
     acing sheets) while the meeting angle comes from the tilted marginal corridor.  With the marginal corridor's own
      tension (rho_rim > 0, rho + p_r = 0) the balance asks lambda = -(cos 2t + tau cos t) a sigma < 0: a junction in
      compression.  The computation below is kept as it was; its premise is refuted.]
  F4 (computed) null energy the README supplies: null dust Phi l l gives T(l,l) = 0 along its own infall rays and
     4 Phi, Phi along the opposite radial and the tangential rays (n, k_t with unit time component in the rim frame);
     timelike dust gives rho (u.k)^2 > 0 along every null k (u.k = -gamma (1 + v cos alpha), 1 + v cos alpha >= 1 - v)
  F5 (computed) the hold, T^nn = 0 (198 (a): the README all in): with no ring, none of A, B, C, B-with-images balances
     at any theta in (0, pi/2) -- a pure-tension rim balances only when the corridor coincides with an inside sheet
     (R7's tangency).  With a ring, C and B-with-images balance at every theta in (0, pi/2) with lambda > 0
  F6 (ESTIMATE, the board's; a scale comparison, not the README's density at the rim during inflow) E = c^4 m/G spread
     over r < 2.15m has mean density (ell/m)^2 / 2.15^3 sigma = 0.10 (ell/m)^2 sigma, >= 2 sigma once ell/m >= 4.46
     (7.3 sigma at the window's lowest 8.54); E feeds 2 sigma through the rim for at most (ell/m)^2/(6 x 2.15^2) m/c
  F7 (cypher) the static and forming arrangements as cells over (phase, support at the rim, balance, nec_in, nec_out,
     nec_t, fits_198, through_hold), with NO per-cell key.  2 = not computed.  The README-cancelling static cell's fit
     with 198 is entered unknown, as rim_readme R9 does.  CORRECTED 2026-10-10 (pass 3): the static marginal cells now
     carry the tangential null energy as KEPT -- corridor_shape S0 found the bank's interpolation 8% wrong in g_rr near
     the throat, and with it corrected the marginal corridor meets the plane beyond r_b with the tangential kept (S3).
     So the target -- a rim that closes through the hold -- is DATA: with a ring (support 1) and with Z2 images and a
     ring (support 2), admitted by every language under every coding, statistics at orders 2-4.  With no support at
     the rim statistics over-reaches at orders 2-3 and refuses at order 4: balance needs a ring or images (F5).  The
     README-cancelling cell is not needed.  Control: the marginal cells given the first version's tangential -- order
     3 refuses, blocked by (nec_in | nec_out, nec_t, fits_198), which was this instrument's first finding and rested on
     that interpolation error.  Closing while the README flows (phase forming) stays refused at order 3 (its null
     energies are not computed)
Named readings (the board's): H-DEPTH-LAW-FOLLOWS-R4 (the corridor's radial null energy near the rim follows the
plane's 4D radial null Ricci along the same direction; R8's sign match, not derived) -- the null-README cell's nec_in = 0
rests on it.  H-CANCEL-IS-183-PAIR (rim_readme.py).
So: the force balance at the rim is not the obstacle -- it closes with Z2 images, a ring of positive tension, a kink or
a tension-carrying README -- and, since corridor_shape's correction, neither is the null energy: the static marginal
corridor keeps the radial and tangential null energy to a rim beyond r_b, and with a ring (or images and a ring) the rim
closes through the hold.  The geometry stays a force diagram until Wall C's global construction gives the rim a
spacetime; what the ring is, is OPEN.
Imports tools/cypher.py by path.  Stdlib + sympy.  python3 forming_rim.py [--selftest | --mutants]
"""
import contextlib
import importlib.util
import io
import itertools
import math
import os
import sys

import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(HERE))))
MUT = {}
S, TH, PI, PHI, LAM, A = sp.symbols("sigma theta Pi phi lambda a", real=True)
STEEP = sp.Interval.open(0, sp.pi / 2)                           # corridor_shape's graph frame needs theta < pi/2


def _load(path, key):
    spec = importlib.util.spec_from_file_location(key, path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[key] = mod
    with contextlib.redirect_stdout(io.StringIO()):
        spec.loader.exec_module(mod)
    return mod


def _v(a):
    return sp.Matrix([sp.cos(a), sp.sin(a)])


# ---------------------------------------------------------------------------------------------------------- F0
def parity():
    """every cyclic order of O, U, P (one-sided) and K (two-sided): is there a bulk/void labelling of the four regions
    with each one-sided sheet between bulk and void and K between bulk and bulk?  Then the same in the Z2 double cover
    (all planes two-sided)."""
    def realisable(sided):
        names = list(sided)
        for order in itertools.permutations(names[1:]):
            seq = [names[0]] + list(order)
            for lab in itertools.product((0, 1), repeat=4):          # region i lies between seq[i] and seq[i+1]
                ok = True
                for i, sh in enumerate(seq):
                    left, right = lab[i - 1], lab[i]
                    if sided[sh] == 1 and left == right:
                        ok = False
                    if sided[sh] == 2 and not (left == 1 and right == 1):
                        ok = False
                if ok:
                    return True
        return False
    one = {"O": 1, "U": 1, "P": 1, "K": 2}
    if MUT.get("even_planes"):
        one = {"O": 1, "U": 1, "P": 2, "K": 2}
    return {"single": realisable(one), "double": realisable({"O": 2, "U": 2, "P": 2, "K": 2})}


# ---------------------------------------------------------------------------------------------------------- F1, F2
def boost():
    v, al = sp.symbols("v alpha", real=True)
    g = 1 / sp.sqrt(1 - v**2)
    L = sp.Matrix([[g, g * v, 0], [g * v, g, 0], [0, 0, 1]])            # (t, x, y), boost along x
    t = sp.Matrix([0, sp.cos(al), sp.sin(al)])                          # the sheet's direction in the cross-section
    h = sp.diag(-1, 0, 0) + t * t.T                                     # its induced metric (t and its own direction)
    T = -S * h if not MUT.get("dust_sheet") else S * sp.diag(1, 0, 0)
    dT = sp.simplify(L * T * L.T - T)
    along = all(sp.simplify(x) == 0 for x in dT.subs(al, 0))
    tilted = any(sp.simplify(x) != 0 for x in dT.subs(al, sp.pi / 4))
    # aberration: a co-moving line at rest-frame angle a' is seen in the lab Lorentz-contracted along x
    ap = sp.Symbol("ap", positive=True)
    lab_tan = sp.tan(ap) * g                                            # dx shrinks by gamma: tan grows by gamma
    return {"along": along, "tilted": tilted, "aberr": sp.simplify(lab_tan / sp.tan(ap) - g) == 0}


def fluid_flux():
    rho, p, v = sp.symbols("rho p v", real=True)
    g2 = 1 / (1 - v**2)
    u = sp.Matrix([sp.sqrt(g2), sp.sqrt(g2) * v])
    eta = sp.diag(-1, 1)
    T = (rho + p) * u * u.T + p * eta.inv()
    Tnn = sp.simplify(T[1, 1])
    if MUT.get("drop_p"):
        Tnn = sp.simplify((rho + p) * g2 * v**2)
    target = sp.simplify((rho + p) * g2 * v**2 + p)
    ex = Tnn.subs({rho: 2 * S, p: -sp.Rational(3, 2) * S, v: 1 / sp.sqrt(2)})
    return {"Tnn": Tnn, "matches": sp.simplify(Tnn - target) == 0, "example": sp.simplify(ex)}


# ---------------------------------------------------------------------------------------------------------- F3
def geom(name, phi=None):
    if name == "A":
        return {"ours": _v(sp.pi), "p2": _v(sp.pi), "corr": _v(sp.pi - TH)}
    if name == "B":
        return {"ours": _v(sp.pi), "p2": _v(sp.pi - (2 * TH if phi is None else phi)), "corr": _v(sp.pi - TH)}
    if name == "C":
        return {"ours": _v(sp.pi + TH), "p2": _v(sp.pi - TH), "corr": _v(sp.pi)}
    raise KeyError(name)


TENS = {"ours": 1, "p2": 1, "corr": -1}


def residual(sh, images=False):
    o = _v(0)
    R = S * o + sum((TENS[k] * S * sh[k] for k in sh), sp.zeros(2, 1))
    if images:                                                       # mirror across our plane of the off-plane sheets
        for k in ("p2", "corr"):
            e = sh[k]
            if sp.simplify(e[1]) != 0:
                R += TENS[k] * S * sp.Matrix([e[0], -e[1]])
    return sp.simplify(R)


def g_law():
    o = _v(0)
    out = {}
    for gname in ("A", "B", "C"):
        sh = geom(gname)
        gk = {k: o + sh[k] for k in sh}
        R = residual(sh)
        out[gname] = sp.simplify(R - S * (gk["ours"] + gk["p2"] - gk["corr"])) == sp.zeros(2, 1)
    # B for any tilt phi of position 2's sheet: det[g_p2, g_corr]
    sh = geom("B", phi=PHI)
    gp, gc = o + sh["p2"], o + sh["corr"]
    det = sp.simplify(gp[0] * gc[1] - gp[1] * gc[0])
    target = 4 * sp.sin(TH / 2) * sp.sin(PHI / 2) * sp.sin((PHI - TH) / 2)
    out["B_det"] = sp.simplify(sp.expand_trig(det - target)) == 0 or sp.simplify(sp.expand_trig(det + target)) == 0
    return out


def solve_split(gname):
    """premises P1-P4: non-negative-or-any-sign forward split (w_ours, w_p2, w_corr); returns the forms"""
    sh = geom(gname)
    o = _v(0)
    sgn = 1 if not MUT.get("pi_plus") else -1
    R = residual(sh)
    g = {k: o + sh[k] for k in sh}
    x, y, z = sp.symbols("x y z", real=True)                        # x = T^nn w_ours, y = T^nn w_p2, z = T^nn w_corr
    F = R - sgn * (x * g["ours"] + y * g["p2"] + z * g["corr"])
    return {"F": sp.simplify(F), "x": x, "y": y, "z": z}


def f3():
    a = solve_split("A")
    sa = sp.solve(list(a["F"]), [a["z"]], dict=True)                 # A: ours, p2 along the plane give g = 0
    c = solve_split("C")
    sc = sp.solve(list(c["F"]), [c["x"], c["y"]], dict=True)         # C: g_corr = 0
    b = solve_split("B")
    sb = sp.solve(list(b["F"]), [b["y"], b["z"]], dict=True)         # B: g_ours = 0
    return {"A": sa, "C": sc, "B": sb, "Bsym": b}


# ---------------------------------------------------------------------------------------------------------- F3b
def f3b():
    o = _v(0)
    shB = geom("B")
    imgs = not MUT.get("images_off")
    RBi = residual(shB, images=imgs)
    Dc = o + (shB["corr"] + sp.Matrix([shB["corr"][0], -shB["corr"][1]])) / 2
    Pi_img = sp.factor(sp.simplify(sp.expand_trig(RBi[0] / Dc[0])))
    ring = 1 if not MUT.get("ring_out") else -1
    lam = {}
    for nm, R in (("C", residual(geom("C"))), ("Bimg", RBi), ("A", residual(geom("A"))), ("B", residual(shB))):
        sol = sp.solve(sp.simplify(R[0] - ring * 2 * LAM / A), LAM)
        lam[nm] = (sp.factor(sp.simplify(sp.expand_trig(sol[0]))) if sol else None, sp.simplify(R[1]))
    # kink family, numerically at theta = 0.3: corridor at kappa, ours/p2 at kappa -+ theta
    def kink(kap, t=0.3):
        eO = (1.0, 0.0)
        eK, eU, eP = [(math.cos(q), math.sin(q)) for q in (kap, kap + t, kap - t)]
        R = [eO[i] + eU[i] + eP[i] - eK[i] for i in range(2)]
        gU = [eO[i] + eU[i] for i in range(2)]
        gP = [eO[i] + eP[i] for i in range(2)]
        det = gU[0] * gP[1] - gU[1] * gP[0]
        x = (R[0] * gP[1] - R[1] * gP[0]) / det
        y = (gU[0] * R[1] - gU[1] * R[0]) / det
        return x >= 0 and y >= 0
    t = 0.3
    inside = all(kink(math.pi + f * t) for f in (-0.99, -0.5, 0.0, 0.5, 0.99))
    outside = not any(kink(math.pi + f * t) for f in (-1.2, 1.2))
    # reflection, B at theta = pi/3: pure reflection back along the outside sheet pushes -2 T^nn e_out
    Rb = residual(shB).subs(TH, sp.pi / 3)
    refl = sp.solve(list(sp.simplify(Rb - 2 * PI * o)), PI, dict=True)
    return {"Pi_img": Pi_img, "lam": lam, "kink_inside": inside, "kink_outside": outside, "refl": refl}


# ---------------------------------------------------------------------------------------------------------- F4
def null_energy():
    eta = sp.diag(-1, 1, 1)
    Phi, v, a = sp.symbols("Phi v alpha", positive=True)
    l = sp.Matrix([1, -1, 0])
    n = sp.Matrix([1, 1, 0])
    kt = sp.Matrix([1, 0, 1])
    lo = eta * l
    Tn = Phi * lo * lo.T
    own = l if not MUT.get("null_own") else n
    q = lambda T, k: sp.simplify((k.T * T * k)[0])
    g = 1 / sp.sqrt(1 - v**2)
    u = g * sp.Matrix([1, -v, 0])
    k = sp.Matrix([1, sp.cos(a), sp.sin(a)])
    uk = sp.simplify((u.T * eta * k)[0])
    c = sp.Symbol("c", real=True)                                    # cos alpha in [-1, 1]: 1 + v c is linear in c
    lin = sp.simplify(-uk * sp.sqrt(1 - v**2)).subs(sp.cos(a), c)
    lo_end = sp.simplify(lin.subs(c, -1))
    return {"own": q(Tn, own), "opp": q(Tn, n), "tan": q(Tn, kt), "lin_is_linear": sp.degree(lin, c) == 1,
            "lo_end": lo_end, "v": v}


# ---------------------------------------------------------------------------------------------------------- F5
def hold():
    out = {}
    for nm, R in (("A", residual(geom("A"))), ("B", residual(geom("B"))), ("C", residual(geom("C"))),
                  ("Bimg", residual(geom("B"), images=True))):
        if MUT.get("hold_flux") and nm == "C":
            R = R - 2 * S * (_v(0) + (geom("C")["ours"] + geom("C")["p2"]) / 2)
        Rn = [sp.simplify(sp.expand_trig(x.subs(S, 1))) for x in R]
        sols = [sp.solveset(x, TH, STEEP) if x != 0 else STEEP for x in Rn]
        out[nm] = sols[0].intersect(sols[1])
    return out


# ---------------------------------------------------------------------------------------------------------- F6
def estimate(lm=8.54, rr=2.15):
    c4G, m, ell = sp.symbols("c4G m ell", positive=True)               # c^4/G, the corridor's mass length, ell
    E = c4G * m
    sigma = 3 * c4G / (4 * sp.pi * ell**2)
    rpow = 3 if not MUT.get("est_r2") else 2
    ratio = sp.simplify(E / (sp.Rational(4, 3) * sp.pi * (rr * m) ** rpow) / sigma)
    tau = sp.simplify(E / (2 * sigma * 4 * sp.pi * (rr * m) ** 2))     # in units of 1/c
    r_at = float(ratio.subs(ell, lm * m)) if rpow == 3 else float(ratio.subs({ell: lm * m, m: 1}))
    t_at = float(sp.simplify(tau.subs(ell, lm * m) / m))
    need = math.sqrt(2 * rr**3)                                         # ell/m where the mean density reaches 2 sigma
    return {"ratio": r_at, "tau": t_at, "need": need}


# ---------------------------------------------------------------------------------------------------------- F7
U = 2
C7 = ["phase", "support", "balance", "nec_in", "nec_out", "nec_t", "fits_198", "through_hold"]
# phase 0 static (the hold), 1 forming; support at the rim 0 none, 1 ring, 2 Z2 images, 3 kink
CELLS = [(0, 0, 1, 0, 0, 1, 1, 1),   # static tangent, pure tensions (rim_readme R7-R9; R8 the radial deficit)
         (0, 0, 0, 1, 1, 1, 1, 1),   # static steep marginal corridor (corridor_shape S0-S3 corrected: tangential kept; R7 no balance)
         (0, 0, 1, 1, 1, 1, U, 1),   # static tangent, README cancelling (rim_readme R9; fit with 198 M's to say)
         (0, 1, 1, 1, 1, 1, 1, 1),   # static steep marginal + ring (F3b (ii), C); NEC: corridor_shape S0-S3 corrected
         (0, 2, 1, 1, 1, 1, 1, 1),   # static steep marginal, Z2 images + ring (F3b (ii)); NEC as corrected
         (1, 0, 0, U, U, U, 1, 0),   # forming steep, corridor_shape's frame, P1-P4 (F3 B)
         (1, 0, 1, 0, U, U, 1, 0),   # forming tangent, null README (F4; nec_in 0 on H-DEPTH-LAW-FOLLOWS-R4)
         (1, 0, 1, U, U, U, 1, 0),   # forming tangent, timelike README
         (1, 3, 1, U, U, U, U, 0),   # forming steep, kink (C), README onto the planes (fit with 198 (a)'s endpoint unknown)
         (1, 2, 1, U, U, U, 1, 0)]   # forming steep, Z2 images, README into the corridor (F3b (i))


def _codings(n):
    out = []
    for perm in itertools.permutations(range(n)):
        out.append(list(perm))
    return out


def cypher():
    cy = _load(os.path.join(ROOT, "tools", "cypher.py"), "fr_cypher")
    full = lambda h: all(h[i] == 1 for i in range(2, 8))
    forming = lambda h: h[0] == 1 and all(h[i] == 1 for i in range(2, 7))
    cells = list(CELLS)
    if MUT.get("old_tangential"):                               # the first version's (artefactual) tangential, S3
        cells = [c[:5] + (0,) + c[6:] if c[0] == 0 and c[1] in (0, 1, 2) and c[3] == 1 and c[2] in (0, 1) and c[5] == 1
                 and c[6] == 1 else c for c in cells]
    if MUT.get("drop_closing"):
        cells = [c for c in cells if not (c[0] == 0 and c[1] in (1, 2))]

    def index(cs, sup_order=(0, 1, 2, 3)):
        vo = {"phase": [0, 1], "support": [x for x in sup_order if x in {c[1] for c in cs}]}
        for j, name in enumerate(C7[2:], start=2):
            vo[name] = [x for x in (0, 1, U) if x in {c[j] for c in cs}]
        ix = cy.Index("forming_rim", C7, [list(c) for c in cs], value_order=vo)
        inv = [{v: k for k, v in ix.code[i].items()} for i in range(len(C7))]
        return ix, inv

    def admitted(cs, test, lang, opts=None, sup_order=(0, 1, 2, 3)):
        ix, inv = index(cs, sup_order)
        out, _ = cy.ADMISSION[lang][0](ix, opts or {})
        if out is None:
            return None
        dec = {tuple(inv[i][c[i]] for i in range(len(C7))) for c in out if all(c[i] in inv[i] for i in range(len(C7)))}
        return sorted(h for h in dec if test(h))

    st2 = admitted(cells, full, "statistics", {"statistics_order": 2})
    st3 = admitted(cells, full, "statistics", {"statistics_order": 3})
    tgt = (0, 0, 1, 1, 1, 1, 1, 1)
    seen3 = {Sx: {tuple(c[i] for i in Sx) for c in cells} for Sx in itertools.combinations(range(8), 3)}
    blocking = sorted(tuple(C7[i] for i in Sx) for Sx, v in seen3.items() if tuple(tgt[i] for i in Sx) not in v)
    ctrl = list(cells)
    ctrl[2] = (0, 0, 1, 1, 1, 1, 1, 1)
    ctrl3 = admitted(ctrl, full, "statistics", {"statistics_order": 3})
    form3 = admitted(cells, forming, "statistics", {"statistics_order": 3})
    fav = [c if c[0] == 0 else c[:2] + tuple(1 if x == U else x for x in c[2:]) for c in cells]
    fav_form3 = admitted(fav, forming, "statistics", {"statistics_order": 3})
    fav_full3 = admitted(fav, full, "statistics", {"statistics_order": 3})
    fav_full4 = admitted(fav, full, "statistics", {"statistics_order": 4})
    seen4 = {Sx: {tuple(c[i] for i in Sx) for c in fav} for Sx in itertools.combinations(range(8), 4)}
    fav_block4 = sorted(tuple(C7[i] for i in Sx) for Sx, v in seen4.items() if tuple(tgt[i] for i in Sx) not in v)
    st4 = admitted(cells, full, "statistics", {"statistics_order": 4})
    old = [c[:5] + (0,) + c[6:] if (c[0] == 0 and c[1] in (0, 1, 2) and c[2] in (0, 1) and c[3] == 1 and c[5] == 1
                                     and c[6] == 1) else c for c in CELLS]
    old3 = admitted(old, full, "statistics", {"statistics_order": 3})
    seen3o = {Sx: {tuple(c[i] for i in Sx) for c in old} for Sx in itertools.combinations(range(8), 3)}
    old_block = sorted(tuple(C7[i] for i in Sx) for Sx, v in seen3o.items() if tuple(tgt[i] for i in Sx) not in v)
    nocancel = [c for c in cells if c[6] != U or c[0] != 0]
    nocancel_ok = {l: all((0, 1, 1, 1, 1, 1, 1, 1) in (admitted(nocancel, full, l, None, tuple(o)) or []) for o in _codings(4))
                   for l in ("order", "algebra", "geometry", "information")}
    closing_all = {l: all({(0, 1, 1, 1, 1, 1, 1, 1), (0, 2, 1, 1, 1, 1, 1, 1)} <= set(admitted(cells, full, l, None, tuple(o)) or [])
                          for o in _codings(4)) for l in ("order", "algebra", "geometry", "information")}
    others = {}
    for lang in ("order", "algebra", "geometry", "information"):
        others[lang] = sorted({tuple(admitted(cells, full, lang, None, tuple(o)) or []) for o in _codings(4)})
    return {"st2": st2, "st3": st3, "blocking": blocking, "ctrl3": ctrl3, "form3": form3, "fav_form3": fav_form3,
            "fav_full3": fav_full3, "fav_full4": fav_full4, "fav_block4": fav_block4, "others": others, "st4": st4,
            "old3": old3, "old_block": old_block, "nocancel_ok": nocancel_ok, "closing_all": closing_all}


# ---------------------------------------------------------------------------------------------------------- run
def compute():
    return {"parity": parity(), "boost": boost(), "fluid": fluid_flux(), "glaw": g_law(), "f3": f3(), "f3b": f3b(),
            "nec": null_energy(), "hold": hold(), "est": estimate(), "cy": cypher()}


def checks(d):
    res = []
    add = lambda n, ok: res.append((n, bool(ok)))
    p = d["parity"]
    add("F0 R7's count with three one-sided planes and a two-sided corridor is not realisable as a line junction; in "
        "the Z2 double cover it is", not p["single"] and p["double"])
    b = d["boost"]
    add("F1 a pure-tension sheet is boost-invariant along itself, not when tilted to the boost; a co-moving sheet's "
        "angle aberrates by gamma", b["along"] and b["tilted"] and b["aberr"])
    fl = d["fluid"]
    add("F2 the flow's momentum flux along the sheet is (rho + p) gamma^2 v^2 + p; the NEC-obeying example rho = 2 sigma, "
        "p = -1.5 sigma, v^2 = 1/2 has T^nn = -sigma", fl["matches"] and sp.simplify(fl["example"] + S) == 0)
    g = d["glaw"]
    add("F3 the residual is sigma (g_ours + g_p2 - g_corr) in A, B, C; B's det[g_p2, g_corr] = +-4 sin(theta/2) "
        "sin(phi/2) sin((phi - theta)/2) for any tilt phi", g["A"] and g["B"] and g["C"] and g["B_det"])
    f = d["f3"]
    zA = f["A"][0][f["Bsym"]["z"]] if f["A"] else None
    add("F3 A: the corridor's share needs T^nn = -sigma (excluded by T^nn >= 0, allowed by the NEC)",
        zA is not None and sp.simplify(zA + S) == 0)
    sC = f["C"][0] if f["C"] else {}
    add("F3 C: the flux onto each plane sheet is exactly sigma (2 sigma onto the two), the corridor's share free",
        sC and sp.simplify(sC[f["Bsym"]["x"]] - S) == 0 and sp.simplify(sC[f["Bsym"]["y"]] - S) == 0)
    sB = f["B"][0] if len(f["B"]) == 1 else {}
    add("F3 B (corridor_shape's frame): the split solves uniquely as position 2's share +sigma and the corridor's "
        "-sigma at every theta -- opposite signs, so no forward split of one flow balances, of either sign",
        sB and sp.simplify(sB[f["Bsym"]["y"]] - S) == 0 and sp.simplify(sB[f["Bsym"]["z"]] + S) == 0)
    x = d["f3b"]
    lam = x["lam"]
    add("F3b (i) Z2 images, B: README into the corridor and its image balances with T^nn = 2 sigma (1 + 2 cos theta)",
        sp.simplify(x["Pi_img"] - 2 * S * (1 + 2 * sp.cos(TH))) == 0)
    add("F3b (ii) a ring: C with lambda = a sigma (1 - cos theta), B with images with a sigma (1 - cos theta)(1 + 2 cos "
        "theta), both > 0 on (0, pi/2); A and B without images keep a normal residual",
        sp.simplify(lam["C"][0] - A * S * (1 - sp.cos(TH))) == 0 and lam["C"][1] == 0
        and sp.simplify(sp.expand_trig(lam["Bimg"][0] - A * S * (1 - sp.cos(TH)) * (1 + 2 * sp.cos(TH)))) == 0
        and lam["Bimg"][1] == 0 and lam["A"][1] != 0 and lam["B"][1] != 0)
    add("F3b (iv) kink: a non-negative split balances for every kappa strictly between pi - theta and pi + theta, not "
        "outside", x["kink_inside"] and x["kink_outside"])
    add("F3b (v) reflection: B at theta = pi/3 balances with pure reflection, T^nn = sigma/2",
        len(x["refl"]) == 1 and sp.simplify(x["refl"][0][PI] - S / 2) == 0)
    nec = d["nec"]
    Phi = sp.Symbol("Phi", positive=True)
    add("F4 null dust: T(l,l) = 0 along its own rays, 4 Phi and Phi along the opposite radial and tangential rays; "
        "timelike: u.k is linear in cos alpha and its least magnitude factor is 1 - v > 0",
        nec["own"] == 0 and sp.simplify(nec["opp"] - 4 * Phi) == 0 and sp.simplify(nec["tan"] - Phi) == 0
        and nec["lin_is_linear"] and sp.simplify(nec["lo_end"] - (1 - nec["v"])) == 0)
    h = d["hold"]
    add("F5 the hold (T^nn = 0), no ring: none of A, B, C, B-with-images balances at any theta in (0, pi/2)",
        all(h[k] == sp.EmptySet for k in ("A", "B", "C", "Bimg")))
    e = d["est"]
    add("F6 ESTIMATE: mean density (ell/m)^2/2.15^3 sigma, 7.3 sigma at ell/m = 8.54, >= 2 sigma from ell/m = 4.46; "
        "the feed time (ell/m)^2/(6 x 2.15^2) m/c, 2.6 m/c at 8.54", 7.2 < e["ratio"] < 7.5 and e["ratio"] >= 2
        and abs(e["need"] - 4.459) < 1e-2 and 2.55 < e["tau"] < 2.7)
    cy = d["cy"]
    add("F7 the closing rim through the hold is data: a ring (support 1) and Z2 images with a ring (support 2) -- "
        "admitted by order, algebra, geometry, information under every coding of the support axis, and by statistics at "
        "orders 2, 3 and 4", all(cy["closing_all"].values())
        and all({(0, 1, 1, 1, 1, 1, 1, 1), (0, 2, 1, 1, 1, 1, 1, 1)} <= set(x or []) for x in (cy["st2"], cy["st3"], cy["st4"])))
    add("F7 with no support at the rim it is not: statistics admits it at orders 2-3 (over-reach) and refuses it at "
        "order 4 -- balance needs a ring or images (F5)", (0, 0, 1, 1, 1, 1, 1, 1) in (cy["st3"] or [])
        and (0, 0, 1, 1, 1, 1, 1, 1) not in (cy["st4"] or []))
    add("F7 control: the static marginal cells given the first version's tangential (negative, corridor_shape S3 before "
        "S0): order 3 refuses, blocked by (nec_in, nec_t, fits_198) and (nec_out, nec_t, fits_198) -- the block of this "
        "instrument's first run, which rested on that interpolation error", cy["old3"] == []
        and cy["old_block"] == [("nec_in", "nec_t", "fits_198"), ("nec_out", "nec_t", "fits_198")])
    add("F7 the README-cancelling cell is not needed: removed, the ring's closing rim is still admitted by every language "
        "under every coding", all(cy["nocancel_ok"].values()))
    add("F7 closing while the README flows: refused at order 3; admitted with the uncomputed null energies favourable",
        cy["form3"] == [] and len(cy["fav_form3"] or []) > 0)
    return res


MUTANTS = {"even_planes": "position 2's plane taken two-sided (parity hidden)",
           "dust_sheet": "the sheet given dust's stress (not boost-invariant)",
           "drop_p": "the flow's own pressure dropped from T^nn",
           "pi_plus": "the flux's push sign flipped (acting as tension)",
           "images_off": "the Z2 images left out of B's balance",
           "ring_out": "the ring made to push outward",
           "null_own": "null dust tested along the opposite rays as its own",
           "hold_flux": "the README left flowing at the rim through the hold",
           "est_r2": "the estimate's volume taken as r^2",
           "old_tangential": "the static marginal cells given the first version's tangential",
           "drop_closing": "the ring's and the images' closing cells left out"}


def selftest():
    r = checks(compute())
    for n, ok in r:
        print("  [%s] %s" % ("ok" if ok else "FAIL", n))
    k = sum(ok for _, ok in r)
    print("selftest: %d/%d" % (k, len(r)))
    return k == len(r)


def mutants():
    caught = 0
    for k, desc in MUTANTS.items():
        MUT.clear()
        MUT[k] = True
        try:
            failed = [n.split()[0] for n, ok in checks(compute()) if not ok]
        except Exception as ex:
            failed = ["raised %s" % type(ex).__name__]
        MUT.clear()
        caught += bool(failed)
        print("  mutant %-13s %-50s %s" % (k, desc, "caught by " + ", ".join(sorted(set(failed))) if failed else "NOT CAUGHT"))
    print("mutants: %d/%d caught" % (caught, len(MUTANTS)))
    return caught == len(MUTANTS)


def report(d):
    print("forming_rim.py -- the rim while the corridor forms (198 (a))\n")
    print("F0 parity:", d["parity"])
    print("F1", d["boost"], " F2", d["fluid"]["Tnn"], d["fluid"]["example"])
    print("F3 A:", d["f3"]["A"], " C:", d["f3"]["C"], " B:", d["f3"]["B"])
    print("F3b", {k: v for k, v in d["f3b"].items()})
    print("F4", {k: v for k, v in d["nec"].items() if k != "v"})
    print("F5 hold:", d["hold"])
    print("F6", d["est"])
    c = d["cy"]
    print("F7 statistics order 2 / 3 on the closing rim:", c["st2"], c["st3"], " blocking triples:", c["blocking"])
    print("F7 control (cancelling cell fits 198):", c["ctrl3"], " forming:", c["form3"], " favourable:", c["fav_form3"],
          " favourable through the hold, order 3 / 4:", c["fav_full3"], c["fav_full4"], c["fav_block4"])
    print("F7 other languages on the closing rim, over the 24 codings of the support axis:", c["others"])


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    if "--mutants" in sys.argv:
        sys.exit(0 if mutants() else 1)
    report(compute())
