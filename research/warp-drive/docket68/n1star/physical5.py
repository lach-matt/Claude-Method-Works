#!/usr/bin/env python3
"""physical5.py -- [Hin26] section 8.5 in five dimensions: the physical large zero energy states (his Proposition 8.14)
and the pairings that make their construction smooth in the rotation (his Lemma 8.15) (N1STAR-PROOF.md section 10.34;
ROUTES-OPEN.md 4.35; D91).  Labels: computed (exact, sympy; numerical, mpmath, where said), deduced, READ.

[Hin26] (arXiv:2606.28253v2) section 8.5 (pp. 158-163): of the roots of L-hat_b(0) with real part in [-3, 0], "the only
exceptional indicial roots are the sl and vl roots -l for l >= 2. They are not related to pure gauge states"; his
Proposition 8.14 constructs, for b near b_0, large zero energy states h^(-2)_b,s2(S), h^(-2)_b,v2(V) with generalized
companions h-breve^(-2),1, and h^(-3)_b,s3(S), h^(-3)_b,v3(V), in ker D Ric and in the gauge, their rho^-l leading terms
spanning ker N(L-bar(0), -l); his Lemma 8.15 gives the pairings of L-hat_b(0) h-breve^2_b,s1(S) and of L-hat_b(0)
h-breve^1_b,v1(V) with the dual states, through which his Steps 1-3 remove the cokernel obstruction smoothly in b. In
five dimensions 10.24 found the physical roots -l and l + 2 at every type, the tensor type included (which four
dimensions lacks), and 10.33 the stationary solutions on Tangherlini harmonic by harmonic.

  Y1 (computed, exact) The stationary equations of 10.33, in z = r^2/mu, are Gauss's hypergeometric equation z (1 - z)
     w'' + (c - (a + b + 1) z) w' - a b w = 0: the tensor type's H with (a, b, c) = (-l/2, 1 + l/2, 1); the vector
     type's y = F_t/r with ((1 - l)/2, (l + 3)/2, 3); the scalar type's Y, from [KI03]'s flow, as Y = z^(1/2) (z - 1)^-1
     w with (-l/2, 1 + l/2, 2) -- l symbolic.  Control: the tensor type with c = 2.
  Y2 (computed, exact and numerical) The solutions smooth at the horizon z = 1: H_l = F(-l/2, 1 + l/2; 1; 1 - z), y_l =
     (1 - z) F((l + 5)/2, (3 - l)/2; 2; 1 - z) and Y_l = z^(1/2) F(2 + l/2, 1 - l/2; 2; 1 - z), F = 2F1; for l = 2, ...,
     8 the terminating ones (H at even l, y at odd l, Y at even l) solve 10.33's operators exactly, their 2F1 factors
     polynomials of degrees l/2, (l - 3)/2 and l/2 - 1 in z with nonzero top coefficients, and every one, at 40 digits,
     solves them at sample radii and grows like r^l, r^(l-1) and r^(l-1) with the coefficients Gamma(l + 1)/Gamma(1 +
     l/2)^2, -Gamma(l + 1)/(Gamma((l + 5)/2) Gamma((l + 1)/2)) and Gamma(l + 1)/(Gamma(2 + l/2) Gamma(1 + l/2)),
     nonzero.  Control: the tensor solution with c = 2.
  Y3 (computed, numerical, 50 digits, at Proposition 10.9's point) From lin5.py's factors of det N_L: at sl, vl and tl,
     l = 2, 3, -l is a root and -l - 1 is not, the nearest root to it at distance 1; -l is simple, the nearest other
     root at sl box^Ups's class root mu_l,1 + 1 = -l - (l + 2) z/(2 (l + 1)(2 l + 3)) + O(z^2) (10.30(ii); z = 4 e_U
     gam_U^2 = 4 x 10^-6), real and below -l by 3.81 x 10^-7 (l = 2) and 2.78 x 10^-7 (l = 3), its first-order term
     matched to 10^-3 (D91 printed 3.3 x 10^-7, section 10.24's s1 pair; D92).  Control: -l in place of -l - 1.
  Y4 (computed, exact) The rotation equivariance behind his Remark 8.10 in five dimensions: on 4+1 Minkowski, with h_A =
     (mu/R^4)(dt (x) w_A + w_A (x) dt) and w_A = x . A dx for A in so(4) (10.28(v)), the Lie derivative along R = B x is
     L_R h_A = h_[A,B], for every pair of the six basis rotations; the form B(V, V') = <[A_V, A_b], A_V'> on so(4) at
     A_b = e_12 is antisymmetric, of rank 4, with kernel spanned by e_12 and e_34, and <[X, Y], Z> = <X, [Y, Z]>; in
     three dimensions it is his triple product <a(V), a(b) x a(V')> up to sign.  Control: h_[B,A] for h_[A,B].

Deduced, not computed here (N1STAR-PROOF.md 10.34): [Hin26] Proposition 8.14 in five dimensions -- at a = 0 for every l
>= 2 and each of the three types, the state's leading term that of Y2's solution put into the gauge, and near a = 0 for
his l = 2, 3 by his Steps 0-5 with 10.33's Corollary 8.13 -- and his Lemma 8.15 there: (1) the s1 pairings minus 10.32's
centre-of-mass row, (2) the v1 pairings one half of 10.32's rotation row at the commutator, -pi^2 mu <[A_V, A_b], A_V'>,
0 at a = 0.

READ.  [Hin26] pp. 125 ((6.29)), 140-142 (section 7.2.1: Proposition 7.4, Lemma 7.5), 154-163 (Proposition 8.9, Remark
8.10, (8.21), Proposition 8.11, Lemma 8.12, Corollary 8.13, section 8.5: Proposition 8.14, Lemma 8.15, their proofs,
(8.27)-(8.37)), 176 (Definition 9.10); alphaXiv, 2026-10-24.  [DLMF] (https://dlmf.nist.gov/, 2026-10-24) 15.8.2, 15.8.8
(the connection formulas at large argument, b - a an integer included) and 15.10.1 (the exponent pairs).

sympy, mpmath.  python3 physical5.py [--selftest | --mutants]   (--verbose lists every sub-check)
"""
import sys
import time

