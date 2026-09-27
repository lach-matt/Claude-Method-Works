#!/usr/bin/env python3
"""DOCKET 67 re-derivation for key 1204.3570-seci-friedrichs.

What FFR 1204.3570 Sec. I (p. 2) states, READ at source:
  (i)   smeared normal-ordered operators are, in the first instance, only
        symmetric on a dense domain; more than one self-adjoint extension may exist;
  (ii)  being bounded below (quantum inequalities) they have a distinguished
        Friedrichs extension (Reed-Simon II Thm X.23) whose lower bound coincides
        with the sharpest QI bound; "It is this operator that we have in mind";
  (iii) essential self-adjointness is "nontrivial and not fully resolved";
  (iv)  "If there are distinct self-adjoint extensions, their corresponding
        probability distributions will all share the same moments in the vacuum".
What the tree adds (noise.py:160-162): "a different self-adjoint extension of a
semibounded operator need not keep the Friedrichs lower bound."

Nothing about the QFT operator itself is finite, so the checks below run on the
textbook model where every object is closed-form:
    A = -d^2/dx^2 on C_c^inf(0,inf) in L^2(0,inf), symmetric, A >= 0.
    Friedrichs extension = Dirichlet A_D, spectrum [0, inf).
    Robin extension A_kappa: psi'(0) = -kappa psi(0), kappa > 0.
Checks:
  C1  <psi, A psi> = INT |psi'|^2 >= 0 on the domain (form bound 0).
  C2  Rayleigh quotient of dilated domain vectors -> 0+: form bound 0, not attained.
  C3  Robin boundary form vanishes: A_kappa is symmetric and extends A.
  C4  e_kappa = sqrt(2 kappa) exp(-kappa x): normalised, obeys Robin BC,
      A_kappa e = -kappa^2 e.  A self-adjoint extension with lower bound
      -kappa^2 < 0 = Friedrichs bound: the tree's sentence, CONFIRMED on a model.
  C5  FFR (iv) on the model: phi = x^N exp(-x) lies in D(A_D^n) and D(A_kappa^n)
      for 2n+1 < N; its Dirichlet and Robin spectral measures have the SAME
      moments m_0..m_4 (computed from both spectral resolutions, numerically,
      and against <phi, A^n phi> symbolically), yet the Robin measure puts mass
      w > 0 at -kappa^2, below the Friedrichs bound, where the Dirichlet measure
      puts none.  Equal (finitely many) moments do not fix the support: this is
      why H3 is load-bearing and why FFR's (iv) does not discharge it.
Exit 1 on any failure.
"""
import sys
import sympy as sp
import mpmath as mp

mp.mp.dps = 30
fails = []


def chk(name, ok, detail=""):
    print(("PASS " if ok else "FAIL ") + name + ((" :: " + detail) if detail else ""))
    if not ok:
        fails.append(name)


x, k, s = sp.symbols("x k s", positive=True)
kap = sp.Integer(1)
N = 10
phi = x**N * sp.exp(-x)

# C1
lhs = sp.integrate(phi * (-sp.diff(phi, x, 2)), (x, 0, sp.oo))
rhs = sp.integrate(sp.diff(phi, x)**2, (x, 0, sp.oo))
chk("C1 <phi,A phi> = INT phi'^2 >= 0", sp.simplify(lhs - rhs) == 0 and rhs > 0, "value %s" % rhs)

# C2  dilation psi_s(x) = phi(x/s): quotient scales as 1/s^2
psi_s = phi.subs(x, x / s)
num = sp.integrate(sp.diff(psi_s, x)**2, (x, 0, sp.oo))
den = sp.integrate(psi_s**2, (x, 0, sp.oo))
Q = sp.simplify(num / den)
chk("C2 Rayleigh quotient = c/s^2 -> 0+ (form bound 0, not attained)",
    sp.simplify(Q * s**2).is_positive and sp.limit(Q, s, sp.oo) == 0, "Q(s) = %s" % Q)

