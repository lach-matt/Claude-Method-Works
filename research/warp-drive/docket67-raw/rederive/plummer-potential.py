#!/usr/bin/env python3
"""
DOCKET 67 -- re-derivation of the Plummer-smoothed point-mass potential as
research/warp-drive/concentric.py uses it (lines 42-47, 98-111, 163-168):

    Phi(r) = m / sqrt(r^2 + a^2)  -  m / max(r, R_s)       (G = c = 1)

inside the composite.py metric  ds^2 = -(1+2Phi) dt^2 + (1-2Phi) dx^2.

Checks (sympy exact unless marked numeric):
  A. Poisson: the first term is the Plummer (1911) potential-density pair with
     total mass -m; enclosed-mass law; the core is NOT compactly supported.
  B. Shell: the second term is a thin shell of mass +m at R_s (Gauss jump),
     with zero Hessian inside (Newton's shell theorem).
  C. Far field: no 1/r term for r > R_s (monopoles cancel exactly); leading
     tail -m a^2/(2 r^3).  Numeric check of the header's quoted values
     (concentric.py:51 'Phi(1000) = -6.2e-13, against Phi(1) = +4.4e-3').
  D. Optical tidal matrix of the exact (non-linearised) composite metric at the
     ray's closest approach (0, b, 0), k = (1,1,0,0), e = y, z: trace ratio vs
     the header's 3.99e-1, 1.97e-2, 7.55e-4 (concentric.py:104-107); plus the
     linear-order closed form.
  E. Where the tree's model metric stops being Lorentzian: 1 - 2 Phi = 0 at
     the core centre once m >~ a/2 (not a property of Plummer's result; of the
     weak-field metric it is inserted into).
  F. The owner's live trace_ratio (read-only import of the tree; optional).
Exit 0 iff every assertion holds.
"""
import math, os, sys
import sympy as sp

ok = True
def check(label, cond, detail=""):
    global ok
    ok &= bool(cond)
    print("  [%s] %s %s" % ("ok" if cond else "FAIL", label, detail))

r, a, m, Rs, x, y, z = sp.symbols("r a m R_s x y z", positive=True)

print("A. POISSON -- Plummer pair, mass -m")
phic = m / sp.sqrt(r**2 + a**2)
lap = sp.simplify(sp.diff(r**2 * sp.diff(phic, r), r) / r**2)
rho = sp.simplify(lap / (4 * sp.pi))                      # grad^2 Phi = 4 pi rho
plummer_rho = -(3 * m / (4 * sp.pi * a**3)) * (1 + r**2 / a**2) ** sp.Rational(-5, 2)
check("grad^2 [m/sqrt(r^2+a^2)] = -3 m a^2/(r^2+a^2)^(5/2)",
      sp.simplify(lap + 3 * m * a**2 / (r**2 + a**2) ** sp.Rational(5, 2)) == 0)
check("rho = Plummer profile of mass -m: -(3m/4 pi a^3)(1+r^2/a^2)^(-5/2)",
      sp.simplify(rho - plummer_rho) == 0)
Menc = sp.simplify(sp.integrate(4 * sp.pi * r**2 * rho, (r, 0, sp.Symbol("R", positive=True))))
R = sp.Symbol("R", positive=True)
check("enclosed mass M(<R) = -m R^3/(R^2+a^2)^(3/2)",
      sp.simplify(Menc + m * R**3 / (R**2 + a**2) ** sp.Rational(3, 2)) == 0)
Mtot = sp.limit(Menc, R, sp.oo)
check("total mass = -m", sp.simplify(Mtot + m) == 0, "(got %s)" % Mtot)
outside = sp.N((1 - (200 / sp.sqrt(200**2 + sp.Rational(2, 100)**2)) ** 3), 6)
check("core mass OUTSIDE R_s=200 at a=0.02 is nonzero (infinite extent)",
      0 < outside < 2e-8, "fraction = %s (~1.5 a^2/R_s^2 = %.3e)" % (outside, 1.5 * 0.02**2 / 200**2))

