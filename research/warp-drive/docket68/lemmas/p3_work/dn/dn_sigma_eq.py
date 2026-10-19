"""P3 double-null (conformal gauge) equations, item 464.
g = e^{2 sig}(-dtau^2 + dchi^2) + e^{2A} dt^2 + R^2 dOmega^2,  R = chi e^{sig + psi} (psi even, psi = 0 on the axis
is elementary flatness).  Bulk: R_ab = -4 g_ab (ell = 1).  Evolution: E_uv, E_tt, E_thth solved for the three
second tau-derivatives; constraints E_uu, E_vv (u = tau - chi, v = tau + chi)."""
import sympy as sp, pickle, os

tau, chi, t, th, ph = sp.symbols("tau chi t th ph")
X = [tau, chi, t, th, ph]
sig, A, psi = (sp.Function(n)(tau, chi) for n in ("sig", "A", "psi"))
R = chi * sp.exp(sig + psi)
g = sp.diag(-sp.exp(2 * sig), sp.exp(2 * sig), sp.exp(2 * A), R**2, R**2 * sp.sin(th)**2)
gi = sp.diag(*[1 / g[i, i] for i in range(5)])


def ricci(g, gi):
    n = 5
    G = [[[sum(gi[a, e] * (sp.diff(g[e, b], X[c]) + sp.diff(g[e, c], X[b]) - sp.diff(g[b, c], X[e])) / 2
               for e in range(n)) for c in range(n)] for b in range(n)] for a in range(n)]
    Ric = sp.zeros(n)
    for b in range(n):
        for c in range(b, n):
            v = sum(sp.diff(G[a][b][c], X[a]) for a in range(n)) - sum(sp.diff(G[a][b][a], X[c]) for a in range(n))
            v += sum(G[a][a][e] * G[e][b][c] - G[a][c][e] * G[e][b][a] for a in range(n) for e in range(n))
            Ric[b, c] = Ric[c, b] = sp.simplify(v)
    return Ric


Ric = ricci(g, gi)
E = Ric + 4 * g
# jet symbols
names = {"sig": sig, "A": A, "psi": psi}
J = {}
for nm, f in names.items():
    for k, d in (("", f), ("_t", f.diff(tau)), ("_x", f.diff(chi)), ("_tt", f.diff(tau, 2)), ("_tx", f.diff(tau, chi)),
                 ("_xx", f.diff(chi, 2))):
        J[nm + k] = (sp.Symbol(nm + k), d)


def jet(e):
    for key in sorted(J, key=lambda k: -len(k.split("_")[-1]) if "_" in k else 0):
        pass
    order = [k for k in J if k.endswith(("_tt", "_tx", "_xx"))] + [k for k in J if k.endswith(("_t", "_x"))] + list(names)
    for k in order:
        e = e.subs(J[k][1], J[k][0])
    return e


Euv = jet((E[0, 0] - E[1, 1]) / 4)
Ett = jet(E[2, 2] * sp.exp(-2 * A))
Eth = jet(E[3, 3] / R**2)
tt = [J["sig_tt"][0], J["A_tt"][0], J["psi_tt"][0]]
sol = sp.solve([Euv, Ett, Eth], tt, dict=True)[0]
rhs = [sp.simplify(sol[v]) for v in tt]
Euu = jet((E[0, 0] - 2 * E[0, 1] + E[1, 1]) / 4)
Evv = jet((E[0, 0] + 2 * E[0, 1] + E[1, 1]) / 4)
Cu = sp.simplify(Euu.subs(dict(zip(tt, rhs))))
Cv = sp.simplify(Evv.subs(dict(zip(tt, rhs))))
syms = [chi] + [J[k][0] for k in J if not k.endswith("_tt")]
pickle.dump(dict(rhs=rhs, Cu=Cu, Cv=Cv, syms=syms), open("dn_sigma_eq.pkl", "wb"))
for v, r in zip(tt, rhs):
    print(v, "=", r)
print("C_uu =", Cu)

# axis limits (chi -> 0) for even sig, A and psi with psi(0) = 0: f_x ~ chi f_xx, psi ~ chi^2 psi_xx / 2
eps = sp.Symbol("eps", positive=True)
lim = {J["sig_x"][0]: eps * J["sig_xx"][0], J["A_x"][0]: eps * J["A_xx"][0], J["psi_x"][0]: eps * J["psi_xx"][0],
       J["psi"][0]: eps**2 * J["psi_xx"][0] / 2, J["psi_t"][0]: eps**2 * J["psi_tx"][0], chi: eps}
rhs0 = [sp.simplify(sp.limit(r.subs(lim), eps, 0)) for r in rhs]
print("axis:", rhs0)

# Kretschmann (K - 40 is Weyl^2 for R_ab = -4 g_ab in five dimensions)
n = 5
Gm = [[[sum(gi[a, e] * (sp.diff(g[e, b], X[c]) + sp.diff(g[e, c], X[b]) - sp.diff(g[b, c], X[e])) / 2
            for e in range(n)) for c in range(n)] for b in range(n)] for a in range(n)]
K = 0
for a in range(n):
    for b in range(n):
        for c in range(n):
            for d in range(c + 1, n):
                r = (sp.diff(Gm[a][d][b], X[c]) - sp.diff(Gm[a][c][b], X[d])
                     + sum(Gm[a][c][e] * Gm[e][d][b] - Gm[a][d][e] * Gm[e][c][b] for e in range(n)))
                if r != 0:
                    K += 2 * r**2 * g[a, a] * gi[b, b] * gi[c, c] * gi[d, d]
Kj = jet(K).subs(th, sp.pi / 3)
Kj = Kj.subs(dict(zip(tt, rhs)))
pickle.dump(dict(rhs=rhs, Cu=Cu, Cv=Cv, syms=syms, rhs0=rhs0, K=Kj), open("dn_sigma_eq.pkl", "wb"))
print("K built, ops", sp.count_ops(Kj))
