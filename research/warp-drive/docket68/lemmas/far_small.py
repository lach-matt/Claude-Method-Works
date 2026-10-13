#!/usr/bin/env python3
"""far_small.py -- items 347, 349: the FAR row at the family's small end, on the one-way object.  M: "Let's start FAR"
(347), after 343's "Yes, agreed" set FAR beside ARRIVAL's verification.  The row: "FAR a far boundary consistent with
(Z), (G), 139 (1), 166" -- the record's (far_cypher, far_bridge, b4c_far), posed before 226, 251, 275 and 320; at the
small end "the hole's far field is the Randall-Sundrum background's, not computed" (warptheorem.py).  Worked in the
conversation (computed with sympy and z3, exact where marked; deduced where marked; not verified by a separate
session; not seated); 2026-10-13.

  F0 (read) The words the row rests on, verbatim in the rulings file: 139 (1), "1 - yes" (position 2's plane the
     negative-tension one, a quarter of ours, ours positive); 166, M chose "Both planes at once"; 183, M chose "Yes:
     never violated as a pair"; 200 (1), "1 - Once: k_R = k_L/2"; 226, M chose "Its own values" (each position 2
     carries its own universe's values, 2a, 2b and 2c positive planes; the option's text added "FAR's stated
     obstruction goes but FAR must be recomputed"); 251, "Localized hole, README only"; 273, "Quantum bounce to pos 2
     (Recommended)"; 275, "Coincident everywhere"; 320, "A consequence of 275 with 276 - no bulk is ever empty. It will
     always contain something wether it is information or matter."; 336, "I think it is B"; 347, "Let's start FAR".
  F1 (deduced) The question at the small end.  B4c's demand, which FAR carries (far_cypher's T-FAR): a far surface
     that encloses the corridor and is strictly untrapped at every ell, in a bulk where (Z), (G), 139 (1) and 166 hold.
     Each term has moved since the record posed it: (G) at the small end is the README's localized hole, our plane
     through its equator (251; C1 verified, 254); 139 (1)'s negative quarter is the value of the position 2 that item
     described, each position 2 carrying its own (226); 166's two planes coincide everywhere (275), so "both planes at
     once" is one surface carrying both sheets, B5a's coincidence; an empty bulk is the board's limit, never M's
     configuration (320 (b)); and since 336 the face stands the hole's life and E crosses any far surface as radiation.
     The record's cells no longer bear: its column models put the throat on our plane under one positive warp
     (b4c_far H-FAR-MODEL (i)), which is not the small end's corridor, and their column fails (Z) (b4c_far X9); the slab
     exists nowhere (275 (a)); model C is withdrawn (232 (2)).  Its NOCOL cell -- Randall-Sundrum's background with no
     column, untrapped at every W >= U (b4c_far X11) -- now has something to enclose.  So FAR at the small end asks:
     on the coincident pair's two-sided bulk, with the README's hole at its centre, is there a far surface enclosing
     the hole, strictly untrapped at every ell, through the write, the arrival and the hole's life?
  F2 (computed, exact) The background at the coincidence.  One surface carries both sheets (275); Israel's jump fixes
     each side's stress (b5a_residue A1): our side Sigma^- = S1, position 2's Sigma^+ = S1 + 2 S2.  For a tension
     Sigma = -lambda h the junction gives K = (kappa^2 lambda/6) h, a side of AdS5 with 1/ell = kappa^2 lambda/6
     (computed), the warp decaying away from the surface when lambda > 0.  So our side has our ell; position 2's side
     has 1/ell+ = kappa+^2 (sigma + 2 sigma_2)/6, kappa+ its own coupling (b5a_residue A6).  At 139 (1)'s sigma_2 =
     -sigma/4, Sigma^+ = sigma/2: with one coupling ell+ = 2 ell, B6's k_R = k_L/2 (200 (1)) from the junction alone
     (computed).  At every one of the twelve destinations (bulk5_index: tension sigma x 2^s, G5 x 2^((g-s)/2)) sigma_2
     > 0, so Sigma^+ = sigma (1 + 2^(s+1)) > 0 and ell+/ell = 2^(-(g-s)/2)/(1 + 2^(s+1)) lies in [1/6, 1/3] (computed).
     Every position 2 the record holds gives a decaying position-2 side.
  F3 (computed, exact; one inequality machine-checked by z3) The far surface on the two-sided bulk.  On each side g =
     (ell/z)^2 (-dt^2 + du^2 + dw^2 + u^2 dOmega_2^2), z = ell + s w with s = +1 (decaying) or -1 (growing), and the
     surface T_E = {(u/U)^2 + (w/W)^2 = 1} x S^2, meeting the pair square-on.  With D = (u^2/U^4 + w^2/W^4)^(1/2) and
     P = 1/(U^2 W^2 D^2) + 2/U^2,
         theta+ = -theta- = (z P - 3 s w/W^2)/(ell D)          (a conformal identity, checked against b4c_far's
     general level-set theta+ at sample points on both sides; the lapse does not enter).  On a decaying side, with K =
     W^2/U^2 and x = (u/U)^2, Q = W^2 P = K/(1 + (K - 1) x) + 2 K, and (Q - 3)(1 + (K - 1) x) is linear in x with end
     values 3 (K - 1) and 2 K (K - 1): Q >= 3 on all of T_E exactly when K >= 1 (z3, with a vacuity guard).  Then
     theta+ >= P/D >= U/W^2 + 2/U at every point and EVERY ell -- the record's sqrt3 (b4c_far X3) was its column's,
     and without the column the line is W = U.  Sharp: for W < U the tip is trapped exactly when ell < (U^2 - W^2)/W.
     A round surface (W = U) has theta+ = 3/U at every point, on either kind of side, at every ell.  On a growing side
     theta+ > 0 wherever w < ell.  Each half of T_E meets the surface square-on: where it crosses the sheets the
     warp's slope jumps, which gives theta+ no singular term (only first derivatives of the metric enter), and the two
     one-sided values are each positive.  The sides are independent, so every position 2 of F2 is covered.
  F4 (computed, exact; the hole's field in the board's test form) The README's hole at the centre. Near the hole (rho <<
     ell) the bulk is Tangherlini (C1 verified, 254; Q2: the 1/r^2 pull for r_h << r << ell); the board's form
     H-HOLE-IN-WARP puts its isotropic spatial factor psi = 1 + mu/(4 rho^2) (rho^2 = u^2 + w^2, mu = r_h^2) under the
     warp -- a test extension, exact as rho/ell -> 0, not a solution. The spatial metric stays conformally flat, so
         theta+ = (z P - 3 s w/W^2 - 3 z mu/(2 rho^4 psi))/(ell psi D)
     (checked against b4c_far's theta+, the lapse again cancelling). On the round surface it is exactly
         (3/(U psi^2)) (1 - mu/(4 U^2) - s (w/ell) mu/(2 U^2)):
     strictly untrapped wherever mu/(4 U^2) + mu/(2 U ell) < 1 -- so, within the test form, at every ell > r_h for any U
     > r_h, the margin at least 1/4, and at every README size of the small end, since its cover U = 1.05 (1 + 2 T) r_h
     exceeds r_h (deduced). The surface covers the write as the record's did, U = 1.05 R_reach with R_reach = r_h (1 + 2
     T), T the write's floor (write_small S3): at the example README U = 140,660 r_h = 1.58e-15 m, U/ell = 1.13e-10,
     mu/U^2 = 5.05e-11 (computed). Position 2's side carries its own face's mu, within V6's readings r_h^2 to 4^(2/3)
     r_h^2 (arrival_small V6), mu/U^2 at most 1.27e-10. The minimum of theta+ U over T_E with the hole, at W/U = 1, 1.5
     and 3, both kinds of side and ell/r_h from 10 to 1.2e15, at the example and at N = 1e3 (U = 9.0 r_h), is positive
     (computed; at ell/r_h = 10 it is the test form's figure, outside rho << ell).
  F5 (computed, exact where marked; deduced where marked) Through the write, the arrival and the hole's life. (a) Exact
     in spherical symmetry: on either Vaidya form, ingoing (the arrival, arrival_small V1) or outgoing (the emission,
     336), g^ab dr dr = 1 - mu/r^2, so a round sphere is untrapped exactly while its Misner-Sharp mu stays below r^2;
     the README's E is the only energy (arrival_small V1, 136 G), so mu <= r_h^2 at every stage and every round sphere
     outside r_h stays untrapped (computed). (b) The gas on the plane before and during the write is weak field,
     (r_h/R)^2 = 2.2e-10 at the write's start (write_small S3), and so is the emission's part carried on the plane
     (267's brane dominance): neither is spherical, and each moves T_E's theta+ by order mu/U^2 (deduced). (c) Beyond
     the near zone (U >~ ell) the hole is the brane's four-dimensional mass m = G E/c^4 = (3 pi/8)(r_h/ell) r_h: at the
     far surface its field is of order m/U = (3 pi/8)(r_h/ell)(r_h/U) (computed identity; the brane's 1/r law beyond ell
     standard-not-READ) -- 6.7e-21 at the example's U, with G5 = G ell; the G5 readings move it by a factor of order
     one. (d) No bulk is ever empty (320): the bulk's content traps a round surface only when its own Misner-Sharp mu
     reaches R^2, a uniform density rho_b >= 3 c^4/(4 pi G5 R^2) = (sigma/ell)(ell/R)^2 -- at the example's U, 7.9e19
     times the bulk's own vacuum energy density |Lambda5| c^4/(8 pi G5) = sigma/ell (computed). (e) Our plane's own dark
     energy enters as H U/c = 9.5e-42 (computed); if position 2's side's own Lambda and its junction disagree, the pair
     is curved (B5a's offset), and its curvature enters as H U/c, at most U/ell = 1.13e-10 for any H up to c/ell
     (deduced). So T_E stays strictly untrapped through the write, the arrival and the life, every correction smaller
     than its margin by at least nine orders at the example.
  F6 (deduced; computed where marked) (Z), (G), 139 (1) and 166 in this far model.  (Z): each side is Einstein, R_ab =
     -(4/ell^2) g_ab (computed), so R(k, k) = 0 on every null ray; the hole is Ricci-flat (C1); a ray crossing the pair
     gathers the summed stress, (sigma + sigma_2 + rho1 + rho2) k_y^2 + (w1 + w2)|k|^2 (b5a_residue A2), whose tension
     part sigma (1 + t) is positive at 139 (1)'s t = -1/4 and at all twelve (computed), its matter part non-negative
     pointwise (320; pointwise.py); a ray that meets the corridor keeps (Z) on Z3bs's reading (318).  (G): the hole at
     the centre is the small end's corridor, our plane through its equator (251; B2t).  139 (1) under 226: every
     position 2 the record holds -- 139 (1)'s quarter and the twelve -- gives a decaying side, F2, and F3 holds on
     each.  166 under 275: the pair is both planes at once.
  F7 (computed) FAR's question through the calculator, in the form C4's stands in (291; c4_residue R9, R12): the
     classes t, the far surface W >= U or W < U, and m, the far model -- the coincident two-sided bulk with the hole,
     or the record's column model (b4c_far H-FAR-MODEL).  f1, "strictly untrapped at every ell": {(1, 1): {1}, (0, 1):
     {0}, (1, 0): {0, 1}, (0, 0): {0}} from F3 and b4c_far X2-X3.  f2, "(Z) kept": {(1, 1): {1}, (0, 1): {1}, (1, 0):
     {0}, (0, 0): {0}} from F6 and b4c_far X9.  Asked at (1, 1), the calculator decides neither: f1 is "both" at
     order 2 and refused at order 3 under all 96 codings, its index clean under 211's audit -- the clause is a
     conjunction of the two classes, and the asked cell's siblings in t and in m are the trapped W < U surfaces and
     the column model, while the interior axis K is idle for a far surface; f2 is 1 at order 2 and refused at order
     3, its index flagged under all 96 codings, m and f one-hot -- (Z) here is the model coordinate itself, so the 1 is
     forced and void as evidence.  Those counts are the statistics-rank protocol; with every language seeing every
     condition (348 (Q4)) f1 is "both" in 24, 1 in 36 and refused in 36 at order 2, refused in all 96 at order 3, and
     f2 is 1 in 60 and refused in 36 at order 2, refused in all 96 at order 3 -- neither protocol decides either
     clause.  The calculator classifies, it does not derive (far_cypher's own words): F3-F6's computations decide, as
     291's form intends.
  F8 (deduced) What carries and what the row rests on.  (a) Carries without the test form: F2 and F3 are exact on the
     two-sided AdS background; F5 (a) is exact in spherical symmetry; F5 (d) is the content's own criterion.  (b) The
     board's own: H-HOLE-IN-WARP (F4), exact as rho/ell -> 0, and the far-zone order of magnitude (F5 (c)); every
     correction they carry is below the margin by nine orders or more at the example.  (c) The row rests on M's 139
     (1), 166, 183, 200 (1), 226, 251, 273, 275, 320 and 336; on the verified C1 (the hole), C2 (its count), C5 (its
     life) and B5a (the coincidence, 339); on write_small S3, arrival_small V1 and V6, b4c_far's level-set theta+ and
     X2-X3, bulk5_index's destinations, pointwise and Z3bs's reading of 318; and on the board's H-HOLE-IN-WARP.

  F9 (item 349, the residue pass before finalization, 314; deduced, and computed where marked) What F0-F8 claim without
     establishing, or rest on without naming. (a) F0's words are checked inside the item each is cited to, not anywhere
     in the file (the ARRIVAL verifier's 348 (Q11) finding, applied here). (b) F5 (a)'s "the README's E is the only
     energy" is exact in 320 (b)'s limit, an empty bulk apart from the README; with the bulk's content F5 (d)'s
     criterion governs. The emission's quantum negative influx lies inside our face (273, 318) and only lowers mu, never
     raising it at T_E. (c) F4's figures are at G5 = G ell. mu/U^2 carries no G5, since U is counted in clocks of r_h
     and the floor carries only N and Z (write_small S3); U/ell moves as g^(1/3), to 1.29e-10 and 8.95e-11 (computed);
     m/U moves by a factor of order one (F5 (c)). (d) F4's test form holds in the near zone, U << ell, which is ell >>
     140,660 r_h (the example has ell = 1.25e15 r_h). For r_h < ell <~ 1.4e5 r_h the far surface lies beyond ell, and F5
     (c)'s order of magnitude replaces the test form: F4's "at every ell > r_h" is the test form's statement, not the
     hole's. F3 holds at every ell regardless. (e) F6's matter condition is pointwise's: classical, rho >= 0 relative to
     the offset inside its vacuum's basin, the quantum case read under 120 (339 (Q4)). (f) The cover U = 1.05 R_reach is
     the record's choice (b4c_far), the board's. FAR needs a surface outside r_h that encloses the write's region, and
     F3-F5 hold for any larger U in the near zone. (g) "Both planes at once" (166) read as the coincident pair is the
     board's reading of 166 under 275: the record's 166 had a slab between the planes, which 275 removed. (h) Where T_E
     crosses the pair, the sheets carry our plane's dark energy beside the tension, 3.6e-63 of sigma (computed), and our
     matter likewise far below it: the pair's junction moves by that fraction. (i) The rests-on, completed: F8 (c) with
     276 and 323 (b5a_residue A1's our side carrying S1), A2 and A6; 328 and B8 (each side Einstein, the Gauss-Bonnet
     coupling zero); 184; 232 (2); 210 (B4d rests on FAR); the verified C6 (264: the floor) and arrival_small V1 and V6
     (verified, 348); and the board's readings -- H-HOLE-IN-WARP, the record's cover, 166 under 275 as in (g), Z3bs's
     reading of 318, and 320 (b)'s limit. (j) What carries and what is the test form's own. F2, F3 and F6 are exact on
     the two-sided AdS background at every ell on either side; F5 (a) is exact in spherical symmetry; F5 (d) is the
     content's own criterion. F4's figures are the test form's, and F5 (b)-(c) are orders of magnitude. The row uses
     only their size, at least nine orders below the margin at the example. (k) Nothing in F0-F8 uses T_E in a
     censorship theorem: that use, with its pointwise NEC premise and global hyperbolicity, stays B4's and B4d's (the
     does-not list).
  F10 (item 351, M-ACCOUNT-BEFORE-VERIFY's gate, 330; deduced, and computed where marked) The verifications so far,
     carried where they bear on FAR (verify_ledger's FAR column; far_large L10 carries the large end's).  (a) 267 (Q6):
     the floor is the write's least time.  A longer write reaches further and the cover grows with it, U = 1.05 (1 + 2T)
     r_h at the write's own T: F3 holds at every U, F4-F5 at any larger U in the near zone, and F5 (c)'s order beyond
     it.  (b) 271 (Q3), 319 (Q1), 341 (Q3): position 2's face is a white-hole face with kappa = c^2/r_h, and position 2's
     own fields hugging it are blueshifted one e-fold per clock, bounded over the face's open period by c_junction J5 --
     at most e^33.6 = 3.9e14, e^34.53 = 9.9e14 under the G5 readings (computed; c8_level V10), J5 re-admitted at 319 and
     Barcelo's threshold read at the face (341 (Q3)).  The Misner-Sharp mu at T_E counts the energy inside T_E, which a
     blueshift at the face redistributes but does not raise, so F4's position-2 mu stands.  (c) 304 (outside): F4's "the
     1/r^2 pull" (254 (Q2)'s words) names the potential's fall-off, mu/(4 rho^2) in psi; the force goes as r_h^2/rho^3,
     which is what F4's term 3 z mu/(2 rho^4 psi) carries.  F5 (c)'s 1/r law beyond ell is READ, Garriga and Tanaka's
     (far_large L3; 254 (Q2)'s 1/r tail), not standard-not-READ.  (d) 310 (Q3) with 276 (a): position 2 reads its own
     mass (240).  F4 gives position 2's side its own face's mu within V6's readings, r_h^2 to 4^(2/3) r_h^2, which bounds
     either identification of that side -- our hole's far hemisphere (mu = r_h^2) or position 2's own face -- and each
     side's T_E is computed on that side alone (F3), so nothing in F3-F5 runs from position 2's side back onto ours.  (e)
     317 (Q8): warp order enters the hole's near field at first order in rho/ell (m1_small's item-269 note), not its
     square: at T_E that is U/ell = 1.13e-10 at the example, inside F4's margin of at least 1/4.  (f) 332 (Q8): 226's
     "Its own values" read to include each position 2's tension -- F2's destinations, bulk5_index's sigma x 2^s -- is
     the board's reading of M's words, as gb_alpha B0's was; the option M chose said FAR must be recomputed.  (g) 337
     (Q3), (Q4): each side Einstein (F6) holds on Lovelock's premises, at the two-derivative order (324, 328); classical
     GR is given up only inside 273's quantum region, inside our face, which T_E encloses.  (h) 337 (Q9), 348 (Q11): F0's
     273 and 275 are the options M chose, their texts the board's.  (i) 341 (Q4): U/ell's 1.29e-10 and 8.95e-11 hold
     under both conventions for sigma, r_h/ell moving as g^(1/3) in each (c8_level V10); mu/U^2 carries no G5, and m/U's
     factor of order one (F5 (c)) is the conventions'.  (j) 348 (Q2): arrival_small's one E holds for a lossless
     collapse.  A lossy one radiates part of E outward, which lowers mu inside T_E and crosses T_E outgoing and positive
     (F5 (a)'s outgoing form), so mu <= r_h^2 stands.  (k) 341 (Q2), 348 (Q5): the rests-on, completed: M-P2-OWN-G (330)
     with 226, F2's kappa+ being position 2's own coupling; 270 (a) (the one object's two faces, ours and position 2's
     white-hole face), 273 (a) (the bounce opening on position 2's exterior) and 336 (a) (position 2's energy its own),
     through F4's position-2 side and V6; and 320 (b)-(c) (the empty bulk and the vacuum readings, limits).

What this does not claim.
  - The exact localized hole on the two-sided bulk: known only numerically for one plane (Kudoh-Tanaka-Nakamura's
    construction, named in B3), and with different couplings on the two sides not computed; F4 is the board's test
    form, F4's position-2 mu a bound over V6's readings.
  - The use of T_E in a censorship theorem: CGS Theorem 3.1's premises include the null energy condition pointwise
    (b4c_far X6, READ there), which 273's quantum region gives up inside our face; global hyperbolicity (W2) -- B4's
    and B4d's, not FAR's.
  - The far zone (U >~ ell) beyond F5 (c)'s order of magnitude.
  - The README's source on the plane (SOURCEs, deferred, 344-346) beyond F5 (b)'s weak-field bound.
  - The large end: there the record's FAR stands (far_cypher, far_bridge, b4c_far), OPEN.  [Item 350: worked in
    far_large.py L0-L9 and seated as a reading; nothing here moved.]

Imports b4c_far.py, bulk5_index.py, write_small.py, c4_residue.py and index_audit.py by path.
Stdlib + sympy + z3.  python3 far_small.py [--selftest | --mutants]
"""
import contextlib
import importlib.util
import io
import itertools
import math
import os
import sys
from collections import Counter

