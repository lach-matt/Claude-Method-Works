#!/usr/bin/env python3
"""gb_cone.py -- item 326: "let's find the object that does fix it so we can dissolve this caveat".  Item 325's caveat:
alpha = 0 rested on B6' and k_R = k_L/2, both written in Einstein's theory and made definitions by 201; "If B6' were
replaced by its Gauss-Bonnet form, alpha would be free again, and nothing else in the record fixes it."  The object
that fixes it is in the record already: item 324's statement that gravity itself keeps the light cone (relativity.py
U6), held in a bulk that can carry gravity's own waves and a hole.  With alpha != 0, gravity there leaves the light
cone, for either sign of alpha.  Worked in the conversation (computed with sympy, exact; READ where marked; deduced
where marked; not verified by a separate session; not seated); 2026-10-12.

  C0 (read) The words this rests on: M's item 326 and the caveat it quotes, verbatim in the rulings file; 256, "The
     corridor is the brane hole whose horizon holds N bits"; 254, the record's hole verified Ricci-flat with
     "Kretschmann 72 r_h^4/r^8"; and relativity.py U6, where "gravity itself" "keeps the light cone in every frame".
  C1 (computed, exact) The instrument.  The Lovelock tensors written with the generalised Kronecker delta in a
     five-dimensional orthonormal frame: Einstein's G = -(1/4) delta^(3) R, Gauss-Bonnet's H = -(1/8) delta^(5) R R,
     the bulk's law E = G + Lambda + alpha H.  Checked against the record and the literature before it is used: the
     record's hole (f = 1 - m/r^2, m = r_h^2) comes out Ricci-flat with Kretschmann 72 m^2/r^8, 254's figure; the
     Boulware-Deser hole f = kappa + r^2 (1 - q)/(4 alpha), q^2 = 1 + 8 alpha m/r^4 + 4 alpha Lambda/3 (Boulware and
     Deser; Cai, as RTW eq. (5.15) quotes it, READ) solves E = 0 exactly, with alpha, m, Lambda and r left symbolic,
     which fixes the normalisation of the Gauss-Bonnet term.  The principal symbol, the part of the linearised law
     that decides where gravity's waves can go: P(xi) t = -(1/2) [delta^(3) xi xi t + alpha delta^(5) xi xi t R]
     (computed from the linearised Riemann tensor), gauge invariant (P kills xi X + X xi), divergence-free (xi.P = 0)
     and symmetric (computed).  A wavefront with normal xi is characteristic -- a front gravity can carry -- when P(xi)
     has a non-gauge kernel; on the transverse tensors (Reall, Tanahashi and Way, arXiv:1406.3379, section 3.3, READ),
     the test is the vanishing of a determinant, computed here as a polynomial in xi_0.  It does not depend on which
     complement of the gauge directions carries it: transversality without its trace term gives every cone unchanged
     (computed, the instrument's first mutant run, which that change did not fail).
  C2 (computed, exact; READ) Einstein's law: gravity keeps the light cone.  At alpha = 0 the determinant vanishes only
     at xi_0^2 = |xi|^2 -- null fronts, on any background.  RTW (READ): "For the Einstein equation, a hypersurface is
     characteristic if, and only if, it is null: 'gravity travels at the speed of light'".
  C3 (computed, exact) The Gauss-Bonnet law on the record's hole.  On any static, spherical or planar bulk (pair
     curvatures K1 = R^{tr}_{tr}, K2 = R^{ti}_{ti} = R^{ri}_{ri}, K3 = R^{ij}_{ij}), a front moving along the sphere
     is characteristic at xi_0^2 = c |xi|^2 with c1 = (1 + 4 alpha K1)/(1 + 4 alpha K2) twice, c2 = (1 + 4 alpha
     K2)/(1 + 4 alpha K3) twice, and c3 = (3 + 32 alpha K2 + 64 alpha^2 K2^2 - 4 alpha (K1 + K3) - 16 alpha^2 K1
     K3)/(3 (1 + 4 alpha K2)(1 + 4 alpha K3)) once: the graviton's five polarisations, three cones.  Radially every
     front is null.  Each c is 1 when K1 = K2 = K3 -- the bulk's own AdS, curvature without Weyl.
  C4 (computed, exact; READ) On the Boulware-Deser hole, exactly: c1 = 3 - 2A, c2 = A, c3 = 2A - 1, A = (1 + 4 alpha
     Lambda/3)/q^2, for the spherical hole (kappa = 1, the corridor, 256) and the planar one (kappa = 0, uniform dark
     radiation, 185) alike -- RTW's tensor, vector and scalar cones c_T, c_V, c_S (their eqs. (5.13) and (5.17) at d =
     5, READ), here from the field equations directly: two routes, one answer.  And A - 1 = -8 alpha m/(r^4 q^2), so
     2(c_T - 1) + 2(c_V - 1) + (c_S - 1) = 0 (computed): the cones fan out about the light cone and cannot all lie
     inside it.  For alpha m > 0 the tensors are outside it, for alpha m < 0 the vectors and scalars; the fastest
     exceeds light by 16 |alpha| m/(r^4 q^2), at every radius outside the horizon (computed).  RTW (READ): "If c_A(r) >
     1 then the outermost graviton cone lies outside the light cone: gravity travels faster than light ... this is
     often the case, including arbitrarily far from the black hole."
  C5 (computed, exact; READ) On gravity's own wave.  A plane gravitational wave (Weyl type N, profile diag(2, -1, -1)
     eps) solves the Gauss-Bonnet law exactly (computed; RTW: "any such spacetime is a solution of Lovelock theory",
     READ).  A graviton crossing it is characteristic at xi^2 = -(l.xi)^2 omega, omega = 8 alpha eps once, 4 alpha eps
     twice, -8 alpha eps twice (computed), RTW's omega_I = -32 k_2 nu_I with k_2 = -alpha/8 (READ): they sum to zero,
     so some omega is positive for either sign of alpha, a front outside the light cone (RTW: "there is generically at
     least one positive omega_I and so this outermost cone lies outside the light cone", READ).  On the bulk's AdS
     (computed pointwise): the wave solves the law with Lambda = -6 k^2 (1 - 2 alpha k^2), and every omega is divided
     by 1 - 4 alpha k^2, positive throughout relativity U4's range -- the same fan.
  C6 (READ) The same from scattering.  Camanho, Edelstein, Maldacena and Zhiboedov (arXiv:1407.5597, READ: abstract,
     sections 1, 2.4, 4.4 and 8; the rest not read): a graviton crossing a shock wave in Gauss-Bonnet theory gets a
     time advance -- "by choosing different polarizations we can get time advance for b^2 ~ |lambda_GB| for any sign
     of lambda_GB" -- so "the purely Gauss-Bonnet theory (2.17) is acausal"; the violation "cannot be fixed by adding
     conventional particles with spins J <= 2.  But, it can be fixed by adding an infinite tower of extra massive
     particles with higher spins, J > 2", and "a finite number of higher spin particles does not fix the problem".
     The record holds no such tower: what can exist is relativity U1's list -- particles, scalar and gauge fields,
     vacuum, tension, geometry, information (read) -- and a tower would take the bulk's law outside Lovelock's
     premises (local, second order), which U4 used (deduced).
  C7 (deduced) The object, and alpha.  Relativity U6 (item 324, M's statement proved): everything that can exist,
     gravity itself included, keeps the light cone.  The bulk can carry gravity's own waves (U6; bulkwarp W7's bulk
     gravitational waves) and holds the record's hole (256; 254's Kretschmann is not zero, so its Weyl is not).  On
     either, alpha != 0 puts a polarisation of gravity outside the light cone (C4, C5), whatever alpha's sign or size;
     alpha = 0 keeps every front null (C2).  So alpha = 0 exactly, from relativity, without B6' and without 201.
     Item 325's caveat dissolves: B6' and k_R = k_L/2, written in Einstein's theory, are written in the bulk's law, and
     gb_alpha.py's B2-B3 become a second route to the same value -- 201's definitions agree with relativity.
  C8 (read; deduced) The other candidates, and why each is not the object.  B6''s coefficient (gb_alpha B2): exact
     only as 201's definition.  k_R = k_L/2: the ratio is item 200's count ("Once: k_R = k_L/2"), but the flatness
     relation that turns it into a curvature is the junction's, which moves with the law (gb_alpha B3).  Clause (H)'s
     count (253-257): chosen as the hole's own entropy "in the bulk theory", so it follows whatever law the bulk has
     and fixes none (in Gauss-Bonnet the hole's entropy is Jacobson and Myers', (A/4 G)(1 + 12 alpha/r_h^2) for a
     spherical horizon -- standard, not READ).  GW170817's one speed (relativity U2) is measured on our plane, which
     no bulk front of C4 or C5 crosses, and bounds rather than fixes.  The holographic bounds on lambda_GB (RTW's refs
     [4]-[8], NAMED-NOT-READ) assume a dual field theory the record does not have, and bound.
  C9 (the cypher NOT-RUN, stated) Which object fixes alpha is a theorem about the law, not a choice among
     configurations; an index of candidates over (exact, free of Einstein's theory, in the record) would carry the
     answer as the conjunction of its own columns, a key (211), as gb_alpha B6 found.  Not run, and said.

What this does not claim.
  - That gravity has been seen to leave the light cone, or not, in a bulk: the effect at alpha != 0 near a hole is
    16 |alpha| m/(r^4 q^2) and no measurement on our plane reaches it; alpha = 0 is deduced from relativity's
    statement, not measured.
  - A reading, stated: 324's "subject to relativity" is read as U6 words it, the one light cone keeping every front
    at every point of every background that can exist, gravity's included; M's to overrule.  Read only as causality
    seen from far away (C6's asymptotic causality), the record's content gives the same.
  - That no world could hold an infinite tower of higher spins: only that the record holds none.
  - The four-dimensional scalar-Gauss-Bonnet branch of currency.py and doors.py: a scalar coupled to the
    Gauss-Bonnet density, another theory, not evaluated here; the same test applies to it and is not run.
    [Item 327: run in sgb_cone.py -- it fails, for every coupling with f' != 0.]
  - RTW's hyperbolicity results beyond the cones used.

Imports nothing from the record but the rulings file and relativity.py's text.  Stdlib + sympy.
python3 gb_cone.py [--selftest | --mutants]
"""
import itertools
import os
import sys

