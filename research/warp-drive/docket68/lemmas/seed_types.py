#!/usr/bin/env python3
"""seed_types.py -- item 525 (SOURCE continued): the seed's escape with the record's waves split exactly into Kodama and
Ishibashi's scalar and tensor types, the scalar type on its own barrier; and how far the seed phase is from linear.

M, 525: "Continue with SOURCE please".  522 (seed_escape.py) computed the escape on scalar harmonics as a proxy and
named two points open: the scalar-type barrier at low l, and nonlinear scattering in the seed phase.  Labels: computed
(exact unless marked), READ (verbatim at source, 2026-10-19), deduced, estimate, M's.

  T0 (M's) 525, verbatim.
  T1 (computed, exact) The record's class holds scalar-type and tensor-type perturbations only.  Its two reflections
     forbid every metric component odd in phi1 or phi2; a divergence-free torus-invariant vector field on S^3 with only
     a theta component is C/(s c), singular, so no vector type enters.
  T2 (computed, exact) The torus-invariant tensor-type harmonics.  For diagonal T^i_j = (A, B, -A-B) on dth^2 + c^2
     dphi1^2 + s^2 dphi2^2, divergence-free fixes B = -(3x + 1)A/2 + (1 - x^2) A'; the rough Laplacian then gives
     A'' + 6 cot(2 theta) A' + (k_T^2 - 6) A = 0: Gegenbauer's equation in cos 2 theta, A_j = C_j^(3/2)(x),
     k_T^2 = 4 j (j + 3) + 6 = l(l + 2) - 2 with l = 2j + 2 -- every even l >= 2, as KI's (5.2) allows.
  T3 (computed, exact quadrature) The record's radiation, split.  Its angular perturbation (hf_mirror5's P1, P2) is
     trace-free on S^3: F carries (-2 s^2/3, -2 s^2/3, 4 s^2/3) h, G carries (-2 c^2/3, 4 c^2/3, -2 c^2/3) h (mixed
     components; F and G a quarter turn apart, so their energies add).  Projected in the energy norm on the scalar-type
     tensors D_i D_j P_k + (l(l+2)/3) gamma_ij P_k (l = 2k) and on the tensor-type harmonics: the powers sum to 1 to
     1e-15 (no third type), scalar type 0.639, tensor type 0.361; l = 2 holds 0.988 (0.635 + 0.353), l = 4 0.0085.
     522's proxy had put 0.777 at l = 0, which carries no radiation.
  T4 (READ; computed) The scalar-type barrier.  Kodama and Ishibashi, Prog. Theor. Phys. 110, 701 (2003), (3.6)-(3.7):
     "V_S(r) = f(r) Q(r) / (16 r^2 H^2)", H = m + n(n + 1) x / 2, m = k^2 - nK, x = 2M/r^(n-1), with Q as (3.7)
     prints it.  The transcription reproduces Zerilli's potential exactly at n = 2 (computed); at n = 3, K = 1:
     Q = 1296 x^3 + (624 m - 144) x^2 + (36 m^2 - 432 m) x + 16 m^3 + 60 m^2, H = m + 6x, m = l(l + 2) - 3.  The
     scalar-type reflection R_S(l, w r_h), l = 2k, k = 1..45, on 522's grid of w r_h: 1655 integrations, cached under
     a hash of its code; the tensor type is 522's grid (V_T is the massless scalar's, READ at 522).
  T5 (computed; deduced) Escape and the least seed at 10 l5, with S = sum_k (p^S_k R_S(2k) + p^T_k R_T(2k)).  The
     scalar type reflects far less at low l (at l = 2 its top reflects 0.0018 against the tensor type's 0.557), but
     the escape at w r_h near 11 is decided by the modes of l near 20 at their tops, where the two differ less: copper's
     least seed lets 4.87e-15 out (1.87e7 half bits; 522: 1.53e7), the least seed for half a bit is r_h0 17.99 l5,
     mu0 324 l5^2 (522: 17.95, 322); the example README's 2.41e5 half bits, 14.10 l5, 199 l5^2 (522: 13.96, 195);
     hf_core5's mu0 = 1000 passes both, 100 fails both; the least seed suffices only for lam <= 1.94 l5 (copper),
     2.51 l5 (example).  522's verdicts stand, its numbers moved by under 1%.
  T6 (computed; estimate) How far the seed phase is from linear.  On the record's shell (kn_gauge K8's profile, scaled
     to each case's r_hf) the wave's strain at the horizon is h_H = sqrt 2 lam_rec sqrt(mu') mu^(-3/4) (hf_mirror5's
     P1 at r = r_h, with mu' = (2/9) A^2 env^2) and the hole's growth per light-crossing is mu'/sqrt(mu).  Both are
     evaluated where the escape is decided (r_h from the least seed to twice it): h_H <= 2.6e-4 (copper), 1.6e-3
     (example); growth per crossing <= 7.6e-6, 1.8e-4.  The first order is a good expansion; but h_H^2 is 6.8e-8 and
     2.6e-6 of the wave's energy, 2.6e14 and 2.1e10 half bits: whether the second order leaves decides it (T7).
  T7 (computed on model sources; estimate) Whether the second order escapes.  Quadratic terms in an ingoing wave of
     frequency w drive the second-order field at 2w (the steady part is the round dust, l = 0: Birkhoff, it changes
     the mass and radiates nothing).  The driven field psi'' + ((2w)^2 - V_l2) psi = c(r) psi1^2 with psi1 the l = 2
     wave transmitted into the hole and model couplings c = f/r^p, p = 3, 6 (rational, singular only at r = 0, as
     the second-order couplings on Tangherlini are): its outgoing amplitude at infinity over its ingoing amplitude at
     the horizon, sigma, falls as e^(-s x), s near 2 pi (the phase mismatch e^(-4i w r*) against the singularity at
     Im r* = pi r_h/2), for l2 = 2, 4 and both types.  A passing seed starts at w r_h >= x* and only grows; the
     escaping second-order energy, 4 h_H^2 sigma(x*)^2 of the wave's, is set against half a bit with a deliberately
     low slope 3 from x = 3.
  Caveats.  Linear scattering off the hole as it stands at first order; the second order on model couplings (T7), not
  the exact second-order Einstein equations.  Beyond the computed window R follows the e^(-2 pi) law from its last
  value above 1e-15, an over-estimate of escape.

Imports seed_escape.py (its grid, solver form and cases) by path.  numpy, scipy, sympy, mpmath.
python3 seed_types.py [--selftest | --mutants | --build]
"""
import contextlib
import hashlib
import importlib.util
import inspect
import io
import json
import os
import sys

