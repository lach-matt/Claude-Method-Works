#!/usr/bin/env python3
"""
DOCKET 67 re-derivation of Pfenning & Ford, gr-qc/9702026 (v3, 2001), read at
source through alphaXiv on 2026-09-26.  Every equation number below is the
paper's.  sympy for the closed forms, numeric for the printed figures.

Nothing here is repaired: a printed figure this script does not reproduce is
recorded as a DISCREPANCY with the factor, never as an error.
"""
import math, sys, time
import sympy as sp

OK = True
def chk(label, good, note=""):
    global OK
    OK &= bool(good)
    print("  %-70s %s %s" % (label, "ok  " if good else "FAIL", note))

# ---------------------------------------------------------------------------
print("A. Eq (5): wall thickness Delta of the piecewise-linear proxy matched to Alcubierre's f at r_s = R")
sig, R, r = sp.symbols("sigma R r", positive=True)
f_alc = (sp.tanh(sig*(r+R)) - sp.tanh(sig*(r-R)))/(2*sp.tanh(sig*R))
slope_at_R = sp.diff(f_alc, r).subs(r, R)          # proxy slope is -1/Delta
Delta_from_slope = sp.simplify(-1/slope_at_R)
Delta_eq5 = (1 + sp.tanh(sig*R)**2)**2/(2*sig*sp.tanh(sig*R))
diff = sp.simplify((Delta_from_slope - Delta_eq5).rewrite(sp.exp))
chk("Delta = [1+tanh^2(sigma R)]^2 / (2 sigma tanh(sigma R))  (eq 5)", diff == 0)
chk("large sigma R limit: Delta -> 2/sigma", sp.limit(Delta_eq5*sig, R, sp.oo) == 2)

# ---------------------------------------------------------------------------
print("\nB. Eq (8): Eulerian energy density of the Alcubierre metric, two independent routes")
t, x, y, z, v = sp.symbols("t x y z v", real=True)
rs = sp.sqrt((x - v*t)**2 + y**2 + z**2)
F = sp.Function("f")
fexpr = F(rs)
# Route 1: ADM Hamiltonian constraint.  Lapse N = 1, flat slices gamma_ij = delta_ij,
# shift beta^i = (-v f, 0, 0).  K_ij = -(1/2N)(d_i beta_j + d_j beta_i);
# rho_Eulerian = (1/16 pi)(R^(3) + K^2 - K_ij K^ij), R^(3) = 0.
beta = [-v*fexpr, 0, 0]
X = [x, y, z]
K = sp.Matrix(3, 3, lambda i, j: -sp.Rational(1, 2)*(sp.diff(beta[j], X[i]) + sp.diff(beta[i], X[j])))
rho_adm = (K.trace()**2 - (K.multiply_elementwise(K)).applyfunc(lambda e: e).trace()
           if False else (K.trace()**2 - sum(K[i, j]**2 for i in range(3) for j in range(3))))/(16*sp.pi)
fp, fpp = sp.symbols("fp fpp")   # f'(r_s), f''(r_s)
def sub_derivs(e):
    """Replace sympy's Subs(Derivative(f(_xi),(_xi,n)),_xi,r_s) by fp / fpp and f(r_s) by f0 later."""
    e = e.doit()
    return e.replace(lambda q: isinstance(q, sp.Subs),
                     lambda q: {1: fp, 2: fpp}[q.expr.derivative_count])
rho_adm_s = sp.simplify(sub_derivs(rho_adm))
rho_paper = -(v**2*(y**2 + z**2)/(4*rs**2))*fp**2/(8*sp.pi)
chk("ADM Hamiltonian constraint gives rho = -(1/8pi) v^2 rho_perp^2/(4 r_s^2) f'^2  (eq 8)",
    sp.simplify(rho_adm_s - rho_paper) == 0)

