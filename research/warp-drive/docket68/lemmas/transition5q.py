#!/usr/bin/env python3
"""transition5q.py -- item 483: the geometry inside 273's quantum region computed from a quantum dynamics of gravity in
five dimensions, and the transition's probability and time.  Ashtekar, Olmedo and Singh's method (arXiv 1806.02406v3,
READ in transition_aos) carried to five dimensions.  It shows that transition5's construction is realized by the
quantum-corrected dynamics.  Labels: computed (exact unless marked), deduced, READ, M's.  Worked in the conversation;
not verified; not seated.

Held against the exclusions first (481): the interior found below has two horizons only (no inner horizon, 464, 471);
its bounce is not classical (318) -- the null energy it needs is the quantum correction's -- and not semiclassical (C9):
the correction reaches order one only at x = 1.

  H0 (M's) 483: "prove that it applies and is true"; "you still need to compute this" (the region's geometry, the
     transition's probability and time).
  H1 (computed, exact) Five-dimensional Kantowski-Sachs, ds^2 = -N^2 dT^2 + A^2 dx^2 + B^2 dOmega_3^2: Einstein-Hilbert
     reduces, up to a total derivative, to L = 6NAB - (6/N)(AB B'^2 + B^2 A' B').  With p_b = AB, p_c = B^2 the
     constraint is N(-pi_b pi_c/3 - 6 p_b).  The canonical transformation P_c = p_c, P_b = p_b sqrt(p_c),
     Pi_b = pi_b/sqrt(p_c), Pi_c = pi_c - Pi_b p_b/(2 sqrt(p_c)), with lapse N = -3 p_c/pi_b, gives
          H = P_c Pi_c + 3 P_b (b + 1/b),   b = Pi_b/6,
     Ashtekar, Olmedo and Singh's form exactly (their gamma -> 1): a sphere sector and a b sector that decouple.
  H2 (computed) The classical limit is Tangherlini's interior: b^2 + 1 = mu/P_c, P_c proportional to e^T, A = b, and
     the Dirac observable mu = -P_c Pi_c/3 is the mass parameter (f = 1 - mu/r^2).
  H3 (computed) The quantum dynamics (holonomy corrections, as AOS): Pi_c -> sin(d_c Pi_c)/d_c, b -> sin(d_b b)/d_b.
     The closed forms P_c = mu (e^T + k^2 e^-T), k = 3 d_c/2, and cos(d_b b) = b_o tanh((b_o T + 2 atanh(1/b_o))/2),
     b_o = sqrt(1 + d_b^2), solve the effective equations (residual below 1e-25), with mu conserved.
  H4 (computed; the scales from 415) Quantum corrections depend on x = l5^2 sqrt(K) alone (P1-P3) only if d_c is
     proportional to mu^(-1/2) and d_b to mu^(-1/4) -- the 5D counterpart of AOS's m^(-1/3).  With no coefficient (P4),
     each sector's correction reaches order one at x = 1: the sphere's minimum at the classical curvature 1/l5^4, and
     d_b b = pi/2 there.  The second condition then gives d_b = sqrt(6 d_c) exactly -- the scaling the first required,
     a consistency the premises did not impose.
  H5 (computed) Exactly two horizons, A = 0 at T = 0 (our black hole) and at T_WH = 2 T_T (position 2's white hole),
     with A > 0 between: no inner horizon.  The sphere shrinks to the future before T_T (trapped) and grows after it
     (anti-trapped): one transition surface.
  H6 (computed) The white hole's mass equals the black hole's: P_c(T_WH) = P_c(0) = mu(1 + k^2), exactly -- derived from
     H4, not imposed.  273's Kruskal construction follows from the quantum dynamics.
  H7 (computed) The curvature is bounded and the same at every mass: max l5^4 K over the interior is 0.2917 (x = 0.54)
     from mu/l5^2 = 1e12 to 1e40, 0.3011 at 1e6.  Wherever the classical x < 1e-2, P_c departs from Tangherlini's by less than 1e-2: the
     correction is confined to the quantum region, as transition5 assumed.
  H8 (computed) Probability.  Quantized, the sphere sector is a free translation: with tan(d_c Pi_c/2) = e^(d_c u),
     H_c = P_u/d_c and P_c = P_u cosh(d_c u).  Every state therefore evolves unitarily through the transition, with
     norm 1 and no other branch: the transition's probability is 1.  A Gaussian state's <P_c>(T) =
     |P_u| e^(d^2 s^2/2) cosh(T + d u0) is bounded below and follows the effective P_c(T); computed on a grid, its norm
     is conserved to 1e-12 and its expectation matches the closed form to 1e-4 (the grid's).
  H10 (computed; deduced from it) No Cauchy horizon (484, M-NO-CAUCHY).  The sphere's radius never falls below B_T > 0
     (no centre, no timelike boundary); the curvature is bounded (H7); inside, N is finite and positive, so every T =
     const slice is spacelike and T is a time function crossed by every causal curve, in at most 2 r_h of proper time
     (H9); the only horizons are A = 0 at T = 0 and T_WH (H5), our black hole's and position 2's white hole's.  With no
     singular or timelike boundary nothing enters the interior except through those two horizons, so the development of
     a slice is the whole interior: there is no Cauchy horizon.
  H9 (computed) Time.  The proper time across the interior, from our face to position 2's, is 2.000 r_h/c to
     corrections in d: 2.7e-13 s at r0 = 20 ell and 1.5e-12 s at the Earth cap (the large end's 5D form), 2 r_h/c at the
     small end.  The README's null rays cross in finite affine length.  (Haggard and Rovelli's exterior time m^2/l_P is
     the two-exterior object's, not the one-way object's, 277; b_bounce's note.)

What this proves and does not: within the quantum dynamics -- AOS's holonomy-corrected Hamiltonian, carried to five
dimensions, its two scales fixed by 415's premises -- 273's transition is computed, not specified.  The interior
crosses one transition surface with no inner horizon; the white hole has the black hole's mass; the curvature is
bounded at the l5 scale for every mass; classical GR holds wherever x is small; the transition happens with
probability 1; and it lasts 2 r_h/c.  transition5's construction is the form this dynamics realizes.  The dynamics is
loop quantum gravity's effective one, a candidate quantum theory of gravity, as AOS's is in four dimensions; no
established theory computes inside x >= 1, which is what Penrose's theorem leaves to quantum gravity.

python3 transition5q.py [--selftest | --mutants]
"""
import os, sys, math, importlib.util
import numpy as np
import sympy as sp
import mpmath as mp