import mpmath as mp
import numpy as np
import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
RULINGS = os.path.join(HERE, "..", "M-RULINGS-2026-10-03.md")
DATA = os.path.join(HERE, "data", "seed_types.json")
K = 45
LAM = 10.0
MUT = set()
MUTANTS = {"proxy_power": "522's scalar-harmonic proxy in place of the exact split (T3-T5)",
           "so_no_phase": "the second-order source taken without the wave's phase (|psi1|^2 in place of psi1^2) (T7)",
           "scalar_on_VT": "the scalar type given the tensor-type barrier (T4-T5)",
           "no_tensor": "the tensor type dropped (T3-T5)",
           "lam_1": "the wavelength taken as 1 l5 in place of 10 (T5-T6)"}


def _load(name, key):
    spec = importlib.util.spec_from_file_location(key, os.path.join(HERE, name))
    mod = importlib.util.module_from_spec(spec)
    with contextlib.redirect_stdout(io.StringIO()):
        spec.loader.exec_module(mod)
    return mod


SE = _load("seed_escape.py", "st_seed_escape")


def words():
    s = open(RULINGS).read()
    return '"Continue with SOURCE please"' in s and "525. **Continue with SOURCE" in s


def tt_ode():
    """T2: divergence-free diagonal torus-invariant T, its rough Laplacian, the ODE for A"""
    th = sp.symbols("theta", positive=True)
    X = [th, sp.Symbol("p1"), sp.Symbol("p2")]
    g = sp.diag(1, sp.cos(th)**2, sp.sin(th)**2); gi = g.inv(); n = 3
    G = [[[sp.simplify(sum(gi[a, d]*(sp.diff(g[d, b], X[c]) + sp.diff(g[d, c], X[b]) - sp.diff(g[b, c], X[d]))
                           for d in range(n))/2) for c in range(n)] for b in range(n)] for a in range(n)]
    A, B = sp.Function("A")(th), sp.Function("B")(th)
    T = g*sp.diag(A, B, -A - B)
    DT = [[[sp.diff(T[i, j], X[k]) - sum(G[l][k][i]*T[l, j] + G[l][k][j]*T[i, l] for l in range(n))
            for j in range(n)] for i in range(n)] for k in range(n)]
    DDT = [[[[sp.diff(DT[k][i][j], X[m]) - sum(G[l][m][k]*DT[l][i][j] + G[l][m][i]*DT[k][l][j]
                                               + G[l][m][j]*DT[k][i][l] for l in range(n))
              for j in range(n)] for i in range(n)] for k in range(n)] for m in range(n)]
    lap = sp.Matrix(n, n, lambda i, j: sum(gi[m, k]*DDT[m][k][i][j] for m in range(n) for k in range(n)))
    div = sp.simplify(sum(gi[i, k]*DT[k][i][0] for i in range(n) for k in range(n)))
    Bs = sp.solve(sp.Eq(div, 0), B)[0]
    lam = sp.Symbol("lam")
    eq = sp.simplify(((gi*lap)[0, 0] + lam*A).subs(B, Bs).doit())
    target = sp.diff(A, th, 2) + 6*sp.cot(2*th)*sp.diff(A, th) + (lam - 6)*A
    a0, a1, a2, dx = sp.symbols("a0 a1 a2 dAdx")
    dif = (eq - target).subs(sp.Derivative(A, th, 2), a2).subs(sp.Derivative(A, th), a1).subs(A, a0)
    Bd = (Bs - (-(3*sp.cos(2*th) + 1)*A/2 + (1 - sp.cos(2*th)**2)*dx)).subs(
        sp.Derivative(A, th), -2*sp.sin(2*th)*dx).subs(A, a0)
    pts = [dict(zip((th, a0, a1, a2, dx, lam), v)) for v in
           ((0.37, 1.3, -0.4, 2.1, 0.8, 7.7), (1.1, -0.6, 1.9, 0.3, -1.2, 15.0), (0.71, 2.2, 0.5, -1.7, 0.4, 3.3))]
    j = sp.Symbol("j", positive=True)
    return dict(ode=max(abs(float(dif.subs(q))) for q in pts) < 1e-12,
                B=max(abs(float(Bd.subs(q))) for q in pts) < 1e-12,
                ell=sp.expand((4*j*(j + 3) + 6) - ((2*j + 2)*(2*j + 4) - 2)) == 0)


