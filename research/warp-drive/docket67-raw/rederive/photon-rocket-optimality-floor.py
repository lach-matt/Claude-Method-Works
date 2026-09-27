#!/usr/bin/env python3
"""
DOCKET 67 re-derivation: photon-rocket-optimality-floor.

Tree claim (research/warp-drive/arrival.py:13):
    "This is a floor: no propulsion does better per unit energy."
Quantity the tree reports and rests on (arrival.py:121-128, 160-161, shipspec.py:142):
    the REST-MASS ratio M0/M1 = sqrt((1+b)/(1-b)) at 100% conversion.

Units c = 1.  Checks:
  C1 (z3, sympy)  Rest-mass floor as a THEOREM for an isolated body whose only momentum
                  change is emission with total 4-momentum future-causal:
                      M0/M1 >= gamma(1+beta), equality iff exhaust null and anti-collinear.
                  No exhaust-speed profile, staging or history assumption is used.
  C2 (sympy)      Thrust per unit jet power for exhaust speed u (rest frame):
                      T/P = gamma_u u / (gamma_u - 1) >= 1, equality only at u = 1.
                  Photon exhaust carries the LEAST momentum per unit liberated energy.
  C3 (numeric)    Liberated energy (rest mass converted to exhaust kinetic energy) for a
                  fixed-u self-contained rocket:  E_lib(u) = (1 - 1/gamma_u)(e^{chi/u} - 1) M1,
                  chi = artanh(beta).  Minimise over u and compare with the photon rocket
                  E_lib(1) = (e^chi - 1) M1.  A u < 1 that liberates less energy is a
                  counterexample to the sentence under the 'energy liberated' reading.
  C4 (sympy)      Universal lower bound on liberated energy for ANY self-contained rocket:
                  E_lib >= (gamma - 1) M1 (energy conservation, E_i >= mu_i per element);
                  the photon rocket exceeds it by exactly gamma*beta*M1.
  C5 (numeric)    Independent stepwise 4-momentum integration of a fixed-u rocket: mass ratio
                  and liberated energy agree with the closed forms of C3.
  C6 (numeric)    Tree numbers resting on the claim (recorded, never repaired).
Exit 0 iff every check that is asserted passes.
"""
import math, sys
import sympy as sp

ok = True
def check(label, cond):
    global ok
    ok &= bool(cond)
    print("  [%s] %s" % ("ok" if cond else "FAIL", label))

# ---------------------------------------------------------------- C1
print("C1  rest-mass floor for an isolated self-contained emitter")
try:
    import z3
    M0, M1, g, b, E, p = z3.Reals("M0 M1 g b E p")
    s = z3.Solver()
    s.add(M1 > 0, g >= 1, b >= 0, b < 1, g*g*(1 - b*b) == 1)
    s.add(E >= 0, E*E >= p*p)                 # total exhaust 4-momentum future causal
    s.add(M0 == g*M1 + E, 0 == g*b*M1 + p)    # 4-momentum conservation, initial rest frame
    s.add(M0 < g*(1 + b)*M1)                  # negation of the floor
    r = s.check()
    print("    z3: negation of M0 >= gamma(1+beta) M1 is", r)
    check("z3 proves M0/M1 >= gamma(1+beta) (negation unsat)", r == z3.unsat)
    # equality case requires E = |p| (null total exhaust momentum)
    s2 = z3.Solver()
    s2.add(M1 > 0, g >= 1, b > 0, b < 1, g*g*(1 - b*b) == 1, E >= 0, E*E >= p*p,
           M0 == g*M1 + E, 0 == g*b*M1 + p, M0 == g*(1 + b)*M1, E*E > p*p)
    r2 = s2.check()
    check("z3: equality forces null total exhaust momentum (E>|p| with equality unsat)", r2 == z3.unsat)
    # a SUM of future-causal vectors is future causal (1+1 D suffices for the bound: transverse
    # components only raise E relative to |p_parallel|)
    E1, p1, E2, p2 = z3.Reals("E1 p1 E2 p2")
    s3 = z3.Solver()
    s3.add(E1 >= 0, E1*E1 >= p1*p1, E2 >= 0, E2*E2 >= p2*p2,
           z3.Not(z3.And(E1 + E2 >= 0, (E1 + E2)**2 >= (p1 + p2)**2)))
    check("z3: sum of two future-causal (E,p) is future causal (induction step)", s3.check() == z3.unsat)
