# Checks for Part VI.B' (PART-VI3-TRAPPING.md): the separation of the null geodesic flow of five-dimensional
# Myers-Perry in III.B's Kerr-Schild form, in spheroidal coordinates with Kerr-Schild time, and the radial structure.
#   S1  rho^2 g^{-1}(p,p) = A(r; p_r, E, Phi, Psi) + K(theta; p_theta, E, Phi, Psi), numerically (40 digits) from III.B's
#       Cartesian definitions, with Phi = zeta(J12 x), Psi = zeta(J34 x), and E~ = E + zeta(M A x / P) = E + p_r-free part.
#   S2  the radial function R = beta^2 - alpha (gamma + K): u P R is a polynomial of degree 5 in u = r^2; at A = 0 it is
#       u^3 (u^2 E^2 - (u - mu) K); Q(w) := w^5 (u P R)(1/w) has Q(0) = E^2 and, at A = 0, Q = E^2 - K w + mu K w^2.
#   S3  off shell: H_A r = 2 p~, H_A p~ = d_r R + (alpha'/alpha)(p~^2 - R), p~ := alpha p_r + beta.
#   S4  phi_pm := p~ -/+ (r - r_c) sqrt(S), R = m + (r - r_c)^2 S: on {p~^2 = R}, H phi_+ = -2T phi_+, H phi_- = 2T phi_-.
#   S5  numbers at b_0 (mu = 1, E^2 = 1): r_c^2 = K/2, m = K (mu - K/4), d^2_r R = 16 mu, rate 4 (2 mu)^{-1/2},
#       {phi_+, phi_-} = 2 alpha sqrt(S) at Gamma.
#   S6  sampled margins of Lemma 1.1 (convexity of Q, positivity for small Lambda) and of the ellipticity in Lemma 3.2.
import sympy as sp, mpmath as mm, random
mm.mp.dps = 40
random.seed(5)

# ---------------- S1 ----------------
def ginv_cart(mu, a, b, r, th, ph, ps, E, pr, pth, Phi_c, Psi_c):
    s = a*a + b*b
    X = mm.matrix([mm.sqrt(r*r+a*a)*mm.sin(th)*mm.cos(ph), mm.sqrt(r*r+a*a)*mm.sin(th)*mm.sin(ph),
                   mm.sqrt(r*r+b*b)*mm.cos(th)*mm.cos(ps), mm.sqrt(r*r+b*b)*mm.cos(th)*mm.sin(ps)])
    A = mm.zeros(4); A[0,1] = a; A[1,0] = -a; A[2,3] = b; A[3,2] = -b
    P = (r*r+a*a)*(r*r+b*b); M = (r*r+s)*mm.eye(4) + A*A
    Q = P - (X.T*M*X)[0]; assert abs(Q) < mm.mpf(10)**-30           # r_A(x) = r
    ell = M*(r*mm.eye(4)+A)*X/P
    F = 1 + (X.T*A*A*M*M*X)[0]/P**2; H = mu*r*r/(P*F)
    # Jacobian dx/d(r, th, ph, ps)
    J = mm.zeros(4)
    ca, cb = mm.sqrt(r*r+a*a), mm.sqrt(r*r+b*b)
    J[0,0] = r/ca*mm.sin(th)*mm.cos(ph); J[1,0] = r/ca*mm.sin(th)*mm.sin(ph)
    J[2,0] = r/cb*mm.cos(th)*mm.cos(ps); J[3,0] = r/cb*mm.cos(th)*mm.sin(ps)
    J[0,1] = ca*mm.cos(th)*mm.cos(ph); J[1,1] = ca*mm.cos(th)*mm.sin(ph)
    J[2,1] = -cb*mm.sin(th)*mm.cos(ps); J[3,1] = -cb*mm.sin(th)*mm.sin(ps)
    J[0,2] = -ca*mm.sin(th)*mm.sin(ph); J[1,2] = ca*mm.sin(th)*mm.cos(ph)
    J[2,3] = -cb*mm.cos(th)*mm.sin(ps); J[3,3] = cb*mm.cos(th)*mm.cos(ps)
    # Phi_c, Psi_c are the conjugate momenta of phi, psi
    q = mm.matrix([pr, pth, Phi_c, Psi_c])
    zeta = (J.T)**-1*q
    G = -E*E + sum(zeta[i]**2 for i in range(4)) - H*(E + sum(ell[i]*zeta[i] for i in range(4)))**2
    J12 = mm.zeros(4); J12[0,1] = 1; J12[1,0] = -1; J34 = mm.zeros(4); J34[2,3] = 1; J34[3,2] = -1
    Phi = (zeta.T*J12*X)[0]; Psi = (zeta.T*J34*X)[0]
    Et_frame = E + (zeta.T*M*A*X)[0]/P                               # E + zeta(M A x / P)
    return G, Phi, Psi, Et_frame

