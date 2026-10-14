"""check: phi from the damping generator's xi equals eqs_fw's PHI on a state of the undamped run"""
import numpy as np, pickle
import interior_fw as IF, interior_damp as ID, core_fw as C
P = pickle.load(open("ifw_16_1_-0.002_-0.3.pkl", "rb")); st = dict(file="fw_bt1_24_24.npy", Ns=24, Nx=24)
I = IF.Interior(16, 1.0, st); I.lastbr = ID.static_brane(1.0); m = I.m
for k in range(len(P["t"])):
    s, Y = P["t"][k], P["y"][:, k]; I.brane_values(s, Y[:5 * m].reshape(5, m), Y[5 * m:].reshape(5, m))
ph = IF.phi_at(I, s, Y); xs, xx = ID.xi_at(I, s, Y)
Xf, Vf = I.brane_values(s, Y[:5 * m].reshape(5, m), Y[5 * m:].reshape(5, m))
f = 1 - s; Dl = 1 / I.b + (1 - I.xn ** 2) / f; g = 2 - I.xn ** 2
gss = Xf[2] / (f ** 4 * s) / Dl ** 2; gxx = 4 * Xf[3] / (f ** 2 * g) / Dl ** 2; gsx = I.xn * Xf[4] / (2 * f ** 3) / Dl ** 2
ph2 = gss * xs ** 2 + 2 * gsx * xs * xx + gxx * xx ** 2
print("s=%.4f max|phi| %.3e, max|phi - phi(xi)| %.3e (axis node excluded); xi^x at brane %.2e" % (s, np.nanmax(np.abs(ph[1:])), np.nanmax(np.abs(ph - ph2)[1:]), xx[-1]))
print("phi", ph[:4], ph2[:4])
