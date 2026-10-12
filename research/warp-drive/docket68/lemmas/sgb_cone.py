#!/usr/bin/env python3
"""sgb_cone.py -- item 327: the light-cone test of relativity U6 run on the four-dimensional scalar-Gauss-Bonnet
theory that currency.py (its "scalar-Gauss-Bonnet branch", arXiv:1904.13091) and doors.py (door one's
Einstein-dilaton-Gauss-Bonnet wormholes, arXiv:1108.3003) rest on, as gb_cone.py ran it on the five-dimensional bulk.
The theory: S = int sqrt(-g) [R/2 - (grad phi)^2/2 - V(phi) + f(phi) L_GB], L_GB the Gauss-Bonnet density, f any
function (exponential for the dilaton, linear for the shift-symmetric case); a constant f is topological in four
dimensions and does nothing, so every wormhole of the branch needs f' != 0.  Worked in the conversation (computed with
sympy, exact; READ where marked; deduced where marked; not verified by a separate session; not seated); 2026-10-12.

  S0 (read) The words this rests on: M's item 327 and the line it quotes, verbatim in the rulings file; relativity.py
     U6, "gravity itself" "keeps the light cone in every frame"; currency.py's "THE SCALAR-GAUSS-BONNET BRANCH ESCAPES
     IT" and doors.py's wormholes "in FOUR-DIMENSIONAL Einstein-dilaton-Gauss-Bonnet".
  S1 (computed, exact) The field equations, derived and checked before use.  Varying the action: the metric equation
     G^a_b + 2 delta^{a c d e}_{b g h k} (nabla_c nabla^g f) R_de^hk = T^a_b (the Gauss-Bonnet density varied with f
     inside, integrated by parts twice; Bianchi's identity removes the rest; computed), the scalar equation box phi - V'
     + f' L_GB = 0.  Checked against the reduced action of a cosmology, -N^2 dt^2 + a^2 dx^2, varied in N, a and phi:
     the Euler-Lagrange equations are -a^3, -3 a^2 and a^3 times the covariant ones, for every f (computed) -- so the
     Gauss-Bonnet term's factor and sign are the action's.  The Friedmann equation: 3 H^2 (1 + 8 H f.) = phi.^2/2 + V.
  S2 (computed, exact) The principal symbol of the coupled system (metric perturbation t, scalar perturbation psi): the
     metric row -(1/2) delta^(3) xi xi t + 2 delta^(4)[-f' xi xi psi R + (nabla nabla f) 2 xi xi t], the scalar row -xi^2
     psi + f' delta^(4) xi xi t R; gauge invariant, divergence-free, and symmetric as an action's must be -- the scalar
     row's coupling to t is -1/2 the metric row's to psi, contracted with t (computed).  Characteristic fronts: the
     vanishing of its determinant on transverse t and psi (Reall, arXiv:2101.11623, sections 2-4, READ in part).  With
     f' = 0 -- Einstein's law and a minimally coupled scalar -- every front is null, on every background used here.
  S3 (computed, exact; READ) On a cosmology.  The tensor fronts: xi_0^2/|xi|^2 = c_T^2 = (1 + 8 f..)/(1 + 8 H f.),
     twice -- Reall's purely gravitational cone, null for the inverse of his effective metric C = g - nabla nabla beta
     (his eq. (91), READ), here with beta = 8 f: two routes, one answer.  The scalar front once, with its own c_S^2.  At
     exact solution points with V = 0 and a linear coupling (H = 1, phi. = 12/5 or -12/5, f' = -1/480 or +1/480, the
     Friedmann equation holding exactly, H. and phi.. from the other two; 8 |H f.| = 1/25), c_T^2 = 537/461 at both,
     above 1 for either sign of f' (computed): in a weakly coupled cosmology gravity's waves outrun light.  Our
     plane's measured one speed (GW170817, relativity U2) bounds 8 (f.. - H f.) today and does not fix f.
  S4 (computed, exact) On gravity's own wave -- the decisive case. A plane gravitational wave (type N, profile diag(1,
     -1) eps) with phi constant solves the theory exactly for every f with V(phi_0) = V'(phi_0) = 0, the branch's
     massless scalar (computed: the metric equation vanishes and L_GB = 0, so the scalar equation does). On it the purely
     gravitational polarization keeps the light cone, and the two others -- graviton and scalar mixed through f' and the
     Weyl curvature -- are characteristic at xi_0^2 = |xi|^2/(1 -+ 8 sqrt(2) f' eps): symmetric about the light cone, so
     one lies outside it for either sign of f' (computed). Every f' != 0 is reached: phi_0 is any point where f' != 0,
     which the branch's wormholes need.
  S5 (READ) The same from scattering.  Serra, Serra, Trincherini and Trombetta (arXiv:2205.08551, which currency.py
     itself cites; READ: abstract, section 1, section 2's eqs. (11)-(13), the rest not read): around a heavy source the
     scalar-graviton mixing gives eigenmodes delayed by 2 r_s (log(b_0/b) +- sqrt(2) |alpha|/b^2), "one of the
     propagation eigenmodes travels faster than what is allowed by the causal structure of the asymptotic spacetime",
     and the time advance is avoided only if new physics enters at |alpha|^(1/2), whose nature they leave open; the
     record holds none (relativity U1's list, read).
  S6 (deduced) The verdict.  For every coupling f with f' != 0 the four-dimensional scalar-Gauss-Bonnet theory carries
     fronts outside the light cone (S4, and S3 in cosmology), so it fails relativity U6 -- whether its scalar is read as
     part of gravity (gravity leaving the light cone) or as matter (U1's scalar fields, which must keep it too).  The
     branch's wormholes need f' != 0 (a constant f is topological in four dimensions), so currency.py's
     scalar-Gauss-Bonnet branch and doors.py's door-one Einstein-dilaton-Gauss-Bonnet solutions rest on a theory
     relativity excludes; their own findings (DEADLINE OPEN, the instability, the bounds) stand as findings about that
     theory and are not repaired.
  S7 (deduced; NOT-RUN) The rest of those instruments' modified gravity, named.  Einsteinian cubic gravity and f(R)
     (currency.py's pure-curvature branch, doors.py's f(R) review) have field equations beyond second order in four
     dimensions, outside relativity U4's law (Lovelock: Einstein's alone, READ there); and the five-dimensional
     Gauss-Bonnet coupling is zero (gb_cone.py, item 326).  Their own light-cone tests are not run here.
  S8 (the cypher NOT-RUN, stated) Whether a theory keeps the light cone is computed from its law, not chosen among
     configurations; an index of theories over (keeps the cone, holds the wormhole) would carry the answer as a key
     (211).  Not run, and said.

What this does not claim.
  - That such a front has been seen: the record's measurement (GW170817) is of one speed on our plane, near-flat.
  - Anything about the wormholes' interiors: the cones are computed on the wave and the cosmology, and S6 needs no
    more; at strong coupling a cosmology's tensor cone can stop being a cone at all (c_T^2 < 0 at 8 H f. = 1/2,
    computed), which RTW and Reall name as a loss of hyperbolicity.
  - A reading, stated: U6's "keeps the light cone" is read as in item 326, one light cone for every front at every
    point of every background that can exist; M's to overrule.

Imports nothing from the record but the text of the rulings file, relativity.py, currency.py and doors.py.
Stdlib + sympy.  python3 sgb_cone.py [--selftest | --mutants]
"""
import itertools
import os
import sys

