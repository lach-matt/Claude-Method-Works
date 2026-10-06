#!/usr/bin/env python3
"""
carrier.py -- a carrier through the bulk (M-RULINGS item 88, link 2: O6, against D13).  Deduced, computed, READ.
SEATED (ledger section 8n, M-D68-89; first written 'Not seated'); verified twice (2026-10-06).  M's words are carried as hypotheses, never as results.

The faithful copy's README (faithful.py: an identity core of order 1e15 bits) must cross from position 1 to position 2.
D13: classical information travels at or below c IN THE METRIC ITS CARRIER PROPAGATES IN.  A carrier through the bulk
propagates in the bulk's metric, so D13 alone does not bound it on our plane (S5's note, O6).  This asks when a bulk
path can arrive before light along the plane, what the board's carriers are, and what M's ruling that "the cost is in
how much information is transferred as a README" (item 89, H-COST-IN-README) makes of the port.

WHAT FOLLOWS THE WORK
  * THE TEST FOR A FASTER-THAN-LIGHT CORRIDOR (C1, C2).  For a static bulk the exact test is Fermat's: a path through
    the bulk beats light along the plane iff its OPTICAL length (the metric h_ij / N^2) is shorter than the plane's.
    Computed on paths that leave the plane and return: in RS1's warp, and in a bulk with a non-trivial g_yy, no path
    is shorter (the theorem, evaluated: with equal warps the integrand is >= 1 pointwise); the CONTROL (time and space
    warped differently) finds one shorter.  In a bulk with 4D Poincare
    symmetry, g_ab positive definite and both planes at fixed y, no causal curve beats the plane's light time -- the
    standard result (Csaki-Erlich-Grojean, READ), generalising bulk.py (2)'s own RS statement.  A shortcut needs at
    least one of these broken: the bulk's symmetry (unequal warping; a bulk that varies along the plane, which is what
    a LOCAL corridor is; planes in relative motion; a bulk changing in time) or the plane's embedding (bent: Ishihara;
    folded: the Manyfold -- both already seated in pairing.py), or g_ab's signature.  So M's corridor, if it beats
    light, is a place where the bulk's optical metric is shorter than the plane's along the route, or where the
    plane's embedding is not flat.
    First written: "THE CONDITION FOR A FASTER-THAN-LIGHT CORRIDOR IS NAMED EXACTLY" and "So M's corridor, if it beats
    light, is a place where the bulk is warped unequally for time and space" -- the list was not exhaustive, C1 was
    presented as new, and its numerical check could not fail (History).
  * GW170817 DOES NOT BOUND A LOCAL CORRIDOR (C3).  Gravitons arrived with light to within -3e-15..+7e-16 of c over at
    least 26 Mpc (READ), under H-SIMULTANEOUS-EMISSION; with LIGO's exotic emission window the faster side widens by
    about two orders.  What that bounds is the asymmetry WEIGHTED BY THE GRAVITON ZERO MODE (CEG eq. 3.25), on the
    branch where the graviton crosses the bulk -- not a corridor confined to a device's neighbourhood.  Unequal
    warping makes faster gravitational signals the generic case (CEG, READ).  On the Proxima line a global asymmetry
    could save at most 9.4e-8 s (the same 7e-16 fraction as O7's 93.8 ns; H-BOUND-TRANSFERS).
  * THE PORT IS WHERE M'S COST LANDS, AND IT DOES NOT COLLAPSE (C4).  Through zeromode's rotor family the identity core
    loads no faster than the printed best arm allows (of order 1e5 years), on the classical capacity of a bosonic mode
    (Giovannetti et al., READ) with an ideal lossless receiver and a bandwidth of order the wave frequency
    (H-BANDWIDTH-F).  Above the best arm (about 4 m) larger rotors are SLOWER: at fixed tip speed the frequency falls
    as 1/a while the gravitons pile into fewer modes.  The README's size sets the port time: at every arm the time is
    proportional to it, so the faithful copy's 3.5e12-fold reduction is the factor between loading the snapshot and
    loading the core.  First written "Larger rotors are SLOWER" and "wherever one bit per graviton holds".
    First written: "a 1 km rotor of the same tip speed and density in 0.53 s" -- zeromode's H-BIT-PER-GRAVITON
    ladder, which fails where more than one graviton falls in a mode (History).
  * Boundary (item 82): in RS1 as the board seats it (bulk.py), the bulk keeps 4D Poincare symmetry by construction
    (RS: the tensions are "required in order to obtain a solution that respects four-dimensional Poincare
    invariance", as crossing.py READ it) and the planes sit at fixed y, so there the README crosses at or below c.
    The escape classes are the board's open items: an unequally warped bulk needs an exotic bulk fluid to keep
    Newton's law on our plane (BULK3-O5) and may need NEC violation somewhere (BULK2-O2; Gao-Wald's Theorem 2 is
    suggestive and not directly applicable); a compact bulk with moving planes needs our boost B relative to the
    preferred frame, unmeasured (O7).

    python3 carrier.py              report
    python3 carrier.py --selftest   checks, CONTROLS and CONTRASTS marked, STRUCTURAL printed and not counted
    python3 carrier.py --json       the numbers as JSON

C1 [computed, exact; the standard result]  Let the bulk metric be ds^2 = e^{2A(y)} eta_{mu nu} dx^mu dx^nu +
   g_ab(y) dy^a dy^b, with g_ab positive definite (4D Poincare-invariant slices; the symmetry itself forbids g_{mu a}
   terms and a second warp factor, so "static" is implied).  Along a causal curve e^{2A}(dt^2 - |dx|^2) =
   g_ab dy^a dy^b + (non-negative) >= 0, so |dx| <= dt at every step.  bulk.py (2) states this for RS ("every causal
   curve has dt >= int sqrt(dx^2 + dz^2) >= |dx|"); C1 is its generalisation to any A(y) and any number of extra
   dimensions.  CEG (hep-th/0012143v3) write the equal-warp metric as eq. 1.1 (p.1) and contrast it with unequal
   warping, which "globally violates 4D Lorentz invariance" (p.2).
   The NUMERICAL test is Fermat's (static bulk, planes at fixed y): T[y(x)] = int sqrt(gxx/gtt + gyy/gtt y'^2) dx
   over paths y(x) that leave the plane at x = 0 and return at x = L, minimised over a family of dives; light along
   the plane takes L.  CONTROL: ds^2 = -e^{2A}dt^2 + e^{2B}dx^2 + dy^2 with B < A for y < 0.
C2 [deduced; the board's and READ]  A shortcut needs at least one premise of C1 broken:
   (i)   unequal warping (Chung-Freese; CEG: "gravitational waves may travel with a speed different from the speed of
         light on the brane, and possibly even faster", abstract p.1; pairing.py, cfgravity.py: Newton's law on our
         plane needs a bulk fluid with c_s^2 = -1/2, BULK3-O5);
   (ii)  a bulk that varies along the plane's directions (a LOCAL corridor; not covered by C1's slices);
   (iii) a compact bulk with planes in relative motion (branelink.py: the saving depends on B, O7);
   (iv)  a bulk changing in time (not modelled);
   (v)   the plane's embedding not at fixed y: the BENT plane (Ishihara, pairing.py (2): RS's own AdS bulk, the brane
         bent by brane matter) and the FOLDED plane (the Manyfold, ADDK, pairing.py (3): ADD's flat bulk);
   (vi)  g_ab not positive definite (a second time dimension).
   For static bulks, Fermat's optical metric is the exact criterion, and it covers (ii) and (v) as well.
   First written: "(i) ... (ii) ... (iii)", "the board holds three such classes" -- (ii), (v) and (vi) were missing.
C3 [READ]  LIGO-Virgo, Fermi-GBM, INTEGRAL, 1710.05834v2 (alphaXiv): "constrain the difference between the speed of
   gravity and the speed of light to be between -3 x 10^-15 and +7 x 10^-16 times the speed of light" (abstract, p.1);
   eq. 1, p.6, with D = 26 Mpc "the lower bound of the 90% credible interval"; the upper bound assumes "the peak of
   the GW signal and the first photons were emitted simultaneously" (H-SIMULTANEOUS-EMISSION) and the lower that the
   SGRB "was emitted 10 s after"; "certain exotic scenarios can extend this time difference window to (-100 s,
   1000 s), yielding a 2 orders of magnitude broadening" (p.6).  The observed delay "1.74 +/- 0.05 s" (p.1); 1.74 s
   over the 26 Mpc light time is 6.5e-16, which LIGO print as 7e-16.
   CEG: the zero mode's speed excess is >= 0 and carries e^{2 k y_R} from asymmetry anywhere in the bulk (eq. 3.25,
   p.21); a geodesic's average speed "will depend on the value of E/|p|" (p.19) -- so GW170817 bounds the
   zero-mode-weighted asymmetry, not the speed of a ray that dives deep; "the possible values of mu and Q could be
   severly [sic] constrained" (p.23).  Fermat: if c(r) decreases away from the brane, "no discrepancy" (p.16).
C4 [computed from the owners; capacity READ]  zeromode.rotor_load_time (imported) gives the graviton rate at one bit per
   graviton (H-BIT-PER-GRAVITON, zeromode's); the rotor scales at fixed tip speed and density (zeromode's scaling:
   m ~ a^3, f ~ 1/a; at a = 1 km, 5e11 kg each at 0.1 Hz, waves at 0.2 Hz).  The CEILING: Giovannetti, Guha, Lloyd,
   Maccone, Shapiro, Yuen, quant-ph/0308012v2 (alphaXiv): C = max sum_k g(eta_k N_k), g(x) = (x+1) log2(x+1) -
   x log2 x (eq. 4, p.1); one mode, C = g(E/hbar omega) per use (eq. 14, p.3).  Here B = f_GW uses per second
   (H-BANDWIDTH-F), N = (graviton rate)/B, eta = 1 (lossless, ideal receiver: an upper limit on rate, so a lower
   limit on load time).  I = faithful.py's identity core (imported).

NAMED HYPOTHESES AND PREMISES
  H-STATIC-WARP: C1's bulk has 4D Poincare-invariant slices, g_ab positive definite, planes at fixed y.
  H-RS1 (carried): our plane is RS1's negative-tension plane.
  H-BOUND-TRANSFERS: GW170817's bound, measured on one line of sight to NGC 4993, applies to gravitons on the Proxima
    line.  H-SIMULTANEOUS-EMISSION: LIGO's own premise for +7e-16.
  H-BIT-PER-GRAVITON (zeromode's; holds only while N <= 1 per mode); the illustrative rotor (zeromode's LAB_ROTOR).
  H-BANDWIDTH-F: the rotor's usable bandwidth is of order its wave frequency f_GW (one use per 1/f_GW).
  H-GW-ANALOGY: Gao-Wald's boundary theorem read as suggestive for a brane, which is not a conformal boundary.
  M's: H-COST-IN-README (item 89), H-ADDRESS-INPUT (item 86), H-INFORMATION-CROSSES (item 86).

OPEN
  1. A corridor geometry that breaks C1's premises locally -- a bulk whose optical metric is shorter along a route
     near a device -- with its energy conditions (with BULK2-O2, BULK3-O5).  Gao-Wald (gr-qc/0007021v2, READ): under
     the NEC and the null generic condition, "any 'fastest null geodesic' connecting two points on the boundary must
     lie entirely within the boundary", so "generic perturbations of anti-de Sitter spacetime always produce a time
     delay" (abstract; Theorem 2, pp.12-13).  Suggestive that a shortcut needs NEC violation; not directly
     applicable, since an RS plane is not AdS's conformal boundary (H-GW-ANALOGY).
  2. A time-dependent bulk (C2 iv).
  3. A port faster than gravitational emission: the bulk scalar of stabilisation (BULK3-O3), or the planes' own fields
     at the corridor's mouth.
  4. Reception: single-graviton detection at these frequencies is unpriced (a 0.2 Hz graviton carries about 1e-34 J,
     far below kT at 300 K; printed), and plausibly beyond any known measurement.  C4 prices emission only.
     First written: "Whether one bit per graviton can be reached (H-BIT-PER-GRAVITON)".
  5. In a bulk that keeps C1's premises, the trip takes the port time plus at least the light time (phase1's span).

HISTORY (verifier, 2026-10-06; first-written claims kept above, each where it stood)
  * C1's random-curve check took dy and the fastest dx at each step, so dx/dt = sqrt(1 - u^2) whatever the warp: it
    could not fail (RS1 and the second metric both printed 0.876005), and its curves never returned to the plane.
    It is now STRUCTURAL ("the identity, evaluated"); the counted test is Fermat's, on returning paths.  The sympy
    line is a string match and is STRUCTURAL too.  "warp2", first labelled "a two-dimensional warp", has one extra
    coordinate: it is now "a bulk with a non-trivial g_yy".
  * C1 is bulk.py (2)'s statement generalised, and a standard result (CEG); first presented as new.
  * The escape list was not exhaustive (the bent and folded planes, a bulk varying along the plane, a second time).
  * C4's 0.536 s at 1 km is zeromode's ladder under H-BIT-PER-GRAVITON, which fails there (of order 1e16 gravitons per
    mode); the ceiling is g(N).  At 1 m the assumption UNDERCOUNTS.
  * Second pass (verifier of uses.py, 2026-10-06): the two equal-warp Fermat checks cannot fail for any equal-warp
    input (the integrand is >= 1 pointwise) and are STRUCTURAL ("the theorem, evaluated"); the C3 Proxima line and
    the C4 linearity CONTRAST recompute their own formulas and are STRUCTURAL.  11/11 became 7/7.
  * The Proxima span is imported (phase1.L_PROXIMA, seat's own via settle); first retyped as 4.24 ly.
  * C3 now names H-SIMULTANEOUS-EMISSION and the exotic window, and its check pins LIGO's rounding rather than a 1 s
    tolerance.
"""
import contextlib
import importlib.util
import io
import json
import math
import os
import random
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
D68 = os.path.dirname(HERE)
BULK = os.path.join(D68, "bulk")
WD = os.path.dirname(D68)

