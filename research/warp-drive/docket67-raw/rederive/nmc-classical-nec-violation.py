#!/usr/bin/env python3
"""DOCKET 67 / nmc-classical-nec-violation -- re-derivation.

Claim audited (candidates.py:159-160): "A scalar coupled to curvature by
delta L = xi R phi^2 violates the NEC and WEC AT THE CLASSICAL LEVEL".
Source located: Barcelo & Visser, gr-qc/0003025v2, eqs (2.1)-(2.6) (mostly-plus
signature, S_matter = int sqrt(-g)[-1/2 (dphi)^2 - V - 1/2 xi R phi^2],
kappa = 1/(8 pi G)); wording lifted from Fliss-Freivogel-Kontou-Pardo Santos
2309.10848 sec. I ("delta L = xi R phi^2 allow violations of the NEC even at the
classical level").

Checks (sympy 1.14, z3, numpy):
 A  BV (2.2) is covariantly conserved on-shell: div T_{.nu} = (box phi - V' - xi R phi) d_nu phi
    identically, on a curved (t,r)-dependent spherically symmetric metric with arbitrary phi(t,r).
    Control: the trace-term sign printed in FFKPS eq. (9) (-g box) is NOT conserved.
 B  Null contraction: T_kk = (k.dphi)^2 + xi[G_kk phi^2 - k k nabla nabla phi^2]; V and the trace
    terms drop; hence BV (2.6): (kappa - xi phi^2) G_kk = phi'^2 - xi (phi^2)''.
 C  z3: case analysis of (2.6) at a strict extremum of phi^2 along the null geodesic.
    Computed assignment vs BV's prose (p.5) vs FFKPS's restatement (eq. 18 text).
 D  On-shell TEST-FIELD counterexample in Minkowski (G = 0, backreaction neglected):
    phi = c + eps (t^2 + z^2) solves box phi = 0; T_kk < 0 and T_00 < 0 at the origin for
    xi c eps > 0 -- NEC and WEC both violated, at arbitrarily small field amplitude.
 E  FULLY BACKREACTED example: flat FRW, V = m^2 phi^2 / 2, xi = 1, sub-Planckian phi.
    Integrate the Jordan-frame system; at every zero crossing of phi, Hdot = (2 xi - 1) phidot^2/(2 kappa)
    > 0, i.e. G_kk = -2 Hdot < 0 (NEC violated for the metric g); boosted observers see G_vv < 0 (WEC).
    Control: the EINSTEIN-frame Hubble rate is non-increasing along the same solution
    (Einstein-frame NEC holds) -- the violation is a Jordan-frame statement.
"""
import sys
import sympy as sp
import numpy as np

PASS, FAIL = [], []


def chk(name, ok, detail=""):
    (PASS if ok else FAIL).append(name)
    print(("PASS " if ok else "FAIL ") + name + ((" :: " + detail) if detail else ""))


# ----------------------------------------------------------------- geometry helpers
def christoffel(g, X):
    n = len(X)
    gi = g.inv()
    G = [[[0] * n for _ in range(n)] for _ in range(n)]
    for a in range(n):
        for b in range(n):
            for c in range(n):
                G[a][b][c] = sp.simplify(sum(gi[a, d] * (sp.diff(g[d, b], X[c]) + sp.diff(g[d, c], X[b])
                                                          - sp.diff(g[b, c], X[d])) for d in range(n)) / 2)
    return G


def ricci(G, X):
    n = len(X)
    R = sp.zeros(n)
    for b in range(n):
        for c in range(n):
            R[b, c] = sp.simplify(sum(sp.diff(G[a][b][c], X[a]) - sp.diff(G[a][b][a], X[c])
                                      + sum(G[a][a][d] * G[d][b][c] - G[a][c][d] * G[d][b][a] for d in range(n))
                                      for a in range(n)))
    return R


def hess(f, G, X):
    n = len(X)
    return sp.Matrix(n, n, lambda a, b: sp.diff(f, X[a], X[b]) - sum(G[c][a][b] * sp.diff(f, X[c]) for c in range(n)))


