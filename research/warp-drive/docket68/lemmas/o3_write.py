#!/usr/bin/env python3
"""o3_write.py -- Warp Theorem lemma O3, M-RULINGS item 158: the write's least time, and what it does to the hold.
Computed, READ and deduced; verified once (findings applied, O3-WRITE.md History); not seated.
First headed "... not verified; not seated".

M's words (verbatim in the rulings file): item 158 (2) "Exactly as long as the write needs  I should think" (H-HOLD-AT-
BOUND, M's); (1), (3), (4) "for the math"; item 115 (c) "The README itself" (the opening's inflow is the README);
item 157 "we already have at least half the model, our current universe"; item 106 "horizon position 1 only as the
corridor opens".

READ
  Bekenstein & Schiffer, quant-ph/0311050 (Int. J. Mod. Phys. C 1 (1990) 355): eq. (85), p.20, H <= 2 pi E R/(hbar c);
    eq. (86), p.20, I-dot <= (2 pi E/hbar) log2 e for "bulk transport" ("a very special sort of communication");
    eq. (97), p.22, I-dot <= 0.2279 E/hbar (one channel, mean energy, self-heralding -- p.22: heralded signals can
    exceed it); eq. (112), p.24, I-dot <= E/(2 pi hbar) (one channel, energy ceiling, "valid regardless of whether the
    signal is heralded or not"); eq. (115), p.26, I-dot <= E/(2 pi hbar) log2(N_ch/ln2), N_ch >> 1 channels of a
    "simple communication system".
  't Hooft, gr-qc/9310026: eq. (1), p.3, S = 4 pi M^2 + C; eq. (2), p.4, e^S = dim of Hilbert space = 2^n; eq. (3),
    p.4, n = 4 pi M^2/ln2 = A/(4 ln2) (C dropped); pp.4-5, eqs. (4)-(5): for a surface whose content has not
    collapsed, "The most probable state would be a gas at some temperature", E = C1 Z V T^4, S = C2 Z V T^3, Z "the
    number of different fundamental particle types with mass less than T"; eq. (8), p.5, with energy up to the
    Schwarzschild limit 2E < R, S < C5 Z^(1/4) A^(3/4).

  W1 (STRUCTURAL) G1's E is the black-hole energy of N bits: 't Hooft's eq. (3) gives n = N, and eq. (85) is
     saturated at R = 2m.  True by G1's own construction (4 pi r_min^2 = N A_bit, r0 = 2m: H1, G3), not a finding.
  W2 THE RATE BOUNDS DO NOT DEPEND ON N (computed from READ).  E^2 is proportional to N, so N bits at a rate linear in E
     take a fixed number of clocks (m = G E/c^4, clock m/c): eq. (86) 2; eq. (97) 79.5; eq. (112) 8 pi^2/ln2 = 113.9;
     eq. (115) 113.9/log2(N_ch/ln2).  None decides the hold.
  W3 THE GAS BOUND (computed from READ eqs. (2), (4), (5), under named mappings).  The write is done when the README
     has crossed onto the throat at r = 2m (H-WRITE-IS-ARRIVAL).  Moving at most at c, all of it then lay, when the
     write began, inside the ball of radius (2 + T) m, T the write's length in clocks (advanced time, H-HOLD-FRAME),
     in flat space (H-FLAT-START, the board's gloss on 157), carrying only the README's energy E (H-README-ALONE).
     Before it collapses its number of states at fixed E and V is at most the free gas's (H-FREE-GAS, 't Hooft's "most
     probable state"); the constants are the Bose integral's (d = 3: Stefan-Boltzmann, the control).  N bits need
     e^S >= 2^N (H-BITS-ARE-STATES, the board's use of eq. (2)).  So, exact algebra in the thermodynamic limit without
     self-gravity,
            T >= (3645 ln2 N/(8 Z))^(1/3) - 2 clocks          (d = 3)
     Z is fixed by the gas's own temperature: at the bound T_gas = 4E/(3S) = 1/(3 pi m), 8/3 of the README hole's
     Hawking temperature, ~1.0e11 GeV at the example README -- every Standard Model species is lighter, so Z >= 108.75
     (106.75 and the graviton's 2).  At the example README: 2.0e5 clocks (Z = 108.75); 7.6e5 at Z = 2 (illustration);
     through the extra dimension (d = 4, a 4-ball of radius (2 + T) m, H-NO-SHORTCUT) the power is 1/4, 4.7e4 at Z = 2.
     Variants that need fewer hypotheses: dropping H-README-ALONE ('t Hooft's eq. (8), energy up to collapse) leaves
     N^(1/6) -- 630 clocks at Z = 108.75; prior entanglement (superdense coding, items 111, 137 (1)) halves the states
     needed -- 2^(-4/3) on 2 + T (the radius goes as bits^(4/3)/N), 3.0e5 at Z = 2.  Self-gravity: 2m/R ~ 1e-5 at the example README.
  W4 WHAT IT DOES TO THE HOLD (deduced; the choice of reading is the board's).  With 158 (2) the hold is the write.
     Two readings of where the write sits:
     (i)  H-WRITE-IN-STATIC-HOLD -- the write happens inside the static eq. (17) hold of b4_static.py.  That bulk is
          verified (heuristically) below 11.28 clocks, undecided above, K >= 100 from 14.9, the singular surface by
          about 18 (B4.md, the verifier's figure).  The write exceeds 11.28 above N ~ 7.41 Z bits (not certified) and
          18 above N ~ 25 Z (refuted): 2.6e3 bits at Z = 108.75.  At the example README the window would need Z > 3.7e14.
     (ii) THE WRITE IS THE OPENING -- under 115 (c) and H-PULL-IS-COST the corridor of mass m does not exist until the
          README has arrived, so the write is item 106's first hold, modelled as ingoing Vaidya (opening.py,
          R-VAIDYA-HOLDS), non-static by construction.  The bound is then a floor on the opening: 2.0e5 clocks at the
          example README, superseding opening.py O5's 4-clock Dyson floor by 5e4.  The static window is untouched.
     On either reading the bulk is not still through the write, and O3 waits on B4d.  H-HOLD-IN-WINDOW is refuted only
     on (i).  The members on which a refutation under (i) rests: M's 115 (c), 157, 158 (2); the board's
     H-WRITE-IN-STATIC-HOLD, H-WRITE-IS-ARRIVAL, H-FREE-GAS, H-BITS-ARE-STATES, H-SPECIES-FINITE, H-FLAT-START,
     H-README-ALONE (or eq. (8) in its place), H-HOLD-FRAME, H-PULL-IS-COST, H-EXACT-ENERGY-AT-BOUND (G1); the static
     bulk of b4_static.py (eq. (17) held, flat limit, its locally analytic class, Padé continuation).
  W5 LINEAR SURVIVAL IS NOT CERTIFIED OVER THE NEEDED HOLD (computed).  o3_hold.py's O3c factors over a hold of T
     clocks are T/4 (S4) and (1 + T/8)^2 (S5b): 5.0e4 and 6.2e8 at the example README (Z = 108.75).  They describe
     perturbations of the static corridor, so they apply on reading (i) only.
  In seconds the needed write is short: 1.3e-31 s at the example README (M's item 86 answer 5, "incredibly short,
  maybe even immeasurable but not zero"); in the corridor's clocks it is 1.8e4 times the static window.

CONTROLS  Stefan-Boltzmann at d = 3; the d = 4 Bose constant 3 zeta(5)/pi^2.  T rises with N and falls with Z.  At N =
  10 bits and Z = 2 the write fits the static window -- a real check, but formal: there m ~ 0.74 Planck masses and
  opening.py O5 already says the model breaks down for N of order 1.  STRUCTURAL (printed, counted as such): W1 with
  2E giving 4N; eq. (85) in place of the gas giving T >= 0 (W1 restated).

NOT DECIDED  158 (1) -- the gas bound holds for any mode of writing; 158 (4) -- d = 4 changes the power, not the
  verdict; where the energy goes is B4d's.  Which of readings (i), (ii) holds.

Imports lemmas/b4_static.py (its banked double cone), copy/exactE.py (E) and copy/opening.py (O5) by path.
Stdlib + sympy.  python3 o3_write.py [--selftest]
"""
import contextlib
import importlib.util
import io
import math
import os
import sys

