#!/usr/bin/env python3
"""collapse_bulk.py -- item 466 (b): the collapse in the bulk.  M (466): "Yes continue please" -- the collapse in the
bulk approved (414 met) -- "AND ... an expectation is not proof. We must compute the large end."  So each hypothesis
of the theorems used is computed here, the theorems are READ, and where a theorem does not reach, that is said.
Labels: READ (verbatim, with the source), computed (sympy, exact unless marked), deduced.  Worked in the
conversation; not verified; not seated.  2026-10-17.

The question.  Inside the corridor's hole, can the bulk's collapse be avoided -- by a bounce, classically or
semiclassically -- at any size?  P3 computes one size (p3_double_null.py D7: the curvature diverges where r- would
stand, bt = 2) and p3_large_end.py the ladder toward the large end.  This instrument asks what holds at every size.

  C0 (READ) M's words, verbatim in the rulings file, and the sources below.
  C1 (computed, exact) The bulk keeps null energy.  Schwarzschild-AdS5 satisfies R_ab = -4 g_ab for every mass, so
     R(k, k) = -4 g(k, k) = 0 for every null k: Lambda_5 adds no focusing and takes none away.  Its Kretschmann
     scalar is 40 + 72 mu^2/r^8: AdS's 40 at large r, divergent at r = 0.
  C2 (computed, exact) The plane's focusing share.  Inverting Israel's condition in D = 5 gives the plane's singular
     Ricci, and for every null k crossing it R_sing(k, k) = 8 pi G5 delta(n) S(k, k) -- the normal terms cancel
     because g(k, k) = 0.  P3's plane rows (p3m.israel_rows: K^t_t = K^r_r = 1 - q, K^th_th = 1 + q, q = kappa/R^4,
     ell = 1) give S^a_b = -sigma delta^a_b + tau^a_b with sigma = 3/(4 pi G5) and tau = diag(-rho, -rho, rho, rho),
     rho = q/(4 pi G5) >= 0: the magnetic field's stress.  Then
         S(k, k) = (sigma + rho) (k^n)^2 + 2 rho ((k^th)^2 + (k^ph)^2),
     a sum of non-negative terms.  The plane focuses every null ray that crosses it.
  C3 (computed, exact) The jump, on an exact plane.  On Randall-Sundrum's doubled Poincare AdS5 (z = ell + |y|),
     the jump of K across the plane gives S = -sigma h, sigma = 3/(4 pi G5 ell); a planar null congruence crossing it
     has theta = 3 c/ell before and -3 c/ell after, so [theta] = -6 c/ell = -8 pi G5 S(k, k)/|k^n|, for every c.
  C4 (computed, imported) A smooth wall keeps null energy at every point (b5b_wall.py W1-W5, its selftest run here),
     and its metric is smooth (A = -b ln cosh(y/w), every derivative finite at y = 0), where the thin plane's is
     only Lipschitz ([A'] = -2/ell).
  C5 (computed) Closed trapped surfaces exist in the computed hole.  On P3's start slices (bt = 2, s0 = -0.05 and
     -0.15) the surface {tau, t fixed}, chi from the axis to the plane, is a closed 3-surface in the doubled bulk (the
     S^2 shrinks at both axis ends: an S^3).  In P3's conformal gauge its null normals are e^{-S+A/2} d_tau +- e^{-A} d_t
     and both expansions equal e^{-S+A/2} d_tau(S - 3A/2 + 2 ln r).  That is negative at every chi:
     at s0 = -0.05 it lies in [-0.44, -0.14], at s0 = -0.15 in [-0.89, -0.24].  The expansion takes only d_tau of the
     metric, tangent to the plane, which is continuous across it, so the surface stays trapped in a smooth wall
     thin enough (deduced).
  C6 (computed) Focusing in D = 5.  With R(k, k) >= 0 (C1, C4) Raychaudhuri gives theta <= 3 theta0/(3 + theta0 lam),
     so every null normal of C5's surface reaches a focal point within lam = 3/|theta0| <= 20.8 ell of affine
     parameter, if it extends that far.  A thin plane only lowers theta (C2, C3: [theta] <= 0).
  C7 (deduced) Penrose's theorem, as READ (Kunzinger, Steinbauer and Vickers, Thm 1.1, n dimensions, C^{1,1}):
     (i) Ric(X, X) >= 0 for null X -- C1 and C4; (ii) a non-compact Cauchy hypersurface -- assumed, as the theorem
     assumes it (far out the doubled bulk is Randall-Sundrum's, conformal to a region of flat space whose t-slices
     are Cauchy and non-compact; B4b' reads the splitting with boundary); (iii) a closed trapped surface -- C5.
     So the smooth-wall spacetime is not future null complete.  The incomplete null geodesic leaves C5's surface,
     inside the Killing horizon s = 0, which future causal curves cross only inward: the incompleteness is inside
     the hole.  The theorem does not say how: a curvature singularity or a Cauchy horizon.  P3 computes which -- the
     curvature diverges where r- would stand (p3_double_null D7, bt = 2; p3_large_end for the ladder).
     The thin plane itself is NOT covered: its metric is Lipschitz (C4), and for Lipschitz metrics Penrose's theorem
     is open (READ, Calisti, Graf, Hafemann, Kunzinger and Steinbauer 2025: "all issues we reserve for future
     research").  The smooth wall is the route, and the thin plane its limit (b5b_wall W4, W5).
  C8 (computed, exact) An exact collapse in AdS5, the null dust of a delivery: Vaidya-AdS5,
     f = 1 + r^2 - mu(v)/r^2.  R_ab + 4 g_ab = (3 mu'/(2 r^3)) l_a l_b with l = dv, so null energy holds iff
     mu' >= 0; the 3-spheres are trapped where f < 0 (theta_in = -3/r, theta_out = 3 f/(2 r)); and the Kretschmann
     scalar's mu-part is 72 mu^2/r^8 at every v: the collapse ends at r = 0 in a curvature singularity.
  C9 (READ + deduced) The plane, semiclassically.  Bousso (PRL 135, 011501, 2025): "Our result excludes 'bounces' or
     any other form of singularity avoidance inside black holes, so long as the semiclassical regime remains valid
     through the bounce", and for brane worlds the GSL it rests on "can be explicitly proven through a classical bulk
     computation that is exact in N"; Shahbazi-Moghaddam (arXiv:2212.03881) proves it "Subject to a technical
     assumption" on "brane-world semiclassical gravity theories which are holographically dual to Einstein gravity in
     a higher dimensional anti-de Sitter spacetime" -- this bulk's theory.  So on the plane, a bounce inside the hole
     is excluded so long as the semiclassical regime holds through it.  Bearing on 273: an information-carrying
     bounce is excluded in semiclassical gravity (Bousso, note 14); a bounce in the full quantum regime, beyond the
     semiclassical, is not addressed by the theorem.  A finding, offered to M; not a ruling.
What this does not prove.
  - That the thin plane's spacetime is null incomplete by a theorem (C7: open for Lipschitz metrics).
  - Hypothesis (ii) for the hole's own spacetime: it is assumed, as Penrose assumes it.
  - That the incompleteness is a curvature singularity at every size: that is P3's computation, size by size.
  - Anything in the full quantum regime (C9).

python3 collapse_bulk.py [--selftest | --mutants]
"""
import importlib.util
import os
import subprocess
import sys

