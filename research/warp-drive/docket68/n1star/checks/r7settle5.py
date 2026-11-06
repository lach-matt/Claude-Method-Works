"""r7settle5.py -- SETTLE-GLAM5 round 7: the exterior regions of R6-A cut by the cone {r + 2(t~ - T) <= V_*} instead
of {Phi_W <= V_*}, so that the exterior estimate, and with it the finiteness and continuity of the energy, hold on
every interval on which |g^-1 - g_b0^-1|_op < 7/25, the bootstrap's class not assumed (the round-6 reader's minor 1:
Step 6's openness needs the continuity at sigma*, where the class is not yet known).
Setting as R4-D: g_b0 = eta + mu r^-2 k k on r >= 4R, mu r^-2 <= 1/16, t~ = t - f(r) with |f'| <= 1/4 there.

  K1 (exact, sympy) the two lateral conormals: beta := d(r + 2 t~) = 2 dt + (1 - 2 f') dr and alpha := d(r - 2 t~) =
     -2 dt + (1 + 2 f') dr have g_b0^-1(beta, beta) = (2 f' - 3)(2 f' + 1) - m (1 + 2 f')^2 and g_b0^-1(alpha, alpha) =
     (2 f' - 1)(2 f' + 3) - m (3 + 2 f')^2 (m := mu r^-2 >= 0), both <= -7/4 for |f'| <= 1/4 (their maxima over f',
     at m = 0, and decreasing in m); |beta|_E^2, |alpha|_E^2 <= 25/4; beta(d_t) = 2, alpha(d_t) = -2. Hence for every
     symmetric delta with |delta|_op < 7/25, (g_b0^-1 + delta)(beta, beta) < 0 and likewise alpha: both pieces are
     spacelike, r + 2 t~ increases and r - 2 t~ decreases along future causal curves, and the region between them lies
     to their past. Control (exact): 7/25 is sharp for the hypotheses |f'| <= 1/4, m >= 0 (attained only as m -> 0):
     at f' = -1/4, m = 0, delta = (7/25) beta beta^T/|beta|^2 makes beta null, and 3/10 makes it spacelike.
  K2 (sampled, 4000 points) the flux forms p -> T_g[p](d_t, n) on the two pieces (n = -g^-1 beta and n = g^-1 alpha,
     future timelike) for g^-1 = g_b0^-1 + delta, |delta|_op = 0.27 (random direction), |f'| <= 1/4, m in [0, 1/16],
     d_t future timelike: their least eigenvalue (exact over p) is positive at every point; and (round 8) in the worst
     directions at the size drawn, delta along beta beta^T at f' = -1/4 and along alpha alpha^T at f' = 1/4, m = 0,
     where the conormals' thresholds attain 7/25. Controls: R6-A's cut {Phi_W = V_*}, conormal dt + (1 - r^-2) dr, at
     |delta|_op = 3 r^-2 (r in [8, 400]) has a negative least eigenvalue somewhere (that cut needs the bootstrap's
     margin); and the cone at |delta|_op = 0.30 has a non-timelike conormal somewhere.
  K3 (exact and sampled) the margins from |H|: with g = g_b0 + H, g^-1 - g_b0^-1 = -g_b0^-1 H g^-1, so |g^-1 -
     g_b0^-1|_op <= s^2 |H|/(1 - s |H|) with s := |g_b0^-1|_op = m + (1 + m^2)^(1/2) (the (t, r) block of g_b0^-1 has
     the eigenvalues -m -+ (1 + m^2)^(1/2), the rest 1); at m = 1/16 the bound is <= 0.0232 for |H|_op <= 1/50 and
     <= 0.0474 for |H|_op <= 1/25 (0.0473378), both < 7/25, and g(d_t, d_t) <= -1 + m + |H| < 0 (exact); 2000 random H
     with |H|_op = 1/25 stay below the bound, and (round 8) H along g_b0's eigenvector of least |eigenvalue| attains it.
     Control: |H|_op = 1/4 gives a bound above 7/25.
  K4 (exact, sympy) the energy identity on the flat radial model of the cone region {t1 <= t <= t2, R + 2(t - t1) <= r
     <= V_* - 2(t - t1)}: E(t2) + F_in + F_out = E(t1) - int int phi_t box phi r^3 for a polynomial phi, the outer flux
     density r^3 (phi_t^2 + phi_r^2 - phi_t phi_r), whose form (round 8: derived from the identity's boundary term
     -rout'(t) e - phi_t phi_r and checked equal to the one typed) has eigenvalues 1/2, 3/2. Control: the outer piece
     at speed 1/2 (timelike) has a flux form with the eigenvalue -1/4.
  K5 (exact; round 8, the round-7 reader's nit 3) every metric with |g^-1 - g_b0^-1|_op <= delta < 7/25 (m <= 1/16,
     |f'| <= 1/4) has |g - g_b0|_op <= s^2 delta/(1 - s delta) <= 0.4521 (g - g_b0 = g (g_b0^-1 - g^-1) g_b0,
     |g_b0|_op = s), so g(d_t, d_t) <= -1 + 1/16 + 0.4521 < -0.485, and g^-1(dt~, dt~) <= g_b0^-1(dt~, dt~) + delta
     |dt~|_E^2 <= -15/16 + (7/25)(17/16) = -0.64 (g_b0^-1(dt~, dt~) = -1 + f'^2 - m(1 + f')^2): d_t is future timelike
     and the slices Sigma~ spacelike, with margins uniform in delta < 7/25. Control: at delta = 0.9 the bound on
     |g - g_b0| exceeds 15/16 and no longer keeps d_t timelike.
  K6 (exact; round 8, nit 4) Step 4's margin: |H|_op <= r^-2/4 with r >= 8 and m <= 1/16 gives |g^-1 - g_b0^-1|_op
     <= s^2 (r^-2/4)/(1 - s r^-2/4) <= 0.2847 r^-2 < r^-2/2, the margin of D4-D5 (B2d); |H|_op <= r^-2/2 would give
     0.57 r^-2 (control).
Labels: computed (K1, K4-K6 exact sympy; K2-K3 floating point, the least eigenvalue exact over the covector).

    python3 checks/r7settle5.py     (5 to 30 seconds)
"""
import random
import sys

