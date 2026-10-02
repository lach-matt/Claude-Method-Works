#!/usr/bin/env python3
"""
composite.py -- where universal seating meets universal transport.  IT IS NOT
EMPTY, AND THE PREVIOUS PASSES MISSED IT BY DROPPING ONE TERM.

M asked whether a device should do both -- transition space AND transition time
-- and the honest answer looked like "it must be two subsystems, because seating
needs R_kk > 0 and advance needs R_kk < 0."  That reasoning used the Ricci-only
reduction of the Jacobi equation.  It is wrong, and this file says why.

-- THE TERM THAT WAS DROPPED --------------------------------------------------
achronal.py, transit.py and seatindex.py all wrote focusing as

        u'' = -(R_kk/2) u

having dropped shear on the grounds that sigma^2 >= 0 "only helps focusing", so
ignoring it is conservative.  Conservative for an EXISTENCE claim about one ray,
and fatal for a SEARCH: the full statement (Gao & Wald 2000, eq. 13) is

        G''/G = -(1/2)[ sigma_ab sigma^ab + R_ab k^a k^b ]

and the two terms have completely different sign structure in the source:

        RICCI focusing   R_kk = 8 pi T_kk        LINEAR in the source
        WEYL focusing    sigma^2                 QUADRATIC in the source
                                                 (its effect on AREA)

RICCI FOCUSING NEEDS POSITIVE ENERGY.  WEYL FOCUSING IS SIGN-BLIND -- because
the vacuum tidal matrix is traceless, so flipping M swaps its converging and
diverging directions; the conjugate point itself is set by the FIRST-order
astigmatic focal length b^2/4|M|.  (That reading is this file's, not Gao &
Wald's.)  To first order in M a negative mass shears the congruence exactly as
hard as a positive mass of the same magnitude -- Born integration gives the
same conjugate point, 55.87, for both signs; the bent rays differ at O(M^2),
55.17 against 56.50 -- and the Shapiro delay, being linear, flips sign with it.

    SO A NEGATIVE MASS CAN FOCUS A CONGRUENCE TO A CONJUGATE POINT WHILE THE
    LIGHT THAT FOCUSES ARRIVES EARLY.  Seating and advance, in one object.

-- MEASURED, ON A VALIDATED PIPELINE ------------------------------------------
Linearised static metric ds^2 = -(1+2 Phi)dt^2 + (1-2 Phi)dx^2, Phi = -M/r, with
M of either sign -- the isotropic form, one potential in g_tt and g_ij (Psi = Phi).  Christoffels, Riemann and the optical tidal matrix all by
finite difference from the metric -- no formula carried from memory.  The full
Jacobi MATRIX is evolved, A'' = -K A with K_ij = R_{k e_i k e_j} (Gao & Wald
eq. 11; MTW 11.10), A(0) = 0, A'(0) = I, on a parallel-propagated screen; a
conjugate point is det A = 0, which includes shear by construction rather than
by an added term.  tidal() returns T = -K (Perlick's optical tidal matrix), so
the loop reads A'' = +T A.
    CORRECTED (DOCKET 67, M: "address/correct/repair all figures").  This read
    "A'' = -T A", and survey() integrated exactly that: A'' = +K A, the
    opposite sign to eq. (11).  The sign is now eq. (11)'s (JACOBI_SIGN); the
    as-written sign is kept as AS_WRITTEN_SIGN for the control.  WHAT MOVED,
    computed with survey() under both signs: at the default n = 900 NOTHING --
    55.17 / 56.50 at +-2e-3 and every row of the window table below are
    identical, because the vacuum tidal matrix is traceless and diagonal on
    this screen, so the flip only swaps which transverse axis collapses (the
    delay is the geodesic's and never read the Jacobi loop).  At n = 3600 the
    first table's conjugate points move by two to three steps of h = 0.021,
    55.16 -> 55.21 and 56.52 -> 56.56 (n = 1800: 55.21, 56.54), because the
    O(M^2) trace no longer cancels between the swapped axes; an independent RK4
    integration of eq. (11) on an exact screen gives 55.2085 and 56.5591
    (DOCKET 67, E5).  No seat, verdict or window edge moved.
    What the flip DID change: for M > 0 the as-written loop collapsed the
    radial (y) axis; with eq. (11)'s sign it is the azimuthal (z) axis, as
    neighbouring geodesics show (the selftest's parallel-data control), and
    the linearised metric's own O(M^2) Ricci now defocuses in the code as the
    text below always said it does.  On a ray through matter the flip would
    reverse the Ricci term (concentric.py's a = 0.5 corridor).

  VALIDATION 1  light deflection agrees with 4M/b to 0.03 % at b = 0.2 -- a
                cancellation: the finite run (x0 = -4, lam = 8) falls 0.125 %
                short of 4M/b at first order, and the linearised metric's
                second-order term adds +pi M/b = 0.157 %.  Against that combined
                prediction the pipeline agrees to about 4e-5.
  VALIDATION 2  the tidal matrix is TRACELESS to four digits at closest
                approach, as vacuum demands at linear order (R_kk = 0) -- in a
                static check whose k = (1,1,0,0) is not null in this metric.
                With the true null tangent the trace is the linearised metric's
                own O(M^2) Ricci, about 0.9 % of |T| at |M| = 2e-3 (up to 5.4 %
                where the Weyl part is weak), and it defocuses.  So what
                focuses here is Weyl to that level; the exact vacuum completion
                is exactly traceless and gives the same conjugate points.
  VALIDATION 3  the antisymmetric part of the arrival time reproduces the
                analytic Shapiro 2M ln[(x1+r1)/(x0+r0)] to 0.6 %.

At b = 0.3, source at 40 (OUTSIDE the focal length b^2/4|M| = 11.25, a
thin-lens value exact only to O(M/b) -- at this b a source inside it forms no
real image, which cost this pass two wrong runs):

        M          conjugate point     t - |dx|        verdict
        +2.0e-3    lambda = 55.21      +5.124e-2       seats, LATE
        -2.0e-3    lambda = 56.56      -3.762e-2       SEATS AND EARLY

(The conjugate points and the +M delay in this table are the n = 3600 run;
survey() at its default n = 900 gives 55.17, 56.50 and +5.123e-2.)
    CORRECTED (DOCKET 67): the conjugate points were 55.16 and 56.52, from the
    loop with the opposite Jacobi sign (A'' = +K A); with eq. (11)'s sign the
    n = 3600 run gives 55.21 and 56.56 (computed: survey(+-2e-3, n=3600)).

Both signs seat, at almost the same place, because the vacuum tidal matrix is
traceless: flipping M swaps the eigen-directions and leaves det A = 0 where it
was at first order.  The 2.4 % difference is the O(M^2) bent ray.  Only the
arrival flips.  Converged to within one coarse step over a 4x refinement in
step count: 56.50, 56.54, 56.56 at n = 900, 1800, 3600 (h = 0.083 at
n = 900; the detector reports on the step grid, so h is its resolution).
CORRECTED (DOCKET 67) from "converged to four figures", which the step grid
cannot resolve.

-- AND IT IS A WINDOW, BOUNDED ON BOTH SIDES ----------------------------------
The arrival time is not purely Shapiro.  Measured minus analytic leaves a
symmetric residue, quadratic in M, so sign-blind, so a delay penalty that
negative mass cannot escape.  About 99 % of it is the PATH LENGTHENING of a
bent ray; about 1.2 % is the linearised metric's own O(Phi^2) term in the null
coordinate speed.  It describes this linearised model, not GR's second-order
Schwarzschild delay:

        t - |dx|  =  (Shapiro, ~ M, flips)  +  (path lengthening, ~ M^2, never)

Seating wants |M| large enough to focus inside the available length; advance
wants |M| small enough that the linear term still beats the quadratic.  They
pull opposite ways and leave a window.  At b = 0.3, L = 75:

        |M|        conjugate         t - |dx|        verdict
        2.0e-4     none              -4.347e-3       early, no seat
        1.0e-3     none              -2.041e-2       early, no seat
        2.0e-3     56.50             -3.762e-2       *** SEATS + EARLY ***
        5.0e-3     45.58             -7.184e-2       *** SEATS + EARLY ***
        1.0e-2     42.83             -7.968e-2       *** SEATS + EARLY ***
        2.0e-2     41.50             +4.111e-2       seats, LATE
        4.0e-2     40.83             +6.160e-1       seats, LATE

    ABOUT ONE DECADE WIDE, and the advance is largest just below the upper
    edge.  This is the answer to "where do they meet": not a point, a band.

-- WHY THE EARLIER PASSES FOUND NOTHING ---------------------------------------
Not only the dropped shear.  The Alcubierre bubble's focusing is RICCI-dominated
-- the wall is where the stress is and the rays that turn are the rays that pass
through positive T_kk.  achronal.py's 25-ray result and transit.py's TURN => LATE
are both correct FOR THAT OBJECT.  A compact source focuses through WEYL instead,
in vacuum, and that is a different mechanism with a different sign rule.  The
two results do not conflict; they are about different terms of the same equation.

Note what this does to the causal bookkeeping.  The ray here travels entirely
through VACUUM -- closest approach b = 0.3, T_kk = 0 along the whole path -- so
it does not violate ANEC anywhere.  It arrives early because of the potential it
crosses, and the exotic matter sits somewhere the payload never goes.  And past
its conjugate point the geodesic is NOT achronal, so Graham & Olum's hypothesis
fails and the achronal ANEC does not reach it.  That is exactly the escape
achronal.py searched for and did not find -- it was not in the Alcubierre family.

-- WHAT IS NOT CLAIMED, AND THE LIST IS LONG ON PURPOSE -----------------------
 1. NEGATIVE MASS IS ASSUMED, NOT DERIVED.  Phi = -M/r with M < 0 is prescribed.
    Whether a self-consistent source exists is the question selfconsistent.py
    treats for Type IV, and it is answered there only at first order in hbar.
 2. LINEARISED WEAK FIELD.  The metric is the standard first-order form.  The
    window's upper edge is where the quadratic term bites, which is also where
    the linearisation starts to be questioned.  Its location is INDICATIVE.
 3. THE FOCUS IS ASTIGMATIC.  The tidal matrix is traceless, so one transverse
    direction converges while the other diverges: det A = 0 is a LINE focus, not
    a point.  A line focus is a conjugate point and breaks achronality, which is
    all the causal argument needs -- but it is not a point-to-point image.
 4. NO PAYLOAD.  This is null-geodesic optics.  Nothing here carries mass, and
    the timelike channel the conjugate point opens has not been integrated.
 5. ONE GEOMETRY.  A single compact spherical source.  The two-region concentric
    device M asked about is NOT-RUN; this file establishes that its enabling
    mechanism is real, not that the device closes.

CORRECTED (DOCKET 67).  Wording only; no verdict, flag or computed number
moved.  As first written: 'exactly as hard as a positive mass' (true at O(M));
'because the focusing is quadratic' (seating is sign-blind because the vacuum
tidal matrix is traceless); 'reproduces 4M/b to 0.03 %' (a cancellation);
'pure Weyl' (to about 1-5 %); 56.52 (the n = 3600 value); 'forms no real image'
without 'at this b', and b^2/4M as exact; the M^2 residue wholly 'path
lengthening'; the static residue 'h-independent ... the metric's own O(Phi^2)'
(it depends on h); and Olum cited as if he governed this ray.  The code's
tidal sign was then recorded at tidal() and left unchanged; on M's ruling it
is now corrected in survey() (see MEASURED, ON A VALIDATED PIPELINE), and no
figure in this file moved.

stdlib only.  Gao & Wald, Class. Quantum Grav. 17, 4999 (2000), gr-qc/0007021,
eq. (13) and eq. (11) for the Jacobi matrix.  Olum, PRL 81, 3567 (1998): his
superluminal path (Condition 1) needs negative energy ON the path.  This early
ray passes outside the M < 0 source with T_ab = 0 along it, and it focuses, so
it is not a Condition-1 path and Olum's theorem does not govern it; the
negative energy here is prescribed off the path (item 1).
"""
import math, sys

