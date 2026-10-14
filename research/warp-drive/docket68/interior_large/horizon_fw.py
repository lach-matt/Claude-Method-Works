"""horizon_fw.py -- item 407: FW's static RSII large hole with a node on the horizon s = 0 and exact regularity rows.

M, 407: "Proposed next step, yours to approve - approved."  The proposal: a static solver with a grid point on the
horizon itself, carrying exact regularity rows from the horizon analysis (T = A there, and each equation's own
limiting form at s = 0); no coefficients; a new instrument beside solver_fw.py, not an edit to it.
Question: does the near-null F direction disappear, and does xi then fall steadily with resolution?
Criterion: the smallest scaled singular value stops shrinking as N grows, and xi falls geometrically.

The record's solver (solver_fw.py) puts Radau nodes in s, which exclude s = 0, and imposes nothing there.  Here s and
x are both Lobatto, so s = 0 is a node, and at s = 0 the record's five equations are replaced by their own exact
limits.  The limits come from an exact truncated Laurent expansion in s of each equation's expression tree, with the
fields and their slopes held as symbols (no series is fitted, nothing is evaluated at small s):
    s E_e = S_e + R_e s + O(s^2),   S_e = the singular part, R_e = the regular part (fields fixed).
Measured (selftest H2): S_thth = S_xx = 0 identically; S_tt = (T - A) Dl0^2 / (4 A T) with Dl0 = 1/bt + 1 - x^2;
S_ss = -S_tt; S_sx = (A - T)(bt x^2 - bt - 1)(T_x (bt x^2 - bt - 1) - 4 T bt x) / (4 T^2 bt^2) -- not zero, but it
too carries the factor (A - T).  So the one condition T = A removes every 1/s, and the rows at s = 0 (0 < x < 1) are
    T row:  T - A = 0
    A row:  R_tt + R_ss                       (the 1/s parts cancel identically, so does their s-derivative)
    S row:  R_thth          B row:  R_xx
    F row:  R_sx + sum_q dS_sx/dq D_s q        (E_sx's own limit when T = A: q in {T, A, T_x}, D_s T_x = T_sx)
and the check, carried as a measurement and not a row:  C_tt = R_tt + sum_q dS_tt/dq D_s q, which is E_tt's own limit
and must fall with N if the smooth solution satisfies the tt equation at the horizon too.  The record's brane rows
(K_tt, K_thth, K_ss, xi^x) have no 1/s (H3), so the corner (0, 1) takes their exact s^0 coefficient, and the corner
(0, 0) takes the record's axis rows.  The top s = 1 and the other edges are the record's rows, unchanged.

python3 horizon_fw.py [N ...]       -- solve at each N (default 16 20 24 28 32): Newton, the singular values raw and
                                       row-then-column equilibrated (2-norms), the null-most mode, xi exactly at the
                                       fixed points static_conv used, C_tt, R4; HORIZON-FW.tsv
python3 horizon_fw.py --record N .. -- the same singular-value measurement on the record's Radau solver
python3 horizon_fw.py --selftest | --mutants
"""
import sys, os, time, random
import numpy as np, sympy as sp
import core_fw as C

MUT = set()
KMAX = 3
NAMES = C.names


# ------------------------------------------------------------------- the exact truncated Laurent expansion in s
class Jet:
    __slots__ = ("v", "c", "p")         # sum c[k] s^(v + k), exact for every power below p
    def __init__(self, v, c, p):
        self.v, self.c, self.p = v, c, p

def j_add(js):
    v = min(j.v for j in js); p = min(min(j.p for j in js), KMAX + 1)
    return Jet(v, [sp.Add(*[j.c[k - j.v] for j in js if 0 <= k - j.v < len(j.c)]) for k in range(v, p)], p)

def j_mul(a, b):
    v = a.v + b.v; p = min(a.p + b.v, b.p + a.v, KMAX + 1); out = []
    for k in range(v, p):
        out.append(sp.Add(*[sp.Mul(a.c[i], b.c[k - a.v - i - b.v]) for i in range(len(a.c))
                            if 0 <= k - a.v - i - b.v < len(b.c)]))
    return Jet(v, out, p)

def j_norm(a, probe):
    """drop leading coefficients that vanish identically (a random exact point, then expand, decides)"""
    if "nonorm" in MUT:
        return a
    while a.c and (a.c[0] == 0 or (probe(a.c[0]) == 0 and sp.expand(a.c[0]) == 0)):
        a = Jet(a.v + 1, a.c[1:], a.p)
    if not a.c:
        raise ValueError("no nonzero coefficient below the precision")
    return a

