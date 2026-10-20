#!/usr/bin/env python3
"""face_grav.py -- item 542, lemmas O3gs and O3g: our face under every gravitational perturbation.  M, 542, to the weak
rows: "strengthen the existing lemmas, and ad more for support".  O3s proved the corridor's survival for Wall E's
scalar wave and left "gravitational perturbations [with] Ishibashi-Kodama's mode stability only, outside the row's
scope", while clause (O) says our face damps every disturbance.  Labels: computed (exact unless marked numerical),
READ, deduced, M's.

  W0 (read) M's words, verbatim in the rulings file, 542.
  W1 (READ) Decay of every type at the small end.  Hung, Keller and Wang (1809.05144v1, p. 4, Theorem 2, READ in
     settle5): "in spacetime dimension six and below, the uniform decay estimate E^N_Psi(Sigma_tau) <= C(n, M)
     I_Psi(Sigma_0)/tau^2" for the master quantities of every type (scalar, vector, tensor).  Cardoso, Lemos and
     Yoshida (hep-th/0311260v2, p. 7, READ): "we have found no unstable mode ... consistent with the results by Kodama
     and Ishibashi, who proved all the higher-D Schwarzschild black holes to be stable against small non-radial
     disturbance".
  W2 (computed, exact) The metric from the master fields, every type, regular on the whole exterior (Kodama and
     Ishibashi, hep-th/0305147v3, READ): tensor H_T = r^(-n/2) Phi ((5.4)); vector r^(n-1) F^a = eps^ab D_b (r^(n/2)
     Phi) ((5.12)-(5.13)); scalar F and F_ab from Phi with coefficients over r^2 H and H ((3.14)), H = m + 6x >= 5 for
     every l >= 2 on the exterior (n = 3).  No coefficient vanishes or diverges for r >= r_h: the metric decays with
     its master fields, as settle_late S2 found for the class (scalar, tensor) and here for the vector type too.
  W3 (computed, numerical) The vector type rings down: settle5's characteristic evolution of the l = 2 vector-type
     equation, its least-damped mode by matrix pencil, omega r_h = 1.134 - 0.328 i (e^(-i omega t)), within 1% of the
     continued-fraction value READ (Table 2: 1.1340 + 0.3275 i in their e^(i omega t)); its signal falls by more than
     four orders over t = 10-60 r_h (7.7e4).  Control: the l = 3 vector mode (1.7254, READ) is not the l = 2 one.
  W4 (READ; deduced) Below l = 2: "there exist no physical degrees of freedom for l = 1" in the scalar type (KI p. 7);
     the vector l = 1 mode "simply represents a rotational perturbation of the black hole ... L corresponds to the
     angular-momentum parameter in the Myers-Perry solution" (KI p. 15); l = 0 is the mass.  The corridor is static at
     J = 0 by the delivery's reflections (settle5 T1, settle_late S1); the inflow's random spin, a/r_h = 7.6e-8 (G1's
     489 F9 note), would make the end state the Myers-Perry hole of that spin, a bounded perturbation, not a growing one.
  W5 (READ) The large end.  Dafermos, Holzegel and Rodnianski (1601.06467v1, abstract, READ): "Solutions to the
     linearisation of the Einstein vacuum equations ('linearised gravity') around a Schwarzschild metric arising from
     regular initial data remain globally bounded on the black hole exterior and in fact decay to a linearised Kerr
     metric."  The plane reads the large hole as four-dimensional Schwarzschild to O((ell/r0)^2) (C3, verified 261;
     m1_large), and Figueras and Wiseman's static family is "dynamically stable" (READ, O3's note).
  W6 (deduced) So our face damps every disturbance: every gravitational perturbation decays, the metric with it, at
     both ends, linearly; the parts below l = 2 change the mass, or with spin the member of the family, and decay to
     it.  The nonlinear settling is SETTLEs' and SETTLE's.

Imports ../n1star/settle5.py (the potentials, the evolution, the pencil) by path.  numpy, scipy, sympy.
python3 face_grav.py [--selftest | --mutants]
"""
import contextlib, importlib.util, io, os, sys
import numpy as np
import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
D68 = os.path.dirname(HERE)
RULINGS = os.path.join(D68, "M-RULINGS-2026-10-03.md")
MUT = {}
WORDS = ((542, "strengthen the existing lemmas, and ad more for support"),)
READ_V = {2: 1.1340 + 0.3275j, 3: 1.7254 + 0.3338j}          # CLY03b Table 2, n = 0 (READ)
_MOD = {}


