"""DOCKET 67 audit re-derivation: maxwell-stress-energy-curved.
Independent sympy re-derivation (does not import drivensource.py).
Metric ds^2 = -e^{2Phi}dt^2 + e^{2Lam}dr^2 + R^2 dOmega^2, all of (t,r).
Source read: Carroll gr-qc/9712019 eqs (7.106)-(7.112), (7.107) T_mn=(1/4pi)(F_mr F_n^r - g F^2/4),
(1.111) printed with -1/(4pi); Bronnikov et al 2604.23741 eqs (2),(5),(6); Kubiznak et al 2605.01811 Thm 1."""
import sympy as sp, math, sys
fails = []
def chk(label, got, want=0):
    ok = sp.simplify(got - want) == 0
    print(("PASS " if ok else "FAIL ") + label + ("" if ok else "   got %s" % sp.simplify(got)))
    if not ok: fails.append(label)

t, r, th, ph = sp.symbols("t r theta phi", real=True)
x = [t, r, th, ph]
Phi, Lam, R = [sp.Function(n)(t, r) for n in ("Phi", "Lambda", "R")]
Q, P, M, mu = sp.symbols("Q P M mu", positive=True)
g = sp.diag(-sp.exp(2*Phi), sp.exp(2*Lam), R**2, R**2*sp.sin(th)**2)
gi = g.inv()
sg = sp.exp(Phi + Lam) * R**2 * sp.sin(th)          # sqrt(-g), 0<theta<pi
chk("sqrt(-g)^2 = -det g", sg**2 + g.det())

def maxwell_div(F):
    Fu = gi * F * gi
    return [sp.simplify(sum(sp.diff(sg*Fu[a, b], x[a]) for a in range(4))) for b in range(4)], Fu
def dF(F):   # cyclic d_[a F_bc]
    out = []
    for a in range(4):
        for b in range(a+1, 4):
            for c in range(b+1, 4):
                out.append(sp.simplify(sp.diff(F[b, c], x[a]) + sp.diff(F[c, a], x[b]) + sp.diff(F[a, b], x[c])))
    return out
def Tmaxwell(F, extra=None):
    Fu = gi*F*gi; F2 = sum(F[a, b]*Fu[a, b] for a in range(4) for b in range(4)); Fm = F*gi
    T = sp.Matrix(4, 4, lambda a, b: (sum(F[a, c]*Fm[b, c] for c in range(4)) - sp.Rational(1, 4)*g[a, b]*F2)/(4*sp.pi))
    if extra is not None: T = T + extra
    return T.applyfunc(sp.simplify)
def orth(T):
    return dict(rho=sp.simplify(T[0, 0]*sp.exp(-2*Phi)), j=sp.simplify(-T[0, 1]*sp.exp(-Phi-Lam)),
                p_r=sp.simplify(T[1, 1]*sp.exp(-2*Lam)), p_T=sp.simplify(T[2, 2]/R**2))

print("A. GENERAL F_tr = f(t,r): the curved Maxwell equations force sqrt(-g)F^{tr} = const*sin(theta)")
f = sp.Function("f")(t, r)
F = sp.zeros(4); F[0, 1] = f; F[1, 0] = -f
mx, Fu = maxwell_div(F)
G = sp.simplify(sg*Fu[0, 1]/sp.sin(th))   # the conserved flux density
print("   sqrt(-g) F^{tr}/sin(theta) =", G)
chk("   Maxwell b=t component is -d_r(G) sin(theta)", mx[0] + sp.diff(G, r)*sp.sin(th))
chk("   Maxwell b=r component is  d_t(G) sin(theta)", mx[1] - sp.diff(G, t)*sp.sin(th))
chk("   dF = 0 automatically for f(t,r) dt^dr", sum(abs(e) for e in dF(F)) if False else sum(e**2 for e in dF(F)))
print("   => G constant; tree's choice F_tr = Q e^{Phi+Lam}/R^2 corresponds to G = -Q")

