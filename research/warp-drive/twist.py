#!/usr/bin/env python3
"""
twist.py -- what the 1+1D reduction throws away, and it is everything.

THE FINDING, IN ONE IDENTITY.  For the Alcubierre warp drive the Eulerian
energy density and the coordinate vorticity of the shift are the SAME OBJECT:

                        E  =  - Omega^2 / (8 pi G)

Negative energy is not a price paid alongside the transport.  It IS the twist,
squared.  A warp bubble with no twist has no exotic matter and no bubble --
Barzegar, Buchert and Vigneron prove exactly that (arXiv:2602.16495,
Theorem III.15): "Coordinate vorticity-free Alcubierre warp drive is Minkowski."

WHY THAT LANDS ON THIS PROJECT.  Smolyaninov's metamaterial mapping -- the one
device.py builds a parts list for -- is 1+1D.  He reduces to one spatial
dimension, in his words, "to avoid unnecessary mathematical complications."
But Omega^2 = (y^2+z^2)/(4 r_s^2) V_s^2 f'^2 vanishes identically when y = z = 0.

    THE 1+1D REDUCTION IS THE ON-AXIS LINE OF THE BUBBLE, AND ON THAT LINE THE
    ALCUBIERRE WARP DRIVE IS MINKOWSKI SPACE.

So the analogue was never emulating a warp drive weakly.  It was emulating flat
spacetime with a graded, non-reciprocal index -- exactly, and by construction.
The 2146 degrees of non-reciprocity device.py computed is a real material
property and a faithful measurement of the medium.  It is a measurement of
nothing about the metric, because on that line there is no metric content to
measure.  This is a stronger statement than RELABEL-ONLY (device.py TEST 17),
which said the observable was a relabel; this says the TARGET was flat.

-- THREE INDEPENDENT ROUTES TO THE SAME PLACE, ALL EXECUTED HERE -------------

(1) THE SHIFT IS GAUGE BELOW A HORIZON.  In 1+1D with v = v(x),
        ds^2 = -c^2 dt^2 + (dx - v dt)^2
    is diagonalised globally by  dT = dt + v dx/(c^2 - v^2):
        ds^2 = -(c^2 - v^2) dT^2 + c^2 dx^2/(c^2 - v^2).
    This is Painleve-Gullstrand -> static, the textbook move, and T is the
    tortoise time.  The integral defining T converges on every compact set iff
    |v| < c everywhere.  Where v crosses c transversally it diverges
    logarithmically, with coefficient 1/(2 v'(x_0)) -- measured here.
    So in 1+1D the ONLY non-gauge content of the metric is a horizon.

(2) THE TWIST IS A 3-FORM AND THERE IS NO ROOM FOR IT.  Irremovability of a
    shift is Frobenius: xi ^ dxi != 0.  That is a 3-form.  On a 2-manifold every
    3-form is identically zero, so in 1+1D every timelike xi is hypersurface-
    orthogonal -- a theorem of the DIMENSION, not of this metric.  In 3+1D,
        (xi ^ dxi)_{txy} = - v_s (1 + v_s^2 f^2) d_y f,
    derived here and checked against finite differences of the full
    antisymmetrised expression to 8 digits.  It vanishes on the axis
    (d_y f = f'(r_s) y/r_s) and peaks off-axis inside the wall.

(3) THE PUBLISHED THEOREM.  BBV's Omega (their Eq. 3.47c) and the wedge above
    are the same quantity: |xi ^ dxi|_{txy} = 2 (1 + v_s^2 f^2) Omega, verified
    here to ten digits at five off-axis points.  Their Eq. 3.48 then gives
    E = -Omega^2/(8 pi G) directly, which is the identity at the top.

-- AND A CORRECTION TO THIS PROJECT'S OWN READING OF TEST 16 ------------------
device.py TEST 16 found that Brown-Hornreich-Shtrikman stability forbids an
analogue horizon for every n, and this series read that as the wall the design
hit.  A HORIZON IS NOT A REQUIREMENT OF WARP TRANSPORT.  A forward-directed null
ray in bubble-comoving coordinates has dx'/dt = v_s(f - 1) + c, which vanishes
at f* = 1 - c/v_s.  That lies in the range of f only for v_s > c: computed here
across v_s = 0.5 .. 10.  The horizon is the signature of the SUPERLUMINAL case,
and it is a pathology, not a feature -- Krasnikov, and Everett and Roman, show
the crew cannot create, steer or stop the bubble from inside precisely because
of it.  A subluminal warp drive has no horizon and needs none.

So TEST 16 was arithmetically right and read the wrong way round: the analogue
declines to emulate the uncontrollable regime.  The wall is not the horizon.
The wall is (2): there is nothing on the axis to emulate.

WHAT WOULD FIX IT, STATED SO IT CAN BE COSTED.  A metamaterial analogue must be
at least 2+1D, with the shift graded TRANSVERSELY (d_y f != 0), before it can
carry any metric content beyond a graded index.  One encouraging number: the
twist peaks where f is mid-wall, and neclab.py's stability margin is a function
of f alone that is worst at f -> 1.  The two extrema are disjoint, exactly as
the NEC violation and the margin were.  Measured below.

-- SOURCES, PINNED ------------------------------------------------------------
Alcubierre M 1994 Class. Quantum Grav. 11 L73, shape function Eq. (7).
Barzegar H, Buchert T, Vigneron Q 2026 arXiv:2602.16495, Eqs (3.45)-(3.48),
    Theorem III.15.  (Also Errors 1-37; they report minor errors in Santiago-
    Schuster-Visser too, at their Errors 9 and 29.)
Smolyaninov I I 2011 Phys. Rev. B 84 113103 = arXiv:1009.5663 -- the 1+1D
    reduction, and the phrase quoted above.
Krasnikov S V 1998 Phys. Rev. D 57 4760; Everett A E, Roman T A 1997
    Phys. Rev. D 56 2100 -- the horizon/controllability problem.

stdlib only.  Every number below is computed, none transcribed.
"""
import math, sys

