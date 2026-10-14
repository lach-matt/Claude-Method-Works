#!/usr/bin/env python3
"""DOCKET 67 -- re-derivation for key 'frw-open-contraction'.

The tree's claims (driven.py:216-217, 243-247, 308-310, 515-516; drivensource.py:68-71,
carried from nonstatic.py:91-107, 446-468):
  (a) in FRW the contraction criterion Gamma = e^{-Lambda} R' > 1 is exactly k < 0
      (open contracts, flat is marginal Gamma = 1);
  (b) open FRW has rho > 0, m > 0, j = 0 and 'the NEC contraction equals rho', strictly > 0.

External inputs checked (read at source):
  Enqvist 0709.2044 eq.(2.2),(2.9): FRW = LTB with A = a r, k(r) = k r^2, g_rr = A'^2/(1-k(r)).
  Escriva 2504.05813 eq.(2.3)-(2.5): Gamma = R'/B, Gamma^2 = 1 + U^2 - 2M/R, comoving gauge;
      eq.(3.3) M_b = 4 pi rho_b R^3/3 for the FLRW background.
  Hayward gr-qc/9408002 eq.(4),(27),(32a),(33): E invariant, 1-2E/r = e^-lambda r'^2 - rdot^2.
  Jai-akson & Yokokura 2601.03077 eq.(8),(46),(50): M foliation-invariant; on radial (Kodama)
      slices theta_(u) = 0, i.e. U = 0.

Checks C1..C8.  Stdlib + sympy + z3.  Exit 0 iff every check passes.
"""
import sys
import sympy as sp

OK = True


def chk(name, cond):
    global OK
    OK &= bool(cond)
    print("  %-78s %s" % (name, "ok" if cond else "FAIL"))


t, chi, th, ph = sp.symbols("t chi theta phi", positive=True)
a = sp.Function("a", positive=True)(t)
ad, add = sp.diff(a, t), sp.diff(a, t, 2)
Lam = sp.Symbol("Lambda_c", real=True)


def einstein(g, x):
    n = 4
    gi = g.inv()
    Gm = [[[sp.simplify(sum(gi[i, d] * (sp.diff(g[d, j], x[k]) + sp.diff(g[d, k], x[j])
                                         - sp.diff(g[j, k], x[d])) for d in range(n)) / 2)
            for k in range(n)] for j in range(n)] for i in range(n)]
    Ric = sp.zeros(n, n)
    for b in range(n):
        for c in range(n):
            s = 0
            for i in range(n):
                s += sp.diff(Gm[i][b][c], x[i]) - sp.diff(Gm[i][b][i], x[c])
                for d in range(n):
                    s += Gm[i][i][d] * Gm[d][b][c] - Gm[i][c][d] * Gm[d][b][i]
            Ric[b, c] = sp.simplify(s)
    Rs = sp.simplify(sum(gi[i, j] * Ric[i, j] for i in range(n) for j in range(n)))
    return sp.simplify(Ric - Rs * g / 2), gi


def frw(k):
    f = {-1: sp.sinh(chi), 0: chi, 1: sp.sin(chi)}[k]
    x = [t, chi, th, ph]
    g = sp.diag(-1, a**2, a**2 * f**2, a**2 * f**2 * sp.sin(th)**2)
    G, gi = einstein(g, x)
    T = G / (8 * sp.pi)
    R = a * f
    rho = sp.simplify(T[0, 0])                    # u = d/dt, comoving
    j = sp.simplify(-T[0, 1] / a)                 # flux in the orthonormal frame
    p_r = sp.simplify(T[1, 1] / a**2)
    p_T = sp.simplify(T[2, 2] / R**2)
    W = sp.simplify(sp.diff(R, chi) / a)          # e^{-Lambda} R'
    U = sp.simplify(sp.diff(R, t))                # e^{-Phi} Rdot, Phi = 0
    m = sp.simplify(R / 2 * (1 - W**2 + U**2))
    return dict(f=f, R=R, rho=rho, j=j, p_r=p_r, p_T=p_T, W=W, U=U, m=m)


