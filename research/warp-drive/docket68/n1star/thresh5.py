#!/usr/bin/env python3
"""thresh5.py -- the structure and threshold quantities of the gauge potential operator in five dimensions: [Hin26]
Lemma 6.1 and (6.11), and the horizon threshold of his footnote 71 ([Hin26c] Definition 5.11) (N1STAR-PROOF.md section
10.18; ROUTES-OPEN.md 4.19; D60).  Labels: computed (exact, sympy), deduced, READ.

[Hin26c] (arXiv:2606.28008v1) works with stationary wave-type operators P_0 = -2 d_t* rho (rho d_rho - (n - 1)/2 - S)
+ P_0^(0) + Q d_t* - g00 d_t*^2 (Definition 9.4, n the spatial dimension; (5.1a) with 1 at n = 3), whose estimates
need threshold conditions: at the event horizon s > 1/2 + vartheta_H+, vartheta_H+ the supremum over N^*H+ of the
spectrum of (rho^2/(2 (r_+ - m))) xi^-1 sigma_1((P_0 - P_0^*)/2i) (Definition 5.11(4)); at infinity, through S-bar, the
bottom of the spectrum of S on the boundary ((9.16c), (9.20), Lemma 5.12).  [Hin26] Lemma 6.1 puts box^Ups in this
class with S = S_E; his Lemma 6.3 computes S-bar for E^Ups on Minkowski ((6.11)); his footnote 71 gives the horizon
threshold 3/2 at gamma_H = 0 for 1-forms.  Here the five-dimensional counterparts, with the trace weight 2/(D - 2) =
2/3 (10.12, U2), f = 1 - mu/r^2, r_h = mu^(1/2); rho^2/(2 (r_+ - m)) is 1/f'(r_+) at a = 0.

  U1 (computed, exact) On 4+1 Minkowski, t* = t - r, the Cartesian frame (dt, dx^i), box^Ups = 2 (delta + E) G delta*
     with E h = -gam (2 iota_c# h - (2/3)(1 - e) c tr h), c = r^-1 dt: no d_t*^2 term, the mixed terms 2 d_t* d_r, and
     the d_t* terms (3/r) + (2/r) S-bar, that is -2 d_t* rho (rho d_rho - 3/2 - S-bar), with S-bar omega = gam (omega +
     omega_t dt* + e <dt*, omega> dt).  Four-dimensional control: weight 1, (1/r)(2 + 2 S-bar), rho d_rho - 1, the same
     S-bar.  Control: the weight 1 in five dimensions, where S-bar omega = gam (omega + omega_t dt* + ((3e - 1)/2)
     <dt*, omega> dt).
  U2 (computed, exact) The spectrum of S-bar: gam (1 - e), 2 gam, and gam on the three angular directions -- his
     (6.11)'s, (1 - e) gam, 2 gam, gam, in any dimension at the weight 2/(D - 2), since (2/(D - 2))(1 - D/2) = -1.
     Control: at the weight 1 in five dimensions it is (3/2)(1 - e) gam, 2 gam, gam.
  U3 (computed, exact) The horizon threshold.  In the ingoing chart, at N^*H+ (r = r_h, zeta = xi dr), the
     subprincipal symbol of box^Ups_H = box + 2 gam_H E_H G delta* on half densities by |dg|, E_H h = 2 iota_c_H# h -
     (2/3) c_H tr h, c_H = c_v dv + c_r dr, is i xi f'(r_h) K with K lower triangular of eigenvalues 1 + c_v gam_H r_h,
     -1 + 2 c_v gam_H r_h, c_v gam_H r_h (three times): vartheta_H+ = 1 at gam_H = 0, and for c_v = 0 (10.15's c_H =
     -(1/2) chi dr) at every gam_H; the threshold s > 3/2.  Four-dimensional control: 1 + 2 c_v gam mu, -1 + 4 c_v gam
     mu, 2 c_v gam mu (twice), so 3/2 at gam_H = 0 (his footnote 71).  Control: the scalar wave operator, K = 0, the
     threshold 1/2.
  U4 (computed, exact) On Tangherlini, t* = t - r: g^-1(dt*, dt*) = -(2 mu rho^2 - mu^2 rho^4)/(1 - mu rho^2), in rho^2
     C^oo as Lemma 6.1 asks; and g - g-bar = (mu rho^2/(1 - mu rho^2)) (dt^2 + ... ) is O(rho^2) in the frame (dt,
     dr, r dw) where Schwarzschild's is O(rho).  Control: the four-dimensional f = 1 - mu/r in five dimensions, O(rho).

Deduced, not computed here: (6.7) in five dimensions with one power to spare -- S_E - S-bar in rho^2 C^oo and the
zero energy operators' difference in rho^4 Diff_b^2, the Christoffel symbols of Tangherlini differing from
Minkowski's by O(rho^3) where Kerr's differ by O(rho^2); and, the transport equation (rho d_rho - 3/2 - S-bar) u = 0
giving u ~ rho^(3/2 + S-bar), outgoing kernel elements of the spectral family in A^(3/2 + S-bar - eps) (his (9.20) has
1 + S-bar), the threshold at R_out (9.16c), r + alpha < -1/2 + S-bar, unchanged for scattering Sobolev spaces on the
Euclidean density.  Not deduced: the radial point estimates themselves in five dimensions ([Hin26c] section 9.2).

READ.  [Hin26] pp. 113-115 (Lemma 6.1, (6.4a)-(6.7), Remark 6.2, Lemma 6.3, (6.10)-(6.11)), 124 (footnote 71);
[Hin26c] pp. 101 (Example 5.4, Remark 5.6), 104-105 (Definition 5.10, Definition 5.11, Lemma 5.12), 158 (Definition
9.4), 163 ((9.16a)-(9.16c), Theorem 9.5, (9.20)); alphaXiv, 2026-10-22.

sympy.  python3 thresh5.py [--selftest | --mutants]   (--verbose lists every sub-check)
"""
import sys
import time