def _Q(n, K_, x, m):
    return (n**4*(n + 1)**2*x**3 + n*(n + 1)*(4*(2*n**2 - 3*n + 4)*m + n*(n - 2)*(n - 4)*(n + 1)*K_)*x**2
            - 12*n*((n - 4)*m + n*(n + 1)*(n - 2)*K_)*m*x + 16*m**3 + 4*K_*n*(n + 2)*m**2)


def zerilli():
    """KI (3.6)-(3.7) as transcribed, at n = 2, against Zerilli's potential"""
    r, M, l, x, m = sp.symbols("r M l x m", positive=True)
    f = 1 - 2*M/r
    V = (f*_Q(2, 1, x, m)/(16*r**2*(m + 3*x)**2)).subs({x: 2*M/r, m: l*(l + 1) - 2})
    lz = (l - 1)*(l + 2)/2
    VZ = f*(2*lz**2*(lz + 1)*r**3 + 6*lz**2*M*r**2 + 18*lz*M**2*r + 18*M**3)/(r**3*(lz*r + 3*M)**2)
    q3 = sp.expand(_Q(3, 1, x, m))
    return dict(zerilli=sp.simplify(V - VZ) == 0,
                q3=sp.expand(q3 - (1296*x**3 + (624*m - 144)*x**2 + (36*m**2 - 432*m)*x + 16*m**3 + 60*m**2)) == 0,
                far=sp.simplify(sp.limit(_Q(3, 1, x, m)/(16*(m + 6*x)**2), x, 0) - m - sp.Rational(15, 4)) == 0)


def VS(u, L):
    r = 1 + u; x = 1/(r*r); m = L*(L + 2) - 3; H = m + 6*x
    Q = 1296*x**3 + (624*m - 144)*x**2 + (36*m*m - 432*m)*x + 16*m**3 + 60*m*m
    return (1 - x)*Q/(16*r*r*H*H)


