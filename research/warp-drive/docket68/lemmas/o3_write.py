#!/usr/bin/env python3
"""o3_write.py -- Warp Theorem lemma O3, M-RULINGS item 158: the write's least time, and whether the static bulk can hold
through it.  Computed and READ; not verified; not seated.

M's words (verbatim in the rulings file): item 158 (2) "Exactly as long as the write needs  I should think" (H-HOLD-AT-
BOUND, M's); (1), (3), (4) "for the math"; item 115 (c) "The README itself" (the opening's inflow is the README);
item 157 "we already have at least half the model, our current universe" (the write starts from our flat universe).

READ
  Bekenstein & Schiffer, quant-ph/0311050 (Int. J. Mod. Phys. C 1 (1990) 355): eq. (85), p.20, H <= 2 pi E R/(hbar c);
    eq. (86), p.20, I-dot <= (2 pi E/hbar) log2 e for "bulk transport" ("a very special sort of communication");
    eq. (97), p.22, I-dot <= 0.2279 E/hbar (one channel, mean energy); eq. (112), p.24, I-dot <= E/(2 pi hbar) (one
    channel, energy ceiling, "valid regardless of whether the signal is heralded or not"); eq. (115), p.26,
    I-dot <= E/(2 pi hbar) log2(N_ch/ln2) for N_ch >> 1 parallel channels.
  't Hooft, gr-qc/9310026: eq. (2), p.4, e^S = dim of Hilbert space = 2^n; eq. (3), p.4, n = 4 pi M^2/ln2 = A/(4 ln2)
    Boolean degrees of freedom for a black hole; pp.4-5, eqs. (4)-(5): for a surface whose content has not collapsed,
    "The most probable state would be a gas at some temperature", E = C1 Z V T^4, S = C2 Z V T^3, Z "the number of
    different fundamental particle types with mass less than T", "this entropy is small compared to that of a black
    hole, if the area A is sufficiently large".

  W1 THE README'S ENERGY IS THE BLACK-HOLE ENERGY OF N BITS (computed identity).  With G1's E, 't Hooft's eq. (3) gives
     n = N exactly, and the register at r = 2m saturates eq. (85): 2 pi E (2m)/(hbar c ln2) = N.  Control: 2E gives 4N.
  W2 THE RATE BOUNDS DO NOT DEPEND ON N (computed from READ).  E^2 is proportional to N, so N bits at a rate linear in E
     take a fixed number of clocks (m = G E/c^4, clock m/c): eq. (86) 2 clocks; eq. (112) 8 pi^2/ln2 = 113.9; eq. (97)
     79.5; eq. (115) 113.9/log2(N_ch/ln2).  A single one-dimensional channel (112) already needs more than the static
     bulk's ~11.3 clocks.
  W3 THE GAS BOUND (computed from READ eqs. (2), (4), (5)).  The write is done when the README has crossed onto the
     throat at r = 2m (H-WRITE-IS-ARRIVAL).  Moving at most at c, all of it then lay, when the write began, inside the
     ball of radius (2 + T) m, T the write's length in clocks, in our flat universe (157).  Before it collapses it is
     matter whose number of states at fixed E and V is at most the free gas's (H-FREE-GAS, 't Hooft's "most probable
     state"); the constants are the Bose integral's, u = Z Omega_{d-1} Gamma(d+1) zeta(d+1) T^(d+1)/(2 pi)^d (d = 3:
     Stefan-Boltzmann, the control).  N bits need e^S >= 2^N (eq. (2)).  So
            T >= (3645 ln2 N/(8 Z))^(1/3) - 2 clocks          (d = 3, exact)
     -- 7.6e5 clocks at the example README with Z = 2, 2.0e5 with the Standard Model's 106.75.  Through the extra
     dimension (d = 4, the 4-ball of radius (2 + T) m, generous) the power is 1/4, still 4.7e4 clocks there
     and N* about 17 bits at Z = 2.
  W4 THE STATIC BULK CANNOT HOLD THROUGH THE WRITE (computed).  With 158 (2) the hold is the write, so the hold is at
     least W3's T.  b4_static.py's static bulk is regular only for holds below ~11.3 clocks.  T exceeds that for every
     README above N* = 8 Z (v + 2)^3/(3645 ln2), about 7.41 Z bits (15 bits at Z = 2, 791 at 106.75); at the example
     README the window would need Z above 3.7e14 light species (H-SPECIES-FINITE, the board's).  What is refuted is a
     conjunction: M's 115 (c), 157, 158 (2) with the board's H-WRITE-IS-ARRIVAL, H-FREE-GAS, H-SPECIES-FINITE and the
     static bulk of b4_static.py (eq. (17) held, flat limit, its locally analytic class).  M's words are M's; the
     board's reading that gives way is the static bulk: the math's answer to 158 (3) is that the bulk is not still
     through the write -- it evolves (B4d).  So H-HOLD-IN-WINDOW is refuted for every README above N*, and O3 waits
     on B4d.
  W5 LINEAR SURVIVAL IS NOT CERTIFIED OVER THE NEEDED HOLD (computed).  o3_hold.py's O3c factors over a hold of T
     clocks are T/4 (S4) and (1 + T/8)^2 (S5b): 1.9e5 and 8.9e9 at the example README.  Linear theory cannot carry the
     corridor through the write; that too is B4d's, nonlinear.
  In seconds the needed write is short: T times the clock, 5e-31 s at the example README (M's item 86 answer 5,
  "incredibly short, maybe even immeasurable but not zero").

CONTROLS  Eq. (85) in place of the gas bound gives T >= 0 (the bound that bites is the gas's, not causality alone).  At
  N = 10 bits and Z = 2 the write fits the window (the refutation is N-dependent).  Stefan-Boltzmann at d = 3.
  W1 with 2E.  T increases with N and falls with Z.

NAMED HYPOTHESES  M's: H-INFLOW-IS-README (115 (c)), H-HALF-IS-OURS (157), H-HOLD-AT-BOUND (158 (2)).  The board's:
  H-WRITE-IS-ARRIVAL, H-FREE-GAS, H-SPECIES-FINITE, H-PULL-IS-COST (m = G E/c^4, the clock).  NOT DECIDED: 158 (1) --
  the gas bound holds for any mode of writing, so it does not choose one; 158 (4) -- d = 4 does not save the static
  bulk, but where the energy goes is B4d's.

Imports lemmas/b4_static.py (its banked double cone) and copy/exactE.py (E) by path.  Stdlib + sympy.  python3 o3_write.py [--selftest]
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
Z_SM = sp.Rational(42700, 400)                                       # 106.75, the Standard Model's g*


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


N, Z, R, E = sp.symbols("N Z R E", positive=True)
T = sp.Symbol("T", real=True)                                         # T >= 0 is a result, not an assumption


def m_squared():
    """m^2 in Planck units (hbar = c = G = 1, h = 2 pi), from G1's E^2 = N h c^5 ln2/(8 pi^2 G) and m = G E/c^4."""
    h = 2 * sp.pi
    return sp.simplify(N * h * sp.log(2) / (8 * sp.pi**2))