# READ, 1710.05834v2
GW_DV_MIN, GW_DV_MAX = -3e-15, 7e-16
GW_D_MPC = 26.0
GW_DELAY_S = 1.74
GW_EXOTIC_WINDOW_S = (-100.0, 1000.0)    # p.6

C = 299792458.0
HPL = 6.62607015e-34                 # J s (SI, exact)
KB = 1.380649e-23                    # J/K (SI, exact)
MPC_M = 3.0856775814913673e22        # one megaparsec in m (standard)
K_RS = 1.0                           # C1's warp scale (units of 1/length; the check is scale-free)
YEAR_S = 3.15576e7                   # Julian year (display only)


def _load(name, path, key):
    spec = importlib.util.spec_from_file_location(key, path)
    m = importlib.util.module_from_spec(spec)
    saved = list(sys.path)
    try:
        sys.path.insert(0, WD)
        sys.path.insert(0, os.path.dirname(path))
        with contextlib.redirect_stdout(io.StringIO()):
            spec.loader.exec_module(m)
    finally:
        sys.path[:] = saved
    return m


_CACHE = {}


def owners():
    if not _CACHE:
        _CACHE["zeromode"] = _load("zeromode", os.path.join(BULK, "zeromode.py"), "bulk_zeromode_carrier")
        _CACHE["faithful"] = _load("faithful", os.path.join(HERE, "faithful.py"), "copy_faithful_carrier")
        _CACHE["phase1"] = _load("phase1", os.path.join(WD, "phase1.py"), "wd_phase1_carrier")
    return _CACHE["zeromode"], _CACHE["faithful"], _CACHE["phase1"]


