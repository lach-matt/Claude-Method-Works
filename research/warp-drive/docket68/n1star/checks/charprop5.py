#!/usr/bin/env python3
"""charprop5: the gauge condition W := Upsilon(g) - H = 0 propagated from characteristic data (FAMILIES5 4e, D440).

propagate5's P3-P4 take data on a spacelike slice. Here N = {u = 0} is a null hypersurface, in coordinates
(u, v, x^A), A = 2 .. n-1, with generators d_v: g_vv = g_vA = 0 on N. Every quantity is evaluated at a point p of N,
exactly, in the polynomial ring Q[T]. The generators T are the transverse jets d_u g_ab(p) and d_u d_c g_ab(p), c any
coordinate. The jets of g along N at p and every jet of H are random rationals. A quantity is data on N when it is
T-free. E := Ric(g) - dstar_g W is the reduced operator, with propagate5's conventions: Upsilon_b = g_bc g^(ad)
Gamma^c_ad, (dstar W)_ab = (1/2)(nabla_a W_b + nabla_b W_a), Ric_ab = d_c Gamma^c_ab - d_b Gamma^c_ac + Gamma Gamma.

  N0  a control of the Ricci tensor, Raychaudhuri: Ric_vv = -d_v theta + kappa theta - chi^A_B chi^B_A, with
      chi_AB = (1/2) d_v g_AB, theta = gamma^(AB) chi_AB, gamma^(AB) the inverse of g_AB, kappa = Gamma^v_vv; and
      Gamma^u_vv = Gamma^A_vv = 0 on N.
  N1  W(p) depends on T only through d_u g_vv, d_u g_vA and gamma^(AB) d_u g_AB: affinely and triangularly, with
      diagonal g^(uv), g^(uv) and -1/2. So W = 0 at a point of N fixes those n derivatives there.
  N2  C_vv := Ric_vv + (theta/2) W_v is T-free, and E_vv = C_vv - d_v W_v + (kappa - theta/2) W_v exactly. So on a
      solution of the reduced equation, d_v W_v = (kappa - theta/2) W_v + C_vv along each generator.
  N3  Modulo W_v and its first derivatives along N: E_vA = C_vA - d_v W_A + (chi_A^B - (theta/2) delta_A^B) W_B,
      chi_A^B = chi_AC gamma^(CB), with C_vA T-free and no other term in W or its first derivatives (W_u, d W_u and
      the angular d_C W_B included). A transport of W_A, once W_v = 0 on N.
  N4  Modulo W_v, W_A and their first derivatives along N: gamma^(AB) E_AB = C_tr + 2 g^(uv) d_v W_u - g^(uv) H_v W_u,
      with C_tr T-free and no d_A W_u term. A transport of W_u, once W_v = W_A = 0 on N.

C_vv, C_vA and C_tr are the null constraints in the gauge W = 0: they involve only g on N, its derivatives along N,
and H. If the data satisfy them on N and W = 0 on the section S = N cap {v = 0}, then N2, N3 and N4 in turn give
W_v = 0, W_A = 0 and W_u = 0 on N (linear ODEs along the generators, zero data at S). On N' = {v = 0} the same holds
with u and v exchanged; the computation is symmetric under that relabelling and is not repeated. propagate5's P2 then
gives box_g W + Ric(g)(W) = 0 with W = 0 on N and N'.

Controls: N2 with g_vv != 0 on N (a hypersurface that is not null), and with theta in place of theta/2, is not
T-free; N3 without the reduction modulo W_v has no solution; N4 with the single component E_22 in place of the trace
has none (the trace-free angular equations carry the trace-free d_v d_u g_AB, not a constraint).

Not computed: that the gauge-reduced constraints can be solved on N and N' (ODEs along the generators) with W = 0 on S
(the corner conditions), the null dusts' stress in place of vacuum, and uniqueness of the characteristic problem for
the linear wave equation with zero data on N and N'.

Run: python3 charprop5.py   (n = 4 and n = 5, three seeds each; exact)
"""
import random
import sys
from fractions import Fraction as Fr

import sympy as sp
from sympy import QQ
from sympy.polys.rings import ring

U, V = 0, 1


