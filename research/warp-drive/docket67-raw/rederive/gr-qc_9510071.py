#!/usr/bin/env python3
"""DOCKET 67 re-derivation: Ford & Roman, gr-qc/9510071 Sec. 2, eqs. (1),(3)-(9).
Checks (exits 1 on any failed assertion):
 C1 Lorentzian sampling function is normalised (so a constant density samples to itself, eq. 4).
 C2 From the paper's eq.(3) (coefficient pi^2/45): static cap tau0 <= (3/2pi)(5/6)^(1/4) L = 0.4562 L (eq. 6).
 C3 g(v) of eq.(8) is minimised at v = 1/sqrt3 with g = (3/2pi)(5/8)^(1/4) = 0.4245 (eq. 9).
 C4 Boost structure: for T_mn = A(eta_mn - 4 z_m z_n), T u u = -A gamma^2 (1+3v^2)  (eq. 3's v-dependence).
 C5 INDEPENDENT: vacuum energy density of ONE real massless scalar, period L, computed two ways
    (exponential-cutoff mode sum minus continuum, and dim-reg + zeta) = -pi^2/(90 L^4), i.e. A = pi^2/90,
    half the paper's pi^2/45.  pi^2/45 is the value for TWO real degrees of freedom (e.g. EM).
 C6 Caps with field content matched to eq.(1) (one real scalar): static 0.5425 L, moving 0.5049 l1.
 C7 Sensitivity: Fewster-Eveson 1998 Lorentzian constant = (9/64) x F-R's -> caps x (9/64)^(1/4).
 C8 Illustration (NOT in the source): constant plate densities (conformal scalar -pi^2/1440L^4 vs scalar QI;
    EM -pi^2/720L^4 vs EM QI 3/16pi^2) give cap 1.085 L > L/2.
 C9 Fraction of the Eq.(1) bound reached by the periodic Casimir density at tau0 = f*L: (f/fmax)^4.
"""
import sys
import sympy as sp

ok = True
def check(name, cond, detail=""):
    global ok
    print(("PASS " if cond else "FAIL ") + name + ("  " + detail if detail else ""))
    ok = ok and bool(cond)

tau, t0, L, v = sp.symbols('tau tau0 L v', positive=True)
C = sp.Rational(3, 32) / sp.pi**2          # eq.(1) constant

# C1
norm = sp.integrate(t0/sp.pi/(tau**2 + t0**2), (tau, -sp.oo, sp.oo))
check("C1 Lorentzian normalised", sp.simplify(norm - 1) == 0, f"integral={norm}")

# C2 paper's coefficient
A_paper = sp.pi**2/45
cap_paper = sp.solve(sp.Eq(A_paper/L**4, C/t0**4), t0)[0]
closed = 3*L/(2*sp.pi)*sp.Rational(5, 6)**sp.Rational(1, 4)
check("C2 static cap from eq.(3) equals (3/2pi)(5/6)^(1/4) L",
      sp.simplify(cap_paper**4 - closed**4) == 0, f"= {sp.N(cap_paper/L, 8)} L")
check("C2 ~0.46 L as printed", abs(float(cap_paper/L) - 0.46) < 0.005)

# C3
x = sp.symbols('x', positive=True)   # x = v^2
h = (1 + 3*x)*(1 - x)
xs = sp.solve(sp.diff(h, x), x)
g = lambda hh: 3/(2*sp.pi)*sp.Rational(5, 6)**sp.Rational(1, 4)*hh**sp.Rational(-1, 4)
gmin = g(h.subs(x, xs[0]))
check("C3 g(v) min at v^2=1/3", xs == [sp.Rational(1, 3)])
check("C3 g_min = (3/2pi)(5/8)^(1/4)",
      sp.simplify(gmin**4 - (3/(2*sp.pi))**4*sp.Rational(5, 8)) == 0, f"= {sp.N(gmin, 8)}")
check("C3 ~0.42 as printed", abs(float(gmin) - 0.42) < 0.005)

# C4 boost structure
A = sp.symbols('A', positive=True)
eta = sp.diag(-1, 1, 1, 1)
z = sp.Matrix([0, 0, 0, 1])
T = A*(eta - 4*z*z.T)                      # lower indices; traceless, T_tt=-A... see below
gam = 1/sp.sqrt(1 - v**2)
u = sp.Matrix([gam, 0, 0, gam*v])
Tuu = sp.simplify((u.T*T*u)[0])
check("C4 T_mn = A(eta - 4zz) traceless", sp.simplify((eta.inv()*T).trace()) == 0)
check("C4 Tuu = -A gamma^2(1+3v^2)", sp.simplify(Tuu + A*gam**2*(1 + 3*v**2)) == 0, f"Tuu={Tuu}")

