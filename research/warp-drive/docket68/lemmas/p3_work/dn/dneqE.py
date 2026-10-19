"""P3 double-null equations in the four-dimensional Einstein frame (item 464).
g5 = e^{-A} [e^{2S}(-dtau^2 + dchi^2) + r^2 dOmega^2] + e^{2A} dt^2   (S = sig + A/2, r = e^{A/2} R).
Misner-Sharp mass m = (r/2)(1 + e^{-2S}(r_t^2 - r_x^2)); m_x = m_v - m_u first order by the constraints E_uu, E_vv."""
import sympy as sp, pickle
tau, chi, t, th, ph = sp.symbols("tau chi t th ph")
X = [tau, chi, t, th, ph]
S, A, r = (sp.Function(n)(tau, chi) for n in ("S", "A", "r"))
g = sp.diag(-sp.exp(2 * S - A), sp.exp(2 * S - A), sp.exp(2 * A), sp.exp(-A) * r**2, sp.exp(-A) * r**2 * sp.sin(th)**2)
gi = sp.diag(*[1 / g[i, i] for i in range(5)])
n = 5
G = [[[sum(gi[a, e] * (sp.diff(g[e, b], X[c]) + sp.diff(g[e, c], X[b]) - sp.diff(g[b, c], X[e])) / 2 for e in range(n))
       for c in range(n)] for b in range(n)] for a in range(n)]
def ric(b, c):
    v = sum(sp.diff(G[a][b][c], X[a]) for a in range(n)) - sum(sp.diff(G[a][b][a], X[c]) for a in range(n))
    v += sum(G[a][a][e] * G[e][b][c] - G[a][c][e] * G[e][b][a] for a in range(n) for e in range(n))
    return sp.simplify(v)
E = {k: ric(*k) + 4 * g[k] for k in [(0, 0), (1, 1), (0, 1), (2, 2), (3, 3)]}
names = {"S": S, "A": A, "r": r}
J = {}
for nm, f in names.items():
    for k, d in (("_tt", f.diff(tau, 2)), ("_tx", f.diff(tau, chi)), ("_xx", f.diff(chi, 2)), ("_t", f.diff(tau)),
                 ("_x", f.diff(chi)), ("", f)):
        J[nm + k] = (sp.Symbol(nm + k), d)
def jet(e):
    for k in [k for k in J if k.endswith(("_tt", "_tx", "_xx"))] + [k for k in J if k.endswith(("_t", "_x"))] + list(names):
        e = e.subs(J[k][1], J[k][0])
    return sp.expand(e)
sy = lambda k: J[k][0]
Euv = jet((E[(0, 0)] - E[(1, 1)]) / 4)
Ett = jet(E[(2, 2)] * sp.exp(-2 * A))
Eth = jet(E[(3, 3)] * sp.exp(A) / r**2)
Euu = jet((E[(0, 0)] - 2 * E[(0, 1)] + E[(1, 1)]) / 4)
Evv = jet((E[(0, 0)] + 2 * E[(0, 1)] + E[(1, 1)]) / 4)
print("E_uu second derivatives present:", sorted(str(s) for s in Euu.free_symbols if str(s).endswith(("_tt", "_tx", "_xx"))))
tt = [sy("S_tt"), sy("A_tt"), sy("r_tt")]
sol = sp.solve([Euv, Ett, Eth], tt, dict=True)[0]
rhs = [sp.expand(sp.simplify(sol[v])) for v in tt]
m = sp.Symbol("m")
mdef = (sy("r") / 2) * (1 + sp.exp(-2 * sy("S")) * (sy("r_t")**2 - sy("r_x")**2))
# m_u, m_v from the definition, then reduce by E_uu / E_vv and the evolution equations
def dtot(e, d):  # total derivative of a jet expression: d = 't' or 'x'
    out = 0
    for nm in names:
        out += sp.diff(e, sy(nm)) * sy(nm + "_" + d)
        out += sp.diff(e, sy(nm + "_t")) * sy(nm + ("_tt" if d == "t" else "_tx"))
        out += sp.diff(e, sy(nm + "_x")) * sy(nm + ("_tx" if d == "t" else "_xx"))
    return out
sub_tt = dict(zip(tt, rhs))
mt, mx = dtot(mdef, "t").subs(sub_tt), dtot(mdef, "x")
mu, mv = sp.expand((mt - mx) / 2), sp.expand((mt + mx) / 2)
Cu, Cv = sp.expand(Euu.subs(sub_tt)), sp.expand(Evv.subs(sub_tt))
al = sp.symbols("al")
def reduce(mm, C):
    a = sp.solve(sp.diff(mm - al * C, sy("r_xx")), al)[0]
    red = sp.simplify(mm - a * C)
    left = sorted(str(s) for s in red.free_symbols if str(s).endswith(("_tt", "_tx", "_xx")))
    return sp.expand(red), a, left
mu_r, au, lu = reduce(mu, Cu)
mv_r, av, lv = reduce(mv, Cv)
print("m_u reduced, multiplier", au, "second derivatives left", lu)
print("m_v reduced, multiplier", av, "second derivatives left", lv)
mx_first = sp.simplify(mv_r - mu_r)
print("m_x =", mx_first)
# mass substitution in the evolution: r_x^2 = r_t^2 + e^{2S}(1 - 2m/r)
rx2 = sy("r_t")**2 + sp.exp(2 * sy("S")) * (1 - 2 * m / sy("r"))
rhs_m = [sp.expand(sp.simplify(sp.expand(e).subs(sy("r_x")**2, rx2))) for e in rhs]
for v, e in zip(tt, rhs_m):
    print(v, "=", e)
pickle.dump(dict(rhs=rhs, rhs_m=rhs_m, mx=mx_first, mdef=mdef, Cu=Cu, Cv=Cv,
                 syms=[chi, m] + [J[k][0] for k in J if not k.endswith("_tt")]), open("dneqE.pkl", "wb"))

# Kretschmann in the Einstein-frame variables, second tau-derivatives by the evolution, r_x^2 by the mass
K = 0
for a in range(n):
    for b in range(n):
        for c in range(n):
            for d in range(c + 1, n):
                rr = (sp.diff(G[a][d][b], X[c]) - sp.diff(G[a][c][b], X[d])
                      + sum(G[a][c][e] * G[e][d][b] - G[a][d][e] * G[e][c][b] for e in range(n)))
                if rr != 0:
                    K += 2 * rr**2 * g[a, a] * gi[b, b] * gi[c, c] * gi[d, d]
Kj = jet(K.subs(th, sp.pi / 3)).subs(dict(zip(tt, rhs_m)))
Kj = sp.expand(Kj).subs(sy("r_x")**2, rx2)
pickle.dump(dict(rhs=rhs, rhs_m=rhs_m, mx=mx_first, mdef=mdef, Cu=Cu, Cv=Cv, K=Kj,
                 syms=[chi, m] + [J[k][0] for k in J if not k.endswith("_tt")]), open("dneqE.pkl", "wb"))
print("K ops", sp.count_ops(Kj))
