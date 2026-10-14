#!/usr/bin/env python3
"""DOCKET 67 re-derivation: the single-channel (single-mode) entropy/information
ceiling  S_dot <= sqrt(pi k^2 P / (3 hbar))  (nats; / ln 2 for bits), attributed
to Pendry 1983 (J. Phys. A 16, 2161) and used as a premise in branelink.py:38-42.

The source was NOT reachable at this stage (alphaXiv quota exhausted; arxiv.org,
iopscience, osti, semanticscholar all EGRESS_BLOCKED).  So this script does not
check Pendry's text; it re-derives the physics from first principles under
NAMED hypotheses and tests each hypothesis the tree's use would lean on:

  H1 one channel = one transverse mode, 1+1 propagation, unidirectional, no
     reflection (the transmitted flux of a single mode);
  H2 free (non-interacting) bosonic mode; energy measured from band bottom,
     zero-point excluded;
  H3 dispersion w(k) monotone, covering [0, inf) (field-blindness claim);
  H4 stationary state; entropy flux = von Neumann/Gibbs entropy flux of the
     occupation numbers; information = entropy (noiseless ideal receiver).

Units: hbar = k_B = 1 unless stated.  Exits 1 if any check fails.
"""
import math, sys
import numpy as np
import sympy as sp
from scipy.integrate import quad
from scipy.optimize import minimize_scalar, brentq

ok = True
def chk(name, got, want, tol=1e-9):
    global ok
    if isinstance(want, bool):
        good = (got == want)
    else:
        good = abs(got - want) <= tol * max(1.0, abs(want))
    ok &= good
    print(("PASS " if good else "FAIL ") + name + ": got %r want %r" % (got, want))

# ---------------------------------------------------------------- 1. closed form
w, T, n, lam = sp.symbols('omega T n lambda', positive=True)
nB = 1 / (sp.exp(w / T) - 1)
sB = (1 + n) * sp.log(1 + n) - n * sp.log(n)          # boson entropy per mode
xx = sp.symbols('x', positive=True)
# flux: dk/2pi * v_g = dw/2pi ; w = T x
# Bose integral int_0^inf x^(s-1)/(e^x-1) dx = Gamma(s) zeta(s); s = 2 -> pi^2/6
P_sym = T**2 * sp.gamma(2) * sp.zeta(2) / (2 * sp.pi)
print("     symbolic P =", sp.simplify(P_sym))
chk("1a0 Bose integral Gamma(2)zeta(2) vs quadrature",
    quad(lambda u: u/math.expm1(u), 1e-12, 80)[0], float(sp.gamma(2)*sp.zeta(2)), 1e-9)
P1 = float(P_sym.subs(T, 1))
chk("1a boson 1D energy flux P = pi T^2/12", P1, math.pi / 12)
S1 = quad(lambda x: ((1 + 1/np.expm1(x)) * np.log1p(1/np.expm1(x))
                     - (1/np.expm1(x)) * np.log(1/np.expm1(x))) / (2 * math.pi), 1e-12, 60)[0]
chk("1b boson 1D entropy flux S_dot = pi T/6", S1, math.pi / 6, 1e-7)
# S_dot^2 / P = pi/3 exactly (symbolic from the two closed forms)
chk("1c S_dot^2/P = pi/3 (the ceiling saturated by thermal)",
    float(sp.simplify((sp.pi*T/6)**2 / (sp.pi*T**2/12))), math.pi/3)

# ----------------------------------------------- 2. thermal is the maximiser (H4)
# Lagrange: d/dn [ s(n) - beta*w*n ] = 0  ->  n = 1/(e^{beta w}-1)
beta = sp.symbols('beta', positive=True)
sol = sp.solve(sp.Eq(sp.diff(sB, n), beta * w), n)
chk("2a stationary point of s(n)-beta w n is Bose-Einstein",
    sp.simplify(sol[0] - 1/(sp.exp(beta*w)-1)) == 0, True)
chk("2b s(n) strictly concave (so the stationary point is the max)",
    sp.simplify(sp.diff(sB, n, 2) + 1/(n*(1+n))) == 0, True)
# numeric: non-thermal occupations never beat the ceiling
rng = np.random.default_rng(67)
x = np.linspace(1e-4, 80, 40001); dx = x[1]-x[0]
def ratio_of(nw, wgrid=x):
    nw = np.clip(nw, 1e-300, None)
    s = (1+nw)*np.log1p(nw) - nw*np.log(nw)
    Sd = np.trapezoid(s, wgrid)/(2*math.pi); Pd = np.trapezoid(wgrid*nw, wgrid)/(2*math.pi)
    return Sd / math.sqrt(math.pi*Pd/3)
worst = 0.0
for _ in range(400):
    a, b, c = rng.uniform(0.2, 5), rng.uniform(0.5, 3), rng.uniform(0, 2)
    nw = c*np.exp(-(x/a)**b) + 1e-12
    worst = max(worst, ratio_of(nw))
