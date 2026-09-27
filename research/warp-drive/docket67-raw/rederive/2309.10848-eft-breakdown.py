#!/usr/bin/env python3
"""DOCKET 67 -- re-derivation for key 2309.10848-eft-breakdown.

FFKP (Fliss, Freivogel, Kontou, Pardo Santos, arXiv:2309.10848v1) Sec. V: the field
bound phi^2_max <~ (8 pi G |xi|)^-1 and the loss of control beyond it.

  A. Jordan frame, constrained saddle: re-derive (116), (117), (119), (121) from the
     printed action (109) and saddle equations (114); check the n=4 de Sitter limit;
     show I -> 0 and G_eff = G/(1-8 pi G xi phibar^2) -> infinity as x -> 1 (xi > 0),
     Lambda_eff < 0 for x > 1; and for xi < 0 that none of this happens.
  B. Einstein frame: re-derive (106)-(107) (n=4 potential expansion), and locate where
     the field redefinition becomes singular (xi > 0 only).
  C. The tree's use: combine FFKP's field bound (8 pi G |xi| phi^2_max = eps) with the
     SNEC-closure arithmetic of candidates.py (shortfall = (l_UV/l_P)^2/(N Lambda)),
     using the sibling audit's Gaussian N_4 = 1/pi^2 + K s, s = |xi| phi~^2_max,
     phi^2_max = phi~^2 / l_UV^2  (FFKP H9).  Ask: does the FIELD bound alone exclude
     every closure point, as 'fails on the EFT field cutoff' says?
"""
import sympy as sp

ok = True
def chk(name, cond):
    global ok
    ok = ok and bool(cond)
    print(("PASS " if cond else "FAIL ") + name)

# ---------------------------------------------------------------- A. Jordan frame
n, G, Lam, m, xi, pb = sp.symbols('n G Lambda m xi phibar', real=True)
x = 8*sp.pi*G*xi*pb**2
# trace of (114) at constant phi = phibar: (1-x) G_mn + Lam g_mn - 8piG T_mn = 0,
# T_mn = -(1/2) g_mn m^2 phibar^2 (constraint term vanishes at phi = phibar)
# => G_mn = -Lam_eff g_mn, Lam_eff = (Lam + 4 pi G m^2 pb^2)/(1-x)
Lam_eff = (Lam + 4*sp.pi*G*m**2*pb**2)/(1 - x)
Rs = sp.Symbol('R')
# G_mn = R_mn - R g/2 with R_mn = (R/n) g (homogeneous): trace -> R(1-n/2) = -n Lam_eff
Rsol = sp.solve(sp.Eq(Rs*(1 - n/2), -n*Lam_eff), Rs)[0]
Rmn = sp.simplify(Rsol/n)
chk("A1 (116): R_mn = 2/(n-2) (Lam+4piG m^2 pb^2)/(1-x) g_mn",
    sp.simplify(Rmn - 2/(n-2)*Lam_eff) == 0)
ell2 = sp.simplify((n-1)/Rmn)              # S^n of radius ell: R_mn = (n-1)/ell^2 g
chk("A2 (117): ell^2 = (n-2)(n-1)/2 * (1-x)/(Lam+4piG m^2 pb^2)",
    sp.simplify(ell2 - (n-2)*(n-1)/2*(1-x)/(Lam + 4*sp.pi*G*m**2*pb**2)) == 0)
# on-shell Lagrangian of (109) with V = 0 at the saddle:
L = -(Rsol*(1 - x) - 2*Lam)/(16*sp.pi*G) + m**2*pb**2/2
chk("A3 (119): I/vol = -(1/(n-2)) (Lam/(4 pi G) + m^2 pb^2)",
    sp.simplify(L + (Lam/(4*sp.pi*G) + m**2*pb**2)/(n-2)) == 0)
Vn = 2*sp.pi**((n+1)/2)/sp.gamma((n+1)/2)
Vnm2 = 2*sp.pi**((n-1)/2)/sp.gamma((n-1)/2)
I = Vn*ell2**(n/2)*L
I121 = -Vnm2/(4*G)*((n-1)*(n-2)/2)**((n-2)/2)*(1-x)**(n/2)*(Lam+4*sp.pi*G*m**2*pb**2)**((2-n)/2)
for nv in (3, 4, 5, 6):
    sub = {n: nv, G: sp.Rational(1, 7), Lam: sp.Rational(3, 2), m: sp.Rational(1, 3),
           xi: sp.Rational(1, 5), pb: sp.Rational(1, 2)}
    chk("A4 (121) equals Vol*L at n=%d (reading V_{n-2}, S^{n-2} area)" % nv,
        abs(sp.N(I.subs(sub) - I121.subs(sub), 30)) < 1e-25)
