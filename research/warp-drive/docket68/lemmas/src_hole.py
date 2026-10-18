#!/usr/bin/env python3
"""src_hole.py -- items 506-508: the shell onto its seed and into the record's core, with no inner horizon and nothing cut
out -- the high-frequency limit (5D Vaidya) and the core as the record computes it, held against the exclusions first.

M, 506: "Those will be answered by the math. Redo the work without the inner horizon"; 508: "There is always a seed -
refer to the the method corpus materials".  Labels: READ (verbatim), computed (exact unless marked), deduced, M's.

Held against the exclusions before computing (481, M-CHECK-EXCLUSIONS; 484, M-NO-CAUCHY): no inner horizon (464, 471) --
every f below has exactly two roots, our black hole's and position 2's white hole's; no Cauchy horizon -- the core is
regular (R >= a > 0) and never visible from infinity once the seed is there (S4); no classical bounce (318) and no
semiclassical one (C9) -- null energy fails only inside x = l5^2 sqrt(K) >= 1 (S7).

  S0 (M's) 506 and 508, verbatim in the rulings file.
  S1 (READ, computed) Ghosh and Dadhich (gr-qc/0105085, eqs. (9)-(11), Table I): 5D null-fluid collapse from flat space,
     mu = lam v^2, is naked -- a Cauchy horizon, the earliest ray out of the singularity -- iff lam X^3 - X + 2 = 0 has a
     positive root, i.e. lam <= 1/27, with X0 = 3 there.  Reproduced: the prior art's measure of when a forming 5D hole
     shows its centre.
  S2 (computed, exact) In 5D Vaidya the record's quantum boundary x = 1 (K = 72 mu^2/r^8, null dust adding no Ricci
     square) is r_q^4 = sqrt(72) mu l5^2, inside the apparent horizon r = sqrt(mu) iff mu > sqrt(72) l5^2.
  S3 (computed) No seed.  At the record's least arrival spread, sigma_t = 28.5 r_h (emitter_process C2; the sin^8 flux
     of hf_mirror5 over D = 269.2 r_h), outgoing rays from the core in its first phase (mu < sqrt(72) l5^2, where r_q >
     sqrt(mu)) reach infinity, at mu_f/l5^2 = 1e4 and 7e40: the core is seen from outside, 273's one-way passage and
     484 both fail.  The core stays hidden only for sigma_t below ~0.5-0.8 r_h, some 40-60 times shorter than C2 allows.
  S3b (computed) The same for the record's own optimal shell, the band-limited state of C2 (energy amplitude a half-
     sine across the band; arrival flux cos^2(pi t/tau)/(1 - 4 t^2/tau^2)^2, sigma_t = tau/2 = 28.5 r_h exactly, its
     t^-4 tail reaching back without end): a ray from the core's first phase reaches infinity at 1e4 and 7e40.
  S4 (computed) A seed of mu0 = 1.01 sqrt(72) l5^2 in place before the shell: every outgoing ray from the core, from the
     shell's first instant to its last, is trapped at once (r_q < sqrt(mu) throughout), at 1e4 and 7e40.  So the math
     answers 506's question as 508 states it: the shell arrives onto a seed, and the least seed is the one whose quantum
     region already lies inside its horizon, mu0 >= sqrt(72) l5^2 (r_h >= 72^(1/4) l5 = 2.91 l5).
  S5 (READ) The Method, sec. 14.5.7-14.5.9 and Registers 1793, 1797: a closed index has a seed; it is constructible,
     need never be searched for, and is "a size, not a set".  S4 gives the hole's seed as a size.
  S6 (computed, exact) The core while it takes the shell in.  On transition5's chart, ds^2 = -f dv^2 + 2 dv dr +
     R^2 dOmega_3^2 with f = 1 - M(r, v)/R^2, R^2 = r^2 + a^2 S(r): the Einstein tensor is derived from the metric, and
     its null energies are G(n,n) = -3 R''/R (n = -d_r) and G(l,l) = -3[(M - R^2)^2 R'' - 2 R^2 M_v R']/(4 R^5)
     (l = d_v + (f/2) d_r) when the transition surface's size a is held through the accretion, and G(l,n) + G(e,e) (e a
     unit vector on the sphere), which with them decides every null direction.  Outside the modified region (R = |r|)
     our side is exactly 5D Vaidya null dust, G(l,l) = 3 mu'/(2 r^3) >= 0 and the mixed part 0.
  S7 (computed) The mass may not be raised on both sides.  With M = mu(v) everywhere, position 2's classical exterior
     (R = -r) carries G(l,l) = -3 mu'/(2 R^3) < 0: negative energy where general relativity holds.  With M rising from
     position 2's constant mu2 to our mu(v) inside 0 <= r <= r2 (r2 <= r_q, so inside x >= 1), null energy fails only
     inside the modified region, our side is the shell's null dust and position 2's side is vacuum: the shell's energy
     is taken up by the core's effective stress (as in regular-Vaidya prior art, arXiv 2506.14875, READ by abstract),
     and none reaches position 2 -- only information does (386, 336, 491).
  S8 (computed) Through the accretion f has exactly two roots, +sqrt(mu(v)) and -sqrt(mu2), and is negative between
     them (no inner horizon, no Cauchy horizon); R' vanishes only at r = 0 (one transition surface); radial ingoing null
     rays have r affine (dr/dlam = -E), so every part of the README crosses the transition surface one way.
  What this does not compute: position 2's mass mu2 -- the record's equal-mass face (transition5q H6, emitter_process
  D4) then has to come from position 2's own bulk (240, 285), not from the shell; and the exact vacuum sequence onto
  the seed down to x = 1, which hf_core5.py runs.

python3 src_hole.py [--selftest | --mutants]
"""
import sys, os
import numpy as np
import sympy as sp
from scipy.integrate import solve_ivp, quad
from scipy.optimize import brentq

