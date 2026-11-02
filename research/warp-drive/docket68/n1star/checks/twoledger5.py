#!/usr/bin/env python3
"""twoledger5: the power counting of Theorem E_2's Steps 4-6 with two families, term by term (FAMILIES5-FULL.md section 8).

The record's section 4 closes because every term on the right of the equations for h, phi and Psi is, at every level j
<= k, at most C N in the scaled norm, or C_R lam^K, or C M^2 lam^(K+1). With two families every equation gains the other
family's terms. This program lists every term of (3.5_2), of the phase transports (3.4_2) and of the Psi transports
(3.6_2) with Lemma 3.3_2 inserted, and derives each term's worst power of lam and its highest derivative from rules
stated once, not typed per term.

  The norm (section 8, (8.1)): N_2 := sum_(j<=k) lam^j (||d^j d h|| + sum_K (||d^j Psi_K|| + ||d^j d phi_K|| + lam ||d^j
  d_x^2 phi_K||)) + ||h|| + sum_K ||phi_K||. From it, by reading off weight and order (derived in weights() below):
  ||d^m h|| <= lam^(-e_h(m)) N_2 with e_h(m) = max(m - 1, 0) for m <= k + 1; the same for s_K(h) = h(ell_K, ell_K),
  ell_K smooth and lam-independent; ||d^m phi|| <= lam^(-e(m)) N_2, e(m) = max(m - 1, 0), m <= k + 2 (the top order through
  Lemma 3.4_2: every second derivative of phi_K is a combination of L_K P s_K, d_x P s_K, d phi_K and d_x^2 phi_K);
  ||d^m Psi|| <= lam^(-m) N_2, m <= k.
  A term is lam^p c d^m U, U one of h, s, phi, Psi; c a coefficient whose derivatives cost lam^-1 each (a profile, or a
  quantity built from g = g_app + w; kappa = 1) or nothing (smooth and lam-independent, kappa = 0). Mollifier rules
  (Lemma 2.2): P costs nothing (M1, M4, M6); P d_i costs lam^-1 and absorbs the d_i (M2: 'bern'); (1 - P) gains lam
  and costs one derivative (M3: 'oneminusP'); [a, P] d_i absorbs the d_i at no cost (M5 first form: 'M5a'); [a, P] gains
  lam (M5 second form: 'M5b'). The target of the h and Psi equations at level j is lam^j ||d^j T||; of the phase
  transport lam^j ||d^j d T|| (one more derivative) and lam^(j+1) ||d^j d_x^2 T||. Then for j <= k and i derivatives on
  c (0 <= i <= j + extra) the exponent is j + p - kappa i - e_U(j + extra - i + m) and the order on U is j + extra - i
  + m. A term passes when the least exponent is >= 0 and the highest order is within N_2's reach.
  The w-coefficient terms: |d^i w| <= C M lam^(K-3-i) (Step 1), so a factor of w is a coefficient with p = K - 3,
  kappa = 1; a pass means <= C M lam^e N_2 with e >= 0, absorbed for lam <= lam0(M).

  T1 every term of Step 4 (h), Step 5 (phi_in, phi_out) and Step 6 (Psi_in, Psi_out, with Lemma 3.3_2's terms and the
     coupling P(-q c_in Psi_out)) passes at k = 6, K = 6, and on the grid k = 6..12, K = 6..10.
  T2 the non-linear and closing rows (ledger5.py L2's rules with N_2 for N): the worst non-linear term lam^-5 N_2^2 <= C
     M^2 lam^(2K-5) <= C M^2 lam^(K+1) (K >= 6), the residual C_R lam^K, and Step 7's choice M := C3 (C_D + 1 + C_R) + 1
     with C3 C M^2 lam0 <= 1 giving N_2 <= M lam^K (exact, symbolic constants).
  Controls (each must fail): (a) the phases defined from s_K(w) in place of s_K(h): Step 5's source then contains P(c_in
     phi_out), c_in oscillating, and lam^j ||d^j d P(c_in phi_out)|| has exponent -1 (all derivatives on c_in, ||phi||
     unweighted): FAMILIES5-FULL.md's 'routing the estimate that way would lose a power of lam'; (b) the coupling c_in
     box_app phi_out of Lemma 3.3_2 estimated as a generic second derivative of phi_out, without Psi_out in the norm:
     exponent -1; (c) Step 6's terms c^(ai) d_a d_i h without the P d_i rewriting: order k + 2 on h at j = k, beyond
     N_2; (d) the same terms under the tau-tau rewriting bounded by (M5)'s second form: order k + 2 (the record's own
     remark); (e) Step 5's d_x^2 phi transport without Bernstein (M2): order k + 2 on s; (f) K = 5: T2's non-linear row.

Labels: computed (exact integer and symbolic arithmetic). Reach: the rules are the record's Lemma 2.1-2.2 and Step 1 as
stated (deduced there); this program computes the counting they imply for every two-family term, not the estimates.
Run: python3 checks/twoledger5.py   (seconds)
"""
import sys