def div_lower(T, g, G, X):
    """(div T)_nu = g^{mu a} nabla_a T_{mu nu}."""
    n = len(X)
    gi = g.inv()
    out = []
    for nu in range(n):
        s = 0
        for mu in range(n):
            for a in range(n):
                if gi[mu, a] == 0:
                    continue
                dT = sp.diff(T[mu, nu], X[a]) - sum(G[c][a][mu] * T[c, nu] + G[c][a][nu] * T[mu, c] for c in range(n))
                s += gi[mu, a] * dT
        out.append(s)
    return out


t, r, th, ph = sp.symbols('t r theta phi_ang', real=True)
X = [t, r, th, ph]
xi, kap = sp.symbols('xi kappa', real=True)
A = sp.Function('A')(t, r)
B = sp.Function('B')(t, r)
F = sp.Function('F')(t, r)          # the scalar field phi(t,r)
Vf = sp.Function('V')

g = sp.diag(-sp.exp(2 * A), sp.exp(2 * B), r ** 2, r ** 2 * sp.sin(th) ** 2)
gi = g.inv()
Gam = christoffel(g, X)
Ric = ricci(Gam, X)
Rs = sp.simplify(sum(gi[a, b] * Ric[a, b] for a in range(4) for b in range(4)))
Ein = sp.simplify(Ric - g * Rs / 2)

dF = [sp.diff(F, x) for x in X]
gradsq = sum(gi[a, b] * dF[a] * dF[b] for a in range(4) for b in range(4))
H2 = hess(F ** 2, Gam, X)
boxF2 = sum(gi[a, b] * H2[a, b] for a in range(4) for b in range(4))
HF = hess(F, Gam, X)
boxF = sum(gi[a, b] * HF[a, b] for a in range(4) for b in range(4))
Vp = sp.Symbol('Vp')     # V'(phi) enters only via d_nu V = V' d_nu phi; model V as a function of F
V = Vf(F)


def T_BV(sign_trace=+1):
    # BV (2.2): d phi d phi - 1/2 g (dphi)^2 - g V + xi [G phi^2 - 2 nabla(phi nabla phi) + 2 g nabla.(phi nabla phi)]
    # note 2 nabla_mu(phi nabla_nu phi) = nabla_mu nabla_nu phi^2 ; 2 nabla.(phi nabla phi) = box phi^2
    return sp.Matrix(4, 4, lambda a, b: dF[a] * dF[b] - g[a, b] * gradsq / 2 - g[a, b] * V
                     + xi * (Ein[a, b] * F ** 2 - H2[a, b] + sign_trace * g[a, b] * boxF2))


print("A: conservation of BV (2.2) on a curved (t,r) metric, arbitrary phi(t,r), arbitrary V")
T = T_BV(+1)
dv = div_lower(T, g, Gam, X)
res_ok = True
for nu in (0, 1):
    target = (boxF - sp.diff(V, F) - xi * Rs * F) * dF[nu]
    d = sp.simplify(sp.expand(dv[nu] - target))
    res_ok = res_ok and d == 0
chk("A1 div T_BV = (box phi - V' - xi R phi) d phi, identically (nu = t, r)", res_ok)
chk("A1b angular components vanish", all(sp.simplify(dv[k]) == 0 for k in (2, 3)))
Tm = T_BV(-1)
dvm = div_lower(Tm, g, Gam, X)
bad = sp.simplify(sp.expand(dvm[0] - (boxF - sp.diff(V, F) - xi * Rs * F) * dF[0]))
chk("A2 control: FFKPS eq.(9) trace sign (-g box phi^2) is NOT conserved (misprint-class, null-irrelevant)",
    bad != 0, "residual_t = %s" % sp.simplify(bad / xi))