except ImportError:
    print("    z3 not installed -- pip install z3-solver ; C1 z3 part NOT RUN")
    ok = False
bs = sp.symbols("beta", positive=True)
gs = 1/sp.sqrt(1 - bs**2)
check("sympy: gamma(1+beta) == sqrt((1+beta)/(1-beta)) == exp(artanh beta)",
      all(abs(float((gs*(1+bs) - sp.sqrt((1+bs)/(1-bs))).subs(bs, v))) < 1e-14 and
          abs(float((gs*(1+bs) - sp.exp(sp.atanh(bs))).subs(bs, v))) < 1e-13
          for v in (sp.Rational(1, 100), sp.Rational(476, 10000), sp.Rational(866, 1000), sp.Rational(99, 100))))

# ---------------------------------------------------------------- C2
print("\nC2  thrust per unit jet power, exhaust speed u in the instantaneous rest frame")
u = sp.symbols("u", positive=True)
gu = 1/sp.sqrt(1 - u**2)
TP = sp.simplify(gu*u/(gu - 1))       # momentum / kinetic energy of an exhaust element
print("    T/P(u) =", TP, "  (c = 1; photon limit u->1:", sp.limit(TP, u, 1, "-"), ")")
# T/P >= 1  <=>  1 - sqrt(1-u^2) <= u  <=>  sqrt(1-u^2) >= 1-u, true on (0,1]
diff = sp.simplify(sp.sqrt(1 - u**2) - (1 - u))
grid = [k/1000 for k in range(1, 1000)]
check("T/P(u) > 1 for every u in (0,1) on a 999-point grid",
      all(float(TP.subs(u, v)) > 1 for v in grid))
check("sqrt(1-u^2) - (1-u) = sqrt(1-u)(sqrt(1+u)-sqrt(1-u)) >= 0 (sympy identity)",
      sp.simplify(diff - sp.sqrt(1-u)*(sp.sqrt(1+u) - sp.sqrt(1-u))) == 0)
check("T/P -> 2/u as u -> 0 (Newtonian 2/v_e)", sp.limit(TP*u, u, 0) == 2)
print("    at u = 0.03: T/P = %.2f  (photon: 1.00)" % float(TP.subs(u, 0.03)))

# ---------------------------------------------------------------- C3
print("\nC3  liberated energy E_lib/M1 for fixed-u self-contained rockets vs the photon rocket")
def elib(beta, uu):
    chi = math.atanh(beta)
    f = 1.0 - math.sqrt(1.0 - uu*uu)
    x = chi/uu
    if x > 700: return float("inf")
    return f*(math.exp(x) - 1.0)
def mratio(beta, uu):
    return math.exp(math.atanh(beta)/uu)
def argmin_u(beta):
    best = (float("inf"), None)
    for k in range(1, 100000):
        uu = k/100000
        e = elib(beta, uu)
        if e < best[0]: best = (e, uu)
    return best
rows = []
print("    %-7s %12s %12s %9s %10s %12s %10s" % ("beta", "photon E", "best-u E", "u*", "photon/best", "M0/M1 at u*", "KE=(g-1)"))
for beta in (0.0476, 0.100, 0.316, 0.622, 0.866, 0.99):
    ep = elib(beta, 1.0)
    eb, ub = argmin_u(beta)
    ke = 1/math.sqrt(1 - beta*beta) - 1
    rows.append((beta, ep, eb, ub, mratio(beta, ub), ke))
    print("    %-7.4f %12.6f %12.6f %9.5f %10.2f %12.4f %10.6f" % (beta, ep, eb, ub, ep/eb, mratio(beta, ub), ke))
