#!/usr/bin/env python3
"""Refute pass: exact checks of the synthesis' flat-plane, control, motion, clause-(B)-reading and k=-1 claims.

Junction (derived independently from the energy equation of a moving shell; per-sheet, normals into kept sides):
  sum_j eps_j sqrt(f_j(R) + X) = lam R,   X = Rdot^2 (proper time);   static iff X = 0 and dX/dR = 0.
"""
import sympy as sp
import mpmath as mp

R, mu, mus, muo, l, ls, l1, l2, X, lam, w = sp.symbols("R mu mu_s mu_o ell ell_s ell_1 ell_2 X lam w", positive=True)
k = sp.Symbol("k")
out = []


def say(*a):
    print(*a)


f = lambda kk, L, m: kk + R**2 / L**2 - m / R**2

# 1. Balance from the energy equation (static: dX/dR = 0 at X = 0) for a general two-sided plane
e1, e2 = sp.symbols("e1 e2")
F = e1 * sp.sqrt(f(k, ls, mus) + X) + e2 * sp.sqrt(f(k, l2, muo) + X) - lam * R
# implicit dX/dR = -F_R/F_X at X = 0 ; static iff F_R = 0 with lam from F = 0
lam_static = sp.solve(F.subs(X, 0), lam)[0]
FR = sp.diff(F, R).subs(X, 0).subs(lam, lam_static)
B_expected = (e1 * (k - 2 * mus / R**2) / sp.sqrt(f(k, ls, mus)) + e2 * (k - 2 * muo / R**2) / sp.sqrt(f(k, l2, muo))) / R
say("1. dF/dR|static * R  ==  R * sum eps (k - 2mu/R^2)/sqrt(f) / R ?",
    sp.simplify(FR * R - B_expected * R * sp.Rational(1, 1) - 0) == 0 or sp.simplify(sp.expand(FR - B_expected)))

# 2. flat k=0, outer massless: B per bridge side and the control
Bside = (-2 * mu / R**2) / sp.sqrt(f(0, l, mu))
target = -2 * mu * l / (R * sp.sqrt(R**4 - l**2 * mu))
say("2a. k=0 per-bridge-side B equals -2 mu ell/(R sqrt(R^4 - ell^2 mu)):",
    sp.simplify(Bside - target).equals(0))
say("2b. control mu=0: B identically", sp.simplify(Bside.subs(mu, 0)), "; tension lam = sum eps/ell_j, independent of R:",
    sp.simplify((sp.sqrt(f(0, ls, 0)) + sp.sqrt(f(0, l1, 0))) / R))

# 3. motion of a mirrored flat plane: 2 sqrt(f + Rdot^2) = lam R
Xexpr = (lam * R / 2)**2 - f(0, l, mu)          # Rdot^2
Xrs = sp.simplify(Xexpr.subs(lam, 2 / l))
acc = sp.simplify(sp.diff(Xexpr, R) / 2)          # R'' = (1/2) dX/dR along the motion
say("3a. at RS (lam = 2/ell): Rdot^2 =", Xrs, " (never zero for mu > 0: never at rest)")
say("3b. at RS: R'' =", sp.simplify(acc.subs(lam, 2 / l)), "   <-- synthesis says -2 mu/R^3")
lam_rest = sp.solve(sp.Eq(Xexpr, 0), lam)
lr = [s for s in lam_rest if s.is_positive is not False][0]
say("3c. momentarily at rest (lam^2/4 = 1/ell^2 - mu/R^4, sub-critical): R'' =", sp.simplify(acc.subs(lam, lr)))

# 4. clause (B) read as the CRITICAL tension of ours' actual two sides (the reading under which the corridor-free flat
#    control passes): ours two-sided, bridge (ell_s free) decaying + own bulk ell_1 = 1 decaying, k = 1.
#    lam1 = 1/ell_s + 1;  tension s + t = lam1 R;  balance => mu = lam1 R^3 / (2 t); then f_s = s^2 must hold.
v = sp.Symbol("v", positive=True)                  # v = 1/ell_s
t = sp.sqrt(1 + R**2)
lam1 = v + 1
s = lam1 * R - t
mu1 = lam1 * R**3 / (2 * t)
cond = sp.simplify((1 + v**2 * R**2 - mu1 / R**2) - s**2)
say("4a. critical reading, k=1: f_s - s^2 =", sp.factor(cond))
sol = sp.solve(sp.Eq(sp.factor(cond) / ((v + 1) * R), 0), R)
say("    its zeros in R > 0:", sol, " -> ours has NO static position for ANY ell_s (Model C F2 holds with ell_s free)")
# check via the reduced identity 4 R t - 4 t^2 + 1 = 0  <=>  16R^2 = 9 + 24R^2
say("    reduced: 16 R^2 (1+R^2) - (3+4R^2)^2 =", sp.expand(16 * R**2 * (1 + R**2) - (3 + 4 * R**2)**2))