def w1():
    m2 = m_squared()
    n_thooft = sp.simplify(4 * sp.pi * m2 / sp.log(2))                 # eq. (3), M = E = m in Planck units
    bek = sp.simplify(2 * sp.pi * sp.sqrt(m2) * 2 * sp.sqrt(m2) / sp.log(2))   # eq. (85) at R = 2m, in bits
    n_ctl = sp.simplify(4 * sp.pi * (4 * m2) / sp.log(2))              # 2E
    return n_thooft, bek, n_ctl


def w2():
    """Clocks for N bits at each READ rate bound; N cancels because E^2 is proportional to N."""
    m2 = m_squared()
    m = sp.sqrt(m2)
    hbar = 1
    rate = {"(86) bulk transport": 2 * sp.pi * m / hbar / sp.log(2),
            "(97) one channel, mean energy": sp.Rational(2279, 10000) * m / hbar,
            "(112) one channel, energy ceiling": m / (2 * sp.pi * hbar)}
    clocks = {k: sp.nsimplify(sp.simplify((N / r) / m)) for k, r in rate.items()}
    nch = sp.Symbol("N_ch", positive=True)
    clocks["(115) N_ch channels"] = sp.simplify((N / (m / (2 * sp.pi) * sp.log(nch / sp.log(2), 2))) / m)
    return clocks


