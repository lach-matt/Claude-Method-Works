"""Constraint damping for the interior evolution of FW's RSII hole: D_ab = kap [n_(a xi_b) - (1/3) g_ab n.xi], added to
the Einstein-DeTurck tensor R_ab + 4 g_ab - nabla_(a xi_b).  n is unit timelike and future directed (decreasing s),
tilted in the (s, x) plane by sinh(eta) = -at x^2 toward the bulk; then at the brane Codazzi gives the constraint the
Robin condition d_x xi_s = (2 Gamma^s_xs + kap n_x) xi_s, below the zero-mode threshold for kap at > 0.  With
1 + rho = 2/3 the principal constraint system is triangular and damped for kap > 0 in five dimensions.  No second
derivatives enter, so the coefficient matrix of the second s-derivatives is unchanged."""
import sympy as sp, pickle, time
t0 = time.time()
tau, s, x, th, ph = sp.symbols("tau s x theta phi", real=True)
bt = sp.Symbol("bt", positive=True); kap, at = sp.symbols("kap at", real=True)
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

def contracted(G):
    """g^pq Gamma^m_pq = -d_p g^pm - (1/2) g^pm d_p ln|det g|, for the block-diagonal metric"""
    Gi = sp.zeros(5, 5)
    Gi[0, 0] = 1 / G[0, 0]; Gi[3, 3] = 1 / G[3, 3]; Gi[4, 4] = 1 / G[4, 4]
    blk = sp.Matrix([[G[1, 1], G[1, 2]], [G[2, 1], G[2, 2]]]); bi = blk.inv()
    Gi[1, 1], Gi[1, 2], Gi[2, 1], Gi[2, 2] = bi[0, 0], bi[0, 1], bi[1, 0], bi[1, 1]
    lndet = sp.log(G[0, 0]**2) / 2 + sp.log(blk.det()**2) / 2 + sp.log(G[3, 3]**2) / 2 + sp.log(G[4, 4]**2) / 2
    out = []
    for m in range(5):
        out.append(-sum(sp.diff(Gi[p, m], X[p]) for p in range(5))
                   - sum(Gi[p, m] * sp.diff(lndet, X[p]) for p in range(5)) / 2)
    return out, Gi

G = metric(*[fn[n] for n in names]); Gb = metric(1, 1, 1, 1, 0)
cG, Gi = contracted(G); cB, Gbi = contracted(Gb)
# xi^m = g^pq (Gamma^m_pq - Gammabar^m_pq); g^pq Gammabar^m_pq = g^pq Gbar_mk^-1... computed from the reference's own
# Christoffels contracted with the evolved inverse metric
def christ(Gm, Gmi):
    return [[[sum(Gmi[a, d] * (sp.diff(Gm[d, b], X[c]) + sp.diff(Gm[d, c], X[b]) - sp.diff(Gm[b, c], X[d]))
                  for d in range(5)) / 2 for c in range(5)] for b in range(5)] for a in range(5)]
GamB = christ(Gb, Gbi)
xi_up = [cG[m] - sum(Gi[p, q] * GamB[m][p][q] for p in range(5) for q in range(5)) for m in range(5)]
xi = [sum(G[m, k] * xi_up[k] for k in range(5)) for m in range(5)]
print("xi", time.time() - t0, flush=True)
# n: unit, future directed (n^s < 0), tilted: n_a = cosh(eta) N delta^s_a + sinh(eta) w_a, w^a = delta^a_x / sqrt(g_xx)
sh = -at * x**2; ch = sp.sqrt(1 + sh**2)
N = 1 / sp.sqrt(-Gi[1, 1])
w_low = [0, G[1, 2] / sp.sqrt(G[2, 2]), sp.sqrt(G[2, 2]), 0, 0]
n_low = [ch * (N if a == 1 else 0) + sh * w_low[a] for a in range(5)]
ndotxi = sum(n_low[a] * xi_up[a] for a in range(5))
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
    D = kap * ((n_low[a] * xi[b] + n_low[b] * xi[a]) / 2 - G[a, b] * ndotxi / 3)
    nrm = G[a, b] if a == b else 1 / (f**3 * Dl**2)
    out[k] = R(D / nrm)
    print(k, time.time() - t0, flush=True)
xs = {"xi_s": R(xi_up[1]), "xi_x": R(xi_up[2]), "ndotxi": R(ndotxi)}
pickle.dump({"D": {k: sp.srepr(v) for k, v in out.items()}, "aux": {k: sp.srepr(v) for k, v in xs.items()}},
            open("damp_fw.pkl", "wb"))
print("done", time.time() - t0)
