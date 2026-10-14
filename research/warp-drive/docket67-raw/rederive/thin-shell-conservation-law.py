#!/usr/bin/env python3
"""DOCKET 67 -- rederivation of the thin-shell surface conservation law as wall.py uses it.

Source: Poisson & Visser, gr-qc/9506083 eqs (8)-(13), (15)-(16); Ishak & Lake gr-qc/0108058 eqs (5)-(8), (12).
Tree:   research/warp-drive/wall.py:222-235 (method), 316-325 (sigma_of_R, p_of_R), 377-384 (dec asymptote),
        389-393 (gap).  wall.py is IMPORTED read-only; nothing under research/ is written.

Checks
 1  Israel/Lanczos surface stress for a dynamic shell R(tau) between two STATIC VACUUM Schwarzschild regions
    f_in = 1-2M_in/R, f_out = 1-2M_out/R (M_in = 0: Minkowski) implies d(sigma A)/dtau + p dA/dtau = 0
    IDENTICALLY in (R, Rdot, Rddot, M_in, M_out)  [PV (13) generalised to unequal masses].
    Regression: two exteriors of equal M (PV's wormhole) reproduce PV (11), (12).
 2  The conservation law <=> sigma' = -(2/R)(sigma+p) <=> m_s' = -8 pi R p (m_s = 4 pi R^2 sigma).
 3  Static values at M_in = 0 equal wall.statics(): sigma0 = (1-s)/(4 pi R), p0 = (1-s)^2/(16 pi R s).
 4  Linear EOS p = p0 + b2 (sigma - sigma0): dsolve reproduces wall.sigma_of_R; A = 1+b2 = 0 is a degenerate
    case (logarithm) the closed form excludes.
 5  INDICATION (not a full computation): with an outgoing-Vaidya exterior, sigma A picks up a dM/du term the
    vacuum derivation lacks.  K_tautau is not recomputed for Vaidya, so the flux-law itself is READ at source
    (Ishak-Lake eqs (6), (12): the transparency condition [G n u] = 0 is what the no-flux law needs).
 6  Dec asymptote 2(b2 sigma0 - p0)/(1+b2) and the gap identity beta2_crit - p0/sigma0 = x/(4 s^2 (1+3s)),
    both symbolic; z3 proves the gap > 0 for all s in (0,1).
 7  Numeric: RK4 of sigma' = -(2/R)(sigma+p) vs closed form; period via an RK4-sigma potential vs the
    closed-form potential vs 2pi/sqrt(V''/2) at the three points wall.py:231-235 names.
 8  Scope of the linear-EOS extrapolation (wall.py:205-216, BONUS): a NONLINEAR barotropic EOS with the
    SAME slope at sigma0 (so the same V''(R0) and the same stability verdict) whose dec margin sigma - p along
    the conservation curve crosses zero at finite R.  This is a scope note on a downstream claim, not on the
    conservation law.
"""
import sys, math, json
import sympy as sp

sys.dont_write_bytecode = True
sys.path.insert(0, "/home/user/Claude-Method-Works/research/warp-drive")
import wall  # read-only import

res = {}
def rec(k, ok, detail=""):
    res[k] = {"ok": bool(ok), "detail": str(detail)}
    print(("PASS " if ok else "FAIL ") + k + ("  " + str(detail) if detail else ""))

R, Rd, Rdd = sp.symbols("R Rdot Rddot", real=True)
Mi, Mo, M = sp.symbols("M_in M_out M", real=True)
pi = sp.pi

def Kth(f):   # K^theta_theta on one side, outward normal, timelike shell
    return sp.sqrt(f + Rd**2) / R
def Ktt(f):   # K^tau_tau on one side
    return (Rdd + sp.diff(f, R) / 2) / sp.sqrt(f + Rd**2)

def surface(f_minus, f_plus, sgn_minus=1, sgn_plus=1):
    """[K] = K^+ - K^-; sgn = orientation of the normal relative to increasing r on that side."""
    jth = sgn_plus * Kth(f_plus) - sgn_minus * Kth(f_minus)
    jtt = sgn_plus * Ktt(f_plus) - sgn_minus * Ktt(f_minus)
    sigma = -jth / (4 * pi)                 # PV (8)
    p = (jtt + jth) / (8 * pi)              # PV (8)
    return sp.simplify(sigma), sp.simplify(p)

def ddtau(expr):
    return sp.diff(expr, R) * Rd + sp.diff(expr, Rd) * Rdd

