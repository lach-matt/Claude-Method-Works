#!/usr/bin/env python3
"""constL5.py -- the constants C_L11 and C_L4 of lam_L as formulas in lambda0's leaves (EQUALITY5-LAYER.md, Round 5,
R5.5).

C_L11 is the constant of Corollary L.11 (the error terms lam^4 eps, lam eps^2, |w| at the boundary) and C_L4 that of
Lemma L.4 (|w| <= C_L4 lam^(N-5) eps_(M*)(v1)).  Their proofs (rounds 2-4) are chains of the same steps as Theorem 1's
lambda0 (CONSTANTS5.md 1.3, 1.5): transports along ell (Lemma L.9 (b): Gronwall e^(M1 L)), energies on Omega_v (Lemma
L.8: Lemma 2.3's constant), the null-face Sobolev step (L.10), Lemma 6.4's radial solve and Proposition 6.5's C0, the
Sobolev constant C_S of Lemma 2.1, Theorem E's M, and sup bounds of the stage profiles and their derivatives.  This
program writes the recursion of Lemma L.3's proof (stages m = 0, ..., N; the constants C^a (oscillating, degree one),
C^b (means and phases), C^c (degree-two remainder), C^e (slice data), C^d (residual), C^U) and Corollary L.11's and
Lemma L.4's assembly as explicit sympy expressions, and checks:

  K1 (computed) every free symbol of C_L11 and C_L4 is a leaf of lambda0's formula (CONSTANTS5 1.3, 1.5: the profile
     bounds P_i := sup |d^i g_j| for i <= 11, C64 (Lemma 6.4), C0 (Proposition 6.5), M (Theorem E), C2 (Lemma 2.3, its
     energy constant), lambda0 itself), a certified number of CONSTANTS5 1.4 (a, b(tau0), tau_end - tau0, mu_end, C_S),
     or a constant of the seed alone (Ks, the bound of the seed's operator coefficients on Omega with two derivatives,
     and C_S3, the Sobolev constant of H^2(S^3) in L^inf): no other quantity enters.  Control: a step that needs a
     profile bound beyond the derivative order lambda0 uses (P_12) is detected.
  K2 (computed) both are increasing in every leaf (expression trees with positive coefficients built by +, *, exp,
     max and positive powers; checked structurally and by finite differences at 200 random positive points).
     Control: a mutated assembly with a difference (C_tr - 1) is detected as not monotone.
  K3 (computed) at P* with the certified leaves inserted, printed in the remaining leaves; with the seed's constants
     and the profile bounds all equal to one (an illustration, not a bound), log10 C_L11 and log10 C_L4 are printed.
     Control: C_S (Lemma 2.1) replaced by 10^-40 makes C_L4 < 1 (the formula is proportional to it).

Labels: the formulas deduced (each from the proof step named beside it); K1-K3 computed.  Run: python3 checks/constL5.py
"""
import random
import sys
import textwrap

import sympy as sp


def out(msg):
    print(textwrap.fill(msg, width=121, subsequent_indent="      ", break_on_hyphens=False), flush=True)


P = sp.symbols('P0:13', positive=True)                    # profile bounds sup |d^i g_j|, i = 0..12
C64, C0, M, C2, lam0 = sp.symbols('C64 C0 M C2 lambda0', positive=True)
a, b, T, mu_end, C_S = sp.symbols('a b T mu_end C_S', positive=True)
Ks, C_S3 = sp.symbols('K_s C_S3', positive=True)
A, mu0 = sp.symbols('A mu0', positive=True)
LEAVES = set(P[:12]) | {C64, C0, M, C2, lam0}
CERT = {a: sp.Rational(269858789, 10**9), b: sp.Rational(13437208254, 10**9), T: sp.Rational(5937208254, 10**9),
        mu_end: sp.Rational(227, 192), C_S: sp.Rational(432158, 10**4), A: 1, mu0: 1}
SEED = {Ks, C_S3}


