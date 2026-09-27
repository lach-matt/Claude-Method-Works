#!/usr/bin/env python3
"""DOCKET 67 -- re-derivation for key pinamonti-siemssen-flrw-existence.

What the tree uses (throatmass.py:147-151): the flat-FLRW semiclassical
existence family is 'not a throat', 'cosmological, not static', 'm < 0
reported: False'.  None of the four papers could be read at source in this
run (alphaXiv quota exceeded; arxiv.org egress-blocked), so this script checks
only what is closed-form and does NOT depend on the papers' text:

  C1  Misner-Sharp mass on flat FLRW is H^2 R^3 / (2G) >= 0 for EVERY a(t),
      so 'm < 0' is impossible on the class -- a geometric theorem, not a
      reported tally.  Contrast k = -1, where m can be negative.
  C2  The class contains a static member: a = const is Minkowski (H = 0,
      m = 0).  'not static' holds for the non-trivial members only.
  C3  Curvature identities on flat FLRW used by any trace-anomaly analysis:
      Ric^2 - R^2/3 = -12 H^2 (Hdot + H^2);  (3)H_ab = 3 H^4 g_ab on de Sitter.
  C4  The critical value a web-search summary of Pinamonti-Siemssen's
      abstract attributes to the paper, 'H_c = 180 pi / G': with the
      conformal-scalar anomaly coefficient 1/(2880 pi^2) (fixed here by the
      de Sitter energy density H^4/(960 pi^2), a literature fixture NOT read
      in this run) and the Box R coefficient set to zero, the trace equation's
      Hdot coefficient vanishes at H^2 = 180 pi / G (hbar = c = 1), and the
      Starobinsky de Sitter point sits at H^2 = 360 pi / G.  So '180 pi / G'
      is a value of H^2, not of H -- a notation point in a summary, recorded,
      not a discrepancy in the paper (the paper was not read).
  C5  With a non-zero Box R coefficient the trace equation contains d^3H/dt^3:
      the reduced second-order system (and hence C4's H_c) exists only for
      that renormalisation choice.
Exit 0 iff every check holds.
"""
import sys
import sympy as sp

t, r, G = sp.symbols('t r G', positive=True)
k = sp.Symbol('k')
a = sp.Function('a')(t)
H = sp.diff(a, t) / a
ok = True


def check(name, cond):
    global ok
    print(("PASS " if cond else "FAIL ") + name)
    ok = ok and bool(cond)


# ---------- C1: Misner-Sharp mass, FLRW with curvature k ----------
# g = -dt^2 + a^2 (dr^2/(1-k r^2) + r^2 dOmega^2); areal radius R = a r.
R_areal = a * r
gtt, grr = -1, (1 - k * r**2) / a**2          # inverse metric components
gradR2 = gtt * sp.diff(R_areal, t)**2 + grr * sp.diff(R_areal, r)**2
m_MS = sp.simplify(R_areal / (2 * G) * (1 - gradR2))
m_expected = R_areal**3 * (H**2 + k / a**2) / (2 * G)
check("C1a Misner-Sharp m = R^3 (H^2 + k/a^2)/(2G) on FLRW",
      sp.simplify(m_MS - m_expected) == 0)
m_flat = sp.simplify(m_MS.subs(k, 0))
check("C1b flat: m = H^2 R^3/(2G), a sum of squares times positives (>= 0)",
      sp.simplify(m_flat - (sp.diff(a, t) * r)**2 * a * r / (2 * G)) == 0)
# k = -1 counterexample: a(t) = t (Milne-like) gives H^2 - 1/a^2 = 0; take a = t/2
m_open = m_MS.subs(k, -1).subs(a, t / 2).doit()
val = sp.simplify(m_open.subs({t: 1, r: 1, G: 1}))
check("C1c open (k=-1) FLRW admits m < 0 (a = t/2, t=r=G=1 gives m = %s)" % val,
      val < 0)

# ---------- C2: a = const is a static member of the flat class ----------
a0 = sp.Symbol('a0', positive=True)
check("C2 a = const: H = 0 and m = 0 (Minkowski, static, m not negative)",
      sp.simplify(m_flat.subs(a, a0).doit()) == 0)

# ---------- C3: curvature of flat FLRW ----------
x, y, z = sp.symbols('x y z')
coords = [t, x, y, z]
g = sp.diag(-1, a**2, a**2, a**2)
ginv = g.inv()
n = 4
Gam = [[[sum(ginv[i, l] * (sp.diff(g[l, j], coords[kk]) + sp.diff(g[l, kk], coords[j])
                            - sp.diff(g[j, kk], coords[l])) for l in range(n)) / 2
         for kk in range(n)] for j in range(n)] for i in range(n)]