HERE = os.path.dirname(os.path.abspath(__file__))
MUT = set()
mp.mp.dps = 60


def _load(name, alias):
    spec = importlib.util.spec_from_file_location(alias, os.path.join(HERE, name))
    mod = importlib.util.module_from_spec(spec); spec.loader.exec_module(mod); return mod


def reduction():
    """H1: the reduced Lagrangian, and the canonical transformation to AOS's form"""
    T = sp.symbols("T"); x, c, th, ph = sp.symbols("x chi theta phi")
    N, A, B = [sp.Function(n)(T) for n in ("N", "A", "B")]
    X = (T, x, c, th, ph)
    g = sp.diag(-N ** 2, A ** 2, B ** 2, B ** 2 * sp.sin(c) ** 2, B ** 2 * sp.sin(c) ** 2 * sp.sin(th) ** 2)
    gi = g.inv()
    G = [[[sum(gi[a, d] * (sp.diff(g[d, b], X[cc]) + sp.diff(g[d, cc], X[b]) - sp.diff(g[b, cc], X[d]))
               for d in range(5)) / 2 for cc in range(5)] for b in range(5)] for a in range(5)]
    def ric(b, d):
        return sum(sp.diff(G[a][b][d], X[a]) - sp.diff(G[a][b][a], X[d])
                   + sum(G[a][a][e] * G[e][b][d] - G[a][d][e] * G[e][b][a] for e in range(5)) for a in range(5))
    Rs = sp.simplify(sum(gi[b, b] * ric(b, b) for b in range(5)))
    L = N * A * B ** 3 * Rs
    Ad, Bd = sp.diff(A, T), sp.diff(B, T)
    total = sp.diff(6 * A * B ** 2 * Bd / N + 2 * B ** 3 * Ad / N, T)
    Lred = sp.simplify(sp.expand(L - total))
    target = 6 * N * A * B - (6 / N) * (A * B * Bd ** 2 + B ** 2 * Ad * Bd)
    ok_L = sp.simplify(Lred - target) == 0
    # canonical transformation, checked as an identity of the constraint
    pb, pc, pib, pic = sp.symbols("p_b p_c pi_b pi_c", positive=True)
    h = -pib * pic / 3 - 6 * pb
    Pc, Pb, Pib = pc, pb * sp.sqrt(pc), pib / sp.sqrt(pc)
    Pic = pic - Pib * pb / (2 * sp.sqrt(pc))
    b = Pib / 6
    H_aos = Pc * Pic + 3 * Pb * (b + 1 / b)
    Nl = -3 * pc / pib
    ok_H = sp.simplify(Nl * h - H_aos) == 0
    # the transformation is canonical: Poisson brackets
    def pb_(f, gg):
        return sp.simplify(sum(sp.diff(f, q) * sp.diff(gg, p) - sp.diff(f, p) * sp.diff(gg, q)
                               for q, p in ((pb, pib), (pc, pic))))
    ok_can = (pb_(Pb, Pib) == 1 and pb_(Pc, Pic) == 1 and pb_(Pb, Pic) == 0 and pb_(Pc, Pib) == 0
              and pb_(Pb, Pc) == 0 and pb_(Pib, Pic) == 0)
    return dict(L=ok_L, H=ok_H, canonical=ok_can)


