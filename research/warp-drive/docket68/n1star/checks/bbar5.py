#!/usr/bin/env python3
"""bbar5.py -- the coefficients B-bar and C-bar of the stage equation for the means (BEYOND5 3(b), D569).

N1STAR-PROOF.md Lemma 5.3 (a) (516) is the stage equation for the mean m_m:
-(1/2) box~ m_m + Bbar . d m_m + Cbar m_m = (sources), its left side being the theta-mean of the part of Rm^(m) (5.3)
linear in m_m (Lemma 5.1, 489-496: "its th-mean part is -(1/2) box~ m_m + first order"). D555 (4) and D564 (3) record
that Bbar and Cbar's expansions at past null infinity were asserted (as theta-means and products of g0 and W terms) and
not shown. Here they are computed. By Lemma 5.1's weights, the terms of Rm^(m) linear in m_m pair m_m (weight m) with
factors of weight 0, which do not depend on m: Bbar and Cbar are the same at every stage. So they are read off at
stage 1 with phi_1 = 0: the lam^1 eps^1 coefficient of Ric^H(g0 + lam W + lam eps h), in lead5.py's gauge, coordinates
(v, r, th, phi1, phi2) and wave (W_TT, and chi dv dv with chi = r^-2 (k_a cos 2s + k_b sin 2s), the second harmonic,
k_a and k_b arbitrary functions of (v, th): a second-harmonic choice: past5.py P5 allows any s-dependence and
lead5.py's L4 an s-independent zero mode, with which the results are the same, verifier 249, D577). h is a symmetric tensor of 15 arbitrary functions of
all five coordinates.

  K0 (exact) the eps-linear part at lam^0 is (1/2) h_rr d_s^2 W, every component: the record's -(1/2) e_1 d_th^2 W with
     e_1 = -m_1(ell, ell) (5.2, phi_1 = 0), and nothing else.
  K1 (exact) the s-mean of the eps-linear part at lam^1, minus the same with the wave off (the linearisation of Ric^H
     at g0, -(1/2) box~ h + B0 . dh + C0 h): no derivative of h appears. So Bbar = B0, built from g0 alone.
  K2 (exact) that difference is quadratic in the wave (homogeneous of degree 2 in (A, k_a, k_b)), the means of the
     terms linear in the wave vanishing; and it has no W_TT-chi cross term (first times second harmonic).
  K3 (exact) its order at past null infinity: the coefficient of each h_de in component bc, times r^(n_de - n_bc) (n
     the number of angular indices; this turns coordinate components into those of an orthonormal frame, whose order
     is the Cartesian one), is of order r^-3 in the W_TT^2 part, attained (in E_3, not E_(7/2)), and the chi^2 part is
     absent (every quadratic chi term pairs dv with dv through g0^-1, which is null; chi is in the computation, K0's vv
     entry carrying it).
  K4 (exact) the wave-off part has principal part -(1/2) g0^{ab} d_a d_b h_cd, component by component (no second
     derivative of another component): the box~ of Lemma 5.3 (a).
  Ctl W_TT with amplitude r^(-1/2) in place of r^(-3/2): K3's order falls to 1, so K3 sees the amplitude.

Deduced from these: Cbar = C0 + Delta C, with Delta C the quadratic wave means of K2-K3 (exact terms r^-p F(v, xhat),
p >= 3, all from W_TT, chi contributing none). B0 and C0 are polynomial in the
Cartesian components of g0 and g0^-1 and their first and second derivatives, and g0 - eta = mu(v) r^-2 dv dv is exact, so they are exact sums of r^-p F(v, xhat) with p >= 2 (each
Cartesian derivative of r^-p F(v, xhat) gives x_hat r^-p F_v plus r^(-p-1) terms). So Bbar and Cbar are exact sums of r^-p F with
p >= 2, each in E_p^ell, as D559's induction uses them (D577: E_2 alone would not give E_2^ell). Labels: computed (exact, sympy) for K0-K4 and Ctl;
deduced for the Cartesian statement about B0 and C0.

    python3 checks/bbar5.py [--cache DIR]      (about ten minutes; DIR keeps the two Ricci expansions)
"""
import os
import pickle
import sys
import time