def j_inv(a, probe):
    a = j_norm(a, probe); n = min(a.p - a.v, KMAX + 1 + a.v)
    b = [1 / a.c[0]]
    for k in range(1, n):
        b.append(-b[0] * sp.Add(*[a.c[j] * b[k - j] for j in range(1, k + 1) if j < len(a.c)]))
    return Jet(-a.v, b, -a.v + n)

def j_rpow(a, r, probe):
    """a^r, r rational: c0^r s^(v r) (1 + u)^r by J.C.P. Miller's recurrence; v r must be an integer"""
    a = j_norm(a, probe)
    if (a.v * r).q != 1:
        raise ValueError("non-integer power of s")
    vr = int(a.v * r); n = min(a.p - a.v, KMAX + 1 - vr); u = [c / a.c[0] for c in a.c]; b = [sp.Integer(1)]
    for k in range(1, n):
        b.append(sp.Add(*[(r * j - (k - j)) * u[j] * b[k - j] for j in range(1, k + 1) if j < len(u)]) / k)
    return Jet(vr, [a.c[0] ** r * q for q in b], vr + n)

def expand_s(expr, s, probe):
    memo = {}
    def go(e):
        if e in memo:
            return memo[e]
        if e == s:
            r = Jet(1, [sp.Integer(1)], KMAX + 1)
        elif not e.has(s):
            r = Jet(0, [e], KMAX + 1)
        elif e.is_Add:
            r = j_add([go(a) for a in e.args])
        elif e.is_Mul:
            r = None
            for a in e.args:
                j = go(a); r = j if r is None else j_mul(r, j)
        elif e.is_Pow and e.exp.is_Integer:
            n = int(e.exp); base = go(e.base)
            if n < 0:
                base = j_inv(base, probe); n = -n
            r = base
            for _ in range(n - 1):
                r = j_mul(r, base)
        elif e.is_Pow and e.exp.is_Rational:
            r = j_rpow(go(e.base), e.exp, probe)
        else:
            raise TypeError("cannot expand %s" % type(e))
        memo[e] = r
        return r
    return go(expr)

def coef(J, k):
    if not J.v <= k < J.p:
        raise ValueError("power %d not known exactly (v %d, p %d)" % (k, J.v, J.p))
    return J.c[k - J.v] if k - J.v < len(J.c) else sp.Integer(0)

def make_probe(seed):
    rnd = random.Random(seed)
    vals = {q: sp.Rational(rnd.randint(1, 997), rnd.randint(1, 997)) * rnd.choice([1, -1])
            for q in [C.x, C.bt] + C.VARS}
    return lambda c: c.xreplace(vals) if hasattr(c, "xreplace") else c


# --------------------------------------------------------------------------------------- the rows at s = 0
SYM = {str(v): v for v in C.VARS}
def D_s(q):
    """the s-slope of a field symbol: T -> T_s, T_x -> T_sx, T_s -> T_ss; anything else is not available"""
    n, _, t = str(q).partition("_")
    return SYM[{"": n + "_s", "x": n + "_sx", "s": n + "_ss"}[t]]

def chain(S):
    return sp.Add(*[sp.diff(S, q) * D_s(q) for q in S.free_symbols if q in C.VARS])

def derive():
    probe = make_probe(1)
    J = [expand_s(E, C.s, probe) for E in C.RES]
    S = [coef(j, -1) if j.v < 0 else sp.Integer(0) for j in J]; R = [coef(j, 0) for j in J]
    Jb = [expand_s(B, C.s, probe) for B in C.BCS]
    T, A = SYM["T"], SYM["A"]
    rows = [T - A, R[0] + (R[0] if "ttonly" in MUT else R[2]), R[1], R[3],
            R[4] + (0 if "nochain" in MUT else chain(S[4]))]
    check = R[0] + chain(S[0])
    return dict(J=J, S=S, R=R, Jb=Jb, rows=rows, check=check, brane0=[coef(j, 0) for j in Jb])

class Rows:
    def __init__(self, d=None):
        self.d = d = d or derive()
        self.f = C.lam(d["rows"]); self.fj = C.lam([[sp.diff(e, v) for v in C.VARS] for e in d["rows"]])
        self.fb = C.lam(d["brane0"]); self.fbj = C.lam([[sp.diff(e, v) for v in C.VARS] for e in d["brane0"]])
        self.fc = C.lam(d["check"])


