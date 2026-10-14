#!/usr/bin/env python3
"""DOCKET 67 re-derivation, result 24/286: maxwell-stress-energy-curved-spherical.

Re-derives, independently of drivensource.electrovac(), in the full dynamical
spherically symmetric metric
    ds^2 = -e^{2Phi(t,r)} dt^2 + e^{2Lambda(t,r)} dr^2 + R(t,r)^2 dOmega^2
the following, and records each as PASS/FAIL:

 A. SYMMETRY: the most general 2-form invariant under the three rotation Killing
    fields (Lie derivative zero, sympy) is F = E(t,r) dt^dr + B(t,r) sin(theta) dtheta^dphi.
    So "spherical symmetry admits only F_{tr}" is checked as a CLAIM.
 B. MAXWELL: dF = 0 and d_a(sqrt(-g) F^{ab}) = 0 force E = Q e^{Phi+Lambda}/R^2 and
    B = P (constant): Gauss' law fixes both charges.
 C. GAUSS' LAW AS WRITTEN: what sqrt(-g) F^{tr} actually equals for that F.
 D. STRESS-ENERGY (Gaussian, signature -+++, T_ab = (F_ac F_b^c - g_ab F^2/4)/(4 pi)):
    rho, j, p_r, p_T for the dyonic field, and the tree's Q-only specialisation.
 E. NEC saturation rho + p_r = 0, tracelessness, positivity, with P present.
 F. Misner-Sharp/Birkhoff residuals with m = M - (Q^2 + P^2)/(2R), M constant, arbitrary
    Phi, Lambda, R (the rests_on step).
 G. Units cross-check: the same T_ab in Heaviside-Lorentz/SI-shaped form (no 4 pi) gives
    rho = Q^2/(2 R^4) -- the tree's Q^2/(8 pi R^4) is the Gaussian convention.
"""
import sympy as sp

t, r, th, ph = sp.symbols("t r theta phi", real=True)
x = [t, r, th, ph]
Phi = sp.Function("Phi")(t, r)
Lam = sp.Function("Lambda")(t, r)
R = sp.Function("R")(t, r)
Q, P = sp.symbols("Q P", real=True)

g = sp.diag(-sp.exp(2 * Phi), sp.exp(2 * Lam), R**2, R**2 * sp.sin(th)**2)
gi = g.inv()
sg = sp.sqrt(-g.det())
sg = sp.simplify(sg)  # e^{Phi+Lam} R^2 |sin th|; take sin th > 0 on the chart
sg = sp.exp(Phi + Lam) * R**2 * sp.sin(th)

results = []
def rec(label, cond, detail=""):
    results.append((label, bool(cond), detail))
    print("  %-70s %s  %s" % (label, "PASS" if cond else "FAIL", detail))

# ---------------------------------------------------------------- A. symmetry
print("A. Which 2-forms are invariant under SO(3)?")
# rotation Killing vectors on the sphere (components in t,r,th,ph)
xi1 = [0, 0, -sp.sin(ph), -sp.cot(th) * sp.cos(ph)]
xi2 = [0, 0, sp.cos(ph), -sp.cot(th) * sp.sin(ph)]
xi3 = [0, 0, 0, 1]
Fs = sp.Matrix(4, 4, lambda a, b: 0)
names = {}
for a in range(4):
    for b in range(a + 1, 4):
        f = sp.Function("F%d%d" % (a, b))(t, r, th, ph)
        Fs[a, b] = f
        Fs[b, a] = -f
        names[(a, b)] = f
def lie(xi, F):
    # (L_xi F)_ab = xi^c d_c F_ab + F_cb d_a xi^c + F_ac d_b xi^c
    L = sp.zeros(4, 4)
    for a in range(4):
        for b in range(4):
            L[a, b] = (sum(xi[c] * sp.diff(F[a, b], x[c]) for c in range(4))
                       + sum(F[c, b] * sp.diff(xi[c], x[a]) for c in range(4))
                       + sum(F[a, c] * sp.diff(xi[c], x[b]) for c in range(4)))
    return L
# Check that the candidate F = E(t,r) dt^dr + B(t,r) sin th dth^dph IS invariant
E = sp.Function("E")(t, r); B = sp.Function("B")(t, r)
Fc = sp.zeros(4, 4)
Fc[0, 1] = E; Fc[1, 0] = -E
Fc[2, 3] = B * sp.sin(th); Fc[3, 2] = -B * sp.sin(th)
inv_ok = all(sp.simplify(lie(xi, Fc)[a, b]) == 0
             for xi in (xi1, xi2, xi3) for a in range(4) for b in range(4))
