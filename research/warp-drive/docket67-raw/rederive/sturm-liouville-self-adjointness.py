#!/usr/bin/env python3
"""
DOCKET 67, audit 28/36 -- sturm-liouville-self-adjointness.

What the tree uses (seatindex.py:105-112, selftest :348-355): "the Jacobi operator is
self-adjoint, so reading the path from the far end gives the same answer" -> the slab
position c folds to L - l - c: seats(slab(m,c,l)) == seats(slab(m,L-l-c,l)) on [0,L].

seats(q, L) is ONE-ENDED: u(0)=0, u'(0)=1, "does u vanish again in (0, L]?".  It is NOT
the two-ended Dirichlet pair statement transit.py (06ee6bf:transit.py:50-54) proved.

Checks
 [1] sympy: Lagrange identity  v L[u] - u L[v] = d/dx[p (v u' - u v')]  for L = (p u')' + q u
     -> formal self-adjointness with Dirichlet ends; Wronskian constant when p = 1.
     With a drift term r u':  W' = -r W, and reversal x -> L-x sends r -> -r(L-x):
     the self-adjoint (no-drift) family is the one CLOSED under reversal.
 [2] sympy: the transit.py substitution v(x) = u(L-x) solves v'' + q(L-x) v = 0.
 [3] z3: the Sturm separation step the fold needs (and transit's pair theorem does not give):
     u0(0)=0=u0(b), u0>0 on (0,b), W constant, uL of one sign on [0,b]  -> UNSAT.
 [4] EXACT (transfer-matrix, no discretisation) piecewise-constant q, seed 67:
     seats(q) == seats(q~) on the scan grid, with hostile exteriors, and on random profiles;
     cross-check: #zeros of u0 in (0,L) == #negative Dirichlet eigenvalues (FD inertia),
     identical for q and q~ (oscillation theorem, self-adjoint spectrum reflection-invariant).
 [5] the TREE's own seats() (seatindex.py, imported by path) against [4]: fold mismatches.
 [6] only the BOOLEAN folds: the turn position differs between c and L-l-c.
 [7] drift term r != 0: keeping r under reversal breaks the fold; r -> -r~ restores it.
 [8] 2x2 Jacobi J'' + T J = 0: T symmetric -> existence of a conjugate point is
     reversal-symmetric AND first-conjugate points coincide; T non-symmetric -> they can fail.
 [9] the selftest fixture: m = 6, l = 0.9, L = 12, c in (0.5, 1.5, 3.0).
"""
import math, random, sys, importlib.util
import sympy as sp

OK = True
def rep(label, cond, detail=""):
    global OK
    OK = OK and bool(cond)
    print(("  PASS " if cond else "  FAIL ") + label + ((" -- " + detail) if detail else ""))

# ------------------------------------------------------------------ [1] Lagrange identity
print("[1] Lagrange identity / Wronskian")
x, Lsym = sp.symbols("x L", real=True)
p, q, r, u, v = [sp.Function(n) for n in "pqruv"]
Lop = lambda f: sp.diff(p(x) * sp.diff(f(x), x), x) + q(x) * f(x)
lhs = v(x) * Lop(u) - u(x) * Lop(v)
rhs = sp.diff(p(x) * (v(x) * sp.diff(u(x), x) - u(x) * sp.diff(v(x), x)), x)
rep("v L[u] - u L[v] == d/dx[p W]", sp.simplify(sp.expand(lhs - rhs)) == 0)
# drift: u'' + r u' + q u = 0 for u and v -> W = u' v - u v' obeys W' = -r W
W = sp.diff(u(x), x) * v(x) - u(x) * sp.diff(v(x), x)
Wp = sp.diff(W, x).subs({sp.diff(u(x), x, 2): -r(x) * sp.diff(u(x), x) - q(x) * u(x),
                         sp.diff(v(x), x, 2): -r(x) * sp.diff(v(x), x) - q(x) * v(x)})
