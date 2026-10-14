#!/usr/bin/env python3
"""DOCKET 67 -- re-derivation of sm-higgs-potential-tree.
Part A (sympy, exact): every polynomial identity the tree uses.
Part B (numeric): lambda, V_min, SI magnitude, the ~1200 overshoot, at the
  tree's READ m_h and at the other published m_h values; the order of the
  excess over the observed dark-energy density.
Part C (numeric, ESTIMATE): one-loop Landau-gauge Coleman-Weinberg depth
  V_eff(0) - V_eff(v) with Buttazzo et al. 1307.3536 Table 3 NLO MS-bar
  couplings at mu = M_t -- how far the tree-level depth moves at one loop.
Part D (sympy): the one-loop correction's second derivative is log-singular
  exactly at the tree spinodal -- the stability edge is a tree-level object.
Exit 1 if any exact identity fails."""
import math, sys
import sympy as sp

ok = True
def chk(name, cond):
    global ok
    print(("PASS " if cond else "FAIL ") + name)
    ok = ok and bool(cond)

# ---------------------------------------------------------------- Part A
lam, v, phi, f, eps, h, m2, lB = sp.symbols('lambda v phi f epsilon h m2 lambda_B', positive=True)
V = lam/4*(phi**2 - v**2)**2
Vp, Vpp = sp.diff(V, phi), sp.diff(V, phi, 2)
chk("A1 V'(v(1+f))/(lam v^3) = f(f+1)(f+2)",
    sp.simplify(Vp.subs(phi, v*(1+f))/(lam*v**3) - f*(f+1)*(f+2)) == 0)
chk("A2 m^2 = V''(v) = 2 lam v^2", sp.simplify(Vpp.subs(phi, v) - 2*lam*v**2) == 0)
chk("A3 V'(v) = 0 and V(v) = 0 in this normalisation (V(0) = lam v^4/4)",
    sp.simplify(Vp.subs(phi, v)) == 0 and sp.simplify(V.subs(phi, v)) == 0
    and sp.simplify(V.subs(phi, 0) - lam*v**4/4) == 0)
# the tree's V_min = -lam v^4/4 is V shifted so that V(0) = 0
Vc = V - lam*v**4/4
chk("A4 with V(0)=0: V_min = -lam v^4/4 = -m^2 v^2/8 (m^2 = 2 lam v^2)",
    sp.simplify(Vc.subs(phi, v) + lam*v**4/4) == 0 and
    sp.simplify((-lam*v**4/4) - (-(2*lam*v**2)*v**2/8)) == 0)
chk("A5 V''(0)/V''(v) = -1/2", sp.simplify(Vpp.subs(phi, 0)/Vpp.subs(phi, v) + sp.Rational(1, 2)) == 0)
# reduced radial equation f'' + 2f'/x = (1/2) f(f+1)(f+2), x = m r
chk("A6 V'/(v m^2) = (1/2) f(f+1)(f+2)",
    sp.simplify(Vp.subs(phi, v*(1+f))/(v*2*lam*v**2) - f*(f+1)*(f+2)/2) == 0)
q = sp.expand((f*(f+1)*(f+2)/2)/f)
chk("A7 q = 1 + (3/2) f + (1/2) f^2", sp.simplify(q - (1 + sp.Rational(3, 2)*f + f**2/2)) == 0)
# D20 holding cost at phi = v(1-eps), rho_EW = lam v^4/4
rho = lam*v**4/4
src = sp.simplify(-Vp.subs(phi, v*(1-eps))*v*(1-eps)/rho)
fld = sp.simplify((V.subs(phi, v*(1-eps)) - V.subs(phi, v))/rho)
chk("A8 source/rho_EW = 4 eps(2-eps)(1-eps)^2", sp.simplify(src - 4*eps*(2-eps)*(1-eps)**2) == 0)
chk("A9 field/rho_EW = eps^2 (2-eps)^2", sp.simplify(fld - eps**2*(2-eps)**2) == 0)
ser = sp.Poly(sp.expand(src + fld), eps).all_coeffs()[::-1]
chk("A10 total = 8 eps - 16 eps^2 + 12 eps^3 - ...", ser[:4] == [0, 8, -16, 12])
spin = sp.solve(sp.Eq(Vpp.subs(phi, v*(1-eps)), 0), eps)
chk("A11 V''=0 at eps = 1 - 1/sqrt(3) (in (0,1))",
    any(sp.simplify(s - (1 - 1/sp.sqrt(3))) == 0 for s in spin))
sf = sp.solve(sp.Eq(src, fld), eps)
chk("A12 source = field at eps = 1 - 1/sqrt(5) (in (0,1))",
    any(sp.simplify(s - (1 - 1/sp.sqrt(5))) == 0 for s in sf))