def proxima_m():
    return owners()[2].L_PROXIMA


# ---------------------------------------------------------------------------------------------------- C1
def rs1(y):
    a = math.exp(-2 * K_RS * abs(y))
    return a, a, 1.0


def gyy_bulk(y):                     # one extra coordinate, equal warp, a non-trivial g_yy
    a = math.exp(-2 * K_RS * abs(y)) * (1 + 0.5 * math.sin(3 * y) ** 2)
    return a, a, 1.0 + 0.3 * math.cos(y) ** 2


def unequal(y):                      # CONTROL: time and space warped differently, B < A where y < 0
    A = -K_RS * abs(y)
    B = A - 0.5 * (1 if y < 0 else 0)
    return math.exp(2 * A), math.exp(2 * B), 1.0


DIVES = [(s * d, p) for s in (-1, 1) for p in (1, 2) for d in (0.01, 0.03, 0.1, 0.3, 0.6, 1.0, 1.5, 2.0, 3.0)]


def fermat_time(metric, path, L=10.0, n=4000):
    """Arrival time along y = path(x), x in [0, L] (both ends on the plane y = 0), for a static metric
    ds^2 = -gtt dt^2 + gxx dx^2 + gyy dy^2: T = int sqrt(gxx/gtt + gyy/gtt y'^2) dx (midpoint rule)."""
    h = L / n
    T = 0.0
    for i in range(n):
        x = (i + 0.5) * h
        y = path(x)
        yp = (path(x + 1e-6) - path(x - 1e-6)) / 2e-6
        gtt, gxx, gyy = metric(y)
        T += math.sqrt(gxx / gtt + gyy / gtt * yp * yp) * h
    return T