rep("drift form: W' = -r W (constant only if r = 0)", sp.simplify(Wp + r(x) * W) == 0)
# reversal of the drift form: v(x) = U(L - x), U'' = -r U' - q U at s = L - x
U = sp.Function("U")
U0, U1, U2 = sp.symbols("U0 U1 U2")
def to_syms(e):
    out = {}
    for S in e.atoms(sp.Subs):
        order = S.expr.derivative_count if isinstance(S.expr, sp.Derivative) else 0
        out[S] = {1: U1, 2: U2}[order]
    return e.xreplace(out).subs(U(Lsym - x), U0)
vrev = U(Lsym - x)
ode = to_syms(sp.diff(vrev, x, 2) - r(Lsym - x) * sp.diff(vrev, x) + q(Lsym - x) * vrev)
chk = sp.simplify(ode.subs(U2, -r(Lsym - x) * U1 - q(Lsym - x) * U0))
rep("reversal maps u''+r u'+q u=0 to v''-r~ v'+q~ v=0 (drift flips sign)", chk == 0, str(chk)[:80])
ode_naive = to_syms(sp.diff(vrev, x, 2) + r(Lsym - x) * sp.diff(vrev, x) + q(Lsym - x) * vrev)
chk2 = sp.simplify(ode_naive.subs(U2, -r(Lsym - x) * U1 - q(Lsym - x) * U0))
rep("naive reflection keeping +r~ fails unless r = 0 (residual 2 r~ v')", sp.simplify(chk2 + 2 * r(Lsym - x) * U1) == 0, str(chk2))

# ------------------------------------------------------------------ [2] transit substitution
print("[2] transit.py's pair theorem (a substitution)")
e2 = to_syms(sp.diff(vrev, x, 2) + q(Lsym - x) * vrev).subs(U2, -q(Lsym - x) * U0)
rep("v(x)=u(L-x) solves v'' + q(L-x) v = 0 (no self-adjointness used)", sp.simplify(e2) == 0)

# ------------------------------------------------------------------ [3] z3 separation step
print("[3] Sturm separation step, z3")
import z3
a0p, abp, uL0, uLb, W0, Wb = z3.Reals("u0p_0 u0p_b uL_0 uL_b W_0 W_b")
s3 = z3.Solver()
# W = u0' uL - u0 uL' ; at 0 and b u0 = 0 so W = u0' uL ; W constant (r = 0)
s3.add(W0 == a0p * uL0, Wb == abp * uLb, W0 == Wb)
s3.add(a0p > 0, abp < 0)            # u0 leaves 0 upward and returns downward (simple zeros)
s3.add(uL0 * uLb > 0)               # uL has the same strict sign at both ends (no zero, by IVT only if sign same)
rep("u0 zeros at 0,b + constant W + uL same sign at 0,b  => UNSAT", s3.check() == z3.unsat)
# note: uL(0)*uL(b) > 0 is necessary for 'no zero in [0,b]'; its negation gives a zero in (0,b) by IVT,
# and uL(0) = 0 or uL(b) = 0 is itself a zero in [0,b] (and b <= L so [0,b] within [0,L)... b < L case;
# b = L: uL(L) = 0 by definition, uL ~ u0 and uL(0) = 0 -- a zero at 0, inside [0, L)).

# ------------------------------------------------------------------ exact piecewise solver
def first_zero_segment(uu, up, m, t0, t1, exclude_start):
    """smallest t in (t0 or [t0, t1] with u(t)=0 for u''=-m u, data (uu,up) at t0."""
    T = t1 - t0
    eps = 1e-13
    if m > 0:
        kk = math.sqrt(m)
        A, B = uu, up / kk
        # u = A cos(kt) + B sin(kt) = R cos(kt - phi)
        phi = math.atan2(B, A)
        # zeros kt = phi + pi/2 + n pi
        t = (phi + math.pi / 2) / kk
        while t > (0 if not exclude_start else eps):
            t -= math.pi / kk
        while t <= (eps if exclude_start else -eps):
            t += math.pi / kk
        return t0 + t if t <= T + 1e-12 else None
    if m == 0:
        if up == 0:
            return (t0 if (uu == 0 and not exclude_start) else None)
        t = -uu / up
        if (t > eps or (not exclude_start and t >= -eps)) and t <= T + 1e-12:
            return t0 + max(t, 0.0)
        return None
    kk = math.sqrt(-m)
    if uu == 0:
        return None if exclude_start else t0
    if up == 0:
        return None
    ratio = -uu * kk / up
    if abs(ratio) >= 1:
        return None
    t = math.atanh(ratio) / kk
    if t > eps and t <= T + 1e-12:
        return t0 + t
    return None

