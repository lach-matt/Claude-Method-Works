#!/usr/bin/env python3
"""
DOCKET 67 -- re-derivation of address.py section 9, "THE DOMINATION THEOREM",
as used by excite.py:52-54, 173-174, 1560-1577.

Reads research/warp-drive READ-ONLY (sys.dont_write_bytecode, no file written
there).  Every check prints PASS/FAIL/FINDING; exit 0 unless an arithmetic
check of the tree's own numbers fails.

  C1  linear response: eps = -rho_H c^2/(m_h^2 v^2) and m_h^2 v^2 = 8|V_min|
      for V = (lam/4)(phi^2 - v^2)^2  (sympy)
  C2  the sharp-edge (planar) exterior amplitude is eps0/2, not eps0 (sympy);
      address.higgs_range/detection_standoff start the tail at eps0
  C3  R(rho) = A sqrt(rho)/ln(B rho): limit oo; dR/drho has the sign of
      ln(B rho) - 2, so R DECREASES for eps0/eps_det in (1, e^2)  (sympy),
      and a continuum counterexample with address.domination_ratio itself
  C4  independent recomputation of excite.py's scan (rho = 1e12..1e22, R = 1 m,
      H1, S = 0.06, eps_det = 1e-18): min ratio > 1e20, monotone from 1e14
  C5  sensitivity: m_h (125.13 tree / 125.11 ATLAS 2308.04775 / 125.20 old pin),
      S (0.0096 .. 0.106), gravimeter floor (1e-11 .. 1e-6), eps_det
      (2.86e-24 .. 1e-15), f under H2
  C6  domain: at fixed R = 1 m the formula's rho -> oo leaves the weak field
      (2GM/Rc^2 = 1 at rho ~ 1.6e26) before eps ~ 1 (rho ~ 1e29)
  C7  point sources: Yukawa (linear) range vs Newton range for m_e, m_p and
      the crossover mass
  C8  Shi, arXiv:2107.04206 (real-scalar, FIXED-source toy): the 1010-1210
      boundary M_c ~ 2.7e14 a^2 kg with valence coupling, rescaled to the
      tree's f; and gravity-vs-light-horizon on that contested branch
"""
import math
import os
import sys

sys.dont_write_bytecode = True
TREE = "/home/user/Claude-Method-Works/research/warp-drive"
sys.path.insert(0, TREE)
import sympy as sp  # noqa: E402

import address  # noqa: E402
import higgs  # noqa: E402

FAIL = []


def rep(ok, msg):
    print("%-8s %s" % ("NOTE" if ok is None else ("PASS" if ok else "FAIL"), msg))
    if ok is False:
        FAIL.append(msg)


# --------------------------------------------------------------------- C1
print("C1  linear response of the Higgs to a scalar source")
phi, v, lam, J = sp.symbols("phi v lam J", positive=True)
V = lam / 4 * (phi ** 2 - v ** 2) ** 2
Vmin = sp.Abs(V.subs(phi, 0) - V.subs(phi, v))       # depth |V(0)-V(v)| = lam v^4/4
mh2 = sp.diff(V, phi, 2).subs(phi, v)                 # 2 lam v^2
rep(sp.simplify(mh2 * v ** 2 - 8 * Vmin) == 0,
    "m_h^2 v^2 = 8|V_min| for the SM quartic: %s vs %s" % (sp.factor(mh2 * v ** 2), sp.factor(8 * Vmin)))
# source term +J*phi (J = rho_H c^2 / v): linearise V'(v+d) + J = 0
d = sp.symbols("d")
lin = sp.series(sp.diff(V, phi).subs(phi, v + d), d, 0, 2).removeO() + J
dsol = sp.solve(sp.Eq(lin, 0), d)[0]
rep(sp.simplify(dsol / v + J / (v * mh2)) == 0,
    "eps = d/v = -J/(v m_h^2) = -rho_H c^2/(m_h^2 v^2) = -rho_H c^2/(8|V_min|)")
rep(None, "NOTE: only the curvature m_h^2 = V''(v) enters; the trilinear/quartic "
    "(kappa_lambda, unmeasured to O(1)) does not, in the linear regime")