print("B. SHELL -- -m/max(r,R_s) is a thin shell of mass +m")
inner, outer = -m / Rs, -m / r
check("Laplacian zero inside and outside",
      sp.diff(r**2 * sp.diff(inner, r), r) == 0 and sp.simplify(sp.diff(r**2 * sp.diff(outer, r), r)) == 0)
jump = sp.simplify(4 * sp.pi * Rs**2 * (sp.diff(outer, r).subs(r, Rs) - sp.diff(inner, r)))
check("Gauss flux jump 4 pi R_s^2 [dPhi/dr] = 4 pi m  => shell mass +m",
      sp.simplify(jump - 4 * sp.pi * m) == 0)
check("continuous at R_s", sp.simplify(inner - outer.subs(r, Rs)) == 0)

print("C. FAR FIELD -- monopoles cancel")
far = sp.series(m / sp.sqrt(r**2 + a**2) - m / r, r, sp.oo, 7).removeO()
check("no 1/r term for r > R_s", sp.simplify(sp.limit(r * (m / sp.sqrt(r**2 + a**2) - m / r), r, sp.oo)) == 0)
check("leading tail -m a^2/(2 r^3)",
      sp.simplify(sp.limit(r**3 * (m / sp.sqrt(r**2 + a**2) - m / r), r, sp.oo) + m * a**2 / 2) == 0)

def Phi(rr, mm, aa, RR):
    import mpmath as mp
    mp.mp.dps = 40
    return float(mm / mp.sqrt(rr * rr + aa * aa) - mm / max(rr, RR))

vals = {}
for aa, RR in ((0.02, 200.0), (0.5, 200.0), (0.5, 30.0)):
    vals[(aa, RR)] = (Phi(1.0, 5e-3, aa, RR), Phi(1000.0, 5e-3, aa, RR))
    print("     m=5e-3 a=%-5g R_s=%-5g  Phi(1)=%+.4e  Phi(1000)=%+.4e" % ((aa, RR) + vals[(aa, RR)]))
p1, p1000 = vals[(0.02, 200.0)]
check("design point a=0.02: Phi(1) = 4.97400e-3 exactly-to-6-figures", abs(p1 - 4.97400e-3) < 1e-9, "(%.8e)" % p1)
check("owner selftest pin 4.9750e-3 is the a=0 value m - m/R_s; off by %.3e, inside the owner's tol 1e-6 by %.1e"
      % (4.9750e-3 - p1, 1e-6 - abs(4.9750e-3 - p1)),
      abs(5e-3 - 5e-3 / 200 - 4.9750e-3) < 1e-15 and abs(4.9750e-3 - p1) <= 1e-6)
check("design point a=0.02: Phi(1000) = -1.0e-15, NOT the header's -6.2e-13",
      abs(p1000 + 1.0e-15) < 1e-18 and abs(p1000 + 6.2e-13) > 1e-13)
q1, q1000 = vals[(0.5, 200.0)]
check("header values (Phi(1)=+4.4e-3, Phi(1000)=-6.2e-13) are the a=0.5, R_s=200 values",
      round(q1, 4) == 4.4e-3 and round(q1000, 14) == -6.2e-13 or (abs(q1 - 4.4e-3) < 5e-5 and abs(q1000 + 6.2e-13) < 1e-14 + 0.06e-13))
# at a = 0.02, is there ANY m giving both header values?  Phi(1000) fixes m a^2.
m_req = 6.2e-13 * 2 * 1000.0**3 / 0.02**2
check("at a=0.02 no single m gives both header values (Phi(1000) needs m=%.3g, then Phi(1)=%.3g)"
      % (m_req, Phi(1.0, m_req, 0.02, 200.0)), abs(Phi(1.0, m_req, 0.02, 200.0) - 4.4e-3) > 1)

