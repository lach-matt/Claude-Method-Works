#!/usr/bin/env python3
r"""
throatmass.py -- O5: SELF-CONSISTENCY.  OPEN, UNCHANGED.  NARROWED, ONE NARROWING DEMOTED.

DOCKET 62's O5 pass is the one status move of that docket the ruling accepted as
proposed: nothing closed, nothing withdrawn, nothing opened.  Its figures lived in
/tmp/o5work.  This file seats what the ruling kept, grades what it graded down,
and DEMOTES the narrowing it refuted.  It is deliberately small: the ruling said
record, do not over-seat.

    python3 throatmass.py             the reading
    python3 throatmass.py --selftest  sympy; a few seconds

===============================================================================
1. WHAT IS SEATED
===============================================================================

(1) THE THROAT MASS, AND THE SERIES RESULT THAT IS THE REAL CONTENT.  In the
    proper-distance gauge ds^2 = -f dt^2 + dl^2 + r(l)^2 dOmega^2 (HPS eq. (2)),
    g^{ll} = 1, so the Misner-Sharp mass is m(l) = (r/2)(1 - r'(l)^2).  Verified
    here: G^t_t = (2 r r'' + r'^2 - 1)/r^2 (HPS eq. (5)'s left side) and
    dm/dl = 4 pi r^2 r' rho, both residuals exactly 0.  So m < 0 iff |r'| > 1, and
    a THROAT (r' = 0, r = r_0 > 0) has m = r_0/2 > 0 exactly.
      GRADED DOWN BY THE RULING: that line is a one-substitution consequence of a
      standard definition.  THE NEW CONTENT is the series: m'(0) = 0 and
      m''(0) = a(1 - 2 r_0 a)/2, a = r''(0), from a Taylor expansion (sympy, not
      by hand) -- and HPS's own eq. (9) sets r''(0) = 0, so m == r_0/2 > 0
      through second order on the one solution with printed boundary data.

(2) THE SCALE LEDGER, with HPS's two figures REPRODUCED from their own quartic
    eq. (8) rather than quoted.  K^2 = 1/(5760 pi).  With f''(0) = r''(0) = 0 and
    ln f(0) = -2/3 it collapses to K^-2 r_0^2 + 16 ln f(0) = 0, r_0 =
    sqrt(15)/(90 sqrt(pi)) = 0.02428 l_P (printed "~0.02").  With f(0) = f''(0) = 1
    it collapses to -4 r_0^4 + K^-2 r_0^2 = 0, r_0 = 1/(2K) = 12 sqrt(10 pi) =
    67.2599 l_P (printed "~67").  Eq. (8) is as transcribed by the O5 pass, which
    read HPS at source.  The largest self-consistent throat anyone has built is
    HPS's quoted 300 l_P = 4.849e-33 m, 32.31 orders below one metre of corridor
    and 48.92 below the Proxima span.

(3) NOT-FOUND, WITH ONE COMPUTED CONTROL AND ONE READ CONTROL.  No
    self-consistent semiclassical solution with m(r) < 0 or negative ADM mass,
    and no theorem forbidding one.  NOT-FOUND, not NO.
    Control 1, COMPUTED (sympy, --selftest section 5): m < 0 IS realised in the
    metric class, by Reissner-Nordstrom, m = M - Q^2/(2r), with rho =
    Q^2/(8 pi r^4) STRICTLY POSITIVE -- because m(0) = -infinity; that is D4's
    regular-centre hypothesis earning its place (index3.py's prior finding,
    cited as control, NOT re-claimed).  This is the only control here that is
    computed.
    Control 2, READ: the same search returned self-consistent families, so the
    zero is a measurement and not a dead search.  The families are seated
    below as SELF_CONSISTENT_FAMILIES -- citation, how the pass reached each,
    and whether it reports m < 0 -- transcribed from the DOCKET 62 O5 pass's
    output in the docket's workflow journal.  Both counts (families returned,
    families with m < 0) are DERIVED from that list, not typed; the list itself
    is READ data and no computation here can move it.  The three throats'
    signs are cross-checked in --selftest against the computed throat mass
    r_0/2 at each READ r_0.  SCOPE, as the docket's adversarial reading put it:
    this control shows the search returns SOLUTIONS; it does not show the search
    could surface a NO-GO theorem if one existed, so it backs the first zero
    (no m < 0 solution) and not the second (no no-go found).

(4) HYPOTHESIS DISCIPLINE, KEPT.  Flanagan-Wald is NOT applied: h ~ 0.5 at the
    core surface makes eps ~ O(1) and their one-parameter perturbative family
    hypothesis fails.  Sanders' Theorem 5.1 is NOT applied: his class is
    ultrastatic with compact maximally symmetric slices.  Failure mode (4)
    declined in the open, twice.

(5) AN EXPULSION IS WORSE THAN A NO-GO.  If Flanagan-Wald, Anderson-Molina-
    Paris-Mottola and Kontou are right that eps ~ 1 lies outside semiclassical
    gravity's domain, the corridor is not refuted -- it is placed beyond the
    theory's jurisdiction.  A no-go names a hypothesis to attack; an expulsion
    names nothing.

===============================================================================
2. WHAT IS DEMOTED
===============================================================================

The pass stated, as a THEOREM, that "no QEI in this family CAN bound rho_ren"
and that this "separates O5 from O2 permanently".  REFUTED AT SOURCE by the
ruling: Fewster & Smith, gr-qc/0702056 eq. (5), bound INT f^2 <v^a v^b T^ren_ab>
directly, from local geometry alone, with no reference state, for the minimally
coupled Klein-Gordon field on any four-dimensional globally hyperbolic spacetime
-- a class containing the corridor.  What survives is the weaker sentence: the
FEWSTER-TEO bound (normal-ordered against the static vacuum, on which
<0|:T:|0> = 0 identically) does not bound it.  The renormalisation gap is real but
narrow: F&S's flat massless limit (their eq. (88)) has the same form and constant,
and the residual freedom is C_ab, a state-independent conserved local curvature
term that vanishes in Minkowski.  Not a free-floating unknown.

===============================================================================
3. WHAT WOULD ANSWER IT
===============================================================================

Re-integrate HPS's printed fourth-order system with REGULAR-CENTRE data r(0) = 0,
r'(0) = 1, f'(0) = 0 in place of throat data -- after re-deriving their eq. (8)
constraint, which assumes r'(0) = 0 and does not hold at a centre -- and ask
whether r'(l) ever exceeds 1.  Read Anderson-Hiscock-Samuel PRD 51 4337 first.
Closed only by a general existence theorem for the static spherically symmetric
asymptotically flat class, which nobody has.  NOT DONE HERE.
"""