import numpy as np
import sympy as sp
from sympy.calculus.util import maximum

import builtins as _builtins
import textwrap as _textwrap

_raw_print = _builtins.print


def print(*args, **kw):  # output lines are kept to 121 characters (wrapped, continuation indented)
    text = kw.pop("sep", " ").join(str(x) for x in args)
    for line in text.split("\n"):
        for piece in (_textwrap.wrap(line, 121, subsequent_indent="        ", break_long_words=True,
                                     replace_whitespace=False, drop_whitespace=True) or [""]):
            _raw_print(piece, **kw)


FAIL = []
Q = sp.Rational


def check(name, ok, msg=""):
    print(f"  {name}: {'pass' if ok else 'FAIL'} {msg}")
    if not ok:
        FAIL.append(name)


def part_k1():
    print("K1  the cone's conormals: spacelike pieces for every |delta|_op < 7/25")
    fp, m = sp.symbols("fp m", real=True)
    eta = sp.diag(-1, 1)
    lvec = sp.Matrix([-1, 1])            # l = g_b0^-1 k restricted to (t, r): (-1, xhat)
    beta = sp.Matrix([2, 1 - 2*fp])
    alpha = sp.Matrix([-2, 1 + 2*fp])
    gform = lambda c: (c.T*eta*c)[0] - m*((lvec.T*c)[0])**2
    gb, ga = sp.expand(gform(beta)), sp.expand(gform(alpha))
    ok_form = (sp.simplify(gb - ((2*fp - 3)*(2*fp + 1) - m*(1 + 2*fp)**2)) == 0
               and sp.simplify(ga - ((2*fp - 1)*(2*fp + 3) - m*(3 + 2*fp)**2)) == 0)
    I = sp.Interval(-Q(1, 4), Q(1, 4))
    mb, ma = maximum(gb.subs(m, 0), fp, I), maximum(ga.subs(m, 0), fp, I)
    dec = (sp.simplify(sp.diff(gb, m) + (1 + 2*fp)**2) == 0      # -(square): decreasing in m
           and sp.simplify(sp.diff(ga, m) + (3 + 2*fp)**2) == 0)
    nb, na = maximum((beta.T*beta)[0], fp, I), maximum((alpha.T*alpha)[0], fp, I)
    ok = ok_form and mb == -Q(7, 4) and ma == -Q(7, 4) and dec and nb == Q(25, 4) and na == Q(25, 4) \
        and beta[0] == 2 and alpha[0] == -2
    check("K1 g_b0^-1(beta, beta) = (2f' - 3)(2f' + 1) - m(1 + 2f')^2 and g_b0^-1(alpha, alpha) = (2f' - 1)(2f' + 3) - "
          "m(3 + 2f')^2, both <= -7/4 on |f'| <= 1/4 (decreasing in m), |beta|_E^2, |alpha|_E^2 <= 25/4, beta(d_t) = 2, "
          "alpha(d_t) = -2 (exact): (g_b0^-1 + delta) keeps both timelike for |delta|_op < 7/25", ok,
          f"maxima {mb}, {ma}; |.|_E^2 <= {nb}, {na}")
    # sharpness: f' = -1/4, m = 0, delta = c beta beta^T/|beta|^2
    b0 = beta.subs(fp, -Q(1, 4))
    val = lambda c: (b0.T*eta*b0)[0] + c*(b0.T*b0)[0]
    check("K1' control: 7/25 is sharp (f' = -1/4, m = 0, delta = c beta beta^T/|beta|^2): c = 7/25 makes beta null, "
          "c = 3/10 spacelike", val(Q(7, 25)) == 0 and val(Q(3, 10)) > 0, f"{val(Q(7, 25))}, {val(Q(3, 10))}")


