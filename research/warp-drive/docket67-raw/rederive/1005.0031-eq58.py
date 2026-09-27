#!/usr/bin/env python3
"""DOCKET 67 audit re-derivation: Milton arXiv:1005.0031 eq. (58), A_EM = 1/(60 pi^2),
as tolman.py uses it (interior, near-wall, eps = a - r).

Parts (each prints PASS/FAIL/INFO with its number):
  A  sympy  Milton (58) read in an orthonormal frame is traceless; the TEXT-LAYER
            coordinate reading diag(2/a,0,a,a sin^2) is NOT (typography discrepancy).
  B  sympy  conservation p_r' + 2(p_r - p_t)/r = 0 fixes the eps^-2 radial stress
            from the eps^-3 tangential stress: p_r = -A/(a^2 eps^2) on BOTH sides.
  C  sympy  Saharian arXiv:0708.1187 eq. (14.21) (interior EM sphere) == tree's
            u, p_r with A = 1/(60 pi^2); cylinder (16.24) = half; Milton (130)
            Dirichlet consistency with A_D = 1/(720 pi^2).
  D  sympy+numeric  tree's derived quantities: m(r), chi, delta limit (V16),
            crossover coefficient, chi(137.8 nm), delta(l_P), eps at delta = 1.
  E  numeric  INDEPENDENT machine check of the coefficient: Saharian's exact
            renormalised mode sum (14.20) for the interior of a perfectly
            conducting sphere, evaluated by Bessel functions (scipy for nu < 40,
            Debye uniform expansion to u_3/v_3 above), validated against the
            published centre value eps(0) = -0.0381/a^4 (14.22), then the near-wall
            coefficients of eps*(a-r)^3 and p*(a-r)^2 extracted by a fit.
"""
import math, json, sys
import sympy as sp
import numpy as np
from scipy import special, integrate

res = {}
def rep(tag, ok, msg):
    print(f"[{tag}] {'PASS' if ok is True else ('FAIL' if ok is False else 'INFO')}  {msg}")
    res[tag] = {"ok": ok, "msg": msg}

# ---------------------------------------------------------------- A
A, a, e, r, th = sp.symbols('A a epsilon r theta', positive=True)
u_ext = 2*A/(a*e**3); pt_ext = A/(a*e**3); pr3 = 0
rep("A1", sp.simplify(-u_ext + pr3 + 2*pt_ext) == 0,
    "orthonormal reading of (58): -u + p_r + 2 p_t = 0 at order eps^-3 (traceless)")
g = sp.diag(-1, 1, r**2, r**2*sp.sin(th)**2)
Ttext = (A/e**3)*sp.diag(2/a, 0, a, a*sp.sin(th)**2)
trace_text = sp.simplify(sum(g[i, i]*Ttext[i, i] for i in range(4)).subs(r, a))
rep("A2", None, f"TEXT-LAYER coordinate reading diag(2/a,0,a,a sin^2 th) (contravariant) has trace "
    f"{trace_text} != 0 -> the alphaXiv text layer has lost the typography of (58) "
    f"(entries must be 1/a^3, 1/(a^3 sin^2 th) for 'properly traceless'); DISCREPANCY, not refutation")
Tfix = (A/e**3)*sp.diag(2/a, 0, 1/a**3, 1/(a**3*sp.sin(th)**2))
rep("A3", sp.simplify(sum(g[i, i]*Tfix[i, i] for i in range(4)).subs(r, a)) == 0,
    "reading with T^thth = A/(a^3 eps^3) is traceless at r = a")

# ---------------------------------------------------------------- B
# exterior: eps = r - a, p_t = +A/(a eps^3); interior: eps = a - r, p_t = -A/(a eps^3)
c = sp.Symbol('c')
res_B = {}
for side, pt_expr, eps_of_r in (("exterior", A/(a*(r - a)**3), r - a),
                                ("interior", A/(a*(r - a)**3), a - r)):
    # same odd formula A/(a (r-a)^3) on both sides (Milton (130) form); leading order
    pr = c/(r - a)**2
    cons = sp.diff(pr, r) + 2*(pr - pt_expr)/r
    # leading (r-a)^-3 coefficient at r = a
    lead = sp.limit(sp.simplify(cons*(r - a)**3), r, a)
    csol = sp.solve(sp.Eq(lead, 0), c)[0]
    res_B[side] = csol
    rep(f"B-{side}", sp.simplify(csol + A/a**2) == 0,
        f"{side}: conservation forces p_r = {csol}/eps^2 (tree: -A/(a^2 eps^2))")
