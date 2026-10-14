#!/usr/bin/env python3
"""modelc.py -- MODEL C (M-RULINGS 181/182): the two-sided bridge.  Do the two planes' balance conditions fix the
bridge's size against ell (an equality), leave a modulus, or admit no solution?  Computed and deduced; scratch, not
verified, not seated.

M's words (verbatim in the rulings file, never paraphrased as M's): 179/180 "We know the corridor *does not sit on
either position's plane, it only bridges them. So one could surmise that the corridor is exclusive to the bulk."; 181
"this bears directly on B4d, and requires priority"; 182 "If I had to guess, I would go with C"; 136 (3) "it lives in
a dimension that connects the positions. It is a bridge, not a physical place"; 162 (one object holding both mouths
and the throat at once, fixed size); 166 "Both planes at once"; 139 (1) "yes" (position 2's plane negative, a quarter
of ours; ours positive); clause (B) (ours at the Randall-Sundrum tension, the plane free of matter); 138 (each
universe under its own laws); 141 (the planes are static); 184 "There are no matter free planes".

THE MODEL.  5D Einstein gravity, Lambda = -6/ell^2 on each vacuum region.  The bridge is the maximally extended
Schwarzschild-AdS5 family f(r) = k + r^2/ell_s^2 - mu/r^2 (k = 1 the literal spherical case; k = 0 the planar black
brane, whose static planes are FLAT; k = -1 hyperbolic, which holds the one neutral extremal member).  Its two
exteriors I and III share (ell_s, mu) (Birkhoff with Lambda, standard-not-READ; Lambda constant on a connected vacuum
region by the contracted Bianchi identity, standard-not-READ).  Our plane is static at r = R1 in I, position 2's at
r = R2 in III, each with the bridge on its inner side (the region toward the horizon), so the bridge lies between them
(179, 136 (3), 166).  Beyond each plane: either its mirror image (the board's H-Z2-PIECES convention, one-sided factor
nu = 2/kappa^2) or its own universe's vacuum bulk (138): pure AdS with its own ell_i (mu_i = 0 by 129/130: the
corridor adds nothing to either position), kept on the side r < R ("decaying", eps = +1) or r > R ("growing",
eps = -1).  The planes share the bridge's symmetry (the board's H-SYMMETRIC-PLANES).

THE JUNCTION (C1, computed twice).  Israel, normal into each kept side: S^a_b = -(1/kappa^2) sum_sides (K^a_b - d K).
For a static plane, with lam = kappa^2 sigma / 3 and the inner (bridge) side eps = +1:
    TENSION  lam R = sum_j eps_j sqrt(f_j(R))
    BALANCE  B(R) := sum_j eps_j (k - 2 mu_j/R^2) / sqrt(f_j(R)) = 0      (equivalently: the traceless parts cancel)
and, under 184 (matter on the plane), kappa^2 (rho_m + p_m) = B(R)/R -- the balance function IS the plane's NEC sum.

  C0  owners (import by path): multiplane.py M4 (+4/3, -1/3; ratio -1/4) through b6_k.py's loader; b6_k.compute (the
      ratio 3/4) under --full; b4d_stage6.sigma_over_rs; sim2_facing.israel, t5c, lemma_t, near_horizon, throat_bulk.
  C1  the junction from a 5D Christoffel computation, and again from the energy equation of a moving plane (the
      turning point with zero acceleration); the RS control; the owners agree.
  C2  FLAT PLANES (k = 0): B = -2 mu/(R^2 sqrt f_s) < 0 for every mu > 0, every tension, every ell, every outer side:
      no static plane beside a black brane.  Control mu = 0: B == 0, every R balances.
  C3  MIRRORED PLANES, every k: static iff k = 2 mu/R^2; only k = 1 has it outside a horizon, at mu = R^2/2, with
      (kappa^2 sigma/6)^2 = 1/ell^2 + 1/(2R^2): super-critical; RS reached only as mu -> infinity; unstable.
  C4  THE SIGN CONDITION: a mirrored plane with the bridge on its side reads sigma = (6/kappa^2) sqrt(f)/R > 0 in
      every exterior; position 2's negative plane needs a two-sided plane whose far side is "growing".
  C5  k = 1, two-sided, closed forms: ours (decaying outer AdS(L1)) is always strictly above the critical tension
      1/ell_s + 1/ell_1; position 2's (growing outer AdS(L2)) is static iff ell_2 < ell_s, and is then negative.
  C6  THE TWO PLANES TOGETHER, under every recorded convention (one ell; M4's ell_2 = 4 ell/3; stage 6's 3 ell; stage
      7's 6 ell; ratio -1/4 or -1/8): NO SOLUTION.  Off-convention branch (ell_1 > ell_s > ell_2, RS read at ell_s or
      at ell_1): a one-parameter family -- mu/ell_s^2 = L1^2/(L1^2 - 1) etc. -- a modulus, not an equality.
  C7  k = -1 and the neutral extremal member mu = -ell^2/4: ours positive needs mu > 0, position 2's negative needs
      mu < 0: no solution; the extremal exterior holds a negative plane for 1/sqrt3 < ell_2/ell_s < 1 only.
  C8  THE THROATS: in AdS2 x X3 (the extremal near-horizon) a plane at fixed AdS2 position carries pressure only,
      never a tension (pure tension only at the centre, sigma = 0); AdS2(ell/2) x H3(ell/sqrt2) is the only vacuum
      product; the board's AdS2 x S2 is a 4D slice whose 5D column (sim2_facing.throat_bulk) ends singular -- no
      second end in the bulk.
  C9  charged extremal (outside clause (B): a bulk Maxwell field): mirrored static planes are positive (C4) and, for
      k = 0, sit exactly on the extremal horizon.
  C10 the controls (mu = 0) and the force: a flat plane at rest beside a black brane falls toward the bridge.
  C11 under 184 (matter on both planes): flat planes need NEC-violating matter; spherical planes leave a modulus.
Stdlib + sympy + mpmath (numpy/scipy via the sim2 owner).  python3 modelc.py [--selftest] [--full]
"""
import contextlib
import importlib.util
import io
import os
import sys
import time

import mpmath as mp
import sympy as sp

D68 = "/home/user/Claude-Method-Works/research/warp-drive/docket68"
LEM = os.path.join(D68, "lemmas")
WD = os.path.dirname(D68)


def _load(path, key):
    saved = list(sys.path)
    sys.path[:0] = [os.path.dirname(path), D68, WD]
    try:
        spec = importlib.util.spec_from_file_location(key, path)
        mod = importlib.util.module_from_spec(spec)
        with contextlib.redirect_stdout(io.StringIO()):
            spec.loader.exec_module(mod)
    finally:
        sys.path[:] = saved
    return mod


_OWN = {}


def owners():
    if not _OWN:
        b6 = _load(os.path.join(LEM, "b6_k.py"), "mc_b6k")
        _OWN["b6"] = b6
        _OWN["mp"] = b6._load(os.path.join(D68, "bulk", "multiplane.py"), "mc_multiplane")
        _OWN["s6"] = _load(os.path.join(LEM, "b4d_stage6.py"), "mc_stage6")
        _OWN["s2"] = _load(os.path.join(LEM, "sim2_facing.py"), "mc_sim2")
    return _OWN