def sep(mu, a, b, r, th, E, pr, pth, Phi, Psi):
    s = a*a + b*b; P = (r*r+a*a)*(r*r+b*b); Del = P - mu*r*r
    Et = E + a*Phi/(r*r+a*a) + b*Psi/(r*r+b*b)
    T = (a*a-b*b)*(Phi**2/(r*r+a*a) - Psi**2/(r*r+b*b))
    Afun = P/(r*r)*pr**2 - r*r*E*E - T - mu*(E + pr + a*Phi/(r*r+a*a) + b*Psi/(r*r+b*b))**2
    K = pth**2 + Phi**2/mm.sin(th)**2 + Psi**2/mm.cos(th)**2 - E*E*(a*a*mm.cos(th)**2 + b*b*mm.sin(th)**2)
    rho2 = r*r + a*a*mm.cos(th)**2 + b*b*mm.sin(th)**2
    alpha = Del/(r*r); beta = -mu*Et; gamma = -r*r*E*E - T - mu*Et**2
    R = beta**2 - alpha*(gamma + K)
    pt = alpha*pr + beta
    return Afun, K, rho2, R, pt, alpha

worst = 0
for trial in range(12):
    mu = mm.mpf(1) + mm.mpf(random.random())/5
    a = mm.mpf(random.uniform(-.3, .3)); b = mm.mpf(random.uniform(-.3, .3))
    r = mm.mpf(random.uniform(1.2, 3)); th = mm.mpf(random.uniform(.2, 1.3))
    ph = mm.mpf(random.uniform(0, 6)); ps = mm.mpf(random.uniform(0, 6))
    E = mm.mpf(random.choice([1, -1])); pr = mm.mpf(random.uniform(-2, 2)); pth = mm.mpf(random.uniform(-2, 2))
    Phc = mm.mpf(random.uniform(-2, 2)); Psc = mm.mpf(random.uniform(-2, 2))
    G, Phi, Psi, Etf = ginv_cart(mu, a, b, r, th, ph, ps, E, pr, pth, Phc, Psc)
    # orientation: zeta(J12 x) = -Phi_c with J12 = E12 - E21; the identity below is written in Phi := zeta(J12 x)
    assert abs(Phi + Phc) < mm.mpf(10)**-30 and abs(Psi + Psc) < mm.mpf(10)**-30
    Afun, K, rho2, R, pt, alpha = sep(mu, a, b, r, th, E, pr, pth, Phi, Psi)
    worst = max(worst, abs(rho2*G - (Afun + K)))
    # frame-free E~ = E + zeta(M A x/P) equals E + a Phi/(r^2+a^2) + b Psi/(r^2+b^2)
    assert abs(Etf - (E + a*Phi/(r*r+a*a) + b*Psi/(r*r+b*b))) < mm.mpf(10)**-30
    # on the level {A + K = 0}: p~^2 = R  <=>  alpha (A + K) = p~^2 - R
    assert abs(alpha*(Afun + K) - (pt**2 - R)) < mm.mpf(10)**-28
assert worst < mm.mpf(10)**-28, worst
print('S1 separation rho^2 g^-1 = A + K: max error', mm.nstr(worst, 3))

