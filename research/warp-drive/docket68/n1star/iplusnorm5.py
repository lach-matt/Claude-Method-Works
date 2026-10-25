#!/usr/bin/env python3
"""iplusnorm5.py -- [Hin26c] sections 10, 11 and 13.2 at n = 4: every numeral of the iota+ normal operator's analysis
that the dimension sets, computed at n = 3 against the printed value and at n = 4 (N1STAR-PROOF.md 10.75 (lx); D166).
Labels: computed (exact, sympy).

[Hin26c] (Hintz, arXiv:2606.28008) proves Theorem 10.1 in 3 + 1 dimensions through the iota+ normal operator N^0 of
(10.6)-(10.7) on [0, oo]_R x S^2, with R = r/t*, tau = 1/t*.  The dimension enters it through (5.1a)'s constant, which
is (n - 1)/2 =: c, and through the densities; the radial point thresholds are sums of these.  Operators x^a p(X), X =
x d_x, are composed exactly, with adjoints for the density x^m |dx/x| given by (x^a p(X))* = x^a p-bar(-X - a - m).

  N1 (computed, exact) (10.6)-(10.7): t*^2 times Minkowski's -box on R^(1+n), on r^b t*^(-a-b) = tau^a R^b, equals
     -2 R^-1 (tau d_tau + R d_R)(R d_R + c) + R^-2 P^(0)(0, omega, -R d_R) with c = (n - 1)/2 and P^(0)(rho d_rho) =
     -(rho d_rho)^2 + (n - 2) rho d_rho; and (10.7)'s second line in x_I = R^-(1/2) is the same operator.  c = 1 at n
     = 3 (his "1 + S"), 3/2 at n = 4.
  N2 (computed, exact) (10.25): Q_0 = Im d_sigma N^0(P_0, 0) for |dx_I/x_I dgslash| is -x_I^2 (2c + 1 + 2 Re S) =
     -x_I^2 (n + 2 Re S): his -x_I^2 (3 + 2 Re S), and -x_I^2 (4 + 2 Re S) at n = 4.
  N3 (computed, exact) (10.27) at R_(I+,+1,in): the symbol of h Im of -(1/2) x_I^2 X (X - 2(c + S)) is x_I^2 (c + 1 +
     Re S) xi, his x_I^2 (2 + Re S) xi; with Q_0 it is x_I^2 ((c + 1) xi - (2c + 1) + Re S (xi - 2)), his "2 xi - 3 +
     (Re S)(xi - 2)", equal to x_I^2 at xi = 2 at every n; Q_1's symbol is x_I^2 xi; so the total -4(gam_I + h^-1 Im
     z) and the condition Im sigma > -gam_I are free of n.
  N4 (computed, exact) (1.2.2) at R_(I+,out): (4 gam_I + 2) - 4(c + Re S) - 2 < 0, i.e. gam_I < c + Re S: his 1 + Re
     S, and 3/2 + Re S at n = 4.
  N5 (computed, exact, but for the parenthesis's arithmetic) the densities: |dt dx| = R^n tau^-(n+1) |dtau/tau dR/R
     domega| = 2 x_I^-2n tau^-(n+1) |dtau/tau dx_I/x_I domega|, so -Im sigma = alpha~_+ + (n + 1)/2, gam_cf = alpha~_K -
     alpha~_+ - n/2 (his + 2 and - 3/2) and gam_I = alpha_I + n/2, gam_+ = alpha_+ + (n + 1)/2 (his 3/2 and 2, section
     10.3); section 11's mu_b = rho_I^n rho_+^(n+1) rho_K |dt dx| = |dt dx|/(t* r^n) with (11.4)'s functions, a b-density
     (his rho_I^3 rho_+^4 rho_K = 1/(t* r^3)), so beta_I = alpha_I + n/2, beta_+ = alpha_+ + (n + 1)/2, the K+ shift 1/2;
     section 13.2's mu_b = |dx|/|x|^n, L^2(mu) = rho^(n/2) L^2(mu_b) (that exponent, and -1/2 + n/2 = c below, arithmetic
     checked by hand, not computed; D172). The metric-density threshold alpha_I < -1/2 + S-bar ((10.2), Theorem 11.1) is
     gam_I, beta_I < c + S-bar at every n: his 1 + S-bar in Proposition 10.6, (11.5), Corollary 13.17 and Proposition
     13.18.
  N6 (computed, exact) (1.3.1) at R_(cf,+1,in): the density correction of Im(h^2 R^-2 P^(0)) from R^n |dR/R| to |dR/R|
     is -n h-hat xi (his -3 h-hat xi); sigma(Q_0,h) = -h-hat (n + 2 Re S) (his 3), whose -2 Re S is vartheta_dK+,in's
     S part -(S + S^*) at his prefactor -xi/2 = 1 ((5.20) takes the whole imaginary part; Lemma 5.12's term 2 rho
     d_t* S); with gam_cf = -(alpha_+ + n/2) the total at xi = -2 is -4b - 4 alpha_+ - 2 + 2 vartheta at n = 3 and n =
     4, his printed sum: (10.28), b + alpha_+ > (1/2)(-1 + vartheta), unchanged (D172; D166 read the Re S as omitted).
  N7 (computed, exact) (1.3.2) at R_(cf,out): twice Im(2h D_R) is -2 h-hat and twice Im(-2(c + S) i R^-1 h) is -4 h-hat
     (c + Re S), so with gam_cf = -(alpha_+ + n/2) the total is 4b + 4 alpha_+ + 2 - 4 Re S at every n: negative iff b +
     alpha_+ < -1/2 + Re S, his threshold; his printed "+ 4 Re S" gives the opposite sign of Re S, a misprint.
  N8 (computed, exact) Lemma 10.10's Fourier step: N^1(P_0, sigma) = R^(i sigma) R^2 N^0(P_0, sigma) R^(-i sigma) is
     -2 d_v (v d_v + i sigma - c - S) + P^(0)(v d_v + i sigma) in v = 1/R; its Fourier transform, on F(v_+^lam) =
     Gamma(lam + 1)(-i rhat)^(-lam-1), is (10.40), 2i rhat(-rhat d_rhat + i sigma - (c + 1) - S) + P^(0)(-rhat d_rhat -
     1 + i sigma): his "i sigma - 2 - S", and i sigma - 5/2 - S at n = 4; and rhat^(1-i sigma), rho-hat = 1/rhat, turn it
     into N_tf(P_0, 1) = 2i rho-hat(rho-hat d_rho-hat - c - S) + rho-hat^2 P^(0)(rho-hat d_rho-hat), the shifts by 1
     being the one-dimensional Fourier transform's, free of n.
  N9 (computed, exact) the counts and shifts: the C(n, 2) rotation fields span T S^(n-1) (Lemma 10.7's V: 1 + 3 + 1
     = 5 at n = 3, 1 + 6 + 1 = 8 at n = 4); Lemma 10.9's right b-density shift dim(iota+) - 1 = n - 1 (2; 3) and
     indicial roots 2 i sigma, 2(c + S); Step 2's Euclidean density Rhat^n: (gam_cf + n/2, b - gam_cf - n/2) there is
     (gam_cf, b - gam_cf) in |dRhat/Rhat|, Corollary 9.39's (q, r) -> (q - 2, r + 1) returning (gam_cf - 2, b - gam_cf
     + 1) at every n, q = gam_cf + n/2 = -alpha_+; Remark 11.4's beta_- < -1 + S-bar + n/2 (his 1/2 + S-bar; 1 + S-bar).
     The span and the rank are computed; the counts, the shifts and the weights are arithmetic in n checked against
     print at n = 3, not computed (D172).

Mutants: N1 with c = 1 at n = 4; N2 with the density x_I |dx_I/x_I|; N3 with Q_0 at n = 3 beside the n = 4 symbol; N4
with c = 1 at n = 4; N5 with r^(n-2); N6 with gam_cf = -(alpha_+ + 3/2) at n = 4; N7 with c = 1 at n = 4; N8 with his
numeral 2 at n = 4; N9 with n - 1 rotation fields.
sympy.  python3 iplusnorm5.py [--selftest | --mutants]   (seconds)
"""
import itertools
import sys
import time