import mpmath as mpm
import sympy as sp

from damping5 import Checklist

r, mu, z = sp.symbols("r mu z", positive=True)
l = sp.Symbol("l", positive=True)
f = 1 - mu / r**2


def tensor_op(u, lv=l):
    return sp.diff(r**3 * f * sp.diff(u, r), r) / r**3 - lv * (lv + 2) * u / r**2


def vector_op(u, lv=l):
    return sp.diff(r**5 * sp.diff(u, r), r) - (lv * (lv + 2) - 3) * r**3 * u / f


def scalar_op(Y, lv=l):
    """[KI03]'s static flow (static5.py S3) with X eliminated: X = Y + r (r^2 - mu) Y'/mu"""
    k2 = lv * (lv + 2)
    X = Y + r * (r**2 - mu) * sp.diff(Y, r) / mu
    Xp = (mu * (mu - 2 * r**2) * X + (k2 * r**2 * (r**2 - mu) + 4 * mu * r**2 - 3 * r**4) * Y) / (mu * r * (r**2 - mu))
    return sp.diff(X, r) - Xp


def in_z(op, pref):
    """op on U(r) = pref(z) w(z), z = r^2/mu, as w'' + P w' + Q w (P, Q returned)"""
    w = sp.Function("w")(z)
    e = op((pref * w).subs(z, r**2 / mu))
    e = sp.simplify(e.subs(r, sp.sqrt(mu * z)))
    W2, W1, W0 = sp.symbols("W2 W1 W0")
    e = sp.expand(sp.simplify(e.subs(sp.Derivative(w, (z, 2)), W2).subs(sp.Derivative(w, z), W1).subs(w, W0)))
    c2 = e.coeff(W2)
    return [sp.factor(sp.simplify(e.coeff(v) / c2)) for v in (W1, W0)]


def is_hyp(P, Q, a, b, c):
    return sp.simplify(P - (c - (a + b + 1) * z) / (z * (1 - z))) == 0 and sp.simplify(Q + a * b / (z * (1 - z))) == 0


# ------------------------------------------------------------------------------------------------- Y1
def y1(control=0, verbose=False):
    chk = Checklist(verbose, quiet=control != 0)
    ct = 1 if control != 1 else 2
    okT = is_hyp(*in_z(tensor_op, 1), -l / 2, 1 + l / 2, ct)
    chk(f"tensor: H solves the hypergeometric equation with (a, b, c) = (-l/2, 1 + l/2, {ct})", okT)
    if control == 0:
        okV = is_hyp(*in_z(vector_op, 1), (1 - l) / 2, (l + 3) / 2, 3)
        okS = is_hyp(*in_z(scalar_op, sp.sqrt(z) / (z - 1)), -l / 2, 1 + l / 2, 2)
        chk("vector: y with ((1 - l)/2, (l + 3)/2, 3); scalar: Y = z^(1/2) (z - 1)^-1 w with (-l/2, 1 + l/2, 2)",
            okV and okS)
    return chk.ok


