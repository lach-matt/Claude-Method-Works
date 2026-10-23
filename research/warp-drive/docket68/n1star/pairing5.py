#!/usr/bin/env python3
"""pairing5.py -- [Hin26] Lemma 8.12 in five dimensions: the L^2-pairings that make the zero energy kernel and cokernel
of the linearized gauge-fixed Einstein operator exact (N1STAR-PROOF.md section 10.32; ROUTES-OPEN.md 4.33; D88).
Labels: computed (exact, sympy), deduced, READ.

[Hin26] (arXiv:2606.28253v2) Proposition 8.11 (p. 155) counts the kernel of L-hat_b(0) -- the gauged linearized Kerr
metrics and the translations' deformation tensors, 1 + 3 + 3 = 7 -- and its cokernel, the dual states of his section 7.2,
by the pairings of his Lemma 8.12 (p. 157), whose proof is that of [Hin24b] Lemma 3.17 (arXiv:2408.06715, p. 51). That
proof removes the gauge terms by integration by parts and reduces each pairing to [Hin23b] Theorem 9.6 (arXiv:2306.07409,
pp. 104-109), where it is a boundary pairing at infinity,

    ell(b-dot)(h*) = lim_eps < [D-hat Ric(0), chi_eps] g'_b(b-dot), G (dt (x)_s omega*) >                       (9.22)

and, for the centre of mass, < [[D Ric, t]-hat(0), chi_eps] h_b,c + [D-hat Ric(0), chi_eps] h-breve_b,c,
G (dt (x)_s omega*) >, with h_b,c = delta*_gb (c . d_x^flat) and h-breve_b,c = [delta*_gb, t](c . d_x^flat) +
delta*_gb ((c . x) d_t^flat); only the Minkowski operators and the leading terms enter. His table: -8 pi m-dot (mass
against dt), -8 pi m (q . a-dot) (rotation against r^2 V(q) = (q x x) . dx), 4 pi m (q . c) (centre of mass against
d(r S(q)) = q . dx), every other entry 0 (a = 0). Here each pairing is computed directly: chi a radial cutoff, 1 near 0
and 0 near infinity, [P, chi] u paired with v in Cartesian coordinates, the integrand chi'(R) A + chi''(R) B, A and B
homogeneous so that R^(n-1) A is R^0 and R^(n-1) B is R^1, the sphere integrals exact, and the pairing -I_A + I_B (int
chi' = -1, int R chi'' = 1); a pairing below the critical weight is 0.

  P1 (computed, exact) His table in four dimensions, with the metric eta + mu R^-1 (dt^2 + dr^2), mu = 2m: mass against
     dt -4 pi mu-dot = -8 pi m-dot, against the translations and the rotations 0; the rotation g'(0, a-dot) = -(2 mu/R^3)
     dt (x)_s ((a-dot x x) . dx) against (q x x) . dx -4 pi mu per plane = -8 pi m (q . a-dot), the planes orthogonal,
     against dt and the translations 0; the centre of mass 2 pi mu (q . c) = 4 pi m (q . c), against dt 0, against the
     rotations 0 except along a plane's own directions, where the pairing sits above the critical weight, the leading
     terms vanish over the sphere and do not determine it (his value 0 at a = 0, Theorem 9.6(5)).  Control: G dropped
     from the dual slot.
  P2 (computed, exact) The Kerr rows in five dimensions, eta + mu R^-2 (dt^2 + dr^2), g'(0, A) = -(2 mu/R^4) dt (x)_s
     w_A, w_A = x^i dx^j - x^j dx^i on the plane ij (d_a g = -h_A, 10.28(vi)): mass against dt -3 pi^2 mu-dot, against
     the four translations and the six rotations 0; the rotations -2 pi^2 mu on their own plane, 0 across planes and
     against dt and the translations.  Control: the mass perturbation's dr^2 term dropped.
  P3 (computed, exact) The centres of mass in five dimensions: (3 pi^2/2) mu (q . c) against q . dx, 0 against dt and
     against the rotations of the planes not containing c's direction, undetermined by the leading terms against the
     three containing it; h-breve_b,c is O(mu), its Minkowski part the boost's Killing form.  Control: h-breve dropped.
  P4 (computed, exact) Non-degeneracy: with the undetermined entries as symbols, the 11 x 11 matrix (rows mass, six
     rotations, four centres of mass; columns dt, six rotations, four translations) is block triangular, its determinant
     (-3 pi^2) (-2 pi^2 mu)^6 (3 pi^2 mu/2)^4 free of them and nonzero for mu != 0; four dimensions the 7 x 7, (-4 pi)
     (-4 pi mu)^3 (2 pi mu)^3.  Control: the translations' first-order pairing < D Ric(t h_b,c), h* > in place of the
     centre of mass, which [Hin23b] Theorem 9.6(6) says vanishes, claimed non-degenerate.
  P5 (computed, exact) Invariance, both dimensions: the Kerr-Schild mass perturbation R^-(n-2) (dt + dr)^2, a pure gauge
     tensor delta*(log R dt), and t* = t - r in place of t give the same Kerr rows; [Hin23b] Theorem 9.6(1), (7).
     Control: a non-gauge R^-(n-2) dx_1^2 added, claimed invariant.

Deduced, not computed here (N1STAR-PROOF.md 10.32): the values are -8 pi M-dot, -8 pi J-dot and 4 pi M (q . c), M and J
the ADM mass and angular momentum (g_tt = -1 + 16 pi M/((n - 1) Omega_(n-1) r^(n-2)): M = 3 pi mu/8, J = pi mu a/4 in
five dimensions), as in four; [Hin26] Lemma 8.12 in five dimensions at a = 0, by his reduction, for his L_b of (8.1) (his
printed values are [Hin24b]'s, whose L, its (3.1a), is 2 (D Ric + ...)); the undetermined entries 0 at a = 0 by his
argument for Theorem 9.6(5), the rotations being Killing on Tangherlini so that h*_v1 is compactly supported, though the
non-degeneracy does not need them; the eleven kernel states and the eleven dual states independent, so his Proposition
8.11 with 11 for 7, dim ker = dim coker >= 11, equality resting on [AHW24] Theorem 6.1(2) in five dimensions (OPEN), and
his Corollary 8.13 with 11 for 7 on it.

READ.  [Hin26] pp. 145 ((8.1)), 154-158 (Proposition 8.9, Remark 8.10, Proposition 8.11 and its proof, (8.22)-(8.25),
Lemma 8.12, (8.26), Corollary 8.13 and its proof); [Hin24b] pp. 33 ((3.1a)), 38-39 (Lemma 3.8), 50-53 (Proposition 3.16,
Lemma 3.17 and its proof); [Hin23b] pp. 101-110 (Lemma 9.1, Definition 9.2, Lemma 9.3, Theorem 9.6, Lemma 9.7, the proof
of Theorem 9.6); alphaXiv, 2026-10-23.

sympy.  python3 pairing5.py [--selftest | --mutants]   (--verbose lists every sub-check)
"""
import sys
import time
from functools import lru_cache

