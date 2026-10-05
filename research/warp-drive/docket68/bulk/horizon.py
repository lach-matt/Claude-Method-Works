#!/usr/bin/env python3
"""
horizon.py -- the corridor as horizons that observe (M-RULINGS items 70-71): the corridor TAKES the information as a
condition of its opening (H-CORRIDOR-TAKES), we are observed rather than loading (H-OBSERVED-NOT-LOADED), the exit is the
same observation mechanism -- position 2 observes and its horizon draws in passively (H-EXIT-BY-OBSERVATION) -- and
the mechanism is expansion (H-EXPANSION).  READ at source, then modelled by deduction (M-DEDUCE).

Not seated; not yet verified.  M's words are carried as hypotheses, never as results.  O9 stays OPEN.

    python3 horizon.py              report
    python3 horizon.py --selftest   checks, with CONTROLS
    python3 horizon.py --json       the numbers as JSON

SOURCES READ (2026-10-05; route: alphaXiv answer_pdf_queries on open arXiv copies, printed pages)
  Bousso hep-th/0203101v2: 'the area of any surface limits the information content of adjacent spacetime regions, at
    1.4 x 10^69 bits per square meter' (abstract); 'When a thermodynamic system disappears behind a black hole's event
    horizon, its entropy is lost to an outside observer' (p.6); S_BH = A/4 (eq. 2.2); A_AH = 3/(2 rho) for the apparent
    horizon of a flat FRW universe (eq. 7.11, Planck units); a_0^2 = (D-1)(D-2)/(2 Lambda) and S_dS = pi a_0^2 = 3 pi/Lambda
    (eqs. 9.8, 9.10); 'the location of event horizons in de Sitter space depends on a choice of observer' (p.44);
    'Classically, objects that fall across the event horizon cannot be recovered' (p.44); in an expanding (dS+-)
    universe 'All matter will have passed through the future event horizon' (p.44).
  Jacobson gr-qc/9504004v2 (also READ by A4): a causal horizon 'can be simply the boundary of the past of any set O
    (for "observer")' (p.2); heat is 'energy that flows across a causal horizon ... its particular form or nature is
    unobservable from outside the horizon' (p.2); horizons 'hide information' (p.2).
  Crispino, Higuchi & Matsas 0710.5373v1: 'the particle content of a field theory is observer dependent' (abstract);
    observers 'must agree on the value of scalar observables ... although they can differ in how they describe the
    phenomenon' (p.22).
  Hayden & Preskill 0708.4025v2: past the half-way point, 'additional quantum information deposited in the black hole is
    revealed in the Hawking radiation very rapidly' (abstract); the receiver's prior entanglement is required (p.5); the
    return is through the same horizon, after a Schwarzschild time O(r_S log(r_S/l_P)) (p.2), and decoding may be hard
    (p.12).
  Parikh & Wilczek hep-th/9907001v3: emission is tunnelling across a contracting horizon, rate Gamma ~ e^{Delta S_BH}
    (eq. 10); information content only 'suggests the possibility' (p.9).
  Alcubierre gr-qc/0009013v1: 'a purely local expansion of spacetime behind the spaceship and an opposite contraction in
    front of it' (abstract); 'the spaceship will be pushed away from the Earth and pulled towards a distant star by
    spacetime itself' (p.3); comoving observers 'always move inside their local light-cones. The enormous speed of
    separation comes from the expansion of spacetime itself' (p.2); theta = -Tr K, theta = v_s ((x - x_s)/r_s) df/dr_s
    (eqs. 11-12); the Eulerian energy density is 'everywhere negative' (eq. 19, p.8).
  Gibbons & Hawking 1977 (cosmological event horizons): NOT FOUND as an open copy; used only through Bousso p.44.

DEDUCTIONS (each from the premises named)
  E1 A HORIZON TAKES WITHOUT BEING FED.  [Bousso p.6, Jacobson p.2, HP p.5]  Whatever crosses a horizon is taken; no
     loading act is involved -- H-CORRIDOR-TAKES has a READ physical form.  Capacity is no obstacle: at A/(4 l_P^2) nats,
     measure.py's counts need a horizon area of ~1e-41 m^2 (computed; check 1 reproduces Bousso's 1.4e69 bits/m^2).
  E2 OBSERVATION DEFINES A HORIZON.  [Jacobson p.2, Bousso p.44, CHM abstract]  A horizon is the boundary of the past of
     an observer set; its location depends on the observer -- each position has its own.  H-OBSERVED-NOT-LOADED has a
     READ counterpart: what an observer can see is what fixes the horizon that takes.
  E3 THE SIGN.  [Bousso p.6 and p.44, Jacobson p.2]  What crosses an observer's horizon leaves THAT observer's view.  So
     position 2 cannot receive through its own horizon in the READ sense; the consistent reading of
     H-EXIT-BY-OBSERVATION is two horizons: position 1's horizon takes the information out of position 1's view, and it
     arrives within position 2's view -- which needs space to be drawn TOWARD position 2.  Hayden-Preskill's return
     goes back out through the same horizon, with prior entanglement and decoding; no READ source has a second horizon
     receiving what a first took (a limit of the sources, not a refutation of M).
  E4 EXPANSION TAKES, CONTRACTION DRAWS IN -- ALCUBIERRE'S PATTERN.  [Alcubierre abstract, pp.2-3, eqs. 11-12]
     Expansion where the information leaves and contraction where it arrives is exactly the warp metric's pattern
     (checked symbolically, check 3): 'pushed away ... and pulled towards a distant star by spacetime itself', with no
     local motion faster than light -- a READ counterpart of H-EXPANSION and of H-NO-SPEED's no-travel.  Its price is an
     energy density 'everywhere negative' (eq. 19); warpdrive.py's Pfenning-Ford energy for an illustrative bubble is
     printed.  -- M's picture meets the board's first subject from the other side.
  E5 EXPANSION ALONE TAKES BUT DOES NOT DELIVER.  [Bousso eqs. 7.11, 9.8-9.10, p.44]  A positive, NEC-saturating vacuum
     energy whose horizon sits between the two positions (radius D) needs u = 3 c^4 / (8 pi G D^2) -- finite and
     POSITIVE (computed for the Proxima span, against today's dark-energy density from cosmo.py).  But comoving
     positions keep their comoving separation: expansion carries everything apart and delivers nothing to position 2,
     and a pattern starting 1 m from position 1 crosses its horizon only after ln(D / 1 m) light-crossing times
     (H-COMOVING-START).  Drawing in is the contraction half, which in E4 is what costs negative energy.
  E6 WHAT EVERY OBSERVER AGREES ON.  [CHM p.22]  The description of a horizon is observer-dependent; scalar observables
     are not.  Two observing horizons can describe one crossing differently, but whether the information arrives is one
     fact for both -- the place H-TWO-PERSPECTIVE-TENSION and H-POSITION-RELATIVE-SPEED meet E3.

NAMED HYPOTHESES
  H-DS-LOCAL (a local de Sitter region of horizon radius D), H-COMOVING-START (the pattern starts 1 m from position 1,
  comoving), H-ALCUBIERRE-ILLUSTRATIVE (bubble R = 100 m at v = c with Pfenning-Ford's wall), with measure.py's counting
  hypotheses; and M's H-CORRIDOR-TAKES, H-OBSERVED-NOT-LOADED, H-EXIT-BY-OBSERVATION, H-EXPANSION, H-NO-SPEED,
  H-TWO-PERSPECTIVE-TENSION, H-POSITION-RELATIVE-SPEED.
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
        bulk = _by_path("bulk_bulk", os.path.join(HERE, "bulk.py"))
        crossing = _by_path("bulk_crossing", os.path.join(HERE, "crossing.py"))
        warpdrive = _by_path("wd_warpdrive", os.path.join(WD, "warpdrive.py"))
finally:
    sys.path[:] = _saved

cosmo = bulk.cosmo
C = cosmo.c
G = cosmo._G
HBAR = cosmo._HBAR
BOUSSO_BITS_PER_M2 = 1.4e69          # READ, Bousso abstract
ALC_R_M = 100.0                       # H-ALCUBIERRE-ILLUSTRATIVE
D0_M = 1.0                            # H-COMOVING-START


def bits_per_m2():
    """1 / (4 l_P^2 ln 2), l_P^2 = hbar G / c^3 -- Bousso's S = A/4 in bits."""
    return 1.0 / (4 * HBAR * G / C ** 3 * math.log(2))


