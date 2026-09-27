#!/usr/bin/env python3
r"""
DOCKET 67 re-derivation for key 2405.05963-sec3.3
(Kontou 2024, "Wormhole restrictions from quantum energy inequalities",
 Universe 10 (2024) 291, arXiv:2405.05963; as used at
 research/warp-drive/qeihps.py:119-132, 395, 446-449, 508-510).

Kontou's sentence (wording confirmed this stage only through web-search
snippets of arxiv.org/pdf/2405.05963 -- the PDF itself was not reachable):
  "The DSNEC of Equation (49) currently makes sense only on Minkowski spacetime
   or at length scales sufficiently smaller than the curvature scale."
It is a scope statement (a status of the literature), not a theorem with a
proof; nothing in it is machine-checkable as such.  What IS finite and
closed-form, and is checked here:

 A. HPS throat data (qeihps.py:161-169: f'=f''=f'''=0, r'=r''=r'''=0,
    r(0)^2 = -16 K^2 L, K^2 = 1/(5760 pi)) give r_0^2 = 1/(540 pi) at L = -2/3
    and the printed 0.0242789 / 0.0171677 l_P.                        (sympy)
 B. For ds^2 = -f(l) dt^2 + dl^2 + r(l)^2 dOmega^2 with that throat data the
    only non-zero orthonormal Riemann component is R_(th ph th ph) = 1/r_0^2,
    and Kretschmann = 4/r_0^4.                                          (sympy)
 C. Over the WHOLE HPS range -1 <= L < 0, r_0 <= 1/sqrt(360 pi) = 0.0297 l_P:
    the throat is sub-Planckian for every admissible L, not only L = -2/3. (z3)
 D. Robustness to the unquantified "sufficiently smaller": for every factor
    k >= 1, no sampling length l with 1 <= l <= r_c/k exists at HPS's r_c
    (either definition).                                                 (z3)
 E. The owner's operationalisation (qeihps.py:446-449: MET iff
    kretschmann == 0 or min(radii) > 1) is NOT equivalent to Kontou's
    hypothesis:
    E1. Kretschmann == 0 does not imply Minkowski: the vacuum plane wave
        ds^2 = -2 du dv + (x^2 - y^2) du^2 + dx^2 + dy^2 has R_abcd != 0 and
        R_abcd R^abcd = 0.                                               (sympy)
    E2. min(radii) > 1 does not imply a length l with 1 <= l <= r_c/k exists:
        r_c in (1, k) passes the proxy and admits none (k = 10 witness).   (z3)
    Both are laxer than the source; neither changes the HPS verdict (FAILS
    under both proxy and literal reading), which D and C show directly.
"""
import sys
import sympy as sp
import z3

ok = True
def chk(name, cond):
    global ok
    ok &= bool(cond)
    print(("PASS " if cond else "FAIL ") + name)

# ---------------- A: r_0 at L = -2/3 ----------------
L = sp.Symbol('L', real=True)
K2 = 1 / (5760 * sp.pi)
r0sq = -16 * K2 * L
r0sq_L0 = sp.simplify(r0sq.subs(L, sp.Rational(-2, 3)))
chk("A1 r_0^2 = 1/(540 pi) at L=-2/3", sp.simplify(r0sq_L0 - 1 / (540 * sp.pi)) == 0)
r0 = sp.sqrt(r0sq_L0)
r0n = float(r0)
kr = float(r0 / sp.sqrt(2))
print("     r_0 = %.7f l_P ; r_0/sqrt2 = %.7f l_P" % (r0n, kr))
chk("A2 r_0 prints 0.0242789 (7 d.p.)", round(r0n, 7) == 0.0242789)
chk("A3 r_0/sqrt2 prints 0.0171677 (7 d.p.)", round(kr, 7) == 0.0171677)

# ---------------- B: orthonormal Riemann at the throat ----------------
t, l, th, ph = sp.symbols('t l theta phi', real=True)
X = [t, l, th, ph]
f = sp.Function('f')(l)
r = sp.Function('r')(l)
g = sp.diag(-f, 1, r**2, r**2 * sp.sin(th)**2)
gi = g.inv()
n = 4
Gam = [[[sp.simplify(sum(gi[a, d] * (sp.diff(g[d, b], X[c]) + sp.diff(g[d, c], X[b])
                                     - sp.diff(g[b, c], X[d])) for d in range(n)) / 2)
         for c in range(n)] for b in range(n)] for a in range(n)]
def Riem(a, b, c, d):   # R^a_{bcd}
    e = sp.diff(Gam[a][b][d], X[c]) - sp.diff(Gam[a][b][c], X[d])
    e += sum(Gam[a][c][m] * Gam[m][b][d] - Gam[a][d][m] * Gam[m][b][c] for m in range(n))
    return sp.simplify(e)
Rup = [[[[Riem(a, b, c, d) for d in range(n)] for c in range(n)] for b in range(n)] for a in range(n)]
Rdn = [[[[sp.simplify(sum(g[a, m] * Rup[m][b][c][d] for m in range(n)))
          for d in range(n)] for c in range(n)] for b in range(n)] for a in range(n)]
# orthonormal scale factors
h = [sp.sqrt(f), 1, r, r * sp.sin(th)]
f0, r0s = sp.symbols('f0 r0', positive=True)
throat = {}
for k in (3, 2, 1):
    throat[sp.diff(f, l, k)] = 0
    throat[sp.diff(r, l, k)] = 0
throat[f] = f0
throat[r] = r0s
def at_throat(e):
    return sp.simplify(e.subs(throat))
nonzero = {}
for a in range(n):
    for b in range(a + 1, n):
        for c in range(n):
            for d in range(c + 1, n):
                v = at_throat(Rdn[a][b][c][d] / (h[a] * h[b] * h[c] * h[d]))
                if v != 0:
                    nonzero[(a, b, c, d)] = v
