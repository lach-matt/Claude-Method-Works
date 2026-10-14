#!/usr/bin/env python3
"""DOCKET 67 -- rederive for key 'jacobi-raychaudhuri-ricci-focusing'.

What the tree uses (spec.py:24-31, 168-175; composite.py:12-27, 412-416; specthm.py:1326-1327):
  q = (4 pi G/c^4) T_kk ; conjugate length pi/sqrt(q) ; 'a conjugate point needs T_kk > 0';
  'Ricci focusing R_kk = 8 pi T_kk needs positive energy; Weyl focusing is sign-blind'.

Checks (each prints PASS/FAIL; exit 1 on any FAIL):
 R1  Einstein eq (with trace term AND Lambda) contracted on a null k gives R_kk = kappa T_kk exactly.
 R2  null Raychaudhuri  theta' = -theta^2/2 - S + W - R_kk  with theta = 2G'/G  <=>  G''/G = -(S - W + R_kk)/2
     (S = sigma_ab sigma^ab, W = omega_ab omega^ab), 4 dims.  Gao-Wald eq.(13) is the W = 0 case.
 R3  Ricci-only reduction: G'' = -(R_kk/2) G = -q G with q = 4 pi G T_kk / c^4 (SI units check: 1/m^2).
 R4  constant q: point-source initial data (G=0,G'=1) -> first zero at pi/sqrt(q) (the tree's figure);
     parallel initial data (G=1,G'=0) -> pi/(2 sqrt q).  The tree's pi/sqrt(q) is point-to-point.
 R5  SUFFICIENCY (Sturm comparison): q(lam) >= q0 > 0 and S >= 0, W = 0 on [0, pi/sqrt(q0)] => a zero of G
     at lam <= pi/sqrt(q0).  Numeric over random profiles.
 R6  NECESSITY holds ONLY in the shear-free twist-free reduction: q <= 0 everywhere, S = 0 => G >= lam > 0.
     and it is 'T_kk > 0 SOMEWHERE', not everywhere and not integrated (profile with int q < 0 still focuses).
 R7  COUNTEREXAMPLE to 'a conjugate point needs T_kk > 0' in the full (2x2) Jacobi equation:
     tidal matrix diag(-e + w, -e - w) with trace -2e <= 0 (T_kk <= 0) and w > e gives det J = 0 at
     pi/sqrt(w - e).  Also verifies eq.(13) along that solution (G = sqrt(det J), S from J'J^-1).
 R8  T_kk vs energy density: dust T_kk = rho c^2 (k normalised k^0 = 1 in the rest frame); perfect fluid
     T_kk = rho c^2 + p; pure magnetic field T_kk = 2u sin^2(alpha), u = B^2/2mu0.  spec.py:304 compares
     seatindex.tkk_required(l) (a T_kk) with energy_density(B) = u: a factor 2 at perpendicular incidence.
     Consequence for spec.py's withdrawn ratio 2 pi^2/3: becomes pi^2/3 = 3.29 > 1 -> conclusion unchanged.
 R9  numbers: q and pi/sqrt(q) for water, and G sensitivity (CODATA 2018 = 2022 = 6.67430(15)e-11).
"""
import math, random, sys
import sympy as sp

fails = []
def rep(tag, ok, msg):
    print("%s %-4s %s" % ("PASS" if ok else "FAIL", tag, msg))
    if not ok:
        fails.append(tag)

# ---------------- R1
kap, Lam = sp.symbols('kappa Lambda', real=True)
th, ph = sp.symbols('theta phi', real=True)
eta = sp.diag(-1, 1, 1, 1)
k = sp.Matrix([1, sp.sin(th)*sp.cos(ph), sp.sin(th)*sp.sin(ph), sp.cos(th)])
Tsym = sp.Matrix(4, 4, lambda i, j: sp.Symbol('T%d%d' % (min(i, j), max(i, j))))
Ttr = sum(eta[i, i]*Tsym[i, i] for i in range(4))  # T = g^ab T_ab (eta inverse = eta)
Ric = kap*(Tsym - sp.Rational(1, 2)*Ttr*eta) + Lam*eta
Rkk = sp.simplify((k.T*Ric*k)[0])
Tkk = sp.simplify((k.T*Tsym*k)[0])
null = sp.simplify((k.T*eta*k)[0])
rep("R1", null == 0 and sp.simplify(Rkk - kap*Tkk) == 0,
    "k null (k.k=%s); R_kk - kappa T_kk = %s (trace term and Lambda both drop)" % (null, sp.simplify(Rkk - kap*Tkk)))