def make(n, seed, null=True):
    """the jets at p of a metric with N = {u = 0} null (null=False: g_vv != 0 on N), and of H"""
    r = random.Random(seed)

    def rnd(den=10, span=5):
        return Fr(r.randint(-span, span), den)
    comps = [(a, b) for a in range(n) for b in range(a, n)]
    names = []
    for a, b in comps:
        names.append("g%d%d_u" % (a, b))
        names += ["g%d%d_u%d" % (a, b, c) for c in range(n)]
    R, *gens = ring(",".join(names), QQ)
    sym = dict(zip(names, gens))

    def c(x):
        return R(sp.Rational(x.numerator, x.denominator))

    def zero_on_n(a, b):
        a, b = min(a, b), max(a, b)
        return null and a == V and b >= V

    while True:
        g0 = [[Fr(0)] * n for _ in range(n)]
        g0[U][U] = rnd()
        g0[U][V] = g0[V][U] = Fr(-1) + rnd(20, 3)
        for A in range(2, n):
            g0[U][A] = g0[A][U] = rnd()
            for B in range(A, n):
                g0[A][B] = g0[B][A] = Fr(int(A == B)) + rnd(20, 3)
        if not null:
            g0[V][V] = Fr(1, 5)
        gam = sp.Matrix(n - 2, n - 2, lambda i, j: sp.Rational(g0[i + 2][j + 2].numerator, g0[i + 2][j + 2].denominator))
        full = sp.Matrix(n, n, lambda i, j: sp.Rational(g0[i][j].numerator, g0[i][j].denominator))
        if all(gam[:k, :k].det() > 0 for k in range(1, n - 1)) and full.det() != 0:
            break
    d1 = {}
    for a, b in comps:
        for e in range(n):
            if e == U:
                d1[a, b, e] = sym["g%d%d_u" % (a, b)]
            else:
                d1[a, b, e] = R(0) if zero_on_n(a, b) else c(rnd())
    d2 = {}
    for a, b in comps:
        for e in range(n):
            for f in range(e, n):
                if e == U:
                    d2[a, b, e, f] = sym["g%d%d_u%d" % (a, b, f)]
                else:
                    d2[a, b, e, f] = R(0) if zero_on_n(a, b) else c(rnd())
    gi0 = full.inv()
    jet = dict(
        n=n, R=R, sym=sym, g0=[[c(g0[i][j]) for j in range(n)] for i in range(n)],
        gi=[[R(gi0[i, j]) for j in range(n)] for i in range(n)],
        gamI=[[R(x) for x in row] for row in gam.inv().tolist()],
        dg=lambda a, b, e: d1[min(a, b), max(a, b), e],
        d2g=lambda a, b, e, f: d2[min(a, b), max(a, b), min(e, f), max(e, f)],
        H0=[c(rnd()) for _ in range(n)], H1=[[c(rnd()) for _ in range(n)] for _ in range(n)])
    return jet


def geometry(j):
    """Gamma, d Gamma, Ric, W, dW and E at p, all in Q[T]"""
    n, R, gi, g0, dg, d2g = j["n"], j["R"], j["gi"], j["g0"], j["dg"], j["d2g"]
    I = range(n)
    half = R(sp.Rational(1, 2))
    dgi = [[[-sum((gi[a][i] * dg(i, k, e) * gi[k][b] for i in I for k in I), R(0)) for b in I] for a in I]
           for e in I]
    cr = [[[dg(b, d, a) + dg(a, d, b) - dg(a, b, d) for d in I] for b in I] for a in I]
    G = [[[half * sum((gi[c_][d] * cr[a][b][d] for d in I), R(0)) for b in I] for a in I] for c_ in I]
    dG = [[[[half * sum((dgi[e][c_][d] * cr[a][b][d]
                         + gi[c_][d] * (d2g(b, d, a, e) + d2g(a, d, b, e) - d2g(a, b, d, e)) for d in I), R(0))
             for b in I] for a in I] for c_ in I] for e in I]
    Ric = [[sum((dG[c_][c_][a][b] - dG[b][c_][a][c_] for c_ in I), R(0))
            + sum((G[c_][c_][e] * G[e][a][b] - G[c_][b][e] * G[e][a][c_] for c_ in I for e in I), R(0))
            for b in I] for a in I]
    gG = [sum((gi[a][d] * G[c_][a][d] for a in I for d in I), R(0)) for c_ in I]
    dgG = [[sum((dgi[e][a][d] * G[c_][a][d] + gi[a][d] * dG[e][c_][a][d] for a in I for d in I), R(0)) for c_ in I]
           for e in I]
    Ups = [sum((g0[b][c_] * gG[c_] for c_ in I), R(0)) for b in I]
    dUps = [[sum((dg(b, c_, e) * gG[c_] + g0[b][c_] * dgG[e][c_] for c_ in I), R(0)) for b in I] for e in I]
    W = [Ups[b] - j["H0"][b] for b in I]
    dW = [[dUps[e][b] - j["H1"][e][b] for b in I] for e in I]
    nW = [[dW[a][b] - sum((G[c_][a][b] * W[c_] for c_ in I), R(0)) for b in I] for a in I]
    E = [[Ric[a][b] - half * (nW[a][b] + nW[b][a]) for b in I] for a in I]
    return dict(G=G, Ric=Ric, W=W, dW=dW, E=E)