# ---------------------------------------------------------------------------------------------- C0 the conventions
def conventions(full=False):
    """139's quarter in the board's three statements.  M4 (multiplane.py): tensions +4/3 and -1/3 of lambda_RS(k_R),
    ratio -1/4 (KDERIVE, b6_k); per sheet (stage 7 K5; 174 (2)'s rule: one per-sheet count reproducing M4's geometry):
    ours (mirrored, both sides k_L) lam = 2 k_L, position 2's (two-sided, k_L growing toward the slab, k_R decaying
    beyond) lam = k_R - k_L = -k_L/4: ratio -1/8."""
    o = owners()
    m4 = o["mp"].m4()
    kL = o["mp"].kL
    kR = m4["kR"]
    ratio_m4 = sp.simplify(m4["tau2_over_rs"] / m4["tau1_over_rs"])
    lam_ours = 2 * kL                      # mirrored, two decaying sides at k_L
    lam_p2_sheet = (-1) * kL + 1 * kR      # eps = -1 toward the slab (growing), +1 beyond (decaying)
    ratio_sheet = sp.simplify(lam_p2_sheet / lam_ours)
    out = {"m4": m4, "ratio_m4": ratio_m4, "ratio_sheet": ratio_sheet, "kR_over_kL": sp.simplify(kR / kL),
           "ell2_over_ell_M4": sp.simplify(kL / kR)}
    if full:
        t = time.time()
        d = o["b6"].compute()
        out["b6_ratio"] = d["ratio"]
        out["b6_seconds"] = time.time() - t
    return out


# ---------------------------------------------------------------------------------------------- C1 the junction
def junction_direct():
    """K_ab of r = R in ds^2 = -f dt^2 + dr^2/f + r^2 gamma_k (gamma_k conformally flat, curvature k), from the
    Christoffels, for the unit normal n^r = s sqrt(f) (s = +1 toward increasing r).  Returns K^t_t, K^x_x, the
    off-diagonal residue, and the static tension/balance conditions for two sides."""
    t, r, x1, x2, x3 = sp.symbols("t r x1 x2 x3", real=True)
    k = sp.Symbol("k", real=True)
    s = sp.Symbol("s", real=True)
    f = sp.Function("f")(r)
    conf = (1 + k * (x1**2 + x2**2 + x3**2) / 4) ** 2
    X = [t, r, x1, x2, x3]
    g = sp.diag(-f, 1 / f, r**2 / conf, r**2 / conf, r**2 / conf)
    gi = sp.diag(*[1 / g[i, i] for i in range(5)])
    Gam = [[[sp.simplify(sum(gi[a, d] * (sp.diff(g[d, b], X[c]) + sp.diff(g[d, c], X[b]) - sp.diff(g[b, c], X[d]))
                             for d in range(5)) / 2) for c in range(5)] for b in range(5)] for a in range(5)]
    n_low = [0, s / sp.sqrt(f), 0, 0, 0]
    tang = [0, 2, 3, 4]
    K = {}
    for a in tang:
        for b in tang:
            K[(a, b)] = sp.simplify(sp.diff(n_low[b], X[a]) - sum(Gam[c][a][b] * n_low[c] for c in range(5)))
    Ktt = sp.simplify(gi[0, 0] * K[(0, 0)])
    Kxx = sp.simplify(gi[2, 2] * K[(2, 2)])
    offdiag = [K[(a, b)] for a in tang for b in tang if a != b]
    return {"Ktt": Ktt, "Kxx": Kxx, "Kyy": sp.simplify(gi[3, 3] * K[(3, 3)]), "offdiag_zero": all(sp.simplify(z) == 0
                                                                                                 for z in offdiag),
            "f": f, "r": r, "s": s, "k": k}


def junction_conditions(sides, kappa2=1):
    """sides: list of (eps, f(R), f'(R)) at the plane, eps = +1 for a kept side r < R (normal toward decreasing r),
    -1 for r > R.  Returns rho, p (S^t_t = -rho, S^x_x = p) from Israel S = -(1/kappa^2) sum (K - d K), with
    K^t_t = -eps f'/(2 sqrt f), K^x_x = -eps sqrt f / R (junction_direct with s = -eps)."""
    R = sp.Symbol("R", positive=True)
    Stt = 0
    Sxx = 0
    for eps, fv, fpv in sides:
        ct = -eps * fpv / (2 * sp.sqrt(fv))
        cx = -eps * sp.sqrt(fv) / R
        Ktr = ct + 3 * cx
        Stt += -(ct - Ktr) / kappa2
        Sxx += -(cx - Ktr) / kappa2
    return {"rho": sp.simplify(-Stt), "p": sp.simplify(Sxx), "R": R}


def balance_function(sides, R, k):
    """B(R) = sum eps_j (2 f_j - R f_j')/(2 sqrt f_j) = R sum eps_j (sqrt f/R - f'/(2 sqrt f))."""
    return sum(eps * (2 * fv - R * fpv) / (2 * sp.sqrt(fv)) for eps, fv, fpv in sides)


def junction_check():
    """C1: (a) the Christoffel K matches the coded K; (b) Israel's rho + p is B/R; (c) the moving-plane route gives
    the same balance; (d) RS control; (e) owners b4d_stage6.sigma_over_rs and sim2_facing.israel agree."""
    d = junction_direct()
    f, r, s = d["f"], d["r"], d["s"]
    coded_t = s * sp.diff(f, r) / (2 * sp.sqrt(f))
    coded_x = s * sp.sqrt(f) / r
    a_ok = sp.simplify(d["Ktt"] - coded_t) == 0 and sp.simplify(d["Kxx"] - coded_x) == 0 and \
        sp.simplify(d["Kyy"] - coded_x) == 0 and d["offdiag_zero"]
    # (b) symbolic two sides
    R = sp.Symbol("R", positive=True)
    e1, e2 = sp.symbols("e1 e2", real=True)
    F1, F2, P1, P2 = sp.symbols("F1 F2 P1 P2", positive=True)
    jc = junction_conditions([(e1, F1, P1), (e2, F2, P2)])
    Rj = jc["R"]
    B = balance_function([(e1, F1, P1), (e2, F2, P2)], Rj, None)
    b_ok = sp.simplify(jc["rho"] + jc["p"] - B / Rj) == 0
    rho_ok = sp.simplify(jc["rho"] - 3 * (e1 * sp.sqrt(F1) + e2 * sp.sqrt(F2)) / Rj) == 0
    # (c) moving plane: K^x_x = s sqrt(f + Rdot^2)/R (from Gamma^r_xx = -f r/conf, n_r = s Tdot, f Tdot =
    # sqrt(f + Rdot^2)); energy eq E(R, X) = sum eps sqrt(f + X) - lam R = 0, X = Rdot^2.  Rest with zero acceleration:
    # X = 0 and dX/dR = 0, i.e. E = 0 and E_R = 0.
    lam, Xs = sp.symbols("lam X", real=True)
    fs = [sp.Function("f1"), sp.Function("f2")]
    E = e1 * sp.sqrt(fs[0](R) + Xs) + e2 * sp.sqrt(fs[1](R) + Xs) - lam * R
    ER = sp.diff(E, R).subs(Xs, 0)
    E0 = E.subs(Xs, 0)
    lam_sol = sp.solve(E0, lam)[0]
    route2 = sp.simplify(ER.subs(lam, lam_sol) * R)            # = -(sum eps (sqrt f - R f'/(2 sqrt f)))
    Bm = balance_function([(e1, fs[0](R), sp.diff(fs[0](R), R)), (e2, fs[1](R), sp.diff(fs[1](R), R))], R, None)
    c_ok = sp.simplify(route2 + Bm) == 0
    # the moving K^x_x itself, from the Christoffel symbols with a general velocity
    T = sp.Function("T")
    tau = sp.Symbol("tau")
    Rt = sp.Function("Rt")(tau)
    Td = sp.Symbol("Td", positive=True)
    Rd = sp.Symbol("Rd", real=True)
    fr = sp.Function("f")(r)
    Gam_r_xx = -fr * r                    # Gamma^r_xx at x = 0 (conf = 1)
    n_r = s * Td
    Kxx_mov = sp.simplify(-Gam_r_xx * n_r / r**2)          # K^x_x = g^xx K_xx = -Gamma^r_xx n_r / r^2
    Tdot = sp.sqrt(fr + Rd**2) / fr
    c2_ok = sp.simplify(Kxx_mov.subs(Td, Tdot) - s * sp.sqrt(fr + Rd**2) / r) == 0
    # (d) RS control: planar pure AdS, two decaying sides
    ell = sp.Symbol("ell", positive=True)
    fA = R**2 / ell**2
    rs = junction_conditions([(1, fA, sp.diff(fA, R)), (1, fA, sp.diff(fA, R))])
    d_ok = sp.simplify(rs["rho"] - 6 / ell) == 0 and sp.simplify(rs["p"] + 6 / ell) == 0
    # mutation: flip one side's orientation -> tension 0 (the RS value is lost): the control can fail
    rs_mut = junction_conditions([(1, fA, sp.diff(fA, R)), (-1, fA, sp.diff(fA, R))])
    d_mut = sp.simplify(rs_mut["rho"]) == 0
    # (e) owners.  Z2 plane in SAdS (k = 1, ell = 1) at the static point mu = R^2/2, R = 3/2: a = K^x_x = K^t_t there.
    o = owners()
    Rv = sp.Rational(3, 2)
    muv = Rv**2 / 2
    fv = 1 + Rv**2 - muv / Rv**2
    fpv = 2 * Rv + 2 * muv / Rv**3
    ct = -fpv / (2 * sp.sqrt(fv))
    cx = -sp.sqrt(fv) / Rv
    umbilic = sp.simplify(ct - cx) == 0
    s_over = o["s6"].sigma_over_rs(cx, cx, sp.Integer(1))            # sigma / lambda_RS(ell = 1)
    mine = sp.sqrt(fv) / Rv                                           # kappa^2 sigma/6 at ell = 1
    e_ok = umbilic and sp.simplify(s_over - mine) == 0
    rho_i, ps = o["s2"].israel([ct, cx, cx, cx], nu=2)                # nu = 2/kappa^2, kappa^2 = 1
    mine_rp = junction_conditions([(1, fv, fpv), (1, fv, fpv)])
    e2_ok = sp.simplify(rho_i - mine_rp["rho"].subs(mine_rp["R"], Rv)) == 0 and \
        all(sp.simplify(pv - mine_rp["p"].subs(mine_rp["R"], Rv)) == 0 for pv in ps)
    return {"direct": a_ok, "rho_plus_p_is_B": b_ok, "rho_formula": rho_ok, "moving_route": c_ok,
            "moving_Kxx": c2_ok, "rs_control": d_ok, "rs_mutation_kills": d_mut, "owner_stage6": e_ok,
            "owner_israel": e2_ok, "static_example_tension": mine}