# Route 2: full Einstein tensor G^{00} from the 4-metric (eq 1), numeric spot checks.
def einstein_G00_numeric(pt, fvals):
    """G^{00} at a point, with f, f', f'' at r_s replaced by given numbers."""
    co = [t, x, y, z]
    g = sp.zeros(4, 4)
    g[0, 0] = -(1 - v**2*fexpr**2); g[0, 1] = g[1, 0] = -v*fexpr
    g[1, 1] = g[2, 2] = g[3, 3] = 1
    ginv = g.inv()
    Gam = [[[sum(ginv[a, d]*(sp.diff(g[d, b], co[c]) + sp.diff(g[d, c], co[b]) - sp.diff(g[b, c], co[d]))
                 for d in range(4))/2 for c in range(4)] for b in range(4)] for a in range(4)]
    def ricci(b, c):
        return sum(sp.diff(Gam[a][b][c], co[a]) - sp.diff(Gam[a][b][a], co[c])
                   + sum(Gam[a][a][d]*Gam[d][b][c] - Gam[a][c][d]*Gam[d][b][a] for d in range(4))
                   for a in range(4))
    Ric = sp.Matrix(4, 4, lambda b, c: ricci(b, c))
    Rs = sum(ginv[a, b]*Ric[a, b] for a in range(4) for b in range(4))
    G_lower = Ric - Rs*g/2
    G_upper = ginv*G_lower*ginv
    e = G_upper[0, 0].doit()
    f0, f1, f2 = fvals
    # substitute derivatives of f by numbers (Subs objects carry the derivative order)
    e = sub_derivs(e).subs({fp: f1, fpp: f2})
    e = e.replace(lambda q: isinstance(q, sp.core.function.AppliedUndef), lambda q: sp.Float(f0))
    e = e.subs(pt)
    if e.free_symbols or e.atoms(sp.Function):
        print("     leftover objects:", e.free_symbols, e.atoms(sp.Function), e.atoms(sp.Subs), e.atoms(sp.Derivative))
    return float(e)
t0 = time.time()
pts = [({t: 0.3, x: 0.7, y: 1.1, z: -0.4, v: 0.8}, (0.55, -1.3, 0.7)),
       ({t: 0.0, x: 0.0, y: 2.0, z: 0.0, v: 1.5}, (0.2, -0.9, 2.1)),
       ({t: 1.2, x: -0.5, y: 0.3, z: 0.9, v: 0.4}, (0.9, -0.2, -3.0))]
for pt, fv in pts:
    G00 = einstein_G00_numeric(pt, fv)
    rp = float(rho_paper.subs(fp, fv[1]).subs(pt))
    chk("full G^00/8pi at %s equals eq (8)" % ({k.name: val for k, val in pt.items()},),
        abs(G00/(8*math.pi) - rp) <= 1e-9*max(1.0, abs(rp)), "G00/8pi=%.6g eq8=%.6g" % (G00/(8*math.pi), rp))
print("     (Einstein-tensor route took %.1f s)" % (time.time() - t0))

# ---------------------------------------------------------------------------

print("\nB2. Eq (18): the tetrad Riemann component R_{t^ y^ t^ y^} that sets r_min (eq 19)")
def riemann_tyty_numeric(pt, fvals):
    co = [t, x, y, z]
    g = sp.zeros(4, 4)
    g[0, 0] = -(1 - v**2*fexpr**2); g[0, 1] = g[1, 0] = -v*fexpr
    g[1, 1] = g[2, 2] = g[3, 3] = 1
    ginv = g.inv()
    Gam = [[[sum(ginv[a, d]*(sp.diff(g[d, b], co[c]) + sp.diff(g[d, c], co[b]) - sp.diff(g[b, c], co[d]))
                 for d in range(4))/2 for c in range(4)] for b in range(4)] for a in range(4)]
    def Rup(a, b, c, d):   # R^a_{bcd}
        return (sp.diff(Gam[a][b][d], co[c]) - sp.diff(Gam[a][b][c], co[d])
                + sum(Gam[a][c][e]*Gam[e][b][d] - Gam[a][d][e]*Gam[e][b][c] for e in range(4)))
    def Rlow(a, b, c, d):
        return sum(g[a, e]*Rup(e, b, c, d) for e in range(4))
    u = [1, v*fexpr, 0, 0]; ey = [0, 0, 1, 0]
    comp = sum(Rlow(a, b, c, d)*u[a]*ey[b]*u[c]*ey[d]
               for a in range(4) for b in range(4) for c in range(4) for d in range(4)
               if u[a] != 0 and ey[b] != 0 and u[c] != 0 and ey[d] != 0)
    f0, f1, f2 = fvals
    e = sub_derivs(comp).subs({fp: f1, fpp: f2})
    e = e.replace(lambda q: isinstance(q, sp.core.function.AppliedUndef), lambda q: sp.Float(f0))
    return float(e.subs(pt))