HERE = os.path.dirname(os.path.abspath(__file__))
RULINGS = os.path.join(HERE, "..", "M-RULINGS-2026-10-03.md")
MUT = set()
S8C = 35/128
_c = [1.0, -4/3, 38/45, -64/189]          # sin^8 x = x^8 (1 - (4/3) x^2 + (38/45) x^4 - (64/189) x^6 + ...)


def Phi(u):
    """the shell's delivered fraction: int_0^u sin^8(pi s) ds / (35/128), by its series where the closed form cancels"""
    if u <= 0:
        return 0.0
    if u >= 1:
        return 1.0
    x = np.pi*u
    if u < 0.01:
        return np.pi**8*u**9*(1/9 + _c[1]*x**2/11 + _c[2]*x**4/13 + _c[3]*x**6/15)/S8C
    return (35*u - 28*np.sin(2*x)/np.pi + 7*np.sin(4*x)/np.pi - 4*np.sin(6*x)/(3*np.pi) + np.sin(8*x)/(8*np.pi))/128/S8C


SIG = np.sqrt(quad(lambda u: (u - 0.5)**2*np.sin(np.pi*u)**8, 0, 1)[0]/S8C)    # sigma_t/D of the sin^8 flux
D_REC = 28.5/SIG                                                              # the record's least spread, in r_h


def mu(v, D, m0=0.0):
    return m0 + (1 - m0)*Phi(v/D)


def r_q(m, L):
    return (np.sqrt(72)*m/L)**0.25


def fate(v0, r0, D, m0=0.0):
    """an outgoing radial null ray of 5D Vaidya from (v0, r0), in s = ln r: 'trapped' once inside sqrt(mu) (with mu
    non-decreasing it stays), 'escapes' once outside 1.01 r_h after the shell"""
    if r0**2 <= mu(v0, D, m0):
        return "trapped"
    f = lambda v, s: [0.5*np.exp(-s[0])*(1 - mu(v, D, m0)*np.exp(-2*s[0]))]
    def tr(v, s):
        m = mu(v, D, m0)
        return s[0] - 0.5*np.log(m) if m > 0 else 1.0
    tr.terminal, tr.direction = True, -1
    es = lambda v, s: (s[0] - np.log(1.01)) if v > D else -1.0
    es.terminal, es.direction = True, 1
    s = solve_ivp(f, (v0, D + 200), [np.log(r0)], method="LSODA", rtol=1e-10, atol=1e-12, events=[tr, es])
    return "trapped" if s.t_events[0].size else "escapes" if s.t_events[1].size else "undecided"


def planck_v0(D, L, frac, m0=0.0):
    """a time in the core's first phase, where mu = frac sqrt(72) l5^2"""
    return brentq(lambda u: Phi(u) - frac*np.sqrt(72)/L, 1e-16, 0.5, xtol=1e-18)*D


