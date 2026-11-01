#!/usr/bin/env python3
"""charcorner5: the corner conditions of the characteristic problem, W = 0 on S = N cap N' (FAMILIES5 4e, D455).

charprop5 (D440) and charcons5 (D448-D449) take data on N = {u = 0} (generators d_v) and on N' = {v = 0} (generators
d_u), and need W := Upsilon(g) - H = 0 on S. Each cone's constraint hierarchy then needs initial values at S: on N the
conformal factor, theta (the expansion of d_v, from gamma^(AB) d_v g_AB), d_v g_uA and d_v g_uu (g_uA = g_uu = 0 at S);
on N' the same factor, theta', d_u g_vA and d_u g_vv. D449 called the first derivatives "what the corner conditions
fix" without computing them. Here W is evaluated at a point of S, where g_vv = g_vA = 0 (N null) and g_uu = g_uA = 0 (N'
null), exactly in the ring Q[d_u g, d_v g] of the first jets in u and v that do not vanish there (d_v of g_vv, g_vA
vanishes along N, d_u of g_uu, g_uA along N'). The angular jets d_C g_ab (zero for the four vanishing components) and H
are random rationals. W involves no second derivative.

  C1 (the mirror of N1, computed) W depends on the v-jets only through d_v g_uu, d_v g_uA and tau := gamma^(AB) d_v g_AB
     (= 2 theta), with W_u's coefficient on d_v g_uu, W_A's on d_v g_uB and W_v's on tau g^(uv), g^(uv) delta_AB and
     -1/2, and on d_v g_uv not at all; N1 holds at S as well (the u-jets through d_u g_vv, d_u g_vA and tau' :=
     gamma^(AB) d_u g_AB). So W is affine in the 2n numbers X = (d_u g_vv, d_u g_vA, tau'; d_v g_uu, d_v g_uA, tau).
  C2 (computed) at S the Jacobian is exactly diagonal in pairs, with no other entry:
         W_u = g^(uv) d_v g_uu - tau'/2 + f_u,   W_v = g^(uv) d_u g_vv - tau/2 + f_v,
         W_A = g^(uv) (d_u g_vA + d_v g_uA) + f_A.
     So the corner system W = 0 is solvable for N's numbers given N-prime's, for N-prime's given N's, and for (d_u g_vv,
     d_v g_uu, d_u g_vA) given (tau, tau', d_v g_uA): each of these n x n blocks is invertible. Control: tau and
     d_u g_vv cannot both be prescribed (the block for the unknowns (d_v g_uu, tau', d_u g_vA) is singular, its W_v row
     zero).
  C3 (computed) f involves no u- or v-jet at all, d_u g_uv and d_v g_uv included: only g at S, its angular derivatives
     d_C g_ab and H.
  Control: at a point of N off S (g_uu, g_uA != 0) C1's statement for the v-jets fails.

So per point of S, given g there (its conformal factor free), its angular derivatives and H, the corner conditions are
n relations, each between one number of N and one of N': the expansion of N with N-prime's d_u g_vv, the expansion of N'
with N's d_v g_uu, and d_v g_uA with d_u g_vA. Both expansions and one of each mixed pair are free, the other n numbers
fixed. This corrects D449's reading: theta is not fixed by the corner conditions, it is paired with d_u g_vv.

Not computed: that the two hierarchies' solutions, so started, give the reduced equation's solution near S (the
characteristic problem's local existence, standard), and the null dusts' stress in place of vacuum.

Run: python3 checks/charcorner5.py   (n = 4 and 5, two seeds each; exact)
"""
import random
import sys
from fractions import Fraction as Fr

import sympy as sp
from sympy import QQ
from sympy.polys.rings import ring

U, V = 0, 1