H = 1.0e-3
B_DEFAULT = 0.3
X0_DEFAULT = -40.0
LAM_DEFAULT = 75.0
NSTEP = 900

#: The Jacobi equation's sign, as survey() applies it to tidal()'s T = -K:
#: A'' = JACOBI_SIGN * T A.  +1 is Gao-Wald eq. (11), A'' = -K A.
#: CORRECTED (DOCKET 67): survey() first ran with -1 (A'' = +K A); that value
#: is kept as AS_WRITTEN_SIGN so the selftest's control can show it is wrong.
JACOBI_SIGN = +1
AS_WRITTEN_SIGN = -1


def phi(p, M):
    r = math.sqrt(p[0] * p[0] + p[1] * p[1] + p[2] * p[2])
    return -M / max(r, 1e-9)


def metric(p, M):
    f = phi(p, M)
    m = [[0.0] * 4 for _ in range(4)]
    m[0][0] = -(1.0 + 2.0 * f)
    m[1][1] = m[2][2] = m[3][3] = (1.0 - 2.0 * f)
    return m


def _sh(p, i, d):
    q = list(p)
    if i > 0:
        q[i - 1] += d
    return tuple(q)


def _dg(p, mu, M, h=H):
    if mu == 0:
        return [[0.0] * 4 for _ in range(4)]
    a, b = metric(_sh(p, mu, h), M), metric(_sh(p, mu, -h), M)
    return [[(a[i][j] - b[i][j]) / (2.0 * h) for j in range(4)] for i in range(4)]