import sympy as sp

from damping5 import Checklist

t, R, mu = sp.Symbol("t"), sp.Symbol("R", positive=True), sp.Symbol("mu")
chi = sp.Function("chi")(R)
c1, c2 = sp.symbols("c1 c2")


class Mink:
    """n + 1 Minkowski in Cartesian coordinates; R = |x| a symbol with d_i R = x_i/R"""

    def __init__(self, n):
        self.n, self.N = n, n + 1
        self.x = sp.symbols(f"x1:{n + 1}", real=True)
        self.eta = sp.diag(-1, *([1] * n))

    def d(self, f, i):
        if i == 0:
            return sp.diff(f, t)
        return sp.diff(f, self.x[i - 1]) + sp.diff(f, R) * self.x[i - 1] / R

    def dric(self, h):
        """D Ric on Minkowski: (1/2)(-box h + d_m d^a h_an + d_n d^a h_am - d_m d_n tr h)"""
        e, N, d = self.eta, self.N, self.d
        tr = sum(e[a, a] * h[a, a] for a in range(N))
        out = sp.zeros(N)
        for m in range(N):
            for v in range(m, N):
                s = -sum(e[a, a] * d(d(h[m, v], a), a) for a in range(N))
                s += sum(e[a, a] * (d(d(h[a, v], a), m) + d(d(h[a, m], a), v)) for a in range(N))
                s -= d(d(tr, m), v)
                out[m, v] = out[v, m] = s / 2
        return out

    def kcomm(self, h):
        """[D Ric, t] on a stationary h"""
        return self.dric(h.applyfunc(lambda q: t * q)).applyfunc(lambda q: q.subs(t, 0))

    def ip(self, A, B):
        e = self.eta
        return sum(A[a, b] * B[a, b] * e[a, a] * e[b, b] for a in range(self.N) for b in range(self.N))

    def G(self, h, drop=False):
        if drop:
            return h
        return h - self.eta * sum(self.eta[a, a] * h[a, a] for a in range(self.N)) / 2

    def sym(self, a, b):
        return sp.Matrix(self.N, self.N, lambda i, j: sp.Rational(1, 2) * (a[i] * b[j] + a[j] * b[i]))

    def form(self, k=None, plane=None, rad=False):
        w = [0] * self.N
        if k is not None:
            w[k] = 1
        if plane is not None:
            i, j = plane
            w[j + 1] += self.x[i]
            w[i + 1] += -self.x[j]
        if rad:
            w = [0] + [xi / R for xi in self.x]
        return w

    def sphere(self, poly):
        tot = 0
        for mon, c in sp.Poly(sp.expand(poly), *self.x).terms():
            if any(e % 2 for e in mon):
                continue
            b = [sp.Rational(e + 1, 2) for e in mon]
            tot += c * 2 * sp.prod([sp.gamma(bb) for bb in b]) / sp.gamma(sum(b))
        return sp.simplify(tot)

    def boundary(self, F):
        """lim of int F over R^n, F = chi'(R) A + chi''(R) B: -I_A + I_B at the critical weights, 0 below them; above
        them the leading terms do not determine the pairing: None if the sphere integral vanishes there"""
        F = sp.expand(F.subs(sp.Derivative(chi, (R, 2)), c2).subs(sp.Derivative(chi, R), c1).subs(chi, 0))
        tot, s = 0, sp.Symbol("s", positive=True)
        for c, crit in ((c1, 0), (c2, 1)):
            A = sp.together(F.coeff(c))
            if A == 0:
                continue
            ratio = sp.together(sp.simplify(A.subs({**{xi: s * xi for xi in self.x}, R: s * R}, simultaneous=True) / A))
            deg = sp.degree(sp.numer(ratio), s) - sp.degree(sp.denom(ratio), s)
            k = self.n - 1 + deg
            if k > crit:
                if self.sphere(sp.together(A.subs(R, 1))) != 0:
                    return sp.nan                                       # divergent: fails every comparison
                return None
            if k == crit:
                I = self.sphere(sp.together(A.subs(R, 1)))
                tot += -I if c == c1 else I
        return sp.simplify(tot)


