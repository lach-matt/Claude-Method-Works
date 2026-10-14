#!/usr/bin/env python3
"""DOCKET 67 re-derivation: Milton arXiv:1005.0031 'properly traceless' (eq. 58), as tolman.py uses it.

Read-only with respect to the research tree (it only greps tolman.py for the A_EM line).
Signature (-,+,+,+).  Sections:
 A  Maxwell T^mu_mu = 0 algebraically, for any F, and for the point-split bilinear F(x)F(x')
 B  Milton eq.(58) trace: zero at LEADING order only (with r -> a); O(eps^-2) remainder when r = a+eps
 C  Deutsch-Candelas leading term, covariant form 2 alpha1 kbar_ij / x^3 (Miao-Chu 1706.09652 eq.1.3a):
    sphere reproduces eq.(58)'s tensor structure; A = 2|alpha1|/3 -> EM 1/(60 pi^2), Dirichlet 1/(720 pi^2);
    alpha1 = b4/2 with Fursaev's b4 (Miao-Chu Table 2)
 D  conservation: p_r from eq.(58) exterior, and interior by kbar -> -kbar; compare with tolman.py's u, p_r, m
 E  Brown-Maclay (49) and Dowker-Kennedy/Deutsch-Candelas wedge (50),(52): traceless; wedge -> EM plates
 F  ESTIMATE of the curved-space trace anomaly against |u| near the wall (named hypothesis 'flat space')
"""
import re, math, sys
import sympy as sp

ok = True
def chk(name, cond):
    global ok
    print(("PASS " if cond else "FAIL ") + name)
    ok = ok and bool(cond)

eta = sp.diag(-1, 1, 1, 1)
# ---------------- A
Fs = sp.symbols('f01 f02 f03 f12 f13 f23'); Gs = sp.symbols('g01 g02 g03 g12 g13 g23')
def antisym(v):
    M = sp.zeros(4); idx = [(0,1),(0,2),(0,3),(1,2),(1,3),(2,3)]
    for (i,j),s in zip(idx, v): M[i,j] = s; M[j,i] = -s
    return M
F = antisym(Fs); Fp = antisym(Gs); inv = eta.inv()
def Tmaxwell(F, Fp):
    Fup = inv*F*inv; Fpup = inv*Fp*inv
    FF = sum(F[a,b]*Fpup[a,b] for a in range(4) for b in range(4))
    T = sp.zeros(4)
    for m in range(4):
        for n in range(4):
            T[m,n] = sp.Rational(1,2)*sum((F[m,l]*(Fp*inv)[n,l] + Fp[m,l]*(F*inv)[n,l]) for l in range(4)) \
                     - sp.Rational(1,4)*eta[m,n]*FF
    return T
T = Tmaxwell(F, F); tr = sp.expand(sum(inv[m,n]*T[m,n] for m in range(4) for n in range(4)))
chk("A1 Maxwell trace g^{mn}T_mn = 0 identically for arbitrary F", tr == 0)
T2 = Tmaxwell(F, Fp); tr2 = sp.expand(sum(inv[m,n]*T2[m,n] for m in range(4) for n in range(4)))
chk("A2 symmetric point-split bilinear T[F(x),F(x')] traceless identically (so Minkowski-subtracted <T> is traceless in flat space)", tr2 == 0)

# ---------------- B
A, a, eps, r, th = sp.symbols('A a epsilon r theta', positive=True)
T58 = sp.diag(2/a, 0, a, a*sp.sin(th)**2)*A/eps**3        # Milton eq.(58), covariant, (t,r,th,ph)
g_at = lambda R: sp.diag(-1, 1, R**2, R**2*sp.sin(th)**2)
trace_at = lambda R: sp.simplify(sum((g_at(R).inv())[i,i]*T58[i,i] for i in range(4)))
chk("B1 eq.(58) trace with metric at r=a is 0 ('properly traceless')", trace_at(a) == 0)
tr_exact = sp.series(trace_at(a+eps), eps, 0, 0).removeO()
print("     trace of eq.(58) with metric at r=a+eps, leading terms:", sp.simplify(tr_exact))
chk("B2 ... but at r=a+eps the truncated eq.(58) has trace -4A/(a^2 eps^2)+O(1/eps): tracelessness is a LEADING-ORDER statement",
    sp.simplify(sp.limit(trace_at(a+eps)*eps**2, eps, 0) + 4*A/a**2) == 0)