import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
D68 = os.path.dirname(HERE)
WD = os.path.dirname(D68)
RULINGS = os.path.join(D68, "M-RULINGS-2026-10-03.md")
TEXTS = {os.path.join(HERE, "relativity.py"): ("gravity itself", "keeps the light cone in every frame"),
         os.path.join(WD, "currency.py"): ("THE SCALAR-GAUSS-BONNET BRANCH ESCAPES IT",),
         os.path.join(WD, "doors.py"): ("FOUR-DIMENSIONAL Einstein-dilaton-Gauss-Bonnet",)}
WORDS = ("Not covered: currency.py and doors.py use a four-dimensional scalar-Gauss-Bonnet theory, which is a different "
         "theory. I didn't evaluate it; the same light-cone test applies and hasn't been run. - this next",)
MUT = {}
D = 4
ETA = (-1, 1, 1, 1)
SYM = [(a, b) for a in range(D) for b in range(a, D)]
x0, H, Hd, pd, pdd, f1, f2, eps = sp.symbols("xi0 H Hd pd pdd f1 f2 epsilon")


def sign(p):
    s, p = 1, list(p)
    for i in range(len(p)):
        while p[i] != i:
            j = p[i]
            p[i], p[j] = p[j], p[i]
            s = -s
    return s


PERMD = {a: [(p[1:], sign(p)) for p in itertools.permutations(range(D)) if p[0] == a] for a in range(D)}
PFULL = [(p, sign(p)) for p in itertools.permutations(range(D))]
PERM3 = [(p, sign(p)) for p in itertools.permutations(range(3))]


