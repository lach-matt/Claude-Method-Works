"""P3 double-null initial data (item 464): the magnetic static hole's slice s = s0 inside the horizon, in conformal gauge.
chi = proper length reparametrised so that sig = sig0 + c chi^2/2 meets the plane's Israel condition at the corner
(the plane at chi = 1 has geodesic curvature e^-sig sig_chi = 1 - kap/R^4); d_tau = e^sig n, n the future unit normal
(toward decreasing s); sig_tau = e^sig k2, k2 the slice's geodesic curvature in the (s, x) quotient."""
import os, sys, numpy as np, sympy as sp, importlib.util
from numpy.polynomial import chebyshev as Ch
L = "/home/user/Claude-Method-Works/research/warp-drive/docket68/lemmas"
_spec = importlib.util.spec_from_file_location("cp2m", os.path.join(L, "corridor_p2.py"))
cp2 = importlib.util.module_from_spec(_spec); _spec.loader.exec_module(cp2)

s, x = sp.symbols("s x")
FN = ["T", "A", "B", "F", "S"]
fs = {k: sp.Function(k)(s, x) for k in FN}
bt = 2
f, gx = 1 - s, 2 - x**2
w = (bt * f / (f + bt * (1 - x**2)))**2
gtt = -w * s * fs["T"]
gss = w * fs["A"] / (s * f**4)
gxx = w * 4 * fs["B"] / (f**2 * gx)
gsx = w * x * fs["F"] / (2 * f**3)
det2 = gss * gxx - gsx**2
gSS, gSX = gxx / det2, -gsx / det2
sq = sp.sqrt(-gSS)
ns, nx = gSS / sq, gSX / sq
vol = sp.sqrt(-det2)
k2 = (sp.diff(vol * ns, s) + sp.diff(vol * nx, x)) / vol
Ast = sp.log(gtt) / 2
lrho = sp.log(sp.sqrt(w * gx * fs["S"]) / f)          # R = x rho
nA = ns * sp.diff(Ast, s) + nx * sp.diff(Ast, x)
nlR = ns * sp.diff(lrho, s) + nx * sp.diff(lrho, x) + (-(w * fs["F"] / (2 * f**3)) / det2) / sq
qty = dict(k2=k2, A=Ast, lrho=lrho, nA=nA, nlR=nlR, sgxx=sp.sqrt(gxx), gsx=gsx,
           dxA=sp.diff(Ast, x), dxlR=sp.diff(lrho, x))
jets = []
for k in FN:
    jets += [(sp.Symbol(k), fs[k]), (sp.Symbol(k + "_s"), fs[k].diff(s)), (sp.Symbol(k + "_x"), fs[k].diff(x))]


def tojet(e):
    for sym, d in jets[::-1]:
        e = e.subs(d, sym)
    return e


LAM = {k: sp.lambdify([s, x] + [j[0] for j in jets], tojet(v), "numpy") for k, v in qty.items()}


def slice_data(U, s0, Ns=38, Nx=20, smin=-0.30):
    t, Dt = cp2.cheb01(Ns)
    sg = 1 - (1 - smin) * t
    Ds = -Dt / (1 - smin)
    xg, Dx = cp2.cheb01(Nx)
    n = (Ns + 1) * (Nx + 1)
    I0 = cp2.DT.interp_matrix(sg, np.array([s0]))
    args = []
    for m in range(5):
        Fm = U[m * n:(m + 1) * n].reshape(Ns + 1, Nx + 1)
        v = (I0 @ Fm)[0]
        args += [v, (I0 @ (Ds @ Fm))[0], Dx @ v]
    with np.errstate(all="ignore"):
        out = {k: lam(s0, xg, *args) * np.ones_like(xg) for k, lam in LAM.items()}
    return xg, out


