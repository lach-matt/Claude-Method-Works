#!/usr/bin/env python3
"""DOCKET 67 audit re-derivation: gr-qc/9701064 (HPS) eq. (2) metric and its Einstein tensor.

Independent of research/warp-drive/hpscentre.py:curvature() (not imported).  Two independent
routes to G^mu_nu of ds^2 = -f(l) dt^2 + dl^2 + r(l)^2 dOmega^2:
  route A: coordinate Christoffels -> Riemann (MTW: R^a_bcd = d_c G^a_bd - d_d G^a_bc + ...),
           Ric_bd = R^a_bad, G^a_b = g^ac Ric_cb - R/2 delta.
  route B: a general warped-product formula via the Lagrangian/ADM route is avoided; instead
           route B is a different parametrisation, f = exp(2 Phi), computed in the orthonormal
           tetrad from Cartan structure equations (hand-coded connection 1-forms), and compared.
Then controls: HPS printed left sides (page 4, arXiv text layer), Bianchi identity, sign
(Einstein static universe rho>0), Schwarzschild vacuum, Ellis wormhole, regular centre finiteness,
dimensional homogeneity, and HPS eq. (8)/(9) re-derived from eq. (6) at the throat.
"""
import sympy as sp

l, t, th, ph = sp.symbols('l t theta phi')
fF, rF = sp.Function('f')(l), sp.Function('r')(l)
f1, f2 = sp.diff(fF, l), sp.diff(fF, l, 2)
r1, r2 = sp.diff(rF, l), sp.diff(rF, l, 2)
ok = True


def chk(label, cond):
    global ok
    ok &= bool(cond)
    print("  [%s] %s" % ("ok" if cond else "XX", label))


def einstein_mixed(g, X):
    n = len(X)
    gi = g.inv()
    Gam = [[[sum(gi[a, d]*(sp.diff(g[d, b], X[c]) + sp.diff(g[d, c], X[b]) - sp.diff(g[b, c], X[d]))
                 for d in range(n))/2 for c in range(n)] for b in range(n)] for a in range(n)]
    def Riem(a, b, c, d):
        e = sp.diff(Gam[a][b][d], X[c]) - sp.diff(Gam[a][b][c], X[d])
        e += sum(Gam[a][c][k]*Gam[k][b][d] - Gam[a][d][k]*Gam[k][b][c] for k in range(n))
        return e
    Ric = sp.Matrix(n, n, lambda b, d: sp.simplify(sum(Riem(a, b, a, d) for a in range(n))))
    R = sp.simplify(sum(gi[i, j]*Ric[i, j] for i in range(n) for j in range(n)))
    Gm = sp.simplify(gi*Ric - R/2*sp.eye(n))
    return Gm, R


# ---------------- route A
X = [t, l, th, ph]
g = sp.diag(-fF, 1, rF**2, rF**2*sp.sin(th)**2)
GA, RA = einstein_mixed(g, X)
print("route A (coordinate, MTW conventions)")
chk("G^mu_nu diagonal (all off-diagonal mixed components vanish)",
    all(sp.simplify(GA[i, j]) == 0 for i in range(4) for j in range(4) if i != j))
chk("G^phi_phi = G^theta_theta", sp.simplify(GA[3, 3] - GA[2, 2]) == 0)

# ---------------- HPS printed left sides (page 4 of the arXiv v1 text layer)
HPS = (2*r2/rF + r1**2/rF**2 - 1/rF**2,
       f1*r1/(fF*rF) + r1**2/rF**2 - 1/rF**2,
       f2/(2*fF) + r2/rF + f1*r1/(2*fF*rF) - f1**2/(4*fF**2))
for k, name in enumerate(("G^t_t", "G^l_l", "G^th_th")):
    chk("%s(route A) - HPS printed %s = 0" % (name, name), sp.simplify(GA[k, k] - HPS[k]) == 0)