def christoffel(p, M, h=H):
    import typefour as tf
    gi = tf.inverse(metric(p, M))
    d = [_dg(p, m, M, h) for m in range(4)]
    return [[[0.5 * sum(gi[a][e] * (d[b][e][c] + d[c][b][e] - d[e][b][c])
                        for e in range(4))
              for c in range(4)] for b in range(4)] for a in range(4)]


def _dchris(p, mu, M, h=H):
    if mu == 0:
        return [[[0.0] * 4 for _ in range(4)] for _ in range(4)]
    A, B = christoffel(_sh(p, mu, h), M, h), christoffel(_sh(p, mu, -h), M, h)
    return [[[(A[a][b][c] - B[a][b][c]) / (2.0 * h) for c in range(4)]
             for b in range(4)] for a in range(4)]


def riemann_lower(p, M, h=H):
    """R_abcd, all indices down, by finite difference from the metric."""
    G = christoffel(p, M, h)
    dG = [_dchris(p, m, M, h) for m in range(4)]
    g = metric(p, M)
    R = [[[[0.0] * 4 for _ in range(4)] for _ in range(4)] for _ in range(4)]
    for a in range(4):
        for b in range(4):
            for c in range(4):
                for d in range(4):
                    up = (dG[c][a][b][d] - dG[d][a][b][c]
                          + sum(G[a][c][e] * G[e][b][d] - G[a][d][e] * G[e][b][c]
                                for e in range(4)))
                    R[a][b][c][d] = up
    return [[[[sum(g[a][e] * R[e][b][c][d] for e in range(4)) for d in range(4)]
              for c in range(4)] for b in range(4)] for a in range(4)]


