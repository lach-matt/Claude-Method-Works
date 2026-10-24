#!/usr/bin/env python3
"""edge5.py -- [Hin26c] sections 7-8 at n = 4: every place the census finds the dimension, computed at n = 3 against
the printed values and at n = 4 (N1STAR-PROOF.md section 10.67; ROUTES 4.68; D137).  Labels: computed (exact, sympy).

[Hin26c] (Hintz, arXiv:2606.28008) proves its propagation, radial point and energy estimates (sections 7-8) in 3 + 1
dimensions.  The census of those sections (122 rows, alphaXiv full text) finds the dimension in the edge form of the
operator at I+, in the K-current of section 8's energy estimate, in the round sphere's rotation fields, in the
densities and in a few counts.  Each is computed here.

  E1 (computed, exact) Minkowski's wave operator in the edge coordinates (t*, x_I = r^-(1/2), omega) of his (8.3):
     box = x_I^2 (x_I d_x_I - (n - 1)) d_t* + x_I^4 ((1/4)(x_I d_x_I)^2 - ((n - 2)/2) x_I d_x_I + Lap_S), on f(t*, r)
     Y(omega).  The second-order part, hence the characteristic set and the radial sets at I+, is the same at every n
     but for the sphere; the first-order part is his x_I d_x_I - 2(1 + p_1) with p_1 = 0 at n = 3, and x_I d_x_I - 3 =
     x_I d_x_I - 2(3/2) at n = 4: the "1" that 10.58(a) reads as (n - 1)/2.
  E2 (computed, exact) The K-current of (8.9)-(8.10): for X_0 = r^(2 alpha + 1)(d_t* + 2 r d_r), K = -(1/2)(L_X0
     g^-1)_munu T(d_mu, d_nu), T(X, Y) = X (x)_s Y - (1/2) g(X, Y) g^-1, on Minkowski: the d_t*^2 coefficient is -(2
     alpha + 1) r^(2 alpha) at both n (his (8.10), so his threshold alpha_I < -1/2 unchanged); the d_t* (x)_s x_I d_x_I
     coefficient -(n - 1) r^(2 alpha), -2 at n = 3 (his) and -3 at n = 4; the x_I^2 gslash^-1 coefficient -(2 alpha + n -
     1) r^(2 alpha), -2(alpha + 1) at n = 3 (his) and -(2 alpha + 3) at n = 4; and T(X_0, -grad t*) = (1/2) r^(2
     alpha)((x_I d_x_I)^2 + x_I^2 gslash^-1) at both, his second line.  With his large constant in front of T(X_0, -grad
     t*), K + 2 w T is positive definite on (dt*, dx_I/x_I) for every alpha < -1/2 at both n, exactly when w > (n -
     1)^2/(4 (-2 alpha - 1)): the determinant is the dt*^2 entry times w less (n - 1)^2/4 (D143).
  E3 (computed, exact) The sphere: the C(n, 2) rotation fields x_a d_b - x_b d_a span T S^(n-1) at every point (3
     fields on S^2, his V_3, V_4, V_5; 6 on S^3), and sum_(a<b) (x_a d_b - x_b d_a)^2 is the Laplacian of S^(n-1)
     (his Lap-slash as a sum of X_a X_b).
  E4 (computed, exact) The counts and densities: |dg| = r^(n-1) |dt* dr dgslash| = 2 x_I^(-2n) |dt* (dx_I/x_I)
     dgslash| (his x_I^-6; x_I^-8 at n = 4); the least integer above dim M/2 = (n + 1)/2 is 3 at both (Lemma 8.8's
     H^3_b); the commuting operators of Lemma 7.12, 2 + C(n, 2) + 1 (his N_0^6; 9 at n = 4); section 8.2's
     fields X_1, ..., X_(n+1) (4; 5) and their second-order monomials, (n + 1)(n + 2)/2 (10; 15), counted from the
     list of fields (D143).

Mutants: E1 with 2 for n - 1; E2 without the trace term; E3 with n - 1 rotation fields; E4 with r^(n-2).
sympy.  python3 edge5.py [--selftest | --mutants]   (under a minute)
"""
import itertools
import sys
import time