import sympy as sp

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import lead5 as L  # noqa: E402

v, r, th, s, lam, A = L.v, L.r, L.th, L.s, L.lam, L.A
X = L.X
eps, z, t = sp.symbols("eps z t")
q = sp.Symbol("q", positive=True)
NAMES = ["v", "r", "t", "p", "q"]
ANG = (2, 3, 4)
ka = sp.Function("k_a")(v, th)
kb = sp.Function("k_b")(v, th)
HM = sp.zeros(5)
HF = {}
for a_ in range(5):
    for b_ in range(a_, 5):
        f_ = sp.Function("h_" + NAMES[a_] + NAMES[b_])(*X)
        HF[(a_, b_)] = f_
        HM[a_, b_] = HM[b_, a_] = f_
HSET = set(HF.values())
CACHE = sys.argv[2] if sys.argv[1:2] == ["--cache"] else None     # a directory for the Ricci coefficients


def wave(p=sp.Rational(-3, 2), with_chi=True):
    C, S_ = sp.cos(th), sp.sin(th)
    y = r**p
    a1 = A * L.Ef * L.Hf * y * (2 * C**2 * sp.cos(s) - S_**2 * sp.sin(s)) / 3
    a2 = A * L.Ef * L.Hf * y * (2 * S_**2 * sp.sin(s) - C**2 * sp.cos(s)) / 3
    W = sp.zeros(5)
    W[2, 2], W[3, 3], W[4, 4] = -2 * r**2 * (a1 + a2), 2 * r**2 * C**2 * a1, 2 * r**2 * S_**2 * a2
    if with_chi:
        W[0, 0] = r**-2 * (ka * sp.cos(2 * s) + kb * sp.sin(2 * s))
    return W


def tr(e, top):
    """lam^k (k <= top) and eps^0, eps^1"""
    e = sp.expand(e)
    out = 0
    for k in range(-3, top + 1):
        ck = e.coeff(lam, k)
        if ck != 0:
            out += (ck.coeff(eps, 0) + eps * ck.coeff(eps, 1)) * lam**k
    return out


def ricci(W):
    """Ric^H(g0 + lam (W + eps h)) to lam^1 and eps^1, in lead5's wave-map gauge relative to g0"""
    n = 5
    g0, g0i = L.background()
    dl = W + eps * HM
    g = g0 + lam * dl
    P = g0i * dl * g0i
    gi = (g0i - lam * P + lam**2 * P * dl * g0i).applyfunc(lambda e: tr(e, 2))
    G = L.christoffel(g, gi, L.D)
    G = [[[tr(x, 2) for x in row] for row in M2] for M2 in G]
    Gh = L.christoffel(g0, g0i, lambda e, k: sp.diff(e, X[k]))
    Dv = [tr(sum(gi[a, b] * (G[rho][a][b] - Gh[rho][a][b]) for a in range(n) for b in range(n)), 2)
          for rho in range(n)]
    out = {}
    for b in range(n):
        for c in range(b, n):
            e = 0
            for a in range(n):
                e += L.D(G[a][b][c], a) - L.D(G[a][b][a], c)
                for d in range(n):
                    e += G[a][a][d] * G[d][b][c] - G[a][c][d] * G[d][b][a]
            hb = sum(g[b, rho] * (L.D(Dv[rho], c) + sum(Gh[rho][c][sg] * Dv[sg] for sg in range(n))) for rho in range(n))
            hc = sum(g[c, rho] * (L.D(Dv[rho], b) + sum(Gh[rho][b][sg] * Dv[sg] for sg in range(n))) for rho in range(n))
            e = tr(e - (hb + hc) / 2, 1)
            out[(b, c)] = {k: e.coeff(lam, k).coeff(eps, 1) for k in (-1, 0, 1)}
    return out