dS = sp.simplify(I.subs({n: 4, m: 0, xi: 0}))
chk("A5 n=4, m=xi=0: I = -3 pi/(G Lam) (Euclidean de Sitter)", sp.simplify(dS + 3*sp.pi/(G*Lam)) == 0)
X = sp.Symbol('X', positive=True)      # X = 8 pi G xi pb^2
I4 = I121.subs(n, 4)
I4X = I4.subs(pb**2, X/(8*sp.pi*G*xi)).subs(pb, sp.sqrt(X/(8*sp.pi*G*xi)))
lim = sp.limit(sp.simplify(I4X.subs({G: 1, Lam: 1, m: 1, xi: sp.Rational(1, 6)})), X, 1, '-')
chk("A6 xi>0: on-shell action -> 0 as 8piG xi pb^2 -> 1 from below (limit = %s)" % lim, lim == 0)
Geff = G/(1 - X)
chk("A7 xi>0: G_eff = G/(1-X) -> +oo as X -> 1-", sp.limit(Geff.subs(G, 1), X, 1, '-') == sp.oo)
chk("A8 xi>0, X>1: Lam_eff < 0 (hyperbolic saddle, 'lay dragons')",
    sp.N(Lam_eff.subs({G: 1, Lam: 1, m: 1, xi: sp.Rational(1, 6)}).subs(pb, sp.sqrt(2*6/(8*sp.pi)))) < 0)
# xi < 0: 1 - x = 1 + 8 pi G |xi| pb^2 >= 1, no critical value; ell^2 grows; I -> -oo
In = I121.subs({n: 4, G: 1, Lam: 1, m: 1, xi: -sp.Rational(1, 6)})
vals = [sp.N(In.subs(pb, v)) for v in (0, 1, 10, 100)]
print("     xi=-1/6, n=4: I at pb = 0,1,10,100:", [float(v) for v in vals])
chk("A9 xi<0: no critical value; -I grows without bound, so exp(-I) integrated over d(pb^2) diverges "
    "(FFKP's non-normalisability) -- the xi>0 breakdown mechanism is absent",
    all(vals[i+1] < vals[i] for i in range(3)))
# growth rate: -I ~ pb^4/pb^2 = pb^2 at large pb for n=4
Ilarge = sp.limit(In/pb**2, pb, sp.oo)
print("     xi=-1/6: lim I/pb^2 =", Ilarge)
chk("A10 xi<0: I ~ -c pb^2 (c>0) => integrand e^{+c pb^2}: non-normalisable", Ilarge < 0)

# ---------------------------------------------------------------- B. Einstein frame, n = 4
ph, ch = sp.symbols('phi chi', real=True)
k = 8*sp.pi*G
Om2 = 1 - k*xi*ph**2
U = Lam/k + m**2*ph**2/2
dchi2 = (Om2 + sp.Rational(3, 2)/k*sp.diff(Om2, ph)**2)/Om2**2   # (dchi/dphi)^2, n=4
chk("B1 (dchi/dphi)^2 = [1 + 8piG xi(6xi-1) phi^2]/Omega^4  (xi_c = 1/6)",
    sp.simplify(dchi2 - (1 + k*xi*(6*xi - 1)*ph**2)/Om2**2) == 0)
dchi = sp.series(sp.sqrt(dchi2), ph, 0, 6).removeO()
chi_of_phi = sp.integrate(dchi, ph)
# invert to O(chi^5)
a3, a5 = sp.symbols('a3 a5')
phi_of_chi = ch + a3*ch**3 + a5*ch**5
eq = sp.expand(sp.series(chi_of_phi.subs(ph, phi_of_chi), ch, 0, 6).removeO() - ch)
sol = sp.solve([eq.coeff(ch, 3), eq.coeff(ch, 5)], [a3, a5], dict=True)[0]
phi_of_chi = phi_of_chi.subs(sol)
Ut = sp.series((U/Om2**2).subs(ph, phi_of_chi), ch, 0, 6).removeO()
Ut = sp.expand(Ut)
c2 = sp.simplify(Ut.coeff(ch, 2)); c4 = sp.simplify(Ut.coeff(ch, 4))
xic = sp.Rational(1, 6)
chk("B2 (107): m_eff^2 = m^2 + 4 xi Lam", sp.simplify(2*c2 - (m**2 + 4*xi*Lam)) == 0)
lam_paper = 4*(m**2*(5 - xi/xic) + 2*Lam*xi*(7 - 2*xi/xic))*(k*xi)
print("     derived lambda = 24*c4 =", sp.factor(24*c4))
print("     printed (107) lambda  =", sp.factor(lam_paper))
chk("B3 (107): quartic lambda = 4[m^2(5-xi/xi_c) + 2 Lam xi(7-2xi/xi_c)](8piG xi)",
    sp.simplify(24*c4 - lam_paper) == 0)