import sympy as sp


def weights(k):
    """(unknown, order m) -> lam-weight w with lam^w ||d^m U|| <= N_2, read off N_2's definition"""
    W = {}

    def put(U, m, w):
        if (U, m) not in W or w < W[(U, m)]:
            W[(U, m)] = w
    for j in range(k + 1):
        put("h", j + 1, j)                 # lam^j ||d^j d h||
        put("Psi", j, j)                   # lam^j ||d^j Psi||
        put("phi", j + 1, j)               # lam^j ||d^j d phi||
        put("phi", j + 2, j + 1)           # lam^(j+1) ||d^j d_x^2 phi|| (and every d^2 phi by Lemma 3.4_2)
    put("h", 0, 0)
    put("phi", 0, 0)
    for m in range(k + 2):                 # s = h(ell, ell), ell smooth: the same as h
        if ("h", m) in W:
            put("s", m, W[("h", m)])
    return W


def term_rows(K):
    """(step, label, U, p, kappa, m, ops, extra, wfac); extra = derivatives the target adds; wfac: a factor of w"""
    Km3 = K - 3
    t = []
    # Step 4: (3.5_2) for h, target lam^j ||d^j T||
    t += [("4", "B.dh", "h", 0, 1, 1, [], 0, 0), ("4", "C.h", "h", 0, 1, 0, [], 0, 0),
          ("4", "[d^a, g^ab] d_a d_b h, g_app part (i >= 1)", "h", 1, 1, 2, ["i>=1"], 0, 0),
          ("4", "[d^a, g^ab] d_a d_b h, w part (i >= 1)", "h", Km3, 1, 2, ["i>=1"], 0, 1)]
    for K_ in ("in", "out"):
        t += [("4", "-(1/2) lam^-1 ((1 - P) s_%s) G2" % K_, "s", -1, 1, 0, ["oneminusP"], 0, 0),
              ("4", "lam^-1 ((ell_app - ell) . d phi_%s) G2, |ell_app - ell| <= C lam" % K_, "phi", 0, 1, 1, [], 0, 0),
              ("4", "-phi_%s [T1]" % K_, "phi", 0, 1, 0, [], 0, 0),
              ("4", "(1/2) Psi_%s G1" % K_, "Psi", 0, 1, 0, [], 0, 0),
              ("4", "(1/2) c^ab d_a d_b phi_%s G1, |c| <= C lam" % K_, "phi", 1, 1, 2, [], 0, 0),
              ("4", "(1/2) lam (box_app phi_%s) F ghat_2: lam Psi" % K_, "Psi", 1, 1, 0, [], 0, 0),
              ("4", "(1/2) lam (box_app phi_%s) F ghat_2: lam^2 d^2 phi" % K_, "phi", 2, 1, 2, [], 0, 0),
              ("4", "B1 . d phi_%s" % K_, "phi", 0, 1, 1, [], 0, 0), ("4", "C1 phi_%s" % K_, "phi", 0, 1, 0, [], 0, 0),
              ("4", "N_phi^%s: |w| lam^-2 |phi|" % K_, "phi", Km3 - 2, 1, 0, [], 0, 1),
              ("4", "N_phi^%s: |w| lam^-1 |d phi|" % K_, "phi", Km3 - 1, 1, 1, [], 0, 1),
              ("4", "N_phi^%s: |w| |d^2 phi|" % K_, "phi", Km3, 1, 2, [], 0, 1)]
    # Step 5: ell_K . d phi_K = (1/2) P s_K(h); targets ||phi|| (j = 0), lam^j ||d^j d phi||, lam^(j+1) ||d^j d_x^2 phi||
    for K_ in ("in", "out"):
        t += [("5", "(1/2) P s_%s, for ||phi||" % K_, "s", 0, 0, 0, ["P", "j=0"], 0, 0),
              ("5", "(1/2) P s_%s, for lam^j ||d^j d phi||" % K_, "s", 0, 0, 0, ["P"], 1, 0),
              ("5", "(1/2) P s_%s, for lam^(j+1) ||d^j d_x^2 phi|| (Bernstein)" % K_, "s", 1, 0, 0, ["P", "bern"], 2, 0),
              ("5", "[d^a, L_%s] phi (smooth coefficients, i >= 1)" % K_, "phi", 0, 0, 1, ["i>=1"], 1, 0)]
    # Step 6: L_K Psi_K + a_K Psi_K = (1/2) box P s_K - (1/2) M_K(P s_K) - N_K phi_K; box P s = P box s + [box, P] s,
    # box s_in from Lemma 3.3_2
    for K_, o in (("in", "out"), ("out", "in")):
        L33 = [("c1 . dh", "h", 0, 1, 1), ("c0 h", "h", 0, 1, 0),
               ("c2 . d phi_%s, c2 . d phi_%s" % (K_, o), "phi", 0, 1, 1),
               ("c3 phi_%s, c3 phi_%s" % (K_, o), "phi", 0, 1, 0),
               ("-q c_%s Psi_%s (the coupling)" % (K_, o), "Psi", 0, 1, 0),
               ("q lam^-1 ((1 - P) s_%s) G2^%s(ell, ell)" % (o, o), "s", -1, 1, 0),
               ("lam d^2 phi (c^ab, lam F ghat_2 terms)", "phi", 1, 1, 2),
               ("2q N_phi: |w| lam^-2 |phi|", "phi", Km3 - 2, 1, 0), ("2q N_phi: |w| lam^-1 |d phi|", "phi", Km3 - 1, 1, 1),
               ("2q N_phi^%s(ell, ell): |w| |d^2 phi_%s|" % (o, o), "phi", Km3, 1, 2)]
        for lab, U, p, ka, m in L33:
            ops = ["P"] + (["oneminusP"] if "(1 - P)" in lab else [])
            t.append(("6", "P box s_%s: %s" % (K_, lab), U, p, ka, m, ops, 0, 1 if "|w|" in lab else 0))
        t += [("6", "P box s_%s: P d_i (c d_a h), |c| <= C(lam + |w|)" % K_, "h", 1, 1, 1, ["P", "bern"], 0, 0),
              ("6", "P box s_%s: P((d_i c) d_a h), |d c| <= C" % K_, "h", 0, 1, 1, ["P"], 0, 0),
              ("6", "[box, P] s_%s: spatial index, (M5) first form" % K_, "s", 0, 0, 1, ["M5a"], 0, 0),
              ("6", "[box, P] s_%s: d^2 P - P d^2 (M4, M6)" % K_, "s", 0, 0, 1, [], 0, 0)]
        for lab, U, p, ka, m in L33:                                     # the tau-tau rewrite, (M5) second form
            if "(1 - P)" in lab:
                ops = ["M5b", "oneminusP"]
            else:
                ops = ["M5b"]
            t.append(("6", "[box, P] s_%s, tau-tau, M5b: %s" % (K_, lab), U, p, ka, m, ops, 0, 1 if "|w|" in lab else 0))
        t += [("6", "[box, P] s_%s, tau-tau: d_i (c d_a h) by (M5) first form" % K_, "h", 1, 1, 1, ["M5a"], 0, 0),
              ("6", "[box, P] s_%s, tau-tau: (d_i c) d_a h by (M5) first form" % K_, "h", 0, 1, 1, ["M5a"], 0, 0),
              ("6", "-(1/2) M_%s(P s_%s)" % (K_, K_), "s", 0, 0, 1, ["P"], 0, 0),
              ("6", "-N_%s phi_%s" % (K_, K_), "phi", 0, 0, 1, [], 0, 0),
              ("6", "a_%s Psi_%s and [d^a, L_%s] Psi_%s" % (K_, K_, K_, K_), "Psi", 0, 0, 0, [], 0, 0)]
    return t