def dive(depth, p, L=10.0):
    return lambda x: depth * math.sin(math.pi * x / L) ** p


def fermat_dives(metric, L=10.0):
    """Every returning dive's arrival time over light along the plane (L, since gtt = gxx = 1 on y = 0): the shortest,
    and the dive that gives it."""
    rows = [(fermat_time(metric, dive(dp, p, L), L) / L, (dp, p)) for dp, p in DIVES]
    return min(rows)


def max_speed_on_plane(metric, trials=2000, steps=60, seed=7):
    """STRUCTURAL ("the identity, evaluated"): each step takes dy and the fastest causal dx for it, so the result is
    sqrt(gtt/gxx) * sqrt(1 - u^2) and does not test the warp.  Kept, never counted (History)."""
    rng = random.Random(seed)
    worst = 0.0
    for _ in range(trials):
        y, t, x = 0.0, 0.0, 0.0
        for _ in range(steps):
            dt = 1e-2
            gtt, gxx, gyy = metric(y)
            room = gtt * dt * dt
            dy = rng.uniform(-1, 1) * math.sqrt(room / gyy)
            dx = math.sqrt(max(room - gyy * dy * dy, 0.0) / gxx)
            t, x, y = t + dt, x + dx, y + dy
        worst = max(worst, x / t)
    return worst