import numpy as np
import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
D68 = os.path.dirname(HERE)
RULINGS = os.path.join(D68, "M-RULINGS-2026-10-03.md")
DN = os.path.join(HERE, "p3_work", "dn")
MUT = set()
WORDS = ("Yes continue please",
         "an expectation is not proof. We must compute the large end.")

# C0: key -> (identifier, the line read, verbatim)
SOURCES = {
    "KSV": ("Kunzinger, Steinbauer and Vickers, The Penrose singularity theorem in regularity C^{1,1}, "
            "arXiv:1502.00287, Theorem 1.1",
            "Let (M, g) be an n-dimensional C1,1-spacetime. Assume (i) For any Lipschitz-continuous local null vector "
            "field X, Ric(X, X) >= 0. (ii) M possesses a non-compact Cauchy-hypersurface S. (iii) There exists a "
            "compact achronal spacelike submanifold T in M of codimension 2 with past-pointing timelike mean curvature "
            "vector field H. Then M is not future null complete."),
    "CGHKS": ("Calisti, Graf, Hafemann, Kunzinger and Steinbauer, Hawking's singularity theorem for Lipschitz "
              "Lorentzian metrics, arXiv:2501.18450 (Commun. Math. Phys. 2025), introduction",
              "In the Penrose case, where one is concerned with null geodesics emanating from a trapped surface, one "
              "would have to replace the usual focusing estimates by a null version of the segment-type inequality. "
              "... all issues we reserve for future research."),
    "CGHKS-shells": ("ibid.",
                     "thin shells and many matched spacetimes ... which all exhibit a delta-function like curvature "
                     "concentrated on a hypersurface. This is precisely the regularity class we deal with in this work"),
    "Bousso": ("Bousso, PRL 135, 011501 (2025)",
               "Our result excludes 'bounces' or any other form of singularity avoidance inside black holes, so long "
               "as the semiclassical regime remains valid through the bounce"),
    "Bousso-brane": ("ibid.",
                     "A concrete example is the brane world scenario ... a version of the QFC, and hence the Bousso "
                     "bound and GSL, can be explicitly proven through a classical bulk computation that is exact in N"),
    "Bousso-14": ("ibid., note 14",
                  "causal structure would have to be preserved in order to transmit information through a bounce ... "
                  "But then the GSL is applicable across the bounce and the contradiction established in our theorem "
                  "still excludes the bounce"),
    "SM": ("Shahbazi-Moghaddam, arXiv:2212.03881",
           "Subject to a technical assumption, I prove this conjecture on brane-world semiclassical gravity theories "
           "which are holographically dual to Einstein gravity in a higher dimensional anti-de Sitter spacetime."),
    "WC": ("Wang and Choptuik, arXiv:1604.04832",
           "the evolutions of sufficiently strong initial configurations of the scalar field result in black holes "
           "that have finite extension into the bulk ... consistent with those previously computed from a static "
           "vacuum ansatz."),
    "Stein": ("Stein, JHEP09(2016)067",
              "We numerically construct large Randall-Sundrum II brane black holes ... good agreement down to a "
              "horizon radius of about r_H ~ 30 ell."),
}


