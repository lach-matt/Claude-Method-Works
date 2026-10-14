#!/usr/bin/env python3
"""c4_residue.py -- item 307: "Address these please, close the residue".  C4 one-way's residue (c4_oneway P21 (2)-(13)
with its notes), one section per item, each closed where reasoning and computation close it and, where they do not,
stated exactly with what would close it.  Worked in the conversation (computed with sympy, exact where marked; READ
where marked, the source quoted; deduced where marked; estimates marked; not verified by a separate session; not
seated); 2026-10-12.

  R0 (read) M's item-307 words, verbatim in the rulings file.
  R1 (P21 (2), (5): the kink through the faces; KTN's profile) Closed by scope, and its condition by a theorem.  M1 is
     claimed at flat order (P6), where there is no kink -- the plane is the exact equator in every chart of the object,
     the extrinsic curvature zero for any F(UV), r(UV) (P2, computed, exact; the C4 verifier's 269: "at flat order there
     is no kink").  The kink through the faces is a warp-order addendum, outside the claim.  Its condition: the static
     solution's Euclidean section is a Riemannian Einstein manifold, smooth at the horizon (the bolt, kappa = 1/r_h, P15),
     and DeTurck and Kazdan, Theorem 5.2 (READ, Ann. Sci. ENS 14 (1981) 249-260): "Let (M,g) be a connected Einstein
     manifold of class C^2 with dim M >= 3. Then g is real analytic in harmonic and geodesic normal coordinates."  So a
     static brane hole that exists with a regular horizon is analytic there in the bulk, and P15's continuation follows
     -- on the brane itself by elliptic regularity up to the boundary (Morrey and Nirenberg, 1957; cited, not READ).
     What stays is existence at r_h/ell = 8.0e-16: the small-hole limit (KTN to ~0.2 ell; Figueras-Wiseman's family down
     to 0.07 ell, read at 261), disputed by Yoshino 2009 and Kleihaus et al. 2011 as 261 records; Karasik, Sahabandu,
     Suranyi and Wijewardhana (READ, gr-qc/0404015, abstract, the RS-I TeV brane, not ours): "We find a solution with a
     regular horizon but its asymptotic expansion in the mass also contains half integer powers."  That is the
     literature's, for the warp-order kink only; it would close with a matched expansion in r_h/ell on a
     positive-tension brane.
     [Item 310, the C4 verifier's (8), accepted: Theorem 5.2 is interior regularity -- its proof reads "Equation (5.1)
     is quasi-linear elliptic in harmonic coordinates ... all of its solutions are real analytic" -- so it makes a
     static brane hole's bulk metric analytic away from the brane, given existence and a C^2 bolt.  The brane is a
     junction where the metric is not C^2 (K = -h/ell), and P15 uses analyticity at the brane-bolt corner: that needs a
     boundary-regularity result for Israel's condition (Morrey-Nirenberg's complementing condition for Einstein's
     equations in harmonic gauge with that boundary condition), cited and not checked.  And analyticity at r_h
     continues the profile within its domain of analyticity, not "until r reaches the quantum region".  At flat order
     the kink clause holds vacuously, as above; its warp-order half is carried, conditional on existence and that step.]
  R2 (P21 (2): tau's domain) Closed: no gap.  tau is defined where the sheets coincide (j_readings J2: "away from the
     corridor, where the sheets coincide"); at the corridor what position 2 receives is what passes, the README, whose
     density at its plane is E7's.  With matter on position 2's plane what it receives is determined in full -- the
     summed stress S1 + S2, a tensor (tau_share T3, computed, exact); "no single number" is its form, not a gap.
  R3 (P21 (3), (5): the flux's size and its bending) Closed by bound and by order.  P5's 0.29 sigma carries hold_small's
     effective greybody gamma_eff; with every greybody factor at 1 (the bound) the flux is 0.29/gamma_eff sigma and its
     bending 3 rho/sigma of the tension's (computed): both below the figures R3 prints.  The bending is K r_h = 3
     (rho/sigma)(r_h/ell), so it vanishes at flat order with r_h/ell (computed, exact) -- warp order, like the kink, and
     falling as (r_h/r)^2: the plane's solved shape under the flux is a warp-order correction outside M1's flat-order
     claim, bounded here.
     [Item 310, the C4 verifier's (9) and (10): greybody 1 is not strictly the bound -- the scalar's factor is 1.003 --
     and P5's 0.29 includes the bulk graviton's 0.6%, which does not land on P1; both under 1%.  The check was one-sided
     (K_max < 7.5e-16) and passed with Israel's factor 3 dropped; it now pins K_max = 7.4e-16 per r_h, with that mutant.]
  R4 (P21 (4): the board's readings) Each reduced to a ruling, a computation or a derivation.  (i) The density scaling
     (P18) realizes M's 300 and nothing more: the cells it gives are those of "survival built in" itself, (the README,
     any tension) -> 1 (computed).  (ii) The channel reading (P20) carries no weight in the one-condition form: there the
     top order is 3 and the operator alone agrees, 1, 1, 1 (P17-P18, computed); it decides only order 4 of the
     two-clause coding, whose (b)/(e) is void as evidence by 211 anyway.  (iii) The coding: at order 3 every coding gives
     1, 1, 1 -- 6 orderings, 24 two-bit codes, 24 codes over four interiors (computed) -- and the one-condition form
     over the four interiors (302) gives it at orders 2 and 3 under all 24 orderings and 4 orientations of tension and
     matter, 96 of 96 (computed).  (iv) The placement is the one reading still bearing weight: peers -- every language
     reading tension and matter -- decides in 60 of the 96 and is refused in 36, information's join again (computed);
     at statistics' rank, 96 of 96.  It is derived, not chosen: P13's -- information can reach C4's combination only as
     a join, which depends on an order that relative tension and matter across infinite universes do not have (295) --
     and 292's reason, that they bear directly on statistical plausibility.  (v) The vacuum reading of (a) is derived, not chosen: (a) is
     a classical clause ("at flat order in classical GR", P6), asked where classical geometry holds; the shell's Israel
     stress is classical stress in the bulk; inside the quantum region the classical equations do not hold (273, b_bounce
     Q4), so Ricci-flatness there has no classical meaning.  Under the other classical reading -- (a) outside the hole,
     K1's scope -- the shell's (a) is 1 too and the quantum bounce's stays 1 (computed): every classical reading gives 1.
     [Item 310, the C4 verifier's (5): R6 carries (b)/(e) through an effective core whose Einstein tensor is not zero
     (the null energy negative).  Read on that metric -- the one the residue uses for (b)/(e) -- the route is not
     Ricci-flat, and with the quantum bounce's (a) entered 0 the calculator returns 0 in 96/96 (304 (5)).  So (a) at the
     bounce is 1 on the reading that the core is outside classical geometry; on R6's effective metric (a) over the whole
     route is 0.  "Every classical reading gives 1" holds for the two readings named here, not for R6's.]
  R5 (P21 note: the inner horizon's exterior) Closed by recomputation.  The inner horizon needs charge or spin (b_interior
     B3), so its exterior carries Maxwell stress or rotation: its (a) is 0 and the outside clauses kept from C1 ((c), (d),
     N1) fail there.  Entered so -- (a) at the inner horizon 0, and the outside clauses as a fourth clause, 0 there and
     1 elsewhere -- C4's four clauses come back 1, 1, 1, 1 at orders 2 and 3 in the one-condition form over the four
     interiors (302), all 24 orderings (computed).  Over the three of P17-P18 alone the top order refuses (a): the
     quantum bounce would be the only vacuum interior, every change of the continuation flipping (a); the fourth, the
     singular interior, vacuum too, keeps it -- so the form is the one condition over four interiors.
     [Item 310, the C4 verifier's (6): a rotating (Myers-Perry) exterior is Ricci-flat, so "its (a) is 0" holds for
     charge only.  The fourth interior is needed for (a) at the top order only when the inner horizon is charged; if it
     spins, its (a) is 1, three interiors agree (P18), and the four-interior result stays 1, 1, 1, 1 (96/96 at orders 2
     and 3, the verifier computed).  The outside clauses still fail there: a spinning exterior is not Tangherlini.]
  R6 (P21 (8): the bounce named, not constructed; P21 (5): the quantum region's duration) Constructed, as an effective
     metric.  The interior in its own time T: ds^2 = -dT^2 + G(T) dt^2 + R(T)^2 dOmega_3^2, G = r_h^2/R^2 - 1.  Its
     Einstein tensor vanishes exactly where R'^2 = r_h^2/R^2 - 1 (Tangherlini's interior, computed, exact): with R(T)
     even, Tangherlini for T < 0 (our future interior) and its image under T -> -T for T > 0 (position 2's past
     interior, b_bounce Q1's map), and a minimum R(0) = r_min > 0 between, the metric is smooth across T = 0; the curves
     of fixed (t, angles) are geodesics in proper time T, so the route is complete through the bounce; the null energy
     at the bounce is negative (computed, exact: the core violates it, as 273's quantum region does), and the curvature
     is finite there.  The crossing of the core: Tangherlini takes r_q^2/(2 r_h) of proper time from r_q to 0
     (computed, exact to first order in r_q/r_h); with the core at the scale (r_h l5^2)^(1/3) (an estimate, the effective
     loop-quantum scaling) that is 1.6e-7 of a clock.  The core's own profile is a model; the two-exterior bounce now
     exists as a smooth effective metric, and its quantum-gravitational form stays beyond any computation here.
     [Item 310, the C4 verifier's (2), accepted: R6 constructs less than "the two-exterior bounce now exists".
     "Tangherlini for T < 0" cannot hold literally -- Tangherlini reaches R = 0 at finite T -- so R6 is Tangherlini for
     |T| >= T_c, a smooth even R(T) with a minimum r_min > 0 between, vacuum exactly outside the core; no R(T) is given.
     The route check Gamma^a_TT = 0 is the curves of fixed (t, angles), the E~ = 0 geodesics, which run from bifurcation
     sphere to bifurcation sphere, the sphere 282 drops; for E~ != 0 completeness through the core follows from Tdot^2 =
     eps + E~^2/G with G > 0 (deduced), not computed.  The 1.6e-7 clocks (1.646e-7) is an E~ = 0 observer's proper time
     over Tangherlini's r_q to 0, r_q an estimate; the check, which a core twice as large passed, now pins 1.6e-7, with
     that mutant.  Locally this is Haggard and Rovelli's geometry; which exterior the white hole opens on is fixed by the
     identification (273) and, for the README itself, by the quantum region's form (R13), not by this metric.]
  R7 (P21 (9): J1's source marked two-way) Closed: J1's one input from m1p2x_fifth F1 -- the junction's energy seen by
     matter emerging across position 2's face, mu E~/(kappa |V|) -- follows from the Kruskal Killing field alone: xi =
     kappa (V d_V - U d_U), on the face U = 0 xi = kappa V d_V, so the emerging matter's momentum along the face's
     generator is p_V = E~/(kappa |V|) (computed, exact), with nothing from position 2 reaching ours.  With the junction's
     rise from m1p2x_oneway O3 (one-way), J1's 33.6 clocks reproduce (computed).
     [Item 310, the C4 verifier's (1): "E~ = |p . xi|" hides the sign -- matter crossing U = 0, V < 0 outward has p . xi
     > 0, while a route entering our face keeps p . xi = -E~ through a t-independent core and cannot leave by U = 0, V <
     0 of b_bounce Q1's image chart (R13).  33.6 clocks is the magnitude at that face, standing where the README does
     emerge there.]
  R8 (P21 (10): tau's 2 : 1 bulk at warp order) Carried.  With position 2's side at curvature k/2 (P19, our side at its
     own k), position 2's exterior at warp order is Schwarzschild-AdS5 of radius 2 ell: at a shared horizon its mass
     parameter r_h^2 (1 + r_h^2/ell_2^2) differs from ours by -(3/4)(r_h/ell)^2 = -4.8e-31 (computed).  P1's "position 2
     reads the same mass" is exact at flat order and holds to 5e-31 at warp order.
     [Item 310, the C4 verifier's (3), accepted: item 240 (READ, M verbatim): "The mass on position 2's side is not
     equal to ours" -- M-P2-MASS-OWN, the board's m2 = m overruled there, 240 (a) re-reading 203's "read the same from
     both sides" as the README's encoding, not equal energies in SI.  P1 asserted SI equality through the isometry, and
     neither c4_oneway, this file nor m1_small cited 240 for it.  Seated: position 2 reads from its own exterior the mass
     it assembles under its own laws (240); in the two-exterior effective geometry, with position 2's G5 and bulk taken
     as ours, that equals ours at flat order -- the construction's simplification, not a claim; and -(3/4)(r_h/ell)^2 is
     the mass-parameter difference at an assumed common r_h, the isometry this section itself breaks at warp order.
     Recorded as the verifier's reading of how 275 and P19 combine (deduced, not computed here): identifying position
     2's side of the coincident junction (P19's k/2 bulk) with the region beyond the white-hole face would put the far
     hemisphere of our hole in position 2's bulk, which our full-sphere Komar reading (N1) integrates over -- an
     influence of position 2's bulk on ours at order (r_h/ell)^2, against 276 (a); neither P19 nor this section
     addresses it.]
  R9 (P21 (11): the population's binary classes) Closed: the classes carry no weight.  Refined -- tension: 139 (1)'s
     -1/4, any other negative, any positive; matter: the README, other matter above sigma/4, other below or none -- with
     (f) realized per class from its law and survival built in, the cypher gives 1, 1, 1 at orders 2 and 3 under all 24
     orderings of the four interiors (computed).
     [Item 310, the C4 verifier's (9): the class (other negative tension, other matter below sigma/4 or none) was
     realized {0} by the witnesses chosen; tau = -1/100 with rho/sigma = 1/5 gives 1.  The witnesses now include them,
     the class realized {0, 1}, and the cypher still gives 1, 1, 1 at orders 2 and 3 under all 24 orderings.]
  R10 (P21 (12): the singular interior's (f)) Closed: read instead as vacuous -- nothing of its route lands, so
     positivity where relevant holds nowhere-relevant -- or left out of (f)'s question, C4's (f) is unchanged (computed);
     and the one-condition form (P17-P18) has no singular interior.
  R11 (P21 (6): "C4 is classical") Closed as a computed scope.  The formed hole's outgoing flux loads P1 with rho/sigma
     = 0.29 (r_h/r)^2: below 1% beyond 5.3 r_h and below 0.1% beyond 17 r_h (computed), so clause (d) -- no matter stress
     on P1 -- holds semiclassically there, and M1's far reading (c), r_h << r << ell, lies wholly beyond; near the hole
     the plane's quantum load is of the tension's order, and M1 is classical there, as the qualification says.
     [Item 310, the C4 verifier's (9): 5.3 r_h is where the load rho/sigma falls below 1%; by P14's own Israel ratio
     the bending is 3 rho/sigma, below 1% only beyond 9.3 r_h and below 0.1% beyond 29 r_h.  Seated: the load below 1%
     beyond 5.3 r_h, the bending below 1% beyond 9.3 r_h.]
  R12 (deduced) The ledger.  Closed: (2) both halves, (3), (4), (6), (8) (as an effective metric), (9), (10), (11), (12),
     the inner horizon's exterior, the vacuum reading.  Stated, not closable by the board: small brane holes' existence
     at r_h/ell = 8.0e-16, for the warp-order kink only (R1, the literature's); the quantum region's quantum-gravitational
     form (R6); and (7), a separate session's verification, which waits on M's finalization (249).  Still bearing
     weight, derived: tension and matter read at statistics' rank (R4 (iv), P13, 292).  The form C4's question now
     stands in: clause by clause, the continuation one condition over four interiors, tension and matter at statistics'
     rank over the population, survival built in -- 1 on every clause at every lawful order (2 and 3, the top), every
     ordering and orientation.
     [Item 310: C4 one-way CONFIRMED with qualifications by its verifier.  By the verifier's (4), in this form the
     operator alone gives 1, 1, 1 at orders 2 and 3 under all 96 codings, and on every clause that is the entered value
     read back -- (a) and (b)/(e) the quantum bounce's own row at the other (tension, matter) classes (entered 0 there,
     the calculator returns 0), (f) C4's own class at the other continuations at order 3 (E7) and the README column at
     order 2 (300 (b)).  Each clause depends only on the continuation or only on (tension, matter), so statistics at
     order >= 2 cannot but return the entered value.  The agreement rests on statistics' rank (peers 60/96), survival
     built in ((f) open at order 2 without it), the population ((f) refused at order 3 without it) and the fourth
     interior given the inner horizon's (a) = 0; it adds nothing to E7, to 300 (b), to the vacuum reading or to
     b_interior B6.  211's audit: the full indices are clean; the (K, answer) projection on which order, geometry or
     information decide (a) and (b)/(e) (32/32/32 of 96) is keyed by K on the known cells, and the verdict logic takes
     is statistics', on the clean index.  Seated in R1, R3-R9, R11, R13 and here; the record is item 310.]
  R13 (item 310, the C4 verifier's (1); computed, exact; deduced where marked) The face the route leaves by.  R6's
     metric does not depend on t and its gluing (T, t) -> (-T, t) keeps d_t, so a route's p . d_t is conserved through
     the core and dt/dlambda = p_t/G with G > 0 there: t is monotone along it (deduced).  With xi = kappa (V d_V - U d_U),
     b_bounce Q1's (U, V) -> (-U, -V) carries xi to xi' and Haggard and Rovelli's time reflection (U, V) -> (-V, -U)
     carries it to -xi' (computed).  A route entering our face with Killing energy E~ > 0 (p . d_t = -E~) leaves into
     the exterior where the continued d_t is future-directed: under either map M that is M's image of the second
     exterior, through the face opposite M's image of our face -- the image chart's V' = 0 under Q1, U' = 0, V' < 0
     under the time reflection -- never M's image of ours (computed).  So the face P1, R6, R7 and b_bounce Q1 assign
     position 2 -- U' = 0, V' < 0 of Q1's image chart, onto Q1's image of our exterior -- is out of reach of any body
     crossing a t-independent core: it is reached with the time reflection's map, or through a core that reverses the
     Killing energy, which nothing here constructs.  The board's critic (deduced): the verifier's further clause, that
     the exterior reached is "locally the one Haggard and Rovelli reconnect to ours", holds under Q1 (the image chart's
     region I, where the time reflection places ours) and not under the time reflection, where a t-independent core
     sends the route to its image of the second exterior, opposite their reconnection.  And the README is not such a
     body on b_bounce Q5's reading: it is the matter that collapses and bounces (115 (c)), and in Haggard and Rovelli's
     construction the collapsing matter leaves as its own image under the gluing map, through a quantum region that is
     not t-independent (their region III, an ansatz, b_bounce Q6), its Killing energy reversed against the continued
     d_t.  Under Q1 that image leaves by U' = 0, V' < 0 onto Q1's image of our exterior (computed) -- the face the
     record names.  So the record's face stands for the README on Q5's reading with a quantum region of Haggard and
     Rovelli's kind, which R6 does not model along the README; R6 and this section concern bodies that cross a
     t-independent core after it.  Which exterior is position 2's is M's identification (273); P1 and P15 hold with
     either map, both keeping U V.
     [Item 311 (c5_oneway U9): "the README" in the critic's scope is the README on reading (ii), one whole body that
     collapses and bounces (b_bounce Q5).  On reading (i), the hole standing at its size through the write, its parts
     are bodies crossing the core of a hole already standing (i_oneway I2, I5), and the first half of this section
     applies to them.]
     [Item 312 (c5_oneway U10): M's 273 ("README only") and 282 (2) ("no horizons" before the opening) exclude reading
     (i), and 162 ("the throat doesn't change size") reading (ii); on the object they leave the README is all in when
     the faces begin, and the critic's scope covers it whole.]

Imports c4_oneway.py, tau_share.py, calculator.py, b_interior.py, hold_small.py, p2_gravity.py, e_positive.py and
research/warp-drive/hlaw.py by path.  Stdlib + sympy.  python3 c4_residue.py [--selftest | --mutants]
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
M307 = "Address these please, close the residue"
_C = {}


def _load(name, key):
    if key in _C:
        return _C[key]
    path = name if os.path.isabs(name) else os.path.join(HERE, name)
    spec = importlib.util.spec_from_file_location(key, path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[key] = mod
    saved = list(sys.path)
    sys.path[:0] = [os.path.dirname(path)]
    try:
        with contextlib.redirect_stdout(io.StringIO()):
            spec.loader.exec_module(mod)
    finally:
        sys.path[:] = saved
    _C[key] = mod
    return mod


def c4():
    return _load("c4_oneway.py", "c4r_c4")


def tools():
    C4 = c4()
    CA = _load("calculator.py", "c4r_calc")
    HL = _load(os.path.join(os.path.dirname(D68), "hlaw.py"), "c4r_hl")
    return C4, CA, HL


def r1():
    eq = c4().equator()
    return dict(flat_exact=eq["zero"])


def r2():
    TS = _load("tau_share.py", "c4r_ts")
    o = TS.compute()
    ok = {n.split()[0]: v for n, v in TS.checks(o)}
    return dict(T3=ok["T3"], received=o["tv"]["received"])


def r3():
    C4 = c4()
    s = C4.state()
    H = _load("hold_small.py", "c4r_hs")
    g = H.l5_checks()["gamma_eff"]
    if MUT.get("greybody_ignored"):
        g = 1.0
    ratio_max = s["ratio"] / g
    PG = _load("p2_gravity.py", "c4r_pg")
    l5 = (PG.HBAR * PG.G * PG.ELL_MAX / PG.C ** 3) ** (1 / 3)
    rh = (2 * 2742570311524972 * math.log(2) / math.pi ** 2) ** (1 / 3) * l5
    x, q = sp.symbols("x q", positive=True)                  # x = r_h/ell, q = rho/sigma
    K = 3 * q * x
    israel = 1 if MUT.get("israel_one") else 3              # item 310 (10): the mutant drops Israel's factor 3
    return dict(gamma=g, ratio=s["ratio"], ratio_max=ratio_max, K_max=israel * ratio_max * rh / PG.ELL_MAX,
                flat=sp.limit(K, x, 0) == 0)


NAMES4 = ("singular", "inner", "quantum", "shell")
A4 = {"singular": 1, "inner": 0, "quantum": 1, "shell": 0}       # (a): the inner horizon's charge or spin (B3)
BE4 = {"singular": 0, "inner": 0, "quantum": 1, "shell": 1}      # (b)/(e): b_interior B6
CD4 = {"singular": 1, "inner": 0, "quantum": 1, "shell": 1}      # the outside clauses kept from C1 ((c), (d), N1)


def _cells(cl, kmap, F, skip, A, extra):
    rows = []
    for k in NAMES4:
        for (t, m), fv in F.items():
            if (k, t, m) == skip:
                continue
            vals = {A[k]} if cl == "a" else {BE4[k]} if cl == "be" else {extra[k]} if cl == "cd" else fv
            for v in vals:
                rows.append((kmap[k], t, m, v))
    return rows


F18 = {(1, 1): {1}, (1, 0): {0, 1}, (0, 1): {1}, (0, 0): {0, 1}}


def _ask_one(cls, F, k, views_kind="stat", A=None, extra=None, tf=0, mf=0, c4row=(1, 1)):
    """the one-condition form over the four interiors (302), every ordering of the continuation's values"""
    C4, CA, HL = tools()
    A = A or A4
    extra = extra or CD4
    res = Counter()
    Ff = {(t ^ tf, m ^ mf): v for (t, m), v in F.items()}
    tq, mq = c4row[0] ^ tf, c4row[1] ^ mf
    for perm in itertools.permutations(range(4)):
        kmap = dict(zip(NAMES4, perm))
        at = (kmap["quantum"], tq, mq)
        views = dict(order=(0,), algebra=(0,), geometry=(0,), information=(0,), statistics=(0, 1, 2)) \
            if views_kind == "stat" else {L: (0, 1, 2) for L in ("order", "algebra", "geometry", "information",
                                                                 "statistics")}
        ans = []
        for cl in cls:
            kn = _cells(cl, kmap, Ff, ("quantum", tq, mq), A, extra)
            ans.append(C4._staged(CA, HL, ["K", "t", "m", cl], kn, at, views, k)["answer"])
        res[tuple(ans)] += 1
    return res