# ---------------------------------------------------------------------------------------------- the family
def f_of(k, ell, mu, R):
    return k + R**2 / ell**2 - mu / R**2


def fp_of(k, ell, mu, R):
    return 2 * R / ell**2 + 2 * mu / R**3


def B_two(k, ells, mus, epss, R):
    """Balance function for the bridge side (eps = +1, ell_s, mu) and one outer side."""
    sides = [(e, f_of(k, l, m, R), fp_of(k, l, m, R)) for e, l, m in zip(epss, ells, mus)]
    return sp.simplify(balance_function(sides, R, k)), sides


# ---------------------------------------------------------------------------------------------- C2 flat planes
def flat():
    R, mu, ls, lo = sp.symbols("R mu ell_s ell_o", positive=True)
    out = {}
    for name, ells, mus, epss in [("mirror", (ls, ls), (mu, mu), (1, 1)), ("outer decaying", (ls, lo), (mu, 0), (1, 1)),
                                  ("outer growing", (ls, lo), (mu, 0), (1, -1))]:
        B, _ = B_two(0, ells, mus, epss, R)
        out[name] = B
    claim = -2 * mu / (R**2 * sp.sqrt(R**2 / ls**2 - mu / R**2))
    ok = all(sp.simplify(out[n] - m * claim) == 0 for n, m in [("mirror", 2), ("outer decaying", 1),
                                                                 ("outer growing", 1)])
    ctrl = all(sp.simplify(v.subs(mu, 0)) == 0 for v in out.values())
    # the force: a plane momentarily at rest, R'' = (B/R) / sum eps/sqrt f  (C10); mirror: sum = 2/sqrt f > 0
    acc_mirror = sp.simplify((out["mirror"] / R) / (2 / sp.sqrt(R**2 / ls**2 - mu / R**2)))
    # at exactly the RS tension (lam = 2/ell_s, mirrored): energy eq 2 sqrt(f + Rdot^2) = lam R -> Rdot^2 = mu/R^2
    rdot2_rs = sp.simplify((2 * R / ls) ** 2 / 4 - (R**2 / ls**2 - mu / R**2))
    rdot2_rs_k1 = sp.simplify((2 * R / ls) ** 2 / 4 - (1 + R**2 / ls**2 - mu / R**2))
    return {"B": out, "B_is_minus_2mu": ok, "control_mu0": ctrl, "acc_mirror": acc_mirror, "rdot2_rs": rdot2_rs,
            "rdot2_rs_k1": rdot2_rs_k1}


# ---------------------------------------------------------------------------------------------- C3 mirrored planes
def mirrored():
    R, ell = sp.symbols("R ell", positive=True)
    mu = sp.Symbol("mu", real=True)
    out = {}
    for k in (1, 0, -1):
        B, _ = B_two(k, (ell, ell), (mu, mu), (1, 1), R)
        num = sp.factor(sp.numer(sp.together(B)))
        sol = sp.solve(sp.Eq(k * R**2 - 2 * mu, 0), mu)
        out[k] = {"B": B, "root": sol}
    # k = 1: mu = R^2/2; tension^2
    k = 1
    mus = R**2 / 2
    lam6sq = sp.simplify(f_of(1, ell, mus, R) / R**2)                     # (kappa^2 sigma / 6)^2
    excess = sp.simplify(lam6sq - 1 / ell**2)
    # the bridge size against the tension's excess: mu = 1/(4 (lam6^2 - 1/ell^2))
    x = sp.Symbol("x", positive=True)                                      # x = (kappa^2 sigma/6)^2 - 1/ell^2
    mu_of_excess = sp.simplify(mus.subs(R, sp.sqrt(1 / (2 * x))))
    # horizon check for k = 1: f(R) > 0 at mu = R^2/2
    f_static = sp.simplify(f_of(1, ell, mus, R))
    # stability: V = f - lam6^2 R^2 (Rdot^2 = -V), V'' at the static point
    lam6 = sp.Symbol("l6", positive=True)
    Rv = sp.Symbol("Rv", positive=True)
    mu0 = sp.Symbol("mu0", positive=True)
    V = f_of(1, ell, mu0, Rv) - lam6**2 * Rv**2
    Vpp = sp.simplify(sp.diff(V, Rv, 2).subs({mu0: Rv**2 / 2, lam6: sp.sqrt(1 / ell**2 + 1 / (2 * Rv**2))}))
    # k = -1: mu = -R^2/2 must lie at or below extremality; exterior impossible
    l = sp.Symbol("l", positive=True)
    rp2 = lambda m: (l**2 / 2) * (1 + sp.sqrt(1 + 4 * m / l**2))           # outer horizon^2, k = -1
    Rsq = sp.Symbol("Rsq", positive=True)
    # need R^2 > r_+^2 with mu = -R^2/2 and 1 + 4mu/l^2 >= 0  -> R^2 <= l^2/2 and R^2 > (l^2/2)(1 + sqrt(1 - 2R^2/l^2))
    gap = sp.simplify(rp2(-Rsq / 2) - Rsq)
    return {"roots": {k: out[k]["root"] for k in out}, "B": {k: out[k]["B"] for k in out}, "lam6sq": lam6sq,
            "excess": excess, "mu_of_excess": mu_of_excess, "f_static": f_static, "Vpp": Vpp, "km1_gap": gap}


