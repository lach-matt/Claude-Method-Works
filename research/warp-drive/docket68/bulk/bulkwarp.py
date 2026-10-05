#!/usr/bin/env python3
"""
bulkwarp.py -- the bulk (BULK4-O6; M-RULINGS item 79, 'Seat all three, then the bulk'): can a bulk keeping the null
energy condition, read through our plane's Weyl term, supply a warp's negative energy?  READ at source, then deduced
from first principles (M-DEDUCE).

Not seated; not verified.  M's words are carried as hypotheses, never as results.  O9 stays OPEN.

    python3 bulkwarp.py              report
    python3 bulkwarp.py --selftest   checks, with CONTROLS
    python3 bulkwarp.py --json       the numbers as JSON

SOURCES READ (2026-10-05; route: alphaXiv answer_pdf_queries on open arXiv copies, printed pages)
  Dahia & Romero gr-qc/0109076v2: 'any n-dimensional semi-Riemannian manifold can be locally embedded in an
    (n+1)-dimensional Einstein space' (abstract); Theorem 3 requires the metric to be analytic ('we are considering only
    manifolds and metrics which are analytic', p.3) and the embedding is local, at a point (p.16); with negative Lambda
    'the embedding space is closely related to the so-called bulk, in the Randall-Sundrum braneworld scenario' (p.19).
  Seahra & Wesson gr-qc/0302015v4: in the thin Z2 braneworld 'any solution of (3 + 1)-dimensional general relativity
    can be realized as a thin 3-brane in the RS scenario. However, to accomplish this we lose control of the jump in
    extrinsic curvature [K] across Sigma_0, which is related to the stress-energy tensor of standard model fields living
    on the brane' and 'if we fix the intrinsic geometry of the brane then the properties of conventional matter will be
    determined dynamically' (p.7); the brane matter is S = -2 eps kappa^-2 P+, P = K - h K (eq. 33), conserved (eq. 23);
    the scalar Gauss constraint (n-1) lambda = R + eps (K.K - K^2) (eq. 25); 'the Campbell-Magaard theorem is a local
    result' (p.5); the thick brane 'cannot embed arbitrary spacetimes if the bulk contains only vacuum energy' (p.11).
  Anderson gr-qc/0409122v2: the Campbell-Magaard theorem 'lends only inadequate support, both because it offers no
    guarantee of continuous dependence on the data and because it disregards causality' and 'is only for the analytic
    functions which renders it inappropriate for the study of the relativistic field equations' (abstract); 'there are
    as yet no known general theorems that offer adequate protection to the proposed applications' prescription'
    (abstract); embeddings are 'so nonunique' (p.7).
  Alias & Jalar 2203.05989v2, a 'braneworld hyperdrive': the energy density 'acquires exotic matter property of
    negative energy at the slope of the transition region' (p.14) and 'the hyperdrive requires much more energy than
    that of a warp drive' (p.14); no bulk is constructed.
  Carried from signdim.py (READ there): Shiromizu-Maeda-Sasaki eqs. 2, 10, 16, 17, 19, 21 (the Gauss and Codazzi
    equations, the Z2 junction, the brane equations, G_N, the conservation of tau); Alcubierre eq. 19 and Natario's
    rho (p.4).

PREMISES
  P-Z2           a thin Z2-symmetric brane: K+ = -(kappa^2/2)(S - q S/3), S = -lambda q + tau (SMS eqs. 14, 16).  READ.
  P-VACUUM-BULK  the bulk's only stress near the plane is its vacuum energy, T = -Lambda g (SMS eq. 13): the NEC holds,
                 saturated; its Weyl curvature is free.  This is BULK4-O6's 'bulk keeping the NEC read through the Weyl
                 term'.  Named.
  P-GC           the scalar Gauss equation R = K^2 - K.K - 2 G5_nn and the Codazzi equation D^nu(K_mn - q K) = kappa^2
                 T5_n mu (SMS eqs. 2, 10): both involve the bulk's Ricci tensor only -- E_mn appears in neither.  READ.
  P-LEADING      leading order in the warp speed v (v << 1) and in R l^2 << 1 (the plane's curvature against the bulk's).
                 Named.
  H-COMOVING     the plane's matter moves with the bubble (depends on x - v t).  Named.
  H-LOCALISED    the plane's matter falls off faster than r^-3.  Named.
  P-NEC-BRANE    the plane's matter keeps the null energy condition (the tension is null-blind).  The question's demand.

DEDUCTIONS (each from the premises named)
  W1 A BULK KEEPING THE NEC EXISTS LOCALLY FOR ANY ANALYTIC WARP METRIC.  [Dahia-Romero Thm 3; Seahra-Wesson p.7;
     computed: Alcubierre's form function is even in r_s, so analytic]  A patch of Alcubierre's metric can be realised
     as a Z2 brane in a vacuum Einstein bulk.  The price is stated by the source: the plane's matter is then
     'determined dynamically'.  The protection is weak (Anderson): local, analytic only, no continuous dependence, no
     causality.
  W2 THE PLANE'S MATTER IS FIXED BY THE PLANE'S METRIC ALONE, WHATEVER THE BULK'S WEYL CURVATURE.  [P-Z2, P-VACUUM-BULK,
     P-GC, P-LEADING; computed]  Write K = -a q + k with a = kappa^2 lambda/6 (the Randall-Sundrum value, sign of the
     tension).  Then the matter is tau = -(2/kappa^2)(k - q k), the scalar Gauss equation gives R = -6 a k to leading
     order, and Codazzi makes tau conserved.  So tau's trace is -6R/(kappa^4 lambda) = -R/(8 pi G_N) -- the same as SMS
     eq. 17's trace (check 3) -- and E drops out.  No choice of bulk Weyl curvature changes the plane's matter's trace or
     its conservation.
  W3 A CONSERVED, LOCALISED, COMOVING MATTER THAT KEEPS THE NEC HAS NON-NEGATIVE TOTAL ENERGY, AND ITS INTEGRATED TRACE
     IS (v^2 - 1) TIMES THAT ENERGY.  [H-COMOVING, H-LOCALISED, P-NEC-BRANE, P-LEADING; the flat-space conservation
     identities, checked on a boosted self-stressed body]  With fields depending on x - v t, conservation gives
     int tau_{mu i} = -v delta_ix int tau_{mu 0}; hence int tau_kk = E (1 - v n_x)^2 for every null k = (1, n), so the NEC
     makes E = int tau_00 >= 0; and int tau^mu_mu = (v^2 - 1) E.
  W4 ALCUBIERRE'S METRIC FIXES THE PLANE'S MATTER'S TOTAL ENERGY: E = int R d^3x / (8 pi G_N), WITH THE SIGN OF THE
     TENSION.  [W2, W3; computed: int R d^3x = (v^2/2) int (f_y^2 + f_z^2) = -16 pi int rho_Alc > 0]  At leading order
     int tau^mu_mu = -E, and W2 makes it -int R/(8 pi G_N).  Since int R > 0, E has the sign of G_N, which is the sign of
     lambda (SMS eq. 19).  On a positive-tension plane E = 2|E_Alc|: positive, twice the magnitude of Alcubierre's
     negative energy, and the bulk's reading carries the rest (-3|E_Alc| in the plane's reading).
  W5 ON A NEGATIVE-TENSION PLANE THE TEST FAILS.  [W4, P-NEC-BRANE; H-RS1 for 'ours']  There E < 0, contradicting W3:
     a slow warp on a negative-tension Z2 plane cannot be carried by matter that keeps the NEC, conserved, localised and
     comoving, in a bulk whose only stress is its vacuum energy -- whatever the bulk's Weyl curvature.  Under H-RS1 that
     plane is ours.  This is H-SIGN-BY-DIMENSION's question answered one way at leading order: the sign of the plane's
     tension -- its position in the fifth dimension -- decides whether the bulk can supply the warp's negative energy.
  W6 ON A POSITIVE-TENSION PLANE THE TEST PASSES, AND SUFFICIENCY IS OPEN.  [W4; computed]  The integral condition is
     met.  Pointwise it is not trivial: R takes both signs across the wall (computed), so dust alone would need negative
     density where R < 0; stresses are needed, and whether a conserved stress keeping the NEC pointwise exists is OPEN.
  W7 WHAT EVADES THE TEST.  [P-GC; named]  A bulk field (Maartens' F_mn): its T5_nn enters the Gauss equation and its
     flux T5_n mu enters Codazzi, and the NEC does not fix T5_nn's sign.  Randall-Sundrum's radion stabilisation is such
     a field (Goldberger-Wise, NAMED-NOT-READ).  Also: a superluminal bubble (outside P-LEADING), matter that radiates
     or is not localised, a thick brane.  Each is OPEN, not a result.

NAMED HYPOTHESES
  P-VACUUM-BULK, P-LEADING, H-COMOVING, H-LOCALISED, H-ALCUBIERRE-ILLUSTRATIVE (sigma = 8, R = 1, v_s = 1, geometric
  units, carried from signdim.py), H-RS1 (carried from bulk.py); and M's H-SIGN-BY-DIMENSION, H-ALCUBIERRE-PARTIAL,
  H-HIGHER-CORRIDOR.
"""
import contextlib
import importlib.util
import io
import json
import math
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
WD = os.path.dirname(os.path.dirname(HERE))


