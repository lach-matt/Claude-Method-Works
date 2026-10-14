#!/usr/bin/env python3
"""
DOCKET 67 -- rederive / machine-check for key 'fewster-osterbrink-qei'.

Source READ at alphaXiv: Fewster & Osterbrink, "Quantum Energy Inequalities for the
Non-Minimally Coupled Scalar Field", arXiv:0708.2450v2 (23 Oct 2007); J. Phys. A 41
(2008) 025402 (journal version NOT read here).

What the tree uses (research/warp-drive/bounds.py:47 and :304): the row
    ("Fewster-Osterbrink QEI", W=1, B=1, S=0, G=0, K=1, Z=1, "state-independent; shares SNEC's cell")
i.e. a smeared density bounded by a NEGATIVE CONSTANT (B=1) with a STATE-INDEPENDENT RHS (S=0).

Checks (all finite / closed form):
  A  Sec.3 counterexample: h_kappa normalised, <H> = 2 kappa/3 (26), rho(t,0) = eq.(28),
     rho(0,0) = -xi (2 kappa)^4 / (3 pi^2) (29), scaling (27).  -> for xi > 0 no
     state-independent lower bound: the S=0 coding is false for xi in (0,1/4].
  B  Sec.5.2 state (70): <H^j> = (kappa/2)^j (j+1)!, rho(t) along the origin, and the
     kappa -> infinity limit of the smeared density over <H^3>  (eqs. 71-72).
  C  Q_{n,k} in (56): Q(1)=0, Q<=1, Q->1; estimate (57)'s coefficient; the xi=0, m=0, n=4
     reduction of (55) to the Fewster-Eveson constant 1/(16 pi^3).
  D  (53) <-> (55) numerically for n=4, m=1, xi in {0, 0.1, 0.25}.
  E  Theorem 5.1 KMS scaling (62)-(64): beta^n * state-dependent part -> 0 while
     beta^n * <rho>(f^2) -> B_{n,2}(0)||f||^2 > 0 (n=4, m=0 closed form).
  F  The tree's cost of the coding: copy of research/warp-drive (+tools) into the scratch
     sandbox, row 304 re-coded to the source's xi>0 content, bounds selftest re-run; the
     pins that move are listed.  NOTHING under research/ is written.
"""
import json, math, os, shutil, subprocess, sys, tempfile
import sympy as sp
import mpmath as mp

OUT = {}
ok_all = True


def rec(name, good, detail=""):
    global ok_all
    ok_all &= bool(good)
    OUT[name] = {"ok": bool(good), "detail": detail}
    print("  [%s] %s %s" % ("ok" if good else "XX", name, detail))


t, k, kap, xi, s, x, y = sp.symbols('t k kappa xi s x y', positive=True)
treal = sp.symbols('t', real=True)

# ---------------------------------------------------------------- A (Sec. 3)
# n=4 massless: dmu(k) = d^3k/((2pi)^3 2|k|); radial: (1/(4 pi^2)) int k dk
h = 4*sp.pi*sp.sqrt(2)*(kap - k/3)*sp.exp(-k/kap)/kap**2
norm = sp.simplify(sp.integrate(k*h**2, (k, 0, sp.oo))/(4*sp.pi**2))
rec("A1 h_kappa normalised (||h||_H = 1)", sp.simplify(norm - 1) == 0, str(norm))
E1 = sp.simplify(sp.integrate(k**2*h**2, (k, 0, sp.oo))/(4*sp.pi**2))
rec("A2 <H> = 2 kappa/3  (26)", sp.simplify(E1 - 2*kap/3) == 0, str(E1))
# F(t) = <Omega|Phi(t,0)Psi> = (1/(4pi^2)) int k e^{-itk} h(k) dk ; spatial grads vanish at x=0
F = sp.simplify(sp.integrate(k*h*sp.exp(-sp.I*treal*k), (k, 0, sp.oo), conds='none')/(4*sp.pi**2))
Fb = sp.conjugate(F)
rho = sp.simplify(sp.expand_complex(sp.diff(F, treal)*sp.conjugate(sp.diff(F, treal))
                  - 4*xi*sp.re(Fb*sp.diff(F, treal, 2))))
rho28 = 8*kap**4/(3*(1 + treal**2*kap**2)**5*sp.pi**2)*((3*treal**4*kap**4 + 3*treal**2*kap**2)
                                                     - xi*(18*treal**4*kap**4 - 44*treal**2*kap**2 + 2))