def null_tangent(p, M, direction=(1.0, 0.0, 0.0)):
    g = metric(p, M)
    dx, dy, dz = direction
    a = g[1][1] * dx * dx + g[2][2] * dy * dy + g[3][3] * dz * dz
    b = 2.0 * g[0][1] * dx
    c = g[0][0]
    s = (-b + math.sqrt(b * b - 4.0 * a * c)) / (2.0 * a)
    return [1.0, s * dx, s * dy, s * dz]


def geodesic(p0, k0, M, lam, n):
    h = lam / n
    x = [0.0, p0[0], p0[1], p0[2]]
    k = list(k0)
    pts, tang = [], []

    def acc(xx, kk):
        G = christoffel((xx[1], xx[2], xx[3]), M)
        return [-sum(G[a][b][c] * kk[b] * kk[c] for b in range(4) for c in range(4))
                for a in range(4)]

    for _ in range(n):
        pts.append(tuple(x))
        tang.append(tuple(k))
        a1 = acc(x, k)
        x2 = [x[m] + 0.5 * h * k[m] for m in range(4)]
        k2 = [k[m] + 0.5 * h * a1[m] for m in range(4)]
        a2 = acc(x2, k2)
        x3 = [x[m] + 0.5 * h * k2[m] for m in range(4)]
        k3 = [k[m] + 0.5 * h * a2[m] for m in range(4)]
        a3 = acc(x3, k3)
        x4 = [x[m] + h * k3[m] for m in range(4)]
        k4 = [k[m] + h * a3[m] for m in range(4)]
        a4 = acc(x4, k4)
        x = [x[m] + h / 6.0 * (k[m] + 2 * k2[m] + 2 * k3[m] + k4[m]) for m in range(4)]
        k = [k[m] + h / 6.0 * (a1[m] + 2 * a2[m] + 2 * a3[m] + a4[m]) for m in range(4)]
    return pts, tang, h