chk("2c 400 random non-thermal spectra: max ratio < 1", worst < 1.0, True)
print("     (max ratio found %.6f; thermal gives %.6f)" % (worst, ratio_of(1/np.expm1(x))))

# ------------------------------------ 3. field-blindness = dispersion independence (H3)
# S_dot = int dk/2pi v_g(k) s(n(w(k))): for monotone w(k) onto [0,inf) = int dw/2pi s(n(w))
def flux_k(disp, vg, kmax, Tt=1.0):
    fS = lambda k: vg(k) * (lambda nn: (1+nn)*math.log1p(nn) - nn*math.log(nn))(1/math.expm1(disp(k)/Tt)) / (2*math.pi)
    fP = lambda k: vg(k) * disp(k) / math.expm1(disp(k)/Tt) / (2*math.pi)
    return quad(fS, 1e-9, kmax, limit=400)[0], quad(fP, 1e-9, kmax, limit=400)[0]
m = 3.0
cases = {
    "photon  w=c|k|":            (lambda k: k,               lambda k: 1.0,                   80),
    "phonon-like w=k^2 (Schr.)": (lambda k: k*k,             lambda k: 2*k,                   9),
    "massive, from band bottom": (lambda k: math.sqrt(k*k+m*m)-m, lambda k: k/math.sqrt(k*k+m*m), 200),
    "w=k^3":                     (lambda k: k**3,            lambda k: 3*k*k,                 4.5),
}
for name, (d, v, km) in cases.items():
    Sd, Pd = flux_k(d, v, km)
    chk("3 dispersion-blind: %s  S_dot^2/P" % name, Sd*Sd/Pd, math.pi/3, 1e-5)

# ----------------------- 3b. where H3 fails, the ceiling still bounds, not saturates
def best_ratio(wlo, whi):
    def r(Tt):
        g = np.linspace(wlo, whi, 20001)
        return ratio_of(1/np.expm1(g/Tt) + 1e-300, g)
    res = minimize_scalar(lambda lt: -r(math.exp(lt)), bounds=(-4, 6), method='bounded')
    return -res.fun
# FIRST RUN (recorded): a grid-trapezoid "max over T < 1" test FAILED at 1.000753 --
# grid error (the thermal reference on the same grid reads 1.000147), and the sup is
# approached as T -> 0 where the band edge is invisible.  Re-done by quadrature:
def band_ratio(Tt, W=1.0):
    sfun = lambda u: ((1+1/math.expm1(u))*math.log1p(1/math.expm1(u)) - (1/math.expm1(u))*math.log(1/math.expm1(u)))
    Sd = Tt*quad(sfun, 1e-14, W/Tt, limit=500)[0]/(2*math.pi)
    Pd = Tt*Tt*quad(lambda u: u/math.expm1(u), 1e-14, W/Tt, limit=500)[0]/(2*math.pi)
    return Sd/math.sqrt(math.pi*Pd/3)
br = [band_ratio(t) for t in (0.02, 0.05, 0.2, 1.0, 5.0, 50.0)]
print("     bounded band [0,1], T = .02,.05,.2,1,5,50 ->", ["%.8f" % r for r in br])
chk("3b bounded band: ratio < 1 at every finite T tested", all(r < 1.0 for r in br), True)
chk("3b' bounded band: ratio -> 1 as T -> 0 (sup, not max)", abs(band_ratio(0.01) - 1) < 1e-6, True)
chk("3c rest energy counted in P (band [m,inf), m=1): best ratio < 1",
    best_ratio(1.0, 80.0) < 1.0, True)
print("     rest energy counted: max over T = %.6f of ceiling" % best_ratio(1.0, 80.0))

# ------------------------------------------- 4. statistics: fermions (not field-blind)
def fermi_ratio(mu, Tt=1.0):
    g = np.linspace(1e-6, 80 + max(mu, 0), 40001)
    f = 1/(np.exp((g-mu)/Tt)+1); f = np.clip(f, 1e-300, 1-1e-16)
    s = -(f*np.log(f) + (1-f)*np.log1p(-f))
    Sd = np.trapezoid(s, g)/(2*math.pi); Pd = np.trapezoid(g*f, g)/(2*math.pi)
    return Sd/math.sqrt(math.pi*Pd/3)
