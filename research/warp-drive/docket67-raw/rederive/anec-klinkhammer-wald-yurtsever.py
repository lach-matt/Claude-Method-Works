#!/usr/bin/env python3
"""
DOCKET 67 -- re-derivation for key 'anec-klinkhammer-wald-yurtsever'.

The tree (bounds.py:147-149, 44/296, 96) uses: "ANEC over a COMPLETE null
geodesic holds (Klinkhammer; Wald & Yurtsever ...)", coded K=0 (known saturated,
"by the vacuum along a complete null geodesic").

Klinkhammer PRD 43 2542 (1991) and Wald-Yurtsever PRD 44 403 (1991) have no
arXiv copy; they are read via restatements (Fewster-Roman gr-qc/0209036 Sec.IID,
Fewster-Olum-Pfenning gr-qc/0609007 Sec.I, Kontou-Sanders 2003.01815 Sec.4.3,
Visser gr-qc/9409043, Graham-Olum 0705.3193).  What is finite or closed form is
checked here:

  A  (sympy)  For a free scalar with ANY curvature coupling xi in flat space,
              k^a k^b T_ab = (k.dphi)^2 - xi (k.d)^2 (phi^2): the xi term is a
              total lambda-derivative along the null line, so the ANEC integral
              is xi-independent (FOP's restatement: Klinkhammer holds "with
              arbitrary curvature coupling").
  B  (numeric) Klinkhammer's mechanism in a finite-mode model of the 4D
              Minkowski massless scalar restricted to a null line: the windowed
              null-energy operator Q_L = int w_L :(d_lambda phi)^2: has negative
              spectrum for finite window L (no null QI -- Fewster-Roman), the
              vacuum expectation is exactly 0, and min spec Q_L -> 0^- as
              L -> infinity (ANEC >= 0, saturated at 0 by the vacuum).
              A MODEL CHECK in a truncated Fock space, not a proof.
  C  (sympy)  Fewster-Roman's own explicit states (nu=1, step B, eq. II.26-27):
              the ANEC value is  N^2 a^{2s-7} (2pi)^-4 * 2pi f(0) C * 2 L0^7/105
              > 0 and -> 0 as alpha -> 0 (sigma = 3.75), while the segment
              average rho_2 ~ -alpha^{sigma-4} -> -infinity.
  D  (sympy)  Urban-Olum 0910.5925 Sec.III: re-derive eqs (39)-(42) from (37),
              (38): in a conformally (and asymptotically) flat 4D spacetime
              the conformally coupled scalar in the (conformal) vacuum has
              ANEC integral (ab - 2a^2) 16 beta sqrt(2 pi)/r^3 with
              beta = -1/(5760 pi^2) < 0: NEGATIVE for b > 2a, on a complete
              ACHRONAL null geodesic.  So the flat background is load-bearing
              for both "holds" and "saturated by the vacuum".

Exit 0 iff every check agrees with the source.
"""
import sys
import numpy as np
import sympy as sp

ok_all = True


def chk(name, cond, detail=""):
    global ok_all
    ok_all &= bool(cond)
    print("  [%s] %s %s" % ("ok" if cond else "XX", name, detail))


# ---------------------------------------------------------------- A
print("A. null contraction of the xi-coupled scalar stress tensor (flat)")
t, x, y, z, xi = sp.symbols("t x y z xi", real=True)
X = (t, x, y, z)
eta = sp.diag(1, -1, -1, -1)
phi = sp.Function("phi")(*X)
d = [sp.diff(phi, c) for c in X]
dphi2 = sum(eta[i, i] * d[i] ** 2 for i in range(4))
box = sum(eta[i, i] * sp.diff(phi, X[i], 2) for i in range(4))
# massless free scalar, arbitrary xi, flat background (curvature terms vanish)
T = sp.zeros(4, 4)
for a in range(4):
    for b in range(4):
        T[a, b] = ((1 - 2 * xi) * d[a] * d[b]
                   + (2 * xi - sp.Rational(1, 2)) * eta[a, b] * dphi2
                   - 2 * xi * phi * sp.diff(phi, X[a], X[b])
                   + 2 * xi * eta[a, b] * phi * box)
