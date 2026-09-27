#!/usr/bin/env python3
"""DOCKET 67 rederivation -- morris-thorne-1988-wormhole-throat.

Re-derives from the metric, with sympy, every quantity the tree quotes for a
Morris-Thorne throat, against the restatement READ at source in
Lobo arXiv:0710.4474 eqs (21)-(33) and Hochberg-Visser gr-qc/9704082 eqs (68),(72),
and the published witness Agnese & La Camera gr-qc/0203067 eq (17).

Metric (Lobo eq 1, G = c = 1, signature -+++):
    ds^2 = -e^{2 Phi(r)} dt^2 + dr^2/(1 - b(r)/r) + r^2 dOmega^2
Orthonormal-frame Einstein tensor -> rho, tau = -p_r, p_t.

Checks (each prints PASS/FAIL; exit 1 on any FAIL):
  C1  G_tt^ = b'/r^2, G_rr^ = -b/r^3 + 2(1-b/r)Phi'/r          (Lobo 21-22)
  C2  at the throat b = r_0 with Phi' FINITE (no Phi' = 0 needed):
      p_r(r_0) = -1/(8 pi r_0^2), i.e. tau(r_0) = 1/(8 pi r_0^2)   (Lobo 30; H-V 68)
  C3  Misner-Sharp mass from g_rr: 1 - 2m/r = 1 - b/r  =>  m = b/2, m(r_0) = r_0/2 > 0  (Lobo 32-33)
  C4  4 pi r_0^3 p_r(r_0) = -m(r_0)  -- the tree's V18 identity, the OPPOSITE sign to +m
  C5  flare-out (b - b' r)/(2 b^2) > 0 at the throat  <=>  b'(r_0) < 1  <=>  rho + p_r < 0 at r_0
      (Lobo 10, 39, 71): NEC violated at the throat; and it is NOT the sign of m(r_0), which is +.
  C6  Agnese-La Camera eq (17): p_par(r_0) = -m/(4 pi beta r_0^3) with r_0 = 2m/beta
      equals -1/(8 pi r_0^2) exactly, and m_MS = m/beta = r_0/2: an independent published witness.
  C7  the tree's own numeric function reproduced: wormhole_throat(3.0) values.
  C8  z3 (if installed): for all r0 > 0, 4 pi r0^3 * (-1/(8 pi r0^2)) + r0/2 == 0, and
      NOT EXISTS r0 > 0 with m(r0) = r0/2 < 0  (flare-out never means negative MS mass).
"""
import sys, math
import sympy as sp

fails = []
def chk(name, cond):
    print(("PASS  " if cond else "FAIL  ") + name)
    if not cond:
        fails.append(name)

t, r, th, ph = sp.symbols("t r theta phi", real=True)
Phi = sp.Function("Phi")(r)
b = sp.Function("b")(r)
x = [t, r, th, ph]
g = sp.diag(-sp.exp(2 * Phi), 1 / (1 - b / r), r ** 2, r ** 2 * sp.sin(th) ** 2)
ginv = g.inv()

def christoffel(g, ginv, x):
    n = len(x)
    return [[[sp.simplify(sum(ginv[a, d] * (sp.diff(g[d, bb], x[c]) + sp.diff(g[d, c], x[bb]) - sp.diff(g[bb, c], x[d])) for d in range(n)) / 2)
              for c in range(n)] for bb in range(n)] for a in range(n)]

Gam = christoffel(g, ginv, x)
n = 4
def riemann(a, bb, c, d):
    e = sp.diff(Gam[a][bb][d], x[c]) - sp.diff(Gam[a][bb][c], x[d])
    e += sum(Gam[a][c][e_] * Gam[e_][bb][d] - Gam[a][d][e_] * Gam[e_][bb][c] for e_ in range(n))
    return e
Ric = sp.Matrix(n, n, lambda bb, d: sp.simplify(sum(riemann(a, bb, a, d) for a in range(n))))
Rs = sp.simplify(sum(ginv[a, bb] * Ric[a, bb] for a in range(n) for bb in range(n)))
G = sp.simplify(Ric - Rs * g / 2)

