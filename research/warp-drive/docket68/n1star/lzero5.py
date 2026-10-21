#!/usr/bin/env python3
"""lzero5.py -- the l = 0 sector of the gauge-vector equation on five-dimensional Tangherlini: the identities behind
[Hun19] section 8 (Theorem 8.1, the convergence of a spherically symmetric solution of box W = 0 to a multiple of the
stationary one-form W*) in five dimensions (N1STAR-PROOF.md section 10.8; D50).  Labels: computed (exact, sympy), READ.

A spherically symmetric one-form W = W0 dt + f^-1 W1 dr on g = -f dt^2 + dr^2/f + r^2 gamma_{S^3}, f = 1 - mu/r^2, with
box W = 0 (Proposition 10.2(i): the gauge vector of an l = 0 perturbation).  Hung's quantities read in five dimensions:
S_W := tr pi_W = 2 div W, P := r (dW)_tr - 2 W0 (his P_even = r (dW)_tr - W0), W3 := f^-1 (W1 - W0) (the dr-component
in the ingoing chart, regular at the horizon), L' := f^-1 (d_t - f d_r), box_s := -f^-1 d_t^2 + f d_r^2 + ((3 r^2 -
mu)/r^3) d_r the scalar wave operator at l = 0.

  Z1 (computed, exact) The components of box W, his (8.2)-(8.3):
       (box W)_t = box_s W0 + (4 mu/r^4) W0 + (2 mu/r^4) P,
       f (box W)_r = box_s W1 - (3/r^2)(1 - 3 mu/r^2) W1 - (mu/r^3) S_W
     (four dimensions: box W0 + (2M/r^3) W0 = -(2M/r^3) P_even and box W1 - (2/r^2)(1 - 4M/r) W1 = (M/r^2) S_W).
     Control: P with Hung's coefficient -W0 in place of -2 W0.
  Z2 (computed, exact) His (8.4)-(8.5): modulo box W = 0, box_s P = d_t S_W and box_s S_W = 0; the coefficient -2 in P is
     the one value for which box_s P is d_t S_W times a constant.  Control: as Z1's.
  Z3 (computed, exact) His (8.9)-(8.12) in (W0, W3): P = r d_t W3 + r L' W0 - 2 W0; S_W = -2 L' W0 + 2 f d_r W3 + (6/r)
     W0 + (6/r)(1 - mu/(3 r^2)) W3; the W3 equation f^-1 (f (box W)_r - (box W)_t) = box_s W3 - f' L' W3 - (3 f/r^2) W3
     - (3/r^2) W0, with f' = 2 mu/r^3 > 0 the coefficient of nabla_L' W3 (his 2M/r^2: the red-shift sign); and, modulo
     box W = 0, d_t W0 = (r f/4) d_r S_W - (1/2) d_t P (his (8.12) with r f/2 and 1), so that on the horizon, where f d_r
     = d_t along the generator, W0 + P/2 - (sqrt mu/4) S_W is constant along H^+ (deduced from (8.12), not a check): his
     c_1(oo) is
       c_1(oo) = mu (W0 + P/2 - (sqrt mu/4) S_W)|_{H^+}
     (his -2M (M S_W - P_even - W0)).  Control: the sign of f' L' W3 reversed.
  Z4 (computed, exact) The two radial ODEs of his (8.14) and (8.24).  The W0 equation at fixed tau, f u'' + ((3 r^2 -
     mu)/r^3) u' + (4 mu/r^4) u = 0, has the solutions 1/r^2 (regular; W*'s dt component) and 1 + (mu/r^2) log(r^2/mu -
     1) (singular at the horizon; his 1 + (2M/r) log(r/2M - 1)), Wronskian 1/(r^3 f) up to a constant.  The stationary
     W3 equation S_W = 0 with W0 = c_1/r^2, 2 f W3' + (6/r)(1 - mu/(3 r^2)) W3 = -2 c_1/r^3, has the homogeneous
     solution 1/(r^3 f) (singular; his 1/(r^2 f)) and the regular particular solution -c_1/(r (r + sqrt mu)), which at
     c_1 = 1 is W*'s own W3 (W2: W* = dt/r^2 + sqrt mu dr/(r^3 f)); his particular solution -c_1/r is replaced by
     this one.  Control: 1/r in place of 1/r^2.
  Z5 (computed, exact) His substitution (8.6) at l = 0, P-hat := P + eta_b (u + r) S_W/2 with u := t - r_* + const (u =
     tau for r >= R_null): where eta_b = 1, modulo box_s S_W = 0,
       box_s P-hat = -(mu/(r^2 f)) nabla_L S_W - (mu/(2 r^3)) S_W,
     the d_t S_W of (8.4) cancelled -- the source is s^-2 f^-1 nabla_L S_W and mu^-1/2 s^-3 S_W (his Lemma 8.3 has
     s^-1 nabla_L S_W and M^-1 s^-2 S_W): the same coefficient 1/2 as in four dimensions, with better weights.
     Control: the coefficient 1/4.

READ (alphaXiv, 2026-10-21).  [Hun19] P.-K. Hung, arXiv:1909.06733v1, section 8 pp. 58-69: (8.1)-(8.33), Theorem 8.1,
Propositions 8.2 and 8.4, Lemma 8.3, the red-shift current (8.34) and the argument for d(tau), c_2(tau) and c_1(oo),
Theorem 8.7; Appendix A (A.12)-(A.14), Proposition A.6; Appendix B (the O_j bounds).

sympy.  python3 lzero5.py [--selftest | --mutants]   (about a quarter of a minute; --verbose lists every sub-check)
"""
import os
import sys
import time

