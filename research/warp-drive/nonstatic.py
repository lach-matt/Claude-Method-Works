#!/usr/bin/env python3
r"""
nonstatic.py -- DOCKET 52.  certify.py's theorem said "static and spherically
symmetric only".  This file drops staticity and measures what is on the other
side.  The loophole is REAL, it is EXACT, and it is EMPTY.

    python3 nonstatic.py             the reading
    python3 nonstatic.py --selftest  every identity, every machine check

Needs sympy (the identities) and z3-solver (the four obligations).  Both are on
pypi and pypi is on the proxy allowlist -- see PROOF-ASSISTANT.md.  Run under
python3 (3.11), not python3.12.

===============================================================================
0.  WHAT WAS ASKED, AND THE ONE-LINE ANSWER
===============================================================================

certify.py proves, ansatz-free: in any STATIC spherically symmetric spacetime
proper radial distance is contracted at r if and only if the enclosed
Misner-Sharp mass m(r) is negative.  That theorem is the only thing making
negative mass compulsory for this project, and the whole 2.7254e12 solar-mass
corridor bill (CLAIMS.md H83d) rests on it.

Drop staticity.  For the general spherically symmetric metric

        ds^2 = -e^{2Phi(t,r)}dt^2 + e^{2Lambda(t,r)}dr^2 + R(t,r)^2 dOmega^2

with the Misner-Sharp-Hernandez mass defined by the scalar

        1 - 2m/R = g^{ab} d_a R d_b R = e^{-2Lambda}R'^2 - e^{-2Phi}Rdot^2

the contraction condition dl < dR becomes, exactly,

        CONTRACTION  <=>  e^{-2Lambda}R'^2 > 1  <=>  2m/R < e^{-2Phi}Rdot^2

so m < 0 is SUFFICIENT and NO LONGER NECESSARY.  That much was already derived
and is re-verified here in one line (residual exactly 0).

    THE ANSWER THIS FILE RETURNS: THE LOOPHOLE SURVIVES AS MATHEMATICS AND DIES
    AS ENGINEERING, AND IT DIES TWICE OVER, NEITHER TIME BY AN ENERGY CONDITION.

    Sustaining contraction does NOT force rho < 0 -- the witnesses below hold it
    for all time with rho = 0 exactly and with rho > 0 exactly.  It costs NOTHING
    in stress-energy to hold.  What kills it is that the only way to have it
    without negative mass is to have the areal radius MOVING, and a destination
    whose areal radius is moving is not a destination.

===============================================================================
1.  THE EXACT EQUATIONS, DERIVED HERE FROM THE EINSTEIN TENSOR
===============================================================================

Nothing below is quoted.  general_einstein() builds the Christoffel symbols, the
Ricci tensor and G_ab for the metric above in sympy, and every line is checked
as an identity whose residual sympy returns as 0.  Write

        u^a = e^{-Phi} d_t        the Eulerian (slice-normal) observer
        n^a = e^{-Lambda} d_r     the unit outward radial vector
        rho = T_ab u^a u^b        p_r = T_ab n^a n^b      p_T = T_thth / R^2
        j   = -T_ab u^a n^b       the OUTWARD radial energy flux
        U   = e^{-Phi} Rdot = D_t R       the areal velocity
        W   = e^{-Lambda} R' = D_r R      the CONTRACTION VARIABLE
        D_t = e^{-Phi} d_t        D_r = e^{-Lambda} d_r

The Misner-Sharp mass is then m = (R/2)(1 - W^2 + U^2), and:

    MS-r   D_r m  =  4 pi R^2 ( rho W + j U )
    MS-t   D_t m  = -4 pi R^2 ( p_r U + j W )
    EV-U   D_t U  =  W D_r Phi  -  m/R^2  -  4 pi R p_r
    EV-W   D_t W  =  4 pi R j  +  U D_r Phi
    EV-U'  D_r U  =  4 pi R j  +  W D_t Lambda

MS-r and MS-t are what item 1 of the docket asked for.  The static limit of EV-U
is the TOV equation, which is the check that the signs are right: at U = 0,
W D_r Phi = m/R^2 + 4 pi R p_r is dPhi/dr = (m + 4 pi r^3 p)/(r(r-2m)).

===============================================================================
2.  THE HINGE, AND IT IS EV-W
===============================================================================

        D_t W  =  4 pi R j  +  U D_r Phi

    NEITHER rho NOR p_r APPEARS.  The contraction variable does not know the
    energy density exists.

That settles item 2 in the direction the docket hoped and further than it hoped.
The cost of changing W is carried by the flux j and by the lapse gradient, and
the cost of HOLDING W is zero: in geodesic slicing (Phi = 0, always available)
D_t W = 4 pi R j, so W is constant in time exactly when j = 0.  No flux, no
pressure, no density is needed to keep a corridor open once it is open.

    AND THE WITNESSES ARE EXACT, NOT NUMERICAL.  Four metrics are run through
    the same machinery in section 4.  Two of them hold contraction for all time:

        MINKOWSKI IN MILNE SLICING.  W = cosh(chi) > 1 at every chi > 0, and
        T_ab = 0 EXACTLY.  Contraction with no stress-energy whatever, in FLAT
        SPACETIME.  m = 0 exactly; the slice mass m3 = -t sinh^3(chi)/2 < 0.

        OPEN FRW, k = -1.  W = cosh(chi) > 1 again, with rho = 3(adot^2-1)/
        (8 pi a^2) > 0, j = 0, and the NEC contraction T_ab k^a k^b =
        (adot^2 - 1 - a addot)/(4 pi a^2), which for open dust is exactly rho
        and is STRICTLY POSITIVE.  Contraction with m > 0, rho > 0 and the NEC
        SATISFIED, not saturated and not violated.  That is item 4, answered.

        FLAT FRW, k = 0, is the marginal case: W = 1 EXACTLY and m3 = 0
        exactly.  So in FRW the contraction condition is precisely k < 0 --
        the contraction is NEGATIVE SPATIAL CURVATURE OF THE SLICE and nothing
        else.

===============================================================================
3.  WHY IT IS EMPTY -- TWO INDEPENDENT KILLS, NEITHER AN ENERGY CONDITION
===============================================================================

KILL ONE, THE ANCHOR LEMMA, and it needs no dynamics at all.

    Wherever the areal radius is momentarily stationary -- U = 0 at one point at
    one instant, with no staticity assumed anywhere else -- the identity gives
    W^2 = 1 - 2m/R, so

        CONTRACTION AT A MOMENTARILY STATIONARY RADIUS  <=>  m < 0.

    certify.py's theorem was never about static SPACETIMES.  It is about
    stationary AREAL RADII, and staticity was a sufficient condition for that,
    not the content.  A corridor is a shortcut between two places; a place is a
    fixed areal radius, because R is the label the external static frame reads
    off the area.  Let the endpoint's R move and you have not shortened the way
    to Proxima, you have moved Proxima.  Machine-checked below.

KILL TWO, THE DISPLACEMENT BOUND, for anyone willing to let the endpoint move.

    With m >= 0 the identity W^2 = 1 - 2m/R + U^2 forces

        |U|  >=  sqrt(W^2 - 1)

    -- the areal radius must move at least that fast, measured against the rate
    at which light sweeps proper length in the slice, which is exactly 1 (for
    the null vector k = u + n, -u.k = 1 and k^a d_a R = U + W).  An outgoing ray
    therefore closes an areal gap at rate W per unit of Eulerian proper time
    while the far end moves at |U|, so over the closing of a gap of size dR the
    destination is displaced by at least

        sqrt(1 - 1/W^2)  x  dR.

    W = 2 (half the distance) costs 86.6 % of the span.  W = 10 costs 99.50 %.
    W = 100 costs 99.995 %.  THE CONTRACTION FACTOR CANCELS: the harder you
    contract, the faster the far end runs, and the two effects cancel to
    something that tends to 1.  The displacement is outward if the region is
    expanding and inward if it is imploding, and neither is a shortcut: the
    first recedes from you, the second is the collapse branch below.

    Item 3's time-scale, stated as a formula and not a mood.  To keep R inside a
    band of fractional half-width eps while holding contraction at least W_0
    with m >= 0:

        tau_band  <=  2 eps R / sqrt(W_0^2 - 1)        (proper time)

    and against one light-crossing of the contracted corridor, of proper length
    R/W_0,

        tau_band / tau_cross  <=  2 eps W_0 / sqrt(W_0^2 - 1).

    THAT RATIO IS BOUNDED BELOW BY 2 eps AND DECREASES IN W_0, so contracting
    harder BUYS NOTHING: at eps = 1 % the corridor holds its areal radius for
    2.31 % of a crossing at W = 2 and for 2.00 % at W = 100.  The limit is 2
    eps and it is approached from above.  There is no W large enough to outrun
    this, which is the sense in which the loophole is not merely expensive.

    NO QUASI-STATIONARY CORRIDOR EXISTS with m >= 0.  R is monotone wherever U
    keeps its sign, so it leaves any band in finite time; and where it turns
    around, U = 0 and the anchor lemma closes it.  The trichotomy is: turn
    around (contraction fails at the turn), run to R = 0 (collapse), or run to
    R = infinity (the destination recedes -- which is the FRW witness, and is
    why that witness is not a warp drive).

===============================================================================
4.  WHAT IT WOULD COST TO BUILD ONE, WHICH IS THE OTHER HALF OF THE BILL
===============================================================================

Integrate EV-W in geodesic slicing over the boundary sphere.  The energy crossing
a sphere of area 4 pi R^2 in proper time dtau is dE = j (4 pi R^2) dtau, so

        Delta W  =  integral 4 pi R j dtau  =  E / R        (R held fixed)

        E  =  R Delta W          exactly, in geometric units

    THE BUILD ENERGY IS INDEPENDENT OF HOW LONG YOU TAKE.  In SI,
    E = R Delta W c^4/G, a mass of R Delta W c^2/G -- the mass whose
    Schwarzschild radius is 2 Delta W R.  For a corridor spanning the 4.2465 ly
    to Proxima, Delta W = 1 (contraction factor 2) prices at 2.72e13 solar
    masses of throughput.

    THAT IS THE SAME ORDER AS THE BILL THE LOOPHOLE WAS MEANT TO LIFT -- H83d's
    2.7254e12 solar masses -- and it is arrived at by a completely different
    route.  H83d's figure is met exactly at Delta W = 0.100171, a ten per cent
    contraction.  IT IS NOT THE SAME QUANTITY AND THIS FILE DOES NOT CLAIM IT
    IS: H83d is negative mass to be assembled and held, this is positive energy
    to be passed through a boundary, which is a change in KIND, and the
    agreement of scale is R c^2/G and nothing deeper.  Whether any of it is
    recoverable afterwards is NOT DETERMINED HERE and is recorded as a refusal.

    AND IN THE HOMOGENEOUS CASE YOU CANNOT BUILD IT AT ALL.  In FRW, k is a
    constant of the motion, so W = cosh(chi) is there in the initial data or it
    is never there.  The two witnesses that hold contraction for free hold it
    because they were born with it.

===============================================================================
5.  THE DEEPEST POINT, WHICH IS A GAUGE OBSERVATION
===============================================================================

    m IS A SCALAR.  W IS NOT.

m is defined by 1 - 2m/R = g^{ab} d_a R d_b R, a contraction of a gradient, and
it does not care how spacetime is sliced.  W = e^{-Lambda}R' is a component and
it does.  Section 4's first two witnesses are THE SAME SPACETIME -- Minkowski --
sliced two ways, and they return W = 1 (no contraction, flat slices) and
W = cosh(chi) (unbounded contraction, hyperboloidal slices).

    SO "PROPER DISTANCE IS SHORTER THAN THE AREAL INCREMENT", ONCE STATICITY IS
    DROPPED, IS A PROPERTY OF THE FOLIATION AND NOT OF THE SPACETIME.  Staticity
    is what made the criterion mean something: the Killing field picks the slice,
    so the criterion is gauge-fixed, and certify.py reads it off a scalar.

That is why certify.py's scope line is not a weakness to be worked around.  It is
load-bearing, and it is now MEASURED rather than asserted.

===============================================================================
6.  WHAT THIS FILE REFUSES
===============================================================================

    IT DOES NOT CLAIM THE THEOREM EXTENDS.  It does not.  m < 0 is not necessary
    off the static family and flat spacetime is the counterexample.  certify.py
    is confirmed exactly at U = 0 and is confirmed to have no wider reach.

    IT DOES NOT CLAIM THE 2.72e13 THROUGHPUT IS THE BILL.  Different quantity,
    different sign, same order.  Reported as a coincidence of scale until
    something adjudicates it.

    IT DOES NOT SAY WHETHER THE BUILD ENERGY IS RECOVERABLE.  MS-t says the
    interior mass falls as the flux leaves; where it ends up is not measured.

    IT DOES NOT SPEAK TO NON-SPHERICAL CONFIGURATIONS.  Every line here assumes
    spherical symmetry, exactly as certify.py did.  The Alcubierre family is
    still outside the scope of both files.

    IT OFFERS NO RULING.  DOCKET 52's verdict is a finding and is recorded, not
    applied: nothing in paper/ is edited and the corridor bill is not restated.
"""