import sympy as sp

from damping5 import Checklist

X = sp.Symbol("X", real=True)                       # x d_x acting on the right
sr, si, sig, imz, gam, b, alp, th = sp.symbols("sr si sigma imz gamma b alpha_p vartheta", real=True)
xi, h = sp.symbols("xi h", positive=True)
S = sr + sp.I * si
I = sp.I


def cc(n):
    return sp.Rational(n - 1, 2)


# ------------------------------------------------------------------ operators sum_a x^a p_a(X), stored as {a: p_a}
def op(d):
    return {sp.nsimplify(a): sp.expand(p) for a, p in d.items() if sp.expand(p) != 0}


def mul(A, B):
    out = {}
    for a, p in A.items():
        for bb, q in B.items():
            out[a + bb] = out.get(a + bb, 0) + p.subs(X, X + bb) * q
    return op(out)


def add(*Ts):
    out = {}
    for T in Ts:
        for a, p in T.items():
            out[a] = out.get(a, 0) + p
    return op(out)


def scal(c, A):
    return op({a: c * p for a, p in A.items()})


def adj(A, m):
    """formal adjoint for the density x^m |dx/x|"""
    return op({a: sp.conjugate(p).subs(X, -X - a - m) for a, p in A.items()})


def im(A, m):
    return scal(1 / (2 * I), add(A, scal(-1, adj(A, m))))