u_int = sp.simplify((2*A/(a*(r - a)**3)).subs(r, a - e))
rep("B-u-int", sp.simplify(u_int + 2*A/(a*e**3)) == 0,
    f"interior u from the odd continuation: {u_int} (tree: -hbar c/(30 pi^2 a eps^3) at A=1/(60pi^2))")

# ---------------------------------------------------------------- C
AEM = 1/(60*sp.pi**2)
sah_eps = -1/(30*sp.pi**2*a*e**3); sah_p = -1/(60*sp.pi**2*a**2*e**2); sah_pperp = sah_eps/2
rep("C1", sp.simplify(u_int.subs(A, AEM) - sah_eps) == 0 and sp.simplify(-AEM/a**2/e**2 - sah_p) == 0,
    "Saharian 0708.1187 (14.21) interior eps = -1/(30pi^2 a (a-r)^3), p = -1/(60pi^2 a^2 (a-r)^2) "
    "== tree's u, p_r with A_EM = 1/(60 pi^2) EXACTLY")
rep("C2", sp.simplify(sah_eps - sah_p - 2*sah_pperp + 0) == sp.simplify(-sah_p),
    "Saharian convention T^k_i = diag(eps,-p,-pperp,-pperp): eps - p - 2 pperp = -p at eps^-3 order "
    "(i.e. traceless at eps^-3, p enters at eps^-2) -- consistent")
cyl = -1/(60*sp.pi**2*a*e**3)
rep("C3", sp.simplify(cyl/sah_eps - sp.Rational(1, 2)) == 0,
    "Saharian (16.24) interior cylinder T^0_0 = -1/(60 pi^2 a (a-r)^3) = 1/2 sphere: coefficient "
    "proportional to kappa1+kappa2 (Deutsch-Candelas structure)")
AD = 1/(720*sp.pi**2)
rep("C4", sp.simplify(2*AD/a - 1/(360*sp.pi**2*a)) == 0,
    "Milton (58) with A_D = 1/(720 pi^2) reproduces Milton (130) u ~ 1/(360 pi^2 a (r-a)^3): internal consistency")

# ---------------------------------------------------------------- D
hb, cc, G, lP, R0 = sp.symbols('hbar c G l_P R0', positive=True)
E0 = sp.Symbol('E0', positive=True)
uI = -hb*cc/(30*sp.pi**2*a*e**3)
# leading divergent part of m(r) = INT 4 pi r^2 u / c^2 dr; d/dr = -d/de
# m(r) = INT_0^r 4 pi r'^2 u/c^2 dr' ; with e' = a - r', dr' = -de' -> INT_eps^a 4 pi a^2 u(e')/c^2 de'
m_full = sp.integrate(4*sp.pi*a**2*uI.subs(e, E0)/cc**2, (E0, e, a))
m_lead = sp.limit(m_full*e**2, e, 0)/e**2
m_tree = -(hb*a)/(15*sp.pi*cc*e**2)
rep("D1", sp.simplify(m_lead - m_tree) == 0, f"leading m(r) = {sp.simplify(m_lead)} (tree: -(hbar a)/(15 pi c eps^2))")
chi = sp.simplify(2*G*sp.Abs(m_tree)/(a*cc**2)).subs(G, lP**2*cc**3/hb)
rep("D2", sp.simplify(chi - sp.Rational(2, 15)/sp.pi*lP**2/e**2) == 0, f"chi = 2G|m|/(a c^2) = {sp.simplify(chi)}")
E = sp.Symbol('E', positive=True)
Uw = -hb*cc/(30*sp.pi**2*a*E**3); Pw = -hb*cc/(60*sp.pi**2*a**2*E**2)
Php = -(sp.Rational(2, 15)/sp.pi)*lP**2/(E**2*(a - E))
Ik = sp.integrate(sp.simplify(4*sp.pi*(a - E)**3*(Uw + Pw)*Php), (E, e, a))
den = 4*sp.pi*(a - e)**3*Pw.subs(E, e)
lim = sp.limit(sp.simplify(Ik/den)*15*sp.pi*e**2/lP**2, e, 0)
rep("D3", sp.simplify(sp.Abs(lim) - 1) == 0, f"V16 re-run: lim eps->0 |delta| 15 pi eps^2/l_P^2 = {lim} (delta -> chi/2 at leading order)")
Ksf = sp.sqrt(2)/(128*sp.pi)
coef = sp.simplify(Ksf/AEM)
rep("D4", sp.simplify(coef - 60*sp.sqrt(2)*sp.pi/128) == 0,
    f"crossover coefficient K_SF/A_EM = {coef} = {float(coef):.6f}; a_c/skin = {1/float(coef):.6f}")
