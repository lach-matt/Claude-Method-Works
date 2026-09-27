#!/usr/bin/env python3
"""DOCKET 67 re-derivation: 'zero (the NEC's RHS) ... saturated by the vacuum and by EM'
(research/warp-drive/bounds.py:43, :295).  Read-only on the tree.

Signature (-,+,+,+), Gaussian units T_ab = (1/4pi)(F_ac F_b^c - 1/4 g_ab F^2)  [K&S 2003.01815 eq 15 up to 4pi].
"""
import sys, random, math
import sympy as sp

ok = True
def chk(name, cond):
    global ok
    print(("PASS " if cond else "FAIL ") + name)
    ok &= bool(cond)

# ---------------- (A) symbolic: T_kk for Maxwell, general E, B, unit n
Ex, Ey, Ez, Bx, By, Bz, n1, n2, n3 = sp.symbols('Ex Ey Ez Bx By Bz n1 n2 n3', real=True)
eta = sp.diag(-1, 1, 1, 1)
# F_{mu nu} lower: F_{0i} = -E_i, F_{ij} = eps_ijk B_k
E = sp.Matrix([Ex, Ey, Ez]); B = sp.Matrix([Bx, By, Bz]); n = sp.Matrix([n1, n2, n3])
F = sp.zeros(4, 4)
for i in range(3):
    F[0, i+1] = -E[i]; F[i+1, 0] = E[i]
F[1, 2] = Bz; F[2, 1] = -Bz
F[2, 3] = Bx; F[3, 2] = -Bx
F[3, 1] = By; F[1, 3] = -By
ginv = eta.inv()
Fmix = F * ginv                       # F_a^c
F2 = sum(F[a, b]*(ginv*F*ginv)[a, b] for a in range(4) for b in range(4))
T = (F * ginv * F.T - sp.Rational(1, 4)*eta*F2) / (4*sp.pi)   # T_ab = F_ac F_bd g^cd - 1/4 g_ab F^2
chk("A0 T_00 = (E^2+B^2)/8pi", sp.simplify(T[0, 0] - (E.dot(E)+B.dot(B))/(8*sp.pi)) == 0)
chk("A1 trace g^ab T_ab = 0 (Maxwell traceless in 4D, K&S eq 37 at n=4, m=0)",
    sp.simplify(sum(ginv[a, a]*T[a, a] for a in range(4))) == 0)
k = sp.Matrix([1, n1, n2, n3])
Tkk = sp.expand((k.T*T*k)[0, 0])
Eperp = E - E.dot(n)*n
sos = (Eperp + n.cross(B)).dot(Eperp + n.cross(B)) / (4*sp.pi)
unit = n1**2 + n2**2 + n3**2 - 1
def zero_mod_unit(expr):
    _, rem = sp.reduced(sp.expand(expr), [unit], n3, n2, n1, Ex, Ey, Ez, Bx, By, Bz)
    return sp.expand(rem) == 0
chk("A2 T_ab k^a k^b = |E_perp + n x B|^2/4pi modulo |n|=1 (Groebner remainder 0; a sum of squares => NEC holds for every F)",
    zero_mod_unit(Tkk - sos))

# ---------------- (B) numeric: every F (generic, non-null) has null k with T_kk = 0 (principal null directions)
import numpy as np
rng = np.random.default_rng(67)
def Tnum(Ev, Bv):
    f = sp.lambdify((Ex, Ey, Ez, Bx, By, Bz), T, 'numpy')
    return np.array(f(*Ev, *Bv), dtype=float)