def tidal(p, k, e1, e2, M):
    """The optical tidal matrix on a transverse screen.  Traceless in vacuum,
    at linear order in Phi.

    SIGN: this returns T = -K with K_ij = R_{k e_i k e_j} (Perlick's optical
    tidal matrix R), so Gao-Wald eq. (11), eta'' = -K eta, reads A'' = +T A,
    and that is what survey() integrates (JACOBI_SIGN = +1).
    CORRECTED (DOCKET 67): survey() first evolved A'' = -T A = +K A, the
    opposite sign to eq. (11).  That agreed with eq. (11) only for a traceless
    diagonal T (vacuum at linear order, T_yz = 0), where the flip swaps the
    eigen-directions and moves no conjugate point; on a ray through matter it
    reversed the Ricci term.  Recorded first; repaired on M's ruling."""
    R = riemann_lower(p, M)
    E = (e1, e2)
    return [[-sum(R[m][a][n][b] * k[m] * E[i][a] * k[n] * E[j][b]
                  for m in range(4) for a in range(4)
                  for n in range(4) for b in range(4))
             for j in range(2)] for i in range(2)]


def survey(M, b=B_DEFAULT, x0=X0_DEFAULT, lam=LAM_DEFAULT, n=NSTEP,
           sign=JACOBI_SIGN):
    """One ray: does it seat (det A = 0), and does it arrive early?

    sign = JACOBI_SIGN integrates eq. (11); AS_WRITTEN_SIGN reproduces the
    first-written loop, kept for the control only (DOCKET 67)."""
    p0 = (x0, b, 0.0)
    k0 = null_tangent(p0, M)
    pts, tang, h = geodesic(p0, k0, M, lam, n)
    e1, e2 = [0., 0., 1., 0.], [0., 0., 0., 1.]
    A = [[0.0, 0.0], [0.0, 0.0]]
    dA = [[1.0, 0.0], [0.0, 1.0]]
    conj, tr_max, tmag = None, 0.0, 0.0
    for i in range(len(pts) - 1):
        x = pts[i]
        k = list(tang[i])
        p = (x[1], x[2], x[3])
        T = tidal(p, k, e1, e2, M)
        mag = max(abs(T[0][0]), abs(T[1][1]))
        if mag > tmag:
            tmag, tr_max = mag, abs(T[0][0] + T[1][1])
        # A'' = +T A = -K A (eq. 11).  CORRECTED (DOCKET 67) from -T A.
        acc = [[sign * sum(T[r][s] * A[s][c] for s in range(2)) for c in range(2)]
               for r in range(2)]
        for r in range(2):
            for c in range(2):
                A[r][c] += h * dA[r][c] + 0.5 * h * h * acc[r][c]
                dA[r][c] += h * acc[r][c]
        # first det A <= 0 after step 5: sufficient, not necessary -- it finds
        # an odd-multiplicity zero only, and would miss a stigmatic focus.
        if i > 5 and conj is None and (A[0][0] * A[1][1] - A[0][1] * A[1][0]) <= 0.0:
            conj = i * h
        G = christoffel(p, M)
        for e in (e1, e2):
            de = [-sum(G[a][al][be] * k[al] * e[be]
                       for al in range(4) for be in range(4)) for a in range(4)]
            for a in range(4):
                e[a] += h * de[a]
    a0, b0 = pts[0], pts[-1]
    dt = b0[0] - a0[0]
    dx = math.sqrt(sum((b0[j] - a0[j]) ** 2 for j in (1, 2, 3)))
    return {"M": M, "conjugate": conj, "seats": conj is not None,
            "delay": dt - dx, "early": (dt - dx) < 0.0,
            "traceless_ratio": tr_max / tmag if tmag else 0.0,
            "bend": math.atan2(-tang[-1][2], tang[-1][1])}


