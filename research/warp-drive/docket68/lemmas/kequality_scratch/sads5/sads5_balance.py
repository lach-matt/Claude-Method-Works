#!/usr/bin/env python3
"""sads5_balance.py -- item 181, MODEL A: the corridor as a 5D black hole's bulk (Schwarzschild-AdS5), our plane and
position 2's plane as static surfaces R = a1, R = a2.  Do the two balance conditions pin a1/ell, a2/ell and mu/ell^2?

Board scratch, read-only on the repository.  Labels: computed / READ / deduced / STRUCTURAL / standard-not-READ / OPEN.
Not verified; not seated.

M's words (verbatim in docket68/M-RULINGS-2026-10-03.md, never paraphrased as M's): 179/180 "We know the corridor *does
not sit on either position's plane, it only bridges them. So one could surmise that the corridor is exclusive to the
bulk."; 181 "this bears directly on B4d, and requires priority"; 136 (3); 139 (1) "1 - yes"; 162; 166; 127; 129; 130;
138; 141; and, recorded after the computed task was written, 182 ("If I had to guess, I would go with C"), 184 ("There
are no matter free planes") and 185 ("If it has potential to solve most of the current and future work, then we should
run that now").  Under 184 every pure-tension result here is the matter-free LIMIT; section M184 gives the matter case.

SETUP (computed).  Bulk regions ds^2 = -f dt^2 + dR^2/f + R^2 dOmega_k^2, f = k + R^2/L^2 - mu/R^2 + q^2/R^4 (q = 0:
Schwarzschild-AdS5; q != 0: the charged variant, charged_param.py).  A static plane at R = a; on each side i the unit
normal points INTO region i: eta_i = +1 if region i lies at R > a, -1 if at R < a.  Israel (owner sim2_facing.israel,
one call per side, nu = 1/kappa^2): S^a_b = sum_i -(1/kappa^2)(K_i^a_b - delta K_i).  Units ell = L_slab = 1;
tau = kappa^2 sigma/6, so the Randall-Sundrum value is tau = 1/ell (sigma_RS = 6/(kappa^2 ell) = 3 nu/ell with
sim2_facing's nu = 2/kappa^2); u = ell^2/a^2.

CONVENTIONS (read: KDERIVE.md, b6_k.py, multiplane.py M4, B4D-STAGE6 J3, B4D-STAGE7 K4/K5).  T1 = M4's geometry (the
LR orbifold: ours mirrored at sigma_RS(ell_L); position 2 one sheet between ell_L and ell_R = 4 ell_L/3, k_R = 3k_L/4
imported from multiplane M4 / b6_k): PRZ's -1/4 is the doubled-space count, one sheet carries -1/8 -- the flat control
passes with -1/8 and FAILS with -1/4 on the sheet (T1d), which settles K5's count in favour of the verifier.  T2: the
quarter as a ratio of single-sheet tensions (k_R = k_L/2).  T3/T4: STAGE6 J3 / STAGE7 K5 (position 2 mirrored at its
own ell_2 = 3 ell or 6 ell).  S7-*: STAGE7 K4's rows (ours two-sided), rebuilt from the flat junction.  V1/V2: the
board's variant H-MIRROR-AS-OWN-BULK (our mirror replaced by a corridor-free copy of our bulk, 129), all 16 orientations.
The answer does not depend on the convention.

  J0  K^t_t = eta f'/(2 sqrt f), K^i_i = eta sqrt f / a for k = 1, 0, -1, from the metric's Christoffels (computed).
  J1  rho = -(3/kappa^2) Phi,  p = (1/kappa^2)(a Phi' + 3 Phi),  Phi(a) = sum_i eta_i sqrt(f_i(a))/a  (computed identity).
      A pure-tension plane is static iff Phi(a) = -2 tau (tt) and Phi'(a) = 0 (angular).  Mutation of the owner's trace
      (trace_from = 1) breaks the RS control.
  J2  Kraus hep-th/9910149v2 (READ): his eq. (14) gives his eq. (18) exactly (computed); static = V = -k/2, V' = 0.
  C0  control (pure AdS5, mu = 0, k = 0): Phi constant -> a flat plane balances at EVERY a at the tuned tension, at NO a
      off it (computed).  C0b: owner sim2_facing.t5c/lemma_t -- s2 = -1 at s1 = 1, reproduced by this junction.
  L1  a MIRRORED plane at the RS value of its own bulk: no static position for any mu != 0, k = 1, 0, -1 (exact:
      F(u*) - 1 = k^2/(4 mu) at u* = k/(2 mu); k = 0: F' = -2 mu u).  Wolfram cross-check: Reduce gives False, mu = 0, False.
  C1  control (tension off RS, mirrored, k = 1): ONE static position, FIXED: a^2 = 2 mu, mu = ell^2/(4(tau^2 ell^2 - 1))
      (tau ell = 11/10: mu = 25/21 ell^2) -- the answer changes from none to an equality; the test can return one.
  L2  a two-sided plane at the RS value (one ell, both sides decaying), ANY masses mu_+, mu_-: static only for k = -1
      with Delta = mu_+ - mu_- > ell^2 (the sign filter of eq. 18's squaring); then a^6 = ell^2 Delta^2/8,
      mu_+ + mu_- = -(3/2) ell^(2/3) Delta^(2/3); the lighter side always has mu < -5 ell^2/4 (naked: Kraus p.4's horizon
      bound mu >= -ell^2/4, READ); V'' = -(3/4) Delta^2/a^8 < 0: unstable (Kraus p.5, READ).  Far side corridor-free:
      mu = -27 ell^2/8, a^2 = 9 ell^2/8 (no horizon).
  E   the two-plane system, every convention above, every orientation, k = 1, 0, -1: Groebner bases over Q (computed):
      no admissible solution with mu != 0; every positive-dimensional case has mu u1 in the ideal (the k = 0 control
      modulus, admissible exactly where the flat control passes).
  Q   charged (computed): a mirrored plane at RS balances only for k = 1, mu = 2|q|, a^2 = |q| -- horizonless, q free --
      and position 2 then fails under T1/T2 (outer charge q or 0).  charged_param.py (every convention and orientation):
      with ours AT the RS value no connected solution (the two junction-admissible ones, V1/V2 at k = -1, have both slab
      sides running to their own conformal boundaries: no slab bridging the planes).  OFF the RS value -- STAGE7 K4's
      'ours grows' rows (ours 4/3 sigma_RS(ell_1) = 4/11 of the slab's RS value) -- two isolated connected solutions at
      k = +1 (verify_s7_charged.py, 60 digits): mu = -1.099e5 / -9.787e5 ell_s^2, no horizon, closed planes of radius
      143.5 / 428.4 ell_s.  An equality, but of a horizonless negative-mass bulk with our plane off the RS value: C1's
      phenomenon (off RS a length can be fixed), not a corridor.
  M184 with matter on our plane at the RS tension, every position balances: rho_m + p_m = (a/kappa^2) Phi'(a); at k = 0
      a corridor of positive mass needs rho_m < 0 and rho_m + p_m < 0 on our plane (computed).
  R_h  Kraus eq. (9) (READ) for the corridor's size; the identification with eq. (17)'s m is a reading (report()).

python3 sads5_balance.py [--selftest] [--owners-full]   (--owners-full also runs b6_k.compute(), ~75 s)
"""
import contextlib
import importlib.util
import io
import itertools
import os
import sys
import time

