"""Independent re-derivation (check-throat-column), symbolic part.  Own code; no owner import.

Metric (units m = 1, e = 1/ell):  ds^2 = dy^2 + alpha(y)^2 gAdS2(L=2) + beta(y)^2 * 4 dOmega^2,
gAdS2 in static coords: -(1 + r^2/4) dt^2 + dr^2/(1 + r^2/4)  (Gaussian curvature -1/4).
A switch cA, cS scales the slice curvatures (cA = cS = 0 is flat slices: pure AdS5 control).
"""
import sympy as sp

t, r, y, th, ph = sp.symbols("t r y theta phi", real=True)
e, cA, cS, nu = sp.symbols("e c_A c_S nu", real=True)
al = sp.Function("alpha")(y)
be = sp.Function("beta")(y)
X = [t, r, y, th, ph]


def metric(cA_, cS_):
    # AdS2 of curvature -cA/4 written as -(1 + cA r^2/4)dt^2 + dr^2/(1 + cA r^2/4); S2: 4/cS-free form
    fA = 1 + cA_ * r**2 / 4
    # S2 of Gaussian curvature cS/4: 4 (dth^2 + s(th)^2 dph^2) with s = sin for cS=1, s = th for cS = 0
    # use general: s(th) = sin(sqrt(cS) th)/sqrt(cS) -> handle by series-safe symbolic: keep sin for cS=1 explicitly
    return fA


def ricci(g, X):
    n = len(X)
    ginv = g.inv()
    Gam = [[[sp.simplify(sum(ginv[a, d] * (sp.diff(g[d, b], X[c]) + sp.diff(g[d, c], X[b]) - sp.diff(g[b, c], X[d]))
                             for d in range(n)) / 2) for c in range(n)] for b in range(n)] for a in range(n)]
    R = sp.zeros(n, n)
    for b in range(n):
        for c in range(n):
            val = 0
            for a in range(n):
                val += sp.diff(Gam[a][b][c], X[a]) - sp.diff(Gam[a][b][a], X[c])
                for d in range(n):
                    val += Gam[a][a][d] * Gam[d][b][c] - Gam[a][c][d] * Gam[d][b][a]
            R[b, c] = sp.simplify(val)
    return R


def build(throat=True):
    if throat:
        fA = 1 + r**2 / 4
        s2 = sp.sin(th) ** 2
    else:
        fA = sp.Integer(1)
        s2 = th ** 2          # flat 2-plane in polar coords (Gaussian curvature 0)
    g = sp.diag(-al**2 * fA, al**2 / fA, 1, 4 * be**2, 4 * be**2 * s2)
    return g


out = {}
p, q = sp.symbols("p q", real=True)
pp, qp = sp.symbols("pprime qprime", real=True)
A, B = sp.symbols("A B", positive=True)
for name, throat in (("throat", True), ("flat-slices", False)):
    g = build(throat)
    R = ricci(g, X)
    ginv = g.inv()
    Rs = sp.simplify(sum(ginv[i, j] * R[i, j] for i in range(5) for j in range(5)))
    Lam = -6 * e**2
    # mixed Einstein tensor with Lambda: E^a_b = R^a_b - R/2 delta + Lam delta
    Emix = sp.simplify(ginv * R - Rs / 2 * sp.eye(5) + Lam * sp.eye(5))
    sub = {sp.Derivative(al, (y, 2)): (pp + p**2) * A, sp.Derivative(be, (y, 2)): (qp + q**2) * B,
           sp.Derivative(al, y): p * A, sp.Derivative(be, y): q * B}
    sub2 = {al: A, be: B}
    E = [sp.simplify(Emix[i, i].subs(sub).subs(sub2)) for i in range(5)]
    offd = [sp.simplify(Emix[i, j]) for i in range(5) for j in range(5) if i != j]
    # vacuum: E^a_b = 0.  Solve the slice components (t,t) and (th,th) for p', q'
    # trace-reversed vacuum equations: R^a_b = (2 Lam/3) delta^a_b = -4 e^2 delta^a_b (slice components)
    Rmix = sp.simplify(ginv * R)
    Rt = sp.simplify(Rmix[0, 0].subs(sub).subs(sub2)); Rth = sp.simplify(Rmix[3, 3].subs(sub).subs(sub2))
    sol = sp.solve([Rt + 4 * e**2, Rth + 4 * e**2], [pp, qp], dict=True)[0]
    Ryy = sp.simplify(Rmix[2, 2].subs(sub).subs(sub2))
    print("  R^y_y =", Ryy)
    cons = sp.simplify(E[2])
    out[name] = dict(pprime=sp.simplify(sol[pp]), qprime=sp.simplify(sol[qp]), constraint=sp.factor(cons),
                     rr_minus_tt=sp.simplify(E[1] - E[0]), phph_minus_thth=sp.simplify(E[4] - E[3]),
                     offdiag_zero=all(o == 0 for o in offd))
    print("==", name)
    for k, v in out[name].items():
        print("  ", k, ":", v)