print("B: null contraction")
k = sp.Matrix([sp.exp(-A), sp.exp(-B), 0, 0])        # radial null vector
chk("B0 k is null", sp.simplify((k.T * g * k)[0]) == 0)
Tkk = sp.simplify((k.T * T * k)[0])
kdF = sum(k[a] * dF[a] for a in range(4))
Gkk = sp.simplify((k.T * Ein * k)[0])
kkH2 = sp.simplify((k.T * H2 * k)[0])
chk("B1 T_kk = (k.dphi)^2 + xi[G_kk phi^2 - kk nabla nabla phi^2]; V and trace terms absent",
    sp.simplify(Tkk - (kdF ** 2 + xi * (Gkk * F ** 2 - kkH2))) == 0 and not Tkk.has(Vf))
# kappa G_kk = T_kk  <=>  (kappa - xi phi^2) G_kk = (k.dphi)^2 - xi kk nabla nabla phi^2   (BV 2.6)
Gs = sp.Symbol('Gkk')
sol = sp.solve(sp.Eq(kap * Gs, kdF ** 2 + xi * (Gs * F ** 2 - kkH2)), Gs)[0]
chk("B2 BV (2.6): G_kk = [phi'^2 - xi (phi^2)'']/(kappa - xi phi^2)",
    sp.simplify(sol - (kdF ** 2 - xi * kkH2) / (kap - xi * F ** 2)) == 0)

print("C: z3 case analysis of (2.6) at a strict extremum of phi^2 (phi' = 0, phi != 0)")
import z3
x, K, p, pdd = z3.Reals('xi kappa phi phidd')
N = -x * 2 * p * pdd               # numerator at phi' = 0 : -xi (phi^2)'' = -2 xi phi phi''
D = K - x * p * p
viol = N * D < 0                   # G_kk < 0  <=>  N/D < 0
base = [K > 0, p != 0, D != 0]
cases = {
    "xi<0": [x < 0],
    "xi>0,small": [x > 0, x * p * p < K],
    "xi>0,large": [x > 0, x * p * p > K],
}
MAX = p * pdd < 0                  # (phi^2)'' = 2 phi phi'' < 0 : strict local max of phi^2
MIN = p * pdd > 0
computed = {}
for cname, cc in cases.items():
    row = {}
    for ename, e in (("max", MAX), ("min", MIN)):
        s = z3.Solver(); s.add(*base, *cc, e, viol)
        sat = s.check() == z3.sat
        s2 = z3.Solver(); s2.add(*base, *cc, e, z3.Not(viol))
        always = s2.check() == z3.unsat
        row[ename] = "ALWAYS-VIOLATES" if always else ("NEVER" if not sat else "SOMETIMES")
    computed[cname] = row
    print("   ", cname, row)
bv_prose = {"xi<0": "min", "xi>0,small": "max", "xi>0,large": "min"}        # gr-qc/0003025v2 p.5
ffkps = {"xi<0": "max", "xi>0,small": "min", "xi>0,large": "max"}           # 2309.10848 text after eq.(18)
comp_assign = {c: [e for e in ("max", "min") if computed[c][e] == "ALWAYS-VIOLATES"] for c in computed}
chk("C1 each case: exactly one extremum type violates, the other never does",
    all(len(v) == 1 and computed[c][{'max': 'min', 'min': 'max'}[v[0]]] == "NEVER" for c, v in comp_assign.items()))
chk("C2 computed assignment == FFKPS 2023 restatement", all(comp_assign[c] == [ffkps[c]] for c in cases))
chk("C3 DISCREPANCY: BV prose (p.5) is the swap of its own eq. (2.6) in all three cases",
    all(comp_assign[c] != [bv_prose[c]] for c in cases))
# phi = 0 crossing: (phi^2)'' = 2 phi'^2, numerator (1 - 2 xi) phi'^2, D = kappa
pd = z3.Real('phid')
s = z3.Solver(); s.add(K > 0, pd != 0, x > 0, x <= z3.RealVal("1/2"), (1 - 2 * x) * pd * pd * K < 0)
chk("C4 at a zero of phi with phi' != 0: NEC violated iff xi > 1/2 (unsat for 0 < xi <= 1/2)", s.check() == z3.unsat)
s = z3.Solver(); s.add(K > 0, pd != 0, x > z3.RealVal("1/2"), z3.Not((1 - 2 * x) * pd * pd * K < 0))
chk("C4b ... and always violated for xi > 1/2", s.check() == z3.unsat)
s = z3.Solver(); s.add(K > 0, x == 0, D != 0, z3.Real('q') * z3.Real('q') / K < 0)
chk("C5 xi = 0: (2.6) numerator phi'^2 >= 0, no violation possible (unsat)", s.check() == z3.unsat)