TRIG = {sp.cos(s): (z + 1 / z) / 2, sp.sin(s): (z - 1 / z) / (2 * sp.I),
        sp.cos(2 * s): (z**2 + z**-2) / 2, sp.sin(2 * s): (z**2 - z**-2) / (2 * sp.I)}


def mean(e):
    e = sp.expand(sp.expand(e).xreplace(TRIG))
    return sp.expand(sum(c for c, ex in (term.as_coeff_exponent(z) for term in sp.Add.make_args(e)) if ex == 0))


def nang(b, c):
    return (b in ANG) + (c in ANG)


def qorder(e):
    """least k with q^k in e(r = q^-2), so e = O(r^(-k/2)); None if e = 0"""
    e = sp.expand(sp.powsimp(sp.expand(e.subs(r, q**-2)), force=True))
    if e == 0:
        return None
    return min(term.as_coeff_exponent(q)[1] for term in sp.Add.make_args(e))


def freeze(R, W):
    """every derivative and function atom of the Ricci coefficients as a plain symbol (sympy's collect cannot take
    multivariate derivatives): (frozen R, frozen W, the map, h's derivative symbols, the wave's symbols)"""
    atoms = set()
    for k in R:
        for kk in R[k]:
            atoms |= R[k][kk].atoms(sp.Derivative)
    sym = {d: sp.Symbol("D%d" % i_) for i_, d in enumerate(sorted(atoms, key=str))}
    for f in list(HF.values()) + [L.Ef, L.Hf, ka, kb, L.Mf]:
        sym[f] = sp.Symbol("F_" + str(f.func))
    FR = {k: {kk: sp.expand(R[k][kk].xreplace(sym)) for kk in R[k]} for k in R}
    FW = W.applyfunc(lambda e: e.xreplace(sym))
    hder = {sym[d]: d for d in atoms if d.expr in HSET}
    chis = {sym[ka], sym[kb]} | {sym[d] for d in atoms if d.expr in (ka, kb)}
    return FR, FW, sym, hder, chis