import math
import sys

import achievable
import foliation

# ---------------------------------------------------------------------------
# The ruling, as data.
# ---------------------------------------------------------------------------

O5_STATUS = "OPEN -- unchanged (accepted as proposed)"
O5_CLOSED = False

THROAT_MASS = "r_0/2 > 0, exactly"                  # one substitution
THROAT_MASS_GRADE = "consequence of a standard definition -- not the lead result"
SERIES_RESULT = "m'(0) = 0, m''(0) = a(1 - 2 r_0 a)/2, a = r''(0)"
SERIES_RESULT_STATUS = "THEOREM (Taylor series, sympy)"

NO_GO_FOR_NEGATIVE_MASS_FOUND = "NOT-FOUND"

#: Control 2, READ.  The self-consistent solution families the DOCKET 62 O5
#: pass's search returned, transcribed from its output (the "SIX FAMILIES
#: RETURNED" block of the docket's workflow journal).  Fields:
#:   (label, citation, how the pass reached it, is-a-throat, m < 0 reported,
#:    READ r_0 values in l_P for a throat, basis of the sign as the pass gave it)
#: "m < 0 reported" is the pass's tally ("solutions found with m(r) < 0
#: anywhere : 0") applied per family; it is READ, never computed here.
SELF_CONSISTENT_FAMILIES = (
    ("Hochberg-Popov-Sushkov", "gr-qc/9701064, PRL 78, 2050 (1997)",
     "CITED, read in full at source", True, False, (0.02428, 300.0),
     "throat: m = r_0/2 > 0 at the throat; HPS eq. (9) sets r''(0) = 0; the "
     "flare-region profile is not reported (NOT-FOUND)"),
    ("Khusnutdinov-Sushkov", "hep-th/0202068, PRD 65, 084028 (2002)",
     "CITED", True, False, (0.0141,),
     "throat (short-throat flat-space wormhole): m = r_0/2 > 0 at the throat"),
    ("Garattini", "gr-qc/0501105, CQG 22, 1105 (2005)",
     "CITED", True, False, (1.158822606, 0.4473670842),
     "throat (graviton one loop): m = r_0/2 > 0 at the throat"),
    ("Abdolrahimi-Page-Tzounis", "1607.05280, PRD 100, 124038",
     "RECOVERED (seated in selfconsistent.py, not re-read)", False, False, (),
     "evaporating Schwarzschild, first order in hbar: not static, not m < 0"),
    ("Sanders", "2007.14311, Ann. Henri Poincare 23, 1321 (2022)",
     "CITED, read at source", False, False, (),
     "Einstein static universe R x S^3: covered by the pass's tally only "
     "(m(r) < 0 anywhere: 0); no per-family sign printed"),
    ("Pinamonti / Pinamonti-Siemssen / Meda-Pinamonti-Siemssen / "
     "Gottschalk-Siemssen", "2011, 2015, 2020, 2021",
     "RECOVERED from bibliographies, not read at source", False, False, (),
     "flat FLRW existence by Banach fixed point: cosmological, not static, "
     "not m < 0"),
)

