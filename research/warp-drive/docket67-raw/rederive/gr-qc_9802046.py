#!/usr/bin/env python3
"""
DOCKET 67 -- re-derivation of Hochberg & Visser gr-qc/9802046 (PRD 58, 044021),
the parts the warp board uses: Sec. 4.2 (static coalescence), Sec. 5 eq. (49)-(50)
(throat NEC constraint), Sec. 6.1 eqs. (72)-(77),(83) (conformally-expanding
Morris-Thorne example), Sec. 6.2 eqs. (86)-(90) (Vaidya-type example), and the
Sec. 7 non-implication "if the wormhole is dynamic, flare-out in the spatial
direction does not imply flare-out in the null directions orthogonal to the throat",
for which an explicit counterexample is constructed and checked.

Everything is computed from the metric with a hand-rolled Christoffel/Einstein
routine: expansions theta = gamma^{ab} nabla_a l_b with gamma^{ab} = g^{ab} +
l+^a l-^b + l-^a l+^b (HV eq. 16), not from HV's printed formulas.

Run:  python3 gr-qc_9802046.py      (sympy; exits 1 on any failed check)
"""
import sys
import sympy as sp

FAIL = []


def chk(name, cond, detail=""):
    ok = bool(cond)
    print(("PASS " if ok else "FAIL ") + name + (("   " + detail) if detail else ""))
    if not ok:
        FAIL.append(name)


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


def ricci(g, X, G):
    n = len(X)
    R = sp.zeros(n, n)
    for b in range(n):
        for c in range(n):
            R[b, c] = sp.simplify(sum(sp.diff(G[a][b][c], X[a]) for a in range(n))
                                  - sum(sp.diff(G[a][b][a], X[c]) for a in range(n))
                                  + sum(G[a][a][d] * G[d][b][c] for a in range(n) for d in range(n))
                                  - sum(G[a][c][d] * G[d][b][a] for a in range(n) for d in range(n)))
    return R


def einstein(g, X):
    G = christoffel(g, X)
    R = ricci(g, X, G)
    Rs = sp.simplify(sum(g.inv()[a, b] * R[a, b] for a in range(4) for b in range(4)))
    return G, R, sp.simplify(R - Rs * g / 2)


def expansion(g, X, G, lp, lm, which):
    """theta = gamma^{ab} nabla_a l_b for l = lp (which=+) or lm (which=-)."""
    gi = g.inv()
    l = lp if which > 0 else lm
    ld = [sum(g[a, b] * l[b] for b in range(4)) for a in range(4)]  # lower index
    gam = sp.Matrix(4, 4, lambda a, b: gi[a, b] + lp[a] * lm[b] + lm[a] * lp[b])
    nab = sp.Matrix(4, 4, lambda a, b: sp.diff(ld[b], X[a]) - sum(G[c][a][b] * ld[c] for c in range(4)))
    return sp.simplify(sum(gam[a, b] * nab[a, b] for a in range(4) for b in range(4)))


def dalong(l, X, f):
    return sp.simplify(sum(l[a] * sp.diff(f, X[a]) for a in range(4)))


t, th, ph = sp.symbols('t theta phi', real=True)
r = sp.symbols('r', positive=True)
X = [t, r, th, ph]

# ---------------------------------------------------------------- Sec. 6.1
print("== Sec. 6.1: ds^2 = Omega(t)^2 [ -dt^2 + dr^2/(1-b/r) + r^2 dOmega^2 ]  (HV eq. 69)")
Om = sp.Function('Omega', positive=True)(t)
b = sp.Function('b')(r)
g = sp.diag(-Om**2, Om**2 / (1 - b / r), Om**2 * r**2, Om**2 * r**2 * sp.sin(th)**2)
Gc, Ric, Ein = einstein(g, X)
s = sp.sqrt(1 - b / r)
lp = [1 / (sp.sqrt(2) * Om), s / (sp.sqrt(2) * Om), 0, 0]      # HV eq. (71), patch 1
lm = [1 / (sp.sqrt(2) * Om), -s / (sp.sqrt(2) * Om), 0, 0]
# normalisation (HV eq. 15)
dot = lambda u, v: sp.simplify(sum(g[a, c] * u[a] * v[c] for a in range(4) for c in range(4)))
chk("eq15 l+.l+ = 0, l-.l- = 0, l+.l- = -1", dot(lp, lp) == 0 and dot(lm, lm) == 0 and sp.simplify(dot(lp, lm) + 1) == 0)
Od = sp.diff(Om, t); Odd = sp.diff(Om, t, 2); bp = sp.diff(b, r)
thp = expansion(g, X, Gc, lp, lm, +1); thm = expansion(g, X, Gc, lp, lm, -1)
hv72 = lambda sg: sp.sqrt(2) * Od / Om**2 + sg * sp.sqrt(2) / (r * Om) * s
chk("eq72 theta_+ (computed from metric) = HV", sp.simplify(thp - hv72(+1)) == 0)
chk("eq72 theta_- (computed from metric) = HV", sp.simplify(thm - hv72(-1)) == 0)
dthp = dalong(lp, X, thp); dthm = dalong(lm, X, thm)
hv73 = lambda sg: (1 / Om**2) * ((Odd / Om - 2 * Od**2 / Om**2) - sg * Od / (r * Om) * s
                                  - (1 / r**2) * (1 - b / r) + (1 / (2 * r**2)) * (-bp + b / r))