def frame(rng):
    r_ = rng.uniform(8, 400)
    m_ = rng.uniform(0, 1/16)
    x = np.array([rng.gauss(0, 1) for _ in range(4)])
    xh = x/np.linalg.norm(x)
    E = np.diag([-1.0, 1, 1, 1, 1])
    k = np.concatenate(([1.0], xh))
    return r_, m_, xh, E - m_*np.outer(E@k, E@k)


def randsym(rng, size):
    A = np.array([[rng.uniform(-1, 1) for _ in range(5)] for _ in range(5)])
    D = (A + A.T)/2
    return D*size/max(abs(np.linalg.eigvalsh(D)))


def lam_min(gi, X, n):
    g = np.linalg.inv(gi)
    Qf = (np.outer(X, n) + np.outer(n, X))/2 - 0.5*(X@g@n)*gi
    return np.linalg.eigvalsh(Qf)[0], X@g@X, n@g@n


def part_k2():
    print("K2  the flux forms on the cone's two pieces at |delta|_op = 0.27, the class not assumed")
    rng = random.Random(77)
    X = np.array([1.0, 0, 0, 0, 0])
    worst, worst_tt, ctl_phi, ctl_cone = 1e9, -1e9, 1e9, -1e9
    worst_x, worst_xtt = 1e9, -1e9
    for _ in range(4000):
        r_, m_, xh, g0i = frame(rng)
        fp = rng.uniform(-0.25, 0.25)
        gi = g0i + randsym(rng, 0.27)
        beta = np.concatenate(([2.0], (1 - 2*fp)*xh))
        alpha = np.concatenate(([-2.0], (1 + 2*fp)*xh))
        for n in (-gi@beta, gi@alpha):
            lm, xx, nn = lam_min(gi, X, n)
            worst, worst_tt = min(worst, lm), max(worst_tt, xx, nn)
        # [R8] the worst directions at the size drawn: delta = size beta beta^T/|beta|^2 at f' = -1/4, m = 0 (beta's
        # threshold attains 7/25 there) and size alpha alpha^T/|alpha|^2 at f' = 1/4, m = 0 (alpha's)
        size = max(abs(np.linalg.eigvalsh(gi - g0i)))
        E0 = np.diag([-1.0, 1, 1, 1, 1])
        bx = np.concatenate(([2.0], 1.5*xh))
        ax = np.concatenate(([-2.0], 1.5*xh))
        for gx, n_of in ((E0 + size*np.outer(bx, bx)/(bx@bx), lambda g_: -g_@bx),
                         (E0 + size*np.outer(ax, ax)/(ax@ax), lambda g_: g_@ax)):
            lm, xx, nn = lam_min(gx, X, n_of(gx))
            worst_x, worst_xtt = min(worst_x, lm), max(worst_xtt, xx, nn)
        # control 1: R6-A's Phi_W cut at |delta| = 3 r^-2
        gi3 = g0i + randsym(rng, 3/r_**2)
        dP = np.concatenate(([1.0], (1 - 1/r_**2)*xh))
        lm3, _, _ = lam_min(gi3, X, -gi3@dP)
        ctl_phi = min(ctl_phi, lm3*r_**2)
        # control 2: the cone at |delta| = 0.30 along beta beta^T
        bb = np.outer(beta, beta)/(beta@beta)
        ctl_cone = max(ctl_cone, beta@(g0i + 0.30*bb)@beta)
    check("K2 at |delta|_op = 0.27, |f'| <= 1/4, m <= 1/16 (4000 points): d_t and both normals are future timelike "
          "and the "
          "flux forms' least eigenvalue (exact over the covector) is positive; [R8] so in the worst directions, "
          "delta = 0.27 beta beta^T/|beta|^2 at f' = -1/4 and 0.27 alpha alpha^T/|alpha|^2 at f' = 1/4, m = 0",
          worst > 0 and worst_tt < 0 and worst_x > 0 and worst_xtt < 0,
          f"min lambda_min {worst:.4f}, max g(X, X), g(n, n) {worst_tt:.4f}; worst directions: {worst_x:.5f}, "
          f"{worst_xtt:.5f}")
    check("K2' controls: R6-A's cut {Phi_W = V_*} at |delta|_op = 3 r^-2 has a negative least eigenvalue somewhere; the "
          "cone at |delta|_op = 0.30 has a non-timelike conormal somewhere", ctl_phi < 0 and ctl_cone > 0,
          f"min r^2 lambda_min {ctl_phi:.4f}; max g^-1(beta, beta) {ctl_cone:.4f}")