def gas(d):
    """Free-gas maximum entropy at energy E in volume V, d space dimensions, Z states: S = a_d Z^(1/(d+1)) V^(1/(d+1))
    E^(d/(d+1)); returns (u coefficient, s coefficient, a_d)."""
    t = sp.Symbol("t", positive=True)
    omega = 2 * sp.pi**sp.Rational(d, 2) / sp.gamma(sp.Rational(d, 2))
    u = omega / (2 * sp.pi)**d * sp.gamma(d + 1) * sp.zeta(d + 1)          # per state, times T^(d+1)
    s = sp.Rational(d + 1, d) * u
    V = sp.Symbol("V", positive=True)
    temp = (E / (Z * u * V))**sp.Rational(1, d + 1)
    S = sp.simplify(Z * s * V * temp**d)
    a = sp.simplify(S / (Z**sp.Rational(1, d + 1) * V**sp.Rational(1, d + 1) * E**sp.Rational(d, d + 1)))
    return sp.simplify(u), sp.simplify(s), a


def ball(d, r):
    return sp.pi**sp.Rational(d, 2) / sp.gamma(sp.Rational(d, 2) + 1) * r**d


def t_min(d):
    """Least write, in clocks: S(E = m, V = ball(d, (2+T) m)) = N ln2, solved for T."""
    m = sp.sqrt(m_squared())
    _, _, a = gas(d)
    S = a * Z**sp.Rational(1, d + 1) * ball(d, (2 + T) * m)**sp.Rational(1, d + 1) * m**sp.Rational(d, d + 1)
    x = sp.Symbol("x", positive=True)                                  # x = 2 + T, the ball's radius in m
    sol = sp.solve(sp.Eq(S.subs(T, x - 2), N * sp.log(2)), x)
    assert len(sol) == 1
    return sp.simplify(sol[0] - 2)


def t_bekenstein():
    """Control: eq. (85) in place of the gas -- 2 pi E R/ln2 >= N with R = (2 + T) m."""
    m2 = m_squared()
    return sp.solve(sp.Eq(2 * sp.pi * m2 * (2 + T) / sp.log(2), N), T)[0]


def compute():
    b4 = _load(os.path.join(HERE, "b4_static.py"), "o3w_b4static").compute(live=False)
    v = float(b4["cone"]["t_cert"])
    ex = _load(os.path.join(D68, "copy", "exactE.py"), "o3w_exactE")
    t3, t4 = t_min(3), t_min(4)
    f3 = lambda n, z: float(t3.subs({N: n, Z: z}).evalf(30))
    f4 = lambda n, z: float(t4.subs({N: n, Z: z}).evalf(30))
    nstar3 = sp.solve(sp.Eq(t3, v), N)[0]
    zneed = sp.solve(sp.Eq(t3, v), Z)[0].subs(N, sp.Float(EXAMPLE_N, 30))   # solved symbolically, then evaluated
    nstar4 = sp.solve(sp.Eq(t4, v), N)[0]
    clock_s = 6.67430e-11 * ex.e_per_sqrt_bit() * math.sqrt(EXAMPLE_N) / 299792458.0**5   # G E/c^5, o3_hold.py's clock
    tex = f3(EXAMPLE_N, 2)
    return {"v": v, "w1": w1(), "w2": w2(), "gas3": gas(3), "t3": t3, "t4": t4, "tb": t_bekenstein(),
            "ex_t3_z2": tex, "ex_t3_sm": f3(EXAMPLE_N, float(Z_SM)), "ex_t4_z2": f4(EXAMPLE_N, 2),
            "t3_n10": f3(10, 2), "nstar3": nstar3, "nstar3_z2": float(nstar3.subs(Z, 2)),
            "nstar3_sm": float(nstar3.subs(Z, Z_SM)), "nstar4_z2": float(nstar4.subs(Z, 2)), "z_need": float(zneed),
            "clock_s": clock_s, "ex_seconds": tex * clock_s, "s4": tex / 4, "s5b": (1 + tex / 8)**2,
            "mono": (f3(100, 2) < f3(1000, 2), f3(1000, 2) > f3(1000, 20))}


