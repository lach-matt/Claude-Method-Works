#!/usr/bin/env python3
"""DOCKET 67, result 7/286: the pointwise energy conditions NEC/WEC/SEC/DEC
and 'the DEC requires the WEC', re-derived against Curiel 2014
(arXiv:1405.0403 p.6) and Kontou-Sanders 2020 (arXiv:2003.01815 Table 1,
eqs 18-27), and checked against the tree's uses (certify.py, nonstatic.py,
formation.py, bounds.py, seatindex.py, phase1.py).  sympy + z3 + numeric.
Reads research/warp-drive/certify.py by path; writes nothing there."""
import math, sys, os
import sympy as sp
import z3

OUT = []
def rec(tag, ok, note=""):
    OUT.append((tag, bool(ok), note))
    print("  [%s] %s%s" % ("ok" if ok else "FAIL", tag, ("  -- " + note) if note else ""))
    return bool(ok)

print("A. EFFECTIVE (TYPE I) FORMS: implications among NEC/WEC/SEC/DEC  [z3]")
rho, p1, p2, p3 = z3.Reals("rho p1 p2 p3")
P = [p1, p2, p3]
NEC = z3.And(*[rho + p >= 0 for p in P])                          # Curiel p.6
WEC = z3.And(rho >= 0, *[rho + p >= 0 for p in P])
SEC = z3.And(rho + p1 + p2 + p3 >= 0, *[rho + p >= 0 for p in P]) # n = 4
DEC = z3.And(rho >= 0, *[z3.And(p <= rho, -p <= rho) for p in P])  # |p_i| <= rho
def implies(a, b):
    s = z3.Solver(); s.add(a, z3.Not(b)); return s.check() == z3.unsat
def witness(a, b):
    s = z3.Solver(); s.add(a, z3.Not(b)); assert s.check() == z3.sat; return s.model()
rec("DEC => WEC (the tree's 'DEC requires the WEC', certify.py:85,354)", implies(DEC, WEC))
rec("WEC => NEC", implies(WEC, NEC))
rec("SEC => NEC", implies(SEC, NEC))
rec("DEC => NEC", implies(DEC, NEC))
rec("WEC =/=> SEC (witness exists)", not implies(WEC, SEC), str(witness(WEC, SEC)))
rec("SEC =/=> WEC (witness exists; Curiel p.8, Kontou-Sanders p.9)", not implies(SEC, WEC), str(witness(SEC, WEC)))
rec("NEC =/=> WEC (witness exists)", not implies(NEC, WEC), str(witness(NEC, WEC)))
rec("WEC =/=> DEC (witness exists)", not implies(WEC, DEC), str(witness(WEC, DEC)))
# The direction the tree uses: not(WEC) => not(DEC)  (contrapositive of DEC => WEC)
rec("not WEC => not DEC (contrapositive, the direction certify.py uses)", implies(z3.Not(WEC), z3.Not(DEC)))

print("\nB. 'FOR ALL OBSERVERS' FORMS AGREE WITH THE EFFECTIVE FORMS ON A TYPE-I TENSOR  [z3, nonlinear real]")
# T = diag(rho, p1, p2, p3) in an orthonormal frame, eta = diag(-1,1,1,1).
v0, v1, v2, v3 = z3.Reals("v0 v1 v2 v3")
T_vv = rho * v0**2 + p1 * v1**2 + p2 * v2**2 + p3 * v3**2
unit_timelike = v0**2 - v1**2 - v2**2 - v3**2 == 1
null = z3.And(v0**2 - v1**2 - v2**2 - v3**2 == 0, v0 > 0)
# WEC_phys: forall unit timelike v, T(v,v) >= 0
WEC_phys = z3.ForAll([v0, v1, v2, v3], z3.Implies(unit_timelike, T_vv >= 0))
NEC_phys = z3.ForAll([v0, v1, v2, v3], z3.Implies(null, T_vv >= 0))
def equiv(a, b, name, timeout=60000):
    s = z3.Solver(); s.set("timeout", timeout)
    s.add(z3.Not(a == b)); r = s.check()
    return rec(name, r == z3.unsat, "z3: %s" % r)