chk("4a fermions, particles only, mu = -inf limit -> Boltzmann ratio < 1", fermi_ratio(-30) < 1, True)
# particle-hole symmetric channel (energy measured from Fermi level, both e and h counted):
# P = pi T^2/12 * (1/2)*2 ... compute: int_{-inf}^{inf}|e| ... one species, e>0 particles, holes e<0
g = np.linspace(1e-6, 60, 60001); f = 1/(np.exp(g)+1)
s = -(f*np.log(f)+(1-f)*np.log1p(-f))
Sd = 2*np.trapezoid(s, g)/(2*math.pi); Pd = 2*np.trapezoid(g*f, g)/(2*math.pi)
# FIRST RUN (recorded): this check expected pi/6 and FAILED -- the expectation was
# the auditor's error.  Electrons above and holes below E_F together SATURATE the ceiling:
chk("4b Fermi sea (e and h, mu=0): S_dot^2/P = pi/3 (ceiling saturated)", Sd*Sd/Pd, math.pi/3, 1e-5)
# a band whose bottom sits AT mu with no hole branch (particles only) carries 1/sqrt 2 of it
chk("4b' particles only, band bottom at mu: S_dot^2/P = pi/6", fermi_ratio(0.0)**2 * math.pi/3, math.pi/6, 1e-5)
res = minimize_scalar(lambda mu: -fermi_ratio(mu), bounds=(-20, 20), method='bounded')
print("     fermions from band bottom, best over mu: ratio %.6f at mu/T = %.3f" % (-res.fun, res.x))
chk("4c fermions from band bottom, best over mu: ratio < 1", -res.fun < 1.0, True)

# ---------------------------------------- 5. boost / Doppler invariance of S_dot^2/P
D = sp.symbols('D', positive=True)
Sp, Pp = sp.pi*(D*T)/6, sp.pi*(D*T)**2/12       # a Doppler-shifted 1D thermal flux is thermal at D T
chk("5a unidirectional massless: S'=D S, P'=D^2 P", sp.simplify(Sp/(sp.pi*T/6) - D) == 0 and
    sp.simplify(Pp/(sp.pi*T**2/12) - D**2) == 0, True)
chk("5b S_dot^2/P boost-invariant (ceiling frame-blind for massless 1D flux)",
    float(sp.simplify(Sp**2/Pp)), math.pi/3)
# the generic argument: entropy count invariant, arrival rate x D; energy per quantum x D, rate x D
chk("5c general unidirectional massless flux: (D S)^2/(D^2 P) = S^2/P",
    sp.simplify((D*sp.Symbol('S'))**2/(D**2*sp.Symbol('P')) - sp.Symbol('S')**2/sp.Symbol('P')) == 0, True)

# ------------------------------------------------ 6. multi-mode (H1 is essential)
N_, Ptot = sp.symbols('N P', positive=True)
# N equal channels, total P split equally, each at its own ceiling: sum = N sqrt(pi (P/N)/3) = sqrt(N) * single
multi = N_*sp.sqrt(sp.pi*(Ptot/N_)/3)
chk("6a N channels at total P: ceiling = sqrt(N) x single-mode ceiling",
    sp.simplify(multi/sp.sqrt(sp.pi*Ptot/3) - sp.sqrt(N_)) == 0, True)
# unequal split never beats equal split (concavity of sqrt; Cauchy-Schwarz)
p = rng.dirichlet(np.ones(7), 2000)
chk("6b 2000 random 7-way splits never exceed sqrt(7) x single",
    float(np.max(np.sum(np.sqrt(p), axis=1))) <= math.sqrt(7) + 1e-12, True)

# -------------------------------------- 7. the tree's S5 form and the unit conversion
A, hb = sp.symbols('A hbar', positive=True)
tree = sp.sqrt(A*sp.pi/(3*hb*sp.log(2)**2))            # branelink.py:350
pendry_bits = sp.sqrt(sp.pi*A/(3*hb))/sp.log(2)          # branelink.py:39, P -> A
chk("7 branelink N(A) == sqrt(pi P/(3 hbar))/ln 2 (nats -> bits by 1/ln 2)",
    sp.simplify(tree - pendry_bits) == 0, True)

# ----------------------------------------------------------- 8. data: hbar then/now
hbar_1973 = 1.0545887e-34      # CODATA 1973 (the value current in 1983)
hbar_now = 6.62607015e-34/(2*math.pi)   # exact since the 2019 SI redefinition
c_then = math.sqrt(math.pi*1.0/(3*hbar_1973))/math.log(2)
c_now = math.sqrt(math.pi*1.0/(3*hbar_now))/math.log(2)
print("     ceiling at P = 1 W: 1983 hbar -> %.6e bit/s; exact hbar -> %.6e bit/s; rel. move %.2e"
      % (c_then, c_now, c_now/c_then - 1))
chk("8 hbar move changes the 1 W ceiling by < 1e-5 relative", abs(c_now/c_then-1) < 1e-5, True)

# --------------------- 9. the same flux gives the thermal-conductance quantum
hs, kB = sp.symbols('h k_B', positive=True)
Pflux = sp.pi*kB**2*T**2/(12*(hs/(2*sp.pi)))
chk("9 dP/dT = pi^2 k^2 T/(3h) (single-channel thermal conductance quantum)",
    sp.simplify(sp.diff(Pflux, T) - sp.pi**2*kB**2*T/(3*hs)) == 0, True)

print("\nALL PASS" if ok else "\nSOME CHECK FAILED")
sys.exit(0 if ok else 1)