@lru_cache(maxsize=None)
def geo(n):
    return Mink(n)


def comm(P, h):
    return P(h.applyfunc(lambda q: chi * q)) - P(h).applyfunc(lambda q: chi * q)


def massg(M, ks=False, extra=False, nodr=False):
    """d/d mu of eta + mu R^-(n-2) (dt^2 + dr^2) (or the Kerr-Schild (dt + dr)^2)"""
    dt, dr = M.form(0), M.form(rad=True)
    k = M.sym(dt, dt) + (sp.zeros(M.N) if nodr else M.sym(dr, dr))
    if ks:
        k = M.sym([a + b for a, b in zip(dt, dr)], [a + b for a, b in zip(dt, dr)])
    if extra:
        k = k + M.sym(M.form(1), M.form(1))
    return k.applyfunc(lambda q: q * R**(-(M.n - 2)))


def rotg(M, plane):
    """g'(0, A) = -(2/R^n) dt (x)_s w_A per unit mu (d_a g = -h_A, 10.28(vi); Kerr: -(4M/r^3) dt (x)_s (a x x) . dx)"""
    return M.sym(M.form(0), M.form(plane=plane)).applyfunc(lambda q: -2 * q / R**M.n)


def christ(M, g):
    N, d = M.N, M.d
    return [[[sp.expand(M.eta[l, l] * (d(g[l, a], b) + d(g[l, b], a) - d(g[a, b], l)) / 2) for b in range(N)]
             for a in range(N)] for l in range(N)]


