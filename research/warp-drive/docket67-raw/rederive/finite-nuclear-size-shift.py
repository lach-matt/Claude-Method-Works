#!/usr/bin/env python3
"""DOCKET 67 -- re-derivation for 'finite-nuclear-size-shift' (address.py:45-52, 834-861, 878-879).

Source READ: CODATA 2022, Mohr-Newell-Taylor-Tiesinga, arXiv:2409.03787v1 (cached full text,
scratchpad d67/src/casmag/all/2409.03787v1.txt, md5 cc640485b0d9f0fe202f38989dac6a2b):
  eq (50)  E(4)_nucl = (2/3) m_e c^2 (Z alpha)^4/n^3 (m_r/m_e)^3 (r_N/lambda_C)^2 delta_l0,
           'solely due to the finite rms charge radius r_N'
  eq (51)-(52) alpha^5 Friar term, r_pF = 1.947(75) fm;  eq (56),(59) alpha^6 term
  eq (28)-(30) Dirac eigenvalue with finite-mass (recoil) corrections
  eq (32)  Salpeter relativistic recoil;  eq (35)-(36) self energy;  Table V Bethe logs
  Table XXXIII r_p = 8.4075(64)e-16 m;  2018 reference value r_p,ref = 0.8414 fm (Table II)

R1  sympy: first-order perturbation of a point Coulomb potential by a spherical charge
    distribution with psi(0) held constant gives (4/3) Z^4 Ry (r_rms/a0)^2/n^3 for uniform
    sphere, Gaussian and exponential shapes alike -- equal to CODATA eq (50) at m_r = m_e.
    Also: if r_N meant the uniform-sphere RADIUS R, the coefficient would be 4/5, not 4/3.
R2  sympy: the tree's K = 28x^2/(14x^2-9) re-derived; value at CODATA 2018 and 2022 inputs.
R3  numeric: (m_r/m_e)^3 factor and the alpha^5 (Friar) / alpha^6 finite-size terms' effect on K.
R4  numeric (mpmath, 40 digits): the same-place sensitivity d ln[nu(1S-2S)/nu(2P-3D)]/d ln v
    under H2 (alpha fixed, r_N fixed, m_e ~ v, m_p ~ v^S) from CODATA eqs (28)-(30), (32),
    (35)-(36) leading terms, VP leading term, and (50): the recoil / reduced-mass terms the
    tree omits, compared with the finite-size term it keeps.
"""
import sympy as sp
import mpmath as mp

out = []
def rec(tag, msg):
    print("%-4s %s" % (tag, msg)); out.append((tag, msg))

# ---------------- R1
r, R, a, b, Z, e2, psi0sq = sp.symbols("r R a b Z e2 psi0sq", positive=True)
def dE_first_order(rho):          # rho(r) normalised charge density (integrates to 1)
    q = sp.integrate(4*sp.pi*r**2*rho, (r, 0, sp.oo))
    assert sp.simplify(q - 1) == 0
    r2 = sp.integrate(4*sp.pi*r**4*rho, (r, 0, sp.oo))
    # V - V_point integrated over all space, from Poisson: int (V-Vpt) d^3r = (2 pi/3) Z e2 <r^2>
    # checked here directly for each shape via the enclosed-charge potential
    s = sp.symbols("s", positive=True)
    Qenc = sp.integrate(4*sp.pi*s**2*rho.subs(r, s), (s, 0, r))
    # V(r) = -Z e2 [Qenc/r + int_r^oo 4 pi s rho ds]
    outer = sp.integrate(4*sp.pi*s*rho.subs(r, s), (s, r, sp.oo))
    V = -Z*e2*(Qenc/r + outer)
    Vpt = -Z*e2/r
    I = sp.integrate(sp.simplify((V - Vpt)*4*sp.pi*r**2), (r, 0, sp.oo))
    return sp.simplify(psi0sq*I), sp.simplify(r2)