chk("A13 1-1/sqrt5 > 1-1/sqrt3 (equality point lies in the unstable range)",
    float(1 - 1/sp.sqrt(5)) > float(1 - 1/sp.sqrt(3)))
chk("A14 source/field -> 2/eps", sp.limit(eps*src/fld, eps, 0) == 2)
# Normalisation equivalence with the READ sources
# Buttazzo (6)/(55): V = -m^2|H|^2/2 + lam|H|^4, |H|^2 = h^2/2
VB = -m2*h**2/4 + lB*h**4/4
hmin2 = sp.solve(sp.diff(VB, h)/h, h**2) if False else [m2/(2*lB)]
chk("A15 Buttazzo form: min at h^2 = m^2/(2 lam), V''(min) = m^2, V = (lam/4)(h^2-v^2)^2 - lam v^4/4",
    sp.simplify(sp.diff(VB, h).subs(h, sp.sqrt(m2/(2*lB)))) == 0 and
    sp.simplify(sp.diff(VB, h, 2).subs(h, sp.sqrt(m2/(2*lB))) - m2) == 0 and
    sp.simplify(VB.subs(m2, 2*lB*v**2) - (lB/4*(h**2 - v**2)**2 - lB*v**4/4)) == 0)
# Buttazzo (11): lam_OS = G_mu M_h^2/sqrt2 == M_h^2/(2 V^2) with V = (sqrt2 G)^(-1/2)
G, Mh = sp.symbols('G M_h', positive=True)
chk("A16 G M_h^2/sqrt2 == M_h^2/(2 V^2), V=(sqrt2 G)^-1/2",
    sp.simplify(G*Mh**2/sp.sqrt(2) - Mh**2/(2*(1/sp.sqrt(sp.sqrt(2)*G))**2)) == 0)
# Martin (47)-(48): Sigma = v_M + H/sqrt2, m_H^2 = lam_M v_M^2, rho = -m_H^2 v_M^2/4, v_M = v/sqrt2
vM = v/sp.sqrt(2)
chk("A17 Martin rho_vac = -m_H^2 v_M^2/4 with v_M = v/sqrt2 equals -m_h^2 v^2/8",
    sp.simplify(-Mh**2*vM**2/4 + Mh**2*v**2/8) == 0)

# ---------------------------------------------------------------- Part B
GF_PDG = 1.1663788e-5           # tree's G_F (PDG); MuLan 1211.0960: 1.1663787(6)e-5
def vev(GF): return 1/math.sqrt(math.sqrt(2)*GF)
HBARC_GEV_M = 1.054571817e-34*2.99792458e8/1.602176634e-10   # GeV m
GEV4_SI = 1.602176634e-10/HBARC_GEV_M**3                     # J/m^3 per GeV^4
TAU0 = 2.073325e42              # pressure.py, internal
vv = vev(GF_PDG)
print("\nPart B   v = %.5f GeV" % vv)
for tag, mh in [("tree READ (PDG-2026 capture)", 125.13), ("withdrawn pin / PDG 2024", 125.20),
                ("Buttazzo 2013 input", 125.15), ("ATLAS Run1+2 2023", 125.11),
                ("low 3-sigma (125.13-0.33)", 124.80), ("high 3-sigma", 125.46)]:
    L = mh**2/(2*vv**2); Vm = -mh**2*vv**2/8
    print("  %-30s m_h=%.2f lam=%.9f V_min=%.4e GeV^4 |V|=%.4e J/m^3 ratio/TAU0=%.1f"
          % (tag, mh, L, Vm, abs(Vm)*GEV4_SI, abs(Vm)*GEV4_SI/TAU0))
L = 125.13**2/(2*vv**2)
chk("B1 lambda(125.13) = 0.129136053130 (higgs.py:602) to 1e-9 rel",
    abs(L/0.129136053130 - 1) < 1e-9)
chk("B2 Buttazzo Table 3 LO lambda 0.12917 reproduced from 125.15, V=246.21971",
    abs(125.15**2/(2*246.21971**2) - 0.12917) < 1e-5)
Vm = 125.13**2*vv**2/8
chk("B3 |V_min| ~ 1.19e8 GeV^4", abs(Vm/1.19e8 - 1) < 0.005)
chk("B4 |V_min| ~ 2.48e45 J/m^3", abs(Vm*GEV4_SI/2.48e45 - 1) < 0.005)
r = Vm*GEV4_SI/TAU0
chk("B5 overshoot ratio in (1e2, 1e4) and ~1200", 1e2 < r < 1e4 and abs(r/1200 - 1) < 0.01)
# observed dark energy: Planck 2018 (1807.06209) H0 = 67.36, Omega_L = 0.6847
H0 = 67.36e3/3.0856775814913673e22
rho_crit = 3*H0**2/(8*math.pi*6.67430e-11)*2.99792458e8**2   # J/m^3
rho_L = 0.6847*rho_crit
print("  rho_Lambda = %.3e J/m^3 = %.3e GeV^4; |V_min|/rho_Lambda = 10^%.2f"
      % (rho_L, rho_L/GEV4_SI, math.log10(Vm*GEV4_SI/rho_L)))