# --------------------------------------------------------------------- C2
print("\nC2  sharp-edge exterior amplitude (planar, R >> lambda_h)")
x, L, e0 = sp.symbols("x L e0", positive=True)
A1, B1 = sp.symbols("A1 B1")
inside = e0 + A1 * sp.exp(x / L)          # x < 0 : source region, regular at -oo
outside = B1 * sp.exp(-x / L)             # x > 0 : decays
sol = sp.solve([sp.Eq(inside.subs(x, 0), outside.subs(x, 0)),
                sp.Eq(sp.diff(inside, x).subs(x, 0), sp.diff(outside, x).subs(x, 0))], [A1, B1])
rep(sp.simplify(sol[B1] - e0 / 2) == 0,
    "(d^2/dx^2 - 1/L^2) eps = -(eps0/L^2) H(-x)  =>  exterior eps = (eps0/2) e^{-x/L}")
lam_h = address.yukawa_range()
fH1 = address.higgs_fraction(0.06, "H1")
e18 = 1e-18
eps_at = lambda rho, f=fH1: abs(address.eps_from_matter(rho, f))  # noqa: E731
rho_t = e18 / eps_at(1.0)                  # threshold density eps0 = eps_det
rep(None, "address threshold (eps0 = eps_det = 1e-18, H1, S=0.06): %.4e kg/m^3; "
    "with the edge factor 1/2 the threshold is %.4e" % (rho_t, 2 * rho_t))
rep(None, "FINDING (discrepancy, conservative for the theorem): address.higgs_range "
    "overstates d by lambda_h ln 2 = %.3e m; at rho = 1e12 the true edge amplitude "
    "%.3e < eps_det, so the Higgs range there is 0, not %.3e m"
    % (lam_h * math.log(2), eps_at(1e12) / 2, address.higgs_range(1e12, fH1, e18)))

# --------------------------------------------------------------------- C3
print("\nC3  the functional claim sqrt(rho) against ln(rho)")
r, A, B = sp.symbols("rho A B", positive=True)
Rf = A * sp.sqrt(r) / sp.log(B * r)
rep(sp.limit(Rf, r, sp.oo) == sp.oo, "lim_{rho->oo} A sqrt(rho)/ln(B rho) = oo")
dR = sp.simplify(sp.diff(Rf, r))
num = sp.simplify(dR * 2 * r * sp.log(B * r) ** 2 / (A * sp.sqrt(r)))
rep(sp.simplify(num - (sp.log(B * r) - 2)) == 0,
    "dR/drho = A (ln(B rho) - 2) / (2 sqrt(rho) ln^2(B rho))  -> minimum at eps0/eps_det = e^2")
# continuum counterexample with the tree's own function
r1, r2 = 1.2 * rho_t, 3.0 * rho_t           # both inside (1, e^2) x threshold
D1 = address.domination_ratio(r1, 1.0, fH1, e18)
D2 = address.domination_ratio(r2, 1.0, fH1, e18)
rep(None, "FINDING: address.domination_ratio(%.3e) = %.4e  >  (%.3e) = %.4e : "
    "the source GREW by 2.5x and r/d FELL -- contradicts address.py:316-317 "
    "'EVERY INCREASE IN THE SOURCE WIDENS IT' and :320 'it is monotone', on "
    "eps_det < eps0 < e^2 eps_det (rho %.3e .. %.3e)"
    % (r1, D1, r2, D2, rho_t, math.e ** 2 * rho_t))
rep(D1 > D2, "the counterexample is real (computed with address.domination_ratio)")
rhos = [rho_t * k for k in (1.01, 1.5, 2, 4, 7.389, 8, 20, 100, 1e3)]
dr = [address.domination_ratio(q, 1.0, fH1, e18) for q in rhos]
imin = min(range(len(dr)), key=lambda i: dr[i])
rep(abs(rhos[imin] / rho_t - math.e ** 2) < 1.0,
    "sampled minimum of r/d sits at eps0/eps_det = %.3f (e^2 = 7.389)" % (rhos[imin] / rho_t))
rep(None, "excite.py:1563-1569 already RECORDS this regime ('just above threshold "
    "... d -> 0 there', check dom[0] > dom[1]); address.py section 9 prose does not")

