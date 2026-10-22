#!/usr/bin/env python3
"""modes5.py -- mode stability of the 1-form wave operator box = 2 delta G delta* on five-dimensional Tangherlini at
nonzero frequency: the reductions behind it, computed (N1STAR-PROOF.md section 10.16; ROUTES-OPEN.md 4.17; D58).
Labels: computed (exact, sympy), deduced, READ.

[Hin26] (arXiv:2606.28253v2) Proposition 6.9 makes box^Ups = 2 (delta + E^Ups) G delta* mode stable at |sigma| >= c_0,
Im sigma >= 0, for small E^Ups, by perturbation from the unmodified operator box, whose mode stability at sigma != 0 on
Kerr he takes from [AHW24] Theorem 5.1, and the high-energy estimates of his Proposition 6.5.  On a Ricci-flat metric
box is the Hodge d'Alembertian d delta + delta d (Weitzenboeck), which commutes with d and delta; so for a mode omega at
sigma != 0, delta omega is a scalar wave mode, d omega a Maxwell field, and omega = (i/sigma) (d iota_T omega + iota_T
d omega), T = d_t (Cartan).  Here the five-dimensional reductions, on Tangherlini f = 1 - mu/r^2, r_h = mu^(1/2), in
the static chart with d_t -> -i sigma (the spectral family), kappa = l (l + 2) the eigenvalue of -Delta on S^3.

  M1 (computed, exact) box = 2 delta G delta* equals d delta + delta d on every 1-form, five arbitrary functions of all
     five coordinates.  Four-dimensional control: Schwarzschild, the same.  Control: f = 1 - mu/r in five dimensions,
     not Ricci flat, where they differ (by -2 Ric(omega)).
  M2 (computed, exact) The scalar wave: for u = r^(-3/2) Phi(r) S, S any function on S^3 with Delta S = -kappa S (the
     rule d_th^2 S -> ..., not a representative), -f r^(3/2) (delta d u)/S = f (f Phi')' + sigma^2 Phi - V_0 Phi, V_0 =
     (f/r^2)(kappa + 3/4 + 9 mu/(4 r^2)).  Four-dimensional control: u = Phi S/r, V_0 = f (kappa/r^2 + mu/r^3).
     Control: the four-dimensional exponent r^-1 in five dimensions.
  M3 (computed, exact) The Maxwell vector type: for A = r^(-1/2) Phi(r) Y, Y any 1-form on S^3 (three arbitrary
     functions of the angles), delta A = r^-2 (r^(-1/2) Phi) delta_S Y, (delta d A)_t = i sigma r^-2 (r^(-1/2) Phi)
     delta_S Y, (delta d A)_r = -r^-2 (r^(-1/2) Phi)' delta_S Y, and -f r^(1/2) ((delta d A)_i - r^-2 (r^(-1/2) Phi)
     (delta_S d_S Y)_i) = (f (f Phi')' + sigma^2 Phi - U_1 Phi) Y_i, U_1 = (f/r^2)(-1/4 + 5 mu/(4 r^2)); so for Y
     co-closed with delta_S d_S Y = lam Y the potential is V_1 = (f/r^2)(lam - 1/4 + 5 mu/(4 r^2)).  The record's
     vector harmonic (gaugepot5.py) is co-closed with lam = (l + 1)^2 = kappa + 1, symbolic l.  Four-dimensional
     control: U_1 = 0.  Control: the four-dimensional exponent r^0 in five dimensions.
  M4 (computed, exact) The Maxwell scalar type, A = a(r) S dt + b(r) S dr (the gauge c = 0: A - d(c S e^(-i sigma
     t)) has the same dA), M = delta d A, R[W] := (f W'/r)' - kappa W/r^3 + sigma^2 W/(r f): (a) R[r^3 F_tr] = (r^2
     M_t)' + i sigma r^2 M_r; (b) where F_tr = 0, M_t = kappa a/r^2 and M_r = kappa b/r^2; (c) f r^(1/2) R[r^(1/2) Phi]
     = f (f Phi')' + sigma^2 Phi - V_2 Phi, V_2 = (f/r^2)(kappa + 3/4 - 7 mu/(4 r^2)); (d) l = 0 (S = 1): M_r = -i
     sigma F_tr/f; (e) for every solution of R[W] = 0, A(W) = (-f W' S dt + i sigma W S dr/f)/(kappa r) is a Maxwell
     field with r^3 F_tr = W.  Four-dimensional control: W = r^2 F_tr, R[W] = (f W')' - kappa W/r^2 + sigma^2 W/f, V_2
     = f kappa/r^2.  Control: the four-dimensional weight r^2 F_tr in five dimensions.
  M5 (computed, exact) (a) For r > r_h, x = mu/r^2 in (0, 1): V_0 r^2/f = kappa + 3/4 + 9x/4 > 0 for l >= 0, V_1
     r^2/f = lam - 1/4 + 5x/4 > 0 for lam >= 2, V_2 r^2/f = kappa + 3/4 - 7x/4 > 0 for kappa >= 3 (l >= 1); (b) r* = r
     + (r_h/2) log((r - r_h)/(r + r_h)) has dr*/dr = 1/f and r* = r - mu/r + O(r^-3), so e^(i sigma r*) = e^(i sigma r)
     (1 + O(1/r)); f'(r_h)/2 = 1/r_h; (c) d iota_T omega + iota_T d omega = -i sigma omega on every spectral 1-form.
     Control: V_2 at l = 0, negative near the horizon (so l = 0 is M4 (d)'s).

Deduced, not computed here (the class: e^(-i sigma t) omega_0 smooth across the future event horizon in (v, r, angles),
v = t + r*, and outgoing at infinity, omega_0 = e^(i sigma r) times a function with an expansion in 1/r): for sigma !=
0, Im sigma >= 0, every mode of box vanishes.  delta omega is a scalar mode (M1: delta box = delta d delta); each
spherical harmonic component's Phi solves -Phi_** + V_0 Phi = sigma^2 Phi with V_0 > 0 (M2, M5), Phi = e^(-i sigma r*)
times a smooth function at r_h and e^(i sigma r*) (c + O(1/r)) at infinity, so Phi = 0: for Im sigma > 0 by the
energy identity, for real sigma by the constant Wronskian Im(conj(Phi) Phi_*), -sigma |Phi e^(i sigma r*)(r_h)|^2 =
sigma |c|^2.  Then delta d omega = box omega - d delta omega = 0: omega is a Maxwell potential; its vector part
vanishes by M3 and M5 (lam >= 2, Bochner on S^3), its scalar part has r^3 F_tr = 0 by M4 (a), (c), M5 for l >= 1 and
M4 (d) for l = 0, hence F = 0 by M4 (b).  So d omega = 0, omega = (i/sigma) d (omega(T)) (M5 (c)), and omega(T) is a
scalar mode (delta d omega(T) = -i sigma delta omega = 0), so 0.  This is what [Hin26] Proposition 6.9 takes from
[AHW24] Theorem 5.1, for Tangherlini.  Not deduced: that kernel elements of his spectral family in five dimensions lie
in the class ([Hin26c] in five dimensions); his Proposition 6.5 in five dimensions.

READ.  [KI03b] (H. Kodama, A. Ishibashi, arXiv:hep-th/0308128v4) (4.23), (5.17), (5.19), (5.20), with n = 3, K = 1, Q
= 0: the master equations of M3 and M4.  [Hin26] pp. 118-119 (Lemma 6.8, Proposition 6.9; alphaXiv, 2026-10-21).

sympy.  python3 modes5.py [--selftest | --mutants]   (--verbose lists every sub-check)
"""
import sys
import time