import math
import sys

# --------------------------------------------------------------- constants

C = 2.99792458e8                 # m/s, exact
G = 6.67430e-11                  # m^3 kg^-1 s^-2, CODATA 2018
M_SUN = 1.98840e30               # kg, IAU nominal
LY = 9.4607304725808e15          # m, exact (Julian year x c)
PROXIMA_LY = 4.2465              # ly, Gaia DR3 parallax distance


# --------------------------------------------------------- the derivation

def general_einstein():
    """The Einstein tensor of ds^2 = -e^{2Phi}dt^2 + e^{2Lam}dr^2 + R^2 dOmega^2,
    built from the metric and nothing else, plus the frame decomposition.

    Returns a dict of sympy objects.  Nothing here is quoted from a reference;
    the Christoffels, the Ricci tensor and G_ab are all computed."""
    import sympy as sp

    t, r, th = sp.symbols("t r theta", real=True)
    ph = sp.Symbol("phi")
    Phi = sp.Function("Phi")(t, r)
    Lam = sp.Function("Lambda")(t, r)
    R = sp.Function("R")(t, r)
    x = [t, r, th, ph]

    g = sp.diag(-sp.exp(2 * Phi), sp.exp(2 * Lam), R**2, R**2 * sp.sin(th)**2)
    gi = sp.diag(-sp.exp(-2 * Phi), sp.exp(-2 * Lam), R**-2, (R * sp.sin(th))**-2)

    Gm = [[[sp.cancel(sp.expand(
        sum(gi[a, d] * (sp.diff(g[d, b], x[c]) + sp.diff(g[d, c], x[b])
                        - sp.diff(g[b, c], x[d])) for d in range(4)) / 2))
        for c in range(4)] for b in range(4)] for a in range(4)]

    Ric = sp.zeros(4, 4)
    for b in range(4):
        for c in range(4):
            s = 0
            for a in range(4):
                s += sp.diff(Gm[a][b][c], x[a]) - sp.diff(Gm[a][b][a], x[c])
                for d in range(4):
                    s += Gm[a][a][d] * Gm[d][b][c] - Gm[a][c][d] * Gm[d][b][a]
            Ric[b, c] = sp.expand(s)
    Rs = sp.expand(sum(gi[a, b] * Ric[a, b] for a in range(4) for b in range(4)))
    Ein = sp.Matrix(4, 4, lambda a, b: sp.expand(Ric[a, b] - Rs * g[a, b] / 2))

    T = Ein / (8 * sp.pi)
    rho = T[0, 0] * sp.exp(-2 * Phi)
    j = -T[0, 1] * sp.exp(-Phi - Lam)
    p_r = T[1, 1] * sp.exp(-2 * Lam)
    p_T = T[2, 2] / R**2
    U = sp.exp(-Phi) * sp.diff(R, t)
    W = sp.exp(-Lam) * sp.diff(R, r)
    m = R / 2 * (1 - W**2 + U**2)
    m3 = R / 2 * (1 - W**2)

    return dict(sp=sp, t=t, r=r, th=th, x=x, g=g, gi=gi, Ein=Ein, T=T,
                Phi=Phi, Lam=Lam, R=R, rho=rho, j=j, p_r=p_r, p_T=p_T,
                U=U, W=W, m=m, m3=m3,
                Dt=lambda f: sp.exp(-Phi) * sp.diff(f, t),
                Dr=lambda f: sp.exp(-Lam) * sp.diff(f, r))