def words():
    s = open(RULINGS).read()
    return ("Those will be answered by the math. Redo the work without the inner horizon" in s
            and "There is always a seed - refer to the the method corpus materials" in s)


def s1():
    out = {}
    for k in (0.999, 1.001):
        rt = np.roots([k/27, 0, -1, 2])
        out[k] = sorted(x.real for x in rt if abs(x.imag) < 1e-9 and x.real > 0)
    lc = 1/27
    return dict(below=out[0.999], above=out[1.001], X0=float(np.roots([lc, 0, -1, 2])[np.argmin(abs(np.roots([lc, 0, -1, 2]) - 3))].real))


def s2():
    L = 1e4
    m_c = np.sqrt(72)/L
    return dict(inside_above=r_q(1.001*m_c, L) < np.sqrt(1.001*m_c), outside_below=r_q(0.999*m_c, L) > np.sqrt(0.999*m_c),
                equal=abs(r_q(m_c, L)/np.sqrt(m_c) - 1))


def s3():
    D = 0.2/SIG if "short_spread" in MUT else D_REC
    out = {}
    for L in (1e4, 7e40):
        out[L] = [fate(v0, r_q(mu(v0, D), L), D) for v0 in (planck_v0(D, L, fr) for fr in (0.01, 0.5, 0.99))]
    lo, hi = 1.0, D_REC
    for _ in range(14):
        mid = 0.5*(lo + hi); v0 = planck_v0(mid, 7e40, 0.5)
        if fate(v0, r_q(mu(v0, mid), 7e40), mid) == "escapes":
            hi = mid
        else:
            lo = mid
    return dict(rays=out, sigma_c=hi*SIG, D=D)


def _g(t):
    """the record's optimal band-limited shell (emitter_process C2): energy amplitude a half-sine across the band, so the
    arrival flux is |its Fourier transform|^2 ~ cos^2(pi t/tau)/(1 - 4 t^2/tau^2)^2, t in units of tau"""
    return np.cos(np.pi*t)**2/(1 - 4*t**2)**2 if abs(abs(t) - 0.5) > 1e-9 else (np.pi/4)**2


_Z = 2*quad(_g, 0, 60, limit=400)[0] + 2*quad(lambda t: 0.5/(16*t**4), 60, np.inf)[0]


def _frac(u):
    if u < -60:
        return 0.5/(16*3*abs(u)**3)/_Z
    pts = [p_ for p_ in (-0.5, 0.5) if -60 < p_ < u]
    return (quad(lambda t: 0.5/(16*t**4), -np.inf, -60)[0] + quad(_g, -60, u, limit=400, points=pts or None)[0])/_Z


def s3b():
    """no seed, the record's own optimal shell at sigma_t = 28.5 r_h: a ray from the core in its first phase"""
    var = 2*quad(lambda t: t*t*_g(t), 0, 60, limit=400)[0]/_Z + 2*quad(lambda t: t*t*0.5/(16*t**4), 60, np.inf)[0]/_Z
    tau = 28.5/np.sqrt(var)
    out = {}
    for L in (1e4, 7e40):
        target = 0.5*np.sqrt(72)/L
        v0 = -(0.5/(16*3*target*_Z))**(1/3)*tau
        m0 = _frac(v0/tau)
        f = lambda v, s_: [0.5*np.exp(-s_[0])*(1 - _frac(v/tau)*np.exp(-2*s_[0]))]
        tr = lambda v, s_: s_[0] - 0.5*np.log(max(_frac(v/tau), 1e-300))
        tr.terminal, tr.direction = True, -1
        sol = solve_ivp(f, (v0, 5*tau), [np.log(r_q(m0, L))], method="LSODA", rtol=1e-8, atol=1e-10, events=[tr])
        out[L] = "trapped" if sol.t_events[0].size else ("escapes" if np.exp(sol.y[0][-1]) > 1.01 else "undecided")
    return dict(rays=out, sig_over_tau=np.sqrt(var))


def s4():
    out = {}
    for L in (1e4, 7e40):
        m0 = 0.0 if "no_seed" in MUT else 1.01*np.sqrt(72)/L
        res = []
        for u0 in (0.0, 1e-6, 1e-3, 0.1, 0.5, 0.9, 1.0):
            v0 = u0*D_REC
            if m0 == 0.0 and u0 < 1e-3:
                v0 = planck_v0(D_REC, L, 0.5)
            res.append(fate(v0, r_q(mu(v0, D_REC, m0), L), D_REC, m0))
        out[L] = res
    return out


