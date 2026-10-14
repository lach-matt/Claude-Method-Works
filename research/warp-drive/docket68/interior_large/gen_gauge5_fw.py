"""A lapse driver steering one function of s (item 365, the first of C1's next steps): the gauge source
h^s = R(s) mu E(s) / N^2, h^x = 0, so that by the same identity as gen_gauge3_fw.py's driver (h^s adds N^3 h^s to
dN/d(-s)) every x is pushed at the same relative rate, d ln N/d(-s) gains mu E.  E(s) is a single number per slice,
computed from the solution (interior_gauge5.py: minus the x-mean, or the brane value, of ln(N / (Nst c(s)))); it enters
here as a function of s alone, its derivative E_s supplied the same way.  h is algebraic in the metric at each slice (no
derivatives), so the principal part is unchanged; the Einstein-DeTurck tensor gains + nabla_(a h_b), first order in the
fields.  Also generated: the damping's action on h, D(h) = kap [n_(a h_b) - (1/3) g n.h] with gen_damp_fw.py's tilted
normal, to be subtracted so that the damping acts on xi~ = xi - h; and N, with its total s-derivative N_s in terms of
the fields' s-derivatives.  Normalised as gen_eqs_fw's components."""
import sympy as sp, pickle, time
t0 = time.time()
tau, s, x, th, ph = sp.symbols("tau s x theta phi", real=True)
bt = sp.Symbol("bt", positive=True); mu = sp.Symbol("mu", real=True)
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
Rr = sp.Function("R")(s); E = sp.Function("E")(s)
hs = Rr * mu * E / N**2
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
rep[sp.diff(E, s)] = sp.Symbol("E_s"); rep[E] = sp.Symbol("E")
order = sorted(rep, key=lambda q: -sp.count_ops(q))
Rp = lambda e: e.subs({d: rep[d] for d in order}).subs(th, sp.pi / 3)
out, dh = {}, {}
for k, (a, b) in {"tt": (0, 0), "ss": (1, 1), "xx": (2, 2), "sx": (1, 2), "thth": (3, 3)}.items():
    nrm = G[a, b] if a == b else 1 / (f**3 * Dl**2)
    out[k] = Rp(nab(a, b) / nrm)
    dh[k] = Rp(kap * ((n_low[a] * h_low[b] + n_low[b] * h_low[a]) / 2 - G[a, b] * ndoth / 3) / nrm)
    print(k, time.time() - t0, flush=True)
aux = {"hs": Rp(hs), "N": Rp(N), "N_s": Rp(sp.diff(N, s))}
pickle.dump({"D": {k: sp.srepr(v) for k, v in out.items()}, "DH": {k: sp.srepr(v) for k, v in dh.items()},
             "aux": {k: sp.srepr(v) for k, v in aux.items()}}, open("gauge5_fw.pkl", "wb"))
print("done", time.time() - t0)