# DERIVED from the list above -- the counts ledger.py prints.
SELF_CONSISTENT_FAMILIES_RETURNED = len(SELF_CONSISTENT_FAMILIES)
FAMILIES_WITH_NEGATIVE_MASS = sum(1 for f in SELF_CONSISTENT_FAMILIES if f[4])
THROAT_FAMILIES = sum(1 for f in SELF_CONSISTENT_FAMILIES if f[3])
NEGATIVE_MASS_SELF_CONSISTENT_FOUND = (
    "NOT-FOUND" if FAMILIES_WITH_NEGATIVE_MASS == 0 else "FOUND")   # not NO

FLANAGAN_WALD_APPLIED = False     # eps ~ O(1): their perturbative hypothesis fails
SANDERS_51_APPLIED = False        # ultrastatic, compact, maximally symmetric only
EXPULSION_WORSE_THAN_NO_GO = True

#: Section 2.  The pass's narrowing #3, demoted from THEOREM.
NO_QEI_CAN_BOUND_RHO_REN = False
NARROWING_3_STATUS = ("DEMOTED -- the FEWSTER-TEO bound does not bound rho_ren; "
                      "Fewster & Smith gr-qc/0702056's absolute QEI does, on a "
                      "class containing the corridor")
SEPARATES_O5_FROM_O2_PERMANENTLY = False

O5_ANSWERED_BY = ("HPS's fourth-order system re-integrated with regular-centre "
                  "data r(0)=0, r'(0)=1, f'(0)=0 after re-deriving their eq. (8) "
                  "(which assumes r'(0)=0): does r'(l) ever exceed 1?  Closed "
                  "only by an existence theorem for the static spherically "
                  "symmetric asymptotically flat class")

