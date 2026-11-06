"""r5settle5.py -- SETTLE-GLAM5 round 5: the computations behind the seating of the round-3 and round-4 verifiers'
findings that are not measured on the full operator (those are in r5op5.py and cclass5.py).

  A (exact, enumeration; round 3 m7) Proposition R3.1's lam-orders derived from the monomials of the record's
    source (11.4), every product of m >= 1 factors from {G_3, ..., G_J, u_J} with its coefficient (eta-contraction,
    mu r^-2, Gamma[g0] ~ r^-3, d d g0 ~ r^-4, (d g0)^2 ~ r^-6) and its two derivatives (each a d_v, costing lam^-1, or
    an r-derivative, gaining r^-1), m up to 7. A1: e(G_k) = k - 4 (k = 4..13). A2: on the far region
    r >= lam^-2 every monomial of the remainder's source trades its excess decay for powers of lam (r^-1/2 <= lam)
    and the stage recursion closes at B_(J+1) = 2 + max(B_J + 1, J - 2), so B_J = 3J - 9 (J = 4..12), the same at
    m_max = 6 and 7: M(J, n, m) = 3J - 9 + n + m, at most R3.1's (J^2 - J)/2 - 3 + n + m and the round-3 verifier's
    4J - 13 + n + m for J >= 4 (so R3.1's stated bound holds a fortiori). Control (the code mutated: no trade): the
    explicit monomials' order grows with m_max (no bound exists).
  B (exact; round 3 m5, nit s > 2) K*(a, 8, M, k0) of Lemma R3.2 with s := max(5/2, (2M + 1)/(7 - 2a)) and
    M = 27 + 2 k0 is quadratic in k0 (a = 11/4: K* = 116, 821.5, 2071.5 at k0 = 0, 10, 20; for k0 >= 400 the second
    differences are those of the quadratic s (a + k0), s = (2M + 1)/(7 - 2a)), and with R5's M = 17 + 2 k0 too.
    Control (the code mutated: s held fixed, not growing with M): the second differences vanish (K* linear).
  C (exact; round 3 P8c-P8d) the interpolation optimum recomputed: the lam-exponent of L sigma^-(k-4)
    (lam^(K-3) + lam^-M sigma^(J'-3)) at sigma = lam^beta, maximised over beta on an exact grid, equals
    (K - 3)(1 - th_k) - M th_k at beta* = (K - 3 + M)/(J' - 3), and beta* > 1 (sigma in the far region) exactly when
    K - 3 + M > J' - 3 (sampled K, M). Controls (the code mutated): the remainder exponent J' - 3 replaced by J' - 4
    breaks the formula; beta held at 0 (no optimisation, a fixed radius) gives the exponent -M < 0.
  D (exact and sampled; round 3 m1) the causal structure on W: g_b0^-1(dv, dv) = 0 and its first variation is
    -h(ell, ell), so for g_b0 + eps h the sign of g^-1(dv, dv) is that of -h(ell, ell): both signs occur (exact,
    two h): v is not a time function for the perturbed metrics, and for g_b0 the infimum of dv(Y) over future causal
    Y is 0, attained at Y = -grad v (exact; T1a's 5.7e-2 was a sampling artefact). The repairs: v + eps t has
    g_b0^-1 = -2 eps - eps^2 (1 + mu r^-2) (margin 2 eps, uniform); Phi_W := v + 1/r has -2 r^-2 + r^-4 (1 - mu r^-2)
    and, for every symmetric delta with operator norm <= r^-2/2, (g_b0^-1 + delta)(dPhi, dPhi) <= -r^-2 + r^-4 < 0
    since |dPhi|_E^2 = 1 + (1 - r^-2)^2 <= 2 (exact); sampled at 2000 points (r in [4, 400]); -grad Phi_W is future
    directed (exact). Control: operator norm 2 r^-2 makes dPhi_W spacelike somewhere.
  E (sampled; round 4 m3) the weight w = (u* - u)^(2a) on W = {v >= v1, t <= f(r), r >= 4R}: with u* := sup f + 1,
    r + 1 <= u* - u <= 2r + C at 4000 sampled points for 20 random f with |f'| <= 1/2 and v1 = f(4R) + 4R. Control
    (round 4's u* := 2 sup f - v1 + 1): r <= u* - u fails.
  F (exact and sampled; round 4 M4) the localised energy argument: F1 the flux through {Phi_W = V_*} is >= 0:
    T(d_t, -grad Phi_W) for g = g_b0 + H, |H|_op <= r^-2/2, random d phi (6000 samples, floating point) is >= 0
    (dominant energy, both vectors future timelike). Control: with the spacelike normal grad r of a timelike cut-off
    {r = R} in place of -grad Phi_W it is negative somewhere (such a boundary's flux has no sign). F2 the
    domain-of-dependence energy identity on a truncated diamond {t1 <= t <= t2, R + (t - t1) <= r <= R2 - (t - t1)}
    in the flat radial model (measure r^3 dr): E(t2) + both null fluxes (each >= 0, tangential derivatives) =
    E(t1) - int int phi_t box phi r^3, exact for a polynomial phi.
    Control: with a transverse derivative in one flux it fails. F3 S1 and the Hardy inequality on a finite interval,
    with their boundary terms, exact identities; and if int^oo r^(2a+3) F^2 dr < oo then liminf R^(2a+4) F(R)^2 = 0
    (so the boundary term vanishes along a sequence): checked on F = r^(-a-2-eta) (-> 0); control F = r^(-a-2) (the
    integral diverges and R^(2a+4) F^2 = 1). F4 the rejected localisation (data g_b0 beyond V_* + 2, h_R = -Sigma there):
    the weighted energy of -Sigma_2 = -r^-2 P beyond V_* is int r^(2a - 3) dr, infinite exactly for a >= 1 (exact).
    F5 the exterior tail: with zero data beyond the band and the source P(Sigma) = O(r^(-13/2)) (r5op5 O2), the
    unweighted energy beyond R after a time |T| is at most C |T|^2 R^-9 (finite speed), and the weighted energy
    int r^(2a) d(-C R^-9) converges exactly for a < 9/2 (exact). Control: the source O(r^-6) of Sigma without F_4
    gives a < 4.
  G (exact and quadrature; round 3 Z7, T2, T7, Z8, window; round 4 B12) the fields: data G_k(v1) = c_k (k = 4..9,
    random rationals; l = 2), the after-shell coefficients G_k(v) from the flat recursion (2q - 3) G_(2q)' = (Delta +
    (q - 1)(q - 3)) G_(2q - 2), Sigma = sum_(p in Pi) r^-p c_(2p) 2F1(p + l, p - l - 2; p - 1/2; s/2). G1: at fixed v
    the coefficients of r^(-k/2) of the truth minus Sigma vanish for k <= 8 and equal c_9 at k = 9 (exact), so h_R =
    O(r^(-9/2)); with p = 4 dropped (control) the r^-4 coefficient survives. G2 (quadrature, 60 digits) the cap energy
    of the truncation (unit band in v at t = T, smoothstep cut-off, weight (2r)^(2a)) has fitted exponent 2a - 6 in |T|
    (a = 2.2, 2.75, 2.95), -> 0 exactly for a < 3; the control (p = 4 dropped) 2a - 5. G3 (exact, sympy) the N-flux
    tail beyond |T| of the field h_R(v1, r) has exponent 2a - 7; the control (p = 4 dropped) 2a - 6. G4 the class on
    S: the S-energy with Hardy (scale5 Z8a) gives rho^(a+1) L^2_b, inside rho^(l0) L^2_b exactly when a + 1 >= l0
    (exact on rho^beta). G5 the weight window: with the kernels of r5op5 O1
    (> 1 for every a), the h_R rows 3/2 + a and a + 1/2 (from S1 and Hardy: exponents computed below), the residual
    9/2 - a (degree -13/2), the cap (G2), the N-flux (G3) and G4, the set of admissible a on the grid a = 0, 1/100,
    ..., 4 is (l0 - 1, 3) for l0 = 3.1, 3.3, 3.6, 3.9: the lower bound 5/2 of rounds 3-4 is needed by nothing.
    Controls: p = 4 dropped gives (l0 - 1, 5/2), empty for l0 >= 7/2; the pointwise reading of the class on S
    (a > l0 - 1/2) gives (l0 - 1/2, 3), empty for l0 >= 7/2. G6 (exact) Sigma|_S: rho^p F_p(1 + (f_oo - v1) rho +
    f_2 rho^3) has the exponents p + j (j = 0..3, p in Pi; the Taylor composition F_p(1 + d) = sum F_p^(m)(1) d^m/m!
    with the derivatives of the 2F1 at 1/2 by mpmath), all in E_0^(1/2); control: a p = 9/4 term gives 9/4.
  H (exact; round 4 m7) the means' exponents from Theorem A_P's coefficient classes (N1STAR-PROOF.md (9.6) and the
    count's last sentence): the inputs of (c) are E_(3/2) m_m, E_(3/2) Psi_m, E_(3/2) ell phi_m, E_(5/2) d_v phi_m,
    E_(5/2) r^-1 Omega phi_m and known sources in L_3; of (a) E_2 m_m, E_3 d phi_m, E_(3/2) gh_(m+1) and L_3; of (b)
    m_m(ell, ell) and q_m in L_2. With m_m, ell phi_m, Psi_m, r^-1 Omega phi_m in L_2, phi_m, d_v phi_m in L_1 and
    gh in O_2 (orders in (1/2)N above their leading ones), every input of (a) and (c) has exponent >= 3 and of (b)
    >= 2: 2/(2q - 5), 1/(q - 5/2) and 1/(q - 1) are finite at every order to 20. Control (the code mutated: d_v phi_m's
    coefficient class E_(3/2) in (c)): an input at q = 5/2 appears (a logarithm).
Labels: computed (exact sympy and integer arithmetic; D-F sampled in floating point; G2-G3 mpmath quadrature).

    python3 checks/r5settle5.py
"""
import random
import sys
from fractions import Fraction as Fr
from itertools import combinations_with_replacement