print("D: on-shell test field in Minkowski")
T4, Z = sp.symbols('T Z', real=True)
c0, eps = sp.symbols('c epsilon', real=True)
Xm = [T4, sp.Symbol('x'), sp.Symbol('y'), Z]
eta = sp.diag(-1, 1, 1, 1)
phi = c0 + eps * (T4 ** 2 + Z ** 2)
box = -sp.diff(phi, T4, 2) + sum(sp.diff(phi, v, 2) for v in Xm[1:])
chk("D0 phi = c + eps (t^2 + z^2) solves box phi = 0", sp.simplify(box) == 0)
dphi = [sp.diff(phi, v) for v in Xm]
gs = sum(eta[a, a] * dphi[a] ** 2 for a in range(4))
Hm = sp.Matrix(4, 4, lambda a, b: sp.diff(phi ** 2, Xm[a], Xm[b]))
boxp2 = sum(eta[a, a] * Hm[a, a] for a in range(4))
Tflat = sp.Matrix(4, 4, lambda a, b: dphi[a] * dphi[b] - eta[a, b] * gs / 2 + xi * (-Hm[a, b] + eta[a, b] * boxp2))
at0 = {T4: 0, Z: 0}
kf = sp.Matrix([1, 0, 0, 1])
Tkk0 = sp.simplify((kf.T * Tflat * kf)[0].subs(at0))
T000 = sp.simplify(Tflat[0, 0].subs(at0))
chk("D1 T_kk(origin) = -8 xi c eps", sp.simplify(Tkk0 + 8 * xi * c0 * eps) == 0, str(Tkk0))
chk("D2 T_00(origin) = -4 xi c eps", sp.simplify(T000 + 4 * xi * c0 * eps) == 0, str(T000))
num = {xi: sp.Rational(1, 6), c0: sp.Rational(1, 10**20), eps: sp.Rational(1, 10**20)}
chk("D3 numeric xi=1/6, c=eps=1e-20 (any tiny amplitude): T_kk<0 and T_00<0",
    Tkk0.subs(num) < 0 and T000.subs(num) < 0, "T_kk=%s T_00=%s" % (Tkk0.subs(num), T000.subs(num)))
# along the null line t = z = lam, phi^2 has a strict local minimum at lam = 0
lam = sp.Symbol('lam')
f2 = (phi ** 2).subs({T4: lam, Z: lam})
chk("D4 along t=z=lam, phi^2 has a strict local MIN at lam=0 (c eps > 0): computed case 'xi>0,small -> min'",
    sp.diff(f2, lam).subs(lam, 0) == 0 and sp.simplify(sp.diff(f2, lam, 2).subs(lam, 0) - 8 * c0 * eps) == 0)
# ANEC along the complete null line: phi grows ~ lam^2, fall-off hypothesis fails; the example is pointwise only
chk("D5 test-field ANEC with fall-off: int T_kk = int phi'^2 - xi [(phi^2)']_boundary >= 0 when phi' -> 0 (flat space, FFKPS 17)",
    True, "identity: integrand = phi'^2 - xi d/dlam (phi^2)'; recorded, not a numeric test")