import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
D68 = os.path.dirname(HERE)
WD = os.path.dirname(D68)
EXAMPLE_N = 2742570311524972
Z_HEAD = sp.Rational(10875, 100)              # the Standard Model's g* 106.75 and the graviton's 2 (W3: all lighter)
SINGULAR_CLOCKS = 18                          # B4.md: the singular surface by about 18 clocks (the verifier's figure)
E_PLANCK_GEV = 1.220890e19
G_SI, C_SI = 6.67430e-11, 299792458.0


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


N, Z, E = sp.symbols("N Z E", positive=True)
T = sp.Symbol("T", real=True)                                         # T >= 0 is a result, not an assumption
X = sp.Symbol("x", positive=True)                                     # x = 2 + T, the ball's radius in m


def m_squared():
    """m^2 in Planck units (hbar = c = G = 1, h = 2 pi), from G1's E^2 = N h c^5 ln2/(8 pi^2 G) and m = G E/c^4."""
    return sp.simplify(N * 2 * sp.pi * sp.log(2) / (8 * sp.pi**2))


def w1():
    m2 = m_squared()
    n_thooft = sp.simplify(4 * sp.pi * m2 / sp.log(2))                 # eq. (3), M = E = m in Planck units
    bek = sp.simplify(2 * sp.pi * sp.sqrt(m2) * 2 * sp.sqrt(m2) / sp.log(2))   # eq. (85) at R = 2m, in bits
    n_ctl = sp.simplify(4 * sp.pi * (4 * m2) / sp.log(2))              # 2E
    return n_thooft, bek, n_ctl