Tf = sp.lambdify((Ex, Ey, Ez, Bx, By, Bz), T, 'numpy')
Ff = sp.lambdify((Ex, Ey, Ez, Bx, By, Bz), F, 'numpy')
etan = np.diag([-1., 1, 1, 1])
worst_pnd = 0.0; min_over_sphere = []
for trial in range(200):
    Ev = rng.normal(size=3); Bv = rng.normal(size=3)
    Tn = np.array(Tf(*Ev, *Bv), float); Fn = np.array(Ff(*Ev, *Bv), float)
    # principal null directions: eigenvectors of F^a_b = g^ac F_cb with eigenvalue real +-lambda, null
    Fup = etan @ Fn
    w, V = np.linalg.eig(Fup)
    found = 0
    for j in range(4):
        if abs(w[j].imag) < 1e-9 and abs(w[j].real) > 1e-9:
            v = V[:, j].real; v = v / v[0]
            norm = v @ etan @ v
            tkk = v @ Tn @ v
            worst_pnd = max(worst_pnd, abs(norm), abs(tkk) / (Tn[0, 0] + 1e-300))
            found += 1
    assert found == 2, (trial, w)
    # min of T_kk over a dense sphere grid, relative to T_00
    th = np.linspace(0, np.pi, 181); ph = np.linspace(0, 2*np.pi, 361)
    TH, PH = np.meshgrid(th, ph)
    N = np.stack([np.ones_like(TH), np.sin(TH)*np.cos(PH), np.sin(TH)*np.sin(PH), np.cos(TH)], -1)
    vals = np.einsum('...a,ab,...b->...', N, Tn, N)
    min_over_sphere.append(vals.min() / Tn[0, 0])
chk("B1 200 random non-null F: both principal null directions are null and give T_kk/T_00 < 1e-10 (max %.2e)"
    % worst_pnd, worst_pnd < 1e-10)
chk("B2 grid min of T_kk/T_00 over the null sphere is >= 0 and small (min %.3e, max %.3e)"
    % (min(min_over_sphere), max(min_over_sphere)), min(min_over_sphere) > -1e-12 and max(min_over_sphere) < 5e-3)

# ---------------- (C) null field (plane wave): T = Phi^2 l l, saturates at k = l
Tn = np.array(Tf(1, 0, 0, 0, 1, 0), float)
chk("C1 plane wave E=x, B=y: T_kk = 0 at k=(1,0,0,1): %.1e" % (np.array([1, 0, 0, 1]) @ Tn @ np.array([1, 0, 0, 1])),
    abs(np.array([1, 0, 0, 1]) @ Tn @ np.array([1, 0, 0, 1])) < 1e-15)
chk("C2 and T_ab = (1/4pi) l_a l_b exactly (type II null dust, MM&V eq 2.13, f=1/4pi)",
    np.allclose(Tn, np.outer([-1, 0, 0, 1], [-1, 0, 0, 1]) / (4*np.pi)))

# ---------------- (D) MM&V 1702.05915 eq 2.15 (mu, -mu, mu, mu): rho + p_1 = 0
mu = sp.symbols('mu', positive=True)
Td = sp.diag(mu, -mu, mu, mu)
kd = sp.Matrix([1, 1, 0, 0])
chk("D1 pure electric field along x: T = diag(mu,-mu,mu,mu), mu = E^2/8pi",
    np.allclose(np.array(Tf(1, 0, 0, 0, 0, 0), float), np.diag([1, -1, 1, 1]) / (8*np.pi)))
chk("D2 NEC along (1,1,0,0): rho + p1 = 0 -> saturated (MM&V NEC table rho+p_i>=0)", (kd.T*Td*kd)[0, 0] == 0)