# C3  Robin boundary form B(f,g) = [f' g - f g'](0) for real f,g obeying g'(0) = -kappa g(0)
f0, g0, K = sp.symbols("f0 g0 kappa", real=True)
B = (-K * f0) * g0 - f0 * (-K * g0)
chk("C3 Robin boundary form vanishes (symmetric extension)", sp.simplify(B) == 0)
chk("C3b domain vectors obey Robin BC (phi(0)=phi'(0)=0)",
    phi.subs(x, 0) == 0 and sp.diff(phi, x).subs(x, 0) == 0)

# C4
e = sp.sqrt(2 * kap) * sp.exp(-kap * x)
norm = sp.integrate(e**2, (x, 0, sp.oo))
bc = sp.simplify(sp.diff(e, x).subs(x, 0) + kap * e.subs(x, 0))
eig = sp.simplify(-sp.diff(e, x, 2) / e)
chk("C4 Robin eigenvector: norm 1, BC holds, eigenvalue -kappa^2 < 0 (Friedrichs bound 0)",
    norm == 1 and bc == 0 and eig == -kap**2, "eigenvalue %s" % eig)

# C5  moments from the two spectral resolutions
# transform formula INT_0^inf x^N e^{-x} e^{ikx} dx = N!/(1-ik)^{N+1}, checked symbolically at N=3
N3 = sp.integrate(x**3 * sp.exp(-x) * sp.exp(sp.I * k * x), (x, 0, sp.oo), conds="none")
chk("C5a Laplace-Fourier formula at N=3", sp.simplify(N3 - 6 / (1 - sp.I * k)**4) == 0)

fact = mp.factorial(N)


def L(kk):
    return fact / (1 - 1j * kk)**(N + 1)


def dir_amp(kk):  # <sqrt(2/pi) sin(kx), phi>
    return mp.sqrt(2 / mp.pi) * mp.im(L(kk))


def rob_amp(kk):  # <sqrt(2/pi)(k cos kx - kappa sin kx)/sqrt(k^2+kappa^2), phi>
    kf = mp.mpf(1)
    return mp.sqrt(2 / mp.pi) * (kk * mp.re(L(kk)) - kf * mp.im(L(kk))) / mp.sqrt(kk**2 + kf**2)


w = (mp.sqrt(2) * fact / 2**(N + 1))**2  # |<e_kappa, phi>|^2, kappa = 1: INT e^{-2x} x^N = N!/2^{N+1}
direct = [sp.integrate(phi * sp.diff(phi, x, 2 * n) * (-1)**n, (x, 0, sp.oo)) for n in range(5)]
ok_all = True
for n in range(5):
    mD = mp.quad(lambda kk: kk**(2 * n) * dir_amp(kk)**2, [0, 1, 5, 20, mp.inf])
    mR = (-1)**n * w + mp.quad(lambda kk: kk**(2 * n) * rob_amp(kk)**2, [0, 1, 5, 20, mp.inf])
    d = mp.mpf(sp.N(direct[n], 30))
    rel = max(abs(mD - d), abs(mR - d)) / abs(d)
    ok = rel < mp.mpf("1e-15")
    ok_all &= ok
    print("   n=%d  <phi,A^n phi>=%s  Dirichlet=%s  Robin=%s  rel=%s" %
          (n, sp.nsimplify(direct[n]), mp.nstr(mD, 20), mp.nstr(mR, 20), mp.nstr(rel, 3)))
chk("C5b m_0..m_4 identical in the Friedrichs (Dirichlet) and Robin resolutions", ok_all)
chk("C5c Robin measure of phi has atom w>0 at -kappa^2 < 0; Dirichlet measure has no mass below 0",
    w > 0, "w = %s of ||phi||^2 = %s" % (mp.nstr(w, 12), sp.N(direct[0], 12)))

print("\nOUTCOME: %s" % ("ALL PASS" if not fails else "FAILURES: " + ", ".join(fails)))
sys.exit(1 if fails else 0)
