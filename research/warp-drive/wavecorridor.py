#!/usr/bin/env python3
r"""
wavecorridor.py -- SOUND AND RESONANCE AGAINST THE TRANSITION CORRIDOR.
THE ACOUSTIC METRIC IS REAL, IT IS THE ONLY HORIZON IN THIS PROJECT ANYONE HAS
ACTUALLY BUILT, AND IT IS A METRIC FOR PHONONS.

M: "Let's also consider sound/wave frequencies as a way to open and traverse a
warp transition corridor, considering each particle and atom have their own
harmonic wave functions."

    python3 wavecorridor.py             the reading
    python3 wavecorridor.py --selftest  fixtures, stdlib only

THE PREMISE IS CORRECT AND IT IS LITERALLY WHAT THIS CORPUS INDEXES.  Every
member of the master index carries quantum numbers, and a quantum number IS a
harmonic specification -- THE CRITERION for membership is exactly that.  So the
question is not whether matter is harmonic.  It is whether SOUND can act on that
harmonic structure, and the answer splits three ways.

    claim                                          verdict
    -------------------------------------------------------------------
    sound gives a genuine effective METRIC         TRUE, and it is a theorem
    a sonic HORIZON can be built and measured      TRUE, and it has been
    that horizon is a spacetime corridor           FALSE -- phonons only

===============================================================================
1. THE ACOUSTIC METRIC IS A THEOREM, NOT AN ANALOGY
===============================================================================

For an irrotational, barotropic, inviscid fluid of density rho with background
flow v and local sound speed c_s, the linearised velocity-potential perturbation
obeys the massless wave equation in the EFFECTIVE METRIC (Unruh 1981;
Visser 1998):

    g_munu  =  (rho / c_s) *  [ -(c_s^2 - v^2)    -v_j  ]
                              [   -v_i             d_ij ]

**THAT IS THE PAINLEVE-GULLSTRAND FORM OF A BLACK HOLE METRIC**, exactly, with
c_s where c belongs.  It is not a resemblance and not a metaphor: phonons in
that fluid obey the same equation a scalar field obeys in curved spacetime, term
for term.  `acoustic_metric()` returns the matrix and
`is_painleve_gullstrand()` checks the identification against the standard form.

**AND THE HORIZON CONDITION IS |v| = c_s** -- where the flow outruns its own
sound.  `horizon_condition()`.  Unlike every other horizon in this project, that
one is easy: a de Laval nozzle does it, and so does a Bose-Einstein condensate.

===============================================================================
2. IT HAS BEEN BUILT.  NOTHING ELSE IN THIS PROJECT HAS
===============================================================================

`analog_hawking_T()` gives T = hbar kappa / (2 pi k_B), kappa = d|v|/dx at the
horizon.  For a BEC at c_s ~ 0.5 mm/s with the transition over ~2 um:

    analog T_H            3.04e-10 K   against a condensate around 1 nK
    a 10-Msun black hole  6.17e-9  K   against a 2.7255 K sky

**THE ASYMMETRY IS A RATIO AND IT IS THE WHOLE REASON THE EXPERIMENT WORKS.**
The analog signal is 0.30 of its own background -- a fraction, not an excess,
and measurable only with care.  A stellar black hole's is 2.3e-9 of its
background, nine orders down and unobservable in principle.  **The analog sits
about 1.3e8 times better against its noise floor**, which is the honest form of
the comparison; an earlier draft of this file wrote "warmer than its bath" and
the fixture refuted it.  Steinhauer measured it (Nature Physics 12, 959 (2016);
Nature 569, 688 (2019)) -- and the 2019 result is a measurement of CORRELATIONS
ACROSS THE HORIZON rather than a thermal excess, which is why the ratio above
does not have to exceed one.

    SOUND IS THE ONLY PLACE IN THIS ENTIRE PROJECT WHERE A HORIZON HAS BEEN
    MADE IN A LABORATORY AND ITS RADIATION READ OFF.

That is worth stating loudly before section 3 takes it away, because it is the
strongest experimental fact anywhere near this subject.

===============================================================================
3. AND IT IS A METRIC FOR PHONONS -- WHICH IS THIS TREE'S OWN RULE
===============================================================================

The acoustic metric governs SOUND.  Light does not see it, matter does not see
it, and gravity does not see it.  A sonic horizon traps phonons and nothing
else; you can reach into a de Laval nozzle and pull your hand back out.

**THIS IS EXACTLY unified.py's RULE ON EIGHT, AND IT IS THE TEXTBOOK CASE OF
IT.**  That rule says a shared mathematical shape is not a correspondence, and
the tree already applies it to refuse that the transition equation is an
instance of the method equation.  Analog gravity is the same shape-sharing at
its most exact -- the equations are IDENTICAL, not merely similar -- and the
analog-gravity literature is itself explicit that the correspondence is
kinematic and not dynamical: the acoustic metric obeys fluid dynamics, not the
Einstein field equations.  `shared_shape_verdict()` states it.

===============================================================================
4. THE FREQUENCY GAP, COMPUTED
===============================================================================

M's premise is that atoms have their own harmonic functions.  They do.  The
question is whether sound can reach them, and `frequency_gap()` says no by ten
orders:

    proton Compton frequency  m c^2 / h        2.2687e23 Hz
    carbon-12                                  2.7028e24 Hz
    highest phonon in any solid (diamond)      4.6466e13 Hz
    ---------------------------------------------------------
    RATIO                                      4.8826e9

A phonon at diamond's Debye frequency carries **2.05e-10 of a proton's rest
energy** -- 0.192 eV against 938 MeV.  Sound is a collective excitation of
matter that is already assembled; it is ten orders too slow to address the
internal harmonic of the matter assembling it, and 1e10 too soft to do anything
to a nucleon.

**AND THE SPEED IS THE SAME STORY.**  `sound_speeds()`: the fastest bulk sound
in any material is about 18 km/s in diamond, so c/c_s = 1.67e4.  A corridor
whose signals travel at the speed of sound is four orders SLOWER than one built
of light, and `transit.py` already measured that light gives advantage 0.000.

**AND THE INTENSITY IS NOT CLOSE.**  `acoustic_energy_density()` takes a solid
at its fracture strain -- the most violent sound a material can carry before it
stops being a material -- and gets about 5e7 J/m^3.  `gjw.py`'s threshold at
D = 1 m is 9.505e43 Pa.  `sound_against_gjw()` returns the shortfall:
**1.9e36**.  Sound is not a weak route to the corridor; it is 36 orders outside
the room.

===============================================================================
5. WHAT RESONANCE IS ACTUALLY FOR, AND IT IS NOT NOTHING
===============================================================================

This is the second time a proposal of M's has turned out to name a real
component in the wrong layer, and the pattern is now worth naming.

    proposal                    wrong layer      RIGHT layer
    ----------------------------------------------------------------
    counter-rotating magnets    source           ORIENTATION -- corridor.py's
                                                 parity theorem: the current's
                                                 handedness labels WHICH MOUTH
                                                 IS THE ENTRANCE
    harmonic resonance          source           ADDRESSING -- which atoms,
                                                 verified to 1 part in 4.3e17

`addressing_precision()` reads the sharpest resonances anyone has:

    Sr-87 optical clock, 698 nm    Q = 4.292e17
    Al+ clock                      Q = 1.401e17
    Cs hyperfine                   Q = 9.193e13
    Fe-57 Mossbauer                Q = 7.390e11

**AND stock.py GIVES THAT A JOB.**  A transition requires the destination to
hold specific elements -- phosphorus binds at 1.7167e3 against stellar material.
Confirming that a remote site holds the right stock, and addressing the
particular species once there, is a SPECTROSCOPIC operation, and spectroscopy is
resonance.  The corpus's index IS the table those measurements read against.

    RESONANCE DOES NOT OPEN THE CORRIDOR.  IT IS HOW YOU KNOW WHICH END YOU
    ARE TALKING TO AND WHAT IT IS MADE OF.

Source layer, orientation layer, addressing layer.  Two of the three now have a
proposed instrument and the third does not.

===============================================================================
6. WHAT THIS FILE REFUSES
===============================================================================

**TO CALL THE ACOUSTIC METRIC A SPACETIME.**  Section 3.  The correspondence is
kinematic; the acoustic metric obeys fluid dynamics and not the field equations,
and no sonic horizon has ever trapped anything but sound.

**TO CALL ANALOG HAWKING RADIATION HAWKING RADIATION.**  It is the same
kinematic effect in a different metric, which is exactly why it tests the
derivation -- and exactly why it is not evidence about black holes' dynamics.
The 2016 result was contested in the literature; `STEINHAUER_STATUS` records
that rather than quoting the claim clean.

**TO PRICE A PHONON ROUTE AS MERELY EXPENSIVE.**  36 orders is not a
gap to be engineered.  Section 4 states it as a refusal, not a target.

**TO SAY M's PREMISE IS WRONG.**  It is right: matter is harmonic, and this
corpus is an index of exactly those harmonics.  What is wrong is only the layer
the mechanism was placed in, and section 5 places it.

**TO RE-DERIVE gjw.py OR stock.py.**  Both are IMPORTED.  The 9.505e43 Pa
threshold and the phosphorus factor come from the instruments that own them.
"""

