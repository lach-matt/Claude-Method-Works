# (see CHARTER.md)
# PRE-DOCKET 68 COMPUTATION (2026-10-02), not seated.  M: "what if our error is accepting that spacetime is flat?"
# corridors.py assumed a FLAT bulk (latticectc's H1).  Here: the spatially flat FRW metric
#   ds^2 = -dt^2 + a(t)^2 (dx^2 + dy^2 + dz^2),  a(t) arbitrary and non-constant.
# An identification of positions is a quotient by an isometry, so the question is which translations and boosts
# are Killing vectors of FRW.  Killing equation: L_xi g = 0, computed symbolically.
import sympy as sp
t, x, y, z = sp.symbols('t x y z', real=True)
a = sp.Function('a')(t)
X = [t, x, y, z]
g = sp.diag(-1, a**2, a**2, a**2)
def lie_g(xi):
    return sp.Matrix(4, 4, lambda m, n: sp.simplify(
        sum(xi[k]*sp.diff(g[m, n], X[k]) for k in range(4))
        + sum(g[k, n]*sp.diff(xi[k], X[m]) for k in range(4))
        + sum(g[m, k]*sp.diff(xi[k], X[n]) for k in range(4))))
cands = {
    "spatial translation d_x (corridor ends at the SAME cosmic time)": [0, 1, 0, 0],
    "rotation x d_y - y d_x": [0, -y, x, 0],
    "time translation d_t (ends at DIFFERENT cosmic times)": [1, 0, 0, 0],
    "boost x d_t + t d_x (a corridor keyed to a moving frame)": [x, t, 0, 0],
}
for name, xi in cands.items():
    L = lie_g(xi)
    print(f"{'KILLING' if L == sp.zeros(4, 4) else 'not Killing':12s} {name}" +
          ("" if L == sp.zeros(4, 4) else f"   e.g. (L g)[0,1] = {sp.simplify(L[0, 1])}, (L g)[1,1] = {sp.simplify(L[1, 1])}"))
# Control: with a(t) = 1 (flat) the boost and the time translation ARE Killing -- the test is not vacuous.
g = sp.diag(-1, 1, 1, 1)
print("control, a = 1 (Minkowski): boost Killing:", lie_g([x, t, 0, 0]) == sp.zeros(4, 4),
      "| time translation Killing:", lie_g([1, 0, 0, 0]) == sp.zeros(4, 4))