import mpmath as mp
import sympy as sp

import builtins as _builtins
import textwrap as _textwrap

_raw_print = _builtins.print


def print(*args, **kw):  # output lines are kept to 121 characters (wrapped, continuation indented)
    text = kw.pop("sep", " ").join(str(x) for x in args)
    for line in text.split("\n"):
        for piece in (_textwrap.wrap(line, 121, subsequent_indent="        ", break_long_words=True,
                                     replace_whitespace=False, drop_whitespace=True) or [""]):
            _raw_print(piece, **kw)


FAIL = []


def check(name, ok, msg=""):
    print(f"  {name}: {'pass' if ok else 'FAIL'} {msg}")
    if not ok:
        FAIL.append(name)


# ================================================================ A: the lam-orders of Proposition 11.1

HALF = Fr(1, 2)
COEFS = [(0, 2), (2, 2), (3, 1), (4, 0), (6, 0)]  # (r-power of the coefficient, derivatives on the u-factors)


def explicit_orders(J, mmax, trade, e):
    """(max effective lam-order of the explicit monomials of r-order >= (J+4)/2, max lam-order at r-order (J+3)/2)
    for products of m factors G_k (3 <= k <= J), m <= mmax. The orders are additive over the factors, so only the
    numbers of d_v and of r-derivatives matter, not which factor carries them."""
    best_tail, best_q = -10**9, -10**9
    target_q = Fr(J + 3, 2)
    for m in range(1, mmax + 1):
        for ks in combinations_with_replacement(range(3, J + 1), m):
            base_r, base_l = Fr(sum(ks), 2), sum(e[k] for k in ks)
            for p0, nd in COEFS:
                if m == 1 and p0 == 0:
                    # the flat operator on one G_k: its d_v part is the recursion (cancelled in the construction of
                    # the G_k); its (Delta + c) G_k r^-(k/2 + 2) part is a source: two r-type derivatives
                    splits = [(0, 2)]
                else:
                    splits = [(nv, nd - nv) for nv in range(nd + 1)]
                for nv, nr in splits:
                    lam = base_l + nv
                    rord = base_r + p0 + nr
                    if rord == target_q:
                        best_q = max(best_q, lam)
                    elif rord >= Fr(J + 4, 2):
                        best_tail = max(best_tail, lam - (2*(rord - Fr(J + 4, 2)) if trade else 0))
    return best_tail, best_q


def remainder_orders(J, B, mmax, e):
    """max effective lam-order of the source terms containing u_J: one factor at the induction bound
    lam^-(B_J + d) r^-(J+1)/2, the others G_k or crude u_J (|d^d u_J| <= lam^-d r^-2 on r >= lam^-2), with the
    trade r^-1/2 <= lam applied to the excess decay"""
    best = -10**9
    for m in range(1, mmax + 1):
        for nrem in range(1, m + 1):
            for ks in combinations_with_replacement(range(3, J + 1), m - nrem):
                base_l = B + sum(e[k] for k in ks)
                base_r = Fr(J + 1, 2) + 2*(nrem - 1) + Fr(sum(ks), 2)
                for p0, nd in COEFS:
                    if m == 1 and p0 == 0:
                        continue  # the principal part of u_J's own equation
                    for d_rem in range(nd + 1):
                        if nrem == m and d_rem != nd:
                            continue
                        for nv in range(nd - d_rem + 1):
                            nr = nd - d_rem - nv
                            lam = base_l + d_rem + nv
                            rord = base_r + p0 + nr
                            assert rord >= Fr(J + 4, 2)
                            best = max(best, lam - 2*(rord - Fr(J + 4, 2)))
    return best