def d3(A):
    """X^a_b = delta^{a c1 c2}_{b d1 d2} A[c1][c2][d1][d2]"""
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


def d4(Hm, B):
    """X^a_b = delta^{a c d e}_{b g h k} Hm[c][g] B[d][e][h][k]: in four dimensions eps eps"""
    X = [[0] * D for _ in range(D)]
    for a, b in itertools.product(range(D), repeat=2):
        X[a][b] = sum(sc * sd * Hm[c[0]][d[0]] * B[c[1]][c[2]][d[1]][d[2]] for c, sc in PERMD[a] for d, sd in PERMD[b])
    return X


def d4full(A, B):
    return sum(sc * sd * A[c[0]][c[1]][d[0]][d[1]] * B[c[2]][c[3]][d[2]][d[3]] for c, sc in PFULL for d, sd in PFULL)


def gbk():
    return 1 if MUT.get("gb_coeff") else 2                  # the mutant: the Gauss-Bonnet term's factor 2 read as 1


def metric_eq(R, Hf, dphi, V):
    """S1: M^a_b = G^a_b + 2 delta^(4) Hf R - T^a_b (orthonormal, mixed)"""
    G, Y = d3(R), d4(Hf, R)
    X2 = sum(ETA[a] * dphi[a] ** 2 for a in range(D))
    T = [[ETA[a] * dphi[a] * dphi[b] - (X2 / 2 + V) * (1 if a == b else 0) for b in range(D)] for a in range(D)]
    return [[sp.simplify(-G[a][b] / 4 + gbk() * Y[a][b] - T[a][b]) for b in range(D)] for a in range(D)]


def lgb(R):
    return sp.simplify(d4full(R, R) / 4)


def diag_curvature(gdiag, X, phi):
    """coordinates X, diagonal metric: orthonormal R_{ab}^{cd}, mixed Hessian of phi, orthonormal gradient"""
    n = len(X)
    g = sp.diag(*gdiag)
    gi = g.inv()
    Gam = [[[sp.simplify(sum(gi[a, d] * (sp.diff(g[d, b], X[c]) + sp.diff(g[d, c], X[b]) - sp.diff(g[b, c], X[d]))
                             for d in range(n)) / 2) for c in range(n)] for b in range(n)] for a in range(n)]
    Rup = [[[[sp.simplify(sp.diff(Gam[a][b][d], X[c]) - sp.diff(Gam[a][b][c], X[d])
                          + sum(Gam[a][c][e] * Gam[e][b][d] - Gam[a][d][e] * Gam[e][b][c] for e in range(n)))
              for d in range(n)] for c in range(n)] for b in range(n)] for a in range(n)]
    sc = [sp.sqrt(gdiag[a] * ETA[a]) for a in range(n)]
    R = [[[[sp.simplify(g[a, a] * Rup[a][b][c][d] * gi[c, c] * gi[d, d] * sc[c] * sc[d] / (sc[a] * sc[b]))
            for d in range(n)] for c in range(n)] for b in range(n)] for a in range(n)]
    dp = [sp.diff(phi, X[a]) for a in range(n)]
    Hs = [[sp.simplify((sp.diff(phi, X[a], X[b]) - sum(Gam[c][a][b] * dp[c] for c in range(n))) * gi[b, b] * sc[b]
                       / sc[a]) for b in range(n)] for a in range(n)]
    return R, Hs, [sp.simplify(dp[a] / sc[a]) for a in range(n)]