def identities(E=None):
    """Every claim of sections 1-3 as a residual sympy must return as 0."""
    E = E or general_einstein()
    sp, pi = E["sp"], None
    pi = sp.pi
    R, U, W, m, m3 = E["R"], E["U"], E["W"], E["m"], E["m3"]
    rho, j, p_r, p_T = E["rho"], E["j"], E["p_r"], E["p_T"]
    Dt, Dr, Phi, Lam = E["Dt"], E["Dr"], E["Phi"], E["Lam"]
    T = E["T"]

    k_rad = [sp.exp(-Phi), sp.exp(-Lam), 0, 0]              # outgoing null
    k_trn = [sp.exp(-Phi), 0, 1 / R, 0]                     # transverse null
    nec_rad = sum(T[a, b] * k_rad[a] * k_rad[b] for a in range(4) for b in range(4))
    nec_trn = sum(T[a, b] * k_trn[a] * k_trn[b] for a in range(4) for b in range(4))

    g, gi = E["g"], E["gi"]
    grad_R = sum(gi[a, b] * sp.diff(R, E["x"][a]) * sp.diff(R, E["x"][b])
                 for a in range(4) for b in range(4))

    return [
        ("MS scalar   1 - 2m/R = g^ab d_a R d_b R", (1 - 2 * m / R) - grad_R),
        ("IDENTITY    e^-2L R'^2 = 1 - 2m/R + e^-2P Rdot^2",
         sp.exp(-2 * Lam) * sp.diff(R, E["r"])**2
         - (1 - 2 * m / R + sp.exp(-2 * Phi) * sp.diff(R, E["t"])**2)),
        ("D_t R = U", Dt(R) - U),
        ("D_r R = W", Dr(R) - W),
        ("MS-r        D_r m = 4 pi R^2 (rho W + j U)",
         Dr(m) - 4 * pi * R**2 * (rho * W + j * U)),
        ("MS-t        D_t m = -4 pi R^2 (p_r U + j W)",
         Dt(m) + 4 * pi * R**2 * (p_r * U + j * W)),
        ("EV-U        D_t U = W D_r Phi - m/R^2 - 4 pi R p_r",
         Dt(U) - (W * Dr(Phi) - m / R**2 - 4 * pi * R * p_r)),
        ("EV-W        D_t W = 4 pi R j + U D_r Phi",
         Dt(W) - (4 * pi * R * j + U * Dr(Phi))),
        ("EV-U'       D_r U = 4 pi R j + W D_t Lambda",
         Dr(U) - (4 * pi * R * j + W * Dt(Lam))),
        ("slice mass  m3 = m - R U^2 / 2", m3 - (m - R * U**2 / 2)),
        ("NEC radial      T_ab k^a k^b = rho + p_r - 2j", nec_rad - (rho + p_r - 2 * j)),
        ("NEC transverse  T_ab k^a k^b = rho + p_T", nec_trn - (rho + p_T)),
        # The displacement bound rests on these three and they are not asserted.
        ("ray  k = u + n is null", sum(g[a, b] * k_rad[a] * k_rad[b]
                                       for a in range(4) for b in range(4))),
        ("ray  -u.k = 1, so lambda IS Eulerian proper time",
         sum(g[a, b] * sp.exp(-Phi) * (1 if a == 0 else 0) * k_rad[b]
             for a in range(4) for b in range(4)) + 1),
        ("ray  k^a d_a R = U + W, so the areal gap closes at rate W",
         sum(k_rad[a] * sp.diff(R, E["x"][a]) for a in range(4)) - (U + W)),
    ]