import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
D68 = os.path.dirname(HERE)
RULINGS = os.path.join(D68, "M-RULINGS-2026-10-03.md")
RELATIVITY = os.path.join(HERE, "relativity.py")
MUT = {}
WORDS = ("B6' and k_R = k_L/2 were both written in Einstein's theory, and 201 made them definitions.If B6' were "
         "replaced by its Gauss-Bonnet form, α would be free again, and nothing else in the record fixes it. - let's "
         "find the object that does fix it so we can dissolve this caveat",
         "The corridor is the brane hole whose horizon holds N bits", "Kretschmann 72 r_h^4/r^8")
WORDS_U6 = ("gravity itself", "keeps the light cone in every frame")
D = 5
ETA = (-1, 1, 1, 1, 1)
x0, al, r, m, L, Q, eps, k = sp.symbols("xi0 alpha r m Lambda Q epsilon k")
K1, K2, K3 = sp.symbols("K1 K2 K3")
SYM = [(a, b) for a in range(D) for b in range(a, D)]


def sign(p):
    s, p = 1, list(p)
    for i in range(len(p)):
        while p[i] != i:
            j = p[i]
            p[i], p[j] = p[j], p[i]
            s = -s
    return s


PERM5 = {a: [(p[1:], sign(p)) for p in itertools.permutations(range(D)) if p[0] == a] for a in range(D)}
PERM3 = [(p, sign(p)) for p in itertools.permutations(range(3))]


