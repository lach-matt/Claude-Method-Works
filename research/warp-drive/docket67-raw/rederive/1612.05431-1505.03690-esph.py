#!/usr/bin/env python3
"""DOCKET 67 re-derivation: 1612.05431-1505.03690-esph.

The tree (massform.py:538-543, 1109-1115, 1475-1477) holds E_sph = 9.11 TeV
(Tye-Wong, pure SU(2)), 9.08 TeV (Funakubo-Fuyuto-Senaha, USED) and 9.0 TeV
(with U(1)), and derives 3226 x (3 proton rest energies) and 3246 Mc^2.

Neither source could be read in this session (alphaXiv quota exhausted;
arxiv.org egress-blocked).  What IS checkable here, independent of both
sources, is the number itself: the static saddle of the SU(2) Yang-Mills-Higgs
energy in the Klinkhamer-Manton spherically symmetric ansatz (which is exact
for theta_W = 0 by symmetry), solved numerically, plus the O(g'^2) U(1)
correction computed by first-order perturbation theory (linear response of the
hypercharge field to the sphaleron's hypercharge current).

  E = (4 pi v / g) B,   B = int_0^inf dxi [ 4 f'^2 + 8 f^2 (1-f)^2 / xi^2
        + xi^2 h'^2 / 2 + h^2 (1-f)^2 + (lam/(4 g^2)) xi^2 (h^2-1)^2 ],
  xi = g v r,  lam/g^2 = m_H^2 / (8 m_W^2),  f(0)=h(0)=0, f,h -> 1.

Validation (fixtures that are NOT the tested number): B -> 1.56 as m_H -> 0
and B -> 2.72 as m_H -> inf (Klinkhamer-Manton as restated by Rubakov &
Shaposhnikov hep-ph/9603208 eq.(2.11), the tree's RS96-esph capture).

Hypercharge current: K_i = Im(Phi^dag D0_i Phi) = (v^2/2) h^2 (1-f) (-y, x, 0)/r^2
(symbolic, km_current.py).  Energy shift at O(g'^2):
  dE = -(g'^2/2) int int K(x).K(y) / (4 pi |x-y|) = -(g'^2/2)(8 pi/3) int a G r^2 dr,
  K_phi = G(r) sin(theta), G = (v^2/2) h^2 (1-f)/r, a = l=1 Green's-function potential.
"""
import math
import numpy as np
from scipy.integrate import solve_bvp, quad, cumulative_trapezoid

def solve(mh_over_mw, L=60.0, eps=1e-3, n=4000, hinf=False):
    k = 0.0 if hinf else mh_over_mw ** 2 / 8.0   # lam / g^2
    mh_xi = math.sqrt(2 * k)           # Higgs mass in units of g v  (m_H = sqrt(2 lam) v)
    xi = np.concatenate([np.linspace(eps, 1, 200)[:-1], np.geomspace(1, L, n)])
    if hinf:
        def rhs(t, Y):
            f, fp = Y
            return np.vstack([fp, 2 * f * (1 - f) * (1 - 2 * f) / t**2 - (1 - f) / 4])
        def bc(a, b):
            return np.array([eps * a[1] - 2 * a[0], b[0] - 1])
        f0 = np.tanh(xi / 4) ** 2
        sol = solve_bvp(rhs, bc, xi, np.vstack([f0, np.gradient(f0, xi)]), tol=1e-8, max_nodes=200000)
        t = np.geomspace(eps, L, 40000)
        f, fp = sol.sol(t)
        e = 4 * fp**2 + 8 * f**2 * (1 - f)**2 / t**2 + (1 - f)**2
        return sol, t, f, np.ones_like(t), np.trapezoid(e, t)
    def rhs(t, Y):
        f, fp, h, hp = Y
        fpp = 2 * f * (1 - f) * (1 - 2 * f) / t**2 - h**2 * (1 - f) / 4
        # (xi^2 h')' = 2 h (1-f)^2 + (lam/g^2) xi^2 h (h^2-1)  ->  lam/g^2 = k
        hpp = -2 * hp / t + 2 * h * (1 - f)**2 / t**2 + k * h * (h**2 - 1)
        return np.vstack([fp, fpp, hp, hpp])
    def bc(a, b):
        # f ~ xi^2, h ~ xi at the origin; exponential approach at L
        return np.array([eps * a[1] - 2 * a[0], eps * a[3] - a[2],
                         b[0] - 1, b[3] + max(mh_xi, 1.0 / L) * (b[2] - 1) + (b[2] - 1) / L])
    f0 = np.tanh(xi / 4) ** 2
    h0 = np.tanh(xi / 3)
    Y0 = np.vstack([f0, np.gradient(f0, xi), h0, np.gradient(h0, xi)])
    sol = solve_bvp(rhs, bc, xi, Y0, tol=1e-8, max_nodes=400000)
    t = np.geomspace(eps, L, 60000)
    f, fp, h, hp = sol.sol(t)
    e = (4 * fp**2 + 8 * f**2 * (1 - f)**2 / t**2 + t**2 * hp**2 / 2
         + h**2 * (1 - f)**2 + (k / 4) * t**2 * (h**2 - 1)**2)
    return sol, t, f, h, np.trapezoid(e, t)