# ---------------------------------------------------------------- E1 compared with the claimed system
pT, qT = out["throat"]["pprime"], out["throat"]["qprime"]
claim_p = 4 * e**2 - 2 * p * (p + q) - 1 / (4 * A**2)
claim_q = 4 * e**2 - 2 * q * (p + q) + 1 / (4 * B**2)
R4 = -1 / (2 * A**2) + 1 / (2 * B**2)
claim_c = p**2 + q**2 + 4 * p * q - 6 * e**2 - R4 / 2
print("E1 p' residual:", sp.simplify(pT - claim_p))
print("E1 q' residual:", sp.simplify(qT - claim_q))
# the constraint E^y_y = 0, compared up to a factor with the claimed one
ratio = sp.simplify(out["throat"]["constraint"] / claim_c)
print("E1 constraint ratio (must be a nonzero constant):", ratio)
print("flat-slice system p', q':", out["flat-slices"]["pprime"], "|", out["flat-slices"]["qprime"])

# ---------------------------------------------------------------- E2 / E4: D and a identities
a_, D_ = sp.symbols("a D", real=True)
S = 1 / (4 * A**2) + 1 / (4 * B**2)
Dp = sp.simplify((claim_q - claim_p) - (-4 * (p + q) / 2 * (q - p) + S))
print("E2 D' - (-4 a D + S):", Dp)
ap = (claim_p + claim_q) / 2
# on the constraint surface: eliminate R4 via constraint, express in a, D
ap_unc = sp.simplify(ap)
apc = sp.expand((ap + claim_c / 2).subs({p: a_ - D_ / 2, q: a_ + D_ / 2}))  # a' + (1/2) * constraint (=0 on shell)
print("E4 a' + constraint/2 - (e^2 - a^2 - D^2/4):", sp.simplify(apc - (e**2 - a_**2 - D_**2 / 4)))
# unconstrained form in a~ = a + e
at = sp.Symbol("at", real=True)
apu = sp.simplify(ap.subs({p: a_ - D_ / 2, q: a_ + D_ / 2}))
print("a' unconstrained:", sp.simplify(apu), " ; in a~:", sp.expand(apu.subs(a_, at - e)))

# variation of constants for D: D(y) = int_0^y S(t) exp(-4 int_t^y a) dt solves D' = -4 a D + S, D(0)=0
Sf, af = sp.Function("Sf"), sp.Function("af")
tt, ss = sp.symbols("t s", real=True)
Dint = sp.Integral(Sf(tt) * sp.exp(-4 * sp.Integral(af(ss), (ss, tt, y))), (tt, 0, y))
res = sp.simplify(sp.diff(Dint, y).doit() - (-4 * af(y) * Dint + Sf(y)))
print("E2 variation-of-constants residual:", sp.simplify(res.doit()))

# ---------------------------------------------------------------- E3 Gauss at umbilic surface
k = sp.Symbol("k", real=True)
R4s = sp.Symbol("R4", real=True)
gauss = sp.solve(sp.Eq(k**2 + k**2 + 4 * k**2 - 6 * e**2, R4s / 2), k**2)
print("E3 k^2 =", gauss)