def d3(A):
    """X^a_b = delta^{a c1 c2}_{b d1 d2} A[c1][c2][d1][d2], c lower and d upper"""
    X = [[0] * D for _ in range(D)]
    for a, b in itertools.product(range(D), repeat=2):
        s = 0
        for c1, c2, d1, d2 in itertools.product(range(D), repeat=4):
            up, lo = (a, c1, c2), (b, d1, d2)
            det = sum(sg for pi, sg in PERM3 if all(up[i] == lo[pi[i]] for i in range(3)))
            if det:
                s += det * A[c1][c2][d1][d2]
        X[a][b] = s
    return X


def d5(A, B):
    """X^a_b = delta^{a c1..c4}_{b d1..d4} A[c1][c2][d1][d2] B[c3][c4][d3][d4]: in five dimensions eps eps"""
    X = [[0] * D for _ in range(D)]
    for a, b in itertools.product(range(D), repeat=2):
        X[a][b] = sum(sc * sd * A[c[0]][c[1]][d[0]][d[1]] * B[c[2]][c[3]][d[2]][d[3]]
                      for c, sc in PERM5[a] for d, sd in PERM5[b])
    return X


def zero4():
    return [[[[0] * D for _ in range(D)] for _ in range(D)] for _ in range(D)]


def riem_pairs(K):
    """R_{ab}^{cd} of a pair-diagonal bulk from K[(a, b)] = R^{ab}_{ab}"""
    R = zero4()
    for (a, b), v in K.items():
        R[a][b][a][b], R[b][a][b][a], R[a][b][b][a], R[b][a][a][b] = v, v, -v, -v
    return R


