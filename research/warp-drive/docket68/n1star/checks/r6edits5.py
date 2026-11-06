"""r6edits5.py -- SETTLE-GLAM5 round 6: the final replacement text for N1STAR-PROOF.md's Lemma 11.0 (R6-D), applied to
a copy of the live file, and the mathematics it states checked, not only its phrases (the round-5 reader's surviving
mutants E-m5 and E-m6 passed r5edits5 E1, which read phrases only).

  E1 (text) R6-D's four blocks, read from SETTLE-GLAM5.md as printed there, applied to a copy of the live
     N1STAR-PROOF.md (the file is not edited): each old block occurs exactly once, every line of the edited file is
     within 121 characters, nothing outside Lemma 11.0 changes, and the edited Lemma 11.0 satisfies r5edits5's
     predicates (a)-(f) ((a) and (b) read for R6-D's wording: R_gamma^n defined in the sentence that uses it, the
     sums read structurally) and four more: (g) "gamma' <= gamma" at both Leibniz sums; (h) the family is indexed by
     delta (gamma' is not reused); (i) f_gamma^n, b^n, c^n and R_gamma^n are defined; (j) ||R_gamma^n|| <= C(lam, j)
     t^(-3/2) uniformly in n is stated, with its reason. Round 7 (the round-6 reader's minor 3): the induction's
     structure (which terms are unknown, of which order R_gamma is, that Gronwall's lemma acts on the family, that
     Lemma 9.3(b)'s hypothesis holds, that b^n and c^n have b's and c's constants) is a read proof, not computed;
     five more predicates check that the text states each step: (k) "contains derivatives of u_1 of order <= j + 1
     only", (l) "by Lemma 9.3(b) (U vanishes on {v = v_start})", (m) "summed over the family, Gronwall's lemma then
     costs", (n) "b . d U is of the order this step estimates and is not known", (o) "obey the bounds on b and c
     above with the same constants"; and round 8 two more: (p) "and c U is one order lower.", (q) "(Lemma 11.1
     applies to u_1^n verbatim"; and, read structurally on Edit 2 (the N1STAR reader's M14, M19, M12, which (m) and
     (n), reading Edit 1, let pass): (r) the forcing of Edit 2's energy inequality is f_gamma^n, and the definition of
     f_gamma read from Edit 1 contains b . d U (R_gamma's subtracts it); (s) both sides of Edit 2's Gronwall bound
     are sums over the family; (t) the step's |gamma|, the family's |delta|, ||f_gamma||'s sum and Edit 2's two sums
     read the same index. Control: on the live, unedited Lemma 11.0 every predicate fails.
  E2 (exact, sympy) what the edited text states, every quantity read from the text by a pattern:
     E2a Leibniz's rule with the sign, the coefficient and the binomial factor read from both sums: for generic g, u of
         (x, y) and every gamma of order 1..3, -(1/2) g d_x^2 d^gamma u = d^gamma(-(1/2) g d_x^2 u) + s c sum_{0 <
         gamma' <= gamma} B (d^gamma' g) d^(gamma - gamma') d_x^2 u holds exactly (s, c, B as read).
         Round 8: B is the text's own definition of C(gamma, gamma'), read and evaluated, not sympy's binomial.
     E2b the bounds read for ||b . d U|| and ||c U|| have the lam- and t-powers of the coefficients the text defines:
         b of lam-order 0 in E_(3/2), and c's leading term -(1/2) lam^p (.)(ell, ell) [d_th^2 W_TT] with p read and
         W_TT ~ r^(-3/2) (read from "lam [W_TT] = r^(-3/2) G_3" before the lemma): on the model
         c = -(1/2) lam^p K(ell, ell) d_th^2 (r^(-3/2) w(theta)), w = sin, its supremum over the phase is
         (1/2) lam^p |K(ell, ell)| r^(-3/2) (exact), and on P+ r ~ t; both sides of the Lemma 9.3(b) step carry it.
     E2c the Gronwall kernel read ("exp(int C(1 + lam^q) t^(e))") is the sum of the two bounds read, and so is
         ||f_gamma||'s.
     E2d the factor read ("at most e^(...) over the far region t >= lam^-2") equals exp of
         int_(lam^-2)^oo (the kernel read) dt, computed (2C(1 + lam)), and is bounded as lam -> 0; round 8 (the
         N1STAR reader's M10): Edit 2's factor ("C e^(...)"), read, is the same computed one.
     E2e Gronwall's lemma in integral form on the model: y(tau) = y0 + int kappa y has y = y0 exp(int kappa) (exact),
         and the solutions of y' = kappa y - g with g >= 0 lie below it (20 sampled g).
     E2f Edit 2's closing bound, read: int_(tau_n)^tau t'^(-3/2) dtau' = 2 (t^(-1/2) - t_n^(-1/2)) <= 2 t^(-1/2) with
         t = 1 + tau0 - tau, tau_n < tau (exact), and t_n^(-1/2) <= t^(-1/2).
     E2g the L^2 norms on Sigma_tau cap P+ = {t + a1 <= r <= t + a2} x S^3 (measure r^3 dr domega): a field in E_q has
         norm ~ t^(3/2 - q) (exact leading power): E_3 gives the t^(-3/2) read for R_gamma's source, a derivative in
         E_2 the t^(-1/2) read for the lower steps' energies, and a product (E_(3/2) or E_2) x t^(-1/2) at most
         t^(-2), which must equal the text's own "each product at most C t^(-2)" (read, round 7): the bound read for
         ||R_gamma|| is the largest of them.
         Round 8: the slice's volume read ("whose volume is at most C t^3") against the computed power.
     E2h the bookkeeping inequality read ("floor((N + 2)/2) <= max(4, N - 3)") holds for N = 1..2000.
     E2i round 8 (the N1STAR reader's n3), not read from the text: the rotation case on E2g's model, exact: a rotation
         keeps a field's class and d raises it (r^-q x_1/r along a ray), |Omega f| <= r |d f| (Lagrange's identity);
         for pure-rotation gamma the |gamma'| = |gamma| product is t^(-3/2) (L^2 factor t^(1/2)), not <= t^(-2) as for
         Cartesian gamma, yet <= the source's t^(-3/2), so ||R_gamma|| <= C t^(-3/2) stands; via Lemma 9.3(b) it is a
         family term with kernel t^-2, integral lam^2; c U as a source integrates for Cartesian gamma only.
  E3 controls: the text under test mutated in memory, each mutation must make E1 or E2 fail: c U's bound lam^-1 ->
     lam^-3 (the reader's E-m5), the factor -> e^(2C/lam) (E-m6), the coefficient 1/2 of the |gamma'| = 1 sum dropped,
     C(gamma, gamma') dropped at the |gamma'| >= 2 sum, R_gamma's source E_3 -> E_(5/2), and max(4, N - 3) ->
     max(4, N - 4); round 8 adds the N1STAR reader's four survivors: Edit 2's factor -> e^(2C/lam) (M10), Edit 2's
     f = f_gamma^n -> R_gamma^n (M14), Edit 2's sums removed (M19), the family's |delta| = j + 1 -> j (M12).
  E4 (text) the final paper blocks, R8-E since round 8 (R7-E's in round 7, R6-E's in round 6), against
     RESPONSE-HL-5D.md (not edited); round 8 adds the status words (deduced, conditional on, proved, and no stronger
     word), BEYOND5 Lemma 6.4 (iv) in block 1 and block 3's "deduced, conditionally", with R7-E's blocks as the control.
     As before:
     each old text once, every line within 121 characters after the edit, and the new texts state what the round-5
     and round-6 readers asked (section 11.1's status, the rounds read and unread, Parts III, IV, VII and VIII,
     BEYOND5 Lemma 6.4 (iv) as deduced, eps named, Proposition 3.1 deduced, the r^(-4) term built for one example,
     the window computed from measured and hand-counted exponents, R6-D seated). Control (round 8): R7-E's blocks
     fail exactly the three predicates round 8 adds on BEYOND5 in block 1, the rounds and the window's list.
  D630: R6-D is seated in N1STAR-PROOF.md (each new block occurs there once, no old block); the program then undoes it
     in memory, with its two "[amended D630: WS-B round 6, R6-D ...]" marks, and runs E1-E3 on that copy, and E1s
     checks that re-applying the blocks gives the live file but for the two marks.
Labels: E1 and E4 text checks; E2 exact (sympy), E2e partly sampled.

    python3 checks/r6edits5.py     (5 to 35 seconds on this loaded machine)
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


def read_binomial(L):
    """[R8] the text's own definition of C(gamma, gamma'), as a function of two multi-indices (None if not read)"""
    m = re.search(r"C\(gamma, gamma'\) := (.+?), where", L)
    if not m:
        return None, "C(gamma, gamma') not defined"
    ex = m.group(1).replace("(gamma - gamma')!", "F(D)").replace("gamma'!", "F(G1)").replace("gamma!", "F(G)")
    ex = ex.replace(") F(", ")*F(")
    if re.search(r"[^FDG1()*/ ]", ex):
        return None, "unread: " + m.group(1)

    def C(gam, gp):
        fac = lambda t_: sp.Mul(*[sp.factorial(k_) for k_ in t_])
        D_ = tuple(a_ - b_ for a_, b_ in zip(gam, gp))
        return eval(ex, {"F": fac, "G": gam, "G1": gp, "D": D_})
    return C, m.group(1)


def leibniz_ok(sums, binom_def=(None, "")):
    """E2a: the identity with the parameters read (the |gamma'| = 1 part from the first sum, >= 2 from the second),
    and [R8] the binomial factor from the text's own definition of C(gamma, gamma')"""
    Cdef, Ctext = binom_def
    if len(sums) != 2:
        return False, f"{len(sums)} sums read"
    if Cdef is None:
        return False, Ctext
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
                B = Cdef(gam, (i, j)) if binom else 1
                rhs += s_*c_*B*d(g, i, j)*d(sp.diff(u, x, 2), gam[0] - i, gam[1] - j)
        ok = ok and sp.expand(lhs - rhs) == 0
    return ok, f"read {[(s_, str(c_), cond, b) for s_, c_, cond, b in sums]}; C(gamma, gamma') := {Ctext}"


def read_bounds(L):
    rb = re.search(r"\|\|b \. d U\|\| <= C (?:lam\^(-?\d+) )?t\^\(([-\d/]+)\) \|\|d U\|\|", L)
    rc = re.search(r"\|\|c U\|\| <= C lam\^(-?\d+) t\^\(([-\d/]+)\) \|\|U\|\| <= C lam\^(-?\d+) t\^\(([-\d/]+)\) "
                   r"\|\|d U\|\|", L)
    cf = re.search(r"c := dF_1/d u_1 = -\(1/2\) lam\^(-?\d+) \(\.\)\(ell_lam, ell_lam\) \[d_th\^2 W_TT\] "
                   r"\+ E_\(3/2\)", L)
    bf = re.search(r"b := dF_1/d\(d u_1\), in E_\(([\d/]+)\) and of lam-order (\d+)", L)
    ker = re.search(r"exp\(int C\(1 \+ lam\^(-?\d+)\) t\^\(([-\d/]+)\)\)", L)
    fk = re.search(r"\|\|f_gamma\|\| <= C\(1 \+ lam\^(-?\d+)\) t\^\(([-\d/]+)\) sum_\{\|(?:delta|gamma')\| = j \+ 1\} "
                   r"\|\|d d\^(?:delta|\{gamma'\}) u_1\|\| \+ \|\|R_gamma\|\|", L)
    fac = re.search(r"at most e\^\((.+?)\) over the far region t >= lam\^-2", L)
    return rb, rc, cf, bf, ker, fk, fac


def read_edit2(L):
    """[R8, the N1STAR reader's M10, M14, M19] Edit 2's energy step, read: the forcing named, the index sets of its two
    family sums (None where a sum is absent) and the Gronwall factor's exponent"""
    m = re.search(r"Lemma 9\.5's energy inequality \(9\.3\) for U_n with f = (\S+), and Gronwall's lemma, give "
                  r"(?:sum_\{\|gamma\| = ([^}]*)\} )?\|\|d U_n\(tau\)\|\| <= C e\^\((.+?)\) "
                  r"(?:sum_\{\|gamma\| = ([^}]*)\} )?\(\|\|d U_n\(tau_n\)\|\| \+ int_\{tau_n\}\^tau "
                  r"\|\|R_gamma\^n\|\| dtau'\)", L)
    if not m:
        return None
    return {"f": m.group(1), "sum1": m.group(2), "exp": m.group(3), "sum2": m.group(4)}


def family_indices(L):
    """[R8, the N1STAR reader's M12] every place the text fixes the order of the step or of the family: the step's
    |gamma|, the family's |delta|, the |delta| of ||f_gamma||'s sum, Edit 2's two sums"""
    st = re.search(r"Induction on the order: for \|gamma\| = ([^,]*), by Leibniz's rule U := d\^gamma u_1", L)
    fam = re.search(r"family \{d\^delta u_1 : \|delta\| = ([^}]*)\}", L)
    fs = re.search(r"\|\|f_gamma\|\| <= C\(1 \+ lam\^-?\d+\) t\^\([-\d/]+\) sum_\{\|delta\| = ([^}]*)\}", L)
    e2 = read_edit2(L)
    return [x.group(1) if x else None for x in (st, fam, fs)] + ([e2["sum1"], e2["sum2"]] if e2 else [None, None])


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
    e2 = read_edit2(L)                    # [R8] Edit 2 states the factor again: it must be the same, computed one
    try:
        fx2 = parse_expr(e2["exp"].replace("lam", "LAM"), {"C": C, "LAM": LAM}, transformations=tr) if e2 else sp.nan
    except Exception:  # noqa: BLE001
        fx2 = sp.nan
    okd = okd and sp.simplify(fx2 - I) == 0
    return {"E2b": (okb, r_b), "E2c": (okc, f"kernel C(1 + lam^{k_lam}) t^({k_t}); f's C(1 + lam^{f_lam}) t^({f_t})"),
            "E2d": (okd, f"read e^({fac.group(1)}), Edit 2 e^({e2['exp'] if e2 else None}); computed "
                         f"exp({sp.simplify(I)})")}


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
    prd = re.search(r"each product at most C t\^\(([-\d/]+)\)", L)      # [R7] the text's own product bound
    eng = re.search(r"the energies of the lower steps, at most C t\^\(([-\d/]+)\)", L)
    rg = re.search(r"\|\|R_gamma\|\| <= C\(lam, j\) t\^\(([-\d/]+)\)\.", L)
    vol = re.search(r"whose volume is at most C t\^(\d+)", L)                # [R8] the slice's volume, read
    if src and eng and rg and prd and vol:
        r, a1, a2 = sp.symbols("r a1 a2", positive=True)

        def l2pow(q):
            I = sp.integrate(r**(-2*q)*r**3, (r, T + a1, T + a2))
            lead = sp.limit(sp.log(I.subs({a1: 1, a2: 3}))/sp.log(T), T, sp.oo)
            return lead/2
        qs = frac(src.group(1).strip("()"))
        p_src, p_eng = l2pow(qs), l2pow(sp.Integer(2))
        p_prod = max(-sp.Rational(3, 2), -2) + p_eng  # a coefficient in E_(3/2) or a factor in E_2, times the L^2 factor
        Iv = sp.integrate(r**3, (r, T + a1, T + a2)).subs({a1: 1, a2: 3})
        p_vol = sp.limit(sp.log(Iv)/sp.log(T), T, sp.oo)                    # the volume of A_P(tau) ~ t^p_vol
        ok = (p_src == frac(src.group(2)) and p_eng == frac(eng.group(1)) and frac(prd.group(1)) == p_prod
              and frac(rg.group(1)) == max(p_src, p_prod) and int(vol.group(1)) == p_vol)
        out["E2g"] = (ok, f"E_{qs} -> t^({p_src}), E_2 -> t^({p_eng}), products <= t^({p_prod}) (read: "
                          f"t^({prd.group(1)})); read ||R_gamma|| t^({rg.group(1)}); volume t^{p_vol} (read: "
                          f"t^{vol.group(1)})")
    else:
        out["E2g"] = (False, "not read")
    bk = re.search(r"floor\(\(N \+ (\d+)\)/(\d+)\) <= max\((\d+), N - (\d+)\) for every N >= 1", L)
    if bk:
        a_, b_, c_, d_ = (int(g) for g in bk.groups())
        out["E2h"] = (all((N + a_)//b_ <= max(c_, N - d_) for N in range(1, 2001)), str(bk.group(0)))
    else:
        out["E2h"] = (False, "not read")
    return out


def rotation_case():
    """E2i [R8, the N1STAR reader's n3] the rotation case, exact (sympy), on the model of E2g: a rotation keeps a field's
    class, a coordinate derivative raises it by one (r^-q x_1/r in R^4 along a ray), and |Omega f| <= r |d f|
    (Lagrange's identity); so for pure-rotation gamma the |gamma'| = |gamma| Leibniz term (d g^{ab}/d g . Omega^gamma
    u_1) d_a d_b u_1 has its L^2 factor ||Omega^gamma u_1|| only from the lower steps' energies with the loss of r,
    t^(1/2), and the product is t^(-3/2): not at most t^(-2), as for Cartesian gamma (t^(-5/2)), but not above the
    source's t^(-3/2), so ||R_gamma|| <= C t^(-3/2) stands; or, by Lemma 9.3(b), the term enters the family with kernel
    t^-2, whose integral over t >= lam^-2 is lam^2 (a lam-free factor). The aside "c U taken as a source, through the
    energies of the lower steps" needs Cartesian gamma: there lam^-1 t^(-2) is integrable, with a rotation lam^-1 t^-1
    is not."""
    x1, x2, x3, x4, rr, q = sp.symbols("x1 x2 x3 x4 r q", positive=True)
    R = sp.sqrt(x1**2 + x2**2 + x3**2 + x4**2)
    f = R**(-q)*x1/R
    om = sp.simplify(x1*sp.diff(f, x2) - x2*sp.diff(f, x1))
    grad2 = sum(sp.diff(f, xi)**2 for xi in (x1, x2, x3, x4))
    ray = {x1: rr/2, x2: rr*sp.sqrt(3)/2, x3: 0, x4: 0}
    qv = sp.Rational(5, 2)
    p_om = sp.limit(sp.log(sp.Abs(om.subs(ray).subs(q, qv)))/sp.log(rr), rr, sp.oo)
    p_d = sp.limit(sp.log(sp.sqrt(grad2.subs(ray).subs(q, qv)))/sp.log(rr), rr, sp.oo)
    xa, xb, pa, pb = sp.symbols("xa xb pa pb", real=True)
    lagr = sp.expand((xa**2 + xb**2)*(pa**2 + pb**2) - (xa*pb - xb*pa)**2 - (xa*pa + xb*pb)**2) == 0
    r_, a1, a2 = sp.symbols("r_ a1 a2", positive=True)

    def l2pow(qq):
        I = sp.integrate(r_**(-2*qq)*r_**3, (r_, T + a1, T + a2))
        return sp.limit(sp.log(I.subs({a1: 1, a2: 3}))/sp.log(T), T, sp.oo)/2
    p_eng = l2pow(sp.Integer(2))                 # the lower steps' energies, a derivative in E_2
    p_rot = l2pow(sp.Integer(1))                 # Omega^gamma u_1: the class of Omega^gamma'' u_1, one below its d
    p_src = l2pow(sp.Integer(3))                 # d_X^gamma F_1(X, 0, 0) in E_3
    sup2 = -2                                    # the second factor, d_a d_b u_1, in E_2, in sup norm
    prod_rot, prod_cart = p_rot + sup2, p_eng + sup2
    Ik = sp.integrate(C*T**-2, (T, LAM**-2, sp.oo))
    cu_cart = sp.integrate(T**(-sp.Rational(3, 2) + p_eng), (T, LAM**-2, sp.oo))
    cu_rot = sp.integrate(T**(-sp.Rational(3, 2) + p_rot), (T, LAM**-2, sp.oo))
    ok = (p_om == -qv and p_d == -qv - 1 and lagr and prod_rot == -sp.Rational(3, 2) and prod_rot > -2
          and prod_rot <= p_src and prod_cart <= -2 and sp.simplify(Ik - C*LAM**2) == 0
          and cu_cart.is_finite and cu_rot == sp.oo)
    return ok, (f"Omega: E_{qv} -> r^({p_om}), d: -> r^({p_d}); Lagrange {lagr}; product t^({prod_rot}) (rotation), "
                f"t^({prod_cart}) (Cartesian), source t^({p_src}); kernel t^-2 -> {Ik}; c U as a source: "
                f"{cu_cart} (Cartesian), {cu_rot} (rotation)")


def math_checks(L, pre, r6=True):
    """the mathematics of an edited Lemma 11.0 (whitespace-normalised) with the text before it (for W_TT's class)"""
    res = {"E2a": leibniz_ok(read_sums(L), read_binomial(L))}
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
    # (a) as r5edits5's, with R6-D's wording of the definition: R_gamma := precedes the first R_gamma^n, and R_gamma^n
    # is defined in the sentence that uses it ("where f_gamma^n, b^n, c^n and R_gamma^n are ... with g_n and u_1^n")
    first_Rn = Ln.find("R_gamma^n")
    p["a"] = (first_Rn >= 0 and "R_gamma :=" in Ln and Ln.index("R_gamma :=") < first_Rn
              and ("R_gamma^n being R_gamma with" in Ln
                   or "c^n and R_gamma^n are f_gamma, b, c and R_gamma with g_n and u_1^n in place of" in Ln))
    # (b) read structurally (r5edits5's fixed windows are too short for the longer index sets of (g))
    p["b"] = len(sums) == 2 and all(sg == 1 and c_ == sp.Rational(1, 2) and bn for sg, c_, _, bn in sums)
    p["g"] = len(sums) == 2 and all(c.startswith("gamma' <= gamma, ") for _, _, c, _ in sums)
    p["h"] = "sum_{|delta| = j + 1}" in Ln and "sum_{|gamma'| = j + 1}" not in Ln
    p["i"] = "where f_gamma^n, b^n, c^n and R_gamma^n are f_gamma, b, c and R_gamma with g_n and u_1^n" in Ln
    p["j"] = ("||R_gamma^n|| <= C(lam, j) t^(-3/2) uniformly in n: d_X^gamma F_1(X, 0, 0) does not depend on n" in Ln
              and "induction hypothesis for u_1^n, which is uniform in n" in Ln)
    # [R7 (minor 3)] the induction's structure is a read proof; these predicates check that the text states its steps
    p["k"] = "contains derivatives of u_1 of order <= j + 1 only" in Ln          # R_gamma is of lower order
    p["l"] = "by Lemma 9.3(b) (U vanishes on {v = v_start})" in Ln               # Lemma 9.3(b)'s hypothesis
    p["m"] = "summed over the family, Gronwall's lemma then costs" in Ln         # Gronwall on the family
    p["n"] = "b . d U is of the order this step estimates and is not known" in Ln
    p["o"] = "obey the bounds on b and c above with the same constants" in Ln   # b^n, c^n uniform in n
    p["p"] = "and c U is one order lower." in Ln                                 # [R8] c U is not of the top order
    p["q"] = "(Lemma 11.1 applies to u_1^n verbatim" in Ln                       # [R8] the lemma that applies to u_1^n
    # [R8, the N1STAR reader's M14, M19, M12] Edit 2: the forcing is the one that contains the unknown b . d U (its
    # definition in Edit 1, read), Gronwall acts on sums over the family on both sides, one family index throughout
    e2 = read_edit2(Ln)
    name = e2["f"][:-2] if e2 and e2["f"].endswith("^n") else "(no forcing read)"
    dfn = re.search(re.escape(name) + r" := (.{0,40})", Ln)
    p["r"] = bool(e2 and dfn and e2["f"].endswith("^n")
                  and (dfn.group(1).startswith("b . d U +") or "+ b . d U" in dfn.group(1)))
    idx = family_indices(Ln)
    p["s"] = bool(e2 and e2["sum1"] is not None and e2["sum2"] is not None)
    p["t"] = all(i is not None for i in idx) and len(set(idx)) == 1
    return p


D630_MARK = re.compile(r" \[amended D630: WS-B round 6, R6-D[^\]]*\]\n")


def unseat(P, blocks):
    """D630: the live file with R6-D undone and its two [amended D630: WS-B round 6, R6-D ...] marks removed (each mark
    closes a block's last line, the rest of which follows on the next line), which is the file R6-D was written for"""
    o1, n1, o2, n2 = blocks
    return D630_MARK.sub(" ", P.replace(n1, o1, 1).replace(n2, o2, 1))


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
          "reason, and [R7] (k) R_gamma of order <= j + 1 only, (l) Lemma 9.3(b)'s hypothesis, (m) Gronwall summed "
          "over the family, (n) b . d U not known, (o) b^n, c^n with the same constants, [R8] (p) c U one order "
          "lower, (q) Lemma 11.1 applies to u_1^n, and on Edit 2 (r) the forcing is f_gamma^n, whose definition "
          "contains b . d U, (s) Gronwall on sums over the family, (t) one family index throughout (text: the "
          "induction's structure is a read proof)",
          all(new_p.values()), str(new_p))
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
    res["E2i"] = rotation_case()
    names["E2i"] = ("[R8, n3] the rotation case: for pure-rotation gamma the |gamma'| = |gamma| product is "
                    "t^(-3/2), not <= t^(-2), and ||R_gamma|| <= C t^(-3/2) stands (or the family, kernel t^-2); "
                    "c U as a source needs Cartesian gamma (exact)")
    for k in ("E2a", "E2b", "E2c", "E2d"):
        check(f"{k} {names[k]}", *res[k])
    check("E2e Gronwall's lemma in integral form: the solution of y' = kappa y is y0 exp(int kappa) (exact) and 20 "
          "sampled subsolutions stay below it", gronwall_model())
    for k in ("E2f", "E2g", "E2h", "E2i"):
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
    ("R_gamma's source E_3 -> E_(5/2)", "d_X^gamma F_1(X, 0, 0), in E_3, has",
     "d_X^gamma F_1(X, 0, 0), in E_(5/2), has"),
    ("max(4, N - 3) -> max(4, N - 4) (in the unchanged text, as read)", "<= max(4, N - 3) for every N >= 1",
     "<= max(4, N - 4) for every N >= 1"),
    # [R8] the N1STAR reader's four survivors, on Edit 2 and the family index
    ("M10: Edit 2's factor e^(2C(1 + lam)) -> e^(2C/lam)", "<= C e^(2C(1 + lam)) sum_{|gamma|",
     "<= C e^(2C/lam) sum_{|gamma|"),
    ("M14: Edit 2's f = f_gamma^n -> R_gamma^n (b . d U taken as known)", "with f = f_gamma^n, and Gronwall's",
     "with f = R_gamma^n, and Gronwall's"),
    ("M19: Edit 2's sums removed (Gronwall per gamma)",
     "give sum_{|gamma| = j + 1} ||d U_n(tau)|| <= C e^(2C(1 + lam)) sum_{|gamma|\n= j + 1} (||d U_n(tau_n)||",
     "give ||d U_n(tau)|| <= C e^(2C(1 + lam))\n(||d U_n(tau_n)||"),
    ("M12: the family index |delta| = j + 1 -> j", "family {d^delta u_1 : |delta| = j + 1}",
     "family {d^delta u_1 : |delta| = j}"),
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
        elif P.count(old) == 1:
            PP = P.replace(old, new, 1)
        else:       # [R8] the text under test is itself mutated: report, do not stop, so E1 and E2 are seen
            results.append((label, None))
            continue
        Q = apply(PP, bl)
        L, pre = lemma_and_pre(Q)
        res = math_checks(norm(L), norm(pre))
        preds = predicates6(L)
        failed = [k for k, v in res.items() if not v[0]] + [k for k, v in preds.items() if not v]
        results.append((label, failed))
    for label, failed in results:
        if failed is None:
            check(f"E3 {label}: caught", False, "the text this control mutates is not in the text under test")
            continue
        check(f"E3 {label}: caught", bool(failed), f"failing: {failed}")


PAPER = os.path.join(os.path.dirname(os.path.dirname(ROOT)), "paper", "RESPONSE-HL-5D.md")


def paper_predicates(b1, b2):
    b1n, b2n = norm(b1), norm(b2)
    return {"b1: section 11.1's repair not yet applied": "repair written and not yet applied" in b1n,
            "b1: the last rounds not yet read": "not yet read by a verifier" in b1n,
            "b1, b2: 'supplement section 11.1'": "supplement section 11.1" in b1n and "supplement section 11.1" in b2n,
            "b2: condition (b), rounds 5-6 unread": "rounds 5–6 of SETTLE-GLAM5.md, not yet read by a verifier" in b2n,
            "b2: R6-D written, not applied": "(R6-D) and not yet applied" in b2n,
            "b2: eps named": "its threshold ε, and with it λ1 and δ" in b2n,
            "b2: Proposition 3.1 deduced":
                "(deduced, SETTLE-GLAM5.md Proposition 3.1; computed for a bump envelope" in b2n,
            "b2: the window computed, not measured": "the weight window, computed from those measured exponents" in b2n
            and "weight window measured" not in b2n and "and weight window on explicit fields" not in b2n}


def paper_predicates7(b1, b2):
    """[R7] what round 7's blocks state (kept as the control's yardstick)"""
    b1n, b2n = norm(b1), norm(b2)
    return {"b1 BEYOND5": "BEYOND5 Lemma 6.4 (iv)" in b1n, "b2 rounds": "rounds 1–7" in b2n}


def paper_predicates8(b1, b2, b3):
    """[R8] what the final blocks must state, status words included (the round-7 reader's m1, nits 6, 10)"""
    b1n, b2n, b3n = norm(b1), norm(b2), norm(b3)
    no_strong = all(w not in t for t in (b1n, b2n, b3n) for w in ("independent of", "unconditionally", "It is proved",
                                                                  "is proved in section 9"))
    return {"b1: conditional on section 11.1, its repair seated, awaiting a confirming read":
                "half-integer orders, conditional on supplement section 11.1, deduced, whose Lemma 11.0 repair is "
                "seated and, with D618's edits to sections 9.5 and 11, awaits a confirming read" in b1n,
            "b1: BEYOND5 Lemma 6.4 (iv)": "on BEYOND5 Lemma 6.4 (iv), deduced and read by a verifier," in b1n,
            "b1: the last round not yet read": "the last round of that deduction, not yet read by a verifier" in b1n,
            "b1, b2: 'supplement section 11.1'": "supplement section 11.1" in b1n and "supplement section 11.1" in b2n,
            "b2: 'It is deduced'": "6.3, deduced). It is deduced, with no gluing," in b2n,
            "b2: conditional on Parts III, IV, VII and VIII, proved, and Theorem P, proved":
                "Theorem R5.1), conditional on the write-out's Parts III, IV, VII and VIII, proved; on Theorem P, "
                "proved;" in b2n,
            "b2: rounds 1-8, round 8 unread": "rounds 1–8, Theorem R5.1" in b2n
            and "round 8 of SETTLE-GLAM5.md, not yet read by a verifier" in b2n,
            "b2: BEYOND5 Lemma 6.4 (iv) deduced": "on BEYOND5 Lemma 6.4 (iv), deduced and read by a verifier;" in b2n,
            "b2: R6-D seated, awaiting a confirming read": "(SETTLE-GLAM5.md R6-D) is seated and, with D618's edits to "
            "sections 9.5 and 11, awaits a confirming read" in b2n,
            "b2: eps named": "its threshold ε, and with it λ1 and δ" in b2n,
            "b2: Proposition 3.1 deduced":
                "(deduced, SETTLE-GLAM5.md Proposition 3.1; computed for a bump envelope" in b2n,
            "b2: the r^(-4) term for one example": "for one example, the general case being deduced" in b2n,
            "b2: the window from measured and hand-counted exponents":
                "the weight window, computed from those measured exponents and from exponents counted by hand (those "
                "of the data class, of the pointwise bound, and of two further thresholds, which do not bind)" in b2n,
            "b3: deduced, conditionally": "is deduced, conditionally, in section 9" in b3n,
            "no stronger status word in any block": no_strong}


def e4(S):
    print("E4  R8-E's paper blocks (final) against RESPONSE-HL-5D.md (not edited)")
    a = S.index("### R8-E ")
    b = S.index("Ledger (round 8).", a)
    bl = re.findall(r"```text\n(.*?)\n```", S[a:b], flags=re.S)
    if len(bl) != 6:
        check("E4a six blocks read", False, str(len(bl)))
        return
    P = open(PAPER).read()
    counts = [P.count(bl[i]) for i in (0, 2, 4)]
    check("E4a each old text occurs exactly once in the paper", counts == [1, 1, 1], str(counts))
    Q = P
    for i in (0, 2, 4):
        Q = Q.replace(bl[i], bl[i + 1], 1)
    long_ = [(k + 1, len(l)) for k, l in enumerate(Q.split("\n")) if len(l) > 121]
    check("E4b the edited paper keeps every line within 121 characters", not long_, str(long_[:5]))
    pr = paper_predicates8(bl[1], bl[3], bl[5])
    check("E4c the new blocks state the status words (deduced, conditional on; Parts III, IV, VII, VIII and Theorem P "
          "proved; no stronger word), section 11.1's status, BEYOND5 Lemma 6.4 (iv) in blocks 1 and 2, the rounds read "
          "and unread, eps, Proposition 3.1 as deduced, the r^(-4) term for one example, and the window's measured and "
          "hand-counted exponents", all(pr.values()), str([k for k, v in pr.items() if not v]))
    a7 = S.index("### R7-E ")
    b7 = S.index("Ledger (round 7).", a7)
    bl7 = re.findall(r"```text\n(.*?)\n```", S[a7:b7], flags=re.S)
    pr7 = paper_predicates8(bl7[1], bl7[3], bl7[5])
    check("E4c' control (R7-E's blocks, the round-7 reader's m1 and nit 6): they fail the three predicates on BEYOND5 "
          "in block 1, the rounds, and the window's hand-counted list",
          {k for k, v in pr7.items() if not v} == {"b1: BEYOND5 Lemma 6.4 (iv)", "b2: rounds 1-8, round 8 unread",
                                                   "b2: the window from measured and hand-counted exponents"},
          str(sorted(k for k, v in pr7.items() if not v)))


def main():
    S = open(os.path.join(ROOT, "SETTLE-GLAM5.md")).read()
    blocks = section_blocks(S, "### R6-D ", "### R6-E ")
    P = open(os.path.join(ROOT, "N1STAR-PROOF.md")).read()
    o1, n1, o2, n2 = blocks
    live = P
    seated = P.count(o1) == 0 and P.count(o2) == 0 and P.count(n1) == 1 and P.count(n2) == 1
    if seated:      # D630: R6-D is seated in the live file; it is undone in memory and every check runs as before
        print("E1s R6-D is seated (D630): each new block occurs once in the live file and no old block; R6-D is undone "
              "in memory with its two marks, and E1-E3 run on that copy")
        P = unseat(P, blocks)
    Q = e1(blocks, P)
    if Q is not None:
        if seated:
            check("E1s re-applying R6-D to the undone copy gives the live file but for its two D630 marks (2 found)",
                  Q == D630_MARK.sub(" ", live) and len(D630_MARK.findall(live)) == 2)
        e2(Q)
        e3(blocks, P)
    e4(S)
    print("FAILED:", FAIL if FAIL else "none")
    return 1 if FAIL else 0


if __name__ == "__main__":
    sys.exit(main())
