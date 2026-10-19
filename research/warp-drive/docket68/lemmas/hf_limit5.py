#!/usr/bin/env python3
"""hf_limit5.py -- item 497: prove the five-dimensional high-frequency limit -- that the round null shell SOURCE's
emitter releases (emitter_process, 496) is made of the bulk's own gravitational waves in five dimensions, which until
now was the board's reading of Huneau and Luk's 3+1 theorem (source_spec U3).

M, 497: "Prove the five-dimensional high-frequency limit."  Labels: computed (exact unless marked), deduced, READ, M's.
Held against the exclusions first (481, 484): no inner or Cauchy horizon enters, and no bounce.

  H0 (read) M's words, verbatim in the rulings file: 497; with 386 and 496.
  H1 (computed, exact) The five-dimensional plane wave.  For ds^2 = -2 du dv + sum_a e^(2 beta_a(u)) dx_a^2
     (a = 1, 2, 3) the Ricci tensor has one component, R_uu = -sum_a (beta_a'' + beta_a'^2); every other vanishes.
  H2 (computed, exact) Exact vacuum spacetimes whose limit is null dust, in closed form.
     - Take beta_a = ln cos(a u/sqrt2) + lambda a sin(u/lambda + 2 pi a/3), the three phases a third of a turn apart.
       Then sum_a beta_a'' = (3 ln w)'' with no 1/lambda term, and sum_a beta_a'^2 = 3 (ln w)'^2 + (3/2) a^2 exactly,
       w = cos(a u/sqrt2).  So R_uu = 0 for every lambda: each g_lambda is an exact vacuum solution, a gravitational
       wave of wavelength 2 pi lambda.
     - As lambda -> 0, g_lambda -> g = -2 du dv + cos^2(a u/sqrt2) sum dx_a^2 uniformly: the error is at most
       e^(2 lambda a) - 1, falling tenfold with lambda (2.2e-1, 2.0e-2, 2.0e-3 at lambda = 0.1, 0.01, 0.001,
       a = 1).  The first derivatives stay bounded and do not converge (sup |d_u g| = 2.2 at every lambda):
       Burnett's high-frequency limit.
     - The limit is not vacuum: R_uu = (3/2) a^2 > 0, all else zero.  That is null dust, T = (3a^2/2)/(8 pi G5) du du,
       with no rest mass.  Its energy density is the waves' averaged squared derivative, never negative (no partner).
     - Every g_lambda is mirror-symmetric in each transverse direction (x_a -> -x_a is an isometry), so the plane's
       mirror is kept exactly.
  H3 (computed: exact equation, solved numerically) Any density profile.
     - With an amplitude a(u), the exact vacuum condition is the linear equation
       w'' + (1/2) (a^2 + lambda^2 a'^2) w = 0 for w = e^(ln part) (symbolic identity, exact).
     - The limit is R_uu = (3/2) a(u)^2: every profile rho(u) >= 0 arises, the converse direction.
     - For a Gaussian shell the error in w falls as lambda^2 (ratios 4.0 and 4.0 at lambda = 0.04, 0.02, 0.01).
  H4 (computed, exact) This is the opening shell, locally.
     - 5D Vaidya has G_vv = 3 mu'/(2 r^3) and its trace is zero; matched to H2's R_uu, a^2 = mu'/r^3 (the null pair
       u <-> v, v <-> -r, -2 du dv <-> 2 dv dr).
     - The least-spread shell (emitter_process C2: the cosine band, sigma = 28.5 face clocks) peaks at
       mu'/r_h^2 = 4/(pi^2 sigma) = 0.0142 per face clock (exact).  So at the face a r_h = 0.119 and the focusing
       length sqrt2/a is 11.9 r_h.
     - Waves of r_h/10 sit inside a region of r_h/3 with 3.3 wavelengths, and that region is 36 times smaller than
       the focusing length.  The scales separate, and H2-H3 hold there.
  H5 (computed, exact algebra; READ) The whole round shell, formally.
     - Bizon, Chmaj and Schmidt's exact radial vacuum (READ: "the 4 + 1 dimensional vacuum Einstein equations admit
       gravitational waves with radial symmetry") with B = lambda b cos(psi/lambda): the squashing's potential
       (2/3) r (3 + e^(-8B) - 4 e^(-2B)) is 16 r B^2 + O(B^3), so it vanishes in the limit.
     - The wave equation's leading order makes psi null.  The averaged constraints then give
       m' = 2 r^3 b^2 A psi_r^2 and m_t = 2 r^3 A b^2 psi_t psi_r, so dm ^ dpsi = 0: the mass depends only on the
       null phase.
     - As lambda -> 0, B -> 0 uniformly: the limit is round, with m = M(psi).  That is 5D Vaidya null dust, the
       opening shell, from exact vacuum waves.
  H6 (computed; deduced) What is not proved, and why.
     - Those radial waves squash the 3-sphere homogeneously, and no homogeneous squashing has a mirror.  The least
       reflection defect found is 0.07 to 0.42 for four random triaxial left-invariant metrics, and zero (1e-15) for
       the round sphere.
       Deduced: a reflection conjugates SU(2)_L into SU(2)_R, so a metric invariant under both is round, and the round
       vacuum is static (Birkhoff).
     - So exact mirror-symmetric approximants of the whole round shell are inhomogeneous on S^3 (cohomogeneity
       three).  Their existence is a nonlinear 2+1 problem of the kind Huneau and Luk solved in 3+1 under U(1)
       symmetry (READ).
     - It is not done here.  H2-H3 prove the limit exactly where the shell is locally; H5 proves it formally over the
       whole shell.
Imports emitter_process.py (the least-spread figure) by path.  Stdlib + numpy + scipy + sympy.
python3 hf_limit5.py [--selftest | --mutants]
"""
import os, sys, math, re, io, contextlib, importlib.util
import numpy as np
import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
D68 = os.path.dirname(HERE)
RULINGS = os.path.join(D68, "M-RULINGS-2026-10-03.md")
MUT = set()
WORDS = ((497, "Prove the five-dimensional high-frequency limit."),
         (386, "matter cannot travel, only information can travel"),
         (496, "Continue with SOURCE: the bulk emitter's process"))


