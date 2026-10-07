#!/usr/bin/env python3
"""loose.py -- the loose ends the board can compute (M-RULINGS item 135, step 3).

Six computations on the corridor fixed by the input N (current.py; eq. 17 of Bronnikov-Kim gr-qc/0212112 at
r0 = 2m), each on the live row it answers or narrows.  Every constant is exact or named; the corridor's per-bit
coefficient is imported from exactE.py (which imports chain.py), never retyped.

  L1  RES-N1   the one exact energy E(N) against the build's floor at position 2
  L2  C8O-O7   the corridor's length: what eq. (17) at r0 = 2m leaves free
  L3  C8P-O5   r0 = 2m: how finely it is tuned, and the test-field potential
  L4  C8P-O2   the coinciding junction: two sheets at one place
  L5  C8P-O7   light rays that leave the plane, in the vacuum bulk
  L6  C8O-O1/2 the opening as a null shell: its energy, and where the junction fails

Stdlib + sympy.  python3 loose.py [--selftest]
"""
import contextlib
import importlib.util
import io
import os
import sys

import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
D68 = os.path.dirname(HERE)
WD = os.path.dirname(D68)

# SI 2019 exact
H = sp.Rational(662607015, 10**42)
C = sp.Integer(299792458)
KB = sp.Rational(1380649, 10**29)
EV = sp.Rational(1602176634, 10**28)
G = sp.Rational(66743, 10**15)            # CODATA 2018, entered exactly; u_r 2.2e-5 (item 98)
TNT_T = sp.Integer(4184) * 10**6          # J per tonne of TNT, by definition
N_SNAPSHOT = sp.Float("1.09e29")          # item 108's full atomic snapshot, as M was shown it (illustrative)
BOND_CEILING_EV = sp.Rational(1111, 100)  # H-BOND-CEILING: <= 11.11 eV per atom (the CO triple bond); NOT READ
T_SITE = sp.Integer(300)                  # H-SITE-T: a site at 300 K (illustrative)
T_CMB = sp.Rational(27255, 10000)         # the background today, K (Fixsen 2009; as carried in cmb/)


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


_C = {}


def owners():
    if not _C:
        _C["exactE"] = _load(os.path.join(D68, "copy", "exactE.py"), "res_exactE")
        _C["balance"] = _load(os.path.join(WD, "step1b", "balance.py"), "res_balance")
    return _C


r, m, y, k, l = sp.symbols("r m y k l", positive=True)
x = sp.Symbol("x", real=True)


def corridor(r0):
    """eq. (17): (g_tt, g_rr) in r."""
    return 1 - 2 * m / r, (1 - 3 * m / (2 * r)) / ((1 - 2 * m / r) * (1 - r0 / r))


# ------------------------------------------------------------------------------------------------ L1
def l1():
    o = owners()
    e = sp.Float(str(o["exactE"].e_per_sqrt_bit()), 30)             # J per sqrt(bit)
    n_ex = sp.Integer(o["exactE"].N_EXAMPLE)
    body = o["balance"].object_conserved()
    atoms = sp.Float(body["atoms"], 15)
    w_chem = atoms * BOND_CEILING_EV * EV                          # ceiling on bond energy to assemble the body
    land = lambda T: KB * T * sp.log(2)                            # J per bit written
    out = {"e": e, "E_ex": e * sp.sqrt(n_ex), "w_chem": w_chem, "atoms": atoms,
           "N_eq_chem": (w_chem / e) ** 2}                         # E(N) = w_chem
    for name, T in (("site", T_SITE), ("cmb", T_CMB)):
        out["N_land_" + name] = (e / land(T)) ** 2                 # E(N) = N k T ln2
        out["land_ex_" + name] = n_ex * land(T)
    out["excess_ex"] = out["E_ex"] - out["w_chem"] - out["land_ex_site"]
    out["excess_ex_Mt"] = out["excess_ex"] / TNT_T / 10**6
    out["E_snap"] = e * sp.sqrt(N_SNAPSHOT)
    out["E_snap_kg"] = out["E_snap"] / C**2
    # item 108's crossover, two disjoint paths: from the coefficient, and from 8 pi^2 G M^2 / (h c ln2)
    M = sp.Integer(70)
    out["Nstar_coeff"] = (M * C**2 / e) ** 2
    out["Nstar_formula"] = 8 * sp.pi**2 * G * M**2 / (H * C * sp.log(2))
    return out


