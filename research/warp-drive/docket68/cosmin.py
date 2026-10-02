# PRE-DOCKET 68 COMPUTATION (2026-10-02), not seated.  Re-derives the headline numbers of
# T. Padmanabhan & H. Padmanabhan, "Cosmic Information, the Cosmological Constant and the Amplitude of primordial
# perturbations", arXiv:1703.06144v1 (READ at source via alphaXiv; M placed it in the Warp folder as an Acrobat
# share link, which the egress proxy refuses -- per ruling M-D67-2 the arXiv version read is the object).
# Every input is the paper's own printed value (p. 4-5); nothing is taken from elsewhere.
# READING OF THE EQUATIONS.  The text layer flattens fractions.  Read literally, eq. (4) gives nu ~ 1e-15, not the
# paper's 6.2e3 -- a fault in the READING, not shown to be in the paper: eq. (4) is the algebraic inverse of eq. (3)
# only if eq. (3)'s argument is k1 (rho_L^2 rho_eq)^(1/12) / E_QG and eq. (4) carries (rho_eq L_P^4)^(-1/2).  That
# reading is DERIVED here (check A below), not assumed, and it reproduces every printed number.
import math
pi = math.pi
rhoL, drhoL = 1.14e-123, 0.09e-123      # rho_Lambda L_P^4  (p.5)
rhoE, drhoE = 2.41e-113, 1.01e-113      # rho_eq L_P^4      (p.5)
Ic = 4*pi                               # the postulate N(a_Lambda, a_QG) = 4 pi (p.4, p.7)
pref = (4/27)*(3/(8*pi))**1.5           # eq. (4)/(5) prefactor
def nu_of(rl, re, I=Ic):                # invert eq. (4): rhoL = pref * nu^-6 * re^(-1/2) * exp(-9 pi I)
    return (pref*math.exp(-9*pi*I)/(rl*math.sqrt(re)))**(1/6)
nu = nu_of(rhoL, rhoE)
lo = nu_of(rhoL+drhoL, rhoE-drhoE); hi = nu_of(rhoL-drhoL, rhoE+drhoE)
print(f"eq.(5) inverted: nu = {nu:.4g}   (range over the printed 1-sigma inputs: {lo:.3g} .. {hi:.3g}); paper: (6.2 +/- 0.3)e3")
# eq.(6), w = 1/3: A = c1/nu * sqrt(4/(3 pi)) * sqrt(3 w^0.5 (6w+5) / (4 (3w+5)^2))
w = 1/3
coef = math.sqrt(4/(3*pi))*math.sqrt(3*w**0.5*(6*w+5)/(4*(3*w+5)**2))
print(f"eq.(6) coefficient = {coef:.4f} (paper: 0.19);  A_theory/c1 = {coef/nu:.3e} (paper: 3.05e-5)")
print(f"c1 needed for A_obs = 4.69e-5: {4.69e-5/(coef/nu):.3f} (paper: 1.54)")
# eq.(7): Ic recovered from nu fixed by A_obs with c1 = 1 -- the 'one part in a thousand' claim depends on c1.
k1 = 3**0.5/2**(1/3)*(8*pi/3)**0.25
def Ic_of(nu_):                          # eq.(3), in Planck units: E_QG = 1/nu
    # / E_QG = * nu in Planck units; rho_L^2 rho_eq ~ 3e-359 underflows a float, so work in logs
    return -(2/(3*pi))*(math.log(k1) + (2*math.log(rhoL) + math.log(rhoE))/12 + math.log(nu_))
for c1 in (1.0, 1.54):
    nu_A = c1*coef/4.69e-5
    print(f"eq.(3) with nu from A_obs at c1 = {c1}: nu = {nu_A:.4g}, Ic = {Ic_of(nu_A):.5f}, Ic/(4 pi) = {Ic_of(nu_A)/(4*pi):.5f}")
print(f"sensitivity: dIc/dln(nu) = {-(2/(3*pi)):.4f}, so a factor 2 in nu moves Ic/(4 pi) by {(2/(3*pi))*math.log(2)/(4*pi):.4f}")
print(f"k1 = {k1:.4f} (paper: ~2.34)")

# check A: eq. (4) as read is the exact inverse of eq. (3) as read (pref == k1^-6), and round-trips.
print(f"check A: pref = {pref:.6e}, k1^-6 = {k1**-6:.6e}; Ic(nu_of(rhoL, rhoE)) = {Ic_of(nu):.12f} vs 4 pi = {4*pi:.12f}")