import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
D68 = os.path.dirname(HERE)
RULINGS = os.path.join(D68, "M-RULINGS-2026-10-03.md")
MUT = {}
# [item 349 (a)] each phrase checked inside the item it is cited to
WORDS = ((139, 'M, verbatim: "1 - yes 2 - positive, and you have to prove it.'), (166, 'M chose: "Both planes at once"'),
         (183, 'M chose: "Yes: never violated as a pair"'), (200, '"1 - Once: k_R = k_L/2'),
         (226, 'M chose: "Its own values"'), (226, "FAR's stated obstruction goes but FAR must be recomputed"),
         (251, '"Localized hole, README only"'), (273, '"Quantum bounce to pos 2 (Recommended)"'),
         (275, 'verbatim: "Coincident everywhere"'),
         (320, '"A consequence of 275 with 276 - no bulk is ever empty. It will always contain something wether it is '
               'information or matter."'), (336, '"I think it is B"'), (347, '"Let\'s start FAR"'),
         (349, '"Continue with FAR"'))
C_LIGHT, G_N = 299792458.0, 6.67430e-11
COVER = 1.05
_MOD = {}


def _load(name, key):
    if key in _MOD:
        return _MOD[key]
    path = os.path.join(HERE, name)
    saved = list(sys.path)
    sys.path[:0] = [HERE, D68]
    try:
        spec = importlib.util.spec_from_file_location(key, path)
        mod = importlib.util.module_from_spec(spec)
        with contextlib.redirect_stdout(io.StringIO()):
            spec.loader.exec_module(mod)
    finally:
        sys.path[:] = saved
    _MOD[key] = mod
    return mod


