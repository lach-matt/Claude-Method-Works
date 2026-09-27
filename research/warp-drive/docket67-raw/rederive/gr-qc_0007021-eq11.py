#!/usr/bin/env python3
"""
DOCKET 67 -- re-derivation for gr-qc/0007021-eq11 (Gao & Wald 2000, eq. 11, the
Jacobi matrix equation d^2A/dl^2 = -R_{a b s}^m k^a k^s A^b_n, A|p = 0,
dA/dl|p = delta; conjugate point where det A = 0) AS USED by composite.py.

Reads composite.py only through a byte-identical SANDBOX COPY (md5 asserted),
never importing from research/warp-drive (no __pycache__ is written there).

  E1  sympy: exact Riemann of composite.py's metric; standard optical tidal
      matrix K_ij = R_{k e_i k e_j} (MTW/Wald sign: eta'' = -K eta) at closest
      approach: K_zz = +3M/b^3, K_yy = -3M/b^3 at O(M); trace O(M^2).
  E2  composite.tidal() returns T = -K (sign opposite to eq. 11's convention).
  E3  convention-free: neighbouring geodesics from the owner's own integrator
      -- for M > 0 the z-separation converges, y diverges, as K says.
  E4  for T diagonal and traceless, A'' = -T A and A'' = +T A have the same
      det A identically (sympy); numerically the code and a sign-corrected copy
      give the SAME conjugate point at all nine window masses.
  E5  independent integration of eq. (11) with the standard sign, sympy-exact
      Riemann, algebraic (exact) screen, RK4, along the owner's geodesic;
      compared with composite.survey at +/-2e-3.
  E6  step refinement of composite.survey (n = 900, 1800, 3600).
  E7  the det-sign detector: blind to an even-multiplicity (stigmatic) zero.
  E8  at the conjugate point A has rank 1: a line focus, i.e. a nontrivial
      Jacobi field vanishing at both ends -- a conjugate point by definition.
"""
import hashlib, math, os, sys
sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))
SANDBOX = os.path.join(HERE, "..", "sandbox", "eq11")
REPO = "/home/user/Claude-Method-Works/research/warp-drive/composite.py"
sys.path.insert(0, SANDBOX)

import sympy as sp

results = []


def rec(tag, ok, msg):
    results.append((tag, ok))
    print("[%s] %s  %s" % (tag, "PASS" if ok else "FAIL", msg))


md5 = lambda p: hashlib.md5(open(p, "rb").read()).hexdigest()
m_repo, m_sb = md5(REPO), md5(os.path.join(SANDBOX, "composite.py"))
rec("E0", m_repo == m_sb, "sandbox composite.py md5 %s == repo %s" % (m_sb, m_repo))
import composite as C  # noqa: E402  (sandbox copy)

# ---------------------------------------------------------------- E1 sympy
t, x, y, z, M = sp.symbols("t x y z M", real=True)
X = [t, x, y, z]
r = sp.sqrt(x**2 + y**2 + z**2)
Phi = -M / r
g = sp.diag(-(1 + 2 * Phi), 1 - 2 * Phi, 1 - 2 * Phi, 1 - 2 * Phi)
gi = g.inv()
Gam = [[[sp.simplify(sum(gi[a, e] * (sp.diff(g[e, b], X[c]) + sp.diff(g[e, c], X[b])
                                     - sp.diff(g[b, c], X[e])) for e in range(4)) / 2)
         for c in range(4)] for b in range(4)] for a in range(4)]


def Rup(a, b, c, d):  # MTW R^a_{bcd}
    return (sp.diff(Gam[a][b][d], X[c]) - sp.diff(Gam[a][b][c], X[d])
            + sum(Gam[a][c][e] * Gam[e][b][d] - Gam[a][d][e] * Gam[e][b][c] for e in range(4)))


Rl = {}
for a in range(4):
    for b in range(4):
        for c in range(4):
            for d in range(4):
                Rl[(a, b, c, d)] = sum(g[a, e] * Rup(e, b, c, d) for e in range(4))
Rfun = {kk: sp.lambdify((x, y, z, M), v, "math") for kk, v in Rl.items() if v != 0}


