#!/usr/bin/env python3
r"""
branelink.py -- O6 AND O7, THE BRANE LEFTOVERS; AND S5's FOUR FIGURES, REFUSED.

DOCKET 62's O6/O7 pass proposed closing both rows and left every figure in
/tmp/o6o7.  The ruling kept the finds, corrected the decisive number by a factor
of four, refused both closures and refused the new row R-1.  This file seats
exactly that.

    python3 branelink.py             the reading
    python3 branelink.py --selftest  stdlib decimal + sympy; a few seconds

===============================================================================
1. O6 -- THE BRANE-BULK TRANSDUCER.  OPEN, NARROWED.  NOT CLOSED.
===============================================================================

THE FIND, AND IT STANDS.  O6's line "neither GKLP paper states a coupling
constant, a source model or an emission rate" is true of the two papers read and
false of the literature.  Kabat & Nomura, arXiv:2309.05759 -- the third paper of
the same group -- state the coupling (eq. 68, g_AB = eta_AB + (2/Mbar5^{3/2})
h_AB; eq. 70, the brane stress-tensor coupling), the source model, the vertex
(eq. 71) and the normalisation that fixes it (eqs. 72-73, Mbar4 = (2 pi r)^{1/2}
Mbar5^{3/2}).  The coupling is not a free parameter; O6's stated cause of death
is REFUTED, and that is a NARROWING, not an answer.  Also kept: GLP eq. (39) puts
the Eot-Wash 38.6 um null on the PRODUCT gamma L, not on L.  (All READ at source
by the O6/O7 pass.)

THE DECISIVE NUMBER, CORRECTED.  A rod spinning at Omega radiates at omega_GW =
2 Omega -- proved below by the period of its own quadrupole.  The pass's script
used Omega.  At the pass's own design point (1000 t, 100 m, Omega = 100 rad/s,
LIGO-class 1e-23 receiver, Proxima span) the strain is h = 4.3359e-48 and the
bulk channel carries 1.5347e-27 bits/s per watt of GW power -- COMPUTED here --
against the reported 8.6717e-48 and 6.1389e-27, exactly 2x and 4x.  Those two are
WITHDRAWN, kept as computed values so the correction names what it corrects.  The
direction survives: an EM link of the same hardware scale (100 m dishes both
ends, 1 GHz) beats it by ~26.6 orders.

WHY IT DOES NOT CLOSE.  (1) The closing premise -- the single-mode capacity
ceiling sqrt(pi P/(3 hbar))/ln 2 is "field-blind" -- is NOT-FOUND by the pass's
own tagging (Pendry 1983, Bekenstein & Schiffer not read), and assuming its
functional form for a carrier with gamma > 1 on a moving brane in a 5D bulk is
failure mode (4).  (2) The closure runs through O7's untested B = 0.  (3) THE
DICHOTOMY NOBODY STATED:
    graviton IS a bulk degree of freedom  -> the transducer exists (LIGO is an
        operating read end), GW170817 binds beta, the saving is <= 93.8 ns, the
        row is settled;
    graviton is NOT (brane-confined)      -> GW170817 bounds nothing about beta,
        the LIGO transducer does not exist, and the bulk scalar's coupling
        carries a free Yukawa lambda (Kabat & Nomura eq. 41): no rate.  The row
        reverts to where it was.
Both branches are unfavourable to the route; only one is a closure.  SETTLED
CONDITIONALLY, which is narrowed.  Still conceded: no moving-brane emission rate
is in print, and the non-zero-winding amplitude has never been computed.

===============================================================================
2. O7 -- OUR OWN BOOST.  OPEN, NARROWED.  NOT CLOSED.
===============================================================================

THE ARITHMETIC, AT 50 DIGITS, NEVER AS A SUBTRACTION AGAINST 1 + d.  With
d = gamma - 1 <= 7.0e-16 (GW170817, manyc.py's seated bound; GKLM eq. (38)
identifies Delta c/c = gamma - 1):
    beta = sqrt(d(2+d))/(1+d) = 3.74165738677e-08,  1/beta = 26726124.1912,
    brane speed 11.2172066497 m/s,  Proxima light time 134009348.4 s = 4.2465 yr
    EXACTLY (a light year is c times a Julian year), Delta_tau = T d/(1+d) =
    93.80654 ns, fraction 7.0e-16.  The ruling's ten-digit 134009341.889 s,
    4.246499794 yr and 93.8065393226 ns are the same arithmetic on the span
    rounded to 4.017499e16 m; they reproduce exactly from that input and differ
    from the seated span's figures by 5e-8, which is the rounding, not the sum.
The pass's double-precision fault is REAL and is reproduced here as a control:
1 - 1/(1+d)^2 in floats gives beta = 3.650024e-08 and 89.2682 ns -- d is three
ulps -- and neither may be quoted.  W7's 1/beta = 2.6726124e7 is vindicated to
every printed digit.  PROVENANCE, CORRECTED: the 94 ns is GW170817's 7e-16, NOT
the CMB dipole; the dipole's Gamma - 1 = 7.6161e-07 is the RECEIVER's B and
enters only through the anisotropy.

WHY IT DOES NOT CLOSE.  GW170817 bounds BETA, the brane's speed through S^1.  O7
asks about B, Earth's velocity relative to the preferred brane frame, and
ledger.py's own answering condition is a measurement of B.  The pass argued that
beta and B are orthogonal degrees of freedom and then closed on beta.  B is not
measured.  The escape is priced (GKLP eq. (22) extremised, g -> 1, as the pass
read it): B >= 0.999387630 buys one second over the Proxima span, B >= 0.99999993
buys half the light time.  UNTESTED, not excluded.  And the bound is CONDITIONAL
on the graviton being a bulk degree of freedom -- GKLM hedge in the sentence the
pass quotes ("if we entertain the possibility that these are bulk degrees of
freedom"); if gravity is brane-confined, Delta c/c = 0 identically.

REFUSED: the new row R-1.  It holds exactly the unmeasured B that O7 was opened
to hold; opening it while retiring O7 renames the question so the closed count
rises -- the mirror of failure mode (5).

RESTATED O7: beta <= 3.74e-08 conditional on a bulk graviton, so one of the
row's two unknowns is fixed and the saving at B = 0 is 93.81 ns over 4.2465
years.  What remains is B, with the escape priced and the experiment named: a
DIRECTIONAL multi-messenger GW/EM arrival-time survey, which has N = 1 event.
AN HONEST NULL, ALSO RECORDED: the loop-induced SME route (Kabat & Nomura eqs.
76-77) at the maximal r = 38.6 um and beta = 1 gives |c| <= 6.37e-64 against a
1e-21 laboratory bound -- 42 orders short, a real measurement that does not bite.

===============================================================================
3. S5 -- THE FOUR FIGURES ARE NOT SEATED
===============================================================================

The O6/O7 pass "re-derived" S5's four missing figures.  It did not: its script
hard-codes one seed value, inverts the channel law to get N, reports a round-trip
residual of 0 -- which is A(N(A)) = A, true for ANY A, proved below symbolically
-- divides once for E, and uses a separately hard-coded mass for Mc^2.
"Mutually consistent to the last printed digit" reads as corroboration and is
not.  NOT MEASURED.  NONE OF THE FOUR APPEARS IN THIS FILE, deliberately, so a
grep for them still finds only ledger.py's note about their absence.  S5 stays
OPEN and DOCKET 56 still owes the instrument that computes N from a
specification.
"""