def _settle5():
    if "s5" not in _MOD:
        spec = importlib.util.spec_from_file_location("fg_settle5", os.path.join(D68, "n1star", "settle5.py"))
        mod = importlib.util.module_from_spec(spec)
        sys.modules["fg_settle5"] = mod
        with contextlib.redirect_stdout(io.StringIO()):
            spec.loader.exec_module(mod)
        _MOD["s5"] = mod
    return _MOD["s5"]


def words():
    txt = open(RULINGS, encoding="utf-8").read()
    return all(w in txt for _, w in WORDS)


def w2():
    """the reconstruction's coefficients on r >= r_h (r_h = 1, n = 3), in x = (r_h/r)^2 on (0, 1]: tensor r^(-3/2) =
    x^(3/4); vector r^(-2) = x and r^(3/2) = x^(-3/4); scalar 1/(4 n r^2 H) = x/(12 H) and 1/H, H = m + 6x.  Regular
    means: neither numerator nor denominator has a zero on (0, 1] (sympy solveset, exact)."""
    x, l = sp.symbols("x l", positive=True)
    n = 3
    m = l * (l + n - 1) - n
    H = m + sp.Rational(n * (n + 1), 2) * x
    if MUT.get("H"):
        H = m - 30 * x                                           # the mutant: a coefficient that vanishes outside
    coeffs = {"tensor": [x ** sp.Rational(n, 4)], "vector": [x ** sp.Rational(n - 1, 2), x ** sp.Rational(-n, 4)],
              "scalar": [x / (4 * n * H), 1 / H]}
    dom = sp.Interval.Lopen(0, 1)
    ok = True
    Hmin = None
    for L in range(2, 11):
        for kind, cs in coeffs.items():
            for c in cs:
                num, den = sp.fraction(sp.together(c.subs(l, L)))
                ok &= sp.solveset(num, x, dom) == sp.S.EmptySet and sp.solveset(den, x, dom) == sp.S.EmptySet
        hl = H.subs(l, L)
        hm = min(hl.subs(x, 0), hl.subs(x, 1))                      # H is linear in x: its least value is at an end
        Hmin = hm if Hmin is None else min(Hmin, hm)
    return ok, float(Hmin)


def w3():
    S5 = _settle5()
    t, sig = S5.evolve(2, "vector")
    w = S5.pencil(t, sig, 12.0, 50.0)
    t3, sig3 = S5.evolve(3, "vector") if not MUT.get("l3") else S5.evolve(2, "vector")
    w3_ = S5.pencil(t3, sig3, 12.0, 45.0)
    a = np.max(np.abs(sig[(t > 9) & (t < 11)]))
    b = np.max(np.abs(sig[(t > 58) & (t < 60)]))
    return dict(w=w, w3=w3_, fall=a / b)


def compute():
    return dict(words=words(), w2=w2(), w3=w3())


def checks(o):
    w = o["w3"]
    close = lambda a, b: abs(a - b) <= 0.01 * abs(b)                # noqa: E731
    return {"W0": o["words"],
            "W2": o["w2"][0] and o["w2"][1] >= 5,
            "W3": close(w["w"], READ_V[2]) and close(w["w3"], READ_V[3]) and not close(w["w3"], READ_V[2])
                  and w["fall"] > 1e4}


def report(o=None):
    o = o or compute(); ck = checks(o)
    print("W0 M's words:", o["words"])
    print("W2 every coefficient regular on r >= r_h for l = 2-10, every type: %s; least H %.3g" % o["w2"])
    w = o["w3"]
    print("W3 vector l = 2: omega r_h = %.4f - %.4f i (READ 1.1340, 0.3275); l = 3: %.4f - %.4f i (READ 1.7254); "
          "fall over t 10-60 r_h: %.2g" % (w["w"].real, w["w"].imag, w["w3"].real, w["w3"].imag, w["fall"]))
    for k, v in ck.items():
        print("%s %s" % (k, v))
    return ck


def selftest(quiet=False):
    with contextlib.redirect_stdout(io.StringIO()) if quiet else contextlib.nullcontext():
        ck = report()
    ok = all(ck.values())
    if not quiet:
        print("selftest: %s" % ("PASS" if ok else "FAIL"))
    return ok


MUTANTS = {"H": "a scalar-type coefficient that vanishes on the exterior (W2)",
           "l3": "the l = 3 control run at l = 2 (W3)"}


def mutants():
    caught = 0
    for m, what in MUTANTS.items():
        MUT.clear(); MUT[m] = True
        try:
            ok = selftest(quiet=True)
        except Exception:
            ok = False
        caught += not ok
        print("mutant %-8s %s  (%s)" % (m, "caught" if not ok else "MISSED", what))
    MUT.clear()
    print("%d/%d caught" % (caught, len(MUTANTS)))
    return caught == len(MUTANTS)


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    if "--mutants" in sys.argv:
        sys.exit(0 if mutants() else 1)
    report()