def _item(n):
    """item n's text in the rulings file, spacing normalized"""
    import re
    txt = open(RULINGS, encoding="utf-8").read()
    m = re.search(r"^%d\. .*?(?=^\d{3}\. |\Z)" % n, txt, re.M | re.S)
    return " ".join(m.group(0).split()) if m else ""


def BF():
    return _load("b4c_far.py", "far_bf")


# ---------------------------------------------------------------------------------- F2 the background at the pair
def f2():
    lam, kap = sp.symbols("lambda kappa", positive=True)
    h = sp.diag(-1, 1, 1, 1)                                     # the surface's induced metric, at a point
    Sig = -lam * h
    trS = sum(Sig[i, i] * h[i, i] for i in range(4))             # h^ab Sig_ab with h = h^-1 here
    K = (kap ** 2 / 2) * (Sig - trS * h / 3)
    inv_ell = sp.simplify(K[1, 1] / h[1, 1])                      # K = (1/ell) h for a decaying side
    t = sp.Symbol("t", real=True)
    plus = (lambda tt: 1 + tt) if MUT.get("sigma_plus_summed") else (lambda tt: 1 + 2 * tt)   # the mutant: S1 + S2
    ratio_139 = 1 / plus(sp.Rational(-1, 4))                      # ell+/ell at one coupling
    B5 = _load("bulk5_index.py", "far_b5")
    dest = {}
    for n, d in B5.five_d().items():
        s_, g5 = d["e"]["sigma"], d["e"]["G5"]
        tt = sp.Integer(2) ** sp.Rational(s_)
        sp_ = plus(tt)
        dest[n] = dict(t=tt, sigma_plus=sp_, ell_ratio=sp.nsimplify(2 ** (-sp.Rational(g5)) / sp_),
                       summed=1 + tt)
    return dict(inv_ell=inv_ell, lam=lam, kap=kap, ratio_139=ratio_139, dest=dest, t=t)


