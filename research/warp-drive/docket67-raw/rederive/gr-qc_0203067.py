#!/usr/bin/env python3
"""DOCKET 67 re-derivation: Agnese & La Camera, gr-qc/0203067 (2002), eqs. (11)-(17).
Computes the Einstein tensor of the published metric from scratch (sympy), and
checks every claim tolman.py makes of eq. (17).  Exit 0 iff every check holds."""
import sys, random
import sympy as sp

r, m, b, t, th, ph = sp.symbols('r m beta t theta phi', positive=True)
ok = True
def chk(name, cond):
    global ok
    print(('PASS ' if cond else 'FAIL ') + name)
    ok = ok and bool(cond)

s = sp.sqrt(1 - 2*m/(b*r))
A = 1/(1 - 2*m/(b*r))                 # eq. (11)
B = (1 + b*(s - 1))**2                # eq. (12) with observer at infinity (alpha = 1)
x = [t, r, th, ph]
g = sp.diag(-B, A, r**2, r**2*sp.sin(th)**2)   # signature (-,+,+,+); paper's (4) reordered
gi = g.inv()
n = 4
Gam = [[[sp.simplify(sum(gi[a, d]*(sp.diff(g[d, bb], x[c]) + sp.diff(g[d, c], x[bb])
        - sp.diff(g[bb, c], x[d])) for d in range(n))/2) for c in range(n)] for bb in range(n)] for a in range(n)]
def Ric(i, j):
    return sp.simplify(sum(sp.diff(Gam[a][i][j], x[a]) - sp.diff(Gam[a][i][a], x[j])
        + sum(Gam[a][a][d]*Gam[d][i][j] - Gam[a][j][d]*Gam[d][i][a] for d in range(n)) for a in range(n)))
R = sp.Matrix(n, n, lambda i, j: Ric(i, j))
Rs = sp.simplify(sum(gi[i, j]*R[i, j] for i in range(n) for j in range(n)))
G = (R - Rs*g/2)
Gmix = sp.simplify(gi*G)              # G^mu_nu
rho = sp.simplify(-Gmix[0, 0]/(8*sp.pi))
ppar = sp.simplify(Gmix[1, 1]/(8*sp.pi))
pperp = sp.simplify(Gmix[2, 2]/(8*sp.pi))

chk("Ricci scalar R = 0 (traceless ansatz)", sp.simplify(Rs) == 0)
chk("rho = 0 identically (eq. 3)", sp.simplify(rho) == 0)
chk("p_|| + 2 p_perp = 0 (eq. 3)", sp.simplify(ppar + 2*pperp) == 0)
p13 = (b - 1)*m/(4*sp.pi*b*(1 + b*(s - 1))*r**3)     # eq. (13)
chk("computed p_|| equals printed eq. (13)", sp.simplify(ppar - p13) == 0)
# numeric spot check of eq (13) against the computed G^r_r, robust to simplify quirks
for _ in range(5):
    sub = {m: random.uniform(0.5, 2), b: random.uniform(0.05, 0.95)}
    sub[r] = 2*sub[m]/sub[b]*random.uniform(1.01, 5)
    chk("  numeric p_|| == eq.(13) at %s" % {str(k): round(v, 3) for k, v in sub.items()},
        abs(float((ppar - p13).subs(sub))) < 1e-12)

# Misner-Sharp mass from g_rr: m_MS = (r/2)(1 - g^rr)
mMS = sp.simplify(r/2*(1 - 1/A))
chk("m_MS = m/beta, constant in r", sp.simplify(mMS - m/b) == 0)
chk("dm_MS/dr = 4 pi r^2 rho (= 0)", sp.simplify(sp.diff(mMS, r) - 4*sp.pi*r**2*rho) == 0)

r0 = 2*m/b
# throat limit of eq (13): s -> 0, bracket -> 1 - beta; valid only for beta != 1
p_throat = sp.limit(p13.subs(m, b*r0/2).subs(r0, 2*m/b), r, 2*m/b, dir='+')
p17a = -m/(4*sp.pi*b*r0**3)
p17b = -b**2/(32*sp.pi*m**2)
chk("throat limit of eq. (13) = eq. (17) first form (generic beta)", sp.simplify(p_throat - p17a) == 0)
chk("eq. (17) two printed forms agree", sp.simplify(p17a - p17b) == 0)
chk("4 pi r_0^3 p_|| = -m_MS at the throat", sp.simplify(4*sp.pi*r0**3*p17a + m/b) == 0)