def re(A, m):
    return scal(sp.Rational(1, 2), add(A, adj(A, m)))


def P0(n, y):
    """P^(0)(0, omega, y, d_omega)'s radial part for -Laplacian on R^n, y standing for rho d_rho"""
    return -y**2 + (n - 2) * y


# ------------------------------------------------------------------ N1
def n1(control=0, verbose=False):
    chk = Checklist(verbose, quiet=control != 0)
    a, bb, ts, r = sp.symbols("a b tstar r", positive=True)
    for n in (3, 4):
        c = 1 if (control and n == 4) else cc(n)
        F = r**bb * ts**(-a - bb)
        box = (2 * sp.diff(F, ts, r) + (n - 1) / r * sp.diff(F, ts) - sp.diff(F, r, 2) - (n - 1) / r * sp.diff(F, r))
        tau, R = 1 / ts, r / ts
        N0 = tau**2 * (-2 / R * (a + bb) * (bb + c) + R**-2 * P0(n, -bb)) * F
        chk(f"n = {n}: t*^2 (-box) = N^0 with c = {c}", sp.simplify(box - N0) == 0)
        # second line of (10.7): x_I = R^(-1/2), R d_R = -(1/2) x d_x, so x d_x acts on R^b as -2b
        s = sp.Symbol("s")
        l1 = -2 * (I * s + bb) * (bb + c)                    # times R^-1 = x_I^2
        l2 = -sp.Rational(1, 2) * (-2 * bb - 2 * I * s) * (-2 * bb - 2 * c)
        chk(f"n = {n}: (10.7)'s two lines agree", sp.expand(l1 - l2) == 0)
    chk("his printed constant 1 is c(3)", cc(3) == 1)
    return chk.ok


# ------------------------------------------------------------------ N2-N3
def N0x(c):
    """x_I^-2 N^0(P_0, sigma)'s first-order part in x_I: -(1/2)(X - 2 i sigma)(X - 2(c + S))"""
    return -sp.Rational(1, 2) * (X - 2 * I * sig) * (X - 2 * (c + S))


def symb1(A, a):
    """principal symbol of h A at the zero section's neighbourhood, A = x^a (q1 X + q0): h X -> i xi"""
    p = sp.Poly(A.get(a, 0), X)
    return sp.expand(p.coeff_monomial(X) * I * xi)


