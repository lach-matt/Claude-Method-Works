#!/usr/bin/env python3
"""stage0two5.py -- FAMILIES5 section 4 (a)-(d): Stage 0 of the two-phase ansatz in the class (computed, exact, sympy).

The background is a general round double-null metric in five dimensions,
    g0 = -2 e^(2 sig(u,v)) du dv + R(u,v)^2 (dth^2 + c^2 dphi1^2 + s^2 dphi2^2),   c = cos th, s = sin th,
with sig and R arbitrary, so no field equation for g0 is assumed. The metric is g = g0 + lam (W_in + W_out), with
    W_in  = R^2 diag(-2(P1 + P2), 2 c^2 P1, 2 s^2 P2)[a(u,v), s1] + chi dv dv,     s1 = v/lam,
    W_out = R^2 diag(-2(Q1 + Q2), 2 c^2 Q1, 2 s^2 Q2)[b(u,v), s2] + chi' du du,    s2 = u/lam,
P1 = a H (2 c^2 cos s1 - s^2 sin s1)/3, P2 = a H (2 s^2 sin s1 - c^2 cos s1)/3 (lead5.py's polarisations), Q the same
with b and s2, H = H(th) free, and chi, chi' free second harmonics in s1, s2. The amplitudes are taken as
a = alpha(v) R^(-3/2) and b = beta(u) R^(-3/2), alpha and beta free: the transports that T3 needs (a mutant drops each).
Ric^H is lead5.py's reduced Ricci tensor in the wave-map gauge relative to g0, Ric - (1/2)(g D^ D + (g D^ D)^T) with
D = g^ab (Gamma - Gamma0)_ab, expanded in lam with d_v -> d_v + lam^-1 F1 and d_u -> d_u + lam^-1 F2, F_k = d/ds_k.
The fast variables are carried as z_k = exp(i s_k), F_k = i z_k d/dz_k, so the harmonic (n1, n2) of a coefficient is
its coefficient of z1^n1 z2^n2. The lam^-1 and lam^0 coefficients are assembled order by order.

  T1 R^(-1) = 0 in every component.
  T2 The (0,0) harmonic of R^(0) is Ric(g0) - K_in dv^2 - K_out du^2, with no other component: each family has its
     own null stress, K_in from family in alone and K_out from family out alone, and they do not interact in the mean.
     With the record's H = sqrt(2/(1 + cos^2 2th)), K_in R^3 does not depend on th: the stress is round.
  T3 Write a = alpha(v) R^(-3/2) and b = beta(u) R^(-3/2): the transport along ell_in = g0^-1 dv, proportional to d_u,
     and along ell_out, proportional to d_v. Then the harmonics (n, 0), n != 0, of R^(0) vanish except in vv at n = +-2,
     and (0, n) except in uu at n = +-2: lead5.py's L3 for each family. chi and chi' enter them only through their
     transports along d_u and d_v (L4).
  T4 The harmonics (n1, n2), n1 n2 != 0, of R^(0) are present (the cross terms do not vanish). A term lam^2 q E in g,
     q any function of (u, v, th, s1, s2) and E any of the 15 symmetric basis tensors, adds exactly
     -g0^uv F1 F2 q E = e^(-2 sig) F1 F2 q E to R^(0). Its symbol at (n1, n2) is -e^(-2 sig) n1 n2, which is
     non-zero, so ghat_2 solves every mixed harmonic by division.
  T5 With alpha = beta = 0, the vv (+-2, 0) harmonics are +-2i e^(-2 sig) R^(-3/2) d_u(R^(3/2) chi_+-2) and the uu
     (0, +-2) ones +-2i e^(-2 sig) R^(-3/2) d_v(R^(3/2) chi'_+-2): chi and chi' enter only by their transports (L4).
  T6 The gauge 1-form D = g^ab (Gamma - Gamma0)_ab vanishes at order lam^0 (lead5.py's L5 in this form: each W is
     transverse to its own generator and traceless).
T1 holds for any W_in(s1) + W_out(s2), as g0^uu = g0^vv = 0, and that the families do not meet in the mean is harmonic
bookkeeping; both are recorded, not tested against a mutant.
python3 checks/stage0two5.py [--selftest | --mutants]
"""
import sys
import time

import sympy as sp

