#!/usr/bin/env python3
"""DOCKET 67 audit: Anderson-Hiscock-Samuel PRD 51 4337 (1995).

AHS itself is NAMED-NOT-READ here (no arXiv copy; APS, INSPIRE, arXiv, academia
egress-blocked; alphaXiv quota exhausted after one call).  What IS checkable: the
AHS DeWitt-Schwinger (large-m WKB) approximation <T^mu_nu>_DS as RESTATED by its
own authors in Taylor-Hiscock-Anderson gr-qc/9608036 (READ this run, pp.1-17),
eqs. (10)-(12) (zero-tidal Schwarzschild wormhole) and (15)-(17) (simple wormhole).

Checks (sympy):
 C1  covariant conservation of TSH (10)-(12) on Phi = 0, b = r0, for all r, xi.
 C2  TSH's printed thresholds from (10)-(12): tau0 > 0 iff xi > 23/84;
     exotic (tau0-rho0)/|rho0| > 0 iff xi < 10/84  -> no overlap.
 C3  covariant conservation of TSH (15)-(17) on Phi = 0, b = r0^2/r.
 C4  TSH's printed roots for (15)-(17) at the throat: 0.860358 (tension),
     0.151551, 0.2596, 1.42218 (exotic condition).
Stress conservation for a static diagonal T^mu_nu on
ds^2 = -e^{2Phi}dt^2 + dr^2/(1-b/r) + r^2 dOmega^2:
   d_r T^r_r + Phi'(T^r_r - T^t_t) + (2/r)(T^r_r - T^th_th) = 0.
"""
import sympy as sp

r, r0, xi, m = sp.symbols('r r0 xi m', positive=True)
pi = sp.pi
ok = True
def chk(name, cond):
    global ok
    ok &= bool(cond)
    print(("PASS " if cond else "FAIL ") + name)

def cons(Ttt, Trr, Tth, Phi=0):
    return sp.simplify(sp.diff(Trr, r) + sp.diff(Phi, r)*(Trr-Ttt) + 2/r*(Trr-Tth))

# --- TSH (10)-(12)
D = 53760*pi**2*r**9*m**2
Ttt = r0**2*(-405*r + 448*r0 + 2520*r*xi - 2772*r0*xi)/D
Trr = r0**2*(261*r - 238*r0 - 1008*r*xi + 924*r0*xi)/D
Tth = r0**2*(-783*r + 833*r0 + 3024*r*xi - 3234*r0*xi)/D
res = cons(Ttt, Trr, Tth)
print("C1 residual (10)-(12):", res)
chk("C1 TSH (10)-(12) conserved identically in r, xi", res == 0)

tau0 = sp.simplify(-Trr.subs(r, r0)); rho0 = sp.simplify(-Ttt.subs(r, r0))
x_t = sp.solve(sp.Eq(tau0, 0), xi); x_e = sp.solve(sp.Eq(tau0 - rho0, 0), xi)
print("C2 tau0 = 0 at xi =", x_t, "; tau0 - rho0 = 0 at xi =", x_e, "; rho0 = 0 at xi =", sp.solve(rho0, xi))
chk("C2 tension threshold 23/84", x_t == [sp.Rational(23, 84)])
chk("C2 exotic numerator root 10/84", x_e == [sp.Rational(10, 84)])
# sign structure: for xi < 10/84 < 43/252, rho0 < 0 ; exotic cond (tau0-rho0)/|rho0|>0 iff xi<10/84
xs = [sp.Rational(k, 1000) for k in range(-500, 1500, 7)]
agree = all(((((tau0-rho0)/sp.Abs(rho0)).subs(xi, x).subs({r0:1, m:1}) > 0)) == (x < sp.Rational(10, 84))
            for x in xs if rho0.subs(xi, x) != 0)
both = [x for x in xs if tau0.subs({xi:x, r0:1, m:1}) > 0 and rho0.subs({xi:x, r0:1, m:1}) != 0
        and ((tau0-rho0)/sp.Abs(rho0)).subs({xi:x, r0:1, m:1}) > 0]
chk("C2 exotic condition <=> xi < 10/84 on a grid of %d xi" % len(xs), agree)
chk("C2 no xi satisfies both (TSH: 'not possible ... for any value')", both == [])

# --- TSH (15)-(17)
D2 = 20160*pi**2*r**12*m**2
Ttt2 = r0**2/D2*(5940*r**4 - 22932*r**2*r0**2 + 18025*r0**4
        + xi*(-60480*r**4 + 238168*r**2*r0**2 - 188930*r0**4)
        + xi**2*(151200*r**4 - 631680*r**2*r0**2 + 513660*r0**4)
        + xi**3*(141120*r**2*r0**2 - 160440*r0**4))