def n2(control=0, verbose=False):
    chk = Checklist(verbose, quiet=control != 0)
    for n in (3, 4):
        c = cc(n)
        dN = op({2: sp.diff(N0x(c), sig).subs(sig, 0)})
        m = 1 if control else 0
        Q0 = im(dN, m)
        want = -(n + 2 * sr)
        chk(f"n = {n}: Q_0 = -x_I^2 ({n} + 2 Re S)", set(Q0) == {2} and sp.simplify(Q0[2] - want) == 0)
    return chk.ok


def n3(control=0, verbose=False):
    chk = Checklist(verbose, quiet=control != 0)
    tot = {}
    for n in (3, 4):
        c = cc(n)
        Q0 = im(op({2: sp.diff(N0x(c), sig).subs(sig, 0)}), 0)[2]
        if control and n == 4:
            Q0 = im(op({2: sp.diff(N0x(1), sig).subs(sig, 0)}), 0)[2]
        B = op({2: N0x(c).subs(sig, 0)})
        sB = symb1(im(B, 0), 2)
        chk(f"n = {n}: symbol of h Im B = ({c + 1} + Re S) xi", sp.simplify(sB - (c + 1 + sr) * xi) == 0)
        tot3 = sp.expand(sB + Q0)
        chk(f"n = {n}: with Q_0, (c + 1) xi - (2c + 1) + Re S (xi - 2)",
            sp.simplify(tot3 - ((c + 1) * xi - (2 * c + 1) + sr * (xi - 2))) == 0)
        if n == 3:
            chk("n = 3: his 2 xi - 3 + (Re S)(xi - 2)", sp.simplify(tot3 - (2 * xi - 3 + sr * (xi - 2))) == 0)
        Q1 = re(op({2: sp.diff(N0x(c), sig).subs(sig, 0)}), 0)
        sQ1 = -symb1(Q1, 2)
        chk(f"n = {n}: sigma(Q_1) = x_I^2 xi", sp.simplify(sQ1 - xi) == 0)
        T = -(4 * gam + 2) + 2 * tot3.subs(xi, 2) - 2 * imz * sQ1.subs(xi, 2)
        tot[n] = sp.simplify(T)
        chk(f"n = {n}: total at R_(I+,+1,in) = -4(gam_I + h^-1 Im z)", sp.simplify(T + 4 * (gam + imz)) == 0)
    return chk.ok


# ------------------------------------------------------------------ N4
def n4(control=0, verbose=False):
    chk = Checklist(verbose, quiet=control != 0)
    for n in (3, 4):
        c = 1 if (control and n == 4) else cc(n)
        # z = 1: h x^2 (h X - 2i)(c + S), and -x^2 h x D_x = i h x^2 X
        A = op({2: h * (h * X - 2 * I) * (c + S)})
        B = op({2: I * h * X})

        def at0(T):
            q = T[2].subs(X, I * xi / h)
            return sp.limit(sp.simplify(q.subs(xi, 0) / h), h, 0)
        sA, sB = 2 * at0(im(A, 0)), 2 * at0(im(B, 0))
        chk(f"n = {n}: 2 h^-1 Im(h z^-1 x^2 (hX - 2iz)(c + S)) at R_out = -4(c + Re S)",
            sp.simplify(sA + 4 * (cc(n) + sr)) == 0)
        chk(f"n = {n}: 2 h^-1 Im(-x^2 h x D) = -2", sp.simplify(sB + 2) == 0)
        thr = sp.solve(sp.Eq((4 * gam + 2) + sA + sB, 0), gam)[0]
        chk(f"n = {n}: threshold gam_I < {cc(n)} + Re S", sp.simplify(thr - (cc(n) + sr)) == 0)
    return chk.ok