def r4():
    C4 = c4()
    EP = _load("e_positive.py", "c4r_ep")
    R = sp.Float(EP.example()["R_rh"] ** 3, 20)
    rel = C4.relative(R)["realized"]
    sv = C4.higher(survive=True)
    mc = C4.more_continuations()
    peers = {k: sum((_ask_one(("a", "be", "f"), F18, k, "peers", tf=tf, mf=mf) for tf, mf in
                     itertools.product((0, 1), repeat=2)), Counter()) for k in (2, 3)}
    stat = {k: sum((_ask_one(("a", "be", "f"), F18, k, "stat", tf=tf, mf=mf) for tf, mf in
                    itertools.product((0, 1), repeat=2)), Counter()) for k in (2, 3)}
    shell_vac = {k: _ask_one(("a",), F18, k, A={"singular": 1, "inner": 0, "quantum": 1, "shell": 1}) for k in (2, 3)}
    return dict(density=rel == {1}, one3=sv["one"][3], bits3=sv["bits"][3], mc3=mc["all"][3], peers=peers, stat=stat,
                shell_vac=shell_vac)


def r5():
    A, extra = dict(A4), dict(CD4)
    if MUT.get("inner_vacuum"):
        A["inner"], extra["inner"] = 1, 1
    three = {}
    for k in (2, 3):                                        # beside it, the three interiors of P17-P18 alone
        C4, CA, HL = tools()
        res = Counter()
        for perm in itertools.permutations(range(3)):
            kmap = dict(zip(("inner", "quantum", "shell"), perm))
            at = (kmap["quantum"], 1, 1)
            views = dict(order=(0,), algebra=(0,), geometry=(0,), information=(0,), statistics=(0, 1, 2))
            kn = [(kmap[kk], t, m, A[kk]) for kk in ("inner", "quantum", "shell") for (t, m) in F18
                  if (kk, t, m) != ("quantum", 1, 1)]
            res[C4._staged(CA, HL, ["K", "t", "m", "a"], kn, at, views, k)["answer"]] += 1
        three[k] = res
    return dict(four={k: _ask_one(("a", "be", "cd", "f"), F18, k, A=A, extra=extra) for k in (2, 3)}, three=three)