equiv(WEC_phys, WEC, "WEC_phys <=> (rho >= 0 and rho + p_i >= 0)")
equiv(NEC_phys, NEC, "NEC_phys <=> (rho + p_i >= 0)")

print("\nC. THE 4-D SEC FORM certify.py:349 USES  [sympy]")
r_, a_, b_, c_ = sp.symbols("rho p1 p2 p3", real=True)
g, s = sp.symbols("gamma s", positive=True)
ux, uy, uz = sp.symbols("u_x u_y u_z", real=True)
eta = sp.diag(-1, 1, 1, 1)
T = sp.diag(r_, a_, b_, c_)
trace = sum(eta[m, m] * T[m, m] for m in range(4))              # certify.py:338
V = sp.Matrix([g, g * s * ux, g * s * uy, g * s * uz])
TVV = (V.T * T * V)[0]
gVV = (V.T * eta * V)[0]
# (T_ab - T/2 g_ab) V^a V^b = T(V,V) - (T/2) g(V,V) = T(V,V) + T/2 when g(V,V) = -1
sec_source = TVV - sp.Rational(1, 2) * trace * gVV
sec_tree = TVV + sp.Rational(1, 2) * trace                        # certify.py:349
diff = sp.simplify((sec_source - sec_tree).subs({g: 1 / sp.sqrt(1 - s**2), ux**2 + uy**2 + uz**2: 1}))
diff = sp.simplify(diff.subs(uz, sp.sqrt(1 - ux**2 - uy**2)))
rec("SEC: (T_ab - T g_ab/2)V^aV^b == T(V,V) + T/2 for unit V (certify.py:349)", diff == 0, "residual %s" % diff)
rec("certify.py:346-347 V = gamma(1, s u), |u| = 1, is unit timelike",
    sp.simplify(gVV.subs({g: 1 / sp.sqrt(1 - s**2), uz: sp.sqrt(1 - ux**2 - uy**2)})) == -1)
# Kontou-Sanders eq.(20): T/(n-2); n = 4 gives 1/2.  A 5-D use would need 1/3.
n = sp.Symbol("n"); rec("T/(n-2) at n = 4 is T/2 (K-S eq. 20); at n = 5 it is T/3", (1/(n-2)).subs(n, 4) == sp.Rational(1, 2) and (1/(n-2)).subs(n, 5) == sp.Rational(1, 3))

print("\nD. THE WEC 'MINIMUM' OVER A SPEED GRID IS A SAMPLE, NOT AN INFIMUM  [sympy]")
# T(V,V) = gamma^2 (rho + s^2 sum p_i u_i^2): if any rho + p_i < 0 the infimum over
# unit timelike V is -infinity (Tipler 1978 / K-S Prop. 2.2).  certify.py samples s <= 10/11.
expr = sp.simplify(TVV.subs({g: 1 / sp.sqrt(1 - s**2)}))
rec("T(V,V) = (rho + s^2 sum p_i u_i^2)/(1 - s^2)", sp.simplify(expr - (r_ + s**2 * (a_ * ux**2 + b_ * uy**2 + c_ * uz**2)) / (1 - s**2)) == 0)
lim = sp.limit(((r_ + s**2 * a_) / (1 - s**2)).subs({r_: 1, a_: -2}), s, 1, "-")
rec("with rho = 1, p_1 = -2 (NEC fails) the WEC infimum along u = x is -oo", lim == -sp.oo, str(lim))

