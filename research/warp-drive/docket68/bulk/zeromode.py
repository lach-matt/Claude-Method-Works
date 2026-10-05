#!/usr/bin/env python3
"""
zeromode.py -- BULK3-O2: the lasting stasis through the massless (zero) graviton mode, worked by deduction from first
principles: where it lives in the bulk, how each plane couples to it, its own clock, and the price of loading the
defining information into it.

Not seated; verified once (2026-10-05), findings applied (HISTORY below).  M's orders: item 68 ("the first. The latter would be impossible but to the very
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
           zero mode is simply N_0 = 1/sqrt(k r_c)' (eq. 8, p.5) -- N_n divides in eq. 6, so chi_0 = 1/N_0 = sqrt(k r_c);
           the zero mode couples to our plane at 1/M_Pl-bar (eq. 10, p.5).  RS (hep-ph/9905221): eq. 13 writes the zero
           mode h-bar(x) with no phi-dependence, 'the physical graviton of the four-dimensional effective theory' (p.4);
           gravity is weak for us 'because of the small overlap of the graviton wave function in the fifth dimension
           (which is the warp factor) with our brane' (p.6); M_Pl-bar^2 = M^3 r_c int e^{-2 k r_c |phi|} dphi (eq. 16 --
           the same weight); g_hid = G(x, phi = 0) (eq. 3, p.2) and g_hid = g-bar (p.5).
  P-RS     (COMPUTED, bulk.py) k = 2e18 GeV, warp e^{k r_c pi} = 1e15 (H-RS1, H-K-PLANCK).
  P-SCALE  (READ, RS pp.5-6, crossing.py) masses 'measured with the metric g-bar'; 'we are assuming all fundamental mass
           parameters are of the same order' (p.6) -- the READ basis of H-SAME-LAGRANGIAN.
  P-KIN    four-momentum conservation: a state of zero invariant mass cannot decay into products of nonzero total
           invariant mass.
  P-POL    (READ, Flanagan & Hughes gr-qc/0501041 p.7) gravitational waves 'have two polarization components'; the
           quadrupole formula (eq. 4.23, p.19); 'it is extremely unlikely there will ever be an interesting laboratory
           source of GWs' (p.2).
  P-PETERS (COMPUTED, slingshot.py: Peters 1964, PINNED there) t_merge = (5/8) a^4 / (c r_s^3) for an equal-mass circular
           binary; with the Newtonian orbital energy -G m1 m2 / (2a) it gives the radiated power L(a) (DEDUCED, check 3).
  P-NULL   (DEDUCED from m = 0) a massless quantum moves on a null curve, along which the proper interval is zero.

DEDUCTIONS
  Z1 IT DOES NOT DECAY SPONTANEOUSLY.  [P-ZM, P-KIN]  A lightest state, massless (the unstabilised radion is massless too,
     H-UNSTABILISED): it cannot decay into massive products.  Redshift and spreading still act on a loaded pattern.
  Z2 WHERE ITS WEIGHT LIES.  [P-ZM, P-RS]  Its norm density per unit PROPER length y is e^{-2ky} (the weight of RS eq. 16):
     about 63 % of it within 1/(2k) = 4.9e-35 m (~3 Planck lengths, at the edge of the classical 5D description,
     H-K-PLANCK) of the hidden plane; the density at our plane is e^{-2 k r_c pi} = 1e-30 of that there (per unit
     conformal length the same ratio reads 1e-45: only integrated fractions are coordinate-free).  This locates the
     mode's weight -- RS's 'small overlap' -- NOT a place where loaded information is kept: the profile is fixed by the
     geometry and is the same for every excitation, ordinary gravitational waves included.
  Z3 IT COUPLES TO BOTH PLANES AT THE SAME 1/M_Pl-bar, EACH IN ITS OWN UNITS.  [P-ZM, P-SCALE]  chi_0 is constant, so the
     coupling through -(1/M^{3/2}) chi_0 / sqrt(r_c) is the same at phi = 0 and phi = pi (check 5; the massive modes'
     ratio is 2.5e-30, crossing.py).  What differs is each plane's natural energy: a process at the hidden plane's
     scale k has gravitational strength k/M_Pl-bar = 0.82, one at ours k e^{-k r_c pi}/M_Pl-bar = 8e-16
     (H-SAME-LAGRANGIAN).  The 1e15 is the warp -- the same single number as crossing.py's D7 and D8 (RS: 'this is the
     only small number produced', p.6) -- not a second asymmetry.
  Z4 NO TRANSIT ACROSS THE CORRIDOR.  [P-ZM, RS eq. 13]  A zero-mode excitation is one 4D field present at both planes at
     once, at equal g-bar amplitude, with no motion or speed in the fifth dimension -- in the corridor direction, a
     CANDIDATE counterpart of H-HIGHER-CORRIDOR's 'position 1 then position 2, with no in between'.  Valid in the
     zero-mode description: times >> the jump time (3.3e-28 s, crossing.py) and energies << m_1.
  Z5 ALONG THE PLANES: ZERO PROPER INTERVAL, READ FROM TWO POSITIONS.  [P-NULL, crossing.py D7]  The proper interval along
     its path is zero, an invariant both planes agree on; the elapsed coordinate time D/c is what depends on the reading
     position, and the two planes' clocks read it 1e15 apart -- one event pair read from two positions at once, a
     candidate form of H-POSITION-RELATIVE-SPEED.  Read from our plane it covers the Proxima span in 4.25 yr at c,
     passing every point between: it matches 'no in-between' in its own elapsed interval, not in position along the
     plane, and from our plane it HAS a speed -- in tension with H-NO-SPEED, carried as a tension, not a refutation.
     It holds for any massless quantum, light included.
  Z6 NO REST FRAME.  [P-NULL]  It can never be brought to rest in any form: a CANDIDATE counterpart of H-CORRIDOR-STASIS's
     'cannot take physical form' (like crossing.py D4).  It persists (Z1) without rest; holding it near one place needs
     confinement (OPEN).
  Z7 THE LOADING PRICE -- IF THE TRAVELLER LOADS.  [P-POL, P-PETERS, H-LAB-ROTOR, H-BIT-PER-GRAVITON, H-FLUX-HDOT2]  An
     illustrative rotor (two 500 kg masses 1 m apart at 100 Hz) radiates ~7e-31 W, ~5 gravitons/s; at one bit per
     graviton measure.py's lower count (9.5e27 bits) takes ~2e27 s, ~4e9 Hubble times.  At fixed tip speed and density
     the graviton rate grows as a^5: ~0.4 Hubble times at 100 m, ~6e4 yr at 1 km (computed).  Under H-SAME-LAGRANGIAN
     the same-physics rotor on the hidden plane loads per own tick (E/M_Pl-bar)^2 = 1e30 times faster (~2e-3 s of its
     own clock) -- but hidden-plane matter is then gravitationally strong at its natural scale, and its
     Chandrasekhar-like number falls to ~1e12 nucleons (H-CHANDRA-SCALING): a macroscopic hidden rotor would collapse
     (OPEN).  M's H-OBSERVED-NOT-LOADED and H-CORRIDOR-TAKES (items 70, 71) replace this picture: the corridor takes,
     the destination draws in -- modelled next, on READ horizon physics.

NAMED HYPOTHESES
  H-FLUX-HDOT2 (derivable from eq. 4.23 with flux ~ hdot^2; named conservatively), H-LAB-ROTOR (tip speed 314 m/s, rim
  stress ~ rho v^2 = 0.77 GPa for steel at 7800 kg/m^3: at the edge of high-strength steel; rod mass ignored),
  H-BIT-PER-GRAVITON (polarization alone gives one bit; timing, frequency or direction could add perhaps tens more --
  orders short of changing the conclusion), H-CHANDRA-SCALING (N ~ (M_Pl / m)^3, not READ), H-UNSTABILISED; bulk.py's
  H-RS1, H-K-PLANCK, H-SAME-LAGRANGIAN, H-OBSERVED-FRAME; crossing.py's H-CONFINED; and M's, as listed.

HISTORY (verifier, 2026-10-05; first-written claims kept)
  * Z2 first said 'A lasting stasis in the zero mode therefore resides, in the bulk, against the FAR plane' -- the
    profile locates the mode's weight, the same for every excitation, not a store for loaded information.
  * Z3 first read 'loading the zero mode is natural from the hidden plane and 1e15 weaker (in amplitude) from ours ...
    again an inhomogeneity' -- the coupling is the same at both planes in each plane's own units; the 1e15 is the warp,
    one number, not a second instance.
  * Z4 first called the zero proper time 'a CANDIDATE counterpart of H-NO-SPEED's ...' 'from the carrier's perspective'
    -- the phrase is H-HIGHER-CORRIDOR's, there is no carrier frame, and the carrier passes every point between along
    the plane; the corridor-direction counterpart (no transit in y) was missed.
  * the md said 'with anything buildable, loading ... would take billions of times the age of the universe' -- one
    illustrative rotor; the rate grows as a^5, and 1/H0 is not the age of the universe.
  * check 5 asserted a hard-coded 1.0; both controls were dummies (an unrelated integral; a dimensionally inconsistent
    ratio); now chi_0 is evaluated at both planes, and the controls are DHR's N_0 read literally and mu = m.
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


def chi0(phi, kpr):
    """The zero mode's profile (DHR eq. 6 with m_0 = 0: constant), chi_0 = 1/N_0 = sqrt(k r_c)."""
    return math.sqrt(kpr / math.pi)


