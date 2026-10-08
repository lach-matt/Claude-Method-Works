#!/usr/bin/env python3
"""o3_ground.py -- Warp Theorem lemma O3, M-RULINGS item 164: what oscillates in a ground state, and what the write under
item 163 needs of the corridor's energy.  Computed, READ and deduced; verified once (findings applied, O3-GROUND.md
History); not seated.  First headed "... not verified; not seated" -- and first concluding "the conflict is withdrawn"
with the oscillating-back objection unanswered, which its verifier showed was not earned.

M's words (verbatim in the rulings file): item 164 "The ground state of any atom is an oscillating state. Thus its
energy oscillates as well" (answering the board's "Achievability conflicts with your rulings. Margolus–Levitin's
achieving state needs an energy spread, a level at 2E, and it oscillates back."); item 133 "There is only one exact
energy needed for any given README"; item 162 "The throat doesn't change size"; item 163 "All together, one whole"
(chosen against the option text "held as a single whole, not bit by bit"); item 115 (c) "The README itself".

READ  Margolus & Levitin, quant-ph/9710043 (re-read in full 2026-10-08): §2's opening, footnote 2, and §2.1, "we will
      choose our zero of energy so that E0 = 0"; eq. (4), tau >= h/(4E), E the average energy above the ground state,
      and eq. (5), the earlier bound tau >= h/(4 Delta E) (Mandelstam-Tamm, their ref. [10]), p.4; eq. (6), |psi_t> =
      sum_n c_n e^(-i E_n t/hbar) |E_n>, and eq. (7), S(t) = sum |c_n|^2 e^(-i E_n t/hbar); eqs. (10)-(11), the
      achieving state, "For these states, ∆E = E"; p.9 (by the paper's order), "an isolated stationary atom in an exact
      energy eigenstate never transitions to an orthogonal state, but if we view this same atom from a moving frame we
      will see a sequence of distinct position states".

  G1 WHAT OSCILLATES -- AND FLUCTUATES -- IN A GROUND STATE (computed).  Hydrogen's 1s and the oscillator's ground state
     solve H psi = E0 psi exactly; by eq. (6) each evolves to e^(-i E0 t/hbar) psi: the phase turns.  The position keeps
     a spread (1s: Delta r = (sqrt 3/2) a0; oscillator: Delta x = 1/sqrt 2), and so do the two halves of the energy:
     kinetic T and potential V each fluctuate, exactly anticorrelated -- oscillator Var T = Var V = 1/8, Cov = -1/8; 1s
     Var T = Var V = 1 hartree^2 (Delta T = Delta V = 2|E0|), Cov = -1.  This is the strongest reading under which "its
     energy oscillates" is literally so: its kinetic and potential energy fluctuate.  (Every ground state does this --
     Heisenberg, standard, not READ; the QED vacuum's field-energy fluctuations in a subregion likewise, with the
     dressed ground state still an eigenstate of the full H -- standard, not READ.)
  G2 ITS TOTAL ENERGY DOES NOT (computed; deduced for the time-independence).  Var(T + V) = Var H = 0 exactly; the
     survival amplitude has |S(t)| = 1 (an identity for one level) -- never orthogonal, ML p.9.  The distributions of
     T, V, r are those of |psi|^2, which the phase leaves fixed: constant in t (deduced).  "Fluctuates", not
     "oscillates".  The phase's rate: in non-relativistic QM it moves with the zero of energy (ML's own E0 = 0) and
     nothing observable moves with it; with gravity the zero is fixed (energy gravitates; ML §3 uses the total
     relativistic energy) and the corridor's phase turns at E/h = 2.4e13 cycles per clock (standard, de Broglie/Compton,
     not READ) -- ML's h/(4E) is exactly a quarter of that period.  Still a phase: it alone makes no orthogonal state.
  G3 NO ISOLATED STATE'S ENERGY OSCILLATES (computed for ML's state; in general Ehrenfest, d<H>/dt = 0 for a fixed H,
     standard, not READ).  ML's achieving state, evolved by eq. (6), has <H> = E with no t left in it; what oscillates
     is S, between 1 and 0.
  G4 WHAT THE WRITE UNDER 163 NEEDS (computed, from ML eqs. (4)-(5)).  163 chose the write as one whole: one orthogonal
     step (H-WRITE-ONE-ORTHOGONAL-STEP), of the closed system corridor plus inflow (H-WRITE-CLOSED-SYSTEM -- under
     115 (c) the corridor alone is not isolated while the README flows in).  It lasts T >= 1.997e5 clocks (o3_write.py).
     Eq. (5) needs Delta E >= h/(4T); eq. (4) needs E >= h/(4T), which E exceeds by ~2e19.  With h/(4E) = (2 pi^2/ln2)/N
     clocks,
        Delta E / E >= (2 pi^2/ln2)/(N T) = 5.2e-20 at the example README;
     if the size tracks the energy (r = 2 G E/c^4 per branch, H-SIZE-TRACKS-ENERGY), the radius's spread is 2m Delta E/E
     = 1.3e-12 Planck lengths.  Sensitivity: written bit by bit -- N orthogonal steps, which 163 declined -- the bound
     per step gives Delta E/E >= 1.4e-4, a radius spread of 3.5e3 Planck lengths.  The write's duration, 1.3e-31 s
     (2.5e12 Planck times), is above the Planck time; the size figure is not, and ML's non-relativistic,
     fixed-background setting is still assumed for a horizon-sized object.
  G5 THE HELD README DOES NOT OSCILLATE BACK (computed; deduced from 133).  By 133 and the board's E(N), the energy
     depends on N only, never on the README's content: all 2^N READMEs of N bits share E -- the register is degenerate
     (H-DEGENERATE-REGISTER, deduced; it is also what an entropy of N bits at one energy counts).  So the write is a
     coupling V between the state before, |a>, and the README, |b>, at the one energy E, on for T and then off
     (H = E + V(t); V = v(|a><b| + |b><a|), v = h/(4T) -- the inflow's coupling, under H-WRITE-CLOSED-SYSTEM):
       * <H> = E exactly at every t (<V> = 0): the energy is the one exact E throughout;
       * Delta E = v = h/(4T) while V is on -- eq. (5) reached; 0 before and after;
       * at T the state is |b> (|<b|psi_T>| = 1), and after V ends it stays |b> for all t: held, not oscillating back;
       * no level at 2E is used: the levels are E +- v;
       * control: with V left on the state returns to |a> at 2T -- the oscillating back is the coupling's, not the
         register's.
  VERDICT (deduced).  On 164: a ground state oscillates in its phase and fluctuates in its position and in its kinetic
     and potential energy (G1); its total energy neither oscillates nor fluctuates (G2), and no isolated state's does
     (G3); ML's p.9 stands.  The board's three objections -- a spread, a level at 2E, oscillating back -- belonged to
     the instant reading.  Under 163, with H-WRITE-ONE-ORTHOGONAL-STEP, H-WRITE-CLOSED-SYSTEM and H-DEGENERATE-REGISTER,
     they are answered: the held README is an exact eigenstate at E (133 exactly); during the write the average energy
     is exactly E and the spread 5.2e-20 of it, carried by the inflow's coupling; no level at 2E; nothing oscillates
     back once the coupling ends.  The reading in which 133 forbids any spread at any moment cannot stand with the
     rulings: by eq. (5) a state with no spread never changes, so the README could never be written (115 (c), 163) --
     the rulings decide against it.  The board reads 164's "oscillating state" as G1 and G5 together: the held
     corridor's phase turns and its parts fluctuate, its energy is exact (H-HELD-EIGENSTATE, the board's).

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


x, t, c = sp.symbols("x t c", real=True)
rp = sp.Symbol("r", positive=True)


# ------------------------------------------------------------------------------------------------ G1-G2 ground states
def hydrogen_1s():
    """Atomic units: H = T + V, T = -(1/2) laplacian on the s-wave, V = -1/r; psi = e^(-r)/sqrt(pi)."""
    psi = sp.exp(-rp) / sp.sqrt(sp.pi)
    Tpsi = -sp.Rational(1, 2) * (sp.diff(psi, rp, 2) + 2 / rp * sp.diff(psi, rp))
    Vpsi = -psi / rp
    w = 4 * sp.pi * rp**2
    ip = lambda f, g: sp.integrate(w * f * g, (rp, 0, sp.oo))            # real wavefunctions
    E0 = sp.simplify((Tpsi + Vpsi) / psi)
    T1, V1 = ip(psi, Tpsi), ip(psi, Vpsi)
    varT, varV = ip(Tpsi, Tpsi) - T1**2, ip(Vpsi, Vpsi) - V1**2
    cov = ip(Tpsi, Vpsi) - T1 * V1
    return {"E0": E0, "norm": ip(psi, psi), "r": ip(psi, rp * psi), "r2": ip(psi, rp**2 * psi),
            "varT": sp.simplify(varT), "varV": sp.simplify(varV), "cov": sp.simplify(cov),
            "varH": sp.simplify(varT + varV + 2 * cov), "varH_direct": sp.simplify(ip(Tpsi + Vpsi, Tpsi + Vpsi) - E0**2)}


def oscillator():
    """Units hbar = m = omega = 1: H = T + V, T = -(1/2) d^2/dx^2, V = x^2/2; psi = pi^(-1/4) e^(-x^2/2)."""
    psi = sp.pi ** sp.Rational(-1, 4) * sp.exp(-x**2 / 2)
    Tpsi = -sp.Rational(1, 2) * sp.diff(psi, x, 2)
    Vpsi = x**2 / 2 * psi
    ip = lambda f, g: sp.integrate(f * g, (x, -sp.oo, sp.oo))
    E0 = sp.simplify((Tpsi + Vpsi) / psi)
    T1, V1 = ip(psi, Tpsi), ip(psi, Vpsi)
    varT, varV = ip(Tpsi, Tpsi) - T1**2, ip(Vpsi, Vpsi) - V1**2
    cov = ip(Tpsi, Vpsi) - T1 * V1
    return {"E0": E0, "x": ip(psi, x * psi), "x2": ip(psi, x**2 * psi), "varT": sp.simplify(varT),
            "varV": sp.simplify(varV), "cov": sp.simplify(cov), "varH": sp.simplify(varT + varV + 2 * cov)}


def evolve_eigen(E0):
    """ML eq. (6) for one level: psi_t = e^(-i E0 t) psi.  Its phase rate, and the same with the zero moved by c.
    |S| = 1 and the cancelling phase are identities for one level, reported, not tested."""
    S = sp.exp(-sp.I * E0 * t)
    Sc = sp.exp(-sp.I * (E0 + c) * t)
    return {"S": S, "absS": sp.simplify(sp.Abs(S)), "freq": sp.simplify(sp.I * sp.diff(S, t) / S),
            "freq_c": sp.simplify(sp.I * sp.diff(Sc, t) / Sc)}


# ------------------------------------------------------------------------------------------------ G3-G4 two levels
def two_level(E1, E2, a2=sp.Rational(1, 2)):
    """sqrt(a2)|E1> + sqrt(1 - a2)|E2>, evolved by ML eq. (6): <H>(t), Delta E, S(t) (units hbar = 1)."""
    w1, w2 = a2, 1 - a2
    psi_t = [sp.sqrt(w1) * sp.exp(-sp.I * E1 * t), sp.sqrt(w2) * sp.exp(-sp.I * E2 * t)]
    H_t = sp.simplify(sum(sp.conjugate(a) * a * En for a, En in zip(psi_t, (E1, E2))))
    S = sp.simplify(sum(sp.sqrt(w) * a for w, a in zip((w1, w2), psi_t)))
    varH = sp.simplify(sum(sp.conjugate(a) * a * En**2 for a, En in zip(psi_t, (E1, E2))) - H_t**2)
    return H_t, sp.sqrt(varH), S


def write_spread(T_clocks, n=EXAMPLE_N, steps=1):
    """Delta E/E >= steps * h/(4 E T), h/(4E) = (2 pi^2/ln2)/N clocks; the radius's spread 2m Delta E/E (Planck)."""
    hold = 2 * math.pi**2 / math.log(2) / n
    rel = steps * hold / T_clocks
    m_planck = math.sqrt(n * math.log(2) / (4 * math.pi))     # m^2 = N ln2/(4 pi), Planck units (o3_atonce.py A1)
    seconds = T_clocks * CLOCK_PER_SQRT_BIT_S * math.sqrt(n)
    return {"hold": hold, "rel": rel, "dr": 2 * m_planck * rel, "m_planck": m_planck, "seconds": seconds,
            "planck_times": seconds / PLANCK_TIME_S, "hold_seconds": hold * CLOCK_PER_SQRT_BIT_S * math.sqrt(n),
            "phase_per_clock": 1 / (4 * hold), "e_over_floor": T_clocks / hold}