Trr2 = r0**2/D2*(-2484*r**4 + 7116*r**2*r0**2 - 4445*r0**4
        + xi*(24192*r**4 - 69048*r**2*r0**2 + 43050*r0**4)
        + xi**2*(-60480*r**4 + 181440*r**2*r0**2 - 115500*r0**4)
        + xi**3*(-40320*r**2*r0**2 + 36120*r0**4))
Tth2 = r0**2/D2*(7452*r**4 - 28464*r**2*r0**2 + 22225*r0**4
        + xi*(-72576*r**4 + 276192*r**2*r0**2 - 215250*r0**4)
        + xi**2*(181440*r**4 - 725760*r**2*r0**2 + 577500*r0**4)
        + xi**3*(161280*r**2*r0**2 - 180600*r0**4))
res2 = sp.expand(sp.simplify(cons(Ttt2, Trr2, Tth2)*D2/r0**2))
print("C3 residual (15)-(17) (times D/r0^2):", sp.factor(res2))
chk("C3 TSH (15)-(17) conserved identically", res2 == 0)

t2 = sp.expand(-Trr2.subs(r, r0)*D2.subs(r, r0)/r0**2)
rh2 = sp.expand(-Ttt2.subs(r, r0)*D2.subs(r, r0)/r0**2)
rt = sorted([sp.N(z) for z in sp.Poly(t2.subs(r0, 1), xi).nroots() if abs(sp.im(z)) < 1e-12], key=float)
rd = sorted([sp.N(z) for z in sp.Poly((t2 - rh2).subs(r0, 1), xi).nroots() if abs(sp.im(z)) < 1e-12], key=float)
rr = sorted([sp.N(z) for z in sp.Poly(rh2.subs(r0, 1), xi).nroots() if abs(sp.im(z)) < 1e-12], key=float)
print("C4 real roots tau0:", [round(float(z), 6) for z in rt])
print("C4 real roots tau0-rho0:", [round(float(z), 6) for z in rd], " rho0:", [round(float(z), 6) for z in rr])
# dividing by |rho0| does not change sign: the exotic condition changes only at roots of tau0-rho0
cands = sorted({round(float(z), 6) for z in rd})
print("C4 exotic-condition breakpoints:", cands)
chk("C4 tension root 0.860358 reproduced", any(abs(float(z) - 0.860358) < 5e-6 for z in rt))
for target in (0.151551, 0.2596, 1.42218):
    chk("C4 exotic breakpoint %s reproduced" % target, any(abs(c - target) < 6e-5 for c in cands))

f_t = sp.lambdify(xi, t2.subs(r0, 1)); f_e = sp.lambdify(xi, (t2 - rh2).subs(r0, 1)); f_r = sp.lambdify(xi, rh2.subs(r0, 1))
grid = [k/10000 for k in range(-20000, 40000)]
ex = [x for x in grid if f_r(x) != 0 and f_e(x) > 0]
supp = [x for x in grid if f_t(x) > 0 and f_r(x) != 0 and f_e(x) > 0]
def ivals(xs):
    out=[]; 
    for x in xs:
        if out and abs(x-out[-1][1]) < 1.5e-4: out[-1][1]=x
        else: out.append([x,x])
    return [(round(a,4),round(b,4)) for a,b in out]
print("C4 exotic intervals on [-2,4):", ivals(ex)); print("C4 both-condition intervals:", ivals(supp))
chk("C4 exotic iff xi<0.151551 or 0.2596<xi<1.42218 (TSH p.9)", len(ivals(ex))==2 and all(abs(a-b)<2e-4 for a,b in zip(sum(map(list,ivals(ex)),[]),[-2.0,0.151551,0.2596,1.42218])))
chk("C4 both conditions iff 0.860358<xi<1.42218 (TSH p.9); excludes xi=0 and 1/6", len(ivals(supp))==1 and abs(ivals(supp)[0][0]-0.860358)<2e-4 and abs(ivals(supp)[0][1]-1.42218)<2e-4)
print("\nNOT CHECKED: AHS's own massless (m = 0) analytic approximation, its state,")
print("its arbitrary parameter, its derivation hypotheses (asymptotic flatness or not):")
print("AHS NAMED-NOT-READ; the tree's transcription of that approximation is HPS (5)-(7)")
print("and Popov (B1)-(B3), whose conservation hpscentre.py already tests.")
print("\nALL PASS" if ok else "\nSOME FAIL")
raise SystemExit(0 if ok else 1)