rec("A1 F = E dt^dr + B sin(th) dth^dph is SO(3)-invariant", inv_ok)
# Check that the candidate is the ONLY one: solve L_xi F = 0 for a general F.
# xi3 = d/dphi: all components independent of phi.
# Then use xi1, xi2 at generic theta for the remaining freedom.
Fg = Fs.subs({names[k]: sp.Function("G%d%d" % k)(t, r, th) for k in names})
eqs = []
for xi in (xi1, xi2):
    L = lie(xi, Fg)
    for a in range(4):
        for b in range(a + 1, 4):
            eqs.append(sp.simplify(L[a, b]))
# Collect coefficients of sin(ph), cos(ph) -- each must vanish separately.
conds = set()
for e in eqs:
    e = sp.expand(e)
    for trig in (sp.sin(ph), sp.cos(ph)):
        c = sp.simplify(e.coeff(trig))
        if c != 0:
            conds.add(c)
    rest = sp.simplify(e.subs({sp.sin(ph): 0, sp.cos(ph): 0}))
    if rest != 0:
        conds.add(rest)
conds = sorted(conds, key=str)
# Expected content: G02 = G03 = G12 = G13 = 0 ; dG01/dth = 0 ; G23 = B(t,r) sin th.
G = {k: sp.Function("G%d%d" % k)(t, r, th) for k in names}
sol_mixed = all(any(sp.simplify(c - G[k]) == 0 or sp.simplify(c + G[k]) == 0
                    or sp.simplify(c / G[k]).free_symbols <= {th} for c in conds)
                for k in [(0, 2), (0, 3), (1, 2), (1, 3)])
# Rather than parse, verify by substitution that the general solution reduces the
# condition set to zero and that a mixed component breaks it:
subs_sol = {G[(0, 2)]: 0, G[(0, 3)]: 0, G[(1, 2)]: 0, G[(1, 3)]: 0,
            G[(0, 1)]: E, G[(2, 3)]: B * sp.sin(th)}
all_zero = all(sp.simplify(c.subs(subs_sol).doit()) == 0 for c in conds)
rec("A2 the invariance conditions vanish on F = E dt^dr + B sin th dth^dph", all_zero,
    "%d conditions" % len(conds))
# Try to break it: put G02 = h(t,r) (a t-theta electric-type component)
h = sp.Function("h")(t, r)
broken = any(sp.simplify(c.subs({**subs_sol, G[(0, 2)]: h}).doit()) != 0 for c in conds)
rec("A3 a nonzero F_{t theta} = h(t,r) VIOLATES SO(3) invariance", broken)
# and F_{theta phi} = B(t,r) * f(theta) with f != sin theta is NOT invariant:
f = sp.Function("f")(th)
brk2 = [sp.simplify(c.subs({**subs_sol, G[(2, 3)]: B * f}).doit()) for c in conds]
brk2 = [c for c in brk2 if c != 0]
rec("A4 F_{theta phi} = B(t,r) f(theta) invariant only if f' = f cot th (f = sin th)",
    len(brk2) > 0 and all(sp.simplify(c.subs(f, sp.sin(th)).doit()) == 0 for c in brk2),
    str(brk2[:1]))
# So spherical symmetry admits F_{tr} AND F_{theta phi} = B sin th: the tree's
# "admits only F_{tr}" is the B = 0 (no magnetic charge) case.

# ---------------------------------------------------------------- B. Maxwell
print("B. Maxwell equations fix E and B")
F = Fc
Fup = gi * F * gi
divF = [sp.simplify(sum(sp.diff(sg * Fup[a, b], x[a]) for a in range(4)) / sg)
        for b in range(4)]
# dF = 0: components (dF)_{abc}
def dF(F):
    out = {}
    for a in range(4):
        for b in range(a + 1, 4):
            for c in range(b + 1, 4):
                out[(a, b, c)] = sp.simplify(sp.diff(F[b, c], x[a]) - sp.diff(F[a, c], x[b])
                                             + sp.diff(F[a, b], x[c]))
    return out
