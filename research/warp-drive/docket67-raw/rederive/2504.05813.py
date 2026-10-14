#!/usr/bin/env python3
"""
DOCKET 67 -- re-derivation for Escriva arXiv:2504.05813 (v3, 28 Nov 2025), eqs. (2.3), (2.4), (2.5).

READ AT SOURCE (alphaXiv, pp.3-5, 12):
  (2.2)  ds^2 = -A^2 dt^2 + B^2 dr^2 + R^2 dOmega^2, zero shift ("comoving threading"),
         perfect fluid (2.1), u^t = 1/A ("comoving slicing").
  (2.3)  U = D_t R = (1/A) dR/dt,   Gamma = D_r R = (1/B) dR/dr.
  (2.4)  M(R) = int_0^R 4 pi Rt^2 rho dRt.
  (2.5)  Gamma = sqrt(1 + U^2 - 2M/R), "where Gamma is called the generalised Lorentz factor".
  p.12:  for type-II data "the throat-neck structure in the areal radius R ... causes the function
         Gamma to take negative values"; Fig. 2 panel Gamma spans about -0.5 .. 1.

CHECKS
  A. (2.5) squared, with M the GEOMETRIC Misner-Sharp mass 1-2M/R = g^ab d_aR d_bR, in the general
     diagonal spherically symmetric metric -- no perfect fluid, no field equation.  (driven.py V4.)
  B. (2.3) with a SHIFT: the literal U = (1/A) dR/dt fails the identity; the normal derivative passes.
     Escriva's zero-shift hypothesis is load-bearing for (2.3) as printed; driven.py's metric is diagonal.
  C. (2.4): the r-derivative of the geometric M from the Einstein tensor.  With comoving perfect fluid
     (T^t_r = 0, T^t_t = -rho) it is 4 pi rho R^2 R' = 4 pi Gamma rho R^2 B (= eq. 2.12), which with a
     regular centre integrates to (2.4).  With radial energy flux it is not -- (2.4) is a perfect-fluid /
     comoving statement; (2.5) with the geometric M is not.
  D. The square-root BRANCH: on a slice with R' < 0 (outward-oriented r, past a throat), Gamma < 0.
     Gamma = +sqrt(...) is then false, and the chain "dl < dR <=> Gamma > 1 <=> 2m/R < U^2"
     (driven.py:164, :386) breaks where Gamma < -1: 2m/R < U^2 holds, Gamma > 1 and dl < dR do not.
     Explicit metric: ds^2 = -dt^2 + dl^2 + R(l)^2 dOmega^2, R = sqrt(a^2 + k^2 l^2), k = 2.
  E. driven.py's own fixture gamma(1, 10, 1) = 1.341640786 re-computed from (2.5).
"""
import math
import sys

import sympy as sp

ok = True


def report(tag, cond, detail=""):
    global ok
    ok = ok and bool(cond)
    print(("PASS " if cond else "FAIL ") + tag + ("   " + detail if detail else ""))


t, r, th, ph = sp.symbols("t r theta phi", real=True)
X = [t, r, th, ph]


def ms_mass(g, R):
    gi = g.inv()
    gradR = sp.simplify(sum(gi[a, b] * sp.diff(R, X[a]) * sp.diff(R, X[b])
                            for a in range(4) for b in range(4)))
    return sp.simplify(R / 2 * (1 - gradR)), gradR