# -- Alcubierre's own shape function, Eq (7), and his parameters ---------------
VS_DEFAULT  = 0.9      # v_s/c for the geometry tests; subluminal on purpose
SIGMA       = 8.0      # wall steepness
RADIUS      = 1.0      # bubble radius
H           = 1.0e-6   # central-difference step
C           = 1.0      # geometric units throughout this file

def shape(rs, sigma=SIGMA, R=RADIUS):
    """Alcubierre Eq (7) / BBV Eq (3.45).  f(0)=1 inside, f->0 outside."""
    return ((math.tanh(sigma * (rs + R)) - math.tanh(sigma * (rs - R)))
            / (2.0 * math.tanh(sigma * R)))

def r_s(x, y, z=0.0):
    return math.sqrt(x * x + y * y + z * z)

def dshape_dr(rs, h=H):
    return (shape(rs + h) - shape(rs - h)) / (2.0 * h)

def dshape_dy(x, y, z=0.0, h=H):
    return (shape(r_s(x, y + h, z)) - shape(r_s(x, y - h, z))) / (2.0 * h)

# -- (1) the diagonalisation, and where it fails -------------------------------

def pg_identity_residual(v):
    """Do the substitution and compare coefficients -- do not assert them.

    dT = dt + A dx with A = v/(c^2-v^2).  Expanding
        -(c^2-v^2) dT^2  +  c^2 dx^2/(c^2-v^2)
    gives, coefficient by coefficient computed FROM A:
        dt^2  : -(c^2-v^2)
        dx dt : -2(c^2-v^2) A
        dx^2  : -(c^2-v^2) A^2 + c^2/(c^2-v^2)
    and the Painleve-Gullstrand form -c^2 dt^2 + (dx - v dt)^2 gives
        (-c^2 + v^2, -2v, 1).  Returns the largest mismatch."""
    c2 = C * C
    d = c2 - v * v
    A = v / d
    diag = (-d, -2.0 * d * A, -d * A * A + c2 / d)
    pg = (-c2 + v * v, -2.0 * v, 1.0)
    return max(abs(p - q) for p, q in zip(diag, pg))

def tortoise(u_of_x, x_hi, x_lo=0.0, steps=400000):
    """INTEGRAL u dx/(1-u^2), u = v/c.  Midpoint rule; c = 1."""
    h = (x_hi - x_lo) / steps
    s = 0.0
    for i in range(steps):
        x = x_lo + (i + 0.5) * h
        u = u_of_x(x)
        s += u / (1.0 - u * u) * h
    return s

def horizon_crossing(U):
    """u(x) = U tanh(x) crosses 1 at x_0 iff U > 1.  Returns (x_0, u'(x_0))."""
    if U <= 1.0:
        return None
    x0 = math.atanh(1.0 / U)
    return x0, U / math.cosh(x0) ** 2