import math
import sys

import gjw
import stock

H = 6.62607015e-34
HBAR = 1.054571817e-34
KB = 1.380649e-23
C = 2.99792458e8
EV = 1.602176634e-19
M_P = 1.67262192369e-27
M_E = 9.1093837015e-31
U = 1.66053906660e-27
G_N = 6.67430e-11
MSUN = 1.98892e30

ACOUSTIC_CITE = ("Unruh (1981), PRL 46, 1351; Visser (1998), "
                 "Class. Quantum Grav. 15, 1767 -- the acoustic metric")
STEINHAUER_STATUS = (
    "Steinhauer, Nature Physics 12, 959 (2016) reported analog Hawking "
    "radiation in a BEC and was CONTESTED; de Nova, Golubkov, Kolobov & "
    "Steinhauer, Nature 569, 688 (2019) measured the entanglement and is "
    "widely accepted.  Cited with its dispute, not quoted clean."
)

#: Debye temperatures, K.  The ceiling on phonon frequency in each solid.
DEBYE_K = {"lead": 105, "copper": 343, "silicon": 645, "diamond": 2230}

#: Bulk sound speeds, m/s.
SOUND = {"air": 343.0, "water": 1481.0, "steel": 5960.0, "diamond": 18000.0}

#: (name, frequency Hz, linewidth Hz) for the sharpest resonances available.
RESONANCES = (("Sr-87 optical clock, 698 nm", 4.2921e14, 1.0e-3),
              ("Al+ optical clock", 1.1210e15, 8.0e-3),
              ("Cs hyperfine (the SI second)", 9.1926e9, 1.0e-4),
              ("Fe-57 Mossbauer", 3.4735e18, 4.7e6))


