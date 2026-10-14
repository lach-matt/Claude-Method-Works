#!/usr/bin/env python3
"""DOCKET 67 re-derivation: Plummer sphere enclosed mass, and the fraction outside R_s
as linstab.py:215-219/547-551/927-932 and specthm.py:524,648-661 use it.
Reads research/warp-drive only (import by path, no writes).  Exit 1 on any failed check."""
import sys, math
sys.dont_write_bytecode = True   # never write into research/warp-drive
import sympy as sp
import mpmath as mp
sys.path.insert(0, "/home/user/Claude-Method-Works/research/warp-drive")
FAIL = []
def chk(name, ok, detail=""):
    print(("PASS " if ok else "FAIL ") + name + ((" :: " + detail) if detail else ""))
    if not ok: FAIL.append(name)

r, a, R, G, M, x = sp.symbols('r a R G M x', positive=True)
# ---- (A) Newtonian (flat Poisson) derivation from the Plummer potential
Phi = -G*M/sp.sqrt(r**2 + a**2)
lap = sp.simplify(sp.diff(r**2*sp.diff(Phi, r), r)/r**2)
rho = sp.simplify(lap/(4*sp.pi*G))
chk("rho = 3 M a^2 / (4 pi (r^2+a^2)^(5/2))", sp.simplify(rho - 3*M*a**2/(4*sp.pi*(r**2+a**2)**sp.Rational(5, 2))) == 0, str(rho))
Menc = sp.simplify(sp.integrate(4*sp.pi*r**2*rho, (r, 0, R)))
chk("M(<R) = M R^3/(R^2+a^2)^(3/2)", sp.simplify(Menc - M*R**3/(R**2+a**2)**sp.Rational(3, 2)) == 0, str(Menc))
Mtot = sp.limit(Menc, R, sp.oo)
chk("total mass = M (finite, all mass accounted)", sp.simplify(Mtot - M) == 0)
gauss = sp.simplify((R**2*sp.diff(Phi, r)/G).subs(r, R))
chk("Gauss: R^2 Phi'(R)/G = M(<R)", sp.simplify(gauss - Menc) == 0)
frac_out = 1 - Menc/M
tree = 1 - (1 + (a/R)**2)**sp.Rational(-3, 2)
chk("fraction outside R = 1-(1+(a/R)^2)^(-3/2) (tree's formula) identically",
    sp.simplify(sp.powsimp(sp.expand_power_base(frac_out - tree, force=True), force=True)) == 0
    or all(abs(float((frac_out - tree).subs({a: av, R: Rv}))) < 1e-15 for av, Rv in [(0.3, 1.7), (2, 0.5), (0.02, 200.0), (1, 1)]))
# linear in M: sign of the core mass (negative in concentric/certify) does not change the fraction
chk("fraction is independent of M (so of its sign) -- Poisson is linear", sp.diff(frac_out, M) == 0)
# ---- (B) series used by linstab.py:929
ser = sp.series(1 - (1 + x)**sp.Rational(-3, 2), x, 0, 4).removeO()
chk("series 1-(1+x)^(-3/2) = 3x/2 - 15x^2/8 + 35x^3/16 + O(x^4)", sp.expand(ser - (sp.Rational(3, 2)*x - sp.Rational(15, 8)*x**2 + sp.Rational(35, 16)*x**3)) == 0)
# ---- (C) the tree's data
import concentric, certify, linstab
for mod in (concentric, certify):
    chk("%s: A_CORE = 0.02, R_SHELL = 200.0" % mod.__name__, (mod.A_CORE, mod.R_SHELL) == (0.02, 200.0))
mp.mp.dps = 50
av, Rv = mp.mpf('0.02'), mp.mpf('200')
exact = 1 - (1 + (av/Rv)**2)**mp.mpf(-1.5)
print("exact fraction (50 dps) =", mp.nstr(exact, 20))
fr_lin = float(linstab.plummer_mass_outside(sp))
fr_spec = 1.0 - (1.0 + (certify.A_CORE / certify.R_SHELL) ** 2) ** -1.5   # specthm.py:524 verbatim
print("linstab.plummer_mass_outside (sympy exact -> float) =", repr(fr_lin))
print("specthm.py:524 float expression =", repr(fr_spec), " printed %%.3e -> %.3e" % fr_spec)
chk("linstab value equals exact to 1e-15 relative", abs(fr_lin/float(exact) - 1) < 1e-15)
chk("specthm float value within 1e-7 relative of exact (cancellation, 1-(1+1e-8)^-1.5)",
    abs(fr_spec/float(exact) - 1) < 1e-7, "rel err %.2e" % abs(fr_spec/float(exact) - 1))