d28 = sp.simplify(rho - rho28)
rec("A3 rho(t,0) reproduces eq.(28) exactly", d28 == 0, "difference = %s" % d28)
r00 = sp.simplify(rho.subs(treal, 0))
rec("A4 rho(0,0) = -xi (2 kappa)^4/(3 pi^2)  (29)",
    sp.simplify(r00 + xi*(2*kap)**4/(3*sp.pi**2)) == 0, str(r00))
lam = sp.symbols('lambda', positive=True)
sc = sp.simplify(rho.subs(kap, lam*kap) - lam**4*rho.subs(treal, lam*treal))
rec("A5 scaling relation (27) on the axis", sc == 0, str(sc))
# unboundedness: j copies at kappa' give j * rho; any rho0 is beaten -> no constant Q(f)
rec("A6 xi>0 => rho(0,0) < 0 for every kappa, and |rho| grows as kappa^4 (no state-independent bound)",
    sp.simplify(r00.subs(xi, sp.Rational(1, 6))/kap**4) < 0, "rho(0,0)/kappa^4 at xi=1/6: %s"
    % sp.simplify(r00.subs(xi, sp.Rational(1, 6))/kap**4))

# ---------------------------------------------------------------- B (Sec. 5.2)
g = 4*sp.pi/kap*sp.exp(-k/kap)
jj = sp.symbols('j', nonnegative=True, integer=True)
Hj = [sp.simplify(sp.integrate(k*k**j*g**2, (k, 0, sp.oo))/(4*sp.pi**2)) for j in range(5)]
rec("B1 <H^j> = (kappa/2)^j (j+1)!  j=0..4",
    all(sp.simplify(Hj[j] - (kap/2)**j*sp.factorial(j + 1)) == 0 for j in range(5)), str(Hj))
G = sp.simplify(sp.integrate(k*g*sp.exp(-sp.I*treal*k), (k, 0, sp.oo), conds='none')/(4*sp.pi**2))
rhoB = sp.simplify(sp.expand_complex(sp.diff(G, treal)*sp.conjugate(sp.diff(G, treal))
                   - 4*xi*sp.re(sp.conjugate(G)*sp.diff(G, treal, 2))))
first_derived = sp.simplify(sp.expand_complex(sp.diff(G, treal)*sp.conjugate(sp.diff(G, treal))))
second_derived = sp.simplify(rhoB - first_derived)
first_printed_as_extracted = kap**4/sp.pi**2*4/(1 + treal**2*kap**2)
first_exp3 = kap**4/sp.pi**2*4/(1 + treal**2*kap**2)**3
second_printed = -kap**4/sp.pi**2*4*xi*6*(treal**2*kap**2 - 1)/(1 + treal**2*kap**2)**4
rec("B2 xi-term of rho(t) equals eq.(71)'s xi-term exactly",
    sp.simplify(second_derived - second_printed) == 0, str(sp.factor(second_derived)))
rec("B3 xi-independent term derived = 4 kappa^4/(pi^2 (1+t^2 kappa^2)^3)",
    sp.simplify(first_derived - first_exp3) == 0, str(sp.factor(first_derived)))
disc71 = sp.simplify(first_derived - first_printed_as_extracted) != 0
OUT["B3_note"] = ("DISCREPANCY (recorded, not a refutation): the alphaXiv text extraction of eq.(71) "
                  "shows the first term as 4/(1+t^2 kappa^2) (no visible exponent); the derivation "
                  "from state (70) gives exponent 3. Extraction may have dropped a superscript; the "
                  "journal version was not read.") if disc71 else "no discrepancy"
# smeared limit: int rho(t) f(t)^2 dt, kappa->inf: substitute t = s/kappa -> kappa^3 f(0)^2 int rho~(s) ds
rho_s = sp.simplify((rhoB/kap**4).subs(treal, s/kap))
I_first = sp.integrate(sp.simplify((first_derived/kap**4).subs(treal, s/kap)), (s, -sp.oo, sp.oo))
I_second = sp.integrate(sp.simplify((second_derived/kap**4).subs(treal, s/kap)), (s, -sp.oo, sp.oo))
I_tot = sp.simplify(I_first + I_second)   # limit = kappa^3 f(0)^2 * I_tot
ratio_derived = sp.simplify(I_tot/3)       # / <H^3> = 3 kappa^3, normalised by f(0)^2
ratio_printed = 2*(2 + 3*xi)/(3*sp.pi)     # eq.(72), normalised (as extracted) by ||f||^2_{L2}
I_first_as_printed = sp.integrate(4/(1 + s**2), (s, -sp.oo, sp.oo))
rec("B4 kappa->inf smeared/<H^3> scales like kappa^0 (q >= 3 conclusion reproduced)",
    sp.simplify(I_tot).is_positive, "limit/(f(0)^2) = %s ; printed (72) = %s" % (ratio_derived, ratio_printed))