def theta_chi(j):
    n, R, gamI, dg = j["n"], j["R"], j["gamI"], j["dg"]
    half = R(sp.Rational(1, 2))
    S = range(2, n)
    chi = [[half * dg(A, B, V) for B in S] for A in S]
    mix = [[sum((gamI[A][C] * chi[C][B] for C in range(n - 2)), R(0)) for B in range(n - 2)] for A in range(n - 2)]
    th = sum((mix[A][A] for A in range(n - 2)), R(0))
    chi2 = sum((mix[A][B] * mix[B][A] for A in range(n - 2) for B in range(n - 2)), R(0))
    dth = sum((gamI[A][B] * half * j["d2g"](A + 2, B + 2, V, V)
               - sum((gamI[A][C] * dg(C + 2, D + 2, V) * gamI[D][B] for C in range(n - 2) for D in range(n - 2)), R(0))
               * chi[A][B] for A in range(n - 2) for B in range(n - 2)), R(0))
    return th, chi2, dth, mix


def reduce_mod(polys, forms, pivots):
    """solve each linear form for its pivot generator, in turn, and substitute"""
    polys, forms = list(polys), list(forms)
    for k, x in enumerate(pivots):
        f = forms[k]
        coef = f.coeff(x)
        assert coef != 0, "pivot absent"
        sol = -(f - f.ring(coef) * x) * f.ring(1 / coef)
        assert sol.coeff(x) == 0
        polys = [p.compose(x, sol) for p in polys]
        forms = [q.compose(x, sol) for q in forms]
    return polys


def express(target, cands):
    """constants mu with target - sum mu_k cands_k T-free, or None"""
    mons = sorted({m for p in [target] + cands for m in p.keys() if any(m)})
    if not mons:
        return [0] * len(cands)
    zero = target.ring.domain.zero
    M = sp.Matrix(len(mons), len(cands), lambda i, k: sp.Rational(str(dict(cands[k]).get(mons[i], zero))))
    b = sp.Matrix(len(mons), 1, lambda i, _: sp.Rational(str(dict(target).get(mons[i], zero))))
    try:
        sol, params = M.gauss_jordan_solve(b)
    except ValueError:
        return None
    if params.shape[0]:
        sol = sol.subs({p_: 0 for p_ in params})
    mu = list(sol)
    res = target - sum((target.ring(m) * w for m, w in zip(mu, cands)), target.ring(0))
    return mu if res.is_ground else None