import sympy as sp

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import wavegauge5 as WG                                       # the five-dimensional one-form box (W1's machinery)

t, r, mu, f = WG.t, WG.r, WG.mu, WG.f
D = sp.diff
fp = D(f, r)
W0, W1, W3 = [sp.Function(nm)(t, r) for nm in ("W0", "W1", "W3")]


class Checklist:
    def __init__(self, verbose, quiet=False):
        self.ok, self.verbose, self.quiet = True, verbose, quiet

    def __call__(self, name, good):
        self.ok &= bool(good)
        if self.verbose or (not good and not self.quiet):
            print("      [%s] %s" % ("ok" if good else "FAIL", name), flush=True)


def boxs(u):
    """the scalar wave operator at l = 0"""
    return -D(u, t, 2)/f + D(r**3*f*D(u, r), r)/r**3


def Lp(u):
    """L' = f^-1 (d_t - f d_r)"""
    return (D(u, t) - f*D(u, r))/f


_BOXW = None


def boxW():
    """(box W)_t and (box W)_r for W = W0 dt + f^-1 W1 dr, from wavegauge5's box on one-forms"""
    global _BOXW
    if _BOXW is None:
        _BOXW = [sp.simplify(e) for e in WG.box1([W0, W1/f, 0, 0, 0], simp=False)[:2]]
    return _BOXW


def quantities(pcoef=-2):
    SW = 2*sp.simplify(-D(W0, t)/f + D(r**3*W1, r)/r**3)
    P = r*(D(W1/f, t) - D(W0, r)) + pcoef*W0
    return SW, P


def reduce_tt(e):
    """eliminate d_t^2 W0, d_t^2 W1 (and their derivatives) with box W = 0"""
    bt, br = boxW()
    sol = sp.solve([bt, br], [D(W0, t, 2), D(W1, t, 2)], dict=True)[0]
    e = sp.expand(e.doit())
    for _ in range(6):
        rep = {}
        for d in e.atoms(sp.Derivative):
            cnt = dict(d.variable_count)
            if d.expr in (W0, W1) and cnt.get(t, 0) >= 2:
                base = sol[D(d.expr, t, 2)]
                extra = [t]*(cnt[t] - 2) + [r]*cnt.get(r, 0)
                rep[d] = D(base, *extra) if extra else base
        if not rep:
            break
        e = sp.expand(e.xreplace(rep).doit())
    return e


def z1(control=0, verbose=False):
    chk = Checklist(verbose, quiet=control != 0)
    bt, br = boxW()
    SW, P = quantities(-1 if control == 1 else -2)
    chk("(box W)_t = box_s W0 + (4 mu/r^4) W0 + (2 mu/r^4) P, P = r (dW)_tr - 2 W0",
        sp.simplify(bt - (boxs(W0) + 4*mu/r**4*W0 + 2*mu/r**4*P)) == 0)
    chk("f (box W)_r = box_s W1 - (3/r^2)(1 - 3 mu/r^2) W1 - (mu/r^3) S_W",
        sp.simplify(f*br - (boxs(W1) - 3/r**2*(1 - 3*mu/r**2)*W1 - mu/r**3*SW)) == 0)
    return chk.ok