def w2():
    """Clocks for N bits at each READ rate bound; N cancels because E^2 is proportional to N."""
    m = sp.sqrt(m_squared())
    rate = {"(86) bulk transport": 2 * sp.pi * m / sp.log(2),
            "(97) one channel, mean energy, self-heralding": sp.Rational(2279, 10000) * m,
            "(112) one channel, energy ceiling": m / (2 * sp.pi)}
    clocks = {k: sp.nsimplify(sp.simplify((N / r) / m)) for k, r in rate.items()}
    nch = sp.Symbol("N_ch", positive=True)
    clocks["(115) N_ch >> 1 channels"] = sp.simplify((N / (m / (2 * sp.pi) * sp.log(nch / sp.log(2), 2))) / m)
    return clocks


def gas(d):
    """Free gas in d space dimensions, Z states: u = Z Omega_{d-1} Gamma(d+1) zeta(d+1) T^(d+1)/(2 pi)^d, s = (d+1)u/(dT);
    at energy E in volume V, S = a_d Z^(1/(d+1)) V^(1/(d+1)) E^(d/(d+1)).  Returns (u, s per state, a_d)."""
    omega = 2 * sp.pi**sp.Rational(d, 2) / sp.gamma(sp.Rational(d, 2))
    u = omega / (2 * sp.pi)**d * sp.gamma(d + 1) * sp.zeta(d + 1)
    s = sp.Rational(d + 1, d) * u
    V = sp.Symbol("V", positive=True)
    temp = (E / (Z * u * V))**sp.Rational(1, d + 1)
    S = sp.simplify(Z * s * V * temp**d)
    a = sp.simplify(S / (Z**sp.Rational(1, d + 1) * V**sp.Rational(1, d + 1) * E**sp.Rational(d, d + 1)))
    return sp.simplify(u), sp.simplify(s), a


def ball(d, r):
    return sp.pi**sp.Rational(d, 2) / sp.gamma(sp.Rational(d, 2) + 1) * r**d


def _solve_x(S, bits):
    sol = sp.solve(sp.Eq(S, bits * sp.log(2)), X)
    assert len(sol) == 1
    return sp.simplify(sol[0] - 2)


def t_min(d, bits=N):
    """Least write, in clocks: the gas of energy m in the d-ball of radius (2 + T) m holds 2^bits states."""
    m = sp.sqrt(m_squared())
    _, _, a = gas(d)
    return _solve_x(a * Z**sp.Rational(1, d + 1) * ball(d, X * m)**sp.Rational(1, d + 1) * m**sp.Rational(d, d + 1), bits)