# ------------------------------------------------------------------ N5
def n5(control=0, verbose=False):
    chk = Checklist(verbose, quiet=control != 0)
    tau, R, x, ts, r = sp.symbols("tau R x_I tstar r", positive=True)
    for n in (3, 4):
        k = n - 2 if control else n - 1                  # dx = r^(n-1) dr domega
        J = sp.Matrix([[sp.diff(1 / tau, tau), sp.diff(1 / tau, R)], [sp.diff(R / tau, tau), sp.diff(R / tau, R)]])
        dens = sp.simplify(sp.Abs(J.det()) * (R / tau)**k * tau * R)
        chk(f"n = {n}: |dt dx| = R^{n} tau^-{n + 1} |dtau/tau dR/R domega|",
            sp.simplify(dens - R**n * tau**-(n + 1)) == 0)
        J2 = sp.Matrix([[sp.diff(1 / tau, tau), sp.diff(1 / tau, x)],
                        [sp.diff(1 / (tau * x**2), tau), sp.diff(1 / (tau * x**2), x)]])
        dens2 = sp.simplify(sp.Abs(J2.det()) * (1 / (tau * x**2))**k * tau * x)
        chk(f"n = {n}: |dt dx| = 2 x_I^-{2 * n} tau^-{n + 1} |dtau/tau dx_I/x_I|",
            sp.simplify(dens2 - 2 * x**(-2 * n) * tau**-(n + 1)) == 0)
        # weights: rho_K = R, rho_+ = tau/R; L^2(|dt dx|) = rho_K^(1/2) rho_+^((n+1)/2) L^2_b
        aK, aP = sp.symbols("aK aP")
        sK, sP = sp.Rational(1, 2), sp.Rational(n + 1, 2)
        chk(f"n = {n}: R^n tau^-(n+1) = rho_K^-1 rho_+^-(n+1)",
            sp.simplify(dens - R**(-2 * sK) * (tau / R)**(-2 * sP)) == 0)
        expR = sp.expand((aK + sK) - (aP + sP)); expT = sp.expand(aP + sP)
        chk(f"n = {n}: gam_cf = alpha~_K - alpha~_+ - {sp.Rational(n, 2)}, -Im sigma = alpha~_+ + {sP}",
            expR == aK - aP - sp.Rational(n, 2) and expT == aP + sp.Rational(n + 1, 2))
        chk(f"n = {n}: gam_I = alpha_I + {sp.Rational(n, 2)}, gam_+ = alpha_+ + {sP} (x_I^{2 * n} = rho_I^{n})",
            sp.simplify(dens2 / 2 - (x**2)**-n * tau**-(n + 1)) == 0)
        rI, rP, rK = ts / (ts + r), (ts + r) / (ts * r), r / (ts + r)
        chk(f"n = {n}: rho_I^{n} rho_+^{n + 1} rho_K = 1/(t* r^{n})",
            sp.simplify(rI**n * rP**(n + 1) * rK - 1 / (ts * r**n)) == 0)
        chk(f"n = {n}: mu_b = |dt dx|/(t* r^{n}) is |dt*/t* dr/r domega|",
            sp.simplify(r**k / (ts * r**n) - 1 / (ts * r)) == 0)
        chk(f"n = {n}: L^2(|dx|) = rho^{sp.Rational(n, 2)} L^2(|dx|/|x|^{n})",
            sp.Rational(k + 1, 2) == sp.Rational(n, 2))
        chk(f"n = {n}: -1/2 + S-bar + n/2 = c + S-bar", -sp.Rational(1, 2) + sp.Rational(n, 2) == cc(n))
    chk("n = 3: his 3/2, 2 and 1 + S-bar", (sp.Rational(3, 2), 2, cc(3)) == (sp.Rational(3, 2), 2, 1))
    return chk.ok