def tortoise_divergence(U=1.5, eps_list=(1e-2, 1e-3, 1e-4, 1e-5)):
    """Near a transversal crossing 1-u^2 ~ 2u'(x_0)(x_0-x), so the integral to
    x_0-eps grows as -(1/(2u'))ln eps.  Returns [(eps, I)]."""
    x0, _ = horizon_crossing(U)
    u = lambda x: U * math.tanh(x)
    return [(e, tortoise(u, x0 - e)) for e in eps_list]

def divergence_slopes(rows):
    """MEASURE the rate rather than assume it.  Consecutive pairs give
    (I_2 - I_1)/ln(eps_1/eps_2), which must converge to 1/(2 u'(x_0))."""
    out = []
    for (e1, i1), (e2, i2) in zip(rows, rows[1:]):
        out.append((e1, e2, (i2 - i1) / math.log(e1 / e2)))
    return out

# -- (2) the twist, as a 3-form --------------------------------------------------

def xi_lower(x, y, z=0.0, vs=VS_DEFAULT):
    """xi = d/dt lowered: xi_mu = g_{mu t} = (-1 + v_s^2 f^2, -v_s f, 0, 0)."""
    f = shape(r_s(x, y, z))
    return [-C * C + vs * vs * f * f, -vs * f, 0.0, 0.0]

def _d(mu, nu, x, y, vs, h=H):
    """d_mu xi_nu.  x_s is fixed, so the configuration is static: d_t = 0.
    z = 0 is a symmetry plane, so d_z = 0 there."""
    if mu == 0 or mu == 3:
        return 0.0
    if mu == 1:
        return (xi_lower(x + h, y, 0.0, vs)[nu] - xi_lower(x - h, y, 0.0, vs)[nu]) / (2 * h)
    return (xi_lower(x, y + h, 0.0, vs)[nu] - xi_lower(x, y - h, 0.0, vs)[nu]) / (2 * h)

def wedge_txy_numeric(x, y, vs=VS_DEFAULT):
    """(xi ^ dxi)_{txy}, fully antisymmetrised, from finite differences."""
    X = xi_lower(x, y, 0.0, vs)
    return (X[0] * (_d(1, 2, x, y, vs) - _d(2, 1, x, y, vs))
            + X[1] * (_d(2, 0, x, y, vs) - _d(0, 2, x, y, vs))
            + X[2] * (_d(0, 1, x, y, vs) - _d(1, 0, x, y, vs)))

def wedge_txy_closed(x, y, vs=VS_DEFAULT):
    """The same, in closed form: -v_s (1 + v_s^2 f^2) d_y f."""
    f = shape(r_s(x, y))
    return -vs * (C * C + vs * vs * f * f) * dshape_dy(x, y)

def wedge_txy_1plus1d(x, vs=VS_DEFAULT):
    """A 3-form on a 2-manifold.  Not small: absent."""
    return 0.0

# -- (3) BBV's vorticity and energy density, and the identity ------------------

def omega_bbv(x, y, z=0.0, vs=VS_DEFAULT):
    """BBV Eq (3.47c): Omega^2 = (y^2+z^2)/(4 r_s^2) V_s^2 (f')^2."""
    r = r_s(x, y, z)
    return math.sqrt((y * y + z * z) / (4.0 * r * r)) * abs(vs * dshape_dr(r))

def energy_density_bbv(x, y, z=0.0, vs=VS_DEFAULT):
    """BBV Eq (3.48), G = 1: E = -(1/32 pi)(y^2+z^2)/r_s^2 V_s^2 (f')^2 <= 0."""
    r = r_s(x, y, z)
    return -(1.0 / (32.0 * math.pi)) * ((y * y + z * z) / (r * r)) \
        * vs * vs * dshape_dr(r) ** 2

def energy_from_twist(omega):
    """THE IDENTITY.  E = -Omega^2/(8 pi G), G = 1."""
    return -omega * omega / (8.0 * math.pi)

def wedge_over_omega(x, y, vs=VS_DEFAULT):
    """|xi ^ dxi|_{txy} / (2(1 + v_s^2 f^2) Omega) -- must be 1 off the axis."""
    f = shape(r_s(x, y))
    o = omega_bbv(x, y, 0.0, vs)
    if o == 0.0:
        return None
    return abs(wedge_txy_closed(x, y, vs)) / (2.0 * (C * C + vs * vs * f * f) * o)

# -- the horizon, and whether anything needs one -------------------------------

def horizon_shape_value(vs):
    """A forward null ray in bubble-comoving coordinates has
    dx'/dt = v_s(f - 1) + c, zero at f* = 1 - c/v_s.  f takes values in [0,1],
    so a horizon exists iff 0 <= f* < 1, i.e. iff v_s >= c."""
    return 1.0 - C / vs