shapes = {
    "uniform sphere radius R": sp.Piecewise((3/(4*sp.pi*R**3), r < R), (0, True)),
    "Gaussian": sp.exp(-r**2/(2*b**2))/((2*sp.pi)**sp.Rational(3, 2)*b**3),
    "exponential": sp.exp(-r/a)/(8*sp.pi*a**3),
}
n, a0, Ry = sp.symbols("n a0 Ry", positive=True)
psi0 = Z**3/(sp.pi*n**3*a0**3)           # |psi_nS(0)|^2
for name, rho in shapes.items():
    if name.startswith("uniform"):
        # piecewise integration: do it by hand-split
        s = sp.symbols("s", positive=True)
        rr = sp.symbols("rr", positive=True)
        Vin = -Z*e2*(3*R**2 - rr**2)/(2*R**3)
        I = sp.integrate((Vin + Z*e2/rr)*4*sp.pi*rr**2, (rr, 0, R))
        r2 = sp.Rational(3, 5)*R**2
        dE = sp.simplify(psi0sq*I)
    else:
        dE, r2 = dE_first_order(rho)
    ratio = sp.simplify(dE/(sp.Rational(2, 3)*sp.pi*Z*e2*psi0sq*r2))
    # in Rydberg: e2/a0 = 2 Ry
    dE_Ry = sp.simplify((dE.subs(psi0sq, psi0)).subs(e2, 2*Ry*a0))
    coeff = sp.simplify(dE_Ry/(Z**4*Ry*r2/(a0**2*n**3)))
    rec("R1", "%-24s dE/[(2pi/3)Z e2 |psi(0)|^2 <r^2>] = %s ; dE = %s * Z^4 Ry <r^2>/(a0^2 n^3)"
        % (name, ratio, coeff))
    assert ratio == 1 and coeff == sp.Rational(4, 3)
# CODATA eq (50) in Rydberg units: m_e c^2 alpha^2 = 2 Ry, lambda_C = alpha a0
al, rN, lamC = sp.symbols("alpha r_N lambda_C", positive=True)
E50 = sp.Rational(2, 3)*(2*Ry/al**2)*(Z*al)**4/n**3*(rN/lamC)**2
tree = sp.Rational(4, 3)*Z**4*Ry*(rN/a0)**2/n**3
rec("R1", "CODATA eq(50) at m_r=m_e minus tree's (4/3)Z^4(r_N/a0)^2/n^3 Ry, lambda_C = alpha a0: %s"
    % sp.simplify(E50.subs(lamC, al*a0) - tree))
rec("R1", "if r_N were the uniform-sphere RADIUS R (not rms): coefficient = (4/3)(3/5) = %s"
    % (sp.Rational(4, 3)*sp.Rational(3, 5)))

# ---------------- R2
x = sp.symbols("x", positive=True)
def E(nn, l):
    return -sp.Rational(1, nn**2) + (sp.Rational(4, 3)*x**2/nn**3 if l == 0 else 0)
K = sp.simplify(sp.diff(sp.log((E(2, 0)-E(1, 0))/(E(3, 2)-E(2, 1))), x)*x)
rec("R2", "K(x) = %s ; residual vs 28x^2/(14x^2-9): %s ; series %s"
    % (K, sp.simplify(K - 28*x**2/(14*x**2-9)), sp.series(K, x, 0, 4).removeO()))
A0_2018, A0_2022 = 5.29177210903e-11, 5.29177210544e-11
RP = {"tree/CODATA2018 0.8414 fm": 0.8414e-15, "CODATA2022 0.84075 fm": 0.84075e-15,
      "CODATA2022 +1sigma": 0.84139e-15, "CODATA2022 -1sigma": 0.84011e-15,
      "old e-p scattering/CODATA2014 0.8751 fm": 0.8751e-15}
Kf = sp.lambdify(x, K)
for k, rp in RP.items():
    a0v = A0_2018 if "2018" in k else A0_2022
    rec("R2", "%-42s x = %.6e  K = %.5e" % (k, rp/a0v, Kf(rp/a0v)))
