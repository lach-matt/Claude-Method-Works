#!/usr/bin/env python3
"""DOCKET 67 re-derivation: schwarzschild-1916.
Independent sympy check of Schwarzschild 1916 (physics/9905030) and of the
two ways driven.py uses it: the static corner V6 and the Lemaitre/PG witness
V11-V13.  Reads nothing from research/warp-drive; imports nothing from it.
Exit 0 iff every check comes out as recorded."""
import sys, math
import sympy as sp

OK = True
def rep(label, val, want=0):
    global OK
    v = sp.simplify(val) if not isinstance(val, (bool, float, int, str)) else val
    good = (v == want)
    OK &= bool(good)
    print(("PASS " if good else "FAIL ") + label + "  ->  " + str(v))

def einstein(g, x):
    n = 4
    gi = g.inv()
    Gam = [[[sp.simplify(sum(gi[a, d]*(sp.diff(g[d, b], x[c]) + sp.diff(g[d, c], x[b])
             - sp.diff(g[b, c], x[d])) for d in range(n))/2) for c in range(n)]
             for b in range(n)] for a in range(n)]
    Ric = sp.zeros(n, n)
    for b in range(n):
        for c in range(n):
            s = 0
            for a in range(n):
                s += sp.diff(Gam[a][b][c], x[a]) - sp.diff(Gam[a][b][a], x[c])
                for d in range(n):
                    s += Gam[a][a][d]*Gam[d][b][c] - Gam[a][c][d]*Gam[d][b][a]
            Ric[b, c] = sp.simplify(s)
    Rs = sp.simplify(sum(gi[a, b]*Ric[a, b] for a in range(n) for b in range(n)))
    G = (Ric - Rs*g/2).applyfunc(sp.simplify)
    return G, gi

t, th, ph = sp.symbols("t theta phi", real=True)

print("E1  Schwarzschild eq.(14) (sign-flipped to -+++): vacuum for EVERY real alpha")
R = sp.Symbol("R", positive=True); al = sp.Symbol("alpha", real=True)
f = 1 - al/R
g14 = sp.diag(-f, 1/f, R**2, R**2*sp.sin(th)**2)
G14, gi14 = einstein(g14, [t, R, th, ph])
rep("E1  G_ab of eq.(14), alpha real (either sign)", G14.norm()**2)

print("E2  Schwarzschild's own system (a)-(d) in x1 = r^3/3, with his f1,f2,f4")
x1, rho = sp.symbols("x1 rho", positive=True); a_ = sp.Symbol("alpha", real=True)
S = 3*x1 + rho
f2 = S**sp.Rational(2, 3); f4 = 1 - a_*S**sp.Rational(-1, 3); f1 = S**sp.Rational(-4, 3)/f4
d = lambda F: sp.diff(F, x1)
eqa = d(d(f1)/f1) - (sp.Rational(1, 2)*(d(f1)/f1)**2 + (d(f2)/f2)**2 + sp.Rational(1, 2)*(d(f4)/f4)**2)
eqb = d(d(f2)/f1) - (2 + d(f2)**2/(f1*f2))
eqc = d(d(f4)/f1) - d(f4)**2/(f1*f4)
eqd = f1*f2**2*f4 - 1
for nm, e in (("(a)", eqa), ("(b)  'automatically fulfilled'", eqb), ("(c)", eqc), ("(d) determinant f1 f2^2 f4 = 1", eqd)):
    rep("E2  eq." + nm, e)

print("E3  domain of Schwarzschild's manifold: R = (r^3+alpha^3)^(1/3), r in (0,inf)")
r = sp.Symbol("r", positive=True); A = sp.Symbol("A", positive=True)
Rr = (r**3 + A**3)**sp.Rational(1, 3)
rep("E3  R(r -> 0+) = alpha", sp.limit(Rr, r, 0, "+") - A)
rep("E3  dR/dr > 0 for r > 0 (monotone)", sp.simplify(sp.diff(Rr, r) - r**2/Rr**2))
print("     => the 1916 chart covers R in (alpha, inf) only; R <= alpha is NOT in the source's manifold")

print("E4  Misner-Sharp mass of eq.(14) is constant alpha/2; its sign is NOT fixed by the field equations")
m14 = R/2*(1 - gi14[1, 1])
rep("E4  m = (R/2)(1 - g^RR) - alpha/2", m14 - al/2)
Kr = None
# Kretschmann for alpha real: 12 alpha^2 / R^6 -> singular at R = 0 for alpha != 0
print("     alpha < 0 is a vacuum solution (E1 holds for real alpha) with g_RR = 1/(1+|alpha|/R) < 1:")
rep("E4  g_RR < 1 at alpha = -1, R = 3 (contracted, vacuum)", bool((1/f).subs({al: -1, R: 3}) < 1), True)