def refl_S(L, w, u0=1e-15, rmax=150.0, rtol=1e-11):
    """seed_escape's solver with the scalar-type potential"""
    from scipy.integrate import solve_ivp
    from scipy.special import h1vp, h2vp, hankel1, hankel2
    s0 = SE.rstar(u0)
    y0 = [np.cos(-w*s0), np.sin(-w*s0), w*np.sin(-w*s0), -w*np.cos(-w*s0), u0]

    def rhs(s, y):
        u = y[4]; q = VS(u, L) - w*w
        return [y[2], y[3], q*y[0], q*y[1], (2*u + u*u)/(1 + u)**2]
    sol = solve_ivp(rhs, [s0, rmax], y0, method="DOP853", rtol=rtol, atol=1e-14)
    s = sol.t[-1]; y = sol.y[:, -1]
    psi = y[0] + 1j*y[1]; dpsi = y[2] + 1j*y[3]
    nu = L + 1; z = w*s; c = np.sqrt(np.pi*z/2)
    ho = c*hankel1(nu, z); hi = c*hankel2(nu, z)
    dho = w*(c*h1vp(nu, z) + hankel1(nu, z)*np.sqrt(np.pi/(8*z)))
    dhi = w*(c*h2vp(nu, z) + hankel2(nu, z)*np.sqrt(np.pi/(8*z)))
    Ain, Aout = np.linalg.solve(np.array([[hi, ho], [dhi, dho]]), [psi, dpsi])
    return abs(Aout/Ain)**2, 1/abs(Ain)**2


def _tasks():
    return [(k, x) for k, x in SE._tasks() if k >= 1]


def _job(a):
    k, x = a
    R, T = refl_S(2*k, x)
    return [k, x, R, T]


def power_exact():
    """T3: the record's F and G polarizations in the energy norm on scalar-type and tensor-type harmonics"""
    mp.mp.dps = 30
    h = lambda x: mp.sqrt(2/(1 + x**2))                          # noqa: E731
    c2 = lambda x: (1 + x)/2                                     # noqa: E731
    s2 = lambda x: (1 - x)/2                                     # noqa: E731
    sF = lambda x: [-2*s2(x)/3*h(x), -2*s2(x)/3*h(x), 4*s2(x)/3*h(x)]      # noqa: E731
    sG = lambda x: [-2*c2(x)/3*h(x), 4*c2(x)/3*h(x), -2*c2(x)/3*h(x)]      # noqa: E731

    def S(k):
        L = 4*k*(k + 1)
        P = lambda t: mp.legendre(k, t)                          # noqa: E731

        def f(x):
            Y, d1, d2 = P(x), mp.diff(P, x), mp.diff(P, x, 2)
            return [4*(1 - x*x)*d2 - 4*x*d1 + L*Y/3, 2*(1 - x)*d1 + L*Y/3, -2*(1 + x)*d1 + L*Y/3]
        return f

    def T(j):
        C = lambda t: mp.gegenbauer(j, 1.5, t)                   # noqa: E731

        def f(x):
            A, dA = C(x), mp.diff(C, x)
            B = -(3*x + 1)*A/2 + (1 - x*x)*dA
            return [A, B, -A - B]
        return f
    ip = lambda a, b: mp.quad(lambda x: sum(u*v for u, v in zip(a(x), b(x))), [-1, 0, 1])   # noqa: E731
    tot = ip(sF, sF) + ip(sG, sG)
    pS = [float((ip(sF, S(k))**2 + ip(sG, S(k))**2)/ip(S(k), S(k))/tot) for k in range(1, K + 1)]
    pT = [float((ip(sF, T(j))**2 + ip(sG, T(j))**2)/ip(T(j), T(j))/tot) for j in range(K)]
    orth = max(abs(float(v)) for v in (ip(S(1), T(0)), ip(S(3), T(5)), ip(S(2), S(4)), ip(T(1), T(3))))
    trace = max(abs(float(sum(sF(mp.mpf(x))))) + abs(float(sum(sG(mp.mpf(x))))) for x in (-0.7, 0.1, 0.9))
    return dict(pS=pS, pT=pT, orth=orth, trace=trace)


def _hash():
    src = "".join(inspect.getsource(f) for f in (VS, refl_S, _tasks, _job, power_exact))
    src += "".join(inspect.getsource(f) for f in (SE.rstar, SE._tasks))
    return hashlib.md5(src.encode()).hexdigest()