def mixed(Rl):
    return [[[[Rl[a][b][c][d] * ETA[c] * ETA[d] for d in range(D)] for c in range(D)] for b in range(D)]
            for a in range(D)]


def static_K(f, kap):
    """C3: pair curvatures of -f dt^2 + dr^2/f + r^2 dSigma_kappa^2 in the orthonormal frame"""
    fp, fpp = sp.diff(f, r), sp.diff(f, r, 2)
    sgn = -1 if MUT.get("riem_sign") else 1                 # the mutant: K1's sign misread
    K = {(0, 1): -sgn * fpp / 2}
    for i in (2, 3, 4):
        K[(0, i)] = -fp / (2 * r)
        K[(1, i)] = -fp / (2 * r)
    for i, j in itertools.combinations((2, 3, 4), 2):
        K[(i, j)] = (kap - f) / r ** 2
    return K


def field_eq(R, alpha, Lam):
    G, H = d3(R), d5(R, R)
    return [[sp.simplify(-G[a][b] / 4 + (Lam if a == b else 0) - alpha * H[a][b] / 8) for b in range(D)]
            for a in range(D)]


def symbol(xi, t, R, alpha):
    """C1: P(xi) t, lower indices"""
    xu = [xi[a] * ETA[a] for a in range(D)]
    tm = [[t[c][d] * ETA[d] for d in range(D)] for c in range(D)]
    S = [[[[xi[c1] * xu[d1] * tm[c2][d2] for d2 in range(D)] for d1 in range(D)] for c2 in range(D)]
         for c1 in range(D)]
    gb = 2 if MUT.get("gb_double") else 1                   # the mutant: the Gauss-Bonnet symbol doubled
    ein = sp.Rational(1, 2) if MUT.get("einstein_half") else 1   # the mutant: Einstein's part halved against it
    X3, X5 = d3(S), d5(S, R)
    return [[sp.expand(-ETA[a] * (ein * X3[a][b] + gb * alpha * X5[a][b]) / 2) for b in range(D)] for a in range(D)]


def unit(a, b):
    t = [[0] * D for _ in range(D)]
    t[a][b] = t[b][a] = 1
    return t