def ricci_diag(g, X):
    n = len(X)
    gi = g.inv()
    Gam = [[[sp.simplify(sum(gi[a, d] * (sp.diff(g[d, b], X[c]) + sp.diff(g[d, c], X[b]) - sp.diff(g[b, c], X[d]))
                             for d in range(n)) / 2) for c in range(n)] for b in range(n)] for a in range(n)]
    Ric = sp.zeros(n, n)
    for b in range(n):
        for c in range(b, n):
            v = sum(sp.diff(Gam[a][b][c], X[a]) for a in range(n)) - sum(sp.diff(Gam[a][b][a], X[c]) for a in range(n))
            v += sum(Gam[a][a][d] * Gam[d][b][c] - Gam[a][c][d] * Gam[d][b][a] for a in range(n) for d in range(n))
            Ric[b, c] = Ric[c, b] = sp.simplify(v)
    return Ric, Gam


def r6():
    T, t, th, ph, ps = sp.symbols("T t theta phi psi", real=True)
    rh = sp.Symbol("r_h", positive=True)
    Rf = sp.Function("R")(T)
    G = rh ** 2 / Rf ** 2 - 1
    g = sp.diag(-1, G, Rf ** 2, Rf ** 2 * sp.sin(th) ** 2, Rf ** 2 * sp.sin(th) ** 2 * sp.sin(ph) ** 2)
    X = [T, t, th, ph, ps]
    Ric, Gam = ricci_diag(g, X)
    gi = g.inv()
    Rs = sp.simplify(sum(gi[i, i] * Ric[i, i] for i in range(5)))
    Ein = sp.simplify(Ric - Rs * g / 2)
    # Tangherlini's interior: R'^2 = r_h^2/R^2 - 1, R'' = -r_h^2/R^3
    R0, R1, R2 = sp.symbols("R0 R1 R2")
    sub = lambda e: sp.simplify(e.subs(sp.Derivative(Rf, (T, 2)), R2).subs(sp.Derivative(Rf, T), R1).subs(Rf, R0))
    E = [sub(Ein[i, i]) for i in range(5)]
    vac = all(sp.simplify(e.subs(R2, -rh ** 2 / R0 ** 3).subs(R1, sp.sqrt(rh ** 2 / R0 ** 2 - 1))) == 0 for e in E)
    # at the bounce: R' = 0, R'' > 0; the null energy along k = d_T + d_t/sqrt(G) and along d_T + d_angle/R
    rmin, a2 = sp.symbols("r_min a2", positive=True)
    if MUT.get("no_bounce"):
        a2 = -a2                                           # the mutant: a maximum, not a bounce
    at_b = {R1: 0, R2: a2, R0: rmin}
    Gb = rh ** 2 / rmin ** 2 - 1
    nec_t = sp.simplify(E[0].subs(at_b) + E[1].subs(at_b) / Gb)
    nec_a = sp.simplify(E[0].subs(at_b) + E[2].subs(at_b) / rmin ** 2)
    neg = bool((nec_t.subs({rh: 1, rmin: sp.Rational(1, 100), a2: 1})) < 0 or (nec_a.subs({rh: 1, rmin: sp.Rational(1, 100), a2: 1})) < 0)
    # geodesics: d_T curves -- Gamma^a_TT = 0 for every a
    geod = all(sp.simplify(Gam[a][0][0]) == 0 for a in range(5))
    # curvature finite at the bounce: the Ricci scalar there
    Rs_b = sp.simplify(sub(Rs).subs(at_b))
    finite = Rs_b.is_finite is not False and not Rs_b.has(sp.zoo)
    # the core's crossing: Tangherlini from r_q to 0, dT = dr / sqrt(r_h^2/r^2 - 1)
    r, rq = sp.symbols("r r_q", positive=True)
    exact = sp.integrate(r / sp.sqrt(rh ** 2 - r ** 2), (r, 0, rq))
    first = sp.series(exact, rq, 0, 3).removeO()
    PG = _load("p2_gravity.py", "c4r_pg")
    l5 = (PG.HBAR * PG.G * PG.ELL_MAX / PG.C ** 3) ** (1 / 3)
    rhv = (2 * 2742570311524972 * math.log(2) / math.pi ** 2) ** (1 / 3) * l5
    rqv = (rhv * l5 ** 2) ** (1 / 3)
    if MUT.get("core_x2"):
        rqv = 2 * rqv                                      # item 310 (10): the mutant doubles the core
    clock = rhv / PG.C
    t_core = float(exact.subs({rh: rhv, rq: rqv})) / PG.C
    return dict(vac=vac, neg=neg, geod=geod, finite=finite, first=sp.simplify(first - rq ** 2 / (2 * rh)) == 0,
                core_clocks=t_core / clock, nec_t=nec_t, nec_a=nec_a)


