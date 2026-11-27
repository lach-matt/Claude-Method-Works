"""The seed's derivatives in (xi, v) up to a given order, symbolically (computed, exact sympy): R_s with
R_v = f(R)/2, R_xi = (du/dxi) R_u = -a cosh(xi) f(R)/g(u), u = -1 + a sinh xi, f = 1 - R^-2, g = 1 - u^-2;
W_s = (1/2) log(f/(2g)), Omega_s^2 = f/(2g).  towers(K) returns {('R'|'W'|'O', a, b): expr in (R, xi)}."""
import sympy as sp
R, xi = sp.symbols('R xi', positive=True)
A = sp.Rational(1, 500)

def towers(K):
    u = -1 + A * sp.sinh(xi)
    f = 1 - 1 / R**2; g = 1 - 1 / u**2
    Rv = f / 2; Rxi = -A * sp.cosh(xi) * f / g
    def Dv(e): return sp.diff(e, R) * Rv
    def Dx(e): return sp.diff(e, R) * Rxi + sp.diff(e, xi)
    base = {'R': R, 'W': sp.log(f / (2 * g)) / 2, 'O': f / (2 * g)}
    out = {}
    for nm, e0 in base.items():
        col = e0
        for b in range(K + 1):
            e = col
            for a in range(K + 1 - b):
                out[(nm, a, b)] = e
                e = Dx(e)
            col = Dv(col)
    return out
