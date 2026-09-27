#!/usr/bin/env python3
"""DOCKET 67 -- squeezed-vacuum-negative-local-energy.  Re-derivation, stdlib+sympy+numpy.
Imports nothing from research/.  hbar = c = 1.

Claim audited (candidates.py:92-99): squeezed vacuum is 'a state in which the energy density at a
spacetime point is genuinely negative ... A real rho < 0' and 'Kill the pump and it is gone at c.
Nothing to remove.'

Model: free massless real scalar, one plane-wave mode k = omega x^ in a box of volume V,
phi = (a e^{i chi} + a^dag e^{-i chi}) / sqrt(2 omega V),  chi = k x - omega t,
T00 = (phi_t^2 + phi_x^2)/2, normal ordered w.r.t. the Minkowski (Fock) vacuum.
Squeezed vacuum S(zeta)|0>, zeta = r e^{i theta}:  <a a> = -e^{i theta} sinh r cosh r, <a^dag a> = sinh^2 r.
"""
import sys, math, cmath
import sympy as sp
import numpy as np

R = []
def chk(name, ok, detail=""):
    R.append((name, bool(ok)))
    print(("PASS " if ok else "FAIL ") + name + ("  -- " + detail if detail else ""))

r, th, w, V, x, t, psi, D = sp.symbols('r theta omega V x t psi Delta', real=True)
rp = sp.symbols('r', positive=True)
s, c = sp.sinh(r), sp.cosh(r)
K = w / (2 * V)
chi = w * x - w * t

# ---------------- A. <:T00:> from the moments (symbolic)
aa = -sp.exp(sp.I * th) * s * c          # <a a>
ada = s**2                               # <a^dag a>
pref = 1 / (2 * w * V)
e, ec = sp.exp(sp.I * chi), sp.exp(-sp.I * chi)
# phi_t = -i w (a e - a^dag ec) * sqrt(pref); phi_x = i w (a e - a^dag ec) * sqrt(pref)
# :(a e - a^dag ec)^2: = a a e^2 + a^dag a^dag ec^2 - 2 a^dag a
Y2 = aa * e**2 + sp.conjugate(aa) * ec**2 - 2 * ada
phit2 = -(w**2) * pref * Y2
phix2 = -(w**2) * pref * Y2
rho = sp.simplify(sp.expand_complex(sp.expand((phit2 + phix2) / 2)))
kf322 = 2 * K * s * (c * sp.cos(2 * chi + th) + s)     # the KF (3.22) shape as encoded in fluctuation.py
chk("A1 <:T00:> = 2K sinh r (sinh r + cosh r cos(2chi+theta)), K = omega/(2V)",
    sp.simplify(sp.expand_trig(sp.expand_complex(rho - kf322))) == 0, str(sp.simplify(rho)))

# ---------------- A'. independent control: truncated Fock space, numeric squeeze operator
def fock_moments(rv, thv, N=120):
    a = np.diag(np.sqrt(np.arange(1, N)), 1).astype(complex)
    ad = a.conj().T
    z = rv * cmath.exp(1j * thv)
    G = 0.5 * (np.conj(z) * a @ a - z * ad @ ad)
    # expm via eigen-decomposition of the anti-Hermitian generator
    # G is anti-Hermitian: G = iH with H Hermitian, so exp(G) = U diag(e^{i h}) U^dag (unitary, stable)
    hv, U = np.linalg.eigh(-1j * G)
    S = U @ np.diag(np.exp(1j * hv)) @ U.conj().T
    v0 = np.zeros(N, complex); v0[0] = 1
    psiv = S @ v0
    ex = lambda O: np.vdot(psiv, O @ psiv)
    return ex(a @ a), ex(ad @ a), ex, a, ad, psiv
for rv, thv in [(0.3, 0.0), (0.7, 1.1), (1.2, -2.0)]:
    m_aa, m_n, *_ = fock_moments(rv, thv)
    res = max(abs(m_aa - (-cmath.exp(1j * thv) * math.sinh(rv) * math.cosh(rv))), abs(m_n - math.sinh(rv)**2))
    chk("A2 Fock control (N=120 truncation) r=%.1f theta=%.1f: <aa>, <a^dag a> match -e^{i th} s c, s^2" % (rv, thv),
        res < 1e-7, "max residual %.1e (truncation)" % res)

# ---------------- B. negativity and its floor
rmin = sp.simplify((2 * K * s * (s - c)).rewrite(sp.exp))
chk("B1 minimum over phase = 2K s(s-c) = -K(1-e^{-2r})",
    sp.simplify(rmin - (-K * (1 - sp.exp(-2 * r)))) == 0, str(sp.factor(rmin)))
sr, cr = sp.sinh(rp), sp.cosh(rp)
chk("B2 negative for EVERY r > 0 (s(s-c) = -s e^{-r} < 0)",
    sp.simplify((sr * (sr - cr)).rewrite(sp.exp) + sp.sinh(rp).rewrite(sp.exp) * sp.exp(-rp)) == 0 and
    sp.ask(sp.Q.positive(sp.sinh(rp) * sp.exp(-rp))) is not False)