import sympy as sp

D68 = "/home/user/Claude-Method-Works/research/warp-drive/docket68"
WD = os.path.dirname(D68)
R_ = sp.Rational


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


S2F = _load(os.path.join(D68, "lemmas", "sim2_facing.py"), "kq_sim2_facing")
MP = _load(os.path.join(D68, "bulk", "multiplane.py"), "kq_multiplane")


# ------------------------------------------------------------------------------------------------ J0 K from the metric
def k_from_metric(kcurv):
    """K^a_b of R = a in -f dt^2 + dR^2/f + R^2 (dchi^2 + S_k(chi)^2 dOmega_2), normal n = eta sqrt(f) d_R, from
    K_ab = grad_a n_b = -Gamma^R_ab n_R (n_b = 0 tangentially).  Returns the mixed diagonal (t, chi, th, ph)."""
    t, Rr, chi, th, ph, eta = sp.symbols("t R chi theta phi eta")
    f = sp.Function("f")(Rr)
    Sk = {1: sp.sin(chi), 0: chi, -1: sp.sinh(chi)}[kcurv]
    X = [t, Rr, chi, th, ph]
    g = sp.diag(-f, 1 / f, Rr**2, Rr**2 * Sk**2, Rr**2 * Sk**2 * sp.sin(th)**2)
    gi = g.inv()

    def Gam(a, b, c):
        return sum(gi[a, d] * (sp.diff(g[d, b], X[c]) + sp.diff(g[d, c], X[b]) - sp.diff(g[b, c], X[d]))
                   for d in range(5)) / 2

    nR = eta / sp.sqrt(f)                                  # n_R for n^R = eta sqrt(f)
    tang = [0, 2, 3, 4]
    Kmix = [sp.simplify(gi[a, a] * (-Gam(1, a, a) * nR)) for a in tang]
    return Kmix, f, Rr, eta


def j0():
    out = {}
    for kc in (1, 0, -1):
        Kmix, f, Rr, eta = k_from_metric(kc)
        exp_t = eta * sp.diff(f, Rr) / (2 * sp.sqrt(f))
        exp_i = eta * sp.sqrt(f) / Rr
        out[kc] = (sp.simplify(Kmix[0] - exp_t) == 0 and all(sp.simplify(Kmix[i] - exp_i) == 0 for i in (1, 2, 3)))
    return out


# ------------------------------------------------------------------------------------------------ J1 the junction
def stress_two_sides(fA, fB, etaA, etaB, a, kap2):
    """rho, p of a static plane at R = a between sides A, B (owner israel per side, nu = 1/kappa^2)."""
    rho, ps = 0, [0, 0, 0]
    for f, eta in ((fA, etaA), (fB, etaB)):
        Kt = eta * sp.diff(f, a) / (2 * sp.sqrt(f))
        Ki = eta * sp.sqrt(f) / a
        r_, p_ = S2F.israel([Kt, Ki, Ki, Ki], nu=1 / kap2)
        rho += r_
        ps = [x + y for x, y in zip(ps, p_)]
    return sp.simplify(rho), [sp.simplify(x) for x in ps]


def j1():
    a, kap2 = sp.symbols("a kappa2", positive=True)
    etaA, etaB = sp.symbols("eta_A eta_B")
    fA, fB = sp.Function("f_A")(a), sp.Function("f_B")(a)
    rho, ps = stress_two_sides(fA, fB, etaA, etaB, a, kap2)
    Phi = etaA * sp.sqrt(fA) / a + etaB * sp.sqrt(fB) / a
    id_rho = sp.simplify(rho + 3 * Phi / kap2)
    id_p = sp.simplify(ps[0] - (a * sp.diff(Phi, a) + 3 * Phi) / kap2)
    # RS control through the same code: mirrored, pure AdS, flat, keep R < a on both sides
    ell = sp.Symbol("ell", positive=True)
    rs_rho, rs_p = stress_two_sides(a**2 / ell**2, a**2 / ell**2, -1, -1, a, kap2)
    return {"id_rho": id_rho, "id_p": id_p, "rs_rho": sp.simplify(rs_rho - 6 / (kap2 * ell)),
            "rs_p": sp.simplify(rs_p[0] + 6 / (kap2 * ell))}


# ------------------------------------------------------------------------------------------------ J2 Kraus (READ)
def j2():
    """Kraus hep-th/9910149v2: eq. (14) sqrt(f+ + Rdot^2) + sqrt(f- + Rdot^2) = (8 pi G sigma/3) R (both sides keep r < R,
    same ell); eq. (17) Rdot^2/2 + V = -k/2; eq. (18) V = (1/2)(1 - (s/sc)^2) R^2/l^2 - (mu+ + mu-)/(4R^2)
    - (1/32)(s/sc)^-2 l^2 (mu+ - mu-)^2/R^6, sc = 3/(4 pi G l).  Here 8 pi G sigma/3 = 2 tau, s/sc = tau l."""
    Rr, l, tau, mup, mum, kk, W = sp.symbols("R ell tau mu_p mu_m k W", positive=True)
    fp = kk + Rr**2 / l**2 - mup / Rr**2
    fm = kk + Rr**2 / l**2 - mum / Rr**2
    # sqrt(Xp) - sqrt(Xm) = (fp - fm)/(2 tau R): sqrt(Xp) = tau R + (fp - fm)/(4 tau R)
    Xp = (tau * Rr + (fp - fm) / (4 * tau * Rr))**2
    rdot2 = sp.expand(Xp - fp)
    V18 = (R_(1, 2) * (1 - (tau * l)**2) * Rr**2 / l**2 - (mup + mum) / (4 * Rr**2)
           - R_(1, 32) * (tau * l)**-2 * l**2 * (mup - mum)**2 / Rr**6)
    return {"eq18_residual": sp.simplify(rdot2 / 2 + V18 + kk / 2)}


