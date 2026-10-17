#!/usr/bin/env python3
"""p3_double_null.py -- item 464: P3 by a double-null evolution.  The magnetic corridor's hole (462, 463) evolved inward
from inside its horizon, to answer P3: is there a regular inner horizon r- on the plane?  M (464): "Still waiting from
last turn: approval to build P3's next attempt as a double-null evolution. - approved. Continue".
Labels: READ (quoted), computed, deduced.  Worked in the conversation; not verified; not seated.  2026-10-17.

The system.  The bulk is vacuum with Lambda_5 (R_ab = -4 g_ab, ell = 1).  The plane's magnetic field enters only through
Israel's condition (p3_work/p3m.py), kappa = 0.2908 from P2's member.  The metric is taken in conformal gauge on the
quotient, with t the Killing direction (spacelike inside the horizon):
    g5 = e^{-A} [e^{2S} (-dtau^2 + dchi^2) + r^2 dOmega^2] + e^{2A} dt^2,
which is the four-dimensional Einstein frame of the reduction along t.  chi runs from the axis (chi = 0, where the S^2
shrinks) to the plane (chi = 1).  The three wave equations (p3_work/dn/dneqE.py, derived symbolically) are
    S_tt = S_xx - (3/4)(A_t^2 - A_x^2) + 2 m e^{2S}/r^3
    A_tt = A_xx + (2/r)(A_x r_x - A_t r_t) - 4 e^{2S-A}
    r_tt = r_xx - 2 m e^{2S}/r^2 - 6 r e^{2S-A},
with m the Misner-Sharp mass, m_x = (3 r^2/8)[e^{-2S}(r_x (A_t^2 + A_x^2) - 2 A_t A_x r_t) - 8 r_x e^{-A}], the two
null constraints reduced to first order.  m is integrated from the axis on every slice.
  - The plane takes Israel's rows as Neumann data: e^-sig A_chi = e^-sig sig_chi = 1 - q and
    e^-sig (log R)_chi = 1 + q, with q = kappa/R^4, sig = S - A/2 and R = e^{-A/2} r.
  - The initial slice is the static solve's s = s0 inside the horizon (p3_work/dn/dninit.py), with chi set by proper
    length so that the plane's rows hold at the corner.
  - Past a curvature singularity the evolution continues by excision (dnx.py).  This is valid only while the cut moves
    faster than light, which is checked.

  D0 (computed) The equations hold on exact AdS5 in this chart: sig = -log cosh tau, A = sig + log cosh chi,
     R = sinh chi/cosh tau.  The second derivatives agree, m_x agrees, and K = 40.
  D1 (computed) The scheme converges at second order on exact AdS5, at N = 20, 40, 80.
  D2 (computed) Why the Einstein frame is needed.  The first formulation, R = chi e^{sig+psi}, is unstable at the axis
     on the same exact data: sig's equation carries sig_xx - (2/chi) sig_x, a radial operator of dimension -1.  The
     instability's growth rate scales as 1/h, so the blow-up time halves with each refinement.
  D3 (computed) The plane's Israel rows, read off the static slice, give 1 -/+ kappa/R^4 to 1e-5.  This fixes their
     signs.
  D4 (computed) The initial data satisfy both constraints.  The interior violation falls with N to 5e-4, the static
     solve's own residual at s0 = -0.05 (7e-4).
  D5 (computed) The evolution against the static DeTurck solve, where both exist.  The plane's N(R), with N = g_tt,
     agrees to the static solve's own residual over s in [-0.28, -0.07].
  D6 (computed) The uncharged control crunches on the plane, as Schwarzschild's interior does: R -> 0 and N -> infinity
     with K -> infinity.
  D7 (computed) The charged hole.
       - On the plane N rises to a maximum of 4.09 at R = 0.62 ell, then falls.  This is the charge's turn, as in
         Reissner-Nordstrom.
       - A spacelike curvature singularity forms in the bulk near the axis and sweeps to the plane.
       - It arrives where N -> 0, at R = 0.30 ell.  K diverges there as N^-1.4.
       - So there is no regular inner horizon.  The curvature diverges where it would stand.
  D8 (computed) The plane's N and R converge at second order (N = 100, 200, 400) up to the end.
  D9 (computed) The excision is valid: the cut moves faster than light, and the plane is independent of where it is
     placed.
  D10 (computed) The result does not depend on the start slice: s0 = -0.05 and s0 = -0.15 give the same N(R) and K(R)
      on the plane.  The test points sit away from the two zeros K crosses, near R = 0.85 and 0.45.
  D11 (computed; 465) No inner trapping horizon on the plane.  With the plane's t-translation symmetry, both null
      expansions of its 2-spheres have the sign of dR/dtau.  That stays negative throughout: -0.24 at the start is its
      largest value and -5.1 at the end its least.  Section 2's semiclassical transition needs an inner trapping horizon to amplify, and here
      there is none: the passage left is 273's quantum bounce.
  Prior art (READ, BOUNCE-RESEARCH section 26):
    - Maeda, Okamura and Koga: in inhomogeneous charged AdS holes the Cauchy horizon disappears and the curvature
      diverges.
    - Ansorg and Hennig: the inner horizon rests on the Ernst equation's integrability.
    - D7 is that prior art's prediction, computed for this hole.  bulk26 W9's r- = 0.316 ell (an area product, S12)
      marks where the singular end falls, at 0.30 ell; it is not a horizon.
"""
import os, sys, math, subprocess, warnings
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
DN = os.path.join(HERE, "p3_work", "dn")
sys.path.insert(0, DN)
warnings.filterwarnings("ignore")
np.seterr(all="ignore")
MUT = set()
KAP = 0.2908
CHG = (os.path.join(DN, "glob_kap0.2908.npy"), KAP, 38)
CTL = (os.path.join(DN, "glob_ctrl0.npy"), 0.0, 34)
S0 = -0.05
KCUT = 1e10


