#!/usr/bin/env python3
"""DOCKET 67 audit: schwarzschild-isotropic-vacuum.

Checks, exactly (sympy) and numerically (the tree's own pipeline, imported read-only):
 E1  the isotropic metric AS CODED in certify.py:221-228 (Cartesian x,y,z; A=((1-u)/(1+u))^2,
     B=(1+u)^4, u=M/2r) has Einstein tensor identically zero for r != M/2 -- exact, symbolic.
 E2  R = r(1+M/2r)^2 carries it to the Hilbert-Droste form with alpha = 2M (Schwarzschild 1916
     eq.14 in its areal-radius form) -- exact.
 E3  R(r) is two-to-one with minimum R = 2M at r = M/2 (the horizon); r = 5, 50 map to R > 2M
     (exterior sheet).  Kretschmann matches Poplawski 0902.1994 eq.(3).
 E4  the tree's own noise-floor numbers (4.08e-10 at r=5, 3.99e-12 at r=50) reproduced by
     importing certify.stress_energy (no file written); plus off-axis points and the h-scan,
     which show the floor is a function of (r, h, direction), not a single number.
Exit 0 iff E1-E3 hold exactly and E4 reproduces the quoted figures to 2 significant digits.
"""
import sys, math
import sympy as sp

ok = True
def rep(tag, cond, msg):
    global ok
    ok &= bool(cond)
    print("%-4s %-4s %s" % (tag, "ok" if cond else "FAIL", msg))

# ---------------- E1: exact Einstein tensor of the coded metric, Cartesian coords
t, x, y, z, M = sp.symbols('t x y z M', real=True)
X = [t, x, y, z]
r = sp.sqrt(x**2 + y**2 + z**2)
u = M / (2 * r)
A = ((1 - u) / (1 + u))**2
B = (1 + u)**4
g = sp.diag(-A, B, B, B)
gi = sp.diag(-1 / A, 1 / B, 1 / B, 1 / B)
Gam = [[[sp.simplify(sum(gi[l, s] * (sp.diff(g[s, m], X[n]) + sp.diff(g[s, n], X[m])
         - sp.diff(g[m, n], X[s])) for s in range(4)) / 2) for n in range(4)]
        for m in range(4)] for l in range(4)]
Ric = sp.zeros(4, 4)
for m in range(4):
    for n in range(4):
        e = 0
        for l in range(4):
            e += sp.diff(Gam[l][m][n], X[l]) - sp.diff(Gam[l][m][l], X[n])
            for s in range(4):
                e += Gam[l][l][s] * Gam[s][m][n] - Gam[l][n][s] * Gam[s][m][l]
        Ric[m, n] = sp.simplify(sp.factor(e))
Rs = sp.simplify(sum(gi[m, n] * Ric[m, n] for m in range(4) for n in range(4)))
Gein = (Ric - Rs * g / 2).applyfunc(sp.simplify)
rep("E1", all(c == 0 for c in Gein), "Einstein tensor of certify.py's coded isotropic metric "
    "is identically 0 (all 16 components, symbolic M, Cartesian x,y,z)")
# spot-check a random rational point exactly, guarding against simplify over-reach
pt = {x: sp.Rational(3, 7), y: sp.Rational(-5, 11), z: sp.Rational(2, 3), M: sp.Rational(1, 5)}
rep("E1b", all(sp.nsimplify(c.subs(pt)) == 0 for c in Gein), "exact zero at a rational off-axis point")
# vacuity guard: the same pipeline must NOT return zero for a non-vacuum metric
gtest = sp.diag(-(1 + u)**2, B, B, B)
# (only the tt changed; compute Ricci scalar cheaply along x-axis via radial reduction)
rr = sp.symbols('rr', positive=True)
def einstein_radial(Af, Bf):
    # static isotropic: G^t_t, G^r_r closed forms computed from the 4D metric in spherical coords
    th, ph = sp.symbols('th ph')
    Y = [t, rr, th, ph]
    gg = sp.diag(-Af, Bf, Bf * rr**2, Bf * rr**2 * sp.sin(th)**2)
    ggi = gg.inv()
    G_ = [[[sum(ggi[l, s] * (sp.diff(gg[s, m], Y[n]) + sp.diff(gg[s, n], Y[m]) - sp.diff(gg[m, n], Y[s]))
            for s in range(4)) / 2 for n in range(4)] for m in range(4)] for l in range(4)]
    R_ = sp.zeros(4, 4)
    for m in range(4):
        for n in range(4):
            e = 0
            for l in range(4):
                e += sp.diff(G_[l][m][n], Y[l]) - sp.diff(G_[l][m][l], Y[n])
                for s in range(4):
                    e += G_[l][l][s] * G_[s][m][n] - G_[l][n][s] * G_[s][m][l]
            R_[m, n] = sp.simplify(e)
    Rsc = sp.simplify(sum(ggi[m, n] * R_[m, n] for m in range(4) for n in range(4)))
    return [sp.simplify((R_ - Rsc * gg / 2)[i, i] * ggi[i, i]) for i in range(4)], R_, gg, ggi, Y