def make(n, seed, corner=True):
    """the metric and first jets at p; corner: p on S (g_uu = g_uA = 0 too), else on N only"""
    r = random.Random(seed)

    def rnd(den=10, span=5):
        return Fr(r.randint(-span, span), den)
    comps = [(a, b) for a in range(n) for b in range(a, n)]
    vanish_N = lambda a, b: a == V                              # g_vv, g_vA (a <= b, so a = V means b >= V)
    vanish_Np = lambda a, b: corner and a == U and b != V        # g_uu, g_uA
    names = []
    for a, b in comps:
        for e in (U, V):
            if e == V and vanish_N(a, b):
                continue
            if e == U and vanish_Np(a, b):
                continue
            names.append("d%sg%d%d" % ("uv"[e], a, b))
    R, *gens = ring(",".join(names), QQ)
    sym = dict(zip(names, gens))

    def c(x):
        return R(sp.Rational(x.numerator, x.denominator))
    while True:
        g0 = [[Fr(0)] * n for _ in range(n)]
        if not corner:
            g0[U][U] = rnd()
        g0[U][V] = g0[V][U] = Fr(-1) + rnd(20, 3)
        for A in range(2, n):
            if not corner:
                g0[U][A] = g0[A][U] = rnd()
            for B in range(A, n):
                g0[A][B] = g0[B][A] = Fr(int(A == B)) + rnd(20, 3)
        gam = sp.Matrix(n - 2, n - 2, lambda i, j: sp.Rational(g0[i + 2][j + 2].numerator, g0[i + 2][j + 2].denominator))
        full = sp.Matrix(n, n, lambda i, j: sp.Rational(g0[i][j].numerator, g0[i][j].denominator))
        if all(gam[:k, :k].det() > 0 for k in range(1, n - 1)) and full.det() != 0:
            break
    d1 = {}
    for a, b in comps:
        for e in range(n):
            nm = "d%sg%d%d" % ("uv"[e], a, b) if e in (U, V) else None
            if nm in sym:
                d1[a, b, e] = sym[nm]
            elif e in (U, V):
                d1[a, b, e] = R(0)
            else:                                                  # angular: tangent to S, so to both cones
                d1[a, b, e] = R(0) if (vanish_N(a, b) or vanish_Np(a, b)) else c(rnd())
    gi0 = full.inv()
    return dict(n=n, R=R, sym=sym, g0=[[c(g0[i][j]) for j in range(n)] for i in range(n)],
                gi=[[R(gi0[i, j]) for j in range(n)] for i in range(n)],
                gamI=[[R(x) for x in row] for row in gam.inv().tolist()],
                dg=lambda a, b, e: d1[min(a, b), max(a, b), e], H0=[c(rnd()) for _ in range(n)])


def gauge_W(j):
    """W_b = g_bc g^(ad) Gamma^c_ad - H_b at p (charprop5's conventions)"""
    n, R, gi, g0, dg = j["n"], j["R"], j["gi"], j["g0"], j["dg"]
    I = range(n)
    half = R(sp.Rational(1, 2))
    cr = [[[dg(b, d, a) + dg(a, d, b) - dg(a, b, d) for d in I] for b in I] for a in I]
    G = [[[half * sum((gi[c_][d] * cr[a][b][d] for d in I), R(0)) for b in I] for a in I] for c_ in I]
    gG = [sum((gi[a][d] * G[c_][a][d] for a in I for d in I), R(0)) for c_ in I]
    return [sum((g0[b][c_] * gG[c_] for c_ in I), R(0)) - j["H0"][b] for b in I]


def trace_coeff(w, j, e):
    """lambda with w's coefficients on d_e g_AB equal to lambda times gamma^(AB) (weight 2 off the diagonal), or None"""
    n, R, sym = j["n"], j["R"], j["sym"]
    S = range(2, n)
    pairs = [(A, B) for A in S for B in S if A <= B]
    wts = [R(sp.Rational(1 if A == B else 2)) * j["gamI"][A - 2][B - 2] for A, B in pairs]
    cs = [R(w.coeff(sym["d%sg%d%d" % ("uv"[e], A, B)])) for A, B in pairs]
    k = next(i for i, x in enumerate(wts) if x != 0)
    lam = cs[k] * R(1 / wts[k].LC)
    return lam if all(cs[i] == lam * wts[i] for i in range(len(pairs))) else None


