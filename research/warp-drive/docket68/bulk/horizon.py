#!/usr/bin/env python3
"""
horizon.py -- the corridor as horizons that observe (M-RULINGS items 70-73): the corridor TAKES the information as a
condition of its opening (H-CORRIDOR-TAKES), we are observed rather than loading (H-OBSERVED-NOT-LOADED), the exit is the
same observation mechanism (H-EXIT-BY-OBSERVATION), the mechanism is expansion (H-EXPANSION), and position 2 does not
view what it draws in because it INCORPORATES it -- an object cannot view itself as a whole without the help of mirrors
(H-INCORPORATION, item 72; folded in on item 73).  READ at source, then modelled by deduction (M-DEDUCE).

Seated in ledger.py section 8l (M: "Seat all three, then the bulk", item 79); first written "Not seated".  Verified once (2026-10-05), findings applied (HISTORY below).  M's words are carried as hypotheses, never
as results.  O9 stays OPEN.

    python3 horizon.py              report
    python3 horizon.py --selftest   checks, with CONTROLS
    python3 horizon.py --json       the numbers as JSON

SOURCES READ (2026-10-05; route: alphaXiv answer_pdf_queries on open arXiv copies, printed pages)
  Bousso hep-th/0203101v2: 'the area of any surface limits the information content of adjacent spacetime regions, at
    1.4 x 10^69 bits per square meter' (abstract); 'When a thermodynamic system disappears behind a black hole's event
    horizon, its entropy is lost to an outside observer' (p.6); the area theorem dA >= 0 (eq. 2.1), S_BH = A/4 (eq. 2.2)
    and the generalized second law dS_total >= 0 (eq. 2.3); A_AH = 3/(2 rho) for the apparent horizon of an FRW universe
    (eq. 7.11, Planck units, any spatial curvature); a_0^2 = (D-1)(D-2)/(2 Lambda), S_dS = pi a_0^2 = 3 pi/Lambda (eqs. 9.8,
    9.10); 'the location of event horizons in de Sitter space depends on a choice of observer' (p.44); 'Classically,
    objects that fall across the event horizon cannot be recovered' (p.44); in dS+- spacetimes, relative to the
    south-pole observer, 'All matter will have passed through the future event horizon' (p.44).
  Jacobson gr-qc/9504004v2 (also READ by A4): a causal horizon 'can be simply the boundary of the past of any set O
    (for "observer")' (p.2); heat is 'energy that flows across a causal horizon ... unobservable from outside the
    horizon' (p.2); 'the system into which the heat is flowing' (p.3, verifier-READ).
  Crispino, Higuchi & Matsas 0710.5373v1: 'the particle content of a field theory is observer dependent' (abstract);
    observers 'must agree on the value of scalar observables, such as the proper excitation rate of a given detector'
    (p.22), in flat spacetime.
  Hayden & Preskill 0708.4025v2 ('Black holes as mirrors'): past the half-way point, deposited information 'is revealed
    in the Hawking radiation very rapidly' (abstract) -- the RAPID return needs the receiver's pre-existing entanglement
    with the hole (p.5, 'it is a quantum information mirror'); without it, information 'remains concealed until the
    half-way point' (abstract); k qubits are re-emitted in Schwarzschild time 'O(kr_S) or O(r_S log(r_S/l_P)),
    whichever is larger' (p.2), on speculative dynamical assumptions; complementarity covers observers 'whether
    outside or inside the black hole' (p.2, verifier-READ); decoding may be hard (p.12).
  Parikh & Wilczek hep-th/9907001v3: emission by tunnelling across a contracting horizon, Gamma ~ e^{Delta S_BH} (eq. 10);
    the Planck flux at inverse temperature 8 pi M (eq. 11, Planck units); information only 'suggests the possibility'
    (p.9).
  Alcubierre gr-qc/0009013v1: 'a purely local expansion of spacetime behind the spaceship and an opposite contraction in
    front of it' (abstract); 'pushed away from the Earth and pulled towards a distant star by spacetime itself' (p.3);
    comoving observers in inflation separate at a 'relative speed' -- 'rate of change of proper spatial distance over
    proper time' -- 'much larger than the speed of light', yet 'always move inside their local light-cones' (p.2);
    theta = -alpha Tr K (eq. 11), theta = v_s ((x - x_s)/r_s) df/dr_s (eq. 12); Eulerian energy density 'everywhere
    negative' (eq. 19).
  Natario gr-qc/0110086v3: the contraction/expansion 'is but a marginal consequence of the choice made by Alcubierre'
    (abstract) and 'is not necessary at all' (p.1); 'Nonflat warp drive spacetimes violate either the weak or the strong
    energy condition' (Thm 1.7, p.3); rho = (theta^2 - K_ij K^ij)/16 pi (p.3); for Alcubierre's choice
    rho = -(1/32 pi) v_s^2 [f'(r_s)]^2 (y^2 + z^2)/r_s^2 (p.4).
  Pfenning & Ford gr-qc/9702026 (via warpdrive.py, and verifier-READ): eq. 22 bounds the wall thickness from ABOVE; R =
    100 m is their own example (p.10); eq. 28 the energy, a floor on |E|.
  Gibbons & Hawking 1977: NOT FOUND as an open copy; used only through Bousso p.44.

DEDUCTIONS (each from the premises named)
  E1 A HORIZON TAKES WITHOUT BEING FED.  [Bousso p.6, Jacobson p.2]  It takes ALL that crosses, not a selection; what
     brings the information to it (gravity, expansion, propagation) is a separate question.  H-CORRIDOR-TAKES has a READ
     physical form.  Capacity is no obstacle: at A/(4 l_P^2 ln 2) bits (check 1), measure.py's counts need ~1e-41 m^2.
  E2 OBSERVATION DEFINES A HORIZON.  [Jacobson p.2, Bousso p.44, CHM abstract]  A horizon is the boundary of the past of an
     observer set, and its location depends on the observer: each position has its own.  H-OBSERVED-NOT-LOADED has a
     READ counterpart.
  E3 ONE HORIZON, TWO SIDES: POSITION 2 INCORPORATES.  [Bousso p.6 ('an outside observer'), eqs. 2.1-2.3; Jacobson
     pp.2-3; HP p.2; H-INCORPORATION]  What crosses a horizon leaves the view of observers on the side it LEAVES; nothing
     enters an observer's own boundary-of-past.  But it enters the region the horizon ENCLOSES, and an observer there
     receives it.  One horizon serves both positions: position 1's horizon is position 2's enclosure.  The horizon grows
     by what it takes (dA >= 0; S = A/4; the generalized second law): the information is incorporated, not destroyed --
     M's 'it is incorporating that information into itself'.  Computed for an illustrative 1 m enclosure
     (H-ENCLOSURE-1M): the area added, and the least energy to incorporate a body's bits at its temperature (from
     Parikh-Wilczek eq. 11) -- half of Bekenstein's floor.  To view itself as a whole the enclosure needs a MIRROR: in
     Hayden-Preskill, a rapid return needs pre-existing entanglement, and k qubits return in O(k r_S) or
     O(r_S log(r_S/l_P)) -- for a body's bits, the O(k r_S) term (printed).  Costs: capture is one-way ('cannot be
     recovered'), position 2 cannot signal back out, and the information still reaches the horizon at <= c.
  E4 EXPANSION/CONTRACTION IS ONE WARP GEOMETRY, AND IT IS NOT WHERE THE PRICE SITS.  [Alcubierre, Natario, Pfenning-Ford]
     Expansion where the information leaves and contraction where it arrives is exactly the pattern of Alcubierre's
     metric (signs computed, check 3).  Natario shows the pattern is not necessary for warp transport -- but the
     negative-energy price is (Thm 1.7).  And the price is not in the contraction: rho = (theta^2 - K_ij K^ij)/16 pi
     (check 4 reproduces the printed form), so expansion and contraction ADD positive energy; Alcubierre's rho is the
     same behind and ahead, zero on the axis where |theta| is largest, and largest on the equator where theta = 0
     (computed).  The negative energy belongs to the transport, not to drawing in.  The board's Pfenning-Ford figure for
     their own 100 m example at v = c with the THICKEST wall the quantum inequality allows is a floor: |E| >= 8.5e79 J.
  E5 EXPANSION ALONE TAKES BUT DOES NOT DELIVER A COMOVING BODY.  [Bousso eqs. 7.11, 9.8-9.10, p.44; Alcubierre p.2]
     A positive vacuum energy whose horizon around position 1 lies at position 2's distance D needs
     u = 3 c^4 / (8 pi G D^2); the region of radius D then holds c^4 D/(2G) -- the mass whose Schwarzschild radius is D.
     Comoving bodies keep their comoving separation, so expansion delivers no comoving body to position 2 (and with the
     horizon exactly at D, light from position 1 never reaches it); a pattern starting 1 m from position 1 crosses its
     horizon after ln(D/1 m) light-crossing times.  Alcubierre's p.2 separation speed between comoving observers is a
     speed defined BETWEEN two positions, not a local one -- a READ counterpart of H-POSITION-RELATIVE-SPEED and of
     H-EXPANSION.
  E6 BUT A SIGNAL CAN BE TAKEN FROM 1 AND OBSERVED AT 2.  [de Sitter light propagation, DEDUCED; Bousso p.44]  With the
     horizon radius c/H between D and 2D, light from position 1 reaches position 2 AFTER position 2 has passed beyond
     position 1's future event horizon, iff the separation at emission exceeds c/(2H) (check 5): position 1's horizon
     takes it out of 1's view and position 2 observes it -- with positive energy only (u between the two printed
     values).  It travels at c and arrives later than D/c: no speed gain.
  E7 WHAT A DETECTOR AT POSITION 2 REGISTERS.  [CHM p.22, DEDUCED]  Descriptions of a horizon are observer-dependent;
     whether a given detector at position 2 registers the information is a local event, the same for every observer.
     Where the information IS can differ between inside and outside under complementarity (HP p.2) -- a hypothesis
     there.

NAMED HYPOTHESES
  H-ENCLOSURE-1M, H-HP-ORDER (HP's O( ) estimates taken at unit coefficient), H-DS-LOCAL, H-COMOVING-START, with
  measure.py's counting hypotheses; and M's H-CORRIDOR-TAKES, H-OBSERVED-NOT-LOADED, H-EXIT-BY-OBSERVATION,
  H-EXPANSION, H-INCORPORATION, H-NO-SPEED, H-TWO-PERSPECTIVE-TENSION, H-POSITION-RELATIVE-SPEED.

HISTORY (verifier, 2026-10-05; first-written claims kept)
  * E3 first read 'position 2 cannot receive through its own horizon in the READ sense ... no READ source has a second
    horizon receiving what a first took' -- one horizon has two sides; the enclosed side receives (and M's
    H-INCORPORATION, item 72, is that side).
  * E4 first said 'Drawing in is the contraction half, which in E4 is what costs negative energy' and called the
    pattern 'exactly the warp metric's pattern' -- the energy density is even behind/ahead and expansion enters with a
    positive sign; Natario shows the pattern is not necessary.  The md said 'the thinnest wall quantum physics allows':
    Pfenning-Ford's bound is on the THICKEST wall, so the figure is a floor.
  * E5 first said the horizon sits 'between the two positions' and that the energy is merely 'finite and POSITIVE' --
    the horizon of radius D lies at position 2, and the region holds c^4 D/(2G).
  * E1 first said a horizon 'takes the information it requires' and cited HP p.5 -- it takes all that crosses; HP p.5
    is about prior entanglement.
  * E6 (the de Sitter signal) was missed; E7 (first E6) stretched CHM p.22 to 'whether the information arrives'.
  * checks 3-4 were identities (eq. 9.8 restated; x = x); the v_s-reversal control could not fail; the eq. 12 residual is
    the chain rule (now STRUCTURAL).
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
ENCLOSURE_R_M = 1.0                   # H-ENCLOSURE-1M: an illustrative enclosure of position 2
MSUN = 1.98892e30


def bits_per_m2():
    """1 / (4 l_P^2 ln 2), l_P^2 = hbar G / c^3 -- Bousso's S = A/4 (nats) in bits."""
    return 1.0 / (4 * HBAR * G / C ** 3 * math.log(2))