print("D. OPTICAL TIDAL MATRIX of the exact composite metric at (0,b,0)")
X = (sp.Symbol("t"), x, y, z)
def tidal_exact(mm, aa, RR, b=1.0):
    rr = sp.sqrt(x**2 + y**2 + z**2)
    ph = mm / sp.sqrt(rr**2 + aa**2) - mm / RR            # inside the shell
    g = sp.diag(-(1 + 2 * ph), 1 - 2 * ph, 1 - 2 * ph, 1 - 2 * ph)
    gi = g.inv()
    pt = {x: 0, y: b, z: 0}
    n = 4
    dg = [[[sp.diff(g[i, j], X[k]) for k in range(n)] for j in range(n)] for i in range(n)]
    Gam = [[[sum(gi[l, s] * (dg[s][i][j] + dg[s][j][i] - dg[i][j][s]) for s in range(n)) / 2
             for j in range(n)] for i in range(n)] for l in range(n)]
    def Riem_up(l, i, j, k):   # R^l_{ijk}
        e = sp.diff(Gam[l][i][k], X[j]) - sp.diff(Gam[l][i][j], X[k])
        e += sum(Gam[l][j][s] * Gam[s][i][k] - Gam[l][k][s] * Gam[s][i][j] for s in range(n))
        return e
    gpt = g.subs(pt)
    kv = [1, 1, 0, 0]
    E = ([0, 0, 1, 0], [0, 0, 0, 1])
    # T_ij = -R_{m a n b} k^m e_i^a k^n e_j^b ;  R_{m a n b} = g_{m l} R^l_{a n b}
    T = [[0.0, 0.0], [0.0, 0.0]]
    for I in range(2):
        for J in range(2):
            s = 0
            for M_ in range(n):
                if kv[M_] == 0: continue
                for N_ in range(n):
                    if kv[N_] == 0: continue
                    A_ = [q for q in range(n) if E[I][q]][0]
                    B_ = [q for q in range(n) if E[J][q]][0]
                    s += gpt[M_, M_] * Riem_up(M_, A_, N_, B_).subs(pt)
            T[I][J] = -float(sp.N(s, 30))
    return T

header = {0.5: 3.99e-1, 0.1: 1.97e-2, 0.02: 7.55e-4}
exact = {}
for aa in (0.5, 0.1, 0.02):
    T = tidal_exact(5e-3, aa, 200.0)
    ratio = abs(T[0][0] + T[1][1]) / max(abs(T[0][0]), abs(T[1][1]))
    exact[aa] = ratio
    print("     a=%-5g T_yy=%+.6e T_zz=%+.6e  |tr|/|max| = %.4e   header %.3e  rel.diff %+.2e"
          % (aa, T[0][0], T[1][1], ratio, header[aa], ratio / header[aa] - 1))
check("exact-metric trace ratios reproduce the header at a=0.5, 0.1 to <0.1%",
      all(abs(exact[aa] / header[aa] - 1) < 1e-3 for aa in (0.5, 0.1)))
check("at a=0.02 exact-metric ratio is %.4e vs header 7.55e-4 (+%.1f%%): a discrepancy, still < 1e-3"
      % (exact[0.02], 100 * (exact[0.02] / 7.55e-4 - 1)),
      1e-2 < exact[0.02] / 7.55e-4 - 1 < 2e-2 and exact[0.02] < 1e-3)
check("monotone in compactness", exact[0.5] > exact[0.1] > exact[0.02])

# linear order in m, closed form: T_ab = -R_{kakb}, with h = -2Phi diag(1,1,1,1)
f = sp.Function("F")(x, y, z)
# linearised Riemann for g = eta + h, h_tt = -2 Phi, h_ij = -2 Phi delta_ij (static)
ph = m / sp.sqrt(x**2 + y**2 + z**2 + a**2)
H = lambda i, j: (-2 * ph if i == j else 0)
def d(e, i): return 0 if i == 0 else sp.diff(e, X[i])
def Rlin(al, be, ga, de):
    return (d(d(H(al, de), be), ga) + d(d(H(be, ga), al), de)
            - d(d(H(al, ga), be), de) - d(d(H(be, de), al), ga)) / 2
kv = [1, 1, 0, 0]
def Tlin(A_, B_):
    return -sum(Rlin(M_, A_, N_, B_) for M_ in (0, 1) for N_ in (0, 1))