import sympy as sp

from damping5 import Checklist

ts, r, al = sp.symbols("tstar r alpha", real=True)


def minkowski(n):
    th = sp.symbols(f"th1:{n}")
    X = [ts, r] + list(th)
    N = n + 1
    g = sp.zeros(N, N)
    g[0, 0] = -1
    g[0, 1] = g[1, 0] = -1                                  # -dt*^2 - 2 dt* dr + r^2 g-hat, t* = t - r
    w = r**2
    for i in range(n - 1):
        g[2 + i, 2 + i] = w
        w = w * sp.sin(th[i])**2
    return X, g, g.inv()


# ------------------------------------------------------------------------------------------------- E1
def e1(control=0, verbose=False):
    chk = Checklist(verbose, quiet=control != 0)
    x = sp.Symbol("x", positive=True)                       # x_I
    lam = sp.Symbol("lam")                                  # Lap_S Y = -lam Y
    for n in (3, 4):
        cc, pp = sp.symbols("c p")
        rp = sp.Symbol("rp", positive=True)
        F = sp.exp(cc * ts) * x**pp                         # a test family, f(t*, r) = F(t*, r^-1/2)
        f = F.subs(x, rp**sp.Rational(-1, 2))
        # box on f(t*, r) Y: |g|^-1/2 d_i(|g|^1/2 g^ij d_j) with |g|^1/2 = r^(n-1) (angular part -lam/r^2)
        gtr = [[0, -1], [-1, 1]]
        Xr = [ts, rp]
        box = sum(sp.diff(rp**(n - 1) * gtr[i][j] * sp.diff(f, Xr[j]), Xr[i]) for i in range(2) for j in range(2))
        box = box / rp**(n - 1) - lam * f / rp**2
        xd = lambda u: x * sp.diff(u, x)
        m = n - 1 if control != 1 else 2
        edge = x**2 * (xd(sp.diff(F, ts)) - m * sp.diff(F, ts)) + x**4 * (xd(xd(F)) / 4 - sp.Rational(n - 2, 2) * xd(F)
                                                                         - lam * F)
        ok = sp.simplify(sp.powsimp(sp.expand(box - edge.subs(x, rp**sp.Rational(-1, 2))), force=True)) == 0
        chk(f"n = {n}: box = x^2 (x d_x - {n - 1}) d_t* + x^4 ((x d_x)^2/4 - ({n - 2}/2) x d_x + Lap_S)", ok)
    return chk.ok


# ------------------------------------------------------------------------------------------------- E2
def kcurrent(n, trace=True):
    X, g, gi = minkowski(n)
    N = n + 1
    V = [r**(2 * al + 1), 2 * r**(2 * al + 2)] + [0] * (n - 1)
    Lgi = sp.zeros(N, N)
    for m in range(N):
        for v in range(N):
            Lgi[m, v] = (sum(V[k] * sp.diff(gi[m, v], X[k]) for k in range(N))
                         - sum(gi[k, v] * sp.diff(V[m], X[k]) + gi[m, k] * sp.diff(V[v], X[k]) for k in range(N)))
    z = sp.symbols(f"z0:{N}")
    zz = sum(gi[a, b] * z[a] * z[b] for a in range(N) for b in range(N))
    tr = 1 if trace else 0
    K = sp.expand(-sum(Lgi[m, v] * (z[m] * z[v] - tr * g[m, v] * zz / 2) for m in range(N) for v in range(N)) / 2)
    # -grad t* = d_r; T(X0, d_r) = zeta(X0) zeta(d_r) - (1/2) g(X0, d_r) |zeta|^2
    gX = sum(g[a, 1] * V[a] for a in range(N))
    T = sp.expand(sum(V[a] * z[a] for a in range(N)) * z[1] - gX * zz / 2)
    # edge frame: zeta(d_t*) = z0, zeta(x_I d_x_I) = zeta(-2 r d_r) = e => z1 = -e/(2r); angular z2^2 has g-hat^11 = 1
    e = sp.Symbol("e")
    K, T = [sp.expand(q.subs(z[1], -e / (2 * r))) for q in (K, T)]
    lead = lambda c, p: sp.limit(sp.simplify(c / r**p), r, sp.oo)
    return {"tt": lead(K.coeff(z[0], 2), 2 * al), "te": lead(K.coeff(z[0], 1).coeff(e, 1), 2 * al),
            "ang": lead(K.coeff(z[2], 2), 2 * al - 1), "ee": lead(K.coeff(e, 2), 2 * al),
            "T_ee": lead(T.coeff(e, 2), 2 * al), "T_ang": lead(T.coeff(z[2], 2), 2 * al - 1),
            "T_te": lead(T.coeff(z[0], 1).coeff(e, 1), 2 * al), "T_tt": lead(T.coeff(z[0], 2), 2 * al)}


