"""Item 372's calibrated top: along a cm_run.py checkpoint of the RSII hole (PROB=fw, eps = bt), the brane's interior
against four-dimensional Schwarzschild's.  On the brane (x = 1, F = 0, Dl = 1/bt) the induced metric is
bt^2 [s T dtau^2 + A ds^2/(f^4 s) + S dOmega^2/f^2]: the areal radius R = bt sqrt(S)/f, the horizon's R_h = bt sqrt(S)
at s = 0 (the static solution), and the s-line at fixed tau is the brane's t = const curve, a radial geodesic of
Schwarzschild's interior from the bifurcation sphere.  Compared, with no normalisation to choose:
  (dR/dtau)^2 against R_h/R - 1 (the geodesic's energy equation, E = 0), and
  the proper time from the horizon tau(R) against R_h [pi/2 - th + sin th cos th], sin^2 th = R/R_h,
and g_tautau = bt^2 s T against bt^2 (1 - R_h/R) (the asymptotic normalisation, t = bt tau).  The deviations should be
of order ell^2/R^2 and grow inward until the curvature radius reaches ell (earth_cap.py K7).
Arguments: checkpoint [every]."""
import os, sys, pickle
P = pickle.load(open(sys.argv[1], "rb")); os.environ["PROB"] = P["tag"]
import numpy as np
import core_fw as C, interior_fw as IF, interior_damp as ID, interior_cb as CB
every = int(sys.argv[2]) if len(sys.argv) > 2 else 10
b, Nx = P["b"], P["Nx"]; st = dict(file=C.static_file(b, P["Ns"], P["Nxs"]), Ns=P["Ns"], Nx=P["Nxs"])
I = CB.HarmOld(Nx, b, st, P["kap"], P["at"], P["s1"], P["ramp"]); I.lastbr = P["lastbr0"].copy(); m = I.m
Rh = b * np.sqrt(ID.static_brane(b, P["Ns"], P["Nxs"])[1])
print("bt %g Nx %d: R_h = %.5f ell (ell/R_h = %.4f, (ell/R_h)^2 = %.2e); Schwarzschild's total proper time "
      "pi R_h/2 = %.4f" % (b, Nx, Rh, 1 / Rh, Rh ** -2, np.pi * Rh / 2))
print("  %9s %8s %9s %10s %10s %11s %10s %9s" % ("s", "R/R_h", "tau/R_h", "tau_S/R_h", "dtau rel", "(dR/dtau)^2",
                                                 "rel", "gtt rel"))
states = [(P["t"][k], P["y"][:, k]) for k in range(len(P["t"]) - 1)]
states += [IF.state_s(I, P["lt"][k], P["ly"][:, k]) for k in range(len(P["lt"]))]
tau = None; prev = None
for k, (s, Y) in enumerate(states):
    Xf, Vf = I.brane_values(s, Y[:5 * m].reshape(5, m), Y[5 * m:].reshape(5, m))
    T, S, A = Xf[0, Nx], Xf[1, Nx], Xf[2, Nx]; Ss = Vf[1, Nx]; f = 1 - s; u = abs(s) ** 0.5
    N = b * np.sqrt(abs(A) / (f ** 4 * abs(s)))
    tau = 2 * abs(s) * N if prev is None else tau + (u * N + prev[1] * prev[0]) * (u - prev[0])
    prev = (u, N)
    if k % every and k != len(states) - 1:
        continue
    R = b * np.sqrt(S) / f; dRds = b * (Ss / (2 * np.sqrt(S) * f) + np.sqrt(S) / f ** 2)
    v2 = (dRds / N) ** 2; v2S = Rh / R - 1
    th = np.arcsin(np.sqrt(min(R / Rh, 1.0))); tS = Rh * (np.pi / 2 - th + np.sin(th) * np.cos(th))
    gtt = b * b * s * T; gS = b * b * (1 - Rh / R)
    print("  %9.4f %8.5f %9.5f %10.5f %10.2e %11.5f %10.2e %9.2e" % (s, R / Rh, tau / Rh, tS / Rh, tau / tS - 1, v2,
                                                                    v2 / v2S - 1 if v2S else 0, gtt / gS - 1),
          flush=True)