def r7():
    U, V, kap, E = sp.symbols("U V kappa E_t", real=True)
    xi = (-kap * U, kap * V)                               # components along d_U, d_V
    if MUT.get("wrong_killing"):
        xi = (-kap * U, kap)
    # on the face U = 0 a momentum with Killing energy E~ = |p . xi| has p_V = E~ / (kappa |V|)
    pV = sp.Symbol("p_V")
    sol = sp.solve(sp.Eq(pV * xi[1].subs(U, 0), -E), pV)[0]
    ok = sp.simplify(sol - E / (kap * sp.Abs(V)).subs(V, -sp.Symbol("w", positive=True)).subs(sp.Symbol("w", positive=True), -V)) == 0
    ok = sp.simplify(sol.subs(V, -sp.Symbol("w", positive=True)) - E / (kap * sp.Symbol("w", positive=True))) == 0
    PG = _load("p2_gravity.py", "c4r_pg")
    l5 = (PG.HBAR * PG.G * PG.ELL_MAX / PG.C ** 3) ** (1 / 3)
    rhv = (2 * 2742570311524972 * math.log(2) / math.pi ** 2) ** (1 / 3) * l5
    dtau = math.log(1 + math.pi / 10 * PG.ELL_MAX / rhv)
    return dict(pV=ok, dtau=dtau)