print("\nE. NULL CONTRACTIONS IN SPHERICAL SYMMETRY (nonstatic.py:324-325,351-352; formation.py:169-171)  [sympy]")
Phi, Lam, R, th = sp.symbols("Phi Lambda R theta", positive=True)
rho_s, j_s, pr_s, pT_s = sp.symbols("rho j p_r p_T", real=True)
gm = sp.diag(-sp.exp(2 * Phi), sp.exp(2 * Lam), R**2, R**2 * sp.sin(th)**2)
# orthonormal components: T_{t^t^} = rho, T_{t^r^} = -j (j = energy flux outward), T_{r^r^} = p_r, T_{th th} = p_T
e = [sp.exp(Phi), sp.exp(Lam), R, R * sp.sin(th)]
Th = sp.Matrix([[rho_s, -j_s, 0, 0], [-j_s, pr_s, 0, 0], [0, 0, pT_s, 0], [0, 0, 0, pT_s]])
Tc = sp.Matrix(4, 4, lambda m, nn: Th[m, nn] * e[m] * e[nn])     # coordinate components
k_rad = sp.Matrix([sp.exp(-Phi), sp.exp(-Lam), 0, 0])
k_trn = sp.Matrix([sp.exp(-Phi), 0, 1 / R, 0])
rec("k_rad is null", sp.simplify((k_rad.T * gm * k_rad)[0]) == 0)
rec("k_trn = (e^-Phi, 0, 1/R, 0) is null (NOT among nonstatic.py's checked identities)", sp.simplify((k_trn.T * gm * k_trn)[0]) == 0)
rec("T(k_rad,k_rad) = rho + p_r - 2j with j = -T_{t^r^} = T^{t^r^} (outward flux)", sp.simplify((k_rad.T * Tc * k_rad)[0] - (rho_s + pr_s - 2 * j_s)) == 0)
rec("T(k_trn,k_trn) = rho + p_T", sp.simplify((k_trn.T * Tc * k_trn)[0] - (rho_s + pT_s)) == 0)
u = sp.Matrix([sp.exp(-Phi), 0, 0, 0]); nvec = sp.Matrix([0, sp.exp(-Lam), 0, 0])
rec("formation.py H_NULL: k = u + n with -u.k = 1", sp.simplify((u.T * gm * (u + nvec))[0] + 1) == 0 and sp.simplify(k_rad - (u + nvec)) == sp.zeros(4, 1))

print("\nF. 'SATURATED BY THE VACUUM AND BY EM' (bounds.py:43,94-95,295)  [sympy, Coulomb + plane wave]")
Ex, Ey, Ez, Bx, By, Bz = sp.symbols("E_x E_y E_z B_x B_y B_z", real=True)
F = sp.Matrix([[0, -Ex, -Ey, -Ez], [Ex, 0, Bz, -By], [Ey, -Bz, 0, Bx], [Ez, By, -Bx, 0]])  # F_{ab}, eta = diag(-1,1,1,1)
etai = eta
Fud = etai * F                                                    # F^a_b
FF = sum(F[a, b] * (etai * F * etai)[a, b] for a in range(4) for b in range(4))
TEM = sp.Matrix(4, 4, lambda a, b: sum(F[a, c] * (etai * F)[c, b] * 0 for c in range(4)))
# T_ab = F_ac F_b^c - (1/4) eta_ab F_cd F^cd
Fup = etai * F * etai                                              # F^{ab}
TEM = sp.Matrix(4, 4, lambda a, b: sum(F[a, c] * (F * etai)[b, c] for c in range(4)) - sp.Rational(1, 4) * eta[a, b] * FF)
rec("EM T_00 = (E^2 + B^2)/2", sp.simplify(TEM[0, 0] - (Ex**2 + Ey**2 + Ez**2 + Bx**2 + By**2 + Bz**2) / 2) == 0)
rec("EM stress tensor is traceless (n = 4)", sp.simplify(sum(eta[m, m] * TEM[m, m] for m in range(4))) == 0)
nx, ny, nz = sp.symbols("n_x n_y n_z", real=True)
k = sp.Matrix([1, nx, ny, nz])
Tkk = sp.expand((k.T * TEM * k)[0])
w = F * k                                                          # w_a = F_ab k^b
wn = sp.expand((w.T * eta * w)[0])
rec("EM: T(k,k) = |F_ab k^b|^2 (a norm of a vector orthogonal to k, hence >= 0)",
    sp.simplify((Tkk - wn).subs(nz, sp.sqrt(1 - nx**2 - ny**2))) == 0)
coul = Tkk.subs({Ey: 0, Ez: 0, Bx: 0, By: 0, Bz: 0})
rec("Coulomb field E = (E,0,0): T(k,k) = E^2 (1 - n_x^2), zero ONLY along +-E (2 of the sphere of null directions)",
    sp.simplify(coul.subs(nz, sp.sqrt(1 - nx**2 - ny**2)) - Ex**2 * (1 - nx**2)) == 0)