# ---------------- C
# sphere, boundary P = (t,theta,phi); mixed extrinsic curvature k^a_b = -s diag(0,1/r,1/r) (Miao-Chu: g_ab = h_ab - 2x k_ab)
s = sp.symbols('s')  # s=+1 exterior (x=r-a), s=-1 interior (x=a-r)
k = -s*sp.diag(0, 1/r, 1/r); ktr = k.trace(); kbar = k - ktr/3*sp.eye(3)
chk("C1 kbar traceless", sp.simplify(kbar.trace()) == 0)
Trkb2 = sp.simplify((kbar*kbar).trace().subs(s**2, 1))
chk("C2 Tr kbar^2 = 2/(3 r^2) for a sphere (either side)", sp.simplify(Trkb2 - sp.Rational(2,3)/r**2) == 0)
al1 = sp.symbols('alpha1')
x = sp.symbols('x', positive=True)
# mixed components T^a_b:  leading 2 alpha1 kbar/x^3 (tangential) + alpha1 (n n - h/3) Tr kbar^2 / x^2
Ttt = 2*al1*kbar[0,0]/x**3 - al1/3*Trkb2/x**2
Tthth = 2*al1*kbar[1,1]/x**3 - al1/3*Trkb2/x**2
Trr = al1*Trkb2/x**2
u_c = sp.simplify(-Ttt.subs(s,1)); u_c_lead = sp.limit(u_c*x**3, x, 0)
# Milton (58) exterior: T_00 = 2A/(a eps^3), T^th_th = A a/(a^2 eps^3) = A/(a eps^3)
Asol = sp.solve(sp.Eq(u_c_lead.subs(r,a), 2*A/a), A)[0]
print("     A in terms of alpha1 from matching energy density:", Asol)
chk("C3 tangential/energy ratio of covariant form = eq.(58) ratio (T^th_th : T_00 = 1 : 2)",
    sp.simplify(sp.limit(Tthth.subs(s,1)*x**3,x,0)/u_c_lead) == sp.Rational(1,2))
tabl = {"Maxwell": (-sp.Rational(1,40)/sp.pi**2, -sp.Rational(1,20)/sp.pi**2, sp.Rational(1,60)/sp.pi**2),
        "Dirichlet scalar": (-sp.Rational(1,480)/sp.pi**2, -sp.Rational(1,240)/sp.pi**2, sp.Rational(1,720)/sp.pi**2)}
for nm,(a1,b4,Amil) in tabl.items():
    chk(f"C4 {nm}: A = -2 alpha1/3 = {sp.simplify(Asol.subs(al1,a1))} equals Milton's A = {Amil}", sp.simplify(Asol.subs(al1,a1)-Amil)==0)
    chk(f"C5 {nm}: alpha1 = b4/2 (Miao-Chu 2.13, b4 from Fursaev via Table 2)", sp.simplify(a1 - b4/2) == 0)
chk("C6 EM/Dirichlet ratio of A is 12", sp.simplify(tabl['Maxwell'][2]/tabl['Dirichlet scalar'][2]) == 12)
# covariant form: trace exactly zero at every r (mixed components, both terms)
trc = sp.simplify(Ttt + 2*Tthth + Trr)
chk("C7 covariant DC/Miao-Chu form traceless EXACTLY at every r (not only leading order)", trc == 0)

# ---------------- D  conservation, flat static spherical: d_r T^r_r + (2/r)T^r_r - (T^th_th+T^ph_ph)/r = 0
for sv, xr, nm in [(1, r-a, "exterior"), (-1, a-r, "interior")]:
    Trr_r = Trr.subs({s:sv, x:xr}); Tth_r = Tthth.subs({s:sv, x:xr})
    div = sp.diff(Trr_r, r) + 2/r*Trr_r - 2*Tth_r/r
    e = sp.symbols('e', positive=True)
    dive = sp.simplify(div.subs(r, a+sv*e))
    lead = sp.limit(dive*e**3, e, 0)
    chk(f"D1 {nm}: conservation residual cancels at the leading order eps^-3", sp.simplify(lead) == 0)
