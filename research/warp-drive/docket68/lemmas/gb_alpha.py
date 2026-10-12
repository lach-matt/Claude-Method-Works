#!/usr/bin/env python3
"""gb_alpha.py -- item 325: "there is at least one unevaluated coefficient still present in the math.  Evaluating the
coefficients to exact value will give us alpha's value".  relativity.py U4 left the Gauss-Bonnet coupling alpha -- the
one constant relativity leaves the five-dimensional bulk -- free, and gave its effect on item 322's offset at an
estimated size (4e-39, alpha set by the five-dimensional Planck length).  Evaluated exactly here, from the coefficients
the record already fixes.  Worked in the conversation (computed with sympy, exact where marked; READ where marked;
deduced where marked; not verified by a separate session; not seated); 2026-10-12.

  B0 (read) The words this rests on, verbatim in the rulings file: M's item 325; 201, M's "σ and its dark-energy
     offset", carried as "B6' (k's scale) becomes a DEFINITION", "the offset carries the dark energy" and "k_R =
     k_L/2"; 202, "the same definitions as we do"; 226, "its plane's tension and offset among them"; and 127 (2), "The
     coefficient value is the difference of that value in a counterfactual universe and its value in our current
     universe, added to the value of our current universe".
  B1 (READ; computed, exact) The Gauss-Bonnet relations.  Charmousis and Dufaux (hep-th/0202107, READ): the tension
     that keeps the plane flat, T = [(1 - s)/alpha]^(1/2) (2 + s) (their eq. (25), units M^3 = 1), the Planck mass on
     it, m_Pl^-2 = M^-3 (1 - s)^(1/2)/(2 sqrt(alpha) (2 - s)) (eq. (27)), and the bulk's curvature from its vacuum
     solution, V = r^2 (1 - s)/(4 alpha) (eq. (17), mu = 0) -- s = sqrt(1 - 8 alpha k^2), q = (1 - s)/(4 alpha) the
     square of the bulk's curvature and ell = 1/sqrt(q) its radius.  Both read formulas follow from their eq. (22) on
     its stable branch (computed: T is the flat value of Sigma = 6 s sqrt(X) + 16 alpha X^(3/2), and 8 pi G is the
     inverse of its response, relativity U4).  Then, exactly (computed):
       sigma G ell^2 = (2 + s)/(4 pi (2 - s))          (ell the bulk's radius 1/sqrt(q));
       sigma G ell^2 = (2 + s)/(2 pi (2 - s)(1 + s))   (ell read instead as 1/k);
       G/(kappa^4 sigma/(48 pi)) = 3/(4 - s^2)         (against the Shiromizu-Maeda-Sasaki law the record reads).
     Each is Einstein's value -- 3/(4 pi), 3/(4 pi), 1 -- at s = 1, alpha = 0.  The first holds on both signs of alpha
     (computed, 30 digits, at alpha k^2 = -3/10, -1/10, 1/20, 1/10: for alpha < 0, s > 1 and the square roots pair into
     real ones), so solving over s >= 0 covers alpha < 0 as well.
  B2 (deduced; computed, exact) Evaluated for ours.  201 makes B6' a definition of our plane's tension: sigma = 3
     c^4/(4 pi G ell^2), the coefficient 3/(4 pi) exact; the same sigma is the tension of every junction in the record
     (139 (1), p2_assume Q3).  With alpha it reads (2 + s1)/(4 pi (2 - s1)), so (2 + s1)/(2 - s1) = 3, s1 = 1
     (computed; with ell read as 1/k, 3 s^2 - s - 2 = 0, roots 1 and -2/3, and s >= 0 leaves 1).  s1 = 1 means alpha
     k1^2 = 0, and our bulk's radius is finite (ell <= 13.964 um, B6P-SCALE), k1 != 0: alpha = 0 exactly (deduced).
     The estimate came from leaving alpha's coefficient open; B6''s coefficient closes it.  It holds whatever sigma's
     scale is, which the record has not fixed (201's window) -- alpha needs no scale, only the coefficient.
  B3 (deduced; computed, exact) Evaluated for position 2's bulk.  202 gives position 2 "the same definitions as we do":
     its side is defined as ours is, its side's tension sigma/2, its coupling and its radius meeting B6''s coefficient,
     so s2 = 1 and alpha2 = 0 in the same way (deduced).  Independently, 201 records k_R = k_L/2: on position 2's side,
     flat at zero offset (p2_assume Q3), sigma/2 = (k2/kappa^2) Phi(alpha2 k2^2) with Phi = sqrt(8/(1 + s)) (2 + s)
     (computed, exact), and with ours Einstein's (B2), k2 = k1/2 needs Phi = 6, 2 s^2 - s - 1 = 0, s = 1 (the other root
     -1/2 is not a square root) -- alpha2 = 0 again.  Phi is strictly increasing in s (d/ds of (2 + s)^2/(1 + s) is
     s (2 + s)/(1 + s)^2 >= 0, computed), so no other alpha2 gives Phi = 6.
  B4 (computed) What it settles.  alpha = 0 in both bulks: the one constant relativity left the bulk is evaluated, and
     Einstein's law holds there exactly -- the record's Israel and Gauss-Codazzi conditions are not its leading order
     but its law.  relativity U4's factor (1 - 4 alpha k1^2) is 1, and item 322's offset is exactly x+ = d1/2 - 3
     d1^2/(2 sigma) + ... = 2.625e-10 J/m^3 (p2_offset V6), its estimated shift (4e-39) withdrawn.
  B5 (deduced) 127 (2)'s rule, applied to alpha: its value in our current universe is 0 (B2), in the counterfactual one
     (position 2, B3) 0; the coefficient is 0 + (0 - 0) = 0.
  B6 (the cypher NOT-RUN, stated) alpha is the root of exact equations the record fixes, not a choice among
     configurations; an index of (alpha, meets B6', meets k_R = k_L/2) rows would carry the answer as its own column, a
     key (211), as p2_offset V8 and p2_assume Q7 found.  Not run, and said.

What this does not claim.
  - That alpha = 0 without 201: it follows from B6''s coefficient being exact, as 201 made it; were B6' replaced by its
    Gauss-Bonnet form, alpha would be free again, and the record holds no other relation that fixes it (KDERIVE: the
    ratio of curvatures comes from the same junction, the scale from nothing yet).
  - That alpha = 0 is measured: B6' and k_R = k_L/2 were written in Einstein's theory and 201 made them definitions;
    alpha = 0 is what those definitions entail, exactly -- an evaluation of the record's coefficients, which item 325
    asked for, not a measurement of the bulk.
  - sigma's scale: B2 needs none.

Imports nothing from the record but the rulings file.  Stdlib + sympy.  python3 gb_alpha.py [--selftest | --mutants]
"""
import os
import sys