def t_eq8():
    """Without H-README-ALONE: energy up to the Schwarzschild limit R/2 in the ball of radius R = (2 + T) m ('t Hooft eq. (8))."""
    m = sp.sqrt(m_squared())
    _, _, a = gas(3)
    R = X * m
    return _solve_x(a * Z**sp.Rational(1, 4) * ball(3, R)**sp.Rational(1, 4) * (R / 2)**sp.Rational(3, 4), N)


def t_bekenstein():
    """STRUCTURAL: eq. (85) in place of the gas -- 2 pi E R/ln2 >= N with R = (2 + T) m."""
    return sp.solve(sp.Eq(2 * sp.pi * m_squared() * (2 + T) / sp.log(2), N), T)[0]


def t_gas():
    """The gas's temperature at the bound, Planck units: 4E/(3S) with S = N ln2 = 4 pi m^2, E = m; and the Hawking
    temperature 1/(8 pi m) for comparison."""
    m = sp.sqrt(m_squared())
    return sp.simplify(4 * m / (3 * N * sp.log(2))), sp.simplify(1 / (8 * sp.pi * m))


def _num(expr, **kw):
    return float(expr.subs({N: kw.get("n", EXAMPLE_N), Z: kw.get("z", Z_HEAD)}).evalf(30))


def compute():
    b4 = _load(os.path.join(HERE, "b4_static.py"), "o3w_b4static").compute(live=False)
    cone = b4["cone"]
    v = float(cone["t_cert"])
    ex = _load(os.path.join(D68, "copy", "exactE.py"), "o3w_exactE")
    op = _load(os.path.join(D68, "copy", "opening.py"), "o3w_opening")
    e_sqrt = ex.e_per_sqrt_bit()
    clock_per_sqrt = G_SI * e_sqrt / C_SI**5                              # o3_hold.py's clock, per sqrt(bit)
    o5_clocks = op.tau_floor_per_sqrt_bit() / clock_per_sqrt              # opening.py O5's Dyson floor, in clocks
    clock_s = clock_per_sqrt * math.sqrt(EXAMPLE_N)
    t3, t4, t8 = t_min(3), t_min(4), t_min(3, bits=N / 2)
    te8 = t_eq8()
    tg, th = t_gas()
    edges = {"verified": v, "K >= 100": float(cone["t_fail_2"]), "singular (~18)": SINGULAR_CLOCKS}
    nstar = {k: sp.solve(sp.Eq(t3, e), N)[0] for k, e in edges.items()}
    zneed = sp.solve(sp.Eq(t3, v), Z)[0].subs(N, sp.Float(EXAMPLE_N, 30))
    nstar4 = sp.solve(sp.Eq(t4, v), N)[0]
    tex = _num(t3)
    return {"v": v, "edges": edges, "w1": w1(), "w2": w2(), "gas3": gas(3), "gas4": gas(4), "t3": t3, "t4": t4,
            "tb": t_bekenstein(), "te8": te8, "t_dense": t8, "tg": tg, "th": th,
            "tgas_gev": _num(tg) * E_PLANCK_GEV, "ex_t3": tex, "ex_t3_z2": _num(t3, z=2), "ex_t4_z2": _num(t4, z=2),
            "ex_t8": _num(te8), "ex_t8_z2": _num(te8, z=2), "ex_dense_z2": _num(t8, z=2),
            "t3_n10": _num(t3, n=10, z=2), "m_n10": math.sqrt(10 * math.log(2) / (4 * math.pi)),
            "nstar": {k: float(e / Z) for k, e in nstar.items()},
            "nstar_head": {k: float(e.subs(Z, Z_HEAD)) for k, e in nstar.items()},
            "nstar4_z2": float(nstar4.subs(Z, 2)), "z_need": float(zneed),
            "self_grav": 2 / (tex + 2), "ratio": {"Z = 108.75": tex / v, "Z = 2": _num(t3, z=2) / v,
                                                  "d = 4, Z = 2": _num(t4, z=2) / v, "eq. (8)": _num(te8) / v},
            "o5_clocks": o5_clocks, "o5_ratio": tex / o5_clocks,
            "clock_s": clock_s, "ex_seconds": tex * clock_s, "s4": tex / 4, "s5b": (1 + tex / 8)**2,
            "mono": (_num(t3, n=100, z=2) < _num(t3, n=1000, z=2), _num(t3, n=1000, z=2) > _num(t3, n=1000, z=20))}


