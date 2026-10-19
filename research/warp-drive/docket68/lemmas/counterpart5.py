#!/usr/bin/env python3
"""counterpart5.py -- item 520: finishing the counterpart proof (THM-HF5, the five-dimensional counterpart of Huneau
and Luk's theorem) -- what it takes, measured exactly; two of 517's claims corrected.

M, 520: "Can you finish the counterpart proof?"  The board's reading: THM-HF5 (511), which 497-498 named "the 5D
counterpart of Huneau and Luk's nonlinear theorem"; its one open lemma L-UNIF', narrowed at 517-519 to the seed
phase, the second order and N1's energy method.  Labels: computed (exact unless marked), READ (verbatim at source,
2026-10-19), deduced, OPEN (a named lemma not proved), M's.

  P0 (M's) 520, verbatim.
  P1 (computed, exact; the scan on kn_gauge's cached core) Which theorem the open points belong to.  THM-HF5 is a
     statement as lam -> 0 at fixed mu0, A and env.  The Kretschmann scalar of five-dimensional Tangherlini is
     72 mu^2/r^8 (computed from the metric), so a wave of length lam is shorter than a tenth of the curvature radius
     K^(-1/4) exactly where z^2 > 10 72^(1/4) lam/sqrt(mu), z = r/sqrt(mu).  On D, where x = l5^2 sqrt(K) <= 1, the
     curvature radius is at least l5: every wave with lam < l5/10 is high-frequency on all of D.  The seed phase (the
     high-frequency edge beyond z = 1.2) needs lam > 1.44 sqrt(mu0)/(10 72^(1/4)), which is 0.144 l5 at the least seed.
     Over the record's shell, with the exponents 517 computed (against the test-field energy):
     - the crude exponent is 1.384e4 at every wavelength -- lam-independent;
     - the seed phase holds 7.7e-6 of the energy at 10 l5, 5.4e-9 at 0.3 l5, and none at 0.1 l5;
     - the "second order" stays near 0.21 from 10 l5 to 0.3 l5 -- the seed phase's edge dominates it, so 517's
       "estimate 0.21, second order" was not a property of small lam -- and falls in proportion to lam once the seed
       phase is gone: 0.148 at 0.1 l5, 0.0148 at 0.01 l5.
     So the seed phase and the 0.21 belong to the anchored wavelength (the application at 10 l5), not to the lam -> 0
     theorem; in that theorem every Gronwall constant is lam-independent, and a crude estimate suffices -- if the
     estimate exists at all (P5's N1*).
  P2 (computed, exact) N1 in the KN gauge -- 517's K6 withdrawn.  For the torus-frame metric in the KN gauge
     (h_rr = h_rth = 0, h_thth = r^6 s^2 c^2) with every function general: h^vv = h^vth = 0 exactly, so no second
     v-derivative of anything reaches the equations -- the high-frequency structure is right.  But the hypersurface
     equations form Bondi's hierarchy: rr fixes h_vr from (d_r psi)^2 and (d_r omega)^2; r-theta fixes h_vth through
     d_theta h_vr; theta-theta fixes h_vv through d_theta^2 h_vr and d_r d_theta h_vth.  And h_vv sits in h^rr, the
     coefficient of d_r^2 in box_h.  An energy estimate with k angular derivatives needs k + 2 of them: two angular
     derivatives are lost.  The torus frame removes the D D U terms but not this; Bondi-like gauges are "only weakly
     hyperbolic" (Giannakopoulos, Hilditch and Zilhao 2020, READ at 511), in this class too.
  P3 (computed, exact) N2's scope -- 517's K5 corrected.  On the background, box_h psi0 = box_h omega0 = 0
     (psi0 = ln(r^2 s c), omega0 = (1/2) ln(c/s)).  Their linearizations in the base metric do not vanish:
     d(box_h) psi0 holds h_vv and d_r h_vv, d(box_h) omega0 holds d_theta h_vr and d_r h_vth, with O(1) coefficients.
     So the remainder of the Killing norms is driven by the base metric's remainder at O(1).  The class's linear
     problem is linearized gravity in the T^2-mirror class (515, item 2: open on a growing hole), not the test-field
     wave equation.  K5's multiplier and constant 35 stand -- for T^2-invariant test fields; K8's absorption ratio
     0.92 and exponents are measured against that test-field energy.
  P4 (READ, 2026-10-19) Prior art for the remaining step.
     - Touati, Commun. Math. Phys. 402, 3109 (2023), arXiv:2206.12318, Theorem 2.2: on [0, 1] x R^3, with the
       background assumed "close to Minkowski" ((2.9): ||g0 - m|| <= eps) and "There exists lambda0 > 0 and
       eps0 = eps0(delta, R) > 0 such that if 0 < eps <= eps0, there exists for all lambda in (0, lambda0] a
       solution"; "their coupling induces a loss of derivatives", regained "by a null foliation associated to g0 as
       well as a Fourier cut-off".  Its energy estimate (3.38) is exp(int ||dg||_Loo): "we need ||dg||_Loo to be
       bounded uniformly in the high-frequency limit".
     - Touati, arXiv:2402.17530 (Ann. PDE 2025), Theorem 1.3: the same smallness ((1.15), "close to Minkowski").
     - Huneau and Luk, Duke Math. J. 167 (2018): polarized U(1), small data, elliptic gauge.  Luk and Rodnianski,
       arXiv:2009.08968: 3+1, double null, local.
     None treats a large background, five dimensions, or fixed points of the symmetry (the T^2 axes).
  P5 (deduced) What finishing takes.  The counterpart of Huneau-Luk and Touati is THM-HF5 on D_T = D with
     v <= v_end + T, for each fixed T (their theorems are on a fixed time interval).  In hand: the limit and part (iv)
     (511, exact); v null at every lam with no second v-derivative anywhere (F5, P2); every constant lam-independent
     and no seed phase below 0.144 l5 (P1).  OPEN, named N1*: for lam <= lam0, existence on D_T of the vacuum solution
     with the record's data and lam-uniform energy estimates for its remainder, in a formulation without derivative
     loss and regular across the axes -- five-dimensional generalised wave gauge (Touati's route) or double null
     (Luk and Rodnianski's) -- for the large background g0 (five-dimensional Vaidya with its interior to x = 1).  No
     published theorem gives it (P4), and a proof is of the size of [Tou23a].  Beyond D_T, the settling after the
     shell is the nonlinear stability of five-dimensional Tangherlini in the class (open: 515).  The application at
     10 l5 additionally needs linearized-gravity control in the class over the shell (P3) and closes the seed phase
     and the 0.21 there.  No inner or Cauchy horizon enters (519): D ends at the spacelike x = 1.

Imports kn_gauge.py (its cached core) and hf_theorem5.py's statement by path.  numpy, sympy.
python3 counterpart5.py [--selftest | --mutants]
"""
import contextlib
import importlib.util
import io
import os
import sys