import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
D68 = os.path.dirname(HERE)
RULINGS = os.path.join(D68, "M-RULINGS-2026-10-03.md")
MUT = {}
WORDS = ("there is at least one unevaluated coefficient still present in the math. Evaluating the coefficients to exact "
         "value will give us α's value", "σ and its dark-energy offset", "B6' (k's scale) becomes a DEFINITION",
         "the offset carries the dark energy", "k_R = k_L/2", "the same definitions as we do",
         "its plane's tension and offset among them",
         "The coefficient value is the difference of that value in a counterfactual universe and its value in our "
         "current universe, added to the value of our current universe")
al, k, kap, X = sp.symbols("alpha k kappa X", positive=True)
s = sp.Symbol("s", nonnegative=True)


def relations():
    """B1: T (25), 8 pi G (27), q (17); from (22); sigma G ell^2 and the SMS ratio, exactly"""
    sk = sp.sqrt(1 - 8 * al * k ** 2)
    q = (1 - sk) / (4 * al)
    half = sp.Rational(1, 2) if MUT.get("cd_half") else 1   # the mutant: (25) misread with a factor 1/2
    T25 = half * sp.sqrt((1 - sk) / al) * (2 + sk) / kap ** 2
    G27 = kap ** 2 * sp.sqrt(1 - sk) / (2 * sp.sqrt(al) * (2 - sk)) / (8 * sp.pi)
    Sig = (6 * sk * sp.sqrt(X) + 16 * al * X ** sp.Rational(3, 2)) / kap ** 2       # eq. (22), stable branch
    from22_T = sp.simplify(Sig.subs(X, q) - T25) == 0
    resp = sp.diff(Sig, X).subs(X, q)
    from22_G = sp.simplify(3 / (8 * sp.pi * resp) - G27) == 0
    einstein = sp.simplify(sp.limit(T25, al, 0) - 6 * k / kap ** 2) == 0 and \
        sp.simplify(sp.limit(G27, al, 0) - kap ** 2 * k / (8 * sp.pi)) == 0
    a_, k_ = sp.symbols("a_ k_")                            # sign-free, for alpha < 0 as well (B1)
    s_ = sp.sqrt(1 - 8 * a_ * k_ ** 2)
    form = sp.sqrt((1 - s_) / a_) * (2 + s_) * sp.sqrt(1 - s_) / (2 * sp.sqrt(a_) * (2 - s_)) / (8 * sp.pi) \
        / ((1 - s_) / (4 * a_)) * half
    both_signs = all(abs(complex(sp.N(form.subs({a_: av, k_: 1}), 30)) - complex(sp.N(
        (2 + sp.sqrt(1 - 8 * av)) / (4 * sp.pi * (2 - sp.sqrt(1 - 8 * av))), 30))) < 1e-25
        for av in (sp.Rational(-3, 10), sp.Rational(-1, 10), sp.Rational(1, 20), sp.Rational(1, 10)))
    sub = {al: (1 - s ** 2) / (8 * k ** 2)}                 # alpha in terms of s at fixed k
    eff = sp.simplify((T25 * G27 / q).subs(sub))
    bare = sp.simplify((T25 * G27 / k ** 2).subs(sub))
    sms = sp.simplify((G27 / (kap ** 4 * T25 / (48 * sp.pi))).subs(sub))
    return dict(from22_T=from22_T, from22_G=from22_G, einstein=einstein, eff=eff, bare=bare, sms=sms,
                both_signs=both_signs,
                eff_ok=sp.simplify(eff - (2 + s) / (4 * sp.pi * (2 - s))) == 0,
                bare_ok=sp.simplify(bare - (2 + s) / (2 * sp.pi * (2 - s) * (1 + s))) == 0,
                sms_ok=sp.simplify(sms - 3 / (4 - s ** 2)) == 0)