def einstein_mixed(g):
    """G^a_b for a 4-metric, by brute force (Christoffel -> Ricci)."""
    gi = g.inv()
    n = 4
    Gam = [[[sp.simplify(sum(gi[a, d] * (sp.diff(g[d, b], X[c]) + sp.diff(g[d, c], X[b])
                                          - sp.diff(g[b, c], X[d])) for d in range(n)) / 2)
             for c in range(n)] for b in range(n)] for a in range(n)]
    Ric = sp.zeros(n, n)
    for b in range(n):
        for c in range(n):
            Ric[b, c] = sp.simplify(
                sum(sp.diff(Gam[a][b][c], X[a]) for a in range(n))
                - sum(sp.diff(Gam[a][b][a], X[c]) for a in range(n))
                + sum(Gam[a][a][d] * Gam[d][b][c] for a in range(n) for d in range(n))
                - sum(Gam[a][c][d] * Gam[d][b][a] for a in range(n) for d in range(n)))
    Rs = sp.simplify(sum(gi[a, b] * Ric[a, b] for a in range(n) for b in range(n)))
    Gdn = Ric - Rs * g / 2
    return sp.simplify(gi * Gdn)


# ---------------------------------------------------------------- A
A = sp.Function("A", positive=True)(t, r)
B = sp.Function("B", positive=True)(t, r)
R = sp.Function("R", positive=True)(t, r)
g = sp.diag(-A**2, B**2, R**2, R**2 * sp.sin(th)**2)
M, gradR = ms_mass(g, R)
U = sp.diff(R, t) / A
Gm = sp.diff(R, r) / B
resA = sp.simplify(Gm**2 - (1 + U**2 - 2 * M / R))
report("A  (2.5)^2 in general diagonal metric, geometric MS mass, no matter model", resA == 0,
       "residual = %s" % resA)

# ---------------------------------------------------------------- B
beta = sp.Function("beta", real=True)(t, r)
gS = sp.Matrix([[-A**2 + B**2 * beta**2, B**2 * beta, 0, 0],
                [B**2 * beta, B**2, 0, 0],
                [0, 0, R**2, 0],
                [0, 0, 0, R**2 * sp.sin(th)**2]])
MS, _ = ms_mass(gS, R)
U_lit = sp.diff(R, t) / A
U_nor = (sp.diff(R, t) - beta * sp.diff(R, r)) / A
resB_lit = sp.simplify(Gm**2 - (1 + U_lit**2 - 2 * MS / R))
resB_nor = sp.simplify(Gm**2 - (1 + U_nor**2 - 2 * MS / R))
report("B1 with shift, literal U=(1/A)R_t: identity FAILS (residual nonzero)", resB_lit != 0,
       "residual = %s" % sp.factor(resB_lit))
report("B2 with shift, normal-derivative U=n^a d_a R: identity holds", resB_nor == 0,
       "residual = %s" % resB_nor)

# ---------------------------------------------------------------- C
G = einstein_mixed(g)
Mr = sp.diff(M, r)
# Try the Hayward (28a)-shaped combination: M' = 4 pi R^2 ( rho R' - flux * Rdot ) with
# 8 pi T^a_b = G^a_b, rho = -T^t_t, and T^t_r the radial energy-flux component.
cand = {}
for s in (1, -1):
    expr = sp.simplify(Mr - (R**2 / 2) * (-G[0, 0] * sp.diff(R, r) + s * G[0, 1] * sp.diff(R, t)))
    cand[s] = expr
sgood = [s for s in cand if cand[s] == 0]
report("C1 M' = (R^2/2)(-G^t_t R' + s G^t_r Rdot) for some sign s (Einstein-tensor identity)",
       len(sgood) == 1, "s = %s" % sgood)
s = sgood[0] if sgood else 1
rho = sp.Symbol("rho", positive=True)
# comoving perfect fluid: T^t_t = -rho, T^t_r = 0
Mr_pf = (R**2 / 2) * (8 * sp.pi * rho * sp.diff(R, r))
report("C2 comoving perfect fluid: M' = 4 pi rho R^2 R' = 4 pi Gamma rho R^2 B  (eq. 2.12 x B)",
       sp.simplify(Mr_pf - 4 * sp.pi * Gm * rho * R**2 * B) == 0)