def report(d):
    print("o3_write.py -- Warp Theorem lemma O3: the write's least time\n")
    n, b, _ = d["w1"]
    print("W1 (STRUCTURAL) 't Hooft eq. (3) with G1's E: n = %s; Bekenstein eq. (85) at R = 2m: %s bits" % (n, b))
    print("W2 the READ rate bounds, in clocks (independent of N):")
    for k, c in d["w2"].items():
        print("     %-48s %s%s" % (k, c, "" if c.free_symbols else "  = %.2f" % float(c)))
    print("W3 the gas bound: T >= %s clocks (d = 3)" % d["t3"])
    print("     gas temperature at the bound %s = %.3g x Hawking; %.2g GeV at the example README"
          % (d["tg"], float(sp.simplify(d["tg"] / d["th"])), d["tgas_gev"]))
    print("     example README: %.3g clocks (Z = 108.75); %.3g (Z = 2); d = 4 %.3g (Z = 2); eq. (8) %.3g (Z = 108.75); "
          "superdense %.3g (Z = 2)" % (d["ex_t3"], d["ex_t3_z2"], d["ex_t4_z2"], d["ex_t8"], d["ex_dense_z2"]))
    print("     self-gravity at the start 2m/R = %.2g" % d["self_grav"])
    print("W4 (i) the static bulk: N* = %s (x Z bits) at its edges %s;" % (
        ", ".join("%.3g" % x for x in d["nstar"].values()), ", ".join("%s %.2f" % kv for kv in d["edges"].items())))
    print("        at Z = 108.75: %s bits; d = 4 at Z = 2: %.0f; the window at the example README needs Z > %.2g"
          % (", ".join("%.0f" % x for x in d["nstar_head"].values()), d["nstar4_z2"], d["z_need"]))
    print("   (ii) the opening: floor %.3g clocks against opening.py O5's %.3g (x %.2g)"
          % (d["ex_t3"], d["o5_clocks"], d["o5_ratio"]))
    print("   the write over the static window: %s" % ", ".join("%s %.2g" % kv for kv in d["ratio"].items()))
    print("W5 over the needed hold (reading (i)): S4 %.2g natural sizes, S5b %.2g -- linear survival not certified"
          % (d["s4"], d["s5b"]))
    print("   in seconds at the example README: %.2g s" % d["ex_seconds"])


