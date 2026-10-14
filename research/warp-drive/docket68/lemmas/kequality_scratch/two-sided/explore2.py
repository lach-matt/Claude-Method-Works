import sympy as sp
u, L, mu, rho = sp.symbols('u L mu rho', positive=True)
A = 1 + u/L**2
s = sp.sqrt(1 + 8*A + 16*A*u)
mu_ours = u*((4*A-1)+s)/(8*A); lam_ours = ((4*A-1)+s)/(4*sp.sqrt(A*u))
# RS at ell_s: lam = 2 -> claim u = L^2/(L^2-1), mu = u
uc = L**2/(L**2-1)
print(sp.simplify(lam_ours.subs(u, uc).subs(L, 2)), sp.simplify(mu_ours.subs(u,uc).subs(L,3) - uc.subs(L,3)))
print(sp.simplify(sp.radsimp(lam_ours.subs(u, uc))))
# RS at ell_1: lam = 2/L, L<1
import mpmath as mp
for Lv in [0.3, 0.5, 0.8, 0.95]:
    f = sp.lambdify(u, lam_ours.subs(L, Lv) - 2/Lv, 'mpmath')
    try:
        r = mp.findroot(f, 1.0)
        print(Lv, r, sp.N(mu_ours.subs({L:Lv, u: r})))
    except Exception as e: print(Lv, 'fail', e)