def s6():
    """the Einstein tensor of -f dv^2 + 2 dv dr + R^2 dOmega_3^2, f = 1 - M(r,v)/R^2, from the metric"""
    v, r, th, p1, p2 = sp.symbols('v r theta phi1 phi2', real=True)
    Mf = sp.Function('M')(r, v); Rf = sp.Function('R')(r)
    f = 1 - Mf/Rf**2
    X = [v, r, th, p1, p2]
    g = sp.zeros(5); g[0, 0] = -f; g[0, 1] = g[1, 0] = 1
    g[2, 2] = Rf**2; g[3, 3] = Rf**2*sp.cos(th)**2; g[4, 4] = Rf**2*sp.sin(th)**2
    gi = g.inv()
    Gam = [[[sp.simplify(sum(gi[a, d]*(sp.diff(g[d, b], X[c]) + sp.diff(g[d, c], X[b]) - sp.diff(g[b, c], X[d]))
                             for d in range(5))/2) for c in range(5)] for b in range(5)] for a in range(5)]
    Rc = sp.zeros(5)
    for b in range(5):
        for c in range(b, 5):
            Rc[b, c] = Rc[c, b] = sp.simplify(sum(sp.diff(Gam[a][b][c], X[a]) - sp.diff(Gam[a][b][a], X[c])
                                                  + sum(Gam[a][a][d]*Gam[d][b][c] - Gam[a][c][d]*Gam[d][b][a]
                                                        for d in range(5)) for a in range(5)))
    Rs = sp.simplify(sum(gi[a, b]*Rc[a, b] for a in range(5) for b in range(5)))
    G = (Rc - Rs*g/2).applyfunc(sp.simplify)
    n = [0, -1, 0, 0, 0]; l = [1, f/2, 0, 0, 0]
    Gnn = sp.simplify(sum(G[a, b]*n[a]*n[b] for a in range(5) for b in range(5)))
    Gll = sp.simplify(sum(G[a, b]*l[a]*l[b] for a in range(5) for b in range(5)))
    Gln = sp.simplify(sum(G[a, b]*l[a]*n[b] for a in range(5) for b in range(5)))
    Gee = sp.simplify(G[2, 2]/Rf**2)
    Rp, Rpp, Mv, Mm, Rr, Mr, Mrr, Mrv = sp.symbols("Rp Rpp Mv Mm Rr Mr Mrr Mrv")
    sub = {sp.Derivative(Rf, (r, 2)): Rpp, sp.Derivative(Rf, r): Rp, sp.Derivative(Mf, r, v): Mrv,
           sp.Derivative(Mf, (r, 2)): Mrr, sp.Derivative(Mf, r): Mr, sp.Derivative(Mf, v): Mv}
    gnn = sp.simplify(Gnn.subs(sub).subs({Mf: Mm, Rf: Rr}))
    gll = sp.simplify(Gll.subs(sub).subs({Mf: Mm, Rf: Rr}))
    gmix = sp.simplify((Gln + Gee).subs(sub).subs({Mf: Mm, Rf: Rr}))
    want_nn = -3*Rpp/Rr
    want_ll = -3*((Mm - Rr**2)**2*Rpp - 2*Rr**2*Mv*Rp)/(4*Rr**5)
    ok = sp.simplify(gnn - want_nn) == 0 and sp.simplify(gll - want_ll) == 0
    ours = sp.simplify(want_ll.subs({Rpp: 0, Rp: 1, Rr: r}))
    p2s = sp.simplify(want_ll.subs({Rpp: 0, Rp: -1, Rr: r}))
    mix_vac = sp.simplify(gmix.subs({Rpp: 0, Rp: 1, Rr: r, Mr: 0, Mrr: 0, Mrv: 0}))     # 0 on 5D Vaidya
    lam = sp.lambdify((Mm, Mr, Mrr, Mv, Rr, Rp, Rpp), gmix, "numpy")
    return dict(forms=ok, ours=ours, pos2=p2s, gnn=gnn, gll=gll, gmix=gmix, mix_vac=mix_vac, mix=lam)