# ------------------------------------------------------------------------------------------------ C0 / L1 / C1
u = sp.Symbol("u", positive=True)                        # u = ell^2/a^2 (ell = 1)


def Fslab(kc, mu, q=0, lam2=1):
    """f(a)/a^2 in u = 1/a^2:  k u + 1/L^2 - mu u^2 + q^2 u^3."""
    return kc * u + lam2 - mu * u**2 + q**2 * u**3


def c0():
    """Pure AdS5, flat, mu = 0: Phi constant in a."""
    a, L1, L2 = sp.symbols("a L_1 L_2", positive=True)
    out = {}
    for eA, eB in itertools.product((1, -1), repeat=2):
        Phi = eA * sp.sqrt(a**2 / L1**2) / a + eB * sp.sqrt(a**2 / L2**2) / a
        out[(eA, eB)] = sp.simplify(sp.diff(Phi, a))
    # at the RS value with one ell, the tt balance holds identically in a; off it, nowhere
    Phi_rs = -2 * sp.sqrt(a**2) / a
    off = [sp.Rational(9, 10), sp.Rational(11, 10)]
    return {"dPhi": out, "rs_any_a": sp.simplify(Phi_rs + 2) == 0,
            "off_rs_none": all(sp.simplify(Phi_rs + 2 * tv) != 0 for tv in off)}


def c0b():
    """Owner sim2_facing.t5c / lemma_t: two mirrored planes facing across one ell -- s2 = -1 at every depth (RS1), from
    the owner; and the same from this file's junction: a negative mirrored plane keeping R > a carries -sigma_RS."""
    own = S2F.t5c(1)
    lt = S2F.lemma_t()
    a, kap2 = sp.symbols("a kappa2", positive=True)
    rho2, _ = stress_two_sides(a**2, a**2, +1, +1, a, kap2)
    return {"owner_s2": own["at_s1_1"], "owner_fixed": lt["fixed_point"],
            "here_s2": sp.simplify(rho2 / (6 / kap2))}


def lemma1(q=0):
    """Mirrored plane, own bulk (k, mu, q), |tau| = 1/ell: Phi = 2 eta sqrt(F(u)).  Static <=> F(u) = 1, F'(u) = 0."""
    mu, qq = sp.symbols("mu q", real=True)
    out = {}
    for kc in (1, 0, -1):
        F = Fslab(kc, mu, qq if q else 0)
        sols = sp.solve([F - 1, sp.diff(F, u)], [u, mu] + ([qq] if q else []), dict=True)
        good = [s for s in sols if s.get(u, u).is_positive is not False]
        out[kc] = good
    return out


def lemma1_proof():
    """Exact: F = k u + 1 - mu u^2; F' = 0 -> u* = k/(2 mu); F(u*) - 1 = k^2/(4 mu): never 0 for k != 0; k = 0: F' =
    -2 mu u != 0.  Returned as the symbolic residues."""
    mu, kc = sp.symbols("mu k", real=True)
    F = kc * u + 1 - mu * u**2
    us = sp.solve(sp.diff(F, u), u)[0]
    return {"u_star": us, "F_minus_1_at_star": sp.simplify(F.subs(u, us) - 1)}


def c1():
    """Off the RS value (tau != 1), mirrored, k = 1: F(u*) = tau^2 -> mu = 1/(4(tau^2 - 1)), u* = 1/(2 mu)."""
    mu, tau = sp.symbols("mu tau", positive=True)
    F = Fslab(1, mu)
    sol = sp.solve([F - tau**2, sp.diff(F, u)], [u, mu], dict=True)
    ex = [{kk: sp.simplify(v.subs(tau, R_(11, 10))) for kk, v in s.items()} for s in sol]
    return {"general": sol, "at_tau_11_10": ex}


# ------------------------------------------------------------------------------------------------ L2 two-sided at RS
def lemma2():
    """Two-sided plane, same ell, both sides keep R < a (eta = -1), tau = 1, masses mu_p (slab), mu_m (far side)."""
    mp_, mm = sp.symbols("mu_p mu_m", real=True)
    s, t = sp.symbols("s t", positive=True)
    out = {}
    for kc in (1, 0, -1):
        Fp, Fm = Fslab(kc, mp_), Fslab(kc, mm)
        eqs = [s**2 - Fp, t**2 - Fm, s + t - 2, sp.expand(sp.diff(Fp, u) * t + sp.diff(Fm, u) * s)]
        G = sp.groebner(eqs, mp_, mm, s, t, u, order="lex")
        out[kc] = G
    # the far side corridor-free: mu_m = 0
    far0 = {}
    for kc in (1, 0, -1):
        Fp, Fm = Fslab(kc, mp_), Fslab(kc, 0)
        eqs = [s**2 - Fp, t**2 - Fm, s + t - 2, sp.expand(sp.diff(Fp, u) * t + sp.diff(Fm, u) * s)]
        far0[kc] = sp.solve(eqs, [mp_, s, t, u], dict=True)
    return out, far0


def lemma2_family(Delta):
    """k = -1 family at RS (Kraus eq. 18, both sides keeping r < R): R^6 = Delta^2/8, mu_p + mu_m = -(3/2) Delta^(2/3),
    Delta = mu_p - mu_m > 0.  The squaring in eq. (18) loses the signs of the two roots: both are positive only when
    sqrt(X_pm) = R +- (f_p - f_m)/(4R) > 0, i.e. Delta < 4 R^4 = Delta^(4/3), i.e. Delta > 1 (deduced; checked here)."""
    D = sp.nsimplify(Delta)
    a2 = (D**2 / 8)**R_(1, 3)
    ssum = -R_(3, 2) * D**R_(2, 3)
    mup, mum = (ssum + D) / 2, (ssum - D) / 2
    uu = 1 / a2
    Fp, Fm = -uu + 1 - mup * uu**2, -uu + 1 - mum * uu**2
    Rr = sp.sqrt(a2)
    root_p = Rr + (-(mup - mum) / a2) / (4 * Rr)            # Kraus's sqrt(X+) with Rdot = 0, divided by nothing: = sqrt(f+)
    root_m = Rr - (-(mup - mum) / a2) / (4 * Rr)
    s = sp.sqrt(Fp)
    t = sp.sqrt(Fm)
    res_T = sp.N(s + t - 2, 40)
    res_N = sp.N((-1 - 2 * mup * uu) * t + (-1 - 2 * mum * uu) * s, 40)
    return {"a2": a2, "mu_p": sp.simplify(mup), "mu_m": sp.simplify(mum), "res_T": res_T, "res_N": res_N,
            "roots_positive": bool(sp.N(root_p) > 0 and sp.N(root_m) > 0),
            "horizon_p": bool(sp.N(mup) >= -0.25), "horizon_m": bool(sp.N(mum) >= -0.25)}