def build():
    """the scalar-type grid (about ten minutes on four processes) and the exact split, with the hash of their code"""
    from multiprocessing import Pool
    with Pool(4) as p:
        rows = p.map(_job, _tasks(), chunksize=4)
    d = dict(hash=_hash(), rows=rows, **power_exact())
    os.makedirs(os.path.dirname(DATA), exist_ok=True)
    json.dump(d, open(DATA, "w"))
    return d


def data():
    d = json.load(open(DATA)) if os.path.exists(DATA) else {}
    return d if d.get("hash") == _hash() else build()


def _I(mS, mT, pS, pT):
    X = SE.X
    S = np.zeros_like(X)
    for k in range(1, K + 1):
        if "no_tensor" not in MUT:
            S += pT[k - 1]*SE._Rk(mT, k, X)
        S += pS[k - 1]*SE._Rk(mT if "scalar_on_VT" in MUT else mS, k, X)
    S += (pS[-1] + pT[-1])/(1 - 0.2)                              # power above k = 45, reflected fully (bound)
    xS = X*S
    return np.concatenate([np.cumsum((xS[1:] + xS[:-1])[::-1]/2*np.diff(X)[::-1])[::-1], [0.0]])


def escape(I, cs, lam):
    X = SE.X
    out = {}
    for name, c in cs.items():
        wr = 2*np.pi*c["rhf"]/lam; half = 1/(3*c["N"]); need = half*wr**2/2
        x0 = 2*np.pi*72**0.25/lam
        esc0 = 2*np.interp(x0, X, I)/wr**2
        xs = X[I < need][0]; rh = xs*lam/(2*np.pi)
        ok = {mu0: 2*np.interp(2*np.pi*np.sqrt(mu0)/lam, X, I)/wr**2 < half for mu0 in (100.0, 1000.0)}
        out[name] = dict(half=half, esc0=esc0, nhalf=esc0/half, x=xs, rh=rh, mu0=rh**2, ok=ok)
    return out


def lam_least(I, cs):
    X = SE.X
    out = {}
    for name, c in cs.items():
        lo, hi = 0.1, 10.0
        for _ in range(60):
            lam = 0.5*(lo + hi); wr = 2*np.pi*c["rhf"]/lam
            if 2*np.interp(2*np.pi*72**0.25/lam, X, I)/wr**2 < 1/(3*c["N"]):
                lo = lam
            else:
                hi = lam
        out[name] = lo
    return out


def nonlinear(cs, esc, lam):
    """T6: the strain at the horizon and the growth per crossing where escape is decided, on the record's shell"""
    A5 = _load("hf_anchor5.py", "st_anchor").a1()
    s = np.linspace(0, 1, 2000001); env = np.sin(np.pi*s)**4; Dd = A5["D"]
    out = {}
    for name, c in cs.items():
        mu0 = A5["seed"]/c["rhf"]**2; dmu = 1 - mu0
        mup = dmu*env**2/((35/128)*Dd)
        muv = mu0 + np.concatenate([[0], np.cumsum((mup[1:] + mup[:-1])/2*np.diff(s*Dd))])
        lr = lam/(2*np.pi)/c["rhf"]                                # the record's lam (phase v/lam), r_hf units
        rh0 = esc[name]["rh"]/c["rhf"]
        win = (np.sqrt(muv) >= rh0) & (np.sqrt(muv) <= 2*rh0)
        if not win.any():                                           # the window lies below the seed: the seed itself
            win[0] = True
        hH = np.sqrt(2)*lr*np.sqrt(mup)*muv**-0.75
        eps = mup/np.sqrt(muv)
        out[name] = dict(hH=float(hH[win].max()), eps=float(eps[win].max()), hH2=float(hH[win].max()**2),
                         s_win=(float(s[win].min()), float(s[win].max())))
    return out


def vector_free():
    """T1: a divergence-free vector field on S^3 with only a theta component"""
    th = sp.symbols("theta", positive=True)
    V = sp.Function("V")
    sol = sp.dsolve(sp.Eq(sp.diff(sp.sin(th)*sp.cos(th)*V(th), th), 0), V(th)).rhs
    C1 = [a for a in sol.free_symbols if a.name == "C1"][0]
    one = sol.subs(C1, 1)
    return (sp.simplify(sp.diff(sol*sp.sin(th)*sp.cos(th), th)) == 0 and sp.limit(one, th, 0, "+") == sp.oo
            and sp.limit(one, th, sp.pi/2, "-") == sp.oo)