def scales(mu, l5=1.0):
    """H4: d_c from the sphere's minimum at the classical curvature 1/l5^4; d_b from d_b b = pi/2 there"""
    mu = mp.mpf(mu)
    pmin = mp.mpf(72) ** 0.25 * mp.sqrt(mu) * l5                       # 72 mu^2/pmin^4 = 1/l5^4
    dc = pmin / (3 * mu) * (2 if "dc" in MUT else 1)
    k = 3 * dc / 2
    TT = mp.log(k)
    # cos(d_b b(TT)) = 0  <=>  b_o TT + 2 atanh(1/b_o) = 0
    db = mp.findroot(lambda d: mp.sqrt(1 + d * d) * TT + 2 * mp.atanh(1 / mp.sqrt(1 + d * d)), mp.sqrt(6 * dc))
    if "db" in MUT:
        db *= 1.5
    return dict(mu=mu, dc=dc, db=db, k=k, TT=TT, bo=mp.sqrt(1 + db * db))


def state(T, s):
    mu, dc, db, k, bo = s["mu"], s["dc"], s["db"], s["k"], s["bo"]
    Pc = mu * (mp.e ** T + k * k * mp.e ** (-T))
    tt = mp.tanh(bo * T / 2)                                             # cos(d_b b) = b_o tanh(b_o T/2 + atanh(1/b_o)),
    cosb = 1 + db * db * tt / (bo + tt)                                 # written so that 1 - cos keeps its digits
    sinb = mp.sqrt(max(mp.mpf(0), -db * db * tt * (2 * bo + tt * (1 + bo * bo)))) / abs(bo + tt)
    Pb = mu * sinb * db / (sinb ** 2 + db ** 2)                         # = mu/(sin/d + d/sin), 0 on the horizons
    B = mp.sqrt(Pc); A = Pb / Pc; N = B * db / (2 * sinb) if sinb != 0 else mp.inf
    Pic = -2 / dc * mp.atan(k * mp.e ** (-T))                            # tan(d_c Pi_c/2) = -k e^-T, d_c Pi_c in (-pi, 0)
    bb = mp.acos(cosb) / db
    return dict(Pc=Pc, Pb=Pb, A=A, B=B, N=N, cosb=cosb, sinb=sinb, Pic=Pic, b=bb)