# ------------------------------------------------------- 1. the acoustic metric

def acoustic_metric(rho, cs, v):
    """The 4x4 effective metric phonons propagate in.  Unruh 1981, Visser 1998.

    v is a 3-vector.  Returned in the (t, x, y, z) block form of the docstring,
    with the conformal factor rho/c_s carried explicitly.
    """
    v2 = sum(x * x for x in v)
    k = rho / cs
    g = [[-k * (cs * cs - v2)] + [-k * v[j] for j in range(3)]]
    for i in range(3):
        g.append([-k * v[i]] + [k * (1.0 if i == j else 0.0) for j in range(3)])
    return g


def is_painleve_gullstrand(rho=1.0, cs=1.0, vr=0.7, tol=1e-12):
    """Does the acoustic metric match PG form with c_s in place of c?

    PG:  ds^2 = -(c^2 - v^2)dt^2 - 2 v dr dt + dr^2.  Checked on the g_tt and
    g_tr entries against the returned matrix, conformal factor divided out.
    """
    g = acoustic_metric(rho, cs, (vr, 0.0, 0.0))
    k = rho / cs
    return (abs(g[0][0] / k + (cs * cs - vr * vr)) < tol
            and abs(g[0][1] / k + vr) < tol
            and abs(g[1][1] / k - 1.0) < tol)


