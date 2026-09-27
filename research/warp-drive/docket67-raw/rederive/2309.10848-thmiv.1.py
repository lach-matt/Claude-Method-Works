#!/usr/bin/env python3
"""DOCKET 67 -- re-derivation for FFKP 2309.10848 Thm IV.1, eq. (72).

Source read: arXiv:2309.10848v1 (19 Sep 2023), cached alphaXiv full text at
  d67/src/2309.10848.txt  (pages from d67/src/casmag/all/2309.10848v1.txt).
FFKP conventions (p.5): signature (-,+,...,+); box_g := -g^{mn} nabla_m nabla_n;
Riemann R(X,Y)Z = nabla_X nabla_Y Z - ..., Ricci its (1,3) contraction; G = 8 pi G T;
"(+,+,+) according to Misner, Thorne and Wheeler".  Action (7):
  S = INT sqrt(-g) [ (R-2L)/16piG - 1/2 (nabla phi)^2 - 1/2 xi R phi^2 - m^2 phi^2/2 ].

Checks
  C1  Which Ricci sign in T_mn is the stress tensor of action (7)?  Decided by the
      OFF-SHELL Noether identity  nabla^m T_mn = -E nabla_n phi,  E = dS/dphi / sqrt(-g)
      = g^{ab} nabla_a nabla_b phi - m^2 phi - xi R phi, on a generic non-static
      4-metric diag(-a, b, c, c)(t,x) with explicit functions (exact sympy
      differentiation, numeric evaluation at points).  Two candidates:
        T9  = FFKP eq. (9)   : ... + xi (G_mn - g_mn g^{ab}nabla_a nabla_b ... ) wait: FFKP (9)
              reads xi(-g box_g - nabla nabla + G) phi^2 with box_g = -g^ab nabla nabla,
              i.e. + xi (g_mn g^ab nabla_a nabla_b - nabla_m nabla_n + G_mn) phi^2.
        T12 = FFKP eq. (12)  : Ricci term inside -2 xi(...) is +1/2 R_mn phi^2.
  C2  (9) -> (12) by FFKP's own steps (10),(11): g-part and nabla-part agree, the
      R_mn term flips sign.  Pure algebra on commuting symbols.
  C3  The smearing step (61)/(62)/(63) -> (64): for T_ll = (1-2xi)A - 2xi B + k xi R_ll phi^2,
      the Leibniz/IBP route gives  rho_n(f) = A(llf) - xi phi^2(nabla nabla(l l f) - k R_ll f),
      so the Ricci coefficient in Q[f] is -k.  (13) printed k=-1 -> +1; (61) as extracted
      k=-2 -> +2; (9) [C1-verified] k=+1 -> -1; (64)/(69b)/(72) print +1/2.
      The distributional identity (63) is verified as a total divergence (flat 2D,
      non-constant null field l).
  C4  On HPS (metric -f dt^2 + dl^2 + r^2 dOmega^2): R_mn l^m l^n for radial null
      l = f^(-1/2) d_t + d_l, general f(l), r(l); with HPS boundary data (f'=f''=f'''=0,
      r'=r''=r'''=0 at l=0) it vanishes at l=0 and is O(l^2) != 0 off the throat,
      i.e. nonzero on any open support of f.  Also g(l,l) = 0 and the hyperbolic-chart
      condition (66) near the throat.
Exit 0 always prints; exit 1 only if a check that must hold fails.
"""
import sys
import sympy as sp

ok = True
def chk(name, cond):
    global ok
    print(("PASS " if cond else "FAIL ") + name)
    ok = ok and bool(cond)

# ---------------------------------------------------------------- geometry
def christoffel(g, X):
    n = len(X); gi = g.inv()
    return [[[sp.Rational(1, 2) * sum(gi[a, d] * (sp.diff(g[d, b], X[c]) + sp.diff(g[d, c], X[b])
              - sp.diff(g[b, c], X[d])) for d in range(n)) for c in range(n)] for b in range(n)]
            for a in range(n)], gi

def ricci(G, X):
    # MTW: R^a_{bcd} = d_c G^a_{db} - d_d G^a_{cb} + G^a_{ce} G^e_{db} - G^a_{de} G^e_{cb}; R_bd = R^a_{bad}
    n = len(X)
    Ric = sp.zeros(n)
    for b in range(n):
        for d in range(n):
            s = 0
            for a in range(n):
                s += sp.diff(G[a][d][b], X[a]) - sp.diff(G[a][a][b], X[d])
                for e in range(n):
                    s += G[a][a][e] * G[e][d][b] - G[a][d][e] * G[e][a][b]
            Ric[b, d] = s
    return Ric

