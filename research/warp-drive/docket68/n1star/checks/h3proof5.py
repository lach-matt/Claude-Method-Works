#!/usr/bin/env python3
"""h3proof5: the structural proof of twohorizon5 H3 -- the outgoing expansion has no harmonic depending on s2 at order
lam (FAMILIES5-FULL.md section 9; the verifier of Part V's proof, its scripts banked here).

Claim: with both families' stage-0 waves and ghat_2's mixed harmonics fixed by stage 0's division, the lam^1 coefficient
of the expansion theta_du of the spheres {u, v = const} has no harmonic depending on s2. Proof, in two computed steps:
  (S) frozen coefficients (exact and symbolic in E = e^(2 sig), the angular metric r1, r2, r3 and every amplitude;
      harmonics z^(+-1), z^(+-2) of both phases, so both sign patterns of the mixed harmonics, e.g. (1, -1), occur):
      (S1) the angular trace of Ric^H at lam^0 on the mixed harmonics is gamma0^AB R^(0)_AB|mixed = -2 g0^uv F1 F2
           (a2)|mixed, a2 := (1/2) tr_gamma0 Q - (1/4) |W_AB|^2_gamma0 -- the lam^0 form of the colliding-plane-wave
           identity gamma^AB R_AB = -alpha^-1 box_h alpha, alpha = sqrt(det gamma) (Szekeres), whose gauge term
           carries only angular derivatives and so is slow; the mixed harmonics need two fast derivatives, so only
           point values enter;
      (S2) after the division Q_n := -R^(0)_n/sym(n) (all fifteen components; sym = -g0^uv n1 n2), R^(0) has no mixed
           harmonic, so a2|mixed = 0;
      (S3) the lam^1 coefficient of theta_du is g0^uv F1 a2 exactly (frozen), so it has no s2-dependent harmonic.
      Control (must fail): no division (Q = 0): a2 has mixed harmonics and theta_du's lam^1 term has four.
  (T) non-frozen (symbolic in every function of (u, v, th) on the general round double-null background): the lam^1
      coefficient of theta_du minus g0^uv F1 a2 is independent of s2 (the remainder carries slow derivatives and s1
      only). Control (must fail): the angular inverse metric taken without its lam corrections leaves an
      s2-dependent remainder.
Hence theta_du's lam^1 term has no s2-dependent harmonic for every function, not only at sample points: item 6's
decisive cancellation is deduced, with the identities computed. Labels: computed (exact, sympy).
Run: python3 checks/h3proof5.py   (about six minutes)
"""
import sys
import time
import sympy as sp

N = 5
U, V = 0, 1
E, r1, r2, r3 = sp.symbols("E r1 r2 r3", positive=True)
z1, z2 = sp.symbols("z1 z2")
LMAX = 2


class S:
    """truncated Laurent series in lam: {k: sympy expr}"""
    __slots__ = ("c",)

    def __init__(self, c=None):
        self.c = {k: v for k, v in (c or {}).items() if v != 0}

    def __add__(self, o):
        out = dict(self.c)
        for k, v in o.c.items():
            out[k] = sp.expand(out.get(k, 0) + v)
        return S(out)

    def __sub__(self, o):
        return self + o.scale(-1)

    def scale(self, a):
        return S({k: sp.expand(a * v) for k, v in self.c.items()})

    def __mul__(self, o):
        out = {}
        for i, a in self.c.items():
            for j, b in o.c.items():
                if i + j > LMAX:
                    continue
                out[i + j] = out.get(i + j, 0) + a * b
        return S({k: sp.expand(v) for k, v in out.items()})

    def fast(self, zz):
        """lam^-1 z d/dz"""
        return S({k - 1: sp.expand(zz * sp.diff(v, zz)) for k, v in self.c.items()})

    def get(self, k):
        return self.c.get(k, 0)


ZERO = S()


def ssum(it):
    out = S()
    for x in it:
        out = out + x
    return out


