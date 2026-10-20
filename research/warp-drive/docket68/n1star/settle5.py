#!/usr/bin/env python3
"""settle5.py -- late-time settling of the hole after the shell, linearly, built on the copper study's barrier
(seed_escape.py E1) and measured at its seeds (D33).  Labels: computed (exact unless marked numerical), READ.

After the shell, g_lam is Tangherlini of the final mass plus lam m1 + O(lam^2) on Omega (Theorem 1, items 3-4); what
it settles to depends on how perturbations of five-dimensional Tangherlini in the class (T^2 with both reflections)
decay.  This program fixes which perturbation types the class contains and measures their ringdown on the barriers.

  T1 (computed, exact) The class has no vector-type perturbations and no linearised rotation.  A co-closed T^2-invariant
     vector field on S^3 (metric dth^2 + c^2 dphi1^2 + s^2 dphi2^2) is a(th) d_th + b1(th) d_phi1 + b2(th) d_phi2 with
     div = (cs)^-1 (cs a)' = 0, so a = C/(cs), smooth only for C = 0; what is left, b1 d_phi1 + b2 d_phi2, is odd under
     the reflections phi_i -> -phi_i, as are the linearised Myers-Perry rotations.  Only scalar-type and tensor-type
     perturbations remain, with harmonics of even degree l = 2k (seed_escape.py E3).  Control: no smoothness required.
  T2 (computed, exact) The potentials.  Cardoso, Lemos and Yoshida (READ below), (2.4) at n = 3: the tensor-type
     potential r^2 V/f = (2l + 3)(2l + 1)/4 + (9/4) x, x = r_h^2/r^2, is the copper study's barrier exactly; the
     scalar-type one is Q/(16 H^2) with their (2.5)-(2.7).  Control: the vector-type formula is not the barrier.
  T3 (computed, numerical) The ringdown on the copper study's barrier.  The 1+1 equation psi_tt - psi_r*r* + V psi = 0
     is evolved on a characteristic grid (step 0.1 r_h) from a Gaussian, and the fundamental mode is read off by a
     matrix pencil on t in [12, 50] r_h (tensor) and [12, 60] r_h (scalar), seen at r* = 10 r_h.  Tensor type, l = 2:
     omega r_h = 1.513 - 0.353 i; scalar type, l = 2: 0.948 - 0.257 i; both within 1% of the continued-fraction values
     READ (1.5106 + 0.3575 i and 0.9477 + 0.2561 i, time dependence e^(i omega t)).
     Control: the l = 4 tensor barrier, whose mode (2.5063 + 0.3550 i READ) is not the l = 2 value.
  T4 (computed) The settling times at the copper study's seeds.  The least-damped mode of the class is scalar-type
     l = 2, e-folding time r_h / 0.2561 = 3.905 r_h: 39.0, 54.5, 70.1 and 123.5 l5 for mu = 100, 195, 322 and 1000 l5^2
     (r_h = sqrt mu), the seeds of seed_escape.py E4.
  T5 (computed, numerical; D39, D44) No growing mode in the class for l = 2, ..., 10, both types, to tau = 275 r_h.
     The same 1+1 equation is marched by diagonals (slices of constant t) from a pulse launched at r* = 15 r_h, with
     T = 170 so that the computed slice, |r*| <= 2T - 15 - tau, covers the fixed region r* in [-20, 50] to tau = 275;
     the outgoing pulse has left that region by tau = 150 r_h after the launch, and from then to 275 the field's sup
     on it is below 1e-5 of its maximum (2.5e-6 at l = 2, 1e-14 at l = 10) and smaller on [200, 275] than on
     [100, 125].  A finite-time observation: growth rates above ln(1e5)/150 r_h = 0.08/r_h are excluded, slower ones
     are not.  Control: the potential's sign reversed grows (the ratio is 1).
  T6 (computed, numerical; D39) The late-time tail.  Measured from the launch, the l = 2 master fields of both types
     fall as a power law with local exponent 7.05 (tensor; 7.03 at step 0.05) and 7.06 (scalar) on tau in [550, 700]
     r_h, approaching 7 from above (7.41, 7.22, 7.12, 7.07 on [100, 150], [150, 250], [250, 400], [400, 550]), the
     two steps agreeing (so no ghost potential, [CYDL03] p. 5).  The origin is the launch; shifted by the launch
     radius, 15 r_h either way, the [550, 700] exponent moves to 6.89 and 7.23 and the earlier windows the other way
     (6.79 and 7.48 on [250, 400]), so the limit 7 is resolved and the direction of approach is not (the shifted pair
     brackets 7, checked).  The l = 4 tensor field, seen at r* = 30 where its tail
     is 3^5.5 times larger, gives 11.5 on [150, 250] before the floor of double precision.  READ:
     [CYDL03] (14), "Psi ~ t^-(2l+D-2), odd D", 7 and 11 at D = 5, their own D = 5 numerics 7.1 and 11.4 (Fig. 2).
     The tail is the flat odd-dimensional Green's function's, not the hole's ([CYDL03] p. 2, p. 4).  Control: the time
     origin placed at the run's own t = 0, 385 r_h after the launch, reads 2.65 from the same points.

READ (alphaXiv, 2026-10-20).  [CLY03b] V. Cardoso, J. P. S. Lemos and S. Yoshida, arXiv:hep-th/0311260v2, Tables 1-3,
pp. 8-9.  [HKW18] P.-K. Hung, J. Keller and M.-T. Wang, arXiv:1809.05144v1, p. 4, Theorem 2: "in spacetime dimension six
and below, the uniform decay estimate E^N_Psi(Sigma_tau) <= C(n, M) I_Psi(Sigma_0)/tau^2" for the master quantities of
every type; p. 4: "the remaining linearized metric components can be controlled by the gauge-invariant master
quantities ... We do not treat this matter in the current paper"; Theorem 1, p. 3: the l < 2 part is pure gauge plus
a linearised Myers-Perry solution.  [Sch10] V. Schlue, arXiv:1012.5963v1, p. 5, Theorem 1: E[phi](Sigma_tau) <= C D /
tau^2 for box phi = 0 on (n + 1)-dimensional Schwarzschild, n >= 3.  [CYDL03] V. Cardoso, S. Yoshida, O. J. C. Dias
and J. P. S. Lemos, arXiv:hep-th/0307122v3, (14) p. 4: "Psi ~ t^-(2l+D-2), odd D"; p. 4: "We have checked numerically
the result (14) for D = 5"; Fig. 2 caption: gravitational l = 2, 3, 4 give t^-7.1, t^-9.2, t^-11.4 against the predicted
-7, -9, -11; p. 2: "for odd dimensions the tail should basically be due to the flat space Green's function"; p. 5: the
ghost potential of a second-order scheme is detected by changing the grid size.

numpy, scipy, sympy.  python3 settle5.py [--selftest | --mutants]
"""
import sys

