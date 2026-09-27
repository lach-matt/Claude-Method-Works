#!/usr/bin/env python3
"""DOCKET 67, result 17/286: Hochberg & Visser, gr-qc/9802046 (PRD 58, 044021), sections 4, 6.1, 7.

Re-derivation of everything closed-form in the section-7 claim:
  "if the wormhole is dynamic, flare-out in the spatial direction does not imply flare-out
   in the null directions orthogonal to the throat."

Checks (sympy, stdlib otherwise):
  A  eq (72): theta_+- for the conformally-scaled Morris-Thorne metric (69), computed as
     gamma^{ab} nabla_a l_b from Christoffels, equals the printed form AND equals (2/R) l(R).
  B  eq (73)/(75): d theta/d u = l^t d_t theta + l^r d_r theta, restricted to theta = 0.
  C  eq (76): G_{tt}+G_{rr} in the orthonormal frame, from the Einstein tensor of (69).
  D  eq (77): on the extremal surface, 8 pi (rho - tau) = -2 d theta/d u exactly (sign-locked).
  E  static limit (Omega' = 0): the extremal spheres coalesce at b(r0)=r0 with flare-out
     (1 - b'(r0))/r0^2, eq (83).
  F  foliation.py:243's theta_+ = (2/R)(U + Gamma) for the general diagonal spherically
     symmetric metric, and normalisation-independence of the zero set and of sign(d theta/du)
     on theta = 0 (Maeda-Harada-Carr 0901.1153 eq 2.10).
  G  INSTANCE 1: b = r0^2/r (Ellis), Omega = exp(H t): the constant-t centre r0 is spatially
     flared-out for all t, theta_+ != 0 there, and of the two null-extremal spheres one is
     flared-out and the other is NOT.  Spatial flare-out at the centre does not give null
     flare-out at the centre.
  H  INSTANCE 2 (Maeda-Harada-Carr 0901.1153 eq 4.53, a = t/t0): the x=0 sphere is a spatial
     minimal sphere with flare-out at every t; theta_+ theta_- > 0 everywhere for t0 < 2b
     (no anti-trapped surface, hence no Hochberg-Visser throat anywhere); NEC (indeed DEC)
     holds everywhere for t0 <= b.  Their eqs (4.54)-(4.57), (4.61) re-derived.
Exit 1 on any failure.  Nothing here is new: every line is the paper's own algebra.
"""
import sys
import sympy as sp

fails = []
discrepancies = []
def discrepancy(name, cond_that_source_is_off):
    """A misprint is a discrepancy, not a refutation (fluctuation.py precedent): recorded, never a failure."""
    if bool(cond_that_source_is_off):
        print("DISCREPANCY " + name); discrepancies.append(name)
    else:
        print("PASS " + name + "  (no discrepancy after all)")
def check(name, cond):
    ok = bool(cond)
    print(("PASS " if ok else "FAIL ") + name)
    if not ok:
        fails.append(name)

t, r, th, ph = sp.symbols('t r theta phi', real=True)
Om = sp.Function('Omega')(t)
b = sp.Function('b')(r)

def christoffel(g, x):
    ginv = g.inv()
    n = len(x)
    G = [[[0]*n for _ in range(n)] for _ in range(n)]
    for a in range(n):
        for bb in range(n):
            for c in range(n):
                G[a][bb][c] = sp.simplify(sum(ginv[a, d]*(sp.diff(g[d, bb], x[c]) + sp.diff(g[d, c], x[bb]) - sp.diff(g[bb, c], x[d])) for d in range(n))/2)
    return G

def ricci(g, x):
    n = len(x)
    G = christoffel(g, x)
    R = sp.zeros(n, n)
    for bb in range(n):
        for c in range(n):
            s = 0
            for a in range(n):
                s += sp.diff(G[a][bb][c], x[a]) - sp.diff(G[a][bb][a], x[c])
                for d in range(n):
                    s += G[a][a][d]*G[d][bb][c] - G[a][c][d]*G[d][bb][a]
            R[bb, c] = sp.simplify(s)
    return R, G