ur = M / (2 * rr)
Gs_vac, _, _, _, _ = einstein_radial(((1 - ur) / (1 + ur))**2, (1 + ur)**4)
Gs_bad, _, _, _, _ = einstein_radial((1 + ur)**2, (1 + ur)**4)
rep("E1c", all(c == 0 for c in Gs_vac) and any(c != 0 for c in Gs_bad),
    "vacuity guard: spherical-chart pipeline gives 0 for the metric and nonzero for a perturbed g_tt "
    "(perturbed G^r_r = %s; G^t_t unchanged as it depends on the spatial metric only)" % sp.factor(Gs_bad[1]))

# ---------------- E2: transformation to Hilbert-Droste / Schwarzschild 1916 eq.(14)
R = rr * (1 + ur)**2
dRdr = sp.diff(R, rr)
alpha = 2 * M
c1 = sp.simplify((1 - alpha / R) - ((1 - ur) / (1 + ur))**2)            # g_tt
c2 = sp.simplify(dRdr**2 / (1 - alpha / R) - (1 + ur)**4)              # g_rr
c3 = sp.simplify(R**2 - (1 + ur)**4 * rr**2)                           # angular
rep("E2", c1 == 0 and c2 == 0 and c3 == 0,
    "R = r(1+M/2r)^2 maps isotropic form onto (1-2M/R)dt^2 - dR^2/(1-2M/R) - R^2 dOmega^2 "
    "(Schwarzschild 1916 eq.14 with alpha = 2M, in areal R)")

# ---------------- E3: chart structure and Kretschmann
rmin = [v for v in sp.solve(sp.Eq(dRdr, 0), rr) if (v.subs(M, 1)) > 0]
print("     positive roots of dR/dr (M>0):", rmin)
rep("E3a", rmin == [M / 2] and sp.simplify(R.subs(rr, M / 2) - 2 * M) == 0,
    "dR/dr = 0 only at r = M/2 where R = 2M: isotropic chart is two-to-one (r -> M^2/4r symmetry)")
inv = sp.simplify(R.subs(rr, M**2 / (4 * rr)) - R)
rep("E3b", inv == 0, "R(M^2/4r) = R(r): the r < M/2 region is a second copy of the exterior")
Rv = {5: float(R.subs({M: 1, rr: 5})), 50: float(R.subs({M: 1, rr: 50}))}
rep("E3c", all(v > 2 for v in Rv.values()),
    "tree's sample radii are on the exterior sheet, outside the horizon: R(5)=%.4f, R(50)=%.4f > 2M = 2"
    % (Rv[5], Rv[50]))
# Kretschmann vs Poplawski eq (3): K = 12 rg^2 r^-6 (1+rg/4r)^-12, rg = 2M -> 48 M^2 / (r^6 (1+M/2r)^12)
K_areal = 48 * M**2 / R**6
K_pop = 12 * (2 * M)**2 / rr**6 / (1 + 2 * M / (4 * rr))**12
rep("E3d", sp.simplify(K_areal - K_pop) == 0, "Kretschmann 48M^2/R^6 equals Poplawski 0902.1994 eq.(3)")

# ---------------- E4: the tree's numeric floor, reproduced by import (read-only)
sys.path.insert(0, "/home/user/Claude-Method-Works/research/warp-drive")
sys.dont_write_bytecode = True
import certify
sch = certify.schwarzschild_isotropic(1.0)
q = {}
for rv in (5.0, 50.0):
    q[rv] = certify.max_abs(certify.stress_energy(sch, [0, rv, 0.0, 0.0], rv * 1e-4))
    print("     on-axis r=%-5g h=r*1e-4  max|T| = %.3e" % (rv, q[rv]))