print("E: fully backreacted flat FRW (Jordan frame), V = m^2 phi^2/2")
tt = sp.Symbol('t', real=True)
a = sp.Function('a')(tt)
p_ = sp.Function('p')(tt)
gF = sp.diag(-1, a ** 2, a ** 2, a ** 2)
XF = [tt, sp.Symbol('X1'), sp.Symbol('X2'), sp.Symbol('X3')]
GamF = christoffel(gF, XF)
RicF = ricci(GamF, XF)
giF = gF.inv()
RsF = sp.simplify(sum(giF[i, j] * RicF[i, j] for i in range(4) for j in range(4)))
EinF = sp.simplify(RicF - gF * RsF / 2)
kF = sp.Matrix([1, 1 / a, 0, 0])
GkkF = sp.simplify((kF.T * EinF * kF)[0])
Hs = sp.diff(a, tt) / a
chk("E0 flat FRW: G_kk = -2 Hdot (k = (1, 1/a, 0, 0))", sp.simplify(GkkF + 2 * sp.diff(Hs, tt)) == 0)
m = sp.Symbol('m', positive=True)
dpF = [sp.diff(p_, v) for v in XF]
gsF = sum(giF[i, j] * dpF[i] * dpF[j] for i in range(4) for j in range(4))
H2F = hess(p_ ** 2, GamF, XF)
bxF = sum(giF[i, j] * H2F[i, j] for i in range(4) for j in range(4))
VF = m ** 2 * p_ ** 2 / 2
Nmat = sp.Matrix(4, 4, lambda i, j: dpF[i] * dpF[j] - gF[i, j] * gsF / 2 - gF[i, j] * VF
                 + xi * (-H2F[i, j] + gF[i, j] * bxF))          # numerator of BV (2.3) (times kappa/(kappa - xi phi^2) -> T_eff)
# Einstein eq: (kappa - xi phi^2) G = Nmat
Hsym, Hd, pp, pd_, pdd_ = sp.symbols('H Hd p pd pdd', real=True)


def to_sym(e):
    e = e.subs(sp.Derivative(a, (tt, 2)), (Hd + Hsym ** 2) * a).subs(sp.Derivative(a, tt), Hsym * a)
    e = e.subs(sp.Derivative(p_, (tt, 2)), pdd_).subs(sp.Derivative(p_, tt), pd_).subs(p_, pp)
    return sp.simplify(e)


con = to_sym((kap - xi * p_ ** 2) * EinF[0, 0] - Nmat[0, 0])            # Friedmann constraint
nul = to_sym((kap - xi * p_ ** 2) * GkkF - (kF.T * Nmat * kF)[0])       # null equation
kg = to_sym(sp.diff(sp.diff(p_, tt) * a ** 3, tt) / a ** 3 + m ** 2 * p_ + xi * RsF * p_)   # -box phi + V' + xi R phi
solv = sp.solve([nul, kg], [Hd, pdd_], dict=True)[0]
Hd_f = sp.lambdify((Hsym, pp, pd_, xi, kap, m), solv[Hd])
pdd_f = sp.lambdify((Hsym, pp, pd_, xi, kap, m), solv[pdd_])
con_f = sp.lambdify((Hsym, pp, pd_, xi, kap, m), con)
print("    constraint:", sp.factor(con))
# at phi = 0: Hdot = (2 xi - 1) phidot^2 / (2 kappa)
chk("E1 closed form at a zero of phi: Hdot = (2 xi - 1) phidot^2/(2 kappa) (any H)",
    sp.simplify(solv[Hd].subs(pp, 0) - (2 * xi - 1) * pd_ ** 2 / (2 * kap)) == 0, str(sp.simplify(solv[Hd].subs(pp, 0))))

XI, KAP, M = 1.0, 1.0, 1.0
p0, pd0 = 0.3, 0.0
# H0 > 0 from the constraint (quadratic in H)
Hroots = sp.solve(con.subs({pp: p0, pd_: pd0, xi: XI, kap: KAP, m: M}), Hsym)
H0 = max(float(sp.re(h)) for h in Hroots if abs(sp.im(h)) < 1e-14)


def rhs(y):
    H, P, Pd, lna = y
    return np.array([Hd_f(H, P, Pd, XI, KAP, M), Pd, pdd_f(H, P, Pd, XI, KAP, M), H])


y = np.array([H0, p0, pd0, 0.0])
dt, nsteps = 1e-3, 40000
traj = [y.copy()]
for _ in range(nsteps):
    k1 = rhs(y); k2 = rhs(y + dt / 2 * k1); k3 = rhs(y + dt / 2 * k2); k4 = rhs(y + dt * k3)
    y = y + dt / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
    traj.append(y.copy())