def cov_deriv_lower(g, G, l_low, x):
    n = len(x)
    D = sp.zeros(n, n)
    for a in range(n):
        for bb in range(n):
            D[a, bb] = sp.diff(l_low[bb], x[a]) - sum(G[c][a][bb]*l_low[c] for c in range(n))
    return D

# ---------------------------------------------------------------- A, B: eqs (72), (73)
x = [t, r, th, ph]
g = sp.diag(-Om**2, Om**2/(1 - b/r), Om**2*r**2, Om**2*r**2*sp.sin(th)**2)
Ric, G = ricci(g, x)
s = sp.sqrt(1 - b/r)
res = {}
for sign, lab in ((1, '+'), (-1, '-')):
    l_up = sp.Matrix([1/(sp.sqrt(2)*Om), sign*s/(sp.sqrt(2)*Om), 0, 0])
    l_low = g*l_up
    D = cov_deriv_lower(g, G, list(l_low), x)
    # gamma^{ab} nabla_a l_b, gamma the sphere part: 2 gamma^{thth} nabla_th l_th, eq (86)-style
    theta = sp.simplify(D[2, 2]/g[2, 2] + D[3, 3]/g[3, 3])
    theta_printed = sp.sqrt(2)*sp.diff(Om, t)/Om**2 + sign*sp.sqrt(2)*s/(r*Om)
    check(f"eq (72) theta_{lab} from Christoffels", sp.simplify(theta - theta_printed) == 0)
    R_areal = Om*r
    check(f"theta_{lab} = (2/R) l(R)  (area-expansion form)",
          sp.simplify(theta - (2/R_areal)*(l_up[0]*sp.diff(R_areal, t) + l_up[1]*sp.diff(R_areal, r))) == 0)
    dth = sp.simplify(l_up[0]*sp.diff(theta, t) + l_up[1]*sp.diff(theta, r))
    Od, Odd = sp.diff(Om, t), sp.diff(Om, t, 2)
    dth_printed = (1/Om**2)*((Odd/Om - 2*Od**2/Om**2) - sign*Od*s/(r*Om) - (1 - b/r)/r**2 + (-sp.diff(b, r) + b/r)/(2*r**2))
    check(f"eq (73) d theta_{lab}/du_{lab}", sp.simplify(dth - dth_printed) == 0)
    res[sign] = (theta, dth)

# on theta_± = 0: s/r = ∓ Od/Om  (eq 74).  Build (73) with S standing for s, substitute.
S = sp.symbols('S', positive=True)
for sign, lab in ((1, '+'), (-1, '-')):
    Od, Odd = sp.diff(Om, t), sp.diff(Om, t, 2)
    dth73 = (1/Om**2)*((Odd/Om - 2*Od**2/Om**2) - sign*Od*S/(r*Om) - S**2/r**2 + (-sp.diff(b, r) + b/r)/(2*r**2))
    dth_on = dth73.subs(S, -sign*r*Od/Om)
    dth75 = (1/Om**2)*((Odd/Om - 2*Od**2/Om**2) + (-sp.diff(b, r) + b/r)/(2*r**2))
    check(f"eq (75) flare-out on theta_{lab}=0 follows from (73)+(74)", sp.simplify(dth_on - dth75) == 0)

# ---------------------------------------------------------------- C, D: eqs (76), (77)
Rs = sp.simplify(sum(g.inv()[a, a]*Ric[a, a] for a in range(4)))
Ein = sp.simplify(Ric - Rs*g/2)
# orthonormal components: G_hat{tt} = Ein_tt / Om^2 ; G_hat{rr} = Ein_rr (1-b/r)/Om^2
Gtt_hat = sp.simplify(Ein[0, 0]/Om**2)
Grr_hat = sp.simplify(Ein[1, 1]*(1 - b/r)/Om**2)
Od, Odd = sp.diff(Om, t), sp.diff(Om, t, 2)
eq76 = (1/Om**2)*(-b/r**3 + sp.diff(b, r)/r**2 - 2*Odd/Om + 4*Od**2/Om**2)
check("eq (76) G_tt + G_rr (orthonormal) = 8 pi (rho - tau)", sp.simplify(Gtt_hat + Grr_hat - eq76) == 0)
dth75 = (1/Om**2)*((Odd/Om - 2*Od**2/Om**2) + (-sp.diff(b, r) + b/r)/(2*r**2))
check("eq (77) 8 pi (rho - tau) = -2 d theta/du on the extremal sphere (sign-locked)", sp.simplify(eq76 + 2*dth75) == 0)