chk("eq73 d theta_+/du_+ = HV", sp.simplify(dthp - hv73(+1)) == 0)
chk("eq73 d theta_-/du_- = HV", sp.simplify(dthm - hv73(-1)) == 0)
# affine check: non-affinity kappa l = l.nabla l ; only kappa*theta enters, zero at theta=0
# eq. (75): on theta_+ = 0 (collapsing branch, H = Omdot/Om = -Hn < 0): (1/r) s = Hn
Hn, OMs, ODDs, Bs, BPs = sp.symbols('Hn OMs ODDs Bs BPs', positive=True)
plain = lambda e: e.subs(Odd, ODDs).subs(Od, -Hn * OMs).subs(bp, BPs).subs(b, Bs).subs(Om, OMs)
expr = plain(hv73(+1)).subs(Bs, r * (1 - Hn**2 * r**2))
chk("theta_+ = 0 on b = r(1 - H^2 r^2) (the throat condition, eq. 74)",
    sp.simplify(plain(hv72(+1)).subs(Bs, r * (1 - Hn**2 * r**2))) == 0)
hv75 = (1 / OMs**2) * ((ODDs / OMs - 2 * Hn**2) + (1 / (2 * r**2)) * (-BPs + (1 - Hn**2 * r**2)))
chk("eq75 flare-out on theta=0 = HV (s eliminated)", sp.simplify(expr - hv75) == 0)
# eq. (76): orthonormal G_tt + G_rr
Gtt_hat = Ein[0, 0] / Om**2
Grr_hat = Ein[1, 1] * (1 - b / r) / Om**2
hv76 = Om**-2 * (-b / r**3 + bp / r**2 - 2 * Odd / Om + 4 * Od**2 / Om**2)
chk("eq76 G_tt^ + G_rr^ = HV", sp.simplify(Gtt_hat + Grr_hat - hv76) == 0)
# eq. (77): on the throat, dtheta/du = -(1/2)(G_tt^ + G_rr^) = -4 pi (rho - tau)
rel = sp.simplify((plain(hv73(+1)) + plain(hv76) / 2).subs(Bs, r * (1 - Hn**2 * r**2)))
chk("eq77 on theta=0: dtheta/du = -(G_tt^+G_rr^)/2 = -4pi(rho-tau)  [so rho-tau>=0 <=> dtheta/du<=0]", rel == 0)
# Raychaudhuri at theta = 0, sigma = 0: dtheta/du = -R_ab l^a l^b (general, before Einstein eq.)
Rll = sp.simplify(sum(Ric[a, c] * lp[a] * lp[c] for a in range(4) for c in range(4)))
ray = sp.simplify((dthp + Rll + thp**2 / 2))  # kappa term: check affinity separately
# affinity of l+: (l.nabla l)^a = kappa l^a
acc = [sp.simplify(sum(lp[c] * (sp.diff(lp[a], X[c]) + sum(Gc[a][c][d] * lp[d] for d in range(4))) for c in range(4))) for a in range(4)]
kap = sp.simplify(acc[0] / lp[0])
chk("l+ is pregeodesic: (l.nabla l) = kappa l", all(sp.simplify(acc[a] - kap * lp[a]) == 0 for a in range(4)), "kappa = %s" % kap)
chk("Raychaudhuri (sigma=omega=0): dtheta/du + theta^2/2 - kappa theta = -R_ab l^a l^b",
    sp.simplify(dthp + thp**2 / 2 - kap * thp + Rll) == 0)