def ds_radius_sq(D, lam=1.0):
    """Bousso eq. 9.8: a_0^2 = (D-1)(D-2)/(2 Lambda)."""
    return (D - 1) * (D - 2) / (2 * lam)


def apparent_horizon_area(rho):
    """Bousso eq. 7.11 (Planck units): A_AH = 3 / (2 rho)."""
    return 3.0 / (2 * rho)


def energy_density_for_horizon(R):
    """Bousso eq. 7.11 with A = 4 pi R^2, units restored: u = 3 c^4 / (8 pi G R^2)."""
    return 3 * C ** 4 / (2 * G * 4 * math.pi * R ** 2)


def warp_fields():
    """Alcubierre's shift beta_x = -v_s f(r_s): theta = -Tr K, K_ij = (d_i beta_j + d_j beta_i)/2, and Natario's
    rho = (theta^2 - K_ij K^ij)/16 pi, against Natario's printed form for Alcubierre's choice (p.4)."""
    import sympy as sp
    x, y, z, xs, vs, sig, R = sp.symbols("x y z x_s v_s sigma R", real=True)
    rs = sp.sqrt((x - xs) ** 2 + y ** 2 + z ** 2)
    f = (sp.tanh(sig * (rs + R)) - sp.tanh(sig * (rs - R))) / (2 * sp.tanh(sig * R))
    X = [x, y, z]
    beta = [-vs * f, 0, 0]
    K = [[(sp.diff(beta[j], X[i]) + sp.diff(beta[i], X[j])) / 2 for j in range(3)] for i in range(3)]
    trK = sum(K[i][i] for i in range(3))
    theta = -trK
    KK = sum(K[i][j] ** 2 for i in range(3) for j in range(3))
    rho = (theta ** 2 - KK) / (16 * sp.pi)
    rho_no_theta = -KK / (16 * sp.pi)
    r = sp.Symbol("r", positive=True)
    fp = sp.diff(f.subs(rs, r), r).subs(r, rs)
    printed = -vs ** 2 * fp ** 2 * (y ** 2 + z ** 2) / (32 * sp.pi * rs ** 2)
    eq12 = vs * (x - xs) / rs * fp
    sub = {sig: 8, R: 1, vs: 1, xs: 0, z: 0}
    ev = lambda e, xx, yy: float(e.subs({**sub, x: xx, y: yy}))
    pts = [(-1.0, 0.3), (1.0, 0.3), (0.7, 0.5), (-1.3, 0.2)]
    return {"theta_behind": ev(theta, -1.0, 0.0), "theta_ahead": ev(theta, 1.0, 0.0),
            "eq12_residual": max(abs(ev(theta - eq12, a, b)) for a, b in pts),
            "rho_vs_printed": max(abs(ev(rho - printed, a, b)) for a, b in pts),
            "rho_no_theta_vs_printed": max(abs(ev(rho_no_theta - printed, a, b)) for a, b in pts),
            "rho_behind": ev(rho, -1.0, 0.3), "rho_ahead": ev(rho, 1.0, 0.3),
            "rho_axis": ev(rho, 1.0, 0.0), "rho_equator": ev(rho, 0.0, 1.0),
            "theta_off_axis_behind": ev(theta, -1.0, 0.3), "theta_equator": ev(theta, 0.0, 1.0)}