LP18 = 1.616255e-35
chi137 = (2/(15*math.pi))*(LP18/137.8e-9)**2
rep("D5", abs(chi137 - 5.8386e-58)/5.8386e-58 < 1e-4, f"chi(137.8 nm) = {chi137:.5e} (tree banked 5.84e-58, recomputed 5.8386e-58)")
rep("D6", abs(1/(15*math.pi) - 0.02122) < 5e-6 and abs(1/math.sqrt(15*math.pi) - 0.1456731) < 5e-8,
    f"delta(l_P) = {1/(15*math.pi):.6f}; delta = 1 at eps = {1/math.sqrt(15*math.pi):.7f} l_P")
# A_EM sensitivity: every magnitude linear in A, every sign independent of A
rep("D7", None, "every tree magnitude built on A_EM (u, p_r, m, chi, delta) is linear in A; "
    "crossover coefficient ~ 1/A; signs independent of A (tolman.py:1059-1060 says the same)")

# ---------------------------------------------------------------- E
NU0 = 40.0
def debye(nu, x):
    w = x/nu
    s = math.sqrt(1 + w*w); t = 1/s
    eta = s + math.log(w/(1 + s))
    u1 = (3*t - 5*t**3)/24
    u2 = (81*t**2 - 462*t**4 + 385*t**6)/1152
    u3 = (30375*t**3 - 369603*t**5 + 765765*t**7 - 425425*t**9)/414720
    v1 = (-9*t + 7*t**3)/24
    v2 = (-135*t**2 + 594*t**4 - 455*t**6)/1152
    v3 = (-42525*t**3 + 451737*t**5 - 883575*t**7 + 475475*t**9)/414720
    SU = 1 + u1/nu + u2/nu**2 + u3/nu**3
    SUm = 1 - u1/nu + u2/nu**2 - u3/nu**3
    SV = 1 + v1/nu + v2/nu**2 + v3/nu**3
    SVm = 1 - v1/nu + v2/nu**2 - v3/nu**3
    logI = nu*eta - 0.5*math.log(2*math.pi*nu) - 0.25*math.log(1 + w*w) + math.log(SU)
    logK = -nu*eta + 0.5*math.log(math.pi/(2*nu)) - 0.25*math.log(1 + w*w) + math.log(SUm)
    dI = (s/w)*SV/SU/nu * nu / x * w  # I'/I = (1+w^2)^{1/2}/w * SV/SU  (derivative wrt x)
    dI = s/w*SV/SU
    dK = -s/w*SVm/SUm
    # derivative with respect to x (= nu w): d/dx = (1/nu) d/dw; A&S 9.7.9/9.7.10 give I'_nu(nu z)
    # already as derivative wrt the argument, so no extra 1/nu.
    return logI, logK, dI, dK

def exact(nu, x):
    iv = special.ive(nu, x); kv = special.kve(nu, x)
    logI = math.log(iv) + x; logK = math.log(kv) - x
    dI = (special.ive(nu - 1, x) + special.ive(nu + 1, x))/(2*iv)
    dK = -(special.kve(nu - 1, x) + special.kve(nu + 1, x))/(2*kv)
    return logI, logK, dI, dK

def funcs(nu, x):
    return debye(nu, x) if nu >= NU0 else exact(nu, x)

def integrand(z, l, rr, aa, which):
    nu = l + 0.5
    x = aa*z; y = rr*z
    lIx, lKx, dIx, dKx = funcs(nu, x)
    lIy, _, dIy, _ = funcs(nu, y)
    br = 1 + (1/(2*x) + dKx)/(1/(2*x) + dIx)
    L = l*(l + 1)
    Heps = (1/(2*y) + dIy)**2 + L/y**2 - 1
    Hpp = L/y**2
    H = {"eps": Heps, "pperp": Hpp, "p": Heps - 2*Hpp}[which]
    return z*y*math.exp(2*lIy + lKx - lIx)*br*H