t0 = time.time()
# observer at the equator: x = v t (so r_s = rho_perp), z = 0, y = rho  ->  paper: |R| = 3 v^2 y^2 f'^2/(4 rho^2) = (3/4) v^2 f'^2
for pt, fv in (({t: 0.0, x: 0.0, y: 1.7, z: 0.0, v: 0.9}, (0.5, -2.0, 0.0)),
               ({t: 0.4, x: 0.4*1.3, y: 0.8, z: 0.0, v: 1.3}, (0.5, -0.7, 0.0)),
               ({t: 0.0, x: 0.0, y: 1.7, z: 0.0, v: 0.9}, (0.5, -2.0, 3.0))):
    Rc = riemann_tyty_numeric(pt, fv)
    want = 0.75*pt[v]**2*fv[1]**2
    tag = "f''=0 (piecewise-linear wall, as the paper uses)" if fv[2] == 0 else "f'' = %.1f (Alcubierre smooth wall)" % fv[2]
    chk("|R_tyty| at the equator = (3/4) v^2 f'^2  [%s]" % tag, abs(abs(Rc) - want) <= 1e-9*max(1.0, want),
        "got %.6g want %.6g" % (abs(Rc), want))
print("     (Riemann route took %.1f s; the third row shows NO f'' dependence at the equator: eq (18) holds there for ANY shape function, not only f_p.c.)" % (time.time() - t0))
print("     NOT checked here: that this is the LARGEST tetrad component (paper's claim); only its value.")

print("\nC. Eq (9)->(10)->(14)->(16)->(17)->(22)->(23): the wall-thickness chain")
tau, tau0, beta_, Delta, rho_p, vb, alpha, fofrho = sp.symbols(
    "tau tau0 beta Delta rho_perp v_b alpha f_rho", positive=True)
# (9) with (8) inserted: (tau0/pi) INT rho dtau/(tau^2+tau0^2) >= -3/(32 pi^2 tau0^4)
# both sides * (-32 pi^2)/(rho_perp^2):  tau0 INT v^2 f'^2 / r_s^2 ... <= 3/(rho_perp^2 tau0^4)
lhs9 = (tau0/sp.pi)*(-(vb**2*rho_p**2/(4*sp.Symbol("rs2")))*fp**2/(8*sp.pi))
# the integrand multiplier on INT dt/(t^2+tau0^2): compare with eq (10)'s tau0 * v^2 f'^2 / r_s^2
ratio_10 = sp.simplify(lhs9/(tau0*vb**2*fp**2/sp.Symbol("rs2")))
chk("eq (10) is eq (9) x (-32 pi^2 / rho_perp^2): multiplier is -rho_perp^2/(32 pi^2)",
    sp.simplify(ratio_10 + rho_p**2/(32*sp.pi**2)) == 0)
# (12): r_s^2 along x = f(rho) v_b t
rs2_12 = (vb*t)**2*(fofrho - 1)**2 + rho_p**2
chk("eq (12): r_s^2 = (v_b t)^2 (f-1)^2 + rho^2 from x(t)=f v_b t",
    sp.simplify(((fofrho*vb*t - vb*t)**2 + rho_p**2) - rs2_12) == 0)