import numpy as np
import sympy as sp

READ_T = {2: 1.5106 + 0.3575j, 4: 2.5063 + 0.3550j}             # [CLY03b] Table 3, n = 0
READ_S = {2: 0.9477 + 0.2561j}                                   # [CLY03b] Table 1, n = 0


def t1(control=0):
    th = sp.Symbol("theta", positive=True)
    a = sp.Function("a")(th)
    c, s = sp.cos(th), sp.sin(th)
    sol = sp.dsolve(sp.Eq(sp.diff(c*s*a, th), 0), a).rhs                  # a = C1/(cos sin)
    C1 = list(sol.free_symbols - {th})[0]
    # the reflection-even co-closed fields are a d_th; b1 d_phi1 + b2 d_phi2 is odd, as are the linearised rotations
    blows_up = sp.limit(sol.subs(C1, 1), th, 0, "+") == sp.oo             # C1 != 0 is not smooth at the axis
    smooth_required = control != 1
    return bool(blows_up and smooth_required)


def potentials(l, kind, n=3):
    r, rh = sp.symbols("r r_h", positive=True)
    x = rh**2/r**2                                                         # 2M/r^(n-1) at n = 3
    if kind == "tensor":
        q = sp.Rational((2*l + n)*(2*l + n - 2), 4) + sp.Rational(n*n, 4)*x
    elif kind == "vector":
        q = sp.Rational((2*l + n)*(2*l + n - 2), 4) - sp.Rational(3*n*n, 4)*x
    else:
        m = l*(l + n - 1) - n
        H = m + sp.Rational(n*(n + 1), 2)*x
        Q = (n**4*(n + 1)**2*x**3 + n*(n + 1)*(4*(2*n*n - 3*n + 4)*m + n*(n - 2)*(n - 4)*(n + 1))*x**2
             - 12*n*((n - 4)*m + n*(n + 1)*(n - 2))*m*x + 16*m**3 + 4*n*(n + 2)*m**2)
        q = Q/(16*H**2)
    return r, rh, sp.simplify((1 - x)*q/r**2)