# ---------------- R2
lam = sp.symbols('lambda', real=True)
G = sp.Function('G')(lam)
S, W, Rk = sp.symbols('S W R_kk', real=True)
theta = 2*sp.diff(G, lam)/G
ray = sp.diff(theta, lam) - (-theta**2/2 - S + W - Rk)
target = sp.diff(G, lam, 2)/G + (S - W + Rk)/2
rep("R2", sp.simplify(ray - 2*target) == 0,
    "Raychaudhuri(theta=2G'/G) == 2*[G''/G + (S - W + R_kk)/2]; W=0 is Gao-Wald eq.(13)")

# ---------------- R3
Gn, c = 6.67430e-11, 299792458.0
# units: G [m^3 kg^-1 s^-2] / c^4 [m^4 s^-4] * T_kk [J m^-3 = kg m^-1 s^-2] -> m^-2
m_, kg_, s_ = sp.symbols('m kg s', positive=True)
units = sp.simplify((m_**3/kg_/s_**2)/(m_/s_)**4*(kg_/m_/s_**2))
rep("R3", units == m_**-2 and sp.simplify(sp.Rational(1, 2)*8*sp.pi - 4*sp.pi) == 0,
    "R_kk/2 = (8 pi G/c^4) T_kk / 2 = (4 pi G/c^4) T_kk; units of q: %s" % units)

# ---------------- R4
qs = sp.symbols('q', positive=True)
g1 = sp.sin(sp.sqrt(qs)*lam)/sp.sqrt(qs)
g2 = sp.cos(sp.sqrt(qs)*lam)
ok = (sp.simplify(sp.diff(g1, lam, 2) + qs*g1) == 0 and g1.subs(lam, 0) == 0 and sp.diff(g1, lam).subs(lam, 0) == 1
      and sp.simplify(g1.subs(lam, sp.pi/sp.sqrt(qs))) == 0
      and sp.simplify(g2.subs(lam, sp.pi/(2*sp.sqrt(qs)))) == 0)
rep("R4", ok, "point data: first zero pi/sqrt(q) (tree's figure); parallel data: pi/(2 sqrt q)")

# ---------------- numeric integrator for scalar G'' = -(q + S/2) G   [G''/G = -(S + R_kk)/2, R_kk = 2q]
def first_zero(qf, Sf, L, G0=0.0, dG0=1.0, n=40000):
    h = L/n; y, v = G0, dG0; x = 0.0
    def a(x, y): return -(qf(x) + 0.5*Sf(x))*y
    for _ in range(n):
        k1y, k1v = v, a(x, y)
        k2y, k2v = v + 0.5*h*k1v, a(x + 0.5*h, y + 0.5*h*k1y)
        k3y, k3v = v + 0.5*h*k2v, a(x + 0.5*h, y + 0.5*h*k2y)
        k4y, k4v = v + h*k3v, a(x + h, y + h*k3y)
        yn = y + h*(k1y + 2*k2y + 2*k3y + k4y)/6; vn = v + h*(k1v + 2*k2v + 2*k3v + k4v)/6
        if x > 0 and y > 0 and yn <= 0:
            return x + h*y/(y - yn)
        x, y, v = x + h, yn, vn
    return None

