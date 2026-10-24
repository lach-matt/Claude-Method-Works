#!/usr/bin/env python3
"""settle_asym.py -- item 548, lemma SETTLEa: the formed hole settles outside the class, under perturbations that
break its symmetry.  M, 547: "Do we need the nonlinear settlings to be symmetric or asymmetric in class? And would
having both be helpful and preferred?"; the board answered that the theorem needs the class only and that the
asymmetric case strengthens it; M, 548: "Yes, add the asymmetric settling row to the register".  SETTLEs and SETTLE
settle the record's own solution, which keeps the class's symmetry; this file is the row beside them for a
perturbation that does not.  Labels: computed (exact unless marked), READ, deduced, M's.

  A0 (read) M's words, verbatim in the rulings file, 547 and 548.
  A1 (computed, exact) What the class removes from the end state, and what returns outside it.  A stationary end
     state near Tangherlini carries a spin matrix A in so(4) and a momentum P in R^4 (the linearised family's l = 1
     sector: Kodama and Ishibashi's vector type, six Killing fields of S^3, the rotations; their scalar type, four l = 1
     harmonics, no physical degree of freedom, the translations and boosts).  Each must be invariant under the
     symmetry the data keep, A by conjugation, P by action:
       - the class (T^2 with both reflections): A = 0 and P = 0, the mass alone (settle5 T1; ROUTES-OPEN 4.2);
       - T^2 without the reflections: A in the span of the two rotations, a two-spin Myers-Perry hole, P = 0;
       - no symmetry: A in all of so(4), dimension 6, and P in R^4; a boost leaves Tangherlini Tangherlini in another
         frame, so the set of data settling to Tangherlini itself has codimension 6 in the linearised count.
     Control, four dimensions: axisymmetry with the reflection phi -> -phi leaves J = 0 and a momentum along the axis
     -- Klainerman and Szeftel's class, "its center-of-mass may move along the symmetry axis" (READ, A4) -- and no
     symmetry leaves so(3), dimension 3, Dafermos, Holzegel, Rodnianski and Taylor's codimension 3 (READ, A4).  The
     l = 1 counts, 6 and 4 on S^3 against 3 and 3 on S^2, are computed as the Killing fields (so(n + 1)) and the
     degree-one harmonic polynomials of R^(n + 1).
  A2 (computed, exact) The five-dimensional Myers-Perry family the end state lies in.  From Emparan and Reall's
     formulas (READ, A4) at d = 5: Pi = (r^2 + a^2)(r^2 + b^2), the horizon Pi(r0) = mu r0^2, kappa = (Pi'(r0) - 2 mu
     r0)/(2 mu r0^2), A_H = (pi^2/kappa) mu (2 - 2a^2/(r0^2 + a^2) - 2b^2/(r0^2 + b^2)), M = 3 pi mu/(8G), J_i = (2/3)
     M a_i.  With the horizon angular velocities Omega_i = a_i/(r0^2 + a_i^2) (deduced: the null generator d_t +
     Omega_i d_phi_i of the metric), the first law dM = kappa dA_H/(8 pi G) + Omega_a dJ_a + Omega_b dJ_b holds
     identically in (r0, a, b), exactly; at b = 0 kappa is their T_H's 2 pi T_H = r0/(r0^2 + a^2); at a = b = 0 it is
     Tangherlini, kappa = 1/r0, A_H = 2 pi^2 r0^3.  Control: the first law fails with Omega_i halved.
  A3 (computed, exact to first order in a^2; numbers) The end state outside the class, at the small end.  The record
     breaks the class's symmetry in one place it computes: the README's inflow is round only in the mean, its random
     angular momentum sqrt(n) hbar giving a/r_h = 7.6e-8 at the example (scope C1, imported, not copied).  At fixed
     mass the Myers-Perry hole of that spin differs from Tangherlini by -(a/r_h)^2/2 in A_H and in kappa (exact series
     from A2), -2.9e-15 each, and rotates at Omega r_h = a/r_h = 7.6e-8.  So a theorem without symmetry would put the
     formed hole's end state within 2.9e-15 of SETTLEs's Tangherlini, for the perturbation the record computes.
  A4 (READ)
     - Hintz (2606.28253v2, p. 2, Theorem 1.1): "Let b0 = (m0, a0) be subextremal parameters. Suppose that the initial
       data gamma, k ... satisfy the constraint equations (1.3). Suppose moreover that (gamma, k) = (gamma_b0, k_b0)
       outside of a compact set, and that gamma - gamma_b0 and k - k_b0 are small in the Sobolev space H^d(Sigma) for
       some large d. Then there exist subextremal parameters b = (m, a) close to b0 such that the MGHD of (Sigma,
       gamma, k) contains a region isometric to (Omega, g), where g is a Lorentzian metric satisfying |g_mu nu - (g_b)
       _mu nu| <~ (1 + t)^(-2-eps_K)"; "This settles the Kerr stability conjecture in the full subextremal range"
       (p. 2); no symmetry is assumed, and "Restricting to axisymmetry, ultimately Schwarzschildean spacetimes, or
       small angular momenta would not lead to simplifications in our arguments" (p. 5).
     - The same, p. 6, (5): Klainerman and Szeftel "proved the nonlinear stability of the Schwarzschild spacetime in
       the class of axially symmetric and polarized spacetimes. These conditions ensure that the final black hole
       must again be a Schwarzschild black hole, though its center-of-mass may move along the symmetry axis"; (9):
       Dafermos, Holzegel, Rodnianski and Taylor "proved the codimension 3 stability of the Schwarzschild family ...
       a 'full-dimensional' subset of initial data, near those of Schwarzschild, for which the final black hole has
       vanishing angular momentum a = 0 in R^3".
     - Emparan and Reall (0801.3471v2): p. 14, (34) "M = (d - 2) Omega_(d-2) mu/(16 pi G), J = 2 M a/(d - 2)"; p. 15,
       (36)-(38), the horizon, A_H = r0^(d-4)(r0^2 + a^2) Omega_(d-2) and T_H = (1/4 pi)(2 r0/(r0^2 + a^2) + (d -
       5)/r0); p. 16, (44)-(46), and p. 17, (47), the general solution's Pi, horizon, area and kappa (odd d); p. 17,
       "In d = 5 eq. (45) admits a real root for |j1| + |j2| <= 1 ... There are no ultra-spinning regimes"; p. 20,
       "The classical linearized stability of these black holes remains largely an open problem" (2008).
  A5 (deduced) What it gives.
     - At the large end: the plane reads the formed hole as four-dimensional Schwarzschild to O((ell/r0)^2) (SETTLE
       E3), so a perturbation breaking the class's symmetry, small enough, settles to a nearby Kerr hole by Hintz's
       theorem (A4), to O((ell/r0)^2), on the footing of SETTLE: proved, the threshold not quantified, both margins
       falling with N.
     - At the small end: the end state is a nearby five-dimensional Myers-Perry hole (A1-A3), and its linear
       settling is proved, every type of perturbation decaying (O3gs: Hung, Keller and Wang's Theorem 2, READ; below
       l = 2 the mass or the Myers-Perry member).  Its nonlinear settling is the five-dimensional counterpart of
       Hintz's theorem, open in the field: theorized, named.  What the class removed returns there -- the vector type,
       the boosts' second-order pole at zero energy, the six rotations and the Myers-Perry end states, whose linear
       stability the review calls largely open -- and the route is the N1* session's route B, whose inputs already
       follow Hintz without symmetry (N1STAR-PROOF 10.29-10.36 on main at 308c527a), with [AHW24]'s rigidity beyond
       zero spin still OPEN there.
     - SETTLEs and SETTLE are unchanged: the record's solution keeps the class.  SETTLEa says the settling survives a
       perturbation that breaks it, and that for the one the record computes the end state is SETTLEs's to 2.9e-15.

What this does not claim: the five-dimensional nonlinear settling without symmetry (theorized); Myers-Perry linear
stability beyond the linearisation about Tangherlini; any end state far from Tangherlini; Hintz's threshold, which his
theorem does not quantify.

python3 settle_asym.py [--selftest | --mutants]
"""
import contextlib, importlib.util, io, os, sys
import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
D68 = os.path.dirname(HERE)
RULINGS = os.path.join(D68, "M-RULINGS-2026-10-03.md")
MUT = {}
WORDS = ((547, "Do we need the nonlinear settlings to be symmetric or asymmetric in class? And would having both be "
               "helpful and preferred?"),
         (548, "Yes, add the asymmetric settling row to the register"))