def z2(control=0, verbose=False):
    chk = Checklist(verbose, quiet=control != 0)
    SW, P = quantities(-1 if control == 1 else -2)
    chk("box_s P = d_t S_W modulo box W = 0", sp.simplify(reduce_tt(boxs(P) - D(SW, t))) == 0)
    chk("box_s S_W = 0 modulo box W = 0", sp.simplify(reduce_tt(boxs(SW))) == 0)
    al = sp.Symbol("alpha")
    E = reduce_tt(boxs(r*(D(W1/f, t) - D(W0, r)) + al*W0) - D(SW, t))
    coeffs = [sp.simplify(E.coeff(q)) for q in sorted(E.atoms(sp.Derivative), key=str) + [W0, W1]]
    chk("the coefficient of W0 in P is forced: alpha = -2",
        sp.solve([c for c in coeffs if c != 0], al, dict=True) == [{al: -2}])
    return chk.ok


def z3(control=0, verbose=False):
    chk = Checklist(verbose, quiet=control != 0)
    bt, br = boxW()
    SW, P = quantities()
    sub = {W1: W0 + f*W3}
    chk("P = r d_t W3 + r L' W0 - 2 W0", sp.simplify(P.xreplace(sub).doit() - (r*D(W3, t) + r*Lp(W0) - 2*W0)) == 0)
    chk("S_W = -2 L' W0 + 2 f d_r W3 + (6/r) W0 + (6/r)(1 - mu/(3 r^2)) W3",
        sp.simplify(SW.xreplace(sub).doit() - (-2*Lp(W0) + 2*f*D(W3, r) + 6/r*W0 + 6/r*(1 - mu/(3*r**2))*W3)) == 0)
    sgn = -1 if control == 1 else 1
    eqW3 = sp.simplify((f*br - bt).xreplace(sub).doit()/f)
    chk("the W3 equation f^-1 (f (box W)_r - (box W)_t) = box_s W3 - f' L' W3 - (3 f/r^2) W3 - (3/r^2) W0, with f' > 0",
        sp.simplify(eqW3 - (boxs(W3) - sgn*fp*Lp(W3) - 3*f/r**2*W3 - 3/r**2*W0)) == 0 and fp.subs(r, sp.sqrt(mu)) > 0)
    chk("d_t W0 = (r f/4) d_r S_W - (1/2) d_t P modulo box W = 0 ((8.12) in five dimensions)",
        sp.simplify(reduce_tt(D(W0, t) - (r*f/4*D(SW, r) - D(P, t)/2))) == 0)
    return chk.ok


def z4(control=0, verbose=False):
    chk = Checklist(verbose, quiet=control != 0)
    u1 = 1/r if control == 1 else 1/r**2
    u2 = 1 + mu/r**2*sp.log(r**2/mu - 1)
    ode = lambda u: f*D(u, r, 2) + (3*r**2 - mu)/r**3*D(u, r) + 4*mu/r**4*u
    chk("the W0 equation f u'' + ((3 r^2 - mu)/r^3) u' + (4 mu/r^4) u = 0 has the solutions 1/r^2 and 1 + (mu/r^2) "
        "log(r^2/mu - 1)", sp.simplify(ode(u1)) == 0 and sp.simplify(ode(u2)) == 0)
    wr = sp.simplify(u1*D(u2, r) - u2*D(u1, r))
    chk("their Wronskian is a constant times 1/(r^3 f)", sp.simplify(wr*r**3*f).is_constant())
    c1 = sp.Symbol("c1")
    v = sp.Function("v")(r)
    SW, _ = quantities()
    sub = {W1: W0 + f*W3}
    SWw = sp.expand(SW.xreplace(sub).doit()).xreplace({W0: c1*u1, W3: v}).doit().xreplace({D(v, t): 0})
    SWw = sp.simplify(SWw)
    chk("S_W with W0 = c_1/r^2 and a stationary W3 is 2 f W3' + (6/r)(1 - mu/(3 r^2)) W3 + 2 c_1/r^3",
        sp.simplify(SWw - (2*f*D(v, r) + 6/r*(1 - mu/(3*r**2))*v + 2*c1/r**3)) == 0)
    hom = 1/(r**3*f)
    part = -c1/(r*(r + sp.sqrt(mu)))
    chk("homogeneous solution 1/(r^3 f), singular at the horizon",
        sp.simplify((2*f*D(v, r) + 6/r*(1 - mu/(3*r**2))*v).subs(v, hom).doit()) == 0)
    chk("particular solution -c_1/(r (r + sqrt mu)), regular; at c_1 = 1 it is W*'s W3 = f^-1 (sqrt mu/r^3 - 1/r^2)",
        sp.simplify(SWw.subs(v, part).doit()) == 0
        and sp.simplify(part.subs(c1, 1) - (sp.sqrt(mu)/r**3 - 1/r**2)/f) == 0)
    return chk.ok


