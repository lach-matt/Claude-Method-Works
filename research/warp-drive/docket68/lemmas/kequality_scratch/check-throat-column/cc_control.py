"""Controls, far sides, one-umbilic-slice test, Jacobian probe (check-throat-column).  Own code; imports only my own
cc_numeric.py by path."""
import math
import sys
import importlib.util
import numpy as np
from scipy.optimize import brentq

here = "/tmp/claude-0/-home-user-Claude-Method-Works/6d820e7d-6d3c-5ac7-8067-527dc14c2847/scratchpad/kequality/check-throat-column/"
spec = importlib.util.spec_from_file_location("cc_numeric", here + "cc_numeric.py")
N = importlib.util.module_from_spec(spec)
spec.loader.exec_module(N)

convs = {"C-PRZ": (-0.25, 0.75), "C-SHEET-M4": (-0.125, 0.75), "C-S6": (-1 / 3, 1 / 3), "C-S7": (-1 / 6, 1 / 6),
         "C-MIRROR(-1/4)": (-0.25, None)}


def detector(sol, e, cA=1.0, cS=1.0, ymax=None):
    """Scan level surfaces: max |D|/e, and for each convention the spread of s2 and whether the target is met."""
    ys = sol.t[-1] if ymax is None else ymax
    yy = np.linspace(1e-6 * ys, ys * (1 - 1e-6), 3001)
    S = sol.sol(yy)
    a = S[2] - e
    D = S[3]
    res = {"maxD/e": float(np.max(np.abs(D)) / e)}
    for nm, (tg, lm) in convs.items():
        if lm is None:
            s2 = a / e                 # mirrored umbilic value ell*a (meaningful only where D = 0)
        else:
            x = -a / e
            s2 = -(x - np.sqrt(x * x - 1 + lm * lm)) / 2
        res[nm] = (float(s2.min()), float(s2.max()), float(s2.max() - s2.min()),
                   "everywhere" if np.max(np.abs(s2 - tg)) < 1e-9 else ("somewhere" if np.any(np.diff(np.sign(s2 - tg)) != 0) else "nowhere"))
    return res


print("== C1. pure AdS5 (cA = cS = 0), e = 1/4, 1, 4: exact alpha = beta = exp(-e y)")
for e in (0.25, 1.0, 4.0):
    sol = N.column(e, cA=0.0, cS=0.0, ymax=3 / e)
    yy = np.linspace(0, 3 / e, 7)
    S = sol.sol(yy)
    err = np.max(np.abs(S[0] + e * yy)) + np.max(np.abs(S[1] + e * yy)) + np.max(np.abs(S[2])) + np.max(np.abs(S[3]))
    d = detector(sol, e, 0, 0, ymax=3 / e)
    print(f"  e={e}: |deviation from exp(-ey)| = {err:.2e}; maxD/e = {d['maxD/e']:.1e};",
          {k: (round(v[0], 6), v[3]) for k, v in d.items() if k != 'maxD/e'})

print("== C1b. throat slices made negligible: alpha0 = beta0 = 1e12, y < 3 ell")
for e in (0.25, 1.0, 4.0):
    sol = N.column(e, al0=1e12, be0=1e12, ymax=3 / e)
    d = detector(sol, e, ymax=3 / e)
    print(f"  e={e}: maxD/e = {d['maxD/e']:.2e};", {k: (round(v[0], 6), f"spread {v[2]:.1e}", v[3]) for k, v in d.items() if k != 'maxD/e'})

print("== C2. mutation: the same detector on the corridor's throat column (alpha0 = beta0 = 1)")
for e in (0.25, 1.0, 4.0):
    sol = N.column(e, max_step=0.002)
    d = detector(sol, e)
    print(f"  e={e}: maxD/e = {d['maxD/e']:.2e};", {k: (round(v[0], 4), round(v[1], 4), f"spread {v[2]:.2f}", v[3]) for k, v in d.items() if k != 'maxD/e'})

print("== C3. positive control: alpha0=1, beta0=2 (R4 = -3/8), umbilic plane at s1 = 1/2: k = -e/2 must satisfy k^2 = e^2 + R4/12")
f = lambda e: (0.5 * e)**2 - (e * e - 3 / 8 / 12)
roots = [brentq(f, a, b, xtol=1e-15) for a, b in zip(np.linspace(1e-3, 2, 400)[:-1], np.linspace(1e-3, 2, 400)[1:]) if f(a) * f(b) < 0]
print("  scan roots:", roots, " 1/sqrt(24) =", 1 / math.sqrt(24))
# and integrate from that data: the constraint must hold at y = 0
e = 1 / math.sqrt(24)
s0 = [0.0, math.log(2.0), -e / 2 + e, 0.0]
print("  constraint at start:", N.constraint_rel(np.array(s0), e))