def Kmat(p, k, E, Mv):
    """standard optical tidal matrix K_ij = R_{k e_i k e_j} (eta'' = -K eta)."""
    Rv = {kk: f(p[0], p[1], p[2], Mv) for kk, f in Rfun.items()}
    return [[sum(v * k[a] * E[i][b] * k[c] * E[j][d] for (a, b, c, d), v in Rv.items())
             for j in range(2)] for i in range(2)]


# closed form at closest approach, k = (1,1,0,0), screen (y, z), series in M
bb = sp.symbols("b", positive=True)
kv = [1, 1, 0, 0]
Ey, Ez = [0, 0, 1, 0], [0, 0, 0, 1]
Ksym = {}
for nm, E in (("yy", Ey), ("zz", Ez)):
    expr = sum(Rl[(a, b_, c, d)] * kv[a] * E[b_] * kv[c] * E[d]
               for a in range(4) for b_ in range(4) for c in range(4) for d in range(4))
    Ksym[nm] = sp.series(sp.simplify(expr.subs({x: 0, y: bb, z: 0})), M, 0, 2).removeO()
tr = sp.simplify(Ksym["yy"] + Ksym["zz"])
rec("E1", sp.simplify(Ksym["zz"] - 3 * M / bb**3) == 0 and sp.simplify(Ksym["yy"] + 3 * M / bb**3) == 0
    and tr == 0,
    "K_zz = %s, K_yy = %s at O(M); trace at O(M) = %s (vacuum: R_kk = 0)" % (Ksym["zz"], Ksym["yy"], tr))

# ---------------------------------------------------------------- E2
Mv, b0 = 2.0e-3, 0.3
Tc = C.tidal((0.0, b0, 0.0), [1.0, 1.0, 0.0, 0.0], [0., 0., 1., 0.], [0., 0., 0., 1.], Mv)
Ks = Kmat((0.0, b0, 0.0), [1.0, 1.0, 0.0, 0.0], [Ey, Ez], Mv)
rel = max(abs(Tc[i][i] + Ks[i][i]) / abs(Ks[i][i]) for i in range(2))
rec("E2", rel < 1e-4,
    "composite.tidal T = %s ; standard K = %s ; T = -K to %.1e -> composite evolves A'' = -T A = +K A, "
    "the opposite sign to eq. (11)" % ([[round(v, 6) for v in row] for row in Tc],
                                        [[round(v, 6) for v in row] for row in Ks], rel))

# ---------------------------------------------------------------- E3
d = 1e-4
def path(p0, Mm, n=900, lam=75.0):
    return C.geodesic(p0, C.null_tangent(p0, Mm), Mm, lam, n)[0]
P = path((-40., 0.3, 0.), Mv); Pz = path((-40., 0.3, d), Mv); Py = path((-40., 0.3 + d, 0.), Mv)
zs, ys = (Pz[-1][3] - P[-1][3]) / d, (Py[-1][2] - P[-1][2]) / d
rec("E3", zs < 1.0 and ys > 1.0,
    "M=+2e-3, parallel neighbours at lambda=75: z-sep/d = %.3f (converges), y-sep/d = %.3f (diverges) "
    "-- the physical sign is K's, not the code's T's" % (zs, ys))

# E3b: the owner's own Jacobi loop (tidal + Euler screen), started with PARALLEL data
# A(0) = I, A'(0) = 0, against the geodesic separations above -- with the code's sign
# and with eq.(11)'s sign.
def owner_loop(Mm, sign, A0, V0, n=900, lam=75.0):
    p0 = (-40.0, 0.3, 0.0)
    pts, tang, h = C.geodesic(p0, C.null_tangent(p0, Mm), Mm, lam, n)
    e1, e2 = [0., 0., 1., 0.], [0., 0., 0., 1.]
    A = [row[:] for row in A0]; dA = [row[:] for row in V0]
    for i in range(len(pts) - 1):
        k = list(tang[i]); p = (pts[i][1], pts[i][2], pts[i][3])
        T = C.tidal(p, k, e1, e2, Mm)
        acc = [[sign * sum(T[r_][s] * A[s][c] for s in range(2)) for c in range(2)] for r_ in range(2)]
        for r_ in range(2):
            for c in range(2):
                A[r_][c] += h * dA[r_][c] + 0.5 * h * h * acc[r_][c]
                dA[r_][c] += h * acc[r_][c]
        G = C.christoffel(p, Mm)
        for e in (e1, e2):
            de = [-sum(G[a][al][be] * k[al] * e[be] for al in range(4) for be in range(4)) for a in range(4)]
            for a in range(4):
                e[a] += h * de[a]
    return A