def hess(phi, G, X):
    n = len(X)
    return sp.Matrix(n, n, lambda m, k: sp.diff(phi, X[m], X[k])
                     - sum(G[e][m][k] * sp.diff(phi, X[e]) for e in range(n)))

def div_lower(T, G, gi, X):
    """(nabla^m T_mn) for symmetric covariant T."""
    n = len(X)
    out = []
    for nu in range(n):
        s = 0
        for m in range(n):
            for a in range(n):
                cov = sp.diff(T[a, nu], X[m]) - sum(G[e][m][a] * T[e, nu] + G[e][m][nu] * T[a, e]
                                                    for e in range(n))
                s += gi[m, a] * cov
        out.append(s)
    return out

# ---------------------------------------------------------------- C1
t, x, y, z = X = sp.symbols('t x y z', real=True)
xi, m = sp.Rational(3, 10), sp.Rational(7, 10)          # generic, non-special values
a = sp.exp(sp.Rational(3, 10) * t * x + sp.Rational(1, 10) * x**2)
b = 1 + sp.Rational(1, 5) * sp.sin(t + x)**2
c = sp.exp(sp.Rational(1, 4) * x - sp.Rational(1, 7) * t**2)
g = sp.diag(-a, b, c, c)
phi = sp.sin(t + 2 * x) + sp.Rational(1, 3) * x * t
G, gi = christoffel(g, X)
Ric = ricci(G, X)
Rs = sum(gi[i, j] * Ric[i, j] for i in range(4) for j in range(4))
H = hess(phi, G, X)
H2 = hess(phi**2, G, X)
dphi = [sp.diff(phi, v) for v in X]
grad2 = sum(gi[i, j] * dphi[i] * dphi[j] for i in range(4) for j in range(4))
boxup = sum(gi[i, j] * H[i, j] for i in range(4) for j in range(4))       # g^ab nabla nabla phi
boxup2 = sum(gi[i, j] * H2[i, j] for i in range(4) for j in range(4))
E = boxup - m**2 * phi - xi * Rs * phi                                      # EL of action (7)
Gmn = Ric - Rs * g / 2
T9 = sp.Matrix(4, 4, lambda i, j: dphi[i] * dphi[j] - g[i, j] * (m**2 * phi**2 + grad2) / 2
               + xi * (g[i, j] * boxup2 - H2[i, j] + Gmn[i, j] * phi**2))
# T12 differs from T9 only in the sign of the xi R_mn phi^2 term (C2 shows this)
T12 = T9 - 2 * xi * Ric * phi**2
pts = [(sp.Rational(1, 3), sp.Rational(1, 2)), (sp.Rational(-2, 5), sp.Rational(7, 10)),
       (sp.Rational(9, 10), sp.Rational(-3, 10))]
def resid(T, sgn):
    d = div_lower(T, G, gi, X)
    worst = 0
    for (tv, xv) in pts:
        for nu in range(4):
            val = sp.N((d[nu] + sgn * E * dphi[nu]).subs({t: tv, x: xv}), 30)
            worst = max(worst, abs(float(val)))
    return worst
r9p, r9m = resid(T9, +1), resid(T9, -1)
r12p, r12m = resid(T12, +1), resid(T12, -1)
print("C1 max |nabla^m T_mn + s E d_n phi| over 3 points x 4 components:")
print("   T9  (FFKP eq. 9):  s=+1: %.3e   s=-1: %.3e" % (r9p, r9m))
print("   T12 (FFKP eq.12):  s=+1: %.3e   s=-1: %.3e" % (r12p, r12m))
chk("C1a FFKP eq.(9) satisfies the off-shell Noether identity (conserved on shell)",
    min(r9p, r9m) < 1e-20)
chk("C1b FFKP eq.(12) Ricci sign violates it (not conserved on shell for xi != 0)",
    min(r12p, r12m) > 1e-6)

