#!/usr/bin/env python3
"""symmshift5.py -- the symmetrizer of Lemma 6.3 (a) when gamma_rA != 0 (D619; the section 6 reader's n1, its
symm_shift.py made a program).

The approximant's slice metric has gamma_(r th) = O(lam^2) (from gh_(m+1) through Pol^+), so the momentum constraint's
principal part in (w, q) must be symmetrizable with gamma_rA != 0 too.  At a point the principal symbol is algebraic in
gamma: J_i = 2(-gamma^(jk) d_k K_ij + d_i tr K) with K -> K + w Pi + q dr + dr q, unknowns (w, q_A), A = th, p1, p2,
coordinates (r, th, p1, p2).  "Pi the metric induced on the spheres, q a covector tangent to them" is read two ways:
  C  coordinate: Pi = the angular block of gamma (zero elsewhere), q_r = 0;
  R  normal-adapted ([Rac16]): Pi = gamma - n n, n = dr/|dr|, q(n^#) = 0.
For each reading the symmetrizers -- the 4 x 4 matrices S with S A^k symmetric for k = r, th, p1, p2 (A^r = A0, the
coefficient of d_r) -- are solved for exactly (a linear system in the sixteen entries of S).

  Y1 (exact) At the reader's two metrics (gamma_rA = 0 and != 0) and at ten random rational positive-definite metrics
     with gamma_rA != 0, in both readings: the symmetrizers form a one-dimensional space.  In reading R its generator
     normalised to S_ww = 1 has S A0 positive definite (every leading principal minor > 0) at all twelve; in reading C
     at the reader's two, but not at five of the random ones (large gamma_rA): there the coordinate reading is not
     symmetric hyperbolic in r, so it serves only near gamma_rA = 0 (Y2), which is the case here.  At gamma_rA = 0 the
     generator is diag(1, -(1/2) Pi_ang^-1) (Pi_ang the angular block), the S of Lemma 6.3 (a).  Control: J with its
     trace term d tr K scaled by 1/3 (the mutation that cancels the w part of the divergence) admits no symmetrizer
     with S A0 > 0 at any metric in either reading.
  Y2 (exact, symbolic delta) g0's slice metric at a point inside the horizon (mu = 1/2, r = 1/3, th = pi/4) with
     gamma_(r th) = delta, gamma_(r p1) = delta/3: the symmetrizer space is one-dimensional for generic delta (the
     linear system solved with delta symbolic), its normalised generator S(delta) is rational in delta, regular at 0,
     and the leading minors of S A0 are positive at delta = 0, hence for |delta| small (the approximant's gamma_rA =
     O(lam^2)), in both readings.  Control: the 1/3 mutant has no symmetrizer with S A0 > 0 at delta = 0.

Labels: Y1, Y2 computed (exact, sympy; principal symbols at points).  Run: python3 checks/symmshift5.py   (seconds)
"""
import random
import sys
import textwrap

import sympy as sp


def out(msg):
    print(textwrap.fill(msg, width=121, subsequent_indent="      ", break_on_hyphens=False), flush=True)


def symbol(g, reading, trace_coef=1):
    """the coefficient matrices of d_k, k = r, th, p1, p2, of J in (w, q_th, q_p1, q_p2)"""
    gi = g.inv()
    w, q1, q2, q3 = sp.symbols('w q1 q2 q3')
    dr = sp.Matrix([1, 0, 0, 0])
    if reading == 'C':
        Pi = sp.zeros(4)
        Pi[1:, 1:] = g[1:, 1:]
        q = sp.Matrix([0, q1, q2, q3])
    else:
        nn = dr/sp.sqrt(gi[0, 0])
        Pi = g - nn*nn.T
        qr = -(gi[0, 1]*q1 + gi[0, 2]*q2 + gi[0, 3]*q3)/gi[0, 0]
        q = sp.Matrix([qr, q1, q2, q3])
    dK = w*Pi + q*dr.T + dr*q.T
    unk = [w, q1, q2, q3]
    trdK = sum(gi[j, l]*dK[j, l] for j in range(4) for l in range(4))
    mats = []
    for k in range(4):
        rows = []
        for i in range(4):
            e = 2*(-sum(gi[j, k]*dK[i, j] for j in range(4)) + trace_coef*(1 if i == k else 0)*trdK)
            rows.append([sp.diff(e, u) for u in unk])
        mats.append(sp.Matrix(rows))
    return mats


def symmetrizers(mats):
    s = sp.symbols('s0:16')
    Ss = sp.Matrix(4, 4, s)
    eqs = []
    for M in mats:
        P = Ss*M
        eqs += [P[i, j] - P[j, i] for i in range(4) for j in range(i + 1, 4)]
    A, _ = sp.linear_eq_to_matrix(eqs, list(s))
    return [sp.Matrix(4, 4, list(v)) for v in A.nullspace(simplify=True)]


def minors(M):
    return [sp.simplify(M[:k, :k].det()) for k in range(1, 5)]


def positive_symmetrizer(mats, at=None):
    """(dimension, normalised generator or None, minors of S A0, decision: True / False / None undecided); with at, a
    substitution, the signs of the minors are decided there"""
    ns = symmetrizers(mats)
    A0 = mats[0]
    if len(ns) == 1:
        S = ns[0]
        if S[0, 0] == 0:
            return 1, None, None, False
        S = sp.simplify(S/S[0, 0])
        mins = minors(sp.simplify(S*A0))
        vals = [sp.simplify(x.subs(at)) if at else x for x in mins]
        for sgn in (1, -1):
            if all(sp.simplify(sgn**(k + 1)*x) > 0 for k, x in enumerate(vals)):
                return 1, S, mins, True
        return 1, S, mins, False
    if len(ns) == 0:
        return 0, None, None, False
    if all((B*A0)[0, :] == sp.zeros(1, 4) for B in ns):      # the w row of S A0 vanishes on the whole space
        return len(ns), None, None, False
    return len(ns), None, None, None                         # undecided