def c1_symbolic():
    """e^{2A}(dt^2 - dx^2) - gyy dy^2 = 0 on a null curve, solved for dx/dt (the derivation; STRUCTURAL)."""
    import sympy as sp
    A, dt, dy, g = sp.symbols("A dt dy g", real=True)
    dx = sp.symbols("dx", positive=True)
    sol = sp.solve(sp.Eq(sp.exp(2 * A) * (dt ** 2 - dx ** 2) - g * dy ** 2, 0), dx)
    return [sp.simplify((s / dt) ** 2) for s in sol]


# ---------------------------------------------------------------------------------------------------- C4
def g_bits(x):
    """Giovannetti et al. eq. 4: g(x) = (x+1) log2(x+1) - x log2 x."""
    if x <= 0:
        return 0.0
    return (math.log1p(x) + x * math.log1p(1.0 / x)) / math.log(2)     # the same, without cancellation at large x


def port(a_m, I):
    """The rotor of arm a (zeromode's scaling): graviton rate, wave frequency, gravitons per mode, the H-BIT-PER-
    GRAVITON load time (zeromode's) and the g(N) ceiling's load time (H-BANDWIDTH-F, lossless)."""
    zm = owners()[0]
    base = zm.LAB_ROTOR
    s = a_m / base["a_m"]
    f_gw = 2.0 * base["f_rot_hz"] / s
    rate = 1.0 / zm.rotor_load_time(a_m, 1.0)            # gravitons per second
    N = rate / f_gw
    cap = f_gw * g_bits(N)                               # bits per second, at most
    return {"a_m": a_m, "m_each_kg": base["m_each_kg"] * s ** 3, "f_rot_hz": base["f_rot_hz"] / s, "f_gw_hz": f_gw,
            "gravitons_per_s": rate, "N_per_mode": N, "load_bit_per_graviton_s": zm.rotor_load_time(a_m, I),
            "ceiling_bits_per_s": cap, "load_ceiling_s": I / cap, "graviton_J": HPL * f_gw}


