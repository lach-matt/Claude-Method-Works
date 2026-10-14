"""DOCKET 67 audit gr-qc/9701064#k2 -- HPS source-term prefactor K^2 = 1/(5760 pi).

Independent of the tree: nothing is imported from research/warp-drive.
The HPS eqs. (5)-(7) NON-LOG brackets are transcribed here afresh from the
arXiv v1 PDF text layer (src/hps/hps_0.xml, pp.4-5).

Checks
 C1  exact arithmetic: 8 pi/(46080 pi^2) == 1/(5760 pi); 46080 = 8*5760.
 C2  K = 1/sqrt(5760 pi) l_P to 12 digits; the withdrawn typed 0.0074335.
 C3  HPS eq. (8), case f(0)=f''(0)=1, r''(0)=0: r(0) = 1/(2K) vs printed "~67 l_P".
 C4  HPS eq. (9), ln f(0) = -2/3: r(0) = sqrt(-16 K^2 ln f0) vs printed "~0.02 l_P".
 C5  TRACE vs CONFORMAL ANOMALY (the independent normalisation):
     tr = tt + ll + 2 thth of the non-log brackets, fitted (linear solve over
     arbitrary f(l), r(l)) as  a*Riem^2 + b*Ric^2 + c*R^2 + d*boxR.
     The conformal-scalar anomaly (heat-kernel a2 / (16 pi^2), xi = 1/6, hbar=1):
       <T> = (1/(2880 pi^2)) (Riem^2 - Ric^2 + boxR)       [MTW signs]
     and 8 pi <T> = K^2 * tr  =>  K^2 = 8 pi/(2880 pi^2 * a)  with a = -b = d, c = 0.
 C6  with hbar, G restored and N identical conformal scalars, K^2 = N l_P^2/(5760 pi);
     K in metres with CODATA 2018/2022 l_P.
"""
import sympy as sp

ok = True
def chk(name, cond, detail=""):
    global ok
    ok &= bool(cond)
    print(("PASS " if cond else "FAIL ") + name + ("  " + str(detail) if detail else ""))

pi = sp.pi
# C1
chk("C1 8 pi/(46080 pi^2) == 1/(5760 pi)", sp.simplify(8*pi/(46080*pi**2) - 1/(5760*pi)) == 0)
chk("C1 46080 == 8*5760", 46080 == 8*5760)
K2 = sp.Rational(1, 5760)/pi
K = sp.sqrt(K2)
Kn = sp.N(K, 15)
# C2
chk("C2 K = 1/sqrt(5760 pi) l_P", True, f"K = {Kn} l_P")
chk("C2 typed 0.0074335 differs in 5th significant digit", abs(float(Kn) - 0.0074335) > 5e-8,
    f"diff = {float(Kn)-0.0074335:.3e}; K rounds to {float(Kn):.7f}")
# C3
r0 = sp.symbols('r0', positive=True)
quart = -4*1*(1 + 0)*r0**4 + 0 + (1/K2 - 0)*r0**2 + 16*0   # eq (8), f0=f''0=1, r''0=0 (ln 1 = 0)
roots = [s for s in sp.solve(sp.Eq(quart, 0), r0)]
rC3 = [sp.N(s, 8) for s in roots]
chk("C3 eq.(8) root = 1/(2K) = 12 sqrt(10 pi) ~ 67 l_P (printed 'r(0) ~ 67 l_P')",
    any(abs(float(s) - 67) < 0.5 for s in rC3) and any(sp.simplify(s - 12*sp.sqrt(10*pi)) == 0 for s in roots),
    rC3)
# C4
rC4 = sp.sqrt(-16*K2*sp.Rational(-2, 3))
chk("C4 eq.(9) r(0) = sqrt(1/(540 pi)) ~ 0.024 l_P (printed 'r(0) ~ 0.02 l_P')",
    sp.simplify(rC4 - sp.sqrt(15)/(90*sp.sqrt(pi))) == 0 and round(float(rC4), 2) == 0.02, sp.N(rC4, 8))
# Alternative normalisations would miss the printed numbers:
for lab, k2alt in (("1/(2880 pi)", 1/(2880*pi)), ("1/(46080 pi^2)", 1/(46080*pi**2)), ("1/(720 pi)", 1/(720*pi))):
    print(f"      control: K^2 = {lab}: eq.(8) root = {float(1/(2*sp.sqrt(k2alt))):.4g} l_P, eq.(9) r0 = {float(sp.sqrt(sp.Rational(32,3)*k2alt)):.4g} l_P")

# C5 ------------------------------------------------------------------------
l, th, ph, t = sp.symbols('l theta phi t', real=True)
f = sp.Function('f')(l); r = sp.Function('r')(l)
X = [t, l, th, ph]
g = sp.diag(-f, 1, r**2, r**2*sp.sin(th)**2)
gi = g.inv()
n = 4
Gam = [[[sp.simplify(sum(gi[a, d]*(sp.diff(g[d, b], X[c]) + sp.diff(g[d, c], X[b]) - sp.diff(g[b, c], X[d]))
                         for d in range(n))/2) for c in range(n)] for b in range(n)] for a in range(n)]
def Riem(a, b, c, d):   # R^a_{bcd}, MTW
    e = sp.diff(Gam[a][b][d], X[c]) - sp.diff(Gam[a][b][c], X[d])
    e += sum(Gam[a][c][k]*Gam[k][b][d] - Gam[a][d][k]*Gam[k][b][c] for k in range(n))
    return sp.simplify(e)