check("photon rocket E_lib = e^chi - 1 = gamma(1+beta) - 1 at beta=0.866 (2.7317)",
      abs(elib(0.866, 1.0) - 2.7316716) < 1e-6)
check("COUNTEREXAMPLE (energy-liberated reading): at every tree beta some u<1 liberates LESS energy than the photon rocket",
      all(eb < ep and ub < 1.0 for (_, ep, eb, ub, _, _) in rows))
b0 = rows[0]
print("    shell beta 0.0476: photon liberates %.5f M1 c^2; u=%.4f liberates %.5f M1 c^2 (%.1fx less) at mass ratio %.3f"
      % (b0[1], b0[3], b0[2], b0[1]/b0[2], b0[4]))
b4 = rows[4]
print("    engine beta 0.866: photon liberates %.4f M1 c^2; u=%.4f liberates %.4f M1 c^2 (%.2fx less) at mass ratio %.3f"
      % (b4[1], b4[3], b4[2], b4[1]/b4[2], b4[4]))
check("the SAME u<1 rockets have a LARGER rest-mass ratio than the photon rocket (rest-mass floor intact)",
      all(mr > math.exp(math.atanh(beta)) for (beta, _, _, _, mr, _) in rows))

# ---------------------------------------------------------------- C4
print("\nC4  universal floor on liberated energy for any self-contained rocket")
# M0 = gamma M1 + sum E_i ; E_lib = (M0 - M1) - sum mu_i = (gamma-1) M1 + sum (E_i - mu_i) >= (gamma-1) M1
Ms, Esum, musum = sp.symbols("M1 Esum musum", positive=True)
M0s = gs*Ms + Esum
Elib = (M0s - Ms) - musum
check("sympy: E_lib - (gamma-1)M1 == sum(E_i - mu_i)  (>= 0 since E_i >= mu_i)",
      sp.simplify(Elib - (gs - 1)*Ms - (Esum - musum)) == 0)
excess = sp.simplify((gs*(1 + bs) - 1) - (gs - 1))
check("sympy: photon E_lib exceeds the (gamma-1)M1 floor by exactly gamma*beta*M1", sp.simplify(excess - gs*bs) == 0)
check("every fixed-u optimum sits above the (gamma-1) floor (consistency)",
      all(eb >= ke - 1e-12 for (_, _, eb, _, _, ke) in rows))
# Le 2606.22531v4 (cached, line 506): fixed-frame radiated energy m_i - m_f cosh d != m_i - m_f
for beta in (0.0476, 0.866):
    d = math.atanh(beta); mi = math.exp(d)
    print("    beta %.4f: invariant depletion m_i-m_f = %.6f ; fixed-frame radiated m_i - m_f cosh d = %.6f"
          % (beta, mi - 1, mi - math.cosh(d)))

# ---------------------------------------------------------------- C5
print("\nC5  independent stepwise 4-momentum integration (fixed u), no closed form used")
def simulate(beta_target, uu, n=200000):
    # accelerate from rest to beta_target (braking is its time reverse); track lab (E,P) of the
    # ship and of the exhaust, and the liberated energy sum dM(1-1/gamma_u)
    E, P = 1.0, 0.0            # start with rest mass 1, rescale at the end
    chi_t = math.atanh(beta_target)
    gU = 1/math.sqrt(1 - uu*uu)
    elib_sum = 0.0
    dchi = chi_t/n
    for _ in range(n):
        M = math.sqrt(E*E - P*P)
        chi = math.atanh(P/E)
        # rest frame: eject mu at speed u backward, ship gains rapidity dchi; exact per step:
        # M -> M' with M'*sinh(dchi) = mu*gU*u, M = M'*cosh(dchi) + mu*gU
        Mp = M/(math.cosh(dchi) + math.sinh(dchi)/uu)
        mu = Mp*math.sinh(dchi)/(gU*uu)
        elib_sum += (M - Mp) - mu
        chi_new = chi + dchi
        E, P = Mp*math.cosh(chi_new), Mp*math.sinh(chi_new)
    Mf = math.sqrt(E*E - P*P)
    return 1.0/Mf, elib_sum/Mf