def r8():
    x = sp.Symbol("x", positive=True)                      # r_h/ell, ours
    ratio2 = sp.Rational(1, 2) if not MUT.get("same_bulk") else 1   # position 2's curvature over ours, P19
    d = sp.simplify(x ** 2 * (ratio2 ** 2 - 1))            # mu = r_h^2 (1 + r_h^2/ell^2); ell_2 = ell / ratio2
    PG = _load("p2_gravity.py", "c4r_pg")
    l5 = (PG.HBAR * PG.G * PG.ELL_MAX / PG.C ** 3) ** (1 / 3)
    rhv = (2 * 2742570311524972 * math.log(2) / math.pi ** 2) ** (1 / 3) * l5
    return dict(coef=sp.simplify(d / x ** 2), value=float(d.subs(x, rhv / PG.ELL_MAX)))


def r9():
    # tension classes: 0 C4's -1/4, 1 other negative, 2 positive; matter: 0 the README, 1 other above sigma/4, 2 other
    # below sigma/4 or none; f = [tau + rho/sigma > 0], the README surviving in every position 2 (300)
    wit_t = {0: [-sp.Rational(1, 4)], 1: [-sp.Rational(1, 8), -sp.Integer(10), -sp.Rational(1, 100)],
             2: [sp.Rational(1, 2)]}                         # item 310 (9): -1/100 with 1/5 realizes (1, 2) -> 1
    wit_m = {1: [sp.Rational(1, 2), sp.Integer(20)], 2: [sp.Integer(0), sp.Rational(1, 10), sp.Rational(1, 5)]}
    F = {}
    for ti, ts in wit_t.items():
        F[(ti, 0)] = {1}                                     # the README: survival built in
        for mi, ms in wit_m.items():
            F[(ti, mi)] = {int(bool(T + P > 0)) for T in ts for P in ms}
    if MUT.get("readme_can_fail"):
        F[(1, 0)] = {0, 1}
    out = {k: _ask_one(("a", "be", "f"), F, k, c4row=(0, 0)) for k in (2, 3)}
    return dict(F=F, out=out)