print("E5  driven.py V6 is an IDENTITY, not a check of Schwarzschild: holds for ARBITRARY Lambda(r)")
Lam = sp.Function("Lambda", real=True)(r)
m_s = r/2*(1 - sp.exp(-2*Lam))
rep("E5  e^{2L} - 1/(1-2m/r), m := (r/2)(1-e^{-2L}), Lambda arbitrary", sp.exp(2*Lam) - 1/(1 - 2*m_s/r))
rep("E5  same with Lambda = r^2 (a NON-vacuum profile)", (sp.exp(2*Lam) - 1/(1 - 2*m_s/r)).subs(Lam, r**2).doit())
print("     and the static metric with g_rr = 1/(1-2m(r)/r) is Schwarzschild only where m' = 0:")
Phi = sp.Function("Phi", real=True)(r); mm = sp.Function("m", real=True)(r)
gst = sp.diag(-sp.exp(2*Phi), 1/(1 - 2*mm/r), r**2, r**2*sp.sin(th)**2)
Gst, gist = einstein(gst, [t, r, th, ph])
rho_st = sp.simplify(-(gist[0, 0]*Gst[0, 0])/(8*sp.pi))   # rho = -T^t_t
rep("E5  rho = -T^t_t = m'/(4 pi r^2)", rho_st - sp.diff(mm, r)/(4*sp.pi*r**2))

print("E6  Lemaitre (= PG) witness as driven/drivensource write it: vacuum, m = r_s/2, Gamma = 1, U = -sqrt(r_s/R)")
rc, rs = sp.symbols("rho_c r_s", positive=True); T = sp.Symbol("t", positive=True)
RL = (sp.Rational(3, 2)*(rc - T))**sp.Rational(2, 3)*rs**sp.Rational(1, 3)
gL = sp.diag(-1, rs/RL, RL**2, RL**2*sp.sin(th)**2)
GL, giL = einstein(gL, [T, rc, th, ph])
rep("E6  G_ab (Lemaitre) = 0", GL.norm()**2)
W = sp.sqrt(giL[1, 1])*sp.diff(RL, rc); U = sp.diff(RL, T)
mL = RL/2*(1 - W**2 + U**2)
rep("E6  Gamma = e^-L R' = 1", W - 1)
rep("E6  m = r_s/2", mL - rs/2)
rep("E6  U + sqrt(r_s/R) = 0", U + sp.sqrt(rs/RL))
rep("E6  |U| > 1 at R = r_s/4 (inside horizon: outside the 1916 chart)", bool((sp.sqrt(rs/RL)).subs(rc, T + sp.Rational(2, 3)*(sp.Rational(1, 4))**sp.Rational(3, 2)*rs).subs(rs, 1) > 1), True)
print("     pullback: dtau = dt + sqrt(rs/r)/(1-rs/r) dr, drho = dt + sqrt(r/rs)/(1-rs/r) dr")
dt_, dr_ = sp.symbols("dt dr"); x = rs/r
a1 = sp.sqrt(rs/r)/(1 - x); b1 = sp.sqrt(r/rs)/(1 - x)
ds2 = sp.expand(-(dt_ + a1*dr_)**2 + x*(dt_ + b1*dr_)**2)
rep("E6  Lemaitre ds^2 = Schwarzschild ds^2 (r > r_s and r < r_s alike)", sp.simplify(ds2 - (-(1 - x)*dt_**2 + dr_**2/(1 - x))))
print("     r_s positivity in V13 ('m = r_s/2 > 0') is INPUT: symbols('rho r_s', positive=True), not derived")

print("E7  numerics in the source (discrepancies, not load-bearing for the tree)")
GM = 1.32712440041e20; c = 299792458.0; aM = 5.7909e10
alpha_sun = 2*GM/c**2
print("     alpha_sun = 2GM/c^2 = %.3f m  (IAU 2015 nominal GM_sun)" % alpha_sun)
print("     Mercury alpha/r = %.3e ; 2 v^2 (v=47.36 km/s) = %.3e" % (alpha_sun/aM, 2*(47.36e3/c)**2))
dev = (alpha_sun/aM)**3/3          # leading term of (1+x^3)^(1/3)-1; float (1+x)^(1/3) underflows to 0
print("     (1+alpha^3/r^3)^(1/3) - 1 = %.2e   (source text: 'of the order 10^-12')" % dev)
n0 = c/(alpha_sun*math.sqrt(2))
print("     n0 = 1/(alpha sqrt 2) = %.3e rad/s = %.3e cycles/s, coordinate time  (source text: 'around 10^4 per second')" % (n0, n0/(2*math.pi)))
rep("E7  Mercury deviation <= 1e-12 (source's bound holds as an upper bound)", dev <= 1e-12, True)
rep("E7  n0/2pi rounds to 10^4 per second (log10 in [3.5, 4.5))", 3.5 <= math.log10(n0/(2*math.pi)) < 4.5, True)

print("\nALL AS RECORDED" if OK else "\nMISMATCH")
sys.exit(0 if OK else 1)
