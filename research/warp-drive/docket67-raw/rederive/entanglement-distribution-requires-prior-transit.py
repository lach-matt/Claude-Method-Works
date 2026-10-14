#!/usr/bin/env python3
"""
DOCKET 67 -- re-derivation for 'entanglement-distribution-requires-prior-transit'.

Tree's claim (transit.py:46-49, :154, :251-258): "A Bell pair spanning distance D
required something to cross D at <= c beforehand.  THE CORRIDOR MUST BE TRAVERSED
IN ORDER TO EXIST."  TRAVERSAL_IS_REMOVED = False is declared, no function behind it.

Four checks, each a separate part of the claim:

 C1  THE THEOREM (sympy, exact + numeric):  separable (hence LOCC) operations map
     separable states to separable states.  Symbolic: the Horodecki identity
     [(A(x)B) rho (A(x)B)^dag]^Gamma = (A(x)B^*) rho^Gamma (A(x)B^*)^dag  (eqs 110-111
     of quant-ph/0702225) on generic 2x2 symbols; numeric: random separable states
     under random product-Kraus separable channels stay PPT (2x2: PPT == separable).
 C2  ENTANGLEMENT SWAPPING (sympy, exact): A and D never interact; a Bell
     measurement on (C,B) leaves (A,D) in a Bell state on EACH outcome, but the
     outcome-averaged (A,D) state is I/4 -- separable.  So swapping needs the
     classical outcome to deliver a usable pair; it does not evade C1.
 C3  CAUSAL GEOMETRY (z3, exact over reals): (a) a pair spanning A=(t,0), B=(t,D)
     needs only a COMMON CAUSAL PAST, reachable at t - t_E = D/(2c) from a midpoint
     source, with no single carrier displaced more than D/2 -- 'something crossed D'
     is not required; (b) sat/unsat boundary: t - t_E < D/(2c) is UNSAT;
     (c) if every resource originates at A (Earth) at t=0, any causal chain reaching
     B needs t >= D/c -- the tree's D/c minimum is recovered under THAT hypothesis.
 C4  VACUUM HARVESTING (numeric, from the Wightman function Reznik prints,
     quant-ph/0212044 p.9): two pointlike detectors, Gaussian switching
     chi(t)=exp(-t^2/T^2), massless scalar, 3+1, leading order.  Negativity
     estimator N = |M| - L (Pozas-Kerstjens & Martin-Martinez eq. 68).  L and M are
     computed here from first principles (k-integral and principal-value integral),
     not copied.  Shows N > 0 at separations beyond the Gaussian light-cone estimate
     d > 7T/sqrt2 (their Fig.1 caption) for a tuned gap, and the size of the best N
     as d/T grows.  No carrier crosses; the entanglement pre-exists in the field.
"""
import sys, math, itertools, random
import sympy as sp
import numpy as np
import mpmath as mp

bad = 0
def chk(label, ok, detail=""):
    global bad
    print(("PASS " if ok else "FAIL ") + label + (("   " + detail) if detail else ""))
    if not ok:
        bad += 1

# ---------------------------------------------------------------- helpers
def ptrans_B(r, dA=2, dB=2):
    """Partial transpose on subsystem B of a (dA*dB)x(dA*dB) matrix (sympy or numpy)."""
    if isinstance(r, np.ndarray):
        R = r.reshape(dA, dB, dA, dB)
        return R.transpose(0, 3, 2, 1).reshape(dA*dB, dA*dB)
    out = sp.zeros(dA*dB, dA*dB)
    for i, j, k, l in itertools.product(range(dA), range(dB), range(dA), range(dB)):
        out[i*dB + l, k*dB + j] = r[i*dB + j, k*dB + l]
    return out

# ================================================================ C1
print("C1  separable operations preserve separability")
a = sp.Matrix(2, 2, sp.symbols('a0:4'))
b = sp.Matrix(2, 2, sp.symbols('b0:4'))
rho = sp.Matrix(4, 4, sp.symbols('r0:16'))
lhs = ptrans_B(sp.kronecker_product(a, b) * rho * sp.kronecker_product(a, b).H)
rhs = sp.kronecker_product(a, b.conjugate()) * ptrans_B(rho) * sp.kronecker_product(a, b.conjugate()).H
chk("Horodecki eq.(110)-(111) identity, generic symbols", sp.simplify(sp.expand(lhs - rhs)) == sp.zeros(4, 4))

rng = np.random.default_rng(67)
def rand_state(d):
    g = rng.normal(size=(d, d)) + 1j*rng.normal(size=(d, d)); r = g @ g.conj().T; return r/np.trace(r)
def rand_sep():
    ps = rng.dirichlet(np.ones(4))
    return sum(p*np.kron(rand_state(2), rand_state(2)) for p in ps)
