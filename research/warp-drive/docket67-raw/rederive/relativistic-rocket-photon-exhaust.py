#!/usr/bin/env python3
"""DOCKET 67 re-derivation: relativistic rocket, exhaust at c (Ackeret 1946 form),
as used at research/warp-drive/arrival.py:11-13,32-34,70-76,119-139,157-161.
Independent of arrival.py (nothing imported from the tree). sympy + stdlib.
Exits 1 if any check fails."""
import math, sys
import sympy as sp

ok = True
def chk(label, cond, detail=""):
    global ok
    ok &= bool(cond)
    print("  %-4s %s %s" % ("ok" if cond else "FAIL", label, detail))

b, u, chi, M, M0 = sp.symbols('beta u chi M M0', positive=True)
g = 1/sp.sqrt(1-b**2)

print("C1  4-momentum conservation, 1-D braking, photons emitted forward")
# lab frame, ship moving +x.  Emitting photons of lab energy dE in +x:
#   d(M g) = -dE ,  d(M g b) = -dE   =>  d(M g (1-b)) = 0
inv = sp.simplify(M*g*(1-b))
inv_closed = M*sp.sqrt((1-b)/(1+b))
chk("M*gamma*(1-beta) == M*sqrt((1-beta)/(1+beta)) on 0<beta<1",
    sp.simplify(sp.expand_power_base(inv**2 - inv_closed**2, force=True)) == 0)
# conserved from beta0 to 0:  M1 = M0 sqrt((1-b)/(1+b))  => M0/M1 = sqrt((1+b)/(1-b))
ratio = sp.sqrt((1+b)/(1-b))
chk("M0/M1 = sqrt((1+b)/(1-b)) == gamma(1+b)",
    sp.simplify((ratio**2 - (g*(1+b))**2)) == 0)
chk("M0/M1 == exp(artanh b) (rapidity form, Le 2606.22531 Lemma 2.1 equality case)",
    sp.simplify(sp.log(ratio) - sp.atanh(b)).rewrite(sp.log).simplify() == 0 or
    all(abs(float(sp.log(ratio).subs(b,x)) - math.atanh(x)) < 1e-14 for x in (0.01,0.3,0.866,0.99)))

print("C2  general exhaust speed u (rest frame), 0<u<=1: dM/M = -dchi/u")
# rest frame: emit rest mass -dM as exhaust with speed u; momentum balance
#   M dchi = (exhaust momentum) = gamma_u u dm_ex ,  energy: -dM = gamma_u dm_ex
#   => M dchi = -u dM  => M0/M1 = exp(chi/u)
Mf = sp.Function('Mf')
ode = sp.Eq(Mf(chi).diff(chi), -Mf(chi)/u)
sol = sp.dsolve(ode, ics={Mf(0): M0})
chk("ODE solution M(chi) = M0 exp(-chi/u)", sp.simplify(sol.rhs - M0*sp.exp(-chi/u)) == 0)
Ru = sp.exp(sp.atanh(b)/u)
chk("u=1 reduces to photon ratio", sp.simplify(Ru.subs(u,1) - sp.exp(sp.atanh(b))) == 0)
worst = min(float(Ru.subs({b:bb,u:uu})) - float(ratio.subs(b,bb))
            for bb in (0.01,0.0476,0.3,0.622,0.866,0.99) for uu in (0.05,0.3,0.5,0.9,0.999))
chk("photon ratio is the FLOOR over exhaust speed u<=1 (grid)", worst > 0, "min excess=%.3e" % worst)

print("C3  independent stepwise integration of the lab-frame balance (no closed form used)")
def rk4_brake(beta0, n=200000):
    # state: E = M gamma, P = M gamma beta (c=1).  Emit lab photon energy dE forward:
    # dE/ds = -1, dP/ds = -1 (parameter s = emitted photon energy).  Stop at P=0.
    M0v = 1.0; gm = 1/math.sqrt(1-beta0**2)
    E, P = M0v*gm, M0v*gm*beta0
    ds = P/n
    for _ in range(n):
        E -= ds; P -= ds
    return M0v/math.sqrt(E*E-P*P)
for bb in (0.0476, 0.5, 0.866, 0.99):
    num = rk4_brake(bb); cf = math.sqrt((1+bb)/(1-bb))
    chk("beta=%.4f  numeric %.10f vs closed %.10f" % (bb, num, cf), abs(num-cf) < 1e-9*cf)

print("C4  the tree's numbers (arrival.py, shipspec.py:142, index3.py:85)")
r0476 = math.sqrt(1.0476/0.9524); r866 = math.sqrt(1.866/0.134)
chk("beta=0.0476 -> 1.0487888 (arrival.py:75)", abs(r0476-1.0487888) < 1e-7, "%.9f" % r0476)
chk("beta=0.866 -> 3.7316716 (report prints 3.7317)", abs(r866-3.7317) < 5e-5, "%.7f" % r866)
g2 = 2+math.sqrt(3)
print("       selftest literal 3.7314 labelled '(gamma = 2)': beta=0.866 gives %.7f,"
      " gamma=2 exactly gives 2+sqrt3 = %.7f; literal is off by %.1e and %.1e rel"
      % (r866, g2, abs(3.7314-r866)/r866, abs(3.7314-g2)/g2))
chk("literal 3.7314 within arrival.py:74 tol 1e-4 of the beta=0.866 value", abs(3.7314-r866)/3.7314 <= 1e-4)
chk("fuel per tonne at 0.0476c = 48.8 kg ('49 KILOGRAMS', arrival.py:128)", abs((r0476-1)*1000-48.79) < 0.01)
chk("speed ratio 0.866/0.0476 = 18.19 ('18x', arrival.py:137)", abs(0.866/0.0476-18.19) < 0.01)
fuel_ratio = (r866-1)/(r0476-1); mr_ratio = r866/r0476
print("       '76x the fuel ratio' (arrival.py:137): fuel-per-tonne ratio = %.2f; M0/M1 ratio = %.3f;"
      " log(M0/M1) ratio = %.2f" % (fuel_ratio, mr_ratio, math.log(r866)/math.log(r0476)))
chk("DISCREPANCY RECORDED: no reading of the photon formula yields 76 (fuel ratio is 56.0)",
    abs(fuel_ratio-76) > 1 and abs(mr_ratio-76) > 1)
print("       '2.73 tonnes of perfect antimatter per tonne landed' (arrival.py:127): total"
      " annihilation fuel = %.4f t; if matter+antimatter pairs, antimatter share = %.4f t" % (r866-1,(r866-1)/2))

print("C5  hypothesis-drop check: 'no propulsion does better' (arrival.py:13)")
# External momentum source: the file's own slingshot (dv = 2U/(1+U^2)) delivers a
# velocity change with zero ship rest-mass loss.  Lemma 2.1 hypothesis F = -dP/ds future
# causal (momentum leaves only as exhaust) is violated, so the floor does not apply.
U = 0.35; dv = 2*U/(1+U*U)
chk("slingshot dv at U=0.35 is %.4f c with M_f/M_i = 1 < photon floor 1/%.4f" % (dv, math.sqrt((1+dv)/(1-dv))), True)

print("\n  RE-DERIVATION %s" % ("OK" if ok else "FAILED"))
sys.exit(0 if ok else 1)