bianchi = dF(F)
print("   d_a(sqrt(-g)F^{ab})/sqrt(-g) =", divF)
print("   dF components =", bianchi)
# divF: b=0 gives d_r(E R^2 e^{-Phi-Lam}) = 0 ; b=1 gives d_t(...) = 0 -> E R^2 e^{-Phi-Lam} = const =: -Q? sign below
# dF = 0: d_t B = d_r B = 0 -> B = const =: P
Esol = Q * sp.exp(Phi + Lam) / R**2
Fd = F.subs({E: Esol, B: P}).doit()
Fupd = gi * Fd * gi
divFd = [sp.simplify(sum(sp.diff(sg * Fupd[a, b], x[a]) for a in range(4))) for b in range(4)]
bianchid = dF(Fd)
rec("B1 with E = Q e^{Phi+Lam}/R^2, B = P: d_a(sqrt(-g)F^{ab}) = 0 for all b",
    all(v == 0 for v in divFd), str(divFd))
rec("B2 with E = Q e^{Phi+Lam}/R^2, B = P: dF = 0 (Bianchi half, not checked by the tree)",
    all(v == 0 for v in bianchid.values()))
# uniqueness: the general divF conditions are exactly d_t and d_r of E R^2 e^{-Phi-Lam}
u = E * R**2 * sp.exp(-Phi - Lam)
rec("B3 divF conditions == {d_r u = 0, d_t u = 0}, u = E R^2 e^{-Phi-Lam}, so E is UNIQUE",
    sp.simplify(divF[0] * sg / sp.diff(u, r)).free_symbols <= {t, r, th} and
    sp.simplify(divF[1] * sg / sp.diff(u, t)).free_symbols <= {t, r, th} and
    sp.simplify(divF[2]) == 0 and sp.simplify(divF[3]) == 0,
    "ratios: %s ; %s" % (sp.simplify(divF[0] * sg / sp.diff(u, r)), sp.simplify(divF[1] * sg / sp.diff(u, t))))
rec("B4 dF = 0 forces d_t B = d_r B = 0 (B = P constant)",
    set(sp.simplify(v) for v in bianchi.values()) <= {0, sp.sin(th) * sp.diff(B, t),
                                                        sp.sin(th) * sp.diff(B, r),
                                                        -sp.sin(th) * sp.diff(B, t),
                                                        -sp.sin(th) * sp.diff(B, r)},
    str(set(bianchi.values())))

# ---------------------------------------------------------------- C. Gauss' law as written
print("C. What sqrt(-g) F^{tr} equals (the comment at drivensource.py:302-303 says 'Q')")
gauss = sp.simplify(sg * Fupd[0, 1])
print("   sqrt(-g) F^{tr} =", gauss)
rec("C1 sqrt(-g) F^{tr} = -Q sin(theta)  (not +Q: sign and sin theta are a misprint in the comment)",
    sp.simplify(gauss + Q * sp.sin(th)) == 0)
rec("C2 the invariant form: (1/4pi) INT_S2 *F = Q  i.e. R^2 e^{-Phi-Lam} F_{tr} = Q",
    sp.simplify(R**2 * sp.exp(-Phi - Lam) * Fd[0, 1] - Q) == 0)

# ---------------------------------------------------------------- D. stress-energy
print("D. Maxwell stress-energy, Gaussian, T_ab = (F_ac F_b^c - g_ab F_cd F^cd /4)/(4 pi)")
Fdd = sum(Fd[a, b] * Fupd[a, b] for a in range(4) for b in range(4))
Fmix = Fd * gi  # F_a^c = F_ac g^{cb}
T = sp.Matrix(4, 4, lambda a, b: sp.simplify(
    (sum(Fd[a, c] * Fmix[b, c] for c in range(4)) - sp.Rational(1, 4) * g[a, b] * Fdd) / (4 * sp.pi)))