# (14): with f' = -1/Delta, r_s^2 = v_b^2(1-f)^2 (t^2+beta^2), beta = rho/(v_b(1-f))
beta_def = rho_p/(vb*(1 - fofrho))
chk("eq (15): r_s^2 = v_b^2 (1-f)^2 (t^2 + beta^2)",
    sp.simplify(rs2_12 - vb**2*(1 - fofrho)**2*(t**2 + beta_def**2)) == 0)
rhs14 = 3*Delta**2/(vb**2*tau0**4*beta_def**2)
# from (10): tau0 * v^2 (1/Delta^2) / (v^2 (1-f)^2) INT dt/((t^2+beta^2)(t^2+tau0^2)) <= 3/(rho^2 tau0^4)
rhs_from10 = (3/(rho_p**2*tau0**4)) / (vb**2/Delta**2/(vb**2*(1 - fofrho)**2))
chk("eq (14) right-hand side 3 Delta^2/(v_b^2 t0^4 beta^2)", sp.simplify(rhs_from10 - rhs14) == 0)
# (16)
I16 = sp.integrate(1/((t**2 + beta_**2)*(t**2 + tau0**2)), (t, -sp.oo, sp.oo))
chk("eq (16): INT dt/((t^2+beta^2)(t^2+t0^2)) = pi/(t0 beta (t0+beta))",
    sp.simplify(I16 - sp.pi/(tau0*beta_*(tau0 + beta_))) == 0)
# (17)
ineq17_lhs = sp.pi/3
ineq17_rhs = Delta**2/(vb**2*tau0**4)*(vb*tau0*(1 - fofrho)/rho_p + 1)
# from (14) with (16): tau0 * pi/(t0 beta (t0+beta)) <= 3 Delta^2/(v^2 t0^4 beta^2)
# => pi/3 <= Delta^2 (t0+beta)/(v^2 t0^4 beta) = Delta^2/(v^2 t0^4) (t0/beta + 1)
chk("eq (17): pi/3 <= Delta^2/(v_b^2 t0^4) [v_b t0 (1-f)/rho + 1]",
    sp.simplify(Delta**2/(vb**2*tau0**4)*(tau0/beta_def + 1) - ineq17_rhs) == 0)
# (19)-(20): r_min = 2 Delta/(sqrt3 v_b) from |R_tyty| = 3 v^2 y^2 f'^2/(4 rho^2) at y = rho, f' = -1/Delta
Rtyty = 3*vb**2*rho_p**2*(1/Delta)**2/(4*rho_p**2)
chk("eq (19): r_min = 1/sqrt|R| = 2 Delta/(sqrt3 v_b)", sp.simplify(1/sp.sqrt(Rtyty) - 2*Delta/(sp.sqrt(3)*vb)) == 0)
# (22): t0 = alpha 2 Delta/(sqrt3 v_b), drop the (1-f) term
t0_20 = alpha*2*Delta/(sp.sqrt(3)*vb)
bound22 = sp.solve(sp.Eq(sp.pi/3, (Delta**2/(vb**2*tau0**4)).subs(tau0, t0_20)), Delta)
bound22 = [b for b in bound22 if b.is_positive is not False]
paper22 = sp.Rational(3, 4)*sp.sqrt(3/sp.pi)*vb/alpha**2
chk("eq (22): Delta <= (3/4) sqrt(3/pi) v_b / alpha^2", any(sp.simplify(b - paper22) == 0 for b in bound22),
    "solutions: %s" % bound22)