# ------------------------------------------------------------------------------------------------- the solver
def setup(N):
    """solver_fw.setup's layout with Lobatto nodes in s (s = 0 and s = 1 both nodes) in place of Radau"""
    sn, xn = C.lobatto01(N), C.lobatto01(N)
    I = np.eye(N + 1); Ds, Dx = np.kron(C.bary_D(sn), I), np.kron(I, C.bary_D(xn))
    S_, X_ = np.meshgrid(sn, xn, indexing="ij")
    return dict(Ns=N, Nx=N, sn=sn, xn=xn, Ds=Ds, Dx=Dx, Dss=Ds @ Ds, Dxx=Dx @ Dx, Dsx=Ds @ Dx,
                S=S_.ravel(), X=X_.ravel())

def residual_and_jac(G, U, b, H, want_jac=True):
    import solver_fw as SF
    n = len(G["S"]); vals = SF.dv(G, U)
    with np.errstate(all="ignore"):
        R = np.array([np.broadcast_to(np.asarray(r, dtype=float), (n,)) for r in SF.fres(G["S"], G["X"], b, *vals)])
        Rb = np.array([np.broadcast_to(np.asarray(r, dtype=float), (n,)) for r in SF.fbc(G["S"], G["X"], b, *vals)])
        Rh = np.array([np.broadcast_to(np.asarray(r, dtype=float), (n,)) for r in H.f(G["S"], G["X"], b, *vals)])
        Rb0 = np.array([np.broadcast_to(np.asarray(r, dtype=float), (n,)) for r in H.fb(G["S"], G["X"], b, *vals)])
    J = Jb = Jh = Jb0 = None
    if want_jac:
        with np.errstate(all="ignore"):
            J = SF.assemble(G, SF.fjac(G["S"], G["X"], b, *vals), 5)
            Jb = SF.assemble(G, SF.fbcj(G["S"], G["X"], b, *vals), 4)
            Jh = SF.assemble(G, H.fj(G["S"], G["X"], b, *vals), 5)
            Jb0 = SF.assemble(G, H.fbj(G["S"], G["X"], b, *vals), 4)
    on = lambda m: np.where(m)[0]
    s0, s1, x0, x1 = (np.abs(G["S"]) < 1e-14, np.abs(G["S"] - 1) < 1e-14, np.abs(G["X"]) < 1e-14,
                      np.abs(G["X"] - 1) < 1e-14)
    top, ax = on(s1), on(x0 & ~s1)
    br, br0 = on(x1 & ~s1 & ~s0), on(x1 & s0)
    hz = on(s0 & ~x0 & ~x1)
    fields = [U[i * n:(i + 1) * n] for i in range(5)]; Id = np.eye(n)
    def setrow(e, idx, val, parts=None, jrows=None):
        R[e, idx] = val
        if want_jac:
            J[e * n + idx, :] = 0
            for fi, M in parts or ():
                J[e * n + idx, fi * n:(fi + 1) * n] += M[idx]
            if jrows is not None:
                J[e * n + idx, :] = jrows
    for e in range(5):                                          # the horizon s = 0, 0 < x < 1: the exact limits
        setrow(e, hz, Rh[e, hz], jrows=(Jh[e * n + hz, :] if want_jac else None))
    target = [1, 1, 1, 1, 0]
    for e in range(5):
        setrow(e, top, fields[e][top] - target[e], [(e, Id)])
    setrow(1, ax, fields[1][ax] - fields[3][ax], [(1, Id), (3, -Id)])
    for e in (0, 2, 3, 4):
        setrow(e, ax, (G["Dx"] @ fields[e])[ax], [(e, G["Dx"])])
    for e in range(4):
        setrow(e, br, Rb[e, br], jrows=(Jb[e * n + br, :] if want_jac else None))
        setrow(e, br0, Rb0[e, br0], jrows=(Jb0[e * n + br0, :] if want_jac else None))
    setrow(4, np.concatenate([br, br0]), fields[4][np.concatenate([br, br0])], [(4, Id)])
    return R.ravel(), J

def newton(G, U, b, H, tol=1e-10, maxit=60):
    nr = np.inf; it = 0
    for it in range(maxit):
        R, J = residual_and_jac(G, U, b, H)
        nr = np.abs(R).max()
        if nr < tol or not np.isfinite(nr):
            break
        dU = np.linalg.solve(J, -R); lam = 1.0; n0 = np.linalg.norm(R)
        while lam > 1e-4:
            Rt = residual_and_jac(G, U + lam * dU, b, H, False)[0]
            if np.all(np.isfinite(Rt)) and np.linalg.norm(Rt) < n0:
                break
            lam /= 2
        U = U + lam * dU
    return U, nr, it