import sympy as sp

import gaugepot5 as G
from damping5 import Checklist

D = sp.diff
mu, L = G.mu, G.L
sg = sp.Symbol("sigma")
kap = sp.Symbol("kappa", positive=True)
cth = sp.Symbol("cth", positive=True)


def static(n, f=None):
    """the static chart of gaugepot5.py, or the same chart with g_tt = -f, g_rr = 1/f (a control)"""
    if f is None:
        return G.ch(n, "static")
    C = dict(G.ch(n, "static"))
    X, N = C["X"], C["N"]
    g = C["g"].copy()
    g[0, 0], g[1, 1] = -f, 1/f
    gi = g.inv().applyfunc(sp.simplify)
    Gam = [[[sp.simplify(sum(gi[a, d]*(D(g[d, b], X[c]) + D(g[d, c], X[b]) - D(g[b, c], X[d])) for d in range(N))/2)
             for c in range(N)] for b in range(N)] for a in range(N)]
    C.update(f=f, g=g, gi=gi, Gam=Gam)
    return C


def dd(C, e, k, spectral):
    return -sp.I*sg*e if (spectral and k == 0) else D(e, C["X"][k])


def hodge(C, w, spectral=True):
    """delta w, F = d w, delta d w; diagonal metric (delta F)_b = -g_bb |g|^-1/2 d_a (|g|^1/2 g^aa g^bb F_ab)"""
    g, gi, vol, N = C["g"], C["gi"], C["vol"], C["N"]
    dl = -sum(dd(C, vol*gi[a, a]*w[a], a, spectral) for a in range(N))/vol
    F = [[dd(C, w[b], a, spectral) - dd(C, w[a], b, spectral) for b in range(N)] for a in range(N)]
    M = [-g[b, b]*sum(dd(C, vol*gi[a, a]*gi[b, b]*F[a][b], a, spectral) for a in range(N))/vol for b in range(N)]
    return dl, F, M