# ---------------------------------------------------------------- Israel at a level surface (own derivation)
def israel_level(pv, qv, n_y, nu_):
    """K_ab = (1/2) n^y d_y h_ab for h = diag(-A^2 fA, A^2/fA, 4B^2, 4B^2 s^2): mixed K = n_y diag(p,p,q,q).
    Per-sheet: S^a_b = -nu (K^a_b - delta K)."""
    Kd = [n_y * pv, n_y * pv, n_y * qv, n_y * qv]
    trK = sum(Kd)
    Sd = [-nu_ * (kk - trK) for kk in Kd]
    return {"rho": sp.simplify(-Sd[0]), "p_r": sp.simplify(Sd[1]), "p_th": sp.simplify(Sd[2])}

# check K_ab = 1/2 n^y d_y h_ab gives mixed n_y diag(p,p,q,q) explicitly
h = sp.diag(-al**2 * (1 + r**2 / 4), al**2 / (1 + r**2 / 4), 4 * be**2, 4 * be**2 * sp.sin(th)**2)
Kmix = sp.simplify(h.inv() * sp.diff(h, y) / 2)
print("K^a_b (n = +d_y):", [sp.simplify(Kmix[i, i].subs({sp.Derivative(al, y): p * al, sp.Derivative(be, y): q * be})) for i in range(4)])

ours = israel_level(-e, -e, +1, nu)            # y = 0, slab at y > 0, normal into slab +d_y, p = q = -e
print("Our plane (mirrored, nu one-sided):", ours, " -> s1 = rho/(3 nu e) =", sp.simplify(ours["rho"] / (3 * nu * e)))
P2 = israel_level(p, q, -1, nu)                # y = y2, slab at y < y2, normal into slab -d_y
print("P2 mirrored level surface:", P2)
print("   rho + p_r =", sp.simplify(P2["rho"] + P2["p_r"]), " ; rho + p_th =", sp.simplify(P2["rho"] + P2["p_th"]))
print("   umbilic p=q=k: s2 = rho/(3 nu e) =", sp.simplify(P2["rho"].subs(q, p) / (3 * nu * e)))
# matter split at law s2: rho_m = rho - s2*3nu e, p_th,m = p_th + s2*3 nu e
s2s = sp.Symbol("s2", real=True)
rho_m = P2["rho"] - s2s * 3 * nu * e
pth_m = P2["p_th"] + s2s * 3 * nu * e
pr_m = P2["p_r"] + s2s * 3 * nu * e
print("   rho_m + p_r,m =", sp.simplify(rho_m + pr_m), " ; rho_m + p_th,m =", sp.factor(rho_m + pth_m))

# ---------------------------------------------------------------- E5 general far side
pf, qf, ef = sp.symbols("p_f q_f e_f", real=True)
kb = sp.Symbol("kbar", real=True)
# two-sided sheet, nu/2 per side; slab side normal -d_y: K = -diag(p,p,q,q); far side normal +d_y: K = diag(pf,pf,qf,qf)
Ks = [-p, -p, -q, -q]
Kf = [pf, pf, qf, qf]
Ssheet = [-(nu / 2) * (Ks[i] - sum(Ks)) - (nu / 2) * (Kf[i] - sum(Kf)) for i in range(4)]
traceless_cond = sp.simplify(Ssheet[0] - Ssheet[2])
print("E5 pure tension iff (S^t_t - S^th_th) = 0:", sp.factor(traceless_cond))
Spure = [sp.simplify(Si.subs({pf: p + 2 * kb, qf: q + 2 * kb})) for Si in Ssheet]
print("   with pf = p + 2kbar, qf = q + 2kbar: S =", Spure, " -> s2 = rho/(3 nu e) =", sp.simplify(-Spure[0] / (3 * nu * e)))
# far constraint: pf^2 + qf^2 + 4 pf qf - 6 ef^2 = R4/2 = p^2 + q^2 + 4pq - 6 e^2 (same induced metric)
fc = sp.expand((pf**2 + qf**2 + 4 * pf * qf - 6 * ef**2) - (p**2 + q**2 + 4 * p * q - 6 * e**2))
fc = sp.expand(fc.subs({pf: p + 2 * kb, qf: q + 2 * kb}).subs({p: a_ - D_ / 2, q: a_ + D_ / 2}))
print("   far constraint in (a, D, kbar):", sp.factor(fc))
kbs = sp.solve(fc, kb)
print("   kbar roots:", kbs)

