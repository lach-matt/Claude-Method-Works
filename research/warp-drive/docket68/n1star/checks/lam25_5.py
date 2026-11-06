#!/usr/bin/env python3
"""lam25_5.py -- the threshold lambda_25(delta) of Proposition L.25'' (a) as a certified formula in the record's
constants (EQUALITY5-LAYER.md, Round 8, R8.3).

L.25' (a)'s proof (R6.2, R7.4) bounds, at lam = 10^(-E), every term of g_lam^-1(dPhi0, dPhi0) + m0 on J_n' against m0's
lower bound m0lb = (2 A^2/(27 mu0)) h_n^2 s_n^(-1) I_beta (A34; I_beta := int beta^2), with n the least index with h_n =
e^(-n^2) <= lam^(3+delta), s_n = 2^(n+2), eps_k(v_1) <= 2 h_n s_n^k B_k, B_k := max_(i<=k) sup|beta^(i)|:

  (W1) Theorem 1's remainder, L.4':  C_w lam^(N-5) eps_(M*)/m0lb,           N = K + 3, M* = 2N + 8;
  (M1) its means, L.3 (b):           C_m sum_(j<=N) lam^j eps_(2j)^2/m0lb;
  (W2), (M2) Theorem 2's:            C_wP lam^(N_P-3) eps_(M_P)/m0lb, and the means to j <= N_P, N_P = K + 12, M_P =
                                     2 N_P + 8 (beta_P = 2, as T6);
  (H1) L.4''s hypothesis eps_4(v_1) <= lam;  (H2) L.4_P's eps_(M_P)(v_1) <= lam^3;
  (Lh) lam <= lam_h(delta), so h_n >= lam^(3.4+delta) (R7.4);  (Tl) e^(2n+1) >= 2^(M_P+1) (the bumps m > n, R6.2 (2));
  (J)  J_n' longer than 4 pi lam: 2^(-n-2) - rho_w >= 4 pi lam with rho_w <= C_rho lam.

The record's constants enter only through gamma_w := log10(C_w mu0/A^2), gamma_m := log10(C_m mu0/A^2), gamma_wP and
log10(4 pi + C_rho), where C_w := C_L1 C_L4 (Lemma L.1's constant times L.4''s), C_m := C_L1 C_L3 (L.3 (b)), C_wP :=
C_L1 C_L4P (L.4_P).  With s := sqrt((3 + delta) ln 10), n + 2 <= s sqrt(E) + 3 and lam_h's bound h_n >= lam^(3.4+delta),
each condition reads -a E + b sqrt(E) + c + gamma <= log10 tau, and holds for every E >= E_i := y_+^2, y_+ := (b +
sqrt(b^2 + 4 a (c + gamma - log10 tau)))/(2a) (all E when the discriminant is negative): tau = 1/4 for (W1), (W2), 1/(4
N) per j for (M1) (1/(4 N_P) for (M2)), 1 for the hypotheses.  So

    lambda_25(delta) := min(lam_rec, 10^(-E_25)),   E_25 := max_i E_i(delta, gamma_i),

lam_rec the record's threshold for g_lam and Lemmas L.3 (b), L.4', L.4_P (lambda0's, unevaluated).  The coefficients a,
b, c are certified: B_k <= B_k+ := max_(i<=k) (2i/e)^(2i) ||p_i||_1 (beta^(i) = e^(-1/u) p_i(t)/u^(2i), u = 1 - t^2,
e^(-1/u) u^(-2i) <= (2i/e)^(2i), |p_i| <= ||p_i||_1 on [-1, 1]; B_0 = 1/e), I_beta >= a right-endpoint Riemann sum
(beta^2 decreasing on [0, 1)), interval arithmetic throughout (mpmath.iv).

  L1 (certified) the coefficients (a, b, c) of every condition and E_i at gamma = 0 (unit constants), delta = 1/10 and
     1/2, K = 6; E_25 and which condition binds; the formula in gamma for the binding ones.
  L2 (certified formula, evaluated) the illustration of R5.5 (every leaf 1, lambda0 = 0.00244: log10 C_L4 ~ 1.8*10^6,
     log10 C_L11 ~ 1.8*10^5): E_25 with gamma_w = 1.8*10^6 and the other gammas 0.
  L3 (computed, a consistency check) at 200 points E_25 (1 + i/50), i = 0..199, every condition evaluated directly with
     the actual n, h_n and B_k+ (no bound on n or h_n): all hold.  Control: the s_n bound halved in the formula (n + 2 <=
     (s sqrt(E) + 3)/2, a lost factor): at the mutated threshold the direct evaluation finds a violated condition.

Labels: L1, L2 certified (interval arithmetic); L3 computed (mpmath), a check on finitely many E.
Run: python3 checks/lam25_5.py   (about a minute)
"""
import sys
import textwrap

import mpmath as mp
import sympy as sp

iv = mp.iv
iv.dps = 50
mp.mp.dps = 50
L2 = iv.log(2)/iv.log(10)
LN10 = iv.log(10)