def second_order(x, l2, p, V2, rmax=150.0, u0=1e-12, rtol=1e-12):
    """T7: the field driven at 2w by c(r) psi1^2, psi1 the l = 2 wave transmitted into the hole (same type as V2);
    returns |outgoing amplitude at infinity| / |ingoing amplitude at the horizon|"""
    from scipy.integrate import solve_ivp
    from scipy.special import h1vp, hankel1
    w = x; W = 2*w; s0 = SE.rstar(u0)
    c = lambda u: (2*u + u*u)/(1 + u)**2/(1 + u)**p           # noqa: E731
    sq = (lambda z: abs(z)**2) if "so_no_phase" in MUT else (lambda z: z*z)   # noqa: E731

    def rhs(s, y):
        u = y[8]; p1 = y[0] + 1j*y[1]; pH = y[4] + 1j*y[5]
        q1 = V2(u, 2) - w*w; qH = V2(u, l2) - W*W; IH = pH*c(u)*sq(p1)
        return [y[2], y[3], q1*y[0], q1*y[1], y[6], y[7], qH*y[4], qH*y[5], (2*u + u*u)/(1 + u)**2, IH.real, IH.imag]
    e1 = np.exp(-1j*w*s0); eH = np.exp(-1j*W*s0)
    y0 = [e1.real, e1.imag, (-1j*w*e1).real, (-1j*w*e1).imag, eH.real, eH.imag, (-1j*W*eH).real, (-1j*W*eH).imag,
          u0, 0, 0]
    so = solve_ivp(rhs, [s0, rmax], y0, method="DOP853", rtol=rtol, atol=1e-16, dense_output=True)
    yE = so.y[:, -1]; sE = so.t[-1]
    pH = yE[4] + 1j*yE[5]; dpH = yE[6] + 1j*yE[7]
    nu = l2 + 1; z = W*sE; cc = np.sqrt(np.pi*z/2)
    po = cc*hankel1(nu, z); dpo = W*(cc*h1vp(nu, z) + hankel1(nu, z)*np.sqrt(np.pi/(8*z)))

    def rhs2(s, y):
        yy = so.sol(s); u = yy[8]; p1 = yy[0] + 1j*yy[1]; pI = y[0] + 1j*y[1]
        qI = V2(u, l2) - W*W; I = pI*c(u)*sq(p1)
        return [y[2], y[3], qI*y[0], qI*y[1], I.real, I.imag]
    si = solve_ivp(rhs2, [sE, s0], [po.real, po.imag, dpo.real, dpo.imag, 0, 0], method="DOP853", rtol=rtol,
                   atol=1e-16)
    Wr = pH*dpo - dpH*po
    return float(abs((yE[9] + 1j*yE[10])/Wr)/abs((si.y[4, -1] + 1j*si.y[5, -1])/Wr))


def so_bound(esc, nl):
    """T7: sigma at w r_h = 2 and 3 for l2 = 2, 4, both types, p = 3, 6; the bound at x* against half a bit"""
    sig = {}
    for tag, V2 in (("T", SE.V), ("S", VS)):
        for l2 in (2, 4):
            for p in (3, 6):
                sig[(tag, l2, p)] = (second_order(2.0, l2, p, V2), second_order(3.0, l2, p, V2))
    slopes = {k: -np.log(b/a) for k, (a, b) in sig.items()}
    s3 = max(b for a, b in sig.values())
    out = {}
    for name in esc:
        xs = esc[name]["x"]
        sx = s3*np.exp(-3.0*(xs - 3.0))                             # a deliberately low slope, 3, from x = 3
        frac = 4*nl[name]["hH"]**2*sx**2
        out[name] = dict(sigma_xstar=sx, frac=frac, ratio=frac/esc[name]["half"])
    return dict(sig=sig, slopes=slopes, s3=s3, cases=out)


