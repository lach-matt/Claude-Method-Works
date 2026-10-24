#!/usr/bin/env python3
"""exterior5.py -- [Hin23a] section 3 at n = 4: every place the dimension enters, computed.

[Hin23a] (Hintz, "Exterior stability of Minkowski space in generalized harmonic gauge",
arXiv:2302.13804v1) proves its section 3 in 3 + 1 dimensions. The dimension n of space enters
that section through six quantities; each is computed here at n = 3, against his printed
values, and at n = 4.

X1  the radial wave operator conjugated by r^k, k = (n - 1)/2: r^k box r^-k = 4 d0 d1 +
    ((n - 1)(n - 3)/4) r^-2 on functions of (x0, x1), no first-order term ((3.34), p. 23);
    and Tangherlini's r* - r, a power series in 1/r with no logarithm (his r* = r + 2m log).
X2  the b-density: rho0^(n+1) rho_I^n |dg| is |d rho0/rho0 d rho_I/rho_I d g_S| exactly on
    Minkowski (his mu_b = rho0^4 rho_I^3 |dg_m|, p. 16).
X3  the energy form (3.25): the principal part of [L0, W] - (div W) L0 for the model
    L0 = -2 rho_I d_rho_I (rho0 d_rho0 - rho_I d_rho_I) + x_I^2 (Lap + q_n), q_n = (n-1)(n-3)/4,
    and W = w^2 V of (3.22); his coefficients, the angular operator Lap + q_n >= q_n >= 0.
X4  A_(E_C,E_Ups) of (2.10)-(2.11) at h = 0, built from Definition 2.2's operators on
    S^2 T* R^(1+n) (p. 7) and reduced to the splitting (2.9): his printed matrices at n = 3
    ((2.11), (3.36), (3.39), (3.40), (3.42), (3.43)), the duality G^-1 A* G = -A_swap of
    Remark 2.3 (G^-1 = G only at n = 3) at n = 3 and n = 4, the block-triangular structure and
    the diagonal.
X5  the order of the quadratic radiation term in R_11 for g = -dx0 dx1 + r^2 (g_S + r^-k chi T):
    r^-2k, against r^-(1+k) for the terms of L = 2 rho_I rho^-(2+k) P' rho^k; ratio r^(1-k),
    critical at n = 3 (his (3.47)) and down by r^-1/2 at n = 4.
X6  the Sobolev counts: the least integer above dim M / 2 = (n + 1)/2 (Notation 3.22's k >= 3)
    and Lemma 3.33's d_(n-1) with his n = dim M.
X7  the h-dependent entries of A_g and B_g (Proposition 3.29): the h u part of
    L_2 = 2 r^(k+1) P r^-k, P(g) = Ric(g) - delta*_(gb,E_C) Upsilon(g; gb), for g = gb + r^-k h,
    h a frame component of size 1, in the three cases A(7,1), A(4,7), B(4,1) (B(7,1) with A(7,1)).
    Each entry is linear in h (the product with u is bilinear). At n = 3 the frame coefficients are
    r-independent, 2 times his printed entries (A on d_1 u, B on u); at n = 4 they are the same
    numbers times r^(1-k) = r^-1/2, exactly.
X8  Lemma 3.6 at n = 4: with f = 1 - mu/r^2 and Tangherlini's r*, the identity (3.8)
    g^-1(r d rho_I, r d rho_I) = (2 x1/r)(1 + x1 f/(2r)) and d rho_0 null; xbar_I = min(sqrt3/2,
    1/(2 mu^(1/4))) keeps r > 2 sqrt(mu), twice the horizon radius (his 1/sqrt(8m): r > 4m), so r*
    is defined, f > 3/4, and (3.8) is negative.

Usage: exterior5.py [--selftest] [--mutants] [--only N]
"""
import sys
import sympy as sp

PRINTED_211 = [  # [Hin23a] (2.11), p. 8; rows/cols (00, 01, 0a, 11, 1a, tr, tf)
    ["2*C", 0, 0, 0, 0, 0, 0],
    ["-U", "-U", 0, 0, 0, 0, 0],
    [0, 0, "C", 0, 0, 0, 0],
    [0, "-2*U", 0, "-2*U", 0, "C", 0],
    [0, 0, "C-U", 0, "-U", 0, 0],
    ["2*C", 0, 0, 0, 0, "C", 0],
    [0, 0, 0, 0, 0, 0, 0]]