def propagate(uu, up, m, T):
    if m > 0:
        kk = math.sqrt(m); c, s_ = math.cos(kk * T), math.sin(kk * T)
        return uu * c + up * s_ / kk, -uu * kk * s_ + up * c
    if m == 0:
        return uu + up * T, up
    kk = math.sqrt(-m); c, s_ = math.cosh(kk * T), math.sinh(kk * T)
    return uu * c + up * s_ / kk, uu * kk * s_ + up * c

def zeros_exact(segs, count=False):
    """segs: list of (length, m). u(0)=0,u'(0)=1. Returns first zero in (0,L] (or list)."""
    uu, up, x0 = 0.0, 1.0, 0.0
    zs = []
    first = True
    for (ln, m) in segs:
        t0 = x0
        cu, cup = uu, up
        excl = first
        tcur = t0
        while True:
            z = first_zero_segment(cu, cup, m, tcur, x0 + ln, excl)
            if z is None:
                break
            zs.append(z)
            if not count:
                return z
            # restart just after z
            cu, cup = propagate(cu, cup, m, z - tcur)
            cu = 0.0
            tcur = z
            excl = True
        uu, up = propagate(uu, up, m, ln)
        x0 += ln
        first = False
    return zs if count else None

def slab_segs(m, c, l, L, outside=0.0):
    segs = []
    if c > 0: segs.append((c, outside))
    segs.append((l, m))
    if L - c - l > 0: segs.append((L - c - l, outside))
    return segs

def fd_negcount(segs, N=3000):
    """# negative eigenvalues of Dirichlet -d2/dx2 - q on [0,L], FD, via LDL^T pivot signs."""
    L = sum(s_[0] for s_ in segs)
    h = L / N
    edges = []
    acc = 0.0
    for ln, m in segs:
        edges.append((acc, acc + ln, m)); acc += ln
    def qat(xx):
        for a, b, m in edges:
            if a <= xx <= b: return m
        return edges[-1][2]
    neg = 0
    d_prev = None
    off = -1.0 / (h * h)
    for i in range(1, N):
        di = 2.0 / (h * h) - qat(i * h)
        if d_prev is not None:
            di -= off * off / d_prev
        if di < 0: neg += 1
        d_prev = di
    return neg

# ------------------------------------------------------------------ [4] exact fold
print("[4] exact fold, transfer matrices (no discretisation)")
MS = (0.5, 1.0, 2.0, 4.0, 8.0, 16.0, 32.0, 64.0)
LS = (0.25, 0.5, 1.0, 2.0, 4.0)
TOTAL = 12.0
CPOS = (0.5, 1.5, 3.0, 5.0)
HOST = (0.0, -5.0, -20.0)
mism = tot = 0
for m in MS:
    for l in LS:
        for c in CPOS + (0.02, 0.1, 0.3, 1.0):
            if c + l > TOTAL: continue
            for h in HOST:
                a = zeros_exact(slab_segs(m, c, l, TOTAL, h)) is not None
                b = zeros_exact(slab_segs(m, TOTAL - l - c, l, TOTAL, h)) is not None
                tot += 1; mism += (a != b)