chk("B3 the dip SATURATES: lim_{r->oo} min = -K = -omega/(2V) (minus the mode's own zero-point density)",
    sp.limit(-K * (1 - sp.exp(-2 * rp)), rp, sp.oo) == -K)
avg = sp.simplify(sp.integrate(2 * K * s * (c * sp.cos(psi) + s), (psi, 0, 2 * sp.pi)) / (2 * sp.pi))
chk("B4 cycle average = 2K sinh^2 r > 0 (energy per mode omega sinh^2 r)", sp.simplify(avg - 2 * K * s**2) == 0, str(avg))
# fraction of phase with rho < 0 : cos psi < -tanh r  ->  arccos(tanh r)/pi
for rv in (0.1, 0.5, 1.0, 1.727, 3.0):
    tt = math.tanh(rv)
    frac_formula = math.acos(tt) / math.pi
    ps = np.linspace(0, 2 * math.pi, 400001)[:-1]
    f = np.sinh(rv) * (np.sinh(rv) + np.cosh(rv) * np.cos(ps))
    frac_num = np.mean(f < 0)
    pos, neg = f[f > 0].sum(), -f[f < 0].sum()
    chk("B5 r=%.3f negative-phase fraction arccos(tanh r)/pi = %.5f (numeric %.5f); positive/negative integral = %.4f > 1"
        % (rv, frac_formula, frac_num, pos / neg), abs(frac_formula - frac_num) < 1e-4 and pos / neg > 1)

# ---------------- C. it is an EXPECTATION value: <:T00^2:> = 3 rho^2 (zero-mean Gaussian), so Delta' = 2
# T00 = X^2 with X = phi_t = alpha a + alpha^* a^dag, alpha = -i w sqrt(pref) e^{i chi}
for rv, thv, chiv in [(0.5, 0.3, 0.2), (1.0, 0.0, 1.7), (0.8, 2.0, -0.4)]:
    _, _, ex, a, ad, _ = fock_moments(rv, thv, N=160)
    al = -1j * math.sqrt(1 / 2) * cmath.exp(1j * chiv)   # w = V = 1
    mp = np.linalg.matrix_power
    X2 = sum(math.comb(2, j) * np.conj(al)**j * al**(2 - j) * mp(ad, j) @ mp(a, 2 - j) for j in range(3))
    X4 = sum(math.comb(4, j) * np.conj(al)**j * al**(4 - j) * mp(ad, j) @ mp(a, 4 - j) for j in range(5))
    rho_n, T2_n = ex(X2).real, ex(X4).real
    rho_c = 2 * 0.5 * math.sinh(rv) * (math.sinh(rv) + math.cosh(rv) * math.cos(2 * chiv + thv))
    chk("C1 r=%.1f: <:T00:> = %.6f (closed form %.6f), <:T00^2:>/rho^2 = %.6f (=3)" % (rv, rho_n, rho_c, T2_n / rho_n**2),
        abs(rho_n - rho_c) < 1e-8 and abs(T2_n / rho_n**2 - 3) < 1e-6)

# ---------------- D. propagation: the pattern depends on chi = k x - omega t only, omega = |k| (massless)
chk("D1 <:T00:>(t+D, x+D) = <:T00:>(t, x): the negative regions move rigidly at c (free massless, vacuum)",
    sp.simplify(rho.subs({t: t + D, x: x + D}, simultaneous=True) - rho) == 0)
kk, mm = sp.symbols('k m', positive=True)
vg = sp.diff(sp.sqrt(kk**2 + mm**2), kk)
chk("D2 control: with mass m the group velocity k/sqrt(k^2+m^2) < 1 -- 'at c' needs the massless, vacuum hypothesis",
    sp.simplify(vg - kk / sp.sqrt(kk**2 + mm**2)) == 0 and float(vg.subs({kk: 1, mm: 1})) < 1)

# ---------------- E. EM plane-wave mode and the measured quantity
# For one plane-wave EM mode B = k^ x E, so :E^2: = :B^2: and <:T00:> = <:E^2:> (Gaussian units /4pi absorbed):
# <:E_phi^2:> is proportional to V_phi - V_vac, the quadrature variance minus shot noise.  So a measured
# sub-shot-noise quadrature variance IS a negative normal-ordered energy density at that phase (single-mode,
# plane-wave idealisation).  Ratio to the mode's vacuum scale:  min <:T00:>/K = V_s/V_vac - 1 = 10^{-dB/10} - 1.
for dB in (6.0, 10.0, 15.0):
    rr = dB * math.log(10) / 20
    val = 10**(-dB / 10) - 1
    chk("E1 %.0f dB squeezing (pure state r=%.4f): min <:T00:>/K = %.4f = -(1-e^{-2r})" % (dB, rr, val),
        abs(val - (-(1 - math.exp(-2 * rr)))) < 1e-12)

n_pass = sum(ok for _, ok in R)
print("\n%d/%d PASS" % (n_pass, len(R)))
sys.exit(0 if n_pass == len(R) else 1)