# --- 1 ------------------------------------------------------------------------
fi, fo = 1 - 2 * Mi / R, 1 - 2 * Mo / R
sig, p = surface(fi, fo)
A = 4 * pi * R**2
cons = sp.simplify(ddtau(sig * A) + p * ddtau(A))
rec("1a conservation identically zero, static vacuum both sides, M_in != M_out", cons == 0, cons)
# numeric spot-check with M_in < 0 and random Rdot, Rddot (guards simplify)
import random
random.seed(1)
worst = 0.0
for _ in range(200):
    vals = {Mi: random.uniform(-2, 0.4), Mo: random.uniform(0, 0.45), R: random.uniform(1.0, 5.0),
            Rd: random.uniform(-2, 2), Rdd: random.uniform(-3, 3)}
    worst = max(worst, abs(float((ddtau(sig * A) + p * ddtau(A)).subs(vals).evalf())))
rec("1b numeric spot-check of 1a over 200 random points (incl. M_in<0)", worst < 1e-12, "max |residual| = %.2e" % worst)
# PV wormhole: two exteriors, normals both pointing away from throat -> [K] = 2 K^+ with sign flip on the minus side
fw = 1 - 2 * M / R
sw, pw = surface(fw, fw, sgn_minus=-1, sgn_plus=1)
pv11 = -sp.sqrt(1 - 2 * M / R + Rd**2) / (2 * pi * R)
pv12 = (1 - M / R + Rd**2 + R * Rdd) / (4 * pi * R * sp.sqrt(1 - 2 * M / R + Rd**2))
rec("1c PV eq (11) reproduced (wormhole, sigma < 0)", sp.simplify(sw - pv11) == 0)
rec("1d PV eq (12) reproduced", sp.simplify(pw - pv12) == 0)
rec("1e PV eq (13) holds for the wormhole", sp.simplify(ddtau(sw * A) + pw * ddtau(A)) == 0)

# --- 2 ------------------------------------------------------------------------
S, P, Sp = sp.symbols("sigma p sigma_prime", real=True)
# d(sigma A)/dtau + p dA/dtau = Rdot [ (sigma A)' + p A' ] ; divide by Rdot (nonzero on a moving shell)
lhs = sp.expand(4 * pi * (R**2 * Sp + 2 * R * S) + P * 8 * pi * R)
sol = sp.solve(lhs, Sp)[0]
rec("2a conservation <=> sigma' = -(2/R)(sigma+p)", sp.simplify(sol + 2 * (S + P) / R) == 0, sol)
ms_prime = sp.diff(4 * pi * R**2, R) * S + 4 * pi * R**2 * sol
rec("2b m_s' = -8 pi R p", sp.simplify(ms_prime + 8 * pi * R * P) == 0, sp.simplify(ms_prime))
# PV (21): [sigma a]' = -(sigma + 2p)
rec("2c PV eq (21) [sigma R]' = -(sigma+2p)", sp.simplify(S + R * sol + (S + 2 * P)) == 0)

# --- 3 ------------------------------------------------------------------------
m_ = sp.symbols("m", positive=True)
s0, p0s = surface(sp.Integer(1), 1 - 2 * m_ / R)
s0 = s0.subs({Rd: 0}); p0s = p0s.subs({Rd: 0, Rdd: 0})
worst = 0.0
for x in (0.05, 0.3, 0.5, 0.8, 0.96):
    ss, mm, sg0, pp0 = wall.statics(x, 1.0)
    a = float(s0.subs({R: 1, m_: mm})); b = float(p0s.subs({R: 1, m_: mm}))
    worst = max(worst, abs(a - sg0) / sg0, abs(b - pp0) / pp0)
rec("3a Israel statics at M_in=0 equal wall.statics() (sigma0, p0)", worst < 1e-11, "max rel err %.1e" % worst)

# --- 4 ------------------------------------------------------------------------
b2, sg0, pp0, R0 = sp.symbols("beta2 sigma0 p0 R0", real=True)
sigf = sp.Function("sigma")
ode = sp.Eq(sigf(R).diff(R), -2 / R * (sigf(R) + pp0 + b2 * (sigf(R) - sg0)))
gen = sp.dsolve(ode, sigf(R), ics={sigf(R0): sg0})
Aa = 1 + b2; K = pp0 - b2 * sg0
closed = (sg0 + K / Aa) * (R / R0)**(-2 * Aa) - K / Aa
d = sp.simplify(sp.expand_power_base(gen.rhs - closed, force=True))
if d != 0:
    d = sp.simplify(sp.powsimp(sp.expand(gen.rhs - closed), force=True))