# --------------------------------------------------------------------- C4
print("\nC4  independent recomputation of excite.py's scan")
G, c, hbar = higgs.G, higgs.c, higgs.HBAR
GEV = 1.602176634e-10
mh, vv = higgs.M_HIGGS, higgs.vev()


def indep_ratio(rho, R=1.0, f=fH1, eps_det=e18, mh_gev=mh, floor=1e-9):
    lamh = hbar * c / (mh_gev * GEV)
    mh2v2 = (mh_gev * GEV) ** 2 * (vv * GEV) ** 2 / (hbar * c) ** 3   # J/m^3 (= 8|Vmin|)
    eps0 = rho * f * c ** 2 / mh2v2
    if eps0 <= eps_det:
        return float("inf"), 0.0, eps0
    dd = lamh * math.log(eps0 / eps_det)
    rn = math.sqrt(G * rho * 4 / 3 * math.pi * R ** 3 / floor)
    return rn / dd, dd, eps0


mh2v2 = (mh * GEV) ** 2 * (vv * GEV) ** 2 / (hbar * c) ** 3
rep(abs(mh2v2 / (8 * address.VMIN_SI) - 1) < 1e-9,
    "independent m_h^2 v^2/(hbar c)^3 = %.6e J/m^3 vs tree 8|V_min| = %.6e" % (mh2v2, 8 * address.VMIN_SI))
scan = (1e12, 1e14, 1e16, 1e18, 1e20, 1e22)
ind = [indep_ratio(q)[0] for q in scan]
tre = [address.domination_ratio(q, 1.0, fH1, e18) for q in scan]
for q, a_, b_ in zip(scan, ind, tre):
    print("         rho %.0e  indep r/d %.4e  tree %.4e" % (q, a_, b_))
rep(all(abs(a_ / b_ - 1) < 1e-9 for a_, b_ in zip(ind, tre)), "independent = tree to 1e-9")
rep(min(ind) > 1e20, "min r/d over excite's scan = %.3e > 1e20" % min(ind))
rep(all(b_ > a_ for a_, b_ in zip(ind[1:], ind[2:])), "monotone increasing from 1e14 (excite's claim)")
rep(ind[0] > ind[1], "and dom[0] > dom[1] (near-threshold regime, excite's claim)")

# --------------------------------------------------------------------- C5
print("\nC5  sensitivity of the conclusion to every datum")
worst = []
for mhv in (125.11, 125.13, 125.20):
    for S in (0.009581, 0.043, 0.06, 0.09, 0.106):
        for hyp in ("H1", "H2"):
            f = float(address.dln_mp_dln_v(S, hyp))
            for floor in (1e-11, 1e-9, 1e-6):
                for ed in (2.86e-24, 1e-18, 1e-15):
                    vals = [indep_ratio(q, f=f, eps_det=ed, mh_gev=mhv, floor=floor)[0] for q in scan]
                    worst.append((min(vals), mhv, S, hyp, floor, ed))
worst.sort()
w = worst[0]
rep(w[0] > 1e17, "worst case over m_h x S x {H1,H2} x floor x eps_det: min r/d = %.3e "
    "(m_h %.2f, S %.4f, %s, floor %.0e, eps_det %.2e) -- conclusion unmoved" % w)
print("         m_h 125.13 -> 125.11 moves lambda_h by %.2e (fractional)" % (125.13 / 125.11 - 1))

# --------------------------------------------------------------------- C6
print("\nC6  domain of 'grows without bound' at fixed R = 1 m")
rho_bh = 3 * c ** 2 / (8 * math.pi * G * 1.0 ** 2)
rho_eps1 = 1.0 / eps_at(1.0)
rep(None, "2GM/(Rc^2) = 1 at rho = %.3e kg/m^3; eps = 1 at rho = %.3e; scan max 1e22 has "
    "2GM/Rc^2 = %.2e" % (rho_bh, rho_eps1, 2 * G * 1e22 * 4 / 3 * math.pi / c ** 2))
rb = indep_ratio(rho_bh)[0]
rep(rb > 1e20, "at the collapse density itself r/d = %.3e: the verdict holds on the whole "
    "physical domain; 'without bound' is a statement about the formula only" % rb)