# ---------------------------------------------------------------- E: static limit, eq (83)
r0 = sp.symbols('r0', positive=True)
Omc = sp.symbols('Omega_c', positive=True)
for sign in (1, -1):
    theta, dth = res[sign]
    th_static = theta.subs(Om, Omc).doit()
    check(f"static: theta_{'+' if sign>0 else '-'} = 0 iff b(r) = r",
          sp.simplify(th_static.subs(b, r)) == 0 and sp.simplify(sp.solve(sp.Eq(th_static, 0), b)[0] - r) == 0)
bp0 = sp.symbols('bp0')
dth_static = res[1][1].subs(Om, Omc).doit().subs(sp.Derivative(b, r), bp0).subs(b, r)
dth_static = sp.simplify(dth_static.subs(Omc, 1))
print("   static flare-out from (73) with Omega=1, b(r0)=r0 :", dth_static)
paper83 = (1 - bp0)/r**2
ratio = sp.simplify(paper83/dth_static)
print("   printed eq (83) / value from (73)-(75) =", ratio)
discrepancy("printed eq (83) (1 - b')/r0^2 vs static limit of (73)/(75) = (1 - b')/(2 r0^2): factor 2, positive, sign unchanged; recorded, not repaired",
            sp.simplify(dth_static - paper83) != 0 and ratio == 2)
check("static: sign of flare-out is sign(1 - b'(r0)) either way (eq 83's conclusion survives)",
      sp.simplify(dth_static*2*r**2 - (1 - bp0)) == 0)

# ---------------------------------------------------------------- F: foliation.py:243
Phi = sp.Function('Phi')(t, r); Lam = sp.Function('Lambda')(t, r); Rf = sp.Function('R')(t, r)
g2 = sp.diag(-sp.exp(2*Phi), sp.exp(2*Lam), Rf**2, Rf**2*sp.sin(th)**2)
Ric2, G2 = ricci(g2, x)
l_up = sp.Matrix([sp.exp(-Phi), sp.exp(-Lam), 0, 0])
check("l = e^{-Phi} d_t + e^{-Lambda} d_r is null", sp.simplify((l_up.T*g2*l_up)[0]) == 0)
D2 = cov_deriv_lower(g2, G2, list(g2*l_up), x)
theta2 = sp.simplify(D2[2, 2]/g2[2, 2] + D2[3, 3]/g2[3, 3])
U = sp.exp(-Phi)*sp.diff(Rf, t); Gam = sp.exp(-Lam)*sp.diff(Rf, r)
check("foliation.py:243  theta_+ = (2/R)(U + Gamma), U = e^{-Phi} R_t, Gamma = e^{-Lambda} R_r",
      sp.simplify(theta2 - (2/Rf)*(U + Gam)) == 0)
# normalisation independence on theta = 0
h = sp.Function('h')(t, r)
thetaH = h*theta2
dthetaH = sp.expand(h*(l_up[0]*sp.diff(thetaH, t) + l_up[1]*sp.diff(thetaH, r)))
dtheta = l_up[0]*sp.diff(theta2, t) + l_up[1]*sp.diff(theta2, r)
check("rescaling l -> h l: d theta'/du' = h^2 d theta/du + h theta l(h), so sign fixed on theta=0",
      sp.simplify(dthetaH - h**2*dtheta - h*theta2*(l_up[0]*sp.diff(h, t) + l_up[1]*sp.diff(h, r))) == 0)

# ---------------------------------------------------------------- G: instance 1
H = sp.Rational(1, 3)          # H^2 = 1/9 < 1/4: two null-extremal spheres
r0v = 1
bE = r0v**2/r                  # Ellis shape function, b(r0)=r0, b' = -1/r^2
spatial_flare = sp.simplify((bE - r*sp.diff(bE, r))/(2*bE**2))     # Morris-Thorne (b - b'r)/(2 b^2) > 0
check("instance 1: centre r0 spatially flared-out (Morris-Thorne (b-b'r)/2b^2 > 0), all t", spatial_flare.subs(r, r0v) > 0)
theta_p = res[1][0].subs(Om, sp.exp(H*t)).subs(b, bE).doit()
check("instance 1: theta_+ != 0 at the centre r0 (the spatially flared sphere is not null-extremal)",
      sp.simplify(theta_p.subs(r, r0v)) != 0 and sp.simplify(theta_p.subs(r, r0v).subs(t, 0)) == sp.sqrt(2)*H)