def part_k3():
    print("K3  the margin |g^-1 - g_b0^-1|_op from |H|_op")
    m, h = sp.symbols("m h", nonnegative=True)
    blk = sp.Matrix([[-1 - m, m], [m, 1 - m]])      # g_b0^-1 on (t, r)
    evs = list(blk.eigenvals())
    s_of = m + sp.sqrt(1 + m**2)
    ok_s = any(sp.simplify(e + s_of) == 0 for e in evs)
    bound = s_of**2*h/(1 - s_of*h)
    b50 = sp.N(bound.subs({m: Q(1, 16), h: Q(1, 50)}), 8)
    b25 = sp.N(bound.subs({m: Q(1, 16), h: Q(1, 25)}), 8)
    b4 = sp.N(bound.subs({m: Q(1, 16), h: Q(1, 4)}), 8)
    mono = sp.simplify(sp.diff(bound, m)) .subs({m: Q(1, 32), h: Q(1, 25)}) > 0
    tt = -1 + Q(1, 16) + Q(1, 25) < 0
    # [R8] the bound is attained: H = -sign(w) |H| e e^T along g_b0's eigenvector e of least |eigenvalue| w (m = 1/16)
    xh0 = np.array([1.0, 0, 0, 0])
    E = np.diag([-1.0, 1, 1, 1, 1])
    k0 = np.concatenate(([1.0], xh0))
    g0i_x = E - (1/16)*np.outer(E@k0, E@k0)
    g0_x = np.linalg.inv(g0i_x)
    w, Vv = np.linalg.eigh(g0_x)
    i0 = int(np.argmin(abs(w)))
    att = {}
    for hv in (1/50, 1/25):
        Hx = -np.sign(w[i0])*hv*np.outer(Vv[:, i0], Vv[:, i0])
        dx = np.linalg.inv(g0_x + Hx) - g0i_x
        att[hv] = max(abs(np.linalg.eigvalsh((dx + dx.T)/2)))
    attained = all(abs(att[hv] - float(sp.N(bound.subs({m: Q(1, 16), h: Q(1, 50) if hv == 1/50 else Q(1, 25)}), 20)))
                   < 1e-12 for hv in att)
    rng = random.Random(78)
    worst = 0.0
    for _ in range(2000):
        r_, m_, xh, g0i = frame(rng)
        g0 = np.linalg.inv(g0i)
        H = randsym(rng, 1/25)
        d = np.linalg.inv(g0 + H) - g0i
        worst = max(worst, max(abs(np.linalg.eigvalsh((d + d.T)/2))))
    check("K3 |g^-1 - g_b0^-1|_op <= s^2|H|/(1 - s|H|), s = m + (1 + m^2)^(1/2) the norm of g_b0^-1 (exact); at m = "
          "1/16: <= 0.0232 for |H| <= 1/50 and <= 0.0474 for |H| <= 1/25, both < 7/25, and g(d_t, d_t) <= -1 + m + |H| "
          "< 0; 2000 random H with |H|_op = 1/25 below the bound; [R8] H along g_b0's eigenvector of least |eigenvalue| "
          "attains it", ok_s and b50 < 0.0233 and b25 < 0.0474 and b25 < 0.28 and tt and mono
          and worst <= float(b25) and attained,
          f"bounds {b50}, {b25}; sampled max {worst:.4f}; attained {att[1/50]:.7f}, {att[1/25]:.7f}")
    check("K3' control: |H|_op = 1/4 gives a bound above 7/25", b4 > 0.28, str(b4))


