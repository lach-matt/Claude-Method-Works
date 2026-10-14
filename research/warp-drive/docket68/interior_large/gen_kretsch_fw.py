import sympy as sp, pickle, time, itertools
t0 = time.time()
tau, s, x, th, ph = sp.symbols("tau s x theta phi", real=True)
bt = sp.Symbol("bt", positive=True)
X = [tau, s, x, th, ph]
names = ["T", "S", "A", "B", "F"]
fn = {n: sp.Function(n)(s, x) for n in names}
f = 1 - s; g = 2 - x**2; z = 1 / bt + (1 - x**2) / f
G = sp.zeros(5, 5)
T, S, A, B, F = [fn[n] for n in names]
G[0, 0] = s * T / z**2; G[1, 1] = A / (f**4 * s) / z**2; G[2, 2] = 4 * B / (f**2 * g) / z**2
G[1, 2] = G[2, 1] = x * F / (2 * f**3) / z**2; G[3, 3] = x**2 * g * S / f**2 / z**2; G[4, 4] = G[3, 3] * sp.sin(th)**2
Gi = G.inv()
Gam = [[[sp.simplify(sum(Gi[a, d] * (sp.diff(G[d, b], X[c]) + sp.diff(G[d, c], X[b]) - sp.diff(G[b, c], X[d]))
                         for d in range(5)) / 2) for c in range(5)] for b in range(5)] for a in range(5)]
print("gam", time.time() - t0, flush=True)
# R^a_{bcd}
Rm = {}
for a, b, c, d in itertools.product(range(5), repeat=4):
    if c < d:
        e = sp.diff(Gam[a][b][d], X[c]) - sp.diff(Gam[a][b][c], X[d]) + sum(Gam[a][c][k] * Gam[k][b][d] - Gam[a][d][k] * Gam[k][b][c] for k in range(5))
        if e != 0:
            Rm[(a, b, c, d)] = e
print("riem", len(Rm), time.time() - t0, flush=True)
# lower first index: R_{abcd} = g_{ae} R^e_{bcd}
Rl = {}
for (a, b, c, d) in set((a, b, c, d) for a in range(5) for (_, b, c, d) in Rm):
    e = sum(G[a, k] * Rm.get((k, b, c, d), 0) for k in range(5))
    if e != 0:
        Rl[(a, b, c, d)] = e
# raise all: K = sum R_{abcd} R^{abcd}; with c<d stored, factor 2
K = 0
for (a, b, c, d), v in Rl.items():
    up = sum(Gi[a, p] * Gi[b, q] * Gi[c, s] * Gi[d, t] * Rl.get((p, q, s, t), 0)
             for p in range(5) for q in range(5) for s in range(5) for t in range(5) if s < t and (p, q, s, t) in Rl)
    K += 2 * v * up
print("K built", time.time() - t0, flush=True)
rep = {}
for n in names:
    h = fn[n]
    for tag, dd in (("_ss", sp.diff(h, s, 2)), ("_xx", sp.diff(h, x, 2)), ("_sx", sp.diff(h, s, x)), ("_s", sp.diff(h, s)), ("_x", sp.diff(h, x))):
        rep[dd] = sp.Symbol(n + tag)
    rep[h] = sp.Symbol(n)
K = K.subs({dd: rep[dd] for dd in sorted(rep, key=lambda q: -sp.count_ops(q))}).subs(th, sp.pi / 3)
pickle.dump(sp.srepr(K), open("kretsch_fw.pkl", "wb")); print("done", time.time() - t0)