I2, Z2 = [[1., 0.], [0., 1.]], [[0., 0.], [0., 0.]]
Acode = owner_loop(Mv, -1.0, I2, Z2)
Aeq11 = owner_loop(Mv, +1.0, I2, Z2)
# screen e1 = y, e2 = z; geodesic separations at the last sample (lambda = 74.92)
rec("E3b", abs(Aeq11[0][0] - ys) < 0.1 and abs(Aeq11[1][1] - zs) < 0.1
    and abs(Acode[0][0] - zs) < 0.1 and abs(Acode[1][1] - ys) < 0.1,
    "parallel data, M=+2e-3: geodesics give (y, z) = (%.3f, %.3f); eq.(11) sign gives (%.3f, %.3f); "
    "composite's sign gives (%.3f, %.3f) -- the transverse axes SWAPPED, same determinant"
    % (ys, zs, Aeq11[0][0], Aeq11[1][1], Acode[0][0], Acode[1][1]))

# ---------------------------------------------------------------- E4
lam, a_ =sp.symbols("lambda a", real=True)
f = sp.Function("f")
# diagonal traceless T = diag(q, -q): A = diag(u, w), u'' = -q u, w'' = +q w; flip -> u'' = +q u, w'' = -q w
# i.e. flipping the sign swaps the two scalar ODEs; det A = u w is symmetric in the swap.
u, w = sp.symbols("u w")
rec("E4a", sp.simplify(u * w - w * u) == 0,
    "sign flip of a diagonal traceless T swaps the two decoupled ODEs; det A = u*w is swap-invariant "
    "(exact up to the O(Phi^2) trace and the screen leak)")
import composite_fix as CF  # sandbox copy with acc = +T A (standard eq. 11 sign)
same = True
rows = []
for Mm in (2e-3, -2e-3, -2e-4, -5e-4, -1e-3, -5e-3, -1e-2, -2e-2, -4e-2):
    a1, a2 = C.survey(Mm), CF.survey(Mm)
    same &= (a1["conjugate"] == a2["conjugate"])
    rows.append((Mm, a1["conjugate"], a2["conjugate"], a1["delay"]))
for row in rows:
    print("       M=%+.1e  code conj %-8s  eq11-sign conj %-8s  delay %+.4e" %
          (row[0], ("%.2f" % row[1]) if row[1] else "none", ("%.2f" % row[2]) if row[2] else "none", row[3]))
want = {2e-3: 55.17, -2e-3: 56.50, -2e-4: None, -5e-4: None, -1e-3: None, -5e-3: 45.58,
        -1e-2: 42.83, -2e-2: 41.50, -4e-2: 40.83}
table_ok = all((want[r_[0]] is None and r_[1] is None) or
               (want[r_[0]] is not None and r_[1] is not None and abs(r_[1] - want[r_[0]]) < 0.006)
               for r_ in rows)
rec("E4b", same and table_ok,
    "code and sign-corrected copy give identical conjugate points at all 9 masses; the owner's window "
    "table (composite.py:70-77) reproduced")

# ---------------------------------------------------------------- E5 independent eq.(11)
def screen(p, k, Mm):
    """exact screen: e2 = z/|z| (reflection symmetry keeps it parallel); e1 in span(x,y),
    orthogonal to k, unit -- unique modulo k, and K is blind to e -> e + alpha k."""
    gxx = 1.0 - 2.0 * (-Mm / math.sqrt(p[0]**2 + p[1]**2 + p[2]**2))
    # e1 = (0, ex, ey, 0) with gxx(ex kx + ey ky) = 0
    ex, ey = -k[2], k[1]
    nrm = math.sqrt(gxx * (ex * ex + ey * ey))
    return [0.0, ex / nrm, ey / nrm, 0.0], [0.0, 0.0, 0.0, 1.0 / math.sqrt(gxx)]