def horizon_condition(cs, v):
    """True where the flow outruns its own sound -- the acoustic horizon."""
    return math.sqrt(sum(x * x for x in v)) >= cs


def analog_hawking_T(cs, dx):
    """T = hbar kappa / (2 pi kB), kappa = c_s/dx the surface-gravity analog."""
    return HBAR * (cs / dx) / (2.0 * math.pi * KB)


def real_hawking_T(M):
    """T = hbar c^3 / (8 pi G M kB), for the comparison in section 2."""
    return HBAR * C ** 3 / (8.0 * math.pi * G_N * M * KB)


def why_the_analog_is_measurable():
    """(analog T, its bath, real T, CMB, analog signal-to-background,
    real signal-to-background, how many orders better the analog sits).

    THE COMPARISON IS A RATIO, NOT A BOOLEAN, AND A FIRST DRAFT GOT IT WRONG.
    The analog T_H is 0.304 nK against a condensate around 1 nK, so it is a
    FRACTION of its background -- comparable, measurable with care, and not
    "warmer than its bath" as this function first claimed.  A stellar black
    hole sits 9 orders BELOW the CMB.  The analog is about 8 orders better
    positioned, and that is the honest form of the asymmetry.
    """
    a = analog_hawking_T(0.5e-3, 2e-6)
    r = real_hawking_T(10 * MSUN)
    bec_bath, cmb = 1e-9, 2.7255
    return a, bec_bath, r, cmb, a / bec_bath, r / cmb, (a / bec_bath) / (r / cmb)


# --------------------------------------------------------- 3. the shape rule

def shared_shape_verdict():
    """Why the acoustic metric is unified.py's rule on EIGHT, stated."""
    return ("The equations are IDENTICAL, not similar -- which makes this the "
            "textbook case of a shared shape that is not a correspondence. "
            "The acoustic metric obeys fluid dynamics, not the Einstein field "
            "equations, and no sonic horizon has trapped anything but sound.")


# ------------------------------------------------------- 4. the frequency gap

def compton_frequency(m):
    """nu = m c^2 / h -- the harmonic of the rest mass itself."""
    return m * C * C / H


def debye_frequency(solid):
    """nu_D = kB theta_D / h -- the highest phonon a solid can carry."""
    return KB * DEBYE_K[solid] / H


def frequency_gap(m=M_P, solid="diamond"):
    """(Compton nu, Debye nu, ratio) -- ten orders for a proton against diamond."""
    a, b = compton_frequency(m), debye_frequency(solid)
    return a, b, a / b


def phonon_energy_fraction(solid="diamond", m=M_P):
    """A Debye phonon's energy as a fraction of a proton's rest energy."""
    return H * debye_frequency(solid) / (m * C * C)


def sound_speeds():
    """[(medium, c_s, c/c_s)] -- the fastest bulk sound is 1.67e4 below light."""
    return [(k, v, C / v) for k, v in
            sorted(SOUND.items(), key=lambda kv: kv[1])]


def acoustic_energy_density(modulus=1.0e12, strain=1.0e-2):
    """Energy density of the most violent sound a solid can carry, in J/m^3.

    (1/2) E eps^2 at the fracture strain.  Beyond it the medium is not a medium.
    """
    return 0.5 * modulus * strain * strain


def sound_against_gjw(D=1.0):
    """(acoustic ceiling, gjw threshold at D, shortfall) -- 36 orders.

    The threshold is IMPORTED from gjw.py, never restated here.
    """
    need = gjw.casimir_cycle(D) * gjw.amplification_needed(D)
    have = acoustic_energy_density()
    return have, need, need / have


