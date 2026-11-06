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
  K2 (computed) with the certified numbers inserted, both are increasing in every remaining leaf (each node of the
     DAG a positive expression of its inputs, built by +, *, exp, max and positive powers; checked structurally and by
     finite differences at 40 random points), so upper bounds of the leaves give upper bounds of C_L11 and C_L4.
     Control: a mutated node with a difference (C_tr - 1) is detected as not monotone.
  K3 (computed) at P* with the certified leaves inserted, printed in the remaining leaves; with the seed's constants
     and the profile bounds all equal to one (an illustration, not a bound), log10 C_L11 and log10 C_L4 are printed.
     Control: C_S (Lemma 2.1) replaced by 0 makes C_L4 vanish (the formula is proportional to it), so the check
     C_L4 > 1 fails.
  K4 (computed; round 6, the verifier of round 5's m11) the DAG agrees, at 20 random points, with an independent
     step-by-step transcription of R5.5's display, each line cited to the proof step it records (L.9 (b), L.10, L.8,
     L.3 (a)-(e), D3, Corollary L.11, Lemma L.4).  Controls: Cd's power N + 1 mutated to N + 5, and a term of Ca
     dropped, are each detected.

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


class Dag:
    """named constants, each defined by a sympy expression in leaves and earlier names (a DAG, not a tree)"""

    def __init__(self):
        self.defs = []                                       # (symbol, expression)

    def __call__(self, name, expr):
        sym = sp.Symbol(name, positive=True)
        self.defs.append((sym, expr))
        return sym

    def names(self):
        return {s_ for s_, _ in self.defs}

    def leaves(self):
        used = set()
        for _, e in self.defs:
            used |= e.free_symbols
        return used - self.names()

    def value(self, subs):
        vals = {k: sp.Float(sp.N(v_, 40), 40) for k, v_ in subs.items()}
        for s_, e in self.defs:
            vals[s_] = sp.Float(sp.N(e.subs(vals), 40), 40)
        return vals


def build(N=9, mutate=None):
    """the recursion of Lemma L.3's proof and the assemblies of Corollary L.11 and Lemma L.4, as a DAG"""
    d = Dag()
    top = P[12] if mutate == "P12" else P[6]
    K = d("K", Ks + top)                                    # coefficient bound of a monomial's factors (F1), (F2)
    M1 = d("M1", 2*sp.pi*K)                                 # Lemma L.9 (b): ||d_th^-1|| <= pi, ||Pi_osc|| <= 2 (D4)
    C_tr = d("C_tr", sp.exp(M1*(b - a)) - (1 if mutate == "minus" else 0))     # Gronwall along ell, L <= b - a
    C_E = d("C_E", C2)                                      # Lemma L.8 = Lemma 2.3's constant on Omega_v
    C_N = d("C_N", C_S3*(1 + sp.sqrt(2)*sp.sqrt(b - a)*a**sp.Rational(-3, 2)))    # Lemma L.10
    KP = d("KP", Ks)                                        # ||Pol^+|| and the 'known' coefficients: the seed's
    Ca = {1: d("Ca1", A*Ks)}                                # stage 0: W_TT, cost i (ansatz5 A3)
    Cb, Ce = {}, {}
    Cc = {1: d("Cc1", C_tr*K*(A*Ks)**2)}                    # chi: transport of a quadratic source (stage 0)
    for m in range(1, N + 1):
        sa = d("sa%d" % m, sum(Ca[l] for l in range(1, m + 1)))
        sb = d("sb%d" % m, sum(Cb[l] for l in range(1, m))) if m > 1 else sp.Integer(0)
        F2 = d("F2_%d" % m, K*(sa**2 + sb))                 # (F2): two oscillating factors, or an earlier mean
        Ce[m] = d("Ce%d" % m, C64*F2)                       # (e): Lemma 6.4 on [a, r]
        Ca[m + 1] = d("Ca%d" % (m + 1), C_tr*(KP*(top*Ce[m] + K*sa)
                                              + (0 if mutate == "Ca_drop" else 1)*(b - a)*K*sa*(1 + sb)))     # (a)
        Cb[m] = d("Cb%d" % m, C_N*C_E*sp.exp(C_E*T)*(Ce[m] + T*F2 + T*K*Ca[m + 1]*(1 + sa)))      # (b)
        Cc[m + 1] = d("Cc%d" % (m + 1), C_tr*(K*(Cc[m] + Cb[m] + sa*Ca[m]) + KP*Ce[m]))            # (c)
    sa = d("sa", sum(Ca.values()))
    sb = d("sb", sum(Cb.values()))
    pw = N + 5 if mutate == "Cd5" else N + 1
    Cd = d("Cd", K**pw*(1 + sa + sb)**(N + 1)/sp.factorial(N - 2))                            # (d)
    CU = d("CU", 2*C0*K*(sa + sb))                                                          # (e) for U
    C_D3 = d("C_D3", sp.Rational(2, 9)*A**2/(4*sp.sqrt(mu0)))                               # D3
    C_beta = d("C_beta", sp.Rational(2, 9)*A**2*(1/(2*mu0) + 1/(4*mu0)))                    # D3: |beta0|
    t1 = d("L11a", sum(lam0**(j - 4)*Ca[j] for j in range(4, N + 2)))
    t2 = d("L11b", sum(lam0**(j - 1)*Cc[j] for j in range(1, N + 2)) + lam0**2*Ca[3]*C_D3
           + 3*C_beta*sum(lam0**(j - 1)*Ca[j] for j in range(1, N + 2)))
    t3 = d("L11c", (1 + C_beta)**2)
    C11 = d("C_L11", sp.Max(t1, t2, t3))                                                    # Corollary L.11
    C_coef = d("C_coef", C2*(1 + M + K))                                                    # L.4 steps 3-4
    C_dat = d("C_dat", CU*(1 + Ks))                                                         # L.4 step 5
    C4 = d("C_L4", C_S*sp.exp(C_coef*T)*(C_dat + T*Cd))                                     # L.4 steps 6-7
    return d, C11, C4