# ------------------------------------------------------------------------------------------------ G5 the held README
def held_write():
    """Degenerate register {|a>, |b>} at energy E; H = E + V, V = v (|a><b| + |b><a|) on for 0 < t < T, v = pi/(2T)
    (h/(4T) with hbar = 1), then off.  Exact evolution in the {a, b} basis."""
    E, T = sp.symbols("E T", positive=True)
    v = sp.pi / (2 * T)
    Hm = sp.Matrix([[E, v], [v, E]])
    U = lambda s: sp.simplify((-sp.I * Hm * s).exp())
    psi0 = sp.Matrix([1, 0])
    psi = lambda s: sp.simplify(U(s) * psi0)                       # while V is on
    meanH = sp.simplify((psi(t).H * Hm * psi(t))[0])
    varH = sp.simplify((psi(t).H * Hm * Hm * psi(t))[0] - meanH**2)
    psiT = psi(T)
    after = sp.simplify(sp.exp(-sp.I * E * t) * psiT)              # V off: H = E on the register
    Hoff = sp.diag(E, E)
    return {"E": E, "T": T, "v": v, "meanH": meanH, "varH": varH, "onb": sp.simplify(sp.Abs(psiT[1])),
            "ona": sp.simplify(sp.Abs(psiT[0])), "held": sp.simplify(sp.Abs(after[1])),
            "varH_after": sp.simplify((after.H * Hoff * Hoff * after)[0] - ((after.H * Hoff * after)[0])**2),
            "back": sp.simplify(sp.Abs(psi(2 * T)[0])), "levels": sorted(Hm.eigenvals().keys(), key=str)}


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
            "mt_is_ml": sp.simplify(mt_S.subs(d, E).subs(t, sp.pi / (2 * E))),        # d = E: ML's own state
            "spread": write_spread(T_gas), "bitwise": write_spread(T_gas, steps=EXAMPLE_N), "held": held_write()}


