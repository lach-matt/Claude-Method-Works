#!/usr/bin/env python3
"""support8b.py -- computations behind five more deduced steps of the paper's section 8 (sections 8.4, 8.7, 8.8).

  M1 (exact, sympy) section 8.8's 'the antipodal map of the four spatial directions is a rotation by half a turn in
     both planes of rotation, so it is an isometry of every five-dimensional Myers-Perry metric; translations are odd
     under it and rotations even' (supplement proof5/PART-III-I16-BASEPOINTS.md (P3) and (I9)), and section 8.7's
     G-invariant data needing no parity condition. The half-turns in the (x1, x2) and (x3, x4) planes compose to -I
     (so -I lies in G = O(2) x O(2)); the Myers-Perry metric in Kerr-Schild form at symbolic spins (a, b) and mass mu
     (checks/mpdata5.py's mp_ingredients, along x = omega/rho) satisfies P* g = g for P = -I on the spatial factor,
     component by component, exactly. The parity of each of the fifteen KIDs of flat data (proof5/PART-V-GLUING.md
     (0.4): e_0 = (0, 1), e_l = (d_l, 0), e_ab = (W_ab x, 0), e'_l = (0, x^l)) under push-forward by -I: e_0 and the six
     rotations even, the four translations and the four boosts odd. Control: x1 -> -x1 alone is not an isometry at
     nonzero spin (a g_t2 component changes at a rational point, a = 1/3).
  M2 (exact, sympy) section 8.7's 'the data of g_lam on Hintz's initial surface near the hole ... are small in every
     norm his theorem uses' (supplement N1STAR-PROOF.md 10.50 (b)-(d), with section 1's (1.1)). The implications, with
     r_q(mu) = (sqrt72 mu l5^2)^(1/4), q0 = r_q(mu0), a = q0 - delta0, V = v_end + T, tau_end >= V - r_q(mu_end):
     the seed condition mu0 >= sqrt72 l5^2 gives q0 <= sqrt(mu0); a < q0; mu_end - mu0 = (2/9) A^2 int env^2 > 0;
     T > r_q(mu_end) - a gives v_end - a < tau_end, so tau1 exists; on {tau = tau1} with r >= a, v = tau1 + r > v_end;
     and (d)'s unscaled bound M lam^(K - j) is at most M lam for j <= d <= K - 1 and 0 < lam <= 1, which is (d)'s
     O(lam) (an enumeration over d <= 8). Each also at a rational instance (l5 = 1, mu0 = 9, mu_end = 10). Control: T =
     r_q(mu_end) - a - 1/10 leaves the certificate v_end - a < V - r_q(mu_end) false.
  M3 (exact, sympy) section 8.7's 'a bump of relative size R^(-1) at radius R costing about R^(l0-3) there' (supplement
     proof5/PART-VII-ASSEMBLY.md (VII6)). The norm is that of rho^(l0) H_b (Theorem 4 (ii); III.K Theorem 4.3) with the
     b-density dr/r dw of PART-III-A-PREREQ.md 1.1: it is the density for which PART-VII's Lemma 0.1 step rho^4 C^oo in
     rho^(l0) H_b holds at l0 < 4 (computed: finite at l0 = 7/2 with it, infinite with |dx|). 'Relative size R^(-1)' is
     read against Tangherlini's deviation at radius R, mu r^-2 in the metric and r^-3 in k: f_R = R^-3 chi(r/R) and k_R
     = R^-4 chi(r/R). For a generic chi, r = R s factors ||r^(l0) f_R||^2 = R^(2 l0 - 6) int s^(2 l0 - 1) chi^2 ds, and
     the weight r^(l0 + 1) on k_R gives the same power; (r d_r)^j chi(r/R) = ((s d_s)^j chi)(r/R) for j = 1, 2, so every
     H_b^m norm scales alike; checked again at a concrete chi at l0 = 7/2, 13/4, R = 2, 3. Both readings are printed:
     the literal amplitude R^-1 costs R^(l0-1). Control (discriminating): asserting R^(l0-3) under that literal
     reading fails, since it gives R^(l0-1).
  M4 (computed, a census) sections 8.4 and 8.8's 'the iteration with alpha in (4 + eps_K - eps'_0, 4 + eps_K] and rate
     alpha - 2' and 'a consistent choice of the parameters ... in an order with no circular threshold' (proof5/PART-VI4-
     PARAMS.md). Its section 1 table is parsed (18 rows, the column 'threshold depends on', ranges such as c1-c3 and 'all
     the above' expanded) into a directed graph, sorted topologically (graphlib), and Theorem 2.1's steps (0)-(6) checked
     to be a linear extension of it (u1, which no step names, placed with the gauge in step (2)). Then exactly: (C5)
     gamma_C v_C >= 1/2 and s_C > 100 at (v_C, e_C) = (1/2, 1/102400) for every gamma_C > 10^6; z_Ups = 4 e_Ups
     gamma_Ups^2 <= 1/2 at gamma_Ups = 1/4, e_Ups = 1 (it increases in both); at the record's point (e_Ups, gamma_Ups)
     = (1/100, 1/100) row u4's bounds, z_Ups = 4 x 10^-6 and 3/2 + delta_sharp = 1.5099 (section 8.4's alpha_min);
     eps_ind <= 1.94137 x 10^-8 (read from N1STAR-PROOF.md 10.52, the point's value, which row w1's eps_ind is) and
     eps_ind < 3 x 10^-6 < delta_sharp, so row w1's eps_+ < min(delta_sharp, eps_ind) has room;
     row d2's interval nonempty; eps'_0 = (1/2) min(eps_K, eps_+ - eps_K) (PART-III-I11-SPACETIME.md) in (0, eps_K), so
     every alpha of row w2 has rate alpha - 2 > 2. Control: a planted edge (c1 depending on n1) makes a cycle, which
     the sort detects.
  M5 (computed, a census) section 8.8's counts. DEDUCTIONS.tsv (category, final), B-MAP.tsv (places, reading),
     READINGS.tsv (the roots and their status), 10.75's item list (N1STAR-PROOF.md) and proof5/BASEPOINT-LEDGER.md's
     batch table give: 248 = 90 D + 29 A + 31 C + 38 ? + 60 B; 61 modification steps (60 + the one ? row placed as B);
     57 naming places and 4 none; 45 short and 16 long write-outs (10.75's list of 61 items and its sixteen); 34 taking
     a reading; the 38 as 12 with no step of their own, 25 at proof level and 1 modification step; ten roots as 5 own
     (settled) + 2 groups written out + 1 READ + 2 at every n (RB, RU: 10.77); 7,577 lines in the five batches. Every
     count is compared with the paper's. Control: a planted D row moves the 90 and the 248.

Labels: computed (exact, sympy; the censuses by parsing the files named). Reach: M2 checks the implications 10.50 states,
not Theorem E or the gluing; M4 checks the table's order and the stated inequalities, not the existence statements each
row cites; M5 counts the files, not the classification each row records.

Run: python3 checks/support8b.py   (about six seconds)
"""
import csv
import graphlib
import os
import re
import sys
import textwrap