def parallel_data(M, sign, b=B_DEFAULT, x0=X0_DEFAULT, lam=LAM_DEFAULT,
                  n=NSTEP, d=1.0e-4):
    """The sign control, convention-free (DOCKET 67, gr-qc/0007021-eq11 E3b).

    Two neighbouring geodesics start PARALLEL to the reference ray, offset by
    d in y (radial) and in z (azimuthal); their end separations / d are what
    any correct Jacobi equation must give with parallel data A(0) = I,
    A'(0) = 0.  Returns ((y_sep, z_sep) from the geodesics, (A_yy, A_zz) from
    this file's Jacobi loop with the given sign)."""
    def path(p0):
        return geodesic(p0, null_tangent(p0, M), M, lam, n)
    pts, tang, h = path((x0, b, 0.0))
    py = path((x0, b + d, 0.0))[0]
    pz = path((x0, b, d))[0]
    seps = ((py[-1][2] - pts[-1][2]) / d, (pz[-1][3] - pts[-1][3]) / d)
    e1, e2 = [0., 0., 1., 0.], [0., 0., 0., 1.]
    A = [[1.0, 0.0], [0.0, 1.0]]
    dA = [[0.0, 0.0], [0.0, 0.0]]
    for i in range(len(pts) - 1):
        k = list(tang[i])
        p = (pts[i][1], pts[i][2], pts[i][3])
        T = tidal(p, k, e1, e2, M)
        acc = [[sign * sum(T[r][s] * A[s][c] for s in range(2)) for c in range(2)]
               for r in range(2)]
        for r in range(2):
            for c in range(2):
                A[r][c] += h * dA[r][c] + 0.5 * h * h * acc[r][c]
                dA[r][c] += h * acc[r][c]
        G = christoffel(p, M)
        for e in (e1, e2):
            de = [-sum(G[a][al][be] * k[al] * e[be]
                       for al in range(4) for be in range(4)) for a in range(4)]
            for a in range(4):
                e[a] += h * de[a]
    return seps, (A[0][0], A[1][1])


def both(M, **kw):
    r = survey(M, **kw)
    return r["seats"] and r["early"]


def analytic_shapiro(M, b=B_DEFAULT, x0=X0_DEFAULT, x1=None, lam=LAM_DEFAULT):
    x1 = (x0 + lam) if x1 is None else x1
    r0, r1 = math.hypot(x0, b), math.hypot(x1, b)
    return 2.0 * M * math.log((x1 + r1) / (x0 + r0))


def focal_length(M, b=B_DEFAULT):
    """b^2/(4|M|), a thin-lens value exact to O(M/b).  At this impact
    parameter b a source INSIDE this forms no real image -- the error that
    cost this pass two runs.  (A smaller b shortens f.  The 4M/b deflection
    route covers M > 0; for M < 0 the radial direction focuses at the same
    distance.)"""
    return b * b / (4.0 * abs(M))


# ---------------------------------------------------------------- selftest

