#!/usr/bin/env python3
"""DOCKET 67 -- re-derivation for key frw-metric-k-minus1-and-k0.

Source forms (READ at alphaXiv):
  Baumann 0907.5424v2 eq.(1)-(3), (105)-(106):
     ds^2 = -dt^2 + a^2 [dr^2/(1-k r^2) + r^2 dOmega^2]
          = -dt^2 + a^2 [dchi^2 + S_k(chi)^2 dOmega^2],  S = sinh, chi, sin for k=-1,0,+1
  Ellis & van Elst gr-qc/9812046v5 eq.(104)-(105): same, f(r)=sin r, r, sinh r; u^a = delta^a_0;
     3-spaces of constant curvature 6k/S^2 (Ricci scalar); Milne = S(t)=t, k=-1, flat empty (sec 4.3.1c).
Tree form (nonstatic.py:405, 450-451): g = diag(-e^{2Phi}, e^{2Lam}, R^2, R^2 sin^2) with
     Phi=0, Lam=log a, R = a sinh chi (k=-1) or a chi (k=0).
Nothing here edits research/.  Exit 0 iff every check passes.
"""
import sys
import sympy as sp

FAIL = []
def chk(label, cond):
    ok = bool(cond)
    print(("PASS " if ok else "FAIL ") + label)
    if not ok:
        FAIL.append(label)

t, chi, th, ph, r = sp.symbols("t chi theta phi r", positive=True)
a = sp.Function("a", positive=True)(t)
ad, add = sp.diff(a, t), sp.diff(a, t, 2)

def iszero(e):
    """sympy's simplify leaves some sinh/tanh and sin/tan identities unreduced;
    rewrite to exponentials before deciding zero."""
    e = sp.simplify(e)
    return e == 0 or sp.simplify(sp.expand(e.rewrite(sp.exp))) == 0

def geom(g, x):
    n = len(x)
    gi = sp.simplify(g.inv())
    Gm = [[[sp.simplify(sum(gi[i, d] * (sp.diff(g[d, j], x[k]) + sp.diff(g[d, k], x[j])
                                        - sp.diff(g[j, k], x[d])) for d in range(n)) / 2)
            for k in range(n)] for j in range(n)] for i in range(n)]
    Riem = {}
    def R4(i, j, k, l):   # R^i_{jkl}
        key = (i, j, k, l)
        if key not in Riem:
            s = sp.diff(Gm[i][j][l], x[k]) - sp.diff(Gm[i][j][k], x[l])
            for m in range(n):
                s += Gm[i][k][m] * Gm[m][j][l] - Gm[i][l][m] * Gm[m][j][k]
            Riem[key] = sp.simplify(s)
        return Riem[key]
    Ric = sp.Matrix(n, n, lambda j, l: sp.simplify(sum(R4(i, j, i, l) for i in range(n))))
    Rs = sp.simplify(sum(gi[i, j] * Ric[i, j] for i in range(n) for j in range(n)))
    return gi, Gm, R4, Ric, Rs

S = {-1: sp.sinh(chi), 0: chi}
print("=== C1  chi-form <-> r-form (Baumann eq.2-3; Ellis eq.105): r = S_k(chi) ===")
for k in (-1, 0):
    rr = S[k]
    # dr^2/(1-k r^2) must equal dchi^2
    chk("k=%d: (dr/dchi)^2/(1-k r^2) = 1" % k, sp.simplify(sp.diff(rr, chi)**2 / (1 - k * rr**2) - 1) == 0)