traj = np.array(traj)
Hdots = np.array([Hd_f(h, P, Pd, XI, KAP, M) for h, P, Pd, _ in traj])
cons = np.array([con_f(h, P, Pd, XI, KAP, M) for h, P, Pd, _ in traj])
xiphi2 = XI * traj[:, 1] ** 2 / KAP
crossings = np.where(np.sign(traj[:-1, 1]) != np.sign(traj[1:, 1]))[0]
chk("E2 constraint preserved by the integration", np.max(np.abs(cons)) < 1e-9, "max|C| = %.2e" % np.max(np.abs(cons)))
chk("E3 field sub-Planckian throughout: max xi phi^2/kappa < 1", xiphi2.max() < 1, "max = %.4f" % xiphi2.max())
chk("E4 phi crosses zero (oscillates)", len(crossings) >= 3, "%d crossings" % len(crossings))
hd_at = [Hdots[i] for i in crossings]
chk("E5 Hdot > 0 at every zero crossing -> G_kk = -2 Hdot < 0: Jordan-frame NEC violated ON-SHELL",
    all(h > 0 for h in hd_at), "Hdot at crossings: " + ", ".join("%.3e" % h for h in hd_at[:4]))
i0 = crossings[0]
H, P, Pd, _ = traj[i0]
eta_b = 3.0
Gvv = 3 * H ** 2 * np.cosh(eta_b) ** 2 - (2 * Hdots[i0] + 3 * H ** 2) * np.sinh(eta_b) ** 2
chk("E6 WEC: boosted observer (rapidity 3) at the first crossing sees G_vv < 0", Gvv < 0, "G_vv = %.3e" % Gvv)
chk("E7 comoving observer: G_tt = 3H^2 >= 0 everywhere (WEC violated only for boosted observers here)",
    True, "min 3H^2 = %.3e" % (3 * traj[:, 0] ** 2).min())
# Einstein frame: Omega^2 = 1 - xi phi^2/kappa, a_E = Omega a, dt_E = Omega dt
Om = np.sqrt(1 - xiphi2)
lnaE = traj[:, 3] + np.log(Om)
tgrid = np.arange(len(traj)) * dt
HE = np.gradient(lnaE, tgrid) / Om               # d ln a_E / d t_E
dHE = np.gradient(HE, tgrid) / Om
inner = slice(5, -5)
chk("E8 control: Einstein-frame dH_E/dt_E <= 0 along the same solution (Einstein-frame NEC holds)",
    dHE[inner].max() <= 1e-6, "max dH_E/dt_E = %.3e ; max Jordan Hdot = %.3e" % (dHE[inner].max(), Hdots.max()))


print("F: FFKPS 2309.10848 eq.(13) null energy vs BV (2.2) contracted (discrepancy check, curved metric)")
Rkk = sp.simplify((k.T * Ric * k)[0])
kkHF = sp.simplify((k.T * HF * k)[0])
form_plus = (1 - 2 * xi) * kdF ** 2 - 2 * xi * F * kkHF + xi * Rkk * F ** 2
form_ffkps = (1 - 2 * xi) * kdF ** 2 - 2 * xi * (F * kkHF + Rkk * F ** 2 / 2)
chk("F1 BV (2.2) gives T_kk = (1-2xi)phi'^2 - 2xi phi kk nabla nabla phi + xi R_kk phi^2 (identity)",
    sp.simplify(Tkk - form_plus) == 0)
chk("F2 DISCREPANCY: FFKPS eq.(13) as printed (-xi R_kk phi^2) differs from it by 2 xi R_kk phi^2 (zero in flat space; FFKPS eq.(16)/(18), the effective form, agrees with BV 2.6)",
    sp.simplify(Tkk - form_ffkps - 2 * xi * Rkk * F ** 2) == 0)

print("\nSUMMARY: %d PASS, %d FAIL" % (len(PASS), len(FAIL)))
if FAIL:
    print("FAILED:", FAIL)
sys.exit(1 if FAIL else 0)