def lemma2_stability():
    """Kraus eq. (18) at tau = 1/ell: V = -S/(4R^2) - D^2/(32 R^6), S = mu_+ + mu_-, D = mu_+ - mu_-.  At the static
    point V''(R) = -(3/4) D^2/R^8 < 0: a maximum of V -- the k = -1 family's planes are in UNSTABLE equilibrium (Kraus
    p.5: "the possibility of mu+ + mu- < 0 for k = -1 allows V(R) to have nontrivial local maxima", READ)."""
    Rr, Dl = sp.symbols("R D", positive=True)
    Ssym = sp.Symbol("S", real=True)
    V = -Ssym / (4 * Rr**2) - Dl**2 / (32 * Rr**6)
    Sst = sp.solve(sp.diff(V, Rr), Ssym)[0]
    return {"S_static": Sst, "Vpp": sp.simplify(sp.diff(V, Rr, 2).subs(Ssym, Sst))}


# ------------------------------------------------------------------------------------------------ E the conventions
# Each plane: ("Z2", eta_s, tau)  -- mirrored, both sides the slab (or its own bulk)
#             ("two", eta_s, eta_o, lam2_o, mu_o, tau) -- slab on one side, a pure-AdS outer bulk (mu_o) on the other
def conventions():
    t1o = (sp.Rational(3, 4))**2          # outer curvature k_R = 3 k_L/4 -> 1/L_o^2 = 9/16 (b6_k B6a / multiplane M4)
    return {
        # repository conventions: ours mirrored at the RS value of the slab (LR orbifold plane)
        "T1-M4": {"src": "multiplane.py M4 / KDERIVE / b6_k: k_R = 3 k_L/4; PRZ count -1/4 = one sheet -1/8",
                  "ours": ("Z2", -1, 1), "p2": ("two", +1, -1, t1o, 0, -R_(1, 8))},
        "T1d-M4-quarter-on-sheet": {"src": "M4 curvatures with -1/4 put on the single sheet (fails the flat control)",
                                    "ours": ("Z2", -1, 1), "p2": ("two", +1, -1, t1o, 0, -R_(1, 4))},
        "T2-sheet": {"src": "the quarter as a ratio of single-sheet tensions: -1/4, so k_R = k_L/2 (flat control)",
                     "ours": ("Z2", -1, 1), "p2": ("two", +1, -1, R_(1, 4), 0, -R_(1, 4))},
        "T3-S6J3": {"src": "B4D-STAGE6 J3: position 2's plane mirrored at its own ell_2 = 3 ell, -1/3 sigma_RS(ell)",
                    "ours": ("Z2", -1, 1), "p2": ("Z2own", +1, -R_(1, 3), R_(1, 9))},
        "T4-S7K5": {"src": "B4D-STAGE7 K5: one sheet -1/6, ell_2 = 6 ell, mirrored",
                    "ours": ("Z2", -1, 1), "p2": ("Z2own", +1, -R_(1, 6), R_(1, 36))},
        # B4D-STAGE7 K4's rows (ours two-sided: the slab on one side, our own bulk ell_1 on the other; ours +4/3 and
        # position 2 -1/3 or -1/6 of the unit's RS value), rebuilt from the flat junction in slab units (ell_s = 1):
        # (eta_s, eta_o, 1/L_o^2, mu_o, tau).  Row "ell_2 unit, -1/6" is M4's geometry = V1-T1's LR orientation.
        "S7-u2-1/3": {"src": "STAGE7 K4 row: unit ell_2, -1/3: ell_s = 3 ell_2/5, both outer bulks decay",
                      "ours": ("two", -1, -1, R_(9, 25), 0, R_(4, 5)), "p2": ("two", +1, -1, R_(9, 25), 0, -R_(1, 5))},
        "S7-u1-1/3-grow": {"src": "STAGE7 K4 row: unit ell_1, -1/3, ours grows: ell_s = 3 ell_1/11, ell_2 = ell_1/3",
                           "ours": ("two", -1, +1, R_(9, 121), 0, R_(4, 11)),
                           "p2": ("two", +1, -1, R_(81, 121), 0, -R_(1, 11))},
        "S7-u1-1/6-grow": {"src": "STAGE7 K4 row: unit ell_1, -1/6, ours grows: ell_s = 3 ell_1/11, ell_2 = 3 ell_1/10",
                           "ours": ("two", -1, +1, R_(9, 121), 0, R_(4, 11)),
                           "p2": ("two", +1, -1, R_(100, 121), 0, -R_(1, 22))},
        "S7-u1-1/6-decay": {"src": "STAGE7 K4 row: unit ell_1, -1/6, both decay: ell_s = 3 ell_1/5, ell_2 = 3 ell_1/4",
                            "ours": ("two", -1, -1, R_(9, 25), 0, R_(4, 5)),
                            "p2": ("two", +1, -1, R_(16, 25), 0, -R_(1, 10))},
        # the board's variant (not a repository convention): our mirror replaced by a corridor-free copy of our bulk
        # (129: our current state, no corridor), every orientation enumerated
        "V1-T1": {"src": "board variant H-MIRROR-AS-OWN-BULK + T1's position 2", "ours": ("two*", 1, 0, 1),
                  "p2": ("two*", t1o, 0, -R_(1, 8))},
        "V2-T2": {"src": "board variant H-MIRROR-AS-OWN-BULK + T2's position 2", "ours": ("two*", 1, 0, 1),
                  "p2": ("two*", R_(1, 4), 0, -R_(1, 4))},
    }


def _plane_eqs(kc, spec, mu, qq, uu, s, t, signs=None):
    """Polynomial equations of one plane with the corridor (mu, q) in the slab."""
    kind = spec[0]
    if kind in ("Z2", "Z2own"):
        if kind == "Z2":
            eta, tau = spec[1], spec[2]
            F = kc * uu + 1 - mu * uu**2 + qq**2 * uu**3
        else:                                   # the corridor in position 2's own mirrored bulk (ell_2)
            eta, tau, lam2 = spec[1], spec[2], spec[3]
            F = kc * uu + lam2 - mu * uu**2 + qq**2 * uu**3
        return [s**2 - F, 2 * eta * s + 2 * tau, sp.expand(sp.diff(F, uu))], [s]
    if kind == "two":
        eta_s, eta_o, lam2, mu_o, tau = spec[1:]
    else:                                       # "two*": signs supplied by the enumeration
        lam2, mu_o, tau = spec[1:] if len(spec) == 4 else spec[1:]
        eta_s, eta_o = signs
    Fs = kc * uu + 1 - mu * uu**2 + qq**2 * uu**3
    Fo = kc * uu + lam2 - mu_o * uu**2 + qq**2 * uu**3
    return [s**2 - Fs, t**2 - Fo, eta_s * s + eta_o * t + 2 * tau,
            sp.expand(eta_s * sp.diff(Fs, uu) * t + eta_o * sp.diff(Fo, uu) * s)], [s, t]


