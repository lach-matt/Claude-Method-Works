"""r6edits5.py -- SETTLE-GLAM5 round 6: the final replacement text for N1STAR-PROOF.md's Lemma 11.0 (R6-D), applied to
a copy of the live file, and the mathematics it states checked, not only its phrases (the round-5 reader's surviving
mutants E-m5 and E-m6 passed r5edits5 E1, which read phrases only).

  E1 (text) R6-D's four blocks, read from SETTLE-GLAM5.md as printed there, applied to a copy of the live
     N1STAR-PROOF.md (the file is not edited): each old block occurs exactly once, every line of the edited file is
     within 121 characters, nothing outside Lemma 11.0 changes, and the edited Lemma 11.0 satisfies r5edits5's
     predicates (a)-(f) and four more: (g) "gamma' <= gamma" at both Leibniz sums; (h) the family is indexed by delta
     (gamma' is not reused); (i) f_gamma^n, b^n, c^n and R_gamma^n are defined; (j) ||R_gamma^n|| <= C(lam, j) t^(-3/2)
     uniformly in n is stated, with its reason. Control: on the live, unedited Lemma 11.0 every predicate fails.
  E2 (exact, sympy) what the edited text states, every quantity read from the text by a pattern:
     E2a Leibniz's rule with the sign, the coefficient and the binomial factor read from both sums: for generic g, u of
         (x, y) and every gamma of order 1..3, -(1/2) g d_x^2 d^gamma u = d^gamma(-(1/2) g d_x^2 u) + s c sum_{0 <
         gamma' <= gamma} B (d^gamma' g) d^(gamma - gamma') d_x^2 u holds exactly (s, c, B as read).
     E2b the bounds read for ||b . d U|| and ||c U|| have the lam- and t-powers of the coefficients the text defines:
         b of lam-order 0 in E_(3/2), and c's leading term -(1/2) lam^p (.)(ell, ell) [d_th^2 W_TT] with p read and
         W_TT ~ r^(-3/2) (read from "lam [W_TT] = r^(-3/2) G_3" before the lemma): on the model
         c = -(1/2) lam^p K(ell, ell) d_th^2 (r^(-3/2) w(theta)), w = sin, its supremum over the phase is
         (1/2) lam^p |K(ell, ell)| r^(-3/2) (exact), and on P+ r ~ t; both sides of the Lemma 9.3(b) step carry it.
     E2c the Gronwall kernel read ("exp(int C(1 + lam^q) t^(e))") is the sum of the two bounds read, and so is
         ||f_gamma||'s.
     E2d the factor read ("at most e^(...) over the far region t >= lam^-2") equals exp of
         int_(lam^-2)^oo (the kernel read) dt, computed (2C(1 + lam)), and is bounded as lam -> 0.
     E2e Gronwall's lemma in integral form on the model: y(tau) = y0 + int kappa y has y = y0 exp(int kappa) (exact),
         and the solutions of y' = kappa y - g with g >= 0 lie below it (20 sampled g).
     E2f Edit 2's closing bound, read: int_(tau_n)^tau t'^(-3/2) dtau' = 2 (t^(-1/2) - t_n^(-1/2)) <= 2 t^(-1/2) with
         t = 1 + tau0 - tau, tau_n < tau (exact), and t_n^(-1/2) <= t^(-1/2).
     E2g the L^2 norms on Sigma_tau cap P+ = {t + a1 <= r <= t + a2} x S^3 (measure r^3 dr domega): a field in E_q has
         norm ~ t^(3/2 - q) (exact leading power): E_3 gives the t^(-3/2) read for R_gamma's source, a derivative in
         E_2 the t^(-1/2) read for the lower steps' energies, and a product (E_(3/2) or E_2) x t^(-1/2) at most
         t^(-2) <= t^(-3/2): the bound read for ||R_gamma|| is the largest of them.
     E2h the bookkeeping inequality read ("floor((N + 2)/2) <= max(4, N - 3)") holds for N = 1..2000.
  E3 controls: the text under test mutated in memory, each mutation must make E1 or E2 fail: c U's bound lam^-1 ->
     lam^-3 (the reader's E-m5), the factor -> e^(2C/lam) (E-m6), the coefficient 1/2 of the |gamma'| = 1 sum dropped,
     C(gamma, gamma') dropped at the |gamma'| >= 2 sum, R_gamma's source E_3 -> E_(5/2), and max(4, N - 3) ->
     max(4, N - 4).
Labels: E1 text checks; E2 exact (sympy), E2e partly sampled.

    python3 checks/r6edits5.py     (about a minute)
"""
import os
import random
import re
import sys