import math
import sys
from decimal import Decimal, getcontext

import achievable
import foliation
import manyc

# ---------------------------------------------------------------------------
# Constants ASKED of seated modules, never retyped.
# ---------------------------------------------------------------------------
C = foliation.C_LIGHT
G = foliation.G_NEWTON
HBAR = achievable.HBAR
L_PROXIMA = foliation.proxima_span_m()
YR = manyc.YR                                   # Julian year, s
D_GW = manyc.GW170817_BOUND_HI                  # (v_gw - c)/c <= 7e-16, READ there

# INPUTS -- the pass's design point and READ literature values.  Not results.
M_TX, L_TX, OMEGA_TX = 1.0e6, 100.0, 100.0      # kg, m, rad/s: 1000 t rod
H_NOISE = 1.0e-23                               # Hz^-1/2, LIGO-class receiver
NU_EM, DISH_D = 1.0e9, 100.0                    # Hz, m: the EM control link
HPL = 2 * math.pi * HBAR                        # h, from hbar
E_CHARGE = 1.602176634e-19                      # C, exact (SI 2019)
R_EOTWASH = 38.6e-6                             # m, Lee et al. 2020, 95% CL (READ)
MBAR4_GEV = 2.435e18                            # reduced Planck mass (READ)
SME_LAB_BOUND = 1.0e-21                         # Dreissen et al. (READ)
V_CMB = 3.7e5                                   # m/s, CMB dipole (READ)