# ------------------------------------------------------------------ N6-N7
def n6(control=0, verbose=False):
    chk = Checklist(verbose, quiet=control != 0)
    hh = sp.Symbol("hhat", positive=True)
    T = {}
    for n in (3, 4):
        c = cc(n)
        P = op({-2: P0(n, -X)})                             # R^-2 P^(0)(0, omega, -R d_R), X = R d_R
        chk(f"n = {n}: R^-2 P^(0) symmetric for R^{n} |dR/R|", im(P, n) == {})
        q = sp.Poly(im(P, 0)[-2], X)
        # h^2 R^-2 q1 X -> h^2 R^-2 q1 (i xi_b), xi_b = (R/h) xi_cl: hhat q1 i xi
        corr = sp.expand(q.coeff_monomial(X) * I)
        chk(f"n = {n}: density correction -{n} hhat xi", sp.simplify(corr + n) == 0)
        dN = op({-1: -2 * I * (X + c + S)})
        Q0 = im(dN, 0)
        chk(f"n = {n}: sigma(Q_0,h) = -hhat ({n} + 2 Re S)", set(Q0) == {-1} and sp.simplify(Q0[-1] + n + 2 * sr) == 0)
        # (5.20): vartheta_dK+,in is the top of the spectrum of all of rho_oo sigma_1(r^2 Im P_0) at R_in, rho_oo =
        # -1/sigma_3b; P_0's term 2 rho d_t* S, d_t* -> i sigma_3b / r, gives -(S + S^*) (Lemma 5.12's proof)
        s3 = sp.Symbol("sigma_3b", negative=True)
        sym = 2 * I * s3 * S
        thS = sp.expand(-(sym - sp.conjugate(sym)) / (2 * I) / s3)
        x0 = -2
        q0S = sp.expand(Q0[-1] - Q0[-1].subs(sr, 0))
        chk(f"n = {n}: vartheta's S part -(S + S^*) = -2 Re S is sigma(Q_0,h)'s at -xi/2 = 1",
            sp.simplify(thS + 2 * sr) == 0 and sp.simplify(q0S + sp.Rational(x0, 2) * thS) == 0)
        gcf = -(alp + (sp.Rational(3, 2) if (control and n == 4) else sp.Rational(n, 2)))
        tot = -(4 * b - 4 * gcf + 2) + 2 * (Q0[-1].subs(sr, 0) + corr * x0 - sp.Rational(x0, 2) * th)
        T[n] = sp.expand(tot)
    chk("total at R_(cf,+1,in) the same at n = 3 and 4", sp.simplify(T[3] - T[4]) == 0)
    chk("= -4b - 4 alpha_+ - 2 + 2 vartheta, Re S inside vartheta: (10.28)",
        sp.simplify(T[3] - (-4 * b - 4 * alp - 2 + 2 * th)) == 0)
    his = -(4 * b + 4 * (alp + sp.Rational(3, 2)) + 2) + 2 * (-3 - 3 * x0 - sp.Rational(x0, 2) * th)
    chk("his printed sum is that total: (10.28), b + alpha_+ > (1/2)(-1 + vartheta)", sp.simplify(his - T[3]) == 0)
    return chk.ok


def n7(control=0, verbose=False):
    chk = Checklist(verbose, quiet=control != 0)
    T = {}
    for n in (3, 4):
        c = 1 if (control and n == 4) else cc(n)
        A = op({-1: -2 * I * h * X})                        # 2 h D_R = -2 i h R^-1 (R d_R)
        B = op({-1: -2 * (c + S) * I * h})                  # -2(c + S) i R^-1 h
        sA, sB = 2 * im(A, 0)[-1] / h, 2 * im(B, 0)[-1] / h
        chk(f"n = {n}: 2 Im(2h D_R) = -2 hhat", sp.simplify(sA + 2) == 0)
        Cc = op({-1: -2 * (c + S) * h * h * X})             # -2(c + S) h z^-1 h d_R: vanishes at xi = 0
        q = sp.expand(im(Cc, 0)[-1] / h**2)
        chk(f"n = {n}: the h d_R term is h^2 R^-1 (q0 + q1 X) = hhat^2 R q0 + hhat R q1 (h X): below the hhat level",
            not q.has(h) and q != 0)
        gcf = -(alp + sp.Rational(n, 2))
        T[n] = sp.expand(4 * b - 4 * gcf + 2 + sA + sB)
        chk(f"n = {n}: total = 4b + 4 alpha_+ + 2 - 4 Re S", sp.simplify(T[n] - (4 * b + 4 * alp + 2 - 4 * sr)) == 0)
    thr = sp.solve(sp.Eq(T[4], 0), b)[0]
    chk("negative iff b + alpha_+ < -1/2 + Re S", sp.simplify(thr - (-alp - sp.Rational(1, 2) + sr)) == 0)
    his = 4 * b + 4 * alp + 2 + 4 * sr
    chk("his printed '+ 4 Re S' gives b + alpha_+ < -1/2 - Re S instead: a sign misprint",
        sp.simplify(sp.solve(sp.Eq(his, 0), b)[0] - (-alp - sp.Rational(1, 2) - sr)) == 0)
    return chk.ok