# ---------------------------------------------------------------------------------- F3 the far surface
def _closed(s, mu=0):
    B = BF()
    u, w, U, W, ell = B.u, B.w, B.U, B.W, B.ell
    D = sp.sqrt(u ** 2 / U ** 4 + w ** 2 / W ** 4)
    P = 1 / (U ** 2 * W ** 2 * D ** 2) + 2 / U ** 2
    z = ell + s * w
    if mu == 0:
        return (z * P - 3 * s * w / W ** 2) / (ell * D)
    rho2 = u ** 2 + w ** 2
    psi = 1 + mu / (4 * rho2)
    sgn = -1 if MUT.get("hole_sign") else 1                       # the mutant: the hole's term with the wrong sign
    return (z * P - 3 * s * w / W ** 2 - sgn * 3 * z * mu / (2 * rho2 ** 2 * psi)) / (ell * psi * D)


def _record(s, mu=0, lapse_kind="warp"):
    B = BF()
    u, w, ell = B.u, B.w, B.ell
    Om = ell / (ell + s * w)
    if mu:
        rho2 = u ** 2 + w ** 2
        psi = 1 + mu / (4 * rho2)
        lapse = Om * (1 - mu / (4 * rho2)) / psi if lapse_kind == "tangherlini" else Om
        Om = Om * psi
    else:
        lapse = Om
    return B.theta_plus(B.ELLIPSE, (lapse, Om ** 2, Om ** 2, Om ** 2 * u ** 2))


