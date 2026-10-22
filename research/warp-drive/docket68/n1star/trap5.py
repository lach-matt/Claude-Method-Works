#!/usr/bin/env python3
"""trap5.py -- the trapping input of [Hin26] Proposition 6.5 in five dimensions: strong trapping admissibility of the
gauge potential operator on Tangherlini, his Lemma 6.4 (N1STAR-PROOF.md section 10.17; ROUTES-OPEN.md 4.18; D59).
Labels: computed (exact, sympy), deduced, READ.

[Hin26] (arXiv:2606.28253v2) Proposition 6.5, mode stability of box^Ups at high energies, rests on [Hin26c] Theorem
9.16 and his Lemma 6.4: box^Ups is strongly trapping admissible ([Hin26c] Definition 5.8) -- for every eps > 0 there is
a stationary positive definite fiber inner product on pi^*(T^*), homogeneous of degree 0, with sigma^-1 (1/2i) (S_sub
- S_sub^*) < eps at the trapped set Gamma_0 ((6.14)).  E^Ups vanishes near the trapped set ((6.1)), so only the 1-form
wave operator box = 2 delta G delta* enters, and S_sub(box) = -i nabla_{H_G} ((6.13), [Hin17] Proposition 4.1).  His
proof: in the frame e_0 = zeta, e_1, e_2, e_3 of (6.15)-(6.16b), nabla_{H_G} = H_G + 2 sigma N with N nilpotent
((6.16c)), so a scaled inner product makes the skew part small.  Here the five-dimensional counterpart on Tangherlini,
f = 1 - mu/r^2, r_h = mu^(1/2), static chart, zeta = -sigma dt + xi dr + eta, G = g^-1(zeta, zeta), H_G = d_zeta G d_z
- d_z G d_zeta, C = r^2 |eta|^2_g (the S^3 Casimir; his Carter constant at a = 0).

  T0 (computed, exact) (6.13) in five dimensions: the full symbol of box = 2 delta G delta*, conjugated to half
     densities by |dg|, has principal part G Id and subprincipal part i Gam^c_ab d_{zeta_b} G, so S_sub(box) = -i H_G +
     sigma_sub = -i nabla^{pi^* T^*}_{H_G}.  Four-dimensional control: Schwarzschild, the same.  Control: the coordinate
     density dx in place of |dg|.
  T1 (computed, exact) The trapped set ([Hin26c] Definition 4.13: xi = H_G xi = 0 on the future characteristic set,
     r > r_h) is r^2 = 2 mu, where H_G xi = -(C/(f r^3))(r f' - 2 f) = (2 C/(f r^5))(r^2 - 2 mu) vanishes, its only
     zero in r > r_h; there sigma^2 = f C/r^2, so C = 4 mu sigma^2 > 0; the differentials of xi, H_G xi and G are
     independent ([Hin26c] Lemma 4.14); and under H = H_G/(H_G t) the normal expansion rate is nu = (2 mu)^(-1/2) =
     1/r_ph.  Four-dimensional control: r = 3 mu/2, nu = 2/(3^(3/2) mu) = 1/(3^(3/2) M).  Control: the
     four-dimensional ratio r_ph = (3/2) r_h claimed in five dimensions.
  T2 (computed, exact) H_G C = 0.  The frame e_0 = zeta, e_1 = r (zeta_(1) w^(0) + zeta_(0) w^(1)), e_2 = (r^2/2)
     (zeta_(0) w^(0) + zeta_(1) w^(1) - eta), w^(0) = f^(1/2) dt, w^(1) = f^(-1/2) dr, has on G = 0 the Gram matrix C
     [[0, 0, -1], [0, 1, 0], [-1, 0, 0]] ((6.16a) at a = 0, its first three rows), of determinant -C^3: for C > 0 it
     spans the (t, r) plane and eta, and its g-orthogonal complement V_perp is the angular covectors orthogonal to eta,
     on which g^-1 = r^-2 g_{S^3}^-1 is positive definite (rank 2; in four dimensions rank 1, e_3).  Control: off the
     characteristic set the Gram matrix is not C J (g^-1(e_0, e_0) = G).
  T3 (computed, exact) On G = 0: nabla_{H_G} e_0 = 0, nabla_{H_G} e_1 = -2 sigma e_0, nabla_{H_G} e_2 = -2 sigma e_1,
     in five dimensions.  Four-dimensional control: the same at a = 0, and e_3 = r (zeta_(3) w^(2) - zeta_(2) w^(3)) is
     parallel -- (6.16c) with e_1 -> -e_1, whose sign there is +2 sigma.  Control: e_1 without the weight r.
  T4 (computed, exact) With N e_1 = e_0, N e_2 = e_1, on span{e_0, e_1, e_2}/C^(1/2): sigma^-1 (1/2i) (S_sub -
     S_sub^*) = N + N^* there, whose norm for the inner product diag(1, eta^-1, eta^-2) is 2^(1/2) eta^(1/2), and for
     diag(1, eta^-2, eta^-4) 2^(1/2) eta (his "O(eta)").  Control: a diagonal entry 1/2 in N, as a connection that is
     not nilpotent would give, where the norm does not tend to 0.

Deduced, not computed here: span{e_0, e_1, e_2} is nabla_{H_G}-invariant (T3), so is its g-orthogonal complement
V_perp (nabla is metric), on which g is positive and parallel and the skew part vanishes; with diag(1, eta^-1,
eta^-2) on the first and g on V_perp, (6.14) holds with eps = 2^(1/2) eta^(1/2) at Gamma_0, where C > 0 (T1): box^Ups
is strongly trapping admissible on five-dimensional Tangherlini when E^Ups vanishes near r^2 = 2 mu ((6.1)), his Lemma
6.4 there.  The flow on Gamma_0 is the geodesic flow of the round S^3, periodic, and transversally hyperbolic at the
rate nu (T1), the r-normal hyperbolicity of [Hin26c] Proposition 4.19.  Not deduced: [Hin26c] Theorem 9.16 in five
dimensions ([Hin26c] works "in 3 + 1 dimensions for concreteness", Remark 5.6), and so his Proposition 6.5 there.

READ.  [Hin26] pp. 113-116 (section 6, (6.1)-(6.3), Lemma 6.1, Remark 6.2, Lemma 6.3; section 6.1: (6.12)-(6.16c),
Lemma 6.4 and its proof, Proposition 6.5); [Hin26c] (arXiv:2606.28008v1) pp. 88 (Definition 4.13, Lemma 4.14), 90-91
(Proposition 4.19), 101-103 (Example 5.4, Remark 5.6, section 5.1.1, Definition 5.8, Remark 5.9), 265 (strong trapping
admissibility of box used in the high-frequency control); alphaXiv, 2026-10-22.

sympy.  python3 trap5.py [--selftest | --mutants]   (--verbose lists every sub-check)
"""
import sys
import time