# ------------------------------------------------------------------ N8
def n8(control=0, verbose=False):
    chk = Checklist(verbose, quiet=control != 0)
    lam, mu, Wv = sp.symbols("lambda mu W", positive=True)
    for n in (3, 4):
        c = cc(n)
        P = lambda y: P0(n, y) - 7                          # any angular eigenvalue
        # (a) N^1 on v^lam: R^(i sig) R^2 N^0 R^(-i sig), with R d_R = -v d_v
        m_ = lam + I * sig
        N0v = -2 * (I * sig - m_) * (c + S - m_)            # coefficient of v^(m+1), R^-1 = v
        lhs = {lam - 1: N0v, lam: P(m_)}                      # after R^2 R^(i sig) = v^(-2 - i sig)
        rhs = {lam - 1: -2 * (lam + I * sig - c - S) * lam, lam: P(lam + I * sig)}
        chk(f"n = {n}: N^1(P_0, sigma) in v", all(sp.simplify(lhs[k] - rhs[k]) == 0 for k in lhs))
        # (b) Fourier: F(v_+^lam) = Gamma(lam + 1) W^(-lam-1), W = -i rhat, rhat d_rhat = W d_W
        g = sp.gamma(lam + 1) * Wv**(-lam - 1)
        F_lhs = rhs[lam - 1] * sp.gamma(lam) * Wv**(-lam) + rhs[lam] * g
        k2 = (2 if control and n == 4 else c + 1)
        rhat = I * Wv
        F_rhs = (2 * I * rhat * (-Wv * sp.diff(g, Wv) + (I * sig - k2 - S) * g)
                 + P(-Wv * sp.diff(g, Wv) / g - 1 + I * sig) * g)
        chk(f"n = {n}: (10.40) with i sigma - {k2} - S", sp.simplify(sp.expand(F_lhs - F_rhs)) == 0)
        # (c) rhat^(1 - i sig) conjugation and rho-hat = 1/rhat: on rhat^mu
        e = mu - 1 + I * sig                                  # rhat^(-1+i sig) rhat^mu
        val = 2 * I * (-e + I * sig - (c + 1) - S), P(-e - 1 + I * sig)      # coefficients of rhat^(e+1), rhat^e
        # times rhat^(1 - i sig) rho-hat^2: rhat^(mu - 1) and rhat^(mu - 2)
        Ntf = 2 * I * (-mu - c - S), P(-mu)                   # rho-hat (rho-hat d - c - S), rho-hat^2 P(rho-hat d)
        chk(f"n = {n}: rhat^(1 - i sigma) gives N_tf(P_0, 1)",
            sp.simplify(val[0] - Ntf[0]) == 0 and sp.simplify(val[1] - Ntf[1]) == 0)
    return chk.ok