import sympy as sp

import gaugepot5 as G
from damping5 import Checklist
from modes5 import canon

D = sp.diff
mu = G.mu
gam, e = sp.symbols("gamma e")


def minkowski(n, weight):
    """2 (delta + E) G delta* on 1-forms of (n+1)-Minkowski, Cartesian frame, coordinates (t*, x), t* = t - r"""
    T = sp.Symbol("T")
    x = sp.symbols("x1:%d" % (n + 1), real=True)
    r = sp.sqrt(sum(xi**2 for xi in x))
    N = n + 1
    eta = sp.diag(-1, *([1]*n))
    W = [sp.Function("W%d" % a)(T, *x) for a in range(N)]

    def d(fn, mu_):
        return D(fn, T) if mu_ == 0 else D(fn, x[mu_ - 1]) - x[mu_ - 1]/r*D(fn, T)

    S = sp.Matrix(N, N, lambda a, b: (d(W[b], a) + d(W[a], b))/2)
    trS = sum(eta[a, a]*S[a, a] for a in range(N))
    Gh = S - eta*trS/2
    c = [1/r] + [0]*n
    cs = [eta[a, a]*c[a] for a in range(N)]
    trG = sum(eta[a, a]*Gh[a, a] for a in range(N))
    E = [-gam*(2*sum(cs[k]*Gh[k, a] for k in range(N)) - weight*(1 - e)*c[a]*trG) for a in range(N)]
    dl = [-sum(eta[k, k]*d(Gh[a, k], k) for k in range(N)) for a in range(N)]
    P = [sp.expand(2*(dl[a] + E[a])) for a in range(N)]
    return dict(P=P, W=W, T=T, x=x, r=r, N=N, eta=eta)


def exact0(q, x):
    """q == 0 exactly: x = R u(s), u the inverse stereographic chart of the unit sphere, so that |x| = R"""
    n = len(x)
    sv = sp.symbols("s1:%d" % n)
    den = 1 + sum(a**2 for a in sv)
    u = [(1 - sum(a**2 for a in sv))/den] + [2*a/den for a in sv]
    R = sp.Symbol("R", positive=True)
    return sp.simplify(sp.radsimp(sp.together(q.subs({x[i]: R*u[i] for i in range(n)})))) == 0


def sbar_formula(n, k):
    """S-bar omega = gam (omega + omega_t dt* + k <dt*, omega> dt) as a matrix on Cartesian components"""
    x = sp.symbols("x1:%d" % (n + 1), real=True)
    r = sp.sqrt(sum(xi**2 for xi in x))
    N = n + 1
    dts = [1] + [-xi/r for xi in x]
    M = sp.zeros(N, N)
    for b in range(N):
        om = [1 if a == b else 0 for a in range(N)]
        pair = -om[0]*dts[0] + sum(om[a]*dts[a] for a in range(1, N))
        out = [gam*(om[a] + om[0]*dts[a] + k*pair*(1 if a == 0 else 0)) for a in range(N)]
        for a in range(N):
            M[a, b] = out[a]
    return M