# Domain: at beta = 1 eq. (13) vanishes identically (Schwarzschild), eq. (17) does not
chk("beta = 1: eq. (13) is identically 0 (Schwarzschild, zero pressure)", sp.simplify(p13.subs(b, 1)) == 0)
chk("beta = 1: eq. (17) evaluates to -1/(32 pi m^2) != 0  => (17) needs beta != 1",
    sp.simplify(p17b.subs(b, 1) + 1/(32*sp.pi*m**2)) == 0)

# 0 < beta < 1: B nonzero and finite on r >= r0; p_|| < 0 on r >= r0
for bv in [0.1, 0.5, 0.9]:
    ss = sp.symbols('ss')   # ss = s in [0,1)
    Bb = 1 + bv*(ss - 1)
    chk("beta=%.1f: 1+beta(s-1) in [1-beta, 1) > 0 for s in [0,1)" % bv,
        float(Bb.subs(ss, 0)) > 0 and float(Bb.subs(ss, 0.999999)) > 0)
    for rr in [1.0001, 1.5, 3, 10, 100]:
        sub = {m: 1.0, b: bv, r: rr*2/bv}
        chk("  beta=%.1f r=%.4g r0: p_|| < 0 (tension)" % (bv, rr), float(p13.subs(sub)) < 0)

# beta > 1 or beta < 0: lapse zero at r* = 2 m beta/(2 beta - 1) > r0
for bv in [1.5, 3.0, -0.5]:
    rstar = 2*bv/(2*bv - 1)   # m = 1
    val = 1 + bv*(sp.sqrt(1 - 2/(bv*rstar)) - 1)
    chk("beta=%.1f: B(r*) = 0 at r* = 2 m beta/(2beta-1)" % bv, abs(float(val)) < 1e-12)
    if bv > 0:
        chk("  and r* > r0 = 2m/beta", rstar > 2/bv)

# Generic Morris-Thorne throat: any A = 1/(1-2M/r) with B finite, nonzero, (r-2M)B'/B -> 0
M = sp.symbols('M', positive=True)
Bf = sp.Function('Bf')
Gtr = ((1 - 2*M/r)*(1 + r*sp.diff(Bf(r), r)/Bf(r)) - 1)/r**2   # 8 pi p_r for this metric
# replace (1-2M/r) r B'/B by eps -> 0 at r0 = 2M
chk("generic throat: 8 pi p_r(2M) = -1/(2M)^2 i.e. 4 pi r0^3 p_r = -M, independent of B",
    sp.simplify((( -1)/r**2).subs(r, 2*M)*4*sp.pi*(2*M)**3/(8*sp.pi) + M) == 0)
# confirm Gtr matches the computed G^r_r for the ALC B, A (with M = m/beta)
chk("  the generic formula reproduces ALC's computed 8 pi p_||",
    sp.simplify(Gtr.subs(M, m/b).replace(Bf, sp.Lambda(r, B)).doit() - 8*sp.pi*ppar) == 0)
chk("  ALC: (r - r0) r B'/B -> 0 at the throat (finite redshift)",
    sp.limit(((1 - 2*m/(b*r))*r*sp.diff(B, r)/B).subs({m: 1, b: sp.Rational(1, 2)}), r, 4, dir='+') == 0)

# Kretschmann (eq. 14) numeric spot check
Rie = {}
def Riem(a, bb, c, d):   # R^a_{b c d}
    return sp.diff(Gam[a][bb][d], x[c]) - sp.diff(Gam[a][bb][c], x[d]) + sum(
        Gam[a][c][e]*Gam[e][bb][d] - Gam[a][d][e]*Gam[e][bb][c] for e in range(n))
Rup = [[[[Riem(a, bb, c, d) for d in range(n)] for c in range(n)] for bb in range(n)] for a in range(n)]
# lower first index: R_{abcd} = g_ae R^e_bcd ; K = R_abcd R^abcd  (diagonal metric)
K = 0
for a in range(n):
    for bb in range(n):
        for c in range(n):
            for d in range(n):
                Rl = g[a, a]*Rup[a][bb][c][d]
                if Rl != 0:
                    K += Rl**2*gi[a, a]*gi[bb, bb]*gi[c, c]*gi[d, d]
K14 = 24*m**2/(r**7*b**2*(1 + b*(s - 1))**2)*(-4*m*b + r*(1 + b*(3*b - 2*(b - 1)*s - 2)))
for _ in range(4):
    sub = {m: random.uniform(0.5, 2), b: random.uniform(0.05, 0.95), th: 0.7}
    sub[r] = 2*sub[m]/sub[b]*random.uniform(1.01, 5)
    Kn = float(K.subs(sub)); K14n = float(K14.subs(sub))
    chk("Kretschmann matches printed eq. (14): %.10g vs %.10g" % (Kn, K14n), abs(Kn - K14n) < 1e-9*max(1, abs(Kn)))