MUT = set()
MUTANTS = {"no_transport": "a = alpha(v) without R^(-3/2): T3 fails",
           "out_no_transport": "b = beta(u) without R^(-3/2): T3 fails",
           "not_reduced": "Ric in place of Ric^H (the gauge term dropped): T3 fails",
           "in_phase": "the two polarisations of family in in phase: its mean stress is not round (T2)",
           "chi_dvdu": "chi placed on dv du in place of dv dv: T3 or T5 fails",
           "principal_no_gauge": "the principal part without the gauge term: T4 fails"}

u, v, th, p1, p2 = sp.symbols("u v theta phi1 phi2", real=True)
z1, z2 = sp.symbols("z1 z2")
X = [u, v, th, p1, p2]
N = 5
sig = sp.Function("sigma")(u, v)
Rf = sp.Function("R")(u, v)
Hf = sp.Function("H")(th)
alpha = sp.Function("alpha")(v)
beta = sp.Function("beta")(u)
C, S = sp.cos(th), sp.sin(th)
xi2, xi2b = sp.Function("x2")(u, v, th), sp.Function("y2")(u, v, th)
et2, et2b = sp.Function("xx2")(u, v, th), sp.Function("yy2")(u, v, th)
H_REC = sp.sqrt(2/(1 + sp.cos(2*th)**2))
SHIFT = 6
NAMES = ["u", "v", "th", "p1", "p2"]


def ex(e):
    return sp.expand(e)


def slow(e, k):
    return sp.diff(e, X[k])


def fast(e, k):
    if k == 1:
        return sp.I*z1*sp.diff(e, z1)
    if k == 0:
        return sp.I*z2*sp.diff(e, z2)
    return 0


def background():
    g = sp.diag(0, 0, Rf**2, Rf**2*C**2, Rf**2*S**2)
    g[0, 1] = g[1, 0] = -sp.exp(2*sig)
    gi = sp.diag(0, 0, 1/Rf**2, 1/(Rf**2*C**2), 1/(Rf**2*S**2))
    gi[0, 1] = gi[1, 0] = -sp.exp(-2*sig)
    return g, gi


def tt(amp, z, in_phase=False):
    co, si = (z + 1/z)/2, (z - 1/z)/(2*sp.I)
    if in_phase:
        si = co
    q1 = amp*Hf*(2*C**2*co - S**2*si)/3
    q2 = amp*Hf*(2*S**2*si - C**2*co)/3
    W = sp.zeros(N)
    W[2, 2], W[3, 3], W[4, 4] = -2*Rf**2*(q1 + q2), 2*Rf**2*C**2*q1, 2*Rf**2*S**2*q2
    return W


def amplitudes():
    a = alpha if "no_transport" in MUT else alpha*Rf**sp.Rational(-3, 2)
    b = beta if "out_no_transport" in MUT else beta*Rf**sp.Rational(-3, 2)
    return a, b


def waves():
    a, b = amplitudes()
    W = tt(a, z1, "in_phase" in MUT) + tt(b, z2)
    if "chi_dvdu" in MUT:
        W[0, 1] += xi2*z1**2 + xi2b/z1**2
        W[1, 0] += xi2*z1**2 + xi2b/z1**2
    else:
        W[1, 1] += xi2*z1**2 + xi2b/z1**2
    W[0, 0] += et2*z2**2 + et2b/z2**2
    return W


def gamma_of(gi, dg):
    """Gamma^a_bc = (1/2) gi^ad (dg_dbc + dg_dcb - dg_bcd), dg[d][b][c] = d_c g_db"""
    return [[[ex(sum(gi[a, d]*(dg[d][b][c] + dg[d][c][b] - dg[b][c][d]) for d in range(N))/2) for c in range(N)]
             for b in range(N)] for a in range(N)]