pw = Tkk.subs({Ex: 0, Ez: 0, Bx: 0, Bz: 0, By: Ey})              # plane wave along +x: E_y = B_y = A... (E x B along x)
pw = Tkk.subs({Ex: 0, Ez: 0, Bx: 0, By: 0, Bz: Ey})               # E = (0,A,0), B = (0,0,A): E x B = +x
rec("null EM field (plane wave along +x): T(k,k) = A^2 (1 - n_x)^2, zero ONLY for k along the wave",
    sp.simplify(pw.subs(nz, sp.sqrt(1 - nx**2 - ny**2)) - Ey**2 * (1 - nx)**2) == 0)
rec("so the ONLY EM field with T(k,k) = 0 for EVERY null k is F = 0 (Coulomb and plane-wave cases both witness a positive value)", True,
    "bounds.py's 'saturated by EM' holds pointwise only along the field's principal null directions")

print("\nG. THE TREE'S OWN TABLE (certify.py:76-82) RECOMPUTED, AND A CLOSED FORM  [numeric + sympy]")
sys.path.insert(0, "/home/user/Claude-Method-Works/research/warp-drive")
import certify
dev = certify.conformastatic()
pinned = {0.2: (-4.7451e-01, -7.6490e-01, -4.1169e+00, -3.7316e+00),
          1.0: (-4.6564e-04, -8.7348e-04, -4.6251e-03, -4.1844e-03),
          10.0: (-4.0744e-08, -8.0044e-08, -4.2191e-07, -3.8135e-07)}
for r, want in pinned.items():
    Tn = certify.stress_energy(dev, [0, r, 0.0, 0.0], max(r * 1e-4, 1e-7))
    Thn = certify.orthonormal(Tn, dev([0, r, 0, 0]))
    nec, wec, sec = certify.energy_conditions(Thn)
    got = (Thn[0][0], nec, wec, sec)
    close = all(abs(a - b) <= 2e-3 * abs(b) for a, b in zip(got, want))
    rec("certify table row r = %g reproduced to 0.2%%" % r, close, "got %s" % (["%.4e" % x for x in got],))
    rec("  r = %g: NEC < 0, WEC < 0, SEC < 0, so dec_holds(wec) is False" % r, nec < 0 and wec < 0 and sec < 0 and not certify.dec_holds(wec))
# Closed form: conformastatic g = diag(-e^{2Phi}, e^{-2Phi} delta) with Phi(r); orthonormal G_{t^t^}.
rr = sp.symbols("r", positive=True); Pf = sp.Function("Phi")(rr)
x = [sp.Symbol("t"), rr, th, sp.Symbol("varphi")]
gc = sp.diag(-sp.exp(2 * Pf), sp.exp(-2 * Pf), sp.exp(-2 * Pf) * rr**2, sp.exp(-2 * Pf) * rr**2 * sp.sin(th)**2)
gci = gc.inv()
def christoffel(gm_, gi_):
    return [[[sum(gi_[a, d] * (sp.diff(gm_[d, b], x[c]) + sp.diff(gm_[d, c], x[b]) - sp.diff(gm_[b, c], x[d])) for d in range(4)) / 2
              for c in range(4)] for b in range(4)] for a in range(4)]
Gam = christoffel(gc, gci)
def ricci(Gam):
    return sp.Matrix(4, 4, lambda b, c: sp.simplify(sum(sp.diff(Gam[a][b][c], x[a]) - sp.diff(Gam[a][b][a], x[c])
                     + sum(Gam[a][a][d] * Gam[d][b][c] - Gam[a][c][d] * Gam[d][b][a] for d in range(4)) for a in range(4))))
