"""Extra checks: (i) roundoff origin of M4/S6 'crossing' near y=0; (ii) Kretschmann formula from my own Riemann;
(iii) cross-check of my y_s and C-S7 depth against the owner's throat_bulk (read-only import by path)."""
import math, sys, importlib.util
import numpy as np
import sympy as sp
here = "/tmp/claude-0/-home-user-Claude-Method-Works/6d820e7d-6d3c-5ac7-8067-527dc14c2847/scratchpad/kequality/check-throat-column/"
spec = importlib.util.spec_from_file_location("cc_numeric", here + "cc_numeric.py"); N = importlib.util.module_from_spec(spec); spec.loader.exec_module(N)

print("== (i) M4 / S6 on the throat column: min over y of s2_dec - target, and where the sign is negative")
for e in (1/64, 1.0, 64.0):
    sol = N.column(e, max_step=0.002 if e < 8 else 0.0005); ys = sol.t[-1]
    yy = np.linspace(1e-6*ys, ys*(1-1e-6), 4001); A = sol.sol(yy)[2]   # at = a + e
    for nm, tg, lm in (("M4", -0.125, 0.75), ("S6", -1/3, 1/3)):
        x = 1 - A/e
        s2 = -(x - np.sqrt(x*x - 1 + lm*lm))/2
        neg = yy[(s2 - tg) < 0]
        print(f"  e={e} {nm}: min(s2-target)={np.min(s2-tg):.2e}; negative at y/y_s in {[round(v/ys,8) for v in neg[:3]]}... (count {len(neg)}); max |a+e|/e there = {np.max(np.abs(A[(s2-tg)<0]))/e if len(neg) else 0:.1e}")

print("== (ii) Kretschmann from own Riemann tensor vs the pair-sum formula")
t, r, y, th, ph = sp.symbols("t r y theta phi", real=True)
al = sp.Function("alpha")(y); be = sp.Function("beta")(y)
X = [t, r, y, th, ph]
g = sp.diag(-al**2*(1 + r**2/4), al**2/(1 + r**2/4), 1, 4*be**2, 4*be**2*sp.sin(th)**2)
gi = g.inv(); n = 5
Gam = [[[sp.simplify(sum(gi[a, d]*(sp.diff(g[d, b], X[c]) + sp.diff(g[d, c], X[b]) - sp.diff(g[b, c], X[d])) for d in range(n))/2) for c in range(n)] for b in range(n)] for a in range(n)]
def Riem(a, b, c, d):  # R^a_{bcd}
    v = sp.diff(Gam[a][b][d], X[c]) - sp.diff(Gam[a][b][c], X[d])
    v += sum(Gam[a][c][k]*Gam[k][b][d] - Gam[a][d][k]*Gam[k][b][c] for k in range(n))
    return v
Rud = {}
for a in range(n):
    for b in range(n):
        for c in range(n):
            for d in range(c+1, n):
                val = sp.simplify(Riem(a, b, c, d))
                if val != 0:
                    Rud[(a, b, c, d)] = val
# lower first index; metric diagonal
Rdddd = {k: sp.simplify(g[k[0], k[0]]*v) for k, v in Rud.items()}
K = 0
for (a, b, c, d), v in Rdddd.items():
    # R_abcd R^abcd with antisymmetry in (c,d): factor 2 for d<c counterpart
    K += 2*v**2*gi[a, a]*gi[b, b]*gi[c, c]*gi[d, d]
p, q, A, B, pp, qp = sp.symbols("p q A B pp qp", real=True)
sub = {sp.Derivative(al, (y, 2)): (pp + p**2)*A, sp.Derivative(be, (y, 2)): (qp + q**2)*B, sp.Derivative(al, y): p*A, sp.Derivative(be, y): q*B}
Ks = sp.simplify(sp.expand(K.subs(sub).subs({al: A, be: B})))
formula = 4*(2*(pp + p**2)**2 + 2*(qp + q**2)**2 + (p**2 + 1/(4*A**2))**2 + (q**2 - 1/(4*B**2))**2 + 4*p**2*q**2)
print("  K - formula =", sp.simplify(Ks - formula))

print("== (iii) owner's throat_bulk (read-only import by path) vs my column")
sys.path.insert(0, "/home/user/Claude-Method-Works/research/warp-drive/docket68/lemmas")
sys.path.insert(0, "/home/user/Claude-Method-Works/research/warp-drive/docket68")
try:
    spec2 = importlib.util.spec_from_file_location("sim2_facing_ro", "/home/user/Claude-Method-Works/research/warp-drive/docket68/lemmas/sim2_facing.py")
    O = importlib.util.module_from_spec(spec2); spec2.loader.exec_module(O)
    for e in (1/32, 1.0, 64.0):
        tb = O.throat_bulk(e)
        mine = N.column(e, max_step=0.002 if e < 8 else 0.0005)
        ys_o, ys_m = tb["y_s"], mine.t[-1]
        yy = np.linspace(0.01*ys_m, 0.99*ys_m, 500)
        so = tb["sol0"].sol(yy); sm = mine.sol(yy)
        p_m, q_m = sm[2]-e - sm[3]/2, sm[2]-e + sm[3]/2
        dev = max(np.max(np.abs(so[2]-p_m)/(1+np.abs(p_m))), np.max(np.abs(so[3]-q_m)/(1+np.abs(q_m))), np.max(np.abs(np.log(so[0])-sm[0])))
        print(f"  e={e}: y_s owner={ys_o:.12g} mine={ys_m:.12g} rel diff={abs(ys_o-ys_m)/ys_m:.1e}; max rel dev (p,q,ln alpha) to 0.99 y_s = {dev:.1e}")
except Exception as ex:
    print("  owner import failed:", repr(ex))