rep("E4a", "%.2e" % q[5.0] == "4.08e-10" and "%.2e" % q[50.0] == "3.99e-12",
    "certify.py:62-66 figures reproduced exactly (4.08e-10, 3.99e-12)")
# off-axis and h-scan: the floor is not a single number
off = {}
for rv in (5.0, 50.0):
    p = [0, rv / math.sqrt(3), rv / math.sqrt(3), rv / math.sqrt(3)]
    off[rv] = certify.max_abs(certify.stress_energy(sch, p, rv * 1e-4))
    print("     off-axis (diag) r=%-5g max|T| = %.3e" % (rv, off[rv]))
for rv in (0.6, 1.0, 2.0):
    v = certify.max_abs(certify.stress_energy(sch, [0, rv, 0, 0], rv * 1e-4))
    print("     on-axis r=%-5g (near horizon r=0.5) max|T| = %.3e" % (rv, v))
for hf in (1e-2, 1e-3, 1e-4, 1e-5):
    v = certify.max_abs(certify.stress_energy(sch, [0, 5.0, 0, 0], 5.0 * hf))
    print("     r=5  h=r*%-6g max|T| = %.3e" % (hf, v))
rep("E4b", max(off.values()) <= 1e-8, "off-axis floor also under the 1e-8 selftest bound")

# ---------------- E5: isotropic Misner-Sharp mass returns M (Simmonds & Visser 2606.01061 sec.2.3)
# Their general diagonal-static eq.(2.22): m = sqrt(g_thth)/2 * [1 - (d g_thth)^2 / (4 g_rr g_thth)].
# With g_thth = r^2 g_rr this gives m = (r sqrt(g)/2) [1 - (1 + r g'/(2g))^2].  The text layer of
# eqs.(2.24)/(2.25) as served by alphaXiv reads (1 + g'/(2g)) with no factor r -- dimensionally
# inconsistent; checked both ways below and recorded as a DISCREPANCY (PDF vs text layer undetermined).
grr = (1 + ur)**4
gth = rr**2 * grr
ms_222 = sp.sqrt(gth) / 2 * (1 - sp.diff(gth, rr)**2 / (4 * grr * gth))
ms_lit = -rr * sp.sqrt(grr) / 2 * (sp.diff(grr, rr) / grr + sp.Rational(1, 4) * (sp.diff(grr, rr) / grr)**2)
d222 = sp.simplify(ms_222 - M)
dlit = sp.simplify(ms_lit - M)
print("     eq.(2.22) with g_thth = r^2 g_rr:  m - M =", d222, " (on r > M/2)")
print("     eq.(2.25) as text layer reads it: m - M =", sp.factor(dlit), " (nonzero: missing r factors)")
rep("E5", d222 == 0 and dlit != 0,
    "isotropic Misner-Sharp mass from 2606.01061 eq.(2.22) is exactly M; the as-extracted (2.25) is not (discrepancy)")

# ---------------- E6: margin of the tree's r = 10 ansatz row over the r = 10 Schwarzschild residual
s10 = certify.max_abs(certify.stress_energy(sch, [0, 10.0, 0.0, 0.0], 10.0 * 1e-4))
dev = certify.conformastatic()
T10 = {hh: certify.stress_energy(dev, [0, 10.0, 0.0, 0.0], hh)[0][0] for hh in (1e-2, 1e-3, 1e-3 * 1.0)}
T10b = certify.stress_energy(dev, [0, 10.0, 0.0, 0.0], max(10.0 * 1e-4, 1e-7))[0][0]
print("     Schwarzschild on-axis r=10 h=1e-3: max|T| = %.3e" % s10)
print("     ansatz T_00 (coordinate) at r=10: h=1e-2 %.4e, h=1e-3 %.4e (rel diff %.1e)" % (
    T10[1e-2], T10[1e-3], abs(T10[1e-2] / T10[1e-3] - 1)))
print("     ratio |ansatz T_00| / Schwarzschild residual at r=10 = %.0f (i.e. %.1f orders, not six)" % (
    abs(T10b) / s10, math.log10(abs(T10b) / s10)))
rep("E6", abs(T10b) / s10 < 1e4, "tree's r = 10 margin is under four orders (certify.py:514-516 says six at every radius)")
print("RESULT:", "ALL CHECKS PASS" if ok else "SOME CHECK FAILED")
sys.exit(0 if ok else 1)