import sympy as sp

import gaugepot5 as G
from damping5 import Checklist
from modes5 import canon

D = sp.diff
mu = G.mu


def phase(n):
    """the static chart with covector coordinates z_a, G, H_G and the pullback connection along H_G"""
    C = G.ch(n, "static")
    X, gi, Gam, N = C["X"], C["gi"], C["Gam"], C["N"]
    z = sp.symbols("z0:%d" % N)
    Gf = sum(gi[a, a]*z[a]**2 for a in range(N))

    def H(u):
        return sum(D(Gf, z[a])*D(u, X[a]) - D(Gf, X[a])*D(u, z[a]) for a in range(N))

    def nab(u):
        return [H(u[a]) - sum(Gam[c][a][b]*D(Gf, z[b])*u[c] for b in range(N) for c in range(N)) for a in range(N)]

    Gn = sp.expand(sp.numer(sp.together(Gf)))
    th = C["ang"][0]

    def onG(e):
        """e on the characteristic set G = 0: its numerator reduced mod G in zeta_t, trig canonicalised"""
        return canon(sp.rem(sp.expand(sp.numer(sp.together(sp.expand(e)))), Gn, z[0]), th)

    return dict(C=C, z=z, Gf=Gf, H=H, nab=nab, onG=onG, th=th)


def frame(Pd, weight=True):
    C, z = Pd["C"], Pd["z"]
    r, f, N = C["r"], C["f"], C["N"]
    w = r if weight else 1
    e0 = list(z)
    e1 = [w*f*z[1], w*z[0]/f] + [0]*(N - 2)
    e2 = [r**2/2*z[0], r**2/2*z[1]] + [-r**2/2*z[a] for a in range(2, N)]
    return e0, e1, e2


# ------------------------------------------------------------------------------------------------- T0
def t0(control=0, verbose=False):
    chk = Checklist(verbose, quiet=control != 0)
    for n in ((4,) if control else (4, 3)):
        Pd = phase(n)
        C, z, Gf, th = Pd["C"], Pd["z"], Pd["Gf"], Pd["th"]
        X, Gam, N = C["X"], C["Gam"], C["N"]
        m = 1 if control == 1 else C["vol"]
        v = [sp.Function("v%d" % a)(*X) for a in range(N)]
        B = G.box(C, [m**sp.Rational(-1, 2)*x for x in v])
        P = [sp.expand(m**sp.Rational(1, 2)*b) for b in B]
        bad = 0
        for a in range(N):
            for c in range(N):
                p2 = sum(P[a].coeff(D(v[c], X[j], X[k]) if j != k else D(v[c], X[j], 2))*(sp.I*z[j])*(sp.I*z[k])
                         * (1 if j == k else sp.Rational(1, 2)) for j in range(N) for k in range(N))
                p1 = sum(P[a].coeff(D(v[c], X[j]))*(sp.I*z[j]) for j in range(N))
                sub = p1 - sum(D(D(p2, X[j]), z[j]) for j in range(N))/(2*sp.I)
                tgt = sp.I*sum(Gam[c][a][b]*D(Gf, z[b]) for b in range(N))
                bad += canon(p2 - (Gf if a == c else 0), th) != 0 or canon(sub - tgt, th) != 0
        chk(f"n + 1 = {n + 1}: box = 2 delta G delta* on half densities by |dg|: principal part G Id, subprincipal part "
            f"i Gam^c_ab d_zeta_b G, so S_sub = -i nabla_(H_G)", bad == 0)
    return chk.ok