# ------------------------------------------------------------------------------------------------- U1
def u1(control=0, verbose=False):
    chk = Checklist(verbose, quiet=control != 0)
    for n in ((4,) if control else (4, 3)):
        w = sp.Rational(2, n - 1) if control != 1 else 1
        Mk = minkowski(n, w)
        P, W, T, x, r, N = Mk["P"], Mk["W"], Mk["T"], Mk["x"], Mk["r"], Mk["N"]
        no_tt = all(exact0(P[a].coeff(D(W[b], T, 2)), x) for a in range(N) for b in range(N))
        mixed = all(exact0(P[a].coeff(D(W[b], T, x[i])) - (2*x[i]/r if a == b else 0), x)
                    for a in range(N) for b in range(N) for i in range(n))
        Sb = sp.Matrix(N, N, lambda a, b: r/2*P[a].coeff(D(W[b], T)) - (sp.Rational(n - 1, 2) if a == b else 0))
        k = e if control != 1 else (3*e - 1)/2
        same = all(exact0(q, x) for q in Sb - sbar_formula(n, e))
        chk(f"n + 1 = {n + 1}: no d_t*^2 term, mixed terms 2 d_t* d_r, d_t* terms ((n - 1) + 2 S-bar)/r with S-bar "
            f"omega = gam (omega + omega_t dt* + e <dt*, omega> dt) (weight {w})", no_tt and mixed and same)
        if control == 1:
            chk("weight 1 in five dimensions: S-bar has k = (3e - 1)/2 in place of e",
                all(exact0(q, x) for q in Sb - sbar_formula(n, k)))
    return chk.ok


# ------------------------------------------------------------------------------------------------- U2
def u2(control=0, verbose=False):
    chk = Checklist(verbose, quiet=control != 0)
    for n in ((4,) if control else (4, 3)):
        k = e if control != 1 else (3*e - 1)/2
        M = sbar_formula(n, k)
        x = sp.symbols("x1:%d" % (n + 1), real=True)
        Mp = M.subs({x[0]: 1, **{xi: 0 for xi in x[1:]}})       # at a boundary point; the spectrum is rotation-invariant
        ev = {sp.factor(a): m for a, m in Mp.eigenvals().items()}
        want = {sp.factor(gam*(1 - e)): 1, 2*gam: 1, gam: n - 1}
        chk(f"n + 1 = {n + 1}: spec S-bar = gam (1 - e), 2 gam, gam ({n - 1} times), his (6.11)'s", ev == want)
    return chk.ok


# ------------------------------------------------------------------------------------------------- U3
def u3(control=0, verbose=False):
    chk = Checklist(verbose, quiet=control != 0)
    gH, cv, cr, xi = sp.symbols("gamma_H c_v c_r xi")
    for n in ((4,) if control else (4, 3)):
        C = G.ch(n, "ingoing")
        X, gi, N, r, f, th = C["X"], C["gi"], C["N"], C["r"], C["f"], C["ang"][0]
        rh = mu if n == 3 else sp.sqrt(mu)
        m = C["vol"]
        z = sp.symbols("z0:%d" % N)
        if control == 1:                                     # the scalar wave operator
            v = sp.Function("v")(*X)
            u = m**sp.Rational(-1, 2)*v
            Pc = sp.expand(m**sp.Rational(1, 2)*(-sum(D(m*gi[a, b]*D(u, X[b]), X[a])
                                                     for a in range(N) for b in range(N))/m))
            p2 = sum(Pc.coeff(D(v, X[j], X[k]) if j != k else D(v, X[j], 2))*(sp.I*z[j])*(sp.I*z[k])
                     * (1 if j == k else sp.Rational(1, 2)) for j in range(N) for k in range(N))
            p1 = sum(Pc.coeff(D(v, X[j]))*(sp.I*z[j]) for j in range(N))
            sub = p1 - sum(D(D(p2, X[j]), z[j]) for j in range(N))/(2*sp.I)
            K = canon(sub.subs({z[0]: 0, z[1]: xi, **{z[k]: 0 for k in range(2, N)}})/(sp.I*xi), th).subs(r, rh)
            chk("scalar: vartheta_H+ = 1", sp.simplify(K/D(f, r).subs(r, rh) - 1) == 0)
            continue
        v = [sp.Function("v%d" % a)(*X) for a in range(N)]
        w = [m**sp.Rational(-1, 2)*q for q in v]
        c = [cv, cr] + [0]*(n - 1)
        cs = [sum(gi[k, j]*c[j] for j in range(N)) for k in range(N)]
        wt = 1 if n == 3 else sp.Rational(2, 3)
        T = G.Gop(C, G.dstar(C, w))
        EGT = [2*sum(cs[k]*T[k, j] for k in range(N)) - wt*c[j]*G.trace(C, T) for j in range(N)]
        B = G.box(C, w)
        P = [sp.expand(m**sp.Rational(1, 2)*(B[a] + 2*gH*EGT[a])) for a in range(N)]
        K = sp.zeros(N, N)
        for a in range(N):
            for b in range(N):
                p2 = sum(P[a].coeff(D(v[b], X[j], X[k]) if j != k else D(v[b], X[j], 2))*(sp.I*z[j])*(sp.I*z[k])
                         * (1 if j == k else sp.Rational(1, 2)) for j in range(N) for k in range(N))
                p1 = sum(P[a].coeff(D(v[b], X[j]))*(sp.I*z[j]) for j in range(N))
                sub = p1 - sum(D(D(p2, X[j]), z[j]) for j in range(N))/(2*sp.I)
                at = sub.subs({z[0]: 0, z[1]: xi, **{z[k]: 0 for k in range(2, N)}})
                K[a, b] = canon(sp.simplify(at/(sp.I*xi)), th).subs(r, rh)
        Kn = (K/sp.simplify(D(f, r).subs(r, rh))).applyfunc(sp.simplify)
        s = rh if n == 4 else 2*mu
        lower = all(Kn[a, b] == 0 for a in range(N) for b in range(N) if b > a)
        diag = [sp.simplify(Kn[a, a]) for a in range(N)]
        want = [1 + cv*gH*s, -1 + 2*cv*gH*s] + [cv*gH*s]*(n - 1)
        chk(f"n + 1 = {n + 1}: K/f'(r_h) lower triangular with diagonal 1 + c_v gam_H s, -1 + 2 c_v gam_H s, c_v "
            f"gam_H s (s = {s} = 2/f'(r_h)): vartheta_H+ = 1 at gam_H = 0 or c_v = 0, threshold 3/2",
            lower and all(sp.simplify(p - q) == 0 for p, q in zip(diag, want)))
    return chk.ok