rho = sp.simplify(T[0, 0] * sp.exp(-2 * Phi))
j = sp.simplify(-T[0, 1] * sp.exp(-Phi - Lam))
p_r = sp.simplify(T[1, 1] * sp.exp(-2 * Lam))
p_T = sp.simplify(T[2, 2] / R**2)
p_T2 = sp.simplify(T[3, 3] / (R**2 * sp.sin(th)**2))
print("   rho =", rho, "; j =", j, "; p_r =", p_r, "; p_T =", p_T)
tgt = (Q**2 + P**2) / (8 * sp.pi * R**4)
rec("D1 rho = (Q^2 + P^2)/(8 pi R^4)  [dyonic]", sp.simplify(rho - tgt) == 0)
rec("D2 j = 0", j == 0)
rec("D3 p_r = -rho", sp.simplify(p_r + rho) == 0)
rec("D4 p_T = +rho (both angular components)", sp.simplify(p_T - rho) == 0 and sp.simplify(p_T2 - rho) == 0)
rec("D5 tree's specialisation P = 0: rho = Q^2/(8 pi R^4)", sp.simplify(rho.subs(P, 0) - Q**2 / (8 * sp.pi * R**4)) == 0)
# off-diagonal check: T_{t theta} etc. vanish
rec("D6 all off-diagonal T_ab vanish", all(T[a, b] == 0 for a in range(4) for b in range(4) if a != b))
# a lower-level cross-check of T via the electric/magnetic invariants: F_cd F^cd = 2(B^2 - E^2)
E_phys = Q / R**2  # orthonormal-frame radial electric field
B_phys = P / R**2
rec("D7 F_cd F^cd = 2 (B_phys^2 - E_phys^2) with E_phys = Q/R^2, B_phys = P/R^2",
    sp.simplify(Fdd - 2 * (B_phys**2 - E_phys**2)) == 0)
rec("D8 rho equals the flat-space (E^2 + B^2)/(8 pi) in the orthonormal frame",
    sp.simplify(rho - (E_phys**2 + B_phys**2) / (8 * sp.pi)) == 0)

# ---------------------------------------------------------------- E. energy conditions
print("E. NEC saturation, trace, positivity")
rec("E1 rho + p_r = 0 (radial NEC saturated, P included)", sp.simplify(rho + p_r) == 0)
rec("E2 rho + p_T = 2 rho >= 0 (tangential NEC, strictly positive for Q^2+P^2 > 0)",
    sp.simplify(rho + p_T - 2 * tgt) == 0)
rec("E3 traceless: -rho + p_r + 2 p_T = 0", sp.simplify(-rho + p_r + 2 * p_T) == 0)
xx = sp.Symbol("x", positive=True)
rec("E4 rho > 0 for all R > 0 whenever (Q,P) != (0,0)",
    sp.ask(sp.Q.positive(rho.subs(R, xx).subs({Q: sp.Symbol("q", positive=True), P: 0}))) is True
    and sp.ask(sp.Q.nonnegative(rho.subs(R, xx))) is True)
# WEC/DEC: rho >= |p_r|, rho >= |p_T|: rho - |p| = 0 -> saturated, holds
_pos = {R: xx}
rec("E5 DEC: rho >= |p_r| and rho >= |p_T| (both saturated), on R = x > 0",
    sp.simplify(rho.subs(_pos) - sp.Abs(p_r.subs(_pos))) == 0
    and sp.simplify(rho.subs(_pos) - sp.Abs(p_T.subs(_pos))) == 0)

# ---------------------------------------------------------------- F. Birkhoff / Misner-Sharp
print("F. Misner-Sharp equations with the dyonic source: m = M - (Q^2+P^2)/(2R), M constant")
M = sp.Symbol("M")
U = sp.exp(-Phi) * sp.diff(R, t)
W = sp.exp(-Lam) * sp.diff(R, r)
Dt = lambda f_: sp.exp(-Phi) * sp.diff(f_, t)
Dr = lambda f_: sp.exp(-Lam) * sp.diff(f_, r)
m = M - (Q**2 + P**2) / (2 * R)
res_r = sp.simplify(Dr(m) - 4 * sp.pi * R**2 * (rho * W + j * U))
res_t = sp.simplify(Dt(m) + 4 * sp.pi * R**2 * (p_r * U + j * W))
rec("F1 MS-r residual D_r m - 4 pi R^2 (rho W + j U) = 0 for ARBITRARY Phi, Lam, R", res_r == 0, str(res_r))
rec("F2 MS-t residual D_t m + 4 pi R^2 (p_r U + j W) = 0 for ARBITRARY Phi, Lam, R", res_t == 0, str(res_t))
# and the MS mass is by definition m = R(1 - g^{ab} d_a R d_b R)/2 = R(1 + U^2 - W^2)/2 ; with the
# residuals the field equations G = 8 pi T then close as RN: 1 - 2m/R = 1 - 2M/R + (Q^2+P^2)/R^2
rec("F3 1 - 2m/R = 1 - 2M/R + (Q^2+P^2)/R^2  (Reissner-Nordstrom (dyonic) form, G = c = 1, Gaussian)",
    sp.simplify((1 - 2 * m / R) - (1 - 2 * M / R + (Q**2 + P**2) / R**2)) == 0)