BLOCKS = ["00", "01", "0a", "11", "1a", "tr", "tf"]
gC, gU = sp.symbols("gamma_C gamma_Ups")


def _printed(tab):
    env = {"C": gC, "U": gU}
    return sp.Matrix([[sp.sympify(e, locals=env) if isinstance(e, str) else e for e in row]
                      for row in tab])


# ---------------------------------------------------------------- X1
def x1(n, mut=None):
    x0, xa, F = sp.symbols("x0 x1 F")
    f = sp.Function("f")(x0, xa)
    r = (x0 - xa) / 2
    k = sp.Rational(n - 1, 2) if mut != "x1" else sp.Rational(n - 2, 2)
    # box = -|g|^-1/2 d_i(|g|^1/2 g^ij d_j) for g = -dx0 dx1 + r^2 g_S, g^01 = -2
    def box(u):
        return 2 * r**(1 - n) * (sp.diff(r**(n - 1) * sp.diff(u, xa), x0)
                                 + sp.diff(r**(n - 1) * sp.diff(u, x0), xa))
    rest = sp.simplify(sp.expand(r**k * box(r**(-k) * f) - 4 * sp.diff(f, x0, xa)))
    q = sp.simplify(rest / f * r**2)
    ok_first = not rest.has(sp.Derivative)
    mu, rr = sp.symbols("mu r", positive=True)
    if n == 4:   # Tangherlini: dr*/dr = (1 - mu/r^2)^-1
        rstar = rr + sp.sqrt(mu) / 2 * sp.log((rr - sp.sqrt(mu)) / (rr + sp.sqrt(mu)))
        ser = sp.series(rstar - rr, rr, sp.oo, 7).removeO()
        no_log = not ser.has(sp.log) and sp.simplify(ser + mu / rr + mu**2 / (3 * rr**3)
                                                     + mu**3 / (5 * rr**5)) == 0
    else:        # Schwarzschild: r* = r + 2m log(r - 2m), his (1.1)
        ser = 2 * mu * sp.log(rr - 2 * mu)
        no_log = sp.simplify(sp.diff(rr + ser, rr) - 1 / (1 - 2 * mu / rr)) == 0 and ser.has(sp.log)
    return {"q": q, "first_order_free": ok_first, "rstar_series": ser, "no_log": no_log}


# ---------------------------------------------------------------- X2
def x2(n):
    p0, pI = sp.symbols("rho0 rhoI", positive=True)
    r = 1 / (p0 * pI)
    t = r - 1 / p0            # rho0 = 1/(r - t), rho_I = (r - t)/r on Minkowski
    J = sp.Matrix([[sp.diff(t, p0), sp.diff(t, pI)], [sp.diff(r, p0), sp.diff(r, pI)]]).det()
    # |dg| = r^(n-1) |dt dr| |dg_S| = r^(n-1) |J| rho0 rhoI x (b-density)
    ratio = sp.simplify(p0**(n + 1) * pI**n * r**(n - 1) * sp.Abs(J) * p0 * pI)
    return {"mu_b/b-density": ratio}


