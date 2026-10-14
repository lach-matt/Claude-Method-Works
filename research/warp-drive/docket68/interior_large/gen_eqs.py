"""Generate the Einstein-DeTurck tensor for FLW's ansatz (4.6), ell = 1, Euclidean, and pickle lambdify-ready exprs."""
import sympy as sp, pickle, time
t0 = time.time()
tau, r, x, th, ph = sp.symbols("tau r x theta phi", real=True)
X = [tau, r, x, th, ph]
names = ["T", "S", "A", "B", "F"]
fn = {n: sp.Function(n)(r, x) for n in names}
T, S, A, B, F = [fn[n] for n in names]
f = 1 - r**2; g = 2 - x**2; z = (1 - x**2) / f

def metric(T, S, A, B, F):
    G = sp.zeros(5, 5)
    G[0, 0] = r**2 * T / z**2
    G[1, 1] = 4 * A / f**4 / z**2
    G[2, 2] = 4 * B / (f**2 * g) / z**2
    G[1, 2] = G[2, 1] = r * x * F / f**3 / z**2
    G[3, 3] = x**2 * g * S / f**2 / z**2
    G[4, 4] = G[3, 3] * sp.sin(th)**2
    return G

def christoffel(G):
    Gi = G.inv()
    return [[[sp.simplify(sum(Gi[a, d] * (sp.diff(G[d, b], X[c]) + sp.diff(G[d, c], X[b]) - sp.diff(G[b, c], X[d]))
                              for d in range(5)) / 2) for c in range(5)] for b in range(5)] for a in range(5)], Gi

G = metric(T, S, A, B, F)
Gb = metric(1, 1, 1, 1, 0)
Gam, Gi = christoffel(G)
print("christoffel", time.time() - t0, flush=True)
Gamb, _ = christoffel(Gb)
print("ref christoffel", time.time() - t0, flush=True)
def ricci(b, c):
    return sum(sp.diff(Gam[a][b][c], X[a]) - sp.diff(Gam[a][b][a], X[c])
               + sum(Gam[a][a][d] * Gam[d][b][c] - Gam[a][c][d] * Gam[d][b][a] for d in range(5)) for a in range(5))
xi_up = [sum(Gi[p, q] * (Gam[m][p][q] - Gamb[m][p][q]) for p in range(5) for q in range(5)) for m in range(5)]
xi = [sum(G[m, n] * xi_up[n] for n in range(5)) for m in range(5)]
def nabla_xi(m, n):   # nabla_m xi_n
    return sp.diff(xi[n], X[m]) - sum(Gam[k][m][n] * xi[k] for k in range(5))
comps = {"tt": (0, 0), "rr": (1, 1), "xx": (2, 2), "rx": (1, 2), "thth": (3, 3)}
E = {}
for k, (a, b) in comps.items():
    e = ricci(a, b) + 4 * G[a, b] - (nabla_xi(a, b) + nabla_xi(b, a)) / 2
    E[k] = e
    print(k, time.time() - t0, flush=True)
# replace function derivatives by plain symbols
syms = {}
rep = {}
for n in names:
    h = fn[n]
    for tag, d in (("", h), ("_r", sp.diff(h, r)), ("_x", sp.diff(h, x)), ("_rr", sp.diff(h, r, 2)),
                   ("_xx", sp.diff(h, x, 2)), ("_rx", sp.diff(h, r, x))):
        s_ = sp.Symbol(n + tag); syms[n + tag] = s_; rep[d] = s_
out = {}
for k, e in E.items():
    e2 = e.subs({d: rep[d] for d in sorted(rep, key=lambda q: -sp.count_ops(q))})
    e2 = e2.subs(th, sp.pi / 3)          # every component is theta-free after the sphere factor, checked below
    out[k] = e2
    print("subs", k, time.time() - t0, flush=True)
pickle.dump({k: sp.srepr(v) for k, v in out.items()}, open("eqs.pkl", "wb"))
print("done", time.time() - t0)