for beta, uu in ((0.0476, rows[0][3]), (0.866, rows[4][3]), (0.866, 0.5)):
    mr_s, el_s = simulate(beta, uu)
    mr_c, el_c = mratio(beta, uu), elib(beta, uu)
    rel = max(abs(mr_s/mr_c - 1), abs(el_s/el_c - 1))
    print("    beta %.4f u %.5f: sim M0/M1 %.8f vs %.8f ; sim E_lib %.8f vs %.8f ; rel %.1e"
          % (beta, uu, mr_s, mr_c, el_s, el_c, rel))
    check("stepwise integration agrees with closed form (rel < 1e-4) at beta %.4f u %.5f" % (beta, uu), rel < 1e-4)

# ---------------------------------------------------------------- C6
print("\nC6  tree numbers resting on the claim (discrepancies recorded, not repaired)")
r1, r2 = math.exp(math.atanh(0.0476)), math.exp(math.atanh(0.866))
print("    M0/M1 at 0.0476 = %.7f (arrival.py:75 1.0487888) ; at 0.866 = %.7f (shipspec.py:142 3.7314; gamma=2 exact 2+sqrt3 = %.7f)"
      % (r1, r2, 2 + math.sqrt(3)))
print("    fuel/tonne 0.866 vs 0.0476 = %.3f ; mass-ratio ratio = %.3f ; arrival.py:137 says '76x'" % ((r2-1)/(r1-1), r2/r1))
print("    speed ratio = %.2f (arrival.py:137 '18x')" % (0.866/0.0476))
check("3.7314 is within the 1e-4 selftest tolerance of the computed 3.7317 (discrepancy 7e-5, recorded)",
      abs(3.7314/r2 - 1) < 1e-4)

# ---------------------------------------------------------------- C7
print("\nC7  consumer outside the canonical owner: warpdrive.py:838-842, 1901 (recorded, not graded here)")
# warpdrive.py models fuel(eff) = floor/eff, floor = M(sqrt((1+b)/(1-b)) - 1), b = 0.0378,
# and asserts fuel(0.004*0.501)/fuel(1) > 100.  Relativistic rocket equation instead: a source
# converting fraction eff of propellant rest mass into exhaust kinetic energy, all propellant
# ejected, ideal nozzle => 1 - 1/gamma_u = eff, M0/M1 = exp(artanh(b)/u).
bw, eff = 0.0378, 0.004*0.501
uf = math.sqrt(1 - (1 - eff)**2)
fuel_re = math.exp(math.atanh(bw)/uf) - 1
floor_w = math.sqrt((1 + bw)/(1 - bw)) - 1
print("    eff %.5f -> ideal exhaust u = %.4f c ; rocket-equation fuel/M = %.4f ; floor/M = %.5f"
      % (eff, uf, fuel_re, floor_w))
print("    rocket-equation fuel ratio vs photon floor = %.1f ; warpdrive.py floor/eff model = %.1f"
      % (fuel_re/floor_w, 1/eff))
check("fusion-powered (ideal nozzle) is still WORSE than the photon floor in rest mass (qualitative claim holds)",
      fuel_re > floor_w)
print("    -> the '> 100' factor at warpdrive.py:1901 holds only under the floor/eff model; the"
      " rocket equation gives %.1f (discrepancy recorded, not a check of this key)" % (fuel_re/floor_w))

print("\nRE-DERIVATION %s" % ("OK" if ok else "FAILED"))
sys.exit(0 if ok else 1)