# ---------------------------------------------------------------- X3
def x3(n, mut=None):
    s0, sI, a0, aI, c, lam, xi0, xiI = sp.symbols("s0 sI alpha0 alphaI c lam xi0 xiI")
    q = sp.Rational((n - 1) * (n - 3), 4)
    F = sp.exp(sp.I * (xi0 * s0 + xiI * sI))
    w2 = sp.exp(-2 * a0 * s0 - 2 * aI * sI)

    def L0(u):  # s = log rho; x_I^2 = rho_I = e^sI; angular operator by its value lam + q
        return (-2 * sp.diff(sp.diff(u, s0) - sp.diff(u, sI), sI)
                + sp.exp(sI) * (lam + q) * u)

    def V(u):
        return sp.diff(u, s0) - (1 + c) * sp.diff(u, sI)

    def W(u):
        return w2 * V(u)
    divW = V(w2)              # the b-density d s0 d sI dg_S is V-invariant
    Q = L0(W(F)) - W(L0(F)) - (0 if mut == "x3" else divW * L0(F))
    sym = sp.expand(sp.simplify(Q / (w2 * F)))
    deg = sp.Poly(sym.subs(lam, lam), xi0, xiI)
    # principal part: degree 2 in (xi0, xiI), and the lam-terms (lam counts degree 2)
    prin = sum(cf * xi0**i * xiI**j for (i, j), cf in deg.terms() if i + j == 2)
    ang = sp.expand(sym).coeff(lam)
    printed = (-4 * aI * (xi0 - xiI)**2 + 4 * c * (a0 - aI) * xiI**2)
    coef_printed = 1 + 2 * (a0 - aI) + c * (1 - 2 * aI)
    ok_xi = sp.simplify(sp.expand(prin) - sp.expand(printed).subs(lam, 0)) == 0
    ok_ang = sp.simplify(ang - sp.exp(sI) * coef_printed) == 0
    # at xi = 0 the form is coef e^sI (lam + q) exactly: q enters only with the angular operator
    zero = sp.simplify(sym.subs({xi0: 0, xiI: 0}) - sp.exp(sI) * coef_printed * (lam + q))
    return {"xi_part_matches_3.25": ok_xi, "angular_coef_matches_3.25": ok_ang,
            "angular_operator_lam_plus_q": zero == 0, "q_n": q}


# ---------------------------------------------------------------- X4
def _frame(n):
    N = n + 1                           # frame (dx0, dx1, r e^2, ..., r e^n)
    g = sp.zeros(N, N)
    g[0, 1] = g[1, 0] = sp.Rational(-1, 2)
    for a in range(2, N):
        g[a, a] = 1
    gi = g.inv()
    c = sp.Matrix([sp.Rational(1, 2), sp.Rational(1, 2)] + [0] * (n - 1))  # r c, c = r^-1 dt
    return N, g, gi, c


def _ops(n, mut=None):
    N, g, gi, c = _frame(n)
    half = sp.Rational(1, 4) if mut == "x4G" else sp.Rational(1, 2)

    def tr(U):
        return sum(gi[i, j] * U[i, j] for i in range(N) for j in range(N))

    def G(U):
        return U - half * tr(U) * g

    def delta_lead(U):                  # (delta u)_nu = -g^(kl) d_k u_(l nu), d_1 part
        return sp.Matrix([-sum(gi[1, l] * U[l, nu] for l in range(N)) for nu in range(N)])

    def dstar_lead(w):                  # (delta* w)_(mu nu) = (d_mu w_nu + d_nu w_mu)/2, d_1 part
        return sp.Matrix(N, N, lambda m, v: sp.Rational(1, 2) * (int(m == 1) * w[int(v)]
                                                                  + int(v == 1) * w[int(m)]))

    def iota(w):                        # iota_(g^-1 c) w
        return sum(gi[i, j] * c[i] * w[j] for i in range(N) for j in range(N))

    def dC(w, gam):                     # (2.4) minus delta*: gam (2 c (x)_s w - g iota_(g^-1 c) w)
        sgn = -1 if mut == "x4s" else 1
        return gam * (c * w.T + w * c.T - sgn * g * iota(w))

    def dU(U, gam):                     # (2.5) minus delta: gam (2 iota_(g^-1 c) U - c tr U)
        iu = sp.Matrix([sum(gi[i, j] * c[i] * U[j, v] for i in range(N) for j in range(N))
                        for v in range(N)])
        return gam * (2 * iu - c * tr(U))

    def A(U, gc=gC, gu=gU):             # L = 2 r^(k+1) P' r^-k == 2 d_1 (2 r d_0 + A)
        return dC(delta_lead(G(U)), gc) + dstar_lead(dU(G(U), gu))
    return N, g, gi, G, delta_lead, dstar_lead, dC, dU, A