import sympy as sp

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
P5 = os.path.join(HERE, "proof5")


def rot(th):
    return sp.Matrix([[sp.cos(th), -sp.sin(th)], [sp.sin(th), sp.cos(th)]])


def m1(control=False):
    sys.path.insert(0, os.path.join(HERE, "checks"))
    import mpdata5 as md
    om, rho, a, b, mu = md.w, md.rho, md.a, md.b, md.mu
    u, h, k, eq = md.mp_ingredients(om, a, b)
    K = [sp.Integer(1)] + k
    g = [[(-1 if i == j == 0 else (1 if i == j else 0)) + h * K[i] * K[j] for j in range(5)] for i in range(5)]
    J = [-1, 1, 1, 1] if control else [-1, -1, -1, -1]
    lam = [1] + J
    sub = {om[i]: J[i] * om[i] for i in range(4)}
    diffs = [lam[i] * lam[j] * g[i][j].subs(sub, simultaneous=True) - g[i][j] for i in range(5) for j in range(i, 5)]
    if control:
        pt = {om[0]: sp.Rational(1, 2), om[1]: sp.Rational(1, 2), om[2]: sp.Rational(1, 2), om[3]: sp.Rational(1, 2),
              rho: sp.Rational(1, 2), a: sp.Rational(1, 3), b: sp.Rational(1, 5), mu: 1}
        return all(sp.N(d_.subs(pt), 30) == 0 for d_ in diffs)
    iso = all(sp.expand(sp.together(d_)) == 0 for d_ in diffs)
    half = sp.diag(rot(sp.pi), rot(sp.pi)) == -sp.eye(4)
    x = sp.symbols("x1:5", real=True)
    X = sp.Matrix(x)
    neg = {x[i]: -x[i] for i in range(4)}

    def push(Y, N):                                                    # (P_* Y)(x) = -Y(-x), N -> N(-x), P = -I
        return -Y.subs(neg, simultaneous=True), N.subs(neg, simultaneous=True)

    def parity(Y, N):
        Y2, N2 = push(Y, N)
        if sp.expand(Y2 - Y) == sp.zeros(4, 1) and sp.expand(N2 - N) == 0:
            return "even"
        if sp.expand(Y2 + Y) == sp.zeros(4, 1) and sp.expand(N2 + N) == 0:
            return "odd"
        return "neither"
    kids = [("e_0 (d_t)", sp.zeros(4, 1), sp.Integer(1))]
    kids += [("e_%d (translation)" % (l + 1), sp.eye(4)[:, l], sp.Integer(0)) for l in range(4)]
    for i in range(4):
        for j in range(i + 1, 4):
            W = sp.zeros(4, 4)
            W[i, j], W[j, i] = 1, -1
            kids.append(("e_%d%d (rotation)" % (i + 1, j + 1), W * X, sp.Integer(0)))
    kids += [("e'_%d (boost)" % (l + 1), sp.zeros(4, 1), x[l]) for l in range(4)]
    par = [(n_, parity(Y, N)) for n_, Y, N in kids]
    want = {"d_t": "even", "translation": "odd", "rotation": "even", "boost": "odd"}
    par_ok = len(par) == 15 and all(p == want[n_.split("(")[1][:-1]] for n_, p in par)
    nev = sum(p == "even" for _, p in par)
    print("  M1: half-turns in both planes compose to -I: %s; P* g_MP = g_MP for P = -I, all 15 components, symbolic\n"
          "      (a, b, mu): %s; the 15 KIDs of (0.4) under -I:" % (half, iso), flush=True)
    for n_, p in par:
        print("        %-22s %s" % (n_, p), flush=True)
    print("      %d even, %d odd; translations and boosts odd, d_t and rotations even: %s" % (nev, 15 - nev, par_ok),
          flush=True)
    return half and iso and par_ok