# singularity of the map: chi(phi) diverges at Omega^2 = 0 (xi>0): integrand ~ 1/Omega^2 there
num = sp.sqrt(Om2 + sp.Rational(3, 2)/k*sp.diff(Om2, ph)**2)   # = sqrt(dchi2)*Omega^2, xi>0
at_crit = sp.simplify(num.subs(ph, 1/sp.sqrt(k*xi)))
print("     sqrt(dchi2)*Omega^2 at phi^2 = (8piG xi)^-1:", at_crit)
chk("B4 xi>0: dchi/dphi ~ const/Omega^2 at the critical value (chi -> oo, Einstein-frame map singular)",
    sp.simplify(at_crit.subs({G: 1, xi: sp.Rational(1, 6)})) != 0)

# ---------------------------------------------------------------- C. the tree's use
LAMBDA = 9.982529174194637          # overturn.py:397 (tree-internal)
K = 4*sp.sqrt(2/sp.pi)*sp.exp(-sp.Rational(1, 2))  # sibling audit rederive E2 (Gaussian, n=4)
Kf = float(K)
print("     K = %.6f, Lambda = %.12f" % (Kf, LAMBDA))
s = sp.Symbol('s', nonnegative=True)             # s = |xi| phi~^2_max
N4 = 1/sp.pi**2 + K*s
# closure: (l_UV/l_P)^2 = N4 * Lambda ; field parameter eps = 8 pi |xi| phi^2_max l_P^2
#        = 8 pi s (l_P/l_UV)^2 = 8 pi s / (N4 Lambda)
eps = 8*sp.pi*s/(N4*LAMBDA)
eps_inf = float(sp.limit(eps, s, sp.oo))
chk("C1 eps(s) increasing, eps(0)=0, eps(oo) = 8pi/(K Lambda) = %.4f (sibling F2: 1.3006)" % eps_inf,
    abs(eps_inf - 1.3006) < 1e-3 and sp.simplify(sp.diff(eps, s)) .subs(s, 1) > 0)
s1 = sp.N(LAMBDA/(sp.pi**2*(8*sp.pi - K*LAMBDA)))
chk("C1b closed-form root agrees with eps(s1) = 1", abs(sp.N(eps.subs(s, s1)) - 1) < 1e-12)
lUV1 = float(sp.sqrt(N4.subs(s, s1)*LAMBDA))
print("     eps = 1 at s = %.6f, closure l_UV = %.6f l_P" % (s1, lUV1))
for e in (0.01, 0.1, 0.5, 1.0):
    se = e*LAMBDA/(sp.pi**2*(8*sp.pi - e*K*LAMBDA))   # closed-form root of eps(s) = e
    print("     eps = %-4s : s = %.6f, closure at l_UV = %.6f l_P" % (e, se, float(sp.sqrt(N4.subs(s, se)*LAMBDA))))
chk("C2 closure points with eps < 1 EXIST (0 <= s < %.4f, l_UV in [%.6f, %.6f) l_P): the FIELD bound "
    "alone does not exclude them" % (s1, float(sp.sqrt(LAMBDA/sp.pi**2)), lUV1), s1 > 0 and lUV1 > 1)
chk("C3 every closure point with eps < 1 has l_UV < %.4f l_P, i.e. a Planckian MOMENTUM cutoff: the exclusion "
    "rests on 'an EFT cut off at a few l_P is not an EFT' (candidates.py:222-225), not on the field bound"
    % lUV1, lUV1 < 2.1)
# tree's N = 1 point
s_tree = float((1 - 1/sp.pi**2)/K)
eps_tree = float(eps.subs(s, s_tree))
print("     tree N=1 <-> s = %.4f (sibling E3: 0.4642); eps there = %.4f" % (s_tree, eps_tree))
chk("C4 at the tree's own N=1 closure (l_UV = 3.1595 l_P) eps = %.3f > 1: the field bound IS exceeded, "
    "by a factor %.2f only" % (eps_tree, eps_tree), eps_tree > 1 and abs(s_tree - 0.4642) < 1e-3)
# N = 1 fixed-coefficient version (tree's literal arithmetic): eps = 8 pi s/Lambda; exceeded iff s > Lambda/(8pi)
print("     tree literal (N=1 fixed, s free): eps = 8 pi s / Lambda > 1 iff s > %.4f" % (LAMBDA/(8*3.141592653589793)))

print("\nREDERIVE PASS" if ok else "\nREDERIVE FAIL")