def _load(name, alias):
    spec = importlib.util.spec_from_file_location(alias, os.path.join(HERE, name))
    mod = importlib.util.module_from_spec(spec)
    with contextlib.redirect_stdout(io.StringIO()):
        spec.loader.exec_module(mod)
    return mod


def words():
    txt = " ".join(open(RULINGS, encoding="utf-8").read().split())
    return all(w in txt for _, w in WORDS)


def gen(n, i, j):
    """the rotation generator in the (i, j) plane of R^n"""
    m = sp.zeros(n, n)
    m[i, j], m[j, i] = -1, 1
    return m


def invariant_dims(n, rotations, reflections):
    """dimensions of the spin matrices (so(n)) and momenta (R^n) left invariant by the rotations (conjugation commutes)
    and the reflections (R A R = A, R P = P)"""
    basis = [gen(n, i, j) for i in range(n) for j in range(i + 1, n)]
    c = sp.symbols("c0:%d" % len(basis))
    A = sum((ci * b for ci, b in zip(c, basis)), sp.zeros(n, n))
    p = sp.Matrix(sp.symbols("p0:%d" % n))
    eqA, eqP = [], []
    for g in rotations:
        eqA += list(g * A - A * g)
        eqP += list(g * p)
    for R in reflections:
        eqA += list(R * A * R - A)
        eqP += list(R * p - p)
    def dim(eqs, xs):
        eqs = [e for e in eqs if e != 0]
        if not eqs:
            return len(xs)
        M = sp.Matrix([[sp.diff(e, x) for x in xs] for e in eqs])
        return len(xs) - M.rank()
    return dim(eqA, list(c)), dim(eqP, list(p))