def char_poly(xi, R, alpha):
    """det of P(xi) on transverse tensors (RTW 3.3), rows the spatial P_ij (xi_0 != 0)"""
    xu = [xi[a] * ETA[a] for a in range(D)]
    ts = sp.symbols("t0:15")
    t = [[0] * D for _ in range(D)]
    for n, (a, b) in enumerate(SYM):
        t[a][b] = t[b][a] = ts[n]
    tr = sum(ETA[a] * t[a][a] for a in range(D))
    cons = [sp.expand(sum(xu[b] * t[a][b] for b in range(D)) - xi[a] * tr / 2) for a in range(D)]
    C = sp.Matrix([[sp.diff(c, v) for v in ts] for c in cons])
    Pb = {ab: symbol(xi, unit(*ab), R, alpha) for ab in SYM}
    cols = [[sp.together(sum(v[n] * Pb[SYM[n]][i][j] for n in range(15))) for (i, j) in SYM if i]
            for v in C.nullspace()]
    if len(cols) != 10:
        raise ValueError("transverse space of dimension %d" % len(cols))
    return sp.factor(sp.together(sp.Matrix(cols).T.det()))


def cones(Qp):
    """the non-null characteristic cones: [(xi_0^2 / |xi|^2, multiplicity)] from factors carrying alpha"""
    out = []
    for fac, mult in sp.factor_list(sp.numer(Qp))[1]:
        if fac.has(x0) and fac.free_symbols - {x0}:
            sol = sp.solve(fac, x0 ** 2)
            if len(sol) == 1:
                out.append((sp.factor(sol[0]), mult))
    return out


def null_only(Qp):
    """every factor carrying xi_0 is xi_0 (the basis's) or a null one, xi_0 = +-1 at |xi| = 1"""
    allowed = (x0, x0 - 1, x0 + 1, x0 ** 2 - 1)
    return all(not fac.has(x0) or any(sp.expand(fac - a) == 0 or sp.expand(fac + a) == 0 for a in allowed)
               for fac, _ in sp.factor_list(sp.numer(Qp))[1])