chk("B6 'some fifty-four orders' (higgs.py caveat a): log10 in [54,55)",
    54 <= math.log10(Vm*GEV4_SI/rho_L) < 55)

# ---------------------------------------------------------------- Part C
# one-loop CW, Landau gauge, MS-bar, mu = M_t, Buttazzo Table 3 couplings.
def Veff(hh, lam_, m_, yt, g2, gY, mu, loop=True):
    V0 = -m_**2*hh**2/4 + lam_*hh**4/4
    if not loop: return V0
    fields = [  # (n, M^2(h), c)
        (1, -m_**2/2 + 3*lam_*hh**2, 1.5),     # Higgs
        (3, -m_**2/2 + lam_*hh**2, 1.5),       # Goldstones
        (6, g2**2*hh**2/4, 5/6),               # W
        (3, (g2**2 + gY**2)*hh**2/4, 5/6),     # Z
        (-12, yt**2*hh**2/2, 1.5)]             # top
    V1 = 0.0
    for n, M2, c in fields:
        if M2 != 0:
            V1 += n*M2**2*(math.log(abs(M2)/mu**2) - c)   # real part
    return V0 + V1/(64*math.pi**2)
def argmin(F, a, b):
    for _ in range(200):
        x1, x2 = a + (b-a)*0.382, a + (b-a)*0.618
        if F(x1) < F(x2): b = x2
        else: a = x1
    return (a+b)/2
Mt = 173.34
print("\nPart C   one-loop depth estimate (Buttazzo 1307.3536 Table 3, mu = M_t)")
rows = {"LO": (0.12917, 125.15, 0.99561, 0.65294, 0.34972),
        "NLO": (0.12774, 132.37, 0.95113, 0.64754, 0.35940),
        "NNLO": (0.12604, 131.55, 0.94018, 0.64779, 0.35830)}
tree_depth = 125.15**2*246.21971**2/8
res = {}
for tag, (l_, m_, yt, g2, gY) in rows.items():
    for loop in (False, True):
        F = lambda x: Veff(x, l_, m_, yt, g2, gY, Mt, loop)
        hm = argmin(F, 150, 350)
        depth = F(1e-9) - F(hm)
        res[(tag, loop)] = (hm, depth)
        print("  %-4s %-8s h_min = %.2f GeV  depth V(0)-V(min) = %.4e GeV^4  /tree(OS) = %.3f"
              % (tag, "1-loop" if loop else "tree", hm, depth, depth/tree_depth))
d1 = res[("NLO", True)][1]/tree_depth
chk("C1 LO tree evaluation reproduces m_h^2 v^2/8 (sanity)",
    abs(res[("LO", False)][1]/tree_depth - 1) < 1e-3)
chk("C2 one-loop depth (NLO couplings) within factor 2 of tree -- ratio verdict (1e2,1e4) unmoved",
    0.5 < d1 < 2 and 1e2 < r*d1 < 1e4)
print("  overshoot ratio with the NLO one-loop depth: %.0f (tree: %.0f)" % (r*d1, r))

# ---------------------------------------------------------------- Part D
a, lm, hh, mu = sp.symbols('a lam h mu', real=True)
M2 = a + 3*lm*hh**2
term = M2**2*(sp.log(M2/mu**2) - sp.Rational(3, 2))
Ls = sp.Symbol('L')
d2 = sp.expand(sp.diff(term, hh, 2).subs(sp.log(M2/mu**2), Ls))
coef_log = sp.simplify(d2.coeff(Ls))
rest = sp.simplify(d2 - coef_log*Ls)
print("         non-log remainder at M^2=0:", sp.simplify(rest.subs(a, -3*lm*hh**2)))
print("\nPart D   d^2/dh^2 [M^4(ln M^2 - 3/2)] log coefficient:", sp.factor(coef_log))
# at the tree spinodal M^2 -> 0 with h != 0 the coefficient is 72 lam^2 h^2 + 6 lam M^2 -> 72 lam^2 h^2 > 0
chk("D1 log coefficient -> 72 lam^2 h^2 at M^2 = 0: the one-loop V'' ~ (72 lam^2 h^2/64pi^2) ln M^2 -> -inf",
    sp.simplify(coef_log.subs(a, -3*lm*hh**2) - 72*lm**2*hh**2) == 0)

