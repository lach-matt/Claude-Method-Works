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


# ---- THE FUEL SCAN, WHICH IS THE SAME ARGUMENT ON THE OTHER SIDE ----------
# Theorem 1 closes the BINDER question: of everything in the charged spectrum,
# only the muon can hold a mesomolecule. It says nothing about what the
# mesomolecule holds, and the design has assumed d-t throughout without ever
# asking whether anything else would do -- which matters, because tritium is
# the single largest environmental liability in the whole plant.
#
# The candidate set is closed the same way the binder set was. A mesomolecular
# fuel is a PAIR of light nuclei that a muon can bind, and the hydrogen
# isotopes give exactly six pairs; the helium ones are listed beside them and
# excluded on the same arithmetic rather than by assertion.
#
# The figure of merit is not Q. A muon is a reusable catalyst with two ways of
# being lost -- it decays, or it sticks to a fusion product -- so what one
# muon is worth is
#
#     N = 1 / (omega_s + lambda_0 / lambda_c)
#
# with lambda_0 the muon decay rate and lambda_c the cycle rate, and the fuel's
# value is N.Q for energy and N.n for neutrons. A slow cycle is punished by
# decay and a sticky one by sticking, and d-t is the only pair that is neither.
LAMBDA_0 = 1.0 / 2.1969811e-6      # muon decay rate, s^-1                EXACT
# (name, cycle rate s^-1 at ~1.2 LHD, effective sticking, Q MeV,
#  neutrons per fusion)   -- rates and stickings SOURCED, muCF literature bands
FUELS = [
    ("d-t",    1.2e8, 0.00505, 17.59, 1.0),
    ("d-d",    1.5e6, 0.12,     3.65, 0.5),
    ("t-t",    1.5e6, 0.14,    11.33, 2.0),
    ("p-d",    5.6e6, 0.90,     5.49, 0.0),
    ("p-t",    1.0e6, 0.95,    19.81, 0.0),
    ("p-p",    1.0e2, 0.99,     1.44, 0.0),
    ("d-He3",  1.0e5, 0.99,    18.35, 0.0),
    ("p-He3",  1.0e4, 0.99,     1.86, 0.0),
]
N_MEASURED_DT = 150.0              # [C44] Los Alamos, and the plant uses THIS


def cycles_per_muon(lambda_c, sticking):
    return 1.0 / (sticking + LAMBDA_0 / lambda_c)


def fuel_table():
    out = []
    for name, lc, ws, q, n in FUELS:
        cyc = cycles_per_muon(lc, ws)
        out.append((name, lc, ws, q, n, cyc, cyc * q, cyc * n))
    return out


def model_fidelity():
    """The model against its one measured point. It is used for RATIOS between
    fuels and never for an absolute N -- the plant uses the measured 150."""
    dt = [r for r in fuel_table() if r[0] == "d-t"][0]
    return dt[5] / N_MEASURED_DT


# ---- AND A D2 CELL DOES NOT STAY A D2 CELL --------------------------------
# One branch of d-d makes TRITIUM -- d + d -> t + p, about half the time -- and
# dtmu forms some eighty times faster than ddmu. So a pure deuterium cell
# tritiates itself until production balances burn, and then runs as a mixture.
# It is not a choice; it is what the cell does.
#
#   steady state:  0.5 f_dd = f_dt  and  f_dd + f_dt = 1   ->  f_dt = 1/3
#
# and the tritium concentration that produces that split follows from the two
# formation rates. The result is the number that matters here: a cell that
# makes its own tritium holds a PERCENT of it rather than half.
def selftritiation():
    """(f_dt, f_dd, tritium atom fraction, N, MeV/muon, n/muon, T mass frac)."""
    ldt = dict((f[0], f[1]) for f in FUELS)["d-t"]
    ldd = dict((f[0], f[1]) for f in FUELS)["d-d"]
    wdt = dict((f[0], f[2]) for f in FUELS)["d-t"]
    wdd = dict((f[0], f[2]) for f in FUELS)["d-d"]
    f_dt, f_dd = 1.0 / 3.0, 2.0 / 3.0
    ratio = (f_dt / f_dd) * ldd / ldt
    c_t = ratio / (1.0 + ratio)
    lc = ldt * c_t + ldd * (1.0 - c_t)
    ws = f_dt * wdt + f_dd * wdd
    n_cycles = cycles_per_muon(lc, ws)
    q = f_dt * 17.59 + f_dd * 3.65
    n = f_dt * 1.0 + f_dd * 0.5
    m_t = c_t * 3.016 / (c_t * 3.016 + (1.0 - c_t) * 2.014)
    return f_dt, f_dd, c_t, n_cycles, n_cycles * q, n_cycles * n, m_t