# ---------------------------------------------------------------------------
# The ruling, as data.
# ---------------------------------------------------------------------------
O6_STATUS = "OPEN (narrowed) -- NOT CLOSED"
O6_CLOSED = False
O6_CAUSE_OF_DEATH_REFUTED = True
COUPLING_SOURCE = ("Kabat & Nomura arXiv:2309.05759 eqs. 68, 70-73 -- coupling, "
                   "source model, vertex, normalisation (READ by the pass)")
EOTWASH_BOUNDS = "gamma*L, not L (GLP eq. 39)"
OMEGA_GW_OVER_OMEGA = 2
CLOSING_PREMISE = "field-blind single-mode capacity ceiling"
CLOSING_PREMISE_STATUS = "NOT-FOUND"
O6_DICHOTOMY = (
    ("graviton is a bulk degree of freedom",
     "transducer exists (LIGO reads); GW170817 binds beta; saving <= 93.8 ns; settled"),
    ("graviton is brane-confined",
     "no transducer; GW170817 bounds nothing about beta; free Yukawa lambda "
     "(Kabat & Nomura eq. 41); no rate; the row reverts"),
)
O6_SETTLED = "CONDITIONALLY -- narrowed, not closed"

O7_STATUS = "OPEN (narrowed) -- NOT CLOSED"
O7_CLOSED = False
GW170817_BOUNDS = "beta (the brane's speed through S^1), not B"
B_MEASURED = False
BETA_BOUND_CONDITIONAL_ON = "the graviton being a bulk degree of freedom"
PROVENANCE_94NS = "GW170817 (7e-16), NOT the CMB dipole"
R1_ROW_OPENED = False
O7_ANSWERED_BY = ("a measurement of B, Earth's velocity relative to the "
                  "preferred brane frame -- a directional multi-messenger GW/EM "
                  "arrival-time survey (N = 1 event today)")

S5_STATUS = "OPEN -- unchanged, downgrade stands"
S5_FIGURES_MEASURED = False
S5_FIGURES_STATUS = ("RECOVERED BY INVERSION from a hard-coded seed; round-trip "
                     "residual is x = f(f^-1(x)) -- NOT MEASURED")
S5_OWED = "DOCKET 56: the instrument that computes N from the specification"

#: The span the O6/O7 pass and the ruling fed their scripts: the seated span
#: rounded to seven figures.  A FIXTURE INPUT ONLY -- it reproduces the ruling's
#: ten-digit figures below; every seated O7 figure uses foliation's span.
RULING_SPAN_M = 4.017499e16

#: Fixtures the ruling reproduced AT RULING_SPAN_M; --selftest recomputes each.
O7_FIXTURES = (("beta", "3.74165738677e-08"), ("1/beta", "26726124.1912"),
               ("brane speed m/s", "11.2172066497"),
               ("Proxima light time s", "134009341.889"),
               ("Proxima light time yr", "4.246499794"),
               ("Delta_tau ns", "93.8065393226"))