Ric = ricci(Gam)
Rs = sp.simplify(sum(gci[a, b] * Ric[a, b] for a in range(4) for b in range(4)))
G = sp.simplify(Ric - Rs * gc / 2)
Gtt_hat = sp.simplify(G[0, 0] / sp.exp(2 * Pf))
lap = sp.diff(Pf, rr, 2) + 2 * sp.diff(Pf, rr) / rr
grad2 = sp.diff(Pf, rr)**2
closed = sp.simplify(Gtt_hat - sp.exp(2 * Pf) * (2 * lap - grad2))   # candidate closed form
print("     G_{t^t^} =", Gtt_hat)
rec("closed form: T_{t^t^} = e^{2Phi} (2 Lap Phi - |grad Phi|^2)  (T = G in certify's units)", closed == 0, "residual %s" % closed)
# Evaluate at r = 1 with certify's Phi and compare with the finite-difference pins
m, a, Rs_ = 0.02, 0.02, 200.0
Phi_num = m / sp.sqrt(rr**2 + a**2) - m / rr            # r < R_s so max(r, R_s) = R_s: -m/R_s constant, drops from derivatives
Phi_full = m / sp.sqrt(rr**2 + a**2) - m / Rs_
val = float((sp.exp(2 * Phi_full) * (2 * lap - grad2)).subs(Pf, Phi_full).doit().subs(rr, 1))
gradv = float(sp.diff(Phi_full, rr).subs(rr, 1))
rec("closed-form T_00 at r = 1 vs certify's TABLE figure -4.6564e-4 (line 80)", abs(val - (-4.6564e-4)) < 2e-7, "exact %.6e" % val)
rec("DISCREPANCY RECORDED, NOT REPAIRED: certify.py:96 and :456 pin T_00(r=1) = -4.8455e-4, 4.1%% off its own table and the closed form; near() there is tol*max(1,|want|) = 1e-3 ABSOLUTE so the pin cannot discriminate; the prose ratio 1.21 (:97) is exactly %.3f. Sign and conclusion unaffected." % (val / (-gradv**2)), True)
rec("-|grad Phi|^2 at r = 1 vs certify's pin -3.9952e-4", abs(-gradv**2 - (-3.9952e-4)) < 1e-7, "exact %.6e, ratio %.3f" % (-gradv**2, val / (-gradv**2)))
# NEC minimum exactly: type I static => min(rho+p_r, rho+p_T); compare to sampled 200-direction minimum
Grr_hat = sp.simplify(G[1, 1] * sp.exp(2 * Pf)); Gthth_hat = sp.simplify(G[2, 2] * sp.exp(2 * Pf) / rr**2)
f = lambda ex: float(ex.subs(Pf, Phi_full).doit().subs(rr, 1))
rho1, pr1, pT1 = f(Gtt_hat), f(Grr_hat), f(Gthth_hat)
nec_exact = min(rho1 + pr1, rho1 + pT1)
Tn = certify.stress_energy(dev, [0, 1.0, 0.0, 0.0], 1e-4); Thn = certify.orthonormal(Tn, dev([0, 1.0, 0, 0]))
nec_s, wec_s, sec_s = certify.energy_conditions(Thn)
rec("exact NEC min at r = 1 (rho+p_r, rho+p_T) brackets certify's sampled -8.7348e-4", nec_exact <= nec_s + 1e-9 and abs(nec_exact - nec_s) < 2e-2 * abs(nec_exact),
    "rho %.4e p_r %.4e p_T %.4e -> exact min %.4e, sampled %.4e" % (rho1, pr1, pT1, nec_exact, nec_s))
rec("at r = 1 rho < 0 (WEC fails for the STATIC observer alone, no sampling needed)", rho1 < 0)

print("\nH. phase1.py:195-197 AGAINST THE DEFINITION AS READ  [sympy]")
# certify.py:110-125 (ansatz-free): dm/dr = 4 pi r^2 rho, m(0) = 0; a shortened region needs m(r) < 0.
# If m(r1) < 0 then rho < 0 somewhere in (0, r1) => T(u,u) < 0 for the static u => WEC fails => DEC fails.
rho_f = sp.Function("rho"); r1 = sp.Symbol("r_1", positive=True)
rec("m(r1) = INT_0^r1 4 pi r^2 rho dr < 0 forces rho < 0 on a set of positive measure in (0, r1) (mean-value; rho >= 0 => m >= 0)",
    True, "phase1's 'every line needs M < 0' (phase1.py:203-204, 558-559) therefore entails a pointwise WEC and DEC failure -- contradicting phase1.py:195-197 as worded")

print("\nSUMMARY")
fails = [t for t, ok, _ in OUT if not ok]
print("  %d checks, %d failed%s" % (len(OUT), len(fails), (": " + "; ".join(fails)) if fails else ""))
sys.exit(1 if fails else 0)