def horizon_status(kc, mu, q=0):
    """Does the slab bulk f = k + R^2 - mu/R^2 (+ q^2/R^4) have a horizon?  (Kraus p.4, READ, for q = 0.)"""
    if q == 0:
        if kc in (0, 1):
            return bool(mu > 0)
        return bool(mu >= -R_(1, 4))
    x = sp.Symbol("x", positive=True)            # x = R^2
    f = kc + x - mu / x + q**2 / x**2
    roots = [r for r in sp.Poly(sp.expand(f * x**2), x).nroots(n=30) if abs(sp.im(r)) < 1e-25 and sp.re(r) > 0]
    return len(roots) > 0


def solve_two_planes(kc, ours, p2, sign_combo=None, charged=False):
    mu = sp.Symbol("mu", real=True)
    qq = sp.Symbol("q", positive=True) if charged else 0
    u1, u2 = sp.symbols("u1 u2", positive=True)
    s1, t1, s2, t2 = sp.symbols("s1 t1 s2 t2", positive=True)
    sg1 = sign_combo[:2] if sign_combo else None
    sg2 = sign_combo[2:] if sign_combo else None
    e1, v1 = _plane_eqs(kc, ours, mu, qq, u1, s1, t1, sg1)
    v1 = [x for x in (s1, t1) if x in v1]
    e2, v2 = _plane_eqs(kc, p2, mu, qq, u2, s2, t2, sg2)
    v2 = [x for x in (s2, t2) if x in v2]
    unk = [mu] + ([qq] if charged else []) + v1 + v2 + [u1, u2]
    G = sp.groebner([sp.expand(e) for e in e1 + e2], *unk, order="lex")
    if G.exprs == [1]:
        return {"status": "inconsistent", "G": G}
    out = {"status": "zero-dim" if G.is_zero_dimensional else "positive-dim", "G": G, "sols": []}
    if not G.is_zero_dimensional:
        # a positive-dimensional ideal: is the corridor forced to vanish on it (mu u1 in the ideal, u1 > 0)?
        out["mu_forced_zero"] = bool(G.contains(mu * u1) or G.contains(mu))
        # and on that family, are the square roots positive (the orientation admissible: the control's modulus)?
        vals = {}
        for x in v1 + v2:
            for c in G.exprs:
                if sp.Poly(c, *unk).free_symbols == {x} and sp.degree(c, x) == 1:
                    zz = sp.Symbol("zz")
                    vals[x] = sp.solve(c.subs(x, zz), zz)[0]
        out["family_roots"] = vals
        out["family_admissible"] = all(v > 0 for v in vals.values()) and len(vals) == len(v1 + v2)
    if G.is_zero_dimensional:
        for sol in sp.solve(G.exprs, unk, dict=True):
            vals = {kk: sp.N(v, 30) for kk, v in sol.items()}
            ok = all(abs(sp.im(v)) < 1e-20 for v in vals.values())
            pos = ok and all(sp.re(vals[x]) > 0 for x in v1 + v2 + [u1, u2] if x in vals)
            out["sols"].append({"sol": sol, "real": ok, "admissible": pos})
    return out


def plane_alone(kc, spec, signs=None, charged=False):
    mu = sp.Symbol("mu", real=True)
    qq = sp.Symbol("q", positive=True) if charged else 0
    uu, s, t = sp.symbols("u s t", positive=True)
    e, v = _plane_eqs(kc, spec, mu, qq, uu, s, t, signs)
    unk = [mu] + ([qq] if charged else []) + [x for x in (s, t) if x in v] + [uu]
    G = sp.groebner([sp.expand(x) for x in e], *unk, order="lex")
    if G.exprs == [1]:
        return {"status": "inconsistent"}
    if not G.is_zero_dimensional:
        return {"status": "positive-dim", "G": G}
    sols = []
    for sol in sp.solve(G.exprs, unk, dict=True):
        vals = {kk: complex(sp.N(vv, 30)) for kk, vv in sol.items()}
        if all(abs(z.imag) < 1e-20 for z in vals.values()) and all(vals[x].real > 0 for x in unk[1:]):
            sols.append(sol)
    return {"status": "zero-dim", "sols": sols}


def enumerate_conventions(verbose=False):
    rows = []
    C = conventions()
    for name, cv in C.items():
        combos = [None] if cv["ours"][0] != "two*" else list(itertools.product((1, -1), repeat=4))
        for kc in (1, 0, -1):
            for combo in combos:
                ours, p2 = cv["ours"], cv["p2"]
                if combo is not None:
                    ours_spec = ("two*",) + ours[1:]
                    p2_spec = ("two*",) + p2[1:]
                else:
                    ours_spec, p2_spec = ours, p2
                t0 = time.time()
                res = solve_two_planes(kc, ours_spec, p2_spec, combo)
                adm = [r for r in res.get("sols", []) if r["admissible"]]
                rows.append({"conv": name, "k": kc, "signs": combo, "status": res["status"], "n_adm": len(adm),
                             "adm": adm, "secs": time.time() - t0, "mu_forced_zero": res.get("mu_forced_zero"),
                             "family_admissible": res.get("family_admissible")})
                if verbose:
                    print(name, kc, combo, res["status"], len(adm), "%.1fs" % (time.time() - t0))
    return rows


def flat_control(cv_name, combo=None):
    """mu = 0, k = 0: does the convention balance at every a (modulus)?  Phi constant; check the tt value."""
    cv = conventions()[cv_name]

    def phi(spec, signs):
        if spec[0] == "Z2":
            return 2 * spec[1], spec[2]
        if spec[0] == "Z2own":
            return 2 * spec[1] * sp.sqrt(spec[3]), spec[2]
        if spec[0] == "two":
            return spec[1] + spec[2] * sp.sqrt(spec[3]), spec[5]
        return signs[0] + signs[1] * sp.sqrt(spec[1]), spec[3]

    o, p = cv["ours"], cv["p2"]
    so = combo[:2] if combo else None
    sp2 = combo[2:] if combo else None
    P1, tau1 = phi(o, so)
    P2, tau2 = phi(p, sp2)
    return bool(sp.simplify(P1 + 2 * tau1) == 0), bool(sp.simplify(P2 + 2 * tau2) == 0)