def symbol(xi, t, psi, R, Hf, c1):
    """S2: metric row (lower) and scalar row of the principal symbol"""
    xu = [xi[a] * ETA[a] for a in range(D)]
    tm = [[t[c][d] * ETA[d] for d in range(D)] for c in range(D)]
    Sh = [[[[xi[a] * xu[b] * tm[c][d] for d in range(D)] for b in range(D)] for c in range(D)] for a in range(D)]
    mix = 0 if MUT.get("mix_drop") else 1                   # the mutant: the metric row's scalar mixing dropped
    X3 = d3(Sh)
    Y1 = d4([[-mix * c1 * xi[c] * xu[g] * psi for g in range(D)] for c in range(D)], R)
    Y2 = d4(Hf, [[[[2 * v for v in r3] for r3 in r2] for r2 in r1] for r1 in Sh])
    PM = [[sp.expand(ETA[a] * (-X3[a][b] / 2 + gbk() * (Y1[a][b] + Y2[a][b]))) for b in range(D)] for a in range(D)]
    xi2 = sum(xi[a] * xu[a] for a in range(D))
    return PM, sp.expand(-xi2 * psi + c1 * d4full(Sh, R))


def unit(a, b):
    t = [[0] * D for _ in range(D)]
    t[a][b] = t[b][a] = 1
    return t


def char_poly(xi, R, Hf, c1):
    """determinant on transverse t and psi; rows the spatial metric components and the scalar (xi_0 != 0)"""
    xu = [xi[a] * ETA[a] for a in range(D)]
    ts = sp.symbols("t0:10")
    t = [[0] * D for _ in range(D)]
    for n, (a, b) in enumerate(SYM):
        t[a][b] = t[b][a] = ts[n]
    tr = sum(ETA[a] * t[a][a] for a in range(D))
    C = sp.Matrix([[sp.diff(sp.expand(sum(xu[b] * t[a][b] for b in range(D)) - xi[a] * tr / 2), v) for v in ts]
                   for a in range(D)])
    Pb = {ab: symbol(xi, unit(*ab), 0, R, Hf, c1) for ab in SYM}
    Pp = symbol(xi, [[0] * D for _ in range(D)], 1, R, Hf, c1)
    cols = []
    for v in C.nullspace():
        cols.append([sp.together(sum(v[n] * Pb[SYM[n]][0][i][j] for n in range(10))) for (i, j) in SYM if i]
                    + [sp.together(sum(v[n] * Pb[SYM[n]][1] for n in range(10)))])
    cols.append([Pp[0][i][j] for (i, j) in SYM if i] + [Pp[1]])
    return sp.factor(sp.together(sp.Matrix(cols).T.det()))


def null_only(Qp):
    allowed = (x0, x0 - 1, x0 + 1, x0 ** 2 - 1, x0 ** 2 - 2)
    return all(not fac.has(x0) or any(sp.expand(fac - a) == 0 or sp.expand(fac + a) == 0 for a in allowed)
               for fac, _ in sp.factor_list(sp.numer(Qp))[1])


def cones(Qp, sym):
    out = []
    for fac, mult in sp.factor_list(sp.numer(Qp))[1]:
        if fac.has(x0) and fac.has(sym):
            out.append((fac, mult))
    return out


def frw_point():
    """orthonormal cosmology at a point: pair curvatures Hd + H^2 and H^2; Hessian of f"""
    R = [[[[0] * D for _ in range(D)] for _ in range(D)] for _ in range(D)]
    K = {(0, i): Hd + H ** 2 for i in (1, 2, 3)}
    K.update({(i, j): H ** 2 for i, j in itertools.combinations((1, 2, 3), 2)})
    for (a, b), v in K.items():
        R[a][b][a][b], R[b][a][b][a], R[a][b][b][a], R[b][a][a][b] = v, v, -v, -v
    Hf = [[0] * D for _ in range(D)]
    s00 = 1 if MUT.get("frw_sign") else -1                 # the mutant: nabla_0 nabla^0 f with the wrong sign
    Hf[0][0] = s00 * (f1 * pdd + f2 * pd ** 2)
    for i in (1, 2, 3):
        Hf[i][i] = -H * f1 * pd
    return R, Hf