def report(d):
    h1, ho, ev, s, b, hw = d["h1"], d["ho"], d["ev"], d["spread"], d["bitwise"], d["held"]
    print("o3_ground.py -- O3 under item 164: what oscillates in a ground state\n")
    print("G1 hydrogen 1s: E0 = %s, Delta r = %s; Var T = %s, Var V = %s, Cov = %s" % (
        h1["E0"], sp.sqrt(h1["r2"] - h1["r"]**2), h1["varT"], h1["varV"], h1["cov"]))
    print("   oscillator: E0 = %s, Delta x = %s; Var T = %s, Var V = %s, Cov = %s" % (
        ho["E0"], sp.sqrt(ho["x2"] - ho["x"]**2), ho["varT"], ho["varV"], ho["cov"]))
    print("   psi_t = %s psi: the phase turns at %s (zero moved by c: %s)" % (ev["S"], ev["freq"], ev["freq_c"]))
    print("G2 Var H = Var T + Var V + 2 Cov: 1s %s (directly %s), oscillator %s; |S(t)| = %s" % (
        h1["varH"], h1["varH_direct"], ho["varH"], ev["absS"]))
    print("   with gravity's fixed zero the corridor's phase turns at E/h = %.3g per clock" % s["phase_per_clock"])
    ml_H, ml_dE, ml_S = d["ml"]
    print("G3 ML's state: <H>(t) = %s, Delta E = %s, S(h/4E) = %s, S(h/2E) = %s" % (ml_H, ml_dE, ml_S, d["ml_back"]))
    mt_H, mt_dE, mt_S = d["mt"]
    print("G4 (|E-d> + |E+d>)/sqrt 2: <H> = %s, Delta E = %s, S(h/4d) = %s" % (mt_H, mt_dE, mt_S))
    print("   write >= %.4g clocks (%.2g s, %.2g Planck times): Delta E/E >= %.3g, radius spread %.2g Planck lengths "
          "(m = %.3g); E exceeds eq. (4)'s h/(4T) by %.2g" % (d["T_gas"], s["seconds"], s["planck_times"], s["rel"],
                                                            s["dr"], s["m_planck"], s["e_over_floor"]))
    print("   bit by bit (declined by 163): Delta E/E >= %.2g, radius spread %.2g Planck lengths" % (b["rel"], b["dr"]))
    print("G5 held write: <H> = %s, Var H while on = %s, after = %s; |<b|psi_T>| = %s, held after = %s; levels %s; "
          "left on, |<a|psi_2T>| = %s" % (hw["meanH"], hw["varH"], hw["varH_after"], hw["onb"], hw["held"],
                                           hw["levels"], hw["back"]))


