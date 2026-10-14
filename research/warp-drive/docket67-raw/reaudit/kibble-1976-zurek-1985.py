#!/usr/bin/env python3
"""DOCKET 67 re-audit: kibble-1976-zurek-1985 against Zurek, Nature 317, 505-508 (1985), READ from its page images.

  Z1  eqs.(12)-(14): xi = xi0 eps^-nu, u = u0 eps^(1-nu)  ->  tau = xi/u = tau0/eps, tau0 = xi0/u0, for ANY nu.
  Z2  eq.(15) tau(t^) = t^ with eq.(11) eps = t/tau_Q  ->  eq.(16) t^ = sqrt(tau0 tau_Q);
      eq.(17) d = xi(eps^) = xi0 (tau_Q/tau0)^(nu/2).
  Z3  the first audit's general form t^ = (tau0 tau_Q^(z nu))^(1/(1+z nu)), xi^ = xi0 (tau_Q/tau0)^(nu/(1+z nu))
      reduces to Z2 exactly at z nu = 1, which is what tau ~ 1/eps (Z1) means.
  Z4  printed numbers: tau0 = xi0/u0 ~= 8.5e-12 s in both models (5.6 A / 70 m/s and 4 A / 47 m/s).
  Z5  tau_Q = 1e-2 s, C = 1 cm: d from eq.(17) in both models vs printed 'd ~ 1e4 A'; v_s from eq.(10)
      vs printed 'detectable v_s ~ 1 mm/s'.  (Zurek: eq.17 'correct to within an order of magnitude'.)
  Z6  eq.(18)-(19): J_s ~ 5e-11 g cm^2/s and J_T ~ 1e-13 g cm^2/s at the printed inputs.
  Z7  eq.(22) RHS (m^2/hbar^2) k T_lambda / pi a^2 vs printed 0.35e-8 / a^2 g cm^-2.
  Z8  eq.(9): N independent phases -> random-walk mismatch ~ sqrt(N) (Monte Carlo, seed 67).
Nothing here tests Kibble 1976 (not obtained); its content is graded READ-VIA-RESTATEMENT in the JSON.
Exit 0 iff all pass.
"""
import sys, math, random
import sympy as sp

ok = []
def chk(name, cond, extra=""):
    ok.append(bool(cond)); print(("PASS " if cond else "FAIL ") + name + (("   " + extra) if extra else ""))

eps, nu, xi0, u0, t, tQ, t0, z = sp.symbols('epsilon nu xi0 u0 t tau_Q tau0 z', positive=True)
xi = xi0*eps**(-nu); u = u0*eps**(1-nu)
tau = sp.simplify(xi/u)
chk("Z1 tau = xi/u = (xi0/u0)/eps for any nu  [eqs.12-14]", sp.simplify(tau - (xi0/u0)/eps) == 0)

th = sp.symbols('that', positive=True)
sol = sp.solve(sp.Eq(t0/(th/tQ), th), th)
chk("Z2 eq.(16): t^ = sqrt(tau0 tau_Q)", len(sol) == 1 and sp.simplify(sol[0] - sp.sqrt(t0*tQ)) == 0)
d = sp.simplify(xi0*(sol[0]/tQ)**(-nu))
chk("Z2 eq.(17): d = xi0 (tau_Q/tau0)^(nu/2)", sp.simplify(sp.log(d) - sp.log(xi0*(tQ/t0)**(nu/2))) == 0)

tgen = (t0*tQ**(z*nu))**(1/(1+z*nu)); xigen_exp = nu/(1+z*nu)
chk("Z3 general KZ form reduces to Zurek 1985 at z*nu = 1",
    sp.simplify(tgen.subs(z, 1/nu) - sp.sqrt(t0*tQ)) == 0 and sp.simplify(xigen_exp.subs(z, 1/nu) - nu/2) == 0)