def canon(e, th):
    x = sp.expand_trig(sp.expand(e))
    x = x.subs(sp.tan(th), sp.sin(th)/sp.cos(th)).subs(sp.cot(th), sp.cos(th)/sp.sin(th))
    x = x.subs(sp.sin(th), sp.sqrt(1 - cth**2)).subs(sp.cos(th), cth)
    return sp.cancel(sp.together(sp.expand(x)))


def sphere(C):
    """the unit sphere's metric diagonal and volume factor, from the chart"""
    r, ang, g, vol = C["r"], C["ang"], C["g"], C["vol"]
    return [g[2 + i, 2 + i]/r**2 for i in range(len(ang))], vol/r**len(ang)


def eigen(C, S, k):
    """the rule d_th^2 S -> ... that imposes Delta_{S^m} S = -k S on an arbitrary function S of the angles"""
    ang = C["ang"]
    h, vs = sphere(C)
    lap = sp.expand(sum(D(vs/h[i]*D(S, x), x) for i, x in enumerate(ang))/vs)
    d2 = D(S, ang[0], 2)
    c2 = lap.coeff(d2)
    return {d2: sp.expand((-k*S - (lap - c2*d2))/c2)}


def per(e, S, rule):
    return sp.cancel(sp.expand(sp.expand(e).subs(rule))/S)


def schro(C, P, V):
    f, r = C["f"], C["r"]
    return f*D(f*D(P, r), r) + sg**2*P - V*P


# ------------------------------------------------------------------------------------------------- M1
def m1(control=0, verbose=False):
    chk = Checklist(verbose, quiet=control != 0)
    cases = [(4, 1 - mu/sp.Symbol("r", positive=True))] if control == 1 else [(4, None), (3, None)]
    for n, fr in cases:
        C = static(n, fr)
        X, N, th = C["X"], C["N"], C["ang"][0]
        w = [sp.Function("w%d" % a)(*X) for a in range(N)]
        B = G.box(C, w)
        dl, _, M = hodge(C, w, spectral=False)
        left = []
        for a in range(N):
            e = sp.expand(B[a] - D(dl, X[a]) - M[a])
            atoms = list(e.atoms(sp.Derivative)) + w
            left += [v for v in sp.Poly(e, *atoms).as_dict().values() if canon(v, th) != 0]
        chk(f"n + 1 = {n + 1}: 2 delta G delta* w = d delta w + delta d w, w_a arbitrary functions of all coordinates",
            not left)
    return chk.ok