# ---------------- (E) z3: no real E,B,n with |n|=1 and T_kk < 0
try:
    import z3
    ex, ey, ez, bx, by, bz, a, b, c = z3.Reals('ex ey ez bx by bz a b c')
    En = [ex, ey, ez]; Bn = [bx, by, bz]; nn = [a, b, c]
    dotEE = sum(x*x for x in En); dotBB = sum(x*x for x in Bn)
    nE = sum(x*y for x, y in zip(nn, En)); nB = sum(x*y for x, y in zip(nn, Bn))
    ExB = [ey*bz - ez*by, ez*bx - ex*bz, ex*by - ey*bx]
    nExB = sum(x*y for x, y in zip(nn, ExB))
    # sympy-derived closed form (4pi T_kk) re-typed: E^2+B^2-(n.E)^2-(n.B)^2-2 n.(ExB)
    tkk4pi = dotEE + dotBB - nE*nE - nB*nB - 2*nExB
    # first confirm this closed form equals sympy's Tkk
    closed = (E.dot(E)+B.dot(B)-E.dot(n)**2-B.dot(n)**2-2*n.dot(E.cross(B)))/(4*sp.pi)
    chk("E0 closed form 4pi T_kk = E^2+B^2-(n.E)^2-(n.B)^2-2n.(ExB) equals the tensor contraction",
        zero_mod_unit(Tkk - closed))
    # E1: direct nonnegativity is beyond z3's nlsat in 60 s here (it returned 'unknown' on the first run);
    # so z3 is asked the equivalent finite question with the SOS witness: is there a unit n where
    # 4pi T_kk differs from |E_perp + n x B|^2 ?  unsat + a square is >= 0  =>  NEC holds.
    Ep = [En[i] - nE*nn[i] for i in range(3)]
    nxB = [b*bz - c*by, c*bx - a*bz, a*by - b*bx]
    sosz = sum((Ep[i] + nxB[i])**2 for i in range(3))
    s = z3.Solver(); s.set('timeout', 120000)
    s.add(a*a + b*b + c*c == 1, tkk4pi != sosz)
    r = s.check()
    chk("E1 z3: {|n|=1, 4pi T_kk != |E_perp + n x B|^2} is %s (unsat = identity holds, hence T_kk >= 0)" % r, r == z3.unsat)
    s3 = z3.Solver(); s3.set('timeout', 60000)
    s3.add(a*a + b*b + c*c == 1, tkk4pi < 0)
    r3 = s3.check()
    print("INFO E1b z3 direct {|n|=1, 4pi T_kk < 0}: %s (unknown is a solver limit, not evidence either way)" % r3)
    s2 = z3.Solver(); s2.set('timeout', 60000)
    s2.add(a*a + b*b + c*c == 1, tkk4pi == 0, dotEE + dotBB > 0, ex*bx + ey*by + ez*bz != 0)
    r2 = s2.check()
    chk("E2 z3: a non-null F (E.B != 0) with T_kk = 0 at some null k exists: %s" % r2, r2 == z3.sat)
except ImportError:
    print("SKIP z3 not installed")

# ---------------- (F) the classical-class hypothesis is load-bearing: nonminimal scalar violates the zero RHS
# K&S eq (39), flat space (G_ab = 0): T_kk = (1-2xi)(k.dphi)^2 - 2 xi phi (k.d)^2 phi
xi, ph, d1, d2 = 1.0, 1.0, 0.0, 1.0
tkk = (1 - 2*xi)*d1**2 - 2*xi*ph*d2
chk("F1 nonminimal scalar xi=1, phi=1, k.dphi=0, (k.d)^2 phi=1: T_kk = %.1f < 0 (classical violation)" % tkk, tkk < 0)
# minimally coupled scalar: T_kk = (k.dphi)^2; saturation needs a null k orthogonal to dphi -> only if dphi non-timelike
dphi = np.array([1.0, 0.3, 0.0, 0.0])   # timelike gradient (lower index)
mins = min((np.array([1, math.sin(t)*math.cos(p), math.sin(t)*math.sin(p), math.cos(t)]) @ dphi)**2
           for t in np.linspace(0, math.pi, 91) for p in np.linspace(0, 2*math.pi, 181))
chk("F2 minimal scalar with timelike grad: min_k (k.dphi)^2 = %.3f > 0 -> NOT saturated there; EM saturates at EVERY point" % mins, mins > 0.4)

# ---------------- (G) Tipler/K&S Prop 2.1 scaling: an unnormalised infimum is always 0, so 'saturated' must mean T_kk=0 at a NONZERO null k
Tpf = np.diag([1.0, 0.2, 0.2, 0.2])      # perfect fluid rho=1, p=0.2: NEC strict
kk = np.array([1, 1, 0, 0.])
chk("G1 perfect fluid rho=1,p=.2: T_kk(r k) = r^2 * 1.2 -> inf over unnormalised k is 0 but never attained",
    abs((1e-3*kk) @ Tpf @ (1e-3*kk) - 1.2e-6) < 1e-15)

# ---------------- (H) the tree's own coding (read-only import)
sys.path.insert(0, '/home/user/Claude-Method-Works/research/warp-drive')
try:
    import bounds
    row = [r for r in bounds.BOUNDS if r[0].startswith("zero")][0]
    chk("H1 bounds.py zero row: W,B,S,G,K,Z = %s ; K = 0 (known saturated)" % (row[1:7],), row[5] == 0 and row[2] == 0)
    chk("H2 zero row counted in bounds.saturated() (count %d)" % len(bounds.saturated()), row[0] in bounds.saturated())
except Exception as e:
    print("SKIP tree import:", e)

print("RESULT:", "ALL PASS" if ok else "FAILURES")
sys.exit(0 if ok else 1)
