"""The constraint damping's action on the gauge source h (gen_gauge3_fw.py): D(h)_ab = kap [n_(a h_b) - (1/3) g_ab n.h]
with gen_damp_fw.py's tilted unit normal.  Under the lapse driver the constraint is xi~ = xi - h, so the damping
must act on xi~: D(xi~) = D(xi) - D(h).  Algebraic in the fields, normalised as gen_eqs_fw's components."""
import sympy as sp, pickle, time
t0 = time.time()
tau, s, x, th, ph = sp.symbols("tau s x theta phi", real=True)
bt = sp.Symbol("bt", positive=True); kap, at = sp.symbols("kap at", real=True)
mu, s1, wF = sp.symbols("mu s1 wF", real=True)
names = ["T", "S", "A", "B", "F"]
V = {n: sp.Symbol(n) for n in names}
Nst, R = sp.Symbol("Nst"), sp.Symbol("R")
f = 1 - s; g = 2 - x**2; Dl = 1 / bt + (1 - x**2) / f
T, S, A, B, F = [V[n] for n in names]
G = sp.zeros(5, 5)
G[0, 0] = s * T / Dl**2; G[1, 1] = A / (f**4 * s) / Dl**2; G[2, 2] = 4 * B / (f**2 * g) / Dl**2
G[1, 2] = G[2, 1] = x * F / (2 * f**3) / Dl**2; G[3, 3] = x**2 * g * S / f**2 / Dl**2
G[4, 4] = G[3, 3] * sp.sin(th)**2
det = G[1, 1] * G[2, 2] - G[1, 2]**2
gi_ss = G[2, 2] / det
N = 1 / sp.sqrt(-gi_ss)
# h^s with wF = 0 (the reference pull kept): R mu (Nst c - N) / N^3
cfac = (1 - s1) / (1 - s)
hs = R * (mu * (Nst * cfac - N) / N**3)
h_up = [0, hs, 0, 0, 0]
h_low = [sum(G[a, b] * h_up[b] for b in range(5)) for a in range(5)]
sh = -at * x**2; ch = sp.sqrt(1 + sh**2)
w_low = [0, G[1, 2] / sp.sqrt(G[2, 2]), sp.sqrt(G[2, 2]), 0, 0]
n_low = [ch * (N if a == 1 else 0) + sh * w_low[a] for a in range(5)]
ndoth = sum(n_low[a] * h_up[a] for a in range(5))
out = {}
for k, (a, b) in {"tt": (0, 0), "ss": (1, 1), "xx": (2, 2), "sx": (1, 2), "thth": (3, 3)}.items():
    D = kap * ((n_low[a] * h_low[b] + n_low[b] * h_low[a]) / 2 - G[a, b] * ndoth / 3)
    nrm = G[a, b] if a == b else 1 / (f**3 * Dl**2)
    out[k] = (D / nrm).subs(th, sp.pi / 3)
pickle.dump({"D": {k: sp.srepr(v) for k, v in out.items()}}, open("damph_fw.pkl", "wb"))
print("done", time.time() - t0)