# ---------------------------------------------------------------- conventions (exact), x = |a|/e >= 1
x = sp.Symbol("x", positive=True)
lam = sp.Symbol("lam", positive=True)  # ell/ell_f = e_f/e
s2_dec = -(1 - lam**2) / (2 * (x + sp.sqrt(x**2 - 1 + lam**2)))
s2_gro = -(x + sp.sqrt(x**2 - 1 + lam**2)) / 2
# check equals -kbar/e for the two roots
for kk in kbs:
    val = sp.simplify((-kk / e).subs(a_, -x * e).subs(ef, lam * e))
    print("   -kbar/e at a = -x e:", sp.simplify(val))
print("   decaying form check:", sp.simplify(s2_dec - (-(x - sp.sqrt(x**2 - 1 + lam**2)) / 2)))
convs = {"C-PRZ": (sp.Rational(-1, 4), sp.Rational(3, 4)), "C-SHEET-M4": (sp.Rational(-1, 8), sp.Rational(3, 4)),
         "C-S6": (sp.Rational(-1, 3), sp.Rational(1, 3)), "C-S7": (sp.Rational(-1, 6), sp.Rational(1, 6))}
for nm, (tgt, lm) in convs.items():
    dec = sp.simplify(s2_dec.subs(lam, lm))
    gro = sp.simplify(s2_gro.subs(lam, lm))
    dec_at1 = sp.simplify(dec.subs(x, 1))
    gro_at1 = sp.simplify(gro.subs(x, 1))
    lim_dec = sp.limit(dec, x, sp.oo)
    roots_dec = sp.solve(sp.Eq(dec, tgt), x)
    roots_gro = sp.solve(sp.Eq(gro, tgt), x)
    mono = sp.simplify(sp.diff(dec, x))
    print(f"{nm}: target {tgt}, ell_f = ell/{lm}: decaying s2(x=1) = {dec_at1}, ->{lim_dec} as x->oo, d/dx = {mono};"
          f" growing s2(x=1) = {gro_at1} (max); decaying roots x = {roots_dec}; growing roots x = {roots_gro}")
# mirror: s2 = ell * a = -x
print("C-MIRROR: s2 = -x <= -1 at every depth")

# ---------------------------------------------------------------- positive control: unequal radii alpha0=1, beta0=2
R4pc = -sp.Rational(1, 2) + sp.Rational(1, 2) / 4
k2 = e**2 + R4pc / 12
s1 = sp.Rational(1, 2)
esol = sp.solve(sp.Eq((s1 * e)**2, k2), e)
print("positive control R4 =", R4pc, "; e with s1 = 1/2:", esol, [sp.N(v, 15) for v in esol])
print("eq.(17) equal radii: (s1 e)^2 = e^2 ->", sp.solve(sp.Eq((s1 * e)**2, e**2), e), "for s1=1/2; s1 = +-1 identity")

# ---------------------------------------------------------------- E7 pure AdS control
ee = sp.Symbol("ee", positive=True)
yy = sp.Symbol("yy", real=True)
alpha = sp.exp(-ee * yy)
pA = sp.diff(alpha, yy) / alpha
fpp = out["flat-slices"]["pprime"]
resid = sp.simplify(sp.diff(pA, yy) - fpp.subs({p: pA, q: pA, e: ee, A: alpha, B: alpha}))
print("E7 pure AdS residual p':", resid, "; constraint:",
      sp.simplify(out["flat-slices"]["constraint"].subs({p: pA, q: pA, e: ee, A: alpha, B: alpha})))

# ---------------------------------------------------------------- Kasner exponents of the alpha -> 0 end
c1, c2 = sp.symbols("c1 c2", real=True)
ks = sp.solve([2 * c1 + 2 * c2 - 1, 2 * c1**2 + 2 * c2**2 - 1], [c1, c2], dict=True)
print("5D vacuum Kasner (2+2 split):", ks)
for kk in ks:
    if sp.N(kk[c1]) > 0:
        print("  alpha ~ tau^c1, c1 =", kk[c1], "=", sp.N(kk[c1]), "; Kretschmann ~ tau^-4 ~ alpha^(-4/c1) =",
              sp.nsimplify(-4 / kk[c1]), "=", sp.N(-4 / kk[c1]))