# static limit (Omega const): theta_+ = theta_- = 0 at b(r0)=r0 simultaneously; eq. (83)
r0 = sp.symbols('r0', positive=True)
st = lambda e: sp.simplify(e.subs(Odd, 0).subs(Od, 0).subs(Om, 1))
chk("Sec 4.2/6.1.3 static: theta_+ = -theta_- (zero at the same sphere b(r0)=r0)", sp.simplify(st(thp) + st(thm)) == 0)
flare_static = sp.simplify(plain(st(dthp)).subs(Bs, r0).subs(r, r0))
print("     static flare-out at r0 (b(r0)=r0, b'(r0)=BPs):", flare_static)
chk("eq83 static flare-out sign = sign(1 - b'(r0))", sp.simplify(flare_static - (1 - BPs) / (2 * r0**2)) == 0,
    "computed (1-b')/(2 r0^2); HV text layer prints (1/r0^2)(1-b') -- factor 2 DISCREPANCY, sign agrees")

# ---------------------------------------------------------------- Sec. 7 counterexample
print("== Sec. 7 non-implication: explicit counterexample in the Sec. 6.1 family")
# b = r0^2/r (Ellis/MT). Spatial slice t=const: Omega(t)^2 x (static MT slice) -> embedding
# flares out at r0 exactly as static MT (b'(r0) = -1 < 1). Choose Omega = exp(h t - k t^2/2).
h, k = sp.Rational(1, 4), sp.Integer(5)
R0 = sp.Integer(1)
Omx = sp.exp(h * t - k * t**2 / 2)
bx = R0**2 / r
subsx = lambda e: e.subs(b, bx).doit().subs(Om, Omx).doit()
# spatial flare-out of slice t=0: area radius A(r) = Omega r; proper radial ds = Omega dr/sqrt(1-b/r)
# dA/ds = sqrt(1-b/r) -> 0 at r0; d^2A/ds^2 = (1/Omega) d/dr sqrt(1-b/r) * sqrt(1-b/r) = (b/r - b')/(2 r Omega) > 0
d2A = sp.simplify(((bx / r - sp.diff(bx, r)) / (2 * r * Omx)).subs(t, 0).subs(r, R0))
chk("slice t=0: spatial flare-out at r0 (d^2 A/ds^2 > 0, i.e. b'(r0) = -1 < 1)", d2A > 0, "d2A/ds2 = %s" % d2A)
# the spatial throat r0 is NOT null-extremal: theta_+- = sqrt2 Omdot/Om^2 != 0
th_r0 = sp.simplify(subsx(thp).subs(t, 0).subs(r, R0))
chk("spatial throat r0 at t=0 is not a null-extremal surface (theta_+ != 0)", th_r0 != 0, "theta_+(r0) = %s" % th_r0)
# patch 1 expanding (h>0): only theta_- can vanish; locate r*: (1/r) sqrt(1 - r0^2/r^2) = h
# eq. (74) on patch 1 has, for this b, TWO roots in r when 0 < h < 1/(2 r0): HV's "only one
# extremal hypersurface in the first patch" holds as "only one of theta_+-", not as one sphere.
f74 = lambda x: (1 / x) * sp.sqrt(1 - 1 / x**2) - h
roots = [sp.nsolve(f74(r), r, (1.0000001, 1.41421356), solver='bisect'),
         sp.nsolve(f74(r), r, (1.41421357, 50), solver='bisect')]
chk("eq74 has two roots for b = r0^2/r, h = 1/4 (discrepancy with 'only one extremal hypersurface' read literally)",
    len(set(round(float(x), 8) for x in roots)) == 2, "r* = %s" % [round(float(x), 10) for x in roots])
for rs in roots:
    th_m_rs = sp.N(subsx(thm).subs(t, 0).subs(r, rs))
    flm = sp.N(subsx(dthm).subs(t, 0).subs(r, rs))
    chk("theta_-(r*) = 0 at r* = %.8f" % rs, abs(th_m_rs) < 1e-12)
    chk("null flare-out FAILS at r* = %.8f: d theta_-/du_- < 0" % rs, flm < 0, "d theta_-/du_- = %.10f" % flm)
    cf = sp.N(-k - h**2 + 1 / rs**4)
    chk("matches HV eq. (75): -k - h^2 + r0^2/r*^4 (Omega(0)=1)", abs(cf - flm) < 1e-10, "%.10f" % cf)
    nec = sp.N(subsx(hv76).subs(t, 0).subs(r, rs))
    chk("NEC holds at r* (8pi(rho-tau) >= 0), consistent with eq. (77)", nec > 0, "8pi(rho-tau) = %.10f" % nec)