# ------------------------------------------------------- 5. what resonance is for

def addressing_precision():
    """[(name, nu, linewidth, Q)] sorted by Q -- what resonance IS precise at."""
    return sorted(((n, nu, dn, nu / dn) for n, nu, dn in RESONANCES),
                  key=lambda r: -r[3])


def best_Q():
    return addressing_precision()[0][3]


def what_addressing_is_for():
    """The job stock.py hands to spectroscopy, with stock.py's own figure."""
    el, fac = stock.binding_element()
    return ("A transition needs the destination to hold specific elements -- "
            "%s binds at %.4e against stellar material.  Confirming a remote "
            "site's stock, and addressing the species once there, is "
            "spectroscopy, and spectroscopy is resonance." % (el, fac))


# ------------------------------------------------------------------- reading

def report():
    print(__doc__.split("=====", 1)[0].strip())
    print()
    print("=" * 74)
    print("1 & 2.  THE ACOUSTIC METRIC, AND THE ONE HORIZON THAT GOT BUILT")
    print("=" * 74)
    print("   Painleve-Gullstrand identification holds: %s"
          % is_painleve_gullstrand())
    print("   horizon at |v| = c_s: at v=0.9 c_s %s, at v=1.1 c_s %s"
          % (horizon_condition(1.0, (0.9, 0, 0)),
             horizon_condition(1.0, (1.1, 0, 0))))
    print("   %s" % ACOUSTIC_CITE)
    print()
    a, bath, r, cmb, sa, sr, better = why_the_analog_is_measurable()
    print("   analog T_H (BEC, c_s 0.5 mm/s over 2 um)  %.4e K" % a)
    print("      against a condensate near              %.4e K  -> S/B %.3e"
          % (bath, sa))
    print("   10-solar-mass black hole                  %.4e K" % r)
    print("      against the CMB                        %.4e K  -> S/B %.3e"
          % (cmb, sr))
    print("   the analog sits %.3e times better against its noise floor"
          % better)
    print("   %s" % STEINHAUER_STATUS)
    print()
    print("=" * 74)
    print("3.  AND IT IS A METRIC FOR PHONONS")
    print("=" * 74)
    print("   " + shared_shape_verdict().replace(". ", ".\n   "))
    print()
    print("=" * 74)
    print("4.  THE FREQUENCY GAP")
    print("=" * 74)
    for nm, m in (("electron", M_E), ("proton", M_P), ("carbon-12", 12 * U),
                  ("70 kg payload", 70.0)):
        print("   Compton nu, %-16s %.4e Hz" % (nm, compton_frequency(m)))
    print()
    for s in sorted(DEBYE_K, key=lambda k: DEBYE_K[k]):
        print("   Debye nu,   %-16s %.4e Hz   (%.3f eV)"
              % (s, debye_frequency(s), H * debye_frequency(s) / EV))
    cf, df, ratio = frequency_gap()
    print("\n   proton Compton / diamond Debye            %.4e" % ratio)
    print("   a Debye phonon is this fraction of m_p c^2 %.3e"
          % phonon_energy_fraction())
    print()
    for nm, cs, ratio2 in sound_speeds():
        print("   c/c_s, %-10s %8.1f m/s -> %.4e" % (nm, cs, ratio2))
    have, need, short = sound_against_gjw()
    print("\n   most violent sound a solid can carry      %.3e J/m^3" % have)
    print("   gjw.py's threshold at D = 1 m             %.3e" % need)
    print("   SHORTFALL                                 %.3e" % short)
    print()
    print("=" * 74)
    print("5.  WHAT RESONANCE IS ACTUALLY FOR")
    print("=" * 74)
    for nm, nu, dn, q in addressing_precision():
        print("   %-30s nu %.4e   dnu %.2e   Q %.3e" % (nm, nu, dn, q))
    print()
    print("   " + what_addressing_is_for().replace(". ", ".\n   "))


# ------------------------------------------------------------------ fixtures