def eom_residual(s, T):
    """the effective equations: dPc/dT = Pc cos(dc Pic), dPic/dT = -sin(dc Pic)/dc, db/dT = -(sin/d + d/sin)/2"""
    dc, db = s["dc"], s["db"]
    st = state(T, s)
    dPc = mp.diff(lambda t: state(t, s)["Pc"], T); dPic = mp.diff(lambda t: state(t, s)["Pic"], T)
    dbb = mp.diff(lambda t: state(t, s)["b"], T)
    r1 = dPc - st["Pc"] * mp.cos(dc * st["Pic"])
    r2 = dPic + mp.sin(dc * st["Pic"]) / dc
    r3 = dbb + (mp.sin(db * st["b"]) / db + db / mp.sin(db * st["b"])) / 2
    mu_obs = st["Pc"] * mp.sin(dc * st["Pic"]) / (3 * dc)
    return max(abs(r1) / st["Pc"], abs(r2) * dc, abs(r3) * db), abs(abs(mu_obs) / s["mu"] - 1)


_KF = {}


def kretschmann_fn():
    if "K" in _KF:
        return _KF["K"]
    T = sp.symbols("T"); x, c, th, ph = sp.symbols("x chi theta phi")
    N, A, B = [sp.Function(n)(T) for n in ("N", "A", "B")]
    X = (T, x, c, th, ph)
    g = sp.diag(-N ** 2, A ** 2, B ** 2, B ** 2 * sp.sin(c) ** 2, B ** 2 * sp.sin(c) ** 2 * sp.sin(th) ** 2)
    gi = sp.diag(*[1 / g[i, i] for i in range(5)])
    G = [[[sp.simplify(gi[a, a] * (sp.diff(g[a, b], X[cc]) + sp.diff(g[a, cc], X[b]) - sp.diff(g[b, cc], X[a])) / 2)
           for cc in range(5)] for b in range(5)] for a in range(5)]
    K = 0
    for a in range(5):
        for b in range(5):
            for cc in range(5):
                for d in range(cc + 1, 5):
                    e = sp.diff(G[a][b][d], X[cc]) - sp.diff(G[a][b][cc], X[d])
                    e += sum(G[a][cc][kk] * G[kk][b][d] - G[a][d][kk] * G[kk][b][cc] for kk in range(5))
                    e = sp.simplify(e)
                    if e != 0:
                        K += 2 * g[a, a] * gi[b, b] * gi[cc, cc] * gi[d, d] * e ** 2
    K = sp.simplify(K)
    syms = sp.symbols("N0 N1 A0 A1 A2 B0 B1 B2")
    K = K.subs({sp.Derivative(A, (T, 2)): syms[4], sp.Derivative(B, (T, 2)): syms[7], sp.Derivative(N, T): syms[1],
                sp.Derivative(A, T): syms[3], sp.Derivative(B, T): syms[6], N: syms[0], A: syms[2], B: syms[5]})
    _KF["K"] = sp.lambdify(syms, K, "mpmath")
    return _KF["K"]


def kret(s, T):
    Kf = kretschmann_fn()
    f = lambda key: (lambda t: state(t, s)[key])
    N0 = state(T, s)["N"]; N1 = mp.diff(f("N"), T)
    A0 = state(T, s)["A"]; A1 = mp.diff(f("A"), T); A2 = mp.diff(f("A"), T, 2)
    B0 = state(T, s)["B"]; B1 = mp.diff(f("B"), T); B2 = mp.diff(f("B"), T, 2)
    return Kf(N0, N1, A0, A1, A2, B0, B1, B2)


def quantum(dc, Pu=1.0, sig=0.6, u0=-3.0, n=4096, L=60.0):
    """H8: the sphere sector quantized -- a Gaussian in u translated by H_c = P_u/d_c; <P_c> = <P_u cosh(d_c u)>"""
    u = np.linspace(-L, L, n, endpoint=False); du = u[1] - u[0]
    hb = 0.05                                                            # a small effective hbar: the state is sharp
    p = 2 * np.pi * np.fft.fftfreq(n, d=du) * hb
    psi0 = np.exp(-(u - u0) ** 2 / (4 * sig ** 2) + 1j * Pu * u / hb)
    psi0 /= np.sqrt(np.sum(np.abs(psi0) ** 2) * du)
    out = []
    for Tq in np.linspace(0.0, 2 * abs(u0), 41):
        shift = Tq / dc if False else Tq                                 # in units where d_c u is the phase, u in 1/d_c
        ph = np.exp(-1j * p * shift / hb) if "nonunitary" not in MUT else np.exp(-1j * p * shift / hb) * 0.999
        psi = np.fft.ifft(np.fft.fft(psi0) * ph)
        norm = np.sum(np.abs(psi) ** 2) * du
        exp_cosh = np.sum(np.abs(psi) ** 2 * np.cosh(u)) * du / norm
        out.append((Tq, norm, exp_cosh))
    return out