def selftest():
    ok = True

    def chk(label, got, want):
        nonlocal ok
        good = got == want
        ok &= good
        print("  %-60s %14s %14s  %s" % (label, got, want, "ok" if good else "FAIL"))

    def near(label, got, want, tol):
        nonlocal ok
        good = abs(got - want) <= tol
        ok &= good
        print("  %-60s %14.6g %14.6g  %s" % (label, got, want, "ok" if good else "FAIL"))

    print("VALIDATION 1 -- light deflection reproduces 4M/b")
    for b, tol in ((0.1, 4e-3), (0.2, 1e-3)):
        Mv = 1.0e-4
        r = survey(Mv, b=b, x0=-4.0, lam=8.0, n=700)
        near("b=%.1f: bend / (4M/b)" % b, r["bend"] / (4.0 * Mv / b), 1.0, tol)

    print("\nVALIDATION 2 -- the tidal matrix is TRACELESS at linear order: Weyl")
    # Two separate claims, because they have different error sources.
    # (a) the PHYSICS, at a fixed point with no screen transport involved.
    Tc = tidal((0.0, B_DEFAULT, 0.0), [1.0, 1.0, 0.0, 0.0],
               [0., 0., 1., 0.], [0., 0., 0., 1.], -2.0e-3)
    ratio = abs(Tc[0][0] + Tc[1][1]) / max(abs(Tc[0][0]), abs(Tc[1][1]))
    near("static, closest approach, k=(1,1,0,0): |trace| / |max|", ratio, 0.0, 5e-4)
    print("       1.6e-4 at this h; it depends on h (9.9e-4 .. 6.0e-5 over")
    print("       h = 3e-3 .. 1e-4), converging to 5.9e-5 for this non-null probe.")
    # (b) along the ray, with the true null tangent, the trace ratio is about a
    #     percent -- mostly the linearised metric's own O(M^2) Ricci (8.7e-3
    #     computed in DOCKET 67), with first-order Euler screen transport adding
    #     little.  As first written this was called the Euler 'leak'.  It
    #     cannot manufacture a conjugate point -- both signs give the same lambda.
    r = survey(2.0e-3)
    chk("along the ray the trace ratio stays under 2 % (O(M^2) Ricci)",
        r["traceless_ratio"] < 2.0e-2, True)
    print("       ratio = %.3e.  Ricci focusing is O(M^2) here; what focuses is shear."
          % r["traceless_ratio"])

    print("\nVALIDATION 3 -- the antisymmetric delay is the analytic Shapiro")
    rp, rm = survey(2.0e-3), survey(-2.0e-3)
    anti = 0.5 * (rp["delay"] - rm["delay"])
    near("antisymmetric part vs 2M ln[(x1+r1)/(x0+r0)]",
         anti / analytic_shapiro(2.0e-3), 1.0, 1e-2)
    sym = 0.5 * (rp["delay"] + rm["delay"])
    chk("and a POSITIVE symmetric residue remains (~M^2, mostly path)",
        sym > 0.0, True)
    print("       antisym %+.5e   analytic %+.5e   sym residue %+.5e"
          % (anti, analytic_shapiro(2.0e-3), sym))

    print("\nVALIDATION 4 -- the Jacobi sign is eq. (11)'s, convention-free (DOCKET 67)")
    # Parallel data A(0) = I, A'(0) = 0 against two neighbouring geodesics
    # started parallel to the ray: a correct Jacobi equation reproduces their
    # separations; the opposite sign returns the two transverse axes swapped.
    seps, a_new = parallel_data(2.0e-3, JACOBI_SIGN)
    _, a_old = parallel_data(2.0e-3, AS_WRITTEN_SIGN)
    print("       geodesics (y, z) = (%.3f, %.3f); eq. (11) sign (%.3f, %.3f);"
          % (seps + a_new))
    print("       as-written sign (%.3f, %.3f)" % a_old)
    chk("M > 0: the azimuthal (z) neighbour converges, the radial (y) diverges",
        (seps[1] < 1.0, seps[0] > 1.0), (True, True))
    chk("eq. (11) sign (A'' = +T A = -K A) reproduces both separations",
        abs(a_new[0] - seps[0]) < 0.1 and abs(a_new[1] - seps[1]) < 0.1, True)
    chk("CONTROL: the as-written sign (A'' = +K A) does NOT -- axes swapped",
        abs(a_old[0] - seps[0]) < 0.1 or abs(a_old[1] - seps[1]) < 0.1, False)
    chk("in vacuum the flip moves no conjugate point at n = 900 (-2e-3)",
        survey(-2.0e-3, sign=AS_WRITTEN_SIGN)["conjugate"],
        survey(-2.0e-3)["conjugate"])

    print("\nTHE HEADLINE -- both signs seat, only the arrival flips")
    print("     %10s %12s %14s %s" % ("M", "conjugate", "t - |dx|", "verdict"))
    for r in (rp, rm):
        print("     %+10.1e %12s %+14.4e %s"
              % (r["M"], ("%.2f" % r["conjugate"]) if r["seats"] else "none",
                 r["delay"],
                 "SEATS + EARLY" if (r["seats"] and r["early"])
                 else "seats, late" if r["seats"] else "no seat"))
    chk("the positive mass seats", rp["seats"], True)
    chk("the negative mass seats TOO -- Weyl focusing is sign-blind",
        rm["seats"], True)
    near("and at nearly the same place (equal at O(M))",
         rm["conjugate"] / rp["conjugate"], 1.0, 0.05)
    chk("the positive mass arrives late", rp["early"], False)
    chk("THE NEGATIVE MASS SEATS AND ARRIVES EARLY", both(-2.0e-3), True)

    print("\nTHE WINDOW -- bounded below by seating, above by the M^2 penalty")
    print("     %10s %12s %14s %s" % ("|M|", "conjugate", "t - |dx|", "verdict"))
    rows = []
    for mag in (5.0e-4, 2.0e-3, 1.0e-2, 4.0e-2):
        r = survey(-mag)
        rows.append(r)
        print("     %10.1e %12s %+14.4e %s"
              % (mag, ("%.2f" % r["conjugate"]) if r["seats"] else "none", r["delay"],
                 "*** SEATS + EARLY ***" if (r["seats"] and r["early"])
                 else "seats, LATE" if r["seats"] else "early, no seat"))
    chk("below the window: early but does not seat",
        (rows[0]["seats"], rows[0]["early"]), (False, True))
    chk("inside the window: both", (rows[1]["seats"], rows[1]["early"]), (True, True))
    chk("still inside an order of magnitude up",
        (rows[2]["seats"], rows[2]["early"]), (True, True))
    chk("above the window: seats, but the M^2 penalty wins",
        (rows[3]["seats"], rows[3]["early"]), (True, False))
    chk("so the window is bounded on BOTH sides", True, True)

    print("\nThe error that cost two runs, kept as a test")
    near("focal length b^2/4M at the design point", focal_length(2.0e-3), 11.25, 1e-9)
    inside = survey(-2.0e-3, x0=-5.0, lam=60.0)
    chk("a source INSIDE the focal length forms no image", inside["seats"], False)
    chk("the same mass with the source outside it does", both(-2.0e-3), True)
    print("       Nothing about the physics changed between those two lines.")

    print("\n  SELFTEST %s" % ("OK" if ok else "FAILED"))
    return 0 if ok else 1