def P(x, k=0):
    """the C^4 smoothstep x^5 (126 - 420 x + 540 x^2 - 315 x^3 + 70 x^4) on [0, 1] and its first two derivatives"""
    x = np.clip(x, 0, 1)
    if k == 0:
        return x**5*(126 - 420*x + 540*x**2 - 315*x**3 + 70*x**4)
    if k == 1:
        return 630*x**4*(1 - x)**4
    return 2520*x**3*(1 - x)**3*(1 - 2*x)


def core_model(mix, L=1e4, mu0=1.0, mu2=1.18229, dmu=0.18229):
    """the accreting core on transition5's chart, in units of the seed, every derivative exact: l5^2 = mu0/L,
    a^4 = mu0 l5^2/4 (the record's c = 1/4), the modified region r1 < |r| < r2 with r2 = r_q(mu0) (inside x >= 1); the mass
    rises from position 2's mu2 to our mu(v) across 0 <= r <= r2 (on both sides in the mutant "same_mass")"""
    l5sq = mu0/L
    a = (0.25*mu0*l5sq)**0.25
    r2 = r_q(mu0, L)*(1.5 if "wide_region" in MUT else 1.0)
    r1 = 0.5*r2
    rr = np.linspace(-3.0, 3.0, 60001)
    w = r2 - r1; xs = (np.abs(rr) - r1)/w
    S, S1, S2 = 1 - P(xs), -P(xs, 1)*np.sign(rr)/w, -P(xs, 2)/w**2
    R2 = rr**2 + a**2*S
    R = np.sqrt(R2)
    Rp = (2*rr + a**2*S1)/(2*R)
    Rpp = (2 + a**2*S2)/(2*R) - Rp**2/R
    xt = rr/r2
    T, T1, T2 = P(xt), P(xt, 1)/r2*(rr > 0), P(xt, 2)/r2**2*(rr > 0)
    res = []
    for muv, muvd in ((mu0, 0.0), (mu0 + 0.5*dmu, 0.3), (mu0 + dmu, 0.0)):
        if "same_mass" in MUT:
            Mr, Mr1, Mr2, Mv = np.full_like(rr, muv), 0*rr, 0*rr, np.full_like(rr, muvd)
        else:
            Mr, Mr1, Mr2, Mv = mu2 + (muv - mu2)*T, (muv - mu2)*T1, (muv - mu2)*T2, muvd*T
        fv = 1 - Mr/R2
        gnn = -3*Rpp/R
        gll = -3*((Mr - R2)**2*Rpp - 2*R2*Mv*Rp)/(4*R**5)
        gmx = mix(Mr, Mr1, Mr2, Mv, R, Rp, Rpp)
        # every null direction a l + b n + c e (c^2 = 2ab): a^2 G(l,l) + b^2 G(n,n) + 2ab (G(l,n) + G(e,e)) >= 0
        tol = 1e-12*max(np.abs(gnn).max(), np.abs(gll).max(), np.abs(gmx).max())
        quad_ok = (gll >= -tol) & (gnn >= -tol) & (gmx >= -np.sqrt(np.maximum(gll, 0)*np.maximum(gnn, 0)) - tol)
        bad = ~quad_ok
        roots = rr[1:][np.diff((fv < 0).astype(int)) != 0]
        inner = (rr > roots.min() + 1e-3) & (rr < roots.max() - 1e-3) if roots.size else rr < -9
        far2, far1 = rr < -1.2*r2, rr > 1.2*r2
        res.append(dict(mu=muv, roots=roots, neg_inside=bool(np.all(fv[inner] < 0)),
                        nec_outside=float(np.abs(rr[bad]).max()) if bad.any() else 0.0, r2=r2, rq=r_q(mu0, L),
                        Rp_zeros=int(np.sum(np.diff((Rp < 0).astype(int)) != 0)),
                        pos2_classical=float(min(gll[far2].min(), gnn[far2].min(), gmx[far2].min(), 0.0)),
                        ours_dust=float(np.max(np.abs(gll[far1] - 1.5*muvd/rr[far1]**3)) + np.abs(gmx[far1]).max()
                                        + np.abs(gnn[far1]).max())))
    return res


def compute():
    a6 = s6()
    return dict(words=words(), s1=s1(), s2=s2(), s3=s3(), s3b=s3b(), s4=s4(), s6=a6, s7=core_model(a6["mix"]))


