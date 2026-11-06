#!/usr/bin/env python3
"""nledger5: the power counting of Theorem E_2_N's Steps 4-6 with N families, term by term (FAMILIES5-R8.md section
R8.4; FAMILIES5-R6.md section 4, E_2_N (vi)).

twoledger5 lists every term of the two-family linearisation and derives each term's worst power of lam and highest
derivative from the record's rules (Lemma 2.1-2.2, Step 1). This program writes out the N-family linearisation
term by term, for N = 2..8, and evaluates every term with twoledger5's own weights() and evaluate(), so that nothing
is taken from the two-family list by analogy. The N-family terms (FAMILIES5-R6.md section 4, E_2_N (i)-(vi)):

  Step 4 (h): the background terms; for every family A: -(1/2) lam^-1 ((1 - P) s_A) G2^A, the ell_app - ell term,
     -phi_A [T1], (1/2) Psi_A G1, the c^ab and lam box_app phi_A F ghat_2 terms, B1 . d phi_A, C1 phi_A, and N_phi^A's
     three w terms.
  Step 5 (phi_A): ell_A . d phi_A = (1/2) P s_A(h): the three targets and [d^a, L_A] phi_A, for every A.
  Step 6 (Psi_A, with Lemma 3.3_N): contracting with ell_A x ell_A kills family A's lam^-1 term and its box phi_A
     term; what is left is c1 . dh, c0 h, the lam d^2 phi and N_phi terms of family A, and for every B != A the cross
     terms c2 . d phi_B, c3 phi_B, the coupling -q c_A Psi_B, q lam^-1 ((1 - P) s_B) G2^B(ell_A, ell_A) and
     2 q N_phi^B(ell_A, ell_A); the P box s_A rewriting with (M5) both forms; -(1/2) M_A(P s_A), -N_A phi_A, a_A Psi_A.
  Coefficient sources: every coefficient c above is built from g = g_app + w, and g_app's stage-1 part holds single
     profiles and products of two (the quadratic stage terms). So each coefficient-bearing term is enumerated over its
     source: the background, one family C, or a pair {C, D}. A cross term of Step 6 (target A, unknown B) with a pair
     source {C, D} carries four family labels, so the full list grows like N^4, not N^3 as FAMILIES5-R6.md section 4
     (vi) said (L2; R8 corrects the count, which only enters the constants).

  L1 every N-family term (level 1: family structure; level 2: with coefficient sources) passes at k = K = 6, for
     N = 2..8, evaluated one by one; and the set of term types (U, p, kappa, m, ops, extra, wfac) the N-family list
     uses is exactly the two-family ledger's, for every N (so twoledger5's grid k = 6..12, K = 6..10 applies; it is
     rerun here on the N = 4 list, every term).
  L2 the term counts are polynomials in N of degree 2 (level 1) and 4 (level 2), found by exact interpolation on
     N = 2..6 and checked on N = 7, 8.
  L3 the coefficient rule for products (computed, sympy): a product of two or three oscillating profiles
     a_C(x) exp(i omega_C . x/lam), distinct phases, has m-th derivatives of size lam^-m exactly (the leading power,
     m = 0..4), as a single profile has: kappa = 1 for every source.
  L4 the closing rows are N-independent in their powers (twoledger5 T2) with N-dependent constants: Step 7's
     M(N) := C3 (C_D(N) + 1 + C_R(N)) + 1, lam0(N) := 1/(C3 C(N) M(N)^2) close for any positive C(N) (exact, symbolic).
  Controls (each must fail): (a) Lemma 3.3_N without the contraction: family A's own lam^-1 term (1/2) lam^-1 P s_A
     G2^A(ell_A, ell_A) left in Step 6 (exponent -1); (b) a cross term q lam^-1 ((1 - P) s_B) G2^B(ell_A, ell_A) without
     its (1 - P) gain, as if s_B entered unmollified (exponent -1); (c) the coupling -q c_A Psi_B for a pair (A, B)
     estimated as a generic second derivative of phi_B (exponent -1); (d) L3's rule with a non-oscillating factor
     replaced by one of phase omega/lam^2 (costs lam^-2 per derivative: kappa = 2, so the w-free coefficient rule
     fails).

Labels: computed (exact integer and symbolic arithmetic). Reach: as twoledger5's -- the rules are the record's
(deduced there); this program computes the counting they imply for every N-family term, not the estimates, and the
constants' N-dependence is carried, not bounded. Run: python3 checks/nledger5.py   (about a minute)
"""
import importlib.util
import itertools
import os
import re
import sys