def compute():
    d = data()
    mS = SE._modes(d["rows"]); mT = SE._modes(SE.grid())
    pS, pT = d["pS"], d["pT"]
    if "proxy_power" in MUT:
        p = SE.power(); pS = list(p[1:]); pT = [0.0]*K; pS[0] += p[0]
    if "no_tensor" in MUT:
        tot = sum(pS); pS = [v/tot for v in pS]
    cs = SE.cases()
    lam = 1.0 if "lam_1" in MUT else LAM
    I = _I(mS, mT, pS, pT)
    esc = escape(I, cs, lam)
    m = {k: dict((round(x, 3), R) for x, R in zip(*mS[k])) for k in mS}
    mt = {k: dict((round(x, 3), R) for x, R in zip(*mT[k])) for k in mT}
    top = {k: (m[k][round(k + 0.5, 3)], mt[k][round(k + 0.5, 3)]) for k in (1, 2, 5, 10, 45)}
    nl = nonlinear(cs, esc, lam)
    return dict(words=words(), vec=vector_free(), tt=tt_ode(), zer=zerilli(), d=d, n=len(d["rows"]),
                flux=max(abs(R + T - 1) for k, x, R, T in d["rows"]), top=top, esc=esc, lamleast=lam_least(I, cs),
                nl=nl, so=so_bound(esc, nl), pS=pS, pT=pT)


def checks(o):
    ch = {}
    ch["T0 words of 525"] = o["words"]
    ch["T1 no vector type: a divergence-free theta-only vector on S^3 is C/(s c), singular at both axes"] = o["vec"]
    t = o["tt"]
    ch["T2 tensor-type harmonics: A'' + 6 cot(2 th) A' + (k_T^2 - 6) A = 0, C_j^(3/2)(cos 2 th), l = 2j + 2"] = (
        t["ode"] and t["B"] and t["ell"])
    d = o["d"]; pS, pT = o["pS"], o["pT"]
    ch["T3 exact split: sum 1 to 1e-12, scalar 0.6390, tensor 0.3610; l = 2 holds 0.6353 + 0.3531; bases orthogonal"] = (
        abs(sum(pS) + sum(pT) - 1) < 1e-12 and abs(sum(pS) - 0.63897) < 1e-5 and abs(sum(pT) - 0.36103) < 1e-5
        and abs(pS[0] - 0.63534) < 1e-5 and abs(pT[0] - 0.35307) < 1e-5 and d["orth"] < 1e-25 and d["trace"] == 0)
    z = o["zer"]; tp = o["top"]
    ch["T4 KI's V_S: Zerilli at n = 2, Q at n = 3 as stated, the far potential ((l+1)^2 - 1/4)/r^2"] = (
        z["zerilli"] and z["q3"] and z["far"])
    ch["T4 scalar-type grid: 1655 points, R + T = 1 to 2e-9; at the top R_S 0.0018 (l = 2) rising to 0.465 (l = 90)"] = (
        o["n"] == 1655 and o["flux"] < 2e-9 and abs(tp[1][0] - 0.0018) < 1e-4 and abs(tp[45][0] - 0.4653) < 1e-3
        and all(tp[a][0] < tp[b][0] for a, b in ((1, 2), (2, 5), (5, 10), (10, 45)))
        and all(tp[k][0] < tp[k][1] for k in tp))
    c, x = o["esc"]["copper"], o["esc"]["example"]
    ch["T5 copper: least seed 1.87e7 half bits out; half a bit needs r_h0 17.99 l5, mu0 324 l5^2"] = (
        abs(c["nhalf"]/1.87e7 - 1) < 0.01 and abs(c["rh"] - 17.99) < 0.01 and abs(c["mu0"] - 324) < 1)
    ch["T5 example README: 2.41e5 half bits; r_h0 14.10 l5, mu0 199 l5^2; mu0 = 1000 passes both, 100 fails both"] = (
        abs(x["nhalf"]/2.41e5 - 1) < 0.01 and abs(x["rh"] - 14.10) < 0.01 and abs(x["mu0"] - 199) < 1
        and c["ok"][1000.0] and x["ok"][1000.0] and not c["ok"][100.0] and not x["ok"][100.0])
    ll = o["lamleast"]
    ch["T5 the least seed suffices only for lam <= 1.943 l5 (copper), 2.509 l5 (example)"] = (
        abs(ll["copper"] - 1.943) < 0.002 and abs(ll["example"] - 2.509) < 0.002)
    n = o["nl"]
    ch["T6 where escape is decided: h_H <= 2.6e-4 / 1.62e-3, growth per crossing <= 7.6e-6 / 1.8e-4"] = (
        abs(n["copper"]["hH"] - 2.60e-4) < 0.05e-4 and abs(n["example"]["hH"] - 1.62e-3) < 0.02e-3
        and abs(n["copper"]["eps"] - 7.55e-6) < 0.1e-6 and abs(n["example"]["eps"] - 1.81e-4) < 0.02e-4)
    q = o["so"]
    ch["T7 second order at 2w: sigma falls with slope 5.6-7.0 (near 2 pi) for l2 = 2, 4, both types, p = 3, 6"] = (
        all(5.6 < v < 7.0 for v in q["slopes"].values()) and len(q["slopes"]) == 8)
    ch["T7 escaping second order, slope 3 from x = 3: <= 1.1e-16 (copper), 2.1e-14 (example) half bits"] = (
        q["cases"]["copper"]["ratio"] < 1.2e-16 and q["cases"]["example"]["ratio"] < 2.2e-14)
    return ch