def _load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


# ---------------------------------------------------------------------------- geometry
def curvature(g, X):
    """Christoffels, Riemann R^a_bcd, Ricci and the Kretschmann scalar of a metric g in coordinates X"""
    n = len(X)
    gi = sp.simplify(g.inv())
    Gam = [[[sp.simplify(sum(gi[a, e] * (sp.diff(g[e, b], X[c]) + sp.diff(g[e, c], X[b]) - sp.diff(g[b, c], X[e]))
                             for e in range(n)) / 2) for c in range(n)] for b in range(n)] for a in range(n)]
    Rm = {}
    for a in range(n):
        for b in range(n):
            for c in range(n):
                for d in range(c + 1, n):
                    v = (sp.diff(Gam[a][b][d], X[c]) - sp.diff(Gam[a][b][c], X[d])
                         + sum(Gam[a][c][e] * Gam[e][b][d] - Gam[a][d][e] * Gam[e][b][c] for e in range(n)))
                    v = sp.simplify(v)
                    Rm[a, b, c, d], Rm[a, b, d, c] = v, -v
    for a in range(n):
        for b in range(n):
            for c in range(n):
                Rm[a, b, c, c] = 0
    Ric = sp.Matrix(n, n, lambda b, d: sp.simplify(sum(Rm[a, b, a, d] for a in range(n))))
    low = {(a, b, c, d): sum(g[a, e] * Rm[e, b, c, d] for e in range(n))
           for a in range(n) for b in range(n) for c in range(n) for d in range(n)}
    up = {(a, b, c, d): sum(gi[b, f] * gi[c, h] * gi[d, k] * Rm[a, f, h, k]
                            for f in range(n) for h in range(n) for k in range(n))
          for a in range(n) for b in range(n) for c in range(n) for d in range(n)}
    K = sp.simplify(sum(low[i] * up[i] for i in low))
    return Ric, K