def z5(control=0, verbose=False):
    chk = Checklist(verbose, quiet=control != 0)
    SWf = sp.Function("SW")(t, r)
    rstar = sp.integrate(1/f, r)                                  # the tortoise coordinate, up to a constant
    u = t - rstar
    a = sp.Rational(1, 4) if control == 1 else sp.Rational(1, 2)
    e = sp.expand(boxs(a*(u + r)*SWf))
    # modulo box_s S_W = 0: replace d_t^2 S_W
    stt = sp.solve(boxs(SWf), D(SWf, t, 2))[0]
    e = sp.expand(e.xreplace({D(SWf, t, 2): stt}).doit())
    L = lambda w: D(w, t) + f*D(w, r)
    chk("box_s((u + r) S_W/2) = -(mu/(r^2 f)) nabla_L S_W - (mu/(2 r^3)) S_W modulo box_s S_W = 0, u := t - r_*: the "
        "source of P-hat = P + (u + r) S_W/2 for r >= 2 b r_h is d_t S_W + this, with d_t S_W cancelled",
        sp.simplify(e + D(SWf, t) - (-mu/(r**2*f)*L(SWf) - mu/(2*r**3)*SWf)) == 0)
    return chk.ok


CHECKS = [("Z1 the components of box W: (8.2)-(8.3) in five dimensions, P = r (dW)_tr - 2 W0", z1, 1),
          ("Z2 box_s P = d_t S_W and box_s S_W = 0 modulo box W = 0; the coefficient -2 forced", z2, 1),
          ("Z3 (8.9)-(8.12) in (W0, W3): the W3 equation with f' L' W3, the red-shift sign; c_1(oo)", z3, 1),
          ("Z4 the radial ODEs: 1/r^2 and the log solution; 1/(r^3 f) and W*'s W3", z4, 1),
          ("Z5 the substitution P-hat = P + (u + r) S_W/2 of his (8.6): its source weights s^-2 nabla_L, s^-3", z5, 1)]


def selftest(verbose=False):
    ok_all = True
    for name, fn, nc in CHECKS:
        t0 = time.time()
        good = fn(verbose=verbose)
        control = any(fn(control=k) for k in range(1, nc + 1))
        state = "PASS" if good and not control else "FAIL"
        ok_all &= state == "PASS"
        print(f"{name:<100} {state}  {time.time() - t0:.0f}s" + ("" if not control else "  (control passed: vacuous)"),
              flush=True)
    print(f"lzero5.py: {len(CHECKS) if ok_all else 'FAILED'}/{len(CHECKS)}")
    return ok_all


def mutants():
    caught = total = 0
    for name, fn, nc in CHECKS:
        for k in range(1, nc + 1):
            total += 1
            m = fn(control=k)
            caught += (not m)
            print(f"mutant {k} of {name[:2]}: {'caught' if not m else 'NOT caught'}", flush=True)
    print(f"lzero5.py mutants: {caught}/{total}")
    return caught == total


if __name__ == "__main__":
    if "--mutants" in sys.argv:
        sys.exit(0 if mutants() else 1)
    sys.exit(0 if selftest("--verbose" in sys.argv) else 1)