def com_rows(M, i, nobrev=False, first=False):
    """the centre-of-mass source tensors, O(mu): [[D Ric, t]-hat, chi] h_b,c + [D-hat Ric, chi] h-breve_b,c"""
    N, d = M.N, M.d
    g = M.eta + massg(M).applyfunc(lambda q: mu * q)
    Gm = christ(M, g)
    lin = lambda A: A.applyfunc(lambda q: sp.expand(q).coeff(mu, 1))
    c = [0] * N
    c[i + 1] = 1
    hbc = lin(sp.Matrix(N, N, lambda a, b: sum(c[l] * d(g[a, b], l) for l in range(N)) / 2))
    w1 = [sum(g[a, l] * c[l] for l in range(N)) for a in range(N)]
    w2 = [M.x[i] * g[a, 0] for a in range(N)]
    dst = sp.Matrix(N, N, lambda a, b: (d(w2[b], a) + d(w2[a], b)) / 2 - sum(Gm[l][a][b] * w2[l] for l in range(N)))
    hb = M.sym(M.form(0), w1) + dst
    zero0 = hb.applyfunc(lambda q: sp.simplify(sp.expand(q).coeff(mu, 0))) == sp.zeros(N)
    hb = lin(hb)
    if first:                                                            # < D Ric(t h_b,c), h* >: Theorem 9.6(6)
        return comm(M.dric, hbc), zero0
    src = comm(M.kcomm, hbc) + (sp.zeros(N) if nobrev else comm(M.dric, hb))
    return src, zero0


def duals(M):
    """the dual columns: dt, the rotations (q x x) . dx per plane, the translations dx^j"""
    n = M.n
    planes = [(i, j) for i in range(n) for j in range(i + 1, n)]
    return [("dt", M.form(0))] + [(f"w{i + 1}{j + 1}", M.form(plane=(i, j))) for i, j in planes] + \
        [(f"dx{j}", M.form(j)) for j in range(1, n + 1)], planes


def pair_row(M, src, cols, dropG=False, tstar=False):
    dt = M.form(0)
    if tstar:
        dt = [a - b for a, b in zip(dt, M.form(rad=True))]
    return [M.boundary(M.ip(src, M.G(M.sym(dt, w), drop=dropG))) for _, w in cols]


@lru_cache(maxsize=None)
def matrix(n, dropG=False, tstar=False, ks=False, nobrev=False, nodr=False, gauge=False, extra=False, first=False):
    M = geo(n)
    cols, planes = duals(M)
    rows, ok0 = [], True
    if gauge:
        lg = sp.log(R)
        w = [lg] + [0] * n
        u = sp.Matrix(M.N, M.N, lambda a, b: (M.d(w[b], a) + M.d(w[a], b)) / 2)
        rows.append(pair_row(M, comm(M.dric, u), cols, dropG, tstar))
        return rows, ok0
    rows.append(pair_row(M, comm(M.dric, massg(M, ks=ks, nodr=nodr, extra=extra)), cols, dropG, tstar))
    for pl in planes:
        rows.append([None if q is None else mu * q for q in pair_row(M, comm(M.dric, rotg(M, pl)), cols, dropG, tstar)])
    for i in range(n):
        src, z0 = com_rows(M, i, nobrev=nobrev, first=first)
        ok0 &= z0
        rows.append([None if q is None else mu * q for q in pair_row(M, src, cols, dropG, tstar)])
    return rows, ok0