import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))


def load(name):
    spec = importlib.util.spec_from_file_location(name, os.path.join(HERE, name + '.py'))
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


TL = load('twoledger5')


def rows_N(K, N, sources=False):
    """the N-family term list; rows as twoledger5's (step, label, U, p, kappa, m, ops, extra, wfac)"""
    Km3 = K - 3
    fam = list(range(1, N + 1))
    srcs = ['bg'] + ['%d' % c for c in fam] + ['%d%d' % cd for cd in itertools.combinations(fam, 2)]
    t = []

    def add(step, lab, U, p, ka, m, ops, extra, wfac):
        # coefficients built from the approximant: every kappa = 1 term but the w terms and those whose coefficient
        # belongs to one family by definition (G2^A, the coupling's c_A)
        if sources and ka == 1 and not wfac and not re.search(r'w part|G2|c_\d+ Psi', lab):
            for s_ in srcs:                                        # a coefficient built from the approximant
                t.append((step, lab + ' [c from %s]' % s_, U, p, ka, m, list(ops), extra, wfac))
        else:
            t.append((step, lab, U, p, ka, m, list(ops), extra, wfac))
    # Step 4
    add("4", "B.dh", "h", 0, 1, 1, [], 0, 0)
    add("4", "C.h", "h", 0, 1, 0, [], 0, 0)
    add("4", "[d^a, g^ab] d_a d_b h, g_app part (i >= 1)", "h", 1, 1, 2, ["i>=1"], 0, 0)
    add("4", "[d^a, g^ab] d_a d_b h, w part (i >= 1)", "h", Km3, 1, 2, ["i>=1"], 0, 1)
    for A in fam:
        add("4", "-(1/2) lam^-1 ((1 - P) s_%d) G2^%d" % (A, A), "s", -1, 1, 0, ["oneminusP"], 0, 0)
        add("4", "lam^-1 ((ell_app - ell) . d phi_%d) G2^%d, |ell_app - ell| <= C lam" % (A, A), "phi", 0, 1, 1, [],
            0, 0)
        add("4", "-phi_%d [T1]" % A, "phi", 0, 1, 0, [], 0, 0)
        add("4", "(1/2) Psi_%d G1" % A, "Psi", 0, 1, 0, [], 0, 0)
        add("4", "(1/2) c^ab d_a d_b phi_%d G1, |c| <= C lam" % A, "phi", 1, 1, 2, [], 0, 0)
        add("4", "(1/2) lam (box_app phi_%d) F ghat_2: lam Psi" % A, "Psi", 1, 1, 0, [], 0, 0)
        add("4", "(1/2) lam (box_app phi_%d) F ghat_2: lam^2 d^2 phi" % A, "phi", 2, 1, 2, [], 0, 0)
        add("4", "B1 . d phi_%d" % A, "phi", 0, 1, 1, [], 0, 0)
        add("4", "C1 phi_%d" % A, "phi", 0, 1, 0, [], 0, 0)
        add("4", "N_phi^%d: |w| lam^-2 |phi|" % A, "phi", Km3 - 2, 1, 0, [], 0, 1)
        add("4", "N_phi^%d: |w| lam^-1 |d phi|" % A, "phi", Km3 - 1, 1, 1, [], 0, 1)
        add("4", "N_phi^%d: |w| |d^2 phi|" % A, "phi", Km3, 1, 2, [], 0, 1)
    # Step 5
    for A in fam:
        add("5", "(1/2) P s_%d, for ||phi||" % A, "s", 0, 0, 0, ["P", "j=0"], 0, 0)
        add("5", "(1/2) P s_%d, for lam^j ||d^j d phi||" % A, "s", 0, 0, 0, ["P"], 1, 0)
        add("5", "(1/2) P s_%d, for lam^(j+1) ||d^j d_x^2 phi|| (Bernstein)" % A, "s", 0, 0, 0, ["P", "bern_t"], 2, 0)
        add("5", "[d^a, L_%d] phi (smooth coefficients, i >= 1)" % A, "phi", 0, 0, 1, ["i>=1"], 1, 0)
    # Step 6, target family A; Lemma 3.3_N: own terms, and the cross terms of every B != A
    for A in fam:
        own = [("c1 . dh", "h", 0, 1, 1), ("c0 h", "h", 0, 1, 0), ("c2 . d phi_%d" % A, "phi", 0, 1, 1),
               ("c3 phi_%d" % A, "phi", 0, 1, 0), ("lam d^2 phi_%d (c^ab, lam F ghat_2 terms)" % A, "phi", 1, 1, 2),
               ("2q N_phi^%d: |w| lam^-2 |phi|" % A, "phi", Km3 - 2, 1, 0),
               ("2q N_phi^%d: |w| lam^-1 |d phi|" % A, "phi", Km3 - 1, 1, 1)]
        cross = []
        for B in fam:
            if B == A:
                continue
            cross += [("c2 . d phi_%d" % B, "phi", 0, 1, 1), ("c3 phi_%d" % B, "phi", 0, 1, 0),
                      ("-q c_%d Psi_%d (the coupling)" % (A, B), "Psi", 0, 1, 0),
                      ("q lam^-1 ((1 - P) s_%d) G2^%d(ell_%d, ell_%d)" % (B, B, A, A), "s", -1, 1, 0),
                      ("lam d^2 phi_%d (c^ab, lam F ghat_2 terms)" % B, "phi", 1, 1, 2),
                      ("2q N_phi^%d: |w| lam^-2 |phi_%d|" % (B, B), "phi", Km3 - 2, 1, 0),
                      ("2q N_phi^%d: |w| lam^-1 |d phi_%d|" % (B, B), "phi", Km3 - 1, 1, 1),
                      ("2q N_phi^%d(ell_%d, ell_%d): |w| |d^2 phi_%d|" % (B, A, A, B), "phi", Km3, 1, 2)]
        for lab, U, p, ka, m in own + cross:
            ops = ["P"] + (["oneminusP"] if "(1 - P)" in lab else [])
            add("6", "P box s_%d: %s" % (A, lab), U, p, ka, m, ops, 0, 1 if "|w|" in lab else 0)
        add("6", "P box s_%d: P d_i (c d_a h), |c| <= C(lam + |w|)" % A, "h", 1, 1, 2, ["P", "bern"], 0, 0)
        add("6", "P box s_%d: P((d_i c) d_a h), |d c| <= C" % A, "h", 0, 1, 1, ["P"], 0, 0)
        add("6", "[box, P] s_%d: spatial index, (M5) first form" % A, "s", 0, 0, 2, ["M5a"], 0, 0)
        add("6", "[box, P] s_%d: d^2 P - P d^2: lam P d_x d s (M4, M6)" % A, "s", 1, 0, 2, ["bern"], 0, 0)
        for lab, U, p, ka, m in own + cross:                       # the tau-tau rewrite, (M5) second form
            ops = ["M5b", "oneminusP"] if "(1 - P)" in lab else ["M5b"]
            add("6", "[box, P] s_%d, tau-tau, M5b: %s" % (A, lab), U, p, ka, m, ops, 0, 1 if "|w|" in lab else 0)
        add("6", "[box, P] s_%d, tau-tau: [a, P] d_i (c d_a h) by (M5) first form" % A, "h", 1, 1, 2, ["M5a"], 0, 0)
        add("6", "[box, P] s_%d, tau-tau: [a, P]((d_i c) d_a h) by (M5) second form" % A, "h", 0, 1, 1, ["M5b"], 0, 0)
        add("6", "-(1/2) M_%d(P s_%d)" % (A, A), "s", 0, 0, 1, ["P"], 0, 0)
        add("6", "-N_%d phi_%d" % (A, A), "phi", 0, 0, 1, [], 0, 0)
        add("6", "a_%d Psi_%d and [d^a, L_%d] Psi_%d" % (A, A, A, A), "Psi", 0, 0, 0, [], 0, 0)
    return t