def hole():
    """C1, C3, C4"""
    o = {}
    Kt = static_K(1 - m / r ** 2, 1)
    Rt = riem_pairs(Kt)
    Gt = d3(Rt)
    o["tang_flat"] = all(sp.simplify(Gt[a][b]) == 0 for a in range(D) for b in range(D))
    o["kretsch"] = sp.simplify(4 * sum(v ** 2 for v in Kt.values()))
    q = sp.sqrt(1 + 8 * al * m / r ** 4 + 4 * al * L / 3)
    Kb = static_K(1 + r ** 2 * (1 - q) / (4 * al), 1)
    E = field_eq(riem_pairs({kk: sp.simplify(v) for kk, v in Kb.items()}), al, L)
    o["bd_solves"] = all(e == 0 for row in E for e in row)
    Kg = {(0, 1): K1}
    for i in (2, 3, 4):
        Kg[(0, i)] = Kg[(1, i)] = K2
    for i, j in itertools.combinations((2, 3, 4), 2):
        Kg[(i, j)] = K3
    Rg = riem_pairs(Kg)
    xi = [x0, 0, 1, 0, 0]
    X = sp.symbols("X0:5")
    Pg = symbol(xi, [[xi[a] * X[b] + xi[b] * X[a] for b in range(D)] for a in range(D)], Rg, al)
    tt = [[sp.Symbol("t%d%d" % (min(a, b), max(a, b))) for b in range(D)] for a in range(D)]
    Pt = symbol(xi, tt, Rg, al)
    xu = [xi[a] * ETA[a] for a in range(D)]
    o["gauge"] = all(sp.expand(v) == 0 for row in Pg for v in row)
    o["bianchi"] = all(sp.expand(sum(xu[a] * Pt[a][b] for a in range(D))) == 0 for b in range(D))
    o["symmetric"] = all(sp.expand(Pt[a][b] - Pt[b][a]) == 0 for a in range(D) for b in range(D))
    o["einstein_null"] = null_only(char_poly(xi, Rg, 0))
    o["radial_null"] = null_only(char_poly([x0, 1, 0, 0, 0], Rg, al))
    cg = cones(char_poly(xi, Rg, al))
    o["cones_general"] = cg
    want = [((1 + 4 * al * K1) / (1 + 4 * al * K2), 2), ((1 + 4 * al * K2) / (1 + 4 * al * K3), 2),
            ((3 + 32 * K2 * al + 64 * K2 ** 2 * al ** 2 - 4 * K1 * al - 4 * K3 * al - 16 * K1 * K3 * al ** 2)
             / (3 * (1 + 4 * K2 * al) * (1 + 4 * K3 * al)), 1)]
    o["cones_ok"] = len(cg) == 3 and all(any(sp.simplify(c - w) == 0 and mu == mw for c, mu in cg)
                                         for w, mw in want)
    o["ads_null"] = all(sp.simplify(c.subs({K1: K3, K2: K3}) - 1) == 0 for c, _ in cg)
    # C4: Boulware-Deser, the point's q as Q (8 alpha m = r^4 (Q^2 - 1 - 4 alpha Lambda/3))
    rr, mm = sp.symbols("rr mm", positive=True)
    qf = sp.sqrt(1 + 8 * al * mm / rr ** 4 + 4 * al * L / 3)
    A = (1 + 4 * al * L / 3) / Q ** 2
    o["bd"] = {}
    for kap in (1, 0):
        f = kap + rr ** 2 * (1 - qf) / (4 * al)
        msub = rr ** 4 * (Q ** 2 - 1 - 4 * al * L / 3) / (8 * al)
        at = lambda e: sp.simplify(e.subs(mm, msub).subs(sp.sqrt(Q ** 2), Q).subs(rr, r))
        sub = {K1: at(-sp.diff(f, rr, 2) / 2), K2: at(-sp.diff(f, rr) / (2 * rr)), K3: at((kap - f) / rr ** 2)}
        if MUT.get("riem_sign"):
            sub[K1] = -sub[K1]
        cs = [(sp.simplify(c.subs(sub)), mu) for c, mu in cg]
        rtw = {"T": 3 - 2 * A, "V": A, "S": 2 * A - 1}
        lab = {}
        for c, mu in cs:
            for nm, w in rtw.items():
                if sp.simplify(c - w) == 0:
                    lab[nm] = (c, mu)
        o["bd"][kap] = lab
    o["bd_ok"] = all(set(o["bd"][kp]) == {"T", "V", "S"} and o["bd"][kp]["T"][1] == 2 and o["bd"][kp]["V"][1] == 2
                     and o["bd"][kp]["S"][1] == 1 for kp in (1, 0))
    o["sum_rule"] = sp.simplify(2 * (3 - 2 * A - 1) + 2 * (A - 1) + (2 * A - 1 - 1))
    o["A_minus_1"] = sp.simplify((A - 1).subs(Q ** 2, 1 + 8 * al * m / r ** 4 + 4 * al * L / 3)
                                 + 8 * al * m / (r ** 4 * (1 + 8 * al * m / r ** 4 + 4 * al * L / 3)))
    # either sign, at a point outside the horizon (Lambda = 0, r = 2): q = 1001/1000 or 999/1000, f = 9/10
    o["either_sign"] = {}
    for av, qv in ((sp.Rational(1, 100), sp.Rational(1001, 1000)), (sp.Rational(-1, 100), sp.Rational(999, 1000))):
        Av = 1 / qv ** 2
        fv = 1 + 4 * (1 - qv) / (4 * av)
        mv = 16 * (qv ** 2 - 1) / (8 * av)
        cv = {"T": 3 - 2 * Av, "V": Av, "S": 2 * Av - 1}
        o["either_sign"][av] = (fv, max(cv, key=cv.get), max(cv.values()), mv)
    return o


