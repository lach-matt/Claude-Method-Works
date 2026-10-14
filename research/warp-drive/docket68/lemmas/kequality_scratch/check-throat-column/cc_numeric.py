"""Independent numerics (check-throat-column).  Own RHS, own variables; no owner import.

Variables: u = ln alpha, v = ln beta, at = a + e (a = (p+q)/2), D = q - p.   Units m = 1, e = 1/ell.
  u' = a - D/2,  v' = a + D/2
  at' = 8 e at - 4 at^2 + (cS/(8 beta^2) - cA/(8 alpha^2))        [unconstrained form of a' from E1]
  D'  = -4 a D + cA/(4 alpha^2) + cS/(4 beta^2)
Constraint (monitored, not imposed): 6a^2 - D^2/2 - 6e^2 - R4/2 = 0, R4 = -cA/(2 alpha^2) + cS/(2 beta^2).
"""
import math
import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import brentq, minimize_scalar

RTOL, ATOL = 1e-13, 1e-14
U_END = math.log(1e-9)


def rhs(y, s, e, cA=1.0, cS=1.0):
    u, v, at, D = s
    a = at - e
    ia2, ib2 = math.exp(-2 * u), math.exp(-2 * v)
    return [a - D / 2, a + D / 2,
            8 * e * at - 4 * at * at + cS * ib2 / 8 - cA * ia2 / 8,
            -4 * a * D + cA * ia2 / 4 + cS * ib2 / 4]


def rhs_constrained(y, s, e, cA=1.0, cS=1.0):
    """second form: a' = e^2 - a^2 - D^2/4 (constraint used), in at: at' = 2 e at - at^2 - D^2/4."""
    u, v, at, D = s
    a = at - e
    ia2, ib2 = math.exp(-2 * u), math.exp(-2 * v)
    return [a - D / 2, a + D / 2, 2 * e * at - at * at - D * D / 4, -4 * a * D + cA * ia2 / 4 + cS * ib2 / 4]


def column(e, al0=1.0, be0=1.0, a0=None, D0=0.0, cA=1.0, cS=1.0, form=rhs, ymax=60.0, direction=1, max_step=np.inf):
    """Integrate from y = 0.  Default start: our plane, alpha = beta = 1, p = q = -e (at = 0, D = 0)."""
    at0 = 0.0 if a0 is None else a0 + e
    s0 = [math.log(al0), math.log(be0), at0, D0]

    def end(y, s, *_):
        return min(s[0], s[1]) - U_END
    end.terminal = True

    def blow(y, s, *_):
        return 1e12 - abs(s[2]) - abs(s[3])
    blow.terminal = True
    f = (lambda y, s: form(y, s, e, cA, cS)) if direction == 1 else (lambda y, s: [-z for z in form(-y, s, e, cA, cS)])
    sol = solve_ivp(f, [0, ymax], s0, method="DOP853", rtol=RTOL, atol=ATOL, events=[end, blow], dense_output=True,
                    max_step=max_step)
    return sol


def constraint_rel(s, e, cA=1.0, cS=1.0):
    u, v, at, D = s
    a = at - e
    ia2, ib2 = np.exp(-2 * u), np.exp(-2 * v)
    R4 = -cA * ia2 / 2 + cS * ib2 / 2
    c = 6 * a * a - D * D / 2 - 6 * e * e - R4 / 2
    scale = 6 * a * a + D * D / 2 + 6 * e * e + abs(cA * ia2) / 4 + abs(cS * ib2) / 4
    return np.abs(c) / scale


def kretschmann(s, e, cA=1.0, cS=1.0):
    u, v, at, D = s
    a = at - e
    p, q = a - D / 2, a + D / 2
    ia2, ib2 = np.exp(-2 * u), np.exp(-2 * v)
    P = 4 * e * e - 2 * p * (p + q) - cA * ia2 / 4      # p'
    Q = 4 * e * e - 2 * q * (p + q) + cS * ib2 / 4      # q'
    return 4 * (2 * (P + p * p)**2 + 2 * (Q + q * q)**2 + (p * p + cA * ia2 / 4)**2 + (q * q - cS * ib2 / 4)**2
                + 4 * p * p * q * q)


def report():
    out = {}
    egrid = [0.0, 1 / 1024, 1 / 256, 1 / 64, 1 / 32, 1 / 16, 1 / 8, 1 / 4, 1 / 2, 1.0, 2.0, 4.0, 8.0, 16.0, 32.0, 64.0]
    print("== 1. columns: y_s, e*y_s, min D, max at (=a+e), constraint rel err, cross-form agreement")
    eys = []
    for e in egrid:
        sol = column(e, max_step=0.002 if e < 8 else 0.0005)
        ys = sol.t[-1]
        ok = sol.status == 1 and len(sol.t_events[0]) > 0
        yy = np.linspace(1e-4 * ys, ys * (1 - 1e-6), 20001)
        S = sol.sol(yy)
        Dmin, atmax = S[3].min(), S[2].max()
        cmax95 = constraint_rel(sol.sol(np.linspace(1e-4 * ys, 0.95 * ys, 4001)), e).max()
        cmax99 = constraint_rel(sol.sol(np.linspace(1e-4 * ys, 0.99 * ys, 4001)), e).max()
        sol2 = column(e, form=rhs_constrained, max_step=0.002 if e < 8 else 0.0005)
        y99 = np.linspace(1e-4 * ys, 0.99 * min(ys, sol2.t[-1]), 4001)
        dif = np.max(np.abs(sol.sol(y99)[2:] - sol2.sol(y99)[2:]) / (1 + np.abs(sol.sol(y99)[2:])))
        # D/e vs analytic small-y: D ~ y/2
        print(f"  e={e:<10.6g} y_s={ys:.10g} e*y_s={e*ys:.6g} reached={ok} minD={Dmin:.3e} max(a+e)={atmax:.3e}"
              f" cons95={cmax95:.1e} cons99={cmax99:.1e} |unc-con|99={dif:.1e} y_s(con)={sol2.t[-1]:.10g}")
        eys.append(e * ys)
        out[e] = sol
    print("  e*y_s strictly rising on grid:", all(b > a for a, b in zip(eys, eys[1:])))
    return out