def ds_arrival(d_emit_over_cH):
    """de Sitter (flat slicing, a = e^{Ht}, H = c = 1), observer 1 at the origin, position 2 at comoving chi; light
    emitted from 1 at a_e = 1 reaches chi when 1 - 1/a_r = chi; position 2 passes beyond 1's future event horizon
    (comoving radius 1/a) when a_h = 1/chi.  Returns (a_r, a_h), and a_r by numerical integration of d chi/dt = 1/a."""
    chi = d_emit_over_cH
    a_r = 1.0 / (1.0 - chi) if chi < 1 else float("inf")
    a_h = 1.0 / chi
    # numeric: integrate the light ray dchi/dt = e^{-t} until chi reached
    t, xi, h = 0.0, 0.0, 1e-5
    while xi < chi and t < 50:
        xi += h * (math.exp(-t) + 4 * math.exp(-(t + h / 2)) + math.exp(-(t + h))) / 6
        t += h
    return a_r, a_h, math.exp(t)


def compute():
    I = crossing.compute()["bits"]
    I_lo, I_hi = min(I.values()), max(I.values())
    bpm2 = bits_per_m2()
    D = bulk.L_PROXIMA
    u_D = energy_density_for_horizon(D)
    u_2D = energy_density_for_horizon(2 * D)
    H0 = cosmo.H0()
    u_lambda0 = (1.0 - cosmo.OMEGA_M) * energy_density_for_horizon(C / H0)
    region_J = u_D * 4.0 / 3.0 * math.pi * D ** 3
    # E3: incorporation at an illustrative enclosure of radius R (Schwarzschild), T from Parikh-Wilczek eq. 11
    R = ENCLOSURE_R_M
    T_enc = HBAR * C / (4 * math.pi * cosmo._KB * R)
    l_p = math.sqrt(HBAR * G / C ** 3)
    w = warp_fields()
    a_r, a_h, a_r_num = ds_arrival(0.75)
    with contextlib.redirect_stdout(io.StringIO()):
        wall = warpdrive.qi_wall(1.0)
        e_geom, e_j, e_kg = warpdrive.alcubierre_energy(ALC_R_M, wall, 1.0)
    return {"bits_per_m2": bpm2, "I_lo": I_lo, "I_hi": I_hi, "area_lo_m2": I_lo / bpm2, "area_hi_m2": I_hi / bpm2,
            "enclosure_R_m": R, "enclosure_mass_kg": R * C ** 2 / (2 * G), "enclosure_T_K": T_enc,
            "incorporation_dA_m2": I_lo / bpm2,
            "incorporation_energy_J": I_lo * cosmo._KB * T_enc * math.log(2),
            "bekenstein_floor_J": I_lo * HBAR * C * math.log(2) / (2 * math.pi * R),
            "mirror_kRs_s": I_lo * R / C, "mirror_scramble_s": R / C * math.log(R / l_p),
            "mirror_return_s": max(I_lo * R / C, R / C * math.log(R / l_p)),
            "mirror_return_hubble": max(I_lo * R / C, R / C * math.log(R / l_p)) * H0,
            "warp": w, "alc_wall_m": wall, "alc_energy_floor_J": abs(e_j), "alc_mass_floor_kg": abs(e_kg),
            "D_m": D, "u_for_horizon_D_J_m3": u_D, "u_for_horizon_2D_J_m3": u_2D, "u_lambda_today_J_m3": u_lambda0,
            "u_ratio": u_D / u_lambda0, "region_energy_J": region_J, "region_mass_msun": region_J / C ** 2 / MSUN,
            "crossing_factor_light_times": math.log(D / D0_M),
            "crossing_time_yr": math.log(D / D0_M) * D / C / cosmo.YR,
            "ds_example": {"d_emit_over_cH": 0.75, "a_arrive": a_r, "a_horizon_pass": a_h, "a_arrive_numeric": a_r_num,
                           "arrival_over_light_time": math.log(a_r) / 0.75}}