random.seed(67)
# ---------------- R5
q0 = 1.0; L0 = math.pi/math.sqrt(q0); worst = 0.0; allok = True
for t in range(60):
    amps = [random.uniform(0, 3) for _ in range(3)]; fr = [random.uniform(0.5, 6) for _ in range(3)]
    qf = lambda x, a=amps, f=fr: q0 + sum(ai*math.sin(fi*x)**2 for ai, fi in zip(a, f))
    sa = random.uniform(0, 4)
    Sf = lambda x, s=sa: s*math.cos(3*x)**2
    z = first_zero(qf, Sf, L0*1.0001)
    allok &= (z is not None and z <= L0*(1 + 1e-6)); worst = max(worst, z or 99)
zt = first_zero(lambda x: q0, lambda x: 0.0, L0*1.01)
allok &= zt is not None and abs(zt - L0) < 1e-6
rep("R5", allok, "60 random profiles q>=q0=1, S>=0: every first zero <= pi/sqrt(q0)=%.6f (max seen %.6f); equality case q=q0,S=0 gives %.6f (bound is sharp)" % (L0, worst, zt))

# ---------------- R6
allok = True
for t in range(30):
    a = random.uniform(0, 2)
    qf = lambda x, a=a: -a*math.sin(2*x)**2
    z = first_zero(qf, lambda x: 0.0, 20.0)
    allok &= z is None
# 'somewhere' not 'integrated': q = +4 on [0,1.6], then -50 on (1.6, 20]
qf = lambda x: 4.0 if x <= 1.6 else -50.0
z = first_zero(qf, lambda x: 0.0, 20.0)
intq = 4.0*1.6 - 50.0*(20 - 1.6)
rep("R6", allok and z is not None and abs(z - math.pi/2) < 1e-3 and intq < 0,
    "q<=0, S=0: no zero on [0,20] in 30 profiles; q>0 only on [0,1.6] with int q = %.0f < 0 still focuses at %.5f = pi/2"
    % (intq, z if z else float('nan')))

# ---------------- R7  full 2x2 Jacobi (parallel-propagated screen), point data J(0)=0, J'(0)=I
e, w = sp.Rational(1, 10), sp.Integer(1)          # R_kk = trace = -2e < 0  (T_kk < 0, NEC violated)
a1, a2 = sp.sqrt(w - e), sp.sqrt(w + e)
J1 = sp.sin(a1*lam)/a1                             # J'' = -(w - e) J   (focusing direction)
J2 = sp.sinh(a2*lam)/a2                            # J'' = +(w + e) J   (defocusing direction)
tidal = sp.diag(w - e, -(w + e))                   # J'' = -tidal J ; tr(tidal) = R_kk = -2e
detJ = J1*J2
zero = sp.pi/a1
ok7a = sp.simplify(sp.diff(J1, lam, 2) + (w - e)*J1) == 0 and sp.simplify(sp.diff(J2, lam, 2) - (w + e)*J2) == 0
ok7b = sp.simplify(detJ.subs(lam, zero)) == 0 and tidal.trace() < 0
# eq.(13) along this solution: G = sqrt(det J); B = J' J^-1 ; sigma = tracefree part of B ; S = tr(sigma^2)
Gs = sp.sqrt(detJ)
B = sp.diag(sp.diff(J1, lam)/J1, sp.diff(J2, lam)/J2)
th_ = B.trace(); sig = B - th_/2*sp.eye(2); Sval = (sig*sig).trace()
resid = sp.diff(Gs, lam, 2)/Gs + (Sval + tidal.trace())/2
vals = [abs(float(resid.subs(lam, x))) for x in (0.3, 0.9, 1.7, 2.5, 3.0)]
rep("R7", ok7a and ok7b and max(vals) < 1e-10,
    "R_kk = %s < 0 (T_kk < 0) yet det J = 0 at pi/sqrt(w-e) = %.6f; eq.(13) residual max %.1e along it"
    % (tidal.trace(), float(zero), max(vals)))