def field_check():
    """S1: covariant equations against the cosmology's reduced action"""
    t, x, y, z = sp.symbols("t x y z")
    N, a, ph = (sp.Function(s)(t) for s in ("N", "a", "phi"))
    fF, VF = sp.Function("f"), sp.Function("V")
    R, Hs, dph = diag_curvature([-N ** 2, a ** 2, a ** 2, a ** 2], [t, x, y, z], ph)
    Ric = sum(R[i][j][i][j] for i in range(D) for j in range(D))
    L = sp.simplify(N * a ** 3 * (Ric / 2 + ph.diff(t) ** 2 / (2 * N ** 2) - VF(ph) + fF(ph) * lgb(R)))
    EL = lambda q: sp.simplify(sp.diff(L, q) - sp.diff(sp.diff(L, q.diff(t)), t)
                               + sp.diff(sp.diff(L, q.diff(t, 2)), t, 2)).subs(N, 1).doit()
    R1, Hs1, dph1 = diag_curvature([-1, a ** 2, a ** 2, a ** 2], [t, x, y, z], ph)
    fp, fpp = sp.diff(fF(ph), ph), sp.diff(fF(ph), ph, 2)
    Hf = [[sp.simplify(fp * Hs1[i][j] + fpp * dph1[i] * dph1[j] * ETA[j]) for j in range(D)] for i in range(D)]
    M = metric_eq(R1, Hf, dph1, VF(ph))
    S = sp.simplify(sum(Hs1[i][i] for i in range(D)) - sp.diff(VF(ph), ph) + fp * lgb(R1))
    ratios = [sp.simplify(EL(N) / M[0][0]), sp.simplify(EL(a) / M[1][1]), sp.simplify(EL(ph) / S)]
    # frw_point against the coordinate computation
    sub = {sp.Derivative(a, (t, 2)): (Hd + H ** 2) * a, sp.Derivative(a, t): H * a,
           sp.Derivative(ph, (t, 2)): pdd, sp.Derivative(ph, t): pd}
    Rf, Hff = frw_point()
    okR = all(sp.simplify(R1[i][j][k][l].subs(sub) - Rf[i][j][k][l]) == 0
              for i, j, k, l in itertools.product(range(D), repeat=4))
    okH = all(sp.simplify((f1 * Hs1[i][j] + f2 * dph1[i] * dph1[j] * ETA[j]).subs(sub) - Hff[i][j]) == 0
              for i in range(D) for j in range(D))
    return dict(ratios=ratios, a=a, frw_ok=okR and okH)


def cosmology():
    """S3"""
    R, Hf = frw_point()
    xi = [x0, 1, 0, 0]
    X = sp.symbols("X0:4")
    PMg, PSg = symbol(xi, [[xi[a] * X[b] + xi[b] * X[a] for b in range(D)] for a in range(D)], 0, R, Hf, f1)
    tt = [[sp.Symbol("t%d%d" % (min(a, b), max(a, b))) for b in range(D)] for a in range(D)]
    PM, PS = symbol(xi, tt, sp.Symbol("psi"), R, Hf, f1)
    xu = [xi[a] * ETA[a] for a in range(D)]
    o = dict(gauge=all(sp.expand(v) == 0 for r in PMg for v in r) and sp.expand(PSg) == 0,
             bianchi=all(sp.expand(sum(xu[a] * PM[a][b] for a in range(D))) == 0 for b in range(D)))
    o["einstein_null"] = null_only(char_poly(xi, R, [[0] * D for _ in range(D)], 0))
    cs = [(sp.factor(sp.solve(fac, x0 ** 2)[0]), mu) for fac, mu in cones(char_poly(xi, R, Hf, f1), f1)]
    fdd = f1 * pdd + f2 * pd ** 2
    cT = (1 + 8 * fdd) / (1 + 8 * H * f1 * pd)
    o["cones"] = cs
    o["tensor_ok"] = any(sp.simplify(c - cT) == 0 and mu == 2 for c, mu in cs)
    # Reall's eq. (91), beta = 8 f: C_mn = g_mn - 8 nabla_m nabla_n f; fronts null for C^{-1}
    Cl = [[ETA[a] * (1 if a == b else 0) - 8 * Hf[a][b] * ETA[b] for b in range(D)] for a in range(D)]
    Ci = sp.Matrix(Cl).inv()
    reall = sp.solve(sum(Ci[a, b] * xi[a] * xi[b] for a in range(D) for b in range(D)), x0 ** 2)
    o["reall_ok"] = len(reall) == 1 and sp.simplify(reall[0] - cT) == 0
    cS = [c for c, mu in cs if mu == 1]
    # exact solution points, V = 0, linear coupling (f2 = 0)
    M = metric_eq(R, Hf, [pd, 0, 0, 0], 0)
    S = sp.simplify(-pdd - 3 * H * pd + f1 * lgb(R))
    pts = {}
    for pv in (sp.Rational(12, 5), sp.Rational(-12, 5)):
        f1v = (pv ** 2 / 2 - 3) / (24 * pv)
        base = {H: 1, pd: pv, f1: f1v, f2: 0}
        s = sp.solve([M[1][1].subs(base), S.subs(base)], [Hd, pdd], dict=True)[0]
        vals = dict(base)
        vals.update({Hd: s[Hd], pdd: s[pdd]})
        pts[f1v] = dict(F=sp.simplify(M[0][0].subs(vals)), weak=8 * abs(f1v * pv), cT=sp.nsimplify(cT.subs(vals)),
                        cS=sp.nsimplify(cS[0].subs(vals)) if cS else None)
    o["points"] = pts
    return o