print("=== C2  Einstein tensor of the tree's metric (nonstatic.py:405,450-451), any a(t) ===")
res = {}
for k in (-1, 0):
    x = [t, chi, th, ph]
    R = a * S[k]
    g = sp.diag(-1, a**2, R**2, R**2 * sp.sin(th)**2)
    gi, Gm, R4, Ric, Rs = geom(g, x)
    Ein = sp.simplify(Ric - Rs * g / 2)
    T = Ein / (8 * sp.pi)
    rho = sp.simplify(T[0, 0])
    j = sp.simplify(-T[0, 1] / a)
    p_r = sp.simplify(T[1, 1] / a**2)
    p_T = sp.simplify(T[2, 2] / R**2)
    rho_src = 3 * (ad**2 + k) / (8 * sp.pi * a**2)            # Baumann (110), Ellis (107)
    p_src = -(2 * a * add + ad**2 + k) / (8 * sp.pi * a**2)    # from Baumann (110)+(111)
    chk("k=%d: rho = 3(adot^2+k)/(8 pi a^2)" % k, sp.simplify(rho - rho_src) == 0)
    chk("k=%d: p_r = p_T = -(2 a addot + adot^2 + k)/(8 pi a^2)  (perfect fluid, isotropic)" % k,
        sp.simplify(p_r - p_src) == 0 and sp.simplify(p_T - p_src) == 0)
    chk("k=%d: j = T_{t chi} = 0 (no flux; comoving u = d/dt)" % k, j == 0)
    off = [sp.simplify(Ein[i, jj]) for i in range(4) for jj in range(4) if i != jj]
    chk("k=%d: Einstein tensor diagonal" % k, all(o == 0 for o in off))
    # acceleration equation Baumann (111)
    chk("k=%d: addot/a = -(4 pi/3)(rho + 3p)" % k, sp.simplify(add / a + 4 * sp.pi / 3 * (rho + 3 * p_r)) == 0)
    # Ricci scalar vs Baumann (109)
    chk("k=%d: R = 6[addot/a + adot^2/a^2 + k/a^2] (Baumann 109, scalar)" % k,
        sp.simplify(Rs - 6 * (add / a + ad**2 / a**2 + k / a**2)) == 0)
    chk("k=%d: R_tt = -3 addot/a (Baumann 109)" % k, sp.simplify(Ric[0, 0] + 3 * add / a) == 0)
    Rchichi = sp.simplify(Ric[1, 1])
    chk("k=%d: R_chichi = (a addot + 2 adot^2 + 2k) gamma_chichi, gamma_chichi = 1" % k,
        sp.simplify(Rchichi - (a * add + 2 * ad**2 + 2 * k)) == 0)
    # geodesic threading: u = d/dt, Gamma^i_tt = 0
    chk("k=%d: comoving worldlines geodesic (Gamma^i_tt = 0)" % k, all(Gm[i][0][0] == 0 for i in range(4)))
    # frame variables as the tree defines them
    W = sp.simplify(sp.diff(R, chi) / a)
    U = sp.simplify(sp.diff(R, t))
    m = sp.simplify(R / 2 * (1 - W**2 + U**2))
    m3 = sp.simplify(R / 2 * (1 - W**2))
    res[k] = dict(W=W, m=m, m3=m3, rho=rho, R=R)
    chk("k=%d: m = (4 pi/3) rho R^3 exactly" % k, sp.simplify(m - sp.Rational(4, 3) * sp.pi * rho * R**3) == 0)
    # Baumann (109) R_ij = delta_ij[2 adot^2 + a addot + 2k/a^2]: check its k-term against the r-form
    if k == -1:
        xr = [t, r, th, ph]
        gr = sp.diag(-1, a**2 / (1 - k * r**2), a**2 * r**2, a**2 * r**2 * sp.sin(th)**2)
        _, _, _, Ricr, Rsr = geom(gr, xr)
        Rrr = sp.simplify(Ricr[1, 1])
        correct = sp.simplify(Rrr - (a * add + 2 * ad**2 + 2 * k) / (1 - k * r**2)) == 0
        printed = sp.simplify(Rrr - (2 * ad**2 + a * add + 2 * sp.Integer(k) / a**2)) == 0
        chk("k=-1 r-form: R_rr = (a addot + 2 adot^2 + 2k)/(1 - k r^2)", correct)
        chk("DISCREPANCY RECORDED (not an error in the tree): Baumann (109) R_ij as printed "
            "[delta_ij(2adot^2 + a addot + 2k/a^2)] does NOT equal R_rr for k=-1", not printed)
        chk("k=-1 r-form: Ricci scalar agrees with chi-form", sp.simplify(Rsr - Rs) == 0)

print("=== C3  frame values the tree prints (nonstatic.py:98-107, 657-659) ===")
chk("k=-1: W = cosh chi", sp.simplify(res[-1]["W"] - sp.cosh(chi)) == 0)
chk("k= 0: W = 1 exactly", sp.simplify(res[0]["W"] - 1) == 0)
chk("k= 0: m3 = 0 exactly", sp.simplify(res[0]["m3"]) == 0)
chk("k=-1: m3 = -a sinh^3(chi)/2", sp.simplify(res[-1]["m3"] + a * sp.sinh(chi)**3 / 2) == 0)
chk("k=-1: m = a sinh^3(chi)(adot^2 - 1)/2", sp.simplify(res[-1]["m"] - a * sp.sinh(chi)**3 * (ad**2 - 1) / 2) == 0)