# ------------------------------------------------------------------------------------------------- T1
def t1(control=0, verbose=False):
    chk = Checklist(verbose, quiet=control != 0)
    sg, Cc, xi = sp.symbols("sigma C xi", positive=True)
    for n in ((4,) if control else (4, 3)):
        C = G.ch(n, "static")
        r, f = C["r"], C["f"]
        Gr = -sg**2/f + f*xi**2 + Cc/r**2
        Hxi = -D(Gr, r)
        Ht = 2*sg/f
        rph = sp.sqrt(2*mu) if n == 4 else 3*mu/2
        if control == 1:
            rph = sp.Rational(3, 2)*sp.sqrt(mu)
        on = {Cc: sp.factor(r**2*sg**2/f)}
        hx = sp.factor(Hxi.subs(xi, 0).subs(on))
        roots = [x for x in sp.solve(sp.numer(sp.together(hx)), r) if x.is_positive]
        ok_set = sp.simplify(hx.subs(r, rph)) == 0 and len(roots) == 1
        Cph = sp.simplify(on[Cc].subs(r, rph))
        J = sp.Matrix([[D(e, x) for x in (r, xi, sg)] for e in (xi, Hxi, Gr)])
        det = sp.simplify(J.subs({xi: 0}).subs(Cc, Cph).subs(r, rph).det())
        A = sp.Matrix([[D(f**2*xi/sg, r), D(f**2*xi/sg, xi)], [D(Hxi/Ht, r), D(Hxi/Ht, xi)]])
        A = A.subs({xi: 0}).subs(Cc, Cph).subs(r, rph)
        nu = sp.sqrt(sp.simplify(A[0, 1]*A[1, 0]))
        want = 1/sp.sqrt(2*mu) if n == 4 else 2/(3*sp.sqrt(3)*mu)
        chk(f"n + 1 = {n + 1}: xi = H_G xi = 0 on G = 0, r > r_h, only at r_ph = {rph}; C = {Cph} > 0; the "
            f"differentials of xi, H_G xi, G independent (det {det}); nu = {sp.simplify(nu)}",
            ok_set and Cph.is_positive and det != 0 and sp.simplify(nu - want) == 0)
    return chk.ok


# ------------------------------------------------------------------------------------------------- T2
def t2(control=0, verbose=False):
    chk = Checklist(verbose, quiet=control != 0)
    for n in ((4,) if control else (4, 3)):
        Pd = phase(n)
        C, z, H, onG, th = Pd["C"], Pd["z"], Pd["H"], Pd["onG"], Pd["th"]
        gi, N, r = C["gi"], C["N"], C["r"]
        Cc = sum(r**2*gi[a, a]*z[a]**2 for a in range(2, N))
        E = frame(Pd)
        red = (lambda e: canon(e, th)) if control == 1 else onG
        J = [[0, 0, -1], [0, 1, 0], [-1, 0, 0]]
        gram = all(red(sum(gi[a, a]*E[i][a]*E[j][a] for a in range(N)) - Cc*J[i][j]) == 0
                   for i in range(3) for j in range(3))
        chk(f"n + 1 = {n + 1}: H_G C = 0, and on G = 0 the Gram matrix of (e_0, e_1, e_2) is C J ((6.16a) at a = 0)",
            canon(H(Cc), th) == 0 and gram)
        if control:
            continue
        y = sp.symbols("y0:%d" % (N - 2))                 # an angular covector orthogonal to eta
        vv = [0, 0] + list(y)
        orth = [sp.expand(sum(gi[a, a]*vv[a]*E[i][a] for a in range(N))) for i in range(3)]
        cond = sp.expand(sum(gi[a, a]*vv[a]*z[a] for a in range(2, N)))
        same = all(sp.simplify(o - k*cond) == 0 for o, k in zip(orth, (1, 0, -r**2/2)))
        chk(f"n + 1 = {n + 1}: an angular covector is g-orthogonal to e_0, e_1, e_2 iff it is orthogonal to eta, and "
            f"g^-1 = r^-2 g_S^-1 > 0 there; det(C J) = -C^3", same and sp.Matrix(J).det() == -1)
    return chk.ok