# ------------------------------------------------------------------------------------------------ L2
def l2():
    gtt, grr = corridor(2 * m)
    integrand = sp.sqrt(sp.factor(grr))                            # proper radial length per dr at fixed t
    res_floor = sp.limit((r - 2 * m) * integrand, r, 2 * m)        # a simple pole: length diverges as m ln
    gtt_w, grr_w = corridor(sp.Rational(11, 5) * m)                # control: r0 = 2.2 m, the two-way wormhole
    blow_w = sp.limit((r - sp.Rational(11, 5) * m) * sp.sqrt(grr_w) ** 2, r, sp.Rational(11, 5) * m)
    # the parameters left free: eq. (17) has (m, r0); the holds fix r0 = 2m, the input fixes m
    mm, r0, mN = sp.symbols("mm r0 m_N", positive=True)
    sol = sp.solve([r0 - 2 * mm, mm - mN], [mm, r0], dict=True)
    return {"pole_residue": sp.simplify(res_floor), "wormhole_grr_order": sp.simplify(blow_w),
            "solutions": sol, "free_after": 2 - 2 if len(sol) == 1 else None}


# ------------------------------------------------------------------------------------------------ L3
def kappa(r0):
    """Surface gravity of the r = 2m horizon for 3m/2 <= r0 <= 2m: (1/2) g_tt' / sqrt(g_tt g_rr) at r = 2m."""
    gtt, grr = corridor(r0)
    prod = sp.simplify(gtt * grr)
    return sp.simplify(sp.Rational(1, 2) * sp.diff(gtt, r).subs(r, 2 * m) / sp.sqrt(prod.subs(r, 2 * m)))


def potential(r0, ll):
    """Test scalar: V = g_tt l(l+1)/r^2 + (1/2r) d/dr (g_tt/g_rr)."""
    gtt, grr = corridor(r0)
    ab = sp.simplify(gtt / grr)
    return sp.factor(sp.simplify(gtt * ll * (ll + 1) / r**2 + sp.diff(ab, r) / (2 * r)))


def l3():
    d = sp.symbols("delta")
    kap = sp.simplify(kappa(2 * m * (1 + d)))                       # r0 = 2m(1+delta), delta < 0
    o = owners()
    e = sp.Float(str(o["exactE"].e_per_sqrt_bit()), 30)
    m_ex = G * e * sp.sqrt(sp.Integer(o["exactE"].N_EXAMPLE)) / C**4
    t_coeff = (H / (2 * sp.pi)) * C / (2 * sp.pi * KB) / (2 * m_ex)  # T = (hbar c / 2 pi k_B) kappa, kappa = sqrt(-d)/2m
    V0 = potential(2 * m, 0)
    V0s = potential(sp.Rational(3, 2) * m, 0)                       # Schwarzschild member, the control
    return {"kappa_delta": kap, "kappa_floor": kappa(2 * m), "kappa_schw": kappa(sp.Rational(3, 2) * m),
            "T_coeff_ex": t_coeff, "m_ex": m_ex, "V0": V0, "V0_schw": V0s,
            "V0_order_at_throat": sp.limit(V0 / (r - 2 * m) ** 2, r, 2 * m),
            "V0s_order_at_horizon": sp.limit(V0s / (r - 2 * m), r, 2 * m)}