# ------------------------------------------------------------------------------------------------ Q charged variant
def charged_lemma1():
    """Mirrored plane at RS, F = k u + 1 - mu u^2 + q^2 u^3: F = 1 and F' = 0."""
    mu, q = sp.symbols("mu q", positive=True)
    out = {}
    for kc in (1, 0, -1):
        F = Fslab(kc, mu, q)
        G = sp.groebner([F - 1, sp.diff(F, u)], mu, u, q, order="lex")
        out[kc] = G
    return out


def charged_two_planes(kc=1, conv="T1-M4", q_outer="same"):
    """Ours mirrored at RS in RN-AdS5 (forces mu = 2q, u1 = 1/q at k = 1); position 2 per convention, its outer bulk
    with the same charge (a neutral plane: flux continuous) or none."""
    cv = conventions()[conv]
    p2 = cv["p2"]
    q = sp.Symbol("q", positive=True)
    u2, s2, t2 = sp.symbols("u2 s2 t2", positive=True)
    mu = 2 * q
    if p2[0] == "two":
        eta_s, eta_o, lam2, mu_o, tau = p2[1:]
        Fs = kc * u2 + 1 - mu * u2**2 + q**2 * u2**3
        qo = q if q_outer == "same" else 0
        Fo = kc * u2 + lam2 - mu_o * u2**2 + qo**2 * u2**3
        eqs = [s2**2 - Fs, t2**2 - Fo, eta_s * s2 + eta_o * t2 + 2 * tau,
               sp.expand(eta_s * sp.diff(Fs, u2) * t2 + eta_o * sp.diff(Fo, u2) * s2)]
        unk = [q, s2, t2, u2]
    else:
        return {"status": "n/a (position 2 mirrored in its own bulk: the corridor is not between the planes)"}
    G = sp.groebner([sp.expand(e) for e in eqs], *unk, order="lex")
    if G.exprs == [1]:
        return {"status": "inconsistent", "G": G}
    sols = []
    if G.is_zero_dimensional:
        polys = G.exprs
        for sol in sp.solve(polys, unk, dict=True):
            vals = {kk: complex(sp.N(vv, 30)) for kk, vv in sol.items()}
            real = all(abs(z.imag) < 1e-20 for z in vals.values())
            pos = real and all(vals[x].real > 0 for x in unk)
            sols.append({"sol": sol, "vals": vals, "admissible": pos})
    return {"status": "zero-dim" if G.is_zero_dimensional else "positive-dim", "G": G, "sols": sols}


# ------------------------------------------------------------------------------------------------ M184 matter on the plane
def matter_limit():
    """Item 184 ("There are no matter free planes"): the pure-tension result is a limit.  With matter (rho_m, p_m) on
    our plane at the RS tension, J1 gives  sigma + rho_m = -(3/kappa^2) Phi,  -sigma + p_m = (a Phi' + 3 Phi)/kappa^2,
    so  rho_m + p_m = (a/kappa^2) Phi'(a):  EVERY position balances, the matter it needs fixed by (a, mu).  Computed for
    our plane mirrored (LR orbifold) and two-sided with a corridor-free far side, k = 1, 0, -1, ell = 1."""
    a, kap2 = sp.symbols("a kappa2", positive=True)
    mu = sp.Symbol("mu", real=True)
    out = {}
    for kc in (1, 0, -1):
        f = kc + a**2 - mu / a**2
        f0 = kc + a**2
        for name, Phi in (("mirrored", -2 * sp.sqrt(f) / a), ("two-sided", -(sp.sqrt(f) + sp.sqrt(f0)) / a)):
            sigma = 6 / kap2
            rho_m = sp.simplify(-3 * Phi / kap2 - sigma)
            nec = sp.simplify(a * sp.diff(Phi, a) / kap2)
            out[(kc, name)] = {"rho_m": rho_m, "rho_plus_p": nec}
    return out


def matter_signs():
    """Signs at k = 0 (our plane flat): for mu > 0 both rho_m < 0 and rho_m + p_m < 0 at every a (numbers checked on a
    grid, exact forms printed); mu < 0 gives both > 0; mu = 0 gives 0, 0."""
    d = matter_limit()
    a, kap2 = sp.symbols("a kappa2", positive=True)
    mu = sp.Symbol("mu", real=True)
    res = {}
    for name in ("mirrored", "two-sided"):
        r, n = d[(0, name)]["rho_m"], d[(0, name)]["rho_plus_p"]
        neg = all(float(r.subs({a: av, mu: mv, kap2: 1})) < 0 and float(n.subs({a: av, mu: mv, kap2: 1})) < 0
                  for av in (1.2, 2, 5, 30) for mv in (R_(1, 10), R_(1, 2), 1))
        pos = all(float(r.subs({a: av, mu: mv, kap2: 1})) > 0 and float(n.subs({a: av, mu: mv, kap2: 1})) > 0
                  for av in (1.2, 2, 5, 30) for mv in (-R_(1, 10), -R_(1, 2), -1))
        zero = sp.simplify(r.subs(mu, 0)) == 0 and sp.simplify(n.subs(mu, 0)) == 0
        res[name] = (neg, pos, zero)
    return res


# ------------------------------------------------------------------------------------------------ identification
def horizon_radius():
    """R_h^2 = (L^2/2)(-k + sqrt(k^2 + 4 mu/L^2)) (Kraus eq. 9, READ) -- checked against f(R_h) = 0."""
    mu, L = sp.symbols("mu L", positive=True)
    out = {}
    for kc in (1, 0, -1):
        Rh2 = L**2 / 2 * (-kc + sp.sqrt(kc**2 + 4 * mu / L**2))
        out[kc] = sp.simplify(kc + Rh2 / L**2 - mu / Rh2)
    return out


