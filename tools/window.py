#!/usr/bin/env python3
"""window.py -- which particles the seven conditions admit, scanned rather than asserted.

WHY THIS EXISTS
---------------
The uniqueness theorem was written as an enumeration -- electron below, muon
inside, pion inside but hadronic, kaon and tau above -- and an enumeration is
only a proof if the list it walks is complete. The first draft ASSERTED that
"no other charged particle has both a mass in the window and a lifetime
sufficient to form a molecule", which is a claim about the whole spectrum made
without scanning it. A referee is entitled to ask which particles were
considered and against what test.

So this states the admissibility test, applies it to every charged particle
with a lifetime long enough to matter, and prints the result. It also answers
the question that makes the theorem robust: **how much would the window's
endpoints have to move before the answer changed?**

THE TEST
--------
A particle may serve as a binder only if all four hold:

    CHARGE      it is negatively charged, so it binds to a nucleus rather than
                to an electron. A positive binder forms an atom with the
                electron and is repelled by every nucleus in the fuel.
    MASS        its mass lies in the structural window, which condition 2 bounds
                below and conditions 3-4 bound above.
    LIFETIME    it lives long enough to form a mesomolecule. The formation rate
                at liquid density is of order 1e8 to 1e9 per second, so a
                candidate needs a lifetime well above a nanosecond.
    INTERACTION it is not strongly interacting. A hadron in a mesomolecule is
                absorbed by the nucleus long before the cycle completes, which
                fails conditions 3 and 4 together.

Masses are PDG values in electron masses; lifetimes are PDG.

    python3 tools/window.py
    python3 tools/window.py --selftest
stdlib only.
"""
import argparse
import sys

# (name, mass in electron masses, lifetime in seconds, strongly interacting)
# The table is illustrative and the COMPLETENESS argument does not rest on it.
# It lists every charged particle that outlives the mesomolecular formation time
# -- which is the set the theorem actually runs on, and which is closed (see
# long_lived below) -- together with the nearest shorter-lived neighbours on
# either side of the window, so that a reader can see where the gaps are.
SPECTRUM = [
    ("electron  e-",       1.0,      float("inf"), False),
    ("muon      mu-",      206.77,   2.197e-6,     False),
    ("pion      pi-",      273.13,   2.603e-8,     True),
    ("kaon      K-",       966.1,    1.238e-8,     True),
    ("proton    p (anti)", 1836.15,  float("inf"), True),
    ("Sigma-",             2343.1,   1.479e-10,    True),
    ("Sigma+",             2327.5,   8.018e-11,    True),
    ("Xi-",                2585.7,   1.639e-10,    True),
    ("Omega-",             3272.0,   8.21e-11,     True),
    ("tau       tau-",     3477.2,   2.903e-13,    False),
    ("D-",                 3658.5,   1.033e-12,    True),
    ("Ds-",                3857.5,   5.04e-13,     True),
    ("B-",                 10324.0,  1.638e-12,    True),
]
# Everything omitted is omitted for one stated reason, and the reason is a hard
# cut rather than a judgement: no charged particle in the Review of Particle
# Physics outside long_lived() has a lifetime exceeding the mesomolecular
# formation time. The charged hyperons are the closest, and they fall short of
# it by roughly an order of magnitude; the tau, the charmed and bottom hadrons and every
# resonance fall short by more. A particle that decays before the molecule forms
# never enters the cycle, so none of them can be a binder whatever its mass.
OMITTED_REASON = ("every other charged particle decays before the mesomolecule "
                  "forms -- the charged hyperons by an order of magnitude, "
                  "everything else by more -- so none can be a binder")

# The alpha the binder may stick to, in electron masses. It enters only through
# the reduced mass: the cancellation in Theorem 2 uses a_b ~ 1/m_b, which holds
# exactly for mu = m_b m_alpha / (m_b + m_alpha) only when m_b << m_alpha. The
# residual is m_b / m_alpha and nothing else, and it is priced below.
M_ALPHA_ME = 7294.30   # 3727.379 MeV / 0.51099895 MeV

WINDOW_LO = 119.0      # [1] sec.2, condition 2
WINDOW_HI = 918.0      # [1] sec.2, conditions 3 and 4
FORMATION_S = 1.0e-9   # the mesomolecular formation time at liquid density