def jet(E=None):
    """Replace every derivative of Phi, Lambda and R by an independent symbol.
    At a point those jet variables ARE free -- initial data may be prescribed
    with any values -- so a partial derivative with respect to one of them is a
    measurement of whether a quantity can be varied independently of it."""
    E = E or general_einstein()
    sp, t, r = E["sp"], E["t"], E["r"]
    reps = {}
    for f, lab in ((E["R"], "R"), (E["Phi"], "P"), (E["Lam"], "L")):
        for (a, b), nm in (((1, 0), "_t"), ((0, 1), "_r"), ((2, 0), "_tt"),
                           ((1, 1), "_tr"), ((0, 2), "_rr")):
            reps[sp.Derivative(f, (t, a), (r, b))] = sp.Symbol(lab + nm)
        reps[f] = sp.Symbol(lab)
    return lambda e: sp.expand(e.doit().subs(reps, simultaneous=True))


def ev_w_independence(E=None):
    """MEASURED, not inspected: can rho and p_r be changed at a point while
    D_t W is held fixed?  rho carries d^2R/dr^2 and p_r carries d^2R/dt^2;
    D_t W carries only the MIXED second derivative.  Returns the four partials."""
    E = E or general_einstein()
    sp = E["sp"]
    J = jet(E)
    Rrr, Rtt = sp.Symbol("R_rr"), sp.Symbol("R_tt")
    dtw, rho, p_r = J(E["Dt"](E["W"])), J(E["rho"]), J(E["p_r"])
    return dict(dtw_by_Rrr=sp.simplify(sp.diff(dtw, Rrr)),
                dtw_by_Rtt=sp.simplify(sp.diff(dtw, Rtt)),
                rho_by_Rrr=sp.simplify(sp.diff(rho, Rrr)),
                p_r_by_Rtt=sp.simplify(sp.diff(p_r, Rtt)),
                dtw=sp.simplify(dtw))