def k1(control=False):
    d, C11, C4 = build(mutate="P12" if control else None)
    allowed = LEAVES | set(CERT) | SEED
    extra = d.leaves() - allowed
    if control:
        return not extra
    out("  K1 the DAG of C_L11 and C_L4 (%d named constants): its leaves %s; outside lambda0's leaves, the certified"
        " numbers and the seed's constants: %s" % (len(d.defs), sorted(map(str, d.leaves())),
                                                  sorted(map(str, extra)) or "none"))
    return not extra


def positive_tree(e):
    """True if e is built from positive symbols and positive numbers by +, *, exp, Max, sqrt and positive powers"""
    if e.is_Symbol:
        return True
    if e.is_Number:
        return e > 0
    if e == sp.pi:
        return True
    if isinstance(e, (sp.Add, sp.Mul, sp.exp, sp.Max)):
        return all(positive_tree(x) for x in e.args)
    if isinstance(e, sp.Pow):
        base, ex = e.args
        return positive_tree(base) and ex.is_Number and (ex > 0 or base.is_Number)
    return False


def k2(control=False):
    d, C11, C4 = build(mutate="minus" if control else None)
    # the certified numbers (a, b(tau0), tau_end - tau0, mu_end, C_S, A, mu0) inserted first: monotone in the others
    structural = all(positive_tree(e.subs(CERT)) for _, e in d.defs)
    if control:
        return structural
    rng = random.Random(11)
    fd_ok = True
    leaves = sorted(d.leaves() - set(CERT), key=str)
    for _ in range(40):
        pt = dict(CERT)
        pt.update({s_: sp.Rational(rng.randint(5, 150), 100) for s_ in leaves})
        k = rng.choice(leaves)
        pt2 = dict(pt)
        pt2[k] = pt[k]*sp.Rational(101, 100)
        v1, v2 = d.value(pt), d.value(pt2)
        fd_ok &= all(v2[c] - v1[c] >= 0 for c in (C11, C4))
    out("  K2 with the certified numbers inserted, C_L11 and C_L4 increasing in every remaining leaf: every node of the"
        " DAG a positive expression of its inputs %s, by finite differences at 40 random points %s"
        % (structural, fd_ok))
    return structural and fd_ok


def k3(control=False):
    d, C11, C4 = build()
    cert = dict(CERT)
    if control:
        cert[C_S] = sp.Integer(0)                            # a mutation: Lemma 2.1's constant dropped
    rest = {s_: 1 for s_ in d.leaves() if s_ not in cert}
    rest[lam0] = sp.Rational(244, 100000)                    # lambda0 < 0.0024433 (CONSTANTS5 Round 4)
    vals = d.value({**cert, **rest})
    import mpmath as mp
    l11 = mp.log10(mp.mpf(sp.N(vals[C11], 30)))
    v4 = mp.mpf(sp.N(vals[C4], 30))
    l4 = mp.log10(v4) if v4 > 0 else -mp.inf
    if control:
        return l11 > 0 and l4 > 0
    out("  K3 at P* (certified leaves inserted) C_L11 and C_L4 depend on %s; with every remaining leaf equal to 1 and"
        " lambda0 = 0.00244 (an illustration of the formula, not a bound): log10 C_L11 = %s, log10 C_L4 = %s" % (
            sorted(map(str, d.leaves() - set(cert))), mp.nstr(l11, 6), mp.nstr(l4, 6)))
    return l11 > 0 and l4 > 0


