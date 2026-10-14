#!/usr/bin/env python3
"""DOCKET 67 re-audit: cosmic-string-deficit-angle-8pigmu against Vilenkin PRD 23, 852 (1981), READ.

Checks what Vilenkin's printed equations imply, and what axial.py uses.
  V1  Vilenkin eq.(14) with the string source T^nu_mu = delta^2 diag(mu,0,0,-p) (p = pressure along z)
      reproduces his eq.(20): h00 = h33 = 4G(mu+p) ln r, h11 = h22 = 4G(mu-p) ln r.
  V2  vacuum string p = -mu (his eq.11, T^0_0 = T^3_3) gives his eq.(21): h00 = 0, h11 = 8 G mu ln r.
  V3  his coordinate change (29)-(30) is consistent to first order in G mu, and (31)-(33) give
      phi' in [0, (1-4G mu) 2 pi): deficit 8 pi G mu, light deflection 4 pi G mu (his eq.34).
  V4  general transverse factor (1 - A ln r): exact cone deficit pi*A.  With A = 4G(mu-p):
      deficit = 4 pi G (mu - p).  Regular rod (p = 0): 4 pi G mu.  Vacuum string: 8 pi G mu.
  V5  sign table: an EXCESS with mu > 0 exists iff p > mu (axial pressure above energy density).
  V6  circumferential slope W'(0) = 1 - 4 G mu (so W'(0)-1 = -4 G mu, not -8 pi G mu).
  V7  Newtonian limit: g00 = 1 + 2U with U = 2G(mu+p) ln r; rod p = 0 gives U = 2 G mu ln r
      (Poisson for a line mass), vacuum string gives U = 0 (his "does not couple to nonrelativistic matter").
Exit 0 iff all pass.
"""
import sys
import sympy as sp

ok = []
def chk(name, cond):
    ok.append(bool(cond)); print(("PASS " if cond else "FAIL ") + name)

G, mu, p, r, r0, A, phi = sp.symbols('G mu p r r0 A phi', real=True)
pos = sp.symbols('rp', positive=True)

# V1: static eq.(14): Laplacian_2D h_{mu nu} = 16 pi G (T_{mu nu} - 1/2 eta T) with signature (+,-,-,-).
# Mixed T^nu_mu = diag(mu, 0, 0, -p) delta^2 ; lower with eta: T_00 = mu, T_11 = T_22 = 0, T_33 = +p.
eta = sp.diag(1, -1, -1, -1)
Tmix = sp.diag(mu, 0, 0, -p)
Tlow = eta * Tmix
trace = sum(Tmix[i, i] for i in range(4))
S = Tlow - sp.Rational(1, 2) * eta * trace
# 2D Laplacian of c*ln r = 2 pi c delta^2  ->  c = 16 pi G S / (2 pi) = 8 G S
coef = [sp.simplify(8 * G * S[i, i]) for i in range(4)]
chk("V1 h00 coefficient = 4G(mu+p)   [Vilenkin eq.20]", sp.simplify(coef[0] - 4*G*(mu+p)) == 0)
chk("V1 h11 = h22 coefficient = 4G(mu-p) [eq.20]", sp.simplify(coef[1] - 4*G*(mu-p)) == 0 and sp.simplify(coef[2]-coef[1]) == 0)
chk("V1 h33 coefficient = 4G(mu+p)   [eq.20]", sp.simplify(coef[3] - 4*G*(mu+p)) == 0)
# Laplacian identity: (1/r) d/dr (r d/dr ln r) = 0 off the axis; flux through circle = 2 pi
lnr = sp.log(pos)
chk("V1 ln r harmonic off axis, flux 2 pi", sp.simplify(sp.diff(pos*sp.diff(lnr, pos), pos)/pos) == 0
    and sp.simplify(2*sp.pi*pos*sp.diff(lnr, pos) - 2*sp.pi) == 0)

# V2
c_vac = [sp.simplify(c.subs(p, -mu)) for c in coef]
chk("V2 vacuum string p=-mu: h00 = h33 = 0, h11 = 8 G mu ln r [eq.21]",
    c_vac[0] == 0 and c_vac[3] == 0 and sp.simplify(c_vac[1] - 8*G*mu) == 0)