# C5a exponential cutoff: rho = (1/L) sum_n G(2 pi |n|/L) - (1/pi) int_0^oo G(q) dq,
#     G(q) = int d^2k/(2pi)^2 (1/2) w e^{-eps w} = (1/4pi) int_q^oo w^2 e^{-eps w} dw
eps, q, w = sp.symbols('epsilon q w', positive=True)
G = sp.integrate(w**2*sp.exp(-eps*w), (w, q, sp.oo))/(4*sp.pi)
a = 2*sp.pi/L
n = sp.symbols('n', integer=True, nonnegative=True)
X = sp.exp(-eps*a)
# sum_{n in Z} G(a|n|) = G(0) + 2 sum_{n>=1} G(a n); G(an) = e^{-eps a n}(a^2n^2/eps + 2an/eps^2 + 2/eps^3)/(4pi)
s0 = sum(X**0 for _ in [0])
xx = sp.symbols('xx', positive=True)
S0 = xx/(1 - xx); S1 = xx/(1 - xx)**2; S2 = xx*(1 + xx)/(1 - xx)**3
sum_pos = (a**2*S2/eps + 2*a*S1/eps**2 + 2*S0/eps**3)/(4*sp.pi)
total = G.subs(q, 0) + 2*sum_pos
cont = sp.integrate(G, (q, 0, sp.oo))/sp.pi * L   # continuum times L (per unit transverse area, length L)
rho_reg = (total.subs(xx, X) - cont)/L
rho = sp.limit(sp.simplify(rho_reg), eps, 0)
check("C5a periodic real scalar rho (cutoff) = -pi^2/(90 L^4)", sp.simplify(rho + sp.pi**2/(90*L**4)) == 0,
      f"rho={sp.simplify(rho)}")
# C5b dim-reg + zeta: int d^2k/(2pi)^2 sqrt(k^2+m^2) -> Gamma(-3/2)/((4pi) Gamma(-1/2)) m^3
dimreg = sp.gamma(sp.Rational(-3, 2))/(4*sp.pi*sp.gamma(sp.Rational(-1, 2)))
rho_z = (1/L)*sp.Rational(1, 2)*dimreg*2*a**3*sp.zeta(-3)
check("C5b periodic real scalar rho (zeta) = -pi^2/(90 L^4)", sp.simplify(rho_z + sp.pi**2/(90*L**4)) == 0,
      f"rho={sp.simplify(rho_z)}")
check("C5 paper's pi^2/45 is exactly 2x the one-real-scalar value", sp.simplify(A_paper/(sp.pi**2/90)) == 2)

# C6 matched caps
A_true = sp.pi**2/90
cap_true = sp.solve(sp.Eq(A_true/L**4, C/t0**4), t0)[0]
gmin_true = gmin*2**sp.Rational(1, 4)
check("C6 static cap (one real scalar) = (135/(16 pi^4))^(1/4) L",
      sp.simplify(cap_true**4 - sp.Rational(135, 16)/sp.pi**4*L**4) == 0, f"= {sp.N(cap_true/L, 6)} L")
print(f"     moving-observer cap (one real scalar): tau0 < {sp.N(gmin_true, 6)} l1  (paper: {sp.N(gmin, 6)} l1)")
# EM: periodic EM rho = -pi^2/(45L^4) against EM QI 3/(16 pi^2): same cap as the matched scalar
cap_em = sp.solve(sp.Eq(sp.pi**2/45/L**4, sp.Rational(3, 16)/sp.pi**2/t0**4), t0)[0]
check("C6 periodic EM (pi^2/45) vs EM QI (3/16pi^2) gives the same matched cap", sp.simplify(cap_em - cap_true) == 0)

# C7 Fewster-Eveson 9/64
fe = sp.Rational(9, 64)**sp.Rational(1, 4)
print(f"     C7 FE-1998 constant: caps x {sp.N(fe, 6)} -> paper coeff {sp.N(cap_paper/L*fe, 5)} L, matched {sp.N(cap_true/L*fe, 5)} L")

# C8 plates illustration
cap_pl = sp.solve(sp.Eq(sp.pi**2/1440/L**4, C/t0**4), t0)[0]
cap_pl_em = sp.solve(sp.Eq(sp.pi**2/720/L**4, sp.Rational(3, 16)/sp.pi**2/t0**4), t0)[0]
check("C8 plate caps (conformal scalar, EM) agree and exceed L/2",
      sp.simplify(cap_pl - cap_pl_em) == 0 and float(cap_pl/L) > 0.5, f"= {sp.N(cap_pl/L, 6)} L")

# C9 fraction of bound at tau0 = f L
for f in (sp.Rational(1, 10), sp.Rational(1, 4)):
    print(f"     C9 tau0={f}L: fraction of Eq.(1) bound = paper {sp.N((f/(cap_paper/L))**4*100, 4)} %,"
          f" matched {sp.N((f/(cap_true/L))**4*100, 4)} %;  at tau0 = cap: 100 % (equality by construction)")

print("ALL PASS" if ok else "SOME CHECK FAILED")
sys.exit(0 if ok else 1)
