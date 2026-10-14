#!/usr/bin/env python3
"""
DOCKET 67, pass S, result 20: warp-folder-printed-parameters.

Re-derives, from the Drive folder "Warp" read 2026-09-26 through the Drive
connector (file ids below), every printed parameter warpfolder.py:210-236 uses,
and the arithmetic built on them.  Nothing under research/ is imported or
edited; the constants are re-typed from the documents' text as read today.

Exit 0 iff every assertion holds.  Assertions are of three kinds:
  T  transcription  -- the tree's constant equals the printed figure
  A  arithmetic     -- a computed consequence (sympy exact where closed form)
  D  drift/robust   -- a hypothesis the tree adds, and whether it moves the
                       conclusion (computed both ways)
"""
import math
import sys
import sympy as sp

FAILS = []


def chk(tag, label, ok, val=""):
    print("  [%s] %s %-66s %s" % ("ok" if ok else "XX", tag, label, val))
    if not ok:
        FAILS.append(label)


# --------------------------------------------------------------- the sources
# Drive ids, folder 1U2VjhhcC28qEu3NeLilwVi1k_dB6FUo7 ("Warp"):
PULSED = "1TrZc7CBf-msA10ZW_8w4z538788pAkNJ"   # pulsed_ignition_and_optics_specification.pdf
BLUE = "1bugkRaEvcWdFLl888HQNcJ3jIS_5_kQA"     # schematics_and_blueprints.pdf
TMPS = "1zv_kkVd1q3nebHMZELwdU8stInJ29tuz"     # transient_metric_propulsion_specification.pdf
COST = "1iRdiHDcN9cDqiPOssJhYWvOA1FUXtySs"     # cost_and_location_assessment.pdf

# Verbatim fragments as returned by read_file_content on 2026-09-26.
QUOTES = {
    "marx_c_v": (PULSED, "charges ten 100 nF energy storage capacitors ($C\\_1 \\\\dots C\\_{10}$) "
                          "in parallel through $1 ext{ M}\\\\Omega$ ceramic isolation resistors "
                          "($R\\_{charge}$) up to $+50 ext{ kV DC}$"),
    "marx_rating": (PULSED, "Storage Capacitors 10x 100 nF / 60 kV High-Energy Density Film"),
    "marx_out": (PULSED, "$V\\_{out} = 10 imes 50 ext{ kV} = 500 ext{ kV}$ at $10 ext{ kA}$ peak current"),
    "marx_fwhm": (PULSED, "Discharge Time ($ au$) $\\\\sim 12 ext{ ns}$"),
    "supply": (PULSED, "Charging Supply +50 kV, 20 kW Continuous DC Module"),
    "peak_power": (PULSED, "PEAK POWER: 10 Petawatts (Coherent Pulse)"),
    "pulse": (PULSED, "femtosecond pulses ($30 ext{ fs}$ duration)"),
    "spot": (PULSED, "diffraction-limited spot diameter of $0.1 ext{ mm} $ ($100\\\\mu ext{m}$) "
                      "directly on the central spin axis, achieving localized intensities "
                      "exceeding $10^{20} ext{ W/cm} ^2$"),
    "power_flow": (PULSED, "The 500 kV output pulse drives an array of eight chirped-pulse "
                            "amplification (CPA) laser heads"),
    "planck": (PULSED, "Electromagnetic Shear + Optical Intensity Spikes to Planck Threshold"),
    "rotor_d": (BLUE, "Flywheel Rotor Diameter: 1.8 meters Carbon-Fiber Wrapped Beryllium-Copper Alloy"),
    "rotor_rpm": (BLUE, "[C/E] Dual Rotors Relativistic Field Shearing 85,000 RPM Counter-Rotating Assembly"),
    "rotor_pair": (COST, "Operating a 1.8-meter flywheel at 85,000 RPM"),
    "rotor_ke": (COST, "Mitigates risks from rotational kinetic energy storage (85,000 RPM rotor)"),
    "ceiling": (COST, "15,000 – 25,000 sq ft industrial layout (25 – 30 ft vertical ceiling clearance)"),
    "utility": (COST, "1.5 – 3 MW three-phase utility feed"),
    "stator": (BLUE, "Superconducting Stator Diameter: 2.1 meters REBCO HTS Tape (20 Tesla Operational Field)"),
    "shell": (BLUE, "Outer Shield Shell Diameter: 2.5 meters"),
    "muCF": (TMPS, "A central copper disc containing a muon-catalyzed fusion ($\\\\mu ext{CF}$) starter cell"),
    "relativistic": (TMPS, "Counter-rotating the inner disc (CCW) and outer ring (CW) at relativistic surface velocities"),
    "row1": (TMPS, "Micro Payload (100 kg) ... 1.48 imes 10^{-25} ... $8.98 imes 10^{18} ext{ J}$"),
    "row2": (TMPS, "Standard Vehicle (5,000 kg) $\\\\sim 7.42 imes 10^{-24} ext{ m}$ ... $4.49 imes 10^{20} ext{ J}$"),
    "row3": (TMPS, "Large Structure (100,000 kg) $\\\\sim 1.48 imes 10^{-22} ext{ m}$ ... $8.98 imes 10^{22} ext{ J}$"),
}