print("\nB. THE TREE'S FIELD, reproduced independently")
Ftree = F.subs(f, Q*sp.exp(Phi+Lam)/R**2).doit()
mx, Fu = maxwell_div(Ftree)
chk("   all four curved Maxwell residuals vanish", sum(e**2 for e in mx))
gauss = sp.simplify(sg*Fu[0, 1])
print("   sqrt(-g) F^{tr} =", gauss, "  (tree comment line 302 says '= Q': DISCREPANCY of sign and sin(theta) factor)")
chk("   sqrt(-g) F^{tr} = -Q sin(theta)", gauss, -Q*sp.sin(th))
chk("   sqrt(-g) F^{rt} / sin(theta) = +Q  (the reading under which the comment holds)", sp.simplify(sg*Fu[1, 0]/sp.sin(th)), Q)
o = orth(Tmaxwell(Ftree))
chk("   rho = Q^2/(8 pi R^4)", o["rho"], Q**2/(8*sp.pi*R**4))
chk("   j = 0", o["j"]); chk("   p_r = -rho", o["p_r"] + o["rho"]); chk("   p_T = +rho", o["p_T"] - o["rho"])
chk("   Carroll sign: F_tr = -q/r^2 flat gives same T (T quadratic in Q)", sp.simplify(o["rho"].subs(Q, -Q) - o["rho"]))

print("\nC. THE DROPPED MAGNETIC COMPONENT (Carroll 7.108: F_thph = g(t,r) sin th is admitted)")
Pf = sp.Function("Pm")(t, r)
Fd = Ftree.copy(); Fd[2, 3] = Pf*sp.sin(th); Fd[3, 2] = -Fd[2, 3]
d = dF(Fd); print("   dF components:", d)
chk("   dF = 0 forces d_t Pm = 0 and d_r Pm = 0 (Bianchi)", sum(e**2 for e in d) - (sp.sin(th)**2)*(sp.diff(Pf, t)**2 + sp.diff(Pf, r)**2))
Fd = Fd.subs(Pf, P)
mx, _ = maxwell_div(Fd)
chk("   dyonic field with constant P satisfies d(sqrt(-g)F^{ab}) = 0", sum(e**2 for e in mx))
chk("   and dF = 0", sum(e**2 for e in dF(Fd)))
od = orth(Tmaxwell(Fd))
chk("   rho = (Q^2+P^2)/(8 pi R^4)", od["rho"], (Q**2+P**2)/(8*sp.pi*R**4))
chk("   j = 0", od["j"]); chk("   rho + p_r = 0 (radial NEC saturation survives)", od["rho"] + od["p_r"])
chk("   p_T = rho", od["p_T"] - od["rho"]); chk("   traceless", -od["rho"] + od["p_r"] + 2*od["p_T"])
U = sp.exp(-Phi)*sp.diff(R, t); W = sp.exp(-Lam)*sp.diff(R, r)
Dt = lambda h: sp.exp(-Phi)*sp.diff(h, t); Dr = lambda h: sp.exp(-Lam)*sp.diff(h, r)
m = M - (Q**2 + P**2)/(2*R)
chk("   MS-r with m = M-(Q^2+P^2)/2R, M const, arbitrary Phi,Lam,R", Dr(m) - 4*sp.pi*R**2*(od["rho"]*W + od["j"]*U))
chk("   MS-t likewise", Dt(m) + 4*sp.pi*R**2*(od["p_r"]*U + od["j"]*W))
print("   => the tree's 'ONLY F_tr' drops P; every conclusion holds with Q^2 -> Q^2 + P^2")

print("\nD. NORMALISATION: Gaussian T^{00} in flat space, sign of 1/(4 pi)")
E1, E2, E3, B1, B2, B3 = sp.symbols("E1 E2 E3 B1 B2 B3", real=True)
eta = sp.diag(-1, 1, 1, 1)
Fl = sp.Matrix([[0, -E1, -E2, -E3], [E1, 0, B3, -B2], [E2, -B3, 0, B1], [E3, B2, -B1, 0]])  # Carroll (1.58)
Flu = eta*Fl*eta; F2 = sum(Fl[a, b]*Flu[a, b] for a in range(4) for b in range(4))
T00 = lambda s: sp.simplify(s*(sum(Flu[0, l]*(Flu[0, :]*eta)[l] for l in range(4)) - sp.Rational(1, 4)*eta[0, 0]*F2)/(4*sp.pi))
U2 = (E1**2+E2**2+E3**2+B1**2+B2**2+B3**2)/(8*sp.pi)
chk("   with +1/(4pi) [Carroll 7.107, 8.25; tree line 316]: T^00 = (E^2+B^2)/8pi", T00(1), U2)
chk("   with -1/(4pi) [Carroll 1.111 as printed]: T^00 = -(E^2+B^2)/8pi  => 1.111 is a sign MISPRINT in the source, not in the tree", T00(-1), -U2)