# ---------------------------------------------------------------------------------------------- C4 sign condition
def sign_condition():
    """Mirrored plane, bridge side kept: kappa^2 sigma / 6 = sqrt(f)/R > 0 wherever f > 0.  T5c contrast: the static
    Gaussian chart from P1 reaches the bifurcation surface (A = f -> 0), so T5c's hypothesis (nearest approach attained
    in the static chart) fails in model C; the mirrored P2 then reads +sqrt(f) ell / R, not <= -1."""
    o = owners()
    t5 = o["s2"].t5c(sp.Rational(1))
    lt = o["s2"].lemma_t()
    R, ell, mu = sp.symbols("R ell mu", positive=True)
    jc = junction_conditions([(1, f_of(1, ell, mu, R), fp_of(1, ell, mu, R))] * 2)
    # depth from a plane at R to the horizon along the t = 0 slice: finite for a simple root (k = 1 example)
    r = sp.Symbol("r", positive=True)
    fnum = f_of(1, 1, sp.Rational(1, 2), r)
    rh = sp.nsolve(fnum, r, 0.7)
    depth = mp.quad(lambda z: 1 / mp.sqrt(1 + z**2 - mp.mpf(1) / 2 / z**2), [rh, 1, 2])
    return {"t5c_bound": t5["s2_max"], "lemma_t_fixed_point": lt["fixed_point"], "rho_mirror": jc["rho"],
            "rho_mirror_claim": sp.simplify(jc["rho"] - 6 * sp.sqrt(f_of(1, ell, mu, jc["R"])) / jc["R"]) == 0,
            "depth_to_bifurcation_example": depth, "rh_example": rh}


# ---------------------------------------------------------------------------------------------- C5 k = 1 closed forms
U, L = sp.symbols("u L", positive=True)
A_ = 1 + U / L**2
S_ = sp.sqrt(1 + 8 * A_ + 16 * A_ * U)
MU_OURS = U * ((4 * A_ - 1) + S_) / (8 * A_)
LAM_OURS = ((4 * A_ - 1) + S_) / (4 * sp.sqrt(A_ * U))
MU_P2 = U * ((4 * A_ - 1) - S_) / (8 * A_)
LAM_P2 = -((4 * A_ - 1) - S_) / (4 * sp.sqrt(A_ * U))


def k1_closed():
    """ell_s = 1, u = R^2, L = ell_outer/ell_s.  The squared balance (2mu/u - 1)^2 (1 + u/L^2) = 1 + u - mu/u is a
    quadratic in mu; its + root is ours (u < 2mu, decaying outer), its - root position 2's (u > 2mu, growing outer)."""
    mu = sp.Symbol("mu", positive=True)
    quad = sp.expand(((2 * mu - U) ** 2 * A_ - U**2 * (1 + U) + mu * U))
    roots_ok = all(sp.simplify(quad.subs(mu, m)) == 0 for m in (MU_OURS, MU_P2))
    # unsquared balance and tension for each branch, checked at sample points (exact rationals where possible)
    samples = [(sp.Rational(1, 3), sp.Rational(1, 2)), (sp.Integer(2), sp.Integer(3)), (sp.Rational(7, 5), sp.Integer(1))]
    br_ours = []
    br_p2 = []
    for uv, Lv in samples:
        m = MU_OURS.subs({U: uv, L: Lv})
        fs = 1 + uv - m / uv
        fo = 1 + uv / Lv**2
        br_ours.append(sp.N((1 - 2 * m / uv) / sp.sqrt(fs) + 1 / sp.sqrt(fo), 30))
        lam = (sp.sqrt(fs) + sp.sqrt(fo)) / sp.sqrt(uv)
        br_ours.append(sp.N(lam - LAM_OURS.subs({U: uv, L: Lv}), 30))
    for uv, Lv in [(sp.Integer(3), sp.Rational(1, 2)), (sp.Integer(10), sp.Rational(3, 4))]:
        m = MU_P2.subs({U: uv, L: Lv})
        fs = 1 + uv - m / uv
        fo = 1 + uv / Lv**2
        br_p2.append(sp.N((1 - 2 * m / uv) / sp.sqrt(fs) - 1 / sp.sqrt(fo), 30))
        lam = (sp.sqrt(fs) - sp.sqrt(fo)) / sp.sqrt(uv)
        br_p2.append(sp.N(lam - LAM_P2.subs({U: uv, L: Lv}), 30))
    # ours strictly above critical 1 + 1/L: with v = sqrt(u)/L, w = v sqrt(1 + v^2):
    # 4 sqrt(A u)(lam - 1 - 1/L) = 3 + 4v^2 + sqrt(9 + 8v^2 + 16 L^2 w^2) - 4 L w - 4 w  >  3 + 4 v^2 - 4 w  > 0
    v = sp.Symbol("v", positive=True)
    lower_sq_gap = sp.expand((3 + 4 * v**2) ** 2 - 16 * v**2 * (1 + v**2))           # = 9 + 8 v^2
    N_expr = sp.simplify((4 * sp.sqrt(A_ * U) * (LAM_OURS - 1 - 1 / L)).subs(U, L**2 * v**2))
    N_claim = 3 + 4 * v**2 + sp.sqrt(9 + 8 * v**2 + 16 * L**2 * v**2 * (1 + v**2)) - 4 * (L + 1) * v * sp.sqrt(1 + v**2)
    N_ok = all(abs(sp.N((N_expr - N_claim).subs({v: vv, L: lv}), 30)) < 1e-25
               for vv, lv in [(sp.Rational(1, 3), sp.Rational(1, 2)), (sp.Integer(2), sp.Integer(5)),
                              (sp.Rational(9, 4), sp.Rational(7, 3))])
    lim_ours = sp.limit(LAM_OURS.subs(L, 2), U, sp.oo)
    # position 2 exists (mu > 0) iff (4A - 1)^2 > 1 + 8A + 16 A u  iff  A - 1 > u  iff  L < 1
    exist = sp.simplify(sp.expand((4 * A_ - 1) ** 2 - (1 + 8 * A_ + 16 * A_ * U)) - 16 * A_ * (A_ - 1 - U))
    lim_p2 = sp.limit(LAM_P2.subs(L, sp.Rational(1, 2)), U, sp.oo)
    return {"roots_ok": roots_ok, "balance_res_ours": br_ours, "balance_res_p2": br_p2, "lower_sq_gap": lower_sq_gap,
            "N_ok": N_ok, "lim_ours_L2": lim_ours, "exist_identity_zero": exist == 0, "lim_p2_Lhalf": lim_p2}


def rs_at_ell_s(L1):
    """Ours at lam = 2/ell_s (RS read at the bridge's ell) with outer AdS(L1): u1 = mu = L1^2/(L1^2 - 1), L1 > 1."""
    u1 = L1**2 / (L1**2 - 1)
    return {"u1": u1, "mu": sp.simplify(MU_OURS.subs({U: u1, L: L1})), "lam": sp.simplify(LAM_OURS.subs({U: u1, L: L1}))}


def rs_at_ell_1(L1):
    """Ours at lam = 2/ell_1 with outer AdS(L1), L1 < 1: w = sqrt(u/(L1^2 + u)) solves w^2 + (L1^2 - 5) w + 3 = 0
    (the smaller root), u1 = L1^2 w^2/(1 - w^2), mu = w u1."""
    w = ((5 - L1**2) - sp.sqrt((5 - L1**2) ** 2 - 12)) / 2
    u1 = sp.simplify(L1**2 * w**2 / (1 - w**2))
    return {"w": w, "u1": u1, "mu": sp.simplify(MU_OURS.subs({U: u1, L: L1})),
            "lam": sp.simplify(LAM_OURS.subs({U: u1, L: L1}))}