# ---------------- S2 ----------------
u, a, b, mu, E, Ph, Ps, K, w = sp.symbols('u a b mu E Phi Psi K w', real=True)
P = (u+a**2)*(u+b**2); Del = P - mu*u
Et = E + a*Ph/(u+a**2) + b*Ps/(u+b**2)
T = (a**2-b**2)*(Ph**2/(u+a**2) - Ps**2/(u+b**2))
alpha = Del/u; beta = -mu*Et; gamma = -u*E**2 - T - mu*Et**2
R = beta**2 - alpha*(gamma + K)
Pol = sp.factor(sp.together(u*P*R))
Pol = sp.expand(sp.cancel(u*P*R))
assert sp.Poly(Pol, u).degree() == 5
Pol_formula = sp.expand(mu*(P*E + a*Ph*(u+b**2) + b*Ps*(u+a**2))**2
                        + Del*(u*P*E**2 + (a**2-b**2)*(Ph**2*(u+b**2) - Ps**2*(u+a**2)) - K*P))
assert sp.expand(Pol - Pol_formula) == 0
assert sp.expand(Pol.subs({a: 0, b: 0}) - u**3*(u**2*E**2 - (u-mu)*K)) == 0
Qw = sp.expand(w**5*Pol.subs(u, 1/w))
assert sp.Poly(Qw, w).degree() <= 5 and sp.expand(Qw.subs(w, 0) - E**2) == 0
assert sp.expand(Qw.subs({a: 0, b: 0}) - (E**2 - K*w + mu*K*w**2)) == 0
print('S2 radial polynomial: degree 5 in u, Q(0) = E^2, Q = E^2 - K w + mu K w^2 at A = 0')

# ---------------- S3 ----------------
r, pr_ = sp.symbols('r p_r', real=True)
al, be, ga = sp.Function('alpha')(r), sp.Function('beta')(r), sp.Function('gamma')(r)
Afun = al*pr_**2 + 2*be*pr_ + ga
pt = al*pr_ + be
Rr = be**2 - al*(ga + K)
Hr = sp.diff(Afun, pr_)                                  # H_A r
Hpt = sp.diff(Afun, pr_)*sp.diff(pt, r) - sp.diff(Afun, r)*sp.diff(pt, pr_)
assert sp.simplify(Hr - 2*pt) == 0
assert sp.simplify(Hpt - (sp.diff(Rr, r) + sp.diff(al, r)/al*(pt**2 - Rr))) == 0
print('S3 H r = 2 p~, H p~ = d_r R + (alpha\'/alpha)(p~^2 - R)')

# ---------------- S4 ----------------
rc, m = sp.symbols('r_c m', real=True)
S = sp.Function('S')(r)
sq = sp.sqrt(S)
Rr2 = m + (r-rc)**2*S
X = (r-rc)*sq; Tt = sp.diff(X, r)
for sgn in (1, -1):
    phi_ = sp.Symbol('phi')          # phi = p~ - sgn X  ->  p~ = phi + sgn X
    ptil = phi_ + sgn*X
    H = sp.diff(Rr2, r) - sgn*2*ptil*Tt        # H phi = H p~ - sgn H X, H r = 2 p~, on shell H p~ = d_r R
    assert sp.simplify(H - (-sgn*2*Tt*phi_)) == 0
print('S4 H phi_pm = -/+ 2 T phi_pm on the characteristic set')

# ---------------- S5 ----------------
r, K = sp.symbols('r K', positive=True)
mu0 = sp.Integer(1)
R0 = r**4 - K*(r**2 - mu0)
rc0 = sp.sqrt(K/2)
assert sp.simplify(sp.diff(R0, r).subs(r, rc0)) == 0
m0 = sp.simplify(R0.subs(r, rc0)); assert sp.simplify(m0 - K*(mu0 - K/4)) == 0
assert sp.simplify(sp.diff(m0, K).subs(K, 4)) == -1
Rrr = sp.simplify(sp.diff(R0, r, 2).subs({K: 4, r: sp.sqrt(2)})); assert Rrr == 16
S0 = sp.simplify(((R0 - m0)/(r - rc0)**2).subs(K, 4)); assert sp.simplify(S0 - (r + sp.sqrt(2))**2) == 0
rate = sp.sqrt(2*Rrr)/2                      # 2 sqrt(S) / rho^2 with rho^2 = r_ph^2 = 2
assert sp.simplify(rate - 4/sp.sqrt(2)) == 0
bracket = 2*(2 - 1)*sp.sqrt(sp.limit(S0, r, sp.sqrt(2)))   # 2 alpha sqrt(S), alpha = r^2 - mu
assert sp.simplify(bracket - 4*sp.sqrt(2)) == 0
print('S5 b_0: r_c^2 = K/2, m = K(mu - K/4), R_rr = 16 mu, S = (r + r_c)^2, rate 4 (2mu)^-1/2, bracket 4 mu sqrt(2 mu)')