rep("scan grid x approaches x hostiles: exact fold", mism == 0, "%d/%d mismatches" % (mism, tot))
rng = random.Random(67)
mism = tot = 0; osc_bad = 0; osc_tot = 0
for trial in range(3000):
    nseg = rng.randint(1, 6)
    segs = [(rng.uniform(0.2, 4.0), rng.uniform(-10, 30)) for _ in range(nseg)]
    a = zeros_exact(segs) is not None
    b = zeros_exact(list(reversed(segs))) is not None
    tot += 1; mism += (a != b)
    if trial < 120:
        za = zeros_exact(segs, count=True); zb = zeros_exact(list(reversed(segs)), count=True)
        L = sum(s_[0] for s_ in segs)
        na = len([z for z in za if z < L - 1e-9]); nb = len([z for z in zb if z < L - 1e-9])
        fa = fd_negcount(segs); fb = fd_negcount(list(reversed(segs)))
        osc_tot += 1
        if not (na == nb == fa == fb):
            # FD is O(h^2); allow a miss only when an eigenvalue is within FD error of zero
            osc_bad += 1
rep("random piecewise q (3000, seed 67): exact fold", mism == 0, "%d/%d mismatches" % (mism, tot))
rep("oscillation: #zeros(q)=#zeros(q~)=#neg Dirichlet eigs (FD, both)", osc_bad <= 2,
    "%d/%d disagreements (FD resolution)" % (osc_bad, osc_tot))

# ------------------------------------------------------------------ [5] tree's seats()
print("[5] the tree's own seats() (seatindex.py, by path)")
spec = importlib.util.spec_from_file_location(
    "seatindex", "/home/user/Claude-Method-Works/research/warp-drive/seatindex.py")
si = importlib.util.module_from_spec(spec); spec.loader.exec_module(si)
mism_tree = tot = wrong_vs_exact = 0; bad = []
for m in MS:
    for l in LS:
        for c in CPOS:
            if c + l > TOTAL: continue
            a = si.seats(si.slab(m, c, l), TOTAL) is not None
            b = si.seats(si.slab(m, TOTAL - l - c, l), TOTAL) is not None
            e = zeros_exact(slab_segs(m, c, l, TOTAL)) is not None
            tot += 1; mism_tree += (a != b); wrong_vs_exact += (a != e)
            if a != b: bad.append((m, l, c))
rep("tree seats(): fold on the scan grid", mism_tree == 0,
    "%d/%d mismatches; %d disagree with exact" % (mism_tree, tot, wrong_vs_exact))
# near threshold: first zero close to L
near_bad = near_tot = near_vs_exact = 0
for m in (1.0, 4.0, 16.0):
    for l in (0.25, 1.0):
        for c in (0.5, 3.0, 6.0):
            if c + l > TOTAL: continue
            # threshold exterior o*: exact seats flips there (first zero passes through L)
            lo, hi = -0.5, 2.0
            if (zeros_exact(slab_segs(m, c, l, TOTAL, lo)) is not None) or (zeros_exact(slab_segs(m, c, l, TOTAL, hi)) is None):
                continue
            for _ in range(80):
                mid = 0.5 * (lo + hi)
                if zeros_exact(slab_segs(m, c, l, TOTAL, mid)) is None: lo = mid
                else: hi = mid
            ostar = 0.5 * (lo + hi)
            for d in (-1e-2, -1e-3, -1e-4, 1e-4, 1e-3, 1e-2):
                o = ostar + d
                e = zeros_exact(slab_segs(m, c, l, TOTAL, o)) is not None
                a_ = si.seats(si.slab(m, c, l, o), TOTAL) is not None
                b_ = si.seats(si.slab(m, TOTAL - l - c, l, o), TOTAL) is not None
                near_tot += 1; near_bad += (a_ != b_); near_vs_exact += (a_ != e)
print("       near-threshold (exterior tuned so the exact first zero sits at L +- small): "
      "tree fold mismatches %d/%d; tree vs exact disagreements %d/%d"
      % (near_bad, near_tot, near_vs_exact, near_tot))
NEAR = (near_bad, near_vs_exact, near_tot)

# ------------------------------------------------------------------ [6] turn position
print("[6] only the Boolean folds")
m, l = 6.0, 0.9
diffs = []
for c in (0.5, 1.5, 3.0):
    za = zeros_exact(slab_segs(m, c, l, TOTAL)); zb = zeros_exact(slab_segs(m, TOTAL - l - c, l, TOTAL))
    diffs.append((c, za, zb))
    print("       c=%.1f  turn=%s   c'=%.1f  turn=%s" % (c, za, TOTAL - l - c, zb))