# ---------------------------------------------------------------- Part E
# The data fix v (G_F) and V''(v) = m_h^2 only.  The trilinear is bounded
# (CMS PLB 861 (2025) 139210, as quoted by 2503.11548 p.2: -1.2 < kappa_lambda
# < 7.5 at 95% CL); the quartic is unmeasured.  Family with the SAME v and m_h:
#   V_b = a x^2 + b x^3,  x = phi^2 - v^2,  a = m^2/(8 v^2)   (b = 0 is the SM tree)
mm, bb, x_ = sp.symbols('m b x', real=True)
X = phi**2 - v**2
Vb = mm**2/(8*v**2)*X**2 + bb*X**3
chk("E1 V_b'(v) = 0 and V_b''(v) = m^2 for every b (same measured v, m_h)",
    sp.simplify(sp.diff(Vb, phi).subs(phi, v)) == 0 and
    sp.simplify(sp.diff(Vb, phi, 2).subs(phi, v) - mm**2) == 0)
kap = sp.simplify(sp.diff(Vb, phi, 3).subs(phi, v)/(3*mm**2/v))
chk("E2 kappa_lambda = 1 + 16 b v^4/m^2", sp.simplify(kap - (1 + 16*bb*v**4/mm**2)) == 0)
k = sp.Symbol('kappa', real=True)
bk = sp.solve(sp.Eq(kap, k), bb)[0]
depth = sp.simplify((Vb.subs(phi, 0) - Vb.subs(phi, v)).subs(bb, bk))
chk("E3 depth V(0)-V(v) = (m^2 v^2/8) (3 - kappa)/2",
    sp.simplify(depth - mm**2*v**2/8*(3 - k)/2) == 0)
r0 = sp.simplify((sp.diff(Vb, phi, 2).subs(phi, 0)/mm**2).subs(bb, bk))
chk("E4 V''(0)/V''(v) = -1/2 + 3(kappa-1)/8", sp.simplify(r0 - (-sp.Rational(1, 2) + 3*(k - 1)/8)) == 0)
# D20's leading ratio source/field -> 2/eps depends only on V''(v): holds for every b
rhoE = mm**2*v**2/8
srcb = -sp.diff(Vb, phi).subs(phi, v*(1-eps))*v*(1-eps)/rhoE
fldb = (Vb.subs(phi, v*(1-eps)) - Vb.subs(phi, v))/rhoE
chk("E5 source/field * eps -> 2 for every b (the 2/eps law is shape-independent at leading order)",
    sp.simplify(sp.limit(sp.simplify(eps*srcb/fldb), eps, 0)) == 2)
EDGES = {}
print("\nPart E   kappa    depth/SM   V''(0)/V''(v)   stability edge eps (V''=0 in (0,1))")
for kv in [-1.2, 0.0, 1.0, 2.0, 3.0, 5.0, 7.5]:
    bnum = (kv - 1)/16            # b v^4/m^2 with v = m = 1
    Vn = sp.Rational(1, 8)*(phi**2 - 1)**2 + sp.nsimplify(bnum)*(phi**2 - 1)**3
    d2n = sp.diff(Vn, phi, 2).subs(phi, 1 - eps)
    roots = [complex(rr) for rr in sp.Poly(sp.expand(d2n), eps).nroots()]
    edge = sorted(rr.real for rr in roots if abs(rr.imag) < 1e-12 and 0 < rr.real < 1)
    EDGES[kv] = edge
    print("          %5.1f   %+.3f      %+.4f         %s" % (kv, (3 - kv)/2, -0.5 + 3*(kv - 1)/8,
          ["%.4f" % e for e in edge] or "none in (0,1)"))
chk("E6 kappa = 1 reproduces the SM edge 1 - 1/sqrt3; kappa = 2 moves it by > 30%",
    len(EDGES[1.0]) == 1 and abs(EDGES[1.0][0] - (1 - 1/math.sqrt(3))) < 1e-12
    and abs(EDGES[2.0][0]/EDGES[1.0][0] - 1) > 0.3)
chk("E7 within the CMS 95% interval the depth changes SIGN (kappa > 3 allowed): depth is NOT fixed by v, m_h",
    (3 - 7.5)/2 < 0 < (3 - (-1.2))/2)
# -v gauge-equivalent to +v in the doublet: -1_2 is in SU(2)
Mneg = sp.Matrix([[-1, 0], [0, -1]])
chk("E8 -1_2 in SU(2): det = 1, unitary (so H -> -H is a gauge transformation)",
    Mneg.det() == 1 and Mneg*Mneg.H == sp.eye(2))

print("\nALL EXACT/NUMERIC CHECKS PASS" if ok else "\nSOME CHECK FAILED")
sys.exit(0 if ok else 1)