def evaluate(rl):
    """B2-B3: B6''s exact coefficient gives s = 1; 201's ratio with flatness gives s2 = 1"""
    coeff = sp.Rational(3, 4) / sp.pi
    if MUT.get("b6_loose"):
        coeff = coeff * sp.Rational(101, 100)              # the mutant: B6''s coefficient read as approximate
    roots_eff = [r for r in sp.solve(sp.Eq(rl["eff"], coeff), s) if r.is_nonnegative]
    roots_bare = [r for r in sp.solve(sp.Eq(rl["bare"], coeff), s) if r.is_nonnegative]
    roots_sms = [r for r in sp.solve(sp.Eq(rl["sms"], 1), s) if r.is_nonnegative]
    alpha_of_s = lambda sv: sp.simplify((1 - sv ** 2) / 8)  # alpha k^2
    w_eff = [alpha_of_s(r) for r in roots_eff]
    Phi = sp.sqrt(8 / (1 + s)) * (2 + s)
    sk = sp.sqrt(1 - 8 * al * k ** 2)
    Phi_from = sp.simplify((sp.sqrt((1 - sk) / (al * k ** 2)) * (2 + sk)).subs(al, (1 - s ** 2) / (8 * k ** 2)))
    phi_ok = sp.simplify(Phi_from - Phi) == 0
    mono = sp.factor(sp.diff((2 + s) ** 2 / (1 + s), s))
    mono_ok = sp.simplify(mono - s * (2 + s) / (1 + s) ** 2) == 0
    ratio = sp.Rational(3, 4) if MUT.get("ratio_doubled") else sp.Rational(1, 2)    # the mutant: k_R = 3 k_L/4
    target = 3 / ratio                                     # sigma/2 = 3 k1/kappa^2 = (ratio k1/kappa^2) Phi
    roots_phi = [r for r in sp.solve(sp.Eq(Phi ** 2, target ** 2), s) if r.is_nonnegative]
    w2 = [alpha_of_s(r) for r in roots_phi]
    return dict(roots_eff=roots_eff, roots_bare=roots_bare, roots_sms=roots_sms, w_eff=w_eff, phi_ok=phi_ok,
                mono_ok=mono_ok, roots_phi=roots_phi, w2=w2,
                coeff_127=sp.Integer(0) + (sp.Integer(0) - sp.Integer(0)))