def rnd_spd(rng, eps):
    g = sp.diag(sp.Rational(7, 5), sp.Rational(9, 4), sp.Rational(5, 3), sp.Rational(11, 6))
    for A in (1, 2, 3):
        g[0, A] = g[A, 0] = eps*sp.Rational(rng.randint(1, 9), 10)
    g[1, 2] = g[2, 1] = sp.Rational(1, 7)
    return g


def random_spd(rng):
    B = sp.Matrix(4, 4, lambda i, j: sp.Rational(rng.randint(-9, 9), rng.randint(1, 6)))
    g = B*B.T + sp.eye(4)/2
    return g


def metrics():
    rng = random.Random(5)
    ms = [("reader gamma_rA = 0", rnd_spd(rng, 0)), ("reader gamma_rA != 0", rnd_spd(rng, 1))]
    rng2 = random.Random(619)
    while len(ms) < 12:
        g = random_spd(rng2)
        if all(g[0, A] != 0 for A in (1, 2, 3)):
            ms.append(("random %d" % (len(ms) - 1), g))
    return ms


def y1(control=False):
    tc = sp.Rational(1, 3) if control else 1
    res, diag0 = {}, True
    for name, g in metrics():
        for rd in "CR":
            dim, S, mins, dec = positive_symmetrizer(symbol(g, rd, tc))
            if control:
                if dec is not False:
                    return True                    # the mutant admits (or may admit) a positive symmetrizer
                continue
            res[(name, rd)] = (dim, dec)
            if name == "reader gamma_rA = 0":
                cand = sp.zeros(4)
                cand[0, 0] = 1
                cand[1:, 1:] = -g[1:, 1:].inv()/2
                diag0 &= S is not None and sp.simplify(S - cand) == sp.zeros(4)
    if control:
        return False
    names = [nm for nm, _ in metrics()]
    R_all = all(res[(nm, "R")] == (1, True) for nm in names)
    C_dim = all(res[(nm, "C")][0] == 1 for nm in names)
    C_reader = all(res[(nm, "C")] == (1, True) for nm in names[:2])
    C_fail = [nm for nm in names if res[(nm, "C")][1] is not True]
    out("  Y1 12 metrics (the reader's two, gamma_rA = 0 and != 0, and ten random rational positive-definite ones with"
        " gamma_rA != 0): reading R (normal-adapted, as in [Rac16]): a one-dimensional symmetrizer space with S A0 > 0 at all"
        " 12: %s; reading C (coordinate): one-dimensional at all 12: %s, S A0 > 0 at the reader's two: %s, but no"
        " symmetrizer with S A0 > 0 at %d of the ten random ones (%s: the coordinate reading is symmetric hyperbolic"
        " near gamma_rA = 0 only, Y2); at gamma_rA = 0, S = diag(1, -(1/2) Pi_ang^-1) in both readings: %s" % (
            R_all, C_dim, C_reader, len(C_fail), ", ".join(C_fail), diag0))
    return R_all and C_dim and C_reader and diag0


def y2(control=False):
    d = sp.Symbol('delta')
    muv, rv = sp.Rational(1, 2), sp.Rational(1, 3)
    g = sp.diag(1 + muv/rv**2, rv**2, rv**2/2, rv**2/2)       # th = pi/4: cos^2 = sin^2 = 1/2
    g[0, 1] = g[1, 0] = d
    g[0, 2] = g[2, 0] = d/3
    rows, ok = [], True
    for rd in "CR":
        mats = symbol(g, rd, sp.Rational(1, 3) if control else 1)
        if control:
            dim, S, mins, dec = positive_symmetrizer([M.subs(d, 0) for M in mats])
            if dec is not False:
                return True
            continue
        dim, S, mins, dec = positive_symmetrizer(mats, at={d: 0})
        regular = S is not None and all(sp.denom(sp.together(x)).subs(d, 0) != 0 for x in S)
        m0 = [sp.simplify(x.subs(d, 0)) for x in mins] if mins else []
        pos0 = dec is True and bool(m0) and all(x > 0 for x in m0)
        good = dim == 1 and regular and pos0
        ok &= good
        rows.append("reading %s: dim %d, S(delta) regular at 0: %s, minors of S A0 at delta = 0: %s, S(delta)_(w, q_th)"
                    " = %s" % (rd, dim, regular, m0, sp.factor(S[0, 1]) if S is not None else None))
    if control:
        return False
    out("  Y2 g0's slice metric at (mu, r, th) = (1/2, 1/3, pi/4), gamma_(r th) = delta, gamma_(r p1) = delta/3: "
        + "; ".join(rows))
    return ok


def main():
    ok = True
    for name, f in (("Y1", y1), ("Y2", y2)):
        good = f()
        ctl = f(control=True)
        out("%s %s%s" % (name, "PASS" if good and not ctl else "FAIL", " (control passed)" if ctl else ""))
        ok &= good and not ctl
    out("symmshift5: %s" % ("all checks pass, every control fails" if ok else "FAILURES"))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