def cone_identity(speed_out):
    t, r = sp.symbols("t r", positive=True)
    t1, t2, R, Vs = Q(0), Q(1, 2), Q(2), Q(9)
    phi = 1 + t*r - r**2/7 + t**2*r/3 + r**3/40 - t**3/5
    pt, pr = sp.diff(phi, t), sp.diff(phi, r)
    box = -sp.diff(phi, t, 2) + sp.diff(phi, r, 2) + 3*pr/r
    e = (pt**2 + pr**2)/2
    rin, rout = R + 2*(t - t1), Vs - speed_out*(t - t1)
    E1 = sp.integrate((e*r**3).subs(t, t1), (r, rin.subs(t, t1), rout.subs(t, t1)))
    E2 = sp.integrate((e*r**3).subs(t, t2), (r, rin.subs(t, t2), rout.subs(t, t2)))
    F_in = sp.integrate((r**3*(2*e + pt*pr)).subs(r, rin), (t, t1, t2))
    F_out = sp.integrate((r**3*(speed_out*e - pt*pr)).subs(r, rout), (t, t1, t2))
    bulk = sp.integrate(sp.integrate(sp.expand(pt*box*r**3), (r, rin, rout)), (t, t1, t2))
    form_out = sp.Matrix([[speed_out/2, -Q(1, 2)], [-Q(1, 2), speed_out/2]])
    # [R8] derived, not typed: on {r = rout(t)}, the outer boundary of {r <= rout}, d_t(e r^3) - d_r(phi_t phi_r r^3) =
    # -phi_t box phi r^3 leaves the boundary density -rout'(t) e - phi_t phi_r (times r^3); its form in (phi_t, phi_r)
    P_, R_ = sp.symbols("P_ R_")
    dens = -sp.diff(rout, t)*(P_**2 + R_**2)/2 - P_*R_
    derived = sp.Matrix([[sp.diff(dens, P_, 2)/2, sp.diff(dens, P_, R_)/2], [sp.diff(dens, P_, R_)/2,
                                                                             sp.diff(dens, R_, 2)/2]])
    return (sp.simplify(E2 + F_in + F_out - (E1 - bulk)) == 0 and sp.simplify(form_out - derived) == sp.zeros(2, 2),
            derived.eigenvals())


def part_k4():
    print("K4  the energy identity on the flat radial model of the cone region")
    ok, ev = cone_identity(Q(2))
    check("K4 E(t2) + F_in + F_out = E(t1) - int int phi_t box phi r^3 on {R + 2(t - t1) <= r <= V_* - 2(t - t1)} "
          "(exact); outer flux form, derived from the identity's boundary term ([R8]) and equal to the one typed, "
          "eigenvalues 1/2, 3/2", ok and set(ev) == {Q(1, 2), Q(3, 2)}, str(list(ev)))
    okc, evc = cone_identity(Q(1, 2))
    check("K4' control (outer piece at speed 1/2, timelike): the identity holds with it, its flux form has the "
          "eigenvalue "
          "-1/4", okc and Q(-1, 4) in evc, str(list(evc)))