import sympy as sp
from sympy.parsing.sympy_parser import (implicit_multiplication_application, parse_expr,
                                        standard_transformations)

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
import r5edits5 as R5E  # noqa: E402

FAIL = []
print = R5E.print


def check(name, ok, msg=""):
    print(f"  {name}: {'pass' if ok else 'FAIL'} {msg}")
    if not ok:
        FAIL.append(name)


def section_blocks(text, head, nxt):
    a = text.index(head)
    b = text.index(nxt, a)
    blocks = re.findall(r"```text\n(.*?)\n```", text[a:b], flags=re.S)
    assert len(blocks) == 4, len(blocks)
    return blocks


def norm(L):
    return re.sub(r"\s+", " ", L)


# ================================================================ the mathematics, read from a text

LAM, C, T, TN = sp.symbols("lam C t t_n", positive=True)


def frac(s):
    return sp.Rational(s)


def read_sums(L):
    """the Leibniz sums: (sign, coefficient, index condition, binomial present)"""
    pat = (r"([+-]) \((\d+)/(\d+)\) sum_\{([^}]*)\} (C\(gamma, gamma'\) )?\(d\^\{gamma'\} g_lam\^\{ab\}\)"
           r" d\^\{gamma - gamma'\} d_a d_b u_1")
    out = []
    for m in re.finditer(pat, L):
        out.append((1 if m.group(1) == "+" else -1, sp.Rational(int(m.group(2)), int(m.group(3))), m.group(4),
                    m.group(5) is not None))
    return out


def leibniz_ok(sums):
    """E2a: the identity with the parameters read (the |gamma'| = 1 part from the first sum, >= 2 from the second)"""
    if len(sums) != 2:
        return False, f"{len(sums)} sums read"
    x, y = sp.symbols("x y")
    g, u = sp.Function("g")(x, y), sp.Function("u")(x, y)
    p1 = sums[0] if "= 1" in sums[0][2] else sums[1]
    p2 = sums[1] if p1 is sums[0] else sums[0]
    ok = True
    for gam in ((1, 0), (0, 1), (2, 1), (1, 2), (3, 0), (1, 1)):
        d = lambda f, a, b: sp.diff(f, x, a, y, b) if a or b else f
        lhs = -sp.Rational(1, 2)*g*d(sp.diff(u, x, 2), *gam)
        rhs = d(-sp.Rational(1, 2)*g*sp.diff(u, x, 2), *gam)
        for i in range(gam[0] + 1):
            for j in range(gam[1] + 1):
                if i + j == 0:
                    continue
                s_, c_, _, binom = p1 if i + j == 1 else p2
                B = sp.binomial(gam[0], i)*sp.binomial(gam[1], j) if binom else 1
                rhs += s_*c_*B*d(g, i, j)*d(sp.diff(u, x, 2), gam[0] - i, gam[1] - j)
        ok = ok and sp.expand(lhs - rhs) == 0
    return ok, f"read {[(s_, str(c_), cond, b) for s_, c_, cond, b in sums]}"