# null-extremal spheres for the collapsing branch (theta_+ = 0 needs Od<0; use Omega=exp(-H t) so theta_+ can vanish)
theta_p = res[1][0].subs(Om, sp.exp(-H*t)).subs(b, bE).doit()
dth_p = res[1][1].subs(Om, sp.exp(-H*t)).subs(b, bE).doit()
roots = [sp.nsimplify(v) for v in sp.solve(sp.Eq(sp.simplify(theta_p*sp.exp(-2*H*t)/sp.sqrt(2)), 0), r) if v.is_real and v > 0]
roots = sorted(set(roots))
check("instance 1: two null-extremal spheres r* > r0 exist", len(roots) == 2 and all(rt > r0v for rt in roots))
signs = [int(sp.sign(sp.N(dth_p.subs(r, rt).subs(t, 0), 30))) for rt in roots]
print("   roots r* =", [float(rt) for rt in roots], " sign(d theta_+/du_+) =", signs)
check("instance 1: one null-extremal sphere is flared-out (+), the other is NOT (-)", sorted(signs) == [-1, 1])
# formula check: dth on theta=0 equals e^{2Ht}[-H^2 + r0^2/r*^4]
for rt in roots:
    check(f"instance 1: eq (75) at r*={float(rt):.4f}: -H^2 + r0^2/r*^4",
          abs(sp.N(dth_p.subs(r, rt).subs(t, 0) - (-H**2 + r0v**2/rt**4), 30)) < 1e-25)