def typeN(ads):
    """C5: a plane wave (type N, profile diag(2, -1, -1) eps), on flat or AdS curvature, pointwise"""
    lu = (1, 1, 0, 0, 0)
    ll = [lu[a] * ETA[a] for a in range(D)]
    mi = {i: [1 if a == i else 0 for a in range(D)] for i in (2, 3, 4)}
    Rl = zero4()
    g = lambda x, y: ETA[x] if x == y else 0
    sk = 1 if MUT.get("ads_sign") else -1                  # the mutant: AdS's curvature with de Sitter's sign
    for a, b, c, d in itertools.product(range(D), repeat=4):
        if ads:
            Rl[a][b][c][d] += sk * k ** 2 * (g(a, c) * g(b, d) - g(a, d) * g(b, c))
        for i, w in ((2, 2), (3, -1), (4, -1)):
            Rl[a][b][c][d] += eps * w * (ll[a] * mi[i][b] - mi[i][a] * ll[b]) * (ll[c] * mi[i][d] - mi[i][c] * ll[d])
    R = mixed(Rl)
    lam = k ** 2 * (12 * al * k ** 2 - 6) if ads else 0
    E = field_eq(R, al, lam)
    solves = all(e == 0 for row in E for e in row)
    cs = cones(char_poly([x0, 0, 1, 0, 0], R, al))
    # xi^2 = -(l.xi)^2 omega with l.xi = xi_0, |xi| = 1:  xi_0^2 = 1/(1 - omega)
    om = sorted([(sp.factor(1 - 1 / c), mu) for c, mu in cs], key=lambda p: str(p[0]))
    return dict(solves=solves, omegas=om)


def compute():
    return dict(hole=hole(), wave=typeN(False), wave_ads=typeN(True))


def report(o):
    h, w, wa = o["hole"], o["wave"], o["wave_ads"]
    print("gb_cone.py -- the object that fixes alpha: gravity keeps the light cone (item 326)\n")
    print("C1 record's hole Ricci-flat %s, Kretschmann %s; Boulware-Deser solves the law %s; symbol gauge-invariant %s,"
          " divergence-free %s, symmetric %s" % (h["tang_flat"], h["kretsch"], h["bd_solves"], h["gauge"],
                                                 h["bianchi"], h["symmetric"]))
    print("C2 Einstein's law: every front null %s" % h["einstein_null"])
    print("C3 Gauss-Bonnet, along the sphere: %s" % "; ".join("c = %s (x%d)" % (c, mu) for c, mu in
                                                               h["cones_general"]))
    print("   radially null %s; all c = 1 on the bulk's AdS (K1 = K2 = K3) %s" % (h["radial_null"], h["ads_null"]))
    for kap in (1, 0):
        print("C4 Boulware-Deser kappa = %d: %s" % (kap, ", ".join("c_%s = %s (x%d)" % (nm, c, mu) for nm, (c, mu)
                                                                   in sorted(h["bd"][kap].items()))))
    print("   2(c_T - 1) + 2(c_V - 1) + (c_S - 1) = %s; A - 1 + 8 alpha m/(r^4 q^2) = %s" % (h["sum_rule"],
                                                                                         h["A_minus_1"]))
    for av, (fv, nm, cv, mv) in h["either_sign"].items():
        print("   alpha = %s, m = %s, at r = 2 (f = %s): fastest c_%s = %s > 1: %s" % (av, mv, fv, nm, cv, cv > 1))
    print("C5 plane wave solves the law %s; omega = %s" % (w["solves"], ", ".join("%s (x%d)" % p for p in w["omegas"])))
    print("   on the bulk's AdS: solves %s; omega = %s" % (wa["solves"], ", ".join("%s (x%d)" % p
                                                                                  for p in wa["omegas"])))