# ---------------- S6 ----------------
u, a, b, muS, E, Ph, Ps, Lam, w = sp.symbols('u a b mu E Phi Psi Lambda w', real=True)
Kfrom = Lam - (a**2+b**2)*E**2                     # K = Lambda - s E^2
QwS = sp.expand(Qw.subs({sp.Symbol('K', real=True): Kfrom}).subs(sp.Symbol('mu', real=True), muS))
Qf = sp.lambdify((a, b, muS, E, Ph, Ps, Lam, w), QwS, 'mpmath')
Qf2 = sp.lambdify((a, b, muS, E, Ph, Ps, Lam, w), sp.diff(QwS, w, 2), 'mpmath')
kappa0 = mm.mpf(1)/6; minconv = mm.inf; minpos = mm.inf
for trial in range(3000):
    epsA = .02
    a_ = mm.mpf(random.uniform(-epsA, epsA)); b_ = mm.mpf(random.uniform(-epsA, epsA))
    mu_ = mm.mpf(random.uniform(.9, 1.1))
    Lam_ = mm.mpf(random.random())                    # normalised E^2 + Lambda/mu0 = 1, mu0 = 1
    E_ = mm.sqrt(1 - Lam_)*random.choice([1, -1])
    t = random.random(); f = mm.sqrt(Lam_)*t; g = mm.sqrt(Lam_)*(1-t)  # (|Phi| + |Psi|)^2 <= Lambda
    Ph_ = f*random.choice([1, -1]); Ps_ = g*random.choice([1, -1])
    w_ = mm.mpf(random.uniform(0, 2))
    if Lam_ >= kappa0:
        minconv = min(minconv, Qf2(a_, b_, mu_, E_, Ph_, Ps_, Lam_, w_))
    else:
        minpos = min(minpos, Qf(a_, b_, mu_, E_, Ph_, Ps_, Lam_, w_))
assert minconv > 0 and minpos > 0
print('S6 sampled, |A| <= 0.02: min Q\'\' (Lambda >= mu0/6) =', mm.nstr(minconv, 4), '; min Q (Lambda < mu0/6) =',
      mm.nstr(minpos, 4))
# ellipticity of the singular orbits of H_K (Lemma 3.2): on the shell 3 mu <= K <= 5 mu,
# U'' >= 2(Phi^2/sin^2 + Psi^2/cos^2) - 2|a^2 - b^2| > 0 and Psi^2 + a^2 - b^2 > 0 on the circle
th = sp.Symbol('theta')
U = Ph**2/sp.sin(th)**2 + Ps**2/sp.cos(th)**2 - a**2 + (a**2 - b**2)*sp.sin(th)**2
low = 2*Ph**2/sp.sin(th)**2 + 2*Ps**2/sp.cos(th)**2 + 2*(a**2-b**2)*sp.cos(2*th)
assert sp.simplify(sp.diff(U, th, 2) - low - 6*Ph**2*sp.cos(th)**2/sp.sin(th)**4
                   - 6*Ps**2*sp.sin(th)**2/sp.cos(th)**4) == 0
U2f = sp.lambdify((a, b, Ph, Ps, th), sp.diff(U, th, 2), 'mpmath')
lowf = sp.lambdify((a, b, Ph, Ps, th), 2*Ph**2/sp.sin(th)**2 + 2*Ps**2/sp.cos(th)**2 - 2*abs(a**2-b**2), 'mpmath')
for trial in range(2000):
    a_ = mm.mpf(random.uniform(-.02, .02)); b_ = mm.mpf(random.uniform(-.02, .02))
    th_ = mm.mpf(random.uniform(.01, 1.56)); Ph_ = mm.mpf(random.uniform(-3, 3)); Ps_ = mm.mpf(random.uniform(-3, 3))
    assert U2f(a_, b_, Ph_, Ps_, th_) >= lowf(a_, b_, Ph_, Ps_, th_) - mm.mpf(10)**-25
print('S6 U\'\' >= 2(Phi^2/sin^2 + Psi^2/cos^2) - 2|a^2 - b^2| (sampled)')
print('trap5 checks pass')