# --------------------------------------------------------------------------------------------- measurements
def sigma(J, n, G):
    """smallest and largest singular values raw and row-then-column equilibrated (2-norms), and the null-most mode"""
    out = {}
    for lab in ("raw", "eq"):
        M = J.copy()
        if lab == "eq":
            M /= np.linalg.norm(M, axis=1)[:, None]; M /= np.linalg.norm(M, axis=0)[None, :]
        Uu, sv, Vt = np.linalg.svd(M)
        v = Vt[-1]; k = np.argmax(np.abs(v)); f, i = divmod(k, n); si, xi = divmod(i, len(G["xn"]))
        out[lab] = dict(small=sv[-3:][::-1], large=sv[0], field="TSABF"[f], at=(G["sn"][si], G["xn"][xi]),
                        share=[float(np.linalg.norm(v[e * n:(e + 1) * n]) ** 2) for e in range(5)])
    return out

PTS = [(s_, x_) for s_ in ("0.5", "0.1", "0.02", "0.002") for x_ in ("0.03", "0.125", "0.5", "0.9")]
PTS += [("-0.002", x_) for x_ in ("0.03", "0.125", "0.5")]
def xi_at(G, U, b, E=None):
    """xi^s and xi^x exactly (deturck_exact, 50 digits) from the solution's own 2D polynomial, at static_conv's points"""
    import mpmath as mp, deturck_exact as D
    E = E or D.Exact(); N = len(G["sn"]) - 1; n = len(G["S"])
    sn = [mp.mpf(float(v)) for v in G["sn"]]; xn = [mp.mpf(float(v)) for v in G["xn"]]
    ws, wx = D.bary_w(sn), D.bary_w(xn)
    F = {nm: [[mp.mpf(float(v)) for v in r] for r in U[e * n:(e + 1) * n].reshape(N + 1, len(xn))]
         for e, nm in enumerate(D.NAMES)}
    out = []
    for sv, xv in PTS:
        sv, xv = mp.mpf(sv), mp.mpf(xv); vals, ds, dx = {}, {}, {}
        for nm in D.NAMES:
            cv, cs = [], []
            for j in range(len(xn)):
                v, d = D.poly_at(sn, ws, [F[nm][i][j] for i in range(N + 1)], sv); cv.append(v); cs.append(d)
            vals[nm], dx[nm] = D.poly_at(xn, wx, cv, xv); ds[nm], _ = D.poly_at(xn, wx, cs, xv)
        o = E.at(sv, xv, mp.mpf(b), vals, ds, dx)
        out.append((float(sv), float(xv), float(o["xi^s"][0]), float(o["xi^x"][0])))
    return out

def check_at(G, U, b, H):
    import solver_fw as SF
    vals = SF.dv(G, U); n = len(G["S"])
    with np.errstate(all="ignore"):
        c = np.broadcast_to(np.asarray(H.fc(G["S"], G["X"], b, *vals), dtype=float), (n,))
    m = (np.abs(G["S"]) < 1e-14) & (G["X"] > 1e-14) & (G["X"] < 1 - 1e-14)
    return float(np.abs(c[m]).max())

def R4(G, U, b):
    n = len(G["S"]); N = len(G["sn"]) - 1
    return b * np.sqrt(U[n:2 * n].reshape(N + 1, -1)[0, -1])