# ---------------- route B: orthonormal tetrad, f = e^{2 Phi}; textbook Morris-Thorne-type
# components in proper length (derived here by hand from Cartan's equations):
#   e0 = e^Phi dt, e1 = dl, e2 = r dth, e3 = r sin th dph
#   w^0_1 = Phi' e0 ; w^2_1 = (r'/r) e2 ; w^3_1 = (r'/r) e3 ; w^3_2 = (cot th / r) e3
#   Riemann (orthonormal): R_0101 = Phi'' + Phi'^2 ; R_0202 = R_0303 = Phi' r'/r ;
#   R_1212 = R_1313 = -r''/r ; R_2323 = (1 - r'^2)/r^2   (signs: R_abab = sectional curvature
#   with R_0i0i entering with the Lorentzian sign)
Phi = sp.Function('Phi')(l)
P1, P2 = sp.diff(Phi, l), sp.diff(Phi, l, 2)
K01 = -(P2 + P1**2)          # sectional curvature of the (t,l) plane (Lorentzian sign)
K02 = -(P1*r1/rF)
K12 = -r2/rF
K23 = (1 - r1**2)/rF**2
# For a diagonal Riemann in an orthonormal frame, G^a_a = -(sum of sectional curvatures of the
# three planes NOT containing a) -- with the Lorentzian sign convention absorbed in K0i.
Gt = -(K12 + K12 + K23)          # planes 12, 13, 23
Gl = -(K02 + K02 + K23)          # planes 02, 03, 23
Gth = -(K01 + K02 + K12)         # planes 01, 03(=02), 13(=12)
sub = {fF: sp.exp(2*Phi)}
GAB = [sp.simplify(GA[k, k].subs(fF, sp.exp(2*Phi)).doit()) for k in range(3)]
for k, (a, name) in enumerate(zip((Gt, Gl, Gth), ("G^t_t", "G^l_l", "G^th_th"))):
    chk("%s route B (Cartan, f=e^{2Phi}) = route A" % name, sp.simplify(sp.expand(a - GAB[k])) == 0)

# ---------------- Bianchi identity nabla_mu G^mu_l = 0 for arbitrary f, r
Gtt, Gll, Gthth = HPS
div = sp.diff(Gll, l) + f1/(2*fF)*(Gll - Gtt) + 2*r1/rF*(Gll - Gthth)
chk("contracted Bianchi: d_l G^l_l + (f'/2f)(G^l_l-G^t_t) + (2r'/r)(G^l_l-G^th_th) = 0",
    sp.simplify(div) == 0)
for bad, lab in ((HPS[2] + f1**2/(4*fF**2), "G^th_th without -f'^2/4f^2"),
                 (HPS[2] - f1*r1/(2*fF*rF), "G^th_th without f'r'/2fr"),
                 (HPS[2] + 1/rF**2, "G^th_th with a stray 1/r^2")):
    d2 = sp.diff(Gll, l) + f1/(2*fF)*(Gll - Gtt) + 2*r1/rF*(Gll - bad)
    chk("  CONTROL: Bianchi FAILS for %s" % lab, sp.simplify(d2) != 0)

# ---------------- sign convention (MTW): Einstein static universe r = a sin(l/a), f = 1
a = sp.symbols('a', positive=True)
def ev(expr, fv, rv):
    rep = {}
    for k in (4, 3, 2, 1, 0):
        rep[sp.diff(fF, l, k) if k else fF] = sp.diff(fv, l, k) if k else fv
        rep[sp.diff(rF, l, k) if k else rF] = sp.diff(rv, l, k) if k else rv
    return sp.simplify(expr.subs(rep))
es = [ev(x, sp.Integer(1), a*sp.sin(l/a)) for x in HPS]
chk("Einstein static universe: G^t_t = -3/a^2 (rho = 3/(8 pi a^2) > 0, MTW sign)", sp.simplify(es[0] + 3/a**2) == 0)
chk("Einstein static universe: G^l_l = G^th_th = -1/a^2 (p = -1/(8 pi a^2) before Lambda)",
    sp.simplify(es[1] + 1/a**2) == 0 and sp.simplify(es[2] + 1/a**2) == 0)

# ---------------- Ellis (Bronnikov-Ellis) wormhole r = sqrt(l^2+b^2), f = 1
b = sp.symbols('b', positive=True)
el = [ev(x, sp.Integer(1), sp.sqrt(l**2 + b**2)) for x in HPS]
# G^t_t = -8 pi rho (MTW): rho = -b^2/(8 pi r^4), p_l = -b^2/(8 pi r^4), p_th = +b^2/(8 pi r^4)
chk("Ellis wormhole: G^t_t = +b^2/r^4 (rho<0), G^l_l = -b^2/r^4, G^th_th = +b^2/r^4",
    [sp.simplify(el[0]*(l**2+b**2)**2), sp.simplify(el[1]*(l**2+b**2)**2),
     sp.simplify(el[2]*(l**2+b**2)**2)] == [b**2, -b**2, b**2])

# ---------------- Schwarzschild vacuum in proper length: use r as parameter, dr/dl = sqrt(1-2M/r)
M, R = sp.symbols('M R', positive=True)
h = sp.sqrt(1 - 2*M/R)                      # dr/dl
def dl(expr):                               # d/dl = h d/dR
    return sp.simplify(h*sp.diff(expr, R))
fv = 1 - 2*M/R
fd = [fv, dl(fv)]; fd.append(dl(fd[1]))
rd = [R, h]; rd.append(dl(rd[1]))
rep = {fF: fd[0], f1: fd[1], f2: fd[2], rF: rd[0], r1: rd[1], r2: rd[2]}
def subsw(e):
    e = e.subs(f2, fd[2]).subs(r2, rd[2]).subs(f1, fd[1]).subs(r1, rd[1]).subs(fF, fd[0]).subs(rF, rd[0])
    return sp.simplify(e)