def read_bounds(L):
    rb = re.search(r"\|\|b \. d U\|\| <= C (?:lam\^(-?\d+) )?t\^\(([-\d/]+)\) \|\|d U\|\|", L)
    rc = re.search(r"\|\|c U\|\| <= C lam\^(-?\d+) t\^\(([-\d/]+)\) \|\|U\|\| <= C lam\^(-?\d+) t\^\(([-\d/]+)\) "
                   r"\|\|d U\|\|", L)
    cf = re.search(r"c := dF_1/d u_1 = -\(1/2\) lam\^(-?\d+) \(\.\)\(ell_lam, ell_lam\) \[d_th\^2 W_TT\] \+ E_\(3/2\)", L)
    bf = re.search(r"b := dF_1/d\(d u_1\), in E_\(([\d/]+)\) and of lam-order (\d+)", L)
    ker = re.search(r"exp\(int C\(1 \+ lam\^(-?\d+)\) t\^\(([-\d/]+)\)\)", L)
    fk = re.search(r"\|\|f_gamma\|\| <= C\(1 \+ lam\^(-?\d+)\) t\^\(([-\d/]+)\) sum_\{\|(?:delta|gamma')\| = j \+ 1\} "
                   r"\|\|d d\^(?:delta|\{gamma'\}) u_1\|\| \+ \|\|R_gamma\|\|", L)
    fac = re.search(r"at most e\^\((.+?)\) over the far region t >= lam\^-2", L)
    return rb, rc, cf, bf, ker, fk, fac


def bounds_ok(L, pre):
    rb, rc, cf, bf, ker, fk, fac = read_bounds(L)
    if not all((rb, rc, cf, bf, ker, fk, fac)):
        return {"E2b": (False, "a bound could not be read"), "E2c": (False, ""), "E2d": (False, "")}
    wcls = re.search(r"lam \[W_TT\] = r\^\(-(\d+/\d+)\) G_3", pre)
    qW = frac(wcls.group(1)) if wcls else None
    # the model: c = -(1/2) lam^p K(ell, ell) d_th^2 (r^(-3/2) w(theta)), w = sin; its sup over theta
    th, r, K = sp.symbols("theta r K", positive=True)
    p = int(cf.group(1))
    cmod = -sp.Rational(1, 2)*LAM**p*K*sp.diff(r**(-qW)*sp.sin(th), th, 2)
    sup = sp.Rational(1, 2)*LAM**p*K*r**(-qW)          # |sin| <= 1, attained at theta = pi/2
    ok_sup = sp.simplify(cmod.subs(th, sp.pi/2) - sup) == 0 and sp.simplify(sp.Abs(cmod) - sup*sp.Abs(sp.sin(th))) == 0
    c_lam, c_t = int(rc.group(1)), frac(rc.group(2))
    c_lam2, c_t2 = int(rc.group(3)), frac(rc.group(4))
    b_lam, b_t = int(rb.group(1) or 0), frac(rb.group(2))
    b_cls, b_ord = frac(bf.group(1)), int(bf.group(2))
    okb = (ok_sup and c_lam == p and c_t == -qW and (c_lam2, c_t2) == (c_lam, c_t)
           and b_lam == -b_ord and b_t == -b_cls)
    r_b = f"b: lam^{b_lam} t^({b_t}) against E_({b_cls}), lam-order {b_ord}; c: lam^{c_lam} t^({c_t}) against " \
          f"the model's lam^{p} r^({-qW})"
    k_lam, k_t = int(ker.group(1)), frac(ker.group(2))
    f_lam, f_t = int(fk.group(1)), frac(fk.group(2))
    okc = ({0, k_lam} == {b_lam, c_lam} and k_t == b_t == c_t and (f_lam, f_t) == (k_lam, k_t))
    kern = C*(1 + LAM**k_lam)*T**k_t
    I = sp.integrate(kern, (T, LAM**-2, sp.oo))
    tr = standard_transformations + (implicit_multiplication_application,)
    try:
        fx = parse_expr(fac.group(1).replace("lam", "LAM"), {"C": C, "LAM": LAM}, transformations=tr)
    except Exception:  # noqa: BLE001
        fx = sp.nan
    okd = sp.simplify(fx - I) == 0 and sp.limit(I, LAM, 0, "+").is_finite
    return {"E2b": (okb, r_b), "E2c": (okc, f"kernel C(1 + lam^{k_lam}) t^({k_t}); f's C(1 + lam^{f_lam}) t^({f_t})"),
            "E2d": (okd, f"read e^({fac.group(1)}); computed exp({sp.simplify(I)})")}