def c1_bulk():
    """Schwarzschild-AdS5: R_ab = -4 g_ab, R(k, k) = 0 for null k, Kretschmann 40 + 72 mu^2/r^8"""
    t, r, a, b, c = sp.symbols("t r a b c", real=True)
    mu = sp.Symbol("mu", positive=True)
    f = 1 + r**2 - mu / r**2
    g = sp.diag(-f, 1 / f, r**2, r**2 * sp.sin(a)**2, r**2 * sp.sin(a)**2 * sp.sin(b)**2)
    if "lam_off" in MUT:
        g = sp.diag(-(1 - mu / r**2), 1 / (1 - mu / r**2), r**2, r**2 * sp.sin(a)**2, r**2 * sp.sin(a)**2 * sp.sin(b)**2)
    Ric, K = curvature(g, [t, r, a, b, c])
    einstein = all(sp.simplify(e) == 0 for e in (Ric + 4 * g))
    k = sp.symbols("k0:5", real=True)
    kv = sp.Matrix(k)
    nul = sp.solve((kv.T * g * kv)[0], k[0])[0]
    Rkk = sp.simplify((kv.T * Ric * kv)[0].subs(k[0], nul))
    kret = sp.simplify(K - 40 - 72 * mu**2 / r**8) == 0
    return dict(einstein=einstein, Rkk=Rkk, kret=kret, K=K)