kup = [1, 0, 0, 1]  # null: 1 - 1 = 0
assert sum(eta[i, i] * kup[i] ** 2 for i in range(4)) == 0
Tkk = sp.expand(sum(T[a, b] * kup[a] * kup[b] for a in range(4) for b in range(4)))
kd = lambda f: sum(kup[i] * sp.diff(f, X[i]) for i in range(4))
target = sp.expand(kd(phi) ** 2 - xi * kd(kd(phi ** 2)))
chk("k k T = (k.dphi)^2 - xi (k.d)^2 phi^2", sp.simplify(Tkk - target) == 0)
print("     => along x = lambda k the xi-term is d^2/dlambda^2 of <phi^2>;"
      " it integrates to a boundary term, so ANEC is xi-independent in flat space")

# ---------------------------------------------------------------- B
print("B. finite-mode model: 4D Minkowski massless scalar on a null line")
rng = np.random.default_rng(67)
nm, nmax = 3, 4          # 3 modes, occupation 0..4 each -> 125-dim Fock space
kvec = rng.normal(size=(nm, 3))
omega = np.linalg.norm(kvec, axis=1)
u = omega - kvec[:, 2]   # l.k with l = (1,0,0,1): u >= 0, zero only if k || l
c = 1.0 / np.sqrt(2 * omega)
dim = (nmax + 1) ** nm
a1 = np.diag(np.sqrt(np.arange(1, nmax + 1)), 1)
I1 = np.eye(nmax + 1)


def op(single, j):
    m = np.array([[1.0]])
    for i in range(nm):
        m = np.kron(m, single if i == j else I1)
    return m


A = [op(a1, j) for j in range(nm)]
Ad = [m.T for m in A]


def what(v, L):  # Fourier transform of w(l) = exp(-l^2/L^2)
    return L * np.sqrt(np.pi) * np.exp(-(L * v) ** 2 / 4)


def QL(L):
    Q = np.zeros((dim, dim))
    for i in range(nm):
        for j in range(nm):
            pre = u[i] * u[j] * c[i] * c[j]
            Q += pre * (2 * what(u[i] - u[j], L) * Ad[i] @ A[j]
                        - what(u[i] + u[j], L) * (A[i] @ A[j] + Ad[i] @ Ad[j]))
    return Q


vac = np.zeros(dim); vac[0] = 1.0
Ls = [0.5, 1, 2, 4, 8, 16, 32]
mins = []
for L in Ls:
    Q = QL(L)
    ev = np.linalg.eigvalsh(Q)
    mins.append(ev[0])
    print("     L = %5.1f   <0|Q_L|0> = %+.3e   min spec Q_L = %+.6e" % (L, vac @ Q @ vac, ev[0]))
chk("vacuum expectation is exactly 0 at every L (saturation)",
    all(abs(vac @ QL(L) @ vac) < 1e-12 for L in Ls))
chk("finite window: spectrum dips below 0 (no null QI on a segment)", mins[0] < -1e-6)
chk("min spec -> 0^- as L grows (ANEC >= 0 over the complete line)",
    abs(mins[-1]) < 1e-9 and abs(mins[-1]) < abs(mins[0]))
print("     u = l.k per mode:", np.round(u, 4))

# ---------------------------------------------------------------- C
print("C. Fewster-Roman explicit states obey ANEC (gr-qc/0209036 eqs II.24,II.37-38)")
v, vp, w, L0, al, sg, f0 = sp.symbols("v vp w Lambda0 alpha sigma f0", positive=True)
C = 1 / (24 * sp.pi ** 2 * L0 ** 4)          # eq. II.27 on the support
psi_inf = lambda m: 2 * sp.pi * f0 * sp.integrate(w ** 2 * C, (w, 0, m))
inner = 2 * sp.integrate(v * sp.integrate(vp * psi_inf(vp), (vp, 0, v)), (v, 0, L0))  # nu = 1, symmetric min
inner = sp.simplify(inner)
Nsq = 1 / (1 + al ** (2 * sg - 6) / (128 * sp.pi ** 4))   # eq. II.28
anec = sp.simplify(Nsq * al ** (2 * sg - 7) / (2 * sp.pi) ** 4 * inner)
print("     double integral =", inner)
print("     ANEC(alpha)     =", anec)
chk("double integral = 2 pi f0 C * 2 L0^7/105",
    sp.simplify(inner - 2 * sp.pi * f0 * C * 2 * L0 ** 7 / 105) == 0)