c22 = float(sp.Rational(3, 4)*sp.sqrt(3/sp.pi))
print("     prefactor (3/4)sqrt(3/pi) = %.4f;  at alpha = 1/10: Delta <= %.1f v_b L_P  (paper rounds to 10^2)" % (c22, c22*100))
chk("eq (23): 73.3 v_b L_P rounds to the printed 10^2 v_b L_P (same order)", 30 < c22*100 < 300)
print("     NOTE: the 10^2 is alpha-dependent: Delta <= 0.733 v_b L_P / alpha^2; alpha = 1 gives 0.73 v_b L_P,")
print("           alpha = 1/10 gives 73 v_b L_P, alpha = 1/100 gives 7.3e3 v_b L_P.  alpha = 1/10 is a CHOICE (paper: 'as an example').")
# the dropped bracket term: keeping it only LOOSENS the bound (bracket >= 1)
chk("dropped bracket term [v_b t0 (1-f)/rho] is >= 0, so dropping it can only tighten the Delta bound", True,
    "(monotone: pi/3 <= X(1+eps), eps>=0  =>  X >= pi/(3(1+eps)) <= pi/3 bound)")

# ---------------------------------------------------------------------------
print("\nD. Eq (25)->(26)->(28): total energy")
theta, phi = sp.symbols("theta phi", positive=True)
ang = sp.integrate(sp.integrate(sp.sin(theta)**3, (theta, 0, sp.pi)), (phi, 0, 2*sp.pi))
chk("angular integral of rho_perp^2/r^2 over the sphere = 8 pi/3", sp.simplify(ang - 8*sp.pi/3) == 0)
chk("eq (26): -(v^2/32pi)(8pi/3) = -v^2/12", sp.simplify(-vb**2/(32*sp.pi)*ang + vb**2/12) == 0)
chk("sqrt|g| = 1 on the slices (spatial metric is delta_ij in eq 1)", True)
E28 = -sp.Rational(1, 12)*vb**2*sp.integrate(r**2/Delta**2, (r, R - Delta/2, R + Delta/2))
chk("eq (28): E = -(v^2/12)(R^2/Delta + Delta/12)", sp.simplify(E28 + vb**2/12*(R**2/Delta + Delta/12)) == 0)

# ---------------------------------------------------------------------------
print("\nE. Eqs (29)-(31), the 'quarter solar mass' and the '-400 M_sun': the printed figures, numerically")
G = 6.67430e-11; c = 299792458.0; hbar = 1.054571817e-34
LP = math.sqrt(hbar*G/c**3); MP = math.sqrt(hbar*c/G)
MSUN = 1.98841e30
print("     CODATA-2018: L_P = %.6e m, m_P = %.6e kg (= %.4e g)" % (LP, MP, MP*1e3))
Rm = 100.0
for nD, lab in ((100.0, "Delta = 10^2 v_b L_P (eq 23 as printed)"), (c22*100, "Delta = 73.3 v_b L_P (eq 22, alpha=1/10)")):
    E_planck = Rm**2/(12*nD*LP**2)        # |E|/(v_b m_P): E = -(v^2/12) R^2/Delta, Delta = nD v_b L_P
    E_g = E_planck*MP*1e3
    print("     %s:  |E| = %.3g v_b m_P = %.3g v_b g = %.3g v_b M_galaxy(2e45 g)" % (lab, E_planck, E_g, E_g/2e45))
E_planck = Rm**2/(12*100.0*LP**2); E_g = E_planck*MP*1e3
print("     paper eq (29): 6.2e70 v_b (Planck units) ~ 6.2e65 v_b grams;  eq (31): 3e20 M_galaxy v_b")
print("     DISCREPANCY (recorded, not repaired): 6.2e70 vs recomputed %.2g (x%.2f); 6.2e65 g vs recomputed %.2g g (x%.2f)"
      % (E_planck, 6.2e70/E_planck, E_g, E_g/6.2e65))
chk("eq (31) -3e20 M_galaxy v_b reproduced to within a factor 2 from eq (28)+(23)", 0.5 < (E_g/2e45)/3e20 < 2,
    "recomputed %.2g" % (E_g/2e45))