def c2_plane():
    """the singular Ricci of a thin plane in D = 5, and S(k, k) from P3's rows"""
    G = sp.Symbol("G5", positive=True)
    eta = sp.diag(-1, 1, 1, 1)
    Ssym = sp.Matrix(4, 4, lambda i, j: sp.Symbol("S%d%d" % (min(i, j), max(i, j))))
    Kj = sp.Matrix(4, 4, lambda i, j: sp.Symbol("K%d%d" % (min(i, j), max(i, j))))
    trK = sum(eta[i, i] * Kj[i, i] for i in range(4))
    # Israel: -[K_ab] + h_ab [K] = 8 pi G S_ab, solved for [K_ab]
    sol = sp.solve([(-Kj + eta * trK - 8 * sp.pi * G * Ssym)[i, j] for i in range(4) for j in range(i, 4)],
                   [Kj[i, j] for i in range(4) for j in range(i, 4)], dict=True)[0]
    Kjs = Kj.subs(sol)
    trKs = sp.simplify(trK.subs(sol))
    kp = sp.Matrix(sp.symbols("k0:4", real=True))
    kn2 = -(kp.T * eta * kp)[0]                                   # (k^n)^2 from g(k, k) = 0
    # Gaussian normal coordinates: R_ab^sing = -[K_ab] delta, R_nn^sing = -[K] delta
    Rsing = -((kp.T * Kjs * kp)[0] + trKs * kn2)
    gauss = sp.simplify(Rsing - 8 * sp.pi * G * (kp.T * Ssym * kp)[0]) == 0
    # P3's rows (one side, ell = 1), mixed components on the plane's orthonormal frame
    q = sp.Symbol("q", nonnegative=True)
    sq = -q if "israel_sign" in MUT else q
    Kmix = sp.diag(1 - sq, 1 - sq, 1 + sq, 1 + sq)
    # the doubled plane: [K^a_b] = -2 K^a_b, fixed so that q = 0 gives a positive tension
    jump = -2 * Kmix
    Smix = (-jump + sp.eye(4) * jump.trace()) / (8 * sp.pi * G)
    if "neg_tension" in MUT:
        Smix = Smix - 2 * Smix.subs(q, 0)
    sigma = sp.simplify(-Smix.subs(q, 0)[0, 0])
    tau = sp.simplify(Smix + sigma * sp.eye(4))
    rho = sp.simplify(-tau[0, 0])
    maxwell = sp.simplify(tau - sp.diag(-rho, -rho, rho, rho)) == sp.zeros(4)
    Slow = eta * Smix                                             # lower the first index
    Skk = sp.expand((kp.T * Slow * kp)[0])
    kn, k2, k3 = sp.symbols("kn k2 k3", nonnegative=True)
    Skk_n = sp.expand(Skk.subs(kp[0]**2, kn**2 + kp[1]**2 + kp[2]**2 + kp[3]**2))
    form = sp.expand((sigma + rho) * kn**2 + 2 * rho * (kp[2]**2 + kp[3]**2))
    coeffs = [sp.simplify(Skk_n.coeff(v, 2).subs({kn: 0, kp[1]: 0, kp[2]: 0, kp[3]: 0}))
              for v in (kn, kp[1], kp[2], kp[3])]
    nonneg = all(sp.simplify(cf.subs({q: qq, G: 1})) >= 0 for cf in coeffs for qq in (0, sp.Rational(1, 3), 2))
    return dict(gauss=gauss, sigma=sigma, rho=rho, maxwell=maxwell,
                matches=sp.simplify(Skk_n - form) == 0, coeffs=coeffs, nonneg=nonneg)


def c3_rs_jump():
    """the expansion jump of a planar null congruence across Randall-Sundrum's doubled plane"""
    y, ell, c, G = sp.symbols("y ell c G5", positive=True)
    def side(sgn):
        z = ell + y if "no_kink" in MUT else ell + sgn * y      # sgn = +1 above, -1 below (y < 0 there)
        Om = ell / z
        K = sp.diff(Om, y)                                        # K_ab = (1/2) Om^-1 d_y(Om^2) eta_ab = Om' eta_ab
        th = 3 * Om**-3 * (-c) * sp.diff(Om, y)                   # theta = 3 Om^-3 k^y d_y Om, k^y = -c
        return sp.limit(K, y, 0), sp.limit(th, y, 0)
    Kup, thb = side(+1)
    Kdn, tha = side(-1)
    Kj = sp.simplify(Kup - Kdn)                                   # [K_ab] = Kj eta_ab at Om = 1
    Sab = (-Kj + 4 * Kj) / (8 * sp.pi * G)                        # -[K_ab] + h [K], h = eta at the plane
    sigma = sp.simplify(-Sab)
    jump = sp.simplify(tha - thb)
    Skk = sigma * c**2                                            # S(k, k) = -sigma h(k, k) = sigma (k^n)^2, |k^n| = c
    pred = -8 * sp.pi * G * Skk / (1 if "drop_kn" in MUT else c)
    return dict(sigma=sigma, before=thb, after=tha, jump=jump, agrees=sp.simplify(jump - pred) == 0,
                focuses=sp.simplify(jump * ell / c) < 0)