def run(Ns, b=1.0, out="HORIZON-FW.tsv"):
    """each N from the saved solution in HFW_DIR if there is one, else from the previous N regridded (from ones at
    the first); every row is written to the table as its N closes"""
    import solver_fw as SF
    t0 = time.time(); H = Rows(); E = None; where = os.environ.get("HFW_DIR", ".")
    print("rows derived and compiled  [%.0f s]" % (time.time() - t0), flush=True)
    head = ["N", "newton_R", "steps", "raw_s1", "raw_s2", "raw_s3", "raw_max", "eq_s1", "eq_s2", "eq_s3", "eq_max",
            "eq_mode_field", "max_xis", "max_xix", "max_xis_s-0.002", "C_tt", "R4"]
    head += ["xis(%s,%s)" % p for p in PTS] + ["xix(%s,%s)" % p for p in PTS]
    with open(out, "w") as fh:
        fh.write("\t".join(head) + "\n")
    Gp = Up = None; lines = []
    for N in Ns:
        G = setup(N); n = len(G["S"]); t1 = time.time(); saved = os.path.join(where, "hfw_bt%g_%d.npy" % (b, N))
        if os.path.exists(saved):
            U0 = np.load(saved); src = "saved"
        elif Up is None:
            U0 = np.concatenate([np.ones(4 * n), np.zeros(n)]); src = "ones"
        else:
            U0 = SF.regrid(Gp, Up, G); src = "regridded"
        U, nr, it = newton(G, U0, b, H)
        R, J = residual_and_jac(G, U, b, H); sg = sigma(J, n, G)
        import deturck_exact as D
        E = E or D.Exact(); xs = xi_at(G, U, b, E); ck = check_at(G, U, b, H)
        ms = max(abs(r[2]) for r in xs if r[0] > 0); mx = max(abs(r[3]) for r in xs if r[0] > 0)
        m0 = max(abs(r[2]) for r in xs if r[0] < 0)
        print("N = %2d: Newton |R| %.1e after %d steps from %s  [%.0f s]" % (N, nr, it, src, time.time() - t1),
              flush=True)
        for lab in ("raw", "eq"):
            q = sg[lab]
            print("    %-3s singular values: smallest %s  largest %.2e; null-most mode in %s at (s, x) = (%.4f, %.3f), "
                  "share T S A B F %s" % (lab, " ".join("%.2e" % v for v in q["small"]), q["large"], q["field"],
                                           q["at"][0], q["at"][1], " ".join("%.2f" % v for v in q["share"])),
                  flush=True)
        print("    xi exact: max |xi^s| %.3e  max |xi^x| %.3e  (s > 0);  continued to s = -0.002: max |xi^s| %.3e;"
              "  C_tt at the horizon %.2e;  R4 %.10f" % (ms, mx, m0, ck, R4(G, U, b)), flush=True)
        L = [N, nr, it, *sg["raw"]["small"], sg["raw"]["large"], *sg["eq"]["small"], sg["eq"]["large"],
             sg["eq"]["field"], ms, mx, m0, ck, R4(G, U, b)] + [r[2] for r in xs] + [r[3] for r in xs]
        lines.append(L)
        with open(out, "a") as fh:
            fh.write("\t".join(v if isinstance(v, str) else ("%d" % v if isinstance(v, int) else "%.6e" % v)
                               for v in L) + "\n")
        np.save(saved, U)
        Gp, Up = G, U
    return lines

def record(Ns, b=1.0):
    """the record's Radau solver, measured the same way (sigma), from ones at the first N, regridded after"""
    import solver_fw as SF
    Gp = Up = None
    for N in Ns:
        G = SF.setup(N, N); n = len(G["S"]); t1 = time.time()
        U0 = np.concatenate([np.ones(4 * n), np.zeros(n)]) if Up is None else SF.regrid(Gp, Up, G)
        U, nr = SF.newton(G, U0, b); R, J = SF.residual_and_jac(G, U, b); sg = sigma(J, n, G)
        print("record N = %2d: |R| %.1e  [%.0f s]" % (N, nr, time.time() - t1), flush=True)
        for lab in ("raw", "eq"):
            q = sg[lab]
            print("    %-3s smallest %s  largest %.2e; null-most in %s at (%.4f, %.3f)" % (
                lab, " ".join("%.2e" % v for v in q["small"]), q["large"], q["field"], q["at"][0], q["at"][1]),
                flush=True)
        Gp, Up = G, U


# ---------------------------------------------------------------------------------------------- selftest / mutants
def test_fields(sv, xv):
    """a smooth configuration with T = A at s = 0 and T_s != A_s, every slope exact; returns VARS' values"""
    x_, s_ = sp.symbols("x_ s_")
    F = {"T": 1 + sp.Rational(3, 10) * s_ + x_ ** 2 / 10, "S": 1 + s_ * x_ / 5 + x_ ** 2 / 20,
         "B": 1 - s_ / 10 + x_ ** 2 / 20, "F": sp.Rational(3, 10) * x_ * s_ * (1 - x_ ** 2)}
    F["A"] = F["T"] - s_ * (1 + x_) / 5
    out = []
    for nm in NAMES:
        f = F[nm]
        for d in (f, f.diff(s_), f.diff(x_), f.diff(s_, 2), f.diff(x_, 2), f.diff(s_, x_)):
            out.append(float(d.subs({s_: sv, x_: xv})))
    return out