OUT["B4_note"] = ("DISCREPANCY (recorded): derived limit = f(0)^2 (1+4 xi)/(2 pi) = f(0)^2 (3/2+6xi)/(3 pi); "
                  "printed (72) = ||f||^2 2(2+3xi)/(3pi). xi-coefficients agree (6 xi/(3pi)); the xi-free "
                  "part agrees with the printed (72) only if (71)'s first term has exponent 1 (int 4/(1+s^2) = %s "
                  "-> 4/(3pi)), which the state (70) does not give (exponent 3 -> int = %s -> 1/(2pi)). "
                  "The normalisation ||f||_{L2}^2 is dimensionally inconsistent with a kappa^3 limit of a "
                  "pulse of width 1/kappa (derived: f(0)^2). The conclusion q >= 3 is unaffected: any positive "
                  "constant gives it. Not quoted as an error: extraction of v2 only, journal version unread."
                  % (I_first_as_printed, I_first))
# numeric cross-check of the limit with a concrete f (f = exp(-t^2)), kappa large
xiv = 0.1
fnum = lambda tt: math.exp(-tt*tt)
rho_num = sp.lambdify((treal, kap, xi), rhoB, 'mpmath')
for K in (1e2, 1e3):
    val = mp.quad(lambda tt: rho_num(tt, K, xiv)*fnum(tt)**2, [-mp.inf, -10/K, 0, 10/K, mp.inf])
    OUT.setdefault("B5_numeric", []).append({"kappa": K, "smeared/<H^3>": float(val/(3*K**3)),
                                              "derived f(0)^2(1+4xi)/(2pi)": (1 + 4*xiv)/(2*math.pi),
                                              "printed 2(2+3xi)/(3pi)*||f||^2": 2*(2 + 3*xiv)/(3*math.pi)*math.sqrt(math.pi/2)})
b5 = OUT["B5_numeric"][-1]
rec("B5 numeric smeared limit matches derived f(0)^2 form (kappa=1e3, xi=0.1)",
    abs(b5["smeared/<H^3>"]/b5["derived f(0)^2(1+4xi)/(2pi)"] - 1) < 1e-2, json.dumps(b5))

# ---------------------------------------------------------------- C (56),(57),(55)
n_ = 4
def Qnum(nn, kk, Y):
    return (nn + kk - 2)/mp.mpf(Y)**(nn + kk - 2)*mp.quad(lambda X: (X*X - 1)**(mp.mpf(nn - 3)/2)*X**kk, [1, Y])
okC = True
for kk in (0, 1, 2):
    okC &= Qnum(4, kk, 1) == 0
    okC &= abs(Qnum(4, kk, 1e6) - 1) < 1e-5
    okC &= all(Qnum(4, kk, v) <= 1 for v in (1.01, 2, 10, 1e3))
# symbolic: (x^2-1)^{(n-3)/2} <= x^{n-3} on x>=1 gives Q_{n,k}(Y) <= 1 - Y^{-(n+k-2)} <= 1
Ysym = sp.symbols('Y', positive=True)
ub = sp.simplify(4/Ysym**4*sp.integrate(x**3, (x, 1, Ysym)))
okC &= sp.simplify(ub - (1 - Ysym**-4)) == 0
# closed form for k=1, n=4: Q_{4,1}(Y) = (1 - 1/Y^2)^{3/2}
q41 = sp.simplify(3/Ysym**3*sp.integrate(sp.sqrt(x**2 - 1)*x, (x, 1, Ysym)))
okC &= abs(float(q41.subs(Ysym, 3)) - float((1 - sp.Rational(1, 9))**sp.Rational(3, 2))) < 1e-12
rec("C1 Q_{4,k}(1)=0, Q_{4,k}->1, Q_{4,k}<=1 for k=0,1,2", okC)
nn = sp.symbols('n', positive=True)
coef57 = sp.simplify(1/nn + 2*sp.Rational(1, 4)/(nn - 2))   # drop -4xi Q_{n,1}/(n-1) <= 0, Q<=1, xi<=1/4
rec("C2 (57) coefficient (3n-4)/(2n(n-2)) = 1/n + (1/2)/(n-2)",
    sp.simplify(coef57 - (3*nn - 4)/(2*nn*(nn - 2))) == 0, str(sp.factor(coef57)))