# orthonormal components: G^_tt = -G^t_t = G_tt * e^{-2Phi};  G^_rr = G_rr * (1 - b/r)
Gtt_hat = sp.simplify(G[0, 0] * sp.exp(-2 * Phi))
Grr_hat = sp.simplify(G[1, 1] * (1 - b / r))
bp = sp.diff(b, r); Php = sp.diff(Phi, r)
chk("C1a G^_tt = b'/r^2 (Lobo 21)", sp.simplify(Gtt_hat - bp / r ** 2) == 0)
chk("C1b G^_rr = -b/r^3 + 2(1-b/r)Phi'/r (Lobo 22)", sp.simplify(Grr_hat - (-b / r ** 3 + 2 * (1 - b / r) * Php / r)) == 0)

rho = Gtt_hat / (8 * sp.pi)
p_r = Grr_hat / (8 * sp.pi)          # T^_rr = p_r = -tau
tau = -p_r

# C2: at the throat, b -> r0, with Phi' an arbitrary FINITE symbol (not zero)
r0, A, bp0 = sp.symbols("r_0 A bp0", real=True)   # A = Phi'(r0), finite; bp0 = b'(r0)
p_r_throat = sp.simplify(p_r.subs({Php: A}).subs({b: r0}).subs({r: r0}))
chk("C2  p_r(r_0) = -1/(8 pi r_0^2) for ANY finite Phi'(r_0) (Lobo 30, H-V 68)",
    sp.simplify(p_r_throat + 1 / (8 * sp.pi * r0 ** 2)) == 0)
chk("C2' the Phi' term at the throat is (1-b/r)Phi'/r -> 0 identically, so Phi'=0 is NOT a needed hypothesis",
    sp.simplify(((1 - b / r) * Php / r).subs({Php: A}).subs({b: r0}).subs({r: r0})) == 0)

# C3: Misner-Sharp mass from g_rr
m = sp.Function("m")(r)
msol = sp.solve(sp.Eq(1 - 2 * m / r, 1 - b / r), m)[0]
chk("C3a m(r) = b(r)/2 from g_rr (Lobo 32)", sp.simplify(msol - b / 2) == 0)
m_throat = msol.subs({b: r0}).subs({r: r0})
chk("C3b m(r_0) = r_0/2 > 0", sp.simplify(m_throat - r0 / 2) == 0)
# and dm/dr = 4 pi r^2 rho (the tt equation) -- consistency with certify.py's definition
chk("C3c dm/dr = 4 pi r^2 rho (certify.py's Misner-Sharp definition agrees)",
    sp.simplify(sp.diff(msol, r) - 4 * sp.pi * r ** 2 * rho) == 0)

# C4: the V18 identity
chk("C4  4 pi r_0^3 p_r(r_0) = -m(r_0)  (V18, opposite sign)",
    sp.simplify(4 * sp.pi * r0 ** 3 * p_r_throat + m_throat) == 0)
chk("C4' and NOT +m: 4 pi r_0^3 p_r(r_0) - m(r_0) = -r_0 != 0",
    sp.simplify(4 * sp.pi * r0 ** 3 * p_r_throat - m_throat + r0) == 0)

# C5: flare-out <=> b'(r0) < 1 <=> NEC violated at throat; independent of sign of m(r0)
flare = (b - bp * r) / (2 * b ** 2)
flare_throat = sp.simplify(flare.subs({bp: bp0}).subs({b: r0}).subs({r: r0}))
chk("C5a flare-out at throat = (1 - b'(r_0))/(2 r_0) (Lobo 10)", sp.simplify(flare_throat - (1 - bp0) / (2 * r0)) == 0)
nec_throat = sp.simplify((rho + p_r).subs({Php: A, bp: bp0}).subs({b: r0}).subs({r: r0}))
chk("C5b rho + p_r at throat = (b'(r_0) - 1)/(8 pi r_0^2) (Lobo 71)", sp.simplify(nec_throat - (bp0 - 1) / (8 * sp.pi * r0 ** 2)) == 0)
chk("C5c so flare-out > 0  <=>  b'(r_0) < 1  <=>  rho + p_r < 0 (NEC violated), exactly",
    sp.simplify(nec_throat * (-4 * sp.pi * r0) - flare_throat) == 0)
