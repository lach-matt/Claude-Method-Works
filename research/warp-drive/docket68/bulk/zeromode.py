#!/usr/bin/env python3
"""
zeromode.py -- BULK3-O2: the lasting stasis through the massless (zero) graviton mode, worked by deduction from first
principles: where it lives in the bulk, how each plane couples to it, its own clock, and the price of loading the
defining information into it.

Not seated; not yet verified.  M's orders: item 68 ("the first. The latter would be impossible but to the very
definition of the transition... There is no in-between...": the massless mode; the switched coupling set aside on M's
ruling); item 69 ("Seat both, then zero mode (Recommended)"); method M-DEDUCE (item 64).  Carried beside M's
H-CORRIDOR-STASIS, H-DETACH, H-POSITION-RELATIVE-SPEED, H-TWO-PERSPECTIVE-TENSION, H-NO-SPEED, H-HIGHER-CORRIDOR and
H-UNOBSERVED-UNBUILT, never as results.  O9 stays OPEN.

    python3 zeromode.py              report
    python3 zeromode.py --selftest   checks, with CONTROLS
    python3 zeromode.py --json       the numbers as JSON

PREMISES
  P-ZM     (READ, Davoudiasl-Hewett-Rizzo hep-ph/9909255) the tower h(x, phi) = sum h^(n)(x) chi^(n)(phi)/sqrt(r_c)
           (eq. 3) with orthonormality int dphi e^{-2 sigma} chi^(m) chi^(n) = delta_mn (p.4); 'the normalization of the
           zero mode is simply N_0 = 1/sqrt(k r_c)' (eq. 8, p.5); the zero mode couples to our plane at 1/M_Pl-bar
           (eq. 10, p.5).  RS (hep-ph/9905221 p.6): gravity is weak for us 'because of the small overlap of the graviton
           wave function in the fifth dimension (which is the warp factor) with our brane'.
  P-RS     (COMPUTED, bulk.py) k = 2e18 GeV, warp e^{k r_c pi} = 1e15 (H-RS1, H-K-PLANCK).
  P-POL    (READ, Flanagan & Hughes gr-qc/0501041 p.7) gravitational waves 'have two polarization components'; the
           quadrupole formula (eq. 4.23, p.19); 'it is extremely unlikely there will ever be an interesting laboratory
           source of GWs' (p.2).
  P-PETERS (COMPUTED, slingshot.py: Peters 1964, PINNED there) t_merge = (5/8) a^4 / (c r_s^3) for an equal-mass circular
           binary; with the Newtonian orbital energy -G m1 m2 / (2a) it gives the radiated power L(a) (DEDUCED, check 3).
  P-NULL   (DEDUCED from P-ZM's m = 0) a massless quantum moves on a null curve, on which the proper time is zero.

DEDUCTIONS
  Z1 THE ZERO MODE DOES NOT DECAY.  [P-ZM]  It is the lightest state, massless; a massless quantum cannot decay into
     massive ones (H-NO-MASSLESS-SPLIT: nor split into collinear massless ones in a way that loses the count).
  Z2 WHERE IT LIVES.  [P-ZM, P-RS]  Its norm density along the fifth dimension is chi_0^2 e^{-2 sigma}, chi_0 constant:
     it falls as e^{-2k y} with proper distance y from the hidden plane.  It sits within ~1/(2k) of the hidden plane;
     its density at our plane is e^{-2 k r_c pi} = 1e-30 of that at the hidden plane -- RS's 'small overlap'.  A
     lasting stasis in the zero mode therefore resides, in the bulk, against the FAR plane.
  Z3 HOW EACH PLANE COUPLES TO IT.  [P-ZM, P-SCALE (crossing.py)]  chi_0 is constant, so in g-bar the zero mode couples
     to both planes at the same 1/M_Pl-bar (ratio 1; the massive modes' ratio is 2.5e-30, crossing.py).  Read against
     each plane's OWN natural scale, the strength is k/M_Pl-bar ~ 0.8 at the hidden plane and k e^{-k r_c pi}/M_Pl-bar
     ~ 8e-16 at ours: loading the zero mode is natural from the hidden plane and 1e15 weaker (in amplitude) from ours.
     -- again an inhomogeneity between the two perspectives at the same time (H-TWO-PERSPECTIVE-TENSION's candidate
     form, crossing.py D8).
  Z4 ITS OWN CLOCK READS ZERO.  [P-NULL]  From the carrier's perspective no time passes between leaving and arriving;
     from ours it moves at c along the plane for D/c.  -- a CANDIDATE counterpart of H-NO-SPEED's 'position 1 then
     position 2, with no in between', from the carrier's perspective; it holds for any massless quantum.
  Z5 STASIS IS NOT REST.  [P-NULL]  A massless quantum has no rest frame: it persists (Z1) and ages not at all (Z4), but
     it moves at c along the planes.  Holding it near one place needs confinement (OPEN).
  Z6 THE PRICE OF LOADING IT FROM OUR PLANE.  [P-POL, P-PETERS, H-LAB-ROTOR, H-BIT-PER-GRAVITON]  The quadrupole power
     scales as Omega^6 at fixed reduced mass and size (H-FLUX-HDOT2: flux ~ hdot^2 with h ~ d^2 I/dt^2, eq. 4.23); a
     laboratory rotor (two 500 kg masses 1 m apart at 100 Hz, H-LAB-ROTOR) radiates ~7e-31 W, ~5 gravitons per second.
     At one bit per graviton (H-BIT-PER-GRAVITON: two polarizations give at most one bit in polarization alone), loading
     9.5e27 bits takes ~2e27 s -- about 4e9 Hubble times (the report prints the computed figures).  Compared with: a
     1.4+1.4 M_sun binary at 1e9 m (slingshot.py's check case) radiates ~2e25 W, but its pattern is its own orbit, not a
     body's: the bottleneck is modulating the source with the defining information, not the raw graviton count (OPEN).

NAMED HYPOTHESES
  H-NO-MASSLESS-SPLIT, H-FLUX-HDOT2, H-LAB-ROTOR, H-BIT-PER-GRAVITON (above); bulk.py's H-RS1, H-K-PLANCK,
  H-SAME-LAGRANGIAN, H-OBSERVED-FRAME; crossing.py's H-CONFINED; and M's, as listed.
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
        searches = _by_path("bulk_searches", os.path.join(HERE, "searches.py"))
        crossing = _by_path("bulk_crossing", os.path.join(HERE, "crossing.py"))
        slingshot = _by_path("wd_slingshot", os.path.join(WD, "slingshot.py"))
finally:
    sys.path[:] = _saved

C = bulk.C
HBAR = crossing.HBAR
MSUN = slingshot.MSUN
G_SI = slingshot.G
LAB_ROTOR = {"m_each_kg": 500.0, "a_m": 1.0, "f_rot_hz": 100.0}       # H-LAB-ROTOR: illustrative
NS_BINARY = {"m_each_kg": 1.4 * MSUN, "a_m": 1e9}                       # slingshot.py's Peters check case


# ------------------------------------------------------------------ Z2, Z3: the profile and the couplings
def zero_mode_profile(kpr, n=200000):
    """chi_0 from DHR's orthonormality (int_{-pi}^{pi} e^{-2 k r_c |phi|} chi_0^2 dphi = 1), in units r_c = 1: returns
    chi_0^2 (closed form), the numerical norm with it, and the density ratio (ours / hidden)."""
    krc = kpr / math.pi
    chi0_sq = krc / (1 - math.exp(-2 * kpr))
    h = math.pi / n
    integ = 2 * sum((1 if i in (0, n) else (4 if i % 2 else 2)) * math.exp(-2 * krc * i * h) for i in range(n + 1)) * h / 3
    return {"chi0_sq": chi0_sq, "norm_numeric": chi0_sq * integ, "density_ours_over_hidden": math.exp(-2 * kpr),
            "dhr_N0_inv_sq": krc}


def couplings():
    g = bulk.rs_geometry()
    mpl = searches.m_pl_bar_gev()
    k = bulk.RS["k_GeV"]
    return {"zero_mode_ratio_gbar": 1.0, "kk_ratio_gbar": crossing.hidden_coupling_ratio(),
            "own_scale_hidden": k / mpl, "own_scale_ours": g["k_vis_GeV"] / mpl}


# ------------------------------------------------------------------ Z6: the power, from the board's Peters time
def peters_power(m_each, a):
    """L = -dE/dt for an equal-mass circular binary, from slingshot.py's Peters merger time (t ~ a^4, so
    da/dt = -a / (4 t)) and the Newtonian orbital energy -G m^2 / (2a)."""
    M = 2 * m_each
    rs = 2 * G_SI * M / C ** 2
    beta = math.sqrt(rs / (8 * a))                              # slingshot.a_over_rs inverted
    t_merge = slingshot.orbits_to_merger(beta) * slingshot.orbital_period(beta, M)
    return G_SI * m_each ** 2 / (8 * a * t_merge), t_merge


def quadrupole_power_closed(m_each, a, omega):
    """(32/5) G mu^2 a^4 Omega^6 / c^5 -- the closed form the Peters power must equal at the Kepler frequency (check 3)."""
    mu = m_each / 2
    return 32.0 / 5.0 * G_SI * mu ** 2 * a ** 4 * omega ** 6 / C ** 5


def rotor_power(m_each, a, omega):
    """H-FLUX-HDOT2: the power at a driven Omega is the Peters power at the same masses and size times (Omega/Omega_K)^6."""
    M = 2 * m_each
    omega_k = math.sqrt(G_SI * M / a ** 3)
    L_k, _ = peters_power(m_each, a)
    return L_k * (omega / omega_k) ** 6


def compute():
    g = bulk.rs_geometry()
    prof = zero_mode_profile(g["k_pi_rc"])
    cp = couplings()
    inv_2k_m = g["inv_k_m"] / 2
    r = LAB_ROTOR
    omega = 2 * math.pi * r["f_rot_hz"]
    L_rot = rotor_power(r["m_each_kg"], r["a_m"], omega)
    e_grav = HBAR * 2 * omega                                   # gravitons at twice the rotation frequency
    n_rate = L_rot / e_grav
    I_lo = crossing.compute()["I_lo"]
    t_load = I_lo / n_rate                                       # H-BIT-PER-GRAVITON
    hubble_s = 1.0 / bulk.cosmo.H0()
    L_ns, t_ns = peters_power(NS_BINARY["m_each_kg"], NS_BINARY["a_m"])
    return {"chi0_sq_over_krc": prof["chi0_sq"] / prof["dhr_N0_inv_sq"], "norm_numeric": prof["norm_numeric"],
            "density_ours_over_hidden": prof["density_ours_over_hidden"], "residence_m": inv_2k_m,
            "coupling_ratio_zero_mode": cp["zero_mode_ratio_gbar"], "coupling_ratio_kk": cp["kk_ratio_gbar"],
            "own_scale_hidden": cp["own_scale_hidden"], "own_scale_ours": cp["own_scale_ours"],
            "own_scale_ratio": cp["own_scale_hidden"] / cp["own_scale_ours"],
            "rotor_power_W": L_rot, "graviton_J": e_grav, "gravitons_per_s": n_rate, "I_lo": I_lo,
            "load_time_s": t_load, "load_time_hubble": t_load / hubble_s,
            "ns_binary_power_W": L_ns, "ns_merge_s": t_ns,
            "proxima_our_clock_s": bulk.L_PROXIMA / C, "carrier_own_clock_s": 0.0}


def report():
    d = compute()
    print("zeromode.py -- BULK3-O2: a lasting stasis in the massless graviton mode, by deduction (not verified; not seated)\n")
    print("Z1 it does not decay (massless, lightest)")
    print("Z2 where it lives: density at our plane / at the hidden plane = %.1e; it sits within ~%.1e m of the hidden "
          "plane -- against the FAR plane" % (d["density_ours_over_hidden"], d["residence_m"]))
    print("Z3 coupling: equal at both planes in g-bar (ratio %.0f; the massive modes' %.1e); against each plane's own "
          "scale %.2f (hidden) vs %.1e (ours) -- %.0e apart: natural from the hidden plane, weak from ours" % (
              d["coupling_ratio_zero_mode"], d["coupling_ratio_kk"], d["own_scale_hidden"], d["own_scale_ours"],
              d["own_scale_ratio"]))
    print("Z4 its own clock reads %.0f s for any crossing; ours reads %.3e s for the Proxima span along the plane" % (
        d["carrier_own_clock_s"], d["proxima_our_clock_s"]))
    print("Z5 it has no rest frame: persistence without rest; confinement is OPEN")
    print("Z6 loading it from our plane: a lab rotor (H-LAB-ROTOR) radiates %.2e W = %.1f gravitons/s; %.2e bits take "
          "%.1e s = %.1e Hubble times (H-BIT-PER-GRAVITON); a 1.4+1.4 M_sun binary at 1e9 m radiates %.2e W" % (
              d["rotor_power_W"], d["gravitons_per_s"], d["I_lo"], d["load_time_s"], d["load_time_hubble"],
              d["ns_binary_power_W"]))


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
    chk("Z2: the zero mode normalised by DHR's orthonormality integrates to %.9f, and chi_0^2 = k r_c (DHR's N_0 = "
        "1/sqrt(k r_c)) to %.1e" % (d["norm_numeric"], abs(d["chi0_sq_over_krc"] - 1)),
        abs(d["norm_numeric"] - 1) < 1e-6 and abs(d["chi0_sq_over_krc"] - 1) < 1e-12)
    g = bulk.rs_geometry()
    krc = g["k_pi_rc"] / math.pi
    h = math.pi / 2000
    flat = 2 * sum((1 if i in (0, 2000) else (4 if i % 2 else 2)) for i in range(2001)) * h / 3
    chk("without the warp weight e^{-2 sigma} the same chi_0 integrates to %.1f, not 1" % (krc * flat),
        abs(krc * flat - 1) > 1, ctl=True)
    a = NS_BINARY["a_m"]
    m = NS_BINARY["m_each_kg"]
    om_k = math.sqrt(G_SI * 2 * m / a ** 3)
    Lp, _ = peters_power(m, a)
    Lq = quadrupole_power_closed(m, a, om_k)
    chk("Z6: the power deduced from slingshot.py's Peters merger time equals (32/5) G mu^2 a^4 Omega^6 / c^5 at the Kepler "
        "frequency (%.6e vs %.6e W)" % (Lp, Lq), abs(Lp / Lq - 1) < 1e-9)
    chk("with Omega^5 in place of Omega^6 they disagree (ratio %.1e)" % (Lp / (Lq / om_k)),
        abs(Lp / (Lq / om_k) - 1) > 1e-3, ctl=True)
    chk("Z3: the zero mode couples equally to both planes in g-bar (1) while the massive modes do not (%.1e)" % (
        d["coupling_ratio_kk"]), d["coupling_ratio_zero_mode"] == 1.0 and d["coupling_ratio_kk"] < 1e-20)
    structural.append("Z4 (zero proper time) and Z5 (no rest frame) follow from masslessness alone and hold for any "
                      "massless quantum, the photon included -- not specific to the corridor")
    structural.append("Z6's load time rests on H-LAB-ROTOR (an illustrative rotor) and H-BIT-PER-GRAVITON; the "
                      "bottleneck named is modulation by the defining information, not the raw graviton count")
    structural.append("Z3's own-scale reading uses k and k e^{-k r_c pi} as each plane's natural scale "
                      "(H-SAME-LAGRANGIAN); the 1e15 is the warp, the same factor as crossing.py's clocks")
    for s_ in structural:
        print("  STRUCTURAL: " + s_)
    print("zeromode.py: %d/%d checks pass, %d of them controls; %d STRUCTURAL printed, not counted" % (
        n_pass, n_pass + n_fail, n_ctl, len(structural)))
    return n_fail == 0


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    elif "--json" in sys.argv:
        print(json.dumps(compute(), indent=1, default=str))
    else:
        report()
