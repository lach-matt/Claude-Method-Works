"""Item 367 step 3 (LITERATURE-366 L9): the AdS4 C-metric brane hole of Emparan, Horowitz and Myers (hep-th/9911043;
Emparan, Frassino and Way 2007.15999 eqs. (2.1)-(2.3), flat brane, kappa = 1, ell = 1), put in the chart of FW's
ansatz so that the interior pipeline built for the RSII hole runs on it unchanged.

Exact metric: ds^2 = (1 + xc r)^-2 [-H dt^2 + dr^2/H + r^2 (dxc^2/G + G dphi^2)], H = 1 - mu/r, G = 1 - xc^2 - mu xc^3,
brane xc = 0 (umbilic), axis xc = x1 (G(x1) = 0), horizon r = mu, singularity r = 0.  With f = mu/r = 1 - s,
tau = t/mu (Euclidean, period 4 pi), xc = x1 (1 - x^2) and phi = 2 psi/P1 (psi period 2 pi) it reads
    ds^2 = Dl^-2 [s dtau^2 + ds^2/(f^4 s) + c0 (dx^2/p + x^2 p dpsi^2)/f^2],  Dl = 1/mu + xc/f,
with G = (x1 - xc) P(xc), P1 = P(x1) = -G'(x1), p = P/P1, c0 = 4 x1/P1: FW's ansatz (9) one dimension down (S^2 -> S^1),
axis x = 0 and brane x = 1 as there.  The parameter is x1 (rational), so mu = (1 - x1^2)/x1^3 is rational too.

The reference metric is this one deformed, so that the Einstein-DeTurck solution is the C-metric in a gauge that is not
its own chart: p_ref = p (1 + a w x^2), Dl_ref = 1/mu + xc (1 + b w x^2)/f, w = 2 f/(1 + f) (zero at infinity s = 1,
one on the horizon, two at the singularity), with a = ca eps and b = cb eps.  An optional fifth argument k makes it
w = 2 f^k/(1 + f^k): with k = 1 the deformation dies at infinity only as f, the order at which the C-metric's mass
sits in this chart (H = s); k = 3 keeps the reference's asymptotic data through that order.  The amplitude eps is the
symbol bt of the RSII code (bt does not otherwise enter here), so one pickle serves every eps and Newton can continue
in it; eps = 0 is the exact chart (T = S = A = B = 1, F = 0).  Ansatz:
    g = Dl_ref^-2 [s T dtau^2 + A ds^2/(f^4 s) + c0 B dx^2/(f^2 p_ref) + x F ds dx/f^3 + c0 x^2 p_ref S dpsi^2/f^2].

Written (keys as gen_eqs_fw's, "thth" carrying psi psi, so core_fw.py and the interior classes read them unchanged):
eqs_<tag>.pkl (E_ab = R_ab + 3 g_ab - nabla_(a xi_b), phi, brane rows, the metric's components), damp_<tag>.pkl
(kap [n_(a xi_b) - (1/2) g n.xi]:
the triangular choice 1 + rho = 2/(D - 2) is 1/2 in four dimensions, 1/3 in five), harm_<tag>.pkl (pure harmonic time,
gen_harm_fw.py's h^s = -R Fbar^s with the four-dimensional damping on h) and kretsch_<tag>.pkl.
Usage: gen_eqs_cm.py tag x1 ca cb [k]    e.g. gen_eqs_cm.py cm23 2/3 1 1, or gen_eqs_cm.py cm23w3 2/3 1 1 3"""
import sympy as sp, pickle, time, itertools, sys
t0 = time.time()
tag = sys.argv[1]; x1, ca, cb = (sp.Rational(v) for v in sys.argv[2:5])
kw = int(sys.argv[5]) if len(sys.argv) > 5 else 1     # k > 1: Christoffels unsimplified (simplify, cancel stall)
tau, s, x, ps = sp.symbols("tau s x psi", real=True)
bt = sp.Symbol("bt", positive=True); a_, b_ = ca * bt, cb * bt
kap, at = sp.symbols("kap at", real=True)
X = [tau, s, x, ps]; D = 4
names = ["T", "S", "A", "B", "F"]
fn = {n: sp.Function(n)(s, x) for n in names}
mu = (1 - x1**2) / x1**3
P = lambda q: mu * q**2 + (mu * x1 + 1) * q + (mu * x1**2 + x1)
P1 = P(x1); assert sp.simplify(P1 - (3 * mu * x1**2 + 2 * x1)) == 0
q_ = sp.Symbol("q"); assert sp.expand((x1 - q_) * P(q_) - (1 - q_**2 - mu * q_**3)) == 0
f = 1 - s; xc = x1 * (1 - x**2); c0 = 4 * x1 / P1; w = 2 * f**kw / (1 + f**kw)
p = sp.expand(P(xc) / P1)
pr = p * (1 + a_ * w * x**2); Dl = 1 / mu + xc * (1 + b_ * w * x**2) / f