def selftest(quiet=False):
    ok = []; s, x = C.s, C.x
    def say(m):
        if not quiet:
            print(m, flush=True)
    probe = make_probe(7)
    # H1: the expander against sympy's own series, including a hidden factor of s and a cancelling leading term
    tests = [sp.sqrt(4 + 3 * s + s ** 2 * x) / (s * (2 + s)),
             1 / (x * s ** 3 - 2 * x * s ** 2 + x * s) ** 2 * (1 + s) ** 3,
             (2 + s) / ((1 + s) ** 2 - 1 - 2 * s + s ** 3 * x) * s ** 2]
    good = True
    for e in tests:
        try:
            Jt = expand_s(e, s, probe); ref = sp.series(e, s, 0, Jt.p).removeO()
            good &= all(sp.simplify(coef(Jt, k) - ref.coeff(s, k)) == 0 for k in range(Jt.v, Jt.p))
        except (ValueError, ZeroDivisionError, TypeError):
            good = False
    ok.append(good); say("H1 the Laurent expander matches sympy's series on three test forms: %s" % good)
    d = derive(); S = d["S"]; T, A = SYM["T"], SYM["A"]
    pr = [make_probe(k) for k in (11, 12, 13)]
    z = lambda e: all(p(e) == 0 for p in pr)
    Dl0 = 1 / C.bt + 1 - x ** 2
    h2 = (z(S[1]) and z(S[3]) and z(S[0] + S[2]) and z(S[0].subs(T, A)) and z(S[4].subs(T, A))
          and z(S[0] - (T - A) * Dl0 ** 2 / (4 * A * T)) and not z(S[4]))
    ok.append(h2); say("H2 S_thth = S_xx = S_tt + S_ss = 0, S_tt = (T-A) Dl0^2/(4AT), S_sx != 0 but 0 at T = A: %s" % h2)
    h3 = all(j.v >= 0 for j in d["Jb"])
    ok.append(h3); say("H3 the record's brane rows carry no 1/s: %s" % h3)
    # H4: the rows are the equations' own limits -- E at small s on a smooth configuration approaches each row
    fE = C.lam(C.RES); fr = C.lam(d["rows"]); fc = C.lam(d["check"]); h4 = True
    for xv in (0.3, 0.7):
        r0 = np.array(fr(0.0, xv, 1.0, *test_fields(0.0, xv)), dtype=float); c0 = float(fc(0.0, xv, 1.0,
                                                                                          *test_fields(0.0, xv)))
        errs = []
        for sv in (1e-4, 1e-5):
            Ev = np.array(fE(sv, xv, 1.0, *test_fields(sv, xv)), dtype=float)
            lim = np.array([Ev[0] + Ev[2], Ev[1], Ev[3], Ev[4], Ev[0]])
            errs.append(np.abs(lim - np.r_[r0[1:], c0]))
        h4 &= bool(np.all(errs[1] < 2e-4) and np.all(errs[1] <= errs[0] * 0.2 + 1e-9) and abs(r0[0]) < 1e-15)
        say("    x %.1f: |E(s) - row| at s = 1e-4: %s;  at 1e-5: %s" % (
            xv, " ".join("%.1e" % v for v in errs[0]), " ".join("%.1e" % v for v in errs[1])))
    ok.append(h4); say("H4 every row (and C_tt) is its equation's limit, the error falling linearly in s: %s" % h4)
    G = setup(6)
    h5 = (abs(G["sn"][0]) < 1e-15 and abs(G["sn"][-1] - 1) < 1e-15 and np.allclose(G["Ds"] @ G["S"], 1))
    ok.append(h5); say("H5 the grid has nodes at s = 0 and s = 1 and differentiates s exactly: %s" % h5)
    return all(ok)

def mutants():
    caught = 0; names = ["nochain", "ttonly", "nonorm"]
    for m in names:
        MUT.clear(); MUT.add(m)
        try:
            r = selftest(quiet=True)
        except Exception:
            r = False
        caught += not r; print("mutant %-8s %s" % (m, "caught" if not r else "SURVIVED"), flush=True)
    MUT.clear(); print("%d/%d caught" % (caught, len(names)))
    return caught == len(names)

if __name__ == "__main__":
    a = sys.argv[1:]
    if a and a[0] == "--selftest":
        sys.exit(0 if selftest() else 1)
    if a and a[0] == "--mutants":
        sys.exit(0 if mutants() else 1)
    if a and a[0] == "--record":
        record([int(v) for v in a[1:]] or [16, 20, 24, 28, 32]); sys.exit(0)
    run([int(v) for v in a] or [16, 20, 24, 28, 32])