def c4_wall():
    """b5b_wall's selftest, and the regularity of the wall's metric against the thin plane's"""
    p = subprocess.run([sys.executable, os.path.join(HERE, "b5b_wall.py"), "--selftest"], capture_output=True,
                       text=True, timeout=900)
    y, b, w, ell = sp.symbols("y b w ell", positive=True)
    A = -b * sp.log(sp.cosh(y / w))
    smooth = all(sp.limit(sp.diff(A, y, k), y, 0, "+") == sp.limit(sp.diff(A, y, k), y, 0, "-") for k in range(1, 6))
    Athin = -sp.Abs(y) / ell
    kinkj = sp.limit(sp.diff(-y / ell, y), y, 0) - sp.limit(sp.diff(y / ell, y), y, 0)
    return dict(selftest=p.returncode == 0, tail=p.stdout.strip().splitlines()[-1:] if p.stdout else [],
                smooth=smooth, thin_jump=sp.simplify(kinkj), thin=Athin)


def c5_trapped(s0=-0.05, N=200, Ns=38, fn="glob_kap0.2908.npy", kap=0.2908, bt=2.0):
    """the doubled closed 3-surface {tau, t fixed} on P3's start slice: theta(chi) for both null normals"""
    sys.path.insert(0, DN)
    import dnrun, dnE
    Y, chk = dnrun.initial(os.path.join(DN, fn), s0, N, kap, Ns, bt=bt)
    ev = dnE.DNE(N, kap)
    J = ev.jets(Y)
    S, A, r, St, At, rt = Y
    lr = np.empty_like(r)
    lr[1:] = rt[1:] / r[1:]
    lr[0] = J["r_tx"][0] / J["r_x"][0]                            # the axis by its limit
    sgn = -1.0 if "flip_time" in MUT else 1.0
    th = sgn * np.exp(-S + A / 2) * (St - 1.5 * At + 2 * lr)
    return th, ev.chi


def c8_vaidya():
    """Vaidya-AdS5: the dust's null energy, the trapped 3-spheres, the singularity"""
    v, r, a, b, c = sp.symbols("v r a b c", real=True)
    mu = sp.Function("mu")(v)
    f = 1 + r**2 - mu / r**2
    g = sp.zeros(5)
    g[0, 0], g[0, 1], g[1, 0] = -f, 1, 1
    g[2, 2], g[3, 3], g[4, 4] = r**2, r**2 * sp.sin(a)**2, r**2 * sp.sin(a)**2 * sp.sin(b)**2
    Ric, K = curvature(g, [v, r, a, b, c])
    src = sp.zeros(5)
    src[0, 0] = 3 * sp.diff(mu, v) / (2 * r**3)
    dust = all(sp.simplify(e) == 0 for e in (Ric + 4 * g - src))
    # expansions of the 3-sphere (area r^3): l_in = -d_r, l_out = d_v + (f/2) d_r
    th_in = sp.simplify(-sp.diff(3 * sp.log(r), r))
    th_out = sp.simplify((f / 2) * sp.diff(3 * sp.log(r), r))
    Kmu = sp.simplify(sp.expand(K).subs(sp.diff(mu, v), 0))
    return dict(dust=dust, th_in=th_in, th_out=th_out, out_form=sp.simplify(th_out - 3 * f / (2 * r)) == 0,
                kret=sp.simplify(Kmu - 40 - 72 * mu**2 / r**8) == 0, K=K)