def coupling_at(phi, kpr, chi=chi0):
    """|-(1/M^{3/2}) chi(phi) / sqrt(r_c)| in units M = r_c = 1 (DHR eq. 9 at phi = pi; RS eq. 3 at phi = 0)."""
    return abs(chi(phi, kpr))


def couplings():
    g = bulk.rs_geometry()
    mpl = searches.m_pl_bar_gev()
    k = bulk.RS["k_GeV"]
    kpr = g["k_pi_rc"]
    zr = coupling_at(math.pi, kpr) / coupling_at(0.0, kpr)
    return {"zero_mode_ratio_gbar": zr, "kk_ratio_gbar": crossing.hidden_coupling_ratio(),
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


def rotor_load_time(a_m, I, base=LAB_ROTOR, rho_scale=True):
    """Load time for a rotor scaled at fixed tip speed and density: m ~ a^3, Omega ~ 1/a."""
    s = a_m / base["a_m"]
    m = base["m_each_kg"] * s ** 3
    omega = 2 * math.pi * base["f_rot_hz"] / s
    L = rotor_power(m, a_m, omega)
    return I / (L / (HBAR * 2 * omega))


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
    scaling = {a_: rotor_load_time(a_, I_lo) / hubble_s for a_ in (1.0, 10.0, 100.0, 1000.0)}
    tip = omega * r["a_m"] / 2
    return {"rotor_load_hubble_by_arm_m": scaling, "rotor_tip_m_s": tip, "rotor_rim_stress_Pa": 7800.0 * tip ** 2,
            "hidden_load_own_s": t_load * (cp["own_scale_ours"] / cp["own_scale_hidden"]) ** 2,
            "chi0_sq_over_krc": prof["chi0_sq"] / prof["dhr_N0_inv_sq"], "norm_numeric": prof["norm_numeric"],
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
    print("zeromode.py -- BULK3-O2: a lasting stasis in the massless graviton mode, by deduction (verified once; not seated)\n")
    print("Z1 no spontaneous decay (a lightest state, massless)")
    print("Z2 its weight: density per proper length at our plane / at the hidden plane = %.1e; ~63%% within %.1e m of the "
          "hidden plane -- the mode's weight, not a store" % (d["density_ours_over_hidden"], d["residence_m"]))
    print("Z3 coupling at our plane / at the hidden plane (g-bar) = %.0f (massive modes %.1e); against each plane's natural "
          "energy %.2f vs %.1e -- the warp, one number" % (d["coupling_ratio_zero_mode"], d["coupling_ratio_kk"],
                                                          d["own_scale_hidden"], d["own_scale_ours"]))
    print("Z4 no transit across the corridor: one 4D field present at both planes at once")
    print("Z5 along the planes: proper interval %.0f (invariant); our clock reads %.3e s for the Proxima span" % (
        d["carrier_own_clock_s"], d["proxima_our_clock_s"]))
    print("Z6 no rest frame")
    print("Z7 IF the traveller loads: lab rotor %.2e W = %.1f gravitons/s (tip %.0f m/s, rim stress %.2f GPa); %.2e bits "
          "take %.1e s = %.1e Hubble times; by arm length (Hubble times): %s; hidden-plane same-physics rotor %.1e s of its "
          "own clock" % (d["rotor_power_W"], d["gravitons_per_s"], d["rotor_tip_m_s"], d["rotor_rim_stress_Pa"] / 1e9,
                         d["I_lo"], d["load_time_s"], d["load_time_hubble"],
                         {k_: "%.1e" % v for k_, v in d["rotor_load_hubble_by_arm_m"].items()}, d["hidden_load_own_s"]))
    print("    M's items 70-71: the corridor takes and the destination draws in -- the loading picture is replaced next")


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
    prof = zero_mode_profile(g["k_pi_rc"])
    literal = prof["norm_numeric"] / prof["chi0_sq"] * (1.0 / krc)        # chi_0 = N_0 read literally
    chk("DHR's N_0 read literally (chi_0 = N_0 = 1/sqrt(k r_c)) integrates to %.4f, not 1" % literal,
        abs(literal - 1) > 0.5, ctl=True)
    a = NS_BINARY["a_m"]
    m = NS_BINARY["m_each_kg"]
    om_k = math.sqrt(G_SI * 2 * m / a ** 3)
    Lp, _ = peters_power(m, a)
    Lq = quadrupole_power_closed(m, a, om_k)
    chk("Z7: the power deduced from slingshot.py's Peters merger time equals (32/5) G mu^2 a^4 Omega^6 / c^5 at the Kepler "
        "frequency (%.6e vs %.6e W)" % (Lp, Lq), abs(Lp / Lq - 1) < 1e-9)
    Lq_mu = quadrupole_power_closed(2 * m, a, om_k)                      # mu = m in place of m/2
    chk("with mu = m in place of m/2 they disagree (ratio %.2f)" % (Lq_mu / Lp), abs(Lq_mu / Lp - 1) > 1e-3, ctl=True)
    chk("Z3: chi_0 evaluated at both planes gives a coupling ratio %.12f, while the massive modes' is %.1e" % (
        d["coupling_ratio_zero_mode"], d["coupling_ratio_kk"]),
        abs(d["coupling_ratio_zero_mode"] - 1) < 1e-12 and d["coupling_ratio_kk"] < 1e-20)
    structural.append("Z5 (zero proper interval) and Z6 (no rest frame) follow from masslessness alone and hold for any "
                      "massless quantum, the photon included; Z4 (no transit in y) is the zero mode's own")
    structural.append("Z7's load time rests on H-LAB-ROTOR (an illustrative rotor) and H-BIT-PER-GRAVITON; the "
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