print("     non-zero orthonormal R_(abcd), a<b, c<d, at throat:", nonzero)
chk("B1 only R_(th ph th ph) survives, = 1/r_0^2",
    set(nonzero) == {(2, 3, 2, 3)} and sp.simplify(nonzero[(2, 3, 2, 3)] - 1 / r0s**2) == 0)
Kfull = 0
for a in range(n):
    for b in range(n):
        for c in range(n):
            for d in range(n):
                if Rdn[a][b][c][d] == 0:
                    continue
                Kfull += Rdn[a][b][c][d] * sum(
                    gi[a, a] * gi[b, b] * gi[c, c] * gi[d, d] * Rdn[a][b][c][d] for _ in [0])
Kt = at_throat(Kfull)
chk("B2 Kretschmann at throat = 4/r_0^4", sp.simplify(Kt - 4 / r0s**4) == 0)
chk("B3 Kretschmann radius (4/r_0^4)^(-1/4) = r_0/sqrt2",
    sp.simplify((4 / r0s**4) ** sp.Rational(-1, 4) - r0s / sp.sqrt(2)) == 0)

# ---------------- C: whole HPS range sub-Planckian ----------------
s = z3.Solver()
Lz, R2 = z3.Reals('L R2')
pi_lo = z3.RealVal("3.14159")         # pi > 3.14159 -> R2 bound below is conservative
# R2 = r_0^2 = -16 L/(5760 pi) = -L/(360 pi) <= -L/(360*3.14159) ; ask for r_0 >= 1 anywhere
s.add(Lz >= -1, Lz < 0, R2 * 360 * pi_lo <= -Lz, R2 >= 1)
chk("C1 z3: no L in [-1,0) gives r_0 >= 1 l_P", s.check() == z3.unsat)
rmax = float(sp.sqrt(1 / (360 * sp.pi)))
print("     max r_0 over HPS range (L=-1) = %.5f l_P" % rmax)
chk("C2 max r_0 = 1/sqrt(360 pi) < 1", rmax < 1)

# ---------------- D: robust to the factor in 'sufficiently smaller' ----------------
for name, rc in (("r_c", r0n), ("Kretschmann radius", kr)):
    s = z3.Solver()
    kk, ll = z3.Reals('k l')
    rcz = z3.RealVal(repr(rc))
    s.add(kk >= 1, ll >= 1, ll * kk <= rcz)
    chk("D  z3: no k>=1, l>=l_P with l <= %s/k (%s = %.7f)" % (name, name, rc), s.check() == z3.unsat)

# ---------------- E1: Kretschmann = 0 but not Minkowski ----------------
u, v, x, y = sp.symbols('u v x y', real=True)
Y = [u, v, x, y]
H = x**2 - y**2
gp = sp.Matrix([[H, -1, 0, 0], [-1, 0, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])
gpi = gp.inv()
G2 = [[[sp.simplify(sum(gpi[a, d] * (sp.diff(gp[d, b], Y[c]) + sp.diff(gp[d, c], Y[b])
                                     - sp.diff(gp[b, c], Y[d])) for d in range(n)) / 2)
        for c in range(n)] for b in range(n)] for a in range(n)]
def Rp(a, b, c, d):
    e = sp.diff(G2[a][b][d], Y[c]) - sp.diff(G2[a][b][c], Y[d])
    e += sum(G2[a][c][m] * G2[m][b][d] - G2[a][d][m] * G2[m][b][c] for m in range(n))
    return sp.simplify(e)
RpU = [[[[Rp(a, b, c, d) for d in range(n)] for c in range(n)] for b in range(n)] for a in range(n)]
RpD = [[[[sp.simplify(sum(gp[a, m] * RpU[m][b][c][d] for m in range(n))) for d in range(n)]
         for c in range(n)] for b in range(n)] for a in range(n)]
RpUall = [[[[sp.simplify(sum(gpi[a, p] * gpi[b, q] * gpi[c, rr] * gpi[d, ss] * RpD[p][q][rr][ss]
                             for p in range(n) for q in range(n) for rr in range(n) for ss in range(n)))
             for d in range(n)] for c in range(n)] for b in range(n)] for a in range(n)]
Kp = sp.simplify(sum(RpD[a][b][c][d] * RpUall[a][b][c][d]
                     for a in range(n) for b in range(n) for c in range(n) for d in range(n)))
Ric = sp.Matrix(n, n, lambda b, d: sp.simplify(sum(RpU[a][b][a][d] for a in range(n))))
anyR = any(RpD[a][b][c][d] != 0 for a in range(n) for b in range(n) for c in range(n) for d in range(n))
chk("E1a plane wave is vacuum (Ricci = 0)", Ric == sp.zeros(n, n))
chk("E1b plane wave has R_abcd != 0 (R_uxux = %s)" % RpD[0][2][0][2], anyR)
chk("E1c plane wave Kretschmann = 0 -> owner's 'kretschmann == 0' proxy would mark it MET "
    "though it is not Minkowski", Kp == 0)

# ---------------- E2: min(radii) > 1 is necessary, not sufficient ----------------
s = z3.Solver()
rc, ll = z3.Reals('rc l')
kfix = z3.RealVal(10)
s.add(rc > 1)                                     # owner's proxy MET
s.add(z3.ForAll([ll], z3.Implies(ll >= 1, ll * kfix > rc)))   # no admissible sampling length
chk("E2 z3: exists r_c > 1 (proxy MET) admitting no l in [1, r_c/10]", s.check() == z3.sat)
if s.check() == z3.sat:
    print("     witness r_c =", s.model()[rc])

print("ALL PASS" if ok else "SOME FAIL")
sys.exit(0 if ok else 1)