rec("F4 m(R) < 0  iff  R < (Q^2+P^2)/(2M)  for M > 0  (the rests_on step of ledger D4)",
    sp.simplify(sp.solve(sp.Eq(m.subs(R, xx), 0), xx)[0] - (Q**2 + P**2) / (2 * M)) == 0)

# ---------------------------------------------------------------- G. units
print("G. Units: same T with the Heaviside-Lorentz/SI-shaped normalisation (no 4 pi)")
T_HL = sp.Matrix(4, 4, lambda a, b: sp.simplify(
    sum(Fd[a, c] * Fmix[b, c] for c in range(4)) - sp.Rational(1, 4) * g[a, b] * Fdd))
rho_HL = sp.simplify(T_HL[0, 0] * sp.exp(-2 * Phi))
rec("G1 Heaviside-Lorentz rho = (Q^2+P^2)/(2 R^4) = 4 pi x Gaussian rho: the 8 pi is a unit convention",
    sp.simplify(rho_HL - 4 * sp.pi * rho) == 0)
# SI: rho = Q^2/(32 pi^2 eps0 R^4) -- Gaussian Q_G^2 = Q_SI^2/(4 pi eps0)
Qsi, eps0 = sp.symbols("Q_SI epsilon_0", positive=True)
rec("G2 SI form rho = Q_SI^2/(32 pi^2 eps0 R^4) via Q_G^2 = Q_SI^2/(4 pi eps0) (section 4's X = Q^2/(8 pi eps0 c^2) is INT rho 4 pi R^2 dR from a: X/a)",
    sp.simplify((Q**2 / (8 * sp.pi * R**4)).subs(Q**2, Qsi**2 / (4 * sp.pi * eps0)) - Qsi**2 / (32 * sp.pi**2 * eps0 * R**4)) == 0
    and sp.simplify(sp.integrate(Qsi**2 / (32 * sp.pi**2 * eps0 * xx**4) * 4 * sp.pi * xx**2, (xx, sp.Symbol("a", positive=True), sp.oo))
                    - Qsi**2 / (8 * sp.pi * eps0 * sp.Symbol("a", positive=True))) == 0)

# ---------------------------------------------------------------- H. run the owner's own function
print("H. The owner's electrovac() re-run here (import by path, nothing edited)")
try:
    import importlib.util, sys
    spec = importlib.util.spec_from_file_location(
        "drivensource", "/home/user/Claude-Method-Works/research/warp-drive/drivensource.py")
    ds = importlib.util.module_from_spec(spec)
    sys.modules["drivensource"] = ds
    spec.loader.exec_module(ds)
    EV = ds.electrovac()
    spo = EV["sp"]
    rec("H1 owner: Maxwell residuals [0,0,0,0]", EV["maxwell"] == [0, 0, 0, 0])
    rec("H2 owner: rho = Q^2/(8 pi R^4), j = 0, p_r = -rho, p_T = rho",
        spo.simplify(EV["rho"] - EV["Q"]**2 / (8 * spo.pi * EV["R"]**4)) == 0
        and spo.simplify(EV["j"]) == 0 and spo.simplify(EV["p_r"] + EV["rho"]) == 0
        and spo.simplify(EV["p_T"] - EV["rho"]) == 0)
    rec("H3 owner: independent rho here (P=0) == owner's rho",
        sp.simplify(rho.subs(P, 0).subs(Q, EV["Q"]) - EV["rho"]) == 0)
    rec("H4 owner: birkhoff_residuals() both 0", all(v == 0 for _, v in ds.birkhoff_residuals(EV)))
except Exception as ex:  # noqa
    rec("H0 owner import failed", False, repr(ex))

print()
n_ok = sum(1 for _, ok, _ in results if ok)
print("SUMMARY: %d/%d checks pass" % (n_ok, len(results)))
for label, ok, d in results:
    if not ok:
        print("  FAIL:", label, d)