def a1():
    I4 = sp.eye(4)
    R1, R2 = sp.diag(1, -1, 1, 1), sp.diag(1, 1, 1, -1)       # phi_1 -> -phi_1, phi_2 -> -phi_2
    T2 = [gen(4, 0, 1), gen(4, 2, 3)]
    refl = [R1, R2] if not MUT.get("one_reflection") else [R1]
    out = {"class": invariant_dims(4, T2, refl), "T2": invariant_dims(4, T2, []), "none": invariant_dims(4, [], [])}
    # four dimensions: the axial rotation in the (x, y) plane with phi -> -phi (Klainerman-Szeftel), and nothing
    out["4d_ks"] = invariant_dims(3, [gen(3, 0, 1)], [sp.diag(1, -1, 1)])
    out["4d_none"] = invariant_dims(3, [], [])
    # the l = 1 counts: Killing fields of S^n = so(n + 1); degree-one harmonic polynomials of R^(n + 1)
    def harm1(m):
        x = sp.symbols("x0:%d" % m)
        c = sp.symbols("h0:%d" % m)
        poly = sum(ci * xi for ci, xi in zip(c, x))
        lap = sum(sp.diff(poly, xi, 2) for xi in x)
        return m - (0 if lap == 0 else 1)
    out["l1"] = {3: (len([1 for i in range(4) for j in range(i + 1, 4)]), harm1(4)),
                 2: (len([1 for i in range(3) for j in range(i + 1, 3)]), harm1(3))}
    return out