#: r_0 in Planck lengths, READ by the O5 pass from the papers named.  The two
#: HPS quartic figures are NOT here: they are computed by hps_quartic().
LITERATURE_THROATS = (
    ("Khusnutdinov-Sushkov 2002, xi = 1/6 minimum", 0.0141),
    ("Garattini 2005, graviton one loop, mu_0 = Planck scale", 0.4473670842),
    ("Garattini 2005, graviton one loop, G_0(mu_0) = l_P^2", 1.158822606),
    ("Hochberg-Popov-Sushkov 1997, largest quoted (horizons far out)", 300.0),
)


def planck_length():
    """sqrt(hbar G / c^3), from achievable.py's constants -- computed."""
    return math.sqrt(achievable.HBAR * achievable.G_SI / achievable.C_SI ** 3)


def largest_throat_m():
    return max(x for _l, x in LITERATURE_THROATS) * planck_length()


def orders_short(length_m):
    return math.log10(length_m / largest_throat_m())


# COMPUTED AT IMPORT, stdlib, for ledger.py.
LARGEST_THROAT_M = largest_throat_m()
ORDERS_SHORT_OF_ONE_METRE = orders_short(1.0)
ORDERS_SHORT_OF_PROXIMA = orders_short(foliation.proxima_span_m())


# ============================================================ symbolic
def misner_sharp(sp):
    """G^t_t in the HPS gauge from the metric, and the two residuals."""
    l = sp.Symbol('l', real=True)
    t, th, ph = sp.symbols('t theta phi', real=True)
    r = sp.Function('r')(l)
    f = sp.Function('f')(l)
    x = [t, l, th, ph]
    g = sp.diag(-f, 1, r ** 2, r ** 2 * sp.sin(th) ** 2)
    gi = g.inv()
    n = 4
    Gam = [[[sp.simplify(sum(gi[a, d] * (sp.diff(g[d, b], x[c]) + sp.diff(g[d, c], x[b])
                                         - sp.diff(g[b, c], x[d])) for d in range(n)) / 2)
             for c in range(n)] for b in range(n)] for a in range(n)]
    Ric = sp.zeros(n)
    for b in range(n):
        for c in range(n):
            e = 0
            for a in range(n):
                e += sp.diff(Gam[a][b][c], x[a]) - sp.diff(Gam[a][b][a], x[c])
                for d in range(n):
                    e += Gam[a][a][d] * Gam[d][b][c] - Gam[a][c][d] * Gam[d][b][a]
            Ric[b, c] = sp.simplify(e)
    Rs = sp.simplify(sum(gi[i, j] * Ric[i, j] for i in range(n) for j in range(n)))
    Gtt = sp.simplify((gi * (Ric - Rs * g / 2))[0, 0])
    rp, rpp = sp.diff(r, l), sp.diff(r, l, 2)
    hps5 = 2 * rpp / r + rp ** 2 / r ** 2 - 1 / r ** 2
    m = r * (1 - rp ** 2) / 2
    rho = -Gtt / (8 * sp.pi)
    r0 = sp.Symbol('r_0', positive=True)
    return (sp.simplify(Gtt - hps5),
            sp.simplify(sp.diff(m, l) - 4 * sp.pi * r ** 2 * rp * rho),
            sp.simplify(m.subs(sp.Derivative(r, l), 0).subs(r, r0) - r0 / 2))


def throat_series(sp):
    """m(l) about an even throat r = r_0 + a l^2/2 + c l^4/24: (m(0), m'(0), m''(0))."""
    l, r0, a, c = sp.symbols('l r_0 a c', real=True)
    r = r0 + a * l ** 2 / 2 + c * l ** 4 / 24
    m = sp.expand(r * (1 - sp.diff(r, l) ** 2) / 2)
    ser = sp.series(m, l, 0, 5).removeO()
    return (sp.simplify(ser.coeff(l, 0) - r0 / 2),
            sp.simplify(sp.diff(ser, l).subs(l, 0)),
            sp.simplify(sp.diff(ser, l, 2).subs(l, 0) - a * (1 - 2 * r0 * a) / 2))