def d(f, c):
    if c == U:
        return f.fast(z2)
    if c == V:
        return f.fast(z1)
    return ZERO


def setup(division=True, verbose=False):
    g0 = sp.zeros(N)
    g0[U, V] = g0[V, U] = -E
    g0[2, 2], g0[3, 3], g0[4, 4] = r1, r2, r3
    g0i = g0.inv()
    amps = {}

    def tt(name):
        a1, a2 = sp.symbols(name + "1 " + name + "2")
        a3 = -r3 * (a1 / r1 + a2 / r2)
        return [a1, a2, a3]
    W = [[0] * N for _ in range(N)]
    Ain_p, Ain_m, Aout_p, Aout_m = tt("ap"), tt("am"), tt("bp"), tt("bm")
    ci_p, ci_m, co_p, co_m = sp.symbols("cip cim cop com")
    for i in range(3):
        W[2 + i][2 + i] = Ain_p[i] * z1 + Ain_m[i] / z1 + Aout_p[i] * z2 + Aout_m[i] / z2
    W[V][V] = ci_p * z1**2 + ci_m / z1**2
    W[U][U] = co_p * z2**2 + co_m / z2**2
    return g0, g0i, W


def ricci_h(g0, g0i, W, Q):
    """Ric^H of g = g0 + lam W + lam^2 Q, frozen (g0 constant, Gamma0 = 0), as S-series, up to lam^0"""
    g = [[S({0: g0[a, b], 1: W[a][b], 2: Q[a][b]}) for b in range(N)] for a in range(N)]
    G0 = [[S({0: g0i[a, b]}) for b in range(N)] for a in range(N)]
    Dl = [[S({1: W[a][b], 2: Q[a][b]}) for b in range(N)] for a in range(N)]

    def mm(A, B):
        return [[ssum(A[a][k] * B[k][b] for k in range(N)) for b in range(N)] for a in range(N)]
    gi, term = G0, G0
    for _ in range(LMAX):
        term = mm(mm(G0, [[x.scale(-1) for x in row] for row in Dl]), term)
        gi = [[gi[a][b] + term[a][b] for b in range(N)] for a in range(N)]
    dg = [[[d(g[a][b], c) for b in range(N)] for a in range(N)] for c in range(N)]   # dg[c][a][b]
    Gl = [[[(dg[b][dd][c] + dg[c][dd][b] - dg[dd][b][c]).scale(sp.Rational(1, 2)) for c in range(N)]
           for b in range(N)] for dd in range(N)]                                     # Gamma_{d b c}
    Gm = [[[ssum(gi[a][dd] * Gl[dd][b][c] for dd in range(N)) for c in range(N)] for b in range(N)]
          for a in range(N)]
    Ric = {}
    tr = [ssum(Gm[a][a][x] for a in range(N)) for x in range(N)]
    for b in range(N):
        for c in range(b, N):
            t1 = ssum(d(Gm[a][b][c], a) for a in range(N))
            t2 = d(tr[b], c)
            t3 = ssum(Gm[a][a][x] * Gm[x][b][c] for a in range(N) for x in range(N))
            t4 = ssum(Gm[a][c][x] * Gm[x][a][b] for a in range(N) for x in range(N))
            Ric[(b, c)] = t1 - t2 + t3 - t4
    Dv = [ssum(gi[a][b] * Gm[r][a][b] for a in range(N) for b in range(N)) for r in range(N)]
    RH = {}
    for b in range(N):
        for c in range(b, N):
            corr = ssum(g[b][r] * d(Dv[r], c) + g[c][r] * d(Dv[r], b) for r in range(N))
            RH[(b, c)] = Ric[(b, c)] - corr.scale(sp.Rational(1, 2))
    return RH, gi, Gm, g, Dv