SAMPLES = (("17/10", "23/10", "11", "3/10", "11/10"), ("1", "1", "3", "1/20", "2/5"), ("2", "5", "40", "1/5", "17/10"),
           ("13/10", "19/10", "15/2", "1/10", "1/5"))


def _agree(e1, e2, mu=None):
    B = BF()
    ok = True
    for row in SAMPLES:
        Uv, Wv, lv, mv, uv = (sp.Rational(x) for x in row)
        sub = {B.U: Uv, B.W: Wv, B.ell: lv, B.u: uv, B.w: Wv * sp.sqrt(1 - (uv / Uv) ** 2)}
        if mu is not None:
            sub[mu] = mv
        a1, a2 = sp.N(e1.subs(sub), 40), sp.N(e2.subs(sub), 40)
        ok &= abs(a1 - a2) < sp.Float("1e-30") * max(1, abs(a1))
    return ok


_F3 = {}


def f3():
    if "r" in _F3 and not MUT:
        return _F3["r"]
    import z3
    B = BF()
    agree = {s: _agree(_closed(s), _record(s)) for s in (1, -1)}
    K, x = sp.symbols("K x", positive=True)
    num = sp.expand((K / (1 + (K - 1) * x) + 2 * K - 3) * (1 + (K - 1) * x))
    num = sp.expand(sp.simplify(num))
    if MUT.get("column_back"):                                    # the mutant: the record's column term (b = 1)
        num = sp.expand(sp.cancel((K / (1 + (K - 1) * x) + 2 * K * x / (x + 1) - 3) * (1 + (K - 1) * x) * (x + 1)))
    linear = sp.degree(num, x) == 1
    ends = (sp.factor(num.subs(x, 0)), sp.factor(num.subs(x, 1)))
    Kz, xz = z3.Reals("K x")
    numz = eval(str(num).replace("^", "**"), {"K": Kz, "x": xz})
    s_ = z3.Solver()
    s_.add(Kz >= 1, xz >= 0, xz <= 1, numz < 0)
    proved = s_.check() == z3.unsat
    s2 = z3.Solver()
    s2.add(Kz > 0, Kz < 1, xz >= 0, xz <= 1, numz < 0)
    vacuity_guard = s2.check() == z3.sat                          # below the line the inequality does fail
    # the floor theta+ >= U/W^2 + 2/U, sampled on T_E at every ell scale (decaying side)
    th = sp.lambdify((B.u, B.w, B.U, B.W, B.ell), _closed(1), "math")
    floor_ok, tip = True, None
    for Kv in (1.0, 1.5, 3.0, 10.0):
        for lv in (1e-6, 1e-2, 1.0, 1e3, 1e9):
            for i in range(1, 40):
                tau = i / 40.0
                uv, wv = (1 - tau ** 2) / (1 + tau ** 2), math.sqrt(Kv) * 2 * tau / (1 + tau ** 2)
                val = th(uv, wv, 1.0, math.sqrt(Kv), lv)
                floor_ok &= val >= 1 / Kv + 2 - 1e-9
    U, W, ell = B.U, B.W, B.ell
    tip = sp.simplify(_closed(1).subs({B.u: 0, B.w: W}))
    tip_trap = sp.solve(sp.Eq(sp.numer(sp.together(tip)), 0), ell)
    round_ = [sp.simplify(_closed(s).subs(W, U).subs(B.w, sp.sqrt(U ** 2 - B.u ** 2))) for s in (1, -1)]
    grow = sp.simplify(_closed(-1) * ell * sp.sqrt(B.u ** 2 / U ** 4 + B.w ** 2 / W ** 4))
    r = dict(agree=agree, linear=linear, ends=ends, proved=proved, vacuity_guard=vacuity_guard, floor_ok=floor_ok,
             tip=tip, tip_trap=tip_trap, round=round_, grow=grow)
    if not MUT:
        _F3["r"] = r
    return r


# ---------------------------------------------------------------------------------- F4 the hole at the centre
def example():
    WS = _load("write_small.py", "far_ws")
    sec = WS.seconds()
    row = sec["rows"][sec["ell_max"]]
    T = WS.head_clocks()
    return dict(rh=row["rh"], ell=row["ell"], T=T, U=COVER * (1 + 2 * T), WS=WS)