def report(d):
    print("o3_write.py -- Warp Theorem lemma O3: the write's least time\n")
    n, b, _ = d["w1"]
    print("W1 't Hooft eq. (3) with G1's E: n = %s; Bekenstein eq. (85) at R = 2m: %s bits" % (n, b))
    print("W2 the READ rate bounds, in clocks (independent of N):")
    for k, c in d["w2"].items():
        print("     %-36s %s%s" % (k, c, "" if c.free_symbols else "  = %.2f" % float(c)))
    print("W3 the gas bound: T >= %s clocks (d = 3)" % d["t3"])
    print("     example README: %.3g clocks (Z = 2), %.3g (Z = 106.75); through the extra dimension (d = 4): %.3g"
          % (d["ex_t3_z2"], d["ex_t3_sm"], d["ex_t4_z2"]))
    print("W4 the static bulk holds %.2f clocks: exceeded for N > %.3f Z = %.1f bits (Z = 2), %.0f (Z = 106.75); d = 4: %.0f;"
          % (d["v"], float(d["nstar3"] / Z), d["nstar3_z2"], d["nstar3_sm"], d["nstar4_z2"]))
    print("     at the example README the window needs Z > %.2g light species" % d["z_need"])
    print("W5 over the needed hold: S4 %.2g natural sizes, S5b %.2g -- linear survival not certified" % (d["s4"], d["s5b"]))
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
    chk("W1: with G1's E, 't Hooft's eq. (3) gives n = N and Bekenstein's eq. (85) at R = 2m gives N bits; control 2E "
        "gives 4N", sp.simplify(nt - N) == 0 and sp.simplify(bk - N) == 0 and sp.simplify(nc - 4 * N) == 0)
    w = d["w2"]
    chk("W2: the READ rate bounds take N-independent clocks -- (86) 2, (112) 8 pi^2/ln2 = 113.9 > the static bulk's "
        "window, (97) 79.5", sp.simplify(w["(86) bulk transport"] - 2) == 0
        and sp.simplify(w["(112) one channel, energy ceiling"] - 8 * sp.pi**2 / sp.log(2)) == 0
        and abs(float(w["(97) one channel, mean energy"]) - 79.55) < 0.05 and float(w["(112) one channel, energy ceiling"]) > d["v"])
    u, s, _ = d["gas3"]
    chk("W3 control: the Bose integral at d = 3 is Stefan-Boltzmann, u = pi^2/30, s = 2 pi^2/45 per state",
        sp.simplify(u - sp.pi**2 / 30) == 0 and sp.simplify(s - 2 * sp.pi**2 / 45) == 0)
    chk("W3: the gas bound is exactly T >= (3645 ln2 N/(8 Z))^(1/3) - 2 clocks",
        sp.simplify(d["t3"] - ((3645 * sp.log(2) * N / (8 * Z))**sp.Rational(1, 3) - 2)) == 0)
    chk("W3 control: Bekenstein's eq. (85) in place of the gas bound gives T >= 0 -- the gas bound is what bites",
        sp.simplify(d["tb"]) == 0)
    chk("W3 control: T rises with N and falls with Z; at N = 10 bits (Z = 2) the write fits the static window",
        all(d["mono"]) and d["t3_n10"] < d["v"])
    chk("W4: the static bulk's ~11.3 clocks are exceeded above N* ~ 7.41 Z bits (15 at Z = 2, 791 at 106.75); at the "
        "example README the gas bound is 7.6e5 clocks (Z = 2), 2.0e5 (106.75), 4.7e4 through the extra dimension, and "
        "the window would need Z > 1e14", 10.5 < d["v"] < 12 and 14 < d["nstar3_z2"] < 16 and 780 < d["nstar3_sm"] < 810
        and 7.4e5 < d["ex_t3_z2"] < 7.7e5 and 1.9e5 < d["ex_t3_sm"] < 2.1e5 and 4e4 < d["ex_t4_z2"] < 6e4
        and d["z_need"] > 1e14 and 10 < d["nstar4_z2"] < 30)
    chk("W5: over the needed hold O3c's factors are T/4 > 1e5 and (1 + T/8)^2 > 1e9 -- linear survival not certified; "
        "in seconds the write is ~5e-31 s", d["s4"] > 1e5 and d["s5b"] > 1e9 and 1e-31 < d["ex_seconds"] < 1e-30)
    print("selftest: %d/%d" % (ok, n))
    return ok == n


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    report(compute())