# ------------------------------------------------------------------------------------------------- Y2
SOL = {   # (prefactor in z, A, B, C, operator, growth exponent of z, the growing coefficient)
    "tensor": (lambda L: 1, lambda L: -sp.S(L) / 2, lambda L: 1 + sp.S(L) / 2, lambda L: 1, tensor_op,
               lambda L: sp.S(L) / 2, lambda L: sp.gamma(L + 1) / sp.gamma(1 + sp.S(L) / 2)**2),
    "vector": (lambda L: 1 - z, lambda L: (sp.S(L) + 5) / 2, lambda L: (3 - sp.S(L)) / 2, lambda L: 2, vector_op,
               lambda L: (sp.S(L) - 1) / 2,
               lambda L: -sp.gamma(L + 1) / (sp.gamma((sp.S(L) + 5) / 2) * sp.gamma((sp.S(L) + 1) / 2))),
    "scalar": (lambda L: sp.sqrt(z), lambda L: 2 + sp.S(L) / 2, lambda L: 1 - sp.S(L) / 2, lambda L: 2,
               scalar_op, lambda L: (sp.S(L) - 1) / 2,
               lambda L: sp.gamma(L + 1) / (sp.gamma(2 + sp.S(L) / 2) * sp.gamma(1 + sp.S(L) / 2))),
}

PREFN = {"tensor": lambda zz: 1, "vector": lambda zz: 1 - zz, "scalar": lambda zz: mpm.sqrt(zz)}