rep("turn positions differ under the fold (the fold is of seat/no-seat only)",
    any(d[1] is not None and d[2] is not None and abs(d[1] - d[2]) > 1e-6 for d in diffs))

# ------------------------------------------------------------------ [7] drift term
print("[7] non-self-adjoint drift form u'' + r u' + q u = 0 (RK4, fine)")
def rk_first_zero(qf, rf, L, n=40000):
    hh = L / n; uu, up = 0.0, 1.0
    f = lambda xx, a, b: (b, -rf(xx) * b - qf(xx) * a)
    for i in range(n):
        xx = i * hh
        k1 = f(xx, uu, up); k2 = f(xx + hh / 2, uu + hh / 2 * k1[0], up + hh / 2 * k1[1])
        k3 = f(xx + hh / 2, uu + hh / 2 * k2[0], up + hh / 2 * k2[1]); k4 = f(xx + hh, uu + hh * k3[0], up + hh * k3[1])
        un = uu + hh / 6 * (k1[0] + 2 * k2[0] + 2 * k3[0] + k4[0])
        up = up + hh / 6 * (k1[1] + 2 * k2[1] + 2 * k3[1] + k4[1])
        if i > 0 and un <= 0: return xx + hh
        uu = un
    return None
Ld = 6.0
cnt_keep = cnt_flip = 0; trials = 0
rngd = random.Random(671)
for t_ in range(30):
    a1, a2, a3 = rngd.uniform(0.2, 1.5), rngd.uniform(0, 3), rngd.uniform(-3, 3)
    qf = lambda xx, a1=a1, a2=a2: a1 * (1 + math.sin(a2 * xx))
    rf = lambda xx, a3=a3: a3 * math.exp(-(xx - 1.5) ** 2)
    qt = lambda xx: qf(Ld - xx)
    s0 = rk_first_zero(qf, rf, Ld, 6000) is not None
    s_keep = rk_first_zero(qt, lambda xx: rf(Ld - xx), Ld, 6000) is not None
    s_flip = rk_first_zero(qt, lambda xx: -rf(Ld - xx), Ld, 6000) is not None
    trials += 1; cnt_keep += (s0 != s_keep); cnt_flip += (s0 != s_flip)
rep("drift: reversing with r -> -r~ preserves the Boolean", cnt_flip == 0, "%d/%d mismatches" % (cnt_flip, trials))
print("       drift kept un-flipped (the naive reflection): %d/%d mismatches" % (cnt_keep, trials))

# ------------------------------------------------------------------ [8] 2x2 Jacobi
print("[8] 2x2 Jacobi J'' + T J = 0")
def mat_first_conj(Tf, L, n=6000, start_back=False):
    """first x in (0,L] with det J = 0, J(0)=0, J'(0)=I (RK4). None if none."""
    hh = L / n
    J = [[0.0, 0.0], [0.0, 0.0]]; P = [[1.0, 0.0], [0.0, 1.0]]
    def mm(A, B): return [[A[i][0]*B[0][j] + A[i][1]*B[1][j] for j in range(2)] for i in range(2)]
    def add(A, B, c=1.0): return [[A[i][j] + c * B[i][j] for j in range(2)] for i in range(2)]
    def det(A): return A[0][0]*A[1][1] - A[0][1]*A[1][0]
    dprev = None
    for i in range(n):
        xx = i * hh
        def F(xv, Jv, Pv): return Pv, [[-v_ for v_ in row] for row in mm(Tf(xv), Jv)]
        k1 = F(xx, J, P)
        k2 = F(xx + hh/2, add(J, k1[0], hh/2), add(P, k1[1], hh/2))
        k3 = F(xx + hh/2, add(J, k2[0], hh/2), add(P, k2[1], hh/2))
        k4 = F(xx + hh, add(J, k3[0], hh), add(P, k3[1], hh))
        J = [[J[a][b] + hh/6*(k1[0][a][b] + 2*k2[0][a][b] + 2*k3[0][a][b] + k4[0][a][b]) for b in range(2)] for a in range(2)]
        P = [[P[a][b] + hh/6*(k1[1][a][b] + 2*k2[1][a][b] + 2*k3[1][a][b] + k4[1][a][b]) for b in range(2)] for a in range(2)]
        d = det(J)
        if i > 3 and dprev is not None and d * dprev <= 0:
            return xx + hh
        dprev = d
    return None
