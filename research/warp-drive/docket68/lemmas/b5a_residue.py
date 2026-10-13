#!/usr/bin/env python3
"""b5a_residue.py -- item 282 (c): theorem row B5a (positivity for the entangled pin at coincidence, 127) brought level
with C1, C4, C5 and C7 one-way.  b5a_oneway.py (items 281-284) re-posed B5a sheet by sheet before the C4 verifier's
report (item 310), whose (7) and whose note on one induced metric bear on it; this carries both, puts B5a's question
through the calculator (196, 286) and audits the row to completion (314).  b5a_oneway is kept as written with its
item-319 note.  Worked in the conversation (computed with sympy, exact where marked; READ where marked; deduced where
marked; not verified by a separate session; not seated); 2026-10-12.

[Item 339, the B5a verifier's report (CONFIRMED with qualifications, nothing refuted; every qualification seated here
and in b5a_oneway, each beside the text it corrects, which is kept as the record). (Q9): b5a_oneway carries no item-319
note -- its notes are headed "Item 282 (c), under 316". (Q5)'s open point is closed by A6, a new entry.]

  A0 (read) The words the row rests on, verbatim in the rulings file: 282's reading (c), that O1c and B5a are re-posed
     the same way; 139 (1)'s "+4/3 and -1/3 of the one-plane value"; M's 276, "The passage is one-way in all aspects";
     M's 275, "Coincident everywhere"; M's 117, "An NEC is never violated"; 284's "Where it lands"; M's 202, "any plane
     has its own structure"; 226, "its plane's tension and offset among them"; M's 320, "prove the pointwise condition"
     and "no bulk is ever empty"; and the C4 verifier's at 310 (not M's words): "the junction fixes position 2's side
     total S1 + 2 S2, not tau" and "one surface carries one induced metric".
  A1 (computed, exact) What the junction fixes.  At the coincidence there is one surface (275).  With each side's
     extrinsic curvature K^-+ = +-(kappa^2/2)(Sigma^-+ - Sigma^-+ h/3), Sigma^-+ the stress that side carries, Israel's
     jump [K] = -kappa^2 (S - S h/3), S = S1 + S2, holds if and only if Sigma^- + Sigma^+ = 2 (S1 + S2) -- computed for
     general symmetric surface stresses, the map X -> X - tr(X) h/3 being invertible in four dimensions (its trace is -tr
     X/3).  One way, our side carries ours alone, Sigma^- = S1 (the board's reading (a) of 276, M's words "one-way in all
     aspects"; b5a_oneway B1) [item 323: proved from 276 -- our side carries what it would without position 2, and with
     our bulk mirrored Israel gives S1 (p2_assume Q2)], and then Sigma^+ = S1 + 2 S2, fixed for any stress, matter
     included. tau is a convention for splitting it (310 (7); tau_share T2's note): j_readings J2's tau S1 + S2 at tau =
     3/4 and S1 + 2 S2 agree on tensions and part only in how position 2's matter is counted (computed: their difference
     is S1/4 + S2, zero for tensions alone).
     [Item 339 (the B5a verifier's (Q2)): "part only in how position 2's matter is counted" is false as worded. S1/4 +
     S2 carries rho1/4 + rho2, so our matter is counted differently too -- rho1 against 3 rho1/4, as position 2's 2 rho2
     against rho2; A2's own readings show it. Nothing turns on it.]
  A2 (computed, exact) Positivity on every ray, on every reading.  A bulk null ray k crossing a surface that carries a
     tension lambda and matter (rho, p) gathers S(k, k)/|k_y| -- j_readings J2's sin a form -- with S(k, k) = (lambda +
     rho) k_y^2 + (rho + p) |k_space|^2 (computed from S_ab = -lambda h_ab + (rho + p) u_a u_b + p h_ab with h(k, k) =
     -k_y^2 on the surface).  The readings, with 139 (1)'s tensions sigma = 4/3 lambda_RS for ours and -sigma/4 for
     position 2's:
       the summed stress S1 + S2 -- what Israel fixes on the one surface whatever the split, and the null energy a
         crossing ray gathers there -- (3 sigma/4 + rho1 + rho2) k_y^2 + (w1 + w2) |k_space|^2;
       our side S1 -- (sigma + rho1) k_y^2 + w1 |k_space|^2;
       position 2's side S1 + 2 S2 -- (sigma/2 + rho1 + 2 rho2) k_y^2 + (w1 + 2 w2) |k_space|^2;
       J2's split at tau = 3/4 -- (sigma/2 + 3 rho1/4 + rho2) k_y^2 + (3 w1/4 + w2) |k_space|^2;
     w = rho + p.  Each tension part is positive and each matter weight positive (computed), so each reading is positive
     on every ray when each universe's matter on the sheets has rho + p >= 0 and rho > -sigma/6, the weakest of the four
     bounds -3 sigma/8, -sigma, -sigma/6, -2 sigma/7 (computed; sigma/6 = 2.5e52 J/m^3 at the example, e_positive E7's
     sigma/4 = 3.7e52).  Both are proved, at every point and for every universe (pointwise.py, item 320): matter built
     of particles, scalar fields and gauge fields satisfies the weak and null conditions pointwise with every mass,
     coupling and potential left general, so ours does and, by 202's "the same definitions as we do, perhaps different
     values", every position 2's, the README's rebuilt matter included -- rho >= 0 above the vacuum and rho + p >= 0,
     the bound never approached.  [Item 320: the condition was named B5'a's and not M's at item 319's audit; M ordered
     it proved, and it is.]  [Item 321: the fields' kinetic signs are their definitions, which 202 gives position 2 as
     ours; the ghost the record defines, position 2's plane's displacement, is plane structure, not matter, held at zero
     by 127, 141 and 275 (pointwise P6, P10).]  Each plane's vacuum energy, its offset (201), enters every reading as a
     tension does (S = -delta sigma h): ours, 5.25e-10 J/m^3 > 0 (201), only adds; position 2's is its own (226) -- ours
     for 2a, 2b and 2c, positive planes -- and for 139 (1)'s plane unstated (theorem_p2 TC: "undecided for 139's plane,
     offset unstated").  With the offsets the side reading's tension part is sigma/2 + delta sigma_1 + 2 delta sigma_2,
     positive if and only if delta sigma_2 > -sigma/4 - delta sigma_1/2 = -3.7e52 J/m^3, the strictest of the four
     (computed; the summed reading needs delta sigma_2 > -3 sigma/4 - delta sigma_1).  So B5a holds for every position 2
     whose offset exceeds -sigma/4 - delta sigma_1/2: every positive plane (226), and 139 (1)'s plane when its own offset
     does, which no ruling gives -- the one question put to M.  [Item 322: M sent the board to the vacuum decay boundary
     and the Higgs mass; the offset is derived, x+ = d1/2 - 3 d1^2/(2 sigma) = 2.625e-10 J/m^3 from the one induced
     metric (p2_offset V5-V6), so B5a holds for 139 (1)'s plane too, to be overruled by M.]  [Items 323-328: the
     derivation's premises are proved (p2_assume Q0-Q7; relativity U1-U6) and the Gauss-Bonnet coupling is zero
     (gb_cone C7, at its verifier as claim C9), so x+ = 2.625e-10 J/m^3 is exact and B5a holds for 139 (1)'s plane
     with nothing left to M; the question put to M is answered.]  [Item 332: C9 verified, CONFIRMED with
     qualifications (gb_cone C10): alpha = 0 under M-ONE-LIGHT-CONE (328), so x+ stays exact.]  [Item 337 (Q4):
     exact on Lovelock's premises, local and second order -- the two-derivative law, as A3's item-337 note says.]
     Where the README lands its density exceeds sigma/4 (E7) and only adds.  B5a does not turn on tau or on which side
     carries what: 310 (7) is closed for it.  On position 2's side it holds on every ray of the plane, not only where
     the README lands (b5a_oneway B2), because the side total carries sigma/2 > 0 of tension (tau_share T4).
     [Item 339, the B5a verifier's (Q1), (Q3), (Q4), (Q6), (Q7). (Q1) "j_readings J2's sin a form" is a wrong citation:
     J2 computes chi = 0 and the late-time sign for every tau, and holds no ray share. The crossing share is m1p2x_sixth
     W1's and c4_oneway P4's (verified at 310); S(k, k)/|k_y| is the thin-shell integral of T_kk, and positivity needs
     only the sign of S(k, k). (Q3) -sigma/6 is the strictest of the four bounds, the binding one, not the weakest (the
     code's name "weakest" kept); each density above -sigma/6 on its own suffices. (Q4) "Both are proved ... rho >= 0
     above the vacuum" claims more than pointwise proves. The null condition, rho + p >= 0, is proved classically for
     every V. rho >= 0 is proved above the potential's least value (pointwise P2), so relative to the plane's offset,
     which is what A2 needs, it holds inside the offset vacuum's basin: our vacuum is metastable, with a deeper region
     at or below -2.0e108 J/m^3 beyond the barrier (p2_offset, item 322), 56 orders past -sigma/6 -- a change of vacuum,
     not matter, and outside this row. "Every potential" needs V bounded below. Quantum states are read under M's 120,
     pointwise P7's reading, a dependency named now. (Q6) Since item 336 (M-ENERGY-STAYS) the energy at position 2's
     face is position 2's own, the one value read from two sides: "the README's density" is stale wording, E7's number
     stands -- 2.0e-15 m, 1.93e-15 and 2.18e-15 m under the 2 : 1 bulk's G5 readings (c8_level V1) -- and A2's every-ray
     result does not use E7. (Q7) x+ is the root of the quadratic 4 x^2 + (4 d1 + 2 sigma) x - sigma d1 = 0; d1/2 - 3
     d1^2/(2 sigma) is its series truncation ("+ ...", as items 322 and 325 write), the difference 1.9e-69 J/m^3.
     "Exactly" in the item-332 and 323-328 notes is on Lovelock's premises, as the item-337 note says. Code-only, from
     the same report: a2 enters J2's offset as d1 + d2 where J2's split gives tau d1 + d2, the strictest bound either
     way unchanged.]
  A3 (computed, exact; READ where marked; deduced where marked) The one-way reading on one induced metric (310's note).
     On a homogeneous slice each side obeys its own Gauss equation with the one Hubble rate H: ours, our lone plane's,
     H^2 = (kappa^2 Sigma^-/6)^2 - k1^2 + C1/a^4, and position 2's, H^2 = (kappa^2 Sigma^+/6)^2 - k2^2 + C2/a^4, k1 =
     kappa^2 sigma/6 and k2 = kappa^2 sigma/12 (the flat static planes, tau_share T4).  Both hold if and only if C2 - C1
     = a^4 (kappa^2/6)^2 [sigma (rho1 - 2 rho2) - 4 rho2 (rho1 + rho2)] (computed).  A vacuum bulk with the cosmological
     symmetries has a constant mass parameter (Bowcock, Charmousis and Gregory, hep-th/0007177, READ, abstract: "The
     cosmology is indeed a boundary of a (class II) Schwarzschild-AdS spacetime"; their mu "an integration constant",
     eq. (17)).  With matter conserved, d(a^4 rho)/dt = a^4 H (rho - 3p) (computed), so both bulks vacuum would need
     (rho1 - 3p1) = 2 (rho2 - 3p2) at first order in rho/sigma -- dust counting rho, vacuum energy 4 rho, radiation 0.
     Otherwise the one-way coincidence on one induced metric needs position 2's bulk mass to change, and position 2's
     bulk is not vacuum -- which M's 320 rules of every bulk: "no bulk is ever empty".  By 276 nothing of position 2's
     enters our side's equation, and position 2's bulk is its own (202: "any plane has its own structure ... perhaps
     different values"), so position 2's side carries it (deduced).  A field of position 2's own suffices: for a
     canonical scalar, T_ab = d_a phi d_b phi - g_ab ((1/2)(d phi)^2 + V), on position 2's sheet in its rest frame the
     Codazzi flux is T_un = phidot d_n phi and the Gauss normal stress T_nn = (1/2)(d_n phi)^2 + (1/2) phidot^2 - V
     (computed), which take any values, the flux through d_n phi and the stress through V, position 2's own (202)
     (deduced); its null energy is T_kk = (k . d phi)^2 >= 0 for every null k and every V (computed), within 117 and
     120; and with them position 2's bulk exists near the sheet: Anderson, Dahia, Lidsey and Romero (gr-qc/0111094,
     Theorem 1, READ) give "a local isometric and analytic embedding ... in an (n+1)-dimensional space sourced by any
     arbitrary scalar field" exactly when the surface's metric, its extrinsic curvature and the field's data on it
     satisfy the Codazzi and Gauss constraints, their (15) and (16) -- here the induced metric ours fixes, K^+ from
     Sigma^+, and the flux and stress just chosen (deduced, for analytic data).  So the one-way reading exists on one
     induced metric, and A2's per-side readings are readings of it (deduced).  For a null-dust carrier instead, in
     either direction, Vaidya-AdS5 with kappa^2 T = +-3 C'/(2 r^3) on the dust's null direction (computed), the brane's
     Codazzi identity on position 2's side is d Sigma/d tau + 3 H (Sigma + Pi) = -(3/(kappa^2 a^3)) w dC2/d tau, w the
     brane's dv/d tau or du/d tau (computed, exact), and with the two Gauss equations H cancels: 117/120 in position 2's
     bulk hold if and only if Q <= 0, Q = 4 (Sigma^-^2 - Sigma^+^2 - 3 sigma^2/4) + 6 Sigma^+ (Sigma^+ + Pi^+) - 6
     Sigma^- (Sigma^- + Pi^-), at first order sigma [(rho1 - 3p1) - 2 (rho2 - 3p2)] (computed): with null dust alone,
     our bulk's content held static, position 2's sheet must carry at least half our rho - 3p -- computed with our
     side's bulk empty, the board's limit and never M's configuration (320, as 184 made matter-free results limits),
     recorded as a computation about that carrier.  The board's earlier report of position 2's bulk as non-empty only
     "unless our sheet's rho - 3p is twice position 2's" was that limit's reading; M's 320 is the case.
     [Items 324-328: the two Gauss equations and Israel's jump are the bulk's law exactly, not its two-derivative
     order -- relativity U1-U6, and the Gauss-Bonnet coupling zero (gb_cone C7, claim C9 at its verifier).  And A3's
     field of position 2's own is a canonical scalar, minimally coupled, so it keeps the one light cone 328 confirms
     (sgb_cone S2: with no curvature coupling every front is null); a scalar coupled to the Gauss-Bonnet density would
     not (sgb_cone S4) and is not what A3 uses (deduced).]
     [Item 337 (the O1c verifier's (Q4), accounted before the next verification, 330): "exactly" holds on Lovelock's
     premises -- local, second order -- the law exact at the two-derivative order (324; relativity.py "What this does
     not prove"); "not its two-derivative order" overstated it. Nothing here turns on the difference.]
     [Item 332: C9 verified (gb_cone C10, sgb_cone S9): the law is the bulk's exactly under 328 (Q1); sgb's potential
     condition (Q5) concerns the coupled scalar, which A3 does not use.]
  A4 (computed) B5a's question through the calculator, in the form C4's (f) stands in (c4_residue R9, R12): the clause
     "positive on every ray, on every reading" realized per class from its law by witnesses -- tension: 139 (1)'s
     -1/4, any other value of position 2's (-1/8, -10, -1/100, +1/2); matter: the README above sigma/4 (1/2, 20), other
     below or none (0, 1/10, 1/5) -- giving {(1, 1): {1}, (1, 0): {1}, (0, 1): {0, 1}, (0, 0): {0, 1}} (computed),
     replicated over the four interiors (B5a is outside the hole and does not turn on the continuation), the question
     cell the quantum bounce's at M's tension and the README.  Result: 1 at orders 2 and 3 under all 96 codings; 211's
     audit flags no key and no one-hot.  As for C4's (f), the answer is the population's read-back at M's class: it adds
     nothing to A2.
     [Item 339 (the B5a verifier's (Q8)): "read-back at M's class" is imprecise. The 1 is statistics' read-back of the t
     = 1 row: order, algebra, geometry and information leave both answers open, and flipping M's class alone to {0}
     gives "both" at order 2 and refused at order 3. With every language seeing every condition the answer is 1 in 60 of
     96 codings and refused in 36 (recomputed in the conversation at item 339), as 310 (4) found for C4. "Adds nothing
     to A2" stands; the verifier's own audit is clean on all 96 codings (A4 audits one, 337 (outside)).]
  A5 (deduced) The row, one way: at the coincidence, on every reading of the junction -- the summed stress Israel fixes,
     our side's S1 and position 2's S1 + 2 S2, J2's split -- the null stress on every ray crossing the sheets is
     positive, each universe's matter satisfying the weak and null conditions at every point (pointwise.py, proved), for
     every position 2 whose offset exceeds -sigma/4 - delta sigma_1/2 (A2).  The one-way element is our side's share,
     ours alone (the board's reading (a) of 276); what the junction fixes on position 2's side follows (A1), and the
     reading exists on one induced metric (A3).  It rests on 139 (1)'s tensions (M's), on 275 and on 276.
     [Item 339 (the B5a verifier's (Q5), residue under 314): "It rests on 139 (1)'s tensions, on 275 and on 276" omits
     what A1-A3 use. It rests also on p2_assume Q2 for Sigma^- = S1 (the mirrored one-plane configuration, B6',
     323-324); on 202 and 226 for every position 2 ("offset among its own values" the board's gloss of M's "Its own
     values", 332 (Q8)); on 201 for our offset; on 320 through pointwise, and on 120 through pointwise P7; on 322-328
     and 332 for 139 (1)'s offset (p2_offset V5-V6, p2_assume, relativity, gb_cone C7 under M-ONE-LIGHT-CONE); and,
     unstated until now, on one five-dimensional coupling on both sides of the coincident surface -- which A6 removes.]
  A6 (item 339 (Q5); computed, exact; the junction for two couplings deduced from an action with each side's own
  Einstein-Hilbert and boundary terms, standard-not-READ) Each position 2's own G sits in its own G5 (226; bulk5_index:
  2b's G5 is 2^(1/2) of ours, 2P's 2^(3/2), 2b + 2P's 4). With each side's own coupling Israel's condition is the jump
  of (K_ab - K h_ab)/kappa^2, which is K^+/kappa_+^2 - K^-/kappa_-^2 = -(S - S h/3) on a four-dimensional surface; with
  each side's K^-+ = +-(kappa_-+^2/2)(Sigma^-+ - Sigma^-+ h/3), it gives Sigma^- + Sigma^+ = 2 (S1 + S2) for every pair
  of couplings (computed for general symmetric stresses). So A1's side total S1 + 2 S2, and A2's four readings with it,
  hold whatever position 2's G5: the verifier's "the sign still survives" made exact, and one five-dimensional kappa is
  not needed. Written as a jump in K alone with one coupling (the mutant), the side total moves with
  kappa_+^2/kappa_-^2.

What this row does not claim -- each left out with its reason, none open in it (314).
  - The bulk away from the sheets: A3 shows the one-way reading exists near them, with a field of position 2's own
    (gr-qc/0111094's embedding is local); position 2's bulk beyond is its own (202), its global form not B5a's.
  - B5c's pin (no radion at the coincidence): its own row.
  - Position 2's matter's laws: A2 proves the condition its matter meets (pointwise.py), not which matter it holds.
  - The corridor: there the causal structure separates the sheets (j_readings J1; tau_share's "does not show").
  - [Item 339 (Q4)] A vacuum beyond our offset's basin: a region past the barrier (p2_offset, at or below -2.0e108
    J/m^3) is a change of vacuum, not matter, and not this row's.

Imports c4_residue.py (its population machinery, which loads c4_oneway.py, calculator.py and hlaw.py), index_audit.py,
p2_gravity.py and pointwise.py by path.  Stdlib + sympy.  python3 b5a_residue.py [--selftest | --mutants]
"""
import contextlib
import importlib.util
import io
import itertools
import os
import sys
from collections import Counter