def e2(control=0, verbose=False):
    chk = Checklist(verbose, quiet=control != 0)
    for n in (3, 4):
        c = kcurrent(n, trace=control != 1)
        # his frame: d_t* (x)_s x_I d_x_I contributes 2 * (1/2) z0 e = z0 e per unit coefficient
        want = {"tt": -(2 * al + 1), "te": -(n - 1), "ang": -(2 * al + n - 1), "ee": 0,
                "T_ee": sp.Rational(1, 2), "T_ang": sp.Rational(1, 2), "T_te": 0, "T_tt": 0}
        got = {k: sp.simplify(v) for k, v in c.items()}
        chk(f"n = {n}: K = r^2a [{got['tt']} dt*^2 + {got['te']} dt* . x dx + ({got['ang']}) x^2 gslash^-1], "
            f"T = r^2a [{got['T_ee']} (x dx)^2 + {got['T_ang']} x^2 gslash^-1]",
            all(sp.simplify(got[k] - want[k]) == 0 for k in want))
        w = sp.Symbol("w", positive=True)
        M = sp.Matrix([[got["tt"], got["te"] / 2], [got["te"] / 2, got["ee"] + 2 * w * got["T_ee"]]])
        det = sp.expand(M.det())
        w0 = sp.solve(det, w)[0]
        lin = sp.degree(det, w) == 1 and sp.simplify(sp.diff(det, w) - got["tt"]) == 0
        chk(f"n = {n}: for every alpha < -1/2, K + 2 w T is positive on (dt*, dx_I/x_I) iff w > {sp.factor(w0)}: the "
            f"dt*^2 entry > 0 iff alpha < -1/2, and det = (that entry) w - (n - 1)^2/4",
            lin and sp.solve(got["tt"] > 0, al) == (al < sp.Rational(-1, 2))
            and sp.simplify(w0 - (n - 1)**2 / (4 * got["tt"])) == 0)
    return chk.ok