print("== C4. at most one umbilic slice: start umbilic with unequal radii, follow both ways")
for (e, al0, be0, sgn) in ((0.5, 1.0, 2.0, -1), (1.0, 2.0, 1.0, -1), (0.25, 1.0, 3.0, +1), (2.0, 1.5, 1.0, -1)):
    R4 = -1 / (2 * al0**2) + 1 / (2 * be0**2)
    k2 = e * e + R4 / 12
    if k2 < 0:
        print("  skip", e, al0, be0); continue
    k = sgn * math.sqrt(k2)
    fw = N.column(e, al0=al0, be0=be0, a0=k, D0=0.0, ymax=5.0, max_step=0.005)
    bw = N.column(e, al0=al0, be0=be0, a0=k, D0=0.0, ymax=5.0, direction=-1, max_step=0.005)
    yf = np.linspace(1e-4, fw.t[-1] * (1 - 1e-6), 4000)
    yb = np.linspace(1e-4, bw.t[-1] * (1 - 1e-6), 4000)
    Df, Db = fw.sol(yf)[3], bw.sol(yb)[3]
    print(f"  e={e} radii=({al0},{be0}) k={k:+.4f}: forward D>0 everywhere: {bool(np.all(Df > 0))} (min {Df.min():.2e}, to y={fw.t[-1]:.3f});"
          f" backward D<0 everywhere: {bool(np.all(Db < 0))} (max {Db.max():.2e}, to y=-{bw.t[-1]:.3f})")

print("== F1. C-S7 far side (decaying, e_f = e/6): distance z to alpha -> 0, z*e_f, Kasner exponent")
for e in (1 / 1024, 1 / 32, 1 / 8, 1.0, 4.0, 64.0):
    sol = N.column(e, max_step=0.002 if e < 8 else 0.0005)
    y2 = N.cs7_depth(sol, e)[0]
    u, v, at, D = sol.sol(y2)
    a = at - e
    ef = e / 6
    af = -math.sqrt(a * a - e * e + ef * ef)
    far = N.column(ef, al0=math.exp(u), be0=math.exp(v), a0=af, D0=D, ymax=50.0, max_step=0.002 if e < 8 else 0.0002)
    zs = far.t[-1]
    s1_, s2_ = far.sol(zs * (1 - 1e-5)), far.sol(zs * (1 - 1e-8))
    ex = (math.log(N.kretschmann(s2_, ef)) - math.log(N.kretschmann(s1_, ef))) / (s2_[0] - s1_[0])
    print(f"  e={e:<10.6g} y2={y2:.6g} far: a_f/e_f={af/ef:.4f} D={D:.4g} z_s={zs:.6g} z*e_f={zs*ef:.4g} dlnK/dln(alpha)={ex:.3f} min D_f>0: {bool(np.all(far.sol(np.linspace(0, zs*(1-1e-6), 2000))[3] > 0))}")

print("== F2. coincidence branches (y2 = 0): far side is the throat column at e_f, pure-trace start")
for e in (1 / 32, 1 / 8, 1.0):
    for nm, lm in (("C-SHEET-M4", 0.75), ("C-S6", 1 / 3)):
        ef = lm * e
        far = N.column(ef, max_step=0.002)
        print(f"  e={e:<8.4g} {nm:10s} e_f={ef:.5g} z*e_f={far.t[-1]*ef:.4f}")

print("== J. Jacobian of (rho_m, p_th,m) in (y2, e) [nu units]: det = 3 (a' D_e - (a_e - s2) D') -- probe")
def state(e, y):
    sol = N.column(e, max_step=0.001)
    return sol, sol.sol(y)
def jac(e, y2, s2, h=1e-6):
    sol = N.column(e, max_step=0.001)
    u, v, at, D = sol.sol(y2)
    a = at - e
    dydt = N.rhs(y2, [u, v, at, D], e)
    ap, Dp = dydt[2], dydt[3]
    sp_ = N.column(e + h, max_step=0.001).sol(y2); sm_ = N.column(e - h, max_step=0.001).sol(y2)
    ae = ((sp_[2] - (e + h)) - (sm_[2] - (e - h))) / (2 * h)
    De = (sp_[3] - sm_[3]) / (2 * h)
    J = np.array([[3 * ap + Dp / 2, 3 * ae + De / 2 - 3 * s2], [-3 * ap + Dp / 2, -3 * ae + De / 2 + 3 * s2]])
    return np.linalg.det(J), sol.t[-1]
for e in (1 / 32, 1 / 8, 1.0):
    ys = N.column(e, max_step=0.001).t[-1]
    row = []
    for frac in (0.25, 0.5, 0.75):
        for s2 in (-0.25, -1/3, -1/6, -0.125, 1.0):
            d, _ = jac(e, frac * ys, s2)
            row.append(f"f{frac}/s{s2:+.3f}:{d:.3g}")
    print(f"  e={e}: ", " ".join(row))