def p2_given(mu, lam_target):
    """Position 2's plane (growing outer AdS(L2)) with given bridge mu and tension lam_target < 0: the quartic
    4 mu^2 (u + u^2 - mu) = lam^2 u^2 (u - 2 mu)^2, then L2^2 = u/(Q^2 - 1), Q = |lam| u^(3/2)/(2 mu).  Returns every
    admissible root (u > 2 mu, Q > 1, the unsquared balance and tension met)."""
    u = sp.Symbol("u", positive=True)
    poly = sp.Poly(sp.expand(4 * mu**2 * (u + u**2 - mu) - lam_target**2 * u**2 * (u - 2 * mu) ** 2), u)
    sols = []
    if poly.domain.is_QQ or poly.domain.is_ZZ:
        cands = list(sp.real_roots(poly))                      # exact algebraic roots (CRootOf)
    else:                                                      # radical coefficients: numerical roots, 50 digits
        cands = [z for z in sp.Poly(poly.as_expr().evalf(60), u).nroots(n=50, maxsteps=200)
                 if abs(sp.im(z)) < 1e-40]
        cands = [sp.re(z) for z in cands]
    for rt in cands:
        uv = sp.N(rt, 50)
        if uv <= 2 * sp.N(mu, 50):
            continue
        Q = abs(sp.N(lam_target, 50)) * uv**sp.Rational(3, 2) / (2 * sp.N(mu, 50))
        if Q <= 1:
            continue
        L2 = sp.sqrt(uv / (Q**2 - 1))
        fs = 1 + uv - mu / uv
        fo = 1 + uv / L2**2
        bal = (1 - 2 * mu / uv) / sp.sqrt(fs) - 1 / sp.sqrt(fo)
        ten = (sp.sqrt(fs) - sp.sqrt(fo)) / sp.sqrt(uv) - lam_target
        sols.append({"u2": uv, "L2": sp.N(L2, 30), "R2": sp.N(sp.sqrt(uv), 30), "bal": sp.N(bal, 10),
                     "ten": sp.N(ten, 10), "root": rt})
    return sols


def horizon_k1(mu):
    return sp.sqrt((sp.sqrt(1 + 4 * mu) - 1) / 2)


# ---------------------------------------------------------------------------------------------- C6 the grid
def grid():
    """Every recorded convention, and the off-convention branch.  ell_s = 1 throughout (the bridge's own length)."""
    rows = []
    # (a) the recorded conventions for position 2's outer ell (relative to the bridge's ell_s = ell)
    for name, L2 in [("one ell (ell_2 = ell)", sp.Integer(1)), ("M4/KDERIVE/b6_k (ell_2 = 4 ell/3)", sp.Rational(4, 3)),
                     ("stage 6 J3 (ell_2 = 3 ell)", sp.Integer(3)), ("stage 7 K5 (ell_2 = 6 ell)", sp.Integer(6))]:
        p2_static = bool(L2 < 1)
        rows.append({"convention": name, "L2": L2, "P2_static_possible": p2_static,
                     "ours_at_RS_mirrored": False, "ours_at_RS_two_sided_one_ell": False, "verdict": "NO SOLUTION"})
    # (b) the off-convention branches
    fam = []
    for L1 in (sp.Rational(3, 2), sp.Integer(2), sp.Integer(3), sp.Integer(10)):
        o = rs_at_ell_s(L1)
        for rho in (sp.Rational(1, 4), sp.Rational(1, 8)):
            sols = p2_given(o["mu"], -rho * o["lam"])
            fam.append({"branch": "RS at ell_s", "L1": L1, "mu": o["mu"], "R1": sp.sqrt(o["u1"]),
                        "rh": horizon_k1(o["mu"]), "ratio": -rho, "p2": sols})
    for L1 in (sp.Rational(1, 2), sp.Rational(4, 5)):
        o = rs_at_ell_1(L1)
        for rho in (sp.Rational(1, 4), sp.Rational(1, 8)):
            sols = p2_given(o["mu"], -rho * o["lam"])
            fam.append({"branch": "RS at ell_1", "L1": L1, "mu": sp.N(o["mu"], 20), "R1": sp.N(sp.sqrt(o["u1"]), 20),
                        "rh": sp.N(horizon_k1(o["mu"]), 20), "ratio": -rho, "p2": sols, "lam": o["lam"]})
    # the L1 -> infinity end of the RS-at-ell_s family: mu -> 1
    lim = {rho: p2_given(sp.Integer(1), -2 * rho) for rho in (sp.Rational(1, 4), sp.Rational(1, 8))}
    # the L1 -> 1+ end: mu -> infinity (numerical, mu = 10^4, 10^6)
    big = {(rho, m): p2_given(sp.Integer(m), -2 * rho) for rho in (sp.Rational(1, 4), sp.Rational(1, 8))
           for m in (10**4, 10**6)}
    return {"rows": rows, "family": fam, "L1_inf": lim, "L1_one": big}


# ---------------------------------------------------------------------------------------------- C7 k = -1, extremal
def hyperbolic():
    R, ell, Lo = sp.symbols("R ell L_o", positive=True)
    mu = sp.Symbol("mu", real=True)
    # balance with outer pure hyperbolic AdS(L_o), outer growing: (-1 - 2mu/R^2)/sqrt f_s + 1/sqrt f_o = 0
    # -> sqrt f_s = (1 + 2mu/R^2) sqrt f_o ; tension lam R = sqrt f_s - sqrt f_o = (2 mu/R^2) sqrt f_o: sign(mu)
    u = sp.Symbol("u", positive=True)
    fs = -1 + u - mu / u
    fo = -1 + u / Lo**2
    lam_R = sp.simplify(((1 + 2 * mu / u) * sp.sqrt(fo)) - sp.sqrt(fo))
    # extremal member mu = -1/4 (ell_s = 1): f_s = (u - 1/2)^2 / u; balance -> u (1/L^2 - 1) = 1
    fs_ext = sp.factor(fs.subs(mu, -sp.Rational(1, 4)))
    u_ext = 1 / (1 / Lo**2 - 1)
    lam_ext = sp.simplify(((2 * (-sp.Rational(1, 4)) / u) * sp.sqrt(fo) / sp.sqrt(u)).subs(u, u_ext))
    # check the unsquared balance at a sample L_o = 4/5
    Lv = sp.Rational(4, 5)
    uv = u_ext.subs(Lo, Lv)
    fsv = fs.subs({mu: -sp.Rational(1, 4), u: uv})
    fov = fo.subs({Lo: Lv, u: uv})
    bal = sp.simplify((-1 + sp.Rational(1, 2) / uv) / sp.sqrt(fsv) + 1 / sp.sqrt(fov))
    window_low = sp.solve(sp.Eq(u_ext, sp.Rational(1, 2)), Lo)
    # decaying outer: needs 1 + 2mu/u < 0, i.e. u < -2mu <= 1/2 (mu >= -1/4), but the exterior needs u > u_+ >= 1/2
    return {"lam_R": lam_R, "fs_ext": fs_ext, "u_ext": u_ext, "lam_ext": lam_ext, "bal_sample": bal,
            "window_low": window_low}