def conformal(U, s0, N, kap, **kw):
    xg, q = slice_data(U, s0, **kw)
    t = 2 * xg - 1                                             # x in [0, 1] -> [-1, 1]
    cs = Ch.chebfit(t, q["sgxx"], len(xg) - 1)
    ci = Ch.chebint(cs, lbnd=-1) / 2                          # l(x) = int_0^x sqrt(g_xx)
    ell = lambda xx: Ch.chebval(2 * xx - 1, ci)
    Lp = ell(1.0)
    Rb = np.exp(q["lrho"][-1])
    kb = 1 - kap / Rb**4
    # the sign check: the plane's Israel rows read off the static slice (g_sx = 0 on the plane)
    chk = dict(dxA=q["dxA"][-1] / q["sgxx"][-1], dxlR=(1 + q["dxlR"][-1]) / q["sgxx"][-1], kb=kb,
               kO=1 + kap / Rb**4, gsx_plane=q["gsx"][-1], Rb=Rb, L=Lp)
    # gauge: sig quadratic in proper length, sig(l) = sig0 + kb l^2 / (2 Lp), so d sig / d l = kb at the plane
    from scipy.integrate import quad
    sigl = lambda l: kb * l**2 / (2 * Lp)
    I1 = quad(lambda l: np.exp(-sigl(l)), 0, Lp, epsabs=1e-14, epsrel=1e-14)[0]
    sig0 = np.log(I1)                                          # chi(Lp) = 1
    chi = np.arange(N + 1) / N
    lch = np.zeros(N + 1)
    for j in range(1, N + 1):
        l = chi[j] * Lp
        for _ in range(40):
            r = np.exp(-sig0) * quad(lambda u: np.exp(-sigl(u)), 0, l, epsabs=1e-15, epsrel=1e-14)[0] - chi[j]
            l -= r / (np.exp(-sig0 - sigl(l)))
            if abs(r) < 1e-15:
                break
        lch[j] = l
    lch[-1] = Lp
    sig = sig0 + sigl(lch)
    c = kb / Lp
    xj = lch / Lp
    cd = Ch.chebder(ci) * 2
    for _ in range(50):
        xj = xj - (ell(xj) - lch) / Ch.chebval(2 * xj - 1, cd)
    xj = np.clip(xj, 0, 1)
    M = cp2.DT.interp_matrix(xg, xj)
    v = {k: M @ q[k] for k in ("k2", "A", "lrho", "nA", "nlR")}
    es = np.exp(sig)
    R = xj * np.exp(v["lrho"])
    psi = np.zeros(N + 1)
    psi[1:] = np.log(R[1:] / (chi[1:] * es[1:]))
    sig_t = es * v["k2"]
    A_t = es * v["nA"]
    psi_t = es * v["nlR"] - sig_t
    chk.update(psi_axis_limit=q["lrho"][0] - np.log(q["sgxx"][0]),
               psi_t_axis=psi_t[0], c=c, sig0=sig0)
    psi_t[0] = 0.0
    return chi, dict(sig=sig, A=v["A"], psi=psi, sig_t=sig_t, A_t=A_t, psi_t=psi_t, x=xj), chk


if __name__ == "__main__":
    U = np.load(sys.argv[1]); s0 = float(sys.argv[2]); kap = float(sys.argv[3]); Ns = int(sys.argv[4])
    chi, d, chk = conformal(U, s0, 40, kap, Ns=Ns)
    print("plane: e^-sig A_chi = %.6f vs 1 - kap/R^4 = %.6f ; e^-sig (log R)_chi = %.6f vs 1 + kap/R^4 = %.6f ; g_sx %.1e"
          % (chk["dxA"], chk["kb"], chk["dxlR"], chk["kO"], chk["gsx_plane"]))
    print("R_plane %.5f  L %.5f  sig0 %.5f  c %.5f ; axis: psi limit %.1e, psi_t %.1e" % (
        chk["Rb"], chk["L"], chk["sig0"], chk["c"], chk["psi_axis_limit"], chk["psi_t_axis"]))
    for j in range(0, 41, 8):
        print("  chi %.2f x %.4f sig %.5f A %.5f psi %+.5f | sig_t %+.5f A_t %+.5f psi_t %+.5f" % (
            chi[j], d["x"][j], d["sig"][j], d["A"][j], d["psi"][j], d["sig_t"][j], d["A_t"][j], d["psi_t"][j]))