def y2(control=0, verbose=False):
    chk = Checklist(verbose, quiet=control != 0)
    mpm.mp.dps = 40
    exact_ok, num_ok, notes = True, True, []
    types = ["tensor", "vector", "scalar"] if control == 0 else ["tensor"]
    for typ in types:
        pref, A, B, C, op, gexp, gcoef = SOL[typ]
        for L in range(2, 9):
            Cv = C(L) if not (control == 1 and typ == "tensor") else 2
            Fz = sp.hyper([A(L), B(L)], [Cv], 1 - z)
            poly = sp.hyperexpand(Fz)
            if poly.is_polynomial(z) and control == 0:            # terminating: exact
                U = sp.expand(pref(L) * poly)
                res = sp.simplify(op(U.subs(z, r**2 / mu), L))
                deg = sp.Poly(sp.expand(poly), z).degree()
                top = sp.Poly(sp.expand(poly), z).LC()
                want = {"tensor": L // 2, "vector": (L - 3) // 2, "scalar": L // 2 - 1}[typ]
                exact_ok &= res == 0 and deg == want and top != 0
                notes.append(f"{typ[0]}{L}: deg {deg}")
            # numerical: the static operator on the function at sample radii (mu = 1), and the growth at large z
            Am, Bm, Cm = (mpm.mpf(sp.Rational(q).p) / sp.Rational(q).q for q in (A(L), B(L), Cv))
            Ufun = lambda rv, typ=typ, Am=Am, Bm=Bm, Cm=Cm: PREFN[typ](rv**2) * mpm.hyp2f1(Am, Bm, Cm, 1 - rv**2)
            for rv in (mpm.mpf("1.3"), mpm.mpf("2.1"), mpm.mpf("5.7")):
                d0 = Ufun(rv)
                d1 = mpm.diff(Ufun, rv, 1)
                d2 = mpm.diff(Ufun, rv, 2)
                ff = 1 - 1 / rv**2
                if typ == "tensor":                              # (1/r^3)(r^3 f H')' = f H'' + (3 f/r + f') H'
                    res = ff * d2 + (3 * ff / rv + 2 / rv**3) * d1 - L * (L + 2) * d0 / rv**2
                elif typ == "vector":
                    res = 5 * rv**4 * d1 + rv**5 * d2 - (L * (L + 2) - 3) * rv**3 * d0 / ff
                else:
                    k2 = L * (L + 2)
                    X = d0 + rv * (rv**2 - 1) * d1
                    Xd = d1 + (3 * rv**2 - 1) * d1 + rv * (rv**2 - 1) * d2
                    res = Xd - ((1 - 2 * rv**2) * X + (k2 * rv**2 * (rv**2 - 1) + 4 * rv**2 - 3 * rv**4) * d0) / (
                        rv * (rv**2 - 1))
                num_ok &= abs(res) < mpm.mpf(10)**-25 * (1 + abs(d0) * rv**(2 * L))
            zz = mpm.mpf(10)**12
            ge = sp.Rational(gexp(L))
            val = Ufun(mpm.sqrt(zz)) / zz**(mpm.mpf(ge.p) / ge.q)
            want = mpm.mpf(sp.N(gcoef(L), 45))
            num_ok &= abs(val / want - 1) < mpm.mpf(10)**-5
    chk(f"the solutions smooth at z = 1 solve 10.33's operators: exactly where they terminate ({', '.join(notes)}), and "
        f"at 40 digits at r = 1.3, 2.1, 5.7 (mu = 1), l = 2, ..., 8", exact_ok and num_ok)
    if control == 0:
        lv = sp.Symbol("l", positive=True)
        coefs = [sp.simplify(SOL[t][6](lv)) for t in ("tensor", "vector", "scalar")]
        finite = all(c.subs(lv, L) not in (0, sp.zoo, sp.nan) for c in coefs for L in range(2, 40))
        chk(f"growing coefficients at infinity (z^(l/2), z^((l-1)/2), z^((l-1)/2)): {coefs}, nonzero for l = 2, ..., 39 "
            f"(Gamma has no zeros), and matched at z = 10^12", finite)
    return chk.ok


# ------------------------------------------------------------------------------------------------- Y3
def y3(control=0, verbose=False):
    chk = Checklist(verbose, quiet=control != 0)
    import lin5
    ok, rep = True, []
    pt = {str(k_): v_ for k_, v_ in lin5.POINT.items()}
    zz = float(4 * pt["eU"] * pt["gU"]**2)
    for typ in ("sl", "vl", "tl"):
        for L in (2, 3):
            rts, _ = lin5.roots_at_point(typ, L)
            target = -L - 1 if control != 1 else -L
            dist_target = min(abs(q - target) for q in rts)
            at_l = [q for q in rts if abs(q + L) < 1e-30]
            others = sorted(abs(q + L) for q in rts if abs(q + L) >= 1e-30)
            ok &= dist_target > 0.5 and len(at_l) == 1 and (others[0] > 1e-12)
            if typ == "sl":                                       # box^Ups's class root mu_l,1 + 1 (10.30(ii); D92)
                q = min((q for q in rts if abs(q + L) >= 1e-30), key=lambda q: abs(q + L))
                d1 = (L + 2) * zz / (2 * (L + 1) * (2 * L + 3))
                ok &= abs(q.imag) < 1e-30 and q.real < -L and abs(abs(q + L) - d1) < 1e-3 * d1
                rep.append(f"{typ[0]}{L}: nearest other {q.real:+.6e}, below -l by {abs(q + L):.3e} against "
                           f"(l + 2) z/(2 (l + 1)(2 l + 3)) = {d1:.3e}")
                continue
            rep.append(f"{typ[0]}{L}: nearest other {others[0]:.2e}")
    chk(f"-l a simple root and -l - 1 none at sl, vl, tl, l = 2, 3 ({'; '.join(rep)})", ok)
    return chk.ok


# ------------------------------------------------------------------------------------------------- Y4
def y4(control=0, verbose=False):
    chk = Checklist(verbose, quiet=control != 0)
    t = sp.Symbol("t")
    xs = sp.symbols("x1:5")
    X = [t] + list(xs)
    Rr = sp.sqrt(sum(q**2 for q in xs))

    def E(i, j):
        M = sp.zeros(4, 4)
        M[i, j], M[j, i] = 1, -1
        return M
    basis = [E(i, j) for i in range(4) for j in range(i + 1, 4)]

    def wform(A):
        return [0] + [sum(xs[i] * A[i, j] for i in range(4)) for j in range(4)]

    def hA(A):
        w = wform(A)
        return sp.Matrix(5, 5, lambda a, b: mu / Rr**4 * ((1 if a == 0 else 0) * w[b] + (1 if b == 0 else 0) * w[a]))

    def lie(B, h):
        R = [0] + [sum(B[i, j] * xs[j] for j in range(4)) for i in range(4)]
        return sp.Matrix(5, 5, lambda a, b: sp.simplify(sum(R[c] * sp.diff(h[a, b], X[c]) for c in range(5))
                                                         + sum(h[c, b] * sp.diff(R[c], X[a]) for c in range(5))
                                                         + sum(h[a, c] * sp.diff(R[c], X[b]) for c in range(5))))
    ok = True
    for A in basis:
        for B in basis:
            want = A * B - B * A if control != 1 else B * A - A * B
            ok &= all(sp.simplify(q) == 0 for q in (lie(B, hA(A)) - hA(want)))
    chk("L_R h_A = h_[A,B] for R = B x and every pair of the six basis rotations (his Remark 8.10's equivariance)", ok)
    if control == 0:
        ip = lambda P, Q: sp.Rational(1, 2) * sum(P[i, j] * Q[i, j] for i in range(4) for j in range(4))
        Ab = basis[0]                                                   # e_12
        Bm = sp.Matrix(6, 6, lambda i, j: ip(basis[i] * Ab - Ab * basis[i], basis[j]))
        ker = Bm.nullspace()
        kernel_planes = sorted(max(range(6), key=lambda i, v=v: abs(v[i])) for v in ker)
        inv = all(ip(P * Q - Q * P, S) == ip(P, Q * S - S * Q) for P in basis for Q in basis for S in basis)
        # three dimensions: so(3) with the same construction is the triple product <a(V), a(b) x a(V')> up to sign
        def E3(i, j):
            M = sp.zeros(3, 3)
            M[i, j], M[j, i] = 1, -1
            return M
        b3 = [E3(1, 2), E3(2, 0), E3(0, 1)]                              # a(V) = e_1, e_2, e_3
        ip3 = lambda P, Q: sp.Rational(1, 2) * sum(P[i, j] * Q[i, j] for i in range(3) for j in range(3))
        ab = b3[2]
        B3 = sp.Matrix(3, 3, lambda i, j: ip3(b3[i] * ab - ab * b3[i], b3[j]))
        e = sp.eye(3)
        T3 = sp.Matrix(3, 3, lambda i, j: e[:, i].dot(e[:, 2].cross(e[:, j])))
        tri = B3 == T3 or B3 == -T3
        chk(f"B(V, V') = <[A_V, e_12], A_V'> on so(4): antisymmetric {Bm == -Bm.T}, rank {Bm.rank()}, kernel at the "
            f"planes {kernel_planes} (12 and 34 in the order 12, 13, 14, 23, 24, 34); <[X, Y], Z> = <X, [Y, Z]>; in "
            f"three dimensions the triple product ({tri})",
            Bm == -Bm.T and Bm.rank() == 4 and kernel_planes == [0, 5] and inv and tri)
    return chk.ok


CHECKS = [("Y1 the stationary equations of 10.33 are hypergeometric in z = r^2/mu, l symbolic", y1, 1),
          ("Y2 the solutions smooth at the horizon, exact where they terminate, and their growth at infinity", y2, 1),
          ("Y3 lin5.py's roots: -l simple and -l - 1 no root at sl, vl, tl, l = 2, 3 (his Step 4)", y3, 1),
          ("Y4 L_R h_A = h_[A,B]; the form <[A_V, A_b], A_V'> on so(4): rank 4; three dimensions his triple product",
           y4, 1)]


def selftest(verbose=False):
    ok_all = True
    for name, fn, nc in CHECKS:
        t0 = time.time()
        good = fn(verbose=verbose)
        control = any(fn(control=k) for k in range(1, nc + 1))
        state = "PASS" if good and not control else "FAIL"
        ok_all &= state == "PASS"
        print(f"{name:<112} {state}  {time.time() - t0:.0f}s" + ("" if not control else "  (control passed: vacuous)"),
              flush=True)
    print(f"physical5.py: {len(CHECKS) if ok_all else 'FAILED'}/{len(CHECKS)}")
    return ok_all


def mutants():
    caught = total = 0
    for name, fn, nc in CHECKS:
        for k in range(1, nc + 1):
            total += 1
            res = fn(control=k)
            caught += (not res)
            print(f"mutant {k} of {name[:2]}: {'caught' if not res else 'NOT caught'}", flush=True)
    print(f"physical5.py mutants: {caught}/{total}")
    return caught == total


if __name__ == "__main__":
    args = sys.argv[1:]
    if "--mutants" in args:
        sys.exit(0 if mutants() else 1)
    if "--only" in args:
        k = int(args[args.index("--only") + 1])
        name, fn, _ = CHECKS[k - 1]
        print(name, fn(verbose=True))
        sys.exit(0)
    sys.exit(0 if selftest(verbose="--verbose" in args) else 1)