def m2(control=False):
    mu0, l5, d0, A, Ienv, eps, eta, t, lam, M = sp.symbols("mu0 l5 delta0 A Ienv epsilon eta t lam M", positive=True)
    vend = sp.Symbol("v_end", real=True)
    s = sp.Symbol("s", nonnegative=True)

    def rq(m):
        return (sp.sqrt(72) * m * l5**2)**sp.Rational(1, 4)
    q0 = rq(mu0)
    a = q0 - d0
    mu_end = mu0 + sp.Rational(2, 9) * A**2 * Ienv
    T = rq(mu_end) - a + (-sp.Rational(1, 10) if control else eps)
    V = vend + T
    cert = sp.simplify(V - rq(mu_end) - (vend - a))                   # tau_end >= V - r_q(mu_end): this minus (v_end-a)
    if control:
        return bool(cert > 0)
    seed = sp.expand((mu0**2 - q0**4).subs(mu0, sp.sqrt(72) * l5**2 + s))   # sqrt(mu0)^4 - q0^4 at mu0 = seed + s
    seed_ok = sp.factor(seed) == sp.factor((sp.sqrt(72) * l5**2 + s) * s) and seed.is_nonnegative
    a_ok = sp.simplify(q0 - a) == d0
    mu_ok = sp.simplify(mu_end - mu0).is_positive
    t_ok = cert == eps
    tau1 = vend - a + eta
    v_ok = sp.simplify(tau1 + (a + t) - vend) == eta + t              # r = a + t, t >= 0
    d_ok = True
    for d in range(0, 9):
        for Kk in range(d + 1, d + 4):
            for j in range(0, d + 1):
                e_ = Kk - j - 1                                        # M lam^(K-j) = M lam * lam^e_, e_ >= 0
                d_ok &= e_ >= 0 and all(sp.Rational(p, 7)**e_ <= 1 for p in range(1, 8))
    d_tight = sp.simplify((M * lam**(sp.Integer(5) - 4)) / lam) == M  # j = d = K - 1: the bound is M lam exactly
    inst = {l5: 1, mu0: 9, A: 1, Ienv: sp.Rational(9, 2), d0: q0.subs({l5: 1, mu0: 9}) / 2, eps: sp.Rational(1, 10)}
    i_seed = bool(sp.sqrt(9) - q0.subs(inst) >= 0)
    i_mu = mu_end.subs(inst) == 10
    i_cert = bool(cert.subs(inst) > 0)
    print("  M2: q0 <= sqrt(mu0) under the seed (mu0^2 - q0^4 = mu0 s, s = mu0 - sqrt72 l5^2 >= 0): %s; a < q0: %s;\n"
          "      mu_end > mu0: %s; T > r_q(mu_end) - a => v_end - a < V - r_q(mu_end) <= tau_end (margin = %s): %s;\n"
          "      on tau = tau1, r >= a: v - v_end = eta + (r - a) > 0: %s; M lam^(K-j) <= M lam for j <= d <= K - 1,\n"
          "      0 < lam <= 1 (d <= 8): %s, attained at j = K - 1 (so O(lam), not <= lam): %s; instance\n"
          "      (l5, mu0, mu_end) = (1, 9, 10): seed %s, mu_end %s, certificate %s"
          % (seed_ok, a_ok, mu_ok, cert, t_ok, v_ok, d_ok, d_tight, i_seed, i_mu, i_cert), flush=True)
    return all([seed_ok, a_ok, mu_ok, t_ok, v_ok, d_ok, d_tight, i_seed, i_mu, i_cert])