def metric(T, S, A, B, F):
    G = sp.zeros(4, 4)
    G[0, 0] = s * T / Dl**2
    G[1, 1] = A / (f**4 * s) / Dl**2
    G[2, 2] = c0 * B / (f**2 * pr) / Dl**2
    G[1, 2] = G[2, 1] = x * F / (2 * f**3) / Dl**2
    G[3, 3] = c0 * x**2 * pr * S / f**2 / Dl**2
    return G

def inverse(G):
    Gi = sp.zeros(4, 4)
    Gi[0, 0] = 1 / G[0, 0]; Gi[3, 3] = 1 / G[3, 3]
    det = G[1, 1] * G[2, 2] - G[1, 2]**2
    Gi[1, 1], Gi[2, 2], Gi[1, 2], Gi[2, 1] = G[2, 2] / det, G[1, 1] / det, -G[1, 2] / det, -G[1, 2] / det
    return Gi

def christ(Gm, Gmi, simp=False):
    out = [[[sum(Gmi[a, d] * (sp.diff(Gm[d, b], X[c]) + sp.diff(Gm[d, c], X[b]) - sp.diff(Gm[b, c], X[d]))
                 for d in range(4)) / 2 for c in range(4)] for b in range(4)] for a in range(4)]
    return [[[sp.simplify(e) if simp and kw == 1 else e for e in r2] for r2 in r1] for r1 in out]

G = metric(*[fn[n] for n in names]); Gi = inverse(G)
Gb = metric(1, 1, 1, 1, 0); Gbi = inverse(Gb)
Gam = christ(G, Gi, True); GamB = christ(Gb, Gbi, True)
print("christoffel", time.time() - t0, flush=True)
def ricci(b, c):
    return sum(sp.diff(Gam[a][b][c], X[a]) - sp.diff(Gam[a][b][a], X[c])
               + sum(Gam[a][a][d] * Gam[d][b][c] - Gam[a][c][d] * Gam[d][b][a] for d in range(4)) for a in range(4))
xi_up = [sum(Gi[p_, q] * (Gam[m][p_][q] - GamB[m][p_][q]) for p_ in range(4) for q in range(4)) for m in range(4)]
xi = [sum(G[m, n] * xi_up[n] for n in range(4)) for m in range(4)]
def nabla_sym(v, m, n):
    return (sp.diff(v[n], X[m]) + sp.diff(v[m], X[n])) / 2 - sum(Gam[k][m][n] * v[k] for k in range(4))
rep = {}
for n in names:
    h = fn[n]
    for tg, d in (("_ss", sp.diff(h, s, 2)), ("_xx", sp.diff(h, x, 2)), ("_sx", sp.diff(h, s, x)),
                  ("_s", sp.diff(h, s)), ("_x", sp.diff(h, x))):
        rep[d] = sp.Symbol(n + tg)
    rep[h] = sp.Symbol(n)
Rr = sp.Function("R")(s)
rep[sp.diff(Rr, s)] = sp.Symbol("R_s"); rep[Rr] = sp.Symbol("R")
order = sorted(rep, key=lambda q: -sp.count_ops(q))
Rp = lambda e: e.subs({d: rep[d] for d in order})
COMP = {"tt": (0, 0), "ss": (1, 1), "xx": (2, 2), "sx": (1, 2), "thth": (3, 3)}
nrm = lambda a, b: G[a, b] if a == b else 1 / (f**3 * Dl**2)
E = {}
for k, (a, b) in COMP.items():
    E[k] = Rp((ricci(a, b) + 3 * G[a, b] - nabla_sym(xi, a, b)) / nrm(a, b))
    print("E", k, time.time() - t0, flush=True)
phi = sum(Rp(G[m, k]) * Rp(xi_up[m]) * Rp(xi_up[k]) for m in range(4) for k in range(4))
# brane x = 1: outward unit normal n_M = N delta^x_M, N = 1/sqrt(g^xx); K_ab = -N Gamma^x_ab; vacuum Israel K_ab = h_ab
Nx_ = 1 / sp.sqrt(Gi[2, 2])
bc = {}
for k, (a, b) in {"Ktt": (0, 0), "Kss": (1, 1), "Kthth": (3, 3)}.items():
    bc[k] = Rp((-Nx_ * Gam[2][a][b] - G[a, b]) / G[a, b])