# eq.(58) route (tree's route): exterior p_t = A/(a eps^3) -> p_r ; interior p_t -> -p_t
p = sp.Function('p')
e = sp.symbols('e', positive=True)
# exterior: r = a + e, dp_r/dr = 2(p_t - p_r)/r ~ 2 p_t / a at leading order
pr_ext = sp.integrate(2*(A/(a*e**3))/a, e)       # dr = de
pr_int = sp.integrate(-2*(-A/(a*e**3))/a, e)      # interior: p_t = -A/(a e^3), dr = -de
chk("D2 exterior p_r from eq.(58) + conservation = -A/(a^2 eps^2)", sp.simplify(pr_ext + A/(a**2*e**2)) == 0)
chk("D3 interior p_r (kbar -> -kbar) = -A/(a^2 eps^2) -- tolman.py:607-613's value", sp.simplify(pr_int + A/(a**2*e**2)) == 0)
hb, c = sp.symbols('hbar c', positive=True)
AEM = sp.Rational(1,60)/sp.pi**2
u_int = -2*AEM*hb*c/(a*e**3)
chk("D4 interior u = -2 A hbar c/(a eps^3) = -hbar c/(30 pi^2 a eps^3) (tolman.py:609)", sp.simplify(u_int + hb*c/(30*sp.pi**2*a*e**3)) == 0)
chk("D5 interior p_r = -hbar c/(60 pi^2 a^2 eps^2) (tolman.py:610)", sp.simplify(pr_int.subs(A,AEM)*hb*c + hb*c/(60*sp.pi**2*a**2*e**2)) == 0)
# m: dm/dr = 4 pi r^2 u/c^2, r = a - e -> dm/de = -4 pi a^2 u/c^2 ; near-wall part
m_int = sp.integrate(-4*sp.pi*a**2*u_int/c**2, e)
chk("D6 near-wall m(r) = -(hbar a)/(15 pi c eps^2) (tolman.py:607)", sp.simplify(m_int + hb*a/(15*sp.pi*c*e**2)) == 0)
chk("D7 leading trace of the interior profile: -u + 2 p_t = 0 at eps^-3", sp.simplify(-u_int/(hb*c) + 2*(-AEM/(a*e**3))) == 0)

# ---------------- E
zh = sp.Matrix([0,0,0,1]); BM = -(sp.pi**2/1440)*(4*zh*zh.T - eta)
chk("E1 Brown-Maclay (49) conformal-scalar plates traceless", sp.simplify(sum(inv[i,i]*BM[i,i] for i in range(4))) == 0)
al, rr = sp.symbols('alpha rr', positive=True)
Tw = sp.diag(1,-1,3,-1)   # orthonormal (t,r,th,z)
chk("E2 wedge (50) traceless in orthonormal frame (-,+,+,+)", sum(eta[i,i]*Tw[i,i] for i in range(4)) == 0)
fEM = (sp.pi**2/al**2 + 11)*(sp.pi**2/al**2 - 1)
aa = sp.symbols('aa', positive=True)   # plate separation aa = alpha*rr
u_w = -fEM/(720*sp.pi**2*rr**4)       # T_tt component coefficient 1
lim = sp.limit((u_w).subs(rr, aa/al), al, 0)
chk("E3 wedge (52) as alpha->0 gives EM plate energy density -pi^2/(720 a^4)", sp.simplify(lim + sp.pi**2/(720*aa**4)) == 0)

# ---------------- F  ESTIMATE (order of magnitude): curved-space anomaly vs |u|
HBAR=1.054571817e-34; C=299792458.0; G=6.67430e-11
lP = math.sqrt(HBAR*G/C**3)
c_ch, a_ch = 1/10, 31/180       # Maxwell bulk central charges, Miao-Chu 1706.09652 Table 2 (read)
Ncurv = 24.0                    # generous bound on |C^2|,|E4| in units of Rscale^2 (assumption, stated)
print("     F  ESTIMATE, a = 1e-6 m cavity; ratio |anomaly|/|u| with anomaly ~ (c+a)/(16 pi^2) * N * Rscale^2 * hbar c,")
print("        Rscale = 8 pi G|u|/c^4; the scheme-dependent box R term is NOT included (coefficient not read here)")
acav = 1e-6
for epsv in [1e-15, 1e-12, 1e-9, 1e-7]:
    uabs = HBAR*C/(30*math.pi**2*acav*epsv**3)
    Rs = 8*math.pi*G*uabs/C**4
    anom = (c_ch+a_ch)/(16*math.pi**2)*Ncurv*Rs**2*HBAR*C
    print(f"        eps={epsv:.0e} m  |u|={uabs:.3e} J/m^3  ratio={anom/uabs:.3e}")
chk("F1 estimated curvature-squared anomaly/|u| < 1e-60 down to eps = 1 fm at a = 1 um (ESTIMATE)",
    (c_ch+a_ch)/(16*math.pi**2)*Ncurv*(8*math.pi*G*(HBAR*C/(30*math.pi**2*acav*1e-45))/C**4)**2*HBAR*C
    /(HBAR*C/(30*math.pi**2*acav*1e-45)) < 1e-60)

# ---------------- tree's constant
try:
    src = open('/home/user/Claude-Method-Works/research/warp-drive/tolman.py').read()
    mm = re.search(r'^A_EM\s*=\s*(.+?)\s*#', src, re.M)
    print("     tolman.py:", mm.group(0).strip())
    val = eval(mm.group(1), {'math': math})
    chk("G1 tolman.py A_EM equals 1/(60 pi^2) to machine precision", abs(val - 1/(60*math.pi**2)) < 1e-18)
except Exception as ex:
    print("     could not read tolman.py:", ex); ok = False

print("ALL PASS" if ok else "SOME FAIL")
sys.exit(0 if ok else 1)