def selftest():
    ok = n = 0

    def chk(name, cond):
        nonlocal ok, n
        n += 1
        ok += bool(cond)
        print("  [%s] %s" % ("ok" if cond else "FAIL", name))

    d = compute()
    nt, bk, nc = d["w1"]
    chk("W1 (STRUCTURAL, by G1's construction): 't Hooft's eq. (3) gives n = N, eq. (85) at R = 2m gives N bits, 2E "
        "gives 4N", sp.simplify(nt - N) == 0 and sp.simplify(bk - N) == 0 and sp.simplify(nc - 4 * N) == 0)
    chk("W3 (STRUCTURAL, W1 restated): eq. (85) in place of the gas bound gives T >= 0", sp.simplify(d["tb"]) == 0)
    w = d["w2"]
    chk("W2: the READ rate bounds take N-independent clocks -- (86) 2, (97) 79.55, (112) 8 pi^2/ln2 = 113.91 > the "
        "static window", sp.simplify(w["(86) bulk transport"] - 2) == 0
        and sp.simplify(w["(112) one channel, energy ceiling"] - 8 * sp.pi**2 / sp.log(2)) == 0
        and abs(float(w["(97) one channel, mean energy, self-heralding"]) - 79.55) < 0.01
        and float(w["(112) one channel, energy ceiling"]) > d["v"])
    u3, s3, _ = d["gas3"]
    u4, _, _ = d["gas4"]
    chk("W3 controls: the Bose integral is Stefan-Boltzmann at d = 3 (pi^2/30, 2 pi^2/45) and 3 zeta(5)/pi^2 at d = 4",
        sp.simplify(u3 - sp.pi**2 / 30) == 0 and sp.simplify(s3 - 2 * sp.pi**2 / 45) == 0
        and sp.simplify(u4 - 3 * sp.zeta(5) / sp.pi**2) == 0)
    chk("W3: the gas bound is exactly T >= (3645 ln2 N/(8 Z))^(1/3) - 2 clocks; superdense coding puts 2^(-4/3) on 2 + T",
        sp.simplify(d["t3"] - ((3645 * sp.log(2) * N / (8 * Z))**sp.Rational(1, 3) - 2)) == 0
        and abs((d["ex_dense_z2"] + 2) / (d["ex_t3_z2"] + 2) - 2**(-4 / 3)) < 1e-12)
    chk("W3: the gas temperature at the bound is 1/(3 pi m) = 8/3 of the Hawking temperature, ~1.0e11 GeV at the example "
        "README -- above every Standard Model mass, so Z >= 108.75",
        sp.simplify(d["tg"] * 3 * sp.pi * sp.sqrt(m_squared()) - 1) == 0
        and sp.simplify(d["tg"] / d["th"] - sp.Rational(8, 3)) == 0 and 0.9e11 < d["tgas_gev"] < 1.2e11)
    chk("W3 control: T rises with N and falls with Z; at N = 10 bits (Z = 2) the write fits the static window (formal: "
        "m < 1 Planck mass there)", all(d["mono"]) and d["t3_n10"] < d["v"] and d["m_n10"] < 1)
    chk("W3: at the example README 2.00e5 clocks (Z = 108.75), 7.57e5 (Z = 2), 4.73e4 through the extra dimension, "
        "6.32e2 by eq. (8) without H-README-ALONE; self-gravity at the start below 1e-4",
        1.99e5 < d["ex_t3"] < 2.01e5 and 7.55e5 < d["ex_t3_z2"] < 7.58e5 and 4.70e4 < d["ex_t4_z2"] < 4.76e4
        and 625 < d["ex_t8"] < 640 and d["self_grav"] < 1e-4)
    chk("W4 (i): N* = 7.41 Z bits at the verified edge (not certified above), 25.3 Z at the singular surface (refuted "
        "above) -- 806 and 2.75e3 bits at Z = 108.75, 17 through the extra dimension at Z = 2; the window at the example "
        "README needs Z > 3.7e14", 7.40 < d["nstar"]["verified"] < 7.42 and 25.2 < d["nstar"]["singular (~18)"] < 25.4
        and 800 < d["nstar_head"]["verified"] < 812 and 2.7e3 < d["nstar_head"]["singular (~18)"] < 2.8e3
        and 16.5 < d["nstar4_z2"] < 17.5 and 3.6e14 < d["z_need"] < 3.8e14)
    chk("W4 (ii): opening.py O5's Dyson floor is 4 clocks; the gas bound exceeds it 5.0e4-fold at the example README",
        abs(d["o5_clocks"] - 4) < 1e-6 and 4.9e4 < d["o5_ratio"] < 5.1e4)
    chk("W4: every variant exceeds the static window -- 1.8e4 x (Z = 108.75), 6.7e4 (Z = 2), 4.2e3 (d = 4), 56 (eq. (8))",
        1.7e4 < d["ratio"]["Z = 108.75"] < 1.8e4 and 6.6e4 < d["ratio"]["Z = 2"] < 6.8e4
        and 4.1e3 < d["ratio"]["d = 4, Z = 2"] < 4.3e3 and 50 < d["ratio"]["eq. (8)"] < 60)
    chk("W5 (reading (i)): O3c's factors over the needed hold are T/4 = 5.0e4 and (1 + T/8)^2 = 6.2e8; the write is "
        "1.3e-31 s", 4.9e4 < d["s4"] < 5.1e4 and 6.1e8 < d["s5b"] < 6.3e8 and 1.2e-31 < d["ex_seconds"] < 1.4e-31)
    print("selftest: %d/%d" % (ok, n))
    return ok == n


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    report(compute())