def selftest():
    ok = n = 0

    def chk(name, cond):
        nonlocal ok, n
        n += 1
        ok += bool(cond)
        print("  [%s] %s" % ("ok" if cond else "FAIL", name))

    d = compute()
    h1, ho, ev, s, b, hw = d["h1"], d["ho"], d["ev"], d["spread"], d["bitwise"], d["held"]
    chk("G1: hydrogen 1s and the oscillator ground state solve H psi = E0 psi exactly (E0 = -1/2, 1/2); position "
        "spreads Delta r = sqrt(3)/2 a0, Delta x = 1/sqrt 2 -- control: the textbook values",
        h1["E0"] == -sp.Rational(1, 2) and ho["E0"] == sp.Rational(1, 2) and h1["norm"] == 1
        and sp.simplify(h1["r2"] - h1["r"]**2 - sp.Rational(3, 4)) == 0
        and sp.simplify(ho["x2"] - ho["x"]**2 - sp.Rational(1, 2)) == 0)
    chk("G1: kinetic and potential energy each fluctuate in the ground state -- oscillator Var T = Var V = 1/8, "
        "Cov = -1/8; 1s Var T = Var V = 1, Cov = -1 (exactly anticorrelated)",
        ho["varT"] == sp.Rational(1, 8) and ho["varV"] == sp.Rational(1, 8) and ho["cov"] == -sp.Rational(1, 8)
        and h1["varT"] == 1 and h1["varV"] == 1 and h1["cov"] == -1)
    chk("G2: the total does not -- Var H = 0 in both, and for 1s computed two independent ways (from T, V and Cov; and "
        "as ||H psi||^2 - E0^2)", h1["varH"] == 0 and h1["varH_direct"] == 0 and ho["varH"] == 0)
    chk("G2: the phase turns at E0, and at E0 + c with the zero moved (non-relativistic QM); with gravity's fixed zero "
        "the corridor's at E/h ~ 2.4e13 per clock, h/(4E) a quarter period",
        sp.simplify(ev["freq"] - h1["E0"]) == 0 and sp.simplify(ev["freq_c"] - h1["E0"] - c) == 0
        and 2.3e13 < s["phase_per_clock"] < 2.5e13 and abs(s["phase_per_clock"] * 4 * s["hold"] - 1) < 1e-12)
    ml_H, ml_dE, ml_S = d["ml"]
    chk("G3: ML's achieving state, evolved by eq. (6), has <psi_t|H|psi_t> = E with no t left and Delta E = E; S is 0 "
        "at h/(4E) and 1 again at h/(2E) (eqs. (10)-(11))",
        sp.simplify(ml_H - d["E"]) == 0 and not ml_H.has(t) and sp.simplify(ml_dE - d["E"]) == 0 and ml_S == 0
        and d["ml_back"] == 1)
    mt_H, mt_dE, mt_S = d["mt"]
    chk("G4: (|E-d> + |E+d>)/sqrt 2 has average exactly E, spread d, orthogonal at h/(4d) (eq. (5) reached); control: "
        "at d = E it is ML's state, orthogonal at h/(4E)",
        sp.simplify(mt_H - d["E"]) == 0 and sp.simplify(mt_dE - d["d"]) == 0 and mt_S == 0 and d["mt_is_ml"] == 0)
    chk("G4: the write's 1.997e5 clocks need Delta E/E >= 5.2e-20 (radius spread 1.3e-12 Planck lengths) and E is "
        "~2e19 above eq. (4)'s need; bit by bit it would be 1.4e-4 (3.5e3 Planck lengths)",
        1.99e5 < d["T_gas"] < 2.0e5 and 5.1e-20 < s["rel"] < 5.3e-20 and 1.2e-12 < s["dr"] < 1.4e-12
        and 1.8e19 < s["e_over_floor"] < 2.0e19 and 1.3e-4 < b["rel"] < 1.5e-4 and 3e3 < b["dr"] < 4e3)
    chk("G4: the write lasts ~1.3e-31 s, ~2.5e12 Planck times; the instant hold was ~7e-51 s, below one",
        1.0e-31 < s["seconds"] < 1.6e-31 and s["planck_times"] > 1e12 and s["hold_seconds"] < PLANCK_TIME_S)
    chk("G5: a write on a degenerate register by a coupling on for T -- <H> = E exactly throughout, Delta E = h/(4T) "
        "while on and 0 after, the README reached at T and held after; levels E +- v, none at 2E; control: left on, "
        "it is back at |a> at 2T",
        sp.simplify(hw["meanH"] - hw["E"]) == 0 and sp.simplify(sp.sqrt(hw["varH"]) - hw["v"]) == 0
        and hw["varH_after"] == 0 and hw["onb"] == 1 and hw["ona"] == 0 and hw["held"] == 1 and hw["back"] == 1
        and all(sp.simplify(l - hw["E"]) in (hw["v"], -hw["v"]) for l in hw["levels"]))
    print("selftest: %d/%d" % (ok, n))
    return ok == n


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    report(compute())