def analyse(W, label, cache=None):
    t0 = time.time()
    if cache and os.path.exists(cache):
        with open(cache, "rb") as fh:
            R = pickle.load(fh)
    else:
        R = ricci(W)
        if cache:
            with open(cache, "wb") as fh:
                pickle.dump(R, fh)
    print("  %s: Ric^H to lam^1 eps^1 (%.0f s)" % (label, time.time() - t0), flush=True)
    R, FW, sym, hder, chis = freeze(R, W)
    Aw = sp.Symbol("Aw")
    res = {}
    hrr = sym[HM[1, 1]]
    res["K0"] = all(R[k][-1] == 0 and sp.expand(R[k][0] - hrr * sp.diff(FW[k], s, 2) / 2) == 0 for k in R)
    off = {A: 0, **{c: 0 for c in chis}}
    k1, k2, k4, cross = True, True, True, True
    orders = {"W_TT^2": [], "chi^2": []}
    g0, g0i = L.background()
    g0i = g0i.applyfunc(lambda e: e.xreplace(sym))
    for k in R:
        m1 = mean(R[k][1])
        m0 = sp.expand(m1.xreplace(off))
        dW = sp.expand(m1 - m0)
        k1 = k1 and not (dW.free_symbols & set(hder))
        scaled = sp.expand(dW.xreplace({A: t * A, **{c: t * c for c in chis}}))
        k2 = k2 and sp.expand(scaled - t**2 * dW) == 0
        tt = sp.expand(dW.xreplace({c: 0 for c in chis}))
        cc = sp.expand(dW.xreplace({A: 0}))
        cross = cross and sp.expand(dW - tt - cc) == 0
        for (d, e_), h in HF.items():
            w = r**(nang(d, e_) - nang(*k))
            for part, name in ((tt, "W_TT^2"), (cc, "chi^2")):
                co = sp.diff(part, sym[h])
                if co != 0:
                    orders[name].append(qorder(co * w))
                    if name == "W_TT^2":
                        res.setdefault("pairs", []).append((NAMES[k[0]] + NAMES[k[1]], NAMES[d] + NAMES[e_], qorder(co * w)))
        # K4: the second derivatives of h in the wave-off part are -(1/2) g0^{ab} d_a d_b h_k, and no other
        for ds, d in hder.items():
            if d.derivative_count != 2:
                continue
            co = m0.coeff(ds)
            vars_ = [X.index(x) for x, nn in d.variable_count for _ in range(nn)]
            want = 0
            if d.expr == HF[k]:
                a, b = vars_
                want = -g0i[a, b] / 2 if a == b else -g0i[a, b]
            k4 = k4 and sp.simplify(co - want) == 0
        for a in range(5):
            for b in range(a, 5):
                if g0i[a, b] != 0:
                    ds = sym.get(sp.diff(HF[k], X[a], X[b]))
                    want = -g0i[a, b] / 2 if a == b else -g0i[a, b]
                    k4 = k4 and ds is not None and sp.simplify(m0.coeff(ds) - want) == 0
    res["K1"], res["K2"], res["K4"] = k1, k2 and cross, k4
    lo = {kk: (min(vv) if vv else None) for kk, vv in orders.items()}
    print("    least order (in powers of r^(-1/2)) of the frame coefficients: W_TT^2 part %s, chi^2 part %s; counts %d, %d"
          % (lo["W_TT^2"], lo["chi^2"], len(orders["W_TT^2"]), len(orders["chi^2"])), flush=True)
    res["orders"] = lo
    res["exact3"] = bool(orders["W_TT^2"]) and min(orders["W_TT^2"]) == 6
    print("  %s done (%.0f s)" % (label, time.time() - t0), flush=True)
    return res


def main():
    ok = {}
    r1 = analyse(wave(), "W_TT + chi dv dv", CACHE and os.path.join(CACHE, "bbar5_R1.pkl"))
    ok["K0"], ok["K1"], ok["K2"], ok["K4"] = r1["K0"], r1["K1"], r1["K2"], r1["K4"]
    ok["K3"] = r1["exact3"] and (r1["orders"]["chi^2"] is None or r1["orders"]["chi^2"] >= 8)
    print("    the W_TT^2 entries (component, h, least power of q): %s" % r1["pairs"])
    print("  K0 eps-linear lam^0 part = (1/2) h_rr d_s^2 W: %s" % r1["K0"])
    print("  K1 no derivative of h in the wave part of the lam^1 mean: %s" % r1["K1"])
    print("  K2 quadratic in the wave, no W_TT-chi cross term: %s" % r1["K2"])
    print("  K3 frame orders: W_TT^2 at least, and at most, r^-3 (q^6); chi^2 absent or at least r^-4 (q^8): %s" % ok["K3"])
    print("  K4 wave-off principal part -(1/2) g0^{ab} d_a d_b h_cd: %s" % r1["K4"])
    r2 = analyse(wave(sp.Rational(-1, 2), with_chi=False), "control: W_TT with amplitude r^(-1/2)",
                 CACHE and os.path.join(CACHE, "bbar5_R2.pkl"))
    ok["Ctl"] = r2["orders"]["W_TT^2"] == 2
    print("  Ctl amplitude r^(-1/2): the W_TT^2 part's least order is q^%s (r^-1)" % r2["orders"]["W_TT^2"])
    for k, val in ok.items():
        print(k, "PASS" if val else "FAIL")
    return 0 if all(ok.values()) else 1


if __name__ == "__main__":
    sys.exit(main())