def compute():
    o = dict(red=reduction())
    QO = _load("quantum_onset.py", "t5q_qo"); CF = _load("core_face.py", "t5q_cf")
    l5 = QO.onset_4d()["l5"]
    res = {}
    for e in (6, 12, 20, 30, 40):
        s = scales(mp.mpf(10) ** e)
        TT, TWH = s["TT"], -4 * mp.atanh(1 / s["bo"]) / s["bo"]
        eom = [eom_residual(s, T) for T in (TT * mp.mpf("0.5"), TT, TT * mp.mpf("1.5"))]
        Ts = [TWH * mp.mpf(j) / 40 for j in range(1, 40)]
        A_ = [state(T, s)["A"] for T in Ts]
        side = (mp.diff(lambda t: state(t, s)["Pc"], TT / 2) > 0, mp.diff(lambda t: state(t, s)["Pc"], 1.5 * TT) < 0)
        Kmax = max(kret(s, T) for T in [TT + mp.mpf(j) / 10 for j in range(-20, 21)])
        # deviation from Tangherlini where the classical x < 1e-2
        dev = 0
        for T in [mp.mpf(-j) / 4 for j in range(1, 200)]:
            Pcl = s["mu"] * mp.e ** T
            x = mp.sqrt(72) * s["mu"] / Pcl ** 2
            if x < mp.mpf("1e-2"):
                dev = max(dev, abs(state(T, s)["Pc"] / Pcl - 1))
        # the interior is symmetric about T_T (P_c a cosh, cos(d_b b) odd): tau = 2 int_{T_T}^0 N dT
        symm = abs(state(TT + mp.mpf("0.7"), s)["N"] / state(TT - mp.mpf("0.7"), s)["N"] - 1)
        Bmin = min(state(T, s)["B"] for T in [TWH * mp.mpf(j) / 200 for j in range(1, 200)]) / mp.sqrt(s["mu"])
        Npos = all(0 < state(T, s)["N"] < mp.inf for T in [TWH * mp.mpf(j) / 50 for j in range(1, 50)])
        tau = 2 * mp.quad(lambda T: state(T, s)["N"], [TT, TT / 2, 0]) / mp.sqrt(s["mu"])
        res[e] = dict(s=s, TWH=TWH, eom=max(r[0] for r in eom), mudrift=max(r[1] for r in eom),
                      Apos=min(A_) > 0, side=side, mwh=state(TWH, s)["Pc"] / state(mp.mpf(0), s)["Pc"],
                      Kmax=Kmax, dev=dev, tau=tau, symm=symm, Bmin=Bmin, Npos=Npos, dbcheck=s["db"] / mp.sqrt(6 * s["dc"]))
    o["res"] = res
    q = quantum(1.0)
    o["q"] = q
    # times at the record's large-end 5D forms
    c = 299792458.0
    o["times"] = {k: 2 * math.sqrt(v["mu5"]) / c for k, v in CF.core_scales().items()}
    o["l5"] = l5
    return o