def best_arm(I, lo=0.1, hi=1e4, n=4001):
    best = None
    for i in range(n):
        a = lo * (hi / lo) ** (i / (n - 1))
        t = port(a, I)["load_ceiling_s"]
        if best is None or t < best[1]:
            best = (a, t)
    return best


def n1_arm(lo=0.1, hi=1e4):
    """The arm at which the gravitons per mode reach 1 (H-BIT-PER-GRAVITON's edge)."""
    for _ in range(200):
        mid = math.sqrt(lo * hi)
        if port(mid, 1.0)["N_per_mode"] >= 1.0:
            hi = mid
        else:
            lo = mid
    return hi


def min_arm_within(budget_s, I, lo=0.1, hi=1e4, n=4001):
    """Smallest arm whose ceiling load time fits a budget, or None (exported for uses.py)."""
    for i in range(n):
        a = lo * (hi / lo) ** (i / (n - 1))
        if port(a, I)["load_ceiling_s"] <= budget_s:
            return a
    return None


# ---------------------------------------------------------------------------------------------------- compute
def compute():
    zm, fa, _ = owners()
    core = fa.identity_core()["total_bits"]
    snapshot = fa._measure()["species"]
    gw_light_s = GW_D_MPC * MPC_M / C
    prox_light_s = proxima_m() / C
    exotic_fast = (GW_DELAY_S - GW_EXOTIC_WINDOW_S[0]) / gw_light_s
    exotic_slow = (GW_EXOTIC_WINDOW_S[1] - GW_DELAY_S) / gw_light_s
    ba = best_arm(core)
    return {"fermat_rs1": fermat_dives(rs1), "fermat_gyy": fermat_dives(gyy_bulk),
            "fermat_unequal": fermat_dives(unequal),
            "identity_rs1": max_speed_on_plane(rs1), "identity_gyy": max_speed_on_plane(gyy_bulk),
            "symbolic": [str(s) for s in c1_symbolic()],
            "gw_light_s": gw_light_s, "gw_delay_over_light": GW_DELAY_S / gw_light_s,
            "gw_max_saving_s": GW_DV_MAX * gw_light_s, "exotic_fast": exotic_fast, "exotic_slow": exotic_slow,
            "proxima_m": proxima_m(), "proxima_light_s": prox_light_s, "proxima_max_saving_s": GW_DV_MAX * prox_light_s,
            "proxima_exotic_saving_s": exotic_fast * prox_light_s,
            "core_bits": core, "snapshot_bits": snapshot,
            "ports": {a: port(a, core) for a in (1.0, 10.0, 100.0, 1000.0)},
            "best_arm_m": ba[0], "best_load_s": ba[1], "n1_arm_m": n1_arm(),
            "port_snapshot_1m_bit_s": zm.rotor_load_time(1.0, snapshot), "kT_300K_J": KB * 300.0}