S2 = 2*sp.sqrt(sp.pi)**3/sp.gamma(sp.Rational(3, 2))
pref = sp.simplify(S2/(2*sp.pi)**4)
massless = sp.simplify(pref*(sp.Rational(1, 4) - 4*xi/3 + 2*xi/2))
rec("C3 m=0,n=4: (55) prefactor x bracket = (1/(4pi^3))(1/4 - xi/3); xi=0 -> 1/(16 pi^3) (Fewster-Eveson)",
    sp.simplify(massless.subs(xi, 0) - 1/(16*sp.pi**3)) == 0, str(massless))

# C4 cross-check against the tree's own evaluation (paper/CLAIMS.md H46b: Q_A = (3-4xi)/(64 pi^2 tau^4),
# "n=4, massless, unit-L2 Gaussian"): (55) at m=0 with f = (pi tau^2)^(-1/4) exp(-t^2/(2 tau^2))
tau, u = sp.symbols('tau u', positive=True)
fg = (sp.pi*tau**2)**sp.Rational(-1, 4)*sp.exp(-treal**2/(2*tau**2))
assert sp.simplify(sp.integrate(fg**2, (treal, -sp.oo, sp.oo)) - 1) == 0
fhat = sp.simplify(sp.integrate(fg*sp.exp(sp.I*u*treal), (treal, -sp.oo, sp.oo)))
QA = sp.simplify(massless*sp.integrate(sp.simplify(fhat*sp.conjugate(fhat))*u**4, (u, 0, sp.oo)))
rec("C4 (55), m=0, n=4, unit-L2 Gaussian exp(-t^2/2tau^2): Q_A = (3-4xi)/(64 pi^2 tau^4), as the tree's CLAIMS.md H46b",
    sp.simplify(QA - (3 - 4*xi)/(64*sp.pi**2*tau**4)) == 0, str(QA))

# ---------------------------------------------------------------- D (53) vs (55)
mp.mp.dps = 15
def fhat2(u):
    return mp.e**(-u*u/4)      # |f^|^2 for a Gaussian test profile (only |f^|^2 enters)
def Q53(xiv, m=1.0):
    Sn = 4*mp.pi
    inner = lambda a: mp.quad(lambda kk: kk**2/mp.sqrt(kk*kk + m*m)*((1 - 2*xiv)*(kk*kk + m*m) + 2*xiv*a*a)
                              * fhat2(a + mp.sqrt(kk*kk + m*m)), [0, 5, mp.inf])
    return Sn/(2*mp.pi)**4*mp.quad(inner, [0, 5, mp.inf])
def Qn4(kk, Y):
    return (kk + 2)/Y**(kk + 2)*mp.quad(lambda X: mp.sqrt(X*X - 1)*X**kk, [1, Y])
def Q55(xiv, m=1.0):
    Sn = 4*mp.pi
    br = lambda u: (Qn4(2, u/m)/4 - 4*xiv*Qn4(1, u/m)/3 + 2*xiv*Qn4(0, u/m)/2)
    return Sn/(2*mp.pi)**4*mp.quad(lambda u: fhat2(u)*u**4*br(u), [m, 5, mp.inf])
dd = []
for xv in (0.0, 0.1, 0.25):
    a, b = Q53(xv), Q55(xv)
    dd.append({"xi": xv, "Q53": float(a), "Q55": float(b), "rel": float(abs(a/b - 1))})
rec("D1 (53) == (55) numerically (n=4, m=1)", all(d["rel"] < 1e-8 for d in dd), json.dumps(dd))

# ---------------------------------------------------------------- E Theorem 5.1 scaling
beta = sp.symbols('beta', positive=True)
z = sp.symbols('z', positive=True)
def bose(r):   # int_0^inf z^r/(e^z-1) dz = Gamma(r+1) zeta(r+1), checked numerically
    val = sp.gamma(r + 1)*sp.zeta(r + 1)
    assert abs(float(val) - float(mp.quad(lambda zz: zz**r/(mp.e**zz - 1), [0, 1, mp.inf]))) < 1e-10
    return sp.nsimplify(sp.simplify(val))
B40 = 4*sp.pi/(2*sp.pi)**3*bose(1)
B42 = 4*sp.pi/(2*sp.pi)**3*bose(3)
state_dep = 2*beta**(2 - 4)*B40      # x ||f'||^2
dens = beta**-4*B42                  # x ||f||^2
rec("E1 m=0,n=4: beta^4 * state-dependent part -> 0, beta^4 * <rho>(f^2) -> B_{4,2}(0) = pi^2/30 > 0",
    sp.limit(beta**4*state_dep, beta, 0) == 0 and sp.simplify(B42 - sp.pi**2/30) == 0,
    "B40=%s B42=%s" % (sp.simplify(B40), sp.simplify(B42)))