# ---------------------------------------------------------------------------------------------- C8 throats
def throats():
    """(a) a plane at fixed global-AdS2 position in AdS2(L) x X3 (or in the board's column, AdS2 warped by alpha(y)):
    S^tau_tau = 0 -- pressure only; (b) the vacuum products; (c) the board's AdS2 x S2 slice (sim2_facing
    near_horizon) and its 5D column's singular end (throat_bulk)."""
    tau, rho, y, x1, x2, x3 = sp.symbols("tau rho y x1 x2 x3", real=True)
    Lq = sp.Symbol("L", positive=True)
    al = sp.Function("alpha")(y)
    be = sp.Function("beta")(y)
    th, ph = sp.symbols("theta phi", real=True)
    # the board's column: dy^2 + alpha^2 L^2 (-cosh^2 rho dtau^2 + drho^2) + beta^2 dOmega2; surface rho = rho0
    X = [tau, rho, y, th, ph]
    g = sp.diag(-al**2 * Lq**2 * sp.cosh(rho) ** 2, al**2 * Lq**2, 1, be**2, be**2 * sp.sin(th) ** 2)
    gi = sp.diag(*[1 / g[i, i] for i in range(5)])
    Gam = lambda a, b, c: sum(gi[a, d] * (sp.diff(g[d, b], X[c]) + sp.diff(g[d, c], X[b]) - sp.diff(g[b, c], X[d]))
                              for d in range(5)) / 2
    n_low = [0, al * Lq, 0, 0, 0]
    tang = [0, 2, 3, 4]
    Km = {a: sp.simplify(gi[a, a] * (sp.diff(n_low[a], X[a]) - sum(Gam(c, a, a) * n_low[c] for c in range(5))))
          for a in tang}
    off = [sp.simplify(sp.diff(n_low[b], X[a]) - sum(Gam(c, a, b) * n_low[c] for c in range(5)))
           for a in tang for b in tang if a != b]
    Ktr = sum(Km.values())
    S = {a: sp.simplify(-(Km[a] - Ktr)) for a in tang}           # nu = 1
    col = {"Km": Km, "S": S, "offdiag_zero": all(z == 0 for z in off)}
    # (b) vacuum products AdS2(L1) x X3(L2) in 5D, R_ab = -(4/ell^2) g_ab
    ell = sp.Symbol("ell", positive=True)
    L1s, L2s = sp.symbols("L1 L2", positive=True)
    prod = {}
    for name, c3 in (("AdS2 x H3", -1), ("AdS2 x S3", 1), ("AdS2 x R3", 0)):
        eqs = [sp.Eq(-1 / L1s**2, -4 / ell**2), sp.Eq(2 * c3 / L2s**2, -4 / ell**2)]
        prod[name] = sp.solve(eqs, [L1s, L2s], dict=True)
    # AdS2(L1) x S2(L2) x line: Ricci eigenvalues -1/L1^2, +1/L2^2, 0 -- must all equal -4/ell^2
    prod["AdS2 x S2 x R"] = sp.solve([sp.Eq(-1 / L1s**2, -4 / ell**2), sp.Eq(1 / L2s**2, -4 / ell**2),
                                      sp.Eq(0, -4 / ell**2)], [L1s, L2s], dict=True)
    # (c) the board's slice and column
    o = owners()
    nh = o["s2"].near_horizon()
    cols = {}
    for e in (0.0, 1.0 / 32, 0.25, 1.0):
        tb = o["s2"].throat_bulk(e)
        cols[e] = (tb["y_s"], tb["reached_alpha0"])
    return {"column": col, "products": prod, "near_horizon": {"AdS2_R": nh["AdS2_R"], "S2_radius": nh["S2_radius"],
                                                              "R_mixed": nh["R_mixed"]}, "column_ends": cols}


# ---------------------------------------------------------------------------------------------- C9 charged extremal
def charged():
    """Outside clause (B) (a bulk Maxwell field; a mirrored plane then carries charge): f = k + r^2 - mu/r^2 + q^2/r^4.
    Mirrored static plane: 2k - 4mu/R^2 + 6q^2/R^4 = 0.  Extremal double root r0."""
    r0, Rs = sp.symbols("r0 R", positive=True)
    out = {}
    for k in (0, 1):
        q2, mu = sp.symbols("q2 mu", positive=True)
        f = lambda r: k + r**2 - mu / r**2 + q2 / r**4
        sol = sp.solve([sp.Eq(f(r0), 0), sp.Eq(sp.diff(f(Rs), Rs).subs(Rs, r0), 0)], [q2, mu], dict=True)[0]
        u = sp.Symbol("u", positive=True)
        bal = sp.expand((2 * k * u**2 - 4 * sol[mu] * u + 6 * sol[q2]))
        roots = sp.solve(bal, u)
        rows = []
        for rt in roots:
            rt = sp.simplify(rt)
            fval = sp.simplify(f(sp.sqrt(rt)).subs(sol))
            rows.append((rt, sp.factor(fval)))
        out[k] = {"q2": sol[q2], "mu": sol[mu], "static_u": rows}
    # k = 1's outside root: (kappa^2 sigma/6)^2 - 1 = f/u - 1, numerator 4(3x+1)^3 - 27x(2x+1)^2 = 9x + 4 (x = r0^2)
    x = sp.Symbol("x", positive=True)
    out["k1_excess_num"] = sp.expand(4 * (3 * x + 1) ** 3 - 27 * x * (2 * x + 1) ** 2)
    return out


# ---------------------------------------------------------------------------------------------- C11 matter (184)
def matter():
    """Under 184 every plane carries matter: rho_tot = sigma + rho_m, p_tot = -sigma + p_m.  Then kappa^2 (rho_m + p_m)
    = B/R (C1), independent of sigma.  Flat planes: B < 0 -- NEC-violating matter, any tension.  Mirrored flat plane at
    RS tension: rho_m = (6/kappa^2)(sqrt(1/ell^2 - mu/R^4) - 1/ell) < 0.  Spherical mirrored planes: rho_m >= 0 and the
    NEC hold on R^2 >= 2 mu (ours at RS) -- a continuum, so matter left unspecified leaves R1, R2, mu free; position
    2's negative tension is then allowed (rho_m = rho_tot + |sigma_2| > 0)."""
    R, ell, mu = sp.symbols("R ell mu", positive=True)
    flatZ2 = junction_conditions([(1, R**2 / ell**2 - mu / R**2, 2 * R / ell**2 + 2 * mu / R**3)] * 2)
    rho_m_flat = sp.simplify(flatZ2["rho"].subs(flatZ2["R"], R) - 6 / ell)
    nec_flat = sp.simplify(flatZ2["rho"].subs(flatZ2["R"], R) + flatZ2["p"].subs(flatZ2["R"], R))
    sph = junction_conditions([(1, f_of(1, ell, mu, R), fp_of(1, ell, mu, R))] * 2)
    rho_m_sph = sp.simplify(sph["rho"].subs(sph["R"], R) - 6 / ell)
    nec_sph = sp.simplify(sph["rho"].subs(sph["R"], R) + sph["p"].subs(sph["R"], R))
    return {"rho_m_flat_RS": rho_m_flat, "nec_flat": nec_flat, "rho_m_sph_RS": rho_m_sph, "nec_sph": nec_sph}


# ---------------------------------------------------------------------------------------------- report
def compute(full=False):
    t = time.time()
    d = {"conv": conventions(full), "junction": junction_check(), "flat": flat(), "mirrored": mirrored(),
         "sign": sign_condition(), "k1": k1_closed(), "grid": grid(), "hyper": hyperbolic(), "throats": throats(),
         "charged": charged(), "matter": matter()}
    d["seconds"] = time.time() - t
    return d