chk("C5d and m(r_0) = r_0/2 > 0 regardless of b'(r_0): flare-out is NOT negative Misner-Sharp mass",
    sp.simplify(m_throat.subs({bp0: -5}) - r0 / 2) == 0 and not m_throat.has(bp0))

# C6: Agnese & La Camera eq (17), a published witness
mA, beta = sp.symbols("m beta", positive=True)
r0A = 2 * mA / beta
p_par = -mA / (4 * sp.pi * beta * r0A ** 3)
chk("C6a A&LC eq (17): p_par(r_0) = -m/(4 pi beta r_0^3) = -1/(8 pi r_0^2) exactly",
    sp.simplify(p_par + 1 / (8 * sp.pi * r0A ** 2)) == 0)
chk("C6b A&LC eq (17) second form -beta^2/(32 pi m^2) agrees", sp.simplify(p_par + beta ** 2 / (32 * sp.pi * mA ** 2)) == 0)
# A = 1/(1 - 2m/(beta r)) => Misner-Sharp m_MS = m/beta, at throat = r0/2
chk("C6c A&LC m_MS = m/beta = r_0/2 at the throat", sp.simplify(mA / beta - r0A / 2) == 0)
chk("C6d A&LC 4 pi r_0^3 p_par = -m_MS (V19 as the tree states)", sp.simplify(4 * sp.pi * r0A ** 3 * p_par + mA / beta) == 0)

# C7: the tree's numeric function, reproduced literally (tolman.py:1439-1445)
def wormhole_throat(r0v):
    pr = -1.0 / (8.0 * math.pi * r0v * r0v)
    mm = r0v / 2.0
    return (pr, mm, 4.0 * math.pi * r0v ** 3 * pr)
prw, mw, fw = wormhole_throat(3.0)
chk("C7  tolman.wormhole_throat(3.0): 4 pi r_0^3 p_r == -m numerically (%.6g vs %.6g)" % (fw, -mw), abs(fw + mw) < 1e-12)
chk("C7' p_r(3.0) = -1/(72 pi) = %.6g" % prw, abs(prw + 1 / (72 * math.pi)) < 1e-15)

# C8: z3, if present
try:
    import z3
    R = z3.Real("r0")
    PI = z3.Real("pi")
    s = z3.Solver()
    s.add(PI > 3, PI < 4)                      # any positive pi; identity is pi-independent
    s.add(R > 0)
    # negate: exists r0>0 with 4 pi r0^3 (-1/(8 pi r0^2)) + r0/2 != 0
    s.add(4 * PI * R ** 3 * (-1 / (8 * PI * R ** 2)) + R / 2 != 0)
    chk("C8a z3: no r_0 > 0 refutes 4 pi r_0^3 p_r = -m  (unsat)", s.check() == z3.unsat)
    s2 = z3.Solver(); s2.add(R > 0, R / 2 < 0)
    chk("C8b z3: no r_0 > 0 has Misner-Sharp throat mass r_0/2 < 0  (unsat)", s2.check() == z3.unsat)
    # vacuity guard: the box is non-empty
    s3 = z3.Solver(); s3.add(R > 0, PI > 3, PI < 4)
    chk("C8c z3 vacuity guard: the domain r_0 > 0 is satisfiable", s3.check() == z3.sat)
except ImportError:
    print("SKIP  C8 z3 not installed")

print()
print("RESULT: %d FAIL" % len(fails) if fails else "RESULT: ALL PASS -- the tree's throat values agree with the source restatement;")
if not fails:
    print("        Phi'(r_0) = 0 is an ADDED hypothesis the source does not need (C2');")
    print("        flare-out <=> NEC violation at the throat, never negative Misner-Sharp mass (C5).")
sys.exit(1 if fails else 0)