def has_horizon(vs):
    fstar = horizon_shape_value(vs)
    return 0.0 <= fstar < 1.0

# -- does the twist demand what the medium cannot spare? ------------------------

def twist_peak_f(vs=VS_DEFAULT, y=0.3, xmax=2.5, steps=40000):
    """Scan x at fixed off-axis y; return (x, f, |wedge|) at the twist maximum.
    The question is which VALUE OF f the twist demands, because neclab.py's
    stability margin is a function of f alone."""
    best = (0.0, 0.0, -1.0)
    for i in range(steps):
        x = -xmax + 2.0 * xmax * i / (steps - 1)
        w = abs(wedge_txy_closed(x, y, vs))
        if w > best[2]:
            best = (x, shape(r_s(x, y)), w)
    return best

def margin_at_twist_peak(n=2.0, beta=None, y=0.3):
    """neclab's stability margin evaluated at the f where the twist peaks,
    against the margin at f -> 1 where the medium is worst off."""
    import neclab
    if beta is None:
        beta = neclab.beta_max_exact(n)
    _, f_pk, _ = twist_peak_f(y=y)
    return f_pk, neclab.margin(n, beta, f_pk), neclab.margin(n, beta, 1.0)

# -- selftest ------------------------------------------------------------------

OFF_AXIS = [(0.9, 0.3), (1.0, 0.2), (1.05, 0.5), (0.5, 0.5), (0.0, 1.0)]
ON_AXIS  = [(0.9, 0.0), (1.0, 0.0), (0.5, 0.0), (1.2, 0.0)]

def selftest():
    ok = True
    def chk(label, got, want, tol=None):
        nonlocal ok
        good = (abs(got - want) <= tol) if tol is not None else (got == want)
        ok &= good
        g = ("%.10g" % got) if isinstance(got, float) else str(got)
        w = ("%.10g" % want) if isinstance(want, float) else str(want)
        print("  %-56s %16s %16s  %s" % (label, g, w, "ok" if good else "FAIL"))

    print("(1) the Painleve-Gullstrand diagonalisation is an exact identity")
    for v in (0.1, 0.25, 0.4, 0.49, 0.9):
        chk("coefficient residual at v = %.2f" % v, pg_identity_residual(v), 0.0, 0.0)

    print("\n    ...and T is global iff there is no horizon")
    chk("u = 0.8 tanh x never crosses 1", horizon_crossing(0.8), None)
    x0, up = horizon_crossing(1.5)
    chk("u = 1.5 tanh x crosses at x_0", x0, math.atanh(1.0 / 1.5), 1e-12)
    chk("  with slope u'(x_0) = 1.5 sech^2 x_0", up, 1.5 * (1.0 - (1.0 / 1.5) ** 2), 1e-12)
    rows = tortoise_divergence()
    k = 1.0 / (2.0 * up)
    print("      eps        I(eps)")
    for e, I in rows:
        print("      %.0e  %12.6f" % (e, I))
    chk("I grows without bound as eps -> 0", rows[-1][1] > rows[0][1] + 4.0, True)
    print("      measured log rate, per decade:")
    slopes = divergence_slopes(rows)
    for e1, e2, sl in slopes:
        print("        %.0e -> %.0e   %.6f   (predicted 1/(2u') = %.6f)" % (e1, e2, sl, k))
    chk("every measured rate matches 1/(2u'(x_0))",
        max(abs(sl - k) for _, _, sl in slopes), 0.0, 5e-3)
    chk("...and it converges: the last rate is sharper", abs(slopes[-1][2] - k), 0.0, 1e-3)
    # a subluminal profile has no singularity on any compact set
    fin = tortoise(lambda x: 0.8 * math.tanh(x), x0)
    chk("subluminal integral over the same interval is finite", math.isfinite(fin), True)

    print("\n(2) the twist: closed form against finite differences of the 3-form")
    worst = 0.0
    for (x, y) in OFF_AXIS:
        d = abs(wedge_txy_numeric(x, y) - wedge_txy_closed(x, y))
        worst = max(worst, d)
    chk("max |numeric - closed| over 5 off-axis points", worst, 0.0, 1e-7)
    chk("the twist is NONZERO off axis", all(abs(wedge_txy_closed(x, y)) > 1e-3
                                             for x, y in OFF_AXIS), True)
    chk("the twist VANISHES on the axis", all(abs(wedge_txy_closed(x, y)) < 1e-12
                                              for x, y in ON_AXIS), True)
    chk("a 3-form on a 2-manifold is identically zero",
        all(wedge_txy_1plus1d(x) == 0.0 for x, _ in OFF_AXIS + ON_AXIS), True)

    print("\n(3) BBV correspondence: the wedge IS the coordinate vorticity")
    for (x, y) in OFF_AXIS:
        chk("  ratio at (%.2f, %.2f)" % (x, y), wedge_over_omega(x, y), 1.0, 1e-8)
    chk("undefined on the axis (both zero)", wedge_over_omega(0.9, 0.0), None)

    print("\n    THE IDENTITY:  E = -Omega^2/(8 pi G)")
    for (x, y) in OFF_AXIS:
        e1 = energy_density_bbv(x, y)
        e2 = energy_from_twist(omega_bbv(x, y))
        chk("  at (%.2f, %.2f)" % (x, y), e1, e2, 1e-14)
    chk("E <= 0 everywhere (exotic matter is forced)",
        all(energy_density_bbv(x, y) <= 0.0 for x, y in OFF_AXIS + ON_AXIS), True)

    print("\n    BBV Theorem III.15: no vorticity => Minkowski")
    chk("on the axis Omega = 0", all(omega_bbv(x, y) == 0.0 for x, y in ON_AXIS), True)
    chk("...and therefore E = 0 there", all(energy_density_bbv(x, y) == 0.0
                                            for x, y in ON_AXIS), True)
    print("      1+1D keeps y = z = 0 exactly, so the emulated geometry is FLAT.")

    print("\n(4) a horizon exists iff the drive is superluminal")
    for vs, want in ((0.5, False), (0.9, False), (0.99, False),
                     (1.0, True), (1.5, True), (2.0, True), (10.0, True)):
        chk("  v_s = %5.2f c has a horizon" % vs, has_horizon(vs), want)
    chk("f* = 1 - c/v_s at v_s = 2", horizon_shape_value(2.0), 0.5, 1e-15)
    chk("f* -> 1 as v_s -> infinity", horizon_shape_value(1e12), 1.0, 1e-11)

    print("\n(5) where the twist asks, does the medium have margin? (neclab)")
    try:
        f_pk, m_pk, m_worst = margin_at_twist_peak()
        print("      f at the twist peak            %.6f" % f_pk)
        print("      neclab margin there            %+.6f" % m_pk)
        print("      neclab margin at f -> 1        %+.6f" % m_worst)
        chk("the twist peak is not where the medium is worst", m_pk > m_worst, True)
        chk("the medium has margin in hand where the twist peaks", m_pk > 0.0, True)
    except Exception as exc:                      # pragma: no cover
        print("      neclab unavailable: %s" % exc)
        ok = False

    print("\n  SELFTEST %s" % ("OK" if ok else "FAILED"))
    return 0 if ok else 1