def stages(Jmax, mmax, trade=True):
    e = {3: -1}
    for k in range(4, Jmax + 2):
        e[k] = explicit_orders(k - 1, mmax, trade, e)[1]
    B = {3: -1}
    for J in range(3, Jmax):
        tail, _ = explicit_orders(J, mmax, trade, e)
        rem = remainder_orders(J, B[J], mmax, e)
        B[J + 1] = max(tail, rem, e[J + 1] + 1, e[J + 1]) + 2
    return e, B


def part_a():
    print("A  Proposition R3.1's lam-orders from the monomials of (11.4) (round 3, m7)")
    e, B = stages(12, 6)
    check("A1 e(G_k) = k - 4 for k = 4..13 from every monomial of r-order exactly (k + 2)/2 (m <= 6 factors)",
          all(e[k] == k - 4 for k in range(4, 14)), str([e[k] for k in range(3, 12)]))
    okB = all(B[J] == 3*J - 9 for J in range(4, 13))
    e7, B7 = stages(12, 7)
    check("A2 with the trade (r^-1/2 <= lam on r >= lam^-2) the recursion gives B_J = 3J - 9 (J = 4..12), the same at "
          "m_max = 6 and 7", okB and all(B7[J] == B[J] for J in range(4, 13)), str([B[J] for J in range(3, 13)]))
    check("A2' B_J = 3J - 9 <= 4J - 13 <= (J^2 - J)/2 - 3 for J = 4..12: the round-3 verifier's and R3.1's exponents "
          "are upper bounds", all(3*J - 9 <= 4*J - 13 <= (J*J - J)//2 - 3 for J in range(4, 13)))
    ee = {k: k - 4 for k in range(3, 10)}
    t4, t7 = explicit_orders(8, 4, False, ee)[0], explicit_orders(8, 7, False, ee)[0]
    check("A2'' control (the code mutated: no trade): at J = 8 the explicit monomials' order grows with m_max (no "
          f"bound): m_max = 4 gives {t4}, m_max = 7 gives {t7}", t7 > t4)


# ================================================================ B: K* of Lemma R3.2

def kstar(a, Jp, M, j, smin=Fr(5, 2), sfixed=None):
    s = sfixed if sfixed is not None else max(smin, Fr(2*M + 1)/(Jp - 1 - 2*a))
    need = [4 + j + s*(a + j)]
    for k in range(4, 9):
        th = Fr(k - 4, Jp - 3)
        if th == 1:
            continue
        for i in range(0, j + 2):
            need.append(3 + i + (s*max(0, 2*a + 2 - k)/2 + (M + i)*th)/(1 - th))
    return s, max(need)


def part_b():
    print("B  K* of Lemma R3.2 as a function of k0 (round 3, m5)")
    a = Fr(11, 4)
    ks = [kstar(a, 8, 27 + 2*k0, k0)[1] for k0 in (0, 10, 20)]
    def d2(M0, k0s, **kw):
        v = [kstar(a, 8, M0 + 2*k0, k0, **kw)[1] for k0 in k0s]
        return [v[i + 2] - 2*v[i + 1] + v[i] for i in range(len(v) - 2)]
    lead = Fr(4)/(7 - 2*a)  # the slope of s = (2M + 1)/(7 - 2a) in k0, M = M0 + 2 k0
    big = d2(27, (400, 500, 600, 700))
    check("B1 M = 27 + 2 k0, a = 11/4: K* = 116, 821.5, 2071.5 at k0 = 0, 10, 20, and for k0 >= 400 the second "
          "differences (step 100) are constant, 2 (4/(7 - 2a)) 100^2 = 160000/3: K* is quadratic in k0, not linear",
          ks == [116, Fr(1643, 2), Fr(4143, 2)] and big[0] == big[1] == 2*lead*100**2,
          f"{[str(x) for x in ks]}, second differences {[str(x) for x in big]}")
    ks2 = [kstar(a, 8, 17 + 2*k0, k0)[1] for k0 in (0, 10, 20)]
    big2 = d2(17, (400, 500, 600, 700))
    check("B2 with R5's M = 17 + 2 k0 (B_8 = 15): quadratic too (the same second differences), and smaller",
          big2[0] == big2[1] == 2*lead*100**2 and all(x < y for x, y in zip(ks2, ks)), f"{[str(x) for x in ks2]}")
    s_old = [kstar(a, 8, 27 + 2*k0, k0, smin=Fr(2))[1] for k0 in (0, 10, 20)]
    check("B3 the nit s > 2: s := max(5/2, ...) leaves K* unchanged wherever (2M + 1)/(7 - 2a) > 5/2 (here)",
          s_old == ks)
    kl = d2(27, (400, 500, 600, 700), sfixed=Fr(37))
    check("B4 control (the code mutated: s held fixed at 37): the second differences vanish (K* linear), so the "
          "quadratic term is s's growth with M", kl == [0, 0], str([str(x) for x in kl]))


# ================================================================ C: the interpolation optimum

def interp_exp(K, M, Jp, k, beta, rem=None):
    rem = Jp - 3 if rem is None else rem
    return min(Fr(K - 3), -Fr(M) + beta*rem) - beta*(k - 4)


def part_c():
    print("C  the interpolation optimum recomputed (round 3, P8c-P8d)")
    Jp = 8
    grid = [Fr(n, 40) for n in range(0, 40*40 + 1)]
    ok_formula, ok_far, ctl1, ctl2 = True, True, False, True
    rnd = random.Random(8)
    for _ in range(12):
        K, M = rnd.randint(6, 60), rnd.randint(1, 40)
        bstar = Fr(K - 3 + M, Jp - 3)
        for k in (5, 6, 7):
            th = Fr(k - 4, Jp - 3)
            best = max(grid + [bstar], key=lambda b: interp_exp(K, M, Jp, k, b))
            val = interp_exp(K, M, Jp, k, best)
            ok_formula = ok_formula and val == (K - 3)*(1 - th) - M*th and interp_exp(K, M, Jp, k, bstar) == val
            ok_far = ok_far and ((bstar > 1) == (K - 3 + M > Jp - 3))
            bm = max(grid + [bstar], key=lambda b: interp_exp(K, M, Jp, k, b, rem=Jp - 4))
            ctl1 = ctl1 or interp_exp(K, M, Jp, k, bm, rem=Jp - 4) != (K - 3)*(1 - th) - M*th
            ctl2 = ctl2 and interp_exp(K, M, Jp, k, Fr(0)) == -M < 0
    check("C1 the optimum over sigma = lam^beta is (K - 3)(1 - th_k) - M th_k at beta* = (K - 3 + M)/(J' - 3) (12 "
          "random "
          "K, M; k = 5, 6, 7)", ok_formula)
    check("C2 beta* > 1 (sigma inside the far region r >= lam^-2) exactly when K - 3 + M > J' - 3", ok_far)
    check("C3 control (the remainder exponent mutated to J' - 4): the formula fails", ctl1)
    check("C4 control (no optimisation, beta = 0: a fixed radius): the exponent is -M < 0", ctl2)


# ================================================================ D: the causal structure on W (round 3, m1)

t, x1, x2, x3, x4, mu, ep = sp.symbols("t x1 x2 x3 x4 mu epsilon", real=True)
RR = sp.sqrt(x1**2 + x2**2 + x3**2 + x4**2)
KV = sp.Matrix([1, x1/RR, x2/RR, x3/RR, x4/RR])
ETA = sp.diag(-1, 1, 1, 1, 1)
GB0I = ETA - mu/RR**2*(ETA*KV)*(ETA*KV).T


def part_d():
    import numpy as np
    print("D  the causal structure on W: v is not a time function; v + eps t and Phi_W are (round 3, m1)")
    dv = KV
    pt = {x1: sp.Rational(3, 1), x2: sp.Rational(1, 1), x3: sp.Rational(-2, 1), x4: sp.Rational(1, 2), mu: 1}
    gb0 = ETA + mu/RR**2*KV*KV.T
    G0p, dvp = gb0.subs(pt), dv.subs(pt)
    ellp = G0p.inv()*dvp
    signs = []
    for H in (sp.diag(0, 1, 0, 0, 0), -sp.diag(0, 1, 0, 0, 0)):
        val = sp.simplify((dvp.T*(G0p + ep*H).inv()*dvp)[0, 0])
        first = sp.simplify(sp.diff(val, ep).subs(ep, 0))
        hll = sp.simplify((ellp.T*H*ellp)[0, 0])
        signs.append((sp.sign(sp.N(val.subs(ep, sp.Rational(1, 100)), 30)), sp.simplify(first + hll) == 0,
                      sp.simplify(val.subs(ep, 0)) == 0))
    check("D1 (g_b0 + eps h)^-1(dv, dv) vanishes at eps = 0, has first variation -h(ell, ell) (exact) and takes both "
          "signs (h = +-dx1^2, eps = 1/100): v is not a time function for the perturbed metrics",
          all(s_[1] and s_[2] for s_ in signs) and {signs[0][0], signs[1][0]} == {1, -1},
          str([str(s_[0]) for s_ in signs]))
    gv = sp.simplify(GB0I*dv)
    Y = -gv
    check("D2 for g_b0, Y = -grad v is future null and dv(Y) = 0 (exact): the infimum of dv over the future causal "
          "cone is 0 (T1a's sampled 5.7e-2 is an artefact)",
          sp.simplify((Y.T*(ETA + mu/RR**2*KV*KV.T)*Y)[0, 0]) == 0 and sp.simplify((dv.T*Y)[0, 0]) == 0 and Y[0] == 1)
    dt = sp.Matrix([1, 0, 0, 0, 0])
    form = sp.simplify(((dv + ep*dt).T*GB0I*(dv + ep*dt))[0, 0])
    check("D3 g_b0^-1(d(v + eps t), d(v + eps t)) = -2 eps - eps^2 (1 + mu r^-2): margin 2 eps, uniform in r",
          sp.simplify(form + 2*ep + ep**2*(1 + mu/RR**2)) == 0)
    dr = sp.Matrix([0, x1/RR, x2/RR, x3/RR, x4/RR])
    dPhi = dv - dr/RR**2
    formP = sp.simplify((dPhi.T*GB0I*dPhi)[0, 0])
    nE = sp.simplify((dPhi.T*dPhi)[0, 0])
    grad = sp.simplify(GB0I*dPhi)
    check("D4 Phi_W := v + 1/r: g_b0^-1(dPhi, dPhi) = -2 r^-2 + r^-4 (1 - mu r^-2), |dPhi|_E^2 = 1 + (1 - r^-2)^2, and "
          "-grad Phi_W has positive t-component (future directed) (exact)",
          sp.simplify(formP - (-2/RR**2 + (1 - mu/RR**2)/RR**4)) == 0 and sp.simplify(nE - 1 - (1 - 1/RR**2)**2) == 0
          and sp.simplify(-grad[0] - (1 + mu/RR**4)) == 0)
    rng = random.Random(12)
    worst, ctl = -1e9, -1e9
    for _ in range(2000):
        r_ = rng.uniform(4, 400)
        m_ = rng.uniform(0.2, 2)
        x = np.array([rng.gauss(0, 1) for _ in range(4)])
        xh = x/np.linalg.norm(x)
        k = np.concatenate(([1.0], xh))
        g0i = np.diag([-1.0, 1, 1, 1, 1]) - m_/r_**2*np.outer(np.diag([-1.0, 1, 1, 1, 1])@k,
                                                             np.diag([-1.0, 1, 1, 1, 1])@k)
        A = np.array([[rng.uniform(-1, 1) for _ in range(5)] for _ in range(5)])
        D = (A + A.T)/2
        D /= max(abs(np.linalg.eigvalsh(D)))
        dP = np.concatenate(([1.0], (1 - 1/r_**2)*xh))
        worst = max(worst, (dP@(g0i + 0.5/r_**2*D)@dP)*r_**2)
        ctl = max(ctl, (dP@(g0i + 2.0/r_**2*D)@dP)*r_**2)
    check("D5 (g_b0^-1 + delta)(dPhi, dPhi) < 0 for |delta|_op <= r^-2/2 (2000 points, r in [4, 400]; bound "
          "-r^-2 + r^-4 "
          "deduced in D4)", worst < 0, f"max r^2 g^-1(dPhi, dPhi) = {worst:.3f}")
    check("D5' control: |delta|_op = 2 r^-2 makes dPhi_W spacelike somewhere", ctl > 0, f"max {ctl:.3f}")


# ================================================================ E: the weight's u* (round 4, m3)

def part_e():
    print("E  the weight on W: u* := sup f + 1 (round 4, m3)")
    rng = random.Random(21)
    R4 = 40.0
    ok, bad_old, worst_hi = True, False, 0
    for _ in range(20):
        c = [rng.uniform(-3, 3) for _ in range(3)]
        f = lambda r: c[0] + c[1]*R4/r + c[2]*(R4/r)**2/2  # f' = O(r^-2), |f'| <= 1/2 on r >= 4R
        fs = [f(R4*(1 + i/20)) for i in range(4000)]
        supf = max(fs + [c[0]])  # f -> c[0] as r -> oo
        v1 = f(R4) + R4
        ustar, ustar_old = supf + 1, 2*supf - v1 + 1
        for _ in range(200):
            r = R4*(1 + rng.random()*50)
            tmax = f(r)
            tmin = v1 - r
            if tmin > tmax:
                continue
            tt = tmin + rng.random()*(tmax - tmin)
            u = tt - r
            ok = ok and (r + 1 <= ustar - u + 1e-6) and (ustar - u <= 2*r + abs(ustar - v1) + 1e-9)
            bad_old = bad_old or (ustar_old - u < r)
            worst_hi = max(worst_hi, (ustar - u)/r)
    check("E1 r + 1 <= u* - u <= 2r + |u* - v1| on W (20 random f, 4000 points)", ok, f"max (u* - u)/r = {worst_hi:.3f}")
    check("E1' control (round 4's u* = 2 sup f - v1 + 1): r <= u* - u fails", bad_old)


# ================================================================ F: the localised energy argument (round 4, M4)

def part_f():
    import numpy as np
    print("F  the localised energy argument on W (round 4, M4)")
    rng = random.Random(31)
    worst, ctl = 1e9, 1e9
    for _ in range(2000):
        r_ = rng.uniform(4, 400)
        m_ = rng.uniform(0.2, 2)
        x = np.array([rng.gauss(0, 1) for _ in range(4)])
        xh = x/np.linalg.norm(x)
        k = np.concatenate(([1.0], xh))
        g0 = np.diag([-1.0, 1, 1, 1, 1]) + m_/r_**2*np.outer(k, k)
        A = np.array([[rng.uniform(-1, 1) for _ in range(5)] for _ in range(5)])
        H = (A + A.T)/2
        H /= max(abs(np.linalg.eigvalsh(H)))
        g = g0 + 0.5/r_**2*H
        gi = np.linalg.inv(g)
        X = np.array([1.0, 0, 0, 0, 0])
        dP = np.concatenate(([1.0], (1 - 1/r_**2)*xh))
        # [R6 (m4)] T_g[phi](X, n) = (p.X)(p.n) - (1/2) g(X, n) g^-1(p, p) is the quadratic form p^T Q p of the
        # covector p = d phi; its minimum over |p|_E = 1 is the least eigenvalue of Q, taken exactly (round 5 sampled
        # three random p, which could not fail: the verifier's mutations Phi = v - 1/r and |H| = 6 r^-2 passed)
        n = -gi@dP

        def qform(nn):
            return (np.outer(X, nn) + np.outer(nn, X))/2 - 0.5*(X@g@nn)*gi
        worst = min(worst, np.linalg.eigvalsh(qform(n))[0]*r_**2)
        dr_ = np.concatenate(([0.0], xh))
        nr = gi@dr_
        ctl = min(ctl, np.linalg.eigvalsh(qform(nr))[0])
    check("F1 the flux T(d_t, -grad Phi_W) through {Phi_W = V_*} is >= 0: its minimum over the covector d phi, the "
          "least eigenvalue of the quadratic form, is positive at 2000 points (g = g_b0 + H, |H|_op <= r^-2/2): that "
          "boundary is spacelike and its flux can be dropped", worst > 0, f"min over points of r^2 lambda_min = "
          f"{worst:.4f}")
    check("F1' control (the normal grad r of a timelike cut-off {r = R} in place of -grad Phi_W): negative somewhere",
          ctl < 0, f"min {ctl:.3e}")
    # [R6 (m4)] the sign, exactly: in a g-orthonormal frame with X = e_0 and n = (cosh s, sinh s, 0, 0, 0) (two
    # future timelike vectors span such a frame; congruence preserves definiteness) the form has the eigenvalues
    # e^s/2, e^-s/2 and cosh(s)/2 (three times): positive definite; for n spacelike, (sinh s, cosh s, 0, 0, 0), it
    # has the eigenvalue (sinh s - cosh s)/2 < 0
    sv = sp.Symbol("s", real=True)
    etaI = sp.diag(-1, 1, 1, 1, 1)
    e0 = sp.Matrix([1, 0, 0, 0, 0])

    def qsym(nn):
        gxn = (e0.T*sp.diag(-1, 1, 1, 1, 1)*nn)[0]
        return (e0*nn.T + nn*e0.T)/2 - gxn*etaI/2
    lm = sp.Symbol("lambda")

    def charpoly_is(nn, roots):
        cp = (qsym(nn) - lm*sp.eye(5)).det()
        tgt = sp.Mul(*[(rt - lm) for rt in roots])
        return sp.simplify(sp.expand((cp - tgt).rewrite(sp.exp))) == 0
    ok_t = charpoly_is(sp.Matrix([sp.cosh(sv), sp.sinh(sv), 0, 0, 0]),
                       [sp.exp(sv)/2, sp.exp(-sv)/2] + [sp.cosh(sv)/2]*3)
    ok_s = charpoly_is(sp.Matrix([sp.sinh(sv), sp.cosh(sv), 0, 0, 0]),
                       [sp.exp(sv)/2, -sp.exp(-sv)/2] + [sp.sinh(sv)/2]*3)
    okx, negs = ok_t, [-sp.exp(-sv)/2] if ok_s else []
    ev_t, ev_s = "e^s/2, e^-s/2, cosh(s)/2 (x3)", "e^s/2, -e^-s/2, sinh(s)/2 (x3)"
    check("F1x (exact) for X = e_0, n = (cosh s, sinh s, 0, 0, 0) the form p -> T(X, n) has eigenvalues e^s/2, e^-s/2, "
          "cosh(s)/2 (x3), all > 0: T(X, n) >= 0 for X, n future timelike, the dominant energy condition; control: n "
          "spacelike, (sinh s, cosh s, 0, 0, 0), gives a negative eigenvalue", okx and len(negs) >= 1,
          f"timelike n: {ev_t}; spacelike n: {ev_s} (characteristic polynomials, exact)")
    tt, rr = sp.symbols("tt rr", positive=True)
    t1, t2, R1, R2 = 0, sp.Rational(1, 2), 2, 6
    phi = 1 + tt*rr + tt**2 - rr**2/7 + tt*rr**2/5 + rr**3/30
    box = -sp.diff(phi, tt, 2) + sp.diff(phi, rr, 2) + 3*sp.diff(phi, rr)/rr
    e = (sp.diff(phi, tt)**2 + sp.diff(phi, rr)**2)/2*rr**3
    E1 = sp.integrate(e.subs(tt, t1), (rr, R1, R2))
    E2 = sp.integrate(e.subs(tt, t2), (rr, R1 + t2 - t1, R2 - (t2 - t1)))
    s = sp.Symbol("s")
    # inner boundary r = R1 + (t - t1) (outgoing): tangential d_t + d_r; outer r = R2 - (t - t1): d_t - d_r
    fin = sp.integrate(((sp.diff(phi, tt) + sp.diff(phi, rr))**2/2*rr**3).subs({tt: s, rr: R1 + s - t1}), (s, t1, t2))
    fout = sp.integrate(((sp.diff(phi, tt) - sp.diff(phi, rr))**2/2*rr**3).subs({tt: s, rr: R2 - (s - t1)}),
                        (s, t1, t2))
    bulk = sp.integrate(sp.integrate(sp.expand(sp.diff(phi, tt)*box*rr**3), (rr, R1 + tt - t1, R2 - (tt - t1))),
                        (tt, t1, t2))
    ok = sp.simplify(E2 + fin + fout - (E1 - bulk)) == 0
    finx = sp.integrate(((sp.diff(phi, tt) - sp.diff(phi, rr))**2/2*rr**3).subs({tt: s, rr: R1 + s - t1}),
                        (s, t1, t2))
    ctlF = sp.simplify(E2 + finx + fout - (E1 - bulk)) != 0
    check("F2 the domain-of-dependence identity on a truncated diamond (flat radial model, exact): E(t2) + inner and "
          "outer null fluxes (tangential derivatives, each >= 0) = E(t1) - int int phi_t box phi r^3", ok,
          f"E(t2) + fluxes = {sp.N(E2 + fin + fout, 12)}")
    check("F2' control (the transverse derivative in the inner flux): the identity fails", ctlF)
    a, R, Rp, eta = sp.symbols("a R Rp eta", positive=True)
    rr_ = sp.Symbol("r", positive=True)
    Ff = sp.Function("F")
    s1 = sp.diff(rr_**(2*a + 3)*Ff(rr_)**2, rr_) - ((2*a + 3)*rr_**(2*a + 2)*Ff(rr_)**2
                                                   + 2*rr_**(2*a + 3)*Ff(rr_)*sp.diff(Ff(rr_), rr_))
    hd = sp.diff(rr_**(2*a + 2)*Ff(rr_)**2/(2*a + 2), rr_) - (rr_**(2*a + 1)*Ff(rr_)**2
                                                           + rr_**(2*a + 2)*Ff(rr_)*sp.diff(Ff(rr_), rr_)/(a + 1))
    check("F3 the identities behind S1 and Hardy on [R, R']: d(r^(2a+3) F^2) = (2a+3) r^(2a+2) F^2 + "
          "2 r^(2a+3) F F' and "
          "d(r^(2a+2) F^2/(2a+2)) = r^(2a+1) F^2 + r^(2a+2) F F'/(a+1) (exact), with the boundary terms at R' kept",
          sp.simplify(s1) == 0 and sp.simplify(hd) == 0)
    Fg = rr_**(-a - 2 - eta)
    I = sp.integrate(rr_**(2*a + 3)*Fg**2, (rr_, 1, sp.oo), conds="none")
    lim = sp.limit((Rp**(2*a + 4)*Fg.subs(rr_, Rp)**2).subs({a: sp.Rational(11, 4), eta: sp.Rational(1, 10)}), Rp,
                   sp.oo)
    Fc = rr_**(-a - 2)
    Ic = sp.integrate((rr_**(2*a + 3)*Fc**2).subs(a, sp.Rational(11, 4)), (rr_, 1, sp.oo))
    check("F3' F = r^(-a-2-eta): int r^(2a+3) F^2 finite and R'^(2a+4) F(R')^2 -> 0 (the boundary terms vanish along "
          "R' -> oo); control F = r^(-a-2): the integral diverges and R'^(2a+4) F^2 = 1",
          sp.simplify(I - 1/(2*eta)) == 0 and lim == 0 and Ic == sp.oo
          and sp.simplify(Rp**(2*a + 4)*Fc.subs(rr_, Rp)**2) == 1)
    Sig2 = rr_**-2
    dens = rr_**(2*a)*sp.diff(Sig2, rr_)**2*rr_**3
    ok4 = all(sp.integrate(dens.subs(a, av), (rr_, 10, sp.oo)) == sp.oo for av in (1, sp.Rational(11, 4))) and \
        sp.integrate(dens.subs(a, sp.Rational(9, 10)), (rr_, 10, sp.oo)).is_finite
    check("F4 the rejected localisation: -Sigma_2 = -r^-2 P beyond V_* has weighted energy int r^(2a-3) dr, infinite at "
          "a = 1, 11/4, finite at a = 9/10 (exact)", ok4)
    Tq = sp.Symbol("T", positive=True)
    for q_src, amax in ((sp.Rational(13, 2), sp.Rational(9, 2)), (6, 4)):
        unweighted_tail = Tq**2*R**(3 - 2*q_src + 1)  # C |T|^2 int_R^oo r^(-2q) r^3 dr up to a constant
        dens_w = rr_**(2*a)*(-sp.diff(unweighted_tail.subs(R, rr_), rr_))
        fin_ok = [sp.integrate(dens_w.subs(a, av), (rr_, 1, sp.oo)).is_finite
                  for av in (amax - sp.Rational(1, 10), amax)]
        if q_src == sp.Rational(13, 2):
            okF5 = fin_ok == [True, False]
        else:
            ctlF5 = fin_ok == [True, False]
    check("F5 finite speed: the exterior energy beyond R is <= C |T|^2 R^-9 for the source O(r^(-13/2)), and its "
          "weighted integral converges exactly for a < 9/2 (exact at a = 4.4, 4.5)", okF5)
    check("F5' control (source O(r^-6), Sigma without F_4): exactly a < 4", ctlF5)


# ================================================================ G: the fields, the caps, the tails, the window

L_HARM = 2


def flat_truth(cs, vv, kmax=9):
    """the after-shell coefficients G_k(v), k = 4..kmax, from the flat recursion with G_3 = 0 and data cs at v1"""
    v1 = sp.Rational(7, 10)
    G = {2: sp.Integer(0), 3: sp.Integer(0)}
    for k in range(4, kmax + 1):
        q = sp.Rational(k, 2)
        rhs = (-L_HARM*(L_HARM + 2) + (q - 1)*(q - 3))*G[k - 2]/(2*q - 3)
        G[k] = cs[k] + sp.integrate(rhs.subs(vv, sp.Symbol("w")), (sp.Symbol("w"), v1, vv))
    return G


def sigma_coeffs(cs, vv, Pi, kmax=10):
    """the coefficients of r^(-k/2) of Sigma at fixed v (exact Taylor coefficients of the 2F1)"""
    v1 = sp.Rational(7, 10)
    out = {k: sp.Integer(0) for k in range(4, kmax + 1)}
    l = L_HARM
    for p in Pi:
        a_, b_, c_ = p + l, p - l - 2, p - sp.Rational(1, 2)
        m = 0
        while 2*(p + m) <= kmax:
            coef = sp.rf(a_, m)*sp.rf(b_, m)/(sp.rf(c_, m)*sp.factorial(m))/2**m
            out[int(2*(p + m))] += cs[int(2*p)]*coef*(vv - v1)**m
            m += 1
    return out


def hR_func(cs, Pi, c10):
    """h_R(v, r) := sum_(k=4)^(10) r^(-k/2) G_k(v) - Sigma(v, r), G_10 := c10 + v (arbitrary), as an mpmath function"""
    vv = sp.Symbol("vv")
    G = flat_truth(cs, vv)
    G[10] = c10 + vv
    l = L_HARM
    Gf = {k: sp.lambdify(vv, G[k], "mpmath") for k in range(4, 11)}
    v1 = mp.mpf("0.7")

    def h(v, r):
        s = (v - v1)/r
        tru = sum(r**(-mp.mpf(k)/2)*Gf[k](v) for k in range(4, 11))
        sig = sum(r**(-mp.mpf(p))*cs[int(2*p)]*mp.hyp2f1(p + l, p - l - 2, p - mp.mpf(1)/2, s/2) for p in Pi)
        return tru - sig
    return h


def part_g():
    print("G  the fields after the shell: h_R, the caps, the N-flux tails, the window (rounds 3-4)")
    rnd = random.Random(41)
    cs = {k: sp.Rational(rnd.randint(1, 9), rnd.randint(1, 5))*rnd.choice([1, -1]) for k in range(4, 10)}
    vv = sp.Symbol("vv")
    Pi = [sp.Integer(2), sp.Rational(5, 2), sp.Integer(3), sp.Rational(7, 2), sp.Integer(4)]
    Pi7 = Pi[:-1]
    G = flat_truth(cs, vv)
    S5 = sigma_coeffs(cs, vv, Pi, kmax=9)
    S7 = sigma_coeffs(cs, vv, Pi7, kmax=9)
    diff5 = {k: sp.expand(G[k] - S5[k]) for k in range(4, 10)}
    diff7 = {k: sp.expand(G[k] - S7[k]) for k in range(4, 10)}
    check("G1 at fixed v the r^(-k/2) coefficients of truth - Sigma vanish for k = 4..8 and equal c_9 at k = 9 (exact, "
          "l = 2): h_R = O(r^(-9/2))", all(diff5[k] == 0 for k in range(4, 9)) and diff5[9] == cs[9],
          str({k: str(v) for k, v in diff5.items()}))
    check("G1' control (p = 4 dropped from Sigma): the r^-4 coefficient survives", diff7[8] != 0, str(diff7[8]))
    mp.mp.dps = 60
    c10 = sp.Rational(3, 7)
    h5, h7 = hR_func(cs, Pi, c10), hR_func(cs, Pi7, c10)
    v1, V, dl = mp.mpf("0.7"), mp.mpf("1.7"), mp.mpf("0.5")

    def chi(v):
        if v <= V:
            return mp.mpf(0)
        x = (v - V)/dl
        return 3*x**2 - 2*x**3 if x < 1 else mp.mpf(1)

    def cap(h, T, a):
        def dens(v):
            r = v - T
            c = 1 - chi(v)
            hv = h(v, r)
            ht = mp.diff(lambda vv_: h(vv_, r), v)               # d_t at fixed x = d_v at fixed r
            hr = mp.diff(lambda rr_: (1 - chi(rr_ + T))*h(rr_ + T, rr_), r)  # d_r of the cut data at fixed t
            return (2*r)**(2*a)*((c*ht)**2 + hr**2 + L_HARM*(L_HARM + 2)*(c*hv)**2/r**2)*r**3
        return mp.quad(dens, [v1, V, V + dl])

    def tail_exp(Pi_, av):
        """the N-flux tail beyond R of h_R(v1, r), exactly (sympy): its leading power of R"""
        rS, RS = sp.symbols("rS RS", positive=True)
        v1s = sp.Rational(7, 10)
        Gv1 = {k: flat_truth(cs, vv)[k].subs(vv, v1s) for k in range(4, 10)}
        Gv1[10] = c10 + v1s
        ph = sum(rS**sp.Rational(-k, 2)*Gv1[k] for k in range(4, 11)) - sum(rS**(-p)*cs[int(2*p)] for p in Pi_)
        dens = sp.expand((2*rS)**(2*av)*(sp.diff(ph, rS)**2 + L_HARM*(L_HARM + 2)*ph**2/rS**2)*rS**3)
        tl = sp.integrate(dens, (rS, RS, sp.oo), conds="none")
        lead_ = sp.limit(sp.log(tl)/sp.log(RS), RS, sp.oo)
        return lead_

    Ts = [mp.mpf(10)**4, mp.mpf(10)**5, mp.mpf(10)**6]
    ok2, ok2c, ok3, ok3c, info = True, True, True, True, []
    for a in (mp.mpf("2.2"), mp.mpf("2.75"), mp.mpf("2.95")):
        e5 = [cap(h5, -T, a) for T in Ts]
        s5 = float(mp.log(e5[2]/e5[1])/mp.log(10))
        e7 = [cap(h7, -T, a) for T in Ts]
        s7 = float(mp.log(e7[2]/e7[1])/mp.log(10))
        aq = sp.nsimplify(str(a))
        q5 = float(tail_exp(Pi, aq))
        q7 = float(tail_exp(Pi7, aq))
        info.append((float(a), round(s5, 3), round(s7, 3), round(q5, 3), round(q7, 3)))
        ok2 = ok2 and abs(s5 - (2*float(a) - 6)) < 0.02
        ok2c = ok2c and abs(s7 - (2*float(a) - 5)) < 0.02
        ok3 = ok3 and abs(q5 - (2*float(a) - 7)) < 0.02
        ok3c = ok3c and abs(q7 - (2*float(a) - 6)) < 0.02
    check("G2 the cap energy of the truncation has fitted exponent 2a - 6 in |T| (a = 2.2, 2.75, 2.95; T = -1e5, -1e6): "
          "-> 0 exactly for a < 3", ok2, "(a, cap, cap w/o p=4, tail, tail w/o p=4) " + str(info))
    check("G2' control (p = 4 dropped): exponent 2a - 5 (-> 0 only for a < 5/2)", ok2c)
    check("G3 the N-flux tail beyond |T| has fitted exponent 2a - 7 (finite flux and vanishing tail for a < 7/2)", ok3)
    check("G3' control (p = 4 dropped): 2a - 6", ok3c)
    # G4: the class on S, exact on rho^beta
    a_, b_, l0 = sp.symbols("a beta l0", positive=True)
    rho = sp.Symbol("rho", positive=True)
    ok4 = True
    for av, l0v in ((sp.Rational(11, 4), sp.Rational(37, 10)), (sp.Rational(23, 10), sp.Rational(31, 10)),
                    (sp.Rational(21, 10), sp.Rational(31, 10))):
        bnorm = sp.integrate((rho**(-l0v)*rho**(av + 1 + sp.Rational(1, 1000)))**2/rho, (rho, 0, 1))
        ok4 = ok4 and (bnorm.is_finite == (av + 1 + sp.Rational(1, 1000) > l0v))
    check("G4 rho^(a + 1 + 1/1000) (the S-energy's class, scale5 Z8a) lies in rho^(l0) L^2_b exactly when a + 1 >= l0 "
          "(three cases, one failing as it must)", ok4)
    # G5: the window from the computed exponents
    def window(l0v, cap_exp, ptw=False):
        good = []
        for n in range(0, 401):
            av = Fr(n, 100)
            rows = [Fr(3) + 0*av, Fr(3), Fr(2), Fr(3, 2) + av, av + HALF, Fr(9, 2) - av]  # O1's and (R4b)'s, residual
            ker = all(q > 1 for q in rows)
            capok = cap_exp(av) < 0
            nflux = 2*av - 7 < 0
            scls = (av > l0v - HALF) if ptw else (av + 1 > l0v)
            if ker and capok and nflux and scls:
                good.append(av)
        return (min(good), max(good)) if good else None
    ok5, ctl5a, ctl5b, info5 = True, True, True, {}
    for l0v in (Fr(31, 10), Fr(33, 10), Fr(36, 10), Fr(39, 10)):
        w = window(l0v, lambda av: 2*av - 6)
        info5[str(l0v)] = (str(w[0]), str(w[1])) if w else None
        ok5 = ok5 and w is not None and w[0] == l0v - 1 + Fr(1, 100) and w[1] == Fr(299, 100)
        wa = window(l0v, lambda av: 2*av - 5)
        wb = window(l0v, lambda av: 2*av - 6, ptw=True)
        if l0v >= Fr(7, 2):
            ctl5a = ctl5a and wa is None
            ctl5b = ctl5b and wb is None
    check("G5 the admissible weights on the grid are (l0 - 1, 3) for l0 = 3.1, 3.3, 3.6, 3.9 (no lower bound 5/2)", ok5,
          str(info5))
    check("G5' controls: p = 4 dropped (cap 2a - 5), or the pointwise reading on S (a > l0 - 1/2): no weight for "
          "l0 >= 7/2", ctl5a and ctl5b)
    # the h_R rows' exponents from S1 and Hardy (computed from the scaling of the inequalities)
    R_, c_ = sp.symbols("R c", positive=True)
    F_ = R_**(-c_)
    lhs = R_**(2*a_ + 3)*F_**2
    crit = sp.solve(sp.Eq(sp.diff(sp.log(lhs), R_)*R_, 0), c_)
    check("G5'' S1's left side R^(2a+3) F(R)^2 is scale-invariant exactly at F ~ R^(-a-3/2): |d h_R| <= eps r^(-3/2-a), "
          "so the first-order h_R row has q = 3/2 + a and, with Hardy (one power of r), the zero-order row a + 1/2",
          crit == [a_ + sp.Rational(3, 2)], str(crit))
    # G6: Sigma|_S, by the explicit Taylor composition F_p(1 + d(rho)) = sum_m F_p^(m)(1) d(rho)^m/m!, d(rho) :=
    # (f_oo - v1) rho + f_2 rho^3, F_p^(m)(s) = (a)_m (b)_m/((c)_m 2^m) 2F1(a + m, b + m; c + m; s/2) (mpmath)
    f_inf, f2 = sp.Rational(-3, 4), sp.Rational(5, 2)
    v1s = sp.Rational(7, 10)
    exps = set()
    mp.mp.dps = 30
    for p in Pi + [sp.Rational(9, 4)]:
        a1, b1, c1 = p + L_HARM, p - L_HARM - 2, p - sp.Rational(1, 2)
        dl_ = (f_inf - v1s)*rho + f2*rho**3
        ser = 0
        for m in range(0, 4):
            A_, B_, C_ = [mp.mpf(x.p)/x.q for x in (a1, b1, c1)]
            # the 2F1 at z = 1/2 by its series (geometric convergence; exact for the terminating cases)
            f21 = mp.nsum(lambda n: mp.rf(A_ + m, n)*mp.rf(B_ + m, n)/(mp.rf(C_ + m, n)*mp.factorial(n))/2**n,
                          [0, 400], method="direct")
            dm = mp.rf(A_, m)*mp.rf(B_, m)/(mp.rf(C_, m)*2**m)*f21
            ser += sp.Float(str(dm), 25)*dl_**m/sp.factorial(m)
        poly = sp.Poly(sp.expand(ser), rho)
        for (deg,), cf in zip(poly.monoms(), poly.coeffs()):
            if deg <= 3 and abs(cf) > 1e-20:
                exps.add((p, p + deg))
    ok6 = all(((2*e_).is_integer and e_ >= 2) for p, e_ in exps if p != sp.Rational(9, 4))
    ctl6 = any(not (2*e_).is_integer for p, e_ in exps if p == sp.Rational(9, 4))
    check("G6 Sigma|_S: rho^p F_p(1 + (f_oo - v1) rho + f_2 rho^3) has exponents p + j, all in E_0^(1/2) (Taylor "
          "composition to rho^(p+3), coefficients by mpmath)", ok6,
          str(sorted({str(e_) for p, e_ in exps if p != sp.Rational(9, 4)})[:10]))
    check("G6' control (a p = 9/4 term): exponents outside E_0^(1/2)", ctl6)


# ================================================================ H: the means' exponents (round 4, m7)

def part_h():
    print("H  the means at past null infinity: inputs from Theorem A_P's coefficient classes (round 4, m7)")

    def orders(lead, top=20):
        return {lead + Fr(j, 2) for j in range(0, 2*top)}

    def inputs(dvphi_class):
        unk = {"m": orders(Fr(2)), "Psi": orders(Fr(2)), "lphi": orders(Fr(2)), "phi": orders(Fr(1)),
               "dvphi": orders(Fr(1)), "Omphi": orders(Fr(2)), "dphi": orders(Fr(1)), "gh": orders(Fr(2))}
        known = orders(Fr(3))
        c_in = set(known)
        for name, cls in (("m", Fr(3, 2)), ("Psi", Fr(3, 2)), ("lphi", Fr(3, 2)), ("dvphi", dvphi_class),
                          ("Omphi", Fr(5, 2))):
            c_in |= {cls + o for o in unk[name]}
        a_in = set(known)
        for name, cls in (("m", Fr(2)), ("dphi", Fr(3)), ("gh", Fr(3, 2))):
            a_in |= {cls + o for o in unk[name]}
        b_in = orders(Fr(2))
        return a_in, b_in, c_in

    a_in, b_in, c_in = inputs(Fr(5, 2))
    ok = (min(a_in) >= 3 and min(c_in) >= 3 and min(b_in) >= 2 and Fr(5, 2) not in a_in | c_in and 1 not in b_in)
    check("H1 every input of (a) and (c) has exponent >= 3, of (b) >= 2: 2/(2q - 5), 1/(q - 5/2), 1/(q - 1) finite at "
          "every order to 20 (no logarithm)", ok, f"min (a) {min(a_in)}, (b) {min(b_in)}, (c) {min(c_in)}")
    a_m, b_m, c_m = inputs(Fr(3, 2))
    check("H1' control (the code mutated: d_v phi_m's coefficient class E_(3/2) in (c)): an input at q = 5/2 appears",
          Fr(5, 2) in c_m)


def main():
    for f in (part_a, part_b, part_c, part_d, part_e, part_f, part_h, part_g):
        f()
    print("FAILED:", FAIL if FAIL else "none")
    return 1 if FAIL else 0


if __name__ == "__main__":
    sys.exit(main())