# ------------------------------------------------------------------ N9
def n9(control=0, verbose=False):
    chk = Checklist(verbose, quiet=control != 0)
    gc, bb, q_, r_ = sp.symbols("gamma_cf b q r")
    for n in (3, 4):
        pt = [sp.Rational(k + 1, 3 * n) for k in range(n - 1)]
        pt = pt + [sp.sqrt(1 - sum(p**2 for p in pt))]
        fields = []
        for a_, b_ in itertools.combinations(range(n), 2):
            v = [0] * n; v[a_], v[b_] = -pt[b_], pt[a_]
            fields.append(v)
        if control:
            fields = fields[:n - 1]
        M = sp.Matrix(fields)
        chk(f"n = {n}: {len(fields)} rotation fields span T S^{n - 1}",
            M.rank() == n - 1 and len(fields) == n * (n - 1) // 2)
        chk(f"n = {n}: Lemma 10.7's V has {len(fields) + 2} entries", len(fields) + 2 == {3: 5, 4: 8}[n])
        chk(f"n = {n}: Lemma 10.9's shift dim(iota+) - 1 = {n - 1}", n - 1 == {3: 2, 4: 3}[n])
        hn = sp.Rational(n, 2)
        # weights in Rhat^n |dRhat/Rhat| = rho_cf^n rho_sf^-n |b|: (a, c) there is (a - n/2, c + n/2) in |b|
        conv = lambda a, cw: (a - hn, cw + hn)
        chk(f"n = {n}: (gam_cf + n/2, b - gam_cf - n/2) is (gam_cf, b - gam_cf) in |b|",
            conv(gc + hn, bb - gc - hn) == (gc, bb - gc))
        out = conv(gc + hn - 2, bb - gc - hn + 1)
        chk(f"n = {n}: Corollary 9.39's output is (gam_cf - 2, b - gam_cf + 1) in |b|",
            sp.simplify(out[0] - (gc - 2)) == 0 and sp.simplify(out[1] - (bb - gc + 1)) == 0)
        chk(f"n = {n}: q = gam_cf + n/2 = -alpha_+", sp.simplify((-(alp + hn)) + hn + alp) == 0)
        chk(f"n = {n}: Remark 11.4's beta_- < {-1 + hn} + S-bar", -1 + hn == {3: sp.Rational(1, 2), 4: 1}[n])
    return chk.ok


CHECKS = [("N1 (10.6)-(10.7): t*^2 (-box) is N^0 with c = (n - 1)/2 (1; 3/2)", n1),
          ("N2 (10.25): Q_0 = -x_I^2 (n + 2 Re S) (3; 4)", n2),
          ("N3 (10.27) at R_I+,in: the symbol (c + 1 + Re S) xi; total -4(gam_I + h^-1 Im z) at every n", n3),
          ("N4 R_I+,out: gam_I < (n - 1)/2 + Re S (1; 3/2)", n4),
          ("N5 densities: R^n tau^-(n+1), the shifts n/2 and (n + 1)/2, mu_b = |dt dx|/(t* r^n), |dx|/|x|^n", n5),
          ("N6 R_cf,in: correction -n hhat xi, Q_0,h -(n + 2 Re S), its Re S in vartheta; (10.28) unchanged", n6),
          ("N7 R_cf,out: 4b + 4 alpha_+ + 2 - 4 Re S at every n; his '+ 4 Re S' a sign misprint", n7),
          ("N8 Lemma 10.10: N^1, (10.40) with i sigma - (c + 1) - S (2; 5/2), N_tf by rhat^(1 - i sigma)", n8),
          ("N9 counts and shifts: C(n,2) fields, n - 1, Rhat^n, Corollary 9.39, Remark 11.4", n9)]


def run(only=None, verbose=False):
    ok = True
    for k, (name, f) in enumerate(CHECKS, 1):
        if only and k != only:
            continue
        t0 = time.time()
        res = f(0, verbose)
        ok &= res
        print(f"{name[:104]:<104} {'PASS' if res else 'FAIL'} {time.time() - t0:3.0f}s", flush=True)
    n = 1 if only else len(CHECKS)
    print(f"iplusnorm5.py: {n if ok else 'not all'}/{n}")
    return ok


def mutants():
    caught = total = 0
    for name, f in CHECKS:
        total += 1
        res = f(1, False)
        caught += not res
        print(f"mutant 1 of {name[:2]}: {'caught' if not res else 'NOT caught'}", flush=True)
    print(f"iplusnorm5.py mutants: {caught}/{total}")
    return caught == total


if __name__ == "__main__":
    args = sys.argv[1:]
    vb = "--verbose" in args
    if "--selftest" in args:
        sys.exit(0 if run(verbose=vb) else 1)
    elif "--mutants" in args:
        sys.exit(0 if mutants() else 1)
    elif "--only" in args:
        sys.exit(0 if run(int(args[args.index("--only") + 1]), vb) else 1)
    print(__doc__)