# ------------------------------------------------------------------------------------------------- T3
def t3(control=0, verbose=False):
    chk = Checklist(verbose, quiet=control != 0)
    for n in ((4,) if control else (4, 3)):
        Pd = phase(n)
        C, z, nab, onG = Pd["C"], Pd["z"], Pd["nab"], Pd["onG"]
        r, N, th = C["r"], C["N"], Pd["th"]
        e0, e1, e2 = frame(Pd, weight=control != 1)
        sig = -z[0]
        rows = [(e0, [0]*N), (e1, [-2*sig*x for x in e0]), (e2, [-2*sig*x for x in e1])]
        ok = all(onG(nab(e)[a] - t[a]) == 0 for e, t in rows for a in range(N))
        chk(f"n + 1 = {n + 1}: on G = 0, nabla_(H_G) e_0 = 0, nabla e_1 = -2 sigma e_0, nabla e_2 = -2 sigma e_1", ok)
        if n == 3 and not control:
            e3 = [0, 0, r*z[3]/sp.sin(th), -r*z[2]*sp.sin(th)]
            chk("n + 1 = 4: e_3 = r (zeta_(3) w^(2) - zeta_(2) w^(3)) is parallel, nabla_(H_G) e_3 = 0",
                all(onG(x) == 0 for x in nab(e3)))
    return chk.ok


# ------------------------------------------------------------------------------------------------- T4
def t4(control=0, verbose=False):
    chk = Checklist(verbose, quiet=control != 0)
    eta = sp.Symbol("eta", positive=True)
    Nm = sp.Matrix([[0, 1, 0], [0, 0, 1], [0, 0, 0]])
    if control == 1:
        Nm = Nm + sp.diag(0, sp.Rational(1, 2), 0)
    for powers, want in (((0, -1, -2), sp.sqrt(2)*sp.sqrt(eta)), ((0, -2, -4), sp.sqrt(2)*eta)):
        B = sp.diag(*[eta**p for p in powers])
        Bh = sp.diag(*[eta**sp.Rational(p, 2) for p in powers])
        Sym = Bh*(Nm + B.inv()*Nm.T*B)*Bh.inv()
        ev = [sp.simplify(x) for x in Sym.eigenvals()]
        norm = sp.Max(*[sp.Abs(x) for x in ev])
        chk(f"inner product diag(1, eta^{powers[1]}, eta^{powers[2]}): |N + N^*| = {want}",
            sp.simplify(norm - want) == 0)
    return chk.ok


CHECKS = [("T0 (6.13) in five dimensions: S_sub(box) = -i nabla_(H_G), from the full symbol (four-dimensional control)",
           t0, 1),
          ("T1 the trapped set r^2 = 2 mu, C = 4 mu sigma^2 > 0, codimension 2, nu = 1/r_ph (four-dimensional control)",
           t1, 1),
          ("T2 H_G C = 0; the frame's Gram matrix C J on G = 0; its complement the angular covectors orthogonal to eta",
           t2, 1),
          ("T3 nabla_(H_G) is nilpotent on span{e_0, e_1, e_2}: 0, -2 sigma e_0, -2 sigma e_1 ((6.16c) at a = 0)",
           t3, 1),
          ("T4 the skew part N + N^* has norm 2^(1/2) eta^(1/2) for diag(1, eta^-1, eta^-2), 2^(1/2) eta for squares",
           t4, 1)]


def selftest(verbose=False):
    ok_all = True
    for name, fn, nc in CHECKS:
        t0_ = time.time()
        good = fn(verbose=verbose)
        control = any(fn(control=k) for k in range(1, nc + 1))
        state = "PASS" if good and not control else "FAIL"
        ok_all &= state == "PASS"
        print(f"{name:<112} {state}  {time.time() - t0_:.0f}s" + ("" if not control else "  (control passed: vacuous)"),
              flush=True)
    print(f"trap5.py: {len(CHECKS) if ok_all else 'FAILED'}/{len(CHECKS)}")
    return ok_all


def mutants():
    caught = total = 0
    for name, fn, nc in CHECKS:
        for k in range(1, nc + 1):
            total += 1
            res = fn(control=k)
            caught += (not res)
            print(f"mutant {k} of {name[:2]}: {'caught' if not res else 'NOT caught'}", flush=True)
    print(f"trap5.py mutants: {caught}/{total}")
    return caught == total


if __name__ == "__main__":
    args = sys.argv[1:]
    if "--mutants" in args:
        sys.exit(0 if mutants() else 1)
    sys.exit(0 if selftest(verbose="--verbose" in args) else 1)