def report():
    print(__doc__)
    print("=" * 79)
    print("MEASURED\n")
    x, f_pk, w = twist_peak_f()
    print("  Alcubierre f, sigma = %.1f, R = %.1f, v_s = %.2f c" % (SIGMA, RADIUS, VS_DEFAULT))
    print("  twist peak at y = 0.30:  x = %+.5f, f = %.6f, |xi^dxi| = %.6f" % (x, f_pk, w))
    print("  on the axis:             |xi^dxi| = 0, Omega = 0, E = 0  (Minkowski)")
    print()
    print("  %-14s %14s %14s %16s" % ("point", "Omega", "E (BBV 3.48)", "-Omega^2/8piG"))
    for (px, py) in ON_AXIS[:1] + OFF_AXIS:
        o = omega_bbv(px, py)
        print("  (%5.2f,%5.2f) %14.8f %14.6e %16.6e"
              % (px, py, o, energy_density_bbv(px, py), energy_from_twist(o)))
    print()
    print("  horizon: f* = 1 - c/v_s in [0,1) iff v_s >= c")
    for vs in (0.5, 0.9, 1.0, 2.0, 10.0):
        print("    v_s = %5.2f c   f* = %+8.4f   %s"
              % (vs, horizon_shape_value(vs), "HORIZON" if has_horizon(vs) else "none"))
    print()
    print("  VERDICT: the metamaterial analogue must be at least 2+1D with a")
    print("  transverse gradient d_y f != 0.  In 1+1D there is nothing to emulate:")
    print("  E = -Omega^2/(8 pi G), and on the axis both sides are zero.")
    return 0

if __name__ == "__main__":
    sys.exit(selftest() if "--selftest" in sys.argv else report())