# ------------------------------------------------------------------------------------------------- M2
def m2(control=0, verbose=False):
    chk = Checklist(verbose, quiet=control != 0)
    for n in ((4,) if control else (4, 3)):
        C = static(n)
        r, f, N = C["r"], C["f"], C["N"]
        S = sp.Function("S")(*C["ang"])
        P = sp.Function("Phi")(r)
        p = sp.Rational(n - 1, 2) if control != 1 else 1
        V0 = (f/r**2)*(kap + sp.Rational(3, 4) + sp.Rational(9, 4)*mu/r**2) if n == 4 else f*(kap/r**2 + mu/r**3)
        u = r**-p*P*S
        du = [dd(C, u, a, True) for a in range(N)]
        dlu, _, _ = hodge(C, du)
        x = per(-f*r**p*dlu, S, eigen(C, S, kap))
        chk(f"n + 1 = {n + 1}: -f r^p (delta d u)/S = f (f Phi')' + sigma^2 Phi - V_0 Phi, u = r^-p Phi S, Delta S = "
            f"-kappa S", sp.simplify(x - schro(C, P, V0)) == 0)
    return chk.ok


# ------------------------------------------------------------------------------------------------- M3
def m3(control=0, verbose=False):
    chk = Checklist(verbose, quiet=control != 0)
    for n in ((4,) if control else (4, 3)):
        C = static(n)
        r, f, ang, th = C["r"], C["f"], C["ang"], C["ang"][0]
        m = n - 1
        h, vs = sphere(C)
        Y = [sp.Function("Y%d" % i)(*ang) for i in range(m)]
        P = sp.Function("Phi")(r)
        p = sp.Rational(m - 2, 2) if control != 1 else 0
        U1 = (f/r**2)*(-sp.Rational(1, 4) + sp.Rational(5, 4)*mu/r**2) if n == 4 else 0
        V = r**-p*P
        A = [0, 0] + [V*y for y in Y]
        dl, _, M = hodge(C, A)
        dS = -sum(D(vs/h[i]*Y[i], x) for i, x in enumerate(ang))/vs
        FS = [[D(Y[j], ang[i]) - D(Y[i], ang[j]) for j in range(m)] for i in range(m)]
        dSdS = [-h[j]*sum(D(vs/(h[i]*h[j])*FS[i][j], x) for i, x in enumerate(ang))/vs for j in range(m)]
        ok_dt = all(canon(e, th) == 0 for e in (dl - V*dS/r**2, M[0] - sp.I*sg*V*dS/r**2, M[1] + D(V, r)*dS/r**2))
        chk(f"n + 1 = {n + 1}: delta A = r^-2 V delta_S Y, (delta d A)_t = i sigma r^-2 V delta_S Y, (delta d A)_r = "
            f"-r^-2 V' delta_S Y, V = r^-p Phi", ok_dt)
        ok_i = all(canon(-f*r**p*(M[2 + i] - V*dSdS[i]/r**2) - schro(C, P, U1)*Y[i], th) == 0 for i in range(m))
        chk(f"n + 1 = {n + 1}: -f r^p ((delta d A)_i - r^-2 V (delta_S d_S Y)_i) = (f (f Phi')' + sigma^2 Phi - U_1 "
            f"Phi) Y_i", ok_i)
        if control or n != 4:
            continue
        Yr = G.vector_harmonic(n, ang, L)
        dSr = -sum(D(vs/h[i]*Yr[i], x) for i, x in enumerate(ang))/vs
        FSr = [[D(Yr[j], ang[i]) - D(Yr[i], ang[j]) for j in range(m)] for i in range(m)]
        lam_r = [-h[j]*sum(D(vs/(h[i]*h[j])*FSr[i][j], x) for i, x in enumerate(ang))/vs for j in range(m)]
        chk("the record's vector harmonic is co-closed with delta_S d_S Y = (l + 1)^2 Y, symbolic l",
            canon(dSr, th) == 0 and all(canon(lam_r[i] - (L + 1)**2*Yr[i], th) == 0 for i in range(m)))
    return chk.ok