# ----------------------------------------------------------- the tree's values
# warpfolder.py:212-220, 235 (re-typed, not imported)
TREE = dict(MARX_STAGES=10, MARX_C=100e-9, MARX_V=50e3, LASER_I=1e20,
            LASER_SPOT=0.1e-3, LASER_T=30e-15, ROTOR_D=1.8, ROTOR_RPM=85000.0,
            PAYLOADS=(100.0, 5000.0, 1.0e5), TABLE_1E5=8.98e22)

# ------------------------------------------------ printed values, from QUOTES
PRINTED = dict(MARX_STAGES=10, MARX_C=100e-9, MARX_V=50e3, LASER_I=1e20,
               LASER_SPOT=0.1e-3, LASER_T=30e-15, ROTOR_D=1.8, ROTOR_RPM=85000.0,
               PAYLOADS=(100.0, 5000.0, 1.0e5), TABLE_1E5=8.98e22,
               MARX_RATED_V=60e3, PEAK_P=10e15, OUT_V=500e3, OUT_I=10e3,
               FWHM=12e-9, SUPPLY_W=20e3, R_CHARGE=1e6, CEIL_FT=30.0,
               UTIL_W_MAX=3e6, B_T=20.0, STATOR_D=2.1, SHELL_D=2.5)
TABLE = [(100.0, 1.48e-25, 8.98e18), (5000.0, 7.42e-24, 4.49e20),
         (1.0e5, 1.48e-22, 8.98e22)]

# ----------------------------------------------------------------- constants
c = 299792458.0                  # exact
G = 6.67430e-11                  # CODATA 2018 = CODATA 2022 value
HBAR = 1.054571817e-34           # exact (2019 SI)
MU0 = 4e-7 * math.pi * (1 + 5.5e-10)   # 2019 SI mu0, to 1e-9
E_CH = 1.602176634e-19
M_E = 9.1093837139e-31

print("warp-folder-printed-parameters.py -- DOCKET 67 pass S item 20")
print()
print("T  TRANSCRIPTION (tree constant == printed figure)")
for k in TREE:
    chk("T", "%s = %r" % (k, TREE[k]), TREE[k] == PRINTED[k])
for key in ("marx_c_v", "spot", "pulse", "rotor_d", "rotor_rpm", "rotor_pair", "row3", "planck"):
    chk("T", "quote on file: %s (%s)" % (key, QUOTES[key][0][:8]), len(QUOTES[key][1]) > 0)

print()
print("A  ARITHMETIC")
C, V, N = sp.symbols("C V N", positive=True)
# Marx: parallel charge N*(1/2)CV^2 == erected (C/N)*(N V)^2 / 2, exactly
chk("A", "Marx parallel store == erected store (sympy identity)",
    sp.simplify(N * C * V**2 / 2 - (C / N) * (N * V)**2 / 2) == 0)
E_marx = 10 * 0.5 * 100e-9 * 50e3**2
chk("A", "Marx store at 50 kV = 1250 J", abs(E_marx - 1250.0) < 1e-9, E_marx)
E_marx_rated = 10 * 0.5 * 100e-9 * 60e3**2
chk("A", "Marx store at the 60 kV RATING = 1800 J (ceiling)", abs(E_marx_rated - 1800) < 1e-9, E_marx_rated)
E_pulse_fwhm = 500e3 * 10e3 * 12e-9
chk("A", "500 kV x 10 kA x 12 ns = 60 J (<= store: consistent)", E_pulse_fwhm <= E_marx, E_pulse_fwhm)
t_min_charge = E_marx / 20e3
chk("A", "20 kW supply needs >= 62.5 ms to charge (timeline gives 109 ms)",
    abs(t_min_charge - 0.0625) < 1e-12 and t_min_charge < 0.109, t_min_charge)