# robust numeric comparison as well
worst = 0.0
for vals in ({b2: 0.5, sg0: 0.3, pp0: 0.1, R0: 1.0}, {b2: 0.2, sg0: 1.1, pp0: 0.4, R0: 2.0}, {b2: -0.4, sg0: 0.7, pp0: 0.2, R0: 1.0}):
    for Rv in (0.5, 1.3, 3.0, 11.0):
        v = {**vals, R: Rv}
        worst = max(worst, abs(float(gen.rhs.subs(v)) - float(closed.subs(v))))
rec("4a dsolve(linear EOS) == wall.py closed form sigma(R)", worst < 1e-12, "max abs diff %.1e; symbolic diff %s" % (worst, d))
rec("4b closed form satisfies the ODE symbolically",
    sp.simplify(sp.diff(closed, R) + 2 / R * (closed + pp0 + b2 * (closed - sg0))) == 0)
worst = 0.0
for x in (0.1, 0.3, 0.7):
    for bb in (0.0, 0.2, 0.5, 1.0, -0.5):
        ss, mm, S0, P0 = wall.statics(x, 1.0)
        for Rv in (0.6, 1.0, 2.5, 9.0):
            want = float(closed.subs({b2: bb, sg0: S0, pp0: P0, R0: 1.0, R: Rv}))
            worst = max(worst, abs(wall.sigma_of_R(Rv, x, bb) - want) / abs(want))
rec("4c wall.sigma_of_R numerically equals the sympy closed form", worst < 1e-12, "max rel %.1e" % worst)
deg = sp.dsolve(ode.subs(b2, -1), sigf(R), ics={sigf(R0): sg0})
rec("4d beta^2 = -1 (A = 0) is logarithmic, excluded by the closed form (division by A)",
    sp.simplify(sp.expand_log(deg.rhs - (sg0 - 2 * (pp0 + sg0) * sp.log(R / R0)), force=True)) == 0, deg.rhs)
try:
    wall.sigma_of_R(2.0, 0.3, -1.0); z = "no exception"
except ZeroDivisionError:
    z = "ZeroDivisionError"
rec("4e wall.sigma_of_R at beta^2 = -1 raises (never called there by wall.py; b2 >= 0 in all its uses)", z == "ZeroDivisionError", z)

# --- 5 ------------------------------------------------------------------------
# Outgoing Vaidya exterior ds^2 = -f(u,r) du^2 - 2 du dr + r^2 dOmega^2, f = 1 - 2 M(u)/r; Minkowski inside.
# Shell r = R(tau), u = U(tau): f Udot^2 + 2 Udot Rdot = 1 -> Udot = (-Rdot + sqrt(Rdot^2 + f))/f.
# K^theta_theta(out) = (1/R) * n^r with n^r = sqrt(f + Rdot^2) (same form, but M now depends on u).
# Then sigma = -(1/4piR)[sqrt(f_out+Rdot^2) - sqrt(1+Rdot^2)], i.e. m_s(R, Rdot, M(u)).
# The Israel identity for K^theta_theta alone gives the Hamiltonian constraint; differentiate along the shell:
Mu, dM = sp.symbols("M_u dMdu", real=True)
f_out_v = 1 - 2 * Mu / R
sig_v = -(sp.sqrt(f_out_v + Rd**2) - sp.sqrt(1 + Rd**2)) / (4 * pi * R)
Udot = (-Rd + sp.sqrt(Rd**2 + f_out_v)) / f_out_v
# p from the angular-angular/tau-tau Israel equation; for Vaidya K^tau_tau(out) picks up a dM/du term.
# Rather than re-deriving K_tautau for Vaidya, use the Hamiltonian constraint (exact) and the momentum constraint
# (Israel): d(sigma A)/dtau + p dA/dtau = -A [T_ab u^a n^b]; with Vaidya T_uu = (dM/du)/(4 pi r^2) (outgoing null
# dust, radiated mass loss dM/du < 0).  T_ab u^a n^b = T_uu Udot n^u.  For outgoing Vaidya n_a = (-Rdot, Udot, 0,0)
# up to orientation, n^u = -Udot (from g^{ur} = -1, g^{rr} = f).  So the flux term is  -A * T_uu * Udot * (-Udot):
flux = -A * (dM / (4 * pi * R**2)) * Udot * (-Udot)
# Hamiltonian-constraint route: take d/dtau of sigma A at fixed functional form, including dM/dtau = dM * Udot.
dsA = sp.diff(sig_v * A, R) * Rd + sp.diff(sig_v * A, Rd) * Rdd + sp.diff(sig_v * A, Mu) * dM * Udot
# The part of dsA proportional to dM is the flux contribution the vacuum law omits:
flux_part = sp.simplify(sp.diff(dsA, dM) * dM)
rec("5a INDICATION ONLY: with a radiating (Vaidya) exterior, d(sigma A)/dtau acquires a term prop. to dM/du absent from the vacuum derivation; p (via K_tautau) is NOT recomputed for Vaidya here, so this does not by itself compute the flux law -- the READ statement is Ishak-Lake eqs (6),(12)",
    sp.simplify(flux_part) != 0, sp.simplify(flux_part))