def rand_product_kraus(n=3):
    """A separable channel sum_i (A_i x B_i) . (A_i x B_i)^dag, normalised to trace preserving."""
    K = [np.kron(rng.normal(size=(2, 2)) + 1j*rng.normal(size=(2, 2)),
                 rng.normal(size=(2, 2)) + 1j*rng.normal(size=(2, 2))) for _ in range(n)]
    return K, None
worst = 1e9
for _ in range(2000):
    r = rand_sep()
    K, _Sm = rand_product_kraus()
    out = sum(k @ r @ k.conj().T for k in K); out = out/np.trace(out)   # trace-nonincreasing + renormalise (SLOCC-type)
    worst = min(worst, np.linalg.eigvalsh(ptrans_B(out)).min())
chk("2000 random separable states x random product-Kraus maps stay PPT (2x2: PPT==separable)",
    worst > -1e-12, "min PT eigenvalue %.3e" % worst)
bell = np.array([1, 0, 0, 1])/math.sqrt(2)
chk("control: Bell state is NPT (min PT eig = -1/2)",
    abs(np.linalg.eigvalsh(ptrans_B(np.outer(bell, bell))).min() + 0.5) < 1e-12)

# ================================================================ C2
print("\nC2  entanglement swapping: A and D never interact")
s2 = 1/sp.sqrt(2)
k0, k1 = sp.Matrix([1, 0]), sp.Matrix([0, 1])
def kr(*vs):
    out = vs[0]
    for v in vs[1:]:
        out = sp.kronecker_product(out, v)
    return out
phi_p = s2*(kr(k0, k0) + kr(k1, k1)); phi_m = s2*(kr(k0, k0) - kr(k1, k1))
psi_p = s2*(kr(k0, k1) + kr(k1, k0)); psi_m = s2*(kr(k0, k1) - kr(k1, k0))
bells = {"phi+": phi_p, "phi-": phi_m, "psi+": psi_p, "psi-": psi_m}
# ordering A, C, B, D : |phi+>_AC |phi+>_BD
state = kr(phi_p, phi_p)
def reorder_ACBD_to_A_CB_D(v):
    # v index (a,c,b,d) -> keep ordering; measurement acts on qubits 2,3 (C,B)
    return v
avg = sp.zeros(4, 4); ok_each = True; probs = []
I2 = sp.eye(2)
for name, bv in bells.items():
    P = kr(I2, bv*bv.H, I2)             # projector on (C,B)
    post = P*state
    p = sp.simplify((post.H*post)[0])
    probs.append(p)
    # extract (A,D) state: contract C,B with <bv|
    ad = sp.zeros(4, 1)
    for a_ in range(2):
        for d_ in range(2):
            amp = 0
            for c_ in range(2):
                for b_ in range(2):
                    amp += sp.conjugate(bv[c_*2 + b_]) * state[a_*8 + c_*4 + b_*2 + d_]
            ad[a_*2 + d_] = amp
    ad = ad/sp.sqrt(p)
    rAD = sp.simplify(ad*ad.H)
    ev = [sp.nsimplify(e) for e in ptrans_B(rAD).eigenvals().keys()]
    ok_each &= (min(ev) == sp.Rational(-1, 2))
    avg += p*rAD
chk("each of the 4 outcomes has probability 1/4", all(sp.simplify(p - sp.Rational(1, 4)) == 0 for p in probs))
chk("each outcome leaves (A,D) maximally entangled (min PT eig = -1/2)", ok_each)
chk("outcome-averaged (A,D) state = I/4 (separable): the outcome must be communicated",
    sp.simplify(avg - sp.eye(4)/4) == sp.zeros(4, 4))

# ================================================================ C3
print("\nC3  causal geometry of a pair spanning D (units c = 1)")
import z3
tE, xE, t, D = z3.Reals('tE xE t D')
s = z3.Solver()
# event E=(tE,xE) whose future cone contains A=(t,0) and B=(t,D)
cone = z3.And(t - tE >= z3.If(xE >= 0, xE, -xE), t - tE >= z3.If(D - xE >= 0, D - xE, xE - D))
s.push(); s.add(D > 0, cone, t - tE == D/2, xE == D/2)
chk("(a) midpoint source reaches both ends at t - tE = D/2 (sat)", s.check() == z3.sat); s.pop()
s.push(); s.add(D > 0, cone, t - tE < D/2)
chk("(b) no common causal past with t - tE < D/2 (unsat)", s.check() == z3.unsat); s.pop()
s.push(); s.add(D > 0, cone, xE == D/2, z3.Or(xE - 0 > D/2, D - xE > D/2))
chk("    midpoint source: no carrier displaced more than D/2 (unsat)", s.check() == z3.unsat); s.pop()
# (c) all resources originate at A at t=0: E must itself be in the causal future of (0,0)
s.push(); s.add(D > 0, cone, tE >= z3.If(xE >= 0, xE, -xE), t < D)
chk("(c) resources originating at A=(0,0): t < D is unsat, so t >= D/c", s.check() == z3.unsat); s.pop()
s.push(); s.add(D > 0, cone, tE >= z3.If(xE >= 0, xE, -xE), t == D)
chk("    ... and t = D/c is attained (sat)", s.check() == z3.sat); s.pop()

