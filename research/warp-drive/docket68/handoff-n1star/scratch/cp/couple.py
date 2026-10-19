# does the remainder of the Killing norms couple to the base-metric remainder at O(1)?  linearize box_h psi0, box_h om0
import sympy as sp
v, r, th, mu, e = sp.symbols("v r theta mu e", positive=True)
X = [v, r, th]; s, c = sp.sin(th), sp.cos(th)
rho = r**2*s*c; F = 1 - mu/r**2
a, b, cc = [sp.Function(n)(v, r, th) for n in ("a", "b", "cc")]
h = rho**2*sp.Matrix([[-F, 1, 0], [1, 0, 0], [0, 0, r**2]]) + e*sp.Matrix([[a, b, cc], [b, 0, 0], [cc, 0, 0]])
def box(h, f):
    hi = h.inv(); dt = h.det(); sq = sp.sqrt(sp.factor(-dt.subs(e, 0)/(r**14*s**6*c**6)))*r**7*s**3*c**3
    sq = sp.sqrt(-dt)  if True else sq
    sq = r**7*s**3*c**3*sp.sqrt(sp.expand(-dt/(r**14*s**6*c**6)))
    return sum(sp.diff(sq*hi[i, j]*sp.diff(f, X[j]), X[i]) for i in range(3) for j in range(3))/sq
psi0, om0 = sp.log(rho), sp.log(c/s)/2
for name, f in (("psi0", psi0), ("om0", om0)):
    b0 = sp.simplify(box(h.subs(e, 0), f))
    L = sp.simplify(sp.diff(box(h, f), e).subs(e, 0))
    print(name, "background box:", b0)
    print(name, "linear term:", sp.factor(L))