print("C1. FRW in comoving (cosmic-time) slicing, general a(t): Gamma = f_k'(chi)")
F = {k: frw(k) for k in (-1, 0, 1)}
chk("k = -1: Gamma = cosh(chi)", sp.simplify(F[-1]["W"] - sp.cosh(chi)) == 0)
chk("k =  0: Gamma = 1 exactly", sp.simplify(F[0]["W"] - 1) == 0)
chk("k = +1: Gamma = cos(chi)", sp.simplify(F[1]["W"] - sp.cos(chi)) == 0)
for k in (-1, 0, 1):
    chk("k = %+d: Gamma^2 - 1 = -k f_k(chi)^2  (LTB 2E = -k r^2, Enqvist k(r) = k r^2)" % k,
        sp.simplify(F[k]["W"]**2 - 1 + k * F[k]["f"]**2) == 0)
chk("isotropy: p_r = p_T for every k (perfect fluid, any a(t))",
    all(sp.simplify(F[k]["p_r"] - F[k]["p_T"]) == 0 for k in (-1, 0, 1)))
chk("j = 0 for every k (comoving slicing, no radial flux)",
    all(sp.simplify(F[k]["j"]) == 0 for k in (-1, 0, 1)))

print("\nC2. Misner-Sharp mass m = (4 pi/3) rho R^3 and rho = 3(adot^2 + k)/(8 pi a^2)")
for k in (-1, 0, 1):
    chk("k = %+d: rho = 3(adot^2 + k)/(8 pi a^2)" % k,
        sp.simplify(F[k]["rho"] - 3 * (ad**2 + k) / (8 * sp.pi * a**2)) == 0)
    chk("k = %+d: m = (4 pi/3) rho R^3  (Escriva eq.3.3 background, Hayward eq.33)" % k,
        sp.simplify(F[k]["m"] - sp.Rational(4, 3) * sp.pi * F[k]["rho"] * F[k]["R"]**3) == 0)
print("     so m > 0  <=>  rho > 0  <=>  adot^2 > -k;  for k = -1 that is adot^2 > 1.")
print("     rho > 0 is NOT implied by 'open FRW with general a(t)': it needs a matter law.")

print("\nC3. The NEC contraction is rho + p, and equals rho ONLY for p = 0 (dust)")
for k in (-1, 0, 1):
    nec = sp.simplify(F[k]["rho"] + F[k]["p_r"])
    chk("k = %+d: rho + p = (adot^2 + k - a addot)/(4 pi a^2)" % k,
        sp.simplify(nec - (ad**2 + k - a * add) / (4 * sp.pi * a**2)) == 0)
# open dust: adot^2 = 1 + C/a, addot = -C/(2 a^2)
C = sp.Symbol("C", positive=True)
w = sp.Symbol("w", real=True)
sub_dust = {add: -C / (2 * a**2)}
rho_d = sp.simplify(F[-1]["rho"].subs(ad**2, 1 + C / a).subs(ad, sp.sqrt(1 + C / a)))
nec_d = sp.simplify((F[-1]["rho"] + F[-1]["p_r"]).subs(sub_dust).subs(ad, sp.sqrt(1 + C / a)))
chk("open DUST: NEC contraction - rho = 0   (nonstatic.py:455-468 reproduced)",
    sp.simplify(nec_d - rho_d) == 0)
chk("open DUST: rho = 3C/(8 pi a^3) > 0", sp.simplify(rho_d - 3 * C / (8 * sp.pi * a**3)) == 0)
# open radiation (w = 1/3): the equality fails, positivity survives
print("     for p = w rho the NEC contraction is (1 + w) rho: equals rho iff w = 0;")
print("     radiation w = 1/3 gives (4/3) rho -- still > 0, but NOT 'equal to rho'.")
chk("p = w rho: (1+w) rho - rho = 0 only at w = 0",
    sp.solve(sp.Eq((1 + w) * sp.Symbol("r", positive=True) - sp.Symbol("r", positive=True), 0), w) == [0])