def harmonics(expr):
    """dict (n1, n2) -> coefficient of a Laurent polynomial in z1, z2"""
    e = sp.expand(expr)
    out = {}
    for term in sp.Add.make_args(e):
        if term == 0:
            continue
        # handle negative powers
        pw = term.as_powers_dict()
        n1 = int(pw.get(z1, 0))
        n2 = int(pw.get(z2, 0))
        cf = sp.expand(term / (z1**n1 * z2**n2))
        out[(n1, n2)] = sp.expand(out.get((n1, n2), 0) + cf)
    return {k: v for k, v in out.items() if sp.simplify(v) != 0}


def mixed(expr):
    return {n: c for n, c in harmonics(expr).items() if n[0] != 0 and n[1] != 0}


def structural():
    t0 = time.time()
    g0, g0i, W = setup()
    Z = [[0] * N for _ in range(N)]
    RH, gi, Gm, g, Dv = ricci_h(g0, g0i, W, Z)
    print("  R^(-1) = 0 in every component: %s  [%.0f s]"
          % (all(sp.expand(RH[k].get(-1)) == 0 for k in RH), time.time() - t0), flush=True)
    print("  D^(0) (lam^0 of the gauge vector) = 0: %s" % all(sp.expand(x.get(0)) == 0 for x in Dv), flush=True)
    R0 = {k: RH[k].get(0) for k in RH}
    # the symbol of the lam^2 Q mixed harmonic at lam^0: compute it with a test Q
    qs = sp.symbols("q0:15")
    Qt = [[0] * N for _ in range(N)]
    it = iter(qs)
    for a in range(N):
        for b in range(a, N):
            Qt[a][b] = Qt[b][a] = next(it) * z1 * z2**-1         # a (1, -1) harmonic, n1 n2 = -1
    RHq, *_ = ricci_h(g0, g0i, [[0] * N for _ in range(N)], Qt)
    sym = {k: sp.simplify(RHq[k].get(0) / (Qt[k[0]][k[1]])) for k in RHq}
    print("  symbol of lam^2 Q z1 z2^-1 at lam^0, per component: %s" % set(sym.values()), flush=True)
    # predicted: -1/2 g^cd k_c k_d with d_u d_v -> n1 n2 (formal F = z d/dz): -g0^{uv} n1 n2 = (1/E) n1 n2
    # (S1) the trace identity with W only
    A = [2, 3, 4]
    rr = [r1, r2, r3]
    trR = sp.expand(sum(R0[(a, a)] / rr[i] for i, a in enumerate(A)))
    Wsq = sp.expand(sum((W[a][a] / rr[i])**2 for i, a in enumerate(A)))
    g0uv = g0i[U, V]
    F1F2 = lambda e: sp.expand(z1 * sp.diff(z2 * sp.diff(e, z2), z1))   # noqa: E731
    s1_lhs = mixed(trR)
    s1_rhs = mixed(-2 * g0uv * F1F2(-Wsq / 4))
    s1 = set(s1_lhs) == set(s1_rhs) and all(sp.simplify(s1_lhs[n] - s1_rhs[n]) == 0 for n in s1_lhs)
    print("  (S1) gamma0^AB R^(0)_AB |mixed = -2 g0^uv F1 F2 (a2) |mixed with Q = 0: %s; mixed harmonics present: %s"
          % (s1, sorted(s1_lhs)), flush=True)
    # (S2) division: Q_n = -R^(0)_n / (n1 n2 / E) componentwise
    Q = [[0] * N for _ in range(N)]
    for a in range(N):
        for b in range(a, N):
            for n, cf in mixed(R0[(a, b)]).items():
                q = -cf * E / (n[0] * n[1]) * z1**n[0] * z2**n[1]
                Q[a][b] += q
                if a != b:
                    Q[b][a] += q
    RH2, gi2, Gm2, g2, _ = ricci_h(g0, g0i, W, Q)
    nomix = all(not mixed(RH2[k].get(0)) for k in RH2)
    print("  (S2) with Q from the division, R^(0) has no mixed harmonic in any component: %s  [%.0f s]"
          % (nomix, time.time() - t0), flush=True)
    trQ = sp.expand(sum(Q[a][a] / rr[i] for i, a in enumerate(A)))
    a2 = sp.expand(trQ / 2 - Wsq / 4)
    a2mix = mixed(a2)
    print("  (S2) a2 = (1/2) tr Q - (1/4)|W|^2: mixed part %s (must be empty)" % a2mix, flush=True)

    # (S3) theta_du = -gamma^{AB} Gamma^u_{AB}, gamma the inverse of the angular block
    def theta_du(gser, Gmser):
        gA = [[gser[a][b] for b in A] for a in A]
        g0A = sp.Matrix(3, 3, lambda i, j: g0[A[i], A[j]])
        g0Ai = g0A.inv()
        G0A = [[S({0: g0Ai[i, j]}) for j in range(3)] for i in range(3)]
        DA = [[S({k: v for k, v in gA[i][j].c.items() if k >= 1}) for j in range(3)] for i in range(3)]

        def mm(X, Y):
            return [[ssum(X[i][k] * Y[k][j] for k in range(3)) for j in range(3)] for i in range(3)]
        gAi, term = G0A, G0A
        for _ in range(LMAX):
            term = mm(mm(G0A, [[x.scale(-1) for x in row] for row in DA]), term)
            gAi = [[gAi[i][j] + term[i][j] for j in range(3)] for i in range(3)]
        return ssum((gAi[i][j] * Gmser[U][A[i]][A[j]]).scale(-1) for i in range(3) for j in range(3))
    th = theta_du(g2, Gm2)
    th1 = th.get(1)
    mix1 = mixed(th1)
    s2dep = {n: c for n, c in harmonics(th1).items() if n[1] != 0}
    pred = sp.expand(g0uv * z1 * sp.diff(a2, z1))
    s3 = sp.simplify(sp.expand(th1 - pred)) == 0
    print("  (S3) theta_du: lam^-1 %s, lam^0 %s; lam^1 = g0^uv F1 a2 exactly: %s; lam^1 harmonics depending on s2: %s"
          % (sp.expand(th.get(-1)), sp.simplify(th.get(0)), s3, s2dep), flush=True)
    # control: no division
    Qz = [[0] * N for _ in range(N)]
    RH3, gi3, Gm3, g3, _ = ricci_h(g0, g0i, W, Qz)
    th_c = theta_du(g3, Gm3).get(1)
    ctl = mixed(th_c)
    print("  control (Q = 0): theta_du lam^1 mixed harmonics present: %s (%d harmonics)" % (bool(ctl), len(ctl)),
          flush=True)
    ok = s1 and nomix and not a2mix and s3 and not s2dep and bool(ctl)
    print("   H3-structural:", "PASS" if ok else "FAIL", "[%.0f s]" % (time.time() - t0))
    return ok