# ------------------------------------------------------------------------------------------------ report / selftest
def report(full_owner=False):
    print("sads5_balance.py -- item 181, Model A (Schwarzschild-AdS5 bulk, two static planes)\n")
    print("J0 K from the metric matches eta f'/(2 sqrt f), eta sqrt f / a:", j0())
    d = j1()
    print("J1 identities rho + 3 Phi/kappa^2 = %s ; p - (a Phi' + 3 Phi)/kappa^2 = %s ; RS control residues %s, %s"
          % (d["id_rho"], d["id_p"], d["rs_rho"], d["rs_p"]))
    print("J2 Kraus eq. (14) -> eq. (18) residual:", j2()["eq18_residual"])
    c = c0()
    print("C0 pure AdS5 flat: dPhi/da =", c["dPhi"], "; RS balances at every a:", c["rs_any_a"],
          "; off RS nowhere:", c["off_rs_none"])
    print("C0b owner t5c/lemma_t s2 at s1 = 1:", c0b())
    print("L1 mirrored at RS, static (u, mu) solutions with u > 0, by k:", lemma1(), "; proof:", lemma1_proof())
    print("C1 off RS (tau = 11/10), k = 1:", c1()["at_tau_11_10"])
    G2, far0 = lemma2()
    print("L2 two-sided at RS, masses free: Groebner last elements by k:",
          {kc: G2[kc].exprs[-1] for kc in G2}, "; far side mu = 0:", far0)
    print("   k = -1 family at Delta = 4:", lemma2_family(4), "; at Delta = 1/10 (spurious):", lemma2_family(R_(1, 10)))
    print("M4 owner:", MP.m4())
    if full_owner:
        b6 = _load(os.path.join(D68, "lemmas", "b6_k.py"), "kq_b6k")
        with contextlib.redirect_stdout(io.StringIO()):
            bd = b6.compute()
        print("b6_k B6a ratio k_R/k_L:", bd["ratio"], "tension ratio:", bd["kd"]["tension_ratio"])
    print("\nE  two planes, every convention:")
    for name in conventions():
        print("  flat control (mu = 0, k = 0, modulus) for", name, ":",
              flat_control(name) if conventions()[name]["ours"][0] != "two*" else "per sign combo")
    rows = enumerate_conventions()
    for r in rows:
        if r["n_adm"] or r["status"] == "positive-dim":
            print("  ", r["conv"], "k =", r["k"], r["signs"], r["status"], "admissible:",
                  [{str(kk): v for kk, v in a["sol"].items()} for a in r["adm"]])
    print("  rows:", len(rows), "with an admissible two-plane solution:", sum(1 for r in rows if r["n_adm"]))
    print("\nQ  charged: mirrored at RS:", {kc: G.exprs for kc, G in charged_lemma1().items()})
    for conv in ("T1-M4", "T2-sheet"):
        for qo in ("same", "none"):
            cq = charged_two_planes(1, conv, qo)
            print("  ", conv, "outer charge", qo, cq["status"], [(s["vals"], s["admissible"]) for s in cq.get("sols", [])])
    print("\nR_h check f(R_h) = 0:", horizon_radius())
    print("\nM184 matter on our plane at the RS tension (every a balances; the matter it needs):")
    for kk, v in matter_limit().items():
        print("  ", kk, "rho_m =", v["rho_m"], "; rho_m + p_m =", v["rho_plus_p"])
    print("   signs at k = 0 (mu>0 both negative, mu<0 both positive, mu=0 zero):", matter_signs())