# ------------------------------------------------------------------------------------------------ L4
def l4():
    """Israel junction at a hypersurface in a vacuum AdS5 bulk, metric e^{-2k|y|} on each side (Z2) or e^{-2ky}
    through it (no Z2).  [K_mn] - g_mn [K] = -kappa5^2 S_mn, with S_mn = -lambda g_mn for pure tension; coinciding
    sheets add their S (the condition is linear in S)."""
    kap5, l1_, l2_ = sp.symbols("kappa5 lambda1 lambda2", positive=True)
    g4 = sp.diag(-1, 1, 1, 1)
    def K(sign):                                                    # K_mn = (1/2) d_y g at y = 0 on one side
        return sign * (-k) * g4
    out = {}
    for name, jump in (("Z2", K(1) - K(-1)), ("smooth", K(1) - K(1))):
        trK = sum(jump[i, i] * g4[i, i] for i in range(4))
        lhs = jump - g4 * trK
        lam = sp.symbols("lam")
        sol = sp.solve(sp.Eq(lhs[1, 1], -kap5**2 * (-lam) * g4[1, 1]), lam)
        out[name] = sol[0]
    return out


# ------------------------------------------------------------------------------------------------ L5
def l5():
    """Vacuum AdS5, ds^2 = e^{-2ky} eta + dy^2 off our plane (y >= 0, K = -k g as closedbulk.py's K = -a q).
    z = e^{ky}/k makes it (1/(kz)^2)(eta + dz^2): null rays are straight lines in (t, x, z)."""
    th, ys = sp.symbols("theta y_s", positive=True)
    z0 = 1 / k
    zs = sp.exp(k * ys) / k
    dt_cross = (zs - z0) / sp.sin(th)                               # conformal-time to reach layer y_s
    lam_horizon = sp.integrate(1 / (k * sp.Symbol("z", positive=True)) ** 2, (sp.Symbol("z", positive=True), z0, sp.oo))
    # control: the other sign (warp growing away), z = e^{-ky}/k falls to the boundary z = 0
    dt_boundary = z0 / sp.sin(th)
    return {"dt_cross": sp.simplify(dt_cross), "affine_to_horizon_per_unit": lam_horizon,
            "dt_boundary_other_sign": dt_boundary}


# ------------------------------------------------------------------------------------------------ L6
def l6():
    """A spherical null shell at v = v1 between a region with no corridor and the corridor (Barrabes-Israel; with
    lambda = -r on both sides the surface energy density is mu = [m_MS]/(4 pi r^2), m_MS = (r/2)(1 - 1/g_rr))."""
    gtt, grr = corridor(2 * m)
    mms = sp.factor(sp.simplify(r / 2 * (1 - 1 / grr)))
    # the generator's areal radius: corridor r = 2m + x^2 (a minimum), no-corridor side r falls to 0
    gen_corr = 2 * m + x**2
    gtt_s, grr_s = corridor(sp.Rational(3, 2) * m)                  # control: Schwarzschild exterior
    mms_s = sp.simplify(r / 2 * (1 - 1 / grr_s))
    return {"mMS": mms, "mMS_throat": sp.simplify(mms.subs(r, 2 * m)), "mMS_inf": sp.limit(mms, r, sp.oo),
            "dmMS": sp.factor(sp.diff(mms, r)), "gen_min": sp.solve(sp.diff(gen_corr, x), x), "mMS_schw": mms_s}


# ------------------------------------------------------------------------------------------------ report
def _f(v, n=6):
    return sp.N(v, n)