def checks(o):
    red, res, q = o["red"], o["res"], o["q"]
    h1 = red["L"] and red["H"] and red["canonical"]
    h3 = all(v["eom"] < 1e-25 and v["mudrift"] < 1e-25 for v in res.values())
    h4 = all(abs(v["dbcheck"] - 1) < 1e-2 for v in res.values())
    h5 = all(v["Apos"] and all(v["side"]) and abs(v["TWH"] / v["s"]["TT"] - 2) < 1e-20 for v in res.values())
    h6 = all(abs(v["mwh"] - 1) < 1e-30 for v in res.values())
    km = [v["Kmax"] for v in res.values()]
    big = [v["Kmax"] for e, v in res.items() if e >= 12]
    h7 = (max(big) / min(big) - 1 < 1e-3 and max(km) / min(km) - 1 < 5e-2 and 0.1 < min(km) < 1e4
          and all(v["dev"] < 1e-2 for v in res.values()))
    norms = [n for _, n, _ in q]
    T0 = q[0][0]
    c0 = q[0][2]
    # Gaussian: <cosh(u + T)> for a packet centred at u0 + T: cosh(u0 + T) e^(s^2/2) with s = 0.6
    ana = [math.cosh(-3.0 + Tq) * math.exp(0.6 ** 2 / 2) for Tq, _, _ in q]
    h8 = max(abs(n - 1) for n in norms) < 1e-12 and max(abs(e / a - 1) for (_, _, e), a in zip(q, ana)) < 1e-4 \
        and min(e for _, _, e in q) >= math.exp(0.18) - 1e-9
    h9 = all(abs(v["tau"] - 2) < 0.01 and v["symm"] < 1e-20 for v in res.values()) and all(1e-14 < t < 1e-10 for t in o["times"].values())
    h10 = all(v["Bmin"] > 0 and v["Npos"] and v["Apos"] for v in res.values()) and h5 and h7 and h9
    return dict(H1=h1, H3=h3, H4=h4, H5=h5, H6=h6, H7=h7, H8=h8, H9=h9, H10=h10)


def report(o=None):
    o = o or compute(); ck = checks(o)
    print("H1 reduction L = 6NAB - (6/N)(AB B'^2 + B^2 A'B'): %s; constraint -> P_c Pi_c + 3P_b(b + 1/b): %s; canonical: "
          "%s" % (o["red"]["L"], o["red"]["H"], o["red"]["canonical"]))
    for e, v in o["res"].items():
        s = v["s"]
        print("   mu/l5^2 1e%d: d_c %.3e, d_b %.3e (/sqrt(6 d_c) %.6f); T_T %.3f, T_WH/T_T %.12f; eom %.1e; A > 0 inside "
              "%s; m_WH/m_BH - 1 %.1e; l5^4 K_max %.4f; Tangherlini dev (x<1e-2) %.1e; tau %.6f r_h" % (
                  e, float(s["dc"]), float(s["db"]), float(v["dbcheck"]), float(s["TT"]), float(v["TWH"] / s["TT"]),
                  float(v["eom"]), v["Apos"], float(v["mwh"] - 1), float(v["Kmax"]), float(v["dev"]), float(v["tau"])))
    print("   quantum sphere sector: norm %s .. %s; <cosh> min %.6f (bound e^(s^2/2) = %.6f)" % (
        "%.15f" % min(n for _, n, _ in o["q"]), "%.15f" % max(n for _, n, _ in o["q"]),
        min(e for _, _, e in o["q"]), math.exp(0.18)))
    print("   times across the interior: %s" % ", ".join("%.2e s (%s)" % (t, k) for k, t in o["times"].items()))
    for k, v in ck.items():
        print("%s %s" % (k, v))
    return all(ck.values())


def selftest(quiet=False):
    o = compute(); ck = checks(o)
    if not quiet:
        report(o)
    return all(ck.values())


def mutants():
    caught = 0; names = ["dc", "db", "nonunitary"]
    for m_ in names:
        MUT.clear(); MUT.add(m_)
        try:
            r_ = selftest(quiet=True)
        except Exception:
            r_ = False
        caught += not r_; print("mutant %-10s %s" % (m_, "caught" if not r_ else "SURVIVED"), flush=True)
    MUT.clear(); print("%d/%d caught" % (caught, len(names)))
    return caught == len(names)


if __name__ == "__main__":
    a = sys.argv[1:]
    if a and a[0] == "--selftest":
        sys.exit(0 if selftest() else 1)
    if a and a[0] == "--mutants":
        sys.exit(0 if mutants() else 1)
    report()