chk("specthm printed '%.3e' = 1.500e-08", "%.3e" % fr_spec == "1.500e-08")
xx = (av/Rv)**2
chk("linstab.py:929 near-check: |f - (3x/2 - 15x^2/8)| < 1e-12", abs(exact - (1.5*xx - mp.mpf(15)/8*xx**2)) < 1e-12,
    "residual %s (= 35x^3/16 order)" % mp.nstr(exact - (1.5*xx - mp.mpf(15)/8*xx**2), 5))
chk("fraction > 0 (so P2's vacuum-outside fails for the exact potential)", exact > 0)

# ---- (D) hypothesis drift: certify.py's EXACT exponential conformastatic metric, not flat Poisson
# ds^2 = -e^{2U} dt^2 + e^{-2U}(dr^2 + r^2 dOmega^2), U = certify.phi.  Misner-Sharp mass from areal radius.
U = sp.Function('U')(r)
Rar = r*sp.exp(-U)
gtt_inv, grr_inv = -sp.exp(-2*U), sp.exp(2*U)
mMS = sp.simplify(Rar/2*(1 - grr_inv*sp.diff(Rar, r)**2))
Up = sp.Symbol('Up')
target = r*sp.exp(-U)/2*(2*r*Up - r**2*Up**2)
chk("Misner-Sharp: m_MS = (r e^-U/2)(2 r U' - r^2 U'^2) for the exponential metric",
    sp.simplify(mMS.subs(sp.diff(U, r), Up) - target) == 0)
# Eulerian density from G_tt (full Einstein tensor, sympy), to integrate outside R_s as a second definition
t, th, ph = sp.symbols('t theta phi')
coords = [t, r, th, ph]
g = sp.diag(-sp.exp(2*U), sp.exp(-2*U), sp.exp(-2*U)*r**2, sp.exp(-2*U)*r**2*sp.sin(th)**2)
gi = g.inv()
def Gam(l, m_, n):
    return sum(gi[l, s]*(sp.diff(g[s, m_], coords[n]) + sp.diff(g[s, n], coords[m_]) - sp.diff(g[m_, n], coords[s])) for s in range(4))/2
Gm = [[[sp.simplify(Gam(l, m_, n)) for n in range(4)] for m_ in range(4)] for l in range(4)]
def Ric(m_, n):
    return sp.simplify(sum(sp.diff(Gm[l][m_][n], coords[l]) - sp.diff(Gm[l][m_][l], coords[n]) +
               sum(Gm[l][l][s]*Gm[s][m_][n] - Gm[l][n][s]*Gm[s][m_][l] for s in range(4)) for l in range(4)))
Rc = sp.Matrix(4, 4, lambda i, j: Ric(i, j))
Rs_ = sp.simplify(sum(gi[i, j]*Rc[i, j] for i in range(4) for j in range(4)))
Gtt = sp.simplify(Rc[0, 0] - g[0, 0]*Rs_/2)
rhoE = sp.simplify(Gtt*sp.exp(-2*U)/(8*sp.pi))       # T_ab u^a u^b, u = e^{-U} d_t
print("Eulerian rho, exponential metric:", rhoE)
lapU = sp.diff(r**2*sp.diff(U, r), r)/r**2
chk("rho_E = e^{2U}(2 lap U - U'^2)/(8 pi): the flat Poisson source (lap U/4pi, U = -Phi_N) plus an O(U'^2) nonlinear term and an e^{2U} factor",
    sp.simplify(rhoE - sp.exp(2*U)*(2*lapU - sp.diff(U, r)**2)/(8*sp.pi)) == 0)