kb = sp.symbols('kb', positive=True)
# [:w_beta:]_c = int dmu 2/(e^{beta k}-1) = (1/(4pi^2)) int 2k/(e^{beta k}-1) dk ; k = z/beta
integrand_k = k*2/(sp.exp(beta*k) - 1)/(4*sp.pi**2)
integrand_z = sp.simplify(integrand_k.subs(k, z/beta)/beta)
assert sp.simplify(integrand_z - beta**-2*2*z/(sp.exp(z) - 1)/(4*sp.pi**2)) == 0
coinc = sp.simplify(beta**-2*2/(4*sp.pi**2)*bose(1))
rec("E2 [:w_beta:]_c = beta^(2-n) B_{n,0}(beta m) (m=0,n=4): F-O eq.(61) as printed omits beta^(2-n); "
    "Fewster-Kontou 1809.05047 fn.4 records the same omission ('final results are correct')",
    sp.simplify(coinc - beta**-2*B40) == 0 and sp.simplify(coinc - B40) != 0,
    "coincidence=%s, B40=%s" % (coinc, sp.simplify(B40)))

# ---------------------------------------------------------------- F the tree's coding, measured
HERE = os.path.dirname(os.path.abspath(__file__))
SANDBOX = os.path.join(os.path.dirname(HERE), "sandbox", "fo-recode")
REPO = "/home/user/Claude-Method-Works"
ROW_OLD = '("Fewster-Osterbrink QEI", 1, 1, 0, 0, 1, 1,'
def run_variant(tag, new_row):
    root = os.path.join(SANDBOX, tag)
    shutil.rmtree(root, ignore_errors=True)
    os.makedirs(os.path.join(root, "research"), exist_ok=True)
    shutil.copytree(os.path.join(REPO, "research", "warp-drive"), os.path.join(root, "research", "warp-drive"),
                    ignore=shutil.ignore_patterns("*.pyc", "__pycache__", "site", "paper", "*.md", "*.json", "*.html"))
    shutil.copytree(os.path.join(REPO, "tools"), os.path.join(root, "tools"),
                    ignore=shutil.ignore_patterns("*.pyc", "__pycache__"))
    bp = os.path.join(root, "research", "warp-drive", "bounds.py")
    src = open(bp).read()
    assert src.count(ROW_OLD) == 1
    if new_row:
        src = src.replace(ROW_OLD, new_row)
        open(bp, "w").write(src)
    env = dict(os.environ, PYTHONDONTWRITEBYTECODE="1")
    p = subprocess.run([sys.executable, "bounds.py", "--selftest"], cwd=os.path.dirname(bp),
                       capture_output=True, text=True, env=env, timeout=600)
    lines = p.stdout.splitlines()
    xx = [l.strip() for l in lines if l.strip().startswith("[XX]")]
    nok = sum(1 for l in lines if l.strip().startswith("[ok]"))
    sys.path.insert(0, os.path.dirname(bp))
    return {"rc": p.returncode, "ok": nok, "XX": xx}
base = run_variant("baseline", None)
v1 = run_variant("B2S1", '("Fewster-Osterbrink QEI", 1, 2, 1, 0, 1, 1,')
v2 = run_variant("B1S1", '("Fewster-Osterbrink QEI", 1, 1, 1, 0, 1, 1,')
OUT["F_baseline"] = base
OUT["F_recode_B2_S1"] = v1
OUT["F_recode_B1_S1"] = v2
rec("F1 baseline copy passes its selftest (live bounds.py unchanged)", base["rc"] == 0 and not base["XX"],
    "ok=%d" % base["ok"])
rec("F2 re-coding the row to the source's xi>0 content moves pins (measured, NOT applied)",
    len(v1["XX"]) > 0, "B2S1: %d XX; B1S1: %d XX" % (len(v1["XX"]), len(v2["XX"])))
for tag, v in (("B2S1", v1), ("B1S1", v2)):
    for l in v["XX"]:
        print("       %s  %s" % (tag, l))

print("\nfewster-osterbrink-qei rederive:", "ALL CHECKS PASS" if ok_all else "SOME CHECKS FAIL")
json.dump(OUT, open(os.path.join(HERE, "fewster-osterbrink-qei.out.json"), "w"), indent=1, default=str)
sys.exit(0 if ok_all else 1)