def q_ren(rr, which, aa=1.0, tol=1e-13):
    tot = 0.0; l = 1; small = 0
    while True:
        nu = l + 0.5
        z1 = max(nu/rr, 1.0)
        f = lambda z: integrand(z, l, rr, aa, which)
        i1, _ = integrate.quad(f, 1e-3, z1, limit=400, epsabs=0, epsrel=1e-11)
        i2, _ = integrate.quad(f, z1, np.inf, limit=400, epsabs=0, epsrel=1e-11)
        term = -(2*l + 1)/(8*math.pi**2*rr**2)*(i1 + i2)
        tot += term
        if abs(term) < tol*abs(tot):
            small += 1
            if small >= 3: break
        else:
            small = 0
        l += 1
        if l > 20000: raise RuntimeError("no convergence")
    return tot, l

# E0: Debye vs exact at the switch (implementation check)
d = debye(NU0 + 0.0, 35.0); x_ = exact(NU0 + 0.0, 35.0)
rep("E0", bool(all(abs(p - q) < 1e-6*max(1, abs(q)) for p, q in zip(d, x_))),
    f"Debye(u3,v3) vs scipy at nu=40, x=35: {[round(v, 9) for v in d]} vs {[round(v, 9) for v in x_]}")
# E1: centre value, published eps(0) = -0.0381 a^-4 (Saharian (14.22))
e0, _ = q_ren(1e-3, "eps")
rep("E1", bool(abs(e0 - (-0.0381))/0.0381 < 5e-3), f"eps(r=1e-3 a) = {e0:.5f} a^-4 (published eps(0) = -0.0381 a^-4)")
p0, _ = q_ren(1e-3, "p")
rep("E1b", bool(abs(e0 - 3*p0) < 1e-3*abs(e0)), f"centre equation of state eps(0) = 3 p(0): {e0:.5f} vs 3*{p0:.5f}")
# E2: near-wall coefficients
deltas = [0.2, 0.15, 0.12, 0.1, 0.08, 0.065, 0.05, 0.04, 0.03]
rows = []
for dl in deltas:
    ev, le = q_ren(1 - dl, "eps"); pv, lp = q_ren(1 - dl, "p")
    rows.append((dl, ev*dl**3, pv*dl**2, le))
    print(f"   delta={dl:<6} eps*d^3={ev*dl**3:+.8f}  p*d^2={pv*dl**2:+.8f}  l_max={le}")
D_ = np.array([r_[0] for r_ in rows]); G3 = np.array([r_[1] for r_ in rows]); G2 = np.array([r_[2] for r_ in rows])
target_e = -1/(30*math.pi**2); target_p = -1/(60*math.pi**2)
fits = {}
for deg in (2, 3, 4):
    ce = np.polyfit(D_, G3, deg)[-1]; cp = np.polyfit(D_, G2, deg)[-1]
    fits[deg] = (ce, cp)
    print(f"   fit deg {deg}: c0(eps*d^3) = {ce:+.8f} (target {target_e:+.8f}, ratio {ce/target_e:.5f});"
          f"  c0(p*d^2) = {cp:+.8f} (target {target_p:+.8f}, ratio {cp/target_p:.5f})")
ce, cp = fits[3]
rep("E2", bool(abs(ce/target_e - 1) < 1e-2),
    f"exact EM mode sum, interior: lim (a-r)^3 eps = {ce:+.7f} vs -1/(30 pi^2) = {target_e:+.7f} (ratio {ce/target_e:.5f})"
    f" -> A_EM = {-ce/2:.7e} vs 1/(60 pi^2) = {1/(60*math.pi**2):.7e}")
rep("E3", bool(abs(cp/target_p - 1) < 2e-2),
    f"exact EM mode sum, interior: lim (a-r)^2 p_r = {cp:+.7f} vs -1/(60 pi^2) = {target_p:+.7f} (ratio {cp/target_p:.5f})")
alt = {"1/(30pi^2) [factor 2]": 1/(30*math.pi**2), "1/(120pi^2) [factor 1/2]": 1/(120*math.pi**2),
       "1/(720pi^2) [Dirichlet]": 1/(720*math.pi**2)}
rep("E4", None, "A extracted vs alternatives: " + "; ".join(f"{k}: ratio {(-ce/2)/v:.3f}" for k, v in alt.items()))

res["_table"] = rows; res["_fits"] = {str(k): v for k, v in fits.items()}
ok = all(v["ok"] is not False for k, v in res.items() if not k.startswith("_"))
print("OVERALL:", "ALL PASS" if ok else "SOME FAIL")
json.dump(res, open(__file__.replace(".py", ".out.json"), "w"), indent=1, default=str)
sys.exit(0 if ok else 1)