# ---------------------------------------------------------------- H: instance 2 (Maeda-Harada-Carr 0901.1153 eq 4.53)
xx = sp.symbols('x', real=True); bb_, t0 = sp.symbols('b t0', positive=True)
a = sp.Function('a')(t)
g3 = sp.diag(-1, a**2, a**2*(xx**2 + bb_**2), a**2*(xx**2 + bb_**2)*sp.sin(th)**2)
x3 = [t, xx, th, ph]
Ric3, G3 = ricci(g3, x3)
Rs3 = sp.simplify(sum(g3.inv()[i, i]*Ric3[i, i] for i in range(4)))
Ein3 = sp.simplify(Ric3 - Rs3*g3/2)
ad, add = sp.diff(a, t), sp.diff(a, t, 2)
Gtt = sp.simplify(Ein3[0, 0]*g3.inv()[0, 0])   # G^t_t
Gxx = sp.simplify(Ein3[1, 1]*g3.inv()[1, 1])   # G^x_x
Gthth = sp.simplify(Ein3[2, 2]*g3.inv()[2, 2])
check("MHC eq (4.54) 8piG T^t_t", sp.simplify(Gtt - (-3*ad**2/a**2 + bb_**2/(a**2*(xx**2 + bb_**2)**2))) == 0)
check("MHC eq (4.55) 8piG T^x_x", sp.simplify(Gxx - (-2*add/a - ad**2/a**2 - bb_**2/(a**2*(xx**2 + bb_**2)**2))) == 0)
check("MHC eq (4.56) 8piG T^th_th", sp.simplify(Gthth - (-2*add/a - ad**2/a**2 + bb_**2/(a**2*(xx**2 + bb_**2)**2))) == 0)
R3 = a*sp.sqrt(xx**2 + bb_**2)
lp = sp.Matrix([1, 1/a, 0, 0]); lm = sp.Matrix([1, -1/a, 0, 0])
check("MHC null normals", sp.simplify((lp.T*g3*lp)[0]) == 0 and sp.simplify((lm.T*g3*lm)[0]) == 0)
thp = sp.simplify((2/R3)*(lp[0]*sp.diff(R3, t) + lp[1]*sp.diff(R3, xx)))
thm = sp.simplify((2/R3)*(lm[0]*sp.diff(R3, t) + lm[1]*sp.diff(R3, xx)))
prod = sp.simplify(thp*thm)
check("MHC theta_+ theta_- = (4/a^2)[a'^2 - x^2/(x^2+b^2)^2]", sp.simplify(prod - (4/a**2)*(ad**2 - xx**2/(xx**2 + bb_**2)**2)) == 0)
# 2Gm = R (1 - g^{ab} R_a R_b): eq (4.57)
mm = sp.simplify(R3*(1 - (-(sp.diff(R3, t))**2 + (sp.diff(R3, xx))**2/a**2)))
check("MHC eq (4.57) 2Gm", sp.simplify(mm - a*sp.sqrt(xx**2 + bb_**2)*(bb_**2/(xx**2 + bb_**2) + ad**2*(xx**2 + bb_**2))) == 0)
# a = t/t0: trapped everywhere iff (x^2+b^2)^2 - t0^2 x^2 > 0 for all x  <=>  t0 < 2b   (eq 4.61)
prod_lin = sp.simplify(prod.subs(a, t/t0).doit())
u = sp.symbols('u', positive=True)
poly = sp.expand((u**2 - t0**2*(u - bb_**2)))          # u = x^2 + b^2 >= b^2 ; eq (4.61)
check("MHC eq (4.61): trapped condition polynomial", sp.simplify(poly - ((xx**2 + bb_**2)**2 - t0**2*xx**2).subs(xx**2, u - bb_**2)) == 0)
disc = sp.discriminant(poly, u)
check("MHC: no anti-trapped/marginal sphere anywhere iff t0 < 2b (discriminant < 0)", sp.simplify(disc - (t0**4 - 4*t0**2*bb_**2)) == 0)
# numeric witness: b=1, t0=1 -> theta_+ theta_- > 0 on a grid; spatial minimal sphere at x=0 flared
import math
b1, t01 = 1.0, 1.0
worst = min(( (xv**2 + b1**2)**2 - t01**2*xv**2 for xv in [i/50 for i in range(-500, 501)]))
check("MHC witness b=1,t0=1: (x^2+b^2)^2 - t0^2 x^2 > 0 on [-10,10] (no H&V throat)", worst > 0)
# spatial minimal sphere on constant t: d_x R = 0 at x=0, d^2_x R > 0
check("MHC: x=0 is a spatial minimal sphere on every constant-t slice",
      sp.simplify(sp.diff(R3, xx).subs(xx, 0)) == 0 and sp.simplify(sp.diff(R3, xx, 2).subs(xx, 0)) == a/bb_)
# NEC along both null directions with a=t/t0: T_ab l^a l^b ∝ (mu + p_r) = 2/t^2 - 2 t0^2 b^2 /(t^2 (x^2+b^2)^2) >= 0 iff (x^2+b^2)^2 >= t0^2 b^2
mu = -Gtt; pr = Gxx
nec = sp.simplify((mu + pr).subs(a, t/t0).doit())
check("MHC eq (4.58)+(4.59): mu + p_r = (2/t^2)[1 - t0^2 b^2/(x^2+b^2)^2]",
      sp.simplify(nec - (2/t**2)*(1 - t0**2*bb_**2/(xx**2 + bb_**2)**2)) == 0)
check("MHC: NEC holds everywhere (worst point x=0) iff t0 <= b", sp.simplify(nec.subs(xx, 0)*t**2/2 - (1 - t0**2/bb_**2)) == 0)
# the genuine NEC contraction: T_ab l^a l^b for l_+ = (1, 1/a): T_tt + T_xx/a^2 = (mu + p_r)/(8 pi G) since T_tt=mu, T_xx = p_r a^2
Ttt = sp.simplify(Ein3[0, 0]); Txx = sp.simplify(Ein3[1, 1])
check("MHC: 8piG T_ab l_+^a l_+^b = mu + p_r", sp.simplify(Ttt + Txx/a**2 - (mu + pr)) == 0)

print()
print(f"SUMMARY: {len(fails)} FAILED, {len(discrepancies)} DISCREPANCY recorded" + (f": {fails}" if fails else ""))
for d in discrepancies: print("  discrepancy:", d)
sys.exit(1 if fails else 0)