import numpy as np
import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
RULINGS = os.path.join(HERE, "..", "M-RULINGS-2026-10-03.md")
MUT = set()
MUTANTS = {"k48": "the Kretschmann scalar 48 mu^2/r^8 in place of 72 (P1)",
           "w_fixed": "the scan holds the wavelength at 10 l5 whatever is asked (P1)",
           "rr_for_thth": "h_vv's equation read from rr in place of theta-theta (P2)",
           "constant_scalars": "the background Killing norms taken constant (P3)"}


def _load(name, key):
    spec = importlib.util.spec_from_file_location(key, os.path.join(HERE, name))
    mod = importlib.util.module_from_spec(spec)
    with contextlib.redirect_stdout(io.StringIO()):
        spec.loader.exec_module(mod)
    return mod


def words():
    s = open(RULINGS).read()
    return '"Can you finish the counterpart proof?"' in s and "520. **Finish the counterpart proof" in s


def kretschmann():
    """K of five-dimensional Tangherlini, from the metric"""
    t, r, th, p1, p2, mu = sp.symbols("t r theta phi1 phi2 mu", positive=True)
    X = [t, r, th, p1, p2]
    F = 1 - mu/r**2
    g = sp.diag(-F, 1/F, r**2, r**2*sp.sin(th)**2, r**2*sp.cos(th)**2)
    gi = g.inv(); n = 5
    G = [[[sp.simplify(sum(gi[a, d]*(sp.diff(g[d, b], X[c]) + sp.diff(g[d, c], X[b]) - sp.diff(g[b, c], X[d]))
                           for d in range(n))/2) for c in range(n)] for b in range(n)] for a in range(n)]
    Rm = {}
    for a in range(n):
        for b in range(n):
            for c in range(n):
                for d in range(c + 1, n):
                    e = sp.diff(G[a][b][d], X[c]) - sp.diff(G[a][b][c], X[d]) + sum(
                        G[a][c][k]*G[k][b][d] - G[a][d][k]*G[k][b][c] for k in range(n))
                    e = sp.simplify(e)
                    if e != 0:
                        Rm[(a, b, c, d)] = e
    K = 0
    for (a, b, c, d), e in Rm.items():           # R^a_bcd R_a^bcd, diagonal metric, c < d counted twice
        K += 2*e**2*g[a, a]/g[b, b]/(g[c, c]*g[d, d])
    K = sp.simplify(sp.fu(sp.simplify(K*r**8/mu**2)))*mu**2/r**8      # fu: the trigonometric reduction to a constant
    if "k48" in MUT:
        K = K*sp.Rational(48, 72)
    return K, (r, mu)