def wave():
    """S4: a plane wave (type N, profile diag(1, -1) eps) with phi constant"""
    lu = (1, 1, 0, 0)
    ll = [lu[a] * ETA[a] for a in range(D)]
    mi = {i: [1 if a == i else 0 for a in range(D)] for i in (2, 3)}
    Rl = [[[[0] * D for _ in range(D)] for _ in range(D)] for _ in range(D)]
    for i, w in ((2, 1), (3, -1)):
        for a, b, c, d in itertools.product(range(D), repeat=4):
            Rl[a][b][c][d] += eps * w * (ll[a] * mi[i][b] - mi[i][a] * ll[b]) * (ll[c] * mi[i][d] - mi[i][c] * ll[d])
    R = [[[[Rl[a][b][c][d] * ETA[c] * ETA[d] for d in range(D)] for c in range(D)] for b in range(D)] for a in range(D)]
    Z = [[0] * D for _ in range(D)]
    M = metric_eq(R, Z, [0] * D, 0)
    o = dict(solves=all(v == 0 for r in M for v in r), lgb=lgb(R))
    xg = [x0] + list(sp.symbols("k1:4"))
    PMp, _ = symbol(xg, Z, 1, R, Z, f1)
    o["self_adjoint"] = all(sp.simplify(symbol(xg, unit(a, b), 0, R, Z, f1)[1] + sum(
        ETA[c] * ETA[d] * PMp[c][d] * unit(a, b)[c][d] for c in range(D) for d in range(D)) / 2) == 0 for a, b in SYM)
    o["einstein_null"] = null_only(char_poly([x0, 0, 1, 0], R, Z, 0))
    res = {}
    for xi in ([x0, 0, 1, 0], [x0, 0, 1, 1]):
        Qp = char_poly(xi, R, Z, f1)
        n2 = sum(v ** 2 for v in xi[1:])
        quartic = [fac for fac, _ in cones(Qp, f1)]
        roots = sorted(sp.solve(quartic[0], x0 ** 2), key=str) if len(quartic) == 1 else []
        want = sorted([n2 / (1 - 8 * sp.sqrt(2) * f1 * eps), n2 / (1 + 8 * sp.sqrt(2) * f1 * eps)], key=str)
        res[tuple(xi[1:])] = dict(roots=roots, n2=n2,
                                  ok=len(roots) == 2 and all(any(sp.simplify(r - w) == 0 for r in roots) for w in want))
    o["dirs"] = res
    o["either_sign"] = {}
    for fe in (sp.Rational(1, 100), sp.Rational(-1, 100)):
        sp_ = [r.subs(f1 * eps, fe).subs(f1, fe / eps) for r in res[(0, 1, 0)]["roots"]]
        o["either_sign"][fe] = sorted((sp.radsimp(sp.simplify(v)) for v in sp_), key=float)
    return o


def compute():
    return dict(field=field_check(), cosmo=cosmology(), wave=wave())


