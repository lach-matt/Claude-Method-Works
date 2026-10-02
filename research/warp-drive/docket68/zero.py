# PRE-DOCKET 68 COMPUTATION (2026-10-02), not seated.  M: "redefine 0 ... a point of ground state, and anything less
# than 0 is not negative, just less than the ground state."  Moving the zero of energy by a constant everywhere is
# T_ab -> T_ab + lam * g_ab (a vacuum term; rho -> rho - lam, p -> p + lam in these signs).  Which energy conditions
# notice where the zero is?  Computed for an ARBITRARY T_ab at a point, in an orthonormal frame.
import sympy as sp
lam = sp.symbols('lambda', real=True)
g = sp.diag(-1, 1, 1, 1)
T = sp.Matrix(4, 4, lambda i, j: sp.Symbol(f"T{min(i,j)}{max(i,j)}", real=True))   # arbitrary symmetric T
Tp = T + lam*g
vx, vy, vz = sp.symbols('v_x v_y v_z', real=True)
k = sp.Matrix([1, sp.cos(vx)*sp.sin(vy), sp.sin(vx)*sp.sin(vy), sp.cos(vy)])          # every null direction
u = sp.Matrix([sp.cosh(vz), sp.sinh(vz), 0, 0])                                       # a boosted unit timelike vector
nec  = sp.simplify((k.T*Tp*k)[0] - (k.T*T*k)[0])
wec  = sp.simplify((u.T*Tp*u)[0] - (u.T*T*u)[0])
trT  = lambda M: sum(g[i, i]*M[i, i] for i in range(4))
sec  = sp.simplify(((u.T*Tp*u)[0] + trT(Tp)/2) - ((u.T*T*u)[0] + trT(T)/2))
print("NEC  T_ab k^a k^b changes by:", nec, "  (k null: g_ab k^a k^b = 0, so the zero of energy is invisible to it)")
print("WEC  T_ab u^a u^b changes by:", wec, "  (moving the zero moves every observer's energy density)")
print("SEC  (T_ab - T g_ab/2) u^a u^b changes by:", sec)
# Morris-Thorne throat (Lobo 0710.4474 eqs 26-28 as restated in D67, STANDS): rho + p_r is the NEC combination.
r, r0 = sp.symbols('r r_0', positive=True); b = sp.Function('b')(r)
rho = sp.diff(b, r)/(8*sp.pi*r**2); p_r = -b/(8*sp.pi*r**3)                           # Phi = 0
print("throat rho + p_r, before and after the shift:", sp.simplify(rho + p_r), "|", sp.simplify((rho - lam) + (p_r + lam)))