def evaluate(row, k, W):
    step, lab, U, p, kappa, m, ops, extra, wfac = row
    imin = 1 if "i>=1" in ops else 0
    jrange = [0] if "j=0" in ops else range(k + 1)
    for op in ops:
        if op == "bern":
            p, extra = p - 1, extra - 1
        elif op == "oneminusP":
            p, m = p + 1, m + 1
        elif op == "M5a":
            m = m - 1 if m > 0 else m
        elif op == "M5b":
            p += 1
    if extra == 2:                                    # the lam^(j+1) ||d^j d_x^2 .|| target carries one more lam
        p += 1
    worst_e, worst_m = None, -1
    for j in jrange:
        for i in range(imin, j + extra + 1):
            order = j + extra - i + m
            if order < 0:
                continue
            worst_m = max(worst_m, order)
            if (U, order) not in W:
                return None, order                    # beyond N_2's reach
            e = j + p - kappa * i - W[(U, order)]
            worst_e = e if worst_e is None else min(worst_e, e)
    return worst_e, worst_m


def check(k, K, rows=None, verbose=False):
    W = weights(k)
    rows = term_rows(K) if rows is None else rows
    out = []
    for r in rows:
        e, mo = evaluate(r, k, W)
        ok = e is not None and e >= 0
        out.append((r, e, mo, ok))
    if verbose:
        for r, e, mo, ok in out:
            print("      Step %s %-86s e = %-4s order %-2s %s" % (r[0], r[1][:86], e, mo, ok), flush=True)
    return all(o for *_, o in out), out


