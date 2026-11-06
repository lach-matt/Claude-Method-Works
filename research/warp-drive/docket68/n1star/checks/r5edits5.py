"""r5edits5.py -- SETTLE-GLAM5 round 5: the replacement text for N1STAR-PROOF.md's Lemma 11.0 (R5-D) and the facts its
new sentences state (the round-4 reader's m1-m2 and the section-11 reader's notes 1-7).

  E1 (text) R5-D's four blocks, read from SETTLE-GLAM5.md as printed there, applied to a copy of N1STAR-PROOF.md (the
     file is not edited): each old block occurs exactly once, the edited file has every line within 121 characters, it
     differs from the original only inside Lemma 11.0, and the edited Lemma 11.0 (a) defines R_gamma before its first
     use and R_gamma^n inside the text ("R_gamma^n being R_gamma with ..."); (b) carries the factor 1/2 and the binomial
     coefficients C(gamma, gamma') at both Leibniz sums (the sums whose summand is (d^{gamma'} g_lam^{ab})
     d^{gamma - gamma'} d_a d_b u_1); (c) names the u_1-free source d_X^gamma F_1(X, 0, 0) in E_3;
     (d) reads "and by (9.8) for u_1^n at the lowest)" where the original had "and by Theorem P for the lowest)";
     (e) gives c's remainder as E_(3/2)
     and d u's phase-shift term as E_(5/2); (f) says that b . d U and c U enter through Lemma 9.5's source before
     Gronwall's lemma, not through its kernel. Control (the code under test applied to the original text): every one of
     (a)-(f) fails on the current Lemma 11.0.
  E2 (exact, sympy) d u's lam^0 terms by the two-scale chain rule, in the radial model: the lam^0 part of
     d(lam W(r, v/lam + phi_1)) is dv d_th W(r, theta + phi_1); its difference from dv d_th W(r, theta), with W =
     r^(-3/2) w(theta) and phi_1 = c r^-1 (phi_1 in L_1), decays exactly like r^(-5/2) (E_(5/2)), and the lam^0 part of
     d(lam chi(r, v/lam)), chi = r^-2 X(theta), is dv d_th chi, decaying like r^-2 (E_2). Control (the phase shift
     mutated to phi_1 = c, not decaying): the difference decays like r^(-3/2) and the E_(5/2) claim fails.
  E3 (computed, 40 digits, on the full five-dimensional gauge-fixed operator with f1lemma5.py's machinery) the
     u_1-free source F_1(X, 0, 0) = -Ric^H(g0 + U3; g0), U3 := lam r^(-3/2) (2 + sin v) sin(v/lam) P, along a ray at
     fixed v (r = 16, 64, 256, 1024; lam = 1e-2): fitted decay exponent 3 (to 0.1): E_3. Control (the amplitude mutated
     to r^-1, not a radiation field): decay 2.
Labels: E1 text checks; E2 exact; E3 computed (mpmath).

    python3 checks/r5edits5.py
"""
import os
import re
import sys

import mpmath as mp
import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import f1lemma5 as F  # noqa: E402

FAIL = []
print = F.print


def check(name, ok, msg=""):
    print(f"  {name}: {'pass' if ok else 'FAIL'} {msg}")
    if not ok:
        FAIL.append(name)


ROOT = os.path.dirname(HERE)


def r5d_blocks():
    s = open(os.path.join(ROOT, "SETTLE-GLAM5.md")).read()
    a = s.index("### R5-D ")
    b = s.index("### R5-E ", a)
    sec = s[a:b]
    blocks = re.findall(r"```text\n(.*?)\n```", sec, flags=re.S)
    assert len(blocks) == 4, len(blocks)
    return blocks


def lemma110(text):
    a = text.index("**Lemma 11.0 (every order at fixed lam).**")
    b = text.index("**Lemma 11.1 (the equation for u).**", a)
    return text[a:b]


def predicates(L):
    L = re.sub(r"\s+", " ", L)  # the text with its line breaks removed
    first_Rn = L.find("R_gamma^n")
    p = {}
    p["a"] = (first_Rn >= 0 and "R_gamma :=" in L and L.index("R_gamma :=") < first_Rn
              and "R_gamma^n being R_gamma with" in L)
    # the Leibniz sums: those whose summand is (d^{gamma'} g_lam^{ab}) d^{gamma - gamma'} d_a d_b u_1
    sums = [m.start() for m in re.finditer(r"sum_\{[^}]*gamma'[^}]*\}", L)
            if "(d^{gamma'} g_lam^{ab}) d^{gamma - gamma'} d_a d_b" in L[m.start():m.start() + 90]]
    p["b"] = len(sums) == 2 and all("(1/2)" in L[max(0, i - 8):i] and "C(gamma, gamma')" in L[i:i + 40] for i in sums)
    p["c"] = "d_X^gamma F_1(X, 0, 0)" in L and "u_1-free source, in E_3" in L
    p["d"] = "and by Theorem P for the lowest)" not in L and "and by (9.8) for u_1^n at the lowest)" in L
    p["e"] = "W_TT] + E_(3/2)" in L and "phase shift's term in E_(5/2)" in L
    p["f"] = "before Gronwall's" in L and "not through its kernel" in L
    return p