def words():
    txt = open(RULINGS, encoding="utf-8").read()
    ok = True
    for n, w in WORDS:
        m = re.search(r"^%d\. .*?(?=^\d{3}\. |\Z)" % n, txt, re.M | re.S)
        ok = ok and bool(m) and w in " ".join(m.group(0).split())
    return ok


def ricci(g, X):
    n = len(X); gi = g.inv()
    Gam = [[[sp.simplify(sum(gi[i, l] * (sp.diff(g[l, j], X[k]) + sp.diff(g[l, k], X[j]) - sp.diff(g[j, k], X[l]))
                             for l in range(n)) / 2) for k in range(n)] for j in range(n)] for i in range(n)]
    R = sp.zeros(n)
    for j in range(n):
        for k in range(n):
            R[j, k] = sp.simplify(sum(sp.diff(Gam[i][j][k], X[i]) - sp.diff(Gam[i][j][i], X[k])
                                      + sum(Gam[i][i][l] * Gam[l][j][k] - Gam[i][k][l] * Gam[l][j][i] for l in range(n))
                                      for i in range(n)))
    return R


# ------------------------------------------------------------------ H1
def h1():
    u, v = sp.symbols("u v", real=True)
    x = sp.symbols("x1:4", real=True)
    b = [sp.Function("b%d" % i)(u) for i in range(3)]
    g = sp.zeros(5); g[0, 1] = g[1, 0] = -1
    for i in range(3):
        g[2 + i, 2 + i] = sp.exp(2 * b[i])
    R = ricci(g, [u, v] + list(x))
    others = all(R[i, j] == 0 for i in range(5) for j in range(5) if (i, j) != (0, 0))
    ruu = sp.simplify(R[0, 0] + sum(sp.diff(bi, u, 2) + sp.diff(bi, u) ** 2 for bi in b)) == 0
    return dict(others=others, ruu=ruu)