def sig(r):
    return (r[0], r[2], r[3], r[4], r[5], tuple(r[6]), r[7], r[8])


def l3():
    """the lam-power of the m-th derivative of a product of oscillating profiles (leading term), exactly"""
    x, lam = sp.symbols('x lam', positive=True)
    a1, a2, a3 = [sp.Function(nm)(x) for nm in ('a1', 'a2', 'a3')]
    w1, w2, w3 = sp.Rational(1), sp.Rational(3, 2), sp.Rational(-2, 3)
    prof = [a1 * sp.exp(sp.I * w1 * x / lam), a2 * sp.exp(sp.I * w2 * x / lam), a3 * sp.exp(sp.I * w3 * x / lam)]
    out = {}
    for nprod in (1, 2, 3):
        c = sp.Mul(*prof[:nprod])
        pw = []
        for m in range(5):
            d = sp.expand(sp.diff(c, x, m) / c)                       # a polynomial in 1/lam
            pw.append(sp.Poly(sp.expand(d.subs(lam, 1 / sp.Symbol('t'))), sp.Symbol('t')).degree())
        out[nprod] = pw
    # control (d): a factor of phase omega x/lam^2 costs lam^-2 per derivative
    c = a1 * sp.exp(sp.I * x / lam**2)
    pwc = []
    for m in range(5):
        d = sp.expand(sp.diff(c, x, m) / c)
        pwc.append(sp.Poly(sp.expand(d.subs(lam, 1 / sp.Symbol('t'))), sp.Symbol('t')).degree())
    return out, pwc