def _reps(n):
    N = n + 1

    def E(i, j):
        M = sp.zeros(N, N)
        M[i, j] += 1
        if i != j:
            M[j, i] += 1
        return M
    tr = sp.zeros(N, N)
    for a in range(2, N):
        tr[a, a] = 1
    tf = E(2, 2) - E(3, 3)
    return [E(0, 0), E(0, 1) / 1, E(0, 2), E(1, 1), E(1, 2), tr, tf]


def _coords(n, R):                      # the splitting (2.9)'s coordinates of a tensor R
    N = n + 1
    trc = sum(R[a, a] for a in range(2, N)) / (n - 1)
    return sp.Matrix([R[0, 0], R[0, 1], R[0, 2], R[1, 1], R[1, 2], trc, R[2, 2] - trc])


def _sym_basis(N):
    out = []
    for i in range(N):
        for j in range(i, N):
            M = sp.zeros(N, N)
            M[i, j] = M[j, i] = 1
            out.append(M)
    return out


def _vec(M, N):
    return sp.Matrix([M[i, j] for i in range(N) for j in range(i, N)])


def x4(n, mut=None):
    N, g, gi, G, dl, dsl, dC, dU, A = _ops(n, mut)
    reps = _reps(n)
    A7 = sp.zeros(7, 7)
    for j, e in enumerate(reps):
        A7[:, j] = _coords(n, sp.expand(A(e)))
    # tensoriality check: the image of each representative lies in the representatives' span
    span_ok = all(sp.expand(A(e) - sum((A7[i, j] * reps[i] for i in range(7)), sp.zeros(N, N)))
                  == sp.zeros(N, N) for j, e in enumerate(reps))
    # duality (Remark 2.3, generalized): G^-1 A_(C,U)^* G = -A_(U,C) on all of S^2 T*
    basis = _sym_basis(N)
    gram = sp.Matrix(len(basis), len(basis), lambda i, j: sum(
        gi[a, b] * gi[c_, d] * basis[i][a, c_] * basis[j][b, d]
        for a in range(N) for b in range(N) for c_ in range(N) for d in range(N)))

    def mat(op):
        cols = [_vec(op(e), N) for e in basis]
        # coordinates in the basis: off-diagonal basis elements have entry 1 at (i, j), (j, i)
        return sp.Matrix.hstack(*cols)
    Am = mat(lambda U: A(U))
    Asw = mat(lambda U: A(U, gU, gC))
    Gm = mat(G)
    Astar = gram.inv() * Am.T * gram
    try:
        dual = sp.simplify(Gm.inv() * Astar * Gm + Asw) == sp.zeros(len(basis), len(basis))
    except sp.matrices.exceptions.NonInvertibleMatrixError:
        dual = False                    # G not invertible: no duality to hold
    # structure: ran pi_C = (00, 0a, tr), pi_Ups = (01, 1a), then tf, then 11
    iC, iU, iT, i11 = [0, 2, 5], [1, 4], [6], [3]
    closedC = all(A7[i, j] == 0 for i in iC for j in iU + iT + i11)
    lowtri = all(A7[i, j] == 0 for i in iC + iU for j in iT + i11) and A7[6, 3] == 0
    CU = A7.extract(iC + iU, iC + iU)
    ev = CU.eigenvals()
    out = {"A7": A7, "span_ok": span_ok, "duality": dual, "pi_C_closed": closedC,
           "lower_triangular": lowtri, "eig_CUps": ev, "tf_diag": A7[6, 6], "11_diag": A7[3, 3]}
    if n == 3:
        out["matches_2.11"] = sp.simplify(A7 - _printed(PRINTED_211)) == sp.zeros(7, 7)
        out["intermediates"] = _intermediates3(n, mut)
    return out