def report(d):
    c = d["conv"]
    print("modelc.py -- model C, the two-sided bridge (items 179-182); scratch, not verified, not seated\n")
    print("C0 conventions: M4 tensions %s, %s of lambda_RS(k_R) -> ratio %s (KDERIVE, b6_k); per sheet (stage 7 K5, "
          "174 (2)) ratio %s; k_R/k_L = %s so M4's ell_2 = %s ell" % (c["m4"]["tau1_over_rs"], c["m4"]["tau2_over_rs"],
                                                                     c["ratio_m4"], c["ratio_sheet"], c["kR_over_kL"],
                                                                     c["ell2_over_ell_M4"]))
    if "b6_ratio" in c:
        print("   b6_k.compute ratio %s (%.0f s)" % (c["b6_ratio"], c["b6_seconds"]))
    j = d["junction"]
    print("C1 junction: Christoffel K = coded %s; rho = 3 sum eps sqrt f / R %s; kappa^2(rho+p) = B/R %s; moving-plane "
          "route agrees %s (K^x_x moving %s); RS control %s (mutation kills it %s); owners stage6 %s, israel %s"
          % (j["direct"], j["rho_formula"], j["rho_plus_p_is_B"], j["moving_route"], j["moving_Kxx"], j["rs_control"],
             j["rs_mutation_kills"], j["owner_stage6"], j["owner_israel"]))
    fl = d["flat"]
    print("C2 flat planes (k = 0): B(mirror) = %s; = 2 x, 1 x, 1 x (-2 mu/(R^2 sqrt f_s)) for mirror/decaying/growing: "
          "%s; mu = 0 control B == 0: %s; at rest R'' = %s (toward the bridge); at exactly RS Rdot^2 = %s (k=0), %s "
          "(k=1)" % (fl["B"]["mirror"], fl["B_is_minus_2mu"], fl["control_mu0"], fl["acc_mirror"], fl["rdot2_rs"],
                     fl["rdot2_rs_k1"]))
    mi = d["mirrored"]
    print("C3 mirrored: static roots mu = %s (k=1), %s (k=0), %s (k=-1); k=1: (kappa^2 sigma/6)^2 - 1/ell^2 = %s > 0; "
          "mu = %s for excess x; f(R) = %s > 0; V'' = %s < 0 (unstable); k=-1 horizon gap r_+^2 - R^2 = %s >= 0"
          % (mi["roots"][1], mi["roots"][0], mi["roots"][-1], mi["excess"], mi["mu_of_excess"], mi["f_static"],
             mi["Vpp"], mi["km1_gap"]))
    sg = d["sign"]
    print("C4 sign: mirrored kappa^2 rho = %s (> 0); T5c's bound s2 <= %s (Lemma T fixed point %s) needs a static chart "
          "to P2, but from P1 the chart ends at the bifurcation surface at finite depth (example %s ell, r_h = %s)"
          % (sg["rho_mirror"], sg["t5c_bound"], sg["lemma_t_fixed_point"], mp.nstr(sg["depth_to_bifurcation_example"], 8),
             sp.N(sg["rh_example"], 8)))
    k1 = d["k1"]
    print("C5 k=1: quadratic roots %s; unsquared residues ours %s, P2 %s; (3+4v^2)^2-16v^2(1+v^2) = %s; N-form %s; "
          "lam_ours -> %s at L=2 (= 1 + 1/L); P2 exists iff L<1 identity %s; lam_P2 -> %s at L=1/2 (= 1 - 1/L)"
          % (k1["roots_ok"], [mp.nstr(x, 3) for x in k1["balance_res_ours"]],
             [mp.nstr(x, 3) for x in k1["balance_res_p2"]], k1["lower_sq_gap"], k1["N_ok"], k1["lim_ours_L2"],
             k1["exist_identity_zero"], k1["lim_p2_Lhalf"]))
    g = d["grid"]
    print("C6 recorded conventions:")
    for row in g["rows"]:
        print("   %-38s L2 = %-4s P2 static possible: %s; ours at RS: no -> %s"
              % (row["convention"], row["L2"], row["P2_static_possible"], row["verdict"]))
    print("   off-convention branches (ell_s = 1):")
    for fm in g["family"]:
        p2s = "; ".join("u2 = %s, L2 = %s, R2 = %s (bal %s, ten %s)" % (sp.N(s_["u2"], 10), sp.N(s_["L2"], 10),
                                                                      sp.N(s_["R2"], 10), s_["bal"], s_["ten"])
                        for s_ in fm["p2"]) or "none"
        print("   %-12s L1 = %-4s mu = %-12s R1 = %-12s r_h = %-12s ratio %s: %s"
              % (fm["branch"], fm["L1"], sp.N(fm["mu"], 10), sp.N(fm["R1"], 10), sp.N(fm["rh"], 10), fm["ratio"], p2s))
    for rho, sols in g["L1_inf"].items():
        print("   L1 -> oo (mu -> 1), ratio -%s: %s" % (rho, ["L2 = %s" % sp.N(s_["L2"], 12) for s_ in sols]))
    for (rho, m), sols in g["L1_one"].items():
        print("   L1 -> 1+ (mu = %s), ratio -%s: %s" % (m, rho, ["L2 = %s" % sp.N(s_["L2"], 12) for s_ in sols]))
    hy = d["hyper"]
    print("C7 k=-1: lam R = %s (sign of mu); extremal f_s = %s, static u = %s, lam = %s, sample balance %s, window "
          "L_o > %s" % (hy["lam_R"], hy["fs_ext"], hy["u_ext"], hy["lam_ext"], hy["bal_sample"], hy["window_low"]))
    th = d["throats"]
    print("C8 throats: column K = %s; S = %s; products %s; board's slice AdS2 R = %s, S2 radius %s; column ends (y_s, "
          "singular) %s" % (th["column"]["Km"], th["column"]["S"], th["products"], th["near_horizon"]["AdS2_R"],
                            th["near_horizon"]["S2_radius"], th["column_ends"]))
    ch = d["charged"]
    print("C9 charged k=1 outside root super-critical: numerator %s > 0" % ch["k1_excess_num"])
    for k in (0, 1):
        print("C9 charged k=%s: extremal q^2 = %s, mu = %s; mirrored static u and f there: %s"
              % (k, ch[k]["q2"], ch[k]["mu"], ch[k]["static_u"]))
    ma = d["matter"]
    print("C11 matter (184): flat mirrored at RS rho_m = %s; kappa^2(rho+p) flat = %s; spherical rho_m = %s, "
          "kappa^2(rho+p) = %s" % (ma["rho_m_flat_RS"], ma["nec_flat"], ma["rho_m_sph_RS"], ma["nec_sph"]))
    print("\n(%.1f s)" % d["seconds"])