def p1():
    """the regime boundary, exactly, and the record's shell scanned in the wavelength"""
    K, (r, mu) = kretschmann()
    lam, z = sp.symbols("lam z", positive=True)
    zhf2 = sp.solve(sp.Eq(lam, (1/K)**sp.Rational(1, 4)/10).subs(r, z*sp.sqrt(mu)), z)
    zhf2 = sp.simplify(zhf2[0]**2) if zhf2 else None
    out = dict(K=sp.simplify(K*r**8/mu**2), zhf2=zhf2)
    c4 = 72**0.25
    out["w_seed_least"] = 1.44*c4/(10*c4)                        # seed phase needs z_hf(mu0) > 1.2; sqrt(mu0) = 72^(1/4) l5
    KN = _load("kn_gauge.py", "cp_kn_gauge")
    KN.k8()
    scan = {}
    for w in (10.0, 1.0, 0.3, 0.1, 0.01):
        o = KN._k8_shell(KN._K8CORE, 10.0 if "w_fixed" in MUT else w)
        scan[w] = dict(crude=o["crude_all"], late=o["late"], seed_E=o["seed_energy"], seed_s=o["seed_s"],
                       ratio=o["ratio"])
    out["scan"] = scan
    return out


def _kn_metric():
    v, r, th = sp.symbols("v r theta", positive=True)
    s, c = sp.sin(th), sp.cos(th)
    A, B, C, psi, om = [sp.Function(n)(v, r, th) for n in ("A", "B", "C", "psi", "om")]
    h = sp.Matrix([[A, B, C], [B, 0, 0], [C, 0, r**6*s**2*c**2]])
    return h, (v, r, th), (A, B, C, psi, om)


def p2():
    """the KN gauge's hypersurface hierarchy: which derivatives each equation holds; the inverse metric"""
    h, X, (A, B, C, psi, om) = _kn_metric()
    hi = sp.simplify(h.inv())
    n = 3
    G = [[[sp.simplify(sum(hi[i, d]*(sp.diff(h[d, j], X[k]) + sp.diff(h[d, k], X[j]) - sp.diff(h[j, k], X[d]))
                           for d in range(n))/2) for k in range(n)] for j in range(n)] for i in range(n)]

    def ric(j, k):
        e = 0
        for i in range(n):
            e += sp.diff(G[i][j][k], X[i]) - sp.diff(G[i][j][i], X[k])
            for d in range(n):
                e += G[i][i][d]*G[d][j][k] - G[i][k][d]*G[d][j][i]
        src = sp.Rational(3, 2)*sp.diff(psi, X[j])*sp.diff(psi, X[k]) + 2*sp.diff(om, X[j])*sp.diff(om, X[k])
        return sp.expand(sp.numer(sp.together(e - src)))

    def ders(e):
        out = set()
        for d in e.atoms(sp.Derivative):
            cnt = {str(x): k for x, k in d.variable_count}
            out.add((d.expr.func.__name__, cnt.get("v", 0), cnt.get("r", 0), cnt.get("theta", 0)))
        return out
    eqs = {"rr": ders(ric(1, 1)), "rth": ders(ric(1, 2)), "thth": ders(ric(2, 2))}
    if "rr_for_thth" in MUT:
        eqs["thth"] = eqs["rr"]
    # angular order of each metric function beyond the energy level (the scalars' first derivatives): each function is
    # integrated in r from its equation, so its order is the largest order of what else that equation holds -- a metric
    # function's own order plus its theta-derivatives, a scalar's derivative count less the one the energy controls
    order = {}

    def level(d):
        if d[0] in ("psi", "om"):
            return max(d[1] + d[2] + d[3] - 1, 0)
        return order[d[0]] + d[3]

    def ordof(eq, f):
        return max([level(d) for d in eqs[eq] if d[0] != f] or [0])
    order["B"] = ordof("rr", "B")
    order["C"] = ordof("rth", "C")
    order["A"] = ordof("thth", "A")
    inv = dict(vv=sp.simplify(hi[0, 0]), vth=sp.simplify(hi[0, 2]), rr=sp.simplify(hi[1, 1]))
    return dict(eqs=eqs, order=order, inv=inv,
                A_in_hrr=inv["rr"].has(A), loss=order["A"])