b = sp.Symbol("b", positive=True)
Tyy = sp.simplify(Tlin(2, 2).subs({x: 0, y: b, z: 0}))
Tzz = sp.simplify(Tlin(3, 3).subs({x: 0, y: b, z: 0}))
trace = sp.simplify(Tyy + Tzz)
print("     linear order:  T_yy =", sp.factor(Tyy), "   T_zz =", sp.factor(Tzz))
print("                    trace =", sp.factor(trace))
lin_ratio = sp.simplify(sp.Abs(trace) / sp.Max(sp.Abs(Tyy), sp.Abs(Tzz)))
check("linear-order tr T = -R_kk = -2 grad^2 Phi = +6 m a^2/(b^2+a^2)^(5/2)  (R_kk < 0: defocusing, rho < 0)",
      sp.simplify(trace - 6 * m * a**2 / (b**2 + a**2) ** sp.Rational(5, 2)) == 0)
check("linear-order ratio |tr|/|T_zz| = 2 a^2/(a^2+b^2) exactly (b/a = 50 -> 8.0e-4)",
      sp.simplify(trace / Tzz - 2 * a**2 / (a**2 + b**2)) == 0 and sp.simplify(sp.Abs(Tzz) - sp.Abs(Tyy)) != 0)
for aa in (0.5, 0.1, 0.02):
    lr = float(lin_ratio.subs({a: aa, b: 1, m: 5e-3}))
    print("     a=%-5g linear-order ratio %.4e  (exact metric %.4e)" % (aa, lr, exact[aa]))


print("E. WHERE THE MODEL METRIC DEGENERATES (1 - 2 Phi = 0 at the core centre)")
for mm in (3e-3, 5e-3, 1e-2, 2e-2, 4e-2, 8e-2):
    phi0 = mm / 0.02 - mm / 200.0
    rdeg = math.sqrt(max(0.0, (2 * mm / (1 + 2 * mm / 200.0)) ** 2 - 0.02**2)) if phi0 > 0.5 else None
    print("     m=%-6g Phi(0)=%.4f  g_xx(0)=1-2Phi=%+.4f  %s" % (
        mm, phi0, 1 - 2 * phi0,
        ("degenerate for r < %.4f (ray at b=1 never enters)" % rdeg) if rdeg else "Lorentzian everywhere"))
check("specthm's mu=5e-3 and 0.6 mu are Lorentzian everywhere (Phi(0)=0.25, 0.15)",
      1 - 2 * (5e-3 / 0.02) > 0 and 1 - 2 * (3e-3 / 0.02) > 0)
check("table rows m >= 2e-2 have a non-Lorentzian core centre", 1 - 2 * (2e-2 / 0.02 - 2e-2 / 200) < 0)

print("F. OWNER'S LIVE trace_ratio (read-only import; no file written)")
tree = "/home/user/Claude-Method-Works/research/warp-drive"
if os.path.isdir(tree) and "--no-tree" not in sys.argv:
    sys.dont_write_bytecode = True
    sys.path.insert(0, tree)
    import io, contextlib
    with contextlib.redirect_stdout(io.StringIO()):
        import concentric
    live = {aa: concentric.trace_ratio(5e-3, a=aa) for aa in (0.5, 0.1, 0.02)}
    for aa in live:
        print("     a=%-5g live %.4e  exact-sympy %.4e  header %.3e" % (aa, live[aa], exact[aa], header[aa]))
    check("owner's live trace_ratio reproduces its header to 3 figures",
          all(abs(live[aa] / header[aa] - 1) < 2e-3 for aa in live))
    print("     live/exact - 1:", {aa: "%+.2e" % (live[aa] / exact[aa] - 1) for aa in live})
    print("     owner adm_residual(5e-3) = %+.4e" % concentric.adm_residual(5e-3))
    check("owner's own adm_residual(5e-3) is ~-1e-15, not -6.2e-13",
          abs(concentric.adm_residual(5e-3)) < 1e-14)
else:
    print("     skipped")

print("\nRESULT:", "ALL CHECKS PASS" if ok else "SOME CHECK FAILED")
sys.exit(0 if ok else 1)