def _intermediates3(n, mut):
    """His (3.36), (3.39), (3.40), (3.42), (3.43) at n = 3, from the same operators."""
    N, g, gi, G, dl, dsl, dC, dU, A = _ops(n, mut)
    reps = _reps(n)
    onef = [sp.Matrix([1 if i == j else 0 for i in range(N)]) for j in range(N)]
    w_reps = [onef[0], onef[1], onef[2]]          # (w0, w1, w_a)

    def cols(op, ins):
        return sp.Matrix.hstack(*[_coords(n, sp.expand(op(e))) for e in ins])

    def cols1(op, ins):
        return sp.Matrix.hstack(*[sp.Matrix(list(sp.expand(op(e)))[:3]) for e in ins])
    m336 = cols(lambda w: dC(w, 1), w_reps)
    m340 = cols(G, reps)
    m339 = cols1(dl, reps)
    m342 = cols(dsl, w_reps)
    m343 = cols1(lambda U: dU(U, 1), reps)
    h = sp.Rational(1, 2)
    p336 = sp.Matrix([[1, 0, 0], [0, 0, 0], [0, 0, h], [0, 1, 0], [0, 0, h], [1, 1, 0], [0, 0, 0]])
    p340 = sp.Matrix([[1, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, h, 0], [0, 0, 1, 0, 0, 0, 0],
                      [0, 0, 0, 1, 0, 0, 0], [0, 0, 0, 0, 1, 0, 0], [0, 2, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 1]])
    p339 = sp.Matrix([[2, 0, 0, 0, 0, 0, 0], [0, 2, 0, 0, 0, 0, 0], [0, 0, 2, 0, 0, 0, 0]])
    p342 = sp.Matrix([[0, 0, 0], [h, 0, 0], [0, 0, 0], [0, 1, 0], [0, 0, h], [0, 0, 0], [0, 0, 0]])
    p343 = sp.Matrix([[-2, 0, 0, 0, 0, -1, 0], [0, 0, 0, -2, 0, -1, 0], [0, 0, -2, 0, -2, 0, 0]])
    return {"3.36": m336 == p336, "3.39": m339 == p339, "3.40": m340 == p340,
            "3.42": m342 == p342, "3.43": m343 == p343}


# ---------------------------------------------------------------- X5
def x5(n):
    x0, xa = sp.symbols("x0 x1")
    s = sp.Symbol("s")
    chi = sp.Function("chi")(xa)
    r = (x0 - xa) / 2
    k = sp.Rational(n - 1, 2)
    eps = s * r**(-k) * chi
    th = sp.symbols("th1:%d" % n)
    # round metric on S^(n-1): dth1^2 + sin^2 th1 (dth2^2 + sin^2 th2 (...))
    sph = []
    f = 1
    for i in range(n - 1):
        sph.append(f)
        f = f * sp.sin(th[i])**2
    T = [0] * (n - 1)
    T[0], T[1] = 1, -1                  # T = dth1^2 - sin^2 th1 dth2^2: trace-free, |T|^2 = 2
    X = [x0, xa] + list(th)
    N = n + 1
    gm = sp.zeros(N, N)
    gm[0, 1] = gm[1, 0] = sp.Rational(-1, 2)
    for a in range(n - 1):
        gm[2 + a, 2 + a] = r**2 * sph[a] * (1 + eps * T[a])
    gi = gm.inv()
    Gam = [[[sp.simplify(sum(gi[a, d] * (sp.diff(gm[d, b], X[c]) + sp.diff(gm[d, c], X[b])
                                         - sp.diff(gm[b, c], X[d])) for d in range(N)) / 2)
             for c in range(N)] for b in range(N)] for a in range(N)]
    b = d = 1
    R11 = sum(sp.diff(Gam[a][b][d], X[a]) - sp.diff(Gam[a][b][a], X[d]) for a in range(N))
    R11 += sum(Gam[a][a][e] * Gam[e][b][d] - Gam[a][d][e] * Gam[e][b][a]
               for a in range(N) for e in range(N))
    quad = sp.series(R11, s, 0, 3).removeO().coeff(s, 2)
    c1 = sp.Symbol("c1")
    quad = quad.subs(sp.Derivative(chi, xa), c1)
    cf = sp.simplify(sp.expand(quad).coeff(c1, 2))
    rr = sp.Symbol("rr", positive=True)
    cf_r = sp.simplify(cf.subs(x0, xa + 2 * rr))
    expo = sp.simplify(sp.log(cf_r / cf_r.subs(rr, 1)) / sp.log(rr)) if cf_r != 0 else None
    return {"chi'^2 coefficient": cf_r, "r_exponent": expo, "expected": -2 * k,
            "ratio_exponent": 1 - k}