# ---------------------------------------------------------------- C2
A, B, Rc, gm, Xi, M2, R, grad, ph2, boxphi = sp.symbols('A B Ric g xi m2 R grad2 phi2 boxphi')
# symbols: A = d_m phi d_n phi, B = phi nabla_m nabla_n phi, Rc = R_mn, gm = g_mn,
# grad = (nabla phi)^2, boxphi = phi * g^ab nabla nabla phi ; on shell boxphi = (m2 + xi R) phi2
nabla2_phi2 = 2 * A + 2 * B                         # nabla_m nabla_n phi^2
gup_nabla2_phi2 = 2 * grad + 2 * boxphi             # g^ab nabla nabla phi^2
T9s = A - gm * (M2 * ph2 + grad) / 2 + Xi * (gm * gup_nabla2_phi2 - nabla2_phi2 + (Rc - gm * R / 2) * ph2)
T9s = sp.expand(T9s.subs(boxphi, (M2 + Xi * R) * ph2))
T12s = sp.expand((1 - 2 * Xi) * A - sp.Rational(1, 2) * (1 - 4 * Xi) * gm * (M2 * ph2 + Xi * R * ph2 + grad)
                 - 2 * Xi * (B + sp.Rational(1, 2) * Rc * ph2))
diff = sp.simplify(T9s - T12s)
print("C2 (9) - (12) after FFKP's own steps (10),(11):", diff)
chk("C2 (9) and (12) agree in every term except R_mn: difference = 2 xi R_mn phi^2",
    sp.simplify(diff - 2 * Xi * Rc * ph2) == 0)

# ---------------------------------------------------------------- C3
k = sp.symbols('k')
# pointwise: T_ll = (1-2xi)A_ll - 2xi B_ll + k xi R_ll phi^2 ; B_ll = 1/2 ll nabla nabla phi^2 - A_ll
# smeared with f and IBP (63): ll nabla nabla phi^2 (f) = phi^2 (nabla nabla (l l f))
Af, N2f, Rf = sp.symbols('A_f N2_f R_f')   # A(llf), phi^2(nabla nabla(llf)), phi^2(R_ll f)
rho = (1 - 2 * Xi) * Af - 2 * Xi * (N2f / 2 - Af) + k * Xi * Rf
coef_R_in_Q = sp.simplify(-sp.diff(rho, Rf) / Xi)        # rho = A_f - xi (N2f + coef*Rf)
chk("C3a smeared: rho_n(f) = A(llf) - xi[phi^2(nabla nabla(llf)) + (-k) phi^2(R_ll f)]",
    sp.simplify(rho - (Af - Xi * (N2f + coef_R_in_Q * Rf))) == 0 and sp.simplify(coef_R_in_Q + k) == 0)
table = {"eq.(9)  [C1-verified], k=+1": 1, "eq.(13) printed, k=-1": -1,
         "eq.(61) as extracted (no 1/2), k=-2": -2}
for lab, kv in table.items():
    print("   Ricci coefficient in Q[f] implied by %-36s = %s" % (lab, -kv))
print("   Ricci coefficient printed in (64)/(69b)/(72) and copied at qeihps.py:99 = 1/2")
chk("C3b printed 1/2 matches none of the coefficients implied by (9), (13) or (61)",
    all(sp.Rational(1, 2) != -kv for kv in table.values()))
# distributional identity (63) as a total divergence, flat 2D, non-constant null l
u, v = sp.symbols('u v', real=True)             # null coords, eta = -du dv (metric g_uv = -1/2)
F = sp.Function('F')(u, v); P = sp.Function('P')(u, v); al = sp.Function('al')(u, v)
lvec = [al, 0]                                  # l = al(u,v) d_u is null for any al
lhs = sum(lvec[i] * lvec[j] * F * sp.diff(P**2, [u, v][i], [u, v][j]) for i in range(2) for j in range(2))
rhs = sum(P**2 * sp.diff(lvec[i] * lvec[j] * F, [u, v][i], [u, v][j]) for i in range(2) for j in range(2))
J = [sum(lvec[i] * lvec[j] * F * sp.diff(P**2, [u, v][j]) - P**2 * sp.diff(lvec[i] * lvec[j] * F, [u, v][j])
         for j in range(2)) for i in range(2)]
divJ = sp.diff(J[0], u) + sp.diff(J[1], v)
chk("C3c (63): f l l nabla nabla phi^2 - phi^2 nabla nabla(l l f) is a total divergence",
    sp.simplify(sp.expand(lhs - rhs - divJ)) == 0)