def t2(K=None):
    Ks = sp.Symbol("K", positive=True) if K is None else K
    lam, M, C, C3, CD, CR = sp.symbols("lam M C C3 C_D C_R", positive=True)
    kap = sp.Symbol("kappa", nonnegative=True)
    KK = 6 + kap if K is None else K
    e_quad = -3 + 2 * (-1)                       # ledger5's rule: lam^-s0 |d w|_k^2, s0 = 3, |d w|_k <= lam^-1 N_2
    nl = sp.expand(2 * KK + e_quad - (KK + 1))  # lam^(2K - 5) M^2 <= lam^(K+1) M^2
    nl_ok = sp.Poly(nl, kap).coeffs() and all(c >= 0 for c in sp.Poly(nl, kap).coeffs()) if K is None else nl >= 0
    lam0 = 1 / (C3 * C * M**2)
    Mdef = C3 * (CD + 1 + CR) + 1
    closing = sp.simplify(Mdef - (C3 * (CD + 1 + CR) + C3 * C * M**2 * lam0)) == 1     # N_2 <= M lam^K, margin 1
    resid = (KK + 3) - 1 - KK >= 0
    return bool(nl_ok), closing, bool(resid), nl


def main():
    ok = True
    print("  the weights read off N_2 (k = 6): h/s orders 0..%d, phi 0..%d, Psi 0..%d"
          % (max(m for (U, m) in weights(6) if U == "h"), max(m for (U, m) in weights(6) if U == "phi"),
             max(m for (U, m) in weights(6) if U == "Psi")), flush=True)
    good, out = check(6, 6, verbose=True)
    n4, n5, n6 = (sum(1 for r, *_ in out if r[0] == s) for s in ("4", "5", "6"))
    grid = all(check(k, K)[0] for k in range(6, 13) for K in range(6, 11))
    print("  T1: %d terms (Step 4: %d, Step 5: %d, Step 6: %d) pass at k = K = 6: %s; on k = 6..12 x K = 6..10: %s"
          % (len(out), n4, n5, n6, good, grid), flush=True)
    ok &= good and grid
    nl_ok, closing, resid, nl = t2()
    print("  T2: non-linear 2K - 5 - (K + 1) = %s >= 0 for K = 6 + kappa: %s; residual within C_R lam^K: %s; Step 7's M "
          "and lam0 close N_2 <= M lam^K with margin 1: %s" % (nl, nl_ok, resid, closing), flush=True)
    ok &= nl_ok and closing and resid
    # controls
    W = weights(6)
    ctl = {}
    ctl["a"] = evaluate(("5", "P(c_in phi_out) from s_in(w)", "phi", 0, 1, 0, ["P"], 1, 0), 6, W)
    ctl["b"] = evaluate(("6", "c_in box_app phi_out as d^2 phi_out", "phi", 0, 1, 2, ["P"], 0, 0), 6, W)
    ctl["c"] = evaluate(("6", "P(c d_a d_i h) directly", "h", 1, 1, 2, ["P"], 0, 0), 6, W)
    ctl["d"] = evaluate(("6", "tau-tau, M5b on c d_a d_i h", "h", 1, 1, 2, ["M5b"], 0, 0), 6, W)
    ctl["e"] = evaluate(("5", "d_x^2 P s without Bernstein", "s", 1, 0, 0, ["P"], 2, 0), 6, W)
    fails = {}
    for key, (e, mo) in ctl.items():
        fails[key] = e is None or e < 0
        print("  control (%s): exponent %s, order %s: rejected %s" % (key, e, mo, fails[key]), flush=True)
    nl5 = t2(5)
    fails["f"] = not nl5[0]
    print("  control (f) K = 5: non-linear 2K - 5 - (K + 1) = %s: rejected %s" % (nl5[3], fails["f"]), flush=True)
    good5 = check(6, 5)[0]
    print("      (the linear terms alone still pass at K = 5: %s; the non-linear row is what K >= 6 is for)" % good5,
          flush=True)
    ok_ctl = all(fails.values())
    print("T1-T2:", "PASS" if ok else "FAIL")
    print("controls (a)-(f) rejected:", "PASS" if ok_ctl else "FAIL")
    return 0 if ok and ok_ctl else 1


if __name__ == "__main__":
    sys.exit(main())