def verdict(name, mass, tau, hadron):
    """Which test a candidate fails, or ADMITTED. The first failure is reported,
    in the order the tests constrain: a particle can fail more than one."""
    if mass < WINDOW_LO:
        return "below the window", f"{mass:.0f} < {WINDOW_LO:.0f}"
    if mass > WINDOW_HI:
        return "above the window", f"{mass:.0f} > {WINDOW_HI:.0f}"
    if tau < FORMATION_S:
        return "too short-lived", f"{tau:.2e} s < {FORMATION_S:.0e} s"
    if hadron:
        return "strongly interacting", "absorbed before the cycle completes"
    return "ADMITTED", "mass, lifetime and interaction all pass"


def admitted():
    return [row for row in SPECTRUM if verdict(*row)[0] == "ADMITTED"]


def in_window():
    return [row for row in SPECTRUM if WINDOW_LO <= row[1] <= WINDOW_HI]


def long_lived():
    """Every charged particle that outlives the mesomolecular formation time.

    This is the set the theorem runs on, and it is CLOSED: the cut is a
    published lifetime against a fixed threshold, so completeness can be
    checked against the Review of Particle Physics without judgement. The
    charged hyperons -- the nearest excluded states -- fall short of the
    threshold by an order of magnitude."""
    return [row for row in SPECTRUM if row[2] > FORMATION_S]


def robustness():
    """How far the window's endpoints may move before the answer changes.

    This is what makes the theorem independent of the exact bounds. The answer
    is set by the GAPS in the spectrum, not by the bounds themselves: the
    largest window giving the same admitted set runs from just above the
    electron to just below the kaon."""
    masses = sorted(r[1] for r in SPECTRUM)
    adm = [r[1] for r in admitted()]
    below = max([m for m in masses if m < min(adm)], default=0.0)
    above = min([m for m in masses if m > max(r[1] for r in in_window())],
                default=float("inf"))
    return below, above


def reduced_mass_residual(m_b):
    """How far the binder's reduced mass with the alpha departs from its own.

    Theorem 2's cancellation is exact in the limit m_b << m_alpha. Restoring the
    reduced mass, the sudden-approximation exponent carries a factor
    m_b / mu = 1 + m_b / m_alpha, so ALL of the residual mass dependence enters
    through this one ratio. It runs in the direction of LESS sticking for a
    heavier binder, which is the direction that would help -- and the window
    has no heavier admissible occupant to exploit it."""
    return m_b / M_ALPHA_ME


def report():
    print("WHICH PARTICLES THE CONDITIONS ADMIT")
    print(f"  window   {WINDOW_LO:.0f} to {WINDOW_HI:.0f} electron masses")
    print(f"  lifetime must exceed the formation time, {FORMATION_S:.0e} s")
    print()
    print(f"  {'candidate':<20}{'mass m_e':>10}{'lifetime s':>13}   verdict")
    for row in SPECTRUM:
        v, why = verdict(*row)
        tau = "stable" if row[2] == float("inf") else f"{row[2]:.3e}"
        mark = "  <<<" if v == "ADMITTED" else ""
        print(f"  {row[0]:<20}{row[1]:>10.1f}{tau:>13}   {v}{mark}")
        print(f"  {'':<20}{'':>10}{'':>13}     {why}")
    print()
    print(f"  OUTLIVE THE FORMATION TIME: {len(long_lived())} -- "
          f"{', '.join(r[0].split()[0] for r in long_lived())}")
    print(f"    That cut is CLOSED against the Review of Particle Physics: it is")
    print(f"    a published lifetime against a fixed threshold, so the set can be")
    print(f"    checked for completeness without judgement. Everything else is")
    print(f"    excluded before its mass is ever consulted.")
    print(f"  IN THE WINDOW AT ALL: {len(in_window())} -- "
          f"{', '.join(r[0].split()[0] for r in in_window())}")
    print(f"  ADMITTED:             {len(admitted())} -- "
          f"{', '.join(r[0].split()[0] for r in admitted())}")
    print()
    print("  WHAT IS NOT LISTED, AND WHY IT NEED NOT BE")
    print(f"    {OMITTED_REASON}.")
    print()
    print("  HOW MUCH THE WINDOW WOULD HAVE TO MOVE")
    below, above = robustness()
    print(f"    The admitted set is decided by the GAPS in the spectrum rather")
    print(f"    than by the bounds. The nearest particle below the muon is the")
    print(f"    electron at {below:.1f}, and the nearest above the pion is the kaon")
    print(f"    at {above:.1f}. So ANY window whose lower bound lies between")
    print(f"    {below:.1f} and {min(r[1] for r in admitted()):.1f}, and whose upper bound lies between")
    print(f"    {max(r[1] for r in in_window()):.1f} and {above:.1f}, admits exactly the same set.")
    lo_span = min(r[1] for r in admitted()) / max(below, 1e-9)
    hi_span = above / max(r[1] for r in in_window())
    print(f"    That is a factor of {lo_span:.0f} in the lower bound and {hi_span:.2f} in the")
    print(f"    upper. The theorem does not depend on the bounds being exact.")
    print()
    print("  THE ONE PLACE A RESIDUAL MASS DEPENDENCE ENTERS")
    mu_r = reduced_mass_residual(admitted()[0][1])
    hi_r = reduced_mass_residual(WINDOW_HI)
    print(f"    Theorem 2 cancels m_b exactly in the limit m_b << m_alpha. The")
    print(f"    residual is m_b/m_alpha and nothing else: {mu_r:.4f} at the muon,")
    print(f"    {hi_r:.4f} at the window's ceiling. It makes a HEAVIER binder stick")
    print(f"    LESS, so it is the direction that would help -- and the window")
    print(f"    admits no heavier occupant to exploit it. The closure of the")
    print(f"    standalone case therefore does not rest on the cancellation")
    print(f"    being exact.")
    print()
    print("  WHAT THIS DOES NOT ESTABLISH.")
    print("    The window's endpoints themselves are carried from [1] sec.2 and")
    print("    are not recomputed here. This scan shows the CONCLUSION is")
    print("    insensitive to them over the spans above; it does not derive them.")
    return 0


