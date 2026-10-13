"""Along a cm_run.py checkpoint, the computed C-metric interior against the exact one.  At each requested lambda:
phi~ (DeTurck or harmonic), the lapse N(1 - s), proper time since the horizon along the coordinate lines (the shift
reported), and at every node the exact point (r, xc) recovered from the two Killing norms (cm_exact.py), with the
computed Kretschmann scalar (X_ss from the evolution equations) against the exact one there.  The decisive numbers:
r/mu where the run fails (r = 0 is the singularity), and how far K_num departs from K_exact before then.
Arguments: checkpoint lambda1 lambda2 ..."""
import os, sys, pickle
P = pickle.load(open(sys.argv[1], "rb")); os.environ["PROB"] = P["tag"]
import numpy as np, sympy as sp
import core_fw as C, interior_fw as IF, interior_damp as ID, interior_cb as CB, cm_exact as M
from cheb_tail_fn import cheb
targets = [float(v) for v in sys.argv[2:]]
b, Nx = P["b"], P["Nx"]; st = dict(file=C.static_file(b, P["Ns"], P["Nxs"]), Ns=P["Ns"], Nx=P["Nxs"])
I = CB.HarmOld(Nx, b, st, P["kap"], P["at"], P["s1"], P["ramp"]); I.lastbr = P["lastbr0"].copy(); m = I.m
E = M.Exact(P["tag"]); mid = Nx // 2; x = I.xn
NM = [sp.Symbol(n) for n in C.names]
fg = sp.lambdify([C.s, C.x] + NM, [C.ev(C._raw["metric"][k]) for k in ("gtt", "gss", "gsx", "gxx", "gpp")], "numpy")
fK = sp.lambdify([C.s, C.x] + C.VARS, C.ev(pickle.load(open("kretsch_%s.pkl" % P["tag"], "rb"))), "numpy", cse=True)

def geo(s, Xg):
    gtt, gss, gsx, gxx, gpp = [np.asarray(v, dtype=float) * np.ones(Nx + 1) for v in fg(s, x, *Xg)]
    with np.errstate(all="ignore"):
        N = 1 / np.sqrt(-gxx / (gss * gxx - gsx ** 2))
        return N, gtt, gpp, np.abs(gsx) / np.sqrt(np.abs(gss) * gxx)

def tau_exact(r, xc, n=400):
    """proper time from the horizon to r along fixed xc in the exact chart"""
    t0 = np.arcsin(np.sqrt(min(r / E.mu, 1.0))); th = t0 + (np.pi / 2 - t0) * (np.arange(n) + 0.5) / n
    rr = E.mu * np.sin(th) ** 2
    return float(np.sum(2 * E.mu * np.sin(th) ** 2 / (1 + xc * rr)) * (np.pi / 2 - t0) / n)

r_prev = E.mu / (1 - P["s0"]) * np.ones(Nx + 1); xc_prev = E.x1 * (1 - x ** 2)
tau = np.zeros(Nx + 1); prev = None
print("cm %s Nx %d kap %g s1 %g: mu %.4f x1 %.4f; exact tau to r = 0 along xc = const: axis %.4f mid %.4f brane %.4f"
      % (P["tag"], Nx, P["kap"], P["s1"], E.mu, E.x1, E.tau_total(E.x1), E.tau_total(E.x1 * (1 - x[mid] ** 2)),
         E.tau_total(0.0)), flush=True)
for k in range(len(P["t"]) - 1):                                # the Radau phase, for proper time and the brane solve
    s, Y = P["t"][k], P["y"][:, k]
    Xf, Vf = I.brane_values(s, Y[:5 * m].reshape(5, m), Y[5 * m:].reshape(5, m))
    N = geo(s, Xf)[0]
    if prev is not None:
        tau += 0.5 * (N + prev[1]) * abs(s - prev[0])
    prev = (s, N)
for k in range(len(P["lt"])):
    s, Y = IF.state_s(I, P["lt"][k], P["ly"][:, k])
    Xf, Vf = I.brane_values(s, Y[:5 * m].reshape(5, m), Y[5 * m:].reshape(5, m))
    N = geo(s, Xf)[0]
    if prev is not None:
        tau += 0.5 * (N + prev[1]) * abs(s - prev[0])
    prev = (s, N)
    if targets and (P["lt"][k] >= targets[0] or k == len(P["lt"]) - 1):
        targets.pop(0); keep = I.lastbr.copy()
        ph = np.abs(I.phi_t(s, Y)); j = 1 + int(np.nanargmax(ph[1:]))
        Fxb = I.slope(s, Xf, Vf); Xg, Vg, DX, DXX, DV = I.derivs(Xf, Vf, Fxb, None)
        Xss_in = I.xss(s, Xf, Vf, Fxb, None); Xss = np.zeros_like(Xg); Xss[:, 1:Nx] = Xss_in
        for e in range(5):
            Xss[e, 0] = C.bary_interp(x[1:Nx], Xss_in[e], [x[0]])[0]
            Xss[e, Nx] = C.bary_interp(x[1:Nx], Xss_in[e], [1.0])[0]
        a = []
        for e in range(5):
            a += [Xg[e], Vg[e], DX[e], Xss[e], DXX[e], DV[e]]
        with np.errstate(all="ignore"):
            K = np.asarray(fK(np.full(Nx + 1, s), x, *a), dtype=float) * np.ones(Nx + 1)
        I.lastbr = keep
        N, gtt, gpp, sh = geo(s, Xg)
        r = np.empty(Nx + 1); xc = np.empty(Nx + 1)
        for i in range(Nx + 1):
            r[i], xc[i] = E.invert(gtt[i], gpp[i], r_prev[i], xc_prev[i], axis=(i == 0))
        r_prev, xc_prev = r.copy(), xc.copy()
        Ke = E.K(r, xc); dK = np.abs(K / Ke - 1)
        tl = max(np.max((cheb(Xg[e]) / max(cheb(Xg[e]).max(), 1e-300))[-3:]) for e in range(5))
        te = [tau_exact(r[i], xc[i]) for i in (1, mid, Nx)]
        print("lam %.3f s %8.3f phi~ %.1e (x %.2f) | r/mu ax %.4f mid %.4f br %.4f | xc(brane) %+.1e | K ax %.2e "
              "mid %.2e nbr %.2e | max|K/Kex-1| inner %.1e | N(1-s) ax %.3f mid %.3f br %.3f | tau ax %.4f mid %.4f "
              "br %.4f (exact along xc %.4f %.4f %.4f) | tail %.0e | shift %.2f" % (
                  P["lt"][k], s, ph[j], x[j], r[1] / E.mu, r[mid] / E.mu, r[Nx] / E.mu, xc[Nx], K[1], K[mid],
                  K[Nx - 1], np.nanmax(dK[1:Nx]), N[1] * (1 - s), N[mid] * (1 - s), N[Nx] * (1 - s), tau[1],
                  tau[mid], tau[Nx], te[0], te[1], te[2], tl, np.nanmax(sh[1:])), flush=True)