R4 = [[[[Riem(a, b, c, d) for d in range(n)] for c in range(n)] for b in range(n)] for a in range(n)]
Ric = sp.Matrix(n, n, lambda b, d: sp.simplify(sum(R4[a][b][a][d] for a in range(n))))
Rs = sp.simplify(sum(gi[a, b]*Ric[a, b] for a in range(n) for b in range(n)))
# Riem^2 = R^a_bcd R_a^bcd ; diagonal metric makes index raising a product of diagonal factors
Riem2 = 0
for a in range(n):
    for b in range(n):
        for c in range(n):
            for d in range(n):
                v = R4[a][b][c][d]
                if v != 0:
                    Riem2 += v**2*g[a, a]*gi[b, b]*gi[c, c]*gi[d, d]
Riem2 = sp.simplify(Riem2)
Ric2 = sp.simplify(sum((gi[a, a]*Ric[a, b])*(gi[b, b]*Ric[b, a]) for a in range(n) for b in range(n)))
sqrtg = f**sp.Rational(1, 2)*r**2   # sqrt(-g)/sin(theta)
boxR = sp.simplify(sp.diff(sqrtg*sp.diff(Rs, l), l)/sqrtg)

F = [sp.diff(f, l, k) for k in range(5)]
Rr = [sp.diff(r, l, k) for k in range(5)]
f0, f1, f2, f3, f4 = F
r_, r1, r2, r3, r4 = Rr
tt = (32/r_**4 + 7*f1**4/f0**4 - 24*f1**3*r1/(f0**3*r_) + 24*f1**2*r1**2/(f0**2*r_**2) - 32*r1**4/r_**4
      + 4*f1**2*f2/f0**3 - 12*f2**2/f0**2 + 80*f1**2*r2/(f0**2*r_) - 160*f1*r1*r2/(f0*r_**2)
      + 128*r1**2*r2/r_**3 - 64*f2*r2/(f0*r_) + 32*r2**2/r_**2 - 16*f1*f3/f0**2 + 64*r1*f3/(f0*r_)
      - 96*f1*r3/(f0*r_) - 64*r1*r3/r_**2 + 16*f4/f0 - 64*r4/r_)
ll = (f1**4/f0**4 - 16*f1**3*r1/(f0**3*r_) + 64*f1*r1**3/(f0*r_**3) - 4*f1**2*f2/f0**3
      + 64*f1*r1*f2/(f0**2*r_) - 64*r1**2*f2/(f0*r_**2) - 4*f2**2/f0**2 - 48*f1**2*r2/(f0**2*r_)
      + 32*f1*r1*r2/(f0*r_**2) + 32*f2*r2/(f0*r_) + 8*f1*f3/f0**2 - 32*r1*f3/(f0*r_) - 32*f1*r3/(f0*r_))
thth = (17*f1**4/f0**4 - 16*f1**3*r1/(f0**3*r_) - 32*f1*r1**3/(f0*r_**3) - 52*f1**2*f2/f0**3
        + 32*f1*r1*f2/(f0**2*r_) + 32*r1**2*f2/(f0*r_**2) + 28*f2**2/f0**2 + 16*f1**2*r2/(f0**2*r_)
        + 64*f1*r1*r2/(f0*r_**2) - 32*f2*r2/(f0*r_) + 24*f1*f3/f0**2 - 48*r1*f3/(f0*r_)
        + 32*f1*r3/(f0*r_) - 16*f4/f0)
tr = tt + ll + 2*thth

a, b, c, d = sp.symbols('a b c d')
expr = sp.expand(sp.simplify((tr - (a*Riem2 + b*Ric2 + c*Rs**2 + d*boxR))*f**4*r**4))
# collect over derivative monomials
syms = sp.symbols('F0:5 S0:5')
rep = {}
for k in range(4, -1, -1):
    rep[sp.diff(f, l, k) if k else f] = syms[k]
    rep[sp.diff(r, l, k) if k else r] = syms[5+k]
e2 = sp.expand(expr.subs(rep))
eqs = sp.Poly(e2, *syms).coeffs()
sol = sp.solve(eqs, [a, b, c, d], dict=True)
print("      trace fit:", sol)
chk("C5 trace of non-log part is a curvature invariant (linear fit solvable)", len(sol) == 1)
if sol:
    s = sol[0]
    chk("C5 structure a = -b = d, c = 0 (Riem^2 - Ric^2 + boxR, the conformal-scalar anomaly)",
        s[a] == -s[b] == s[d] and s[c] == 0, s)
    K2_from_anomaly = sp.simplify(8*pi/(2880*pi**2*s[a]))
    chk("C5 K^2 fixed by the anomaly coefficient 1/(2880 pi^2) equals HPS's printed 1/(5760 pi)",
        sp.simplify(K2_from_anomaly - K2) == 0, K2_from_anomaly)
    # sign check: a > 0 means <T> = +(1/2880 pi^2)(Riem^2 - Ric^2 + boxR) in MTW signs
    print("      overall sign of Riem^2 coefficient in 8 pi <T> / K^2:", sp.sign(s[a]))
# C6
lP = {"CODATA2018": 1.616255e-35, "CODATA2022": 1.616255e-35}
for k_, v in lP.items():
    print(f"      K = {float(Kn)*v:.6e} m  ({k_} l_P = {v} m)")
print("      N identical conformal scalars: K^2 -> N/(5760 pi); K -> sqrt(N) K; eq.(8) root -> 67.26/sqrt(N) l_P")
print("ALL PASS" if ok else "SOME FAIL")
import sys; sys.exit(0 if ok else 1)