def ds_radius_sq(D, lam=1.0):
    """Bousso eq. 9.8: a_0^2 = (D-1)(D-2)/(2 Lambda)."""
    return (D - 1) * (D - 2) / (2 * lam)


def energy_density_for_horizon(R):
    """Bousso eq. 7.11, A_AH = 3/(2 rho) (G = c = 1), with A = 4 pi R^2 and units restored: u = 3 c^4 / (8 pi G R^2)."""
    return 3 * C ** 4 / (2 * G * 4 * math.pi * R ** 2)


def alcubierre_theta_signs():
    """theta = -Tr K with K_ij = (d_i beta_j + d_j beta_i)/2, beta_x = -v_s f(r_s) (Alcubierre eqs. 3, 10-11), computed
    symbolically and evaluated just behind and just ahead of the bubble centre, on the wall."""
    import sympy as sp
    x, y, z, xs, vs, sig, R = sp.symbols("x y z x_s v_s sigma R", real=True)
    rs = sp.sqrt((x - xs) ** 2 + y ** 2 + z ** 2)
    f = (sp.tanh(sig * (rs + R)) - sp.tanh(sig * (rs - R))) / (2 * sp.tanh(sig * R))
    beta = [-vs * f, 0, 0]
    trK = sp.diff(beta[0], x)
    theta = -trK
    eq12 = vs * (x - xs) / rs * sp.diff(f.subs(rs, sp.Symbol("r", positive=True)), sp.Symbol("r", positive=True)).subs(
        sp.Symbol("r", positive=True), rs)
    vals = {"sigma": 8, "R": 1, "v_s": 1, "x_s": 0}
    sub = {sig: 8, R: 1, vs: 1, xs: 0, y: 0, z: 0}
    behind = float(theta.subs({**sub, x: -1.0}))
    ahead = float(theta.subs({**sub, x: 1.0}))
    flipped_ahead = float(theta.subs({**sub, vs: -1, x: 1.0}))
    agree = abs(float((theta - eq12).subs({**sub, x: 0.7}))) + abs(float((theta - eq12).subs({**sub, x: -1.3})))
    return {"behind": behind, "ahead": ahead, "flipped_ahead": flipped_ahead, "eq12_residual": agree, "params": vals}