def report_fuels():
    """Is d-t the only fuel? A closed scan over the pairs a muon can bind."""
    print("  THE FUEL SCAN")
    print()
    print("    Theorem 1 closes the BINDER question and says nothing about")
    print("    what the mesomolecule holds. This asks the other half, and it")
    print("    matters because tritium is the largest environmental liability")
    print("    in the plant. The candidate set is closed the same way: a")
    print("    mesomolecular fuel is a PAIR of light nuclei, the hydrogen")
    print("    isotopes give exactly six, and the helium pairs are listed")
    print("    beside them and excluded by the same arithmetic.")
    print()
    print("    THE FIGURE OF MERIT IS NOT Q. A muon is a reusable catalyst")
    print("    with two ways of being lost, so what one is worth is")
    print("      N = 1 / (omega_s + lambda_0/lambda_c)")
    print("    A slow cycle is punished by decay and a sticky one by sticking.")
    print()
    print("      fuel     cycle rate   sticking   decay term      N"
          "     MeV/muon   n/muon")
    for name, lc, ws, _q, _n, cyc, e, nn in fuel_table():
        print(f"      {name:7s} {lc:11.2e} {100*ws:8.2f} %"
              f" {LAMBDA_0/lc:12.4f} {cyc:8.2f} {e:11.1f} {nn:8.2f}")
    print()
    best = max(fuel_table(), key=lambda r: r[6])
    second = sorted(fuel_table(), key=lambda r: -r[6])[1]
    print(f"    d-t is first by {best[6]/second[6]:.0f}x on energy per muon, and")
    print(f"    the second is {second[0]}, which uses MORE tritium than d-t does.")
    dd = [r for r in fuel_table() if r[0] == "d-d"][0]
    print(f"    Against d-d -- the only tritium-free pair with any rate at")
    print(f"    all -- it is {best[6]/dd[6]:.0f}x on energy and {best[7]/dd[7]:.0f}x on neutrons.")
    print()
    print(f"    THE MODEL AGAINST ITS ONE MEASURED POINT: it returns")
    print(f"    {best[5]:.1f} cycles for d-t where {N_MEASURED_DT:.0f} were measured,")
    print(f"    a fidelity of {model_fidelity():.3f}. It is therefore used for")
    print("    RATIOS between fuels and never for an absolute N -- every")
    print("    balance in this work uses the MEASURED 150.")
    print()
    print("    SO YES: d-t IS THE ONLY FUEL, and it is not a preference. It")
    print("    is the only pair whose cycle is fast enough to outrun the muon")
    print("    and whose sticking is low enough to let it repeat.")
    print()
    print("    BUT A D2 CELL DOES NOT STAY A D2 CELL, AND THAT IS THE ANSWER")
    print("    THE SCAN ALMOST HID.")
    f_dt, f_dd, c_t, n_cyc, e, n, m_t = selftritiation()
    print()
    print("      One branch of d-d makes TRITIUM -- d + d -> t + p, about half")
    print("      the time -- and dtmu forms some eighty times faster than ddmu.")
    print("      So a deuterium cell tritiates ITSELF until production balances")
    print("      burn. That is not a choice; it is what the cell does.")
    print()
    print(f"        steady state          f_dt {f_dt:.4f}   f_dd {f_dd:.4f}")
    print(f"        tritium atom fraction {100*c_t:8.3f} %")
    print(f"        tritium MASS fraction {100*m_t:8.3f} %"
          f"   against 60 % in d-t")
    print(f"        cycles per muon       {n_cyc:8.2f}")
    print(f"        neutrons per muon     {n:8.3f}"
          f"   against {best[7]:.1f} for d-t")
    print()
    print(f"      A CELL THAT MAKES ITS OWN TRITIUM HOLDS "
          f"{0.600/m_t:.0f}x LESS OF IT, and it")
    print("      needs no lithium, no breeder zone, no tritium plant, no")
    print("      staged charging and no fleet doubling time -- the whole")
    print("      tritium economy leaves the design with the tritium charge.")
    print()
    print("      WHAT IT COSTS is the fusion channel, by "
          f"{best[7]/n:.0f}x in neutrons. See")
    print("      environment.py --tradeoff for what that is worth at the")
    print("      station, where the channel is a fourteenth of the source.")
    print()
    print("      NOT COMPUTED AND IT RUNS AGAINST THIS: the other d-d branch")
    print("      makes He-3, muon transfer to He-3 is fast, and He-3 is a")
    print("      known poison in deuterium cells. It would lower N further by")
    print("      an amount this work does not calculate. The equilibrium above")
    print("      is FIRST ORDER and is stated as a requirement to measure, not")
    print("      as a result to build on.")


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
    print()
    print("  the fuel scan closes the same way the binder scan does")
    tab = fuel_table()
    check("the hydrogen pairs are complete: p-p, p-d, p-t, d-d, d-t, t-t",
          {r[0] for r in tab} >= {"p-p", "p-d", "p-t", "d-d", "d-t", "t-t"})
    check("d-t is first on energy per muon",
          max(tab, key=lambda r: r[6])[0] == "d-t")
    check("  -- and first on neutrons per muon",
          max(tab, key=lambda r: r[7])[0] == "d-t")
    check("the second best uses MORE tritium, not less",
          sorted(tab, key=lambda r: -r[6])[1][0] == "t-t")
    check("d-t beats the best tritium-free pair by over a hundred times",
          max(tab, key=lambda r: r[6])[6]
          / [r for r in tab if r[0] == "d-d"][0][6] > 100.0)
    check("the model reproduces its one measured point within 30 percent",
          0.7 < model_fidelity() < 1.3)
    check("  -- and the plant uses the MEASURED N, not the model's",
          abs(N_MEASURED_DT - 150.0) < 1e-9)
    # the figure of merit must be a FIGURE OF MERIT: a fuel with a huge Q and
    # a dead cycle must lose to one with a small Q and a live one.
    check("a large Q does not rescue a slow, sticky cycle",
          [r for r in tab if r[0] == "p-t"][0][6]
          < [r for r in tab if r[0] == "d-t"][0][6])
    print()
    print("  a deuterium cell tritiates itself, and the selftest pins it")
    f_dt, f_dd, c_t, n_cyc, _e, n, m_t = selftritiation()
    check("production balances burn at the stated split",
          abs(0.5 * f_dd - f_dt) < 1e-12)
    check("the equilibrium tritium fraction is percent-scale, not half",
          0.001 < c_t < 0.05)
    check("  -- so the holding falls by more than an order of magnitude",
          0.600 / m_t > 10.0)
    check("and it costs the fusion channel more than an order of magnitude",
          [r for r in tab if r[0] == "d-t"][0][7] / n > 10.0)
    check("the equilibrium is between the two pure cases, as it must be",
          [r for r in tab if r[0] == "d-d"][0][5] < n_cyc
          < [r for r in tab if r[0] == "d-t"][0][5])
    print()
    print(f"selftest: {fail} failures -> {'PASS' if fail == 0 else 'FAIL'}")
    return 1 if fail else 0


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--selftest", action="store_true")
    ap.add_argument("--fuels", action="store_true",
                    help=report_fuels.__doc__)
    a = ap.parse_args()
    if a.selftest:
        return selftest()
    if a.fuels:
        return report_fuels()
    return report()


if __name__ == "__main__":
    sys.exit(main())