def f4():
    B = BF()
    mu = sp.Symbol("mu", positive=True)
    agree = {(s, lk): _agree(_closed(s, mu), _record(s, mu, lk), mu) for s in (1, -1) for lk in ("warp", "tangherlini")}
    U, W, ell, u, w = B.U, B.W, B.ell, B.u, B.w
    psi = 1 + mu / (4 * U ** 2)
    rnd = {s: sp.simplify(_closed(s, mu).subs(W, U).subs(w, sp.sqrt(U ** 2 - u ** 2)) * U * psi ** 2 / 3)
           for s in (1, -1)}
    want = {s: 1 - mu / (4 * U ** 2) - s * sp.sqrt(U ** 2 - u ** 2) * mu / (2 * U ** 2 * ell) for s in (1, -1)}
    round_exact = all(sp.simplify(rnd[s] - want[s]) == 0 for s in (1, -1))
    ex = example()
    WS = ex["WS"]
    n_small = 1000
    T_small = float(WS._num(WS.s3()["t3"], n=n_small))
    U_small = COVER * (1 + 2 * T_small)
    mins = {}
    for label, Uv, mu_max in (("example", ex["U"], 4 ** (2 / 3)), ("N=1e3", U_small, 4 ** (2 / 3))):
        lo = math.inf
        for Kv in (1.0, 1.5, 3.0):
            for s in (1, -1):
                th = sp.lambdify((u, w, U, W, ell, mu), _closed(s, mu), "math")
                for lv in (10.0, 1e3, 1e6, 1.2467e15):
                    if s == -1 and math.sqrt(Kv) * Uv >= lv:
                        continue                                  # a growing side only below its ell
                    for mv in (1.0, mu_max):
                        for i in range(1, 60):
                            tau = i / 60.0
                            uv = Uv * (1 - tau ** 2) / (1 + tau ** 2)
                            wv = math.sqrt(Kv) * Uv * 2 * tau / (1 + tau ** 2)
                            lo = min(lo, th(uv, wv, Uv, math.sqrt(Kv) * Uv, lv, mv) * Uv)
        mins[label] = lo
    return dict(agree=agree, round_exact=round_exact, U=ex["U"], U_small=U_small, mu_U2=1 / ex["U"] ** 2,
                mu2_U2=4 ** (2 / 3) / ex["U"] ** 2, U_m=ex["U"] * ex["rh"], U_ell=ex["U"] * ex["rh"] / ex["ell"],
                mins=mins, ex=ex)


# ---------------------------------------------------------------------------------- F5 through the write and life
def f5():
    v, r, rr = sp.symbols("v r rr", positive=True)
    m = sp.Function("mu")(v)
    th, ph, ch = sp.symbols("theta phi chi")
    out = {}
    for kind, sgn in (("ingoing", 1), ("outgoing", -1)):
        f = 1 - (m / r if MUT.get("ms_4d") else m / r ** 2)       # the mutant: the four-dimensional falloff
        g = sp.zeros(5)
        g[0, 0], g[0, 1], g[1, 0] = -f, sgn, sgn
        g[2, 2], g[3, 3], g[4, 4] = r ** 2, r ** 2 * sp.sin(th) ** 2, r ** 2 * sp.sin(th) ** 2 * sp.sin(ph) ** 2
        gi = g.inv()
        out[kind] = sp.simplify(gi[1, 1])                          # g^ab d_a r d_b r
    ex = example()
    rh, ell, U = ex["rh"], ex["ell"], ex["U"]
    E = 1.28098e9
    m4 = G_N * E / C_LIGHT ** 4
    m_identity = (3 * math.pi / 8) * rh ** 2 / ell
    sigma = 3 * C_LIGHT ** 4 / (4 * math.pi * G_N * ell ** 2)     # G5 = G ell (the record's reading)
    content_ratio = (ell / (U * rh)) ** 2                         # (sigma/ell)(ell/R)^2 over sigma/ell
    rho_de = 5.3e-10                                              # J/m^3, our plane's dark energy, the record's order
    H = math.sqrt(8 * math.pi * G_N * rho_de / (3 * C_LIGHT ** 2))
    return dict(ms=out, m4=m4, m_identity=m_identity, mfar=m_identity / (U * rh), sigma=sigma,
                content_ratio=content_ratio, HU=H * U * rh / C_LIGHT, write_weak=2.2e-10)


# ---------------------------------------------------------------------------------- F6 (Z): each side Einstein
def f6():
    t_, u_, w_, th, ph = sp.symbols("t u w theta phi", real=True)
    ell = sp.Symbol("ell", positive=True)
    res = {}
    for s in (1, -1):
        z = ell + s * w_
        O2 = (ell / z) ** 2
        g = sp.diag(-O2, O2, O2, O2 * u_ ** 2, O2 * u_ ** 2 * sp.sin(th) ** 2)
        X = (t_, u_, w_, th, ph)
        gi = g.inv()
        Gam = [[[sum(gi[a, d] * (sp.diff(g[d, b], X[c]) + sp.diff(g[d, c], X[b]) - sp.diff(g[b, c], X[d]))
                     for d in range(5)) / 2 for c in range(5)] for b in range(5)] for a in range(5)]
        Ric = sp.zeros(5)
        for b in range(5):
            for c in range(5):
                Ric[b, c] = sp.simplify(sum(sp.diff(Gam[a][b][c], X[a]) - sp.diff(Gam[a][b][a], X[c])
                                            + sum(Gam[a][a][d] * Gam[d][b][c] - Gam[a][c][d] * Gam[d][b][a]
                                                  for d in range(5)) for a in range(5)))
        res[s] = all(sp.simplify(Ric[b, c] + 4 * g[b, c] / ell ** 2) == 0 for b in range(5) for c in range(5))
    return res


# ---------------------------------------------------------------------------------- F7 the calculator
def populations():
    F1 = {(1, 1): {1}, (0, 1): {0}, (1, 0): {0, 1}, (0, 0): {0}}
    F2 = {(1, 1): {1}, (0, 1): {1}, (1, 0): {0}, (0, 0): {0}}
    if MUT.get("calc_spread"):                                    # the mutant: the two-sided cell left undecided
        F1 = {**F1, (1, 1): {0, 1}}
    return dict(f1=F1, f2=F2)