def checks(o):
    c = {}
    c["S0 words of 506 and 508"] = o["words"]
    a = o["s1"]
    c["S1 Ghosh-Dadhich: naked iff lam <= 1/27, X0 = 3"] = len(a["below"]) == 2 and not a["above"] and abs(a["X0"] - 3) < 1e-6
    a = o["s2"]
    c["S2 the core inside the apparent horizon iff mu > sqrt(72) l5^2"] = a["inside_above"] and a["outside_below"] and a["equal"] < 1e-12
    a = o["s3"]
    c["S3 no seed: the core seen from infinity at the record's spread"] = (all(x == "escapes" for v in a["rays"].values() for x in v)
                                                                          and 0.3 < a["sigma_c"] < 1.0 and a["D"] == D_REC)
    a = o["s3b"]
    c["S3b no seed, the record's own optimal shell: the core seen from infinity"] = (
        all(x == "escapes" for x in a["rays"].values()) and abs(a["sig_over_tau"] - 0.5) < 1e-6)
    a = o["s4"]
    c["S4 the seed mu0 >= sqrt(72) l5^2: every core ray trapped throughout"] = all(x == "trapped" for v in a.values() for x in v)
    a = o["s6"]
    c["S6 the accreting core's null energies, derived; our side 5D Vaidya dust"] = (
        a["forms"] and sp.simplify(a["ours"] - sp.Symbol("Mv")*sp.Rational(3, 2)/sp.Symbol("r", real=True)**3) == 0
        and sp.simplify(a["pos2"] + sp.Symbol("Mv")*sp.Rational(3, 2)/sp.Symbol("r", real=True)**3) == 0
        and a["mix_vac"] == 0)
    res = o["s7"]
    c["S7 null energy fails only inside x >= 1; none reaches position 2"] = all(
        q["nec_outside"] <= q["r2"]*1.0001 and q["r2"] <= q["rq"]*1.0001 and q["pos2_classical"] > -1e-9 and q["ours_dust"] < 1e-6
        for q in res)
    c["S8 two horizons only, one transition surface, through the accretion"] = all(
        q["roots"].size == 2 and q["neg_inside"] and q["Rp_zeros"] == 1 for q in res)
    return c


MUTANTS = {"no_seed": "no seed before the shell (S4: the core seen from infinity)",
           "short_spread": "the shell delivered in 0.2 r_h instead of the record's 28.5 (S3: the core hidden without a seed)",
           "same_mass": "the mass raised on both sides of the core (S7: negative energy in position 2's classical exterior)",
           "wide_region": "the modified region wider than x >= 1 (S7: null energy failing where the curvature is classical)"}


def report(o=None):
    o = o or compute()
    for k, v in checks(o).items():
        print("%-72s %s" % (k, "PASS" if v else "FAIL"))
    print("  S3 critical spread for a hidden core (no seed, mu_f/l5^2 = 7e40): sigma_t = %.3f r_h; the record's least: 28.5 r_h"
          % o["s3"]["sigma_c"])
    for q in o["s7"]:
        print("  S7/S8 mu = %.4f: horizons at r = %s; null energy fails out to |r| = %.4f (r2 = %.4f, r_q = %.4f); "
              "position 2's classical G(l,l) min %.2e; transition surfaces %d" % (q["mu"], np.round(q["roots"], 4),
                                                                                 q["nec_outside"], q["r2"], q["rq"],
                                                                                 q["pos2_classical"], q["Rp_zeros"]))
    return o


def selftest():
    o = compute()
    c = checks(o)
    report(o)
    print("%s: %d/%d" % (os.path.basename(__file__), sum(c.values()), len(c)))
    return all(c.values())


def mutants():
    caught = 0
    for m_, desc in MUTANTS.items():
        MUT.clear(); MUT.add(m_)
        try:
            c = checks(compute())
            failed = [k for k, v in c.items() if not v]
        except Exception as ex:
            failed = ["raised %s" % type(ex).__name__]
        caught += bool(failed)
        print("mutant %-14s %s  (%s)  failing: %s" % (m_, "caught" if failed else "MISSED", desc, "; ".join(failed)))
    MUT.clear()
    print("mutants: %d/%d" % (caught, len(MUTANTS)))
    return caught == len(MUTANTS)


if __name__ == "__main__":
    if "--mutants" in sys.argv:
        sys.exit(0 if mutants() else 1)
    sys.exit(0 if selftest() else 1)