def r10():
    C4, CA, HL = tools()
    BI = _load("b_interior.py", "c4r_bi")
    cells = BI.cells()
    inter = {"singular": cells[(0, "none", "ours")], "inner": cells[(1, "none", "pos2")],
             "quantum": cells[(0, "quantum", "pos2")], "shell": cells[(0, "shell", "pos2")]}
    names = list(inter)
    own = tuple((inter[k]["nec"], inter[k]["readme_only"]) for k in names)
    cm = dict(zip(names, own))
    views = dict(order=(0, 1), algebra=(0, 1), geometry=(0, 1), information=(0, 1), statistics=(0, 1, 2, 3))
    out = {}
    for mode in ("vacuous", "left_out"):
        res = {}
        for k in (2, 3):
            kn = []
            for kk in names:
                if mode == "left_out" and kk == "singular":
                    continue
                for (t, m), fv in F18.items():
                    if (kk, t, m) == ("quantum", 1, 1):
                        continue
                    vals = {1} if (mode == "vacuous" and kk == "singular") else fv
                    if MUT.get("singular_fails") and kk == "singular":
                        vals = {0}
                    for v in vals:
                        kn.append(cm[kk] + (t, m, v))
            res[k] = C4._staged(CA, HL, ["c1", "c2", "t", "m", "f"], kn, cm["quantum"] + (1, 1), views, k)["answer"]
        res["channel"] = C4._channel_rule([x for x in kn], cm["quantum"] + (1, 1))
        out[mode] = res
    return out