_F7 = {}


def f7():
    key = bool(MUT.get("calc_spread"))
    if key in _F7:
        return _F7[key]
    CR = _load("c4_residue.py", "far_cr")
    IA = _load("index_audit.py", "far_ia")
    P = populations()
    res = {}
    for name in ("f1", "f2"):
        F = P[name]
        out = {k: sum((CR._ask_one(("f",), F, k, tf=tf, mf=mf, c4row=(1, 1))
                       for tf, mf in itertools.product((0, 1), repeat=2)), Counter()) for k in (2, 3)}
        out_all = {k: sum((CR._ask_one(("f",), F, k, views_kind="all", tf=tf, mf=mf, c4row=(1, 1))
                           for tf, mf in itertools.product((0, 1), repeat=2)), Counter()) for k in (2, 3)}
        flagged = 0
        for tf, mf in itertools.product((0, 1), repeat=2):
            Ff = {(t ^ tf, m ^ mf): v for (t, m), v in F.items()}
            for perm in itertools.permutations(range(4)):
                kn = CR._cells("f", dict(zip(CR.NAMES4, perm)), Ff, ("quantum", 1 ^ tf, 1 ^ mf), CR.A4, CR.CD4)
                au = IA.audit_index(["K", "t", "m", "f"], kn)
                flagged += bool(au["keys"] or au["onehot"])
        res[name] = dict(F=F, out=out, out_all=out_all, flagged=flagged)
    _F7[key] = res
    return res


def f9():
    """item 349: the residue pass's computed figures -- U/ell under the G5 readings, the sheets' dark energy beside
    sigma"""
    ex = example()
    u_ell = ex["U"] * ex["rh"] / ex["ell"]
    sigma = 3 * C_LIGHT ** 4 / (4 * math.pi * G_N * ex["ell"] ** 2)
    return dict(u_ell_g5=[u_ell * g ** (1 / 3) for g in (1.5, 0.5)], de_sigma=5.3e-10 / sigma, ell_rh=1 / (
        ex["rh"] / ex["ell"]))


def compute():
    return dict(f2=f2(), f3=f3(), f4=f4(), f5=f5(), f6=f6(), f7=f7(), f9=f9())


def report(o):
    print("far_small.py -- the FAR row at the small end, one-way (item 347)\n")
    a = o["f2"]
    print("F2 the junction: 1/ell = %s; ell+/ell at 139 (1)'s quarter, one coupling: %s; the twelve's ell+/ell: %s"
          % (a["inv_ell"], a["ratio_139"], sorted({str(d["ell_ratio"]) for d in a["dest"].values()})))
    b = o["f3"]
    print("F3 closed form = b4c_far's theta+ (decaying, growing): %s; (Q - 3)(...) linear in x: %s, ends %s; z3: "
          "K >= 1 => Q >= 3: %s (fails below: %s); floor U/W^2 + 2/U held: %s" % (
              b["agree"], b["linear"], b["ends"], b["proved"], b["vacuity_guard"], b["floor_ok"]))
    print("   tip theta+ = %s, trapped below ell = %s; round surface theta+ = %s" % (
        b["tip"], b["tip_trap"], b["round"]))
    c = o["f4"]
    print("F4 hole: closed form = b4c_far's theta+ (sides x lapses): %s; round exact: %s; U = %.0f r_h = %.3g m, "
          "U/ell = %.3g, mu/U^2 = %.3g (position 2's side %.3g); min theta+ U over T_E: %s" % (
              c["agree"], c["round_exact"], c["U"], c["U_m"], c["U_ell"], c["mu_U2"], c["mu2_U2"],
              {k: round(v, 4) for k, v in c["mins"].items()}))
    d = o["f5"]
    print("F5 g^rr (Misner-Sharp): %s; m = %.4g m (identity %.4g); far field m/U = %.3g; bulk content needs %.3g "
          "times sigma/ell; H U/c = %.2g" % (d["ms"], d["m4"], d["m_identity"], d["mfar"], d["content_ratio"],
                                            d["HU"]))
    print("F6 each side Einstein, R_ab = -(4/ell^2) g_ab: %s" % o["f6"])
    for name, r in o["f7"].items():
        print("F7 %s: population %s; order 2 %s, order 3 %s; with every language %s, %s; audit flagged %d of 96" % (
            name, r["F"], dict(r["out"][2]), dict(r["out"][3]), dict(r["out_all"][2]), dict(r["out_all"][3]),
            r["flagged"]))