def m3(control=False):
    r, R, sv, l0, rho = sp.symbols("r R s l0 rho", positive=True)
    chi = sp.Function("chi")

    def power(weight, amp):
        """the exponent p with ||weight * amp * chi(r/R)||_(L^2(dr/r)) = R^p * (an R-free constant)"""
        I = sp.Integral(weight**2 * amp**2 * chi(r / R)**2 / r, (r, 0, sp.oo)).transform(r, (R * sv, sv))
        f = sp.powsimp(sp.expand_power_base(I.function, force=True), force=True)
        c, rest = f.as_independent(sv)
        p2 = sp.simplify(sp.log(sp.powsimp(c, force=True)).expand(force=True) / sp.log(R))
        free = not sp.simplify(rest).has(R)
        return sp.simplify(p2 / 2), free
    if control:
        p, free = power(r**l0, R**-1)                                  # the literal reading: amplitude R^-1
        print("  M3 control: literal amplitude R^-1 gives R^(%s); asserted R^(l0-3)" % p, flush=True)
        return sp.simplify(p - (l0 - 3)) == 0
    p_g, f_g = power(r**l0, R**-3)
    p_k, f_k = power(r**(l0 + 1), R**-4)
    p_lit, _ = power(r**l0, R**-1)                                     # the literal amplitude R^-1, for the record
    p_leb = sp.simplify(power(r**l0 * r**2, R**-3)[0])                # |dx| = r^4 dr/r dw on R^4
    bder, Fr, Fs = True, chi(r / R), chi(sv)
    for j in (1, 2):                                                   # (r d_r)^j chi(r/R) against ((s d_s)^j chi)(r/R)
        Fr, Fs = r * sp.diff(Fr, r), sv * sp.diff(Fs, sv)
        bder &= sp.simplify((Fr - Fs.subs(sv, r / R)).doit()) == 0
    conc = True
    cs = (sv - sp.Rational(1, 2))**2 * (2 - sv)**2                     # a concrete bump on [1/2, 2]
    for L0 in (sp.Rational(7, 2), sp.Rational(13, 4)):
        Js = sp.integrate(sp.expand(sv**(2 * L0 - 1) * cs**2), (sv, sp.Rational(1, 2), 2))
        for RR in (2, 3):
            Ir = sp.integrate(sp.expand(r**(2 * L0 - 1) * sp.Integer(RR)**-6 * cs.subs(sv, r / RR)**2),
                              (r, sp.Rational(RR, 2), 2 * RR))
            conc &= sp.simplify(Ir - sp.Integer(RR)**(2 * L0 - 6) * Js) == 0
    b_fin = sp.integrate(rho**(2 * (4 - sp.Rational(7, 2))) / rho, (rho, 0, 1)).is_finite
    l_fin = sp.integrate(rho**(2 * (4 - sp.Rational(7, 2))) * rho**-4 / rho, (rho, 0, 1)).is_finite
    ok = sp.simplify(p_g - (l0 - 3)) == 0 and sp.simplify(p_k - (l0 - 3)) == 0 and f_g and f_k
    print("  M3: rho^4 C^oo in rho^(7/2) H_b near rho = 0: with dr/r dw %s, with |dx| %s; ||r^l0 R^-3 chi(r/R)||_b ~\n"
          "      R^(%s), ||r^(l0+1) R^-4 chi(r/R)||_b ~ R^(%s), R-free remainders: %s; (r d_r)^j chi(r/R) = ((s d_s)^j\n"
          "      chi)(r/R), j = 1, 2: %s; concrete chi, l0 = 7/2, 13/4, R = 2, 3: %s; for the record, amplitude R^-1:\n"
          "      R^(%s); Lebesgue |dx|, amplitude R^-3: R^(%s)"
          % (b_fin, l_fin, p_g, p_k, f_g and f_k, bder, conc, p_lit, p_leb), flush=True)
    return ok and bder and conc and b_fin and not l_fin