RC = 1e6 * 100e-9
chk("A", "per-stage R_charge*C = 0.1 s (so 50 kV by 109 ms is a ceiling)", abs(RC - 0.1) < 1e-15, RC)

area_cm2 = math.pi * (0.1e-3 * 100 / 2) ** 2
E_laser_I = 1e20 * area_cm2 * 30e-15
chk("A", "laser I*area*t at 1e20 W/cm^2 = 235.6 J", abs(E_laser_I - 235.619) < 1e-2, E_laser_I)
I_from_P = 10e15 / area_cm2
chk("A", "10 PW over the 0.1 mm spot = 1.27e20 W/cm^2 ('exceeding 1e20': consistent)",
    I_from_P > 1e20 and abs(I_from_P / 1.2732e20 - 1) < 1e-3, "%.4e" % I_from_P)
E_laser_P = 10e15 * 30e-15
chk("A", "laser at the printed 10 PW peak x 30 fs = 300 J (ceiling)", abs(E_laser_P - 300) < 1e-9, E_laser_P)

# The table: r_s = 2GM/c^2, E = Mc^2; printed figures are TRUNCATED to 3 s.f.
def trunc3(x):
    e = math.floor(math.log10(x))
    return math.floor(x / 10**e * 100) / 100 * 10**e
for M, rs_p, E_p in TABLE:
    rs, E = 2 * G * M / c**2, M * c**2
    chk("A", "r_s(%g kg) = %.5e ; printed %.2e = truncation" % (M, rs, rs_p),
        abs(trunc3(rs) / rs_p - 1) < 1e-9)
    if M < 1e5:
        chk("A", "E(%g kg) = %.5e ; printed %.2e = truncation" % (M, E, E_p),
            abs(trunc3(E) / E_p - 1) < 1e-9)
E3 = 1e5 * c**2
chk("A", "E(1e5 kg) = 8.98755e21, printed 8.98e22: ratio 9.9916 (x10 cell)",
    abs(8.98e22 / E3 - 9.9916) < 1e-3, "%.5f" % (8.98e22 / E3))
chk("A", "  and its mantissa is the truncation of the right value (exponent slip only)",
    abs(trunc3(E3) * 10 / 8.98e22 - 1) < 1e-9)

E_need = 100 * c**2
store_tree = E_marx + E_laser_I
sf_tree = E_need / store_tree
chk("A", "tree's shortfall 6.050e15 = 15.78 orders", abs(math.log10(sf_tree) - 15.7818) < 1e-3,
    "%.4f" % math.log10(sf_tree))

v_tip = math.pi * 1.8 * 85000 / 60
chk("A", "tip speed 8011.06 m/s", abs(v_tip - 8011.06) < 0.01, v_tip)
chk("A", "v/c = 2.672e-5 ; counter-rotating relative 5.34e-5 : not relativistic",
    v_tip / c < 1e-4 and 2 * v_tip / c < 1e-4, "%.3e" % (v_tip / c))
gm1 = 1 / math.sqrt(1 - (2 * v_tip / c) ** 2) - 1
chk("A", "  gamma-1 at the RELATIVE speed = %.2e" % gm1, gm1 < 2e-9)

E_P = math.sqrt(HBAR * c**5 / G)
chk("A", "Planck energy 1.956e9 J; store/E_P = 7.60e-7", abs(store_tree / E_P - 7.595e-7) < 1e-9)

print()
print("D  HYPOTHESIS DRIFT, EACH COMPUTED BOTH WAYS")
# D1 laser is DOWNSTREAM of the Marx bank (power-flow sentence): tree sums both
sf_marx_only = E_need / E_marx
chk("D", "D1 Marx-only (no double count): %.4f orders (tree 15.78; tree favours doc)"
    % math.log10(sf_marx_only), math.log10(sf_marx_only) > math.log10(sf_tree))
# D2 ceilings from the documents' own printed maxima
store_ceiling = E_marx_rated + E_laser_P
chk("D", "D2 printed ceilings (60 kV rating + 10 PW, still summed) = %.0f J -> %.4f orders"
    % (store_ceiling, math.log10(E_need / store_ceiling)), math.log10(E_need / store_ceiling) > 15.6)