def checks(o):
    h, w, wa = o["hole"], o["wave"], o["wave_ads"]
    res = []
    add = lambda n, ok: res.append((n, bool(ok)))
    rul = " ".join(open(RULINGS, encoding="utf-8").read().split())
    rel = " ".join(open(RELATIVITY, encoding="utf-8").read().split())
    add("C0 item 326 and its caveat, 256 and 254 verbatim in the rulings file; U6's words in relativity.py",
        all(x in rul for x in WORDS) and all(x in rel for x in WORDS_U6))
    add("C1 record's hole Ricci-flat with Kretschmann 72 m^2/r^8; Boulware-Deser solves the Gauss-Bonnet law exactly",
        h["tang_flat"] and sp.simplify(h["kretsch"] - 72 * m ** 2 / r ** 8) == 0 and h["bd_solves"])
    add("C1 the principal symbol is gauge invariant, divergence-free and symmetric",
        h["gauge"] and h["bianchi"] and h["symmetric"])
    add("C2 Einstein's law (alpha = 0): every characteristic front is null", h["einstein_null"])
    add("C3 Gauss-Bonnet on a static bulk: three cones (x2, x2, x1) along the sphere, null radially, 1 on AdS",
        h["cones_ok"] and h["radial_null"] and h["ads_null"])
    add("C4 Boulware-Deser (kappa = 1, 0): the cones are RTW's c_T = 3 - 2A, c_V = A, c_S = 2A - 1",
        h["bd_ok"])
    add("C4 sum rule 0 and A - 1 = -8 alpha m/(r^4 q^2): the fastest is outside the light cone for either sign",
        h["sum_rule"] == 0 and h["A_minus_1"] == 0
        and all(fv > 0 and mv > 0 and cv > 1 for fv, _, cv, mv in h["either_sign"].values())
        and h["either_sign"][sp.Rational(1, 100)][1] == "T" and h["either_sign"][sp.Rational(-1, 100)][1] != "T")
    ow = sorted(str(sp.factor(p[0])) + "x%d" % p[1] for p in w["omegas"])
    want = sorted(str(sp.factor(v)) + "x%d" % mu for v, mu in ((8 * al * eps, 1), (4 * al * eps, 2),
                                                                (-8 * al * eps, 2)))
    add("C5 a plane wave solves the law; omega = 8 alpha eps, 4 alpha eps (x2), -8 alpha eps (x2), summing to zero",
        w["solves"] and ow == want)
    wa_ok = wa["solves"] and len(wa["omegas"]) == 3 and all(
        any(sp.simplify(p[0] - v / (1 - 4 * al * k ** 2)) == 0 and p[1] == mu for p in wa["omegas"])
        for v, mu in ((8 * al * eps, 1), (4 * al * eps, 2), (-8 * al * eps, 2)))
    add("C5 on the bulk's AdS the wave solves the law and each omega is divided by 1 - 4 alpha k^2", wa_ok)
    return res


MUTANTS = {"gb_double": "the Gauss-Bonnet term of the symbol doubled against the field equation (C1)",
           "riem_sign": "the radial tidal curvature K1 with the wrong sign (C3)",
           "einstein_half": "Einstein's part of the symbol halved against the Gauss-Bonnet part (C1)",
           "ads_sign": "the bulk's AdS curvature given de Sitter's sign (C5)"}


def selftest():
    r_ = checks(compute())
    for n, ok in r_:
        print("  [%s] %s" % ("ok" if ok else "FAIL", n))
    kk = sum(ok for _, ok in r_)
    print("selftest: %d/%d" % (kk, len(r_)))
    return kk == len(r_)


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
        print("  mutant %-15s %-75s %s" % (kk, desc, "caught by " + ", ".join(failed) if failed else "NOT CAUGHT"))
    print("mutants: %d/%d caught" % (caught, len(MUTANTS)))
    return caught == len(MUTANTS)


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    if "--mutants" in sys.argv:
        sys.exit(0 if mutants() else 1)
    report(compute())