Ktree = Kf(0.8414e-15/A0_2018)
rec("R2", "selftest pin -7.8654e-10 rtol 1e-4: tree inputs %s ; 2022 inputs %s"
    % (abs(Ktree+7.8654e-10) <= 1e-4*7.8654e-10,
       abs(Kf(0.84075e-15/A0_2022)+7.8654e-10) <= 1e-4*7.8654e-10))

# ---------------- R3 / R4 numeric with mpmath
mp.mp.dps = 40
alpha = mp.mpf(1)/mp.mpf("137.035999177")
me0 = mp.mpf(1)
mp_over_me = mp.mpf("1836.152673426")
lamC0_fm = mp.mpf("386.15926744")        # reduced Compton wavelength, fm (CODATA 2022)
rp_fm = mp.mpf("0.84075")
rpF_fm = mp.mpf("1.947")
lnk0 = {(1, 0): mp.mpf("2.984128556"), (2, 0): mp.mpf("2.811769893"),
        (2, 1): mp.mpf("-0.030016709"), (3, 2): mp.mpf("-0.005232148")}  # 3D: NAMED-NOT-READ (not in CODATA Table V)

def kappa(l, j2):   # j2 = 2j
    j = mp.mpf(j2)/2
    return int((-1)**(j - l + mp.mpf(1)/2)*(j + mp.mpf(1)/2))

def energy(nn, l, j2, me, mN, rfm, terms):
    """energy (units m_e0 c^2) excluding rest mass, from CODATA eqs (28)-(30),(32),(35)-(36),(50),(51)."""
    k = kappa(l, j2)
    Za = alpha
    delta = abs(k) - mp.sqrt(k**2 - Za**2)
    f = (1 + Za**2/(nn - delta)**2)**mp.mpf(-0.5)
    M = me + mN
    mr = me*mN/M
    d0 = 1 if l == 0 else 0
    Et = mp.mpf(0)
    if "dirac" in terms:
        Et += (f - 1)*mr
    if "recoil30" in terms:
        Et += -(f - 1)**2*mr**2/(2*M) + (1 - d0)/(k*(2*l + 1))*Za**4*mr**3/(2*nn**3*mN**2)
    lamC = lamC0_fm*me0/me          # reduced Compton wavelength scales as 1/m_e
    if "fns4" in terms:
        Et += mp.mpf(2)/3*me*Za**4/nn**3*(mr/me)**3*(rfm/lamC)**2*d0
    if "fns4_nomr" in terms:
        Et += mp.mpf(2)/3*me*Za**4/nn**3*(rfm/lamC)**2*d0
    if "fns5" in terms:
        Et += -mp.mpf(1)/3*me*Za**5/nn**3*(mr/me)**3*(rpF_fm/lamC)**3*d0
    if "salpeter" in terms:
        H = mp.fsum(mp.mpf(1)/i for i in range(1, nn + 1))
        an = (-2*(mp.log(mp.mpf(2)/nn) + H + 1 - mp.mpf(1)/(2*nn))*d0
              + ((1 - d0)/(l*(l + 1)*(2*l + 1)) if l else 0))
        br = (mp.mpf(1)/3*d0*mp.log(Za**-2) - mp.mpf(8)/3*lnk0[(nn, l)] - mp.mpf(1)/9*d0
              - mp.mpf(7)/3*an - 2/(mN**2 - me**2)*d0*(mN**2*mp.log(me/mr) - me**2*mp.log(mN/mr)))
        Et += mr**3/(me**2*mN)*Za**5/(mp.pi*nn**3)*me*br
    if "qed" in terms:          # leading one-loop self energy (A41 L + A40) and Uehling VP (-4/15)
        L = mp.log((me/mr)*Za**-2)
        A41 = mp.mpf(4)/3*d0
        A40 = -mp.mpf(4)/3*lnk0[(nn, l)] + mp.mpf(10)/9*d0 - (1 - d0)/(2*k*(2*l + 1))
        Et += alpha/mp.pi*Za**4/nn**3*(mr/me)**3*me*(A41*L + A40 - mp.mpf(4)/15*d0)
    return Et