# with flux q = T^t_r != 0 the extra term s*4 pi R^2 q Rdot survives -> (2.4) is not M
q = sp.Symbol("q", real=True)
extra = sp.simplify((R**2 / 2) * s * 8 * sp.pi * q * sp.diff(R, t))
report("C3 with radial flux T^t_r = q != 0 and Rdot != 0, M' picks up 4 pi R^2 q Rdot*s: (2.4) != M",
       extra != 0, "extra = %s" % extra)

# ---------------------------------------------------------------- D
l = sp.Symbol("l", real=True)
a, k = sp.Integer(1), sp.Integer(2)
Rl = sp.sqrt(a**2 + k**2 * l**2)
Gam_l = sp.diff(Rl, l)                  # B = 1, so Gamma = dR/dl
U_l = sp.Integer(0)                     # static
m_l = sp.simplify(Rl / 2 * (1 - Gam_l**2 + U_l**2))
l0 = -10
G0 = float(Gam_l.subs(l, l0))
R0 = float(Rl.subs(l, l0))
m0 = float(m_l.subs(l, l0))
g2 = 1 + 0.0 - 2 * m0 / R0
print("   D: at l = %d:  R = %.6f  Gamma = dR/dl = %.6f  m = %.6f  Gamma^2 = %.6f  sqrt(1+U^2-2m/R) = %.6f"
      % (l0, R0, G0, m0, G0 * G0, math.sqrt(g2)))
report("D1 identity Gamma^2 = 1+U^2-2m/R holds on the far side of the throat",
       abs(G0 * G0 - g2) < 1e-12)
report("D2 positive-root form Gamma = +sqrt(...) is FALSE there (Gamma < 0)",
       abs(G0 - math.sqrt(g2)) > 1.0, "Gamma = %.6f vs +sqrt = %.6f" % (G0, math.sqrt(g2)))
crit = 2.0 * m0 / R0 < 0.0 ** 2        # driven.contracts(m, R, U) body, verbatim: 2m/R < U^2
gam_gt1 = G0 > 1.0
dl, dR = 1.0, G0 * 1.0                  # dl along +l, dR = Gamma dl
report("D3 driven.py's contracts() criterion 2m/R < U^2 returns True there", crit)
report("D4 but 'Gamma > 1' is False and 'dl < dR' is False there (dR < 0)",
       (not gam_gt1) and not (dl < dR), "Gamma>1: %s, dl<dR: %s, |dR|>dl: %s" % (gam_gt1, dl < dR, abs(dR) > dl))
# and the same metric on the near side (l > 0) -- the chain holds when R' > 0
G1 = float(Gam_l.subs(l, 10)); m1 = float(m_l.subs(l, 10)); R1 = float(Rl.subs(l, 10))
report("D5 on the R' > 0 side the chain holds: Gamma > 1 and 2m/R < U^2 agree",
       (G1 > 1.0) == (2 * m1 / R1 < 0.0), "Gamma = %.6f" % G1)
# try to import the real function read-only (no bytecode written into the tree)
try:
    sys.dont_write_bytecode = True
    sys.path.insert(0, "/home/user/Claude-Method-Works/research/warp-drive")
    import driven  # noqa: E402
    real = driven.contracts(m0, R0, 0.0)
    report("D6 driven.contracts(m, R, 0) itself at l = -10 returns True (import, read-only)", real is True,
           "returned %r" % real)
except Exception as exc:  # pragma: no cover
    print("NOTE D6 not run: %r (D3 reproduces the one-line body)" % (exc,))

# ---------------------------------------------------------------- E
e = math.sqrt(1 + 1.0**2 - 2 * 1.0 / 10.0)
report("E  gamma(1,10,1) = sqrt(1.8) = 1.341640786 (driven.py:698 fixture)", abs(e - 1.341640786) < 1e-9,
       "%.12f" % e)

print("\nALL CHECKS AS EXPECTED" if ok else "\nSOME CHECK DID NOT COME OUT AS EXPECTED")
sys.exit(0 if ok else 1)