def out(msg):
    print(textwrap.fill(msg, width=121, subsequent_indent="      ", break_on_hyphens=False), flush=True)


def lg(x):
    return iv.log(x)/LN10


def up(p, d=4):
    with mp.workdps(50):
        return mp.nstr(mp.ceil(mp.mpf(p._mpi_[1])*10**d)/10**d, 15)


def dn(p, d=6):
    with mp.workdps(50):
        return mp.nstr(mp.floor(mp.mpf(p._mpi_[0])*10**d)/10**d, 15)


def mid(p):
    with mp.workdps(50):
        return mp.nstr((mp.mpf(p._mpi_[0]) + mp.mpf(p._mpi_[1]))/2, 7)


# ------------------------------------------------------------------------------------------------------------ inputs
def bump_bounds(kmax):
    """log10 B_k+ for k <= kmax (certified upper bounds)"""
    t = sp.Symbol('t')
    p = sp.Poly(1, t)
    single = []
    for k in range(kmax + 1):
        if k == 0:
            single.append(-1/LN10)
        else:
            l1 = sum(abs(int(co)) for co in p.all_coeffs())
            single.append(2*k*lg(iv.mpf(2*k)/iv.e) + lg(iv.mpf(l1)))
        p = sp.Poly(sp.expand((1 - t**2)**2*sp.diff(p.as_expr(), t) + (4*k*t*(1 - t**2) - 2*t)*p.as_expr()), t)
    B = []
    for k in range(kmax + 1):
        m = single[0]
        for x in single[1:k + 1]:
            m = iv.mpf([max(m.a, x.a), max(m.b, x.b)])
        B.append(m)
    return B


def ibeta_lower(m=2000):
    tot = iv.mpf(0)
    for i in range(1, m):
        x = iv.mpf(i)/m
        tot += iv.exp(-2/(1 - x*x))
    return (2*tot/m).a


def conditions(delta, K, lB, Ib, halve=False):
    """[(name, a, b, c, log10 tau)]: -a E + b sqrt(E) + c + gamma <= log10 tau"""
    N, NP = K + 3, K + 12
    Ms, MP = 2*N + 8, 2*NP + 8
    s = iv.sqrt((3 + delta)*LN10)
    f = iv.mpf(1)/2 if halve else 1                       # the control's lost factor in n + 2 <= s sqrt(E) + 3
    lt4 = -lg(iv.mpf(4))
    cs = []
    cs.append(("W1", N - iv.mpf('8.4') - delta, f*(Ms + 1)*s*L2, lg(27/Ib) + lB[Ms] + f*3*(Ms + 1)*L2, lt4))
    for j in range(1, N + 1):
        cs.append(("M1_j%d" % j, iv.mpf(j), f*(4*j + 1)*s*L2, lg(54/Ib) + 2*lB[2*j] + f*3*(4*j + 1)*L2,
                   lt4 - lg(iv.mpf(N))))
    cs.append(("H1", 2 + delta, f*4*s*L2, L2 + lB[4] + f*12*L2, iv.mpf(0)))
    cs.append(("W2", NP - 3 - iv.mpf('3.4') - delta, f*(MP + 1)*s*L2, lg(27/Ib) + lB[MP] + f*3*(MP + 1)*L2, lt4))
    for j in range(1, NP + 1):
        cs.append(("M2_j%d" % j, iv.mpf(j), f*(4*j + 1)*s*L2, lg(54/Ib) + 2*lB[2*j] + f*3*(4*j + 1)*L2,
                   lt4 - lg(iv.mpf(NP))))
    cs.append(("H2", delta, f*MP*s*L2, L2 + lB[MP] + f*3*MP*L2, iv.mpf(0)))
    cs.append(("J", iv.mpf(1), f*s*L2, f*3*L2, iv.mpf(0)))
    return cs, s


def threshold(a, b, c, ltau, gamma=0):
    C = c + gamma - ltau
    disc = b*b + 4*a*C
    if disc.b < 0:
        return iv.mpf(0)
    disc = iv.mpf([max(disc.a, 0), disc.b])
    y = (b + iv.sqrt(disc))/(2*a)
    return y*y


def special(delta, K):
    """(Lh) and (Tl): the E beyond which they hold"""
    yh = (2*iv.sqrt(3 + delta) + iv.sqrt(4*(3 + delta) + iv.mpf('1.6')))/iv.mpf('0.8')
    Eh = yh*yh/LN10
    MP = 2*(K + 12) + 8
    nmin = ((MP + 1)*iv.log(2) - 1)/2
    Etl = nmin*nmin/((3 + delta)*LN10)
    return [("Lh", Eh), ("Tl", Etl)]


def e25(delta, K, lB, Ib, gammas=None, halve=False):
    gammas = gammas or {}
    cs, _ = conditions(delta, K, lB, Ib, halve)
    rows = [(nm, threshold(a, b, c, lt, gammas.get(nm[:2] if nm[0] == 'M' else nm, 0)), (a, b, c, lt))
            for nm, a, b, c, lt in cs]
    rows += [(nm, E, None) for nm, E in special(delta, K)]
    worst = max(rows, key=lambda x: x[1].b)
    return worst[1], worst[0], rows