def e1():
    print("E1  R5-D's replacement text for Lemma 11.0, applied to a copy of N1STAR-PROOF.md")
    o1, n1, o2, n2 = r5d_blocks()
    P = open(os.path.join(ROOT, "N1STAR-PROOF.md")).read()
    once = P.count(o1) == 1 and P.count(o2) == 1
    check("E1a each old block occurs exactly once in the current file", once, f"{P.count(o1)}, {P.count(o2)}")
    if not once:
        return
    Q = P.replace(o1, n1, 1).replace(o2, n2, 1)
    long_ = [(i + 1, len(l)) for i, l in enumerate(Q.split("\n")) if len(l) > 121]
    check("E1b the edited file keeps every line within 121 characters", not long_, str(long_[:5]))
    a, b = P.index("**Lemma 11.0"), P.index("**Lemma 11.1")
    a2, b2 = Q.index("**Lemma 11.0"), Q.index("**Lemma 11.1")
    check("E1c the edit changes nothing outside Lemma 11.0", P[:a] == Q[:a2] and P[b:] == Q[b2:],
          f"{len(Q.split(chr(10))) - len(P.split(chr(10)))} lines added")
    new_p, old_p = predicates(lemma110(Q)), predicates(lemma110(P))
    check("E1d the edited Lemma 11.0 satisfies (a) R_gamma, R_gamma^n defined, (b) 1/2 and C(gamma, gamma') at both "
          "sums, (c) the u_1-free source, (d) (9.8) for u_1^n, (e) E_(3/2) and E_(5/2), (f) through the source before "
          "Gronwall",
          all(new_p.values()), str(new_p))
    check("E1e control (the same predicates on the current, unedited Lemma 11.0): every one fails",
          not any(old_p.values()), str(old_p))


def e2():
    print("E2  the lam^0 terms of d u (two-scale chain rule, radial model)")
    r, th, lam, c = sp.symbols("r theta lam c", positive=True)
    w = sp.Function("w")
    Xf = sp.Function("X")

    def lam0_dr(field, phase_r):
        """the lam^0 part of the d_r-component (at fixed t, v = t + r) of lam * field(r, v/lam + phase(r)):
        lam [d_r field + (1/lam + phase') d_th field]"""
        Li = sp.Symbol("Li")
        tot = lam*(sp.diff(field, r) + (Li + sp.diff(phase_r, r))*sp.diff(field, th))
        tot = sp.expand(tot.subs(Li, 1/lam))
        return sp.simplify(tot.coeff(lam, 0))

    def shifted(phi):
        W = r**sp.Rational(-3, 2)*sp.sin(th + phi)*sp.Rational(3, 2)
        return lam0_dr(W, phi)

    base = lam0_dr(r**sp.Rational(-3, 2)*sp.sin(th)*sp.Rational(3, 2), sp.Integer(0))
    d1 = sp.simplify(shifted(c/r) - base)
    lim52 = sp.limit((d1*r**sp.Rational(5, 2)).subs({th: sp.Rational(1, 3), c: sp.Rational(7, 5)}), r, sp.oo)
    lim2 = sp.limit((d1*r**2).subs({th: sp.Rational(1, 3), c: sp.Rational(7, 5)}), r, sp.oo)
    check("E2a the phase shift phi_1 = c r^-1 (L_1) adds to dv [d_th W] a lam^0 term decaying exactly like r^(-5/2)",
          lim52.is_finite and lim52 != 0 and lim2 == 0, f"r^(5/2) x term -> {sp.nsimplify(lim52)}")
    chi = r**-2*sp.cos(2*th)
    lc = lam0_dr(chi, sp.Integer(0))
    l2 = sp.limit((lc*r**2).subs(th, sp.Rational(1, 3)), r, sp.oo)
    check("E2b the lam^0 part of d(lam chi), chi = r^-2 cos(2 theta), is d_th chi, decaying like r^-2 (E_2)",
          sp.simplify(lc - sp.diff(chi, th)) == 0 and l2.is_finite and l2 != 0)
    dm = sp.simplify(shifted(c) - base)
    l52m = sp.limit((dm*r**sp.Rational(5, 2)).subs({th: sp.Rational(1, 3), c: sp.Rational(7, 5)}), r, sp.oo)
    check("E2c control (phi_1 mutated to the constant c): the term decays only like r^(-3/2), the E_(5/2) claim fails",
          not l52m.is_finite or l52m in (sp.oo, -sp.oo), str(l52m))


def e3():
    print("E3  the u_1-free source F_1(X, 0, 0) on the full operator")
    mp.mp.dps = 40
    G0 = F.gb0()
    J0_s = F.Jets(G0)
    V = F.t + F.RR
    res = {}
    for name, pw in (("r^(-3/2)", sp.Rational(-3, 2)), ("control r^-1", sp.Integer(-1))):
        U3 = F.lam*F.RR**pw*(2 + sp.sin(V))*sp.sin(V/F.lam)*F.PMAT
        Js = F.Jets(G0 + U3)
        vals = []
        for r in (16, 64, 256, 1024):
            X = [mp.mpf("1.3") - r] + [r*mp.mpf("0.5")]*4
            lv = mp.mpf("1e-2")
            vals.append(mp.mnorm(F.ricH(Js.at(X, lv), J0_s.at(X, lv)), 1))
        res[name] = [float(mp.log(vals[i - 1]/vals[i])/mp.log(4)) for i in range(1, 4)]
    s3, sc = res["r^(-3/2)"][-1], res["control r^-1"][-1]
    check("E3 |F_1(X, 0, 0)| = |Ric^H(g0 + U3)| decays like r^-3 along the ray (E_3)", abs(s3 - 3) < 0.1,
          str([round(x, 3) for x in res["r^(-3/2)"]]))
    check("E3' control (amplitude r^-1): decay 2", abs(sc - 2) < 0.1, str([round(x, 3) for x in res["control r^-1"]]))


def main():
    for f in (e1, e2, e3):
        f()
    print("FAILED:", FAIL if FAIL else "none")
    return 1 if FAIL else 0


if __name__ == "__main__":
    sys.exit(main())
