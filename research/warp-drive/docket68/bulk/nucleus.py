#!/usr/bin/env python3
"""nucleus.py -- M's item 144 followed through: the relative laws act on the nucleus and the electron's mass.

M (item 144): "Yes" -- with light the same (item 143, H-LIGHT-INVARIANT), the relative laws by which another universe's
elements differ (item 138) act on the nucleus (its mass, its size, which nuclei are stable) and on the electron's mass.
The observable they move is mu = m_p/m_e (with nuclear size and stability beside it).

READ:
  Hanneke, Kuzhan & Lunstad 2020, arXiv:2007.15750: p.2 "Around 99 % of their mass [protons, neutrons] arises from the
      strong interaction ... By contrast, the electron is a fundamental particle. Its mass arises from its interaction
      with the Higgs field"; p.6 eq. (14) "The electronic energy T_e is independent of mu. The vibrational coefficient
      omega_e scales as 1/sqrt(mu) ... the rotational constant B_e ... as 1/mu"; p.3 eq. (2) high-redshift molecular
      spectra "constrain |Delta mu|/mu < 1e-6 - 1e-7 over ~1e10 yr".
  Bagdonaite et al. 2013, arXiv:1311.3438 (PRL 111, 231101): ten methanol lines in the PKS1830-211 lensing galaxy at
      z = 0.89, "a lookback time of 7.5 billion years", Table I (K_mu and V_LSR, transcribed below); "a purely
      statistical 1-sigma constraint of Delta mu/mu = (1.5 +- 1.5) x 10^-7" with reduced chi^2 = 10.2; robust
      "(-1.0 +- 0.8 stat +- 1.0 sys) x 10^-7"; ammonia K_mu = -4.46; H2 K_mu ~ 0.05.

  U1  (STRUCTURAL, READ scaling) what mu moves: a diatomic's levels T_e + omega_e (v+1/2) + B_e J(J+1) with
      omega_e ~ mu^-1/2, B_e ~ mu^-1 -- computed sensitivities K = 0 (electronic), -1/2 (vibrational), -1 (rotational)
  U2  the board refits Bagdonaite et al.'s Table I (17 points, V_LSR/c = a - K_mu Delta mu/mu): their statistical value
      (1.5 +- 1.5) x 10^-7 is reproduced, the error scaled by sqrt(reduced chi^2) as theirs is.  Control: a Delta mu/mu
      of 1e-6 injected into the same velocities is recovered
  U3  what it means for item 144: in the one distant cloud where it is best measured, the gas's mu is ours to a few
      parts in 10^7 (their robust result, stat and sys combined).  Matter there whose nuclear or electron mass differed
      by more would have shown as a slope across methanol's K_mu = -1 to -32.8
  U4  what the laws would do to a reconstruction at position 2 (item 136: "complete reconstruction at position 2"):
      the electrons' structure is rebuilt identically (alpha held); every vibrational frequency of the copy moves by
      -1/2 Delta mu/mu and every rotational one by -Delta mu/mu (STRUCTURAL)
Stdlib only.  python3 nucleus.py [--selftest]
"""
import math
import sys

C_KMS = 299792.458

# Bagdonaite et al. 2013 Table I: (transition, K_mu, V_LSR km/s, sigma km/s)    (READ)
METHANOL = [
    ("3-1-20E", -32.8, 9.1, 0.7), ("3-1-20E", -32.8, 10.7, 0.7), ("3-1-20E", -32.8, 12.6, 2.0), ("3-1-20E", -32.8, 7.4, 1.3),
    ("00-10A+", -1.0, 8.3, 0.1), ("00-10A+", -1.0, 8.8, 0.2), ("00-10A+", -1.0, 8.7, 0.2), ("00-10A+", -1.0, 7.8, 0.3),
    ("00-10E", -1.0, 8.9, 0.3), ("00-10E", -1.0, 10.4, 0.7), ("00-10E", -1.0, 7.6, 0.6),
    ("2-1-10E", -7.4, 9.8, 0.4), ("2-1-10E", -7.4, 8.0, 0.9),
    ("30-21A+", -2.7, 9.5, 1.5), ("1-1-10E+", -3.5, 10.5, 0.7), ("10-11A", -1.9, 8.8, 1.0), ("30-41A+", -1.6, 11.7, 0.3)]


def u1(eps=1e-6):
    """A diatomic with CO-like constants (cm^-1; standard values, not READ here): T_e, omega_e, B_e."""
    Te, we, Be = 65075.0, 2169.81, 1.9313
    E = lambda s, v, J, el=0: (Te if el else 0.0) + we * s**-0.5 * (v + 0.5) + Be / s * J * (J + 1)
    K = lambda f: (f(1 + eps) / f(1.0) - 1) / eps
    vib = lambda s: E(s, 1, 0) - E(s, 0, 0)
    rot = lambda s: E(s, 0, 1) - E(s, 0, 0)
    ele = lambda s: E(s, 0, 0, el=1) - E(s, 0, 0)                   # pure electronic offset, v and J held
    return {"K_vib": K(vib), "K_rot": K(rot), "K_ele": K(ele)}