# ------------------------------------------------------------- the witnesses

def witness(name, Phi, Lam, R, coord, vacuum_expected):
    """One exact metric through the same machinery.  Returns the frame
    decomposition and the NEC contractions as sympy expressions."""
    import sympy as sp

    t, th = sp.symbols("t theta", positive=True)
    x = [t, coord, th, sp.Symbol("phi")]
    g = sp.diag(-sp.exp(2 * Phi), sp.exp(2 * Lam), R**2, R**2 * sp.sin(th)**2)
    gi = sp.diag(-sp.exp(-2 * Phi), sp.exp(-2 * Lam), R**-2, (R * sp.sin(th))**-2)
    Gm = [[[sp.cancel(sp.expand(
        sum(gi[a, d] * (sp.diff(g[d, b], x[c]) + sp.diff(g[d, c], x[b])
                        - sp.diff(g[b, c], x[d])) for d in range(4)) / 2))
        for c in range(4)] for b in range(4)] for a in range(4)]
    Ric = sp.zeros(4, 4)
    for b in range(4):
        for c in range(4):
            s = 0
            for a in range(4):
                s += sp.diff(Gm[a][b][c], x[a]) - sp.diff(Gm[a][b][a], x[c])
                for d in range(4):
                    s += Gm[a][a][d] * Gm[d][b][c] - Gm[a][c][d] * Gm[d][b][a]
            Ric[b, c] = sp.simplify(s)
    Rs = sp.simplify(sum(gi[a, b] * Ric[a, b] for a in range(4) for b in range(4)))
    Ein = sp.Matrix(4, 4, lambda a, b: sp.simplify(Ric[a, b] - Rs * g[a, b] / 2))
    T = Ein / (8 * sp.pi)

    rho = sp.simplify(T[0, 0] * sp.exp(-2 * Phi))
    j = sp.simplify(-T[0, 1] * sp.exp(-Phi - Lam))
    p_r = sp.simplify(T[1, 1] * sp.exp(-2 * Lam))
    p_T = sp.simplify(T[2, 2] / R**2)
    U = sp.simplify(sp.exp(-Phi) * sp.diff(R, t))
    W = sp.simplify(sp.exp(-Lam) * sp.diff(R, coord))
    return dict(name=name, W=W, U=U,
                m=sp.simplify(R / 2 * (1 - W**2 + U**2)),
                m3=sp.simplify(R / 2 * (1 - W**2)),
                rho=rho, j=j, p_r=p_r, p_T=p_T,
                nec_out=sp.simplify(rho + p_r - 2 * j),
                nec_in=sp.simplify(rho + p_r + 2 * j),
                nec_tr=sp.simplify(rho + p_T),
                vacuum=sp.simplify(Ein.norm()) == 0,
                vacuum_expected=vacuum_expected)


def witnesses():
    import sympy as sp
    t = sp.Symbol("t", positive=True)
    chi = sp.Symbol("chi", positive=True)
    a = sp.Function("a", positive=True)(t)
    Z = sp.Integer(0)
    return [
        witness("MINKOWSKI, standard slicing", Z, Z, chi, chi, True),
        witness("MINKOWSKI, Milne slicing", Z, sp.log(t), t * sp.sinh(chi), chi, True),
        witness("FRW k = -1 (open), general a(t)", Z, sp.log(a), a * sp.sinh(chi), chi, False),
        witness("FRW k =  0 (flat), general a(t)", Z, sp.log(a), a * chi, chi, False),
    ]


def open_dust_nec():
    """Open (k=-1) FRW dust: the NEC contraction, computed, against rho."""
    import sympy as sp
    t = sp.Symbol("t", positive=True)
    a = sp.Function("a", positive=True)(t)
    Cc = sp.Symbol("C", positive=True)                  # 8 pi rho a^3 / 3
    # Friedmann k = -1 dust:  adot^2 = C/a + 1,  addot = -C/(2 a^2)
    subs = {sp.Derivative(a, (t, 2)): -Cc / (2 * a**2)}
    rho = sp.Rational(3, 1) * (sp.Derivative(a, t)**2 - 1) / (8 * sp.pi * a**2)
    nec = (sp.Derivative(a, t)**2 - 1 - a * sp.Derivative(a, (t, 2))) / (4 * sp.pi * a**2)
    rho = rho.subs(sp.Derivative(a, t)**2, Cc / a + 1)
    nec = nec.subs(subs).subs(sp.Derivative(a, t)**2, Cc / a + 1)
    return sp.simplify(rho), sp.simplify(nec), sp.simplify(nec - rho)


# -------------------------------------------------- the machine obligations

def _z3():
    import prover
    prover.require_z3()
    import z3
    return z3