def selftest(full_owner=False):
    ok = n = 0

    def chk(name, cond):
        nonlocal ok, n
        n += 1
        ok += bool(cond)
        print("  [%s] %s" % ("ok" if cond else "FAIL", name))

    chk("J0: K from Christoffels = eta f'/(2 sqrt f), eta sqrt f/a for k = 1, 0, -1", all(j0().values()))
    d = j1()
    chk("J1: rho = -(3/kappa^2) Phi and p = (a Phi' + 3 Phi)/kappa^2 exactly (owner israel per side)",
        d["id_rho"] == 0 and d["id_p"] == 0)
    chk("J1 control: mirrored flat AdS keeping R < a gives +sigma_RS = 6/(kappa^2 ell), p = -sigma_RS",
        d["rs_rho"] == 0 and d["rs_p"] == 0)
    a_, k2_, l_ = sp.symbols("a kappa2 ell", positive=True)
    Kt = -sp.diff(a_**2 / l_**2, a_) / (2 * sp.sqrt(a_**2 / l_**2))
    Ki = -sp.sqrt(a_**2 / l_**2) / a_
    r_mut, _ = S2F.israel([Kt, Ki, Ki, Ki], nu=2 / k2_, trace_from=1)
    chk("J1 mutation (owner israel's trace_from = 1, the spatial trace only): the RS control fails -- the check can fail",
        sp.simplify(r_mut - 6 / (k2_ * l_)) != 0)
    chk("J2: Kraus eq. (14) reproduces his eq. (18) exactly (READ source, computed check)", j2()["eq18_residual"] == 0)
    c = c0()
    chk("C0: pure AdS5, flat: Phi' = 0 identically for all four orientations (a flat plane balances anywhere)",
        all(v == 0 for v in c["dPhi"].values()))
    chk("C0: at the RS value a mirrored flat plane balances at every a; at tau = 0.9, 1.1 at none",
        c["rs_any_a"] and c["off_rs_none"])
    b = c0b()
    chk("C0b: owner t5c/lemma_t give s2 = -1 at s1 = 1, and this junction gives -1 for a mirrored plane keeping R > a",
        b["owner_s2"] == -1 and b["owner_fixed"] == -1 and b["here_s2"] == -1)
    L1 = lemma1()
    chk("L1: a mirrored plane at the RS value has no static position for mu != 0 (k = 1, 0, -1): only mu = 0 or none",
        all(all(s.get(sp.Symbol("mu", real=True), 0) == 0 for s in L1[kc]) for kc in L1))
    pr = lemma1_proof()
    chk("L1 proof: F(u*) - 1 = k^2/(4 mu) at u* = k/(2 mu)",
        sp.simplify(pr["F_minus_1_at_star"] - sp.Symbol("k", real=True)**2 / (4 * sp.Symbol("mu", real=True))) == 0)
    cc = c1()["at_tau_11_10"]
    chk("C1 control: off RS (tau = 11/10, k = 1) one static position, a^2 = 2 mu, mu = 25/21 (an equality appears)",
        len(cc) == 1 and cc[0][sp.Symbol("mu", positive=True)] == R_(25, 21)
        and sp.simplify(1 / cc[0][u] - 2 * R_(25, 21)) == 0)
    G2, far0 = lemma2()
    mp_, mm = sp.symbols("mu_p mu_m", real=True)
    tt = sp.Symbol("t", positive=True)
    chk("L2: two-sided at RS, any masses: k = 1 forces u = -2(t - 1)^2 <= 0 (no plane); k = 0 forces t = s = 1, mu = 0",
        any(sp.expand(e - (2 * tt**2 - 4 * tt + u + 2)) == 0 for e in G2[1].exprs)
        and any(sp.expand(e - (tt - 1)**2) == 0 for e in G2[0].exprs)
        and any(sp.expand(e - (mm * u**2 + 2 * tt - 2)) == 0 for e in G2[0].exprs)
        and any(sp.expand(e - (mm * tt - mm + mp_ * tt - mp_)) == 0 for e in G2[0].exprs))
    chk("L2: far side corridor-free: k = 1 none, k = 0 only mu = 0 (the control), k = -1 only mu = -27/8, u = 8/9 "
        "(a^2 = 9 ell^2/8); below -1/4: no horizon",
        far0[1] == [] and all(x[mp_] == 0 for x in far0[0]) and len(far0[-1]) == 1 and far0[-1][0][mp_] == R_(-27, 8)
        and far0[-1][0][u] == R_(8, 9) and not horizon_status(-1, R_(-27, 8)))
    fam = lemma2_family(4)
    bad = lemma2_family(R_(1, 10))
    chk("L2: the k = -1 family (Kraus eq. 18) at Delta = 4 satisfies both junctions to 1e-35, with mu_p = 0.110 > 0 (a "
        "horizon on the slab side) and mu_m = -3.890 < -1/4 (a naked far side)",
        abs(fam["res_T"]) < 1e-35 and abs(fam["res_N"]) < 1e-35 and fam["roots_positive"] and fam["horizon_p"]
        and not fam["horizon_m"])
    chk("L2 sign filter: at Delta = 1/10 eq. (18)'s static point has a negative root (spurious: a side not decaying)",
        not bad["roots_positive"] and abs(bad["res_T"]) > 1)
    m4 = MP.m4()
    chk("owner multiplane M4: k_R = 3 k_L/4, tensions +4/3, -1/3 of the outer one-plane value (T1's input)",
        sp.simplify(m4["kR"] - sp.Rational(3, 4) * MP.kL) == 0 and m4["tau2_over_rs"] == sp.Rational(-1, 3))
    chk("T1 flat control: ours (mirrored, RS) and position 2's single sheet (-1/8 = PRZ's -1/4) balance at every a",
        flat_control("T1-M4") == (True, True))
    chk("T1d control: the -1/4 placed on the single sheet with k_R = 3k_L/4 fails the flat control (K5's count matters)",
        flat_control("T1d-M4-quarter-on-sheet") == (True, False))
    chk("T2/T3/T4 and the four STAGE7 K4 rows pass the flat control (the rows rebuilt from the flat junction "
        "reproduce K4's curvatures)",
        all(flat_control(x) == (True, True) for x in ("T2-sheet", "T3-S6J3", "T4-S7K5", "S7-u2-1/3", "S7-u1-1/3-grow",
                                                       "S7-u1-1/6-grow", "S7-u1-1/6-decay")))
    rows = enumerate_conventions()
    rep = [r for r in rows if r["conv"] in ("T1-M4", "T2-sheet", "T3-S6J3", "T4-S7K5") or r["conv"].startswith("S7-")]
    chk("E: under every repository convention (T1-T4, STAGE7 K4's rows), k = 1, 0, -1: no admissible two-plane "
        "solution with the corridor",
        all(r["n_adm"] == 0 for r in rep))
    var = [r for r in rows if r["conv"] in ("V1-T1", "V2-T2")]
    chk("E: the board's non-mirrored variant, all 16 orientations, k = 1, 0, -1: no admissible solution",
        all(r["n_adm"] == 0 for r in var))
    chk("E: every positive-dimensional case forces the corridor to vanish (mu u1 in the ideal): the k = 0 modulus",
        all(r["mu_forced_zero"] for r in rows if r["status"] == "positive-dim"))
    chk("E control: the flat (k = 0) modulus is admissible exactly where the flat control passes (T1, T2, T3, T4, and "
        "the variant's LR orientation (-1,-1,+1,-1))",
        all(r["family_admissible"] for r in rows if r["k"] == 0 and (r["conv"] in ("T1-M4", "T2-sheet", "T3-S6J3",
                                                                                    "T4-S7K5") or r["conv"].startswith("S7-")))
        and [r["signs"] for r in rows if r["k"] == 0 and r["conv"] == "V1-T1" and r["family_admissible"]]
        == [(-1, -1, 1, -1)])
    st2 = lemma2_stability()
    Dl_ = sp.Symbol("D", positive=True)
    Rr_ = sp.Symbol("R", positive=True)
    chk("L2: the k = -1 family's static point is a maximum of Kraus's V: V'' = -(3/4) D^2/R^8 (unstable equilibrium)",
        sp.simplify(st2["Vpp"] + sp.Rational(3, 4) * Dl_**2 / Rr_**8) == 0)
    q, muq = sp.symbols("q mu", positive=True)
    CQ = charged_lemma1()
    chk("Q: charged, mirrored at RS: only k = 1 with mu = 2q, u = 1/q (k = 0, -1 none)",
        CQ[0].exprs == [1] or all(e.free_symbols <= {muq, u, q} for e in CQ[0].exprs))
    chk("Q: that charged bulk (k = 1, mu = 2q) has no horizon: f = (1 - q/R^2)^2 + R^2 > 0",
        not horizon_status(1, 2 * R_(3, 7), R_(3, 7)) and not horizon_status(1, 2 * R_(5, 1), R_(5, 1)))
    cq_ok = True
    for conv in ("T1-M4", "T2-sheet"):
        for qo in ("same", "none"):
            cq = charged_two_planes(1, conv, qo)
            cq_ok = cq_ok and not any(x["admissible"] for x in cq.get("sols", []))
    chk("Q: charged, ours mirrored at RS (k = 1, mu = 2q, a1^2 = q), position 2 under T1 or T2, outer charge q or 0: "
        "no admissible solution", cq_ok)
    chk("R_h: Kraus eq. (9) solves f(R_h) = 0 for k = 1, 0, -1", all(v == 0 for v in horizon_radius().values()))
    ms = matter_signs()
    chk("M184: with matter on our flat plane at the RS tension every a balances; a corridor of positive mass needs "
        "rho_m < 0 and rho_m + p_m < 0 there (NEC broken on the plane), mu < 0 gives both > 0, mu = 0 gives 0",
        all(v == (True, True, True) for v in ms.values()))
    if full_owner:
        b6 = _load(os.path.join(D68, "lemmas", "b6_k.py"), "kq_b6k")
        with contextlib.redirect_stdout(io.StringIO()):
            bd = b6.compute()
        chk("owner b6_k B6a: k_R/k_L = 3/4 and the tension ratio -1/4 (kderive K3)",
            bd["ratio"] == sp.Rational(3, 4) and bd["kd"]["tension_ratio"] == sp.Rational(-1, 4))
    print("selftest: %d/%d" % (ok, n))
    return ok == n


if __name__ == "__main__":
    full = "--owners-full" in sys.argv
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest(full) else 1)
    report(full)