# at the static instant Rdot=0 the extra term is -(dM Udot)/sqrt(f) != 0 whenever dM/du != 0
fp0 = sp.simplify(flux_part.subs(Rd, 0))
rec("5b at Rdot = 0 the flux term is dM/du * Udot / sqrt(f) * (-1): vanishes iff dM/du = 0",
    sp.simplify(fp0 + dM * Udot.subs(Rd, 0) / sp.sqrt(f_out_v)) == 0 or sp.simplify(fp0 - dM * Udot.subs(Rd, 0) / sp.sqrt(f_out_v)) == 0, fp0)

# --- 6 ------------------------------------------------------------------------
s = sp.symbols("s", positive=True)
Rs = sp.Symbol("Rs", positive=True)
lim = sp.limit((closed - (pp0 + b2 * (closed - sg0))).subs({R0: 1}).subs(R, Rs), Rs, sp.oo) if False else None
# asymptote by hand: for A > 0, sigma -> -K/A; sigma - p -> -K/A - p0 - b2(-K/A - sg0)
asym = sp.simplify(-K / Aa - pp0 - b2 * (-K / Aa - sg0))
rec("6a dec asymptote sigma-p -> 2(b2 sigma0 - p0)/(1+b2) (A > 0)", sp.simplify(asym - 2 * (b2 * sg0 - pp0) / (1 + b2)) == 0, asym)
# sigma + p along the curve = A*C*R^{-2A} with C = (sigma0+p0)/A > 0 -> monotone margin, no crossing before the limit
spp = sp.simplify(closed + pp0 + b2 * (closed - sg0))
rec("6b sigma+p along the curve = (sigma0+p0)(R/R0)^(-2A) (never changes sign)",
    sp.simplify(spp - (sg0 + pp0) * (R / R0)**(-2 * Aa)) == 0, spp)
xs = 1 - s**2
b2c = (1 - s) * (3 * s**2 + 2 * s + 1) / (4 * s**2 * (1 + 3 * s))
gap = sp.simplify(b2c - (1 - s) / (4 * s) - xs / (4 * s**2 * (1 + 3 * s)))
rec("6c gap identity beta2_crit - p0/sigma0 = x/(4 s^2 (1+3s)) symbolic", gap == 0, gap)
try:
    import z3
    zs = z3.Real("s")
    zg = (1 - zs) * (3 * zs * zs + 2 * zs + 1) - (1 - zs) * zs * (1 + 3 * zs)  # numerator over 4 s^2 (1+3s) > 0
    sol_ = z3.Solver(); sol_.add(zs > 0, zs < 1, zg <= 0)
    r = sol_.check()
    rec("6d z3: gap numerator > 0 for every s in (0,1) (unsat of negation)", r == z3.unsat, r)
except ImportError:
    rec("6d z3 not available", False)

# --- 7 ------------------------------------------------------------------------
def rk4_sigma(R_end, x, bb, n=4000):
    _, _, S0, P0 = wall.statics(x, 1.0)
    f = lambda r, sg: -2.0 / r * (sg + P0 + bb * (sg - S0))
    h = (R_end - 1.0) / n; r, sg = 1.0, S0
    for _ in range(n):
        k1 = f(r, sg); k2 = f(r + h / 2, sg + h * k1 / 2); k3 = f(r + h / 2, sg + h * k2 / 2); k4 = f(r + h, sg + h * k3)
        sg += h * (k1 + 2 * k2 + 2 * k3 + k4) / 6; r += h
    return sg
worst = 0.0
for x, bb in ((0.3, 0.5), (0.5, 0.5), (0.3, 0.2)):
    for Re in (0.7, 1.5, 4.0):
        worst = max(worst, abs(rk4_sigma(Re, x, bb) - wall.sigma_of_R(Re, x, bb)) / abs(wall.sigma_of_R(Re, x, bb)))