print("\nC4. Lambda != 0: 'the NEC contraction equals rho' fails for the tree's rho")
# the tree reads rho off the Einstein tensor (nonstatic.witness), so rho_tree = rho_M + Lambda/(8 pi)
rhoM = sp.Symbol("rho_M", positive=True)
rho_tree = rhoM + Lam / (8 * sp.pi)
p_tree = 0 - Lam / (8 * sp.pi)                     # dust + vacuum
chk("dust + Lambda: NEC contraction = rho_M (Lambda cancels)", sp.simplify(rho_tree + p_tree - rhoM) == 0)
chk("dust + Lambda: NEC - rho_tree = -Lambda/(8 pi) != 0 for Lambda != 0",
    sp.simplify(rho_tree + p_tree - rho_tree + Lam / (8 * sp.pi)) == 0)

print("\nC5. z3: in the areal-comoving chart (Enqvist 2.2/2.9) Gamma^2 = 1 - k r^2")
import z3
k_, r_, G2 = z3.Reals("k r G2")
base = [r_ > 0, G2 == 1 - k_ * r_ * r_]


def unsat(extra):
    s = z3.Solver(); s.add(*base, *extra); return s.check() == z3.unsat


def sat(extra):
    s = z3.Solver(); s.add(*base, *extra); return s.check() == z3.sat


chk("k < 0, r > 0  =>  Gamma^2 > 1      (negation unsat)", unsat([k_ < 0, z3.Not(G2 > 1)]))
chk("k = 0         =>  Gamma^2 = 1      (negation unsat)", unsat([k_ == 0, z3.Not(G2 == 1)]))
chk("k > 0, r > 0  =>  Gamma^2 < 1      (negation unsat)", unsat([k_ > 0, z3.Not(G2 < 1)]))
chk("Gamma^2 > 1   =>  k < 0            (negation unsat: criterion is exactly k<0)",
    unsat([G2 > 1, z3.Not(k_ < 0)]))
chk("vacuity guard: k < 0 with Gamma^2 > 1 is satisfiable", sat([k_ < 0, G2 > 1]))
chk("vacuity guard: k > 0 with Gamma^2 < 1 is satisfiable", sat([k_ > 0, G2 < 1]))

print("\nC6. SLICING HYPOTHESIS: the k<0 criterion is a property of comoving slicing only")
# In the normal 2-plane (U, Gamma) are the orthonormal components of dR; a change of slicing is a
# boost of rapidity eta: U' = U cosh eta - Gamma sinh eta, Gamma' = Gamma cosh eta - U sinh eta,
# with Gamma'^2 - U'^2 = 1 - 2m/R invariant (m a scalar -- Hayward eq.4, 2601.03077 eq.8).
eta = sp.Symbol("eta", real=True)
U, Wv, m_, R_ = sp.symbols("U Gamma m R", real=True)
Up = U * sp.cosh(eta) - Wv * sp.sinh(eta)
Wp = Wv * sp.cosh(eta) - U * sp.sinh(eta)
chk("Gamma'^2 - U'^2 = Gamma^2 - U^2 (boost invariance, so m is slicing-independent)",
    sp.simplify(Wp**2 - Up**2 - (Wv**2 - U**2)) == 0)
# (i) OPEN dust FRW, untrapped point: the Kodama (U' = 0) slicing gives Gamma' = sqrt(1-2m/R) < 1
Wo = F[-1]["W"]; Uo = F[-1]["U"]; mo = F[-1]["m"]; Ro = F[-1]["R"]
num = {a: 1.0, C: 1.0, chi: 0.3}
Wn = float(Wo.subs(chi, 0.3)); Un = float(Uo.subs(ad, sp.sqrt(1 + C / a)).subs(num))
etan = float(sp.atanh(Un / Wn))
Wpn = float(Wp.subs({Wv: Wn, U: Un, eta: etan})); Upn = float(Up.subs({Wv: Wn, U: Un, eta: etan}))
mn = float(mo.subs(ad, sp.sqrt(1 + C / a)).subs(num)); Rn = float(Ro.subs(num))
print("     open dust a=1, C=1, chi=0.3: comoving Gamma = %.9f, U = %.9f, 2m/R = %.9f" % (Wn, Un, 2 * mn / Rn))
print("     boost eta = atanh(U/Gamma) = %.9f  ->  U' = %.2e, Gamma' = %.9f" % (etan, Upn, Wpn))
chk("open dust, same event, U'=0 slicing: Gamma' = sqrt(1-2m/R) < 1 (NO contraction)",
    abs(Upn) < 1e-12 and abs(Wpn - (1 - 2 * mn / Rn) ** 0.5) < 1e-12 and Wpn < 1)