bc["xix"] = Rp(xi_up[2])
pickle.dump({"E": {k: sp.srepr(v) for k, v in E.items()}, "phi": sp.srepr(phi),
             "bc": {k: sp.srepr(v) for k, v in bc.items()},
             "metric": {k: sp.srepr(Rp(G[i, j])) for k, (i, j) in
                        {"gtt": (0, 0), "gss": (1, 1), "gxx": (2, 2), "gsx": (1, 2), "gpp": (3, 3)}.items()},
             "meta": dict(x1=str(x1), mu=str(mu), P1=str(P1), c0=str(c0), ca=str(ca), cb=str(cb), kw=kw)},
            open("eqs_%s.pkl" % tag, "wb"))
print("eqs written", time.time() - t0, flush=True)
# damping, gen_damp_fw.py's tilted normal (sinh eta = -at x^2), coefficient 1/(D - 2)
N = 1 / sp.sqrt(-Gi[1, 1])
sh = -at * x**2; ch = sp.sqrt(1 + sh**2)
w_low = [0, G[1, 2] / sp.sqrt(G[2, 2]), sp.sqrt(G[2, 2]), 0]
n_low = [ch * (N if a == 1 else 0) + sh * w_low[a] for a in range(4)]
cD = sp.Rational(1, D - 2)
def damping(vl, vu):
    nd = sum(n_low[a] * vu[a] for a in range(4))
    return {k: Rp(kap * ((n_low[a] * vl[b] + n_low[b] * vl[a]) / 2 - cD * G[a, b] * nd) / nrm(a, b))
            for k, (a, b) in COMP.items()}, nd
DM, ndx = damping(xi, xi_up)
pickle.dump({"D": {k: sp.srepr(v) for k, v in DM.items()},
             "aux": {"xi_s": sp.srepr(Rp(xi_up[1])), "xi_x": sp.srepr(Rp(xi_up[2])), "ndotxi": sp.srepr(Rp(ndx))}},
            open("damp_%s.pkl" % tag, "wb"))
print("damp written", time.time() - t0, flush=True)
# pure harmonic time: h^s = -R(s) Fbar^s, Fbar^s = g^pq Gammabar^s_pq
Fbar_s = sum(Gi[p_, q] * GamB[1][p_][q] for p_ in range(4) for q in range(4))
hs = -Rr * Fbar_s
h_up = [0, hs, 0, 0]; h_low = [sum(G[a, b] * h_up[b] for b in range(4)) for a in range(4)]
HD = {k: Rp(nabla_sym(h_low, a, b) / nrm(a, b)) for k, (a, b) in COMP.items()}
DH, _ = damping(h_low, h_up)
pickle.dump({"D": {k: sp.srepr(v) for k, v in HD.items()}, "DH": {k: sp.srepr(v) for k, v in DH.items()},
             "aux": {"hs": sp.srepr(Rp(hs)), "N": sp.srepr(Rp(N)), "Fbar_s": sp.srepr(Rp(Fbar_s))}},
            open("harm_%s.pkl" % tag, "wb"))
print("harm written", time.time() - t0, flush=True)
# Kretschmann R_abcd R^abcd (c < d stored, factor 2)
Rm = {}
for a, b, c, d in itertools.product(range(4), repeat=4):
    if c < d:
        e = (sp.diff(Gam[a][b][d], X[c]) - sp.diff(Gam[a][b][c], X[d])
             + sum(Gam[a][c][k] * Gam[k][b][d] - Gam[a][d][k] * Gam[k][b][c] for k in range(4)))
        if e != 0:
            Rm[(a, b, c, d)] = e
Rl = {}
for (a, b, c, d) in set((a, b, c, d) for a in range(4) for (_, b, c, d) in Rm):
    e = sum(G[a, k] * Rm.get((k, b, c, d), 0) for k in range(4))
    if e != 0:
        Rl[(a, b, c, d)] = e
K = 0
for (a, b, c, d), v in Rl.items():
    up = sum(Gi[a, p_] * Gi[b, q] * Gi[c, r] * Gi[d, t] * Rl[(p_, q, r, t)]
             for (p_, q, r, t) in Rl)
    K += 2 * v * up
pickle.dump(sp.srepr(Rp(K)), open("kretsch_%s.pkl" % tag, "wb"))
print("done", time.time() - t0, flush=True)