def undetermined(n):
    """the super-critical entries: the centre of mass along x^i against the rotations of the planes containing i (his
    0 at a = 0, Theorem 9.6(5))"""
    planes = [(i, j) for i in range(n) for j in range(i + 1, n)]
    k = len(planes)
    return {(1 + k + i, 1 + b) for i in range(n) for b, pl in enumerate(planes) if i in pl}


def agree(rows, W, n, idx):
    """the computed entries of the rows idx equal W's, and the undetermined ones are exactly where expected"""
    und = undetermined(n)
    ok = True
    for i in idx:
        for j, q in enumerate(rows[i]):
            ok &= (q is None) == ((i, j) in und)
            ok &= q is None or sp.simplify(q - W[i, j]) == 0
    return ok


def expected(n):
    """per mu-dot (mass row) and per mu (the others): diag(mass, rotations, centre of mass)"""
    k = n * (n - 1) // 2
    m, rot, com = (-4 * sp.pi, -4 * sp.pi, 2 * sp.pi) if n == 3 else (-3 * sp.pi**2, -2 * sp.pi**2, 3 * sp.pi**2 / 2)
    return sp.diag(m, *([rot * mu] * k), *([com * mu] * n))


# ------------------------------------------------------------------------------------------------- P1
def p1(control=0, verbose=False):
    chk = Checklist(verbose, quiet=control != 0)
    A, ok0 = matrix(3, dropG=control == 1)
    good = agree(A, expected(3), 3, range(7)) and ok0
    chk(f"n + 1 = 4: the diagonal {[A[i][i] for i in range(7)]} (mass, rotations 12, 13, 23, centres 1-3), the rest 0 "
        f"or (against the rotations) undetermined by the leading terms: with mu = 2m his -8 pi m-dot, -8 pi m "
        f"(q . a-dot), 4 pi m (q . c); [Hin23b] Theorem 9.6", good)
    return chk.ok


# ------------------------------------------------------------------------------------------------- P2
def p2(control=0, verbose=False):
    chk = Checklist(verbose, quiet=control != 0)
    A, _ = matrix(4, nodr=control == 1)
    good = agree(A, expected(4), 4, range(7))
    chk(f"n + 1 = 5: mass against dt {A[0][0]}, rotations on their planes {[A[i][i] for i in range(1, 7)]}, every "
        f"other Kerr-row entry 0 (mass against the rotations undetermined by the leading terms)", good)
    return chk.ok


# ------------------------------------------------------------------------------------------------- P3
def p3(control=0, verbose=False):
    chk = Checklist(verbose, quiet=control != 0)
    A, ok0 = matrix(4, nobrev=control == 1)
    good = agree(A, expected(4), 4, range(7, 11)) and ok0
    chk(f"n + 1 = 5: centres of mass against the translations {[A[i][i] for i in range(7, 11)]}, against dt 0, "
        f"against the rotations undetermined by the leading terms; h-breve_b,c is O(mu) (Minkowski part the boost's "
        f"Killing form: {ok0})", good)
    return chk.ok