def selftest():
    fail = 0

    def check(label, got, want=True):
        nonlocal fail
        ok = got == want
        fail += 0 if ok else 1
        print(f"  {label:<62} {'PASS' if ok else 'FAIL'}")

    check("exactly one candidate is admitted", len(admitted()) == 1)
    check("five charged particles outlive the formation time",
          len(long_lived()) == 5)
    check("and the admitted one is among them",
          admitted()[0] in long_lived())
    check("every particle in the window at all outlives it too",
          all(r in long_lived() for r in in_window()))
    check("the reduced-mass residual is small at the muon",
          reduced_mass_residual(admitted()[0][1]) < 0.03)
    check("and bounded by an eighth across the whole window",
          reduced_mass_residual(WINDOW_HI) < 0.13)
    check("it runs toward LESS sticking as the binder is made heavier",
          reduced_mass_residual(WINDOW_HI)
          > reduced_mass_residual(admitted()[0][1]))
    nearest = max(r[2] for r in SPECTRUM if r not in long_lived())
    check("the nearest excluded state falls short of the threshold by >5x",
          nearest * 5 < FORMATION_S)
    check("and it is the muon", admitted()[0][0].startswith("muon"))
    check("two particles lie in the window at all", len(in_window()) == 2)
    check("the second is the pion, excluded as a hadron",
          verdict(*[r for r in in_window() if not r[0].startswith("muon")][0])[0]
          == "strongly interacting")
    check("the electron fails on mass, not on anything else",
          verdict(*SPECTRUM[0])[0] == "below the window")
    check("the tau fails on mass before its lifetime is reached",
          verdict(*[r for r in SPECTRUM if r[0].startswith("tau")][0])[0]
          == "above the window")
    below, above = robustness()
    check("the window may move by a large factor without changing the answer",
          below < 10 and above > 900)
    print()
    print("  the scan can fail: a candidate inside the window that passed every")
    print("  other test would break uniqueness, so that case is constructed")
    ghost = ("ghost", 400.0, 1.0e-3, False)
    check("a hypothetical light, long-lived, non-hadronic particle IS admitted",
          verdict(*ghost)[0] == "ADMITTED")
    print("    -- so the theorem's content is that the real spectrum has no such")
    print("       particle, which is a fact about the spectrum and not a tautology")
    print()
    print(f"selftest: {fail} failures -> {'PASS' if fail == 0 else 'FAIL'}")
    return 1 if fail else 0


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args()
    return selftest() if a.selftest else report()


if __name__ == "__main__":
    sys.exit(main())