def checks(o):
    res = []
    add = lambda n, ok: res.append((n, bool(ok)))
    words = [(n + 1 if MUT.get("word_wrong_item") and n == 275 else n, w) for n, w in WORDS]   # the mutant: misfiled
    add("F0 139 (1), 166, 183, 200 (1), 226, 251, 273, 275, 320, 336, 347 and 349 verbatim, each inside its own item "
        "(item 349 (a))", all(" ".join(w.split()) in _item(n) for n, w in words))
    a = o["f2"]
    ok = sp.simplify(a["inv_ell"] - a["kap"] ** 2 * a["lam"] / 6) == 0 and a["ratio_139"] == 2
    ok &= len(a["dest"]) == 12 and all(d["sigma_plus"] > 0 and d["summed"] > 0 for d in a["dest"].values())
    ok &= {str(d["ell_ratio"]) for d in a["dest"].values()} <= {"1/3", "1/6", "sqrt(2)/6", "2**(1/3)/6"} \
        and min(float(d["ell_ratio"]) for d in a["dest"].values()) >= 1 / 6 - 1e-12
    ok &= max(float(d["ell_ratio"]) for d in a["dest"].values()) <= 1 / 3 + 1e-12
    add("F2 the junction: 1/ell = kappa^2 lambda/6; at 139 (1)'s quarter position 2's side has ell+ = 2 ell (B6's "
        "k_R = k_L/2); every one of the twelve gives a decaying side, ell+/ell in [1/6, 1/3]", ok)
    b = o["f3"]
    K = sp.Symbol("K", positive=True)
    add("F3 the far surface on the two-sided bulk: the closed form is b4c_far's theta+ on both sides; Q >= 3 exactly "
        "when W >= U (linear in x, ends 3(K - 1) and 2K(K - 1), z3 with its guard); the floor U/W^2 + 2/U at every "
        "ell; the tip's sharp line; theta+ = 3/U on the round surface on either side",
        all(b["agree"].values()) and b["linear"] and sp.simplify(b["ends"][0] - 3 * (K - 1)) == 0
        and sp.simplify(b["ends"][1] - 2 * K * (K - 1)) == 0 and b["proved"] and b["vacuity_guard"]
        and b["floor_ok"] and len(b["tip_trap"]) == 1
        and sp.simplify(b["tip_trap"][0] - (BF().U ** 2 - BF().W ** 2) / BF().W) == 0
        and all(sp.simplify(x - 3 / BF().U) == 0 for x in b["round"]))
    c = o["f4"]
    add("F4 the hole at the centre: the closed form is b4c_far's theta+ on both sides under either lapse; the round "
        "surface exact; U = 140,660 r_h, U/ell = 1.13e-10, mu/U^2 = 5.05e-11 (1.27e-10 on position 2's side); "
        "theta+ positive over T_E at the example and at N = 1e3",
        all(c["agree"].values()) and c["round_exact"] and round(c["U"]) == 140660
        and "%.3g" % c["U_ell"] == "1.13e-10" and "%.3g" % c["mu_U2"] == "5.05e-11"
        and "%.3g" % c["mu2_U2"] == "1.27e-10" and all(v > 0.5 for v in c["mins"].values())
        and 8.5 < c["U_small"] < 9.5)
    d = o["f5"]
    rr = sp.Symbol("r", positive=True)
    mu_v = sp.Function("mu")(sp.Symbol("v", positive=True))
    add("F5 through the write, the arrival and the life: g^ab dr dr = 1 - mu/r^2 on both Vaidya forms; m = G E/c^4 "
        "= (3 pi/8)(r_h/ell) r_h; the far field m/U = 6.7e-21; the bulk's content traps only at 7.9e19 sigma/ell; "
        "H U/c = 9.5e-42",
        all(sp.simplify(x - (1 - mu_v / rr ** 2)) == 0 for x in d["ms"].values())
        and abs(d["m4"] / d["m_identity"] - 1) < 2e-3 and "%.2g" % d["mfar"] == "6.7e-21"
        and "%.2g" % d["content_ratio"] == "7.9e+19" and "%.2g" % d["HU"] == "9.5e-42")
    add("F6 (Z): each side of the pair is Einstein, R_ab = -(4/ell^2) g_ab, decaying and growing alike",
        all(o["f6"].values()))
    z = o["f7"]
    add("F7 the calculator decides neither clause: f1 (untrapped at every ell) \"both\" at order 2 and refused at "
        "order 3 under all 96 codings, its audit clean; f2 ((Z) kept) 1 at order 2, refused at order 3, its index "
        "flagged under all 96 (m and f one-hot: forced, void as evidence); with every language, f1 both 24, 1 in 36, "
        "refused 36 and f2 1 in 60, refused 36 at order 2, both refused at order 3",
        z["f1"]["out"][2] == Counter({("both",): 96}) and z["f1"]["out"][3] == Counter({("refused",): 96})
        and z["f1"]["flagged"] == 0 and z["f2"]["out"][2] == Counter({(1,): 96})
        and z["f2"]["out"][3] == Counter({("refused",): 96}) and z["f2"]["flagged"] == 96
        and z["f1"]["out_all"][2] == Counter({("both",): 24, (1,): 36, ("refused",): 36})
        and z["f2"]["out_all"][2] == Counter({(1,): 60, ("refused",): 36})
        and all(z[n]["out_all"][3] == Counter({("refused",): 96}) for n in ("f1", "f2")))
    q = o["f9"]
    add("F9 (item 349) the residue pass's figures: U/ell 1.29e-10 and 8.95e-11 under the G5 readings; the sheets' "
        "dark energy 3.6e-63 of sigma; ell = 1.25e15 r_h at the example, far above the near zone's 140,660 r_h",
        ["%.3g" % v for v in q["u_ell_g5"]] == ["1.29e-10", "8.95e-11"] and "%.2g" % q["de_sigma"] == "3.6e-63"
        and "%.3g" % q["ell_rh"] == "1.25e+15")
    # [item 351] the gate's rows, each named in F10 (the mutant: F10 left unwritten)
    doc = __doc__ if not MUT.get("gate_unwritten") else __doc__.split("  F10 (item 351")[0]
    f10 = " ".join(doc.split("  F10 (item 351")[1].split("What this does not claim")[0].split()) \
        if "  F10 (item 351" in doc else ""
    gate = ("267 (Q6)", "271 (Q3)", "319 (Q1)", "341 (Q3)", "304 (outside)", "310 (Q3)", "317 (Q8)", "332 (Q8)",
            "337 (Q3)", "337 (Q9)", "348 (Q11)", "341 (Q4)", "348 (Q2)", "341 (Q2)", "348 (Q5)")
    add("F10 (item 351) the gate: every row carried here named in F10; the blueshift bound e^33.6 = 3.9e14, and "
        "e^34.53 = 9.9e14 under the G5 readings", all(g in f10 for g in gate)
        and "%.2g" % math.exp(33.6) == "3.9e+14" and "%.2g" % math.exp(34.53) == "9.9e+14")
    return res


MUTANTS = {"sigma_plus_summed": "position 2's side carrying S1 + S2, not S1 + 2 S2 (F2)",
           "column_back": "the record's throat column put back into the far model (F3)",
           "hole_sign": "the hole's term in theta+ with the wrong sign (F4)",
           "ms_4d": "the Misner-Sharp falloff taken four-dimensional (F5)",
           "calc_spread": "the two-sided cell of f1 left undecided (F7)",
           "word_wrong_item": "275's words looked for in item 276 (F0; item 349 (a))",
           "gate_unwritten": "the verifications' rows that bear left uncarried (F10; item 351)"}


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