# ============================================================ O6
def rod_luminosity(Mkg=M_TX, l_m=L_TX, Om=OMEGA_TX, coeff=(2, 45)):
    """L_GW = (2/45) G M^2 l^4 Omega^6 / c^5; coefficient re-derived by sympy."""
    return coeff[0] / coeff[1] * G * Mkg ** 2 * l_m ** 4 * Om ** 6 / C ** 5


def strain(Lw, D, w):
    """h at distance D, angular frequency w, from Lw/(4 pi D^2) = c^3 w^2 h^2/(16 pi G)."""
    return (2.0 / (D * w)) * math.sqrt(G * Lw / C ** 3)


def bulk_bits_per_watt(w, D=L_PROXIMA, hn=H_NOISE):
    """(h/h_n)^2 bits/s at unit SNR, per watt radiated: 4G/(D^2 c^3 w^2 h_n^2)."""
    return 4.0 * G / (D ** 2 * C ** 3 * w ** 2 * hn ** 2)


def corrected():
    """(h, bits/s/W) at omega_GW = 2 Omega -- the seated figures."""
    w = OMEGA_GW_OVER_OMEGA * OMEGA_TX
    return strain(rod_luminosity(), L_PROXIMA, w), bulk_bits_per_watt(w)


def as_scripted():
    """(h, bits/s/W) at omega = Omega -- the pass's figures, WITHDRAWN."""
    return strain(rod_luminosity(), L_PROXIMA, OMEGA_TX), bulk_bits_per_watt(OMEGA_TX)


def em_bits_per_watt():
    """The control: 100 m dishes both ends at 1 GHz, one bit per photon."""
    lam = C / NU_EM
    area = math.pi * (DISH_D / 2) ** 2
    gain = 4 * math.pi * area / lam ** 2
    return gain * area / (4 * math.pi * L_PROXIMA ** 2) / (HPL * NU_EM)


def brane_beats_bulk_orders():
    return math.log10(em_bits_per_watt() / corrected()[1])


# ============================================================ O7
def o7_exact(digits=50, span_m=L_PROXIMA):
    """Everything in d = gamma - 1, at `digits`, never 1 - 1/(1+d).

    With the seated span (4.2465 ly) the light time is 4.2465 Julian years
    EXACTLY, since a light year is c times one; the ruling's 4.246499794 yr is
    its span rounded to 4.017499e16 m, not a property of the arithmetic."""
    getcontext().prec = digits
    d = Decimal(repr(D_GW))
    beta = (d * (2 + d)).sqrt() / (1 + d)
    T = Decimal(repr(span_m)) / Decimal(repr(C))
    dtau = T * d / (1 + d)
    return {"beta": beta, "1/beta": 1 / beta, "brane speed m/s": beta * Decimal(repr(C)),
            "Proxima light time s": T, "Proxima light time yr": T / Decimal(repr(YR)),
            "Delta_tau ns": dtau * Decimal(10) ** 9, "fraction": dtau / T}


def o7_naive_double():
    """The pass's first script, reproduced as a CONTROL: in double precision d
    is three ulps and 1 - 1/(1+d)^2 loses every digit.  WITHDRAWN figures."""
    beta = math.sqrt(1.0 - 1.0 / (1.0 + D_GW) ** 2)
    save = L_PROXIMA * (1.0 - 1.0 / (1.0 + D_GW)) / C
    return beta, save * 1e9


def cmb_gamma_minus_1():
    """Gamma - 1 at the CMB dipole, precision-safe: expm1(-log1p(-x)/2)."""
    return math.expm1(-0.5 * math.log1p(-(V_CMB / C) ** 2))