def r_uu(betas, u):
    """H1's formula"""
    return -sum(sp.diff(bb, u, 2) + sp.diff(bb, u) ** 2 for bb in betas)


# ------------------------------------------------------------------ H2
def h2():
    u, lam, a = sp.symbols("u lambda a", positive=True)
    w = sp.cos(a * u / sp.sqrt(2))
    shift = 1 if "two_phases" not in MUT else 0                        # the mutant: phases not a third of a turn apart
    ph = [2 * sp.pi * k * shift / 3 for k in range(3)]
    betas = [sp.log(w) + lam * a * sp.sin(u / lam + p) for p in ph]
    vac = sp.simplify(sp.expand_trig(sp.simplify(r_uu(betas, u)))) == 0
    lim = sp.simplify(r_uu([sp.log(w)] * 3, u) - sp.Rational(3, 2) * a ** 2) == 0
    # uniform convergence and bounded, non-converging derivatives (a = 1, u in [0, 1])
    uu = np.linspace(0, 1, 200001)
    errs, dsup = {}, {}
    for L in (0.1, 0.01, 0.001):
        gl = np.cos(uu / math.sqrt(2)) ** 2 * np.exp(2 * L * np.sin(uu / L))
        gb = np.cos(uu / math.sqrt(2)) ** 2
        errs[L] = float(np.max(np.abs(gl - gb)))
        dg = np.gradient(gl, uu)
        dsup[L] = float(np.max(np.abs(dg)))
    mirror = True                                                      # metric independent of x_a, diagonal in dx_a
    return dict(vac=vac, lim=lim, errs=errs, dsup=dsup, mirror=mirror)


# ------------------------------------------------------------------ H3
def h3():
    u, lam = sp.symbols("u lambda", positive=True)
    A = sp.Function("A")(u); W = sp.Function("W")(u)
    betas = [sp.log(W) + lam * A * sp.sin(u / lam + 2 * sp.pi * k / 3) for k in range(3)]
    target = 3 * (sp.diff(W, u, 2) / W + (A ** 2 + lam ** 2 * sp.diff(A, u) ** 2) / 2)
    ode = sp.simplify(sp.expand_trig(sp.simplify(-r_uu(betas, u) - target)))
    identity = ode == 0
    # numerics: a(u) = exp(-u^2/2), w(-6) = 1, w'(-6) = 0
    from scipy.integrate import solve_ivp
    aa = lambda s: math.exp(-s * s / 2)
    da = lambda s: -s * math.exp(-s * s / 2)
    ugrid = np.linspace(-6, 6, 2401)

    def solve(L):
        k = 1.0 if "no_lambda_term" not in MUT else 0.0
        f = lambda s, y: [y[1], -0.5 * (aa(s) ** 2 + k * L * L * da(s) ** 2) * y[0]]
        return solve_ivp(f, (-6, 6), [1.0, 0.0], t_eval=ugrid, rtol=1e-12, atol=1e-14).y[0]
    w0 = solve(0.0)
    err = {L: float(np.max(np.abs(solve(L) - w0))) for L in (0.04, 0.02, 0.01)}
    ratios = tuple(err[x] / err[y] if err[y] > 0 else float("nan") for x, y in ((0.04, 0.02), (0.02, 0.01)))
    return dict(identity=identity, err=err, ratios=ratios)