# ---------------- R7b  exact spacetime realising R7: plane wave ds^2 = 2 du dv + H du^2 + dx^2 + dy^2
U, V, X, Y = sp.symbols('u v x y', real=True)
co = [U, V, X, Y]
H = -(w - e)*X**2 + (w + e)*Y**2
g = sp.Matrix([[H, 1, 0, 0], [1, 0, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])
gi = g.inv()
Gam = [[[sp.simplify(sum(gi[a, d]*(sp.diff(g[d, b], co[c]) + sp.diff(g[d, c], co[b]) - sp.diff(g[b, c], co[d]))
         for d in range(4))/2) for c in range(4)] for b in range(4)] for a in range(4)]
def Riem(a, b, c, d):  # R^a_{bcd}
    r = sp.diff(Gam[a][b][d], co[c]) - sp.diff(Gam[a][b][c], co[d])
    r += sum(Gam[a][c][m]*Gam[m][b][d] - Gam[a][d][m]*Gam[m][b][c] for m in range(4))
    return sp.simplify(r)
Ruu = sp.simplify(sum(Riem(a, 0, a, 0) for a in range(4)))
tid = sp.Matrix([[Riem(2, 0, 2, 0), Riem(2, 0, 3, 0)], [Riem(3, 0, 2, 0), Riem(3, 0, 3, 0)]])  # R^i_{u j u}
rep("R7b", Ruu == tidal.trace() and sp.simplify(tid - tidal) == sp.zeros(2),
    "plane wave H=-(w-e)x^2+(w+e)y^2: R_uu = %s (= -2e < 0), tidal R^i_uju = %s -- R7 is an exact GR spacetime "
    "(T_uu = R_uu/8pi < 0 null dust + a gravitational-wave Weyl part); geodesic x=y=0 with affine u"
    % (Ruu, list(tid)))

# ---------------- R8  T_kk for three sources, k = (1, n) in the source rest frame (units c = 1)
rho, p, u, al = sp.symbols('rho p u alpha', real=True)
n = sp.Matrix([sp.sin(al), 0, sp.cos(al)])
kk = sp.Matrix([1, n[0], n[1], n[2]])
Tdust = sp.diag(rho, 0, 0, 0)
Tpf = sp.diag(rho, p, p, p)
# pure B along z: T_00 = u, T_0i = 0, T_ij = u delta_ij - B_i B_j/mu0 = u delta_ij - 2u zhat_i zhat_j
Tij = u*sp.eye(3) - 2*u*sp.Matrix([[0, 0, 0], [0, 0, 0], [0, 0, 1]])
TB = sp.zeros(4); TB[0, 0] = u
for i in range(3):
    for j in range(3):
        TB[i+1, j+1] = Tij[i, j]
f = lambda T: sp.simplify((kk.T*T*kk)[0])
tb = sp.simplify(f(TB) - 2*u*sp.sin(al)**2)
ratio_old = 2*sp.pi**2/3
ratio_new = sp.simplify((sp.pi/8)/(sp.Rational(3, 8)/sp.pi))
rep("R8", f(Tdust) == rho and sp.simplify(f(Tpf) - rho - p) == 0 and tb == 0 and ratio_new == sp.pi**2/3,
    "dust T_kk=rho; fluid T_kk=rho+p; magnetic T_kk=2u sin^2(alpha) (=2u perpendicular, 0 along B). "
    "spec.py:304 sets T_kk=u: withdrawn ratio 2pi^2/3=%.4f -> pi^2/3=%.4f at perpendicular incidence, still >1"
    % (float(ratio_old), float(ratio_new)))

# ---------------- R9
rho_w = 1000.0
qw = 4*math.pi*Gn/c**4*(rho_w*c**2)
Lw = math.pi/math.sqrt(qw)
AU = 1.495978707e11
dG = 0.00015e-11/6.67430e-11
rep("R9", 9.3e-24 < qw < 9.4e-24 and 1.0e12 < Lw < 1.04e12,
    "water rho=1000: q=%.4e m^-2, pi/sqrt(q)=%.4e m = %.2f AU (point-to-point, constant q, shear-free); "
    "G rel. unc. %.1e -> length rel. %.1e; sign condition G-independent" % (qw, Lw, Lw/AU, dG, dG/2))

print("\n%d/%d checks passed" % (10 - len(fails), 10))
sys.exit(1 if fails else 0)