# control: k = 0 (Omega = e^{h t}, no deceleration) -> inner root IS null-flared (the example is not rigged)
flm0 = sp.N((-h**2 + 1 / roots[0]**4))
chk("control k=0: inner r* is null-flared (dtheta/du > 0), so the failure above is caused by Omega-ddot",
    flm0 > 0, "%.10f" % flm0)
# second patch: same by symmetry (HV 6.1.2) -- theta_+ vanishes there; flare-out expression identical

# ---------------------------------------------------------------- Sec. 6.2
print("== Sec. 6.2: ds^2 = -e^{2psi}(1-2m/r) dv^2 + 2 e^psi dv dr + r^2 dOmega^2  (HV eq. 84)")
v = sp.symbols('v', real=True)
Y = [v, r, th, ph]
psi = sp.Function('psi')(v, r)
m = sp.Function('m')(v, r)
g2 = sp.Matrix([[-sp.exp(2 * psi) * (1 - 2 * m / r), sp.exp(psi), 0, 0],
                [sp.exp(psi), 0, 0, 0], [0, 0, r**2, 0], [0, 0, 0, r**2 * sp.sin(th)**2]])
G2, R2, E2 = einstein(g2, Y)
lp2 = [1, sp.exp(psi) * (1 - 2 * m / r) / 2, 0, 0]          # HV eq. (85)
lm2 = [0, -sp.exp(-psi), 0, 0]
dot2 = lambda u, w: sp.simplify(sum(g2[a, c] * u[a] * w[c] for a in range(4) for c in range(4)))
chk("eq85 normalisation (15)", dot2(lp2, lp2) == 0 and dot2(lm2, lm2) == 0 and sp.simplify(dot2(lp2, lm2) + 1) == 0)
tp2 = expansion(g2, Y, G2, lp2, lm2, +1); tm2 = expansion(g2, Y, G2, lp2, lm2, -1)
print("     theta_+ computed:", tp2, "   theta_- computed:", tm2)
chk("eq87 theta_- = -(2/r) e^{-psi}", sp.simplify(tm2 + 2 * sp.exp(-psi) / r) == 0)
chk("eq86 as printed in text layer, theta_+ = (1/2) e^psi (1-2m/r)",
    sp.simplify(tp2 - sp.exp(psi) * (1 - 2 * m / r) / 2) == 0,
    "EXPECTED FAIL if misprint; computed e^psi(1-2m/r)/r")
FAIL[:] = [f for f in FAIL if not f.startswith("eq86 as printed")]
chk("eq86 corrected: theta_+ = e^psi (1-2m/r)/r  (zero iff 2m = r, as HV state)",
    sp.simplify(tp2 - sp.exp(psi) * (1 - 2 * m / r) / r) == 0)
d2 = dalong(lp2, Y, tp2)
Mv = sp.symbols('M_v', real=True)
d2t = sp.simplify(d2.subs(m, r / 2 + 0 * m).doit()) if False else None
# evaluate on 2m = r: substitute m -> r/2 after differentiation
mv = sp.Derivative(m, v); mr = sp.Derivative(m, r)
d2s = sp.simplify(d2.subs({sp.Derivative(m, v): Mv}).subs(m, r / 2))
chk("eq88 dtheta_+/du_+ on 2m=r = -(2/r^2) e^psi dm/dv", sp.simplify(d2s + 2 / r**2 * sp.exp(psi) * Mv) == 0)
Tvv = sp.simplify(E2[0, 0] / (8 * sp.pi))
Tvv_s = sp.simplify(Tvv.subs({sp.Derivative(m, v): Mv}).subs(m, r / 2))
print("     T_vv on 2m=r computed:", Tvv_s)
chk("eq89 as printed, dm/dv = 4 pi r^2 T_vv", sp.simplify(Mv - 4 * sp.pi * r**2 * Tvv_s) == 0,
    "EXPECTED FAIL unless psi=0: computed dm/dv = 4 pi r^2 e^{-psi} T_vv")
FAIL[:] = [f for f in FAIL if not f.startswith("eq89 as printed")]
chk("eq89 corrected: dm/dv = 4 pi r^2 e^{-psi} T_vv (e^{-psi} > 0, so the sign equivalence (90) is untouched)",
    sp.simplify(Mv - 4 * sp.pi * r**2 * sp.exp(-psi) * Tvv_s) == 0)
chk("eq90 hence dtheta_+/du_+ >= 0 <=> T_vv <= 0 (l+ = d/dv on 2m=r)", sp.simplify(lp2[1].subs(m, r / 2)) == 0)