def table(leaf, N=9):
    """an independent transcription of R5.5's display, step by step (each line its proof step), as numbers"""
    import mpmath as mp
    mp.mp.dps = 40
    g = lambda nm: mp.mpf(sp.N(leaf[nm], 40))                                         # noqa: E731
    Ks_, P6_, C64_, C0_, M_, C2_, l0, a_, b_, T_, CS, CS3, A_, mu_ = [g(x) for x in (
        Ks, P[6], C64, C0, M, C2, lam0, a, b, T, C_S, C_S3, A, mu0)]
    K = Ks_ + P6_                                           # the factors' bound, (F1), (F2)
    C_tr = mp.exp(2*mp.pi*K*(b_ - a_))                      # L.9 (b): Gronwall along ell, ||d_th^-1|| <= pi, ||Pi|| <= 2
    C_N = CS3*(1 + mp.sqrt(2)*mp.sqrt(b_ - a_)*a_**mp.mpf(-1.5))    # L.10
    C_E = C2_                                               # L.8 = Lemma 2.3
    Ca, Cb, Cc, Ce = {1: A_*Ks_}, {}, {1: C_tr*K*(A_*Ks_)**2}, {}
    for m in range(1, N + 1):
        sa = sum(Ca[l] for l in range(1, m + 1))
        sb = sum(Cb[l] for l in range(1, m))
        Ce[m] = C64_*K*(sa**2 + sb)                                                # L.3 (e)
        Ca[m + 1] = C_tr*(Ks_*(P6_*Ce[m] + K*sa) + (b_ - a_)*K*sa*(1 + sb))       # L.3 (a)
        Cb[m] = C_N*C_E*mp.exp(C_E*T_)*(Ce[m] + T_*K*(sa**2 + sb) + T_*K*Ca[m + 1]*(1 + sa))     # L.3 (b)
        Cc[m + 1] = C_tr*(K*(Cc[m] + Cb[m] + sa*Ca[m]) + Ks_*Ce[m])                 # L.3 (c)
    sa, sb = sum(Ca.values()), sum(Cb.values())
    Cd = K**(N + 1)*(1 + sa + sb)**(N + 1)/mp.factorial(N - 2)                    # L.3 (d)
    CU = 2*C0_*K*(sa + sb)                                                         # L.3 (e), U
    C_D3, C_b = mp.mpf(2)/9*A_**2/(4*mp.sqrt(mu_)), mp.mpf(2)/9*A_**2*(mp.mpf(3)/(4*mu_))   # D3
    C11 = max(sum(l0**(j - 4)*Ca[j] for j in range(4, N + 2)),
              sum(l0**(j - 1)*Cc[j] for j in range(1, N + 2)) + l0**2*Ca[3]*C_D3
              + 3*C_b*sum(l0**(j - 1)*Ca[j] for j in range(1, N + 2)), (1 + C_b)**2)   # Corollary L.11
    C4 = CS*mp.exp(C2_*(1 + M_ + K)*T_)*(CU*(1 + Ks_) + T_*Cd)                     # L.4 steps 3-7
    return C11, C4


def k4(control=False):
    import mpmath as mp
    rng = random.Random(4)
    worst = mp.mpf(0)
    for mut in (("Cd5", "Ca_drop") if control else (None,)):
        d, C11, C4 = build(mutate=mut)
        ok = True
        for _ in range(20):
            leaf = dict(CERT)
            leaf.update({s_: sp.Rational(rng.randint(5, 150), 100) for s_ in d.leaves() - set(CERT)})
            v = d.value(leaf)
            t11, t4 = table(leaf)
            for x, y in ((v[C11], t11), (v[C4], t4)):
                rel = abs(mp.mpf(sp.N(x, 40)) - y)/abs(y)
                worst = max(worst, rel)
                ok &= rel < mp.mpf('1e-25')
        if control and ok:
            return True
    if control:
        return False
    out("  K4 the DAG against an independent step-by-step transcription of R5.5's display (each line cited to its"
        " proof step), at 20 random points: largest relative difference %s: %s" % (mp.nstr(worst, 3), ok))
    return ok


def main():
    ok = True
    for name, f in (("K1", k1), ("K2", k2), ("K3", k3), ("K4", k4)):
        good = f()
        ctl = f(control=True)
        out("%s %s%s" % (name, "PASS" if good and not ctl else "FAIL", " (control passed)" if ctl else ""))
        ok &= good and not ctl
    out("constL5: %s" % ("all checks pass, every control fails" if ok else "FAILURES"))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