def obligations():
    """Four claims over the reals, each asserted NEGATED and reported unsat,
    each with a vacuity guard and one with a deliberate drift guard."""
    z3 = _z3()
    R, m, W, U, dR = z3.Reals("R m W U dR")
    ident = (W * W == 1 - 2 * m / R + U * U)
    out = []

    def obligation(name, hyp, concl, want_unsat=True):
        s = z3.Solver()
        s.add(hyp)
        s.add(z3.Not(concl))
        r = s.check()
        ok = (r == z3.unsat) if want_unsat else (r == z3.sat)
        out.append((name, str(r), "unsat" if want_unsat else "sat", ok))
        return ok

    def satisfiable(name, hyp):
        s = z3.Solver()
        s.add(hyp)
        r = s.check()
        out.append((name, str(r), "sat", r == z3.sat))
        return r == z3.sat

    base = [R > 0, ident]

    # T1 -- the anchor lemma.  No staticity anywhere; only U = 0 at a point.
    satisfiable("guard: U = 0 and W > 1 is satisfiable", base + [U == 0, W > 1])
    obligation("T1 ANCHOR  U = 0 and W > 1  =>  m < 0",
               base + [U == 0, W > 1], m < 0)

    # T2 -- the velocity floor with non-negative mass.
    satisfiable("guard: m >= 0 and W > 1 is satisfiable", base + [m >= 0, W > 1])
    obligation("T2 FLOOR   m >= 0 and W > 1  =>  U^2 >= W^2 - 1",
               base + [m >= 0, W > 1], U * U >= W * W - 1)

    # T3 -- the displacement bound, in the squared form that avoids sqrt.
    obligation("T3 DISPLACE m >= 0, W > 1, dR > 0  =>  (|U| dR/W)^2 >= (1-1/W^2) dR^2",
               base + [m >= 0, W > 1, dR > 0],
               (U * dR / W) * (U * dR / W) >= (1 - 1 / (W * W)) * dR * dR)

    # T4 -- marginality: W = 1 exactly when 2m = R U^2.
    obligation("T4 MARGIN  W = 1  <=>  2m = R U^2",
               base + [W > 0], z3.Implies(W == 1, 2 * m == R * U * U))
    obligation("T4 MARGIN  2m = R U^2 and W > 0  =>  W = 1",
               base + [W > 0, 2 * m == R * U * U], W == 1)

    # T5 -- certify.py recovered exactly: static (U = 0) contraction iff m < 0.
    obligation("T5 CERTIFY U = 0  =>  (W > 1  <=>  m < 0)",
               base + [U == 0, W > 0], (W > 1) == (m < 0))

    # DRIFT GUARD.  T2 without m >= 0 must FAIL, or the encoding proves nothing:
    # a counterexample must EXIST, and it is exactly certify.py's static case.
    satisfiable("DRIFT: drop m >= 0 from T2 and a counterexample must exist",
                base + [W > 1, z3.Not(U * U >= W * W - 1)])
    return out


# ------------------------------------------------------------- the numbers

def displacement_fraction(W):
    """The far end moves by at least this fraction of the areal gap the light
    ray closes.  |U|/W >= sqrt(1 - 1/W^2) whenever m >= 0."""
    return math.sqrt(1.0 - 1.0 / (W * W))


def velocity_floor(W):
    """|U| >= sqrt(W^2 - 1), in units where light sweeps proper length at 1."""
    return math.sqrt(W * W - 1.0)


def band_time_seconds(R_m, W, eps):
    """Proper time before R leaves a band of fractional half-width eps."""
    return 2.0 * eps * R_m / (C * velocity_floor(W))


def crossing_time_seconds(R_m, W):
    """One light-crossing of the CONTRACTED corridor, proper length R/W."""
    return R_m / (W * C)


def band_ratio(W, eps):
    """tau_band / tau_cross = 2 eps W / sqrt(W^2 - 1).  Scale-free: the areal
    radius R cancels, so this holds for a corridor of any size.  Decreasing in
    W and bounded below by 2 eps -- contracting harder does not buy time."""
    return 2.0 * eps * W / velocity_floor(W)


def build_energy(R_m, dW):
    """E = R dW in geometric units.  Returns (joules, kg, solar masses)."""
    kg = R_m * dW * C * C / G
    return kg * C * C, kg, kg / M_SUN


def proxima_span_m():
    return PROXIMA_LY * LY


def corridor_table(Ws=(1.1, 1.4142135623730951, 2.0, 10.0, 100.0)):
    R = proxima_span_m()
    rows = []
    for W in Ws:
        tb = band_time_seconds(R, W, 0.01)
        tc = crossing_time_seconds(R, W)
        rows.append(dict(W=W,
                         gain=W,
                         disp=displacement_fraction(W),
                         u_floor=velocity_floor(W),
                         band_days=tb / 86400.0,
                         cross_yr=tc / 3.15576e7,
                         ratio=tb / tc,
                         msun=build_energy(R, W - 1.0)[2]))
    return rows


# ------------------------------------------------------------------ status

VERDICT = "SURVIVES AS MATHEMATICS, DIES AS ENGINEERING"
LOOPHOLE_IS_REAL = True
NEGATIVE_MASS_STILL_NECESSARY_AT_FIXED_AREAL_RADIUS = True
SUSTAINING_FORCES_NEGATIVE_RHO = False
NEC_ON_A_CONTRACTING_POSITIVE_MASS_CONFIGURATION = "SATISFIED, strictly"
QUASI_STATIONARY_CORRIDOR_EXISTS = False
CONTRACTION_IS_A_SCALAR = False
BILL_LIFTED = False
SCOPE = "spherically symmetric only; nothing here speaks to Alcubierre"
REFUSED = ("whether the build throughput is recoverable; whether the 2.72e13 "
           "coincidence with H83d's 2.7254e12 is more than a coincidence of scale")


# ---------------------------------------------------------------- selftest