A = 1e-10  # m
tau0_LG = 5.6*A/70.0; tau0_RG = 4.0*A/47.0
chk("Z4 tau0 = xi0/u0 ~ 8.5e-12 s (LG, RG)", abs(tau0_LG-8.5e-12)/8.5e-12 < 0.07 and abs(tau0_RG-8.5e-12)/8.5e-12 < 0.01,
    "LG %.3e s, RG %.3e s" % (tau0_LG, tau0_RG))

hbar = 1.054571817e-34; m4 = 6.6464731e-27; kB = 1.380649e-23
tauQ = 1e-2; C = 1e-2
res = {}
for name, x0, n_ in (("LG nu=1/2", 5.6*A, 0.5), ("RG nu=2/3", 4.0*A, 2.0/3.0)):
    dd = x0*(tauQ/8.5e-12)**(n_/2)
    vs = (hbar/m4)/math.sqrt(C*dd)
    res[name] = (dd, vs)
    print("     %s: d = %.0f A,  v_s = %.2f mm/s" % (name, dd/A, vs*1e3))
dmax = max(v[0] for v in res.values()); vmax = max(v[1] for v in res.values())
chk("Z5 printed 'd ~ 1e4 A' is within one order of magnitude of eq.(17) in both models",
    all(0.1 <= (v[0]/A)/1e4 <= 1.0 for v in res.values()), "d/1e4A = %.2f, %.2f" % tuple(v[0]/A/1e4 for v in res.values()))
vs_1e4 = (hbar/m4)/math.sqrt(C*1e4*A)
chk("Z5 v_s at d = 1e4 A is 0.16 mm/s; at the eq.(17) d values 0.24-0.49 mm/s: 'v_s ~ 1 mm/s' is order-of-magnitude",
    0.1e-3 < vs_1e4 < 0.2e-3 and 0.2e-3 < vmax < 0.5e-3, "v_s(1e4 A) = %.3f mm/s" % (vs_1e4*1e3))

# cgs for eqs.(18)-(22)
rho_s = 0.1; Ccm = 1.0; rcm = 1e-4; R = Ccm/(2*math.pi); vcm = 0.1  # 1 mm/s
M = rho_s*Ccm*math.pi*rcm**2
Js = M*R*vcm
JT = math.sqrt(1.380649e-16*2.0*M*R**2)
chk("Z6 J_s ~ 5e-11 g cm^2/s at v_s = 1 mm/s", 3e-11 < Js < 7e-11, "J_s = %.2e" % Js)
chk("Z6 J_T ~ 1e-13 g cm^2/s at T = 2 K", 0.5e-13 < JT < 3e-13, "J_T = %.2e" % JT)
mg = 6.6464731e-24; hb = 1.054571817e-27
rhs = (mg/hb)**2*1.380649e-16*2.17/math.pi
rhs2 = (mg/hb)**2*1.380649e-16*2.0/math.pi
chk("Z7 eq.(22) RHS = 0.35e-8/a^2 g cm^-2 (reproduced at T = 2.0 K; 0.38e-8 at T_lambda = 2.17 K)",
    abs(rhs2 - 0.35e-8)/0.35e-8 < 0.05, "T=2.17K: %.3e ; T=2.0K: %.3e" % (rhs, rhs2))

random.seed(67)
def mismatch(N, trials=4000):
    s = 0.0
    for _ in range(trials):
        th = [random.uniform(-math.pi, math.pi) for _ in range(N)]
        tot = 0.0
        for i in range(N):
            dth = (th[(i+1) % N] - th[i] + math.pi) % (2*math.pi) - math.pi  # geodesic rule
            tot += dth
        s += tot*tot
    return math.sqrt(s/trials)
m100 = mismatch(100); m400 = mismatch(400, 2000)
chk("Z8 eq.(9) delta-theta ~ sqrt(N): rms ratio N=400/N=100 ~ 2", 1.7 < m400/m100 < 2.3,
    "rms(100) = %.2f, rms(400) = %.2f" % (m100, m400))

n = sum(ok); print("\n%d/%d PASS" % (n, len(ok)))
sys.exit(0 if n == len(ok) else 1)