def u1_shift_fraction(t, f, h, B, gprime_over_g):
    """dE/E at O(g'^2), in xi units: r = xi/(g v).  Returns dE / E(theta_W=0)."""
    # Work with v = 1, g = 1 (the ratio is scale-free once g'/g is fixed):
    # G(xi) = (1/2) h^2 (1-f) / xi   (v^2/2 h^2 (1-f)/r with r = xi, gv = 1)
    G = 0.5 * h**2 * (1 - f) / t
    I_in = cumulative_trapezoid(G * t**3, t, initial=0.0)
    I_out_total = np.trapezoid(G, t)
    I_out = I_out_total - cumulative_trapezoid(G, t, initial=0.0)
    a = (I_in / t**2 + t * I_out) / 3.0
    dE = -(gprime_over_g**2 / 2.0) * (8 * math.pi / 3.0) * np.trapezoid(a * G * t**2, t)
    E0 = 4 * math.pi * B       # (4 pi v/g) B with v = g = 1
    return dE / E0

if __name__ == "__main__":
    out = {}
    # --- validation against the READ KM endpoints (1.56, 2.72) ---
    s_, t, f, h, Binf = solve(None, hinf=True, eps=1e-4)
    print("B(m_H -> inf) [h == 1]      = %.4f   (KM restated: 2.72)  status=%d" % (Binf, s_.status))
    for r_ in (0.02, 0.05):
        _, t, f, h, B0 = solve(r_, L=400.0)
        print("B(m_H/m_W = %.2f)           = %.4f   (KM restated: 1.56 as m_H -> 0)" % (r_, B0))
    for r_ in (1.0, 2.0, 3.0, 5.0):
        s_, t, f, h, Bx = solve(r_, eps=1e-4)
        print("B(m_H/m_W = %5.2f)          = %.4f  status=%d (monotone rise toward the m_H->inf limit)" % (r_, Bx, s_.status))
    print()
    # --- data sets ---
    cases = {
        "TW-2015 inputs (v=246, m_W=80, m_H=125)": (246.0, 80.0, 125.0, 91.1876),
        "PDG-2014-era (v=246.22, m_W=80.385, m_H=125.09)": (246.22, 80.385, 125.09, 91.1876),
        "tree (v=246.2196, m_W=80.362 massform, m_H=125.20)": (246.21964, 80.362, 125.20, 91.1880),
        "PDG-2024 (v=246.22, m_W=80.3692, m_H=125.20)": (246.21964, 80.3692, 125.20, 91.1880),
        "CDF-2022 m_W=80.4335 (contested)": (246.21964, 80.4335, 125.20, 91.1880),
    }
    for name, (v, mw, mh, mz) in cases.items():
        s_, t, f, h, B = solve(mh / mw)
        assert s_.status == 0, s_.message
        g = 2 * mw / v
        E = 4 * math.pi * v / g * B / 1000.0
        s2_os = 1 - (mw / mz)**2
        gp_os = math.sqrt(s2_os / (1 - s2_os))
        gp_ms = math.sqrt(0.23122 / (1 - 0.23122))
        dos = u1_shift_fraction(t, f, h, B, gp_os)
        dms = u1_shift_fraction(t, f, h, B, gp_ms)
        print("%-52s m_H/m_W=%.4f B=%.4f E_sph(SU2)=%.3f TeV  "
              "U(1) O(g'^2): %.2f%% (on-shell s2=%.4f) -> %.3f TeV; %.2f%% (MSbar 0.23122) -> %.3f TeV"
              % (name, mh / mw, B, E, 100 * dos, s2_os, E * (1 + dos), 100 * dms, E * (1 + dms)))
        out[name] = (B, E, dos, dms)
    print()
    # --- the tree's arithmetic ---
    mp = 938.272089
    print("9.08 TeV / (3 m_p c^2) = %.1f   (tree: 3226)" % (9.08e6 / (3 * mp)))
    print("9.11 TeV / (3 m_p c^2) = %.1f ; 9.0 -> %.1f" % (9.11e6 / (3 * mp), 9.0e6 / (3 * mp)))
    Bpdg, Epdg, dpdg, _ = out["PDG-2024 (v=246.22, m_W=80.3692, m_H=125.20)"]
    print("independent E_sph(PDG-2024, SU(2)) / (3 m_p) = %.1f" % (Epdg * 1e6 / (3 * mp)))
    print("TW product 4.75 x (1.31+0.60) = %.4f (TW print 9.11)" % (4.75 * 1.91))
    print("tree 3246 Mc^2 scales linearly with E_sph: at independent E=%.3f -> %.1f Mc^2"
          % (Epdg, 3245.684939 * Epdg / 9.08))