# ---------------------------------------------------------------- Sec. 4.2 eq. (47) normalisation
print("== Sec. 4.2 eq. (47): l-+ = c (V +- n) must satisfy l+.l- = -1 (eq. 15)")
c = sp.symbols('c', positive=True)
eta = sp.diag(-1, 1)            # V, n orthonormal (V timelike, n spacelike)
Vv = sp.Matrix([1, 0]); nv = sp.Matrix([0, 1])
lpv = c * (Vv - nv); lmv = c * (Vv + nv)
ip = sp.simplify((lpv.T * eta * lmv)[0])
chk("eq47 with c = 1/2 (as printed in the text layer) gives l+.l- = -1/2, not -1", ip.subs(c, sp.Rational(1, 2)) == sp.Rational(-1, 2),
    "DISCREPANCY (normalisation only; coalescence argument (48) is sign/ratio-only and unaffected)")
chk("eq47 requires c = 1/sqrt(2)", sp.solve(sp.Eq(ip, -1), c) == [1 / sp.sqrt(2)])

# ---------------------------------------------------------------- later literature check
print("== Maeda-Harada-Carr 0901.1153 eq. (4.53): ds^2 = -dt^2 + a(t)^2 [dx^2 + (x^2+b^2) dOmega^2], a = t/t0")
x = sp.symbols('x', real=True); B = sp.symbols('B', positive=True); t0 = sp.symbols('t0', positive=True)
Z = [t, x, th, ph]
a = t / t0
g3 = sp.diag(-1, a**2, a**2 * (x**2 + B**2), a**2 * (x**2 + B**2) * sp.sin(th)**2)
G3, R3, E3 = einstein(g3, Z)
mu = sp.simplify(E3[0, 0] / (8 * sp.pi))                 # rho = T_tt (u = d/dt)
pr = sp.simplify(E3[1, 1] / a**2 / (8 * sp.pi))
pt = sp.simplify(E3[2, 2] / (a**2 * (x**2 + B**2)) / (8 * sp.pi))
chk("MHC (4.58) 8pi mu = 3/t^2 - t0^2 B^2/(t^2 (x^2+B^2)^2)", sp.simplify(8 * sp.pi * mu - (3 / t**2 - t0**2 * B**2 / (t**2 * (x**2 + B**2)**2))) == 0)
chk("MHC (4.59) 8pi p_r = -1/t^2 - t0^2 B^2/(t^2 (x^2+B^2)^2)", sp.simplify(8 * sp.pi * pr - (-1 / t**2 - t0**2 * B**2 / (t**2 * (x**2 + B**2)**2))) == 0)
# radial NEC: mu + p_r >= 0  <=>  2/t^2 - 2 t0^2 B^2/(t^2 (x^2+B^2)^2) >= 0, worst at x = 0: t0 <= B
nec_r = sp.simplify((8 * sp.pi * (mu + pr)).subs(x, 0))
chk("radial NEC at the spatial throat x=0: 8pi(mu+p_r) = 2(1 - t0^2/B^2)/t^2 >= 0 iff t0 <= B",
    sp.simplify(nec_r - 2 * (1 - t0**2 / B**2) / t**2) == 0)
# the x=0 sphere is a minimal sphere of the t=const slice (spatial flare-out) ...
Rarea = a * sp.sqrt(x**2 + B**2)
chk("x=0 is a spatial minimal sphere on t=const (dR/dx = 0, d2R/dx2 > 0)",
    sp.diff(Rarea, x).subs(x, 0) == 0 and bool(sp.simplify(sp.diff(Rarea, x, 2).subs(x, 0)).subs(t, sp.Symbol('tp', positive=True)).is_positive))
# ... but it is trapped (theta+ theta- > 0), so NOT a HV null throat, for t0 < 2B
thpl = sp.simplify((sp.diff(Rarea, t) + sp.diff(Rarea, x) / a) / Rarea * 2 / sp.sqrt(2))
thmi = sp.simplify((sp.diff(Rarea, t) - sp.diff(Rarea, x) / a) / Rarea * 2 / sp.sqrt(2))
chk("MHC: x=0 sphere is trapped (theta+ = theta- = sqrt2/t > 0): spatial flare-out, no null flare-out, NEC/DEC can hold",
    sp.simplify(thpl.subs(x, 0) - thmi.subs(x, 0)) == 0 and sp.simplify(thpl.subs(x, 0)) == sp.sqrt(2) / t)

print()
print("FAILED:", FAIL if FAIL else "none")
sys.exit(1 if FAIL else 0)