def p3():
    """the background Killing norms' wave operator, linearized in the base metric (KN gauge)"""
    v, r, th, mu, e = sp.symbols("v r theta mu e", positive=True)
    X = [v, r, th]; s, c = sp.sin(th), sp.cos(th)
    rho = r**2*s*c; F = 1 - mu/r**2
    a, b, cc = [sp.Function(n)(v, r, th) for n in ("a", "b", "cc")]
    h = rho**2*sp.Matrix([[-F, 1, 0], [1, 0, 0], [0, 0, r**2]]) + e*sp.Matrix([[a, b, cc], [b, 0, 0], [cc, 0, 0]])

    def box(f):
        hi = h.inv()
        sq = r**7*s**3*c**3*sp.sqrt(sp.expand(-h.det()/(r**14*s**6*c**6)))
        return sum(sp.diff(sq*hi[i, j]*sp.diff(f, X[j]), X[i]) for i in range(3) for j in range(3))/sq
    psi0, om0 = sp.log(rho), sp.log(c/s)/2
    if "constant_scalars" in MUT:
        psi0, om0 = sp.Integer(1), sp.Integer(2)
    out = {}
    for name, f in (("psi", psi0), ("om", om0)):
        bx = box(f)
        out[name + "_bg"] = sp.simplify(bx.subs(e, 0))
        L = sp.factor(sp.simplify(sp.diff(bx, e).subs(e, 0)))
        out[name + "_lin"] = L
        out[name + "_terms"] = sorted({(d.expr.func.__name__, tuple(str(x) for x, k in d.variable_count for _ in range(k)))
                                       for d in L.atoms(sp.Derivative)} |
                                      {(fn.func.__name__, ()) for fn in L.atoms(sp.Function) if fn.func in (a.func, b.func, cc.func)})
    return out


def thm_text():
    s = open(os.path.join(HERE, "hf_theorem5.py")).read()
    return "(i)   g_lam exists on D for every lam <= lam0;" in s and "F7 OPEN, named, narrowed by F5: L-UNIF'." in s


def compute():
    return dict(words=words(), p1=p1(), p2=p2(), p3=p3(), thm=thm_text())


