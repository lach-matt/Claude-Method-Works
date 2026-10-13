"""Pure harmonic time for the interior (item 367 step 2; LITERATURE-366 L2-L3): the gauge source h^s = -R(s) Fbar^s,
h^x = 0, so that xi~^s = xi^s - h^s = g^bc Gamma^s_bc = -box s once R = 1: the reference metric's pull on the slicing is
removed and s becomes a harmonic time (Alcubierre's f = 1: N proportional to sqrt(gamma) along the normals), marginally
singularity avoiding (Garfinkle gr-qc/0110013: harmonic time runs to infinity as the singularity is approached).  The
x-gauge keeps the reference metric.  R(s) is the C^1 ramp of interior_gauge.py.  h is algebraic in the metric (no
derivatives), so the principal part is unchanged; the Einstein-DeTurck tensor gains + nabla_(a h_b), first order.  Also
generated: the damping's action on h (to be subtracted, so the damping acts on xi~) and h^s itself.  Normalised as
gen_eqs_fw's components."""
import sympy as sp, pickle, time
t0 = time.time()
tau, s, x, th, ph = sp.symbols("tau s x theta phi", real=True)
bt = sp.Symbol("bt", positive=True)
kap, at = sp.symbols("kap at", real=True)
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

def inverse(G):
    Gi = sp.zeros(5, 5)
    Gi[0, 0] = 1 / G[0, 0]; Gi[3, 3] = 1 / G[3, 3]; Gi[4, 4] = 1 / G[4, 4]
    det = G[1, 1] * G[2, 2] - G[1, 2]**2
    Gi[1, 1], Gi[2, 2], Gi[1, 2], Gi[2, 1] = G[2, 2] / det, G[1, 1] / det, -G[1, 2] / det, -G[1, 2] / det
    return Gi

def christ(Gm, Gmi):
    return [[[sum(Gmi[a, d] * (sp.diff(Gm[d, b], X[c]) + sp.diff(Gm[d, c], X[b]) - sp.diff(Gm[b, c], X[d]))
                  for d in range(5)) / 2 for c in range(5)] for b in range(5)] for a in range(5)]

G = metric(*[fn[n] for n in names]); Gi = inverse(G)
N = 1 / sp.sqrt(-Gi[1, 1])
Gb = metric(1, 1, 1, 1, 0); Gbi = inverse(Gb)
GamB = christ(Gb, Gbi)
Fbar_s = sum(Gi[p, q] * GamB[1][p][q] for p in range(5) for q in range(5))
Rr = sp.Function("R")(s)
hs = -Rr * Fbar_s
h_up = [0, hs, 0, 0, 0]
h_low = [sum(G[a, b] * h_up[b] for b in range(5)) for a in range(5)]
Gam = christ(G, Gi)
print("christoffel", time.time() - t0, flush=True)
def nab(a, b):
    return (sp.diff(h_low[b], X[a]) + sp.diff(h_low[a], X[b])) / 2 - sum(Gam[c][a][b] * h_low[c] for c in range(5))
# the damping on h: gen_damp_fw.py's unit normal, future directed (decreasing s), tilted toward the bulk
sh = -at * x**2; ch = sp.sqrt(1 + sh**2)
w_low = [0, G[1, 2] / sp.sqrt(G[2, 2]), sp.sqrt(G[2, 2]), 0, 0]
n_low = [ch * (N if a == 1 else 0) + sh * w_low[a] for a in range(5)]
ndoth = sum(n_low[a] * h_up[a] for a in range(5))
rep = {}
for n in names:
    h = fn[n]
    for tag, d in (("_ss", sp.diff(h, s, 2)), ("_xx", sp.diff(h, x, 2)), ("_sx", sp.diff(h, s, x)),
                   ("_s", sp.diff(h, s)), ("_x", sp.diff(h, x))):
        rep[d] = sp.Symbol(n + tag)
    rep[h] = sp.Symbol(n)
rep[sp.diff(Rr, s)] = sp.Symbol("R_s"); rep[Rr] = sp.Symbol("R")
order = sorted(rep, key=lambda q: -sp.count_ops(q))
Rp = lambda e: e.subs({d: rep[d] for d in order}).subs(th, sp.pi / 3)
out, dh = {}, {}
for k, (a, b) in {"tt": (0, 0), "ss": (1, 1), "xx": (2, 2), "sx": (1, 2), "thth": (3, 3)}.items():
    nrm = G[a, b] if a == b else 1 / (f**3 * Dl**2)
    out[k] = Rp(nab(a, b) / nrm)
    dh[k] = Rp(kap * ((n_low[a] * h_low[b] + n_low[b] * h_low[a]) / 2 - G[a, b] * ndoth / 3) / nrm)
    print(k, time.time() - t0, flush=True)
aux = {"hs": Rp(hs), "N": Rp(N), "Fbar_s": Rp(Fbar_s)}
pickle.dump({"D": {k: sp.srepr(v) for k, v in out.items()}, "DH": {k: sp.srepr(v) for k, v in dh.items()},
             "aux": {k: sp.srepr(v) for k, v in aux.items()}}, open("harm_fw.pkl", "wb"))
print("done", time.time() - t0)