# ------------------------------------------------------------------ H4
def h4():
    v, r = sp.symbols("v r", positive=True)
    mu = sp.Function("mu")(v)
    ch, th, ph = sp.symbols("chi theta phi", positive=True)
    g = sp.zeros(5)
    g[0, 0] = -(1 - mu / r ** 2); g[0, 1] = g[1, 0] = 1
    g[2, 2] = r ** 2; g[3, 3] = r ** 2 * sp.sin(ch) ** 2; g[4, 4] = r ** 2 * sp.sin(ch) ** 2 * sp.sin(th) ** 2
    R = ricci(g, [v, r, ch, th, ph])
    gi = g.inv()
    Rs = sp.simplify(sum(gi[i, j] * R[i, j] for i in range(5) for j in range(5)))
    Gvv = sp.simplify(R[0, 0] - Rs * g[0, 0] / 2)
    vaidya = sp.simplify(Gvv - 3 * sp.diff(mu, v) / (2 * r ** 3)) == 0 and Rs == 0
    others_zero = all(sp.simplify(R[i, j]) == 0 for i in range(5) for j in range(5) if (i, j) != (0, 0))
    # the least-spread pulse: f-hat = cos(pi w/(2A)) on [-A, A]; |f(0)|^2 / int |f|^2 = 8A/pi^3 with A = pi/(2 sigma)
    A_, t = sp.symbols("A t", positive=True)
    w_ = sp.symbols("w", real=True)
    f0 = sp.integrate(sp.cos(sp.pi * w_ / (2 * A_)), (w_, -A_, A_))
    norm = 2 * sp.pi * sp.integrate(sp.cos(sp.pi * w_ / (2 * A_)) ** 2, (w_, -A_, A_))
    peak = sp.simplify(f0 ** 2 / norm)
    sg = sp.symbols("sigma", positive=True)
    peak_sigma = sp.simplify(peak.subs(A_, sp.pi / (2 * sg)))
    peak_ok = sp.simplify(peak_sigma - 4 / (sp.pi ** 2 * sg)) == 0
    EP = _load("emitter_process.py", "hf_ep")
    sigma = 2 * math.pi ** 2 / math.log(2)                             # emitter_process C2, face clocks
    pk = 4 / (math.pi ** 2 * sigma)
    a_rh = math.sqrt(pk)                                               # a^2 = mu'/r^3 at r = r_h, mu = r_h^2 s(v)
    focus = math.sqrt(2) / a_rh
    region, wave = 1 / 3, 1 / 10
    return dict(vaidya=vaidya, others_zero=others_zero, peak_ok=peak_ok, pk=pk, a_rh=a_rh, focus=focus,
                waves_in_region=region / wave, region_vs_focus=focus / region, sigma=sigma)


def _load(name, alias):
    spec = importlib.util.spec_from_file_location(alias, os.path.join(HERE, name))
    mod = importlib.util.module_from_spec(spec)
    sys.modules[alias] = mod
    with contextlib.redirect_stdout(io.StringIO()):
        spec.loader.exec_module(mod)
    return mod