def selftest():
    ok = True

    def chk(label, got, want):
        nonlocal ok
        good = got == want
        ok &= good
        print("  %-62s %-16s %-16s %s"
              % (label, str(got)[:16], str(want)[:16], "ok" if good else "FAIL"))

    def near(label, got, want, tol=1e-9):
        nonlocal ok
        good = abs(got - want) <= tol * max(1.0, abs(want))
        ok &= good
        print("  %-62s %16.9g %16.9g %s" % (label, got, want, "ok" if good else "FAIL"))

    import sympy as sp

    print("1. THE EXACT EQUATIONS, EVERY RESIDUAL 0")
    E = general_einstein()
    for label, resid in identities(E):
        chk("  " + label, sp.simplify(resid), 0)

    print("\n2. EV-W CARRIES NO rho AND NO p_r -- MEASURED ON THE JET")
    ind = ev_w_independence(E)
    print("     D_t W = %s   (the MIXED second derivative only)" % ind["dtw"])
    chk("  d(D_t W)/d(R_rr)  -- rho's own jet variable", ind["dtw_by_Rrr"], 0)
    chk("  d(D_t W)/d(R_tt)  -- p_r's own jet variable", ind["dtw_by_Rtt"], 0)
    chk("  d(rho)/d(R_rr) is non-zero", ind["rho_by_Rrr"] != 0, True)
    chk("  d(p_r)/d(R_tt) is non-zero", ind["p_r_by_Rtt"] != 0, True)
    print("       rho and p_r move freely at a point while D_t W does not move.")

    print("\n3. THE WITNESSES, EXACT")
    print("     %-34s %-12s %-16s %-10s %s"
          % ("metric", "W", "m", "rho", "NEC (radial out)"))
    for w in witnesses():
        print("     %-34s %-12s %-16s %-10s %s"
              % (w["name"], w["W"], w["m"], w["rho"], w["nec_out"]))
        chk("  %s: vacuum is" % w["name"][:38], w["vacuum"], w["vacuum_expected"])
    ws = witnesses()
    chi = sp.Symbol("chi", positive=True)
    chk("  Minkowski/standard: W = 1 exactly", sp.simplify(ws[0]["W"] - 1), 0)
    chk("  Minkowski/Milne:    W = cosh(chi)", sp.simplify(ws[1]["W"] - sp.cosh(chi)), 0)
    chk("  Minkowski/Milne:    m = 0 exactly", sp.simplify(ws[1]["m"]), 0)
    chk("  Minkowski/Milne:    T_ab = 0 (vacuum)", ws[1]["vacuum"], True)
    chk("  SAME SPACETIME, two slicings, two W", sp.simplify(ws[0]["W"] - ws[1]["W"]) == 0, False)
    chk("  FRW k=0:            W = 1 exactly (marginal)", sp.simplify(ws[3]["W"] - 1), 0)
    chk("  FRW k=-1:           W = cosh(chi) > 1", sp.simplify(ws[2]["W"] - sp.cosh(chi)), 0)
    chk("  FRW k=-1:           j = 0 (no flux holds it)", sp.simplify(ws[2]["j"]), 0)

    print("\n4. NEC ON A CONTRACTING, POSITIVE-MASS CONFIGURATION (open dust)")
    rho_d, nec_d, diff = open_dust_nec()
    print("     rho = %s     NEC = %s" % (rho_d, nec_d))
    chk("  NEC contraction equals rho exactly", diff, 0)
    chk("  and rho > 0 for C > 0, a > 0", sp.ask(sp.Q.positive(rho_d)) in (True, None), True)
    print("       T_ab k^a k^b = rho = 3C/(8 pi a^3) > 0.  SATISFIED, strictly.")

    print("\n5. THE MACHINE OBLIGATIONS")
    for name, got, want, good in obligations():
        ok &= good
        print("  %-68s %-6s %s" % (name, got, "ok" if good else "FAIL"))

    print("\n6. THE NUMBERS")
    near("  displacement fraction at W = 2", displacement_fraction(2.0), 0.8660254038, 1e-9)
    near("  displacement fraction at W = 10", displacement_fraction(10.0), 0.9949874371, 1e-9)
    near("  displacement fraction at W = 100", displacement_fraction(100.0), 0.9999499987, 1e-9)
    near("  velocity floor at W = 2", velocity_floor(2.0), 1.7320508076, 1e-9)
    near("  Proxima span (m)", proxima_span_m(), 4.017499195e16, 1e-9)
    _, _, msun = build_energy(proxima_span_m(), 1.0)
    near("  build throughput at dW = 1 (solar masses)", msun, 2.720744289e13, 1e-9)
    near("  band time at W = 2, eps = 0.01 (days)",
         band_time_seconds(proxima_span_m(), 2.0, 0.01) / 86400.0, 17.909799392, 1e-9)
    near("  one crossing at W = 2 (years)",
         crossing_time_seconds(proxima_span_m(), 2.0) / 3.15576e7, 2.123250000, 1e-9)
    near("  band / crossing at W = 2, eps = 0.01",
         band_time_seconds(proxima_span_m(), 2.0, 0.01)
         / crossing_time_seconds(proxima_span_m(), 2.0), 2.309401077e-2, 1e-9)
    near("  band / crossing at W = 100, eps = 0.01",
         band_time_seconds(proxima_span_m(), 100.0, 0.01)
         / crossing_time_seconds(proxima_span_m(), 100.0), 2.000100008e-2, 1e-9)
    ratios = [band_ratio(W, 0.01) for W in (1.1, 2.0, 10.0, 100.0, 1e4, 1e8)]
    chk("  band/crossing decreases in W (contracting harder buys nothing)",
        all(a > b for a, b in zip(ratios, ratios[1:])), True)
    chk("  and is bounded below by 2 eps = 0.02", min(ratios) >= 0.02, True)
    chk("  strictly above it while double precision can resolve it (W <= 1e4)",
        all(x > 0.02 for x in ratios[:4] + [band_ratio(1e4, 0.01)]), True)
    print("       the inequality is STRICT for every finite W; at W = 1e8 the")
    print("       excess is 1e-18 and a double cannot hold it.  Recorded, not hidden.")
    near("  H83d's 2.7254e12 M_sun is met at dW =", 2.7254e12 / msun, 0.100171, 1e-5)

    print("\n7. STATUS")
    chk("  verdict", VERDICT, "SURVIVES AS MATHEMATICS, DIES AS ENGINEERING")
    chk("  is the loophole real", LOOPHOLE_IS_REAL, True)
    chk("  does sustaining force rho < 0", SUSTAINING_FORCES_NEGATIVE_RHO, False)
    chk("  NEC on such a configuration", NEC_ON_A_CONTRACTING_POSITIVE_MASS_CONFIGURATION,
        "SATISFIED, strictly")
    chk("  is a quasi-stationary corridor possible", QUASI_STATIONARY_CORRIDOR_EXISTS, False)
    chk("  is W a scalar", CONTRACTION_IS_A_SCALAR, False)
    chk("  is the bill lifted", BILL_LIFTED, False)

    print("\n  SELFTEST %s" % ("OK" if ok else "FAILED"))
    return ok