def report():
    a, b, c3, d4, e5, f6 = l1(), l2(), l3(), l4(), l5(), l6()
    print("loose.py -- the loose ends the board can compute (item 135, step 3)\n")
    print("L1 RES-N1: the one exact energy against the build's floor at position 2")
    print("  E per sqrt(bit) %s J (exactE.py); E at the example N %s J" % (_f(a["e"], 12), _f(a["E_ex"], 10)))
    print("  build ceiling: %s atoms x %s eV (H-BOND-CEILING) = %s J" % (_f(a["atoms"]), _f(BOND_CEILING_EV, 4),
                                                                       _f(a["w_chem"])))
    print("  E(N) equals that ceiling at N = %s bits" % _f(a["N_eq_chem"]))
    print("  Landauer N k_B T ln2 equals E(N) at N = %s bits (300 K), %s bits (2.7255 K)"
          % (_f(a["N_land_site"]), _f(a["N_land_cmb"])))
    print("  at the example N: Landauer %s J (300 K); E - ceiling - Landauer = %s J = %s Mt of TNT"
          % (_f(a["land_ex_site"]), _f(a["excess_ex"], 8), _f(a["excess_ex_Mt"], 5)))
    print("  at the atomic snapshot N = 1.09e29: E = %s J = %s kg x c^2" % (_f(a["E_snap"]), _f(a["E_snap_kg"])))
    print("  item 108's crossover N* (70 kg): %s from the coefficient, %s from 8 pi^2 G M^2/(h c ln2)"
          % (_f(a["Nstar_coeff"], 8), _f(a["Nstar_formula"], 8)))
    print("\nL2 C8O-O7: the corridor's length")
    print("  sqrt(g_rr) at r0 = 2m has a simple pole at the throat, residue %s: the length at fixed t diverges as m ln"
          % b["pole_residue"])
    print("  control r0 = 2.2m: (r - r0) g_rr -> %s, an integrable 1/sqrt singularity: a finite length" %
          b["wormhole_grr_order"])
    print("  eq. (17)'s two parameters under the two conditions (holds; input): %s -- none left free" % b["solutions"])
    print("\nL3 C8P-O5: r0 = 2m tuning, and the test field")
    print("  surface gravity at r0 = 2m(1+delta): %s; at delta = 0: %s; Schwarzschild member: %s"
          % (c3["kappa_delta"], c3["kappa_floor"], c3["kappa_schw"]))
    print("  T = %s K x sqrt(-delta) at the example N (m = %s m)" % (_f(c3["T_coeff_ex"]), _f(c3["m_ex"])))
    print("  V(l=0) at r0 = 2m: %s" % c3["V0"])
    print("    double zero at the throat (V/(r-2m)^2 -> %s); Schwarzschild's simple zero (V/(r-2m) -> %s)"
          % (c3["V0_order_at_throat"], c3["V0s_order_at_horizon"]))
    print("\nL4 C8P-O2: two sheets at one place")
    print("  total tension the junction needs: with Z2 %s; through a smooth bulk %s" % (d4["Z2"], d4["smooth"]))
    print("\nL5 C8P-O7: rays leaving the plane (vacuum AdS5, y >= 0)")
    print("  conformal time to reach layer y_s: %s; never returns; affine parameter to the horizon %s per unit E"
          % (e5["dt_cross"], e5["affine_to_horizon_per_unit"]))
    print("  control, warp growing away: the boundary in time %s" % e5["dt_boundary_other_sign"])
    print("\nL6 C8O-O1/2: the opening as a null shell")
    print("  m_MS(r) = %s; at the throat %s; at infinity %s; dm_MS/dr = %s"
          % (f6["mMS"], f6["mMS_throat"], f6["mMS_inf"], f6["dmMS"]))
    print("  the corridor's generator r = 2m + x^2 has its minimum at x = %s; the side without a corridor falls to "
          "r = 0: no single shell joins whole generators" % f6["gen_min"])
    print("  control, Schwarzschild exterior: m_MS = %s (constant), r monotone on both sides: the shell joins"
          % f6["mMS_schw"])