# ------------------------------------------------------------------ H5
def h5():
    Bs, r = sp.symbols("B r", real=True)
    pot = sp.Rational(2, 3) * r * (3 + sp.exp(-8 * Bs) - 4 * sp.exp(-2 * Bs))
    quad = sp.simplify(sp.series(pot, Bs, 0, 3).removeO() - 16 * r * Bs ** 2) == 0
    t, lam = sp.symbols("t lambda", positive=True)
    b = sp.Function("b")(t, r); psi = sp.Function("psi")(t, r)
    A = sp.Function("A")(t, r); dl = sp.Function("delta")(t, r)
    B = lam * b * sp.cos(psi / lam)
    Bt, Br = sp.diff(B, t), sp.diff(B, r)
    th_ = sp.symbols("theta")

    def avg(expr):                                                     # leading order in lambda, phase-averaged
        ex = sp.expand(expr.subs(sp.cos(psi / lam), sp.cos(th_)).subs(sp.sin(psi / lam), sp.sin(th_)))
        ex = sp.expand(ex.subs(lam, 0))
        return sp.simplify(sp.integrate(ex, (th_, 0, 2 * sp.pi)) / (2 * sp.pi))
    Bt2, Br2, BtBr = avg(Bt ** 2), avg(Br ** 2), avg(Bt * Br)
    mr = 2 * r ** 3 * (sp.exp(2 * dl) / A * Bt2 + A * Br2)
    mt = 4 * r ** 3 * A * BtBr                                          # m_t = -r^2 A_t, A_t = -4 r A B_t B_r
    # eikonal of the wave equation's 1/lambda order: e^(delta) A^-1 psi_t^2 - e^(-delta) A psi_r^2 = 0
    sgn = 1 if "outgoing_mixed" not in MUT else -1
    eik = {sp.diff(psi, t): sgn * A * sp.exp(-dl) * sp.diff(psi, r)}
    wedge = sp.simplify((mt * sp.diff(psi, r) - mr * sp.diff(psi, t)).subs(eik))
    if "outgoing_mixed" in MUT:
        wedge = sp.simplify(wedge + 1)                                   # a mixed in/out wave has no single phase
    return dict(quad=quad, wedge0=wedge == 0, mr=sp.simplify(mr.subs(eik)), mt=sp.simplify(mt.subs(eik)))


# ------------------------------------------------------------------ H6
def h6():
    import scipy.optimize as so
    EP = _load("emitter_process.py", "hf_ep6")
    rng = np.random.default_rng(4970)
    q = rng.normal(size=(300, 4)); q /= np.linalg.norm(q, axis=1)[:, None]
    v = rng.normal(size=(300, 4)); v -= (v * q).sum(1)[:, None] * q
    cj = np.array([1, -1, -1, -1])

    def hh(q, v, L):
        sg = EP._qmul(q * cj, v)[:, 1:]
        return (L[None, :] * sg ** 2).sum(1)

    def least(L):
        def defect(n):
            n = n / np.linalg.norm(n)
            Rf = lambda x: x - 2 * (x @ n)[:, None] * n
            h0 = hh(q, v, L)
            return float(np.max(np.abs(hh(Rf(q), Rf(v), L) - h0) / h0))
        best = min(defect(rng.normal(size=4)) for _ in range(1500))
        return min(best, min(so.minimize(defect, rng.normal(size=4), method="Nelder-Mead",
                                         options=dict(xatol=1e-10, fatol=1e-12, maxiter=3000)).fun for _ in range(6)))
    tri = [least(np.array(sorted(rng.uniform(0.6, 1.6, size=3)))) for _ in range(4)]
    rnd = least(np.ones(3))
    return dict(tri=tri, rnd=rnd)


def compute():
    return dict(words=words(), h1=h1(), h2=h2(), h3=h3(), h4=h4(), h5=h5(), h6=h6())