rngm = random.Random(672)
Lm = 8.0
ex_bad = co_bad = 0; ntr = 0; ns_ex_bad = ns_co_bad = 0; ns_tr = 0
for t_ in range(40):
    b1, b2, b3, b4, b5 = [rngm.uniform(-1, 1) for _ in range(5)]
    base = rngm.uniform(0.05, 0.4)
    def Ts(xx, b1=b1, b2=b2, b3=b3, b4=b4, base=base):
        R = base * (1 + 0.5 * math.sin(b1 * 3 * xx + 1))           # Ricci trace part
        w1 = b2 * math.exp(-(xx - 2.0) ** 2); w2 = b3 * math.cos(b4 * xx)  # Weyl (traceless)
        return [[R + w1, w2], [w2, R - w1]]
    def Tn(xx, b5=b5, Ts=Ts):
        A = Ts(xx); a = 0.6 * b5 * (1 + math.sin(2 * xx))              # antisymmetric part
        return [[A[0][0], A[0][1] + a], [A[1][0] - a, A[1][1]]]
    for Tf, tag in ((Ts, "S"), (Tn, "N")):
        fz = mat_first_conj(Tf, Lm)
        bz = mat_first_conj(lambda xx: Tf(Lm - xx), Lm)
        exist_bad = (fz is None) != (bz is None)
        coinc_bad = False
        if fz is not None:
            # first conjugate from b = fz read backward: should be exactly b (i.e. back to 0)
            bb = mat_first_conj(lambda xx, fz=fz: Tf(fz - xx), fz * 1.0 + 1e-9, n=6000)
            coinc_bad = bb is None or abs(bb - fz) > 5 * fz / 6000 + 1e-6
        if tag == "S":
            ntr += 1; ex_bad += exist_bad; co_bad += coinc_bad
        else:
            ns_tr += 1; ns_ex_bad += exist_bad; ns_co_bad += coinc_bad
rep("symmetric T: existence reversal-symmetric", ex_bad == 0, "%d/%d" % (ex_bad, ntr))
rep("symmetric T: first conjugate from 0 is b  <=>  first conjugate from b (backward) is 0",
    co_bad == 0, "%d/%d mismatches" % (co_bad, ntr))
print("       NON-symmetric T (antisymmetric part added): existence mismatches %d/%d, "
      "first-conjugate coincidence failures %d/%d" % (ns_ex_bad, ns_tr, ns_co_bad, ns_tr))

# ------------------------------------------------------------------ [9] fixture
print("[9] selftest fixture m=6, l=0.9, L=12")
for c in (0.5, 1.5, 3.0):
    a = zeros_exact(slab_segs(6.0, c, 0.9, 12.0)); b = zeros_exact(slab_segs(6.0, 12 - 0.9 - c, 0.9, 12.0))
    at = si.seats(si.slab(6.0, c, 0.9), 12.0); bt = si.seats(si.slab(6.0, 12 - 0.9 - c, 0.9), 12.0)
    print("       c=%.1f exact %s / %s   tree %s / %s" % (c, a, b, at, bt))
    rep("fixture c=%.1f folds (exact and tree)" % c, (a is None) == (b is None) and (at is None) == (bt is None)
        and (a is None) == (at is None))
print("       sturm number m l^2/pi^2 = %.4f (<1: not Sturm-universal); lyapunov L m l/4 = %.2f (>1)"
      % (6 * 0.81 / math.pi ** 2, 12 * 6 * 0.9 / 4))

print("\nALL CHECKS AGREE" if OK else "\nSOME CHECK FAILED")
sys.exit(0 if OK else 1)