def compute():
    rl = relations()
    return dict(rl=rl, ev=evaluate(rl))


def report(o):
    rl, ev = o["rl"], o["ev"]
    print("gb_alpha.py -- the Gauss-Bonnet coupling evaluated (item 325)\n")
    print("B1 (25) and (27) from (22): %s, %s; Einstein limit %s; sigma G ell^2 = %s (bulk radius), %s (1/k); "
          "G/SMS = %s" % (rl["from22_T"], rl["from22_G"], rl["einstein"], rl["eff"], rl["bare"], rl["sms"]))
    print("B1 the same on both signs of alpha: %s" % rl["both_signs"])
    print("B2 B6''s 3/(4 pi) exact: s = %s (radius), %s (1/k), SMS's 1: %s; alpha k1^2 = %s" % (
        ev["roots_eff"], ev["roots_bare"], ev["roots_sms"], ev["w_eff"]))
    print("B3 Phi = sqrt(8/(1 + s)) (2 + s): %s; increasing in s: %s; k_R = k_L/2 needs s = %s, alpha2 k2^2 = %s" % (
        ev["phi_ok"], ev["mono_ok"], ev["roots_phi"], ev["w2"]))
    print("B5 127 (2): 0 + (0 - 0) = %s" % ev["coeff_127"])


def checks(o):
    rl, ev = o["rl"], o["ev"]
    res = []
    add = lambda n, ok: res.append((n, bool(ok)))
    rul = " ".join(open(RULINGS, encoding="utf-8").read().split())
    add("B0 item 325, 201's definition and ratio, 202, 226 and 127 (2) verbatim in the rulings file",
        all(w in rul for w in WORDS))
    add("B1 Charmousis-Dufaux (25) and (27) follow from (22) and reduce to Einstein's at alpha = 0",
        rl["from22_T"] and rl["from22_G"] and rl["einstein"])
    add("B1 sigma G ell^2 = (2 + s)/(4 pi (2 - s)) or (2 + s)/(2 pi (2 - s)(1 + s)); G/SMS = 3/(4 - s^2)",
        rl["eff_ok"] and rl["bare_ok"] and rl["sms_ok"])
    add("B1 sigma G ell^2 = (2 + s)/(4 pi (2 - s)) on both signs of alpha (30 digits at four values)", rl["both_signs"])
    add("B2 B6''s exact coefficient leaves s = 1 alone on either reading of ell, and SMS's law too: alpha = 0",
        ev["roots_eff"] == [1] and ev["roots_bare"] == [1] and ev["roots_sms"] == [1] and ev["w_eff"] == [0])
    add("B3 Phi = sqrt(8/(1 + s)) (2 + s), increasing in s; k_R = k_L/2 with flatness leaves s = 1: alpha2 = 0",
        ev["phi_ok"] and ev["mono_ok"] and ev["roots_phi"] == [1] and ev["w2"] == [0])
    add("B5 127 (2): the coefficient is 0 + (0 - 0) = 0", ev["coeff_127"] == 0)
    return res


MUTANTS = {"cd_half": "Charmousis-Dufaux's (25) misread with a factor 1/2 (B1)",
           "b6_loose": "B6''s coefficient read as approximate, 1 % off (B2)",
           "ratio_doubled": "position 2's curvature ratio read as the doubled count's 3/4 (B3)"}


def selftest():
    r_ = checks(compute())
    for n, ok in r_:
        print("  [%s] %s" % ("ok" if ok else "FAIL", n))
    kk = sum(ok for _, ok in r_)
    print("selftest: %d/%d" % (kk, len(r_)))
    return kk == len(r_)


def mutants():
    caught = 0
    for kk, desc in MUTANTS.items():
        MUT.clear()
        MUT[kk] = True
        try:
            failed = sorted({n.split()[0] for n, ok in checks(compute()) if not ok})
        except Exception as ex_:
            failed = ["raised %s" % type(ex_).__name__]
        MUT.clear()
        caught += bool(failed)
        print("  mutant %-14s %-60s %s" % (kk, desc, "caught by " + ", ".join(failed) if failed else "NOT CAUGHT"))
    print("mutants: %d/%d caught" % (caught, len(MUTANTS)))
    return caught == len(MUTANTS)


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    if "--mutants" in sys.argv:
        sys.exit(0 if mutants() else 1)
    report(compute())
