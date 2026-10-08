#!/usr/bin/env python3
"""o3_ground.py -- Warp Theorem lemma O3, M-RULINGS item 164: what oscillates in a ground state, and what the write under
item 163 needs of the corridor's energy.  Computed, READ and deduced; not verified; not seated.

M's words (verbatim in the rulings file): item 164 "The ground state of any atom is an oscillating state. Thus its
energy oscillates as well" (answering the board's "Achievability conflicts with your rulings. Margolus–Levitin's
achieving state needs an energy spread, a level at 2E, and it oscillates back."); item 133 "There is only one exact
energy needed for any given README"; item 162 "The throat doesn't change size"; item 163 "All together, one whole".

READ  Margolus & Levitin, quant-ph/9710043 (re-read in full 2026-10-08): §2.1, "we will choose our zero of energy so
      that E0 = 0" (with footnote 2); eq. (4), tau >= h/(4E), E the average energy above the ground state, and eq. (5),
      the earlier bound tau >= h/(4 Delta E) (Mandelstam-Tamm, their ref. [10]), p.4; eq. (6), |psi_t> = sum_n c_n
      e^(-i E_n t/hbar) |E_n>, and eq. (7), S(t) = sum |c_n|^2 e^(-i E_n t/hbar); eqs. (10)-(11), the achieving state,
      for which "Delta E = E"; p.9, "an isolated stationary atom in an exact energy eigenstate never transitions to an
      orthogonal state".

  G1 WHAT OSCILLATES IN A GROUND STATE (computed).  Hydrogen's 1s and the oscillator's ground state solve H psi = E0 psi
     exactly; evolved by eq. (6) they become e^(-i E0 t/hbar) psi.  So the phase rotates -- at E0/h -- and the position
     has a nonzero spread that never goes away (1s: <r> = 3/2 a0, Delta r = (sqrt 3/2) a0; oscillator: Delta x =
     1/sqrt 2).  Both are true of every ground state, and in that sense it is an oscillating state.
  G2 ITS ENERGY DOES NOT (computed).  In the same states the energy's spread is exactly 0 and <r>, <r^2>, <H> are
     constant in t; the survival amplitude S(t) has |S| = 1 for every t, so the state never turns orthogonal (ML p.9).
     The rotation's rate is not even fixed: moving the zero of energy by c (ML's own choice, E0 = 0) changes the phase's
     frequency and changes nothing observable -- |S|, every <O>, the density matrix.  So the oscillation in a ground
     state is of its phase and its non-energy observables' spread, never of its energy.
  G3 NO ISOLATED STATE'S ENERGY OSCILLATES (computed).  For ML's achieving state, eq. (10), <H>(t) = E at every t, and
     the weights |c_n|^2 are constant; what oscillates is S(t), between 1 and 0.  This is Ehrenfest's d<H>/dt = 0 for a
     time-independent H (standard, not READ).
  G4 WHAT THE WRITE UNDER 163 NEEDS (computed, from ML eqs. (4)-(5)).  A write of T >= 2.0e5 clocks (o3_write.py, which
     163 keeps) needs, by eq. (5), an energy spread Delta E >= h/(4T), and by eq. (4) an average above the ground of no
     more than that.  With E = the README's energy, h/(4E) = (2 pi^2/ln 2)/N clocks (o3_atonce.py), so
        Delta E / E >= (2 pi^2/ln 2)/(N T) = 5.2e-20 at the example README.
     The state that reaches eq. (5) exactly, (|E - d> + |E + d>)/sqrt 2 with d = h/(4T), has average energy exactly E and
     turns orthogonal at exactly T (computed); its two branches differ in radius by 2m d/E = 1.3e-12 Planck lengths.
     At T = 2.0e5 clocks the write lasts 1.3e-31 s, about 2.5e12 Planck times: inside the physics used, where the
     instant hold (6.9e-51 s) was not.
  VERDICT (deduced).  On 164: the ground state oscillates in its phase and in the spread of its position, and those are
     what "oscillating state" can mean; its energy does not oscillate (G2), and no isolated state's does (G3).  ML's
     p.9 stands.  But the conflict the board reported was the instant reading's: an orthogonal step in h/(4E) needs
     Delta E = E.  Under 163 the write lasts >= 2.0e5 clocks and needs Delta E/E of only 5.2e-20 (G4), so 133's one exact
     energy holds to 5.2e-20 and 162's fixed size to 1.3e-12 Planck lengths.  The conflict is withdrawn, not by
     reading the energy as oscillating, but because the whole write needs almost no spread.  The board reads 164's
     "oscillating state" for the corridor as this: the corridor holding the README is a near-eigenstate whose energy is
     exact to 5.2e-20 and whose phase rotates (H-NEAR-EIGENSTATE, the board's).

Imports lemmas/o3_write.py by path.  Stdlib + sympy.  python3 o3_ground.py [--selftest]
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
CLOCK_PER_SQRT_BIT_S = 6.67430e-11 * 459404002.42356986 / 299792458.0**5   # G E/c^5 per sqrt(bit), as o3_atonce.py
PLANCK_TIME_S = 5.391247e-44                                               # CODATA 2018


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


r, x, t, c = sp.symbols("r x t c", real=True)
rp = sp.Symbol("r", positive=True)


def hydrogen_1s():
    """Atomic units: H = -(1/2) laplacian - 1/r on the s-wave; psi = e^(-r)/sqrt(pi)."""
    psi = sp.exp(-rp) / sp.sqrt(sp.pi)
    Hpsi = -sp.Rational(1, 2) * (sp.diff(psi, rp, 2) + 2 / rp * sp.diff(psi, rp)) - psi / rp
    E0 = sp.simplify(Hpsi / psi)
    w = 4 * sp.pi * rp**2
    mean = lambda f: sp.integrate(w * psi**2 * f, (rp, 0, sp.oo))
    H2 = sp.integrate(w * Hpsi**2, (rp, 0, sp.oo))
    return {"E0": E0, "norm": mean(1), "r": mean(rp), "r2": mean(rp**2), "varH": sp.simplify(H2 - mean(1) * E0**2)}


def oscillator():
    """Units hbar = m = omega = 1: H = -(1/2) d^2/dx^2 + x^2/2; psi = pi^(-1/4) e^(-x^2/2)."""
    psi = sp.pi ** sp.Rational(-1, 4) * sp.exp(-x**2 / 2)
    Hpsi = -sp.Rational(1, 2) * sp.diff(psi, x, 2) + x**2 / 2 * psi
    E0 = sp.simplify(Hpsi / psi)
    mean = lambda f: sp.integrate(psi**2 * f, (x, -sp.oo, sp.oo))
    return {"E0": E0, "x": mean(x), "x2": mean(x**2), "varH": sp.simplify(sp.integrate(Hpsi**2, (x, -sp.oo, sp.oo))
                                                                           - E0**2)}


def evolve_eigen(E0):
    """ML eq. (6) for one level: psi_t = e^(-i E0 t) psi.  Survival amplitude, its modulus, and the same with the zero
    of energy moved by c; the density matrix |psi_t><psi_t| = |psi><psi| (the phase cancels)."""
    S = sp.exp(-sp.I * E0 * t)
    Sc = sp.exp(-sp.I * (E0 + c) * t)
    rho_phase = sp.simplify(S * sp.conjugate(S))
    return {"S": S, "absS": sp.simplify(sp.Abs(S)), "absSc": sp.simplify(sp.Abs(Sc)), "rho_phase": rho_phase,
            "freq": sp.simplify(sp.I * sp.diff(S, t) / S), "freq_c": sp.simplify(sp.I * sp.diff(Sc, t) / Sc)}


def two_level(E1, E2, a2=sp.Rational(1, 2)):
    """sqrt(a2)|E1> + sqrt(1 - a2)|E2>: <H>(t), Delta E, S(t) (units hbar = 1)."""
    w1, w2 = a2, 1 - a2
    psi_t = [sp.sqrt(w1) * sp.exp(-sp.I * E1 * t), sp.sqrt(w2) * sp.exp(-sp.I * E2 * t)]      # ML eq. (6)
    H_t = sp.simplify(sum(sp.conjugate(a) * a * En for a, En in zip(psi_t, (E1, E2))))         # <psi_t|H|psi_t>
    S = sp.simplify(sum(sp.sqrt(w) * a for w, a in zip((w1, w2), psi_t)))                     # <psi_0|psi_t>
    varH = sp.simplify(sum(sp.conjugate(a) * a * En**2 for a, En in zip(psi_t, (E1, E2))) - H_t**2)
    return H_t, sp.sqrt(varH), S


def write_spread(T_clocks, n=EXAMPLE_N):
    """Delta E/E >= h/(4 E T) with h/(4E) = (2 pi^2/ln2)/N clocks; the MT state's radius split in Planck lengths."""
    hold = 2 * math.pi**2 / math.log(2) / n
    rel = hold / T_clocks
    m_planck = math.sqrt(n * math.log(2) / (4 * math.pi))     # m^2 = N ln2/(4 pi), Planck units (o3_atonce.py A1)
    seconds = T_clocks * CLOCK_PER_SQRT_BIT_S * math.sqrt(n)
    return {"hold": hold, "rel": rel, "split": 2 * m_planck * rel, "m_planck": m_planck, "seconds": seconds,
            "planck_times": seconds / PLANCK_TIME_S, "hold_seconds": hold * CLOCK_PER_SQRT_BIT_S * math.sqrt(n)}