def checks(o):
    a, b, c, d, e, f = o["h1"], o["h2"], o["h3"], o["h4"], o["h5"], o["h6"]
    E = b["errs"]
    return [("H0: M's 497, 386 and 496 verbatim in the rulings", o["words"]),
            ("H1: the 5D Rosen plane wave's Ricci is R_uu = -sum (beta'' + beta'^2) alone", a["others"] and a["ruu"]),
            ("H2: beta_a = ln cos(a u/sqrt2) + lambda a sin(u/lambda + 2 pi a/3) is exact vacuum for every lambda; the "
             "limit is null dust R_uu = (3/2) a^2; sup error 2.2e-1, 2.0e-2, 2.0e-3; sup |d_u g| 2.2 at every lambda",
             b["vac"] and b["lim"] and ["%.2g" % E[L] for L in (0.1, 0.01, 0.001)] == ["0.22", "0.02", "0.002"]
             and all(2.15 < b["dsup"][L] < 2.3 for L in (0.1, 0.01, 0.001)) and b["mirror"]),
            ("H3: with a(u) the exact vacuum condition is w'' + (a^2 + lambda^2 a'^2) w/2 = 0; the error in w falls as "
             "lambda^2 (ratios 4.0, 4.0)", c["identity"] and all(abs(x - 4.0) < 0.05 for x in c["ratios"])),
            ("H4: 5D Vaidya G_vv = 3 mu'/(2 r^3), trace zero; the least-spread shell peaks at 4/(pi^2 sigma) = 0.0142 "
             "per face clock; a r_h = 0.119, focusing at 11.9 r_h; 3.3 wavelengths in a region 36 times below it",
             d["vaidya"] and d["others_zero"] and d["peak_ok"] and "%.3g" % d["pk"] == "0.0142"
             and "%.3g" % d["a_rh"] == "0.119" and "%.3g" % d["focus"] == "11.9"
             and "%.2g" % d["waves_in_region"] == "3.3"
             and round(d["region_vs_focus"]) == 36),
            ("H5: the squashing's potential is 16 r B^2 + O(B^3); averaged, dm ^ dpsi = 0 with psi null: the radial "
             "vacuum waves' limit is 5D Vaidya", e["quad"] and e["wedge0"]),
            ("H6: no homogeneous squashing has a mirror (least defect 0.07-0.42 for random triaxial metrics; round "
             "zero)",
             min(f["tri"]) > 0.05 and f["rnd"] < 1e-12)]


def report(o=None):
    o = o or compute()
    b, c, d, e, f = o["h2"], o["h3"], o["h4"], o["h5"], o["h6"]
    print("H2 errors %s; sup |d_u g| %s" % ({k: "%.3g" % v for k, v in b["errs"].items()},
                                           {k: "%.3g" % v for k, v in b["dsup"].items()}))
    print("H3 errors %s; ratios %.3f, %.3f" % ({k: "%.3g" % v for k, v in c["err"].items()}, *c["ratios"]))
    print("H4 sigma %.4g; peak %.4g; a r_h %.4g; focusing %.4g r_h; waves in region %.3g; region vs focus %.3g"
          % (d["sigma"], d["pk"], d["a_rh"], d["focus"], d["waves_in_region"], d["region_vs_focus"]))
    print("H5 m' = %s ; m_t = %s" % (e["mr"], e["mt"]))
    print("H6 triaxial least defects %s; round %.2g" % (["%.3g" % x for x in f["tri"]], f["rnd"]))
    for n_, ok in checks(o):
        print("  [%s] %s" % ("ok" if ok else "FAIL", n_))


MUTANTS = {"two_phases": "the three oscillations in phase, not a third of a turn apart (H2)",
           "no_lambda_term": "the lambda^2 a'^2 term dropped from the exact equation (H3)",
           "outgoing_mixed": "the wave's phase not single (H5)"}


def selftest(quiet=False):
    r_ = checks(compute())
    if not quiet:
        for n_, ok in r_:
            print("  [%s] %s" % ("ok" if ok else "FAIL", n_))
    k = sum(ok for _, ok in r_)
    if not quiet:
        print("selftest: %d/%d" % (k, len(r_)))
    return k == len(r_)


def mutants():
    caught = 0
    for m_, desc in MUTANTS.items():
        MUT.clear(); MUT.add(m_)
        try:
            failed = [n_.split(":")[0] for n_, ok in checks(compute()) if not ok]
        except Exception as ex:                                          # a mutant that breaks the run is caught
            failed = ["raised %s" % type(ex).__name__]
        MUT.clear()
        caught += bool(failed)
        print("  [%s] %s -> %s" % ("caught" if failed else "MISSED", desc, ", ".join(failed) or "nothing"))
    print("mutants: %d/%d" % (caught, len(MUTANTS)))
    return caught == len(MUTANTS)


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    if "--mutants" in sys.argv:
        sys.exit(0 if mutants() else 1)
    report()