def wls(data):
    S = Sx = Sy = Sxx = Sxy = 0.0
    for _, K, V, s in data:
        w = 1 / s**2
        S += w; Sx += w * K; Sy += w * V; Sxx += w * K * K; Sxy += w * K * V
    D = S * Sxx - Sx * Sx
    b = (S * Sxy - Sx * Sy) / D
    a = (Sxx * Sy - Sx * Sxy) / D
    sb = math.sqrt(S / D)
    chi2 = sum(((V - a - b * K) / s) ** 2 for _, K, V, s in data)
    nu = len(data) - 2
    return {"dmu": -b / C_KMS, "sig": sb / C_KMS, "chi2nu": chi2 / nu, "sig_scaled": sb / C_KMS * math.sqrt(chi2 / nu)}


def u2(inject=1e-6):
    fit = wls(METHANOL)
    shifted = [(nm, K, V - K * inject * C_KMS, sg) for nm, K, V, sg in METHANOL]      # V/c = -K dmu/mu added
    return {"fit": fit, "control": wls(shifted), "inject": inject}


def u3():
    stat, sys_ = 0.8e-7, 1.0e-7
    tot = math.hypot(stat, sys_)
    return {"robust": -1.0e-7, "total_sigma": tot, "two_sigma_bound": abs(-1.0e-7) + 2 * tot}


def u4(dmu=1e-7):
    return {"vib_shift": -0.5 * dmu, "rot_shift": -1.0 * dmu}


def compute():
    return {"u1": u1(), "u2": u2(), "u3": u3(), "u4": u4()}


def report(d):
    a, b, c, e = d["u1"], d["u2"], d["u3"], d["u4"]
    print("nucleus.py -- item 144: the relative laws on the nucleus and the electron's mass\n")
    print("U1 sensitivities (Born-Oppenheimer scaling): electronic %.3f, vibrational %.3f, rotational %.3f"
          % (a["K_ele"], a["K_vib"], a["K_rot"]))
    f = b["fit"]
    print("U2 refit of Bagdonaite et al. Table I (17 points): Delta mu/mu = %+.2e +- %.2e (unscaled), reduced chi^2 = %.1f, "
          "+- %.2e scaled -- theirs (1.5 +- 1.5)e-7" % (f["dmu"], f["sig"], f["chi2nu"], f["sig_scaled"]))
    print("   control, Delta mu/mu = %.0e injected into the same velocities: recovered %+.3e"
          % (b["inject"], b["control"]["dmu"]))
    print("U3 their robust result (-1.0 +- 0.8 stat +- 1.0 sys)e-7: combined sigma %.2e; |Delta mu/mu| < %.1e at 2 sigma, "
          "7.5 billion years back" % (c["total_sigma"], c["two_sigma_bound"]))
    print("U4 a copy rebuilt where mu differs by 1e-7: vibrations %+.1e, rotations %+.1e (fractional)"
          % (e["vib_shift"], e["rot_shift"]))


def selftest():
    ok = n = 0

    def chk(name, cond):
        nonlocal ok, n
        n += 1
        ok += bool(cond)
        print("  [%s] %s" % ("ok" if cond else "FAIL", name))

    d = compute()
    a, f, ctl, c = d["u1"], d["u2"]["fit"], d["u2"]["control"], d["u3"]
    chk("U1 (STRUCTURAL): electronic 0, vibrational -1/2, rotational -1",
        abs(a["K_ele"]) < 1e-9 and abs(a["K_vib"] + 0.5) < 1e-5 and abs(a["K_rot"] + 1) < 1e-5)
    chk("U2: the refit reproduces Bagdonaite et al.'s statistical value 1.5e-7 (+-0.1e-7) and chi^2/nu 10.2 (+-0.3)",
        abs(f["dmu"] - 1.5e-7) < 0.1e-7 and abs(f["chi2nu"] - 10.2) < 0.3)
    chk("U2: their quoted +-1.5e-7 is the fit's error scaled by sqrt(reduced chi^2) (+-0.1e-7)",
        abs(f["sig_scaled"] - 1.5e-7) < 0.1e-7)
    chk("U2 control (STRUCTURAL: the fit is linear): Delta mu/mu = 1e-6 injected into the same velocities is recovered (to 1e-9)",
        abs(ctl["dmu"] - f["dmu"] - d["u2"]["inject"]) < 1e-9)
    chk("U3: their robust result bounds |Delta mu/mu| below 4e-7 at 2 sigma", c["two_sigma_bound"] < 4e-7)
    print("selftest: %d/%d" % (ok, n))
    return ok == n


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    report(compute())