def compute():
    ow = _load(os.path.join(HERE, "o3_write.py"), "o3g_o3write")
    T_gas = ow._num(ow.t_min(3))
    h1, ho = hydrogen_1s(), oscillator()
    ev = evolve_eigen(h1["E0"])
    E = sp.Symbol("E", positive=True)
    ml_H, ml_dE, ml_S = two_level(0, 2 * E)
    d = sp.Symbol("d", positive=True)
    mt_H, mt_dE, mt_S = two_level(E - d, E + d)
    return {"T_gas": T_gas, "h1": h1, "ho": ho, "ev": ev, "E": E, "d": d,
            "ml": (ml_H, ml_dE, sp.simplify(ml_S.subs(t, sp.pi / (2 * E)))),        # t = h/(4E), h = 2 pi
            "ml_back": sp.simplify(ml_S.subs(t, sp.pi / E)),
            "mt": (mt_H, mt_dE, sp.simplify(mt_S.subs(t, sp.pi / (2 * d)))),
            "spread": write_spread(T_gas)}


def report(d):
    h1, ho, ev, sp_ = d["h1"], d["ho"], d["ev"], d["spread"]
    print("o3_ground.py -- O3 under item 164: what oscillates in a ground state\n")
    print("G1 hydrogen 1s: E0 = %s, <r> = %s, <r^2> = %s, Delta r = %s; oscillator: E0 = %s, Delta x = %s" % (
        h1["E0"], h1["r"], h1["r2"], sp.sqrt(h1["r2"] - h1["r"]**2), ho["E0"], sp.sqrt(ho["x2"] - ho["x"]**2)))
    print("   psi_t = %s psi: the phase rotates at %s (with the zero moved by c: %s)" % (ev["S"], ev["freq"], ev["freq_c"]))
    print("G2 Var H: 1s %s, oscillator %s; |S(t)| = %s (zero moved: %s); the phase in rho: %s" % (
        h1["varH"], ho["varH"], ev["absS"], ev["absSc"], ev["rho_phase"]))
    ml_H, ml_dE, ml_S = d["ml"]
    print("G3 ML's state (|0> + |2E>)/sqrt 2: <H>(t) = %s for all t, Delta E = %s, S(h/4E) = %s, S(h/2E) = %s" % (
        ml_H, ml_dE, ml_S, d["ml_back"]))
    mt_H, mt_dE, mt_S = d["mt"]
    print("G4 Mandelstam-Tamm state (|E-d> + |E+d>)/sqrt 2: <H> = %s, Delta E = %s, S(h/4d) = %s" % (mt_H, mt_dE, mt_S))
    print("   write >= %.3g clocks (%.2g s, %.2g Planck times): Delta E/E >= %.2g; radius split %.2g Planck lengths "
          "(m = %.3g Planck lengths); the instant hold was %.2g s" % (d["T_gas"], sp_["seconds"], sp_["planck_times"],
                                                                     sp_["rel"], sp_["split"], sp_["m_planck"],
                                                                     sp_["hold_seconds"]))