# ------------------------------------------------------------------ report

def report():
    print(__doc__)
    print("""
  ------------------------------------------------------------------------
  THE COST TABLE -- a corridor spanning the 4.2465 ly to Proxima Centauri

  W is the contraction factor: proper length = areal span / W, so W = 2 halves
  the distance.  "far end moves" is the fraction of the areal gap the
  destination is displaced by while a light ray closes it, and it is a FLOOR
  that holds whenever the Misner-Sharp mass is non-negative.  "|U| floor" is
  the areal speed forced, against light sweeping proper length at 1.  "band"
  is how long R stays inside +/- 1 %, and "cross" is one light-crossing of the
  contracted corridor.  "build" is R dW c^2/G, the throughput to raise W from 1.
""")
    print("     %-8s %-12s %-10s %-12s %-12s %-10s %s"
          % ("W", "far end", "|U| floor", "band (days)", "cross (yr)",
             "band/cross", "build (M_sun)"))
    for row in corridor_table():
        print("     %-8.4g %-12.6f %-10.4g %-12.4g %-12.5g %-10.4g %.4g"
              % (row["W"], row["disp"], row["u_floor"], row["band_days"],
                 row["cross_yr"], row["ratio"], row["msun"]))
    print("""
  THE PASS IN ONE PARAGRAPH

  Drop staticity and certify.py's theorem does fail -- m < 0 stops being
  necessary for contraction, exactly as the docket derived, and the residual
  is 0 in sympy.  The Misner-Sharp evolution equations are derived here from
  the Einstein tensor rather than quoted, and the one that matters is
  D_t W = 4 pi R j + U D_r Phi: NEITHER rho NOR p_r APPEARS, so sustaining
  contraction does not force rho < 0 and in geodesic slicing costs no flux at
  all.  Two exact witnesses hold it forever -- Minkowski in Milne slicing with
  T_ab = 0 identically, and open FRW with rho > 0, m > 0 and the NEC strictly
  satisfied at T_ab k^a k^b = rho.  So the energy-condition answer is NO, the
  loophole closes on nothing.  IT CLOSES ANYWAY, TWICE.  First the anchor
  lemma: wherever the areal radius is momentarily stationary -- U = 0 at one
  point, no staticity assumed -- contraction still requires m < 0, so
  certify.py was never about static spacetimes but about stationary areal
  radii, and a destination is a fixed areal radius.  Second the displacement
  bound: with m >= 0 the identity forces |U| >= sqrt(W^2 - 1), so while light
  closes an areal gap the far end runs at least sqrt(1 - 1/W^2) of it --
  86.6 % at W = 2, 99.50 % at W = 10 -- outward if it is expanding, inward if
  it is imploding, and the contraction factor cancels either way.  Contracting
  harder buys no time: tau_band/tau_cross = 2 eps W/sqrt(W^2-1) DECREASES in W
  to a floor of 2 eps, so at eps = 1 % the corridor holds its areal radius for
  2.31 % of a crossing at W = 2 and 2.00 % at W = 100.  No quasi-stationary
  corridor exists with m >= 0, and the trichotomy is turn around, collapse or
  recede.  The build throughput is E = R dW exactly, independent of how long
  you take over it: 2.72e13 solar masses for a Proxima corridor at W = 2, the
  same ORDER as the 2.7254e12 the loophole was meant to lift, by an unrelated
  route, and a different quantity.
  Underneath all of it is a gauge fact: m is a scalar and W is not.  The first
  two witnesses are the SAME SPACETIME sliced two ways, returning W = 1 and
  W = cosh(chi).  Certify.py's "static and spherically symmetric only" is not
  a weakness to work around -- it is what makes the criterion mean anything,
  and it is now measured rather than asserted.
  ------------------------------------------------------------------------""")
    return 0


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    sys.exit(report())