def vi4_table():
    rows = []
    for line in open(os.path.join(P5, "PART-VI4-PARAMS.md"), encoding="utf-8"):
        m_ = re.match(r"\| ([cubwdn]\d) \|", line)
        if m_:
            rows.append((m_.group(1), line.rstrip().rstrip("|").split("|")[-1].strip()))
    return rows


def deps_of(rid, text, order):
    if "all the above" in text:
        return order[:order.index(rid)]
    out = []
    for L, i, j in re.findall(r"\b([cubwdn])(\d)(?:-\1?(\d))?\b", text):
        out += ["%s%d" % (L, n_) for n_ in range(int(i), int(j or i) + 1)]
    return out


def m4(control=False):
    rows = vi4_table()
    order = [r_ for r_, _ in rows]
    graph = {r_: set(deps_of(r_, t, order)) for r_, t in rows}
    if control:
        graph["c1"].add("n1")                                          # planted: a circular threshold
    known = all(d_ in graph for ds in graph.values() for d_ in ds)
    try:
        topo = list(graphlib.TopologicalSorter(graph).static_order())
        acyclic = True
    except graphlib.CycleError:
        acyclic = False
    if control:
        return acyclic
    step = {"b1": 0, "c1": 1, "c2": 1, "c3": 1, "c4": 1, "u1": 2, "u2": 2, "u3": 2, "u4": 2, "u5": 2, "d1": 3, "d2": 3,
            "w1": 4, "w2": 4, "b2": 5, "b3": 5, "b4": 5, "n1": 6}
    ext = all(step[d_] < step[r_] or (step[d_] == step[r_] and order.index(d_) < order.index(r_))
              for r_, ds in graph.items() for d_ in ds)
    eK, e1 = sp.symbols("eps_K e1", positive=True)
    vC, eC = sp.Rational(1, 2), sp.Rational(1, 102400)
    gam = 10**6 + e1                                                   # every gamma_C > 10^6
    sC = (1 - eC) * (1 - vC) * gam
    c5 = sp.simplify(gam * vC - sp.Rational(1, 2)).is_positive and sp.simplify(sC - 100).is_positive
    gu, eu = sp.symbols("gamma_U e_U", positive=True)
    z_ok = sp.simplify(sp.Rational(1, 2) - 4 * eu * gu**2).subs({gu: sp.Rational(1, 4), eu: 1}) >= 0
    eU, gU = sp.Rational(1, 100), sp.Rational(1, 100)
    u4 = gU < min(sp.Rational(3, 8), sp.Rational(1, 4), sC.subs(e1, 0) / 2)
    zU = 4 * eU * gU**2
    dsh = (1 - eU) * gU
    rec = zU == sp.Rational(4, 10**6) and 0 < zU <= sp.Rational(1, 2) and sp.Rational(3, 2) + dsh == sp.Rational(
        15099, 10000)
    d2 = all(3 < min(L, sp.Rational(3, 2) + sC.subs(e1, 0)) for L in (sp.Rational(301, 100), sp.Rational(399, 100)))
    s52 = open(os.path.join(HERE, "N1STAR-PROOF.md"), encoding="utf-8").read().split("### 10.52 ")[1]
    m_ = re.search(r"eps_ind at most (\d)\.(\d+) x 10\^-(\d+)", s52.split("\n### ")[0])
    eind = sp.Rational(int(m_.group(1) + m_.group(2)), 10**(len(m_.group(2)) + int(m_.group(3))))
    epsind_ok = 0 < eind < sp.Rational(3, 10**6) < dsh                # eps_ind < 3e-6 < delta_sharp: eps_+ room
    ok_w = True
    for EK, EP in [(sp.Rational(1, 10**7), sp.Rational(2, 10**7)), (sp.Rational(1, 10**7), sp.Rational(29, 10**7)),
                   (sp.Rational(2, 10**6), sp.Rational(25, 10**7))]:
        e0p = sp.Rational(1, 2) * min(EK, EP - EK)
        ok_w &= 0 < e0p < EK and (4 + EK - e0p) - 2 > 2
    gap = sp.Symbol("x", positive=True)                                # x = eps_+ - eps_K > 0; min is eps_K or x < eps_K
    e0_sym = (eK / 2 - eK).is_negative and (gap / 2 - eK).subs(gap, eK - e1).is_negative
    print("  M4: %d rows parsed, every dependency a row: %s; acyclic: %s; a topological order:\n        %s;\n"
          "      Theorem 2.1's steps (0)-(6) a linear extension: %s; (C5) and s_C > 100 for gamma_C > 10^6: %s;\n"
          "      z_Ups <= 1/2 at the extremes gamma_Ups = 1/4, e_Ups = 1: %s; record point: u4 %s, z_Ups = %s, 3/2 +\n"
          "      delta_sharp = %s: %s; d2 nonempty: %s; eps_ind <= %s (10.52) < 3e-6 < delta_sharp: %s;\n"
          "      eps'_0 in (0, eps_K), rate alpha - 2 > 2 on row w2 (three witnesses; eps'_0 <= eps_K/2 < eps_K\n"
          "      symbolically): %s, %s"
          % (len(rows), known, acyclic, " ".join(topo), ext, c5, z_ok, u4, zU, sp.Rational(3, 2) + dsh, rec, d2,
             sp.Float(eind, 6), epsind_ok, ok_w, e0_sym), flush=True)
    return all([len(rows) == 18, known, acyclic, ext, c5, z_ok, u4, rec, d2, epsind_ok, ok_w, e0_sym])