def ricci_orders(W):
    """(R^(-1), R^(0)) of Ric^H(g0 + lam W), assembled order by order"""
    g0, g0i = background()
    Wu = (g0i*W*g0i).applyfunc(ex)
    dg0 = [[[slow(g0[d, b], c) for c in range(N)] for b in range(N)] for d in range(N)]
    A0 = [[[dg0[d][b][c] + fast(W[d, b], c) for c in range(N)] for b in range(N)] for d in range(N)]
    A1 = [[[slow(W[d, b], c) for c in range(N)] for b in range(N)] for d in range(N)]
    Gh = gamma_of(g0i, dg0)
    G0 = gamma_of(g0i, A0)
    t1 = gamma_of(g0i, A1)
    t2 = gamma_of(Wu, A0)
    G1 = [[[ex(t1[a][b][c] - t2[a][b][c]) for c in range(N)] for b in range(N)] for a in range(N)]
    dG = [[[ex(G0[r][a][b] - Gh[r][a][b]) for b in range(N)] for a in range(N)] for r in range(N)]
    D0 = [ex(sum(g0i[a, b]*dG[r][a][b] for a in range(N) for b in range(N))) for r in range(N)]
    D1 = [ex(sum(g0i[a, b]*G1[r][a][b] - Wu[a, b]*dG[r][a][b] for a in range(N) for b in range(N)))
          for r in range(N)]
    out = {}
    for b in range(N):
        for c in range(b, N):
            m1 = sum(fast(G0[a][b][c], a) - fast(G0[a][b][a], c) for a in range(N))
            z0 = sum(slow(G0[a][b][c], a) - slow(G0[a][b][a], c) + fast(G1[a][b][c], a) - fast(G1[a][b][a], c)
                     for a in range(N))
            z0 += sum(G0[a][a][d]*G0[d][b][c] - G0[a][c][d]*G0[d][b][a] for a in range(N) for d in range(N))
            if "not_reduced" not in MUT:
                for (p, q) in ((b, c), (c, b)):
                    m1 -= sum(g0[p, r]*fast(D0[r], q) for r in range(N))/2
                    z0 -= sum(g0[p, r]*(slow(D0[r], q) + fast(D1[r], q) + sum(Gh[r][q][s]*D0[s] for s in range(N)))
                              + W[p, r]*fast(D0[r], q) for r in range(N))/2
            out[(b, c)] = (ex(m1), ex(z0))
    out["D0"] = D0
    return out


def background_ricci():
    g0, g0i = background()
    dg0 = [[[slow(g0[d, b], c) for c in range(N)] for b in range(N)] for d in range(N)]
    Gh = gamma_of(g0i, dg0)
    out = {}
    for b in range(N):
        for c in range(b, N):
            e = sum(slow(Gh[a][b][c], a) - slow(Gh[a][b][a], c) for a in range(N))
            e += sum(Gh[a][a][d]*Gh[d][b][c] - Gh[a][c][d]*Gh[d][b][a] for a in range(N) for d in range(N))
            out[(b, c)] = ex(e)
    return out


def principal(Q):
    """the lam^0 coefficient of Ric^H(g0 + lam^2 Q) - Ric(g0), the only terms with two fast derivatives"""
    g0, g0i = background()
    A = [[[fast(Q[d, b], c) for c in range(N)] for b in range(N)] for d in range(N)]
    G1 = gamma_of(g0i, A)
    D1 = [ex(sum(g0i[a, b]*G1[r][a][b] for a in range(N) for b in range(N))) for r in range(N)]
    out = {}
    for b in range(N):
        for c in range(b, N):
            e = sum(fast(G1[a][b][c], a) - fast(G1[a][b][a], c) for a in range(N))
            if "principal_no_gauge" not in MUT:
                e -= sum(g0[b, r]*fast(D1[r], c) + g0[c, r]*fast(D1[r], b) for r in range(N))/2
            out[(b, c)] = ex(e)
    return out


def harmonics(e):
    e = ex(e*z1**SHIFT*z2**SHIFT)
    if e == 0:
        return {}
    return {(i - SHIFT, j - SHIFT): cf for (i, j), cf in sp.Poly(e, z1, z2).as_dict().items()}


def zero(e):
    e = ex(e)
    return e == 0 or sp.simplify(e) == 0