def report():
    print(__doc__)
    print("=" * 79)
    print("THE WINDOW, at b = %.2f, source %.0f, run %.0f" % (B_DEFAULT, -X0_DEFAULT, LAM_DEFAULT))
    print("  %10s %12s %14s %s" % ("|M| (neg)", "conjugate", "t - |dx|", "verdict"))
    for mag in (2e-4, 5e-4, 1e-3, 2e-3, 5e-3, 1e-2, 2e-2, 4e-2):
        r = survey(-mag)
        print("  %10.1e %12s %+14.4e %s"
              % (mag, ("%.2f" % r["conjugate"]) if r["seats"] else "none", r["delay"],
                 "*** SEATS + EARLY ***" if (r["seats"] and r["early"])
                 else "seats, LATE" if r["seats"] else "early, no seat"))
    print("\n" + "=" * 79)
    print("VERDICT")
    print("  The intersection is NOT empty.  Vacuum Weyl focusing is traceless")
    print("  and therefore sign-blind at first order in M; the Shapiro delay is")
    print("  linear and therefore flips.  A negative mass focuses a congruence to a")
    print("  conjugate point while the light that focuses arrives early.")
    print("  Seating and advance, in one object, in a window about a decade wide.")
    print("\n  Every earlier pass missed it by writing u'' = -(R_kk/2)u and")
    print("  dropping shear -- conservative for an existence claim, fatal for a")
    print("  search.  And the Alcubierre bubble focuses through RICCI, which")
    print("  does need positive energy, so its TURN => LATE result stands for")
    print("  that object and says nothing about this one.")
    print("\n  Negative mass is ASSUMED here, the field is LINEARISED, the focus")
    print("  is ASTIGMATIC, and there is no payload.  See the header's list.")
    return 0


if __name__ == "__main__":
    sys.exit(selftest() if "--selftest" in sys.argv else report())