def compute():
    I = crossing.compute()["bits"]
    I_lo, I_hi = min(I.values()), max(I.values())
    bpm2 = bits_per_m2()
    A_lo, A_hi = I_lo / bpm2, I_hi / bpm2
    D = bulk.L_PROXIMA
    u_D = energy_density_for_horizon(D)
    H0 = cosmo.H0()
    omega_l = 1.0 - cosmo.OMEGA_M                                   # flat, radiation neglected
    u_crit0 = energy_density_for_horizon(C / H0)
    u_lambda0 = omega_l * u_crit0
    th = alcubierre_theta_signs()
    with contextlib.redirect_stdout(io.StringIO()):
        wall = warpdrive.qi_wall(1.0)
        e_geom, e_j, e_kg = warpdrive.alcubierre_energy(ALC_R_M, wall, 1.0)
    return {"bits_per_m2": bpm2, "bousso_bits_per_m2": BOUSSO_BITS_PER_M2, "I_lo": I_lo, "I_hi": I_hi,
            "area_lo_m2": A_lo, "area_hi_m2": A_hi, "radius_hi_m": math.sqrt(A_hi / (4 * math.pi)),
            "D_m": D, "u_for_horizon_D_J_m3": u_D, "u_lambda_today_J_m3": u_lambda0, "u_ratio": u_D / u_lambda0,
            "H_for_D_per_s": C / D, "crossing_factor_light_times": math.log(D / D0_M),
            "crossing_time_yr": math.log(D / D0_M) * D / C / cosmo.YR,
            "theta": th, "alc_wall_m": wall, "alc_energy_J": e_j, "alc_mass_kg": e_kg}