def report():
    d = compute()
    print("carrier.py -- a carrier through the bulk (M item 88, link 2; verified twice; seated, ledger 8n)\n")
    print("C1 Fermat, shortest returning dive / light along the plane: RS1 %.6f, g_yy bulk %.6f; CONTROL (unequal) %.4f "
          "(dive %s)" % (d["fermat_rs1"][0], d["fermat_gyy"][0], d["fermat_unequal"][0], d["fermat_unequal"][1]))
    print("   STRUCTURAL the identity, evaluated: %.6f, %.6f ; null curve (dx/dt)^2 = %s" % (
        d["identity_rs1"], d["identity_gyy"], d["symbolic"]))
    print("C3 GW170817: 1.74 s / %.4e s = %.2e (printed 7e-16); at +7e-16 a graviton saves at most %.2f s over 26 Mpc; "
          "exotic window: +%.2e / -%.2e" % (d["gw_light_s"], d["gw_delay_over_light"], d["gw_max_saving_s"],
                                            d["exotic_fast"], d["exotic_slow"]))
    print("   Proxima (phase1, %.6e m): light %.4e s; global asymmetry saves at most %.3e s (exotic %.2e s)" % (
        d["proxima_m"], d["proxima_light_s"], d["proxima_max_saving_s"], d["proxima_exotic_saving_s"]))
    print("C4 the identity core (%.3e bits) through zeromode's rotors:" % d["core_bits"])
    for a, p in d["ports"].items():
        print("   arm %g m: %.3g kg each, waves %.3g Hz, %.3g gravitons/s, %.3g per mode; bit-per-graviton %.3g s; "
              "ceiling %.3g bits/s -> %.3g s (%.3g yr)" % (a, p["m_each_kg"], p["f_gw_hz"], p["gravitons_per_s"],
                                                         p["N_per_mode"], p["load_bit_per_graviton_s"],
                                                         p["ceiling_bits_per_s"], p["load_ceiling_s"],
                                                         p["load_ceiling_s"] / YEAR_S))
    print("   fastest at the ceiling: arm %.2f m, %.3g s (%.3g yr); one graviton per mode at arm %.2f m" % (
        d["best_arm_m"], d["best_load_s"], d["best_load_s"] / YEAR_S, d["n1_arm_m"]))
    print("   a %.3g Hz graviton carries %.3g J; kT at 300 K is %.3g J" % (
        d["ports"][1000.0]["f_gw_hz"], d["ports"][1000.0]["graviton_J"], d["kT_300K_J"]))