def _slow_ns():
    u, v, th = sp.symbols("u v theta")
    z1, z2, lam = sp.symbols("z1 z2 lam")
    X = [u, v, th]
    N = 5
    E = sp.Function("E")(u, v)
    R = sp.Function("R")(u, v)
    C, Sn = sp.cos(th), sp.sin(th)

    def fun(name):
        return sp.Function(name)(u, v, th)

    def slow(mutate=False):
        t0 = time.time()
        g0 = sp.zeros(N)
        g0[0, 1] = g0[1, 0] = -E
        om = [1, C**2, Sn**2]
        for i in range(3):
            g0[2 + i, 2 + i] = R**2 * om[i]
        g0i = g0.inv()
        a1, a2 = fun("a1"), fun("a2")
        b1, b2 = fun("b1"), fun("b2")
        ain = [a1, a2, -a1 - a2]
        bout = [b1, b2, -b1 - b2]
        W = sp.zeros(N)
        for i in range(3):
            W[2 + i, 2 + i] = R**2 * om[i] * (ain[i] * z1 + bout[i] * z2)
        W[1, 1] = fun("ci") * z1**2
        W[0, 0] = fun("co") * z2**2
        Q = sp.zeros(N)
        m, n = sp.symbols("m n", integer=True, nonzero=True)
        for a in range(N):
            for b in range(a, N):
                Q[a, b] = Q[b, a] = fun("q%d%d" % (a, b)) * z1**m * z2**n
        g = g0 + lam * W + lam**2 * Q
        # inverse to O(lam^2) and angular inverse to O(lam^2)
        gi = g0i - lam * g0i * W * g0i + lam**2 * (g0i * W * g0i * W * g0i - g0i * Q * g0i)
        A = [2, 3, 4]
        gA0 = sp.Matrix(3, 3, lambda i, j: g0[A[i], A[j]])
        gA0i = gA0.inv()
        WA = sp.Matrix(3, 3, lambda i, j: W[A[i], A[j]])
        QA = sp.Matrix(3, 3, lambda i, j: Q[A[i], A[j]])
        gAi = gA0i - lam * gA0i * WA * gA0i + lam**2 * (gA0i * WA * gA0i * WA * gA0i - gA0i * QA * gA0i)
        if mutate:                                       # control: the angular inverse without its lam corrections
            gAi = gA0i

        def D(e, c):
            out = sp.diff(e, X[c]) if c < 3 else 0
            if c == 0:
                out += z2 * sp.diff(e, z2) / lam
            if c == 1:
                out += z1 * sp.diff(e, z1) / lam
            return out
        tot = 0
        for i, a in enumerate(A):
            for j, b in enumerate(A):
                if gAi[i, j] == 0:
                    continue
                low = [D(g[d, a], b) + D(g[d, b], a) - D(g[a, b], d) for d in range(N)]
                Gk = sum(gi[0, d] * low[d] for d in range(N)) / 2
                tot += -gAi[i, j] * Gk
        tot = sp.expand(tot)
        th1 = sp.expand(tot.coeff(lam, 1))
        print("  theta_du expanded  [%.0f s]" % (time.time() - t0), flush=True)
        # prediction for the fast part: g0^{uv} F1 a2
        trQ = sum(gA0i[i, j] * QA[j, i] for i in range(3) for j in range(3))
        Wsq = sp.expand((gA0i * WA * gA0i * WA).trace())
        a2f = trQ / 2 - Wsq / 4
        pred = sp.expand(g0i[0, 1] * z1 * sp.diff(a2f, z1))
        diff = sp.expand(th1 - pred)
        # what remains must not depend on z2 (s2) at all
        dz2 = sp.simplify(sp.diff(diff, z2))
        print("  lam^1 of theta_du minus g0^uv F1 a2 is independent of s2: %s  [%.0f s]" % (dz2 == 0, time.time() - t0),
              flush=True)
        rest = sp.simplify(diff)
        print("  the remainder (s1-only, slow-derivative terms): %s" % rest, flush=True)
        ok = dz2 == 0 and not rest.has(z2)
        print("   H3-slow%s:" % (" (mutated)" if mutate else ""), "PASS" if ok else "FAIL",
              "[%.0f s]" % (time.time() - t0))
        return ok

    return slow


slow = _slow_ns()


def main():
    t0 = time.time()
    print("(T) non-frozen: lam^1 of theta_du = g0^uv F1 a2 + (s2-independent)", flush=True)
    ok_t = slow()
    ok_tm = slow(mutate=True)
    print("   control rejected: %s" % (not ok_tm), flush=True)
    print("(S) frozen coefficients: (S1)-(S3) and the control", flush=True)
    ok_s = structural()
    ok = ok_t and not ok_tm and ok_s
    print("PASS" if ok else "FAIL", "[%.0f s]" % (time.time() - t0))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