# --------------------------------------------------------------------- C7
print("\nC7  point sources (linear Yukawa tail vs Newton), floor 1e-9, eps_det 2.86e-24")
vJ = vv * GEV


def yukawa_range_point(M, f, eps_det):
    # eps(r) = f M c^2 (hbar c) e^{-r/lam} / (4 pi r v^2), solve eps = eps_det by iteration
    lamh = hbar * c / (mh * GEV)
    K = f * M * c ** 2 * hbar * c / (4 * math.pi * vJ ** 2)
    rr = lamh
    for _ in range(500):
        arg = K / (rr * eps_det)
        if arg <= 1:
            return 0.0
        new = lamh * math.log(arg)
        if abs(new - rr) < 1e-15 * new:
            break
        rr = new
    return rr


for name, M, f in (("electron", 9.1093837e-31, 1.0), ("proton", 1.67262192e-27, fH1)):
    ry = yukawa_range_point(M, f, 2.86e-24)
    rnw = math.sqrt(G * M / 1e-9)
    rep(rnw > ry, "%-8s Yukawa range %.3e m, Newton range %.3e m, ratio %.1f"
        % (name, ry, rnw, rnw / ry))
lo, hi = 1e-40, 1e-27
for _ in range(200):
    mid = math.sqrt(lo * hi)
    if math.sqrt(G * mid / 1e-9) > yukawa_range_point(mid, 1.0, 2.86e-24):
        hi = mid
    else:
        lo = mid
rep(None, "crossover (f = 1): Newton range = Yukawa range at M = %.2e kg (%.2e m_e) -- "
    "no source at or above one electron mass is out-read by the Higgs in this model" % (hi, hi / 9.1093837e-31))

# --------------------------------------------------------------------- C8
print("\nC8  Shi arXiv:2107.04206 (contested for the SM: real Z2 scalar, source held FIXED)")
f_val = 3 * 3.45 / 938.27                # Shi p.15: N = 3M/m_p, m_f = 3.45 MeV
scale = fH1 / f_val
Mc_val = 2.7e14                          # kg per a_m^2, Shi p.15
Mc_tree = Mc_val / scale
rep(None, "Shi's valence coupling f = %.4f vs the tree's SVZ/H1 f = %.4f (x%.1f)" % (f_val, fH1, scale))
rep(None, "1010->1210 boundary for a = 1 m: M_c = %.2e kg (Shi) -> %.2e kg with the tree's f; "
    "as a uniform 1 m sphere that is rho = %.2e / %.2e kg/m^3 -- inside excite's scan"
    % (Mc_val, Mc_tree, Mc_val / (4 / 3 * math.pi), Mc_tree / (4 / 3 * math.pi)))
# light-horizon radius on the contested branch, Shi p.2: rho_c ~ R sqrt(ln(3 R S0/(D-1))), D = 3
for rho in (1e14, 1e16, 1e18, 1e22):
    M = rho * 4 / 3 * math.pi
    Rnd = 1.0 / lam_h
    Anorm = 1.3e22 * M * scale           # Shi p.15, A ~ 1.3e22 M_kg, rescaled to the tree's f
    S0 = Anorm / (Rnd ** 3 * math.pi ** 1.5)
    arg = 3 * Rnd * S0 / 2
    if arg <= 1:
        print("         rho %.0e: below the asymptotic light-horizon condition" % rho)
        continue
    rc = 1.0 * math.sqrt(math.log(arg))
    rn = math.sqrt(G * M / 1e-9)
    print("         rho %.0e: light-horizon radius ~ %.2f m (source scale 1 m); Newton range %.2e m; ratio %.1e"
          % (rho, rc, rn, rn / rc))
rep(None, "ORDER-OF-MAGNITUDE only (Gaussian vs uniform sphere, asymptotic formula): even on "
    "Shi's contested non-perturbative branch gravity still out-reads the Higgs, by ~1e6-1e10 rather "
    "than >1e20, and the Higgs reach there scales as R sqrt(ln), not lambda_h ln rho")

print("\nRESULT: %s" % ("ALL ARITHMETIC CHECKS PASS" if not FAIL else "FAILURES: %r" % FAIL))
sys.exit(1 if FAIL else 0)