rec("7a RK4 sigma(R) vs closed form, three wall.py points", worst < 1e-10, "max rel %.1e" % worst)

# period through an RK4-sigma potential (independent of the closed form) -- small-amplitude orbit
def V_rk4(Rv, x, bb):
    _, m, _, _ = wall.statics(x, 1.0)
    ms = 4 * math.pi * Rv * Rv * rk4_sigma(Rv, x, bb, n=400)
    return 1.0 - (ms / (2 * Rv) + m / ms)**2
def period_from(Vfun, x, bb, eps=1e-4, dt=2e-4, tmax=80.0):
    h = 1e-6
    dV = lambda r: (Vfun(r + h, x, bb) - Vfun(r - h, x, bb)) / (2 * h)
    # velocity Verlet on R'' = -V'/2
    r, v, t, prev, cross = 1.0 + eps, 0.0, 0.0, 1.0 + eps, []
    a = -0.5 * dV(r)
    while t < tmax and len(cross) < 3:
        r += v * dt + 0.5 * a * dt * dt
        an = -0.5 * dV(r); v += 0.5 * (a + an) * dt; a = an; t += dt
        if (prev - 1.0) * (r - 1.0) < 0.0:
            # linear interpolation of the crossing
            cross.append(t - dt * (r - 1.0) / (r - prev))
        prev = r
    return 2.0 * (cross[2] - cross[1]) if len(cross) > 2 else float("nan")
rows = []
okall = True
for x, bb in ((0.3, 0.5), (0.5, 0.5), (0.3, 0.2)):
    Tan = wall.period_scaled(x, bb)
    Tcf = period_from(wall.V_of_R, x, bb)
    Trk = period_from(V_rk4, x, bb)
    rows.append((x, bb, Tan, Tcf, Trk, abs(Tcf - Tan) / Tan, abs(Trk - Tan) / Tan))
    okall &= abs(Trk - Tcf) / Tan < 1e-4 and abs(Tcf - Tan) / Tan < 1e-3
rec("7b period: analytic 2pi/sqrt(V''/2) vs closed-form-V orbit vs RK4-sigma-V orbit", okall,
    "; ".join("(%.1f,%.1f) T=%.6f cf=%.6f rk=%.6f rel %.1e/%.1e" % r_ for r_ in rows))

# --- 8 ------------------------------------------------------------------------
# p(sigma) = p0 + b2 (sigma - sigma0) + c (sigma - sigma0)^2 has dp/dsigma = b2 at sigma0 (same V''(R0)).
x, bb, c = 0.3, 0.5, 400.0
_, mm, S0, P0 = wall.statics(x, 1.0)
pnl = lambda sg: P0 + bb * (sg - S0) + c * (sg - S0)**2
def rk4_nl(R_end, n=20000):
    f = lambda r, sg: -2.0 / r * (sg + pnl(sg))
    h = (R_end - 1.0) / n; r, sg = 1.0, S0
    out = []
    for i in range(n):
        k1 = f(r, sg); k2 = f(r + h / 2, sg + h * k1 / 2); k3 = f(r + h / 2, sg + h * k2 / 2); k4 = f(r + h, sg + h * k3)
        sg += h * (k1 + 2 * k2 + 2 * k3 + k4) / 6; r += h
        out.append((r, sg, sg - pnl(sg), sg + pnl(sg)))
        if sg - pnl(sg) < 0:
            break
    return out
tr = rk4_nl(3.0)
cross = next((r for r, sg, mrg, spp_ in tr if mrg < 0), None)
spp_min = min(q[3] for q in tr)
stable_same = wall.is_stable(x, bb)
lin_basin = wall.basin_unbounded(x, bb)
rec("8a scope: nonlinear EOS, same beta^2(sigma0)=0.5 (stable, linear basin unbounded) -> dec margin crosses 0 at finite R",
    stable_same and lin_basin and cross is not None,
    "x=0.3, c=%.0f: sigma-p < 0 first at R/R0 = %s (sigma+p stays > 0, min %.3g, so the curve is regular there); linear-EOS asymptote %.4g > 0" % (c, "%.4f" % cross if cross else None, spp_min, wall.dec_asymptotic_margin(x, bb)))

nf = sum(1 for v in res.values() if not v["ok"])
print("\n%d checks, %d failed" % (len(res), nf))
json.dump(res, open(__file__.replace(".py", ".out.json"), "w"), indent=1)
sys.exit(1 if nf else 0)