def run(n, seed):
    j = make(n, seed)
    R, sym = j["R"], j["sym"]
    geo = geometry(j)
    G, Ric, W, dW, E = geo["G"], geo["Ric"], geo["W"], geo["dW"], geo["E"]
    S = list(range(2, n))
    guv = j["gi"][U][V]
    out = {}
    th, chi2, dth, mix = theta_chi(j)
    kap = G[V][V][V]
    half = R(sp.Rational(1, 2))
    out["N0"] = (Ric[V][V] == -dth + kap * th - chi2) and all(G[c_][V][V] == 0 for c_ in [U] + S)
    # N1: W(p) on the transverse first jets
    first = {nm: x for nm, x in sym.items() if nm.endswith("_u")}
    ok1 = all(w.coeff(x) == 0 for w in W for nm, x in sym.items() if not nm.endswith("_u"))
    allowed = {"g%d%d_u" % (V, V)} | {"g%d%d_u" % (V, A) for A in S} \
        | {"g%d%d_u" % (A, B) for A in S for B in S if A <= B}
    ok1 &= all(w.coeff(first[nm]) == 0 for w in W for nm in first if nm not in allowed)
    trw = [R(sp.Rational(1 if A == B else 2)) * j["gamI"][A - 2][B - 2] for A in S for B in S if A <= B]
    trn = ["g%d%d_u" % (A, B) for A in S for B in S if A <= B]
    for b in range(n):
        cs = [W[b].coeff(first[nm]) for nm in trn]
        k = next((i for i, w in enumerate(trw) if w != 0), None)
        lam = R(cs[k]) * R(1 / trw[k].LC)
        ok1 &= all(R(cs[i]) == lam * trw[i] for i in range(len(trn)))
        if b == U:
            ok1 &= lam == -half
        else:
            ok1 &= lam == 0
    ok1 &= R(W[V].coeff(first["g%d%d_u" % (V, V)])) == guv
    ok1 &= all(W[V].coeff(first["g%d%d_u" % (V, A)]) == 0 for A in S)
    ok1 &= all(R(W[A].coeff(first["g%d%d_u" % (V, B)])) == (guv if A == B else R(0)) for A in S for B in S)
    out["N1"] = ok1
    # N2
    Cvv = Ric[V][V] + th * half * W[V]
    out["N2"] = Cvv.is_ground and E[V][V] == Cvv - dW[V][V] + (kap - th * half) * W[V]
    # N3: modulo W_v, d_v W_v, d_A W_v
    piv1 = [sym["g%d%d_u" % (V, V)], sym["g%d%d_u%d" % (V, V, V)]] + [sym["g%d%d_u%d" % (V, V, A)] for A in S]
    forms1 = [W[V], dW[V][V]] + [dW[A][V] for A in S]
    labels = ["W%d" % B for B in S] + ["dvW%d" % B for B in S] + ["d%dW%d" % (C, B) for C in S for B in S] \
        + ["Wu", "dvWu"] + ["d%dWu" % C for C in S]
    cands = [W[B] for B in S] + [dW[V][B] for B in S] + [dW[C][B] for C in S for B in S] + [W[U], dW[V][U]] \
        + [dW[C][U] for C in S]
    ok3 = True
    mus3 = []
    for A in S:
        red = reduce_mod([E[V][A]] + cands, forms1, piv1)
        mu = express(red[0], red[1:])
        if mu is None:
            ok3 = False
            continue
        mus3.append(mu)
        for lab, m in zip(labels, mu):
            if lab == "dvW%d" % A:
                ok3 &= m == -1
            elif lab.startswith("W") and lab != "Wu":
                B = int(lab[1:])
                want = mix[B - 2][A - 2] - (th * half if A == B else R(0))
                ok3 &= R(sp.Rational(m)) == want
            else:
                ok3 &= m == 0
    out["N3"] = ok3
    # N4: modulo W_v, W_A and their first derivatives along N
    piv2 = piv1 + [sym["g%d%d_u" % (min(V, A), max(V, A))] for A in S] \
        + [sym["g%d%d_u%d" % (V, A, V)] for A in S] + [sym["g%d%d_u%d" % (V, A, C)] for A in S for C in S]
    forms2 = forms1 + [W[A] for A in S] + [dW[V][A] for A in S] + [dW[C][A] for A in S for C in S]
    trE = sum((j["gamI"][A - 2][B - 2] * E[A][B] for A in S for B in S), R(0))
    c4 = [W[U], dW[V][U]] + [dW[C][U] for C in S]
    red = reduce_mod([trE, E[2][2]] + c4, forms2, piv2)
    mu4 = express(red[0], red[2:])
    out["N4"] = (mu4 is not None and mu4[1] == sp.Rational(str(2 * guv.LC)) and all(m == 0 for m in mu4[2:])
                 and R(sp.Rational(mu4[0])) == -guv * j["H0"][V])
    ctl = {}
    ctl["E22 for the trace (N4)"] = express(red[1], red[2:]) is None
    ctl["theta for theta/2 (N2)"] = not (Ric[V][V] + th * W[V]).is_ground
    red0 = [E[V][S[0]]] + cands
    ctl["no reduction mod W_v (N3)"] = express(red0[0], red0[1:]) is None
    jn = make(n, seed, null=False)
    gn = geometry(jn)
    thn = theta_chi(jn)[0]
    ctl["g_vv != 0 on N (N2)"] = not (gn["Ric"][V][V] + thn * half * gn["W"][V]).is_ground
    return out, ctl, mus3, mu4


def main():
    ok = {}
    for n in (4, 5):
        for seed in (1, 2, 3):
            out, ctl, mus3, mu4 = run(n, seed)
            print("  n = %d, seed %d: %s; controls fail as required: %s" % (
                n, seed, ", ".join("%s %s" % (k, "ok" if v else "FAIL") for k, v in out.items()),
                ", ".join("%s %s" % (k, "yes" if v else "NO") for k, v in ctl.items())), flush=True)
            if seed == 1:
                print("      N3 coefficients of W_B in E_vA (rows A; = chi_A^B - theta/2 delta): %s"
                      % [[str(m) for m in mu[:n - 2]] for mu in mus3])
                print("      N4 coefficients of W_u, d_v W_u, d_A W_u in the trace: %s" % [str(m) for m in mu4])
            for k, v in out.items():
                ok[k] = ok.get(k, True) and v
            ok["controls"] = ok.get("controls", True) and all(ctl.values())
    for k, v in ok.items():
        print(k, "PASS" if v else "FAIL")
    return 0 if all(ok.values()) else 1


if __name__ == "__main__":
    sys.exit(main())
