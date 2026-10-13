"""Figueras-Wiseman's RSII large hole (1105.2558, ansatz (9)) in s = r^2 and x, ell = 1: the Einstein-DeTurck tensor,
the DeTurck norm, and the brane conditions at x = 1 (vacuum Israel K_ab = gamma_ab for the outward normal, xi^x = 0;
F = 0 is imposed directly).  Delta = 1/bt + (1 - x^2)/(1 - s): FLW's z shifted by the brane depth 1/bt."""
import sympy as sp, pickle, time
t0 = time.time()
tau, s, x, th, ph = sp.symbols("tau s x theta phi", real=True)
bt = sp.Symbol("bt", positive=True)
X = [tau, s, x, th, ph]
names = ["T", "S", "A", "B", "F"]
fn = {n: sp.Function(n)(s, x) for n in names}
f = 1 - s; g = 2 - x**2; Dl = 1 / bt + (1 - x**2) / f

def metric(T, S, A, B, F):
    G = sp.zeros(5, 5)
    G[0, 0] = s * T / Dl**2
    G[1, 1] = A / (f**4 * s) / Dl**2
    G[2, 2] = 4 * B / (f**2 * g) / Dl**2
    G[1, 2] = G[2, 1] = x * F / (2 * f**3) / Dl**2
    G[3, 3] = x**2 * g * S / f**2 / Dl**2
    G[4, 4] = G[3, 3] * sp.sin(th)**2
    return G

def christoffel(G):
    Gi = G.inv()
    return [[[sp.simplify(sum(Gi[a, d] * (sp.diff(G[d, b], X[c]) + sp.diff(G[d, c], X[b]) - sp.diff(G[b, c], X[d]))
                              for d in range(5)) / 2) for c in range(5)] for b in range(5)] for a in range(5)], Gi

G = metric(*[fn[n] for n in names]); Gb = metric(1, 1, 1, 1, 0)
Gam, Gi = christoffel(G); Gamb, _ = christoffel(Gb)
print("christoffel", time.time() - t0, flush=True)
def ricci(b, c):
    return sum(sp.diff(Gam[a][b][c], X[a]) - sp.diff(Gam[a][b][a], X[c])
               + sum(Gam[a][a][d] * Gam[d][b][c] - Gam[a][c][d] * Gam[d][b][a] for d in range(5)) for a in range(5))
xi_up = [sum(Gi[p, q] * (Gam[m][p][q] - Gamb[m][p][q]) for p in range(5) for q in range(5)) for m in range(5)]
xi = [sum(G[m, n] * xi_up[n] for n in range(5)) for m in range(5)]
def nabla_xi(m, n):
    return sp.diff(xi[n], X[m]) - sum(Gam[k][m][n] * xi[k] for k in range(5))
rep = {}
for n in names:
    h = fn[n]
    for tag, d in (("_ss", sp.diff(h, s, 2)), ("_xx", sp.diff(h, x, 2)), ("_sx", sp.diff(h, s, x)),
                   ("_s", sp.diff(h, s)), ("_x", sp.diff(h, x))):
        rep[d] = sp.Symbol(n + tag)
    rep[h] = sp.Symbol(n)
order = sorted(rep, key=lambda q: -sp.count_ops(q))
R = lambda e: e.subs({d: rep[d] for d in order}).subs(th, sp.pi / 3)
out = {}
for k, (a, b) in {"tt": (0, 0), "ss": (1, 1), "xx": (2, 2), "sx": (1, 2), "thth": (3, 3)}.items():
    e = ricci(a, b) + 4 * G[a, b] - (nabla_xi(a, b) + nabla_xi(b, a)) / 2
    nrm = G[a, b] if a == b else 1 / (f**3 * Dl**2)
    out[k] = R(e / nrm)
    print(k, time.time() - t0, flush=True)
phi = sum(R(G[m, k]) * R(xi_up[m]) * R(xi_up[k]) for m in range(5) for k in range(5))
# brane conditions: outward unit normal n_M = N delta^x_M, N = 1/sqrt(g^xx); K_ab = -N Gamma^x_ab
N = 1 / sp.sqrt(Gi[2, 2])
bc = {}
for k, (a, b) in {"Ktt": (0, 0), "Kss": (1, 1), "Kthth": (3, 3)}.items():
    K = -N * Gam[2][a][b]
    bc[k] = R((K - G[a, b]) / G[a, b])
bc["xix"] = R(xi_up[2])
pickle.dump({"E": {k: sp.srepr(v) for k, v in out.items()}, "phi": sp.srepr(phi),
             "bc": {k: sp.srepr(v) for k, v in bc.items()}}, open("eqs_fw.pkl", "wb"))
print("done", time.time() - t0)