def report(o):
    fc, c, w = o["field"], o["cosmo"], o["wave"]
    print("sgb_cone.py -- the light-cone test on four-dimensional scalar-Gauss-Bonnet (item 327)\n")
    print("S1 reduced-action / covariant equations: %s (f-independent); cosmology data %s" % (fc["ratios"],
                                                                                         fc["frw_ok"]))
    print("S2 symbol gauge-invariant %s, divergence-free %s; f' = 0: every front null (cosmology %s, wave %s)" % (
        c["gauge"], c["bianchi"], c["einstein_null"], w["einstein_null"]))
    print("S3 cosmology cones: %s" % "; ".join("c^2 = %s (x%d)" % (cc, mu) for cc, mu in c["cones"]))
    print("   tensor = (1 + 8 f..)/(1 + 8 H f.) %s; Reall's C = g - 8 nabla nabla f gives it %s" % (c["tensor_ok"],
                                                                                              c["reall_ok"]))
    for fv, p in c["points"].items():
        print("   f' = %s: Friedmann %s, 8|H f.| = %s, c_T^2 = %s (> 1: %s), c_S^2 = %s" % (
            fv, p["F"], p["weak"], p["cT"], p["cT"] > 1, p["cS"]))
    print("S4 plane wave with phi constant solves the theory %s (L_GB = %s); f' = 0 null %s" % (w["solves"], w["lgb"],
                                                                                              w["einstein_null"]))
    for d, r in w["dirs"].items():
        print("   direction %s: mixed fronts xi_0^2 = %s (|xi|^2/(1 -+ 8 sqrt 2 f' eps): %s)" % (d, r["roots"], r["ok"]))
    for fe, v in w["either_sign"].items():
        print("   f' eps = %s: xi_0^2 = %s -- one outside the light cone: %s" % (fe, v, any(x > 1 for x in v)))


def checks(o):
    fc, c, w = o["field"], o["cosmo"], o["wave"]
    res = []
    add = lambda n, ok: res.append((n, bool(ok)))
    rul = " ".join(open(RULINGS, encoding="utf-8").read().split())
    texts = all(all(x in " ".join(open(p, encoding="utf-8").read().split()) for x in ws) for p, ws in TEXTS.items())
    add("S0 item 327 verbatim in the rulings file; U6, currency.py's and doors.py's words in their files",
        all(x in rul for x in WORDS) and texts)
    a = fc["a"]
    add("S1 the covariant equations are the reduced action's, -a^3, -3a^2 and a^3 times, for every f",
        [sp.simplify(r) for r in fc["ratios"]] == [-a ** 3, -3 * a ** 2, a ** 3] and fc["frw_ok"])
    add("S2 the coupled symbol is gauge invariant, divergence-free and symmetric; with f' = 0 every front is null",
        c["gauge"] and c["bianchi"] and c["einstein_null"] and w["einstein_null"] and w["self_adjoint"])
    add("S3 cosmology: tensor fronts (1 + 8 f..)/(1 + 8 H f.) twice, Reall's eq. (91) with beta = 8 f",
        c["tensor_ok"] and c["reall_ok"] and len(c["cones"]) == 2)
    pts = c["points"]
    add("S3 exact weakly coupled solutions (V = 0, linear f): c_T^2 > 1 for f' of either sign",
        len(pts) == 2 and all(p["F"] == 0 and p["weak"] < 1 and p["cT"] > 1 for p in pts.values())
        and {sp.sign(k) for k in pts} == {1, -1})
    add("S4 a plane wave with phi constant solves the theory exactly for every f (L_GB = 0)",
        w["solves"] and w["lgb"] == 0)
    add("S4 mixed fronts at |xi|^2/(1 -+ 8 sqrt 2 f' eps): one outside the light cone for either sign of f'",
        all(r["ok"] for r in w["dirs"].values())
        and all(any(x > 1 for x in v) and any(x < 1 for x in v) for v in w["either_sign"].values()))
    return res


MUTANTS = {"gb_coeff": "the Gauss-Bonnet term's factor 2 in the metric equation read as 1 (S1)",
           "mix_drop": "the metric row's scalar mixing f' xi xi psi R dropped from the symbol (S2)",
           "frw_sign": "the cosmology's nabla_0 nabla^0 f given the wrong sign (S3)"}


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
        print("  mutant %-10s %-75s %s" % (kk, desc, "caught by " + ", ".join(failed) if failed else "NOT CAUGHT"))
    print("mutants: %d/%d caught" % (caught, len(MUTANTS)))
    return caught == len(MUTANTS)


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    if "--mutants" in sys.argv:
        sys.exit(0 if mutants() else 1)
    report(compute())