def t2(control=0):
    r, rh, V = potentials(2, "vector" if control == 1 else "tensor")
    ok = True
    for l in (2, 4, 6):
        r, rh, V = potentials(l, "vector" if control == 1 else "tensor")
        barrier = (1 - rh**2/r**2)*(((l + 1)**2 - sp.Rational(1, 4))/r**2 + sp.Rational(9, 4)*rh**2/r**4)
        ok &= sp.simplify(V - barrier) == 0
    return bool(ok)


def evolve(l, kind, h=0.1, T=120.0, obs=10.0):
    """characteristic (Gundlach-Price-Pullin) evolution in r_h = 1 units; returns psi(t) at r* = obs"""
    from scipy.optimize import brentq
    r, rh, Vs = potentials(l, kind)
    Vf = sp.lambdify(r, Vs.subs(rh, 1), "numpy")

    def r_of(rs):                                                          # r* = r + (1/2) log((r - 1)/(r + 1))
        g = lambda q: 1 + np.exp(q) + 0.5*(q - np.log(2 + np.exp(q))) - rs   # noqa: E731, q = log(r - 1)
        return 1 + np.exp(brentq(g, -400.0, np.log(abs(rs) + 20.0)))
    N = int(round(2*T/h))
    u = np.arange(N + 1)*h - T                                            # u = t - r*, v = t + r*
    v = np.arange(N + 1)*h - T
    Vd = np.array([float(Vf(r_of(k*h/2))) for k in range(-N, N + 1)])     # V on the diagonal j - i = k
    psi = np.zeros((N + 1, N + 1))
    psi[0, :] = np.exp(-(v - 0.0)**2/2.0)                                 # data on u = u0: a Gaussian in v
    for d in range(2, 2*N + 1):                                           # march on i + j = d
        i = np.arange(max(1, d - N), min(N, d - 1) + 1)
        j = d - i
        w, e, s_ = psi[i, j - 1], psi[i - 1, j], psi[i - 1, j - 1]
        psi[i, j] = w + e - s_ - h*h/8*Vd[(j - 1) - (i - 1) + N]*(w + e)
    t, sig = [], []
    for i in range(N + 1):
        j = i + int(round(2*obs/h))
        if j <= N:
            t.append((u[i] + v[j])/2); sig.append(psi[i, j])
    return np.array(t), np.array(sig)


def pencil(t, x, t0, t1, keep=6):
    """matrix pencil: the least-damped oscillating pole of the signal on [t0, t1], as omega r_h with e^(-i omega t)"""
    y = x[(t >= t0) & (t <= t1)]
    L = len(y)//2
    Y = np.array([y[i:i + L + 1] for i in range(len(y) - L)])
    V = np.linalg.svd(Y, full_matrices=False)[2].conj().T[:, :keep]
    z = np.linalg.eigvals(np.linalg.pinv(V[:-1, :]) @ V[1:, :])
    w = [1j*np.log(q)/(t[1] - t[0]) for q in z]
    return min((complex(abs(q.real), abs(q.imag)) for q in w if abs(q.real) > 0.3), key=lambda q: q.imag)