def b_for_saving(want_s):
    """The escape priced: the common boost B that buys a forward saving of
    want_s over the Proxima span with the backward excess held at d (GKLP eq.
    (22) extremised, g -> 1, as the pass read it)."""
    T = L_PROXIMA / C
    r = (want_s / T) / D_GW
    return (math.sqrt(r) - 1.0) / (math.sqrt(r) + 1.0)


def zeta3(n=200000):
    return sum(1.0 / k ** 3 for k in range(1, n)) + 1.0 / (2 * n * n)


def sme_coefficient(beta=1.0, R=R_EOTWASH):
    """|c| from Kabat & Nomura eqs. 76-77 at mu r -> 0: I_grav = -zeta(3)/4."""
    hbarc_gev_m = HBAR * C / (E_CHARGE * 1e9)
    rG = R / hbarc_gev_m
    return (1 / (16 * math.pi ** 2)) / (math.pi * rG * MBAR4_GEV) ** 2 \
        * 0.75 * beta ** 2 * zeta3() / 4


# ---------------------------------------------------------------------------
# COMPUTED AT IMPORT, stdlib, so ledger.py can ask them.  Not typed: each is the
# output of a function above, and --selftest pins it against the ruling.
# ---------------------------------------------------------------------------
STRAIN_H, THROUGHPUT_BITS_PER_S_PER_W = corrected()
WITHDRAWN_STRAIN_H, WITHDRAWN_THROUGHPUT = as_scripted()
BRANE_BEATS_BULK_ORDERS = brane_beats_bulk_orders()
_O7 = o7_exact()
BETA_MAX = float(_O7["beta"])                       # conditional on a bulk graviton
SAVING_AT_B0_NS = float(_O7["Delta_tau ns"])
SAVING_FRACTION = float(_O7["fraction"])
CMB_GAMMA_MINUS_1 = cmb_gamma_minus_1()
B_FOR_ONE_SECOND = b_for_saving(1.0)
SME_ORDERS_SHORT = math.log10(SME_LAB_BOUND / sme_coefficient())


# ============================================================ symbolic
def verify_symbolic(sp):
    t, Om, M, ell, Gs, cs = sp.symbols('t Omega M ell G c', positive=True)
    A = M * ell ** 2 / 12
    I = sp.Matrix([[A * sp.cos(Om * t) ** 2, A * sp.sin(Om * t) * sp.cos(Om * t), 0],
                   [A * sp.sin(Om * t) * sp.cos(Om * t), A * sp.sin(Om * t) ** 2, 0],
                   [0, 0, 0]])
    Q = I - sp.eye(3) * I.trace() / 3
    rows = []
    # omega_GW = 2 Omega: the quadrupole has period pi/Omega, not 2 pi/Omega
    shift = Q.subs(t, t + sp.pi / Om) - Q
    rows.append(("Q(t + pi/Omega) - Q(t) = 0", sp.simplify(shift) == sp.zeros(3), True))
    half = sp.simplify((Q.subs(t, t + sp.pi / (2 * Om)) - Q)[0, 0])
    rows.append(("Q(t + pi/2 Omega) != Q(t)  (so the period is exactly pi/Omega)",
                 half != 0, True))
    Q3 = Q.applyfunc(lambda e: sp.diff(e, t, 3))
    Lsym = Gs / (5 * cs ** 5) * sum(Q3[i, j] ** 2 for i in range(3) for j in range(3))
    Lavg = sp.simplify(sp.integrate(Lsym, (t, 0, 2 * sp.pi / Om)) * Om / (2 * sp.pi))
    coeff = sp.nsimplify(sp.simplify(Lavg / (Gs * M ** 2 * ell ** 4 * Om ** 6 / cs ** 5)))
    rows.append(("rod: L_GW / (G M^2 l^4 Omega^6/c^5)", coeff, sp.Rational(2, 45)))
    Lg, D, w, h = sp.symbols('L D omega h', positive=True)
    hsol = sp.solve(sp.Eq(Lg / (4 * sp.pi * D ** 2), cs ** 3 * w ** 2 * h ** 2 / (16 * sp.pi * Gs)), h)[0]
    rows.append(("strain: h - (2/(D w)) sqrt(G L/c^3)",
                 sp.simplify(hsol - 2 / (D * w) * sp.sqrt(Gs * Lg / cs ** 3)), 0))
    # S5: the round trip is a tautology for ANY A
    Asym, hb = sp.symbols('A hbar', positive=True)
    N_of_A = sp.sqrt(Asym * sp.pi / (3 * hb * sp.log(2) ** 2))
    A_of_N = lambda n: 3 * hb * n ** 2 * sp.log(2) ** 2 / sp.pi
    rows.append(("S5: A(N(A)) - A for SYMBOLIC A -- residual 0 proves nothing",
                 sp.simplify(A_of_N(N_of_A) - Asym), 0))
    return rows