ROMAN = {"i": 1, "v": 5, "x": 10, "l": 50}


def roman(s):
    v = 0
    for i, ch in enumerate(s):
        n_ = ROMAN[ch]
        v += -n_ if i + 1 < len(s) and ROMAN[s[i + 1]] > n_ else n_
    return v


def tsv(name):
    return list(csv.DictReader(open(os.path.join(HERE, name), encoding="utf-8"), delimiter="\t"))


PAPER = {"deduced": 248, "D": 90, "A": 29, "C": 31, "?": 38, "B": 60, "modification": 61, "places named": 57,
         "places none": 4, "short": 45, "long": 16, "reading": 34, "no step": 12, "proof level": 25, "one more B": 1,
         "roots": 10, "own": 5, "groups": 2, "READ": 1, "every n": 2, "lines": 7577}


def m5(control=False):
    ded = tsv("DEDUCTIONS.tsv")
    if control:
        ded = ded + [dict(ded[0], category="D", final="D")]            # planted: one more D row
    bmap, rd = tsv("B-MAP.tsv"), tsv("READINGS.tsv")
    got = {"deduced": len(ded)}
    for c in "DACB?":
        got[c] = sum(x["category"] == c for x in ded)
    got["modification"] = sum(x["final"] == "B" for x in ded)
    q = [x["final"] for x in ded if x["category"] == "?"]
    got["no step"] = sum(f in ("S", "N") for f in q)                   # summaries and four-dimensional remarks (10.73)
    got["proof level"] = sum(f in ("D", "A", "E", "G", "H") for f in q)
    got["one more B"] = q.count("B")
    got["places none"] = sum(x["places"] == "none" for x in bmap)
    got["places named"] = len(bmap) - got["places none"]
    got["reading"] = sum(x["reading"] == "yes" for x in bmap)
    text = open(os.path.join(HERE, "N1STAR-PROOF.md"), encoding="utf-8").read()
    sec = text.split("### 10.75 ")[1].split("\n### ")[0]
    items = [roman(m_) for m_ in re.findall(r"^ \(([ivxl]+)\) 10\.\d+", sec, re.M)]
    longs = sec.split("The sixteen carry longer runs of proof")[1].split("\n\n")[0]
    lr = set()
    for i, j in re.findall(r"\(([ivxl]+)\)(?:-\(([ivxl]+)\))?\s", longs):
        lr |= set(range(roman(i), roman(j or i) + 1))
    got["long"] = len(lr)
    got["short"] = len(items) - len(lr) if items == list(range(1, len(items) + 1)) else -1
    status = {}
    for x in rd:
        for r1, r2, st in re.findall(r"\b(R[A-Z])\b(?: and (R[A-Z]))? (settled|written out|READ)", x["through"]):
            for r_ in (r1, r2):
                if r_:
                    status.setdefault(r_, set()).add(st)
    every_n = {"RB", "RU"}                                             # 10.77: 'both are the same at every n'
    got["roots"] = len(status)
    got["own"] = sum(st == {"settled"} for st in status.values())
    got["READ"] = sum(st == {"READ"} for st in status.values())
    got["every n"] = sum(r_ in every_n and st == {"written out"} for r_, st in status.items())
    got["groups"] = sum(r_ not in every_n and st == {"written out"} for r_, st in status.items())
    led = open(os.path.join(P5, "BASEPOINT-LEDGER.md"), encoding="utf-8").read()
    batch = re.findall(r"^\| \d \| [^|]+ \| ([\d,]+) \|", led, re.M)
    got["lines"] = sum(int(n_.replace(",", "")) for n_ in batch)
    bad = {k_: (PAPER[k_], got.get(k_)) for k_ in PAPER if got.get(k_) != PAPER[k_]}
    if control:
        return not bad
    sums = (got["D"] + got["A"] + got["C"] + got["?"] + got["B"] == got["deduced"]
            and got["no step"] + got["proof level"] + got["one more B"] == got["?"]
            and got["B"] + got["one more B"] == got["modification"] == len(bmap) == len(items)
            and got["own"] + got["groups"] + got["READ"] + got["every n"] == got["roots"])
    print(textwrap.fill("M5: counts in the files, each equal to the paper's unless listed below: " + "; ".join(
        "%s %s" % (k_, got[k_]) for k_ in PAPER), 118, initial_indent="  ", subsequent_indent="      "), flush=True)
    print(textwrap.fill("roots by status: %s; 10.75's items numbered 1-%d, %d of them long; READINGS.tsv %d rows "
                        "(the 34 and five on none); batches %s; sums consistent: %s; mismatches: %s"
                        % (", ".join("%s %s" % (r_, "/".join(sorted(s_))) for r_, s_ in sorted(status.items())),
                           len(items), len(lr), len(rd), "+".join(batch), sums, bad or "none"),
                        118, initial_indent="      ", subsequent_indent="      "), flush=True)
    return not bad and sums


CHECKS = [("M1", m1), ("M2", m2), ("M3", m3), ("M4", m4), ("M5", m5)]


def main():
    ok = True
    for name, f in CHECKS:
        good = f()
        ctl = f(control=True)
        print("%s %s%s" % (name, "PASS" if good and not ctl else "FAIL", " (control passed)" if ctl else ""),
              flush=True)
        ok &= good and not ctl
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
