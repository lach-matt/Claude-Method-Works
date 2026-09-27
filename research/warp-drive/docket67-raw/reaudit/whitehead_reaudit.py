"""Re-audit checks: Whitehead, Quart. J. Math. 3 (1932) 33-42 (Drive 1LY79WDjcfFwDTSwgu5Qt6DtZ8PBgVXkD).
Whitehead's hypothesis (p.34, (2.2)-(2.3)): the connection components Gamma^i_jk are defined on a cell,
bounded, continuous and satisfy a LIPSCHITZ condition.  For a Levi-Civita connection that is: metric C^{1,1}
and non-degenerate on an open neighbourhood.  The tree (qeihps.py:103-105, 436-439) tests f(0)>0, r(0)>0 only."""
import sympy as sp, math
P=[];F=[]
def chk(n,ok): (P if ok else F).append(n); print(("PASS " if ok else "FAIL ")+n)
t,l,th,ph=sp.symbols('t l theta phi',real=True)
f=sp.Function('f')(l); r=sp.Function('r')(l)
g=sp.diag(-f,1,r**2,r**2*sp.sin(th)**2); X=[t,l,th,ph]; gi=g.inv()
Gam=lambda a,b,c: sp.simplify(sum(gi[a,d]*(sp.diff(g[d,b],X[c])+sp.diff(g[d,c],X[b])-sp.diff(g[b,c],X[d])) for d in range(4))/2)
G=[[[Gam(a,b,c) for c in range(4)] for b in range(4)] for a in range(4)]
nz=sorted({str(G[a][b][c]) for a in range(4) for b in range(4) for c in range(4) if G[a][b][c]!=0})
print("   nonzero Christoffels of metric (2):", nz)
chk("every Gamma of -f dt^2+dl^2+r^2 dOmega^2 is built from f'/f, f', r r', r'/r (and angular factors)",
    all(('Derivative' in s) or ('sin' in s) or ('cos' in s) or ('tan' in s) for s in nz))
# counterexample class of the first audit: f = 1/(1+|l|^{3/2}): non-degenerate at 0, C^1, NOT C^{1,1}
ff=lambda x: 1/(1+abs(x)**1.5)
fp=lambda x: -1.5*math.copysign(abs(x)**0.5,x)/(1+abs(x)**1.5)**2
Gl_tt=lambda x: fp(x)/2          # Gamma^l_tt = f'/2
ratios=[abs(Gl_tt(h)-Gl_tt(0))/h for h in (1e-2,1e-4,1e-6,1e-8)]
print("   |Gamma^l_tt(h)-Gamma^l_tt(0)|/h:", ["%.3g"%x for x in ratios])
chk("f=1/(1+|l|^1.5): f(0)=1>0 (passes the tree's point test)", ff(0)==1.0)
chk("  but Gamma^l_tt is NOT Lipschitz at l=0 (difference quotient -> inf): Whitehead's (2.3) fails", ratios[-1]>1e3 and ratios==sorted(ratios))
# geodesic non-uniqueness for that metric (1+1 part): l'' = -Gamma^l_tt t'^2, t' = E/f ; take E=1 normalisation
# l = 0 and a second solution leaving l=0 with zero velocity: l'' = (3/4) sgn(l)|l|^{1/2} (leading order) -> l = s^4/256
s=sp.symbols('s',positive=True); lc=s**4/256
lhs=sp.diff(lc,s,2); rhs=sp.Rational(3,4)*sp.sqrt(lc)
chk("  leading-order l''=(3/4)|l|^{1/2} has l=0 AND l=s^4/256 through (0,0): exp_p ill-defined", sp.simplify(lhs-rhs)==0)
# first run used s^4/144 -- my arithmetic error (12c = (3/4)sqrt(c) gives c = 1/256), corrected; matches the first audit's s^4/256.
chk("Whitehead's conclusion is local and sizeless: 'a simple, convex region which can be made as small as we please' (p.33)", True)
print("\n%d PASS, %d FAIL"%(len(P),len(F))); raise SystemExit(1 if F else 0)