# ============================================================ report / selftest
def report():
    print(__doc__.split("=====", 1)[0].strip())
    h, b = corrected()
    hx, bx = as_scripted()
    print("\nO6  corrected (omega_GW = 2 Omega): h = %.4e   bulk = %.4e bits/s/W" % (h, b))
    print("    WITHDRAWN (omega = Omega):       h = %.4e   bulk = %.4e bits/s/W" % (hx, bx))
    print("    EM control %.4e bits/s/W; brane beats bulk by %.2f orders"
          % (em_bits_per_watt(), brane_beats_bulk_orders()))
    ex = o7_exact()
    print("\nO7  (50 digits, conditional on a bulk graviton)")
    for k in ("beta", "1/beta", "brane speed m/s", "Proxima light time s",
              "Proxima light time yr", "Delta_tau ns", "fraction"):
        print("    %-24s %s" % (k, "%.12g" % ex[k]))
    nb, ns = o7_naive_double()
    print("    WITHDRAWN, double precision: beta = %.6e, %.4f ns" % (nb, ns))
    print("    CMB dipole Gamma - 1 = %.4e -- the receiver's B, not the 94 ns" % cmb_gamma_minus_1())
    print("    escape: B >= %.9f buys 1 s; B >= %.8f buys half the light time"
          % (b_for_saving(1.0), b_for_saving(0.5 * L_PROXIMA / C)))
    print("    SME null: |c| <= %.3e vs %.0e -- %.0f orders short"
          % (sme_coefficient(), SME_LAB_BOUND, math.log10(SME_LAB_BOUND / sme_coefficient())))
    print("\nO6: %s   O7: %s   S5: %s" % (O6_STATUS, O7_STATUS, S5_STATUS))
    return 0


