#!/usr/bin/env python3
"""
carrier.py -- a carrier through the bulk (M-RULINGS item 88, link 2: O6, against D13).  Deduced, computed, READ.  Not
seated; not verified.  M's words are carried as hypotheses, never as results.

The faithful copy's README (faithful.py: an identity core of order 1e15 bits) must cross from position 1 to position 2.
D13: classical information travels at or below c IN THE METRIC ITS CARRIER PROPAGATES IN.  A carrier through the bulk
propagates in the bulk's metric, so D13 alone does not bound it on our plane (S5's note, O6).  This asks when a bulk
path can arrive before light along the plane, what the board's carriers are, and what M's ruling that "the cost is in
how much information is transferred as a README" (item 89, H-COST-IN-README) makes of the port.

WHAT FOLLOWS THE WORK
  * THE CONDITION FOR A FASTER-THAN-LIGHT CORRIDOR IS NAMED EXACTLY (C1, C2).  A bulk path between two points of one
    plane can arrive before light along the plane only if the bulk BREAKS the plane's 4D Poincare symmetry -- warped
    differently for time and for space, compact with the planes in relative motion, or changing in time.  In every
    static bulk that keeps it (a single warp factor on the plane's coordinates, any number of extra dimensions: RS1,
    ours under H-RS1; RS2; ADD's flat bulk), every causal curve obeys |dx| <= dt in the plane's coordinates: computed
    exactly, and checked on random curves; the CONTROL breaks the symmetry and the same test finds the shortcut.
    So M's corridor, if it beats light, is a place where the bulk is warped unequally for time and space.
  * THE CORRIDOR MUST BE LOCAL, NOT A PROPERTY OF THE WHOLE BULK (C3).  Gravitons -- the bulk carrier RS1 has --
    from GW170817 arrived with light: the speed difference lies between -3e-15 and +7e-16 of c over at least 26 Mpc
    (READ).  A bulk warped unequally everywhere would show there; a corridor confined to a device's neighbourhood
    need not.  On a graviton-borne README to Proxima, a global asymmetry could save at most 7e-16 of the light time,
    9.4e-8 s (H-BOUND-TRANSFERS).
  * THE PORT IS WHERE M'S COST LANDS (C4).  The board's illustrative gravitational port (zeromode.py's 1 m rotor, about 5
    gravitons a second, one bit per graviton) would load the identity core in 5.4e14 s -- 17 million years -- and a
    1 km rotor of the same tip speed and density in 0.53 s.  Under H-COST-IN-README the trip's cost is that port time,
    and it scales with the README: the faithful copy's 3.5e12-fold reduction (faithful.py) is the factor between the
    snapshot's load time and the core's.
  * Boundary (item 82): in RS1 as the board seats it (bulk.py), the bulk keeps 4D Poincare symmetry by construction
    (RS: the tensions are "required in order to obtain a solution that respects four-dimensional Poincare
    invariance", as crossing.py READ it), so there the README crosses at or below c: D13 extends to bulk carriers in
    every such bulk.  The escape classes are the board's own open items: an unequally warped bulk needs an exotic
    bulk fluid to keep Newton's law on our plane (BULK3-O5) and may need NEC violation somewhere (BULK2-O2); a compact
    bulk with moving planes needs our boost B relative to the preferred frame, unmeasured (O7).

    python3 carrier.py              report
    python3 carrier.py --selftest   checks, CONTROLS and CONTRASTS marked, STRUCTURAL printed and not counted
    python3 carrier.py --json       the numbers as JSON

C1 [computed, exact]  Let the bulk metric be ds^2 = e^{2A(y)} eta_{mu nu} dx^mu dx^nu + g_ab(y) dy^a dy^b, with g_ab
   positive definite and A any function of the bulk coordinates alone (static, 4D Poincare-invariant slices).  Along a
   causal curve, e^{2A}(dt^2 - |dx|^2) = g_ab dy^a dy^b + (non-negative) >= 0, so |dx| <= dt at every step: between
   two points of one plane no causal curve through the bulk beats the plane's own light time.  Checked numerically on
   random causal curves in RS1's warp A = -k|y| and in a two-dimensional warp; CONTROL: with time and space warped
   differently, ds^2 = -e^{2A}dt^2 + e^{2B}dx^2 + dy^2 and B < A on part of the path, the same test finds |dx|/dt > 1.
C2 [deduced; the board's]  So a bulk carrier escapes D13 only where the bulk breaks the plane's Poincare symmetry.
   The board holds three such classes: (i) unequal warping (Chung-Freese; pairing.py, cfgravity.py: Newton's law on
   our plane needs a bulk fluid with c_s^2 = -1/2, BULK3-O5; BULK2-O2 asks whether NEC violation is needed somewhere);
   (ii) a compact bulk with planes in relative motion (branelink.py: the saving depends on B, our boost relative to the
   preferred frame, O7; GW170817 bounds the plane's speed on the bulk-graviton branch); (iii) a time-dependent bulk
   (not covered by C1; not modelled here).
C3 [READ]  LIGO-Virgo, Fermi-GBM, INTEGRAL, 1710.05834v2 (alphaXiv): "constrain the difference between the speed of
   gravity and the speed of light to be between -3 x 10^-15 and +7 x 10^-16 times the speed of light" (abstract, p.1;
   eq. 1, p.6, with D = 26 Mpc "the lower bound of the 90% credible interval", and an emission window of 10 s); the
   observed delay "1.74 +/- 0.05 s" (p.1).  Under H-BOUND-TRANSFERS (the bound measured on one line of sight holds for
   gravitons on the Proxima line), a global asymmetry saves at most 7e-16 x 4.24 ly / c.
C4 [computed from the owners]  zeromode.rotor_load_time (imported): load time = I / (graviton rate), at one bit per
   graviton (H-BIT-PER-GRAVITON, zeromode's); I = faithful.py's identity core (imported).  The rotor scales at fixed tip
   speed and density (zeromode's own scaling).

NAMED HYPOTHESES AND PREMISES
  H-STATIC-WARP: C1's bulk is static, with one warp factor on the plane's coordinates.
  H-RS1 (carried): our plane is RS1's negative-tension plane.
  H-BOUND-TRANSFERS: GW170817's bound, measured on one line of sight to NGC 4993, applies to gravitons on the Proxima
    line.
  H-BIT-PER-GRAVITON (zeromode's); the illustrative rotor (zeromode's LAB_ROTOR).
  M's: H-COST-IN-README (item 89), H-ADDRESS-INPUT (item 86), H-INFORMATION-CROSSES (item 86).

OPEN
  1. A corridor geometry that breaks Poincare symmetry locally -- unequal warping confined to a device's neighbourhood
     -- with its energy conditions (with BULK2-O2, BULK3-O5).
  2. A time-dependent bulk (C2 iii).
  3. A port faster than gravitational emission: the bulk scalar of stabilisation (BULK3-O3), or the planes' own fields
     at the corridor's mouth.
  4. Whether one bit per graviton can be reached (H-BIT-PER-GRAVITON) -- at the sending end, and at the receiving end,
     where single gravitons would have to be detected.
  5. In a bulk that keeps the symmetry, the trip takes the port time plus at least the light time (4.24 years to
     Proxima): C1 makes the flight no shorter than light.
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

C = 299792458.0
LY_M = 9.4607304725808e15            # one light year in m (IAU Julian year x c; standard)
MPC_M = 3.0856775814913673e22        # one megaparsec in m (standard)
PROXIMA_LY = 4.24                    # the board's span is imported below where needed; 4.24 ly is illustrative here
K_RS = 1.0                           # C1's warp scale (units of 1/length; the check is scale-free)


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


# ---------------------------------------------------------------------------------------------------- C1
def max_speed_on_plane(metric, trials=4000, steps=60, seed=7):
    """Largest |dx|/dt over random causal curves.  metric(y) -> (gtt, gxx, gyy) for ds^2 = -gtt dt^2 + gxx dx^2 +
    gyy dy^2 (gtt, gxx, gyy > 0); each step picks dy and a direction, and takes the fastest causal dx for that dy:
    gxx dx^2 + gyy dy^2 <= gtt dt^2."""
    rng = random.Random(seed)
    worst = 0.0
    for _ in range(trials):
        y, t, x = 0.0, 0.0, 0.0
        for _ in range(steps):
            dt = 1e-2
            gtt, gxx, gyy = metric(y)
            room = gtt * dt * dt
            dy = rng.uniform(-1, 1) * math.sqrt(room / gyy)
            dx = math.sqrt(max(room - gyy * dy * dy, 0.0) / gxx)        # the fastest allowed along x
            t, x, y = t + dt, x + dx, y + dy
        worst = max(worst, x / t)
    return worst


def rs1(y):
    a = math.exp(-2 * K_RS * abs(y))
    return a, a, 1.0


def warp2(y):                        # a second extra dimension folded into y's metric factor (two-dimensional warp)
    a = math.exp(-2 * K_RS * abs(y)) * (1 + 0.5 * math.sin(3 * y) ** 2)
    return a, a, 1.0 + 0.3 * math.cos(y) ** 2


def unequal(y):                      # CONTROL: time and space warped differently, B < A where y < 0
    A = -K_RS * abs(y)
    B = A - 0.5 * (1 if y < 0 else 0)
    return math.exp(2 * A), math.exp(2 * B), 1.0


def c1_symbolic():
    """e^{2A}(dt^2 - dx^2) - gyy dy^2 = 0 on a null curve, solved for dx/dt: returns the bound as a sympy expression,
    which is <= 1 for any real A and gyy dy^2 >= 0."""
    import sympy as sp
    A, dt, dy, g = sp.symbols("A dt dy g", real=True)
    dx = sp.symbols("dx", positive=True)
    sol = sp.solve(sp.Eq(sp.exp(2 * A) * (dt ** 2 - dx ** 2) - g * dy ** 2, 0), dx)
    return [sp.simplify((s / dt) ** 2) for s in sol]


# ---------------------------------------------------------------------------------------------------- C3, C4
def compute():
    zm = _load("zeromode", os.path.join(BULK, "zeromode.py"), "bulk_zeromode_carrier")
    fa = _load("faithful", os.path.join(HERE, "faithful.py"), "copy_faithful_carrier")
    core = fa.identity_core()["total_bits"]
    snapshot = fa._measure()["species"]
    gw_light_s = GW_D_MPC * MPC_M / C
    prox_light_s = PROXIMA_LY * LY_M / C
    ports = {a: zm.rotor_load_time(a, core) for a in (1.0, 10.0, 100.0, 1000.0)}
    return {"rs1_max": max_speed_on_plane(rs1), "warp2_max": max_speed_on_plane(warp2),
            "unequal_max": max_speed_on_plane(unequal), "symbolic": [str(s) for s in c1_symbolic()],
            "gw_light_s": gw_light_s, "gw_max_saving_s": GW_DV_MAX * gw_light_s,
            "proxima_light_s": prox_light_s, "proxima_max_saving_s": GW_DV_MAX * prox_light_s,
            "core_bits": core, "snapshot_bits": snapshot, "port_s_by_arm_m": ports,
            "port_snapshot_1m_s": zm.rotor_load_time(1.0, snapshot)}


def report():
    d = compute()
    print("carrier.py -- a carrier through the bulk (M item 88, link 2; not verified; not seated)\n")
    print("C1 largest |dx|/dt on random causal curves: RS1 %.6f, two-dimensional warp %.6f; CONTROL (unequal warp) %.4f" % (
        d["rs1_max"], d["warp2_max"], d["unequal_max"]))
    print("   null curve, (dx/dt)^2 = %s" % d["symbolic"])
    print("C3 GW170817: light time over 26 Mpc %.3e s; at +7e-16 a graviton saves at most %.2f s; on the Proxima line "
          "at most %.2e s" % (d["gw_light_s"], d["gw_max_saving_s"], d["proxima_max_saving_s"]))
    print("C4 port time for the identity core (%.2e bits), by rotor arm: %s" % (
        d["core_bits"], ", ".join("%g m: %.3g s" % kv for kv in d["port_s_by_arm_m"].items())))
    print("   the snapshot count (%.2e bits) through the 1 m rotor: %.3g s" % (d["snapshot_bits"],
                                                                            d["port_snapshot_1m_s"]))


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
    chk("C1: in RS1's warp no random causal curve beats the plane's light speed (largest |dx|/dt = %.6f)" % d["rs1_max"],
        d["rs1_max"] <= 1 + 1e-12)
    chk("C1: nor in a two-dimensional warp (largest %.6f)" % d["warp2_max"], d["warp2_max"] <= 1 + 1e-12)
    chk("C1: with time and space warped differently the same test finds a shortcut (largest |dx|/dt = %.4f > 1)" %
        d["unequal_max"], d["unequal_max"] > 1.1, ctl=True)
    chk("C1: on a null curve (dx/dt)^2 = 1 - g dy^2 e^{-2A}/dt^2, never above 1 (sympy: %s)" % d["symbolic"],
        any("exp(-2*A)" in s for s in d["symbolic"]))
    chk("C3: GW170817's +7e-16 over 26 Mpc (light time %.3e s) allows %.2f s, consistent with the observed %.2f s "
        "delay; on the Proxima line it is %.2e s" % (d["gw_light_s"], d["gw_max_saving_s"], GW_DELAY_S,
                                                       d["proxima_max_saving_s"]),
        abs(d["gw_max_saving_s"] - GW_DELAY_S) < 1.0 and d["proxima_max_saving_s"] < 1e-6)
    p = d["port_s_by_arm_m"]
    chk("C4: the identity core through the board's 1 m gravitational port takes %.3g s (%.1f million years); a 1 km "
        "rotor of the same tip speed and density, %.3g s" % (p[1.0], p[1.0] / 3.156e13, p[1000.0]),
        p[1.0] > 1e14 and p[1000.0] < p[1.0] * 1e-14)
    chk("C4: the port time scales with the README: snapshot / core = %.3e, equal to the bit ratio %.3e" % (
        d["port_snapshot_1m_s"] / p[1.0], d["snapshot_bits"] / d["core_bits"]),
        abs(d["port_snapshot_1m_s"] / p[1.0] / (d["snapshot_bits"] / d["core_bits"]) - 1) < 1e-9, contrast=True)
    structural.append("C2: the escape classes are the board's open items (BULK3-O5, BULK2-O2, O7); none is computed here")
    structural.append("C3 uses D = 26 Mpc, LIGO's conservative lower bound; the board's own Proxima span is in nopath.py "
                      "(4.0175e16 m); 4.24 ly is illustrative here")
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