print("=== C4  sign of rho: the metric does NOT fix it (hypothesis at nonstatic.py:98-99) ===")
rho_m1 = res[-1]["rho"]
cases = {"a = 2 + t/2 (adot^2 = 1/4 < 1)": 2 + t / 2, "a = t (Milne, adot = 1)": t,
         "a = t^(2/3)+t (adot^2 > 1)": t**sp.Rational(2, 3) + t}
for lab, af in cases.items():
    v = sp.simplify(rho_m1.subs(a, af).doit())
    print("     k=-1, %-32s rho = %s" % (lab, v))
v1 = sp.simplify(rho_m1.subs(a, 2 + t / 2).doit())
chk("k=-1 counter-case: general a(t) admits rho < 0 (a = 2 + t/2)", sp.simplify(v1 + sp.Rational(9, 8) / (sp.pi * (t + 4)**2) * 4) == 0 or v1.is_negative)
chk("k=-1 Milne a = t: rho = 0", sp.simplify(rho_m1.subs(a, t).doit()) == 0)
# open dust: adot^2 = 1 + C/a  -> rho = 3C/(8 pi a^3) > 0
C = sp.Symbol("C", positive=True)
rd = sp.simplify(rho_m1.subs(sp.Derivative(a, t), sp.sqrt(1 + C / a)))
chk("k=-1 dust (adot^2 = 1 + C/a): rho = 3C/(8 pi a^3) > 0", sp.simplify(rd - 3 * C / (8 * sp.pi * a**3)) == 0)
chk("k= 0: rho = 3 adot^2/(8 pi a^2) >= 0 for every a(t)", sp.simplify(res[0]["rho"] - 3 * ad**2 / (8 * sp.pi * a**2)) == 0)

print("=== C5  slices are spaces of constant curvature k/a^2 (Ellis 4.1 item 2) ===")
for k in (-1, 0):
    A = sp.Symbol("A", positive=True)   # a at fixed t
    x3 = [chi, th, ph]
    h = sp.diag(A**2, A**2 * S[k]**2, A**2 * S[k]**2 * sp.sin(th)**2)
    hi, _, R3, Ric3, Rs3 = geom(h, x3)
    Kc = sp.Rational(k) / A**2
    okc = True
    for i in range(3):
        for j2 in range(3):
            for kk in range(3):
                for l in range(3):
                    lower = sp.simplify(sum(h[i, m] * R3(m, j2, kk, l) for m in range(3)))
                    want = Kc * (h[i, kk] * h[j2, l] - h[i, l] * h[j2, kk])
                    if not iszero(lower - want):
                        okc = False
    chk("k=%d: R_ijkl = (k/a^2)(h_ik h_jl - h_il h_jk)" % k, okc)
    chk("k=%d: 3-Ricci scalar = 6k/a^2 (Ellis eq.107)" % k, sp.simplify(Rs3 - 6 * Kc) == 0)

print("=== C6  Milne (tree nonstatic.py:449) is the k=-1 form at a = t, and is flat (Ellis 4.3.1c) ===")
x = [t, chi, th, ph]
Rm = t * sp.sinh(chi)
gm = sp.diag(-1, t**2, Rm**2, Rm**2 * sp.sin(th)**2)
_, _, R4m, _, _ = geom(gm, x)
flat = all(iszero(R4m(i, j2, kk, l)) for i in range(4) for j2 in range(4) for kk in range(4) for l in range(4))
chk("Milne a = t, k=-1: full Riemann tensor = 0", flat)
# k=0 with a = const is also flat; k=-1 with a = const is NOT vacuum
A0 = sp.Symbol("A0", positive=True)
chk("k=-1, a = const: rho = -3/(8 pi a^2) < 0 (not vacuum)", sp.simplify(rho_m1.subs(a, A0).doit() + 3 / (8 * sp.pi * A0**2)) == 0)

print("=== C7  normalisation: any k<0 rescales to k=-1 (Ellis 'k can be normalised to +-1') ===")
kk_, L = sp.symbols("kappa L", positive=True)   # k = -kappa
# a^2 [dr^2/(1+kappa r^2) + r^2 dOmega^2]; r = s/sqrt(kappa), a -> a/sqrt(kappa)
s = sp.Symbol("s", positive=True)
lhs = (a**2) * (1 / (1 + kk_ * r**2)) * sp.diff(s / sp.sqrt(kk_), s)**2
lhs = sp.simplify(lhs.subs(r, s / sp.sqrt(kk_)))
rhs = (a / sp.sqrt(kk_))**2 / (1 + s**2)
chk("k=-kappa rescales to k=-1 with a' = a/sqrt(kappa)", sp.simplify(lhs - rhs) == 0)

print()
print("RESULT: %d FAIL" % len(FAIL))
sys.exit(1 if FAIL else 0)