# ---------------------------------------------------------------- C4
l_ = sp.symbols('l', real=True)
f_ = sp.Function('f')(l_); r_ = sp.Function('r')(l_)
th, ph_ = sp.symbols('theta varphi', real=True)
Xs = [t, l_, th, ph_]
gs = sp.diag(-f_, 1, r_**2, r_**2 * sp.sin(th)**2)
Gs, gis = christoffel(gs, Xs)
Rics = ricci(Gs, Xs)
lv = [f_**sp.Rational(-1, 2), 1, 0, 0]
norm = sp.simplify(sum(gs[i, j] * lv[i] * lv[j] for i in range(4) for j in range(4)))
chk("C4a g(l,l) = 0 for l = f^(-1/2) d_t + d_l (exact)", norm == 0)
Rll = sp.simplify(sum(Rics[i, j] * lv[i] * lv[j] for i in range(4) for j in range(4)))
print("C4 R_mn l^m l^n (general f(l), r(l)) =", Rll)
# HPS boundary data at l=0: f'=f''=f'''=0, r'=r''=r'''=0 ; r''''(0)/r(0) = 129600 pi^2 (2-L^2)/(L^2(3L+4))
L = sp.Rational(-2, 3)
f0 = sp.exp(L)
r4_over_r0 = 129600 * sp.pi**2 * (2 - L**2) / (L**2 * (3 * L + 4))
f4_over_f0 = 259200 * sp.pi**2 * (-L - 1) / (L * (3 * L + 4))
K2 = 1 / (5760 * sp.pi)
r0 = sp.sqrt(-16 * K2 * L)
fser = f0 * (1 + f4_over_f0 * l_**4 / 24)
rser = r0 * (1 + r4_over_r0 * l_**4 / 24)
Rll_ser = sp.series(Rll.subs({f_: fser, r_: rser}).doit(), l_, 0, 3).removeO()
Rll_ser = sp.simplify(Rll_ser)
print("C4 HPS (L=-2/3) R_ll near throat =", Rll_ser, " ~ %.6g l^2" % float(sp.N(Rll_ser.coeff(l_, 2))))
chk("C4b HPS: R_ll(0) = 0 and R_ll = O(l^2) != 0 off the throat (nonzero on any open supp f)",
    sp.simplify(Rll_ser.subs(l_, 0)) == 0 and sp.N(Rll_ser.coeff(l_, 2)) != 0)
# -2 r''/r leading => -r''''(0)/r(0) l^2 ; compare to qeihps: 8 pi (rho+p_l) = -(r''''/r) l^2
chk("C4c R_ll = 8 pi (rho + p_l) to O(l^2): -(r''''(0)/r(0)) l^2 (matches qeihps.py:174)",
    sp.simplify(Rll_ser.coeff(l_, 2) + r4_over_r0) == 0)
# hyperbolic chart (66): causal covector u: -u0^2/f + ul^2 + uth^2/r^2 + uph^2/(r^2 sin^2) <= 0
# => sum_j u_j^2 <= u0^2 * max(1, r^2, r^2 sin^2)/f  ; c = sqrt(1 + max(1, r^2)/f) works away from poles
cbound = sp.sqrt(1 + sp.Max(1, r0**2) / f0)
print("C4 hyperbolic-chart constant at the throat (theta away from poles): c = %.6g" % float(sp.N(cbound)))
chk("C4d FFKP (66) satisfiable at the throat in the static chart (finite c, d_t timelike since f(0)>0)",
    bool(sp.N(cbound) < sp.oo) and bool(f0 > 0))

# ---------------------------------------------------------------- summary
print()
print("SUMMARY: eq.(9) is the conserved stress tensor of action (7) (C1a); eq.(12)/(13)")
print("flip the sign of its xi R_mn phi^2 term (C1b, C2); the (61)->(64) step then halves")
print("or quarters it (C3).  The Q[f] printed in (69b)/(72) carries R_ll-coefficient +1/2;")
print("the coefficient consistent with (9) is -1.  The discrepancy is inert where")
print("R_mn l^m l^n = 0 on supp f (Minkowski: DSNEC/SNEC (75)-(93)) or xi = 0, and live")
print("on HPS's throat neighbourhood (C4b).  Not a refutation of (72): no state violating")
print("the printed bound is exhibited; the bound is not sharp (FFKP p.19).")
sys.exit(0 if ok else 1)