print("\nE. SI bridge used downstream (X_of_Q): exterior energy of rho_SI = eps0 E^2/2")
eps0, a, rr = sp.symbols("epsilon0 a rr", positive=True)
rhoSI = eps0/2*(Q/(4*sp.pi*eps0*rr**2))**2
chk("   int_a^oo 4 pi r^2 rho_SI dr = Q^2/(8 pi eps0 a)", sp.integrate(4*sp.pi*rr**2*rhoSI, (rr, a, sp.oo)), Q**2/(8*sp.pi*eps0*a))

print("\nF. EXTENSION: nonlinear electrodynamics L(f), f = F_ab F^ab (Bronnikov 2604.23741 eq 5)")
Lf, Lv = sp.symbols("L_f L", real=True)       # arbitrary values at the point
Fd_u = gi*Fd*gi; Fmix = Fd*gi
Tmix = sp.Matrix(4, 4, lambda mu_, nu: -2*Lf*sum(Fd[mu_, al]*Fd_u[nu, al] for al in range(4)) + sp.Rational(1, 2)*sp.KroneckerDelta(mu_, nu)*Lv)
Tmix = Tmix.applyfunc(sp.simplify)
chk("   T^t_t = T^r_r for ANY L(f), dyonic, dynamical metric", Tmix[0, 0] - Tmix[1, 1])
chk("   T^t_r = 0 (no flux) for ANY L(f)", Tmix[1, 0])
fval = sp.simplify(sum(Fd[a_, b_]*Fd_u[a_, b_] for a_ in range(4) for b_ in range(4)))
print("   invariant f =", fval)
chk("   T^th_th + T^t_t = L - f L_f  (p_T = rho iff L linear in f, i.e. Maxwell)", Tmix[2, 2] + Tmix[0, 0], Lv - fval*Lf)
chk("   trace T^mu_mu = 2(L - f L_f)  (traceless iff Maxwell-type L = c f)", sum(Tmix[i, i] for i in range(4)), 2*(Lv - fval*Lf))

print("\nG. NAMED HYPOTHESIS m_gamma = 0: Proca term mu^2 (A_a A_b - g_ab A^2/2)/(4pi), electrostatic A = A_t dt")
At = sp.Function("A_t")(t, r)
A = sp.Matrix([At, 0, 0, 0]); Au = gi*A; A2 = (A.T*Au)[0]
Tp = sp.Matrix(4, 4, lambda a_, b_: mu**2*(A[a_]*A[b_] - g[a_, b_]*A2/2)/(4*sp.pi))
op = orth(Tp)
print("   Proca increment to rho + p_r =", sp.simplify(op["rho"] + op["p_r"]))
chk("   rho + p_r increment = mu^2 A_t^2 e^{-2Phi}/(4pi) >= 0 (moves AWAY from NEC violation)", op["rho"] + op["p_r"], mu**2*At**2*sp.exp(-2*Phi)/(4*sp.pi))
# magnitude at the read bound: m_gamma < 1e-18 eV (Ryutov 2007 via Goldhaber-Nieto 0809.1003 Table I)
hbarc_eVm = 1.973269804e-7
lam = hbarc_eVm/1e-18
print("   reduced Compton wavelength at 1e-18 eV: %.3e m (Goldhaber-Nieto quote ~2e11 m)" % lam)
for L in (1.0, 1e3, 6.4e6, 1.5e11):
    # rho+p_r over rho for Coulomb potential phi = Q/r, E = Q/r^2: ratio = 2 mu^2 r^2
    print("   r = %.1e m : (rho+p_r)/rho ~ 2(r/lambda)^2 = %.3e" % (L, 2*(L/lam)**2))

print("\nRESULT:", "ALL PASS" if not fails else "FAILURES: %s" % fails)
sys.exit(1 if fails else 0)