def hps_quartic(sp):
    """HPS eq. (8) at l = 0 with r'(0) = f'(0) = 0, K^2 = 1/(5760 pi), as the O5
    pass transcribed it; the two printed cases.  Returns exact r_0 values."""
    r0 = sp.Symbol('r_0', positive=True)
    K2 = sp.Rational(1, 5760) / sp.pi
    f0, fpp, rpp = sp.symbols('f_0 fpp rpp', real=True)
    L = sp.log(f0)
    quart = (-4 * (fpp / f0) ** 2 * (1 + L) * r0 ** 4 + 32 * (fpp * rpp / f0) * (1 + L / 2) * r0 ** 3
             + (1 / K2 - 16 * rpp ** 2 * L) * r0 ** 2 + 16 * L)
    c1 = quart.subs({fpp: 0, rpp: 0, f0: sp.exp(sp.Rational(-2, 3))})
    c2 = quart.subs({f0: 1, fpp: 1, rpp: 0})
    s1 = [s for s in sp.solve(sp.Eq(c1, 0), r0) if s.is_positive]
    s2 = [s for s in sp.solve(sp.Eq(sp.simplify(c2), 0), r0) if s.is_positive]
    return s1, s2


def rn_control(sp):
    """Reissner-Nordstrom: m < 0 near the centre with rho > 0 -- the control."""
    r, M, Q = sp.symbols('r M Q', positive=True)
    m = M - Q ** 2 / (2 * r)
    rho = Q ** 2 / (8 * sp.pi * r ** 4)
    return (sp.simplify(sp.diff(m, r) - 4 * sp.pi * r ** 2 * rho),
            sp.solve(sp.Eq(m, 0), r)[0], sp.limit(m, r, 0, '+'))


# ============================================================ report / selftest
def report():
    print(__doc__.split("=====", 1)[0].strip())
    lp = planck_length()
    print("\nl_P = %.6e m" % lp)
    print("largest self-consistent throat: %.4e m -- %.2f orders below 1 m, %.2f "
          "below the Proxima span" % (largest_throat_m(), orders_short(1.0),
                                      orders_short(foliation.proxima_span_m())))
    print("\nO5: %s" % O5_STATUS)
    print("NARROWING 3: %s" % NARROWING_3_STATUS)
    print("ANSWERED BY: %s" % O5_ANSWERED_BY)
    return 0