# V3: (1-lam) r^2 = (1-8G mu) r'^2 with lam = 8 G mu ln(r/r0); check (1-lam) dr^2 = dr'^2 to O(G mu)
eps = sp.symbols('eps')
lam = 8*eps*G*mu*sp.log(pos/r0)
rprime = pos*sp.sqrt((1-lam)/(1-8*eps*G*mu))
lhs = sp.series(sp.diff(rprime, pos)**2, eps, 0, 2).removeO()
rhs = sp.series(1 - lam, eps, 0, 2).removeO()
chk("V3 eqs.(29)-(30) consistent to first order in G mu", sp.simplify(sp.expand(lhs - rhs)) == 0)
defic = 2*sp.pi - (1 - 4*G*mu)*2*sp.pi
chk("V3 phi' range (1-4G mu)2pi -> deficit 8 pi G mu", sp.simplify(defic - 8*sp.pi*G*mu) == 0)
dphi = sp.pi*(1 + 4*G*mu)
chk("V3 eq.(34): deflection = dphi - pi = 4 pi G mu = deficit/2", sp.simplify((dphi - sp.pi) - defic/2) == 0)

# V4: 2-metric r^{-A}(dr^2 + r^2 dphi^2) (exact form of conformal factor e^{-A ln r}).
# rho = r^{1-A/2}/(1-A/2): d rho = r^{-A/2} dr, and circumference factor r^{1-A/2} = (1-A/2) rho.
a = sp.symbols('a', positive=True)
rho = pos**(1 - a/2)/(1 - a/2)
chk("V4 d rho/dr = r^{-A/2}", sp.simplify(sp.diff(rho, pos) - pos**(-a/2)) == 0)
circ_over_rho = sp.simplify(pos**(1 - a/2)/rho)       # = 1 - A/2
deficit_general = sp.simplify(2*sp.pi*(1 - circ_over_rho))
chk("V4 exact cone: deficit = pi*A", sp.simplify(deficit_general - sp.pi*a) == 0)
Ageneral = 4*G*(mu - p)
dgen = sp.pi*Ageneral
chk("V4 deficit(mu,p) = 4 pi G (mu - p)", sp.simplify(dgen - 4*sp.pi*G*(mu-p)) == 0)
chk("V4 regular rod p=0 ('regular massive rods'): deficit 4 pi G mu, NOT 8 pi G mu",
    sp.simplify(dgen.subs(p, 0) - 4*sp.pi*G*mu) == 0)
chk("V4 vacuum string p=-mu: deficit 8 pi G mu", sp.simplify(dgen.subs(p, -mu) - 8*sp.pi*G*mu) == 0)
tau = sp.symbols('tau')
chk("V4 with tension tau = -p: 4 pi G (mu + tau) [= Hindmarsh-Kibble eq.4.6 deficit]",
    sp.simplify(dgen.subs(p, -tau) - 4*sp.pi*G*(mu+tau)) == 0)

# V5: numeric sign table (G = 1)
cases = [(0.01, 0.0), (0.01, -0.01), (-0.01, 0.0), (-0.01, 0.01), (0.01, 0.02), (0.01, 0.01)]
rows = []
for m_, p_ in cases:
    d_ = float(dgen.subs({G: 1, mu: m_, p: p_}))
    rows.append((m_, p_, d_))
    print("     mu=%+.3f p=%+.3f  deficit=%+.6f  %s" % (m_, p_, d_, "EXCESS" if d_ < 0 else ("none" if d_ == 0 else "deficit")))
excess_pos_mu = [(m_, p_) for m_, p_, d_ in rows if d_ < 0 and m_ > 0]
chk("V5 excess with mu > 0 occurs, and only with p > mu", excess_pos_mu == [(0.01, 0.02)])
chk("V5 for p <= 0 (rod or tension), excess iff mu < 0",
    all((d_ < 0) == (m_ < 0) for m_, p_, d_ in rows if p_ <= 0))

# V6
Wp0 = 1 - 4*G*mu          # phi' = (1-4 G mu) phi, r' ~ r at the matching region
chk("V6 W'(0) - 1 = -4 G mu (canonical paraphrase '-8 pi G mu' is a normalisation slip)",
    sp.simplify((Wp0 - 1) + 4*G*mu) == 0 and sp.simplify(2*sp.pi*(1 - Wp0) - 8*sp.pi*G*mu) == 0)

# V7
U = sp.simplify(coef[0]/2)
chk("V7 Newtonian potential U = 2G(mu+p) ln r; rod: 2 G mu ln r; vacuum string: 0",
    sp.simplify(U - 2*G*(mu+p)) == 0 and sp.simplify(U.subs(p, 0) - 2*G*mu) == 0 and U.subs(p, -mu) == 0)

n = sum(ok); print("\n%d/%d PASS" % (n, len(ok)))
sys.exit(0 if n == len(ok) else 1)