def report():
    d = compute()
    print("horizon.py -- the corridor as horizons that observe (M items 70-71), by deduction (not verified; not seated)\n")
    print("E1 a horizon takes without being fed; S = A/4 gives %.3e bits/m^2 (Bousso: 1.4e69); %.1e-%.1e bits need "
          "%.1e-%.1e m^2 (radius %.1e m)" % (d["bits_per_m2"], d["I_lo"], d["I_hi"], d["area_lo_m2"], d["area_hi_m2"],
                                              d["radius_hi_m"]))
    print("E2 observation defines a horizon (Jacobson, Bousso, CHM)")
    print("E3 what crosses an observer's horizon leaves that observer's view: position 1 takes, position 2 must be drawn "
          "toward; no READ source has a second horizon receiving")
    t = d["theta"]
    print("E4 Alcubierre's pattern: theta behind %+.3f (expansion), ahead %+.3f (contraction); price: Pfenning-Ford "
          "energy for R = 100 m at v = c with the QI wall (%.1e m): %.2e J (%.2e kg)" % (
              t["behind"], t["ahead"], d["alc_wall_m"], d["alc_energy_J"], d["alc_mass_kg"]))
    print("E5 a positive vacuum energy with its horizon at the Proxima span: u = %.2e J/m^3 (%.1e x today's dark "
          "energy, %.2e J/m^3); H = %.2e /s; a pattern from 1 m crosses after %.1f light-crossing times (%.0f yr) -- "
          "and expansion delivers nothing to position 2" % (d["u_for_horizon_D_J_m3"], d["u_ratio"],
                                                             d["u_lambda_today_J_m3"], d["H_for_D_per_s"],
                                                             d["crossing_factor_light_times"], d["crossing_time_yr"]))
    print("E6 scalar observables are shared: whether it arrives is one fact for both positions")


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
    chk("E1: S = A/(4 l_P^2) from the board's hbar, G, c gives %.3e bits/m^2, Bousso's READ 1.4e69 to 2 %%" %
        d["bits_per_m2"], abs(d["bits_per_m2"] / BOUSSO_BITS_PER_M2 - 1) < 0.02)
    chk("with h in place of hbar in l_P^2 it is %.2e, off Bousso's figure" % (d["bits_per_m2"] / (2 * math.pi)),
        abs(d["bits_per_m2"] / (2 * math.pi) / BOUSSO_BITS_PER_M2 - 1) > 0.5, ctl=True)
    a4 = ds_radius_sq(4)
    chk("Bousso eqs. 9.8 and 9.10 agree with S = A/4 in four dimensions: pi a_0^2 = %.6f = 3 pi / Lambda (Lambda = 1)" %
        (math.pi * a4), abs(math.pi * a4 - 3 * math.pi) < 1e-12 and abs(4 * math.pi * a4 / 4 - math.pi * a4) < 1e-12)
    chk("in five dimensions eq. 9.8 gives a_0^2 = %.1f, not 3 -- the dimension enters" % ds_radius_sq(5),
        abs(ds_radius_sq(5) - 3) > 1, ctl=True)
    t = d["theta"]
    chk("E4: theta = -Tr K from Alcubierre's shift is positive behind (%+.3f) and negative ahead (%+.3f) -- his 'expanding "
        "behind, contracting in front' -- and equals his eq. 12 (residual %.1e)" % (t["behind"], t["ahead"],
                                                                                    t["eq12_residual"]),
        t["behind"] > 0 and t["ahead"] < 0 and t["eq12_residual"] < 1e-12)
    chk("reversing v_s reverses it (ahead becomes %+.3f)" % t["flipped_ahead"], t["flipped_ahead"] > 0, ctl=True)
    structural.append("E5's energy density is Bousso eq. 7.11 with units restored, u = 3 c^4/(8 pi G R^2) = 3 c^2 H^2/"
                      "(8 pi G) at R = c/H -- the same identity, not a second measurement")
    structural.append("E3 is a limit of the READ sources (no second horizon receives), not a refutation of "
                      "H-EXIT-BY-OBSERVATION")
    structural.append("E4 is a correspondence of PATTERN (expansion where it leaves, contraction where it arrives); "
                      "Alcubierre's price (negative energy, eq. 19) comes with it")
    for s_ in structural:
        print("  STRUCTURAL: " + s_)
    print("horizon.py: %d/%d checks pass, %d of them controls; %d STRUCTURAL printed, not counted" % (
        n_pass, n_pass + n_fail, n_ctl, len(structural)))
    return n_fail == 0


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    elif "--json" in sys.argv:
        print(json.dumps(compute(), indent=1, default=str))
    else:
        report()