def a2():
    r0, a, b, G = sp.symbols("r0 a b G", positive=True)
    r = sp.Symbol("r", positive=True)
    Pi = (r ** 2 + a ** 2) * (r ** 2 + b ** 2)
    mu = sp.simplify(Pi.subs(r, r0) / r0 ** 2)                 # Pi(r0) = mu r0^2
    kappa = sp.simplify(((sp.diff(Pi, r) - 2 * mu * r) / (2 * mu * r ** 2)).subs(r, r0))
    AH = sp.simplify(sp.pi ** 2 / kappa * mu * (2 - 2 * a ** 2 / (r0 ** 2 + a ** 2) - 2 * b ** 2 / (r0 ** 2 + b ** 2)))
    M = 3 * sp.pi * mu / (8 * G)
    Ja, Jb = 2 * M * a / 3, 2 * M * b / 3
    f = sp.Rational(1, 2) if MUT.get("half_omega") else 1
    Oa, Ob = f * a / (r0 ** 2 + a ** 2), f * b / (r0 ** 2 + b ** 2)
    first = [sp.simplify(sp.diff(M, x) - kappa * sp.diff(AH, x) / (8 * sp.pi * G) - Oa * sp.diff(Ja, x)
                         - Ob * sp.diff(Jb, x)) for x in (r0, a, b)]
    single = sp.simplify(kappa.subs(b, 0) - r0 / (r0 ** 2 + a ** 2))
    tang = (sp.simplify(kappa.subs({a: 0, b: 0}) - 1 / r0),
            sp.simplify(AH.subs({a: 0, b: 0}) - 2 * sp.pi ** 2 * r0 ** 3))
    return dict(first=first, single=single, tang=tang, kappa=kappa, AH=AH, mu=mu)


def a3():
    sc = _load("scope.py", "sa_scope")
    x = sc.uniqueness()["a_over_r"]
    # at fixed mass (mu = 1, r_h = 1): b = 0, r0^2 = mu - a^2, A_H = 2 pi^2 mu r0, kappa = r0/mu
    a = sp.Symbol("a", positive=True)
    r0 = sp.sqrt(1 - a ** 2)
    dA = sp.series(2 * sp.pi ** 2 * r0 / (2 * sp.pi ** 2) - 1, a, 0, 4).removeO()
    dk = sp.series(r0 - 1, a, 0, 4).removeO()
    lead = (sp.simplify(dA + a ** 2 / 2), sp.simplify(dk + a ** 2 / 2))
    return dict(x=x, lead=lead, dA=float(-x ** 2 / 2), Om=x)


def compute():
    return dict(words=words(), a1=a1(), a2=a2(), a3=a3())


def checks(o):
    e, m, t = o["a1"], o["a2"], o["a3"]
    return {"A0": o["words"],
            "A1": e["class"] == (0, 0) and e["T2"] == (2, 0) and e["none"] == (6, 4) and e["4d_ks"] == (0, 1)
                  and e["4d_none"] == (3, 3) and e["l1"] == {3: (6, 4), 2: (3, 3)},
            "A2": all(f == 0 for f in m["first"]) and m["single"] == 0 and m["tang"] == (0, 0),
            "A3": t["lead"] == (0, 0) and "%.2g" % t["x"] == "7.6e-08" and "%.2g" % t["dA"] == "-2.9e-15"}


def report(o=None):
    o = o or compute(); ck = checks(o)
    e, m, t = o["a1"], o["a2"], o["a3"]
    print("A0 M's words (547, 548):", o["words"])
    print("A1 (spins, momenta) invariant: the class %s; T^2 alone %s; no symmetry %s; four dimensions, axial with "
          "phi -> -phi %s, none %s; l = 1 (Killing, scalar) on S^3 %s, on S^2 %s"
          % (e["class"], e["T2"], e["none"], e["4d_ks"], e["4d_none"], e["l1"][3], e["l1"][2]))
    print("A2 Myers-Perry, d = 5: first law residuals %s; single spin kappa = r0/(r0^2 + a^2): %s; Tangherlini %s"
          % (m["first"], m["single"] == 0, m["tang"]))
    print("A3 the inflow's spin a/r_h = %.2g (scope C1): at fixed mass dA/A = dkappa/kappa = %.2g, Omega r_h = %.2g; "
          "series exact: %s" % (t["x"], t["dA"], t["Om"], t["lead"]))
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


MUTANTS = {"one_reflection": "the class with one reflection only (A1)",
           "half_omega": "the horizon angular velocities halved (A2)"}


def mutants():
    caught = 0
    for m, what in MUTANTS.items():
        MUT.clear(); MUT[m] = True
        try:
            ok = selftest(quiet=True)
        except Exception:
            ok = False
        caught += not ok
        print("mutant %-14s %s  (%s)" % (m, "caught" if not ok else "MISSED", what))
    MUT.clear()
    print("%d/%d caught" % (caught, len(MUTANTS)))
    return caught == len(MUTANTS)


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    if "--mutants" in sys.argv:
        sys.exit(0 if mutants() else 1)
    report()