def lnratio(me, mN, rfm, terms, lo=(2, 1, 1), hi=(3, 2, 3)):
    nu1 = energy(2, 0, 1, me, mN, rfm, terms) - energy(1, 0, 1, me, mN, rfm, terms)
    nu2 = energy(*hi, me, mN, rfm, terms) - energy(*lo, me, mN, rfm, terms)
    return mp.log(nu1/nu2)

def K_H2(terms, S, lo=(2, 1, 1), hi=(3, 2, 3)):
    """d ln R/d ln v = dlnR/dln m_e * 1 + dlnR/dln m_p * S, r_N and alpha fixed (H2)."""
    mN = mp_over_me
    dme = mp.diff(lambda t: lnratio(me0*mp.e**t, mN, rp_fm, terms, lo, hi), 0)
    dmN = mp.diff(lambda t: lnratio(me0, mN*mp.e**t, rp_fm, terms, lo, hi), 0)
    return dme + S*dmN

base = ("dirac",)
rec("R3", "control: Dirac point nucleus infinite-mass-scaled only -> K = %s (expect 0: m_r cancels)"
    % mp.nstr(K_H2(base, 0), 5))
k_nomr = K_H2(base + ("fns4_nomr",), 0) - K_H2(base, 0)
rec("R3", "finite size, tree form (no (m_r/m_e)^3), full Dirac background, 2022 r_p: K = %s"
    % mp.nstr(k_nomr, 6))
k_fs4 = K_H2(base + ("fns4",), 0) - K_H2(base, 0)
rec("R3", "finite size eq(50) with (m_r/m_e)^3, S=0: K = %s" % mp.nstr(k_fs4, 6))
k_fs5 = K_H2(base + ("fns4", "fns5"), 0) - K_H2(base + ("fns4",), 0)
rec("R3", "alpha^5 Friar term (eq 51, r_pF 1.947 fm) adds: %s  (%.3g of the leading)"
    % (mp.nstr(k_fs5, 4), float(k_fs5/k_fs4)))

for S in (mp.mpf("0.0096"), mp.mpf("0.06")):
    for lo, hi, lab in (((2, 1, 1), (3, 2, 3), "2P1/2-3D3/2"), ((2, 1, 3), (3, 2, 5), "2P3/2-3D5/2")):
        k_rec = K_H2(base + ("recoil30",), S, lo, hi) - K_H2(base, S, lo, hi)
        k_sal = K_H2(base + ("salpeter",), S, lo, hi) - K_H2(base, S, lo, hi)
        k_qed = K_H2(base + ("qed",), S, lo, hi) - K_H2(base, S, lo, hi)
        k_fs = K_H2(base + ("fns4",), S, lo, hi) - K_H2(base, S, lo, hi)
        allt = base + ("recoil30", "salpeter", "qed", "fns4", "fns5")
        k_all = K_H2(allt, S, lo, hi)
        rec("R4", "S=%s %s: K_recoil(eq30)=%s K_Salpeter=%s K_QED(m_r)=%s K_fs=%s  TOTAL=%s  |omitted|/|fs|=%.2f"
            % (S, lab, mp.nstr(k_rec, 4), mp.nstr(k_sal, 4), mp.nstr(k_qed, 4), mp.nstr(k_fs, 4),
               mp.nstr(k_all, 4), float(abs(k_all - k_fs)/abs(k_fs))))

# closed-form check of the dominant recoil piece: -[f-1]^2 m_r^2/2M -> -mu alpha^2/(4 n^4) (units m_r alpha^2/2)
mu = 1/mp_over_me
closed = (mp.mpf(15)/64/(mp.mpf(3)/4) - mp.mpf(65)/5184/(mp.mpf(5)/36))*mu*alpha**2
rec("R4", "closed form, leading (Z alpha)^4 m^2/M recoil term, d lnR/d ln mu = (2/9) mu alpha^2 approx: %s"
    % mp.nstr(closed, 5))