def build(N=9, mutate=None):
    """the recursion of Lemma L.3's proof and the assemblies of Corollary L.11 and Lemma L.4"""
    top = P[12] if mutate == "P12" else P[6]
    K = Ks + top                                            # coefficient bound of a monomial's factors (F1), (F2)
    M1 = 2*sp.pi*K                                          # Lemma L.9 (b): ||d_th^-1|| <= pi, ||Pi_osc|| <= 2 (D4)
    C_tr = sp.exp(M1*(b - a))                               # Gronwall along ell, L <= b(tau0) - a
    if mutate == "minus":
        C_tr = C_tr - 1
    C_E = C2                                                # Lemma L.8 = Lemma 2.3's constant on Omega_v
    C_N = C_S3*(1 + sp.sqrt(2)*sp.sqrt(b - a)*a**sp.Rational(-3, 2))   # Lemma L.10
    KP = Ks                                                 # ||Pol^+|| and the 'known' coefficients: the seed's
    Ca = {1: A*Ks}                                          # stage 0: W_TT, cost i (ansatz5 A3)
    Cb, Cc, Ce = {}, {1: C_tr*K*(A*Ks)**2}, {}             # chi: transport of a quadratic source (stage 0)
    for m in range(1, N + 1):
        sa = sum(Ca[l] for l in range(1, m + 1))
        sb = sum(Cb[l] for l in range(1, m))
        F2 = K*(sa**2 + sb)                                 # (F2): two oscillating factors, or an earlier mean
        Ce[m] = C64*F2                                      # (e): Lemma 6.4 on [a, r]
        Ca[m + 1] = C_tr*(KP*(top*Ce[m] + K*sa) + (b - a)*K*sa*(1 + sb))                 # (a)
        Cb[m] = C_N*C_E*sp.exp(C_E*T)*(Ce[m] + T*F2 + T*K*Ca[m + 1]*(1 + sa))          # (b): L.8, L.9 (a), L.10
        Cc[m + 1] = C_tr*(K*(Cc[m] + Cb[m] + sa*Ca[m]) + KP*Ce[m])                       # (c)
    sa = sum(Ca.values())
    sb = sum(Cb.values())
    Cd = K**(N + 1)*(1 + sa + sb)**(N + 1)/sp.factorial(N - 2)                            # (d): Taylor in lam
    CU = 2*C0*K*(sa + sb)                                                                # (e) for U: Prop. 6.5
    C_D3 = sp.Rational(2, 9)*A**2/(4*sp.sqrt(mu0))                                       # D3: r_q - sqrt(mu0)
    C_beta = sp.Rational(2, 9)*A**2*(1/(2*mu0) + 1/(4*mu0))                              # D3: |beta0|
    C11 = sp.Max(sum(lam0**(j - 4)*Ca[j] for j in range(4, N + 2)),
                 sum(lam0**(j - 1)*Cc[j] for j in range(1, N + 2)) + lam0**2*Ca[3]*C_D3
                 + 3*C_beta*sum(lam0**(j - 1)*Ca[j] for j in range(1, N + 2)),
                 (1 + C_beta)**2)                                                         # Corollary L.11
    C_coef = C2*(1 + M + K)                                                              # L.4 steps 3-4
    C_dat = CU*(1 + Ks)                                                                  # L.4 step 5
    C4 = C_S*sp.exp(C_coef*T)*(C_dat + T*Cd)                                             # L.4 steps 6-7
    return C11, C4


def leafset(e):
    return e.free_symbols


def k1(control=False):
    C11, C4 = build(mutate="P12" if control else None)
    allowed = LEAVES | set(CERT) | SEED
    extra = (leafset(C11) | leafset(C4)) - allowed
    if control:
        return not extra
    out("  K1 free symbols of C_L11: %s; of C_L4: %s; outside lambda0's leaves, the certified numbers and the seed's"
        " constants: %s" % (sorted(map(str, leafset(C11))), sorted(map(str, leafset(C4))), sorted(map(str, extra))
                            or "none"))
    return not extra


def positive_tree(e):
    """True if e is built from positive symbols and positive numbers by +, *, exp, Max, sqrt and positive powers"""
    if e.is_Symbol:
        return True
    if e.is_Number:
        return e > 0
    if isinstance(e, (sp.Add, sp.Mul, sp.exp, sp.Max)):
        return all(positive_tree(x) for x in e.args)
    if isinstance(e, sp.Pow):
        base, ex = e.args
        return positive_tree(base) and (ex.is_Number and (ex > 0 or base.is_Number))
    if e.func == sp.pi.func or e == sp.pi:
        return True
    return False


def k2(control=False):
    C11, C4 = build(mutate="minus" if control else None)
    structural = positive_tree(C11) and positive_tree(C4)
    rng = random.Random(11)
    fd_ok = True
    syms = sorted((leafset(C11) | leafset(C4)), key=str)
    f11 = sp.lambdify(syms, C11, 'mpmath')
    f4 = sp.lambdify(syms, C4, 'mpmath')
    import mpmath as mp
    mp.mp.dps = 30
    for _ in range(200):
        pt = [mp.mpf(rng.uniform(0.05, 1.5)) for _ in syms]
        k = rng.randrange(len(syms))
        pt2 = list(pt)
        pt2[k] *= mp.mpf('1.01')
        for f in (f11, f4):
            fd_ok &= f(*pt2) >= f(*pt)
    if control:
        return structural
    out("  K2 C_L11 and C_L4 increasing in every leaf: structurally %s, by finite differences at 200 random points %s"
        % (structural, fd_ok))
    return structural and fd_ok


def k3(control=False):
    C11, C4 = build()
    cert = dict(CERT)
    if control:
        cert[C_S] = sp.Rational(1, 10**40)                   # a mutation: Lemma 2.1's constant dropped
    c11 = C11.subs(cert)
    c4 = C4.subs(cert)
    ones = {s_: 1 for s_ in (leafset(c11) | leafset(c4)) if s_ != lam0}
    ones[lam0] = sp.Rational(244, 100000)                    # lambda0 < 0.0024433 (CONSTANTS5 Round 4)
    import mpmath as mp
    l11 = mp.log10(mp.mpf(sp.N(c11.subs(ones), 30)))
    l4 = mp.log10(mp.mpf(sp.N(c4.subs(ones), 30)))
    if control:
        return l11 > 0 and l4 > 0
    out("  K3 at P* (certified leaves inserted) C_L11 and C_L4 depend on %s; with every remaining leaf equal to 1 and"
        " lambda0 = 0.00244 (an illustration of the formula, not a bound): log10 C_L11 = %s, log10 C_L4 = %s" % (
            sorted(map(str, leafset(c11) | leafset(c4))), mp.nstr(l11, 6), mp.nstr(l4, 6)))
    return l11 > 0 and l4 > 0


def main():
    ok = True
    for name, f in (("K1", k1), ("K2", k2), ("K3", k3)):
        good = f()
        ctl = f(control=True)
        out("%s %s%s" % (name, "PASS" if good and not ctl else "FAIL", " (control passed)" if ctl else ""))
        ok &= good and not ctl
    out("constL5: %s" % ("all checks pass, every control fails" if ok else "FAILURES"))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