def selftest():
    bad = []

    def chk(what, got, want):
        ok = got == want
        if not ok:
            bad.append((what, got, want))
        print("   %-60s %s" % (what, "ok" if ok else "FAIL %r != %r"
                               % (got, want)))

    print("wavecorridor.py fixtures  (stdlib only; imports gjw.py and stock.py)")

    # -- 1.  the metric is the real thing ------------------------------------
    chk("the acoustic metric IS Painleve-Gullstrand with c_s for c",
        is_painleve_gullstrand(), True)
    chk("and at several flows", [is_painleve_gullstrand(1.3, 2.0, v)
                                 for v in (0.1, 0.5, 0.99, 1.5)],
        [True] * 4)
    chk("subsonic flow has no horizon", horizon_condition(1.0, (0.9, 0, 0)),
        False)
    chk("supersonic flow does", horizon_condition(1.0, (1.1, 0, 0)), True)
    chk("g_tt changes sign exactly at the horizon",
        acoustic_metric(1.0, 1.0, (1.0, 0, 0))[0][0], 0.0)

    # -- 2.  the asymmetry that makes the analog measurable -------------------
    a, bath, r, cmb, sa, sr, better = why_the_analog_is_measurable()
    chk("the analog T_H is a FRACTION of its bath, not an excess", sa < 1.0,
        True)
    chk("and that fraction is 0.304", float("%.3g" % sa), 0.304)
    chk("a 10-Msun hole is 9 orders below the CMB",
        int(round(-math.log10(sr))), 9)
    chk("so the analog sits ~8 orders better against its noise floor",
        int(round(math.log10(better))), 8)
    chk("analog T_H to three digits, in K", float("%.3g" % a), 3.04e-10)

    # -- 4.  the gap ----------------------------------------------------------
    chk("proton Compton frequency, 4 digits",
        float("%.4g" % compton_frequency(M_P)), 2.269e23)
    chk("diamond's Debye frequency is the highest of the four",
        max(DEBYE_K, key=lambda s: debye_frequency(s)), "diamond")
    chk("the gap is ten orders", int(round(math.log10(frequency_gap()[2]))), 10)
    chk("a Debye phonon is 2.05e-10 of a proton's rest energy",
        float("%.3g" % phonon_energy_fraction()), 2.05e-10)
    chk("the fastest bulk sound is still 1.67e4 below light",
        float("%.3g" % sound_speeds()[-1][2]), 1.67e4)
    chk("and sound falls short of gjw's threshold by 36 orders",
        int(round(math.log10(sound_against_gjw()[2]))), 36)
    # a measuring fixture: a SOFTER solid must be further behind, not equal
    chk("a softer solid is strictly further behind diamond",
        debye_frequency("lead") < debye_frequency("diamond"), True)
    chk("and the gap scales with the Debye temperature exactly",
        float("%.6g" % (frequency_gap(M_P, "lead")[2]
                        / frequency_gap(M_P, "diamond")[2])),
        float("%.6g" % (DEBYE_K["diamond"] / DEBYE_K["lead"])))

    # -- 5.  what resonance IS good at ----------------------------------------
    chk("the sharpest resonance is the Sr-87 clock",
        addressing_precision()[0][0], "Sr-87 optical clock, 698 nm")
    chk("at Q = 4.29e17", float("%.3g" % best_Q()), 4.29e17)
    chk("Mossbauer is sharp in frequency but not in Q",
        addressing_precision()[-1][0], "Fe-57 Mossbauer")
    chk("the addressing job cites stock.py's own binding element",
        stock.binding_element()[0] in what_addressing_is_for(), True)

    # -- the refusals are load-bearing ----------------------------------------
    chk("the Steinhauer citation carries its dispute",
        "CONTESTED" in STEINHAUER_STATUS, True)
    chk("the shape verdict names the kinematic/dynamical split",
        "not the Einstein field equations" in shared_shape_verdict(), True)

    print("\n%d failure(s)" % len(bad))
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(selftest() if "--selftest" in sys.argv else (report() or 0))