def _eqs():
    for script, pkl in (("dneqE.py", "dneqE.pkl"), ("dn_sigma_eq.py", "dn_sigma_eq.pkl")):
        if not os.path.exists(os.path.join(DN, pkl)):
            subprocess.run([sys.executable, script], cwd=DN, check=True, stdout=subprocess.DEVNULL)


_eqs()
import sympy as sp
import dnE, dnx, dnrun, dninit, dn_sigma


def evo_class():
    base = dnx.DNX

    class C(base):
        def plane_slopes(self, Y):
            if "israel_sign" in MUT or "kappa0" in MUT:
                k = self.kap
                self.kap = -k if "israel_sign" in MUT else 0.0
                try:
                    return base.plane_slopes(self, Y)
                finally:
                    self.kap = k
            return base.plane_slopes(self, Y)

        def mass(self, J):
            if "no_mass" in MUT and self.jL == 0:
                JJ = dict(J, chi=self.chi, m=0 * self.chi)
                m = dnE.MDEF(*[JJ[n] for n in dnE.names])
                m[0] = 0.0
                mr3 = np.empty_like(m)
                mr3[1:] = m[1:] / J["r"][1:]**3
                mr3[0] = mr3[1]
                return m, mr3
            return base.mass(self, J)
    return C


# ---------------------------------------------------------------- exact AdS5 in the chart
def ads_exact(chi, tau):
    sig = -np.log(np.cosh(tau)) + 0 * chi
    A = sig + np.log(np.cosh(chi))
    S = sig + A / 2
    r = np.exp(A / 2) * np.sinh(chi) / np.cosh(tau)
    return [S, A, r, -1.5 * np.tanh(tau) + 0 * chi, -np.tanh(tau) + 0 * chi, r * (-1.5 * np.tanh(tau))]


def ads_class():
    base = evo_class()

    class ADS(base):
        def plane_slopes(self, Y):
            k = np.tanh(1.0) / 2 + 1 / np.tanh(1.0)
            return [np.tanh(1.0) / 2, np.tanh(1.0), Y[2][-1] * k], [0.0, 0.0, Y[5][-1] * k]
    return ADS


def d0_exact():
    D = dnE.D
    T, X = sp.symbols("T X")
    sg = -sp.log(sp.cosh(T)); Ae = sg + sp.log(sp.cosh(X)); Se = sg + Ae / 2
    re = sp.exp(Ae / 2) * sp.sinh(X) / sp.cosh(T)
    pt = {T: 0.37, X: 0.61}
    v = {}
    for nm, f in (("S", Se), ("A", Ae), ("r", re)):
        for k, e in (("", f), ("_t", f.diff(T)), ("_x", f.diff(X)), ("_tx", f.diff(T, X)), ("_xx", f.diff(X, 2)),
                     ("_tt", f.diff(T, 2))):
            v[nm + k] = float(e.subs(pt))
    v["chi"] = 0.61
    v["m"] = v["r"] / 2 * (1 + math.exp(-2 * v["S"]) * (v["r_t"]**2 - v["r_x"]**2))
    a = [v[n] for n in dnE.names]
    err = max(abs(float(sp.lambdify(dnE.SY, e)(*a)) - v[nm + "_tt"]) for e, nm in zip(D["rhs_m"], ("S", "A", "r")))
    mx_ex = float(sp.diff((re / 2) * (1 + sp.exp(-2 * Se) * (re.diff(T)**2 - re.diff(X)**2)), X).subs(pt))
    emx = abs(dnE.MX(*a) - mx_ex)
    K = float(dnrun.KR(*a))
    return err, emx, K