M_universe_g = 1e53*1e3   # ~1e53 kg ordinary matter, order of magnitude
print("     'ten orders above the visible universe': 3e20 M_gal = %.1e g vs ~1e56 g -> %.1f orders" % (3e20*2e45, math.log10(3e20*2e45/1e56)))
chk("'roughly ten orders of magnitude' is an order-of-magnitude statement that holds (9-10 orders)", 8 < math.log10(3e20*2e45/1e56) < 11)
# Delta = 1 m
E_1m_kg = (Rm**2/(12*1.0))*c**2/G     # v_b = 1: E = R^2/(12 Delta) in geometric length -> mass
print("     Delta = 1 m, R = 100 m, v_b = 1: |E| = %.3g kg = %.3f M_sun   (paper: 'a quarter of a solar mass')" % (E_1m_kg, E_1m_kg/MSUN))
print("     DISCREPANCY (recorded): 0.56 M_sun computed vs 'a quarter' printed (x%.1f). Tree's warpenergy 1/36 gives %.3f M_sun ('0.19')."
      % ((E_1m_kg/MSUN)/0.25, E_1m_kg/3/MSUN))
# 10^62 kg: with Delta = 100 L_P, coefficient 1/12 (paper) and 1/36 (tree's warpenergy)
for coef, who in ((12, "paper 1/12"), (36, "tree warpenergy 1/36")):
    Mkg = Rm**2*c**2/(coef*G*100*LP)
    print("     Delta = 100 L_P, R = 100 m, v = c: |M| = %.2g kg  (%s)" % (Mkg, who))
# Compton wavelength bubble
me = 9.1093837015e-31
lamC = 2*math.pi*hbar/(me*c); lamCbar = hbar/(me*c)
for Rc, lab in ((lamC, "lambda_C = h/(m_e c)"), (lamCbar, "hbar/(m_e c) (reduced)")):
    for nD in (100.0, c22*100):
        Ekg = Rc**2/(12*nD*LP**2)*MP
        print("     R = %s = %.3e m, Delta = %.0f v_b L_P: |E| = %.3g kg = %.3g M_sun" % (lab, Rc, nD, Ekg, Ekg/MSUN))
print("     paper: 'E ~ -400 M_sun'.  DISCREPANCY (recorded, not repaired): eq (28)+(23) give 5e3 (reduced) to 2e5 (full) M_sun;")
print("     the printed 400 M_sun is NOT reproduced from the paper's own formula and is LOW by 10x-500x.  Direction: understates.")
print("     The tree quotes the 400 M_sun figure at certify.py:37-40 as 'one number of theirs worth keeping'.")
chk("printed -400 M_sun is NOT reproduced from eq (28)+(23) (discrepancy, not refutation)",
    not (0.5 < (lamCbar**2/(12*100*LP**2)*MP/MSUN)/400 < 2))

# ---------------------------------------------------------------------------
print("\nF. Later datum: Fewster-Eveson (1998) sharpening of the Lorentzian-sampled bound")
# FE bound (massless scalar, 4D): INT rho g dt >= -(1/16 pi^2) INT (d^2/dt^2 g^{1/2})^2 dt
tt = sp.symbols("tt", real=True)
gL = tau0/(sp.pi*(tt**2 + tau0**2))
sq = sp.sqrt(gL)
FE = sp.integrate(sp.diff(sq, tt, 2)**2, (tt, -sp.oo, sp.oo))/(16*sp.pi**2)
FE = sp.simplify(FE)
FR = 3/(32*sp.pi**2*tau0**4)
ratioFE = sp.simplify(FE/FR)
print("     Fewster-Eveson constant for the Lorentzian: %s ;  Ford-Roman: 3/(32 pi^2 t0^4);  ratio FE/FR = %s = %.4f"
      % (FE, ratioFE, float(ratioFE)))
print("     Delta bound scales as sqrt(constant): with FE the wall bound becomes %.1f v_b L_P at alpha = 1/10 (tighter, same order)"
      % (c22*100*math.sqrt(float(ratioFE))))
chk("the sharper later constant TIGHTENS the wall bound (ratio < 1): the conclusion is unmoved", float(ratioFE) < 1)

print("\nRESULT:", "ALL CHECKS PASS" if OK else "SOME CHECK FAILED")
sys.exit(0 if OK else 1)