# (ii) FLAT dust FRW: a tilted slicing gives Gamma' > 1 (contraction), same spacetime
F0 = F[0]
Wf = 1.0; Uf = float(F0["U"].subs(ad, sp.Rational(2, 3)).subs({a: 1.0, chi: 0.3}))  # H = 2/3 at t=1
Wpf = float(Wp.subs({Wv: Wf, U: Uf, eta: -0.5}))
print("     flat dust a=1, adot=2/3, chi=0.3: comoving Gamma = 1, U = %.9f; eta = -0.5 -> Gamma' = %.9f" % (Uf, Wpf))
chk("flat FRW, tilted slicing (eta=-0.5): Gamma' > 1 (flat FRW DOES contract there)", Wpf > 1)
# z3: for any untrapped event with m > 0 there is a slicing with Gamma' <= 1
Ws, Us, M2R = z3.Reals("W U twoMoverR")
s = z3.Solver()
s.add(Ws > 0, Us * Us < Ws * Ws, M2R > 0, M2R < 1, Ws * Ws - Us * Us == 1 - M2R)
s.add(z3.Not(Ws * Ws - Us * Us < 1))
chk("z3: untrapped, m > 0  =>  the U'=0 slicing has Gamma'^2 = 1-2m/R < 1 (negation unsat)",
    s.check() == z3.unsat)
s2 = z3.Solver(); s2.add(Ws > 0, Us * Us < Ws * Ws, M2R > 0, M2R < 1, Ws * Ws - Us * Us == 1 - M2R, Ws > 1)
chk("vacuity guard: untrapped, m>0 AND comoving Gamma>1 is satisfiable (open FRW exists)",
    s2.check() == z3.sat)

print("\nC7. 'holds contraction forever' is per COMOVING SHELL; at fixed areal radius it decays")
# open dust exact solution: a = (C/2)(cosh s - 1), t = (C/2)(sinh s - s); Gamma^2 = 1 + R^2/a^2
import math
Cn, Rfix = 1.0, 1.0
prev = None; dec = True
for sv in (1.0, 2.0, 4.0, 8.0, 16.0):
    an = Cn / 2 * (math.cosh(sv) - 1)
    Gam = math.sqrt(1 + Rfix**2 / an**2)
    print("     s = %5.1f  a = %.6e  Gamma(R=1) = %.12f" % (sv, an, Gam))
    if prev is not None and not Gam < prev:
        dec = False
    prev = Gam
chk("at fixed R, comoving-slicing Gamma decreases toward 1 as a grows", dec and prev - 1 < 1e-10)
chk("per comoving shell Gamma = cosh(chi) is t-independent", sp.diff(F[-1]["W"], t) == 0)

print("\nC8. DATA (context only -- no datum is an input of the witness)")
# Planck 2018 VI (1807.06209) eq.(47b): Omega_K = 0.0007 +/- 0.0019 (TT,TE,EE+lowE+lensing+BAO)
# Omega_K = -k/(a0 H0)^2, so k < 0 <=> Omega_K > 0; comoving Gamma^2 - 1 = Omega_K (R H0/c)^2.
H0 = 67.4e3 / 3.0857e22; c = 2.99792458e8
for OK_, lab in ((0.0007, "central"), (0.0007 + 0.0019, "+1 sigma"), (0.0007 - 0.0019, "-1 sigma")):
    for R, rl in ((c / H0, "Hubble radius"), (4.017499195e16, "Proxima span")):
        g2m1 = OK_ * (R * H0 / c) ** 2
        print("     Omega_K = %+.4f (%s), R = %s: Gamma^2 - 1 = %+.3e" % (OK_, lab, rl, g2m1))
chk("the sign of Omega_K is not settled at 1 sigma (interval straddles 0)",
    0.0007 - 0.0019 < 0 < 0.0007 + 0.0019)

print("\nRESULT:", "ALL PASS" if OK else "FAILURES")
sys.exit(0 if OK else 1)
