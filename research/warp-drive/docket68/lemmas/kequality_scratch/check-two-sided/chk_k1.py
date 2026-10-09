"""Independent check of the k=1 two-sided closed forms, super-criticality, P2's L<1 condition,
and the convention grid -- including the reading the author's verdict does not state:
ell in the recorded 'ell_2 = c ell' taken as OUR outer bulk's ell_1 (not the bridge's ell_s).

Units ell_s = 1.  v = 1/L.  f_s = 1 + u - mu/u,  f_o = 1 + u v^2  (u = R^2).
Ours (outer decaying):  sqrt f_s = x sqrt f_o,  x = 2mu/u - 1 > 0,  lam sqrt u = (1+x) sqrt f_o.
P2 (outer growing):     sqrt f_s = y sqrt f_o,  y = 1 - 2mu/u in (0,1), lam sqrt u = -(1-y) sqrt f_o.
"""
import sympy as sp
import mpmath as mp
mp.mp.dps = 50

u, mu, L, v, x, y, lam = sp.symbols('u mu L v x y lam', positive=True)
A = 1 + u/L**2
G = 1 + u - mu/u - (1 - 2*mu/u)**2*A
roots = sp.solve(sp.Eq(G, 0), mu)
claim = [u*((4*A-1) + s*sp.sqrt(1 + 8*A + 16*A*u))/(8*A) for s in (1, -1)]
ok = all(any(sp.simplify(c - rt) == 0 for rt in roots) for c in claim)
print("k=1 quadratic roots mu = u[(4A-1) +/- sqrt(1+8A+16Au)]/(8A):", ok)

# super-criticality, exact: in terms of x and v
uX = (2*x-1)*(x+1)/(2*(1 - x**2*v**2))
lam2 = sp.simplify((1+x)**2*(1/uX + v**2))
print("ours lam^2 =", sp.factor(lam2))
N = sp.factor(sp.simplify((lam2 - (1+v)**2)*(2*x-1)))
print("ours (lam^2 - (1+v)^2)(2x-1) =", N, " [own proof: (vx-1)(vx-2v-3); u>0 forces sign(2x-1)=sign(1-xv) => >0]")

# P2: mu>0 iff L<1
uY = (2*y+1)*(y-1)/(2*(1 - y**2*v**2))
print("P2: u(1 - y^2 v^2) = (2y+1)(y-1)/2 < 0 for y in (0,1) => needs y v > 1 => v > 1 (L < 1). check uY form:",
      sp.simplify((1 + uY - (1-y)/2) - y**2*(1 + uY*v**2)) == 0)
lamP2sq = sp.factor(sp.simplify((1-y)**2*(1/uY + v**2)))
print("P2 lam^2 =", lamP2sq)

# ---------- numerics ----------
def ours_from(L1, lamt):
    """all (x, u, mu) for ours at tension lam = lamt (ell_s units), outer decaying."""
    vv = 1/mp.mpf(L1)
    # (1+x)(2+v^2(x-1)) = lamt^2 (2x-1)
    a, b, c = vv**2, 2 - vv**2 + 2 - 2*lamt**2 - 2, None
    # expand: v^2 x^2 + x(2 + 0) ... do it numerically by polyroots
    # (1+x)(2 + v^2 x - v^2) = v^2 x^2 + 2x + 2 - v^2 ;  minus lamt^2(2x-1)
    co = [vv**2, 2 - 2*lamt**2, 2 - vv**2 + lamt**2]
    sols = []
    for xr in mp.polyroots(co, maxsteps=200, extraprec=200):
        if abs(mp.im(xr)) > mp.mpf(10)**-30: continue
        xr = mp.re(xr)
        if xr <= 0: continue
        uu = (2*xr-1)*(xr+1)/(2*(1 - xr**2*vv**2))
        if uu <= 0: continue
        m = uu*(1+xr)/2
        # verify unsquared
        fs = 1 + uu - m/uu; fo = 1 + uu*vv**2
        if fs <= 0: continue
        bal = (1 - 2*m/uu)/mp.sqrt(fs) + 1/mp.sqrt(fo)
        ten = (mp.sqrt(fs) + mp.sqrt(fo))/mp.sqrt(uu) - lamt
        if abs(bal) < mp.mpf(10)**-30 and abs(ten) < mp.mpf(10)**-30:
            sols.append((xr, uu, m))
    return sols