chk("Schwarzschild exterior (r > 2M) in proper length: G^mu_nu = 0 (all three)",
    [subsw(x) for x in HPS] == [0, 0, 0])

# ---------------- regular centre r = l + c3 l^3, f = f0(1 + b2 l^2): G finite at l = 0
c3, b2, f0 = sp.symbols('c3 b2 f0', positive=True)
rc = [sp.series(ev(x, f0*(1 + b2*l**2), l + c3*l**3), l, 0, 2).removeO() for x in HPS]
chk("regular centre: G^t_t -> +18 c3, finite (1/r^2 terms cancel)", sp.simplify(rc[0].subs(l, 0) - 18*c3) == 0)
# Misner-Sharp: m' = 4 pi rho r^2 r' with 8 pi rho = -G^t_t  ->  m = -3 c3 l^3 + O(l^5)
# (hpscentre.py docstring (a): "m = -3 c3 l^3 + O(l^5)")
mser = sp.integrate(sp.series(-ev(HPS[0], f0*(1 + b2*l**2), l + c3*l**3)/2
                    * (l + c3*l**3)**2 * sp.diff(l + c3*l**3, l), l, 0, 4).removeO(), (l, 0, l))
chk("regular centre: Misner-Sharp m = -3 c3 l^3 + O(l^5)", sp.simplify(sp.series(mser, l, 0, 5).removeO() + 3*c3*l**3) == 0)
print("     regular-centre limits G(0) =", [sp.simplify(x.subs(l, 0)) for x in rc])
chk("regular centre: all three components finite at l = 0",
    all(sp.limit(ev(x, f0*(1 + b2*l**2), l + c3*l**3), l, 0).is_finite for x in HPS))

# ---------------- dimensional homogeneity: every term length^-2 under l -> s l, r -> s r
s = sp.symbols('s', positive=True)
F0, F1, F2, R0, R1, R2 = sp.symbols('F0 F1 F2 R0 R1 R2')
repS = {f2: F2/s**2, f1: F1/s, fF: F0, r2: R2/s, r1: R1, rF: R0*s}
homog = all(sp.simplify(term.subs(repS)*s**2 - term.subs(repS).subs(s, 1)) == 0
            for x in HPS for term in sp.Add.make_args(sp.expand(x)))
chk("every term of G^t_t, G^l_l, G^th_th scales as length^-2", homog)

# ---------------- HPS eq. (8) re-derived from eq. (6) at l = 0 (r' = f' = 0), and eq. (9)
# eq. (6) RHS transcribed from the page text; only terms without f' or r' survive at l=0:
Kk, lnf, F, Rpp, r0 = sp.symbols('K lnf F Rpp r0', positive=True)   # F = f''/f, Rpp = r''
rhs6_throat = Kk**2*(-4*F**2 + 32*F*Rpp/r0
                     + lnf*(16/r0**4 - 4*F**2 + 16*F*Rpp/r0 - 16*Rpp**2/r0**2))
lhs6_throat = HPS[1].subs({f1: 0, r1: 0}).subs(rF, r0)            # G^l_l at the throat
eq8_derived = sp.expand((lhs6_throat - rhs6_throat)*(-r0**4/Kk**2))
eq8_printed = (-4*F**2*(1 + lnf)*r0**4 + 32*F*Rpp*(1 + lnf/2)*r0**3
               + (Kk**-2 - 16*Rpp**2*lnf)*r0**2 + 16*lnf)
chk("G^l_l(throat) = -1/r0^2, and (6) at l=0 reproduces HPS printed quartic (8) exactly",
    sp.simplify(lhs6_throat + 1/r0**2) == 0 and sp.simplify(eq8_derived - eq8_printed) == 0)
K2 = 1/(5760*sp.pi)
rr = sp.sqrt(-16*K2*sp.Rational(-2, 3))
chk("eq. (9): r(0) = sqrt(-16 K^2 ln f0) solves (8) at f''=r''=0; ln f0=-2/3 -> r0 = %.4f l_P (HPS: '~0.02 l_P')"
    % float(rr), sp.simplify(eq8_printed.subs({F: 0, Rpp: 0, lnf: sp.Rational(-2, 3), Kk: sp.sqrt(K2), r0: rr})) == 0)
r67 = sp.nsolve(eq8_printed.subs({F: 1, Rpp: 0, lnf: 0, Kk: sp.sqrt(K2)}), r0, 60)
chk("eq. (8), f0 = f0'' = 1, r'' = 0: r0 = %.3f l_P (HPS: 'r(0) ~ 67 l_P')" % float(r67),
    abs(float(r67) - 67) < 1)

print("\nRESULT:", "ALL CHECKS PASS" if ok else "A CHECK FAILED")
raise SystemExit(0 if ok else 1)