def d1_ads(Ns=(20, 40, 80), T=1.0):
    errs = []
    for N in Ns:
        ev = ads_class()(N, 0.0); dt = 0.25 * ev.h
        Y = ads_exact(ev.chi, 0.0)
        for _ in range(int(round(T / dt))):
            Y = ev.step(Y, dt)
        E = ads_exact(ev.chi, T)
        errs.append([np.abs(Y[m] - E[m]).max() for m in range(3)])
    return np.array(errs)


def d2_sigma_frame():
    class ADSs(dn_sigma.DN):
        def plane_slopes(self, f):
            return [0.0, np.tanh(1.0), 1 / np.tanh(1.0) - 1.0], [0.0, 0.0, 0.0]
    out = []
    for N in (20, 40):
        ev = ADSs(N, 0.0); dt = 0.25 * ev.h
        chi = ev.chi
        def ex(tau):
            sig = -np.log(np.cosh(tau)) + 0 * chi
            psi = np.where(chi > 0, np.log(np.sinh(chi + (chi == 0)) / (chi + (chi == 0))), 0.0)
            return [sig, sig + np.log(np.cosh(chi)), psi, -np.tanh(tau) + 0 * chi, -np.tanh(tau) + 0 * chi, 0 * chi]
        Y, tb = ex(0.0), np.inf
        for n in range(int(round(1.0 / dt))):
            Y = ev.step(Y, dt)
            e = np.abs(Y[0] - ex((n + 1) * dt)[0]).max()
            if not np.isfinite(e) or e > 1.0:
                tb = (n + 1) * dt
                break
        out.append(tb)
    return out


# ---------------------------------------------------------------- the holes
_RUNS = {}


def run(which, N, s0=S0, Kcut=KCUT, tmax=1.6):
    key = (which, N, s0, Kcut, tuple(sorted(MUT)))
    if key not in _RUNS:
        fn, kap, Ns = CHG if which == "charged" else CTL
        if "no_excision" in MUT:
            Kcut = np.inf
        _RUNS[key] = dnx.run(fn, s0, N, kap, Ns, tmax, Kcut=Kcut, quiet=True, cls=evo_class())
    return _RUNS[key]


def series(hist, k):
    return np.array([h["tau"] for h in hist]), np.array([h[k] for h in hist])


def at(hist, t, k):
    ts, v = series(hist, k)
    return np.interp(t, ts, v) if t <= ts[-1] else np.nan


def plane_curve(hist):
    R = np.array([h["Rpl"] for h in hist]); N = np.array([h["Npl"] for h in hist]); K = np.array([h["Kpl"] for h in hist])
    return R[::-1], N[::-1], K[::-1]


def static_plane(fn, Ns, ss, Nx=20, smin=-0.30):
    cp2 = dninit.cp2
    U = np.load(fn); n = (Ns + 1) * (Nx + 1)
    t, _ = cp2.cheb01(Ns); s = 1 - (1 - smin) * t
    T = U[0:n].reshape(Ns + 1, Nx + 1)[:, -1]; S = U[4 * n:5 * n].reshape(Ns + 1, Nx + 1)[:, -1]
    M = cp2.DT.interp_matrix(s, ss)
    return -4 * ss * (M @ T), 2 * np.sqrt(M @ S) / (1 - ss)          # on the plane w = 4: g_tt, sqrt(g_OmOm)


def init_constraints(N):
    fn, kap, Ns = CHG
    Y, chk = dnrun.initial(fn, S0, N, kap, Ns)
    ev = evo_class()(N, kap)
    J = ev.jets(Y); m, _ = ev.mass(J); J["chi"], J["m"] = ev.chi, m
    a = [J[k] for k in dnE.names]
    e2 = np.exp(2 * Y[0] - Y[1])
    lo, hi = int(0.25 * N), int(0.9 * N)
    return np.abs(dnE.CU(*a)[lo:hi] / e2[lo:hi]).max(), np.abs(dnE.CV(*a)[lo:hi] / e2[lo:hi]).max(), chk