def report():
    d = compute()
    w = d["warp"]
    print("horizon.py -- the corridor as horizons that observe (M items 70-73), by deduction (verified once; seated 8l)\n")
    print("E1 a horizon takes all that crosses: %.3e bits/m^2 (Bousso 1.4e69); %.1e-%.1e bits need %.1e-%.1e m^2" % (
        d["bits_per_m2"], d["I_lo"], d["I_hi"], d["area_lo_m2"], d["area_hi_m2"]))
    print("E2 observation defines a horizon (Jacobson, Bousso, CHM)")
    print("E3 one horizon, two sides: position 2 inside incorporates.  A %.0f m enclosure (mass %.1e kg, T = %.2e K): "
          "incorporating %.2e bits adds %.1e m^2 and needs >= %.1f J (half Bekenstein's %.1f J); the mirror (prior "
          "entanglement) returns them in ~%.1e s = %.0f Hubble times (O(k r_S); scrambling alone %.1e s)" % (
              d["enclosure_R_m"], d["enclosure_mass_kg"], d["enclosure_T_K"], d["I_lo"], d["incorporation_dA_m2"],
              d["incorporation_energy_J"], d["bekenstein_floor_J"], d["mirror_return_s"], d["mirror_return_hubble"],
              d["mirror_scramble_s"]))
    print("E4 Alcubierre's pattern: theta behind %+.2f, ahead %+.2f; rho behind %.4f = ahead %.4f; on the axis %.1e; on "
          "the equator %.4f (theta there %.1e) -- the price is not in the contraction; Pfenning-Ford floor |E| >= %.2e J" % (
              w["theta_behind"], w["theta_ahead"], w["rho_behind"], w["rho_ahead"], w["rho_axis"], w["rho_equator"],
              w["theta_equator"], d["alc_energy_floor_J"]))
    print("E5 horizon around position 1 at D: u = %.2e J/m^3 (%.1e x today's dark energy); the region holds %.2e J = "
          "%.1e M_sun; a pattern from 1 m crosses after %.1f light times (%.0f yr); no comoving body is delivered" % (
              d["u_for_horizon_D_J_m3"], d["u_ratio"], d["region_energy_J"], d["region_mass_msun"],
              d["crossing_factor_light_times"], d["crossing_time_yr"]))
    e = d["ds_example"]
    print("E6 a signal emitted at separation 0.75 c/H arrives at a = %.2f, after position 2 passed 1's horizon at a = %.2f "
          "-- taken from 1, observed at 2, positive energy (u %.1e-%.1e J/m^3), %.2f light times: no speed gain" % (
              e["a_arrive"], e["a_horizon_pass"], d["u_for_horizon_2D_J_m3"], d["u_for_horizon_D_J_m3"],
              e["arrival_over_light_time"]))
    print("E7 whether a detector at position 2 registers it is one local event for every observer")


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
    w = d["warp"]
    chk("E1: S = A/(4 l_P^2) from the board's hbar, G, c gives %.3e bits/m^2, Bousso's READ 1.4e69 to 2 %%" %
        d["bits_per_m2"], abs(d["bits_per_m2"] / BOUSSO_BITS_PER_M2 - 1) < 0.02)
    chk("with h in place of hbar in l_P^2 it is %.2e, off Bousso's figure" % (d["bits_per_m2"] / (2 * math.pi)),
        abs(d["bits_per_m2"] / (2 * math.pi) / BOUSSO_BITS_PER_M2 - 1) > 0.5, ctl=True)
    lam = 1.0
    A_711 = apparent_horizon_area(lam / (8 * math.pi))
    A_98 = 4 * math.pi * ds_radius_sq(4, lam)
    chk("two READ equations agree: Bousso eq. 7.11 with rho_Lambda = Lambda/8 pi gives A_AH = %.6f, and eq. 9.8 gives "
        "4 pi a_0^2 = %.6f (Lambda = 1)" % (A_711, A_98), abs(A_711 - A_98) < 1e-12)
    chk("with rho = Lambda/4 pi they miss by a factor %.1f" % (A_98 / apparent_horizon_area(lam / (4 * math.pi))),
        abs(apparent_horizon_area(lam / (4 * math.pi)) - A_98) > 1, ctl=True)
    chk("E4: theta = -Tr K from Alcubierre's shift is positive behind (%+.2f) and negative ahead (%+.2f): his 'expanding "
        "behind, contracting in front'" % (w["theta_behind"], w["theta_ahead"]), w["theta_behind"] > 0 > w["theta_ahead"])
    chk("E4: Natario's rho = (theta^2 - K_ij K^ij)/16 pi computed from the shift equals his printed form for Alcubierre "
        "(max residual %.1e), and is equal behind and ahead (%.5f, %.5f) while theta flips" % (
            w["rho_vs_printed"], w["rho_behind"], w["rho_ahead"]),
        w["rho_vs_printed"] < 1e-12 and abs(w["rho_behind"] - w["rho_ahead"]) < 1e-12
        and w["theta_off_axis_behind"] > 0)
    chk("dropping the theta^2 term misses the printed form (residual %.1e) -- expansion enters rho with a positive sign" %
        w["rho_no_theta_vs_printed"], w["rho_no_theta_vs_printed"] > 1e-4, ctl=True)
    e = d["ds_example"]
    chk("E6: in de Sitter a signal emitted at separation 0.75 c/H arrives at a = %.4f (closed form) = %.4f (integrated), "
        "after position 2 passes 1's horizon at a = %.4f" % (e["a_arrive"], e["a_arrive_numeric"], e["a_horizon_pass"]),
        abs(e["a_arrive"] - e["a_arrive_numeric"]) < 1e-3 and e["a_arrive"] > e["a_horizon_pass"])
    a_r2, a_h2, _ = ds_arrival(0.4)
    chk("emitted at 0.4 c/H (< c/2H) it arrives before the horizon passes (a = %.3f < %.3f)" % (a_r2, a_h2),
        a_r2 < a_h2, ctl=True)
    structural.append("Alcubierre's eq. 12 equals theta = -Tr K by the chain rule (residual %.1e): the content is the sign "
                      "under eqs. 10-11's convention" % w["eq12_residual"])
    structural.append("E3's incorporation energy (T from Parikh-Wilczek eq. 11 times k ln 2 per bit) is exactly half of "
                      "Bekenstein's floor for the same radius -- algebra, not a second measurement")
    structural.append("E3's mirror time uses HP's O( ) estimates at unit coefficient (H-HP-ORDER), on their speculative "
                      "dynamical assumptions; for a body's bits the O(k r_S) term dominates")
    structural.append("E3 and E6 realise H-EXIT-BY-OBSERVATION's taking-and-observing with positive energy, but neither "
                      "beats light: the information reaches the horizon, or position 2, at <= c")
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