def cs7_depth(sol, e):
    """C-S7 decaying far side: s2 = -1/6 at ell_f = 6 ell  <=>  |a|/e = 13/8  <=>  at = -5e/8."""
    ys = sol.t[-1]
    f = lambda y: sol.sol(y)[2] + 5 * e / 8
    yy = np.linspace(1e-9 * ys, ys * (1 - 1e-9), 20001)
    v = np.array([f(z) for z in yy])
    idx = np.where(np.sign(v[:-1]) != np.sign(v[1:]))[0]
    roots = [brentq(f, yy[i], yy[i + 1], xtol=1e-14) for i in idx]
    return roots


def s2_free(a, e, lam, branch="dec"):
    x = -a / e
    rt = math.sqrt(x * x - 1 + lam * lam)
    return -(x - rt) / 2 if branch == "dec" else -(x + rt) / 2


def wec_threshold(s2):
    """e* where max_y [ (p + 2q) - 3 s2 e ] = 0 on the column; p + 2q = 3a + D/2."""
    def F(e, ret=False):
        sol = column(e, max_step=0.002)
        ys = sol.t[-1]
        L = lambda y: float(3 * (sol.sol(y)[2] - e) + sol.sol(y)[3] / 2 - 3 * s2 * e)
        yy = np.linspace(1e-6 * ys, ys * (1 - 1e-7), 6001)
        vals = np.array([L(z) for z in yy])
        i = int(np.argmax(vals))
        lo, hi = yy[max(i - 1, 0)], yy[min(i + 1, len(yy) - 1)]
        r = minimize_scalar(lambda z: -L(z), bounds=(lo, hi), method="bounded", options={"xatol": 1e-13})
        if ret:
            return -r.fun, r.x / ys
        return -r.fun
    # bracket
    es = np.geomspace(1e-3, 1.0, 40)
    vs = [F(z) for z in es]
    for i in range(len(es) - 1):
        if vs[i] > 0 and vs[i + 1] < 0:
            est = brentq(F, es[i], es[i + 1], xtol=1e-12)
            return est, F(est, ret=True)[1]
    return None, None


if __name__ == "__main__":
    cols = report()

    print("== 2. C-S7 depth curve (at = -5e/8)")
    for e in (1 / 1024, 1 / 256, 1 / 32, 0.25, 1.0, 4.0, 16.0, 64.0):
        sol = cols.get(e) or column(e, max_step=0.002)
        roots = cs7_depth(sol, e)
        y2 = roots[0] if roots else None
        chk = s2_free(sol.sol(y2)[2] - e, e, 1 / 6) if y2 else None
        print(f"  e={e:<10.6g} roots={len(roots)} y2={y2:.6g} e*y2={e*y2:.6g} y2/y_s={y2/sol.t[-1]:.4f} s2 check={chk:.12f}")

    print("== 3. free-far-side s2 along columns vs targets (sampled), convention by convention")
    convs = {"C-PRZ": (-0.25, 0.75), "C-SHEET-M4": (-0.125, 0.75), "C-S6": (-1 / 3, 1 / 3), "C-S7": (-1 / 6, 1 / 6)}
    for e in (1 / 64, 1.0, 64.0):
        sol = cols[e]
        ys = sol.t[-1]
        yy = np.linspace(1e-6 * ys, ys * (1 - 1e-6), 4001)
        A = sol.sol(yy)[2] - e
        for nm, (tg, lm) in convs.items():
            dec = np.array([s2_free(a, e, lm, "dec") for a in A])
            gro = np.array([s2_free(a, e, lm, "gro") for a in A])
            ndec = int(np.sum(np.sign(dec[:-1] - tg) != np.sign(dec[1:] - tg)))
            print(f"  e={e:<8.4g} {nm:11s} dec in [{dec.min():.6f},{dec.max():.6f}] crossings={ndec}; gro max={gro.max():.6f}")

    print("== 4. WEC thresholds ell* (positive README energy on mirrored level-surface P2)")
    m_ex = 7.5918511091462209829e-36 * math.sqrt(2742570311524972) / 2
    print(f"  example README: r_min(1) sqrt(N) = {2*m_ex:.6e} m, m = {m_ex:.6e} m")
    for s2 in (-0.25, -1 / 3, -1 / 6, -0.125, 1.0):
        est, frac = wec_threshold(s2)
        print(f"  s2={s2:+.4f}: e*={est:.7f}  ell*/m={1/est:.4f}  best depth/y_s={frac:.3f}  ell*={m_ex/est:.4e} m")

    print("== 5. singular end: Kretschmann exponent d ln K / d ln alpha near y_s")
    for e in (1 / 32, 1.0, 64.0):
        sol = cols[e]
        ys = sol.t[-1]
        y1, y2_ = ys * (1 - 1e-5), ys * (1 - 1e-8)
        s1_, s2_ = sol.sol(y1), sol.sol(y2_)
        expo = (math.log(kretschmann(s2_, e)) - math.log(kretschmann(s1_, e))) / (s2_[0] - s1_[0])
        print(f"  e={e}: dlnK/dln(alpha) = {expo:.4f}  (Kasner prediction -16/(1+sqrt3) = {-16/(1+math.sqrt(3)):.4f})")