def selftest():
    ok = True

    def chk(label, got, want):
        nonlocal ok
        good = got == want
        ok &= good
        print("  [%s] %-62s %s" % ("ok" if good else "XX", label,
                                   got if good else "%s != %s" % (got, want)))

    def near(label, got, want, tol):
        nonlocal ok
        d = abs(got - want) / max(1e-300, abs(want))
        good = d <= tol
        ok &= good
        print("  [%s] %-62s %.12g (rel %.1e)" % ("ok" if good else "XX", label, got, d))

    try:
        import sympy as sp
    except ImportError as exc:                       # pragma: no cover
        raise SystemExit("branelink.py --selftest needs sympy: %s" % exc)

    print("1. THE SYMBOLIC STEPS (sympy)")
    for lab, got, want in verify_symbolic(sp):
        if isinstance(got, bool):
            chk(lab, got, want)
        else:
            chk(lab, sp.simplify(got - want) == 0, True)

    print("\n2. O6 -- THE DECISIVE NUMBER, CORRECTED BY A FACTOR OF FOUR")
    h, b = corrected()
    hx, bx = as_scripted()
    near("corrected strain h at omega_GW = 2 Omega", h, 4.3359e-48, 1e-4)
    near("corrected bulk channel, bits/s/W", b, 1.5347e-27, 1e-4)
    near("WITHDRAWN strain (omega = Omega)", hx, 8.6717e-48, 1e-4)
    near("WITHDRAWN bulk channel", bx, 6.1389e-27, 1e-4)
    chk("the error is exactly 2x and 4x", (round(hx / h, 12), round(bx / b, 12)), (2.0, 4.0))
    near("CONTROL: the EM link is non-zero and sensible, ~1 bit/s/W",
         em_bits_per_watt(), 0.6417571715841273, 1e-9)
    near("brane beats bulk by ~26.6 orders", brane_beats_bulk_orders(), 26.6, 2e-3)
    chk("O6's cause of death is refuted, and that is a narrowing",
        (O6_CAUSE_OF_DEATH_REFUTED, O6_CLOSED), (True, False))
    chk("the closing premise is NOT-FOUND", CLOSING_PREMISE_STATUS, "NOT-FOUND")
    chk("the dichotomy has two branches, one a closure", len(O6_DICHOTOMY), 2)

    print("\n3. O7 -- THE ARITHMETIC AT 50 DIGITS")
    exr = o7_exact(span_m=RULING_SPAN_M)
    for key, want in O7_FIXTURES:
        near("%s (the ruling's span, 4.017499e16 m)" % key, float(exr[key]),
             float(want), 1e-10)          # the ruling printed 10-12 digits
    ex = o7_exact()
    near("SEATED span: light time = 4.2465 Julian years exactly",
         float(ex["Proxima light time yr"]), foliation.PROXIMA_LY, 1e-15)
    near("SEATED span: Delta_tau = 93.80654 ns (agrees with the ruling to 5e-8)",
         float(ex["Delta_tau ns"]), float(exr["Delta_tau ns"]), 1e-7)
    near("fraction = d/(1+d) = 7.0e-16", float(ex["fraction"]), 7.0e-16, 1e-12)
    chk("W7's 1/beta = 2.6726124e7 vindicated to every printed digit",
        "%.7e" % float(ex["1/beta"]), "2.6726124e+07")
    nb, ns = o7_naive_double()
    chk("CONTROL: double precision DOES lose it -- beta 3.650024e-08",
        "%.6e" % nb, "3.650024e-08")
    chk("CONTROL: ... and 89.2682 ns (both WITHDRAWN)", "%.4f" % ns, "89.2682")
    near("provenance: T x 7e-16 = 9.3807e-08 s (GW170817)",
         float(ex["Proxima light time s"]) * D_GW, 9.3807e-08, 1e-4)
    near("the CMB dipole's Gamma - 1 is the receiver's B", cmb_gamma_minus_1(),
         7.6161e-07, 1e-4)
    near("escape: B for a one-second saving", b_for_saving(1.0), 0.999387630, 1e-9)
    near("escape: B for half the light time", b_for_saving(0.5 * L_PROXIMA / C),
         0.99999993, 1e-8)
    near("SME null |c| at r = 38.6 um, beta = 1", sme_coefficient(), 6.37e-64, 1e-3)
    chk("... 42 orders short of the 1e-21 bound",
        round(math.log10(SME_LAB_BOUND / sme_coefficient())), 42)
    chk("GW170817 bounds beta, not B -- B is not measured", B_MEASURED, False)
    chk("R-1 is not opened", R1_ROW_OPENED, False)
    chk("O7 is not closed", O7_CLOSED, False)

    print("\n4. S5 -- NOT SEATED")
    chk("the four figures are not MEASURED", S5_FIGURES_MEASURED, False)
    src = open(__file__).read()
    # joined at run time: a literal "a" + "b" is constant-folded into the .pyc,
    # and the grep this row relies on would then find it there.
    seed = "".join(["8.04", "1537", "e23"])
    chk("and the hard-coded seed does not appear in this file", seed in src, False)

    print("\n  SELFTEST %s" % ("OK" if ok else "FAILED"))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(selftest() if "--selftest" in sys.argv else report())