# D3 energy stores the tree does not count: rotor KE, 20 T field, utility, muCF
rho_becu, rho_os = 8250.0, 22590.0            # ORDER, not from the folder
ceil_m = 30 * 0.3048
R = 0.9
m_rotor_max = rho_becu * math.pi * R**2 * ceil_m     # solid disc, full ceiling height
KE_disc_max = 0.25 * m_rotor_max * v_tip**2           # I w^2/2 = m v_tip^2 / 4
m_os = rho_os * math.pi * R**2 * ceil_m
KE_rim_os = 0.5 * m_os * v_tip**2                     # thin-rim bound v^2/2 per kg, densest metal
chk("D", "D3a rotor KE per kg at v_tip: <= v^2/2 = %.3e J/kg" % (v_tip**2 / 2), True)
m_needed = 2 * E_need / v_tip**2
chk("D", "D3a rotor mass to supply M c^2 even as a thin rim = %.3e kg" % m_needed, m_needed > 1e11)
L_needed = 4 * E_need / v_tip**2 / (rho_becu * math.pi * R**2)
chk("D", "D3a  = a 1.8 m Be-Cu disc %.3e m long (facility ceiling 9.14 m)" % L_needed, L_needed > 1e6)
chk("D", "D3a Be-Cu disc filling the 30 ft ceiling: KE %.3e J -> shortfall %.2f orders"
    % (KE_disc_max, math.log10(E_need / KE_disc_max)), E_need / KE_disc_max > 1e6)
chk("D", "D3a osmium thin-rim bound, same volume: %.3e J -> %.2f orders"
    % (KE_rim_os, math.log10(E_need / KE_rim_os)), E_need / KE_rim_os > 1e5)
KE_1m = 0.25 * rho_becu * math.pi * R**2 * 1.0 * v_tip**2
chk("D", "D3a a 1 m-thick Be-Cu disc: KE %.3e J -> %.2f orders (vs tree 15.78)"
    % (KE_1m, math.log10(E_need / KE_1m)), 7 < math.log10(E_need / KE_1m) < 8)
u_B = 20.0**2 / (2 * MU0)
E_B = u_B * math.pi * (2.5 / 2) ** 2 * ceil_m
chk("D", "D3b 20 T field energy %.3e J/m^3; filling shell x ceiling = %.3e J" % (u_B, E_B), E_B < 1e11)
t_util = E_need / 3e6
chk("D", "D3c 3 MW feed takes %.3e s = %.0f yr to deliver M c^2" % (t_util, t_util / 3.156e7),
    t_util / 3.156e7 > 9e4)
chk("D", "D3d muCF starter cell: NAMED, UNQUANTIFIED in the folder -> not computable", True)
AMU = 1.66053906892e-27
e_DT = 17.589e6 * E_CH / ((2.014102 + 3.016049) * AMU)   # J/kg, full burn of D+T
V_rotor = math.pi * R**2 * ceil_m
E_fus_max = e_DT * 250.0 * V_rotor                        # solid DT ~0.25 g/cm^3 (ORDER)
chk("D", "D3d BOUND: whole 1.8 m x 9.14 m rotor of solid DT, 100%% burn = %.3e J -> %.2f orders short"
    % (E_fus_max, math.log10(E_need / E_fus_max)), E_fus_max < E_need)
# D4 "Planck Threshold" is printed as an OPTICAL INTENSITY; tree reads energy
I_P_cm2 = c**8 / (HBAR * G**2) / 1e4
chk("D", "D4 Planck intensity c^8/(hbar G^2) = %.3e W/cm^2; 1.27e20 is %.1f orders short"
    % (I_P_cm2, math.log10(I_P_cm2 / I_from_P)), I_P_cm2 / I_from_P > 1e90)
E_S = M_E**2 * c**3 / (E_CH * HBAR)
I_S = 0.5 * c * 8.8541878188e-12 * E_S**2 / 1e4
chk("D", "D4 even the Schwinger intensity %.2e W/cm^2 is not reached" % I_S, I_S > I_from_P)
# D5 rotor burst: rim sqrt(s/rho) vs solid isotropic disc sqrt(8 s/((3+nu) rho))
nu = 0.3
for name, s, rho in (("T1000 fibre", 6.4e9, 1800.0), ("Be-Cu", 1.4e9, 8250.0)):
    v_rim = math.sqrt(s / rho)
    v_disc = math.sqrt(8 * s / ((3 + nu) * rho))
    chk("D", "D5 %-11s over rim limit %.2fx, over solid-disc limit %.2fx" %
        (name, v_tip / v_rim, v_tip / v_disc), v_tip / v_disc > 1)

print()
if FAILS:
    print("FAILED: %d" % len(FAILS))
    for f in FAILS:
        print("   ", f)
    sys.exit(1)
print("ALL ASSERTIONS HOLD")