# ------------------------------------------------------------------------------------------------- E3
def e3(control=0, verbose=False):
    chk = Checklist(verbose, quiet=control != 0)
    for n in (3, 4):
        x = sp.symbols(f"x1:{n + 1}")
        pairs = list(itertools.combinations(range(n), 2))
        if control == 1:
            pairs = pairs[:n - 1]
        Om = [(a, b) for a, b in pairs]

        def rot(f, a, b):
            return x[a] * sp.diff(f, x[b]) - x[b] * sp.diff(f, x[a])
        # span: the vectors at a generic point of the sphere, as rows, have rank n - 1
        pt = {x[i]: sp.Rational(i + 1, 7) for i in range(n)}
        rows = []
        for a, b in Om:
            v = [0] * n
            v[a], v[b] = -x[b], x[a]
            rows.append([sp.sympify(c).subs(pt) for c in v])
        rk = sp.Matrix(rows).rank()
        rr = sp.sqrt(sum(xi**2 for xi in x))
        tests = [x[0] * x[1] / rr**2, x[0]**3 / rr**3, x[n - 1] * x[0]**2 / rr**3]
        lap = all(sp.simplify(sum(rot(rot(f, a, b), a, b) for a, b in Om)
                              - rr**2 * sum(sp.diff(f, xi, 2) for xi in x)) == 0 for f in tests)
        chk(f"n = {n}: {len(Om)} rotation fields span T S^{n - 1} (rank {rk}) and sum Omega^2 = Lap_S",
            rk == n - 1 and lap and len(Om) == n * (n - 1) // 2)
    return chk.ok


# ------------------------------------------------------------------------------------------------- E4
def e4(control=0, verbose=False):
    chk = Checklist(verbose, quiet=control != 0)
    x = sp.Symbol("x", positive=True)
    for n in (3, 4):
        rr = x**-2
        p = n - 1 if control != 1 else n - 2
        dens = sp.simplify(rr**p * sp.diff(rr, x) * x)      # r^(n-1) dr in units of dx/x
        chk(f"n = {n}: r^(n-1) |dr| = {sp.simplify(-dens)} |dx_I/x_I|", sp.simplify(-dens - 2 * x**(-2 * n)) == 0)
        k = (n + 1) // 2 + 1
        fields = sp.symbols(f"v0:{n + 1}")                   # d_t* and the n coordinate fields of R^n
        mono = list(itertools.combinations_with_replacement(fields, 2))
        chk(f"n = {n}: least integer above (n + 1)/2 = {k}; Lemma 7.12's operators {2 + n * (n - 1) // 2 + 1}; "
            f"section 8.2's fields {len(fields)} and their second-order monomials {len(mono)}",
            k == 3 and (2 + n * (n - 1) // 2 + 1) == (6 if n == 3 else 9) and len(fields) == n + 1
            and len(mono) == (10 if n == 3 else 15) == (n + 1) * (n + 2) // 2)
    return chk.ok


CHECKS = [("E1 box in edge coordinates at I+: second-order part n-free; first-order x d_x - (n - 1)", e1),
          ("E2 the K-current (8.10): dt*^2 coefficient -(2 alpha + 1) at both n; threshold alpha < -1/2 kept", e2),
          ("E3 the rotation fields of S^(n-1): C(n, 2), spanning, their squares sum to Lap_S", e3),
          ("E4 densities and counts: x_I^-2n; H^3_b at both n; 6 -> 9 operators; 10 -> 15 monomials", e4)]


def run(only=None, verbose=False):
    ok = True
    for k, (name, f) in enumerate(CHECKS, 1):
        if only and k != only:
            continue
        t0 = time.time()
        res = f(0, verbose)
        ok &= res
        print(f"{name[:104]:<104} {'PASS' if res else 'FAIL'} {time.time() - t0:3.0f}s", flush=True)
    n = 1 if only else len(CHECKS)
    print(f"edge5.py: {n if ok else 'not all'}/{n}")
    return ok


def mutants():
    caught = total = 0
    for name, f in CHECKS:
        total += 1
        res = f(1, False)
        caught += not res
        print(f"mutant 1 of {name[:2]}: {'caught' if not res else 'NOT caught'}", flush=True)
    print(f"edge5.py mutants: {caught}/{total}")
    return caught == total


if __name__ == "__main__":
    args = sys.argv[1:]
    vb = "--verbose" in args
    if "--selftest" in args:
        sys.exit(0 if run(verbose=vb) else 1)
    elif "--mutants" in args:
        sys.exit(0 if mutants() else 1)
    elif "--only" in args:
        sys.exit(0 if run(int(args[args.index("--only") + 1]), vb) else 1)
    print(__doc__)