import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
D68 = os.path.dirname(HERE)
RULINGS = os.path.join(D68, "M-RULINGS-2026-10-03.md")
MUT = {}
WORDS = ("theorem rows O1c and B5a, marked at 281, are re-posed the same way", "The passage is one-way in all aspects",
         "Coincident everywhere", "An NEC is never violated", "Where it lands",
         "the junction fixes position 2's side total S1 + 2 S2, not tau", "one surface carries one induced metric",
         "any plane has its own structure", "+4/3 and -1/3 of the one-plane value", "prove the pointwise condition",
         "no bulk is ever empty", "its plane's tension and offset among them")
_MOD = {}


def _load(name, key):
    if key in _MOD:
        return _MOD[key]
    path = os.path.join(HERE, name)
    spec = importlib.util.spec_from_file_location(key, path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[key] = mod
    saved = list(sys.path)
    sys.path[:0] = [HERE]
    try:
        with contextlib.redirect_stdout(io.StringIO()):
            spec.loader.exec_module(mod)
    finally:
        sys.path[:] = saved
    _MOD[key] = mod
    return mod


def a1():
    """the side total: Sigma^- + Sigma^+ = 2 (S1 + S2) for general symmetric stresses; one way, Sigma^+ = S1 + 2 S2"""
    h = sp.diag(-1, 1, 1, 1)
    hi = h.inv()

    def sym(name):
        s = sp.symbols(name + "_0:10")
        it = iter(s)
        M = sp.zeros(4)
        for i in range(4):
            for j in range(i, 4):
                M[i, j] = M[j, i] = next(it)
        return M, list(s)
    S1, _ = sym("s1")
    S2, _ = sym("s2")
    Sp, up = sym("sp")
    tr = lambda X: sum(hi[i, j] * X[i, j] for i in range(4) for j in range(4))
    P = lambda X: X - tr(X) * h / 3
    kap = sp.Symbol("kappa", positive=True)
    Sm = S1 + S2 if MUT.get("a1_composite") else S1                  # the mutant: one junction both sheets act on
    jump = -(kap ** 2 / 2) * P(Sp) - (kap ** 2 / 2) * P(Sm)         # K^+ - K^-
    eqs = [sp.expand(e) for e in (jump + kap ** 2 * P(S1 + S2))]
    sol = sp.solve(eqs, up, dict=True)
    Sp_sol = Sp.subs(sol[0]) if sol else None
    fixed = Sp_sol is not None and sp.simplify(Sp_sol - (S1 + 2 * S2)) == sp.zeros(4)
    # J2's split at tau = 3/4 against the side total: they differ by S1/4 + S2, zero on 139 (1)'s tensions alone
    sig = sp.Symbol("sigma", positive=True)
    diff_t = sp.simplify(((S1 + 2 * S2) - (sp.Rational(3, 4) * S1 + S2)).subs(
        {**{e: v for e, v in zip(S1, (-sig * h))}, **{e: v for e, v in zip(S2, (sig / 4 * h))}}))
    return dict(fixed=fixed, tensions_agree=diff_t == sp.zeros(4))


def _null_stress():
    """S(k, k) for tension plus a perfect fluid, k null in the bulk, on the surface h(k, k) = -k_y^2"""
    lam, rho, p, kx, ky = sp.symbols("lambda rho p k_x k_y", real=True)
    h = sp.diag(-1, 1, 1, 1)
    u = sp.Matrix([-1, 0, 0, 0])                                    # u_a
    k0 = sp.sqrt(kx ** 2 + ky ** 2)
    k = sp.Matrix([k0, kx, 0, 0])                                   # k^a along the surface
    S = -lam * h + (rho + p) * u * u.T + p * h
    val = sp.expand(sp.simplify((k.T * S * k)[0]))
    return sp.simplify(val - ((lam + rho) * ky ** 2 + (rho + p) * kx ** 2)) == 0


def a2():
    sig = sp.Symbol("sigma", positive=True)
    r1, r2, w1, w2 = sp.symbols("rho1 rho2 w1 w2", nonnegative=True)
    t2 = -sig / 4 if not MUT.get("a2_minus_sigma") else -sig          # the mutant: position 2's tension read as -sigma
    readings = {"summed": (sig + t2, r1 + r2, w1 + w2), "ours": (sig, r1, w1),
                "side": (sig + 2 * t2, r1 + 2 * r2, w1 + 2 * w2),
                "J2": ((1 + t2 / sig) * sig + t2, sp.Rational(3, 4) * r1 + r2, sp.Rational(3, 4) * w1 + w2)}
    tension = {n: sp.simplify(v[0] / sig) for n, v in readings.items()}
    pos = all(sp.simplify(v[0]).is_positive and sp.simplify(v[0] + v[1]).is_positive and
              sp.simplify(v[2]).is_nonnegative for v in readings.values())
    x = sp.Symbol("x", real=True)                                   # both matters at density x sigma, the bound on x
    bounds = {n: sp.solve(sp.Eq((v[0] + v[1].subs({r1: x * sig, r2: x * sig})) / sig, 0), x)[0]
              for n, v in readings.items()}
    PG = _load("p2_gravity.py", "b5ar_pg")
    sigma_SI = 3 * PG.C ** 4 / (4 * sp.pi.evalf() * PG.G * PG.ELL_MAX ** 2)
    # each plane's offset enters as a tension does: the strictest reading's bound on position 2's
    d1, d2 = sp.symbols("delta_1 delta_2", real=True)
    so = -1 if MUT.get("a2_offset_sign") else 1                     # the mutant: the offset entering with the wrong sign
    off = {"summed": d1 + d2, "ours": d1, "side": d1 + 2 * d2, "J2": d1 + d2}
    obound = {n: sp.solve(sp.Eq(readings[n][0] + so * off[n], 0), d2)[0] for n in ("summed", "side", "J2")}
    strict = max(obound.values(), key=lambda e: float(e.subs({sig: 1, d1: 0})))
    PW = _load("pointwise.py", "b5ar_pw")
    pw = all(ok for _, ok in PW.checks(PW.compute()))
    return dict(null=_null_stress(), tension=tension, pos=pos, bounds=bounds, weakest=max(bounds.values()),
                sigma6=float(sigma_SI / 6), sigma4=float(sigma_SI / 4), obound=obound, strict=strict, pointwise=pw,
                strict_SI=float(strict.subs({sig: sigma_SI, d1: 5.25e-10})))


def a3():
    """the shared induced metric on a homogeneous slice; the null-dust carrier's Codazzi identity and its NEC"""
    kap, sig, a, H = sp.symbols("kappa sigma a H", positive=True)
    r1, p1, r2, p2 = sp.symbols("rho1 p1 rho2 p2", real=True)
    k1, k2 = kap ** 2 * sig / 6, kap ** 2 * sig / 12
    Sm, Pm = sig + r1, -sig + p1
    w2 = 1 if MUT.get("a3_tau_split") else 2                       # the mutant: J2's split, position 2's matter once
    Sp, Pp = sig / 2 + r1 + w2 * r2, -sig / 2 + p1 + w2 * p2
    C1, C2 = [a ** 4 * ((kap ** 2 * s / 6) ** 2 - kk ** 2 - H ** 2) * -1 for s, kk in ((Sm, k1), (Sp, k2))]
    gap = sp.simplify(C2 - C1 - a ** 4 * (kap ** 2 / 6) ** 2 * (sig * (r1 - 2 * r2) - 4 * r2 * (r1 + r2)))
    t = sp.Symbol("t")
    af, rf, pf = sp.Function("a")(t), sp.Function("rho")(t), sp.Function("p")(t)
    cons = {sp.Derivative(rf, t): -3 * sp.diff(af, t) / af * (rf + pf)}
    trace_id = sp.simplify(sp.diff(af ** 4 * rf, t).subs(cons) - af ** 4 * sp.diff(af, t) / af * (rf - 3 * pf)) == 0
    Q = sp.expand(4 * (Sm ** 2 - Sp ** 2 - 3 * sig ** 2 / 4) + 6 * Sp * (Sp + Pp) - 6 * Sm * (Sm + Pm))
    eps = sp.Symbol("epsilon")
    Q1 = sp.expand(sp.series(Q.subs({r1: eps * r1, p1: eps * p1, r2: eps * r2, p2: eps * p2}), eps, 0, 2).removeO()
                   .subs(eps, 1))
    first = sp.simplify(Q1 - sig * ((r1 - 3 * p1) - 2 * (r2 - 3 * p2))) == 0
    # the Gauss pair differentiated, ours conserved, position 2's with Codazzi's gamma Cdot: Cdot as computed
    Sm_, Sp_, Pm_, Pp_, Hd, X, gam, C1_ = sp.symbols("S_m S_p P_m P_p Hdot X gamma C_1", real=True)
    c = (kap ** 2 / 6) ** 2
    C2_ = C1_ + a ** 4 * (c * (Sm_ ** 2 - Sp_ ** 2) - 3 * c * sig ** 2 / 4)
    e1 = sp.Eq(2 * c * Sm_ * (-3 * H * (Sm_ + Pm_)), 2 * H * Hd + 4 * H * C1_ / a ** 4)
    e2 = sp.Eq(2 * c * Sp_ * (-3 * H * (Sp_ + Pp_) + gam * X), 2 * H * Hd - X / a ** 4 + 4 * H * C2_ / a ** 4)
    sol = sp.solve([e1, e2], [Hd, X], dict=True)[0][X]
    Qs = 4 * (Sm_ ** 2 - Sp_ ** 2 - 3 * sig ** 2 / 4) + 6 * Sp_ * (Sp_ + Pp_) - 6 * Sm_ * (Sm_ + Pm_)
    pair = sp.simplify(sol - H * a ** 4 * c * Qs / (1 + 2 * c * a ** 4 * Sp_ * gam)) == 0
    # a canonical scalar of position 2's own: its null energy for every V, and the two components on the sheet
    a0, a1_, a2_, a3_, a4_, Vp = sp.symbols("phidot phi_x phi_y phi_z phi_n V", real=True)
    eta = sp.diag(-1, 1, 1, 1, 1)
    dphi = sp.Matrix([a0, a1_, a2_, a3_, a4_])                       # d_a phi in an orthonormal frame
    sgn = -1 if MUT.get("a3_scalar_ghost") else 1                   # the mutant: a ghost, the kinetic sign reversed
    Tsc = sgn * (dphi * dphi.T - eta * ((dphi.T * eta.inv() * dphi)[0] / 2)) - eta * Vp
    kx, ky = sp.symbols("k_x k_n", real=True)
    kv = sp.Matrix([sp.sqrt(kx ** 2 + ky ** 2), kx, 0, 0, ky])
    Tkk = sp.simplify((kv.T * Tsc * kv)[0])
    nec = sp.simplify(Tkk - (kv.T * dphi)[0] ** 2) == 0
    home = {a1_: 0, a2_: 0, a3_: 0}                                  # homogeneous on the sheet, at rest
    Tun = sp.simplify(Tsc[0, 4].subs(home))
    Tnn = sp.simplify(Tsc[4, 4].subs(home))
    comps = sp.simplify(Tun - a0 * a4_) == 0 and sp.simplify(Tnn - (a4_ ** 2 / 2 + a0 ** 2 / 2 - Vp)) == 0
    return dict(gap=gap == 0, trace_id=trace_id, Q=Q, first=first, pair=pair, codazzi=_vaidya(), scalar_nec=nec,
                scalar_comps=comps)


_V = {}


def _vaidya():
    """the brane's Codazzi identity in Vaidya-AdS5, in and out: d Sigma + 3 H (Sigma + Pi) = -(3/(kappa^2 a^3)) w dC"""
    key = bool(MUT.get("a3_nec_sign"))
    if key in _V:
        return _V[key]
    out = {}
    for sense in (1, -1):                                          # 1: ingoing (v), -1: outgoing (u)
        v, x, y, z, tau = sp.symbols("v x y z tau", real=True)
        r, k, kap = sp.symbols("r k kappa", positive=True)
        C = sp.Function("C")(v)
        f = k ** 2 * r ** 2 - C / r ** 2
        X = [v, r, x, y, z]
        g = sp.zeros(5)
        g[0, 0], g[0, 1], g[1, 0] = -f, sense, sense
        for i in (2, 3, 4):
            g[i, i] = r ** 2
        gi = g.inv()
        Gam = [[[sp.simplify(sum(gi[i, d] * (sp.diff(g[d, b], X[c]) + sp.diff(g[d, c], X[b]) - sp.diff(g[b, c], X[d]))
                                 for d in range(5)) / 2) for c in range(5)] for b in range(5)] for i in range(5)]
        ric = lambda b, c: sp.simplify(sum(sp.diff(Gam[i][b][c], X[i]) - sp.diff(Gam[i][b][i], X[c]) + sum(
            Gam[i][i][d] * Gam[d][b][c] - Gam[i][c][d] * Gam[d][b][i] for d in range(5)) for i in range(5)))
        Rvv = ric(0, 0)
        Rs = sp.simplify(sum(gi[i, j] * ric(i, j) for i in range(5) for j in range(5) if gi[i, j] != 0))
        Tvv = sp.simplify(Rvv - Rs * g[0, 0] / 2 - 6 * k ** 2 * g[0, 0])          # kappa^2 T_vv, Lambda = -6 k^2
        a = sp.Function("a", positive=True)(tau)
        vt = sp.Function("vt")(tau)
        ad = sp.diff(a, tau)
        fb = f.subs(r, a).subs(v, vt)
        wd = (sense * ad + sp.sqrt(ad ** 2 + fb)) / fb             # the future root of -f w^2 + 2 sense w a' = -1
        u = [wd, ad, 0, 0, 0]
        nl = [ad, -wd, 0, 0, 0]                                    # n_a, the normal into r < a
        sub = {v: vt, r: a}
        Kxx = -sum(Gam[m][2][2].subs(sub) * nl[m] for m in range(5)) / a ** 2
        ud = [sp.diff(wd, tau).subs(sp.Derivative(vt, tau), wd), sp.diff(ad, tau), 0, 0, 0]
        acc = [ud[b] + sum(Gam[b][c][d].subs(sub) * u[c] * u[d] for c in range(5) for d in range(5)) for b in range(5)]
        Kuu = -sum(nl[b] * acc[b] for b in range(5))
        Sr = -(6 / kap ** 2) * Kxx
        Pi = -(2 / kap ** 2) * Kuu - sp.Rational(2, 3) * Sr
        cod = (sp.diff(Sr, tau) + 3 * ad / a * (Sr + Pi)).subs(sp.Derivative(vt, tau), wd)
        Cp, Cv = sp.symbols("Cp Cv")
        cod = cod.replace(lambda e: isinstance(e, sp.Subs) or (isinstance(e, sp.Derivative) and
                                                               e.expr == sp.Function("C")(vt)), lambda e: Cp)
        cod = cod.subs(sp.Function("C")(vt), Cv)
        F, A, AD = sp.symbols("F A adot", positive=True)
        c2 = cod.subs(sp.Derivative(a, tau), AD).subs(a, A).subs(Cv, k ** 2 * A ** 4 - A ** 2 * F)
        w = (sense * AD + sp.sqrt(AD ** 2 + F)) / F
        ratio = sp.simplify(c2 / (-3 * Cp * w ** 2 / (kap ** 2 * A ** 3)))
        static = sp.simplify(Kxx.subs(sp.Derivative(a, tau, 2), 0).subs(sp.Derivative(a, tau), 0)
                             .subs(sp.Function("C")(vt), 0))
        # the Gauss pair's factor 1 + 2 (kappa^2/6)^2 a^4 Sigma^+ gamma: gamma = -3 w/(kappa^2 a^3) and
        # kappa^2 Sigma^+/6 = s/a give 1 - s w
        s_ = sp.sqrt(AD ** 2 + F)
        gamma = -3 * w / (kap ** 2 * A ** 3)
        sp_ = 6 * s_ / (kap ** 2 * A)
        factor = sp.simplify(1 + 2 * (kap ** 2 / 6) ** 2 * A ** 4 * sp_ * gamma - (1 - s_ * w)) == 0
        # the Gauss pair: Cdot [1 - (kappa^2 Sigma^+/6) a w] = H a^4 (kappa^2/6)^2 Q (a3's pair)
        denom = sp.simplify(1 - s_ * w)
        dCdw_sign = sp.simplify(denom / (AD / A))                  # dC/dw = Cdot/w = H a^4 (k^2/6)^2 Q/(denom w)
        sgn_T = 1 if sense == 1 else -1                            # kappa^2 T_ww = sense 3 dC/dw/(2 r^3)
        if MUT.get("a3_nec_sign"):
            sgn_T = -sgn_T
        # NEC: T_ww >= 0  <=>  sgn_T * dC/dw >= 0  <=>  sgn_T * Q * dCdw_sign >= 0 (A, w > 0)
        nec_if_Q_neg = sp.simplify(sgn_T * dCdw_sign / w).is_negative
        out[sense] = dict(Tvv=sp.simplify(Tvv - sense * 3 * sp.diff(C, v) / (2 * r ** 3)) == 0, ratio=ratio,
                          static=static, denom=denom, factor=factor, nec_if_Q_neg=bool(nec_if_Q_neg))
    _V[key] = out
    return out


F_LAW = {}


def population():
    """the clause per class from its law: every reading positive, worst case our matter 0"""
    wit_t = {1: [-sp.Rational(1, 4)], 0: [-sp.Rational(1, 8), -sp.Integer(10), -sp.Rational(1, 100), sp.Rational(1, 2)]}
    wit_m = {1: [sp.Rational(1, 2), sp.Integer(20)], 0: [sp.Integer(0), sp.Rational(1, 10), sp.Rational(1, 5)]}
    F = {}
    for ti, ts in wit_t.items():
        for mi, ms in wit_m.items():
            vals = set()
            for T in ts:
                for P in ms:
                    reads = (1 + T + P, 1, 1 + 2 * T + 2 * P, 1 + 2 * T + P)   # summed, ours, side, J2 (tau = 1 + T)
                    vals.add(int(all(rr > 0 for rr in reads)))
            F[(ti, mi)] = vals
    if MUT.get("a4_readme_can_fail"):
        F[(1, 1)] = {0, 1}
    return F


_A4 = {}


def a4():
    key = bool(MUT.get("a4_readme_can_fail"))
    if key in _A4:
        return _A4[key]
    CR = _load("c4_residue.py", "b5ar_cr")
    IA = _load("index_audit.py", "b5ar_ia")
    F = population()
    out = {}
    for k in (2, 3):
        out[k] = sum((CR._ask_one(("f",), F, k, tf=tf, mf=mf, c4row=(1, 1))
                      for tf, mf in itertools.product((0, 1), repeat=2)), Counter())
    kmap = dict(zip(CR.NAMES4, range(4)))
    kn = CR._cells("f", kmap, F, ("quantum", 1, 1), CR.A4, CR.CD4)
    au = IA.audit_index(["K", "t", "m", "f"], kn)
    _A4[key] = dict(F=F, out=out, audit=bool(au["keys"] or au["onehot"]))
    return _A4[key]


def a6():
    """item 339 (Q5): Israel's condition with each side's own coupling -- the jump of (K - K h)/kappa^2 -- fixes
    Sigma^- + Sigma^+ = 2 (S1 + S2) for every pair of couplings"""
    h = sp.diag(-1, 1, 1, 1)
    hi = h.inv()

    def sym(name):
        s = sp.symbols(name + "_0:10")
        it = iter(s)
        M = sp.zeros(4)
        for i in range(4):
            for j in range(i, 4):
                M[i, j] = M[j, i] = next(it)
        return M, list(s)
    S1, _ = sym("t1")
    S2, _ = sym("t2")
    Sp, up = sym("tp")
    tr = lambda X: sum(hi[i, j] * X[i, j] for i in range(4) for j in range(4))
    P = lambda X: X - tr(X) * h / 3
    km, kp = sp.symbols("kappa_m kappa_p", positive=True)
    Km = (km ** 2 / 2) * P(S1)                                        # our side, Sigma^- = S1 (A1, p2_assume Q2)
    Kp = -(kp ** 2 / 2) * P(Sp)
    if MUT.get("a6_one_coupling"):                                    # the mutant: a jump in K alone, one coupling
        lhs = (Kp - Km) / km ** 2
    else:
        lhs = Kp / kp ** 2 - Km / km ** 2
    eqs = [sp.expand(e) for e in (lhs + P(S1 + S2))]
    sol = sp.solve(eqs, up, dict=True)
    Sp_sol = Sp.subs(sol[0]) if sol else None
    free = Sp_sol is not None and sp.simplify(Sp_sol - (S1 + 2 * S2)) == sp.zeros(4)
    # the same condition from its (K - K h) form: trace-reversing the jump gives back -S
    lhs2 = (Kp - tr(Kp) * h) / kp ** 2 - (Km - tr(Km) * h) / km ** 2
    form = sp.simplify((lhs2 + (S1 + S2)).subs({e: v for e, v in zip(up, [Sp_sol[i, j] for i in range(4)
                                                                         for j in range(i, 4)])})) == sp.zeros(4) \
        if Sp_sol is not None else False
    return dict(free=free, form=form)


def compute():
    return dict(a1=a1(), a2=a2(), a3=a3(), a4=a4(), a6=a6())


def report(o):
    print("b5a_residue.py -- theorem row B5a brought level (item 282 (c))\n")
    print("A1 Sigma^+ = S1 + 2 S2 fixed for general stresses: %s; J2's split and the side total agree on tensions: %s"
          % (o["a1"]["fixed"], o["a1"]["tensions_agree"]))
    b = o["a2"]
    print("A2 S(k,k) = (lambda + rho) k_y^2 + (rho + p) |k|^2: %s; tension parts in sigma %s; every reading positive: "
          "%s; bounds on rho/sigma %s, weakest %s; sigma/6 = %.2g J/m^3 (sigma/4 = %.2g)" % (
              b["null"], b["tension"], b["pos"], b["bounds"], b["weakest"], b["sigma6"], b["sigma4"]))
    c = o["a3"]
    print("A3 C2 - C1 formula: %s; d(a^4 rho)/dt = a^4 H (rho - 3p): %s; Q at first order sigma [(rho1 - 3p1) - "
          "2 (rho2 - 3p2)]: %s; Cdot from the Gauss pair: %s; scalar carrier: T_kk = (k . d phi)^2 %s, T_un and T_nn "
          "%s" % (c["gap"], c["trace_id"], c["first"], c["pair"], c["scalar_nec"], c["scalar_comps"]))
    for s, d in c["codazzi"].items():
        print("   %s: kappa^2 T = +-3 C'/(2 r^3): %s; Codazzi ratio %s; static K^x_x %s; Gauss-pair factor %s; NEC iff "
              "Q <= 0: %s" % ("ingoing" if s == 1 else "outgoing", d["Tvv"], d["ratio"], d["static"], d["denom"],
                             d["nec_if_Q_neg"]))
    z = o["a4"]
    print("A4 population %s; order 2 %s, order 3 %s; audit flagged %s" % (z["F"], dict(z["out"][2]), dict(z["out"][3]),
                                                                           z["audit"]))
    print("A6 (item 339 (Q5)) two couplings: Sigma^+ = S1 + 2 S2 whatever kappa_-, kappa_+: %s; the (K - K h)/kappa^2 "
          "form agrees: %s" % (o["a6"]["free"], o["a6"]["form"]))


def checks(o):
    res = []
    add = lambda n, ok: res.append((n, bool(ok)))
    rul = " ".join(open(RULINGS, encoding="utf-8").read().split())
    add("A0 282 (c), 276, 275, 117, 284, 202, 139 (1), 226, 320 and the C4 verifier's two at 310 verbatim in the "
        "rulings file",
        all(w in rul for w in WORDS))
    add("A1 the junction fixes Sigma^+ = S1 + 2 S2 for general stresses given Sigma^- = S1; J2's split agrees on "
        "tensions", o["a1"]["fixed"] and o["a1"]["tensions_agree"])
    b = o["a2"]
    sig = sp.Symbol("sigma", positive=True)
    ok = b["null"] and b["pos"] and b["tension"] == {"summed": sp.Rational(3, 4), "ours": 1, "side": sp.Rational(1, 2),
                                                     "J2": sp.Rational(1, 2)}
    ok &= b["bounds"] == {"summed": -sp.Rational(3, 8), "ours": -1, "side": -sp.Rational(1, 6),
                          "J2": -sp.Rational(2, 7)} and b["weakest"] == -sp.Rational(1, 6)
    ok &= "%.2g" % b["sigma6"] == "2.5e+52" and "%.2g" % b["sigma4"] == "3.7e+52" and b["pointwise"]
    d1 = sp.Symbol("delta_1", real=True)
    ok &= sp.simplify(b["strict"] - (-sig / 4 - d1 / 2)) == 0 and "%.2g" % b["strict_SI"] == "-3.7e+52"
    add("A2 every reading positive on every ray: the matter condition proved pointwise (pointwise.py, item 320); with "
        "the offsets, position 2's must exceed -sigma/4 - delta sigma_1/2 = -3.7e52 J/m^3", ok)
    c = o["a3"]
    ok = c["gap"] and c["trace_id"] and c["first"] and c["pair"] and c["scalar_nec"] and c["scalar_comps"]
    ok &= all(d["Tvv"] and d["ratio"] == 1 and sp.simplify(d["static"] + sp.Symbol("k", positive=True)) == 0
              and d["factor"] and d["nec_if_Q_neg"] for d in c["codazzi"].values())
    add("A3 the one-way reading on one induced metric: C2 - C1 as computed; both bulks vacuum only if (rho1 - 3p1) = "
        "2 (rho2 - 3p2); a scalar of position 2's own carries it with T_kk = (k . d phi)^2 >= 0; null dust keeps "
        "117/120 iff Q <= 0, ingoing and outgoing", ok)
    z = o["a4"]
    ok = z["F"] == {(1, 1): {1}, (1, 0): {1}, (0, 1): {0, 1}, (0, 0): {0, 1}}
    ok &= all(z["out"][k] == Counter({(1,): 96}) for k in (2, 3)) and not z["audit"]
    add("A4 B5a's question through the calculator: the clause realized per class from its law; 1 at orders 2 and 3 "
        "under all 96 codings; audit clean", ok)
    add("A6 (item 339 (Q5)) Israel's condition with each side's own coupling: Sigma^- + Sigma^+ = 2 (S1 + S2) for every "
        "pair of five-dimensional couplings, so A1's side total and A2's readings need no single kappa",
        o["a6"]["free"] and o["a6"]["form"])
    return res


MUTANTS = {"a1_composite": "one junction both sheets act on, Sigma^- = S1 + S2 (A1)",
           "a2_minus_sigma": "position 2's tension read as -sigma (A2)",
           "a2_offset_sign": "a plane's offset entering with the wrong sign (A2)",
           "a3_tau_split": "position 2's matter counted once on its side (A3)",
           "a3_nec_sign": "the null dust's energy sign reversed (A3)",
           "a3_scalar_ghost": "the scalar carrier a ghost, its kinetic sign reversed (A3)",
           "a4_readme_can_fail": "M's class with the README realized {0, 1} (A4)",
           "a6_one_coupling": "two couplings written as a jump in K alone with one coupling (A6, item 339)"}


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
        print("  mutant %-20s %-56s %s" % (kk, desc, "caught by " + ", ".join(failed) if failed else "NOT CAUGHT"))
    print("mutants: %d/%d caught" % (caught, len(MUTANTS)))
    return caught == len(MUTANTS)


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    if "--mutants" in sys.argv:
        sys.exit(0 if mutants() else 1)
    report(compute())