def ms_num(m, rr, side):
    """m_MS at radius rr for certify.phi with mass m; side='in' uses the core branch at R_s-."""
    a_, Rs = mp.mpf('0.02'), mp.mpf('200')
    rr = mp.mpf(rr)
    Uv = m/mp.sqrt(rr**2 + a_**2) - (m/Rs if (side == 'in' or rr < Rs) else m/rr)
    Upv = -m*rr/(rr**2 + a_**2)**1.5 + (0 if (side == 'in' or rr < Rs) else m/rr**2)
    return rr*mp.exp(-Uv)/2*(2*rr*Upv - rr**2*Upv**2)
print("\n  m        m_MS(Rs-) core-inside    m_MS(Rs+)            GR fraction outside    Plummer f        rel. dev")
worst = 0
for m in (mp.mpf('1e-3'), mp.mpf('5e-3'), mp.mpf('1e-2'), mp.mpf('2e-2')):
    Rs = mp.mpf('200')
    m_in = ms_num(m, Rs, 'in')        # core's MS mass inside R_s (negative)
    m_out_edge = ms_num(m, Rs, 'out') # MS mass just outside the shell
    core_out = 0 - m_out_edge         # M_ADM = 0 at infinity; core's MS contribution beyond R_s
    fGR = core_out/(core_out + m_in)
    dev = fGR/exact - 1
    worst = max(worst, abs(dev))
    print("  %-7s  %-22s  %-19s  %-21s  %-15s  %s" % (mp.nstr(m, 3), mp.nstr(m_in, 12), mp.nstr(m_out_edge, 12),
          mp.nstr(fGR, 12), mp.nstr(exact, 12), mp.nstr(dev, 4)))
    chk("  m=%s: MS mass outside the shell = m*f to 1e-10 relative" % mp.nstr(m, 3), abs(m_out_edge/(m*exact) - 1) < 1e-10,
        "rel %s" % mp.nstr(m_out_edge/(m*exact) - 1, 3))
    chk("  m=%s: GR fraction deviates from Plummer f by ~ -m/(2 R_s)" % mp.nstr(m, 3),
        abs(dev + m/(2*Rs)) < 2*(m/(2*Rs))**2 + 1e-12, "dev %s vs -m/2Rs = %s" % (mp.nstr(dev, 4), mp.nstr(-m/(2*Rs), 4)))
# certify M_SEATED
chk("certify.M_SEATED = 0.02", certify.M_SEATED == 2.0e-2)
print("worst relative deviation of the GR (Misner-Sharp) fraction from Plummer's, m <= 0.02: %.3e" % worst)
chk("the deviation is below the printed precision (%.3e) of specthm.py:650",
    all("%.3e" % float(exact*(1 + s*worst)) == "1.500e-08" for s in (-1, 1)))
# second definition: integrate Eulerian rho over proper volume outside R_s, certify m
m = mp.mpf('0.02'); a_ = mp.mpf('0.02'); Rs = mp.mpf('200')
def Ufun(q): return m/mp.sqrt(q**2 + a_**2) - m/q
def U1(q): return -m*q/(q**2 + a_**2)**1.5 + m/q**2
def U2(q): return m*(2*q**2 - a_**2)/(q**2 + a_**2)**2.5 - 2*m/q**3
def rhoEn(q): return mp.exp(2*Ufun(q))*(2*(U2(q) + 2*U1(q)/q) - U1(q)**2)/(8*mp.pi)
Mout_E = mp.quad(lambda q: 4*mp.pi*q**2*mp.exp(-3*Ufun(q))*rhoEn(q), [Rs, 10*Rs, mp.inf])
print("proper-volume integral of Eulerian rho outside R_s (certify, m=0.02):", mp.nstr(Mout_E, 15), " vs -m f =", mp.nstr(-m*exact, 15))
chk("Eulerian proper-volume mass outside R_s = -m f to 1e-6 relative", abs(Mout_E/(-m*exact) - 1) < 1e-6,
    "rel %s" % mp.nstr(Mout_E/(-m*exact) - 1, 3))
print("\n%d checks failed" % len(FAIL) if FAIL else "\nALL CHECKS PASS")
sys.exit(1 if FAIL else 0)