def selftest():
    ok = n = 0

    def chk(name, cond):
        nonlocal ok, n
        n += 1
        ok += bool(cond)
        print("  [%s] %s" % ("ok" if cond else "FAIL", name))

    a, b, c3, d4, e5, f6 = l1(), l2(), l3(), l4(), l5(), l6()
    chk("L1: E per sqrt(bit) is exactE's 459404002.42356985091 J (to the float exactE hands the ledger, 1e-15)",
        abs(a["e"] / sp.Float("459404002.42356985091", 25) - 1) < 1e-15)
    chk("L1: item 108's crossover agrees by two disjoint paths (coefficient; closed form) to 1e-12",
        abs(a["Nstar_coeff"] / sp.N(a["Nstar_formula"], 30) - 1) < 1e-12)
    chk("L1: E(N) passes the build ceiling for every N above %s bits, and Landauer stays below E(N) to N = %s (300 K)"
        % (_f(a["N_eq_chem"], 3), _f(a["N_land_site"], 3)),
        a["N_eq_chem"] < 1000 and a["N_land_site"] > 1e58 and a["excess_ex"] > 0.9999 * a["E_ex"])
    chk("L1 control: Landauer's crossover scales as 1/T^2 (300 K against 2.7255 K)",
        abs(a["N_land_cmb"] / a["N_land_site"] - (T_SITE / T_CMB) ** 2) / ((T_SITE / T_CMB) ** 2) < 1e-20)
    chk("L2: the throat at r0 = 2m is at infinite length (pole residue m)", sp.simplify(b["pole_residue"] - m) == 0)
    chk("L2 control: at r0 = 2.2m g_rr has only a simple pole, so the length is finite",
        b["wormhole_grr_order"] != sp.oo and b["wormhole_grr_order"] != 0)
    chk("L2: eq. (17) at the holds and the input leaves no free parameter (one solution)", len(b["solutions"]) == 1)
    chk("L3: surface gravity vanishes at r0 = 2m and is 1/(4m) at the Schwarzschild member (control)",
        sp.simplify(c3["kappa_floor"]) == 0 and sp.simplify(c3["kappa_schw"] - 1 / (4 * m)) == 0)
    Vn = sp.lambdify(r, c3["V0"].subs(m, 1))
    samples = [2 + 10 ** (-j) for j in range(1, 8)] + [2.5, 3, 5, 10, 100, 1e4]
    chk("L3: V(l=0) >= 0 for r >= 2m (its factors 3r-4m, (r-2m)^2, m are non-negative); sampled",
        all(Vn(s) >= 0 for s in samples) and c3["V0"].has(3 * r - 4 * m) and c3["V0"].has((r - 2 * m) ** 2))
    chk("L3: the throat is a double zero of V (power-law tails), against Schwarzschild's simple zero",
        c3["V0_order_at_throat"] not in (0, sp.oo) and c3["V0s_order_at_horizon"] not in (0, sp.oo))
    chk("L4: coinciding sheets need total tension 6k/kappa5^2 with Z2, 0 through a smooth bulk",
        sp.simplify(d4["Z2"] - 6 * k / sp.Symbol("kappa5", positive=True) ** 2) == 0 and d4["smooth"] == 0)
    chk("L5: a ray leaving the plane reaches the horizon at finite affine parameter 1/k and never returns",
        sp.simplify(e5["affine_to_horizon_per_unit"] - 1 / k) == 0)
    chk("L5 control: with the warp growing away the ray reaches the boundary in finite time 1/(k sin theta)",
        e5["dt_boundary_other_sign"].has(sp.sin(sp.Symbol("theta", positive=True))))
    chk("L6: the opening shell's energy is positive and rises from m at the throat to 5m/4 at infinity",
        sp.simplify(f6["mMS_throat"] - m) == 0 and sp.simplify(f6["mMS_inf"] - sp.Rational(5, 4) * m) == 0 and
        sp.simplify(f6["dmMS"] - m**2 / (2 * (2 * r - 3 * m) ** 2)) == 0)
    chk("L6: the corridor's generators have a minimum radius (x = 0); control: Schwarzschild's m_MS is constant m",
        f6["gen_min"] == [0] and sp.simplify(f6["mMS_schw"] - m) == 0)
    print("selftest: %d/%d" % (ok, n))
    return ok == n


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    report()