def cut_speed(cut):
    c = np.array(cut)
    if len(c) < 3:
        return np.nan
    sl = np.diff(c[1:, 1]) / np.maximum(np.diff(c[1:, 0]), 1e-12)       # after the first cut (the axis region)
    return sl.min()


def end_state(hist):
    N = np.array([h["Npl"] for h in hist]); K = np.array([h["Kpl"] for h in hist]); R = np.array([h["Rpl"] for h in hist])
    i = int(np.argmax(N))
    sel = (N < 0.08) & (N > 0) & (np.arange(len(N)) > i)
    p = np.polyfit(np.log(N[sel]), np.log(np.abs(K[sel])), 1)[0] if sel.sum() > 4 else np.nan
    Rend = np.polyfit(N[sel][-6:], R[sel][-6:], 1)[1] if sel.sum() > 6 else np.nan
    return dict(Nmax=N[i], RNmax=R[i], Nlast=N[-1], Klast=K[-1], Rlast=R[-1], p=p, Rend=Rend)


def selftest(quiet=False):
    say = (lambda *a: None) if quiet else print
    ok = []
    e, emx, K = d0_exact()
    r = e < 1e-9 and emx < 1e-9 and abs(K - 40) < 1e-9; ok.append(r)
    say("D0 exact AdS5: second derivatives %.1e, m_x %.1e, K = %.10f: %s" % (e, emx, K, r))
    E = d1_ads()
    rat = E[:-1] / E[1:]
    r = bool(np.all(np.isfinite(E)) and np.all((rat > 3.5) & (rat < 4.5))); ok.append(r)
    say("D1 AdS5 evolution, errors (S, A, r) at N = 20, 40, 80: %s; ratios %s: %s" % (
        " ".join("%.1e" % v for v in E[:, 1]), " ".join("%.2f" % v for v in rat.ravel()), r))
    tb = d2_sigma_frame()
    r = tb[0] < 0.5 and tb[1] < 0.75 * tb[0]; ok.append(r)
    say("D2 the sig-frame on the same data blows up at tau %.3f (N = 20), %.3f (N = 40) -- rate ~ 1/h: %s" % (*tb, r))
    c1, v1, chk = init_constraints(100)
    c2, v2, _ = init_constraints(200)
    r = abs(chk["dxA"] - chk["kb"]) < 1e-5 and abs(chk["dxlR"] - chk["kO"]) < 1e-5; ok.append(r)
    say("D3 plane rows off the static slice: %.6f vs 1 - q = %.6f; %.6f vs 1 + q = %.6f: %s" % (
        chk["dxA"], chk["kb"], chk["dxlR"], chk["kO"], r))
    r = c1 / c2 > 2.5 and v1 / v2 > 2.5 and max(c2, v2) < 1e-3; ok.append(r)
    say("D4 initial constraints in chi [0.25, 0.9], to the static solve's floor: C_uu %.1e -> %.1e, C_vv %.1e -> %.1e "
        "(ratios %.2f, %.2f): %s" % (
        c1, c2, v1, v2, c1 / c2, v1 / v2, r))
    h4, _ = run("charged", 400)
    ss = np.linspace(-0.28, -0.07, 8)
    Nst, Rst = static_plane(CHG[0], CHG[2], ss)
    R4, N4, K4 = plane_curve(h4)
    dN = np.abs(np.interp(Rst, R4, N4) - Nst).max()
    r = dN < 1e-3; ok.append(r)
    say("D5 plane N(R), evolution against the static solve over s in [-0.28, -0.07]: max |dN| %.1e: %s" % (dN, r))
    hc, _ = run("control", 400, tmax=1.0)
    c = hc[-1]
    r = c["Rpl"] < 0.06 and c["Kpl"] > 1e9 and c["Npl"] > 100; ok.append(r)
    say("D6 control: the plane ends at R %.3f, N %.1f, K %.1e (crunch): %s" % (c["Rpl"], c["Npl"], c["Kpl"], r))
    es = end_state(h4)
    r = (4.0 < es["Nmax"] < 4.2 and 0.60 < es["RNmax"] < 0.65 and es["Nlast"] < 0.02 and abs(es["Klast"]) > 1e9
         and 0.29 < es["Rend"] < 0.31 and -1.6 < es["p"] < -1.2); ok.append(r)
    say("D7 charged plane: N max %.3f at R %.3f; ends N %.1e, K %.1e, R -> %.4f; K ~ N^%.2f: %s" % (
        es["Nmax"], es["RNmax"], es["Nlast"], es["Klast"], es["Rend"], es["p"], r))
    h1, _ = run("charged", 100); h2, cut2 = run("charged", 200)
    rats = []
    for t in (1.2, 1.28):
        for k in ("Npl", "Rpl"):
            v = [at(h, t, k) for h in (h1, h2, h4)]
            rats.append((v[0] - v[1]) / (v[1] - v[2]))
    rats = np.array(rats)
    r = bool(np.all(np.isfinite(rats)) and np.all((rats > 3.3) & (rats < 4.7))); ok.append(r)
    say("D8 plane N, R convergence at tau 1.2, 1.28 (N = 100, 200, 400): ratios %s: %s" % (
        " ".join("%.2f" % v for v in rats), r))
    _, cut4 = run("charged", 400)
    h2b, _ = run("charged", 200, Kcut=1e8)
    sp2, sp4 = cut_speed(cut2), cut_speed(cut4)
    dK = abs(at(h2b, 1.28, "Npl") / at(h2, 1.28, "Npl") - 1)
    r = sp2 > 1 and sp4 > 1 and dK < 1e-4; ok.append(r)
    say("D9 excision: slowest cut speed %.2f (N 200), %.2f (N 400); plane N at Kcut 1e8 vs 1e10 differs %.1e: %s" % (
        sp2, sp4, dK, r))
    hs, _ = run("charged", 200, s0=-0.15)
    Ra, Na, Ka = plane_curve(h2); Rb, Nb, Kb = plane_curve(hs)
    dev = max(max(abs(np.interp(x, Ra, Na) / np.interp(x, Rb, Nb) - 1), abs(np.interp(x, Ra, Ka) / np.interp(x, Rb, Kb) - 1))
              for x in (1.0, 0.7, 0.4, 0.35, 0.32))
    r = dev < 3e-3; ok.append(r)
    say("D10 start slice s0 = -0.05 against -0.15: N(R), K(R) agree to %.1e: %s" % (dev, r))
    d = np.array([h["dRpl"] for h in h4])
    r = bool(np.all(d < 0) and d[-1] < 4 * d[0] and d[-1] == d.min() and d.max() == d[0]); ok.append(r)
    say("D11 plane dR/dtau_proper stays negative, %.2f at the start (its largest) to %.2f at the end (its least): no "
        "inner trapping horizon: %s" % (d[0], d[-1], r))
    say("%d/%d" % (sum(ok), len(ok)))
    return all(ok)