# ------------------------------------------------------------------------------------------------- U4
def u4(control=0, verbose=False):
    chk = Checklist(verbose, quiet=control != 0)
    rho = sp.Symbol("rho", positive=True)
    f = 1 - mu*rho**2 if control != 1 else 1 - mu*rho
    g00 = sp.simplify(-1/f + f)                              # g^-1(dt - dr, dt - dr), static chart
    want = -(2*mu*rho**2 - mu**2*rho**4)/(1 - mu*rho**2)
    dev = [sp.simplify(-f + 1), sp.simplify(1/f - 1)]        # g - g-bar in (dt, dr): -f + 1, 1/f - 1
    order = min(sp.Poly(sp.series(x, rho, 0, 6).removeO(), rho).monoms()[-1][0] for x in dev)
    chk("g^-1(dt*, dt*) = -(2 mu rho^2 - mu^2 rho^4)/(1 - mu rho^2), and g - g-bar = O(rho^2) in (dt, dr, r dw)",
        sp.simplify(g00 - want) == 0 and order == 2)
    return chk.ok


CHECKS = [("U1 Lemma 6.1 on 4+1 Minkowski: -2 d_t* rho (rho d_rho - 3/2 - S-bar), S-bar = gam (1 + omega_t dt* + ...)",
           u1, 1),
          ("U2 spec S-bar = gam (1 - e), 2 gam, gam at the weight 2/3: his (6.11)'s (four-dimensional control)", u2, 1),
          ("U3 the horizon threshold: vartheta_H+ = 1, s > 3/2, at gam_H = 0 and for c_H = c_r dr at every gam_H",
           u3, 1),
          ("U4 Tangherlini at infinity: g00 in rho^2 C^oo, g - g-bar = O(rho^2)", u4, 1)]


def selftest(verbose=False):
    ok_all = True
    for name, fn, nc in CHECKS:
        t0 = time.time()
        good = fn(verbose=verbose)
        control = any(fn(control=k) for k in range(1, nc + 1))
        state = "PASS" if good and not control else "FAIL"
        ok_all &= state == "PASS"
        print(f"{name:<112} {state}  {time.time() - t0:.0f}s" + ("" if not control else "  (control passed: vacuous)"),
              flush=True)
    print(f"thresh5.py: {len(CHECKS) if ok_all else 'FAILED'}/{len(CHECKS)}")
    return ok_all


def mutants():
    caught = total = 0
    for name, fn, nc in CHECKS:
        for k in range(1, nc + 1):
            total += 1
            res = fn(control=k)
            caught += (not res)
            print(f"mutant {k} of {name[:2]}: {'caught' if not res else 'NOT caught'}", flush=True)
    print(f"thresh5.py mutants: {caught}/{total}")
    return caught == total


if __name__ == "__main__":
    args = sys.argv[1:]
    if "--mutants" in args:
        sys.exit(0 if mutants() else 1)
    sys.exit(0 if selftest(verbose="--verbose" in args) else 1)