def selftest():
    n_pass = n_fail = n_ctl = n_con = 0
    structural = []

    def chk(label, ok, ctl=False, contrast=False):
        nonlocal n_pass, n_fail, n_ctl, n_con
        n_ctl += ctl
        n_con += contrast
        n_pass += bool(ok)
        n_fail += (not ok)
        print("  %s %s%s" % ("ok  " if ok else "FAIL", "CONTROL: " if ctl else ("CONTRAST: " if contrast else ""), label))

    d = compute()
    chk("C1 Fermat: with time and space warped differently, a returning dive arrives at %.4f of the plane's light time"
        % d["fermat_unequal"][0], d["fermat_unequal"][0] < 0.95, ctl=True)
    chk("C3: LIGO's +7e-16 is the 1.74 s delay over the 26 Mpc light time (%.3e) rounded to one figure" %
        d["gw_delay_over_light"], float("%.0e" % d["gw_delay_over_light"]) == GW_DV_MAX)
    chk("C3: the exotic window (-100 s, 1000 s) broadens each side by about two orders (+%.2e against +7e-16, -%.2e "
        "against -3e-15), as LIGO print" % (d["exotic_fast"], d["exotic_slow"]),
        1.5 < math.log10(d["exotic_fast"] / GW_DV_MAX) < 2.5 and 1.5 < math.log10(d["exotic_slow"] / -GW_DV_MIN) < 2.5)
    p1, pk = d["ports"][1.0], d["ports"][1000.0]
    lo_r = g_bits(1e-6) / (1e-6 * math.log2(math.e / 1e-6))
    hi_r = g_bits(1e6) / math.log2(math.e * 1e6)
    chk("C4: g(N) tends to N log2(e/N) for N << 1 and to log2(eN) for N >> 1 (ratios %.6f, %.6f)" % (lo_r, hi_r),
        abs(lo_r - 1) < 1e-4 and abs(hi_r - 1) < 1e-6)
    chk("C4: at 1 m (N = %.3f per mode) the ceiling, %.1f bits/s, exceeds one bit per graviton (%.2f/s): there the "
        "assumption undercounts" % (p1["N_per_mode"], p1["ceiling_bits_per_s"], p1["gravitons_per_s"]),
        p1["N_per_mode"] < 1 and p1["ceiling_bits_per_s"] > p1["gravitons_per_s"])
    chk("C4: at 1 km (N = %.2e per mode) the ceiling gives %.3g s, against zeromode's %.3g s under H-BIT-PER-GRAVITON"
        % (pk["N_per_mode"], pk["load_ceiling_s"], pk["load_bit_per_graviton_s"]),
        pk["N_per_mode"] > 1e10 and pk["load_ceiling_s"] > 1e13 * pk["load_bit_per_graviton_s"])
    chk("C4: the fastest rotor is interior (arm %.2f m, %.3g s); smaller and larger arms are slower (1 m: %.3g s; "
        "1 km: %.3g s)" % (d["best_arm_m"], d["best_load_s"], p1["load_ceiling_s"], pk["load_ceiling_s"]),
        1.0 < d["best_arm_m"] < 100.0 and pk["load_ceiling_s"] > d["best_load_s"] < p1["load_ceiling_s"])
    structural.append("C1 Fermat, the theorem evaluated: with gxx = gtt the integrand sqrt(1 + gyy/gtt y'^2) is >= 1 "
                      "pointwise, so no equal-warp dive can beat light (RS1 %.6f, g_yy bulk %.6f); the CONTROL is the "
                      "live test.  First counted as two checks (History)" % (d["fermat_rs1"][0], d["fermat_gyy"][0]))
    structural.append("C3 the Proxima saving, 7e-16 x D/c = %.3e s (its own formula; first counted)" %
                      d["proxima_max_saving_s"])
    structural.append("C4 the port time is linear in the README at every arm, in both columns (snapshot / core = %.3e, "
                      "the bit ratio; first counted as a CONTRAST)" % (d["port_snapshot_1m_bit_s"] /
                                                                      p1["load_bit_per_graviton_s"]))
    structural.append("C1 the identity, evaluated on random curves: RS1 %.6f, g_yy bulk %.6f -- equal by construction "
                      "(History)" % (d["identity_rs1"], d["identity_gyy"]))
    structural.append("C1 the derivation (sympy): (dx/dt)^2 = %s" % d["symbolic"])
    structural.append("C2: the escape classes are the board's open items (BULK3-O5, BULK2-O2, O7) or seated shortcuts "
                      "(pairing.py's bent and folded planes); none is computed here")
    structural.append("C4 prices emission; reception (single gravitons of %.2g J) is unpriced (OPEN 4)" %
                      pk["graviton_J"])
    for s_ in structural:
        print("  STRUCTURAL: " + s_)
    print("carrier.py: %d/%d checks pass, %d of them controls and %d contrasts; %d STRUCTURAL printed, not counted" % (
        n_pass, n_pass + n_fail, n_ctl, n_con, len(structural)))
    return n_fail == 0


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    elif "--json" in sys.argv:
        print(json.dumps(compute(), indent=1, default=str))
    else:
        report()