def report(o=None):
    o = o or compute()
    for k_, v_ in checks(o).items():
        print("%-118s %s" % (k_[:118], "PASS" if v_ else "FAIL"))
    print("  T1 %s; T2 %s; T4 %s" % (o["vec"], o["tt"], o["zer"]))
    d = o["d"]
    print("  T3 sum pS %.6f, sum pT %.6f, total %.15f; l = 2: %.6f + %.6f; l = 4: %.3e + %.3e; orth %.1e, trace %.1e"
          % (sum(o["pS"]), sum(o["pT"]), sum(o["pS"]) + sum(o["pT"]), o["pS"][0], o["pT"][0], o["pS"][1], o["pT"][1],
             d["orth"], d["trace"]))
    print("  T4 %d points, max |R + T - 1| %.2g; R at the top (scalar, tensor): %s"
          % (o["n"], o["flux"], {k: (round(a, 4), round(b, 4)) for k, (a, b) in o["top"].items()}))
    for n_, e in o["esc"].items():
        print("  T5 %-8s least seed escapes %.3g = %.3g half bits; least seed for half a bit w r_h %.2f, r_h0 %.2f l5,"
              " mu0 %.0f l5^2; mu0 100 %s, 1000 %s" % (n_, e["esc0"], e["nhalf"], e["x"], e["rh"], e["mu0"],
                                                       e["ok"][100.0], e["ok"][1000.0]))
    print("  T5 the least seed delivers for lam <= %s l5" % {k: round(v, 3) for k, v in o["lamleast"].items()})
    for n_, e in o["nl"].items():
        print("  T6 %-8s strain at the horizon <= %.3g (squared %.3g = %.3g half bits), growth per crossing <= %.3g,"
              " over s in %s" % (n_, e["hH"], e["hH2"], e["hH2"]/o["esc"][n_]["half"], e["eps"], e["s_win"]))
    q = o["so"]
    print("  T7 sigma at w r_h 2, 3 and slope: %s" % {"%s%d p%d" % k: ("%.2e" % a, "%.2e" % b, round(q["slopes"][k], 2))
                                                    for k, (a, b) in q["sig"].items()})
    for n_, e in q["cases"].items():
        print("  T7 %-8s sigma(x*) <= %.2e (slope 3 from %.2e at x = 3); second-order escape <= %.2e = %.2e half bits"
              % (n_, e["sigma_xstar"], q["s3"], e["frac"], e["ratio"]))


def selftest():
    c = checks(compute())
    n = sum(c.values())
    for k_, v_ in c.items():
        print("%-118s %s" % (k_[:118], "PASS" if v_ else "FAIL"))
    print("seed_types.py: %d/%d" % (n, len(c)))
    return n == len(c) and n > 0


def mutants():
    caught = 0
    for m_, desc in MUTANTS.items():
        MUT.clear(); MUT.add(m_)
        try:
            c = checks(compute()); failed = [k[:44] for k, v in c.items() if not v]
        except Exception as ex:                                  # noqa: BLE001
            failed = ["raised %s" % type(ex).__name__]
        caught += bool(failed)
        print("mutant %-14s %s  (%s)  failing: %s" % (m_, "caught" if failed else "MISSED", desc, "; ".join(failed)))
    MUT.clear()
    print("mutants: %d/%d" % (caught, len(MUTANTS)))
    return caught == len(MUTANTS)


if __name__ == "__main__":
    if "--build" in sys.argv:
        print("%d points" % len(build()["rows"]))
        sys.exit(0)
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    if "--mutants" in sys.argv:
        sys.exit(0 if mutants() else 1)
    report()