def run(n, seed):
    j = make(n, seed)
    R, sym, gi = j["R"], j["sym"], j["gi"]
    W = gauge_W(j)
    S = list(range(2, n))
    guv = gi[U][V]
    half = R(sp.Rational(1, 2))
    co = lambda w, nm: R(w.coeff(sym[nm]))
    out = {}
    # C1: the v-jets (and N1's u-jets) enter only through X
    lam_v = [trace_coeff(w, j, V) for w in W]
    lam_u = [trace_coeff(w, j, U) for w in W]
    ok = all(lam is not None for lam in lam_v + lam_u)
    ok &= lam_v[V] == -half and all(lam_v[b] == 0 for b in range(n) if b != V)
    ok &= lam_u[U] == -half and all(lam_u[b] == 0 for b in range(n) if b != U)
    ok &= co(W[U], "dvg00") == guv and all(co(W[U], "dvg0%d" % A) == 0 for A in S)
    ok &= all(co(W[A], "dvg0%d" % B) == (guv if A == B else R(0)) for A in S for B in S)
    ok &= co(W[V], "dug11") == guv and all(co(W[V], "dug1%d" % A) == 0 for A in S)
    ok &= all(co(W[A], "dug1%d" % B) == (guv if A == B else R(0)) for A in S for B in S)
    out["C1"] = ok
    # the Jacobian in X, columns (d_u g_vv, d_u g_vA, tau'; d_v g_uu, d_v g_uA, tau), tau := gamma^(AB) d_v g_AB
    cols = ["dug11"] + ["dug1%d" % A for A in S] + ["tr_u"] + ["dvg00"] + ["dvg0%d" % A for A in S] + ["tr_v"]
    def jac(w):
        row = []
        for nm in cols:
            if nm == "tr_u":
                row.append(trace_coeff(w, j, U))
            elif nm == "tr_v":
                row.append(trace_coeff(w, j, V))
            else:
                row.append(co(w, nm))
        return [sp.Rational(str(x.LC)) if x != 0 else sp.Integer(0) for x in row]
    Jm = sp.Matrix([jac(W[b]) for b in [U, V] + S])          # rows W_u, W_v, W_A
    m = n - 2
    iNp = list(range(0, 2 + m))                                   # N-prime's numbers: d_u g_vv, d_u g_vA, tau'
    iN = list(range(2 + m, 4 + 2 * m))                            # N's numbers: d_v g_uu, d_v g_uA, tau
    blk = lambda idx: Jm[:, idx].det()
    ok2 = blk(iN) != 0 and blk(iNp) != 0
    guvq = sp.Rational(str(guv.LC))
    want = sp.zeros(n, 2 * n)
    want[0, 2 + m] = guvq; want[0, 1 + m] = sp.Rational(-1, 2)
    want[1, 0] = guvq; want[1, 3 + 2 * m] = sp.Rational(-1, 2)
    for i in range(m):
        want[2 + i, 1 + i] = guvq; want[2 + i, 3 + m + i] = guvq
    ok2 &= Jm == want
    mixed = [0, 2 + m] + list(range(1, 1 + m))                    # unknowns d_u g_vv, d_v g_uu, d_u g_vA
    ok2 &= blk(mixed) != 0
    bad = [2 + m, 1 + m] + list(range(1, 1 + m))                  # unknowns d_v g_uu, tau', d_u g_vA
    ok2 &= blk(bad) == 0 and all(Jm[1, k] == 0 for k in bad)
    out["C2"] = ok2
    # C3: beyond X, only d_u g_uv and d_v g_uv among the u- and v-jets
    Xn = {"dug11", "dvg00"} | {"dug1%d" % A for A in S} | {"dvg0%d" % A for A in S} \
        | {"d%sg%d%d" % (e, A, B) for e in "uv" for A in S for B in S if A <= B}
    rest_ok = True
    used = set()
    for w in W:
        for nm, x in sym.items():
            if nm in Xn:
                continue
            if w.coeff(x) != 0:
                used.add(nm)
    rest_ok = not used
    out["C3"] = rest_ok
    # control: off S, the v-jet half of C1
    jc = make(n, seed, corner=False)
    Wc = gauge_W(jc)
    lam_c = [trace_coeff(w, jc, V) for w in Wc]
    co_c = lambda w, nm: R(w.coeff(jc["sym"][nm])) if nm in jc["sym"] else R(0)
    mirror = all(lam is not None for lam in lam_c) and lam_c[V] == -half \
        and all(lam_c[b] == 0 for b in range(n) if b != V) \
        and R(Wc[U].coeff(jc["sym"]["dvg00"])) == jc["gi"][U][V] \
        and all(co_c(w, "dvg01") == 0 for w in Wc)
    ctl = not mirror
    return out, ctl, Jm, used


def main():
    ok = {}
    for n in (4, 5):
        for seed in (1, 2):
            out, ctl, Jm, used = run(n, seed)
            print("  n = %d, seed %d: %s; control (off S the mirror fails): %s; the rest uses %s" % (
                n, seed, ", ".join("%s %s" % (k, "ok" if v else "FAIL") for k, v in out.items()),
                "yes" if ctl else "NO", sorted(used)), flush=True)
            if seed == 1:
                print("      Jacobian of (W_u, W_v, W_A) in (d_u g_vv, d_u g_vA, tau'; d_v g_uu, d_v g_uA, tau):")
                for i in range(Jm.rows):
                    print("        " + "  ".join("%7s" % str(x) for x in Jm.row(i)))
            for k, v in out.items():
                ok[k] = ok.get(k, True) and v
            ok["control"] = ok.get("control", True) and ctl
    for k, v in ok.items():
        print(k, "PASS" if v else "FAIL")
    return 0 if all(ok.values()) else 1


if __name__ == "__main__":
    sys.exit(main())