def selftest():
    ok = n = 0

    def chk(name, cond):
        nonlocal ok, n
        n += 1
        ok += bool(cond)
        print("  [%s] %s" % ("ok" if cond else "FAIL", name))

    d = compute()
    h1, ho, ev, s = d["h1"], d["ho"], d["ev"], d["spread"]
    chk("G1: hydrogen 1s and the oscillator ground state solve H psi = E0 psi exactly (E0 = -1/2, 1/2); the position "
        "spread is nonzero (Delta r = sqrt(3)/2 a0, Delta x = 1/sqrt 2) -- control: the textbook values",
        h1["E0"] == -sp.Rational(1, 2) and ho["E0"] == sp.Rational(1, 2) and h1["norm"] == 1
        and sp.simplify(h1["r2"] - h1["r"]**2 - sp.Rational(3, 4)) == 0 and sp.simplify(ho["x2"] - ho["x"]**2 - sp.Rational(1, 2)) == 0)
    chk("G1: evolved, the ground state's phase rotates at E0 (and at E0 + c with the zero moved: the rate is not fixed)",
        sp.simplify(ev["freq"] - d["h1"]["E0"]) == 0 and sp.simplify(ev["freq_c"] - d["h1"]["E0"] - c) == 0)
    chk("G2: its energy does not oscillate -- Var H = 0 exactly in both ground states, |S(t)| = 1 for every t with "
        "either zero of energy, and the phase cancels in the density matrix (ML p.9: never orthogonal)",
        h1["varH"] == 0 and ho["varH"] == 0 and ev["absS"] == 1 and ev["absSc"] == 1 and ev["rho_phase"] == 1)
    ml_H, ml_dE, ml_S = d["ml"]
    chk("G3: ML's achieving state, evolved by eq. (6), has <psi_t|H|psi_t> = E with no t left in it and Delta E = E; S is 0 at h/(4E) and 1 again at h/(2E) "
        "(eqs. (10)-(11)) -- what oscillates is S, not the energy",
        sp.simplify(ml_H - d["E"]) == 0 and not ml_H.has(t) and sp.simplify(ml_dE - d["E"]) == 0 and ml_S == 0
        and d["ml_back"] == 1)
    mt_H, mt_dE, mt_S = d["mt"]
    chk("G4: the state (|E-d> + |E+d>)/sqrt 2 has average exactly E, spread d, and is orthogonal at h/(4d) (ML eq. (5) "
        "reached)", sp.simplify(mt_H - d["E"]) == 0 and sp.simplify(mt_dE - d["d"]) == 0 and mt_S == 0)
    chk("G4: under 163 the write's >= 2.0e5 clocks need Delta E/E >= 5.2e-20 at the example README; the radius split "
        "is ~1.3e-12 Planck lengths; control: at T = h/(4E) the bound is Delta E = E",
        1.9e5 < d["T_gas"] < 2.1e5 and 5.0e-20 < s["rel"] < 5.4e-20 and 1e-12 < s["split"] < 1.6e-12
        and abs(write_spread(s["hold"])["rel"] - 1) < 1e-12)
    chk("G4: the write lasts ~1.3e-31 s, about 2.5e12 Planck times -- inside the physics used; the instant hold was "
        "~7e-51 s, below a Planck time", 1.0e-31 < s["seconds"] < 1.6e-31 and s["planck_times"] > 1e12
        and s["hold_seconds"] < PLANCK_TIME_S)
    print("selftest: %d/%d" % (ok, n))
    return ok == n


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    report(compute())