def mutants():
    names = ["israel_sign", "no_mass", "kappa0", "no_excision"]
    caught = 0
    for m in names:
        MUT.clear(); MUT.add(m)
        try:
            bad = not selftest(quiet=True)
        except Exception:
            bad = True
        caught += bad
        print("mutant %-12s %s" % (m, "caught" if bad else "MISSED"))
    MUT.clear()
    print("%d/%d caught" % (caught, len(names)))
    return caught == len(names)


def report():
    h, cut = run("charged", 400)
    print("Charged magnetic hole (kappa %.4f), plane history (N = 400, s0 = %.2f):" % (KAP, S0))
    print("   tau    cut chi   N = g_tt    R/ell     K")
    for t in (0.0, 0.3, 0.6, 0.9, 1.1, 1.2, 1.25, 1.28, 1.30, 1.31):
        print("  %.2f    %.3f    %.4e  %.4f  %+.3e" % (t, at(h, t, "chiL"), at(h, t, "Npl"), at(h, t, "Rpl"), at(h, t, "Kpl")))
    es = end_state(h)
    print("N max %.3f at R %.3f; the plane ends where N -> 0 at R %.4f, with K ~ N^%.2f (K %.2e at N %.1e)" % (
        es["Nmax"], es["RNmax"], es["Rend"], es["p"], es["Klast"], es["Nlast"]))
    print("the singularity first forms near the axis at tau %.3f and reaches the plane at tau %.3f; slowest cut speed %.2f"
          % (cut[0][0], h[-1]["tau"], cut_speed(cut)))
    hc, _ = run("control", 400, tmax=1.0)
    print("control (kappa 0): the plane crunches at tau %.3f: R %.3f, N %.1f, K %.1e" % (
        hc[-1]["tau"], hc[-1]["Rpl"], hc[-1]["Npl"], hc[-1]["Kpl"]))


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    if "--mutants" in sys.argv:
        sys.exit(0 if mutants() else 1)
    report()