def r11():
    q0 = c4().state()["ratio"]
    return dict(q0=q0, r1=math.sqrt(q0 / 0.01), r01=math.sqrt(q0 / 0.001), b1=math.sqrt(3 * q0 / 0.01),
                b01=math.sqrt(3 * q0 / 0.001))                # item 310 (9): the bending is 3 rho/sigma (P14)


def r13():
    """item 310 (1): the face a route with conserved Killing energy leaves the white-hole interior by"""
    U, V, k, Up, Vp = sp.symbols("U V kappa Up Vp", real=True)
    xi, xip = sp.Matrix([-k * U, k * V]), sp.Matrix([-k * Up, k * Vp])       # components along d_U, d_V
    maps = {"Q1": (sp.Matrix([[-1, 0], [0, -1]]), {U: -Up, V: -Vp}, lambda u, v: (-u, -v)),
            "HR": (sp.Matrix([[0, -1], [-1, 0]]), {U: -Vp, V: -Up}, lambda u, v: (-v, -u))}
    coords = {"I'": (-1, 1), "III'": (1, -1)}             # the image chart's exteriors; U', V' increase to the future
    face_to = {"I'": "V'=0", "III'": "U'=0"}               # the white-hole interior U', V' < 0 meets I' on V' = 0
    out = {}
    for nm, (J, sub, f) in maps.items():
        w = sp.simplify((J * xi).subs(sub))
        sign = 1 if sp.simplify(w - xip) == sp.zeros(2, 1) else -1 if sp.simplify(w + xip) == sp.zeros(2, 1) else 0
        if MUT.get("exit_reversed"):
            sign = -sign                                   # the mutant: a core reversing the Killing energy read as R6's
        # p . d_t = -E~ < 0 conserved: the body leaves where the continued d_t = sign xi' is future-directed
        fut = [reg for reg, (u, v) in coords.items() if sign * -u > 0 and sign * v > 0]
        img = {"I": f(-1, 1), "III": f(1, -1)}
        exit_ = [n for n, c in img.items() if c == coords[fut[0]]][0] if len(fut) == 1 else None
        ours = f(0, 1)                                     # the image of our face U = 0, V > 0
        ours_face = "U'=0" if ours[0] == 0 else "V'=0"
        out[nm] = dict(sign=sign, exit=exit_, face=face_to[fut[0]] if fut else None,
                       opposite=bool(fut) and face_to[fut[0]] != ours_face, mirror_face=ours_face,
                       mirror_exit=[n for n, c in img.items() if face_to[[r for r, cc in coords.items() if cc == c][0]]
                                    == ours_face][0])
    return out


def compute():
    return dict(r1=r1(), r2=r2(), r3=r3(), r4=r4(), r5=r5(), r6=r6(), r7=r7(), r8=r8(), r9=r9(), r10=r10(),
                r11=r11(), r13=r13())


def report(o):
    print("c4_residue.py -- C4's residue closed (item 307)\n")
    print("R1 at flat order the plane is the exact equator in every chart: %s" % o["r1"]["flat_exact"])
    print("R2 tau_share T3 (what position 2 receives with matter, S1 + S2): %s" % o["r2"]["T3"])
    r3 = o["r3"]
    print("R3 gamma_eff %.3f; flux %.3f sigma, at most %.3f with every greybody 1; bending at most K r_h = %.2g; at flat "
          "order zero: %s" % (r3["gamma"], r3["ratio"], r3["ratio_max"], r3["K_max"], r3["flat"]))
    r4 = o["r4"]
    print("R4 density = survival built in: %s; one-condition order 3 %s; two bits %s; four interiors %s" % (
        r4["density"], dict(r4["one3"]), dict(r4["bits3"]), dict(r4["mc3"])))
    for k in (2, 3):
        print("R4 order %d over 96 codings: statistics' rank %s; peers %s; (a) with the shell vacuum %s" % (
            k, dict(r4["stat"][k]), dict(r4["peers"][k]), dict(r4["shell_vac"][k])))
    print("R5 the inner horizon's exterior entered (its (a) 0, the outside clauses 0), four interiors: order 2 %s, "
          "order 3 %s; (a) over three interiors alone: %s" % (dict(o["r5"]["four"][2]), dict(o["r5"]["four"][3]),
                                                              {k: dict(v) for k, v in o["r5"]["three"].items()}))
    r6 = o["r6"]
    print("R6 vacuum where R'^2 = r_h^2/R^2 - 1: %s; null energy negative at the bounce: %s; d_T geodesics: %s; finite "
          "there: %s; core crossing r_q^2/(2 r_h): %s, %.2g clocks" % (r6["vac"], r6["neg"], r6["geod"], r6["finite"],
                                                                     r6["first"], r6["core_clocks"]))
    print("R7 p_V = E~/(kappa |V|) on U = 0 from the Killing field: %s; J1's closing %.1f clocks" % (o["r7"]["pV"],
                                                                                                o["r7"]["dtau"]))
    print("R8 position 2's mass parameter at warp order differs by %s (r_h/ell)^2 = %.2g" % (o["r8"]["coef"],
                                                                                         o["r8"]["value"]))
    print("R9 refined classes: order 2 %s, order 3 %s" % (dict(o["r9"]["out"][2]), dict(o["r9"]["out"][3])))
    print("R10 the singular interior's (f): %s" % o["r10"])
    r11 = o["r11"]
    print("R11 flux load %.2f (r_h/r)^2: below 1%% beyond %.1f r_h, below 0.1%% beyond %.0f r_h; the bending 3 rho/sigma "
          "below 1%% beyond %.1f r_h, 0.1%% beyond %.0f r_h" % (r11["q0"], r11["r1"], r11["r01"], r11["b1"], r11["b01"]))
    for nm, v in o["r13"].items():
        print("R13 %s: xi -> %+d xi'; a body crossing a t-independent core leaves by %s onto the image of %s (opposite the "
              "image of our face: %s); the README as its own image leaves by %s onto the image of %s" % (
                  nm, v["sign"], v["face"], v["exit"], v["opposite"], v["mirror_face"], v["mirror_exit"]))