def run(verbose=True):
    t0 = time.time()
    ok = {}
    out = ricci_orders(waves())
    if verbose:
        print("  expansion assembled (%.0fs)" % (time.time() - t0), flush=True)
    ok["T1"] = all(zero(out[k][0]) for k in out if k != "D0")
    ok["T6"] = all(zero(e) for e in out["D0"])
    ric0 = background_ricci()
    t2, t3, t4a = True, True, False
    Kin = Kout = 0
    for k in sorted(kk for kk in out if kk != "D0"):
        Hm = harmonics(out[k][1])
        mean = ex(Hm.get((0, 0), 0) - ric0[k])
        if k == (1, 1):
            Kin = -mean
        elif k == (0, 0):
            Kout = -mean
        elif not zero(mean):
            t2 = False
            if verbose:
                print("  T2: mean in %s%s nonzero" % (NAMES[k[0]], NAMES[k[1]]))
        for (n1, n2), cf in Hm.items():
            if (n1, n2) == (0, 0):
                continue
            if n1*n2 != 0:
                t4a = t4a or not zero(cf)
                continue
            allowed = (k == (1, 1) and n2 == 0 and abs(n1) == 2) or (k == (0, 0) and n1 == 0 and abs(n2) == 2)
            if not allowed and not zero(cf):
                t3 = False
                if verbose:
                    print("  T3: harmonic (%d,%d) in %s%s nonzero" % (n1, n2, NAMES[k[0]], NAMES[k[1]]))
    Kin, Kout = sp.simplify(Kin), sp.simplify(Kout)
    t2 = t2 and not Kin.has(beta) and not Kin.has(et2) and not Kout.has(alpha) and not Kout.has(xi2)
    rin = sp.simplify((Kin*Rf**3).subs(Hf, H_REC).doit())
    rout = sp.simplify((Kout*Rf**3).subs(Hf, H_REC).doit())
    t2 = t2 and not rin.has(th) and not rout.has(th) and rin != 0 and rout != 0
    ok["T2"] = t2
    ok["T3"] = t3
    if verbose:
        print("  K_in  =", sp.factor(Kin))
        print("  K_out =", sp.factor(Kout))
        print("  with the record's H: K_in R^3 =", rin, "; K_out R^3 =", rout)
        vv = harmonics(out[(1, 1)][1]).get((2, 0), 0)
        print("  vv (2,0) harmonic:", sp.factor(vv))
    t4b = True
    q = sp.Function("q")(u, v, th, z1, z2)
    for i in range(N):
        for j in range(i, N):
            Q = sp.zeros(N)
            Q[i, j] = Q[j, i] = q
            pr = principal(Q)
            ff = sp.I*z1*sp.diff(sp.I*z2*sp.diff(q, z2), z1)
            for k in pr:
                if not zero(pr[k] - sp.exp(-2*sig)*ff*(Q[k[0], k[1]]/q)):
                    t4b = False
                    if verbose:
                        print("  T4: E = %s%s, component %s%s" % (NAMES[i], NAMES[j], NAMES[k[0]], NAMES[k[1]]))
    ok["T4"] = t4a and t4b
    t5 = True
    for k, n, chi_, d in (((1, 1), (2, 0), xi2, u), ((1, 1), (-2, 0), xi2b, u), ((0, 0), (0, 2), et2, v),
                          ((0, 0), (0, -2), et2b, v)):
        sgn = 1 if sum(n) > 0 else -1
        cf = harmonics(out[k][1]).get(n, 0).subs({alpha: 0, beta: 0}).doit()
        expect = sgn*2*sp.I*sp.exp(-2*sig)*Rf**sp.Rational(-3, 2)*sp.diff(Rf**sp.Rational(3, 2)*chi_, d)
        if not zero(cf - expect):
            t5 = False
            if verbose:
                print("  T5: %s%s %s" % (NAMES[k[0]], NAMES[k[1]], n))
    ok["T5"] = t5
    if verbose:
        print("  (%.0fs)" % (time.time() - t0), flush=True)
    return ok


def main():
    if "--mutants" in sys.argv:
        bad = 0
        for m, why in MUTANTS.items():
            MUT.clear()
            MUT.add(m)
            ok = run(verbose=False)
            caught = not all(ok.values())
            print("mutant %-13s %s  (%s)" % (m, "caught" if caught else "NOT CAUGHT", why), flush=True)
            bad += not caught
        sys.exit(1 if bad else 0)
    ok = run()
    for k, val in ok.items():
        print(k, "PASS" if val else "FAIL", flush=True)
    if "--selftest" in sys.argv:
        sys.exit(0 if all(ok.values()) else 1)


if __name__ == "__main__":
    main()