def checks(o):
    ch = {}
    ch["P0 words of 520"] = o["words"]
    q = o["p1"]; sc = q["scan"]
    ch["P1 K = 72 mu^2/r^8 (computed); high-frequency where z^2 > 10 72^(1/4) lam/sqrt(mu); all of D for lam < l5/10"] = (
        q["K"] == 72 and q["zhf2"] is not None and sp.simplify(q["zhf2"] - 10*72**sp.Rational(1, 4)*sp.Symbol("lam", positive=True)
                                                             / sp.sqrt(sp.Symbol("mu", positive=True))) == 0)
    ch["P1 seed phase only above 0.144 l5 (least seed): 7.7e-6 of the energy at 10 l5, none at 0.1 l5"] = (
        abs(q["w_seed_least"] - 0.144) < 1e-12 and abs(sc[10.0]["seed_E"] - 7.73e-6) < 0.05e-6
        and sc[0.1]["seed_E"] == 0 and sc[0.01]["seed_E"] == 0 and sc[0.3]["seed_E"] > 0)
    ch["P1 crude exponent lam-independent (1.384e4); the 0.21 held by the seed phase's edge, then ~ lam (0.148, 0.0148)"] = (
        max(abs(sc[w]["crude"] / sc[10.0]["crude"] - 1) for w in sc) < 1e-9 and abs(sc[10.0]["crude"] - 1.384e4) < 10
        and abs(sc[1.0]["late"] - sc[10.0]["late"]) < 0.01 and abs(sc[0.1]["late"] / sc[0.01]["late"] - 10) < 0.01
        and 0.14 < sc[0.1]["late"] < 0.155)
    p = o["p2"]
    ch["P2 KN gauge: h^vv = h^vth = 0 (no second v-derivative anywhere); h_vv in h^rr, box_h's d_r^2 coefficient"] = (
        p["inv"]["vv"] == 0 and p["inv"]["vth"] == 0 and p["A_in_hrr"])
    ch["P2 hierarchy rr -> h_vr, r-theta -> h_vth (d_theta h_vr), theta-theta -> h_vv (d_theta^2 h_vr): 2 derivatives lost"] = (
        p["order"]["B"] == 0 and p["order"]["C"] == 1 and p["order"]["A"] == 2 and p["loss"] == 2
        and ("B", 0, 0, 2) in p["eqs"]["thth"] and ("C", 0, 1, 1) in p["eqs"]["thth"] and ("A", 0, 1, 0) in p["eqs"]["thth"])
    c = o["p3"]
    to = set(c["om_terms"])
    ch["P3 box_h psi0 = box_h omega0 = 0, and their linearizations hold h_vv, d_r h_vv (psi), d_th h_vr, d_r h_vth (omega)"] = (
        c["psi_bg"] == 0 and c["om_bg"] == 0 and c["psi_lin"] != 0 and c["om_lin"] != 0
        and ("a", ()) in c["psi_terms"] and ("a", ("r",)) in c["psi_terms"]
        and ("b", ("theta",)) in to and ("cc", ("r",)) in to)
    ch["P5 THM-HF5's part (i) and F7 as 511 states them"] = o["thm"]
    return ch


def report(o=None):
    o = o or compute()
    for k_, v_ in checks(o).items():
        print("%-118s %s" % (k_[:118], "PASS" if v_ else "FAIL"))
    q = o["p1"]
    print("  P1 K r^8/mu^2 = %s; z_hf^2 = %s; seed phase needs lam > %.3f l5 at the least seed" % (q["K"], q["zhf2"], q["w_seed_least"]))
    for w, d in q["scan"].items():
        print("     lam %5.2f l5: crude %.4e  'second order' %.4e  seed share %.3e (to s = %.4f)  absorbed ratio %.4f"
              % (w, d["crude"], d["late"], d["seed_E"], d["seed_s"], d["ratio"]))
    p = o["p2"]
    print("  P2 orders (theta-derivatives beyond the scalars' cone derivatives): %s; h^rr = %s" % (p["order"], p["inv"]["rr"]))
    for k_ in ("rr", "rth", "thth"):
        print("     %-4s holds %s" % (k_, sorted(p["eqs"][k_])))
    c = o["p3"]
    print("  P3 d(box) psi0 holds %s" % c["psi_terms"])
    print("     d(box) omega0 = %s" % c["om_lin"])


def selftest():
    c = checks(compute())
    n = sum(c.values())
    for k_, v_ in c.items():
        print("%-118s %s" % (k_[:118], "PASS" if v_ else "FAIL"))
    print("counterpart5.py: %d/%d" % (n, len(c)))
    return n == len(c)


def mutants():
    caught = 0
    for m_, desc in MUTANTS.items():
        MUT.clear(); MUT.add(m_)
        try:
            c = checks(compute()); failed = [k[:44] for k, v in c.items() if not v]
        except Exception as ex:                                  # noqa: BLE001
            failed = ["raised %s" % type(ex).__name__]
        caught += bool(failed)
        print("mutant %-18s %s  (%s)  failing: %s" % (m_, "caught" if failed else "MISSED", desc, "; ".join(failed)))
    MUT.clear()
    print("mutants: %d/%d" % (caught, len(MUTANTS)))
    return caught == len(MUTANTS)


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    if "--mutants" in sys.argv:
        sys.exit(0 if mutants() else 1)
    report()