def qnm(l, kind):
    t, x = evolve(l, kind)
    return pencil(t, x, 12.0, 50.0) if kind == "tensor" else pencil(t, x, 12.0, 60.0)


def t3(control=0):
    lt = 4 if control == 1 else 2
    wt = qnm(lt, "tensor")
    ws = qnm(2, "scalar")
    close = lambda a, b: abs(a - b) <= 0.01*abs(b)                       # noqa: E731
    return bool(close(wt, READ_T[2]) and close(ws, READ_S[2]))


def t4(control=0):
    im = READ_S[2].imag if control == 0 else READ_T[2].imag
    want = {100: 39.0, 195: 54.5, 322: 70.1, 1000: 123.5}
    return all(abs(np.sqrt(mu)/im - val) < 0.06 for mu, val in want.items())


def march(l, kind, h=0.1, T=400.0, obs=(10.0,), sign=1.0, rs_lo=-20.0, rs_hi=200.0):
    """the same double-null scheme marched by diagonals i + j = const (slices of constant t), two diagonals kept, from a
    Gaussian in v on u = -T centred at v_c = -T + 30 (r* = 15 at launch, t_p = -T + 15); returns tau = t - t_p, the
    signal at each observer r* and the sup of |psi| over r* in [rs_lo, rs_hi] on every slice"""
    from scipy.optimize import brentq
    r, rh, Vs = potentials(l, kind)
    Vf = sp.lambdify(r, Vs.subs(rh, 1), "numpy")

    def r_of(rs):
        g = lambda q: 1 + np.exp(q) + 0.5*(q - np.log(2 + np.exp(q))) - rs           # noqa: E731
        return 1 + np.exp(brentq(g, -4000.0, np.log(abs(rs) + 20.0)))
    N = int(round(2*T/h))
    Vd = sign*np.array([float(Vf(r_of(k*h/2))) for k in range(-N, N + 1)])            # V at r* = k h/2
    v = np.arange(N + 1)*h - T
    vc, tp = -T + 30.0, -T + 15.0
    prev2 = np.zeros(N + 1); prev2[0] = np.exp(-(v[0] - vc)**2/2)                      # diagonal 0: psi[0, 0]
    prev1 = np.zeros(N + 1); prev1[0] = np.exp(-(v[1] - vc)**2/2)                      # diagonal 1: psi[0, 1], psi[1, 0]
    ko = [int(round(2*o/h)) for o in obs]
    taus, sig, sup = [], [[] for _ in obs], []
    for d in range(2, 2*N + 1):
        cur = np.zeros(N + 1)
        if d <= N:
            cur[0] = np.exp(-(v[d] - vc)**2/2)
        i = np.arange(max(1, d - N), min(N, d - 1) + 1)
        w, e, s_ = prev1[i], prev1[i - 1], prev2[i - 1]            # psi[i, j-1], psi[i-1, j], psi[i-1, j-1]
        cur[i] = w + e - s_ - h*h/8*Vd[(d - 2*i) + N]*(w + e)
        tau = (d*h - 2*T)/2 - tp
        rs = (d - 2*i)*h/2
        win = (rs >= rs_lo) & (rs <= rs_hi)
        taus.append(tau); sup.append(float(np.abs(cur[i][win]).max()) if win.any() else 0.0)
        for m, k in enumerate(ko):
            if (d - k) % 2 == 0 and 0 <= (d - k)//2 <= N and (d + k)//2 <= N:
                sig[m].append((tau, float(cur[(d - k)//2])))
        prev2, prev1 = prev1, cur
    return np.array(taus), [np.array(q) for q in sig], np.array(sup)


def exponent(tau, y, a, b):
    """the local power-law exponent -d log|y| / d log tau fitted on [a, b]"""
    m = (tau >= a) & (tau <= b) & (np.abs(y) > 0)
    return -np.polyfit(np.log(tau[m]), np.log(np.abs(y[m])), 1)[0]


def t5(control=0):
    ok = True
    for l in range(2, 11):
        for kind in ("tensor", "scalar"):
            T = 170.0
            tau, sig, sup = march(l, kind, T=T, sign=-1.0 if control == 1 else 1.0, rs_hi=50.0)
            cov = tau <= 2*T - 15.0 - 50.0           # the slice spans |r*| <= 2T - 15 - tau: covered to 275
            late = sup[(tau >= 150.0) & cov].max()/sup[cov].max()        # the outgoing pulse has left r* <= 50 by then
            falling = sup[(tau >= 200.0) & cov].max() < sup[(tau >= 100.0) & (tau <= 125.0)].max()
            ok &= late < 1e-5 and falling and bool(np.isfinite(sig[0][:, 1]).all())
            if not ok:
                return False
    return True


def t6(control=0):
    ok = True
    for kind, hs in (("tensor", (0.1, 0.05)), ("scalar", (0.1,))):
        for h in hs:
            tau, sig, _ = march(2, kind, h=h, T=400.0)
            t_, y = sig[0][:, 0], sig[0][:, 1]
            if control == 1:                 # the origin at the run's own t = 0, 385 after the launch: same data points
                ok &= abs(exponent(t_ - 385.0, y, 165.0, 315.0) - 7.0) < 0.1
                continue
            late, mid = exponent(t_, y, 550.0, 700.0), exponent(t_, y, 250.0, 400.0)
            ok &= abs(late - 7.0) < 0.1 and mid > late
            ok &= exponent(t_ - 15.0, y, 550.0, 700.0) < 7.0 < exponent(t_ + 15.0, y, 550.0, 700.0)   # the origin
    if control == 0:
        tau, sig, _ = march(4, "tensor", T=400.0, obs=(30.0,))               # the l = 4 tail is 3^5.5 larger there
        ok &= abs(exponent(sig[0][:, 0], sig[0][:, 1], 150.0, 250.0) - 11.0) < 0.6
    return bool(ok)


CHECKS = [("T1 the class has no vector-type perturbations and no linearised rotation", t1, 1),
          ("T2 the tensor-type potential of [CLY03b] at n = 3 is the copper study's barrier", t2, 1),
          ("T3 the ringdown on the barriers: l = 2 tensor and scalar modes within 1% of [CLY03b]", t3, 1),
          ("T4 the slowest e-folding time of the class at the copper study's seeds", t4, 1),
          ("T5 no growing mode in the class, l = 2..10, both types: the sup on a fixed region falls by 1e-5", t5, 1),
          ("T6 the late-time tail is t^-7 at l = 2 (both types, two grids) and t^-11 at l = 4: [CYDL03] (14)", t6, 1)]


def selftest():
    ok_all = True
    for name, f, nc in CHECKS:
        good = f()
        control = any(f(control=k) for k in range(1, nc + 1))
        state = "PASS" if good and not control else "FAIL"
        ok_all &= state == "PASS"
        print(f"{name:<100} {state}" + ("" if not control else "  (control passed: vacuous)"), flush=True)
    print(f"settle5.py: {len(CHECKS) if ok_all else 'FAILED'}/{len(CHECKS)}")
    return ok_all


def mutants():
    caught = total = 0
    for name, f, nc in CHECKS:
        for k in range(1, nc + 1):
            total += 1
            m = f(control=k)
            caught += (not m)
            print(f"mutant {k} of {name[:2]}: {'caught' if not m else 'NOT caught'}")
    print(f"settle5.py mutants: {caught}/{total}")
    return caught == total


if __name__ == "__main__":
    if "--mutants" in sys.argv:
        sys.exit(0 if mutants() else 1)
    sys.exit(0 if selftest() else 1)