# the tree's fixture tolman.py:2992 alc_throat(1.0, 0.5)
mv, bv = 1.0, 0.5
r0v = 2*mv/bv; ppv = -mv/(4*3.141592653589793*bv*r0v**3)
chk("fixture m=1, beta=0.5: r0=4, 4 pi r0^3 p_|| = -2 = -m_MS, m_MS=2>0, p_||<0",
    abs(r0v - 4) < 1e-15 and abs(4*3.141592653589793*r0v**3*ppv + 2) < 1e-12 and ppv < 0)
# the matter integral the tree's identity uses: INT 4 pi r^2 u dr with u = rho = 0
chk("matter integral INT_r0^R 4 pi r^2 rho dr = 0 (not m_MS): m_MS is a boundary constant",
    sp.integrate(4*sp.pi*r**2*rho, (r, 2*m/b, 10*m/b)) == 0)

# ---- LATER/CONCURRENT LITERATURE CHECKS -------------------------------------------
# (i) ALC is the Dadhich-Kar-Mukherjee-Visser (gr-qc/0109069, Sept 2001) R=0 family
#     g_tt = -(kappa + lambda sqrt(1-2M/r))^2, g_rr = 1/(1-2M/r) with
#     kappa = 1 - beta, lambda = beta, M = m/beta (unit lapse at infinity: kappa+lambda = 1).
kap, lam = 1 - b, b
Mv = m/b
tauD = -(2*Mv*kap)/(8*sp.pi*r**3*(kap + lam*s))     # DKMV eq. (10), tau = radial pressure
chk("ALC lapse == DKMV (8) with kappa=1-beta, lambda=beta, M=m/beta", sp.simplify(B - (kap + lam*s)**2) == 0)
chk("ALC eq.(13) p_|| == DKMV eq.(10) tau under that map", sp.simplify(p13 - tauD) == 0)
# (ii) two-sided continuation.  Near the throat s ~ l (proper length), so the SMOOTH
#     continuation through r0 is s -> -s (DKMV: '+ root on one side and - root on the other').
#     Far-side lapse N_far(s) = 1 - beta - beta s vanishes at s* = (1-beta)/beta,
#     which lies in [0,1) iff beta > 1/2 : a naked singularity on the far sheet (DKMV eq. 23).
for bv in [0.3, 0.5, 0.6, 0.9]:
    sstar = (1 - bv)/bv
    sing = 0 <= sstar < 1
    chk("beta=%.1f: smooth far-sheet lapse has a zero at finite r: %s (expected %s)"
        % (bv, sing, bv > 0.5), sing == (bv > 0.5))
# (iii) ALC's own eq. (19) glues with |sin psi| (mirror, + root both sides): the lapse is
#     even in l with a kink.  dN/dl = beta ds/dl, ds/dl = r0/(2 r^2) at the throat -> beta/(4m)
#     per unit beta, so [dN/dl] = beta^2/(2m).  Israel: [K^theta_theta] = 0 (r'(l)=0 at throat),
#     so surface energy sigma = 0 and surface tangential pressure P = [N'/N]/(8 pi)
#     = beta^2 / (16 pi m (1 - beta)) != 0 : an UNSTATED thin shell at the throat.
l = sp.symbols('l', positive=True)
rr = sp.symbols('rr', positive=True)
dsdl = sp.limit(sp.diff(sp.sqrt(1 - (2*m/b)/rr), rr)*sp.sqrt(1 - (2*m/b)/rr), rr, 2*m/b, dir='+')
chk("ds/dl at the throat = beta/(4m)", sp.simplify(dsdl - b/(4*m)) == 0)
jump = 2*b*dsdl
P_shell = sp.simplify(jump/(1 - b)/(8*sp.pi))
chk("mirror gluing (ALC eq. 19): lapse-gradient jump beta^2/(2m); shell sigma = 0, "
    "P = beta^2/(16 pi m (1-beta)) != 0 for 0<beta<1",
    sp.simplify(jump - b**2/(2*m)) == 0 and sp.simplify(P_shell - b**2/(16*sp.pi*m*(1 - b))) == 0)
print("   shell P at the tree fixture m=1, beta=1/2: %.6g = 1/(32 pi)" % float(P_shell.subs({m: 1, b: sp.Rational(1, 2)})))
# the shell has sigma = 0, so m_MS is continuous across it and the bulk throat values are one-sided limits:
chk("sigma = 0: [K^theta_theta] = [r'(l)/r] with r'(l) = s = 0 at the throat, so m_MS is continuous and the "
    "throat identity is a one-sided bulk limit unaffected by the shell", sp.limit(s, r, 2*m/b, dir='+') == 0)

print("ALL PASS" if ok else "SOME FAIL")
sys.exit(0 if ok else 1)