# ================================================================ C4
print("\nC4  entanglement harvesting from the massless vacuum (lambda^2 factored out, T = 1)")
mp.mp.dps = 30
def L_local(Om, T=1):
    # L = int d^3k/((2pi)^3 2k) |chi~(Om+k)|^2,  chi~(w) = sqrt(pi) T exp(-w^2 T^2/4)
    f = lambda k: k*mp.pi*T**2*mp.e**(-(Om + k)**2*T**2/2)
    return mp.quad(f, [0, mp.inf])/(4*mp.pi**2)
def M_nonlocal(Om, d, T=1):
    # M = -int dt int dt' chi chi e^{i Om (t+t')} G_F(t-t', d),
    # G_F = 1/(4 pi^2 (d^2 - s^2 + i0))  (time-ordered form of Reznik's D+, p.9)
    pref = -mp.sqrt(2*mp.pi)*T*mp.e**(-Om**2*T**2/2)/2/(4*mp.pi**2)
    g = lambda s: mp.e**(-s**2/(2*T**2))
    # principal value of int g(s)/(d^2-s^2) ds  (even integrand): 2 * PV int_0^inf
    # PV int_0^inf ds/(d^2-s^2) = 0 exactly, so subtracting g(d) changes nothing and
    # leaves a regular integrand at s = d
    pv = 2*mp.quad(lambda s: (g(s) - g(d))/(d**2 - s**2), [0, d, 2*d, mp.inf])
    delta = -1j*mp.pi*g(d)/d          # -i pi * sum over s=+-d of g/(2d)
    return pref*(pv + delta)
def N2(Om, d):
    return abs(M_nonlocal(Om, d)) - L_local(Om)

light = 7/math.sqrt(2)   # Pozas-Kerstjens Fig.1 caption: effective light-cone edge for Gaussian switching
rows = []
for d in [1.0, 3.0, 5.0, 6.0, 8.0]:
    best = None
    for Om in [x*0.5 for x in range(0, 61)]:
        n = N2(Om, d)
        if best is None or n > best[1]:
            best = (Om, n)
    rows.append((d, best))
    print("   d/T = %4.1f  %-9s best N(2) = %+.3e at Omega T = %4.1f" %
          (d, "SPACELIKE" if d > light else "", float(best[1]), best[0]))
chk("harvesting N(2) > 0 at d/T = 5, 6, 8 (beyond the 7T/sqrt2 = %.2f light-cone estimate)" % light,
    all(r[1][1] > 0 for r in rows if r[0] > light))
chk("best harvested N(2) falls by > 10 orders from d/T = 1 to 8",
    float(rows[0][1][1]/rows[-1][1][1]) > 1e10,
    "ratio %.2e" % float(rows[0][1][1]/rows[-1][1][1]))
# Large-d asymptotics from the closed forms: L ~ e^{-W^2/2}/(4 pi^2 W^2) for W = Om T >> 1;
# |M| ~ e^{-W^2/2} * sqrt(2pi)/(8 pi^2) * |PV| with |PV| ~ 2 T^2/d^2 for d >> T,
# so N > 0 needs W^2 ~> d^2/(2 sqrt(2 pi) T^2)... check the scaling numerically:
Wmin = []
for d in [6.0, 8.0, 10.0]:
    W = 0.0
    while N2(W, d) <= 0 and W < 40:
        W += 0.25
    Wmin.append((d, W))
print("   minimum gap for N(2)>0:", ", ".join("d/T=%.0f -> Omega T=%.2f" % x for x in Wmin))
chk("the gap needed grows linearly with d/T (Omega T / (d/T) within 30 pct across d/T = 6..10)",
    max(w/d for d, w in Wmin)/min(w/d for d, w in Wmin) < 1.3)
# Proxima with T chosen so the detectors are spacelike: d/T > 7/sqrt2 needs T < D/(4.95 c)
LY = 9.4607304725808e15; PROXIMA_M = 4.0175e16   # transit.py DISTANCES value
light_time_yr = PROXIMA_M/2.99792458e8/3.15576e7
print("   Proxima light time %.3f yr; spacelike harvesting needs switching width T < %.3f yr"
      % (light_time_yr, light_time_yr/light))
print("   => the detectors must couple for ~a year-scale window to harvest at Proxima: the interaction "
      "time is comparable to the light time, and N ~ exp(-Omega^2 T^2/2) is tiny.")

print("\n" + ("ALL PASS" if bad == 0 else "FAILURES: %d" % bad))
sys.exit(1 if bad else 0)