def part_k5():
    print("K5  the general claim of R7-A, exact: d_t timelike and the slices spacelike for |delta|_op < 7/25")
    m, d, fp = sp.symbols("m delta fp", nonnegative=True)
    s_of = m + sp.sqrt(1 + m**2)
    gbound = s_of**2*d/(1 - s_of*d)
    g_at = sp.N(gbound.subs({m: Q(1, 16), d: Q(7, 25)}), 12)
    mono = (sp.diff(gbound, d).subs({m: Q(1, 16), d: Q(1, 10)}) > 0
            and sp.diff(gbound, m).subs({m: Q(1, 32), d: Q(1, 10)}) > 0)
    tt = -1 + Q(1, 16) + g_at
    fq = sp.Symbol("f", real=True)
    gtt = -1 + fq**2 - m*(1 + fq)**2                     # g_b0^-1(dt~, dt~), dt~ = dt - f' dr, l = (-1, xhat)
    I = sp.Interval(-Q(1, 4), Q(1, 4))
    mx = maximum(gtt.subs(m, 0), fq, I)
    nrm = maximum(1 + fq**2, fq, I)
    dec = sp.simplify(sp.diff(gtt, m) + (1 + fq)**2) == 0
    tslice = mx + Q(7, 25)*nrm
    g_ctl = sp.N(gbound.subs({m: Q(1, 16), d: Q(9, 10)}), 8) if (1 - (Q(1, 16) + sp.sqrt(1 + Q(1, 256)))*Q(9, 10)) > 0 \
        else sp.oo
    check("K5 |g - g_b0|_op <= s^2 delta/(1 - s delta) <= 0.4521 at delta = 7/25, m = 1/16 (increasing in both), so "
          "g(d_t, d_t) <= -1 + 1/16 + 0.4521 < -0.485; g^-1(dt~, dt~) <= max(g_b0^-1(dt~, dt~)) + (7/25) max |dt~|^2 = "
          "-15/16 + (7/25)(17/16) = -0.64 (exact)", g_at < 0.4522 and tt < -0.485 and mono and mx == -Q(15, 16)
          and nrm == Q(17, 16) and dec and tslice == -Q(16, 25), f"{g_at}, g(d_t, d_t) <= {sp.N(tt, 6)}, "
          f"g^-1(dt~, dt~) <= {tslice}")
    check("K5' control: at delta = 9/10 the bound on |g - g_b0| exceeds 15/16 (or is infinite): d_t no longer kept "
          "timelike", g_ctl > Q(15, 16), str(g_ctl))


def part_k6():
    print("K6  Step 4's margin: |H| <= r^-2/4 keeps |g^-1 - g_b0^-1| below r^-2/2")
    m, x = sp.symbols("m x", nonnegative=True)             # x := r^-2 <= 1/64
    s_of = m + sp.sqrt(1 + m**2)
    ratio = lambda c: sp.N((s_of**2*(c*x)/(1 - s_of*c*x)/x).subs({m: Q(1, 16), x: Q(1, 64)}), 10)
    r4, r2 = ratio(Q(1, 4)), ratio(Q(1, 2))
    check("K6 |H|_op <= r^-2/4 (r >= 8, m <= 1/16) gives |g^-1 - g_b0^-1|_op <= 0.2847 r^-2 < r^-2/2, the margin "
          "of D4-D5 "
          "(the bound increases with r^-2 and m)", r4 < 0.2848 and r4 < 0.5, str(r4))
    check("K6' control: |H|_op <= r^-2/2 gives 0.57 r^-2 > r^-2/2", r2 > 0.5, str(r2))


def main():
    for f in (part_k1, part_k2, part_k3, part_k4, part_k5, part_k6):
        f()
    print("FAILED:", FAIL if FAIL else "none")
    return 1 if FAIL else 0


if __name__ == "__main__":
    sys.exit(main())
