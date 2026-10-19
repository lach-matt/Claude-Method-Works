# KN gauge (torus frame, 2+1): which theta-derivatives of the metric functions each equation holds
import sympy as sp, time
t0 = time.time()
v, r, th = sp.symbols("v r theta", positive=True)
X = [v, r, th]
s, c = sp.sin(th), sp.cos(th)
H = r**6*s**2*c**2
A, B, C, psi, om = [sp.Function(n)(v, r, th) for n in ("A", "B", "C", "psi", "om")]   # h_vv, h_vr, h_vth
h = sp.Matrix([[A, B, C], [B, 0, 0], [C, 0, H]])
hi = sp.simplify(h.inv())
print("inverse:", [sp.simplify(hi[i, j]) for i in range(3) for j in range(i, 3)], flush=True)
n = 3
G = [[[sp.simplify(sum(hi[i, d]*(sp.diff(h[d, j], X[k]) + sp.diff(h[d, k], X[j]) - sp.diff(h[j, k], X[d])) for d in range(n))/2)
       for k in range(n)] for j in range(n)] for i in range(n)]
def Ric(j, k):
    e = 0
    for i in range(n):
        e += sp.diff(G[i][j][k], X[i]) - sp.diff(G[i][j][i], X[k])
        for d in range(n):
            e += G[i][i][d]*G[d][j][k] - G[i][k][d]*G[d][j][i]
    return sp.expand(e)
src = lambda j, k: sp.Rational(3, 2)*sp.diff(psi, X[j])*sp.diff(psi, X[k]) + 2*sp.diff(om, X[j])*sp.diff(om, X[k])
names = {(1, 1): "rr", (1, 2): "rth", (2, 2): "thth", (0, 1): "vr", (0, 2): "vth", (0, 0): "vv"}
def orders(e):
    out = {}
    for d in e.atoms(sp.Derivative):
        f = d.expr.func.__name__
        cnt = {str(x): k for x, k in d.variable_count}
        key = (f, cnt.get("v", 0), cnt.get("r", 0), cnt.get("theta", 0))
        out[key] = True
    return sorted(out)
for jk in [(1, 1), (1, 2), (2, 2), (0, 1)]:
    E = sp.together(Ric(*jk) - src(*jk))
    num = sp.expand(sp.numer(E))
    print(names[jk], "derivatives present:", orders(num), " t", round(time.time() - t0), flush=True)