def _by_path(key, path):
    if key in sys.modules:
        return sys.modules[key]
    spec = importlib.util.spec_from_file_location(key, path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[key] = mod
    spec.loader.exec_module(mod)
    return mod


_saved = list(sys.path)
try:
    sys.path.insert(0, WD)
    with contextlib.redirect_stdout(io.StringIO()):
        signdim = _by_path("bulk_signdim", os.path.join(HERE, "signdim.py"))
finally:
    sys.path[:] = _saved

GRID = (400, 200)                     # Simpson grid for the axisymmetric integrals (x, s)


# ------------------------------------------------------------------ W3: the conservation identities
def laue_boosted(conserved=True):
    """A body at rest with mass density A e^{-r^2} and stress T'_ij = delta_ij lap(phi) - d_i d_j phi (divergence-free,
    phi = B e^{-r^2}); with conserved=False the stress is a pressure delta_ij phi (not divergence-free).  Boosted to
    speed v and integrated over the lab frame at t = 0: returns int tau^mu_mu - (v^2 - 1) int tau_00 (zero if W3 holds)."""
    import sympy as sp
    x, y, z = sp.symbols("x y z", real=True)
    A, B = sp.symbols("A B", positive=True)
    v = sp.Rational(3, 5)
    g = 1 / sp.sqrt(1 - v ** 2)
    r2 = x ** 2 + y ** 2 + z ** 2
    rho = A * sp.exp(-r2)
    phi = B * sp.exp(-r2)
    X = (x, y, z)
    if conserved:
        lap = sum(sp.diff(phi, c, 2) for c in X)
        T = [[(lap if i == j else 0) - sp.diff(phi, X[i], X[j]) for j in range(3)] for i in range(3)]
    else:
        T = [[(phi if i == j else 0) for j in range(3)] for i in range(3)]
    tau00 = g ** 2 * (rho + v ** 2 * T[0][0])
    trace = -rho + T[0][0] + T[1][1] + T[2][2]
    sub = {x: g * x}                                          # at t = 0 the rest-frame x' is gamma x

    def integ(e):
        e = sp.simplify(e.subs(sub, simultaneous=True))
        return sp.integrate(e, (x, -sp.oo, sp.oo), (y, -sp.oo, sp.oo), (z, -sp.oo, sp.oo))

    return sp.simplify(integ(trace) - (v ** 2 - 1) * integ(tau00))


def nec_integrated():
    """From int tau_{mu i} = -v delta_ix int tau_{mu 0}: int tau_kk for k = (1, n) in terms of E = int tau_00."""
    import sympy as sp
    E, v, nx, ny, nz = sp.symbols("E v n_x n_y n_z", real=True)
    t0 = {"x": -v * E, "y": 0, "z": 0}
    tij = {("x", "x"): v ** 2 * E}
    n = {"x": nx, "y": ny, "z": nz}
    s = E + 2 * sum(n[i] * t0[i] for i in "xyz") + sum(n[i] * n[j] * tij.get((i, j), 0) for i in "xyz" for j in "xyz")
    trace = -E + v ** 2 * E
    return sp.factor(s.subs({ny: sp.sqrt(1 - nx ** 2), nz: 0})), sp.factor(trace)


# ------------------------------------------------------------------ W2: the plane's matter from Gauss-Codazzi
def gauss_trace(tuned=True):
    """K = -a q + e k (k symmetric, generic); R = K^2 - K.K + 2 kappa^2 Lambda (SMS eq. 2 contracted twice, spacelike
    normal); a = kappa^2 lambda/6, Lambda = -kappa^2 lambda^2/6 (Lambda_4 = 0) or, untuned, -kappa^2 lambda^2/3.  Returns
    (the e^0 part of R, the trace of tau = -(2/kappa^2)(k - q k) + R/(8 pi G_N) at first order, with 8 pi G_N =
    kappa^4 lambda/6 from SMS eq. 19)."""
    import sympy as sp
    kap, lam, e = sp.symbols("kappa lambda epsilon", positive=True)
    q = sp.diag(-1, 1, 1, 1)
    qi = q.inv()
    ks = sp.symbols("k0:10")
    idx = [(i, j) for i in range(4) for j in range(i, 4)]
    k = sp.zeros(4)
    for s_, (i, j) in zip(ks, idx):
        k[i, j] = k[j, i] = s_
    a = kap ** 2 * lam / 6
    K = -a * q + e * k
    Kmix = qi * K
    trK = Kmix.trace()
    KK = (Kmix * Kmix).trace()
    Lam = -kap ** 2 * lam ** 2 / (6 if tuned else 3)
    R = sp.expand(trK ** 2 - KK + 2 * kap ** 2 * Lam)
    R0 = sp.simplify(R.subs(e, 0))
    R1 = sp.simplify(sp.diff(R, e).subs(e, 0))
    ktr = (qi * k).trace()
    tau = -(2 / kap ** 2) * (k - q * ktr)
    tau_tr = (qi * tau).trace()
    GN8pi = kap ** 4 * lam / 6
    return R0, sp.simplify(tau_tr + R1 / GN8pi)


# ------------------------------------------------------------------ W1, W4, W6: Alcubierre
def analytic_profile(one_sided=False):
    """f(r) - f(-r) for Alcubierre's tanh form (zero: f is even, so analytic in r_s^2); one_sided: tanh(sigma(r - R))."""
    import sympy as sp
    r, s, R = sp.symbols("r sigma R", positive=True)
    if one_sided:
        f = sp.tanh(s * (r - R))
    else:
        f = (sp.tanh(s * (r + R)) - sp.tanh(s * (r - R))) / (2 * sp.tanh(s * R))
    return sp.simplify(sp.expand_trig(f - f.subs(r, -r)))


def momentum_order():
    """Alcubierre's G_ty / v and G_yy / v at a wall point as v -> 0: the first is finite (the plane's total momentum is
    O(v)), the second vanishes (O(v^2))."""
    import sympy as sp
    t, x, y, z, v = sp.symbols("t x y z v", real=True)
    F = sp.Function("F")
    f = F(x - v * t, y, z)
    g = sp.zeros(4)
    g[0, 0] = -1 + v ** 2 * f ** 2
    g[0, 1] = g[1, 0] = -v * f
    g[1, 1] = g[2, 2] = g[3, 3] = 1
    _, _, G, _ = signdim.curvature(g, [t, x, y, z])
    rs = sp.sqrt(x ** 2 + y ** 2 + z ** 2)
    fn = (sp.tanh(8 * (rs + 1)) - sp.tanh(8 * (rs - 1))) / (2 * sp.tanh(8))
    pt = {x: 0.6, y: 0.7, z: 0.1}

    def lim(expr):
        e = sp.expand(sp.simplify(expr.subs(t, 0)))
        assert e.coeff(v, 0) == 0
        return float(e.coeff(v, 1).subs(F(x, y, z), fn).doit().subs(pt))

    return lim(G[0, 2]), lim(G[2, 2])


def alcubierre_integrals():
    """int R d^3x and int rho_Alc d^3x for signdim.py's Alcubierre bubble (axisymmetric Simpson on x in [-3, 3],
    s in [0, 3]); and R's range on the grid."""
    a = signdim.alcubierre()
    R, rho = a["R_num"], a["printed_num"]
    nx, ns = GRID
    X0, X1, S1 = -3.0, 3.0, 3.0
    hx, hs = (X1 - X0) / nx, S1 / ns
    w = lambda n, i: 1 if i in (0, n) else (4 if i % 2 else 2)
    IR = Irho = 0.0
    rmin, rmax = float("inf"), -float("inf")
    for i in range(nx + 1):
        xx = X0 + i * hx + 1e-7
        for j in range(ns + 1):
            s = j * hs + 1e-7
            wt = w(nx, i) * w(ns, j) * 2 * math.pi * s
            rv = R(xx, s, 0.0)
            IR += wt * rv
            Irho += wt * rho(xx, s, 0.0)
            rmin, rmax = min(rmin, rv), max(rmax, rv)
    return IR * hx * hs / 9, Irho * hx * hs / 9, rmin, rmax


def compute():
    IR, Irho, rmin, rmax = alcubierre_integrals()
    E_plus = IR / (8 * math.pi)                               # G_N = +1 (positive tension), geometric units
    nec, tr = nec_integrated()
    R0, gauss_res = gauss_trace()
    R0u, _ = gauss_trace(tuned=False)
    gty, gyy = momentum_order()
    return {"int_R": IR, "int_rho_alc": Irho, "int_R_over_minus16pi_int_rho": IR / (-16 * math.pi * Irho),
            "R_min": rmin, "R_max": rmax,
            "E_brane_plus_over_abs_E_alc": E_plus / abs(Irho), "E_brane_minus_sign": -1,
            "laue_residual": str(laue_boosted()), "laue_residual_pressure": str(laue_boosted(False)),
            "nec_integrated": str(nec), "trace_integrated": str(tr),
            "gauss_R0": str(R0), "gauss_trace_residual": str(gauss_res), "gauss_R0_untuned": str(R0u),
            "even_residual": str(analytic_profile()), "even_residual_one_sided": str(analytic_profile(True)),
            "G_ty_over_v": gty, "G_yy_over_v": gyy}


def report():
    d = compute()
    print("bulkwarp.py -- the bulk (BULK4-O6, M item 79), by deduction (not verified; not seated)\n")
    print("W1 Alcubierre's profile is even in r_s (residual %s): analytic, so Dahia-Romero embed a patch in a vacuum "
          "Einstein bulk; the plane's matter is then fixed by the embedding" % d["even_residual"])
    print("W2 Gauss-Codazzi: R's zeroth order %s (Randall-Sundrum tuning); the plane's matter's trace = -R/(8 pi G_N) "
          "(residual %s); E drops out" % (d["gauss_R0"], d["gauss_trace_residual"]))
    print("W3 conserved, localised, comoving: int tau_kk = %s, int trace = %s; boosted body residual %s" % (
        d["nec_integrated"], d["trace_integrated"], d["laue_residual"]))
    print("W4 int R d^3x = %.4f = -16 pi int rho_Alc x %.6f > 0; on a positive-tension plane E = %.3f |E_Alc|" % (
        d["int_R"], d["int_R_over_minus16pi_int_rho"], d["E_brane_plus_over_abs_E_alc"]))
    print("W5 on a negative-tension plane (ours under H-RS1) E < 0: matter keeping the NEC cannot carry a slow warp in a "
          "vacuum bulk, whatever its Weyl curvature")
    print("W6 R ranges %.1f to %.1f: dust alone fails where R < 0; pointwise sufficiency OPEN" % (d["R_min"], d["R_max"]))
    print("W7 evaded by bulk fields (F), superluminal speed, radiating or unlocalised matter, a thick brane: OPEN")


def selftest():
    n_pass = n_fail = n_ctl = 0
    structural = []

    def chk(label, ok, ctl=False):
        nonlocal n_pass, n_fail, n_ctl
        n_ctl += ctl
        n_pass += bool(ok)
        n_fail += (not ok)
        print("  %s %s%s" % ("ok  " if ok else "FAIL", "CONTROL: " if ctl else "", label))

    d = compute()
    chk("W3: a self-stressed body (divergence-free stress) boosted to v = 3/5 obeys int tau^mu_mu = (v^2 - 1) int tau_00 "
        "(residual %s)" % d["laue_residual"], d["laue_residual"] == "0")
    chk("with a pressure that is not divergence-free it does not (residual %s)" % d["laue_residual_pressure"],
        d["laue_residual_pressure"] != "0", ctl=True)
    chk("W2: with the Randall-Sundrum tuning R has no zeroth-order part (%s), and the Gauss-Codazzi trace of the plane's "
        "matter equals SMS eq. 17's -R/(8 pi G_N) (residual %s)" % (d["gauss_R0"], d["gauss_trace_residual"]),
        d["gauss_R0"] == "0" and d["gauss_trace_residual"] == "0")
    chk("untuned (Lambda = -kappa^2 lambda^2/3) a zeroth-order curvature %s remains" % d["gauss_R0_untuned"],
        d["gauss_R0_untuned"] != "0", ctl=True)
    chk("W4: int R d^3x = %.4f > 0 and equals -16 pi int rho_Alc (ratio %.8f), rho_Alc being Natario's printed form" % (
        d["int_R"], d["int_R_over_minus16pi_int_rho"]),
        d["int_R"] > 0 and abs(d["int_R_over_minus16pi_int_rho"] - 1) < 1e-6)
    chk("W1: Alcubierre's form function is even in r_s (residual %s), so analytic in r_s^2" % d["even_residual"],
        d["even_residual"] == "0")
    chk("a one-sided tanh profile is not (residual nonzero)", d["even_residual_one_sided"] != "0", ctl=True)
    chk("W2: Alcubierre's total G_ty is O(v) (G_ty/v -> %.3f as v -> 0): the plane's momentum must be carried by E, so "
        "the plane's matter can be chosen O(v^2)" % d["G_ty_over_v"], abs(d["G_ty_over_v"]) > 1e-3)
    chk("while G_yy is O(v^2) (G_yy/v -> %.1e)" % d["G_yy_over_v"], abs(d["G_yy_over_v"]) < 1e-12, ctl=True)
    chk("W6: R takes both signs across the wall (%.2f to %.2f): dust alone would need negative density where R < 0" % (
        d["R_min"], d["R_max"]), d["R_min"] < 0 < d["R_max"])
    structural.append("W3's integrated null projection int tau_kk = %s and trace %s: algebra on the conservation "
                      "identities" % (d["nec_integrated"], d["trace_integrated"]))
    structural.append("W4: E = int R/(8 pi G_N) = %.4f |E_Alc| for G_N > 0 (leading order in v); for G_N < 0 the sign "
                      "flips -- the test fails on a negative-tension plane" % d["E_brane_plus_over_abs_E_alc"])
    structural.append("int R = (v^2/2) int (f_y^2 + f_z^2) because the remaining terms of R are total x-derivatives; "
                      "this is why int R = -16 pi int rho_Alc")
    structural.append("W7: P-VACUUM-BULK is the whole content of the test's scope -- bulk fields enter the scalar Gauss "
                      "and Codazzi equations and are not covered")
    for s_ in structural:
        print("  STRUCTURAL: " + s_)
    print("bulkwarp.py: %d/%d checks pass, %d of them controls; %d STRUCTURAL printed, not counted" % (
        n_pass, n_pass + n_fail, n_ctl, len(structural)))
    return n_fail == 0


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    elif "--json" in sys.argv:
        print(json.dumps(compute(), indent=1, default=str))
    else:
        report()