# ---------------------------------------------------------------------------- checks
def selftest(quiet=False):
    out = []
    def ok(name, cond, note=""):
        out.append((name, bool(cond)))
        if not quiet:
            print("  %-4s %s  %s" % (name, "PASS" if cond else "FAIL", note), flush=True)

    txt = open(RULINGS).read()
    ok("C0", all(wd in txt for wd in WORDS) and len(SOURCES) == 9, "M's words verbatim; 9 sources READ")
    c1 = c1_bulk()
    ok("C1", c1["einstein"] and c1["Rkk"] == 0 and c1["kret"],
       "R_ab = -4 g_ab; R(k,k) = 0 for null k; K = 40 + 72 mu^2/r^8")
    c2 = c2_plane()
    ok("C2", c2["gauss"] and c2["maxwell"] and c2["matches"] and c2["nonneg"]
       and sp.simplify(c2["sigma"] - sp.Rational(3, 4) / sp.pi / sp.Symbol("G5", positive=True)) == 0,
       "R_sing(k,k) = 8 pi G5 S(k,k); sigma = %s, rho = %s; S(k,k) = (sigma+rho)(k^n)^2 + 2 rho (k_th^2 + k_ph^2)"
       % (c2["sigma"], c2["rho"]))
    c3 = c3_rs_jump()
    ok("C3", c3["agrees"] and c3["focuses"],
       "sigma = %s; theta %s -> %s; [theta] = %s = -8 pi G5 S(k,k)/|k^n|" % (c3["sigma"], c3["before"], c3["after"],
                                                                         c3["jump"]))
    c4 = c4_wall()
    ok("C4", c4["selftest"] and c4["smooth"] and c4["thin_jump"] != 0,
       "b5b_wall selftest %s; wall C^5 at y = 0; thin plane [A'] = %s" % (
           "passes" if c4["selftest"] else "FAILS", c4["thin_jump"]))
    rng = []
    for s0 in (-0.05, -0.15):
        th, chi = c5_trapped(s0)
        rng.append((s0, th.min(), th.max()))
    ok("C5", all(hi < 0 for _, lo, hi in rng),
       "; ".join("s0 %.2f: theta in [%.3f, %.3f]" % v for v in rng))
    th0 = max(hi for _, lo, hi in rng)
    lam = 3 / abs(th0)
    # Raychaudhuri with R(k,k) >= 0: the comparison solution reaches -infinity at lam = 3/|theta0|
    tl = sp.Symbol("t0", negative=True)
    L = sp.Symbol("lam", positive=True)
    comp = 3 * tl / (3 + tl * L)
    ode = sp.simplify(sp.diff(comp, L) + comp**2 / 3) == 0
    ok("C6", ode and lam < 21, "theta' = -theta^2/3 solved; focal point within lam = 3/|theta0| = %.1f ell" % lam)
    ok("C7", c4["selftest"] and c1["Rkk"] == 0 and all(hi < 0 for _, lo, hi in rng) and c4["thin_jump"] != 0,
       "KSV (i) C1+C4, (iii) C5, (ii) assumed: smooth wall not future null complete; thin plane open (Lipschitz)")
    c8 = c8_vaidya()
    ok("C8", c8["dust"] and c8["th_in"] == -3 / sp.Symbol("r", real=True) and c8["out_form"] and c8["kret"],
       "R_ab + 4 g_ab = (3 mu'/(2 r^3)) l l; theta_in = -3/r, theta_out = 3 f/(2r); K_mu = 72 mu^2/r^8")
    ok("C9", "Bousso" in SOURCES and "SM" in SOURCES and "Bousso-14" in SOURCES,
       "semiclassical bounce excluded on the plane (READ + deduced); full quantum regime not addressed")
    n = sum(v for _, v in out)
    if not quiet:
        print("collapse_bulk selftest: %d/%d" % (n, len(out)))
    return out


MUTANTS = {"lam_off": "C1", "israel_sign": "C2", "neg_tension": "C2", "no_kink": "C3", "drop_kn": "C3",
           "flip_time": "C5"}


def mutants():
    caught = 0
    for m, target in MUTANTS.items():
        MUT.clear(); MUT.add(m)
        res = dict(selftest(quiet=True))
        hit = not res.get(target, True)
        caught += hit
        print("  mutant %-12s -> %s %s" % (m, target, "caught" if hit else "MISSED"), flush=True)
    MUT.clear()
    print("collapse_bulk mutants: %d/%d caught" % (caught, len(MUTANTS)))
    return caught == len(MUTANTS)


if __name__ == "__main__":
    if "--mutants" in sys.argv:
        sys.exit(0 if mutants() else 1)
    res = selftest()
    sys.exit(0 if all(v for _, v in res) else 1)