def p2_lam(m, L2):
    """P2 (outer growing) at fixed mu=m and L2: return list of (u2, |lam|) on the static curve u2>2mu."""
    vv = 1/mp.mpf(L2)
    # mu = u(1-y)/2 with u = (2y+1)(y-1)/(2(1-y^2v^2)) : solve for y in (1/vv, 1)
    g = lambda yy: (2*yy+1)*(yy-1)/(2*(1-yy**2*vv**2))*(1-yy)/2 - m
    out = []
    if vv <= 1: return out
    lo = 1/vv
    grid = [lo + (1-lo)*mp.mpf(i)/400 for i in range(1, 400)]
    vals = [g(t) for t in grid]
    for i in range(len(grid)-1):
        if vals[i]*vals[i+1] < 0:
            yy = mp.findroot(g, (grid[i], grid[i+1]), solver='bisect' if False else 'anderson')
            uu = (2*yy+1)*(yy-1)/(2*(1-yy**2*vv**2))
            fs = 1 + uu - m/uu; fo = 1 + uu*vv**2
            bal = (1 - 2*m/uu)/mp.sqrt(fs) - 1/mp.sqrt(fo)
            lm = (mp.sqrt(fs) - mp.sqrt(fo))/mp.sqrt(uu)
            assert abs(bal) < mp.mpf(10)**-25
            out.append((uu, lm))
    return out

if __name__ == '__main__':
    # (ii) RS at ell_s, author's example L1=2
    s = ours_from(2, mp.mpf(2))
    print("\n(ii) RS at ell_s, L1=2: ours solutions (x,u,mu):", [(mp.nstr(a, 12), mp.nstr(b, 12), mp.nstr(c, 12)) for a, b, c in s])
    m = s[0][2]
    print("   R1 =", mp.nstr(mp.sqrt(s[0][1]), 10), " r_h =", mp.nstr(mp.sqrt((-1 + mp.sqrt(1+4*m))/2), 10))
    # P2 at |lam|=1/2 and 1/4: find L2 with lam = target. scan L2
    for ratio in (mp.mpf(1)/4, mp.mpf(1)/8):
        tgt = 2*ratio
        def res(L2):
            r_ = p2_lam(m, L2)
            return [lm + tgt for uu, lm in r_]
        # direct solve: unknowns u2, L2: 4mu^2(u+u^2-mu) = lam^2 u^2 (u-2mu)^2, L2^2 = u/(Q^2-1)
        U = sp.Symbol('U', positive=True)
        poly = sp.Poly(4*sp.Rational(4, 3)**2*(U + U**2 - sp.Rational(4, 3)) - sp.Rational(tgt.__float__()).limit_denominator(100)**2*U**2*(U - sp.Rational(8, 3))**2, U)
        rts = [complex(z) for z in sp.Poly(poly).nroots(n=40)]
        for z in rts:
            if abs(z.imag) < 1e-20 and z.real > 8/3:
                uu = mp.mpf(z.real)
                Q2 = tgt**2*uu**3/(4*m**2)
                L2 = mp.sqrt(uu/(Q2-1))
                chk = p2_lam(m, L2)
                print(f"   ratio -{mp.nstr(ratio,3)}: u2={mp.nstr(uu,12)} R2={mp.nstr(mp.sqrt(uu),10)} L2={mp.nstr(L2,20)} recheck lam={[mp.nstr(c[1],12) for c in chk]}")
