import sympy as sp, pickle
tau, r, x, th, ph = sp.symbols("tau r x theta phi", real=True)
X = [tau, r, x, th, ph]
names = ["T", "S", "A", "B", "F"]
fn = {n: sp.Function(n)(r, x) for n in names}
f = 1 - r**2; g = 2 - x**2; z = (1 - x**2) / f
def metric(T, S, A, B, F):
    G = sp.zeros(5, 5)
    G[0, 0] = r**2 * T / z**2; G[1, 1] = 4 * A / f**4 / z**2; G[2, 2] = 4 * B / (f**2 * g) / z**2
    G[1, 2] = G[2, 1] = r * x * F / f**3 / z**2; G[3, 3] = x**2 * g * S / f**2 / z**2; G[4, 4] = G[3, 3] * sp.sin(th)**2
    return G
def chris(G):
    Gi = G.inv()
    return [[[sum(Gi[a, d] * (sp.diff(G[d, b], X[c]) + sp.diff(G[d, c], X[b]) - sp.diff(G[b, c], X[d])) for d in range(5)) / 2
              for c in range(5)] for b in range(5)] for a in range(5)], Gi
G = metric(*[fn[n] for n in names]); Gb = metric(1, 1, 1, 1, 0)
Gam, Gi = chris(G); Gamb, _ = chris(Gb)
xi = [sp.simplify(sum(Gi[p, q] * (Gam[m][p][q] - Gamb[m][p][q]) for p in range(5) for q in range(5))) for m in range(5)]
phi = sum(G[m, k] * xi[m] * xi[k] for m in range(5) for k in range(5))
rep = {}
for n in names:
    h = fn[n]
    for tag, d in (("_r", sp.diff(h, r)), ("_x", sp.diff(h, x))):
        rep[d] = sp.Symbol(n + tag)
    rep[h] = sp.Symbol(n)
phi = phi.subs({d: rep[d] for d in sorted(rep, key=lambda q: -sp.count_ops(q))}).subs(th, sp.pi / 3)
pickle.dump(sp.srepr(phi), open("phi.pkl", "wb")); print("ok", phi.free_symbols)