def l4():
    lam, M, C3, CD, CR, N = sp.symbols("lam M C3 C_D C_R N", positive=True)
    C = sp.Function('C')(N)
    CDN, CRN = sp.Function('C_D')(N), sp.Function('C_R')(N)
    Mdef = C3 * (CDN + 1 + CRN) + 1
    lam0 = 1 / (C3 * C * Mdef**2)
    # Step 7: N_2 <= C3 (C_D + 1 + C_R) lam^K + C3 C M^2 lam^(K+1) <= (C3 (C_D + 1 + C_R) + C3 C M^2 lam0) lam^K
    #         = M lam^K
    return sp.simplify(Mdef - (C3 * (CDN + 1 + CRN) + C3 * C * Mdef**2 * lam0)) == 0


def main():
    ok = True
    W6 = TL.weights(6)
    two = {sig(r) for r in TL.term_rows(6)}
    counts1, counts2 = {}, {}
    print("L1 every N-family term evaluated with twoledger5's weights and rules, k = K = 6")
    for N in range(2, 9):
        res = {}
        for lev, srcs in ((1, False), (2, True)):
            rows = rows_N(6, N, sources=srcs)
            fails = []
            for r in rows:
                e, mo = TL.evaluate(r, 6, W6)
                if e is None or e < 0:
                    fails.append((r[1], e, mo))
            types = {sig(r) for r in rows}
            res[lev] = (len(rows), len(fails), types == two, len(types))
            (counts1 if lev == 1 else counts2)[N] = len(rows)
            ok &= not fails and types == two
        print("   N = %d: level 1 %d terms, %d fail, types = the two-family ledger's (%d): %s; level 2 (coefficient "
              "sources) %d terms, %d fail, types the same: %s" % (N, res[1][0], res[1][1], res[1][3], res[1][2],
                                                                  res[2][0], res[2][1], res[2][2]), flush=True)
    rows4 = rows_N(6, 4, sources=True)
    grid = True
    for k in range(6, 13):
        Wk = TL.weights(k)
        for K in range(6, 11):
            rowsK = rows_N(K, 4, sources=True) if K != 6 else rows4
            grid &= all((lambda e: e[0] is not None and e[0] >= 0)(TL.evaluate(r, k, Wk)) for r in rowsK)
    print("   the N = 4 list (level 2, %d terms), every term on k = 6..12 x K = 6..10: %s" % (len(rows4), grid))
    ok &= grid
    print("L1", "PASS" if ok else "FAIL", flush=True)
    # L2: degrees by finite differences
    n = sp.Symbol('N')
    deg = {}
    for lev, cnt in ((1, counts1), (2, counts2)):
        xs = sorted(cnt)
        poly = sp.interpolate([(x, cnt[x]) for x in xs[:5]], n)
        exact = all(poly.subs(n, x) == cnt[x] for x in xs)
        deg[lev] = (sp.degree(poly, n), sp.factor(poly), exact)
    l2 = deg[1][0] == 2 and deg[2][0] == 4 and deg[1][2] and deg[2][2]
    print("L2 term counts: level 1 = %s (degree %d, exact on N = 2..8: %s); level 2 = %s (degree %d, exact: %s): %s"
          % (sp.expand(deg[1][1]), deg[1][0], deg[1][2], sp.expand(deg[2][1]), deg[2][0], deg[2][2],
             "PASS" if l2 else "FAIL"))
    ok &= l2
    pw, pwc = l3()
    l3ok = all(pw[k_] == list(range(5)) for k_ in (1, 2, 3))
    print("L3 the leading lam-power of d^m (product of 1, 2, 3 profiles)/(product), m = 0..4, non-resonant phases: "
          "%s, %s, %s (= m: kappa = 1 for every source; a resonant product costs less): %s" %
          (pw[1], pw[2], pw[3], "PASS" if l3ok else "FAIL"))
    ok &= l3ok
    l4ok = l4()
    nl = TL.t2()
    print("L4 the closing rows: twoledger5 T2's powers (non-linear 2K - 5 - (K + 1) = %s >= 0: %s), N-independent; "
          "Step 7 with M(N), lam0(N) for any positive C(N), C_D(N), C_R(N) closes (exact): %s" %
          (nl[3], nl[0], "PASS" if l4ok and nl[0] and nl[1] else "FAIL"))
    ok &= l4ok and nl[0] and nl[1]
    # controls
    ctl = {}
    ctl['a'] = TL.evaluate(("6", "own lam^-1 term left: (1/2) lam^-1 P s_A G2^A(ell_A, ell_A)", "s", -1, 1, 0, ["P"],
                            0, 0), 6, W6)
    ctl['b'] = TL.evaluate(("6", "q lam^-1 s_B G2^B(ell_A, ell_A) without (1 - P)", "s", -1, 1, 0, ["P"], 0, 0), 6, W6)
    ctl['c'] = TL.evaluate(("6", "-q c_A Psi_B as d^2 phi_B", "phi", 0, 1, 2, ["P"], 0, 0), 6, W6)
    fails = {k_: (e is None or e < 0) for k_, (e, _) in ctl.items()}
    fails['d'] = pwc != list(range(5))
    for k_ in ('a', 'b', 'c'):
        print("   control (%s): exponent %s, order %s: rejected %s" % (k_, ctl[k_][0], ctl[k_][1], fails[k_]))
    print("   control (d): a factor of phase x/lam^2 has leading powers %s (kappa = 2): rejected %s" % (pwc, fails['d']))
    ok_ctl = all(fails.values())
    print("L1-L4:", "PASS" if ok else "FAIL")
    print("controls (a)-(d) rejected:", "PASS" if ok_ctl else "FAIL")
    return 0 if ok and ok_ctl else 1


if __name__ == "__main__":
    sys.exit(main())
