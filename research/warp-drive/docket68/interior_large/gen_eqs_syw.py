"""FLW's ansatz in s = r^2, y = x^2 (ell = R0 = 1): the Einstein-DeTurck tensor, valid as formal expressions for s of
either sign (the static metric's field equations for the functions do not see tau -> i t)."""
import sympy as sp, pickle, time
t0 = time.time()
tau, s, y, th, ph = sp.symbols("tau s y theta phi", real=True)
X = [tau, s, y, th, ph]
names = ["T", "W", "A", "B", "F"]
fn = {n: sp.Function(n)(s, y) for n in names}
f = 1 - s; g = 2 - y; z = (1 - y) / f

def metric(T, W, A, B, F):
    G = sp.zeros(5, 5)
    G[0, 0] = s * T / z**2
    G[1, 1] = A / (f**4 * s) / z**2
    G[2, 2] = B / (y * f**2 * g) / z**2
    G[1, 2] = G[2, 1] = F / (4 * f**3) / z**2
    G[3, 3] = y * g * (B + y * W) / f**2 / z**2
    G[4, 4] = G[3, 3] * sp.sin(th)**2
    return G

def christoffel(G):
    Gi = G.inv()
    return [[[sp.simplify(sum(Gi[a, d] * (sp.diff(G[d, b], X[c]) + sp.diff(G[d, c], X[b]) - sp.diff(G[b, c], X[d]))
                              for d in range(5)) / 2) for c in range(5)] for b in range(5)] for a in range(5)], Gi

G = metric(*[fn[n] for n in names]); Gb = metric(1, 0, 1, 1, 0)
Gam, Gi = christoffel(G); Gamb, _ = christoffel(Gb)
print("christoffel", time.time() - t0, flush=True)
def ricci(b, c):
    return sum(sp.diff(Gam[a][b][c], X[a]) - sp.diff(Gam[a][b][a], X[c])
               + sum(Gam[a][a][d] * Gam[d][b][c] - Gam[a][c][d] * Gam[d][b][a] for d in range(5)) for a in range(5))
xi_up = [sum(Gi[p, q] * (Gam[m][p][q] - Gamb[m][p][q]) for p in range(5) for q in range(5)) for m in range(5)]
xi = [sum(G[m, n] * xi_up[n] for n in range(5)) for m in range(5)]
def nabla_xi(m, n):
    return sp.diff(xi[n], X[m]) - sum(Gam[k][m][n] * xi[k] for k in range(5))
comps = {"tt": (0, 0), "ss": (1, 1), "yy": (2, 2), "sy": (1, 2), "thth": (3, 3)}
rep = {}
for n in names:
    h = fn[n]
    for tag, d in (("_ss", sp.diff(h, s, 2)), ("_yy", sp.diff(h, y, 2)), ("_sy", sp.diff(h, s, y)),
                   ("_s", sp.diff(h, s)), ("_y", sp.diff(h, y))):
        rep[d] = sp.Symbol(n + tag)
    rep[h] = sp.Symbol(n)
order = sorted(rep, key=lambda q: -sp.count_ops(q))
out = {}
for k, (a, b) in comps.items():
    e = ricci(a, b) + 4 * G[a, b] - (nabla_xi(a, b) + nabla_xi(b, a)) / 2
    # mixed-index normalisation: divide by the metric's own component (sqrt of the diagonal pair for sy)
    nrm = G[a, b] if a == b else sp.sqrt(G[1, 1] * G[2, 2])
    e = (e / nrm).subs({d: rep[d] for d in order}).subs(th, sp.pi / 3)
    out[k] = e
    print(k, time.time() - t0, flush=True)
xi_s = [xx.subs({d: rep[d] for d in order}).subs(th, sp.pi / 3) for xx in xi_up]
phi = sum(G[m, k].subs({d: rep[d] for d in order}).subs(th, sp.pi / 3) * xi_s[m] * xi_s[k]
          for m in range(5) for k in range(5))
pickle.dump({"E": {k: sp.srepr(v) for k, v in out.items()}, "phi": sp.srepr(phi)}, open("eqs_syw.pkl", "wb"))
print("done", time.time() - t0)