# ------------------------------------------------------------------------------------------------- M4
def m4(control=0, verbose=False):
    chk = Checklist(verbose, quiet=control != 0)
    for n in ((4,) if control else (4, 3)):
        C = static(n)
        r, f, ang, N = C["r"], C["f"], C["ang"], C["N"]
        m = n - 1
        q = m if control != 1 else 2
        S = sp.Function("S")(*ang)
        rule = eigen(C, S, kap)
        a, b = sp.Function("a")(r), sp.Function("b")(r)

        def R(W):
            return D(f*r**(2 - m)*D(W, r), r) - kap*r**(-m)*W + sg**2*r**(2 - m)*W/f

        _, F, M = hodge(C, [a*S, b*S] + [0]*m)
        Mt, Mr, Ftr = per(M[0], S, rule), per(M[1], S, rule), per(F[0][1], S, rule)
        chk(f"n + 1 = {n + 1}: (a) R[r^m F_tr] = (r^2 M_t)' + i sigma r^2 M_r, A = a S dt + b S dr",
            sp.expand(sp.numer(sp.together(R(r**q*Ftr) - D(r**2*Mt, r) - sp.I*sg*r**2*Mr))) == 0)
        if control:
            continue
        z = {b: sp.I*D(a, r)/sg}
        chk(f"n + 1 = {n + 1}: (b) F_tr = -i sigma b - a' and, where it vanishes (b = i a'/sigma), M_t = kappa a/r^2, "
            f"M_r = kappa b/r^2",
            sp.simplify(Ftr + sp.I*sg*b + D(a, r)) == 0 and sp.simplify(Mt.subs(z).doit() - kap*a/r**2) == 0
            and sp.simplify((Mr - kap*b/r**2).subs(z).doit()) == 0)
        P = sp.Function("Phi")(r)
        V2 = (f/r**2)*(kap + sp.Rational(3, 4) - sp.Rational(7, 4)*mu/r**2) if n == 4 else f*kap/r**2
        e = sp.Rational(m - 2, 2)
        chk(f"n + 1 = {n + 1}: (c) f r^e R[r^e Phi] = f (f Phi')' + sigma^2 Phi - V_2 Phi, e = (m - 2)/2",
            sp.simplify(f*r**e*R(r**e*P) - schro(C, P, V2)) == 0)
        _, F0, M0 = hodge(C, [a, b] + [0]*m)
        chk(f"n + 1 = {n + 1}: (d) l = 0: M_r = -i sigma F_tr/f, and F_tr dt dr is all of F",
            sp.simplify(M0[1] + sp.I*sg*F0[0][1]/f) == 0
            and all(F0[i][j] == 0 for i in range(N) for j in range(N) if (i, j) not in ((0, 1), (1, 0))))
        W = sp.Function("W")(r)
        AW = [-f*r**(2 - m)*D(W, r)/kap*S, sp.I*sg*r**(2 - m)*W/(kap*f)*S] + [0]*m
        _, FW, MW = hodge(C, AW)
        w2 = sp.solve(R(W), D(W, r, 2))[0]
        on = {D(W, r, 3): D(w2, r).subs(D(W, r, 2), w2), D(W, r, 2): w2}
        res = [per(MW[k], S, rule) for k in (0, 1)] + [per(FW[0][1], S, rule) - W/r**m]
        res += [sp.cancel(MW[k]/D(S, C["X"][k])) for k in range(2, N)]
        chk(f"n + 1 = {n + 1}: (e) where R[W] = 0, A(W) has delta d A(W) = 0 and r^m F_tr = W",
            all(sp.simplify(x.subs(on)) == 0 for x in res))
    return chk.ok