# 5. the three form-equalities: corridor-free flat control with the SAME tensions and ells
mp.mp.dps = 30
cases = {"(a) -1/8, ell_2=4/3": (mp.mpf("2.11473369241"), mp.mpf(-1) / 8, mp.mpf(4) / 3),
         "(b) -1/4, ell_2=1": (mp.mpf("2.31786300534"), mp.mpf(-1) / 4, mp.mpf(1)),
         "(c) -1/8, ell_2=1": (mp.mpf("1.34322964955"), mp.mpf(-1) / 8, mp.mpf(1))}
for name, (Ls, r, c) in cases.items():
    lam1v = mp.mpf(2)
    crit1 = 1 / Ls + 1
    lam2v = r * lam1v
    crit2 = 1 / Ls - 1 / c
    say("5. %s: ours lam1 = 2 vs flat-balance value %s (super-critical by %s%%); position 2 lam2 = %s vs %s"
        % (name, mp.nstr(crit1, 8), mp.nstr(100 * (lam1v / crit1 - 1), 4), mp.nstr(lam2v, 6), mp.nstr(crit2, 8)))
    say("   -> with mu = 0 (no corridor) neither plane balances anywhere at these tensions: M's flat control FAILS")
# can the flat control pass for both planes in Model C's orientation with M4's per-sheet pair at ours = 2/ell_1?
vs = sp.solve(sp.Eq(v + 1, 2), v)[0]
say("5x. control for ours at 2/ell_1 forces ell_s = ell_1; then position 2's flat value 1/ell_s - 3/4 =",
    vs - sp.Rational(3, 4), "(positive: wrong sign for 139)")

# 6. k = -1, two-exterior (Model C) with ell_s FREE: sign argument (F4)
#    ours outer growing: s - t = lam1 R > 0 and (-1 - 2mu/R^2)/s + 1/t = 0  ->  1 + 2mu/R^2 = s/t > 1  ->  mu > 0
#    position 2 outer growing, lam2 < 0: s < t and the same balance -> 1 + 2mu/R^2 = s/t < 1 -> mu < 0
#    ours outer decaying: (-1 - 2mu/R^2) t = -s ... -> -1 - 2mu/R^2 > 0 -> R^2 < -2mu ; horizons r_pm^2 = (1 pm sqrt(1+4w mu))/(2w)
xx = sp.Symbol("x", positive=True)                  # x = -4 w mu in (0,1)
rp2 = (1 + sp.sqrt(1 - xx)) / 2                     # times 1/w
rm2 = (1 - sp.sqrt(1 - xx)) / 2
say("6. k=-1 ours decaying outer needs R^2 < -2mu = x/(2w): outer horizon r_+^2 - x/(2w) =",
    sp.simplify(rp2 - xx / 2), "> 0 on (0,1), so R is inside r_+ (not in an exterior); horizonless if x > 1")
say("   F4 holds with ell_s free in Model C's orientation (deduced from the three sign lines above)")

# 7. the flat no-go needs the outer bulks massless: a k=0 static NEGATIVE-tension plane with a massive outer bulk
mp.mp.dps = 30
Rv, Lsv, musv, cv = mp.mpf(1), mp.mpf(1), mp.mpf("0.5"), mp.mpf("0.5")
sv = mp.sqrt(Rv**2 / Lsv**2 - musv / Rv**2)
g = lambda tt: tt**2 - (Rv**2 / cv**2 - musv * tt / sv / Rv**2)
tv = mp.findroot(g, 1.5)
muov = musv * tv / sv
Bv = (-2 * musv / Rv**2) / sv + (2 * muov / Rv**2) / tv      # bridge side decaying (+), outer growing (-)
say("7. k=0, bridge mu_s=0.5 (ell_s=1) decaying, outer ell_2=1/2 growing with its own mass mu_o=%s: B=%s, lam2=%s"
    % (mp.nstr(muov, 10), mp.nstr(Bv, 3), mp.nstr((sv - tv) / Rv, 10)))
say("   -> a static flat negative plane exists once the outer bulk carries mass: 'any tensions, any lengths' needs mu_o = 0")
