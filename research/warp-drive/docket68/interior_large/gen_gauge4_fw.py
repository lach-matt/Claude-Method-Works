"""A lapse driver (wF weights the cancellation of the reference pull; wF = 0 keeps it), ramped in by R(s) (C^1,
zero at the switch with its derivative), for the interior: the gauge source h^s = -wF Fbar^s + mu (Nst c(s) - N)/N^3
added to the DeTurck vector,
xi~ = xi - h (h^x = 0), with N = 1/sqrt(-g^ss) the lapse of the s-slices, Fbar^s = g^cd Gammabar^s_cd the reference's
contribution, and c(s) = (1 - s1)/(1 - s) so that the driver holds the lapse per unit lambda = ln(1 - s) near its value
at the switch.  h is algebraic in the metric, so the principal part and the constraint system's structure are
unchanged; the Einstein-DeTurck tensor gains + nabla_(a h_b), first order in the fields.  Nst(x) is a frozen field
(its x-derivative enters).  Normalised as gen_eqs_fw's components."""
import sympy as sp, pickle, time
t0 = time.time()
tau, s, x, th, ph = sp.symbols("tau s x theta phi", real=True)
bt = sp.Symbol("bt", positive=True); mu, s1, wF = sp.symbols("mu s1 wF", real=True)
X = [tau, s, x, th, ph]
names = ["T", "S", "A", "B", "F"]
fn = {n: sp.Function(n)(s, x) for n in names}
Nst = sp.Function("Nst")(x)
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
Gb = metric(1, 1, 1, 1, 0); Gbi = inverse(Gb)
GamB = christ(Gb, Gbi)
Fbar_s = sum(Gi[p, q] * GamB[1][p][q] for p in range(5) for q in range(5))
N = 1 / sp.sqrt(-Gi[1, 1])
cfac = (1 - s1) / (1 - s)
Rr = sp.Function("R")(s)
hs = Rr * (1 - x**2) * (-wF * Fbar_s + mu * (Nst * cfac - N) / N**3)
h_up = [0, hs, 0, 0, 0]
h_low = [sum(G[a, b] * h_up[b] for b in range(5)) for a in range(5)]
Gam = christ(G, Gi)
print("christoffel", time.time() - t0, flush=True)
def nab(a, b):
    return (sp.diff(h_low[b], X[a]) + sp.diff(h_low[a], X[b])) / 2 - sum(Gam[c][a][b] * h_low[c] for c in range(5))
rep = {}
for n in names:
    h = fn[n]
    for tag, d in (("_ss", sp.diff(h, s, 2)), ("_xx", sp.diff(h, x, 2)), ("_sx", sp.diff(h, s, x)),
                   ("_s", sp.diff(h, s)), ("_x", sp.diff(h, x))):
        rep[d] = sp.Symbol(n + tag)
    rep[h] = sp.Symbol(n)
rep[sp.diff(Nst, x)] = sp.Symbol("Nst_x"); rep[Nst] = sp.Symbol("Nst")
rep[sp.diff(Rr, s)] = sp.Symbol("R_s"); rep[Rr] = sp.Symbol("R")
order = sorted(rep, key=lambda q: -sp.count_ops(q))
R = lambda e: e.subs({d: rep[d] for d in order}).subs(th, sp.pi / 3)
out = {}
for k, (a, b) in {"tt": (0, 0), "ss": (1, 1), "xx": (2, 2), "sx": (1, 2), "thth": (3, 3)}.items():
    nrm = G[a, b] if a == b else 1 / (f**3 * Dl**2)
    out[k] = R(nab(a, b) / nrm)
    print(k, time.time() - t0, flush=True)
aux = {"hs": R(hs), "N": R(N), "Fbar_s": R(Fbar_s)}
pickle.dump({"D": {k: sp.srepr(v) for k, v in out.items()}, "aux": {k: sp.srepr(v) for k, v in aux.items()}},
            open("gauge4_fw.pkl", "wb"))
print("done", time.time() - t0)