# ------------------------------------------------------------------------------------------------- M5
def m5(control=0, verbose=False):
    chk = Checklist(verbose, quiet=control != 0)
    x = sp.Symbol("x", positive=True)
    lo = 0 if control == 1 else 3
    v2 = kap + sp.Rational(3, 4) - sp.Rational(7, 4)*x
    chk("(a) V_2 r^2/f = kappa + 3/4 - 7x/4 > 0 on 0 < x < 1 for kappa >= 3 (linear in x: x = 1 gives kappa - 1)",
        all(v2.subs({kap: lo, x: xe}) > 0 for xe in (0, 1)))
    if control:
        return chk.ok
    chk("(a) V_0 r^2/f = kappa + 3/4 + 9x/4 > 0 for kappa >= 0 and V_1 r^2/f = lam - 1/4 + 5x/4 > 0 for lam >= 2",
        all(e > 0 for xe in (0, 1) for e in (sp.Rational(3, 4) + sp.Rational(9, 4)*xe,
                                              2 - sp.Rational(1, 4) + sp.Rational(5, 4)*xe)))
    C = static(4)
    r, f, X, N = C["r"], C["f"], C["X"], C["N"]
    rh = G.SQ
    rs = r + rh/2*sp.log((r - rh)/(r + rh))
    chk("(b) dr*/dr = 1/f, r* = r - mu/r + O(r^-3), f'(r_h)/2 = 1/r_h",
        sp.simplify(D(rs, r) - 1/f) == 0 and sp.limit(r*(rs - r) + mu, r, sp.oo) == 0
        and sp.simplify(D(f, r).subs(r, rh)/2 - 1/rh) == 0)
    w = [sp.Function("w%d" % a)(*X[1:]) for a in range(N)]
    dT = [dd(C, w[0], b, True) for b in range(N)]
    Fw = [[dd(C, w[b], a, True) - dd(C, w[a], b, True) for b in range(N)] for a in range(N)]
    chk("(c) Cartan: d iota_T omega + iota_T d omega = -i sigma omega, T = d_t, omega spectral",
        all(sp.expand(dT[b] + Fw[0][b] + sp.I*sg*w[b]) == 0 for b in range(N)))
    return chk.ok


CHECKS = [("M1 box = 2 delta G delta* is d delta + delta d on every 1-form on Tangherlini (four-dimensional control)",
           m1, 1),
          ("M2 the scalar wave: -Phi_** + V_0 Phi = sigma^2 Phi, V_0 = (f/r^2)(kappa + 3/4 + 9 mu/(4 r^2)), any S",
           m2, 1),
          ("M3 the Maxwell vector type: V_1 = (f/r^2)(lam - 1/4 + 5 mu/(4 r^2)), any 1-form Y on S^3", m3, 1),
          ("M4 the Maxwell scalar type: R[r^3 F_tr] from Maxwell, V_2 = (f/r^2)(kappa + 3/4 - 7 mu/(4 r^2)), l = 0",
           m4, 1),
          ("M5 the potentials positive for r > r_h, the tortoise coordinate, Cartan's identity", m5, 1)]


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
    print(f"modes5.py: {len(CHECKS) if ok_all else 'FAILED'}/{len(CHECKS)}")
    return ok_all


def mutants():
    caught = total = 0
    for name, fn, nc in CHECKS:
        for k in range(1, nc + 1):
            total += 1
            res = fn(control=k)
            caught += (not res)
            print(f"mutant {k} of {name[:2]}: {'caught' if not res else 'NOT caught'}", flush=True)
    print(f"modes5.py mutants: {caught}/{total}")
    return caught == total


if __name__ == "__main__":
    args = sys.argv[1:]
    if "--mutants" in args:
        sys.exit(0 if mutants() else 1)
    sys.exit(0 if selftest(verbose="--verbose" in args) else 1)