def checks(o):
    res = []
    add = lambda n, ok: res.append((n, bool(ok)))
    rul = " ".join(open(RULINGS, encoding="utf-8").read().split())
    add("R0 M's item-307 words verbatim in the rulings file", M307 in rul)
    add("R1 M1's flat-order plane is the exact equator in every chart (P2): the kink is warp order", o["r1"]["flat_exact"])
    add("R2 what position 2 receives is determined in full: S1 + S2 (tau_share T3)", o["r2"]["T3"])
    r3 = o["r3"]
    add("R3 the flux at most %.2f sigma with every greybody 1 (0.29 at gamma_eff); its bending at most 7.4e-16 per r_h "
        "(pinned, item 310), zero at flat order" % r3["ratio_max"], r3["gamma"] < 1 and "%.2f" % r3["ratio"] == "0.29"
        and r3["ratio_max"] < 0.32 and "%.2g" % r3["K_max"] == "7.4e-16" and r3["flat"])
    r4 = o["r4"]
    ok = r4["density"] and r4["one3"] == Counter({(1, 1, 1): 6}) and r4["bits3"] == Counter({(1, 1, 1): 24})
    ok &= r4["mc3"] == Counter({(1, 1, 1): 24}) and all(r4["stat"][k] == Counter({(1, 1, 1): 96}) for k in (2, 3))
    ok &= all(r4["shell_vac"][k] == Counter({(1,): 24}) for k in (2, 3))
    add("R4 the readings reduced: the density scaling is 300's survival; at order 3 every coding agrees; statistics' "
        "rank agrees under all 96 codings of the four interiors at orders 2 and 3; (a) is 1 under every classical "
        "reading", ok)
    r5 = o["r5"]
    add("R5 with the inner horizon's exterior entered, C4's four clauses 1, 1, 1, 1 at orders 2 and 3 over the four "
        "interiors; over three alone the top order refuses (a), the quantum bounce then the only vacuum interior",
        all(r5["four"][k] == Counter({(1, 1, 1, 1): 24}) for k in (2, 3)) and r5["three"][2] == Counter({1: 6})
        and r5["three"][3] == Counter({"refused": 6}))
    r6 = o["r6"]
    add("R6 the bounce as an effective metric: vacuum exactly on Tangherlini's interior, null energy negative at the "
        "bounce, the E~ = 0 route a geodesic through it, finite there; the core crossed in 1.6e-7 of a clock (pinned, "
        "item 310)", r6["vac"] and r6["neg"] and r6["geod"] and r6["finite"] and r6["first"]
        and "%.2g" % r6["core_clocks"] == "1.6e-07")
    add("R7 J1's seen energy from the Killing field alone, p_V = E~/(kappa |V|); 33.6 clocks reproduce",
        o["r7"]["pV"] and "%.1f" % o["r7"]["dtau"] == "33.6")
    add("R8 position 2's mass at warp order differs by -(3/4)(r_h/ell)^2 = -4.8e-31",
        o["r8"]["coef"] == -sp.Rational(3, 4) and "%.2g" % o["r8"]["value"] == "-4.8e-31")
    add("R9 refined tension and matter classes: 1, 1, 1 at orders 2 and 3 under all 24 orderings of the four interiors",
        all(o["r9"]["out"][k] == Counter({(1, 1, 1): 24}) for k in (2, 3)))
    r10 = o["r10"]
    add("R10 the singular interior's (f) read as vacuous: C4's (f) 1 at orders 2 and 3 and under the channel reading; "
        "left out, 1 at orders 2 and 3, the channel then lacking the fourth code (P20)",
        all(r10["vacuous"][k] == 1 for k in (2, 3, "channel")) and all(r10["left_out"][k] == 1 for k in (2, 3))
        and r10["left_out"]["channel"] == "refused")
    r11 = o["r11"]
    add("R11 the flux load below 1% beyond 5.3 r_h, below 0.1% beyond 17 r_h; the bending below 1% beyond 9.3 r_h, "
        "0.1% beyond 29 r_h (item 310)", "%.1f" % r11["r1"] == "5.3" and "%.0f" % r11["r01"] == "17"
        and "%.1f" % r11["b1"] == "9.3" and "%.0f" % r11["b01"] == "29")
    r13 = o["r13"]
    add("R13 through a t-independent core a body leaves by the face opposite the map's image of ours, onto the image of "
        "the second exterior, under Q1 (V' = 0) and the time reflection (U' = 0) alike; the README as its own image "
        "leaves by U' = 0, V' < 0 under Q1, onto the image of ours (item 310)",
        r13["Q1"]["sign"] == 1 and r13["HR"]["sign"] == -1 and all(r13[m]["exit"] == "III" and r13[m]["opposite"]
                                                                  for m in ("Q1", "HR"))
        and r13["Q1"]["face"] == "V'=0" and r13["HR"]["face"] == "U'=0" and r13["Q1"]["mirror_face"] == "U'=0"
        and r13["Q1"]["mirror_exit"] == "I")
    return res


MUTANTS = {"greybody_ignored": "the greybody bound dropped (R3)",
           "inner_vacuum": "the inner horizon's exterior taken as vacuum, its outside clauses kept (R5)",
           "no_bounce": "a maximum of R, not a minimum (R6)",
           "wrong_killing": "the Killing field's V component made constant (R7)",
           "same_bulk": "position 2's side at our curvature (R8)",
           "readme_can_fail": "the README failing at some other negative tension (R9)",
           "singular_fails": "the singular interior's (f) read as failing (R10)",
           "israel_one": "Israel's factor 3 dropped from the bending (R3, item 310)",
           "core_x2": "the core twice as large (R6, item 310)",
           "exit_reversed": "a core reversing the Killing energy read as R6's (R13, item 310)"}


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
        print("  mutant %-16s %-60s %s" % (kk, desc, "caught by " + ", ".join(failed) if failed else "NOT CAUGHT"))
    print("mutants: %d/%d caught" % (caught, len(MUTANTS)))
    return caught == len(MUTANTS)


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    if "--mutants" in sys.argv:
        sys.exit(0 if mutants() else 1)
    report(compute())