def r6_only_ok(L):
    out = {}
    m = re.search(r"int_\{tau_n\}\^tau t'\^\(([-\d/]+)\) dtau' <= (\d+) t\^\(([-\d/]+)\)", L)
    m2 = re.search(r"\|\|d U_n\(tau_n\)\|\| <= C\(lam, j\) t_n\^\(([-\d/]+)\) <= C\(lam, j\) t\^\(([-\d/]+)\)", L)
    if m and m2:
        q, k, e = frac(m.group(1)), int(m.group(2)), frac(m.group(3))
        sv = sp.Symbol("s", positive=True)
        # tau' from tau_n up to tau is t' = 1 + tau0 - tau' from t_n down to t: int_t^(t_n) s^q ds
        I_t = sp.integrate(sv**q, (sv, T, TN))
        exact = sp.simplify(I_t - 2*(T**sp.Rational(-1, 2) - TN**sp.Rational(-1, 2))) == 0
        ok = exact and q == sp.Rational(-3, 2) and k == 2 and e == sp.Rational(-1, 2) and \
            frac(m2.group(1)) == frac(m2.group(2)) == e
        out["E2f"] = (ok, f"int = {I_t} (t_n >= t), read <= {k} t^({e})")
    else:
        out["E2f"] = (False, "not read")
    src = re.search(r"F_1\(X, 0, 0\), in E_(\d+|\(\d+/\d+\)), has L\^2 norm at most C t\^\(([-\d/]+)\)", L)
    eng = re.search(r"the energies of the lower steps, at most C t\^\(([-\d/]+)\)", L)
    rg = re.search(r"\|\|R_gamma\|\| <= C\(lam, j\) t\^\(([-\d/]+)\)\.", L)
    if src and eng and rg:
        r, a1, a2 = sp.symbols("r a1 a2", positive=True)

        def l2pow(q):
            I = sp.integrate(r**(-2*q)*r**3, (r, T + a1, T + a2))
            lead = sp.limit(sp.log(I.subs({a1: 1, a2: 3}))/sp.log(T), T, sp.oo)
            return lead/2
        qs = frac(src.group(1).strip("()"))
        p_src, p_eng = l2pow(qs), l2pow(sp.Integer(2))
        p_prod = max(-sp.Rational(3, 2), -2) + p_eng  # a coefficient in E_(3/2) or a factor in E_2, times the L^2 factor
        ok = (p_src == frac(src.group(2)) and p_eng == frac(eng.group(1)) and p_prod <= -2
              and frac(rg.group(1)) == max(p_src, p_prod))
        out["E2g"] = (ok, f"E_{qs} -> t^({p_src}), E_2 -> t^({p_eng}), products <= t^({p_prod}); read ||R_gamma|| "
                          f"t^({rg.group(1)})")
    else:
        out["E2g"] = (False, "not read")
    bk = re.search(r"floor\(\(N \+ (\d+)\)/(\d+)\) <= max\((\d+), N - (\d+)\) for every N >= 1", L)
    if bk:
        a_, b_, c_, d_ = (int(g) for g in bk.groups())
        out["E2h"] = (all((N + a_)//b_ <= max(c_, N - d_) for N in range(1, 2001)), str(bk.group(0)))
    else:
        out["E2h"] = (False, "not read")
    return out


def math_checks(L, pre, r6=True):
    """the mathematics of an edited Lemma 11.0 (whitespace-normalised) with the text before it (for W_TT's class)"""
    res = {"E2a": leibniz_ok(read_sums(L))}
    res.update(bounds_ok(L, pre))
    if r6:
        res.update(r6_only_ok(L))
    return res


def gronwall_model():
    """E2e: y' = kappa y has y0 exp(int kappa) (exact); the solutions of y' = kappa y - g, g >= 0, i.e. of
    y = y0 + int (kappa y - g), lie below it (20 random g, mpmath quadrature of the variation-of-constants formula)"""
    import mpmath as mp
    s_ = sp.Symbol("s", positive=True)
    y = sp.Function("y")
    lam = sp.Rational(1, 10)
    kap = 3*(1 + 1/lam)*s_**sp.Rational(-3, 2)
    s0 = lam**-2
    sol = sp.dsolve(sp.Eq(y(s_).diff(s_), kap*y(s_)), y(s_), ics={y(s0): 1})
    Kf = sp.integrate(kap, (s_, s0, s_))
    exact = sp.simplify(sol.rhs - sp.exp(Kf)) == 0
    Kn = sp.lambdify(s_, Kf, "mpmath")
    rng = random.Random(9)
    ok = True
    for _ in range(20):
        c1, c2 = rng.uniform(0, 1), rng.uniform(0.01, 0.2)
        g = lambda x: c1*mp.exp(-c2*(x - 100))
        x_end = mp.mpf(100 + rng.uniform(1, 400))
        ysub = mp.exp(Kn(x_end)) - mp.quad(lambda x: mp.exp(Kn(x_end) - Kn(x))*g(x), [100, x_end])
        ok = ok and ysub <= mp.exp(Kn(x_end))
    return exact and ok


# ================================================================ E1-E3

def lemma_and_pre(text):
    L = R5E.lemma110(text)
    a = text.index("### 11.1 The expansion of g_lam at past null infinity")
    return L, text[a:text.index("**Lemma 11.0", a)]


def predicates6(L):
    p = R5E.predicates(L)
    Ln = norm(L)
    sums = read_sums(Ln)
    # (b) read structurally (r5edits5's fixed windows are too short for the longer index sets of (g))
    p["b"] = len(sums) == 2 and all(sg == 1 and c_ == sp.Rational(1, 2) and bn for sg, c_, _, bn in sums)
    p["g"] = len(sums) == 2 and all(c.startswith("gamma' <= gamma, ") for _, _, c, _ in sums)
    p["h"] = "sum_{|delta| = j + 1}" in Ln and "sum_{|gamma'| = j + 1}" not in Ln
    p["i"] = "where f_gamma^n, b^n, c^n and R_gamma^n are f_gamma, b, c and R_gamma with g_n and u_1^n" in Ln
    p["j"] = ("||R_gamma^n|| <= C(lam, j) t^(-3/2) uniformly in n: d_X^gamma F_1(X, 0, 0) does not depend on n" in Ln
              and "induction hypothesis for u_1^n, which is uniform in n" in Ln)
    return p


def apply(P, blocks):
    o1, n1, o2, n2 = blocks
    return P.replace(o1, n1, 1).replace(o2, n2, 1)


def e1(blocks, P):
    print("E1  R6-D's replacement text for Lemma 11.0, applied to a copy of the live N1STAR-PROOF.md")
    o1, n1, o2, n2 = blocks
    once = P.count(o1) == 1 and P.count(o2) == 1
    check("E1a each old block occurs exactly once in the live file", once, f"{P.count(o1)}, {P.count(o2)}")
    if not once:
        return None
    Q = apply(P, blocks)
    long_ = [(i + 1, len(l)) for i, l in enumerate(Q.split("\n")) if len(l) > 121]
    check("E1b the edited file keeps every line within 121 characters", not long_, str(long_[:5]))
    a, b = P.index("**Lemma 11.0"), P.index("**Lemma 11.1")
    a2, b2 = Q.index("**Lemma 11.0"), Q.index("**Lemma 11.1")
    check("E1c the edit changes nothing outside Lemma 11.0", P[:a] == Q[:a2] and P[b:] == Q[b2:],
          f"{len(Q.split(chr(10))) - len(P.split(chr(10)))} lines added")
    new_p, old_p = predicates6(lemma_and_pre(Q)[0]), predicates6(lemma_and_pre(P)[0])
    check("E1d the edited Lemma 11.0 satisfies (a)-(f) of r5edits5 and (g) gamma' <= gamma at both sums, (h) the "
          "family index delta, (i) f_gamma^n, b^n, c^n, R_gamma^n defined, (j) ||R_gamma^n|| uniform in n with its "
          "reason", all(new_p.values()), str(new_p))
    check("E1e control (the same predicates on the live, unedited Lemma 11.0): every one fails",
          not any(old_p.values()), str(old_p))
    return Q


def e2(Q):
    print("E2  the mathematics the edited Lemma 11.0 states, read from its text")
    L, pre = lemma_and_pre(Q)
    res = math_checks(norm(L), norm(pre))
    names = {"E2a": "Leibniz's rule with the sign, 1/2 and C(gamma, gamma') read from both sums (orders 1..3, exact)",
             "E2b": "the bounds read for b . d U and c U have the lam- and t-powers of b and c as the text defines "
                    "them (c's on the model, exact)",
             "E2c": "the Gronwall kernel and ||f_gamma||'s bound read are the sum of the two bounds read",
             "E2d": "the factor read equals exp of the kernel's integral over t >= lam^-2 (computed), lam-free",
             "E2f": "Edit 2's closing bound read: int t'^(-3/2) = 2(t^(-1/2) - t_n^(-1/2)) <= 2 t^(-1/2) (exact)",
             "E2g": "the L^2 powers on Sigma_tau cap P+ computed from the classes read match the bounds read",
             "E2h": "the bookkeeping inequality read holds for N = 1..2000"}
    for k in ("E2a", "E2b", "E2c", "E2d"):
        check(f"{k} {names[k]}", *res[k])
    check("E2e Gronwall's lemma in integral form: the solution of y' = kappa y is y0 exp(int kappa) (exact) and 20 "
          "sampled subsolutions stay below it", gronwall_model())
    for k in ("E2f", "E2g", "E2h"):
        check(f"{k} {names[k]}", *res[k])
    return res


MUTANTS = [
    ("E-m5: c U's bound lam^-1 -> lam^-3", "||c U|| <= C\nlam^-1 t^(-3/2) ||U||", "||c U|| <= C\nlam^-3 t^(-3/2) ||U||"),
    ("E-m6: the factor -> e^(2C/lam)", "at most e^(2C(1 + lam)) over the far region",
     "at most e^(2C/lam) over the far region"),
    ("the 1/2 of the |gamma'| = 1 sum dropped", "        + (1/2) sum_{gamma' <= gamma, |gamma'| = 1}",
     "        + sum_{gamma' <= gamma, |gamma'| = 1}"),
    ("C(gamma, gamma') dropped at the |gamma'| >= 2 sum", "|gamma'| >= 2} C(gamma, gamma') (d^{gamma'}",
     "|gamma'| >= 2} (d^{gamma'}"),
    ("R_gamma's source E_3 -> E_(5/2)", "d_X^gamma F_1(X, 0, 0), in E_3, has", "d_X^gamma F_1(X, 0, 0), in E_(5/2), has"),
    ("max(4, N - 3) -> max(4, N - 4) (in the unchanged text, as read)", "<= max(4, N - 3) for every N >= 1",
     "<= max(4, N - 4) for every N >= 1"),
]


def e3(blocks, P):
    print("E3  controls: the text under test mutated, each mutation must fail E1 or E2")
    results = []
    for label, old, new in MUTANTS:
        bl = list(blocks)
        hit = [i for i in range(4) if old in bl[i]]
        if hit:
            bl[hit[0]] = bl[hit[0]].replace(old, new, 1)
            PP = P
        else:
            assert P.count(old) == 1, label
            PP = P.replace(old, new, 1)
        Q = apply(PP, bl)
        L, pre = lemma_and_pre(Q)
        res = math_checks(norm(L), norm(pre))
        preds = predicates6(L)
        failed = [k for k, v in res.items() if not v[0]] + [k for k, v in preds.items() if not v]
        results.append((label, failed))
    for label, failed in results:
        check(f"E3 {label}: caught", bool(failed), f"failing: {failed}")


def main():
    S = open(os.path.join(ROOT, "SETTLE-GLAM5.md")).read()
    blocks = section_blocks(S, "### R6-D ", "### R6-E ")
    P = open(os.path.join(ROOT, "N1STAR-PROOF.md")).read()
    Q = e1(blocks, P)
    if Q is not None:
        e2(Q)
        e3(blocks, P)
    print("FAILED:", FAIL if FAIL else "none")
    return 1 if FAIL else 0


if __name__ == "__main__":
    sys.exit(main())