# ------------------------------------------------------------------------------------------------- P4
def p4(control=0, verbose=False):
    chk = Checklist(verbose, quiet=control != 0)
    ok = True
    for n in (3, 4):
        rows, _ = matrix(n, first=control == 1)
        if any(q is None for i, row in enumerate(rows) for j, q in enumerate(row) if (i, j) not in undetermined(n)):
            ok = False
            continue
        A = sp.Matrix(len(rows), len(rows), lambda i, j: rows[i][j] if rows[i][j] is not None
                      else sp.Symbol(f"y_{i}_{j}"))
        det = sp.factor(A.det())
        good = det != 0 and not det.has(sp.nan) and not any(str(q).startswith("y_") for q in det.free_symbols)
        ok &= good
        chk(f"n + 1 = {n + 1}: det of the {A.shape[0]} x {A.shape[0]} pairing matrix = {det}, whatever the undetermined "
            f"entries", good)
    return chk.ok and ok


# ------------------------------------------------------------------------------------------------- P5
def p5(control=0, verbose=False):
    chk = Checklist(verbose, quiet=control != 0)
    ok = True
    for n in (3, 4):
        base, _ = matrix(n)
        k = 1 + n * (n - 1) // 2
        ks, _ = matrix(n, ks=True, extra=control == 1)
        ts, _ = matrix(n, tstar=True)
        ga, _ = matrix(n, gauge=True)
        same = lambda p, q: (p is None and q is None) or (p is not None and q is not None and sp.simplify(p - q) == 0)
        good = all(same(p, q) for p, q in zip(ks[0], base[0]))
        good &= all(same(p, q) for i in range(k) for p, q in zip(ts[i], base[i]))
        good &= all(q is None or sp.simplify(q) == 0 for q in ga[0])
        ok &= good
        chk(f"n + 1 = {n + 1}: Kerr-Schild mass row, t* = t - r, and delta*(log R dt) ({ga[0]}) leave the pairings "
            f"unchanged", good)
    return chk.ok and ok


CHECKS = [("P1 four dimensions: [Hin23b] Theorem 9.6's table, -8 pi m-dot, -8 pi m (q . a-dot), 4 pi m (q . c)", p1, 1),
          ("P2 five dimensions, Kerr rows: mass -3 pi^2 mu-dot against dt, rotations -2 pi^2 mu on their planes", p2, 1),
          ("P3 five dimensions, centres of mass: (3 pi^2/2) mu (q . c) against the translations, 0 elsewhere", p3, 1),
          ("P4 the 11 x 11 matrix (four dimensions 7 x 7) non-degenerate; the first-order translation pairing not", p4,
           1),
          ("P5 invariance: Kerr-Schild mass, t* = t - r, a pure gauge tensor; [Hin23b] Theorem 9.6(1), (7)", p5, 1)]


def selftest(verbose=False):
    ok_all = True
    for name, fn, nc in CHECKS:
        t0 = time.time()
        good = fn(verbose=verbose)
        control = any(fn(control=k) for k in range(1, nc + 1))
        state_ = "PASS" if good and not control else "FAIL"
        ok_all &= state_ == "PASS"
        print(f"{name:<112} {state_}  {time.time() - t0:.0f}s" + ("" if not control else "  (control passed: vacuous)"),
              flush=True)
    print(f"pairing5.py: {len(CHECKS) if ok_all else 'FAILED'}/{len(CHECKS)}")
    return ok_all


def mutants():
    caught = total = 0
    for name, fn, nc in CHECKS:
        for k in range(1, nc + 1):
            total += 1
            res = fn(control=k)
            caught += (not res)
            print(f"mutant {k} of {name[:2]}: {'caught' if not res else 'NOT caught'}", flush=True)
    print(f"pairing5.py mutants: {caught}/{total}")
    return caught == total


if __name__ == "__main__":
    args = sys.argv[1:]
    if "--mutants" in args:
        sys.exit(0 if mutants() else 1)
    if "--only" in args:
        k = int(args[args.index("--only") + 1])
        name, fn, _ = CHECKS[k - 1]
        print(name, fn(verbose=True))
        sys.exit(0)
    sys.exit(0 if selftest(verbose="--verbose" in args) else 1)