def ricci(i, j):
    return sp.simplify(sum(sp.diff(Gam[l][i][j], coords[l]) - sp.diff(Gam[l][i][l], coords[j])
                           + sum(Gam[l][l][mm] * Gam[mm][i][j] - Gam[l][j][mm] * Gam[mm][i][l]
                                 for mm in range(n)) for l in range(n)))


Ric = sp.Matrix(n, n, lambda i, j: ricci(i, j))
Rs = sp.simplify(sum(ginv[i, j] * Ric[i, j] for i in range(n) for j in range(n)))
Hd = sp.diff(H, t)
check("C3a R = 6 (Hdot + 2 H^2)", sp.simplify(Rs - 6 * (Hd + 2 * H**2)) == 0)
Ric_up = ginv * Ric * ginv
Ric2 = sp.simplify(sum(Ric[i, j] * Ric_up[i, j] for i in range(n) for j in range(n)))
check("C3b Ric^2 - R^2/3 = -12 H^2 (Hdot + H^2)",
      sp.simplify(Ric2 - Rs**2 / 3 + 12 * H**2 * (Hd + H**2)) == 0)
# (3)H_ab on de Sitter, a = exp(h t)
h = sp.Symbol('h', positive=True)
RicM = Ric.subs(a, sp.exp(h * t)).doit()
gM = g.subs(a, sp.exp(h * t))
gMinv = gM.inv()
RsM = sp.simplify(sum(gMinv[i, j] * RicM[i, j] for i in range(n) for j in range(n)))
RicMix = RicM * gMinv                        # R_a^c
Ric2M = sp.simplify(sum(RicM[i, j] * (gMinv * RicM * gMinv)[i, j] for i in range(n) for j in range(n)))
H3 = sp.simplify(RicMix * RicM - sp.Rational(2, 3) * RsM * RicM
                 - Ric2M / 2 * gM + RsM**2 / 4 * gM)
check("C3c (3)H_ab = 3 h^4 g_ab on de Sitter", sp.simplify(H3 - 3 * h**4 * gM) == sp.zeros(4, 4))

# ---------- C4: critical H^2 from the trace equation ----------
Hs, Hdot_s = sp.symbols('H Hdot', real=True)
cA = sp.Symbol('cA')                         # <T> = cA * (Ric^2 - R^2/3)  (Box R coeff = 0)
T_trace = cA * (-12 * Hs**2 * (Hdot_s + Hs**2))
# fix cA from the de Sitter energy density rho = H^4/(960 pi^2):
# on dS T_ab = -rho g_ab (signature -+++), trace = -4 rho.
cA_val = sp.solve(sp.Eq(T_trace.subs(Hdot_s, 0), -4 * Hs**4 / (960 * sp.pi**2)), cA)[0]
check("C4a anomaly coefficient = 1/(2880 pi^2)", sp.simplify(cA_val - 1 / (2880 * sp.pi**2)) == 0)
# trace of G_ab = 8 pi G T_ab:  -R = 8 pi G <T>
eq = -6 * (Hdot_s + 2 * Hs**2) - 8 * sp.pi * G * T_trace.subs(cA, cA_val)
coeff = sp.expand(eq).coeff(Hdot_s, 1)
Hc2 = sp.solve(sp.Eq(coeff, 0), Hs**2) if False else sp.solve(sp.Eq(coeff.subs(Hs, sp.sqrt(sp.Symbol('X', positive=True))), 0))
Xs = sp.Symbol('X', positive=True)
Hc2 = sp.solve(sp.Eq(coeff.subs(Hs**2, Xs), 0), Xs)
print("     Hdot coefficient:", sp.simplify(coeff), "; vanishes at H^2 =", Hc2)
check("C4b Hdot coefficient vanishes at H^2 = 180 pi / G", Hc2 == [180 * sp.pi / G])
dS = sp.solve(sp.Eq(eq.subs(Hdot_s, 0).subs(Hs**2, Xs).subs(Hs**4, Xs**2), 0), Xs)
dS = [s for s in dS if s != 0]
print("     Starobinsky de Sitter point H^2 =", dS)
check("C4c de Sitter point at H^2 = 360 pi / G = 2 x critical", dS == [360 * sp.pi / G])

# ---------- C5: Box R term raises the order ----------
Hf = sp.Function('H')(t)
Rf = 6 * (sp.diff(Hf, t) + 2 * Hf**2)
BoxR = sp.expand(-sp.diff(Rf, t, 2) - 3 * Hf * sp.diff(Rf, t))   # Box f(t) = -f'' - 3H f'
H3d = sp.diff(Hf, t, 3)
c3 = BoxR.coeff(H3d)
print("     Box R =", BoxR)
check("C5 Box R contains d^3H/dt^3 (coefficient -6): a non-zero Box R coefficient "
      "makes the trace equation third order in H, so C4's reduced equation needs it zero",
      sp.simplify(c3 + 6) == 0)

print("ALL PASS" if ok else "SOME CHECK FAILED")
sys.exit(0 if ok else 1)