# ---------------------------------------------------------------- X6
def x6(n):
    dimM = n + 1
    k_inf = dimM // 2 + 1                # least integer > dim M / 2
    d = lambda p: -(-(p + 1) // 2)       # d_p = ceil((p + 1)/2), least integer > p/2
    return {"dim M": dimM, "H^k_b in L^oo for k >=": k_inf, "d_(dimM-1)": d(dimM - 1)}


# ---------------------------------------------------------------- X7
HIN329 = {"A71": {(2, 2): {"C1F1": 4, "C2F0": 4}, (3, 3): {"C1F1": -4, "C2F0": -4}},
          "A47": {(1, 1): {"C1F1": -2}},
          "B41": {(1, 1): {"E2F0": 4}}}   # 2 x his A(7,1) = 2 d_1 h, B(7,1), A(4,7) = -(1/2) d_1 h, B(4,1)


def x7(n, case, mut=None):
    x0, xa = sp.symbols("x0 x1")
    eps, s, R = sp.symbols("eps s R", positive=True)
    th = sp.symbols("th1:%d" % n)
    X = [x0, xa] + list(th)
    N = n + 1
    r = (x0 - xa) / 2
    k = sp.Rational(n - 1, 2)
    kh = k if mut != "x7" else sp.Rational(n - 2, 2)
    chi, eta, f = sp.Function("chi")(xa), sp.Function("eta")(xa), sp.Function("f")(xa)
    sph, w = [], sp.Integer(1)
    for i in range(n - 1):
        sph.append(w)
        w = w * sp.sin(th[i])**2
    T = [0] * (n - 1)
    T[0], T[1] = 1, -1
    gb = sp.zeros(N, N)
    gb[0, 1] = gb[1, 0] = sp.Rational(-1, 2)
    for a in range(n - 1):
        gb[2 + a, 2 + a] = r**2 * sph[a]
    H, U = sp.zeros(N, N), sp.zeros(N, N)
    for a in range(n - 1):              # frame components: r^2 g-slash-weighted angular entries
        H[2 + a, 2 + a] = r**2 * sph[a] * T[a] * chi * int(case != "B41")
        U[2 + a, 2 + a] = r**2 * sph[a] * T[a] * int(case == "A47")
    H[1, 1] = eta * int(case == "B41")
    U[0, 0] = int(case != "A47")
    g = gb + eps * r**(-kh) * H + s * r**(-k) * f * U
    gi = sp.zeros(N, N)
    Bi = g[:2, :2].inv()
    for i in range(2):
        for j in range(2):
            gi[i, j] = Bi[i, j]
    for a in range(2, N):
        gi[a, a] = 1 / g[a, a]
    gbi = gb.inv()

    def chris(G, Gi):
        return [[[sum(Gi[a, d] * (sp.diff(G[d, b], X[c]) + sp.diff(G[d, c], X[b]) - sp.diff(G[b, c], X[d]))
                      for d in range(N)) / 2 for c in range(N)] for b in range(N)] for a in range(N)]
    Gam, Gb = chris(g, gi), chris(gb, gbi)

    def es(e):
        return sp.diff(e, eps, s).subs({eps: 0, s: 0})
    ups = [sum(gi[a, b] * (Gam[q][a][b] - Gb[q][a][b]) for a in range(N) for b in range(N)) for q in range(N)]
    ups = [es(sum(g[m, q] * ups[q] for q in range(N))) for m in range(N)]
    c = [1 / (2 * r), 1 / (2 * r)] + [0] * (n - 1)
    d = sp.symbols("C0 C1 C2 E0 E1 E2 F0 F1 F2")
    sub = {sp.Derivative(chi, (xa, 2)): d[2], sp.Derivative(chi, xa): d[1], sp.Derivative(eta, (xa, 2)): d[5],
           sp.Derivative(eta, xa): d[4], sp.Derivative(f, (xa, 2)): d[8], sp.Derivative(f, xa): d[7]}
    mons = {"C1F1": d[1] * d[7], "C2F0": d[2] * d[6], "E2F0": d[5] * d[6], "E1F1": d[4] * d[7]}
    out = {}
    for (i, j) in ([(1, 1)] if case != "A71" else [(2, 2), (3, 3)]):
        ric = sum(sp.diff(Gam[a][i][j], X[a]) - sp.diff(Gam[a][i][a], X[j]) for a in range(N))
        ric += sum(Gam[a][a][q] * Gam[q][i][j] - Gam[a][j][q] * Gam[q][i][a] for a in range(N) for q in range(N))
        dst = (sp.diff(ups[j], X[i]) + sp.diff(ups[i], X[j])) / 2 - sum(Gb[l][i][j] * ups[l] for l in range(N))
        dst += gC * (c[i] * ups[j] + c[j] * ups[i]
                     - gb[i, j] * sum(gbi[a, b] * c[a] * ups[b] for a in range(N) for b in range(N)))
        scale = 1 if i < 2 else r**2 * sph[i - 2]
        L2 = sp.expand(2 * r**(k + 1) * (es(ric) - dst) / scale)
        L2 = sp.expand(L2.subs(sub).subs({chi: d[0], eta: d[3], f: d[6]}).subs(x0, xa + 2 * R))
        poly = sp.Poly(L2, *d)
        out[(i, j)] = {nm: sp.simplify(poly.coeff_monomial(mo)) for nm, mo in mons.items()
                       if poly.coeff_monomial(mo) != 0}
    return out, R, k


def x7all(n, mut=None):
    res = {"matches": True}
    for case, want in HIN329.items():
        out, R, k = x7(n, case, mut)
        res[case] = out
        res["matches"] = res["matches"] and out == {ij: {nm: sp.simplify(v * R**(1 - k)) for nm, v in cf.items()}
                                                     for ij, cf in want.items()}
    return res


# ---------------------------------------------------------------- X8
def x8(n, mut=None):
    r, mu, x1s, rs = sp.symbols("r mu x1 rs", positive=True)
    mu_ = 2 * mu if n == 3 else mu                 # mu = m at n = 3: f = 1 - 2m/r
    f = 1 - mu_ / r**(n - 2)
    rh = mu_**sp.Rational(1, n - 2)                 # horizon radius: 2m, sqrt(mu)
    # r d rho_I with rho_I = -x1/r and dr = f dr* = f (dx0 - dx1)/2:  a dx0 + b dx1
    a = x1s * f / (2 * r)
    b = -1 - x1s * f / (2 * r)
    ginv01 = -2 / f                                # g = -f dx0 dx1 + r^2 g-slash
    q = sp.simplify(2 * ginv01 * a * b)
    ident = sp.simplify(q - (2 * x1s / r) * (1 + x1s * f / (2 * r))) == 0
    rstar = (r + 2 * mu * sp.log(r - 2 * mu) if n == 3 else
             r + sp.sqrt(mu) / 2 * sp.log((r - sp.sqrt(mu)) / (r + sp.sqrt(mu))))
    tort = sp.simplify(sp.diff(rstar, r) - 1 / f) == 0
    xbar_m = 1 / sp.sqrt(8 * mu) if n == 3 else 1 / (2 * mu**sp.Rational(1, 4))
    if mut == "x8":
        xbar_m = 1 / sp.sqrt(8 * mu)
    rmin = sp.Rational(1, 2) * xbar_m**-2               # r > rmin on x_I < xbar_I, rho_0 < 2
    samples = [sp.Rational(1, 100), 1, 100]
    good = all(sp.simplify(rmin - 2 * rh).subs(mu, m0) >= 0 for m0 in samples)
    fmin = sp.simplify(f.subs(r, 2 * rh))
    # |x1 f/(2r)| = x_I^2 f/2 < (3/4)(1/2) < 1 since 0 < f < 1 for mu > 0
    return {"identity_3.8": ident, "tortoise": tort, "r_min": sp.simplify(rmin), "r > 2 r_h": good,
            "f(2 r_h)": fmin, "second_factor_bound": (sp.sqrt(3) / 2)**2 / 2}


# ---------------------------------------------------------------- driver
def run(only=None, mut=None, quiet=False):
    res = {}
    for n in (3, 4):
        if only in (None, 1):
            res[("X1", n)] = x1(n, mut)
        if only in (None, 2):
            res[("X2", n)] = x2(n)
        if only in (None, 3):
            res[("X3", n)] = x3(n, mut)
        if only in (None, 4):
            res[("X4", n)] = x4(n, mut)
        if only in (None, 5) and mut is None:
            res[("X5", n)] = x5(n)
        if only in (None, 6):
            res[("X6", n)] = x6(n)
        if only in (None, 7):
            res[("X7", n)] = x7all(n, mut)
        if only in (None, 8):
            res[("X8", n)] = x8(n, mut)
    if not quiet:
        for key, v in res.items():
            print(key)
            for kk, vv in v.items():
                print("   ", kk, ":", vv)
    return res


def checks(res):
    ok = []
    for n in (3, 4):
        if ("X1", n) in res:
            v = res[("X1", n)]
            ok.append(("X1 n=%d" % n, v["first_order_free"] and v["no_log"]
                       and v["q"] == sp.Rational((n - 1) * (n - 3), 4)))
        if ("X2", n) in res:
            ok.append(("X2 n=%d" % n, res[("X2", n)]["mu_b/b-density"] == 1))
        if ("X3", n) in res:
            v = res[("X3", n)]
            ok.append(("X3 n=%d" % n, v["xi_part_matches_3.25"] and v["angular_coef_matches_3.25"]
                       and v["angular_operator_lam_plus_q"]))
        if ("X4", n) in res:
            v = res[("X4", n)]
            good = v["span_ok"] and v["duality"] and v["pi_C_closed"] and v["lower_triangular"]
            good = good and v["tf_diag"] == 0 and sp.simplify(v["11_diag"] + 2 * gU) == 0
            want = ({2 * gC: 1, gC: 2, -gU: 2} if n == 3 else
                    {2 * gC: 1, gC: 1, sp.Rational(3, 2) * gC: 1, -sp.Rational(3, 2) * gU: 1, -gU: 1})
            good = good and {sp.simplify(e): m for e, m in v["eig_CUps"].items()} == want
            if n == 3:
                good = good and v["matches_2.11"] and all(v["intermediates"].values())
            ok.append(("X4 n=%d" % n, good))
        if ("X5", n) in res:
            v = res[("X5", n)]
            ok.append(("X5 n=%d" % n, v["r_exponent"] == v["expected"]))
        if ("X6", n) in res:
            v = res[("X6", n)]
            ok.append(("X6 n=%d" % n, v["H^k_b in L^oo for k >="] == 3
                       and v["d_(dimM-1)"] == (2 if n == 3 else 3)))
        if ("X7", n) in res:
            ok.append(("X7 n=%d" % n, res[("X7", n)]["matches"]))
        if ("X8", n) in res:
            v = res[("X8", n)]
            ok.append(("X8 n=%d" % n, v["identity_3.8"] and v["tortoise"] and v["r > 2 r_h"]
                       and v["f(2 r_h)"] == (sp.Rational(1, 2) if n == 3 else sp.Rational(3, 4))))
    return ok


def main():
    args = sys.argv[1:]
    only = int(args[args.index("--only") + 1]) if "--only" in args else None
    if "--mutants" in args:
        caught = 0
        muts = [("x1", 1), ("x3", 3), ("x4G", 4), ("x4s", 4), ("x7", 7), ("x8", 8)]
        for m, o in muts:
            res = run(o, m, quiet=True)
            bad = [name for name, good in checks(res) if not good]
            print("mutant", m, "caught" if bad else "MISSED", bad)
            caught += bool(bad)
        print("mutants caught %d/%d" % (caught, len(muts)))
        sys.exit(0 if caught == len(muts) else 1)
    res = run(only, quiet="--selftest" in args)
    ok = checks(res)
    for name, good in ok:
        print(name, "PASS" if good else "FAIL")
    if "--selftest" in args:
        print("selftest %d/%d" % (sum(g for _, g in ok), len(ok)))
        sys.exit(0 if all(g for _, g in ok) else 1)


if __name__ == "__main__":
    main()