def selftest():
    ok = True

    def chk(label, got, want):
        nonlocal ok
        good = got == want
        ok &= good
        print("  [%s] %-60s %s" % ("ok" if good else "XX", label,
                                   got if good else "%s != %s" % (got, want)))

    def near(label, got, want, tol):
        nonlocal ok
        d = abs(got - want) / max(1e-300, abs(want))
        good = d <= tol
        ok &= good
        print("  [%s] %-60s %.10g (rel %.1e)" % ("ok" if good else "XX", label, got, d))

    try:
        import sympy as sp
    except ImportError as exc:                       # pragma: no cover
        raise SystemExit("throatmass.py --selftest needs sympy: %s" % exc)

    print("1. THE MISNER-SHARP MASS IN THE HPS GAUGE (sympy, from the metric)")
    a, b, c = misner_sharp(sp)
    chk("G^t_t - HPS eq. (5) left side", a, 0)
    chk("dm/dl - 4 pi r^2 r' rho", b, 0)
    chk("throat (r' = 0, r = r_0): m - r_0/2", c, 0)

    print("\n2. THE SERIES RESULT -- THE NEW CONTENT")
    m0, m1, m2 = throat_series(sp)
    chk("m(0) - r_0/2", m0, 0)
    chk("m'(0)", m1, 0)
    chk("m''(0) - a(1 - 2 r_0 a)/2", m2, 0)

    print("\n3. HPS's TWO FIGURES, REPRODUCED FROM THEIR OWN QUARTIC")
    s1, s2 = hps_quartic(sp)
    chk("case 1 root is sqrt(15)/(90 sqrt(pi))",
        sp.simplify(s1[0] - sp.sqrt(15) / (90 * sp.sqrt(sp.pi))) == 0, True)
    near("  = 0.02428 l_P (printed ~0.02)", float(s1[0]), 0.02428, 1e-3)
    chk("case 2 root is 12 sqrt(10 pi)",
        sp.simplify(s2[0] - 12 * sp.sqrt(10 * sp.pi)) == 0, True)
    near("  = 67.2599 l_P (printed ~67)", float(s2[0]), 67.25989459677514, 1e-12)

    print("\n4. THE SCALE LEDGER")
    near("l_P computed = achievable.L_PLANCK", planck_length(), achievable.L_PLANCK, 1e-6)
    near("largest throat: 300 l_P in metres", largest_throat_m(), 4.849e-33, 1e-3)
    near("orders short of one metre", orders_short(1.0), 32.31, 1e-3)
    near("orders short of the Proxima span", orders_short(foliation.proxima_span_m()),
         48.92, 1e-3)

    print("\n5. CONTROL 1 (COMPUTED) AND CONTROL 2 (READ)")
    res, rz, m0lim = rn_control(sp)
    chk("RN: m' - 4 pi r^2 rho (so rho = Q^2/8 pi r^4 > 0 sources it)", res, 0)
    chk("RN: m < 0 for r < Q^2/(2M)", rz, sp.Symbol('Q', positive=True) ** 2
        / (2 * sp.Symbol('M', positive=True)))
    chk("RN: m(0+) = -oo -- not a regular centre", m0lim, -sp.oo)
    # Control 2 is READ data: these rows re-derive the counts from the list and
    # cross-check it against computation where computation reaches (the throats).
    chk("control 2 (READ): the search returned a non-empty family list",
        len(SELF_CONSISTENT_FAMILIES) > 0, True)
    chk("  RECORD PIN: the transcribed list holds the ruling's 'six families'",
        SELF_CONSISTENT_FAMILIES_RETURNED, 6)
    chk("  RECORD PIN: 'NOT ONE has m(r) < 0' -- NOT-FOUND, not NO",
        (FAMILIES_WITH_NEGATIVE_MASS, NEGATIVE_MASS_SELF_CONSISTENT_FOUND),
        (0, "NOT-FOUND"))
    # Where computation reaches the READ list: section 1's residual c is
    # m_throat - r_0/2 computed from the metric, so m_throat = r_0/2 + c; its
    # sign at every READ throat radius must match the READ "m < 0 reported".
    r0s = sp.Symbol('r_0', positive=True)
    agree = all(bool(((r0s / 2 + c).subs(r0s, sp.Float(x)) < 0) == f[4])
                for f in SELF_CONSISTENT_FAMILIES if f[3] for x in f[5])
    chk("  every READ throat r_0 gives computed m_throat > 0, as READ",
        agree and all(f[5] for f in SELF_CONSISTENT_FAMILIES if f[3]), True)
    chk("  each READ throat r_0 is in the scale ledger or the HPS quartic",
        all(any(abs(x - y) <= 1e-3 * y for y in
                [v for _l, v in LITERATURE_THROATS] + [float(s1[0]), float(s2[0])])
            for f in SELF_CONSISTENT_FAMILIES if f[3] for x in f[5]), True)

    print("\n6. THE DEMOTION AND THE ROW")
    chk("'no QEI can bound rho_ren' is refuted (Fewster & Smith)", NO_QEI_CAN_BOUND_RHO_REN, False)
    chk("O5 is not separated from O2 permanently", SEPARATES_O5_FROM_O2_PERMANENTLY, False)
    chk("Flanagan-Wald not applied; Sanders 5.1 not applied",
        (FLANAGAN_WALD_APPLIED, SANDERS_51_APPLIED), (False, False))
    chk("O5 is not closed", O5_CLOSED, False)

    print("\n  SELFTEST %s" % ("OK" if ok else "FAILED"))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(selftest() if "--selftest" in sys.argv else report())