# ------------------------------------------------------------------------------------------------------------ direct
def direct_ok(E, delta, K, lB, Ib):
    """every condition at lam = 10^-E with the actual n and h_n (mpmath, not interval)"""
    E = mp.mpf(E)
    d = mp.mpf(delta)
    N, NP = K + 3, K + 12
    Ms, MP = 2*N + 8, 2*NP + 8
    n = int(mp.ceil(mp.sqrt((3 + d)*E*mp.log(10))))
    lh = -n*n/mp.log(10)
    ls = (n + 2)*mp.log10(2)
    lb = [mp.mpf(x._mpi_[1]) for x in lB]
    lib = mp.log10(mp.mpf(Ib._mpi_[0]))
    lm0 = mp.log10(mp.mpf(2)/27) + lib + 2*lh - ls
    le = lambda k: mp.log10(2) + lh + k*ls + lb[k]                                # noqa: E731
    l4 = -mp.log10(4)
    ok = lh >= -(mp.mpf('3.4') + d)*E and lh <= -(3 + d)*E
    ok &= mp.e**(2*n + 1) >= 2**(MP + 1)
    ok &= -(N - 5)*E + le(Ms) - lm0 <= l4
    ok &= all(-j*E + 2*le(2*j) - lm0 <= l4 - mp.log10(N) for j in range(1, N + 1))
    ok &= le(4) <= -E
    ok &= -(NP - 3)*E + le(MP) - lm0 <= l4
    ok &= all(-j*E + 2*le(2*j) - lm0 <= l4 - mp.log10(NP) for j in range(1, NP + 1))
    ok &= le(MP) <= -3*E
    ok &= -(n + 2)*mp.log10(2) >= mp.log10(4*mp.pi) - E
    return bool(ok)


# ------------------------------------------------------------------------------------------------------------ checks
CACHE = {}


def inputs():
    if not CACHE:
        CACHE['lB'] = bump_bounds(2*(6 + 12) + 8)
        CACHE['Ib'] = ibeta_lower()
    return CACHE['lB'], CACHE['Ib']


def l1(control=False):
    lB, Ib = inputs()
    rows_out = []
    for delta in (iv.mpf(1)/10, iv.mpf(1)/2):
        E, nm, rows = e25(delta, 6, lB, Ib)
        top = sorted(rows, key=lambda x: -x[1].b)[:3]
        desc = ", ".join("%s %s" % (r_[0], up(r_[1], 1)) for r_ in top)
        abc = [r_ for r_ in rows if r_[0] in ("W1", "W2", "H2")]
        form = "; ".join("%s: a = %s, b = %s, c = %s" % (r_[0], mid(r_[2][0]), mid(r_[2][1]), mid(r_[2][2]))
                         for r_ in abc)
        rows_out.append("delta = %s: E_25 = %s (binding %s; the three largest E_i: %s); %s"
                        % ("1/10" if delta.a < 0.2 else "1/2", up(E, 1), nm, desc, form))
    out("  L1 unit constants (every gamma = 0), K = 6, log10 B_44+ = %s, I_beta >= %s: " % (up(lB[44], 2), dn(Ib))
        + "; ".join(rows_out))
    return True


def l2(control=False):
    lB, Ib = inputs()
    rows_out = []
    for delta in (iv.mpf(1)/10, iv.mpf(1)/2):
        E, nm, _ = e25(delta, 6, lB, Ib, gammas={"W1": iv.mpf('1.8e6')})
        rows_out.append("delta = %s: E_25 = %s (binding %s)" % ("1/10" if delta.a < 0.2 else "1/2", up(E, 0), nm))
    out("  L2 R5.5's illustration, gamma_w = log10 C_L4 = 1.8*10^6, other gammas 0: " + "; ".join(rows_out)
        + ": with these inputs L.25'' (a) holds for lam <= min(lam_rec, 10^(-E_25))")
    return True


def l3(control=False):
    lB, Ib = inputs()
    good = True
    for delta in (sp.Rational(1, 10), sp.Rational(1, 2)):
        dv = iv.mpf(delta.p)/delta.q
        E, _, _ = e25(dv, 6, lB, Ib, halve=control)
        E0 = mp.mpf(E._mpi_[1])
        okd = all(direct_ok(E0*(1 + mp.mpf(i)/50), float(delta), 6, lB, Ib) for i in range(200))
        good &= okd
    if not control:
        out("  L3 at E_25 (1 + i/50), i = 0..199, both deltas: every condition holds with the actual n and h_n: %s"
            % good)
    return good


def main():
    ok = True
    for name, f in (("L1", l1), ("L2", l2)):
        good = f()
        out("%s %s" % (name, "PASS" if good else "FAIL"))
        ok &= good
    good = l3()
    ctl = l3(control=True)
    out("L3 %s%s" % ("PASS" if good and not ctl else "FAIL", " (control passed)" if ctl else " (control detected)"))
    ok &= good and not ctl
    out("lam25_5: %s" % ("all checks pass, every control fails" if ok else "FAILURES"))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