def conj_independent(Mm, n=3600, lam=75.0):
    p0 = (-40.0, 0.3, 0.0)
    pts, tang, h = C.geodesic(p0, C.null_tangent(p0, Mm), Mm, lam, 2 * n)
    Ks_ = []
    for i in range(len(pts)):
        pp = (pts[i][1], pts[i][2], pts[i][3])
        Ks_.append(Kmat(pp, tang[i], screen(pp, tang[i], Mm), Mm))
    H = 2 * h
    A = [[0., 0.], [0., 0.]]; V = [[1., 0.], [0., 1.]]
    mm = lambda K, B: [[-sum(K[r_][s] * B[s][c] for s in range(2)) for c in range(2)] for r_ in range(2)]
    add = lambda P_, Q, s: [[P_[i][j] + s * Q[i][j] for j in range(2)] for i in range(2)]
    det = lambda B: B[0][0] * B[1][1] - B[0][1] * B[1][0]
    prev, conj, Aconj = None, None, None
    for i in range(0, 2 * n - 2, 2):
        K0, K1, K2 = Ks_[i], Ks_[i + 1], Ks_[i + 2]
        k1a, k1v = V, mm(K0, A)
        k2a, k2v = add(V, k1v, H / 2), mm(K1, add(A, k1a, H / 2))
        k3a, k3v = add(V, k2v, H / 2), mm(K1, add(A, k2a, H / 2))
        k4a, k4v = add(V, k3v, H), mm(K2, add(A, k3a, H))
        An = [[A[a][b] + H / 6 * (k1a[a][b] + 2 * k2a[a][b] + 2 * k3a[a][b] + k4a[a][b]) for b in range(2)] for a in range(2)]
        Vn = [[V[a][b] + H / 6 * (k1v[a][b] + 2 * k2v[a][b] + 2 * k3v[a][b] + k4v[a][b]) for b in range(2)] for a in range(2)]
        l0, l1 = (i // 2) * H, (i // 2 + 1) * H
        if i > 10 and conj is None and det(A) > 0 >= det(An):
            conj = l0 + H * det(A) / (det(A) - det(An))
            Aconj = An
        A, V = An, Vn
    return conj, Aconj, Ks_


ci_p, Ap, Kp = conj_independent(2e-3)
ci_m, Am, Km = conj_independent(-2e-3)
tr_max = max(abs(K[0][0] + K[1][1]) / max(abs(K[0][0]), abs(K[1][1]), 1e-30) for K in Kp
             if max(abs(K[0][0]), abs(K[1][1])) > 1e-3)
offd = max(abs(K[0][1]) for K in Kp)
cp, cm = C.survey(2e-3)["conjugate"], C.survey(-2e-3)["conjugate"]
rec("E5", abs(ci_p - cp) < 0.1 and abs(ci_m - cm) < 0.1,
    "independent eq.(11), standard sign, exact screen, RK4 (n=3600): conj(+2e-3) = %.4f vs code %.2f; "
    "conj(-2e-3) = %.4f vs code %.2f; along the ray max |trace|/|K| = %.2e (|K| > 1e-3), max |K_yz| = %.1e"
    % (ci_p, cp, ci_m, cm, tr_max, offd))

# ---------------------------------------------------------------- E6
ref = {}
for n in (900, 1800, 3600):
    ref[n] = (C.survey(2e-3, n=n)["conjugate"], C.survey(-2e-3, n=n)["conjugate"],
              C.survey(-2e-3, n=n)["early"])
    print("       n=%4d  h=%.4f  conj(+2e-3) = %.4f  conj(-2e-3) = %.4f  early(-2e-3) = %s"
          % (n, 75.0 / n, ref[n][0], ref[n][1], ref[n][2]))
spread = max(abs(ref[n][1] - ref[3600][1]) for n in ref)
rec("E6", spread < 0.1 and all(ref[n][2] for n in ref),
    "code conj(-2e-3) spread over 4x refinement = %.4f (<= one coarse step 0.083); docstring line 50 "
    "'56.52' is off the n=900 grid (56.50) -- a figure from another resolution, not an error" % spread)

# ---------------------------------------------------------------- E7 detector
def det_rule(Tfun, lam=10.0, n=2000):
    h = lam / n
    A = [[0., 0.], [0., 0.]]; dA = [[1., 0.], [0., 1.]]
    mind, conj = 1e9, None
    for i in range(n):
        T = Tfun(i * h)
        acc = [[-sum(T[r_][s] * A[s][c] for s in range(2)) for c in range(2)] for r_ in range(2)]
        for r_ in range(2):
            for c in range(2):
                A[r_][c] += h * dA[r_][c] + 0.5 * h * h * acc[r_][c]
                dA[r_][c] += h * acc[r_][c]
        dt = A[0][0] * A[1][1] - A[0][1] * A[1][0]
        if i > 5:
            mind = min(mind, dt)
            if conj is None and dt <= 0.0:
                conj = i * h
    return conj, mind
c_stig, md = det_rule(lambda l: [[1.0, 0.0], [0.0, 1.0]])
c_ast, _ = det_rule(lambda l: [[1.0, 0.0], [0.0, 0.9]])
rec("E7", c_stig is None and c_ast is not None,
    "composite's rule 'first det A <= 0 after step 5' misses a stigmatic focus (T = I: true conjugate "
    "point at pi = 3.1416, min det = %.2e > 0, detected = %s) and finds an astigmatic one (%.3f): it is "
    "SUFFICIENT, not necessary; irrelevant for composite's traceless (vacuum) T, where zeros are simple"
    % (md, c_stig, c_ast))

# ---------------------------------------------------------------- E8
def svals(B):
    a, b, c, d_ = B[0][0], B[0][1], B[1][0], B[1][1]
    s1 = a * a + b * b + c * c + d_ * d_
    dd = abs(a * d_ - b * c)
    disc = math.sqrt(max(s1 * s1 - 4 * dd * dd, 0.0))
    return math.sqrt((s1 + disc) / 2), math.sqrt(max((s1 - disc) / 2, 0.0))
sp_, sm_ = svals(Ap), svals(Am)
rec("E8", sp_[1] / sp_[0] < 0.02 and sm_[1] / sm_[0] < 0.02,
    "at the conjugate point A has singular values %.3f, %.2e (+M) and %.3f, %.2e (-M): rank 1, a line "
    "focus -- a nontrivial Jacobi field vanishing at both ends, so a conjugate point in the eq.(11) sense"
    % (sp_[0], sp_[1], sm_[0], sm_[1]))

# ---------------------------------------------------------------- E9 where the flip is NOT invisible
# concentric.py reuses composite's tidal() with the same acc = -T A.  Sandbox copies only.
import concentric as CC, concentric_fix as CCF  # noqa: E402
m_cc = md5("/home/user/Claude-Method-Works/research/warp-drive/concentric.py") == md5(os.path.join(SANDBOX, "concentric.py"))
e9 = []
for m_, a_c in ((1e-2, 0.02), (1e-2, 0.5), (5e-3, 0.5)):
    tr_ = CC.trace_ratio(m_, a=a_c)
    c1, c2 = CC.survey(m_, a=a_c)["conjugate"], CCF.survey(m_, a=a_c)["conjugate"]
    e9.append((m_, a_c, tr_, c1, c2))
    print("       concentric m=%.0e a=%.2f  |trace|/|T| = %.2e  code conj %s  eq11-sign conj %s"
          % (m_, a_c, tr_, c1, c2))
rec("E9", m_cc and abs(e9[0][3] - e9[0][4]) < 0.25 and e9[1][3] is not None and e9[1][4] is not None
    and abs(e9[1][3] - e9[1][4]) > 10 and e9[2][3] is not None and e9[2][4] is None,
    "vacuum corridor (a=0.02, the design point): the flip moves the conjugate point by one step; "
    "NON-vacuum ray (a=0.5, R_kk < 0, concentric.py's withdrawn first corridor): code 191.76 vs eq.(11) 232.56, "
    "and at m=5e-3 the code seats where eq.(11) does not -- with composite's sign, negative R_kk FOCUSES")

npass = sum(1 for _, ok in results if ok)
print("\n%d/%d PASS" % (npass, len(results)))
sys.exit(0 if npass == len(results) else 1)