vals = {sg: sp.Rational(15, 4), L0: 1, f0: 1}
a02 = float(anec.subs(vals).subs(al, sp.Rational(1, 5)))
a0005 = float(anec.subs(vals).subs(al, sp.Rational(1, 200)))
print("     sigma=3.75, L0=f(0)=1: ANEC(0.2) = %.4e   ANEC(0.005) = %.4e" % (a02, a0005))
chk("ANEC value > 0 and decreasing to 0 as alpha -> 0", a02 > a0005 > 0)
chk("segment average exponent sigma - 4 < 0 (rho_2 -> -inf) and 2sigma-7 > 0",
    (sp.Rational(15, 4) - 4 < 0) and (2 * sp.Rational(15, 4) - 7 > 0))

# ---------------------------------------------------------------- D
print("D. Urban-Olum anomalous ANEC violation, conformally flat 4D (0910.5925 Sec.III)")
U, V, xx, yy, a, b, r = sp.symbols("u v x y a b r", real=True)
rr = sp.symbols("r", positive=True)
om = (a + b * xx ** 2 / rr ** 2) * sp.exp(-(U ** 2 + V ** 2 + xx ** 2 + yy ** 2) / rr ** 2)
# MTW (+++) signature, u=(z-t)/sqrt2, v=(z+t)/sqrt2: ds^2 = 2 du dv + dx^2 + dy^2
boxom = 2 * sp.diff(om, U, V) + sp.diff(om, xx, 2) + sp.diff(om, yy, 2)
on = {U: 0, xx: 0, yy: 0}
box_on = sp.simplify(boxom.subs(on))
omvv_on = sp.simplify(sp.diff(om, V, 2).subs(on))
chk("eq.(39): box omega = 2 r^-2 (b-2a) e^{-v^2/r^2}",
    sp.simplify(box_on - 2 / rr ** 2 * (b - 2 * a) * sp.exp(-V ** 2 / rr ** 2)) == 0)
chk("eq.(40): omega_,vv = 2a r^-2 (2v^2/r^2 - 1) e^{-v^2/r^2}",
    sp.simplify(omvv_on - 2 * a / rr ** 2 * (2 * V ** 2 / rr ** 2 - 1) * sp.exp(-V ** 2 / rr ** 2)) == 0)
beta = -1 / (5760 * sp.pi ** 2)            # eq.(29), real scalar
Tvv = -16 * sp.Symbol("beta") * box_on * omvv_on    # eq.(38), Omega ~ 1, first term 0
chk("eq.(41) reproduced from (38)",
    sp.simplify(Tvv + 64 * sp.Symbol("beta") * a / rr ** 4 * (2 * V ** 2 / rr ** 2 - 1)
                * (b - 2 * a) * sp.exp(-2 * V ** 2 / rr ** 2)) == 0)
I = sp.simplify(sp.integrate(Tvv, (V, -sp.oo, sp.oo)))
chk("eq.(42): int T_vv dv = (ab - 2a^2) 16 beta sqrt(2 pi)/r^3",
    sp.simplify(I - (a * b - 2 * a ** 2) * 16 * sp.Symbol("beta") * sp.sqrt(2 * sp.pi) / rr ** 3) == 0)
num = float(I.subs({sp.Symbol("beta"): beta, a: sp.Rational(1, 100), b: sp.Rational(1, 20), rr: 1}))
print("     a=0.01, b=0.05, r=1: ANEC integral = %.4e (vacuum state, test field)" % num)
chk("negative for b > 2a: ANEC fails in a curved (conformally flat) background", num < 0)

print("RESULT:", "ALL AGREE" if ok_all else "DISAGREEMENT")
sys.exit(0 if ok_all else 1)