def selftest(full=False):
    ok = n = 0

    def chk(name, cond):
        nonlocal ok, n
        n += 1
        ok += bool(cond)
        print("  [%s] %s" % ("ok" if cond else "FAIL", name))

    d = compute(full)
    c = d["conv"]
    chk("C0: M4's tensions +4/3, -1/3 give ratio -1/4; one sheet in M4's geometry gives -1/8; ell_2 = 4 ell/3",
        c["ratio_m4"] == sp.Rational(-1, 4) and c["ratio_sheet"] == sp.Rational(-1, 8) and
        c["ell2_over_ell_M4"] == sp.Rational(4, 3))
    if full:
        chk("C0 (--full): b6_k.compute's ratio is 3/4", c["b6_ratio"] == sp.Rational(3, 4))
    j = d["junction"]
    chk("C1: K from the 5D Christoffels equals the coded K (t, x, y; off-diagonal zero)", j["direct"])
    chk("C1: rho = 3 sum eps sqrt f/R and kappa^2 (rho + p) = B/R, symbolic two sides", j["rho_formula"] and
        j["rho_plus_p_is_B"])
    chk("C1: the moving-plane route (turning point with zero acceleration) gives the same balance", j["moving_route"] and
        j["moving_Kxx"])
    chk("C1 control: planar AdS, two decaying sides, gives the RS tension 6/(kappa^2 ell); flipping one side kills it",
        j["rs_control"] and j["rs_mutation_kills"])
    chk("C1 owners: b4d_stage6.sigma_over_rs and sim2_facing.israel reproduce the static mirrored plane", j["owner_stage6"]
        and j["owner_israel"])
    fl = d["flat"]
    chk("C2: flat planes, B = -2 mu/(R^2 sqrt f_s) x (2, 1, 1) -- never zero for mu > 0", fl["B_is_minus_2mu"])
    chk("C2 control: mu = 0 makes B vanish identically (a flat plane balances at every R)", fl["control_mu0"])
    Rv, lv, mv = sp.Rational(2), sp.Integer(1), sp.Rational(1, 10)
    chk("C2 control can fail: at mu = 1/10, R = 2, ell = 1 the mirrored B is nonzero (%s)" %
        sp.N(fl["B"]["mirror"].subs({sp.Symbol("R", positive=True): Rv, sp.Symbol("ell_s", positive=True): lv,
                                     sp.Symbol("mu", positive=True): mv}), 6),
        sp.N(fl["B"]["mirror"].subs({sp.Symbol("R", positive=True): Rv, sp.Symbol("ell_s", positive=True): lv,
                                     sp.Symbol("mu", positive=True): mv})) != 0)
    mi = d["mirrored"]
    R_, ell_ = sp.symbols("R ell", positive=True)
    chk("C3: mirrored static roots mu = R^2/2 (k=1), 0 (k=0), -R^2/2 (k=-1)",
        mi["roots"][1] == [R_**2 / 2] and mi["roots"][0] == [0] and mi["roots"][-1] == [-R_**2 / 2])
    chk("C3: k = 1 super-critical: (kappa^2 sigma/6)^2 - 1/ell^2 = 1/(2R^2) > 0; mu = 1/(4x); unstable V'' = -4/R^2",
        sp.simplify(mi["excess"] - 1 / (2 * R_**2)) == 0 and sp.simplify(mi["Vpp"] + 4 / sp.Symbol("Rv", positive=True)**2)
        == 0)
    Rsq = sp.Symbol("Rsq", positive=True)
    gap_ok = all(sp.N(mi["km1_gap"].subs({Rsq: q, sp.Symbol("l", positive=True): 1})) >= 0
                 for q in (sp.Rational(1, 10), sp.Rational(1, 4), sp.Rational(49, 100), sp.Rational(1, 2)))
    chk("C3: k = -1 mirrored static point never lies outside the horizon (r_+^2 - R^2 >= 0 on its whole range)", gap_ok)
    sg = d["sign"]
    chk("C4: mirrored plane with the bridge side: kappa^2 rho = 6 sqrt(f)/R (> 0); T5c's bound is -1 and its premise "
        "fails (finite depth to the bifurcation surface)", sg["rho_mirror_claim"] and sg["t5c_bound"] == -1 and
        sg["depth_to_bifurcation_example"] > 0)
    k1 = d["k1"]
    chk("C5: both branch formulas solve the squared balance; unsquared balance and tension residues < 1e-25",
        k1["roots_ok"] and all(abs(x) < 1e-25 for x in k1["balance_res_ours"] + k1["balance_res_p2"]))
    chk("C5: ours strictly super-critical: (3+4v^2)^2 - 16 v^2 (1+v^2) = 9 + 8 v^2 and the N-form identity holds",
        sp.simplify(k1["lower_sq_gap"] - (9 + 8 * sp.Symbol("v", positive=True)**2)) == 0 and k1["N_ok"])
    chk("C5: lam_ours -> 1 + 1/L (L = 2: 3/2), lam_P2 -> 1 - 1/L (L = 1/2: -1)", k1["lim_ours_L2"] == sp.Rational(3, 2)
        and k1["lim_p2_Lhalf"] == -1)
    chk("C5: P2 static iff L2 < 1 (the identity (4A-1)^2 - D = 16 A (A - 1 - u))", k1["exist_identity_zero"])
    # mutation for C5's criterion: at L = 4/3 and L = 3 the P2 mu root is negative at sample u
    neg = all(sp.N(MU_P2.subs({U: uv, L: Lv})) < 0 for uv in (1, 5, 50) for Lv in (sp.Rational(4, 3), 3, 6))
    pos = all(sp.N(MU_P2.subs({U: uv, L: sp.Rational(1, 2)})) > 0 for uv in (1, 5, 50))
    chk("C5 control: P2's mu < 0 at L2 = 4/3, 3, 6 (the recorded conventions) and > 0 at L2 = 1/2", neg and pos)
    g = d["grid"]
    chk("C6: every recorded convention (ell_2 = ell, 4ell/3, 3ell, 6ell) is NO SOLUTION",
        all(r_["verdict"] == "NO SOLUTION" and not r_["P2_static_possible"] for r_ in g["rows"]))
    fam_ok = all(len(fm["p2"]) >= 1 and all(abs(s_["bal"]) < 1e-20 and abs(s_["ten"]) < 1e-20 and s_["L2"] < 1
                                            for s_ in fm["p2"]) for fm in g["family"])
    chk("C6: the off-convention branches have admissible P2 roots (balance and tension met, L2 < 1)", fam_ok)
    rs = rs_at_ell_s(sp.Integer(2))
    chk("C6: RS at ell_s with L1 = 2 gives u1 = mu = 4/3 exactly and lam = 2", rs["u1"] == sp.Rational(4, 3) and
        sp.simplify(rs["mu"] - sp.Rational(4, 3)) == 0 and sp.simplify(rs["lam"] - 2) == 0)
    r1 = rs_at_ell_1(sp.Rational(4, 5))
    chk("C6: RS at ell_1 with L1 = 4/5 gives lam = 2/L1 = 5/2", abs(sp.N(r1["lam"] - sp.Rational(5, 2), 30)) < 1e-25)
    hy = d["hyper"]
    Lo = sp.Symbol("L_o", positive=True)
    chk("C7: k = -1 tension carries the sign of mu; extremal static u = L^2/(1 - L^2), lam = -(1 - L^2)/(2 L^2), "
        "window L > 1/sqrt3", sp.simplify(hy["lam_ext"] + (1 - Lo**2) / (2 * Lo**2)) == 0 and hy["bal_sample"] == 0 and
        hy["window_low"] == [sp.sqrt(3) / 3])
    th = d["throats"]
    Sv = th["column"]["S"]
    chk("C8: a plane at fixed global-AdS2 position in the warped column has S^tau_tau = 0 (no energy) and K only in tau",
        Sv[0] == 0 and th["column"]["offdiag_zero"] and all(th["column"]["Km"][a] == 0 for a in (2, 3, 4)))
    pr = th["products"]
    chk("C8: the only vacuum Lambda<0 products are AdS2(ell/2) x H3(ell/sqrt2); AdS2 x S3, AdS2 x R3, AdS2 x S2 x R "
        "have none", len(pr["AdS2 x H3"]) == 1 and pr["AdS2 x S3"] == [] and pr["AdS2 x R3"] == [] and
        pr["AdS2 x S2 x R"] == [])
    chk("C8 owners: the board's slice is AdS2(2m) x S2(2m) (R = -1/2, radius 2); its column ends singular at finite y_s",
        th["near_horizon"]["AdS2_R"] == sp.Rational(-1, 2) and th["near_horizon"]["S2_radius"] == 2 and
        all(v[1] and 0 < v[0] < 3 for v in th["column_ends"].values()))
    ch = d["charged"]
    r0 = sp.Symbol("r0", positive=True)
    k0 = ch[0]["static_u"]
    chk("C9: charged k = 0 extremal: the mirrored static plane sits on the horizon (u = r0^2, f = 0)",
        len(k0) == 1 and sp.simplify(k0[0][0] - r0**2) == 0 and k0[0][1] == 0)
    chk("C9: charged k = 1 extremal outside mirrored plane is super-critical (9x + 4)",
        sp.simplify(ch["k1_excess_num"] - 9 * sp.Symbol("x", positive=True) - 4) == 0)
    chk("C2: at exactly RS a flat mirrored plane moves, Rdot^2 = mu/R^2 (never at rest for mu > 0)",
        sp.simplify(fl["rdot2_rs"] - sp.Symbol("mu", positive=True) / R_**2) == 0)
    ma = d["matter"]
    chk("C11: flat mirrored plane at RS beside a black brane: rho_m < 0 and kappa^2(rho+p) < 0 (sample mu = 1/10, R = 2)",
        sp.N(ma["rho_m_flat_RS"].subs({sp.Symbol("mu", positive=True): sp.Rational(1, 10), R_: 2, ell_: 1})) < 0 and
        sp.N(ma["nec_flat"].subs({sp.Symbol("mu", positive=True): sp.Rational(1, 10), R_: 2, ell_: 1})) < 0)
    print("selftest: %d/%d (%.1f s)" % (ok, n, d["seconds"]))
    return ok == n


if __name__ == "__main__":
    full = "--full" in sys.argv
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest(full) else 1)
    report(compute(full))
